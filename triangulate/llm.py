"""DeepSeek 调用：OpenAI 兼容 chat/completions，非思考模式 + JSON 输出。改编自 fanout-ledger/llm.py，换成标准库 urllib。

每次调用记一行到 results/calls.jsonl：arm、题 id、第几次尝试、token、延迟、finish_reason、估算 USD。
日志里不记 prompt、不记回复内容、不记 key。
"""
import json
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .config import API_URL, CALLS, MODEL, read_key, usd_cost

RETRY_STATUS = {429, 500, 502, 503, 504}
TOTAL_TIMEOUT_S = 1200
_LOG_LOCK = threading.Lock()


class KeyRejected(RuntimeError):
    pass


class TransportError(RuntimeError):
    """服务端没给出可解析的回复（超时、5xx、空 body）。不算模型的输出问题，不占用「输出无效重试一次」的名额；
    runner 不保存这道题，之后再跑 run 会补上。"""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """不跟随跳转（v2.6g，D9）。urllib 默认把 POST 的 301/302/303 改成 GET 跟到 Location，并把 Authorization、
    x-api-key 这些请求头原样带过去。这里不生成新请求，urllib 就把 3xx 当作 HTTPError 抛出（e.code 是 3xx）。"""

    def redirect_request(self, *args, **kwargs):
        return None


_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirect)


def urlopen_no_redirect(req, timeout: float):
    """同 urllib.request.urlopen(req, timeout=timeout)，只是不跟随跳转。带 key 的请求都走这里：
    本模块的 LLM、agent/search.py 的 Searcher、search_direct.py 的 DirectClient、agent/jev.py
    （另有手动探针 probes/deepseek_search_probe.py）。前四处都在调用时按 llm.urlopen_no_redirect 取这个函数，
    测试换掉这一个名字就能拦下这四处的 HTTP。"""
    return _NO_REDIRECT_OPENER.open(req, timeout=timeout)


class LLM:
    def __init__(self, calls_path=CALLS, model: str = MODEL):
        self.model = model
        self.calls_path = calls_path
        self._key = read_key()

    def json_call(self, messages: list, *, arm: str, qid: str, attempt: int, max_tokens: int = 4000):
        """返回 (parsed_dict_or_None, raw_text, error_or_None)，error 只表示模型输出本身的问题。
        传输层失败（超时、5xx、空 body）内部重试最多 3 次，仍失败则抛 TransportError。
        3xx 跳转不跟随、不重试，直接抛 TransportError（D9）。"""
        payload = {"model": self.model, "messages": messages,
                   "thinking": {"type": "disabled"}, "response_format": {"type": "json_object"},
                   "temperature": 0, "max_tokens": max_tokens, "stream": False}
        body = json.dumps(payload).encode("utf-8")
        rec = {"arm": arm, "qid": qid, "attempt": attempt, "model": self.model}
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(API_URL, data=body, method="POST", headers={
                "Content-Type": "application/json", "Authorization": f"Bearer {self._key}"})
            try:
                status, raw = self._post(req)
            except urllib.error.HTTPError as e:
                status, raw = e.code, b""
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                rec.update(ok=False, error=type(e).__name__, http_try=http_try)
                time.sleep(2 * http_try)
                continue
            latency = round(time.time() - t0, 2)
            rec.update(http=status, http_try=http_try, latency_s=latency, at=started.isoformat(timespec="seconds"))
            if status in (401, 403):
                # key 被拒：不重试，直接停整轮；只记状态码
                rec.update(ok=False, error=f"http_{status}")
                self._log(rec)
                raise KeyRejected(f"DeepSeek rejected the API key (HTTP {status})")
            if 300 <= status < 400:
                # 跳转没有跟随（urlopen_no_redirect）：跟过去的请求会带着 Authorization 头发到新地址
                rec.update(ok=False, error=f"http_{status}")
                self._log(rec)
                raise TransportError(f"{arm} {qid} attempt {attempt}: http_{status} redirect not followed "
                                     f"(the API key is only sent to {API_URL})")
            if status in RETRY_STATUS and http_try < 3:
                time.sleep(2 * http_try)
                continue
            if status != 200:
                rec.update(ok=False, error=f"http_{status}")
                break
            try:
                data = json.loads(raw)
                choice = data["choices"][0]
                usage = data.get("usage") or {}
            except (ValueError, KeyError, IndexError, TypeError):
                # 只记诊断信息：长度、顶层键、服务端 error.message（不含回复内容，也不含 key）
                rec.update(ok=False, error="bad_response_body", body_bytes=len(raw), body_head_is_ws=raw[:1].isspace())
                try:
                    d = json.loads(raw)
                    rec["body_keys"] = sorted(d)[:10] if isinstance(d, dict) else type(d).__name__
                    if isinstance(d, dict) and isinstance(d.get("error"), dict):
                        rec["server_error"] = str(d["error"].get("message", ""))[:200]
                except ValueError:
                    rec["body_keys"] = "not_json"
                if http_try < 3:
                    self._log(dict(rec, will_retry=True))
                    time.sleep(5 * http_try)
                    continue
                break
            rec.update(finish_reason=choice.get("finish_reason"),
                       prompt_tokens=usage.get("prompt_tokens", 0),
                       prompt_cache_hit_tokens=usage.get("prompt_cache_hit_tokens", 0),
                       prompt_cache_miss_tokens=usage.get("prompt_cache_miss_tokens", 0),
                       completion_tokens=usage.get("completion_tokens", 0),
                       usd=round(usd_cost(usage, started, self.model), 6))
            text = (choice.get("message") or {}).get("content") or ""
            # 先查截断：被截断的 JSON 几乎总是解析失败，先解析的话截断会被误报成「不是合法 JSON」
            if choice.get("finish_reason") == "length":
                rec.update(ok=False, error="truncated")
                self._log(rec)
                return None, text, "reply was truncated (finish_reason=length)"
            try:
                out = json.loads(text)
            except json.JSONDecodeError:
                rec.update(ok=False, error="invalid_json")
                self._log(rec)
                return None, text, "reply is not valid JSON"
            if not isinstance(out, dict):
                rec.update(ok=False, error="not_an_object")
                self._log(rec)
                return None, text, "reply is not a JSON object"
            rec["ok"] = True
            self._log(rec)
            return out, text, None
        self._log(rec)
        raise TransportError(f"{arm} {qid} attempt {attempt}: {rec.get('error', 'request failed')}")

    @staticmethod
    def _post(req, sock_timeout: float = 180, total_timeout: float = TOTAL_TIMEOUT_S):
        """服务端排队时会先回 200 头，再每隔约 60 秒发一个换行保活，最后才给 body。
        socket 超时管单次读，total_timeout 管整次请求。"""
        t0 = time.time()
        with urlopen_no_redirect(req, timeout=sock_timeout) as r:
            chunks = []
            while True:
                c = r.read1(65536)
                if not c:
                    break
                chunks.append(c)
                if time.time() - t0 > total_timeout:
                    raise TimeoutError(f"request exceeded {total_timeout}s")
            return r.status, b"".join(chunks)

    def _log(self, rec: dict):
        self.calls_path.parent.mkdir(parents=True, exist_ok=True)
        with _LOG_LOCK, self.calls_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

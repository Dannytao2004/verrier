"""模型的 JSON 调用。默认 DeepSeek：OpenAI 兼容 chat/completions，非思考模式 + JSON 输出。改编自 fanout-ledger/llm.py，换成标准库 urllib。

v2.10a：建请求、解析回复、计价交给 provider adapter（triangulate/providers.py）；重试、先查截断、JSON 解析、日志留在这里。
没有 ModelSpec（命令行、回测、基线）时用 DeepSeek adapter + key 文件 + 下面的 API_URL，请求体和 v2.9b 逐字节相同。
有 ModelSpec（自带 key 的运行）时 provider / 模型 / key / 思考档位都按它。

每次调用记一行到 results/calls.jsonl：arm、题 id、第几次尝试、token、延迟、finish_reason、估算 USD。
日志里不记 prompt、不记 key。（v2.9b 起，回复不是合法 JSON 时记首尾各 200 字符的诊断。）
"""
import json
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .config import API_URL, CALLS, MODEL, THINKING, THINKING_EXTRA_TOKENS, price, read_key, thinking_role
from .providers import DEEPSEEK

RETRY_STATUS = {429, 500, 502, 503, 504}
TOTAL_TIMEOUT_S = 1200
_LOG_LOCK = threading.Lock()


class KeyRejected(RuntimeError):
    pass


class TransportError(RuntimeError):
    """服务端没给出可解析的回复（超时、5xx、空 body）。不算模型的输出问题，不占用「输出无效重试一次」的名额；
    runner 不保存这道题，之后再跑 run 会补上。"""


class BalanceExhausted(TransportError):
    """v2.10a：账户余额不足（DeepSeek 402）。不重试；agent 运行据此立刻停下（pipeline.AgentLLM / run_direction 把它变成
    预算中止，之后的调用都不再发）。是 TransportError 的子类，所以基线（forecast / runner 只接 TransportError）照旧跳过这道题。"""


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


def read_error_body(e: urllib.error.HTTPError, limit: int = 65536) -> bytes:
    """出错时服务端的 body（只给 adapter 判断错误类型用，不写日志：有的 provider 会回显部分 key）。"""
    try:
        return e.read(limit) or b""
    except Exception:  # noqa: BLE001
        return b""


class LLM:
    spec = None   # v2.10a：这次运行的 ModelSpec；None = 命令行 / 回测 / 基线。类级默认：测试会用 object.__new__ 绕过 __init__

    def __init__(self, calls_path=CALLS, model: str = MODEL, spec=None):
        if spec is not None:
            # key 只留在 spec 里（每次发请求时才取），运行结束时 spec.drop_key() 一处清掉
            self.spec, self.model, self.calls_path, self._key = spec, spec.model, calls_path, None
            return
        price(model)   # 没有价格的模型拒跑（config.UnknownModel），在读 key 之前
        self.model = model
        self.calls_path = calls_path
        self._key = read_key()

    @property
    def adapter(self):
        return DEEPSEEK if self.spec is None else self.spec.adapter

    def _auth_key(self) -> str:
        return self._key if self.spec is None else self.spec.key

    def effort_and_tokens(self, arm: str, max_tokens: int):
        """(这次调用的思考档位或 None, 实际发出的 max_tokens)。开了思考的调用多给 THINKING_EXTRA_TOKENS（思考 token 计入
        输出上限）；有 ModelSpec 时不超过模型的最大输出。没有 ModelSpec 时档位来自 TRIANGULATE_THINKING（v2.9a，默认全关）。"""
        role = thinking_role(arm)
        effort = THINKING.get(role) if self.spec is None else self.spec.effort(role)
        tokens = max_tokens + (THINKING_EXTRA_TOKENS if effort else 0)
        if self.spec is not None:
            tokens = min(tokens, self.spec.max_output)
        return effort, tokens

    def json_call(self, messages: list, *, arm: str, qid: str, attempt: int, max_tokens: int = 4000):
        """返回 (parsed_dict_or_None, raw_text, error_or_None)，error 只表示模型输出本身的问题。
        传输层失败（超时、5xx、空 body）内部重试最多 3 次，仍失败则抛 TransportError。
        3xx 跳转不跟随、不重试，直接抛 TransportError（D9）。"""
        ad = self.adapter
        effort, out_tokens = self.effort_and_tokens(arm, max_tokens)
        url = API_URL if self.spec is None else ad.chat_url(self.spec.region)
        headers, payload = ad.chat_request(self.model, self._auth_key(), messages, max_tokens=out_tokens, effort=effort)
        body = json.dumps(payload).encode("utf-8")
        rec = {"arm": arm, "qid": qid, "attempt": attempt, "model": self.model}
        if effort:
            rec["thinking"] = effort
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(url, data=body, method="POST", headers=headers)
            try:
                status, raw = self._post(req)
            except urllib.error.HTTPError as e:
                status, raw = e.code, (read_error_body(e) if e.code in ad.error_body_statuses else b"")
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
                raise KeyRejected(f"{ad.label} rejected the API key (HTTP {status})")
            if 300 <= status < 400:
                # 跳转没有跟随（urlopen_no_redirect）：跟过去的请求会带着 Authorization 头发到新地址
                rec.update(ok=False, error=f"http_{status}")
                self._log(rec)
                raise TransportError(f"{arm} {qid} attempt {attempt}: http_{status} redirect not followed "
                                     f"(the API key is only sent to {url})")
            why = ad.balance_exhausted(status, raw)
            if why:
                # 余额不足：不重试，整次运行停下（v2.10a）；日志行和 v2.9b 记 http_402 的那行相同
                rec.update(ok=False, error=f"http_{status}")
                self._log(rec)
                raise BalanceExhausted(f"insufficient balance: {ad.label} {why} ({arm} {qid} attempt {attempt}); "
                                       f"the run was stopped without retrying. Top up the {ad.label} account and run again.")
            if status in RETRY_STATUS and http_try < 3:
                time.sleep(2 * http_try)
                continue
            if status != 200:
                rec.update(ok=False, error=f"http_{status}")
                break
            try:
                data = json.loads(raw)
                unpacked = ad.chat_unpack(data)
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
            rec.update(ad.chat_meter(unpacked, started, self.model, effort))
            text = ad.chat_text(unpacked)
            # 先查截断：被截断的 JSON 几乎总是解析失败，先解析的话截断会被误报成「不是合法 JSON」
            if ad.chat_truncated(unpacked):
                rec.update(ok=False, error="truncated")
                self._log(rec)
                return None, text, "reply was truncated (finish_reason=length)"
            try:
                out = json.loads(text)
            except json.JSONDecodeError as e:
                # v2.9b：思考模式下裁判常回不合法的 JSON（finish_reason=stop，没截断）。只多记诊断：长度、出错位置、首尾各 200 字符
                rec.update(ok=False, error="invalid_json", text_len=len(text), json_error=f"{e.msg} at {e.pos}",
                           text_head=text[:200], text_tail=text[-200:], text_at_error=text[max(0, e.pos - 100):e.pos + 100])
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
        line = json.dumps(rec, ensure_ascii=False)
        if self.spec is not None:   # 兜底：记录里本来就没有 key
            line = self.spec.redact(line)
        self.calls_path.parent.mkdir(parents=True, exist_ok=True)
        with _LOG_LOCK, self.calls_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

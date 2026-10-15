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
_LOG_LOCK = threading.Lock()


class KeyRejected(RuntimeError):
    pass


class LLM:
    def __init__(self, calls_path=CALLS, model: str = MODEL):
        self.model = model
        self.calls_path = calls_path
        self._key = read_key()

    def json_call(self, messages: list, *, arm: str, qid: str, attempt: int, max_tokens: int = 4000):
        """返回 (parsed_dict_or_None, raw_text, error_or_None)。HTTP 层面的瞬时错误内部重试最多 3 次；
        这和「输出无效时重试一次」是两回事，后者由调用方决定。"""
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
                with urllib.request.urlopen(req, timeout=180) as r:
                    status, raw = r.status, r.read()
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
                rec.update(ok=False, error="bad_response_body")
                break
            rec.update(finish_reason=choice.get("finish_reason"),
                       prompt_tokens=usage.get("prompt_tokens", 0),
                       prompt_cache_hit_tokens=usage.get("prompt_cache_hit_tokens", 0),
                       prompt_cache_miss_tokens=usage.get("prompt_cache_miss_tokens", 0),
                       completion_tokens=usage.get("completion_tokens", 0),
                       usd=round(usd_cost(usage, started, self.model), 6))
            text = (choice.get("message") or {}).get("content") or ""
            try:
                out = json.loads(text)
            except json.JSONDecodeError:
                rec.update(ok=False, error="invalid_json")
                self._log(rec)
                return None, text, "reply is not valid JSON"
            if choice.get("finish_reason") == "length":
                rec.update(ok=False, error="truncated")
                self._log(rec)
                return None, text, "reply was truncated (finish_reason=length)"
            if not isinstance(out, dict):
                rec.update(ok=False, error="not_an_object")
                self._log(rec)
                return None, text, "reply is not a JSON object"
            rec["ok"] = True
            self._log(rec)
            return out, text, None
        self._log(rec)
        return None, "", rec.get("error", "request failed")

    def _log(self, rec: dict):
        self.calls_path.parent.mkdir(parents=True, exist_ok=True)
        with _LOG_LOCK, self.calls_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

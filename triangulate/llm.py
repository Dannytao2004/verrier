"""模型的 JSON 调用。默认 DeepSeek：OpenAI 兼容 chat/completions，非思考模式 + JSON 输出。改编自 fanout-ledger/llm.py，换成标准库 urllib。

v2.10a：建请求、解析回复、计价交给 provider adapter（triangulate/providers.py）；重试、先查截断、JSON 解析、日志留在这里。
没有 ModelSpec（命令行、回测、基线）时用 DeepSeek adapter + key 文件 + 下面的 API_URL，请求体和 v2.9b 逐字节相同。
有 ModelSpec（自带 key 的运行）时 provider / 模型 / key / 思考档位都按它。
v2.10b：各家不同的解码（Claude 是流式 SSE）、可重试的状态码、超时、回复本身的问题（截断 / 拒答 / 暂停）也由 adapter 给；
check_key() 用 models 列表接口校验 key。
v2.10c：OpenAI（Chat Completions）；读过的错误 body 另记 error.code，像 key 的片段换成 sk-***。
v2.10d：Kimi（流式 Chat Completions）；计量按 spec.price_id（国内站的价格）；retry_after() 另认 Kimi 搜索接口的 X-RateLimit-Reset。

每次调用记一行到 results/calls.jsonl：arm、题 id、第几次尝试、token、延迟、finish_reason、估算 USD。
日志里不记 prompt、不记 key。（v2.9b 起，回复不是合法 JSON 时记首尾各 200 字符的诊断。）
"""
import json
import re
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
    """v2.10a：账户余额不足（DeepSeek 402；v2.10b / c 起也包括 Claude、OpenAI 的余额和额度上限）。不重试；agent 运行据此立刻停下（pipeline.AgentLLM / run_direction 把它变成
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
    """出错时服务端的 body（只给 adapter 判断错误类型用，不整段写日志：有的 provider 会回显部分 key）。"""
    try:
        return e.read(limit) or b""
    except Exception:  # noqa: BLE001
        return b""


RETRY_AFTER_MAX_S = 60


def retry_after(ad, headers):
    """v2.10d：出错的回复要求等多少秒（交给 retry_wait）：adapter 不看（honor_retry_after = False，DeepSeek）或没有响应头时 None；
    先取 retry-after；没有时，adapter 指定了 reset_header（Kimi 搜索接口的 X-RateLimit-Reset，Unix 秒）就换成距现在的秒数。
    v2.10b / c 的 Claude、OpenAI 只看 retry-after，行为不变。"""
    if not ad.honor_retry_after or not headers:
        return None
    ra = headers.get("retry-after")
    name = getattr(ad, "reset_header", None)
    if ra is None and name and headers.get(name) is not None:
        try:
            ra = float(headers.get(name)) - time.time()
        except ValueError:
            ra = None
    return ra


def retry_wait(default_s: float, retry_after) -> float:
    """重试前等多久：默认 default_s；adapter 要求看 retry-after（Claude）且服务端给了秒数时，等两者中较长的，最多 60 秒。"""
    try:
        ra = float(retry_after) if retry_after is not None else None
    except ValueError:
        ra = None
    return default_s if ra is None or ra < 0 else max(default_s, min(ra, RETRY_AFTER_MAX_S))


# v2.10c：OpenAI 401 的 message 会回显打了码的 key（10-21 实测："Incorrect API key provided: sk-proj-****...0000"）。401 / 403 的 body
# 本来就不读；这里再兜底：日志里像 key 的片段一律换成 sk-***
_MASKED_KEY_RE = re.compile(r"\bsk-[A-Za-z0-9_\-*]+")


def server_error(ad, raw: bytes) -> dict:
    """v2.10b：adapter 允许时（Claude、OpenAI），读过的错误 body 只取 error.type 和 error.message 前 200 字记进日志
    （v2.10c 另记 error.code）；否则什么都不记。"""
    if not getattr(ad, "log_server_error", False) or not raw:
        return {}
    try:
        err = json.loads(raw).get("error")
    except (ValueError, AttributeError):
        return {}
    if not isinstance(err, dict):
        return {}
    out = {"server_error_type": str(err.get("type", ""))[:40],
           "server_error": _MASKED_KEY_RE.sub("sk-***", str(err.get("message", "")))[:200]}
    if err.get("code"):   # v2.10c：OpenAI 的 error.code（rate_limit_exceeded、slow_down、server_is_overloaded 等）
        out["server_error_code"] = str(err["code"])[:60]
    return out


def server_error_detail(rec: dict) -> str:
    """异常文字里服务端说明的那一段：" (type: message)"，有 error.code 时 " (type/code: message)"（v2.10c）；没读过 body 时为空。"""
    if not rec.get("server_error_type"):
        return ""
    code = f"/{rec['server_error_code']}" if rec.get("server_error_code") else ""
    return f" ({rec['server_error_type']}{code}: {rec.get('server_error', '')})"


def check_key(spec, timeout: float = 30) -> dict:
    """v2.10b：用这次运行的 key 调这家的 models 列表（Claude：GET /v1/models；DeepSeek：GET /models），不生成 token。
    返回可以给网页看的 dict：ok、status、error（key_rejected / balance / redirect / http_<code> / bad_response_body / network）、
    message、model_listed（所选模型在不在列表里；列表不完整又没找到时是 None）、n_models。不含 key，不含服务端原文。"""
    ad = spec.adapter
    url, headers = ad.key_check_request(spec.region, spec.key)
    out = {"provider": spec.provider, "model": spec.model, "ok": False}
    req = urllib.request.Request(url, method="GET", headers=headers)
    try:
        with urlopen_no_redirect(req, timeout=timeout) as r:
            status, raw = r.status, r.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, (read_error_body(e) if e.code in ad.error_body_statuses else b"")
        e.close()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return {**out, "error": "network", "message": f"could not reach {ad.label} ({type(e).__name__})"}
    out["status"] = status
    if status in (401, 403):
        return {**out, "error": "key_rejected", "message": f"{ad.label} rejected the API key (HTTP {status})"}
    if 300 <= status < 400:
        return {**out, "error": "redirect", "message": f"HTTP {status} redirect not followed (the API key is only sent to {url})"}
    why = ad.balance_exhausted(status, raw)
    if why:
        return {**out, "error": "balance", "message": f"insufficient balance: {ad.label} {why}. {ad.balance_hint}"}
    if status != 200:
        return {**out, "error": f"http_{status}", "message": f"{ad.label} models list returned HTTP {status}"}
    try:
        ids, complete = ad.models_unpack(json.loads(raw))
    except (ValueError, KeyError, TypeError, AttributeError):
        return {**out, "error": "bad_response_body", "message": f"{ad.label} models list returned an unexpected body"}
    listed = True if spec.model in ids else (False if complete else None)
    return {**out, "ok": True, "model_listed": listed, "n_models": len(ids),
            "message": f"{ad.label} accepted the API key" + ("" if listed else
                                                             f"; {spec.model} is not in the models list" if listed is False
                                                             else f"; {spec.model} was not on the first page of the models list")}


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

    @property
    def price_model(self) -> str:
        """v2.10d：计价用的 id：没有 spec 时就是 model；有 spec 时是 spec.price_id（Kimi 国内站 "kimi-k3@cn"，其余等于 model）。"""
        return self.model if self.spec is None else self.spec.price_id

    def _auth_key(self) -> str:
        return self._key if self.spec is None else self.spec.key

    def effort_and_tokens(self, arm: str, max_tokens: int):
        """(这次调用的思考档位或 None, 实际发出的 max_tokens)。开了思考的调用多给 THINKING_EXTRA_TOKENS（思考 token 计入
        输出上限）；有 ModelSpec 时不超过模型的最大输出。没有 ModelSpec 时档位来自 TRIANGULATE_THINKING（v2.9a，默认全关）。"""
        role = thinking_role(arm)
        if self.spec is not None:
            return self.spec.tokens_for(role, max_tokens)
        effort = THINKING.get(role)
        return effort, max_tokens + (THINKING_EXTRA_TOKENS if effort else 0)

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
            wait_hint = None
            try:
                status, raw = self._post(req, **ad.chat_timeouts)
            except urllib.error.HTTPError as e:
                status, raw = e.code, (read_error_body(e) if e.code in ad.error_body_statuses else b"")
                wait_hint = retry_after(ad, e.headers)
                e.close()
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
                                       f"the run was stopped without retrying. {ad.balance_hint}")
            if status in ad.retry_statuses and http_try < 3:
                time.sleep(retry_wait(2 * http_try, wait_hint))
                continue
            if status != 200:
                rec.update(ok=False, error=f"http_{status}", **server_error(ad, raw))
                break
            try:
                data = ad.chat_decode(raw)
                unpacked = ad.chat_unpack(data)
            except (ValueError, KeyError, IndexError, TypeError) as e:
                # 只记诊断信息：长度、顶层键、服务端 error.message（不含回复内容，也不含 key）
                rec.update(ok=False, error="bad_response_body", body_bytes=len(raw), body_head_is_ws=raw[:1].isspace())
                if getattr(e, "error_type", None):   # v2.10b：Claude 流里的 error 事件 / 流没收完
                    rec["stream_error"] = e.error_type
                try:
                    d = json.loads(raw)
                    rec["body_keys"] = sorted(d)[:10] if isinstance(d, dict) else type(d).__name__
                    if isinstance(d, dict) and isinstance(d.get("error"), dict):
                        rec["server_error"] = _MASKED_KEY_RE.sub("sk-***", str(d["error"].get("message", "")))[:200]
                except ValueError:
                    rec["body_keys"] = "not_json"
                if http_try < 3:
                    self._log(dict(rec, will_retry=True))
                    time.sleep(5 * http_try)
                    continue
                break
            rec.update(ad.chat_meter(unpacked, started, self.price_model, effort))
            text = ad.chat_text(unpacked)
            # 先查截断：被截断的 JSON 几乎总是解析失败，先解析的话截断会被误报成「不是合法 JSON」
            # （v2.10b：adapter 的 chat_problem 统一报回复本身的问题；DeepSeek 只有截断，Claude 另有拒答、暂停）
            problem = ad.chat_problem(unpacked)
            if problem:
                rec.update(ok=False, error=problem[0])
                self._log(rec)
                return None, text, problem[1]
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
        raise TransportError(f"{arm} {qid} attempt {attempt}: {rec.get('error', 'request failed')}{server_error_detail(rec)}")

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

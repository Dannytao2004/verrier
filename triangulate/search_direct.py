"""arm (3)「DeepSeek 联网直接答」（设计见 EVAL_SHOWCASE_PLAN.md，tag showcase-prereg 时定死）。

同一个模型，走 Anthropic 兼容接口 + 服务端 web_search（同 triangulate/agent/search.py 的 Searcher），一次调用，要一个数。
system = arm (1) 的 NAIVE_SYSTEM 加一句；user = arm (1) 的同一条 user 消息。数字由代码用 arm (1) 的 check_naive 从
最后一段文字里的 JSON 取，不做别的处理。输出不合格时带错误清单重试一次（重试不带工具）。
搜索不能限定日期，所以只跑未公布题（forecast.py 里 set = live 的题）。标准库实现。
"""
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .agent.search import SEARCH_FEE_ASSUMED_USD, SEARCH_URL, Searcher, anthropic_usage_to_cost
from .arms import _messages, check_naive
from .llm import TransportError
from .prompts import NAIVE_SYSTEM, RETRY

ARM = "search_direct"
SYSTEM = NAIVE_SYSTEM + ("\nYou can use the web_search tool before you answer. "
                         "Your final message must contain only the JSON object.")
MAX_USES = 5
MAX_TOKENS = 4096   # 这个接口默认带 thinking 块（probes/out/deepseek_search_probe.json），比 arm (1) 的 500 留得宽


class DirectClient(Searcher):
    """复用 Searcher 的 key 读取、模型名和日志回调；只把 HTTP 这一步拆成可替换的 call()，测试里用假客户端。"""

    def call(self, body: dict, *, qid: str, attempt: int) -> dict:
        """返回解析后的响应 dict。没拿到 HTTP 200 的传输错误最多重发 3 次（同 Searcher），仍失败抛 TransportError。"""
        data = json.dumps(body).encode("utf-8")
        rec = {"arm": ARM, "qid": qid, "attempt": attempt, "model": self.model, "kind": "search_direct"}
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(SEARCH_URL, data=data, method="POST", headers={
                "Content-Type": "application/json", "x-api-key": self._key, "anthropic-version": "2023-06-01"})
            try:
                with urllib.request.urlopen(req, timeout=600) as r:
                    status, raw = r.status, r.read()
            except urllib.error.HTTPError as e:
                status, raw = e.code, b""
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                rec.update(ok=False, error=type(e).__name__, http_try=http_try)
                time.sleep(3 * http_try)
                continue
            rec.update(http=status, http_try=http_try, latency_s=round(time.time() - t0, 2),
                       at=started.isoformat(timespec="seconds"))
            if status in (429, 500, 502, 503, 504) and http_try < 3:
                time.sleep(3 * http_try)
                continue
            if status != 200:
                rec.update(ok=False, error=f"http_{status}")
                break
            try:
                d = json.loads(raw)
            except ValueError:
                rec.update(ok=False, error="bad_response_body")
                break
            m = metered(d, started, self.model)
            rec.update(ok=True, stop=d.get("stop_reason"), **{k: m[k] for k in METER_KEYS})
            self._log(rec)
            d["_started_at"] = started.isoformat(timespec="seconds")
            d["_latency_s"] = rec["latency_s"]
            return d
        self._log(rec)
        raise TransportError(f"{ARM} {qid} attempt {attempt}: {rec.get('error', 'request failed')}")


METER_KEYS = ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens",
              "web_search_requests", "usd", "usd_search_fee_assumed")


def metered(d: dict, started: datetime, model: str) -> dict:
    usage = d.get("usage") or {}
    n_req = int(((usage.get("server_tool_use") or {}).get("web_search_requests")) or 0)
    return {"input_tokens": usage.get("input_tokens", 0) or 0,
            "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0) or 0,
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0) or 0,
            "output_tokens": usage.get("output_tokens", 0) or 0, "web_search_requests": n_req,
            "usd": round(anthropic_usage_to_cost(usage, started, model), 6),
            "usd_search_fee_assumed": round(n_req * SEARCH_FEE_ASSUMED_USD, 4)}


def final_text(content: list) -> str:
    """最后一段文字 = 最后一个工具块（server_tool_use / web_search_tool_result）之后的 text 块，按顺序拼起来。
    没有工具块时就是全部 text 块。thinking 块不算。"""
    blocks = content if isinstance(content, list) else []
    last_tool = max((i for i, b in enumerate(blocks) if isinstance(b, dict)
                     and b.get("type") in ("server_tool_use", "web_search_tool_result")), default=-1)
    return "".join(b.get("text") or "" for b in blocks[last_tool + 1:] if isinstance(b, dict) and b.get("type") == "text")


def parse_json(text: str):
    """取 JSON 对象：整段解析；不行就去掉 ``` 围栏再解析；再不行取第一个 { 到最后一个 } 之间。返回 (dict 或 None, 错误)。"""
    t = (text or "").strip()
    cands = [t]
    if t.startswith("```"):
        cands.append(t.strip("`").removeprefix("json").strip())
    if "{" in t and "}" in t:
        cands.append(t[t.index("{"):t.rindex("}") + 1])
    for c in cands:
        try:
            out = json.loads(c)
        except ValueError:
            continue
        return (out, None) if isinstance(out, dict) else (None, "reply is not a JSON object")
    return None, "reply is not valid JSON" if t else "reply has no text after the last search"


def audit(d: dict) -> dict:
    """审计字段：搜索词、结果 URL（含 page_age）、全部 text 块、thinking 块数。不存搜索结果的正文。"""
    queries, results, texts, n_err, n_think = [], [], [], 0, 0
    for b in d.get("content") or []:
        t = b.get("type") if isinstance(b, dict) else None
        if t == "server_tool_use":
            queries.append(str((b.get("input") or {}).get("query", ""))[:200])
        elif t == "web_search_tool_result":
            c = b.get("content")
            if isinstance(c, list):
                results += [{"url": x.get("url"), "title": str(x.get("title") or "")[:200], "page_age": x.get("page_age")}
                            for x in c if isinstance(x, dict) and x.get("url")]
            else:
                n_err += 1
        elif t == "text":
            texts.append(b.get("text") or "")
        elif t == "thinking":
            n_think += 1
    return {"queries": queries, "results": results, "n_search_errors": n_err, "texts": texts, "n_thinking_blocks": n_think}


def run_search_direct(client, q: dict) -> dict:
    """一题：首次调用（带 web_search）+ 输出不合格时重试一次（不带工具）。返回要保存的记录。"""
    user = _messages(SYSTEM, q)[1]["content"]
    msgs = [{"role": "user", "content": user}]
    strict = q.get("strict", True)
    record = {"qid": q["id"], "arm": ARM, "model": client.model, "target_unit": q["answer_unit"], "as_of": q["as_of"],
              "system": SYSTEM, "user": user, "max_uses": MAX_USES, "attempts": []}
    for attempt in (1, 2):
        body = {"model": client.model, "max_tokens": MAX_TOKENS, "system": SYSTEM, "messages": msgs}
        if attempt == 1:
            body["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_USES}]
        d = client.call(body, qid=q["id"], attempt=attempt)
        started = d.get("_started_at")
        text = final_text(d.get("content"))
        reply, err = parse_json(text)
        if d.get("stop_reason") == "max_tokens":
            reply, err = None, "reply was truncated (stop_reason=max_tokens)"
        problems = [err] if err else check_naive(reply, q["answer_unit"], strict)[2]
        m = metered(d, datetime.fromisoformat(started) if started else datetime.now(timezone.utc), client.model)
        record["attempts"].append({"attempt": attempt, "with_tools": attempt == 1, "at": started,
                                   "latency_s": d.get("_latency_s"), "stop_reason": d.get("stop_reason"),
                                   "final_text": text, "reply": reply, "problems": problems, **m, **audit(d)})
        if not problems or attempt == 2:
            break
        msgs = msgs + [{"role": "assistant", "content": text or "{}"},
                       {"role": "user", "content": RETRY.format(problems="\n".join(f"- {p}" for p in problems))}]
    record["final_attempt"] = len(record["attempts"])
    status, est, _ = check_naive(record["attempts"][-1]["reply"], q["answer_unit"], strict)
    record.update(status=status, estimate=est,
                  usd=round(sum(a["usd"] for a in record["attempts"]), 6),
                  usd_search_fee_assumed=round(sum(a["usd_search_fee_assumed"] for a in record["attempts"]), 4))
    return record

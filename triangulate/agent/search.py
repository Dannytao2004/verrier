"""SEARCHER：DeepSeek 的 Anthropic 兼容接口 + 服务端 web_search 工具。

只有这一个角色看得到搜索结果。它的输出由代码用正则只取 URL，其余文字（标题、摘要、模型的话）全部丢弃，
分析角色（extractor / judge / final）永远看不到。每次调用记一行 calls.jsonl（不含内容、不含 key）。
"""
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from ..config import MAX_TOKENS, MODEL, read_key, usd_cost

SEARCH_URL = "https://api.deepseek.com/anthropic/v1/messages"
# DeepSeek 价格页（2026-10-15 查看）没有列 web search 的单价。预算里按 Anthropic 公开价 $10 / 1000 次 记账，
# 这是保守假设，报告里单列，不和 token 成本混在一起。
SEARCH_FEE_ASSUMED_USD = 0.01
URL_RE = re.compile(r"https?://[^\s<>\"'`\)\]\}|]+")
_TRAIL = ".,;:!?*'\")]}>"


def parse_urls(text: str, cap: int = 5) -> list:
    """从任意文字里只取 URL：去尾部标点、去 #fragment、去重保序，最多 cap 个。"""
    out = []
    for m in URL_RE.finditer(text or ""):
        u = m.group(0).rstrip(_TRAIL).split("#", 1)[0]
        if len(u) > 12 and u not in out:
            out.append(u)
        if len(out) >= cap:
            break
    return out


def anthropic_usage_to_cost(usage: dict, t: datetime, model: str = MODEL) -> float:
    return usd_cost({"prompt_cache_hit_tokens": usage.get("cache_read_input_tokens", 0) or 0,
                     "prompt_cache_miss_tokens": (usage.get("input_tokens", 0) or 0)
                     + (usage.get("cache_creation_input_tokens", 0) or 0),
                     "completion_tokens": usage.get("output_tokens", 0) or 0}, t, model)


class Searcher:
    def __init__(self, log, model: str = MODEL):
        self.model = model
        self._key = read_key()
        self._log = log  # callable(rec)

    def search(self, prompt: str, *, role: str, qid: str, max_uses: int = 3, cap: int = 5) -> dict:
        body = json.dumps({"model": self.model, "max_tokens": MAX_TOKENS["search"],
                           "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}],
                           "messages": [{"role": "user", "content": prompt}]}).encode("utf-8")
        rec = {"arm": role, "qid": qid, "model": self.model, "kind": "search"}
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(SEARCH_URL, data=body, method="POST", headers={
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
            usage = d.get("usage") or {}
            n_req = int(((usage.get("server_tool_use") or {}).get("web_search_requests")) or 0)
            queries, result_urls, texts, n_err = [], [], [], 0
            for b in d.get("content") or []:
                if b.get("type") == "server_tool_use":
                    queries.append(str((b.get("input") or {}).get("query", ""))[:200])
                elif b.get("type") == "web_search_tool_result":
                    c = b.get("content")
                    if isinstance(c, list):
                        result_urls += [x.get("url") for x in c if isinstance(x, dict) and x.get("url")]
                    else:
                        n_err += 1
                elif b.get("type") == "text":
                    texts.append(b.get("text") or "")
            text_urls = parse_urls("\n".join(texts), cap=cap)
            # 模型最后挑的 URL 优先；不够 cap 个时用搜索结果里的 URL 按顺序补
            urls = list(text_urls)
            for u in parse_urls("\n".join(result_urls), cap=50):
                if len(urls) >= cap:
                    break
                if u not in urls:
                    urls.append(u)
            usd = anthropic_usage_to_cost(usage, started, self.model)
            rec.update(ok=True, stop=d.get("stop_reason"), input_tokens=usage.get("input_tokens", 0),
                       cache_read_input_tokens=usage.get("cache_read_input_tokens", 0),
                       output_tokens=usage.get("output_tokens", 0), web_search_requests=n_req,
                       n_result_urls=len(result_urls), n_text_urls=len(text_urls), n_search_errors=n_err,
                       usd=round(usd, 6), usd_search_fee_assumed=round(n_req * SEARCH_FEE_ASSUMED_USD, 4))
            self._log(rec)
            # 返回给调用方的只有：查询词（只进 state.json 审计，不进任何分析 prompt）、URL、计量
            return {"queries": queries, "urls": urls, "n_text_urls": len(text_urls), "n_result_urls": len(result_urls),
                    "web_search_requests": n_req, "usd": usd, "usd_search_fee_assumed": n_req * SEARCH_FEE_ASSUMED_USD}
        self._log(rec)
        return {"queries": [], "urls": [], "error": rec.get("error", "request failed"), "web_search_requests": 0,
                "usd": 0.0, "usd_search_fee_assumed": 0.0}

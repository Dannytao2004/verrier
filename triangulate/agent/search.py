"""SEARCHER：默认是 DeepSeek 的 Anthropic 兼容接口 + 服务端 web_search 工具。v2.10a：请求格式、解析和计价交给
provider adapter（triangulate/providers.py），有 ModelSpec 的运行按它选 provider / 模型 / key；没有时和 v2.9b 逐字节相同。

只有这一个角色看得到搜索结果。它的输出由代码用正则只取 URL，其余文字（标题、摘要、模型的话）全部丢弃，
分析角色（extractor / judge / final）永远看不到。每次调用记一行 calls.jsonl（不含内容、不含 key）。
"""
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .. import llm
from ..config import MAX_TOKENS, MODEL, price, read_key
from ..providers import DEEPSEEK, DEEPSEEK_SEARCH_FEE_ASSUMED_USD, anthropic_usage_to_cost  # noqa: F401（search_direct 从这里取）

SEARCH_URL = "https://api.deepseek.com/anthropic/v1/messages"
# DeepSeek 价格页没有单列 Anthropic 兼容接口里 web search 的单价。预算里按 Anthropic 公开价 $10 / 1000 次 记账，
# 这是保守假设，报告里单列，不和 token 成本混在一起（说明见 providers.DEEPSEEK_SEARCH_FEE_ASSUMED_USD）。
SEARCH_FEE_ASSUMED_USD = DEEPSEEK_SEARCH_FEE_ASSUMED_USD
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


class Searcher:
    spec = None   # v2.10a：这次运行的 ModelSpec；None = 命令行 / 回测（基线的 DirectClient 继承这个构造）

    def __init__(self, log, model: str = MODEL, spec=None):
        if spec is not None:   # key 只留在 spec 里，见 llm.LLM.__init__
            self.spec, self.model, self._key = spec, spec.model, None
        else:
            price(model)   # 没有价格的模型拒跑
            self.model = model
            self._key = read_key()
        self._log = log  # callable(rec)

    def search(self, prompt: str, *, role: str, qid: str, max_uses: int = 3, cap: int = 5) -> dict:
        """返回查询词、URL 和计量。余额不足（DeepSeek 402）抛 llm.BalanceExhausted（run_direction 据此停下整次运行）；
        其余 HTTP 错误照旧记在返回的 error 里，不抛。"""
        sp = self.spec
        ad = DEEPSEEK if sp is None else sp.adapter
        url = SEARCH_URL if sp is None else ad.search_url(sp.region)
        fee = SEARCH_FEE_ASSUMED_USD if sp is None else ad.search_fee_usd
        headers, payload = ad.search_request(self.model, self._key if sp is None else sp.key, prompt,
                                             max_tokens=MAX_TOKENS["search"], max_uses=max_uses)
        body = json.dumps(payload).encode("utf-8")
        rec = {"arm": role, "qid": qid, "model": self.model, "kind": "search"}
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(url, data=body, method="POST", headers=headers)
            try:
                # 不跟随跳转（D9）：3xx 以 HTTPError 回来，下面记成 http_3xx 错误返回，key 不会发到别的地址
                with llm.urlopen_no_redirect(req, timeout=600) as r:
                    status, raw = r.status, r.read()
            except urllib.error.HTTPError as e:
                status, raw = e.code, (llm.read_error_body(e) if e.code in ad.error_body_statuses else b"")
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                rec.update(ok=False, error=type(e).__name__, http_try=http_try)
                time.sleep(3 * http_try)
                continue
            rec.update(http=status, http_try=http_try, latency_s=round(time.time() - t0, 2),
                       at=started.isoformat(timespec="seconds"))
            why = ad.balance_exhausted(status, raw)
            if why:   # v2.10a：余额不足，不重试；日志行和 v2.9b 记 http_402 的那行相同
                rec.update(ok=False, error=f"http_{status}")
                self._log(rec)
                raise llm.BalanceExhausted(f"insufficient balance: {ad.label} {why} ({role} {qid}); the run was stopped "
                                           f"without retrying. Top up the {ad.label} account and run again.")
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
            parsed = ad.search_unpack(d)
            queries, result_urls, n_req = parsed["queries"], parsed["result_urls"], parsed["n_req"]
            text_urls = parse_urls("\n".join(parsed["texts"]), cap=cap)
            # 模型最后挑的 URL 优先；不够 cap 个时用搜索结果里的 URL 按顺序补
            urls = list(text_urls)
            for u in parse_urls("\n".join(result_urls), cap=50):
                if len(urls) >= cap:
                    break
                if u not in urls:
                    urls.append(u)
            tokens, usd = ad.search_meter(parsed, started, self.model)
            rec.update(ok=True, stop=parsed["stop"], **tokens, web_search_requests=n_req,
                       n_result_urls=len(result_urls), n_text_urls=len(text_urls), n_search_errors=parsed["n_err"],
                       usd=round(usd, 6), usd_search_fee_assumed=round(n_req * fee, 4))
            self._log(rec)
            # 返回给调用方的只有：查询词（只进 state.json 审计，不进任何分析 prompt）、URL、计量
            return {"queries": queries, "urls": urls, "n_text_urls": len(text_urls), "n_result_urls": len(result_urls),
                    "web_search_requests": n_req, "usd": usd, "usd_search_fee_assumed": n_req * fee}
        self._log(rec)
        return {"queries": [], "urls": [], "error": rec.get("error", "request failed"), "web_search_requests": 0,
                "usd": 0.0, "usd_search_fee_assumed": 0.0}

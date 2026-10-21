"""SEARCHER：默认是 DeepSeek 的 Anthropic 兼容接口 + 服务端 web_search 工具。v2.10a：请求格式、解析和计价交给
provider adapter（triangulate/providers.py），有 ModelSpec 的运行按它选 provider / 模型 / key；没有时和 v2.9b 逐字节相同。
v2.10b：Claude 走官方 api.anthropic.com 的同一个工具；回复是 pause_turn 时续上（见 Searcher.search）。
v2.10c：GPT 走 OpenAI Responses API 的 hosted web_search（解析见 providers.openai_search_unpack）。
v2.10d：Kimi 的模型侧搜索（$web_search）已下线，adapter.search_mode = "queries"：先用一次小的 JSON 调用把同一段搜索 prompt
变成几个查询词（prompts.SEARCH_QUERIES_*，只有这类 provider 用），再逐个调 POST /v1/tools/search，按名次交替合并 URL
（Searcher._search_by_queries）。DeepSeek / Claude / GPT 的搜索路径不变。
v2.10e：GLM 走同一条路（POST {base}/web_search）；搜索请求按区域建（adapter.tools_search_request 多收 region），每个 HTTP 200
都按一次计费（adapter.search_bills_every_ok_response）。

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
from ..config import MAX_TOKENS, MODEL, read_key, require_deepseek
from ..providers import DEEPSEEK, DEEPSEEK_SEARCH_FEE_ASSUMED_USD, anthropic_usage_to_cost  # noqa: F401（search_direct 从这里取）
from ..providers import search_fee_usd
from .prompts import SEARCH_QUERIES_SYSTEM, SEARCH_QUERIES_USER

SEARCH_URL = "https://api.deepseek.com/anthropic/v1/messages"
# DeepSeek 价格页没有单列 Anthropic 兼容接口里 web search 的单价。预算里按 Anthropic 公开价 $10 / 1000 次 记账，
# 这是保守假设，报告里单列，不和 token 成本混在一起（说明见 providers.DEEPSEEK_SEARCH_FEE_ASSUMED_USD）。
SEARCH_FEE_ASSUMED_USD = DEEPSEEK_SEARCH_FEE_ASSUMED_USD
URL_RE = re.compile(r"https?://[^\s<>\"'`\)\]\}|]+")
_TRAIL = ".,;:!?*'\")]}>"
# v2.10d：「生成查询词」那次 JSON 调用的输出上限（几个查询词的 JSON，远用不完；开思考的模型另加 THINKING_EXTRA_TOKENS）。
# 不放进 config.MAX_TOKENS：那张表会原样记进每次运行的 settings，DeepSeek 运行的 settings 要保持不变
SEARCH_QUERIES_MAX_TOKENS = 2000


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


class _QueryLLM(llm.LLM):
    """v2.10d：Searcher 里「生成查询词」的那次调用：走 llm.LLM.json_call（同一套 adapter、重试、截断检查、日志字段），
    日志交给 Searcher 的 log（agent 里是 AgentLLM._log：写 calls.jsonl、去 key、计入预算）。key 只经 spec 取，不另存。"""

    def __init__(self, spec, sink):
        self.spec, self.model, self.calls_path, self._key, self._sink = spec, spec.model, None, None, sink

    def _log(self, rec: dict):
        self._sink(rec)


class Searcher:
    spec = None   # v2.10a：这次运行的 ModelSpec；None = 命令行 / 回测（基线的 DirectClient 继承这个构造）
    # v2.10f：续接（Claude 的 pause_turn）之前重新预扣一次搜索的预扣；pipeline.Context 在自带 key 的运行里设成
    # Budget.renew_current（换掉这个线程已用掉的那份预扣，放不下就返回 False：不续，不中止整次运行）。None = 不预扣（命令行不续接）
    renew = None

    def __init__(self, log, model: str = MODEL, spec=None):
        if spec is not None:   # key 只留在 spec 里，见 llm.LLM.__init__
            self.spec, self.model, self._key = spec, spec.model, None
        else:
            require_deepseek(model)   # 没有价格的模型拒跑；v2.10f：别家的模型也拒跑（没有 spec 时只有 DeepSeek 的 key）
            self.model = model
            self._key = read_key()
        self._log = log  # callable(rec)

    def search(self, prompt: str, *, role: str, qid: str, max_uses: int = 3, cap: int = 5) -> dict:
        """返回查询词、URL 和计量。余额不足（DeepSeek 402、Claude 402、OpenAI 429 credit_balance_exhausted 等）抛 llm.BalanceExhausted（run_direction 据此停下整次运行）；
        其余 HTTP 错误照旧记在返回的 error 里，不抛。v2.10b：adapter 允许时（Claude），回复的 stop_reason 是 pause_turn 就把这次的
        content 原样回传续上（最多 adapter.max_search_continuations 次），每次请求各记一行日志，结果合并。"""
        sp = self.spec
        ad = DEEPSEEK if sp is None else sp.adapter
        if getattr(ad, "search_mode", "model") == "queries":   # v2.10d Kimi
            return self._search_by_queries(ad, prompt, role=role, qid=qid, max_uses=max_uses, cap=cap)
        url = SEARCH_URL if sp is None else ad.search_url(sp.region)
        fee = SEARCH_FEE_ASSUMED_USD if sp is None else search_fee_usd(sp.price_id)
        price_model = self.model if sp is None else sp.price_id
        effort, out_tokens = (None, MAX_TOKENS["search"]) if sp is None else sp.tokens_for("search", MAX_TOKENS["search"])
        # v2.10f：自带 key 的运行用 adapter 的 search_request_spec（有的话：DeepSeek 在请求体里写明关思考）；命令行照旧 search_request
        build = ad.search_request if sp is None else getattr(ad, "search_request_spec", ad.search_request)
        headers, payload = build(self.model, self._key if sp is None else sp.key, prompt,
                                 max_tokens=out_tokens, max_uses=max_uses, effort=effort)
        rounds, error = [], None
        for n in range(ad.max_search_continuations + 1):
            if n and self.renew is not None and not self.renew():   # v2.10f：续接也按最坏情况预扣，放不下就不续
                error = "not sent: the spending cap has no room for another worst-case search request"
                break
            rec = {"arm": role, "qid": qid, "model": self.model, "kind": "search"}
            if n:
                rec["continuation"] = n
            got = self._request(ad, url, headers, payload, rec, role, qid)
            if got is None:   # 这次请求失败：第一次就失败照旧返回空结果；续的时候失败就用已经拿到的结果
                self._log(rec)
                error = rec.get("error", "request failed") + llm.server_error_detail(rec)
                break
            d, started = got
            parsed = ad.search_unpack(d)
            text_urls = parse_urls("\n".join(parsed["texts"]), cap=cap)
            tokens, usd = ad.search_meter(parsed, started, price_model)
            rec.update(ok=True, stop=parsed["stop"], **tokens, web_search_requests=parsed["n_req"],
                       n_result_urls=len(parsed["result_urls"]), n_text_urls=len(text_urls), n_search_errors=parsed["n_err"],
                       usd=round(usd, 6), usd_search_fee_assumed=round(parsed["n_req"] * fee, 4))
            self._log(rec)
            rounds.append((parsed, usd))
            payload = ad.search_continue(payload, d)
            if payload is None:
                break
        if not rounds:
            return {"queries": [], "urls": [], "error": error, "web_search_requests": 0,
                    "usd": 0.0, "usd_search_fee_assumed": 0.0}
        queries = [q for p, _ in rounds for q in p["queries"]]
        result_urls = [u for p, _ in rounds for u in p["result_urls"]]
        text_urls = parse_urls("\n".join(t for p, _ in rounds for t in p["texts"]), cap=cap)
        n_req = sum(p["n_req"] for p, _ in rounds)
        usd = sum(u for _, u in rounds)
        # 模型最后挑的 URL 优先；不够 cap 个时用搜索结果里的 URL 按顺序补
        urls = list(text_urls)
        for u in parse_urls("\n".join(result_urls), cap=50):
            if len(urls) >= cap:
                break
            if u not in urls:
                urls.append(u)
        # 返回给调用方的只有：查询词（只进 state.json 审计，不进任何分析 prompt）、URL、计量。搜索结果的标题不往外传
        out = {"queries": queries, "urls": urls, "n_text_urls": len(text_urls), "n_result_urls": len(result_urls),
               "web_search_requests": n_req, "usd": usd, "usd_search_fee_assumed": n_req * fee}
        if len(rounds) > 1:
            out["continuations"] = len(rounds) - 1
        if error:
            out["error"] = f"continuation {len(rounds)}: {error}"
        return out

    def _search_by_queries(self, ad, brief: str, *, role: str, qid: str, max_uses: int, cap: int) -> dict:
        """v2.10d（adapter.search_mode = "queries"，Kimi；v2.10e 起 GLM）：一次 JSON 调用把搜索 prompt（brief）变成最多 max_uses 个查询词，
        再逐个 POST 搜索接口（adapter.tools_search_request），每次请求记一行日志（kind = search，query_n = 第几个）。
        URL 按名次交替合并（每个查询词的第 1 名、再第 2 名……），去重后取 cap 个；标题解析出来但不往外传（同其他 provider）。
        一个查询词失败不影响其余的，失败原因合在返回的 error 里；生成查询词失败就没有 URL（error 以 "queries:" 开头）。
        余额不足（生成查询词或搜索）抛 llm.BalanceExhausted。返回的字段同 search()；usd 是生成查询词的 token 成本，
        usd_search_fee_assumed 是搜索接口的按次费用（Kimi：只有返回非空结果的才收费；GLM：每个 HTTP 200 都算）。"""
        sp = self.spec
        fee = search_fee_usd(sp.price_id)
        queries, usd, err = self._write_queries(brief, role=role, qid=qid, n=max_uses)
        out = {"queries": queries, "urls": [], "n_text_urls": 0, "n_result_urls": 0, "web_search_requests": 0, "usd": usd,
               "usd_search_fee_assumed": 0.0}
        if err:
            out["error"] = err
            return out
        url, per_query, errors, n_req = ad.search_url(sp.region), [], [], 0
        # v2.10e：Kimi 只有 HTTP 200 且结果非空才收费；GLM 文档只说按调用次数计费，每个 HTTP 200 都按一次记（含空结果、形状不对的）
        every_ok = getattr(ad, "search_bills_every_ok_response", False)
        for i, q in enumerate(queries, 1):
            headers, payload = ad.tools_search_request(sp.key, q, limit=cap, region=sp.region)
            rec = {"arm": role, "qid": qid, "model": self.model, "kind": "search", "query_n": i}
            got, hits = self._request(ad, url, headers, payload, rec, role, qid), None
            if got is not None:
                try:
                    hits = ad.tools_search_unpack(got[0])
                except (KeyError, TypeError):
                    rec.update(ok=False, error="bad_response_body")
            billed = 1 if hits or (got is not None and every_ok) else 0
            n_req += billed
            if hits is None:
                if billed:   # GLM：HTTP 200 但形状不对，也按一次计费（计入预算）
                    rec.update(web_search_requests=1, usd=0.0, usd_search_fee_assumed=round(fee, 6))
                self._log(rec)
                errors.append(f"query {i}: {rec.get('error', 'request failed')}{llm.server_error_detail(rec)}")
                continue
            rec.update(ok=True, web_search_requests=billed, n_result_urls=len(hits), usd=0.0,
                       usd_search_fee_assumed=round(billed * fee, 6))
            self._log(rec)
            per_query.append(hits)
        merged = [h[rank] for rank in range(max((len(h) for h in per_query), default=0)) for h in per_query if rank < len(h)]
        out.update(urls=parse_urls("\n".join(u for u, _title in merged), cap=cap), n_result_urls=len(merged),
                   web_search_requests=n_req, usd_search_fee_assumed=n_req * fee)
        if errors:
            out["error"] = "; ".join(errors)
        return out

    def _write_queries(self, brief: str, *, role: str, qid: str, n: int):
        """返回 (查询词列表, 这次调用的 USD, 错误或 None)。只调一次（不像 AgentLLM.ask 那样带错误重问：调用方 run_direction 已经
        占着并发名额和预扣）。查询词只做最少的整理：去首尾空白、去掉空的和重复的、非字符串的不要，最多 n 个；不修 JSON。"""
        spent = [0.0]

        def sink(rec):
            spent[0] += float(rec.get("usd") or 0)
            self._log(rec)

        msgs = [{"role": "system", "content": SEARCH_QUERIES_SYSTEM},
                {"role": "user", "content": SEARCH_QUERIES_USER.format(n=n, brief=brief)}]
        try:
            got, _text, err = _QueryLLM(self.spec, sink).json_call(msgs, arm=f"{role}:queries", qid=qid, attempt=1,
                                                                   max_tokens=SEARCH_QUERIES_MAX_TOKENS)
        except llm.BalanceExhausted:
            raise
        except (llm.TransportError, llm.KeyRejected) as e:
            return [], spent[0], f"queries: {e}"
        if err:
            return [], spent[0], f"queries: {err}"
        raw = got.get("queries")
        if not isinstance(raw, list):
            return [], spent[0], 'queries: the reply has no "queries" list'
        qs = []
        for q in raw:
            if isinstance(q, str) and q.strip() and q.strip() not in qs:
                qs.append(q.strip())
        if not qs:
            return [], spent[0], "queries: the reply listed no search queries"
        return qs[:n], spent[0], None

    def _request(self, ad, url: str, headers: dict, payload: dict, rec: dict, role: str, qid: str):
        """发一次搜索请求（传输层失败最多试 3 次）。成功返回 (解析后的 dict, 开始时刻)，失败返回 None（原因在 rec 里）。
        余额不足抛 llm.BalanceExhausted。"""
        body = json.dumps(payload).encode("utf-8")
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(url, data=body, method="POST", headers=headers)
            wait_hint = None
            try:
                # 不跟随跳转（D9）：3xx 以 HTTPError 回来，下面记成 http_3xx 错误返回，key 不会发到别的地址
                with llm.urlopen_no_redirect(req, timeout=600) as r:
                    status, raw = r.status, r.read()
            except urllib.error.HTTPError as e:
                status, raw = e.code, (llm.read_error_body(e) if e.code in ad.error_body_statuses else b"")
                wait_hint = llm.retry_after(ad, e.headers)
                e.close()
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
                raise llm.BalanceExhausted(llm.balance_message(ad, why, f"{role} {qid}"))
            if status in ad.retry_statuses and http_try < 3:
                time.sleep(llm.retry_wait(3 * http_try, wait_hint))
                continue
            if status != 200:   # v2.10f：服务端说明先 redact（这次运行的 key）再截断
                rec.update(ok=False, error=f"http_{status}",
                           **llm.server_error(ad, raw, None if self.spec is None else self.spec.redact))
                return None
            try:
                d = json.loads(raw)
            except ValueError:
                rec.update(ok=False, error="bad_response_body")
                return None
            return d, started
        return None

"""SEARCHER：默认是 DeepSeek 的 Anthropic 兼容接口 + 服务端 web_search 工具。v2.10a：请求格式、解析和计价交给
provider adapter（triangulate/providers.py），有 ModelSpec 的运行按它选 provider / 模型 / key；没有时和 v2.9b 逐字节相同。
v2.10b：Claude 走官方 api.anthropic.com 的同一个工具；回复是 pause_turn 时续上（见 Searcher.search）。
v2.10c：GPT 走 OpenAI Responses API 的 hosted web_search（解析见 providers.openai_search_unpack）。
v2.10d：Kimi 的模型侧搜索（$web_search）已下线，adapter.search_mode = "queries"：先用一次小的 JSON 调用把同一段搜索 prompt
变成几个查询词（prompts.SEARCH_QUERIES_*，只有这类 provider 用），再逐个调 POST /v1/tools/search，按名次交替合并 URL
（Searcher._search_by_queries）。DeepSeek / Claude / GPT 的搜索路径不变。
v2.10e：GLM 走同一条路（POST {base}/web_search）；搜索请求按区域建（adapter.tools_search_request 多收 region），每个 HTTP 200
都按一次计费（adapter.search_bills_every_ok_response）。
v2.10h（用户 10-21：每个模型只用自家自带的联网搜索）：「生成查询词 + 搜索接口」那条路（search_mode = "queries"）删掉。Kimi K3 走
Responses API 自带的 web_search，GLM 走 Chat Completions 自带的 web_search，和 DeepSeek / Claude / GPT 同一条路（adapter 的
search_request / search_unpack / search_meter）；search_request 多收 region（GLM 两站的搜索引擎不同）。
v2.10i（审查修正）：自带 key 的运行里，回复没给 usage 时这次搜索按预扣的 token 部分记账（不按 0）；Responses 回复 status failed 时
记 ok false、把 redact 过的 error 往外报；Kimi、GLM 的搜索读超时不重发、按预扣记账，单次读超时取 adapter 的 search_timeout_s；
GLM 的回复里没有查询词，返回值带 queries_reported False。DeepSeek 命令行的请求、超时、日志、返回值都不变（24 组金样本）。
v2.11c（计划 D3，决定 17、18）：返回值多一个 candidates = {provider, by_query}：每次搜索每个查询词的全部结果 URL（含没被选中的），
URL 用和选中的 URL 同一个 parse_urls 规范化，不带标题（见 by_query）。run_direction 照旧把整个返回值存进 state.json 的
results[*].search，只给人事后审计，不进任何 prompt（tests/test_search_candidates.py 的哨兵测试）。所以 v2.10i 那句「返回值都不变」
从 v2.11c 起不再成立：DeepSeek 命令行的请求体、超时、日志仍和金样本逐字节相同，拿到过回复的搜索的返回值只多 candidates 这一个键
（tests/test_providers.py 对 4 个 case 写明了豁免）。回复里没有搜索结果（只有文字、use 没有结果块、Responses status failed）也加，
by_query 是空列表；一轮回复都没拿到（请求失败、读超时不重发）时返回值不变，没有这个键。

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


def by_query(parsed_rounds: list) -> list:
    """v2.11c：各轮 search_unpack 的 groups 汇总成 candidates.by_query。每组 {query 或 queries, urls[, error]}；urls 用 parse_urls
    规范化（同选中的 URL：去尾部标点、去 #fragment、组内去重保序），不截断，不带标题。
    Anthropic 格式（DeepSeek / Claude，组里有 tool_use_id）：各轮拼起来，先按 tool_use_id 对 server_tool_use 的 id；id 对得上、但那个
    查询词已被前面同 id 的组配走的（同一个 id 出现两次），仍记那个查询词；没有 id 或对不上任何查询词的组，按先进先出配给还没配上的
    查询词；还配不上就记 query None。OpenAI / Kimi 的组带 queries 列表，GLM 的组 query 是 None，照原样。"""
    uses = [(i, q) for p in parsed_rounds for i, q in zip(p.get("query_ids") or [], p["queries"])]
    groups = [g for p in parsed_rounds for g in p.get("groups") or []]
    free, pick = list(range(len(uses))), {}   # free：还没配上的查询词（按出现顺序）；pick：组号 -> 查询词号
    for gi, g in enumerate(groups):
        if g.get("tool_use_id") is not None:
            ui = next((u for u in free if uses[u][0] == g["tool_use_id"]), None)
            if ui is not None:
                pick[gi] = ui
                free.remove(ui)
    out = []
    for gi, g in enumerate(groups):
        if "tool_use_id" in g:
            tid = g["tool_use_id"]
            same = None if tid is None else next((u for u, (i, _) in enumerate(uses) if i == tid), None)
            if gi not in pick and same is not None:   # id 对得上，只是查询词已被同 id 的组配走：仍记它，不占先进先出
                pick[gi] = same
            elif gi not in pick and free:   # 没有 id 或对不上任何查询词：先进先出
                pick[gi] = free.pop(0)
            row = {"query": uses[pick[gi]][1] if gi in pick else None}
        elif "queries" in g:
            row = {"queries": list(g["queries"])}
        else:
            row = {"query": g.get("query")}
        row["urls"] = parse_urls("\n".join(g["urls"]), cap=10 ** 6)   # cap 只是不截断
        if "error" in g:
            row["error"] = g["error"]
        out.append(row)
    return out


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
        content 原样回传续上（最多 adapter.max_search_continuations 次），每次请求各记一行日志，结果合并。
        v2.10h：五家都走这一条路（各家自带的搜索工具）；自带 key 的运行把区域交给 adapter（GLM 两站的搜索引擎不同）。
        v2.10i：缺 usage 按预扣记账、status failed 报错、Kimi / GLM 读超时不重发（见模块说明和 _request）。
        v2.11c：拿到过回复时多一个 candidates（各查询词的全部结果 URL，见 by_query）；一轮都没拿到时没有这个键。"""
        sp = self.spec
        ad = DEEPSEEK if sp is None else sp.adapter
        url = SEARCH_URL if sp is None else ad.search_url(sp.region)
        fee = SEARCH_FEE_ASSUMED_USD if sp is None else search_fee_usd(sp.price_id)
        price_model = self.model if sp is None else sp.price_id
        effort, out_tokens = (None, MAX_TOKENS["search"]) if sp is None else sp.tokens_for("search", MAX_TOKENS["search"])
        # DeepSeek 的请求体两条路都和 v2.9b 相同（v2.10g：用户 10-21 定搜索请求保持原样；region 不进请求体）
        headers, payload = ad.search_request(self.model, self._key if sp is None else sp.key, prompt, max_tokens=out_tokens,
                                             max_uses=max_uses, effort=effort, region=None if sp is None else sp.region)
        # v2.10i：这次搜索的预扣（token 部分, 搜索费部分），和 pipeline.Budget.search_reserve 同一个算法：回复没给 usage、读超时不重发时按它记账
        reserve = (lambda: self._reserve_usd(price_model, out_tokens, max_uses, fee))
        rounds, error, failed = [], None, None
        for n in range(ad.max_search_continuations + 1):
            if n and self.renew is not None and not self.renew():   # v2.10f：续接也按最坏情况预扣，放不下就不续
                error = "not sent: the spending cap has no room for another worst-case search request"
                break
            rec = {"arm": role, "qid": qid, "model": self.model, "kind": "search"}
            if n:
                rec["continuation"] = n
            got = self._request(ad, url, headers, payload, rec, role, qid, reserve)
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
            if sp is not None and not parsed["usage"]:
                # v2.10i：自带 key 的运行里回复没给 usage（Kimi Responses 的 usage 可以是 null；GLM 缺 usage）：token 按这次搜索预扣的
                # token 部分记账，不按 0（同 llm.py 的 JSON 调用，v2.10f）。搜索费照旧按回复里的搜索次数。命令行（DeepSeek）不变
                usd = reserve()[0]
                rec.update(usd=round(usd, 6), usage_missing=True, usd_basis="reserve (usage missing)")
            if parsed.get("error") is not None:
                # v2.10i：HTTP 200 但 status failed（Responses）：error.code / message 先 redact（这次运行的 key）再记、再往外报
                e = parsed["error"]
                redact = None if sp is None else sp.redact
                rec.update(ok=False, error="response_failed", server_error_code=llm.scrub_server_text(e["code"], redact, 60),
                           server_error=llm.scrub_server_text(e["message"], redact))
                failed = "response_failed" + llm.server_error_detail(rec)
            self._log(rec)
            rounds.append((parsed, usd))
            if failed:
                break
            payload = ad.search_continue(payload, d)
            if payload is None:
                break
        if not rounds:   # v2.10i：读超时不重发时 rec 里记了预扣（usd），返回值跟着记；其余失败照旧是 0
            return {"queries": [], "urls": [], "error": error, "web_search_requests": 0,
                    "usd": float(rec.get("usd") or 0.0), "usd_search_fee_assumed": float(rec.get("usd_search_fee_assumed") or 0.0)}
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
        # 返回给调用方的只有：查询词（只进 state.json 审计，不进任何分析 prompt）、URL、计量、candidates（v2.11c，同查询词只进 state.json）。
        # 搜索结果的标题不往外传
        out = {"queries": queries, "urls": urls, "n_text_urls": len(text_urls), "n_result_urls": len(result_urls),
               "web_search_requests": n_req, "usd": usd, "usd_search_fee_assumed": n_req * fee}
        if len(rounds) > 1:
            out["continuations"] = len(rounds) - 1
        if not getattr(ad, "search_reports_queries", True):   # v2.10i（GLM）：回复里没有查询词，账本据此不写「(none)」
            out["queries_reported"] = False
        if failed:
            out["error"] = failed if len(rounds) == 1 else f"continuation {len(rounds) - 1}: {failed}"
        elif error:
            out["error"] = f"continuation {len(rounds)}: {error}"
        out["candidates"] = {"provider": ad.provider, "by_query": by_query([p for p, _ in rounds])}
        return out

    def _reserve_usd(self, price_model: str, out_tokens: int, max_uses: int, fee: float) -> tuple:
        """v2.10i：这次搜索请求的预扣 (token 部分, 搜索费部分)，同 pipeline.Budget.search_reserve：输入按 SEARCH_INPUT_TOKENS（自带 key 的
        运行按 SEARCH_INPUT_TOKENS_BYOK，同 configure_byok），输出按发出的 max tokens，加 (2 x max_uses + 2) 次搜索费。"""
        from .pipeline import Budget   # 这里才 import：pipeline 本身 import 本模块
        n_in = Budget.SEARCH_INPUT_TOKENS if self.spec is None else Budget.SEARCH_INPUT_TOKENS_BYOK
        return Budget.search_tokens_reserve(price_model, n_in, out_tokens), (2 * max_uses + 2) * fee

    def _request(self, ad, url: str, headers: dict, payload: dict, rec: dict, role: str, qid: str, reserve=None):
        """发一次搜索请求（传输层失败最多试 3 次）。成功返回 (解析后的 dict, 开始时刻)，失败返回 None（原因在 rec 里）。
        余额不足抛 llm.BalanceExhausted。v2.10i：单次读超时取 adapter 的 search_timeout_s（没有就 600 秒，DeepSeek / Claude / GPT 不变）；
        adapter 的 search_resend_after_timeout 是 False 时（Kimi、GLM：搜索是整段思考生成的非流式请求），请求发出后读超时就不重发
        （服务端可能照样处理、照样计费），这次请求按预扣（reserve() = (token 部分, 搜索费部分)）记账。"""
        body = json.dumps(payload).encode("utf-8")
        timeout = getattr(ad, "search_timeout_s", 600)
        for http_try in range(1, 4):
            started = datetime.now(timezone.utc)
            t0 = time.time()
            req = urllib.request.Request(url, data=body, method="POST", headers=headers)
            wait_hint = None
            try:
                # 不跟随跳转（D9）：3xx 以 HTTPError 回来，下面记成 http_3xx 错误返回，key 不会发到别的地址
                with llm.urlopen_no_redirect(req, timeout=timeout) as r:
                    status, raw = r.status, r.read()
            except urllib.error.HTTPError as e:
                status, raw = e.code, (llm.read_error_body(e) if e.code in ad.error_body_statuses else b"")
                wait_hint = llm.retry_after(ad, e.headers)
                e.close()
            except TimeoutError as e:
                # 等回复头或读 body 时超时（请求已经发出去了；连接阶段的超时 urllib 包成 URLError，走下面那条照旧重试）
                if getattr(ad, "search_resend_after_timeout", True) or reserve is None:
                    rec.update(ok=False, error=type(e).__name__, http_try=http_try)
                    time.sleep(3 * http_try)
                    continue
                tok, fees = reserve()
                rec.update(ok=False, error=type(e).__name__, http_try=http_try, timeout_s=timeout, resent=False,
                           usd=round(tok, 6), usd_search_fee_assumed=round(fees, 4), usd_basis="reserve (read timeout, not resent)")
                return None
            except (urllib.error.URLError, OSError) as e:
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

"""子 agent 流水线与运行上下文：预算、带日志的 LLM、SEARCHER -> FETCHER -> EXTRACTOR -> 代码核对。
v2.5 真实使用（ctx.live_fetch）：一个方向的几个 URL 同时直接抓 live 页（fetch_live，不查 Wayback），按 URL 顺序抽取；
每页核对完的点交给 ctx.early（published.EarlyWatch），确认了已公布的目标值就停下其余子 agent。回测的流程没有改。"""
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import date, datetime, timezone

from ..config import MAX_TOKENS, MODEL, PRICES
from ..llm import LLM, TransportError
from . import evidence as ev
from .fetch import fetch_live, fetch_page
from .prompts import EXTRACT_SYSTEM, EXTRACT_USER, SEARCH_USER
from .search import SEARCH_FEE_ASSUMED_USD, Searcher

MAX_CHARS_TO_EXTRACTOR = 24_000
QUOTE_STORE_CHARS = 200


class BudgetExceeded(RuntimeError):
    pass


class Budget:
    """每题的上限。USD 包括 token 成本和按假设单价记的搜索费。
    每次调用前在锁里按「最坏情况」预扣（hold），调用结束后退回预扣、只留实际花费；已花 + 在途预扣 + 这次预扣
    超过上限就不发这次调用（抛 BudgetExceeded，各节点据此干净收尾）。预扣按上限估：LLM 按输入字符数 / 2 个 token
    和 max_tokens 个输出 token、峰时价；搜索按 token 上限加 (2 x max_uses + 2) 次搜索费（实测最多 6 次 / max_uses 3）。
    v2.5.5：先拿并发名额（sem）再预扣，排队等名额的调用不占预扣，在途预扣最多 llm_concurrency 份。
    方向数不写死，由页面和美元预算推出来（max_directions）。"""

    # 规划方向数用的「一个方向的典型花费」：实测搜索中位 $0.047（含假设的搜索费）+ 4 次抽取约 $0.006 + 挑页 $0.002
    TYPICAL_DIRECTION_USD = 0.06
    ROUND1_USD_SHARE = 0.6   # 第一轮方向最多用掉上限的 60%，其余留给 base-rate 方向、裁判、终稿

    def __init__(self, usd: float = 1.00, pages: int = 48, round1_pages: int = 40, llm_concurrency: int = 8,
                 extra_directions: int = 3, urls_per_direction: int = 4, search_max_uses: int = 3,
                 max_directions_hard: int = 16):
        self.usd_cap, self.pages_cap, self.round1_pages = usd, pages, round1_pages
        self.extra_directions = extra_directions
        self.urls_per_direction, self.search_max_uses = urls_per_direction, search_max_uses
        self.directions = max(1, min(max_directions_hard, round1_pages // urls_per_direction,
                                     int(self.ROUND1_USD_SHARE * usd / self.TYPICAL_DIRECTION_USD)))
        self.usd_tokens = 0.0
        self.usd_search_fee = 0.0
        self.reserved = 0.0
        self.pages_used = 0
        self.n_calls = 0
        self.aborted = ""
        self.sem = threading.BoundedSemaphore(llm_concurrency)
        self._lock = threading.Lock()

    @property
    def usd(self):
        return self.usd_tokens + self.usd_search_fee

    def add(self, rec: dict):
        with self._lock:
            self.n_calls += 1
            self.usd_tokens += float(rec.get("usd") or 0)
            self.usd_search_fee += float(rec.get("usd_search_fee_assumed") or 0)
            if self.usd > self.usd_cap and not self.aborted:
                self.aborted = f"usd cap {self.usd_cap} exceeded ({self.usd:.4f})"

    @contextmanager
    def hold(self, amount: float):
        """预扣 amount；已花 + 在途预扣 + amount 超过上限就抛 BudgetExceeded。退出时退回预扣（实际花费已由 add 记入）。"""
        with self._lock:
            if self.aborted or self.usd + self.reserved + amount > self.usd_cap:
                self.aborted = self.aborted or (f"usd cap {self.usd_cap} would be exceeded "
                                                f"(spent {self.usd:.4f} + in flight {self.reserved:.4f} + {amount:.4f})")
                raise BudgetExceeded(self.aborted)
            self.reserved += amount
        try:
            yield
        finally:
            with self._lock:
                self.reserved -= amount

    @staticmethod
    def llm_reserve(prompt_chars: int, max_tokens: int) -> float:
        hit, miss, out = PRICES.get(MODEL, PRICES["deepseek-flash"])["peak"]
        return (prompt_chars / 2 * miss + max_tokens * out) / 1e6

    def search_reserve(self) -> float:
        hit, miss, out = PRICES.get(MODEL, PRICES["deepseek-flash"])["peak"]
        return (30_000 * miss + MAX_TOKENS["search"] * out) / 1e6 + (2 * self.search_max_uses + 2) * SEARCH_FEE_ASSUMED_USD

    def reserve_page(self, round_no: int) -> bool:
        cap = self.round1_pages if round_no == 1 else self.pages_cap
        with self._lock:
            if self.pages_used >= cap:
                return False
            self.pages_used += 1
            return True

    def release_page(self):
        with self._lock:
            self.pages_used -= 1

    def snapshot(self):
        return {"usd_total_assumed": round(self.usd, 4), "usd_tokens": round(self.usd_tokens, 4),
                "usd_search_fee_assumed": round(self.usd_search_fee, 4), "usd_cap": self.usd_cap,
                "pages_used": self.pages_used, "pages_cap": self.pages_cap, "round1_pages": self.round1_pages,
                "max_directions": self.directions, "urls_per_direction": self.urls_per_direction,
                "n_calls_logged": self.n_calls, "aborted": self.aborted}


class AgentLLM(LLM):
    """llm.LLM 加两件事：调用前先占一个并发名额、再查预算；每条日志同时计入预算。"""

    def __init__(self, calls_path, budget: Budget):
        super().__init__(calls_path=calls_path)
        self.budget = budget

    def _log(self, rec: dict):
        super()._log(rec)
        if "usd" in rec:
            self.budget.add(rec)

    def ask(self, system: str, user: str, *, role: str, qid: str, max_tokens: int = MAX_TOKENS["final"], tries: int = 2):
        """返回 (dict|None, error)。输出无效时带着错误信息重试一次。"""
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        err = None
        for attempt in range(1, tries + 1):
            need = Budget.llm_reserve(sum(len(m["content"]) for m in msgs), max_tokens)
            with self.budget.sem, self.budget.hold(need):
                try:
                    out, text, err = self.json_call(msgs, arm=role, qid=qid, attempt=attempt, max_tokens=max_tokens)
                except TransportError as e:
                    return None, f"transport: {e}"
            if out is not None:
                return out, None
            ask_again = (f"Your reply was cut off at the output limit ({err}). Reply again with one complete, valid JSON "
                         "object that is shorter: keep notes and reasons brief."
                         if "truncated" in (err or "") else f"Your reply was rejected: {err}. Reply again with one valid JSON object.")
            msgs = msgs[:2] + [{"role": "assistant", "content": (text or "")[:2000]}, {"role": "user", "content": ask_again}]
        return None, err


class Context:
    """一题一个：预算、LLM、SEARCHER、哨兵、as_of。图的节点通过闭包拿到它，不放进 LangGraph state。"""

    def __init__(self, qid: str, question: str, as_of: str, calls_path, leak_value=None, budget: Budget | None = None,
                 ablate_own_history: bool = False):
        self.qid, self.question, self.as_of_s = qid, question, as_of
        self.as_of = date.fromisoformat(as_of)
        self.ablate_own_history = ablate_own_history  # 回测消融：见 ablation.py
        self.check_published = False  # v2.4「答案已公布」检查（published.py）：只有 run.prepare_run 在真实使用时打开
        self.live_fetch = False  # v2.5 直接抓 live 页（fetch_live）：同上，只在真实使用时打开
        self.early = None        # v2.5 提前停（published.EarlyWatch）：同上
        self.budget = budget or Budget()
        self.calls_path = calls_path
        self.llm = AgentLLM(calls_path, self.budget)
        self.searcher = Searcher(log=self.llm._log)
        # 哨兵只在代码里用：真值（和其他 as_of 之后才公布的已知值）不进任何 prompt。可以是一个数或一组数
        self.leak_patterns = ev.leak_patterns(leak_value) if leak_value else []
        self.progress = None  # 可选的进度回调 progress(event: dict)，网页用；只读通知，不影响运行


def _emit(ctx, **event):
    """把进度事件交给 ctx.progress（没有就跳过）。回调出任何错都吞掉：进度显示不能影响运行。"""
    cb = getattr(ctx, "progress", None)
    if cb is not None:
        try:
            cb(event)
        except Exception:  # noqa: BLE001
            pass


def verify_point(raw: dict, text_n: str, as_of: date, page_date, allow_no_period: bool, url: str = "") -> tuple:
    """返回 (point|None, reason)。quote 逐字在页面里、value_as_written 在 quote 里、数字和倍数由代码解析、日期 <= as_of。"""
    if not isinstance(raw, dict):
        return None, "not an object"
    q, vw = ev.norm(str(raw.get("quote") or "")), ev.norm(str(raw.get("value_as_written") or ""))
    if not q or not vw:
        return None, "missing quote or value_as_written"
    if len(q) > 400:
        return None, "quote longer than 400 chars"
    span = ev.quote_span(q, text_n)
    if span is None:
        return None, "quote not found verbatim in page (elisions must skip <= 150 chars within one sentence)"
    i = ev.find_value(q, vw)
    if i < 0:
        return None, "value_as_written not in quote as a whole number"
    sw = str(raw.get("scale_word") or "")
    try:
        value, is_pct = ev.parse_value(vw, sw)
    except ValueError as e:
        return None, f"number: {e}"
    if cut := ev.cjk_fragment(q, vw, sw):   # v2.6e：只写了更大的中日韩数字的一截（1億3000万 里的 1億3000）就丢，不静默读错
        return None, f"number: {cut}"
    basis = ev.scale_supported(sw, q, text_n[max(0, span[0] - ev.HEADER_WINDOW_CHARS):span[0]], vw)
    if not basis:
        return None, f"scale word {sw!r} not supported by quote or table header"
    why = ev.date_check(raw, as_of, page_date, allow_no_period=allow_no_period)
    if why:
        return None, why
    # 抽取员给的期间年份必须在页面正文或网址里出现过（v2.1b 韩国题：旧页面上「7 月（报告当年）」被标成了 2026 年 7 月）
    # v2.6e：页面只写纪年（令和8年、民國115年、台湾的「115年」）时也算出现过（evidence.era_years）；period_end 本身写成纪年
    # （parse_date 现在认「令和8年3月」）时换成公历年再查，不让这种写法绕过检查
    pe_s = str(raw.get("period_end") or "")
    y = pe_s[:4]
    if not y.isdigit() and not pe_s[:1].isascii() and (pe := ev.parse_date(pe_s, end=True)):
        y = str(pe.year)
    if y.isdigit() and y not in text_n and y not in url and not (y.isdecimal() and int(y) in ev.era_years(text_n)):
        return None, f"period year {y} does not appear in the page text or URL (likely mis-dated)"
    unit = "%" if is_pct else str(raw.get("unit") or "")[:60]
    lo = max(0, min(i - 80, len(q) - QUOTE_STORE_CHARS))
    return {"name": str(raw.get("name") or "")[:160], "value": value, "value_as_written": vw, "scale_word": sw,
            "scale_basis": basis, "unit": unit, "period_start": str(raw.get("period_start") or ""),
            "period_end": str(raw.get("period_end") or ""),
            "published_at_if_visible": str(raw.get("published_at_if_visible") or ""),
            "quote": q[lo:lo + QUOTE_STORE_CHARS]}, ""


def _process_page(ctx: Context, target: dict, d: dict, round_no: int, page: dict, text, out: dict,
                  allow_no_period: bool) -> list:
    """取到的一页：哨兵 -> 抽取 -> 代码核对，记进 out。返回这一页核对通过的点（v2.5 提前停检查用）。"""
    _emit(ctx, kind="page", direction_id=d["id"], status=page.get("status"))
    if page["status"] == "dropped":
        ctx.budget.release_page()
        out["pages"].append(page)
        return []
    hits = ev.leak_scan(text, ctx.leak_patterns)
    page["leak_hits"] = hits
    if hits:
        page["status_detail"] = "excluded: leak sentinel hit"
        out["pages"].append(page)
        return []
    sent = text[:MAX_CHARS_TO_EXTRACTOR]
    page.update(chars_sent=len(sent), truncated=len(text) > len(sent),
                late_dates_in_sent_text=[x.isoformat() for x in ev.late_dates(sent, ctx.as_of, date.today())][:10])
    res, err = ctx.llm.ask(EXTRACT_SYSTEM, EXTRACT_USER.format(
        text=sent, **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end")},
        hypothesis=str(d.get("hypothesis", ""))[:600], data_to_find=str(d.get("data_to_find", ""))[:600]),
        role=f"extract:{d['id']}", qid=ctx.qid, max_tokens=MAX_TOKENS["extract"])
    page["extract_error"] = err
    text_n = ev.norm(sent)
    raws = (res or {}).get("points") or []
    page["n_points_raw"] = len(raws) if isinstance(raws, list) else 0
    new = []
    for j, r in enumerate(raws if isinstance(raws, list) else []):
        pd = date.fromisoformat(page["page_date"]) if page.get("page_date") else None
        p, why = verify_point(r, text_n, ctx.as_of, pd, allow_no_period, url=page["url"])
        base = {"direction_id": d["id"], "round": round_no, "source_url": page["url"], "via": page["status"],
                "page_date": page.get("page_date"), "snapshot_ts": page.get("snapshot_ts"), "order": (len(out["pages"]), j)}
        if p is None:
            out["dropped_points"].append({**base, "reason": why, "name": str((r or {}).get("name", ""))[:120]
                                          if isinstance(r, dict) else "", "value_as_written": str((r or {}).get("value_as_written", ""))[:40]
                                          if isinstance(r, dict) else ""})
        else:
            new.append({**base, **p, "verified_by": "quote_in_page"})
            out["points"].append(new[-1])
    page["n_points_verified"] = len(new)
    out["pages"].append(page)
    _emit(ctx, kind="extracted", direction_id=d["id"], n_verified=len(new))
    return new


def _timed_live(url: str, as_of: date, qid: str) -> dict:
    """fetch_live 加计时（fetch_at = 开始时刻 UTC，fetch_s = 用时，含按 host 限速排队的时间）。"""
    t0, at = time.time(), datetime.now(timezone.utc).isoformat(timespec="seconds")
    page = fetch_live(url, as_of, qid)
    page.update(fetch_at=at, fetch_s=round(time.time() - t0, 2))
    return page


def _live_pages(ctx: Context, target: dict, d: dict, round_no: int, urls: list, out: dict, allow_no_period: bool):
    """v2.5 真实使用：这个方向的 URL 同时开抓（fetch_live；同一 host 的请求由 net 的限速排队，robots 照旧），按 URL 顺序
    抽取（点的编号因此可复现）。每页核对完的点交给 ctx.early；确认了已公布的值就不再抽取，没开始的抓取取消。"""
    b, w = ctx.budget, getattr(ctx, "early", None)
    ok = [b.reserve_page(round_no) for _ in urls]
    pool = ThreadPoolExecutor(max_workers=max(1, sum(ok)), thread_name_prefix=f"fetch-{d['id']}")
    futs = [pool.submit(_timed_live, u, ctx.as_of, ctx.qid) if k else None for u, k in zip(urls, ok)]
    def stopped(i):   # 已确认已公布的值：这一页和后面的页不再抽取，名额退回
        if w is None or not w.stop.is_set():
            return False
        for _ in [f for f in futs[i:] if f is not None]:
            b.release_page()
        out["stopped"] = w.stop_reason
        return True

    try:
        for i, (url, fut) in enumerate(zip(urls, futs)):
            if fut is None:
                out["pages"].append({"url": url, "status": "dropped", "reason": "page cap reached"})
                continue
            if stopped(i):
                break
            page = fut.result()
            if stopped(i):   # v2.5.1：等这一页的时候别的子 agent 已经确认了（published2 的 d5 多抽了一页）
                break
            new = _process_page(ctx, target, d, round_no, page, page.pop("text", None), out, allow_no_period)
            if w is not None and new:
                w.offer(ctx.llm, ctx.qid, target, ctx.as_of_s, ctx.as_of, new)
    finally:
        pool.shutdown(wait=False, cancel_futures=True)


class _Stopped(Exception):
    """v2.5 提前停：这个方向开始搜索之前，已经确认了已公布的值。"""


def run_direction(ctx: Context, target: dict, d: dict, round_no: int) -> dict:
    """一个子 agent：搜索（只取 URL）-> 逐个取快照 -> 哨兵 -> 抽取 -> 代码核对。异常和预算耗尽都在这里收住。
    v2.5 真实使用：同时直接抓 live 页（_live_pages）；ctx.early 确认了已公布的值以后，还没做的步骤不再做（out["stopped"]）。"""
    t0 = time.time()
    b = ctx.budget
    w = getattr(ctx, "early", None)
    out = {"direction_id": d["id"], "round": round_no, "search": {}, "pages": [], "points": [], "dropped_points": []}
    _emit(ctx, kind="direction_start", direction_id=d["id"], round=round_no)
    try:
        if w is not None and w.stop.is_set():
            out["stopped"] = w.stop_reason
            raise _Stopped
        prompt = SEARCH_USER.format(cap=b.urls_per_direction, as_of=ctx.as_of_s,
                                    hints="; ".join(map(str, d.get("search_hints") or []))[:400],
                                    **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end", "publisher")},
                                    **{k: str(d.get(k, ""))[:600] for k in ("category", "perspective", "hypothesis", "data_to_find")})
        with b.sem, b.hold(b.search_reserve()):
            s = ctx.searcher.search(prompt, role=f"search:{d['id']}", qid=ctx.qid, max_uses=b.search_max_uses,
                                    cap=b.urls_per_direction)
        out["search"] = s
        _emit(ctx, kind="searched", direction_id=d["id"], n_urls=len(s.get("urls", [])[: b.urls_per_direction]))
        allow_no_period = d.get("category") == "base_rates"
        urls = s.get("urls", [])[: b.urls_per_direction]
        # v2.6c 回测泄漏护栏（D3）：查询词里出现登记值（哨兵的写法），这个方向作废：不取页、不重搜，命中的写法记进
        # search.voided。真实使用没有登记值（ctx.leak_patterns 为空），不受影响
        voided = sorted({h for q in s.get("queries") or [] for h in ev.leak_scan(str(q), ctx.leak_patterns)})
        if voided:
            out["search"] = {**s, "voided": voided}
        elif w is not None and w.stop.is_set():
            out["stopped"] = w.stop_reason
        elif getattr(ctx, "live_fetch", False):
            _live_pages(ctx, target, d, round_no, urls, out, allow_no_period)
        else:
            for url in urls:
                if not b.reserve_page(round_no):
                    out["pages"].append({"url": url, "status": "dropped", "reason": "page cap reached"})
                    continue
                page = fetch_page(url, ctx.as_of, ctx.qid)
                _process_page(ctx, target, d, round_no, page, page.pop("text", None), out, allow_no_period)
    except _Stopped:
        pass
    except BudgetExceeded as e:
        out["aborted"] = str(e)
    except Exception as e:  # noqa: BLE001  一个方向的意外错误不拖垮整题，记下来
        out["error"] = f"{type(e).__name__}: {e}"[:300]
    out["wall_s"] = round(time.time() - t0, 1)
    _emit(ctx, kind="direction_done", direction_id=d["id"], round=round_no, n_points=len(out["points"]),
          stopped=out.get("error") or out.get("aborted") or out.get("stopped"))
    return out


def dumps(x) -> str:
    return json.dumps(x, ensure_ascii=False, default=str)

"""子 agent 流水线与运行上下文：预算、带日志的 LLM、SEARCHER -> FETCHER -> EXTRACTOR -> 代码核对。"""
import json
import threading
import time
from datetime import date

from ..llm import LLM, TransportError
from . import evidence as ev
from .fetch import fetch_page
from .prompts import EXTRACT_SYSTEM, EXTRACT_USER, SEARCH_USER
from .search import Searcher

MAX_CHARS_TO_EXTRACTOR = 24_000
QUOTE_STORE_CHARS = 200


class BudgetExceeded(RuntimeError):
    pass


class Budget:
    """每题的硬上限。USD 包括 token 成本和按假设单价记的搜索费；超了就抛 BudgetExceeded，各节点据此干净收尾。"""

    def __init__(self, usd: float = 1.00, pages: int = 40, round1_pages: int = 32, llm_concurrency: int = 8,
                 directions: int = 8, extra_directions: int = 3, urls_per_direction: int = 5, search_max_uses: int = 3):
        self.usd_cap, self.pages_cap, self.round1_pages = usd, pages, round1_pages
        self.directions, self.extra_directions = directions, extra_directions
        self.urls_per_direction, self.search_max_uses = urls_per_direction, search_max_uses
        self.usd_tokens = 0.0
        self.usd_search_fee = 0.0
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

    def check(self, reserve: float = 0.0):
        if self.aborted or self.usd + reserve > self.usd_cap:
            self.aborted = self.aborted or f"usd cap {self.usd_cap} would be exceeded"
            raise BudgetExceeded(self.aborted)

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
                "pages_used": self.pages_used, "pages_cap": self.pages_cap, "n_calls_logged": self.n_calls,
                "aborted": self.aborted}


class AgentLLM(LLM):
    """llm.LLM 加两件事：调用前查预算并占一个并发名额；每条日志同时计入预算。"""

    def __init__(self, calls_path, budget: Budget):
        super().__init__(calls_path=calls_path)
        self.budget = budget

    def _log(self, rec: dict):
        super()._log(rec)
        if "usd" in rec:
            self.budget.add(rec)

    def ask(self, system: str, user: str, *, role: str, qid: str, max_tokens: int = 4000, tries: int = 2):
        """返回 (dict|None, error)。输出无效时带着错误信息重试一次。"""
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        err = None
        for attempt in range(1, tries + 1):
            self.budget.check(reserve=0.01)
            with self.budget.sem:
                try:
                    out, text, err = self.json_call(msgs, arm=role, qid=qid, attempt=attempt, max_tokens=max_tokens)
                except TransportError as e:
                    return None, f"transport: {e}"
            if out is not None:
                return out, None
            msgs = msgs[:2] + [{"role": "assistant", "content": (text or "")[:2000]},
                               {"role": "user", "content": f"Your reply was rejected: {err}. Reply again with one valid JSON object."}]
        return None, err


class Context:
    """一题一个：预算、LLM、SEARCHER、哨兵、as_of。图的节点通过闭包拿到它，不放进 LangGraph state。"""

    def __init__(self, qid: str, question: str, as_of: str, calls_path, leak_value=None, budget: Budget | None = None):
        self.qid, self.question, self.as_of_s = qid, question, as_of
        self.as_of = date.fromisoformat(as_of)
        self.budget = budget or Budget()
        self.calls_path = calls_path
        self.llm = AgentLLM(calls_path, self.budget)
        self.searcher = Searcher(log=self.llm._log)
        # 哨兵只在代码里用：真值不进任何 prompt
        self.leak_patterns = ev.leak_patterns(leak_value) if leak_value is not None else []


def verify_point(raw: dict, text_n: str, as_of: date, page_date, allow_no_period: bool) -> tuple:
    """返回 (point|None, reason)。quote 逐字在页面里、value_as_written 在 quote 里、数字和倍数由代码解析、日期 <= as_of。"""
    if not isinstance(raw, dict):
        return None, "not an object"
    q, vw = ev.norm(str(raw.get("quote") or "")), ev.norm(str(raw.get("value_as_written") or ""))
    if not q or not vw:
        return None, "missing quote or value_as_written"
    if len(q) > 400:
        return None, "quote longer than 400 chars"
    if not ev.quote_in_text(q, text_n):
        return None, "quote not found verbatim in page"
    if vw not in q:
        return None, "value_as_written not in quote"
    sw = str(raw.get("scale_word") or "")
    try:
        value, is_pct = ev.parse_value(vw, sw)
    except ValueError as e:
        return None, f"number: {e}"
    basis = ev.scale_supported(sw, q, text_n)
    if not basis:
        return None, f"scale word {sw!r} not supported by quote or page header"
    why = ev.date_check(raw, as_of, page_date, allow_no_period=allow_no_period)
    if why:
        return None, why
    unit = "%" if is_pct else str(raw.get("unit") or "")[:60]
    i = q.find(vw)
    lo = max(0, min(i - 80, len(q) - QUOTE_STORE_CHARS))
    return {"name": str(raw.get("name") or "")[:160], "value": value, "value_as_written": vw, "scale_word": sw,
            "scale_basis": basis, "unit": unit, "period_start": str(raw.get("period_start") or ""),
            "period_end": str(raw.get("period_end") or ""),
            "published_at_if_visible": str(raw.get("published_at_if_visible") or ""),
            "quote": q[lo:lo + QUOTE_STORE_CHARS]}, ""


def run_direction(ctx: Context, target: dict, d: dict, round_no: int) -> dict:
    """一个子 agent：搜索（只取 URL）-> 逐个取快照 -> 哨兵 -> 抽取 -> 代码核对。异常和预算耗尽都在这里收住。"""
    t0 = time.time()
    b = ctx.budget
    out = {"direction_id": d["id"], "round": round_no, "search": {}, "pages": [], "points": [], "dropped_points": []}
    try:
        b.check(reserve=0.05)
        prompt = SEARCH_USER.format(cap=b.urls_per_direction, as_of=ctx.as_of_s,
                                    hints="; ".join(map(str, d.get("search_hints") or []))[:400],
                                    **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end", "publisher")},
                                    **{k: str(d.get(k, ""))[:600] for k in ("category", "perspective", "hypothesis", "data_to_find")})
        with b.sem:
            s = ctx.searcher.search(prompt, role=f"search:{d['id']}", qid=ctx.qid, max_uses=b.search_max_uses,
                                    cap=b.urls_per_direction)
        out["search"] = s
        allow_no_period = d.get("category") == "base_rates"
        for url in s.get("urls", [])[: b.urls_per_direction]:
            if not b.reserve_page(round_no):
                out["pages"].append({"url": url, "status": "dropped", "reason": "page cap reached"})
                continue
            page = fetch_page(url, ctx.as_of, ctx.qid)
            text = page.pop("text", None)
            if page["status"] == "dropped":
                b.release_page()
                out["pages"].append(page)
                continue
            hits = ev.leak_scan(text, ctx.leak_patterns)
            page["leak_hits"] = hits
            if hits:
                page["status_detail"] = "excluded: leak sentinel hit"
                out["pages"].append(page)
                continue
            sent = text[:MAX_CHARS_TO_EXTRACTOR]
            page.update(chars_sent=len(sent), truncated=len(text) > len(sent))
            b.check(reserve=0.01)
            res, err = ctx.llm.ask(EXTRACT_SYSTEM, EXTRACT_USER.format(
                text=sent, **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end")},
                hypothesis=str(d.get("hypothesis", ""))[:600], data_to_find=str(d.get("data_to_find", ""))[:600]),
                role=f"extract:{d['id']}", qid=ctx.qid, max_tokens=4000)
            page["extract_error"] = err
            text_n = ev.norm(sent)
            raws = (res or {}).get("points") or []
            page["n_points_raw"] = len(raws) if isinstance(raws, list) else 0
            kept = 0
            for j, r in enumerate(raws if isinstance(raws, list) else []):
                pd = date.fromisoformat(page["page_date"]) if page.get("page_date") else None
                p, why = verify_point(r, text_n, ctx.as_of, pd, allow_no_period)
                base = {"direction_id": d["id"], "round": round_no, "source_url": page["url"], "via": page["status"],
                        "page_date": page.get("page_date"), "snapshot_ts": page.get("snapshot_ts"), "order": (len(out["pages"]), j)}
                if p is None:
                    out["dropped_points"].append({**base, "reason": why, "name": str((r or {}).get("name", ""))[:120]
                                                  if isinstance(r, dict) else "", "value_as_written": str((r or {}).get("value_as_written", ""))[:40]
                                                  if isinstance(r, dict) else ""})
                else:
                    out["points"].append({**base, **p, "verified_by": "quote_in_page"})
                    kept += 1
            page["n_points_verified"] = kept
            out["pages"].append(page)
    except BudgetExceeded as e:
        out["aborted"] = str(e)
    except Exception as e:  # noqa: BLE001  一个方向的意外错误不拖垮整题，记下来
        out["error"] = f"{type(e).__name__}: {e}"[:300]
    out["wall_s"] = round(time.time() - t0, 1)
    return out


def dumps(x) -> str:
    return json.dumps(x, ensure_ascii=False, default=str)

"""运行一题或多题、写出结果、离线打分。题库不在这里：调用方（__main__）传题目列表进来。

题目 = {"id", "question", "as_of"}，可选 "answer_value"（有真值才打分）、"leak_values"（泄漏哨兵要认的值：
真值，以及同一题里所有公布日晚于 as_of 的已知官方值）、"last_year"、"source"。
agent 只拿到题目文字和 as_of。真值和哨兵值只交给代码，不进任何 prompt。没有真值（真实使用）时不打分、不显示官方值。
"""
import json
import math
import time
from datetime import date, datetime, timezone

from langgraph.types import Command

from ..config import RESULTS
from . import evidence as ev
from .evidence import parse_date
from .graph import build
from .outputs import ledger, render_graph
from .pipeline import Context

RES = RESULTS / "agent"
RESIDUAL_RISKS = [
    "The searcher sees post-cutoff search results and chooses which URLs are fetched, so page selection can be "
    "conditioned on the answer; only the URLs leave the searcher, and in backtests every fetched page is a snapshot "
    "dated <= as_of.",
    "Live pages are used only when as_of is today; in backtests every page is an archived snapshot dated <= as_of.",
    "The leak sentinel only catches registered official values in common formats, not paraphrased or derived numbers.",
    "The model's own training data (knowledge cutoff unpublished) can include history before as_of; it cannot include "
    "the target if the target was published after the model's release.",
    "Wayback snapshots are captured by a third party; a snapshot date <= as_of proves the content existed by then.",
]
BY_CONSTRUCTION = [
    "Only URLs leave the searcher (code regex); extractor, judge and final prompts never contain search result "
    "titles, snippets or the searcher's text. This holds by construction and is not measured.",
]


def _ask_human(payload: dict) -> dict:
    print(json.dumps(payload, indent=1, ensure_ascii=False))
    ans = input("Approve these directions? [y/N] ").strip().lower()
    return {"approved": ans in ("y", "yes"), "by": "human"}


def _after(s, a: date, end: bool) -> bool:
    d = parse_date(s, end=end) if isinstance(s, str) else None
    return d is not None and d > a


def leakage_audit(state: dict, as_of: str, leak_values=None) -> dict:
    """运行后的泄漏检查，全部从 state 里量出来。"""
    a = date.fromisoformat(as_of)
    pages = [pg for r in state.get("results") or [] for pg in r.get("pages") or []]
    sent = [pg for pg in pages if pg.get("chars_sent")]
    late_points = [p["id"] for p in state.get("points") or []
                   if _after(p.get("period_end"), a, True) or _after(p.get("published_at_if_visible"), a, False)
                   or _after(p.get("page_date"), a, False)]
    late_snaps = [pg["url"] for pg in pages if pg.get("snapshot_ts") and pg["snapshot_ts"][:8] > a.strftime("%Y%m%d")]
    pats = ev.leak_patterns(leak_values) if leak_values else []
    queries = [q for r in state.get("results") or [] for q in (r.get("search") or {}).get("queries") or []]
    return {"pages_total": len(pages), "pages_snapshot": sum(pg.get("status") == "snapshot" for pg in pages),
            "pages_live_dated": sum(pg.get("status") == "live_dated" for pg in pages),
            "pages_dropped": sum(pg.get("status") == "dropped" for pg in pages),
            "pages_sent_to_extractor": {"total": len(sent), "snapshot": sum(pg.get("status") == "snapshot" for pg in sent),
                                        "live_dated": sum(pg.get("status") == "live_dated" for pg in sent)},
            # 送给 extractor 的文字里，晚于 as_of、不晚于取页日的显式日期。快照页里出现的是当时写的「将来的安排」，
            # live 页里出现就是泄漏（live 页在回测里已经不收）
            "late_dates_in_text_sent": [{"url": pg["url"], "status": pg.get("status"), "dates": pg["late_dates_in_sent_text"]}
                                        for pg in sent if pg.get("late_dates_in_sent_text")],
            "sentinel_hits": [{"url": pg["url"], "hits": pg["leak_hits"]} for pg in pages if pg.get("leak_hits")],
            "points_dated_after_as_of": late_points, "snapshots_after_as_of": late_snaps,
            "searcher_queries_containing_registered_values": [q for q in queries if ev.leak_scan(q, pats)],
            "page_selection": sorted({(r.get("search") or {}).get("selection", "searcher_urls")
                                      for r in state.get("results") or [] if r.get("search")}),
            "by_construction": BY_CONSTRUCTION, "residual_risks": RESIDUAL_RISKS}


def run_question(q: dict, auto_approve: bool, tag: str = "") -> dict:
    out_dir = RES / q["id"] / tag if tag else RES / q["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    calls = out_dir / "calls.jsonl"
    if calls.exists():  # 保留之前那次运行的调用日志（失败重跑也留痕）
        calls.rename(out_dir / f"calls.before_{stamp}.jsonl")
    leak_values = q.get("leak_values") or ([q["answer_value"]] if q.get("answer_value") is not None else None)
    ctx = Context(q["id"], q["question"], q["as_of"], calls, leak_value=leak_values)
    g = build(ctx)
    cfg = {"configurable": {"thread_id": f"{q['id']}-{stamp}"}, "max_concurrency": 12, "recursion_limit": 80}
    t0 = time.time()
    out = g.invoke({"qid": q["id"], "question": q["question"], "as_of": q["as_of"]}, cfg)
    approvals = []
    while out.get("__interrupt__"):
        payload = out["__interrupt__"][0].value
        decision = {"approved": True, "by": "auto-approve"} if auto_approve else _ask_human(payload)
        approvals.append(decision)
        print(f"[{q['id']}] plan: {len(payload['directions'])} directions -> approved={decision['approved']}", flush=True)
        out = g.invoke(Command(resume=decision), cfg)
    state = dict(g.get_state(cfg).values)
    state.update(started_at=stamp, wall_s=round(time.time() - t0, 1), budget=ctx.budget.snapshot(), approvals=approvals,
                 leakage=leakage_audit(state, q["as_of"], leak_values), model=ctx.llm.model, tag=tag)
    (out_dir / "state.json").write_text(json.dumps(state, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    score = score_one(q, state)
    (out_dir / "ledger.md").write_text(ledger(state, score), encoding="utf-8")
    r = (state.get("compute") or {}).get("result") or {}
    meta = (f"as_of <b>{q['as_of']}</b> &middot; estimate <b>{_n(r.get('central'))}</b> &middot; 80% [{_n(r.get('p10'))}, "
            f"{_n(r.get('p90'))}] ({r.get('basis')})")
    if q.get("answer_value") is not None:
        meta += f" &middot; official value (scoring only) <b>{q['answer_value']:,}</b>"
    (out_dir / "graph.html").write_text(render_graph(state, f"Agent: {q['id']}", meta), encoding="utf-8")
    print(f"[{q['id']}] done in {state['wall_s']}s; estimate {_n(r.get('central'))}; usd {state['budget']['usd_total_assumed']}",
          flush=True)
    return state


def _n(v):
    return "n/a" if v is None else f"{v:,.0f}"


def score_one(q: dict, state: dict) -> dict:
    r = (state.get("compute") or {}).get("result") or {}
    est, ans = r.get("central"), q.get("answer_value")
    row = {"id": q["id"], "as_of": q["as_of"], "answer_value": ans, "source": q.get("source"), "estimate": est,
           "p10": r.get("p10"), "p90": r.get("p90"), "basis": r.get("basis"), "scored": ans is not None}
    if ans is None:  # 真实使用：没有真值，不打分
        return row
    row.update(pct_err=None if est is None else est / ans - 1,
               abs_log10_err=None if est is None else abs(math.log10(est / ans)),
               covered_80=None if est is None else r["p10"] <= ans <= r["p90"])
    return row


def score_all(questions: list, tag: str = "", forecast_summary=None) -> list:
    """离线打分：只给有真值的题打分；有 forecast_summary（已保存的另两个 arm）时一起列出。"""
    by_id = {row["id"]: row for row in forecast_summary or []}
    rows = []
    for q in questions:
        p = (RES / q["id"] / tag if tag else RES / q["id"]) / "state.json"
        if not p.exists() or q.get("answer_value") is None:
            continue
        st = json.loads(p.read_text(encoding="utf-8"))
        s = score_one(q, st)
        f = by_id.get(q["id"], {})
        ans = q["answer_value"]

        def arm(est):
            return None if est is None else {"estimate": est, "pct_err": est / ans - 1, "abs_log10_err": abs(math.log10(est / ans))}
        s["arms"] = {"agent": arm(s["estimate"]), "naive": arm((f.get("naive") or {}).get("estimate")),
                     "structured_no_retrieval": arm((f.get("structured") or {}).get("estimate")),
                     "last_year_same_period": arm(q.get("last_year"))}
        s["within_20pct"] = {k: (v is not None and abs(v["pct_err"]) <= 0.20) for k, v in s["arms"].items()}
        s["usd_total_assumed"] = st["budget"]["usd_total_assumed"]
        s["usd_tokens"] = st["budget"]["usd_tokens"]
        s["wall_s"] = st["wall_s"]
        rows.append(s)
    name = f"summary_{tag}.json" if tag else "summary.json"
    (RES / name).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    return rows


def main(questions: list, auto_approve: bool, tag: str = "", forecast_summary=None):
    for q in questions:
        run_question(q, auto_approve, tag)
    scored = [q for q in questions if q.get("answer_value") is not None]
    return score_all(scored, tag, forecast_summary) if scored else []

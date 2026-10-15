"""命令行入口：python -m triangulate agent --question <id> | --all [--auto-approve]；agent-score 离线打分。

agent 只拿到题目文字和 as_of。真值只交给代码里的泄漏哨兵和打分，不进任何 prompt。
"""
import json
import math
import time
from datetime import date, datetime, timezone

from langgraph.types import Command

from ..config import RESULTS
from ..forecast import QUESTIONS
from .graph import build
from .outputs import ledger, render_graph
from .pipeline import Context

RES = RESULTS / "agent"
RESIDUAL_RISKS = [
    "The searcher sees post-cutoff web results and may choose URLs using post-cutoff knowledge (only URLs pass; their archived "
    "versions are dated <= as_of).",
    "live_dated pages: the publication date comes from URL/metadata; a page updated later can carry newer content. "
    "The leak sentinel only catches the true value in common formats, not paraphrased or derived numbers.",
    "The model's own training data (knowledge cutoff unpublished) can include history before as_of; it cannot include "
    "the target if the target was published after the model's release.",
    "Wayback snapshots are captured by a third party; a snapshot date <= as_of proves the content existed by then.",
]


def _ask_human(payload: dict) -> dict:
    print(json.dumps(payload, indent=1, ensure_ascii=False))
    ans = input("Approve these directions? [y/N] ").strip().lower()
    return {"approved": ans in ("y", "yes"), "by": "human"}


def leakage_audit(state: dict, as_of: str) -> dict:
    a = date.fromisoformat(as_of)
    pages = [pg for r in state.get("results") or [] for pg in r.get("pages") or []]
    late_points = [p["id"] for p in state.get("points") or []
                   if (p.get("period_end") and p["period_end"][:10] > as_of) or (p.get("page_date") and p["page_date"] > as_of)]
    late_snaps = [pg["url"] for pg in pages if pg.get("snapshot_ts") and pg["snapshot_ts"][:8] > a.strftime("%Y%m%d")]
    return {"pages_total": len(pages), "pages_snapshot": sum(pg.get("status") == "snapshot" for pg in pages),
            "pages_live_dated": sum(pg.get("status") == "live_dated" for pg in pages),
            "pages_dropped": sum(pg.get("status") == "dropped" for pg in pages),
            "sentinel_hits": [{"url": pg["url"], "hits": pg["leak_hits"]} for pg in pages if pg.get("leak_hits")],
            "points_dated_after_as_of": late_points, "snapshots_after_as_of": late_snaps,
            "analysts_saw_search_results": False, "residual_risks": RESIDUAL_RISKS}


def run_question(q: dict, auto_approve: bool) -> dict:
    out_dir = RES / q["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    calls = out_dir / "calls.jsonl"
    if calls.exists():  # 保留之前那次运行的调用日志（失败重跑也留痕）
        calls.rename(out_dir / f"calls.before_{stamp}.jsonl")
    ctx = Context(q["id"], q["question"], q["as_of"], calls, leak_value=q["answer_value"])
    g = build(ctx)
    cfg = {"configurable": {"thread_id": f"{q['id']}-{stamp}"}, "max_concurrency": 9, "recursion_limit": 60}
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
                 leakage=leakage_audit(state, q["as_of"]), model=ctx.llm.model)
    (out_dir / "state.json").write_text(json.dumps(state, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    score = score_one(q, state)
    (out_dir / "ledger.md").write_text(ledger(state, score), encoding="utf-8")
    r = (state.get("compute") or {}).get("result") or {}
    meta = (f"as_of <b>{q['as_of']}</b> &middot; estimate <b>{_n(r.get('central'))}</b> &middot; 80% [{_n(r.get('p10'))}, "
            f"{_n(r.get('p90'))}] ({r.get('basis')}) &middot; official value (scoring only) <b>{q['answer_value']:,}</b>")
    (out_dir / "graph.html").write_text(render_graph(state, f"Agent: {q['id']}", meta), encoding="utf-8")
    print(f"[{q['id']}] done in {state['wall_s']}s; estimate {_n(r.get('central'))}; usd {state['budget']['usd_total_assumed']}",
          flush=True)
    return state


def _n(v):
    return "n/a" if v is None else f"{v:,.0f}"


def score_one(q: dict, state: dict) -> dict:
    r = (state.get("compute") or {}).get("result") or {}
    est, ans = r.get("central"), q["answer_value"]
    return {"id": q["id"], "as_of": q["as_of"], "answer_value": ans, "source": q["source"], "estimate": est,
            "p10": r.get("p10"), "p90": r.get("p90"), "basis": r.get("basis"),
            "pct_err": None if est is None else est / ans - 1,
            "abs_log10_err": None if est is None else abs(math.log10(est / ans)),
            "covered_80": None if est is None else r["p10"] <= ans <= r["p90"]}


def score_all() -> list:
    fc = json.loads((RESULTS / "forecast" / "summary.json").read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in fc}
    rows = []
    for q in QUESTIONS:
        p = RES / q["id"] / "state.json"
        if not p.exists():
            continue
        st = json.loads(p.read_text(encoding="utf-8"))
        s = score_one(q, st)
        f = by_id.get(q["id"], {})
        ans = q["answer_value"]

        def arm(est):
            return None if est is None else {"estimate": est, "pct_err": est / ans - 1, "abs_log10_err": abs(math.log10(est / ans))}
        s["arms"] = {"agent": arm(s["estimate"]), "naive": arm((f.get("naive") or {}).get("estimate")),
                     "structured_no_retrieval": arm((f.get("structured") or {}).get("estimate")),
                     "last_year_same_period": arm(q["last_year"])}
        s["within_20pct"] = {k: (v is not None and abs(v["pct_err"]) <= 0.20) for k, v in s["arms"].items()}
        s["usd_total_assumed"] = st["budget"]["usd_total_assumed"]
        s["usd_tokens"] = st["budget"]["usd_tokens"]
        s["wall_s"] = st["wall_s"]
        rows.append(s)
    (RES / "summary.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    return rows


def main(qids: list, auto_approve: bool):
    qs = [q for q in QUESTIONS if q["id"] in qids] if qids else QUESTIONS
    for q in qs:
        run_question(q, auto_approve)
    return score_all()

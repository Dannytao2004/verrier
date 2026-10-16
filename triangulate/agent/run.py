"""运行一题或多题、写出结果、离线打分。题库不在这里：调用方（__main__）传题目列表进来。

题目 = {"id", "question", "as_of"}，可选 "answer_value"（有真值才打分）、"leak_values"（泄漏哨兵要认的值：
真值，以及同一题里所有公布日晚于 as_of 的已知官方值）、"last_year"、"source"。
agent 只拿到题目文字和 as_of。真值和哨兵值只交给代码，不进任何 prompt。没有真值（真实使用）时不打分、不显示官方值。
"""
import html
import json
import math
import time
from datetime import date, datetime, timezone

from langgraph.types import Command

from ..config import RESULTS
from . import ablation as AB
from . import discrete as D
from . import evidence as ev
from .evidence import parse_date
from .graph import build
from .outputs import ledger, outcome_table_html, render_graph
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
    "Assumption values are proposed by the judge model from its own knowledge, which can include the target's history "
    "before as_of; code checks their form, not where the number came from.",
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
    av = state.get("assumptions") or {}
    a_text = [(a.get("id"), " ".join(str(a.get(k, "")) for k in ("name", "value", "low", "high", "rationale",
                                                                   "applies_when", "falsified_by")))
              for a in (av.get("kept") or []) + (av.get("rejected") or [])]
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
            "assumptions_containing_registered_values": [i for i, t in a_text if ev.leak_scan(t, pats)],
            "page_selection": sorted({(r.get("search") or {}).get("selection", "searcher_urls")
                                      for r in state.get("results") or [] if r.get("search")}),
            "by_construction": BY_CONSTRUCTION, "residual_risks": RESIDUAL_RISKS}


def ablation_tag(tag: str) -> str:
    """消融运行的结果单独放：tag 不以 noown 结尾就补上（v2 -> v2_noown；空 -> noown），不会覆盖正常运行。"""
    return tag if tag.endswith("noown") else (f"{tag}_noown" if tag else "noown")


def ablation_summary(state: dict) -> dict:
    """消融记录（写进 state.json 和账本）：去掉了哪些方向、按什么规则排除了哪些点、残余风险。"""
    target = (state.get("plan") or {}).get("target") or {}
    pts = state.get("points") or []
    ex = [{k: p.get(k) for k in ("id", "name", "value", "unit", "period_end", "direction_id")} | {"reason": p["ablation_excluded"]}
          for p in pts if p.get("ablation_excluded")]
    return {"own_history": True,
            "dropped_candidate_directions": [c["id"] for c in (state.get("plan") or {}).get("candidates") or []
                                             if c.get("ablation_dropped")],
            "dropped_extra_directions": [i for j in state.get("judge_rounds") or []
                                         for i in j.get("ablation_dropped_extra_directions") or []],
            "entity_anchors": AB.entity_anchors(target), "quantity_stems": sorted(AB.quantity_stems(target)),
            "n_points_total": len(pts), "n_points_excluded": len(ex), "excluded_points": ex,
            "methods_allowed": sorted(AB.ALLOWED_METHODS),
            "rule": "exclude points from own_history directions and points whose name contains a target entity anchor "
                    "and whose name or unit shares a stem with the target unit (triangulate/agent/ablation.py)",
            "residual_risks": AB.RESIDUAL_RISKS}


def checks_published(q: dict, today=None) -> bool:
    """v2.4「答案已公布」检查（published.py）只在真实使用时做：as_of 是今天（或更晚）、题目没有登记真值。
    回测和留出测试的目标值在 as_of 之后才公布，不可能是保留的点，所以不检查、不调模型。"""
    return q.get("answer_value") is None and date.fromisoformat(q["as_of"]) >= (today or date.today())


def prepare_run(q: dict, tag: str = "", ablate_own_history: bool = False) -> dict:
    """建结果目录、上下文和图（不调模型）。返回运行句柄：g、cfg、ctx、out_dir、stamp、tag、leak_values、t0。
    命令行（run_question）和网页（triangulate/web）共用；图的第一个输入是 initial_input(q)。"""
    if ablate_own_history:
        tag = ablation_tag(tag)
    out_dir = RES / q["id"] / tag if tag else RES / q["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    calls = out_dir / "calls.jsonl"
    if calls.exists():  # 保留之前那次运行的调用日志（失败重跑也留痕）
        calls.rename(out_dir / f"calls.before_{stamp}.jsonl")
    leak_values = q.get("leak_values") or ([q["answer_value"]] if q.get("answer_value") is not None else None)
    ctx = Context(q["id"], q["question"], q["as_of"], calls, leak_value=leak_values, ablate_own_history=ablate_own_history)
    # 有真值的题（回测 / 留出测试，--auto-approve 没人把关）只在题目明确标了 outcome_type = discrete 时才接受离散目标
    ctx.allow_discrete = q.get("answer_value") is None or q.get("outcome_type") == "discrete"
    ctx.check_published = checks_published(q)
    g = build(ctx)
    cfg = {"configurable": {"thread_id": f"{q['id']}-{stamp}"}, "max_concurrency": 12, "recursion_limit": 80}
    return {"q": q, "g": g, "cfg": cfg, "ctx": ctx, "out_dir": out_dir, "stamp": stamp, "tag": tag,
            "leak_values": leak_values, "ablate": ablate_own_history, "t0": time.time()}


def initial_input(q: dict) -> dict:
    return {"qid": q["id"], "question": q["question"], "as_of": q["as_of"]}


def run_question(q: dict, auto_approve: bool, tag: str = "", ablate_own_history: bool = False) -> dict:
    h = prepare_run(q, tag, ablate_own_history)
    g, cfg = h["g"], h["cfg"]
    out = g.invoke(initial_input(q), cfg)
    approvals = []
    while out.get("__interrupt__"):
        payload = out["__interrupt__"][0].value
        decision = {"approved": True, "by": "auto-approve"} if auto_approve else _ask_human(payload)
        approvals.append(decision)
        print(f"[{q['id']}] plan: {len(payload['directions'])} directions -> approved={decision['approved']}", flush=True)
        out = g.invoke(Command(resume=decision), cfg)
    return save_run(h, approvals)


def save_run(h: dict, approvals: list) -> dict:
    """图跑完以后：取最终 state，补上计量和泄漏审计，写 state.json、ledger.md、graph.html。"""
    q, g, cfg, ctx, out_dir = h["q"], h["g"], h["cfg"], h["ctx"], h["out_dir"]
    stamp, tag, leak_values, ablate_own_history, t0 = h["stamp"], h["tag"], h["leak_values"], h["ablate"], h["t0"]
    state = dict(g.get_state(cfg).values)
    state.update(started_at=stamp, wall_s=round(time.time() - t0, 1), budget=ctx.budget.snapshot(), approvals=approvals,
                 leakage=leakage_audit(state, q["as_of"], leak_values), model=ctx.llm.model, tag=tag)
    if ablate_own_history:
        state["ablation"] = ablation_summary(state)
    (out_dir / "state.json").write_text(json.dumps(state, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    score = score_one(q, state)
    (out_dir / "ledger.md").write_text(ledger(state, score), encoding="utf-8")
    r = (state.get("compute") or {}).get("result") or {}
    if r.get("mode") == "discrete":   # 离散目标：页头放结果概率表（含 Jev 对照臂）
        meta = f"as_of <b>{q['as_of']}</b> &middot; " + outcome_table_html(state)
        est = f"most likely {r.get('most_likely')} ({'n/a' if r.get('most_likely_prob') is None else f'{100 * r['most_likely_prob']:.1f}%'})"
        if r.get("resolved"):
            est = f"resolved {r.get('most_likely')} (published value)"
    elif r.get("basis") == "published":   # v2.4：结果是已公布的值（published.py）；组合估计只作参考
        e, pub = (state.get("compute") or {}).get("estimate_result") or {}, r.get("published") or {}
        meta = (f"as_of <b>{q['as_of']}</b> &middot; published value <b>{_n(r.get('central'))}</b> (data point "
                f"{html.escape(str(pub.get('id')))}, dated {html.escape(str(pub.get('date')))}) &middot; estimate for reference "
                f"{_n(e.get('central'))}, 80% [{_n(e.get('p10'))}, {_n(e.get('p90'))}] (not blended)")
        est = f"published value {_n(r.get('central'))}"
    else:
        meta = (f"as_of <b>{q['as_of']}</b> &middot; estimate <b>{_n(r.get('central'))}</b> &middot; 80% [{_n(r.get('p10'))}, "
                f"{_n(r.get('p90'))}] ({r.get('basis')})")
        est = f"estimate {_n(r.get('central'))}"
    if q.get("answer_value") is not None:
        meta += f" &middot; official value (scoring only) <b>{q['answer_value']:,}</b>"
    (out_dir / "graph.html").write_text(render_graph(state, f"Agent: {q['id']}", meta), encoding="utf-8")
    print(f"[{q['id']}] done in {state['wall_s']}s; {est}; usd {state['budget']['usd_total_assumed']}", flush=True)
    return state


def _n(v):
    return "n/a" if v is None else f"{v:,.0f}"


def score_one(q: dict, state: dict) -> dict:
    r = (state.get("compute") or {}).get("result") or {}
    est, ans = r.get("central"), q.get("answer_value")
    used_a = [a for a in (state.get("assumptions") or {}).get("kept") or [] if a.get("used_by")]
    row = {"id": q["id"], "as_of": q["as_of"], "answer_value": ans, "source": q.get("source"), "estimate": est,
           "p10": r.get("p10"), "p90": r.get("p90"), "basis": r.get("basis"), "scored": ans is not None,
           "n_assumptions_used": len(used_a), "assumptions_used": [a["id"] for a in used_a],
           "assumption_weight_share": r.get("assumption_weight_share"), "ablation": bool(state.get("ablation"))}
    if r.get("mode") == "discrete":   # 离散目标：各结果的概率；有真值时打分 = 真结果的概率、Brier、最可能的结果对不对
        row.update(mode="discrete", outcomes=r.get("outcomes"), most_likely=r.get("most_likely"))
        if ans is not None:
            row.update(D.score(r, ans))
        return row
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
        if s.get("mode") != "discrete":   # 离散目标没有点估计（central 只是最可能结果的数值）：只留 D.score 的打分
            s["arms"] = {"agent": arm(s["estimate"]), "naive": arm((f.get("naive") or {}).get("estimate")),
                         "structured_no_retrieval": arm((f.get("structured") or {}).get("estimate")),
                         "last_year_same_period": arm(q.get("last_year"))}
            for lim in (20, 10, 5):
                s[f"within_{lim}pct"] = {k: (v is not None and abs(v["pct_err"]) <= lim / 100) for k, v in s["arms"].items()}
        s["usd_total_assumed"] = st["budget"]["usd_total_assumed"]
        s["usd_tokens"] = st["budget"]["usd_tokens"]
        s["wall_s"] = st["wall_s"]
        rows.append(s)
    name = f"summary_{tag}.json" if tag else "summary.json"
    (RES / name).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    return rows


def main(questions: list, auto_approve: bool, tag: str = "", forecast_summary=None, ablate_own_history: bool = False):
    for q in questions:
        run_question(q, auto_approve, tag, ablate_own_history)
    if ablate_own_history:
        tag = ablation_tag(tag)
    scored = [q for q in questions if q.get("answer_value") is not None]
    return score_all(scored, tag, forecast_summary) if scored else []

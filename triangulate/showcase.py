"""展示集汇总（离线，只读保存的文件，不调模型）：EVAL_SHOWCASE_PLAN.md 的 4 道题、每个 arm 的数、已公布题的误差和 80% 区间
覆盖、预注册成功标准的中期 / 最终判定。写 results/showcase/summary.json，SHOWCASE.md 和网页（回测页的展示集一节）都用它。

「去年同月」不是对照（2026-10-16 的决定），这里不读 last_year。arm (3) 的补充运行（max_tokens 32000，不在预注册里）单独列出，
不进成功标准。没有估计的 arm 按 v2 的规则记为失败：|log10 误差| = 无穷大，计入中位数。
"""
import json
import math
import statistics

from .arms import check_naive
from .config import RESULTS
from .engine import evaluate_structured
from .forecast import FC, QUESTIONS
from .report import _clean, _load, final_reply

TAG = "showcase1"
AGENT = RESULTS / "agent"
OUT = RESULTS / "showcase" / "summary.json"
SHOWCASE = [q for q in QUESTIONS if q.get("set") in ("showcase", "live")]
ARMS = ("agent", "naive", "structured", "search_direct")          # 进成功标准的 arm（search_direct 只在未公布题上）
LEAK_KEYS = ("sentinel_hits", "points_dated_after_as_of", "snapshots_after_as_of", "late_dates_in_text_sent",
             "searcher_queries_containing_registered_values", "assumptions_containing_registered_values")


def _err(est, ans):
    if ans is None:
        return {}
    if est is None:
        return {"pct_err": None, "abs_log10_err": math.inf}
    return {"pct_err": est / ans - 1, "abs_log10_err": abs(math.log10(est / ans))}


def _naive(q):
    n = _load(FC / "raw" / "naive" / f"{q['id']}.json")
    if n is None:
        return None
    status, est, _ = check_naive(final_reply(n), q["answer_unit"], strict_target=False)
    return {"status": status, "estimate": est, "attempts": len(n["attempts"])}


def _structured(q):
    s = _load(FC / "raw" / "structured" / f"{q['id']}.json")
    if s is None:
        return None
    st = _clean(evaluate_structured(final_reply(s), q["answer_unit"], q["id"], strict_target=False, question=q["question"]))
    r = st["result"]
    return {"estimate": r["central"], "p10": r["p10"], "p90": r["p90"], "n_valid_paths": r["n_valid_paths"],
            "attempts": len(s["attempts"]), "errors": st["errors"]}


def _search(q, arm):
    s = _load(FC / "raw" / arm / f"{q['id']}.json")
    if s is None:
        return None
    a = s["attempts"]
    return {"status": s["status"], "estimate": s["estimate"], "attempts": len(a), "max_tokens": s.get("max_tokens", 4096),
            "web_search_requests": sum(x["web_search_requests"] for x in a), "queries": [y for x in a for y in x["queries"]],
            "stop_reasons": [x["stop_reason"] for x in a], "problems": [x["problems"] for x in a],
            "usd": s["usd"], "usd_search_fee_assumed": s["usd_search_fee_assumed"], "at": a[0].get("at")}


def _agent(q, tag):
    p = AGENT / q["id"] / tag / "state.json"
    if not p.is_file():
        return None
    st = json.loads(p.read_text(encoding="utf-8"))
    comp = st.get("compute") or {}
    r = comp.get("result") or {}
    pts = {x.get("id"): x for x in st.get("points") or [] if x.get("id")}
    kept_a = {a["id"]: a for a in (st.get("assumptions") or {}).get("kept") or []}
    methods = []
    for m in comp.get("methods") or []:
        methods.append({"id": m.get("id"), "method": m.get("method"), "formula": (m.get("params") or {}).get("formula"),
                        "estimate": m.get("estimate"), "weight": (r.get("weights") or {}).get(m.get("id")),
                        "rationale": m.get("rationale"), "notes": m.get("notes"),
                        "points": [{k: pts.get(i, {}).get(k) for k in ("id", "name", "value", "unit", "source_url", "page_date",
                                                                        "via")} for i in m.get("used_ids") or []],
                        "assumptions": [{k: kept_a.get(i, {}).get(k) for k in ("id", "name", "value", "low", "high", "p10_used",
                                                                                "p90_used", "unit")}
                                        for i in m.get("used_assumptions") or []]})
    mk = next((x.get("markets") for x in st.get("results") or [] if x.get("direction_id") == "markets"), None) or {}
    lk = st.get("leakage") or {}
    b = st.get("budget") or {}
    return {"estimate": r.get("central"), "p10": r.get("p10"), "p90": r.get("p90"), "basis": r.get("basis"),
            "weight_rule": r.get("weight_rule"), "assumption_weight_share": r.get("assumption_weight_share"),
            "methods": methods, "n_points_kept": sum(1 for x in st.get("points") or [] if x.get("keep")),
            "n_points": len(st.get("points") or []), "published_check": (st.get("published") or {}).get("status"),
            "markets": {"keywords": mk.get("keywords"), "matched": [x.get("question") for x in mk.get("markets") or []],
                        "price_points": [{k: x.get(k) for k in ("name", "value", "period_end", "source_url")}
                                         for x in mk.get("points") or []], "note": mk.get("note")},
            "leakage": {"pages_total": lk.get("pages_total"), "pages_snapshot": lk.get("pages_snapshot"),
                        "pages_live_dated": lk.get("pages_live_dated"), "pages_dropped": lk.get("pages_dropped"),
                        **{k: len(lk.get(k) or []) for k in LEAK_KEYS}},
            "usd_total_assumed": b.get("usd_total_assumed"), "usd_tokens": b.get("usd_tokens"),
            "usd_search_fee_assumed": b.get("usd_search_fee_assumed"), "n_calls": b.get("n_calls_logged"),
            "aborted": b.get("aborted") or st.get("aborted") or "", "wall_s": st.get("wall_s"), "started_at": st.get("started_at"),
            "final_text": (st.get("final") or {}).get("text", "")}


def _median(xs):
    return statistics.median(xs) if xs else None


def _inf(x):
    """中位数是无穷大（一半以上的题没有估计）时写成字符串 "inf"，免得被 _clean 换成 None、和「没算」混在一起。"""
    return "inf" if x == math.inf else x


def criteria(rows):
    """预注册的两条成功标准。已公布题打分；未公布题公布后登记真值才打分，之前判定为 pending。"""
    scored = [r for r in rows if r["answer_value"] is not None]
    n_all = len(rows)
    final = len(scored) == n_all

    def med(arm, rs):
        return _median([(r["arms"].get(arm) or {}).get("abs_log10_err", math.inf) for r in rs])
    a_pct = _median([math.inf if (r["arms"].get("agent") or {}).get("pct_err") is None
                     else abs(r["arms"]["agent"]["pct_err"]) for r in scored])
    meds = {arm: med(arm, scored) for arm in ("agent", "naive", "structured")} if scored else {}
    # 标准按全部 4 题定义：没打完分之前只报已打分题上的数（interim），判定一律 None（待定）
    c1 = (a_pct <= 0.20) if final else None
    c2_main = (meds["agent"] < meds["naive"] and meds["agent"] < meds["structured"]) if final else None
    unpub = [r for r in rows if r["kind"] == "unpublished"]
    unpub_scored = [r for r in unpub if r["answer_value"] is not None]
    c2_search = None
    if unpub and len(unpub_scored) == len(unpub):
        c2_search = med("agent", unpub_scored) < med("search_direct", unpub_scored)
    return {"n_questions": n_all, "n_scored": len(scored), "final": final,
            "c1_agent_median_abs_pct_err": _inf(a_pct), "c1_pass": c1,
            "median_abs_log10": {k: _inf(v) for k, v in meds.items()},
            "c2_vs_naive_structured_pass": c2_main, "c2_vs_search_direct_pass": c2_search,
            "met": (c1 and c2_main and c2_search) if final else None}


def build(tag: str = TAG) -> dict:
    rows = []
    for q in SHOWCASE:
        ans = q.get("answer_value")
        kind = "unpublished" if q.get("set") == "live" else "published"
        arms = {"agent": _agent(q, tag), "naive": _naive(q), "structured": _structured(q)}
        if kind == "unpublished":
            arms["search_direct"] = _search(q, "search_direct")
        for v in arms.values():
            if v is not None:
                v.update(_err(v.get("estimate"), ans))
        supp = _search(q, "search_direct_supp") if kind == "unpublished" else None
        if supp is not None:
            supp.update(_err(supp.get("estimate"), ans))
        cov = {k: (None if ans is None or (arms.get(k) or {}).get("estimate") is None
                   else arms[k]["p10"] <= ans <= arms[k]["p90"]) for k in ("agent", "structured")}
        rows.append({"id": q["id"], "kind": kind, "question": q["question"], "as_of": q["as_of"], "answer_value": ans,
                     "released": q.get("released"), "expected_release": q.get("expected_release"), "source": q.get("source"),
                     "arms": arms, "search_direct_supplementary": supp, "covered_80": cov})
    return _clean({"tag": tag, "rows": rows, "criteria": criteria(rows)})


def write(tag: str = TAG) -> dict:
    d = build(tag)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
    return d

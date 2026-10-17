"""网页的只读数据层：列出保存的运行、把一次运行的 state.json 整理成结果页要的 JSON、「证据 vs 假设」占比、回测表。

全部离线：只读 results/ 下已有的文件，不调模型、不联网，也不改写任何旧文件（假设占比只加在 API 返回的 JSON 里）。
"""
import json
import math
import re
import urllib.parse
from pathlib import Path

from ..agent.graph import TARGET_HISTORY_ROLE
from ..agent.outputs import basis_text, unit_text
from ..agent.run import RES, score_one
from ..forecast import QUESTIONS
from ..mc import Z90

SHARE_WARN = 0.5
QUESTIONS_BY_ID = {q["id"]: q for q in QUESTIONS}
# 回测页的两张表（用户指定）：开发集每题取最新的 agent 版本；留出测试集是 test1（EVAL_TEST_PLAN.md）
DEV_SET = [("fc_yell_2026_08", "v21b"), ("fc_yell_2026_09", "v21b"), ("fc_jnto_2026_08", "v21d"),
           ("fc_kr_births_2026_07", "v21d")]
TEST_SET = [("fc_tw_births_2026_09", "test1"), ("fc_lhr_pax_2026_09", "test1"), ("fc_jp_births_2026_07", "test1")]
# 展示集（EVAL_SHOWCASE_PLAN.md）：python -m triangulate showcase 写的汇总。「去年同月」不是对照（2026-10-16 的决定），网页不显示。
SHOWCASE_FILE = RES.parent / "showcase" / "summary.json"
SHARE_DEFINITION = ("每个输入 sigma_ln = ln(P90/P10) / (2 x 1.2816)；一个 formula_mc 方法的假设占比 = 假设输入的 sigma_ln^2 之和 / "
                    "全部采样输入的 sigma_ln^2 之和；序列方法记 0；总体 = 按方法权重平均。每个输入只出现一次、指数为 ±1 的纯乘除"
                    "公式，这就是 ln 方差的精确分解；有加减、mean() 或幂次时只是近似。观测点的 P10/P90 由代码统一给（v/1.2 .. v*1.2），假设用代码放宽后的范围。")
_SEG = re.compile(r"^[A-Za-z0-9_.\-]+$")


class NotFound(LookupError):
    pass


def clean(x):
    """JSON 里不许 NaN / inf（浏览器的 JSON.parse 不认）：一律换成 None。"""
    if isinstance(x, float):
        return x if math.isfinite(x) else None
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    return x


# ---------- 「证据 vs 假设」 ----------
def sigma_ln(p10, p90) -> float:
    """80% 区间 [p10, p90] 的 lognormal sigma；常数（p10 == p90）或无效值记 0。"""
    try:
        p10, p90 = float(p10), float(p90)
    except (TypeError, ValueError):
        return 0.0
    if not (p10 > 0 and p90 > p10) or not math.isfinite(p90 / p10):
        return 0.0
    return math.log(p90 / p10) / (2 * Z90)


def method_assumption_share(m: dict) -> dict:
    """一个方法的假设占比。formula_mc 按 inputs_detail 分解 ln 方差；序列方法（和没有采样输入的方法）记 0。"""
    if m.get("method") != "formula_mc":
        return {"share": 0.0, "var_assumption": 0.0, "var_point": 0.0, "note": "series method: 0 by definition"}
    va = vp = 0.0
    for d in m.get("inputs_detail") or []:
        v = sigma_ln(d.get("p10"), d.get("p90")) ** 2
        if d.get("kind") == "assumption":
            va += v
        elif d.get("kind") == "point":
            vp += v
    tot = va + vp
    return {"share": va / tot if tot > 0 else 0.0, "var_assumption": va, "var_point": vp, "note": ""}


def assumption_share(compute: dict) -> dict:
    """compute（state.json 里的那一节）-> {overall, warning, per_method}。只算算出了估计、拿到权重的方法；
    权重来自 compute.result.weights（已归一化）。没有算出估计的运行 overall = None。"""
    comp = compute or {}
    w = (comp.get("result") or {}).get("weights") or {}
    per = {}
    for m in comp.get("methods") or []:
        if m.get("estimate") is None:
            continue
        per[m["id"]] = {**method_assumption_share(m), "weight": float(w.get(m["id"], 0.0)), "method": m.get("method")}
    tw = sum(x["weight"] for x in per.values())
    overall = sum(x["weight"] * x["share"] for x in per.values()) / tw if tw > 0 else None
    return {"overall": overall, "warning": overall is not None and overall > SHARE_WARN, "threshold": SHARE_WARN,
            "per_method": per, "definition": SHARE_DEFINITION}


# ---------- 保存的运行 ----------
def _check_seg(s: str, what: str):
    if not _SEG.fullmatch(s) or s in (".", ".."):
        raise NotFound(f"bad {what}: {s!r}")


def run_dir(qid: str, tag: str = "", res: Path = RES) -> Path:
    """results/agent/<qid>/<tag>/；tag 可以为空（老的运行）或多段（v2/run1_judge_truncated）。拒绝 .. 和奇怪字符。"""
    _check_seg(qid, "question id")
    parts = [p for p in (tag or "").split("/") if p]
    for p in parts:
        _check_seg(p, "tag")
    d = res.joinpath(qid, *parts)
    if not d.resolve().is_relative_to(res.resolve()):
        raise NotFound("path outside results")
    return d


_LIST_CACHE = {}


def _run_kind(qid: str, tag: str) -> str:
    q = QUESTIONS_BY_ID.get(qid)
    if q is not None and q.get("answer_value") is not None:
        return "backtest"
    return "web" if tag.split("/")[-1].startswith("web_") else "ask"


def list_runs(res: Path = RES) -> list:
    """所有带 state.json 的运行（任意深度），按题 id、tag 排序。每个文件按修改时间缓存摘要。"""
    rows = []
    if not res.exists():
        return rows
    for p in sorted(res.glob("*/**/state.json")):
        rel = p.parent.relative_to(res).parts
        qid, tag = rel[0], "/".join(rel[1:])
        key, mt = str(p), p.stat().st_mtime
        hit = _LIST_CACHE.get(key)
        if hit and hit[0] == mt:
            rows.append(hit[1])
            continue
        try:
            st = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        r = (st.get("compute") or {}).get("result") or {}
        row = {"qid": qid, "tag": tag, "kind": _run_kind(qid, tag), "question": st.get("question", ""),
               "as_of": st.get("as_of"), "started_at": st.get("started_at"), "model": st.get("model"),
               "mode": r.get("mode") or "continuous", "most_likely": r.get("most_likely"),
               "most_likely_prob": r.get("most_likely_prob"),
               "estimate": r.get("central"), "p10": r.get("p10"), "p90": r.get("p90"),
               "usd": (st.get("budget") or {}).get("usd_total_assumed"), "wall_s": st.get("wall_s"),
               "share": assumption_share(st.get("compute")).get("overall")}
        row = clean(row)
        _LIST_CACHE[key] = (mt, row)
        rows.append(row)
    return rows


def load_state(qid: str, tag: str = "", res: Path = RES) -> dict:
    p = run_dir(qid, tag, res) / "state.json"
    if not p.is_file():
        raise NotFound(f"no saved run {qid}/{tag}")
    return json.loads(p.read_text(encoding="utf-8"))


def snapshot_url(p: dict):
    ts = p.get("snapshot_ts")
    if p.get("via") == "snapshot" and ts and p.get("source_url"):
        return f"https://web.archive.org/web/{ts}/{p['source_url']}"
    return None


def _snap_date(ts):
    return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}" if isinstance(ts, str) and len(ts) >= 8 and ts[:8].isdigit() else None


def _point_view(p: dict, used_by=None) -> dict:
    return {"id": p.get("id"), "direction_id": p.get("direction_id"), "name": p.get("name"), "value": p.get("value"),
            "value_as_written": p.get("value_as_written"), "unit": p.get("unit"), "period_start": p.get("period_start"),
            "period_end": p.get("period_end"), "source_url": p.get("source_url"),
            "domain": urllib.parse.urlsplit(p.get("source_url") or "").netloc, "via": p.get("via"),
            "snapshot_url": snapshot_url(p), "snapshot_date": _snap_date(p.get("snapshot_ts")),
            "page_date": p.get("page_date"), "quote": p.get("quote"), "keep": bool(p.get("keep")),
            "judge_reason": p.get("judge_reason"), "ablation_excluded": p.get("ablation_excluded"),
            "used_by": used_by or []}


def _evidence(iid: str, pts: dict, kept_a: dict) -> dict:
    if iid in kept_a:
        a = kept_a[iid]
        return {"kind": "assumption", "id": iid, "name": a.get("name"), "value": a.get("value"), "unit": a.get("unit"),
                "is_pct": a.get("is_pct")}
    if iid.startswith("k_"):
        return {"kind": "constant", "id": iid, "name": "calendar or unit constant (code)"}
    p = pts.get(iid)
    if p is None:
        return {"kind": "unknown", "id": iid}
    v = _point_view(p)
    v.pop("used_by")
    return {"kind": "point", **v}


def _inputs(m: dict, pts: dict, kept_a: dict) -> list:
    """方法的每个输入：名字、id、裁判写的 role、它指向的证据（数据点 / 假设 / 常数），formula_mc 另带采样用的 P10/P90。"""
    prm = m.get("params") or {}
    det = {d.get("name"): d for d in m.get("inputs_detail") or []}
    rows = []
    if m.get("method") == "outcome_probs":   # 离散目标：每个结果的概率输入（余下的结果没有输入）
        det = {d.get("label"): d for d in m.get("inputs_detail") or []}
        for label, spec in (prm.get("probs") or {}).items():
            spec = spec if isinstance(spec, dict) else {"id": spec}
            iid = str(spec.get("id"))
            rows.append({"name": str(label), "id": iid, "role": str(spec.get("role") or ""),
                         "evidence": _evidence(iid, pts, kept_a), "prob": (det.get(label) or {}).get("prob")})
    elif m.get("method") == "formula_mc":
        for name, spec in (prm.get("inputs") or {}).items():
            spec = spec if isinstance(spec, dict) else {"id": spec}
            iid = str(spec.get("id"))
            d = det.get(name) or {}
            rows.append({"name": name, "id": iid, "role": str(spec.get("role") or ""), "evidence": _evidence(iid, pts, kept_a),
                         "p10": d.get("p10"), "p90": d.get("p90"), "sigma_ln": sigma_ln(d.get("p10"), d.get("p90")) if d else None})
    else:
        for i in prm.get("target_history") or []:
            rows.append({"name": "target_history", "id": str(i), "role": TARGET_HISTORY_ROLE,
                         "evidence": _evidence(str(i), pts, kept_a)})
        for i in prm.get("signal_history") or []:
            rows.append({"name": "signal_history", "id": str(i), "role": "signal series (aligned by year)",
                         "evidence": _evidence(str(i), pts, kept_a)})
    return rows


def _formula(m: dict) -> str:
    prm = m.get("params") or {}
    if m.get("method") == "formula_mc":
        return str(prm.get("formula") or "")
    if m.get("method") == "series_naive":
        return f"mean of the last k={prm.get('k', 1)} years of the target"
    if m.get("method") == "outcome_probs":
        rem = prm.get("remainder")
        return "probability of each outcome from its input" + (f"; remainder {rem!r} = 1 minus the others" if rem else "")
    return {"yoy_scaling": "target[last year] x signal[this year] / signal[last year]",
            "linear_fit": "linear regression of target on signal", "ratio": "signal[this year] x historical target/signal ratio"
            }.get(m.get("method"), str(m.get("method")))


def _repair_view(jr: dict):
    rp = jr.get("repair")
    if not rp:
        return None
    return {"round": jr.get("round"), "errors": rp.get("errors") or [], "error": rp.get("error"),
            "errors_after": rp.get("errors_after"), "reverted": rp.get("reverted"),
            "previous_methods": [f"{m.get('id')} {m.get('method')}" + (f": {(m.get('params') or {})['formula']}"
                                                                     if (m.get("params") or {}).get("formula") else "")
                                 for m in rp.get("previous_methods") or [] if isinstance(m, dict)]}


def _leakage_view(lk: dict) -> dict:
    lk = lk or {}

    def n(k):
        v = lk.get(k)
        return len(v) if isinstance(v, list) else v
    return {"pages_total": lk.get("pages_total"), "pages_snapshot": lk.get("pages_snapshot"),
            "pages_live_dated": lk.get("pages_live_dated"), "pages_dropped": lk.get("pages_dropped"),
            "pages_sent_to_extractor": lk.get("pages_sent_to_extractor"),
            "sentinel_hits": n("sentinel_hits"), "sentinel_hit_urls": [h.get("url") for h in lk.get("sentinel_hits") or []],
            "points_dated_after_as_of": n("points_dated_after_as_of"), "snapshots_after_as_of": n("snapshots_after_as_of"),
            "searcher_queries_containing_registered_values": n("searcher_queries_containing_registered_values"),
            "assumptions_containing_registered_values": n("assumptions_containing_registered_values"),
            "late_dates_in_text_sent": n("late_dates_in_text_sent"), "page_selection": lk.get("page_selection"),
            "by_construction": lk.get("by_construction") or [], "residual_risks": lk.get("residual_risks") or []}


def result_view(st: dict, qid: str, tag: str = "") -> dict:
    """一次运行的结果页 JSON（API 返回的就是它）。假设占比只在这里算，不写回 state.json。"""
    comp = st.get("compute") or {}
    r = comp.get("result") or {}
    w, wb = r.get("weights") or {}, r.get("weight_basis") or {}
    pts = {p["id"]: p for p in st.get("points") or [] if p.get("id")}
    av = st.get("assumptions") or {}
    kept_a = {a["id"]: a for a in av.get("kept") or [] if a.get("id")}
    share = assumption_share(comp)
    used_by = {}
    methods = []
    for m in comp.get("methods") or []:
        for i in m.get("used_ids") or []:
            used_by.setdefault(i, []).append(m["id"])
        ms = share["per_method"].get(m["id"]) or {}
        methods.append({"id": m["id"], "label": m.get("label"), "method": m.get("method"), "formula": _formula(m),
                        "inputs": _inputs(m, pts, kept_a), "estimate": m.get("estimate"), "weight": w.get(m["id"], 0.0),
                        "weight_basis": wb.get(m["id"]), "backtest": m.get("backtest") or [],
                        "backtest_mean_abs_log_err": m.get("backtest_mean_abs_log_err"),
                        "target_series": m.get("target_series"), "signal_series": m.get("signal_series"),
                        "mc": m.get("mc"), "error": m.get("error"), "notes": m.get("notes") or [],
                        "rationale": m.get("rationale"), "assumption_share": ms.get("share"),
                        "distribution": m.get("distribution"), "remainder": m.get("remainder"),
                        "status": "computed" if m.get("estimate") is not None or m.get("distribution") else
                        "excluded_by_coverage" if m.get("coverage_excluded") else "failed",
                        "coverage": m.get("coverage"), "coverage_excluded": m.get("coverage_excluded")})
    # 输入核对没过、compute 没有用的方法：公式和输入从裁判那一轮的原始方法列表里取
    jr = next((j for j in st.get("judge_rounds") or [] if j.get("round") == comp.get("methods_from_round")), {})
    for i, reason in sorted((jr.get("audit_failed") or {}).items(), key=lambda x: int(x[0])):
        raw = (jr.get("methods") or [])[int(i)] if int(i) < len(jr.get("methods") or []) else {}
        methods.append({"id": f"({raw.get('id', '?')})", "label": raw.get("id"), "method": raw.get("method"),
                        "formula": _formula(raw), "inputs": _inputs(raw, pts, kept_a), "estimate": None, "weight": 0.0,
                        "error": reason, "notes": [], "rationale": raw.get("rationale"), "status": "excluded_by_input_audit"})
    kept_pts = [_point_view(p, used_by.get(p["id"])) for p in pts.values() if p.get("keep") and not p.get("ablation_excluded")]
    disc_pts = [_point_view(p) for p in pts.values() if not p.get("keep") and not p.get("ablation_excluded")]
    abl_pts = [_point_view(p) for p in pts.values() if p.get("ablation_excluded")]
    code_drop = {}
    pages = {"snapshot": 0, "live_dated": 0, "dropped": 0}
    for res in st.get("results") or []:
        for x in res.get("dropped_points") or []:
            code_drop[x.get("reason", "?")] = code_drop.get(x.get("reason", "?"), 0) + 1
        for pg in res.get("pages") or []:
            pages[pg.get("status", "dropped")] = pages.get(pg.get("status", "dropped"), 0) + 1
    assumptions = []
    for a in av.get("kept") or []:
        f = 100.0 if a.get("is_pct") else 1.0
        assumptions.append({k: a.get(k) for k in ("id", "name", "unit", "value", "low", "high", "is_pct", "rationale",
                                                   "applies_when", "falsified_by", "widened_by_floor", "used_by")}
                           | {"p10_used": None if a.get("p10_used") is None else a["p10_used"] * f,
                              "p90_used": None if a.get("p90_used") is None else a["p90_used"] * f})
    out = {"qid": qid, "tag": tag, "kind": _run_kind(qid, tag), "question": st.get("question"), "as_of": st.get("as_of"),
           "model": st.get("model"), "started_at": st.get("started_at"), "wall_s": st.get("wall_s"),
           "budget": st.get("budget") or {}, "target": (st.get("plan") or {}).get("target") or {},
           "directions": [{k: d.get(k) for k in ("id", "category", "perspective", "hypothesis")} for d in st.get("directions") or []],
           "approvals": st.get("approvals") or [],
           "estimate": {k: r.get(k) for k in ("central", "p10", "p90", "basis", "weight_rule", "sigma_ln")}
                       | {"basis_text": basis_text(r.get("basis")),   # v2.6d：区间依据的说明（outputs.BASIS_TEXT）
                          "unit": unit_text((st.get("plan") or {}).get("target"))},   # v2.7e：估计值和区间的单位
           "mode": r.get("mode") or "continuous", "discrete": discrete_view(st),
           "final_text": (st.get("final") or {}).get("text", ""), "methods": methods,
           "repairs": [x for x in (_repair_view(j) for j in st.get("judge_rounds") or []) if x],
           "audit_errors": [j.get("audit_error") for j in st.get("judge_rounds") or [] if j.get("audit_error")],
           "methods_from_round": comp.get("methods_from_round"),
           "assumptions": assumptions, "assumptions_rejected": [{k: a.get(k) for k in ("id", "name", "reason", "raw")}
                                                                for a in av.get("rejected") or []],
           "assumption_min_width": av.get("min_width"),
           "evidence": {"kept": kept_pts, "discarded": disc_pts, "ablation_excluded": abl_pts, "dropped_by_code": code_drop,
                        "pages": pages},
           "leakage": _leakage_view(st.get("leakage")), "ablation": bool(st.get("ablation")),
           "assumption_share": share, "aborted": st.get("aborted") or (st.get("budget") or {}).get("aborted") or None,
           "official": None}
    q = QUESTIONS_BY_ID.get(qid)
    if q is not None and q.get("answer_value") is not None:   # 只有回测题才显示官方值和误差
        s = score_one(q, st)
        out["official"] = {"answer_value": q["answer_value"], "source": q.get("source"), "released": q.get("released"),
                           "pct_err": s.get("pct_err"),
                           "abs_log10_err": s.get("abs_log10_err"), "covered_80": s.get("covered_80")}
        if s.get("mode") == "discrete":
            out["official"].update({k: s.get(k) for k in ("true_outcome", "prob_true", "brier", "most_likely_correct")})
    return out


def discrete_view(st: dict):
    """离散目标的结果表：每个结果的 agent 概率（等权平均）、每个方法的概率、Jev 对照臂（不并入）。连续值目标返回 None。"""
    comp = st.get("compute") or {}
    r = comp.get("result") or {}
    if r.get("mode") != "discrete":
        return None
    ms = [m for m in comp.get("methods") or [] if m.get("distribution")]
    jv = st.get("jev") or {}
    jp = jv.get("probabilities") if jv.get("status") == "ok" else None
    rows = [{"label": o.get("label"), "value": o.get("value"), "prob": o.get("prob"),
             "per_method": {m["id"]: m["distribution"].get(o.get("label")) for m in ms},
             "jev": None if not jp else jp.get(o.get("label"))} for o in r.get("outcomes") or []]
    jev = {k: jv.get(k) for k in ("status", "note", "error", "model", "choice", "confidence", "usage", "usd_estimated",
                                  "price_source", "n_points_in_brief", "brief_chars", "latency_s", "endpoint")} if jv else None
    return {"outcomes": rows, "methods": [m["id"] for m in ms], "most_likely": r.get("most_likely"),
            "most_likely_prob": r.get("most_likely_prob"), "weight_rule": r.get("weight_rule"),
            "assumption_weight_share": r.get("assumption_weight_share"), "jev": jev,
            "jev_brief": jv.get("brief") if jv else None}


def load_result(qid: str, tag: str = "", res: Path = RES) -> dict:
    return clean(result_view(load_state(qid, tag, res), qid, tag))


# ---------- 回测表 ----------
def _arm(x):
    return None if not x else {"estimate": x.get("estimate"), "pct_err": x.get("pct_err")}


def backtest_row(qid: str, tag: str, summary_rows: list, res: Path = RES) -> dict:
    """一行：官方值、agent 估计和误差、80% 区间是否盖住、两个基线（直接问、不联网结构化）、假设占比。数字取自 summary_<tag>.json，
    假设占比由同一次运行的 state.json 算出。"""
    s = next((r for r in summary_rows if r.get("id") == qid), None)
    q = QUESTIONS_BY_ID.get(qid) or {}
    row = {"qid": qid, "tag": tag, "as_of": q.get("as_of"), "answer_value": q.get("answer_value"), "found": s is not None}
    if s is None:
        return row
    arms = s.get("arms") or {}
    row.update(answer_value=s.get("answer_value"), estimate=s.get("estimate"), p10=s.get("p10"), p90=s.get("p90"),
               pct_err=s.get("pct_err"), abs_log10_err=s.get("abs_log10_err"), covered_80=s.get("covered_80"),
               naive=_arm(arms.get("naive")), structured=_arm(arms.get("structured_no_retrieval")),
               usd=s.get("usd_total_assumed"))
    try:
        share = assumption_share(load_state(qid, tag, res).get("compute"))
        row.update(share=share["overall"], share_warning=share["warning"])
    except NotFound:
        row.update(share=None, share_warning=False)
    return row


def _summary(tag: str, res: Path) -> list:
    p = res / f"summary_{tag}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else []


def _sc_arm(x, keys=()):
    return None if not x else {k: x.get(k) for k in ("estimate", "pct_err", "abs_log10_err", "status", *keys)}


def showcase_view(path: Path = SHOWCASE_FILE):
    """展示集一节：每题每个 arm 的数（已公布题带误差），agent 的区间、覆盖、成本、方法和市场工具的结果，预注册标准的判定。
    联网直接答的补充运行（不在预注册里）单列。没有汇总文件时返回 None。"""
    if not path.is_file():
        return None
    d = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for r in d.get("rows") or []:
        a = r.get("arms") or {}
        ag = a.get("agent")
        agent = None if not ag else dict(_sc_arm(ag, ("p10", "p90", "basis", "usd_total_assumed", "wall_s",
                                                      "assumption_weight_share", "n_points_kept", "aborted")),
                                         covered_80=(r.get("covered_80") or {}).get("agent"),
                                         methods=[{k: m.get(k) for k in ("id", "formula", "estimate", "weight")}
                                                  for m in ag.get("methods") or []],
                                         markets=ag.get("markets"))
        st = _sc_arm(a.get("structured"), ("p10", "p90"))
        if st is not None:
            st["covered_80"] = (r.get("covered_80") or {}).get("structured")
        rows.append({"qid": r.get("id"), "tag": d.get("tag"), "kind": r.get("kind"), "as_of": r.get("as_of"),
                     "answer_value": r.get("answer_value"), "released": r.get("released"),
                     "expected_release": r.get("expected_release"), "question": r.get("question"),
                     "agent": agent, "naive": _sc_arm(a.get("naive")), "structured": st,
                     "search_direct": _sc_arm(a.get("search_direct")) if "search_direct" in a else None,
                     "search_direct_supp": _sc_arm(r.get("search_direct_supplementary"))})
    return {"tag": d.get("tag"), "rows": rows, "criteria": d.get("criteria")}


def backtests(res: Path = RES, showcase_path: Path = SHOWCASE_FILE) -> dict:
    tables = {}
    for name, rows in (("dev", DEV_SET), ("test", TEST_SET)):
        cache = {}
        out = []
        for qid, tag in rows:
            if tag not in cache:
                cache[tag] = _summary(tag, res)
            out.append(backtest_row(qid, tag, cache[tag], res))
        tables[name] = out
    return clean({"dev": tables["dev"], "test": tables["test"], "showcase": showcase_view(showcase_path),
                  "share_threshold": SHARE_WARN, "share_definition": SHARE_DEFINITION})

"""COMPUTE（只有代码）：把裁判选的方法和数据点 id 变成序列，跑方法、回测、加权、给区间。"""
import statistics
from datetime import timedelta

from . import methods as M
from .evidence import parse_date

TOL_DAYS = 3


def _span(p):
    pe = parse_date(p.get("period_end"), end=True)
    ps = parse_date(p.get("period_start")) or pe
    return ps, pe


def _same_calendar(ps, pe, ref_ps, ref_pe) -> bool:
    """同一日历期间：期末月日相差 <= 3 天，期长相差 <= 3 天（跨年份比较）。"""
    try:
        ref_end = ref_pe.replace(year=pe.year)
    except ValueError:  # 2 月 29 日
        ref_end = ref_pe.replace(year=pe.year, day=28)
    return abs((pe - ref_end).days) <= TOL_DAYS and abs(((pe - ps) - (ref_pe - ref_ps)).days) <= TOL_DAYS


def build_series(ids, pts: dict, ref=None) -> tuple:
    """返回 ({year: value}, notes, used_ids)。ref = (period_start, period_end)：target_history 用目标期间；
    signal 用序列里最晚那个点的期间做参照。只用裁判 keep 的点。"""
    notes, cand = [], []
    for i in ids or []:
        p = pts.get(i)
        if p is None:
            notes.append(f"{i}: unknown id")
            continue
        if not p.get("keep", True):
            notes.append(f"{i}: discarded by judge, not used")
            continue
        ps, pe = _span(p)
        if pe is None:
            notes.append(f"{i}: no period_end")
            continue
        cand.append((i, ps, pe, p))
    if not cand:
        return {}, notes, []
    if ref is None:
        _, rps, rpe, _ = max(cand, key=lambda c: c[2])
    else:
        rps, rpe = ref
    pct = [c for c in cand if c[3].get("unit") == "%"]
    if pct and len(pct) != len(cand):
        notes.append("mixed % and non-% units; dropped the minority")
        cand = pct if len(pct) > len(cand) / 2 else [c for c in cand if c[3].get("unit") != "%"]
    by_year, used = {}, []
    for i, ps, pe, p in cand:
        if not _same_calendar(ps, pe, rps, rpe):
            notes.append(f"{i}: period {ps}..{pe} is not the same calendar period as {rps}..{rpe}")
            continue
        by_year.setdefault(pe.year, []).append(p["value"])
        used.append(i)
    return {y: statistics.median(v) for y, v in by_year.items()}, notes, used


def run(methods: list, pts: dict, target: dict) -> dict:
    tps = parse_date(target.get("period_start"))
    tpe = parse_date(target.get("period_end"), end=True)
    if tpe is None:
        return {"error": "target period_end unparseable", "methods": [], "result": M.combine([])}
    tps = tps or tpe - timedelta(days=0)
    year = tpe.year
    results = []
    for n, m in enumerate(methods or [], start=1):
        # id 由代码按列表顺序重编（m1..mN），保证唯一；裁判给的 id 只作为 label 保存
        r = {"id": f"m{n}", "label": str(m.get("id", ""))[:40], "method": m.get("method"), "params": m.get("params") or {},
             "rationale": str(m.get("rationale", ""))[:400], "estimate": None, "backtest": [], "notes": []}
        prm = r["params"]
        try:
            if r["method"] in ("series_naive", "yoy_scaling", "linear_fit", "ratio"):
                tgt, n1, u1 = build_series(prm.get("target_history"), pts, ref=(tps, tpe))
                r["notes"] += n1
                r["target_series"] = {str(y): v for y, v in sorted(tgt.items())}
                r["used_ids"] = list(u1)
                sig = {}
                if r["method"] != "series_naive":
                    sig, n2, u2 = build_series(prm.get("signal_history"), pts)
                    r["notes"] += n2
                    r["signal_series"] = {str(y): v for y, v in sorted(sig.items())}
                    r["used_ids"] += u2
                k = int(prm.get("k", 1) or 1) if r["method"] == "series_naive" else 1
                k = min(max(k, 1), 3)
                fn = {"series_naive": lambda: M.series_naive(tgt, year, k), "yoy_scaling": lambda: M.yoy_scaling(tgt, sig, year),
                      "linear_fit": lambda: M.linear_fit(tgt, sig, year), "ratio": lambda: M.ratio(tgt, sig, year)}[r["method"]]
                r["estimate"] = fn()
                if r["method"] == "series_naive":
                    r["years_used"] = M.prior_years(tgt, year, k)
                r["backtest"] = M.backtest(r["method"], tgt, sig, year, k)
            elif r["method"] == "formula_mc":
                inputs, used = {}, []
                for name, spec in (prm.get("inputs") or {}).items():
                    spec = spec if isinstance(spec, dict) else {"id": spec}
                    p = pts.get(spec.get("id"))
                    if p is None or not p.get("keep", True):
                        raise M.MethodError(f"input {name}: id {spec.get('id')} unknown or discarded")
                    v = p["value"] / 100 if p.get("unit") == "%" else p["value"]
                    # 不确定度由代码统一给；裁判填的 rel_uncertainty 只记录，不使用
                    inputs[name] = (v, M.DEFAULT_REL_U)
                    if "rel_uncertainty" in spec:
                        r.setdefault("rel_uncertainty_from_judge_ignored", {})[name] = spec.get("rel_uncertainty")
                    used.append(spec.get("id"))
                s = M.formula_mc(str(prm.get("formula", "")), inputs)
                r.update(estimate=s["median"], mc={"p10": s["p10"], "p90": s["p90"]}, used_ids=used)
            else:
                raise M.MethodError(f"unknown method {r['method']!r}")
        except M.MethodError as e:
            r["error"] = str(e)
        except (TypeError, ValueError, KeyError, AttributeError) as e:
            r["error"] = f"bad params: {type(e).__name__}: {e}"[:200]
        if r["backtest"]:
            errs = [abs(b["log_err"]) for b in r["backtest"]]
            r["backtest_mean_abs_log_err"] = statistics.fmean(errs)
        results.append(r)
    ok = [r for r in results if r.get("estimate")]
    return {"target_year": year, "methods": results, "result": M.combine(ok), "rel_uncertainty_formula_inputs": M.DEFAULT_REL_U}

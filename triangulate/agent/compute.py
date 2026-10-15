"""COMPUTE（只有代码）：把裁判选的方法和数据点 id 变成序列，跑方法、回测、加权、给区间。
formula_mc 的输入可以是保留的数据点，也可以是校验通过的假设（assumptions.py）；规则：至少一个观测点、最多 3 个假设。"""
import random
import re
import statistics
from datetime import timedelta

from . import assumptions as A
from . import methods as M
from ..mc import sample_lognormal
from .evidence import parse_date

TOL_DAYS = 3


RATIO_UNIT = re.compile(r"^\s*$|%|\b(?:ratio|ratios|share|shares|fraction|factor|multiplier|proportion|percent|percentage|pct|"
                        r"dimensionless|index)\b", re.I)


def is_ratio_unit(unit: str) -> bool:
    """单位是纯比率 / 百分比（没有「量」）。空单位也算：说不清是什么量的输入不能当作量。"""
    return bool(RATIO_UNIT.search(unit or ""))


def restated_point(a: dict, pts: dict, rel_tol: float = 0.005) -> str:
    """假设的值和某个保留观测点的值相同（相对差 <= 0.5%）、单位也对得上（都是 %，或单位词干有交集）时，返回那个点的 id。
    只比数值会误伤：黄石 9 月的「变化倍数 1.0（ratio）」撞上了「道路开放日 1（day of month）」。"""
    v = a.get("value")
    if not v:
        return ""
    a_pct, a_st = a.get("unit") == "%", A.stems(a.get("unit", ""))
    for p in pts.values():
        pv = p.get("value")
        if not (p.get("keep", True) and pv and abs(pv - v) <= rel_tol * abs(v)):
            continue
        p_pct = p.get("unit") == "%"
        if (a_pct and p_pct) or (not a_pct and not p_pct and a_st & A.stems(p.get("unit", ""))):
            return p["id"]
    return ""


def calendar_constants(tps, tpe) -> dict:
    """formula_mc 里可以引用的日历常数（k_ 开头，由代码给，不采样，不算观测点）：天数、周数这类精确数不该让模型写进公式。"""
    return {"k_days_target": float((tpe - tps).days + 1), "k_days_per_week": 7.0, "k_days_per_year": 365.25,
            "k_weeks_per_year": 365.25 / 7, "k_months_per_year": 12.0}


class Draws:
    """按输入 id 抽 Monte Carlo 样本并缓存：同一个点或假设在几个方法里共用同一份样本（种子 = MC_SEED + id，可复现）。"""

    def __init__(self, n: int = M.MC_N, seed: int = M.MC_SEED):
        self.n, self.seed, self._cache = n, seed, {}

    def get(self, key: str, low: float, high: float) -> list:
        k = (key, low, high)
        if k not in self._cache:
            self._cache[k] = sample_lognormal(low, high, self.n, random.Random(f"{self.seed}|{key}"))
        return self._cache[k]


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


def run(methods: list, pts: dict, target: dict, assumptions=None, only_methods=None) -> dict:
    """assumptions：assumptions.validate() 的结果（{"kept": [...], "rejected": [...]}），没有就当空。
    only_methods：只允许这些方法（消融 --ablate-own-history 时 = {"formula_mc"}），其余记错误、不计算。"""
    av = assumptions or {"kept": [], "rejected": []}
    kept_a = {a["id"]: a for a in av.get("kept") or []}
    rejected_a = {a.get("id"): a.get("reason", "") for a in av.get("rejected") or [] if a.get("id") and a.get("id") not in kept_a}
    draws = Draws()
    tps = parse_date(target.get("period_start"))
    tpe = parse_date(target.get("period_end"), end=True)
    if tpe is None:
        return {"error": "target period_end unparseable", "methods": [], "result": M.combine([])}
    tps = tps or tpe - timedelta(days=0)
    year = tpe.year
    consts = calendar_constants(tps, tpe)
    results = []
    for n, m in enumerate(methods or [], start=1):
        # id 由代码按列表顺序重编（m1..mN），保证唯一；裁判给的 id 只作为 label 保存
        r = {"id": f"m{n}", "label": str(m.get("id", ""))[:40], "method": m.get("method"), "params": m.get("params") or {},
             "rationale": str(m.get("rationale", ""))[:400], "estimate": None, "backtest": [], "notes": []}
        prm = r["params"]
        try:
            if only_methods is not None and r["method"] not in only_methods:
                raise M.MethodError(f"ablation: only {sorted(only_methods)} allowed (method needs target_history)")
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
                env, used, used_a, detail = {}, [], [], []
                for name, spec in (prm.get("inputs") or {}).items():
                    spec = spec if isinstance(spec, dict) else {"id": spec}
                    iid = str(spec.get("id"))
                    fixed = None
                    if iid in consts:
                        fixed = lo = hi = consts[iid]
                        kind = "constant"
                    elif iid in kept_a:
                        a = kept_a[iid]
                        dup = restated_point(a, pts)
                        if dup:  # 假设的值就是某个保留的观测点：应该直接用观测点（FOMC 题：FedWatch 概率被写成了假设）
                            raise M.MethodError(f"input {name}: assumption {iid} restates kept data point {dup} "
                                                f"(same value and unit); reference {dup} instead")
                        lo, hi = a["p10_used"], a["p90_used"]
                        used_a.append(iid)
                        kind = "assumption"
                    elif iid in rejected_a:
                        raise M.MethodError(f"input {name}: assumption {iid} was rejected ({rejected_a[iid]})")
                    else:
                        p = pts.get(iid)
                        if p is None or not p.get("keep", True):
                            raise M.MethodError(f"input {name}: id {iid} unknown or discarded")
                        v = p["value"] / 100 if p.get("unit") == "%" else p["value"]
                        if not (v > 0):
                            raise M.MethodError(f"input {name} must be positive for lognormal sampling")
                        # 观测点的不确定度由代码统一给；裁判填的 rel_uncertainty 只记录，不使用
                        lo, hi = v / (1 + M.DEFAULT_REL_U), v * (1 + M.DEFAULT_REL_U)
                        if "rel_uncertainty" in spec:
                            r.setdefault("rel_uncertainty_from_judge_ignored", {})[name] = spec.get("rel_uncertainty")
                        used.append(iid)
                        kind = "point"
                    env[name] = [fixed] * draws.n if fixed is not None else draws.get(iid, lo, hi)
                    unit = (kept_a[iid].get("unit") if kind == "assumption" else
                            pts[iid].get("unit") if kind == "point" else "constant")
                    detail.append({"name": name, "id": iid, "kind": kind, "p10": lo, "p90": hi, "unit": unit or ""})
                r.update(used_ids=used, used_assumptions=sorted(set(used_a)), inputs_detail=detail)
                if not used:
                    raise M.MethodError("formula_mc must use at least one kept observed data point "
                                        "(a formula made only of assumptions is rejected)")
                # 目标本身是百分比 / 比率（利率、占比）时不适用：那时百分比输入就是「量」（FOMC 题里这条把所有路线都挡掉了）
                if not is_ratio_unit(target.get("unit", "")) and \
                        not any(d["kind"] in ("point", "assumption") and not is_ratio_unit(d.get("unit", "")) for d in detail):
                    raise M.MethodError("formula_mc needs at least one input that is a quantity (not a share, ratio or %); "
                                        "a product of ratios cannot produce the target")
                if len(set(used_a)) > A.MAX_PER_METHOD:
                    raise M.MethodError(f"formula_mc uses {len(set(used_a))} assumptions (at most {A.MAX_PER_METHOD})")
                s = M.formula_mc_samples(str(prm.get("formula", "")), env)
                r.update(estimate=s["median"], mc={"p10": s["p10"], "p90": s["p90"]})
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
    for r in results:
        r["n_point_inputs"] = len(set(r.get("used_ids") or []))
        r["n_assumption_inputs"] = len(r.get("used_assumptions") or [])
        r["rests_mainly_on_assumptions"] = r["n_assumption_inputs"] > 0 and r["n_assumption_inputs"] >= r["n_point_inputs"]
    ok = [r for r in results if r.get("estimate")]
    res = M.combine(ok)
    w = res.get("weights") or {}
    res["assumption_weight_share"] = sum(w.get(r["id"], 0) for r in ok if r.get("used_assumptions"))
    used_by = {}
    for r in ok:
        for aid in r.get("used_assumptions") or []:
            used_by.setdefault(aid, []).append(r["id"])
    return {"target_year": year, "methods": results, "result": res, "rel_uncertainty_formula_inputs": M.DEFAULT_REL_U,
            "assumption_min_width": A.MIN_WIDTH, "assumptions_used_by": used_by}

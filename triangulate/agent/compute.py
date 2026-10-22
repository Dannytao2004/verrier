"""COMPUTE（只有代码）：把裁判选的方法和数据点 id 变成序列，跑方法、回测、加权、给区间。
formula_mc 的输入可以是保留的数据点，也可以是校验通过的假设（assumptions.py）；规则：至少一个观测点、最多 3 个假设
（v2.7d：coverage 为 sum 的方法每个部分最多 3 个、整个方法最多 8 个）。"""
import random
import re
import statistics
from datetime import timedelta

from . import ablation as AB
from . import assumptions as A
from . import methods as M
from . import qty as Q
from ..mc import sample_lognormal
from .evidence import PAGE_DATE, parse_date

TOL_DAYS = 3


RATIO_UNIT = re.compile(r"^\s*$|%|\b(?:ratio|ratios|share|shares|fraction|factor|multiplier|proportion|percent|percentage|pct|"
                        r"dimensionless|index)\b", re.I)


def is_ratio_unit(unit: str) -> bool:
    """单位是纯比率 / 百分比（没有「量」）。空单位也算：说不清是什么量的输入不能当作量。"""
    return bool(RATIO_UNIT.search(unit or ""))


# v2.11b（R14）：restated_point 比单位词干之前按整词去掉的通用词：它们只说明是比率 / 倍数，不指认是哪个量。
# 按整词去、不按 5 字母词干去：factories、proposals、rations、dimensions 是真实的量；index 不去（index (2020=100) 要照旧抓）
RESTATE_GENERIC = {"ratio", "ratios", "share", "shares", "fraction", "fractions", "factor", "factors", "multiplier",
                   "multiple", "multiples", "proportion", "proportions", "percent", "percentage", "pct", "dimensionless",
                   "times", "fold"}


def _restate_stems(unit) -> set:
    """同 ablation.stems，只是先按整词去掉 RESTATE_GENERIC。"""
    return {AB.stem(t) for t in AB._tokens(str(unit or ""))
            if t.lower() not in AB.STOP and t.lower() not in RESTATE_GENERIC and len(t) >= 2}


def restated_point(a: dict, pts: dict, rel_tol: float = 0.005) -> str:
    """假设的值和某个保留观测点的值相同（相对差 <= 0.5%）、单位也对得上（都是 %，或点不是 % 且单位词干有交集）时，返回那个点的 id。
    只比数值会误伤：黄石 9 月的「变化倍数 1.0（ratio）」撞上了「道路开放日 1（day of month）」。
    v2.5.4（N17）：假设是不是百分数用 assumptions.is_pct（「% of annual live births」也算）；点仍按 compute 对点的规则
    （unit == "%"，同 formula_mc 的点）。点也改用 is_pct 会误伤：discrete7 的 a2「降息概率 2 %」撞上 p31「核心 CPI 2.0 percent」。
    以前第二个条件还要求假设不是 %：unit 为 "%" 时词干本来就是空的，去掉不改变结果，「% of ...」的假设照旧按词干比。
    v2.11b（R14）：词干分支再要求两边的 is_pct 相同，词干先去掉 RESTATE_GENERIC 再求交集。以前的误判：token 题 v1 的
    a11「ratio (annual / Q1-2025 quarter)」= 7 撞上 p151「ratio」= 7（只有 ratio 相同）；「% of annual live births」8.4
    撞上「live births (persons)」8.4。两边都是 % 的分支不变（v2.11 方案决定 16，BUGS S35）。任何一边的单位只剩通用词时词干交集为空，不再算复述（漏检，BUGS S37）。"""
    v = a.get("value")
    if not v:
        return ""
    a_pct, a_st = A.is_pct(a.get("unit")), _restate_stems(a.get("unit"))
    for p in pts.values():
        pv = p.get("value")
        if not (p.get("keep", True) and pv and abs(pv - v) <= rel_tol * abs(v)):
            continue
        p_pct = p.get("unit") == "%"
        if (a_pct and p_pct) or (not p_pct and a_pct == A.is_pct(p.get("unit")) and a_st & _restate_stems(p.get("unit"))):
            return p["id"]
    return ""


# 单位换算常数（v2.2）：和日历常数一样由代码给。FOMC 题里裁判只能把「25 基点 = 0.25 个百分点」写成假设或常数 1 的组合
UNIT_CONSTANTS = {"k_bp_per_pct_point": 100.0, "k_percent_per_unit": 100.0}


def calendar_constants(tps, tpe) -> dict:
    """formula_mc 里可以引用的常数（k_ 开头，由代码给，不采样，不算观测点）：天数、周数这类精确数不该让模型写进公式；
    另加单位换算常数 UNIT_CONSTANTS。"""
    return {"k_days_target": float((tpe - tps).days + 1), "k_days_per_week": 7.0, "k_days_per_year": 365.25,
            "k_weeks_per_year": 365.25 / 7, "k_months_per_year": 12.0, **UNIT_CONSTANTS}


def _names(c: dict, key: str, at_least: int) -> list:
    v = c.get(key)
    if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
        raise M.MethodError(f"coverage: {key} must be a list of names")
    v = [x.strip() for x in v]
    if len(v) < at_least:
        raise M.MethodError(f"coverage: {key} needs at least {at_least} name{'s' if at_least > 1 else ''}")
    if len(set(v)) != len(v):
        raise M.MethodError(f"coverage: {key} lists a name twice")
    return v


def coverage(c) -> tuple:
    """v2.7d：方法的 coverage 声明（省略 = full）。返回 (规范化的声明或 None, 不进合并的原因或 "")；不合规抛 MethodError。
    part（只覆盖目标的一部分）和 missing 不为空的 sum 照算，但不进合并，原因交给修正轮。"""
    if c is None:
        return None, ""
    if not isinstance(c, dict):
        raise M.MethodError(f"coverage must be an object such as {{\"kind\": \"full\"}}, not {c!r}"[:200])
    kind = c.get("kind")
    if kind not in ("full", "part", "sum"):
        raise M.MethodError(f"coverage: kind must be \"full\", \"part\" or \"sum\", not {kind!r}")
    if kind == "full":
        return {"kind": "full"}, ""
    dim = c.get("dimension")
    if not isinstance(dim, str) or not dim.strip():
        raise M.MethodError("coverage: dimension must be a name (e.g. \"channel\")")
    dim = dim.strip()
    if kind == "part":
        part = c.get("part")
        if not isinstance(part, str) or not part.strip():
            raise M.MethodError("coverage: part must be a name")
        sib = _names(c, "siblings", 1)
        return ({"kind": "part", "dimension": dim, "part": part.strip(), "siblings": sib},
                f"covers only {part.strip()} of {dim}, so code does not combine it with full estimates; sum it with its "
                f"siblings ({', '.join(sib)}) in one method, with an allowance assumption for parts without evidence")
    parts, miss = _names(c, "parts", 2), _names(c, "missing", 0)
    return ({"kind": "sum", "dimension": dim, "parts": parts, "missing": miss},
            f"sums {', '.join(parts)} of {dim} but misses {', '.join(miss)}, so code does not combine it with full estimates; "
            f"add each missing part to the sum with an allowance assumption (missing then empty), or drop the method"
            if miss else "")


def produced(m: dict) -> bool:
    """一个方法算出了结果：连续值方法有正的 estimate，离散方法（outcome_probs）有 distribution。"""
    return bool(m.get("estimate")) or bool(m.get("distribution"))


class Draws:
    """按输入 id 抽 Monte Carlo 样本并缓存：同一个点或假设在几个方法里共用同一份样本（种子 = MC_SEED + id，可复现）。"""

    def __init__(self, n: int = M.MC_N, seed: int = M.MC_SEED):
        self.n, self.seed, self._cache = n, seed, {}

    def get(self, key: str, low: float, high: float) -> list:
        k = (key, low, high)
        if k not in self._cache:
            self._cache[k] = sample_lognormal(low, high, self.n, random.Random(f"{self.seed}|{key}"))
        return self._cache[k]

    def get_range(self, key: str, low: float, high: float) -> list:
        """v2.8o：原文给的区间（3-4 slices）：在 [low, high] 上均匀取值，再乘和单个观测点一样的误差（中位数 1，P10/P90 = 1/1.2、1.2）。"""
        k = (key, "range", low, high)
        if k not in self._cache:
            u = 1 + M.DEFAULT_REL_U
            noise = sample_lognormal(1 / u, u, self.n, random.Random(f"{self.seed}|{key}"))
            rng = random.Random(f"{self.seed}|{key}|range")
            self._cache[k] = [rng.uniform(low, high) * z for z in noise]
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
        # v2.11d：页面日期兜底的点不进序列（target 和 signal 都不进）：期初 = 期末，会成为 signal 的参照期间、挤掉年度点；
        # 两个相隔一年的页面日期点还能拼出假的年度序列
        if p.get("period_source") == PAGE_DATE:
            notes.append(f"{i}: period not stated in the source (page dated {p.get('period_end')}), not used in a series")
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
    if (target or {}).get("outcome_type") == "discrete":   # 离散目标走 discrete.py（只有 outcome_probs）；连续值路径不变
        from . import discrete
        return discrete.run(methods, pts, target, assumptions)
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
    # v2.7c：规划钉了单位（target.unit_canonical）时，formula_mc 要声明「公式结果的单位」（方法的 unit），代码把结果换算成目标单位；
    # 观测点的单位里带 %（'% of population'）就除以 100，目标本身是百分数时除外。没钉单位的运行（已存的都是）照旧。
    tu = (target or {}).get("unit_canonical") or ""
    target_pct = A.is_pct(tu or (target or {}).get("unit", ""))
    results = []
    for n, m in enumerate(methods or [], start=1):
        # id 由代码按列表顺序重编（m1..mN），保证唯一；裁判给的 id 只作为 label 保存
        r = {"id": f"m{n}", "label": str(m.get("id", ""))[:40], "method": m.get("method"), "params": m.get("params") or {},
             "rationale": str(m.get("rationale", ""))[:400], "estimate": None, "backtest": [], "notes": []}
        prm = r["params"]
        try:
            cov, excluded = coverage(m.get("coverage"))
            if cov is not None:
                r["coverage"] = cov
            # v2.8m：sum 方法最多 8 个假设（MAX_PER_SUM），其他方法每个最多 6 个（以前 3 个，sum 按部分数算）
            cap = A.MAX_PER_SUM if cov and cov["kind"] == "sum" else A.MAX_PER_METHOD
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
                inputs = dict(prm.get("inputs") or {})
                # v2.8d（冒烟测试 smoke_tea）：公式里直接写了代码给的常数（k_days_per_year），inputs 里漏列；常数的值由代码定，补上
                for nm in sorted(set(re.findall(r"[A-Za-z_]\w*", str(prm.get("formula", "")))) & set(consts) - set(inputs)):
                    inputs[nm] = {"id": nm, "role": "constant supplied by code"}
                for name, spec in inputs.items():
                    spec = spec if isinstance(spec, dict) else {"id": spec}
                    iid = str(spec.get("id"))
                    fixed = None
                    if iid in consts:
                        if iid == "k_percent_per_unit" and tu and not target_pct:
                            # v2.8k（一道网页题输出 0.0066 人）：代码已经把每个 % 输入换成小数，再除以 k_percent_per_unit 就小了 100 倍；
                            # 单位核对查不出（100 percent = 1，量纲不变）。只有目标本身是百分数时才用得上它
                            raise M.MethodError(f"input {name}: k_percent_per_unit is only for a percentage target; code already turns "
                                                "every % input into a fraction, so dividing by it makes the result 100 times too small. "
                                                "Remove it from the formula")
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
                        pct = (A.is_pct(p.get("unit")) and not target_pct) if tu else p.get("unit") == "%"
                        f = 100 if pct else 1   # 除以 f（不乘 0.01：浮点结果和以前逐位相同）
                        v = p["value"] / f if pct else p["value"]
                        if not (v > 0):
                            raise M.MethodError(f"input {name} must be positive for lognormal sampling")
                        # 观测点的不确定度由代码统一给；裁判填的 rel_uncertainty 只记录，不使用
                        lo, hi = v / (1 + M.DEFAULT_REL_U), v * (1 + M.DEFAULT_REL_U)
                        rng_lo, rng_hi = p.get("value_low"), p.get("value_high")   # v2.8o：原文给的区间
                        ranged = isinstance(rng_lo, (int, float)) and isinstance(rng_hi, (int, float)) and 0 <= rng_lo < rng_hi
                        if "rel_uncertainty" in spec:
                            r.setdefault("rel_uncertainty_from_judge_ignored", {})[name] = spec.get("rel_uncertainty")
                        used.append(iid)
                        kind = "point"
                    if kind == "point" and ranged:
                        env[name] = draws.get_range(iid, rng_lo / f, rng_hi / f)
                        q = sorted(env[name])
                        detail.append({"name": name, "id": iid, "kind": kind, "p10": q[len(q) // 10], "p90": q[len(q) * 9 // 10],
                                       "value": v, "low": rng_lo / f, "high": rng_hi / f, "unit": pts[iid].get("unit") or ""})
                        continue
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
                    # v2.6b（B5 的一部分）：点名每个观测点 / 假设输入（id、unit、name 的前 60 个字符），修正轮才知道是哪个输入被当成了比率
                    checked = [d for d in detail if d["kind"] in ("point", "assumption")]
                    names = {d["id"]: (kept_a if d["kind"] == "assumption" else pts)[d["id"]].get("name", "") for d in checked}
                    named = "; ".join(f'{d["name"]} = {d["id"]} (unit "{d["unit"]}", name "{str(names[d["id"]])[:60]}")'
                                      for d in checked)
                    # 输入写在说明前面：ledger 的方法表只显示报错的前 200 个字符（outputs.ledger）
                    raise M.MethodError("formula_mc needs at least one input that is a quantity (not a share, ratio or %); "
                                        f"a product of ratios cannot produce the target. Inputs: {named}. Code reads each of "
                                        "these units as a share, ratio, % or empty unit")
                if len(set(used_a)) > cap:
                    raise M.MethodError(f"formula_mc uses {len(set(used_a))} assumptions (at most {cap})")
                try:
                    s = M.formula_mc_samples(str(prm.get("formula", "")), env)
                except M.MethodError as e:
                    # v2.8d（冒烟测试 smoke_pizza）：公式里的 / 1000 是克换千克；只说「make it a named input」，修正轮就自造了
                    # k_grams_per_kg 这种不存在的常数。钉了单位时，换单位交给代码
                    if tu and "numeric constant" in str(e):
                        raise M.MethodError(f"{e}. If the number only converts units (1000 g per kg, days per year), drop it and "
                                            f"set the method's \"unit\" to the unit the formula then gives (e.g. 'g/day'); "
                                            f"code converts it to '{tu}'") from None
                    raise
                f = 1.0
                if tu:
                    mu = m.get("unit")
                    if not isinstance(mu, str) or not mu.strip():
                        raise M.MethodError(f"give the method a \"unit\": the unit its formula produces, in pint notation (e.g. 'kg/year' "
                                            f"for an annual total); code converts it to the target unit '{tu}'")
                    f, err = Q.convert_factor(mu.strip(), tu)
                    if err:
                        raise M.MethodError(f"unit of the formula's result: {err}. Write the unit the formula actually produces "
                                            "(an annual total gives a per-year result); code converts units, do not add scale factors")
                    r["unit_check"] = {"unit": mu.strip(), "target_unit": tu, "factor": f}
                r.update(estimate=s["median"] * f, mc={"p10": s["p10"] * f, "p90": s["p90"] * f})
            elif r["method"] == "outcome_probs":
                raise M.MethodError("outcome_probs is only available for a discrete target (outcome_type 'discrete'); "
                                    "this target is continuous")
            else:
                raise M.MethodError(f"unknown method {r['method']!r}")
            if excluded:   # 只覆盖一部分：结果留作诊断，不进合并（权重 0），原因交给修正轮
                r["coverage_excluded"] = {"estimate": r["estimate"], "mc": r.pop("mc", None)}
                r["estimate"], r["error"] = None, excluded
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

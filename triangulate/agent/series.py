"""目标自身的月度序列（v2.12 算子层）：裁判列出的目标历史点 -> 按月排好的序列；series_auto 由代码按数据决定用哪些成员。
不调模型，所有数字由代码算。

月度序列（build_monthly）：
- 只收裁判 keep 的点；页面日期兜底的点不收（同 compute.build_series）；% 和非 % 混在一起时丢少数一方（同 build_series）。
- 期间是一个日历月（期初、期末各在月初、月末 3 天内）-> 月值；同年 1 月 1 日到某月末（2-12 月）-> 年内累计（ytd），
  单独存、不当月值用；其他期间（季度、周、跨年的 12 个月……）不收，记原因。
- 目标月和它以后的月不收；非正的值不收（ln 空间的算子用不了）。同一个月有几个值取中位数，相差 > 0.5% 记一句。
月份序号 t = 年 * 12 + 月 - 1，和基准（bench/harness.py）一致。

series_auto（决定 2，阈值来自基准，见 BENCH_ZH.md）：
- h = 目标月 - 序列最后一个月，只做 h = 1..H_MAX（基准只测了 1..4，校准表也只有这几行）。
- 以最后一个月结尾的连续月 >= MIN_MODEL（13）：成员 = AutoETS、Theta（statsforecast 2.1.1，season_length 12）、yoy3、
  全局 LightGBM（lgbm_global.py），点估计 = 四个成员的算术平均（基准的 comb_ETYL_mean）。窗口最多取最近 MAX_WINDOW（36）
  个月 [人为约定：基准测过的最长 L]；校准行按窗口长度归到 L13（13-23 个月）/ L24（24-35）/ L36（36）。任一成员失败就退到 yoy 路径。
- 否则（或模型失败）：yoy3 = 去年同月 x 最近至多 3 个同比对的增长（合计比合计）；同比对 = 月 k 和 k-12 都有值，
  且 k 在去年同月之后（k > 目标月 - 12）、不晚于最后一个月；只有一对时就是 yoy1。校准行按同比对个数（1 / 2 / 3）。
- 区间：校准表（calibration.py）里那一行的 ln 误差 10% / 90% 分位；用了哪一行记在结果里。
- 季节朴素（去年同月）只作对照基线记在结果里（baseline），不是成员。
"""
import calendar
import math
import statistics
import warnings
from datetime import date, timedelta

from .evidence import PAGE_DATE, parse_date

TOL_DAYS = 3
MIN_MODEL = 13        # 模型路径至少要的连续月数（基准最短的 L）
MAX_WINDOW = 36       # 模型路径最多用的月数（基准最长的 L）[人为约定]
H_MAX = 4             # 基准只测了 h = 1..4
YOY_PAIRS = 3         # yoy3：最多 3 个同比对
DISAGREE = 0.005      # 同月几个值相差超过 0.5% 就记一句


class SeriesError(ValueError):
    pass


def mi(y: int, m: int) -> int:
    return y * 12 + m - 1


def ym(t: int) -> str:
    return f"{t // 12:04d}-{t % 12 + 1:02d}"


def _month_bounds(t: int):
    y, m = t // 12, t % 12 + 1
    return date(y, m, 1), date(y, m, calendar.monthrange(y, m)[1])


def classify(ps, pe):
    """(kind, t)：kind = "month"（一个日历月）/ "ytd"（同年 1 月到第 t 个月的累计）；都不是返回 (None, None)。"""
    if ps is None or pe is None:
        return None, None
    k = pe - timedelta(days=TOL_DAYS)          # 期末比月末多出 / 少几天时仍归到同一个月
    t = mi(k.year, k.month)
    first, last = _month_bounds(t)
    if abs((pe - last).days) > TOL_DAYS:
        return None, None
    if abs((ps - first).days) <= TOL_DAYS:
        return "month", t
    if t % 12 >= 1 and abs((ps - date(t // 12, 1, 1)).days) <= TOL_DAYS:
        return "ytd", t
    return None, None


def target_month(tps, tpe):
    """目标期间是不是一个日历月：是就返回它的月份序号，否则 None。"""
    kind, t = classify(tps, tpe)
    return t if kind == "month" else None


def build_monthly(ids, pts: dict, target_t: int) -> dict:
    """裁判列的目标历史 id -> {"months": {t: 值}, "month_ids": {t: [id]}, "ytd": {t: 值}, "ytd_ids": {t: [id]},
    "notes": [...], "used_ids": [...], "units": [...]}。规则见文件头。"""
    notes, cand = [], []
    for i in ids or []:
        p = pts.get(i)
        if p is None:
            notes.append(f"{i}: unknown id")
            continue
        if not p.get("keep", True):
            notes.append(f"{i}: discarded by judge, not used")
            continue
        if p.get("period_source") == PAGE_DATE:
            notes.append(f"{i}: period not stated in the source (page dated {p.get('period_end')}), not used in a series")
            continue
        pe = parse_date(p.get("period_end"), end=True)
        ps = parse_date(p.get("period_start"))
        if pe is None or ps is None:
            notes.append(f"{i}: period start or end missing, cannot tell a month from a cumulative total")
            continue
        cand.append((i, ps, pe, p))
    pct = [c for c in cand if c[3].get("unit") == "%"]
    if pct and len(pct) != len(cand):
        notes.append("mixed % and non-% units; dropped the minority")
        cand = pct if len(pct) > len(cand) / 2 else [c for c in cand if c[3].get("unit") != "%"]
    vals = {"month": {}, "ytd": {}}
    for i, ps, pe, p in cand:
        kind, t = classify(ps, pe)
        if kind is None:
            notes.append(f"{i}: period {ps}..{pe} is neither one calendar month nor a year-to-date total from 1 January")
            continue
        if t >= target_t:
            notes.append(f"{i}: period {ym(t)} is at or after the target month {ym(target_t)}")
            continue
        v = p.get("value")
        if not isinstance(v, (int, float)) or not v > 0:
            notes.append(f"{i}: value {v!r} is not positive, not used")
            continue
        vals[kind].setdefault(t, []).append((i, float(v)))
    out = {"notes": notes, "units": sorted({str(c[3].get("unit") or "") for c in cand})}
    used = []
    for kind, key, key_ids in (("month", "months", "month_ids"), ("ytd", "ytd", "ytd_ids")):
        series, sids = {}, {}
        for t in sorted(vals[kind]):
            vs = vals[kind][t]
            med = statistics.median(v for _, v in vs)
            lo, hi = min(v for _, v in vs), max(v for _, v in vs)
            if hi / lo - 1 > DISAGREE:
                notes.append(f"{ym(t)} ({kind}): values disagree ({', '.join(f'{i} = {v:,.6g}' for i, v in vs)}); "
                             f"median {med:,.6g} used")
            series[t], sids[t] = med, [i for i, _ in vs]
            used += sids[t]
        out[key], out[key_ids] = series, sids
    if out["ytd"]:
        notes.append(f"year-to-date totals kept separately, not used as months: {', '.join(ym(t) for t in out['ytd'])}")
    out["used_ids"] = used
    return out


def tail_run(months: dict, last: int) -> list:
    """以 last 结尾的连续月（升序）。"""
    run = [last]
    while run[0] - 1 in months:
        run.insert(0, run[0] - 1)
    return run


def yoy(months: dict, target_t: int, last: int, w: int = YOY_PAIRS) -> dict:
    """去年同月 x 最近至多 w 个同比对的增长（合计比合计）。同比对 = 月 k 和 k-12 都有值，目标月 - 12 < k <= last。"""
    base = target_t - 12
    if base not in months:
        raise SeriesError(f"needs last year's value for the target month ({ym(base)})")
    ks = [k for k in sorted(months, reverse=True) if base < k <= last and k - 12 in months][:w]
    if not ks:
        raise SeriesError(f"needs at least one month after {ym(base)} that also has its value a year earlier "
                          f"(no year-on-year pair)")
    num, den = sum(months[k] for k in ks), sum(months[k - 12] for k in ks)
    g = num / den
    return {"estimate": months[base] * g, "growth": g, "base_month": ym(base), "base_value": months[base],
            "pairs": [{"month": ym(k), "value": months[k], "year_earlier": months[k - 12]} for k in sorted(ks)],
            "n_pairs": len(ks), "months_used": sorted({base} | set(ks) | {k - 12 for k in ks})}


def _yoy_params(y3: dict) -> dict:
    return {k: y3[k] for k in ("base_month", "base_value", "growth", "n_pairs", "pairs")}


def _ets(y, h):
    from statsforecast.models import AutoETS
    with warnings.catch_warnings():   # 短序列上库会报除零之类的 RuntimeWarning（基准里同样忽略）；结果的有限性另外检查
        warnings.simplefilter("ignore")
        m = AutoETS(season_length=12).fit(y)
        return float(m.predict(h)["mean"][h - 1]), {"model": m.model_["method"], "season_length": 12}


def _theta(y, h):
    from statsforecast.models import Theta
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = Theta(season_length=12).fit(y)
        return float(m.predict(h)["mean"][h - 1]), {"model": "Theta(season_length=12, decomposition_type=multiplicative)"}


def _lgbm(y, t, h):
    from . import lgbm_global as LG
    return LG.predict_one(y, t, h), {"model": "global LightGBM, 0.5 quantile", "cfg_key": LG.cfg_key(),
                                     "bench_cfg_key": LG.BENCH_CFG_KEY,
                                     "files": sorted(p.name for p in LG.model_paths().values()),
                                     "point_model": LG.model_paths()[0.5].name, "point_model_text_sha256": LG.text_sha256(0.5)}


def l_bucket(n: int) -> int:
    return 13 if n < 24 else 24 if n < 36 else 36


def _finite_pos(x) -> bool:
    return isinstance(x, float) and math.isfinite(x) and x > 0


def seasonal_baseline(ms: dict, target_t: int):
    """季节朴素对照（决定 3）：目标去年同月的值；没有返回 None。build_monthly 只收正值，所以有就 > 0。
    compute 在调 series_auto 之前就记下它，series_auto 做不了（h > 4、没有同比对）时对照照样有（v2.12d）。"""
    base = target_t - 12
    v = ms["months"].get(base)
    return None if v is None else {"method": "seasonal naive (last year's same month)", "month": ym(base), "estimate": v,
                                   "ids": list(ms["month_ids"].get(base) or [])}


def series_auto(ms: dict, target_t: int) -> dict:
    """ms = build_monthly 的结果。返回 estimate、成员估计、用到的月份、校准行、区间和季节朴素基线；做不了抛 SeriesError。"""
    months = ms["months"]
    if not months:
        raise SeriesError("no monthly values of the target series (the listed ids give no single calendar months "
                          "before the target)")
    last = max(months)
    h = target_t - last
    if h > H_MAX:
        raise SeriesError(f"the last known month is {ym(last)}, {h} months before the target {ym(target_t)}; series_auto is "
                          f"calibrated only for 1 to {H_MAX} months ahead")
    run = tail_run(months, last)
    out = {"h": h, "last_month": ym(last), "consecutive_months": len(run), "notes": [],
           "baseline": seasonal_baseline(ms, target_t)}
    if len(run) >= MIN_MODEL:
        window = run[-MAX_WINDOW:]
        wm = {k: months[k] for k in window}
        try:
            mem, prm = _members(wm, window, target_t, last, h)
        except Exception as e:   # 成员失败（库报错、非有限值）：退到 yoy 路径，原因记下（v2.12d：另存一份给终稿写明）
            out["models_path_failed"] = f"{type(e).__name__}: {str(e)[:160]}"
            out["notes"].append(f"model path failed ({out['models_path_failed']}); used the year-on-year path")
        else:
            point = statistics.fmean(mem.values())
            key, row = _cal_row("comb_ETYL_mean", f"L{l_bucket(len(window))}", h)
            out.update(path="models", rule="arithmetic mean of AutoETS, Theta, yoy3 and LightGBM (benchmark comb_ETYL_mean)",
                       estimate=point, members=mem, member_params=prm, **_window(window, ms))
            out.update(_interval(point, key, row))
            return out
    y3 = yoy(months, target_t, last)
    key, row = _cal_row("yoy", f"pairs{y3['n_pairs']}", h)
    # v2.12d（审查）：规则名跟成员名、校准行一样按实际的同比对个数（以前 2 对时写 yoy3）
    out.update(path="yoy", rule=("yoy1: last year's same month x the year-on-year growth of the one available pair"
                                 if y3["n_pairs"] == 1 else
                                 f"yoy{y3['n_pairs']}: last year's same month x the summed growth of the latest "
                                 f"{y3['n_pairs']} year-on-year pairs"),
               estimate=y3["estimate"], members={f"yoy{y3['n_pairs']}": y3["estimate"]},
               member_params={f"yoy{y3['n_pairs']}": _yoy_params(y3)},
               **_window(y3["months_used"], ms))
    out.update(_interval(y3["estimate"], key, row))
    return out


def _members(wm: dict, window: list, target_t: int, last: int, h: int) -> tuple:
    """模型路径的四个成员：({名字: 点估计}, {名字: 参数})；有一个不是有限正数就抛 SeriesError。"""
    y = [wm[k] for k in window]
    ets, p_ets = _ets(_arr(y), h)
    th, p_th = _theta(_arr(y), h)
    y3 = yoy(wm, target_t, last)
    lg, p_lg = _lgbm(y, list(window), h)
    mem = {"AutoETS": float(ets), "Theta": float(th), "yoy3": float(y3["estimate"]), "LightGBM": float(lg)}
    bad = [k for k, v in mem.items() if not _finite_pos(v)]
    if bad:
        raise SeriesError(f"member(s) {', '.join(bad)} gave a non-finite or non-positive value")
    return mem, {"AutoETS": p_ets, "Theta": p_th, "yoy3": _yoy_params(y3), "LightGBM": p_lg}


def _window(ts, ms: dict) -> dict:
    ts = sorted(ts)
    return {"window": [ym(k) for k in ts], "window_ids": [i for k in ts for i in ms["month_ids"][k]],
            "window_month_ids": {ym(k): list(ms["month_ids"][k]) for k in ts}}   # v2.12d：每个月用了哪些点（同月取中位数）


def _arr(y):
    import numpy as np
    return np.asarray(y, float)


def _cal_row(kind: str, bucket: str, h: int) -> tuple:
    from . import calibration as CAL   # 表由 models/build_calibration.py 生成；生成脚本本身要 import 本模块，所以这里晚导入
    return CAL.row(kind, bucket, h)


def _interval(point: float, key: str, row: dict) -> dict:
    from . import calibration as CAL
    return {"interval": {"p10": point * math.exp(row["q10"]), "p90": point * math.exp(row["q90"]), "calibration_row": key,
                         "q10_ln": row["q10"], "q90_ln": row["q90"], "n_cases": row["n"], "table": CAL.TABLE_ID,
                         "cov80_by_dataset_in_sample": {d: row[f"cov80_{d}"] for d in ("M4", "M3", "Tourism")}}}

"""代码方法库：裁判只选方法、给参数（数据点 id），数字全部在这里算。

序列对齐规则：一个序列 = 同一个量在不同年份的同一日历期间；按 period_end 的年份对齐（同一年有多个来源时取中位数）。
回测：在目标的历史年份上逐年回测（series_naive / yoy_scaling 只用该年之前的数据；linear_fit / ratio 用留一年法，
拟合时去掉被测年和目标年）。误差 = ln(预测 / 实际)。
加权：有回测的方法权重 = 1 / (平均 |ln 误差| + EPS)；没回测的方法取有回测方法权重的中位数；全都没回测就等权。
合并：加权几何平均。区间规则见 combine()。
"""
import math
import statistics

from ..expr import Formula, FormulaError
from ..mc import sample_inputs, summarise

EPS = 0.01            # 1% 的误差下限，防止某个方法回测碰巧几乎为 0 时独占权重
Z90 = 1.2815515655446004
FALLBACK_SIGMA = 0.25  # 既无回测、也无方法分歧、也无 MC 时的区间宽度（ln 空间），报告里标为 no_basis
MC_N = 20000
MC_SEED = 20261015


class MethodError(ValueError):
    pass


# ---------- 单个方法：输入是 {year: value} ----------
def series_naive(target: dict, year: int, k: int = 1) -> float:
    prior = sorted(y for y in target if y < year)[-k:]
    if len(prior) < k:
        raise MethodError(f"series_naive needs {k} earlier years, has {len(prior)}")
    return statistics.fmean(target[y] for y in prior)


def yoy_scaling(target: dict, signal: dict, year: int) -> float:
    need = [(target, year - 1, "target"), (signal, year - 1, "signal"), (signal, year, "signal")]
    for s, y, name in need:
        if y not in s:
            raise MethodError(f"yoy_scaling needs {name} for {y}")
    if signal[year - 1] <= 0:
        raise MethodError("signal for previous year is not positive")
    return target[year - 1] * signal[year] / signal[year - 1]


def _common(target, signal, year, exclude):
    """正式预测（exclude=None）：只用 year 之前的年份。回测（exclude=被测年）：留一年法，用除被测年以外的所有年份
    （调用方已去掉目标年）。"""
    ys = sorted(y for y in set(target) & set(signal) if y != year and y != exclude and (exclude is not None or y < year))
    if year not in signal:
        raise MethodError(f"signal has no value for {year}")
    return ys


def linear_fit(target: dict, signal: dict, year: int, exclude=None) -> float:
    ys = _common(target, signal, year, exclude)
    if len(ys) < 3:
        raise MethodError(f"linear_fit needs >= 3 aligned years, has {len(ys)}")
    xs = [signal[y] for y in ys]
    if len(set(xs)) < 2:
        raise MethodError("signal is constant over aligned years")
    slope, icpt = statistics.linear_regression(xs, [target[y] for y in ys])
    pred = slope * signal[year] + icpt
    if pred <= 0:
        raise MethodError("linear_fit prediction is not positive")
    return pred


def ratio(target: dict, signal: dict, year: int, exclude=None) -> float:
    ys = [y for y in _common(target, signal, year, exclude) if signal[y] > 0]
    if not ys:
        raise MethodError("ratio needs >= 1 aligned year")
    return signal[year] * statistics.fmean(target[y] / signal[y] for y in ys)


def formula_mc(formula: str, inputs: dict) -> dict:
    """inputs: name -> (value, rel_uncertainty)。value 以 P10/P90 = value/(1+u), value*(1+u) 的 lognormal 采样。"""
    try:
        f = Formula(formula)
    except FormulaError as e:
        raise MethodError(f"formula: {e}") from None
    if f.names != set(inputs):
        raise MethodError(f"formula names {sorted(f.names)} != inputs {sorted(inputs)}")
    ranges = {}
    for name, (v, u) in inputs.items():
        if not (v > 0):
            raise MethodError(f"input {name} must be positive for lognormal sampling")
        u = min(max(float(u), 0.0), 1.0)
        ranges[name] = (v / (1 + u), v * (1 + u))
    s = summarise(f.eval_vec(sample_inputs(ranges, MC_N, MC_SEED), MC_N))
    if not (s["median"] > 0):
        raise MethodError("formula median is not positive")
    return s


# ---------- 回测 ----------
def backtest(method: str, target: dict, signal: dict, year: int, k: int = 1) -> list:
    """返回 [{year, pred, actual, log_err}]；做不出的年份跳过。"""
    out = []
    for y in sorted(t for t in target if t < year):
        try:
            if method == "series_naive":
                pred = series_naive(target, y, k)
            elif method == "yoy_scaling":
                pred = yoy_scaling(target, signal, y)
            elif method in ("linear_fit", "ratio"):
                fit_t = {t: v for t, v in target.items() if t != year}
                fit_s = {t: v for t, v in signal.items() if t != year}
                pred = (linear_fit if method == "linear_fit" else ratio)(fit_t, fit_s, y, exclude=y)
            else:
                return []
        except MethodError:
            continue
        if pred > 0 and target[y] > 0:
            out.append({"year": y, "pred": pred, "actual": target[y], "log_err": math.log(pred / target[y])})
    return out


# ---------- 合并与区间 ----------
def combine(results: list) -> dict:
    """results: [{id, estimate, backtest:[...], mc:{p10,p90}|None}]（只放算出了估计的方法）。

    区间规则（80%，ln 空间对称，central x exp(+-Z90 * sigma)）：
    1. 有回测（全部方法合计 >= 2 个回测年）：sigma_hist = sqrt(按权重平均的回测 ln 误差平方)；
       若方法之间的分歧 sigma_spread 更大，取更大的（历史误差小但方法互相打架时不该给窄区间）。
    2. 否则，有 >= 2 个方法：sigma = max(sigma_spread, sigma_mc)。
    3. 否则只有 formula_mc：用它自己的 MC 区间宽度。
    4. 都没有：FALLBACK_SIGMA，basis = no_basis。
    """
    ok = [r for r in results if r.get("estimate") and r["estimate"] > 0]
    if not ok:
        return {"central": None, "p10": None, "p90": None, "weights": {}, "basis": "no_method"}
    bt = {r["id"]: [e["log_err"] for e in r.get("backtest") or []] for r in ok}
    raw = {i: 1 / (statistics.fmean(abs(x) for x in errs) + EPS) for i, errs in bt.items() if errs}
    if raw:
        fill = statistics.median(raw.values())
        w = {r["id"]: raw.get(r["id"], fill) for r in ok}
        rule = "inverse_backtest_error"
    else:
        w = {r["id"]: 1.0 for r in ok}
        rule = "equal"
    tot = sum(w.values())
    w = {i: v / tot for i, v in w.items()}
    logc = sum(w[r["id"]] * math.log(r["estimate"]) for r in ok)
    central = math.exp(logc)
    spread = math.sqrt(sum(w[r["id"]] * (math.log(r["estimate"]) - logc) ** 2 for r in ok)) if len(ok) >= 2 else None
    mc = [(math.log(r["mc"]["p90"]) - math.log(r["mc"]["p10"])) / (2 * Z90) for r in ok
          if r.get("mc") and r["mc"].get("p10", 0) > 0]
    sig_mc = max(mc) if mc else None
    n_folds = sum(len(e) for e in bt.values())
    hist = None
    if n_folds >= 2:
        ws = {i: w[i] for i in bt if bt[i]}
        hist = math.sqrt(sum(ws[i] * statistics.fmean(x * x for x in bt[i]) for i in ws) / sum(ws.values()))
    if hist is not None:
        sigma, basis = max(hist, spread or 0.0), "historical_errors" if hist >= (spread or 0) else "method_spread"
    elif spread is not None:
        sigma, basis = max(spread, sig_mc or 0.0), "method_spread" if spread >= (sig_mc or 0) else "monte_carlo"
    elif sig_mc is not None:
        sigma, basis = sig_mc, "monte_carlo"
    else:
        sigma, basis = FALLBACK_SIGMA, "no_basis"
    return {"central": central, "p10": central * math.exp(-Z90 * sigma), "p90": central * math.exp(Z90 * sigma),
            "sigma_ln": sigma, "sigma_hist": hist, "sigma_spread": spread, "sigma_mc": sig_mc, "n_backtest_folds": n_folds,
            "weights": w, "weight_rule": rule, "basis": basis}

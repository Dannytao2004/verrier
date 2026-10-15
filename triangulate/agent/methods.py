"""代码方法库：裁判只选方法、给参数（数据点 id），数字全部在这里算。

序列对齐规则：一个序列 = 同一个量在不同年份的同一日历期间；按 period_end 的年份对齐（同一年有多个来源时取中位数）。
series_naive 取「目标年之前、有值的最近 k 个年份」，年份可以不连续（用到哪几年记在结果里）。
回测：在目标的历史年份上逐年回测，所有方法都只用被测年之前的数据（扩展窗口；signal 另取被测年当年的值）。
误差 = ln(预测 / 实际)。
加权：有回测的方法权重 = 1 / (平均 |ln 误差| + EPS)；没回测的方法（典型的是带假设输入的 formula_mc）取有回测方法
权重的中位数，相当于「有回测方法的中位误差」、惩罚系数 1（不打折：没有证据说明没回测的路线更差或更好，打折系数只能
拍脑袋）；全都没回测就等权。所以没回测的方法不会自动拿 0 权重。每个方法按哪条规则拿的权重记在 weight_basis 里。
合并：加权几何平均（内部按列表下标，不按 id）。区间规则见 combine()。
formula_mc：公式另过一道 agent 专用的白名单（整数指数、不许纯常数子式、常数 1 至多 3 个）；观测点输入的不确定度由代码
统一给 DEFAULT_REL_U，裁判填的值只记录、不使用；假设输入按裁判给的 low / high（经代码放宽，见 assumptions.py）采样。
样本按输入 id 抽（compute.Draws），同一个点或假设在几个方法里用的是同一份样本。
"""
import ast
import math
import statistics

from ..expr import Formula, FormulaError, _const
from ..mc import sample_inputs, summarise

EPS = 0.01            # 1% 的误差下限，防止某个方法回测碰巧几乎为 0 时独占权重
Z90 = 1.2815515655446004
FALLBACK_SIGMA = 0.25  # 既无回测、也无方法分歧、也无 MC 时的区间宽度（ln 空间），报告里标为 no_basis
MC_N = 20000
MC_SEED = 20261015
DEFAULT_REL_U = 0.2    # formula_mc 每个输入的 80% 相对不确定度（P10/P90 = v/1.2, v*1.2），由代码统一给
MAX_EXP_AGENT = 3      # formula_mc 只许整数指数 -3..3（开方用 sqrt()）
MAX_ONES = 3           # formula_mc 里常数 1 至多出现 3 次（1 - share、1 + growth 这类写法够用）
MAX_NODES_AGENT = 60


class MethodError(ValueError):
    pass


# ---------- 单个方法：输入是 {year: value} ----------
def series_naive(target: dict, year: int, k: int = 1) -> float:
    prior = prior_years(target, year, k)
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


def prior_years(target: dict, year: int, k: int) -> list:
    """series_naive 用到的年份：year 之前有值的最近 k 年（可以不连续）。"""
    return sorted(y for y in target if y < year)[-k:]


def _common(target, signal, year):
    """只用 year 之前、target 和 signal 都有值的年份；signal 还必须有 year 当年的值。"""
    ys = sorted(y for y in set(target) & set(signal) if y < year)
    if year not in signal:
        raise MethodError(f"signal has no value for {year}")
    return ys


def linear_fit(target: dict, signal: dict, year: int) -> float:
    ys = _common(target, signal, year)
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


def ratio(target: dict, signal: dict, year: int) -> float:
    ys = [y for y in _common(target, signal, year) if signal[y] > 0]
    if not ys:
        raise MethodError("ratio needs >= 1 aligned year")
    return signal[year] * statistics.fmean(target[y] / signal[y] for y in ys)


def _has_name(node) -> bool:
    """子树里有没有输入名（min/max/sqrt 这些函数名不算）。"""
    funcs = {id(c.func) for c in ast.walk(node) if isinstance(c, ast.Call)}
    return any(isinstance(n, ast.Name) and id(n) not in funcs for n in ast.walk(node))


def check_agent_formula(f: Formula):
    """在通用白名单之上，再挡住「用常数拼出任意数」：指数只许 -3..3 的整数；每个二元运算和函数调用都必须含输入名
    （不许 1+1、1/(1+1) 这类纯常数子式）；常数 1 至多 MAX_ONES 个；节点数有上限。"""
    nodes = list(ast.walk(f.root))
    if len(nodes) > MAX_NODES_AGENT:
        raise MethodError(f"formula has more than {MAX_NODES_AGENT} nodes")
    in_exponent = set()
    for n in nodes:
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
            e = _const(n.right)
            if e is None or not float(e).is_integer() or abs(e) > MAX_EXP_AGENT:
                raise MethodError(f"exponent must be an integer in [-{MAX_EXP_AGENT}, {MAX_EXP_AGENT}]; use sqrt() for roots")
            in_exponent |= {id(x) for x in ast.walk(n.right)}
    ones = 0
    for n in nodes:
        if id(n) in in_exponent:
            continue
        if isinstance(n, (ast.BinOp, ast.Call)) and not _has_name(n):
            raise MethodError("constant-only sub-expression in formula")
        if isinstance(n, ast.Constant):
            ones += 1
    if ones > MAX_ONES:
        raise MethodError(f"formula uses the constant 1 more than {MAX_ONES} times")


def _agent_formula(formula: str) -> Formula:
    try:
        f = Formula(formula)
    except FormulaError as e:
        raise MethodError(f"formula: {e}") from None
    check_agent_formula(f)
    return f


def formula_mc(formula: str, inputs: dict) -> dict:
    """inputs: name -> (value, rel_uncertainty)。value 以 P10/P90 = value/(1+u), value*(1+u) 的 lognormal 采样。
    agent 的 compute.py 不走这里：它按输入 id 先抽好样本（同一个 id 在几个方法里共用一份样本），再调 formula_mc_samples。"""
    f = _agent_formula(formula)
    if f.names != set(inputs):
        raise MethodError(f"formula names {sorted(f.names)} != inputs {sorted(inputs)}")
    ranges = {}
    for name, (v, u) in inputs.items():
        if not (v > 0):
            raise MethodError(f"input {name} must be positive for lognormal sampling")
        u = min(max(float(u), 0.0), 1.0)
        ranges[name] = (v / (1 + u), v * (1 + u))
    return formula_mc_samples(formula, sample_inputs(ranges, MC_N, MC_SEED))


def formula_mc_samples(formula: str, env: dict) -> dict:
    """env: name -> 长度 MC_N 的样本列表（调用方已抽好）。返回样本分布的摘要（median / p10 / p90）。"""
    f = _agent_formula(formula)
    if f.names != set(env):
        raise MethodError(f"formula names {sorted(f.names)} != inputs {sorted(env)}")
    s = summarise(f.eval_vec(env, MC_N))
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
                # 扩展窗口：只用 y 之前的年份拟合，signal 另带 y 当年的值（和正式预测同一口径）
                fit_t = {t: v for t, v in target.items() if t < y}
                fit_s = {t: v for t, v in signal.items() if t <= y}
                pred = (linear_fit if method == "linear_fit" else ratio)(fit_t, fit_s, y)
            else:
                return []
        except MethodError:
            continue
        if pred > 0 and target[y] > 0:
            out.append({"year": y, "pred": pred, "actual": target[y], "log_err": math.log(pred / target[y])})
    return out


# ---------- 合并与区间 ----------
def combine(results: list) -> dict:
    """results: [{id, estimate, backtest:[...], mc:{p10,p90}|None}]（只放算出了估计的方法）。id 必须互不相同
    （compute.run 统一编号 m1..mN）；计算内部按列表下标，id 只用来给 weights 起名。

    区间规则（80%，ln 空间对称，central x exp(+-Z90 * sigma)）：
    1. 有回测（全部方法合计 >= 2 个回测年）：sigma_hist = sqrt(按权重平均的回测 ln 误差平方)；
       若方法之间的分歧 sigma_spread 更大，取更大的（历史误差小但方法互相打架时不该给窄区间）。
    2. 没有回测：sigma = max(sigma_spread, sigma_mc, FALLBACK_SIGMA)。方法分歧和 MC 宽度只能把区间放宽，
       不能把它压到 FALLBACK_SIGMA 以下（两个方法用同一份证据时分歧接近 0，不代表不确定性小）。
       basis 记最大的那一项；FALLBACK_SIGMA 最大时记 no_basis。
    """
    ok = [r for r in results if r.get("estimate") and r["estimate"] > 0]
    if not ok:
        return {"central": None, "p10": None, "p90": None, "weights": {}, "basis": "no_method"}
    ids = [str(r.get("id", "")) for r in ok]
    if len(set(ids)) != len(ids):
        raise MethodError(f"duplicate method ids {ids}")
    bt = [[e["log_err"] for e in r.get("backtest") or []] for r in ok]
    raw = {i: 1 / (statistics.fmean(abs(x) for x in errs) + EPS) for i, errs in enumerate(bt) if errs}
    if raw:
        fill = statistics.median(raw.values())
        w = [raw.get(i, fill) for i in range(len(ok))]
        rule = "inverse_backtest_error"
        wbasis = ["backtest" if i in raw else "median_of_backtested" for i in range(len(ok))]
    else:
        w = [1.0] * len(ok)
        rule = "equal"
        wbasis = ["equal"] * len(ok)
    tot = sum(w)
    w = [v / tot for v in w]
    logs = [math.log(r["estimate"]) for r in ok]
    logc = sum(wi * li for wi, li in zip(w, logs))
    central = math.exp(logc)
    spread = math.sqrt(sum(wi * (li - logc) ** 2 for wi, li in zip(w, logs))) if len(ok) >= 2 else None
    mc = [(math.log(r["mc"]["p90"]) - math.log(r["mc"]["p10"])) / (2 * Z90) for r in ok
          if r.get("mc") and r["mc"].get("p10", 0) > 0]
    sig_mc = max(mc) if mc else None
    n_folds = sum(len(e) for e in bt)
    hist = None
    if n_folds >= 2:
        idx = [i for i, e in enumerate(bt) if e]
        hist = math.sqrt(sum(w[i] * statistics.fmean(x * x for x in bt[i]) for i in idx) / sum(w[i] for i in idx))
    if hist is not None:
        sigma, basis = max(hist, spread or 0.0), "historical_errors" if hist >= (spread or 0) else "method_spread"
    else:
        cands = [(FALLBACK_SIGMA, "no_basis"), (spread or 0.0, "method_spread"), (sig_mc or 0.0, "monte_carlo")]
        sigma, basis = max(cands, key=lambda c: c[0])
    return {"central": central, "p10": central * math.exp(-Z90 * sigma), "p90": central * math.exp(Z90 * sigma),
            "sigma_ln": sigma, "sigma_hist": hist, "sigma_spread": spread, "sigma_mc": sig_mc, "n_backtest_folds": n_folds,
            "weights": dict(zip(ids, w)), "weight_rule": rule, "weight_basis": dict(zip(ids, wbasis)), "basis": basis}

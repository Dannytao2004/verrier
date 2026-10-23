"""代码方法库：裁判只选方法、给参数（数据点 id），数字全部在这里算。

序列对齐规则：一个序列 = 同一个量在不同年份的同一日历期间；按 period_end 的年份对齐（同一年有多个来源时取中位数）。
series_naive 取「目标年之前、有值的最近一个年份」（季节朴素；v2.12 起只有 k=1：基准里 k=2、3 都显著差于 k=1，BENCH_ZH.md 1.4）。
v2.12 起它只作对照基线（compute 记在 baseline_only 和结果的 baseline 里，ledger、终稿写「vs seasonal naive」），不进合并。
yoy_scaling、ratio 都是 ratio 形式（beta = 1，比值取 ratio of means，METHODS_ZH.md 1.4）；linear_fit（几个年度点上的 OLS）
v2.12 删掉了。目标自身的月度序列方法（series_auto）在 series.py；部分期间放大（partial_period）的公式在本文件，期间核对在 compute.py。
回测：在目标的历史年份上逐年回测，所有方法都只用被测年之前的数据（扩展窗口；signal 另取被测年当年的值）。
误差 = ln(预测 / 实际)。回测误差只用来定区间宽度，不用来加权（v2.12，见 combine 前的注释）。
合并：按输入分块、块等权（ln 空间：1 块 = 它自己，2 块 = 几何平均，>= 3 块 = 中位数）；区间规则见 combine 前的注释。
formula_mc：公式另过一道 agent 专用的白名单（整数指数、不许纯常数子式、常数 1 至多 3 个）；观测点输入的不确定度由代码
统一给 DEFAULT_REL_U，裁判填的值只记录、不使用；假设输入按裁判给的 low / high（经代码放宽，见 assumptions.py）采样。
样本按输入 id 抽（compute.Draws），同一个点或假设在几个方法里用的是同一份样本。
"""
import ast
import math
import statistics

from ..config import MC_SAMPLES as MC_N, MC_SEED   # Monte Carlo 样本数和种子：和 structured 基线同一来源
from ..expr import Formula, FormulaError, _const
from ..mc import Z90, sample_inputs, summarise

EPS = 0.01            # 1% 的下限：回测给的宽度、chi2 里的块宽度；WEIGHT_GATE 打开时防止某块回测碰巧几乎为 0 时独占权重
FALLBACK_SIGMA = 0.25  # 方法没有误差依据时的区间宽度（ln 空间），报告里标为 no_basis [人为约定，v2.11 起]
DEFAULT_REL_U = 0.2    # formula_mc 每个输入的 80% 相对不确定度（P10/P90 = v/1.2, v*1.2），由代码统一给
MAX_EXP_AGENT = 3      # formula_mc 只许整数指数 -3..3（开方用 sqrt()）
MAX_ONES = 3           # formula_mc 里常数 1 至多出现 3 次（1 - share、1 + growth 这类写法够用）
MAX_NODES_AGENT = 60


class MethodError(ValueError):
    pass


# ---------- 单个方法：输入是 {year: value} ----------
REMOVED = {"linear_fit": "linear_fit was removed from the method library (an OLS fit on a few annual points is unstable); "
                         "use ratio or yoy_scaling for a related signal, or series_auto for the target's own monthly history"}
BASELINE_ONLY = ("series_naive (the target's value for the same calendar period last year) is a baseline only: code reports "
                 "it for comparison and never combines it. For the target's own history use series_auto with all monthly "
                 "values of the target series")


def series_naive(target: dict, year: int, k: int = 1) -> float:
    """季节朴素：目标年之前有值的最近一年。k 只许 1（v2.12）。"""
    if k != 1:
        raise MethodError(f"series_naive k={k} is no longer available: averaging the {k} most recent years was less accurate "
                          "than the most recent year alone in the offline benchmark; use k=1")
    prior = prior_years(target, year, 1)
    if not prior:
        raise MethodError("series_naive needs 1 earlier years, has 0")   # 原文照旧（G4 逐字节比较）
    return target[prior[0]]


def yoy_scaling(target: dict, signal: dict, year: int) -> float:
    """ratio 形式（beta = 1）：目标去年值 x 信号今年 / 信号去年。"""
    need = [(target, year - 1, "target"), (signal, year - 1, "signal"), (signal, year, "signal")]
    for s, y, name in need:
        if y not in s:
            raise MethodError(f"yoy_scaling needs {name} for {y}")
    if signal[year - 1] <= 0:
        raise MethodError("signal for previous year is not positive")
    return target[year - 1] * signal[year] / signal[year - 1]


def yoy_detail(target: dict, signal: dict, year: int) -> dict:
    """yoy_scaling 用到的数（ledger、终稿显示用；先调 yoy_scaling 确认能算）。"""
    return {"base_year": year - 1, "target_base": target[year - 1], "signal_base": signal[year - 1],
            "signal_now": signal[year], "growth": signal[year] / signal[year - 1]}


def ratio_detail(target: dict, signal: dict, year: int) -> dict:
    """ratio 用到的年份和合计（ledger、终稿显示用；先调 ratio 确认能算）。"""
    ys = [y for y in _common(target, signal, year) if signal[y] > 0]
    st, ss = sum(target[y] for y in ys), sum(signal[y] for y in ys)
    return {"years": ys, "sum_target": st, "sum_signal": ss, "ratio": st / ss, "signal_now": signal[year]}


def prior_years(target: dict, year: int, k: int) -> list:
    """series_naive 用到的年份：year 之前有值的最近 k 年（可以不连续）。"""
    return sorted(y for y in target if y < year)[-k:]


def _common(target, signal, year):
    """只用 year 之前、target 和 signal 都有值的年份；signal 还必须有 year 当年的值。"""
    ys = sorted(y for y in set(target) & set(signal) if y < year)
    if year not in signal:
        raise MethodError(f"signal has no value for {year}")
    return ys


def ratio(target: dict, signal: dict, year: int) -> float:
    """ratio 形式：信号今年值 x 对齐年份上 sum(目标) / sum(信号)（ratio of means；v2.12 以前是逐年比值的算术平均）。"""
    ys = [y for y in _common(target, signal, year) if signal[y] > 0]
    if not ys:
        raise MethodError("ratio needs >= 1 aligned year")
    return signal[year] * sum(target[y] for y in ys) / sum(signal[y] for y in ys)


def partial_period(partial_this: float, pairs: list) -> dict:
    """部分期间放大（nowcast）：目标 = 本期已知部分 x sum(往期全期) / sum(往期同一部分)（ratio of means，beta = 1）。
    pairs = [(往期部分, 往期全期)]，至少一对，都 > 0，部分不能大于全期。覆盖率 = sum(部分) / sum(全期)。"""
    if not pairs:
        raise MethodError("partial_period needs at least one earlier period with both the partial and the full value")
    if not partial_this > 0:
        raise MethodError("partial_period: the partial value for this period must be positive")
    for part, full in pairs:
        if not (part > 0 and full > 0):
            raise MethodError("partial_period: earlier partial and full values must be positive")
        if part > full * (1 + 1e-9):
            raise MethodError(f"partial_period: an earlier partial value ({part:,.6g}) is larger than its full period "
                              f"({full:,.6g}), so it is not a part of it")
    cov = sum(p for p, _ in pairs) / sum(f for _, f in pairs)
    return {"estimate": partial_this / cov, "coverage": cov}


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
            elif method == "ratio":
                # 扩展窗口：只用 y 之前的年份，signal 另带 y 当年的值（和正式预测同一口径）
                fit_t = {t: v for t, v in target.items() if t < y}
                fit_s = {t: v for t, v in signal.items() if t <= y}
                pred = ratio(fit_t, fit_s, y)
            else:
                return []
        except MethodError:
            continue
        if pred > 0 and target[y] > 0:
            out.append({"year": y, "pred": pred, "actual": target[y], "log_err": math.log(pred / target[y])})
    return out


def backtest_partial(pairs: dict) -> list:
    """partial_period 的回测：pairs = {年: (部分, 全期)}；每个年份用更早年份的覆盖率预测它的全期（扩展窗口）。"""
    out = []
    for y in sorted(pairs):
        early = [pairs[t] for t in sorted(pairs) if t < y]
        if not early:
            continue
        try:
            pred = partial_period(pairs[y][0], early)["estimate"]
        except MethodError:
            continue
        out.append({"year": y, "pred": pred, "actual": pairs[y][1], "log_err": math.log(pred / pairs[y][1])})
    return out


# ---------- 合并与区间（v2.12，METHODS_ZH.md 4.1、4.2、5.4）----------
# 中心值：分块等权，不按回测误差加权。每个阈值是 [人为约定] 或写了依据：
# 1. 分块：两个方法的输入 id（观测点 + 假设）Jaccard >= JACCARD_BLOCK 就归为一块（并查集，可传递）[人为约定 0.5，4.1 第 3 步；
#    依据 Wang 等 2023：用同一批信息的预测合并没有好处]。consensus / 分析师估计和数据路线不共用 id，按这条规则自成一块。
# 2. 块内、跨块用同一条规则（ln 空间）：1 个 -> 它自己；2 个 -> 均值（几何平均）；>= 3 个 -> 中位数（偶数个取中间两个的均值）
#    [4.1 第 4b、6 步；依据 Stock & Watson 2004 表 8、SCUM 表 4：少数据时等权 / 中位数不比估计权重差]。
# 3. 不用回测误差加权：题库级闸门（>= 30 道打过分的题，回测较好的路线实际也较好的命中率 >= 0.7）没过，WEIGHT_GATE 关着；
#    打开时块按 1 / (块内回测平均 |ln 误差| + EPS) 加权（v2.11 的规则搬到块上），这条路径现在不会走 [4.1 第 8 步、闸门]。
# 区间（80%，ln 空间）：
# 4. 每个方法自己的宽度 sigma（_member_sigma）：series_auto 用校准表那一行（离线基准的经验分位，calibration.py），
#    和别的块放在一起时取它的对称等效宽度 (q90 - q10) / (2 z(0.9))；
#    formula_mc 用 Monte Carlo 的 P10 / P90（对数正态传播，决定 6），但不低于 FALLBACK_SIGMA（v2.11 同样不许 MC 把区间压窄：
#    观测点的宽度 DEFAULT_REL_U 是代码给的，没有校准）[人为约定]；有 >= MIN_FOLDS_T 个回测折的方法（yoy_scaling、ratio、
#    partial_period）用 t 修正的回测 RMSE：RMSE x t(n, 0.9) / z(0.9)，n = 折数 [METHODS_ZH 4.2 I1；>= 2 折是人为约定，同 v2.11]；
#    都没有就是 FALLBACK_SIGMA（no_basis，同 v2.11）。
# 5. 块的宽度 = 成员宽度的最大值，和块内方法分歧（成员 ln 值对块值的均方根）取大的 [人为约定：同块成员共用输入，误差不独立；
#    分歧只能放宽，同 v2.11]。
# 6. 只有 1 块：用这一块的宽度；这一块只有一个 series_auto 时直接用它的校准区间（不对称）。
#    >= 2 块：sigma = 各块宽度的均方根（不按块数的平方根收窄 [人为约定]：块只按共用 id 分开，同类来源、同一个裁判的假设这类
#    共同偏差没有建模；Fermi 类区间普遍偏窄，METHODS_ZH 5），再乘 Birge 比 R = sqrt(chi2 / (k - 1))（R > 1 时），
#    chi2 = sum(((块值 - 加权均值) / 块宽度)^2)，加权均值按 1 / 块宽度^2 加权（只用来检验各块彼此是否一致，中心仍按第 2 条）
#    [METHODS_ZH 5.4 F4，PDG 2019 5.2.2；N = 2-3 时检验功效低，所以 R > 1 就放宽，不等显著]。
#    以中心算 chi2 会让一个很窄的块和等权中心的距离把区间撑到离谱（编造的 6 万 / 7.5 万两块，R = 4），所以用加权均值。
#    块宽度不低于 EPS（1%），防止回测误差恰好为 0 时除以 0 [人为约定]。
# 7. 块值的 max - min > ln 2：标记「路线分歧超过 x2」，区间放宽到盖住每一块 [4.1 第 7 步，人为约定]；R > BIRGE_FLAG 只标记
#    （PDG 说这时可以不平均；中心规则按决定 5 不变）[人为约定，5.4]。
JACCARD_BLOCK = 0.5
MIN_FOLDS_T = 2
DISAGREE_X2 = math.log(2)
BIRGE_FLAG = 3.0
WEIGHT_GATE = {"passed": False, "min_questions": 30, "min_hit_rate": 0.7,
               "note": "off: inverse backtest-error weights need a bank-level gate (>= 30 scored questions with >= 2 "
                       "backtested routes, hit rate >= 0.7; METHODS_ZH 4.1), which has not been run"}
# t 分布的 0.9 分位（自由度 1-30，scipy.stats.t.ppf(0.9, df)，tests/test_combine.py 核对）；更大的自由度用 Cornish-Fisher 展开
T90 = (3.077684, 1.885618, 1.637744, 1.533206, 1.475884, 1.439756, 1.414924, 1.396815, 1.383029, 1.372184,
       1.363430, 1.356217, 1.350171, 1.345030, 1.340606, 1.336757, 1.333379, 1.330391, 1.327728, 1.325341,
       1.323188, 1.321237, 1.319460, 1.317836, 1.316345, 1.314972, 1.313703, 1.312527, 1.311434, 1.310415)


def t90(df: int) -> float:
    if df < 1:
        raise MethodError("t quantile needs at least 1 degree of freedom")
    if df <= len(T90):
        return T90[df - 1]
    z = Z90
    return z + (z ** 3 + z) / (4 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * df ** 2)


def _member_sigma(r: dict) -> tuple:
    """一个方法自己的 80% 宽度（ln 空间的 sigma）：(sigma, 来源, 细节)。规则见上面第 4 条。"""
    iv = (r.get("series_auto") or {}).get("interval")
    if iv:
        return ((iv["q90_ln"] - iv["q10_ln"]) / (2 * Z90), "series_calibration",
                {"calibration_row": iv.get("calibration_row"), "table": iv.get("table"), "q10_ln": iv["q10_ln"],
                 "q90_ln": iv["q90_ln"]})
    mc = r.get("mc") or {}
    if (mc.get("p10") or 0) > 0 and (mc.get("p90") or 0) > 0:
        s = (math.log(mc["p90"]) - math.log(mc["p10"])) / (2 * Z90)
        if s >= FALLBACK_SIGMA:
            return s, "monte_carlo", {"sigma_mc": s}
        return FALLBACK_SIGMA, "no_basis", {"sigma_mc": s, "note": "Monte Carlo width below the default, not used to narrow"}
    errs = [b["log_err"] for b in r.get("backtest") or []]
    if len(errs) >= MIN_FOLDS_T:
        rmse = math.sqrt(statistics.fmean(e * e for e in errs))
        t = t90(len(errs))
        return max(rmse * t / Z90, EPS), "backtest_t", {"n_folds": len(errs), "rmse_ln": rmse, "t90": t}
    return FALLBACK_SIGMA, "no_basis", {"n_folds": len(errs)}


def _inputs(r: dict) -> set:
    return set(r.get("used_ids") or []) | set(r.get("used_assumptions") or [])


def blocks_of(results: list) -> list:
    """按输入 id 的 Jaccard 分块（并查集）。返回块的列表，每块是 results 的下标列表，按第一个成员的下标排序。"""
    n = len(results)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    ins = [_inputs(r) for r in results]
    for i in range(n):
        for j in range(i + 1, n):
            u = ins[i] | ins[j]
            if u and len(ins[i] & ins[j]) / len(u) >= JACCARD_BLOCK:
                parent[find(j)] = find(i)
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    return sorted(groups.values(), key=lambda g: g[0])


def _centre(logs: list) -> tuple:
    """ln 值 -> (中心, 每个值的系数, 规则名)：1 个 -> 它自己；2 个 -> 均值；>= 3 个 -> 中位数（并列按下标）。"""
    n = len(logs)
    if n == 1:
        return logs[0], [1.0], "single"
    if n == 2:
        return (logs[0] + logs[1]) / 2, [0.5, 0.5], "geometric_mean"
    order = sorted(range(n), key=lambda i: (logs[i], i))
    coef = [0.0] * n
    mid = [order[n // 2]] if n % 2 else [order[n // 2 - 1], order[n // 2]]
    for i in mid:
        coef[i] = 1 / len(mid)
    return sum(coef[i] * logs[i] for i in range(n)), coef, "median"


def _weighted_blocks(bvals: list, bfolds: list) -> tuple:
    """WEIGHT_GATE 打开时才用（现在不会走）：块按 1 / (块内回测平均 |ln 误差| + EPS) 加权，没回测的块取有回测块权重的中位数。"""
    raw = {i: 1 / (statistics.fmean(abs(x) for x in f) + EPS) for i, f in enumerate(bfolds) if f}
    if not raw:
        return _centre(bvals)
    fill = statistics.median(raw.values())
    w = [raw.get(i, fill) for i in range(len(bvals))]
    w = [x / sum(w) for x in w]
    return sum(wi * v for wi, v in zip(w, bvals)), w, "inverse_backtest_error"


RULE_TEXT = {"single": "the only one", "geometric_mean": "geometric mean", "median": "median",
             "inverse_backtest_error": "weighted by inverse backtest error"}


def combine(results: list) -> dict:
    """results: compute.run 里算出了估计的方法（{id, method, estimate, used_ids, used_assumptions, backtest, mc, series_auto}）。
    id 必须互不相同（compute.run 统一编号 m1..mN）。规则见上面的注释（第 1-7 条）。
    weights：每个方法在 ln 中心里的系数（和为 1）；取中位数时不是中位的块系数为 0，但它参与了投票和区间。"""
    ok = [r for r in results if r.get("estimate") and r["estimate"] > 0]
    if not ok:
        return {"central": None, "p10": None, "p90": None, "weights": {}, "basis": "no_method"}
    ids = [str(r.get("id", "")) for r in ok]
    if len(set(ids)) != len(ids):
        raise MethodError(f"duplicate method ids {ids}")
    logs = [math.log(r["estimate"]) for r in ok]
    msig = [_member_sigma(r) for r in ok]
    blocks, coef = [], [0.0] * len(ok)
    for g in blocks_of(ok):
        c, cf, rule = _centre([logs[i] for i in g])
        spread = math.sqrt(statistics.fmean((logs[i] - c) ** 2 for i in g)) if len(g) >= 2 else 0.0
        top = max(g, key=lambda i: msig[i][0])
        sig, src = (spread, "method_spread") if spread > msig[top][0] else (msig[top][0], msig[top][1])
        shared = sorted(set.intersection(*[_inputs(ok[i]) for i in g])) if len(g) >= 2 else []
        blocks.append({"id": f"B{len(blocks) + 1}", "members": [ids[i] for i in g], "index": g, "log": c, "coef_in": cf,
                       "value": math.exp(c), "rule": rule, "sigma_ln": sig, "sigma_source": src, "spread_ln": spread,
                       "shared_inputs": shared, "folds": [b["log_err"] for i in g for b in ok[i].get("backtest") or []]})
    bvals = [b["log"] for b in blocks]
    if WEIGHT_GATE["passed"]:
        logc, bcoef, across = _weighted_blocks(bvals, [b["folds"] for b in blocks])
    else:
        logc, bcoef, across = _centre(bvals)
    for b, bc in zip(blocks, bcoef):
        b["coef"] = bc
        for i, ci in zip(b["index"], b["coef_in"]):
            coef[i] = bc * ci
    central = math.exp(logc)
    k = len(blocks)
    iv = {"n_blocks": k, "flags": []}
    if k == 1:
        b = blocks[0]
        sigma, basis = b["sigma_ln"], b["sigma_source"]
        sa = (ok[b["index"][0]].get("series_auto") or {}).get("interval") if len(b["index"]) == 1 else None
        if sa and basis == "series_calibration":   # 只有一个 series_auto：直接用它的校准区间（不对称）
            p10, p90 = central * math.exp(sa["q10_ln"]), central * math.exp(sa["q90_ln"])
            iv["rule"] = "the only route is series_auto, so the interval is its calibration row"
        else:
            p10, p90 = central * math.exp(-Z90 * sigma), central * math.exp(Z90 * sigma)
            iv["rule"] = "one block, so the interval is that block's own width"
    else:
        rms = math.sqrt(statistics.fmean(b["sigma_ln"] ** 2 for b in blocks))
        sb = [max(b["sigma_ln"], EPS) for b in blocks]
        mu_w = sum(b["log"] / s ** 2 for b, s in zip(blocks, sb)) / sum(1 / s ** 2 for s in sb)
        chi2 = sum(((b["log"] - mu_w) / s) ** 2 for b, s in zip(blocks, sb))
        birge = math.sqrt(chi2 / (k - 1))
        scale = max(1.0, birge)
        sigma = rms * scale
        basis = "blocks_disagree" if birge > 1 else "blocks"
        p10, p90 = central * math.exp(-Z90 * sigma), central * math.exp(Z90 * sigma)
        iv.update(rule="several blocks: root mean square of the block widths, times the Birge ratio when it exceeds 1",
                  sigma_blocks_rms=rms, chi2=chi2, dof=k - 1, birge_ratio=birge, scale=scale,
                  chi2_weighted_mean=math.exp(mu_w))
        lo, hi = min(b["value"] for b in blocks), max(b["value"] for b in blocks)
        if math.log(hi / lo) > DISAGREE_X2:
            iv["flags"].append("blocks_disagree_x2")
            if p10 > lo or p90 < hi:
                iv["widened_to_cover_blocks"] = {"p10_before": p10, "p90_before": p90}
                p10, p90 = min(p10, lo), max(p90, hi)
        if birge > BIRGE_FLAG:
            iv["flags"].append("birge_ratio_above_3")
    iv["sigma_ln"] = sigma
    out_blocks = [{key: b[key] for key in ("id", "members", "value", "rule", "coef", "sigma_ln", "sigma_source", "spread_ln",
                                           "shared_inputs")} for b in blocks]
    wb = {}
    for b in blocks:
        for i in b["index"]:
            inside = "" if len(b["index"]) == 1 else f", {RULE_TEXT[b['rule']]} of {len(b['index'])} methods sharing inputs"
            if k == 1:
                wb[ids[i]] = f"{b['id']} (only block{inside})"
            elif across == "median":
                wb[ids[i]] = f"{b['id']} of {k} blocks{inside}; median of blocks: " + \
                             ("this block is the median" if b["coef"] > 0 else "not the median (one vote, counts in the interval)")
            else:
                wb[ids[i]] = f"{b['id']} of {k} blocks{inside}; {RULE_TEXT[across]} of blocks"
    n_folds = sum(len(r.get("backtest") or []) for r in ok)
    return {"central": central, "p10": p10, "p90": p90, "sigma_ln": sigma, "basis": basis,
            "weights": dict(zip(ids, coef)),
            "weight_rule": "single_block" if k == 1 else f"{'blocks' if WEIGHT_GATE['passed'] else 'equal_blocks'}_{across}",
            "weight_basis": wb, "n_backtest_folds": n_folds,
            "combination": {"n_blocks": k, "rule_across_blocks": across, "jaccard_threshold": JACCARD_BLOCK,
                            "blocks": out_blocks, "weight_gate": WEIGHT_GATE["note"]},
            "member_sigma": {ids[i]: {"sigma_ln": s, "source": src, **det} for i, (s, src, det) in enumerate(msig)},
            "interval": iv}

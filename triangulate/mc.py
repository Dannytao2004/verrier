"""Monte Carlo：输入按 lognormal 采样，路径分布，跨路径聚合。全部纯 Python 标准库，固定种子。

约定（预注册于 PROBE_PLAN.md）：
- low / high 视为 P10 / P90；中位数 = sqrt(low * high)；low == high 时退化为常数。
- 路径中心 = 样本中位数；聚合中心 = 有效路径中位数在 log 空间的中位数。
- 80% 区间 = 有效路径等权混合样本的 P10 / P90。
- 路径中位数与中心相差 > 1 个数量级 -> outlier。
"""
import math
import random
import statistics

Z90 = 1.2815515655446004  # 标准正态的 0.9 分位数
OUTLIER_OOM = 1.0


def lognormal_params(low: float, high: float):
    if not (0 < low <= high) or not (math.isfinite(low) and math.isfinite(high)):
        raise ValueError(f"need 0 < low <= high, got low={low}, high={high}")
    mu = (math.log(low) + math.log(high)) / 2
    sigma = (math.log(high) - math.log(low)) / (2 * Z90)
    return mu, sigma


def lognormal_median(low: float, high: float) -> float:
    return math.sqrt(low * high)


def sample_lognormal(low: float, high: float, n: int, rng: random.Random) -> list:
    mu, sigma = lognormal_params(low, high)
    if sigma == 0:
        return [float(low)] * n  # 题目给定的数原样使用，避免 exp(log(x)) 的浮点误差
    return [math.exp(mu + sigma * rng.gauss(0.0, 1.0)) for _ in range(n)]


def sample_inputs(ranges: dict, n: int, seed) -> dict:
    """ranges: name -> (low, high)。按名字排序后依次采样，保证同种子同结果、与 dict 顺序无关。"""
    rng = random.Random(seed)
    return {name: sample_lognormal(lo, hi, n, rng) for name, (lo, hi) in sorted(ranges.items())}


def quantile(sorted_vals: list, q: float) -> float:
    """线性插值分位数（与 numpy 默认 'linear' 一致）。"""
    if not sorted_vals:
        return math.nan
    pos = (len(sorted_vals) - 1) * q
    lo = math.floor(pos)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (pos - lo)


def summarise(values: list) -> dict:
    """单条路径的分布摘要；非有限值剔除并计数。"""
    finite = sorted(v for v in values if math.isfinite(v))
    out = {"n": len(values), "n_nonfinite": len(values) - len(finite),
           "n_nonpositive": sum(1 for v in finite if v <= 0)}
    if not finite:
        out.update(median=math.nan, p10=math.nan, p90=math.nan)
        return out
    out.update(median=quantile(finite, 0.5), p10=quantile(finite, 0.1), p90=quantile(finite, 0.9))
    return out


def log_median(values: list) -> float:
    """正数在 log10 空间取中位数再还原；偶数个时即中间两个的几何平均。"""
    logs = [math.log10(v) for v in values]
    return 10 ** statistics.median(logs)


def aggregate(path_samples: dict) -> dict:
    """path_samples: path_id -> 样本列表（已在目标单位）。只传有效路径。"""
    summaries = {pid: summarise(v) for pid, v in path_samples.items()}
    usable = {pid: s for pid, s in summaries.items() if math.isfinite(s["median"]) and s["median"] > 0}
    if not usable:
        return {"central": None, "p10": None, "p90": None, "paths": summaries, "used": [], "outliers": []}
    central = log_median([s["median"] for s in usable.values()])
    pooled = sorted(v for pid in usable for v in path_samples[pid] if math.isfinite(v))
    outliers = [pid for pid, s in usable.items() if abs(math.log10(s["median"] / central)) > OUTLIER_OOM]
    for pid, s in usable.items():
        s["log10_vs_central"] = math.log10(s["median"] / central)
    return {"central": central, "p10": quantile(pooled, 0.1), "p90": quantile(pooled, 0.9),
            "paths": summaries, "used": sorted(usable), "outliers": sorted(outliers)}

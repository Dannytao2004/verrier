"""全局 LightGBM（series_auto 的成员之一）：特征、模型加载、预测。不调模型、不联网。

模型 = 离线基准（bench/forecasters_ml.py，配置键 BENCH_CFG_KEY）的 lgbm，由 models/train_lgbm.py 重训（同数据、同参数、
deterministic），三个分位模型（0.1 / 0.5 / 0.9）的文本用 xz 压缩后放在 models/。训练窗口：L 在 13..40 均匀、15% 的窗口挖
1-3 个中间月、h = 1..4（h 是特征），所以只对 h <= HMAX 有意义。特征和训练脚本共用本文件，训练和推理不会各写一套。
point = 0.5 分位（agent 只用它；区间来自 calibration.py 的基准误差分位，不用这里的 0.1 / 0.9）。
月份序号 t = 年 * 12 + 月 - 1（t % 12 == 0 是一月），和基准一致。
"""
import json
import lzma
import threading
import warnings
import zlib
from pathlib import Path

import numpy as np

MODELS = Path(__file__).resolve().parent / "models"
META = MODELS / "lgbm_meta.json"
SEASON = 12
K = 40                     # 特征回看的月数
HMAX = 4                   # 训练用的最大 h
QS = (0.1, 0.5, 0.9)
SEED = 2026
# 训练配置：和基准 bench/forecasters_ml.py 的 TRAIN_CFG / LGB_CFG 逐项相同（改了就不是同一个模型，配置键会变）
TRAIN_CFG = dict(n_train=20000, per=6, lmin=13, lmax=K, p_gap=0.15, val_frac=0.1, seed=SEED, dedup="v2")
LGB_CFG = dict(learning_rate=0.05, num_leaves=63, min_data_in_leaf=200, feature_fraction=0.8, bagging_fraction=0.8,
               bagging_freq=1, lambda_l2=1.0, rounds=3000, early_stop=100)
BENCH_CFG_KEY = "d12f86e0"   # 基准里这个模型的配置键（它的键还含 N-BEATS 的配置，所以和 cfg_key() 不同）

FEAT = ([f"z{k}" for k in range(K)] + ["h", "tmon", "nobs", "span", "sm1", "sm2", "sm3", "g1", "g3", "g12", "gsd",
                                       "yoy3f", "yoy12f", "d1", "dsd", "ma3"])
CAT = [FEAT.index("tmon")]


def cfg_key() -> str:
    """agent 这份模型的配置键：训练配置 + 特征名 + 回看长度。"""
    return f"{zlib.crc32(repr((TRAIN_CFG, LGB_CFG, FEAT, K)).encode()):08x}"


def model_paths() -> dict:
    return {q: MODELS / f"lgbm_q{int(q * 100):02d}.txt.xz" for q in QS}


# ---------- 特征（照抄基准，逐字节同一算法） ----------
def grids(hists):
    """每条历史变成最近 K 个月的 ln 值（第 0 列 = 最后一个已知月），没观测到的月是 NaN。"""
    n = len(hists)
    X = np.full((n, K), np.nan)
    T, span = np.empty(n, int), np.empty(n, int)
    for i, (y, t) in enumerate(hists):
        y, t = np.asarray(y, float), np.asarray(t, int)
        off = t[-1] - t
        m = (off < K) & (y > 0)
        X[i, off[m]] = np.log(y[m])
        T[i], span[i] = t[-1], t[-1] - t[0] + 1
    return X, T, span


def _nan(f, a):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return f(a, axis=1)


def features(X, T, span, hs):
    """返回 (行按 (case, h) 排的特征矩阵, 每个 case 的水平 lvl)；目标 = ln y_{T+h} - lvl。"""
    lvl = _nan(np.nanmean, X[:, :12])
    Z = X - lvl[:, None]
    yo = X[:, :K - 12] - X[:, 12:]          # 同比 ln 差，第 k 列 = 第 k 个月 vs 一年前
    g1, g3, g12, gsd = yo[:, 0], _nan(np.nanmean, yo[:, :3]), _nan(np.nanmean, yo[:, :12]), _nan(np.nanstd, yo[:, :12])
    d = Z[:, :12] - Z[:, 1:13]
    d1, dsd, ma3 = d[:, 0], _nan(np.nanstd, d), _nan(np.nanmean, Z[:, :3])
    nobs = (~np.isnan(X)).sum(1)
    per_h = []
    for h in hs:
        sm1, sm2, sm3 = Z[:, 12 - h], Z[:, 24 - h], Z[:, 36 - h]
        per_h.append(np.column_stack([Z, np.full(len(X), h), (T + h) % SEASON, nobs, span, sm1, sm2, sm3, g1, g3, g12,
                                      gsd, sm1 + g3, sm1 + g12, d1, dsd, ma3]))
    return np.stack(per_h, axis=1).reshape(len(X) * len(hs), len(FEAT)), lvl


# ---------- 模型 ----------
_BOOSTERS = {}
_LOCK = threading.Lock()


def boosters() -> dict:
    """三个分位模型（第一次用时从 xz 解压加载，之后缓存在进程里）。
    v2.12d（审查）：网页一个进程同时跑 2 个运行，以前缓存逐个分位填、后到的线程会看到只装了一半的缓存（KeyError 0.5，
    series_auto 安静地退到 yoy 路径）。现在加锁，三个都装好了才一次放进缓存。"""
    if len(_BOOSTERS) == len(QS):
        return _BOOSTERS
    with _LOCK:
        if len(_BOOSTERS) != len(QS):
            import lightgbm as lgb
            loaded = {}
            for q, p in model_paths().items():
                if not p.exists():
                    raise FileNotFoundError(f"LightGBM model file missing: {p.name} (run triangulate/agent/models/train_lgbm.py)")
                loaded[q] = lgb.Booster(model_str=lzma.decompress(p.read_bytes()).decode("utf-8"))
            _BOOSTERS.clear()
            _BOOSTERS.update(loaded)
    return _BOOSTERS


def meta() -> dict:
    return json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}


def text_sha256(q: float) -> str:
    """一个分位模型解压后文本的 sha256（训练时记在 lgbm_meta.json；tests/test_series_auto.py 核对文件和它对得上）。"""
    return str((((meta().get("train_log") or {}).get(f"q{q}") or {}).get("text_sha256")) or "")


def predict_batch(hists, hs, threads: int = 1):
    """一批历史 [(y, t)] -> (point, p10, p90)，形状 (N, len(hs))。分位交叉时按大小重排（同基准）。"""
    hs = [int(h) for h in hs]
    if any(h < 1 or h > HMAX for h in hs):
        raise ValueError(f"LightGBM was trained for h = 1..{HMAX}, got {hs}")
    bs = boosters()
    X, T, span = grids(hists)
    F, lvl = features(X, T, span, hs)
    q = np.sort(np.stack([bs[q].predict(F, num_threads=threads).reshape(len(hists), len(hs)) for q in QS]), axis=0)
    return tuple(np.exp(lvl[:, None] + q[i]) for i in (1, 0, 2))


def predict_one(y, t, h: int) -> float:
    """一条历史、一个 h 的点估计（0.5 分位）。"""
    pt, _, _ = predict_batch([(np.asarray(y, float), np.asarray(t, int))], [h])
    return float(pt[0, 0])

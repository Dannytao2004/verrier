"""重训 series_auto 用的全局 LightGBM（由 bench/forecasters_ml.py 的 train_windows / train_lgbm 改写，算法逐行相同）。
不调任何 LLM、不联网。

训练数据：M4 月度的官方训练段（Monthly-train.csv，不含每条序列最后 18 个月的测试段）+ M4-info.csv（起始月份），
从 https://github.com/Mcompetitions/M4-methods 的 Dataset/ 下载（bench/fetch_data.py；本仓库不带数据，sha256 记在 lgbm_meta.json）。
剔除：离线基准抽中的 1,400 条 M4 序列（基准评测用，一个点都不进训练），以及和任何基准序列共享一段 24 个月走势的拷贝
（基准审计的去重 v2，394 条）。两份名单在 lgbm_exclude.json（--exclude-from-bench 从 bench 的缓存重建）。
窗口：随机取 20,000 条，每条 6 个窗口，L 在 13..40 均匀，15% 的窗口挖 1-3 个中间月，目标 h = 1..4；10% 的序列留作早停验证。
模型：三个分位回归（alpha 0.1 / 0.5 / 0.9），deterministic、force_row_wise、种子 2026；按早停的最佳轮数存成文本，再 xz 压缩
（三个文本约 23.6 MB，压缩后约 6.9 MB；压缩无损，预测逐位不变）。

用法（在仓库根目录）：
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe -m triangulate.agent.models.train_lgbm --m4 bench/data/m4
  --exclude-from-bench bench   先从 bench 的抽样缓存和去重缓存重写 lgbm_exclude.json
  --compare-dir bench/data/_cache/ml   训练完和基准存的模型文本逐字节比较（lgbm_<键>_qNN.txt）
"""
import argparse
import hashlib
import json
import lzma
import os
import sys
import time
from pathlib import Path

import numpy as np

from .. import lgbm_global as LG

HERE = Path(__file__).resolve().parent
EXCLUDE = HERE / "lgbm_exclude.json"


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def m4_start(d: str) -> int:
    """M4-info 的 StartingDate 有两种写法：'31-01-90 12:00'（日-月-两位年）和 '1879-03-01 12:00:00'（同 bench/harness.py）。"""
    if d[4] == "-":
        return int(d[:4]) * 12 + int(d[5:7]) - 1
    yy = int(d[6:8])
    return (1900 + yy if yy > 30 else 2000 + yy) * 12 + int(d[3:5]) - 1


def exclude_from_bench(bench: Path) -> dict:
    """从 bench 的缓存重建剔除名单：抽样（bench/harness.sample_series 的缓存）里的 M4 序列 + 去重 v2 的 pool_drop。"""
    sys.path.insert(0, str(bench))
    import harness as H   # noqa: E402  只读 bench/data/_cache 的抽样缓存
    picked, _ = H.sample_series()
    ov = json.loads((bench / "data" / "_cache" / "ml" / "overlap_w24_v2.json").read_text(encoding="utf-8"))
    return {"benchmark_m4_sample": sorted(s["sid"] for s in picked if s["dataset"] == "M4"),
            "duplicates_pool_drop": sorted(ov["pool_drop"]),
            "source": "bench/harness.py sample_series (seed 2026) and bench/data/_cache/ml/overlap_w24_v2.json "
                      "(forecasters_ml.overlap, dedup v2: 24-month segments, grids 1e-4 / 1e-3 / 1e-2, verified)"}


def train_windows(m4: Path, excl: set):
    import pandas as pd
    info = pd.read_csv(m4 / "M4-info.csv")
    info = info[info.SP == "Monthly"].set_index("M4id")
    tr = pd.read_csv(m4 / "Monthly-train.csv", index_col=0)
    A = tr.to_numpy(float)
    c = LG.TRAIN_CFG
    pool = []
    for k, sid in enumerate(tr.index):
        if sid in excl:
            continue
        y = A[k][~np.isnan(A[k])]
        if len(y) >= c["lmin"] + LG.HMAX and y.min() > 0:
            pool.append((sid, y, m4_start(info.at[sid, "StartingDate"])))
    rng = np.random.default_rng([c["seed"], 7])
    chosen = [pool[i] for i in sorted(rng.choice(len(pool), size=min(c["n_train"], len(pool)), replace=False))]
    hists, tgt, grp = [], [], []
    for g, (sid, y, t0) in enumerate(chosen):
        n = len(y)
        for _ in range(c["per"]):
            L = int(rng.integers(c["lmin"], min(c["lmax"], n - LG.HMAX) + 1))
            T = int(rng.integers(L - 1, n - LG.HMAX))          # 最后一个已知月的下标；T + 4 <= n - 1
            yy, tt = y[T - L + 1:T + 1], t0 + np.arange(T - L + 1, T + 1)
            if rng.random() < c["p_gap"] and L > 6:
                drop = rng.choice(np.arange(1, L - 1), size=int(rng.integers(1, 4)), replace=False)
                keep = np.ones(L, bool)
                keep[drop] = False
                yy, tt = yy[keep], tt[keep]
            hists.append((yy, tt))
            tgt.append(y[T + 1:T + 1 + LG.HMAX])
            grp.append(g)
    grp = np.array(grp)
    val = np.isin(grp, rng.choice(len(chosen), size=int(len(chosen) * c["val_frac"]), replace=False))
    info_out = dict(pool=len(pool), excluded=len(excl), series=len(chosen), windows=len(hists), val_windows=int(val.sum()))
    return hists, np.array(tgt), val, info_out


def train(m4: Path, threads: int, out: Path) -> dict:
    import lightgbm as lgb
    ex = json.loads(EXCLUDE.read_text(encoding="utf-8"))
    excl = set(ex["benchmark_m4_sample"]) | set(ex["duplicates_pool_drop"])
    hists, tgt, val, inf = train_windows(m4, excl)
    X, T, span = LG.grids(hists)
    F, lvl = LG.features(X, T, span, range(1, LG.HMAX + 1))
    u = (np.log(tgt) - lvl[:, None]).reshape(-1)
    v = np.repeat(val, LG.HMAX)
    ok = np.isfinite(u)
    log = dict(inf, rows=int(ok.sum()))
    texts = {}
    for q, path in LG.model_paths().items():
        t0 = time.perf_counter()
        c = LG.LGB_CFG
        p = dict(objective="quantile", alpha=q, learning_rate=c["learning_rate"], num_leaves=c["num_leaves"],
                 min_data_in_leaf=c["min_data_in_leaf"], feature_fraction=c["feature_fraction"],
                 bagging_fraction=c["bagging_fraction"], bagging_freq=c["bagging_freq"], lambda_l2=c["lambda_l2"],
                 num_threads=threads, seed=LG.SEED, deterministic=True, force_row_wise=True, verbose=-1)
        dtr = lgb.Dataset(F[ok & ~v], u[ok & ~v], feature_name=LG.FEAT, categorical_feature=LG.CAT, free_raw_data=False)
        dva = lgb.Dataset(F[ok & v], u[ok & v], reference=dtr)
        b = lgb.train(p, dtr, num_boost_round=c["rounds"], valid_sets=[dva],
                      callbacks=[lgb.early_stopping(c["early_stop"], verbose=False)])
        txt = b.model_to_string(num_iteration=b.best_iteration)
        texts[q] = txt
        (out / path.name).write_bytes(lzma.compress(txt.encode("utf-8"), preset=9 | lzma.PRESET_EXTREME))
        log[f"q{q}"] = dict(best_iter=b.best_iteration, val_loss=b.best_score["valid_0"]["quantile"],
                            sec=round(time.perf_counter() - t0, 1), text_bytes=len(txt.encode("utf-8")),
                            text_sha256=hashlib.sha256(txt.encode("utf-8")).hexdigest(),
                            xz_bytes=(out / path.name).stat().st_size)
    return log, texts


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--m4", required=True, help="目录，含 Monthly-train.csv 和 M4-info.csv")
    ap.add_argument("--threads", type=int, default=max(1, (os.cpu_count() or 2) - 4))
    ap.add_argument("--exclude-from-bench", default="", help="bench 目录：先重写 lgbm_exclude.json")
    ap.add_argument("--compare-dir", default="", help="和这个目录里基准存的 lgbm_<键>_qNN.txt 逐字节比较")
    a = ap.parse_args(argv)
    import lightgbm as lgb
    m4 = Path(a.m4)
    if a.exclude_from_bench:
        EXCLUDE.write_text(json.dumps(exclude_from_bench(Path(a.exclude_from_bench)), indent=1), encoding="utf-8",
                           newline="\n")
    t0 = time.perf_counter()
    log, texts = train(m4, a.threads, HERE)
    ex = json.loads(EXCLUDE.read_text(encoding="utf-8"))
    meta = {
        "cfg_key": LG.cfg_key(), "bench_cfg_key": LG.BENCH_CFG_KEY, "train_cfg": LG.TRAIN_CFG, "lgb_cfg": LG.LGB_CFG,
        "features": LG.FEAT, "lookback": LG.K, "hmax": LG.HMAX, "quantiles": list(LG.QS), "lightgbm": lgb.__version__,
        "numpy": np.__version__, "threads": a.threads, "wall_sec": round(time.perf_counter() - t0, 1),
        "training_data": {
            "source": "M4 monthly, official training segment only (https://github.com/Mcompetitions/M4-methods, Dataset/)",
            "Monthly-train.csv_sha256": sha256(m4 / "Monthly-train.csv"), "M4-info.csv_sha256": sha256(m4 / "M4-info.csv"),
            "excluded_benchmark_series": len(ex["benchmark_m4_sample"]), "excluded_duplicates": len(ex["duplicates_pool_drop"]),
            "exclude_file_sha256": sha256(EXCLUDE), "exclude_source": ex["source"]},
        "train_log": log,
        "licence_note": "LightGBM is MIT. Redistribution terms of the M4 data were not verified (BENCH_ZH.md 4.1).",
    }
    if a.compare_dir:
        cmp = {}
        for q, txt in texts.items():
            # 基准用 Booster.save_model 存文件：Windows 上末尾 pandas_categorical 两行是 CRLF，树是 LF；比较前统一成 LF
            ref = Path(a.compare_dir) / f"lgbm_{LG.BENCH_CFG_KEY}_q{int(q * 100):02d}.txt"
            same = ref.exists() and ref.read_bytes().replace(b"\r\n", b"\n") == txt.encode("utf-8")
            cmp[f"q{int(q * 100):02d}"] = "identical (CRLF normalised)" if same else "missing" if not ref.exists() else "differs"
        meta["compare_with_bench_model_text"] = cmp
    (HERE / "lgbm_meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8", newline="\n")
    print(json.dumps({k: meta[k] for k in ("cfg_key", "wall_sec", "train_log")} |
                     {"compare": meta.get("compare_with_bench_model_text")}, indent=1))


if __name__ == "__main__":
    main()

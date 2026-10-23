"""生成 triangulate/agent/calibration.py（series_auto 的 80% 区间校准表）。不调任何 LLM、不联网，只读离线基准的输出。

输入（都在 bench/，本仓库不提交它们，sha256 写进生成的表）：
- bench/out/classic_results.csv（ets、theta、yoy1、yoy3 列）和 bench/out/ml_results.csv（lgbm 列，配置键见 ml_meta.json）；
- bench/harness.py 的抽样缓存（2,000 条序列，种子 2026）和 make_tasks 的原点：yoy 的 1 / 2 / 3 个同比对由本仓库的
  series.yoy 在这些原点上重算（基准只存了 yoy1、yoy3 两列；重算的 1 对、3 对和这两列逐 case 对得上才写表）。
行：
- comb_ETYL_mean|L{13,24,36}|h{1..4}：点 = ets、theta、yoy3、lgbm 四列的算术平均（基准 leaderboard.py 的 comb_ETYL_mean）；
  有成员不是正数的 case 不算（agent 在那种情况下退到 yoy 路径），去掉的个数记在 SOURCE；
- yoy|pairs{1,2,3}|h{1..4}：去年同月 x 最近 n 个同比对的增长。
每行：e = ln(真值 / 点) 的 10% / 50% / 90% 分位（numpy 默认线性插值；每格约 6,000 个 case）、case 数、
在同一批 case 上的 80% 覆盖率（合并与按数据集分开；合并的覆盖率按构造约为 0.80，按数据集分开的才说明问题）。
--verify N：另抽 N 条基准序列，用 series._members（agent 的 AutoETS / Theta / yoy3 / LightGBM 调用）重算基准的 case，
和 CSV 比最大相对差；再用 agent 的 LightGBM 跑全部 18,000 个历史，和基准 lgbm 列比平均 ale。结果写进表的 VERIFY。

v2.12d（审查：表在提交的仓库里查不了）：bench/ 不提交（它的输出 bench/out 和数据 bench/data 留在本机，数据的再分发条款
未核实），所以另提交每个 case 的 ln 误差 CASES（models/calibration_cases.csv.xz：行名、数据集、e；只有误差，没有序列的值）。
--dump-cases 从 bench 重算这些误差，先确认算出的行和 calibration.py 逐位相同再写文件（不改 calibration.py）；
--check-cases 不需要 bench：从 CASES 重算每一行和 TABLE_ID，和 calibration.py 比（tests/test_series_auto.py 同样核对）。

用法（仓库根目录）：
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe -m triangulate.agent.models.build_calibration --bench bench --verify 60
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe -m triangulate.agent.models.build_calibration --bench bench --dump-cases
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe -m triangulate.agent.models.build_calibration --check-cases
"""
import argparse
import hashlib
import io
import json
import lzma
import math
import sys
import time
import zlib
from pathlib import Path

import numpy as np

from .. import lgbm_global as LG
from .. import series as S

OUT = Path(__file__).resolve().parent.parent / "calibration.py"
CASES = Path(__file__).resolve().parent / "calibration_cases.csv.xz"
HS = (1, 2, 3, 4)
LS = (13, 24, 36)
DATASETS = ("M4", "M3", "Tourism")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _stats(e: np.ndarray, ds: np.ndarray) -> dict:
    q10, q50, q90 = (float(x) for x in np.quantile(e, [0.1, 0.5, 0.9]))
    cov = lambda m: float(np.mean((e[m] >= q10) & (e[m] <= q90)))
    r = {"q10": round(q10, 6), "q50": round(q50, 6), "q90": round(q90, 6), "n": int(len(e)),
         "cov80": round(cov(np.ones(len(e), bool)), 4)}
    for d in ("M4", "M3", "Tourism"):
        r[f"cov80_{d}"] = round(cov(ds == d), 4)
    return r


def _bench(bench: Path):
    sys.path.insert(0, str(bench))
    import harness as H   # noqa: E402  只读 bench 的抽样缓存
    picked, _ = H.sample_series()
    return H, picked, H.make_tasks(picked, gaps=0)


def etyl_rows(bench: Path):
    import pandas as pd
    c = pd.read_csv(bench / "out" / "classic_results.csv", usecols=["case_id", "dataset", "L", "h", "actual", "ets", "theta",
                                                                      "yoy1", "yoy3", "fallbacks"])
    m = pd.read_csv(bench / "out" / "ml_results.csv", usecols=["case_id", "actual", "lgbm", "fallbacks"])
    d = c.merge(m, on="case_id", suffixes=("", "_ml"))
    assert len(d) == len(c) == len(m) == 72000, (len(c), len(m), len(d))
    assert np.allclose(d.actual, d.actual_ml, rtol=1e-6)
    for col, fb in (("ets", "fallbacks"), ("theta", "fallbacks"), ("yoy3", "fallbacks"), ("lgbm", "fallbacks_ml")):
        assert not d[fb].fillna("").str.split(";").apply(lambda x: col in x).any(), f"{col} has fallbacks"
    mem = d[["ets", "theta", "yoy3", "lgbm"]]
    # 有成员不是正数的 case（基准里 ETS 9 个、Theta 18 个）agent 不走模型路径（series._members 报错、退到 yoy），不进这几行
    pos = (mem > 0).all(axis=1).to_numpy()
    pt = mem.mean(axis=1).to_numpy()
    e = np.log(d.actual.to_numpy()[pos] / pt[pos])
    rows, cases = {}, {}
    for L in LS:
        for h in HS:
            k = ((d.L == L) & (d.h == h)).to_numpy()[pos]
            key = f"comb_ETYL_mean|L{L}|h{h}"
            cases[key] = (e[k], d.dataset.to_numpy()[pos][k])
            rows[key] = _stats(*cases[key])
    return rows, d, int((~pos).sum()), cases


def yoy_rows(bench: Path, d):
    """在基准原点上重算 yoy（1 / 2 / 3 对），和 CSV 的 yoy1、yoy3 逐 case 核对。"""
    H, picked, tasks = _bench(bench)
    ref1 = dict(zip(d.case_id, d.yoy1))
    ref3 = dict(zip(d.case_id, d.yoy3))
    err = {n: {h: [] for h in HS} for n in (1, 2, 3)}
    dss = {n: {h: [] for h in HS} for n in (1, 2, 3)}
    worst = {1: 0.0, 3: 0.0}
    for k, jobs in tasks:
        s = picked[k]
        for T in sorted({T for T, _, _ in jobs}):
            t = s["t"][T - 35:T + 1]
            months = {int(a): float(b) for a, b in zip(t, s["y"][T - 35:T + 1])}
            last = int(t[-1])
            for h in HS:
                actual = float(s["y"][T + h])
                for n in (1, 2, 3):
                    p = S.yoy(months, last + h, last, w=n)["estimate"]
                    err[n][h].append(math.log(actual / p))
                    dss[n][h].append(s["dataset"])
                    if n in (1, 3):   # yoy1 在任何 L 都一样；yoy3 在 L24 / L36 一样（都有 >= 3 对）
                        ref = (ref1 if n == 1 else ref3)[f"{s['sid']}|T{T}|L36|h{h}"]
                        worst[n] = max(worst[n], abs(p / ref - 1))
    assert worst[1] < 1e-5 and worst[3] < 1e-5, worst   # CSV 只存 6 位有效数字
    cases = {f"yoy|pairs{n}|h{h}": (np.array(err[n][h]), np.array(dss[n][h])) for n in (1, 2, 3) for h in HS}
    rows = {k: _stats(*v) for k, v in cases.items()}
    return rows, {"max_rel_diff_yoy1_vs_csv": worst[1], "max_rel_diff_yoy3_vs_csv": worst[3]}, cases


def table_id(rows: dict, ml_cfg_key: str) -> str:
    return f"bench-{ml_cfg_key}-{zlib.crc32(json.dumps(rows, sort_keys=True).encode()):08x}"


def dump_cases(cases: dict, path: Path = CASES):
    """每个 case 的 ln 误差：行名下标、数据集下标、e（repr，17 位有效数字，重算分位时逐位相同）。xz 压缩。"""
    keys = sorted(cases)
    buf = io.StringIO()
    buf.write("# rows: " + json.dumps(keys) + "\n# datasets: " + json.dumps(DATASETS) + "\nrow,dataset,e\n")
    for i, k in enumerate(keys):
        e, ds = cases[k]
        for x, d in zip(e, ds):
            buf.write(f"{i},{DATASETS.index(str(d))},{float(x)!r}\n")
    path.write_bytes(lzma.compress(buf.getvalue().encode("utf-8"), preset=9 | lzma.PRESET_EXTREME))


def rows_from_cases(path: Path = CASES) -> dict:
    """不需要 bench：从 CASES 重算校准表的每一行（同 _stats）。"""
    lines = lzma.decompress(path.read_bytes()).decode("utf-8").splitlines()
    keys = json.loads(lines[0][len("# rows: "):])
    dsn = json.loads(lines[1][len("# datasets: "):])
    assert lines[2] == "row,dataset,e", lines[2]
    e = {i: [] for i in range(len(keys))}
    ds = {i: [] for i in range(len(keys))}
    for ln in lines[3:]:
        r, d, x = ln.split(",")
        e[int(r)].append(float(x))
        ds[int(r)].append(dsn[int(d)])
    return {k: _stats(np.array(e[i]), np.array(ds[i])) for i, k in enumerate(keys)}


def check_cases(path: Path = CASES) -> dict:
    """CASES 重算的行和 TABLE_ID 是否和 calibration.py 相同。返回 {"rows_equal", "table_id_equal", "table_id", "n_cases"}。"""
    from .. import calibration as CAL
    rows = rows_from_cases(path)
    tid = table_id(rows, CAL.SOURCE["ml_cfg_key"])
    return {"rows_equal": rows == CAL.ROWS, "table_id_equal": tid == CAL.TABLE_ID, "table_id": tid,
            "n_cases": sum(r["n"] for r in rows.values()), "bad_rows": sorted(k for k in set(rows) | set(CAL.ROWS)
                                                                          if rows.get(k) != CAL.ROWS.get(k))}


def verify(bench: Path, d, n_series: int) -> dict:
    """agent 的成员调用重算基准 case（抽 n_series 条序列），以及 agent 的 LightGBM 跑全部基准历史。"""
    H, picked, tasks = _bench(bench)
    ref = d.set_index("case_id")
    rng = np.random.default_rng([2026, 99])
    pick = sorted(rng.choice(len(tasks), size=min(n_series, len(tasks)), replace=False).tolist())
    worst = {k: 0.0 for k in ("AutoETS", "Theta", "yoy3", "LightGBM")}
    col = {"AutoETS": "ets", "Theta": "theta", "yoy3": "yoy3", "LightGBM": "lgbm"}
    n_fit = 0
    t0 = time.perf_counter()
    for j in pick:
        k, jobs = tasks[j]
        s = picked[k]
        for T, L, _ in jobs:
            t = [int(x) for x in s["t"][T - L + 1:T + 1]]
            wm = dict(zip(t, (float(v) for v in s["y"][T - L + 1:T + 1])))
            for h in HS:
                mem, _ = S._members(wm, t, t[-1] + h, t[-1], h)
                r = ref.loc[f"{s['sid']}|T{T}|L{L}|h{h}"]
                for name, v in mem.items():
                    worst[name] = max(worst[name], abs(v / r[col[name]] - 1))
            n_fit += 1
    sec = time.perf_counter() - t0
    hists, acts, keys = [], [], []
    for k, jobs in tasks:
        s = picked[k]
        for T, L, _ in jobs:
            hists.append((s["y"][T - L + 1:T + 1], s["t"][T - L + 1:T + 1]))
            acts.append([s["y"][T + h] for h in HS])
            keys.append([f"{s['sid']}|T{T}|L{L}|h{h}" for h in HS])
    pt, _, _ = LG.predict_batch(hists, HS, threads=8)
    a = np.array(acts)
    ale_agent = float(np.mean(np.abs(np.log(pt / a))))
    bench_l = ref.loc[[x for row in keys for x in row], "lgbm"].to_numpy().reshape(pt.shape)
    ale_bench = float(np.mean(np.abs(np.log(bench_l / a))))
    return {"series_checked": len(pick), "fits_checked": n_fit, "sec": round(sec, 1),
            "max_rel_diff_vs_csv": {k: float(f"{v:.3g}") for k, v in worst.items()},
            "lgbm_all_cases": {"cases": int(pt.size), "mean_ale_agent_model": round(ale_agent, 6),
                               "mean_ale_bench_csv": round(ale_bench, 6),
                               "max_rel_diff_vs_csv": float(f"{float(np.max(np.abs(pt / bench_l - 1))):.3g}")}}


TEMPLATE = '''"""series_auto 的 80% 区间校准表：离线基准（2,000 条 M4 / M3 / Tourism 月度序列，72,000 个 case）上的经验 ln 误差分位。
由 models/build_calibration.py 生成，不要手改（改了基准或成员就重新生成，TABLE_ID 随内容变）。

e = ln(真值 / 点估计)；区间 = 点 x exp(q10) .. 点 x exp(q90)（80%）。行：
- comb_ETYL_mean|L{{13,24,36}}|h{{1..4}}：series_auto 的模型路径（AutoETS、Theta、yoy3、LightGBM 的算术平均），
  基准里历史正好 L 个连续月；series_auto 把 13-23 个月归 L13、24-35 归 L24、36 归 L36 [人为约定：较短的那一档，偏保守]。
  有成员不是正数的 case 不进这几行（agent 那时退到 yoy 路径；个数见 SOURCE）。
- yoy|pairs{{1,2,3}}|h{{1..4}}：yoy 路径，按用到的同比对个数（基准原点上、最近 n 个月的同比对）。
每行另有同一批 case 上的 80% 覆盖率：合并的按构造约为 0.80；按数据集分开（cov80_M4 / _M3 / _Tourism）差很多，
说明一张表不能对每条序列都校准（BENCH_ZH.md 4.3）。这些覆盖率是样本内的，不是样本外验证。
"""
TABLE_ID = {table_id!r}
SOURCE = {source}
VERIFY = {verify}
ROWS = {rows}


def row(kind: str, bucket: str, h: int) -> tuple:
    """(行名, 行)；没有这一行抛 KeyError。"""
    key = f"{{kind}}|{{bucket}}|h{{h}}"
    return key, ROWS[key]
'''


def _fmt(obj) -> str:
    return json.dumps(obj, indent=1, ensure_ascii=False).replace("true", "True").replace("false", "False").replace("null", "None")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", default="bench")
    ap.add_argument("--verify", type=int, default=0, help="抽这么多条基准序列核对 agent 的成员调用（0 = 不核对）")
    ap.add_argument("--dump-cases", action="store_true", help="只写 models/calibration_cases.csv.xz（算出的行要和现有表相同）")
    ap.add_argument("--check-cases", action="store_true", help="不需要 bench：从 CASES 重算，和 calibration.py 比")
    a = ap.parse_args(argv)
    if a.check_cases:
        r = check_cases()
        print(json.dumps(r, indent=1))
        return 0 if r["rows_equal"] and r["table_id_equal"] else 1
    bench = Path(a.bench)
    rows, d, n_nonpos, cases = etyl_rows(bench)
    yr, ychk, ycases = yoy_rows(bench, d)
    ychk["etyl_cases_dropped_nonpositive_member"] = n_nonpos
    rows.update(yr)
    cases.update(ycases)
    if a.dump_cases:
        from .. import calibration as CAL
        assert rows == CAL.ROWS, "rows from bench differ from calibration.py; regenerate the table first"
        dump_cases(cases)
        r = check_cases()
        print(json.dumps({**r, "file": str(CASES), "bytes": CASES.stat().st_size, "sha256": sha256(CASES)}, indent=1))
        return 0 if r["rows_equal"] and r["table_id_equal"] else 1
    ml_meta = json.loads((bench / "out" / "ml_meta.json").read_text(encoding="utf-8"))
    source = {"benchmark": "BENCH_ZH.md (2026-10-23): 2,000 monthly series (M4 1,400 / M3 300 / Tourism 300), 3 origins each, "
                           "L in 13/24/36, h 1..4, no missing months",
              "classic_results.csv_sha256": sha256(bench / "out" / "classic_results.csv"),
              "ml_results.csv_sha256": sha256(bench / "out" / "ml_results.csv"),
              "ml_cfg_key": ml_meta.get("cfg_key"), "agent_lgbm_cfg_key": LG.cfg_key(),
              "sample": "bench/harness.py sample_series(seed 2026), make_tasks(gaps 0)", "log_error": "ln(actual / point)",
              "quantiles": "numpy.quantile, linear interpolation", **ychk}
    ver = verify(bench, d, a.verify) if a.verify else {}
    assert all(math.isfinite(r[q]) for r in rows.values() for q in ("q10", "q50", "q90")), "non-finite quantile"
    tid = table_id(rows, ml_meta.get("cfg_key"))
    OUT.write_text(TEMPLATE.format(table_id=tid, source=_fmt(source), verify=_fmt(ver), rows=_fmt(rows)),
                   encoding="utf-8", newline="\n")
    print(json.dumps({"table_id": tid, "rows": len(rows), "verify": ver, **ychk}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

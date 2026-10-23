"""series_auto 的 80% 区间校准表：离线基准（2,000 条 M4 / M3 / Tourism 月度序列，72,000 个 case）上的经验 ln 误差分位。
由 models/build_calibration.py 生成，不要手改（改了基准或成员就重新生成，TABLE_ID 随内容变）。

e = ln(真值 / 点估计)；区间 = 点 x exp(q10) .. 点 x exp(q90)（80%）。行：
- comb_ETYL_mean|L{13,24,36}|h{1..4}：series_auto 的模型路径（AutoETS、Theta、yoy3、LightGBM 的算术平均），
  基准里历史正好 L 个连续月；series_auto 把 13-23 个月归 L13、24-35 归 L24、36 归 L36 [人为约定：较短的那一档，偏保守]。
  有成员不是正数的 case 不进这几行（agent 那时退到 yoy 路径；个数见 SOURCE）。
- yoy|pairs{1,2,3}|h{1..4}：yoy 路径，按用到的同比对个数（基准原点上、最近 n 个月的同比对）。
每行另有同一批 case 上的 80% 覆盖率：合并的按构造约为 0.80；按数据集分开（cov80_M4 / _M3 / _Tourism）差很多，
说明一张表不能对每条序列都校准（BENCH_ZH.md 4.3）。这些覆盖率是样本内的，不是样本外验证。
"""
TABLE_ID = 'bench-d12f86e0-1013c974'
SOURCE = {
 "benchmark": "BENCH_ZH.md (2026-10-23): 2,000 monthly series (M4 1,400 / M3 300 / Tourism 300), 3 origins each, L in 13/24/36, h 1..4, no missing months",
 "classic_results.csv_sha256": "25a0b58dbb912ed8730ab4daf1cd531f3d8e0b078fc16b04991f53824edb2694",
 "ml_results.csv_sha256": "c13a5217edcbcb8d835f4103b4980c1b1daa2a3d642d317e4b6efc71f615a62a",
 "ml_cfg_key": "d12f86e0",
 "agent_lgbm_cfg_key": "621e6b73",
 "sample": "bench/harness.py sample_series(seed 2026), make_tasks(gaps 0)",
 "log_error": "ln(actual / point)",
 "quantiles": "numpy.quantile, linear interpolation",
 "max_rel_diff_yoy1_vs_csv": 4.970272064586112e-06,
 "max_rel_diff_yoy3_vs_csv": 4.952490668563847e-06,
 "etyl_cases_dropped_nonpositive_member": 27
}
VERIFY = {
 "series_checked": 60,
 "fits_checked": 540,
 "sec": 58.9,
 "max_rel_diff_vs_csv": {
  "AutoETS": 4.68e-06,
  "Theta": 4.92e-06,
  "yoy3": 4.87e-06,
  "LightGBM": 4.94e-06
 },
 "lgbm_all_cases": {
  "cases": 72000,
  "mean_ale_agent_model": 0.112238,
  "mean_ale_bench_csv": 0.112238,
  "max_rel_diff_vs_csv": 4.97e-06
 }
}
ROWS = {
 "comb_ETYL_mean|L13|h1": {
  "q10": -0.180553,
  "q50": -0.000175,
  "q90": 0.144016,
  "n": 5999,
  "cov80": 0.8,
  "cov80_M4": 0.8831,
  "cov80_M3": 0.7911,
  "cov80_Tourism": 0.4211
 },
 "comb_ETYL_mean|L13|h2": {
  "q10": -0.201385,
  "q50": 0.000339,
  "q90": 0.160597,
  "n": 5999,
  "cov80": 0.8,
  "cov80_M4": 0.8676,
  "cov80_M3": 0.8078,
  "cov80_Tourism": 0.4767
 },
 "comb_ETYL_mean|L13|h3": {
  "q10": -0.230505,
  "q50": -0.000242,
  "q90": 0.188128,
  "n": 5997,
  "cov80": 0.7999,
  "cov80_M4": 0.8628,
  "cov80_M3": 0.8244,
  "cov80_Tourism": 0.4811
 },
 "comb_ETYL_mean|L13|h4": {
  "q10": -0.267506,
  "q50": 0.000701,
  "q90": 0.195137,
  "n": 5994,
  "cov80": 0.7998,
  "cov80_M4": 0.859,
  "cov80_M3": 0.8189,
  "cov80_Tourism": 0.5033
 },
 "comb_ETYL_mean|L24|h1": {
  "q10": -0.158155,
  "q50": -6.6e-05,
  "q90": 0.140026,
  "n": 5998,
  "cov80": 0.7999,
  "cov80_M4": 0.8773,
  "cov80_M3": 0.7856,
  "cov80_Tourism": 0.4533
 },
 "comb_ETYL_mean|L24|h2": {
  "q10": -0.180939,
  "q50": 0.000385,
  "q90": 0.15752,
  "n": 5999,
  "cov80": 0.8,
  "cov80_M4": 0.8643,
  "cov80_M3": 0.8011,
  "cov80_Tourism": 0.4989
 },
 "comb_ETYL_mean|L24|h3": {
  "q10": -0.209662,
  "q50": 0.000383,
  "q90": 0.185046,
  "n": 5996,
  "cov80": 0.7999,
  "cov80_M4": 0.8573,
  "cov80_M3": 0.8189,
  "cov80_Tourism": 0.5128
 },
 "comb_ETYL_mean|L24|h4": {
  "q10": -0.242792,
  "q50": 0.001123,
  "q90": 0.188466,
  "n": 5994,
  "cov80": 0.7998,
  "cov80_M4": 0.8541,
  "cov80_M3": 0.8211,
  "cov80_Tourism": 0.525
 },
 "comb_ETYL_mean|L36|h1": {
  "q10": -0.141491,
  "q50": 0.000414,
  "q90": 0.131511,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8669,
  "cov80_M3": 0.7789,
  "cov80_Tourism": 0.5089
 },
 "comb_ETYL_mean|L36|h2": {
  "q10": -0.161588,
  "q50": 0.000664,
  "q90": 0.145181,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8533,
  "cov80_M3": 0.7933,
  "cov80_Tourism": 0.5578
 },
 "comb_ETYL_mean|L36|h3": {
  "q10": -0.177945,
  "q50": 0.00061,
  "q90": 0.173278,
  "n": 5999,
  "cov80": 0.8,
  "cov80_M4": 0.8454,
  "cov80_M3": 0.8067,
  "cov80_Tourism": 0.5811
 },
 "comb_ETYL_mean|L36|h4": {
  "q10": -0.207143,
  "q50": 0.001494,
  "q90": 0.171251,
  "n": 5998,
  "cov80": 0.7999,
  "cov80_M4": 0.8406,
  "cov80_M3": 0.8,
  "cov80_Tourism": 0.61
 },
 "yoy|pairs1|h1": {
  "q10": -0.182322,
  "q50": 0.0,
  "q90": 0.204972,
  "n": 6000,
  "cov80": 0.8003,
  "cov80_M4": 0.8645,
  "cov80_M3": 0.7533,
  "cov80_Tourism": 0.5478
 },
 "yoy|pairs1|h2": {
  "q10": -0.209035,
  "q50": 0.0,
  "q90": 0.234405,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8536,
  "cov80_M3": 0.76,
  "cov80_Tourism": 0.59
 },
 "yoy|pairs1|h3": {
  "q10": -0.231521,
  "q50": 0.0,
  "q90": 0.235631,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8505,
  "cov80_M3": 0.77,
  "cov80_Tourism": 0.5944
 },
 "yoy|pairs1|h4": {
  "q10": -0.256101,
  "q50": -0.000712,
  "q90": 0.248671,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8467,
  "cov80_M3": 0.7789,
  "cov80_Tourism": 0.6033
 },
 "yoy|pairs2|h1": {
  "q10": -0.174925,
  "q50": 0.0,
  "q90": 0.194648,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8579,
  "cov80_M3": 0.7733,
  "cov80_Tourism": 0.5567
 },
 "yoy|pairs2|h2": {
  "q10": -0.200104,
  "q50": -0.0,
  "q90": 0.221675,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8445,
  "cov80_M3": 0.7811,
  "cov80_Tourism": 0.6111
 },
 "yoy|pairs2|h3": {
  "q10": -0.218461,
  "q50": -7.7e-05,
  "q90": 0.226545,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8457,
  "cov80_M3": 0.7844,
  "cov80_Tourism": 0.6022
 },
 "yoy|pairs2|h4": {
  "q10": -0.234132,
  "q50": -0.000859,
  "q90": 0.233505,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8355,
  "cov80_M3": 0.7889,
  "cov80_Tourism": 0.6456
 },
 "yoy|pairs3|h1": {
  "q10": -0.172246,
  "q50": 0.0,
  "q90": 0.194803,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8531,
  "cov80_M3": 0.7733,
  "cov80_Tourism": 0.5789
 },
 "yoy|pairs3|h2": {
  "q10": -0.196328,
  "q50": 0.000299,
  "q90": 0.215503,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8429,
  "cov80_M3": 0.7889,
  "cov80_Tourism": 0.6111
 },
 "yoy|pairs3|h3": {
  "q10": -0.213141,
  "q50": 7.1e-05,
  "q90": 0.224981,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8386,
  "cov80_M3": 0.7989,
  "cov80_Tourism": 0.6211
 },
 "yoy|pairs3|h4": {
  "q10": -0.23172,
  "q50": -0.000442,
  "q90": 0.238417,
  "n": 6000,
  "cov80": 0.8,
  "cov80_M4": 0.8317,
  "cov80_M3": 0.8044,
  "cov80_Tourism": 0.6478
 }
}


def row(kind: str, bucket: str, h: int) -> tuple:
    """(行名, 行)；没有这一行抛 KeyError。"""
    key = f"{kind}|{bucket}|h{h}"
    return key, ROWS[key]

"""v2.12 合并与区间（决定 5）、方法菜单（决定 7）、方法细节的显示（决定 8）。
全部用编造的输入，答案已知；不调模型、不联网（模型路径的成员用编造的结果字典，不跑 statsforecast / LightGBM）。"""
import math
import re
import unittest
from unittest import mock

from triangulate.agent import compute as C
from triangulate.agent import methods as M
from triangulate.agent import outputs as O
from triangulate.agent import prompts as PR

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

Z = M.Z90


def r(mid, est, ids=(), assumptions=(), folds=(), mc=None, sa=None, method="formula_mc"):
    """combine 的一个输入（compute.run 给的方法结果里 combine 用到的字段）。"""
    out = {"id": mid, "method": method, "estimate": est, "used_ids": list(ids), "used_assumptions": list(assumptions),
           "backtest": [{"year": 2020 + i, "log_err": e} for i, e in enumerate(folds)]}
    if mc:
        out["mc"] = {"p10": mc[0], "p90": mc[1]}
    if sa:
        out["series_auto"] = {"interval": {"q10_ln": sa[0], "q90_ln": sa[1], "calibration_row": "yoy|pairs1|h1",
                                           "table": "t"}}
    return out


class TestT90(unittest.TestCase):
    def test_table_matches_scipy(self):
        from scipy import stats
        for df in range(1, 31):
            self.assertAlmostEqual(M.t90(df), stats.t.ppf(0.9, df), places=5, msg=df)
        for df in (31, 40, 60, 120, 500):                                   # 表外用 Cornish-Fisher 展开
            self.assertAlmostEqual(M.t90(df), stats.t.ppf(0.9, df), places=4, msg=df)


class TestBlocks(unittest.TestCase):
    def test_jaccard_half_joins_and_is_transitive(self):
        rs = [r("m1", 1.0, ["p1", "p2"]), r("m2", 1.0, ["p2", "p3"]), r("m3", 1.0, ["p3", "p4", "p2"]), r("m4", 1.0, ["p9"])]
        # m1-m2: 1/3 < 0.5；m2-m3: 2/3 >= 0.5；m1-m3: 1/4。m1 自己一块，m2 + m3 一块，m4 一块
        self.assertEqual(M.blocks_of(rs), [[0], [1, 2], [3]])
        rs[0]["used_ids"] = ["p2", "p3", "p1"]          # m1-m2: 2/3：三个连成一块（并查集，可传递）
        self.assertEqual(M.blocks_of(rs), [[0, 1, 2], [3]])

    def test_assumptions_count_as_inputs(self):
        a = r("m1", 10.0, ["p1"], ["a1", "a2"])
        b = r("m2", 12.0, ["p5"], ["a1", "a2"])          # 共用两个假设：2/4 = 0.5 -> 一块
        self.assertEqual(M.blocks_of([a, b]), [[0, 1]])

    def test_consensus_point_is_its_own_block(self):
        # 分析师 / consensus 估计作为一条路线（formula "a" = 那个点），和数据路线不共用 id：自成一块，和数据块等权
        data1 = r("m1", 100.0, ["p1", "p2", "p3"], method="series_auto", sa=(-0.15, 0.15))
        data2 = r("m2", 110.0, ["p1", "p2", "p3", "p4"], method="yoy_scaling", folds=(0.02, -0.01))
        consensus = r("m3", 130.0, ["p9"], mc=(108.0, 156.0))
        c = M.combine([data1, data2, consensus])
        self.assertEqual([b["members"] for b in c["combination"]["blocks"]], [["m1", "m2"], ["m3"]])
        self.assertAlmostEqual(c["central"], math.sqrt(math.sqrt(100 * 110) * 130))
        self.assertEqual(c["weights"], {"m1": 0.25, "m2": 0.25, "m3": 0.5})


class TestCentre(unittest.TestCase):
    def test_one_two_three_four_blocks(self):
        self.assertAlmostEqual(M.combine([r("m1", 50.0)])["central"], 50.0)
        self.assertAlmostEqual(M.combine([r("m1", 50.0), r("m2", 200.0)])["central"], 100.0)            # 几何平均
        c = M.combine([r("m1", 50.0), r("m2", 200.0), r("m3", 90.0)])                                      # 中位数
        self.assertAlmostEqual(c["central"], 90.0)
        self.assertEqual(c["weights"], {"m1": 0.0, "m2": 0.0, "m3": 1.0})
        c = M.combine([r("m1", 50.0), r("m2", 200.0), r("m3", 90.0), r("m4", 160.0)])                     # 偶数：中间两个
        self.assertAlmostEqual(c["central"], math.sqrt(90 * 160))
        self.assertEqual(c["weights"], {"m1": 0.0, "m2": 0.0, "m3": 0.5, "m4": 0.5})
        self.assertEqual(c["weight_rule"], "equal_blocks_median")

    def test_inside_a_block_two_average_three_take_the_median(self):
        ids = ["p1", "p2"]
        c = M.combine([r("m1", 100.0, ids), r("m2", 121.0, ids)])
        self.assertAlmostEqual(c["central"], 110.0)
        self.assertEqual(c["weight_rule"], "single_block")
        c = M.combine([r("m1", 100.0, ids), r("m2", 121.0, ids), r("m3", 300.0, ids)])
        self.assertAlmostEqual(c["central"], 121.0)
        self.assertEqual(c["combination"]["blocks"][0]["rule"], "median")

    def test_backtest_errors_do_not_set_weights(self):
        good = r("m1", 100.0, ["p1"], folds=(0.001, -0.001, 0.002))
        bad = r("m2", 200.0, ["p2"], folds=(0.5, -0.4, 0.6))
        c = M.combine([good, bad])
        self.assertEqual(c["weights"], {"m1": 0.5, "m2": 0.5})
        self.assertIn("off", c["combination"]["weight_gate"])

    def test_weight_gate_path_is_off_but_runs_when_opened(self):
        good = r("m1", 100.0, ["p1"], folds=(0.01, -0.01))
        bad = r("m2", 200.0, ["p2"], folds=(0.2, -0.2))
        with mock.patch.dict(M.WEIGHT_GATE, {"passed": True}):
            c = M.combine([good, bad])
        w = c["weights"]
        self.assertAlmostEqual(w["m1"] / w["m2"], (0.2 + M.EPS) / (0.01 + M.EPS))
        self.assertEqual(c["weight_rule"], "blocks_inverse_backtest_error")
        self.assertFalse(M.WEIGHT_GATE["passed"])


class TestIntervals(unittest.TestCase):
    def test_member_widths(self):
        s, src, d = M._member_sigma(r("m1", 1.0, folds=(0.1, -0.1, 0.1)))
        self.assertEqual(src, "backtest_t")
        self.assertAlmostEqual(s, 0.1 * M.t90(3) / Z)                       # RMSE x t(n, 0.9) / z(0.9)
        self.assertEqual(M._member_sigma(r("m1", 1.0, folds=(0.1,)))[1], "no_basis")   # 1 折不够
        self.assertEqual(M._member_sigma(r("m1", 1.0, mc=(90.0, 110.0)))[:2], (M.FALLBACK_SIGMA, "no_basis"))   # MC 不收窄
        s, src, _ = M._member_sigma(r("m1", 1.0, mc=(50.0, 200.0)))
        self.assertEqual(src, "monte_carlo")
        self.assertAlmostEqual(s, math.log(4) / (2 * Z))
        s, src, d = M._member_sigma(r("m1", 1.0, sa=(-0.2, 0.1)))
        self.assertEqual((src, d["calibration_row"]), ("series_calibration", "yoy|pairs1|h1"))
        self.assertAlmostEqual(s, 0.3 / (2 * Z))

    def test_single_series_auto_uses_its_calibrated_interval(self):
        c = M.combine([r("m1", 1000.0, ["p1"], method="series_auto", sa=(-0.2, 0.1))])
        self.assertEqual(c["basis"], "series_calibration")
        self.assertAlmostEqual(c["p10"], 1000.0 * math.exp(-0.2))
        self.assertAlmostEqual(c["p90"], 1000.0 * math.exp(0.1))      # 不对称，照校准行

    def test_agreeing_blocks_keep_the_rms_width(self):
        a = r("m1", 100.0, ["p1"], mc=(70.0, 140.0))
        b = r("m2", 102.0, ["p2"], mc=(80.0, 125.0))
        c = M.combine([a, b])
        sa, sb = math.log(2) / (2 * Z), math.log(125 / 80) / (2 * Z)
        sb = max(sb, M.FALLBACK_SIGMA)
        self.assertEqual(c["basis"], "blocks")
        self.assertAlmostEqual(c["sigma_ln"], math.sqrt((sa ** 2 + sb ** 2) / 2))   # 不按块数收窄
        self.assertLess(c["interval"]["birge_ratio"], 1)

    def test_disagreeing_blocks_are_widened_by_the_birge_ratio(self):
        a = r("m1", 100.0, ["p1"], sa=(-0.1, 0.1), method="series_auto")
        b = r("m2", 160.0, ["p2"], folds=(0.02, -0.03, 0.01), method="yoy_scaling")
        c = M.combine([a, b])
        iv = c["interval"]
        sa, sb = 0.2 / (2 * Z), math.sqrt((0.02 ** 2 + 0.03 ** 2 + 0.01 ** 2) / 3) * M.t90(3) / Z
        mu = (math.log(100) / sa ** 2 + math.log(160) / sb ** 2) / (1 / sa ** 2 + 1 / sb ** 2)   # chi2 绕 1/sigma^2 加权均值
        chi2 = ((math.log(100) - mu) / sa) ** 2 + ((math.log(160) - mu) / sb) ** 2
        self.assertAlmostEqual(iv["chi2"], chi2)
        self.assertAlmostEqual(iv["birge_ratio"], math.sqrt(chi2))
        self.assertAlmostEqual(c["sigma_ln"], math.sqrt((sa ** 2 + sb ** 2) / 2) * math.sqrt(chi2))
        self.assertEqual(c["basis"], "blocks_disagree")
        self.assertIn("birge_ratio_above_3", iv["flags"])
        self.assertAlmostEqual(c["central"], math.sqrt(100 * 160))                 # 中心仍是等权的几何平均

    def test_a_tight_block_near_a_wide_one_is_not_a_disagreement(self):
        # 数据块 60,149（3% 宽）和 Fermi 块 75,000（MC 约 x/÷1.5）：彼此在宽度以内，不放宽（chi2 绕加权均值算）
        rs = [r("m1", 59800.0, ["p1", "p4"], folds=(-0.01, 0.02, 0.0)), r("m2", 60500.0, ["p1", "p4"], folds=(0.01, -0.02, 0.03)),
              r("m3", 75000.0, ["p9"], ["a1"], mc=(50000.0, 112000.0))]
        c = M.combine(rs)
        self.assertEqual(c["basis"], "blocks")
        self.assertLess(c["interval"]["birge_ratio"], 1)
        self.assertLessEqual(c["p10"], 59800.0)
        self.assertGreaterEqual(c["p90"], 75000.0)

    def test_blocks_more_than_twice_apart_are_covered(self):
        rs = [r("m1", 100.0, ["p1"], sa=(-0.02, 0.02), method="series_auto"), r("m2", 104.0, ["p2"], sa=(-0.02, 0.02)),
              r("m3", 1000.0, ["p3"], sa=(-0.02, 0.02))]
        c = M.combine(rs)
        self.assertAlmostEqual(c["central"], 104.0)
        self.assertIn("blocks_disagree_x2", c["interval"]["flags"])
        self.assertLessEqual(c["p10"], 100.0)
        self.assertGreaterEqual(c["p90"], 1000.0 - 1e-9)

    def test_block_width_is_at_least_the_spread_inside_it(self):
        ids = ["p1", "p2"]
        c = M.combine([r("m1", 100.0, ids, sa=(-0.01, 0.01)), r("m2", 200.0, ids, sa=(-0.01, 0.01))])
        self.assertEqual(c["basis"], "method_spread")
        self.assertAlmostEqual(c["sigma_ln"], math.log(2) / 2)


class TestComputeBaselineAndDetails(unittest.TestCase):
    PTS = {"p1": {"id": "p1", "value": 1210.0, "unit": "w", "keep": True, "period_start": "2025-06-01", "period_end": "2025-06-30"},
           "p2": {"id": "p2", "value": 1000.0, "unit": "w", "keep": True, "period_start": "2025-05-01", "period_end": "2025-05-31"},
           "p3": {"id": "p3", "value": 1100.0, "unit": "w", "keep": True, "period_start": "2026-05-01", "period_end": "2026-05-31"},
           "s1": {"id": "s1", "value": 50.0, "unit": "w", "keep": True, "period_start": "2025-05-01", "period_end": "2025-05-31"},
           "s2": {"id": "s2", "value": 56.0, "unit": "w", "keep": True, "period_start": "2026-05-01", "period_end": "2026-05-31"},
           "k1": {"id": "k1", "value": 1250.0, "unit": "w", "keep": True, "period_start": "2026-06-01", "period_end": "2026-06-30"}}
    TGT = {"period_start": "2026-06-01", "period_end": "2026-06-30"}

    def run3(self):
        ms = [{"method": "series_auto", "params": {"target_history": ["p1", "p2", "p3"]}},
              {"method": "yoy_scaling", "params": {"target_history": ["p1"], "signal_history": ["s1", "s2"]}},
              {"method": "formula_mc", "params": {"formula": "a", "inputs": {"a": {"id": "k1", "role": "analyst consensus"}}}}]
        return C.run(ms, self.PTS, self.TGT)

    def test_three_routes_baseline_and_details(self):
        out = self.run3()
        m1, m2, m3 = out["methods"]
        self.assertAlmostEqual(m1["estimate"], 1210.0 * 1.1)                  # yoy1：去年 6 月 x 1,100 / 1,000
        self.assertAlmostEqual(m2["estimate"], 1210.0 * 56 / 50)
        self.assertEqual(m2["detail"], {"base_year": 2025, "target_base": 1210.0, "signal_base": 50.0, "signal_now": 56.0,
                                        "growth": 1.12})
        res = out["result"]
        # m1 和 m2 只共用 p1：1/4 < 0.5，三块取中位数
        self.assertEqual([b["members"] for b in res["combination"]["blocks"]], [["m1"], ["m2"], ["m3"]])
        self.assertEqual(res["baseline"]["estimate"], 1210.0)                  # 季节朴素：去年同月，不进合并
        self.assertEqual((res["baseline"]["period"], res["baseline"]["from"]), ("2025-06", "m1"))
        self.assertAlmostEqual(res["baseline"]["estimate_vs_baseline"], res["central"] / 1210.0 - 1)
        d1 = O.method_details(m1, res)
        # v2.12d（审查）：不连续的窗口逐月列出用了哪些点；同比对的值、去年同月的值、校准表的 id 都写出来
        for s in ("m1 series_auto, yoy path: yoy1:", "Members: yoy1 1,331 (base month 2025-06 = 1,210 x growth 1.1000 over 1",
                  "sum of the same months a year earlier, 2026-05: 1,100 / 1,000)",
                  "Data window 2025-05 (p2), 2025-06 (p1), 2026-05 (p3) (3 months used, not consecutive; last month 2026-05, "
                  "1 month(s) before the target; the run of consecutive months ending there is 1 long)",
                  "row yoy|pairs1|h1 of table bench-"):
            self.assertIn(s, d1)
        self.assertIn("m2 yoy_scaling: target 2025 1,210 x signal 56 / 50 (growth 1.1200); no backtest year", O.method_details(m2, res))
        self.assertIn("m3 formula_mc: a; Monte Carlo P10 to P90", O.method_details(m3, res))
        comb = O.combination_details(res)
        self.assertTrue(comb[0].startswith("Combination: 3 block(s), equal weight per block"))
        self.assertIn("Estimate = the median of the blocks.", comb[0])
        self.assertTrue(comb[1].startswith("Interval: root mean square of the block widths"))
        self.assertTrue(comb[2].startswith("Seasonal naive baseline (not combined): 1,210 (2025-06, point p1, from m1)"))
        self.assertIn("Birge ratio", comb[1])
        self.assertIn("(not above one, so no widening)" if res["interval"]["birge_ratio"] <= 1 else
                      "(above one, so the width is multiplied by it)", comb[1])

    def test_ledger_inputs_column_for_every_operator(self):
        """v2.12d（审查）：ledger 方法表的输入一栏以前只给 formula_mc 填，series_auto / yoy_scaling 是空的。"""
        out = self.run3()
        st = {"qid": "q", "question": "q?", "as_of": "2026-06-20", "plan": {"target": {}},
              "compute": {"methods": out["methods"], "result": out["result"]}}
        rows = {ln.split(" | ")[0]: ln for ln in O.ledger(st).splitlines() if ln.startswith("| m")}
        self.assertIn("| series_auto | 1,331 | ['p2', 'p1', 'p3'] / [] |", rows["| m1"])
        self.assertIn("| yoy_scaling | 1,355 | ['p1', 's1', 's2'] / [] |", rows["| m2"])

    def test_placeholders_carry_every_number(self):
        out = self.run3()
        ph, put = {}, None

        def put(key, text):
            ph[key] = text
            return f"[[{key}]]"
        lines = [O.method_details(m, out["result"], put) for m in out["methods"]] + O.combination_details(out["result"], put)
        tpl = "\n".join(lines)
        self.assertFalse(re.search(r"\d,\d{3}|\d\.\d", tpl), tpl)             # 数字（千分位、小数）只在占位符里
        rendered = re.sub(r"\[\[([a-z0-9_]+)\]\]", lambda m: ph[m.group(1)], tpl)
        self.assertEqual(rendered, "\n".join([O.method_details(m, out["result"]) for m in out["methods"]]
                                             + O.combination_details(out["result"])))
        self.assertTrue(all(re.fullmatch(r"[a-z0-9_]+", k) for k in ph))

    def test_models_path_details_list_every_member(self):
        sa = {"path": "models", "rule": "arithmetic mean of AutoETS, Theta, yoy3 and LightGBM (benchmark comb_ETYL_mean)",
              "members": {"AutoETS": 7211.0, "Theta": 7661.0, "yoy3": 7206.0, "LightGBM": 7826.0},
              "member_params": {"AutoETS": {"model": "ETS(M,A,M)"}, "Theta": {"model": "Theta(season_length=12)"},
                                "yoy3": {"base_month": "2025-09", "growth": 0.98, "n_pairs": 3},
                                "LightGBM": {"cfg_key": "621e6b73", "point_model": "lgbm_q50.txt.xz",
                                             "point_model_text_sha256": "981053e930267cdeb719"}},
              "window": [f"2025-{m:02d}" for m in range(1, 13)] + [f"2026-{m:02d}" for m in range(1, 8)],
              "last_month": "2026-07", "h": 2, "consecutive_months": 19,
              "interval": {"p10": 6112.0, "p90": 8778.0, "calibration_row": "comb_ETYL_mean|L13|h2", "q10_ln": -0.2,
                           "q90_ln": 0.16, "table": "t"}}
        m = {"id": "m1", "method": "series_auto", "estimate": 7476.0, "series_auto": sa, "used_ids": ["p1"]}
        res = M.combine([m])
        d = O.method_details(m, res)
        for s in ("AutoETS 7,211 (ETS(M,A,M))", "Theta 7,661 (Theta(season_length=12))",
                  "yoy3 7,206 (base month 2025-09 x growth 0.9800 over 3",
                  "LightGBM 7,826 (config 621e6b73, model lgbm_q50.txt.xz (text sha256 981053e93026))",
                  "Data window 2025-01..2026-07 (19 months used, consecutive", "Calibrated 80% interval 6,112 to 8,778",
                  "row comb_ETYL_mean|L13|h2 of table t"):
            self.assertIn(s, d)
        self.assertNotIn("Models path not used", d)
        # v2.12d（审查）：模型路径没走成时，终稿和 ledger 的细节行写明原因
        sa2 = {**sa, "path": "yoy", "models_path_failed": "FileNotFoundError: LightGBM model file missing: lgbm_q10.txt.xz"}
        d2 = O.method_details({**m, "series_auto": sa2}, res)
        self.assertIn("Models path not used: FileNotFoundError: LightGBM model file missing: lgbm_q10.txt.xz.", d2)

    def test_old_results_get_no_details(self):
        self.assertEqual(O.method_details({"id": "m1", "method": "series_naive", "estimate": 5.0}, {"basis": "no_basis"}), "")
        self.assertEqual(O.combination_details({"basis": "no_basis"}), [])


class TestMenuAndAudit(unittest.TestCase):
    def test_methods_spec_lists_the_new_operators(self):
        lines = [x.split(":")[0] for x in PR.METHODS_SPEC.splitlines() if x.startswith("- ")]
        self.assertEqual(lines, ["- series_auto", "- yoy_scaling", "- ratio", "- partial_period", "- formula_mc", "- coverage (optional, any method)"])
        for gone in ("series_naive", "linear_fit", "weights methods by their historical error"):
            self.assertNotIn(gone, PR.METHODS_SPEC)
        self.assertIn("every kept id that is a value of the target itself", PR.METHODS_SPEC)
        self.assertIn("Backtest errors set the interval width, not weights.", PR.METHODS_SPEC)
        self.assertIn('"method": "series_auto", "params": {{"target_history": ["p1", "p2", "p5"]}}', PR.JUDGE_USER)
        self.assertNotIn("series_naive", PR.JUDGE_USER)

    @unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
    def test_audit_rows_for_new_operators(self):
        from triangulate.agent import graph as G
        by_id = {i: {"id": i, "name": i, "value": 1.0, "unit": "w", "period_start": "2025-01-01", "period_end": "2025-01-31"}
                 for i in ("p1", "p2", "p3", "p4")}
        rows = G.audit_rows({"params": {"target_history": ["p1", "p2"]}}, {"method": "series_auto"}, by_id, {})
        self.assertEqual([(n, i, role) for n, i, role, _ in rows], [("p1", "p1", G.TARGET_MONTHLY_ROLE), ("p2", "p2", G.TARGET_MONTHLY_ROLE)])
        rows = G.audit_rows({"params": {"partial_this": "p1", "partial_last": ["p2"], "full_last": ["p3", "p4"]}},
                            {"method": "partial_period"}, by_id, {})
        self.assertEqual([(n, role) for n, _, role, _ in rows],
                         [("partial_this:p1", G.PARTIAL_ROLES["partial_this"]), ("partial_last:p2", G.PARTIAL_ROLES["partial_last"]),
                          ("full_last:p3", G.PARTIAL_ROLES["full_last"]), ("full_last:p4", G.PARTIAL_ROLES["full_last"])])
        rows = G.audit_rows({"params": {"target_history": ["p1"]}}, {"method": "yoy_scaling"}, by_id, {})
        self.assertEqual(rows[0][2], G.TARGET_HISTORY_ROLE)               # 旧算子照旧


if __name__ == "__main__":
    unittest.main()

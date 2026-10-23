"""v2.12 算子层：月度序列、series_auto（yoy 路径和模型路径）、partial_period、ratio of means、删掉的 linear_fit 和
series_naive k>1。全部用编造的序列，答案已知；不调模型、不联网。模型路径要 statsforecast 和 lightgbm（requirements.txt）。"""
import math
import unittest
from unittest import mock

from triangulate.agent import calibration as CAL
from triangulate.agent import compute as C
from triangulate.agent import lgbm_global as LG
from triangulate.agent import methods as M
from triangulate.agent import outputs as O
from triangulate.agent import series as S

TARGET = {"period_start": "2026-08-01", "period_end": "2026-08-31"}
T_AUG26 = S.mi(2026, 8)


def month_pts(values: dict, unit: str = "visitors", start: int = 1) -> dict:
    """{(年, 月): 值} -> 月度点 p1..pN（期间是整月）。"""
    import calendar
    out = {}
    for n, ((y, m), v) in enumerate(sorted(values.items()), start=start):
        last = calendar.monthrange(y, m)[1]
        out[f"p{n}"] = {"id": f"p{n}", "value": v, "unit": unit, "keep": True,
                        "period_start": f"{y}-{m:02d}-01", "period_end": f"{y}-{m:02d}-{last:02d}"}
    return out


def seasonal(y: int, m: int, g: float = 0.01) -> float:
    """乘法季节 x 每月 1% 增长：同比恰好是 1.01^12，yoy 的答案精确已知。"""
    t = S.mi(y, m) - S.mi(2023, 1)
    return 1000.0 * (1 + g) ** t * (1 + 0.3 * math.sin(2 * math.pi * (m - 1) / 12))


def months_back(last: tuple, n: int) -> list:
    t = S.mi(*last)
    return [((k // 12), k % 12 + 1) for k in range(t - n + 1, t + 1)]


def build(values: dict, target_t: int = T_AUG26, **kw) -> dict:
    pts = month_pts(values, **kw)
    return S.build_monthly(list(pts), pts, target_t)


class TestMonthlySeries(unittest.TestCase):
    def test_months_ytd_and_rejections(self):
        pts = month_pts({(2025, 8): 100.0, (2026, 6): 120.0, (2026, 7): 130.0})
        pts["q1"] = {"id": "q1", "value": 900.0, "unit": "visitors", "keep": True, "period_start": "2026-01-01",
                     "period_end": "2026-07-31"}                                   # 年内累计：单独存
        pts["q2"] = {"id": "q2", "value": 300.0, "unit": "visitors", "keep": True, "period_start": "2026-04-01",
                     "period_end": "2026-06-30"}                                   # 季度：不收
        pts["q3"] = {"id": "q3", "value": 140.0, "unit": "visitors", "keep": True, "period_start": "2026-08-01",
                     "period_end": "2026-08-31"}                                   # 目标月本身：不收
        pts["q4"] = {"id": "q4", "value": 0.0, "unit": "visitors", "keep": True, "period_start": "2026-05-01",
                     "period_end": "2026-05-31"}                                   # 非正：不收
        pts["q5"] = {"id": "q5", "value": 1.0, "unit": "visitors", "keep": False, "period_start": "2026-04-01",
                     "period_end": "2026-04-30"}
        pts["q6"] = {"id": "q6", "value": 1.0, "unit": "visitors", "keep": True, "period_start": "", "period_end": "2026-03-31"}
        pts["q7"] = {"id": "q7", "value": 1.0, "unit": "visitors", "keep": True, "period_start": "2026-02-28",
                     "period_end": "2026-02-28", "period_source": "page_date"}
        ms = S.build_monthly(list(pts) + ["zz"], pts, T_AUG26)
        self.assertEqual(ms["months"], {S.mi(2025, 8): 100.0, S.mi(2026, 6): 120.0, S.mi(2026, 7): 130.0})
        self.assertEqual(ms["ytd"], {S.mi(2026, 7): 900.0})
        notes = " | ".join(ms["notes"])
        for frag in ("q2: period 2026-04-01..2026-06-30 is neither", "q3: period 2026-08 is at or after the target",
                     "q4: value 0.0 is not positive", "q5: discarded", "q6: period start or end missing",
                     "q7: period not stated", "zz: unknown id", "year-to-date totals kept separately"):
            self.assertIn(frag, notes)
        self.assertNotIn("q1", ms["used_ids"][:3])
        self.assertEqual(ms["used_ids"], ["p1", "p2", "p3", "q1"])

    def test_same_month_median_and_tolerance(self):
        pts = month_pts({(2026, 6): 100.0, (2026, 7): 130.0})
        pts["d1"] = {"id": "d1", "value": 110.0, "unit": "visitors", "keep": True, "period_start": "2026-06",
                     "period_end": "2026-06"}                                     # YYYY-MM 写法 = 整月
        pts["d2"] = {"id": "d2", "value": 130.0, "unit": "visitors", "keep": True, "period_start": "2026-07-01",
                     "period_end": "2026-08-02"}                                  # 期末多 2 天仍是 7 月
        ms = S.build_monthly(list(pts), pts, T_AUG26)
        self.assertEqual(ms["months"][S.mi(2026, 6)], 105.0)
        self.assertEqual(ms["month_ids"][S.mi(2026, 6)], ["p1", "d1"])
        self.assertEqual(ms["months"][S.mi(2026, 7)], 130.0)
        self.assertTrue(any("2026-06 (month): values disagree" in n for n in ms["notes"]))
        self.assertFalse(any("2026-07 (month)" in n for n in ms["notes"]))

    def test_mixed_percent_minority_dropped(self):
        pts = month_pts({(2026, 5): 100.0, (2026, 6): 110.0, (2026, 7): 120.0})
        pts["x"] = {"id": "x", "value": 3.0, "unit": "%", "keep": True, "period_start": "2026-04-01", "period_end": "2026-04-30"}
        ms = S.build_monthly(list(pts), pts, T_AUG26)
        self.assertNotIn(S.mi(2026, 4), ms["months"])
        self.assertIn("mixed % and non-% units; dropped the minority", ms["notes"])

    def test_target_month(self):
        from datetime import date
        self.assertEqual(S.target_month(date(2026, 8, 1), date(2026, 8, 31)), T_AUG26)
        self.assertIsNone(S.target_month(date(2026, 7, 1), date(2026, 9, 30)))
        self.assertIsNone(S.target_month(date(2026, 1, 1), date(2026, 12, 31)))


class TestYoy(unittest.TestCase):
    def test_known_answer_three_pairs(self):
        # 去年 8 月 100；今年 5-7 月 110 / 120 / 130，去年 5-7 月 100 / 100 / 100 -> g = 360 / 300 = 1.2 -> 120
        v = {(2025, 8): 100.0, (2025, 5): 100.0, (2025, 6): 100.0, (2025, 7): 100.0,
             (2026, 5): 110.0, (2026, 6): 120.0, (2026, 7): 130.0, (2026, 4): 999.0}
        ms = build(v)
        y = S.yoy(ms["months"], T_AUG26, max(ms["months"]))
        self.assertAlmostEqual(y["growth"], 1.2)
        self.assertAlmostEqual(y["estimate"], 120.0)
        self.assertEqual([p["month"] for p in y["pairs"]], ["2026-05", "2026-06", "2026-07"])   # 4 月没有去年值，不成对

    def test_one_pair_is_yoy1_and_gaps_skip(self):
        v = {(2025, 8): 100.0, (2025, 5): 80.0, (2026, 5): 88.0, (2026, 7): 1.0}   # 只有 5 月成对；7 月没有去年值
        ms = build(v)
        y = S.yoy(ms["months"], T_AUG26, S.mi(2026, 7))
        self.assertEqual(y["n_pairs"], 1)
        self.assertAlmostEqual(y["estimate"], 110.0)

    def test_old_pairs_not_used(self):
        # 2024-03 / 2023-03 是一对，但在去年同月（2025-08）之前：那是去年的增长，不是今年的
        v = {(2025, 8): 100.0, (2024, 3): 50.0, (2023, 3): 40.0, (2026, 7): 90.0}
        with self.assertRaisesRegex(S.SeriesError, "no year-on-year pair"):
            S.yoy(build(v)["months"], T_AUG26, S.mi(2026, 7))

    def test_missing_last_year_month(self):
        v = {(2025, 7): 100.0, (2026, 7): 110.0, (2024, 8): 90.0}
        with self.assertRaisesRegex(S.SeriesError, r"last year's value for the target month \(2025-08\)"):
            S.yoy(build(v)["months"], T_AUG26, S.mi(2026, 7))


class TestSeriesAutoYoyPath(unittest.TestCase):
    def test_short_history_uses_yoy_and_calibration(self):
        v = {k: seasonal(*k) for k in [(2025, 8), (2025, 5), (2025, 6), (2025, 7), (2026, 5), (2026, 6), (2026, 7)]}
        r = S.series_auto(build(v), T_AUG26)
        self.assertEqual(r["path"], "yoy")
        self.assertAlmostEqual(r["estimate"], seasonal(2026, 8), places=6)        # 同比恒定：yoy 精确
        self.assertEqual(r["interval"]["calibration_row"], "yoy|pairs3|h1")
        key, row = CAL.row("yoy", "pairs3", 1)
        self.assertAlmostEqual(r["interval"]["p10"], r["estimate"] * math.exp(row["q10"]))
        self.assertAlmostEqual(r["interval"]["p90"], r["estimate"] * math.exp(row["q90"]))
        self.assertLess(r["interval"]["p10"], r["estimate"])
        self.assertGreater(r["interval"]["p90"], r["estimate"])
        self.assertEqual(r["baseline"], {"method": "seasonal naive (last year's same month)", "month": "2025-08",
                                         "estimate": seasonal(2025, 8), "ids": ["p4"]})   # month_pts 按月份排：2025-08 是 p4
        self.assertTrue(r["rule"].startswith("yoy3: "))
        self.assertEqual(r["window_month_ids"]["2025-08"], ["p4"])
        self.assertEqual(r["window"], ["2025-05", "2025-06", "2025-07", "2025-08", "2026-05", "2026-06", "2026-07"])
        self.assertEqual(r["consecutive_months"], 3)

    def test_h_up_to_4_and_beyond(self):
        v = {(2025, 8): 100.0, (2025, 4): 100.0, (2026, 4): 105.0}
        r = S.series_auto(build(v), T_AUG26)                                        # 最后已知 4 月，h = 4
        self.assertEqual(r["h"], 4)
        self.assertEqual(r["interval"]["calibration_row"], "yoy|pairs1|h4")
        self.assertAlmostEqual(r["estimate"], 105.0)
        v = {(2025, 8): 100.0, (2025, 3): 100.0, (2026, 3): 105.0}
        with self.assertRaisesRegex(S.SeriesError, "5 months before the target 2026-08; series_auto is calibrated only for 1 to 4"):
            S.series_auto(build(v), T_AUG26)

    def test_very_short_history(self):
        with self.assertRaisesRegex(S.SeriesError, "no monthly values"):
            S.series_auto(build({}), T_AUG26)
        with self.assertRaisesRegex(S.SeriesError, "no year-on-year pair"):
            S.series_auto(build({(2025, 8): 100.0, (2026, 7): 110.0}), T_AUG26)

    def test_gap_breaks_consecutive_run(self):
        ks = months_back((2026, 7), 20)
        v = {k: seasonal(*k) for k in ks if k != (2026, 3)}        # 3 月缺：以 7 月结尾的连续段只有 4 个月
        r = S.series_auto(build(v), T_AUG26)
        self.assertEqual(r["consecutive_months"], 4)
        self.assertEqual(r["path"], "yoy")

    def test_non_positive_month_dropped(self):
        ks = months_back((2026, 7), 16)
        v = {k: seasonal(*k) for k in ks}
        v[(2026, 2)] = -5.0
        ms = build(v)
        self.assertNotIn(S.mi(2026, 2), ms["months"])
        r = S.series_auto(ms, T_AUG26)
        self.assertEqual(r["consecutive_months"], 5)
        self.assertEqual(r["path"], "yoy")


class TestSeriesAutoModelPath(unittest.TestCase):
    def test_models_known_series(self):
        v = {k: seasonal(*k) for k in months_back((2026, 7), 30)}
        r = S.series_auto(build(v), T_AUG26)
        self.assertEqual(r["path"], "models")
        self.assertEqual(set(r["members"]), {"AutoETS", "Theta", "yoy3", "LightGBM"})
        self.assertAlmostEqual(r["estimate"], sum(r["members"].values()) / 4)
        self.assertAlmostEqual(r["members"]["yoy3"], seasonal(2026, 8), places=6)
        truth = seasonal(2026, 8)
        # 成员各有偏差（这条强趋势 + 季节的序列上 Theta 的季节检验没认出季节，约 +17%）；只钉住合并值和 ETS
        self.assertLess(abs(r["estimate"] / truth - 1), 0.10, r["members"])
        self.assertLess(abs(r["members"]["AutoETS"] / truth - 1), 0.03, r["members"])
        self.assertEqual(len(r["window"]), 30)
        self.assertEqual(r["interval"]["calibration_row"], "comb_ETYL_mean|L24|h1")
        self.assertTrue(r["member_params"]["AutoETS"]["model"].startswith("ETS("))
        self.assertEqual(r["member_params"]["LightGBM"]["cfg_key"], LG.cfg_key())

    def test_window_capped_and_buckets(self):
        for n, bucket, wlen in ((13, "L13", 13), (23, "L13", 23), (24, "L24", 24), (40, "L36", 36)):
            v = {k: seasonal(*k) for k in months_back((2026, 6), n)}               # h = 2
            r = S.series_auto(build(v), T_AUG26)
            self.assertEqual(r["path"], "models", n)
            self.assertEqual(r["interval"]["calibration_row"], f"comb_ETYL_mean|{bucket}|h2", n)
            self.assertEqual(len(r["window"]), wlen, n)
            self.assertEqual(r["window"][-1], "2026-06")

    def test_member_failure_falls_back_to_yoy(self):
        v = {k: seasonal(*k) for k in months_back((2026, 7), 15)}
        with mock.patch.object(S, "_ets", side_effect=RuntimeError("boom")):
            r = S.series_auto(build(v), T_AUG26)
        self.assertEqual(r["path"], "yoy")
        self.assertIn("model path failed (RuntimeError: boom)", r["notes"][0])
        self.assertEqual(r["models_path_failed"], "RuntimeError: boom")     # v2.12d：终稿写明原因用
        self.assertEqual(r["interval"]["calibration_row"], "yoy|pairs3|h1")

    def test_rule_name_follows_pairs(self):
        """v2.12d（审查）：2 个同比对时规则名是 yoy2（以前写 yoy3），和成员名、校准行一致。"""
        v = {k: seasonal(*k) for k in [(2025, 8), (2025, 6), (2025, 7), (2026, 6), (2026, 7)]}
        r = S.series_auto(build(v), T_AUG26)
        self.assertEqual(list(r["members"]), ["yoy2"])
        self.assertTrue(r["rule"].startswith("yoy2: ") and "latest 2 year-on-year pairs" in r["rule"], r["rule"])
        self.assertEqual(r["interval"]["calibration_row"], "yoy|pairs2|h1")

    def test_concurrent_first_load(self):
        """v2.12d（审查）：两个线程同时第一次用 LightGBM，以前后到的线程看到只装了一半的缓存（KeyError 0.5）、安静地退到 yoy。"""
        import threading
        y = [1000 * 1.01 ** i for i in range(24)]
        t = list(range(2024 * 12, 2024 * 12 + 24))
        saved = dict(LG._BOOSTERS)
        LG._BOOSTERS.clear()
        res, errs = {}, []

        def go(name):
            try:
                res[name] = LG.predict_one(y, t, 1)
            except Exception as e:   # noqa: BLE001  测试要看到任何异常
                errs.append(f"{name}: {type(e).__name__}: {e}")
        try:
            th = [threading.Thread(target=go, args=(f"t{i}",)) for i in range(4)]
            for x in th:
                x.start()
            for x in th:
                x.join()
        finally:
            if not LG._BOOSTERS:
                LG._BOOSTERS.update(saved)
        self.assertEqual(errs, [])
        self.assertEqual(len(set(res.values())), 1)
        self.assertEqual(sorted(LG._BOOSTERS), [0.1, 0.5, 0.9])

    def test_lgbm_rejects_h_beyond_training(self):
        with self.assertRaises(ValueError):
            LG.predict_batch([([1.0] * 13, list(range(13)))], [5])


class TestComputeIntegration(unittest.TestCase):
    def test_series_auto_through_compute(self):
        pts = month_pts({k: seasonal(*k) for k in [(2025, 8), (2025, 6), (2025, 7), (2026, 6), (2026, 7)]})
        out = C.run([{"method": "series_auto", "params": {"target_history": list(pts)}}], pts, TARGET)
        m = out["methods"][0]
        self.assertNotIn("error", m)
        self.assertAlmostEqual(m["estimate"], seasonal(2026, 8), places=6)
        self.assertEqual(sorted(m["used_ids"]), sorted(pts))
        self.assertEqual(m["series_auto"]["path"], "yoy")
        self.assertEqual(m["monthly_series"]["2026-07"], seasonal(2026, 7))
        self.assertAlmostEqual(out["result"]["central"], m["estimate"])

    def test_series_auto_needs_monthly_target(self):
        pts = month_pts({(2025, 8): 1.0})
        out = C.run([{"method": "series_auto", "params": {"target_history": ["p1"]}}], pts,
                    {"period_start": "2026-07-01", "period_end": "2026-09-30"})
        self.assertIn("one calendar month", out["methods"][0]["error"])

    def test_partial_period_known_answer(self):
        def pt(i, v, a, b):
            return i, {"id": i, "value": v, "unit": "visitors", "keep": True, "period_start": a, "period_end": b}
        pts = dict([pt("t", 600.0, "2026-01-01", "2026-08-31"),                      # 今年 1-8 月
                    pt("a25", 500.0, "2025-01-01", "2025-08-31"), pt("f25", 800.0, "2025-01-01", "2025-12-31"),
                    pt("a24", 400.0, "2024-01-01", "2024-08-31"), pt("f24", 700.0, "2024-01-01", "2024-12-31"),
                    pt("f23", 650.0, "2023-01-01", "2023-12-31")])
        year = {"period_start": "2026-01-01", "period_end": "2026-12-31"}
        one = {"method": "partial_period", "params": {"partial_this": "t", "partial_last": "a25", "full_last": "f25"}}
        m = C.run([one], pts, year)["methods"][0]
        self.assertAlmostEqual(m["estimate"], 960.0)                                # 600 / (500 / 800)
        self.assertAlmostEqual(m["partial_period"]["coverage_ratio"], 0.625)
        two = {"method": "partial_period", "params": {"partial_this": "t", "partial_last": ["a25", "a24"],
                                                      "full_last": ["f25", "f24", "f23"]}}
        m = C.run([two], pts, year)["methods"][0]
        self.assertAlmostEqual(m["estimate"], 1000.0)                               # 600 x 1500 / 900（ratio of means）
        self.assertEqual([p["year"] for p in m["partial_period"]["pairs"]], [2024, 2025])
        self.assertEqual(m["used_ids"], ["t", "a24", "f24", "a25", "f25"])
        self.assertTrue(any("f23 (2023) has no partial_last value" in n for n in m["notes"]))
        self.assertEqual(len(m["backtest"]), 1)                                     # 2025 用 2024 的覆盖率
        self.assertAlmostEqual(m["backtest"][0]["pred"], 500 / (400 / 700))
        self.assertAlmostEqual(m["backtest"][0]["log_err"], math.log(500 / (400 / 700) / 800))

    def test_partial_period_errors(self):
        def pt(v, a, b, unit="visitors"):
            return {"value": v, "unit": unit, "keep": True, "period_start": a, "period_end": b}
        year = {"period_start": "2026-01-01", "period_end": "2026-12-31"}
        base = {"t": pt(600.0, "2026-01-01", "2026-08-31"), "a": pt(500.0, "2025-01-01", "2025-08-31"),
                "f": pt(800.0, "2025-01-01", "2025-12-31")}
        cases = [({"a": pt(900.0, "2025-01-01", "2025-08-31")}, {}, "larger than its full period"),
                 ({"t": pt(600.0, "2025-09-01", "2026-08-31")}, {}, "not inside the target period"),
                 ({"a": pt(500.0, "2025-01-01", "2025-06-30")}, {}, "same calendar span as partial_this"),
                 ({"f": pt(800.0, "2025-01-01", "2025-08-31")}, {}, "same calendar span as the target"),
                 ({"a": pt(5.0, "2025-01-01", "2025-08-31", "%")}, {}, "is a percentage"),
                 ({"a2": pt(510.0, "2025-01-01", "2025-08-31")}, {"partial_last": ["a", "a2"]}, "lists two points for 2025"),
                 ({}, {"partial_this": ["t", "a"]}, "must be one data point id"),
                 ({}, {"full_last": []}, "must be a data point id or a list"),
                 ({"f": pt(800.0, "2024-01-01", "2024-12-31")}, {}, "needs at least one earlier period")]
        for over, prm_over, msg in cases:
            pts = {k: {"id": k, **v} for k, v in {**base, **over}.items()}
            prm = {"partial_this": "t", "partial_last": "a", "full_last": "f", **prm_over}
            m = C.run([{"method": "partial_period", "params": prm}], pts, year)["methods"][0]
            self.assertIn(msg, m.get("error", ""), (over, prm_over))

    def test_ratio_of_means_and_removed_methods(self):
        T = {2023: 10.0, 2024: 30.0}
        Sg = {2023: 1.0, 2024: 2.0, 2025: 4.0}
        self.assertAlmostEqual(M.ratio(T, Sg, 2025), 4.0 * 40.0 / 3.0)            # 旧规则（比值均值）是 4 x 12.5 = 50
        self.assertFalse(hasattr(M, "linear_fit"))
        pts = month_pts({(2025, 8): 100.0, (2024, 8): 90.0})
        out = C.run([{"method": "linear_fit", "params": {"target_history": ["p1", "p2"], "signal_history": ["p1"]}},
                     {"method": "series_naive", "params": {"target_history": ["p1", "p2"], "k": 2}},
                     {"method": "series_naive", "params": {"target_history": ["p1", "p2"], "k": 1}}], pts, TARGET)
        e = [m.get("error", "") for m in out["methods"]]
        self.assertIn("linear_fit was removed", e[0])
        self.assertIn("series_naive k=2 is no longer available", e[1])
        # v2.12（决定 3）：k=1 只作对照基线，不进合并
        self.assertIsNone(out["methods"][2]["estimate"])
        self.assertEqual(out["methods"][2]["baseline_only"]["estimate"], 100.0)
        self.assertIn("is a baseline only", e[2])
        self.assertIsNone(out["result"]["central"])
        self.assertEqual(out["result"]["baseline"]["estimate"], 100.0)

    def test_baseline_kept_when_series_auto_fails(self):
        """v2.12d（审查）：series_auto 做不了（没有同比对、h > 4）时，去年同月照样作季节朴素对照（决定 3），月度序列也留着。"""
        tgt = {"period_start": "2026-09-01", "period_end": "2026-09-30"}
        fm = {"method": "formula_mc", "params": {"formula": "a * k_days_target", "inputs": {"a": {"id": "d", "role": "r"}}}}
        day = {"d": {"id": "d", "value": 50.0, "unit": "people per day", "keep": True, "period_start": "2026-09-01",
                     "period_end": "2026-09-30"}}
        for v, msg in (({(2025, 9): 1000.0, (2026, 8): 1100.0, (2026, 7): 1080.0}, "no year-on-year pair"),
                       ({(2025, 9): 1000.0, (2026, 4): 1100.0, (2025, 4): 1050.0}, "5 months before the target")):
            pts = {**month_pts(v), **day}
            out = C.run([{"method": "series_auto", "params": {"target_history": [k for k in pts if k != "d"]}}, fm], pts, tgt)
            m1 = out["methods"][0]
            self.assertIn(msg, m1["error"])
            self.assertEqual(m1["seasonal_baseline"]["estimate"], 1000.0)
            self.assertIn("2025-09", m1["monthly_series"])
            b = out["result"]["baseline"]
            self.assertEqual((b["estimate"], b["period"], b["from"]), (1000.0, "2025-09", "m1"))
            self.assertAlmostEqual(b["estimate_vs_baseline"], out["result"]["central"] / 1000.0 - 1)

    def test_zero_baseline_does_not_crash(self):
        """v2.12d（审查）：去年同期是 0 的计数（series_naive k=1 = 0）以前在 compute.run 里除以 0，整个运行死在裁判节点。"""
        def pt(ps, pe, v):
            return {"value": v, "unit": "incident", "keep": True, "period_start": ps, "period_end": pe}
        pts = {"p1": pt("2025-08-01", "2025-08-31", 0.0), "p2": pt("2024-08-01", "2024-08-31", 3.0),
               "p3": pt("2026-07-01", "2026-07-31", 2.0)}
        tgt = {"period_start": "2026-08-01", "period_end": "2026-08-31"}
        out = C.run([{"method": "series_naive", "params": {"target_history": ["p1", "p2"], "k": 1}},
                     {"method": "formula_mc", "params": {"formula": "x", "inputs": {"x": {"id": "p3", "role": "r"}}}}], pts, tgt)
        self.assertGreater(out["result"]["central"], 0)
        self.assertIsNone(out["result"]["baseline"])                  # 0 不能当对照的分母：没有对照
        self.assertEqual(out["methods"][0]["baseline_only"]["estimate"], 0.0)
        self.assertEqual(C.baseline([{"id": "m1", "baseline_only": {"estimate": 0.0, "years_used": [2025]}},
                                     {"id": "m2", "baseline_only": {"estimate": 4.0, "years_used": [2025]}}], 2026)["from"], "m2")

    def test_partial_period_details_list_every_pair(self):
        """v2.12d（审查）：partial_period 的细节写出每个往年的部分 / 全期 id 和值，覆盖率能照着重算。"""
        pts = {"t": {"id": "t", "value": 600.0, "unit": "v", "keep": True, "period_start": "2026-01-01", "period_end": "2026-08-31"},
               "a25": {"id": "a25", "value": 500.0, "unit": "v", "keep": True, "period_start": "2025-01-01",
                       "period_end": "2025-08-31"},
               "f25": {"id": "f25", "value": 800.0, "unit": "v", "keep": True, "period_start": "2025-01-01",
                       "period_end": "2025-12-31"}}
        out = C.run([{"method": "partial_period", "params": {"partial_this": "t", "partial_last": "a25", "full_last": "f25"}}],
                    pts, {"period_start": "2026-01-01", "period_end": "2026-12-31"})
        d = O.method_details(out["methods"][0], out["result"])
        self.assertIn("partial_this t (2026-01-01..2026-08-31) 600 / coverage 0.6250 (sum of partial / sum of full, ratio of "
                      "means, over 2025: partial a25 = 500 / full f25 = 800)", d)


class TestCalibrationTable(unittest.TestCase):
    def test_rows_and_source(self):
        for L in (13, 24, 36):
            for h in (1, 2, 3, 4):
                key, row = CAL.row("comb_ETYL_mean", f"L{L}", h)
                self.assertTrue(row["q10"] < 0 < row["q90"], key)
                self.assertGreater(row["n"], 5000)
        for n in (1, 2, 3):
            for h in (1, 2, 3, 4):
                key, row = CAL.row("yoy", f"pairs{n}", h)
                self.assertTrue(row["q10"] < 0 < row["q90"], key)
        with self.assertRaises(KeyError):
            CAL.row("yoy", "pairs1", 5)
        self.assertEqual(CAL.SOURCE["ml_cfg_key"], LG.BENCH_CFG_KEY)
        self.assertTrue(CAL.TABLE_ID.startswith(f"bench-{LG.BENCH_CFG_KEY}-"))

    def test_table_rebuilds_from_committed_cases(self):
        """v2.12d（审查）：bench/ 不提交；提交的每个 case 的 ln 误差（models/calibration_cases.csv.xz）能逐位重算出整张表和 TABLE_ID。"""
        from triangulate.agent.models import build_calibration as BC
        r = BC.check_cases()
        self.assertEqual(r["bad_rows"], [])
        self.assertTrue(r["rows_equal"] and r["table_id_equal"], r)
        self.assertEqual(r["n_cases"], 72000 - CAL.SOURCE["etyl_cases_dropped_nonpositive_member"] + 72000)

    def test_model_files_match_meta(self):
        import hashlib
        import lzma
        meta = LG.meta()
        self.assertEqual(meta["cfg_key"], LG.cfg_key())
        for q, p in LG.model_paths().items():
            txt = lzma.decompress(p.read_bytes())
            self.assertEqual(hashlib.sha256(txt).hexdigest(), meta["train_log"][f"q{q}"]["text_sha256"])


if __name__ == "__main__":
    unittest.main()

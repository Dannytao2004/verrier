import math
import random
import unittest

from triangulate.mc import aggregate, lognormal_params, log_median, quantile, sample_inputs, sample_lognormal


class TestLognormal(unittest.TestCase):
    def test_low_high_are_p10_p90(self):
        xs = sorted(sample_lognormal(10.0, 1000.0, 200_000, random.Random(1)))
        self.assertAlmostEqual(quantile(xs, 0.1) / 10.0, 1.0, delta=0.03)
        self.assertAlmostEqual(quantile(xs, 0.9) / 1000.0, 1.0, delta=0.03)
        self.assertAlmostEqual(quantile(xs, 0.5) / 100.0, 1.0, delta=0.02)

    def test_degenerate_range_is_constant(self):
        self.assertEqual(sample_lognormal(5.0, 5.0, 10, random.Random(0)), [5.0] * 10)

    def test_invalid_range(self):
        for lo, hi in [(0, 1), (2, 1), (-1, 3), (1, math.inf)]:
            with self.subTest(lo=lo, hi=hi), self.assertRaises(ValueError):
                lognormal_params(lo, hi)

    def test_seed_determinism(self):
        r = {"a": (1.0, 10.0), "b": (2.0, 3.0)}
        self.assertEqual(sample_inputs(r, 50, "s:q1"), sample_inputs(dict(reversed(list(r.items()))), 50, "s:q1"))
        self.assertNotEqual(sample_inputs(r, 50, "s:q1")["a"], sample_inputs(r, 50, "s:q2")["a"])


class TestQuantileAndLogMedian(unittest.TestCase):
    def test_quantile_linear(self):
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0.5), 3)
        self.assertAlmostEqual(quantile([1, 2, 3, 4], 0.5), 2.5)
        self.assertAlmostEqual(quantile([0, 10], 0.1), 1.0)

    def test_log_median(self):
        self.assertAlmostEqual(log_median([10, 100, 1e6]), 100)
        self.assertAlmostEqual(log_median([10, 1000]), 100)  # 偶数个 -> 几何平均


class TestAggregate(unittest.TestCase):
    def test_median_of_path_medians(self):
        n = 100
        agg = aggregate({"p1": [10.0] * n, "p2": [100.0] * n, "p3": [1000.0] * n})
        self.assertAlmostEqual(agg["central"], 100.0)
        self.assertEqual(agg["outliers"], [])  # 恰好 1 个数量级不算 outlier

    def test_outlier_flag(self):
        n = 100
        agg = aggregate({"p1": [90.0] * n, "p2": [100.0] * n, "p3": [10000.0] * n})
        self.assertAlmostEqual(agg["central"], 100.0)
        self.assertEqual(agg["outliers"], ["p3"])

    def test_pooled_interval(self):
        n = 1000
        agg = aggregate({"p1": [1.0] * n, "p2": [100.0] * n})
        self.assertAlmostEqual(agg["central"], 10.0)
        self.assertAlmostEqual(agg["p10"], 1.0)
        self.assertAlmostEqual(agg["p90"], 100.0)

    def test_invalid_paths_excluded(self):
        n = 10
        agg = aggregate({"p1": [-5.0] * n, "p2": [float("nan")] * n, "p3": [7.0] * n})
        self.assertEqual(agg["used"], ["p3"])
        self.assertAlmostEqual(agg["central"], 7.0)
        self.assertIsNone(aggregate({"p1": [-1.0] * n})["central"])


if __name__ == "__main__":
    unittest.main()

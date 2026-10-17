"""qty：pint 的薄封装（v2.7c 起）。只测我们加的部分：货币、计数名词、百分数和换算系数。"""
import unittest

from triangulate.agent import qty as Q


class TestQty(unittest.TestCase):
    def test_pint_notation(self):
        for t, mag, units in (("t/day", 1.0, "metric_ton / day"), ("USD/year", 1.0, "USD / year"), ("percent", 1, "percent"),
                              ("birth/(1000 person)", 0.001, "birth / person"), ("11 %", 11, "percent")):
            with self.subTest(t=t):
                q, err = Q.parse_unit(t)
                self.assertEqual(err, "")
                self.assertAlmostEqual(q.magnitude, mag)
                self.assertEqual(str(q.units), units)

    def test_count_nouns_and_plurals(self):
        self.assertEqual(Q.convert_factor("slice/person", "slices/people"), (1.0, ""))
        self.assertEqual(Q.convert_factor("cities", "city"), (1.0, ""))
        self.assertIn("cannot be converted", Q.convert_factor("visitor", "person")[1])   # 不同名词是不同的单位

    def test_currencies_are_separate(self):
        self.assertIn("cannot be converted", Q.convert_factor("USD", "EUR")[1])
        self.assertEqual(Q.convert_factor("USD/year", "USD/year"), (1.0, ""))

    def test_pizza_conversions(self):
        # 披萨题（ask_3e7f14f7）：m1 是 克/天，m2、m3 是 公斤/年；目标钉成 t/day
        f1, _ = Q.convert_factor("g/day", "t/day")
        f2, _ = Q.convert_factor("kg/year", "t/day")
        self.assertAlmostEqual(f1 * 1e6, 1.0, places=12)
        self.assertAlmostEqual(f2 * 365250, 1.0, places=12)
        self.assertAlmostEqual(64.785611753720574e6 * f1, 64.79, places=2)
        self.assertIn("cannot be converted", Q.convert_factor("kg", "t/day")[1])

    def test_errors_are_strings(self):
        for t in ("", "kg/", "kg ** (", "@@"):
            with self.subTest(t=t):
                q, err = Q.parse_unit(t)
                self.assertIsNone(q)
                self.assertTrue(err)


if __name__ == "__main__":
    unittest.main()

"""v2.5.4（N17）：假设的 unit 里带 % 的都按百分数换算（assumptions.is_pct），百分点 / 基点不换算；unit 原文保留用于显示；
compute.restated_point 的假设一侧用同一个判断（点一侧不变）。例子取自韩国 8 月出生题（fc_kr_births_2026_08/showcase1）第 2 轮的 a2：
unit 是 "% of annual live births"，以前不是精确的 "%"，没有除以 100（p10_used / p90_used = 5.93 / 11.87，大 100 倍）。
不调模型、不联网。"""
import math
import unittest

from triangulate.agent import assumptions as AS
from triangulate.agent import compute as C
from triangulate.agent import discrete as D

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

TARGET = {"what": "Number of live births in South Korea during August 2026", "unit": "live births (persons)",
          "period_start": "2026-08-01", "period_end": "2026-08-31"}


def A(**kw):
    """showcase1 第 2 轮的 a2（文字字段截短）。"""
    base = {"id": "a2", "name": "August share of 2026 annual live births", "value": 8.4, "low": 8.0, "high": 8.8,
            "unit": "% of annual live births", "rationale": "August accounted for 8.4% of 2024 annual births (p73)",
            "applies_when": "the August seasonal share remains near its recent level",
            "falsified_by": "a 2025 or 2026 August share materially outside 8.0-8.8%", "route": "m2"}
    base.update(kw)
    return base


def _pt(pid, value, unit, period_start="2025-01-01", period_end="2025-12-31", keep=True):
    return {"id": pid, "value": value, "unit": unit, "period_start": period_start, "period_end": period_end, "keep": keep,
            "name": "x", "direction_id": "d1"}


class TestIsPct(unittest.TestCase):
    def test_percent_units(self):
        for u in ("%", "percent", "Percent", "per cent", "pct", "PCT", "percentage", "percent (%)",
                  "% of annual live births", "percent of annual live births", "percentage of GDP", "share (%)"):
            self.assertTrue(AS.is_pct(u), u)

    def test_points_and_other_units_are_not_percent(self):
        for u in ("percentage points", "percentage point", "pp", "p.p.", "bp", "bps", "basis points", "ratio",
                  "live births (persons)", "percentile", "per 1,000 population", "", None):
            self.assertFalse(AS.is_pct(u), u)

    def test_same_patterns_as_discrete(self):
        # 和离散模式（discrete.PCT_UNIT / CHANGE_UNIT）同一套写法；两边改了一边，这里会失败
        self.assertEqual((AS.PCT_RE.pattern, AS.PCT_RE.flags), (D.PCT_UNIT.pattern, D.PCT_UNIT.flags))
        self.assertEqual((AS.PCT_CHANGE_RE.pattern, AS.PCT_CHANGE_RE.flags), (D.CHANGE_UNIT.pattern, D.CHANGE_UNIT.flags))


class TestValidatePercent(unittest.TestCase):
    def test_percent_of_something_is_divided_by_100(self):
        a = AS.validate([A(value=8, low=6, high=11)], TARGET)["kept"][0]
        self.assertEqual(a["unit"], "% of annual live births")   # 原文保留，不改写成 "%"
        self.assertTrue(a["is_pct"])
        self.assertEqual((a["value"], a["low"], a["high"]), (8, 6, 11))   # 裁判给的值照原样记
        # 换算到 0.06 / 0.11 之后再套区间下限（11 / 6 < MIN_WIDTH，按几何中心放宽到 2 倍）
        c = math.sqrt(0.06 * 0.11)
        self.assertTrue(a["widened_by_floor"])
        self.assertAlmostEqual(a["p10_used"], c / math.sqrt(AS.MIN_WIDTH))
        self.assertAlmostEqual(a["p90_used"], c * math.sqrt(AS.MIN_WIDTH))
        self.assertTrue(0.05 < a["p10_used"] < 0.06 and 0.11 < a["p90_used"] < 0.12, (a["p10_used"], a["p90_used"]))
        # 和写成精确 "%" 的同一条假设完全一样
        b = AS.validate([A(value=8, low=6, high=11, unit="%")], TARGET)["kept"][0]
        self.assertEqual((a["p10_used"], a["p90_used"], a["is_pct"]), (b["p10_used"], b["p90_used"], b["is_pct"]))

    def test_wide_range_not_widened(self):
        lo, hi, widened = AS.effective_range(A(value=8, low=6, high=13))
        self.assertFalse(widened)
        self.assertAlmostEqual(lo, 0.06)
        self.assertAlmostEqual(hi, 0.13)

    def test_percentage_points_not_converted(self):
        for u in ("percentage points", "pp", "bp"):
            a = AS.validate([A(name="change in the August share of annual births", unit=u, value=0.2, low=0.1, high=0.4)],
                            TARGET)["kept"][0]
            self.assertEqual(a["unit"], u)
            self.assertFalse(a["is_pct"], u)
            self.assertEqual((a["p10_used"], a["p90_used"]), (0.1, 0.4), u)

    def test_exact_units_still_normalised(self):
        ref = AS.validate([A()], TARGET)["kept"][0]
        for u in ("%", "percent", "Per cent", "PCT", "percentage", "percent (%)"):
            a = AS.validate([A(unit=u)], TARGET)["kept"][0]
            self.assertEqual(a["unit"], "%", u)
            self.assertTrue(a["is_pct"], u)
            self.assertEqual((a["p10_used"], a["p90_used"]), (ref["p10_used"], ref["p90_used"]), u)

    def test_formula_gets_a_fraction(self):
        # showcase1 第 2 轮 m2 的写法：年度总数 × 8 月占比。以前 a2 按 8.4 采样，结果大 100 倍
        pts = {"p9": _pt("p9", 250000.0, "live births (persons)")}   # 测试用的年度总数
        av = AS.validate([A()], TARGET)
        out = C.run([{"method": "formula_mc", "params": {"formula": "t * s", "inputs": {"t": {"id": "p9"}, "s": {"id": "a2"}}}}],
                    pts, TARGET, assumptions=av)
        m = out["methods"][0]
        self.assertNotIn("error", m, m)
        self.assertTrue(0.06 * 250000 < m["estimate"] < 0.11 * 250000, m["estimate"])
        a_in = next(d for d in m["inputs_detail"] if d["id"] == "a2")
        self.assertEqual(a_in["unit"], "% of annual live births")
        self.assertLess(a_in["p90"], 1)


class TestRestatedPoint(unittest.TestCase):
    def test_percent_assumption_vs_percent_point(self):
        # 假设一侧用 is_pct：「% of annual live births」和 unit 为 "%" 的点同值就是复述（以前 a 不是 "%"，对不上）
        self.assertEqual(C.restated_point(A(), {"p73": _pt("p73", 8.4, "%")}), "p73")
        self.assertEqual(C.restated_point(A(unit="%"), {"p73": _pt("p73", 8.4, "%")}), "p73")

    def test_point_side_rule_unchanged(self):
        # 点一侧仍是 unit == "%"；不是 "%" 的点照旧比单位词干（和以前相同）
        self.assertEqual(C.restated_point(A(), {"p73": _pt("p73", 8.4, "percent of annual live births")}), "p73")
        self.assertEqual(C.restated_point(A(), {"p1": _pt("p1", 8.4, "percentage points")}), "")
        self.assertEqual(C.restated_point(A(unit="percentage points"), {"p1": _pt("p1", 8.4, "%")}), "")
        # discrete7：a2「降息概率」2 %，p31「核心 CPI 三个月年化」2.0 percent，不是复述（点也用 is_pct 就会误判）
        cut = A(name="Probability the next meeting cuts the target range", unit="%", value=2, low=1, high=4)
        self.assertEqual(C.restated_point(cut, {"p31": _pt("p31", 2.0, "percent")}), "")

    def test_non_percent_rules_unchanged(self):
        r = A(name="August-to-July ratio", unit="ratio", value=1.0, low=0.9, high=1.1)
        self.assertEqual(C.restated_point(r, {"p1": _pt("p1", 1.0, "day of month")}), "")
        self.assertEqual(C.restated_point(r, {"p1": _pt("p1", 1.0, "ratio")}), "p1")
        self.assertEqual(C.restated_point(r, {"p1": _pt("p1", 1.0, "ratio", keep=False)}), "")


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestDisplayKeepsUnitText(unittest.TestCase):
    """终稿的 Key assumptions：is_pct 只决定换算，unit 原文照写；精确 "%" 的显示不变。"""

    @staticmethod
    def _render(a):
        from triangulate.agent import graph as G
        text = G.key_assumptions_template([dict(a, used_by=["m2"])], 2026)
        for k, v in G.assumption_placeholders(a).items():
            text = text.replace(f"[[{k}]]", v)
        return text

    def test_percent_of_something(self):
        a = AS.validate([A()], TARGET)["kept"][0]
        line = self._render(a).splitlines()[1]
        self.assertIn("% of annual live births", line)
        self.assertIn("- a2 August share of 2026 annual live births: 8.4 % of annual live births, range 5.933 to 11.87 "
                      "(range widened by code); used by m2.", line)
        # 和 showcase1 存的 a2（旧代码：is_pct False，p10_used / p90_used 没除以 100）显示的文字完全一样
        saved = dict(a, is_pct=False, p10_used=5.932958789676531, p90_used=11.865917579353063)
        self.assertEqual(self._render(saved), self._render(a))

    def test_exact_percent_unchanged(self):
        a = AS.validate([A(unit="%")], TARGET)["kept"][0]
        line = self._render(a).splitlines()[1]
        self.assertIn(": 8.4%, range 5.933% to 11.87% (range widened by code); used by m2.", line)


if __name__ == "__main__":
    unittest.main()

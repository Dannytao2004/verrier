"""v2.7c：钉了单位时，formula_mc 声明「公式结果的单位」，代码换算到目标单位；观测点的 % 单位除以 100。
夹具来自披萨题（results/agent/ask_3e7f14f7/web_20261017T072118Z）和韩国出生题的「年总量 / 12」写法；假设用 low = high = value，
采样中位数就是 value，期望值可以手算。"""
import unittest

from triangulate.agent import assumptions as A
from triangulate.agent import compute as C


def target(unit_canonical=None, unit="pizza mass per day", ps="2026-01-01", pe="2026-12-31"):
    t = {"what": "pizza eaten per day in Chicago", "unit": unit, "period_start": ps, "period_end": pe, "outcome_type": "continuous"}
    if unit_canonical:
        t["unit_canonical"] = unit_canonical
    return t


def pt(pid, value, unit):
    return pid, {"id": pid, "name": pid, "value": value, "unit": unit, "keep": True, "period_start": "2025-01-01", "period_end": "2025-12-31"}


def asm(aid, value, unit, name):
    return {"id": aid, "name": name, "value": value, "low": value, "high": value, "unit": unit, "rationale": "fixture"}


PTS = dict([pt("p84", 11.0, "% of population"), pt("p18", 77.0, "grams per slice"), pt("p64", 50.1e9, "USD"),
            pt("p21", 254500.0, "live births")])
RAW_A = [asm("a1", 2.7e6, "people", "Chicago population"), asm("a2", 1.15, "ratio", "Chicago adjustment factor"),
         asm("a3", 2.5, "slices per eater-day", "slices per pizza eater per day"), asm("a4", 0.008, "share", "Chicago share of US"),
         asm("a5", 18.0, "USD per pizza", "average price per pizza"), asm("a6", 1.0, "kg per pizza", "mass per pizza"),
         asm("a7", 1.08, "ratio (this year / last year)", "July 2026 growth factor of births")]


def m1(unit=None):
    m = {"id": "m1", "method": "formula_mc", "params": {"formula": "a * b * c * d * e", "inputs": {
        "a": {"id": "p84", "role": "share eating pizza on a day"}, "b": {"id": "a3", "role": "slices per eater per day"},
        "c": {"id": "p18", "role": "grams per slice"}, "d": {"id": "a1", "role": "Chicago population"},
        "e": {"id": "a2", "role": "Chicago adjustment"}}}}
    if unit is not None:
        m["unit"] = unit
    return m


def m2(unit=None):
    m = {"id": "m2", "method": "formula_mc", "params": {"formula": "a * b / c * d", "inputs": {
        "a": {"id": "p64", "role": "US restaurant pizza revenue in 2024"}, "b": {"id": "a4", "role": "Chicago share"},
        "c": {"id": "a5", "role": "price per pizza"}, "d": {"id": "a6", "role": "kg per pizza"}}}}
    if unit is not None:
        m["unit"] = unit
    return m


def run(methods, t):
    return C.run(methods, PTS, t, assumptions=A.validate(RAW_A, t))


class TestMethodUnit(unittest.TestCase):
    def test_pizza_routes_convert_to_tonnes_per_day(self):
        t = target("t/day")
        r = run([m1("g/day"), m2("kg/year")], t)
        e1, e2 = (x["estimate"] for x in r["methods"])
        self.assertAlmostEqual(e1 / (0.11 * 2.5 * 77 * 2.7e6 * 1.15 / 1e6), 1, delta=0.02)   # 约 65.7 t/day；% of population 除以了 100
        self.assertAlmostEqual(e2 / (50.1e9 * 0.008 / 18 * 1.0 / 365.25 / 1e3), 1, delta=0.02)   # 约 61.0 t/day；年换成天
        self.assertEqual(r["methods"][1]["unit_check"]["unit"], "kg/year")
        self.assertAlmostEqual(r["methods"][1]["unit_check"]["factor"] * 365250, 1, places=9)

    def test_missing_or_wrong_unit_is_a_method_error(self):
        r = run([m1(), m2("kg")], target("t/day"))
        self.assertIn('give the method a "unit"', r["methods"][0]["error"])
        self.assertIn("cannot be converted", r["methods"][1]["error"])

    def test_annual_total_over_twelve_is_not_inflated(self):
        # 韩国出生：月目标钉成 birth，「年出生数 / k_months_per_year × 增长」照旧是普通数字的写法，不会悄悄大 12 倍
        t = target("birth", unit="live births", ps="2026-07-01", pe="2026-07-31")
        m = {"id": "m1", "method": "formula_mc", "unit": "birth", "params": {"formula": "a / k * g", "inputs": {
            "a": {"id": "p21", "role": "2025 live births"}, "k": {"id": "k_months_per_year", "role": "months per year"},
            "g": {"id": "a7", "role": "growth factor"}}}}
        e = run([m], t)["methods"][0]["estimate"]
        self.assertAlmostEqual(e / (254500 / 12 * 1.08), 1, delta=0.02)

    def test_percent_target_keeps_percent_points(self):
        # 目标本身是百分数（利率）：观测点的 percent 不除以 100
        pts = dict([pt("p1", 4.0, "percent")])
        t = {"what": "policy rate", "unit": "percent", "unit_canonical": "percent", "period_start": "2026-10-28",
             "period_end": "2026-10-28", "outcome_type": "continuous"}
        m = {"id": "m1", "method": "formula_mc", "unit": "percent", "params": {"formula": "a", "inputs": {"a": {"id": "p1", "role": "rate"}}}}
        r = C.run([m], pts, t, assumptions={"kept": [], "rejected": []})
        self.assertAlmostEqual(r["methods"][0]["estimate"], 4.0, delta=0.1)

    def test_legacy_target_without_unit_canonical_is_unchanged(self):
        # 没钉单位（已存的运行都是这样）：不要求 unit，不换算；'% of population' 也照旧不除以 100
        r = run([m1()], target())
        x = r["methods"][0]
        self.assertNotIn("unit_check", x)
        self.assertAlmostEqual(x["estimate"] / (11 * 2.5 * 77 * 2.7e6 * 1.15), 1, delta=0.02)


if __name__ == "__main__":
    unittest.main()

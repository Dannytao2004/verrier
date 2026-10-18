"""v2.8r：一个点的数和单位必须成对（XBRL「金额以元为单位」、SDMX UNIT_MEASURE 不含倍数）：代码乘过倍数，unit 里就不能再有；
倍数只写在 unit 里、原文有依据时挪到数上。unit 写法来自已存运行的普查（results/agent/*/*/state.json）。"""
import unittest
from datetime import date

from triangulate.agent import evidence as ev
from triangulate.agent.pipeline import verify_point

PAGE = ev.norm("2024 年度报告 单位：万元 币种：人民币\n| 外贸模式 | 4,774.13 | 4,513.39 | 5.78 |\n"
               "2024 turnover reached £5.2 million. 2024 exports were 36 in the table. Births per 1,000 women in 2024: 1.2.")


PLAIN = ev.norm("2024 exports were 36 in the table.")   # 没有表头


def vp(vw, quote, unit, sw="", page=PAGE, **kw):
    raw = {"name": "x", "value_as_written": vw, "scale_word": sw, "unit": unit, "period_start": "2024-01-01",
           "period_end": "2024-12-31", "quote": quote, **kw}
    return verify_point(raw, page, date(2026, 10, 18), None, False)


class TestStripUnitMultiplier(unittest.TestCase):
    def test_census_units(self):
        cases = {("万元 (10,000 CNY)", 1e4): "元 (CNY)", ("万元 RMB", 1e4): "元 RMB",
                 ("liters (万升 = ten-thousand liters)", 1e4): "liters (升 = liters)",
                 ("passengers (terminal passengers, thousands)", 1e3): "passengers (terminal passengers)",
                 ("USD (ten-thousand)", 1e4): "USD", ("CNY yuan (100 million)", 1e8): "CNY yuan",
                 ("亿元 (100 million yuan) vinegar series revenue", 1e8): "元 (yuan) vinegar series revenue",
                 ("CNY (亿元)", 1e8): "CNY (元)", ("万 (10,000) followers", 1e4): "followers", ("USD million", 1e6): "USD",
                 ("visitors (万人 = ten thousand people)", 1e4): "visitors (人 = people)",
                 ("births per 1,000 women", 1e3): "births per 1,000 women"}
        for (u, f), want in cases.items():
            self.assertEqual(ev.strip_unit_multiplier(u, f), (want, ""), u)
        self.assertIn("different multiplier", ev.strip_unit_multiplier("亿元", 1e4)[1])

    def test_rates_and_si_prefixes_are_not_multipliers(self):
        for u in ("births per 1,000 women", "births per thousand population", "pizza restaurants per 100,000 residents",
                  "per thousand (crude birth rate)", "beds per 10,000 people", "每万人床位数", "kg", "千克", "bottles (1000 ml)", "km per year"):
            self.assertEqual(ev.unit_multipliers(u), [], u)
        self.assertEqual([f for _, f in ev.unit_multipliers("£ million")], [1e6])
        self.assertEqual([f for _, f in ev.unit_multipliers("ten thousand USD (万美元)")], [1e4, 1e4])


class TestVerifyPointPairing(unittest.TestCase):
    Q = "| 外贸模式 | 4,774.13 | 4,513.39 | 5.78 |"

    def test_multiplied_value_gets_a_plain_unit(self):
        # 恒顺 v2.8p 的 p1：表头「单位：万元」，scale_word 万，unit 又写了万元
        p, why = vp("4,774.13", self.Q, "万元 (10,000 CNY)", sw="万")
        self.assertEqual(why, "")
        self.assertEqual((p["value"], p["unit"], p["unit_as_written"]), (47741300.0, "元 (CNY)", "万元 (10,000 CNY)"))

    def test_multiplier_only_in_the_unit_moves_onto_the_number(self):
        # 同一个数，抽取员没填 scale_word、只在 unit 里写了万元：表头有「单位：万元」，挪到数上，结果和上面相同
        p, _ = vp("4,774.13", self.Q, "万元 (10,000 CNY)")
        self.assertEqual((p["value"], p["unit"], p["scale_word"], p["scale_basis"]), (47741300.0, "元 (CNY)", "万", "page_header"))
        p, _ = vp("5.2", "2024 turnover reached £5.2 million.", "£ million")
        self.assertEqual((p["value"], p["unit"], p["scale_word"]), (5.2e6, "£", "million"))

    def test_unsupported_unit_multiplier_is_left_alone(self):
        # 原文和表头都没有「万」：不挪，照旧（数和单位本身是一对）
        p, _ = vp("36", "2024 exports were 36 in the table.", "ten thousand USD", page=PLAIN)
        self.assertEqual((p["value"], p["unit"]), (36.0, "ten thousand USD"))
        self.assertNotIn("unit_as_written", p)

    def test_conflicting_multipliers_drop_the_point(self):
        _, why = vp("4,774.13", self.Q, "亿元", sw="万")
        self.assertIn("unit: unit '亿元' names a different multiplier", why)

    def test_rates_and_percent_unchanged(self):
        p, _ = vp("1.2", "Births per 1,000 women in 2024: 1.2.", "births per 1,000 women")
        self.assertEqual((p["value"], p["unit"]), (1.2, "births per 1,000 women"))
        self.assertNotIn("unit_as_written", p)
        p, _ = vp("5.78", self.Q, "percent growth")
        self.assertEqual(p["unit"], "percent growth")


if __name__ == "__main__":
    unittest.main()

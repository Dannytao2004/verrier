"""v2.8o：value_as_written 照抄原文写法（单词、分数、区间），抽取员另给 number / low / high；算之前模型逐个核对。
夹具的原文来自披萨题抓到的 USDA FSRG Dietary Data Brief No. 62（NHANES 2017-March 2020）。"""
import unittest
from datetime import date

from triangulate.agent import assumptions as A
from triangulate.agent import compute as C
from triangulate.agent import evidence as ev
from triangulate.agent import value_check as VC
from triangulate.agent.pipeline import verify_point

PAGE = ev.norm("What We Eat in America, NHANES 2017-March 2020 Prepandemic. "
               "On any given day, pizza was consumed by 11% of the population overall (data not shown). "
               "Overall, males had four and females had three slices of pizza (see definition of a slice, p.8) at an eating "
               "occasion (P<0.001). One slice of pizza is approximately 1/6 of 14-inch fast food/restaurant cheese pizza with a "
               "regular crust. An estimated 3-4 slices are eaten per occasion by adolescents, and fourteen percent of eaters "
               "had pizza twice. Sales reached two million pies in 2019. 共三百五十家门店。")


def raw(vw, quote, **kw):
    return {"name": "x", "value_as_written": vw, "unit": kw.pop("unit", "slices"), "period_start": "2017-01-01",
            "period_end": "2020-03-31", "quote": quote, **kw}


def vp(r):
    return verify_point(r, PAGE, date(2026, 10, 18), None, False)


class TestFindValueWords(unittest.TestCase):
    def test_word_boundaries(self):
        q = ev.norm("fourteen percent of someone's four slices; 共三百五十家, 两万三千人")
        self.assertEqual(ev.find_value(q, "four"), q.index("four slices"))   # 不从 fourteen 里匹配
        self.assertEqual(ev.find_value(q, "one"), -1)                        # 不从 someone 里匹配
        self.assertEqual(ev.find_value(q, "三百"), -1)                        # 三百五十 的一截
        self.assertEqual(ev.find_value(q, "两万"), -1)                        # 两万三千 的一截
        self.assertGreaterEqual(ev.find_value(q, "三百五十"), 0)
        self.assertEqual(ev.find_value(ev.norm("2.9% vs 12.9%"), "2.9%"), 0)  # 数字写法照旧


class TestVerifyPointReading(unittest.TestCase):
    def test_number_words_are_kept_with_a_pending_check(self):
        q = "Overall, males had four and females had three slices of pizza"
        p, why = vp(raw("four", q, number=4))
        self.assertEqual(why, "")
        self.assertEqual((p["value"], p["reading"], p["value_check"]), (4.0, {"number": 4.0}, "pending"))
        p3, _ = vp(raw("three", q, number=3))
        self.assertEqual(p3["value"], 3.0)

    def test_fraction_percent_scale_word(self):
        p, _ = vp(raw("1/6", "One slice of pizza is approximately 1/6 of 14-inch fast food/restaurant cheese pizza", number=0.16667))
        self.assertAlmostEqual(p["value"], 0.16667)
        p, _ = vp(raw("11%", "pizza was consumed by 11% of the population overall", number=11, unit="share"))
        self.assertEqual((p["value"], p["unit"]), (11.0, "%"))
        p, _ = vp(raw("fourteen percent", "fourteen percent of eaters had pizza twice", number=14, unit="share"))
        self.assertEqual((p["value"], p["unit"]), (14.0, "%"))
        p, why = vp(raw("two million", "Sales reached two million pies in 2019", number=2, scale_word="million", unit="pies",
                        period_start="2019-01-01", period_end="2019-12-31"))
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 2e6, "quote"))
        p, _ = vp(raw("1/6", "approximately 1/6 of 14-inch", number="1/6"))   # 分数写成字符串也认，由代码除
        self.assertAlmostEqual(p["value"], 1 / 6)

    def test_range(self):
        p, why = vp(raw("3-4", "An estimated 3-4 slices are eaten per occasion by adolescents", low=3, high=4, number=None))
        self.assertEqual(why, "")
        self.assertEqual((p["value"], p["value_low"], p["value_high"], p["reading"]), (3.5, 3.0, 4.0, {"low": 3.0, "high": 4.0}))
        _, why = vp(raw("3-4", "An estimated 3-4 slices", low=3))
        self.assertIn("both low and high", why)
        _, why = vp(raw("3-4", "An estimated 3-4 slices", low=4, high=3))
        self.assertIn("low must be below high", why)

    def test_multiplier_is_applied_by_code(self):
        # 倍数词由代码定（scale_word 或写法末尾的），不交给核对模型（v2.8o 探针）
        q = "Sales reached two million pies in 2019"
        kw = dict(unit="pies", period_start="2019-01-01", period_end="2019-12-31")
        p, _ = vp(raw("two million", q, number=2, **kw))   # 抽取员漏写 scale_word：照写法里的 million 乘
        self.assertEqual(p["value"], 2e6)
        _, why = vp(raw("two million", q, number=2, scale_word="thousand", **kw))
        self.assertIn("scale conflict", why)
        cases = {("4.8 million", ""): ("4.8", 1e6), ("3409万元", ""): ("3409元", 1e4), ("两万", ""): ("两", 1e4),
                 ("三千", ""): ("三千", 1.0), ("1千", ""): ("1", 1e3), ("519万548", ""): ("519万548", 1.0),
                 ("$5bn", ""): ("$5", 1e9), ("4.8 m", ""): ("4.8 m", 1.0), ("4,774.10", "万"): ("4,774.10", 1e4),
                 ("four thousand two hundred", ""): ("four thousand two hundred", 1.0), ("11%", ""): ("11%", 1.0)}
        for (vw, sw), want in cases.items():
            self.assertEqual(ev.split_multiplier(vw, sw), want, vw)
        with self.assertRaises(ValueError):
            ev.split_multiplier("519万548", "万")

    def test_range_needs_a_range_in_the_written_form(self):
        _, why = vp(raw("fourteen percent", "fourteen percent of eaters had pizza twice", low=10, high=12, unit="share"))
        self.assertIn("not a range", why)

    def test_digits_are_parsed_by_code_not_read_by_the_model(self):
        # 用户 10-18 选的：阿拉伯数字照旧由代码解析，抽取员给的 number 不用，也不交给模型核对
        p, _ = vp(raw("11%", "pizza was consumed by 11% of the population overall", number=0.11, unit="share"))
        self.assertEqual((p["value"], p["unit"]), (11.0, "%"))
        self.assertNotIn("value_check", p)
        p, _ = vp(raw("two million", "Sales reached two million pies in 2019", number=2, unit="pies",
                      period_start="2019-01-01", period_end="2019-12-31"))
        self.assertEqual(p["value_check"], "pending")

    def test_bad_number_or_fragment_dropped(self):
        _, why = vp(raw("four", "Overall, males had four and females had three slices of pizza", number="four"))
        self.assertIn("not a plain number", why)
        _, why = vp(raw("four", "fourteen percent of eaters had pizza twice", number=4))
        self.assertEqual(why, "value_as_written not in quote as a whole number")
        _, why = vp(raw("三百", "共三百五十家门店。", number=300, unit="stores"))
        self.assertEqual(why, "value_as_written not in quote as a whole number")

    def test_without_number_the_code_parses_as_before(self):
        p, why = vp(raw("11%", "pizza was consumed by 11% of the population overall", unit="share"))
        self.assertEqual((why, p["value"], p["unit"]), ("", 11.0, "%"))
        self.assertNotIn("value_check", p)
        _, why = vp(raw("four", "Overall, males had four and females had three slices of pizza"))
        self.assertEqual(why, "number: no number in value_as_written")


def pt(pid, value, unit, **kw):
    return {"id": pid, "name": pid, "value": value, "unit": unit, "keep": True, "period_start": "2025-01-01",
            "period_end": "2025-12-31", **kw}


class TestRangeSampling(unittest.TestCase):
    def run_one(self, p, t_unit="slices"):
        t = {"what": "x", "unit": t_unit, "period_start": "2026-01-01", "period_end": "2026-12-31", "outcome_type": "continuous"}
        m = {"id": "m1", "method": "formula_mc", "params": {"formula": "a * b", "inputs": {
            "a": {"id": p["id"], "role": "r"}, "b": {"id": "a1", "role": "people"}}}}
        av = A.validate([{"id": "a1", "name": "people", "value": 1000, "low": 1000, "high": 1000, "unit": "people",
                          "rationale": "fixture"}], t)
        return C.run([m], {p["id"]: p}, t, assumptions=av)["methods"][0]

    def test_range_is_centred_on_the_midpoint_and_wider_than_a_point(self):
        r = self.run_one(pt("p1", 3.5, "slices", value_low=3.0, value_high=4.0))
        d = r["inputs_detail"][0]
        self.assertAlmostEqual(r["estimate"] / 3500, 1, delta=0.02)
        self.assertEqual((d["value"], d["low"], d["high"]), (3.5, 3.0, 4.0))
        s = self.run_one(pt("p2", 3.5, "slices"))["inputs_detail"][0]
        self.assertGreater(d["p90"] / d["p10"], s["p90"] / s["p10"])   # 区间均匀 x 点误差，比单个点宽
        w = self.run_one(pt("p3", 3.5, "slices", value_low=1.0, value_high=6.0))["inputs_detail"][0]
        self.assertGreater(w["p10"], 0)
        self.assertLess(w["p10"], 2.0)
        self.assertGreater(w["p90"], 5.0)

    def test_percent_range_is_divided_by_100(self):
        d = self.run_one(pt("p1", 11.0, "%", value_low=10.0, value_high=12.0), t_unit="pizza eaters")["inputs_detail"][0]
        self.assertAlmostEqual(d["value"], 0.11)
        self.assertAlmostEqual(d["low"], 0.10)
        self.assertAlmostEqual(d["high"], 0.12)


class FakeLLM:
    """value_check / value_reread 的假模型：checks、rereads 依次给出回复；None = 调用失败。"""

    def __init__(self, checks, rereads=()):
        self.checks, self.rereads, self.roles = list(checks), list(rereads), []

    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        self.roles.append(role)
        q = self.checks if role.startswith("value_check") else self.rereads
        x = q.pop(0)
        return (None, "transport: boom") if x is None else (x, None)


def reading_point(pid="p1", vw="four", reading=None, **kw):
    return {"id": pid, "name": "male slices per occasion", "value": 4.0, "value_as_written": vw, "scale_word": "",
            "unit": "slices", "quote": "Overall, males had four and females had three slices", "reading": reading or {"number": 4.0},
            "value_check": "pending", "keep": True, **kw}


JR = {"methods": [{"id": "m1", "method": "formula_mc", "params": {"formula": "a", "inputs": {"a": {"id": "p1", "role": "r"}}}}]}


class TestValueCheck(unittest.TestCase):
    def test_match_true(self):
        p, llm = reading_point(), FakeLLM([{"match": True}])
        self.assertEqual(VC.review(llm, "q", JR, [p]), [])
        self.assertEqual((p["value_check"], p["value"]), ("ok", 4.0))
        self.assertEqual(llm.roles, ["value_check:p1"])

    def test_false_then_reread_fixes_it(self):
        p = reading_point(value=40.0, reading={"number": 40.0})
        llm = FakeLLM([{"match": False}, {"match": True}], [{"number": 4, "low": None, "high": None}])
        self.assertEqual(VC.review(llm, "q", JR, [p]), [])
        self.assertEqual((p["value_check"], p["value"], p["reading"], p["reading_from_extractor"]),
                         ("ok", 4.0, {"number": 4.0}, {"number": 40.0}))
        self.assertEqual(llm.roles, ["value_check:p1", "value_reread:p1", "value_check:p1"])

    def test_reread_can_turn_a_number_into_a_range(self):
        p = reading_point(vw="3-4", value=3.5, reading={"number": 3.5}, quote="An estimated 3-4 slices")
        llm = FakeLLM([{"match": False}, {"match": True}], [{"number": None, "low": 3, "high": 4}])
        VC.review(llm, "q", JR, [p])
        self.assertEqual((p["value"], p["value_low"], p["value_high"]), (3.5, 3.0, 4.0))

    def test_still_wrong_after_three_rereads_is_removed(self):
        p = reading_point(value=40.0, reading={"number": 40.0})
        llm = FakeLLM([{"match": False}] * 4, [{"number": 40}] * 3)
        errs = VC.review(llm, "q", JR, [p])
        self.assertEqual(p["value_check"], "failed")
        self.assertEqual(len(p["value_check_tries"]), 4)
        self.assertIn("data point p1", errs[0])
        self.assertEqual(VC.usable([p]), [])
        self.assertEqual(VC.review(FakeLLM([]), "q", JR, [p]), errs)   # 再次 check：不再调用，原因照旧交给修正轮

    def test_call_failure_lets_the_point_through(self):
        p = reading_point()
        VC.review(FakeLLM([None]), "q", JR, [p])
        self.assertEqual(p["value_check"], "error")
        self.assertEqual(VC.usable([p]), [p])

    def test_only_used_pending_points_are_checked(self):
        used, unused = reading_point("p1"), reading_point("p2")
        code = {"id": "p3", "name": "c", "value": 1.0, "unit": "x"}   # 代码解析的点（没有 value_check）
        jr = {"methods": [{"id": "m1", "method": "formula_mc", "params": {"formula": "a * b", "inputs": {
            "a": {"id": "p1", "role": "r"}, "b": {"id": "p3", "role": "r"}}}}]}
        llm = FakeLLM([{"match": True}])
        VC.review(llm, "q", jr, [used, unused, code])
        self.assertEqual(llm.roles, ["value_check:p1"])
        self.assertEqual((used["value_check"], unused["value_check"]), ("ok", "pending"))
        self.assertNotIn("value_check", code)


if __name__ == "__main__":
    unittest.main()

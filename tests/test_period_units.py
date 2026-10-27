"""v2.13a（用户 10-26：单位带期间，「单位错，结果一定错」）：抽取时写计算用的单位 unit_calc（原文的 unit 照旧），裁判表格和
单位核对都看得到它；结果单位由代码按定下的输入单位推（unit_review.derive_unit，测试在 test_unit_review.py）；答案的单位写全。"""
import unittest
from datetime import date

from triangulate.agent import evidence as ev
from triangulate.agent import graph as G
from triangulate.agent import outputs as O
from triangulate.agent import unit_review as UR
from triangulate.agent.pipeline import verify_point

TEXT = "New registrations from January to April 2026: 948,567 passenger cars."
RAW = {"name": "Germany Pkw new registrations January-April 2026", "value_as_written": "948,567", "number": 948567,
       "scale_word": "", "unit": "new passenger car registrations", "unit_calc": "vehicle/(4 month)",
       "period_start": "2026-01-01", "period_end": "2026-04-30", "quote": TEXT}


class TestExtractedUnit(unittest.TestCase):
    def test_both_columns_kept(self):
        p, why = verify_point(RAW, ev.norm(TEXT), date(2026, 9, 5), date(2026, 5, 1), None)
        self.assertEqual(why, "")
        self.assertEqual((p["unit"], p["unit_calc"]), ("new passenger car registrations", "vehicle/(4 month)"))

    def test_missing_unit_calc_is_simply_absent(self):
        p, _ = verify_point({k: v for k, v in RAW.items() if k != "unit_calc"}, ev.norm(TEXT), date(2026, 9, 5), None, None)
        self.assertNotIn("unit_calc", p)


class TestShown(unittest.TestCase):
    P = {"id": "p75", "direction_id": "d1", "name": "Jan-Apr registrations", "value": 948567.0, "unit": "registrations",
         "unit_calc": "vehicle/(4 month)", "period_start": "2026-01-01", "period_end": "2026-04-30", "source_url": "https://kba.de/x",
         "via": "snapshot", "page_date": "2026-05-04", "quote": TEXT, "keep": True}

    def test_judge_table(self):
        rows = G._table([self.P]).splitlines()
        self.assertEqual(rows[0], "id | dir | name | value | unit | unit for computation | period | published | source | via | quote")
        self.assertTrue(rows[1].startswith("p75 | d1 | Jan-Apr registrations | 948,567 | registrations | vehicle/(4 month) | "))

    def test_unit_check_input_line(self):
        m_in = {"params": {"formula": "p75 * a2", "inputs": {"p75": {"id": "p75", "role": "Jan-Apr total"}}}}
        m_out = {"inputs_detail": [{"name": "p75", "id": "p75", "kind": "point", "p10": 790472.5, "p90": 1138280.4}]}
        line = UR.input_lines(m_in, m_out, {"p75": self.P}, {})[0]
        self.assertIn('"unit_as_recorded": "registrations", "unit_at_extraction": "vehicle/(4 month)"', line)


class TestAnswerUnit(unittest.TestCase):
    def test_unit_full(self):
        sep = {"unit": "new passenger car registrations", "unit_canonical": "vehicle", "period_start": "2026-09-01",
               "period_end": "2026-09-30"}
        self.assertEqual(O.unit_full(sep), "vehicle (new passenger car registrations; total for 2026-09-01 to 2026-09-30)")
        rate = {"unit": "tonnes of pizza per day", "unit_canonical": "t/day", "period_start": "2026-01-01", "period_end": "2026-12-31"}
        self.assertEqual(O.unit_full(rate), "t/day (tonnes of pizza per day; average over 2026-01-01 to 2026-12-31)")
        stock = {"unit": "job posting", "unit_canonical": "job posting", "period_start": "2026-10-26", "period_end": "2026-10-26"}
        self.assertEqual(O.unit_full(stock), "job posting (on 2026-10-26)")
        unpinned = {"unit": "widgets", "period_start": "2026-09-01", "period_end": "2026-09-30"}
        self.assertEqual(O.unit_full(unpinned), "widgets (for 2026-09-01 to 2026-09-30)")
        self.assertEqual(O.unit_full({}), "")




class TestSameThingSameUnit(unittest.TestCase):
    """v2.13a（用户 10-26：「月」和「月份」应该是同一个东西，别区分开）：复数、缩写、中文时间词都归到同一个单位。"""

    def test_aliases(self):
        from triangulate.agent import qty as Q
        same = [("months", "month"), ("persons", "person"), ("people", "person"), ("visit/mo", "visit/month"),
                ("person/annum", "person/year"), ("wk", "week"), ("vehicle/月", "vehicle/month"), ("person/月份", "person/month"),
                ("vehicle/(4 个月)", "vehicle/(4 month)"), ("person/年", "person/year"), ("t/天", "t/day")]
        for a, b in same:
            self.assertEqual(Q.convert_factor(a, b), (1.0, ""), a)
        self.assertEqual(Q.convert_factor("USD/quarter", "USD/year")[0], 4.0)   # 季度 = 3 个月（pint 的 quarter 是重量）
        self.assertEqual(Q.convert_factor("person/季度", "person/month")[0], 1 / 3)
        self.assertEqual(Q.convert_factor("headquarters", "headquarters"), (1.0, ""))   # 整词才换


class TestMergeSearches(unittest.TestCase):
    """v2.13b：一个方向几个搜索 agent 各搜各的，网址合并：被几次搜索找到的排前面。"""

    def test_votes_then_first_seen(self):
        from triangulate.agent.pipeline import merge_searches
        runs = [{"queries": ["q1"], "urls": ["a", "b", "c"], "web_search_requests": 2, "usd": 0.01, "usd_search_fee_assumed": 0.02},
                {"queries": ["q2"], "urls": ["c", "d", "a"], "web_search_requests": 3, "usd": 0.02, "usd_search_fee_assumed": 0.03},
                {"queries": [], "urls": [], "error": "http 500", "web_search_requests": 0}]
        m = merge_searches(runs, cap=3)
        self.assertEqual(m["urls"], ["a", "c", "b"])   # a、c 各 2 票（a 先出现），b 1 票先于 d
        self.assertEqual(m["url_votes"], {"a": 2, "c": 2, "b": 1, "d": 1})
        self.assertEqual((m["queries"], m["web_search_requests"], m["n_searches"]), (["q1", "q2"], 5, 3))
        self.assertAlmostEqual(m["usd"], 0.03)
        self.assertNotIn("error", m)   # 只有一次失败：不算整个方向失败
        self.assertEqual(merge_searches([{"urls": [], "error": "x"}] * 2, 4)["error"], "x")


if __name__ == "__main__":
    unittest.main()

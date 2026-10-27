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


if __name__ == "__main__":
    unittest.main()

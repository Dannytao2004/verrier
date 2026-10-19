"""forecast.report() 离线重打分要用每题的 answer_unit（2026-10-19：以前写死空单位，fc_ca_rail_2026_07 的 32,000,000 tonne、
fc_us_gen_2026_07 的 410,000 GWh 在运行时通过检查，重打分却成了 unit_unreconciled、估计值 None）。离线，不调模型。
"""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from triangulate import forecast


def _q(qid, unit, answer):
    return {"id": qid, "as_of": "2026-08-29", "released": "2026-09-28", "answer_value": answer, "last_year": answer,
            "source": "test", "question": f"Estimate the test quantity {qid}.", "answer_unit": unit, "strict": False}


def _raw(reply):
    return {"attempts": [{"attempt": 1, "reply": reply, "unparsed_text": None, "problems": []}], "final_attempt": 1}


def _inp(name, lo, hi, unit):
    return {"name": name, "description": name, "value": (lo * hi) ** 0.5, "low": lo, "high": hi, "unit": unit,
            "provenance": {"type": "assumption", "rationale": "test"}}


MASS_SPEC = {"target": {"definition": "freight carried", "unit": "tonne"},
             "inputs": [_inp("freight_t", 3.1e7, 3.3e7, "t"), _inp("freight_tonne", 3.0e7, 3.4e7, "tonne"),
                        _inp("freight_kg", 3.0e10, 3.4e10, "kg")],
             "paths": [{"id": "p1", "method": "top_down", "formula": "freight_t", "output_unit": "tonne"},
                       {"id": "p2", "method": "bottom_up", "formula": "freight_tonne", "output_unit": "tonne"},
                       {"id": "p3", "method": "proxy", "formula": "freight_kg", "output_unit": "kg"}]}


class TestReportUsesAnswerUnit(unittest.TestCase):
    def _report(self, questions, naive, structured):
        with tempfile.TemporaryDirectory() as d:
            fc, graphs = Path(d) / "forecast", Path(d) / "graphs"
            graphs.mkdir()
            for arm, replies in (("naive", naive), ("structured", structured)):
                for qid, reply in replies.items():
                    p = fc / "raw" / arm / f"{qid}.json"
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(json.dumps(_raw(reply)), encoding="utf-8")
            with mock.patch.object(forecast, "FC", fc), mock.patch.object(forecast, "GRAPHS", graphs), \
                    mock.patch.object(forecast, "QUESTIONS", questions):
                forecast.report()
            return {r["id"]: r for r in json.loads((fc / "summary.json").read_text(encoding="utf-8"))}

    def test_dimensioned_naive_answer_is_kept(self):
        rows = self._report([_q("rail", "tonne", 31686803), _q("gen", "GWh", 453744), _q("pax", "", 7180000)],
                            {"rail": {"estimate": 32000000.0, "unit": "tonne"},
                             "gen": {"estimate": 410, "unit": "TWh"},        # 换算进题目的单位，不是原样照抄
                             "pax": {"estimate": 7200000, "unit": ""}}, {})
        rail, gen, pax = rows["rail"]["naive"], rows["gen"]["naive"], rows["pax"]["naive"]
        self.assertEqual((rail["status"], rail["estimate"]), ("ok", 32000000.0))
        self.assertAlmostEqual(rail["pct_err"], 32000000 / 31686803 - 1)
        self.assertEqual(gen["status"], "ok")
        self.assertAlmostEqual(gen["estimate"], 410000.0)
        self.assertEqual((pax["status"], pax["estimate"]), ("ok", 7200000.0))   # 计数题（空单位）照旧

    def test_dimensioned_naive_answer_in_wrong_dimension_still_rejected(self):
        rows = self._report([_q("rail", "tonne", 31686803)], {"rail": {"estimate": 32000000.0, "unit": "GWh"}}, {})
        self.assertEqual((rows["rail"]["naive"]["status"], rows["rail"]["naive"]["estimate"]), ("unit_unreconciled", None))

    def test_dimensioned_structured_answer_is_kept(self):
        rows = self._report([_q("rail", "tonne", 31686803)], {}, {"rail": MASS_SPEC})
        s = rows["rail"]["structured"]
        self.assertEqual(s["n_valid_paths"], 3, s["remaining_errors"])
        self.assertEqual(s["remaining_errors"], [])
        self.assertTrue(3.0e7 < s["estimate"] < 3.4e7, s["estimate"])   # 以吨计；若按 kg 会是 ~3.2e10


if __name__ == "__main__":
    unittest.main()

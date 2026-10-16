"""展示集汇总（triangulate/showcase.py）：预注册成功标准的判定、失败记为无穷大、不读去年同月。离线。"""
import math
import unittest

from triangulate import showcase as SC


def row(kind, ans, **ests):
    arms = {}
    for k, e in ests.items():
        arms[k] = {"estimate": e, **SC._err(e, ans)}
    return {"kind": kind, "answer_value": ans, "arms": arms}


class TestCriteria(unittest.TestCase):
    def test_interim_with_unscored_live_questions(self):
        rows = [row("published", 100, agent=110, naive=150, structured=None),
                row("published", 200, agent=190, naive=210, structured=260),
                row("unpublished", None, agent=5, naive=5, structured=5, search_direct=None),
                row("unpublished", None, agent=5, naive=5, structured=5, search_direct=6)]
        c = SC.criteria(rows)
        self.assertEqual((c["n_scored"], c["final"], c["met"], c["c2_vs_search_direct_pass"]), (2, False, None, None))
        self.assertAlmostEqual(c["c1_agent_median_abs_pct_err"], 0.075)
        self.assertEqual(c["median_abs_log10"]["structured"], "inf")   # 一题没有估计：两题的中位数 = 无穷大
        self.assertEqual((c["c1_pass"], c["c2_vs_naive_structured_pass"]), (None, None))   # 没打完分：只报数，不判定

    def test_missing_agent_estimate_counts_as_failure(self):
        rows = [row("published", 100, agent=None, naive=150, structured=120),
                row("published", 100, agent=101, naive=150, structured=120),
                row("unpublished", 100, agent=None, naive=150, structured=120, search_direct=200)]
        c = SC.criteria(rows)
        self.assertEqual(c["c1_agent_median_abs_pct_err"], "inf")
        self.assertFalse(c["c1_pass"])
        self.assertFalse(c["c2_vs_naive_structured_pass"])

    def test_final_needs_both_criteria_and_search_direct(self):
        rows = [row("published", 100, agent=105, naive=150, structured=130),
                row("unpublished", 100, agent=95, naive=150, structured=130, search_direct=None)]
        c = SC.criteria(rows)
        self.assertEqual((c["final"], c["c1_pass"], c["c2_vs_naive_structured_pass"], c["c2_vs_search_direct_pass"], c["met"]),
                         (True, True, True, True, True))
        rows[1]["arms"]["search_direct"] = {"estimate": 99, **SC._err(99, 100)}
        c = SC.criteria(rows)
        self.assertEqual((c["c2_vs_search_direct_pass"], c["met"]), (False, False))

    def test_err(self):
        self.assertEqual(SC._err(None, 100), {"pct_err": None, "abs_log10_err": math.inf})
        self.assertEqual(SC._err(5, None), {})
        self.assertAlmostEqual(SC._err(110, 100)["pct_err"], 0.1)


class TestBuild(unittest.TestCase):
    def test_rows_cover_the_four_questions_without_last_year(self):
        d = SC.build()
        self.assertEqual([r["id"] for r in d["rows"]],
                         ["fc_nhs_ae_2026_09", "fc_jp_movers_2026_08", "fc_jnto_2026_09", "fc_kr_births_2026_08"])
        self.assertNotIn("last_year", str(d))
        live = [r for r in d["rows"] if r["kind"] == "unpublished"]
        self.assertTrue(all("search_direct" in r["arms"] and r["answer_value"] is None for r in live))
        self.assertTrue(all("search_direct" not in r["arms"] for r in d["rows"] if r["kind"] == "published"))


if __name__ == "__main__":
    unittest.main()

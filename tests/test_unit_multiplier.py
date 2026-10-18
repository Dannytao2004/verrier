"""v2.8q：代码已乘过倍数（scale_word 万 / million）的数据点，单位核对不能再乘一次。
夹具来自恒顺题 results/agent/ask_9b1539aa/v28p_test：p1「4,774.13」scale_word 万（表头「单位：万元」），value 47,741,300 元，
unit 记成 '万元 (10,000 CNY)'；裁定把它判成 '10000 CNY/year'，m1 = 69.5 亿瓶。"""
import json
import unittest

from triangulate.agent import unit_review as UR

P1 = {"id": "p1", "name": "Hengshun foreign trade (export) mode sales revenue, 2024", "value": 47741300.0,
      "value_as_written": "4,774.13", "scale_word": "万", "unit": "万元 (10,000 CNY)", "period_start": "2024-01-01",
      "period_end": "2024-12-31", "quote": "| 外贸模式 | 4,774.13 | 4,513.39 | 5.78 |"}
P2 = {"id": "p2", "name": "bottles per case", "value": 24.0, "value_as_written": "24", "scale_word": "", "unit": "bottles per case",
      "period_start": "2024-01-01", "period_end": "2024-12-31", "quote": "550ML@24"}
P3 = {"id": "p3", "name": "US share", "value": 11.0, "value_as_written": "11%", "scale_word": "", "unit": "%",
      "period_start": "2024-01-01", "period_end": "2024-12-31", "quote": "11%"}
BY_ID = {p["id"]: p for p in (P1, P2, P3)}
A2 = {"id": "a2", "name": "revenue per bottle", "value": 12.0, "unit": "CNY per bottle", "rationale": "fixture"}


def detail(pid, v):
    return {"name": pid, "id": pid, "kind": "point", "p10": v / 1.2, "p90": v * 1.2, "unit": BY_ID[pid]["unit"]}


def lines(*pids, values=None):
    vals = values or {"p1": 47741300.0, "p2": 24.0, "p3": 0.11}
    m_in = {"params": {"formula": " * ".join(pids), "inputs": {i: {"id": i, "role": "r"} for i in pids}}}
    m_out = {"inputs_detail": [detail(i, vals[i]) for i in pids]}
    return [json.loads(x) for x in UR.input_lines(m_in, m_out, BY_ID, {})]


class TestInputNote(unittest.TestCase):
    def test_multiplied_point_gets_a_note(self):
        x = lines("p1")[0]
        self.assertIn("code already multiplied it by 10,000", x["note"])
        self.assertIn("written as 4,774.13 with multiplier 万", x["note"])
        self.assertEqual(x["value_used"], 47741300.0)

    def test_other_points_unchanged(self):
        x2, x3 = lines("p2", "p3")
        self.assertNotIn("note", x2)                                     # 没有倍数：和以前逐字相同（没有 note）
        self.assertEqual(x3["note"], "recorded as 11 %; code divided it by 100, so the formula uses the fraction 0.11")
        self.assertEqual(UR._multiplier({"value_as_written": "4.8 million", "scale_word": ""}), 1e6)
        self.assertEqual(UR._multiplier({"value_as_written": "519万548", "scale_word": ""}), 1.0)   # 复合写法：整个数，没有倍数


class TestDoubledGuard(unittest.TestCase):
    def test_guard(self):
        m = {"p1": 1e4}
        reply = lambda u: {"inputs": [{"name": "p1", "unit": u}, {"name": "a2", "unit": "CNY/bottle"}]}
        self.assertIn("must not contain the factor 10000", UR._doubled(reply("10000 CNY/year"), m))
        self.assertEqual(UR._doubled(reply("CNY/year"), m), "")
        self.assertEqual(UR._doubled(reply("10000 CNY/year"), {}), "")                      # 没乘过倍数的点不查
        self.assertEqual(UR._doubled({"inputs": [{"name": "p1", "unit": "birth/(1000 person)"}]}, {"p1": 1e3}), "")
        self.assertIn("factor 1000", UR._doubled({"inputs": [{"name": "p1", "unit": "1000 birth/year"}]}, {"p1": 1e3}))

    def test_arbiter_is_asked_again(self):
        target = {"what": "bottles of Hengshun vinegar sold into the US", "unit": "bottle", "unit_canonical": "bottle",
                  "period_start": "2024-01-01", "period_end": "2024-12-31"}
        users = []

        class LLM:
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                users.append((role, user))
                if role.startswith("unit_check"):
                    return {"inputs": [], "derivation": "", "result_unit": "bottle/year", "declared_unit_matches": True}, None
                u, r = ("10000 CNY/year", "10000 bottle/year") if role.endswith(":1") else ("CNY/year", "bottle/year")
                return {"inputs": [{"name": "p1", "unit": u}, {"name": "a2", "unit": "CNY/bottle"}], "derivation": "",
                        "result_unit": r, "fit_reason": "a bottle count", "fits_target": True}, None
        m_in = {"unit": "bottle", "params": {"formula": "p1 / a2", "inputs": {"p1": {"id": "p1", "role": "r"}, "a2": {"id": "a2", "role": "r"}}}}
        m_out = {"label": "m1", "inputs_detail": [detail("p1", 47741300.0),
                                                  {"name": "a2", "id": "a2", "kind": "assumption", "p10": 6, "p90": 25, "unit": "CNY per bottle"}]}
        rec = UR.review_method(LLM(), "q", "m1", m_in, m_out, BY_ID, {"a2": A2}, target)
        self.assertIn("already multiplied", rec["arbiter"][0]["problem"])
        self.assertEqual(rec["arbiter"][1]["problem"], "")
        self.assertEqual((rec["unit"], rec["factor"]), ("(bottle/year) * 1 year", 1.0))
        self.assertIn("must not contain the factor 10000", users[-1][1])   # 第二次裁定的 prompt 带着问题


if __name__ == "__main__":
    unittest.main()

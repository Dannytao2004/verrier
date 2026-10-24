"""v2.12b（BUGS S66）：单位里写着倍数、代码没乘过的数据点，单位核对不能把倍数丢掉（_doubled 的反方向）。
夹具逐字来自两次真实运行：
- results/agent/fc_cn_profits_2026_09/test4：p1「52719.8」unit '亿元 (100 million CNY)'，scale_word 空（表格行里没有「亿」）；
  核对和裁定都把 p1 判成 'CNY'，m3 = p1 * (1 + a3) 出了 58,009「元」（应为约 5.8 万亿元）；
- results/agent/fc_us_retail_2026_06/test3：p6「763,705」unit 'millions of USD'，scale_word 空；裁定判成 'USD'，终稿 766,401 美元。"""
import json
import unittest

from triangulate.agent import unit_review as UR

P_CN = {"id": "p1", "name": "Cumulative total profits of China's industrial enterprises above designated size, Jan-Aug 2026 (table total)",
        "value": 52719.8, "value_as_written": "52719.8", "scale_word": "", "unit": "亿元 (100 million CNY)",
        "period_start": "2026-01-01", "period_end": "2026-08-31", "quote": "| 总计 | 930851.2 | 6.6 | 791893.6 | 6.1 | 52719.8 | 15.7 |"}
P_US = {"id": "p6", "name": "Seasonally adjusted total retail and food services sales, May 2026 (Table 1)", "value": 763705.0,
        "value_as_written": "763,705", "scale_word": "", "unit": "millions of USD", "period_start": "2026-05-01",
        "period_end": "2026-05-31", "quote": "total ......... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036"}
P_DONE = {"id": "p9", "name": "already multiplied", "value": 47741300.0, "value_as_written": "4,774.13", "scale_word": "万",
          "unit": "万元 (10,000 CNY)", "period_start": "2024-01-01", "period_end": "2024-12-31", "quote": "| 外贸模式 | 4,774.13 |"}
P_RATE = {"id": "p2", "name": "birth rate", "value": 6.4, "value_as_written": "6.4", "scale_word": "", "unit": "births per 1,000 women",
          "period_start": "2025-01-01", "period_end": "2025-12-31", "quote": "6.4"}
BY_ID = {p["id"]: p for p in (P_CN, P_US, P_DONE, P_RATE)}
A3 = {"id": "a3", "name": "Jan-Sep over Jan-Aug growth", "value": 0.1003, "unit": "1", "rationale": "fixture"}
TARGET = {"what": "Cumulative total profits of China's industrial enterprises above designated size, January-September 2026",
          "unit": "亿元 (100 million CNY)", "unit_canonical": "CNY", "period_start": "2026-01-01", "period_end": "2026-09-30"}


def detail(pid):
    v = BY_ID[pid]["value"]
    return {"name": pid, "id": pid, "kind": "point", "p10": v / 1.2, "p90": v * 1.2, "unit": BY_ID[pid]["unit"]}


class TestNamedMultiplier(unittest.TestCase):
    def test_which_points(self):
        self.assertEqual(UR._named_multiplier(P_CN), 1e8)
        self.assertEqual(UR._named_multiplier(P_US), 1e6)
        self.assertEqual(UR._named_multiplier(P_DONE), 1.0)    # 代码已乘过：归 _doubled 管
        self.assertEqual(UR._named_multiplier(P_RATE), 1.0)    # 比率的分母不是倍数
        self.assertEqual(UR._named_multiplier({"value_as_written": "5", "scale_word": "", "unit": "USD"}), 1.0)

    def test_input_note(self):
        m_in = {"params": {"formula": "p1 * p2", "inputs": {"p1": {"id": "p1", "role": "r"}, "p2": {"id": "p2", "role": "r"}}}}
        x1, x2 = [json.loads(x) for x in UR.input_lines(m_in, {"inputs_detail": [detail("p1"), detail("p2")]}, BY_ID, {})]
        self.assertIn("names the multiplier 100,000,000 and code did NOT multiply", x1["note"])
        self.assertIn("must carry the factor 100000000", x1["note"])
        self.assertNotIn("note", x2)                            # 其他点和以前逐字相同


class TestDroppedGuard(unittest.TestCase):
    def test_guard(self):
        reply = lambda u: {"inputs": [{"name": "p1", "unit": u}, {"name": "a3", "unit": "1"}]}
        named = {"p1": 1e8}
        self.assertIn("multiplier 100,000,000", UR._dropped(reply("CNY"), named))      # 真实回复：漏乘
        self.assertIn("multiplier 100,000,000", UR._dropped(reply("CNY/year"), named))
        self.assertEqual(UR._dropped(reply("100 million CNY"), named), "")   # 带了倍数；million 能不能换算归后面的换算检查
        self.assertEqual(UR._dropped(reply("100000000 CNY"), named), "")
        self.assertEqual(UR._dropped(reply("1e8 CNY"), named), "")
        self.assertEqual(UR._dropped(reply("CNY"), {}), "")                            # 单位里没有倍数的点不查
        self.assertIn("multiplier 1,000,000", UR._dropped({"inputs": [{"name": "p6", "unit": "USD"}]}, {"p6": 1e6}))
        self.assertEqual(UR._dropped({"inputs": [{"name": "p6", "unit": "1e6 USD/month"}]}, {"p6": 1e6}), "")
        self.assertIn("multiplier 1,000,000", UR._dropped({"inputs": [{"name": "p6", "unit": "USD/month"}]}, {"p6": 1e6}))
        # 倍数吸收进前缀是对的：v211g_reg 的 p32「4,408」billion kilowatthours 判成 'TWh'
        self.assertEqual(UR._dropped({"inputs": [{"name": "p32", "unit": "TWh"}]}, {"p32": 1e9}), "")
        # 倍数词留着、和另一个输入约掉是对的：test2_think 的 p7「1,004,412」million cubic feet × a1 GWh/(million cubic feet)
        self.assertEqual(UR._dropped({"inputs": [{"name": "p7", "unit": "million cubic feet"}]}, {"p7": 1e6}), "")
        self.assertIn("multiplier 1,000,000", UR._dropped({"inputs": [{"name": "p7", "unit": "ft**3"}]}, {"p7": 1e6}))


class LLM:
    """核对照真实回复给 'CNY'；裁定前 n_bad 次照真实回复给 'CNY'，之后改成带倍数的单位。"""
    def __init__(self, n_bad):
        self.n_bad, self.users = n_bad, []

    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        self.users.append((role, user))
        if role.startswith("unit_check"):
            return {"inputs": [{"name": "p1", "unit": "CNY"}], "derivation": "", "result_unit": "CNY", "declared_unit_matches": True}, None
        u = "CNY" if int(role.rsplit(":", 1)[1]) <= self.n_bad else "100000000 CNY"
        return {"inputs": [{"name": "p1", "unit": u}, {"name": "a3", "unit": "1"}], "derivation": "p1 * (1 + a3)",
                "result_unit": u, "fit_reason": "a CNY amount", "fits_target": True}, None


class TestArbiter(unittest.TestCase):
    M_IN = {"unit": "亿元 (100 million CNY)", "params": {"formula": "p1 * (1 + a3)",
                                                       "inputs": {"p1": {"id": "p1", "role": "r"}, "a3": {"id": "a3", "role": "r"}}}}
    M_OUT = {"label": "m3", "inputs_detail": [detail("p1"), {"name": "a3", "id": "a3", "kind": "assumption", "p10": 0.08, "p90": 0.12, "unit": "1"}]}

    def test_asked_again_then_fixed(self):
        llm = LLM(n_bad=1)
        rec = UR.review_method(llm, "q", "m3", self.M_IN, self.M_OUT, BY_ID, {"a3": A3}, TARGET)
        self.assertIn("did NOT multiply", rec["arbiter"][0]["problem"])
        self.assertEqual(rec["arbiter"][1]["problem"], "")
        self.assertEqual(rec["factor"], 1e8)                    # 58,009 × 1e8 ≈ 5.8e12 元
        self.assertIn("must carry that factor", llm.users[-1][1])

    def test_fails_instead_of_wrong_number(self):
        rec = UR.review_method(LLM(n_bad=UR.ARBITER_TRIES), "q", "m3", self.M_IN, self.M_OUT, BY_ID, {"a3": A3}, TARGET)
        self.assertNotIn("unit", rec)
        self.assertIn("did NOT multiply", rec["failure"])


if __name__ == "__main__":
    unittest.main()

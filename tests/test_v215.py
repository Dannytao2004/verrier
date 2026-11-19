"""v2.15：三方审计 + GPT 评估之后的五处小修（2026-11-19）。
a 报错里的数字格式；b 裁判 JSON 少右花括号时定点补上，补不好再关思考重问；c 百分数假设写成小数时交回确认；
d 量级闸门（和不联网直接问的粗估比，差 2 倍以上定向修正一次）；e 抽取每页上限 15 -> 30。"""
import json
import unittest
from unittest import mock

from triangulate import llm
from triangulate.agent import assumptions as AS
from triangulate.agent import graph as G
from triangulate.agent import pipeline as P


def _m(mid, est):
    return {"id": mid, "method": "formula_mc", "estimate": est}


class TestErrorNumberFormat(unittest.TestCase):
    """v2.15a：BCG 那次（11-12）0.069 被写成「0」，修正轮看不出是哪条路线小了几个数量级。"""

    def test_small_estimates_keep_their_digits(self):
        jr = {"methods": [_m("m1", 0.06934), _m("m2", 15043.2)]}
        out = {"methods": [_m("m1", 0.06934), _m("m2", 15043.2)]}
        _, probs = G._problems(jr, out, {"rejected": []}, {})
        text = "\n".join(probs)
        self.assertIn("m2 gives 15,043 but m1 gives 0.06934", text)
        self.assertNotIn("gives 0 ", text)

    def test_third_far_method_listed_with_digits(self):
        ms = [_m("m1", 0.06934), _m("m2", 15043.2), _m("m3", 101.4)]
        _, probs = G._problems({"methods": ms}, {"methods": ms}, {"rejected": []}, {})
        far = [p for p in probs if p.startswith("methods more than")]
        self.assertEqual(len(far), 1)
        self.assertIn("m1 (0.06934)", far[0])
        self.assertIn("m3 (101)", far[0])


GOOD = {"assessment": ["x"], "methods": [
    {"id": "m1", "method": "formula_mc", "params": {"formula": "a * b", "inputs": {"a": {"id": "p1"}, "b": {"id": "a1"}}},
     "rationale": "r1"},
    {"id": "m2", "method": "formula_mc", "params": {"formula": "c", "inputs": {"c": {"id": "p2"}}}, "rationale": "r2"}],
    "assumptions": [{"id": "a1", "value": 0.5}]}


class TestBraceRepair(unittest.TestCase):
    """v2.15b：存档里裁判 JSON 损坏、带出错片段的 24 次里 23 次是同一种坏法：方法对象在下一个 {"id": ...} 前少一个右花括号。"""

    def broken(self, drop: int):
        text = json.dumps(GOOD, ensure_ascii=False)
        cut = text.index(', {"id": "m2"')   # m1 的右花括号就在这前面
        return text[:cut - drop] + text[cut:] if drop else text

    def test_one_missing_brace(self):
        text = self.broken(1)
        with self.assertRaises(json.JSONDecodeError):
            json.loads(text)
        out, n = llm.close_missing_braces(text)
        self.assertEqual((out, n), (GOOD, 1))

    def test_two_missing_braces(self):
        # params 是 m1 的最后一个键：params 和 m1 本身的右花括号都没写
        good = {"methods": [{"id": "m1", "params": {"formula": "a", "inputs": {"a": {"id": "p1"}}}},
                            {"id": "m2", "params": {"formula": "b", "inputs": {"b": {"id": "p2"}}}}]}
        text = json.dumps(good)
        cut = text.index(', {"id": "m2"')
        out, n = llm.close_missing_braces(text[:cut - 2] + text[cut:])
        self.assertEqual((out, n), (good, 2))

    def test_compact_form_from_the_archive(self):
        # 存档 judge:r2 原样的交界没有空格：..."not clean."},{"id":"m3",...；少的是 m2 自己的右花括号
        good = {"methods": [{"id": "m2", "params": {"formula": "x"}, "rationale": "not clean."},
                            {"id": "m3", "params": {"formula": "y"}}]}
        text = json.dumps(good, separators=(",", ":"))
        bad = text.replace('"not clean."},{', '"not clean.",{')
        self.assertNotEqual(bad, text)
        out, n = llm.close_missing_braces(bad)
        self.assertEqual((out, n), (good, 1))

    def test_other_breakage_is_left_alone(self):
        # 抽取员那种坏法（多出一个孤立的 null 当键名）不是这一种：不修，照旧交给重问
        text = '{"points": [{"low": null, null: null, "high": null}]}'
        self.assertEqual(llm.close_missing_braces(text), (None, 0))
        self.assertEqual(llm.close_missing_braces('{"a": [1, 2,]}'), (None, 0))

    def test_json_call_returns_the_repaired_object(self):
        bad = self.broken(1)

        def fake_post(req, **k):
            reply = {"choices": [{"message": {"content": bad}, "finish_reason": "stop"}], "usage": {}}
            return 200, json.dumps(reply).encode()

        with mock.patch.object(llm, "read_key", return_value="k"),                 mock.patch.object(llm.LLM, "_post", staticmethod(fake_post)), mock.patch.object(llm.LLM, "_log") as log:
            out, _, err = llm.LLM().json_call([{"role": "user", "content": "json"}], arm="judge:r1", qid="q", attempt=1)
        self.assertIsNone(err)
        self.assertEqual(out, GOOD)
        rec = log.call_args[0][0]
        self.assertTrue(rec["ok"])
        self.assertEqual(rec["json_repaired"]["braces_inserted"], 1)
        self.assertIn("Expecting property name", rec["json_repaired"]["json_error"])


class TestThinkingOffRetry(unittest.TestCase):
    """v2.15b：补不好时，开了思考的调用重问那一次关思考；没开思考的照旧原样重问。"""

    def run_ask(self, thinking: dict, first_err: str):
        a = object.__new__(P.AgentLLM)
        a.budget, a.model = P.Budget(), "deepseek-flash"
        calls = []

        def fake_json_call(msgs, *, arm, qid, attempt, max_tokens, **kw):
            calls.append(kw.get("thinking_off", False))
            return (None, "{bad", first_err) if attempt == 1 else ({"ok": 1}, "{}", None)

        with mock.patch.object(llm, "THINKING", thinking), mock.patch.object(a, "json_call", fake_json_call):
            out, err = a.ask("s", "u", role="judge:r1", qid="q", max_tokens=1000)
        self.assertEqual(out, {"ok": 1})
        return calls

    def test_invalid_json_with_thinking_retries_with_thinking_off(self):
        self.assertEqual(self.run_ask({"judge": "high"}, "reply is not valid JSON"), [False, True])

    def test_thinking_off_already_is_unchanged(self):
        self.assertEqual(self.run_ask({}, "reply is not valid JSON"), [False, False])

    def test_other_errors_keep_thinking(self):
        self.assertEqual(self.run_ask({"judge": "high"}, "reply is not a JSON object"), [False, False])

    def test_off_payload(self):
        sent = {}

        def fake_post(req, **k):
            sent["body"] = json.loads(req.data)
            return 200, json.dumps({"choices": [{"message": {"content": "{}"}, "finish_reason": "stop"}],
                                    "usage": {}}).encode()

        with mock.patch.object(llm, "THINKING", {"judge": "high"}), mock.patch.object(llm, "read_key", return_value="k"),                 mock.patch.object(llm.LLM, "_post", staticmethod(fake_post)), mock.patch.object(llm.LLM, "_log") as log:
            llm.LLM().json_call([{"role": "user", "content": "j"}], arm="judge:r1", qid="q", attempt=2, max_tokens=1000,
                                thinking_off=True)
        self.assertEqual(sent["body"]["thinking"], {"type": "disabled"})
        self.assertEqual(sent["body"]["max_tokens"], 1000)
        self.assertTrue(log.call_args[0][0]["thinking_off_retry"])
        self.assertNotIn("thinking", log.call_args[0][0])



def _a(aid, value, unit, low=None, high=None, name="US share of North America headcount"):
    return {"id": aid, "name": name, "unit": unit, "rationale": "r", "value": value,
            "low": value * 0.9 if low is None else low, "high": value * 1.1 if high is None else high}


class TestPercentBelowOne(unittest.TestCase):
    """v2.15c：单位 % 的假设写成小于 1 的数，交回裁判写清是哪种意思（BCG 11-12：0.85 "%" 被当成 0.0085）。"""

    def test_bcg_case_goes_back_with_both_readings(self):
        r = AS.validate([_a("a5", 0.85, "%", 0.75, 0.92)], {"unit": "person"})
        self.assertEqual(r["kept"], [])
        why = r["rejected"][0]["reason"]
        self.assertIn("0.85% = 0.0085 as a fraction", why)
        self.assertIn('write value 85 with unit "%"', why)
        self.assertIn('(0.0085) with unit "1"', why)

    def test_both_rewrites_pass(self):
        r = AS.validate([_a("a5", 85, "%", 75, 92), _a("a6", 0.0085, "1", 0.007, 0.01)], {"unit": "person"})
        self.assertEqual([a["id"] for a in r["kept"]], ["a5", "a6"])
        self.assertAlmostEqual(r["kept"][0]["p10_used"] * r["kept"][0]["p90_used"], 0.75 * 0.92)

    def test_percent_one_or_more_and_percentage_points_unchanged(self):
        r = AS.validate([_a("a1", 1.0, "%"), _a("a2", 24.7, "percent"), _a("a3", 0.5, "percentage points", name="change")],
                        {"unit": "person"})
        self.assertEqual([a["id"] for a in r["kept"]], ["a1", "a2", "a3"])

    def test_repair_scope_names_only_that_assumption(self):
        r = AS.validate([_a("a5", 0.85, "%")], {"unit": "person"})
        err = f"assumption a5 rejected: {r['rejected'][0]['reason']}"
        self.assertEqual(G._repair_scope([err], [])[1], {"a5"})


if __name__ == "__main__":
    unittest.main()

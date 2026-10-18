"""v2.8e：单位核对（三个核对 + 一个裁定）。假模型，不联网；夹具照披萨 smoke2 的写法（人 × 千卡 ÷ 每 100 g 的千卡），
裁判把结果单位写成 t/day（错，公式给的是「每天多少个 100 g」）。"""
import threading
import unittest

from triangulate.agent import assumptions as A
from triangulate.agent import compute as C
from triangulate.agent import unit_review as UR

TARGET = {"what": "pizza eaten per day in Chicago", "unit": "metric tons per day", "unit_canonical": "t/day",
          "period_start": "2026-01-01", "period_end": "2026-12-31", "outcome_type": "continuous"}
PTS = [{"id": "p1", "name": "people eating pizza on a day", "value": 300000.0, "unit": "people", "keep": True,
        "period_start": "2025-01-01", "period_end": "2025-12-31", "quote": "300,000 people eat pizza on any given day"},
       {"id": "p2", "name": "energy from pizza per eater on the day", "value": 700.0, "unit": "kilocalories", "keep": True,
        "period_start": "2025-01-01", "period_end": "2025-12-31", "quote": "mean energy from pizza was 700 kilocalories"}]
RAW_A = [{"id": "a1", "name": "pizza energy density", "value": 250.0, "low": 250.0, "high": 250.0, "unit": "kcal per 100 g",
          "rationale": "fixture"}]


def method(unit="t/day", formula="a * b / c"):
    m = {"id": "m1", "method": "formula_mc", "params": {"formula": formula, "inputs": {
        "a": {"id": "p1", "role": "pizza eaters per day"}, "b": {"id": "p2", "role": "kcal per eater per day"},
        "c": {"id": "a1", "role": "kcal per 100 g"}}}}
    if unit is not None:
        m["unit"] = unit
    return m


class FakeLLM:
    """按 role 前缀回答：unit_check:* 用 checker，unit_arbiter:* 依次用 arbiter 列表里的回答（None = 调用失败）。"""

    def __init__(self, checker, arbiter):
        self.checker, self.arbiter, self.calls, self.lock = checker, list(arbiter), [], threading.Lock()

    def ask(self, system, user, *, role, qid, max_tokens):
        with self.lock:
            self.calls.append((role, user))
            if role.startswith("unit_check:"):
                return dict(self.checker), None
            out = self.arbiter.pop(0)
            return (None, "transport: boom") if out is None else (dict(out), None)


RIGHT = [{"name": "a", "reason": "...", "unit": "person/day"}, {"name": "b", "reason": "...", "unit": "kcal/person"},
         {"name": "c", "reason": "...", "unit": "kcal/(100 g)"}]
CHECK = {"inputs": RIGHT, "derivation": "person/day * kcal/person / (kcal/(100 g)) = 100 g/day", "result_unit": "100 g/day",
         "declared_unit_matches": False}


def arb(unit, fits=True, inputs=RIGHT):
    return {"inputs": inputs, "derivation": "...", "result_unit": unit, "fit_reason": "...", "fits_target": fits}


def trial(methods, target=TARGET):
    av = A.validate(RAW_A, target)
    out = C.run(methods, {p["id"]: p for p in PTS}, target, assumptions=av)
    failed = {i: (m.get("error") or "no estimate") for i, m in enumerate(out["methods"]) if not C.produced(m)}
    return out, av, failed


def review(llm, jr, target=TARGET):
    out, av, failed = trial(jr["methods"], target)
    return UR.review(llm, "q", jr, out, av, PTS, failed, target)


class TestUnitReview(unittest.TestCase):
    def test_arbiter_unit_replaces_the_judges_and_is_converted(self):
        jr = {"methods": [method("t/day")]}
        before = trial(jr["methods"])[0]["methods"][0]["estimate"]
        llm = FakeLLM(CHECK, [arb("100 g/day")])
        self.assertEqual(review(llm, jr), {})
        m = jr["methods"][0]
        self.assertEqual((m["unit"], m["unit_from_judge"]), ("100 g/day", "t/day"))
        after = trial(jr["methods"])[0]["methods"][0]["estimate"]
        self.assertAlmostEqual(after / before, 1e-4, places=9)   # 30 万人 × 700 kcal ÷ 250 kcal/100 g = 84 t/day
        self.assertAlmostEqual(after, 84.0, delta=84 * 0.05)
        roles = sorted(r for r, _ in llm.calls)
        self.assertEqual(roles, ["unit_arbiter:m1:1", "unit_check:m1:1", "unit_check:m1:2", "unit_check:m1:3"])
        rec = jr["unit_reviews"][0]["methods"][0]
        self.assertEqual(len(rec["checkers"]), 3)
        self.assertEqual(rec["checkers"][0]["converts_to_target"], "0.0001")
        self.assertIn('"converts_to_target": "0.0001"', [u for r, u in llm.calls if r.startswith("unit_arbiter")][0])

    def test_inputs_are_one_json_line_each_with_value_unit_and_description_apart(self):
        llm = FakeLLM(CHECK, [arb("100 g/day")])
        review(llm, {"methods": [method()]})
        user = [u for r, u in llm.calls if r == "unit_check:m1:1"][0]
        self.assertIn('{"name": "c", "kind": "analyst assumption", "value_used": 250.0, "unit_as_recorded": "kcal per 100 g", '
                      '"description": "pizza energy density"', user)
        self.assertIn('"unit_as_recorded": "kilocalories", "description": "energy from pizza per eater on the day"', user)
        self.assertIn("Result unit written by the analyst: t/day", user)

    def test_unconvertible_unit_is_retried_with_the_reason(self):
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [arb("100 g"), arb("100 g/day")])   # 漏了 per day：100 g 换不到 t/day，重来
        self.assertEqual(review(llm, jr), {})
        rec = jr["unit_reviews"][0]["methods"][0]
        self.assertIn("code cannot convert '100 g' to the target unit 't/day'", rec["arbiter"][0]["problem"])
        self.assertEqual(rec["arbiter"][1]["problem"], "")
        retry = [u for r, u in llm.calls if r == "unit_arbiter:m1:2"][0]
        self.assertIn("Your previous answer:", retry)
        self.assertIn('"result_unit": "100 g"', retry)
        self.assertEqual(jr["methods"][0]["unit"], "100 g/day")

    def test_no_fit_after_all_tries_fails_the_method(self):
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [arb("100 g/day", fits=False)] * UR.ARBITER_TRIES)
        fails = review(llm, jr)
        self.assertEqual(list(fails), [0])
        self.assertTrue(fails[0].startswith("unit check: the formula's result is '100 g/day'"))
        self.assertEqual(jr["methods"][0]["unit"], "t/day")   # 没定下单位：不改裁判写的
        self.assertEqual(len(jr["unit_reviews"][0]["methods"][0]["arbiter"]), UR.ARBITER_TRIES)

    def test_arbiter_call_failure_lets_the_method_through(self):
        jr = {"methods": [method()]}
        self.assertEqual(review(FakeLLM(CHECK, [None]), jr), {})
        self.assertEqual(jr["methods"][0]["unit"], "t/day")
        self.assertIn("error", jr["unit_reviews"][0]["methods"][0]["arbiter"][0])

    def test_missing_judge_unit_is_reviewed_and_rescued(self):
        jr = {"methods": [method(unit=None)]}
        self.assertTrue(trial(jr["methods"])[0]["methods"][0]["error"].startswith(UR.UNIT_ERRORS))
        self.assertEqual(review(FakeLLM(CHECK, [arb("100 g/day")]), jr), {})
        self.assertAlmostEqual(trial(jr["methods"])[0]["methods"][0]["estimate"], 84.0, delta=84 * 0.05)

    def test_unpinned_target_is_untouched(self):
        t = {k: v for k, v in TARGET.items() if k != "unit_canonical"}
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [])
        self.assertIsNone(review(llm, jr, t))
        self.assertEqual(llm.calls, [])
        self.assertNotIn("unit_reviews", jr)


if __name__ == "__main__":
    unittest.main()

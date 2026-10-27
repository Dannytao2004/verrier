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
        self.assertEqual((m["unit"], m["unit_from_judge"]), ("100 gram/day", "t/day"))   # v2.13a：由代码按输入单位推出
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
        # v2.13a：结果单位由代码按裁定的输入单位推出；输入 a 漏了 per day，推出来是 100 gram，换不到 t/day，重来
        no_day = [dict(RIGHT[0], unit="person")] + RIGHT[1:]
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [arb("100 g", inputs=no_day), arb("100 g/day")])
        self.assertEqual(review(llm, jr), {})
        rec = jr["unit_reviews"][0]["methods"][0]
        self.assertIn("code cannot convert '100 gram' (worked out by code from your input units) to the target unit 't/day'",
                      rec["arbiter"][0]["problem"])
        self.assertEqual(rec["arbiter"][1]["problem"], "")
        retry = [u for r, u in llm.calls if r == "unit_arbiter:m1:2"][0]
        self.assertIn("Your previous answer:", retry)
        self.assertIn('"result_unit": "100 g"', retry)
        self.assertEqual(jr["methods"][0]["unit"], "100 gram/day")

    def test_result_unit_is_worked_out_by_code_not_taken_from_the_arbiter(self):
        # v2.13a（德国新车探针）：裁定的推导漏了一个除数、result_unit 写错，代码按它自己定的输入单位重新推
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [arb("100 g/year")])   # 输入单位推出来是 100 g/day
        self.assertEqual(review(llm, jr), {})
        self.assertEqual(jr["methods"][0]["unit"], "100 gram/day")
        self.assertEqual(jr["unit_reviews"][0]["methods"][0]["arbiter"][0]["derived_unit"], "100 gram/day")

    def test_inputs_on_different_scales_cannot_be_added(self):
        d, err = UR.derive_unit("a + b", {"a": "person/year", "b": "person/month"})
        self.assertEqual(d, "")
        self.assertIn("different scales", err)
        self.assertEqual(UR.derive_unit("(a + b) * c", {"a": "person/year", "b": "person/year", "c": "year/month"})[0],
                         "person/month")
        self.assertIn("different kinds", UR.derive_unit("a + b", {"a": "person", "b": "kg"})[1])

    def test_period_units(self):   # v2.13a：总数带期间，份额是 (长期间)/(短期间)，代码换算
        sep = {"period_start": "2026-09-01", "period_end": "2026-09-30"}
        d = UR.derive_unit("p * k * a / k", {"p": "vehicle/(4 month)", "k": "month/year", "a": "year/month"})[0]
        self.assertEqual(UR.to_target(d, "vehicle", sep)[1], 3.0)   # 约掉的 k 不影响：1-4 月的数 x 3 x 份额
        d = UR.derive_unit("p * a", {"p": "person/year", "a": "year/month"})[0]
        self.assertEqual(UR.to_target(d, "person", sep)[1], 1.0)   # 全年总数 x 月份额 = 当月个数（S60 不再多除 12）

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

    def test_rate_for_a_period_total_target_is_multiplied_by_the_period(self):
        # v2.8j（恒顺题）：目标锁成 bottle（一年的瓶数），裁定给 1000 bottle/year：乘上 1 year 换算，不再判失败
        t = dict(TARGET, unit="bottles in 2024", unit_canonical="kg", period_start="2024-01-01", period_end="2024-12-31")
        jr = {"methods": [method("kg")]}
        per_year = [dict(RIGHT[0], unit="person/year")] + RIGHT[1:]   # v2.13a：结果单位由输入单位推出
        self.assertEqual(review(FakeLLM(CHECK, [arb("100 g/year", inputs=per_year)]), jr, t), {})
        self.assertEqual(jr["methods"][0]["unit"], "(100 gram/year) * 1 year")
        yearly = {"unit_canonical": "bottle", "period_start": "2024-01-01", "period_end": "2024-12-31"}
        self.assertEqual(UR.to_target("1000 bottle/year", "bottle", yearly)[:2], ("(1000 bottle/year) * 1 year", 1000.0))
        monthly = {"period_start": "2026-07-01", "period_end": "2026-07-31"}
        self.assertEqual(UR.to_target("birth/month", "birth", monthly)[1], 1.0)
        # 目标本身是速率时不乘：错单位不能凑成对的
        self.assertIsNone(UR.to_target("1000 cup/(year*day)", "cup/day", {"period_start": "2024-01-01", "period_end": "2025-10-17"})[1])

    def test_unpinned_target_is_untouched(self):
        t = {k: v for k, v in TARGET.items() if k != "unit_canonical"}
        jr = {"methods": [method()]}
        llm = FakeLLM(CHECK, [])
        self.assertIsNone(review(llm, jr, t))
        self.assertEqual(llm.calls, [])
        self.assertNotIn("unit_reviews", jr)


if __name__ == "__main__":
    unittest.main()

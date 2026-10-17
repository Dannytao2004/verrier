"""v2.7d：方法层的覆盖范围（UNITS_PLAN.md「覆盖范围」）。part 方法和缺部分的 sum 照算、不进合并（权重 0），交给修正轮；
sum 方法每个部分最多 3 个假设、整个方法最多 8 个。夹具是披萨题（results/agent/ask_3e7f14f7/web_20261017T072118Z）的字面值，
不读 results/：m1 消费侧、m2 餐馆营收、m3 冷冻披萨销售，钉成 t/day 后约 64.8 / 59.9 / 22.3；餐馆 + 冷冻一个公式 86.2，和 m1 合并 74.7。"""
import json
import re
import unittest

from triangulate.agent import assumptions as A
from triangulate.agent import compute as C
from triangulate.agent import methods as M
from triangulate.agent import outputs as O
from triangulate.agent.prompts import JUDGE_USER, METHODS_SPEC

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

TARGET = {"what": "pizza eaten per day in Chicago", "unit": "pizza mass per day", "unit_canonical": "t/day",
          "period_start": "2026-01-01", "period_end": "2026-12-31", "outcome_type": "continuous"}


def pt(pid, value, unit, ps="2024-01-01", pe="2024-12-31"):
    return pid, {"id": pid, "name": pid, "value": value, "unit": unit, "keep": True, "period_start": ps, "period_end": pe}


PTS = dict([pt("p84", 11.0, "% of population", "2017-01-01", "2020-03-31"), pt("p18", 77.0, "grams per slice", "", ""),
            pt("p64", 50.1e9, "USD"), pt("p60", 7e9, "USD")])


def asm(aid, name, value, low, high, unit):
    return {"id": aid, "name": name, "value": value, "low": low, "high": high, "unit": unit, "rationale": "fixture"}


RAW_A = [asm("a1", "Chicago city population, 2026", 2700000, 2550000, 2850000, "people"),
         asm("a2", "Chicago-vs-US pizza consumption adjustment factor", 1.15, 0.9, 1.5, "ratio"),
         asm("a3", "Average slices eaten per pizza-eating day per eater", 2.5, 1.5, 4.0, "slices per eater-day"),
         asm("a4", "Chicago share of US pizza restaurant revenue", 0.008, 0.005, 0.012, "share"),
         asm("a5", "Average price per whole restaurant pizza", 18, 12, 26, "USD per pizza"),
         asm("a6", "Average mass per whole pizza", 1.0, 0.7, 1.4, "kg per pizza"),
         asm("a7", "Share of US frozen pizza sales attributable to Chicago", 0.008, 0.005, 0.012, "share"),
         asm("a8", "Average price per frozen pizza", 7, 4, 11, "USD per frozen pizza")]


def fm(mid, formula, inputs, unit, coverage=None):
    m = {"id": mid, "method": "formula_mc", "unit": unit,
         "params": {"formula": formula, "inputs": {k: {"id": v, "role": f"role of {v}"} for k, v in inputs.items()}}}
    if coverage is not None:
        m["coverage"] = coverage
    return m


M1 = fm("m1", "a * b * c * d * e", {"a": "p84", "b": "a3", "c": "p18", "d": "a1", "e": "a2"}, "g/day")
M2 = fm("m2", "a * b / c * d", {"a": "p64", "b": "a4", "c": "a5", "d": "a6"}, "kg/year")
M3 = fm("m3", "a * b / c * d", {"a": "p60", "b": "a7", "c": "a8", "d": "a6"}, "kg/year")
PART = {"kind": "part", "dimension": "channel", "part": "frozen_retail", "siblings": ["restaurant", "other"]}
PART_ERR = ("covers only frozen_retail of channel, so code does not combine it with full estimates; sum it with its siblings "
            "(restaurant, other) in one method, with an allowance assumption for parts without evidence")
# 餐馆 + 冷冻一个公式（两条渠道共用每个披萨的公斤数 a6）：5 个假设，两个部分的上限是 6
SUPPLY = fm("m2", "(a * b / c + e * f / g) * d", {"a": "p64", "b": "a4", "c": "a5", "e": "p60", "f": "a7", "g": "a8", "d": "a6"},
            "kg/year", {"kind": "sum", "dimension": "channel", "parts": ["restaurant", "frozen_retail"], "missing": []})


def run(methods, raw_a=RAW_A, target=TARGET):
    return C.run(methods, PTS, target, assumptions=A.validate(raw_a, target))


def by_id(out):
    return {m["id"]: m for m in out["methods"]}


class TestPizzaCoverage(unittest.TestCase):
    def test_legacy_methods_without_coverage_unchanged(self):
        out = run([M1, M2, M3])
        ms = by_id(out)
        for mid, e in (("m1", 64.8), ("m2", 59.9), ("m3", 22.3)):
            self.assertAlmostEqual(ms[mid]["estimate"], e, delta=0.05)
            self.assertNotIn("coverage", ms[mid])
            self.assertNotIn("coverage_excluded", ms[mid])
        self.assertAlmostEqual(out["result"]["central"], 44.2217, delta=0.001)   # 改前 v2.7c：m3 也等权进了合并
        self.assertEqual(sorted(out["result"]["weights"]), ["m1", "m2", "m3"])

    def test_explicit_full_gives_the_same_numbers(self):
        a, b = run([M1, M2]), run([dict(M1, coverage={"kind": "full"}), M2])
        self.assertEqual(by_id(b)["m1"]["coverage"], {"kind": "full"})
        self.assertEqual(by_id(a)["m1"]["estimate"], by_id(b)["m1"]["estimate"])
        self.assertEqual(a["result"], b["result"])

    def test_part_method_is_computed_but_not_combined(self):
        out = run([M1, M2, fm("m3", M3["params"]["formula"], {"a": "p60", "b": "a7", "c": "a8", "d": "a6"}, "kg/year", PART)])
        m3 = by_id(out)["m3"]
        self.assertIsNone(m3["estimate"])
        self.assertNotIn("mc", m3)
        self.assertEqual(m3["error"], PART_ERR)
        self.assertEqual(m3["coverage"], PART)
        self.assertAlmostEqual(m3["coverage_excluded"]["estimate"], 22.3, delta=0.05)   # 照算，只作诊断
        self.assertLess(m3["coverage_excluded"]["mc"]["p10"], m3["coverage_excluded"]["estimate"])
        self.assertFalse(C.produced(m3))
        self.assertEqual(sorted(out["result"]["weights"]), ["m1", "m2"])
        only12 = M.combine([m for m in out["methods"] if m["id"] in ("m1", "m2")])
        self.assertEqual(out["result"]["central"], only12["central"])
        self.assertNotIn("m3", sum(out["assumptions_used_by"].values(), []))

    def test_supply_sum_of_restaurant_and_frozen_is_pooled(self):
        out = run([M1, SUPPLY])
        ms = by_id(out)
        self.assertNotIn("error", ms["m2"])
        self.assertEqual(ms["m2"]["n_assumption_inputs"], 5)   # 两个部分：上限 6
        self.assertAlmostEqual(ms["m2"]["estimate"], 86.2, delta=0.05)
        r = out["result"]
        self.assertAlmostEqual(r["central"], 74.7, delta=0.05)
        self.assertAlmostEqual(r["p10"], 35.67, delta=0.05)
        self.assertAlmostEqual(r["p90"], 156.53, delta=0.05)
        self.assertGreater(r["weights"]["m2"], 0)

    def test_three_part_sum_with_allowance_for_other_is_pooled(self):
        # other 没有证据：给一个余量假设（相对餐馆 + 冷冻的比例）。id 只有 a1..a8，所以冷冻沿用 a4 的芝加哥占比（原运行里 a7 和 a4 的值相同），
        # a7 改成 other 的余量；这个方法用 5 个假设（3 个部分，上限 8），m1 用 3 个，合计 8 个
        raw = RAW_A[:6] + [asm("a7", "Other channels as a share of restaurant plus frozen pizza", 0.1, 0.05, 0.2, "share"),
                           RAW_A[7]]
        m = fm("m2", "(a * b / c + e * b / g) * d * (1 + o)", {"a": "p64", "b": "a4", "c": "a5", "e": "p60", "g": "a8", "d": "a6",
                                                               "o": "a7"}, "kg/year",
               {"kind": "sum", "dimension": "channel", "parts": ["restaurant", "frozen_retail", "other"], "missing": []})
        out = run([M1, m], raw)
        ms = by_id(out)
        self.assertNotIn("error", ms["m2"])
        self.assertEqual(ms["m2"]["n_assumption_inputs"], 5)
        self.assertAlmostEqual(ms["m2"]["estimate"], 93.68, delta=0.05)   # 比两个部分的 86.2 多了 other 的余量
        self.assertAlmostEqual(out["result"]["central"], 77.91, delta=0.05)
        self.assertEqual(sorted(out["result"]["weights"]), ["m1", "m2"])
        self.assertGreater(out["result"]["weights"]["m2"], 0)

    def test_sum_with_missing_parts_is_not_combined(self):
        miss = dict(SUPPLY, coverage={"kind": "sum", "dimension": "channel", "parts": ["restaurant", "frozen_retail"],
                                      "missing": ["other"]})
        m2 = by_id(run([M1, miss]))["m2"]
        self.assertIsNone(m2["estimate"])
        self.assertAlmostEqual(m2["coverage_excluded"]["estimate"], 86.2, delta=0.05)
        self.assertEqual(m2["error"], "sums restaurant, frozen_retail of channel but misses other, so code does not combine it "
                                      "with full estimates; add each missing part to the sum with an allowance assumption "
                                      "(missing then empty), or drop the method")


class TestAssumptionCap(unittest.TestCase):
    LEGACY = {k: v for k, v in TARGET.items() if k != "unit_canonical"}   # 上限和单位无关：不钉单位，不用写 unit

    def method(self, n_assumptions, coverage=None):
        ids = [f"a{i}" for i in range(1, n_assumptions + 1)]
        names = ["p64"] + ids
        f = " * ".join(f"x{i}" for i in range(len(names)))
        return fm("m1", f, {f"x{i}": v for i, v in enumerate(names)}, None, coverage)

    def err(self, n, coverage=None):
        return by_id(run([self.method(n, coverage)], target=self.LEGACY))["m1"].get("error", "")

    def test_caps(self):
        part = dict(PART)
        two = {"kind": "sum", "dimension": "channel", "parts": ["restaurant", "frozen_retail"], "missing": []}
        three = dict(two, parts=["restaurant", "frozen_retail", "other"])
        four = dict(two, parts=["w", "x", "y", "z"])
        self.assertEqual(self.err(3), "")
        self.assertEqual(self.err(4), "formula_mc uses 4 assumptions (at most 3)")
        self.assertEqual(self.err(4, {"kind": "full"}), "formula_mc uses 4 assumptions (at most 3)")
        self.assertEqual(self.err(4, part), "formula_mc uses 4 assumptions (at most 3)")
        self.assertEqual(self.err(6, two), "")
        self.assertEqual(self.err(7, two), "formula_mc uses 7 assumptions (at most 6)")
        self.assertEqual(self.err(8, three), "")   # 3 个部分：min(9, 8)
        self.assertEqual(self.err(8, four), "")    # 4 个部分：仍是 8（= 每次运行的上限）
        self.assertEqual((A.MAX_PER_RUN, A.MAX_PER_METHOD), (8, 3))


class TestCoverageValidation(unittest.TestCase):
    def test_invalid_coverage_is_a_method_error(self):
        cases = [("partial", None),
                 ({"kind": "partial"}, "coverage: kind must be \"full\", \"part\" or \"sum\", not 'partial'"),
                 ({}, "coverage: kind must be \"full\", \"part\" or \"sum\", not None"),
                 ({"kind": "part", "part": "x", "siblings": ["y"]}, "coverage: dimension must be a name (e.g. \"channel\")"),
                 ({"kind": "part", "dimension": "channel", "siblings": ["y"]}, "coverage: part must be a name"),
                 ({"kind": "part", "dimension": "channel", "part": "x", "siblings": []}, "coverage: siblings needs at least 1 name"),
                 ({"kind": "part", "dimension": "channel", "part": "x", "siblings": "y"}, "coverage: siblings must be a list of names"),
                 ({"kind": "sum", "dimension": "channel", "parts": ["x"], "missing": []}, "coverage: parts needs at least 2 names"),
                 ({"kind": "sum", "dimension": "channel", "parts": ["x", "x"], "missing": []}, "coverage: parts lists a name twice"),
                 ({"kind": "sum", "dimension": "channel", "parts": ["x", "y"]}, "coverage: missing must be a list of names")]
        for cov, msg in cases:
            with self.subTest(cov=cov):
                m = by_id(run([dict(M1, coverage=cov)]))["m1"]
                self.assertIsNone(m["estimate"])
                self.assertNotIn("coverage_excluded", m)
                self.assertEqual(m["error"], msg or "coverage must be an object such as {\"kind\": \"full\"}, not 'partial'")
        self.assertIsNone(by_id(run([dict(M1, coverage=None)]))["m1"].get("error"))   # JSON null = 省略

    def test_prompt_examples_follow_the_code_rules(self):
        line = next(x for x in METHODS_SPEC.splitlines() if x.startswith("- coverage"))
        dec = json.JSONDecoder()
        ex = [dec.raw_decode(line, i.start())[0] for i in re.finditer(r'\{"kind"', line)]
        self.assertEqual([e["kind"] for e in ex], ["full", "sum", "part"])
        self.assertEqual(C.coverage(ex[0]), ({"kind": "full"}, ""))
        self.assertEqual(C.coverage(ex[1])[1], "")   # 完整的 sum：进合并
        self.assertTrue(C.coverage(ex[2])[1].startswith("covers only B of channel"))
        u = JUDGE_USER.format(question="q", as_of="2026-01-01", target="{}", directions="", table="", methods_spec="", extra_rule="")
        m = json.loads(re.search(r'\{"id": "m2", "method": "formula_mc".*?"rationale": "\.\.\."\}', u).group())
        self.assertEqual(C.coverage(m["coverage"]), ({"kind": "full"}, ""))


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestRepairAndViews(unittest.TestCase):
    def test_part_method_triggers_the_repair_round(self):
        from triangulate.agent import graph as G
        pts = list(PTS.values())
        part3 = dict(M3, coverage=PART)
        for methods, want in (([M1, M2, M3], (3, [])), ([M1, M2, part3], (2, [f"method m3 (formula_mc): {PART_ERR}"]))):
            jr = {"methods": methods, "assumptions": RAW_A}
            out, av, failed = G._code_check(jr, pts, TARGET)
            self.assertEqual(G._problems(jr, out, av, failed), want)   # 改前：m1、m2 吻合就不交回裁判

    def test_audit_header_shows_declared_coverage(self):
        from triangulate.agent import graph as G
        out = run([M1, SUPPLY])
        self.assertEqual(G._audit_header(M1, out["methods"][0]), "m1 (formula_mc): a * b * c * d * e")   # 没声明：不变
        self.assertEqual(G._audit_header(SUPPLY, out["methods"][1]),
                         'm2 (formula_mc): (a * b / c + e * f / g) * d; declared coverage = {"kind": "sum", "dimension": '
                         '"channel", "parts": ["restaurant", "frozen_retail"], "missing": []}')

    def test_ledger_and_result_view_show_coverage(self):
        from triangulate.web import results as R
        comp = run([M1, SUPPLY, dict(M3, coverage=PART)])
        st = {"qid": "q", "question": "q", "as_of": "2026-10-17", "plan": {"target": TARGET}, "compute": comp,
              "assumptions": A.validate(RAW_A, TARGET)}
        led = O.ledger(st)
        self.assertIn("- m2 coverage: sum over channel of restaurant, frozen_retail\n", led)
        self.assertIn("- m3 coverage: only frozen_retail of channel (siblings restaurant, other); not combined "
                      "(its own estimate 22.29)\n", led)
        self.assertNotIn("coverage:", O.ledger({**st, "compute": run([M1, M2, M3])}))   # 没声明 coverage 的运行：ledger 不变
        v = {m["id"]: m for m in R.result_view(st, "q")["methods"]}
        self.assertEqual((v["m2"]["status"], v["m3"]["status"]), ("computed", "excluded_by_coverage"))
        self.assertEqual(v["m3"]["coverage"], PART)
        self.assertAlmostEqual(v["m3"]["coverage_excluded"]["estimate"], 22.3, delta=0.05)
        self.assertEqual((v["m1"]["coverage"], v["m1"]["coverage_excluded"]), (None, None))

    def test_fake_model_run_repairs_a_part_method_into_a_sum(self):
        """假模型、真的图（tests/test_web.FakeLLM 的模式）：第一次的 m3 只覆盖一部分 -> 修正轮看到原因 -> 改成 sum 后进合并。"""
        from tests.test_plan_unit import graph_run
        from tests.test_web import FakeLLM
        users = {}
        part = {"id": "m3", "method": "formula_mc", "coverage": {"kind": "part", "dimension": "channel", "part": "A",
                                                                 "siblings": ["B"]},
                "params": {"formula": "a * s", "inputs": {"a": {"id": "p3", "role": "June 2025 widgets"},
                                                          "s": {"id": "a1", "role": "share of channel A"}}}}
        summed = {"id": "m3", "method": "formula_mc", "coverage": {"kind": "sum", "dimension": "channel", "parts": ["A", "B"],
                                                                   "missing": []},
                  "params": {"formula": "a * s + a * t", "inputs": {"a": {"id": "p3", "role": "June 2025 widgets"},
                                                                    "s": {"id": "a1", "role": "share of channel A"},
                                                                    "t": {"id": "a2", "role": "share of channel B"}}}}
        shares = [{"id": "a1", "name": "share of channel A", "value": 0.6, "low": 0.5, "high": 0.7, "unit": "share",
                   "rationale": "r"}, {"id": "a2", "name": "share of channel B", "value": 0.4, "low": 0.3, "high": 0.5,
                                       "unit": "share", "rationale": "r"}]
        full = {"id": "m2", "method": "formula_mc", "params": {"formula": "a", "inputs": {"a": {"id": "p3", "role": "June 2025 widgets"}}}}

        class LLM(FakeLLM):
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                out, err = super().ask(system, user, role=role, qid=qid, max_tokens=max_tokens, tries=tries)
                users.setdefault(role, []).append(user)
                if role.startswith("judge"):
                    out["methods"] = out["methods"] + [full, summed if role.endswith("repair") else part]
                    out["assumptions"] = shares
                return out, err

        st = graph_run(LLM())
        rp = st["judge_rounds"][0]["repair"]
        self.assertIn("method m3 (formula_mc): covers only A of channel, so code does not combine it with full estimates; "
                      "sum it with its siblings (B) in one method, with an allowance assumption for parts without evidence",
                      rp["errors"])
        self.assertEqual(rp["errors_after"], [])
        ms = {m["id"]: m for m in st["compute"]["methods"]}
        self.assertEqual(ms["m3"]["coverage"]["kind"], "sum")
        self.assertGreater(st["compute"]["result"]["weights"]["m3"], 0)
        self.assertAlmostEqual(st["compute"]["result"]["central"], 1210, delta=1210 * 0.05)
        self.assertIn('declared coverage = {"kind": "sum"', users["audit"][-1])
        self.assertIn("Coverage: a method's result must cover the whole target", users["audit"][-1])
        self.assertIn("- coverage (optional, any method)", users["judge:r1"][0])
        self.assertTrue(st["final"]["text"])


if __name__ == "__main__":
    unittest.main()

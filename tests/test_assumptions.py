"""v2：假设输入（校验、拒绝规则、区间下限、采样、加权）和 --ablate-own-history（方向、数据点、方法的过滤）。
图的离线端到端测试需要 .venv（langgraph）；没有装时跳过。"""
import math
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import ablation as AB
from triangulate.agent import assumptions as AS
from triangulate.agent import compute as C
from triangulate.agent import evidence as ev
from triangulate.agent import methods as M
from triangulate.mc import quantile

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

TARGET = {"what": "Recreation visits to Yellowstone National Park, as counted by the National Park Service",
          "unit": "recreation visits (person-visits)", "period_start": "2026-08-01", "period_end": "2026-08-31"}


def A(**kw):
    base = {"id": "a1", "name": "August-to-July visit ratio (historical average)", "value": 0.9, "low": 0.8, "high": 1.0,
            "unit": "ratio", "rationale": "seasonal pattern in earlier years", "applies_when": "no closures",
            "falsified_by": "an August closure", "route": "m2"}
    base.update(kw)
    return base


def _pt(pid, value, period_end, unit="visits", period_start=None, keep=True, name="x", direction_id="d1"):
    return {"id": pid, "value": value, "unit": unit, "period_end": period_end, "keep": keep, "name": name,
            "period_start": period_start or period_end[:8] + "01", "direction_id": direction_id}


class TestAssumptionValidation(unittest.TestCase):
    def test_valid_assumption_kept(self):
        v = AS.validate([A()], TARGET)
        self.assertEqual([a["id"] for a in v["kept"]], ["a1"])
        self.assertEqual(v["rejected"], [])
        self.assertFalse(v["kept"][0]["is_pct"])

    def test_form_rules(self):
        bad = [(A(id="a13"), "a1..a12"), (A(id="a0"), "a1..a12"), (A(id="b1"), "a1..a12"), (A(value="0.9"), "numbers"), (A(low=True), "numbers"),
               (A(high=float("nan")), "numbers"), (A(low=0.0), "0 < low"), (A(value=1.2), "low <= value <= high"),
               (A(low=0.95), "low <= value"), (A(unit=""), "required"), (A(name=" "), "required"),
               (A(rationale=""), "required"), ("not a dict", "not an object")]
        for x, why in bad:
            v = AS.validate([x], TARGET)
            self.assertEqual(v["kept"], [], x)
            self.assertIn(why, v["rejected"][0]["reason"], x)

    def test_duplicates_and_run_cap(self):
        v = AS.validate([A(), A(name="another ratio")], TARGET)
        self.assertEqual(len(v["kept"]), 1)
        self.assertEqual(v["rejected"][0]["reason"], "duplicate id")
        many = [A(id=f"a{i}", name=f"ratio number {i}") for i in range(1, 13)] + [A(id="a13")]
        v = AS.validate(many, TARGET)
        self.assertEqual(len(v["kept"]), AS.MAX_PER_RUN)
        self.assertEqual(len(v["rejected"]), 1)

    def test_target_like_rejected(self):
        cases = [
            A(name="Uncounted backcountry visits", unit="visits", value=900, low=500, high=2000),   # 目标单位的水平值
            A(name="Yellowstone August visitors", unit="people", value=8e5, low=7e5, high=9e5),     # 名字指向目标实体和量
        ]
        for x in cases:
            v = AS.validate([x], TARGET)
            self.assertEqual(v["kept"], [], x["name"])
            self.assertIn("target-like", v["rejected"][0]["reason"], x["name"])

    def test_year_and_change_factors_allowed_v21(self):
        # v2.1：带目标年份的比率、相对期间的占比、目标的同比变化倍数都允许（v2 一律拒绝，挡掉了正常路线）
        cases = [
            A(name="Ratio of August 2026 to July 2026 visits"),
            A(name="Share of visits this year arriving in August"),
            A(name="Year-over-year change in August recreation visits", unit="factor", value=0.98, low=0.94, high=1.02),
        ]
        for x in cases:
            v = AS.validate([x], TARGET)
            self.assertEqual(len(v["kept"]), 1, (x["name"], v["rejected"]))
        a = AS.validate([cases[2]], TARGET)["kept"][0]
        self.assertTrue(AS.is_change_factor(a))
        self.assertAlmostEqual(a["p90_used"] / a["p10_used"], AS.MIN_WIDTH_CHANGE)

    def test_calendar_constants_in_formula(self):
        pts = {"p1": _pt("p1", 28000.0, "2026-07-31", period_start="2026-07-01")}
        out = C.run([{"method": "formula_mc", "params": {"formula": "d * n", "inputs": {"d": {"id": "p1"}, "n": {"id": "k_days_target"}}}}],
                    pts, TARGET, assumptions=AS.validate([], TARGET))
        m = out["methods"][0]
        self.assertNotIn("error", m)
        self.assertAlmostEqual(m["estimate"] / 28000.0, 31, delta=1.5)   # 8 月 31 天；中位数只受 p1 的采样影响
        self.assertEqual((m["n_point_inputs"], m["n_assumption_inputs"]), (1, 0))

    def test_ratio_and_other_entity_allowed(self):
        ok = [A(), A(name="Yellowstone share of regional visits", unit="%", value=40, low=30, high=50),
              A(name="Visits per entering vehicle", unit="visits per vehicle", value=2.5, low=2, high=3),
              A(name="Average party size of park visitors", unit="people per party", value=3, low=2, high=4)]
        v = AS.validate([dict(x, id=f"a{i}") for i, x in enumerate(ok, 1)], TARGET)
        self.assertEqual(len(v["kept"]), 4, v["rejected"])

    def test_percent_like_data_points(self):
        v = AS.validate([A(name="share of annual visits in August", unit="percent", value=18.5, low=17, high=20)], TARGET)
        a = v["kept"][0]
        self.assertEqual(a["unit"], "%")
        self.assertTrue(a["is_pct"])
        self.assertLess(a["p90_used"], 1)  # 除以 100 后再采样，和数据点一样
        pts = {"p1": _pt("p1", 4.0e6, "2025-12-31", period_start="2025-01-01")}
        out = C.run([{"method": "formula_mc", "params": {"formula": "t * s", "inputs": {"t": {"id": "p1"}, "s": {"id": "a1"}}}}],
                    pts, TARGET, assumptions=v)
        self.assertTrue(0.6e6 < out["methods"][0]["estimate"] < 0.9e6, out["methods"][0])


class TestWidthFloor(unittest.TestCase):
    def test_narrow_range_widened_around_geometric_centre(self):
        lo, hi, widened = AS.effective_range(A(low=0.88, high=0.92))
        self.assertTrue(widened)
        self.assertAlmostEqual(hi / lo, AS.MIN_WIDTH)
        self.assertAlmostEqual(lo * hi, 0.88 * 0.92)
        lo, hi, widened = AS.effective_range(A(low=0.9, high=0.9))  # low == high 也放宽
        self.assertTrue(widened)
        self.assertLess(lo, 0.9)

    def test_wide_range_unchanged(self):
        self.assertEqual(AS.effective_range(A(low=0.5, high=1.5)), (0.5, 1.5, False))
        lo, hi, _ = AS.effective_range(A(unit="%", low=10, high=30, value=20))
        self.assertAlmostEqual(lo, 0.10)
        self.assertAlmostEqual(hi, 0.30)

    def test_floor_is_wider_than_point_inputs(self):
        self.assertGreater(AS.MIN_WIDTH, (1 + M.DEFAULT_REL_U) ** 2)


class TestSampling(unittest.TestCase):
    def test_assumption_samples_have_p10_p90_at_bounds(self):
        xs = sorted(C.Draws().get("a1", 0.5, 1.5))
        self.assertAlmostEqual(quantile(xs, 0.1), 0.5, delta=0.02)
        self.assertAlmostEqual(quantile(xs, 0.9), 1.5, delta=0.05)
        self.assertAlmostEqual(quantile(xs, 0.5), math.sqrt(0.75), delta=0.02)

    def test_samples_shared_by_id_and_reproducible(self):
        d = C.Draws()
        self.assertIs(d.get("a1", 1, 2), d.get("a1", 1, 2))
        self.assertNotEqual(d.get("a1", 1, 2)[:5], d.get("a2", 1, 2)[:5])
        self.assertEqual(d.get("a1", 1, 2)[:5], C.Draws().get("a1", 1, 2)[:5])

    def test_same_inputs_under_different_names_give_identical_results(self):
        v = AS.validate([A()], TARGET)
        pts = {"p1": _pt("p1", 958706.0, "2026-07-31")}
        ms = [{"method": "formula_mc", "params": {"formula": "p * a", "inputs": {"p": {"id": "p1"}, "a": {"id": "a1"}}}},
              {"method": "formula_mc", "params": {"formula": "z * c", "inputs": {"z": {"id": "a1"}, "c": {"id": "p1"}}}}]
        out = C.run(ms, pts, TARGET, assumptions=v)
        m1, m2 = out["methods"]
        self.assertEqual((m1["estimate"], m1["mc"]), (m2["estimate"], m2["mc"]))
        self.assertEqual(out["assumptions_used_by"], {"a1": ["m1", "m2"]})


class TestFormulaRulesWithAssumptions(unittest.TestCase):
    PTS = {"p1": _pt("p1", 958706.0, "2026-07-31")}

    def _run(self, inputs, formula, assumptions):
        out = C.run([{"method": "formula_mc", "params": {"formula": formula, "inputs": inputs}}], self.PTS, TARGET,
                    assumptions=AS.validate(assumptions, TARGET))
        return out["methods"][0], out

    def test_only_assumptions_rejected(self):
        m, out = self._run({"a": {"id": "a1"}, "b": {"id": "a2"}}, "a * b", [A(), A(id="a2", name="another ratio")])
        self.assertIn("at least one kept observed data point", m["error"])
        self.assertIsNone(out["result"]["central"])

    def test_more_than_six_assumptions_per_method(self):
        # v2.8m：上限 3 -> 6
        xs = [A(id=f"a{i}", name=f"ratio {chr(96 + i)}") for i in range(1, 8)]
        inputs = {"p": {"id": "p1"}} | {f"x{i}": {"id": f"a{i}"} for i in range(1, 8)}
        m, _ = self._run(inputs, "p * x1 * x2 * x3 * x4 * x5 * x6 * x7", xs)
        self.assertIn("at most 6", m["error"])
        m, _ = self._run({k: v for k, v in inputs.items() if k != "x7"}, "p * x1 * x2 * x3 * x4 * x5 * x6", xs)
        self.assertNotIn("error", m)
        self.assertTrue(m["rests_mainly_on_assumptions"])

    def test_rejected_assumption_cannot_be_used(self):
        m, _ = self._run({"p": {"id": "p1"}, "a": {"id": "a1"}}, "p * a",
                         [A(name="Uncounted backcountry visits", unit="visits", value=900, low=500, high=2000)])
        self.assertIn("assumption a1 was rejected", m["error"])

    def test_observed_inputs_keep_code_uncertainty(self):
        m, _ = self._run({"p": {"id": "p1"}, "a": {"id": "a1"}}, "p * a", [A()])
        d = {x["id"]: x for x in m["inputs_detail"]}
        self.assertAlmostEqual(d["p1"]["p90"] / d["p1"]["p10"], (1 + M.DEFAULT_REL_U) ** 2)
        self.assertAlmostEqual(d["a1"]["p90"] / d["a1"]["p10"], AS.MIN_WIDTH)
        self.assertEqual((m["n_point_inputs"], m["n_assumption_inputs"]), (1, 1))


class TestWeightingRule(unittest.TestCase):
    HIST = {f"p{i}": _pt(f"p{i}", v, f"{y}-08-31") for i, (y, v) in
            enumerate([(2021, 1.0e6), (2022, 0.6e6), (2023, 0.85e6), (2024, 0.87e6), (2025, 0.88e6)], 1)}

    def test_untested_formula_gets_nonzero_weight_with_backtests(self):
        pts = dict(self.HIST, p9=_pt("p9", 958706.0, "2026-07-31"))
        ms = [{"method": "series_naive", "params": {"target_history": list(self.HIST), "k": 1}},
              {"method": "formula_mc", "params": {"formula": "j * r", "inputs": {"j": {"id": "p9"}, "r": {"id": "a1"}}}}]
        out = C.run(ms, pts, TARGET, assumptions=AS.validate([A()], TARGET))
        res = out["result"]
        self.assertTrue(out["methods"][0]["backtest"])
        self.assertFalse(out["methods"][1]["backtest"])
        self.assertEqual(res["weight_rule"], "inverse_backtest_error")
        self.assertEqual(res["weight_basis"], {"m1": "backtest", "m2": "median_of_backtested"})
        self.assertGreater(res["weights"]["m2"], 0)
        self.assertAlmostEqual(res["weights"]["m1"], res["weights"]["m2"])  # 只有一个回测方法：中位数 = 它自己
        self.assertAlmostEqual(res["assumption_weight_share"], res["weights"]["m2"])

    def test_no_backtests_equal_weights(self):
        pts = {"p9": _pt("p9", 958706.0, "2026-07-31"), "p8": _pt("p8", 881936.0, "2025-08-31")}
        ms = [{"method": "series_naive", "params": {"target_history": ["p8"], "k": 1}},
              {"method": "formula_mc", "params": {"formula": "j * r", "inputs": {"j": {"id": "p9"}, "r": {"id": "a1"}}}}]
        res = C.run(ms, pts, TARGET, assumptions=AS.validate([A()], TARGET))["result"]
        self.assertEqual(res["weight_rule"], "equal")
        self.assertEqual(set(res["weight_basis"].values()), {"equal"})
        self.assertAlmostEqual(res["weights"]["m1"], 0.5)


class TestAblationFilters(unittest.TestCase):
    def test_entity_anchors(self):
        self.assertEqual(AB.entity_anchors(TARGET), ["yellowstone"])
        self.assertEqual(AB.entity_anchors({"what": "Heathrow Airport passenger traffic in July 2026"}), ["heathrow"])
        self.assertEqual(AB.entity_anchors({"what": "Monthly recreation visits, Yellowstone National Park"})[:1],
                         ["yellowstone"])  # 第一个子句没有锚词时用整个 what
        self.assertEqual(AB.entity_anchors({"what": "new cars sold in the country"}), [])

    def test_own_values_excluded_others_kept(self):
        dirs = {"d1": {"category": "related_series"}, "d2": {"category": "own_history"}}
        own = [_pt("p1", 958706, "2026-07-31", name="Yellowstone National Park recreation visits in July 2026"),
               _pt("p2", 4.7e6, "2025-12-31", name="Yellowstone total visitors 2025", unit="people"),
               _pt("p3", 1.0, "2025-08-31", name="anything", direction_id="d2")]
        other = [_pt("p4", 4.1e5, "2026-07-31", name="Grand Teton National Park recreation visits July 2026"),
                 _pt("p5", 81.0, "2026-07-31", name="Yellowstone lodging occupancy July 2026", unit="%"),
                 _pt("p6", 1.2e6, "2026-07-31", name="Regional airport passengers July 2026", unit="passengers")]
        for p in own:
            self.assertTrue(AB.own_value_reason(p, TARGET, dirs), p["name"])
        for p in other:
            self.assertEqual(AB.own_value_reason(p, TARGET, dirs), "", p["name"])

    def test_methods_spec_lists_only_allowed_methods(self):
        s = AB.methods_spec()
        self.assertIn("formula_mc", s)
        for m in ("series_naive", "yoy_scaling", "linear_fit", "- ratio", "Series rules"):
            self.assertNotIn(m, s)

    def test_compute_allows_only_formula_methods(self):
        pts = {"p1": _pt("p1", 881936.0, "2025-08-31"), "p9": _pt("p9", 4.1e5, "2026-07-31")}
        ms = [{"method": "series_naive", "params": {"target_history": ["p1"], "k": 1}},
              {"method": "formula_mc", "params": {"formula": "g * r", "inputs": {"g": {"id": "p9"}, "r": {"id": "a1"}}}}]
        out = C.run(ms, pts, TARGET, assumptions=AS.validate([A(name="Ratio of the target to the neighbour")], TARGET),
                    only_methods=AB.ALLOWED_METHODS)
        self.assertIn("ablation", out["methods"][0]["error"])
        self.assertIsNotNone(out["methods"][1]["estimate"])

    def test_tag(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent.run import ablation_tag
        self.assertEqual(ablation_tag("v2"), "v2_noown")
        self.assertEqual(ablation_tag("v2_noown"), "v2_noown")
        self.assertEqual(ablation_tag(""), "noown")


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestGraphWithAssumptions(unittest.TestCase):
    """假模型：裁判提假设、用 formula_mc；检查 state、最终答案的 Key assumptions、账本、依赖图；消融时检查方向和表格。"""

    def _run(self, ablate: bool):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import outputs
        from triangulate.agent import pipeline as P
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many visits to Yellowstone in August 2026?", "2026-08-15", \
            date(2026, 8, 15)
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], ablate
        seen = {}

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                if role == "plan":
                    return {"target": TARGET | {"publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "own", "data_to_find": "f"},
                                           {"category": "related_series", "hypothesis": "neighbour", "data_to_find": "f"}]}, None
                if role.startswith("extract"):
                    return {"points": [
                        {"name": "Yellowstone National Park recreation visits in July 2026", "value_as_written": "958,706",
                         "unit": "visits", "period_start": "2026-07-01", "period_end": "2026-07-31",
                         "quote": "July 2026: 958,706 visits"},
                        {"name": "Grand Teton National Park recreation visits in July 2026", "value_as_written": "410,000",
                         "unit": "visits", "period_start": "2026-07-01", "period_end": "2026-07-31",
                         "quote": "neighbour July 2026: 410,000 visits"}]}, None
                if role == "audit":
                    seen["audit_user"] = user
                    return {"methods": []}, None
                if role.startswith("judge"):
                    seen["judge_user"] = user
                    return {"decisions": [], "extra_directions": [],
                            "assumptions": [A(route="m1"), A(id="a2", name="Yellowstone August visitors", unit="people", value=8e5, low=7e5, high=9e5),
                                            A(id="a3", name="target to neighbour ratio, 2014 to 2018 average", value=2.2,
                                              low=2.0, high=2.4, route="m2")],
                            "methods": [{"id": "m1", "method": "formula_mc",
                                         "params": {"formula": "j * r", "inputs": {"j": {"id": "p1", "role": "July 2026 visits"},
                                                                                      "r": {"id": "a1", "role": "August/July ratio"}}}},
                                        {"id": "m2", "method": "formula_mc",
                                         "params": {"formula": "g * k", "inputs": {"g": {"id": "p2", "role": "neighbour July visits"},
                                                                                   "k": {"id": "a3", "role": "target/neighbour ratio"}}}}]}, None
                if role == "final":
                    return {"answer": "About [[estimate]] visits; a1 is about 0.9 (my guess)."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                seen.setdefault("search_dirs", []).append(role)
                return {"queries": ["q"], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid, **kw):
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260814000000", "page_date": "2026-08-14",
                    "text": "July 2026: 958,706 visits. neighbour July 2026: 410,000 visits."}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": f"a{ablate}"}}
            g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = dict(g.get_state(cfg).values)
        if ablate:
            from triangulate.agent.run import ablation_summary
            st["ablation"] = ablation_summary(st)
        return st, seen, outputs

    def test_assumptions_flow_to_outputs(self):
        st, seen, outputs = self._run(ablate=False)
        av = st["assumptions"]
        self.assertEqual([a["id"] for a in av["kept"]], ["a1", "a3"])
        self.assertEqual([a["id"] for a in av["rejected"]], ["a2"])
        self.assertEqual({a["id"]: a["used_by"] for a in av["kept"]}, {"a1": ["m1"], "a3": ["m2"]})
        self.assertIsNotNone(st["compute"]["result"]["central"])
        text = st["final"]["text"]
        self.assertIn("Key assumptions", text)
        self.assertIn("0.9", text)                   # 代码填的 a1 值
        self.assertNotIn("about 0.9", text)          # 模型自己写的数字被替换
        self.assertIn("a1 is about [n]", text)
        self.assertIn("[n] to 2018 average", text)   # 假设名字里模型写的数字也按同一规则替换（2014 离 as_of 超过 10 年）
        self.assertNotIn("unknown placeholder", text)
        led = outputs.ledger(st, None)
        self.assertIn("## Assumptions", led)
        self.assertIn("Rejected by code", led)
        dg = outputs.dep_graph(st)
        anodes = [n for n in dg["nodes"] if n["kind"] == "assumption"]
        self.assertEqual({n["colour"] for n in anodes}, {outputs.COL["assumption"]})
        self.assertIn({"from": "A:a1", "to": "M:m1"}, dg["edges"])

    def test_ablation_drops_own_history_and_hides_own_values(self):
        st, seen, outputs = self._run(ablate=True)
        self.assertEqual([d["category"] for d in st["directions"]], ["related_series"])
        self.assertEqual(len(seen["search_dirs"]), 1)
        self.assertNotIn("958,706", seen["judge_user"])  # 目标自身的值不进裁判的表格
        self.assertIn("410,000", seen["judge_user"])
        self.assertNotIn("series_naive", seen["judge_user"].split("Tasks:")[0])
        ab = st["ablation"]
        self.assertEqual(ab["n_points_excluded"], 1)
        self.assertEqual(ab["dropped_candidate_directions"], ["c1"])
        m = {x["id"]: x for x in st["compute"]["methods"]}
        self.assertIn("unknown or discarded", m["m1"]["error"])   # p1 被排除，m1 用不了
        self.assertIsNotNone(m["m2"]["estimate"])
        self.assertIn("## Ablation", outputs.ledger(st, None))


class TestAuditOfAssumptions(unittest.TestCase):
    def test_registered_values_in_assumptions_are_reported(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent import run
        st = {"points": [], "results": [],
              "assumptions": {"kept": [A(rationale="based on 856,467 last month")], "rejected": []}}
        self.assertEqual(run.leakage_audit(st, "2026-08-15", [856467])["assumptions_containing_registered_values"], ["a1"])
        self.assertTrue(ev.leak_patterns([856467]))


if __name__ == "__main__":
    unittest.main()


class TestJudgeRepairDryRun(unittest.TestCase):
    """v2.1：裁判这一轮的方法一个都跑不出来时，代码先试跑，把错误清单交回裁判修一次（graph._dry_run_errors）。"""

    def test_errors_listed_when_nothing_runs(self):
        from triangulate.agent import graph as G
        pts = [dict(_pt("p1", 958706.0, "2026-07-31", period_start="2026-07-01"), id="p1", keep=True)]
        jr = {"methods": [{"id": "m1", "method": "formula_mc",
                           "params": {"formula": "j * r", "inputs": {"j": {"id": "p1"}, "r": {"id": "a1"}}}}],
              "assumptions": [A(name="Uncounted backcountry visits", unit="visits", value=900, low=500, high=2000)]}
        errs = G._dry_run_errors(jr, pts, TARGET)
        self.assertTrue(any("a1" in e and "rejected" in e for e in errs), errs)
        jr["assumptions"] = [A()]
        self.assertEqual(G._dry_run_errors(jr, pts, TARGET), [])

    def test_no_methods(self):
        from triangulate.agent import graph as G
        self.assertEqual(G._dry_run_errors({"methods": [], "assumptions": []}, [], TARGET), ["no methods were proposed"])


class TestV21FormulaGuards(unittest.TestCase):
    """v2.1：公式至少要有一个「量」输入（v2.1 第一轮 9 月消融版用两个比率相乘，交出了 2.2 这个「估计」）；mean() 取平均。"""

    def test_product_of_ratios_rejected(self):
        pts = {"p1": _pt("p1", 2.2, "2024-09-30", unit="percent")}
        out = C.run([{"method": "formula_mc", "params": {"formula": "s * r", "inputs": {"s": {"id": "p1"}, "r": {"id": "a1"}}}}],
                    pts, TARGET, assumptions=AS.validate([A(name="ratio 2026 to 2024", unit="ratio", value=1.0, low=0.85, high=1.18)], TARGET))
        self.assertIn("needs at least one input that is a quantity", out["methods"][0]["error"])

    def test_mean_of_points(self):
        pts = {f"p{i}": _pt(f"p{i}", v, f"2021-09-0{i}", unit="vehicle entries") for i, v in enumerate([8945.0, 11062.0, 12380.0, 9982.0], 1)}
        out = C.run([{"method": "formula_mc", "params": {"formula": "mean(a, b, c, d) * n",
                                                         "inputs": {"a": {"id": "p1"}, "b": {"id": "p2"}, "c": {"id": "p3"},
                                                                    "d": {"id": "p4"}, "n": {"id": "k_days_target"}}}}],
                    pts, TARGET, assumptions=AS.validate([], TARGET))
        m = out["methods"][0]
        self.assertNotIn("error", m)
        self.assertAlmostEqual(m["estimate"] / (sum([8945.0, 11062.0, 12380.0, 9982.0]) / 4 * 31), 1, delta=0.1)


class TestInputAuditRows(unittest.TestCase):
    """v2.1：输入核对要看的内容（graph.audit_rows）：formula_mc 每个输入的 role 和证据；序列方法的 target_history。"""

    def test_rows(self):
        from triangulate.agent import graph as G
        by_id = {"p1": dict(_pt("p1", 2781.0, "2026-05-31", unit="births", name="Year-over-year increase in births, May 2026"),
                            id="p1", source_url="https://x.example/a")}
        kept_a = {"a1": {"id": "a1", "name": "July 2026 / July 2025", "value": 1.13, "unit": "ratio"}}
        m_in = {"method": "formula_mc", "params": {"formula": "b * r", "inputs": {"b": {"id": "p1", "role": "July 2025 births"},
                                                                                 "r": {"id": "a1"}, "d": {"id": "k_days_target"}}}}
        rows = G.audit_rows(m_in, {"method": "formula_mc"}, by_id, kept_a)
        self.assertEqual([r[0] for r in rows], ["b", "r"])          # 日历常数不核对
        self.assertEqual(rows[1][2], "")                            # 没写 role -> 由 audit 直接判不通过
        self.assertIn("Year-over-year increase", rows[0][3])
        s_rows = G.audit_rows({"method": "series_naive", "params": {"target_history": ["p1"]}}, {"method": "series_naive"}, by_id, {})
        self.assertEqual(s_rows[0][2], G.TARGET_HISTORY_ROLE)

    def test_repair_errors_only_when_nothing_survives(self):
        from triangulate.agent import graph as G
        jr = {"methods": [{"id": "m1"}, {"id": "m2"}]}
        out = {"methods": [{"id": "m1", "method": "formula_mc"}, {"id": "m2", "method": "formula_mc"}]}
        av = {"rejected": []}
        self.assertEqual(G._repair_errors(jr, out, av, {0: "input audit: b: a change used as a level"}), [])
        errs = G._repair_errors(jr, out, av, {0: "x", 1: "input audit: y"})
        self.assertEqual(len(errs), 2)


class TestProblemsForRepair(unittest.TestCase):
    """v2.1c：有方法失败、或能跑的方法差 3 倍以上，都交回裁判修一次（graph._problems）。"""

    def test_conflict_and_failures(self):
        from triangulate.agent import graph as G
        out = {"methods": [{"id": "m1", "method": "formula_mc", "estimate": 22494.0},
                           {"id": "m2", "method": "formula_mc", "estimate": None},
                           {"id": "m3", "method": "formula_mc", "estimate": 3264.0}]}
        n_ok, probs = G._problems({"methods": [{}, {}, {}]}, out, {"rejected": []}, {1: "bad params"})
        self.assertEqual(n_ok, 2)
        self.assertTrue(any("disagree" in p for p in probs), probs)
        self.assertTrue(any("bad params" in p for p in probs), probs)

    def test_agreeing_methods_no_problems(self):
        from triangulate.agent import graph as G
        out = {"methods": [{"id": "m1", "estimate": 843000.0}, {"id": "m2", "estimate": 853000.0}]}
        self.assertEqual(G._problems({"methods": [{}, {}]}, out, {"rejected": []}, {}), (2, []))


class TestProblemsKeepsGoodRuns(unittest.TestCase):
    def test_two_agreeing_survivors_with_a_failure(self):
        from triangulate.agent import graph as G
        out = {"methods": [{"id": "m1", "estimate": 843000.0}, {"id": "m2", "estimate": 853000.0}, {"id": "m3", "estimate": None}]}
        self.assertEqual(G._problems({"methods": [{}, {}, {}]}, out, {"rejected": []}, {2: "x"}), (2, []))

    def test_single_survivor_with_a_failure_goes_back(self):
        from triangulate.agent import graph as G
        out = {"methods": [{"id": "m1", "estimate": 8.77e6}, {"id": "m2", "estimate": None}]}
        n, probs = G._problems({"methods": [{}, {}]}, out, {"rejected": []}, {1: "numeric constant 100 not allowed"})
        self.assertEqual(n, 1)
        self.assertTrue(probs)


class TestPercentTargetsAndRestatedPoints(unittest.TestCase):
    """v2.1d（FOMC 题）：目标本身是百分比时不套用「至少一个量输入」；假设不能和保留的观测点同值。"""
    RATE = {"what": "Upper bound of the US federal funds target range after the next FOMC meeting", "unit": "percent per annum",
            "period_start": "2026-10-16", "period_end": "2026-12-31"}

    def test_percent_target_allows_percent_inputs(self):
        pts = {"p1": _pt("p1", 4.0, "2026-09-16", unit="percent per annum", period_start="2026-09-16"),
               "p2": _pt("p2", 43.6, "2026-10-14", unit="%", period_start="2026-10-14")}
        av = AS.validate([A(id="a1", name="rate step per move", unit="percentage points", value=0.25, low=0.25, high=0.25)], self.RATE)
        out = C.run([{"method": "formula_mc", "params": {"formula": "u + s * q",
                                                         "inputs": {"u": {"id": "p1"}, "s": {"id": "a1"}, "q": {"id": "p2"}}}}],
                    pts, self.RATE, assumptions=av)
        self.assertNotIn("error", out["methods"][0], out["methods"][0])

    def test_assumption_restating_a_point_is_rejected(self):
        pts = {"p1": _pt("p1", 4.0, "2026-09-16", unit="percent per annum", period_start="2026-09-16"),
               "p43": _pt("p43", 43.6, "2026-10-14", unit="%", period_start="2026-10-14")}
        av = AS.validate([A(id="a1", name="probability of a hike", unit="%", value=43.6, low=30, high=55)], self.RATE)
        out = C.run([{"method": "formula_mc", "params": {"formula": "u * q", "inputs": {"u": {"id": "p1"}, "q": {"id": "a1"}}}}],
                    pts, self.RATE, assumptions=av)
        self.assertIn("restates kept data point p43", out["methods"][0]["error"])

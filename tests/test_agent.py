"""Agent MVP 的代码部分：URL 解析、快照选择、quote 核对、数字解析、哨兵、日期过滤、方法库、加权与区间、图的连线。
需要 .venv（langgraph）；没有装时整组跳过。"""
import json
import math
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import evidence as ev
from triangulate.agent import methods as M
from triangulate.agent.fetch import clean_url, select_snapshot
from triangulate.agent.search import parse_urls

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False


class TestSearcherParsing(unittest.TestCase):
    def test_only_urls_survive(self):
        text = ("Here are the sources (official!): https://example.gov/data/2025.htm, and "
                "[news](https://news.example.com/a?b=1#frag). The value is 123,456 visits.\n"
                "https://example.gov/data/2025.htm again; http://x.org/p).")
        self.assertEqual(parse_urls(text), ["https://example.gov/data/2025.htm", "https://news.example.com/a?b=1",
                                            "http://x.org/p"])

    def test_cap(self):
        text = " ".join(f"https://a{i}.example.com/x" for i in range(9))
        self.assertEqual(len(parse_urls(text, cap=5)), 5)

    def test_wayback_url_is_unwrapped(self):
        self.assertEqual(clean_url("https://web.archive.org/web/20250101000000/https://a.org/b#c"), "https://a.org/b")


class TestSnapshotSelection(unittest.TestCase):
    ROWS = [["timestamp", "original", "statuscode", "mimetype"],
            ["20250910040101", "https://a.org/x", "200", "text/html"],
            ["20260815235900", "https://a.org/x", "200", "text/html"],
            ["20260816000001", "https://a.org/x", "200", "text/html"],
            ["20260801000000", "https://a.org/x", "404", "text/html"]]

    def test_latest_on_or_before_as_of(self):
        self.assertEqual(select_snapshot(self.ROWS, date(2026, 8, 15))["timestamp"], "20260815235900")

    def test_none_before(self):
        self.assertIsNone(select_snapshot(self.ROWS, date(2025, 9, 1)))
        self.assertIsNone(select_snapshot([["timestamp"]], date(2026, 1, 1)))


class TestQuoteAndNumbers(unittest.TestCase):
    PAGE = ev.norm("The park hosted 881,936 recreation visits in August 2025, up 2% from\n August 2024 "
                   "(868,259 recreation visits). Revenue was $4.8 million. Table values in thousands.")

    def test_quote_verbatim_whitespace_normalised(self):
        self.assertTrue(ev.quote_in_text("hosted 881,936 recreation visits in August 2025", self.PAGE))
        self.assertTrue(ev.quote_in_text("up 2% from August 2024", self.PAGE))
        self.assertFalse(ev.quote_in_text("hosted 881,937 recreation visits", self.PAGE))
        self.assertTrue(ev.quote_in_text("hosted 881,936 ... (868,259 recreation", self.PAGE))
        self.assertFalse(ev.quote_in_text("(868,259 ... hosted 881,936", self.PAGE))  # 顺序不对

    def test_parse_value(self):
        self.assertEqual(ev.parse_value("881,936", ""), (881936.0, False))
        self.assertEqual(ev.parse_value("$4.8 million", ""), (4.8e6, False))
        self.assertEqual(ev.parse_value("4.8", "million"), (4.8e6, False))
        self.assertEqual(ev.parse_value("2.5M", ""), (2.5e6, False))
        self.assertEqual(ev.parse_value("12%", ""), (12.0, True))
        self.assertEqual(ev.parse_value("(1,234)", ""), (-1234.0, False))
        for bad in [("about 3 to 4", ""), ("n/a", ""), ("4.8 million", "billion"), ("7", "dozens")]:
            with self.assertRaises(ValueError):
                ev.parse_value(*bad)

    def test_scale_needs_textual_support(self):
        self.assertEqual(ev.scale_supported("million", ev.norm("Revenue was $4.8 million."), self.PAGE, "$4.8"), "quote")
        self.assertEqual(ev.scale_supported("thousand", "value 12", self.PAGE, "12"), "page_header")
        self.assertEqual(ev.scale_supported("billion", "value 12", self.PAGE, "12"), "")
        self.assertEqual(ev.scale_supported("", "value 12", self.PAGE, "12"), "none_needed")
        self.assertEqual(ev.scale_supported("thousand", "Visitors 12", "Table 3 (in thousands of visits)", "12"), "page_header")
        self.assertEqual(ev.scale_supported("m", "sales of $4.8m in May", "", "$4.8"), "quote")

    BAD = ("Employees can enroll in the 401(k) plan. Section 2(b) applies. The storm resulted in thousands of "
           "cancellations. In August 2025 the site counted 3,412 visitors. Annual total for 2025 was 41,250 visitors. "
           "I'm told 12.9% fewer came.")

    def _pt(self, **kw):
        base = {"name": "x", "scale_word": "", "unit": "visitors", "period_start": "2025-08-01", "period_end": "2025-08-31"}
        from triangulate.agent.pipeline import verify_point
        return verify_point({**base, **kw}, ev.norm(self.BAD), date(2026, 8, 15), None, False)

    def test_scale_counterexamples_rejected(self):
        q = "In August 2025 the site counted 3,412 visitors."
        for sw in ("thousand", "k", "b"):
            p, why = self._pt(quote=q, value_as_written="3,412", scale_word=sw)
            self.assertIsNone(p, sw)
            self.assertIn("scale word", why)
        self.assertEqual(self._pt(quote=q, value_as_written="3,412")[0]["value"], 3412.0)

    def test_quote_and_number_boundaries(self):
        p, why = self._pt(quote="In August 2025 ... 41,250 visitors", value_as_written="41,250")
        self.assertIsNone(p)  # 省略号跨句子，把月份和年总量拼到了一起
        self.assertIn("quote not found", why)
        self.assertIsNotNone(self._pt(quote="In August 2025 ... counted 3,412 visitors", value_as_written="3,412")[0])
        self.assertIsNone(self._pt(quote="I'm told 12.9% fewer came.", value_as_written="2.9%")[0])
        self.assertIsNone(self._pt(quote="3,412 visitors", value_as_written="412")[0])
        self.assertEqual(self._pt(quote="I'm told 12.9% fewer came.", value_as_written="12.9%")[0]["value"], 12.9)
        with self.assertRaises(ValueError):
            ev.parse_value("1.234.567", "")
        self.assertEqual(ev.parse_value("1.234", ""), (1.234, False))


class TestLeakSentinel(unittest.TestCase):
    def test_formats(self):
        pats = ev.leak_patterns(856467)
        for t in ["visits: 856,467 in", "856467", "856 467 visits", "856.5 thousand", "about 856.5k", "0.856 million",
                  "nearly 856,000 visitors", "856 467"]:
            self.assertTrue(ev.leak_scan(t, pats), t)
        for t in ["856K visits", "0.86 million", "856,500", "856.47 thousand", "856k"]:  # 审查补上的写法
            self.assertTrue(ev.leak_scan(t, pats), t)
        for t in ["1,856,467", "856,4670", "8564671", "881,936", "857.5 thousand"]:
            self.assertFalse(ev.leak_scan(t, pats), t)

    def test_several_values(self):
        pats = ev.leak_patterns([868450, 856467])  # 目标真值 + 另一个 as_of 之后才公布的官方值
        self.assertTrue(ev.leak_scan("August: 856,467", pats))
        self.assertTrue(ev.leak_scan("September: 868,450", pats))


class TestDateFilter(unittest.TestCase):
    A = date(2026, 8, 15)

    def test_parse_date(self):
        self.assertEqual(ev.parse_date("2025-08", end=True), date(2025, 8, 31))
        self.assertEqual(ev.parse_date("2025", end=True), date(2025, 12, 31))
        self.assertEqual(ev.parse_date("August 2025"), date(2025, 8, 1))
        self.assertEqual(ev.parse_date("Sep 4, 2025"), date(2025, 9, 4))
        self.assertIsNone(ev.parse_date("last summer"))

    def test_check(self):
        ok = {"period_start": "2026-07-01", "period_end": "2026-07-31", "published_at_if_visible": "2026-08-12"}
        self.assertEqual(ev.date_check(ok, self.A, date(2026, 8, 14)), "")
        self.assertIn("period_end", ev.date_check({**ok, "period_end": "2026-08-31"}, self.A, None))
        self.assertIn("published", ev.date_check({**ok, "published_at_if_visible": "2026-09-15"}, self.A, None))
        self.assertIn("page date", ev.date_check(ok, self.A, date(2026, 8, 16)))
        self.assertIn("missing", ev.date_check({"period_end": ""}, self.A, None))
        self.assertEqual(ev.date_check({"period_end": ""}, self.A, None, allow_no_period=True), "")


class TestMethods(unittest.TestCase):
    T = {2022: 100.0, 2023: 110.0, 2024: 121.0, 2025: 133.1}
    S = {2022: 10.0, 2023: 11.0, 2024: 12.1, 2025: 13.31, 2026: 14.641}

    def test_series_naive(self):
        self.assertEqual(M.series_naive(self.T, 2026, 1), 133.1)
        self.assertAlmostEqual(M.series_naive(self.T, 2026, 2), (121 + 133.1) / 2)
        with self.assertRaises(M.MethodError):
            M.series_naive({2025: 1.0}, 2026, 2)

    def test_yoy(self):
        self.assertAlmostEqual(M.yoy_scaling(self.T, self.S, 2026), 146.41)
        with self.assertRaises(M.MethodError):
            M.yoy_scaling(self.T, {2025: 1.0}, 2026)

    def test_linear_and_ratio(self):
        self.assertAlmostEqual(M.linear_fit(self.T, self.S, 2026), 146.41, places=6)  # 精确线性关系 y = 10x
        self.assertAlmostEqual(M.ratio(self.T, self.S, 2026), 146.41, places=6)
        with self.assertRaises(M.MethodError):
            M.linear_fit({2024: 1.0, 2025: 2.0}, self.S, 2026)

    def test_formula_mc(self):
        s = M.formula_mc("a * b", {"a": (1000.0, 0.0), "b": (0.08, 0.0)})
        self.assertAlmostEqual(s["median"], 80.0)
        s = M.formula_mc("a * b", {"a": (1000.0, 0.2), "b": (0.08, 0.2)})
        self.assertLess(s["p10"], 80.0)
        self.assertGreater(s["p90"], 80.0)
        with self.assertRaises(M.MethodError):
            M.formula_mc("a * 3", {"a": (1.0, 0.1)})

    def test_backtest_no_lookahead(self):
        bt = M.backtest("series_naive", self.T, {}, 2026, 1)
        self.assertEqual([b["year"] for b in bt], [2023, 2024, 2025])
        self.assertAlmostEqual(bt[0]["log_err"], math.log(100 / 110))
        bt = M.backtest("yoy_scaling", self.T, self.S, 2026)
        self.assertTrue(all(abs(b["log_err"]) < 1e-12 for b in bt))
        # linear_fit / ratio 也只用被测年之前的年份（扩展窗口）：linear_fit 要 3 个更早的年份，只有 2025 能测
        bt = M.backtest("linear_fit", self.T, self.S, 2026)
        self.assertEqual([b["year"] for b in bt], [2025])
        bt = M.backtest("ratio", self.T, self.S, 2026)
        self.assertEqual([b["year"] for b in bt], [2023, 2024, 2025])

    def test_formula_rules_for_agent(self):
        self.assertAlmostEqual(M.formula_mc("a * (1 - b)", {"a": (1000.0, 0.0), "b": (0.25, 0.0)})["median"], 750.0)
        self.assertAlmostEqual(M.formula_mc("a ** 2 / b", {"a": (10.0, 0.0), "b": (4.0, 0.0)})["median"], 25.0)
        for bad in ["a ** 0.97", "a * (1 - 1/(1+1+1+1+1+1+1+1+1+1))", "a * (1 + 1)", "a + 1 + 1 + 1 + 1", "a * max(1, 1)"]:
            with self.assertRaises(M.MethodError, msg=bad):
                M.formula_mc(bad, {"a": (881936.0, 0.0)})


class TestCombine(unittest.TestCase):
    def test_inverse_error_weights_and_hist_interval(self):
        a = {"id": "m1", "estimate": 100.0, "backtest": [{"log_err": 0.1}, {"log_err": -0.1}]}
        b = {"id": "m2", "estimate": 110.0, "backtest": [{"log_err": 0.01}, {"log_err": -0.01}]}
        c = M.combine([a, b])
        self.assertAlmostEqual(c["weights"]["m1"] / c["weights"]["m2"], (0.01 + M.EPS) / (0.1 + M.EPS))
        self.assertEqual(c["weight_rule"], "inverse_backtest_error")
        self.assertTrue(100 < c["central"] < 110)
        self.assertIn(c["basis"], ("historical_errors", "method_spread"))
        self.assertAlmostEqual(math.log(c["p90"] / c["central"]), M.Z90 * c["sigma_ln"])

    def test_no_backtest_equal_weights_spread(self):
        c = M.combine([{"id": "m1", "estimate": 100.0}, {"id": "m2", "estimate": 400.0}])
        self.assertEqual(c["weight_rule"], "equal")
        self.assertAlmostEqual(c["central"], 200.0)
        self.assertEqual(c["basis"], "method_spread")
        self.assertAlmostEqual(c["sigma_ln"], math.log(2))

    def test_single_method_fallback_and_mc(self):
        self.assertEqual(M.combine([{"id": "m1", "estimate": 5.0}])["basis"], "no_basis")
        c = M.combine([{"id": "m1", "estimate": 5.0, "mc": {"p10": 2.0, "p90": 12.5}}])  # MC 比 FALLBACK 宽
        self.assertEqual(c["basis"], "monte_carlo")
        self.assertIsNone(M.combine([])["central"])

    def test_no_backtest_interval_has_floor(self):
        # 两个方法估计相同、没有回测：分歧为 0，区间不能退化成一个点
        c = M.combine([{"id": "m1", "estimate": 850000.0}, {"id": "m2", "estimate": 850000.0}])
        self.assertEqual(c["basis"], "no_basis")
        self.assertAlmostEqual(c["sigma_ln"], M.FALLBACK_SIGMA)
        self.assertLess(c["p10"], 850000.0 * 0.8)
        c = M.combine([{"id": "m1", "estimate": 100.0, "mc": {"p10": 90.0, "p90": 110.0}}])
        self.assertEqual(c["basis"], "no_basis")  # MC 比 FALLBACK 窄，不能拿来收窄

    def test_duplicate_ids_rejected_and_compute_renumbers(self):
        with self.assertRaises(M.MethodError):
            M.combine([{"id": "m1", "estimate": 8e5}, {"id": "m1", "estimate": 9e5}])
        from triangulate.agent import compute as C
        pts = {f"p{i}": {"id": f"p{i}", "value": v, "period_start": f"{y}-08-01", "period_end": f"{y}-08-31", "keep": True,
                         "unit": "visits"} for i, (y, v) in enumerate([(2023, 846389.0), (2024, 868259.0), (2025, 881936.0)], 1)}
        tgt = {"period_start": "2026-08-01", "period_end": "2026-08-31"}
        for ids in ([None, None], ["naive_last_year", "naive_last_two"], ["m1", "m1"]):
            ms = [{"method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": k}} for k in (1, 2)]
            for m, i in zip(ms, ids):
                if i is not None:
                    m["id"] = i
            out = C.run(ms, pts, tgt)
            self.assertEqual([m["id"] for m in out["methods"]], ["m1", "m2"])
            self.assertTrue(860000 < out["result"]["central"] < 890000, out["result"]["central"])
            self.assertEqual(out["methods"][1]["years_used"], [2024, 2025])

    def test_formula_uncertainty_set_by_code(self):
        from triangulate.agent import compute as C
        pts = {"p1": {"id": "p1", "value": 881936.0, "period_end": "2025-08-31", "keep": True, "unit": "visits"}}
        tgt = {"period_start": "2026-08-01", "period_end": "2026-08-31"}
        widths = []
        for u in (0.01, 1.0):
            out = C.run([{"id": "x", "method": "formula_mc", "params": {"formula": "a", "inputs": {"a": {"id": "p1", "rel_uncertainty": u}}}}],
                        pts, tgt)
            m = out["methods"][0]
            widths.append(m["mc"]["p90"] / m["mc"]["p10"])
            self.assertEqual(m["rel_uncertainty_from_judge_ignored"], {"a": u})
        self.assertAlmostEqual(widths[0], widths[1])

    def test_untested_method_gets_median_weight(self):
        a = {"id": "m1", "estimate": 100.0, "backtest": [{"log_err": 0.05}]}
        b = {"id": "m2", "estimate": 100.0, "backtest": [{"log_err": 0.15}]}
        c = M.combine([a, b, {"id": "m3", "estimate": 100.0}])
        w1, w2, w3 = (c["weights"][k] for k in ("m1", "m2", "m3"))
        self.assertAlmostEqual(w3, (w1 + w2) / 2)


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestGraphOffline(unittest.TestCase):
    """假模型、假搜索、假网页：只检查图的连线、interrupt、Send 扇出、编号、计算和模板。"""

    def test_end_to_end_with_fakes(self):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P

        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget = P.Budget()
        ctx.leak_patterns = ev.leak_patterns(4242)

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"id": "d1", "category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                           {"id": "d2", "category": "physical_flow", "hypothesis": "h2", "data_to_find": "f2"}]}, None
                if role.startswith("extract"):
                    if "LEAKPAGE" in user:
                        raise AssertionError("leak-flagged page reached the extractor")
                    pts = [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "scale_word": "", "unit": "widgets",
                            "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                           for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]
                    pts.append({"name": "bad", "value_as_written": "9", "quote": "not in page", "period_end": "2025-01-01"})
                    return {"points": pts}, None
                if role.startswith("judge"):
                    return {"decisions": [], "extra_directions": [],
                            "methods": [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}},
                                        {"id": "m2", "method": "linear_fit", "params": {"target_history": ["p1"]}}]}, None
                if role == "final":
                    return {"answer": "About [[estimate]] widgets (range [[p10]] to [[p90]]); I think 1,234 too."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                return {"queries": ["q"], "urls": ["https://a.org/1", "https://leak.org/2"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid):
            text = "LEAKPAGE value 4,242" if "leak" in url else "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01", "text": text}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "t1"}}
            out = g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            self.assertIn("__interrupt__", out)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = g.get_state(cfg).values
        self.assertEqual(len([r for r in st["results"] if r["direction_id"] != "markets"]), 2)
        self.assertEqual(len(st["points"]), 6)  # 2 个方向 x 3 个核对通过的点
        self.assertEqual([p["id"] for p in st["points"]][:3], ["p1", "p2", "p3"])
        leak_pages = [pg for r in st["results"] for pg in r["pages"] if pg.get("leak_hits")]
        self.assertEqual(len(leak_pages), 2)
        dropped = [x["reason"] for r in st["results"] for x in r["dropped_points"]]
        self.assertTrue(any(r.startswith("quote not found verbatim in page") for r in dropped), dropped)
        m = {x["id"]: x for x in st["compute"]["methods"]}
        self.assertEqual(m["m1"]["estimate"], 1210.0)
        self.assertIn("error", m["m2"])
        self.assertIn("1,210", st["final"]["text"])
        self.assertNotIn("1,234", st["final"]["text"])
        self.assertEqual(st["final"]["digits_removed"], 1)



@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestGraphRound2AndBudget(unittest.TestCase):
    """第二轮 base-rate 方向：Send round=2、点的续号、第二轮裁判失败时回退到第一轮的方法；预算中止路径。"""

    def _ctx(self, budget=None):
        from triangulate.agent import pipeline as P
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget = budget or P.Budget()
        ctx.leak_patterns = []
        return ctx

    def test_second_round_numbering_and_fallback(self):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        ctx = self._ctx()
        calls = []

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                calls.append(role)
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
                if role.startswith("extract"):
                    if "BASE" in user:
                        return {"points": [{"name": f"ratio {y}", "value_as_written": f"{v}%", "unit": "%",
                                            "period_start": f"{y}-01-01", "period_end": f"{y}-12-31", "quote": f"{y} ratio {v}%"}
                                           for y, v in ((2023, 10), (2024, 11), (2025, 12))]}, None
                    return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                        "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                                       for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
                if role == "judge:r1":
                    return {"decisions": [{"id": "p1", "keep": False, "reason": "dup"}],
                            "extra_directions": [{"id": "b1", "hypothesis": "base rate", "data_to_find": "ratio"}],
                            "methods": [{"id": "x", "method": "series_naive", "params": {"target_history": ["p2", "p3"], "k": 1}}]}, None
                if role == "judge:r2":
                    return None, "reply is not valid JSON"
                if role == "final":
                    return {"answer": "About [[estimate]]."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                return {"queries": ["q"], "urls": ["https://base.org/1" if "base rate" in prompt else "https://a.org/1"],
                        "web_search_requests": 1}

        def fake_fetch(url, as_of, qid, **kw):
            text = "BASE 2023 ratio 10% 2024 ratio 11% 2025 ratio 12%" if "base" in url else \
                "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01", "text": text}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "t2"}}
            g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = g.get_state(cfg).values
        self.assertEqual(calls.count("judge:r1"), 1)
        self.assertEqual(calls.count("judge:r2"), 1)
        self.assertEqual([p["id"] for p in st["points"]], [f"p{i}" for i in range(1, 7)])
        self.assertEqual({p["round"] for p in st["points"][3:]}, {2})
        self.assertFalse(st["points"][0]["keep"])                    # 第一轮裁判丢掉的
        self.assertTrue(all(p["keep"] for p in st["points"][1:3]))   # 没列出的 = 保留
        self.assertEqual(st["compute"]["methods_from_round"], 1)     # 第二轮失败，回退到第一轮的方法
        self.assertAlmostEqual(st["compute"]["result"]["central"], 1210.0, places=6)
        self.assertEqual(st["compute"]["methods"][0]["label"], "x")
        self.assertEqual(st["final"]["placeholders"]["n_points_kept"], "2")  # 只数经裁判看过、且保留的点

    def test_budget_abort_in_sub_agent(self):
        from triangulate.agent import pipeline as P
        ctx = self._ctx(P.Budget(usd=0.05))

        class NoSearch:
            def search(self, *a, **k):
                raise AssertionError("search must not run when the reservation does not fit")
        ctx.searcher = NoSearch()
        out = P.run_direction(ctx, {"what": "w"}, {"id": "d1", "category": "own_history"}, 1)
        self.assertIn("usd cap", out["aborted"])


class TestDirectionsAndGenericEntry(unittest.TestCase):
    def test_select_directions(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent.graph import _clean_direction, select_directions
        raw = ([{"category": "own_history", "expected_information": 5}, {"category": "own_history", "expected_information": 4}]
               + [{"category": "related_series", "expected_information": 4} for _ in range(4)]
               + [{"category": c, "expected_information": 2} for c in ("physical_flow", "attention", "shocks")]
               + [{"category": "persona", "expected_information": 1}, {"category": "persona", "expected_information": 3}])
        cands = [_clean_direction(d, i + 1, "c") for i, d in enumerate(raw)]
        dirs = select_directions(cands, 8)
        cats = [d["category"] for d in dirs]
        self.assertEqual(len(dirs), 8)
        self.assertEqual(cats[0], "own_history")
        self.assertIn("persona", cats)                            # 排在清单后面的类别也有名额
        self.assertGreaterEqual(cats.count("related_series"), 2)  # 一类可以出几个方向
        self.assertEqual(sum(c["selected"] for c in cands), 8)
        self.assertEqual([d["id"] for d in dirs], [f"d{i}" for i in range(1, 9)])

    def test_question_without_answer_runs_offline_parts(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent import outputs, run
        q = {"id": "ask_x", "question": "What share of men in country X have colour vision deficiency?", "as_of": "2026-10-15"}
        st = {"qid": "ask_x", "question": q["question"], "as_of": q["as_of"], "plan": {"target": {}}, "directions": [],
              "results": [], "points": [], "compute": {"methods": [], "result": {"central": 0.08, "p10": 0.06, "p90": 0.1}},
              "final": {"text": "x"}, "judge_rounds": []}
        sc = run.score_one(q, st)
        self.assertFalse(sc["scored"])
        self.assertNotIn("pct_err", sc)
        self.assertIn("Evidence ledger", outputs.ledger(st, sc))
        self.assertEqual(run.leakage_audit(st, q["as_of"], None)["sentinel_hits"], [])
        self.assertNotIn("QUESTIONS", vars(run))  # agent 的运行代码不认识回测题库

    def test_audit_uses_dates_not_strings(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent import run
        st = {"points": [{"id": "p1", "period_end": "2026-09"}, {"id": "p2", "period_end": "2026-08"},
                         {"id": "p3", "period_end": "2026-08-31", "published_at_if_visible": "2026-09-15"}],
              "results": [{"search": {"queries": ["visits 856,467 report"]}, "pages": []}]}
        a = run.leakage_audit(st, "2026-09-06", [856467])
        self.assertEqual(a["points_dated_after_as_of"], ["p1", "p3"])  # '2026-09' 按月末算，晚于 as_of
        self.assertEqual(a["searcher_queries_containing_registered_values"], ["visits 856,467 report"])


class TestFetchDecoding(unittest.TestCase):
    def test_gzip_body_is_decompressed(self):
        import gzip

        from triangulate.agent.net import decompress
        self.assertEqual(decompress(gzip.compress(b"<p>x</p>"), {"Content-Encoding": "gzip"}), b"<p>x</p>")
        self.assertEqual(decompress(gzip.compress(b"<p>x</p>"), {}), b"<p>x</p>")  # 缓存里没有头，靠魔数
        self.assertEqual(decompress(b"<p>x</p>", {}), b"<p>x</p>")

    def test_undecodable_text_is_rejected(self):
        import os

        from triangulate.agent.fetch import _to_text
        text, why = _to_text(os.urandom(4000), {"Content-Type": "text/html"})
        self.assertIsNone(text)
        self.assertIn("undecodable", why)


class TestNetRobots(unittest.TestCase):
    def setUp(self):
        from triangulate.agent import net
        self.net = net
        net._ROBOTS.clear()
        self.addCleanup(net._ROBOTS.clear)

    def _fake(self, url, timeout):
        if url == "http://www.example.com/robots.txt":
            return 301, b"", {"Location": "https://www.example.com/robots.txt"}
        if url == "https://www.example.com/robots.txt":
            return 200, b"User-agent: *\nDisallow: /private/\nCrawl-delay: 5\n", {}
        if url.endswith("/robots.txt"):
            return 302, b"", {"Location": url}  # 自己重定向到自己：重定向太多
        return 200, b"ok", {}

    def test_redirected_robots_is_followed_per_scheme(self):
        with mock.patch.object(self.net, "_raw_get", self._fake), mock.patch.object(self.net.time, "sleep", lambda s: None), \
                mock.patch.object(self.net.LIMITER, "set_interval") as si:
            self.assertFalse(self.net.robots_allowed("http://www.example.com/private/a"))
            self.assertFalse(self.net.robots_allowed("https://www.example.com/private/b"))
            self.assertTrue(self.net.robots_allowed("https://www.example.com/public/c"))
            si.assert_called_with("www.example.com", 5.0)
            self.assertFalse(self.net.robots_allowed("https://loop.example.org/x"))  # 超过 5 跳 -> 全部禁止

    def test_crawl_delay_sets_host_interval(self):
        lim = self.net.HostLimiter()
        lim.set_interval("a.org", 5)
        lim.wait("a.org")
        self.assertGreaterEqual(lim._next["a.org"] - self.net.time.monotonic(), 4.0)


class TestFetchLeakRules(unittest.TestCase):
    """回测里不收 live 页；live 页正文有晚于 as_of 的日期就整页丢；快照重定向读不出时间戳就丢。"""

    def setUp(self):
        import tempfile
        from pathlib import Path

        from triangulate.agent import fetch
        self.F = fetch
        d = Path(tempfile.mkdtemp())
        for name, val in (("RAW_AGENT", d), ("CACHE", d / "_cache")):
            patcher = mock.patch.object(fetch, name, val)
            patcher.start()
            self.addCleanup(patcher.stop)

    LIVE = (b"<html><head><meta property='article:published_time' content='2026-08-17'></head><body><p>"
            + b"Market page. " * 30 + b"Kalshi prices No at 95% as of October 15, 2026.</p></body></html>")

    def test_backtest_never_uses_live_pages(self):
        with mock.patch.object(self.F, "cdx_lookup", lambda u, a: None), \
                mock.patch.object(self.F.net, "get", lambda *a, **k: (200, self.LIVE, {"Content-Type": "text/html"}, a[0])):
            rec = self.F.fetch_page("https://x.org/stats/2019-05/dashboard", date(2026, 9, 6), "t", today=date(2026, 10, 15))
        self.assertEqual(rec["status"], "dropped")
        self.assertIn("live pages not used in backtests", rec["reason"])

    def test_live_page_with_later_date_in_text_is_dropped(self):
        with mock.patch.object(self.F, "cdx_lookup", lambda u, a: None), \
                mock.patch.object(self.F.net, "get", lambda *a, **k: (200, self.LIVE, {"Content-Type": "text/html"}, a[0])):
            rec = self.F.fetch_page("https://x.org/stats/2019-05/dashboard", date(2026, 9, 6), "t", allow_live=True,
                                    today=date(2026, 10, 15))
        self.assertEqual(rec["status"], "dropped")
        self.assertIn("2026-10-15", rec["reason"])
        self.assertEqual(ev.late_dates("as of October 15, 2026; closes March 31, 2027", date(2026, 9, 6), date(2026, 10, 15)),
                         [date(2026, 10, 15)])

    def test_unverifiable_snapshot_redirect_is_dropped(self):
        snap = {"timestamp": "20260801000000", "original": "https://a.org/x"}
        html = b"<html><body><p>" + b"Some archived text. " * 30 + b"</p></body></html>"
        for final in ("https://web.archive.org/web/20260901000000/https://a.org/x", "https://a.org/x"):
            with mock.patch.object(self.F, "cdx_lookup", lambda u, a: snap), \
                    mock.patch.object(self.F.net, "get", lambda *a, **k: (200, html, {"Content-Type": "text/html"}, final)):
                rec = self.F.fetch_page("https://a.org/x", date(2026, 9, 6), "t", today=date(2026, 10, 15))
            self.assertEqual(rec["status"], "dropped", final)
            self.assertIn("not verifiable", rec["reason"])
            import shutil
            shutil.rmtree(self.F.CACHE / "snap", ignore_errors=True)  # 下一轮换一个最终 URL，不能读到缓存
        ok = "https://web.archive.org/web/20260801000000id_/https://a.org/x"
        with mock.patch.object(self.F, "cdx_lookup", lambda u, a: snap), \
                mock.patch.object(self.F.net, "get", lambda *a, **k: (200, html, {"Content-Type": "text/html"}, ok)):
            rec = self.F.fetch_page("https://a.org/x", date(2026, 9, 6), "t", today=date(2026, 10, 15))
        self.assertEqual(rec["status"], "snapshot")


class TestBudgetHold(unittest.TestCase):
    def test_in_flight_calls_are_reserved(self):
        from triangulate.agent import pipeline as P
        b = P.Budget(usd=1.00)
        with b.hold(0.5):
            with b.hold(0.4):
                with self.assertRaises(P.BudgetExceeded):  # 0.5 + 0.4 在途，再要 0.2 就超
                    with b.hold(0.2):
                        pass
        self.assertAlmostEqual(b.reserved, 0.0)

    def test_reservation_released_and_actual_kept(self):
        from triangulate.agent import pipeline as P
        b = P.Budget(usd=1.00)
        with b.hold(b.search_reserve()):
            b.add({"usd": 0.007, "usd_search_fee_assumed": 0.04})
        self.assertAlmostEqual(b.usd, 0.047)
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertGreaterEqual(b.search_reserve(), 0.068)  # 实测单次搜索最高 $0.068

    def test_directions_follow_budget(self):
        from triangulate.agent import pipeline as P
        self.assertEqual(P.Budget().directions, 10)                      # 40 页 / 每方向 4 页；$1 x 60% / $0.06
        self.assertEqual(P.Budget(usd=0.30).directions, 3)
        self.assertEqual(P.Budget(round1_pages=80, usd=5.0).directions, 16)  # 硬上限


class TestMarketsGarbage(unittest.TestCase):
    def test_bad_bodies_do_not_raise(self):
        from triangulate.agent import markets as MK
        from triangulate.agent import net
        events = [{"markets": [{"question": "a b c", "createdAt": "2026-01-01T00:00:00Z", "clobTokenIds": "[\"1\"]",
                                "outcomes": "[\"Yes\"]", "slug": "s"}, "junk"]}, "junk"]
        cases = [
            lambda u, **k: (200, b"<html>maintenance</html>", {}, u),
            lambda u, **k: (200, b"[1, 2]", {}, u),
            lambda u, **k: ((200, json.dumps({"events": events}).encode(), {}, u) if "gamma" in u
                            else (200, json.dumps({"history": [{"t": "1786000000", "p": 0.4}, {"t": "x"}, {"p": 2}]}).encode(), {}, u)),
            lambda u, **k: ((200, json.dumps({"events": events}).encode(), {}, u) if "gamma" in u else (200, b"not json", {}, u)),
        ]
        for fake in cases:
            with mock.patch.object(net, "get", fake):
                rec = MK.search_markets(["a", "b"], date(2026, 8, 15))
            self.assertIsInstance(rec["points"], list)
        self.assertEqual(rec["points"], [])

    def test_string_timestamps_are_parsed(self):
        from triangulate.agent import markets as MK
        from triangulate.agent import net
        events = [{"markets": [{"question": "a b c", "createdAt": "2026-01-01T00:00:00Z", "clobTokenIds": "[\"1\"]",
                                "outcomes": "[\"Yes\"]", "slug": "s"}]}]

        def fake(u, **k):
            if "gamma" in u:
                return 200, json.dumps({"events": events}).encode(), {}, u
            return 200, json.dumps({"history": [{"t": "1786000000", "p": "0.4"}]}).encode(), {}, u
        with mock.patch.object(net, "get", fake):
            rec = MK.search_markets(["a", "b"], date(2026, 8, 15))
        self.assertEqual([p["value"] for p in rec["points"]], [0.4])


class TestFinalScrub(unittest.TestCase):
    def test_model_digits_replaced(self):
        from triangulate.agent.graph import scrub_digits
        self.assertEqual(scrub_digits("My own range is [800,000, 900,000].", 2026)[0], "My own range is [[n], [n]].")
        self.assertEqual(scrub_digits("USD900,000 or about900k", 2026)[0], "USD[n] or about[n]k")
        self.assertEqual(scrub_digits("Roughly 2050 employees", 2026)[0], "Roughly [n] employees")
        self.assertEqual(scrub_digits("Roughly 2030 employees", 2026)[0], "Roughly [n] employees")
        t, n = scrub_digits("In August 2025, m1 used values from 2021, 2023 and 2024", 2026, {"m1"})
        self.assertEqual((t, n), ("In August 2025, m1 used values from 2021, 2023 and 2024", 0))
        self.assertEqual(scrub_digits("it used 2021", 2026)[1], 1)  # 没有年份上下文就替换（宁可多换）


class TestTruncatedReplies(unittest.TestCase):
    """被 max_tokens 截断的回复要报成 truncated（v2 8 月第一次运行：两次都被报成 invalid_json，重试没说要写短）。"""

    def _llm(self, tmp):
        from triangulate.llm import LLM
        llm = object.__new__(LLM)
        llm.model, llm.calls_path, llm._key = "fake", tmp, "x"
        return llm

    def test_truncated_json_is_reported_as_truncated(self):
        import tempfile
        from pathlib import Path
        body = json.dumps({"choices": [{"finish_reason": "length", "message": {"content": "{\"assessment\": [{\"ids\": "}}],
                           "usage": {"completion_tokens": 6000}}).encode()
        tmp = Path(tempfile.mkdtemp()) / "calls.jsonl"
        llm = self._llm(tmp)
        with mock.patch.object(type(llm), "_post", staticmethod(lambda req: (200, body))):
            out, text, err = llm.json_call([{"role": "user", "content": "x"}], arm="judge:r1", qid="t", attempt=1)
        self.assertIsNone(out)
        self.assertIn("truncated", err)
        self.assertEqual(json.loads(tmp.read_text(encoding="utf-8").splitlines()[-1])["error"], "truncated")

    def test_agent_retry_asks_for_a_shorter_reply(self):
        from triangulate.agent import pipeline as P
        seen = []

        class Fake(P.AgentLLM):
            def __init__(self):
                self.budget = P.Budget()

            def json_call(self, msgs, **kw):
                seen.append(msgs)
                return (None, "{\"a\": ", "reply was truncated (finish_reason=length)") if len(seen) == 1 else ({"a": 1}, "", None)
        out, err = Fake().ask("s", "u", role="judge:r1", qid="t")
        self.assertEqual(out, {"a": 1})
        self.assertIn("shorter", seen[1][-1]["content"])


if __name__ == "__main__":
    unittest.main()

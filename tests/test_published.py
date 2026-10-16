"""v2.4「答案已公布」（published.py）：代码挑候选（期间、实体、量、单位、不是预测 / 变化）、模型只确认、数字取自数据点；
连续值报这个值（估计只作参考、不混合），离散报 resolved；回测不检查。全部离线：假模型、假搜索、假网页。"""
import os
import shutil
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate.agent import published as PB

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

UK = {"what": "New passenger car registrations in the United Kingdom, as reported by SMMT",
      "unit": "number of new cars registered", "period_start": "2026-09-01", "period_end": "2026-09-30",
      "publisher": "Society of Motor Manufacturers and Traders (SMMT)", "outcome_type": "continuous"}
TOTAL = "UK new car registrations, September 2026 (preliminary SMMT figure)"


def _p(pid, name, value, unit="new cars registered", ps="2026-09-01", pe="2026-09-30", keep=True, **kw):
    return {"id": pid, "name": name, "value": value, "value_as_written": f"{value:,.0f}", "unit": unit, "period_start": ps,
            "period_end": pe, "keep": keep, "judged_round": 1, "source_url": "https://news.example.co.uk/a",
            "via": "snapshot", "page_date": "2026-10-02", "published_at_if_visible": "", "quote": f"q {value}", **kw}


NEAR_MISSES = [
    _p("p2", "UK new car registrations, August 2026", 150000, ps="2026-08-01", pe="2026-08-31"),          # 别的期间
    _p("p3", "UK new car registrations, September 2025", 312891, ps="2025-09-01", pe="2025-09-30"),       # 别的年份
    _p("p4", "Germany new car registrations, September 2026", 230000),                                   # 别的实体
    _p("p5", "SMMT forecast of UK new car registrations, September 2026", 340000),                      # 预测
    _p("p6", "UK new car registrations growth, September 2026", 12.1, unit="%"),                         # 变化率
    _p("p7", "UK new car registrations, January-September 2026 (cumulative)", 1739253, ps="2026-01-01"),  # 累计
    _p("p8", "UK new car registrations, September 2026 (other source)", 350000, keep=False),             # 裁判丢掉的
    _p("p9", "UK new homes completed, September 2026", 12000, unit="homes"),                             # 别的量
]


class TestCandidates(unittest.TestCase):
    def test_terms(self):
        self.assertEqual(PB.entity_terms(UK), ["smmt", "uk", "united kingdom"])
        self.assertEqual(PB.measure_stems(UK), {"car", "passe", "regis"})
        self.assertEqual(PB.publisher_terms(UK), ["society of motor manufacturers and traders", "smmt"])

    def test_only_same_entity_measure_and_period(self):
        pts = [_p("p1", TOTAL, 350518), _p("p10", "UK private new car registrations, September 2026", 149158),
               _p("p11", "UK fleet registrations, September 2026", 190988)] + NEAR_MISSES
        c, note = PB.candidates(pts, UK, date(2026, 10, 16))
        # 子集（private、fleet）代码放过，留给模型拒；和目标量共同词干多的排前面
        self.assertEqual([p["id"] for p in c], ["p1", "p10", "p11"])
        self.assertIn("3 candidate(s)", note)

    def test_near_misses_are_never_candidates(self):
        self.assertEqual(PB.candidates(NEAR_MISSES, UK, date(2026, 10, 16))[0], [])

    def test_target_period_not_over(self):
        c, note = PB.candidates([_p("p1", TOTAL, 350518)], {**UK, "period_end": "2026-10-31", "period_start": "2026-10-01"},
                                date(2026, 10, 16))
        self.assertEqual(c, [])
        self.assertIn("after as_of", note)

    def test_cap(self):
        pts = [_p(f"p{i}", f"UK new car registrations, September 2026, source {i}", 350518) for i in range(1, 30)]
        c, note = PB.candidates(pts, UK, date(2026, 10, 16))
        self.assertEqual(len(c), PB.MAX_CANDIDATES)
        self.assertIn("only the first", note)


class TestResolve(unittest.TestCase):
    C = [_p("p1", TOTAL, 350518), _p("p10", "UK private new car registrations, September 2026", 149158),
         _p("p15", "UK new car registrations, September 2026", 350536)]

    def test_value_comes_from_the_point_not_the_model(self):
        rec = PB.resolve({"candidates": [{"id": "p1", "verdict": "Target", "value": 999, "reason": "same"},
                                         {"id": "p10", "verdict": "different", "reason": "private buyers only"}]},
                         self.C, UK)
        self.assertEqual((rec["status"], rec["id"], rec["value"]), ("published", "p1", 350518))
        self.assertEqual([c["verdict"] for c in rec["candidates"]], ["target", "different", "no verdict"])

    def test_agreeing_sources_prefer_the_publisher(self):
        rec = PB.resolve({"candidates": [{"id": "p15", "verdict": "target"}, {"id": "p1", "verdict": "target"}]}, self.C, UK)
        self.assertEqual((rec["status"], rec["id"], rec["confirmed_ids"]), ("published", "p1", ["p1", "p15"]))

    def test_conflict_unknown_ids_and_bad_replies(self):
        rec = PB.resolve({"candidates": [{"id": "p1", "verdict": "target"}, {"id": "p10", "verdict": "target"}]}, self.C, UK)
        self.assertEqual(rec["status"], "conflict")
        self.assertEqual(rec["values"], {"p1": 350518, "p10": 149158})
        self.assertIn("p1 = 350,518; p10 = 149,158", PB.conflict_note(rec))
        for reply in ({"candidates": [{"id": "p4", "verdict": "target"}]}, {"candidates": "p1"}, None, {"x": 1}):
            self.assertEqual(PB.resolve(reply, self.C, UK)["status"], "not_confirmed", reply)

    def test_discrete_outcome_and_tails(self):
        t = {"what": "Bank Rate", "unit": "percent", "outcome_type": "discrete",
             "outcomes": [{"label": "3.75% or lower", "value": 3.75, "le": 3.75}, {"label": "4.00%", "value": 4.0},
                          {"label": "4.25% or higher", "value": 4.25, "ge": 4.25}]}
        for v, want in ((4.0, "4.00%"), (4.5, "4.25% or higher"), (3.5, "3.75% or lower")):
            rec = PB.resolve({"candidates": [{"id": "p1", "verdict": "target"}]}, [_p("p1", "Bank Rate", v, unit="%")], t)
            self.assertEqual(rec["outcome"], want, v)
        res = PB.result(rec, {"outcomes": [{**o, "prob": 0.5} for o in t["outcomes"]]}, t)
        self.assertEqual((res["resolved"], res["most_likely"], res["basis"]), (True, "3.75% or lower", "published"))
        self.assertEqual([o["prob"] for o in res["outcomes"]], [1.0, 0.0, 0.0])
        rec = PB.resolve({"candidates": [{"id": "p1", "verdict": "target"}]}, [_p("p1", "Bank Rate", 4.1, unit="%")], t)
        self.assertIsNone(rec["outcome"])
        self.assertIn("not in the outcome list", PB.result(rec, {}, t)["most_likely"])


class TestGate(unittest.TestCase):
    def test_only_live_questions_are_checked(self):
        from triangulate.agent.run import checks_published
        from triangulate.forecast import QUESTIONS
        today = date(2026, 10, 16)
        self.assertTrue(QUESTIONS)
        for q in QUESTIONS:   # 全部回测 / 留出题：有真值、as_of 早于今天
            self.assertFalse(checks_published(q, today), q["id"])
        self.assertTrue(checks_published({"as_of": "2026-10-16"}, today))
        self.assertFalse(checks_published({"as_of": "2026-10-15"}, today))
        self.assertFalse(checks_published({"as_of": "2026-10-16", "answer_value": 350518}, today))

    def test_prepare_run_sets_the_flag(self):
        from triangulate.agent import run as R

        class FakeCtx:   # 真的 Context 会读 DeepSeek key：测试里换掉
            def __init__(self, *a, **kw):
                pass
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(R, "RES", tmp), mock.patch.object(R, "Context", FakeCtx), \
                    mock.patch.object(R, "build", lambda ctx: None):
                self.assertTrue(R.prepare_run({"id": "a", "question": "?", "as_of": date.today().isoformat()})["ctx"].check_published)
                self.assertFalse(R.prepare_run({"id": "b", "question": "?", "as_of": "2026-09-06",
                                                "answer_value": 1})["ctx"].check_published)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


HIST = [(2023, 270000), (2024, 290000), (2025, 312891)]


def graph_run(check, verdicts=None, extra_points=(), discrete=False):
    """假模型跑整张图（as_of 2026-10-16）。check = ctx.check_published；verdicts = 假确认模型的回复（id -> verdict）。
    返回 (state, 调用过的 role, 确认 prompt)。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import jev as J
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many new cars?", "2026-10-16", date(2026, 10, 16)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    ctx.check_published = check
    roles, seen = [], {}
    if discrete:
        target = {"what": "Bank Rate set by the Bank of England at its September 2026 meeting", "unit": "percent",
                  "period_start": "2026-09-17", "period_end": "2026-09-17", "publisher": "Bank of England",
                  "outcome_type": "discrete", "outcome_kind": "policy rate in fixed steps"}
        raw = [("Bank Rate set at the 17 September 2026 meeting", "4%", "%", "2026-09-17"),
               ("Market-implied probability that Bank Rate is held at the September 2026 meeting", "70%", "%", "2026-09-10"),
               ("Market-implied probability of a cut at the September 2026 meeting", "30%", "%", "2026-09-10")]
        pts = [{"name": n, "value_as_written": v, "unit": u, "period_start": d, "period_end": d, "quote": f"{n}: {v}"}
               for n, v, u, d in raw]
        outs = [{"label": "3.75% or lower", "value": 3.75, "le": 3.75}, {"label": "4.00%", "value": 4.0},
                {"label": "4.25% or higher", "value": 4.25, "ge": 4.25}]
        judge = {"decisions": [], "extra_directions": [], "outcomes": outs,
                 "outcomes_basis": {"ids": ["p1", "p2"], "note": "current level and market odds"},
                 "methods": [{"id": "m1", "method": "outcome_probs",
                              "params": {"probs": {"4.00%": {"id": "p2", "role": "prob hold"},
                                                   "3.75% or lower": {"id": "p3", "role": "prob cut"}},
                                         "remainder": "4.25% or higher"}}]}
    else:
        target = {k: v for k, v in UK.items() if k != "outcome_type"}
        pts = [{"name": f"UK new car registrations, September {y}", "value_as_written": f"{v:,}", "unit": "new cars registered",
                "period_start": f"{y}-09-01", "period_end": f"{y}-09-30", "quote": f"September {y}: {v:,} new cars"}
               for y, v in HIST]
        pts += [{"name": n, "value_as_written": f"{v:,}", "unit": "new cars registered", "period_start": "2026-09-01",
                 "period_end": "2026-09-30", "quote": f"{n}: {v:,} new cars"}
                for n, v in [(TOTAL, 350518), ("UK private new car registrations, September 2026", 149158),
                             ("Germany new car registrations, September 2026", 230000),
                             ("SMMT forecast of UK new car registrations, September 2026", 340000), *extra_points]]
        judge = {"decisions": [], "extra_directions": [],
                 "methods": [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}}]}
    text = " ".join(p["quote"] for p in pts) + " 2023 2024 2025 2026"

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            roles.append(role)
            if role == "plan":
                return {"target": target, "market_keywords": [],
                        "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": pts}, None
            if role.startswith("judge"):
                return judge, None
            if role == "audit":
                return {"methods": []}, None
            if role == "published":
                seen["published_user"] = user
                return {"candidates": [{"id": i, "verdict": v, "reason": "checked 350,518", "value": 1}
                                       for i, v in (verdicts or {}).items()]}, None
            if role == "final":
                return {"answer": "About [[estimate]]." if not discrete else "Odds from p2."}, None
            raise AssertionError(role)

    class FakeSearcher:
        def search(self, prompt, *, role, qid, max_uses=3, cap=5):
            return {"queries": ["q"], "urls": ["https://news.example.co.uk/sep"], "web_search_requests": 1}

    def fake_fetch(url, as_of, qid, **kw):
        return {"url": url, "status": "snapshot", "snapshot_ts": "20261002000000", "page_date": "2026-10-02", "text": text}

    ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
    with mock.patch.object(P, "fetch_page", fake_fetch), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}), \
            mock.patch.dict(os.environ, {}):
        os.environ.pop(J.KEY_ENV, None)
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "pub"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        st = dict(g.get_state(cfg).values)
    return st, roles, seen.get("published_user", "")


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestPublishedGraph(unittest.TestCase):
    def test_live_confirmed_value_is_the_answer(self):
        from triangulate.agent import outputs
        st, roles, user = graph_run(True, {"p4": "target", "p5": "different"})
        self.assertEqual(roles.count("published"), 1)
        self.assertNotIn("final", roles)                                   # 终稿由代码写
        self.assertIn('- p4: "UK new car registrations, September 2026 (preliminary SMMT figure)" = 350,518', user)
        self.assertIn("- p5:", user)
        for pid in ("p1:", "p2:", "p3:", "p6:", "p7:"):                    # 历史、德国、预测：代码不送去确认
            self.assertNotIn(f"- {pid}", user)
        pub = st["published"]
        self.assertEqual((pub["status"], pub["id"], pub["value"]), ("published", "p4", 350518.0))
        r, e = st["compute"]["result"], st["compute"]["estimate_result"]
        self.assertEqual((r["central"], r["p10"], r["p90"], r["basis"], r["weights"]), (350518.0, None, None, "published", {}))
        self.assertAlmostEqual(e["central"], 312891.0, places=3)                           # 估计照算，只作参考
        text = st["final"]["text"]
        self.assertTrue(text.startswith("Published value: 350,518 new cars registered. This is the pinned target itself"))
        self.assertIn("For reference only (not blended with the published value): the estimation methods gave 312,891", text)
        self.assertIn("data point p4", text)
        led = outputs.ledger(st, None)
        self.assertIn("Result: **published value 350,518** (data point p4)", led)
        self.assertIn("## Published-value check (live use only)", led)
        self.assertIn("| p5 | UK private new car registrations, September 2026 | 149,158 |", led)
        self.assertIn("| m1 | series_naive | 312,891 |", led)
        dg = outputs.dep_graph(st)
        self.assertEqual(dg["nodes"][0]["label"], "target\n350,518\npublished")
        self.assertIn({"from": "P:p4", "to": "target"}, dg["edges"])

    def test_backtest_never_checks(self):
        st, roles, _ = graph_run(False, {"p4": "target"})
        self.assertNotIn("published", roles)
        self.assertEqual(st["published"]["status"], "not_checked")
        r = st["compute"]["result"]
        self.assertAlmostEqual(r["central"], 312891.0, places=3)
        self.assertNotIn("estimate_result", st["compute"])
        self.assertNotEqual(r.get("basis"), "published")
        self.assertIn("final", roles)

    def test_live_near_miss_not_confirmed_keeps_the_estimate(self):
        st, roles, _ = graph_run(True, {"p4": "different", "p5": "different", "p6": "target"})   # p6 不是候选：忽略
        self.assertEqual(st["published"]["status"], "not_confirmed")
        self.assertAlmostEqual(st["compute"]["result"]["central"], 312891.0, places=3)
        self.assertIn("final", roles)
        self.assertNotIn("Published value", st["final"]["text"])

    def test_live_conflict_reports_the_estimate_with_a_note(self):
        st, roles, _ = graph_run(True, {"p4": "target", "p8": "target"},
                                 extra_points=[("UK new car registrations, September 2026 (revised)", 300000)])
        self.assertEqual(st["published"]["status"], "conflict")
        self.assertAlmostEqual(st["compute"]["result"]["central"], 312891.0, places=3)
        self.assertIn("p4 = 350,518; p8 = 300,000", st["final"]["text"])
        self.assertTrue(st["final"]["text"].startswith("About 312,891."))

    def test_live_discrete_resolved(self):
        from triangulate.agent import outputs
        st, roles, user = graph_run(True, {"p1": "target"}, discrete=True)
        self.assertIn("- p1:", user)
        self.assertNotIn("- p2:", user)                                    # 概率不是结果本身
        r = st["compute"]["result"]
        self.assertEqual((r["mode"], r["resolved"], r["most_likely"], r["most_likely_prob"]), ("discrete", True, "4.00%", 1.0))
        self.assertEqual(st["compute"]["estimate_result"]["most_likely"], "4.00%")
        text = st["final"]["text"]
        self.assertTrue(text.startswith("Resolved: the target resolves to outcome '4.00%' (published value 4%)"))
        self.assertIn("outcome probabilities: 3.75% or lower 30.0%; 4.00% 70.0%; 4.25% or higher 0.0%", text)
        self.assertNotIn("final", roles)
        self.assertEqual(st["jev"]["status"], "not_configured")
        self.assertIn("Resolved by a published value: **4.00%** (data point p1)", outputs.ledger(st, None))
        self.assertIn("resolved <b>4.00%</b>", outputs.outcome_table_html(st))


if __name__ == "__main__":
    unittest.main()

"""离散结果模式（v2.2）和 Jev 对照臂：plan 解析和退回、outcome_probs 校验、等权平均、输入核对的行、终稿模板、打分、
Jev 客户端（假 HTTP 层）、离散运行的网页结果 JSON。全部离线：假模型、假搜索、假网页、假 HTTP。"""
import json
import os
import shutil
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate.agent import assumptions as AS
from triangulate.agent import compute as C
from triangulate.agent import discrete as D
from triangulate.agent import jev as J

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

OUTS = [{"label": "cut to 3.75%", "value": 3.75}, {"label": "unchanged at 4.00%", "value": 4.0},
        {"label": "hike to 4.25%", "value": 4.25}]
TARGET = {"what": "Upper bound of the policy rate range after the next meeting", "unit": "percent per annum",
          "period_start": "2026-10-28", "period_end": "2026-10-28", "outcome_type": "discrete", "outcomes": OUTS}
CUT, HOLD, HIKE = (o["label"] for o in OUTS)


def _pt(pid, value, unit="%", name="market-implied probability", keep=True):
    return {"id": pid, "name": name, "value": value, "unit": unit, "period_start": "2026-10-14", "period_end": "2026-10-14",
            "keep": keep, "source_url": "https://www.example.org/monitor", "page_date": "2026-10-14"}


PTS = {"p1": _pt("p1", 56.4, name="probability unchanged at the next meeting"),
       "p2": _pt("p2", 43.6, name="probability of a hike at the next meeting"),
       "p3": _pt("p3", 0.436, unit="probability", name="probability of a hike, fraction"),
       "p4": _pt("p4", 43.6, unit="percent probability"),
       "p5": _pt("p5", 4.0, unit="percent per annum", name="current upper bound"),
       "p6": _pt("p6", 30.0, keep=False)}


def _a(**kw):
    a = {"id": "a1", "name": "probability of a cut at the next meeting", "value": 1.0, "low": 0.5, "high": 3.0, "unit": "%",
         "rationale": "no market weight on a cut", "applies_when": "w", "falsified_by": "f", "route": "m1"}
    a.update(kw)
    return a


def _run(probs, remainder=None, assumptions=(), method="outcome_probs", target=TARGET):
    av = AS.validate(list(assumptions), target)
    m = {"id": "x", "method": method, "params": {"probs": probs, "remainder": remainder}}
    return C.run([m], dict(PTS), target, assumptions=av)


class TestPlanOutcomes(unittest.TestCase):
    def test_discrete_parsed(self):
        kind, note = D.parse_outcomes({"outcome_type": "Discrete", "outcomes": [{"label": " yes ", "value": None},
                                                                                {"label": "no", "value": "0"}]})
        self.assertEqual(note, "")
        self.assertEqual(kind, {"outcome_type": "discrete", "outcomes": [{"label": "yes", "value": None},
                                                                          {"label": "no", "value": 0.0}]})
        self.assertTrue(D.is_discrete(kind))

    def test_fallbacks(self):
        bad = {"one outcome": [{"label": "a"}], "eleven": [{"label": str(i)} for i in range(11)],
               "duplicate": [{"label": "A"}, {"label": "a "}], "no label": [{"label": "a"}, {"value": 1}],
               "not a list": "a, b"}
        for why, outs in bad.items():
            kind, note = D.parse_outcomes({"outcome_type": "discrete", "outcomes": outs})
            self.assertEqual(kind, {"outcome_type": "continuous"}, why)
            self.assertIn("fell back to continuous", note, why)
        self.assertEqual(D.parse_outcomes({"outcome_type": "continuous", "outcomes": OUTS}), ({"outcome_type": "continuous"}, ""))
        self.assertEqual(D.parse_outcomes({})[0], {"outcome_type": "continuous"})
        self.assertIn("not recognised", D.parse_outcomes({"outcome_type": "categorical"})[1])
        self.assertFalse(D.is_discrete({"outcome_type": "continuous"}))


class TestOutcomeProbs(unittest.TestCase):
    def test_percent_conversion_and_remainder(self):
        out = _run({HOLD: {"id": "p1", "role": "r"}, HIKE: {"id": "p2", "role": "r"}}, remainder=CUT)
        m = out["methods"][0]
        self.assertNotIn("error", m)
        self.assertAlmostEqual(m["distribution"][HOLD], 0.564)
        self.assertAlmostEqual(m["distribution"][HIKE], 0.436)
        self.assertAlmostEqual(m["distribution"][CUT], 0.0)
        self.assertEqual(m["used_ids"], ["p1", "p2"])
        # 「percent probability」也按百分数换算；fraction 不换算
        m2 = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p4"}}, remainder=CUT)["methods"][0]
        self.assertAlmostEqual(m2["distribution"][HIKE], 0.436)
        m3 = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p3"}}, remainder=CUT)["methods"][0]
        self.assertAlmostEqual(m3["distribution"][HIKE], 0.436)

    def test_remainder_takes_the_rest(self):
        m = _run({HIKE: {"id": "p2"}}, remainder=HOLD, assumptions=[_a()])["methods"][0]
        self.assertIn("outcomes without a probability", m["error"])          # cut 没有概率
        m = _run({HIKE: {"id": "p2"}, CUT: {"id": "a1"}}, remainder=HOLD, assumptions=[_a()])["methods"][0]
        self.assertAlmostEqual(m["distribution"][HOLD], 1 - 0.436 - 0.01)
        self.assertEqual(m["used_assumptions"], ["a1"])

    def test_sums(self):
        # 有余下结果：其余之和 <= 1.02，超过一点时余下 = 0 再归一化
        m = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p2"}, CUT: {"id": "a1"}}, assumptions=[_a(value=1.5, low=1, high=3)])
        self.assertAlmostEqual(sum(m["methods"][0]["distribution"].values()), 1.0)    # 没有余下：1.015 归一化
        m = _run({HOLD: {"id": "p1"}, CUT: {"id": "p2"}}, remainder=HIKE)["methods"][0]
        self.assertAlmostEqual(m["distribution"][HIKE], 0.0)
        over = _run({HOLD: {"id": "p1"}, CUT: {"id": "p1"}}, remainder=HIKE)["methods"][0]
        self.assertIn("would be negative", over["error"])
        low = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p6"}, CUT: {"id": "a1"}}, assumptions=[_a()])["methods"][0]
        self.assertIn("unknown or discarded", low["error"])
        short = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a2"}, CUT: {"id": "a1"}},
                     assumptions=[_a(), _a(id="a2", name="probability of a hike", value=20, low=10, high=30)])["methods"][0]
        self.assertIn("must sum to between 0.9 and 1.1", short["error"])
        ok = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a2"}, CUT: {"id": "a1"}},
                  assumptions=[_a(), _a(id="a2", name="probability of a hike", value=40, low=30, high=50)])["methods"][0]
        self.assertAlmostEqual(sum(ok["distribution"].values()), 1.0)
        self.assertAlmostEqual(ok["distribution"][HOLD], 0.564 / 0.974)

    def test_rejections(self):
        unknown = _run({"hold": {"id": "p1"}, HIKE: {"id": "p2"}}, remainder=CUT)["methods"][0]
        self.assertIn("unknown outcome label", unknown["error"])
        self.assertIn("is not one of the outcomes", _run({HOLD: {"id": "p1"}}, remainder="other")["methods"][0]["error"])
        both = _run({HOLD: {"id": "p1"}, CUT: {"id": "p2"}}, remainder=CUT)["methods"][0]
        self.assertIn("also the remainder", both["error"])
        not_p = _run({HOLD: {"id": "p5"}, HIKE: {"id": "p3"}}, remainder=CUT)["methods"][0]
        self.assertNotIn("error", not_p)                                      # 4.0 percent per annum -> 0.04（核对交给输入核对）
        big = _run({HOLD: {"id": "p1"}, HIKE: {"id": "x"}}, remainder=CUT)["methods"][0]
        self.assertIn("unknown or discarded", big["error"])
        raw = dict(PTS)
        raw["p7"] = _pt("p7", 56.4, unit="probability")
        m = C.run([{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p7"}}, "remainder": HIKE}}], raw, TARGET)
        self.assertIn("not a probability in [0, 1]", m["methods"][0]["error"])
        restated = _run({HOLD: {"id": "a1"}, HIKE: {"id": "p2"}}, remainder=CUT,
                        assumptions=[_a(name="probability unchanged", value=56.4, low=50, high=60)])["methods"][0]
        self.assertIn("restates kept data point p1", restated["error"])
        rej = _run({HOLD: {"id": "a1"}, HIKE: {"id": "p2"}}, remainder=CUT, assumptions=[_a(low=5)])["methods"][0]
        self.assertIn("was rejected", rej["error"])

    def test_continuous_methods_rejected_for_discrete_and_vice_versa(self):
        for method in ("formula_mc", "series_naive"):
            m = _run({}, method=method)["methods"][0]
            self.assertIn("not available for a discrete target", m["error"])
        cont = {k: v for k, v in TARGET.items() if k not in ("outcome_type", "outcomes")}
        m = C.run([{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}}}}], dict(PTS), cont)["methods"][0]
        self.assertIn("only available for a discrete target", m["error"])

    def test_pooling(self):
        av = AS.validate([_a()], TARGET)
        ms = [{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}, HIKE: {"id": "p2"}}, "remainder": CUT}},
              {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}, CUT: {"id": "a1"}}, "remainder": HIKE}},
              {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}}}}]          # 失败：不计入平均
        out = C.run(ms, dict(PTS), TARGET, assumptions=av)
        r = out["result"]
        self.assertEqual(r["mode"], "discrete")
        self.assertEqual(r["weights"], {"m1": 0.5, "m2": 0.5})
        probs = {o["label"]: o["prob"] for o in r["outcomes"]}
        self.assertAlmostEqual(probs[CUT], 0.005)
        self.assertAlmostEqual(probs[HIKE], (0.436 + 0.426) / 2)
        self.assertAlmostEqual(sum(probs.values()), 1.0)
        self.assertEqual(r["most_likely"], HOLD)
        self.assertEqual(r["central"], 4.0)
        self.assertIsNone(r["p10"])
        self.assertIsNone(r["p90"])
        self.assertEqual(r["assumption_weight_share"], 0.5)
        self.assertEqual(out["assumptions_used_by"], {"a1": ["m2"]})
        self.assertTrue(C.produced(out["methods"][0]))
        self.assertFalse(C.produced(out["methods"][2]))

    def test_non_numeric_outcomes_and_no_method(self):
        t = {**TARGET, "outcomes": [{"label": "yes", "value": None}, {"label": "no", "value": None}]}
        pts = {"p1": _pt("p1", 70.0)}
        r = C.run([{"method": "outcome_probs", "params": {"probs": {"yes": {"id": "p1"}}, "remainder": "no"}}], pts, t)["result"]
        self.assertEqual(r["most_likely"], "yes")
        self.assertIsNone(r["central"])
        none = C.run([], pts, t)["result"]
        self.assertIsNone(none["most_likely"])
        self.assertEqual(none["basis"], "no_method")

    def test_scoring(self):
        r = {"outcomes": [{"label": CUT, "value": 3.75, "prob": 0.0}, {"label": HOLD, "value": 4.0, "prob": 0.6},
                          {"label": HIKE, "value": 4.25, "prob": 0.4}], "most_likely": HOLD}
        s = D.score(r, 4.25)
        self.assertEqual(s["true_outcome"], HIKE)
        self.assertAlmostEqual(s["prob_true"], 0.4)
        self.assertAlmostEqual(s["brier"], 0.36 + 0.36)
        self.assertFalse(s["most_likely_correct"])
        self.assertTrue(D.score(r, 4.0)["most_likely_correct"])
        self.assertTrue(D.score(r, "Unchanged at 4.00%")["most_likely_correct"])   # 也可以按 label 给真值
        out = D.score(r, 5.0)                                                       # 真值不在结果列表里
        self.assertIsNone(out["true_outcome"])
        self.assertEqual(out["prob_true"], 0.0)
        self.assertAlmostEqual(out["brier"], 0.36 + 0.16 + 1.0)

    def test_score_one_discrete(self):
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        from triangulate.agent.run import score_one
        st = {"compute": {"result": {"mode": "discrete", "central": 4.0, "most_likely": HOLD,
                                     "outcomes": [{"label": HOLD, "value": 4.0, "prob": 0.7}, {"label": HIKE, "value": 4.25, "prob": 0.3}]}}}
        row = score_one({"id": "q", "as_of": "2026-10-15", "answer_value": 4.0}, st)
        self.assertEqual(row["mode"], "discrete")
        self.assertAlmostEqual(row["prob_true"], 0.7)
        self.assertAlmostEqual(row["brier"], 0.18)
        self.assertTrue(row["most_likely_correct"])
        self.assertNotIn("pct_err", row)
        live = score_one({"id": "q", "as_of": "2026-10-15"}, st)
        self.assertNotIn("prob_true", live)


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestAuditRowsAndProblems(unittest.TestCase):
    def test_audit_rows_for_probability_inputs(self):
        from triangulate.agent import graph as G
        mi = {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"},
                                                              HIKE: {"id": "a1", "role": "prob hike"}}, "remainder": CUT}}
        rows = G.audit_rows(mi, {"method": "outcome_probs"}, {p["id"]: p for p in PTS.values()}, {"a1": _a(value=40)})
        self.assertEqual([(r[0], r[1], r[2]) for r in rows], [(HOLD, "p1", "prob unchanged"), (HIKE, "a1", "prob hike")])
        self.assertIn("56.4 %", rows[0][3])
        self.assertIn("analyst assumption a1", rows[1][3])
        self.assertIn("remainder outcome", G._audit_header(mi, {"id": "m1", "method": "outcome_probs"}))

    def test_problems_do_not_compare_discrete_methods_by_ratio(self):
        from triangulate.agent import graph as G
        jr = {"methods": [{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}, HIKE: {"id": "p2"}}, "remainder": CUT}},
                          {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p2"}, HIKE: {"id": "p1"}}, "remainder": CUT}}]}
        out, av, failed = G._code_check(jr, list(PTS.values()), TARGET)
        self.assertEqual(failed, {})
        self.assertEqual(G._problems(jr, out, av, failed), (2, []))
        jr["methods"].append({"method": "formula_mc", "params": {}})
        out, av, failed = G._code_check(jr, list(PTS.values()), TARGET)
        n_ok, probs = G._problems(jr, out, av, failed)
        self.assertEqual(n_ok, 2)
        self.assertEqual(probs, [])     # 两条以上能跑的方法：不交回裁判（规则同连续值）


class TestJevClient(unittest.TestCase):
    PTS = [_pt("p1", 56.4, name="probability unchanged"), _pt("p2", 43.6, name="probability of a hike")]

    @staticmethod
    def _reply(probs, status=200, choice=None):
        body = {"model": "jev-1.13.0", "answers": {"outcome": {"type": "choice", "choice": choice or max(probs, key=probs.get),
                                                                "probabilities": probs, "confidence": 0.4}},
                "usage": {"input_tokens": 1000, "output_tokens": 7}}
        return status, json.dumps(body).encode()

    def test_request_and_response(self):
        seen = {}

        def post(url, body, headers, timeout):
            seen.update(url=url, body=json.loads(body), headers=headers)
            return self._reply({CUT: 0.02, HOLD: 0.6, HIKE: 0.38})

        logs = []
        out = J.run_arm(TARGET, self.PTS, "2026-10-15", qid="q", log=logs.append, client=J.JevClient("sk-test-123", post=post))
        self.assertEqual(seen["url"], "https://api.typesafe.ai/v1/systemone")
        self.assertEqual(seen["headers"]["Authorization"], "Bearer sk-test-123")
        b = seen["body"]
        self.assertEqual(b["model"], "jev-latest")
        self.assertEqual(set(b["questions"]), {"outcome"})                       # 一个请求一个问题
        q = b["questions"]["outcome"]
        self.assertEqual(q["type"], "choice")
        self.assertEqual(list(q["criteria"]), [CUT, HOLD, HIKE])
        self.assertIn("probability unchanged = 56.4 %, period 2026-10-14..2026-10-14, source www.example.org, 2026-10-14",
                      b["state"])
        self.assertIn("Days from the information cutoff to the end of the target period (computed by code): 13", b["state"])
        self.assertEqual(out["status"], "ok")
        self.assertEqual(out["choice"], HOLD)
        self.assertAlmostEqual(out["probabilities"][HIKE], 0.38)
        self.assertAlmostEqual(out["usd_estimated"], 1000 * 0.042 / 1e6)
        self.assertFalse(out["pooled_with_agent"])
        self.assertEqual(logs[0]["input_tokens"], 1000)
        self.assertNotIn("usd", logs[0])                                          # 不计入 DeepSeek 的预算
        self.assertNotIn("sk-test-123", json.dumps(out) + json.dumps(logs))      # key 不进记录

    def test_bad_replies_and_errors(self):
        def missing(url, body, headers, timeout):
            return self._reply({HOLD: 0.6, HIKE: 0.4})
        out = J.run_arm(TARGET, self.PTS, "2026-10-15", client=J.JevClient("k", post=missing))
        self.assertEqual(out["status"], "error")
        self.assertIn("do not cover exactly the outcomes", out["error"])

        def rejected(url, body, headers, timeout):
            return 401, b'{"error": "bad key"}'
        out = J.run_arm(TARGET, self.PTS, "2026-10-15", client=J.JevClient("secret-k", post=rejected))
        self.assertIn("HTTP 401", out["error"])
        self.assertNotIn("secret-k", json.dumps(out))
        calls = []

        def busy(url, body, headers, timeout):
            calls.append(1)
            return (529, b"") if len(calls) < 3 else self._reply({CUT: 0.0, HOLD: 0.5, HIKE: 0.5})
        out = J.run_arm(TARGET, self.PTS, "2026-10-15", client=J.JevClient("k", post=busy, sleep=lambda s: None))
        self.assertEqual((out["status"], out["attempts"], len(calls)), ("ok", 3, 3))
        self.assertEqual(J.run_arm(TARGET, [], "2026-10-15", client=J.JevClient("k", post=busy))["status"], "skipped")

    def test_skip_when_not_configured_and_key_file(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop(J.KEY_ENV, None)
            out = J.run_arm(TARGET, self.PTS, "2026-10-15")
        self.assertEqual(out["status"], "not_configured")
        tmp = Path(tempfile.mkdtemp())
        try:
            (tmp / "k.env").write_text("OTHER=1\nTYPESAFE_API_KEY='tsk-abc'\n", encoding="utf-8")
            self.assertEqual(J.read_key(tmp / "k.env"), "tsk-abc")
            (tmp / "empty.env").write_text("TYPESAFE_API_KEY=\n", encoding="utf-8")
            with self.assertRaises(J.JevError):
                J.read_key(tmp / "empty.env")
            with mock.patch.dict(os.environ, {J.KEY_ENV: str(tmp / "missing.env")}):
                out = J.run_arm(TARGET, self.PTS, "2026-10-15")
            self.assertEqual(out["status"], "error")
            self.assertIn("key file not found", out["error"])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


def discrete_graph_run(jev_post=None):
    """假模型跑一遍离散目标的整张图，返回最终 state 和看到的 prompt。jev_post 给了就配置一个临时 key 文件和假 HTTP 层。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "Upper bound after the next meeting?", "2026-10-15", date(2026, 10, 15)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    seen = {}

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            if role == "plan":
                seen["plan_user"] = user
                return {"target": {k: v for k, v in TARGET.items()} | {"publisher": "X"}, "market_keywords": [],
                        "directions": [{"category": "forecasts_markets", "hypothesis": "market odds", "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": [
                    {"name": "Market-implied probability the range is unchanged at the 2026-10-28 meeting",
                     "value_as_written": "56.4%", "unit": "%", "period_start": "2026-10-14", "period_end": "2026-10-14",
                     "quote": "unchanged 3.75-4.00: 56.4%"},
                    {"name": "Market-implied probability of a hike to 4.00-4.25 at the 2026-10-28 meeting",
                     "value_as_written": "43.6%", "unit": "%", "period_start": "2026-10-14", "period_end": "2026-10-14",
                     "quote": "hike 4.00-4.25: 43.6%"}]}, None
            if role == "audit":
                seen["audit_user"] = user
                return {"methods": []}, None
            if role.startswith("judge"):
                seen.setdefault("judge_roles", []).append(role)
                seen["judge_user"] = user
                return {"decisions": [], "extra_directions": [],
                        "assumptions": [_a(route="m2")],
                        "methods": [{"id": "m1", "method": "outcome_probs", "rationale": "market odds",
                                     "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"},
                                                          HIKE: {"id": "p2", "role": "prob hike"}}, "remainder": CUT}},
                                    {"id": "m2", "method": "outcome_probs", "rationale": "market odds plus a small cut",
                                     "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"},
                                                          HIKE: {"id": "p2", "role": "prob hike"},
                                                          CUT: {"id": "a1", "role": "prob cut"}}}}]}, None
            if role == "final":
                seen["final_user"] = user
                return {"answer": "Markets put about 56% on [[o2_label]] ([[o2_prob]]); m1 uses p1."}, None
            raise AssertionError(role)

    class FakeSearcher:
        def search(self, prompt, *, role, qid, max_uses=3, cap=5):
            return {"queries": ["q"], "urls": [f"https://monitor.example.org/{role}"], "web_search_requests": 1}

    def fake_fetch(url, as_of, qid, **kw):
        return {"url": url, "status": "live_dated", "snapshot_ts": None, "page_date": "2026-10-14",
                "text": "Monitor 2026-10-14. unchanged 3.75-4.00: 56.4% hike 4.00-4.25: 43.6%"}

    ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
    tmp = Path(tempfile.mkdtemp())
    env = {}
    if jev_post is not None:
        (tmp / "ts.env").write_text("TYPESAFE_API_KEY=tsk-graph\n", encoding="utf-8")
        env[J.KEY_ENV] = str(tmp / "ts.env")
    try:
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}), \
                mock.patch.dict(os.environ, env), mock.patch.object(J, "_urllib_post", jev_post or (lambda *a: (500, b""))):
            if jev_post is None:
                os.environ.pop(J.KEY_ENV, None)
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "d"}}
            g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = dict(g.get_state(cfg).values)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return st, seen


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestDiscreteGraph(unittest.TestCase):
    def test_end_to_end_final_template_and_outputs(self):
        from triangulate.agent import outputs
        st, seen = discrete_graph_run()
        self.assertEqual(st["plan"]["target"]["outcome_type"], "discrete")
        self.assertIn("outcome_type", seen["plan_user"])
        self.assertIn("Only outcome_probs is available", seen["judge_user"])
        self.assertIn(f'"{HOLD}" (value 4 percent per annum)', seen["judge_user"])
        self.assertIn("outcome_probs", seen["audit_user"])
        self.assertIn('prob hike"; evidence = data point p2', seen["audit_user"])
        self.assertEqual(seen["judge_roles"], ["judge:r1"])                    # 两个方法都能跑：没有修正轮
        r = st["compute"]["result"]
        self.assertEqual(r["mode"], "discrete")
        self.assertEqual(r["most_likely"], HOLD)
        probs = {o["label"]: o["prob"] for o in r["outcomes"]}
        self.assertAlmostEqual(probs[HOLD], (0.564 + 0.564 / 1.01) / 2)
        text = st["final"]["text"]
        for lab, p in probs.items():
            self.assertIn(f"- {lab}: {100 * p:.1f}%", text)                     # 代码生成的结果行
        self.assertIn(f"Most likely outcome: {HOLD} ({100 * probs[HOLD]:.1f}%)", text)
        self.assertIn("Markets put about [n] on unchanged at 4.00% (", text)     # 模型写的数字被换掉，占位符由代码填
        self.assertIn("m1 uses p1", text)
        self.assertIn("Key assumptions (proposed by the analyst model, not observed; code uses each value as given)", text)
        self.assertNotIn("unknown placeholder", text)
        self.assertEqual(st["jev"]["status"], "not_configured")
        led = outputs.ledger(st, None)
        self.assertIn("## Outcome probabilities (computed by code)", led)
        self.assertIn("| outcome | value | agent (pooled) | m1 | m2 | Jev (not pooled) |", led)
        self.assertIn("Jev arm (TypeSafe, not pooled): not_configured", led)
        dg = outputs.dep_graph(st)
        self.assertTrue(dg["nodes"][0]["label"].startswith(f"target\n{HOLD}"))
        self.assertIn({"from": "P:p1", "to": "M:m1"}, dg["edges"])
        self.assertIn("Jev (not pooled)", outputs.outcome_table_html(st))

    def test_jev_arm_runs_when_configured(self):
        sent = {}

        def post(url, body, headers, timeout):
            sent["body"] = json.loads(body)
            sent["auth"] = headers["Authorization"]
            return TestJevClient._reply({CUT: 0.05, HOLD: 0.5, HIKE: 0.45})
        st, _ = discrete_graph_run(jev_post=post)
        self.assertEqual(sent["auth"], "Bearer tsk-graph")
        self.assertIn("56.4 %", sent["body"]["state"])
        jv = st["jev"]
        self.assertEqual(jv["status"], "ok")
        self.assertEqual(jv["n_points_in_brief"], 2)
        self.assertAlmostEqual(jv["probabilities"][HIKE], 0.45)
        r = st["compute"]["result"]
        self.assertNotAlmostEqual({o["label"]: o["prob"] for o in r["outcomes"]}[HIKE], 0.45)   # 不并入 agent 的答案
        self.assertNotIn("tsk-graph", json.dumps(st, default=str))

    def test_continuous_run_skips_jev_and_keeps_old_result_shape(self):
        """连续值目标：target 只多一个 outcome_type = continuous；不经过 jev 节点；结果仍是 central / p10 / p90。"""
        from tests.test_assumptions import TestGraphWithAssumptions
        st, _, _ = TestGraphWithAssumptions()._run(ablate=False)
        self.assertEqual(st["plan"]["target"]["outcome_type"], "continuous")
        self.assertNotIn("outcomes", st["plan"]["target"])
        self.assertNotIn("jev", st)
        r = st["compute"]["result"]
        self.assertNotIn("mode", r)
        self.assertIsNotNone(r["p10"])
        self.assertIn("code samples each one between the bounds shown", st["final"]["text"])


if __name__ == "__main__":
    unittest.main()

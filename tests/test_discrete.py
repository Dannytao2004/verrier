"""离散结果模式（v2.2；v2.3 起结果列表由裁判定义）和 Jev 对照臂：plan 解析和退回、裁判定义的结果列表、outcome_probs 校验、等权平均、输入核对的行、终稿模板、打分、
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
    """v2.3：plan 只给 outcome_type 和可选的 outcome_kind，不列结果（结果列表由裁判根据证据定义）。"""

    def test_plan_without_outcomes(self):
        kind, note = D.parse_outcome_type({"outcome_type": "Discrete", "outcome_kind": "  policy rate \n in fixed steps "})
        self.assertEqual(note, "")
        self.assertEqual(kind, {"outcome_type": "discrete", "outcome_kind": "policy rate in fixed steps"})
        self.assertTrue(D.is_discrete(kind))                                   # 没有结果列表也是离散目标
        self.assertEqual(D.parse_outcome_type({"outcome_type": "discrete"})[0], {"outcome_type": "discrete", "outcome_kind": ""})
        # plan 还列了结果：忽略，记一条说明（结果列表只能由裁判定义）
        kind, note = D.parse_outcome_type({"outcome_type": "discrete", "outcome_kind": "yes/no", "outcomes": OUTS})
        self.assertEqual(kind, {"outcome_type": "discrete", "outcome_kind": "yes/no"})
        self.assertIn("plan listed outcomes; ignored", note)

    def test_continuous_and_fallbacks(self):
        self.assertEqual(D.parse_outcome_type({"outcome_type": "continuous", "outcome_kind": "x", "outcomes": OUTS}),
                         ({"outcome_type": "continuous"}, ""))                 # 连续值 target 不多任何字段
        self.assertEqual(D.parse_outcome_type({})[0], {"outcome_type": "continuous"})
        self.assertEqual(D.parse_outcome_type("junk")[0], {"outcome_type": "continuous"})
        self.assertIn("not recognised", D.parse_outcome_type({"outcome_type": "categorical"})[1])
        self.assertFalse(D.is_discrete({"outcome_type": "continuous"}))

    def test_plan_prompt_has_no_outcome_list(self):
        from triangulate.agent import prompts as PR
        self.assertIn('"outcome_kind": ""', PR.PLAN_USER)
        self.assertIn("Do not list the outcomes", PR.PLAN_USER)
        self.assertNotIn('"outcomes"', PR.PLAN_USER)
        self.assertNotIn("__OUTCOMES__", PR.DISCRETE_METHODS_SPEC)          # 方法说明不再带 plan 的列表


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
        self.assertNotIn("error", m)                                          # cut 没有输入：概率 0（记进 notes）
        self.assertAlmostEqual(m["distribution"][CUT], 0.0)
        self.assertAlmostEqual(m["distribution"][HOLD], 1 - 0.436)
        self.assertEqual(m["zero_outcomes"], [CUT])
        self.assertIn(f"no input for ['{CUT}']: probability 0", m["notes"])
        m = _run({HIKE: {"id": "p2"}, CUT: {"id": "a1"}}, remainder=HOLD, assumptions=[_a()])["methods"][0]
        self.assertAlmostEqual(m["distribution"][HOLD], 1 - 0.436 - 0.01)
        self.assertEqual(m["used_assumptions"], ["a1"])

    def test_sums(self):
        # 有余下结果：其余之和 <= 1.02，超过一点时余下 = 0 再归一化
        m = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p2"}, CUT: {"id": "a1"}}, assumptions=[_a(value=1.5, low=1, high=3)])
        self.assertAlmostEqual(sum(m["methods"][0]["distribution"].values()), 1.0)    # 没有余下：1.015 归一化
        m = _run({HOLD: {"id": "p1"}, CUT: {"id": "p2"}}, remainder=HIKE)["methods"][0]
        self.assertAlmostEqual(m["distribution"][HIKE], 0.0)
        over = _run({HOLD: {"id": "p1"}, CUT: {"id": "a1"}}, remainder=HIKE, assumptions=[_a(value=50, low=40, high=60)])
        self.assertIn("would be negative", over["methods"][0]["error"])
        low = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p6"}, CUT: {"id": "a1"}}, assumptions=[_a()])["methods"][0]
        self.assertIn("unknown or discarded", low["error"])
        short = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a2"}, CUT: {"id": "a1"}},
                     assumptions=[_a(), _a(id="a2", name="probability of a hike", value=20, low=10, high=30)])["methods"][0]
        self.assertIn("must sum to between 0.9 and 1.1", short["error"])
        ok = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a2"}, CUT: {"id": "a1"}},
                  assumptions=[_a(), _a(id="a2", name="probability of a hike", value=40, low=30, high=50)])["methods"][0]
        self.assertAlmostEqual(sum(ok["distribution"].values()), 1.0)
        self.assertAlmostEqual(ok["distribution"][HOLD], 0.564 / 0.974)

    def test_outcomes_without_input_get_zero(self):
        # live 运行 discrete4：FedWatch 只报维持和加息（和 = 1），其余结果没有输入 -> 概率 0，不再整题没出数
        m = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p2"}})["methods"][0]
        self.assertNotIn("error", m)
        self.assertEqual((m["distribution"][CUT], m["zero_outcomes"]), (0.0, [CUT]))
        self.assertAlmostEqual(m["distribution"][HOLD], 0.564)
        # 没有余下结果时和的检查照旧：只给 56.4% 不够
        short = _run({HOLD: {"id": "p1"}})["methods"][0]
        self.assertIn("must sum to between 0.9 and 1.1", short["error"])
        self.assertIn("count as 0", short["error"])
        # 每个结果都有输入或是余下结果：没有概率 0 的结果
        z = _run({HOLD: {"id": "p1"}, CUT: {"id": "p2"}}, remainder=HIKE)["methods"][0]
        self.assertEqual(z["zero_outcomes"], [])

    def test_rejections(self):
        unknown = _run({"hold": {"id": "p1"}, HIKE: {"id": "p2"}}, remainder=CUT)["methods"][0]
        self.assertIn("unknown outcome label", unknown["error"])
        self.assertIn("is not one of the outcomes", _run({HOLD: {"id": "p1"}}, remainder="other")["methods"][0]["error"])
        both = _run({HOLD: {"id": "p1"}, CUT: {"id": "p2"}}, remainder=CUT)["methods"][0]
        self.assertIn("also the remainder", both["error"])
        not_p = _run({HOLD: {"id": "p5"}, HIKE: {"id": "p3"}}, remainder=CUT)["methods"][0]
        self.assertIn("p5 ('current upper bound', unit 'percent per annum') is not stated as a probability", not_p["error"])
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
        # 一个方法的全部问题一次报出（修正轮要一次看到）：被拒的假设和漏掉的结果
        both = _run({HIKE: {"id": "a1"}}, remainder=CUT, assumptions=[_a(low=0)])["methods"][0]
        self.assertIn("was rejected", both["error"])
        self.assertNotIn("without", both["error"])                           # 没有输入的结果不是错误（概率 0）
        over = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p2"}, CUT: {"id": "a1"}, "x": {"id": "p1"}}, remainder=HOLD,
                    assumptions=[_a(value=5, low=2, high=8)])["methods"][0]
        self.assertIn("unknown outcome label 'x'", over["error"])
        self.assertIn("also the remainder", over["error"])

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
        self.assertEqual([(r[0], r[1]) for r in rows], [(HOLD, "p1"), (HIKE, "a1")])
        self.assertEqual(rows[1][2], "probability that the target resolves to outcome 'hike to 4.25%'; analyst's role: prob hike")
        # v2.2.1：role 由代码写成「target 取这个结果的概率」（有 target 时带数值和单位），余下结果也核对一行
        out = C.run([mi], dict(PTS), TARGET, assumptions=AS.validate([_a(value=40, low=30, high=50)], TARGET))["methods"][0]
        rows = G.audit_rows(mi, out, {p["id"]: p for p in PTS.values()}, {"a1": _a(value=40)}, TARGET)
        self.assertEqual(rows[0][2], "probability that the target resolves to outcome 'unchanged at 4.00%' (value 4 percent "
                                     "per annum); analyst's role: prob unchanged")
        self.assertEqual(rows[2][:3], (CUT, "remainder", "probability that the target resolves to outcome 'cut to 3.75%' "
                                                         "(value 3.75 percent per annum), taken as the rest (1 minus the other inputs)"))
        self.assertEqual(rows[2][3], "computed by code: 1 - 0.964 = 0.036; the other inputs cover 'unchanged at 4.00%' from "
                                     "p1, 'hike to 4.25%' from a1; outcomes with no input get 0: []")
        no_role = {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}}, "remainder": HIKE}}
        out = C.run([no_role], dict(PTS), TARGET)["methods"][0]
        self.assertEqual(G.audit_rows(no_role, out, {p["id"]: p for p in PTS.values()}, {}, TARGET)[0][2], "")   # 照旧拦下
        self.assertIn('mark it "mismatch" when the probability left over', G._audit_header(mi, {"id": "m1", "method": "outcome_probs"}))
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


# v2.3：裁判第一轮定义的结果列表（两个合并尾部用 le / ge 标出）和依据的点
JUDGE_OUTS = [{"label": CUT, "value": 3.75, "le": 3.75}, {"label": HOLD, "value": 4.0}, {"label": HIKE, "value": 4.25, "ge": 4.25}]
BASIS = {"ids": ["p1", "p2"], "note": "p1 and p2 price a hold at the current 4.00% upper bound and a hike to 4.25%"}
GOOD_METHODS = [{"id": "m1", "method": "outcome_probs", "rationale": "market odds",
                 "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"},
                                      HIKE: {"id": "p2", "role": "prob hike"}}, "remainder": CUT}},
                {"id": "m2", "method": "outcome_probs", "rationale": "market odds plus a small cut",
                 "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"},
                                      HIKE: {"id": "p2", "role": "prob hike"},
                                      CUT: {"id": "a1", "role": "prob cut"}}}}]


def judge_reply(outcomes=JUDGE_OUTS, basis=BASIS, methods=None, **kw):
    """假裁判的一次回复；outcomes / basis 为 None 时不带这个字段。"""
    r = {"decisions": [], "extra_directions": [], "assumptions": [_a(route="m2")],
         "methods": GOOD_METHODS if methods is None else methods}
    if outcomes is not None:
        r["outcomes"] = outcomes
    if basis is not None:
        r["outcomes_basis"] = basis
    r.update(kw)
    return r


def discrete_graph_run(jev_post=None, allow_discrete=None, judge=None):
    """假模型跑一遍离散目标的整张图，返回最终 state 和看到的 prompt。jev_post 给了就配置一个临时 key 文件和假 HTTP 层。
    allow_discrete 给了就设到 ctx 上（run.prepare_run 对有真值的题的做法）。
    judge：裁判各次调用（r1、r1:repair、r2 ...）依次给的回复；默认每次都是 judge_reply()。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "Upper bound after the next meeting?", "2026-10-15", date(2026, 10, 15)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    if allow_discrete is not None:
        ctx.allow_discrete = allow_discrete
    seen = {}
    replies = list(judge or [judge_reply()])

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            if role == "plan":
                seen["plan_user"] = user
                t = {k: v for k, v in TARGET.items() if k != "outcomes"}
                return {"target": t | {"publisher": "X", "outcome_kind": "policy rate in fixed steps"}, "market_keywords": [],
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
                seen["n_audit"] = seen.get("n_audit", 0) + 1
                return {"methods": []}, None
            if role.startswith("judge"):
                n = len(seen.setdefault("judge_roles", []))
                seen["judge_roles"].append(role)
                seen["judge_user"] = user
                seen.setdefault("judge_users", []).append(user)
                return replies[min(n, len(replies) - 1)], None
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
        self.assertEqual(st["plan"]["target"]["outcome_kind"], "policy rate in fixed steps")
        self.assertNotIn("outcomes", st["plan"]["target"])                   # v2.3：plan 不列结果
        self.assertIn("Only outcome_probs is available", seen["judge_user"])
        self.assertIn("kind of outcome, from the plan: policy rate in fixed steps", seen["judge_user"])
        self.assertIn("Its outcome list is not fixed yet", seen["judge_user"])
        self.assertEqual((st["outcomes"]["list"], st["outcomes"]["defined_round"]), (JUDGE_OUTS, 1))
        self.assertIn("outcome_probs", seen["audit_user"])
        self.assertIn("Outcome list of this discrete target, defined by the analyst from the evidence", seen["audit_user"])
        self.assertIn(f'- "{HIKE}" (value 4.25 percent per annum or higher)', seen["audit_user"])
        self.assertIn('  - data point p1: "Market-implied probability the range is unchanged', seen["audit_user"])
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
        self.assertIn("Outcome list defined by the judge in round 1, from kept points ['p1', 'p2']: p1 and p2 price", led)
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

    def test_jev_node_error_does_not_crash_the_run(self):
        with mock.patch.object(J, "run_arm", side_effect=RuntimeError("boom tsk-secret")):
            st, _ = discrete_graph_run()
        self.assertEqual(st["jev"], {"arm": "jev", "status": "error", "error": "jev arm error RuntimeError"})
        self.assertEqual(st["compute"]["result"]["most_likely"], HOLD)
        self.assertIn("Most likely outcome", st["final"]["text"])

    def test_scored_question_not_marked_discrete_stays_continuous(self):
        st, _ = discrete_graph_run(allow_discrete=False)
        self.assertEqual(st["plan"]["target"]["outcome_type"], "continuous")
        self.assertNotIn("outcomes", st["plan"]["target"])
        self.assertIn("plan chose a discrete target, but this scored question is not marked outcome_type 'discrete'; "
                      "treated as continuous", st["plan_notes"])
        self.assertNotIn("jev", st)
        self.assertNotEqual((st["compute"]["result"] or {}).get("mode"), "discrete")

    def test_prepare_run_sets_allow_discrete(self):
        from triangulate.agent import run as R

        class FakeCtx:   # 真的 Context 会读 DeepSeek key：测试里换掉
            def __init__(self, *a, **kw):
                pass
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(R, "RES", tmp), mock.patch.object(R, "Context", FakeCtx), \
                    mock.patch.object(R, "build", lambda ctx: None):
                for q, want in (({"id": "a", "question": "?", "as_of": "2026-10-15"}, True),
                                ({"id": "b", "question": "?", "as_of": "2026-10-15", "answer_value": 4.0}, False),
                                ({"id": "c", "question": "?", "as_of": "2026-10-15", "answer_value": 4.0,
                                  "outcome_type": "discrete"}, True)):
                    self.assertIs(R.prepare_run(q)["ctx"].allow_discrete, want, q["id"])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class TestJudgeDefinedOutcomes(unittest.TestCase):
    """v2.3：结果列表由裁判第一轮根据保留的证据定义；代码校验（label 唯一、2-6 个、数值型用 le / ge 两个尾部覆盖全部、
    依据的 id 都是保留的点），不合格交回修正轮；之后沿用，最多修订一次；outcome_probs 按裁判的列表算。"""
    KEPT = {"p1", "p2", "p5"}

    def _v(self, outs, basis=None):
        return D.validate_outcomes(outs, {"ids": ["p5"], "note": "current level"} if basis is None else basis, self.KEPT)

    def test_good_lists(self):
        clean, basis, errs = self._v(JUDGE_OUTS)
        self.assertEqual(errs, [])
        self.assertEqual(clean, JUDGE_OUTS)
        self.assertEqual(basis, {"ids": ["p5"], "note": "current level"})
        # 尾部只给界、不给 value：value 取界；字符串数字照样解析；非数值的结果（是 / 否）不需要尾部
        clean, _, errs = self._v([{"label": "3.75% or lower", "le": "3.75"}, {"label": "4.00%", "value": "4.00%"},
                                  {"label": "4.25% or higher", "value": None, "ge": 4.25}])
        self.assertEqual(errs, [])
        self.assertEqual([(c["value"], c.get("le"), c.get("ge")) for c in clean], [(3.75, 3.75, None), (4.0, None, None),
                                                                                   (4.25, None, 4.25)])
        self.assertEqual(self._v([{"label": "yes", "value": None}, {"label": "no"}])[2], [])
        self.assertEqual(self._v(JUDGE_OUTS, ["p1", "p2"])[1]["ids"], ["p1", "p2"])     # 依据可以直接给 id 列表

    def test_bad_lists_rejected(self):
        tail_lo, mid, tail_hi = JUDGE_OUTS
        bad = {
            "need 2 to 6": [tail_lo],
            "7 outcomes": [{"label": "3.00% or lower", "value": 3.0, "le": 3.0}] +
                          [{"label": f"{v:.2f}%", "value": v} for v in (3.25, 3.5, 3.75, 4.0, 4.25)] +
                          [{"label": "4.50% or higher", "value": 4.5, "ge": 4.5}],
            "duplicate outcome label": [tail_lo, mid, {**mid, "label": HOLD.upper()}, tail_hi],
            "has no label": [tail_lo, {"value": 4.0}, tail_hi],
            "the lowest outcome 'cut to 3.75%' must be a merged tail": [{"label": CUT, "value": 3.75}, mid, tail_hi],
            "the highest outcome 'hike to 4.25%' must be a merged tail": [tail_lo, mid, {"label": HIKE, "value": 4.25}],
            "only the lowest outcome may carry le": [tail_lo, {**mid, "le": 4.0}, tail_hi],
            "must equal its value": [{**tail_lo, "le": 3.5}, mid, tail_hi],
            "has both le and ge": [tail_lo, mid, {**tail_hi, "le": 4.25}],
            "le must be a number": [{**tail_lo, "le": "low"}, mid, tail_hi],
            "either every outcome has a numeric value or none has": [tail_lo, {"label": "other", "value": None}, tail_hi],
            "two outcomes have the same value": [tail_lo, mid, {"label": "hold again", "value": 4.0}, tail_hi],
            "either every outcome has a numeric": [{"label": "yes"}, {"label": "no", "le": 0}],   # 界给了数值
            "must be a list": "3.75%, 4.00%",
        }
        for why, outs in bad.items():
            errs = self._v(outs)[2]
            self.assertTrue(any(why in e for e in errs), f"{why}: {errs}")

    def test_basis_ids_must_be_kept_points(self):
        for basis, why in ((None, "outcomes_basis"), ({"ids": []}, "outcomes_basis"), ({"note": "x"}, "outcomes_basis"),
                           ({"ids": ["p6"]}, "['p6'] are not kept data points"),        # 丢掉的点
                           ({"ids": ["p5", "a1"]}, "['a1'] are not kept data points"),   # 假设不能当依据
                           ({"ids": ["p99"]}, "['p99'] are not kept data points")):
            errs = D.validate_outcomes(JUDGE_OUTS, basis, self.KEPT)[2]
            self.assertTrue(any(why in e for e in errs), f"{basis}: {errs}")

    def test_accept_define_reuse_revise(self):
        r1 = {"outcomes": JUDGE_OUTS, "outcomes_basis": BASIS}
        rec, errs = D.accept_outcomes(r1, None, 1, self.KEPT)
        self.assertEqual(errs, [])
        self.assertEqual((rec["list"], rec["basis"]["ids"], rec["defined_round"], rec["revised_round"]),
                         (JUDGE_OUTS, ["p1", "p2"], 1, None))
        self.assertIn("no outcome list yet", D.accept_outcomes({}, None, 1, self.KEPT)[1][0])
        bad = D.accept_outcomes({"outcomes": JUDGE_OUTS[:1], "outcomes_basis": BASIS}, None, 1, self.KEPT)
        self.assertIsNone(bad[0])
        self.assertTrue(bad[1][0].startswith("outcome list: 1 outcomes"))
        # 之后的轮次：不给、或给一样的列表 = 沿用（不算修订）
        self.assertIs(D.accept_outcomes({}, rec, 2, self.KEPT)[0], rec)
        self.assertIs(D.accept_outcomes({"outcomes": [dict(o) for o in JUDGE_OUTS]}, rec, 2, self.KEPT)[0], rec)
        # 修订：要理由；有理由且合格才换，记下原来的列表
        new = [{"label": "4.00% or lower", "value": 4.0, "le": 4.0}, {"label": "4.25%", "value": 4.25},
               {"label": "4.50% or higher", "value": 4.5, "ge": 4.5}]
        same, errs = D.accept_outcomes({"outcomes": new, "outcomes_basis": {"ids": ["p5"]}}, rec, 2, self.KEPT)
        self.assertIs(same, rec)
        self.assertIn("needs \"outcomes_revision_reason\"", errs[-1])
        rev, errs = D.accept_outcomes({"outcomes": new, "outcomes_basis": {"ids": ["p5"]},
                                       "outcomes_revision_reason": "p5 shows the current level is 4.25%"}, rec, 2, self.KEPT)
        self.assertEqual(errs, [])
        self.assertEqual((rev["list"], rev["defined_round"], rev["revised_round"], rev["previous_list"]), (new, 1, 2, JUDGE_OUTS))
        again, errs = D.accept_outcomes({"outcomes": JUDGE_OUTS, "outcomes_basis": BASIS, "outcomes_revision_reason": "x"},
                                        rev, 3, self.KEPT)
        self.assertIs(again, rev)
        self.assertIn("already revised in round 2", errs[0])

    def test_outcome_probs_against_judge_defined_outcomes(self):
        plan_target = {k: v for k, v in TARGET.items() if k != "outcomes"}
        rec = D.accept_outcomes({"outcomes": JUDGE_OUTS, "outcomes_basis": BASIS}, None, 1, self.KEPT)[0]
        t = D.with_outcomes(plan_target, rec)
        self.assertEqual((t["outcomes"], t["outcomes_basis"]["ids"]), (JUDGE_OUTS, ["p1", "p2"]))
        self.assertIs(D.with_outcomes(plan_target, None), plan_target)
        out = C.run([{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}, HIKE: {"id": "p2"}}, "remainder": CUT}},
                     {"method": "outcome_probs", "params": {"probs": {"4.00%": {"id": "p1"}}, "remainder": HIKE}}],
                    dict(PTS), t)
        self.assertNotIn("error", out["methods"][0])
        self.assertIn("unknown outcome label '4.00%'", out["methods"][1]["error"])   # 只认裁判列表里的 label
        r = out["result"]
        self.assertEqual([o["label"] for o in r["outcomes"]], [CUT, HOLD, HIKE])
        self.assertEqual((r["outcomes"][0]["le"], r["outcomes"][2]["ge"]), (3.75, 4.25))   # 尾部的界跟着结果走
        self.assertEqual(r["most_likely"], HOLD)
        # 没有合格的列表：每个方法都报 no outcome list，没有结果
        none = C.run([{"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1"}}, "remainder": HIKE}}], dict(PTS), plan_target)
        self.assertIn("no outcome list", none["methods"][0]["error"])
        self.assertIsNone(none["result"]["most_likely"])
        # 打分：le / ge 标的尾部认超出它的真值（label 不必写 or lower）
        s = D.score({"outcomes": [{**o, "prob": p} for o, p in zip(JUDGE_OUTS, (0.1, 0.6, 0.3))], "most_likely": HOLD}, 3.5)
        self.assertEqual((s["true_outcome"], s["prob_true"]), (CUT, 0.1))
        self.assertEqual(D.score({"outcomes": [{**o, "prob": 0.3} for o in JUDGE_OUTS]}, 5.0)["true_outcome"], HIKE)

    @unittest.skipUnless(HAVE_LG, "langgraph not installed")
    def test_audit_rows_check_the_judge_defined_outcome(self):
        from triangulate.agent import graph as G
        t = D.with_outcomes({k: v for k, v in TARGET.items() if k != "outcomes"},
                            {"list": JUDGE_OUTS, "basis": {"ids": ["p5"], "note": "n"}})
        mi = {"method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1", "role": "prob unchanged"}}, "remainder": CUT}}
        out = C.run([{**mi, "params": {**mi["params"], "probs": {**mi["params"]["probs"], HIKE: {"id": "p2", "role": "r"}}}}],
                    dict(PTS), t)["methods"][0]
        rows = G.audit_rows(mi, out, {p["id"]: p for p in PTS.values()}, {}, t)
        self.assertEqual(rows[0][2], "probability that the target resolves to outcome 'unchanged at 4.00%' (value 4 percent "
                                     "per annum); analyst's role: prob unchanged")
        self.assertEqual(rows[-1][2], "probability that the target resolves to outcome 'cut to 3.75%' (value 3.75 percent "
                                      "per annum or lower), taken as the rest (1 minus the other inputs)")


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestJudgeDefinedOutcomesGraph(unittest.TestCase):
    """整张图（假模型）：列表不合格交回修正轮、修正后仍不合格就没有结果、第二轮沿用或修订第一轮的列表。"""
    EXTRA = [{"id": "b1", "category": "forecasts_markets", "hypothesis": "more odds", "data_to_find": "f",
              "search_hints": ["q"]}]

    def test_bad_list_goes_back_to_the_repair_round(self):
        seven = [{"label": "3.00% or lower", "value": 3.0, "le": 3.0}] + \
                [{"label": f"{v:.2f}%", "value": v} for v in (3.25, 3.5, 3.75, 4.0, 4.25)] + \
                [{"label": "4.50% or higher", "value": 4.5, "ge": 4.5}]
        # 第一次：7 个结果、依据里有一个这一轮丢掉的点（p2 被丢，方法也只用 p1）；修正：合格的列表
        one = [{"id": "m1", "method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1", "role": "r"}}, "remainder": HIKE}}]
        bad = judge_reply(outcomes=seven, basis={"ids": ["p1", "p2"]}, methods=one,
                          decisions=[{"id": "p2", "keep": False, "reason": "duplicate"}])
        good = judge_reply(basis={"ids": ["p1"], "note": "p1"}, methods=one, decisions=bad["decisions"])
        st, seen = discrete_graph_run(judge=[bad, good])
        self.assertEqual(seen["judge_roles"], ["judge:r1", "judge:r1:repair"])
        jr = st["judge_rounds"][0]
        errs = jr["repair"]["errors"]
        self.assertTrue(any(e.startswith("outcome list: 7 outcomes") for e in errs), errs)
        self.assertTrue(any("['p2'] are not kept data points" in e for e in errs), errs)
        self.assertTrue(any("no outcome list" in e for e in errs), errs)      # 方法因为没有列表也算不出
        self.assertIn("Code rejected the outcome list in your previous reply", seen["judge_users"][1])
        self.assertIn('"3.00% or lower"', seen["judge_users"][1])              # 修正轮看得到被拒的列表
        self.assertEqual(jr["repair"]["outcome_errors_after"], [])
        self.assertEqual(st["outcomes"]["list"], JUDGE_OUTS)
        self.assertEqual(st["outcomes"]["basis"]["ids"], ["p1"])
        r = st["compute"]["result"]
        self.assertEqual(r["most_likely"], HOLD)
        self.assertAlmostEqual({o["label"]: o["prob"] for o in r["outcomes"]}[HIKE], 1 - 0.564)

    def test_still_invalid_after_repair_ends_without_estimate(self):
        bad = judge_reply(outcomes=[{"label": CUT, "value": 3.75}, {"label": HOLD, "value": 4.0}])   # 没有尾部
        st, seen = discrete_graph_run(judge=[bad, bad])
        self.assertEqual(seen["judge_roles"], ["judge:r1", "judge:r1:repair"])
        self.assertIsNone(st["outcomes"])
        self.assertTrue(st["judge_rounds"][0]["repair"]["outcome_errors_after"])
        self.assertTrue(all("no outcome list" in m["error"] for m in st["compute"]["methods"]))
        self.assertIsNone(st["compute"]["result"]["most_likely"])
        self.assertEqual(st["jev"]["status"], "skipped")
        self.assertEqual(st["final"]["text"], "No estimate: the judge did not define a valid outcome list for this discrete target.")
        self.assertNotIn("n_audit", seen)                                        # 方法都没跑通：没有输入核对

    def test_round_two_reuses_the_round_one_list(self):
        # 第一轮还要再搜：列表不合格也立刻修（只修列表，方法不核对）；第二轮不给 outcomes = 沿用第一轮的列表
        bad = judge_reply(basis={"ids": ["a1"]}, extra_directions=self.EXTRA)
        fixed = judge_reply(extra_directions=self.EXTRA)
        r2 = judge_reply(outcomes=None, basis=None)
        st, seen = discrete_graph_run(judge=[bad, fixed, r2])
        self.assertEqual(seen["judge_roles"], ["judge:r1", "judge:r1:repair", "judge:r2"])
        j1, j2 = st["judge_rounds"]
        self.assertEqual(j1["repair"]["errors"], ["outcome list: outcomes_basis ids ['a1'] are not kept data points "
                                                  "(assumptions, discarded or unknown ids cannot ground the outcome list)"])
        self.assertNotIn("audit_failed", j1)                                     # 第一轮的方法不核对（第二轮才是最终的）
        self.assertIn("Its outcome list is not fixed yet", seen["judge_users"][0])
        self.assertIn("which you defined in judge round 1 from kept points p1, p2", seen["judge_users"][2])
        self.assertIn(f'- "{CUT}" (value 3.75 percent per annum or lower)', seen["judge_users"][2])
        self.assertIn("you may revise it once", seen["judge_users"][2])
        self.assertEqual(j2["outcome_errors"], [])
        self.assertEqual((st["outcomes"]["defined_round"], st["outcomes"]["revised_round"]), (1, None))
        self.assertEqual(st["compute"]["methods_from_round"], 2)
        self.assertEqual(st["compute"]["result"]["most_likely"], HOLD)

    def test_round_two_may_revise_once(self):
        new = [{"label": "4.00% or lower", "value": 4.0, "le": 4.0}, {"label": "4.25% or higher", "value": 4.25, "ge": 4.25}]
        ms = [{"id": "m1", "method": "outcome_probs",
               "params": {"probs": {"4.00% or lower": {"id": "p3", "role": "r"}, "4.25% or higher": {"id": "p4", "role": "r"}}}}]
        r2 = judge_reply(outcomes=new, basis={"ids": ["p3", "p4"], "note": "new odds"}, methods=ms,
                         outcomes_revision_reason="p3 and p4 show only a hold or a hike are priced")
        st, seen = discrete_graph_run(judge=[judge_reply(extra_directions=self.EXTRA), r2])
        self.assertEqual(seen["judge_roles"], ["judge:r1", "judge:r2"])
        o = st["outcomes"]
        self.assertEqual((o["list"], o["defined_round"], o["revised_round"], o["previous_list"]), (new, 1, 2, JUDGE_OUTS))
        self.assertIn("p3 and p4 show", o["revision_reason"])
        r = st["compute"]["result"]
        self.assertEqual([x["label"] for x in r["outcomes"]], ["4.00% or lower", "4.25% or higher"])
        self.assertEqual(r["most_likely"], "4.00% or lower")
        from triangulate.agent import outputs
        self.assertIn("Outcome list defined by the judge in round 1; revised in round 2 (p3 and p4 show", outputs.ledger(st, None))


class TestV221Fixes(unittest.TestCase):
    """v2.2.1 审查意见的修复：只有假设的方法、一个 id 给两个结果、不是概率的点、离散方法互相打架、尾部结果打分、
    离散运行的 score_all、Jev 的 HTTPException。"""

    def test_method_needs_a_kept_point(self):
        av = [_a(value=25, low=15, high=35, name="probability of a hike"), _a(id="a2", value=5, low=2, high=8)]
        m = _run({HIKE: {"id": "a1"}, CUT: {"id": "a2"}}, remainder=HOLD, assumptions=av)["methods"][0]   # discrete4 第 1 轮
        self.assertIn("needs at least one kept data point", m["error"])
        self.assertIsNone(_run({HIKE: {"id": "a1"}, CUT: {"id": "a2"}}, remainder=HOLD, assumptions=av)["result"]["most_likely"])
        ok = _run({HIKE: {"id": "p2"}, CUT: {"id": "a2"}}, remainder=HOLD, assumptions=av)["methods"][0]
        self.assertNotIn("error", ok)

    def test_one_id_one_outcome(self):
        m = _run({HOLD: {"id": "p1"}, HIKE: {"id": "p1"}}, remainder=CUT)["methods"][0]
        self.assertIn("id p1 is used for outcomes 'unchanged at 4.00%' and 'hike to 4.25%'; one probability denotes one "
                      "outcome", m["error"])
        a = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a1"}, CUT: {"id": "a1"}}, assumptions=[_a(value=40, low=30, high=50)])
        self.assertIn("id a1 is used for outcomes", a["methods"][0]["error"])

    def test_points_must_be_probabilities(self):
        pts = dict(PTS)
        pts["p8"] = _pt("p8", 22.1, unit="percentage points", name="change in implied probability of a hike")
        pts["p9"] = _pt("p9", 4.1, unit="percent", name="unemployment rate")
        pts["p10"] = _pt("p10", 25.0, unit="bp", name="probability-weighted expected move")
        for pid, want in (("p8", "is a change or difference"), ("p9", "is not stated as a probability"),
                          ("p10", "is a change or difference")):
            m = C.run([{"method": "outcome_probs", "params": {"probs": {HIKE: {"id": pid}}, "remainder": HOLD}}], pts, TARGET)
            self.assertIn(want, m["methods"][0]["error"], pid)
        a = _run({HOLD: {"id": "p1"}, HIKE: {"id": "a1"}}, remainder=CUT,
                 assumptions=[_a(value=20, low=10, high=30, unit="percentage points")])["methods"][0]
        self.assertIn("is a change or difference", a["error"])
        # 名字带 probability（FedWatch）、unit = probability（markets.py）、percent probability：照旧通过
        for pid in ("p1", "p3", "p4"):
            self.assertNotIn("error", _run({HIKE: {"id": pid}}, remainder=HOLD)["methods"][0], pid)

    @unittest.skipUnless(HAVE_LG, "langgraph not installed")
    def test_discrete_methods_that_disagree_go_back_to_the_judge(self):
        from triangulate.agent import graph as G
        jr = {"methods": [{"id": "m1", "method": "outcome_probs",
                           "params": {"probs": {HOLD: {"id": "p1"}, HIKE: {"id": "p2"}}, "remainder": CUT}},
                          {"id": "m2", "method": "outcome_probs",
                           "params": {"probs": {CUT: {"id": "p1"}, HIKE: {"id": "p2"}}, "remainder": HOLD}}]}
        out, av, failed = G._code_check(jr, list(PTS.values()), TARGET)
        n_ok, probs = G._problems(jr, out, av, failed)
        self.assertEqual(n_ok, 2)
        self.assertEqual(len(probs), 1)
        self.assertIn("methods disagree: m1 gives most likely 'unchanged at 4.00%' (56.4%) but m2 gives most likely "
                      "'cut to 3.75%' (56.4%) (total variation distance 0.56, more than 0.5)", probs[0])

    def test_scoring_merged_tails(self):
        r = {"outcomes": [{"label": "4.00% or lower", "value": 4.0, "prob": 0.6}, {"label": "4.25%", "value": 4.25, "prob": 0.4},
                          {"label": "4.50% or higher", "value": 4.5, "prob": 0.0}], "most_likely": "4.00% or lower"}
        s = D.score(r, 3.75)
        self.assertEqual((s["true_outcome"], s["most_likely_correct"]), ("4.00% or lower", True))
        self.assertAlmostEqual(s["prob_true"], 0.6)
        self.assertAlmostEqual(s["brier"], 0.16 + 0.16)
        self.assertEqual(D.score(r, 4.0)["true_outcome"], "4.00% or lower")
        self.assertEqual(D.score(r, 4.25)["true_outcome"], "4.25%")
        self.assertEqual(D.score(r, 5.0)["true_outcome"], "4.50% or higher")
        self.assertIsNone(D.score({"outcomes": r["outcomes"][1:2]}, 3.75)["true_outcome"])   # 没有尾部：照旧不在列表里

    @unittest.skipUnless(HAVE_LG, "langgraph not installed")
    def test_score_all_discrete_has_no_point_estimate_arms(self):
        from triangulate.agent import run as R
        tmp = Path(tempfile.mkdtemp())
        st = {"compute": {"result": {"mode": "discrete", "central": 0.0, "most_likely": "no",
                                     "outcomes": [{"label": "yes", "value": 1.0, "prob": 0.3}, {"label": "no", "value": 0.0, "prob": 0.7}]}},
              "budget": {"usd_total_assumed": 0.1, "usd_tokens": 0.05}, "wall_s": 1.0}
        try:
            (tmp / "q").mkdir()
            (tmp / "q" / "state.json").write_text(json.dumps(st), encoding="utf-8")
            with mock.patch.object(R, "RES", tmp):
                rows = R.score_all([{"id": "q", "as_of": "2026-10-15", "answer_value": 0.0}])   # 真值 0：以前除零
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(rows[0]["true_outcome"], "no")
        self.assertAlmostEqual(rows[0]["prob_true"], 0.7)
        self.assertNotIn("arms", rows[0])
        self.assertNotIn("within_20pct", rows[0])
        self.assertEqual(rows[0]["usd_total_assumed"], 0.1)

    def test_jev_http_exception_is_an_error_not_a_crash(self):
        import http.client

        def broken(url, body, headers, timeout):
            raise http.client.IncompleteRead(b"{", 10)
        out = J.run_arm(TARGET, TestJevClient.PTS, "2026-10-15",
                        client=J.JevClient("k", post=broken, sleep=lambda s: None))
        self.assertEqual(out["status"], "error")
        self.assertIn("IncompleteRead", out["error"])


if __name__ == "__main__":
    unittest.main()

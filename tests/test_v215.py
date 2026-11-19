"""v2.15：三方审计 + GPT 评估之后的五处小修（2026-11-19）。
a 报错里的数字格式；b 裁判 JSON 少右花括号时定点补上，补不好再关思考重问；c 百分数假设写成小数时交回确认；
d 量级闸门（和不联网直接问的粗估比，差 2 倍以上定向修正一次）；e 抽取每页上限 15 -> 30。"""
import json
import unittest
from datetime import date
from unittest import mock

from triangulate import llm
from triangulate.agent import assumptions as AS
from triangulate.agent import graph as G
from triangulate.agent import magnitude as MG
from triangulate.agent import pipeline as P

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False


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
    {"id": "m1", "method": "formula_mc", "params": {"formula": "a * b", "inputs": {"a": {"id": "p1", "role": "r"},
                                                                                   "b": {"id": "a1", "role": "s"}}},
     "unit": "car", "coverage": {"kind": "part", "part": "Bavaria"}, "rationale": "r1"},
    {"id": "m2", "method": "formula_mc", "params": {"formula": "c", "inputs": {"c": {"id": "p2", "role": "t"}}},
     "unit": "car", "rationale": "r2"}],
    "assumptions": [{"id": "a1", "value": 0.5}]}


def _drop(text: str, marker: str) -> str:
    """删掉 marker 结尾的那个右花括号（marker 在 text 里唯一）。"""
    i = text.index(marker) + len(marker) - 1
    assert text[i] == "}"
    return text[:i] + text[i + 1:]


class TestBraceRepair(unittest.TestCase):
    """v2.15b / v2.15f：存档里裁判 JSON 损坏、带出错片段的 24 次里 23 次是同一种报错（下一个 {"id": ...} 处 Expecting property
    name），而且出错点前面那个 } 在：少的是里层的括号（某个输入、inputs、params），不是方法自己的。v2.15b 补在末尾会让
    unit / coverage / rationale 掉进 params（审查复现）；v2.15f 在当前方法里逐个逗号试补，只收结构检查通过的。"""

    def check(self, bad: str, good=GOOD):
        with self.assertRaises(json.JSONDecodeError) as cm:
            json.loads(bad)
        self.assertTrue(cm.exception.msg.startswith("Expecting property name"))
        return llm.close_missing_braces(bad, G.judge_shape_ok)

    def test_inner_brace_missing_archive_signature(self):
        for sep in ((",", ":"), (", ", ": ")):
            text = json.dumps(GOOD, separators=sep)
            k = sep[1]
            for marker in ('"role"%s"s"}' % k,                     # 输入 b 没关
                           '"role"%s"s"}}' % k,                    # inputs 没关
                           '"role"%s"s"}}}' % k,                   # params 没关
                           '"Bavaria"}' % ()):                     # coverage 没关
                bad = _drop(text, marker)
                self.assertTrue(bad[:bad.index('{"id"%s"m2"' % k)].rstrip().endswith("},") or marker == '"Bavaria"}',
                                marker)
                self.assertEqual(self.check(bad), (GOOD, 1), (sep, marker))

    def test_method_brace_missing(self):
        text = json.dumps(GOOD, separators=(",", ":"))
        self.assertEqual(self.check(_drop(text, '"rationale":"r1"}')), (GOOD, 1))

    def test_two_missing_braces_go_to_the_retry(self):
        text = json.dumps(GOOD, separators=(",", ":"))
        bad = _drop(_drop(text, '"role":"s"}}}'), '"role":"s"}}')
        self.assertEqual(llm.close_missing_braces(bad, G.judge_shape_ok), (None, 0))

    def test_other_breakage_is_left_alone(self):
        # 抽取员那种坏法（多出一个孤立的 null 当键名）不是这一种：不修，照旧交给重问
        text = '{"points": [{"low": null, null: null, "high": null}]}'
        self.assertEqual(llm.close_missing_braces(text, G.judge_shape_ok), (None, 0))
        self.assertEqual(llm.close_missing_braces('{"a": [1, 2,]}', G.judge_shape_ok), (None, 0))

    def test_shape_check(self):
        self.assertTrue(G.judge_shape_ok(GOOD))
        moved = json.loads(json.dumps(GOOD))
        moved["methods"][0]["params"]["rationale"] = moved["methods"][0].pop("rationale")
        self.assertFalse(G.judge_shape_ok(moved))
        nested = json.loads(json.dumps(GOOD))
        nested["methods"][0]["params"]["inputs"]["a"]["b"] = nested["methods"][0]["params"]["inputs"].pop("b")
        self.assertFalse(G.judge_shape_ok(nested))

    def _json_call(self, bad, **kw):
        def fake_post(req, **k):
            reply = {"choices": [{"message": {"content": bad}, "finish_reason": "stop"}], "usage": {}}
            return 200, json.dumps(reply).encode()

        with mock.patch.object(llm, "read_key", return_value="k"), \
                mock.patch.object(llm.LLM, "_post", staticmethod(fake_post)), mock.patch.object(llm.LLM, "_log") as log:
            out, _, err = llm.LLM().json_call([{"role": "user", "content": "json"}], arm="judge:r1", qid="q", attempt=1,
                                              **kw)
        return out, err, log.call_args[0][0]

    def test_json_call_repairs_only_with_a_shape_check(self):
        bad = _drop(json.dumps(GOOD, separators=(",", ":")), '"role":"s"}}}')
        out, err, rec = self._json_call(bad, shape_check=G.judge_shape_ok)
        self.assertIsNone(err)
        self.assertEqual(out, GOOD)
        self.assertTrue(rec["ok"])
        self.assertEqual(rec["json_repaired"]["braces_inserted"], 1)
        self.assertIn("Expecting property name", rec["json_repaired"]["json_error"])
        out, err, rec = self._json_call(bad)   # 不是裁判（基线、抽取……）：不补，照旧报不合法
        self.assertIsNone(out)
        self.assertEqual(err, "reply is not valid JSON")
        self.assertEqual(rec["error"], "invalid_json")


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
        self.assertIn('(0.0085) with unit "fraction"', why)

    def test_both_rewrites_pass(self):
        r = AS.validate([_a("a5", 85, "%", 75, 92), _a("a6", 0.0085, "fraction", 0.007, 0.01)], {"unit": "person"})
        self.assertEqual([a["id"] for a in r["kept"]], ["a5", "a6"])
        self.assertAlmostEqual(r["kept"][0]["p10_used"] * r["kept"][0]["p90_used"], 0.75 * 0.92)
        # 存档重放：名字指向目标的变化量（英国轿车 9 月同比、LHR 损失）照建议写成 fraction 也能过 target_reason
        r = AS.validate([_a("a1", 0.0002, "fraction", 0.00001, 0.0012, name="September 2026 YoY change in UK car production")],
                        {"unit": "car", "what": "cars manufactured in the United Kingdom in September 2026"})
        self.assertEqual([a["id"] for a in r["kept"]], ["a1"])

    def test_percent_one_or_more_and_percentage_points_unchanged(self):
        r = AS.validate([_a("a1", 1.0, "%"), _a("a2", 24.7, "percent"), _a("a3", 0.5, "percentage points", name="change")],
                        {"unit": "person"})
        self.assertEqual([a["id"] for a in r["kept"]], ["a1", "a2", "a3"])

    def test_repair_scope_names_only_that_assumption(self):
        r = AS.validate([_a("a5", 0.85, "%")], {"unit": "person"})
        err = f"assumption a5 rejected: {r['rejected'][0]['reason']}"
        self.assertEqual(G._repair_scope([err], [])[1], {"a5"})


class TestMagnitudeParts(unittest.TestCase):
    """v2.15d：量级闸门的零件。"""

    def test_parse_reply(self):
        self.assertEqual(MG._parse({"estimate": 60337.4, "unit": "CNY*10**8"}, None, "CNY*10**8")["estimate"], 60337.4)
        r = MG._parse({"estimate": 6.03e12, "unit": "CNY"}, None, "CNY*10**8")
        self.assertEqual(r["status"], "ok")
        self.assertAlmostEqual(r["estimate"], 60300.0)
        self.assertEqual(MG._parse({"estimate": 5, "unit": "billion USD"}, None, "USD")["status"], "unit_unreconciled")
        self.assertEqual(MG._parse({"estimate": "about 5", "unit": "USD"}, None, "USD")["status"], "invalid")
        self.assertEqual(MG._parse(None, "reply is not valid JSON", "USD")["status"], "error")

    def bcg(self):
        # BCG 11-12 的形状：m1 = 0.069（% 小 100 倍）、m4 = 101、m2 = 15,043；粗估假设是 10,000
        by_id = {"p1": {"id": "p1", "value": 33.5, "unit": "person"}, "p317": {"id": "p317", "value": 12103, "unit": "person"},
                 "p224": {"id": "p224", "value": 6.1e9, "unit": "USD"}}
        kept_a = {"a5": {"id": "a5", "value": 0.85, "unit": "%", "is_pct": True},
                  "a3": {"id": "a3", "value": 430000, "unit": "USD/person", "is_pct": False}}
        ms = [{"id": "m1", "method": "formula_mc", "estimate": 0.069,
               "inputs_detail": [{"id": "p1", "kind": "point"}, {"id": "a5", "kind": "assumption"}]},
              {"id": "m4", "method": "formula_mc", "estimate": 101.0,
               "inputs_detail": [{"id": "p317", "kind": "point"}, {"id": "a5", "kind": "assumption"}]},
              {"id": "m2", "method": "formula_mc", "estimate": 15043.0,
               "inputs_detail": [{"id": "p224", "kind": "point"}, {"id": "a3", "kind": "assumption"}]}]
        return ms, by_id, kept_a

    def test_check_names_the_far_methods_and_spells_out_inputs(self):
        ms, by_id, kept_a = self.bcg()
        rec, lines = MG.check({"status": "ok", "estimate": 10000.0}, 101.0, ms, by_id, kept_a)
        self.assertEqual(rec["status"], "off")
        # v2.15g：点名全部能用的方法，只说合并值偏低（不说哪条在 2 倍以内，免得泄露粗估的范围）
        self.assertEqual([x.split(" ")[1] for x in lines], ["m1", "m4", "m2"])
        self.assertIn("the combined estimate of the usable methods (101) is more than 2x below", lines[1])
        self.assertIn("this method gives 101", lines[1])
        self.assertIn("a5 = 0.85 % = 0.0085 as a fraction", lines[1])
        self.assertIn("p317 = 12,103 person", lines[1])
        self.assertTrue(all("10,000" not in x and "10000" not in x for x in lines))   # 粗估的数不进报错
        self.assertEqual(G._repair_scope(lines, [])[0], {"m1", "m4", "m2"})

    def test_result_unit_and_series_inputs_are_spelled_out(self):
        # 美国零售 test3：p6 记的是 millions of USD，方法的单位被定成 USD、倍数 1；series 方法没有逐项输入
        by_id = {"p6": {"id": "p6", "value": 763705.0, "unit": "millions of USD"},
                 "p7": {"id": "p7", "value": 41, "unit": "car", "unit_calc": "car/month"}}
        ms = [{"id": "m1", "method": "formula_mc", "estimate": 766400.0, "inputs_detail": [{"id": "p6", "kind": "point"}],
               "unit_check": {"unit": "USD", "target_unit": "USD", "factor": 1.0}},
              {"id": "m2", "method": "series_auto", "estimate": 770000.0, "used_ids": ["p7", "p6"]}]
        _, lines = MG.check({"status": "ok", "estimate": 7.4e11}, 768000.0, ms, by_id, {})
        self.assertIn("p6 = 763,705 millions of USD", lines[0])
        self.assertIn("code reads this method's result in USD and converts it to the target unit USD with factor 1", lines[0])
        self.assertIn("p7 = 41 car/month (recorded unit car); p6 = 763,705 millions of USD", lines[1])
        self.assertNotIn("code reads them as: )", lines[1])

    def test_within_ratio_or_no_reference_is_quiet(self):
        ms, by_id, kept_a = self.bcg()
        self.assertEqual(MG.check({"status": "ok", "estimate": 12000.0}, 15043.0, ms, by_id, kept_a)[1], [])
        rec, lines = MG.check({"status": "error"}, 101.0, ms, by_id, kept_a)
        self.assertEqual((rec["status"], lines), ("not_checked", []))

    def test_final_note(self):
        self.assertEqual(MG.final_note(MG.final_record({"status": "ok", "estimate": 100.0}, 150.0)), "")
        note = MG.final_note(MG.final_record({"status": "ok", "estimate": 10000.0}, 101.0, repair_sent=True))
        self.assertIn("about 99.0 times below", note)
        self.assertIn("one targeted repair did not close the gap", note)
        self.assertNotIn("10,000", note)
        # v2.15f：闸门第一次偏出时修正轮已经用完，报错没发出去：终稿不能说修过
        self.assertIn("the judge was not asked to re-check it",
                      MG.final_note(MG.final_record({"status": "ok", "estimate": 10000.0}, 101.0)))
        self.assertEqual(MG.final_record({"status": "ok", "estimate": 10.0}, None)["status"], "not_checked")


MONTHS = ((2023, 6, 30, "June", 1000), (2024, 6, 30, "June", 1100), (2025, 6, 30, "June", 1210),
          (2025, 5, 31, "May", 1000), (2026, 5, 31, "May", 1000))
M_A = {"id": "m1", "method": "series_auto", "params": {"target_history": ["p1", "p2", "p3", "p4", "p5"]}}
M_B = {"id": "m3", "method": "formula_mc", "unit": "widget",
       "params": {"formula": "c * c / d", "inputs": {"c": {"id": "p3", "role": "June 2025 widgets"},
                                                     "d": {"id": "p2", "role": "June 2024 widgets"}}}}


def run_gate(rough):
    """裁判层面：单位钉成 widget，两条路线都约 1,200；粗估给 rough（None = 粗估调用失败）。返回 (state, 角色, {角色: user})。"""
    from langgraph.types import Command

    from triangulate.agent import unit_review as UR
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    roles, users = [], {}

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            roles.append(role)
            users[role] = user
            if role == "plan":
                return {"target": {"what": "widgets", "unit": "widget", "unit_canonical": "widget",
                                   "period_start": "2026-06-01", "period_end": "2026-06-30", "publisher": "X"},
                        "market_keywords": [], "directions": [{"category": "own_history", "hypothesis": "h",
                                                               "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": [{"name": f"widgets {mon} {y}", "value_as_written": f"{v:,}", "unit": "widget",
                                    "unit_calc": "widget", "period_start": f"{y}-{mo:02d}-01",
                                    "period_end": f"{y}-{mo:02d}-{d}", "quote": f"{mon} {y}: {v:,} widgets"}
                                   for y, mo, d, mon, v in MONTHS]}, None
            if role.startswith("judge"):   # 修正轮原样交回同样的两条路线（输入都对）
                return {"decisions": [], "extra_directions": [], "methods": [M_A, M_B]}, None
            if role == MG.ROLE:
                return ({"estimate": rough, "unit": "widget"}, None) if rough else (None, "reply is not valid JSON")
            if role == "audit":
                return {"methods": []}, None
            if role == "final":
                return {"answer": "About [[estimate]]."}, None
            raise AssertionError(role)

    class FakeSearcher:
        def search(self, prompt, *, role, qid, max_uses=3, cap=5):
            return {"queries": ["q"], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}

    def fake_fetch(url, as_of, qid, **kw):
        return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                "text": " ".join(f"{mon} {y}: {v:,} widgets." for y, _, _, mon, v in MONTHS)}

    ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
    with mock.patch.object(P, "fetch_page", fake_fetch), mock.patch.object(UR, "review", lambda *a, **k: None), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "t1"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        st = dict(g.get_state(cfg).values)
    return st, roles, users


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestMagnitudeGate(unittest.TestCase):
    def test_far_off_triggers_exactly_one_repair_and_a_final_note(self):
        st, roles, users = run_gate(1_200_000)
        self.assertEqual(roles.count(MG.ROLE), 1)
        self.assertEqual([r for r in roles if r.startswith("judge")], ["judge:r1", "judge:r1:repair"])
        rep = users["judge:r1:repair"]
        self.assertIn("magnitude check", rep)
        self.assertNotIn("1,200,000", rep)
        jr = st["judge_rounds"][-1]
        self.assertTrue(jr["magnitude_repair_sent"])
        self.assertEqual([c["status"] for c in jr["magnitude_checks"]], ["off", "off"])
        self.assertEqual(st["compute"]["magnitude"]["status"], "off")
        self.assertIn("Magnitude check: this estimate is about", st["final"]["text"])
        self.assertIn("one targeted repair did not close the gap", st["final"]["text"])
        self.assertTrue(st["compute"]["magnitude"]["repair_sent"])
        self.assertIn("times below", st["final"]["text"])
        self.assertIsNotNone(st["compute"]["result"]["central"])   # 不准不出数：数照出

    def test_close_reference_changes_nothing(self):
        st, roles, _ = run_gate(1250)
        self.assertEqual([r for r in roles if r.startswith("judge")], ["judge:r1"])
        self.assertEqual(st["compute"]["magnitude"]["status"], "ok")
        self.assertNotIn("Magnitude check", st["final"]["text"])

    def test_failed_reference_leaves_the_run_alone(self):
        st, roles, _ = run_gate(None)
        self.assertEqual([r for r in roles if r.startswith("judge")], ["judge:r1"])
        self.assertEqual(st["compute"]["magnitude"]["status"], "not_checked")
        self.assertEqual(roles.count(MG.ROLE), 1)   # 失败也只问一次（缓存），compute 不再问


if __name__ == "__main__":
    unittest.main()

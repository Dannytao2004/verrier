"""v2.16（2026-11-24，11-19 回归前 6 次的分析之后）：a 抽取上限退回 15；b 不合法 JSON 存完整原始回复（测试在 test_v215 /
test_providers）；c S84：修正报错写明方法用到的已丢弃点和丢弃理由，修正回复只采用对这些点的 keep:true。"""
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import graph as G
from triangulate.agent import magnitude as MG
from triangulate.agent import pipeline as P
from triangulate.agent import prompts as PR

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False


class TestExtractCap(unittest.TestCase):
    def test_cap_is_15(self):
        self.assertIn("Extract up to 15 relevant numeric facts", PR.EXTRACT_USER)


def _pts():
    return {"p61": {"id": "p61", "keep": False, "judge_reason": "retained only via the 12-month route"},
            "p63": {"id": "p63", "keep": False, "judge_reason": "kept via m2"},
            "p70": {"id": "p70", "keep": True, "judge_reason": ""}}


M1 = {"id": "m1", "method": "formula_mc", "params": {"formula": "p61 * p63 * p70", "inputs": {
    "p61": {"id": "p61", "role": "July level"}, "p63": {"id": "p63", "role": "annual"}, "p70": {"id": "p70", "role": "x"}}}}


class TestExplainDiscarded(unittest.TestCase):
    def test_all_discarded_inputs_with_round_and_reason(self):
        errs = ["method m1 (formula_mc): input p61: id p61 unknown or discarded", "method m2 (formula_mc): other problem"]
        out, rest = G._explain_discarded(errs, [M1], _pts(), {"p61"})
        self.assertEqual(rest, {"p61", "p63"})
        self.assertEqual(out[1], errs[1])
        line = out[0]
        self.assertTrue(line.startswith("method m1 (formula_mc): it uses discarded data points"))
        self.assertIn('p61 (discarded by your decisions in this round; reason given: "retained only via the 12-month route")',
                      line)
        self.assertIn('p63 (discarded by an earlier round; reason given: "kept via m2")', line)
        self.assertNotIn("p70 (", line)   # 保留着的点不列
        self.assertIn('{"id": "p61", "keep": true, "reason": "..."}', line)
        self.assertEqual(G._repair_scope(out[:1], [])[0], {"m1"})   # 修正范围照旧点名这个方法

    def test_quoted_reason_does_not_widen_the_repair_scope(self):
        # v2.16c 审查：理由原文里的 m2 / a2 / p70 不能把没点名的方法、假设解锁
        pts = _pts()
        pts["p61"]["judge_reason"] = 'superseded by a2; see method m2 (ratio) which uses "p70"'
        errs = ["method m1 (formula_mc): input p61: id p61 unknown or discarded"]
        out, _ = G._explain_discarded(errs, [M1], pts, {"p61"})
        self.assertIn("reason given: \"superseded by a2; see method m2 (ratio) which uses 'p70'\"", out[0])
        a5 = {"id": "a5", "rationale": "from p70"}
        self.assertEqual(G._repair_scope(out, [a5]), ({"m1"}, set()))

    def test_series_failure_gets_the_discarded_points_appended(self):
        # series 类遇到丢弃的点只跳过、不报 unknown or discarded（v2.16c 审查）：原报错保留，后面补上
        ser = {"id": "m2", "method": "series_auto", "params": {"target_history": ["p61", "p70"]}}
        errs = ["method m2 (series_auto): series_auto needs at least one month after 2025-06 that also has its value a year "
                "earlier (no year-on-year pair)",
                "method m2 (series_auto): magnitude check: the combined estimate ... is more than 2x below ..."]
        out, rest = G._explain_discarded(errs, [ser], _pts(), set())
        self.assertTrue(out[0].startswith(errs[0] + " It also uses discarded data points: p61 (discarded by an earlier round"))
        self.assertEqual(out[1], errs[1])   # 闸门的报错不动
        self.assertEqual(rest, {"p61"})
        self.assertEqual(G._explain_discarded(errs[:1], [{**ser, "params": {"target_history": ["p70"]}}], _pts(), set()),
                         (errs[:1], set()))   # 没用到丢弃点：原样

    def test_unknown_id_and_kept_point_are_left_alone(self):
        only_kept = {**M1, "params": {"formula": "x * p70", "inputs": {"x": {"id": "p999", "role": "?"},
                                                                       "p70": {"id": "p70", "role": "x"}}}}
        errs = ["method m1 (formula_mc): input x: id p999 unknown or discarded"]
        self.assertEqual(G._explain_discarded(errs, [only_kept], _pts(), set()), (errs, set()))
        pts = _pts()
        pts["p61"]["keep"] = pts["p63"]["keep"] = True
        errs = ["method m1 (formula_mc): input p61: id p61 unknown or discarded"]
        self.assertEqual(G._explain_discarded(errs, [M1], pts, set()), (errs, set()))
        # 不认识的 id 报错照旧，但方法另外用到的丢弃点要补上
        out, rest = G._explain_discarded(["method m1 (formula_mc): input x: id p999 unknown or discarded"], [M1], _pts(), set())
        self.assertTrue(out[0].startswith("method m1 (formula_mc): input x: id p999 unknown or discarded It also uses"))
        self.assertEqual(rest, {"p61", "p63"})

    def test_partial_period_wording(self):
        errs = ["method m4 (partial_period): partial_period: base p63 is unknown or discarded"]
        out, rest = G._explain_discarded(errs, [], _pts(), set())
        self.assertEqual(rest, {"p63"})
        self.assertIn("p63 (discarded by an earlier round", out[0])


class TestRestore(unittest.TestCase):
    def test_only_named_points_with_keep_true(self):
        pts = _pts()
        pts["p80"] = {"id": "p80", "keep": False, "judge_reason": "off topic"}
        decisions = [{"id": "p61", "keep": False, "reason": "retained only via the 12-month route"},
                     {"id": "p80", "keep": False, "reason": "off topic"}]
        reply = {"decisions": [{"id": "p61", "keep": True, "reason": "it is the July level m1 needs"},
                               {"id": "p63", "keep": False, "reason": "still out"},
                               {"id": "p80", "keep": True, "reason": "not named, ignored"}]}
        got = G._restore_points(reply, {"p61", "p63"}, pts, decisions, 2)
        self.assertEqual(got, [{"id": "p61", "reason": "it is the July level m1 needs",
                                "discard_reason": "retained only via the 12-month route"}])
        self.assertTrue(pts["p61"]["keep"])
        self.assertEqual(pts["p61"]["restored_in_repair"]["attempt"], 2)
        self.assertFalse(pts["p63"]["keep"])
        self.assertFalse(pts["p80"]["keep"])
        self.assertEqual(decisions[0]["keep"], True)
        self.assertEqual(decisions[0]["discard_reason"], "retained only via the 12-month route")
        G._undo_restores(got, pts, decisions)
        self.assertFalse(pts["p61"]["keep"])
        self.assertEqual(pts["p61"]["judge_reason"], "retained only via the 12-month route")
        self.assertNotIn("restored_in_repair", pts["p61"])
        self.assertEqual(decisions[0], {"id": "p61", "keep": False, "reason": "retained only via the 12-month route"})


MONTHS = ((2023, 6, 30, "June", 1000), (2024, 6, 30, "June", 1100), (2025, 6, 30, "June", 1210),
          (2025, 5, 31, "May", 1000), (2026, 5, 31, "May", 1000), (2022, 6, 30, "June", 900))
M_A = {"id": "m1", "method": "series_auto", "params": {"target_history": ["p1", "p2", "p3", "p4", "p5"]}}
M_B = {"id": "m3", "method": "formula_mc", "unit": "widget",
       "params": {"formula": "c * c / d", "inputs": {"c": {"id": "p3", "role": "June 2025 widgets"},
                                                     "d": {"id": "p2", "role": "June 2024 widgets"}}}}
DISCARD = [{"id": "p3", "keep": False, "reason": "Duplicate of another June 2025 row"},
           {"id": "p6", "keep": False, "reason": "2022 is too old"}]


def run_judge(repair_decisions):
    """裁判层面：第 1 轮丢了 p3（m1、m3 都用）和 p6（哪条方法都不用，不会被点名）；修正回复的 decisions = repair_decisions，
    方法原样交回。"""
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
            users.setdefault(role, []).append(user)
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
            if role == "judge:r1":
                return {"decisions": DISCARD, "extra_directions": [], "methods": [M_A, M_B]}, None
            if role == "judge:r1:repair":
                return {"decisions": repair_decisions, "methods": [M_A, M_B]}, None
            if role == MG.ROLE:
                return None, "reply is not valid JSON"   # 闸门不起作用，只看 S84
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
class TestS84Judge(unittest.TestCase):
    def test_restore_named_point_and_method_computes(self):
        st, roles, users = run_judge([{"id": "p3", "keep": True, "reason": "m3 needs the June 2025 level"},
                                      {"id": "p6", "keep": True, "reason": "not named"}])
        rep = users["judge:r1:repair"][0]
        self.assertIn("it uses discarded data points", rep)
        self.assertIn('reason given: "Duplicate of another June 2025 row"', rep)
        self.assertNotIn("unknown or discarded", rep)
        jr = st["judge_rounds"][-1]
        self.assertEqual([r["id"] for r in jr["repairs"][0]["restored_points"]], ["p3"])
        pts = {p["id"]: p for p in st["points"]}
        self.assertTrue(pts["p3"]["keep"])
        self.assertEqual(pts["p3"]["restored_in_repair"]["discard_reason"], "Duplicate of another June 2025 row")
        self.assertFalse(pts["p6"]["keep"])   # 没被点名：照旧不采用
        self.assertEqual(roles.count("judge:r1:repair"), 1)
        est = {m["id"]: m.get("estimate") for m in st["compute"]["methods"]}
        self.assertEqual(len([e for e in est.values() if e]), 2)

    def test_no_restore_keeps_the_point_discarded(self):
        st, roles, users = run_judge([])
        jr = st["judge_rounds"][-1]
        self.assertNotIn("restored_points", jr["repairs"][0])
        self.assertFalse({p["id"]: p for p in st["points"]}["p3"]["keep"])
        # 同一句报错不重复发：下一次修正（如果有）里的文字和第一次相同，走原来的 MAX_REPAIRS 上限
        self.assertTrue(all("it uses discarded data points" in u for u in users["judge:r1:repair"]))


if __name__ == "__main__":
    unittest.main()

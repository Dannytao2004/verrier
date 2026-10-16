"""v2.6b（FIX_PLAN S5）：裁判轮次协议。
D1（N11）：第 2 轮（和修正轮）的完整表格只列仍保留的点和新点，之前轮次丢掉的点另起一段，每个一行（id | name | value | 第几轮丢弃）；
判定规则不变（没列出的点沿用原状态，keep:true 恢复）。量纲规则报错点名每个输入（B5 的一部分）。
JUDGE_USER 回复示例里 formula_mc 的 inputs 带 role（N15）。图的离线测试需要 langgraph（.venv），没装时跳过。"""
import json
import re
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import assumptions as AS
from triangulate.agent import compute as C
from triangulate.agent.prompts import JUDGE_USER

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

BLOCK = "Points discarded in earlier judge rounds (left out of the table above):\nid | name | value | discarded in round\n"
RESTORE = 'These points stay discarded. To restore one, list it in decisions with "keep": true and a short reason.'
TASK2 = "Every point in the data-point table above that you do not list is kept."
EXTRA = [{"id": "b1", "category": "base_rates", "hypothesis": "h3", "data_to_find": "f3", "search_hints": ["q"]}]


def continuous_run(r1_decisions, r2_decisions):
    """假模型跑一遍连续值目标的图（同 probes/compare_continuous_prompts.py 的做法）：d1、b1 每页各 3 个点
    （d1 -> p1..p3，b1 -> p4..p6）；第 2 轮第一次回复的方法跑不出来，交回修正轮。返回 (最终 state, [(role, user prompt)])。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    log = []

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            log.append((role, user))
            if role == "plan":
                return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                   "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                        "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                    "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                                   for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
            bad = [{"id": "m1", "method": "linear_fit", "params": {"target_history": ["p1"]}}]
            good = [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2"], "k": 1}}]
            if role == "judge:r1":
                return {"decisions": r1_decisions, "extra_directions": EXTRA, "methods": bad}, None
            if role == "judge:r2":
                return {"decisions": r2_decisions, "extra_directions": [], "methods": bad}, None
            if role == "judge:r2:repair":
                return {"decisions": [], "extra_directions": [], "methods": good}, None
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
                "text": "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."}

    ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
    with mock.patch.object(P, "fetch_page", fake_fetch), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "t1"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        st = dict(g.get_state(cfg).values)
    return st, log


def table_ids(user: str) -> list:
    """prompt 里完整表格各行的 id（表头之后、第一个空行之前）。"""
    head = "id | dir | name | value | unit | period | published | source | via | quote\n"
    body = user[user.index(head) + len(head):].split("\n\n")[0]
    return [r.split(" | ")[0] for r in body.split("\n")]


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestDiscardedPointsBlock(unittest.TestCase):
    def test_round_two_lists_earlier_discards_compactly_and_codes_rule_is_unchanged(self):
        r1 = [{"id": "p2", "keep": False, "reason": "dup"}, {"id": "p3", "keep": False, "reason": "dup"}]
        r2 = [{"id": "p2", "keep": True, "reason": "needed after all"}, {"id": "p4", "keep": False, "reason": "dup"}]
        st, log = continuous_run(r1, r2)
        users = dict(log)
        self.assertEqual([r for r, _ in log if r.startswith("judge")], ["judge:r1", "judge:r2", "judge:r2:repair"])
        # 第 1 轮：没有之前的轮次，整段不出现，表格照旧列全部点
        self.assertNotIn("Points discarded in earlier", users["judge:r1"])
        self.assertEqual(table_ids(users["judge:r1"]), ["p1", "p2", "p3"])
        # 第 2 轮：表格只有仍保留的 p1 和新点 p4..p6；第 1 轮丢的 p2、p3 各一行，不带 quote
        u2 = users["judge:r2"]
        self.assertEqual(table_ids(u2), ["p1", "p4", "p5", "p6"])
        self.assertIn("\n\n" + BLOCK + "p2 | widgets June 2024 | 1,100 | 1\np3 | widgets June 2025 | 1,210 | 1\n" + RESTORE +
                      "\n\nCode method library", u2)
        self.assertNotIn("June 2024: 1,100 widgets", u2.split(BLOCK)[1].split("\n\n")[0])   # 紧凑行不带 quote
        for u in (users["judge:r1"], u2):
            self.assertIn(TASK2, u)
        # 修正轮：同一张表 + 同一段（修正 prompt 以第 2 轮的 prompt 开头）
        self.assertTrue(users["judge:r2:repair"].startswith(u2))
        # 判定规则没变：p2 用 keep:true 恢复；p3 没列出，沿用丢弃；p4 这一轮丢；其余保留
        keep = {p["id"]: p["keep"] for p in st["points"]}
        self.assertEqual(keep, {"p1": True, "p2": True, "p3": False, "p4": False, "p5": True, "p6": True})
        self.assertEqual({p["judged_round"] for p in st["points"]}, {2})
        self.assertEqual(st["compute"]["methods"][0]["used_ids"], ["p1", "p2"])

    def test_no_block_when_nothing_was_discarded_before(self):
        st, log = continuous_run([], [{"id": "p2", "keep": False, "reason": "dup"}])
        users = dict(log)
        for role in ("judge:r1", "judge:r2", "judge:r2:repair"):
            self.assertNotIn("Points discarded in earlier", users[role])
        self.assertEqual(table_ids(users["judge:r2"]), ["p1", "p2", "p3", "p4", "p5", "p6"])
        self.assertFalse(next(p for p in st["points"] if p["id"] == "p2")["keep"])

    def test_discrete_repair_shows_the_block_and_still_names_every_discarded_point(self):
        from tests.test_discrete import HIKE, HOLD, TestJudgeDefinedOutcomesGraph, discrete_graph_run, judge_reply
        one = [{"id": "m1", "method": "outcome_probs", "params": {"probs": {HOLD: {"id": "p1", "role": "r"}}, "remainder": HIKE}}]
        r1 = judge_reply(basis={"ids": ["p1"], "note": "p1"}, decisions=[{"id": "p2", "keep": False, "reason": "dup"}],
                         extra_directions=TestJudgeDefinedOutcomesGraph.EXTRA)
        bad = [{"id": "m1", "method": "outcome_probs", "params": {"probs": {"x": {"id": "p99", "role": "r"}}}}]
        r2 = judge_reply(outcomes=None, basis=None, methods=bad, decisions=[{"id": "p4", "keep": False, "reason": "dup"}])
        st, seen = discrete_graph_run(judge=[r1, r2, judge_reply(outcomes=None, basis=None, methods=one)])
        self.assertEqual(seen["judge_roles"], ["judge:r1", "judge:r2", "judge:r2:repair"])
        u2, rep = seen["judge_users"][1], seen["judge_users"][2]
        self.assertEqual(table_ids(u2), ["p1", "p3", "p4"])
        self.assertIn(BLOCK + "p2 | Market-implied probability of a hike to 4.00-4.25 at the 2026-10-28 meeting | 43.6 | 1\n"
                      + RESTORE, u2)
        self.assertTrue(rep.startswith(u2))
        # 修正轮的 REPAIR_DISCARDED 照旧列出全部已丢弃的点（之前轮次的 p2 和这一轮的 p4），修正回复的 decisions 不采用
        self.assertTrue(rep.endswith("decisions in this reply do not change that: do not use them in \"outcomes_basis\" or as "
                                     "method inputs: p2, p4"), rep[-300:])
        self.assertEqual({p["id"]: p["keep"] for p in st["points"]}, {"p1": True, "p2": False, "p3": True, "p4": False})
        self.assertEqual(st["compute"]["result"]["most_likely"], HOLD)


class TestDimensionRuleNamesInputs(unittest.TestCase):
    TARGET = {"what": "Live births in country X", "unit": "live births", "period_start": "2026-07-01",
              "period_end": "2026-07-31"}
    LONG = "Share of annual live births that occur in July, national vital statistics, 2015-2024 average"

    def test_error_lists_id_unit_and_name_of_each_point_and_assumption_input(self):
        pts = {"p1": {"id": "p1", "value": 8.6, "unit": "% of annual live births", "keep": True, "name": self.LONG,
                      "period_start": "2024-01-01", "period_end": "2024-12-31"},
               "p2": {"id": "p2", "value": 1.02, "unit": "", "keep": True, "name": "Births trend factor",
                      "period_start": "2025-01-01", "period_end": "2025-12-31"}}
        av = AS.validate([{"id": "a1", "name": "July 2026 versus July 2025 change factor", "value": 0.98, "low": 0.95,
                           "high": 1.01, "unit": "ratio", "rationale": "r", "applies_when": "w", "falsified_by": "f",
                           "route": "m1"}], self.TARGET)
        self.assertEqual([a["id"] for a in av["kept"]], ["a1"])
        m = {"method": "formula_mc", "params": {"formula": "s * f * c / k_days_target",
                                               "inputs": {"s": {"id": "p1"}, "f": {"id": "p2"}, "c": {"id": "a1"},
                                                          "k_days_target": {"id": "k_days_target"}}}}
        err = C.run([m], pts, self.TARGET, assumptions=av)["methods"][0]["error"]
        self.assertEqual(err, "formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of "
                              'ratios cannot produce the target. Inputs: s = p1 (unit "% of annual live births", name "'
                              + self.LONG[:60] + '"); f = p2 (unit "", name "Births trend factor"); '
                              'c = a1 (unit "ratio", name "July 2026 versus July 2025 change factor"). '
                              "Code reads each of these units as a share, ratio, % or empty unit")

    def test_rule_itself_unchanged(self):
        pts = {"p1": {"id": "p1", "value": 600000.0, "unit": "live births", "keep": True, "name": "Annual live births 2025",
                      "period_start": "2025-01-01", "period_end": "2025-12-31"},
               "p2": {"id": "p2", "value": 8.6, "unit": "%", "keep": True, "name": "July share",
                      "period_start": "2024-01-01", "period_end": "2024-12-31"}}
        m = {"method": "formula_mc", "params": {"formula": "b * s", "inputs": {"b": {"id": "p1"}, "s": {"id": "p2"}}}}
        out = C.run([m], pts, self.TARGET)["methods"][0]
        self.assertNotIn("error", out)
        self.assertGreater(out["estimate"], 0)


class TestReplyExampleRoles(unittest.TestCase):
    def test_formula_mc_example_gives_every_input_a_role(self):
        from triangulate.agent import graph as G
        u = JUDGE_USER.format(question="q", as_of="2026-01-01", target="{}", directions="", table="", methods_spec="",
                              extra_rule="")
        ex = re.search(r'\{"id": "m2", "method": "formula_mc".*?"rationale": "\.\.\."\}', u).group()
        m = json.loads(ex)
        self.assertEqual(m["params"]["inputs"], {"a": {"id": "p3", "role": "..."}, "b": {"id": "a1", "role": "..."}})
        # 和规则一致：输入核对按 role 拦方法（audit_methods 的 "no role stated"），示例的每个输入都不会被这条拦下
        rows = G.audit_rows(m, {"method": "formula_mc"}, {"p3": {"id": "p3", "name": "n", "value": 1.0}},
                            {"a1": {"id": "a1", "name": "n", "value": 1.0, "unit": "ratio"}})
        self.assertEqual([(r[0], r[2]) for r in rows], [("a", "..."), ("b", "...")])


if __name__ == "__main__":
    unittest.main()

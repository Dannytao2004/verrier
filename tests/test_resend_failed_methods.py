"""v2.11e（计划 D2）：两条以上路线吻合时，代码否掉的方法也至少交回裁判一次。
假模型：d1 一页 3 个点（p1..p3，1,000 / 1,100 / 1,210 widgets）；m1、m2 吻合，m3 是 formula_mc。
裁判第 1 轮不加方向，check 在第 1 轮就跑；修正轮的角色是 judge:r1:repair。图的离线测试需要 langgraph（.venv），没装时跳过。"""
import unittest
from datetime import date
from unittest import mock

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

M1 = {"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}}
M2 = {"id": "m2", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 3}}
FAR = {"id": "m2", "method": "formula_mc",   # 只用来造「打架」的 m2（4 x 1,210，和 m1 差 3 倍以上）
       "params": {"formula": "c + c + c + c", "inputs": {"c": {"id": "p3", "role": "June 2025 widgets"}}}}


def m3(formula):
    return {"id": "m3", "method": "formula_mc",
            "params": {"formula": formula, "inputs": {"c": {"id": "p3", "role": "June 2025 widgets"},
                                                      "d": {"id": "p2", "role": "June 2024 widgets"}}}}


BAD = m3("c * 1.1")
BAD2 = m3("c * 1.2")          # 修了 1.1，又冒出另一个常数
GOOD = m3("c * c / d")


def run(replies, audit=None, r1_methods=None):
    """replies：judge:r1 之后各次修正轮依次给的方法列表。audit：{方法 id: 原因}，输入核对对这些方法报 mismatch。
    返回 (最终 state, [调用角色], {角色: 最后一次 user prompt})。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    roles, users, todo = [], {}, list(replies)

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            roles.append(role)
            users[role] = user
            if role == "plan":
                return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                   "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                        "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                    "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                                   for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
            if role == "judge:r1":
                return {"decisions": [], "extra_directions": [], "methods": r1_methods or [M1, M2, BAD]}, None
            if role == "judge:r1:repair":
                return {"decisions": [], "extra_directions": [], "methods": todo.pop(0)}, None
            if role == "audit":
                return {"methods": [{"id": k, "inputs": [{"name": "c", "verdict": "mismatch", "reason": r}]}
                                    for k, r in (audit or {}).items()]}, None
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
    return st, [r for r in roles if r.startswith("judge")], users


def err(formula_const):
    return (f"method m3 (formula_mc): formula: numeric constant {formula_const} not allowed (only 1 and exponents); "
            f"make it a named input")


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestResendFailedMethods(unittest.TestCase):
    def test_fixed(self):
        st, judge, users = run([[M1, M2, GOOD]])
        self.assertEqual(judge, ["judge:r1", "judge:r1:repair"])
        jr = st["judge_rounds"][-1]
        self.assertEqual(jr["repair"]["resent_failed_methods"], [err(1.1)])
        self.assertEqual(jr["repair"]["errors"], [err(1.1)])
        self.assertEqual(jr["repair"]["errors_after"], [])
        self.assertIn("numeric constant 1.1 not allowed", users["judge:r1:repair"])
        self.assertEqual([m["id"] for m in st["compute"]["methods"] if m.get("estimate")], ["m1", "m2", "m3"])

    def test_still_failing_is_sent_once_and_the_error_stays(self):
        st, judge, _ = run([[M1, M2, BAD]])
        self.assertEqual(judge, ["judge:r1", "judge:r1:repair"])   # 同一条文字已经发过：不再修第二轮
        jr = st["judge_rounds"][-1]
        self.assertEqual(len(jr["repairs"]), 1)
        self.assertEqual(jr["repair"]["errors_after"], [])
        m = {x["id"]: x for x in st["compute"]["methods"]}
        self.assertIn("numeric constant 1.1", m["m3"]["error"])
        self.assertIsNotNone(m["m1"]["estimate"])
        self.assertIsNotNone(m["m2"]["estimate"])

    def test_newly_surfaced_error_is_sent_too(self):
        st, judge, users = run([[M1, M2, BAD2], [M1, M2, GOOD]])
        self.assertEqual(judge, ["judge:r1", "judge:r1:repair", "judge:r1:repair"])
        reps = st["judge_rounds"][-1]["repairs"]
        self.assertEqual([r["resent_failed_methods"] for r in reps], [[err(1.1)], [err(1.2)]])
        self.assertIn("numeric constant 1.2 not allowed", users["judge:r1:repair"])
        self.assertEqual([m["id"] for m in st["compute"]["methods"] if m.get("estimate")], ["m1", "m2", "m3"])

    def test_error_already_sent_for_another_reason_is_not_resent(self):
        # 第 1 次：m1、m2 打架（今天的规则就交回），m3 的错误跟着发出去；修完 m1、m2 吻合、m3 原样：不再交回
        st, judge, _ = run([[M1, M2, BAD]], r1_methods=[M1, FAR, BAD])
        jr = st["judge_rounds"][-1]
        self.assertEqual(judge, ["judge:r1", "judge:r1:repair"])
        self.assertNotIn("resent_failed_methods", jr["repair"])
        self.assertTrue(any(e.startswith("methods disagree") for e in jr["repair"]["errors"]))
        self.assertIn(err(1.1), jr["repair"]["errors"])

    def test_audit_only_rejection_does_not_trigger(self):
        st, judge, _ = run([], audit={"m3": "not the quantity the formula needs"}, r1_methods=[M1, M2, GOOD])
        self.assertEqual(judge, ["judge:r1"])
        jr = st["judge_rounds"][-1]
        self.assertNotIn("repair", jr)
        self.assertEqual(list(jr["audit_failed"].values()), ["input audit: c: not the quantity the formula needs"])


if __name__ == "__main__":
    unittest.main()

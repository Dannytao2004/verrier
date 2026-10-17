"""U1（v2.7b）：规划钉死 target.unit_canonical（UNITS_PLAN.md「钉死单位」）。
连续目标的 unit_canonical 必须是 qty 能解析的一个单位；缺失、解析不了、几个候选时带着错误重问一次规划，
仍不行就不钉、记 plan note「unit not pinned: …; unit checks off」，运行照常继续；离散目标不要。
假模型、真的 LangGraph 图；不联网、不调模型、不读 results/。"""
import json
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import qty as Q
from triangulate.agent.prompts import CHECKLIST, PLAN_UNIT_RETRY, PLAN_USER

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

# 披萨题（芝加哥人每天吃多少披萨）规划的 target，按字面值重建：unit 是给人看的描述，里面有两个候选
PIZZA = {"what": "Total pizza consumed per day by people in Chicago",
         "unit": "pizza mass per day (kg or lbs), with secondary slice/serving count per day",
         "period_start": "2026-01-01", "period_end": "2026-12-31", "publisher": "None official", "cadence": "n/a",
         "caveats": "residents versus pizza eaten within city limits", "outcome_type": "continuous"}
UNSET = object()


def plan_reply(unit_canonical=UNSET, hyp="h1", **target):
    t = dict(PIZZA, **target)
    if unit_canonical is not UNSET:
        t["unit_canonical"] = unit_canonical
    return {"target": t, "market_keywords": [],
            "directions": [{"category": "related_series", "hypothesis": hyp, "data_to_find": "f"}]}


class PlanLLM:
    """plan 角色按顺序回 replies（None = 无效回复）；记下每次的 user prompt、tries、max_tokens。"""
    model = "fake"

    def __init__(self, *replies):
        self.replies, self.calls = list(replies), []

    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        assert role == "plan", role
        self.calls.append({"user": user, "tries": tries, "max_tokens": max_tokens})
        r = self.replies[len(self.calls) - 1]
        return (r, None) if r is not None else (None, "reply is not valid JSON")


def _ctx(llm, allow_discrete=None):
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How much pizza do people in Chicago eat per day?", "2026-10-17", \
        date(2026, 10, 17)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history, ctx.llm = P.Budget(), [], False, llm
    if allow_discrete is not None:
        ctx.allow_discrete = allow_discrete
    return ctx


def run_plan(llm, allow_discrete=None) -> dict:
    """只跑 plan 节点：图停在 approve（interrupt），返回 state。"""
    from triangulate.agent import graph as G
    ctx = _ctx(llm, allow_discrete)
    g = G.build(ctx)
    cfg = {"configurable": {"thread_id": "t1"}}
    g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
    return g.get_state(cfg).values


def unit_notes(st) -> list:
    return [n for n in st.get("plan_notes") or [] if "unit" in n]


class TestPlanPrompt(unittest.TestCase):
    def test_prompt_asks_for_unit_canonical_and_its_examples_parse(self):
        user = PLAN_USER.format(question="q", as_of="2026-10-17", checklist=CHECKLIST)
        self.assertIn('"unit": "...", "unit_canonical": "..."', user)
        for ex in ("visitor", "t/day", "USD/year", "birth/(1000 person)", "percent"):
            self.assertIn(f"'{ex}'", user)
            self.assertEqual(Q.parse_unit(ex)[1], "", ex)
        self.assertIn("'visitor/month'", user)   # 反例：一段期间的总量不写成速率
        self.assertIn("For a discrete target, leave unit_canonical empty.", user)   # 和代码一致：离散目标不检查、不存


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestPinUnit(unittest.TestCase):
    def test_valid_unit_kept(self):
        llm = PlanLLM(plan_reply(" t/day "))
        st = run_plan(llm)
        t = st["plan"]["target"]
        self.assertEqual(len(llm.calls), 1)
        self.assertEqual(t["unit_canonical"], "t/day")
        self.assertEqual(t["unit"], PIZZA["unit"])   # 给人看的描述照旧（已公布检测仍用它）
        self.assertEqual(unit_notes(st), [])
        self.assertFalse(st.get("aborted"))
        # 钉死的单位直接交给 qty（U2 用）：披萨 m2 的公式单位 kg/year、m1 的 g * percent / day 都能换到 t/day；
        # 没有时间口径的 kg 不能换
        self.assertAlmostEqual(Q.convert_factor("kg/year", t["unit_canonical"])[0] * 365250, 1.0, places=12)   # 相对比较
        self.assertAlmostEqual(Q.convert_factor("gram * percent / day", t["unit_canonical"])[0] * 1e8, 1.0, places=12)
        self.assertIn("cannot be converted", Q.convert_factor("kg", t["unit_canonical"])[1])

    def test_invalid_then_valid_on_retry(self):
        llm = PlanLLM(plan_reply("kg or lbs", hyp="first"), plan_reply("t/day", hyp="second"))
        st = run_plan(llm)
        err = "target.unit_canonical: unit 'kg or lbs': 'or' gives alternatives; pin exactly one unit"
        self.assertEqual(len(llm.calls), 2)
        self.assertEqual(llm.calls[1]["user"], llm.calls[0]["user"] + PLAN_UNIT_RETRY.format(error=err))
        self.assertEqual((llm.calls[1]["tries"], llm.calls[1]["max_tokens"]), (1, llm.calls[0]["max_tokens"]))   # 只重问一次
        self.assertEqual(st["plan"]["target"]["unit_canonical"], "t/day")
        self.assertEqual([c["hypothesis"] for c in st["plan"]["candidates"]], ["second"])   # 用重问得到的那份规划
        self.assertEqual(unit_notes(st), [])

    def test_invalid_twice_gives_note_and_no_unit(self):
        """重问的回复仍钉不住单位：沿用第一份规划（方向也是它的），note 记第一份的单位错误。"""
        llm = PlanLLM(plan_reply(["kg", "lb"], hyp="first"), plan_reply("kg, lb", hyp="second"))
        st = run_plan(llm)
        self.assertEqual(len(llm.calls), 2)
        self.assertIn('rejected: target.unit_canonical must be one unit written as a string, not ["kg", "lb"]. Reply again',
                      llm.calls[1]["user"])
        self.assertNotIn("unit_canonical", st["plan"]["target"])
        self.assertEqual(unit_notes(st), ['unit not pinned: target.unit_canonical must be one unit written as a string, '
                                          'not ["kg", "lb"]; unit checks off'])
        self.assertEqual(st["directions"][0]["hypothesis"], "first")
        self.assertFalse(st.get("aborted"))

    def test_retry_reply_replaces_plan_only_if_usable_and_pinned(self):
        """重问的回复是合法 JSON、单位也钉住了，但不是一份能用的规划（没有 dict 方向），或者改成了离散目标：
        沿用第一份规划和它的单位错误。"""
        partial = {"target": dict(PIZZA, unit_canonical="t/day")}   # 审查的例子：只回了 target
        for name, second in (("no directions", partial), ("empty directions", dict(partial, directions=[])),
                             ("directions a dict", dict(partial, directions={"d1": {"category": "related_series"}})),
                             ("directions a number", dict(partial, directions=3)),
                             ("directions not dicts", dict(partial, directions=["d1"])),
                             ("discrete target", plan_reply("t/day", hyp="second", outcome_type="discrete", outcome_kind="yes/no"))):
            with self.subTest(name):
                llm = PlanLLM(plan_reply(hyp="first"), second)
                st = run_plan(llm)
                t = st["plan"]["target"]
                self.assertEqual(len(llm.calls), 2)
                self.assertEqual([c["hypothesis"] for c in st["plan"]["candidates"]], ["first"])
                self.assertEqual([d["hypothesis"] for d in st["directions"]], ["first"])
                self.assertEqual((t["outcome_type"], "unit_canonical" in t), ("continuous", False))
                self.assertEqual(unit_notes(st), ["unit not pinned: target.unit_canonical is missing; unit checks off"])
                self.assertFalse(st.get("aborted"))

    def test_missing_unit_and_invalid_retry_reply_keeps_first_plan(self):
        llm = PlanLLM(plan_reply(hyp="first"), None)
        st = run_plan(llm)
        self.assertEqual(len(llm.calls), 2)
        self.assertTrue(llm.calls[1]["user"].endswith(
            "\n\nA previous reply to this request was rejected: target.unit_canonical is missing. Reply again with the complete "
            "JSON object, with target.unit_canonical written as exactly one unit as described in Step 1."))
        self.assertEqual(unit_notes(st), ["unit not pinned: target.unit_canonical is missing; unit checks off"])
        self.assertNotIn("unit_canonical", st["plan"]["target"])
        self.assertEqual(st["directions"][0]["hypothesis"], "first")
        self.assertFalse(st.get("aborted"))

    def test_discrete_target_skips_unit(self):
        for uc in (UNSET, "kg or lbs", "percent"):
            with self.subTest(unit_canonical=uc):
                llm = PlanLLM(plan_reply(uc, outcome_type="discrete", outcome_kind="yes/no"))
                st = run_plan(llm)
                t = st["plan"]["target"]
                self.assertEqual(len(llm.calls), 1)
                self.assertEqual(t["outcome_type"], "discrete")
                self.assertNotIn("unit_canonical", t)
                self.assertEqual(unit_notes(st), [])

    def test_discrete_reply_treated_as_continuous_needs_unit(self):
        """评分题没标 discrete（run.prepare_run 的 allow_discrete=False）：按连续题处理，也要钉单位；
        PLAN_USER 让离散目标留空 unit_canonical，所以重问时讲清楚这道题要连续数。"""
        d = {"outcome_type": "discrete", "outcome_kind": "yes/no"}
        why = ('target.unit_canonical is missing; this question needs a continuous number, so outcome_type must be '
               '"continuous" and target.unit_canonical must be given')
        forced = ("plan chose a discrete target, but this scored question is not marked outcome_type 'discrete'; "
                  "treated as continuous")
        for name, second, unit, notes in (
                ("discrete again, with unit", plan_reply("t/day", hyp="second", **d), "t/day", [forced]),
                ("continuous, with unit", plan_reply("t/day", hyp="second"), "t/day", []),
                ("invalid reply", None, None, [forced, f"unit not pinned: {why}; unit checks off"])):
            with self.subTest(name):
                llm = PlanLLM(plan_reply(hyp="first", **d), second)
                st = run_plan(llm, allow_discrete=False)
                t = st["plan"]["target"]
                self.assertEqual(len(llm.calls), 2)
                self.assertEqual(llm.calls[1]["user"], llm.calls[0]["user"] + PLAN_UNIT_RETRY.format(error=why))
                self.assertEqual((t["outcome_type"], t.get("unit_canonical")), ("continuous", unit))
                self.assertEqual([n for n in st["plan_notes"] if "unit" in n or "discrete" in n], notes)
                self.assertEqual(st["directions"][0]["hypothesis"], "first" if second is None else "second")


def graph_run(llm) -> dict:
    """假模型跑完整的图（同 tests/test_web.py：FakeSearcher、fake_fetch、没有市场），审批后跑到终稿，返回 state。"""
    from langgraph.types import Command

    from tests.test_web import FakeSearcher, fake_fetch
    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = _ctx(llm)
    ctx.question, ctx.as_of_s, ctx.as_of = "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.searcher = FakeSearcher()
    with mock.patch.object(P, "fetch_page", fake_fetch), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "t1"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        return g.get_state(cfg).values


@unittest.skipUnless(HAVE_LG, "langgraph not installed")
class TestGraphWithPinnedUnit(unittest.TestCase):
    def test_fake_model_run_completes(self):
        """假模型跑完整的图（同 tests/test_web.py 的 FakeLLM，plan 多给 unit_canonical）：照常出数，单位进了 target。"""
        from tests.test_web import FakeLLM
        users = {}

        class LLM(FakeLLM):
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                out, err = super().ask(system, user, role=role, qid=qid, max_tokens=max_tokens, tries=tries)
                users[role] = user
                if role == "plan":
                    out["target"]["unit_canonical"] = "widget"
                return out, err

        llm = LLM()
        st = graph_run(llm)
        self.assertEqual(llm.roles.count("plan"), 1)
        self.assertEqual(st["plan"]["target"]["unit_canonical"], "widget")
        self.assertEqual(unit_notes(st), [])
        self.assertAlmostEqual(st["compute"]["result"]["central"], 1210)
        self.assertIn("1,210", st["final"]["text"])
        self.assertIn(json.dumps({"unit_canonical": "widget"})[1:-1], users["judge:r1"])   # 裁判看到的 target 里有它

    def test_partial_retry_reply_does_not_break_the_run(self):
        """第一份规划没有 unit_canonical，重问只回了 target（钉住了单位、没有方向）：沿用第一份，照常出 1,210。"""
        from tests.test_web import FakeLLM

        class LLM(FakeLLM):
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                out, err = super().ask(system, user, role=role, qid=qid, max_tokens=max_tokens, tries=tries)
                if role == "plan" and self.roles.count("plan") == 2:
                    return {"target": dict(out["target"], unit_canonical="widget")}, None
                return out, err

        llm = LLM()
        st = graph_run(llm)
        self.assertEqual(llm.roles.count("plan"), 2)
        self.assertEqual(len(st["directions"]), 3)
        self.assertNotIn("unit_canonical", st["plan"]["target"])
        self.assertEqual(unit_notes(st), ["unit not pinned: target.unit_canonical is missing; unit checks off"])
        self.assertAlmostEqual(st["compute"]["result"]["central"], 1210)
        self.assertIn("1,210", st["final"]["text"])


if __name__ == "__main__":
    unittest.main()

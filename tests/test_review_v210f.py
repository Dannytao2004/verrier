"""v2.10f：审查发现的几处小问题（低优先级）的回归测试：key 的字符集、命令行只收 DeepSeek 模型、服务端说明先 redact 再截断（含 GLM 形状的
key）、网页的裁判摘要先 redact 再截断、DeepSeek 自带 key 的搜索请求关思考、上限放不下最小运行时拒跑并清 key。不联网、不读 key 文件。"""
import unittest
from unittest import mock

from triangulate import config, llm
from triangulate import providers as PV

GLM_KEY = "0123456789abcdef0123456789abcdef.AbCdEfGhIjKlMnOp"


def no_key_file(*a, **k):
    raise AssertionError("must not read the key file")


class TestKeyCharset(unittest.TestCase):
    def test_real_key_shapes_are_accepted(self):
        for k in ("sk-ant-api03-AbC_d-ef0123456789-XYZ_AA", "sk-proj-Ab_cD-ef01234567890", "sk-0123456789abcdef0123456789abcdef",
                  GLM_KEY, "abc+def/ghi=jkl~mno.pqr"):
            self.assertEqual(PV.clean_key("  " + k + "\n"), k)

    def test_characters_that_change_when_serialized_are_refused(self):
        """兜底的 redact 在 json.dumps / HTML 转义之后的文字上找 key：带 " \\ & < > ' 的 key 转义以后就找不到了，入口直接拒。"""
        for bad in ('"', "\\", "&", "<", ">", "'", "!", "#", "%", "`", "é", " ", "\t"):
            with self.subTest(ch=bad):
                with self.assertRaises(PV.SpecError) as cm:
                    PV.clean_key("sk-0123456789" + bad + "abcdef")
                self.assertNotIn("0123456789", str(cm.exception))   # 消息里不带 key


class TestCommandLineOnlyDeepSeek(unittest.TestCase):
    def test_other_providers_models_are_refused_before_reading_the_key(self):
        """审查发现：TRIANGULATE_MODEL 设成有价格的别家模型时，以前会带着 DeepSeek 的 key 把别家的模型 id 发到 api.deepseek.com。"""
        from triangulate.agent import search as S
        with mock.patch("triangulate.llm.read_key", no_key_file), mock.patch("triangulate.agent.search.read_key", no_key_file):
            for m in ("claude-haiku-5-5", "gpt-6-luna", "kimi-k3", "glm-5.2", "kimi-k3@cn"):
                with self.subTest(model=m):
                    with self.assertRaises(config.UnsupportedModel) as cm:
                        llm.LLM(model=m)
                    self.assertIn("only use DeepSeek models", str(cm.exception))
                    with self.assertRaises(config.UnsupportedModel):
                        S.Searcher(log=lambda r: None, model=m)
            with self.assertRaises(config.UnknownModel):
                llm.LLM(model="no-such-model-x")
        with mock.patch("triangulate.llm.read_key", lambda: "k"), mock.patch("triangulate.agent.search.read_key", lambda: "k"):
            self.assertEqual(llm.LLM(model="deepseek-v4-pro").model, "deepseek-v4-pro")
            self.assertEqual(S.Searcher(log=lambda r: None, model="deepseek-flash").model, "deepseek-flash")
        self.assertTrue(issubclass(config.UnsupportedModel, config.UnknownModel))


class TestServerTextRedaction(unittest.TestCase):
    def test_redact_before_truncating(self):
        """服务端的说明：先换掉这次运行的 key，再换像 key 的片段（sk-...、GLM 形状），最后截断。"""
        msg = "x" * 185 + " key=" + GLM_KEY + " end"
        self.assertEqual(llm.scrub_server_text(msg, lambda t: t.replace(GLM_KEY, "***")), ("x" * 185 + " key=*** end")[:200])
        self.assertNotIn(GLM_KEY[:9], llm.scrub_server_text(msg, None))   # 不知道 key 也认得 GLM 的形状
        self.assertEqual(llm.scrub_server_text("bad " + GLM_KEY + " x"), "bad *** x")
        self.assertEqual(llm.scrub_server_text("Bad key sk-proj-****0000 here"), "Bad key sk-*** here")

    def test_glm_parse_error_is_not_cut_before_redaction(self):
        import json
        sp = PV.ModelSpec("glm", "glm-5.2", GLM_KEY)
        raw = json.dumps({"error": {"code": "1210", "message": "x" * 185 + " key=" + GLM_KEY}}).encode()
        self.assertEqual(PV.GLM.parse_error(raw)["server_error"], "x" * 185 + " key=" + GLM_KEY)   # 不在 adapter 里截断
        out = llm.server_error(PV.GLM, raw, sp.redact)
        self.assertEqual(out, {"server_error": ("x" * 185 + " key=***")[:200], "server_error_code": "1210"})
        self.assertNotIn(GLM_KEY[:9], json.dumps(out))
        out = llm.server_error(PV.CLAUDE, json.dumps({"error": {"type": "invalid_request_error",
                                                                "message": "y" * 190 + "sk-ant-api03-SECRET0123456789"}}).encode())
        self.assertNotIn("SECRET", out["server_error"])

    def test_web_judge_summary_is_redacted_before_it_is_cut(self):
        """网页的裁判摘要会截断文字：_on_update 先 redact 再做摘要（审查发现：以前先截断，截在 key 中间的半截认不出来）。"""
        from triangulate.web.runs import WebRun
        sp = PV.ModelSpec("glm", "glm-5.2", GLM_KEY)
        run = WebRun("r", {"id": "q", "question": "q", "as_of": "2026-06-20"}, "t", None, None, spec=sp)
        err = "transport: " + "x" * 280 + GLM_KEY
        run._on_update({"judge": {"judge_rounds": [{"round": 1, "error": err}, {"round": 2, "audit_error": "y" * 105 + GLM_KEY,
                                                                                 "methods": []}]}})
        for r in (1, 2):
            self.assertNotIn(GLM_KEY[:6], run.judge[r]["text"])
        self.assertTrue(run.judge[1]["text"].startswith("没有完成：transport: xxx"))


class TestDeepSeekSpecSearch(unittest.TestCase):
    def test_spec_search_body_same_as_cli(self):
        """用户 10-21：DeepSeek 搜索「保持原本一样即可」。自带 key 的运行也不加 thinking，请求体和命令行逐字相同（v2.10g 撤回 v2.10f 的改动）。"""
        ds = PV.DEEPSEEK
        self.assertFalse(hasattr(ds, "search_request_spec"))
        h0, b0 = ds.search_request("deepseek-flash", "k", "p", max_tokens=8192, max_uses=3)
        self.assertEqual(list(b0), ["model", "max_tokens", "tools", "messages"])
        sp = PV.ModelSpec("deepseek", "deepseek-flash", "sk-0123456789abcdef", thinking="high")
        self.assertIsNone(sp.effort("search"))   # 搜索不是 plan / judge / repair


class TestWebStatusAfterBudgetStop(unittest.TestCase):
    """WebRun._after_stream：原因只在 budget.aborted（state 里没有 aborted）也认得：没有估计 -> failed + error；有估计 -> done + stopped。"""

    def run_with(self, state):
        from types import SimpleNamespace as NS

        from tests import test_web as TW
        from triangulate.web.runs import WebRun
        sp = TW.byok_spec()
        run = WebRun("r", {"id": "q", "question": "q", "as_of": "2026-06-20"}, "t", None,
                     lambda h, approvals, keep_key=False: state, spec=sp)
        from triangulate.agent.pipeline import Budget
        run.h = {"g": NS(get_state=lambda cfg: NS(interrupts=())), "cfg": {}, "tag": "t", "ctx": NS(budget=Budget())}
        run._after_stream()
        return run

    def test_failed_with_the_budget_reason(self):
        why = "insufficient balance: DeepSeek HTTP 402 Insufficient Balance (search:d1 q); the run was stopped without retrying."
        run = self.run_with({"compute": {"result": {}}, "budget": {"aborted": why}})
        self.assertEqual((run.status, run.error, run.stopped), ("failed", why, None))

    def test_done_with_an_estimate_keeps_the_reason_as_stopped(self):
        run = self.run_with({"compute": {"result": {"central": 5.0}}, "budget": {"aborted": "usd cap 2.0 exceeded (2.0100)"}})
        self.assertEqual((run.status, run.error, run.stopped), ("done", None, "usd cap 2.0 exceeded (2.0100)"))
        self.assertEqual(run.status_view()["stopped"], "usd cap 2.0 exceeded (2.0100)")

    def test_no_reason_no_estimate_is_done_as_before(self):
        run = self.run_with({"compute": {"result": {}}, "budget": {"aborted": ""}})
        self.assertEqual((run.status, run.error), ("done", None))


class TestCapRefusal(unittest.TestCase):
    def test_refused_before_registering_and_the_key_is_dropped(self):
        from tests import test_web as TW
        from triangulate.web import catalog as C
        from triangulate.web.runs import CapTooLow, Registry

        def refuse(q, tag="", spec=None):
            raise AssertionError("must not start")
        reg = Registry(prepare=refuse, save=refuse)
        sp = TW.byok_spec(provider="claude", model="claude-opus-5-5", thinking="low", usd_cap=2.0)
        with self.assertRaises(CapTooLow) as cm:
            reg.start("How many widgets?", "2026-06-20", spec=sp)
        self.assertIsInstance(cm.exception, ValueError)   # app 把它变成 400
        floor = C.run_floor("claude-opus-5-5", "global", "low")["usd"]
        self.assertIn(f"${C.min_cap(floor):.2f}", str(cm.exception))
        self.assertIn("规划 + 一次搜索 + 抽取一页 + 裁判", str(cm.exception))
        self.assertFalse(sp.has_key)
        self.assertEqual(reg.runs, {})
        ok = TW.byok_spec(provider="claude", model="claude-opus-5-5", thinking="low", usd_cap=C.min_cap(floor))
        self.assertIsNone(__import__("triangulate.web.runs", fromlist=["x"]).check_spec_cap(ok))
        reg2 = Registry(prepare=refuse, save=refuse, check_cap=False)   # 关掉检查时照旧登记（测试用）
        run = reg2.start("q", "2026-06-20", spec=TW.byok_spec(provider="claude", model="claude-opus-5-5", thinking="low"))
        self.assertIn(run.id, reg2.runs)


if __name__ == "__main__":
    unittest.main()

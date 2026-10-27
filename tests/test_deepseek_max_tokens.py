"""v2.13d：DeepSeek 的裁判 / 修正 / 抽取默认上限放宽（providers.DEEPSEEK_MAX_TOKENS，用户 10-27：付得起）。
起因：留出测试 4 英国住宅交易关思考，第 1 轮裁判两次在 24000 处截断，整轮作废、没出数（BUGS S76）。"""
import unittest

from triangulate import config
from triangulate import providers as PV
from triangulate.llm import LLM


class TestRoleMaxTokens(unittest.TestCase):
    def test_deepseek_defaults_are_wider(self):
        for model in ("deepseek-flash", "deepseek-v4-pro"):
            for role, want in (("judge", 96000), ("repair", 96000), ("extract", 64000)):
                with self.subTest(model=model, role=role):
                    self.assertEqual(PV.role_max_tokens(model, role, config.MAX_TOKENS[role]), want)

    def test_other_roles_and_explicit_values_unchanged(self):
        for role in ("plan", "audit", "unit_check", "unit_arbiter", "final", "published", "search"):
            self.assertEqual(PV.role_max_tokens("deepseek-flash", role, config.MAX_TOKENS[role]), config.MAX_TOKENS[role])
        self.assertEqual(PV.role_max_tokens("deepseek-flash", "judge", 1000), 1000)   # 显式传的上限照原样

    def test_other_providers_unchanged(self):
        for model in ("claude-sonnet-5-5", "claude-opus-5-5"):
            self.assertEqual(PV.role_max_tokens(model, "judge", config.MAX_TOKENS["judge"]), config.MAX_TOKENS["judge"])
            effort = PV.effort_for(model, "off", "judge")   # Opus 关不掉思考：off 档也有思考余量（v2.13d 之前就这样）
            self.assertEqual(PV.tokens_for_model(model, "off", "judge", config.MAX_TOKENS["judge"])[1],
                             config.MAX_TOKENS["judge"] + (config.THINKING_EXTRA_TOKENS if effort else 0))

    def test_both_paths_send_the_same(self):
        """命令行（没有 ModelSpec）和网页（有 ModelSpec）发出的上限相同；开思考的再加思考余量。"""
        cli = LLM.__new__(LLM)
        cli.spec, cli.model = None, "deepseek-flash"
        self.assertEqual(cli.effort_and_tokens("judge:r1", config.MAX_TOKENS["judge"]), (None, 96000))
        self.assertEqual(cli.effort_and_tokens("extract:d2", config.MAX_TOKENS["extract"]), (None, 64000))
        self.assertEqual(PV.tokens_for_model("deepseek-flash", "off", "judge", config.MAX_TOKENS["judge"]), (None, 96000))
        self.assertEqual(PV.tokens_for_model("deepseek-flash", "high", "judge", config.MAX_TOKENS["judge"]),
                         ("high", 96000 + config.THINKING_EXTRA_TOKENS))

    def test_fits_the_request_time_limit(self):
        """存档里 DeepSeek 最慢 157 token/秒；最长的一次（裁判 + 思考余量）要在整次请求 1200 秒内写完。"""
        longest = max(PV.DEEPSEEK_MAX_TOKENS.values()) + config.THINKING_EXTRA_TOKENS
        self.assertLess(longest / 157, 1200)
        self.assertLessEqual(longest, PV.MODELS["deepseek-flash"]["max_output"])


if __name__ == "__main__":
    unittest.main()

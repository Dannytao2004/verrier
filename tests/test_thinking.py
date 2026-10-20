"""v2.9a：按角色打开 DeepSeek 思考模式。默认全关时请求体和 frozen-v2.8r 逐字相同；开了的角色带 reasoning_effort、max_tokens 加余量。"""
import json
import unittest
from unittest import mock

from triangulate import config, llm


class TestParse(unittest.TestCase):
    def test_parse_and_roles(self):
        self.assertEqual(config.parse_thinking(""), {})
        self.assertEqual(config.parse_thinking("judge=high, repair=HIGH,audit=low"),
                         {"judge": "high", "repair": "high", "audit": "low"})
        for bad in ("judge", "judge=medium", "=high", "judge=mid"):
            with self.assertRaises(ValueError):
                config.parse_thinking(bad)

    def test_thinking_role(self):
        self.assertEqual(config.thinking_role("plan"), "plan")
        self.assertEqual(config.thinking_role("judge:r2"), "judge")
        self.assertEqual(config.thinking_role("judge:r2:repair"), "repair")
        self.assertEqual(config.thinking_role("unit_arbiter:m1:2"), "unit_arbiter")
        self.assertEqual(config.thinking_role("published:early"), "published")


class TestPayload(unittest.TestCase):
    def _call(self, thinking, arm, max_tokens=1000):
        sent = {}

        def fake_post(req, **k):
            sent["body"] = json.loads(req.data)
            reply = {"choices": [{"message": {"content": "{\"ok\": 1}"}, "finish_reason": "stop"}],
                     "usage": {"prompt_tokens": 10, "completion_tokens": 30, "prompt_cache_miss_tokens": 10,
                               "completion_tokens_details": {"reasoning_tokens": 25}}}
            return 200, json.dumps(reply).encode()

        with mock.patch.object(llm, "THINKING", thinking), mock.patch.object(llm, "read_key", return_value="k"), \
                mock.patch.object(llm.LLM, "_post", staticmethod(fake_post)), mock.patch.object(llm.LLM, "_log") as log:
            out, _, err = llm.LLM().json_call([{"role": "user", "content": "json"}], arm=arm, qid="q", attempt=1,
                                              max_tokens=max_tokens)
        self.assertIsNone(err)
        self.assertEqual(out, {"ok": 1})
        return sent["body"], log.call_args[0][0]

    def test_default_is_unchanged(self):
        body, rec = self._call({}, "judge:r1")
        self.assertEqual(body["thinking"], {"type": "disabled"})
        self.assertNotIn("reasoning_effort", body)
        self.assertEqual(body["max_tokens"], 1000)
        self.assertNotIn("thinking", rec)
        self.assertNotIn("reasoning_tokens", rec)

    def test_enabled_role(self):
        body, rec = self._call({"repair": "high"}, "judge:r2:repair")
        self.assertEqual(body["thinking"], {"type": "enabled"})
        self.assertEqual(body["reasoning_effort"], "high")
        self.assertEqual(body["max_tokens"], 1000 + config.THINKING_EXTRA_TOKENS)
        self.assertEqual(rec["thinking"], "high")
        self.assertEqual(rec["reasoning_tokens"], 25)

    def test_other_roles_stay_off(self):
        body, _ = self._call({"repair": "high"}, "judge:r2")
        self.assertEqual(body["thinking"], {"type": "disabled"})
        body, _ = self._call({"repair": "high"}, "extract:d1")
        self.assertEqual(body["thinking"], {"type": "disabled"})


if __name__ == "__main__":
    unittest.main()

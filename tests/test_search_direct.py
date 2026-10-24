"""arm (3) 联网直接答（triangulate/search_direct.py）的离线测试：假客户端，不联网、不读 key。"""
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

from triangulate import forecast, search_direct as SD
from triangulate.arms import _messages
from triangulate.llm import TransportError
from triangulate.prompts import NAIVE_SYSTEM

Q = next(q for q in forecast.QUESTIONS if q["id"] == "fc_jnto_2026_09")
USAGE = {"input_tokens": 1000, "cache_read_input_tokens": 2000, "cache_creation_input_tokens": 0, "output_tokens": 300,
         "server_tool_use": {"web_search_requests": 2}}


def resp(final, stop="end_turn", early_text="I will search first. Last year was 3266800."):
    return {"stop_reason": stop, "usage": USAGE, "_started_at": "2026-10-16T12:00:00+00:00", "_latency_s": 5.0,
            "content": [{"type": "thinking", "thinking": "..."}, {"type": "text", "text": early_text},
                        {"type": "server_tool_use", "input": {"query": "JNTO September 2026 visitor arrivals"}},
                        {"type": "web_search_tool_result", "content": [
                            {"url": "https://www.jnto.go.jp/a.html", "title": "JNTO", "page_age": "2026-10-01",
                             "encrypted_content": "xxx"}]},
                        {"type": "thinking", "thinking": "..."}, {"type": "text", "text": final}]}


class Fake:
    model = "deepseek-flash"

    def __init__(self, *responses):
        self.responses, self.bodies = list(responses), []

    def call(self, body, *, qid, attempt):
        self.bodies.append(json.loads(json.dumps(body)))
        return self.responses.pop(0)


class TestSearchDirect(unittest.TestCase):
    def test_one_call_with_tools_same_user_message(self):
        c = Fake(resp('{"estimate": 3100000, "unit": ""}'))
        r = SD.run_search_direct(c, Q)
        self.assertEqual((r["status"], r["estimate"], r["final_attempt"]), ("ok", 3100000.0, 1))
        b = c.bodies[0]
        self.assertEqual(b["tools"], [{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}])
        self.assertTrue(b["system"].startswith(NAIVE_SYSTEM))
        self.assertIn("Your final message must contain only the JSON object.", b["system"])
        self.assertEqual(b["messages"], [{"role": "user", "content": _messages(NAIVE_SYSTEM, Q)[1]["content"]}])
        a = r["attempts"][0]
        self.assertEqual(a["queries"], ["JNTO September 2026 visitor arrivals"])
        self.assertEqual(a["results"], [{"url": "https://www.jnto.go.jp/a.html", "title": "JNTO", "page_age": "2026-10-01"}])
        self.assertEqual((a["web_search_requests"], a["usd_search_fee_assumed"], a["n_thinking_blocks"]), (2, 0.02, 2))
        self.assertGreater(a["usd"], 0)
        self.assertNotIn("encrypted_content", json.dumps(r))

    def test_only_text_after_last_tool_block_is_read(self):
        # 搜索之前那段文字里的数（3266800）不能被当成答案
        c = Fake(resp("Done."), resp('{"estimate": 2900000, "unit": ""}'))
        r = SD.run_search_direct(c, Q)
        self.assertEqual(r["attempts"][0]["problems"], ["reply is not valid JSON"])
        self.assertEqual(r["estimate"], 2900000.0)

    def test_fenced_json_and_trailing_words(self):
        for text in ('```json\n{"estimate": 3.1e6, "unit": ""}\n```', 'Answer: {"estimate": 3100000, "unit": ""}'):
            self.assertEqual(SD.run_search_direct(Fake(resp(text)), Q)["estimate"], 3100000.0)

    def test_retry_once_without_tools_with_problem_list(self):
        c = Fake(resp('{"estimate": "about 3 million", "unit": ""}'), resp('{"estimate": 3000000, "unit": ""}'))
        r = SD.run_search_direct(c, Q)
        self.assertEqual((r["final_attempt"], r["estimate"]), (2, 3000000.0))
        b2 = c.bodies[1]
        self.assertNotIn("tools", b2)
        self.assertEqual([m["role"] for m in b2["messages"]], ["user", "assistant", "user"])
        self.assertIn('"estimate" must be a positive JSON number', b2["messages"][2]["content"])
        self.assertEqual(r["attempts"][1]["with_tools"], False)

    def test_two_invalid_replies_give_no_estimate(self):
        r = SD.run_search_direct(Fake(resp("no idea"), resp('{"estimate": -1}')), Q)
        self.assertEqual((r["status"], r["estimate"], r["final_attempt"]), ("invalid_output", None, 2))

    def test_truncated_reply_is_invalid(self):
        c = Fake(resp('{"estimate": 3100000, "unit": ""}', stop="max_tokens"), resp('{"estimate": 3200000, "unit": ""}'))
        r = SD.run_search_direct(c, Q)
        self.assertEqual(r["attempts"][0]["problems"], ["reply was truncated (stop_reason=max_tokens)"])
        self.assertEqual(r["estimate"], 3200000.0)

    def test_max_tokens_default_and_override(self):
        c = Fake(resp('{"estimate": 1, "unit": ""}'), resp('{"estimate": 1, "unit": ""}'))
        self.assertEqual(SD.run_search_direct(c, Q)["max_tokens"], 4096)
        self.assertEqual(SD.run_search_direct(c, Q, max_tokens=32000)["max_tokens"], 32000)
        self.assertEqual([b["max_tokens"] for b in c.bodies], [4096, 32000])

    def test_costs_are_summed_over_attempts(self):
        r = SD.run_search_direct(Fake(resp("x"), resp('{"estimate": 1, "unit": ""}')), Q)
        self.assertAlmostEqual(r["usd"], sum(a["usd"] for a in r["attempts"]), places=6)
        self.assertEqual(r["usd_search_fee_assumed"], 0.04)


class TestThinkingControl(unittest.TestCase):
    """v2.12e：control_thinking=True 时按 config.THINKING 的 search_direct 档位显式开 / 关思考（同另两个臂的按角色机制）；
    默认调用的请求体不变（不带 thinking 字段）。"""

    def run_with(self, settings, **kw):
        from triangulate import config
        c = Fake(resp("no idea"), resp('{"estimate": 3000000, "unit": ""}'))
        with mock.patch.dict(config.THINKING, settings, clear=True):
            r = SD.run_search_direct(c, Q, **kw)
        return r, c.bodies

    def test_default_request_unchanged(self):
        r, bodies = self.run_with({"search_direct": "high"})   # 默认调用不看档位
        self.assertEqual([list(b) for b in bodies], [["model", "max_tokens", "system", "messages", "tools"],
                                                     ["model", "max_tokens", "system", "messages"]])
        self.assertEqual([b["max_tokens"] for b in bodies], [4096, 4096])
        self.assertNotIn("thinking", r)

    def test_off_sends_disabled_on_both_attempts(self):
        r, bodies = self.run_with({}, control_thinking=True)
        self.assertEqual([b["thinking"] for b in bodies], [{"type": "disabled"}] * 2)
        self.assertTrue(all("output_config" not in b for b in bodies))
        self.assertEqual(([b["max_tokens"] for b in bodies], r["max_tokens"], r["thinking"]), ([4096, 4096], 4096, "disabled"))
        self.assertEqual(list(bodies[0]), ["model", "max_tokens", "system", "messages", "thinking", "tools"])

    def test_on_sends_effort_and_extra_tokens(self):
        from triangulate import config
        r, bodies = self.run_with({"search_direct": "high", "naive": "low"}, control_thinking=True)
        want = 4096 + config.THINKING_EXTRA_TOKENS
        for b in bodies:
            self.assertEqual((b["thinking"], b["output_config"], b["max_tokens"]), ({"type": "enabled"}, {"effort": "high"}, want))
        self.assertEqual((r["max_tokens"], r["thinking"], r["estimate"]), (want, "high", 3000000.0))
        r, bodies = self.run_with({"naive": "high"}, control_thinking=True)   # 别的角色开了，这个臂照旧关
        self.assertEqual(bodies[0]["thinking"], {"type": "disabled"})

    def test_same_endpoint_and_tool_as_the_agent_searcher(self):
        from triangulate import providers
        from triangulate.agent import search as S
        self.assertEqual(SD.SEARCH_URL, S.SEARCH_URL)
        _, payload = providers.DEEPSEEK.search_request("deepseek-flash", "k", "p", max_tokens=1, max_uses=SD.MAX_USES)
        _, bodies = self.run_with({}, control_thinking=True)
        self.assertEqual(bodies[0]["tools"], payload["tools"])


class TestDirectClient(unittest.TestCase):
    def test_transport_failure_resends_three_times_then_raises(self):
        logs = []
        with mock.patch("triangulate.agent.search.read_key", return_value="sk-FAKE-123"):
            c = SD.DirectClient(logs.append)
        with mock.patch("triangulate.llm.urlopen_no_redirect", side_effect=urllib.error.URLError("down")) as u, \
                mock.patch("time.sleep"):
            with self.assertRaises(TransportError):
                c.call({"model": "deepseek-flash"}, qid="q", attempt=1)
        self.assertEqual(u.call_count, 3)
        self.assertEqual(len(logs), 1)
        self.assertNotIn("sk-FAKE-123", json.dumps(logs))

    def test_ok_response_is_logged_with_tokens(self):
        logs = []
        with mock.patch("triangulate.agent.search.read_key", return_value="secret"):
            c = SD.DirectClient(logs.append)
        body = json.dumps({"stop_reason": "end_turn", "usage": USAGE, "content": []}).encode()
        r = mock.MagicMock()
        r.__enter__.return_value = mock.MagicMock(status=200, read=lambda: body)
        with mock.patch("triangulate.llm.urlopen_no_redirect", return_value=r) as u:
            d = c.call({"model": "deepseek-flash"}, qid="q", attempt=1)
        self.assertEqual(u.call_args[0][0].full_url, SD.SEARCH_URL)
        self.assertEqual(d["stop_reason"], "end_turn")
        self.assertEqual((logs[0]["ok"], logs[0]["web_search_requests"], logs[0]["output_tokens"]), (True, 2, 300))
        self.assertNotIn("secret", json.dumps(logs))


class TestRunSearch(unittest.TestCase):
    def test_only_live_questions_and_skip_saved(self):
        seen = []

        def fake_run(client, q):
            seen.append(q["id"])
            return {"attempts": [{}], "status": "ok", "estimate": 1.0}
        with tempfile.TemporaryDirectory() as d, mock.patch.object(forecast, "FC", Path(d)), \
                mock.patch.object(SD, "DirectClient", lambda log: object()), \
                mock.patch.object(SD, "run_search_direct", fake_run):
            forecast.run_search()
            self.assertEqual(sorted(seen), ["fc_jnto_2026_09", "fc_kr_births_2026_08"])
            self.assertTrue((Path(d) / "raw" / "search_direct" / "fc_jnto_2026_09.json").exists())
            seen.clear()
            forecast.run_search()
            self.assertEqual(seen, [])


if __name__ == "__main__":
    unittest.main()

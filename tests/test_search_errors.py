"""v2.6a（N25）：Searcher 的 n_search_errors 也数 list 里的 web_search_tool_result_error。
DeepSeek 的 Anthropic 兼容接口把错误放在 list 里（probes/out/deepseek_search_probe.json 的第 10、11 块：
content = [{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]），以前只数「content 不是 list」的情形，记成 0。
只改 calls.jsonl 那一行的 n_search_errors；返回给 run_direction 的结构不变。不联网、不读 key（假 urlopen）。"""
import json
import unittest
from unittest import mock

from triangulate.agent import search as S

# 返回给调用方的键（v2.5.5 起没变过；S4 不往 state 加字段）
RETURN_KEYS = {"queries", "urls", "n_text_urls", "n_result_urls", "web_search_requests", "usd", "usd_search_fee_assumed"}


def _result(*urls):
    return {"type": "web_search_tool_result", "tool_use_id": "t",
            "content": [{"type": "web_search_result", "title": "x", "url": u, "page_age": None} for u in urls]}


ERROR_IN_LIST = {"type": "web_search_tool_result", "tool_use_id": "t",
                 "content": [{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]}
ERROR_AS_DICT = {"type": "web_search_tool_result", "tool_use_id": "t",       # Anthropic 文档里的写法：content 直接是错误对象
                 "content": {"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}}


def run(content):
    """假 urlopen 回一次 200，返回 (search 的返回值, 记进 calls.jsonl 的那一行)。"""
    body = {"content": content, "stop_reason": "end_turn",
            "usage": {"input_tokens": 100, "output_tokens": 10, "server_tool_use": {"web_search_requests": 4}}}

    class Resp:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return json.dumps(body).encode("utf-8")

    logged = []
    s = object.__new__(S.Searcher)   # 不走 __init__：不读 key
    s.model, s._key, s._log = "deepseek-flash", "not-a-key", logged.append
    with mock.patch("triangulate.llm.urlopen_no_redirect", lambda req, timeout: Resp()):
        out = s.search("p", role="search:d1", qid="t")
    return out, logged[-1]


class TestSearchErrorCount(unittest.TestCase):
    def test_errors_inside_list_are_counted(self):
        """探针的形状：2 个正常结果块 + 2 个 list 里的 max_uses_exceeded 错误块。"""
        content = [{"type": "server_tool_use", "input": {"query": "q1"}}, {"type": "server_tool_use", "input": {"query": "q2"}},
                   _result("https://a.example.org/1", "https://a.example.org/2"), _result("https://b.example.org/1"),
                   {"type": "server_tool_use", "input": {"query": "q3"}}, {"type": "server_tool_use", "input": {"query": "q4"}},
                   ERROR_IN_LIST, ERROR_IN_LIST,
                   {"type": "text", "text": "https://b.example.org/1\nhttps://a.example.org/2"}]
        out, rec = run(content)
        self.assertEqual(rec["n_search_errors"], 2)
        # 错误块不带 URL，其余计数和 URL 不受影响
        self.assertEqual(rec["n_result_urls"], 3)
        self.assertEqual(out["urls"], ["https://b.example.org/1", "https://a.example.org/2", "https://a.example.org/1"])
        self.assertEqual(out["queries"], ["q1", "q2", "q3", "q4"])
        self.assertEqual(set(out), RETURN_KEYS)

    def test_error_object_not_in_list_still_counted_once(self):
        out, rec = run([_result("https://a.example.org/1"), ERROR_AS_DICT])
        self.assertEqual(rec["n_search_errors"], 1)
        self.assertEqual(out["urls"], ["https://a.example.org/1"])
        self.assertEqual(set(out), RETURN_KEYS)

    def test_normal_and_empty_lists_are_not_errors(self):
        out, rec = run([_result("https://a.example.org/1"), _result(), {"type": "text", "text": "none"}])
        self.assertEqual(rec["n_search_errors"], 0)
        self.assertEqual(rec["n_result_urls"], 1)
        self.assertEqual(set(out), RETURN_KEYS)


if __name__ == "__main__":
    unittest.main()

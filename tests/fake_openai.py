"""v2.10c：127.0.0.1 上的假 OpenAI API（Chat Completions、Responses、List models），给 tests/test_openai.py 用。不联网、不需要真 key。

服务端复用 tests/fake_claude.py 的脚本化 HTTP 服务（按脚本依次回复，记下每个请求的方法、路径、小写请求头、JSON body）；
这里只加 OpenAI 形状的回复和 regions()。脚本项同 fake_claude：("json", status, obj[, headers])、("raw", ...)、("redirect", ...)。
"""
from tests.fake_claude import FakeClaude

# 2026-10-21 对 https://api.openai.com/v1/models 实测（probes/openai_key_probe.py，没花钱）的两种 HTTP 401 body
REAL_401_NO_KEY = {"error": {"message": "Missing bearer authentication in header", "type": "invalid_request_error",
                             "param": None, "code": None}}
REAL_401_FAKE_KEY = {"error": {"message": "Incorrect API key provided: sk-proj-**********************0000. You can find your "
                                          "API key at https://platform.openai.com/account/api-keys.",
                               "type": "invalid_request_error", "param": None, "code": "invalid_api_key"}}


def error_body(etype: str, message: str, code=None, param=None) -> dict:
    """API 的错误形状：{"error": {"message", "type", "param", "code"}}（Error codes 页、上面的实测 body）。"""
    return {"error": {"message": message, "type": etype, "param": param, "code": code}}


def chat_completion(content='{"a": 1}', finish_reason="stop", usage=None, refusal=None, model="gpt-6-luna"):
    """Chat Completions 的回复（API 参考 ChatCompletion 对象）。"""
    return {"id": "chatcmpl-fake", "object": "chat.completion", "created": 1792000000, "model": model,
            "choices": [{"index": 0, "finish_reason": finish_reason, "logprobs": None,
                         "message": {"role": "assistant", "content": content, "refusal": refusal, "annotations": []}}],
            "usage": usage or {"prompt_tokens": 1000, "completion_tokens": 300, "total_tokens": 1300,
                               "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
                               "completion_tokens_details": {"reasoning_tokens": 0}},
            "service_tier": "default"}


def search_call(queries=("widgets June 2025",), sources=("https://stats.example.org/w", "https://b.example.org/x"),
                status="completed", kind="search", url=None):
    """Responses 的 web_search_call 输出项（API 参考 WebSearchCall：action 是 search / open_page / find_in_page）。"""
    if kind == "search":
        action = {"type": "search", "queries": list(queries), "query": queries[0] if queries else None,
                  "sources": [{"type": "url", "url": u} for u in sources]}
    else:
        action = {"type": kind, "url": url}
    return {"type": "web_search_call", "id": "ws_fake", "status": status, "action": action}


def response(output, status="completed", usage=None, incomplete=None, model="gpt-6-luna"):
    """Responses API 的 Response 对象。"""
    return {"id": "resp_fake", "object": "response", "created_at": 1792000000, "status": status, "model": model,
            "error": None, "incomplete_details": {"reason": incomplete} if incomplete else None, "output": output,
            "usage": usage or {"input_tokens": 6039, "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
                               "output_tokens": 931, "output_tokens_details": {"reasoning_tokens": 0}, "total_tokens": 6970},
            "store": False}


def message(text, citations=()):
    """Responses 的 message 输出项：output_text + url_citation 注解（url、title、start_index、end_index）。"""
    anns = [{"type": "url_citation", "url": u, "title": t, "start_index": 0, "end_index": 1} for u, t in citations]
    return {"type": "message", "id": "msg_fake", "status": "completed", "role": "assistant",
            "content": [{"type": "output_text", "text": text, "annotations": anns, "logprobs": []}]}


class FakeOpenAI(FakeClaude):
    def regions(self) -> dict:
        return {"global": {"chat": self.url("/v1/chat/completions"), "search": self.url("/v1/responses"),
                           "models": self.url("/v1/models")}}

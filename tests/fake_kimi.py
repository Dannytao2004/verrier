"""v2.10d：127.0.0.1 上的假 Kimi API（Chat Completions 流式、/v1/models；v2.10h 起搜索是 /v1/responses，不再有 /v1/tools/search），
给 tests/test_kimi.py 用。不联网、不需要真 key。

服务端复用 tests/fake_claude.py 的脚本化 HTTP 服务（按脚本依次回复，记下每个请求的方法、路径、小写请求头、JSON body）；
这里只加 Kimi 形状的回复和 regions()。流式回复用 ("raw", 200, sse_bytes) 一次写出（LLM._post 读完整个 body 才解码）。
国际站和国内站接到同一个假服务的不同路径上（/v1/... 和 /cn/v1/...），测试据此确认区域选对了。
"""
import json

from tests.fake_claude import FakeClaude

# 2026-10-21 实测（probes/kimi_key_probe.py，没花钱）：GET https://api.moonshot.ai/v1/models 不带 key / 带假 key 的 HTTP 401 body；
# 国内站 api.moonshot.cn 带假 key 同 REAL_401_FAKE_KEY
REAL_401_NO_KEY = {"error": {"message": "Incorrect API key provided", "type": "incorrect_api_key_error"}}
REAL_401_FAKE_KEY = {"error": {"message": "Invalid Authentication", "type": "invalid_authentication_error"}}


def error_body(etype: str, message: str) -> dict:
    """Common Error Codes 页的错误形状：{"error": {"type", "message"}}。"""
    return {"error": {"type": etype, "message": message}}


def usage(prompt=1000, completion=300, cached=0, write=0) -> dict:
    """Chat API 的 usage：顶层 cached_tokens + prompt_tokens_details（cached_tokens、cache_write_tokens）。"""
    return {"prompt_tokens": prompt, "completion_tokens": completion, "total_tokens": prompt + completion,
            "cached_tokens": cached, "prompt_tokens_details": {"cached_tokens": cached, "cache_write_tokens": write}}


def sse(content='{"a": 1}', finish_reason="stop", use=None, reasoning="Let me think about the widgets.", pieces=3,
        include_usage=True, done=True, model="kimi-k3", crlf=False, keepalive=True) -> bytes:
    """一条流式回复（Chat API 页的 SSE 格式）：先是 reasoning_content 的 delta（思考，总在 content 之前），content 分 pieces 段，
    最后一个 choice 带 finish_reason；include_usage 时 [DONE] 之前多一个 choices 为空的 usage chunk。"""
    def chunk(choices, u=None):
        d = {"id": "cmpl-fake", "object": "chat.completion.chunk", "created": 1792000000, "model": model, "choices": choices}
        if u is not None:
            d["usage"] = u
        return "data: " + json.dumps(d) + "\n\n"
    out = [chunk([{"index": 0, "delta": {"role": "assistant", "content": ""}, "finish_reason": None}])]
    if keepalive:
        out.append(": keep-alive\n\n")
    if reasoning:
        out.append(chunk([{"index": 0, "delta": {"reasoning_content": reasoning}, "finish_reason": None}]))
    n = max(1, pieces)
    step = max(1, -(-len(content) // n)) if content else 1
    for i in range(0, len(content), step):
        out.append(chunk([{"index": 0, "delta": {"content": content[i:i + step]}, "finish_reason": None}]))
    out.append(chunk([{"index": 0, "delta": {}, "finish_reason": finish_reason}]))
    if include_usage:
        out.append(chunk([], use or usage()))
    if done:
        out.append("data: [DONE]\n\n")
    text = "".join(out)
    return (text.replace("\n", "\r\n") if crlf else text).encode("utf-8")


def responses_usage(inp=9000, out=600, cached=0, write=0, reasoning=200) -> dict:
    """v2.10h：Responses API 的 usage（Responses 页 ResponsesUsage）：input_tokens 是全部输入，input_tokens_details 的 cached_tokens /
    cache_write_tokens 和未缓存的部分互斥；output_tokens 含思考（output_tokens_details.reasoning_tokens）。"""
    return {"input_tokens": inp, "input_tokens_details": {"cached_tokens": cached, "cache_write_tokens": write},
            "output_tokens": out, "output_tokens_details": {"reasoning_tokens": reasoning}, "total_tokens": inp + out}


def search_response(text="https://a.example.org/w", query="widgets June 2026 official statistics", sources=(), searched=True,
                    status="completed", incomplete=None, use=None) -> dict:
    """v2.10h：K3 搜索的非流式回复（Responses 页 ResponsesResponse）。output 的顺序：web_search_call（服务端决定要搜时才有）、reasoning、
    message。web_search_call.action：type search、query、sources [{type: url, url, title}]（include 了才有）。"""
    output = []
    if searched:
        output.append({"type": "web_search_call", "id": "ws_fake01", "status": "completed",
                       "action": {"type": "search", "query": query,
                                  "sources": [{"type": "url", "url": u, "title": f"Title of {u.rsplit('/', 1)[-1]}"} for u in sources]}})
    output.append({"type": "reasoning", "id": "rs_fake01", "summary": [{"type": "summary_text", "text": "SECRET-REASONING"}],
                   "encrypted_content": None, "status": "completed"})
    output.append({"type": "message", "id": "msg_fake01", "role": "assistant", "status": "completed",
                   "content": [{"type": "output_text", "text": text, "annotations": []}]})
    return {"id": "resp_fake01", "object": "response", "created_at": 1792000000, "status": status, "model": "kimi-k3",
            "output": output, "usage": use or responses_usage(), "incomplete_details": incomplete, "error": None, "store": False}


class FakeKimi(FakeClaude):
    def regions(self) -> dict:
        return {"global": {"chat": self.url("/v1/chat/completions"), "search": self.url("/v1/responses"),
                           "models": self.url("/v1/models")},
                "cn": {"chat": self.url("/cn/v1/chat/completions"), "search": self.url("/cn/v1/responses"),
                       "models": self.url("/cn/v1/models")}}

"""v2.10d：127.0.0.1 上的假 Kimi API（Chat Completions 流式、/v1/tools/search、/v1/models），给 tests/test_kimi.py 用。
不联网、不需要真 key。

服务端复用 tests/fake_claude.py 的脚本化 HTTP 服务（按脚本依次回复，记下每个请求的方法、路径、小写请求头、JSON body）；
这里只加 Kimi 形状的回复和 regions()。流式回复用 ("raw", 200, sse_bytes) 一次写出（LLM._post 读完整个 body 才解码）。
国际站和国内站接到同一个假服务的不同路径上（/v1/... 和 /cn/v1/...），测试据此确认区域选对了。
"""
import json

from tests.fake_claude import FakeClaude

# 2026-10-21 实测（probes/kimi_key_probe.py，没花钱）：GET https://api.moonshot.ai/v1/models 不带 key / 带假 key 的 HTTP 401 body；
# 国内站 api.moonshot.cn 带假 key 同 REAL_401_FAKE_KEY；POST /v1/tools/search 带假 key 是 401、body 为空（文档：No error body）
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
        include_usage=True, done=True, model="kimi-k2.6", crlf=False, keepalive=True) -> bytes:
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


def search_result(url, title="", snippet="snippet", site="Example"):
    """/v1/tools/search 的一条结果（Web Search Basic 页：所有字段都在，没有数据时是空字符串）。"""
    return {"authority": "S", "date": "2026-06-01", "icon": "", "mime": "text/html", "site_name": site, "snippet": snippet,
            "text": "", "title": title, "url": url}


def search_results(*urls) -> dict:
    return {"search_results": [search_result(u, title=f"Title of {u.rsplit('/', 1)[-1]}") for u in urls]}


class FakeKimi(FakeClaude):
    def regions(self) -> dict:
        return {"global": {"chat": self.url("/v1/chat/completions"), "search": self.url("/v1/tools/search"),
                           "models": self.url("/v1/models")},
                "cn": {"chat": self.url("/cn/v1/chat/completions"), "search": self.url("/cn/v1/tools/search"),
                       "models": self.url("/cn/v1/models")}}

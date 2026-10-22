"""v2.10e：127.0.0.1 上的假 GLM API（Chat Completions 非流式、/models；v2.10h 起搜索也是 Chat Completions 带自带的 web_search 工具，
不再有独立的 /web_search），给 tests/test_glm.py 用。不联网、不需要真 key。

服务端复用 tests/fake_claude.py 的脚本化 HTTP 服务（按脚本依次回复，记下每个请求的方法、路径、小写请求头、JSON body）；
这里只加 GLM 形状的回复和 regions()。国际站和国内站接到同一个假服务的不同路径上（/api/paas/v4/... 和 /cn/api/paas/v4/...），
测试据此确认区域选对了。
"""
from tests.fake_claude import FakeClaude

# 2026-10-21 实测（probes/glm_key_probe.py，没花钱）：GET https://api.z.ai/api/paas/v4/models 不带 key / 带假 key 的 HTTP 401 body；
# 国内站 open.bigmodel.cn 带假 key 是同一个 code、中文 message。POST /chat/completions、/web_search 带假 key 也是同样的 body
# （/web_search 是 v2.10e 用的独立搜索接口，v2.10h 起不用）
REAL_401_NO_KEY = {"error": {"code": "1001", "message": "Authentication parameter not received in Header, unable to authenticate"}}
REAL_401_FAKE_KEY = {"error": {"code": "1000", "message": "Authentication Failed"}}
REAL_401_FAKE_KEY_CN = {"error": {"code": "1000", "message": "身份验证失败。"}}


def error_body(code, message: str, *, wrapped: bool = True) -> dict:
    """错误码页的形状 {"error": {"code": "1214", "message"}}（code 是字符串，实测如此）；wrapped=False 时是 API 参考里 Error schema 的
    形状 {"code": 1214, "message"}（没有外层 error，code 是整数）。"""
    if wrapped:
        return {"error": {"code": str(code), "message": message}}
    return {"code": int(code), "message": message}


def usage(prompt=1000, completion=300, cached=0) -> dict:
    """Chat Completion API 的 usage：prompt_tokens、completion_tokens、prompt_tokens_details.cached_tokens、total_tokens。"""
    return {"completion_tokens": completion, "prompt_tokens": prompt, "prompt_tokens_details": {"cached_tokens": cached},
            "total_tokens": prompt + completion}


def web_search_item(url, i=1, title=None, content="summary", media="Example"):
    """v2.10h：回复顶层 web_search[] 的一条（API 参考：title、link、content、media、icon、refer、publish_date；联网搜索指南的示例）。"""
    return {"content": content, "icon": "", "link": url, "media": media, "publish_date": "2026-06-01", "refer": f"ref_{i}",
            "title": f"Title of {url.rsplit('/', 1)[-1]}" if title is None else title}


def completion(content='{"a": 1}', finish_reason="stop", use=None, reasoning="Let me think about the widgets.",
               model="glm-5.2", web=None) -> dict:
    """一条非流式回复（API 参考 ChatCompletionResponse；思考内容在 message.reasoning_content，Deep Thinking 指南的示例）。
    web（v2.10h）：带 web_search 工具、search_result: true 时顶层的 web_search[]（一组 URL）。"""
    msg = {"role": "assistant", "content": content}
    if reasoning is not None:
        msg["reasoning_content"] = reasoning
    out = {"id": "20261021fake0001", "request_id": "20261021fake0001", "created": 1792000000, "model": model,
           "choices": [{"index": 0, "message": msg, "finish_reason": finish_reason}], "usage": use or usage()}
    if web is not None:
        out["web_search"] = [web_search_item(u, i) for i, u in enumerate(web, 1)]
    return out


class FakeGLM(FakeClaude):
    def regions(self) -> dict:
        return {"global": {"chat": self.url("/api/paas/v4/chat/completions"), "search": self.url("/api/paas/v4/chat/completions"),
                           "models": self.url("/api/paas/v4/models")},
                "cn": {"chat": self.url("/cn/api/paas/v4/chat/completions"), "search": self.url("/cn/api/paas/v4/chat/completions"),
                       "models": self.url("/cn/api/paas/v4/models")}}

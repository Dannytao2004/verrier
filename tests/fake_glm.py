"""v2.10e：127.0.0.1 上的假 GLM API（Chat Completions 非流式、/web_search、/models），给 tests/test_glm.py 用。
不联网、不需要真 key。

服务端复用 tests/fake_claude.py 的脚本化 HTTP 服务（按脚本依次回复，记下每个请求的方法、路径、小写请求头、JSON body）；
这里只加 GLM 形状的回复和 regions()。国际站和国内站接到同一个假服务的不同路径上（/api/paas/v4/... 和 /cn/api/paas/v4/...），
测试据此确认区域选对了。
"""
from tests.fake_claude import FakeClaude

# 2026-10-21 实测（probes/glm_key_probe.py，没花钱）：GET https://api.z.ai/api/paas/v4/models 不带 key / 带假 key 的 HTTP 401 body；
# 国内站 open.bigmodel.cn 带假 key 是同一个 code、中文 message。POST /chat/completions、/web_search 带假 key 也是同样的 body
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


def completion(content='{"a": 1}', finish_reason="stop", use=None, reasoning="Let me think about the widgets.",
               model="glm-5.2") -> dict:
    """一条非流式回复（API 参考 ChatCompletionResponse；思考内容在 message.reasoning_content，Deep Thinking 指南的示例）。"""
    msg = {"role": "assistant", "content": content}
    if reasoning is not None:
        msg["reasoning_content"] = reasoning
    return {"id": "20261021fake0001", "request_id": "20261021fake0001", "created": 1792000000, "model": model,
            "choices": [{"index": 0, "message": msg, "finish_reason": finish_reason}], "usage": use or usage()}


def search_result(url, title="", content="summary", media="Example"):
    """/web_search 的一条结果（API 参考 WebSearchObjectResponse）。"""
    return {"title": title, "content": content, "link": url, "media": media, "icon": "", "refer": "ref_1",
            "publish_date": "2026-06-01"}


def search_results(*urls) -> dict:
    return {"created": 1792000000, "id": "20261021fakesearch", "request_id": "20261021fakesearch",
            "search_result": [search_result(u, title=f"Title of {u.rsplit('/', 1)[-1]}") for u in urls]}


class FakeGLM(FakeClaude):
    def regions(self) -> dict:
        return {"global": {"chat": self.url("/api/paas/v4/chat/completions"), "search": self.url("/api/paas/v4/web_search"),
                           "models": self.url("/api/paas/v4/models")},
                "cn": {"chat": self.url("/cn/api/paas/v4/chat/completions"), "search": self.url("/cn/api/paas/v4/web_search"),
                       "models": self.url("/cn/api/paas/v4/models")}}

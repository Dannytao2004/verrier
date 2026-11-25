"""v2.10a 金样本：DeepSeek 默认路径（没有 ModelSpec：命令行、回测、基线）发出的 HTTP 请求和 calls.jsonl 行。

capture() 用假 urlopen 跑一组固定输入（json_call、AgentLLM.ask、Searcher.search、基线的 DirectClient.call），记下
每个请求的 URL、方法、请求头、请求体字节、超时，每行日志（只把 at / latency_s 换成占位符），以及返回值或异常。
不联网、不读 key 文件（read_key 换成假 key）。tests/golden/deepseek_requests_head.json 是在 HEAD b01734d（v2.9b）
的导出上跑出来的：
  git archive b01734d triangulate | tar -x -C probes/out/_old_v2_9b
  .venv/Scripts/python.exe tests/golden_deepseek.py probes/out/_old_v2_9b tests/golden/deepseek_requests_head.json
tests/test_provider_golden.py 在现在的代码上再跑一次 capture()，和这份文件逐字节比较。
v2.13d：DeepSeek 的裁判 / 修正 / 抽取默认上限放宽（providers.DEEPSEEK_MAX_TOKENS）以后，这份文件里只有 json_extract_off_while_thinking
的请求体按默认上限发（16000 -> 64000），只改了这一处；其余用例显式传上限，照原样（和 v2.13c 的 capture 逐行比过）。
"""
import io
import json
import sys
import tempfile
import urllib.error
from pathlib import Path
from unittest import mock

FAKE_KEY = "sk-golden-0123456789abcdef"
MSGS = [{"role": "system", "content": "You are a careful analyst. 只回 JSON。"},
        {"role": "user", "content": "Estimate widgets in June 2026 (单位：万件). Reply {\"a\": 1}."}]
USAGE = {"prompt_tokens": 1200, "prompt_cache_hit_tokens": 256, "prompt_cache_miss_tokens": 944,
         "completion_tokens": 300, "completion_tokens_details": {"reasoning_tokens": 120}}


def _chat(content, finish="stop", usage=USAGE):
    return json.dumps({"choices": [{"message": {"content": content}, "finish_reason": finish}], "usage": usage}).encode()


SEARCH_BODY = json.dumps({"stop_reason": "end_turn", "content": [
    {"type": "server_tool_use", "input": {"query": "widgets June 2025 official"}},
    {"type": "web_search_tool_result", "content": [{"type": "web_search_result", "url": "https://stats.example.org/w"},
                                                   {"type": "web_search_result", "url": "https://b.example.org/x"}]},
    {"type": "server_tool_use", "input": {"query": "widgets 2024"}},
    {"type": "web_search_tool_result", "content": [{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]},
    {"type": "text", "text": "Best: https://stats.example.org/w, and https://c.example.org/y."}],
    "usage": {"input_tokens": 15000, "cache_read_input_tokens": 12000, "output_tokens": 900,
              "server_tool_use": {"web_search_requests": 2}}}).encode()


class _Resp:
    def __init__(self, status, body):
        self.status, self._body, self._done = status, body, False

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self):
        return self._body

    def read1(self, n):
        if self._done:
            return b""
        self._done = True
        return self._body


class _Net:
    """按顺序回放脚本里的回复：("ok", status, body) / ("http", code, body) / ("down",)。"""

    def __init__(self):
        self.script, self.seen, self.errors = [], [], []

    def close(self):
        """关掉抛出过的 HTTPError（它带一个临时文件对象，不关的话垃圾回收时有 ResourceWarning）。"""
        for e in self.errors:
            e.close()
        self.errors = []

    def __call__(self, req, timeout):
        self.seen.append({"url": req.full_url, "method": req.get_method(), "headers": sorted(req.header_items()),
                          "body": req.data.decode("utf-8"), "timeout": timeout})
        kind, *rest = self.script.pop(0)
        if kind == "down":
            raise urllib.error.URLError("down")
        code, body = rest
        if kind == "http":
            self.errors.append(urllib.error.HTTPError(req.full_url, code, "x", {}, io.BytesIO(body)))
            raise self.errors[-1]
        return _Resp(code, body)


def _norm_log(lines):
    out = []
    for line in lines:
        r = json.loads(line) if isinstance(line, str) else dict(line)
        for k in ("at", "latency_s"):
            if k in r:
                r[k] = f"<{k}>"
        out.append(json.dumps(r, ensure_ascii=False))
    return out


def _exc(e):
    from triangulate.llm import TransportError
    return {"raised": type(e).__name__, "message": str(e), "is_transport_error": isinstance(e, TransportError)}


def capture() -> dict:
    from triangulate import config, llm
    from triangulate.agent import pipeline as P
    from triangulate.agent import search as S
    from triangulate import search_direct as SD

    net, cases = _Net(), []
    tmp = Path(tempfile.mkdtemp())
    with mock.patch.object(llm, "urlopen_no_redirect", net), mock.patch("time.sleep"), \
            mock.patch.object(llm, "read_key", return_value=FAKE_KEY), mock.patch.object(S, "read_key", return_value=FAKE_KEY), \
            mock.patch.object(config, "is_peak", lambda t: False):

        def chat(name, script, *, arm="judge:r1", max_tokens=12000, thinking=None, msgs=MSGS, peak=False):
            calls = tmp / f"{name}.jsonl"
            net.script, net.seen = list(script), []
            with mock.patch.object(llm, "THINKING", thinking or {}), mock.patch.object(config, "is_peak", lambda t: peak):
                client = llm.LLM(calls_path=calls)
                try:
                    res = list(client.json_call(msgs, arm=arm, qid="t", attempt=1, max_tokens=max_tokens))
                except Exception as e:  # noqa: BLE001
                    res = _exc(e)
            log = calls.read_text(encoding="utf-8").splitlines() if calls.exists() else []
            cases.append({"case": name, "requests": net.seen, "log": _norm_log(log), "result": res})

        ok = ("ok", 200, _chat('{"a": 1}'))
        chat("json_off", [ok])
        chat("json_off_peak", [ok], peak=True)
        chat("json_plan_low", [ok], arm="plan", max_tokens=6000, thinking={"plan": "low", "judge": "high", "repair": "max"})
        chat("json_repair_max", [ok], arm="judge:r2:repair", thinking={"plan": "low", "judge": "high", "repair": "max"})
        chat("json_judge_high", [ok], arm="judge:r3", thinking={"plan": "low", "judge": "high", "repair": "max"})
        chat("json_extract_off_while_thinking", [ok], arm="extract:d3", max_tokens=16000,
             thinking={"plan": "low", "judge": "high", "repair": "max"})
        chat("json_truncated", [("ok", 200, _chat('{"a": [1, 2', finish="length"))], arm="final", max_tokens=4000)
        chat("json_invalid", [("ok", 200, _chat('{"keep": [1, 2,]} trailing'))])
        chat("json_not_object", [("ok", 200, _chat("[1, 2]"))])
        chat("json_retry_500", [("http", 500, b"busy"), ("http", 503, b""), ok])
        chat("json_network_then_ok", [("down",), ok])
        chat("json_bad_body", [("ok", 200, b"<html>"), ("ok", 200, b'{"error": {"message": "overloaded"}}'),
                               ("ok", 200, b"\n\n")])
        chat("json_401", [("http", 401, b"Authentication Fails")])
        chat("json_402", [("http", 402, b'{"error": {"message": "Insufficient Balance"}}')])
        chat("json_302", [("http", 302, b"")])
        chat("json_400", [("http", 400, b'{"error": {"message": "bad"}}')])

        def search(name, script, **kw):
            logged = []
            net.script, net.seen = list(script), []
            s = S.Searcher(log=logged.append)
            try:
                res = s.search("Find official widget data. 中文提示。", role="search:d2", qid="t", **kw)
            except Exception as e:  # noqa: BLE001
                res = _exc(e)
            cases.append({"case": name, "requests": net.seen, "log": _norm_log(logged), "result": res})

        search("search_ok", [("ok", 200, SEARCH_BODY)], max_uses=3, cap=4)
        search("search_ok_defaults", [("ok", 200, SEARCH_BODY)])
        search("search_retry_503", [("http", 503, b""), ("ok", 200, SEARCH_BODY)], max_uses=2, cap=2)
        search("search_401", [("http", 401, b"")])
        search("search_402", [("http", 402, b"")])
        search("search_bad_body", [("ok", 200, b"not json")])

        # 运行上下文：Context 建的 AgentLLM（第一次回复无效、带错误重问一次）和 Searcher，花费计入同一个预算
        calls = tmp / "ctx.jsonl"
        net.script, net.seen = [("ok", 200, _chat("not json")), ok, ("ok", 200, SEARCH_BODY)], []
        ctx = P.Context("t", "How many widgets?", "2026-06-20", calls)
        res = [list(ctx.llm.ask(MSGS[0]["content"], MSGS[1]["content"], role="judge:r1", qid="t", max_tokens=12000))]
        res.append(ctx.searcher.search("p", role="search:d1", qid="t", max_uses=ctx.budget.search_max_uses,
                                       cap=ctx.budget.urls_per_direction))
        snap = ctx.budget.snapshot()
        cases.append({"case": "context_ask_and_search", "requests": net.seen,
                      "log": _norm_log(calls.read_text(encoding="utf-8").splitlines()), "result": res,
                      "budget": snap, "directions": ctx.budget.directions,
                      "llm_reserve": P.Budget.llm_reserve(1000, 12000), "search_reserve": ctx.budget.search_reserve()})

        # 基线 arm (3) 的 DirectClient（继承 Searcher 的构造）
        logged = []
        net.script, net.seen = [("ok", 200, SEARCH_BODY)], []
        d = SD.DirectClient(logged.append)
        out = d.call({"model": d.model, "max_tokens": 4096, "messages": [{"role": "user", "content": "x"}]}, qid="t", attempt=1)
        cases.append({"case": "direct_client", "requests": net.seen, "log": _norm_log(logged),
                      "result": {k: out[k] for k in ("stop_reason", "usage")}})
    net.close()
    return {"model": config.MODEL, "cases": cases}


def dumps(x) -> str:
    return json.dumps(x, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
    Path(sys.argv[2]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[2]).write_text(dumps(capture()) + "\n", encoding="utf-8")
    print(sys.modules["triangulate"].__file__)

"""v2.10a：每次运行的模型设置（ModelSpec）和各家 API 的请求格式（adapter）。v2.10b 加 Claude（原生 Messages API）。

ModelSpec = provider、model、region、思考档位、这次运行的花费上限，加上用户自己的 key（只在内存里，见 ModelSpec 的说明）。
有 ModelSpec 的运行就是「自带 key」（BYOK）的运行：pipeline.Context(spec=...) 把它交给 AgentLLM、Searcher 和 Budget。
没有 ModelSpec（命令行、回测、基线）时一切照旧：DeepSeek + key 文件，请求体和 HEAD 逐字节相同（tests/test_providers.py）。

adapter 只管各家不同的三件事：建请求（URL、请求头、请求体）、解析回复（文字、截断、用量）、计价；重试、先查截断、
JSON 解析、日志、预算这些外层循环留在 llm.LLM.json_call 和 agent/search.Searcher.search，所有 provider 共用。
设计说明和各家官方文档的链接在仓库根目录的 PROVIDERS.md。
"""
import json
import math

from .config import CLAUDE_US_GEO_MULTIPLIER, MODEL, PRICES, THINKING_EXTRA_TOKENS, UnknownModel, price, usd_cost

THINKING_UI = ("off", "low", "medium", "high")   # 网页上的一个总档位
REASONING_ROLES = ("plan", "judge", "repair")    # 档位只作用于这三个角色（config.thinking_role 的取值）；其余角色能关就关
DEFAULT_USD_CAP = 2.00
KEY_MIN_CHARS, KEY_MAX_CHARS = 8, 512

# DeepSeek 价格页（2026-10-21 查看）列了独立的 Search API（$0.75 / 1000 次成功请求，2026-11-01 起按次计费），没有单列
# Anthropic 兼容接口里服务端 web_search 工具的价格。预算里照旧按 Anthropic 公开价 $10 / 1000 次记账（保守假设，报告里单列）
DEEPSEEK_SEARCH_FEE_ASSUMED_USD = 0.01


class SpecError(ValueError):
    """ModelSpec 的某一项不合法。消息里从不带 key。"""


class KeyDropped(RuntimeError):
    """这次运行结束时 key 已经从内存里清掉了，之后不能再用这个 ModelSpec 发请求。"""


# ---------- 各家的请求格式 ----------

def anthropic_usage_to_cost(usage: dict, t, model: str = MODEL) -> float:
    """Anthropic 形的 usage（input / cache_read / cache_creation / output tokens）按 config.PRICES 计价。
    DeepSeek 的 Anthropic 兼容接口用它；cache_creation 按 cache miss 价算。"""
    return usd_cost({"prompt_cache_hit_tokens": usage.get("cache_read_input_tokens", 0) or 0,
                     "prompt_cache_miss_tokens": (usage.get("input_tokens", 0) or 0)
                     + (usage.get("cache_creation_input_tokens", 0) or 0),
                     "completion_tokens": usage.get("output_tokens", 0) or 0}, t, model)


def anthropic_search_unpack(d: dict) -> dict:
    """Anthropic Messages 形的回复（content 块数组）里取：查询词、搜索结果 URL（和标题）、文字块、搜索次数、搜索错误数。
    标题只在这里解析出来（v2.10b），Searcher 不往外传：分析角色只拿得到 URL（设计同 v2.9b）。"""
    usage = d.get("usage") or {}
    n_req = int(((usage.get("server_tool_use") or {}).get("web_search_requests")) or 0)
    queries, result_urls, result_titles, texts, n_err = [], [], [], [], 0
    for b in d.get("content") or []:
        if b.get("type") == "server_tool_use":
            queries.append(str((b.get("input") or {}).get("query", ""))[:200])
        elif b.get("type") == "web_search_tool_result":
            c = b.get("content")
            if isinstance(c, list):
                hits = [x for x in c if isinstance(x, dict) and x.get("url")]
                result_urls += [x.get("url") for x in hits]
                result_titles += [str(x.get("title") or "") for x in hits]
                # DeepSeek 把错误也放在 list 里：[{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]
                n_err += sum(1 for x in c if isinstance(x, dict) and x.get("type") == "web_search_tool_result_error")
            else:   # Claude 官方格式：出错时 content 是一个错误对象（HTTP 仍是 200）
                n_err += 1
        elif b.get("type") == "text":
            texts.append(b.get("text") or "")
    return {"usage": usage, "n_req": n_req, "queries": queries, "result_urls": result_urls, "result_titles": result_titles,
            "texts": texts, "n_err": n_err, "stop": d.get("stop_reason")}


class DeepSeekAdapter:
    """DeepSeek：JSON 调用走 OpenAI 兼容的 chat/completions（json_object 输出、temperature 0、按角色开关思考），
    搜索走 Anthropic 兼容的 /anthropic/v1/messages + 服务端 web_search 工具。请求体和 v2.9b 的 llm.py / search.py 逐字节相同。"""

    provider, label = "deepseek", "DeepSeek"
    regions = {"global": {"chat": "https://api.deepseek.com/chat/completions",
                          "search": "https://api.deepseek.com/anthropic/v1/messages",
                          "models": "https://api.deepseek.com/models"}}
    default_region = "global"
    search_fee_usd = DEEPSEEK_SEARCH_FEE_ASSUMED_USD
    error_body_statuses = frozenset()   # 判断余额不足只看状态码（402），出错时的 body 不读
    retry_statuses = frozenset({429, 500, 502, 503, 504})   # 和 v2.9b 的 llm.RETRY_STATUS 相同
    honor_retry_after = False           # 重试照旧等 2 / 4 秒（v2.9b），不看 retry-after
    log_server_error = False            # 出错时不读 body，日志里没有服务端的说明
    chat_timeouts = {}                  # 用 LLM._post 的默认值（单次读 180 秒，整次 1200 秒）
    max_search_continuations = 0        # 搜索不续 pause_turn（v2.9b 原样）
    balance_hint = "Top up the DeepSeek account and run again."

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

    def key_check_request(self, region: str, key: str):
        """校验 key 用的 GET（官方 List Models：GET /models，返回 {"object": "list", "data": [{"id": ...}]}）。"""
        return self.regions[region]["models"], {"Authorization": f"Bearer {key}"}

    @staticmethod
    def models_unpack(d: dict):
        """(模型 id 列表, 列表是否完整)。"""
        return [str(x.get("id")) for x in d["data"] if isinstance(x, dict)], True

    chat_decode = staticmethod(json.loads)

    def chat_request(self, model: str, key: str, messages: list, *, max_tokens: int, effort):
        """返回 (请求头, 请求体 dict)。键的顺序就是发出去的顺序（json.dumps 不排序）。"""
        payload = {"model": model, "messages": messages,
                   "thinking": {"type": "enabled" if effort else "disabled"}, "response_format": {"type": "json_object"},
                   "temperature": 0, "max_tokens": max_tokens, "stream": False}
        if effort:
            payload["reasoning_effort"] = effort
        return {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}, payload

    @staticmethod
    def chat_unpack(data: dict):
        """回复的骨架；形状不对时抛 KeyError / IndexError / TypeError（调用方记 bad_response_body 并重试）。"""
        return data["choices"][0], data.get("usage") or {}

    @staticmethod
    def chat_meter(unpacked, started, model: str, effort) -> dict:
        """写进 calls.jsonl 那一行的计量字段（含 usd），顺序和 v2.9b 相同。"""
        choice, usage = unpacked
        m = {"finish_reason": choice.get("finish_reason"),
             "prompt_tokens": usage.get("prompt_tokens", 0),
             "prompt_cache_hit_tokens": usage.get("prompt_cache_hit_tokens", 0),
             "prompt_cache_miss_tokens": usage.get("prompt_cache_miss_tokens", 0),
             "completion_tokens": usage.get("completion_tokens", 0),
             "usd": round(usd_cost(usage, started, model), 6)}
        if effort:   # 思考 token 计在 completion_tokens 里（已计价），这里单独记一下
            m["reasoning_tokens"] = (usage.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
        return m

    @staticmethod
    def chat_text(unpacked) -> str:
        return (unpacked[0].get("message") or {}).get("content") or ""

    @staticmethod
    def chat_problem(unpacked):
        """回复本身的问题（不解析 JSON 就先报）：None 或 (日志里的 error, 交给调用方的说明)。DeepSeek 只有截断。"""
        if unpacked[0].get("finish_reason") == "length":
            return "truncated", "reply was truncated (finish_reason=length)"
        return None

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None):
        """effort 不用：DeepSeek 搜索请求体保持 v2.9b 原样（不带 thinking 字段，见 PROVIDERS.md 第 8 节）。"""
        payload = {"model": model, "max_tokens": max_tokens,
                   "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}],
                   "messages": [{"role": "user", "content": prompt}]}
        return {"Content-Type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"}, payload

    search_unpack = staticmethod(anthropic_search_unpack)

    @staticmethod
    def search_continue(payload: dict, d: dict):
        return None

    @staticmethod
    def search_meter(unpacked: dict, started, model: str):
        """(写进 calls.jsonl 的 token 字段, token 成本 USD)。"""
        usage = unpacked["usage"]
        return ({"input_tokens": usage.get("input_tokens", 0),
                 "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
                 "output_tokens": usage.get("output_tokens", 0)},
                anthropic_usage_to_cost(usage, started, model))

    def balance_exhausted(self, status: int, body: bytes):
        """余额不足就返回一句说明，否则 None。官方错误码页：402 = Insufficient Balance（You have run out of balance）。"""
        return "HTTP 402 Insufficient Balance" if status == 402 else None


ANTHROPIC_VERSION = "2023-06-01"
CLAUDE_SEARCH_FEE_USD = 0.01   # Pricing 页 / Web search tool 页：$10 / 1,000 次搜索（出错的搜索不计费），另按 token 计


class StreamError(ValueError):
    """Claude 的流式回复不完整（没收到 message_stop），或流里来了 error 事件（如 overloaded_error）。
    是 ValueError：LLM.json_call 当作 bad_response_body 记下（error_type 记成 stream_error）并重试。"""

    def __init__(self, message: str, error_type=None):
        super().__init__(message)
        self.error_type = error_type


def parse_sse_message(raw: bytes) -> dict:
    """Messages API 的流式回复（server-sent events）拼回完整的 Message 对象，形状同非流式回复。
    官方 Streaming 页：message_start（content 为空的 Message）-> 每个块 content_block_start / 若干 content_block_delta /
    content_block_stop（index 对应最终 content 的位置）-> message_delta（stop_reason 等顶层变化；usage 是累计值）-> message_stop。
    中间可以有任意多个 ping；未知事件和未知 delta 类型按文档要求忽略。"""
    msg, blocks, partial, stopped = None, {}, {}, False
    for chunk in raw.decode("utf-8").replace("\r\n", "\n").split("\n\n"):
        data = [ln[5:].removeprefix(" ") for ln in chunk.split("\n") if ln.startswith("data:")]
        if not data:
            continue
        ev = json.loads("\n".join(data))
        t = ev.get("type")
        if msg is None and t in ("content_block_start", "content_block_delta", "content_block_stop", "message_delta"):
            raise StreamError(f"stream event {t!r} before message_start", "malformed_stream")
        if t == "message_start":
            msg = dict(ev["message"])
            msg["usage"] = dict(msg.get("usage") or {})
        elif t == "content_block_start":
            blocks[ev["index"]] = dict(ev["content_block"])
        elif t == "content_block_delta":
            b, dl = blocks[ev["index"]], ev["delta"]
            kind = dl.get("type")
            if kind == "text_delta":
                b["text"] = (b.get("text") or "") + dl["text"]
            elif kind == "thinking_delta":
                b["thinking"] = (b.get("thinking") or "") + dl["thinking"]
            elif kind == "signature_delta":
                b["signature"] = dl["signature"]
            elif kind == "input_json_delta":
                partial[ev["index"]] = partial.get(ev["index"], "") + dl["partial_json"]
            elif kind == "citations_delta":
                b["citations"] = list(b.get("citations") or []) + [dl["citation"]]
        elif t == "content_block_stop":
            if ev["index"] in partial:
                blocks[ev["index"]]["input"] = json.loads(partial.pop(ev["index"]) or "{}")
        elif t == "message_delta":
            msg.update(ev.get("delta") or {})
            msg["usage"].update({k: v for k, v in (ev.get("usage") or {}).items() if v is not None})
        elif t == "message_stop":
            stopped = True
        elif t == "error":
            etype = str((ev.get("error") or {}).get("type") or "unknown")
            raise StreamError(f"error event in the stream: {etype}", etype)
    if msg is None or not stopped:
        raise StreamError("stream ended before message_stop", "incomplete_stream")
    msg["content"] = [blocks[i] for i in sorted(blocks)]
    return msg


def claude_usage_cost(usage: dict, model: str) -> float:
    """Claude 的 usage 按 config.PRICES 计价。总 prompt = input_tokens + cache_read + cache_creation（官方 Messages API 文档）；
    cache 写入按 usage.cache_creation 里的 5 分钟 / 1 小时两档分开算，没有分档时按 5 分钟（默认 TTL）。
    Haiku 5.5：总 prompt 超过 100,000 token 的请求整次按高价（官方 Long context pricing）。inference_geo 为 "us" 时乘 1.1。"""
    p = price(model)
    inp = usage.get("input_tokens", 0) or 0
    read = usage.get("cache_read_input_tokens", 0) or 0
    split = usage.get("cache_creation") or {}
    w1h = split.get("ephemeral_1h_input_tokens", 0) or 0
    create = usage.get("cache_creation_input_tokens")
    create = (split.get("ephemeral_5m_input_tokens", 0) or 0) + w1h if create is None else create
    w5m = max(0, create - w1h)
    out = usage.get("output_tokens", 0) or 0
    hit, base, outp = p["peak"]
    r5, r1 = p["cache_write_5m"], p["cache_write_1h"]
    lc = p.get("long_context")
    if lc and inp + read + create > lc["threshold_tokens"]:
        (hit, base, outp), r5, r1 = lc["peak"], lc["cache_write_5m"], lc["cache_write_1h"]
    usd = (inp * base + read * hit + w5m * r5 + w1h * r1 + out * outp) / 1e6
    return usd * (CLAUDE_US_GEO_MULTIPLIER if usage.get("inference_geo") == "us" else 1.0)


def _claude_split_system(messages: list):
    """原生 Messages API 没有 system 角色的输入消息：开头的 system 消息拼成顶层 system 字段，其余照原样。
    内容为空的 assistant 消息不发（TextBlockParam.text 的 minLength 是 1）；前后两条 user 消息由 API 合并成一轮（官方文档：
    Consecutive user or assistant turns in your request will be combined into a single turn）。"""
    system, turns = [], []
    for m in messages:
        role, content = m["role"], m["content"]
        if role == "system":
            if turns:
                raise ValueError("a system message after the first user turn is not supported by this adapter")
            system.append(content)
        elif role == "assistant" and not str(content).strip():
            continue
        else:
            turns.append({"role": role, "content": content})
    return "\n\n".join(system), turns


class ClaudeAdapter:
    """Claude：原生 Messages API（POST https://api.anthropic.com/v1/messages），不用 OpenAI 兼容层（官方说它会忽略
    response_format / reasoning_effort、不适合生产）。JSON 调用：顶层 system、max_tokens、thinking + output_config.effort（按模型），
    不发 temperature / top_p / top_k（这几个模型上非默认值一律 400），不发 output_config.format（用户决定：不用 JSON schema），
    stream: true（官方：max_tokens 大的请求用流式，避免长时间空闲连接被断）。回复只拼 type == "text" 的块。
    搜索：同一个接口 + 服务端 web_search_20250305 工具（非流式），stop_reason 为 pause_turn 时把这次的 content 原样回传续上。
    设计说明和官方文档链接见 PROVIDERS.md。"""

    provider, label = "claude", "Claude"
    regions = {"global": {"chat": "https://api.anthropic.com/v1/messages",
                          "search": "https://api.anthropic.com/v1/messages",
                          "models": "https://api.anthropic.com/v1/models"}}
    default_region = "global"
    search_fee_usd = CLAUDE_SEARCH_FEE_USD
    # 除 401 / 403（key 被拒，不读）以外的错误都读 body：400 / 402 / 429 判断余额、额度（billing_error、credit balance、
    # spend limit、enforced_spend_limit_reached）；其余只把 error.type / message 记进日志（log_server_error）
    error_body_statuses = frozenset({400, 402, 404, 409, 413, 429, 500, 502, 503, 504, 529})
    balance_statuses = frozenset({400, 402, 429})
    retry_statuses = frozenset({429, 500, 502, 503, 504, 529})   # 529 overloaded_error：官方 Errors 页说退避重试
    honor_retry_after = True     # Rate limits 页：响应带 retry-after 时等那么多秒再重试
    log_server_error = True      # 读过的错误 body 只把 error.message 前 200 字记进日志（Anthropic 的错误消息不回显 key）
    # 流式：单次读最多等 600 秒（官方 SDK 的默认超时也是 10 分钟），整次最多 3600 秒
    chat_timeouts = {"sock_timeout": 600, "total_timeout": 3600}
    max_search_continuations = 2   # pause_turn 最多续两次（官方 Server tools 页：continue ... capping the number of continuations）
    balance_hint = "Check Plans & Billing and the spend limits in the Claude Console, then run again."

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

    @staticmethod
    def _headers(key: str) -> dict:
        """Authentication 页：直接发 HTTP 时 key 放 Authorization: Bearer（x-api-key 是 legacy，仍支持）；每个请求带 anthropic-version。"""
        return {"Content-Type": "application/json", "Authorization": f"Bearer {key}", "anthropic-version": ANTHROPIC_VERSION}

    @staticmethod
    def thinking_fields(model: str, effort) -> dict:
        """effort（ModelSpec.effort 的结果）-> thinking 和 output_config。开思考：adaptive + 同名 effort（low / medium / high）；
        关思考（只有能关的模型会走到这里）：按模型的关法（Haiku 5.5 disabled、Sonnet 5.5 between_tools），effort 写这个模型的
        默认值（官方：等于不写，写出来是为了换模型时不悄悄变；两种关法都只接受 high 及以下）。"""
        m = MODELS[model]
        if effort:
            return {"thinking": {"type": "adaptive"}, "output_config": {"effort": effort}}
        return {"thinking": dict(m["off"]), "output_config": {"effort": m["default_effort"]}}

    def chat_request(self, model: str, key: str, messages: list, *, max_tokens: int, effort):
        system, turns = _claude_split_system(messages)
        payload = {"model": model, "max_tokens": max_tokens}
        if system:
            payload["system"] = system
        payload["messages"] = turns
        payload.update(self.thinking_fields(model, effort))
        payload["stream"] = True
        return self._headers(key), payload

    chat_decode = staticmethod(parse_sse_message)

    @staticmethod
    def chat_unpack(data: dict) -> dict:
        if not isinstance(data["content"], list):
            raise TypeError("content is not a list")
        data["stop_reason"]   # noqa: B018  没有 stop_reason 的回复按形状不对处理（KeyError）
        return data

    @staticmethod
    def chat_meter(data: dict, started, model: str, effort) -> dict:
        u = data.get("usage") or {}
        inp, read = u.get("input_tokens", 0) or 0, u.get("cache_read_input_tokens", 0) or 0
        create, out = u.get("cache_creation_input_tokens", 0) or 0, u.get("output_tokens", 0) or 0
        m = {"finish_reason": data.get("stop_reason"), "prompt_tokens": inp + read + create, "input_tokens": inp,
             "cache_read_input_tokens": read, "cache_creation_input_tokens": create, "completion_tokens": out,
             "usd": round(claude_usage_cost(u, model), 6)}
        if data.get("stop_reason") == "refusal":
            m["stop_category"] = (data.get("stop_details") or {}).get("category")
        if effort:   # 思考 token 计在 output_tokens 里（已计价）；usage.output_tokens_details.thinking_tokens 是拆分
            m["reasoning_tokens"] = (u.get("output_tokens_details") or {}).get("thinking_tokens", 0)
        return m

    @staticmethod
    def chat_text(data: dict) -> str:
        return "".join(b.get("text") or "" for b in data["content"] if isinstance(b, dict) and b.get("type") == "text")

    @staticmethod
    def chat_problem(data: dict):
        """stop_reason（官方 Messages API）：max_tokens / model_context_window_exceeded = 输出没写完；refusal = 安全分类器拒答
        （HTTP 200，stop_details.category 给类别）；pause_turn = 长回合被暂停（JSON 调用不带工具，正常不会出现）。
        end_turn / stop_sequence 照常解析 JSON。"""
        stop = data.get("stop_reason")
        if stop in ("max_tokens", "model_context_window_exceeded"):
            return "truncated", f"reply was truncated (stop_reason={stop})"
        if stop == "refusal":
            cat = (data.get("stop_details") or {}).get("category")
            return "refusal", f"the model declined to answer (stop_reason=refusal, category={cat})"
        if stop == "pause_turn":
            return "paused", "reply was paused before it finished (stop_reason=pause_turn)"
        return None

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None):
        """web_search_20250305（基础版）：所有当前模型都能用、结果块直接在顶层 content 里、ZDR-eligible；带 dynamic filtering 的
        20260209 / 20260318 会在内部跑 code execution、嵌套块带 caller 字段，这里只要 URL，用不上（见 PROVIDERS.md）。"""
        payload = {"model": model, "max_tokens": max_tokens,
                   "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}],
                   "messages": [{"role": "user", "content": prompt}]}
        payload.update(self.thinking_fields(model, effort))
        return self._headers(key), payload

    search_unpack = staticmethod(anthropic_search_unpack)

    def search_continue(self, payload: dict, d: dict):
        """pause_turn：把这次回复的 content 原样作为 assistant 消息接在后面，工具不变，再发一次（官方 Server tools 页）。"""
        if d.get("stop_reason") != "pause_turn" or not isinstance(d.get("content"), list):
            return None
        return {**payload, "messages": list(payload["messages"]) + [{"role": "assistant", "content": d["content"]}]}

    @staticmethod
    def search_meter(unpacked: dict, started, model: str):
        u = unpacked["usage"]
        return ({"input_tokens": u.get("input_tokens", 0), "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
                 "cache_creation_input_tokens": u.get("cache_creation_input_tokens", 0), "output_tokens": u.get("output_tokens", 0)},
                claude_usage_cost(u, model))

    def balance_exhausted(self, status: int, body: bytes):
        """余额 / 额度用完就返回一句说明（不含服务端原文），否则 None。官方：402 billing_error；用户自设的 spend limit 到了是
        400 invalid_request_error，message 以 "You have reached your specified (workspace) API usage limits" 开头；用量档的
        月度上限是 429 且 error.details.error_code = enforced_spend_limit_reached（没有 retry-after，重试没用）；
        额度用完时的原文 "Your credit balance is too low to access the Anthropic API"（API credits 页；状态码文档没写，按原文认）。"""
        if status == 402:
            return "HTTP 402 billing_error"
        if status not in self.balance_statuses:
            return None
        try:
            err = json.loads(body).get("error") or {}
        except (ValueError, AttributeError):
            return None
        if not isinstance(err, dict):
            return None
        msg, etype = str(err.get("message") or ""), err.get("type")
        if msg.startswith("Your credit balance is too low"):
            return f"HTTP {status} credit balance too low"
        if status == 429 and (err.get("details") or {}).get("error_code") == "enforced_spend_limit_reached":
            return "HTTP 429 enforced_spend_limit_reached (the organization's monthly spend cap for its usage tier)"
        if status == 400 and msg.startswith(("You have reached your specified API usage limits",
                                             "You have reached your specified workspace API usage limits")):
            return "HTTP 400 spend limit reached (a limit set in the Claude Console)"
        if etype == "billing_error":
            return f"HTTP {status} billing_error"
        return None

    def key_check_request(self, region: str, key: str):
        """List Models：GET /v1/models（limit 1 到 1000，默认 20），不生成 token。"""
        return self.regions[region]["models"] + "?limit=1000", {"Authorization": f"Bearer {key}",
                                                                 "anthropic-version": ANTHROPIC_VERSION}

    @staticmethod
    def models_unpack(d: dict):
        return [str(x.get("id")) for x in d["data"] if isinstance(x, dict)], not d.get("has_more", False)


DEEPSEEK = DeepSeekAdapter()
CLAUDE = ClaudeAdapter()
ADAPTERS = {"deepseek": DEEPSEEK, "claude": CLAUDE}

# 网页上可选的模型（2026-10-21 按官方 Models & Pricing 页）。max_output = 官方写的最大输出 token 数；思考 token 计入输出上限，
# 开思考的调用多给的余量（config.THINKING_EXTRA_TOKENS）不超过它。efforts：网页档位 -> 这家 API 的取值；
# thinking_off = 这个模型能不能关掉思考（不能关的模型网页上不给 off，其余角色用最低一档）
MODELS = {
    # DeepSeek Thinking Mode 文档：reasoning_effort 只有 low / high / max，medium 按 high 处理；默认开思考（high），
    # 请求里写 thinking.type = disabled 就关掉
    "deepseek-flash": {"provider": "deepseek", "label": "DeepSeek Flash (DeepSeek-V4.1-Flash-1017)", "max_output": 384_000,
                       "thinking_off": True, "efforts": {"low": "low", "medium": "high", "high": "high"}},
    "deepseek-v4-pro": {"provider": "deepseek", "label": "DeepSeek V4 Pro (DeepSeek-V4-Pro-0813)", "max_output": 384_000,
                        "thinking_off": True, "efforts": {"low": "low", "medium": "high", "high": "high"}},
    # v2.10b Claude（官方 Models overview / Effort / Errors 页，2026-10-21）：四个模型都是 1M 上下文、最大输出 128K（同步请求）；
    # 思考是 adaptive，深度用 output_config.effort（low / medium / high / xhigh / max，这里只用前三档、同名）。
    # off = 关思考的写法：Haiku 5.5 {"type": "disabled"}、Sonnet 5.5 {"type": "between_tools"}（disabled 会 400），两种都只在
    # effort ≤ high 时接受；Opus 5.5 / Fable 5.1 的思考关不掉（disabled 在任何 effort 下都 400），网页不给 off。
    # default_effort = 官方默认档（Opus 5.5、Haiku 5.5 是 medium，其余 high），关思考的调用把它显式写上
    "claude-haiku-5-5": {"provider": "claude", "label": "Claude Haiku 5.5", "max_output": 128_000, "thinking_off": True,
                         "off": {"type": "disabled"}, "default_effort": "medium",
                         "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    "claude-sonnet-5-5": {"provider": "claude", "label": "Claude Sonnet 5.5", "max_output": 128_000, "thinking_off": True,
                          "off": {"type": "between_tools"}, "default_effort": "high",
                          "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    "claude-opus-5-5": {"provider": "claude", "label": "Claude Opus 5.5", "max_output": 128_000, "thinking_off": False,
                        "default_effort": "medium", "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    "claude-fable-5-1": {"provider": "claude", "label": "Claude Fable 5.1", "max_output": 128_000, "thinking_off": False,
                         "default_effort": "high", "efforts": {"low": "low", "medium": "medium", "high": "high"}},
}
PROVIDERS = {"deepseek": {"label": "DeepSeek", "models": ("deepseek-flash", "deepseek-v4-pro"),
                          "default_model": "deepseek-flash"},
             # 默认 Opus 5.5：官方推荐的默认模型（claude-api 参考，2026-10-21）。$2 上限下它的方向数和预扣见 PROVIDERS.md 第 9 节
             "claude": {"label": "Claude", "models": ("claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5",
                                                      "claude-fable-5-1"),
                        "default_model": "claude-opus-5-5"}}
DEFAULT_PROVIDER = "deepseek"


def adapter_for_model(model: str):
    m = MODELS.get(model)
    if m is None:
        if model in PRICES:   # 命令行用 TRIANGULATE_MODEL 指定、有价格但不在网页清单里的 DeepSeek 模型
            return ADAPTERS[PRICES[model].get("provider", "deepseek")]
        raise UnknownModel(f"model {model!r} has no price entry in config.PRICES; add one (with source and date) first")
    return ADAPTERS[m["provider"]]


def search_fee_usd(model: str) -> float:
    return adapter_for_model(model).search_fee_usd


def thinking_levels(model: str) -> tuple:
    """这个模型在网页上能选的思考档位。"""
    m = MODELS[model]
    return (("off",) if m["thinking_off"] else ()) + tuple(x for x in THINKING_UI if x in m["efforts"])


def clean_key(api_key) -> str:
    """去掉首尾空白（粘贴时常带换行）；只收可打印 ASCII、中间不能有空白，长度 8–512。
    否则 urllib 拼请求头时会抛带着整把 key 的 ValueError / UnicodeEncodeError（research：已实测），这里先拦下。消息里不带 key。"""
    if not isinstance(api_key, str):
        raise SpecError("API key must be a string")
    k = api_key.strip()
    if not KEY_MIN_CHARS <= len(k) <= KEY_MAX_CHARS:
        raise SpecError(f"API key must be {KEY_MIN_CHARS}-{KEY_MAX_CHARS} characters after trimming whitespace")
    if not all("!" <= c <= "~" for c in k):
        raise SpecError("API key may only contain printable ASCII characters without spaces")
    return k


class ModelSpec:
    """一次运行的模型设置 + 用户自己的 key。

    key 只放在这个对象里（LLM / Searcher 每次发请求时才取，不另存一份），运行结束时 drop_key() 一处清掉。
    repr、public()、错误消息都不带 key；不能 pickle / copy（避免被哪里顺手序列化）。不要把它放进题目 dict（q 会进
    save_run / score_one）或 LangGraph 的 state。"""

    __slots__ = ("provider", "model", "region", "thinking", "usd_cap", "_key")

    def __init__(self, provider: str, model: str, api_key: str, *, region: str | None = None, thinking: str = "off",
                 usd_cap: float = DEFAULT_USD_CAP):
        if provider not in PROVIDERS:
            raise SpecError(f"unknown provider {provider!r}; choose one of {', '.join(PROVIDERS)}")
        p, ad = PROVIDERS[provider], ADAPTERS[provider]
        if model not in p["models"] or MODELS.get(model, {}).get("provider") != provider:
            raise SpecError(f"model {model!r} is not offered for {ad.label}; choose one of {', '.join(p['models'])}")
        price(model)   # 没有价格的模型拒跑（UnknownModel），不按别的模型计价
        region = region or ad.default_region
        if region not in ad.regions:
            raise SpecError(f"unknown region {region!r} for {ad.label}; choose one of {', '.join(ad.regions)}")
        level = str(thinking).strip().lower()
        if level not in thinking_levels(model):
            raise SpecError(f"thinking level {thinking!r} is not available for {model}; choose one of "
                            f"{', '.join(thinking_levels(model))}")
        try:
            cap = float(usd_cap)
        except (TypeError, ValueError):
            raise SpecError("usd_cap must be a number") from None
        if not math.isfinite(cap) or cap <= 0:
            raise SpecError("usd_cap must be a positive number of US dollars")
        self.provider, self.model, self.region, self.thinking, self.usd_cap = provider, model, region, level, cap
        self._key = clean_key(api_key)

    # ---------- key ----------
    @property
    def key(self) -> str:
        if self._key is None:
            raise KeyDropped("the API key for this run was dropped when the run ended")
        return self._key

    @property
    def has_key(self) -> bool:
        return self._key is not None

    def drop_key(self):
        self._key = None

    def redact(self, text):
        """兜底：把文字里出现的 key 换成 ***（正常路径上 key 不会进任何文字）。"""
        k = self._key
        return text.replace(k, "***") if k and isinstance(text, str) else text

    def __repr__(self):
        return (f"ModelSpec(provider={self.provider!r}, model={self.model!r}, region={self.region!r}, "
                f"thinking={self.thinking!r}, usd_cap={self.usd_cap!r}, key=***)")

    __str__ = __repr__

    def __reduce_ex__(self, protocol):
        raise TypeError("ModelSpec holds an API key; it cannot be pickled or copied")

    # ---------- 模型 ----------
    @property
    def adapter(self):
        return ADAPTERS[self.provider]

    @property
    def max_output(self) -> int:
        return MODELS[self.model]["max_output"]

    def effort(self, role: str):
        """这个角色发给 API 的思考档位；None = 关思考。role 是 config.thinking_role(arm) 的结果。"""
        m = MODELS[self.model]
        if role in REASONING_ROLES and self.thinking != "off":
            return m["efforts"][self.thinking]
        if m["thinking_off"]:
            return None
        return m["efforts"][next(x for x in THINKING_UI if x in m["efforts"])]   # 关不掉思考的模型：最低一档

    def tokens_for(self, role: str, max_tokens: int):
        """(这个角色的思考档位或 None, 实际发出的 max_tokens)：开了思考的调用多给 THINKING_EXTRA_TOKENS（思考 token 计入输出上限），
        不超过模型的最大输出。LLM.json_call 和 Searcher.search 都用它。"""
        effort = self.effort(role)
        return effort, min(max_tokens + (THINKING_EXTRA_TOKENS if effort else 0), self.max_output)

    def thinking_by_role(self) -> dict:
        """开了思考的角色 -> API 档位（「*」= 其余角色，只有关不掉思考的模型才有）。记进 run settings。"""
        out = {r: e for r in REASONING_ROLES if (e := self.effort(r))}
        if (e := self.effort("*")) is not None:
            out["*"] = e
        return out

    def public(self) -> dict:
        """记进 state.json settings、可以给网页看的部分（不含 key）。"""
        return {"provider": self.provider, "model": self.model, "region": self.region, "thinking": self.thinking,
                "thinking_by_role": self.thinking_by_role(), "usd_cap": self.usd_cap, "byok": True}

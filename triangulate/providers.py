"""v2.10a：每次运行的模型设置（ModelSpec）和各家 API 的请求格式（adapter）。v2.10b 加 Claude（原生 Messages API）。
v2.10c 加 GPT（OpenAI：JSON 调用走 Chat Completions，搜索走 Responses API 的 web_search）。
v2.10d 加 Kimi（国际站 / 国内站两个区域；JSON 调用走 OpenAI 兼容的流式 Chat Completions，搜索是「生成查询词 + /v1/tools/search」）；
国内站按 CNY 价折算，计价用 ModelSpec.price_id（"kimi-k3@cn"）。
v2.10e 加 GLM（Z.ai 国际站 / 智谱开放平台国内站；JSON 调用走 OpenAI 兼容的非流式 Chat Completions，搜索同 Kimi：生成查询词 +
POST /web_search）；只收 Standard API Key（GLM_KEY_NOTE）。
v2.10h（用户 10-21：每个模型只用自家自带的联网搜索，没有就删掉这个模型）：删掉 Kimi K2.6；「生成查询词 + 另调搜索接口」那条路删掉。
K3 的搜索走 Responses API 的 web_search 工具（KimiAdapter.search_request），GLM 的搜索走 Chat Completions 的 web_search 工具
（GLMAdapter.search_request）；DeepSeek / Claude / GPT 的搜索不变。所有 adapter 的 search_request 多收一个 region（只有 GLM 用：两站的
搜索引擎不同）。PROVIDERS.md 第 16 节。
v2.10i（v2.10h 审查修正）：openai_search_unpack 在 status failed 时带出 error；Kimi / GLM 的搜索读超时 1200 秒、不重发
（search_timeout_s / search_resend_after_timeout）；GLM 的 search_reports_queries / search_tool_settings。PROVIDERS.md 第 17 节。

ModelSpec = provider、model、region、思考档位、这次运行的花费上限，加上用户自己的 key（只在内存里，见 ModelSpec 的说明）。
有 ModelSpec 的运行就是「自带 key」（BYOK）的运行：pipeline.Context(spec=...) 把它交给 AgentLLM、Searcher 和 Budget。
没有 ModelSpec（命令行、回测、基线）时一切照旧：DeepSeek + key 文件，请求体和 HEAD 逐字节相同（tests/test_providers.py）。

adapter 只管各家不同的三件事：建请求（URL、请求头、请求体）、解析回复（文字、截断、用量）、计价；重试、先查截断、
JSON 解析、日志、预算这些外层循环留在 llm.LLM.json_call 和 agent/search.Searcher.search，所有 provider 共用。
设计说明和各家官方文档的链接在仓库根目录的 PROVIDERS.md。
"""
import json
import math

from .config import (CLAUDE_US_GEO_MULTIPLIER, KIMI_WEB_SEARCH_FEE_ASSUMED_USD, MODEL, PRICES, THINKING_EXTRA_TOKENS, UnknownModel,
                     price, usd_cost)

THINKING_UI = ("off", "low", "medium", "high")   # 网页上的一个总档位
REASONING_ROLES = ("plan", "judge", "repair")    # 档位只作用于这三个角色（config.thinking_role 的取值）；其余角色能关就关
DEFAULT_USD_CAP = 3.00   # v2.13b：第一轮每个方向 3 个搜索 agent 以后，$2 只放得下 6 个方向（按假设单价的搜索费），$3 放得下 10 个
KEY_MIN_CHARS, KEY_MAX_CHARS = 8, 512
# v2.10f：key 只收这些字符（各家真实的 key：sk-... 的 base64url、GLM 的 hex.secret 都在里面）。不收 " \ & < > ' 等：
# 兜底的 redact 是在序列化之后的文字上找 key，JSON 转义（\" \\）和 HTML 转义（&amp; 等）会让它找不到
KEY_CHARS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._~+/=-")

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
    标题只在这里解析出来（v2.10b），Searcher 不往外传：分析角色只拿得到 URL（设计同 v2.9b）。
    v2.11c：每个结果块一组 groups（tool_use_id、原样的 URL、出错时的 error_code），query_ids 和 queries 一一对应（server_tool_use 的 id）；
    查询词和结果的配对在 Searcher 里做（pause_turn 续接时 use 和 result 可能在不同轮）。"""
    usage = d.get("usage") or {}
    n_req = int(((usage.get("server_tool_use") or {}).get("web_search_requests")) or 0)
    queries, query_ids, result_urls, result_titles, texts, groups, n_err = [], [], [], [], [], [], 0
    for b in d.get("content") or []:
        if b.get("type") == "server_tool_use":
            queries.append(str((b.get("input") or {}).get("query", ""))[:200])
            query_ids.append(b.get("id"))
        elif b.get("type") == "web_search_tool_result":
            c = b.get("content")
            g = {"tool_use_id": b.get("tool_use_id"), "urls": []}
            if isinstance(c, list):
                hits = [x for x in c if isinstance(x, dict) and x.get("url")]
                result_urls += [x.get("url") for x in hits]
                result_titles += [str(x.get("title") or "") for x in hits]
                g["urls"] = [x.get("url") for x in hits]
                # DeepSeek 把错误也放在 list 里：[{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]
                errs = [x for x in c if isinstance(x, dict) and x.get("type") == "web_search_tool_result_error"]
                n_err += len(errs)
            else:   # Claude 官方格式：出错时 content 是一个错误对象（HTTP 仍是 200）
                n_err += 1
                errs = [c]
            if errs:
                g["error"] = str((errs[0].get("error_code") if isinstance(errs[0], dict) else None) or "error")[:60]
            groups.append(g)
        elif b.get("type") == "text":
            texts.append(b.get("text") or "")
    return {"usage": usage, "n_req": n_req, "queries": queries, "result_urls": result_urls, "result_titles": result_titles,
            "texts": texts, "n_err": n_err, "stop": d.get("stop_reason"), "query_ids": query_ids, "groups": groups}


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
    # v2.10f：预扣把输入字符数换成 token 时每个 token 按几个字符算（pipeline.Budget.llm_reserve）。DeepSeek 照旧 2（命令行的预扣不变）；
    # 别家的 tokenizer 没测过，按 1 个字符 1 个 token（审查发现：按 2 算时中文页面会低估）
    reserve_chars_per_token = 2

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

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None, region=None):
        """effort、region 不用：DeepSeek 搜索请求体保持 v2.9b 原样（不带 thinking 字段）。命令行和自带 key 的运行都走这里：
        用户 10-21 定「保持原本一样即可」，v2.10g 撤回了 v2.10f 给自带 key 的运行加的 thinking disabled（PROVIDERS.md 第 8、14.6 节）。"""
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
    # v2.10f：403 也读，只取 error.type（permission_error 等）显示，不取 message（llm.forbidden_info）
    error_body_statuses = frozenset({400, 402, 403, 404, 409, 413, 429, 500, 502, 503, 504, 529})
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

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None, region=None):
        """region 不用（只有一个区域）。web_search_20250305（基础版）：所有当前模型都能用、结果块直接在顶层 content 里、ZDR-eligible；带 dynamic filtering 的
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


OPENAI_SEARCH_FEE_USD = 0.01   # Pricing 页 Tools：Web search $10.00 / 1k calls（只有 search 动作计次，web search 指南），另按 token 计
# Error codes 页：这些 429 是额度 / 余额 / 用量上限，重试没用（Retrying billing, spend, or quota errors won't restore API access）；
# error.type 也可能是 insufficient_quota
OPENAI_BALANCE_CODES = {
    "credit_balance_exhausted": "credit_balance_exhausted (no prepaid credits left)",
    "organization_spend_limit_exceeded": "organization_spend_limit_exceeded (the organization's spend limit)",
    "project_spend_limit_exceeded": "project_spend_limit_exceeded (the project's spend limit)",
    "organization_usage_limit_exceeded": "organization_usage_limit_exceeded (the OpenAI-assigned monthly usage limit)",
    "insufficient_quota": "insufficient_quota",
}


def openai_usage_cost(usage: dict, model: str) -> float:
    """OpenAI 的 usage 按 config.PRICES 计价；Chat Completions（prompt_tokens / prompt_tokens_details）和 Responses
    （input_tokens / input_tokens_details）两种字段名都认。Prompt caching 页的算法：普通 input = input - cached - cache_write，
    cached 按 cached input 价，写入按 30 分钟 / 12 小时写入价（Responses 的 cache_write_tokens_details 有分档；Chat Completions
    只有 30 分钟一档），output（含 reasoning token）按 output 价。input 超过 272K token 的请求整次按 long context 价。"""
    p = price(model)
    if "input_tokens" in usage or "input_tokens_details" in usage:
        inp, det, out = usage.get("input_tokens", 0) or 0, usage.get("input_tokens_details") or {}, usage.get("output_tokens", 0) or 0
    else:
        inp, det, out = usage.get("prompt_tokens", 0) or 0, usage.get("prompt_tokens_details") or {}, usage.get("completion_tokens", 0) or 0
    read, write = det.get("cached_tokens", 0) or 0, det.get("cache_write_tokens", 0) or 0
    split = det.get("cache_write_tokens_details") or {}
    w12 = split.get("ttl_12h_tokens", 0) or 0
    w30 = max(0, write - w12)
    tier = p
    lc = p.get("long_context")
    if lc and inp > lc["threshold_tokens"]:
        tier = lc
    hit, base, outp = tier["peak"]
    plain = max(0, inp - read - write)
    return (plain * base + read * hit + w30 * tier["cache_write_30m"] + w12 * tier["cache_write_12h"] + out * outp) / 1e6


def _openai_turns(messages: list) -> list:
    """Chat Completions 的消息：system 角色改成 developer（API 参考：With o1 models and newer, use developer messages for this
    purpose instead；GPT-6 都是推理模型）。内容不变。"""
    return [{"role": "developer" if m["role"] == "system" else m["role"], "content": m["content"]} for m in messages]


def openai_search_unpack(d: dict) -> dict:
    """Responses API 的回复（output 项数组）里取：查询词、URL（和标题）、文字、搜索次数、出错的搜索数。
    web_search_call.action：search（queries / query；include 了 web_search_call.action.sources 时带 sources[]，只有 url）、
    open_page（url）、find_in_page。只有 search 动作计次收费（web search 指南：Search actions incur a tool call cost）。
    message 项的 output_text：文字 + url_citation 注解（url、title）。URL 顺序：引用的 -> sources -> open_page；标题有引用的，
    v2.10h 起还有 sources 里带的（Kimi K3 的 Responses API：sources 是 {type, url, title}；OpenAI 的只有 url，标题照旧是空字符串），
    只在这里解析（Searcher 不往外传）。v2.10i：status 是 failed 时多一个 error（{code, message}，原文；Searcher 先 redact 再记、再往外报）。
    v2.11c：每个 web_search_call 一组 groups：queries（这次调用的查询词列表）、urls（search 的 sources 原样；open_page 是打开的那个
    url；find_in_page 没有）、调用 status failed 时 error "failed"。message 里引用的 URL 不属于哪一次调用，不进 groups。"""
    usage = d.get("usage") or {}
    cited, cited_titles, sources, source_titles, opened, queries, texts, groups = [], [], [], [], [], [], [], []
    n_req = n_err = 0
    for item in d.get("output") or []:
        if not isinstance(item, dict):
            continue
        t = item.get("type")
        if t == "web_search_call":
            a = item.get("action") or {}
            g = {"queries": [], "urls": []}
            if item.get("status") == "failed":
                n_err += 1
                g["error"] = "failed"
            kind = a.get("type")
            if kind in ("search", None):   # 没有 action 的调用也按一次搜索计费（保守）
                n_req += 1
                qs = a.get("queries") or ([a["query"]] if a.get("query") else [])
                queries += [str(q)[:200] for q in qs]
                hits = [s for s in a.get("sources") or [] if isinstance(s, dict) and s.get("url")]
                sources += [s["url"] for s in hits]
                source_titles += [str(s.get("title") or "") for s in hits]
                g.update(queries=[str(q)[:200] for q in qs], urls=[s["url"] for s in hits])
            elif kind == "open_page" and a.get("url"):
                opened.append(a["url"])
                g["urls"] = [a["url"]]
            groups.append(g)
        elif t == "message":
            for c in item.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "output_text":
                    texts.append(c.get("text") or "")
                    for ann in c.get("annotations") or []:
                        if isinstance(ann, dict) and ann.get("type") == "url_citation" and ann.get("url"):
                            cited.append(ann["url"])
                            cited_titles.append(str(ann.get("title") or ""))
    result_urls = cited + sources + opened
    result_titles = cited_titles + source_titles + [""] * len(opened)
    status = d.get("status")
    reason = (d.get("incomplete_details") or {}).get("reason")
    out = {"usage": usage, "n_req": n_req, "queries": queries, "result_urls": result_urls, "result_titles": result_titles,
           "texts": texts, "n_err": n_err, "stop": f"{status}:{reason}" if reason else status, "groups": groups}
    if status == "failed":   # v2.10i：HTTP 200 但 status failed：error 是 {code, message}（Kimi Responses 页；OpenAI 同形状）
        err = d.get("error") if isinstance(d.get("error"), dict) else {}
        out["error"] = {"code": "" if err.get("code") is None else str(err["code"]),
                        "message": "" if err.get("message") is None else str(err["message"])}
    return out


class OpenAIAdapter:
    """GPT（OpenAI 官方 API，api.openai.com）。JSON 调用走 Chat Completions（POST /v1/chat/completions）：response_format
    json_object（用户决定：不用 JSON schema）、reasoning_effort 按模型和角色、max_completion_tokens（含 reasoning token；
    max_tokens 已 deprecated）、reasoning_effort 不是 none 时不发 temperature（GPT-6 迁移指南）、store: false。
    搜索走 Responses API（POST /v1/responses，hosted web_search 工具只在 Responses 里有）：tool_choice required、
    max_tool_calls、include web_search_call.action.sources、store: false。设计说明和官方文档链接见 PROVIDERS.md。"""

    provider, label = "gpt", "OpenAI"
    regions = {"global": {"chat": "https://api.openai.com/v1/chat/completions",
                          "search": "https://api.openai.com/v1/responses",
                          "models": "https://api.openai.com/v1/models"}}
    default_region = "global"
    search_fee_usd = OPENAI_SEARCH_FEE_USD
    # 除 401 / 403（key 被拒，不读：401 的 message 会回显打了码的 key 片段）以外的错误都读 body：429 判断余额 / 额度
    # （error.code），其余只把 error.type / code / message 记进日志
    # v2.10f：403（Error codes 页：Country, region, or territory not supported）也读，只取 error.type / code 显示，不取 message
    # （401 的 message 才回显打了码的 key；401 照旧不读）
    error_body_statuses = frozenset({400, 403, 404, 409, 413, 422, 429, 500, 502, 503, 504})
    balance_statuses = frozenset({429})
    retry_statuses = frozenset({429, 500, 502, 503, 504})   # Error codes / Rate limits 页：429 限流、slow_down，503 server_is_overloaded
    honor_retry_after = True     # Rate limits 页：Retry-After 是重试前最少要等的秒数
    log_server_error = True
    # 非流式：生成完才回 body，思考档高的长回复单次读可能要等很久（没实测）。单次读最多等 1200 秒，整次 1800 秒
    chat_timeouts = {"sock_timeout": 1200, "total_timeout": 1800}
    max_search_continuations = 0   # Responses 没有 pause_turn；status = incomplete 就照原样用已有的结果
    balance_hint = "Add credits or raise the spend limits in the OpenAI Platform settings (Billing / Limits), then run again."

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

    @staticmethod
    def _headers(key: str) -> dict:
        return {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}

    @staticmethod
    def api_effort(model: str, effort) -> str:
        """ModelSpec.effort 的结果 -> reasoning effort。None（关思考，只有能关的模型会走到这里）-> "none"：省略时 Luna 默认按
        medium 思考（Reasoning 指南），要关必须显式写 none。"""
        if effort:
            return effort
        off = MODELS[model].get("off_effort")
        if off is None:
            raise ValueError(f"{model} cannot turn reasoning off")
        return off

    def chat_request(self, model: str, key: str, messages: list, *, max_tokens: int, effort):
        eff = self.api_effort(model, effort)
        payload = {"model": model, "messages": _openai_turns(messages), "reasoning_effort": eff,
                   "response_format": {"type": "json_object"}}
        if eff == "none":   # GPT-6 迁移指南：只有 effort 是 none 时才能带 temperature（DeepSeek 同样发 0）
            payload["temperature"] = 0
        payload["max_completion_tokens"] = max_tokens
        payload["store"] = False
        return self._headers(key), payload

    chat_decode = staticmethod(json.loads)

    @staticmethod
    def chat_unpack(data: dict):
        choice = data["choices"][0]
        if not isinstance(choice.get("message"), dict):
            raise TypeError("choices[0].message is not an object")
        return choice, data.get("usage") or {}

    @staticmethod
    def chat_meter(unpacked, started, model: str, effort) -> dict:
        choice, u = unpacked
        det = u.get("prompt_tokens_details") or {}
        m = {"finish_reason": choice.get("finish_reason"), "prompt_tokens": u.get("prompt_tokens", 0),
             "cached_tokens": det.get("cached_tokens", 0) or 0, "cache_write_tokens": det.get("cache_write_tokens", 0) or 0,
             "completion_tokens": u.get("completion_tokens", 0), "usd": round(openai_usage_cost(u, model), 6)}
        if effort:   # reasoning token 计在 completion_tokens 里（已计价），这里单独记一下
            m["reasoning_tokens"] = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
        if choice["message"].get("refusal"):
            m["refusal"] = True   # 拒答的文字不记（日志不记回复内容）
        return m

    @staticmethod
    def chat_text(unpacked) -> str:
        return unpacked[0]["message"].get("content") or ""

    @staticmethod
    def chat_problem(unpacked):
        """message.refusal 有值 = 安全拒答（没有 JSON）；finish_reason：length = 撞到 max_completion_tokens，content_filter =
        内容被过滤（JSON 可能不完整）。Structured Outputs 指南的 JSON mode 一节要求先处理这几种情况。"""
        choice = unpacked[0]
        if choice["message"].get("refusal"):
            return "refusal", "the model declined to answer (message.refusal)"
        fr = choice.get("finish_reason")
        if fr == "length":
            return "truncated", "reply was truncated (finish_reason=length)"
        if fr == "content_filter":
            return "content_filter", "reply was stopped by the content filter (finish_reason=content_filter)"
        return None

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None, region=None):
        """region 不用（只有 global）。Responses API + hosted web_search（新集成用 {"type": "web_search"}）。tool_choice required：web search 指南
        Limitations「With tool_choice: "auto", search is optional. Use tool_choice: "required" ... when search must run」。
        max_tool_calls = max_uses（所有内置工具调用合计，含 open_page / find_in_page）。sources 要 include 才返回。
        store: false（默认 true，保存至少 30 天）。"""
        payload = {"model": model, "input": prompt, "tools": [{"type": "web_search"}], "tool_choice": "required",
                   "max_tool_calls": max_uses, "include": ["web_search_call.action.sources"],
                   "reasoning": {"effort": self.api_effort(model, effort)}, "max_output_tokens": max_tokens, "store": False}
        return self._headers(key), payload

    search_unpack = staticmethod(openai_search_unpack)

    @staticmethod
    def search_continue(payload: dict, d: dict):
        return None

    @staticmethod
    def search_meter(unpacked: dict, started, model: str):
        u = unpacked["usage"]
        det, odet = u.get("input_tokens_details") or {}, u.get("output_tokens_details") or {}
        return ({"input_tokens": u.get("input_tokens", 0), "cached_tokens": det.get("cached_tokens", 0) or 0,
                 "cache_write_tokens": det.get("cache_write_tokens", 0) or 0, "output_tokens": u.get("output_tokens", 0),
                 "reasoning_tokens": odet.get("reasoning_tokens", 0) or 0},
                openai_usage_cost(u, model))

    def balance_exhausted(self, status: int, body: bytes):
        """余额 / 额度用完就返回一句说明（不含服务端原文），否则 None。Error codes 页：429 + error.code 是
        credit_balance_exhausted / organization_spend_limit_exceeded / project_spend_limit_exceeded /
        organization_usage_limit_exceeded；error.type 可能仍是 insufficient_quota。普通限流（rate_limit_exceeded、slow_down）不算。"""
        if status not in self.balance_statuses:
            return None
        try:
            err = json.loads(body).get("error") or {}
        except (ValueError, AttributeError):
            return None
        if not isinstance(err, dict):
            return None
        code, etype = err.get("code"), err.get("type")
        if code in OPENAI_BALANCE_CODES:
            return f"HTTP {status} {OPENAI_BALANCE_CODES[code]}"
        if etype == "insufficient_quota":
            return f"HTTP {status} insufficient_quota" + (f" ({code})" if code else "")
        return None

    def key_check_request(self, region: str, key: str):
        """List models：GET /v1/models（不生成 token），返回 {"object": "list", "data": [{"id", ...}]}，没有分页。"""
        return self.regions[region]["models"], {"Authorization": f"Bearer {key}"}

    @staticmethod
    def models_unpack(d: dict):
        return [str(x.get("id")) for x in d["data"] if isinstance(x, dict)], True


# ---------- v2.10d Kimi ----------

def parse_chat_sse(raw: bytes) -> dict:
    """OpenAI 兼容的流式回复（Kimi Chat Completions，stream: true）拼回非流式回复的形状。官方 Chat API 页：每个事件一行
    "data: <chunk JSON>"，内容在 choices[0].delta.content 里累加，finish_reason 只在最后一个 choice 上非空；
    stream_options.include_usage 时 "data: [DONE]" 之前多一个 usage chunk（choices 为空数组）。delta.reasoning_content
    （思考内容）不拼、不记。没收到 [DONE] 或流里来了 error 对象：StreamError（LLM.json_call 记 bad_response_body 并重试）。
    收到 [DONE] 却没有 usage（文档：流被打断时可能收不到）：照常返回，usage_missing = True（不重试，免得重复计费）。"""
    content, finish, usage, done = [], None, None, False
    for chunk in raw.decode("utf-8").replace("\r\n", "\n").split("\n\n"):
        data = [ln[5:].removeprefix(" ") for ln in chunk.split("\n") if ln.startswith("data:")]
        if not data:
            continue
        payload = "\n".join(data).strip()
        if payload == "[DONE]":
            done = True
            break
        ev = json.loads(payload)
        if not isinstance(ev, dict):
            raise StreamError("stream chunk is not an object", "malformed_stream")
        if isinstance(ev.get("error"), dict):
            etype = str(ev["error"].get("type") or "unknown")
            raise StreamError(f"error object in the stream: {etype}", etype)
        for ch in ev.get("choices") or []:
            if not isinstance(ch, dict) or ch.get("index", 0) != 0:
                continue
            piece = (ch.get("delta") or {}).get("content")
            if piece:
                content.append(piece)
            if ch.get("finish_reason") is not None:
                finish = ch["finish_reason"]
        if isinstance(ev.get("usage"), dict):
            usage = ev["usage"]
    if not done:
        raise StreamError("stream ended before data: [DONE]", "incomplete_stream")
    return {"choices": [{"index": 0, "message": {"role": "assistant", "content": "".join(content)}, "finish_reason": finish}],
            "usage": usage or {}, "usage_missing": usage is None}


def kimi_usage_cost(usage: dict, price_id: str) -> float:
    """Kimi 的 usage 按 config.PRICES[price_id]（国内站已折成 USD）计价。Chat API 页：prompt_tokens 是全部输入；
    prompt_tokens_details 里 cached_tokens（命中）、cache_write_tokens（写入）和未缓存的部分互斥、相加等于 prompt_tokens。
    命中按 cache hit 价；写入按 5 分钟写入价（本项目不写 prompt_cache_options，官方默认 5 分钟档；没有单列写入价的模型按 miss 价）；
    其余按 miss 价；completion_tokens（含思考）按 output 价。没有 prompt_tokens_details 时用顶层的 cached_tokens。"""
    p = price(price_id)
    hit, miss, outp = p["peak"]
    inp = usage.get("prompt_tokens", 0) or 0
    det = usage.get("prompt_tokens_details")
    det = det if isinstance(det, dict) else {"cached_tokens": usage.get("cached_tokens", 0)}
    read, write = det.get("cached_tokens", 0) or 0, det.get("cache_write_tokens", 0) or 0
    plain = max(0, inp - read - write)
    out = usage.get("completion_tokens", 0) or 0
    return (plain * miss + read * hit + write * p.get("cache_write_5m", miss) + out * outp) / 1e6


def kimi_responses_cost(usage: dict, price_id: str) -> float:
    """v2.10h：K3 搜索（Responses API）的 usage 计价，算法同 kimi_usage_cost。Responses 页 Usage fields：input_tokens 是全部输入
    （含服务端放进上下文的搜索结果），input_tokens_details 的 cached_tokens（命中）、cache_write_tokens（写入）和未缓存的部分互斥、
    相加等于 input_tokens；output_tokens 含思考 token。"""
    det = usage.get("input_tokens_details") if isinstance(usage.get("input_tokens_details"), dict) else {}
    return kimi_usage_cost({"prompt_tokens": usage.get("input_tokens", 0) or 0,
                            "prompt_tokens_details": {"cached_tokens": det.get("cached_tokens", 0) or 0,
                                                      "cache_write_tokens": det.get("cache_write_tokens", 0) or 0},
                            "completion_tokens": usage.get("output_tokens", 0) or 0}, price_id)


def _kimi_turns(messages: list) -> list:
    """Chat API：messages 里每条的 content must not be empty。内容为空的 assistant 消息（AgentLLM.ask 重问时，回复被思考用完、
    正文为空的情况）不发；其余原样（Kimi 收 system 角色）。"""
    return [{"role": m["role"], "content": m["content"]} for m in messages
            if not (m["role"] == "assistant" and not str(m["content"]).strip())]


KIMI_BALANCE_TYPES = {   # Common Error Codes 页：429 + 这个 error.type = 余额不足 / 账户欠费或停用 / token 额度不足（充值）
    "exceeded_current_quota_error": "exceeded_current_quota_error (balance insufficient, account in arrears or disabled, "
                                    "or token quota used up)",
}


class KimiAdapter:
    """Kimi（Moonshot AI 开放平台）。国际站 api.moonshot.ai（USD）和国内站 api.moonshot.cn（CNY）两个区域，key 不能混用（混用 401）。
    v2.10h 起只有 K3（K2.6 删掉：没有可用的自带搜索，用户 10-21）。
    JSON 调用走 OpenAI 兼容的 Chat Completions（POST /v1/chat/completions）：response_format json_object（用户决定：不用 JSON
    schema）、max_completion_tokens（max_tokens 已 deprecated；思考 token 计入）、顶层 reasoning_effort（K3 永远在想，不发 thinking）；
    temperature / top_p / n / 两个 penalty 都是固定值，不发；stream: true + stream_options.include_usage（错误码页：非流式请求 900 秒
    没回就 504，要用流式）。
    搜索（v2.10h）：Responses API（POST /v1/responses）自带的 web_search 工具（search_request）：服务端先按输入决定要不要搜，搜了就把
    结果放进模型的上下文，output 最前面是 web_search_call（include web_search_call.action.sources 才带结果的 url / title），模型再按
    结果回答。设计说明和官方文档链接见 PROVIDERS.md 第 11、16 节。"""

    provider, label = "kimi", "Kimi"
    regions = {"global": {"chat": "https://api.moonshot.ai/v1/chat/completions",
                          "search": "https://api.moonshot.ai/v1/responses",
                          "models": "https://api.moonshot.ai/v1/models"},
               "cn": {"chat": "https://api.moonshot.cn/v1/chat/completions",
                      "search": "https://api.moonshot.cn/v1/responses",
                      "models": "https://api.moonshot.cn/v1/models"}}
    region_labels = {"global": "International (platform.kimi.ai, billed in USD)",
                     "cn": "China (platform.kimi.com, billed in CNY)"}
    default_region = "global"
    # Responses 里 web_search 的单价两站都没列：按 web_search_call 的个数、每次这个假设的美元数记（config.KIMI_WEB_SEARCH_FEE_ASSUMED_USD；
    # 价格表里两站的 search_fee_usd 也是它）
    search_fee_usd = KIMI_WEB_SEARCH_FEE_ASSUMED_USD
    # 除 401 / 403（key 被拒，不读）以外的错误都读 body：429 判断余额（error.type），其余只把 error.type / message 记进日志
    error_body_statuses = frozenset({400, 404, 408, 413, 422, 429, 500, 502, 503, 504})
    balance_statuses = frozenset({429})
    # 429 engine_overloaded_error / rate_limit_reached_error、500、502、503、504 重试
    retry_statuses = frozenset({429, 500, 502, 503, 504})
    honor_retry_after = True          # 错误码页：engine_overloaded_error 按 Retry-After 等
    log_server_error = True
    chat_timeouts = {"sock_timeout": 600, "total_timeout": 3600}   # 流式：单次读最多 600 秒，整次 3600 秒（没实测）
    # v2.10i：搜索是非流式的 Responses 请求（整段思考生成完才回 body）。Common Error Codes 页：非流式请求 900 秒没回服务端给 504；
    # 单次读等 1200 秒（比 900 秒长：先等到服务端的 504，而不是我们先放弃一个服务端可能照样计费的请求）。读超时以后不重发，
    # 这次请求按预扣记账（Searcher._request）。时长没实测
    search_timeout_s = 1200
    search_resend_after_timeout = False
    max_search_continuations = 0      # Responses 没有 pause_turn；status = incomplete 就照原样用已有的结果
    balance_hint = ("Top up the Kimi account on the platform where the key was created (platform.kimi.ai or platform.kimi.com), "
                    "then run again.")

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

    @staticmethod
    def _headers(key: str) -> dict:
        return {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}

    @staticmethod
    def thinking_fields(model: str, effort) -> dict:
        """K3（v2.10h 起唯一的模型）：只有顶层 reasoning_effort（low / high / max，省略时 max；不发 thinking：文档 should not）。"""
        if not effort:
            raise ValueError(f"{model} always thinks; it needs a reasoning_effort")
        return {"reasoning_effort": effort}

    def chat_request(self, model: str, key: str, messages: list, *, max_tokens: int, effort):
        payload = {"model": model, "messages": _kimi_turns(messages)}
        payload.update(self.thinking_fields(model, effort))
        payload.update({"response_format": {"type": "json_object"}, "max_completion_tokens": max_tokens, "stream": True,
                        "stream_options": {"include_usage": True}})
        return self._headers(key), payload

    chat_decode = staticmethod(parse_chat_sse)

    @staticmethod
    def chat_unpack(data: dict):
        choice = data["choices"][0]
        if not isinstance(choice.get("message"), dict):
            raise TypeError("choices[0].message is not an object")
        return choice, data.get("usage") or {}, bool(data.get("usage_missing"))

    @staticmethod
    def chat_meter(unpacked, started, model: str, effort) -> dict:
        """model 是计价用的 id（ModelSpec.price_id：国内站是 "kimi-k3@cn"）。"""
        choice, u, missing = unpacked
        det = u.get("prompt_tokens_details") if isinstance(u.get("prompt_tokens_details"), dict) else {}
        m = {"finish_reason": choice.get("finish_reason"), "prompt_tokens": u.get("prompt_tokens", 0),
             "cached_tokens": det.get("cached_tokens", u.get("cached_tokens", 0)) or 0,
             "cache_write_tokens": det.get("cache_write_tokens", 0) or 0,
             "completion_tokens": u.get("completion_tokens", 0), "usd": round(kimi_usage_cost(u, model), 6)}
        if "reasoning_tokens" in (u.get("completion_tokens_details") or {}):   # Chat API 的 usage 没写这个字段；有才记
            m["reasoning_tokens"] = u["completion_tokens_details"]["reasoning_tokens"]
        if missing:
            m["usage_missing"] = True
        return m

    @staticmethod
    def chat_text(unpacked) -> str:
        return unpacked[0]["message"].get("content") or ""

    @staticmethod
    def chat_problem(unpacked):
        """finish_reason（Chat API）：stop 照常解析 JSON；length = 撞到 max_completion_tokens（思考 + 正文共用）；
        其余（不带工具时不该出现的 tool_calls、流里没给 finish_reason）照原样报，不解析。内容审核是 HTTP 400 content_filter。"""
        fr = unpacked[0].get("finish_reason")
        if fr == "length":
            return "truncated", "reply was truncated (finish_reason=length)"
        if fr != "stop":
            return "unexpected_finish", f"reply ended with finish_reason={fr}"
        return None

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None, region=None):
        """v2.10h：Responses API（POST /v1/responses，两站的 Responses 页）自带的 web_search 工具。body：model；input（字符串 = 一条
        user 消息：搜索 prompt 原样）；tools 只有一个 {"type": "web_search"}（每个请求最多一个；search_context_size / blocked_domains 会报
        invalid_request_error，不发）；include web_search_call.action.sources（不写就不返回结果的 url / title）；reasoning.effort（省略时
        默认 max，最贵，所以显式写；搜索不是 plan / judge / repair：low）；max_output_tokens（默认 131072）。
        不发：tool_choice（只有 auto，就是默认；没法强制搜）、max_tool_calls（没有这个参数）、stream（默认 false：回复是文档写明的
        ResponsesResponse 形状）、store（回复里 Always false）、prompt_cache_options（省略 = 默认 5 分钟档）、instructions。
        max_uses、region 不用：搜不搜由服务端按输入定（Responses 页：the server first decides from the input whether a search is needed）。"""
        if not effort:
            raise ValueError(f"{model} always thinks; it needs a reasoning effort")
        payload = {"model": model, "input": prompt, "tools": [{"type": "web_search"}],
                   "include": ["web_search_call.action.sources"], "reasoning": {"effort": effort}, "max_output_tokens": max_tokens}
        return self._headers(key), payload

    # output[]：web_search_call（只有服务端决定要搜时才有，在最前面）的 action：type search、query（实际用的查询词）、sources
    # [{type: url, url, title}]；reasoning；message 的 output_text。形状同 OpenAI Responses（openai_search_unpack 也取 sources 的 title）。
    # 计次 = web_search_call 的个数（usage 里没有搜索次数）
    search_unpack = staticmethod(openai_search_unpack)

    @staticmethod
    def search_continue(payload: dict, d: dict):
        return None

    @staticmethod
    def search_meter(unpacked: dict, started, model: str):
        """(写进 calls.jsonl 的 token 字段, token 成本 USD)。model 是计价 id（国内站 "kimi-k3@cn"）。usage 是 null（文档允许）时这里算出 0，
        v2.10i 起 Searcher 在自带 key 的运行里改按这次搜索预扣的 token 部分记账（usd_basis "reserve (usage missing)"，同 llm.py）。"""
        u = unpacked["usage"]
        det = u.get("input_tokens_details") if isinstance(u.get("input_tokens_details"), dict) else {}
        odet = u.get("output_tokens_details") if isinstance(u.get("output_tokens_details"), dict) else {}
        return ({"input_tokens": u.get("input_tokens", 0), "cached_tokens": det.get("cached_tokens", 0) or 0,
                 "cache_write_tokens": det.get("cache_write_tokens", 0) or 0, "output_tokens": u.get("output_tokens", 0),
                 "reasoning_tokens": odet.get("reasoning_tokens", 0) or 0},
                kimi_responses_cost(u, model))

    def balance_exhausted(self, status: int, body: bytes):
        """余额不足就返回一句说明（不含服务端原文），否则 None。错误码页：429 + error.type = exceeded_current_quota_error
        （余额不足或账户停用 / token 额度不足）；同为 429 的 engine_overloaded_error、rate_limit_reached_error 是限流，重试。
        v2.10h：搜索走的 Responses 接口只写了 429「Rate limited or out of quota」、错误形状 {"error": {message, type, code}}，没单列
        type（未核实它用不用同一个 type）；按同一规则认。"""
        if status not in self.balance_statuses:
            return None
        try:
            err = json.loads(body).get("error") or {}
        except (ValueError, AttributeError):
            return None
        if not isinstance(err, dict):
            return None
        etype = err.get("type")
        return f"HTTP {status} {KIMI_BALANCE_TYPES[etype]}" if etype in KIMI_BALANCE_TYPES else None

    def key_check_request(self, region: str, key: str):
        """List Models：GET /v1/models（Bearer），返回 {"object": "list", "data": [{"id", "context_length", ...}]}，没有分页。"""
        return self.regions[region]["models"], {"Authorization": f"Bearer {key}"}

    @staticmethod
    def models_unpack(d: dict):
        return [str(x.get("id")) for x in d["data"] if isinstance(x, dict)], True


# ---------- v2.10e GLM ----------

def glm_error(raw: bytes):
    """GLM 的错误 body -> (code, message) 或 None。错误码页（两站）的形状是 {"error": {"code": "1113", "message": ...}}（code 是字符串；
    2026-10-21 实测 401 也是这样），API 参考里的 Error schema 却写成没有外层 error、code 是 integer 的 {"code": 1113, "message": ...}：
    两种都认，code 统一成字符串。"""
    try:
        d = json.loads(raw)
    except (ValueError, TypeError):
        return None
    if not isinstance(d, dict):
        return None
    err = d["error"] if isinstance(d.get("error"), dict) else d
    code, msg = err.get("code"), err.get("message")
    if code is None and msg is None:
        return None
    return (None if code is None else str(code).strip()), ("" if msg is None else str(msg))


def glm_usage_cost(usage: dict, price_id: str) -> float:
    """GLM 的 usage 按 config.PRICES[price_id]（国内站已折成 USD）计价。Chat Completion API：prompt_tokens 是全部输入，
    prompt_tokens_details.cached_tokens 是其中命中缓存的部分（按 cached input 价），其余按 input 价；completion_tokens 按 output 价
    （思考 token 是否计在 completion_tokens 里文档没写，usage 里也没有 reasoning_tokens：按 completion_tokens 计价，未核实）。
    缓存是隐式的，没有写入费；缓存存储限时免费，不计。"""
    hit, miss, outp = price(price_id)["peak"]
    inp = usage.get("prompt_tokens", 0) or 0
    det = usage.get("prompt_tokens_details") if isinstance(usage.get("prompt_tokens_details"), dict) else {}
    read = det.get("cached_tokens", 0) or 0
    out = usage.get("completion_tokens", 0) or 0
    return (max(0, inp - read) * miss + read * hit + out * outp) / 1e6


# 错误码页（两站同表）：429 里这些码重试没用，整次运行停下（BalanceExhausted）。1113 是余额不足；GLM_LIMIT_CODES 是用量上限，
# GLM_PLAN_CODES 是套餐过期 / 不含这个模型 / 套餐类型不对的 key（要到给出的重置时间、续订或换 key 才能恢复），和 OpenAI 的 spend / usage
# limit 一样停下，但说明的开头不写成 insufficient balance（stop_prefix，v2.10f）。1302（限流）、1305（过载）、1313（公平使用策略下的
# 频率限制，v2.10f 起按限流重试：调研只把 1113 列为余额不足）重试
GLM_BALANCE_CODES = {
    "1113": "code 1113 (insufficient balance or no resource package)",
}
GLM_LIMIT_CODES = {
    "1308": "code 1308 (usage limit reached; it resets at the time given by the server)",
    "1310": "code 1310 (weekly / monthly usage limit exhausted)",
    "1316": "code 1316 (5-hour usage limit reached and the balance is too low for extra usage)",
    "1317": "code 1317 (7-day usage limit reached and the balance is too low for extra usage)",
    "1318": "code 1318 (5-hour usage limit reached; extra usage blocked by a monthly spend limit)",
    "1319": "code 1319 (7-day usage limit reached; extra usage blocked by a monthly spend limit)",
    "1320": "code 1320 (5-hour usage limit reached; extra usage blocked by the enterprise monthly spend limit)",
    "1321": "code 1321 (7-day usage limit reached; extra usage blocked by the enterprise monthly spend limit)",
}
_GLM_PLAN_KEY = "this looks like a GLM Coding Plan / package key; this app needs a Standard API Key"
GLM_PLAN_CODES = {
    "1309": f"code 1309 (the GLM Coding Plan has expired; {_GLM_PLAN_KEY})",
    "1311": f"code 1311 (the subscription plan does not include this model; {_GLM_PLAN_KEY})",
    "1314": f"code 1314 (the enterprise package has expired; {_GLM_PLAN_KEY})",
    "1315": f"code 1315 (the key is limited to enterprise coding package scenarios; {_GLM_PLAN_KEY})",
}
GLM_KEY_NOTE = ("Use a Standard API Key: on Z.ai, API Keys -> Standard API Key (https://z.ai/manage-apikey/apikey-list); on "
                "bigmodel.cn, the standard API Keys page (https://bigmodel.cn/usercenter/proj-mgmt/apikeys). GLM Coding Plan keys "
                "(Personal / Team Coding Plan) are not allowed: since 2026-10-16 they are a separate key type, and the usage policy "
                "limits them to officially supported coding tools (violations can lead to rate limiting or a frozen account). "
                "This app only calls the general endpoint /api/paas/v4, never the Coding Plan endpoint /api/coding/paas/v4.")


def glm_search_unpack(d: dict) -> dict:
    """v2.10h：Chat Completions + 自带 web_search 工具的回复（两站 API 参考 ChatCompletionResponse）：choices[0].message.content 是模型的
    文字（模型挑的 URL 从这里取），顶层 web_search[] 是这次搜索的结果（search_result: true 才返回；每项 title、link、content、media、icon、
    refer、publish_date），取 link 和 title（标题不出 Searcher）。回复里没有查询词（由服务端定）。计次：文档按实际调用次数计费，回复里没有
    搜索次数，也没写意图识别判定不搜时收不收：每个 HTTP 200 的回复按一次记（保守）。形状不对的部分按空的处理（不抛，Searcher 照常记一行）。
    v2.11c：groups 只有一组，query 是 None（回复里没有查询词）。"""
    usage = d.get("usage") if isinstance(d.get("usage"), dict) else {}
    choices = d.get("choices") if isinstance(d.get("choices"), list) else []
    ch = choices[0] if choices and isinstance(choices[0], dict) else {}
    msg = ch.get("message") if isinstance(ch.get("message"), dict) else {}
    text = msg.get("content")
    found = d.get("web_search") if isinstance(d.get("web_search"), list) else []
    hits = [x for x in found if isinstance(x, dict) and x.get("link")]
    return {"usage": usage, "n_req": 1, "queries": [], "result_urls": [str(x["link"]) for x in hits],
            "result_titles": [str(x.get("title") or "") for x in hits], "texts": [text] if isinstance(text, str) else [],
            "n_err": 0, "stop": ch.get("finish_reason"), "groups": [{"query": None, "urls": [str(x["link"]) for x in hits]}]}


class GLMAdapter:
    """GLM（Z.ai 国际站 api.z.ai / 智谱开放平台国内站 open.bigmodel.cn，用户选区域；两站的账户、key、价格、搜索引擎都不同）。
    只用通用端点 /api/paas/v4（不用 Coding Plan 端点），只收 Standard API Key（网页提示见 GLM_KEY_NOTE）。
    JSON 调用：OpenAI 兼容的 Chat Completions（POST {base}/chat/completions），非流式；response_format json_object（用户决定：不用 JSON
    schema；GLM 也没有）、max_tokens（1–131072）、思考按模型族（5.3：thinking enabled + reasoning_effort low / high / max，关不掉；
    5.2：disabled，或 enabled + reasoning_effort；4.7 系列：enabled / disabled，没有 reasoning_effort）；temperature / top_p / do_sample
    不发（官方默认 temperature 1.0、top_p 0.95 就是推荐值）。回复按 finish_reason 分：stop 解析，length / model_context_window_exceeded
    报截断，sensitive 报内容审核，其余照原样报。错误 body 的 code 可能是字符串或整数、可能没有外层 error（glm_error）。
    搜索（v2.10h，用户 10-21：只用自带的搜索）：同一个 Chat Completions 接口带上自带的 web_search 工具（search_request；国际站引擎
    search_pro_jina，国内站 search_std），服务端先对输入做搜索意图识别、搜一次，把结果放进上下文再生成；结果的 link 在回复顶层的
    web_search[] 里。设计说明和官方文档链接见 PROVIDERS.md 第 12、16 节。"""

    provider, label = "glm", "GLM"
    # v2.10h：搜索也发到 chat/completions（带 web_search 工具），不再用独立的 /web_search 接口
    regions = {"global": {"chat": "https://api.z.ai/api/paas/v4/chat/completions",
                          "search": "https://api.z.ai/api/paas/v4/chat/completions",
                          "models": "https://api.z.ai/api/paas/v4/models"},
               "cn": {"chat": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
                      "search": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
                      "models": "https://open.bigmodel.cn/api/paas/v4/models"}}
    region_labels = {"global": "International (Z.ai, z.ai, billed in USD)",
                     "cn": "China (Zhipu BigModel open platform, bigmodel.cn, billed in CNY)"}
    key_note = GLM_KEY_NOTE
    key_pages = {"global": "https://z.ai/manage-apikey/apikey-list", "cn": "https://bigmodel.cn/usercenter/proj-mgmt/apikeys"}
    default_region = "global"
    search_fee_usd = 0.01             # 国际站；按区域的价格在 config.PRICES 的 search_fee_usd（providers.search_fee_usd）
    # v2.10h：web_search 工具的 search_engine（必填）。国际站 Chat Completion API 参考的 enum 只有 search_pro_jina（Web Search 指南的
    # 「Web Search in Chat」示例写的是 search-prime，和参考页矛盾，按参考页）；国内站用 search_std（基础版，¥0.01 / 次）
    search_engines = {"global": "search_pro_jina", "cn": "search_std"}
    # 除 401 / 403（key 被拒，不读）以外的错误都读 body：429 判断余额 / 用量上限（code），其余只把 code / message 记进日志
    error_body_statuses = frozenset({400, 404, 413, 429, 500, 502, 503, 504})
    balance_statuses = frozenset({429})
    retry_statuses = frozenset({429, 500, 502, 503, 504})   # 429 的 1302 限流、1305 过载（余额 / 上限的码先被 balance_exhausted 拦下）
    honor_retry_after = True          # 文档没写 Retry-After；服务端给了就照它等（最多 60 秒），没给照常退避
    log_server_error = True
    # 非流式：生成完才回 body（文档没写服务端的超时）。单次读最多等 1200 秒，整次 1800 秒（同 OpenAI，没实测）
    chat_timeouts = {"sock_timeout": 1200, "total_timeout": 1800}
    # v2.10i：搜索也是非流式的 Chat Completions（GLM-5.3 开着思考），单次读同 JSON 调用（1200 秒）；读超时以后不重发，这次请求按预扣
    # 记账（Searcher._request）
    search_timeout_s = chat_timeouts["sock_timeout"]
    search_resend_after_timeout = False
    # v2.10i：回复里没有查询词（服务端自己定）：账本写「not reported by the provider」，不写「(none)」（Searcher 返回 queries_reported False）
    search_reports_queries = False
    max_search_continuations = 0
    balance_hint = ("Top up the GLM account (or check its limits) on the platform where the key was created "
                    "(z.ai/manage-apikey/billing or bigmodel.cn), make sure it is a Standard API Key, then run again.")

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

    @staticmethod
    def _headers(key: str) -> dict:
        """两站的 HTTP API 页：Content-Type: application/json，Authorization: Bearer <API Key>。"""
        return {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}

    @staticmethod
    def thinking_fields(model: str, effort) -> dict:
        """MODELS[model]["thinking_param"]：
        "reasoning_effort"（5.3 / 5.2）：开思考 = thinking enabled + reasoning_effort（官方示例两个都写）；关（只有 5.2 能关）= thinking
        disabled，不发 reasoning_effort（文档：只在 enabled 时生效）。5.3 传 disabled 会报错，这里防御性地拒绝。
        "thinking"（4.7 系列）：thinking enabled（强制思考）/ disabled；不支持 reasoning_effort（只有 5.2 及以上有）。"""
        m = MODELS[model]
        if m["thinking_param"] == "reasoning_effort":
            if effort:
                return {"thinking": {"type": "enabled"}, "reasoning_effort": effort}
            if not m["thinking_off"]:
                raise ValueError(f"{model} always thinks; it needs a reasoning_effort")
            return {"thinking": {"type": "disabled"}}
        return {"thinking": {"type": "enabled" if effort else "disabled"}}

    def chat_request(self, model: str, key: str, messages: list, *, max_tokens: int, effort):
        """body 依次是 model、messages（原样：GLM 收 system 角色）、thinking（和 reasoning_effort）、response_format、max_tokens、stream。"""
        payload = {"model": model, "messages": [{"role": m["role"], "content": m["content"]} for m in messages]}
        payload.update(self.thinking_fields(model, effort))
        payload.update({"response_format": {"type": "json_object"}, "max_tokens": max_tokens, "stream": False})
        return self._headers(key), payload

    chat_decode = staticmethod(json.loads)

    @staticmethod
    def chat_unpack(data: dict):
        choice = data["choices"][0]
        if not isinstance(choice.get("message"), dict):
            raise TypeError("choices[0].message is not an object")
        return choice, data.get("usage") or {}

    @staticmethod
    def chat_meter(unpacked, started, model: str, effort) -> dict:
        """model 是计价用的 id（ModelSpec.price_id：国内站是 "glm-5.3@cn"）。"""
        choice, u = unpacked
        det = u.get("prompt_tokens_details") if isinstance(u.get("prompt_tokens_details"), dict) else {}
        m = {"finish_reason": choice.get("finish_reason"), "prompt_tokens": u.get("prompt_tokens", 0),
             "cached_tokens": det.get("cached_tokens", 0) or 0, "completion_tokens": u.get("completion_tokens", 0),
             "usd": round(glm_usage_cost(u, model), 6)}
        if "reasoning_tokens" in (u.get("completion_tokens_details") or {}):   # API 参考的 usage 没有这个字段；有才记
            m["reasoning_tokens"] = u["completion_tokens_details"]["reasoning_tokens"]
        return m

    @staticmethod
    def chat_text(unpacked) -> str:
        """只取 message.content（最终答案）；思考内容在 message.reasoning_content，不拼、不记。"""
        return unpacked[0]["message"].get("content") or ""

    @staticmethod
    def chat_problem(unpacked):
        """finish_reason（API 参考：stop / tool_calls / length / sensitive / model_context_window_exceeded / network_error）：
        stop 照常解析 JSON；length = 撞到 max_tokens、model_context_window_exceeded = 超出上下文窗口：输出没写完，报截断；
        sensitive = 被内容安全审核拦截；其余（不带工具时的 tool_calls、network_error = 推理异常、没给 finish_reason）照原样报，不解析。"""
        fr = unpacked[0].get("finish_reason")
        if fr in ("length", "model_context_window_exceeded"):
            return "truncated", f"reply was truncated (finish_reason={fr})"
        if fr == "sensitive":
            return "sensitive", "reply was stopped by content moderation (finish_reason=sensitive)"
        if fr != "stop":
            return "unexpected_finish", f"reply ended with finish_reason={fr}"
        return None

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int, effort=None, region=None):
        """v2.10h：Chat Completions（POST {base}/chat/completions）自带的 web_search 工具（两站 API 参考的 WebSearchToolSchema；联网搜索
        指南「对话中的网络搜索」/「Web Search in Chat」）。body 依次是 model、messages（一条 user：搜索 prompt 原样）、thinking（和
        reasoning_effort；规则同 JSON 调用：搜索不是 plan / judge / repair，5.2 / 4.7-FlashX 关思考，5.3 用 low）、tools、max_tokens、stream。
        web_search 里只写：enable true（默认 false）、search_engine（必填，按区域）、search_result true（默认 false：不写就不返回结果的
        link / title）。不写 search_query（那是「强制按这个查询词搜」，等于由我们写查询词）、search_intent / require_search（用默认：服务端
        先做搜索意图识别）、count / search_domain_filter / search_recency_filter / content_size / search_prompt（用默认）。不发
        response_format（搜索角色回的是 URL 列表，不是 JSON）、tool_choice（只有 auto，而且只对 function 有效）。max_uses 不用：一次请求
        搜一次，由服务端定。"""
        region = region or self.default_region
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        payload.update(self.thinking_fields(model, effort))
        payload.update({"tools": [{"type": "web_search", "web_search": {"enable": True, "search_engine": self.search_engines[region],
                                                                       "search_result": True}}],
                        "max_tokens": max_tokens, "stream": False})
        return self._headers(key), payload

    def search_tool_settings(self, region: str) -> dict:
        """v2.10i：state.json 的 settings.search_tool（run.run_settings 记，事后查得出这次运行用的搜索端点和引擎）。国际站的
        search_pro_jina 按 API 参考写，没用真 key 测过（PROVIDERS.md 第 17 节），所以另记 search_engine_tested False。不含 key。"""
        return {"endpoint": self.search_url(region), "tool": "web_search", "search_engine": self.search_engines[region],
                "search_engine_tested": False}

    search_unpack = staticmethod(glm_search_unpack)

    @staticmethod
    def search_continue(payload: dict, d: dict):
        return None

    @staticmethod
    def search_meter(unpacked: dict, started, model: str):
        """(写进 calls.jsonl 的 token 字段, token 成本 USD)：usage 同 JSON 调用（prompt_tokens 含服务端放进上下文的搜索结果）。
        model 是计价 id（国内站 "glm-5.3@cn"）。没有 usage 时这里算出 0，v2.10i 起 Searcher 在自带 key 的运行里改按预扣记账。"""
        u = unpacked["usage"]
        det = u.get("prompt_tokens_details") if isinstance(u.get("prompt_tokens_details"), dict) else {}
        return ({"prompt_tokens": u.get("prompt_tokens", 0), "cached_tokens": det.get("cached_tokens", 0) or 0,
                 "completion_tokens": u.get("completion_tokens", 0)}, glm_usage_cost(u, model))

    @staticmethod
    def parse_error(raw: bytes) -> dict:
        """llm.server_error 用：读过的错误 body 只取 code 和 message（GLM 的错误没有 type）。v2.10f：message 不在这里截断：
        llm.server_error 先 redact、去掉像 key 的片段，再截到 200 字（先截断的话，截在 key 中间的半截认不出来）。"""
        got = glm_error(raw)
        if got is None:
            return {}
        code, msg = got
        out = {"server_error": msg}
        if code:
            out["server_error_code"] = code[:60]
        return out

    def balance_exhausted(self, status: int, body: bytes):
        """余额 / 用量上限 / 套餐 key 的问题就返回一句说明（不含服务端原文），否则 None。错误码页：HTTP 429 + 业务码 1113 = 余额不足或
        没有资源包；1308–1321（1313 除外）是用量上限和套餐的问题（GLM_LIMIT_CODES / GLM_PLAN_CODES）。同为 429 的 1302（限流）、
        1305（过载）、1313（公平使用策略的频率限制，v2.10f）重试。"""
        if status not in self.balance_statuses:
            return None
        got = glm_error(body)
        if got is None or got[0] is None:
            return None
        code = got[0]
        why = GLM_BALANCE_CODES.get(code) or GLM_LIMIT_CODES.get(code) or GLM_PLAN_CODES.get(code)
        return f"HTTP {status} {why}" if why else None

    @staticmethod
    def stop_prefix(why: str) -> str:
        """v2.10f：停下整次运行的说明的开头（llm.balance_message）：只有 1113 是余额不足；用量上限、套餐 key 的码分开写。"""
        code = why.split("code ", 1)[1].split(" ", 1)[0] if "code " in why else None
        if code in GLM_LIMIT_CODES:
            return "usage limit reached"
        if code in GLM_PLAN_CODES:
            return "key or plan not accepted"
        return "insufficient balance"

    def key_check_request(self, region: str, key: str):
        """GET {base}/models（Bearer）。两站的文档都没有列这个接口，但它存在：10-20 / 10-21 不带 key、带假 key 实测都是 401
        （probes/glm_key_probe.py）。有效 key 的回复是什么形状没核实（手上没有 key）。"""
        return self.regions[region]["models"], {"Authorization": f"Bearer {key}"}

    @staticmethod
    def models_unpack(d):
        """接口没有文档：回复是 OpenAI 的形状（data 列表，每项有 id）就取出模型 id，否则空列表。第二项 None = 不知道列表全不全
        （llm.check_key 据此不说「模型不在列表里」）。HTTP 200 本身已经说明 key 被接受。"""
        data = d.get("data") if isinstance(d, dict) else None
        ids = [str(x.get("id")) for x in data if isinstance(x, dict) and x.get("id")] if isinstance(data, list) else []
        return ids, None


DEEPSEEK = DeepSeekAdapter()
CLAUDE = ClaudeAdapter()
OPENAI = OpenAIAdapter()
KIMI = KimiAdapter()
GLM = GLMAdapter()
ADAPTERS = {"deepseek": DEEPSEEK, "claude": CLAUDE, "gpt": OPENAI, "kimi": KIMI, "glm": GLM}

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
    # v2.10c GPT（官方模型页 / Reasoning 指南 / GPT-6 迁移指南，2026-10-21）：三个模型都是 1,050,000 上下文、最大输出 128,000。
    # 思考深度：Chat Completions 用 reasoning_effort、Responses 用 reasoning.effort，取值同名（这里只用 low / medium / high）。
    # off_effort = 关思考时发的值：只有 Luna 支持 none（省略时默认 medium，所以要显式写）；6.1 Sol 和 Astra 不支持 none
    # （发了 HTTP 400），网页不给 off，其余角色用最低一档 low
    "gpt-6-luna": {"provider": "gpt", "label": "GPT-6 Luna", "max_output": 128_000, "thinking_off": True, "off_effort": "none",
                   "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    "gpt-6.1-sol": {"provider": "gpt", "label": "GPT-6.1 Sol", "max_output": 128_000, "thinking_off": False,
                    "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    "gpt-6-astra": {"provider": "gpt", "label": "GPT-6 Astra", "max_output": 128_000, "thinking_off": False,
                    "efforts": {"low": "low", "medium": "medium", "high": "high"}},
    # v2.10d Kimi（官方 Model Parameter Reference / Reasoning Effort / Chat API，2026-10-21）。
    # K3：1M 上下文，max_completion_tokens 最大 1,048,576（输入 + 输出不能超过上下文）；永远在想，顶层 reasoning_effort 只有
    # low / high / max（默认 max）。网页档位按调研的映射：low -> low、medium -> high、high -> max；不给 off，其余角色 low。
    # v2.10h：K2.6 删掉（用户 10-21：只用自带的搜索；Responses API 只支持 K3，Chat Completions 的 $web_search 已在 10-20 下线）
    "kimi-k3": {"provider": "kimi", "label": "Kimi K3", "max_output": 1_048_576, "context": 1_048_576, "thinking_off": False,
                "thinking_depth": True, "efforts": {"low": "low", "medium": "high", "high": "max"}},
    # v2.10e GLM（Z.ai / 智谱官方 Chat Completion API、Deep Thinking、Core Parameters、模型页，2026-10-21）：max_tokens 最大 131,072。
    # GLM-5.3：1M 上下文；永远在想（thinking 只能 enabled），reasoning_effort 只有 low / high / max（默认 max）。网页档位同 Kimi K3：
    # low -> low、medium -> high、high -> max；不给 off，其余角色 low。
    # GLM-5.2：1M 上下文；能关（thinking disabled）；reasoning_effort 收 7 个值，但 low / medium 都映射成 high、xhigh 映射成 max，实际只有
    # 关 / high / max 三档：网页 low、medium 都发 high（发映射后的值，日志里看得到实际档位），high 发 max。
    # GLM-4.7-FlashX：200K 上下文；thinking enabled（4.7 系列开了就强制思考）/ disabled，没有 reasoning_effort（只有 5.2 及以上有）：
    # low / medium / high 都是「开」（thinking_depth = False，网页上合并显示）。模型 id 取自国内站 API 参考的 model enum；国际站 API 参考的
    # enum 里没有它（国际站价格页 Other Pricing 有 GLM-4.7-FlashX），国际站是否收这个 id 没核实
    "glm-5.3": {"provider": "glm", "label": "GLM-5.3", "max_output": 131_072, "context": 1_000_000, "thinking_off": False,
                "thinking_param": "reasoning_effort", "thinking_depth": True,
                "efforts": {"low": "low", "medium": "high", "high": "max"}},
    "glm-5.2": {"provider": "glm", "label": "GLM-5.2", "max_output": 131_072, "context": 1_000_000, "thinking_off": True,
                "thinking_param": "reasoning_effort", "thinking_depth": True,
                "efforts": {"low": "high", "medium": "high", "high": "max"}},
    "glm-4.7-flashx": {"provider": "glm", "label": "GLM-4.7-FlashX", "max_output": 131_072, "context": 200_000,
                       "thinking_off": True, "thinking_param": "thinking", "thinking_depth": False,
                       "efforts": {"low": "enabled", "medium": "enabled", "high": "enabled"}},
}
PROVIDERS = {"deepseek": {"label": "DeepSeek", "models": ("deepseek-flash", "deepseek-v4-pro"),
                          "default_model": "deepseek-flash"},
             # v2.10f：默认改成 Sonnet 5.5（审查发现：Opus 5.5 + 默认 $2 上限放不下一次最坏情况的运行，网页会拒跑）。和 GPT / Kimi 选
             # 默认模型的口径一致：默认上限下能跑完、能关思考。官方推荐的默认模型是 Opus 5.5（claude-api 参考），要用它把上限调高
             "claude": {"label": "Claude", "models": ("claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5",
                                                      "claude-fable-5-1"),
                        "default_model": "claude-sonnet-5-5"},
             # 默认 Luna：$2 上限下只有它能跑满 10 个方向（6.1 Sol 约 5 个、Astra 1 个，PROVIDERS.md 第 10 节），也是三个里
             # 唯一能关思考的（ModelSpec 的默认档位是 off）。官方「新项目从 Astra 开始」，要改随时说
             "gpt": {"label": "GPT (OpenAI)", "models": ("gpt-6-luna", "gpt-6.1-sol", "gpt-6-astra"),
                     "default_model": "gpt-6-luna"},
             # v2.10h：只有 K3（K2.6 删掉：没有自带的搜索，用户 10-21）。K3 要先充值才解锁；默认 $2 上限放不下一次最小运行，
             # 网页会拒跑并给出最小上限（PROVIDERS.md 第 16 节）
             "kimi": {"label": "Kimi (Moonshot AI)", "models": ("kimi-k3",), "default_model": "kimi-k3"},
             # 默认 GLM-5.2：国际站 API 参考里有这个 id、能关思考（ModelSpec 的默认档位是 off），$2 上限下 9 个方向。最便宜的 4.7-FlashX
             # （10 个方向）国际站 id 没核实；5.3（官方默认的旗舰）关不掉思考。PROVIDERS.md 第 12 节。key_note：网页上要显示的 key 说明
             "glm": {"label": "GLM (Z.ai / Zhipu)", "models": ("glm-4.7-flashx", "glm-5.2", "glm-5.3"), "default_model": "glm-5.2",
                     "key_note": GLM_KEY_NOTE}}
DEFAULT_PROVIDER = "deepseek"


def adapter_for_model(model: str):
    m = MODELS.get(model)
    if m is None:
        if model in PRICES:   # 命令行用 TRIANGULATE_MODEL 指定、有价格但不在网页清单里的 DeepSeek 模型
            return ADAPTERS[PRICES[model].get("provider", "deepseek")]
        raise UnknownModel(f"model {model!r} has no price entry in config.PRICES; add one (with source and date) first")
    return ADAPTERS[m["provider"]]


def stop_prefix(ad, why: str) -> str:
    """v2.10f：余额 / 额度问题停下整次运行时说明的开头。adapter 有 stop_prefix（GLM：用量上限、套餐 key 不算余额不足）就用它，
    否则 "insufficient balance"（DeepSeek、Claude、OpenAI、Kimi 的文字不变）。"""
    f = getattr(ad, "stop_prefix", None)
    return f(why) if f is not None else "insufficient balance"


def reserve_chars_per_token(model: str) -> float:
    """v2.10f：预扣时输入的「每个 token 几个字符」：按模型所属 provider 的 adapter（DeepSeek 2，其余 1）。model 是计价 id。"""
    return getattr(adapter_for_model(model), "reserve_chars_per_token", 1)


def search_fee_usd(model: str) -> float:
    """每次搜索的费用（USD）。model 是计价 id；v2.10d：价格表里按区域写了 search_fee_usd 的（Kimi、GLM）用它，否则用这家 adapter 的。"""
    p = PRICES.get(model) or {}
    return p["search_fee_usd"] if "search_fee_usd" in p else adapter_for_model(model).search_fee_usd


def price_id(model: str, region: str, ad) -> str:
    """计价 id：这家的默认区域用模型名本身（DeepSeek / Claude / GPT 只有一个区域，和以前相同），其余区域 "模型@区域"。"""
    return model if region == ad.default_region else f"{model}@{region}"


def thinking_levels(model: str) -> tuple:
    """这个模型在网页上能选的思考档位。"""
    m = MODELS[model]
    return (("off",) if m["thinking_off"] else ()) + tuple(x for x in THINKING_UI if x in m["efforts"])


def effort_for(model: str, level: str, role: str):
    """网页档位 level 下，这个角色发给 API 的思考档位；None = 关思考。档位只作用于 REASONING_ROLES；其余角色能关就关，
    关不掉思考的模型用最低一档。ModelSpec.effort 和网页的花费估计（web/catalog.py，没有 key 时）都用它。"""
    m = MODELS[model]
    if role in REASONING_ROLES and level != "off":
        return m["efforts"][level]
    if m["thinking_off"]:
        return None
    return m["efforts"][next(x for x in THINKING_UI if x in m["efforts"])]   # 关不掉思考的模型：最低一档


def tokens_for_model(model: str, level: str, role: str, max_tokens: int):
    """(这个角色的思考档位或 None, 实际发出的 max_tokens)：开了思考的调用多给 THINKING_EXTRA_TOKENS（思考 token 计入输出上限），
    不超过模型的最大输出。"""
    effort = effort_for(model, level, role)
    return effort, min(max_tokens + (THINKING_EXTRA_TOKENS if effort else 0), MODELS[model]["max_output"])


def _redact_deep(obj, key: str):
    if isinstance(obj, str):
        return obj.replace(key, "***")
    if isinstance(obj, dict):
        return {_redact_deep(k, key): _redact_deep(v, key) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_redact_deep(x, key) for x in obj]
    return obj


def clean_key(api_key) -> str:
    """去掉首尾空白（粘贴时常带换行）；长度 8–512，中间不能有空白。
    否则 urllib 拼请求头时会抛带着整把 key 的 ValueError / UnicodeEncodeError（research：已实测），这里先拦下。消息里不带 key。
    v2.10f：只收 KEY_CHARS（字母、数字和 . _ ~ + / = -），不再收所有可打印 ASCII（见 KEY_CHARS 的说明）。"""
    if not isinstance(api_key, str):
        raise SpecError("API key must be a string")
    k = api_key.strip()
    if not KEY_MIN_CHARS <= len(k) <= KEY_MAX_CHARS:
        raise SpecError(f"API key must be {KEY_MIN_CHARS}-{KEY_MAX_CHARS} characters after trimming whitespace")
    if not all(c in KEY_CHARS for c in k):
        raise SpecError("API key may only contain letters, digits and . _ ~ + / = - (no spaces or other characters)")
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
        region = region or ad.default_region
        if region not in ad.regions:
            raise SpecError(f"unknown region {region!r} for {ad.label}; choose one of {', '.join(ad.regions)}")
        price(price_id(model, region, ad))   # 没有价格的模型（或区域）拒跑（UnknownModel），不按别的模型计价
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

    def redact_obj(self, obj):
        """web-v0.9：redact 的深层版：dict / list / tuple 里所有字符串（含 dict 的键）里的 key 换成 ***，返回新的对象（不改原对象）。
        key 已经清掉时原样返回。网页的运行状态在返回前、清 key 之前都过一遍。"""
        k = self._key
        return _redact_deep(obj, k) if k else obj

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
    def price_id(self) -> str:
        """v2.10d：计价用的 id（config.PRICES 的键）：默认区域是模型名本身，别的区域是 "模型@区域"（Kimi 国内站 "kimi-k3@cn"，
        按 CNY 价折算）。请求里发的仍是 model。LLM / Searcher 的计量和 Budget 都用它。"""
        return price_id(self.model, self.region, self.adapter)

    @property
    def max_output(self) -> int:
        return MODELS[self.model]["max_output"]

    def effort(self, role: str):
        """这个角色发给 API 的思考档位；None = 关思考。role 是 config.thinking_role(arm) 的结果。"""
        return effort_for(self.model, self.thinking, role)

    def tokens_for(self, role: str, max_tokens: int):
        """(这个角色的思考档位或 None, 实际发出的 max_tokens)：见 tokens_for_model。LLM.json_call 和 Searcher.search 都用它。"""
        return tokens_for_model(self.model, self.thinking, role, max_tokens)

    def thinking_by_role(self) -> dict:
        """开了思考的角色 -> API 档位（「*」= 其余角色，只有关不掉思考的模型才有）。记进 run settings。"""
        out = {r: e for r in REASONING_ROLES if (e := self.effort(r))}
        if (e := self.effort("*")) is not None:
            out["*"] = e
        return out

    def public(self) -> dict:
        """记进 state.json settings、可以给网页看的部分（不含 key）。v2.10d：计价 id 和模型名不同时（Kimi 国内站）另记
        price_id 和折算用的汇率。"""
        out = {"provider": self.provider, "model": self.model, "region": self.region, "thinking": self.thinking,
               "thinking_by_role": self.thinking_by_role(), "usd_cap": self.usd_cap, "byok": True}
        if self.price_id != self.model:
            out["price_id"] = self.price_id
            if "fx" in PRICES[self.price_id]:
                out["fx"] = dict(PRICES[self.price_id]["fx"])
        return out

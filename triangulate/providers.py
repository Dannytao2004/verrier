"""v2.10a：每次运行的模型设置（ModelSpec）和各家 API 的请求格式（adapter）。目前只有 DeepSeek。

ModelSpec = provider、model、region、思考档位、这次运行的花费上限，加上用户自己的 key（只在内存里，见 ModelSpec 的说明）。
有 ModelSpec 的运行就是「自带 key」（BYOK）的运行：pipeline.Context(spec=...) 把它交给 AgentLLM、Searcher 和 Budget。
没有 ModelSpec（命令行、回测、基线）时一切照旧：DeepSeek + key 文件，请求体和 HEAD 逐字节相同（tests/test_providers.py）。

adapter 只管各家不同的三件事：建请求（URL、请求头、请求体）、解析回复（文字、截断、用量）、计价；重试、先查截断、
JSON 解析、日志、预算这些外层循环留在 llm.LLM.json_call 和 agent/search.Searcher.search，所有 provider 共用。
设计说明和各家官方文档的链接在仓库根目录的 PROVIDERS.md。
"""
import math

from .config import MODEL, PRICES, UnknownModel, price, usd_cost

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
    """Anthropic Messages 形的回复（content 块数组）里取：查询词、搜索结果 URL、文字块、搜索次数、搜索错误数。"""
    usage = d.get("usage") or {}
    n_req = int(((usage.get("server_tool_use") or {}).get("web_search_requests")) or 0)
    queries, result_urls, texts, n_err = [], [], [], 0
    for b in d.get("content") or []:
        if b.get("type") == "server_tool_use":
            queries.append(str((b.get("input") or {}).get("query", ""))[:200])
        elif b.get("type") == "web_search_tool_result":
            c = b.get("content")
            if isinstance(c, list):
                result_urls += [x.get("url") for x in c if isinstance(x, dict) and x.get("url")]
                # DeepSeek 把错误也放在 list 里：[{"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}]
                n_err += sum(1 for x in c if isinstance(x, dict) and x.get("type") == "web_search_tool_result_error")
            else:
                n_err += 1
        elif b.get("type") == "text":
            texts.append(b.get("text") or "")
    return {"usage": usage, "n_req": n_req, "queries": queries, "result_urls": result_urls, "texts": texts,
            "n_err": n_err, "stop": d.get("stop_reason")}


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

    def chat_url(self, region: str) -> str:
        return self.regions[region]["chat"]

    def search_url(self, region: str) -> str:
        return self.regions[region]["search"]

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
    def chat_truncated(unpacked) -> bool:
        return unpacked[0].get("finish_reason") == "length"

    def search_request(self, model: str, key: str, prompt: str, *, max_tokens: int, max_uses: int):
        payload = {"model": model, "max_tokens": max_tokens,
                   "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}],
                   "messages": [{"role": "user", "content": prompt}]}
        return {"Content-Type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"}, payload

    search_unpack = staticmethod(anthropic_search_unpack)

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


DEEPSEEK = DeepSeekAdapter()
ADAPTERS = {"deepseek": DEEPSEEK}

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
}
PROVIDERS = {"deepseek": {"label": "DeepSeek", "models": ("deepseek-flash", "deepseek-v4-pro"),
                          "default_model": "deepseek-flash"}}
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

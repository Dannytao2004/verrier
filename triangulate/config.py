"""路径、模型、价格和 key 读取。key 只从外部文件读一行到内存，不打印、不写盘、不进 git。"""
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw" / "realFP"                       # 官方原件（不进 git）
BACKTEST_FULL = DATA / "backtest_realfp20.json"     # 含题目和答案（不进 git，可由 select 重建）
BACKTEST_IDS = DATA / "backtest_realfp20_ids.json"  # 只有 id（进 git）
RESULTS = ROOT / "results"
RESULTS_LOCAL = RESULTS / "realfp"                  # 含题目文字的逐题结果（不进 git）
CALLS = RESULTS / "calls.jsonl"                     # 每次模型调用一行，只有计量字段，没有内容
DOCS = ROOT / "docs"
GRAPHS = DOCS / "graphs"
GRAPHS_LOCAL = GRAPHS / "realfp"                    # 含题目文字的图页面（不进 git）

# 选题与 Monte Carlo 的固定种子（预注册在 PROBE_PLAN.md）
SELECT_SEED = 2021
SELECT_SPLIT = "test"
N_QUESTIONS = 20
MC_SEED = 20261015
MC_SAMPLES = 20000

# 默认读仓库根目录的 .env（已被 .gitignore 忽略）；放在别处就用环境变量 TRIANGULATE_KEY_FILE 指过去
KEY_FILE = Path(os.environ.get("TRIANGULATE_KEY_FILE", str(ROOT / ".env")))
KEY_NAME = "DEEPSEEK_API_KEY"
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = os.environ.get("TRIANGULATE_MODEL", "deepseek-flash")
MAX_CONCURRENCY = int(os.environ.get("TRIANGULATE_CONCURRENCY", "4"))

# v2.9a：按角色打开 DeepSeek 思考模式（实验臂；默认全关，请求和 frozen-v2.8r 逐字相同）。
# 环境变量 TRIANGULATE_THINKING，例如 "plan=high,judge=high,repair=high,audit=low,unit_arbiter=low"。
# 档位只有 low / high / max（官方 Thinking Mode 文档：medium 按 high 处理）。角色取 arm 的第一段，"judge:rN:repair" 算 repair。
# 思考 token 计入 max_tokens（probes/thinking_probe.py 实测：max_tokens=150 时思考用满、content 为空、finish_reason=length），
# 所以开了思考的角色在 MAX_TOKENS 之外再加 THINKING_EXTRA_TOKENS。思考 token 计在 completion_tokens 里，usd_cost 不用改。
THINKING_LEVELS = ("low", "high", "max")


def parse_thinking(spec: str) -> dict:
    out = {}
    for part in filter(None, (p.strip() for p in spec.split(","))):
        role, _, level = part.partition("=")
        role, level = role.strip(), level.strip().lower()
        if not role or level not in THINKING_LEVELS:
            raise ValueError(f"TRIANGULATE_THINKING: bad entry {part!r} (want role=low|high|max)")
        out[role] = level
    return out


def thinking_role(arm: str) -> str:
    parts = arm.split(":")
    return "repair" if "repair" in parts[1:] else parts[0]


THINKING = parse_thinking(os.environ.get("TRIANGULATE_THINKING", ""))
THINKING_EXTRA_TOKENS = int(os.environ.get("TRIANGULATE_THINKING_EXTRA", "24000"))

# 每个角色一次调用的输出上限（max_tokens）。只有这一个来源：各调用处和预算预扣（agent/pipeline.Budget）都查这张表，
# 每次 agent 运行的 state.json 里也记一份（agent/run.save_run 的 settings）。v2.5.3 只是收拢，值和收拢前各处写的相同。
MAX_TOKENS = {
    "plan": 6000,
    "extract": 16000,        # 抽取员，每页一次。v2.8b 从 4000 调到 16000：页面最多发 40 万字符，长页的 JSON 不被截断
    "judge": 24000,          # v2 的 6000 在 167 个数据点时被截断过；v2.11d 冒烟（347 个点）第 2 轮在 12000 处被截断两次
    "repair": 24000,         # 裁判修正轮：同 judge
    "audit": 4000,           # 输入核对
    "unit_check": 4000,      # v2.8e：单位核对（三个核对模型，每个方法各一次）
    "unit_arbiter": 4000,    # v2.8e：单位裁定（第四个模型）
    "value_check": 2000,     # v2.8o：一个数的核对（只回 true / false）
    "value_reread": 2000,    # v2.8o：核对没过时重新读这个数
    "published": 3000,       # 「答案已公布」确认
    "early": 3000,           # 提前停确认：同 published（同一个 prompt）
    "final": 4000,           # 终稿
    "search": 8192,          # agent 的 SEARCHER（Anthropic 兼容接口）。v2.6a 从 2048 调到 8192：已存 493 次搜索里 39 次在 2048 截断
    "naive": 500,            # arm (1) 直接问
    "structured": 6000,      # arm (2) 不联网结构化
    "search_direct": 4096,   # arm (3) 联网直接答的正式运行（预注册结果用的值；补充运行的 32000 在 probes/search_direct_supp.py）
}

# USD / 1M tokens：(cache hit, cache miss, output)，每个模型一项，带来源和查看日期。v2.10a：没有价格的模型拒跑（price() 抛
# UnknownModel），不再静默按 deepseek-flash 计价。DeepSeek 峰时 = UTC 周一至周五 01:00-04:00、06:00-10:00，闲时半价；
# 中国法定假日也算闲时，这里忽略（只会高估成本）。没有分时价的 provider，peak 和 offpeak 写同一组价。
DEEPSEEK_PRICING = "https://api-docs.deepseek.com/quick_start/pricing"
PRICES = {
    "deepseek-flash": {"provider": "deepseek", "offpeak": (0.003, 0.15, 0.60), "peak": (0.006, 0.30, 1.20),
                       "source": DEEPSEEK_PRICING, "checked": "2026-10-21"},   # 2026-10-15 首次记录，10-21 复查未变
    "deepseek-v4-pro": {"provider": "deepseek", "offpeak": (0.022, 0.66, 1.98), "peak": (0.044, 1.32, 3.96),
                        "source": DEEPSEEK_PRICING, "checked": "2026-10-21"},
}

# v2.10b：Claude（Anthropic 官方 Pricing 页，2026-10-21 查看）。没有分时价：peak = offpeak = (cache hit, base input, output)。
# cache 写入另有两档价（5 分钟 / 1 小时，providers.claude_usage_cost 用）。prompt_cache = "explicit"：只有请求里写了
# cache_control 才缓存（本项目不写），所以按 DeepSeek 实测的「一个方向」估价时，DeepSeek 自动缓存命中的那部分按 base input 算
# （pipeline.Budget.typical_direction_usd）。Haiku 5.5 按单次请求的 prompt 长度分两档：prompt（input + cache 读 + cache 写）
# 超过 100,000 token 的请求整次按高价（long_context）。请求里不写 inference_geo（默认 global，标准价）；回复里 usage.inference_geo
# 是 "us" 时按官方 1.1 倍算
CLAUDE_PRICING = "https://platform.claude.com/docs/en/about-claude/pricing"


def _claude_price(base_in, write_5m, write_1h, hit, out, **extra) -> dict:
    return {"provider": "claude", "offpeak": (hit, base_in, out), "peak": (hit, base_in, out),
            "cache_write_5m": write_5m, "cache_write_1h": write_1h, "prompt_cache": "explicit",
            "source": CLAUDE_PRICING, "checked": "2026-10-21", **extra}


PRICES.update({
    "claude-haiku-5-5": _claude_price(0.10, 0.125, 0.20, 0.01, 0.50, long_context={
        "threshold_tokens": 100_000, "peak": (0.05, 0.50, 2.50), "cache_write_5m": 0.625, "cache_write_1h": 1.00}),
    "claude-sonnet-5-5": _claude_price(2.00, 2.50, 4.00, 0.10, 10.00),
    "claude-opus-5-5": _claude_price(4.00, 5.00, 8.00, 0.20, 20.00),
    "claude-fable-5-1": _claude_price(10.00, 12.50, 20.00, 0.25, 50.00),
})
CLAUDE_US_GEO_MULTIPLIER = 1.1   # Pricing 页 Data residency：inference_geo "us" 所有 token 类别 1.1 倍

# v2.10c：OpenAI（官方 Pricing 页 Standard 档，2026-10-21 查看）。没有分时价：peak = offpeak = (cached input, input, output)。
# GPT-5.6 及以后的模型 cache 写入单独计价（Prompt caching 页：30 分钟 1.25 倍、12 小时 2.5 倍 input 价，不是另加的费用，
# 而是这部分 input 改按写入价算）。默认的 implicit 模式在最后一条 user 消息末尾写缓存（本项目不改这个默认，见 PROVIDERS.md），
# 所以 prompt_cache = "implicit_write"：预扣和「一个方向」的估价把输入都按 30 分钟写入价算（最坏情况）。
# 单次请求 input 超过 272K token 时整次按 long_context 价（Pricing 页：Short context ≤272K input tokens）。
# 只用 api.openai.com（global）；data residency 端点（us. / eu.）对 2026-03-05 以后的模型加价 10%，不提供
OPENAI_PRICING = "https://developers.openai.com/api/docs/pricing"


def _openai_price(base_in, hit, write_30m, write_12h, out, long) -> dict:
    lbase, lhit, lw30, lw12, lout = long
    return {"provider": "gpt", "offpeak": (hit, base_in, out), "peak": (hit, base_in, out),
            "cache_write_30m": write_30m, "cache_write_12h": write_12h, "prompt_cache": "implicit_write",
            "long_context": {"threshold_tokens": 272_000, "peak": (lhit, lbase, lout),
                             "cache_write_30m": lw30, "cache_write_12h": lw12},
            "source": OPENAI_PRICING, "checked": "2026-10-21"}


PRICES.update({   # input, cached input, 30m write, 12h write, output；long context 同顺序
    "gpt-6-luna": _openai_price(0.10, 0.01, 0.125, 0.25, 0.50, long=(0.20, 0.02, 0.25, 0.50, 0.75)),
    "gpt-6.1-sol": _openai_price(2.00, 0.10, 2.50, 5.00, 10.00, long=(4.00, 0.20, 5.00, 10.00, 15.00)),
    "gpt-6-astra": _openai_price(10.00, 1.00, 12.50, 25.00, 50.00, long=(20.00, 2.00, 25.00, 50.00, 75.00)),
})

# v2.10d：Kimi（Moonshot AI 开放平台，2026-10-21 查看）。国际站（api.moonshot.ai）按 USD、国内站（api.moonshot.cn）按 CNY，
# 两站的 key、余额、价格各自独立，所以价格按「模型@区域」记：国际站用模型名本身，国内站是 "kimi-k3@cn"（ModelSpec.price_id）。
# 价格表在页面里由 JS 渲染（.md 导出是空表），数字取自页面 HTML 里编译后的表格（列名见 PROVIDERS.md 第 11.6 节）。
# 没有分时价：peak = offpeak = (cache hit, cache miss, output)。K3 另列缓存写入（5 分钟 / 1 小时）；本项目不写 prompt_cache_options，
# 按官方默认是 5 分钟档（K3 的 5 分钟写入价 = cache miss 价）。
# prompt_cache = "implicit"：服务端自动缓存重复前缀，但这个 agent 在 Kimi 上的命中率没测过，「一个方向」的估价把输入全按 miss 价算。
# v2.10h：K2.6 删掉（用户 10-21：只用各家自带的搜索，K2.6 没有）。K3 的搜索改走 Responses API 自带的 web_search 工具；两站的 WebSearch
# Pricing 页都没列它的单价（只列了 REST 接口 Basic / Pro / Fetch 和已下线的 $web_search），usage 里也没有搜索次数，所以按 web_search_call
# 的个数、每次 KIMI_WEB_SEARCH_FEE_ASSUMED_USD 的保守假设记账（同 DeepSeek 的做法；高于两站列出的所有搜索单价：旧 $web_search
# $0.005 / ¥0.03、Pro $0.003 / ¥0.015），两站都按这个美元数（search_fee_assumed = True，不是官方价）。
# 国内站的 CNY 价按下面的汇率折成 USD（这次运行的上限是美元）：中国人民银行授权中国外汇交易中心公布的 2026-10-21 人民币汇率中间价
KIMI_PRICING = "https://platform.kimi.ai/docs/pricing/chat"
KIMI_PRICING_CN = "https://platform.kimi.com/docs/pricing/chat"
KIMI_SEARCH_PRICING = "https://platform.kimi.ai/docs/pricing/websearch"
KIMI_SEARCH_PRICING_CN = "https://platform.kimi.com/docs/pricing/websearch"
KIMI_WEB_SEARCH_FEE_ASSUMED_USD = 0.01
CNY_PER_USD = 6.7192
CNY_PER_USD_SOURCE = "https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026102108513972558/index.html"
CNY_PER_USD_DATE = "2026-10-21"


def _kimi_price(currency, hit, miss, out, write_5m, write_1h) -> dict:
    """Kimi 一个模型在一个区域的价格。currency 是 "USD" 或 "CNY"（CNY 按 CNY_PER_USD 折成 USD，原价另存在 "listed" 里）。
    搜索费是假设的美元数（见上面的说明），不按区域折算。"""
    r = 1.0 if currency == "USD" else 1.0 / CNY_PER_USD
    p = {"provider": "kimi", "offpeak": (hit * r, miss * r, out * r), "peak": (hit * r, miss * r, out * r),
         "prompt_cache": "implicit", "search_fee_usd": KIMI_WEB_SEARCH_FEE_ASSUMED_USD, "search_fee_assumed": True,
         "currency": currency, "listed": {"hit": hit, "miss": miss, "out": out, "write_5m": write_5m, "write_1h": write_1h},
         "source": KIMI_PRICING if currency == "USD" else KIMI_PRICING_CN,
         "search_source": KIMI_SEARCH_PRICING if currency == "USD" else KIMI_SEARCH_PRICING_CN, "checked": "2026-10-21",
         "cache_write_5m": write_5m * r, "cache_write_1h": write_1h * r}
    if currency != "USD":
        p["fx"] = {"cny_per_usd": CNY_PER_USD, "source": CNY_PER_USD_SOURCE, "date": CNY_PER_USD_DATE}
    return p


PRICES.update({   # cache hit, cache miss, output, 5 分钟 / 1 小时缓存写入
    "kimi-k3": _kimi_price("USD", 0.30, 3.00, 15.00, write_5m=3.00, write_1h=6.00),
    "kimi-k3@cn": _kimi_price("CNY", 2.00, 20.00, 100.00, write_5m=20.00, write_1h=40.00),
})

# v2.10e：GLM（Z.ai 国际站 api.z.ai 按 USD；智谱开放平台国内站 open.bigmodel.cn 按 CNY，2026-10-21 查看）。同 Kimi：两站的 key、余额、
# 价格各自独立，价格按「模型@区域」记（国际站是模型名本身，国内站 "glm-5.3@cn"），CNY 按上面同一个汇率中间价折成 USD。
# 没有分时价：peak = offpeak = (cached input, input, output)。缓存是隐式自动的（Context Caching 指南），没有写入费；缓存存储
# 「限时免费」（两站价格页），这里不计。prompt_cache = "implicit"：这个 agent 在 GLM 上的命中率没测过，「一个方向」的估价和预扣把输入
# 全按 input 价算（同 Kimi）。search_fee_usd：v2.10h 起是 Chat Completions 自带的 web_search 工具每次的价格（用户 10-21：只用自带的
# 搜索）：国际站价格页 Built-in Tools「Web Search $0.01 / use」；国内站「搜索工具按照实际调用次数计费」，本项目用的引擎 search_std
# ¥0.01 / 次（联网搜索指南的搜索引擎说明表同价）
GLM_PRICING = "https://docs.z.ai/guides/overview/pricing"
GLM_PRICING_CN = "https://docs.bigmodel.cn/cn/guide/start/pricing"


def _glm_price(currency, hit, miss, out, search_fee) -> dict:
    """GLM 一个模型在一个区域的价格（同 _kimi_price 的形状：CNY 折成 USD，原价存在 "listed" 里）。"""
    r = 1.0 if currency == "USD" else 1.0 / CNY_PER_USD
    p = {"provider": "glm", "offpeak": (hit * r, miss * r, out * r), "peak": (hit * r, miss * r, out * r),
         "prompt_cache": "implicit", "search_fee_usd": search_fee * r, "currency": currency,
         "listed": {"hit": hit, "miss": miss, "out": out, "search_fee": search_fee},
         "source": GLM_PRICING if currency == "USD" else GLM_PRICING_CN, "checked": "2026-10-21"}
    if currency != "USD":
        p["fx"] = {"cny_per_usd": CNY_PER_USD, "source": CNY_PER_USD_SOURCE, "date": CNY_PER_USD_DATE}
    return p


PRICES.update({   # cached input, input, output, 每次搜索
    "glm-5.3": _glm_price("USD", 0.26, 1.4, 4.4, 0.01),
    "glm-5.2": _glm_price("USD", 0.26, 1.4, 4.4, 0.01),
    "glm-4.7-flashx": _glm_price("USD", 0.01, 0.07, 0.4, 0.01),   # 国际站价格页 Other Pricing
    "glm-5.3@cn": _glm_price("CNY", 2, 8, 28, 0.01),
    "glm-5.2@cn": _glm_price("CNY", 2, 8, 28, 0.01),
    "glm-4.7-flashx@cn": _glm_price("CNY", 0.1, 0.5, 3, 0.01),      # 国内站价格页「更多文本模型」
})


class UnknownModel(ValueError):
    """config.PRICES 里没有这个模型：不能计价，就不跑。"""


class UnsupportedModel(UnknownModel):
    """v2.10f：命令行、回测、基线（没有 ModelSpec）只走 DeepSeek + key 文件；TRIANGULATE_MODEL 设成别家（有价格）的模型时拒跑，
    不把别家的模型 id 带着 DeepSeek 的 key 发到 api.deepseek.com、又按别家的价格记账。"""


def price(model: str) -> dict:
    p = PRICES.get(model)
    if p is None:
        raise UnknownModel(f"model {model!r} has no price entry in config.PRICES; add one (with source and date) first")
    return p


def require_deepseek(model: str) -> dict:
    """没有 ModelSpec 的调用（命令行、回测、基线）用：有价格、而且是 DeepSeek 的模型。否则抛 UnknownModel / UnsupportedModel。"""
    p = price(model)
    provider = p.get("provider", "deepseek")
    if provider != "deepseek":
        raise UnsupportedModel(f"model {model!r} is a {provider} model; command-line runs, backtests and baselines only use "
                               "DeepSeek models with the key file (TRIANGULATE_MODEL); other providers are only available in "
                               "bring-your-own-key web runs")
    return p


def read_key() -> str:
    """只取 KEY_NAME 这一行；找不到就报错，报错信息里不带任何 key 内容。"""
    if not KEY_FILE.exists():
        raise RuntimeError(f"key file not found: {KEY_FILE} (set TRIANGULATE_KEY_FILE)")
    for line in KEY_FILE.read_text(encoding="utf-8-sig").splitlines():  # utf-8-sig：去掉 PowerShell 写出的 BOM
        line = line.strip().removeprefix("export ").strip()
        if line.startswith(KEY_NAME + "="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
    raise RuntimeError(f"{KEY_NAME} not set in {KEY_FILE}")


def is_peak(t: datetime) -> bool:
    t = t.astimezone(timezone.utc)
    return t.weekday() < 5 and (1 <= t.hour < 4 or 6 <= t.hour < 10)


def usd_cost(usage: dict, t: datetime, model: str = MODEL) -> float:
    hit, miss, out = price(model)["peak" if is_peak(t) else "offpeak"]
    return (usage.get("prompt_cache_hit_tokens", 0) * hit + usage.get("prompt_cache_miss_tokens", 0) * miss
            + usage.get("completion_tokens", 0) * out) / 1e6


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

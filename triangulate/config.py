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
    "judge": 12000,          # v2 的 6000 在 167 个数据点时被截断过
    "repair": 12000,         # 裁判修正轮：同 judge
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


class UnknownModel(ValueError):
    """config.PRICES 里没有这个模型：不能计价，就不跑。"""


def price(model: str) -> dict:
    p = PRICES.get(model)
    if p is None:
        raise UnknownModel(f"model {model!r} has no price entry in config.PRICES; add one (with source and date) first")
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

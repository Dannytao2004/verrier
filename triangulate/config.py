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

# 每个角色一次调用的输出上限（max_tokens）。只有这一个来源：各调用处和预算预扣（agent/pipeline.Budget）都查这张表，
# 每次 agent 运行的 state.json 里也记一份（agent/run.save_run 的 settings）。v2.5.3 只是收拢，值和收拢前各处写的相同。
MAX_TOKENS = {
    "plan": 6000,
    "extract": 4000,         # 抽取员，每页一次
    "judge": 12000,          # v2 的 6000 在 167 个数据点时被截断过
    "repair": 12000,         # 裁判修正轮：同 judge
    "audit": 4000,           # 输入核对
    "published": 3000,       # 「答案已公布」确认
    "early": 3000,           # 提前停确认：同 published（同一个 prompt）
    "final": 4000,           # 终稿
    "search": 8192,          # agent 的 SEARCHER（Anthropic 兼容接口）。v2.6a 从 2048 调到 8192：已存 493 次搜索里 39 次在 2048 截断
    "naive": 500,            # arm (1) 直接问
    "structured": 6000,      # arm (2) 不联网结构化
    "search_direct": 4096,   # arm (3) 联网直接答的正式运行（预注册结果用的值；补充运行的 32000 在 probes/search_direct_supp.py）
}

# USD / 1M tokens：(cache hit, cache miss, output)。来源 https://api-docs.deepseek.com/quick_start/pricing（2026-10-15 查看）。
# 峰时 = UTC 周一至周五 01:00-04:00、06:00-10:00；中国法定假日也算闲时，这里忽略（只会高估成本）。
PRICES = {"deepseek-flash": {"offpeak": (0.003, 0.15, 0.60), "peak": (0.006, 0.30, 1.20)}}


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
    hit, miss, out = PRICES.get(model, PRICES["deepseek-flash"])["peak" if is_peak(t) else "offpeak"]
    return (usage.get("prompt_cache_hit_tokens", 0) * hit + usage.get("prompt_cache_miss_tokens", 0) * miss
            + usage.get("completion_tokens", 0) * out) / 1e6


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

"""web-v0.9：网页上的 provider / 模型目录（GET /api/providers）和每次运行的花费估计。不含任何 key。

只读 providers.py（PROVIDERS、MODELS、各家 adapter）和 config.PRICES 里已有的东西，不另写一份模型清单。
花费估计 = DeepSeek 实测的一次运行的 token 构成（RUN_PROFILE）x 这个模型的官方价（峰时价；缓存的处理同 Budget.profile_usd，偏保守），
方向数按这个模型在这个上限下的 Budget.for_model(...).directions 算。只是给人看的估计，不参与预算（预算照旧按预扣守上限）。
v2.10f：「会不会中止」改成看一次最小的运行（规划 + 一次搜索 + 抽取一页 + 裁判）最坏情况的预扣合计（run_floor）：预扣放不下只是因为
在途的调用时，自带 key 的运行会等（pipeline.Budget.wait_for_room），第一轮同时在途的预扣合计不再让运行中止。合计超过上限时，
网页运行由 Registry.start 在服务端拒跑（web/runs.py）。
"""
import inspect
import math

from .. import providers as PV
from ..agent.pipeline import Budget, configure_byok
from ..config import MAX_TOKENS, PRICES

# 一次运行的 token 构成（只用来估花费）。来源：results/agent/**/calls.jsonl 里 2026-10-18 起的 deepseek-flash 运行（同 frozen-v2.8r 的代码），
# 50 次不开思考的平均；思考两项来自 22 次思考实验运行（v2.9a/b：plan / judge / repair = high，audit / unit_arbiter = low）。
# 方向本身的 token 用 Budget.DIRECTION_PROFILE（1251 个方向的平均，每个方向 4 次搜索）
RUN_PROFILE = {
    "directions_per_round1_max": 1.13,   # 实际跑的方向数（第一轮 + 第二轮 base-rate）/ 第一轮的方向上限（max_directions）
    "calls_per_direction": 3.1,          # 每个方向的调用次数（搜索 + 挑页 + 抽取）
    "reasoning": {"hit": 19_400, "miss": 28_400, "out": 14_900},   # plan、judge、repair 合计（每次运行）
    "other": {"hit": 5_000, "miss": 18_700, "out": 3_100},         # 单位核对、输入核对、已公布检查、终稿等合计
    "other_calls": 15,
    "thinking_out_reasoning": 47_300,    # plan / judge / repair 开思考时多出的思考 token（每次运行；DeepSeek high 实测，别的档位也按它算）
    "thinking_out_per_call_low": 870,    # 其余角色开 low 时每次调用的思考 token（DeepSeek low 实测：audit / unit_arbiter）
}
MIN_CAP_STEP = 0.5            # 「放得下的最小上限」按 0.5 美元一档往上取整
EXTRACT_PAGE_CHARS = 40_000   # 「抽取一页」的预扣按这么长的页面算（PROVIDERS.md 各家预扣表里的「抽取（4 万字符）」）
# v2.10f：一次最小的运行（run_floor）里规划、裁判两次调用按多长的 prompt 算：规划的 prompt（PLAN_SYSTEM + PLAN_USER + 清单）约 9,000 字符，
# 加上最长 2,000 字符的题目取 20,000（PROVIDERS.md 各家预扣表的「plan（2 万字符）」）；裁判取 100,000（已存 355 次 DeepSeek 裁判调用的
# prompt p99 约 25,400 token，英文按约 4 字符 / token）
PLAN_PROMPT_CHARS = 20_000
JUDGE_PROMPT_CHARS = 100_000
_DEFAULTS = {k: p.default for k, p in inspect.signature(Budget.__init__).parameters.items()
             if p.default is not inspect.Parameter.empty}
LLM_CONCURRENCY = _DEFAULTS["llm_concurrency"]   # 第一轮同时在途的调用最多这么多（Budget.sem）
THINK_KEYS = ("thinking", "reasoning_effort", "output_config")   # 各家请求体里控制思考的字段

ESTIMATE_NOTE = {
    "en": "Rough estimate, not a quote: token counts measured on DeepSeek Flash runs (50 runs from 2026-10-18; thinking from 22 "
          "thinking runs) priced at this model's official price (peak price, no cache discount). Other tokenizers and thinking "
          "lengths differ (not measured). The spending cap is what limits a run: each call first reserves an estimate of its "
          "worst case (and waits while other calls are in flight); a cap that cannot cover the worst case of a minimal run is "
          "refused. The estimate is not a hard limit: a call that uses more than its reservation can overshoot the cap a little.",
    "zh": "只是粗估：token 数取自 DeepSeek Flash 的实测运行（2026-10-18 起 50 次；思考部分取自 22 次思考实验），按这个模型的官方价"
          "（峰时价、不算缓存折扣）计价。别家的 tokenizer 和思考长度不同（没测过）。真正限住花费的是上限：每次调用先按估计的最坏情况预扣"
          "（别的调用在途、放不下时先等）；放不下一次最小运行的上限会被拒跑。预扣是估计，不是硬上限：用得比预扣多的调用会让花费略超上限。",
}

PROVIDER_NOTES = {
    "deepseek": [
        {"en": "The budget counts each web search at an assumed US$0.01: DeepSeek's price page does not list the web_search tool of "
               "its Anthropic-compatible API.",
         "zh": "预算按每次搜索 $0.01 的假设记账：DeepSeek 价格页没有单列 Anthropic 兼容接口里 web_search 工具的价格。"},
    ],
    "claude": [
        {"en": "Use a key limited to one workspace: keys that need the anthropic-workspace-id header are rejected with HTTP 400 "
               "(this app does not send it).",
         "zh": "请用只属于一个 workspace 的 key：需要 anthropic-workspace-id 请求头的 key 会被拒（HTTP 400），本应用不发这个头。"},
        {"en": "Mainland China, Hong Kong and Macau are not in Anthropic's supported regions.",
         "zh": "中国大陆、香港、澳门不在 Anthropic 支持的地区内。"},
    ],
    "gpt": [
        {"en": "Use a project key with a hard spend limit set in the OpenAI Platform (Billing / Limits).",
         "zh": "建议用 project key，并在 OpenAI Platform 的 Billing / Limits 里设硬性消费上限。"},
        {"en": "Mainland China, Hong Kong and Macau are not on OpenAI's supported countries list.",
         "zh": "中国大陆、香港、澳门不在 OpenAI 支持的国家和地区列表里。"},
    ],
    "kimi": [   # 两站的 key 互不通用：网页的区域一栏统一写（Kimi、GLM 都有）
        {"en": "New accounts (Tier0, US$1 topped up) are limited to 1 concurrent request and 3 requests per minute; runs will hit "
               "429 rate limits. Tier1 (US$10 cumulative) or above is recommended. K3 must be unlocked by topping up first.",
         "zh": "新账户（Tier0，累计充值 $1）只有并发 1、每分钟 3 次，运行会连续撞 429 限流；建议 Tier1（累计 $10）以上。K3 要先充值解锁。"},
        # v2.10h：搜索改走 K3 自带的 web_search（用户 10-21：只用自带的搜索）
        {"en": "Web search uses K3's built-in web_search tool (Responses API): Kimi's server decides from the search brief whether "
               "to search, runs the search before the model answers, and cannot be forced to search. Kimi does not list a price "
               "for it; the budget assumes US$0.01 per search. Kimi's K3 quickstart says web search is being updated and is not "
               "recommended for production workflows in the near term.",
         "zh": "联网搜索用 K3 自带的 web_search 工具（Responses API）：由 Kimi 服务端按搜索说明决定搜不搜、在模型回答之前搜，没法强制它搜。"
               "Kimi 没公布这个工具的单价，预算按每次 $0.01 的假设记账。Kimi 的 K3 快速开始页写着联网搜索正在更新、近期不建议用于生产流程。"},
    ],
    "glm": [
        {"en": PV.GLM_KEY_NOTE,
         "zh": "只收 Standard API Key：Z.ai 在 API Keys -> Standard API Key（https://z.ai/manage-apikey/apikey-list）；智谱开放平台在 "
               "API Keys（https://bigmodel.cn/usercenter/proj-mgmt/apikeys）。GLM Coding Plan 的 key 只能在官方支持的编程工具里用，"
               "不能用在这里。"},
        {"en": "Z.ai shows billing one day late (n-1), and its top-up does not support 3-D Secure cards.",
         "zh": "Z.ai 的账单晚一天显示（n-1），充值不支持 3DS 信用卡。"},
        # v2.10h：搜索改走 GLM 自带的 web_search（用户 10-21：只用自带的搜索）
        {"en": "Web search uses GLM's built-in web_search tool in Chat Completions (engine search_pro_jina on Z.ai, search_std on "
               "bigmodel.cn): the service first checks the search brief for search intent, searches once per request and feeds the "
               "results to the model; links come from the reply's web_search list. Each request is counted as one search "
               "(US$0.01 on Z.ai, CNY 0.01 on bigmodel.cn).",
         "zh": "联网搜索用 GLM 在 Chat Completions 里自带的 web_search 工具（Z.ai 用 search_pro_jina 引擎，智谱开放平台用 search_std）："
               "服务端先对搜索说明做意图识别，一次请求搜一次，把结果交给模型；链接取自回复里的 web_search 列表。每个请求按一次搜索记账"
               "（Z.ai $0.01，智谱 ¥0.01）。"},
    ],
}

# 模型自己的说明（思考档位的映射等）。关不掉思考、没有深度档位这两条由 MODELS 自动生成，不写在这里
MODEL_NOTES = {
    "deepseek-flash": [{"en": "DeepSeek has low / high / max; medium is sent as high (official mapping).",
                        "zh": "DeepSeek 只有 low / high / max，medium 按官方映射发 high。"}],
    "deepseek-v4-pro": [{"en": "DeepSeek has low / high / max; medium is sent as high (official mapping).",
                         "zh": "DeepSeek 只有 low / high / max，medium 按官方映射发 high。"}],
    "claude-sonnet-5-5": [{"en": "Off sends thinking type between_tools (Sonnet 5.5 rejects disabled).",
                           "zh": "关思考发的是 thinking type between_tools（Sonnet 5.5 不收 disabled）。"}],
    "gpt-6-luna": [{"en": "Off sends reasoning_effort none (left out, Luna would think at medium).",
                    "zh": "关思考发 reasoning_effort none（不写的话 Luna 默认按 medium 思考）。"}],
    "kimi-k3": [{"en": "High is sent as max (K3 has low / high / max).", "zh": "high 发的是 max（K3 只有 low / high / max）。"}],
    "glm-5.3": [{"en": "High is sent as max (GLM-5.3 has low / high / max).", "zh": "high 发的是 max（GLM-5.3 只有 low / high / max）。"}],
    "glm-5.2": [{"en": "Low and medium are both sent as high (GLM maps them to high anyway); high is sent as max.",
                 "zh": "low、medium 都发 high（GLM 本来就把它们映射成 high）；high 发 max。"}],
    "glm-4.7-flashx": [{"en": "Model id taken from the China API reference; whether the international site accepts it was not "
                              "verified (if not, the first call fails with error 1211).",
                        "zh": "模型 id 取自国内站 API 参考；国际站收不收这个 id 没核实（不收的话第一个调用报 1211）。"}],
}
NOTE_NO_OFF = {"en": "Thinking cannot be turned off for this model: off is not offered, and the other roles use the lowest level.",
               "zh": "这个模型关不掉思考：不提供 off，其余角色用最低一档。"}
NOTE_NO_DEPTH = {"en": "No depth levels: low, medium and high all mean thinking on.",
                 "zh": "没有深度档位：low、medium、high 都只是「开」。"}


def parse_cap(v) -> float:
    """网页传来的花费上限（美元）。不是有限正数就抛 ValueError（ModelSpec 也做同样的检查）。"""
    if isinstance(v, bool):
        raise ValueError("usd_cap must be a number")
    try:
        cap = float(v)
    except (TypeError, ValueError):
        raise ValueError("usd_cap must be a number") from None
    if not math.isfinite(cap) or cap <= 0:
        raise ValueError("usd_cap must be a positive number of US dollars")
    return cap


def default_thinking(model: str) -> str:
    """网页上这个模型的默认档位：能关就 off，否则最低一档（同 ModelSpec 的默认 off）。"""
    return PV.thinking_levels(model)[0]


def sends(model: str, effort) -> dict:
    """这个思考档位下，这家请求体里控制思考的字段（用 adapter 自己建请求体取出来，和真实发出的相同；不发请求，key 留空）。"""
    ad = PV.ADAPTERS[PV.MODELS[model]["provider"]]
    _headers, payload = ad.chat_request(model, "", [{"role": "user", "content": "x"}], max_tokens=1, effort=effort)
    return {k: payload[k] for k in THINK_KEYS if k in payload}


def _budget(pid: str, model: str, level: str, cap: float) -> Budget:
    """和真正运行的预算同样设置（pipeline.Context -> configure_byok：搜索按实际发出的 max_tokens 和 p99 的输入预扣）。"""
    return configure_byok(Budget.for_model(pid, usd=cap), model, level)


def _round1_hold(b: Budget) -> float:
    """第一轮各方向同时搜索时的预扣合计（最多 LLM_CONCURRENCY 个在途）。v2.10f：超过上限时搜索排队（等在途的结束），不再中止运行。"""
    return min(b.directions, LLM_CONCURRENCY) * b.search_reserve()


def _call_hold(pid: str, model: str, level: str, role: str, chars: int) -> float:
    """一次 JSON 调用（这个角色、prompt 有 chars 个字符）的预扣：同 AgentLLM.ask，按发出的 max_tokens（含思考余量）。"""
    return Budget.llm_reserve(chars, PV.tokens_for_model(model, level, role, MAX_TOKENS[role])[1], pid)


def _extract_hold(pid: str, model: str, level: str) -> float:
    """抽取一个 EXTRACT_PAGE_CHARS 字符的页面时的预扣。"""
    return _call_hold(pid, model, level, "extract", EXTRACT_PAGE_CHARS)


def run_floor(model: str, region: str, level: str) -> dict:
    """v2.10f：一次最小的运行（一个方向：规划 + 一次搜索 + 抽取一页 + 裁判一次）各步最坏情况的预扣和合计（usd）。预扣是一步一步拿的，
    每一步都要「已花 + 这一次」放得下；前面的调用按预扣算（最坏情况）。合计放不下上限的运行在最坏情况下拿不到裁判那一步，网页拒跑。
    不随上限变（上限只决定方向数）。"""
    ad = PV.ADAPTERS[PV.MODELS[model]["provider"]]
    pid = PV.price_id(model, region, ad)
    parts = {"plan": _call_hold(pid, model, level, "plan", PLAN_PROMPT_CHARS),
             "search": _budget(pid, model, level, 1.0).search_reserve(),
             "extract": _extract_hold(pid, model, level),
             "judge": _call_hold(pid, model, level, "judge", JUDGE_PROMPT_CHARS)}
    return {"parts": {k: round(v, 4) for k, v in parts.items()}, "usd": sum(parts.values())}


def min_cap(floor_usd: float) -> float:
    """放得下一次最小运行的最小上限：floor_usd 按 MIN_CAP_STEP 往上取整。"""
    return round(math.ceil(floor_usd / MIN_CAP_STEP - 1e-9) * MIN_CAP_STEP, 2)


def estimate(model: str, region: str, level: str, cap: float) -> dict:
    """这个模型 / 区域 / 档位 / 上限下：第一轮方向数、估计的每次运行花费、第一轮的预扣（同时搜索的合计、抽取一页），
    一次最小运行的最坏情况预扣（run_floor_usd）放不放得下（stops_early = 放不下，网页会拒跑；这时给 min_cap_usd），
    第一轮的搜索会不会排队（round1_queues：同时在途的预扣合计超过上限）。"""
    ad = PV.ADAPTERS[PV.MODELS[model]["provider"]]
    pid = PV.price_id(model, region, ad)
    b = _budget(pid, model, level, cap)
    rp = RUN_PROFILE
    n_dirs = rp["directions_per_round1_max"] * b.directions
    usd = (n_dirs * Budget.profile_usd(pid, Budget.DIRECTION_PROFILE) + Budget.profile_usd(pid, rp["reasoning"])
           + Budget.profile_usd(pid, rp["other"]))
    think = 0.0
    if PV.effort_for(model, level, "plan"):
        think += rp["thinking_out_reasoning"]
    if PV.effort_for(model, level, "extract"):   # 关不掉思考的模型：其余角色也按最低一档在想
        think += rp["thinking_out_per_call_low"] * (rp["calls_per_direction"] * n_dirs + rp["other_calls"])
    usd += think * Budget.peak_rates(pid, 0)[2] / 1e6
    ex = _extract_hold(pid, model, level)
    floor = run_floor(model, region, level)
    out = {"price_id": pid, "directions": b.directions, "est_usd": round(usd, 2), "over_cap": usd > cap,
           "round1_search_hold_usd": round(_round1_hold(b), 2), "extract_hold_usd": round(ex, 2),
           "round1_queues": _round1_hold(b) > cap, "run_floor_usd": round(floor["usd"], 2), "run_floor": floor["parts"],
           "stops_early": floor["usd"] > cap}
    if out["stops_early"]:
        out["min_cap_usd"] = min_cap(floor["usd"])
    return out


def _price_view(pid: str) -> dict:
    p = PRICES[pid]
    hit, miss, out = p["peak"]
    v = {"usd_per_mtok": {"cache_hit": hit, "input": miss, "output": out}, "source": p.get("source"), "checked": p.get("checked"),
         "currency": p.get("currency", "USD"), "peak_offpeak": p.get("offpeak") != p.get("peak")}
    if "listed" in p:
        v["listed"] = dict(p["listed"])
    if "fx" in p:
        v["fx"] = dict(p["fx"])
    return v


def model_view(model: str, cap: float) -> dict:
    m = PV.MODELS[model]
    ad = PV.ADAPTERS[m["provider"]]
    levels = PV.thinking_levels(model)
    notes = list(MODEL_NOTES.get(model, []))
    if not m["thinking_off"]:
        notes.insert(0, NOTE_NO_OFF)
    if m.get("thinking_depth") is False:
        notes.insert(0, NOTE_NO_DEPTH)
    thinking = {"levels": list(levels), "can_turn_off": bool(m["thinking_off"]), "default": default_thinking(model),
                "sends": {lv: sends(model, PV.effort_for(model, lv, "plan")) for lv in levels},
                "sends_other_roles": sends(model, PV.effort_for(model, levels[0], "extract"))}
    by_region = {}
    for region in ad.regions:
        est = {lv: estimate(model, region, lv, cap) for lv in levels}
        first = est[levels[0]]
        by_region[region] = {"price_id": first["price_id"], "price": _price_view(first["price_id"]),
                             "directions": first["directions"], "by_thinking": est}
    return {"id": model, "label": m["label"], "max_output": m["max_output"], "thinking": thinking, "notes": notes,
            "by_region": by_region}


def providers_view(cap: float = PV.DEFAULT_USD_CAP) -> dict:
    """GET /api/providers 的内容：provider、区域、模型（思考档位、估计花费）、默认值和说明。没有 key、没有任何秘密。"""
    out = []
    for pid, p in PV.PROVIDERS.items():
        ad = PV.ADAPTERS[pid]
        labels = getattr(ad, "region_labels", {})
        regions = [{"id": r, "label": labels.get(r, "Global")} for r in ad.regions]
        v = {"id": pid, "label": p["label"], "default_model": p["default_model"], "default_region": ad.default_region,
             "regions": regions, "region_choice": len(regions) > 1, "notes": PROVIDER_NOTES.get(pid, []),
             "models": [model_view(m, cap) for m in p["models"]]}
        if getattr(ad, "key_pages", None):
            v["key_pages"] = dict(ad.key_pages)
        out.append(v)
    return {"default_provider": PV.DEFAULT_PROVIDER, "default_usd_cap": PV.DEFAULT_USD_CAP, "usd_cap": cap,
            "thinking_levels": list(PV.THINKING_UI), "reasoning_roles": list(PV.REASONING_ROLES),
            "llm_concurrency": LLM_CONCURRENCY, "estimate_note": ESTIMATE_NOTE, "providers": out}

"""假设输入（assumption）：某条路线缺一个没有任何保留数据点能提供的系数时，裁判可以提出它的数值和范围（只提，不算）。
代码校验、按下限加宽区间、在 formula_mc 里采样。校验不过的整条丢弃，原因写进 state.json。

校验规则（validate）：
1. id 必须是 a1..a12 且不重复；每次运行最多 MAX_PER_RUN = 12 条（超出的丢弃）。v2.8d 以前是 a1..a8：冒烟测试 smoke_pizza 的
   修正轮写到 a10，用到 a9 的加总方法被拒，整题没出数。
2. name、unit、rationale 不能为空；value / low / high 都是有限数字（布尔、字符串不算），且 0 < low <= value <= high。
3. 百分数和数据点一样处理：unit 是 % / percent / per cent / pct / percentage 时记为 "%"，代码使用时除以 100。
   v2.5.4（N17）：是不是百分数由 is_pct(unit) 判断：unit 里含 %、percent、per cent、pct、percentage 的都除以 100
   （如 "% of annual live births"），百分点 / 基点（percentage points、pp、bp）不算。只有上面这几种写法改记为 "%"，
   其余保留原文用于显示。
4. 不能是目标量的水平值（target_reason）：name 和 unit 都没有比率类的词（RATIO_WORDS），并且 unit 的实词词干全部落在
   目标 unit 的词干里，或者 name 指向目标实体 + 目标量（ablation.refers_to_target）。v2 还按「提到目标年份」「是目标的
   变化」拒绝，v2.1 去掉了这两条：它们挡住了「去年同期 × 今年变化倍数」这类正常路线（见 AGENT_MVP.md v2.1 节）。
方法层面的规则在 compute.py：每个 formula_mc 至少引用一个保留的观测点（只由假设组成的公式丢弃）；每个方法最多
MAX_PER_METHOD = 6 个假设（v2.8m 以前 3 个）；coverage 为 sum 的方法最多 MAX_PER_SUM = 8 个。

不确定度（effective_range）：P10 / P90 = low / high 的 lognormal。high / low 小于下限时（变化倍数 MIN_WIDTH_CHANGE = 1.25，其余 MIN_WIDTH），以 sqrt(low * high) 为中心、
在对数空间对称放宽到下限。MIN_WIDTH = 2.0：探针 1 里模型给的假设区间 high / low 的中位数约 1.5
（38 / 163 个干脆 low == high），80% 区间只盖住 20% 的答案，所以下限取得比模型的中位数宽。观测点的不确定度不变
（methods.DEFAULT_REL_U，P10 / P90 = v / 1.2, v * 1.2，即 high / low = 1.44）。
"""
import math
import re

from .ablation import refers_to_target, stems

MAX_PER_RUN = 12
MAX_PER_METHOD = 6   # v2.8m：3 -> 6。恒顺题修正 3 轮都卡在「4 个假设」：密度、汇率、「3 年」这类固定数也只能写成假设
MAX_PER_SUM = 8
MIN_WIDTH = 2.0
MIN_WIDTH_CHANGE = 1.25
ID_RE = re.compile(r"a(?:[1-9]|1[0-2])")
PCT_UNITS = {"%", "percent", "per cent", "pct", "percentage", "percent (%)"}
# 百分数单位和百分点 / 基点（N17）：和 discrete.PCT_UNIT / CHANGE_UNIT 同一套写法（测试比对两边的 pattern）。
# 不从 discrete 导入：discrete 导入 compute，compute 导入这里
PCT_RE = re.compile(r"%|\bper ?cent\b|\bpercentage\b|\bpct\b", re.I)
PCT_CHANGE_RE = re.compile(r"\bpercentage[- ]?points?\b|\bpp\b|\bp\.p\.|\bbps?\b|\bbasis[- ]?points?\b", re.I)
RATIO_WORDS = re.compile(r"%|/|\b(?:share|shares|ratio|ratios|rate|rates|per|fraction|proportion|percent|percentage|"
                         r"factor|multiplier|elasticity|coefficient|conversion)\b", re.I)
CHANGE_WORDS = re.compile(r"\b(?:growth|grow|change|changes|yoy|year[- ]over[- ]year|year[- ]on[- ]year|increase|"
                          r"decrease|decline|trend)\b", re.I)
TEXT_FIELDS = ("name", "unit", "rationale", "applies_when", "falsified_by", "route")


def _num(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    x = float(x)
    return x if math.isfinite(x) else None


def is_pct(unit) -> bool:
    """unit 是百分数（代码使用时除以 100）：含 %、percent、per cent、pct、percentage；百分点、基点（变化量）不算。
    只决定换算，不改 unit 的文字。"""
    u = str(unit or "")
    return bool(PCT_RE.search(u)) and not PCT_CHANGE_RE.search(u)


def target_reason(a: dict, target: dict) -> str:
    """返回「这条假设就是目标或它的变相复制」的原因；空串 = 不是。
    v2.1：只拒绝「目标量的水平值」（没有比率词、单位或名字对上目标）。带年份的系数、目标量的变化倍数、占比都允许：
    它们本来就是「去年同期 × 今年变化」这类路线需要的输入（v2 按年份和变化词一律拒绝，把这类路线全挡掉了）；
    任何 formula_mc 仍至少要有一个观测点，所以假设不能单独构成答案。"""
    name, unit = a.get("name", ""), a.get("unit", "")
    both = f"{name} {unit}"
    ratio_like = bool(RATIO_WORDS.search(both)) or is_pct(unit)
    tu, au = stems((target or {}).get("unit", "")), stems(unit)
    if not ratio_like and ((au and tu and au <= tu) or refers_to_target(name, unit, target)):
        return "a level of the target quantity (unit or name matches the target, no ratio wording)"
    return ""


def is_change_factor(a: dict) -> bool:
    """「相对已观测期间的变化倍数」（如 2026 相对 2025 的倍数）：比率类、名字里有变化词。"""
    both = f"{a.get('name', '')} {a.get('unit', '')}"
    return (bool(RATIO_WORDS.search(both)) or is_pct(a.get("unit"))) and bool(CHANGE_WORDS.search(both))


def validate(raw, target: dict) -> dict:
    """raw：裁判 JSON 里的 assumptions 列表。返回 {"kept": [...], "rejected": [...]}，都按原顺序。"""
    kept, rejected, seen = [], [], set()
    for i, x in enumerate(raw if isinstance(raw, list) else []):
        if not isinstance(x, dict):
            rejected.append({"raw": str(x)[:120], "reason": "not an object"})
            continue
        a = {"id": str(x.get("id", "")).strip().lower()[:8]}
        for k in TEXT_FIELDS:
            a[k] = str(x.get(k) or "").strip()[:300]
        a["value"], a["low"], a["high"] = (_num(x.get(k)) for k in ("value", "low", "high"))
        if a["unit"].lower() in PCT_UNITS:
            a["unit"] = "%"
        why = ""
        if not ID_RE.fullmatch(a["id"]):
            why = "id must be a1..a12"
        elif a["id"] in seen:
            why = "duplicate id"
        elif len(kept) >= MAX_PER_RUN:
            why = f"more than {MAX_PER_RUN} assumptions"
        elif not (a["name"] and a["unit"] and a["rationale"]):
            why = "name, unit and rationale are required"
        elif None in (a["value"], a["low"], a["high"]):
            why = "value, low and high must be numbers"
        elif not (0 < a["low"] <= a["value"] <= a["high"]):
            why = "need 0 < low <= value <= high"
        else:
            why = target_reason(a, target)
            if why:
                why = f"target-like: {why}"
        if why:
            rejected.append({**a, "reason": why})
            continue
        seen.add(a["id"])
        lo, hi, widened = effective_range(a)
        kept.append({**a, "is_pct": is_pct(a["unit"]), "p10_used": lo, "p90_used": hi, "widened_by_floor": widened})
    return {"kept": kept, "rejected": rejected}


def effective_range(a: dict) -> tuple:
    """(P10, P90, 是否被下限放宽)，单位换算后（% 已除以 100）。
    变化倍数用 MIN_WIDTH_CHANGE（1.25，约 ±11%）：它围绕 1 附近，2 倍下限会把区间撑到 ±40%，失去意义；其余用 MIN_WIDTH。"""
    f = 0.01 if is_pct(a.get("unit")) else 1.0
    lo, hi = a["low"] * f, a["high"] * f
    w = MIN_WIDTH_CHANGE if is_change_factor(a) else MIN_WIDTH
    if hi / lo >= w:
        return lo, hi, False
    c = math.sqrt(lo * hi)
    return c / math.sqrt(w), c * math.sqrt(w), True

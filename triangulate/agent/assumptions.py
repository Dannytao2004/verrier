"""假设输入（assumption）：某条路线缺一个没有任何保留数据点能提供的系数时，裁判可以提出它的数值和范围（只提，不算）。
代码校验、按下限加宽区间、在 formula_mc 里采样。校验不过的整条丢弃，原因写进 state.json。

校验规则（validate）：
1. id 必须是 a1..a8 且不重复；每次运行最多 MAX_PER_RUN = 8 条（超出的丢弃）。
2. name、unit、rationale 不能为空；value / low / high 都是有限数字（布尔、字符串不算），且 0 < low <= value <= high。
3. 百分数和数据点一样处理：unit 是 % / percent / per cent / pct / percentage 时记为 "%"，代码使用时除以 100。
4. 不能是目标本身或它的变相复制（target_reason），三条任一成立就丢弃：
   a. name 或 unit 提到目标期间的年份（目标 period_start..period_end 覆盖的四位年份），或 this year / current year /
      this month / current month / next month：假设应当是可迁移的关系，不是目标期间的数值；
   b. 是目标量的水平值：unit 的实词词干全部落在目标 unit 的词干里，或者 name 指向目标实体 + 目标量
      （ablation.refers_to_target）；并且 name 和 unit 都没有比率类的词（RATIO_WORDS）；
   c. 是目标量的变化：name 含 growth / change / yoy 等（CHANGE_WORDS），且和目标 what 至少共享一个实词词干。
   规则是保守的启发式，宁可多丢；换了说法的变相目标仍可能漏过（记在残余风险里）。
方法层面的规则在 compute.py：每个 formula_mc 至少引用一个保留的观测点（只由假设组成的公式丢弃）；每个方法最多
MAX_PER_METHOD = 3 个假设。

不确定度（effective_range）：P10 / P90 = low / high 的 lognormal。high / low < MIN_WIDTH 时，以 sqrt(low * high) 为中心、
在对数空间对称放宽到 high / low = MIN_WIDTH。MIN_WIDTH = 2.0：探针 1 里模型给的假设区间 high / low 的中位数约 1.5
（38 / 163 个干脆 low == high），80% 区间只盖住 20% 的答案，所以下限取得比模型的中位数宽。观测点的不确定度不变
（methods.DEFAULT_REL_U，P10 / P90 = v / 1.2, v * 1.2，即 high / low = 1.44）。
"""
import math
import re

from .ablation import refers_to_target, stems
from .evidence import parse_date

MAX_PER_RUN = 8
MAX_PER_METHOD = 3
MIN_WIDTH = 2.0
ID_RE = re.compile(r"a[1-8]")
PCT_UNITS = {"%", "percent", "per cent", "pct", "percentage", "percent (%)"}
RATIO_WORDS = re.compile(r"%|/|\b(?:share|shares|ratio|ratios|rate|rates|per|fraction|proportion|percent|percentage|"
                         r"factor|multiplier|elasticity|coefficient|conversion)\b", re.I)
CHANGE_WORDS = re.compile(r"\b(?:growth|grow|change|changes|yoy|year[- ]over[- ]year|year[- ]on[- ]year|increase|"
                          r"decrease|decline|trend)\b", re.I)
RELATIVE_PERIOD = re.compile(r"\b(?:this|current|next)\s+(?:year|month|season|quarter)\b", re.I)
TEXT_FIELDS = ("name", "unit", "rationale", "applies_when", "falsified_by", "route")


def _num(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    x = float(x)
    return x if math.isfinite(x) else None


def target_years(target: dict) -> list:
    ps = parse_date((target or {}).get("period_start"))
    pe = parse_date((target or {}).get("period_end"), end=True)
    if pe is None:
        return []
    return list(range((ps or pe).year, pe.year + 1))


def target_reason(a: dict, target: dict) -> str:
    """返回「这条假设就是目标或它的变相复制」的原因；空串 = 不是。规则见模块说明第 4 条。"""
    name, unit = a.get("name", ""), a.get("unit", "")
    both = f"{name} {unit}"
    for y in target_years(target):
        if re.search(rf"(?<!\d){y}(?!\d)", both):
            return f"names the target period ({y})"
    if RELATIVE_PERIOD.search(both):
        return "names the target period (relative wording)"
    ratio_like = bool(RATIO_WORDS.search(both)) or a.get("unit") == "%"
    tu, au = stems((target or {}).get("unit", "")), stems(unit)
    if not ratio_like and ((au and tu and au <= tu) or refers_to_target(name, unit, target)):
        return "a level of the target quantity (unit or name matches the target, no ratio wording)"
    if CHANGE_WORDS.search(name) and stems(name) & stems((target or {}).get("what", "")):
        return "a change of the target quantity (disguised copy of the target)"
    return ""


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
            why = "id must be a1..a8"
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
        kept.append({**a, "is_pct": a["unit"] == "%", "p10_used": lo, "p90_used": hi, "widened_by_floor": widened})
    return {"kept": kept, "rejected": rejected}


def effective_range(a: dict) -> tuple:
    """(P10, P90, 是否被下限放宽)，单位换算后（% 已除以 100）。"""
    f = 0.01 if a.get("unit") == "%" else 1.0
    lo, hi = a["low"] * f, a["high"] * f
    if hi / lo >= MIN_WIDTH:
        return lo, hi, False
    c = math.sqrt(lo * hi)
    return c / math.sqrt(MIN_WIDTH), c * math.sqrt(MIN_WIDTH), True

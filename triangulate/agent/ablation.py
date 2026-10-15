"""--ablate-own-history（回测消融）：去掉目标自身的历史，看 agent 还能不能估、差多少。另外放「一个名字是不是在说目标」
的通用判断，假设校验（assumptions.py）也用它。全部是代码规则，不调模型。

消融做三件事：
1. plan 的候选方向里去掉 own_history（名额留给别的类别）；裁判第一轮追加的 own_history 方向也去掉。
2. 排除「目标自身在更早期间的值」，规则保守（宁可多排除）：
   a. 来自 own_history 方向的点（正常情况下第 1 步之后已经没有）；
   b. 名字指向「目标实体 + 目标量」的点：name 里有目标的实体锚词（见 entity_anchors），而且 name 或 unit 里有
      目标 unit 的词干（见 quantity_stems；目标 unit 没有实词时只看锚词）。
   被排除的点不进裁判的表格（裁判看不到它们的值），state 里保留并标原因。
3. 只允许不需要 target_history 的方法（ALLOWED_METHODS，目前只有 formula_mc）；裁判看到的方法库说明也只列这些方法。

残余风险见 RESIDUAL_RISKS（写进 state.json 的 ablation 记录）。
"""
import calendar
import re

from .prompts import METHODS_SPEC

ALLOWED_METHODS = {"formula_mc"}
RESIDUAL_RISKS = [
    "Own values named by an alias or abbreviation, or with no entity in the point name, are not excluded.",
    "The rule over-excludes on purpose: any point naming the target entity together with the target quantity "
    "(for example a survey of the target's visitors) is excluded, even when it is not a value of the target itself.",
    "The model's own memory of the target's history is not removed: it can still shape the plan, the judge's choices "
    "and assumption values.",
    "The searcher and the extractor still see pages that contain own values; only the judge's table is filtered.",
]

# 通用的停用词：功能词和到处都有的统计用语。只用来算词干，不含任何领域词。
STOP = {"the", "a", "an", "of", "in", "on", "at", "to", "for", "by", "from", "with", "as", "and", "or", "is", "are", "be",
        "its", "it", "this", "that", "which", "who", "into", "over", "under", "per", "all", "each", "via", "s",
        "number", "total", "count", "counts", "counted", "reported", "report", "reports", "official", "data",
        "statistics", "statistic", "monthly", "annual", "yearly", "daily", "weekly", "quarterly", "month", "months",
        "year", "years", "week", "weeks", "day", "days", "quarter", "period", "value", "values", "estimate", "level",
        "unit", "units"}
# 通用的专名「类别词」：许多领域的专名里都有（某某公园、某某机场、某某公司），单独不能指认一个实体，所以不当锚词。
DESIGNATORS = {"national", "international", "federal", "state", "states", "united", "county", "city", "town", "village",
               "park", "parks", "airport", "port", "river", "lake", "mount", "mountain", "island", "islands", "valley",
               "north", "south", "east", "west", "northern", "southern", "eastern", "western", "central", "new",
               "great", "saint", "st", "company", "corporation", "corp", "inc", "ltd", "llc", "plc", "group",
               "holdings", "bank", "university", "college", "school", "hospital", "department", "ministry", "office",
               "bureau", "agency", "service", "services", "authority", "council", "commission", "association",
               "institute", "center", "centre", "museum", "station", "region", "province", "district", "republic",
               "kingdom", "system", "public"}
_CALENDAR = {m.lower() for m in calendar.month_name if m} | {m.lower() for m in calendar.month_abbr if m} | \
            {d.lower() for d in calendar.day_name} | {"sept"}
_WORD = re.compile(r"[A-Za-z][A-Za-z'’&.-]*[A-Za-z]|[A-Za-z]")


def _tokens(text: str) -> list:
    out = []
    for t in _WORD.findall(text or ""):
        t = re.sub(r"['’]s$", "", t).strip(".-'’")
        out += [x for x in re.split(r"[-.]", t) if x] if "-" in t else [t]
    return out


def stem(tok: str) -> str:
    """简单词干：小写，长度 >= 5 的词取前 5 个字母（visits / visitors / visit -> visit）。"""
    t = tok.lower()
    return t[:5] if len(t) >= 5 else t


def stems(text: str) -> set:
    return {stem(t) for t in _tokens(text) if t.lower() not in STOP and len(t) >= 2}


def _head(what: str) -> str:
    """目标 what 的第一个子句：第一个逗号、分号、括号或 ' as ' 之前。"""
    return re.split(r"[,;(]|\s+as\s+", what or "", maxsplit=1)[0]


def _anchors_in(text: str) -> list:
    toks = _tokens(text)
    runs, cur = [], []
    for i, t in enumerate(toks):
        if t[:1].isupper():
            cur.append((i, t))
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    out = []
    for run in runs:
        if run[0][0] == 0 and len(run) == 1:
            continue  # 句首单个大写词只是语法
        for _, t in run:
            lo = t.lower()
            if lo not in DESIGNATORS and lo not in _CALENDAR and lo not in STOP and lo not in out:
                out.append(lo)
    return out


def entity_anchors(target: dict) -> list:
    """目标的实体锚词：what 第一个子句里大写开头的词组成的专名短语中，去掉句首单个大写词、通用类别词（DESIGNATORS）、
    月份和星期名之后剩下的词（小写）。第一个子句里找不到时用整个 what。
    例：'Recreation visits to Yellowstone National Park, as counted by ...' -> ['yellowstone']；
    'Heathrow Airport passenger traffic in July' -> ['heathrow']。"""
    what = str((target or {}).get("what", ""))
    return _anchors_in(_head(what)) or _anchors_in(what)


def quantity_stems(target: dict) -> set:
    """目标量的词干：目标 unit 的实词词干（'recreation visits (person-visits)' -> {recre, visit, perso}）。"""
    return stems(str((target or {}).get("unit", "")))


def refers_to_target(name: str, unit: str, target: dict) -> bool:
    """name 里有目标的实体锚词，而且 name 或 unit 里有目标量的词干（目标 unit 没有实词时只看锚词）。
    没有锚词时返回 False（无法判断实体；记在残余风险里）。"""
    anchors = entity_anchors(target)
    low = (name or "").lower()
    if not anchors or not any(re.search(rf"(?<![a-z]){re.escape(a)}(?![a-z])", low) for a in anchors):
        return False
    q = quantity_stems(target)
    return not q or bool((stems(name) | stems(unit)) & q)


def own_value_reason(point: dict, target: dict, directions: dict) -> str:
    """返回排除原因；空串 = 不排除。directions: id -> direction（看点来自哪一类方向）。"""
    d = directions.get(point.get("direction_id")) or {}
    if d.get("category") == "own_history":
        return "ablation: point from an own_history direction"
    if refers_to_target(point.get("name", ""), point.get("unit", ""), target):
        return f"ablation: name refers to the target entity {entity_anchors(target)} and quantity"
    return ""


def methods_spec() -> str:
    """消融时给裁判的方法库说明：只留不需要 target_history 的方法（逐字取自 METHODS_SPEC，只删行）。"""
    drop = ("- series_naive", "- yoy_scaling", "- linear_fit", "- ratio", "Series rules")
    return "\n".join(line for line in METHODS_SPEC.splitlines() if not line.startswith(drop))

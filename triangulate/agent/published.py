"""「答案已公布」（v2.4）：真实使用时（as_of = 今天、题目没有登记真值），保留的数据点里可能就有目标本身
（同一对象、同一量、同一期间，as_of 当天或之前已公布）。ask_fa4b4c74（英国 2026 年 9 月新车注册）：SMMT 的 350,518
被找到并保留了，却和「去年同月」方法按 50/50 平均成了 331,271。

1. 候选（代码，candidates）：裁判看过并保留的点里，同时满足
   - 期间 = 目标期间：同一年、期末差 <= 3 天、期长差 <= 3 天（compute._same_calendar）；
   - name 里有目标的实体词（entity_terms：目标 what 第一个子句里大写开头的专名词组——整个词组、首字母缩写、
     其中不是通用类别词的词——以及 what 里的全大写缩写；不算量的名字和发布方，见 entity_terms；一个都没有时不查这一条，
     说明里写 no entity constraint）；
   - name 或 unit 和目标量有共同词干（measure_stems：目标 unit 和 what 第一个子句里的实词）；
   - 单位同为 % 或同不为 %；unit 不是百分点 / 基点（变化量）；name 不说概率、预测、预期、变化（NOT_VALUE）；
   - v2.4.1：页面日期（快照 = 快照日期）和页面写明的发布日期都不早于目标期末（_dated_before）；quote 里数值所在的
     那一段不说预测 / 预期（_forecast_quote）。
   代码只做粗筛（实体词那一条尤其粗：别的实体仍可能通过）：漏掉的后果是照旧估计（v2.3 的行为），多放的由下一步的模型拒掉。
   name 和目标量共同词干多的排前面，最多 MAX_CANDIDATES 个。
2. 确认（模型，一次调用，形式同输入核对）：每个候选是不是目标本身；模型只回 id、verdict（target / different）和理由，
   数字一律取自数据点，不由模型写。
3. 结果（代码，resolve）：确认的点数值一致（相对差 <= REL_TOL）= published，报其中一个
   （先取 name 或 quote 提到目标发布方的，再取 value_as_written 位数多的，再取编号靠前的）；不一致 = conflict，不改结果、终稿后面附一句。
   连续值：compute.result 换成这个值（basis published，没有区间），原来的组合估计留在 compute.estimate_result，
   终稿里作参考列出、不混合。离散：值落在裁判的结果列表里（先找相等，再找合并的尾部）就报这个结果 resolved。
   终稿由代码写（final_text），不调终稿模型。
回测和留出测试（as_of 早于今天，或题目登记了真值）不检查（status not_checked），不调模型：那时目标值不可能在 as_of 前公布。
4. v2.5 提前停（EarlyWatch，只在真实使用、连续值目标时）：子 agent 每核对完一页，就把这一页的新点按上面 1–3 检查一次
   （候选不要求裁判看过；只送新点，送过的不再送）。第一次确认出 published 就停下其余子 agent，跳过裁判和估计，
   终稿写明没有做估计；确认的值互相矛盾就不再提前检查，照常走裁判、估计和上面的检查。
   v2.5.2：一次检查出错（transport / 输出无效 / 预算），它的候选和下一页的候选一起再送一次。
"""
import json
import math
import re
import threading
import time
import urllib.parse
from datetime import datetime, timezone

from . import ablation as AB
from . import compute as C
from . import discrete as D
from .evidence import find_value, parse_date
from .prompts import PUBLISHED_SYSTEM, PUBLISHED_USER

MAX_CANDIDATES = 20
REL_TOL = 0.005
NOT_VALUE = re.compile(r"forecast|project(?:ed|ion)|predict|expect|consensus|outlook|guidance|scenario|probab|\bodds\b|"
                       r"\bchances?\b|likelihood|implied|\bpriced\b|\bchanges?\b|\bgrowth\b|\bincreases?\b|\bdecreases?\b|"
                       r"\bdeclines?\b|\bdifference\b|year[- ]on[- ]year|\byoy\b|\by/y\b", re.I)
# quote 里数值所在那一段的预测 / 预期词（v2.4.1）。不含涨跌词：实际值的 quote 常写「rose 12% to 350,536」。
FORECAST_NEAR = re.compile(r"\bforecast|\bproject(?:ed|ion)|\bpredict|\bexpect|\bconsensus|\banticipat|\boutlook|"
                           r"\bwill be\b|\bon track\b", re.I)
_CLAUSE = re.compile(r",\s|;|:|\(|\)|[.!?](?:\s|$)|\s[-–—]\s")   # 千分位逗号后面没有空格，不算分段
PREPS = {"of", "in", "for", "at", "on"}
NOT_CHECKED = ("not checked: backtest or scored question (as_of before today, or an official value is registered), so the "
               "target cannot have been published by as_of")
POINT_KEYS = ("id", "name", "value", "value_as_written", "unit", "period_start", "period_end", "source_url", "via",
              "page_date", "published_at_if_visible", "quote")


def _fmt(v) -> str:
    if v is None or not isinstance(v, (int, float)) or not math.isfinite(v):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:.4g}"


def _with_unit(v, unit: str) -> str:
    return f"{_fmt(v)}%" if unit == "%" else f"{_fmt(v)} {unit}".strip()


def _runs(text: str) -> list:
    """大写开头的连续词组成的词组（去掉句首单个大写词）：[(起始位置, 词组, 词组后面那个词)]。"""
    toks = AB._tokens(text)
    runs, cur = [], []
    for i, t in enumerate(toks + [""]):
        if t[:1].isupper():
            cur.append(i)
            continue
        if cur:
            runs.append((cur[0], [toks[j] for j in cur], t))
        cur = []
    return [r for r in runs if not (r[0] == 0 and len(r[1]) == 1)]


def _run_terms(run: list) -> set:
    words = [w for w in run if w.lower() not in AB.STOP and w.lower() not in AB._CALENDAR]
    out = {w.lower() for w in words if len(w) >= 2 and w.lower() not in AB.DESIGNATORS}
    if len(words) >= 2:
        out |= {" ".join(words).lower(), "".join(w[0] for w in words).lower()}
    return out


def entity_terms(target: dict) -> list:
    """目标的实体词（小写，按词边界在点的 name 里找）：what 第一个子句里的大写专名词组，加上 what 里的全大写缩写。
    v2.4.1 去掉两类不是实体的词：
    - 量的名字：句首的大写词组后面紧跟 of / in / for / at / on、后面还有别的专名词组时（'Real GDP of France'），
      它的词、整个词组、缩写都不算，what 里同样的全大写缩写（GDP）也不算；
    - 只从第一个子句以外来的发布方写法（publisher_terms）：发布方不是实体（'..., as reported by SMMT'：SMMT 也报苏格兰）。
      第一个子句的专名词组里的不去（'the next FOMC meeting'、'Deliveries of Tesla vehicles'：发布方就是实体）。
    'New passenger car registrations in the United Kingdom, as reported by SMMT' -> ['uk', 'united kingdom']。
    仍只是粗筛：量的缩写不在句首词组里（'France real GDP' 的 GDP）、实体不大写或不写时，别的实体仍可能通过，由模型拒。"""
    what = str((target or {}).get("what", ""))
    runs = [(s, _run_terms(r), nxt) for s, r, nxt in _runs(AB._head(what))]
    measure = set()
    if runs and runs[0][0] == 0 and runs[0][2].lower() in PREPS and runs[0][1] and any(t for _, t, _ in runs[1:]):
        measure = runs.pop(0)[1]
    heads = set().union(*(t for _, t, _ in runs))
    caps = {a.lower() for a in re.findall(r"\b[A-Z]{2,}\b", what)}
    return sorted(heads | (caps - measure - set(publisher_terms(target))))


def publisher_terms(target: dict) -> list:
    """目标发布方的写法（小写）：全名（括号前）和全大写缩写。'Society of Motor Manufacturers and Traders (SMMT)' ->
    ['society of motor manufacturers and traders', 'smmt']。"""
    pub = str((target or {}).get("publisher", ""))
    full = " ".join(AB._head(pub).split()).lower()
    return [x for x in [full] if len(x) >= 3] + [a.lower() for a in re.findall(r"\b[A-Z]{2,}\b", pub)]


def _mstem(t: str) -> str:
    t = t.lower()
    t = t[:-1] if len(t) > 3 and t.endswith("s") else t
    return t[:5]


def measure_stems(target: dict) -> set:
    """目标量的词干：目标 unit 和 what 第一个子句里的实词，去掉停用词、月份、通用类别词（United、Kingdom、National ...）。
    大写词也算（「Bank Rate」的 Rate 就是量）；实体名的词干因此也在里面，只会多放候选、由模型拒掉。"""
    toks = AB._tokens(str((target or {}).get("unit", ""))) + AB._tokens(AB._head(str((target or {}).get("what", ""))))
    return {_mstem(t) for t in toks if len(t) >= 3 and t.lower() not in AB.STOP | AB._CALENDAR | AB.DESIGNATORS}


def _is_pct(unit: str) -> bool:
    return unit.strip() == "%" or bool(D.PCT_UNIT.search(unit))


def _dated_before(p: dict, tpe) -> bool:
    """页面日期（快照 = 快照日期）或页面写明的发布日期早于目标期末：那时目标值还不可能公布，这个数只能是预测 / 预告。
    日期不完整时取最晚的可能日期（'2026-09' -> 9 月 30 日），只排除肯定早于期末的。"""
    return any(d is not None and d < tpe
               for d in (parse_date(p.get(k), end=True) for k in ("page_date", "published_at_if_visible")))


def _forecast_quote(p: dict) -> bool:
    """quote 里数值所在的那一段（逗号、分号、冒号、括号、句末标点、破折号之间）说预测 / 预期：
    'SMMT expects around 340,000 new cars to be registered in September'。同一句别的段（'..., better than expected'）不算。"""
    q, vw = str(p.get("quote") or ""), str(p.get("value_as_written") or "")
    i = find_value(q, vw) if vw else -1
    if i < 0:
        return False
    a = max((m.end() for m in _CLAUSE.finditer(q[:i])), default=0)
    m = _CLAUSE.search(q, i + len(vw))
    return bool(FORECAST_NEAR.search(q[a:m.start() if m else len(q)]))


def candidates(points: list, target: dict, as_of, judged_only: bool = True) -> tuple:
    """(候选点, 说明)。只看裁判看过并保留的点（judged_only=False：v2.5 提前停，裁判还没看过）；规则见模块说明。"""
    tps = parse_date((target or {}).get("period_start"))
    tpe = parse_date((target or {}).get("period_end"), end=True)
    if tpe is None:
        return [], "target period_end unparseable"
    if tpe > as_of:
        return [], f"target period ends {tpe}, after as_of: it cannot have been published yet"
    tps = tps or tpe
    terms, stems_t = entity_terms(target), measure_stems(target)
    t_pct = _is_pct(str((target or {}).get("unit", "")))
    out, early = [], 0
    for p in points or []:
        if (judged_only and not (p.get("keep") and p.get("judged_round"))) or p.get("ablation_excluded"):
            continue
        v, name, unit = p.get("value"), str(p.get("name") or ""), str(p.get("unit") or "")
        if not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v):
            continue
        ps, pe = C._span(p)
        if pe is None or pe.year != tpe.year or not C._same_calendar(ps, pe, tps, tpe):
            continue
        if _dated_before(p, tpe) or _forecast_quote(p):
            early += 1
            continue
        low = name.lower()
        if terms and not any(re.search(rf"(?<![a-z]){re.escape(t)}(?![a-z])", low) for t in terms):
            continue
        if stems_t and not ({_mstem(t) for t in AB._tokens(f"{name} {unit}")} & stems_t):
            continue
        if _is_pct(unit) != t_pct or D.CHANGE_UNIT.search(unit) or NOT_VALUE.search(f"{name} {unit}"):
            continue
        out.append((len({_mstem(t) for t in AB._tokens(name)} & stems_t), p))
    # 和目标量共同词干多的排前面（「UK new car registrations」先于「UK fleet registrations」），一样多按编号
    out = [p for _, p in sorted(out, key=lambda x: (-x[0], _order(x[1])))]
    note = (f"{len(out)} candidate(s); entity terms {terms or 'none (no entity constraint)'}; "
            f"measure stems {sorted(stems_t)}")
    if early:
        note += (f"; {early} point(s) for the target period excluded as dated before the period end or quoted "
                 f"as a forecast")
    if len(out) > MAX_CANDIDATES:
        note += f"; only the first {MAX_CANDIDATES} sent to the check"
    return out[:MAX_CANDIDATES], note


def _order(p: dict) -> int:
    m = re.search(r"\d+", str(p.get("id", "")))
    return int(m.group()) if m else 0


def _via(p: dict) -> str:
    if p.get("via") == "snapshot":
        return f"archived snapshot {p.get('page_date')}"
    return f"{p.get('via')} page dated {p.get('page_date') or '?'}"


def candidate_line(p: dict) -> str:
    dom = urllib.parse.urlsplit(p.get("source_url", "")).netloc
    return (f'- {p["id"]}: "{p.get("name")}" = {_fmt(p.get("value"))} {p.get("unit", "")}, period '
            f'{p.get("period_start") or "?"}..{p.get("period_end") or "?"}, source {dom} ({_via(p)}), publication date '
            f'{p.get("published_at_if_visible") or "not stated"}; quote: "{p.get("quote", "")}"')


def prompt(target: dict, as_of: str, cands: list) -> tuple:
    """(system, user)。target 用 plan 的 target（不带裁判写的结果列表依据说明）。"""
    return PUBLISHED_SYSTEM, PUBLISHED_USER.format(target=json.dumps(target, ensure_ascii=False, default=str), as_of=as_of,
                                                   candidates="\n".join(candidate_line(p) for p in cands))


def _summary(p: dict) -> dict:
    return {k: p.get(k) for k in POINT_KEYS} | {"domain": urllib.parse.urlsplit(p.get("source_url", "")).netloc}


def resolve(reply, cands: list, target: dict) -> dict:
    """模型回复 + 候选 -> 记录。target 是带裁判结果列表的 target（离散时用来找结果）。"""
    by_id = {p["id"]: p for p in cands}
    verdicts = {}
    raw = reply.get("candidates") if isinstance(reply, dict) else None
    for x in raw if isinstance(raw, list) else []:
        i = str(x.get("id")) if isinstance(x, dict) else ""
        if i in by_id and i not in verdicts:
            verdicts[i] = {"verdict": str(x.get("verdict", "")).strip().lower(), "reason": str(x.get("reason", ""))[:300]}
    conf = [p for p in cands if verdicts.get(p["id"], {}).get("verdict") == "target"]
    rec = {"status": "not_confirmed", "confirmed_ids": [p["id"] for p in conf],
           "candidates": [_summary(p) | verdicts.get(p["id"], {"verdict": "no verdict", "reason": ""}) for p in cands]}
    if not conf:
        return rec
    v0 = conf[0]["value"]
    if any(abs(p["value"] - v0) > REL_TOL * max(abs(v0), abs(p["value"])) for p in conf):
        rec.update(status="conflict", values={p["id"]: p["value"] for p in conf})
        return rec
    pub = publisher_terms(target)
    best = max(conf, key=lambda p: (any(t in f"{p.get('name')} {p.get('quote')}".lower() for t in pub),
                                    len(re.sub(r"\D", "", str(p.get("value_as_written") or ""))), -_order(p)))
    rec.update(status="published", id=best["id"], value=best["value"], unit=best.get("unit", ""),
               date=best.get("published_at_if_visible") or best.get("page_date"), point=_summary(best),
               reason=verdicts[best["id"]]["reason"], outcome=None)
    if D.is_discrete(target):
        outs = (target or {}).get("outcomes") or []
        rec["outcome"] = next((o["label"] for t in (False, True) for o in outs if D._matches(o, best["value"], t)), None)
        rec["outcome_list"] = bool(outs)
    return rec


def result(rec: dict, est: dict, target: dict) -> dict:
    """已公布时 compute.result 换成这个值；est（原来的组合估计）由调用方另存为 compute.estimate_result。"""
    src = {k: rec.get(k) for k in ("id", "value", "unit", "date")} | {"source_url": (rec.get("point") or {}).get("source_url")}
    base = {"central": rec["value"], "p10": None, "p90": None, "weights": {}, "weight_basis": {}, "basis": "published",
            "assumption_weight_share": 0, "published": src}
    if not D.is_discrete(target):
        return base | {"weight_rule": "none: published value (estimation methods kept for reference, not blended)"}
    lab = rec.get("outcome")
    outs = (est or {}).get("outcomes") or [dict(o) for o in (target or {}).get("outcomes") or []]
    return base | {"mode": "discrete", "resolved": True, "weight_rule": "none: resolved by a published value",
                   "outcomes": [{**o, "prob": (1.0 if o["label"] == lab else 0.0) if lab else None} for o in outs],
                   "most_likely": lab or f"{_with_unit(rec['value'], rec.get('unit', ''))} (published; not in the outcome list)",
                   "most_likely_prob": 1.0 if lab else None}


def _evidence_lines(rec: dict) -> list:
    p = rec.get("point") or {}
    others = [i for i in rec.get("confirmed_ids") or [] if i != rec.get("id")]
    pub = f", publication date {p['published_at_if_visible']}" if p.get("published_at_if_visible") else ""
    return [f"Source: data point {p.get('id')} \"{p.get('name')}\" (period {p.get('period_start')}..{p.get('period_end')}), "
            f"from {p.get('domain')} ({_via(p)}{pub}), quoting: \"{p.get('quote')}\"",
            "A separate model check confirmed that this data point has the pinned target's entity, measure and period and "
            "is a reported value, not a forecast; the number is taken from the data point by code."
            + (f" Also confirmed with the same value: {', '.join(others)}." if others else "")]


def final_text(state: dict) -> dict:
    """已公布时的终稿：全部由代码写（不调终稿模型）。连续值报这个值；离散报它落在哪个结果上。估计方法的结果只作参考列出。"""
    rec = state.get("published") or {}
    comp = state.get("compute") or {}
    est = comp.get("estimate_result") or {}
    target = (state.get("plan") or {}).get("target") or {}
    v = _with_unit(rec.get("value"), rec.get("unit", ""))
    if D.is_discrete(target):
        lab = rec.get("outcome")
        head = (f"Resolved: the target resolves to outcome '{lab}' (published value {v}), so this is a reported result, "
                f"not a probability estimate." if lab else
                f"Resolved by a published value: {v}; it matches none of the outcomes in the judge's list."
                if rec.get("outcome_list") else f"Resolved by a published value: {v} (the judge defined no outcome list).")
        probs = [f"{o['label']} {100 * o['prob']:.1f}%" for o in est.get("outcomes") or [] if o.get("prob") is not None]
        ref = (f"For reference only (not blended with the published result): the estimation methods gave these outcome "
               f"probabilities: {'; '.join(probs)}." if est.get("most_likely") is not None and probs else
               "For reference: the estimation methods produced no outcome probabilities.")
    else:
        head = (f"Published value: {v}. This is the pinned target itself (period {target.get('period_start')}.."
                f"{target.get('period_end')}) as already published, not an estimate.")
        n = sum(1 for m in comp.get("methods") or [] if m.get("estimate"))
        ref = (f"For reference only (not blended with the published value): the estimation methods gave "
               f"{_fmt(est.get('central'))} (80% interval {_fmt(est.get('p10'))} to {_fmt(est.get('p90'))}) from {n} "
               f"method(s)." if est.get("central") is not None else
               "For reference: the estimation methods produced no estimate.")
        if rec.get("early_stop"):   # v2.5 提前停：没有做估计
            ref = EARLY_NO_ESTIMATE
    text = "\n\n".join([head, "\n".join(_evidence_lines(rec)), ref,
                        f"A published figure can be revised later; this answer reports it as published by {state.get('as_of')}."])
    return {"template": text, "text": text, "placeholders": {}, "digits_removed": 0, "model_error": None,
            "used_model_text": False, "written_by": "code (published value)"}


def conflict_note(rec: dict) -> str:
    vals = "; ".join(f"{i} = {_fmt(v)}" for i, v in (rec.get("values") or {}).items())
    return (f"Note: kept data points {', '.join(rec.get('confirmed_ids') or [])} were each confirmed as the published "
            f"target value, but their values disagree ({vals}); code reports the estimate above instead of choosing "
            f"between them.")


EARLY_NO_ESTIMATE = ("No estimate was made: the run stopped as soon as this published value was confirmed, so the remaining "
                     "sub-agents, the judge and the estimation methods were skipped.")
EARLY_ROLE = "published:early"


class EarlyWatch:
    """v2.5 提前停（只在真实使用时由 run.prepare_run 放进 ctx.early；回测没有它）。子 agent 每核对完一页调 offer：
    这一页的新点编临时 id（e1, e2 ...），按 candidates(judged_only=False) 选候选，有候选就问一次确认模型（prompt 同 v2.4），
    resolve 判定。published：记下、stop.set()，其余子 agent 看到就停；conflict：不再提前检查（照常走裁判、估计和 v2.4 的
    检查）。离散目标不提前停（结果列表由裁判定义）。检查一个接一个做（锁），已送过的点不再送；
    v2.5.2：出错的那次检查的候选不算送过，下一次检查一起送（否则后一页一确认就停，出错页上矛盾的值没人看）。"""

    def __init__(self):
        self.stop = threading.Event()
        self.stop_reason = "stopped early: the published target value was confirmed"
        self._lock = threading.Lock()
        self.n = 0
        self.keys = {}      # 临时 id -> (direction_id, order, source_url)：裁判节点用它换成 p 编号
        self.checks = []
        self.rec = None     # 确认出 published 的那次 resolve 记录（临时 id）
        self.off = ""       # 不再提前检查的原因
        self.pending = []   # v2.5.2：出错（transport / 输出无效 / 预算）的检查的候选，下一次检查一起重送

    def offer(self, llm, qid: str, target: dict, as_of_s: str, as_of, points: list):
        if not points or self.stop.is_set() or self.off or D.is_discrete(target):
            return
        from .pipeline import BudgetExceeded
        with self._lock:
            if self.stop.is_set() or self.off:
                return
            tagged = []
            for p in points:
                self.n += 1
                self.keys[f"e{self.n}"] = (p["direction_id"], tuple(p["order"]), p["source_url"])
                tagged.append({**p, "id": f"e{self.n}"})
            resent = [p["id"] for p in self.pending]
            cands, note = candidates(self.pending + tagged, target, as_of, judged_only=False)
            if not cands:
                return
            if resent:
                note += f"; re-sent {len(resent)} candidate(s) from failed early check(s)"
            chk = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "n_points": len(tagged),
                   "direction_id": tagged[0]["direction_id"], "source_url": tagged[0]["source_url"], "note": note,
                   "resent_ids": resent}
            system, user = prompt(target, as_of_s, cands)
            t0 = time.time()
            try:
                out, err = llm.ask(system, user, role=EARLY_ROLE, qid=qid, max_tokens=3000)
            except BudgetExceeded as e:
                out, err = None, str(e)
            chk["wall_s"] = round(time.time() - t0, 2)
            if out is None:   # 这些候选没人看过：留到下一次检查一起送，让 resolve 看得到互相矛盾的值
                self.pending = cands
                self.checks.append({**chk, "status": "error", "error": err, "candidates": [_summary(p) for p in cands]})
                return
            self.pending = []
            rec = resolve(out, cands, target)
            self.checks.append({**chk, **rec})
            if rec["status"] == "published":
                self.rec = {**rec, "note": note}
                self.stop.set()
            elif rec["status"] == "conflict":
                self.off = (f"early check off: confirmed values disagree ({rec.get('values')}); the judge, the estimate "
                            f"and the v2.4 check run as usual")

    def record(self, idmap: dict) -> dict:
        """写进 state["published_early"]：每次检查（临时 id 换成 p 编号，原 id 留在 early_id）。"""
        status = "published" if self.rec else ("off" if self.off else "not_confirmed")
        by = {}
        for c in self.checks:
            by[c["status"]] = by.get(c["status"], 0) + 1
        return {"status": status, "off": self.off, "n_checks": len(self.checks), "by_status": by,
                "n_error": by.get("error", 0), "checks": [renumber(c, idmap) for c in self.checks]}


def renumber(rec: dict, idmap: dict) -> dict:
    """resolve 记录里的临时 id（e1 ...）换成裁判节点编的 p 编号。"""
    def f(i):
        return idmap.get(i, i)
    out = {**rec, "confirmed_ids": [f(i) for i in rec.get("confirmed_ids") or []],
           "candidates": [{**c, "id": f(c.get("id")), "early_id": c.get("id")} for c in rec.get("candidates") or []]}
    if "id" in rec:
        out["id"] = f(rec["id"])
    if rec.get("resent_ids"):
        out["resent_ids"] = [f(i) for i in rec["resent_ids"]]
    if rec.get("point"):
        out["point"] = {**rec["point"], "id": f(rec["point"].get("id")), "early_id": rec["point"].get("id")}
    if rec.get("values"):
        out["values"] = {f(i): v for i, v in rec["values"].items()}
    return out

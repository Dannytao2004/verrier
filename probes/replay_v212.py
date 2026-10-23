"""v2.12 离线重放：已存的、有真值的运行，用新的算子层重算。不调模型、不联网、只读 results/ 和 bench/out/。

每个已存运行（results/agent/<qid>/<tag>/state.json，连续值、compute 那一轮有方法、不是消融运行）：
- 目标历史点：这次运行自己 keep 的点里，按 bench/our_cases.py 的逐题规则（RULES 和同样的期间 / 单位 / 名字核对）认出的目标序列的点；
  单位倍数（us_gen 的 billion kWh）和德文千分点（de_cars，BUGS S24）照 bench 的规则在内存里改，只用于重放，逐条记下；
- 方法 = 存档裁判在 compute 那一轮的方法（去掉输入核对没过的；series_naive / linear_fit 去掉：v2.12 里前者只作对照、后者删了），
  加一个 series_auto（target_history = 上面认出的点），再用新的 compute.run 合并；
- 另算一列「汇总历史」：series_auto 改用 bench/out/our_series.json 里这道题跨所有运行汇总的月度历史（裁判列出全部月份时的上限）。
和官方值、存档的 agent 估计比。输出 probes/out/replay_v212.md 和 probes/out/replay_v212.json（都在 gitignore 的目录）。
用法：.venv/Scripts/python.exe probes/replay_v212.py
"""
import copy
import json
import math
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "bench"))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import compute as C  # noqa: E402
from triangulate.agent import value_check as VC  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402
import our_cases as OC  # noqa: E402  bench 的逐题规则（只读）

OUT = ROOT / "probes" / "out"
AGENT = ROOT / "results" / "agent"
DROP = ("series_naive", "linear_fit")


def compute_round(st):
    comp = st.get("compute") or {}
    return next((j for j in st.get("judge_rounds") or [] if j.get("round") == comp.get("methods_from_round") and j.get("methods")),
                None)


def skip_reason(st):
    t = (st.get("plan") or {}).get("target") or {}
    if not t:
        return "no target"
    if t.get("outcome_type") == "discrete":
        return "discrete"
    if (st.get("published") or {}).get("early_stop") or ((st.get("compute") or {}).get("result") or {}).get("basis") == "published":
        return "published"
    if st.get("ablation"):
        return "ablation run (own history excluded by design)"
    if compute_round(st) is None:
        return "no methods"
    return ""


def history_ids(q, st):
    """这次运行 keep 的点里目标序列的点：[(id, 内存里要用的值, 改值说明)]。规则同 bench/our_cases.collect（逐点）。"""
    qid, as_of, tm = q["id"], q["as_of"], OC._target_month(q)
    rule = OC.RULES[qid]
    inc = [re.compile(r, re.I) for r in rule["inc"]]
    exc = re.compile(rule["exc"] + "|" + OC.GENERIC_EXC, re.I)
    src_exc = (re.compile(rule["src_exc"][0], re.I), rule["src_exc"][1]) if rule.get("src_exc") else None
    units = [(re.compile(r, re.I), f) for r, f in rule.get("units", [])]
    out = []
    for p in st.get("points") or []:
        if not p.get("keep"):
            continue
        name, unit, v = p.get("name") or "", p.get("unit") or "", p.get("value")
        if not all(r.search(f"{name} | {unit}") for r in inc) or exc.search(name):
            continue
        k = OC._kind(p)
        if k is None or not isinstance(v, (int, float)):
            continue
        ym = p["period_end"][:7]
        if units:
            fac = next((f for r, f in units if r.search(unit)), None)
            if fac is None:
                continue
        else:
            fac = 1.0
            if re.search(OC.BAD_UNIT, unit, re.I):
                continue
        full_year = k == "YTD" and ym[5:] == "12"
        if src_exc and src_exc[0].search(p.get("source_url") or "") and not (src_exc[1] and full_year):
            continue
        pd_ = (p.get("page_date") or "")[:10]
        if (p["period_end"] > as_of or ym >= tm or (len(pd_) == 10 and (pd_ > as_of or pd_ < p["period_end"]))
                or (not OC._YEAR_RE.search(name) and re.search(OC.REL, name, re.I)) or not OC._name_period_ok(name, ym)
                or v <= 0):
            continue
        val, note = float(v) * fac, (f"x{fac:g} ({unit})" if fac != 1 else "")
        vaw = (p.get("value_as_written") or "").strip()
        if rule.get("thousands_dot") and re.fullmatch(r"\d{1,3}(\.\d{3})+", vaw) and float(v) < 1000:
            val, note = float(vaw.replace(".", "")) * fac, f"thousands dot {vaw!r} -> {float(vaw.replace('.', '')) * fac:g} (S24)"
        out.append((p["id"], val, note))
    return out


def pooled_points(series: dict):
    """our_series.json 的汇总历史 -> 假的点（id h1..），月值和年内累计各一个点。"""
    import calendar
    pts = []
    for kind in ("history", "ytd"):
        for ym, v, _ in series[kind]:
            y, m = int(ym[:4]), int(ym[5:7])
            pts.append({"id": f"h{len(pts) + 1}", "keep": True, "value": float(v), "unit": "", "name": f"pooled {kind} {ym}",
                        "period_start": f"{y}-01-01" if kind == "ytd" else f"{y}-{m:02d}-01",
                        "period_end": f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"})
    return pts


def replay(st, q, series):
    jr = compute_round(st)
    target = st["plan"]["target"]
    bad = jr.get("audit_failed") or {}
    kept = [m for i, m in enumerate(jr["methods"]) if str(i) not in bad]
    others = [copy.deepcopy(m) for m in kept if m.get("method") not in DROP]
    dropped = [m.get("method") for m in kept if m.get("method") in DROP]
    av = AS.validate(jr.get("assumptions") or [], target)
    pts = {p["id"]: dict(p) for p in VC.usable(st.get("points") or [])}
    hist = history_ids(q, st)
    fixes = []
    for i, v, note in hist:
        if i in pts and note:
            pts[i]["value"] = v
            fixes.append(f"{i} {note}")
    out = {"history_ids": [i for i, _, _ in hist], "fixes": fixes, "dropped_methods": dropped,
           "other_methods": [m.get("method") for m in others]}
    for variant, extra_pts, ids in (("run", {}, [i for i, _, _ in hist]),
                                    ("pooled", {p["id"]: p for p in pooled_points(series)}, None)):
        ids = ids if ids is not None else list(extra_pts)
        ms = others + ([{"id": "m_auto", "method": "series_auto", "params": {"target_history": ids}, "rationale": "replay"}]
                       if ids else [])
        try:
            res = C.run(ms, {**pts, **extra_pts}, target, assumptions=av)
        except Exception as e:  # noqa: BLE001
            out[variant] = {"error": f"{type(e).__name__}: {e}"[:200]}
            continue
        r = res["result"]
        sa = next((m for m in res["methods"] if m.get("method") == "series_auto"), None)
        out[variant] = {"central": r.get("central"), "p10": r.get("p10"), "p90": r.get("p90"), "basis": r.get("basis"),
                        "n_blocks": (r.get("combination") or {}).get("n_blocks"),
                        "rule": (r.get("combination") or {}).get("rule_across_blocks"),
                        "methods": [(m["id"], m["method"], m.get("estimate"), (m.get("error") or "")[:120]) for m in res["methods"]],
                        "series_auto": None if sa is None else {
                            "estimate": sa.get("estimate"), "error": (sa.get("error") or "")[:160],
                            "path": (sa.get("series_auto") or {}).get("path"),
                            "window": (sa.get("series_auto") or {}).get("window"),
                            "members": (sa.get("series_auto") or {}).get("members"),
                            "row": ((sa.get("series_auto") or {}).get("interval") or {}).get("calibration_row")}}
    return out


def pe(x, a):
    return None if x is None else x / a - 1


def fmt(x):
    return "—" if x is None else f"{x * 100:+.1f}%"


def main():
    series = json.loads((ROOT / "bench" / "out" / "our_series.json").read_text(encoding="utf-8"))
    qs = {q["id"]: q for q in QUESTIONS if q["id"] in series}
    rows, skipped = [], {}
    for qid, q in qs.items():
        for p in sorted((AGENT / qid).glob("**/state.json")):
            key = p.parent.relative_to(AGENT).as_posix()
            st = json.loads(p.read_text(encoding="utf-8"))
            if st.get("as_of") != q["as_of"]:
                skipped.setdefault("as_of differs from the bank", []).append(key)
                continue
            why = skip_reason(st)
            if why:
                skipped.setdefault(why, []).append(key)
                continue
            saved = ((st.get("compute") or {}).get("result") or {}).get("central")
            r = replay(st, q, series[qid])
            rows.append({"key": key, "qid": qid, "tag": p.parent.name if p.parent.name != qid else "(root)",
                         "answer": q["answer_value"], "saved": saved, "saved_pct": pe(saved, q["answer_value"]), **r})
    (OUT / "replay_v212.json").write_text(json.dumps({"rows": rows, "skipped": skipped}, indent=1, ensure_ascii=False, default=str),
                                          encoding="utf-8")
    md = render(rows, skipped, qs)
    (OUT / "replay_v212.md").write_text(md, encoding="utf-8")
    print(md)


def _abs_med(xs):
    xs = [abs(x) if x is not None else math.inf for x in xs]
    return statistics.median(xs) if xs else None


def render(rows, skipped, qs):
    L = ["# v2.12 离线重放（probes/replay_v212.py）", "",
         "误差 = 估计 / 官方值 - 1。「存档」= 运行当时代码算的估计；「重放·本次」= 存档裁判的其他方法 + series_auto（这次运行自己 keep 的"
         "目标历史点），新 combine；「重放·汇总」= series_auto 改用 bench/out/our_series.json 跨运行汇总的历史。series_naive / linear_fit"
         " 从方法里去掉（v2.12：前者只作对照，后者删了）。样本内、单次运行，只能当个案看。", ""]
    L += ["## 每题一行（每题取最新的回归运行：v211g_reg > v211_reg > test2 > 其他按名字最后一个）", "",
          "| 题 | 运行 | 官方值 | 存档 | 重放·本次 | 重放·汇总 | 本次 series_auto | 块数 | 说明 |", "|---|---|---|---|---|---|---|---|---|"]
    order = {"v211g_reg": 0, "v211_reg": 1, "test2": 2}
    sel = []
    for qid in qs:
        cands = [r for r in rows if r["qid"] == qid]
        std = [r for r in cands if r["tag"] in order]
        if cands:
            sel.append(min(std, key=lambda r: order[r["tag"]]) if std else max(cands, key=lambda r: r["tag"]))
    L += [_row(r) for r in sel]
    L += ["", "## 合计（每题一行的那张表）", ""]
    L += _summary(sel)
    L += ["", "## 全部运行", "", "| 题 | 运行 | 官方值 | 存档 | 重放·本次 | 重放·汇总 | 本次 series_auto | 块数 | 说明 |",
          "|---|---|---|---|---|---|---|---|---|"]
    L += [_row(r) for r in rows]
    L += ["", "## 合计（全部运行）", ""]
    L += _summary(rows)
    L += ["", "## 没重放的运行", ""]
    L += [f"- {k}（{len(v)}）：{', '.join(v)}" for k, v in sorted(skipped.items())]
    return "\n".join(L) + "\n"


def _row(r):
    run, pool = r.get("run") or {}, r.get("pooled") or {}
    sa = run.get("series_auto")
    if sa is None:
        s = "（没认出目标历史点）"
    elif sa.get("estimate") is None:
        s = f"失败：{sa.get('error')}"
    else:
        s = f"{sa.get('path')} {fmt(pe(sa['estimate'], r['answer']))}，{len(sa.get('window') or [])} 个月，{sa.get('row')}"
    note = "; ".join(x for x in (", ".join(r["fixes"]) and "改值 " + ", ".join(r["fixes"])[:80],
                                  r["dropped_methods"] and "去掉 " + "/".join(r["dropped_methods"]),
                                  run.get("error"), pool.get("error")) if x)
    return (f"| {r['qid']} | {r['tag']} | {r['answer']:,} | {fmt(r['saved_pct'])} | {fmt(pe(run.get('central'), r['answer']))} | "
            f"{fmt(pe(pool.get('central'), r['answer']))} | {s.replace('|', '/')} | {run.get('n_blocks') or '—'} | {note.replace('|', '/')} |")


def _summary(rows):
    out = []
    for label, get in (("存档", lambda r: r["saved_pct"]), ("重放·本次", lambda r: pe((r.get("run") or {}).get("central"), r["answer"])),
                       ("重放·汇总", lambda r: pe((r.get("pooled") or {}).get("central"), r["answer"]))):
        xs = [get(r) for r in rows]
        n_est = sum(x is not None for x in xs)
        cov = [r for r in rows if (r.get("run") or {}).get("p10") is not None] if label == "重放·本次" else []
        out.append(f"- {label}：出数 {n_est}/{len(rows)}；中位绝对误差 {(_abs_med(xs) or 0) * 100:.2f}%（没出数记 inf）；"
                   f"±10% 内 {sum(x is not None and abs(x) <= 0.10 for x in xs)}；±5% 内 {sum(x is not None and abs(x) <= 0.05 for x in xs)}"
                   + (f"；80% 区间盖住官方值 {sum(r['run']['p10'] <= r['answer'] <= r['run']['p90'] for r in cov)}/{len(cov)}" if cov else ""))
    for label, v in (("本次", "run"), ("汇总", "pooled")):
        sa = [((r.get(v) or {}).get("series_auto") or {}) for r in rows]
        ok = [x for x in sa if x.get("estimate") is not None]
        why = {}
        for x in sa:
            if x and x.get("estimate") is None:
                k = re.sub(r"\d{4}-\d{2}|\d+", "N", x.get("error") or "")[:90]
                why[k] = why.get(k, 0) + 1
        out.append(f"- series_auto（{label}）出数 {len(ok)}/{len(rows)}（模型路径 {sum(x.get('path') == 'models' for x in ok)}，"
                   f"yoy 路径 {sum(x.get('path') == 'yoy' for x in ok)}；没认出目标历史点 {sum(not x for x in sa)}）；失败原因："
                   + "；".join(f"{k} x{n}" for k, n in sorted(why.items(), key=lambda kv: -kv[1])))
    both = [(r["saved_pct"], pe((r.get("run") or {}).get("central"), r["answer"])) for r in rows]
    both = [(a, b) for a, b in both if a is not None and b is not None]
    out.append(f"- 存档和重放·本次都出数的 {len(both)} 个里，重放更准 {sum(abs(b) < abs(a) for a, b in both)} 个、"
               f"更差 {sum(abs(b) > abs(a) for a, b in both)} 个、一样 {sum(abs(b) == abs(a) for a, b in both)} 个")
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

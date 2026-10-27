"""v2.13a 探针（单位带期间）：最短流程，只重跑「抽取」和「单位核对」两步，真模型，不跑整题。
每个案例：用已存运行的缓存页面（data/raw/agent/，只读）按当前抽取 prompt 重新抽，取出公式用到的点的 unit_calc；
再用当前单位核对（三个核对 + 裁定）核对已存的裁判方法（加几个改写的公式），代码按裁定的单位换到目标单位。
打印每个方法：各输入定下的单位、推导、结果单位、换算后的估计、对不对。不写 results/，回答存 probes/out/unit_period/。
用法：TRIANGULATE_KEY_FILE=... .venv/Scripts/python.exe probes/unit_period_probe.py [重复次数，默认 1]
"""
import copy
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent import graph as G  # noqa: E402
from triangulate.agent import unit_review as UR  # noqa: E402
from triangulate.agent.pipeline import MAX_CHARS_TO_EXTRACTOR, AgentLLM, Budget, verify_point  # noqa: E402
from triangulate.agent.prompts import EXTRACT_SYSTEM, EXTRACT_USER  # noqa: E402
from triangulate.config import MAX_TOKENS  # noqa: E402

OUT = ROOT / "probes" / "out" / "unit_period"
F = "formula_mc"

# (已存运行, 要核对的方法 [(标签, 公式或 None=用存档的, 输入)], 对的范围 (lo, hi), 说明)
CASES = [
    ("fc_de_cars_2026_09/v211g_reg", [("m2", None, None),
                                      ("fix", "p75 * k_months_per_year * a2", {"p75": "Germany Pkw new registrations January-April 2026",
                                                                               "k_months_per_year": "months per year",
                                                                               "a2": "September share of annual 2026 registrations"}),
                                      ("naive", "p75 * a2", {"p75": "Germany Pkw new registrations January-April 2026",
                                                             "a2": "September share of annual 2026 registrations"})],
     (200_000, 280_000), "1-4 月累计 x 9 月占全年份额；官方 256,774。存档 m2 = 78,938（12/12 被约掉）"),
    ("fc_lhr_pax_2026_09/v211_reg", [("m3", None, None)], (6_000_000, 9_000_000),
     "2025 全年旅客 x 9 月份额（S60）；官方 7,180,000，存档 609,608（多除了 12）"),
    ("fc_jp_movers_2026_08/v211_reg", [("m2", None, None)], (300_000, 600_000),
     "2025 全年迁移人数 x 8 月份额（S60）；官方 356,920，存档 38,136（多除了 12）"),
    ("smoke_pizza/v212f", [("m1", None, None), ("m2", None, None)], (40, 250),
     "芝加哥披萨吨/天；存档 m1 88.8、m2 107.5（本来是对的，不能误拦、不能变）"),
    ("ask_504d98a4/web_20261026T154556Z", [("m1", None, None)], (100, 1500),
     "某一天在架的招聘帖（存量，没有期间）；存档 363"),
    # 回归里本来就算对的题：新单位规则不能把它们弄坏（None = 这一轮所有 formula_mc 方法）
    ("fc_kr_births_2026_07/v211g_reg", None, (18_000, 30_000), "韩国 7 月出生；官方 24,275，存档 23,379"),
    ("fc_us_starts_2026_08/v211g_reg", None, (1_000_000, 1_600_000), "美国 8 月新屋开工（年化）；存档 1,271,700（-0.3%）"),
    ("fc_nhs_ae_2026_09/v211g_reg", None, (1_900_000, 2_900_000), "英格兰 9 月急诊就诊；存档 2,356,999（-3.4%）"),
]


def page_text(qid, p):
    k = hashlib.sha1(f"{p['source_url']}|{p.get('snapshot_ts') or 'live'}".encode("utf-8")).hexdigest()[:16]
    f = ROOT / "data" / "raw" / "agent" / qid / f"{k}.txt"
    return f.read_text(encoding="utf-8") if f.exists() else None


def reextract(llm, st, pts_needed):
    """按当前抽取 prompt 重抽这些点所在的页，返回 {点 id: 新抽到的 unit_calc 或 None}。"""
    t, qid = st["plan"]["target"], st["qid"]
    dirs = {d["id"]: d for d in st.get("directions") or []}
    by_page, got = {}, {}
    for p in pts_needed:
        by_page.setdefault((p["source_url"], p.get("snapshot_ts")), []).append(p)
    for (url, _), ps in by_page.items():
        text = page_text(qid, ps[0])
        if text is None:
            for p in ps:
                got[p["id"]] = None
            continue
        d = dirs.get(ps[0]["direction_id"]) or {}
        sent = text[:MAX_CHARS_TO_EXTRACTOR]
        res, err = llm.ask(EXTRACT_SYSTEM, EXTRACT_USER.format(
            text=sent, **{k: t.get(k, "") for k in ("what", "unit", "period_start", "period_end")},
            hypothesis=str(d.get("hypothesis", ""))[:600], data_to_find=str(d.get("data_to_find", ""))[:600]),
            role="extract:probe", qid=qid, max_tokens=MAX_TOKENS["extract"])
        new = []
        for r in (res or {}).get("points") or []:
            pt, _ = verify_point(r, ev.norm(sent), date.fromisoformat(st["as_of"]),
                                 date.fromisoformat(ps[0]["page_date"]) if ps[0].get("page_date") else None, None, url=url)
            if pt:
                new.append(pt)
        for p in ps:
            same = [x for x in new if abs(x["value"] - p["value"]) <= 1e-9 * max(1, abs(p["value"]))]
            got[p["id"]] = (same[0].get("unit_calc") if same else None)
    return got


def run_case(llm, run, methods, ok_range, note, rep):
    st = json.loads((ROOT / "results" / "agent" / run / "state.json").read_text(encoding="utf-8"))
    t = dict(st["plan"]["target"])
    rnd = st["compute"]["methods_from_round"]
    jr0 = copy.deepcopy(next(j for j in st["judge_rounds"] if j.get("round") == rnd))
    arch = {m.get("id"): m for m in jr0.get("methods") or []}
    labels = {m["id"]: m.get("label") for m in st["compute"]["methods"]}   # compute 重编过 id：m1.. -> 裁判写的 label
    by_label = {v: k for k, v in labels.items()}
    if methods is None:   # 这一轮所有 formula_mc 方法，标签用 compute 重编后的 id
        methods = [(m["id"], None, None) for m in st["compute"]["methods"] if m.get("method") == F]
    ms = []
    for lab, formula, roles in methods:
        if formula is None:
            src = arch.get(labels.get(lab, lab)) or arch.get(lab)
            ms.append(dict(copy.deepcopy(src), id=lab))
        else:
            base = next(iter(arch.values()))
            ms.append({"id": lab, "method": F, "unit": t.get("unit_canonical"), "coverage": {"kind": "full"},
                       "params": {"formula": formula, "inputs": {k: {"id": k, "role": v} for k, v in roles.items()}},
                       "rationale": "probe variant"})
    jr0["methods"] = ms
    pts = copy.deepcopy(st["points"])
    by_id = {p["id"]: p for p in pts}
    need = sorted({i for m in ms for i in [s.get("id") if isinstance(s, dict) else s for s in (m.get("params") or {}).get("inputs", {}).values()]
                   if str(i) in by_id}, key=str)
    uc = reextract(llm, st, [by_id[i] for i in need])
    for i, u in uc.items():
        if u:
            by_id[i]["unit_calc"] = u
    out0, av, failed = G._code_check(jr0, pts, t)
    fails = UR.review(llm, f"{st['qid']}_probe{rep}", jr0, out0, av, pts, dict(failed), t)
    out1, _, failed1 = G._code_check(jr0, pts, t)
    failed1.update(fails or {})
    recs = {r["method"]: r for r in (jr0.get("unit_reviews") or [{"methods": []}])[-1]["methods"]}
    rows = []
    for i, m1 in enumerate(out1["methods"]):
        lab = ms[i]["id"]
        r = recs.get(m1["id"]) or {}
        arb = (r.get("arbiter") or [{}])[-1].get("reply") or {}
        est = m1.get("estimate")
        ok = (est is not None and ok_range[0] <= est <= ok_range[1] and i not in failed1)
        blocked = i in failed1
        rows.append({"case": run, "method": lab, "formula": (ms[i].get("params") or {}).get("formula"),
                     "unit_calc": {k: uc.get(k) for k in need}, "inputs": [(x.get("name"), x.get("unit")) for x in arb.get("inputs") or []],
                     "derivation": arb.get("derivation"), "result_unit": r.get("unit"), "estimate": est,
                     "blocked": failed1.get(i, "")[:200] if blocked else "", "ok": ok})
    print(f"\n=== {run}  ({note})  target {t.get('unit_canonical')!r} {t.get('period_start')}..{t.get('period_end')}")
    print(f"    re-extracted unit_calc: {uc}")
    for x in rows:
        mark = "OK " if x["ok"] else ("BLOCKED" if x["blocked"] else "WRONG")
        e = "—" if x["estimate"] is None else f"{x['estimate']:,.0f}"
        print(f"  [{mark}] {x['method']}: {x['formula']}  ->  {e}   unit {x['result_unit']!r}")
        print(f"        inputs {x['inputs']}")
        print(f"        derivation: {x['derivation']}")
        if x["blocked"]:
            print(f"        blocked: {x['blocked']}")
    return rows


def main():
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    OUT.mkdir(parents=True, exist_ok=True)
    llm = AgentLLM(OUT / "calls.jsonl", Budget(usd=3.0))
    allrows = []
    for rep in range(reps):
        print(f"\n################ repeat {rep + 1}/{reps}")
        for run, methods, ok_range, note in CASES:
            allrows += [dict(x, rep=rep) for x in run_case(llm, run, methods, ok_range, note, rep)]
    (OUT / "rows.json").write_text(json.dumps(allrows, ensure_ascii=False, indent=1), encoding="utf-8")
    n_ok = sum(x["ok"] for x in allrows)
    print(f"\nSUMMARY: {n_ok}/{len(allrows)} method checks OK; spent ${llm.budget.usd:.3f}")
    for x in allrows:
        if not x["ok"]:
            print(f"  not ok: rep {x['rep'] + 1} {x['case']} {x['method']}: est {x['estimate']} blocked={bool(x['blocked'])}")


if __name__ == "__main__":
    main()

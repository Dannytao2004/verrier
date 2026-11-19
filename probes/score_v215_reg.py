"""v2.15 固定回归打分（口径：results/experiments/v215_reg_2026-11-19/PLAN.md）。只读存档，不调模型。
输出 results/experiments/v215_reg_2026-11-19/score.json 和 score.md。"""
import collections
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "results" / "agent"
OUT = ROOT / "results" / "experiments" / "v215_reg_2026-11-19"
sys.path.insert(0, str(ROOT / "probes"))
from run_v215_reg import RUNS  # noqa: E402

OLD = {r["id"]: r for r in json.loads((AGENT / "summary_v211g_reg.json").read_text(encoding="utf-8"))}
PCT_REJ = re.compile(r'assumption (a\d+) rejected: value (\S+) with unit "%"')


def calls(d: Path) -> list:
    f = d / "calls.jsonl"
    return [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines() if x.strip()] if f.exists() else []


def one(r: dict) -> dict:
    d = AGENT / r["dir"][0] / r["dir"][1]
    row = {"run": r["name"], "dir": f"{r['dir'][0]}/{r['dir'][1]}", "mode": r["mode"]}
    if not (d / "state.json").exists():
        return {**row, "status": "missing"}
    s = json.loads((d / "state.json").read_text(encoding="utf-8"))
    comp = s.get("compute") or {}
    res = comp.get("result") or {}
    qid = r["dir"][0]
    truth = (OLD.get(qid) or {}).get("answer_value")
    c, p10, p90 = res.get("central"), res.get("p10"), res.get("p90")
    jr = next((j for j in reversed(s.get("judge_rounds") or []) if j.get("methods")), {})
    errs = [e for rp in jr.get("repairs") or [] for e in rp.get("errors") or []]
    cl = calls(d)
    judge_in = [x.get("prompt_tokens") for x in cl if str(x.get("arm", "")).startswith("judge") and x.get("prompt_tokens")]
    pages = collections.Counter((p.get("source_url"), p.get("direction_id"), p.get("round")) for p in s.get("points") or [])
    mag = comp.get("magnitude") or {}
    row.update(
        status="ok" if c else "no estimate", estimate=c, p10=p10, p90=p90, truth=truth,
        err=(c / truth - 1) if (c and truth) else None,
        abs_log10=abs(math.log10(c / truth)) if (c and truth) else None,
        covered=(p10 <= truth <= p90) if (c and truth and p10 and p90) else None,
        width=(p90 / p10) if (p10 and p90) else None,
        old_estimate=(OLD.get(qid) or {}).get("estimate"), old_err=(OLD.get(qid) or {}).get("pct_err"),
        gate=mag.get("status"), gate_ratio=mag.get("ratio"), gate_ref=((mag.get("reference") or {}).get("estimate")),
        gate_ref_status=(mag.get("reference") or {}).get("status"), gate_repair_sent=mag.get("repair_sent"),
        gate_checks=[x.get("status") for x in jr.get("magnitude_checks") or []],
        estimate_before_gate=((jr.get("magnitude_checks") or [{}])[0].get("estimate")),
        pct_rejections=PCT_REJ.findall("\n".join(errs)),
        n_repairs=len(jr.get("repairs") or []),
        json_repaired=sum(1 for x in cl if x.get("json_repaired")), thinking_off_retry=sum(1 for x in cl if x.get("thinking_off_retry")),
        invalid_json=sum(1 for x in cl if x.get("error") == "invalid_json"),
        truncated=sum(1 for x in cl if "trunc" in str(x.get("error", ""))),
        n_points=len(s.get("points") or []), n_pages=len(pages), pages_at_30=sum(1 for v in pages.values() if v >= 30),
        judge_prompt_tokens_max=max(judge_in) if judge_in else None,
        usd=(s.get("budget") or {}).get("usd_total_assumed"), usd_tokens=(s.get("budget") or {}).get("usd_tokens"),
        wall_s=s.get("wall_s"),
        final_brackets=len(re.findall(r"\[n\]", (s.get("final") or {}).get("text") or "")),
        final_unknown_ph=((s.get("final") or {}).get("text") or "").count("[unknown placeholder]"),
        final_has_gate_note="Magnitude check:" in ((s.get("final") or {}).get("text") or ""))
    return row


def med(xs):
    xs = sorted(x for x in xs if x is not None)
    return xs[len(xs) // 2] if len(xs) % 2 else (xs[len(xs) // 2 - 1] + xs[len(xs) // 2]) / 2 if xs else None


def main():
    rows = [one(r) for r in RUNS]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "score.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    reg = [x for x in rows if x["dir"].endswith("/v215_reg")]

    def agg(xs, key):
        e = [abs(x[key]) if x.get(key) is not None else math.inf for x in xs]
        return med(e)
    lines = ["# v2.15 固定回归打分（probes/score_v215_reg.py）", "",
             "## 回归 14 题（关思考），对照 v2.11g（10-22）", "",
             "| 题 | v2.15 估计 | 误差 | 80% 区间 | 盖住 | 宽 | v2.11g 误差 | 闸门 | 粗估比值 | 修正 | % 交回 | 点 / 页 / 满 30 页 | 裁判输入 max | 花费 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    f = lambda v, p=0: "—" if v is None else (f"{v:,.{p}f}")
    pc = lambda v: "—" if v is None else f"{100 * v:+.1f}%"
    for x in rows:
        if x["status"] == "missing":
            lines.append(f"| {x['run']} | 缺 | | | | | | | | | | | | |")
            continue
        lines.append(f"| {x['run']} | {f(x['estimate'])} | {pc(x['err'])} | {f(x['p10'])}–{f(x['p90'])} | "
                     f"{'—' if x['covered'] is None else ('是' if x['covered'] else '否')} | {f(x['width'], 2)} | {pc(x['old_err'])} | "
                     f"{x['gate']} {x['gate_checks']} | {f(x['gate_ratio'], 2)} | {x['n_repairs']} | {len(x['pct_rejections'])} | "
                     f"{x['n_points']} / {x['n_pages']} / {x['pages_at_30']} | {f(x['judge_prompt_tokens_max'])} | {f(x['usd'], 2)} |")
    n_ok = sum(1 for x in reg if x.get("status") == "ok")
    old_ids = [x["dir"].split("/")[0] for x in reg]
    lines += ["", f"- 回归 14 题出数 {n_ok}/14（v2.11g：{sum(1 for q in old_ids if OLD[q].get('estimate'))}/14）；"
              f"中位绝对误差 {pc(agg(reg, 'err'))}（v2.11g {pc(med([abs(OLD[q]['pct_err']) if OLD[q].get('pct_err') is not None else math.inf for q in old_ids]))}，没出数记 inf）；"
              f"±10% 内 {sum(1 for x in reg if x.get('err') is not None and abs(x['err']) <= .1)}（v2.11g {sum(1 for q in old_ids if OLD[q].get('pct_err') is not None and abs(OLD[q]['pct_err']) <= .1)}）；"
              f"区间盖住 {sum(1 for x in reg if x.get('covered'))}/{sum(1 for x in reg if x.get('covered') is not None)}",
              f"- 闸门 off：{[x['run'] for x in rows if x.get('gate') == 'off']}；裁判阶段触发：{[x['run'] for x in rows if 'off' in (x.get('gate_checks') or [])]}",
              f"- 补括号 {sum(x.get('json_repaired') or 0 for x in rows)} 次，关思考重问 {sum(x.get('thinking_off_retry') or 0 for x in rows)} 次，"
              f"invalid_json {sum(x.get('invalid_json') or 0 for x in rows)} 次，截断 {sum(x.get('truncated') or 0 for x in rows)} 次",
              f"- 终稿：[n] {sum(x.get('final_brackets') or 0 for x in rows)} 处，未知占位符 {sum(x.get('final_unknown_ph') or 0 for x in rows)} 处，"
              f"闸门提示 {[x['run'] for x in rows if x.get('final_has_gate_note')]}",
              f"- 花费合计 ${sum(x.get('usd') or 0 for x in rows):.2f}（token ${sum(x.get('usd_tokens') or 0 for x in rows):.2f}）"]
    (OUT / "score.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

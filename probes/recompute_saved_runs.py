"""离线重算：审查修复后的 compute / 方法库 / 区间规则，作用在三次已保存运行的同一批数据点和同一组裁判方法上。
不调模型、不联网。另外用修复后的证据核对（quote 省略号、数字边界、倍数词依据）重新核一遍方法用到的点
（页面原文在 data/raw/agent/，只在本地）。输出 results/agent/recompute_post_review.json。

用法：.venv/Scripts/python.exe probes/recompute_saved_runs.py
"""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import compute as C  # noqa: E402
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent.pipeline import MAX_CHARS_TO_EXTRACTOR, verify_point  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402

RUNS = [("fc_yell_2026_08", "run1_gzip_bug", "8 月第 1 次（预注册主结果）"), ("fc_yell_2026_08", "", "8 月第 2 次"),
        ("fc_yell_2026_09", "", "9 月")]


def page_text(qid: str, url: str, snap_ts):
    k = hashlib.sha1(f"{url}|{snap_ts or 'live'}".encode("utf-8")).hexdigest()[:16]
    p = ROOT / "data" / "raw" / "agent" / qid / f"{k}.txt"
    return p.read_text(encoding="utf-8") if p.exists() else None


def main():
    qs = {q["id"]: q for q in QUESTIONS}
    rows = []
    for qid, sub, label in RUNS:
        st = json.loads((ROOT / "results" / "agent" / qid / sub / "state.json").read_text(encoding="utf-8"))
        q = qs[qid]
        rnd = st["compute"].get("methods_from_round")
        methods = next(j for j in st["judge_rounds"] if j.get("round") == rnd)["methods"]
        pts = {p["id"]: p for p in st["points"]}
        new = C.run(methods, pts, st["plan"]["target"])
        old_r, new_r = st["compute"]["result"], new["result"]
        used = sorted({i for m in new["methods"] if m.get("estimate") for i in m.get("used_ids") or []},
                      key=lambda s: int(s[1:]))
        recheck = {}
        for i in used:
            p = pts[i]
            text = page_text(qid, p["source_url"], p.get("snapshot_ts")) if p.get("via") != "api" else None
            if text is None:
                recheck[i] = "page text not available locally"
                continue
            pd = date.fromisoformat(p["page_date"]) if p.get("page_date") else None
            raw = {k: p.get(k) for k in ("name", "value_as_written", "scale_word", "unit", "period_start", "period_end",
                                         "published_at_if_visible", "quote")}
            pp = None   # v2.11d：页面日期兜底的点按抽取员原样（期间为空）重查，页面日期就是它的 period_end
            if p.get("period_source") == ev.PAGE_DATE:
                raw.update(period_start="", period_end="")
                pp = date.fromisoformat(p["period_end"])
            ok, why = verify_point(raw, ev.norm(text[:MAX_CHARS_TO_EXTRACTOR]), date.fromisoformat(st["as_of"]), pd, pp)
            recheck[i] = "passes" if ok and ok["value"] == p["value"] else f"rejected: {why or 'value differs'}"
        ans = q["answer_value"]
        row = {"run": label, "qid": qid, "dir": f"results/agent/{qid}/{sub}".rstrip("/"), "answer": ans,
               "old": {k: old_r.get(k) for k in ("central", "p10", "p90", "basis", "sigma_ln")},
               "new": {k: new_r.get(k) for k in ("central", "p10", "p90", "basis", "sigma_ln", "n_backtest_folds", "weights")},
               "new_pct_err": None if new_r.get("central") is None else new_r["central"] / ans - 1,
               "new_covered_80": None if new_r.get("central") is None else new_r["p10"] <= ans <= new_r["p90"],
               "methods": [{k: m.get(k) for k in ("id", "label", "method", "estimate", "years_used", "error")}
                           | {"backtest_years": [b["year"] for b in m.get("backtest") or []]} for m in new["methods"]],
               "used_points_recheck": recheck}
        rows.append(row)
        print(f"{label}: central {old_r['central']:,.0f} -> {new_r['central']:,.0f}; "
              f"80% [{old_r['p10']:,.0f}, {old_r['p90']:,.0f}] {old_r['basis']} -> [{new_r['p10']:,.0f}, {new_r['p90']:,.0f}] "
              f"{new_r['basis']}; covered {row['new_covered_80']}; recheck {recheck}")
    out = ROOT / "results" / "agent" / "recompute_post_review.json"
    out.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

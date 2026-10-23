"""离线示例：v2.12 的 series_auto 和旧的 series_naive(k=1)（去年同月）在 17 道有真值的题上的对比。不调模型、不联网。
输入是离线基准从 agent 存档重建的目标序列（bench/out/our_series.json，口径见 bench/our_cases.py 的 docstring；只在本地）。
每道题把重建的月值和年内累计各做成一个点，全部列进 target_history，走 compute.run（和 agent 同一条路径）。

用法：PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe probes/series_auto_examples.py [题 id ...]
"""
import calendar
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import compute as C  # noqa: E402


def pts_of(series: dict) -> dict:
    out = {}
    for kind, rows in (("m", series["history"]), ("y", series["ytd"])):
        for n, (ym, v, _) in enumerate(rows, 1):
            y, m = int(ym[:4]), int(ym[5:])
            start = f"{y}-{m:02d}-01" if kind == "m" else f"{y}-01-01"
            out[f"{kind}{n}"] = {"id": f"{kind}{n}", "value": v, "unit": "count", "keep": True, "period_start": start,
                                 "period_end": f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"}
    return out


def pct(est, truth):
    return "-" if est is None else f"{(est / truth - 1) * 100:+.1f}%"


def main(ids):
    data = json.loads((ROOT / "bench" / "out" / "our_series.json").read_text(encoding="utf-8"))
    rows = []
    for qid, s in data.items():
        if ids and qid not in ids:
            continue
        y, m = int(s["target_month"][:4]), int(s["target_month"][5:])
        tgt = {"period_start": f"{y}-{m:02d}-01", "period_end": f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"}
        pts = pts_of(s)
        out = C.run([{"method": "series_naive", "params": {"target_history": list(pts), "k": 1}},
                     {"method": "series_auto", "params": {"target_history": list(pts)}}], pts, tgt)
        old, new = out["methods"]
        sa = new.get("series_auto") or {}
        iv = sa.get("interval") or {}
        bo = old.get("baseline_only") or {}   # v2.12 起 series_naive 只作对照基线：估计记在 baseline_only
        rows.append({"qid": qid, "truth": s["truth"], "months": len(s["history"]),
                     "old_series_naive_k1": bo.get("estimate"), "old_years": old.get("years_used"),
                     "old_error": None if bo else old.get("error"),
                     "new_series_auto": new.get("estimate"), "new_error": new.get("error"), "path": sa.get("path"),
                     "h": sa.get("h"), "consecutive": sa.get("consecutive_months"), "members": sa.get("members"),
                     "window": sa.get("window"), "row": iv.get("calibration_row"), "p10": iv.get("p10"), "p90": iv.get("p90"),
                     "covered": None if not iv else iv["p10"] <= s["truth"] <= iv["p90"], "notes": new.get("notes")})
    print("| question | truth | old series_naive k=1 | err | new series_auto | err | path / h / consecutive | calibration row | 80% interval | covered |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        o = r["old_series_naive_k1"]
        n = r["new_series_auto"]
        print(f"| {r['qid']} | {r['truth']:,.0f} | {'-' if o is None else f'{o:,.0f}'} | {pct(o, r['truth'])} | "
              f"{'-' if n is None else f'{n:,.0f}'} | {pct(n, r['truth'])} | "
              + (f"{r['path']} / {r['h']} / {r['consecutive']}" if n is not None else (r["new_error"] or "")[:90]) + " | "
              f"{r['row'] or '-'} | " + (f"{r['p10']:,.0f} .. {r['p90']:,.0f}" if r["p10"] else "-") + f" | {r['covered']} |")
    both = [r for r in rows if r["old_series_naive_k1"] is not None and r["new_series_auto"] is not None]
    ae = lambda e, t: abs(e / t - 1) * 100
    if both:
        import statistics
        o = [ae(r["old_series_naive_k1"], r["truth"]) for r in both]
        n = [ae(r["new_series_auto"], r["truth"]) for r in both]
        print(f"\nboth produced: {len(both)} questions; median |% error| old {statistics.median(o):.2f}%, new "
              f"{statistics.median(n):.2f}%; new closer on {sum(b < a for a, b in zip(o, n))}; covered "
              f"{sum(bool(r['covered']) for r in both)}/{len(both)}")
    print(f"old produced {sum(r['old_series_naive_k1'] is not None for r in rows)}, new produced "
          f"{sum(r['new_series_auto'] is not None for r in rows)} of {len(rows)}")
    if ids:
        print(json.dumps(rows, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main(sys.argv[1:])

"""v2.13b 实验的报告（读 probes/out/search_overlap/results.json，不调模型）：两次运行之间的重合度、边际效益。
数据点「同一个」的认法（用户 10-26：「月」和「月份」这种应该算同一个，别区分开）：
- 数值取 3 位有效数字相同；
- 单位：两边的计算单位用 pint 换算系数为 1 就算同一个（months / month、persons / person、/年 / /year）；
  有一边解析不了就去掉空格、标点、复数 s 再比字符串；
- 另给「只看数值」的重合率作为上限参考。
用法：.venv/Scripts/python.exe probes/search_overlap_report.py"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import qty as Q  # noqa: E402

DATA = ROOT / "probes" / "out" / "search_overlap" / "results.json"


def sig(v):
    return float(f"{v:.3g}") if v else 0.0


def loose(u: str) -> str:
    s = re.sub(r"[^a-z0-9/*()]", "", str(u or "").lower())
    return re.sub(r"s\b", "", s)


def same_unit(a: str, b: str) -> bool:
    if (a or "").strip() == (b or "").strip():
        return True
    f, err = Q.convert_factor(a, b) if a and b else (None, "empty")
    if not err and f is not None and abs(f - 1) < 1e-9:
        return True
    return loose(a) == loose(b)


def point_overlap(pa: list, pb: list, by_unit: bool) -> float:
    def hits(xs, ys):
        n = 0
        for x in xs:
            if any(sig(x["value"]) == sig(y["value"]) and (not by_unit or same_unit(x["unit"], y["unit"])) for y in ys):
                n += 1
        return n / len(xs) if xs else 0.0
    return (hits(pa, pb) + hits(pb, pa)) / 2


def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def main():
    store = json.loads(DATA.read_text(encoding="utf-8"))
    order = sorted(store, key=lambda k: (int(k[1:k.index("n")]), int(k[k.index("n") + 1:])))
    rows = []
    for k in order:
        a, b = store[k]["runs"]
        dom = lambda xs: {urlparse(u).netloc.replace("www.", "") for u in xs}
        rows.append({"setting": k, "agents": a["k"], "urls_per_dir": a["n"],
                     "pages_read": (len(a["read"]) + len(b["read"])) / 2,
                     "page_jaccard": jac(a["read"], b["read"]), "domain_jaccard": jac(dom(a["read"]), dom(b["read"])),
                     "points": (len(a["points"]) + len(b["points"])) / 2,
                     "point_overlap": point_overlap(a["points"], b["points"], True),
                     "point_overlap_value_only": point_overlap(a["points"], b["points"], False),
                     "usd_tokens": (a["usd_tokens"] + b["usd_tokens"]) / 2,
                     "usd_fee_assumed": (a["usd_search_fee_assumed"] + b["usd_search_fee_assumed"]) / 2,
                     "wall_s": (a["wall_s"] + b["wall_s"]) / 2})
    print("| setting | agents | URLs/dir | pages read | page overlap | site overlap | points | point overlap | (value only) "
          "| tokens $/run | search fee (assumed) $/run | wall s |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['setting']} | {r['agents']} | {r['urls_per_dir']} | {r['pages_read']:.0f} | {r['page_jaccard']:.0%} | "
              f"{r['domain_jaccard']:.0%} | {r['points']:.0f} | {r['point_overlap']:.0%} | {r['point_overlap_value_only']:.0%} | "
              f"{r['usd_tokens']:.3f} | {r['usd_fee_assumed']:.2f} | {r['wall_s']:.0f} |")
    print("\nmarginal (each step vs the previous K=3 setting): point overlap gained per extra page read and per extra $ of tokens")
    k3 = [r for r in rows if r["agents"] == 3]
    for x, y in zip(k3, k3[1:]):
        dp = y["pages_read"] - x["pages_read"]
        do = y["point_overlap"] - x["point_overlap"]
        du = y["usd_tokens"] - x["usd_tokens"]
        print(f"  {x['setting']} -> {y['setting']}: +{dp:.0f} pages, point overlap {do:+.0%}, page overlap "
              f"{y['page_jaccard'] - x['page_jaccard']:+.0%}, tokens {du:+.3f} $/run"
              + (f", {do / dp * 10:+.1%} overlap per 10 pages" if dp > 0 else ""))
    (DATA.parent / "report.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()

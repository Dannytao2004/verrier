"""v2.13b 实验：第一轮多派搜索 agent、每个方向多抓网页，看两次运行之间数据的重合度怎么随网址数变（用户 10-26）。
题目：应届生 sponsor 题（ask_504d98a4，最模糊的一题）。规划固定用 B 那次运行的目标和第一轮方向，只重跑第一轮（搜索 -> 抓 live 页
-> 抽取 -> 代码核对），不跑裁判，这样两次之间的差别只来自搜索和抓页这一层。每个设置跑两次，比：
- 读到的页面（status live_dated / snapshot）的 Jaccard 重合率，网站（域名）的重合率；
- 核对通过的数据点：按「数值取 3 位有效数字 + 计算单位」认同一个数，A 的点有多少在 B 里也有（双向平均）；
- 页数、实际 token 花费、按假设单价记的搜索费。
用法：TRIANGULATE_KEY_FILE=... .venv/Scripts/python.exe probes/search_overlap_probe.py k1n4 k3n6 k3n8 ...（kKnN：K 个搜索 agent、每方向 N 个网址）
结果追加到 probes/out/search_overlap/results.json（不写 results/）。"""
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import pipeline as P  # noqa: E402

RUN = ROOT / "results" / "agent" / "ask_504d98a4" / "web_20261026T154556Z"
OUT = ROOT / "probes" / "out" / "search_overlap"


def one_run(k: int, n: int, rep: int) -> dict:
    st = json.loads((RUN / "state.json").read_text(encoding="utf-8"))
    target = st["plan"]["target"]
    dirs = [d for d in st["directions"] if d.get("id", "").startswith("d")]   # 第一轮方向（b 开头的是裁判追加的）
    as_of = date.today().isoformat()
    calls = OUT / f"calls_k{k}n{n}_r{rep}.jsonl"
    if calls.exists():
        calls.unlink()
    budget = P.Budget(usd=6.0, pages=12 * n + 40, round1_pages=12 * n, urls_per_direction=n, searches_per_direction=k)
    ctx = P.Context(st["qid"], st["question"], as_of, calls, budget=budget)
    ctx.live_fetch, ctx.early, ctx.human = True, None, False
    t0 = time.time()
    with ThreadPoolExecutor(len(dirs)) as ex:
        res = list(ex.map(lambda d: P.run_direction(ctx, target, d, 1), dirs))
    read = sorted({pg["url"] for r in res for pg in r["pages"] if pg.get("status") in ("live_dated", "snapshot")})
    pool = sorted({u for r in res for u in (r.get("search") or {}).get("url_votes", {}) or (r.get("search") or {}).get("urls", [])})
    pts = [p for r in res for p in r["points"]]
    usd = sum(json.loads(l).get("usd") or 0 for l in calls.read_text(encoding="utf-8").splitlines())
    fee = sum(float((r.get("search") or {}).get("usd_search_fee_assumed") or 0) for r in res)
    return {"k": k, "n": n, "rep": rep, "wall_s": round(time.time() - t0), "directions": len(dirs), "read": read, "pool": pool,
            "points": [{"value": p["value"], "unit": p.get("unit_calc") or p.get("unit"), "name": p.get("name"), "url": p.get("source_url")}
                       for p in pts], "usd_tokens": usd, "usd_search_fee_assumed": fee,
            "errors": [r.get("error") or r.get("aborted") for r in res if r.get("error") or r.get("aborted")]}


def key(p):
    v = p["value"]
    return (float(f"{v:.3g}") if v else 0.0, str(p.get("unit") or "").strip().lower())


def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else None


def compare(a: dict, b: dict) -> dict:
    dom = lambda xs: {urlparse(u).netloc.replace("www.", "") for u in xs}
    ka, kb = {key(p) for p in a["points"]}, {key(p) for p in b["points"]}
    both = len(ka & kb)
    return {"pages_read": (len(a["read"]), len(b["read"])), "page_jaccard": jac(a["read"], b["read"]),
            "domain_jaccard": jac(dom(a["read"]), dom(b["read"])), "points": (len(a["points"]), len(b["points"])),
            "point_overlap": (both / len(ka) + both / len(kb)) / 2 if ka and kb else None,
            "usd_tokens": a["usd_tokens"] + b["usd_tokens"], "usd_search_fee_assumed": a["usd_search_fee_assumed"] + b["usd_search_fee_assumed"]}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "results.json"
    store = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    for arg in sys.argv[1:]:
        k, n = int(arg[1:arg.index("n")]), int(arg[arg.index("n") + 1:])
        runs = [one_run(k, n, rep) for rep in (1, 2)]
        cmp = compare(*runs)
        store[arg] = {"runs": runs, "compare": cmp}
        path.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{arg}: pages {cmp['pages_read']} page_jaccard {cmp['page_jaccard']:.2f} domain_jaccard {cmp['domain_jaccard']:.2f} "
              f"points {cmp['points']} point_overlap {cmp['point_overlap'] if cmp['point_overlap'] is None else round(cmp['point_overlap'], 2)} "
              f"usd_tokens {cmp['usd_tokens']:.3f} fee_assumed {cmp['usd_search_fee_assumed']:.2f} "
              f"wall {[r['wall_s'] for r in runs]} errors {[len(r['errors']) for r in runs]}", flush=True)


if __name__ == "__main__":
    main()

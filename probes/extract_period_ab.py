"""v2.8f 抽取 prompt 的期间写法：同一页用旧 prompt（v2.8e）和新 prompt 各抽一次，过同一个 verify_point，比较保留的点数和因期间被丢的点数。
页面取已存运行里「期间缺失被丢的点」最多的页（原文在 data/raw/agent/<题>/<key>.txt，只读）。真模型；不写 results/，结果写 probes/out/extract_ab/。
用法：.venv/Scripts/python.exe probes/extract_period_ab.py [每个运行取几页，默认 3]"""
import collections
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent import prompts as NEW  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget, verify_point  # noqa: E402
from triangulate.config import MAX_TOKENS  # noqa: E402
from triangulate.agent.pipeline import MAX_CHARS_TO_EXTRACTOR  # noqa: E402

RUNS = ["ask_9b1539aa/web_20261018T100833Z", "smoke_pizza/smoke3"]
OUT = ROOT / "probes" / "out" / "extract_ab"
OLD = {}
exec(subprocess.run(["git", "show", "v2.8e:triangulate/agent/prompts.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout, OLD)


def pages_for(run, k):
    s = json.loads((ROOT / "results/agent" / run / "state.json").read_text(encoding="utf-8"))
    dirs = {d["id"]: d for d in s["directions"]}
    n = collections.Counter()
    meta = {}
    for res in s["results"]:
        for pg in res.get("pages") or []:
            if pg.get("status") == "live_dated" and pg.get("raw_path"):
                meta.setdefault(pg["url"], (res["direction_id"], pg))
        for d in res.get("dropped_points") or []:
            if "period_end missing" in str(d.get("reason")):
                n[d["source_url"]] += 1
    out = []
    for url, c in n.most_common():
        if url in meta and len(out) < k:
            did, pg = meta[url]
            out.append({"run": run, "url": url, "n_period_drops_saved": c, "dir": dirs.get(did, {}), "page_date": pg.get("page_date"),
                        "txt": ROOT / pg["raw_path"].replace(".raw", ".txt"), "target": s["plan"]["target"], "as_of": s["as_of"]})
    return out


def extract(llm, P, page, tag):
    text = page["txt"].read_text(encoding="utf-8")[:MAX_CHARS_TO_EXTRACTOR]
    t, d = page["target"], page["dir"]
    res, err = llm.ask(P["EXTRACT_SYSTEM"], P["EXTRACT_USER"].format(text=text, **{k: t.get(k, "") for k in ("what", "unit", "period_start", "period_end")},
                       hypothesis=str(d.get("hypothesis", ""))[:600], data_to_find=str(d.get("data_to_find", ""))[:600]),
                       role=f"extract_ab:{tag}", qid=page["run"].replace("/", "_"), max_tokens=MAX_TOKENS["extract"])
    text_n = ev.norm(text)
    pd = date.fromisoformat(page["page_date"]) if page.get("page_date") else None
    kept, drops = [], collections.Counter()
    for r in (res or {}).get("points") or []:
        p, why = verify_point(r, text_n, date.fromisoformat(page["as_of"]), pd, d.get("category") == "base_rates", url=page["url"])
        if p:
            kept.append({k: r.get(k) for k in ("name", "value_as_written", "period_start", "period_end")})
        else:
            drops["period" if "period_end missing" in why or "period_start" in why else why[:50]] += 1
    return {"raw": len((res or {}).get("points") or []), "kept": kept, "drops": dict(drops), "error": err}


def main():
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    OUT.mkdir(parents=True, exist_ok=True)
    llm = AgentLLM(OUT / "calls.jsonl", Budget(usd=5.0))
    pages = [p for run in RUNS for p in pages_for(run, k)]
    jobs = [(P, p, tag) for p in pages for P, tag in ((OLD, "old"), (NEW.__dict__, "new"))]
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(lambda j: extract(llm, *j), jobs))
    rows = []
    tot = collections.Counter()
    for i, p in enumerate(pages):
        o, n = res[2 * i], res[2 * i + 1]
        rows.append({"url": p["url"], "run": p["run"], "old": o, "new": n})
        for tag, x in (("old", o), ("new", n)):
            tot[tag + "_raw"] += x["raw"]; tot[tag + "_kept"] += len(x["kept"]); tot[tag + "_period_drop"] += x["drops"].get("period", 0)
        print(f"{p['run'][:22]:<22} {p['url'][:60]:<60} old kept {len(o['kept']):>2}/{o['raw']:<2} period-drop {o['drops'].get('period', 0):>2} | "
              f"new kept {len(n['kept']):>2}/{n['raw']:<2} period-drop {n['drops'].get('period', 0):>2}")
    print("TOTAL", dict(tot))
    (OUT / "ab.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()

"""事后诊断（非预注册）：路径共用了多少输入、输入区间有多宽、80% 区间为什么没盖住答案。

只读 results/realfp/states/ 和 results/per_question.json，不发请求，不打印题目原文。
用法：python probes/diag_paths.py
"""
import glob
import itertools
import json
import math
import statistics as st
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
pq = {q["id"]: q for q in json.load(open(ROOT / "results/per_question.json", encoding="utf-8"))}

jac, top_shared, n_multi = [], 0, 0
widths, zero = {}, Counter()
for f in sorted(glob.glob(str(ROOT / "results/realfp/states/*.json"))):
    s = json.load(open(f, encoding="utf-8"))
    for i in s["inputs"]:
        lo, hi = i.get("low"), i.get("high")
        if not (i.get("usable") and lo and hi and lo > 0):
            continue
        w = math.log10(hi / lo)
        widths.setdefault(i["status"], []).append(w)
        zero[i["status"]] += w == 0
    vp = [p for p in s["paths"] if p["status"] in ("valid", "outlier")]
    if len(vp) < 2:
        continue
    n_multi += 1
    for a, b in itertools.combinations(vp, 2):
        A, B = set(a["uses"]), set(b["uses"])
        jac.append(len(A & B) / len(A | B))
    common = set.intersection(*[set(p["uses"]) for p in vp])
    top = max(s["inputs"], key=lambda i: abs(i.get("sensitivity") or 0))["name"]
    top_shared += top in common

print(f"有 >=2 条有效路径的题: {n_multi}")
print(f"路径两两之间输入重合度 (Jaccard) 中位数 {st.median(jac):.2f}；重合 >= 0.5 的路径对占 {sum(j >= 0.5 for j in jac) / len(jac):.0%}")
print(f"最敏感的输入被所有路径共用: {top_shared}/{n_multi}")
for k, v in sorted(widths.items()):
    print(f"{k}: n={len(v)}, 区间宽度 log10(high/low) 中位数 {st.median(v):.2f}, low == high 的有 {zero[k]} 个")

miss = Counter()
for qid, q in pq.items():
    r = q["structured"]
    if r["status"] != "ok" or r["covered_80"]:
        continue
    miss["答案高于 P90" if r["signed_log10_err"] < 0 else "答案低于 P10"] += 1
print("80% 区间没盖住:", dict(miss))

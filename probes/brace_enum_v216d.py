"""v2.16d 补括号的离线检验（不调模型）。拿存档里合法的裁判回复（按 state.json 重建，同 v2.15f 的检验），删掉右花括号：
A 单个：每个方法对象里字符串外的每个 `}`（含最后一个方法，v2.15f 不认那种报错）；
B 两个：每两个方法各删 params 的右括号（11-24 日本搬家原文就是这样）、同一个方法删 inputs 和 params 的右括号（少在同一处）
  + 每份回复随机 3 组任意两个；
C 三个：前三个方法各删 params 的右括号 + 每份回复随机 1 组任意三个。
看 close_missing_braces(text, judge_shape_ok) 补完是否和原回复相同；补出来结构检查通过、但和原回复不同 = 补错（静默）。
用法：.venv/Scripts/python.exe probes/brace_enum_v216d.py"""
import collections
import glob
import json
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate import llm  # noqa: E402
from triangulate.agent import graph as G  # noqa: E402

KEYS = ("id", "method", "params", "unit", "coverage", "rationale")
rng = random.Random(20261124)


def braces(text, lo, hi):
    pos, in_str, esc = [], False, False
    for i in range(lo, hi):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "}":
            pos.append(i)
    return pos


def drop(text, idx):
    for i in sorted(idx, reverse=True):
        text = text[:i] + text[i + 1:]
    return text


stats = {k: collections.Counter() for k in ("A1", "A1_last", "B2_params", "B2_same_spot", "B2_random", "C3_params",
                                           "C3_random")}
wrong, slow = [], []


def trial(kind, text, idx, reply):
    bad = drop(text, idx)
    try:
        json.loads(bad)
        stats[kind]["deletion still valid JSON"] += 1
        return
    except json.JSONDecodeError:
        pass
    t0 = time.time()
    out, n = llm.close_missing_braces(bad, G.judge_shape_ok)
    dt = time.time() - t0
    slow.append(dt)
    if out is None:
        stats[kind]["not repaired (retry)"] += 1
    elif out == reply:
        stats[kind][f"exact ({n} inserted)"] += 1
    else:
        stats[kind]["REPAIRED WRONG"] += 1
        if len(wrong) < 8:
            wrong.append((kind, n, [text[max(0, i - 50):i + 1] for i in idx]))


n_replies = 0
for f in sorted(glob.glob(str(ROOT / "results/agent/*/*/state.json"))):
    st = json.load(open(f, encoding="utf-8"))
    for jr in st.get("judge_rounds") or []:
        ms = [m for m in jr.get("methods") or [] if isinstance(m, dict)]
        if len(ms) < 2:
            continue
        methods = [{k: (m.get("unit_from_judge") or m.get("unit")) if k == "unit" else m[k] for k in KEYS if k in m} for m in ms]
        reply = {"assessment": ["x"], "decisions": [{"id": "p1", "keep": False, "reason": "r"}],
                 "assumptions": [{k: v for k, v in a.items() if not isinstance(v, (dict, list))}
                                 for a in jr.get("assumptions") or [] if isinstance(a, dict)], "methods": methods}
        if not G.judge_shape_ok(reply):
            continue
        n_replies += 1
        sep = (", ", ": ")   # DeepSeek 的回复都是这种分隔符（存档原文）
        text = json.dumps(reply, ensure_ascii=False, separators=sep)
        starts = [text.index('{"id": ' + json.dumps(m["id"]) + ', "method"') for m in methods]
        ends = starts[1:] + [text.rindex("]")]
        per = [braces(text, a, b) for a, b in zip(starts, ends)]
        params = [next((i for i in p if text.startswith('}, "unit"', i)), None) for p in per]
        for k, p in enumerate(per):
            for i in p:
                trial("A1_last" if k == len(per) - 1 else "A1", text, [i], reply)
        pk = [i for i in params if i is not None]
        for a in range(len(pk)):
            for b in range(a + 1, len(pk)):
                trial("B2_params", text, [pk[a], pk[b]], reply)
        for j in pk:   # 同一处少两层：inputs 和 params 的右括号都没写（`}}}` 写成 `}`）
            if text[j - 1] == "}":
                trial("B2_same_spot", text, [j - 1, j], reply)
        allb = [i for p in per for i in p]
        for _ in range(3):
            if len(allb) >= 2:
                trial("B2_random", text, rng.sample(allb, 2), reply)
        if len(pk) >= 3:
            trial("C3_params", text, pk[:3], reply)
        if len(allb) >= 3:
            trial("C3_random", text, rng.sample(allb, 3), reply)

print("replies", n_replies)
for k, v in stats.items():
    print(k, dict(v))
slow.sort()
print("repair time s: median %.3f  p99 %.3f  max %.3f" % (slow[len(slow) // 2], slow[int(len(slow) * .99)], slow[-1]))
for w in wrong:
    print("WRONG", w)

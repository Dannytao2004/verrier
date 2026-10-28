"""修正轮实际做了什么（只读、离线）：存档里每次修正，按「被点名」的范围比对修正前后的方法和假设。

被点名（v2.14a 的规则，见 graph._repair_scope）：
- 方法：报错里写到的（method X (...): ...），以及互相打架的两条（methods disagree: X gives ... but Y gives ...）；
- 假设：被拒的、报错里直接写到 id 的、理由 / 名字里引用了报错里写到的数据点的。
统计：没被点名的方法被删 / 被改、没被点名的方法用到的假设被改、被点名的方法被删、新加的方法。
用法：.venv/Scripts/python.exe probes/repair_scope_scan.py
"""
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

M_KEYS = ("method", "formula", "params", "coverage", "kind", "unit")
A_KEYS = ("value", "low", "high", "unit")


def sig(m, keys):
    return json.dumps({k: m.get(k) for k in keys}, sort_keys=True, ensure_ascii=False, default=str)


def named(errors, prev_assumptions):
    text = "\n".join(errors)
    ms = set(re.findall(r"\bmethod (\S+) \(", text))
    for a, b in re.findall(r"methods disagree: (\S+) gives .*? but (\S+) gives", text):
        ms |= {a, b}
    pts = set(re.findall(r"\bp\d+\b", text))
    asum = set(re.findall(r"\bassumption (\S+) rejected", text)) | set(re.findall(r"\ba\d+\b", text))
    for a in prev_assumptions or []:
        blob = " ".join(str(a.get(k) or "") for k in ("rationale", "name", "applies_when", "falsified_by"))
        if pts & set(re.findall(r"\bp\d+\b", blob)):
            asum.add(str(a.get("id")))
    return ms, asum, pts


def uses(m, aid):
    blob = json.dumps({k: m.get(k) for k in ("formula", "params")}, ensure_ascii=False, default=str)
    return re.search(rf"\b{re.escape(aid)}\b", blob) is not None


def main():
    tot = Counter()
    examples = []
    for path in sorted(glob.glob(str(ROOT / "results" / "agent" / "*" / "*" / "state.json"))):
        try:
            st = json.load(open(path, encoding="utf-8"))
        except Exception:
            continue
        run = "/".join(Path(path).parts[-3:-1])
        for jr in st.get("judge_rounds") or []:
            reps = jr.get("repairs") or []
            for k, rp in enumerate(reps):
                if "previous_methods" not in rp:
                    continue
                prev_m, prev_a = rp["previous_methods"] or [], rp["previous_assumptions"] or []
                if k + 1 < len(reps) and "previous_methods" in reps[k + 1]:
                    new_m, new_a = reps[k + 1]["previous_methods"] or [], reps[k + 1]["previous_assumptions"] or []
                elif rp.get("reverted"):
                    continue   # 修完一个都跑不了、代码已经退回原方案：回复本身没留下
                else:
                    new_m, new_a = jr.get("methods") or [], jr.get("assumptions") or []
                ms, asum, _ = named(rp.get("errors") or [], prev_a)
                pm, nm = {str(m.get("id")): m for m in prev_m}, {str(m.get("id")): m for m in new_m}
                pa, na = {str(a.get("id")): a for a in prev_a}, {str(a.get("id")): a for a in new_a}
                tot["attempts"] += 1
                ev = Counter()
                for mid, m in pm.items():
                    if mid in ms:
                        if mid not in nm:
                            ev["named_method_deleted"] += 1
                        elif sig(m, M_KEYS) != sig(nm[mid], M_KEYS):
                            ev["named_method_changed"] += 1
                    else:
                        if mid not in nm:
                            ev["UNNAMED_method_deleted"] += 1
                        elif sig(m, M_KEYS) != sig(nm[mid], M_KEYS):
                            ev["UNNAMED_method_changed"] += 1
                unnamed_kept = [m for mid, m in pm.items() if mid not in ms and mid in nm]
                for aid, a in pa.items():
                    if aid in asum or not any(uses(m, aid) for m in unnamed_kept):
                        continue
                    if aid not in na or sig(a, A_KEYS) != sig(na[aid], A_KEYS):
                        ev["UNNAMED_assumption_changed"] += 1
                ev["methods_added"] += len(set(nm) - set(pm))
                # 用 graph 里真正的规则模拟一遍：这次修正回复交给 _lock_repair 会被退回什么
                from triangulate.agent import graph as G
                gm, ga = G._repair_scope(rp.get("errors") or [], prev_a)
                _, _, lock = G._lock_repair(prev_m, prev_a, new_m, new_a, gm, ga, [])
                for x in lock:
                    ev[f"lock:{x['kind']}:{x['action']}"] += 1
                if "ask_eed7d5d6" in run:
                    print("sponsor 10-27", "round", jr.get("round"), "attempt", k + 1, "->", [(x["id"], x["action"]) for x in lock])
                tot.update(ev)
                if any(key.startswith("UNNAMED") for key in ev):
                    tot["attempts_with_unnamed_change"] += 1
                    if len(examples) < 12:
                        examples.append((run, jr.get("round"), k + 1, dict(ev)))
    print(json.dumps(dict(tot), indent=1))
    print("\nexamples (run, round, attempt, events):")
    for e in examples:
        print(" ", e)


if __name__ == "__main__":
    main()

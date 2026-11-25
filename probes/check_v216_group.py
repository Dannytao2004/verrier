"""v2.16 固定回归每组跑完后的核对（口径：PLAN.md「执行方式」的四条改坏标准）。只读存档，不调模型。
用法：.venv/Scripts/python.exe probes/check_v216_group.py <组号>   打出每次运行的判定、补括号的位置（原文上下文）、S84 恢复的点和
理由、闸门记录、终稿全文（逐字读用）。"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "probes"))
from triangulate import llm  # noqa: E402
from triangulate.agent import graph as G  # noqa: E402
import score_v216_reg as SC  # noqa: E402
from run_v216_groups import GROUPS  # noqa: E402


def insert_positions(text: str):
    """和 llm.close_missing_braces 同一个搜索，另外记下补在原文的哪些位置（原文坐标）。"""
    try:
        json.loads(text)
        return None
    except json.JSONDecodeError as e:
        layer = [(text, e.pos, e.msg, [])]
    seen = set()
    for _ in range(llm.MAX_BRACES):
        nxt = []
        for t, pos, msg, ins in layer:
            for k in llm._brace_spots(t, pos, msg) or []:
                t2 = t[:k] + "}" + t[k:]
                orig = k - sum(1 for j in ins if j < k)   # 换回原文坐标（前面补过的括号各占一个字符）
                try:
                    out = json.loads(t2)
                except json.JSONDecodeError as e2:
                    if e2.pos >= pos + 1 and hash(t2) not in seen and len(nxt) < llm.MAX_FRONTIER:
                        seen.add(hash(t2))
                        nxt.append((t2, e2.pos, e2.msg, ins + [k]))
                    continue
                if isinstance(out, dict) and G.judge_shape_ok(out):
                    pts, done = [], []
                    for j in ins + [k]:
                        pts.append(j - sum(1 for d in done if d < j))
                        done.append(j)
                    return sorted(pts)
        layer = nxt
    return None


def main(g: int):
    by = {r["name"]: r for r in SC.RUNS}
    for name in GROUPS[g]:
        r = by[name]
        x = SC.one(r)
        d = SC.AGENT / r["dir"][0] / r["dir"][1]
        print("=" * 100)
        print(name, "|", x["status"])
        if x["status"] == "missing":
            continue
        old = SC.OLD.get(r["dir"][0]) or {}
        old_err = old.get("pct_err")
        flags = []
        if not x["estimate"] and old.get("estimate"):
            flags.append("1 no estimate (v2.11g had one)")
        out = (SC.OUT / f"{name.replace(' ', '__')}.out")
        tail = out.read_text(encoding="utf-8", errors="replace") if out.exists() else ""
        if "Traceback" in tail:
            flags.append("2 traceback in run output")
        if x["covered"] is False and x["err"] is not None and old_err is not None and abs(x["err"]) > abs(old_err) + 0.10:
            flags.append("3 interval misses truth and |err| > v2.11g + 10pp")
        print(f"  estimate {x['estimate']}  truth {x['truth']}  err {x['err']}  covered {x['covered']}  v2.11g err {old_err}  "
              f"v2.15g {x['v215_err']}")
        print(f"  repairs {x['n_repairs']}  pct rejections {x['pct_rejections']}  gate {x['gate']} {x['gate_checks']} ratio "
              f"{x['gate_ratio']} ref {x['gate_ref']} repair_sent {x['gate_repair_sent']} before-gate {x['estimate_before_gate']}")
        print(f"  points {x['n_points']} pages {x['n_pages']} at15 {x['pages_at_15']} judge_in {x['judge_prompt_tokens_max']}  "
              f"usd {x['usd']} tokens {x['usd_tokens']}  invalid_json {x['invalid_json']} off_retry {x['thinking_off_retry']}")
        calls = SC.calls(d)
        for c in calls:
            if c.get("json_repaired"):
                pos = insert_positions(c["text"]) if c.get("text") else None
                print(f"  BRACES {c['arm']} inserted {c['json_repaired']}  positions {pos}")
                for p in pos or []:
                    print("     ...", repr(c["text"][max(0, p - 90):p]), "<}>", repr(c["text"][p:p + 30]))
            elif c.get("error") == "invalid_json" and str(c.get("arm", "")).startswith("judge"):
                print(f"  JUDGE INVALID JSON {c['arm']} {c.get('json_error')} (raw text kept: {'text' in c})")
        s = json.loads((d / "state.json").read_text(encoding="utf-8"))
        pts = {p["id"]: p for p in s.get("points") or []}
        for j in s.get("judge_rounds") or []:
            for rp in j.get("repairs") or []:
                for e in rp.get("errors") or []:
                    print(f"  r{j.get('round')} repair {rp['attempt']}: {e[:260]}")
                for q in rp.get("restored_points") or []:
                    p = pts.get(q["id"], {})
                    print(f"  RESTORED {q['id']} = {p.get('name')} {p.get('value')} {p.get('unit')} "
                          f"[{p.get('period_start')}..{p.get('period_end')}]\n     restore reason: {q['reason']}\n"
                          f"     discard reason: {q['discard_reason']}")
        if x["gate_checks"] and "off" in x["gate_checks"]:
            flags.append("4? gate fired: check whether the error was already < 2x and the repair made it worse")
        print("  FLAGS:", flags or "none (criteria 1-3); read 4 below")
        print("-" * 40, "final text")
        print((s.get("final") or {}).get("text"))


if __name__ == "__main__":
    main(int(sys.argv[1]))

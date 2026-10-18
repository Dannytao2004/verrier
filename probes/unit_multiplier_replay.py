"""v2.8q 探针，v2.8r 沿用（第 3 层兜底）：用当前代码（倍数说明 + 兜底）和真实模型重放已存运行里「数据点被代码乘过倍数」的方法的单位核对。
恒顺 v28p_test m1 以前判成 10000 bottle/year（乘重），其余几个以前判对；期望全部判对。结果写进 probes/out/unit_multiplier/replay.json。"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import unit_review as UR  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget  # noqa: E402

OUT = ROOT / "probes" / "out" / "unit_multiplier"
CASES = [("ask_9b1539aa", "v28p_test", "m1"), ("ask_9b1539aa", "v28i_test", "m2"), ("smoke_pizza", "smoke3", "m4"),
         ("smoke_pizza", "smoke4", "m4"), ("smoke_tea", "smoke3", "m5"), ("smoke_tea", "smoke4", "m2")]


def load(qid, tag, label):
    s = json.load(open(ROOT / "results" / "agent" / qid / tag / "state.json", encoding="utf-8"))
    jr = next(j for j in reversed(s["judge_rounds"]) if j.get("methods"))
    m = next(x for x in jr["methods"] if x.get("id") == label)
    m_in = {**m, "unit": m.get("unit_from_judge", m.get("unit"))}   # 裁判原来写的单位
    m_out = next(x for x in s["compute"]["methods"] if x.get("label") == label)
    saved = next((r for rv in jr.get("unit_reviews") or [] for r in rv["methods"] if r.get("label") == label), {})
    av = AS.validate(jr.get("assumptions") or [], s["plan"]["target"])
    return s, m_in, m_out, {p["id"]: p for p in s["points"]}, {a["id"]: a for a in av["kept"]}, saved


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    llm = AgentLLM(OUT / "calls.jsonl", Budget(usd=2.0))

    def one(case):
        qid, tag, label = case
        s, m_in, m_out, by_id, kept_a, saved = load(qid, tag, label)
        if not m_out.get("inputs_detail"):
            return {"case": case, "skipped": "no inputs_detail in saved compute"}
        rec = UR.review_method(llm, f"replay_{qid}", label, m_in, m_out, by_id, kept_a, s["plan"]["target"])
        return {"case": case, "saved_unit": saved.get("unit"), "saved_factor": saved.get("factor"), "now_unit": rec.get("unit"),
                "now_factor": rec.get("factor"), "failure": rec.get("failure"),
                "problems": [a.get("problem") for a in rec.get("arbiter") or []], "rec": rec}

    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(one, CASES))
    (OUT / "replay.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    for r in rows:
        if "skipped" in r:
            print(r["case"], "SKIPPED", r["skipped"])
            continue
        print(f"{'/'.join(r['case'])}: saved {r['saved_unit']!r} x{r['saved_factor']} -> now {r['now_unit']!r} x{r['now_factor']}"
              f"  arbiter tries {len(r['problems'])} problems {[p[:70] for p in r['problems'] if p]} failure {str(r['failure'])[:120]}")


if __name__ == "__main__":
    main()

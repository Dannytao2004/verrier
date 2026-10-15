"""探针：拿 v2.1 第一轮保存下来的裁判方法，回放给输入核对（graph.audit_methods），看它能不能抓住已知的错用。

第一轮的方法还没有 role 字段，这里按公式和假设名能看出来的本意手工补 role（ROLES）；其余输入用占位 role。
只做核对，不改结果。调用记到 probes/out/audit_replay_calls.jsonl。
用法：TRIANGULATE_KEY_FILE=... python probes/audit_replay.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import graph as G  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
# (题, tag, 方法下标, 输入名) -> 本意（第一轮的错用案例 + 两个本来正确的对照）
ROLES = {
    ("fc_kr_births_2026_07", "v21", 0, "p1"): "July 2025 live births in South Korea",
    ("fc_jnto_2026_08", "v21_noown", 0, "b1"): "August 2025 foreign visitor arrivals to Japan (JNTO)",
    ("fc_yell_2026_08", "v21_noown", 0, "a"): "Yellowstone National Park total recreation visits in 2025",
}
CASES = [("fc_kr_births_2026_07", "v21"), ("fc_jnto_2026_08", "v21_noown"), ("fc_yell_2026_08", "v21_noown"),
         ("fc_yell_2026_08", "v21"), ("fc_jnto_2026_08", "v21")]

llm = AgentLLM(ROOT / "probes" / "out" / "audit_replay_calls.jsonl", Budget())
for qid, tag in CASES:
    s = json.loads((ROOT / "results" / "agent" / qid / tag / "state.json").read_text(encoding="utf-8"))
    jr = next(j for j in reversed(s["judge_rounds"]) if j.get("methods"))
    jr = json.loads(json.dumps(jr))
    for i, m in enumerate(jr["methods"]):
        for name, spec in ((m.get("params") or {}).get("inputs") or {}).items():
            if isinstance(spec, dict) and not spec.get("role"):
                spec["role"] = ROLES.get((qid, tag, i, name)) or f"(as used in the formula: {name})"
    target = s["plan"]["target"]
    out, av, failed = G._code_check(jr, s["points"], target, None)
    res = G.audit_methods(llm, qid, jr, out, av, s["points"], failed, target)
    print(f"== {qid} [{tag}] code failures {sorted(failed)}; audit: {json.dumps(res, ensure_ascii=False)[:600]}"
          f"{'; audit_error ' + jr['audit_error'] if jr.get('audit_error') else ''}")

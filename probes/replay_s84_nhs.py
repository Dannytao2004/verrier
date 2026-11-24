"""v2.16c 定向检验：用 11-19 NHS 急诊（v2.15 回归）存档，重建第 2 轮第 1 次修正的 prompt，报错换成 v2.16c 的写法，
真调一次裁判（DeepSeek，关思考，和回归同设置），看它会不会恢复 p61 / p63 / p37，恢复后方法能不能算。
不写进 results/；调用日志等在 probes/out/s84_replay/。用法：python probes/replay_s84_nhs.py <repo> [--dry]
11-24 结果：p61 / p63 / p37 三个都恢复，方法原样，$0.0063；恢复后离线重算（单位按单位核对写回的形式代入，模拟）+2.1% / -0.7% / -0.1%。"""
import copy
import json
import sys
from pathlib import Path

ROOT = sys.argv[1]
sys.path.insert(0, ROOT)
from triangulate.agent import graph as G  # noqa: E402
from triangulate.agent import value_check as VC  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget  # noqa: E402
from triangulate.agent.prompts import JUDGE_SYSTEM, JUDGE_USER, METHODS_SPEC, EXTRA_RULE_R2  # noqa: E402
from triangulate.config import MAX_TOKENS  # noqa: E402

HERE = Path(ROOT) / "probes" / "out" / "s84_replay"   # 调用日志、重建的 prompt、回复（gitignore，只在本机）
HERE.mkdir(parents=True, exist_ok=True)
s = json.load(open(f"{ROOT}/results/agent/fc_nhs_ae_2026_09/v215_reg/state.json", encoding="utf-8"))
r1, r2 = s["judge_rounds"][0], s["judge_rounds"][1]
rep = r2["repairs"][0]
shown = [copy.deepcopy(p) for p in s["points"] if not p.get("ablation_excluded")]
r1_gone = {str(d["id"]) for d in r1["decisions"] if not d.get("keep")}
r2_dec = {str(d["id"]) for d in r2["decisions"]}
# 第 2 轮开始时的表：第 1 轮丢的点另起一段（当时 judged_round = 1）
for p in shown:
    if p["id"] in r1_gone:
        p["_r"] = 1
gone_before = [p for p in shown if p.get("_r") == 1]
rows_before = [dict(p, judged_round=1) for p in gone_before]
table = G._table([p for p in shown if p.get("_r") != 1]) + G._discarded_rows(rows_before)
dirs = "\n".join(f"- {d['id']} [{d['category']}] {d['hypothesis']}" for d in s["directions"])
judge_user = JUDGE_USER.format(question=s["question"], as_of=s["as_of"], target=G.dumps(s["plan"]["target"]),
                               directions=dirs, table=table, methods_spec=METHODS_SPEC,
                               extra_rule=EXTRA_RULE_R2 + G._previous_round([r1]))
by_id = {p["id"]: p for p in shown}   # keep / judge_reason = 第 2 轮判定之后（存档里没有恢复过）
new_errs, restorable = G._explain_discarded(rep["errors"], rep["previous_methods"], by_id, r2_dec)
prev_reply = {"methods": rep["previous_methods"], "assumptions": rep["previous_assumptions"]}
user = judge_user + G.REPAIR.format(previous=G.dumps(prev_reply), errors="\n".join(f"- {e}" for e in new_errs))
old_user = judge_user + G.REPAIR.format(previous=G.dumps(prev_reply), errors="\n".join(f"- {e}" for e in rep["errors"]))
(HERE / "repair_user.txt").write_text(user, encoding="utf-8")
print("errors sent:\n" + "\n".join(new_errs))
print("restorable:", sorted(restorable))
print("prompt chars new / old:", len(user), len(old_user))
if "--dry" in sys.argv:
    raise SystemExit
llm = AgentLLM(calls_path=HERE / "calls.jsonl", budget=Budget(usd=0.3))
out, err = llm.ask(JUDGE_SYSTEM, user, role="judge:r2:repair", qid="s84_replay", max_tokens=MAX_TOKENS["repair"],
                   shape_check=G.judge_shape_ok)
(HERE / "reply.json").write_text(json.dumps({"out": out, "err": err}, ensure_ascii=False, indent=1), encoding="utf-8")
if out is None:
    raise SystemExit(f"no reply: {err}")
print("decisions in reply about named points:",
      [d for d in out.get("decisions") or [] if isinstance(d, dict) and str(d.get("id")) in restorable])
print("methods in reply:", [(m.get("id"), (m.get("params") or {}).get("formula")) for m in out.get("methods") or []])
jr = {"methods": out.get("methods") or [], "assumptions": out.get("assumptions") or [], "decisions": r2["decisions"]}
got = G._restore_points(out, restorable, by_id, copy.deepcopy(r2["decisions"]), 1)
print("restored:", got)
live = VC.usable(shown)
out_c, av_c, failed = G._code_check(jr, live, s["plan"]["target"], None)
print("methods after restore:", [(m.get("id"), round(m["estimate"]) if m.get("estimate") else m.get("error"))
                                 for m in out_c.get("methods") or []])
print("usd:", llm.budget.usd if hasattr(llm.budget, "usd") else None)

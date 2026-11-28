"""v_prereg check 3: offline tests of paper/_tools/run_repeats.py helpers after the review edits. No model call, no run:
the runner's PREREG/LEAK_DIR/ABANDONED globals are pointed at a temporary folder; synthetic round logs and synthetic
leak-check answers exercise the scheduling prerequisites, the infra re-run planning, classify_infra, call_facts and
leak_decide. Writes only inside a temporary folder (deleted at the end) and this script's stdout."""
import json
import shutil
import sys
import tempfile
from datetime import timedelta
from pathlib import Path

ROOT = Path("D:/triangulate-agent")
sys.path.insert(0, str(ROOT / "paper" / "_tools"))
import run_repeats as RR  # noqa: E402

tmp = Path(tempfile.mkdtemp(prefix="vprereg_"))
RR.PREREG, RR.LEAK_DIR, RR.ABANDONED = tmp, tmp / "leak_check", tmp / "abandoned_cells.json"
runs = RR.load_runs()
roots = {"HEAD": RR.MAIN}
ok = True


def check(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


def write_log(rnd, events):
    with open(RR.log_path(rnd), "w", encoding="utf-8") as f:
        for e in events:
            f.write(json.dumps(e) + "\n")


now = RR.now_utc()
old = RR.iso(now - timedelta(hours=30))
r1 = sorted([o for o in runs if o["round"] == 1], key=lambda o: o["order_in_round"])
A = [o for o in r1 if o["pool"] == "A"]
ev = []
for o in r1:   # every round-1 run started and ended cleanly ...
    ev.append({"at": old, "event": "start", "qid": o["qid"], "tag": o["tag"]})
    ev.append({"at": old, "event": "end", "qid": o["qid"], "tag": o["tag"], "infra": None})
# ... except: A[0] ended with http_402; A[1] has a start but no end (runner killed)
ev = [e for e in ev if not (e["event"] == "end" and (e["qid"], e["tag"]) in {(A[0]["qid"], A[0]["tag"]), (A[1]["qid"], A[1]["tag"])})]
ev.append({"at": old, "event": "end", "qid": A[0]["qid"], "tag": A[0]["tag"], "infra": "http_402"})
write_log(1, ev)
(RR.LEAK_DIR).mkdir(parents=True, exist_ok=True)
(RR.LEAK_DIR / "decision.json").write_text(json.dumps({"decision": "GO", "checked_at": old, "excluded_questions": []}))

pend = RR.pending_infra(1, runs, roots, set())
check("pending_infra lists the 402 run and the interrupted run", sorted(pend) == sorted(
    [f"{A[0]['qid']}/{A[0]['tag']}", f"{A[1]['qid']}/{A[1]['tag']}"]))
pr = RR.round_prereq(2, runs, set(), False, roots)
print("   round 2 prerequisites:", pr)
check("round 2 blocked while round-1 infra re-runs are pending", any("infrastructure failures" in p for p in pr))
logged = []
todo = RR.plan_round(1, runs, roots, set(), True, logged.append)
check("--rerun-infra plans exactly the two runs under their rerun_tag",
      sorted((o["qid"], t, r) for o, t, r in todo) == sorted(
          [(A[0]["qid"], A[0]["rerun_tag"], A[0]["tag"]), (A[1]["qid"], A[1]["rerun_tag"], A[1]["tag"])]))
check("the interrupted run is logged as infra_interrupted", any(e.get("event") == "infra_interrupted" for e in logged))
# a recent start without end (child may still be running) is not re-runnable yet
ev2 = [e for e in ev if not ((e["qid"], e["tag"]) == (A[1]["qid"], A[1]["tag"]))]
ev2.append({"at": RR.iso(now - timedelta(minutes=30)), "event": "start", "qid": A[1]["qid"], "tag": A[1]["tag"]})
write_log(1, ev2)
todo = RR.plan_round(1, runs, roots, set(), True, lambda e: None)
check("a start younger than 2 x timeout is not re-run", all(o["qid"] != A[1]["qid"] for o, _, _ in todo))
# after both re-runs started, round 2 is no longer blocked by pending infra (gap / day rules still apply)
ev3 = ev + [{"at": old, "event": "start", "qid": A[0]["qid"], "tag": A[0]["rerun_tag"]},
            {"at": old, "event": "end", "qid": A[0]["qid"], "tag": A[0]["rerun_tag"], "infra": None},
            {"at": old, "event": "start", "qid": A[1]["qid"], "tag": A[1]["rerun_tag"]},
            {"at": old, "event": "end", "qid": A[1]["qid"], "tag": A[1]["rerun_tag"], "infra": None}]
write_log(1, ev3)
pr3 = RR.round_prereq(2, runs, set(), False, roots)
print("   round 2 prerequisites after the re-runs:", pr3)
check("round 2 allowed after the re-runs (30 h gap, different day)", pr3 == [])
# abandoned cell clears the block
write_log(1, ev)
RR.ABANDONED.write_text(json.dumps([{"cell_id": A[0]["cell_id"], "reason": "test"}, {"cell_id": A[1]["cell_id"], "reason": "test"}]))
check("abandoned cells clear the pending list", RR.pending_infra(1, runs, roots, set()) == [])
RR.ABANDONED.unlink()
# same-question concurrency guard and window rule (pure functions)
t = now.replace(year=2026, month=11, day=30, hour=0, minute=35, second=0, microsecond=0)   # Monday 00:35 UTC
check("Mon 00:35 + 20 min ok, + 27 min not ok (peak 01:00)", RR.window_ok(t, 20) and not RR.window_ok(t, 27))
check("is_peak Mon 01:00 True, Sat 02:00 False", RR.is_peak(t.replace(hour=1, minute=0)) and
      not RR.is_peak(t.replace(day=28, hour=2)))

# classify_infra on archive dirs (unchanged classes except api_rejected needs 'no estimate')
dirs = sorted(p.parent for p in (ROOT / "results" / "agent").rglob("state.json"))
cl = {}
for d in dirs:
    k = RR.classify_infra(d, 0, "", False)
    cl[k] = cl.get(k, 0) + 1
print("   classify_infra over", len(dirs), "archive dirs:", cl)
check("archive: only the 7 *_402 runs are infra", cl == {None: len(dirs) - 7, "http_402": 7})
# synthetic run dir: state with an estimate and a 400 call -> outcome; without estimate -> api_rejected_400
d = tmp / "fake_run"
d.mkdir()
(d / "calls.jsonl").write_text(json.dumps({"http": 200, "ok": True, "usd": 0.01}) + "\n" + json.dumps({"http": 400, "ok": False}) + "\n")
(d / "state.json").write_text(json.dumps({"compute": {"result": {"central": 5.0}}}))
check("400 on one call of a run with an estimate is an outcome", RR.classify_infra(d, 0, "", False) is None)
(d / "state.json").write_text(json.dumps({"compute": {"result": {"central": None}}}))
check("400 on a run without an estimate is api_rejected_400", RR.classify_infra(d, 0, "", False) == "api_rejected_400")
cf = RR.call_facts(ROOT / "results/agent/fc_lhr_pax_2026_09/v216_reg")
print("   call_facts(fc_lhr_pax_2026_09/v216_reg):", cf)
check("call_facts finds the plan prompt tokens", isinstance(cf["plan_prompt_tokens"], int))

# leak_decide on synthetic answers (October replies re-used as 'new' answers)
ref = json.loads(RR.LEAK_REF.read_text(encoding="utf-8"))


def decide(answers):
    (RR.LEAK_DIR / "answers.json").write_text(json.dumps(answers), encoding="utf-8")
    RR.leak_decide(None)
    return json.loads((RR.LEAK_DIR / "decision.json").read_text(encoding="utf-8"))


base = [{"qid": r["qid"], "reply": r["attempt1_reply"], "at": RR.iso(now), "prompt_tokens": r["archived_prompt_tokens"]}
        for r in ref]
out = decide(base)
check("identical answers -> GO, 23 identical, 0 hits", out["decision"] == "GO" and out["n_identical_answers"] == 23
      and out["hits"] == 0)
truth = {x["qid"]: (x["new"], x["e_old"]) for x in out["rows"]}
sys.path.insert(0, str(ROOT))
from triangulate import forecast as FC  # noqa: E402
by = {q["id"]: q for q in FC.QUESTIONS}


def tv(qid):
    q = by[qid]
    return q.get("answer_value") if q.get("answer_value") is not None else FC.TEST4_OFFICIAL[qid]["value"]


cand = [r for r in out["rows"] if r["e_old"] and r["e_old"] > 0.01 and by[r["qid"]].get("answer_unit", "") == ""]
leak = [dict(a) for a in base]
for a in leak:
    if a["qid"] in {c["qid"] for c in cand[:4]}:
        a["reply"] = {"estimate": tv(a["qid"]), "unit": ""}
out4 = decide(leak)
check(f"4 exact-truth answers -> STOP (hits {out4['hits']})", out4["decision"] == "STOP" and out4["hits"] == 4)
leak1 = [dict(a) for a in base]
for a in leak1:
    if a["qid"] == cand[0]["qid"]:
        a["reply"] = {"estimate": tv(a["qid"]), "unit": ""}
out1 = decide(leak1)
check("1 exact-truth answer -> EXCLUDE that question", out1["decision"] == "EXCLUDE" and out1["excluded_questions"] == [cand[0]["qid"]])
tok = [dict(a, prompt_tokens=(a["prompt_tokens"] or 0) + 3) for a in leak]
outt = decide(tok)
check("tokenizer change: shift test still uses all 23, flag set", outt["n_shift"] == 4
      and outt["tokenizer_or_hosted_request_changed"] and outt["decision"] == "STOP")
inv = [dict(a) for a in base]
inv[0]["reply"] = None
outi = decide(inv)
check("an invalid new answer -> EXCLUDE that question", outi["decision"] == "EXCLUDE" and outi["excluded_questions"] == [inv[0]["qid"]])

shutil.rmtree(tmp)
print("ALL PASS" if ok else "SOME TESTS FAILED")

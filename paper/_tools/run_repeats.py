"""Tier-3 same-configuration repeat batch of the paper "Revisions, Not Repeats" (pre-registered in paper/prereg/PREREG.md).

Modelled on probes/run_v216_reg.py and probes/run_v216_groups.py. It reads the frozen run list paper/prereg/runs.json and
runs one round at a time under the pre-registered rules:
- at most 3 runs at once, never two runs of the same question at the same time (b6 verdict 7: concurrent replicas are
  correlated);
- a run starts only off-peak and only if no DeepSeek peak window (config.is_peak: Mon-Fri 01:00-04:00, 06:00-10:00 UTC)
  begins within its margin (runs.json margin_min, >= 20 minutes);
- runs whose state.json exists are skipped; a run that was started once is never started again, except an
  infrastructure failure, which may be re-run once under its rerun_tag (--rerun-infra) and is logged;
- the code is frozen: HEAD:triangulate of the main checkout must keep the tree hash recorded at pre-registration, and an
  old-version worktree must sit on its runs.json tree_commit with a clean triangulate/;
- a hard stop when the summed token fees (calls*.jsonl "usd") of the batch exceed $30, plus a guard that never starts a
  run if fees so far + $0.70 per running or starting run would exceed $30;
- rounds on different UTC calendar days, the first run of round N+1 at least 20 h after the last run of round N ended;
- round 1 needs the direct-ask leakage check (--leak-check, then --leak-decide) decided GO or EXCLUDE within 24 h.
Old-version runs execute in a git worktree of their tree commit (--code-root PATH, repeatable); their result folder is then
copied to results/agent/<qid>/<tag>/ of the main checkout (never overwriting) and their raw pages to
data/raw/agent_repB/<slug>/<qid>/.

Usage (interpreter: the project venv; PYTHONIOENCODING=utf-8; TRIANGULATE_THINKING etc. must be unset):
  python paper/_tools/run_repeats.py --leak-check --dry-run          print the 23 direct-ask requests, call nothing
  python paper/_tools/run_repeats.py --leak-check                    the leakage check (23 naive calls), then decides
  python paper/_tools/run_repeats.py --leak-decide                   offline: (re)compute the decision from saved answers
  python paper/_tools/run_repeats.py --round N --dry-run [--code-root PATH ...] [--python PATH]
  python paper/_tools/run_repeats.py --round N --preflight --code-root PATH ...   offline checks (imports, question text)
  python paper/_tools/run_repeats.py --round N --code-root PATH ...  run the round
  python paper/_tools/run_repeats.py --round N --rerun-infra --code-root PATH ...  re-run logged infrastructure failures once
--dry-run prints every command, environment change and output folder and exits without starting anything.
"""
import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

MAIN = Path(__file__).resolve().parents[2]            # D:/triangulate-agent (main checkout)
PREREG = MAIN / "paper" / "prereg"
RUNS_JSON = PREREG / "runs.json"
LEAK_DIR = PREREG / "leak_check"
LEAK_REF = PREREG / "leak_reference.json"
ABANDONED = PREREG / "abandoned_cells.json"   # cells declared not reproducible under PREREG.md C5 (written by the main session)
FROZEN_TREE = "7eaec1e42547889eb7b911fd6cd69ced854f33bf"   # git rev-parse HEAD:triangulate on 2026-11-27 (HEAD 2f9fd91)
TAG_V217A_TREE = "f3cad700d9da1c7db19e6058c537d69037c97f6c"  # git rev-parse v2.17a^{commit}:triangulate (comment-only diff)
PEAK_EXPR = "t.weekday() < 5 and (1 <= t.hour < 4 or 6 <= t.hour < 10)"   # must still be config.is_peak's body
MAX_PARALLEL = 3
FEE_STOP_USD = 30.0
PER_RUN_FEE_ALLOWANCE = 0.70      # 2 x the largest v2.17a off-peak token fee of the v2.16 regression ($0.341), rounded up
MIN_ROUND_GAP_H = 20
RUN_TIMEOUT_S = 90 * 60           # 1.9 x the longest archived thinking-off run of any version used (47.1 min, v2.1*)
LEAK_MAX_AGE_H = 24
FORBIDDEN_ENV = ("TRIANGULATE_THINKING", "TRIANGULATE_CONCURRENCY", "TRIANGULATE_THINKING_EXTRA")
POLL_S = 30
TRANSPORT = re.compile(r"TransportError|ConnectionError|URLError|TimeoutError|timed out|getaddrinfo|SSLError|"
                       r"RemoteDisconnected|ConnectionResetError|http_5\d\d", re.I)

_print_lock = threading.Lock()


# ----------------------------------------------------------------------------------------------------------- helpers
def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(t: datetime) -> str:
    return t.astimezone(timezone.utc).isoformat(timespec="seconds")


def is_peak(t: datetime) -> bool:
    """Same rule as triangulate.config.is_peak (checked against its source text by check_peak_rule)."""
    t = t.astimezone(timezone.utc)
    return t.weekday() < 5 and (1 <= t.hour < 4 or 6 <= t.hour < 10)


def window_ok(t: datetime, margin_min: int) -> bool:
    """Off-peak now and at every minute of the next margin_min minutes."""
    return all(not is_peak(t + timedelta(minutes=m)) for m in range(0, margin_min + 1))


def next_window(t: datetime, margin_min: int) -> datetime:
    s = t.replace(second=0, microsecond=0)
    if s < t:
        s += timedelta(minutes=1)
    for _ in range(7 * 24 * 60):
        if window_ok(s, margin_min):
            return s
        s += timedelta(minutes=1)
    return s


def check_peak_rule() -> None:
    src = (MAIN / "triangulate" / "config.py").read_text(encoding="utf-8")
    if PEAK_EXPR not in src:
        raise SystemExit("triangulate/config.py is_peak changed; the pre-registered peak rule no longer matches")


def git(root: Path, *a) -> str:
    p = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.stdout.strip() if p.returncode == 0 else ""


def load_runs() -> list:
    return json.loads(RUNS_JSON.read_text(encoding="utf-8"))


def log_path(rnd: int) -> Path:
    return PREREG / f"batch_round{rnd}.log"


def read_log(rnd: int) -> list:
    p = log_path(rnd)
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return out


class Logger:
    def __init__(self, rnd, dry):
        self.rnd, self.dry = rnd, dry

    def __call__(self, rec: dict):
        rec = {"at": iso(now_utc()), **rec}
        with _print_lock:
            if not self.dry:
                with open(log_path(self.rnd), "a", encoding="utf-8") as f:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(json.dumps(rec, ensure_ascii=False), flush=True)


def calls_usd(run_dir: Path) -> float:
    tot = 0.0
    for p in sorted(run_dir.glob("calls*.jsonl")):
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                tot += float(json.loads(line).get("usd") or 0)
            except (json.JSONDecodeError, TypeError, ValueError):
                pass
    return tot


def read_calls(run_dir: Path) -> list:
    out = []
    for p in sorted(run_dir.glob("calls*.jsonl")):
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


# ------------------------------------------------------------------------------------------------------ code roots
def resolve_roots(args, runs) -> dict:
    """tree_commit -> root Path. HEAD runs use the main checkout. --code-root paths are matched by their HEAD commit;
    in --dry-run, missing worktrees fall back to runs.json code_root_hint (marked as not present)."""
    roots = {"HEAD": MAIN}
    for p in args.code_root or []:
        r = Path(p)
        c = git(r, "rev-parse", "HEAD")
        if not c:
            raise SystemExit(f"--code-root {p}: not a git checkout")
        roots[c] = r
    for o in runs:
        if o["tree_commit"] not in roots and args.dry_run:
            roots.setdefault(o["tree_commit"], Path(o["code_root_hint"]))
    return roots


def root_checks(root: Path, tree_commit: str) -> list:
    """Problems that forbid starting a run from this root (empty list = ok). Read-only git and file checks."""
    probs = []
    if not root.exists():
        return [f"code root {root} does not exist (create the worktree first, PREREG.md section B4)"]
    if root.resolve() == MAIN.resolve():
        t = git(MAIN, "rev-parse", "HEAD:triangulate")
        if t != FROZEN_TREE:
            probs.append(f"main checkout: HEAD:triangulate is {t}, frozen {FROZEN_TREE} (code changed: frozen batch)")
    else:
        h = git(root, "rev-parse", "HEAD")
        if h != tree_commit:
            probs.append(f"{root}: HEAD {h} != tree_commit {tree_commit}")
        cache = root / "data" / "raw" / "agent" / "_cache"
        main_cache = MAIN / "data" / "raw" / "agent" / "_cache"
        try:
            same = cache.exists() and os.path.samefile(cache, main_cache)
        except OSError:
            same = False
        if not same:
            probs.append(f"{cache} is not a junction to {main_cache} (PREREG.md section B4)")
    st = git(root, "status", "--porcelain", "--", "triangulate")
    if st:
        probs.append(f"{root}: uncommitted changes under triangulate/: {st[:200]}")
    return probs


def env_problems() -> list:
    p = [f"{k} is set ({os.environ[k]!r}); it must be unset" for k in FORBIDDEN_ENV if os.environ.get(k)]
    m = os.environ.get("TRIANGULATE_MODEL")
    if m and m != "deepseek-flash":
        p.append(f"TRIANGULATE_MODEL={m!r}; the batch uses deepseek-flash")
    return p


def run_env(root: Path) -> tuple:
    """(env for the child, description of the changes). Never reads any key file; for a worktree it only points
    TRIANGULATE_KEY_FILE at the main checkout's key file path, because a worktree has no .env of its own."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    changes = {"PYTHONIOENCODING": "utf-8"}
    for k in FORBIDDEN_ENV:
        if k in env:
            env.pop(k)
            changes[k] = "<removed>"
    if root.resolve() != MAIN.resolve() and not os.environ.get("TRIANGULATE_KEY_FILE"):
        env["TRIANGULATE_KEY_FILE"] = str(MAIN / ".env")
        changes["TRIANGULATE_KEY_FILE"] = str(MAIN / ".env") + " (path only)"
    return env, changes


def command(o: dict, python: str, tag: str) -> list:
    if o["cli_mode"] == "ask":
        cmd = [python, "-m", "triangulate", "agent", "--ask", o["ask_question"], "--as-of", o["as_of"], "--id", o["qid"],
               "--tag", tag, "--auto-approve"]
    else:
        cmd = [python, "-m", "triangulate", "agent", "--question", o["qid"], "--tag", tag, "--auto-approve"]
    if o["noown"]:
        cmd.append("--ablate-own-history")
    return cmd


def run_dirs(o: dict, root: Path, tag: str) -> tuple:
    own = root / "results" / "agent" / o["qid"] / tag
    main = MAIN / "results" / "agent" / o["qid"] / tag
    return own, main


def has_state(o, root, tag) -> bool:
    own, main = run_dirs(o, root, tag)
    return (own / "state.json").exists() or (main / "state.json").exists()


# ------------------------------------------------------------------------------------------------ infra failures
def classify_infra(run_dir: Path, exit_code, stderr_tail: str, timed_out: bool):
    """Pre-registered infrastructure-failure classes (PREREG.md section C4). None = a valid outcome (never re-run)."""
    if timed_out:
        return "timeout"
    st_p = run_dir / "state.json"
    calls = read_calls(run_dir) if run_dir.exists() else []
    https = {c.get("http") for c in calls}
    for code in (401, 402, 403):
        if code in https:
            return f"http_{code}"
    if not st_p.exists():
        return "crash_no_state"
    st = json.loads(st_p.read_text(encoding="utf-8"))
    aborted = " ".join(str(x) for x in (st.get("aborted"), (st.get("budget") or {}).get("aborted")) if x)
    if "insufficient balance" in aborted.lower():
        return "http_402"
    has_est = ((st.get("compute") or {}).get("result") or {}).get("central") is not None
    for code in (400, 404, 422):   # v_prereg: only without an estimate (a run that still estimated is an outcome)
        if code in https and not has_est:
            return f"api_rejected_{code}"
    if not any(c.get("ok") for c in calls):
        return "no_model_call"
    if not has_est and (TRANSPORT.search(aborted) or (exit_code not in (0, None) and TRANSPORT.search(stderr_tail or ""))):
        return "network"
    return None


def call_facts(run_dir: Path) -> dict:
    """v_prereg: HTTP status counts and the prompt_tokens of the first 'plan' call (request-identity check, PREREG E0)."""
    calls = read_calls(run_dir) if run_dir.exists() else []
    http = {}
    for c in calls:
        if c.get("http") is not None:
            http[str(c["http"])] = http.get(str(c["http"]), 0) + 1
    plan = next((c.get("prompt_tokens") for c in calls if c.get("arm") == "plan" and c.get("prompt_tokens")), None)
    return {"http_codes": http, "plan_prompt_tokens": plan}


# ------------------------------------------------------------------------------------------------------- fee sums
def batch_fees(runs: list, roots: dict) -> float:
    """Token fees of the whole batch so far: every runs.json run (tag and rerun_tag), counted once (own code root first,
    then the main checkout), plus the leakage-check calls."""
    tot = 0.0
    for o in runs:
        root = roots.get(o["tree_commit"], Path(o["code_root_hint"]))
        for tag in (o["tag"], o["rerun_tag"]):
            own, main = run_dirs(o, root, tag)
            d = own if own.exists() else main
            if d.exists():
                tot += calls_usd(d)
    if LEAK_DIR.exists():
        tot += calls_usd(LEAK_DIR)
    return tot


# ------------------------------------------------------------------------------------------- copying old results
def copy_back(o: dict, root: Path, tag: str, started: datetime, log) -> None:
    if root.resolve() == MAIN.resolve():
        return
    own, main = run_dirs(o, root, tag)
    if not own.exists():
        log({"event": "copy_skip", "qid": o["qid"], "tag": tag, "why": f"{own} does not exist"})
        return
    if main.exists():
        log({"event": "copy_conflict", "qid": o["qid"], "tag": tag, "dst": str(main),
             "why": "destination exists; nothing overwritten"})
        return
    shutil.copytree(own, main)
    log({"event": "copy", "qid": o["qid"], "tag": tag, "src": str(own), "dst": str(main)})
    raw_src = root / "data" / "raw" / "agent" / o["qid"]
    raw_dst = MAIN / "data" / "raw" / "agent_repB" / o["slug"] / o["qid"]
    n = 0
    if raw_src.exists():
        raw_dst.mkdir(parents=True, exist_ok=True)
        for f in raw_src.iterdir():
            if f.is_file() and f.stat().st_mtime >= started.timestamp() - 5 and not (raw_dst / f.name).exists():
                shutil.copy2(f, raw_dst / f.name)
                n += 1
    log({"event": "copy_raw", "qid": o["qid"], "tag": tag, "dst": str(raw_dst), "files": n})


# ---------------------------------------------------------------------------------------------- leakage check
def leak_requests() -> list:
    """The 23 direct-ask requests: messages and parameters exactly as probes/naive_ask.py builds them (arms._messages
    with prompts.NAIVE_SYSTEM; thinking disabled, json_object, temperature 0, max_tokens = config.MAX_TOKENS['naive']).
    test4 questions take forecast.with_as_of(question, as_of of the archived naive answer)."""
    sys.path.insert(0, str(MAIN))
    from triangulate import config, forecast as FC   # noqa: E402
    from triangulate.arms import _messages           # noqa: E402
    from triangulate.prompts import NAIVE_SYSTEM     # noqa: E402
    ref = json.loads(LEAK_REF.read_text(encoding="utf-8"))
    by = {q["id"]: q for q in FC.QUESTIONS}
    out = []
    for r in ref:
        q = dict(by[r["qid"]])
        if r.get("as_of_for_template"):
            q = FC.with_as_of(q, r["as_of_for_template"])
        out.append({"qid": r["qid"], "q": q, "messages": _messages(NAIVE_SYSTEM, q),
                    "max_tokens": config.MAX_TOKENS["naive"], "ref": r})
    return out


def leak_check(args) -> None:
    if args.dry_run:
        os.environ["TRIANGULATE_KEY_FILE"] = str(PREREG / "_no_key_in_dry_run")   # nothing can read a key
    probs = env_problems()
    if probs:
        raise SystemExit("; ".join(probs))
    reqs = leak_requests()
    if args.dry_run:
        print(f"== leakage check (dry run): {len(reqs)} direct-ask calls, nothing is sent")
        print("POST https://api.deepseek.com/chat/completions, model deepseek-flash, thinking disabled, response_format "
              "json_object, temperature 0, stream false; arm 'naive' (thinking role 'naive', unset), attempt 1, no retry")
        print(f"calls log: {LEAK_DIR / 'calls.jsonl'}; answers: {LEAK_DIR / 'answers.json'}; decision: {LEAK_DIR / 'decision.json'}")
        for r in reqs:
            print(json.dumps({"qid": r["qid"], "max_tokens": r["max_tokens"], "messages": r["messages"],
                              "archived": {k: r["ref"].get(k) for k in ("source", "archived_at", "archived_prompt_tokens")}},
                             ensure_ascii=False))
        return
    LEAK_DIR.mkdir(parents=True, exist_ok=True)
    if (LEAK_DIR / "answers.json").exists():
        raise SystemExit("leak_check/answers.json exists: the check runs once (a repeat is a logged deviation, PREREG D5)")
    from triangulate.llm import LLM   # noqa: E402  (reads the key file here, only in a real check)
    llm = LLM(calls_path=LEAK_DIR / "calls.jsonl")
    answers = []
    for r in reqs:
        reply, text, err = llm.json_call(r["messages"], arm="naive", qid=r["qid"], attempt=1, max_tokens=r["max_tokens"])
        rec = [c for c in read_calls(LEAK_DIR) if c.get("qid") == r["qid"]]
        answers.append({"qid": r["qid"], "reply": reply, "text": text, "error": err, "at": iso(now_utc()),
                        "prompt_tokens": (rec[-1].get("prompt_tokens") if rec else None),
                        "http": (rec[-1].get("http") if rec else None)})
        print(json.dumps(answers[-1], ensure_ascii=False), flush=True)
    (LEAK_DIR / "answers.json").write_text(json.dumps(answers, indent=1, ensure_ascii=False), encoding="utf-8")
    leak_decide(args)


def _signflip_p_one_sided(d: list, seed: int = 20261127) -> float:
    """Exact one-sided sign-flip p for mean(d) > 0 (Monte Carlo with 10^6 draws if more than 16 values)."""
    import itertools
    d = [x for x in d if x != 0]
    m = len(d)
    if m == 0:
        return 1.0
    obs = sum(d)
    if m <= 16:
        n = ge = 0
        for signs in itertools.product((1, -1), repeat=m):
            n += 1
            ge += sum(s * x for s, x in zip(signs, d)) >= obs - 1e-12
        return ge / n
    rng = random.Random(seed)
    n, ge = 1_000_000, 0
    for _ in range(n):
        ge += sum(x if rng.random() < 0.5 else -x for x in d) >= obs - 1e-12
    return (ge + 1) / (n + 1)


def leak_decide(args) -> None:
    """Pre-registered decision (PREREG.md section D3). Offline."""
    import math
    sys.path.insert(0, str(MAIN))
    from triangulate import forecast as FC          # noqa: E402
    from triangulate.arms import check_naive        # noqa: E402
    ans = {a["qid"]: a for a in json.loads((LEAK_DIR / "answers.json").read_text(encoding="utf-8"))}
    ref = {r["qid"]: r for r in json.loads(LEAK_REF.read_text(encoding="utf-8"))}
    by = {q["id"]: q for q in FC.QUESTIONS}
    rows, d = [], []
    for qid, r in ref.items():
        q = by[qid]
        truth = q.get("answer_value")
        if truth is None:
            truth = (FC.TEST4_OFFICIAL.get(qid) or {}).get("value")
        unit, strict = q.get("answer_unit", ""), q.get("strict", True)
        old = check_naive(r["attempt1_reply"], unit, strict)[1]
        a = ans.get(qid) or {}
        new = check_naive(a.get("reply"), unit, strict)[1] if a.get("reply") is not None else None
        e_old = abs(math.log(old / truth)) if old else None
        e_new = abs(math.log(new / truth)) if new else None
        rel_new = abs(new / truth - 1) if new else None
        rel_old = abs(old / truth - 1) if old else None
        hit = bool(new) and rel_new <= 0.005 and (old is None or rel_old > 0.005) and (e_old is None or e_new <= e_old / 4)
        same_req = a.get("prompt_tokens") == r.get("archived_prompt_tokens")
        # v_prereg: the request text is identical by construction (05 log), so a prompt_tokens difference means a hosted-
        # model / tokenizer change, the case most prone to leakage: it is reported, it does not remove the question
        if e_old is not None and e_new is not None:
            d.append(e_old - e_new)
        rows.append({"qid": qid, "old": old, "new": new, "identical_answer": old == new, "e_old": e_old, "e_new": e_new,
                     "hit": hit, "same_request_tokens": same_req, "new_valid": new is not None, "error": a.get("error")})
    H = sum(r["hit"] for r in rows)
    p = _signflip_p_one_sided(d)
    eo = sorted(r["e_old"] for r in rows if r["e_old"] is not None)
    en = sorted(r["e_new"] for r in rows if r["e_new"] is not None)
    med = lambda x: (x[len(x) // 2] if len(x) % 2 else (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2) if x else None
    unchecked = [r["qid"] for r in rows if not r["new_valid"]]
    if H >= 4 or (H >= 2 and p < 0.05) or p < 0.01:
        decision = "STOP"
    elif H >= 1 or unchecked:
        decision = "EXCLUDE"
    else:
        decision = "GO"
    out = {"decided_at": iso(now_utc()), "checked_at": max((a.get("at") or "") for a in ans.values()),
           "decision": decision, "hits": H, "p_shift_one_sided": p, "n_shift": len([x for x in d if x != 0]),
           "median_e_old": med(eo), "median_e_new": med(en),
           "n_identical_answers": sum(r["identical_answer"] for r in rows),
           "n_prompt_tokens_differ": sum(not r["same_request_tokens"] for r in rows),
           "tokenizer_or_hosted_request_changed": all(not r["same_request_tokens"] for r in rows),
           "excluded_questions": sorted({r["qid"] for r in rows if r["hit"]} | set(unchecked)) if decision == "EXCLUDE" else [],
           "rows": rows}
    (LEAK_DIR / "decision.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, ensure_ascii=False, indent=1))


def abandoned_cells() -> dict:
    """cell_id -> reason, from abandoned_cells.json (a list of {"cell_id", "reason"}); empty if the file does not exist."""
    if not ABANDONED.exists():
        return {}
    return {c["cell_id"]: c["reason"] for c in json.loads(ABANDONED.read_text(encoding="utf-8"))}


def leak_status() -> dict:
    p = LEAK_DIR / "decision.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


# ------------------------------------------------------------------------------------------------ round logic
def interrupted(o: dict, root: Path, start_ev: dict, end_ev) -> bool:
    """v_prereg: a start was logged but no end event and no state.json, and the start is older than 2 x the run timeout
    (so no orphaned child can still be running): the runner was killed (reboot, power loss). Infrastructure class
    'interrupted', re-runnable once like the classes of classify_infra."""
    return (start_ev is not None and end_ev is None and not has_state(o, root, o["tag"])
            and now_utc() - datetime.fromisoformat(start_ev["at"]) > timedelta(seconds=2 * RUN_TIMEOUT_S))


def pending_infra(rnd: int, runs: list, roots: dict, excluded: set) -> list:
    """v_prereg: runs of round rnd that ended with an infrastructure class, or were interrupted (start, no end, no
    state.json), whose infra re-run has neither a logged start nor a state.json, and whose cell is not abandoned.
    Round rnd + 1 waits for them (PREREG.md C5)."""
    lg = read_log(rnd)
    starts = {(e["qid"], e["tag"]) for e in lg if e.get("event") == "start"}
    ends = {(e["qid"], e["tag"]): e for e in lg if e.get("event") == "end"}
    ab = abandoned_cells()
    out = []
    for o in runs:
        if o["round"] != rnd or o["qid"] in excluded or o["cell_id"] in ab:
            continue
        root = roots.get(o["tree_commit"], Path(o["code_root_hint"]))
        key = (o["qid"], o["tag"])
        e = ends.get(key)
        failed = bool(e and e.get("infra")) or (e is None and key in starts and not has_state(o, root, o["tag"]))
        if failed and (o["qid"], o["rerun_tag"]) not in starts and not has_state(o, root, o["rerun_tag"]):
            out.append(f"{o['qid']}/{o['tag']}")
    return out


def round_prereq(rnd: int, runs: list, excluded: set, rerun: bool, roots=None) -> list:
    """Problems that forbid starting round rnd (empty = ok)."""
    probs = []
    roots = roots or {"HEAD": MAIN}
    ls = leak_status()
    if not ls:
        probs.append("no leakage-check decision (run --leak-check first)")
    elif ls["decision"] == "STOP":
        probs.append("leakage check decided STOP: no runs (PREREG.md D3)")
    if rnd == 1 and ls and not rerun:
        age = now_utc() - datetime.fromisoformat(ls["checked_at"])
        if age > timedelta(hours=LEAK_MAX_AGE_H) and not any(e.get("event") == "start" for e in read_log(1)):
            probs.append(f"leakage check is {age} old (> {LEAK_MAX_AGE_H} h) and round 1 has not started (PREREG D5)")
    if rnd > 1:
        prev = read_log(rnd - 1)
        ends = [e["at"] for e in prev if e.get("event") == "end"]
        if not ends:
            probs.append(f"round {rnd - 1} has no finished run")
        else:
            gap = now_utc() - datetime.fromisoformat(max(ends))
            if gap < timedelta(hours=MIN_ROUND_GAP_H) and not rerun:
                probs.append(f"only {gap} since the last run of round {rnd - 1} ended (need {MIN_ROUND_GAP_H} h)")
        started = {(e["qid"], e["tag"]) for e in prev if e.get("event") == "start"}
        ab = abandoned_cells()
        missing = [o for o in runs if o["round"] == rnd - 1 and o["qid"] not in excluded and o["cell_id"] not in ab
                   and (o["qid"], o["tag"]) not in started]
        if missing and not rerun:
            probs.append(f"round {rnd - 1} not complete: {len(missing)} runs never started")
        pend = pending_infra(rnd - 1, runs, roots, excluded)
        if pend and not rerun:
            probs.append(f"round {rnd - 1} has {len(pend)} infrastructure failures or interrupted runs without their "
                         f"once-only re-run (--round {rnd - 1} --rerun-infra) or an abandoned cell: {pend[:6]}")
        days = {e["at"][:10] for k in range(1, rnd) for e in read_log(k) if e.get("event") == "start"}
        if now_utc().date().isoformat() in days and not rerun:
            probs.append(f"today (UTC) already holds a start of an earlier round: {sorted(days)}")
    return probs


def plan_round(rnd: int, runs: list, roots: dict, excluded: set, rerun: bool, log) -> list:
    """List of (run, tag, rerun_of) to start, in runs.json order; logs skips."""
    mine = sorted([o for o in runs if o["round"] == rnd], key=lambda o: o["order_in_round"])
    started = {}
    for e in read_log(rnd):
        if e.get("event") == "start":
            started[(e["qid"], e["tag"])] = e
    ends = {(e["qid"], e["tag"]): e for e in read_log(rnd) if e.get("event") == "end"}
    todo = []
    for o in mine:
        root = roots.get(o["tree_commit"])
        if o["qid"] in excluded:
            log({"event": "skip", "qid": o["qid"], "tag": o["tag"], "why": "question excluded by the leakage check"})
            continue
        if o["cell_id"] in abandoned_cells():
            log({"event": "skip", "qid": o["qid"], "tag": o["tag"], "why": "cell abandoned: " + abandoned_cells()[o["cell_id"]]})
            continue
        if root is None:
            log({"event": "skip", "qid": o["qid"], "tag": o["tag"], "why": f"no --code-root for tree {o['tree_commit'][:10]} "
                                                                           f"({o['code_version']}, hint {o['code_root_hint']})"})
            continue
        if not rerun:
            if has_state(o, root, o["tag"]):
                log({"event": "skip", "qid": o["qid"], "tag": o["tag"], "why": "state.json exists"})
                continue
            if (o["qid"], o["tag"]) in started:
                log({"event": "skip", "qid": o["qid"], "tag": o["tag"], "why": "already started once (no state.json): "
                                                                                 "only --rerun-infra may re-run it"})
                continue
            todo.append((o, o["tag"], None))
        else:
            e = ends.get((o["qid"], o["tag"]))
            cut = interrupted(o, root, started.get((o["qid"], o["tag"])), e)
            if not cut and (not e or not e.get("infra")):
                continue
            if has_state(o, root, o["rerun_tag"]) or (o["qid"], o["rerun_tag"]) in started:
                log({"event": "skip", "qid": o["qid"], "tag": o["rerun_tag"], "why": "infra re-run already made (once only)"})
                continue
            if cut:
                log({"event": "infra_interrupted", "qid": o["qid"], "tag": o["tag"],
                     "started": started[(o["qid"], o["tag"])]["at"],
                     "why": "start logged, no end event, no state.json, older than 2 x the run timeout"})
            todo.append((o, o["rerun_tag"], o["tag"]))
    return todo


def execute_round(args, runs, roots, excluded, log) -> None:
    todo = plan_round(args.round, runs, roots, excluded, args.rerun_infra, log)
    log({"event": "plan", "round": args.round, "n_to_start": len(todo), "rerun_infra": args.rerun_infra,
         "runs": [f"{o['qid']}/{tag}" for o, tag, _ in todo]})
    running = {}          # qid -> (run, tag)
    lock = threading.Lock()
    stop = {"why": ""}

    def worker(o, tag, rerun_of, root):
        started = now_utc()
        env, changes = run_env(root)
        cmd = command(o, args.python, tag)
        own, main = run_dirs(o, root, tag)
        log({"event": "start", "qid": o["qid"], "tag": tag, "rerun_of": rerun_of, "pool": o["pool"],
             "code_version": o["code_version"], "root": str(root), "commit": git(root, "rev-parse", "HEAD"),
             "tree": git(root, "rev-parse", "HEAD:triangulate"), "cmd": cmd, "env_changes": changes, "out": str(own)})
        t0, timed_out, code, err_tail, out_tail = time.time(), False, None, "", ""
        try:
            p = subprocess.run(cmd, cwd=root, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=RUN_TIMEOUT_S)
            code, err_tail, out_tail = p.returncode, p.stderr[-20000:], p.stdout[-20000:]
        except subprocess.TimeoutExpired as e:
            timed_out = True
            out_tail = (e.stdout or "")[-20000:] if isinstance(e.stdout, str) else ""
            err_tail = (e.stderr or "")[-20000:] if isinstance(e.stderr, str) else ""
        try:
            od = PREREG / f"out_round{args.round}"
            od.mkdir(parents=True, exist_ok=True)
            (od / f"{o['qid']}__{tag}.out").write_text(out_tail + "\n--- stderr ---\n" + err_tail, encoding="utf-8")
            infra = classify_infra(own, code, err_tail, timed_out)
            fee_run = calls_usd(own) if own.exists() else 0.0
            log({"event": "end", "qid": o["qid"], "tag": tag, "rerun_of": rerun_of, "exit": code, "timed_out": timed_out,
                 "wall_s": round(time.time() - t0, 1), "state_json": (own / "state.json").exists(), "infra": infra,
                 "fee_run_usd": round(fee_run, 6), "fees_batch_usd": round(batch_fees(runs, roots), 6),
                 **call_facts(own)})
            copy_back(o, root, tag, started, log)
            if infra in ("http_402", "http_401", "http_403"):
                stop["why"] = stop["why"] or f"{infra} on {o['qid']}/{tag}: stop starting runs (balance or key)"
        except Exception as e:   # noqa: BLE001  (never leave a question marked as running)
            log({"event": "worker_error", "qid": o["qid"], "tag": tag, "error": f"{type(e).__name__}: {e}"[:300]})
        finally:
            with lock:
                running.pop(o["qid"], None)

    while todo or running:
        with lock:
            n_run = len(running)
        if not stop["why"] and todo:
            fees = batch_fees(runs, roots)
            if fees > FEE_STOP_USD:
                stop["why"] = f"hard stop: batch token fees ${fees:.2f} > ${FEE_STOP_USD}"
            probs = root_checks(MAIN, "HEAD") + env_problems()   # the main checkout's code must stay frozen
            if probs:
                stop["why"] = "code freeze / environment: " + "; ".join(probs)
        if stop["why"] and todo:
            log({"event": "stop", "why": stop["why"], "not_started": [f"{o['qid']}/{t}" for o, t, _ in todo]})
            todo = []
        started_one = False
        if todo and n_run < MAX_PARALLEL:
            fees = batch_fees(runs, roots)
            if fees + (n_run + 1) * PER_RUN_FEE_ALLOWANCE > FEE_STOP_USD:
                if n_run == 0:
                    log({"event": "stop", "why": f"fee guard: ${fees:.2f} + allowance would exceed ${FEE_STOP_USD}",
                         "not_started": [f"{o['qid']}/{t}" for o, t, _ in todo]})
                    todo = []
            else:
                t = now_utc()
                for i, (o, tag, rerun_of) in enumerate(todo):
                    root = roots[o["tree_commit"]]
                    with lock:
                        busy = o["qid"] in running
                    if busy or not window_ok(t, o["margin_min"]):
                        continue
                    probs = root_checks(root, o["tree_commit"]) + env_problems()
                    if probs:
                        log({"event": "skip", "qid": o["qid"], "tag": tag, "why": "; ".join(probs)})
                        todo.pop(i)
                        started_one = True
                        break
                    with lock:
                        running[o["qid"]] = (o, tag)
                    threading.Thread(target=worker, args=(o, tag, rerun_of, root), daemon=False).start()
                    todo.pop(i)
                    started_one = True
                    break
        if not started_one:
            time.sleep(POLL_S if (todo or running) else 0)
    log({"event": "round_done", "round": args.round, "fees_batch_usd": round(batch_fees(runs, roots), 6)})


def pending_copies(runs, roots, log) -> None:
    """Copy finished old-version runs that an interrupted invocation did not copy yet."""
    for o in runs:
        root = roots.get(o["tree_commit"])
        if root is None or root.resolve() == MAIN.resolve():
            continue
        for tag in (o["tag"], o["rerun_tag"]):
            own, main = run_dirs(o, root, tag)
            if (own / "state.json").exists() and not main.exists():
                copy_back(o, root, tag, datetime.fromtimestamp(own.stat().st_ctime, timezone.utc), log)


# ---------------------------------------------------------------------------------------------- preflight / dry run
PREFLIGHT = r"""
import json, sys
import triangulate, triangulate.agent.run, triangulate.forecast as FC
out = {"package": triangulate.__file__, "questions": {}}
for qid in sys.argv[1:]:
    q = next((x for x in FC.QUESTIONS if x["id"] == qid), None)
    out["questions"][qid] = None if q is None else {"question": q.get("question"), "as_of": q.get("as_of")}
print(json.dumps(out, ensure_ascii=False))
"""


def preflight(args, runs, roots) -> None:
    """Offline checks per code root of the round: root state, package import path, question text and as_of against the
    archive run being repeated. Imports the agent package with a key path that does not exist (nothing can read a key)."""
    mine = [o for o in runs if o["round"] == args.round]
    ok = True
    for tree in sorted({o["tree_commit"] for o in mine}):
        root = roots.get(tree)
        os_ = [o for o in mine if o["tree_commit"] == tree]
        if root is None:
            print(f"[preflight] tree {tree[:10]} ({os_[0]['code_version']}): no --code-root given")
            ok = False
            continue
        probs = root_checks(root, tree)
        env = dict(os.environ, PYTHONIOENCODING="utf-8", TRIANGULATE_KEY_FILE=str(PREREG / "_no_key_preflight"))
        for k in FORBIDDEN_ENV:
            env.pop(k, None)
        qids = sorted({o["qid"] for o in os_ if o["cli_mode"] == "question"})
        p = subprocess.run([args.python, "-c", PREFLIGHT, *qids], cwd=root, env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if p.returncode != 0:
            probs.append(f"import failed: {p.stderr[-600:]}")
        else:
            info = json.loads(p.stdout.strip().splitlines()[-1])
            if Path(info["package"]).resolve().parent.parent != root.resolve():
                probs.append(f"imported triangulate from {info['package']}, not from {root}")
            for o in os_:
                if o["cli_mode"] != "question":
                    continue
                ref = o["reference_run"] or next(
                    (f"{o['qid']}/{t}" for t in ("v216_reg", "v217a_try") if (MAIN / "results/agent" / o["qid"] / t / "state.json").exists()),
                    None)
                q = info["questions"].get(o["qid"])
                if q is None:
                    probs.append(f"{o['qid']}: not in this root's forecast.QUESTIONS")
                elif ref:
                    st = json.loads((MAIN / "results/agent" / ref / "state.json").read_text(encoding="utf-8"))
                    if (q["question"], q["as_of"]) != (st["question"], st["as_of"]):
                        probs.append(f"{o['qid']}: question/as_of differ from {ref}")
        print(f"[preflight] {os_[0]['code_version']:7s} root={root} tree={tree[:10]} runs={len(os_)}: "
              + ("OK" if not probs else "PROBLEMS: " + " | ".join(probs)))
        ok &= not probs
    print("[preflight]", "all OK" if ok else "NOT OK")


def dry_run(args, runs, roots) -> None:
    t = now_utc()
    mine = sorted([o for o in runs if o["round"] == args.round], key=lambda o: o["order_in_round"])
    ls = leak_status()
    excluded = set(ls.get("excluded_questions") or [])
    print(f"== DRY RUN round {args.round}: {len(mine)} runs in runs.json; nothing is started")
    print(f"now {iso(t)}  peak now: {is_peak(t)}  python: {args.python}  main checkout: {MAIN}")
    print(f"frozen HEAD:triangulate {FROZEN_TREE}; current {git(MAIN, 'rev-parse', 'HEAD:triangulate')}; "
          f"tag v2.17a tree {git(MAIN, 'rev-parse', 'v2.17a^{commit}:triangulate')} (expected {TAG_V217A_TREE}; "
          f"differs only in two comment lines)")
    print(f"uncommitted changes under triangulate/: {git(MAIN, 'status', '--porcelain', '--', 'triangulate') or 'none'}")
    print(f"environment problems: {env_problems() or 'none'}")
    print(f"leakage-check decision: {ls.get('decision', 'not made yet (required before round 1)')}; excluded questions: "
          f"{sorted(excluded) or 'none'}")
    print(f"round prerequisites now: {round_prereq(args.round, runs, excluded, False, roots) or 'all met'}")
    print(f"batch token fees so far: ${batch_fees(runs, roots):.4f} (hard stop ${FEE_STOP_USD}; guard ${PER_RUN_FEE_ALLOWANCE}"
          f" per running run); max parallel {MAX_PARALLEL}; one run per question at a time; timeout {RUN_TIMEOUT_S // 60} min")
    print(f"log: {log_path(args.round)}; per-run output: {PREREG / f'out_round{args.round}'}")
    print()
    for o in mine:
        root = roots.get(o["tree_commit"], Path(o["code_root_hint"]))
        tag = o["tag"]
        env, changes = run_env(root)
        own, main = run_dirs(o, root, tag)
        status = ("SKIP (question excluded)" if o["qid"] in excluded else
                  "SKIP (cell abandoned)" if o["cell_id"] in abandoned_cells() else
                  "SKIP (state.json exists)" if has_state(o, root, tag) else "WOULD RUN")
        print(f"#{o['order_in_round']:02d} [{status}] pool {o['pool']} {o['qid']} {o['code_version']} noown={o['noown']} "
              f"tag={tag} (infra re-run tag {o['rerun_tag']})")
        print(f"    cwd: {root}  {'(present)' if root.exists() else '(NOT PRESENT: create the worktree, PREREG B4)'}")
        print(f"    tree commit: {o['tree_commit']}  agent-code commit: {o['code_commit']}")
        if root.exists() and root.resolve() != MAIN.resolve():
            print(f"    root checks: {root_checks(root, o['tree_commit']) or 'ok'}")
        print(f"    command: {json.dumps(command(o, args.python, tag), ensure_ascii=False)}")
        print(f"    env changes: {json.dumps(changes, ensure_ascii=False)}")
        print(f"    output folder: {own}")
        if root.resolve() != MAIN.resolve():
            print(f"    copied after the run to: {main}  (only if it does not exist); raw pages to "
                  f"{MAIN / 'data/raw/agent_repB' / o['slug'] / o['qid']}")
        print(f"    start rule: off-peak and no peak within {o['margin_min']} min; next such time from now: "
              f"{iso(next_window(t, o['margin_min']))}")
    print()
    print("dry run: nothing started, nothing written.")


# ---------------------------------------------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--round", type=int, choices=(1, 2, 3))
    ap.add_argument("--code-root", action="append", help="git worktree of an old tree commit (repeatable)")
    ap.add_argument("--python", default=str(MAIN / ".venv" / "Scripts" / "python.exe"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--preflight", action="store_true")
    ap.add_argument("--rerun-infra", action="store_true")
    ap.add_argument("--leak-check", action="store_true")
    ap.add_argument("--leak-decide", action="store_true")
    args = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    check_peak_rule()
    if args.leak_check:
        return leak_check(args)
    if args.leak_decide:
        return leak_decide(args)
    if not args.round:
        ap.error("--round is required (or --leak-check / --leak-decide)")
    runs = load_runs()
    roots = resolve_roots(args, runs)
    if args.dry_run:
        return dry_run(args, runs, roots)
    if args.preflight:
        return preflight(args, runs, roots)
    probs = env_problems()
    if probs:
        raise SystemExit("; ".join(probs))
    ls = leak_status()
    excluded = set(ls.get("excluded_questions") or [])
    probs = round_prereq(args.round, runs, excluded, args.rerun_infra, roots)
    if probs:
        raise SystemExit("round cannot start: " + "; ".join(probs))
    lockf = PREREG / "run_repeats.lock"
    try:
        fd = os.open(lockf, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise SystemExit(f"{lockf} exists: another invocation may be running (delete it only if none is)")
    os.write(fd, json.dumps({"pid": os.getpid(), "at": iso(now_utc()), "round": args.round}).encode())
    os.close(fd)
    log = Logger(args.round, False)
    try:
        log({"event": "invocation", "round": args.round, "argv": sys.argv, "head": git(MAIN, "rev-parse", "HEAD"),
             "tree": git(MAIN, "rev-parse", "HEAD:triangulate"), "roots": {k: str(v) for k, v in roots.items()},
             "leak_decision": ls.get("decision"), "excluded": sorted(excluded)})
        pending_copies(runs, roots, log)
        execute_round(args, runs, roots, excluded, log)
    finally:
        lockf.unlink(missing_ok=True)


if __name__ == "__main__":
    main()

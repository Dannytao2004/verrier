# v_prereg: adversarial review of the tier-3 pre-registration (before any run)

Reviewed 2026-11-27 (about 22:00-23:00 UTC): `paper/prereg/PREREG.md`, `runs.json`, `summary.json`, the four dry runs,
`paper/_tools/run_repeats.py`, and the sources they cite. No model call, no agent run, no state-changing git command,
no official value of the 13 prospective questions opened. The runner was run only with `--dry-run`; its helpers were
tested offline on synthetic logs (`v04_runner_tests.py`, all pass).

Scripts and logs in this folder:
- `v01_counts.py` / `_log.txt`: independent recount from the frozen `runs.csv` and cross-check of `runs.json`.
- `v02_http_codes.py` / `_log.txt`: HTTP codes and call errors in the archive; `classify_infra` on all 233 run dirs.
- `v03_tree_commits.py` / `_log.txt`: pool-B tree commits vs run start times; code vs tree diffs; HEAD vs v2.17a.
- `v04_runner_tests.py` / `_log.txt`: offline tests of the edited runner (prerequisites, re-run planning, infra classes,
  call facts, leak decision on synthetic answers).
- `v05_plan_tokens_launchers.py` / `_log.txt`: plan-call prompt_tokens determinism and references; launchers of the
  v2.1* / v2.1b originals.
- `v06_commit_copies.py` / `_log.txt`: commit identity checked by content against the other commits with the same
  author date and subject.
- `dryrun_round{1,2,3}_v_prereg.txt`, `dryrun_leakcheck_v_prereg.txt`: dry runs of the edited runner (identical to the
  earlier ones apart from the clock lines).

## Verdicts

| check | verdict | basis |
|---|---|---|
| 1a scored questions and runs | confirmed | 233 rows; 115 scored runs (all with an estimate) on the 23 listed questions; 112 cells: 109 x 1, 3 x 2 (all v2.11g, none catastrophic) (`v01` [1], [4]) |
| 1b catastrophic runs | confirmed | 14 runs on 8 questions; flag = recomputed abs(ln err) > ln 2; all thinking off, deepseek-flash; versions and commits as in PREREG B3; 3 on v2.11f (`v01` [2]) |
| 1c pool B is same-configuration | corrected | version, code commit, thinking, noown, question text, as_of and backtest mode match every original; tags unique and new (`v01` [7], [8]). Found: the v2.8r tree also adds the test2 questions to forecast.py (worktrees.json note incomplete); the 5 v2.1*/v2.1b originals ran as 8 threads of one process sharing the fetch limiter (`v05` [c]); commit identity confirmed by content (`v06`: 24 copies, comment lines only). Documented in B3, request-identity check added (E0), sensitivity without the 5 cells (E3/R2) |
| 2a HEAD triangulate/ vs v2.17a | confirmed | not byte-equal: 2 comment lines (forecast.py, showcase_engine.py, commit 6c7f702); the runner freezes HEAD:triangulate 7eaec1e4; no uncommitted change (`v03`) |
| 2b old-version invocation and copying | confirmed (with the launcher caveat of 1c) | CLI flags, result paths, ablation_tag, key-file variable and cache format identical at every tree commit; results/forecast/summary.json and the LightGBM files are tracked at those commits; the runner copies only to a non-existing destination |
| 3 runner | corrected | off-peak margins, per-question exclusivity, 3 lanes, skip-existing, $30 stop and guard, lock, logging verified by reading and dry runs; fixed: api_rejected only without an estimate; new `interrupted` class (a killed runner left runs neither re-runnable nor classified); round N+1 waits for round-N infra re-runs; leak shift test no longer drops questions on a prompt-token difference; end events log HTTP codes and plan prompt_tokens |
| 4a section E fully specified | corrected | added: zero-spread floor for log variances; label precedence and the "against the thesis" label; R2 statistic, test and label; F2/M1/B1/S1 moved to descriptive (no test existed); E3 denominator and no-estimate sensitivity, "both intervals" rule; E4 ties and the definition of drift detected; E1 inclusion, comparator choice and clustering caveat; the G that applies to V1 and K1 |
| 4b leakage rule before data | corrected | the rule is stated and implemented as written, but its prompt-token filter would have switched the shift test off when the hosted model or tokenizer changed, the case most prone to leakage; filter removed, change flagged in the decision record (tested on synthetic answers) |
| 4c O2 single frozen statement and lookup | corrected | one primary (gate false alarms) with direction rules; added a strength rule (Fisher exact vs 0/82), dropped a past-only reading that could not fail, and lookup rules for a third lookup, approximate or bound values, other time bases and earnings-call sources. o2_score.py is unchanged |
| 4d literature coding rules | corrected | partial statements on S and T = P; strata so that ablation-only papers (admitted by G2 (ii)) cannot drive the headline gap count |
| 5 claims served, hurting outcome reported | corrected | outcome 2 (as-is about equal to same-config) was already defined; added the ceiling caveat for P2, which reading each pool-B direction cuts against, and the handling of inconclusive or reversed primaries; the 3-lane departure from TOPIC_DECISION O3 "one at a time" is now stated |
| 6 budget arithmetic | confirmed | pool A 69 x $0.2138 = $14.75 (max $0.3413: $23.55); pool B medians $2.96 x 1.12 = $3.31, maxima $4.87 x 1.12 = $5.45; margins 27/71/62/23/20 recomputed from runs.csv; about 22 run-hours, 3.0 / 3.0 / 1.6 h per round with 3 lanes |

## Problems not fixed here

- The as-is vs pool-A contrast for K1 (P2) is confounded with the ceiling of v2.17a. The design has no
  same-configuration aggregation measurement on old code that is not conditioned on a catastrophic original (pool B
  is). The caveat is stated, not resolved.
- `o2_score.py` prints only the direction of the gate reading; the strength rule (Fisher) must be computed in the O2
  report from its counts.
- The runner's live paths (thread scheduling, copying, `--rerun-infra`, the real leak check, `--preflight`) are tested
  only through their helpers and dry runs. An exception raised in `worker` before its `try` block (for example a disk
  error while logging the start) would leave the question marked as running and the loop waiting.
- The request-identity check covers the plan prompt and question text only; other prompts cannot be checked without
  running.
- In the main checkout, pool-A runs overwrite `data/raw/agent/<qid>/<k>.txt` of the same snapshot with v2.17a decoder
  text (local and gitignored; `.raw` bytes are identical; no analysis script reads these files).
- `run.main` writes a one-row `results/agent/summary_<tag>.json` per run (pool-A tags shared by 23 questions); harmless
  because scores are recomputed, but the files are misleading.
- Inherent limits stated in PREREG: a late-2026 floor, not the archive's; test4 repeats are backtests of live-mode
  originals; the direct-ask check tests memory through one prompt only.

## For the user

1. How to freeze: commit `paper/prereg/` and the runner with a tag (the repository is public), or keep the SHA-256
   list (`FROZEN_HASHES.txt`, new block "after v_prereg review").
2. Approve the 7 worktrees and cache junctions (PREREG B4).
3. 3 lanes (as planned) or one run at a time (TOPIC_DECISION O3 wording; `MAX_PARALLEL = 1`, about 22 h of run time).
4. The second literature coder.
5. The $30 stop leaves about $1 over the conservative high scenario ($29); the expected cost is about $18.

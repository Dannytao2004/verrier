# PREREG: tier-3 extension of "Revisions, Not Repeats" (same-configuration repeats, leakage check, O2, literature count)

Written 2026-11-27 (about 20:00-21:30 UTC) by the unit `p_prereg`, before any run of this batch, before the leakage check
and before any official value of the 13 prospective questions was looked up. The user approved this tier-3 extension on
2026-11-27. The second-archive audit (O1) is not planned here; it gets its own pre-registration.

Frozen artifacts (SHA-256 in `paper/prereg/FROZEN_HASHES.txt`, this file's hash included):
- `paper/prereg/runs.json`: the 93 runs, one object per run (built by `10_build_runs.py`, log `10_build_runs_log.txt`);
- `paper/_tools/run_repeats.py`: the runner (dry runs: `dryrun_round1.txt`, `dryrun_round2.txt`, `dryrun_round3.txt`,
  `dryrun_leakcheck.txt`);
- `leak_reference.json` (archived direct-ask answers), `prospective_runs.json` (O2 material), `o2_score.py` (O2 scorer),
  `excluded_cells.json`, `worktrees.json`;
- the pre-batch canonical table `paper/analysis/data/runs.csv` (its hash is recorded; the as-is column is computed from
  this file, not from a rebuilt one).

Every archive fact below names its file. Counting scripts and logs are in this folder (`01`-`10`, `*_log.txt`).

---

## 0. What I saw before writing this plan (it is not blind)

- `topic/TOPIC_DECISION.md` §1-4, `topic/checks/check_2.md` §3-4, `check_9_counts_log.txt`, the verify files cited
  below, `analysis/data/DATA_NOTES.md` (it lists the truth of all 23 scored questions and every catastrophic run with
  its error), `draft/positions/noise.md`.
- The single-run errors of the 2026-11-24/25 v2.17a regression runs on 10 questions (DATA_NOTES; `01_counts_log.txt`
  [4]). Pool-A outcomes on those questions are partly anticipated.
- S24 (`235.528` read as a decimal) was misread in all 7 pre-v2.17a DE cars runs (`a6_explore/verify/VERIFY.md` H6), and
  both v2.1* KR births siblings (normal and noown) are catastrophic (`a1_signal/verify/VERIFY.md` H2 problem 3). Pool-B
  recurrence for mechanisms M1 and M5 is therefore partly anticipated.
- The registered leak values of the pool-B questions (`06_question_identity_log.txt`) and one archived direct-ask answer
  (LHR, 7,200,000) while inspecting the file format.
- I did not open any official value, release page, `probes/out/test4_official_*` file or naive answer of the 13
  prospective questions. `TEST4_OFFICIAL` holds `None` for Q3-Q7 and I read nothing else about them.

---

## A. Why these runs: the claims only same-configuration repeats can settle

The archive holds 112 scored (question, configuration) cells; 109 hold one run, 3 hold two, none holds three, and none
of the 14 catastrophic runs has a same-configuration partner (`topic/checks/check_2_counts_log.txt`;
`topic/TOPIC_DECISION.md` §1). Every multi-run number in the paper is therefore a statement about a mixture of code
versions. The paper's claims that this extension tests:

| claim (TOPIC_DECISION.md) | what the archive cannot tell | what the repeats identify |
|---|---|---|
| **C1** a development archive mostly cannot supply same-configuration repeats; revisions depend on outcomes; the as-is numbers are "unidentified as statements about a frozen agent", not shown wrong | whether the as-is numbers happen to be close to the frozen-agent values | the frozen-agent values themselves (pool A), and how often each catastrophe recurs on its own code (pool B) |
| **C2** look-ahead: past-only partners remove the detectable re-run benefit (+4.9 pp [+0.8, +9.6] any partner vs +3.0 pp [-1.7, +8.2] same-or-older, `a5_policy/verify/VERIFY.md` H1) | what re-running the *same* configuration buys | same-config policy outcomes (pool A) and same-config "rescue" of the archive's catastrophic runs (pool B) |
| **C3** shrinkage under revision-aware rules may be power loss and ceiling; matched-n null; MDEs | the estimand value at the same n with no version mixing | K = 3 aggregation gain, flags and variance attribution at n = 3 on one configuration |
| **Risk 2** "shrinkage is power loss or ceiling, not a different estimand" (`check_2.md` §0.3) | it is decided inside the archive only by simulation (c1) | a direct same-config measurement on old code with headroom (pool B) and on frozen recent code (pool A) |
| noise memo "frozen repeat noise was never measured" (`draft/positions/noise.md` §3.4) | the repeat floor | the repeat floor per cell and pooled |

**What each outcome means for the paper** (labels are fixed in section E; every outcome is reported, including the ones
that hurt the thesis):

1. *Thesis supported.* The as-is within-question spread is a multiple of the pool-A repeat floor (P1 positive), the
   as-is K = 3 gain exceeds the same-config gain (P2 positive), and pool-B catastrophes mostly recur on their own
   version, so same-config re-running would not have rescued them. Then the archive's aggregation and re-run benefits
   came from mixing in fixed code, and C1-C3 carry same-configuration evidence. (v_prereg caveat: P2 positive on
   pool A alone is also what a ceiling would produce, since v2.17a single runs leave little room for a K = 3 gain;
   K1 is reported with the pool-A single-run w10, and P2 is read as an estimand difference only together with the
   pool-B rows on old code with headroom, E3 and R2.)
2. *Thesis hurt: as-is and same-configuration nearly equal.* The as-is spread is within a factor 2 of the floor, the
   K = 3 gains are equivalent, and pool-B catastrophes mostly do not recur (same-config repeats rescue them as well as
   cross-version partners did). Then the archive's revisions behaved like repeats for these statistics; the as-is
   numbers were approximately right. The paper says so in the abstract. The empirical claim narrows to C1 as an
   identification result (this could not be known without the repeats), C2's time-order results, and C4; the main
   table gains a row stating that the as-is and same-config values agree.
3. *Mixed.* Pool A agrees with the as-is values (recent code is at the ceiling) but pool B shows deterministic
   recurrence, or the reverse. The paper reports each row with its label; no row is dropped.
4. *Fix vs regression to the mean.* If pool-B catastrophes rarely recur, a large share of the archive's "improvement
   after the fix" is regression to the mean, which supports the outcome-dependent-revision part of C1 even if it hurts
   the aggregation rows. If they always recur, the fixes did the work. (v_prereg: each direction cuts against one
   reading, and the paper says which: high rho against the regression-to-the-mean reading of C1, low rho against the
   version-mixing reading of the aggregation and re-run rows.)
5. *Leakage or drift.* If the leakage check stops the batch, the paper reports that blind same-configuration repeats
   could no longer be made on this hosted model (section D). If the drift anchor detects drift, every pool-A number is
   labelled a late-November-2026 floor (it always is; see the limit below).
6. *Inconclusive or reversed primaries (v_prereg).* A primary row labelled "inconclusive" is reported as undecided
   and counts towards neither outcome 1 nor 2; a row labelled "different, against the thesis" (E0) counts as
   outcome 2 for that row and is stated in the abstract.

**Limit stated in advance.** The hosted model, the live web and the search engine may have changed since October, so
these runs estimate a late-2026 repeat floor of each configuration, not the archive's own floor
(`TOPIC_DECISION.md` §4 O3). Identical code is not identical behaviour (`b6_probes/verify/VERIFY.md` problem 1).

---

## B. The run list

### B1. Facts checked first

- **Scored questions.** `paper/analysis/data/runs.csv` has 115 scored runs on 23 questions (`01_counts_log.txt` [1]):
  fc_ca_rail_2026_07, fc_cn_profits_2026_09, fc_cn_retail_2026_04, fc_de_cars_2026_09, fc_es_transit_2026_08,
  fc_hk_visitors_2026_09, fc_jnto_2026_08, fc_jp_births_2026_07, fc_jp_movers_2026_08, fc_kr_births_2026_07,
  fc_kr_online_2026_08, fc_lhr_pax_2026_09, fc_nhs_ae_2026_09, fc_nz_exports_2026_03, fc_pola_teu_2026_09,
  fc_tw_births_2026_09, fc_tw_visitors_2026_09, fc_uk_insolv_2026_08, fc_us_gen_2026_07, fc_us_retail_2026_06,
  fc_us_starts_2026_08, fc_yell_2026_08, fc_yell_2026_09.
- **Frozen code.** `git diff --stat v2.17a HEAD -- triangulate/` is *not* empty: `triangulate/forecast.py` and
  `triangulate/showcase_engine.py` differ, one line each, and both lines are comments (commit IDs quoted in comments;
  commit 6c7f702 "Docs: update commit IDs cited in docs and comments", the only commit after v2.17a touching `triangulate/`). `git status --porcelain --
  triangulate` is empty. So the main checkout runs v2.17a behaviour; the runner freezes the tree hash
  `HEAD:triangulate = 7eaec1e4...` (tag v2.17a's tree is `f3cad700...`) and refuses to start if it changes.
- **Question text.** For every pool-A question, HEAD's question bank gives the same question text and as_of as every
  archive run of that question; for every pool-B cell, the question bank at the worktree commit gives the same text and
  as_of as the catastrophic run (`06_question_identity_log.txt`).
- **Catastrophic runs.** 14 scored runs on 8 questions; all thinking off (`01_counts_log.txt` [2],
  `02_catastrophic_detail_log.txt`).

### B2. Pool A (69 runs)

3 repeats of each of the 23 scored questions on frozen v2.17a (main checkout), thinking off, own history not ablated.
Tags `rep217a_r1`, `rep217a_r2`, `rep217a_r3` (round = repeat index). Command:
`python -m triangulate agent --question <qid> --tag rep217a_r<k> --auto-approve`.

The two test4 questions (fc_cn_profits_2026_09, fc_tw_visitors_2026_09) have `as_of = None` and `question = None` in
`forecast.py`; their archive runs were made by `probes/run_test4.py` in real-use mode on 2026-10-24. They are repeated
with the archive runs' exact text through
`python -m triangulate agent --ask "<state.json question>" --as-of 2026-10-24 --id <qid> --tag rep217a_r<k> --auto-approve`
(text stored in `runs.json` `ask_question`). Because as_of is now in the past, these runs are backtests (Wayback
snapshots only), while all 8 archive runs of the two questions fetched live pages (`state.leakage.pages_live_dated`
21-40, `pages_snapshot` 0; v_prereg corrected 26-40). Their leak sentinel has no registered values, as in the archive. Consequence: they are valid
same-configuration repeats of each other, but every as-is comparison is reported with and without them.

### B3. Pool B (24 runs): which versions, and why

`TOPIC_DECISION.md` proposed 3 repeats of each of the 8 catastrophic *questions* on v2.11f. Only 3 of the 14
catastrophic runs ran on v2.11f, so that design would not repeat the catastrophic configurations. I re-run each
catastrophic run's **own** configuration (its code version, thinking off, its noown flag), 2 repeats per cell:

| cell (catastrophic run) | code version | tree commit (worktree) | mechanism |
|---|---|---|---|
| fc_jnto_2026_08/v21_noown | v2.1* (untagged 2bbe8ae) | 2bbe8ae | M5 wrong input quantity, noown |
| fc_kr_births_2026_07/v21 | v2.1* | 2bbe8ae | M5 |
| fc_kr_births_2026_07/v21_noown | v2.1* | 2bbe8ae | M5, noown |
| fc_yell_2026_09/v21_noown | v2.1* | 2bbe8ae | M5, noown |
| fc_jnto_2026_08/v21b | v2.1b | 66e70a8 | M6 single assumption-only route |
| fc_de_cars_2026_09/test2 | v2.8r | 48e6b45 (agent code = c64d3a3 = frozen-v2.8r) | M1 S24 |
| fc_de_cars_2026_09/v211_reg | v2.11f | 8e3b64e | M1 S24 |
| fc_lhr_pax_2026_09/v211_reg | v2.11f | 8e3b64e | M3 S60 |
| fc_jp_movers_2026_08/v211_reg | v2.11f | 8e3b64e | M3 S60 |
| fc_de_cars_2026_09/v211g_reg | v2.11g | 1ff32f6 | M4 S72 |
| fc_us_retail_2026_06/test3 | v2.12a | cf3413e | M2 S66 |
| fc_de_cars_2026_09/v216_reg | v2.16e | 31e0021 (agent code = b77e098) | M1 S24 |

The tree commit is the latest commit of any kind before the archive run started; `03_old_versions_log.txt` shows its
agent code (`triangulate/agent`, `llm.py`, `config.py`, `expr.py`, `mc.py`, `prompts.py`, `providers.py`) is
byte-identical to the code commit, and its question bank gives the run's exact question (`06_question_identity_log.txt`).

**Same-configuration caveats found in review (v_prereg; `verify/v03_tree_commits_log.txt`,
`verify/v05_plan_tokens_launchers_log.txt`, `verify/v06_commit_copies_log.txt`).**
- The tree commit is the latest *by committer date* (author dates are not monotone along the history, e.g. d28f96b).
  For v2.8r, tree 48e6b45 differs from code commit c64d3a3 by BUGS.md, results and 148 inserted lines in
  `triangulate/forecast.py` (the test2 questions, insertions only); `worktrees.json` says "adds only BUGS.md", which is
  incomplete. Agent code is identical.
- Commit identity is also checked by content: each of the 10 code and tree commits has the same `triangulate/` code,
  differing in comment lines only, as the 24 other commits in the local object store with the same author date and
  subject. The request-identity check of E0 tests the plan prompt and question text of every new run at run time.
- The v2.1* (4 cells) and v2.1b (1 cell) originals were made by `probes/run_v2_backtests.py`: 8 runs as threads of one
  process sharing the fetch rate limiter (Wayback 1 connection, 1.5 s spacing), which explains their 39-47 min wall
  times. The repeats use the per-run CLI that EVAL_AGENT_PLAN_v2.md calls equivalent (same code path and flags; fetch
  timing and page arrival order differ). E3 and R2 are also reported without these 5 cells.

**Excluded cells (2), each stated in `excluded_cells.json`:**
- fc_kr_births_2026_07/v21c (M7, v2.1c-pre): the run started on an uncommitted working tree (f5fe773 plus unknown
  edits; DATA_NOTES §9 override, `check/CHECK.md` fix F2). No commit reproduces it.
- fc_cn_profits_2026_09/test4 (M2 S66): real-use run on its own day (40 live-dated pages, 0 snapshots). Any run with
  as_of 2026-10-24 is now a backtest, i.e. a fetch-mode toggle, not the same configuration. S66 stays covered by
  fc_us_retail_2026_06/test3.

Tags `repB_<slug>_r<k>` (`_noown` appended for noown cells, so `run.ablation_tag` leaves them unchanged), rounds 1-2.
Size: 12 cells x 2 = 24 runs (limit about 30). Total 93 runs (limit about 100).

### B4. Old-code worktrees (commands for the main session; I created none)

CLI at every tree commit (`03_old_versions_log.txt`, from `git show <commit>:triangulate/__main__.py` and
`agent/run.py`): `python -m triangulate agent --question <qid> --tag <tag> --auto-approve [--ablate-own-history]`;
results go to `<root>/results/agent/<qid>/<tag>/` (`RES = RESULTS / "agent"`, `RESULTS = ROOT / "results"`,
`ROOT` = the checkout holding the package); an existing `calls.jsonl` is renamed `calls.before_<stamp>.jsonl`;
`run.main` rewrites `<root>/results/agent/summary_<tag>.json`; raw pages go to `<root>/data/raw/agent/<qid>/`; the
Wayback cache is `<root>/data/raw/agent/_cache` with the same key and file format at every commit; the key file is
`TRIANGULATE_KEY_FILE` or `<root>/.env`; model default `deepseek-flash`; `is_peak` identical.

Create (Git Bash or PowerShell; the commits are full hashes):
```
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v21s  2bbe8aef41e35c4c85f784d97edde38e2137e493
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v21b  66e70a8808fbcdafc1cef920132c50cd64faf1c3
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v28r  48e6b45082d5165c8693e11dbd52be866bfbe363
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v211f 8e3b64ed321da839e1718e020c79ac79c808e36a
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v211g 1ff32f6ab07226b348cd1732065c1c7d98712dc6
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v212a cf3413e49bb0e99d6847c24110a75de2fcfce1c9
git -C D:/triangulate-agent worktree add --detach D:/triangulate-agent-rep/v216e 31e0021dd5cb313aa7911b9d7866a8be91ad4d71
```
Share only the Wayback cache with the main checkout (PowerShell 5.1, ASCII):
```
foreach ($s in 'v21s','v21b','v28r','v211f','v211g','v212a','v216e') {
  New-Item -ItemType Directory -Force -Path "D:\triangulate-agent-rep\$s\data\raw\agent" | Out-Null
  New-Item -ItemType Junction -Path "D:\triangulate-agent-rep\$s\data\raw\agent\_cache" -Target "D:\triangulate-agent\data\raw\agent\_cache" | Out-Null
}
```
Why the cache is shared and nothing else: pool A and every archive run read this cache (`fetch.cdx_lookup` and the
snapshot cache), so sharing it keeps pool B in the same environment as pool A and as the original runs. Raw page text
(`<k>.txt`) is not shared, because old decoders would overwrite page text that newer runs reference.

Then run the offline preflight (imports, package path, question text, junction, clean tree; no model call):
```
.venv/Scripts/python.exe -B paper/_tools/run_repeats.py --round 1 --preflight --code-root D:/triangulate-agent-rep/v21s --code-root D:/triangulate-agent-rep/v21b --code-root D:/triangulate-agent-rep/v28r --code-root D:/triangulate-agent-rep/v211f --code-root D:/triangulate-agent-rep/v211g --code-root D:/triangulate-agent-rep/v212a --code-root D:/triangulate-agent-rep/v216e
```
The same venv interpreter runs every version: `requirements.txt` at each tree commit differs from HEAD by insertions
only, so every package an old commit pins is pinned to the same version today (`git diff --stat <commit> HEAD --
requirements.txt`).

**Copy rule.** After each old-version run the runner copies `<root>/results/agent/<qid>/<tag>/` to
`D:/triangulate-agent/results/agent/<qid>/<tag>/` with `shutil.copytree` only if the destination does not exist
(otherwise it logs `copy_conflict` and overwrites nothing), and copies the run's new raw pages to
`D:/triangulate-agent/data/raw/agent_repB/<slug>/<qid>/` (no overwrite). `summary_<tag>.json` in the worktree is not
copied (scores are recomputed). Worktrees stay until `r_repeats` is verified.

### B5. runs.json fields

`qid, code_version, thinking, round, tag, purpose`, plus `pool, repeat_index, cell_id, noown, slug, tree_commit,
code_commit, code_root_hint, cli_mode, ask_question, as_of, reference_run, mechanism, margin_min, rerun_tag,
order_in_round`. Rounds: 1 = 23 A + 12 B, 2 = 23 A + 12 B, 3 = 23 A.

---

## C. Schedule and execution (implemented in `run_repeats.py`)

1. **Rounds.** One repeat of every cell per round. Round N+1 starts at least 20 h after the last run of round N ended,
   on a UTC calendar day with no start of an earlier round. Round N+1 needs every run of round N started (or its cell
   excluded or abandoned under C5).
2. **Order.** Within a round, the seeded permutation `order_in_round` (`random.Random(20261127 + round)`). A free slot
   takes the first run in that order that is startable now.
3. **Concurrency.** At most 3 runs at once; never two runs of the same question at the same time (any pools; b6 verdict 7).
   One runner process at a time (lock file). This departs from `TOPIC_DECISION.md` §4 O3 ("launch the runs one at a
   time"): b6 verdict 7 is about byte-identical prompts sent at once, which the same-question rule and the >= 20 h
   spacing of a cell's repeats exclude; runs of different questions share only the time window (v_prereg; the user
   may set `MAX_PARALLEL = 1`, about 22 h of run time instead of about 8).
4. **Peak hours.** A run starts only if no minute of `[now, now + margin_min]` is in a DeepSeek peak window
   (`config.is_peak`: Mon-Fri 01:00-04:00 and 06:00-10:00 UTC). `margin_min = max(20, ceil(1.5 x the longest archived
   thinking-off wall time of that version))`: v2.17a 27, v2.1* 71, v2.1b 62, v2.16e 23, others 20 minutes.
5. **Skip and re-run rules.** A run whose `state.json` exists (in its root or the main checkout) is skipped. A run with a
   `start` event in the round log is never started again. **Infrastructure failures** may be re-run **once**, under the
   run's `rerun_tag`, with `--rerun-infra`, and are logged. The classes (function `classify_infra`): `timeout` (90 min);
   `crash_no_state` (no `state.json`); `http_401/402/403` (key or balance; any call, or "insufficient balance" in the
   abort text); `api_rejected_400/404/422`; `no_model_call` (no call with `ok`); `network` (no estimate and a transport
   error in the abort text or in the stderr of a failed process). Everything else is an outcome and is never re-run:
   no estimate, invalid or truncated judge JSON, a budget-cap abort, any error size.
   - (v_prereg) `api_rejected_*` applies only to a run without an estimate: a 400/404/422 on some call of a run that
     still estimated is an outcome (the archive has no such code in 14,678 calls, `verify/v02_http_codes_log.txt`).
     Added class `interrupted`: a logged start without an end event and without `state.json`, older than 2 x the
     timeout (runner killed, reboot, power loss). If its `state.json` appears later (orphaned child), the original run
     counts and its re-run is reported but not used.
   - (v_prereg) Order: round N+1 does not start while a round-N run has an infrastructure class or is interrupted and
     its once-only re-run has not started, unless its cell is abandoned; the re-runs are logged in round N's log, so
     the 20 h gap and the calendar-day rule count from them.
   - A cell is **abandoned** (listed in `abandoned_cells.json` by the main session, with the reason, as a logged
     deviation) only if its preflight fails, or both its run and its infra re-run fail with an infrastructure class
     other than `crash_no_state`. A run that crashes twice with the same Python exception in the agent code is an
     outcome of that configuration (counted as "no estimate, crash").
   - After an HTTP 401/402/403 the runner stops starting runs.
6. **Code freeze** for the whole batch: the main checkout must keep `HEAD:triangulate = 7eaec1e4...` with no
   uncommitted change under `triangulate/` (checked before every start; a violation stops the batch); a worktree must
   sit on its tree commit with a clean `triangulate/` and the cache junction. `TRIANGULATE_THINKING`,
   `TRIANGULATE_CONCURRENCY`, `TRIANGULATE_THINKING_EXTRA` must be unset and `TRIANGULATE_MODEL` unset or
   `deepseek-flash`.
7. **Money.** Hard stop: no run starts once the summed token fees of the batch (all `calls*.jsonl` `usd` of every
   runs.json run dir, counted once, plus the leakage-check calls) exceed $30. Guard: no run starts if fees so far +
   $0.70 x (running + 1) would exceed $30 ($0.70 = 2 x the largest v2.16-regression token fee, $0.341).
8. **The per-run cap.** `RUN_USD_CAP = $3.00` (`triangulate/agent/pipeline.py` line 704) counts token fees plus the
   assumed $0.01 per search; the cap can abort a run when spent + in-flight reservations exceed it. Evidence it will not
   bind on v2.17a: 0 cap aborts in the archive's 52 deepseek CLI runs with the $3.00 cap (and in its 158 with the
   older $1.00 cap); the largest v2.17a `usd_total` is $1.99 (a peak-hour run; off-peak thinking-off maximum $1.66); the in-flight reservation is at most about 8 x $0.099 (8
   concurrent searches: 30,000 input tokens and 8,192 output tokens at peak price plus 8 assumed searches) = $0.79, so
   at most $2.79 < $3.00 (`04_cost_cap_log.txt` [1], [2]; `pipeline.Budget`). Old versions have a $1.00 cap; the
   archived maximum `usd_total` under it is $0.87 (a v2.11f run) with 0 aborts in 158 runs (`04_cost_cap_log.txt` [5]). If a cap abort happens, it is an outcome of
   that configuration (category `aborted_budget_cap`), reported separately and never re-run; a sensitivity analysis
   drops such runs. The assumed search fee is not money (DeepSeek no longer bills server-side search separately since
   2026-11-18 12:00 Beijing time), so `usd_total_assumed` overstates the real cost by about $1.27 per v2.17a run.
   The `usd` of a call is the code's own estimate from `config.PRICES` (the same deepseek-flash table at every version
   used), not the bill; the $30 stop applies to these recorded fees (v_prereg note).
9. **Logs.** `paper/prereg/batch_round<N>.log` (JSON lines: invocation, plan, start with command, commit, tree, env
   changes; end with exit, wall time, infra class, run fee and batch fee, HTTP status counts and the first plan call's
   prompt_tokens (v_prereg); copy; skip; stop; infra_interrupted), per-run stdout/stderr tails
   in `paper/prereg/out_round<N>/`. Deviations go to `paper/prereg/DEVIATIONS.md` (main session), each with time and
   reason.

Invocation per round (after the leakage check for round 1):
`.venv/Scripts/python.exe -B paper/_tools/run_repeats.py --round N --code-root <each worktree>`.

---

## D. Direct-ask leakage check (once, right before round 1)

**D1. What.** For each of the 23 scored questions, one call of the naive direct-answer arm exactly as
`probes/naive_ask.py` builds it: `arms._messages(prompts.NAIVE_SYSTEM, q)`, model deepseek-flash, thinking disabled,
`response_format` json_object, temperature 0, `max_tokens` 500 (`config.MAX_TOKENS["naive"]`), attempt 1, no retry
message; arm label `naive` (the archive arm's label; with `TRIANGULATE_THINKING` unset the request is identical to
`naive_ask`'s). For the two test4 questions `q = forecast.with_as_of(q, "2026-10-24")`, the as_of of their archived
naive answers. `run_repeats.py --leak-check` writes `leak_check/calls.jsonl`, `answers.json`, then `decision.json`.

**D2. Reference.** The archive's thinking-off naive answers (`leak_reference.json`, built by `07_leak_reference.py`):
17 from `results/forecast/raw/naive/` (calls 2026-10-15..19), 4 from `results/test3/raw/naive_off/` (2026-10-23),
2 from `results/test4/raw/naive_off/` (2026-10-24); all 23 are single valid attempt-1 replies. The baseline copies in
`results/agent/summary_*.json` match the canonical baseline file except in pre-G8 summaries (DATA_NOTES §5). The system prompt, user
template, `unit_display` and `_messages` are identical at HEAD and at every commit current when those answers were made
(`05_naive_prompt_identity_log.txt`), and the request body (thinking disabled, json_object, temperature 0, max_tokens,
stream false) is unchanged (`providers.py` 137-140; `llm.py` at 3a9cca5 line 39). The new call's `prompt_tokens` is
compared with the archived call's and reported. (v_prereg: because the request text is identical by construction, a
difference means a hosted-model or tokenizer change, the case most prone to leakage; such a question stays in the
shift test, and if all 23 differ the decision record flags `tokenizer_or_hosted_request_changed`. The earlier rule
"leaves the shift test" would have switched the shift test off in exactly that case.)

**D3. Decision rule** (implemented in `leak_decide`). Both replies go through `check_naive(reply, answer_unit, strict)`
into the scoring unit; truth = `answer_value` or `TEST4_OFFICIAL[qid].value`.
- A **hit** on question q: the new answer is within 0.5% of the truth, the October answer was not, and the new
  |ln error| is at most a quarter of the October one.
- **Shift test:** d_q = |ln err_Oct| - |ln err_new| over questions with both answers valid (v_prereg: no
  prompt-token filter, see D2);
  exact one-sided sign-flip test of mean d > 0 (zeros dropped; Monte Carlo with 10^6 draws if more than 16 non-zero).
- **STOP** if hits >= 4, or (hits >= 2 and shift p < 0.05), or shift p < 0.01: no agent run is made; O3 ends; the
  check is reported as the result ("blind same-configuration repeats could not be made on this hosted model").
- **EXCLUDE** otherwise, if hits >= 1 or a new answer is invalid: those questions are dropped from pools A and B in all
  rounds; the batch goes on.
- **GO** otherwise.
- Under "the hosted model changed but knows nothing" with a per-question hit chance of 2%, P(hits >= 2) = 0.077 and
  P(hits >= 4) = 0.001 (`09_mde_log.txt` [6]); the rule rarely stops a clean batch.
- Reported in any case: the number of answers identical to October's (a hosted-model drift indicator for this prompt).

**D4. Why it matters here.** The agent's plan, judge, assumptions and the v2.15d magnitude gate (a no-retrieval rough
estimate) all draw on model memory. Memory of released values would pull same-config runs toward the truth and shrink
their spread, which favours the thesis (a smaller floor). So the rule errs towards excluding.

**D5.** The check runs once. Round 1 must start within 24 h of it; otherwise it is repeated once, logged as a
deviation, and the later result governs. (v_prereg: the runner refuses a second check while `leak_check/answers.json`
exists; the main session renames the folder to `leak_check_1/` first, and the batch fee then also counts
`leak_check_1/calls.jsonl` by hand, about $0.001. A call that fails with a transport, key or balance error aborts the
check before `answers.json` is written; such a check is re-run whole and logged, it is not an invalid answer.)

---

## E. Analysis plan (executed later by the unit `r_repeats`; verified by `v_r_repeats`)

**E0. Common rules.**
- Scoring: the canonical rule of DATA_NOTES §4: `est = est_raw x unit_factor` (from `plan.target.unit_canonical` to the
  registered `answer_unit` with the repo's unit library); `ln_err = ln(est/truth)`; catastrophic = |ln err| > ln 2;
  w10 = |est/truth - 1| <= 0.10; power-of-ten slips count as catastrophic.
- `r_repeats` rebuilds the tables with `paper/analysis/data/build.py` plus an override that takes code_version,
  code_commit and pool from `runs.json` for every batch (qid, tag); build.py's date-based version mapping would label
  pool-B runs v2.17a. It checks that every archive row of the rebuilt `runs.csv` equals the frozen pre-batch file.
- "As-is" = the archive's 115 scored runs in the frozen `runs.csv` (rule A, all versions). The as-is value is recomputed
  with the same code on the same question set as its same-config counterpart; the verify-file values are quoted next
  to it.
- Unit of independence: the question. Primary tests are exact sign-flip tests over questions (all 2^G patterns if
  G <= 20, else 10^6 draws, seed 20261127), two-sided unless stated. CIs for means: t intervals over questions
  (G - 1 df). Rates with <= 5 events: Clopper-Pearson on runs and on questions-with-an-event, rule of three if 0.
  Percentile and wild cluster bootstraps (Webb weights) are secondary and go to the appendix; c5's coverage results are
  cited for each method used.
- Missing estimates: excluded from spreads, counted in the no-estimate rate; for aggregation, the median of the
  available estimates (P0 convention, as a2) with the P1 convention (no answer = failure) as secondary.
- Budget-cap aborts, infra failures and abandoned cells are reported in a flow table (planned 93, started, infra
  re-runs, abandoned, with estimate).
- (v_prereg) **Request-identity check.** The first `plan` call's `prompt_tokens` (logged in each end event) depends only
  on code and question (equal in all 3 same-configuration archive cells; `verify/v05_plan_tokens_launchers_log.txt`
  [b] lists every reference). Pool-B runs are compared with their original catastrophic run, pool-A runs with the
  question's v2.17a archive run (10 questions) and otherwise with each other. A pool-B cell whose repeats differ is
  "request changed" (its plan prompt or question text is not what the original ran, e.g. a difference that git does
  not show): it leaves E3, R2 and F2 and is reported separately. It detects changes of the plan prompt and question
  text only.
  It is not checkable, and reported so, if the leakage check flags `tokenizer_or_hosted_request_changed`.
- (v_prereg) **Zero spread.** For log-variance statistics (E1, V1, V1b), a cell whose estimates are all equal to 6
  significant digits gets s_c^2 = 1e-6 (an SD of 0.001 in ln); the number of such cells is reported, and a
  sensitivity drops them.
- (v_prereg) **Label precedence and direction.** If a row is both "different" and "nearly equal", its label is "nearly
  equal (p < 0.05)": a difference inside the margin is not read as support. A "different" row whose sign is opposite
  to the thesis (as-is variance below the pool-A floor, or as-is K = 3 gain below the same-configuration gain) is
  labelled "different, against the thesis".
- (v_prereg) **Drift detected** (used by the E2 sensitivity) means E4 test (i) or (ii) has p < 0.05.

### E1. Repeat floor
Per cell c (pool A: 23 cells; pool B: 12 cells, the 2 new runs only):
- s_c = SD of ln estimate (ddof 1), on all estimates and on non-catastrophic estimates ("core");
- catastrophic rate and no-estimate rate.
Pooled (pool A, primary): typical repeat variance = exp(mean_c[ln s_c^2 - k(df_c)]), with
k(df) = digamma(df/2) + ln(2/df) (the expected log of a chi-square variance estimate), t interval over cells; secondary:
the pooled SD (sum (n_c - 1) s_c^2 / sum (n_c - 1))^1/2. Cells enter with >= 2 estimates (all) or >= 2 core
estimates (core). Pool-A catastrophic rate k/n (n = pool-A runs with an estimate) with Clopper-Pearson, tested
against the as-is tail rate 11/108 = 10.2% (`a4_failures/verify/VERIFY.md` F4) with an exact one-sided binomial
(secondary). (v_prereg: 10.2% is kept as p0 because it is the more conservative of a4's 11/108 and the frozen
`runs.csv` rate 14/115 = 12.2% (`verify/v01_counts_log.txt` [2]), which is reported next to it; the binomial treats
the 3 runs of a question as independent and is anti-conservative under clustering, so the count of questions with a
catastrophic pool-A run is reported with it.) Pool B's floor is reported separately; it is conditional on a
catastrophic original.

### E2. Same-configuration counterparts of the audited as-is statistics
Each row: as-is value [CI] (n_q, n_runs) | same-config value [CI] (n_q, n_runs) | difference [CI] | exact p | label | MDE.

| row | statistic | as-is source (value) | same-config version |
|---|---|---|---|
| **V1 (P1)** | within-question variance of ln est, core | archive scored non-catastrophic runs per question | pool A core; per question L_q = [ln s2_asis - k(df_asis)] - [ln s2_A - k(df_A)]; statistic mean L_q; questions with >= 2 core estimates on both sides |
| V1b | same, all estimates | | |
| **K1 (P2)** | K = 3 median gain on w10 | a2 (`a2_aggregation/verify/VERIFY.md` §1-2: +0.132 [+0.070, +0.198], 16 q; v2.12a+ +0.003; within era +0.119) | per question: w10(median of the 3 pool-A runs) - mean w10(single); as-is per question by enumerating all 3-subsets of its archive scored runs; d_q = as-is - same-config over questions with >= 3 archive runs |
| K2 | K = 3 catastrophic-rate reduction | a2 | same construction with the catastrophic indicator |
| R1 | A - B3, A - C(ln 2), A - D-med3[rs, 0.2] catastrophic rate; w10; E[runs]; E[token USD] | a5 (`a5_policy/verify/VERIFY.md` H1: A 11.33%, B3 3.27%, D-med3 3.07%; first-run reduction +4.9 pp any partner, +3.0 pp same-or-older) | pool A, exact enumeration of the 6 orderings of each question's 3 repeats; D-med3 threshold = leave-one-question-out question-weighted 80th percentile of route spread over pool-A runs (single route = flagged), as a5 PREREG; secondary: the as-is threshold |
| R2 | rescue of the archive's catastrophic runs | a5/c2: partners from any version vs same-or-older (e.g. DE cars v216_reg 0.000 vs 0.800, `a5_policy/verify/VERIFY.md` M1) | pool B: original run + its 2 same-config repeats; B3 = median of 3; C(ln 2) with repeat 1 as second run; D-med3 with the a5 trigger; rescue rate = share of cells whose policy answer is not catastrophic |
| F1 | leave-one-out 2x flag: false alarms, catches, AUROC | a1 (`a1_signal/verify/VERIFY.md` H2: AUROC 0.983; later-only 13/13, 0/56; earlier-only 6/6, 8/63) | pool A: each run against the median of its cell's other 2 runs; AUROC only if >= 2 catastrophic runs on >= 2 questions; per-question false-alarm difference with sign-flip |
| F2 | catch of the archive's catastrophic runs by same-config references | a1 (13/13 with any references) | pool B: is the original flagged against its 2 repeats |
| M1 | MC share: within-cell SD / MC SD | b6 verdict 4 (ratio 59 [20, 279] across versions; 17.9 median on the 3 same-config cells) | pool A; MC SD from offline own-version compute replays of each pool-A run with the 8 alternative seeds b6 used (no model call) |
| B1 | bias share of non-catastrophic MSE (unbiased decomposition) | `a2_aggregation/verify/VERIFY.md` §1 item 2 (about 0.21; variance share 0.790 [0.422, 1.015]) | the same estimator on pool A |
| S1 | systematic share of squared error | `b4_baselines/verify/VERIFY.md` H1 (all agent runs 0.02 [-0.004, 0.14]; questions without a catastrophic run 0.26 [-0.06, 0.73]; thinking toggle 0.80 [0.22, 0.94]) | the b4 estimator on pool A (3 repeats instead of a toggle pair) |

Labels (fixed now) for V1 and K1, and descriptively for the rest:
- **different**: Holm-adjusted sign-flip p < 0.05 (P1, P2) or unadjusted p < 0.05 (others);
- **nearly equal**: the 90% CI of the difference lies within the margin: V1 |mean L| <= ln 2 (variance within a factor
  2); K1/K2/R1 within +-0.05 (5 pp); F1 false-alarm rate within +-0.05;
- **inconclusive** otherwise.
Precedence and direction: E0 (v_prereg).
**R2 primary (v_prereg).** Per cell, d_c = same-configuration B3 rescue (1 if the median of the original and its 2
repeats is not catastrophic, else 0) minus a5's `p_rescue_med3_any` for that original run
(`a5_policy/verify/v04_rescue_by_version.csv`); statistic mean d_c over the cells, exact two-sided sign-flip p
reported; label "same-config rescues at least as well as cross-version partners" if mean d_c >= 0, else "same-config
rescues less". `p_rescue_med3_not_later` (where a5 defines it) is reported next to it; C(ln 2) and D-med3 rescue are
descriptive.
Each row is also reported under c1's rules B-E where c1 has computed them (context, no new test).
Sensitivity for every row: without the two test4 questions; adding the 2026-11-24/25 v2.17a runs as a fourth repeat
(only if E4 detects no drift); excluding exposed runs (E5).

### E3. Pool B: recurrence and regression to the mean
- Per cell: k_c of 2 repeats catastrophic; also "same sign and the same mechanism" read from the state (route inputs,
  as a4 F1 did), reported per cell.
- Pooled recurrence rho = sum k_c / 24, Clopper-Pearson on runs and a t interval over the 12 cell means; mechanism
  level (M1-M6) k/n. Labels (the wider interval decides): "mostly deterministic" if the lower bound >= 0.5, "mostly
  chance" if the upper bound <= 0.5, else "mixed". (v_prereg: precisely, a label applies only if both intervals meet
  its condition, the t interval clipped to [0, 1]. The denominator is the repeats with an estimate, sum n_c; a repeat
  without an estimate is reported and, in a sensitivity, counted as a recurrence (P1 convention). Also reported
  without the 5 cells launched in-process in October, B3.)
- As-is improvement after the fix: for each cell, Y_after = catastrophic indicator of the next archive scored run of
  the same question (started later, same thinking and noown flags, later code version); I_c = 1 - Y_after. Cells
  without such a run (fc_us_retail_2026_06/test3) stay in rho but not in the share.
- Expected improvement from re-running the same configuration (regression to the mean) E_c = 1 - rho_c.
- RTM share = sum E_c / sum I_c over cells with an after-run; interval from the Clopper-Pearson interval of the pooled
  rho. Labels: "mostly regression to the mean" if the interval lies in [0.5, inf), "mostly the fix" if within
  [0, 0.2], else "mixed".
- Reading: high rho means same-config re-running would not have rescued these runs, so the as-is aggregation and re-run
  gains on them came from version mixing; low rho means they were chance events of their configuration and the as-is
  fix improvements are largely regression to the mean.

### E4. Drift anchor
The 10 archive runs on v2.17a with thinking off (ca_rail, es_transit, hk_visitors, jp_births, kr_online, lhr_pax,
pola_teu, tw_births, us_starts `v216_reg`; de_cars `v217a_try`, made at peak hours, which in the code only sets the
price, `config.is_peak` / `usd_cost`, v_prereg) against the pool-A runs of the same
question. Under no drift the archive run is exchangeable with the 3 new runs. Tests on the 9 with an estimate:
(i) number lying outside the range of the 3 new runs, exact one-sided binomial with p = 0.5; (ii) sum of (rank - 2.5),
exact two-sided (direction). (v_prereg: an archive estimate equal to the minimum or maximum of the 3 new ones is not
"outside"; ranks are mid-ranks.) ES transit (archive no estimate) and process metrics (searches, pages, points, token
fee, wall time, searcher-call input and output tokens, plan prompt_tokens) are compared descriptively. MDE: only gross drift is detectable (P(outside) >= 0.91, `09_mde_log.txt` [5]).
The October-to-November drift of the hosted model is not identified by this anchor; the leakage check's
identical-answer count is the only (prompt-level) indicator.

### E5. Leakage exposure (the c6 fields)
Per run, for the new runs and for every archive run of the same questions, recomputed uniformly offline:
- query hits: searcher queries containing a registered value (`ev.leak_patterns` / `ev.leak_scan` with HEAD's
  registered values: leak_values plus the truth; for test4 the `TEST4_OFFICIAL` value), split into truth hits (exact,
  rounded) and other registered values (as `topic/checks/check_7_counts.py` [A]);
- sentinel hits: pages excluded by the live sentinel (`state.leakage.sentinel_hits`, page `leak_hits`); for the two
  test4 questions, which ran without registered values, the stored page text is scanned with the same patterns;
- post-as-of dates: searcher-proposed URLs (`results[*].search.urls`) with an explicit date after as_of (`fetch.URL_DATE`
  regex, as `topic/proposals/benchmark_counts.py`), plus `points_dated_after_as_of`, `snapshots_after_as_of`,
  `late_dates_in_text_sent`, `directions_voided`.
Comparison: per question, mean of the new runs minus mean of the archive runs; exact sign-flip over questions; share of
runs with >= 1 truth query hit. The new runs are expected to be more exposed (the values are public); no claim is made
that exposure changes scores (zhang2026backtesting). Sensitivity of E1-E3: drop new runs with a truth query hit, with
any query hit, or with a post-as-of URL in the final combination (c6 sets (a)-(c)).

### E6. Minimum detectable effects (`09_mde_log.txt`)
- Sign-flip / paired comparisons over G questions (alpha 0.05 two-sided, power 0.8): 0.611 SD of the per-question
  difference at G = 23, 0.749 at G = 16, 1.27 at G = 7. A rare binary difference needs >= 6 questions differing in one
  direction to reach p < 0.05.
- V1: per-question log-variance-ratio sampling SD about 1.79 (normal errors) gives an MDE of a variance ratio of about
  3.0 at G = 23 and 3.8 at G = 16 (SD ratio 1.7-2.0). "Nearly equal" (within a factor 2) is reachable only if the
  estimate is close to 1. (v_prereg: the G that applies: V1 at most 21 questions, the as-is side has >= 2 core
  estimates on 21 (`verify/v01_counts_log.txt` [12]), about 3.3; K1/K2 17 questions with >= 3 archive scored runs,
  0.72 SD by interpolation of `09_mde_log.txt` [1].)
- Pool-A floor: 46 df give a 95% CI factor [0.83, 1.26] on the pooled SD under normal errors; wider with a tail.
- Pool-A catastrophic rate: 0/69 gives an upper bound of 4.3%; against the as-is 10.2% the exact test rejects with <= 2
  events and reaches power 0.8 only if the true rate is <= 2.2%.
- Pool-B rho on 24 runs: 12/24 gives [0.29, 0.71]; H0 rho = 0.9 is rejected with <= 18 recurrences (power 0.77 at
  rho = 0.7, 0.997 at 0.5).
- Drift anchor: see E4. Leakage check: see D3.

### E7. Confirmatory vs exploratory
- **Primary confirmatory (Holm over the two):** P1 = V1 (core variance ratio, as-is vs pool A); P2 = K1 (K = 3 w10
  gain, as-is vs pool A).
- **Primary estimation with pre-set labels (no test):** E3 rho and the RTM share; R2 rescue rate vs the as-is rescue
  (label rule in E2, v_prereg).
- **Secondary confirmatory (pre-specified, unadjusted, labelled secondary):** V1b, K2, R1, F1, the pool-A
  catastrophic rate vs 10.2%, E4, E5.
- **Secondary descriptive (v_prereg; no test, point estimate with the interval method of the cited source analysis):**
  F2, M1, B1, S1. (They had been listed as secondary confirmatory without a test.)
- **Exploratory:** per-mechanism breakdowns beyond E3; extraction agreement among pool-A repeats on identical snapshots
  (c4 metrics); query, URL and page overlap among repeats vs across versions (b3/b7 metrics); cost and wall time;
  time-of-day and order effects; the four 2026-10-20 v2.9a thinking runs of O2 questions (section F).

### E8. What the paper will show
- **Main table row block "same-configuration"** (one row each): V1, K1, R1 (A - D-med3), F1, E3 rho, E3 RTM share, with
  the columns of E2 and the label; plus the updated cell count (23 pool-A cells with 3 runs; 12 pool-B cells with
  3 runs, the original included).
- **Figure `r_strips`**: per question, ln err of the archive runs (colour = version order, marker = thinking) next to
  the 3 pool-A repeats; the visual form of "revisions, not repeats".
- **Figure `r_variance`**: per-question as-is variance vs pool-A floor (log-log, identity and factor-2 bands), pooled
  ratio with CI.
- **Figure `r_recurrence`**: pool-B cells grouped by mechanism: original error, two repeat errors, recurrence.
- **Appendix tables**: E1 per cell; E2 full rows (V1b, K2, R1 full, F2, M1, B1, S1); E3 per cell with Y_after; E4 per
  question with ranks and process metrics; E5 per metric; D leakage-check rows; the flow table.
- `numbers.csv` gains, for every new number: estimand "same-configuration repeat, late November 2026", admissible rule
  "pool A" or "pool B", number of cells.

---

## F. O2: one confirmatory statement on the 13 prospective questions (frozen now)

**F1. Material.** The 22 prospective runs on the 13 questions listed in `topic/checks/check_9_counts_log.txt`
(fc_byd_rev_2026_q3, fc_de_unemployed_2026_10, fc_eqnr_prod_2026_q3, fc_googl_tokens_2026_q3, fc_jnto_2026_09,
fc_kr_births_2026_08, fc_meta_capex_2026_q3, fc_mx_exports_2026_09, fc_tw_restaurants_2026_09, fc_uk_carprod_2026_09,
fc_uk_homesales_2026_09, fc_uk_mortgages_2026_09, fc_us_milk_2026_09), listed in `prospective_runs.json`
(`08_prospective_log.txt`): frozen code v2.5.2 (2), v2.8r (6), v2.13b (10), v2.14a reruns (4); 19 with an estimate,
all started before their registered release (check_9). Secondary set (exploratory): the four v2.9a thinking runs
`test2_think` of 2026-10-20 on googl_tokens, meta_capex, tw_restaurants and us_milk (eval_role
`no_truth_registered`, "question already used during development").

**F2. The statement.** Once first-release official values are registered (F4), `o2_score.py` reports on the 22 runs:
- (a) the frozen pipelines' catastrophic rate: runs with |ln(est/official)| > ln 2 out of the runs with an estimate on
  questions with a comparable official value, with Clopper-Pearson, the exact one-sided upper bound (rule of three if
  0), and the number of questions with a catastrophic run (no-estimate runs, 3 of 22, are reported but are not an
  outcome);
- (b) **primary:** the false alarms of the magnitude gate replayed offline exactly as `b6_probes/verify/v07_magnitude.py`
  did: flag if max(est/ref, ref/est) > 2.0 (`magnitude.RATIO`), ref = the question's archived thinking-off naive answer
  (final attempt through `check_naive`); false alarms = flags on non-catastrophic runs, as k/n with the exact upper
  bound (rule of three if 0); catches = flags on catastrophic runs;
- (c) the false alarms and catches of the past-only flag: |ln est - median ln est of the earlier runs| > ln 2, using
  every earlier scored-task run of the same question with an estimate in the same unit (evaluable on 8 runs).
- Secondary: the same with last year's value as the reference (`runs.csv` `last_year`), for C3's free-reference bound.

**F3. What supports or contradicts which claim.**
- Gate (C2: archive-tuned thresholds borrow from the archive; in-sample 13/13 caught and 0/82 false alarms inside a
  1.88x-2.22x band, out of sample 1/1 and 0/19, `b6_probes/verify/VERIFY.md` verdict 10): **supports C2** if at least
  one false alarm or one missed catastrophic run occurs; **cuts against C2 for the gate row** if 0 false alarms and every
  catastrophic run is caught; the paper then reports the gate's transfer with the exact upper bound.
  (v_prereg, strength: a missed catastrophic run is a direct counterexample; false alarms alone count as "supports C2"
  only if the one-sided Fisher exact test of k/n false alarms against the in-sample 0/82 gives p < 0.05, which needs
  about 2 false alarms on about 17 runs; 1 false alarm with p >= 0.05 is reported as "weak, not significant support".
  `o2_score.py` prints only the direction; the strength is computed from its counts in the O2 report.)
- Past-only flag (C2: earlier-only 8/63 false alarms in-sample, a1 H2): descriptive only, with about 8 evaluable runs
  (v_prereg: the earlier wording "consistent with C2 if its interval overlaps 12.7%" could not fail and is dropped).
- Catastrophic rate: no directional prediction. It is compared with the in-sample tail 10.2% (a4 F4); if its 95% upper
  bound is below 10.2%, the paper says the in-sample tail rate was not reproduced on unseen questions.

**F4. Lookup protocol (a separate unit `o2_lookup`, which never edits this file, `prospective_runs.json` or
`o2_score.py`; a second unit `o2_lookup_check` repeats it independently).**
- Before the lookup the main session records the SHA-256 of this file and `o2_score.py` in `o2/frozen_hashes.txt`.
- The unit receives only the 13 question ids, their question text or template, and the `source`, `released` /
  `expected_release` fields of `forecast.py`. It does not see the agent estimates.
- Official sources only: the publisher named in the question (statistics office, central bank, ministry, or the
  company's own results release or filing). Search engines and secondary sites may be used only to find the official
  page.
- First release: the value as first published for the target period. If the page now shows a revised value, the unit
  finds the first release (press release, PDF, or a Wayback snapshot dated on or after the release date and before the
  next release) and records both.
- Per value: qid; verbatim quote; value and unit as written; scale words; the value converted to the question's
  `answer_unit` (count questions: plain count; scale words expanded exactly, e.g. million, 億, 万; `mboe/d` -> `boe/d`
  x 1000 as in `TEST4_SCORING_NOTES`), using the repo's unit library as in DATA_NOTES §4; release date from the
  document; URL; Wayback URL if used; access time; any definitional mismatch. A definitional mismatch means
  `status = "no_comparable_value"` and the question leaves all three parts (reported).
- Output `paper/prereg/o2/official_values.json`: `{qid: {"status": "ok" | "no_comparable_value", "value_in_answer_unit",
  "quote", "unit_as_written", "release_date", "url", "wayback_url", "accessed_at", "notes"}}`. The two lookups must
  agree to 3 significant figures; a disagreement goes to a third lookup and is recorded.
- (v_prereg) Ambiguous cases. (i) Third lookup: the value two of the three lookups agree on is used; if all three
  differ, `no_comparable_value`. (ii) A value stated only approximately ("about", "nearly") or as a bound ("more than",
  "over", "at least") is recorded with its number and a flag in `notes` ("approximate" / "bound"); it is used, and the
  O2 numbers are also reported without flagged values. (iii) A value given only on another time base or aggregation
  than the question asks (e.g. per month for a per-minute question, Jan-Sep for a single quarter) is
  `no_comparable_value`; no conversion across time bases. (iv) Where the question names earnings-call remarks
  (fc_googl_tokens_2026_q3), the company's own transcript, webcast or investor-relations post counts as official.
- The values are written only to `paper/prereg/o2/`, not into `triangulate/forecast.py`. Blindness can only be attested:
  the values have been public since October 2026.

---

## G. Literature reporting-gap count (`check_2.md` §3, objection 1)

**G1. Population.** All 77 records of `paper/lit/verified_papers.json` (generated 2026-11-27), plus a fixed extension:
the papers opened and cited in `TOPIC_DECISION.md` §6 that are not records there: Hardy et al. arXiv 2610.00651;
He arXiv 2610.14662; Wiedmann et al. arXiv 2610.01618; Ding et al. arXiv 2610.14460; Heineman et al. "Signal and
Noise" (NeurIPS 2025); Ben Sghaier et al. arXiv 2607.03691; Baltes and Treude arXiv 2610.35348; Zhu et al. arXiv
2602.03238; Bowyer et al. arXiv 2503.01747. No other paper is added (no new search), so the population is fixed now.

**G2. Screening (inclusion).** A paper is in the coded set if it (i) reports its own experiments with an LLM-based
agent or agentic system (multi-step, with tools, retrieval or environment actions), and (ii) reports at least one
result computed from two or more runs of the same task: repeated runs, K-run aggregation or selection, run-to-run
variance or consistency, disagreement across runs, or comparisons across system versions evaluated on the same tasks.
Excluded: single-call LLM tasks without agentic steps; papers without own experiments (surveys, position papers,
pure theory); only single-run results. Both coders screen all 86 candidates.

**G3. Items** (each coded Yes / Partial / No with a verbatim quote and its location; sources = the arXiv version current
on the coding day including appendices, or the proceedings version; the official repository README only for V):
- **V (version per run):** Y = a code or harness version identifier (commit, tag, release number) is given for every
  reported run or result set, or one identifier is stated for all experiments; P = the harness or code is named or
  linked without an identifier, or identifiers exist for some results only; N = none.
- **S (same-configuration count):** Y = the number of repeats per configuration behind each multi-run statistic is
  stated (e.g. "5 runs per task per model"), or a same-configuration cell count; P = a number of runs is stated but it
  is unclear whether the runs share one configuration; N = none.
- **T (timing of repeats):** Y = states whether repeats were concurrent, sequential or spaced (dates, intervals or
  schedule); P = only the overall experiment period; N = none.
- **D (development vs held-out):** Y = says that the evaluated configuration was frozen before the reported runs, or
  that development runs and reported runs (or tasks) are separated and reported separately; P = a dev/test task split
  is mentioned without saying whether development used test runs; N = none.
- Auxiliary (not headline): **M** model snapshot identifier per run (Y/P/N); **R** whether a multi-run statistic pools
  runs of different system versions (yes / no / unclear).

**G4. Coding rules for ambiguous cases.** The model snapshot (an API model name with date) is not a harness version (it
goes to M). A benchmark version is not a harness version. A GitHub link without commit or tag is P for V. "Averaged over
3 seeds" counts as S = Y only if the seeds are runs of the agent, not of data splits. Temperature-0 claims of
determinism without repeats do not make a paper multi-run. Leaderboard or meta-analysis papers are coded on their own
experiments; if they re-analyse others' runs, items refer to the runs they analyse. Released traces count only if the
paper states the per-run field (artifacts are not inspected). When in doubt between two codes, the lower one is used and
the case is flagged. (v_prereg) For S and T, a statement that covers some multi-run statistics of the paper but not
others is P. A paper that states each configuration was run once (and reports only cross-version comparisons) is
S = Y with count 1.

**G4b. Strata (v_prereg).** Criterion G2 (ii) admits papers whose only multi-run result is a comparison across system
versions (ablations), which would dominate and inflate the gap count. Every headline count is therefore reported for
all included papers and separately for (a) papers with at least one statistic over repeated runs of one configuration
(repeats, K-run aggregation or selection, run-to-run variance or consistency, disagreement across runs) and (b) papers
whose only multi-run results are cross-version comparisons. The stratum is coded by both coders and enters kappa.

**G5. Coders and agreement.** Coder 1: an LLM unit (`lit_gap_1`) with web access to the papers. Coder 2: independent
and blind to coder 1 (human preferred; see decisions). Double-coding subset: 20 included papers drawn after screening
with `random.Random(20261127).sample(sorted(bibkeys), 20)` (all if fewer than 20); coder 1 codes all included papers.
Reported per item: percent agreement and Cohen's kappa on the subset; disagreements are resolved by discussion and
listed. Headline: for each of V, S, T, D, the count of Y / P / N among the included papers with Wilson 95% intervals,
compared with Baltes and Treude's 15 of 325 experiments with an exact harness version (as context, not a test).

---

## H. Budget, time and stopping

- **Runs:** 93 agent runs (69 pool A, 24 pool B) + 23 direct-ask calls; at most one infra re-run per run.
- **Token fees** (the search fee is no longer billed; `04_cost_cap_log.txt`):
  - pool A: 69 x median $0.214 = **$14.75**; at the v2.16-regression maximum $0.341: $23.55;
  - pool B (October token fees per version, x 1.12 for the post-2026-11-18 rise of searcher-call fees, median $0.00374
    vs $0.00335 per call): medians give **$3.31**, archived maxima give $5.45;
  - leakage check: about $0.001 (archived naive calls cost $0.00004-0.00005 each);
  - **expected about $18; high scenario about $29.** Hard stop at $30 (C7).
- **Wall time:** pool A median 12.1 min per run (maximum 20.4, v2.16 regression); pool B by archived medians: v2.1*
  43.6 min (made 8 at once in October), v2.1b 38.7, v2.16e 14.6, v2.8r 6.3, v2.12a 5.1, v2.11f 3.8, v2.11g 3.3. About
  22 run-hours in total; with 3 lanes about 3.0 h for rounds 1 and 2 and 1.6 h for round 3, plus waits for off-peak
  windows (weekdays 10:00-00:40 and 04:00-05:40 UTC with the 20-minute margin; weekends all day). At least 3 calendar
  days.
- **Stopping:** the $30 stop and guard; a leakage STOP; an HTTP 401/402/403 (runs stop; after a top-up the round
  resumes and the 402 runs are infra re-runs); a code-freeze violation. Rounds already completed are analysed; a partial
  round is analysed with its missing cells reported; no top-up runs beyond `runs.json`.

---

## I. Things this plan does not do

- No code change to the agent, no patch to old versions, no thinking-on repeats, no runs beyond `runs.json`.
- No look at pool outcomes before all rounds end, except the runner's logs (fees, exit codes, infra classes). The main
  session commits results after each round as usual; `r_repeats` starts only after round 3 (or a stop). (v_prereg:
  the per-run `out_round<N>/*.out` tails contain the agent's printed estimate; they are opened only to diagnose an
  infrastructure failure, and any such opening is logged in DEVIATIONS.md.)
- O1 (second archive) has its own pre-registration.

---

## Review changes (v_prereg)

Adversarial review on 2026-11-27 (about 22:00-23:00 UTC) by the unit `v_prereg`, before any run, leakage check or O2
lookup. Scripts and logs: `paper/prereg/verify/` (`v01_counts`, `v02_http_codes`, `v03_tree_commits`,
`v04_runner_tests`, `v05_plan_tokens_launchers`, `v06_commit_copies`, each with `_log.txt`); new dry runs
`verify/dryrun_round{1,2,3}_v_prereg.txt` and `verify/dryrun_leakcheck_v_prereg.txt` (identical to the earlier ones
apart from the clock lines). `runs.json` is unchanged. Every edit above is marked "v_prereg"; the list:

**Runner (`paper/_tools/run_repeats.py`)**
1. `classify_infra`: `api_rejected_400/404/422` only for a run without an estimate. Reason: a single rejected call in a
   run that still estimated would have been re-run, a re-run selected on a partial outcome.
2. New infra class `interrupted` (`interrupted()`): start logged, no end event, no `state.json`, older than 2 x the
   90-min timeout; re-runnable once with `--rerun-infra`, logged as `infra_interrupted`. Reason: a killed runner
   (reboot, power loss) left the run neither re-runnable nor classified, so the cell silently lost a repeat.
3. `pending_infra()` and a new `round_prereq` condition: round N+1 does not start while a round-N infra failure or
   interrupted run lacks its once-only re-run (or an abandoned cell). Reason: re-runs could otherwise be made after
   the next round, out of order and closer than 20 h to another repeat of the same cell.
4. `leak_decide`: a prompt-token difference no longer removes a question from the shift test; the decision records
   `n_prompt_tokens_differ` and `tokenizer_or_hosted_request_changed`. Reason: the request text is identical by
   construction, so a difference means a hosted-model change, and the old rule would have disabled the shift test in
   exactly the most leak-prone case (all 23 differ).
5. End events log `http_codes` and `plan_prompt_tokens` (`call_facts()`). Reason: the request-identity check (E0) and
   infra diagnosis without opening outputs.
   Offline tests of 1-5 on synthetic logs and answers: `verify/v04_runner_tests_log.txt` (all pass); `classify_infra`
   on the 233 archive dirs still gives exactly the 7 `*_402` runs.

**Plan (this file)**
6. B2: live-page range of the test4 archive runs 21-40, not 26-40 (`state.leakage`).
7. B3 caveats: the tree commit is the latest by committer date; v2.8r's tree also adds the test2 questions to
   `forecast.py` (`worktrees.json` note incomplete); commit identity checked by content against the other commits of
   the same author date and subject (comment lines only); the 5 v2.1*/v2.1b originals ran as 8 threads of one process
   with a shared fetch limiter (`probes/run_v2_backtests.py`), the repeats as single CLI processes. Sensitivity
   without those 5 cells added to E3/R2.
8. C3: the 3-lane concurrency is stated as a departure from TOPIC_DECISION O3 "one at a time", with the reason.
9. C5: the infra changes 1-3 in words; C7: recorded fees are the code's price-table estimate; C9: new log fields.
10. D2/D3: change 4 in words. D5: how a repeated check is made and that a transport/key/balance failure aborts the check
    rather than producing an invalid answer.
11. E0: request-identity check (plan prompt_tokens; mismatching pool-B cells leave E3/R2/F2); zero-spread floor for
    log variances (s^2 = 1e-6) with a sensitivity; label precedence ("nearly equal (p < 0.05)") and the
    "different, against the thesis" label; definition of "drift detected". Reason: undefined cases that would have
    been decided after seeing the data (ln 0, overlapping labels, reversed signs).
12. E1: cell inclusion (>= 2 estimates), denominator = runs with an estimate, why p0 stays 10.2% (vs runs.csv 12.2%),
    clustering caveat and question-level count.
13. E2: R2 given a primary statistic, test and label (it was listed as "with pre-set labels" but had none).
14. E3: both intervals must meet a label; rho over repeats with an estimate, no-estimate sensitivity.
15. E4: tie rule; searcher-call tokens and plan prompt_tokens among the process metrics; note that peak hours only set
    the price in the code, so `v217a_try` is the same configuration.
16. E6: the G that applies to V1 (<= 21) and K1/K2 (17).
17. E7: F2, M1, B1, S1 moved from "secondary confirmatory" to "secondary descriptive" (no test had been defined).
18. A: P2 ceiling caveat; which reading each pool-B direction cuts against; new item 6 for inconclusive and reversed
    primaries.
19. F3: strength rule for "supports C2" (Fisher exact vs 0/82; one false alarm alone is "weak, not significant");
    the past-only reading that could not fail is dropped. `o2_score.py` is unchanged (it prints the direction only).
20. F4: rules for the third lookup, approximate or bound statements, other time bases or aggregations, and
    earnings-call sources.
21. G4/G4b: partial statements on S and T are P; strata (a) same-configuration statistics vs (b) cross-version-only
    papers, because criterion G2 (ii) would otherwise let ablation-only papers dominate the gap count.
22. I: the `out_round` tails contain estimates; opening them is logged.

**Not changed, for the user to decide** (also in `verify/summary.json`): how to freeze (commit + tag vs hashes only);
the worktrees and junctions; 3 lanes vs one at a time; the second literature coder; the $30 stop (the conservative
high scenario, $29, leaves about $1 of headroom: the guard could then serialise the end of round 3 and hold back its
last one or two runs; the expected $18 leaves ample room).

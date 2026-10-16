# triangulate-agent

A backtest **probe** for a triangulation / estimation agent. The LLM only proposes structure; Python does every number.

- The model proposes three estimation paths per question (top-down, bottom-up, proxy). Each path is a formula over named inputs. Each input has a value, unit, 80% range (low/high) and provenance (`sourced` with a source and quote, or `assumption` with a rationale).
- Python parses the formulas with a whitelist evaluator (no `eval`), converts units with an explicit unit table, propagates uncertainty by Monte Carlo (lognormal inputs, fixed seed), aggregates paths by the median of path medians, reports an 80% interval, and flags paths more than one order of magnitude from the aggregate.
- Every question gets a world-model state JSON and a dependency graph (target, paths, inputs). Node colour shows status, input node size shows sensitivity.
- The probe compares this structured arm with a naive arm (the model gives one number) on 20 realFP Fermi questions. The pre-registered plan is in `PROBE_PLAN.md`; results, in Chinese, are in `PROBE.md`.

The probe (`select`, `run`, `demo`, `report`, `forecast`) uses the standard library only (Python 3.12+).
The research agent (`agent`, see `AGENT_MVP.md`) needs `langgraph` and `trafilatura`: create `.venv` with
`py -3.14 -m venv .venv` and `.venv/Scripts/python.exe -m pip install -r requirements.txt`.

## Commands

```
python -m triangulate select      # pick the 20 questions from data/raw (see DATA.md to download)
python -m triangulate run         # both arms on the 20 questions, then the report
python -m triangulate demo        # structured arm on the finance demo question, then the report
python -m triangulate report      # offline: rebuild states, graphs and tables from saved replies
python -m unittest                # tests: evaluator, Monte Carlo aggregation, graph sensitivity, units, agent code
.venv/Scripts/python.exe -m triangulate agent --ask "How many ... in ...?"        # research agent on any question (as_of = today)
.venv/Scripts/python.exe -m triangulate agent --ask "..." --as-of 2026-08-15      # same, standing on an earlier date (backtest mode)
.venv/Scripts/python.exe -m triangulate agent --auto-approve --tag post_review    # backtest on the two forecast questions
.venv/Scripts/python.exe -m triangulate agent --auto-approve --tag v2 --ablate-own-history  # ablation: no own history (tag v2_noown)
.venv/Scripts/python.exe -m triangulate agent-score [--tag post_review]           # offline: score saved backtest runs
.venv/Scripts/python.exe probes/recompute_saved_runs.py                           # offline: saved runs under the current compute code
.venv/Scripts/python.exe probes/recheck_continuous.py                             # offline: the 7 dev/test runs recompute to the saved estimates
.venv/Scripts/python.exe probes/plan_only.py <out_dir>                            # plan node only for the 7 dev/test questions (outcome_type check)
.venv/Scripts/python.exe probes/replay_judge_outcomes.py                          # offline: saved FOMC judge evidence through the v2.3 outcome-list checks
```

## Discrete targets (v2.2; outcome lists from the judge since v2.3)

Some targets can only take one of a few values (a policy rate after one meeting, an election winner, a yes/no event); an expected value such as 4.11% would be an impossible answer. The plan marks such a target `outcome_type: "discrete"` with an optional `outcome_kind` hint (for example "policy rate in fixed steps") and does not list outcomes. Since v2.3 the judge defines the outcome list in its first round, after the evidence is in: `outcomes` (2-6 mutually exclusive `{label, value}`; for numbers the lowest carries `le` and the highest `ge`, two merged tails that make the list exhaustive) and `outcomes_basis` (the kept point ids it relies on). Code checks the list (unique labels, 2-6, the two tails, whose labels must say "or lower" / "or higher" since v2.3.1, every basis id a kept point) and sends a failing list back in the repair round; later rounds reuse it, and the judge may revise it once with a reason (`state.json` -> `outcomes`). The judge then has one method, `outcome_probs`: each outcome's probability references a kept data point (market-implied or published probabilities preferred) or an assumption, one outcome may take the remainder, and an outcome with no input gets probability 0 (listed in the method's notes). Code converts percentages to fractions, checks each probability is in [0, 1], checks the sum (others <= 1.02 with a remainder; [0.9, 1.1] without, then normalised), pools several methods by an equal-weight linear average, and reports every outcome's probability and the most likely outcome (`central` = its value when numeric; no interval). The restated-point rule, the input audit (one row per probability input) and the judge repair round apply. Since v2.2.1: every method needs at least one kept data point; one id gives the probability of one outcome only; a data point used as a probability must be named as one (probability, odds, chance or likelihood in its name or unit), and percentage-point or basis-point changes are rejected; two methods whose distributions differ by a total variation distance above 0.5 go back to the judge; the input audit also checks the remainder outcome; a scored (backtest) question stays continuous unless it is marked `outcome_type: "discrete"`; scoring maps a true value beyond a merged tail ("X or lower") to that tail. Code: `triangulate/agent/discrete.py`.

Optional Jev arm (`triangulate/agent/jev.py`): when `TYPESAFE_KEY_FILE` names a file with a line `TYPESAFE_API_KEY=...`, code writes a plain evidence brief from the kept points and asks TypeSafe's Jev once (official endpoint `https://api.typesafe.ai/v1/systemone`, one choice question). Its distribution is stored as a separate arm (`state.json` → `jev`), shown beside the agent's in the ledger, `graph.html` and the web result page, and never pooled into the agent's answer. Without the variable the arm is recorded as `not_configured`. Jev tokens are logged with an estimated cost at the listed price ($0.042 per million input tokens, output free; docs.typesafe.ai/models, checked 2026-10-15).

Status (2026-10-15): five live runs of the FOMC question (`results/agent/ask_0e2d5021/discrete1`, `2`, `4`, `5`, `6`) found the right evidence (current upper bound 4.00%; CME FedWatch readings on pages dated 2026-10-14, which conflict: hold 56.3% and 25bp hike 43.7% from two sources, 25bp hike 53.7% from CNBC) but ended without an estimate. discrete5: the outcome list, fixed at planning time before any search, did not contain the current rate (hence v2.3). discrete6 (v2.3): the judge's first reply in each round left out the outcome list, and each repaired list cited basis ids that the round's first reply had discarded (the repair prompt did not say which ids were discarded), so code rejected both. v2.3.1 (offline fixes, no live run yet) names the discarded ids in the repair prompt, rewrites the method notes after an accepted revision, requires tail labels to say "or lower" / "or higher", and gives the Jev arm the tail meaning. Causes and open problems are in `NEXT.md`. The Jev arm has only been tested offline.

The DeepSeek key is read at run time from the file in `TRIANGULATE_KEY_FILE` (default `./.env`, git-ignored). The file must contain one line `DEEPSEEK_API_KEY=...`. The key is never printed or logged.

`run` and `demo` skip questions that already have saved replies. Use `--force` to call the model again (this costs money and changes results).

## Already-published targets (v2.4, live use only)

When the agent runs on today's date and the question has no registered official value, a kept data point may already be the target value (same entity, measure and period, published on or before as_of). Code proposes candidates (kept points whose period matches the target period, whose name contains one of the target's entity words and shares a stem with the target's measure, with the same % / non-% unit, that are not named as a forecast, probability or change, and, since v2.4.1, whose page date (for a snapshot, the capture date) and stated publication date are not before the end of the target period and whose quote does not call the number a forecast or expectation in the clause that holds it). The entity test is only a coarse filter: entity words are the capitalised names and acronyms in the target's description, without a leading measure name ("Real GDP of France" gives only "france") and without the publisher's name or acronym from outside the first clause ("as reported by SMMT"); other entities can still pass (for example when the measure is an acronym elsewhere in the description, or when no entity word is found, which the check notes as "no entity constraint"), and only the model check rejects them. One model call marks each candidate `target` or `different` and writes no numbers. If the confirmed values agree (within 0.5%), the result is that value, marked `published` with its source and date (`state.json` -> `published`; `compute.result.basis = "published"`); the estimation methods are still computed and listed for reference (`compute.estimate_result`) but not blended, and code writes the final answer. A discrete target whose published value falls in one of the judge's outcomes is reported as resolved. Confirmed values that disagree are reported as a conflict next to the estimate. Backtests never run the check (the target is published after as_of there); the 7 dev/test runs recompute identically and the continuous-path prompt hash is unchanged. Code: `triangulate/agent/published.py`.

Live check (2026-10-16, `results/agent/ask_a63174a0/published1`): "How many new cars were registered in the UK in September 2026, as reported by SMMT?" was reported as published, 350,536 (SMMT preliminary figure via fleetnews.co.uk and tradingeconomics.com; the estimation methods gave 352,638 for reference), $0.46, 27 minutes. An earlier snapshot of the same article said 350,518; which figure is SMMT's final one was not checked. Open problems are in `NEXT.md`.

## Web UI (local)

```
.venv/Scripts/python.exe -m triangulate serve               # http://127.0.0.1:8770/ (binds 127.0.0.1 only)
.venv/Scripts/python.exe -m triangulate serve --port 8771   # another port
```

Browsing saved runs works offline. Starting a run needs the key file (`TRIANGULATE_KEY_FILE`) and network; set the variable in the environment of the server process. Code: `triangulate/web/` (FastAPI, `static/` is plain HTML + JS, no build step).

| page | shows |
|---|---|
| 新问题 (`#/`) | form: question + optional as_of (empty = today, live use; earlier date = backtest mode). The run plans, then stops for approval. At most 2 unfinished runs per server. |
| run progress (`#/run/<id>`) | status (planning / awaiting_approval / running / done / failed / cancelled), elapsed time, dollars spent (tokens + assumed search fee), the pinned target, the proposed directions with checkboxes (unchecked ones are dropped through the existing resume-with-directions path), per-direction progress (searching / fetching n pages / extracting / done: k points kept), judge rounds, input audit and repair, compute, final; cancel button. Results go to `results/agent/<qid>/web_<UTC time>/`. Runs live in server memory; after a restart only the saved files remain. |
| 已保存的运行 (`#/saved`) | every `results/agent/**/state.json` (backtests, `--ask`, web runs) by question id and tag |
| result (`#/result?qid=&tag=`) | estimate and 80% interval (discrete runs: most likely outcome and an outcome-probability table with per-method and Jev columns); final answer; "证据 vs 假设" (assumption share, warning above 50%); methods (formula, each input with its role and the evidence it points to, estimate, weight, errors incl. input-audit exclusions and repair rounds); assumptions (value, judge range, range used after widening, rationale, applies_when, falsified_by, used by); kept / discarded evidence with source and Wayback snapshot links; leakage audit; links to `graph.html` and `ledger.md`. Official value and error only for backtest questions. |
| 回测 (`#/backtests`) | development set (Yellowstone Aug/Sep at v21b, JNTO and Korea at v21d) and held-out test (test1): official value, agent estimate, % error, interval, coverage, assumption share, and the naive / no-retrieval structured / last-year baselines |

Assumption share (read-only, computed from the saved state, never written back): for each `formula_mc` method, sigma_ln = ln(P90/P10) / (2 x 1.2816) per sampled input; share = sum of assumption sigma_ln^2 / sum over all sampled inputs; series methods count 0; overall = weight average over the methods that produced an estimate. It is an exact log-variance split only for pure products / ratios with each input used once; with sums, `mean()` or powers it is an approximation.

## Layout

| path | content |
|---|---|
| `triangulate/expr.py` | whitelist expression evaluator (scalar, vector, dimension inference) |
| `triangulate/units.py` | explicit unit table and unit-string parser |
| `triangulate/mc.py` | lognormal sampling, path distributions, aggregation |
| `triangulate/engine.py` | validates the model's structure and builds the world-model state |
| `triangulate/graph.py` | dependency graph and per-input sensitivity |
| `triangulate/arms.py`, `prompts.py`, `llm.py` | the two arms, prompts, DeepSeek client with per-call logging |
| `triangulate/report.py`, `viewer.py` | offline metrics, tables and HTML graph pages |
| `results/` | `summary.json`, `per_question.json`, `report_tables.md`, `calls.jsonl`, `demo/` |
| `triangulate/agent/` | research agent: LangGraph graph, searcher (URLs only), Wayback fetcher, extractor checks, judge, method library, assumption inputs for formula_mc (`assumptions.py`), own-history ablation (`ablation.py`), discrete targets (`discrete.py`), optional Jev arm (`jev.py`), already-published targets in live use (`published.py`) |
| `results/agent/<id>/[<tag>/]` | `state.json`, `calls.jsonl`, `ledger.md`, `graph.html` per run; raw pages stay in `data/raw/agent/` (local only) |
| `docs/graphs/` | `index.html`, the finance demo graph; realFP question pages under `realfp/` (local only) |

## Data and licence

realFP comes from allenai/fermi, which has no licence file. Question text and answers are therefore kept out of git (see `DATA.md`). Only question ids and metrics are committed.

## Viewing the graphs

Open `docs/graphs/index.html` in a browser. Pages load vis-network 9.1.9 from jsDelivr, so they need an internet connection. Click a node to see its details.

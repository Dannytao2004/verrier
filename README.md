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
```

## Discrete targets (v2.2)

Some targets can only take one of a few values (a policy rate after one meeting, an election winner, a yes/no event); an expected value such as 4.11% would be an impossible answer. The plan marks such a target `outcome_type: "discrete"` and lists 2-10 mutually exclusive outcomes `{label, value}` (invalid lists fall back to continuous, with a plan note). The judge then has one method, `outcome_probs`: each outcome's probability references a kept data point (market-implied or published probabilities preferred) or an assumption, one outcome may take the remainder, and an outcome with no input gets probability 0 (listed in the method's notes). Code converts percentages to fractions, checks each probability is in [0, 1], checks the sum (others <= 1.02 with a remainder; [0.9, 1.1] without, then normalised), pools several methods by an equal-weight linear average, and reports every outcome's probability and the most likely outcome (`central` = its value when numeric; no interval). The restated-point rule, the input audit (one row per probability input) and the judge repair round apply. Since v2.2.1: every method needs at least one kept data point; one id gives the probability of one outcome only; a data point used as a probability must be named as one (probability, odds, chance or likelihood in its name or unit), and percentage-point or basis-point changes are rejected; two methods whose distributions differ by a total variation distance above 0.5 go back to the judge; the input audit also checks the remainder outcome; a scored (backtest) question stays continuous unless it is marked `outcome_type: "discrete"`; scoring maps a true value beyond a merged tail ("X or lower") to that tail. Code: `triangulate/agent/discrete.py`.

Optional Jev arm (`triangulate/agent/jev.py`): when `TYPESAFE_KEY_FILE` names a file with a line `TYPESAFE_API_KEY=...`, code writes a plain evidence brief from the kept points and asks TypeSafe's Jev once (official endpoint `https://api.typesafe.ai/v1/systemone`, one choice question). Its distribution is stored as a separate arm (`state.json` → `jev`), shown beside the agent's in the ledger, `graph.html` and the web result page, and never pooled into the agent's answer. Without the variable the arm is recorded as `not_configured`. Jev tokens are logged with an estimated cost at the listed price ($0.042 per million input tokens, output free; docs.typesafe.ai/models, checked 2026-10-15).

Status (2026-10-15): four live runs of the FOMC question (`results/agent/ask_0e2d5021/discrete1`, `2`, `4`, `5`) found the right evidence (CME FedWatch on 2026-10-14: hold 56.3%, 25bp hike 43.7%) but ended without an estimate; the last one because the outcome list, fixed at planning time before any search, did not contain the current rate. Causes and open problems are in `NEXT.md`. The Jev arm has only been tested offline.

The DeepSeek key is read at run time from the file in `TRIANGULATE_KEY_FILE` (default `./.env`, git-ignored). The file must contain one line `DEEPSEEK_API_KEY=...`. The key is never printed or logged.

`run` and `demo` skip questions that already have saved replies. Use `--force` to call the model again (this costs money and changes results).

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
| `triangulate/agent/` | research agent: LangGraph graph, searcher (URLs only), Wayback fetcher, extractor checks, judge, method library, assumption inputs for formula_mc (`assumptions.py`), own-history ablation (`ablation.py`), discrete targets (`discrete.py`), optional Jev arm (`jev.py`) |
| `results/agent/<id>/[<tag>/]` | `state.json`, `calls.jsonl`, `ledger.md`, `graph.html` per run; raw pages stay in `data/raw/agent/` (local only) |
| `docs/graphs/` | `index.html`, the finance demo graph; realFP question pages under `realfp/` (local only) |

## Data and licence

realFP comes from allenai/fermi, which has no licence file. Question text and answers are therefore kept out of git (see `DATA.md`). Only question ids and metrics are committed.

## Viewing the graphs

Open `docs/graphs/index.html` in a browser. Pages load vis-network 9.1.9 from jsDelivr, so they need an internet connection. Click a node to see its details.

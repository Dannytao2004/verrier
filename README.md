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
.venv/Scripts/python.exe -m triangulate agent-score [--tag post_review]           # offline: score saved backtest runs
.venv/Scripts/python.exe probes/recompute_saved_runs.py                           # offline: saved runs under the current compute code
```

The DeepSeek key is read at run time from the file in `TRIANGULATE_KEY_FILE` (default `./.env`, git-ignored). The file must contain one line `DEEPSEEK_API_KEY=...`. The key is never printed or logged.

`run` and `demo` skip questions that already have saved replies. Use `--force` to call the model again (this costs money and changes results).

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
| `triangulate/agent/` | research agent: LangGraph graph, searcher (URLs only), Wayback fetcher, extractor checks, judge, method library |
| `results/agent/<id>/[<tag>/]` | `state.json`, `calls.jsonl`, `ledger.md`, `graph.html` per run; raw pages stay in `data/raw/agent/` (local only) |
| `docs/graphs/` | `index.html`, the finance demo graph; realFP question pages under `realfp/` (local only) |

## Data and licence

realFP comes from allenai/fermi, which has no licence file. Question text and answers are therefore kept out of git (see `DATA.md`). Only question ids and metrics are committed.

## Viewing the graphs

Open `docs/graphs/index.html` in a browser. Pages load vis-network 9.1.9 from jsDelivr, so they need an internet connection. Click a node to see its details.

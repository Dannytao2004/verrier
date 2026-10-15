# DATA

## Source

- Dataset: **realFP** from *How Much Coffee Was Consumed During EMNLP 2019? Fermi Problems: A New Reasoning Challenge for AI* (Kalyan, Kumar, Chandrasekaran, Sabharwal, Clark; arXiv:2110.14207, 2021).
- Official repository: <https://github.com/allenai/fermi> (linked from the paper; created 2021-11-04, last push 2021-11-10).
- Pinned commit used for download: `dfd4ceec41ef5fa0fe63e24c6027f13730d39a36`.

## Licence

- The official repository has **no licence file**: the GitHub API reports `license: null` and `GET /repos/allenai/fermi/license` returns 404 (checked 2026-10-15 UTC). The README asks users to cite the paper but grants no redistribution right.
- The arXiv paper itself is CC BY 4.0, but that licence covers the paper, not the dataset files.
- A third-party Hugging Face copy (`jeggers/fermi`) is tagged `cc-by-4.0`; that tag was set by the uploader, not by the authors, so it is not relied on here.
- **Decision:** treat the data as *not licensed for redistribution*. The raw files and every file that embeds question text or answer values are git-ignored (`data/raw/`, `data/backtest_realfp20.json`, `results/realfp/`, `docs/graphs/realfp/`). Only question ids (plus aggregate metrics) are committed. If the authors' permission is obtained later, these paths can be removed from `.gitignore`.

## Files downloaded (into `data/raw/realFP/`, not committed)

Downloaded 2026-10-15T03:40:50Z with `curl` from
`https://raw.githubusercontent.com/allenai/fermi/dfd4ceec41ef5fa0fe63e24c6027f13730d39a36/data/realFP/<split>_realfp.json`.
The `distractor_setting/` subfolder and the synthFP data were not downloaded.

| file | items | sha256 |
|---|---|---|
| `train_realfp.json` | 185 | `7286f67b9fb1f02b3c95b0be9987e8e1155e45ad88d1c7117308becdb436dc18` |
| `val_realfp.json` | 125 | `620ff2b64373e188e4e3fae952c69543762a9ce0dcd3b3322d7cfc2998d3391a` |
| `test_realfp.json` | 557 | `aefa45fe9c035d6a19aba46e2a895e0206c10e0fb38b2d5fe0718d740a9032d1` |

Each item has `question`, `program`, `answer`, `context`. There is no id field, so this repo uses `"<split>:<index>"` (0-based list index).

To rebuild locally:

```
mkdir -p data/raw/realFP
for f in train val test; do curl -sSfL -o data/raw/realFP/${f}_realfp.json "https://raw.githubusercontent.com/allenai/fermi/dfd4ceec41ef5fa0fe63e24c6027f13730d39a36/data/realFP/${f}_realfp.json"; done
python -m triangulate select
```

## Backtest selection

- Split: `test` (557 items). Only the `question` and `answer` fields are used; `program` and `context` (the annotated solution) are never shown to the model.
- Eligible: answer parses as a positive number with an optional unit (a leading `$` means USD) **and** the unit parses strictly with the explicit unit table in `triangulate/units.py`. 547 eligible, 10 rejected (temperature, angle, decibel, molar `M`, and two `$ per unit` answers). The rejected ids and reasons are listed in `data/backtest_realfp20_ids.json`.
- Selection: `random.Random(2021).sample(eligible sorted by index, 20)`.
- Committed: `data/backtest_realfp20_ids.json` (ids, selection metadata, rejected ids). Local only: `data/backtest_realfp20.json` (question, answer value, unit).
- Results committed per question (`results/per_question.json`, `results/report_tables.md`, `PROBE.md`): id, target unit, estimates and signed log10 errors. Answer values can be derived from these numbers; question text is never committed. Per-question states and graph pages that show the question text live in the git-ignored `results/realfp/` and `docs/graphs/realfp/`.

Caveat: realFP answers are the annotators' own Fermi estimates, not measured ground truth. Some are odd (one selected item's answer is about 6e-18 km). The probe scores against them as given.

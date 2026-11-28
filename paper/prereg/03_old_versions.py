"""Pre-registration facts (read-only git show): for each code commit that pool B would re-run, how the CLI is invoked,
where results are written, how the key file / model / prices / peak window / run cap / assumed search fee are set,
and whether the question bank at the tree commit contains the question with the archive run's as_of.
No model call, no worktree, nothing written outside paper/prereg/."""
import re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def show(rev, path):
    p = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return p.stdout if p.returncode == 0 else None
CELLS = [  # (label, code commit, tree commit = latest commit before the archive run started, qid, as_of)
    ("v2.1*", "2bbe8ae", "2bbe8ae", ["fc_jnto_2026_08", "fc_kr_births_2026_07", "fc_yell_2026_09"]),
    ("v2.1b", "66e70a8", "66e70a8", ["fc_jnto_2026_08"]),
    ("v2.1c-pre (base f5fe773)", "f5fe773", "f5fe773", ["fc_kr_births_2026_07"]),
    ("v2.8r", "c64d3a3", "48e6b45", ["fc_de_cars_2026_09"]),
    ("v2.11f", "8e3b64e", "8e3b64e", ["fc_de_cars_2026_09", "fc_lhr_pax_2026_09", "fc_jp_movers_2026_08"]),
    ("v2.11g", "1ff32f6", "1ff32f6", ["fc_de_cars_2026_09"]),
    ("v2.12a", "cf3413e", "cf3413e", ["fc_us_retail_2026_06"]),
    ("v2.12a (cn_profits tree)", "cf3413e", "f5099a4", ["fc_cn_profits_2026_09"]),
    ("v2.16e", "b77e098", "31e0021", ["fc_de_cars_2026_09"]),
    ("v2.17a", "2c69959", "HEAD", []),
]
AGENT_CODE = ["triangulate/agent", "triangulate/llm.py", "triangulate/config.py", "triangulate/expr.py", "triangulate/mc.py",
              "triangulate/prompts.py", "triangulate/providers.py"]
def grep(text, pat, n=3):
    if text is None:
        return ["<file missing>"]
    out = [l.strip()[:170] for l in text.splitlines() if re.search(pat, l)]
    return out[:n] if out else ["<no match>"]
for label, code, tree, qids in CELLS:
    print("=" * 100)
    print(label, "code", code, "tree", tree)
    d = subprocess.run(["git", "diff", "--stat", code, tree, "--", *AGENT_CODE], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    print("  agent-code diff code..tree:", d or "<none>")
    m = show(tree, "triangulate/__main__.py")
    for pat in [r'"--question"', r'"--tag"', r'"--auto-approve"', r'"--ablate-own-history"', r'"--ask"', r'"--as-of"', r'"--id"']:
        print("  CLI", pat, "->", grep(m, re.escape(pat), 1)[0])
    r = show(tree, "triangulate/agent/run.py")
    print("  run.py RES:", grep(r, r"^RES\s*=|RES = ", 1)[0])
    print("  run.py out_dir:", grep(r, r"out_dir = ", 2))
    print("  run.py ablation_tag:", grep(r, r"def ablation_tag|_noown", 3))
    print("  run.py calls rename:", grep(r, r"calls.before_", 1)[0])
    print("  run.py summary file:", grep(r, r"summary_\{tag\}|summary.json", 1)[0])
    c = show(tree, "triangulate/config.py")
    print("  config KEY_FILE:", grep(c, r"KEY_FILE\s*=", 1)[0])
    print("  config MODEL:", grep(c, r"^MODEL\s*=", 1)[0])
    print("  config API_URL:", grep(c, r"API_URL\s*=", 1)[0])
    print("  config deepseek-flash price:", grep(c, r'"deepseek-flash"', 2))
    print("  config is_peak body:", grep(c, r"weekday\(\) < 5", 1)[0])
    print("  config THINKING env:", grep(c, r"TRIANGULATE_THINKING", 1)[0])
    print("  config CONCURRENCY:", grep(c, r"MAX_CONCURRENCY", 1)[0])
    p = show(tree, "triangulate/agent/pipeline.py")
    print("  pipeline RUN_USD_CAP:", grep(p, r"RUN_USD_CAP\s*=|USD_CAP|usd_cap|max_usd", 4))
    print("  pipeline search fee:", grep(p, r"SEARCH_FEE|search_fee|0\.01", 4))
    s = show(tree, "triangulate/agent/search.py")
    print("  search.py endpoint:", grep(s, r"anthropic|api\.deepseek|web_search", 3))
    f = show(tree, "triangulate/forecast.py")
    for q in qids:
        hit = grep(f, r'"id": "%s"' % q, 1)[0]
        print("  forecast", q, "->", hit[:170])
    fe = show(tree, "triangulate/agent/fetch.py")
    print("  fetch.py cache:", grep(fe, r"_cache|CACHE\s*=", 2))

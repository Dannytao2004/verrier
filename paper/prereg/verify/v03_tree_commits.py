"""v_prereg check 2: for each pool-B cell, is runs.json tree_commit the latest commit (on main's first-parent history)
before the archive run started, by author date and by committer date? Is the agent code byte-identical between
tree_commit and code_commit? Do all commits exist? Read-only git."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("D:/triangulate-agent")


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, encoding="utf-8").stdout.strip()


runs = json.load(open(ROOT / "paper/prereg/runs.json", encoding="utf-8"))
log = [l.split("|", 3) for l in git("log", "--first-parent", "main", "--format=%H|%aI|%cI|%s").splitlines()]
cells = {}
for o in runs:
    if o["pool"] == "B":
        cells.setdefault(o["reference_run"], o)
AGENT = ["triangulate/agent", "triangulate/llm.py", "triangulate/config.py", "triangulate/expr.py", "triangulate/mc.py",
         "triangulate/prompts.py", "triangulate/providers.py", "triangulate/__main__.py", "triangulate/forecast.py",
         "triangulate/units.py", "triangulate/arms.py"]
for ref, o in sorted(cells.items()):
    st = json.loads((ROOT / "results/agent" / ref / "state.json").read_text(encoding="utf-8"))
    t0 = datetime.strptime(st["started_at"], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
    before_a = next((h for h, a, c, s in log if datetime.fromisoformat(a) <= t0), None)
    before_c = next((h for h, a, c, s in log if datetime.fromisoformat(c) <= t0), None)
    exists = git("cat-file", "-t", o["tree_commit"]) == "commit" and git("cat-file", "-t", o["code_commit"]) == "commit"
    paths = [p for p in AGENT if git("ls-tree", o["tree_commit"], p)]
    diff = git("diff", "--stat", o["code_commit"], o["tree_commit"], "--", *paths)
    on_main = git("merge-base", "--is-ancestor", o["tree_commit"], "main") == "" and \
        subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", o["tree_commit"], "main"]).returncode == 0
    print(f"{ref:36s} start={t0.isoformat()} tree={o['tree_commit'][:7]} code={o['code_commit'][:7]} exists={exists} "
          f"on_main={on_main} latest_before(author)={before_a[:7] if before_a else None} "
          f"latest_before(committer)={before_c[:7] if before_c else None} "
          f"match_author={before_a == o['tree_commit']} match_committer={before_c == o['tree_commit']}")
    print(f"    agent-code diff code..tree (incl. __main__, forecast, units, arms): {diff or '<none>'}")
# HEAD vs v2.17a, full triangulate/
print("HEAD:triangulate", git("rev-parse", "HEAD:triangulate"), " v2.17a:triangulate", git("rev-parse", "v2.17a^{commit}:triangulate"))
print("diff v2.17a HEAD -- triangulate:", git("diff", "--stat", "v2.17a", "HEAD", "--", "triangulate"))
print("diff v2.17a HEAD -- triangulate, non-comment changed lines:")
for line in git("diff", "-U0", "v2.17a", "HEAD", "--", "triangulate").splitlines():
    if line[:1] in "+-" and not line.startswith(("+++", "---")):
        body = line[1:].strip()
        print("   ", "COMMENT" if body.startswith("#") else "CODE", line[:110])

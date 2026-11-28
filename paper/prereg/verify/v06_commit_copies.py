"""v_prereg: commit identity checked by content. For every code / tree commit used by the batch, find the other commits
in the local object store with the same author date and subject (`git log --all --reflog`) and diff their triangulate/
trees against the batch commit; changed lines are classified as comment-only or code. Read-only git."""
import json
import subprocess
from pathlib import Path

ROOT = Path("D:/triangulate-agent")


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, encoding="utf-8",
                          errors="replace").stdout


runs = json.load(open(ROOT / "paper/prereg/runs.json", encoding="utf-8"))
commits = sorted({o["tree_commit"] for o in runs if o["tree_commit"] != "HEAD"} | {o["code_commit"] for o in runs})
allc = {}
for line in git("log", "--all", "--reflog", "--format=%H|%aI|%s").splitlines():
    h, a, s = line.split("|", 2)
    allc.setdefault((a, s), set()).add(h)
ok_all, n_copies = True, 0
for c in commits:
    a, s = git("log", "-1", "--format=%aI|%s", c).strip().split("|", 1)
    copies = sorted(allc.get((a, s), set()) - {c})
    n_copies += len(copies)
    print(f"== {c[:10]} {a} {s[:70]}")
    if not copies:
        print("   no other commit with this author date and subject")
    for t in copies:
        tt, tc = git("rev-parse", f"{t}:triangulate").strip(), git("rev-parse", f"{c}:triangulate").strip()
        if tt == tc:
            print(f"   copy {t[:10]}: triangulate/ tree identical")
            continue
        diff = git("diff", "-U0", t, c, "--", "triangulate")
        changed = [l for l in diff.splitlines() if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        code = [l for l in changed if l[1:].strip() and not l[1:].strip().startswith("#")]
        files = sorted({l[6:] for l in diff.splitlines() if l.startswith("+++ b/")})
        print(f"   copy {t[:10]}: triangulate/ differs in {files}: {len(changed)} changed lines, {len(code)} non-comment")
        ok_all &= not code
print(f"[1] {len(commits)} batch commits, {n_copies} other copies; every copy has the same triangulate/ code "
      f"(differences in comment lines only): {ok_all}")

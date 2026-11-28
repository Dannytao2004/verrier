"""Pre-registration check (read-only git show): are the naive arm's system prompt, user template, unit_display and
_messages identical at HEAD and at every commit that was current when the archive's thinking-off naive answers were made?
Extracts the source text of those symbols with ast from each revision. No model call."""
import ast, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def show(rev, path):
    p = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return p.stdout if p.returncode == 0 else None
def symbols(src, names):
    t = ast.parse(src); out = {}
    for node in t.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and getattr(node.targets[0], "id", None) in names:
            out[node.targets[0].id] = ast.get_source_segment(src, node)
        if isinstance(node, ast.FunctionDef) and node.name in names:
            out[node.name] = ast.get_source_segment(src, node)
    return out
def at(ts):
    return subprocess.run(["git", "log", "-1", "--format=%h", f"--before={ts}"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
TIMES = ["2026-10-15T05:51:38+00:00", "2026-10-15T09:23:35+00:00", "2026-10-15T18:35:03+00:00", "2026-10-16T09:05:17+00:00",
         "2026-10-19T08:47:53+00:00", "2026-10-23T23:14:27+00:00", "2026-10-24T05:00:01+00:00"]
head_p = symbols(show("HEAD", "triangulate/prompts.py"), {"NAIVE_SYSTEM", "USER", "unit_display"})
head_a = symbols(show("HEAD", "triangulate/arms.py"), {"_messages"})
head_c = [l for l in show("HEAD", "triangulate/config.py").splitlines() if '"naive":' in l]
print("HEAD config naive max_tokens line:", head_c)
for ts in TIMES:
    rev = at(ts)
    p = symbols(show(rev, "triangulate/prompts.py"), {"NAIVE_SYSTEM", "USER", "unit_display"})
    a = symbols(show(rev, "triangulate/arms.py"), {"_messages"})
    cfg = show(rev, "triangulate/config.py") or ""
    mt = [l for l in cfg.splitlines() if '"naive":' in l]
    same = {k: p.get(k) == head_p.get(k) for k in head_p} | {k: a.get(k) == head_a.get(k) for k in head_a}
    print(ts, "commit", rev, "identical to HEAD:", same, "| naive max_tokens line:", [x.strip()[:60] for x in mt] or "<none>")

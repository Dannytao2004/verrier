"""Pre-registration facts for pool B (read-only): per catastrophic run, the code commit, the latest commit of any kind
before the run started (the tree the run most likely saw), the state's question/as_of/leakage keys and settings.
No outcome of the planned analyses is computed. Reads runs.csv, state.json files and read-only git."""
import csv, json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
cat = [r for r in rows if r["scored"] == "True" and r["catastrophic"] == "True"]
def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.strip()
for r in sorted(cat, key=lambda r: r["started_at"]):
    st = json.loads((ROOT / "results/agent" / r["run_id"] / "state.json").read_text(encoding="utf-8"))
    tree = git("log", "-1", "--format=%h %cI %s", f"--before={r['started_at']}", "--all")
    tree_main = git("log", "-1", "--format=%h %cI %s", f"--before={r['started_at']}")
    print("==", r["run_id"])
    print("   code_version", r["code_version"], "code_commit", r["code_commit"], "confidence:", r["version_confidence"])
    print("   evidence:", r["version_evidence"][:300])
    print("   started", r["started_at"], "| latest commit before start (HEAD history):", tree_main[:140])
    print("   state keys:", sorted(st.keys()))
    print("   qid", st.get("qid"), "as_of", st.get("as_of"), "tag", st.get("tag"), "model", st.get("model"))
    print("   question:", (st.get("question") or "")[:160].replace("\n", " "))
    lk = st.get("leakage") or {}
    print("   leakage keys:", sorted(lk.keys()))
    print("   settings keys:", sorted((st.get("settings") or {}).keys()))
    print("   ablation:", json.dumps(st.get("ablation"))[:120] if st.get("ablation") else None)

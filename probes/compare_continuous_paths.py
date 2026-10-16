"""离线复核：连续目标在两份代码下的 compute.run / 假设校验 / _problems / 输入核对的行和表头是否逐字节相同。
对 results/ 下每个连续目标的 state.json、每一轮裁判的方法（全部方法、去掉输入核对没过的两种）算一个 sha256。
不调模型、不联网。旧代码先导出到 gitignore 的目录：
  git archive <tag> triangulate | tar -x -C probes/out/_old
用法：.venv/Scripts/python.exe probes/compare_continuous_paths.py <代码根目录> > 输出.json，两份代码各跑一次再比。
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])
from triangulate.agent import graph as G  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main():
    out = {}
    for p in sorted(ROOT.glob("results/**/state.json")):
        st = json.loads(p.read_text(encoding="utf-8"))
        target = (st.get("plan") or {}).get("target") or {}
        if not target or target.get("outcome_type") == "discrete":
            continue
        pts = st.get("points") or []
        by_id = {q["id"]: q for q in pts}
        new_sig = "target" in G.audit_rows.__code__.co_varnames
        for jr in st.get("judge_rounds") or []:
            for variant in ("all", "no_audit_failed"):
                bad = (jr.get("audit_failed") or {}) if variant == "no_audit_failed" else {}
                ms = [m for i, m in enumerate(jr.get("methods") or []) if str(i) not in bad]
                if not ms:
                    continue
                jj = dict(jr, methods=ms)
                o, av, failed = G._code_check(jj, pts, target)
                kept_a = {a["id"]: a for a in av["kept"]}
                rows = [G.audit_rows(mi, mo, by_id, kept_a, target) if new_sig else G.audit_rows(mi, mo, by_id, kept_a)
                        for mi, mo in zip(ms, o["methods"])]
                hdr = [G._audit_header(mi, mo) for mi, mo in zip(ms, o["methods"])]
                blob = json.dumps([o, av, failed, G._problems(jj, o, av, failed), rows, hdr], sort_keys=True, default=str)
                out[f"{p.relative_to(ROOT).as_posix()}|r{jr.get('round')}|{variant}"] = hashlib.sha256(blob.encode()).hexdigest()
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()

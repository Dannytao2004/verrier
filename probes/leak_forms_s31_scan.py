"""v2.12c（S31）离线检查：新写法表（billion / trillion / 亿 / 万亿 / 兆 / 조）会让哪些页面多被哨兵作废。不调模型、不联网、只读。

1. 已存运行取过的页面（data/raw/agent/<qid>/*.txt，取页时哨兵扫的就是这份全文）：对每道有 leak_values 的题，
   HEAD 的 evidence.py（git show 导出到 probes/out/_s31_old/）和当前代码各扫一遍，列出「现在命中、以前不命中」的页和写法。
2. 另给的 as_of 之前的页面（test3 复查时下载的官方页，参数 <qid>=<路径>，HTML 去标签后扫）：同样两份代码各扫一遍。
当前代码按 run.prepare 的口径带上目标真值（answer_value；v2.12d 起两位有效数字的大数写法只给它登记）。
用法：.venv/Scripts/python.exe probes/leak_forms_s31_scan.py [<qid>=<页面路径> ...]
输出：stdout 和 probes/out/s31_scan.txt。
"""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as NEW  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402

OUT = ROOT / "probes" / "out"


def old_module():
    d = OUT / "_s31_old"
    d.mkdir(parents=True, exist_ok=True)
    src = subprocess.run(["git", "show", "HEAD:triangulate/agent/evidence.py"], cwd=ROOT, capture_output=True,
                         check=True).stdout
    p = d / "evidence_head.py"
    p.write_bytes(src)
    spec = importlib.util.spec_from_file_location("evidence_head", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def html_text(raw: bytes, name: str) -> str:
    s = raw.decode("utf-8", errors="replace")
    if name.endswith((".html", ".htm")):
        s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
        s = re.sub(r"<[^>]+>", " ", s)
    return s


def compare(old, text: str, vals, answer=None) -> tuple:
    """answer：目标真值（v2.12d：两位有效数字的大数写法只给它登记，和 run.prepare 交给哨兵的一样）。"""
    a = set(old.leak_scan(text, old.leak_patterns(vals)))
    b = set(NEW.leak_scan(text, NEW.leak_patterns(vals, answer=answer)))
    return sorted(a), sorted(b - a), sorted(a - b)


def main(argv):
    old = old_module()
    lines = []
    by_id = {q["id"]: q for q in QUESTIONS}
    n_pages = n_new = 0
    lines.append("## 1. stored pages (data/raw/agent), questions with leak_values")
    for q in QUESTIONS:
        vals = q.get("leak_values")
        d = ROOT / "data" / "raw" / "agent" / q["id"]
        if not vals or not d.is_dir():
            continue
        files = sorted(d.glob("*.txt"))
        newly, lost = [], []
        for f in files:
            _, add, gone = compare(old, f.read_text(encoding="utf-8", errors="replace"), vals, q.get("answer_value"))
            if add:
                newly.append((f.name, add))
            if gone:
                lost.append((f.name, gone))
        n_pages += len(files)
        n_new += len(newly)
        lines.append(f"{q['id']}: {len(files)} pages; newly hit {len(newly)}; no longer hit {len(lost)}")
        for name, add in newly:
            lines.append(f"  + {name}: {', '.join(add)}")
        for name, gone in lost:
            lines.append(f"  - {name}: {', '.join(gone)}")
    lines.append(f"total: {n_pages} pages, {n_new} newly hit")
    lines.append("")
    lines.append("## 2. given pre-as_of pages")
    for arg in argv:
        qid, _, path = arg.partition("=")
        q = by_id.get(qid)
        if q is None:
            lines.append(f"{arg}: unknown question id")
            continue
        p = Path(path)
        text = html_text(p.read_bytes(), p.name)
        before, add, gone = compare(old, text, q["leak_values"], q.get("answer_value"))
        lines.append(f"{qid} {p.name}: HEAD hits {before or 'none'}; new hits {add or 'none'}; no longer hit {gone or 'none'}")
    out = "\n".join(lines)
    print(out)
    (OUT / "s31_scan.txt").write_text(out + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1:])

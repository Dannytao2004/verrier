"""探针：Wayback CDX 前缀查询（matchType=prefix）的真实返回：行数、耗时、collapse=urlkey 保留哪次抓取、limit 怎么截。
用 triangulate.agent.net.get（同一个 UA、robots、限速）。只打印结构和样例，不存原件。"""
import json
import sys
import time
import urllib.parse

sys.path.insert(0, ".")
from triangulate.agent import net  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CDX = "https://web.archive.org/cdx/search/cdx"


def q(prefix, frm, to, limit, collapse=True):
    p = {"url": prefix, "matchType": "prefix", "from": frm, "to": to, "output": "json", "limit": str(limit),
         "fl": "timestamp,original,mimetype,statuscode", "filter": ["statuscode:200", "mimetype:text/html"]}
    if collapse:
        p["collapse"] = "urlkey"
    t0 = time.time()
    st, body, _, _ = net.get(f"{CDX}?{urllib.parse.urlencode(p, doseq=True)}", timeout=120)
    rows = json.loads(body) if st == 200 and body.strip() else []
    print(f"{prefix} {frm}-{to} limit={limit} collapse={collapse}: http {st}, {max(len(rows) - 1, 0)} rows, {time.time() - t0:.1f}s")
    for r in rows[1:4] + rows[-3:]:
        print("   ", r)
    return rows


for args in [("www.nps.gov/yell/learn/news/", "20250801", "20260815", 500),
             ("buckrail.com/", "20260601", "20260815", 500),
             ("www.ypradio.org/regional-news/", "20260501", "20260815", 300),
             ("dailymontanan.com/2026/", "20260501", "20260815", 300)]:
    try:
        rows = q(*args)
        ts = sorted(r[0] for r in rows[1:])
        if ts:
            print("    earliest/latest kept ts:", ts[0], ts[-1])
    except Exception as e:  # noqa: BLE001
        print(args[0], "error", type(e).__name__, e)

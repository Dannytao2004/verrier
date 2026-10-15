"""探针：Wayback CDX（as_of 之前最新快照）、id_ 原始抓取、robots.txt、Polymarket Gamma 搜索的真实返回长什么样。
只打印结构和长度；原件存 probes/out/（不进 git）。"""
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.robotparser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
UA = "triangulate-agent/0.1 (research prototype)"
OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)


def get(url, timeout=60):
    t0 = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(), dict(r.headers), round(time.time() - t0, 1)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers), round(time.time() - t0, 1)


for host in ("web.archive.org", "gamma-api.polymarket.com", "clob.polymarket.com", "www.nps.gov"):
    rp = urllib.robotparser.RobotFileParser(f"https://{host}/robots.txt")
    try:
        rp.read()
        print(host, "robots ok; cdx allowed:", rp.can_fetch(UA, f"https://{host}/cdx/search/cdx?url=x"),
              "| web allowed:", rp.can_fetch(UA, f"https://{host}/web/2025id_/x"), "| /public-search:", rp.can_fetch(UA, f"https://{host}/public-search?q=x"))
    except Exception as e:
        print(host, "robots error", type(e).__name__, e)
    time.sleep(1)

target = "https://www.nps.gov/yell/learn/news/25019.htm"
q = urllib.parse.urlencode({"url": target, "to": "20260815", "output": "json", "limit": "-3",
                            "filter": "statuscode:200", "fl": "timestamp,original,statuscode,mimetype"})
st, body, h, dt = get("https://web.archive.org/cdx/search/cdx?" + q)
print("CDX", st, dt, "s", body[:400])
time.sleep(1)
rows = json.loads(body) if st == 200 and body.strip() else []
if len(rows) > 1:
    ts, orig = rows[-1][0], rows[-1][1]
    st, raw, h, dt = get(f"https://web.archive.org/web/{ts}id_/{orig}")
    print("SNAP", st, dt, "s", len(raw), "bytes", h.get("Content-Type"))
    (OUT / "snap_probe.html").write_bytes(raw)
    import trafilatura
    txt = trafilatura.extract(raw.decode("utf-8", "replace"), include_tables=True) or ""
    print("TEXT len", len(txt)); print(txt[:600])
    md = trafilatura.extract_metadata(raw.decode("utf-8", "replace"))
    print("META date", md.date if md else None)
time.sleep(1)
for path in ("/public-search?" + urllib.parse.urlencode({"q": "national park visitors", "limit_per_type": 5}),
             "/markets?" + urllib.parse.urlencode({"limit": 3, "closed": "false"})):
    st, body, h, dt = get("https://gamma-api.polymarket.com" + path)
    print("GAMMA", path[:40], st, dt, "s", len(body))
    try:
        d = json.loads(body)
        if isinstance(d, dict):
            print("  keys", sorted(d)[:12])
            ev = d.get("events") or []
            for e in ev[:3]:
                print("  event:", e.get("title"), "| created", e.get("createdAt"), "| markets", len(e.get("markets") or []))
                if e.get("markets"):
                    m = e["markets"][0]; print("   market keys", sorted(m)[:60])
        else:
            print("  list", len(d), sorted(d[0])[:60] if d else None)
    except Exception as ex:
        print("  not json", ex, body[:200])
    time.sleep(1)

"""回测时的选页（审查发现：SEARCHER 看得到 as_of 之后的网页，两次 8 月运行的查询词里直接写着真值，它挑的 URL 是
「以答案为条件」选出来的）。

改成两步：
1. SEARCHER 照常搜索，但它给的 URL 只用来决定「去哪些站点、哪些目录找」：代码把每个 URL 变成目录前缀
   （带日期的路径换成 as_of 所在月和前两个月），用 Wayback CDX 前缀查询列出这些目录在 as_of 当天或之前存过的页面。
2. PICKER（一个看不到任何搜索结果、也不知道 SEARCHER 挑了哪几页的模型调用）只看「URL + 第一次存档日期」列表，
   挑出最可能有所需数据的几页。PICKER 失败时按存档日期取最新的几页（同样不看搜索结果）。
残余：选哪些站点和目录仍受 SEARCHER 的事后知识影响；具体读哪几页不受。
真实使用（as_of = 今天）不需要这一步，直接用 SEARCHER 的 URL。
"""
import json
import re
import threading
import urllib.parse
from datetime import date, timedelta

from . import net
from .fetch import CACHE, CDX, _key
from .prompts import PICK_SYSTEM, PICK_USER

MONTHS_BACK = 3               # 带日期的目录：as_of 所在月和前两个月
DIR_WINDOW_DAYS = 400         # 普通目录：只列 as_of 之前 400 天内存过的页面
ROOT_WINDOW_DAYS = 90         # 站点根目录（新闻站常见）：页面太多，只看 90 天
LIST_LIMIT = 1500             # 每个前缀最多列这么多个 URL（CDX 按 URL 字母序截断）
MAX_QUERIES_PER_DIRECTION = 5
MAX_CANDIDATES_TO_PICKER = 150
_JUNK = re.compile(r"/(?:tag|tags|category|categories|author|authors|page|feed|wp-json|wp-content|search|login|cart|account|"
                   r"share|print|amp)(?:/|$)|\.(?:css|js|json|xml|rss|jpe?g|png|gif|svg|ico|woff2?|ttf)$|robots\.txt$|sitemap|"
                   r"wp-login|wp-admin|xmlrpc",
                   re.I)
_DROP_PARAMS = re.compile(r"^(?:utm_.*|_amp|amp|fbclid|gclid|ref|share|output)$", re.I)
_LOCKS, _LOCKS_GUARD = {}, threading.Lock()


def _months_back(as_of: date, n: int) -> list:
    y, m, out = as_of.year, as_of.month, []
    for _ in range(n):
        out.append((y, m))
        y, m = (y, m - 1) if m > 1 else (y - 1, 12)
    return out


def url_prefixes(url: str, as_of: date) -> list:
    """一个 URL -> [(CDX 前缀, from 日期)]。纯函数。
    /2026/06/10/slug -> 同一位置的 as_of 所在月和前两个月（.../2026/08/、.../2026/07/、.../2026/06/）；
    /2026-06-10/slug -> .../2026-08、.../2026-07、.../2026-06；其余 -> 页面所在目录；目录为空 -> 站点根。"""
    p = urllib.parse.urlsplit(url)
    host = p.netloc.lower()
    if not host or p.scheme not in ("http", "https"):
        return []
    segs = [s for s in p.path.split("/") if s]
    months = _months_back(as_of, MONTHS_BACK)
    for i, s in enumerate(segs):
        base = "/".join(segs[:i])
        base = f"{base}/" if base else ""
        if re.fullmatch(r"(?:19|20)\d{2}", s) and i + 1 < len(segs) and re.fullmatch(r"0[1-9]|1[0-2]", segs[i + 1]):
            return [(f"{host}/{base}{y:04d}/{m:02d}/", date(y, m, 1)) for y, m in months]
        if re.fullmatch(r"(?:19|20)\d{2}-(?:0[1-9]|1[0-2])(?:-\d{2})?", s):
            return [(f"{host}/{base}{y:04d}-{m:02d}", date(y, m, 1)) for y, m in months]
    parent = segs[:-1]
    if not parent:
        return [(f"{host}/", as_of - timedelta(days=ROOT_WINDOW_DAYS))]
    return [(f"{host}/{'/'.join(parent)}/", as_of - timedelta(days=DIR_WINDOW_DAYS))]


def _canon(url: str) -> str:
    p = urllib.parse.urlsplit(url)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True) if not _DROP_PARAMS.match(k)]
    return urllib.parse.urlunsplit((p.scheme, p.netloc.lower(), p.path, urllib.parse.urlencode(q), ""))


def list_prefix(prefix: str, frm: date, as_of: date) -> list:
    """CDX 前缀查询：[(第一次存档时间戳, URL)]，只有 200、text/html、时间戳在 [frm, as_of] 里的。按 key 缓存。"""
    ck = CACHE / "cdx_prefix" / f"{_key(prefix + '|' + frm.isoformat() + '|' + as_of.isoformat())}.json"
    with _LOCKS_GUARD:
        lock = _LOCKS.setdefault(ck.name, threading.Lock())
    with lock:  # 同一个前缀被几个方向同时要时只查一次
        if ck.exists():
            rows = json.loads(ck.read_text(encoding="utf-8"))
        else:
            q = urllib.parse.urlencode({"url": prefix, "matchType": "prefix", "from": frm.strftime("%Y%m%d"),
                                        "to": as_of.strftime("%Y%m%d"), "output": "json", "limit": str(LIST_LIMIT),
                                        "fl": "timestamp,original", "filter": ["statuscode:200", "mimetype:text/html"],
                                        "collapse": "urlkey"}, doseq=True)
            status, body, _, _ = net.get(f"{CDX}?{q}", timeout=120)
            if status != 200:
                raise RuntimeError(f"cdx prefix http {status}")
            rows = json.loads(body) if body.strip() else []
            ck.parent.mkdir(parents=True, exist_ok=True)
            ck.write_text(json.dumps(rows), encoding="utf-8")
    lim = as_of.strftime("%Y%m%d") + "235959"
    return [(r[0], r[1]) for r in rows[1:] if len(r) >= 2 and len(r[0]) == 14 and r[0] <= lim]


def build_candidates(search_urls: list, as_of: date) -> dict:
    """SEARCHER 的 URL（它挑的在前，搜索结果在后）-> 前缀 -> 存档列表 -> 候选（按第一次存档时间从新到旧，
    几个前缀轮流取，最多 MAX_CANDIDATES_TO_PICKER 个）。"""
    prefixes, seen = [], set()
    for u in search_urls:
        group = [pf for pf in url_prefixes(u, as_of) if pf[0] not in seen]
        if not group or len(prefixes) + len(group) > MAX_QUERIES_PER_DIRECTION:
            continue
        prefixes += group
        seen |= {pf[0] for pf in group}
    lists, errors = [], []
    for prefix, frm in prefixes:
        try:
            rows = list_prefix(prefix, frm, as_of)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{prefix}: {type(e).__name__}"[:120])
            continue
        best = {}
        for ts, u in rows:
            if _JUNK.search(urllib.parse.urlsplit(u).path):
                continue
            c = _canon(u)
            if c not in best or ts < best[c]:
                best[c] = ts
        lists.append(sorted(((ts, u) for u, ts in best.items()), reverse=True))
    out, used = [], set()
    while len(out) < MAX_CANDIDATES_TO_PICKER and any(lists):
        for lst in lists:
            while lst:
                ts, u = lst.pop(0)
                if u not in used:
                    used.add(u)
                    out.append({"url": u, "first_archived": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"})
                    break
            if len(out) >= MAX_CANDIDATES_TO_PICKER:
                break
    return {"prefixes": [p for p, _ in prefixes], "errors": errors, "candidates": out}


def pick(ctx, target: dict, d: dict, cands: list, cap: int) -> tuple:
    """PICKER：只看候选 URL 和存档日期。返回 (urls, error)。失败时取最新的 cap 个。"""
    if not cands:
        return [], "no archived candidates"
    lines = "\n".join(f"c{i} | {c['first_archived']} | {c['url']}" for i, c in enumerate(cands, start=1))
    out, err = ctx.llm.ask(PICK_SYSTEM, PICK_USER.format(
        cap=cap, as_of=ctx.as_of_s, candidates=lines,
        **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end", "publisher")},
        **{k: str(d.get(k, ""))[:600] for k in ("category", "perspective", "hypothesis", "data_to_find")}),
        role=f"pick:{d['id']}", qid=ctx.qid, max_tokens=300)
    picks = []
    for x in (out or {}).get("picks") or []:
        m = re.fullmatch(r"c(\d+)", str(x).strip())
        if m and 1 <= int(m.group(1)) <= len(cands) and cands[int(m.group(1)) - 1]["url"] not in picks:
            picks.append(cands[int(m.group(1)) - 1]["url"])
    if picks:
        return picks[:cap], None
    return [c["url"] for c in cands[:cap]], f"picker gave no valid ids ({err or 'empty'}); took the {cap} most recent"

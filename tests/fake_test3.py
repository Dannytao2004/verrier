"""留出测试 3 的假数据世界（tests/test_run_test3.py 用）：4 道 test3 题的假网页、假抽取、假裁判、假基线回复，假的 DeepSeek
（chat/completions 和 anthropic/v1/messages，走真实的 llm.LLM.json_call / Searcher.search 和 urllib 请求对象），假取页，联网守卫。
数字都是编的，不是官方值；每页都避开登记的泄漏写法，只有一页故意带着 CN 的真值（测哨兵）。不联网、不读 key 文件、不写 data/raw。
"""
import io
import json
import re
import socket
import threading
import urllib.error
from contextlib import ExitStack, contextmanager
from unittest import mock

FAKE_KEY = "sk-test3-FAKE-0123456789abcdef"
CTX = threading.local()   # 当前这次调用的 (role, qid)：包一层 LLM.json_call / Searcher.search 设进来
MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
       "December"]


def _ym(s):
    return int(s[:4]), int(s[5:7])


def _end(y, m):
    import calendar
    return f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"


def _month_point(name, ym, vw, sw, unit, quote):
    y, m = _ym(ym)
    return {"name": name, "value_as_written": vw, "number": float(vw.replace(",", "")), "scale_word": sw, "unit": unit,
            "period_start": f"{y}-{m:02d}-01", "period_end": _end(y, m), "published_at_if_visible": "", "quote": quote}


def _page(url, page_date, sentences, points):
    return {"url": url, "page_date": page_date, "text": " ".join(sentences), "points": points}


# ---------- 四道题的假网页 ----------
def _us():
    rows = [("2025-03", 711214), ("2025-04", 712866), ("2025-05", 709931), ("2025-06", 720164), ("2025-07", 726377),
            ("2025-08", 731048), ("2025-09", 733512), ("2025-10", 734209), ("2025-11", 735876), ("2025-12", 737041),
            ("2026-01", 741288), ("2026-02", 748934), ("2026-03", 754911), ("2026-04", 759097), ("2026-05", 763705)]

    def pg(url, date, rs):
        sents, pts = [], []
        for ym, v in rs:
            y, m = _ym(ym)
            q = f"Retail and food services sales, {MON[m - 1]} {y}: ${v:,} million"
            sents.append(q + ".")
            pts.append(_month_point(f"US retail and food services sales, {MON[m - 1]} {y}", ym, f"{v:,}", "million", "USD", q))
        return _page(url, date, sents, pts)
    return [pg("https://www.census.gov/retail/fake/adv2605.html", "2026-06-17", rows[7:]),
            pg("https://www.census.gov/retail/fake/adv2509.html", "2025-10-16", rows[:7])]


def _nz():
    rows = [("2025-01", 5812334120), ("2025-02", 5934781442), ("2025-03", 7594592976), ("2025-04", 7102553871),
            ("2025-05", 7688214309), ("2025-06", 6912447013), ("2025-07", 6734118552), ("2025-08", 6287903664),
            ("2025-09", 6041778215), ("2025-10", 6552309877), ("2025-11", 6904211436), ("2025-12", 7013872651),
            ("2026-01", 6108334297), ("2026-02", 6640118923)]
    sents, pts = [], []
    for ym, v in rows:
        y, m = _ym(ym)
        q = f"Goods exports in {MON[m - 1]} {y} were ${v:,}"
        sents.append(q + ".")
        pts.append(_month_point(f"New Zealand goods exports, {MON[m - 1]} {y}", ym, f"{v:,}", "", "NZD", q))
    return [_page("https://www.stats.govt.nz/fake/overseas-merchandise-trade-february-2026/", "2026-03-20", sents, pts)]


def _uk():
    def month(ym, v):
        y, m = _ym(ym)
        q = f"The number of registered company insolvencies in England and Wales was {v:,} in {MON[m - 1]} {y}"
        return q + ".", _month_point(f"Registered company insolvencies, England and Wales, {MON[m - 1]} {y}", ym, f"{v:,}", "",
                                     "insolvency", q)

    def part(y, v):
        q = f"Registered company insolvencies in England and Wales from 1 to 14 August {y}: {v:,}"
        return q + ".", {"name": f"Registered company insolvencies, England and Wales, 1-14 August {y}", "value_as_written": f"{v:,}",
                         "number": float(v), "scale_word": "", "unit": "insolvency", "period_start": f"{y}-08-01",
                         "period_end": f"{y}-08-14", "published_at_if_visible": "", "quote": q}
    a = [month(*r) for r in (("2026-06", 2019), ("2026-05", 1987), ("2025-06", 2211), ("2025-05", 2064))]
    b = [month(*r) for r in (("2025-08", 2048), ("2025-07", 2083), ("2024-08", 1933))]
    c = [part(2026, 905), part(2025, 960), part(2024, 879)]
    return [_page("https://www.gov.uk/fake/company-insolvencies-june-2026", "2026-07-20", *map(list, zip(*a))),
            _page("https://www.gov.uk/fake/company-insolvencies-august-2025", "2025-09-20", *map(list, zip(*b))),
            _page("https://www.insolvency-notices.example.org/fake/august-2026", "2026-08-18", *map(list, zip(*c)))]


def _cn():
    def pg(url, date, rs):
        sents, pts = [], []
        for ym, v in rs:
            y, m = _ym(ym)
            q = f"{y}年{m}月份，社会消费品零售总额{v}亿元"
            sents.append(q + "。")
            pts.append(_month_point(f"China total retail sales of consumer goods, {MON[m - 1]} {y}", ym, str(v), "亿", "CNY", q))
        return _page(url, date, sents, pts)
    leak = _page("https://www.example-forecasts.cn/fake/2026-04-preview", "2026-04-17",
                 ["市场预计2026年4月份社会消费品零售总额37247亿元。"], [])
    return [pg("https://www.stats.gov.cn/fake/t20260416.html", "2026-04-16", (("2026-03", 41616), ("2025-12", 45136),
                                                                              ("2025-11", 43898))),
            pg("https://www.stats.gov.cn/fake/t20250519.html", "2025-05-20", (("2025-04", 37174), ("2025-03", 40940))),
            pg("https://www.stats.gov.cn/fake/t20250117.html", "2025-01-20", (("2024-12", 45172), ("2024-11", 43763))),
            leak]


TARGETS = {
    "fc_cn_retail_2026_04": {"what": "China total retail sales of consumer goods, April 2026 (single month)", "unit": "CNY",
                             "period_start": "2026-04-01", "period_end": "2026-04-30", "publisher": "NBS", "cadence": "monthly",
                             "outcome_type": "continuous", "unit_canonical": "CNY"},
    "fc_us_retail_2026_06": {"what": "US retail and food services sales, June 2026 (SA, advance)", "unit": "USD",
                             "period_start": "2026-06-01", "period_end": "2026-06-30", "publisher": "US Census Bureau",
                             "cadence": "monthly", "outcome_type": "continuous", "unit_canonical": "USD"},
    "fc_uk_insolv_2026_08": {"what": "Registered company insolvencies in England and Wales, August 2026", "unit": "insolvency",
                             "period_start": "2026-08-01", "period_end": "2026-08-31", "publisher": "The Insolvency Service",
                             "cadence": "monthly", "outcome_type": "continuous", "unit_canonical": "insolvency"},
    "fc_nz_exports_2026_03": {"what": "New Zealand goods exports, March 2026", "unit": "NZD", "period_start": "2026-03-01",
                              "period_end": "2026-03-31", "publisher": "Stats NZ", "cadence": "monthly",
                              "outcome_type": "continuous", "unit_canonical": "NZD"},
}
PAGES = {"fc_us_retail_2026_06": _us(), "fc_nz_exports_2026_03": _nz(), "fc_uk_insolv_2026_08": _uk(), "fc_cn_retail_2026_04": _cn()}
BY_URL = {p["url"]: p for ps in PAGES.values() for p in ps}
# 结构化臂的路线：(名字, 值, low, high, 单位) 和三条公式（目标单位 = 题目登记的 answer_unit）
STRUCT = {
    "fc_cn_retail_2026_04": ("CNY", [("april_2025", 3.72e12, 3.6e12, 3.8e12, "CNY"), ("growth", 1.02, 0.98, 1.06, ""),
                                     ("people", 1.408e9, 1.40e9, 1.41e9, "person"), ("spend", 2650, 2400, 2900, "CNY/person"),
                                     ("march", 4.16e12, 4.1e12, 4.2e12, "CNY"), ("ratio", 0.9, 0.85, 0.95, "")],
                             ["april_2025 * growth", "people * spend", "march * ratio"]),
    "fc_us_retail_2026_06": ("USD", [("june_2025", 7.2e11, 7.1e11, 7.3e11, "USD"), ("growth", 1.04, 1.01, 1.07, ""),
                                     ("households", 1.32e8, 1.28e8, 1.36e8, "household"),
                                     ("spend", 5800, 5300, 6300, "USD/household"), ("may", 7.6e11, 7.5e11, 7.7e11, "USD"),
                                     ("ratio", 1.003, 0.99, 1.016, "")],
                             ["june_2025 * growth", "households * spend", "may * ratio"]),
    "fc_uk_insolv_2026_08": ("", [("august_2025", 2048, 2000, 2100, "company"), ("growth", 0.97, 0.9, 1.05, ""),
                                  ("companies", 5.5e6, 5.3e6, 5.7e6, "company"), ("rate", 3.6e-4, 3.0e-4, 4.2e-4, ""),
                                  ("july", 2000, 1900, 2100, "company"), ("ratio", 0.98, 0.92, 1.04, "")],
                          ["august_2025 * growth", "companies * rate", "july * ratio"]),
    "fc_nz_exports_2026_03": ("NZD", [("march_2025", 7.6e9, 7.4e9, 7.8e9, "NZD"), ("growth", 1.03, 0.97, 1.09, ""),
                                      ("tonnes", 2.6e6, 2.3e6, 2.9e6, "t"), ("price", 3000, 2700, 3300, "NZD/t"),
                                      ("february", 6.6e9, 6.5e9, 6.7e9, "NZD"), ("ratio", 1.15, 1.05, 1.25, "")],
                              ["march_2025 * growth", "tonnes * price", "february * ratio"]),
}
NAIVE = {"fc_cn_retail_2026_04": (3.75e12, "CNY"), "fc_us_retail_2026_06": (7.7e11, "USD"), "fc_uk_insolv_2026_08": (2000, ""),
         "fc_nz_exports_2026_03": (7.5e9, "NZD")}
# 裁判的分析路线：最近一个月 x 假设的月度比（单位核对会被调到）
LATEST = {"fc_cn_retail_2026_04": ("China total retail sales of consumer goods, March 2026", 0.9, 0.85, 0.95),
          "fc_us_retail_2026_06": ("US retail and food services sales, May 2026", 1.003, 0.99, 1.016),
          "fc_uk_insolv_2026_08": ("Registered company insolvencies, England and Wales, June 2026", 0.97, 0.9, 1.04),
          "fc_nz_exports_2026_03": ("New Zealand goods exports, February 2026", 1.15, 1.05, 1.25)}
PREFIX = {"fc_cn_retail_2026_04": "China total retail sales of consumer goods, ", "fc_us_retail_2026_06": "US retail and food services sales, ",
          "fc_uk_insolv_2026_08": "Registered company insolvencies, England and Wales, ", "fc_nz_exports_2026_03": "New Zealand goods exports, "}


def structured_reply(qid):
    unit, inputs, formulas = STRUCT[qid]
    return {"target": {"definition": TARGETS[qid]["what"], "unit": unit},
            "inputs": [{"name": n, "description": n.replace("_", " "), "value": v, "low": lo, "high": hi, "unit": u,
                        "provenance": {"type": "assumption", "rationale": "fake"}} for n, v, lo, hi, u in inputs],
            "paths": [{"id": f"p{i + 1}", "method": m, "description": m, "formula": f, "output_unit": unit}
                      for i, (m, f) in enumerate(zip(("top_down", "bottom_up", "proxy"), formulas))]}


def _rows(user):
    """裁判 prompt 里的数据点表 -> [(id, name, period)]。"""
    out = []
    for line in user.splitlines():
        c = line.split(" | ")
        if len(c) >= 6 and re.fullmatch(r"p\d+", c[0]):
            out.append((c[0], c[2], c[5]))
    return out


def judge_reply(qid, user):
    rows = _rows(user)
    hist = [i for i, n, _ in rows if n.startswith(PREFIX[qid]) and "1-14" not in n]
    name, v, lo, hi = LATEST[qid]
    latest = next(i for i, n, _ in rows if n == name)
    unit = TARGETS[qid]["unit_canonical"]
    methods = [{"id": "m1", "method": "series_auto", "params": {"target_history": hist}, "rationale": "own monthly history"},
               {"id": "m2", "method": "formula_mc", "params": {"formula": "x * g", "inputs": {
                   "x": {"id": latest, "role": f"{name.split(', ')[-1]} value of the target series"},
                   "g": {"id": "a1", "role": "ratio of the target month to the latest observed month"}}},
                "unit": unit, "coverage": {"kind": "full"}, "rationale": "latest month times a monthly ratio"}]
    if qid == "fc_uk_insolv_2026_08":
        part = {int(n[-4:]): i for i, n, _ in rows if "1-14 August" in n}
        full = {int(n[-4:]): i for i, n, _ in rows if n.startswith(PREFIX[qid]) and n.endswith(("August 2025", "August 2024"))
                and "1-14" not in n}
        methods.append({"id": "m3", "method": "partial_period", "params": {
            "partial_this": part[2026], "partial_last": [part[2025], part[2024]], "full_last": [full[2025], full[2024]]},
            "rationale": "first two weeks scaled by earlier years' coverage"})
    return {"assessment": [], "decisions": [], "extra_directions": [], "methods": methods,
            "assumptions": [{"id": "a1", "name": "Ratio of the target month to the latest observed month", "value": v, "low": lo,
                             "high": hi, "unit": "ratio", "rationale": "seasonal pattern in earlier years (fake)",
                             "applies_when": "the seasonal pattern holds", "falsified_by": "a shock in the target month",
                             "route": "m2"}]}


def unit_reply(qid, role):
    u = TARGETS[qid]["unit_canonical"]
    ins = [{"name": "x", "reason": "latest month", "unit": u}, {"name": "g", "reason": "ratio", "unit": "1"}]
    if role.startswith("unit_check"):
        return {"inputs": [dict(i, recorded_unit_ok=True) for i in ins], "derivation": f"{u} * 1 = {u}", "result_unit": u,
                "declared_unit_matches": True}
    return {"inputs": ins, "derivation": f"{u} * 1 = {u}", "result_unit": u, "fit_reason": "same quantity", "fits_target": True}


def plan_reply(qid):
    return {"target": dict(TARGETS[qid]), "market_keywords": [],
            "directions": [{"category": "own_history", "hypothesis": "monthly series of the target", "data_to_find": "monthly values",
                            "search_hints": ["q"]},
                           {"category": "related_series", "hypothesis": "partial-month data", "data_to_find": "weekly values",
                            "search_hints": ["q"]}]}


def extract_reply(user):
    for p in BY_URL.values():
        if p["text"] and p["text"] in user:
            return {"points": [dict(x) for x in p["points"]]}
    return {"points": []}


# ---------- 假服务 ----------
class Resp:
    def __init__(self, body):
        self.status, self._body, self._done = 200, body, False

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self, *a):
        return self._body

    def read1(self, n):
        if self._done:
            return b""
        self._done = True
        return self._body


USAGE = {"prompt_tokens": 1000, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 1000, "completion_tokens": 200,
         "completion_tokens_details": {"reasoning_tokens": 50}}


class FakeDeepSeek:
    """script[(cid, role 前缀)] = [回复, ...]：这个配置、这个角色依次用这些回复（"BAD_JSON" / "TRUNCATED" / "HTTP500" / "CRASH"；
    搜索另有 "HTTP402"），
    用完以后按正常回复。requests 记下每个 chat 请求的 (cid, role, thinking type, reasoning_effort, max_tokens)。"""

    def __init__(self):
        self.cid, self.script, self.requests, self.searches, self.other = None, {}, [], [], []
        self.last_judge, self.lock = {}, threading.Lock()

    def _scripted(self, role):
        with self.lock:
            for (cid, pre), q in self.script.items():
                if cid == self.cid and role.startswith(pre) and q:
                    return q.pop(0)
        return None

    def __call__(self, req, timeout):
        url, body = req.full_url, json.loads(req.data.decode("utf-8"))
        role, qid = getattr(CTX, "role", None), getattr(CTX, "qid", None)
        if url == "https://api.deepseek.com/anthropic/v1/messages":
            with self.lock:
                self.searches.append((self.cid, role, qid))
            if self._scripted(role) == "HTTP402":   # 余额不足（DeepSeek 402）
                raise urllib.error.HTTPError(url, 402, "Payment Required", {}, io.BytesIO(b""))
            urls = [p["url"] for p in PAGES[qid]]
            return Resp(json.dumps({"stop_reason": "end_turn", "content": [
                {"type": "server_tool_use", "id": "s1", "input": {"query": "monthly statistics"}},
                {"type": "web_search_tool_result", "tool_use_id": "s1",
                 "content": [{"type": "web_search_result", "url": u} for u in urls]},
                {"type": "text", "text": "\n".join(urls)}],
                "usage": {"input_tokens": 5000, "output_tokens": 300, "server_tool_use": {"web_search_requests": 1}}}).encode())
        if url != "https://api.deepseek.com/chat/completions":
            with self.lock:
                self.other.append(url)
            raise AssertionError(f"unexpected URL {url}")
        with self.lock:
            self.requests.append((self.cid, role, body["thinking"]["type"], body.get("reasoning_effort"), body["max_tokens"]))
        s = self._scripted(role)
        if s == "CRASH":
            raise RuntimeError("fake crash inside the model call")
        if s == "HTTP500":
            raise urllib.error.HTTPError(url, 500, "busy", {}, io.BytesIO(b""))
        msgs = body["messages"]
        content, fin = json.dumps(self.reply(role, qid, msgs), ensure_ascii=False), "stop"
        if s == "BAD_JSON":
            content = content[:-3] + ",]"
        elif s == "TRUNCATED":
            content, fin = content[: len(content) // 2], "length"
        return Resp(json.dumps({"choices": [{"message": {"content": content}, "finish_reason": fin}], "usage": USAGE}).encode())

    def reply(self, role, qid, msgs):
        user = msgs[1]["content"]
        if role == "naive":
            est, unit = NAIVE[qid]
            return {"estimate": est, "unit": unit}
        if role == "structured":
            return structured_reply(qid)
        if role == "plan":
            return plan_reply(qid)
        if role.startswith("extract"):
            return extract_reply(user)
        if role.startswith("judge"):   # 修正轮的 prompt 里没有数据点表：照上一轮的回复
            if _rows(user):
                self.last_judge[(self.cid, qid)] = judge_reply(qid, user)
            return self.last_judge[(self.cid, qid)]
        if role == "audit":
            return {"methods": []}
        if role.startswith(("unit_check", "unit_arbiter")):
            return unit_reply(qid, role)
        if role.startswith(("value_check", "value_reread")):
            return {"match": True}
        if role == "final":
            return {"answer": "About [[estimate]] ([[interval_level]] interval [[p10]] to [[p90]])."}
        raise AssertionError(f"no fake reply for role {role}")


def fake_fetch(url, as_of, qid, **kw):
    p = BY_URL.get(url)
    if p is None:
        return {"url": url, "status": "dropped", "reason": "fake: unknown url", "snapshot_ts": None, "page_date": None}
    return {"url": url, "status": "snapshot", "snapshot_ts": p["page_date"].replace("-", "") + "000000", "page_date": p["page_date"],
            "page_published": None, "text": p["text"]}


class NetGuard:
    """真实联网的入口都换成记录 + 抛错：socket.create_connection、socket.socket.connect、socket.getaddrinfo。"""

    def __init__(self):
        self.attempts = []

    def _block(self, name):
        def f(*a, **k):
            self.attempts.append((name, repr(a)[:120]))
            raise OSError(f"network blocked in tests ({name})")
        return f

    def patches(self):
        return [mock.patch.object(socket, "create_connection", self._block("create_connection")),
                mock.patch.object(socket.socket, "connect", self._block("connect")),
                mock.patch.object(socket, "getaddrinfo", self._block("getaddrinfo"))]


@contextmanager
def fake_world(agent_res):
    """装好假世界：返回 (fake 服务, 联网守卫)。agent_res：agent 结果目录（代替 results/agent）。"""
    from triangulate import llm
    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    from triangulate.agent import run as R
    from triangulate.agent import search as S
    net, guard = FakeDeepSeek(), NetGuard()
    real_json_call, real_search = llm.LLM.json_call, S.Searcher.search

    def json_call(self, messages, *, arm, qid, attempt, max_tokens=4000):
        CTX.role, CTX.qid = arm, qid
        return real_json_call(self, messages, arm=arm, qid=qid, attempt=attempt, max_tokens=max_tokens)

    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        CTX.role, CTX.qid = role, qid
        return real_search(self, prompt, role=role, qid=qid, max_uses=max_uses, cap=cap)

    def no_key_file(*a, **k):
        raise AssertionError("the key file must not be read in tests")
    with ExitStack() as st:
        for p in guard.patches():
            st.enter_context(p)
        st.enter_context(mock.patch.object(llm, "urlopen_no_redirect", net))
        st.enter_context(mock.patch.object(llm.LLM, "json_call", json_call))
        st.enter_context(mock.patch.object(S.Searcher, "search", search))
        st.enter_context(mock.patch.object(llm, "read_key", return_value=FAKE_KEY))
        st.enter_context(mock.patch.object(S, "read_key", return_value=FAKE_KEY))
        st.enter_context(mock.patch("triangulate.config.read_key", no_key_file))
        st.enter_context(mock.patch.object(P, "fetch_page", fake_fetch))
        st.enter_context(mock.patch.object(P, "fetch_live", lambda *a, **k: (_ for _ in ()).throw(AssertionError("live fetch"))))
        st.enter_context(mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "fake"}))
        st.enter_context(mock.patch.object(R, "RES", agent_res))
        st.enter_context(mock.patch("time.sleep"))
        yield net, guard

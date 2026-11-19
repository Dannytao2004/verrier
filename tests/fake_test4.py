"""留出测试 4 的假数据世界（tests/test_run_test4.py 用）：2 道 test4 题的假 live 网页、假抽取、假裁判、假基线回复，假的 DeepSeek
（chat/completions 和 anthropic/v1/messages：agent 的 SEARCHER 和 search_direct 臂都走真实的 Searcher.search / DirectClient.call
和 urllib 请求对象），假的 live 取页（快照路径一被调用就报错），联网守卫。真实使用：agent.run 的「今天」换成 FAKE_TODAY。
数字都是编的，不是官方值。不联网、不读 key 文件、不写 data/raw。页面、假服务和联网守卫的写法照 tests/fake_test3.py。
"""
import io
import json
import threading
import urllib.error
from contextlib import ExitStack, contextmanager
from datetime import date, datetime, timedelta, timezone
from unittest import mock

from tests import fake_test3 as W3

FAKE_KEY = "sk-test4-FAKE-0123456789abcdef"
CTX = threading.local()   # 当前这次调用的 (role, qid)
LOCAL_TZ = timezone(timedelta(hours=-5))                           # 美国中部 CDT（固定偏移，测试不依赖本机时区）
NOW = datetime(2026, 10, 24, 15, 0, tzinfo=timezone.utc)           # 周六，美国中部时间 10:00：不是高峰
FAKE_TODAY = date(2026, 10, 24)
MON = W3.MON
CN, TW = "fc_cn_profits_2026_09", "fc_tw_visitors_2026_09"
SEARCH_URL = "https://api.deepseek.com/anthropic/v1/messages"
CHAT_URL = "https://api.deepseek.com/chat/completions"


class _Today(date):
    """agent.run 里的 date：today() 固定为 FAKE_TODAY（checks_published 用它判断真实使用）。"""

    @classmethod
    def today(cls):
        return FAKE_TODAY


# ---------- 两道题的假网页（as_of 之前公布） ----------
def _cn():
    def pg(url, page_date, rows):
        sents, pts = [], []
        for y, m, v in rows:
            q = f"{y}年1—{m}月份，全国规模以上工业企业实现利润总额{v}亿元"
            sents.append(q + "。")
            pts.append({"name": f"China industrial enterprise profits, January-{MON[m - 1]} {y} (cumulative)",
                        "value_as_written": str(v), "number": float(v), "scale_word": "亿", "unit": "CNY",
                        "period_start": f"{y}-01-01", "period_end": W3._end(y, m), "published_at_if_visible": "", "quote": q})
        return W3._page(url, page_date, sents, pts)
    return [pg("https://www.stats.gov.cn/fake/t20260928.html", "2026-09-28", ((2026, 8, 51234.5), (2026, 7, 45012.3))),
            pg("https://www.stats.gov.cn/fake/t20251027.html", "2025-10-27", ((2025, 9, 52900.0), (2025, 8, 46100.2)))]


def _tw():
    rows = [("2025-01", 701233), ("2025-02", 652118), ("2025-03", 668904), ("2025-04", 655431), ("2025-05", 612877),
            ("2025-06", 598812), ("2025-07", 671205), ("2025-08", 668043), ("2025-09", 598771), ("2025-10", 702345),
            ("2025-11", 735512), ("2025-12", 790026), ("2026-01", 720114), ("2026-02", 698027), ("2026-03", 701552),
            ("2026-04", 688214), ("2026-05", 640335), ("2026-06", 629908), ("2026-07", 690121), ("2026-08", 655873)]
    sents, pts = [], []
    for ym, v in rows:
        y, m = W3._ym(ym)
        q = f"Visitor arrivals to Taiwan in {MON[m - 1]} {y}: {v:,}"
        sents.append(q + ".")
        pts.append(W3._month_point(f"Visitor arrivals to Taiwan, {MON[m - 1]} {y}", ym, f"{v:,}", "", "visitor", q))
    return [W3._page("https://stat.taiwan.example.gov.tw/fake/visitors-2026-08", "2026-09-25", sents, pts)]


TARGETS = {
    CN: {"what": "Total profits of China's industrial enterprises above designated size, January-September 2026 (cumulative)",
         "unit": "CNY", "period_start": "2026-01-01", "period_end": "2026-09-30", "publisher": "NBS", "cadence": "monthly",
         "outcome_type": "continuous", "unit_canonical": "CNY"},
    TW: {"what": "Visitor arrivals to Taiwan, September 2026", "unit": "visitor", "period_start": "2026-09-01",
         "period_end": "2026-09-30", "publisher": "Tourism Administration, MOTC", "cadence": "monthly",
         "outcome_type": "continuous", "unit_canonical": "visitor"},
}
PAGES = {CN: _cn(), TW: _tw()}
BY_URL = {p["url"]: p for ps in PAGES.values() for p in ps}
NAIVE = {CN: (5.8e12, "CNY"), TW: (630000, "")}
# 联网直接问的最后一段文字：CN 用「亿元」写成 100 million CNY（测代码换算），TW 写 visitors（计数名词）
DIRECT = {CN: (58500, "100 million CNY"), TW: (640000, "visitors")}
DIRECT_URLS = {CN: ["https://www.stats.gov.cn/fake/t20260928.html", "https://news.example.cn/fake/profits-aug"],
               TW: ["https://stat.taiwan.example.gov.tw/fake/visitors-2026-08", "https://news.example.tw/fake/sep-forecast"]}
# 裁判：最近一期 x 假设的比（CN：1-9 月 / 1-8 月；TW：9 月 / 8 月），TW 另加 series_auto（自己的月度序列）
LATEST = {CN: ("China industrial enterprise profits, January-August 2026 (cumulative)", 1.13, 1.10, 1.16),
          TW: ("Visitor arrivals to Taiwan, August 2026", 0.92, 0.85, 0.99)}
PREFIX = {TW: "Visitor arrivals to Taiwan, "}


def plan_reply(qid):
    return {"target": dict(TARGETS[qid]), "market_keywords": [],
            "directions": [{"category": "own_history", "hypothesis": "the target's own series", "data_to_find": "earlier values",
                            "search_hints": ["q"]},
                           {"category": "related_series", "hypothesis": "related data", "data_to_find": "related values",
                            "search_hints": ["q"]}]}


def judge_reply(qid, user):
    rows = W3._rows(user)
    name, v, lo, hi = LATEST[qid]
    latest = next(i for i, n, _ in rows if n == name)
    unit = TARGETS[qid]["unit_canonical"]
    methods = [{"id": "m2", "method": "formula_mc", "params": {"formula": "x * g", "inputs": {
        "x": {"id": latest, "role": "latest observed value of the target series"},
        "g": {"id": "a1", "role": "ratio of the target period to the latest observed period"}}},
        "unit": unit, "coverage": {"kind": "full"}, "rationale": "latest value times a ratio"}]
    if qid in PREFIX:
        hist = [i for i, n, _ in rows if n.startswith(PREFIX[qid])]
        methods.insert(0, {"id": "m1", "method": "series_auto", "params": {"target_history": hist}, "rationale": "own monthly history"})
    return {"assessment": [], "decisions": [], "extra_directions": [], "methods": methods,
            "assumptions": [{"id": "a1", "name": "Ratio of the target period to the latest observed period", "value": v, "low": lo,
                             "high": hi, "unit": "ratio", "rationale": "pattern in earlier years (fake)",
                             "applies_when": "the pattern holds", "falsified_by": "a shock in the target period", "route": "m2"}]}


def unit_reply(qid, role):
    u = TARGETS[qid]["unit_canonical"]
    ins = [{"name": "x", "reason": "latest value", "unit": u}, {"name": "g", "reason": "ratio", "unit": "1"}]
    if role.startswith("unit_check"):
        return {"inputs": [dict(i, recorded_unit_ok=True) for i in ins], "derivation": f"{u} * 1 = {u}", "result_unit": u,
                "declared_unit_matches": True}
    return {"inputs": ins, "derivation": f"{u} * 1 = {u}", "result_unit": u, "fit_reason": "same quantity", "fits_target": True}


def extract_reply(user):
    for p in BY_URL.values():
        if p["text"] and p["text"] in user:
            return {"points": [dict(x) for x in p["points"]]}
    return {"points": []}


def direct_reply(qid, body, scripted):
    """search_direct 的一次回复（Anthropic Messages 形状）。第 1 次（带工具）：思考块（请求开了思考或没写 thinking 字段时，
    同服务端默认）、一次搜索、结果、最后一段文字；第 2 次（不带工具）只有文字。scripted：NOT_JSON / MAX_TOKENS / DSML。"""
    est, unit = DIRECT[qid]
    final, stop = json.dumps({"estimate": est, "unit": unit}), "end_turn"
    if scripted == "NOT_JSON":
        final = "Based on the search results, my estimate is about the same as last year."
    elif scripted == "MAX_TOKENS":
        final, stop = "", "max_tokens"
    elif scripted == "DSML":   # 正式运行里真实出现过的失败：不带工具的重试里模型用文字写了一个工具调用
        final = ('<｜｜DSML｜｜ calls>\n<｜｜DSML｜｜ invoke name="web_search">\n<｜｜DSML｜｜ parameter name="query" string="true">'
                 'fake query</｜｜DSML｜｜ parameter>\n</｜｜DSML｜｜ invoke>\n</｜｜DSML｜｜ calls>')
    think = (body.get("thinking") or {}).get("type", "enabled") != "disabled"
    content = [{"type": "thinking", "thinking": "...", "signature": "x"}] if think else []
    n_req = 0
    if "tools" in body:
        n_req = 1
        content += [{"type": "text", "text": "I will search first."},
                    {"type": "server_tool_use", "id": "s1", "name": "web_search", "input": {"query": "official statistics"}},
                    {"type": "web_search_tool_result", "tool_use_id": "s1",
                     "content": [{"type": "web_search_result", "url": u, "title": "fake", "page_age": "2026-10-01",
                                  "encrypted_content": "xxx"} for u in DIRECT_URLS[qid]]}]
        if think:
            content.append({"type": "thinking", "thinking": "...", "signature": "y"})
    content.append({"type": "text", "text": final})
    return {"stop_reason": stop, "content": content,
            "usage": {"input_tokens": 6000, "output_tokens": 400, "server_tool_use": {"web_search_requests": n_req}}}


class FakeDeepSeek:
    """script[(cid, role 前缀)] = [回复, ...]：这个配置、这个角色依次用这些回复（chat："BAD_JSON" / "TRUNCATED" / "HTTP500" /
    "CRASH"；search_direct："NOT_JSON" / "MAX_TOKENS" / "DSML" / "HTTP500"），用完以后按正常回复。
    requests：chat 请求的 (cid, role, thinking type, reasoning_effort, max_tokens)；searches：agent SEARCHER 的 (cid, role, qid,
    请求体里有没有 thinking)；direct：search_direct 的 (cid, url, attempt, 请求体)。"""

    def __init__(self):
        self.cid, self.script, self.requests, self.searches, self.direct, self.other = None, {}, [], [], [], []
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
        if url == SEARCH_URL and "system" in body:   # search_direct（agent 的 SEARCHER 不带 system）
            with self.lock:
                self.direct.append((self.cid, url, getattr(CTX, "attempt", None), body))
            s = self._scripted("search_direct")
            if s == "HTTP500":
                raise urllib.error.HTTPError(url, 500, "busy", {}, io.BytesIO(b""))
            return W3.Resp(json.dumps(direct_reply(qid, body, s), ensure_ascii=False).encode())
        if url == SEARCH_URL:
            with self.lock:
                self.searches.append((self.cid, role, qid, "thinking" in body))
            urls = [p["url"] for p in PAGES[qid]]
            return W3.Resp(json.dumps({"stop_reason": "end_turn", "content": [
                {"type": "server_tool_use", "id": "s1", "input": {"query": "monthly statistics"}},
                {"type": "web_search_tool_result", "tool_use_id": "s1",
                 "content": [{"type": "web_search_result", "url": u} for u in urls]},
                {"type": "text", "text": "\n".join(urls)}],
                "usage": {"input_tokens": 5000, "output_tokens": 300, "server_tool_use": {"web_search_requests": 1}}}).encode())
        if url != CHAT_URL:
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
        content, fin = json.dumps(self.reply(role, qid, body["messages"]), ensure_ascii=False), "stop"
        if s == "BAD_JSON":
            content = content[:-3] + ",]"
        elif s == "TRUNCATED":
            content, fin = content[: len(content) // 2], "length"
        return W3.Resp(json.dumps({"choices": [{"message": {"content": content}, "finish_reason": fin}], "usage": W3.USAGE}).encode())

    def reply(self, role, qid, msgs):
        user = msgs[1]["content"]
        if role == "naive":
            est, unit = NAIVE[qid]
            return {"estimate": est, "unit": unit}
        if role == "magnitude":   # v2.15d 量级闸门的粗估：同直接问的数，按题目要的单位写
            est, unit = NAIVE[qid]
            return {"estimate": est, "unit": unit or TARGETS[qid]["unit_canonical"]}
        if role == "plan":
            return plan_reply(qid)
        if role.startswith("extract"):
            return extract_reply(user)
        if role.startswith("judge"):   # 修正轮的 prompt 里没有数据点表：照上一轮的回复
            if W3._rows(user):
                self.last_judge[(self.cid, qid)] = judge_reply(qid, user)
            return self.last_judge[(self.cid, qid)]
        if role == "audit":
            return {"methods": []}
        if role.startswith(("unit_check", "unit_arbiter")):
            return unit_reply(qid, role)
        if role.startswith(("value_check", "value_reread")):
            return {"match": True}
        if role.startswith("published"):   # 「答案已公布」确认（含提前停）：假页面里没有目标期间的值，都不是
            import re
            return {"candidates": [{"id": i, "verdict": "different", "reason": "fake"}
                                   for i in re.findall(r"^- ([ep]\d+): ", user, re.M)]}
        if role == "final":
            return {"answer": "About [[estimate]] ([[interval_level]] interval [[p10]] to [[p90]])."}
        raise AssertionError(f"no fake reply for role {role}")


def fake_live(url, as_of, qid, **kw):
    """真实使用的取页（pipeline.fetch_live）：假页面标 live_dated。"""
    p = BY_URL.get(url)
    if p is None:
        return {"url": url, "status": "dropped", "reason": "fake: unknown url", "snapshot_ts": None, "page_date": None}
    return {"url": url, "status": "live_dated", "snapshot_ts": None, "page_date": p["page_date"], "page_published": None,
            "text": p["text"]}


@contextmanager
def fake_world(agent_res):
    """装好假世界：返回 (fake 服务, 联网守卫)。agent_res：agent 结果目录（代替 results/agent）。"""
    from triangulate import llm
    from triangulate import search_direct as SD
    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    from triangulate.agent import run as R
    from triangulate.agent import search as S
    net, guard = FakeDeepSeek(), W3.NetGuard()
    real_json_call, real_search, real_direct = llm.LLM.json_call, S.Searcher.search, SD.DirectClient.call

    def json_call(self, messages, *, arm, qid, attempt, max_tokens=4000, **kw):   # v2.15b：thinking_off 照传
        CTX.role, CTX.qid = arm, qid
        if kw.get("thinking_off"):   # v2.15b：JSON 不合法后关思考的重问，记下来（测试按它放行这一次的 disabled）
            net.__dict__.setdefault("off_retries", []).append((getattr(net, "cid", None), arm))
        return real_json_call(self, messages, arm=arm, qid=qid, attempt=attempt, max_tokens=max_tokens, **kw)

    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        CTX.role, CTX.qid = role, qid
        return real_search(self, prompt, role=role, qid=qid, max_uses=max_uses, cap=cap)

    def direct(self, body, *, qid, attempt):
        CTX.role, CTX.qid, CTX.attempt = "search_direct", qid, attempt
        return real_direct(self, body, qid=qid, attempt=attempt)

    def no_key_file(*a, **k):
        raise AssertionError("the key file must not be read in tests")
    with ExitStack() as st:
        for p in guard.patches():
            st.enter_context(p)
        st.enter_context(mock.patch.object(llm, "urlopen_no_redirect", net))
        st.enter_context(mock.patch.object(llm.LLM, "json_call", json_call))
        st.enter_context(mock.patch.object(S.Searcher, "search", search))
        st.enter_context(mock.patch.object(SD.DirectClient, "call", direct))
        st.enter_context(mock.patch.object(llm, "read_key", return_value=FAKE_KEY))
        st.enter_context(mock.patch.object(S, "read_key", return_value=FAKE_KEY))
        st.enter_context(mock.patch("triangulate.config.read_key", no_key_file))
        st.enter_context(mock.patch.object(P, "fetch_live", fake_live))
        st.enter_context(mock.patch.object(P, "fetch_page", lambda *a, **k: (_ for _ in ()).throw(
            AssertionError("snapshot path in a real-use run"))))
        st.enter_context(mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "fake"}))
        st.enter_context(mock.patch.object(R, "RES", agent_res))
        st.enter_context(mock.patch.object(R, "date", _Today))
        st.enter_context(mock.patch("time.sleep"))
        yield net, guard

"""留出测试 4（probes/run_test4.py）：题库登记（没有真值、as_of 在跑的那天填）、门（首发时刻、高峰、时段不够、跨过本地午夜、
--wait）、12 个配置的假数据端到端（含每个臂各一种不合法的回复）、没有首发值和填了编造首发值两种打分。
假数据世界在 tests/fake_test4.py：真实的 LLM.json_call / Searcher.search / DirectClient.call 和 urllib 请求对象，HTTP 换成假的 DeepSeek，
真实使用的 live 取页换成假页（快照路径一被调用就报错），联网入口（socket）全部换成抛错并记录。不调模型、不联网、不读 key 文件，
结果写临时目录（不写 results/、data/raw/）。"""
import importlib.util
import json
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from triangulate import config, forecast
from triangulate.providers import role_max_tokens

try:
    import langgraph  # noqa: F401
    import statsforecast  # noqa: F401
    HAVE_DEPS = True
except ImportError:
    HAVE_DEPS = False

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("run_test4", ROOT / "probes" / "run_test4.py")
RT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RT)
CN, TW = "fc_cn_profits_2026_09", "fc_tw_visitors_2026_09"
TZ = timezone(timedelta(hours=-5))   # 美国中部 CDT（固定偏移）
SAT = datetime(2026, 10, 24, 15, 0, tzinfo=timezone.utc)          # 周六美国中部时间 10:00：不是高峰
FRI_PEAK = datetime(2026, 10, 23, 3, 0, tzinfo=timezone.utc)      # 周五北京 11:00：高峰
FRI_LUNCH = datetime(2026, 10, 23, 4, 30, tzinfo=timezone.utc)    # 周五北京 12:30：离 14:00 只剩 1.5 小时（美国中部时间周四 23:30）
THU_1900 = datetime(2026, 10, 23, 0, 0, tzinfo=timezone.utc)      # 周四美国中部时间 19:00：离下一个高峰（北京周五 9:00）1 小时
FRI_2350 = datetime(2026, 10, 24, 4, 50, tzinfo=timezone.utc)     # 周五美国中部时间 23:50（UTC 已是周六，不是高峰）
MON_1950 = datetime(2026, 10, 27, 0, 50, tzinfo=timezone.utc)     # 周一美国中部时间 19:50：10 分钟后高峰，40 分钟后 CN 首发
MON_2020 = datetime(2026, 10, 27, 1, 20, tzinfo=timezone.utc)     # 周一美国中部时间 20:20：高峰，10 分钟后 CN 首发
CN_RELEASE = datetime(2026, 10, 27, 1, 30, tzinfo=timezone.utc)
# 10-27 起 test4 登记了更多题（第 3-7 题），假数据世界只有最早的 2 道：本模块的测试把 test4 题库固定成这 2 道、首发值都没填；
# 真实题库的登记规则由 TestRegistry 检查
REAL_QUESTIONS, REAL_OFFICIAL = forecast.QUESTIONS, forecast.TEST4_OFFICIAL
_PATCHES = [mock.patch.object(forecast, "QUESTIONS", [q for q in forecast.QUESTIONS
                                                      if q.get("set") != "test4" or q["id"] in (CN, TW)]),
            mock.patch.object(forecast, "TEST4_OFFICIAL", {CN: None, TW: None})]


def setUpModule():
    for p in _PATCHES:
        p.start()


def tearDownModule():
    for p in _PATCHES:
        p.stop()


class TestRegistry(unittest.TestCase):
    def test_every_registered_question(self):
        qs = sorted((q for q in REAL_QUESTIONS if q.get("set") == "test4"), key=RT.release)
        self.assertEqual([q["id"] for q in qs][:2], [CN, TW])
        self.assertEqual(sorted(q["id"] for q in qs), sorted(REAL_OFFICIAL))
        self.assertEqual(len({q["id"] for q in qs}), len(qs))
        for q in qs:
            self.assertIsNotNone(datetime.fromisoformat(q["released_at"]).tzinfo, q["id"])
            self.assertNotIn("answer_value", q)
            self.assertEqual((q["as_of"], q["question"], q["leak_values"], q["strict"]), (None, None, [], False), q["id"])
            self.assertTrue(q["source"].startswith("http") and q["last_year_source"].startswith("http"), q["id"])
            self.assertTrue(q["question_template"].startswith("Assume today is {as_of}. You know nothing published after this date. "))
            self.assertEqual(q["question_template"].count("{"), 1, q["id"])   # 只有 {as_of}：with_as_of 的 format 不会出错
            self.assertGreater(q["last_year"], 0)
            sn = forecast.TEST4_SCORING_NOTES.get(q["id"])
            if sn is not None:   # 打分说明：登记的臂都存在、有原文
                self.assertTrue(set(sn["arms"]) <= set(RT.ARMS) and sn["note"], q["id"])
            off = REAL_OFFICIAL[q["id"]]
            if off is not None:   # 公布后填的首发值
                self.assertGreater(off["value"], 0)
                self.assertTrue(off["source"].startswith("https://") and off["quote"] and off["checked"], q["id"])


def _log(root):
    p = root / "run.log"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []


class TestBank(unittest.TestCase):
    def test_two_questions_registered_without_answers(self):
        qs = RT.questions()
        self.assertEqual([q["id"] for q in qs], [CN, TW])   # 按首发时刻排
        self.assertEqual([RT.release(q) for q in qs], [CN_RELEASE, datetime(2026, 10, 27, 8, 20, tzinfo=timezone.utc)])
        for q in qs:
            self.assertEqual(q["set"], "test4")
            self.assertNotIn("answer_value", q)
            self.assertIsNone(q["as_of"])
            self.assertIsNone(q["question"])
            self.assertEqual(q["leak_values"], [])
            self.assertFalse(q["strict"])
            self.assertTrue(q["source"].startswith("https://") and q["last_year_source"].startswith("https://"))
            self.assertTrue(q["question_template"].startswith("Assume today is {as_of}. You know nothing published after this date. "))
            self.assertIn(q["id"], forecast.TEST4_OFFICIAL)
            self.assertIsNone(forecast.TEST4_OFFICIAL[q["id"]])
        cn, tw = qs
        self.assertEqual((cn["answer_unit"], cn["unit_hint"], cn["last_year"]), ("CNY", "an amount of money in CNY", 5373200000000))
        self.assertEqual((tw["answer_unit"], tw["unit_hint"], tw["last_year"]), ("", "a count of visitor arrivals", 601339))
        self.assertIn("January-September 2026 (the cumulative total, not the single month of September)", cn["question_template"])

    def test_with_as_of_fills_a_copy(self):
        q = RT.questions()[0]
        r = forecast.with_as_of(q, "2026-10-24")
        self.assertEqual(r["as_of"], "2026-10-24")
        self.assertTrue(r["question"].startswith("Assume today is 2026-10-24. You know nothing published after this date. Estimate "))
        self.assertNotIn("{", r["question"])
        self.assertIsNone(q["as_of"])   # 题库里的那一条不变
        from triangulate.agent.run import checks_published
        self.assertTrue(checks_published(r, today=datetime(2026, 10, 24).date()))    # 真实使用
        self.assertFalse(checks_published(r, today=datetime(2026, 10, 25).date()))

    def test_forecast_run_and_report_skip_test4(self):
        def raw(arm, qid):
            return Path(__file__) if qid not in (CN, TW) else Path("does/not/exist.json")
        with mock.patch.object(forecast, "_raw", raw), mock.patch.object(forecast, "LLM", side_effect=AssertionError("no calls")):
            self.assertIsNone(forecast.run())
        self.assertIn("test4", forecast.OWN_RUNNER)

    def test_configs(self):
        cs = RT.configs()
        self.assertEqual(len(cs), 12)
        self.assertEqual([c["cid"] for c in cs[:6]], [f"{CN}__{a}__{m}" for a in RT.ARMS for m in RT.MODES])
        self.assertEqual(RT.THINKING_ON["search_direct"], {"search_direct": "high"})
        self.assertEqual(config.thinking_role("search_direct"), "search_direct")


class TestGate(unittest.TestCase):
    def runner(self, now, wait=False, sleep=None):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        r = RT.Runner(root=tmp, now=now if callable(now) else (lambda: now), sleep=sleep or (lambda s: None), wait=wait,
                      log=lambda s: None, tz=TZ)
        ran = []
        r.run_one = lambda c, rerun_reason="": ran.append((c["cid"], r.now())) or {"usd": 0.0, "outcome": "done"}
        return r, ran, tmp

    def test_release_reached(self):
        r, ran, tmp = self.runner(CN_RELEASE)
        res = r.run(RT.configs(RT.questions([CN])))
        self.assertEqual((res["ran"], res["stopped"], len(res["refused"])), ([], "release", 6))
        log = _log(tmp)
        self.assertEqual([x["event"] for x in log], ["refused"] * 6)
        self.assertTrue(all("reached (the answer may be public)" in x["reason"] for x in log))
        self.assertEqual(r.pending(RT.configs(RT.questions([CN])))[0]["cid"], f"{CN}__naive__off")   # 没有开跑、没有状态

    def test_would_finish_after_release(self):
        r, ran, tmp = self.runner(MON_2020)
        res = r.run(RT.configs(RT.questions([CN])))
        self.assertEqual(ran, [])
        self.assertEqual(sorted(res["refused"]), [f"{CN}__agent__off", f"{CN}__agent__think"])   # 12 / 30 分钟跑不完
        self.assertEqual(res["stopped"], "gate")
        log = _log(tmp)
        self.assertIn("would finish after the release time", log[0]["reason"])
        self.assertIn("peak hours now", log[-1]["reason"])   # 其余 4 个：高峰

    def test_peak_and_short_window(self):
        r, ran, tmp = self.runner(FRI_PEAK)
        self.assertEqual(r.run(RT.configs())["stopped"], "gate")
        self.assertIn("peak hours now", _log(tmp)[-1]["reason"])
        r, ran, tmp = self.runner(FRI_LUNCH)
        self.assertEqual(r.run(RT.configs())["stopped"], "gate")   # 12 个要 1:42:30，午间只剩 1:30
        self.assertIn("only 1:30:00 left before the next peak", _log(tmp)[-1]["reason"])
        self.assertEqual(ran, [])
        r, ran, tmp = self.runner(THU_1900)
        self.assertEqual(r.run(RT.configs())["stopped"], "gate")
        self.assertEqual(_log(tmp)[-1]["reason"], "only 1:00:00 left before the next peak; need 1:42:30")
        r, ran, tmp = self.runner(THU_1900)
        self.assertIsNone(r.run(RT.configs(RT.questions([CN])))["stopped"])   # 一题 51 分钟：够
        self.assertEqual(len(ran), 6)

    def test_local_midnight(self):
        r, ran, tmp = self.runner(FRI_2350)
        self.assertEqual(r.run(RT.configs(RT.questions([CN])))["stopped"], "gate")
        self.assertIn("would cross local midnight (2026-10-24T00:00-05:00)", _log(tmp)[-1]["reason"])
        clock, slept = {"t": FRI_2350}, []

        def sleep(s):
            slept.append(s)
            clock["t"] = clock["t"] + timedelta(seconds=s)
        r, ran, tmp = self.runner(lambda: clock["t"], wait=True, sleep=sleep)
        self.assertIsNone(r.run(RT.configs(RT.questions([CN])))["stopped"])
        self.assertEqual(slept, [600.0])   # 睡到本地午夜
        self.assertEqual(len(ran), 6)
        self.assertEqual(r.as_of(), "2026-10-24")

    def test_wait_does_not_wait_past_release(self):
        """周一 19:50：CN 一题 51 分钟，10 分钟后高峰、下一个非高峰时段（美国中部时间 23:00）已过首发：--wait 也拒跑，不睡。"""
        slept = []
        r, ran, tmp = self.runner(MON_1950, wait=True, sleep=slept.append)
        res = r.run(RT.configs(RT.questions([CN])))
        self.assertEqual((ran, slept, res["stopped"]), ([], [], "gate"))
        self.assertIn("would finish after the release time", _log(tmp)[-1]["reason"])   # 批的累计时长赶不上首发
        cs = [c for c in RT.configs(RT.questions([CN])) if c["cid"] == f"{CN}__agent__off"]
        r, ran, tmp = self.runner(MON_1950, wait=True, sleep=slept.append)
        self.assertEqual(r.run(cs)["stopped"], "gate")   # agent 关 12 分钟：高峰前不够，等到下一个时段（23:00）又过了首发
        self.assertEqual((ran, slept), ([], []))
        self.assertIn("would miss the release time", _log(tmp)[-1]["reason"])

    def test_plan_text(self):
        r, ran, tmp = self.runner(SAT)
        text = RT.plan_text(r)
        self.assertIn("12 configurations, 12 not run yet; estimated time 1:42:30", text)
        self.assertIn("batch gate now: would start", text)
        self.assertIn(f"{CN}: release 2026-10-27T01:30+00:00 = local 2026-10-26T20:30-05:00", text)
        self.assertEqual(text.count("(runnable now)"), 12)
        self.assertIn("latest start of this question's pending configurations (all four gates): local 2026-10-26T19:08-05:00",
                      text)   # 美国中部时间周一 20:00 起高峰：51 分钟要在 19:09 前开跑
        self.assertEqual(RT.latest_start(SAT, RT.configs(RT.questions([TW])), TZ),
                         datetime(2026, 10, 27, 5, 8, tzinfo=timezone.utc))   # 周二美国中部时间 0:08（午夜后、1:00 高峰前）
        self.assertFalse((tmp / "configs").exists())   # --plan 不写状态


# 故意坏掉的回复：(配置, 角色前缀) -> 依次用的回复。每个臂至少一种
SCRIPT = {
    (f"{CN}__naive__off", "naive"): ["BAD_JSON", "BAD_JSON"],                     # 两次都不合法：没出数
    (f"{TW}__naive__think", "naive"): ["BAD_JSON"],                               # 第二次（带错误重试）合法
    (f"{TW}__naive__off", "naive"): ["HTTP500"] * 3,                              # 传输失败：基础设施故障
    (f"{CN}__search_direct__think", "search_direct"): ["MAX_TOKENS", "DSML"],       # 截断，重试时用文字写工具调用：没出数
    (f"{TW}__search_direct__off", "search_direct"): ["NOT_JSON"],                  # 最后一段不是 JSON，重试（不带工具）合法
    (f"{CN}__agent__think", "judge"): ["BAD_JSON"],                               # 裁判第一次不合法，ask 的第二次合法
    (f"{TW}__agent__off", "final"): ["BAD_JSON", "BAD_JSON"],                     # 终稿不合法：用代码的默认文字
    (f"{TW}__agent__think", "plan"): ["CRASH"],                                   # 意外异常：这个配置记为崩溃
}
FABRICATED = {CN: {"value": 5.9e12, "source": "fake", "quote": "fake", "checked": "2026-10-27"}, TW: {"value": 650000}}


@unittest.skipUnless(HAVE_DEPS, "langgraph / statsforecast not installed (use .venv)")
class TestFakeEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests import fake_test4 as W
        cls.W = W
        cls.tmp = Path(tempfile.mkdtemp())
        cls.agent_res = cls.tmp / "agent"
        cls.real_out_existed = RT.OUT.exists()
        raw = ROOT / "data" / "raw" / "agent"
        cls.raw_dirs_before = {p.name for p in raw.glob("*")} if raw.exists() else set()
        with W.fake_world(cls.agent_res) as (net, guard):
            net.script = {k: list(v) for k, v in SCRIPT.items()}
            cls.net, cls.guard = net, guard
            cls.runner = RT.Runner(root=cls.tmp / "test4", now=lambda: W.NOW, sleep=lambda s: None, log=lambda s: None,
                                   on_start=lambda c: setattr(net, "cid", c["cid"]), tz=W.LOCAL_TZ)
            cls.res = cls.runner.run(RT.configs())
            cls.again = cls.runner.run(RT.configs())
            cls.unscored = json.loads(json.dumps(RT.score(cls.runner)))
            cls.unscored_md = (cls.tmp / "test4" / "summary.md").read_text(encoding="utf-8")
            with mock.patch.dict(forecast.TEST4_OFFICIAL, FABRICATED):
                cls.scored = RT.score(cls.runner)
            cls.scored_md = (cls.tmp / "test4" / "summary.md").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def status(self, cid):
        return self.runner.status({"cid": cid})

    def state(self, cid):
        qid, _, mode = cid.split("__")
        return json.loads((self.agent_res / qid / RT.AGENT_TAG[mode] / "state.json").read_text(encoding="utf-8"))

    def raw(self, cid):
        qid, arm, mode = cid.split("__")
        return json.loads((self.tmp / "test4" / "raw" / f"{arm}_{mode}" / f"{qid}.json").read_text(encoding="utf-8"))

    def test_every_configuration_ends_once(self):
        self.assertEqual(len(self.res["ran"]), 12)
        self.assertEqual((self.res["stopped"], self.res["refused"]), (None, []))
        outcomes = {c["cid"]: self.status(c["cid"])["outcome"] for c in RT.configs()}
        self.assertEqual(outcomes.pop(f"{TW}__agent__think"), "crashed")
        self.assertEqual(outcomes.pop(f"{TW}__naive__off"), "infra_failed")
        self.assertEqual(set(outcomes.values()), {"done"})
        self.assertIn("RuntimeError: fake crash", self.status(f"{TW}__agent__think")["error"])
        self.assertEqual(self.again, {"ran": [], "stopped": None, "refused": []})   # 一个配置只跑一次，崩溃的也不重跑
        cost = [x for x in _log(self.tmp / "test4") if x["event"] == "cost"]
        self.assertEqual(len(cost), 12)
        self.assertAlmostEqual(cost[-1]["cumulative_usd"], sum(self.status(c["cid"])["usd"] or 0 for c in RT.configs()), places=5)
        self.assertGreater(self.status(f"{TW}__search_direct__think")["usd"], 0.01)   # token 费 + 按假设单价记的搜索费

    def test_no_network_no_key_no_real_files(self):
        self.assertEqual(self.guard.attempts, [])
        self.assertEqual(self.net.other, [])
        self.assertEqual(RT.OUT.exists(), self.real_out_existed)
        raw = ROOT / "data" / "raw" / "agent"
        self.assertEqual({p.name for p in raw.glob("*")} if raw.exists() else set(), self.raw_dirs_before)
        self.assertTrue(self.net.searches and self.net.direct and self.net.requests)
        blob = "".join(p.read_text(encoding="utf-8") for p in self.tmp.rglob("*") if p.is_file())
        self.assertNotIn(self.W.FAKE_KEY, blob)

    def test_as_of_is_the_run_date(self):
        for c in RT.configs():
            st = self.status(c["cid"])
            self.assertEqual(st["as_of"], "2026-10-24", c["cid"])
            self.assertTrue(st["question"].startswith("Assume today is 2026-10-24. "), c["cid"])
        sd = self.raw(f"{TW}__search_direct__think")
        self.assertEqual(sd["as_of"], "2026-10-24")
        self.assertIn("Question: Assume today is 2026-10-24. You know nothing published after this date.", sd["user"])
        self.assertTrue(all("Assume today is 2026-10-24." in b["messages"][0]["content"] for *_, b in self.net.direct))

    def test_agent_runs_in_real_use_mode(self):
        for cid in (f"{CN}__agent__off", f"{CN}__agent__think", f"{TW}__agent__off"):
            st = self.state(cid)
            pages = [p for r in st["results"] for p in r.get("pages") or []]
            self.assertTrue(any(p["status"] == "live_dated" for p in pages), cid)   # live 页，没有快照
            self.assertFalse([p for p in pages if p.get("status") == "snapshot" or p.get("snapshot_ts")], cid)
            self.assertEqual(st["leakage"]["pages_snapshot"], 0)
            self.assertGreater(st["leakage"]["pages_live_dated"], 0)
            self.assertEqual(st["published"]["status"], "no_candidates", cid)   # 「答案已公布」检查做了（回测是 not_checked）
            self.assertEqual(st["as_of"], "2026-10-24")
            self.assertEqual(self.status(cid)["real_use"]["published_check"], "no_candidates")
        self.assertTrue(all(not has_thinking for *_, has_thinking in self.net.searches))   # agent 的搜索请求体没变

    def test_search_direct_requests(self):
        from triangulate import providers, search_direct as SD
        from triangulate.agent import search as S
        self.assertEqual(SD.SEARCH_URL, S.SEARCH_URL)
        self.assertEqual(SD.SEARCH_URL, providers.DEEPSEEK.search_url("global"))
        by_cid = {}
        for cid, url, attempt, body in self.net.direct:
            by_cid.setdefault(cid, []).append((attempt, body))
            mode = cid.split("__")[2]
            self.assertEqual(url, S.SEARCH_URL)
            if mode == "think":
                self.assertEqual((body["thinking"], body["output_config"]), ({"type": "enabled"}, {"effort": "high"}))
                self.assertEqual(body["max_tokens"], config.MAX_TOKENS["search_direct"] + config.THINKING_EXTRA_TOKENS)
            else:
                self.assertEqual(body["thinking"], {"type": "disabled"})
                self.assertNotIn("output_config", body)
                self.assertEqual(body["max_tokens"], config.MAX_TOKENS["search_direct"])
            if attempt == 1:
                self.assertEqual(body["tools"], [{"type": "web_search_20250305", "name": "web_search", "max_uses": SD.MAX_USES}])
            else:
                self.assertNotIn("tools", body)
        self.assertEqual(sorted(by_cid), sorted(c["cid"] for c in RT.configs() if c["arm"] == "search_direct"))
        self.assertEqual([a for a, _ in by_cid[f"{CN}__search_direct__off"]], [1])
        self.assertEqual([a for a, _ in by_cid[f"{TW}__search_direct__off"]], [1, 2])
        self.assertEqual([a for a, _ in by_cid[f"{CN}__search_direct__think"]], [1, 2])
        calls = (self.tmp / "test4" / "raw" / "search_direct_think" / f"{TW}.calls.jsonl").read_text(encoding="utf-8")
        self.assertEqual(json.loads(calls.splitlines()[0])["thinking"], "high")

    def test_search_direct_records_urls_and_units(self):
        W = self.W
        for qid in (CN, TW):
            rec = self.raw(f"{qid}__search_direct__think")
            a = rec["attempts"][0]
            self.assertEqual([r["url"] for r in a["results"]], W.DIRECT_URLS[qid])
            self.assertEqual(a["queries"], ["official statistics"])
        tw = self.raw(f"{TW}__search_direct__think")
        self.assertEqual((tw["status"], tw["estimate"], tw["thinking"], tw["max_tokens"]),
                         ("ok", 640000.0, "high", config.MAX_TOKENS["search_direct"] + config.THINKING_EXTRA_TOKENS))
        self.assertEqual(tw["attempts"][0]["n_thinking_blocks"], 2)
        st = self.status(f"{TW}__search_direct__think")
        self.assertEqual((st["result_urls"], st["web_search_requests"], st["estimate"]), (W.DIRECT_URLS[TW], 1, 640000.0))
        off = self.raw(f"{TW}__search_direct__off")
        self.assertEqual((off["thinking"], off["final_attempt"], off["estimate"]), ("disabled", 2, 640000.0))
        self.assertEqual([a["n_thinking_blocks"] for a in off["attempts"]], [0, 0])
        self.assertEqual(off["attempts"][0]["problems"], ["reply is not valid JSON"])
        rows = {r["config"]: r for r in self.unscored["configs"]}
        self.assertEqual(rows[f"{TW}__search_direct__think"]["estimate"], 640000.0)
        # CN 的回复写成 58500「100 million CNY」：记录和打分都经同 naive 的单位检查（check_naive）换算成元
        self.assertAlmostEqual(self.raw(f"{CN}__search_direct__off")["estimate"] / 5.85e12, 1.0, places=12)
        self.assertAlmostEqual(rows[f"{CN}__search_direct__off"]["estimate"] / 5.85e12, 1.0, places=12)
        cn = self.raw(f"{CN}__search_direct__think")   # 截断 + DSML：没出数；同样的单位检查（check_naive）
        self.assertEqual((cn["status"], cn["estimate"]), ("invalid_output", None))
        self.assertEqual(cn["attempts"][0]["problems"], ["reply was truncated (stop_reason=max_tokens)"])
        self.assertEqual(cn["attempts"][1]["problems"], ["reply is not valid JSON"])
        from triangulate.arms import check_naive   # CN 的回复写成「100 million CNY」：同 naive 的单位检查换算成元
        status, est, _ = check_naive({"estimate": 58500, "unit": "100 million CNY"}, "CNY", False)
        self.assertEqual(status, "ok")
        self.assertAlmostEqual(est / 5.85e12, 1.0, places=12)

    def test_chat_thinking_flags_per_configuration(self):
        seen = {}
        off = list(getattr(self.net, "off_retries", []))   # v2.15b：JSON 不合法后关思考重问的那几次
        for cid, role, kind, effort, mt in self.net.requests:
            arm, mode = cid.split("__")[1:]
            base = config.thinking_role(role)
            want = RT.THINKING_ON[arm].get(base) if mode == "think" else None
            if want and kind == "disabled" and (cid, role) in off:
                off.remove((cid, role))
                want = None
            self.assertEqual((kind, effort), ("enabled" if want else "disabled", want), (cid, role))
            # v2.13d：DeepSeek 的裁判 / 修正 / 抽取用模型自己的默认上限（providers.role_max_tokens）
            self.assertEqual(mt, role_max_tokens(config.MODEL, base, config.MAX_TOKENS[base])
                             + (config.THINKING_EXTRA_TOKENS if want else 0), (cid, role))
            seen.setdefault((arm, mode), set()).add(base)
        self.assertTrue({"plan", "extract", "judge", "audit", "unit_check", "unit_arbiter", "final"} <= seen[("agent", "off")])
        self.assertTrue({"plan", "judge", "audit", "unit_arbiter"} <= seen[("agent", "think")])
        self.assertEqual(seen[("naive", "think")], {"naive"})
        self.assertNotIn(("search_direct", "off"), seen)   # search_direct 不走 chat/completions
        got = self.state(f"{CN}__agent__think")["settings"].get("thinking")
        self.assertEqual(got and got["by_role"], RT.THINKING_ON["agent"])
        self.assertIsNone(self.state(f"{CN}__agent__off")["settings"].get("thinking"))

    def test_malformed_replies_recorded(self):
        rows = {r["config"]: r for r in self.unscored["configs"]}
        self.assertEqual((rows[f"{CN}__naive__off"]["arm_status"], rows[f"{CN}__naive__off"]["estimate"]), ("invalid_output", None))
        self.assertEqual((rows[f"{TW}__naive__think"]["arm_status"], rows[f"{TW}__naive__think"]["attempts"]), ("ok", 2))
        self.assertEqual((rows[f"{TW}__naive__off"]["outcome"], rows[f"{TW}__naive__off"]["estimate"]), ("infra_failed", None))
        self.assertEqual(rows[f"{CN}__search_direct__think"]["arm_status"], "invalid_output")
        self.assertEqual((rows[f"{TW}__search_direct__off"]["arm_status"], rows[f"{TW}__search_direct__off"]["attempts"]), ("ok", 2))
        self.assertIsNotNone(rows[f"{CN}__agent__think"]["estimate"])   # 裁判第一次不合法，第二次合法
        fin = self.state(f"{TW}__agent__off")["final"]["text"]
        self.assertTrue(fin.startswith("Estimate: "), fin[:80])   # 终稿模型没答上：代码的默认文字
        self.assertIsNotNone(rows[f"{TW}__agent__off"]["estimate"])
        self.assertEqual((rows[f"{TW}__agent__think"]["outcome"], rows[f"{TW}__agent__think"]["estimate"]), ("crashed", None))

    def test_score_without_official_values(self):
        rows, agg = self.unscored["configs"], self.unscored["summary"]
        self.assertEqual(len(rows), 12)
        self.assertTrue(all(not r["scored"] and "pct_err" not in r and "covered_80" not in r for r in rows))
        self.assertEqual(sum(r["estimate"] is not None for r in rows), 8)
        self.assertEqual([(a["arm"], a["thinking"]) for a in agg], [(a, m) for a in RT.ARMS for m in RT.MODES])
        for a in agg:
            self.assertEqual((a["n"], a["n_scored"], a["median_abs_pct_err"], a["within_10pct"]), (2, 0, None, 0))
            self.assertEqual(a["covered_80"], "n/a (no official value yet)")
        self.assertEqual(self.unscored["official"], {CN: None, TW: None})
        self.assertEqual(self.unscored_md.count("还没登记"), 2)
        self.assertEqual(self.unscored_md.count("\n| fc_"), 12 + 2)

    def test_score_with_fabricated_official_values(self):
        rows, agg = {r["config"]: r for r in self.scored["configs"]}, {(a["arm"], a["thinking"]): a for a in self.scored["summary"]}
        for r in rows.values():
            self.assertTrue(r["scored"])
            if r["estimate"] is not None:
                self.assertAlmostEqual(r["pct_err"], r["estimate"] / FABRICATED[r["qid"]]["value"] - 1, places=9)
                self.assertIn("abs_log10_err", r)
                self.assertEqual("covered_80" in r, r["arm"] == "agent")
        self.assertAlmostEqual(rows[f"{TW}__search_direct__think"]["pct_err"], 640000 / 650000 - 1, places=9)
        self.assertAlmostEqual(rows[f"{CN}__naive__think"]["pct_err"], 5.8e12 / 5.9e12 - 1, places=9)
        self.assertAlmostEqual(rows[f"{CN}__search_direct__off"]["pct_err"], 5.85e12 / 5.9e12 - 1, places=9)
        nv = agg[("naive", "off")]   # 两题都没出数：中位误差 inf
        self.assertEqual((nv["n"], nv["n_estimates"], nv["n_scored"], nv["median_abs_pct_err"]), (2, 0, 2, float("inf")))
        self.assertEqual(nv["failures"], [f"{CN}: done / invalid_output", f"{TW}: infra_failed"])
        sd = agg[("search_direct", "think")]   # 一题没出数：两个数的中位数是 inf 和误差的平均，也是 inf
        self.assertEqual((sd["n_estimates"], sd["median_abs_pct_err"], sd["failures"]),
                         (1, float("inf"), [f"{CN}: done / invalid_output"]))
        sd = agg[("search_direct", "off")]
        self.assertAlmostEqual(sd["median_abs_pct_err"], (abs(5.85e12 / 5.9e12 - 1) + abs(640000 / 650000 - 1)) / 2, places=9)
        self.assertEqual((sd["within_10pct"], sd["within_5pct"], sd["covered_80"]), (2, 2, "n/a (no interval)"))
        ag = agg[("agent", "off")]
        self.assertEqual((ag["n_estimates"], ag["covered_80"].split("/")[1]), (2, "2"))
        self.assertEqual(agg[("agent", "think")]["failures"], [f"{TW}: crashed"])
        self.assertTrue(all(isinstance(a["usd"], float) for a in agg.values()))
        self.assertEqual(self.scored_md.count("还没登记"), 0)
        self.assertIn("| inf |", self.scored_md)
        saved = json.loads((self.tmp / "test4" / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["official"][TW], {"value": 650000})
        self.assertIsNone(next(a for a in saved["summary"] if (a["arm"], a["thinking"]) == ("naive", "off"))["median_abs_pct_err"])


@unittest.skipUnless(HAVE_DEPS, "langgraph / statsforecast not installed (use .venv)")
class TestRound(unittest.TestCase):
    def test_new_round_leaves_the_previous_round_alone(self):
        """--round：同一批 agent 配置改完代码再测一轮，结果写进新目录，上一轮的状态和 agent 结果逐字节不变。"""
        from tests import fake_test4 as W
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        cs = [c for c in RT.configs() if c["arm"] == "agent"]
        kw = dict(now=lambda: W.NOW, sleep=lambda s: None, log=lambda s: None, tz=W.LOCAL_TZ)
        with W.fake_world(tmp / "agent") as (net, guard):
            net.script = {k: list(v) for k, v in SCRIPT.items()}
            first = RT.Runner(root=tmp / "test4", on_start=lambda c: setattr(net, "cid", c["cid"]), **kw)
            self.assertEqual(len(first.run(cs)["ran"]), 4)
            before = {p: p.read_bytes() for p in (tmp / "agent").rglob("*") if p.is_file()}
            before.update({p: p.read_bytes() for p in (tmp / "test4").rglob("*") if p.is_file()})
            net.script = {k: list(v) for k, v in SCRIPT.items()}
            second = RT.Runner(root=tmp / "test4" / "rounds" / "r2", on_start=lambda c: setattr(net, "cid", c["cid"]),
                               round_name="r2", **kw)
            res = second.run(cs)
            dirs = [second.agent_dir(c) for c in cs[:2]]
        self.assertEqual(len(res["ran"]), 4)                                  # 上一轮跑过，新一轮照样跑
        self.assertEqual({p: p.read_bytes() for p in before}, before)       # 上一轮的文件一个字节都没变
        self.assertEqual(dirs, [tmp / "agent" / CN / "test4_r2", tmp / "agent" / CN / "test4_think_r2"])
        self.assertTrue((tmp / "agent" / CN / "test4_r2" / "state.json").exists())
        self.assertEqual(second.status(cs[0])["outcome"], "done")
        self.assertEqual(guard.attempts, [])
        with mock.patch("sys.stderr"), self.assertRaises(SystemExit):
            RT.main(["--plan", "--round", "R-2"])                         # 轮次名只许小写字母和数字（它会进目录名和 tag）


class TestStops(unittest.TestCase):
    def test_balance_in_search_direct_stops_the_batch(self):
        """search_direct 撞上 402：DirectClient 报 TransportError（http_402），runner 记 stopped、后面的配置不跑。"""
        from tests import fake_test4 as W
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        cs = [c for c in RT.configs() if c["arm"] == "search_direct"][:2]
        with W.fake_world(tmp / "agent") as (net, guard):
            def resp_402(req, timeout):
                import io
                import urllib.error
                raise urllib.error.HTTPError(req.full_url, 402, "Payment Required", {}, io.BytesIO(b""))
            with mock.patch("triangulate.llm.urlopen_no_redirect", resp_402):
                r = RT.Runner(root=tmp / "test4", now=lambda: W.NOW, sleep=lambda s: None, log=lambda s: None, tz=W.LOCAL_TZ)
                res = r.run(cs)
        self.assertEqual(res["ran"], [cs[0]["cid"]])
        self.assertIn("http_402", res["stopped"])
        self.assertEqual(r.status(cs[0])["outcome"], "stopped")
        self.assertEqual(r.status(cs[1]), {})
        self.assertEqual(guard.attempts, [])

    def test_refuses_when_real_use_would_be_off(self):
        """注入的时区和本机日期不一致（as_of 不是 agent 眼里的今天）：agent 配置不开跑、不留状态（脚本的错，不算结果）。"""
        from tests import fake_test4 as W
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        c = next(c for c in RT.configs() if c["arm"] == "agent")
        with W.fake_world(tmp / "agent") as (net, guard):
            r = RT.Runner(root=tmp / "test4", now=lambda: W.NOW - timedelta(days=1), sleep=lambda s: None, log=lambda s: None,
                          tz=W.LOCAL_TZ)
            with self.assertRaises(SystemExit):
                r.run_one(c)
        self.assertEqual(r.status(c), {})


if __name__ == "__main__":
    unittest.main()

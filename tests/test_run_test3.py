"""留出测试 3（probes/run_test3.py）：题库登记、思考开关对三个臂都生效、高峰门、24 个配置的假数据端到端。
假数据世界在 tests/fake_test3.py：真实的 LLM.json_call / Searcher.search 和 urllib 请求对象，HTTP 换成假的 DeepSeek，取页换成假页，
联网入口（socket）全部换成抛错并记录。不调模型、不联网、不读 key 文件，结果写临时目录（不写 results/、data/raw/）。"""
import importlib.util
import json
import shutil
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
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
_spec = importlib.util.spec_from_file_location("run_test3", ROOT / "probes" / "run_test3.py")
RT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RT)
FINAL_FOUR = ["fc_cn_retail_2026_04", "fc_us_retail_2026_06", "fc_uk_insolv_2026_08", "fc_nz_exports_2026_03"]
SAT = datetime(2026, 10, 24, 3, 0, tzinfo=timezone.utc)    # 周六（北京 11:00）：不是高峰
FRI_PEAK = datetime(2026, 10, 23, 3, 0, tzinfo=timezone.utc)   # 周五北京 11:00：高峰
FRI_LUNCH = datetime(2026, 10, 23, 4, 30, tzinfo=timezone.utc)  # 周五北京 12:30：离 14:00 只剩 1.5 小时


class TestBank(unittest.TestCase):
    def test_final_four_registered(self):
        qs = RT.questions()
        self.assertEqual([q["id"] for q in qs], FINAL_FOUR)
        for q in qs:
            self.assertEqual(q["set"], "test3")
            self.assertFalse(q["strict"])
            self.assertIn(q["answer_value"], q["leak_values"])
            gap = (date.fromisoformat(q["released"]) - date.fromisoformat(q["as_of"])).days
            self.assertTrue(28 <= gap <= 30, (q["id"], gap))
            self.assertTrue(q["question"].startswith(f"Assume today is {q['as_of']}. You know nothing published after this date. "))
            self.assertNotIn(str(q["answer_value"]), q["question"])
        uk = next(q for q in qs if q["id"] == "fc_uk_insolv_2026_08")
        self.assertEqual(uk["leak_values"], [1946, 1934, 1431, 1882, 1953, 1420])   # 复查改过：去掉了三位数的分项

    def test_forecast_run_skips_test3(self):
        """python -m triangulate forecast 不跑 test3（只由 run_test3.py 跑）：别的题都当作已有回复时，一个调用都不发。"""
        def raw(arm, qid):
            return Path(__file__) if not qid.startswith(tuple(FINAL_FOUR)) else Path("does/not/exist.json")
        with mock.patch.object(forecast, "_raw", raw), mock.patch.object(forecast, "LLM", side_effect=AssertionError("no calls")):
            self.assertIsNone(forecast.run())


class TestThinkingSwitch(unittest.TestCase):
    def test_shared_dict_and_restore(self):
        from triangulate import llm
        from triangulate.agent import run as agent_run
        self.assertIs(llm.THINKING, config.THINKING)
        self.assertIs(agent_run.THINKING, config.THINKING)
        before = dict(config.THINKING)
        with RT.thinking({"naive": "high"}):
            self.assertEqual(llm.THINKING, {"naive": "high"})
        self.assertEqual(config.THINKING, before)

    def test_baseline_requests(self):
        """基线臂的角色名就是 arm 名：开思考时请求体 thinking enabled + reasoning_effort，max_tokens 多 THINKING_EXTRA_TOKENS。"""
        from tests import fake_test3 as W
        from triangulate import llm
        from triangulate.arms import run_naive, run_structured
        q = RT.questions()[0]
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        with W.fake_world(tmp / "agent") as (net, guard):
            for mode in ("off", "think"):
                for arm, fn in (("naive", run_naive), ("structured", run_structured)):
                    net.requests.clear()
                    with RT.thinking(RT.thinking_for({"arm": arm, "mode": mode})):
                        rec = fn(llm.LLM(calls_path=tmp / f"{arm}_{mode}.jsonl"), q)
                    self.assertEqual(rec["attempts"][-1]["problems"], [], (arm, mode))
                    (_, role, kind, effort, mt), = net.requests
                    base = config.MAX_TOKENS[arm]
                    if mode == "think":
                        self.assertEqual((role, kind, effort, mt), (arm, "enabled", "high", base + config.THINKING_EXTRA_TOKENS))
                    else:
                        self.assertEqual((role, kind, effort, mt), (arm, "disabled", None, base))
            self.assertEqual(guard.attempts, [])


class TestPeakGate(unittest.TestCase):
    def test_windows(self):
        self.assertEqual(RT.offpeak_left(FRI_PEAK), timedelta(0))
        self.assertEqual(RT.offpeak_left(FRI_LUNCH), timedelta(hours=1, minutes=30))
        self.assertEqual(RT.offpeak_left(SAT), timedelta(days=1, hours=22))   # 到周一北京 9:00
        need = RT.need_for(RT.configs())
        self.assertEqual(need, timedelta(seconds=RT.SAFETY * 4 * sum(RT.EST_S.values())))
        self.assertEqual(RT.next_start(FRI_PEAK, need), datetime(2026, 10, 23, 10, 0, tzinfo=timezone.utc))   # 北京 18:00
        self.assertEqual(RT.next_start(FRI_LUNCH, need), datetime(2026, 10, 23, 10, 0, tzinfo=timezone.utc))
        self.assertEqual(RT.next_start(SAT, need), SAT)

    def test_refuses_or_waits(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        ran = []
        r = RT.Runner(root=tmp, now=lambda: FRI_PEAK, sleep=lambda s: None, log=lambda s: None)
        r.run_one = lambda c, rerun_reason="": ran.append(c["cid"]) or {"usd": 0.0, "outcome": "done"}
        self.assertEqual(r.run(RT.configs()), {"ran": [], "stopped": "peak"})
        self.assertEqual(ran, [])
        log = [json.loads(x) for x in (tmp / "run.log").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(log[-1]["event"], "refused")
        self.assertIn("peak hours now", log[-1]["reason"])
        clock = {"t": FRI_LUNCH}   # --wait：睡到北京 18:00 再跑
        slept = []

        def sleep(s):
            slept.append(s)
            clock["t"] = clock["t"] + timedelta(seconds=s)
        r = RT.Runner(root=tmp, now=lambda: clock["t"], sleep=sleep, wait=True, log=lambda s: None)
        r.run_one = lambda c, rerun_reason="": ran.append(c["cid"]) or {"usd": 0.0, "outcome": "done"}
        self.assertEqual(r.run(RT.configs())["stopped"], None)   # 全部 24 个要约 2.6 小时，午间窗口不够
        self.assertEqual(slept, [timedelta(hours=5, minutes=30).total_seconds()])
        self.assertEqual(len(ran), 24)
        self.assertEqual([x["event"] for x in map(json.loads, (tmp / "run.log").read_text(encoding="utf-8").splitlines())
                          if x["event"] == "waiting"], ["waiting"])


# 故意坏掉的回复：(配置, 角色前缀) -> 依次用的回复
SCRIPT = {
    ("fc_uk_insolv_2026_08__naive__off", "naive"): ["BAD_JSON", "BAD_JSON"],          # 两次都不合法：没出数
    ("fc_cn_retail_2026_04__naive__think", "naive"): ["BAD_JSON"],                    # 第二次（带错误重试）合法
    ("fc_us_retail_2026_06__structured__think", "structured"): ["TRUNCATED", "TRUNCATED"],   # 两次都截断：没出数
    ("fc_nz_exports_2026_03__structured__off", "structured"): ["HTTP500"] * 3,        # 传输失败：基础设施故障
    ("fc_nz_exports_2026_03__agent__think", "judge"): ["BAD_JSON"],                   # 裁判第一次不合法，ask 的第二次合法
    ("fc_uk_insolv_2026_08__agent__off", "unit_check:m2:1"): ["BAD_JSON", "BAD_JSON"],   # 单位核对的第 1 个核对模型没答上
    ("fc_cn_retail_2026_04__agent__think", "final"): ["BAD_JSON", "BAD_JSON"],        # 终稿不合法：用代码的默认文字
    ("fc_us_retail_2026_06__agent__think", "plan"): ["CRASH"],                        # 意外异常：这个配置记为崩溃
}


@unittest.skipUnless(HAVE_DEPS, "langgraph / statsforecast not installed (use .venv)")
class TestFakeEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests import fake_test3 as W
        cls.W = W
        cls.tmp = Path(tempfile.mkdtemp())
        cls.agent_res = cls.tmp / "agent"
        cls.real_out_existed = RT.OUT.exists()
        cls.raw_dirs_before = {p.name for p in (ROOT / "data" / "raw" / "agent").glob("*")} if (ROOT / "data" / "raw" / "agent").exists() else set()
        with W.fake_world(cls.agent_res) as (net, guard):
            net.script = {k: list(v) for k, v in SCRIPT.items()}
            cls.net, cls.guard = net, guard
            cls.runner = RT.Runner(root=cls.tmp / "test3", now=lambda: SAT, sleep=lambda s: None, log=lambda s: None,
                                   on_start=lambda c: setattr(net, "cid", c["cid"]))
            cls.res = cls.runner.run(RT.configs())
            cls.again = cls.runner.run(RT.configs())
            cls.scored = RT.score(cls.runner)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def state(self, cid):
        qid, _, mode = cid.split("__")
        return json.loads((self.agent_res / qid / RT.AGENT_TAG[mode] / "state.json").read_text(encoding="utf-8"))

    def test_every_configuration_ends(self):
        self.assertEqual(len(self.res["ran"]), 24)
        self.assertIsNone(self.res["stopped"])
        outcomes = {c["cid"]: self.runner.status(c)["outcome"] for c in RT.configs()}
        self.assertEqual(outcomes.pop("fc_us_retail_2026_06__agent__think"), "crashed")
        self.assertEqual(outcomes.pop("fc_nz_exports_2026_03__structured__off"), "infra_failed")
        self.assertEqual(set(outcomes.values()), {"done"})
        st = self.runner.status({"cid": "fc_us_retail_2026_06__agent__think"})
        self.assertIn("RuntimeError: fake crash", st["error"])
        self.assertEqual(self.again, {"ran": [], "stopped": None})   # 一个配置只跑一次

    def test_no_network_and_no_real_files(self):
        self.assertEqual(self.guard.attempts, [])
        self.assertEqual(self.net.other, [])
        self.assertEqual(RT.OUT.exists(), self.real_out_existed)
        after = {p.name for p in (ROOT / "data" / "raw" / "agent").glob("*")} if (ROOT / "data" / "raw" / "agent").exists() else set()
        self.assertEqual(after, self.raw_dirs_before)
        self.assertTrue(self.net.searches)

    def test_thinking_flags_per_configuration(self):
        seen = {}
        for cid, role, kind, effort, mt in self.net.requests:
            arm, mode = cid.split("__")[1:]
            base = config.thinking_role(role)
            want = RT.THINKING_ON[arm].get(base) if mode == "think" else None
            self.assertEqual((kind, effort), ("enabled" if want else "disabled", want), (cid, role))
            # v2.13d：DeepSeek 的裁判 / 修正 / 抽取用模型自己的默认上限（providers.role_max_tokens）
            self.assertEqual(mt, role_max_tokens(config.MODEL, base, config.MAX_TOKENS[base])
                             + (config.THINKING_EXTRA_TOKENS if want else 0), (cid, role))
            seen.setdefault((arm, mode), set()).add(base)
        self.assertTrue({"plan", "extract", "judge", "audit", "unit_check", "unit_arbiter", "final"} <= seen[("agent", "off")])
        self.assertTrue({"plan", "judge", "audit", "unit_arbiter"} <= seen[("agent", "think")])
        for cid in ("fc_uk_insolv_2026_08__agent__off", "fc_cn_retail_2026_04__agent__think"):
            got = (self.state(cid)["settings"]).get("thinking")
            self.assertEqual(got and got["by_role"], RT.THINKING_ON["agent"] if cid.endswith("think") else None)

    def test_new_operators_exercised(self):
        paths = {}
        for c in RT.configs():
            if c["arm"] != "agent" or c["cid"] == "fc_us_retail_2026_06__agent__think":
                continue
            ms = {m["method"]: m for m in self.state(c["cid"])["compute"]["methods"]}
            self.assertIsNotNone(ms["series_auto"].get("estimate"), c["cid"])
            paths[c["cid"]] = ms["series_auto"]["series_auto"]["path"]
            if c["qid"] == "fc_uk_insolv_2026_08":
                pp = ms["partial_period"]
                self.assertAlmostEqual(pp["estimate"], 905 * (2048 + 1933) / (960 + 879), places=6)
        self.assertEqual(paths["fc_us_retail_2026_06__agent__off"], "models")
        self.assertEqual(paths["fc_nz_exports_2026_03__agent__off"], "models")
        self.assertEqual(paths["fc_nz_exports_2026_03__agent__think"], "models")
        for cid in ("fc_cn_retail_2026_04__agent__off", "fc_uk_insolv_2026_08__agent__off", "fc_uk_insolv_2026_08__agent__think"):
            self.assertEqual(paths[cid], "yoy", cid)

    def test_leak_page_voided(self):
        st = self.state("fc_cn_retail_2026_04__agent__off")
        pages = [p for r in st["results"] for p in r.get("pages") or [] if "2026-04-preview" in p["url"]]
        self.assertTrue(pages)
        self.assertTrue(all(p["status_detail"] == "excluded: leak sentinel hit" for p in pages))
        self.assertFalse([p for p in st["points"] if "2026-04-preview" in p["source_url"]])

    def test_malformed_replies_recorded(self):
        rows = {r["config"]: r for r in self.scored["configs"]}
        self.assertEqual(rows["fc_uk_insolv_2026_08__naive__off"]["arm_status"], "invalid_output")
        self.assertIsNone(rows["fc_uk_insolv_2026_08__naive__off"]["estimate"])
        self.assertEqual((rows["fc_cn_retail_2026_04__naive__think"]["arm_status"], rows["fc_cn_retail_2026_04__naive__think"]["attempts"]),
                         ("ok", 2))
        self.assertIsNone(rows["fc_us_retail_2026_06__structured__think"]["estimate"])
        self.assertEqual(rows["fc_nz_exports_2026_03__structured__off"]["outcome"], "infra_failed")
        self.assertIsNone(rows["fc_us_retail_2026_06__agent__think"]["estimate"])
        self.assertEqual(rows["fc_us_retail_2026_06__agent__think"]["outcome"], "crashed")
        fin = self.state("fc_cn_retail_2026_04__agent__think")["final"]["text"]
        self.assertTrue(fin.startswith("Estimate: "), fin[:80])   # 终稿模型没答上：代码的默认文字
        uc = [x for j in self.state("fc_uk_insolv_2026_08__agent__off")["judge_rounds"] for u in j.get("unit_reviews") or []
              for m in u["methods"] for x in m["checkers"]]
        self.assertTrue(any("error" in x for x in uc))
        self.assertIsNotNone(rows["fc_nz_exports_2026_03__agent__think"]["estimate"])

    def test_score_table(self):
        rows, agg = self.scored["configs"], self.scored["summary"]
        self.assertEqual(len(rows), 24)
        self.assertEqual([(a["arm"], a["thinking"]) for a in agg],
                         [(a, m) for a in ("naive", "structured_no_retrieval", "agent") for m in ("off", "think")])
        for r in rows:
            if r["estimate"] is not None:
                self.assertIn("pct_err", r)
                self.assertIn("abs_log10_err", r)
                if r["arm"] != "naive":
                    self.assertIn("covered_80", r)
        a = next(x for x in agg if (x["arm"], x["thinking"]) == ("agent", "think"))
        self.assertEqual((a["n"], a["n_estimates"]), (4, 3))
        self.assertEqual(a["failures"], ["fc_us_retail_2026_06: crashed"])
        self.assertTrue(all(isinstance(x["usd"], float) for x in agg))
        md = (self.tmp / "test3" / "summary.md").read_text(encoding="utf-8")
        self.assertEqual(md.count("\n| fc_"), 24 + 4)   # 24 个配置 + 4 行去年同月参照
        self.assertTrue((self.tmp / "test3" / "summary.json").exists())


@unittest.skipUnless(HAVE_DEPS, "langgraph / statsforecast not installed (use .venv)")
class TestStopsOnBalance(unittest.TestCase):
    def test_balance_inside_agent_stops_the_batch(self):
        """agent 里的搜索撞上余额不足（402）：agent 照常存盘（预算中止），这个配置记 stopped，后面的配置不跑。"""
        from tests import fake_test3 as W
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        cs = [c for c in RT.configs() if c["arm"] == "agent"][:2]
        with W.fake_world(tmp / "agent") as (net, guard):
            net.script = {(cs[0]["cid"], "search"): ["HTTP402"] * 10}
            r = RT.Runner(root=tmp / "test3", now=lambda: SAT, sleep=lambda s: None, log=lambda s: None,
                          on_start=lambda c: setattr(net, "cid", c["cid"]))
            res = r.run(cs)
        self.assertEqual(res["ran"], [cs[0]["cid"]])
        self.assertIn("insufficient balance", res["stopped"].lower())
        self.assertEqual(r.status(cs[0])["outcome"], "stopped")
        self.assertEqual(r.status(cs[1]), {})
        self.assertEqual(guard.attempts, [])


if __name__ == "__main__":
    unittest.main()

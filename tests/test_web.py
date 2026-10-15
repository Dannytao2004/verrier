"""网页层：假设占比、回测表、结果页 JSON、API 路由和运行登记（假模型、假搜索、假网页；不联网、不调模型）。"""
import json
import math
import shutil
import tempfile
import threading
import time
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

try:
    import fastapi  # noqa: F401
    import langgraph  # noqa: F401
    HAVE_WEB = True
except ImportError:
    HAVE_WEB = False

Z = 1.2815515655446004


def _formula_method(mid, inputs, estimate=100.0):
    """inputs: [(kind, p10, p90)]"""
    det = [{"name": f"x{i}", "id": f"{'a' if k == 'assumption' else 'p'}{i}", "kind": k, "p10": lo, "p90": hi, "unit": "u"}
           for i, (k, lo, hi) in enumerate(inputs, start=1)]
    return {"id": mid, "method": "formula_mc", "estimate": estimate, "inputs_detail": det}


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestAssumptionShare(unittest.TestCase):
    def test_sigma_ln(self):
        from triangulate.web.results import sigma_ln
        self.assertAlmostEqual(sigma_ln(1.0, math.exp(2 * Z)), 1.0)
        self.assertEqual(sigma_ln(5.0, 5.0), 0.0)        # 常数
        self.assertEqual(sigma_ln(None, 3.0), 0.0)
        self.assertEqual(sigma_ln(-1.0, 3.0), 0.0)

    def test_one_point_one_assumption(self):
        from triangulate.web.results import method_assumption_share
        m = _formula_method("m1", [("point", 100 / 1.2, 120.0), ("assumption", 0.5, 2.0)])
        va, vp = (math.log(4) / (2 * Z)) ** 2, (math.log(1.44) / (2 * Z)) ** 2
        self.assertAlmostEqual(method_assumption_share(m)["share"], va / (va + vp))

    def test_constants_ignored_and_series_zero(self):
        from triangulate.web.results import method_assumption_share
        m = _formula_method("m1", [("point", 1.0, 2.0), ("constant", 30.0, 30.0)])
        self.assertEqual(method_assumption_share(m)["share"], 0.0)
        self.assertEqual(method_assumption_share({"method": "series_naive", "estimate": 5})["share"], 0.0)
        only_a = _formula_method("m2", [("assumption", 1.0, 2.0), ("constant", 7.0, 7.0)])
        self.assertEqual(method_assumption_share(only_a)["share"], 1.0)

    def test_overall_is_weight_averaged_over_computed_methods(self):
        from triangulate.web.results import assumption_share
        m1 = _formula_method("m1", [("point", 1.0, 2.0), ("assumption", 1.0, 2.0)])   # 同宽：0.5
        m2 = {"id": "m2", "method": "series_naive", "estimate": 10.0}                  # 0
        m3 = _formula_method("m3", [("assumption", 1.0, 9.0), ("point", 1.0, 1.1)], estimate=None)  # 没算出：不计
        out = assumption_share({"methods": [m1, m2, m3], "result": {"weights": {"m1": 0.75, "m2": 0.25}}})
        self.assertAlmostEqual(out["per_method"]["m1"]["share"], 0.5)
        self.assertAlmostEqual(out["overall"], 0.75 * 0.5)
        self.assertNotIn("m3", out["per_method"])
        self.assertFalse(out["warning"])
        heavy = _formula_method("m1", [("point", 1.0, 1.44), ("assumption", 1.0, 4.0)])
        self.assertTrue(assumption_share({"methods": [heavy], "result": {"weights": {"m1": 1.0}}})["warning"])

    def test_no_estimate(self):
        from triangulate.web.results import assumption_share
        out = assumption_share({"methods": [], "result": {"weights": {}}})
        self.assertIsNone(out["overall"])
        self.assertFalse(out["warning"])


def _state(qid="ask_x", with_audit=True):
    """一个小的合成 state：一个 formula_mc（点 + 假设）、一个 series_naive、一个被输入核对排除的方法、一轮修正。"""
    pts = [{"id": "p1", "direction_id": "d1", "name": "widgets 2025", "value": 1000.0, "unit": "widgets", "period_start": "2025-06-01",
            "period_end": "2025-06-30", "source_url": "https://a.org/x", "via": "snapshot", "snapshot_ts": "20260601000000",
            "page_date": "2026-06-01", "quote": "June 2025: 1,000 widgets", "keep": True},
           {"id": "p2", "direction_id": "d1", "name": "widgets 2024", "value": 900.0, "unit": "widgets", "period_start": "2024-06-01",
            "period_end": "2024-06-30", "source_url": "https://a.org/y", "via": "snapshot", "snapshot_ts": "20260601000000",
            "quote": "June 2024: 900 widgets", "keep": False, "judge_reason": "duplicate"}]
    a1 = {"id": "a1", "name": "growth factor", "unit": "ratio", "value": 1.0, "low": 0.9, "high": 1.1, "is_pct": False,
          "p10_used": 0.7, "p90_used": 1.4, "widened_by_floor": True, "rationale": "r", "applies_when": "w", "falsified_by": "f",
          "used_by": ["m1"]}
    m1 = {"id": "m1", "label": "m1", "method": "formula_mc", "estimate": 1000.0, "used_ids": ["p1"], "used_assumptions": ["a1"],
          "params": {"formula": "p1 * a1", "inputs": {"p1": {"id": "p1", "role": "last year's level"},
                                                      "a1": {"id": "a1", "role": "change factor"}}},
          "inputs_detail": [{"name": "p1", "id": "p1", "kind": "point", "p10": 1000 / 1.2, "p90": 1200.0, "unit": "widgets"},
                            {"name": "a1", "id": "a1", "kind": "assumption", "p10": 0.7, "p90": 1.4, "unit": "ratio"}],
          "mc": {"p10": 700.0, "p90": 1400.0}, "notes": []}
    m2 = {"id": "m2", "label": "x", "method": "series_naive", "estimate": 1000.0, "used_ids": ["p1"],
          "params": {"target_history": ["p1"], "k": 1}, "target_series": {"2025": 1000.0}, "backtest": [], "notes": []}
    raw_methods = [{"id": "m1", "method": "formula_mc", "params": m1["params"]}, {"id": "x", "method": "series_naive", "params": m2["params"]},
                   {"id": "bad", "method": "formula_mc", "params": {"formula": "p2 * a1", "inputs": {"p2": {"id": "p2", "role": "r"}}}}]
    jr = {"round": 1, "methods": raw_methods, "repair": {"errors": ["method bad: input audit: p2 mismatch"], "errors_after": [],
                                                         "previous_methods": raw_methods[:1]}}
    if with_audit:
        jr["audit_failed"] = {"2": "input audit: p2: wrong entity"}
    return {"qid": qid, "question": "How many widgets in June 2026?", "as_of": "2026-06-20", "model": "fake",
            "plan": {"target": {"what": "widgets", "unit": "widgets"}}, "directions": [{"id": "d1", "category": "own_history"}],
            "results": [{"direction_id": "d1", "pages": [{"url": "https://a.org/x", "status": "snapshot"},
                                                         {"url": "https://b.org", "status": "dropped"}],
                         "dropped_points": [{"reason": "no period"}]}],
            "points": pts, "judge_rounds": [jr],
            "compute": {"methods": [m1, m2], "methods_from_round": 1,
                        "result": {"central": 1000.0, "p10": 800.0, "p90": 1250.0, "basis": "monte_carlo",
                                   "weights": {"m1": 0.5, "m2": 0.5}, "sigma_ln": float("nan")}},
            "assumptions": {"kept": [a1], "rejected": [{"id": "a2", "name": "level 2026", "reason": "target-like"}]},
            "final": {"text": "About 1,000 widgets."}, "leakage": {"pages_total": 2, "sentinel_hits": [], "residual_risks": ["r"]},
            "budget": {"usd_total_assumed": 0.1}, "started_at": "20261015T000000Z", "wall_s": 12.0, "tag": "t"}


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestResultView(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        d = self.tmp / "ask_x" / "web_1"
        d.mkdir(parents=True)
        (d / "state.json").write_text(json.dumps(_state()), encoding="utf-8")
        (d / "ledger.md").write_text("# ledger", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_methods_inputs_evidence_and_exclusions(self):
        from triangulate.web import results as R
        v = R.load_result("ask_x", "web_1", self.tmp)
        ms = {m["id"]: m for m in v["methods"]}
        self.assertEqual(ms["m1"]["formula"], "p1 * a1")
        kinds = {i["id"]: i["evidence"]["kind"] for i in ms["m1"]["inputs"]}
        self.assertEqual(kinds, {"p1": "point", "a1": "assumption"})
        p1 = ms["m1"]["inputs"][0]
        self.assertEqual(p1["role"], "last year's level")
        self.assertEqual(p1["evidence"]["snapshot_url"], "https://web.archive.org/web/20260601000000/https://a.org/x")
        self.assertEqual(ms["m2"]["inputs"][0]["name"], "target_history")
        self.assertEqual(ms["m2"]["assumption_share"], 0.0)
        excl = [m for m in v["methods"] if m["status"] == "excluded_by_input_audit"]
        self.assertEqual(len(excl), 1)
        self.assertIn("wrong entity", excl[0]["error"])
        self.assertEqual(v["repairs"][0]["errors"], ["method bad: input audit: p2 mismatch"])
        self.assertIsNone(v["estimate"]["sigma_ln"])  # NaN -> None
        self.assertEqual(v["assumptions"][0]["p10_used"], 0.7)
        self.assertEqual(v["assumptions_rejected"][0]["reason"], "target-like")
        self.assertEqual([p["id"] for p in v["evidence"]["kept"]], ["p1"])
        self.assertEqual(v["evidence"]["kept"][0]["used_by"], ["m1", "m2"])
        self.assertEqual([p["id"] for p in v["evidence"]["discarded"]], ["p2"])
        self.assertEqual(v["evidence"]["dropped_by_code"], {"no period": 1})
        self.assertEqual(v["evidence"]["pages"]["dropped"], 1)
        self.assertIsNone(v["official"])            # 不是回测题：不显示官方值
        self.assertEqual(v["kind"], "web")
        sh = v["assumption_share"]
        self.assertGreater(sh["per_method"]["m1"]["share"], 0.5)
        self.assertAlmostEqual(sh["overall"], 0.5 * sh["per_method"]["m1"]["share"])

    def test_official_only_for_backtest_ids(self):
        from triangulate.web import results as R
        v = R.result_view(_state("fc_jp_births_2026_07"), "fc_jp_births_2026_07", "t")
        self.assertEqual(v["official"]["answer_value"], 62479)
        self.assertAlmostEqual(v["official"]["pct_err"], 1000 / 62479 - 1)
        self.assertFalse(v["official"]["covered_80"])

    def test_list_runs_and_path_checks(self):
        from triangulate.web import results as R
        rows = R.list_runs(self.tmp)
        self.assertEqual([(r["qid"], r["tag"], r["kind"]) for r in rows], [("ask_x", "web_1", "web")])
        for qid, tag in (("..", ""), ("ask_x", "../.."), ("ask_x", "a/../../b"), ("a b", "")):
            with self.assertRaises(R.NotFound):
                R.run_dir(qid, tag, self.tmp)
        with self.assertRaises(R.NotFound):
            R.load_state("ask_x", "nope", self.tmp)

    def test_every_saved_run_loads(self):
        from triangulate.web import results as R
        rows = R.list_runs()
        self.assertGreater(len(rows), 0)
        for r in rows:
            v = R.load_result(r["qid"], r["tag"])
            self.assertIn("assumption_share", v)


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestBacktestTables(unittest.TestCase):
    def test_saved_summaries(self):
        from triangulate.web import results as R
        b = R.backtests()
        self.assertEqual([(r["qid"], r["tag"]) for r in b["dev"]], R.DEV_SET)
        self.assertEqual([(r["qid"], r["tag"]) for r in b["test"]], R.TEST_SET)
        self.assertTrue(all(r["found"] for r in b["dev"] + b["test"]))
        summ = {r["id"]: r for r in json.loads((R.RES / "summary_test1.json").read_text(encoding="utf-8"))}
        jp = next(r for r in b["test"] if r["qid"] == "fc_jp_births_2026_07")
        self.assertEqual(jp["answer_value"], 62479)
        self.assertAlmostEqual(jp["estimate"], summ["fc_jp_births_2026_07"]["estimate"])
        self.assertEqual(jp["covered_80"], summ["fc_jp_births_2026_07"]["covered_80"])
        self.assertEqual(jp["naive"]["estimate"], summ["fc_jp_births_2026_07"]["arms"]["naive"]["estimate"])
        self.assertEqual(jp["last_year"]["estimate"], 63415)
        self.assertGreater(jp["share"], 0.5)        # 日本题的估计主要靠假设（births per clinic delivery）
        self.assertTrue(jp["share_warning"])
        lhr = next(r for r in b["test"] if r["qid"] == "fc_lhr_pax_2026_09")
        self.assertLess(lhr["share"], 0.5)
        tw = next(r for r in b["test"] if r["qid"] == "fc_tw_births_2026_09")
        self.assertIsNone(tw["structured"])         # 台湾题的不联网结构化 arm 没有估计

    def test_row_builder_on_synthetic_summary(self):
        from triangulate.web import results as R
        tmp = Path(tempfile.mkdtemp())
        try:
            d = tmp / "fc_jp_births_2026_07" / "t"
            d.mkdir(parents=True)
            (d / "state.json").write_text(json.dumps(_state("fc_jp_births_2026_07")), encoding="utf-8")
            summ = [{"id": "fc_jp_births_2026_07", "answer_value": 62479, "estimate": 1000.0, "pct_err": -0.98, "covered_80": False,
                     "arms": {"naive": {"estimate": 65000, "pct_err": 0.04}, "structured_no_retrieval": None}}]
            row = R.backtest_row("fc_jp_births_2026_07", "t", summ, tmp)
            self.assertEqual(row["naive"], {"estimate": 65000, "pct_err": 0.04})
            self.assertIsNone(row["structured"])
            self.assertGreater(row["share"], 0.0)
            missing = R.backtest_row("fc_jp_births_2026_07", "t", [], tmp)
            self.assertFalse(missing["found"])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


# ---------- 运行登记：真的 LangGraph 图 + 假模型 / 假搜索 / 假网页 ----------
class FakeLLM:
    model = "fake"

    def __init__(self):
        self.roles = []

    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        self.roles.append(role)
        if role == "plan":
            return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30",
                               "publisher": "X"}, "market_keywords": [],
                    "directions": [{"category": "own_history", "hypothesis": "h1", "data_to_find": "f"},
                                   {"category": "physical_flow", "hypothesis": "h2", "data_to_find": "f"},
                                   {"category": "attention", "hypothesis": "h3", "data_to_find": "f"}]}, None
        if role.startswith("extract"):
            return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                               for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
        if role.startswith("judge"):
            return {"decisions": [], "extra_directions": [],
                    "methods": [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}}]}, None
        if role == "audit":
            return {"methods": []}, None
        if role == "final":
            return {"answer": "About [[estimate]] widgets."}, None
        raise AssertionError(role)


class FakeSearcher:
    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        return {"queries": ["q"], "urls": ["https://a.org/1", "https://b.org/2"], "web_search_requests": 1}


def fake_fetch(url, as_of, qid, **kw):
    if "b.org" in url:
        return {"url": url, "status": "dropped", "reason": "no snapshot", "snapshot_ts": None, "page_date": None}
    return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
            "text": "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."}


def make_prepare(tmp: Path, gate: threading.Event | None = None):
    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P

    def prepare(q, tag=""):
        if gate is not None:
            gate.wait(10)
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = q["id"], q["question"], q["as_of"], date.fromisoformat(q["as_of"])
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history, ctx.progress = P.Budget(), [], False, None
        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        out_dir = tmp / q["id"] / tag
        out_dir.mkdir(parents=True, exist_ok=True)
        return {"q": q, "g": G.build(ctx), "cfg": {"configurable": {"thread_id": tag}}, "ctx": ctx, "out_dir": out_dir,
                "stamp": "s", "tag": tag, "leak_values": None, "ablate": False, "t0": time.time()}
    return prepare


def wait_for(client, run_id, statuses, timeout=15):
    t = time.time()
    while time.time() - t < timeout:
        r = client.get(f"/api/runs/{run_id}").json()
        if r["status"] in statuses:
            return r
        time.sleep(0.05)
    raise AssertionError(f"run {run_id} stuck in {r['status']}: {r.get('error')}")


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestApiRuns(unittest.TestCase):
    def setUp(self):
        from fastapi.testclient import TestClient

        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        from triangulate.web.app import create_app
        from triangulate.web.runs import Registry
        self.tmp = Path(tempfile.mkdtemp())
        self.patches = [mock.patch.object(P, "fetch_page", fake_fetch),
                        mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"})]
        for p in self.patches:
            p.start()
        self.gate = threading.Event()
        self.gate.set()
        self.reg = Registry(prepare=make_prepare(self.tmp, self.gate), max_active=1)
        self.c = TestClient(create_app(self.reg, res=self.tmp), base_url="http://127.0.0.1")

    def tearDown(self):
        self.gate.set()
        for r in self.reg.runs.values():   # 等后台线程收尾，再撤掉 mock
            t = time.time()
            while r.status in ("planning", "running") and time.time() - t < 10:
                time.sleep(0.05)
        for p in self.patches:
            p.stop()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_start_stops_at_approval_then_resume_with_subset(self):
        r = self.c.post("/api/runs", json={"question": "How many widgets in June 2026?", "as_of": "2026-06-20"})
        self.assertEqual(r.status_code, 200, r.text)
        rid = r.json()["id"]
        self.assertTrue(r.json()["tag"].startswith("web_"))
        st = wait_for(self.c, rid, ("awaiting_approval", "failed"))
        self.assertEqual(st["status"], "awaiting_approval", st.get("error"))
        self.assertEqual(st["target"]["what"], "widgets")
        ids = [d["id"] for d in st["directions_proposed"]]
        self.assertEqual(len(ids), 3)
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={"keep_direction_ids": ["zz"]}).status_code, 400)
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={"keep_direction_ids": []}).status_code, 400)
        keep = [ids[0], ids[2]]
        r = self.c.post(f"/api/runs/{rid}/approve", json={"keep_direction_ids": keep})
        self.assertEqual(r.status_code, 200, r.text)
        st = wait_for(self.c, rid, ("done", "failed"))
        self.assertEqual(st["status"], "done", st.get("error"))
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={}).status_code, 409)
        # 去掉的方向没有跑；保留的两个被 approve 节点重新编号 d1, d2
        self.assertEqual([d["id"] for d in st["directions"]], ["d1", "d2"])
        for d in st["directions"]:
            self.assertEqual(d["status"], "done")
            self.assertEqual(d["pages"], {"snapshot": 1, "live_dated": 0, "dropped": 1})
            self.assertEqual(d["n_points"], 3)
            self.assertEqual(d["n_kept"], 3)
        self.assertEqual({s["key"]: s["status"] for s in st["stages"]}["final"], "done")
        self.assertAlmostEqual(st["compute"]["central"], 1210.0)
        saved = json.loads((self.tmp / st["qid"] / st["tag"] / "state.json").read_text(encoding="utf-8"))
        self.assertEqual([d["hypothesis"] for d in saved["directions"]], ["h1", "h3"])
        self.assertEqual(saved["approvals"][0]["by"], "web")
        self.assertEqual(st["result"], {"qid": st["qid"], "tag": st["tag"]})
        res = self.c.get("/api/result", params=st["result"]).json()   # 网页运行写盘后，结果页也能读
        self.assertAlmostEqual(res["estimate"]["central"], 1210.0)
        self.assertIsNone(res["official"])
        self.assertEqual(self.c.get("/api/file", params={**st["result"], "name": "ledger.md"}).status_code, 200)
        self.assertEqual([x["id"] for x in self.c.get("/api/runs").json()["runs"]], [rid])

    def test_approve_all_sends_plain_approval(self):
        rid = self.c.post("/api/runs", json={"question": "How many widgets in June 2026?", "as_of": "2026-06-20"}).json()["id"]
        wait_for(self.c, rid, ("awaiting_approval",))
        self.c.post(f"/api/runs/{rid}/approve", json={})
        st = wait_for(self.c, rid, ("done", "failed"))
        self.assertEqual(st["approvals"], [{"approved": True, "by": "web"}])
        self.assertEqual(len(st["directions"]), 3)

    def test_concurrency_limit_and_cancel_at_approval(self):
        self.gate.clear()   # 第一个运行卡在 prepare 里（planning）
        r1 = self.c.post("/api/runs", json={"question": "q1", "as_of": "2026-06-20"})
        self.assertEqual(r1.status_code, 200)
        r2 = self.c.post("/api/runs", json={"question": "q2", "as_of": "2026-06-20"})
        self.assertEqual(r2.status_code, 429)
        self.assertIn("上限 1", r2.json()["detail"])
        self.gate.set()
        rid = r1.json()["id"]
        wait_for(self.c, rid, ("awaiting_approval",))
        self.assertEqual(self.c.post(f"/api/runs/{rid}/cancel").status_code, 200)
        st = wait_for(self.c, rid, ("cancelled", "failed"))
        self.assertEqual(st["status"], "cancelled")
        self.assertEqual(st["approvals"][-1]["approved"], False)
        self.assertEqual(st["directions"], [])           # 没批准：一个方向都没跑
        self.assertEqual(self.c.post(f"/api/runs/{rid}/cancel").status_code, 409)
        self.assertEqual(self.c.post("/api/runs", json={"question": "q2", "as_of": "2026-06-20"}).status_code, 200)

    def test_cancel_during_planning_ends_without_approval(self):
        # 审查发现：规划中点取消，原来会停进 awaiting_approval、占着名额，还能被批准
        self.gate.clear()
        rid = self.c.post("/api/runs", json={"question": "q1", "as_of": "2026-06-20"}).json()["id"]
        self.assertEqual(self.c.post(f"/api/runs/{rid}/cancel").status_code, 200)
        self.gate.set()
        st = wait_for(self.c, rid, ("cancelled", "failed", "awaiting_approval"))
        self.assertEqual(st["status"], "cancelled", st)
        self.assertFalse(any(a.get("approved") for a in st["approvals"]), st["approvals"])
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={}).status_code, 409)
        self.assertEqual(self.c.post("/api/runs", json={"question": "q2", "as_of": "2026-06-20"}).status_code, 200)

    def test_non_string_fields_are_400(self):
        self.assertEqual(self.c.post("/api/runs", json={"question": 123}).status_code, 400)
        self.assertEqual(self.c.post("/api/runs", json={"question": "x", "as_of": 20260101}).status_code, 400)

    def test_cancel_while_running_uses_budget_abort(self):
        from triangulate.web.runs import CANCEL_REASON, Registry
        go = threading.Event()
        base = make_prepare(self.tmp)

        class SlowSearcher(FakeSearcher):
            def search(self, *a, **k):
                go.wait(10)
                return super().search(*a, **k)

        def prepare(q, tag=""):
            h = base(q, tag)
            h["ctx"].searcher = SlowSearcher()
            return h
        reg = Registry(prepare=prepare)
        run = reg.start("How many widgets in June 2026?", "2026-06-20")
        t = time.time()
        while run.status != "awaiting_approval" and time.time() - t < 10:
            time.sleep(0.02)
        run.approve(None)
        while not any(d["status"] == "searching" for d in run.status_view()["directions"]) and time.time() - t < 10:
            time.sleep(0.02)
        run.cancel()
        go.set()
        while run.status == "running" and time.time() - t < 15:
            time.sleep(0.02)
        self.assertEqual(run.status, "cancelled", run.error)
        saved = json.loads((self.tmp / run.q["id"] / run.tag / "state.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["budget"]["aborted"], CANCEL_REASON)
        roles = run.h["ctx"].llm.roles   # 假 LLM 不走预算预扣；裁判和终稿节点自己看 budget.aborted，不再调用
        self.assertNotIn("judge:r1", roles)
        self.assertNotIn("final", roles)

    def test_failed_prepare_is_reported(self):
        from triangulate.web.runs import Registry

        def boom(q, tag=""):
            raise RuntimeError("key file not found: X (set TRIANGULATE_KEY_FILE)")
        reg = Registry(prepare=boom)
        run = reg.start("q", "2026-06-20")
        t = time.time()
        while run.status == "planning" and time.time() - t < 5:
            time.sleep(0.02)
        self.assertEqual(run.status, "failed")
        self.assertIn("key file not found", run.status_view()["error"])

    def test_input_validation_and_404(self):
        self.assertEqual(self.c.post("/api/runs", json={"question": "  "}).status_code, 400)
        self.assertEqual(self.c.post("/api/runs", json={"question": "q", "as_of": "2999-01-01"}).status_code, 400)
        self.assertEqual(self.c.get("/api/runs/nope").status_code, 404)
        self.assertEqual(self.c.post("/api/runs/nope/approve", json={}).status_code, 404)
        self.assertEqual(self.c.get("/api/result", params={"qid": "..", "tag": ""}).status_code, 404)
        self.assertEqual(self.c.get("/api/file", params={"qid": "x", "tag": "", "name": "state.json"}).status_code, 404)
        self.assertEqual(self.c.get("/api/runs", headers={"Host": "evil.example"}).status_code, 400)   # 只认本机 Host
        self.assertEqual(self.c.post("/api/runs", content=b'{"question": "q"}', headers={"Content-Type": "text/plain"}).status_code, 422)


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestApiSaved(unittest.TestCase):
    """保存的运行：用仓库里真实的结果目录（只读）。"""

    def setUp(self):
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        self.c = TestClient(create_app(), base_url="http://127.0.0.1")

    def test_pages_and_saved_run(self):
        self.assertIn("triangulate-agent", self.c.get("/").text)
        self.assertEqual(self.c.get("/static/app.js").status_code, 200)
        runs = self.c.get("/api/saved").json()["runs"]
        self.assertIn(("fc_jp_births_2026_07", "test1"), {(r["qid"], r["tag"]) for r in runs})
        v = self.c.get("/api/result", params={"qid": "fc_jp_births_2026_07", "tag": "test1"}).json()
        self.assertEqual(v["official"]["answer_value"], 62479)
        self.assertTrue(v["assumption_share"]["warning"])
        g = self.c.get("/api/file", params={"qid": "fc_jp_births_2026_07", "tag": "test1", "name": "graph.html"})
        self.assertEqual(g.status_code, 200)
        self.assertIn("text/html", g.headers["content-type"])
        bt = self.c.get("/api/backtests").json()
        self.assertEqual(len(bt["dev"]), 4)
        self.assertEqual(len(bt["test"]), 3)


if __name__ == "__main__":
    unittest.main()

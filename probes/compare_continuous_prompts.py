"""离线复核：假模型跑一遍连续值目标的图（两轮 + 第二轮修正轮 + 输入核对 + 终稿），把全部 prompt、judge_rounds、compute、final
算一个 sha256，用来比较两份代码的连续值路径是否逐字节相同。不调模型、不联网。旧代码先导出到 gitignore 的目录：
  git archive <tag> triangulate | tar -x -C probes/out/_old
用法：.venv/Scripts/python.exe probes/compare_continuous_prompts.py <代码根目录>，两份代码各跑一次再比 sha256。
"""
import hashlib, json, sys
from datetime import date
from unittest import mock
sys.path.insert(0, sys.argv[1])
from langgraph.types import Command
from triangulate.agent import graph as G, pipeline as P
ctx = object.__new__(P.Context)
ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
log, n = [], {"judge": 0}
EXTRA = [{"id": "b1", "category": "base_rates", "hypothesis": "h3", "data_to_find": "f3", "search_hints": ["q"]}]
class FakeLLM:
    model = "fake"
    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        log.append([role, system, user])
        if role == "plan":
            return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30",
                               "publisher": "X"}, "market_keywords": [],
                    "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
        if role.startswith("extract"):
            return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                               for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
        if role.startswith("judge"):
            n["judge"] += 1
            bad = [{"id": "m1", "method": "linear_fit", "params": {"target_history": ["p1"]}}]
            good = [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}}]
            ex = EXTRA if role == "judge:r1" else []
            return {"decisions": [{"id": "p2", "keep": False, "reason": "x"}] if role == "judge:r2" else [],
                    "extra_directions": ex, "methods": bad if role in ("judge:r1", "judge:r2") else good}, None
        if role == "audit":
            return {"methods": []}, None
        if role == "final":
            return {"answer": "About [[estimate]]."}, None
        raise AssertionError(role)
class FakeSearcher:
    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        return {"queries": ["q"], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}
def fake_fetch(url, as_of, qid, **kw):
    return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
            "text": "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."}
ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
with mock.patch.object(P, "fetch_page", fake_fetch), \
        mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
    g = G.build(ctx)
    cfg = {"configurable": {"thread_id": "t1"}}
    g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
    g.invoke(Command(resume={"approved": True}), cfg)
    st = g.get_state(cfg).values
out = {"roles": [x[0] for x in log], "prompts": log, "judge_rounds": st["judge_rounds"], "compute": st["compute"],
       "final": st["final"]}
blob = json.dumps(out, sort_keys=True, default=str)
print(json.dumps({"roles": out["roles"], "sha256": hashlib.sha256(blob.encode()).hexdigest(),
                  "repairs": [sorted((j.get("repair") or {}).keys()) for j in st["judge_rounds"]]}))

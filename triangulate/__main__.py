"""python -m triangulate {select|run|demo|report|forecast|agent|agent-score|serve}"""
import argparse
import json
import sys


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m triangulate")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("select", help="pick the 20 backtest questions from data/raw (deterministic)")
    r = sub.add_parser("run", help="call the model for both arms on the 20 questions, then build the report")
    r.add_argument("--force", action="store_true", help="re-run questions that already have saved replies")
    r.add_argument("--limit", type=int, default=None, help="only the first N questions (debugging)")
    d = sub.add_parser("demo", help="structured arm on the finance demo question, then build the report")
    d.add_argument("--force", action="store_true")
    sub.add_parser("report", help="offline: rebuild states, graphs and tables from saved replies")
    f = sub.add_parser("forecast", help="one-month-ahead forecast questions (naive and no-retrieval structured arms), then score")
    f.add_argument("--force", action="store_true")
    f.add_argument("--search-direct", action="store_true",
                   help="also run arm (3), DeepSeek with web search answering directly, on the unpublished (live) questions")
    g = sub.add_parser("agent", help="research agent (LangGraph): any question via --ask, or the backtest questions; "
                                     "needs .venv packages")
    g.add_argument("--ask", default=None, help="any question about a number you cannot obtain (no scoring)")
    g.add_argument("--as-of", default=None, help="date the agent stands on (YYYY-MM-DD); default today")
    g.add_argument("--id", default=None, help="result folder name for --ask (default: derived from the question)")
    g.add_argument("--question", action="append", default=[], help="backtest question id (repeatable); default: all")
    g.add_argument("--tag", default="", help="write results to results/agent/<id>/<tag>/ (keeps earlier runs)")
    g.add_argument("--auto-approve", action="store_true", help="approve the plan without asking (backtests)")
    g.add_argument("--ablate-own-history", action="store_true",
                   help="backtest ablation: no own_history directions, own earlier values excluded before the judge, "
                        "only formula_mc; results go under a tag ending in 'noown'")
    s = sub.add_parser("agent-score", help="offline: score saved agent backtest runs against official values and the other arms")
    s.add_argument("--tag", default="")
    w = sub.add_parser("serve", help="local web UI on 127.0.0.1: start runs (stops for approval), browse saved runs and "
                                     "backtests; needs .venv packages")
    w.add_argument("--port", type=int, default=8770)
    a = ap.parse_args(argv)

    if a.cmd == "serve":
        from .web.app import serve
        sys.stdout.reconfigure(encoding="utf-8")
        serve(a.port)
        return

    if a.cmd in ("agent", "agent-score"):
        from .agent import run as agent_run
        sys.stdout.reconfigure(encoding="utf-8")
        if a.cmd == "agent" and a.ask:
            import hashlib
            from datetime import date
            as_of = a.as_of or date.today().isoformat()
            qid = a.id or "ask_" + hashlib.sha1(f"{a.ask}|{as_of}".encode("utf-8")).hexdigest()[:8]
            state = agent_run.run_question({"id": qid, "question": a.ask, "as_of": as_of}, a.auto_approve, a.tag,
                                           a.ablate_own_history)
            print((state.get("final") or {}).get("text", ""))
            return
        from .forecast import FC, QUESTIONS  # 回测题库只在这里接进来；agent 代码本身不认识它
        fc = json.loads((FC / "summary.json").read_text(encoding="utf-8"))
        picked = getattr(a, "question", None)
        qs = [q for q in QUESTIONS if q["id"] in picked] if picked else QUESTIONS
        rows = (agent_run.main(qs, a.auto_approve, a.tag, fc, a.ablate_own_history) if a.cmd == "agent"
                else agent_run.score_all(QUESTIONS, a.tag, fc))
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return

    if a.cmd == "forecast":
        from .forecast import report, run
        run(force=a.force)
        if a.search_direct:
            from .forecast import run_search
            run_search(force=a.force)
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(report(), indent=1, ensure_ascii=False))
        return

    if a.cmd == "select":
        from .data import select
        print(json.dumps(select(), indent=1))
        return
    if a.cmd == "run":
        from .runner import run_backtest
        run_backtest(force=a.force, limit=a.limit)
    if a.cmd == "demo":
        from .runner import run_demo
        run_demo(force=a.force)
    from .report import build
    summary, md = build()
    sys.stdout.reconfigure(encoding="utf-8")
    print(md or json.dumps(summary.get("demo"), indent=1))
    if "stop_rule_triggered" in summary:
        print(f"stop_rule_triggered = {summary['stop_rule_triggered']}")


if __name__ == "__main__":
    main()

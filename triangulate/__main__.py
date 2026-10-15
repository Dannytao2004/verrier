"""python -m triangulate {select|run|demo|report}"""
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
    a = ap.parse_args(argv)

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

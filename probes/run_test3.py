"""留出测试 3：4 道题（forecast.py 的 set "test3"）x 3 个臂 x 思考关 / 开 = 24 个配置，每个配置只跑一次，然后打分出一张对比表。

三个臂：
- naive：直接问，不联网（arms.run_naive）；
- structured：不联网的结构化拆解，Python 算（arms.run_structured；打分表里叫 structured_no_retrieval）；
- agent：完整 agent，联网（Wayback 快照 <= as_of），agent.run.run_question(auto_approve)。
思考开关：TRIANGULATE_THINKING 的按角色档位（config.THINKING）。基线臂的角色名就是 arm 名（config.thinking_role），
本脚本每个配置在进程内设一次（config.THINKING 和 llm / agent.run 引用的是同一个 dict），跑完还原；启动时环境变量必须为空。
- 关：全部角色不开（请求和 frozen-v2.8r 逐字相同）；
- 开：naive=high；structured=high；agent 用 v2.9a 实验的设置 plan=high,judge=high,repair=high,audit=low,unit_arbiter=low
  （results/agent/*/test2_think 用的就是这一组）。
一个配置只跑一次：不因为回复不合法、没出数而重跑（用户：跑得不好也是测试结果）。「只跑一次」说的是本脚本这一层：已开跑
（有 started_at）的配置不再跑，崩溃的配置不自动重跑，--rerun 每个配置最多一次。各臂内部原有的重试照旧会再发付费请求，是冻结
协议的一部分，开关思考都一样，不改：基线「输出无效带错误重试一次」；agent 每次 JSON 调用 tries=2（规划、裁判、输入核对、终稿等）
和修正轮（graph.MAX_REPAIRS）；llm.py 传输层失败（超时、5xx、空 body）每次请求最多试 3 次。有回复的每次尝试都写进调用记录、
计入费用（基线 = 调用记录的 usd 合计；agent = 预算的 usd_total_assumed）。只有基础设施故障（网络 / API 中断、进程被杀）
可以用 --rerun <配置> --reason "<原因>" 手动重跑一次，原因和两次的结果都留在状态文件里。

高峰：DeepSeek 高峰 = 北京时间周一到周五 9:00-12:00、14:00-18:00（config.is_peak）。开跑前和每个配置开跑前都检查：
现在不是高峰，而且离下一个高峰的剩余时间 >= 预计时长 x SAFETY；不满足就拒跑（--wait 则等到下一个够长的非高峰窗口）。

结果：
- 基线：results/test3/raw/<arm>_<off|think>/<qid>.json，调用记录同目录 <qid>.calls.jsonl；
- agent：results/agent/<qid>/test3/ 和 results/agent/<qid>/test3_think/（标准位置，网页和 agent-score 照样能读）；
- 每个配置的状态：results/test3/configs/<配置>.json；运行日志（含费用）：results/test3/run.log；
- 打分：results/test3/summary.json、results/test3/summary.md。

用法（解释器 .venv/Scripts/python.exe，PYTHONIOENCODING=utf-8）：
  probes/run_test3.py --plan                     列出配置、预计时长和费用、离下一个高峰多久；不调模型
  probes/run_test3.py --run [--wait]             跑还没跑过的配置，跑完打分
  probes/run_test3.py --rerun <配置> --reason R  基础设施故障的配置重跑一次
  probes/run_test3.py --score                    只离线打分
"""
import argparse
import json
import math
import statistics
import sys
import time
import traceback
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from triangulate import config  # noqa: E402
from triangulate import llm as LLM_MOD  # noqa: E402
from triangulate.arms import check_naive, run_naive, run_structured  # noqa: E402
from triangulate.engine import evaluate_structured  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402
from triangulate.report import _clean, final_reply  # noqa: E402

SET = "test3"
OUT = config.RESULTS / "test3"
ARMS = ("naive", "structured", "agent")
MODES = ("off", "think")
AGENT_TAG = {"off": "test3", "think": "test3_think"}
THINKING_ON = {"naive": {"naive": "high"}, "structured": {"structured": "high"},
               "agent": {"plan": "high", "judge": "high", "repair": "high", "audit": "low", "unit_arbiter": "low"}}
# 每个配置的预计时长（秒）[人为约定，取已存运行的最大值往上取整]：agent 关 = test2 的 14 次 wall_s 最大 468.9；agent 开 = test2_think
# 最大 680.5；naive 关 = 2 次调用 x results/forecast/calls.jsonl 最大延迟 1.34；naive 开 = 2 x probes/out/leak_naive_thinking_calls.jsonl
# 最大 25.45；structured 关 = 2 x 8.41；structured 开没有存过的运行，按 2 x 120 秒估（未核实）
EST_S = {("naive", "off"): 10, ("naive", "think"): 60, ("structured", "off"): 30, ("structured", "think"): 240,
         ("agent", "off"): 480, ("agent", "think"): 720}
SAFETY = 1.5          # 剩余非高峰时间至少是预计时长的 1.5 倍 [人为约定]
# 预计费用（美元）[人为约定]：agent 按 Budget 的默认上限 1.0（已存 test2 / test2_think 最大 0.71 / 0.73）；基线按已存调用的量级
EST_USD = {("naive", "off"): 0.001, ("naive", "think"): 0.01, ("structured", "off"): 0.01, ("structured", "think"): 0.05,
           ("agent", "off"): 1.0, ("agent", "think"): 1.0}
SCAN_DAYS = 8         # 找非高峰窗口最多往后看 8 天（周末窗口 63 小时，一定找得到）


def questions() -> list:
    return [q for q in QUESTIONS if q.get("set") == SET]


def configs(qs=None) -> list:
    """跑的顺序：先 16 个基线（便宜、快，基础设施问题先暴露），再 8 个 agent。"""
    qs = questions() if qs is None else qs
    out = [{"qid": q["id"], "arm": a, "mode": m} for a in ("naive", "structured") for q in qs for m in MODES]
    out += [{"qid": q["id"], "arm": "agent", "mode": m} for m in MODES for q in qs]
    for c in out:
        c["cid"] = f"{c['qid']}__{c['arm']}__{c['mode']}"
    return out


def thinking_for(c: dict) -> dict:
    return dict(THINKING_ON[c["arm"]]) if c["mode"] == "think" else {}


@contextmanager
def thinking(settings: dict):
    """在进程内换掉思考档位（config.THINKING 原地改，llm.THINKING / agent.run.THINKING 是同一个对象），退出时还原。"""
    from triangulate.agent import run as agent_run
    if not (LLM_MOD.THINKING is config.THINKING and agent_run.THINKING is config.THINKING):
        raise RuntimeError("config.THINKING is not shared with llm / agent.run; cannot switch thinking in-process")
    old = dict(config.THINKING)
    config.THINKING.clear()
    config.THINKING.update(settings)
    try:
        yield
    finally:
        config.THINKING.clear()
        config.THINKING.update(old)


# ---------- 高峰 ----------
def _utc(t: datetime) -> datetime:
    return t.astimezone(timezone.utc).replace(second=0, microsecond=0)


def offpeak_windows(now: datetime, days: int = SCAN_DAYS) -> list:
    """从 now 起 days 天内的非高峰时段 [(开始, 结束)]，按分钟扫 config.is_peak。第一个时段可能从 now 开始。"""
    t, end, out, start = _utc(now), _utc(now) + timedelta(days=days), [], None
    while t < end:
        if config.is_peak(t):
            if start is not None:
                out.append((start, t))
                start = None
        elif start is None:
            start = t
        t += timedelta(minutes=1)
    if start is not None:
        out.append((start, end))
    return out


def offpeak_left(now: datetime) -> timedelta:
    """现在离下一个高峰还有多久；现在就是高峰时为 0。"""
    if config.is_peak(now):
        return timedelta(0)
    w = offpeak_windows(now)
    return timedelta(seconds=int((w[0][1] - now.astimezone(timezone.utc)).total_seconds())) if w else timedelta(0)


def next_start(now: datetime, need: timedelta):
    """最早能开跑的时刻：在一个非高峰时段里、离时段结束至少 need。找不到时 None。"""
    nu = now.astimezone(timezone.utc)
    for a, b in offpeak_windows(now):
        s = max(a, nu)
        if b - s >= need:
            return s
    return None


def need_for(cs: list) -> timedelta:
    return timedelta(seconds=SAFETY * sum(EST_S[(c["arm"], c["mode"])] for c in cs))


# ---------- 运行 ----------
def _read(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _write(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(_clean(obj), indent=1, ensure_ascii=False, default=str), encoding="utf-8")


def _usd_of_calls(p: Path) -> float:
    """调用记录里的花费合计：token 费（usd）加搜索费（usd_search_fee_assumed，只有 agent 的搜索调用有）。"""
    if not p.exists():
        return 0.0
    rs = [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    return round(sum(float(r.get("usd") or 0) + float(r.get("usd_search_fee_assumed") or 0) for r in rs), 6)


class Runner:
    """root：test3 的结果目录（测试换成临时目录）；agent 的结果目录由 agent.run.RES 决定（测试同样换掉）。
    now / sleep 可注入（测试用固定时钟）。on_start(c)：每个配置开跑前回调（测试用来给假服务换脚本）。"""

    def __init__(self, root: Path = OUT, now=None, sleep=time.sleep, wait: bool = False, log=print, llm_factory=None,
                 on_start=None):
        self.root, self.wait, self.log_print, self.sleep = Path(root), wait, log, sleep
        self.now = now or (lambda: datetime.now(timezone.utc))
        self.llm_factory = llm_factory or (lambda calls: LLM_MOD.LLM(calls_path=calls))
        self.on_start = on_start

    # 路径
    def status_path(self, c):
        return self.root / "configs" / f"{c['cid']}.json"

    def raw_dir(self, c):
        return self.root / "raw" / f"{c['arm']}_{c['mode']}"

    def agent_dir(self, c):
        from triangulate.agent import run as agent_run
        return agent_run.RES / c["qid"] / AGENT_TAG[c["mode"]]

    def status(self, c):
        return _read(self.status_path(c)) or {}

    def log(self, **rec):
        rec = {"at": self.now().astimezone(timezone.utc).isoformat(timespec="seconds"), **rec}
        self.root.mkdir(parents=True, exist_ok=True)
        with (self.root / "run.log").open("a", encoding="utf-8") as f:
            f.write(json.dumps(_clean(rec), ensure_ascii=False, default=str) + "\n")
        self.log_print(json.dumps(rec, ensure_ascii=False, default=str))

    def pending(self, cs):
        return [c for c in cs if not self.status(c).get("outcome") and not self.status(c).get("started_at")]

    # 高峰门
    def gate(self, need: timedelta, what: str) -> bool:
        now = self.now()
        left = offpeak_left(now)
        if left >= need:
            return True
        why = "peak hours now" if left == timedelta(0) else f"only {left} left before the next peak"
        if not self.wait:
            self.log(event="refused", what=what, reason=f"{why}; need {need}")
            return False
        s = next_start(now, need)
        if s is None:
            self.log(event="refused", what=what, reason=f"{why}; no off-peak window of {need} in the next {SCAN_DAYS} days")
            return False
        self.log(event="waiting", what=what, reason=why, until=s.isoformat(timespec="minutes"))
        self.sleep(max(0.0, (s - now.astimezone(timezone.utc)).total_seconds()))
        return self.gate(need, what)

    def run(self, cs) -> dict:
        if config.THINKING:
            raise SystemExit("TRIANGULATE_THINKING must be unset: this script sets thinking per configuration")
        todo = self.pending(cs)
        if not todo:
            self.log(event="nothing to run")
            return {"ran": [], "stopped": None}
        if not self.gate(need_for(todo), f"batch of {len(todo)} configurations"):
            return {"ran": [], "stopped": "peak"}
        ran, cum = [], 0.0
        for c in todo:
            if not self.gate(need_for([c]), c["cid"]):
                return {"ran": ran, "stopped": "peak"}
            st = self.run_one(c)
            ran.append(c["cid"])
            cum += st.get("usd") or 0.0
            self.log(event="cost", cid=c["cid"], usd=st.get("usd"), cumulative_usd=round(cum, 6))
            if st.get("outcome") == "stopped":   # key 被拒 / 余额不足：后面的配置都不跑
                return {"ran": ran, "stopped": st.get("error")}
        return {"ran": ran, "stopped": None}

    def run_one(self, c, rerun_reason: str = "") -> dict:
        q = next(x for x in questions() if x["id"] == c["qid"])
        prev = self.status(c)
        st = {"cid": c["cid"], "qid": c["qid"], "arm": c["arm"], "thinking": c["mode"], "thinking_by_role": thinking_for(c),
              "started_at": self.now().astimezone(timezone.utc).isoformat(timespec="seconds"), "attempts": prev.get("attempts", [])}
        if rerun_reason:
            st["attempts"] = st["attempts"] + [{k: prev.get(k) for k in ("started_at", "finished_at", "outcome", "error")}
                                               | {"rerun_reason": rerun_reason}]
        _write(self.status_path(c), st)
        self.log(event="start", cid=c["cid"], thinking=st["thinking_by_role"])
        if self.on_start is not None:
            self.on_start(c)
        t0 = time.time()
        try:
            with thinking(thinking_for(c)):
                st.update(self._agent(c, q) if c["arm"] == "agent" else self._baseline(c, q))
            st["outcome"] = "stopped" if st.get("error") else "done"
        except (LLM_MOD.KeyRejected, LLM_MOD.BalanceExhausted) as e:
            st.update(outcome="stopped", error=f"{type(e).__name__}: {e}")
        except LLM_MOD.TransportError as e:
            st.update(outcome="infra_failed", error=f"TransportError: {e}")
        except Exception as e:  # noqa: BLE001  任何崩溃都记成这个配置的结果，接着跑下一个
            st.update(outcome="crashed", error=f"{type(e).__name__}: {e}"[:500],
                      traceback=traceback.format_exc(limit=8)[-3000:])
        st["wall_s"] = round(time.time() - t0, 1)
        st["finished_at"] = self.now().astimezone(timezone.utc).isoformat(timespec="seconds")
        if st.get("usd") is None:   # 失败的配置也记已经花掉的钱
            st["usd"] = (self._agent_usd(c) if c["arm"] == "agent"
                         else _usd_of_calls(self.raw_dir(c) / f"{c['qid']}.calls.jsonl"))
        _write(self.status_path(c), st)
        self.log(event="end", cid=c["cid"], outcome=st["outcome"], wall_s=st["wall_s"], usd=st["usd"], error=st.get("error"))
        return st

    def _baseline(self, c, q) -> dict:
        d = self.raw_dir(c)
        calls = d / f"{q['id']}.calls.jsonl"
        llm = self.llm_factory(calls)
        rec = (run_naive if c["arm"] == "naive" else run_structured)(llm, q)
        rec["thinking_by_role"] = dict(config.THINKING)
        _write(d / f"{q['id']}.json", rec)
        return {"raw": str(d / f"{q['id']}.json"), "usd": _usd_of_calls(calls), "attempts_in_arm": len(rec["attempts"])}

    def _agent(self, c, q) -> dict:
        from triangulate.agent import run as agent_run
        state = agent_run.run_question(q, True, AGENT_TAG[c["mode"]])
        b = state.get("budget") or {}
        out = {"state": str(self.agent_dir(c) / "state.json"), "usd": b.get("usd_total_assumed"),
               "usd_tokens": b.get("usd_tokens"), "settings_thinking": (state.get("settings") or {}).get("thinking")}
        why = str(b.get("aborted") or state.get("aborted") or "")
        if "insufficient balance" in why.lower():   # agent 把余额不足变成预算中止、照常存盘；这里让整批停下（后面的配置也会撞上）
            out["error"] = f"BalanceExhausted (inside the agent run): {why}"[:500]
        return out

    def _agent_usd(self, c):
        p = self.agent_dir(c) / "state.json"
        st = _read(p)
        if st:
            return (st.get("budget") or {}).get("usd_total_assumed")
        return _usd_of_calls(self.agent_dir(c) / "calls.jsonl")


# ---------- 打分 ----------
def _unit_factor(state: dict, q: dict):
    """agent 钉的 unit_canonical 和登记单位不同时的换算系数（EVAL_TEST2_PLAN 的单位口径）：(系数或 None, 说明)。
    登记单位为空（计数题）时不换算。"""
    from triangulate.agent import qty as Q
    uc = ((state.get("plan") or {}).get("target") or {}).get("unit_canonical") or ""
    au = q.get("answer_unit") or ""
    if not au or not uc or uc == au:
        return 1.0, uc
    f, err = Q.convert_factor(uc, au)
    return f, (f"{uc} -> {au} x {f:g}" if f is not None else err)


def score_config(c: dict, q: dict, runner: Runner) -> dict:
    st = runner.status(c)
    ans = q["answer_value"]
    row = {"config": c["cid"], "qid": c["qid"], "arm": "structured_no_retrieval" if c["arm"] == "structured" else c["arm"],
           "thinking": c["mode"], "outcome": st.get("outcome") or ("started, not finished" if st.get("started_at") else "not run"),
           "usd": st.get("usd"), "wall_s": st.get("wall_s"), "estimate": None, "p10": None, "p90": None, "detail": ""}
    if st.get("error"):
        row["detail"] = st["error"][:200]
    if c["arm"] == "naive":
        rec = _read(runner.raw_dir(c) / f"{c['qid']}.json")
        if rec is not None:
            status, est, problems = check_naive(final_reply(rec), q["answer_unit"], strict_target=False)
            row.update(estimate=est, arm_status=status, attempts=len(rec["attempts"]))
            if problems:   # 最后一次回复本身不合法时，说明用那次尝试记下的原因（截断、不是合法 JSON）
                row["detail"] = "; ".join(rec["attempts"][-1]["problems"] or problems)[:200]
    elif c["arm"] == "structured":
        rec = _read(runner.raw_dir(c) / f"{c['qid']}.json")
        if rec is not None:
            s = evaluate_structured(final_reply(rec), q["answer_unit"], q["id"], strict_target=False, question=q["question"])
            r = s["result"]
            row.update(estimate=r.get("central"), p10=r.get("p10"), p90=r.get("p90"), attempts=len(rec["attempts"]),
                       n_valid_paths=r.get("n_valid_paths"), arm_status="ok" if r.get("central") is not None else "no valid path")
            if s["errors"]:
                row["detail"] = "; ".join(rec["attempts"][-1]["problems"] if final_reply(rec) is None else s["errors"])[:200]
    else:
        state = _read(runner.agent_dir(c) / "state.json")
        if state is not None:
            r = (state.get("compute") or {}).get("result") or {}
            f, note = _unit_factor(state, q)
            est = r.get("central")
            row.update(estimate_as_run=est, unit_note=note, basis=r.get("basis"),
                       methods=[(m.get("id"), m.get("method"), m.get("estimate")) for m in (state.get("compute") or {}).get("methods") or []])
            if est is not None and f is None:
                row.update(arm_status="unit not convertible", detail=note)
            elif est is not None:
                row.update(estimate=est * f, p10=None if r.get("p10") is None else r["p10"] * f,
                           p90=None if r.get("p90") is None else r["p90"] * f, arm_status="ok")
            else:
                row["arm_status"] = "no estimate"
                row["detail"] = row["detail"] or str(state.get("aborted") or (state.get("compute") or {}).get("error") or "")[:200]
    est = row["estimate"]
    if est is not None and est > 0:
        row.update(pct_err=est / ans - 1, abs_log10_err=abs(math.log10(est / ans)))
        if row["p10"] is not None and row["p90"] is not None:
            row["covered_80"] = row["p10"] <= ans <= row["p90"]
    return row


def _median_inf(xs):
    return statistics.median(xs) if xs else None


def aggregate(rows: list) -> list:
    """每个臂 x 思考一行。没出数的配置误差记为无穷大、计入中位数（EVAL_TEST2_PLAN 的约定）。"""
    out = []
    for arm in ("naive", "structured_no_retrieval", "agent"):
        for mode in MODES:
            rs = [r for r in rows if r["arm"] == arm and r["thinking"] == mode]
            if not rs:
                continue
            pe = [abs(r["pct_err"]) if r.get("pct_err") is not None else math.inf for r in rs]
            le = [r["abs_log10_err"] if r.get("abs_log10_err") is not None else math.inf for r in rs]
            iv = [r for r in rs if "covered_80" in r]
            out.append({"arm": arm, "thinking": mode, "n": len(rs), "n_estimates": sum(r.get("pct_err") is not None for r in rs),
                        "median_abs_pct_err": _median_inf(pe), "median_abs_log10_err": _median_inf(le),
                        "within_10pct": sum(x <= 0.10 for x in pe), "within_5pct": sum(x <= 0.05 for x in pe),
                        "covered_80": f"{sum(r['covered_80'] for r in iv)}/{len(iv)}" if iv else "n/a (no interval)",
                        "usd": round(sum(r.get("usd") or 0 for r in rs), 4),
                        "failures": [f"{r['qid']}: {r['outcome']}" + (f" / {r.get('arm_status')}" if r.get("arm_status") not in (None, "ok") else "")
                                     for r in rs if r.get("pct_err") is None]})
    return out


def _f(x, kind):
    if x is None:
        return "—"
    if isinstance(x, float) and math.isinf(x):
        return "inf"
    if kind == "pct":
        return f"{x * 100:+.1f}%"
    if kind == "apct":
        return f"{x * 100:.1f}%"
    if kind == "log":
        return f"{x:.3f}"
    if kind == "usd":
        return f"{x:.4f}"
    return f"{x:,.0f}"


def render_md(rows: list, agg: list, qs: list) -> str:
    L = ["# 留出测试 3：三臂 x 思考开关（probes/run_test3.py --score）", "",
         "误差 = 估计 / 真值 - 1；abs(log10) = |log10(估计 / 真值)|；没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂"
         "（直接问没有区间）。费用：基线 = 调用记录的 usd 合计；agent = 预算的 usd_total_assumed（含按假设单价记的搜索费）。", "",
         "## 汇总", "", "| 臂 | 思考 | 出数 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for a in agg:
        L.append(f"| {a['arm']} | {a['thinking']} | {a['n_estimates']}/{a['n']} | {_f(a['median_abs_pct_err'], 'apct')} | "
                 f"{_f(a['median_abs_log10_err'], 'log')} | {a['within_10pct']} | {a['within_5pct']} | {a['covered_80']} | "
                 f"{_f(a['usd'], 'usd')} | {'; '.join(a['failures']) or '—'} |")
    L += ["", "## 逐个配置", "", "| 题 | 臂 | 思考 | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        cov = "—" if "covered_80" not in r else ("是" if r["covered_80"] else "否")
        L.append(f"| {r['qid']} | {r['arm']} | {r['thinking']} | {r['outcome']}{' / ' + r['arm_status'] if r.get('arm_status') else ''} | "
                 f"{_f(r['estimate'], 'n')} | {_f(r.get('pct_err'), 'pct')} | {_f(r.get('abs_log10_err'), 'log')} | "
                 f"{_f(r['p10'], 'n')} | {_f(r['p90'], 'n')} | {cov} | {_f(r.get('usd'), 'usd')} | {(r.get('detail') or '').replace('|', '/')[:120]} |")
    L += ["", "## 参照（不是对照臂）：去年同月的登记值", "", "| 题 | 真值 | 去年同月 | 误差 |", "|---|---|---|---|"]
    for q in qs:
        L.append(f"| {q['id']} | {q['answer_value']:,} | {q['last_year']:,} | {_f(q['last_year'] / q['answer_value'] - 1, 'pct')} |")
    return "\n".join(L) + "\n"


def score(runner: Runner) -> dict:
    qs = questions()
    by_id = {q["id"]: q for q in qs}
    rows = [score_config(c, by_id[c["qid"]], runner) for c in configs(qs)]
    agg = aggregate(rows)
    out = {"set": SET, "configs": rows, "summary": agg}
    _write(runner.root / "summary.json", out)
    (runner.root / "summary.md").write_text(render_md(rows, agg, qs), encoding="utf-8")
    return out


def plan_text(runner: Runner) -> str:
    cs = configs()
    todo = runner.pending(cs)
    now = runner.now()
    left = offpeak_left(now)
    need = need_for(todo)
    usd = sum(EST_USD[(c["arm"], c["mode"])] for c in todo)
    lines = [f"{len(cs)} configurations, {len(todo)} not run yet; estimated time {need} (x{SAFETY} safety), "
             f"estimated cost up to ${usd:.2f}",
             f"now {now.astimezone(timezone.utc).isoformat(timespec='minutes')}; peak now: {config.is_peak(now)}; "
             f"off-peak time left: {left}"]
    s = next_start(now, need) if todo else None
    if todo:
        lines.append(f"earliest start with enough off-peak time: {s.isoformat(timespec='minutes') if s else 'none found'}")
    for c in cs:
        st = runner.status(c)
        lines.append(f"  {c['cid']:48s} thinking={thinking_for(c) or 'off'}  {st.get('outcome') or ('started' if st.get('started_at') else 'pending')}")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="test3: 4 questions x 3 arms x thinking off/on, one run each")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--plan", action="store_true")
    g.add_argument("--run", action="store_true")
    g.add_argument("--rerun", metavar="CONFIG")
    g.add_argument("--score", action="store_true")
    ap.add_argument("--wait", action="store_true", help="wait for an off-peak window that is long enough instead of refusing")
    ap.add_argument("--reason", default="", help="why --rerun is an infrastructure failure (required with --rerun)")
    a = ap.parse_args(argv)
    runner = Runner(wait=a.wait)
    if a.plan:
        print(plan_text(runner))
        return 0
    if a.score:
        print(json.dumps(score(runner)["summary"], indent=1, ensure_ascii=False, default=str))
        return 0
    if a.rerun:
        c = next((x for x in configs() if x["cid"] == a.rerun), None)
        if c is None:
            ap.error(f"unknown configuration {a.rerun}")
        st = runner.status(c)
        if not a.reason:
            ap.error("--rerun needs --reason (only infrastructure failures may be re-run, once)")
        if st.get("attempts"):
            ap.error(f"{a.rerun} was already re-run once")
        if st.get("outcome") not in ("infra_failed", "crashed", "stopped", None) or not st.get("started_at"):
            ap.error(f"{a.rerun} has outcome {st.get('outcome')!r}; only an infra failure, a crash, a stop (key / balance) or an "
                     "interrupted run may be re-run")
        if config.THINKING:
            raise SystemExit("TRIANGULATE_THINKING must be unset: this script sets thinking per configuration")
        if not runner.gate(need_for([c]), c["cid"]):
            return 2
        runner.run_one(c, rerun_reason=a.reason)
        score(runner)
        return 0
    res = runner.run(configs())
    print(json.dumps(score(runner)["summary"], indent=1, ensure_ascii=False, default=str))
    return 0 if res["stopped"] is None else 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())

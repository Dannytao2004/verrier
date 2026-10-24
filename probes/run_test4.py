"""留出测试 4（前瞻）：forecast.py 的 set "test4"（现在 2 道：中国 2026 年 1-9 月规上工业企业利润总额、台湾 2026 年 9 月来台旅客）
x 3 个臂 x 思考关 / 开 = 12 个配置，每个配置只跑一次，然后打分出一张对比表。真值公布、填进 forecast.TEST4_OFFICIAL 之前，
表里只列估计、不算误差。照 probes/run_test3.py 写（那个脚本不改）：高峰窗口、思考开关、读写和单位换算直接用它的函数。

三个臂：
- naive：直接问，不联网（arms.run_naive）；
- search_direct：直接问 + 模型自带的联网搜索（search_direct.run_search_direct，control_thinking=True）：DeepSeek Anthropic 兼容接口
  + 服务端 web_search，和 agent 的 SEARCHER 同一个地址、同一个工具；记录里有每次尝试的查询词和全部结果 URL；数字由代码用
  arms.check_naive 从最后一段文字的 JSON 取（同 naive 的单位检查）；
- agent：完整 agent，真实使用：as_of = 跑的那天、直接抓 live 页、「答案已公布」检查和提前停都照真实使用（agent.run.prepare_run
  按 checks_published 打开；本脚本开跑前再确认一次，不满足就不跑）。
思考开关同 run_test3：启动时 TRIANGULATE_THINKING 必须为空，每个配置在进程内设一次 config.THINKING，跑完还原。
- 关：全部角色不开（search_direct 显式发 thinking disabled；默认调用不带这个字段、服务端默认开思考，见 search_direct.py）；
- 开：naive=high；search_direct=high；agent 同 test3：plan=high,judge=high,repair=high,audit=low,unit_arbiter=low。
一个配置只跑一次（同 run_test3 的约定）：已开跑（有 started_at）的配置不再跑，崩溃的配置不自动重跑，--rerun 每个配置最多一次、
只给基础设施故障。各臂内部原有的重试照旧（基线「输出无效带错误重试一次」、agent 每次 JSON 调用 tries=2 和修正轮、传输层每次请求
最多 3 次），有回复的每次尝试都写进调用记录、计入费用。
题干：as_of 在每个配置开跑时取本机当地日期（forecast.with_as_of 填进 question_template），和 question 一起记进配置的状态文件。

门（每批开跑前和每个配置开跑前都查）：
1. 现在 >= 这题的首发时刻（released_at）：拒跑，答案可能已公开；
2. 按预计时长 x SAFETY 跑完会晚于首发时刻：拒跑。1、2 以后只会更不满足，--wait 也不等；
3. DeepSeek 高峰（config.is_peak），或离下一个高峰不够预计时长 x SAFETY：拒跑（--wait 则等到够长的非高峰时段）；
4. 跑完会跨过本机当地午夜：拒跑（--wait 则等）。跨过午夜 as_of 就早于「今天」，agent 之后取的页退回快照路径
   （fetch.fetch_live 的 v2.5.2 规则），不再是真实使用。
一批里有的配置被 1、2 永久拒掉时，其余配置照常（每个配置的门照查）。

结果：
- 基线：results/test4/raw/<arm>_<off|think>/<qid>.json，调用记录同目录 <qid>.calls.jsonl；
- agent：results/agent/<qid>/test4/ 和 results/agent/<qid>/test4_think/（标准位置，网页和 agent-score 照样能读）；
- 每个配置的状态：results/test4/configs/<配置>.json；运行日志（含拒跑原因、费用）：results/test4/run.log；
- 打分：results/test4/summary.json、results/test4/summary.md。

用法（解释器 .venv/Scripts/python.exe，PYTHONIOENCODING=utf-8）：
  probes/run_test4.py --plan [--question QID]                 列出配置、门的检查结果、预计时长和费用；不调模型
  probes/run_test4.py --run [--wait] [--question QID]         跑还没跑过的配置（--question 可写多次，只跑这些题），跑完打分
  probes/run_test4.py --run --config <配置> [--config ...]    只跑这几个配置（--plan 也认 --config）
  probes/run_test4.py --rerun <配置> --reason R               基础设施故障的配置重跑一次（门照查）
  probes/run_test4.py --score                                 只离线打分
"""
import argparse
import importlib.util
import json
import math
import re
import sys
import time
import traceback
from datetime import datetime, time as dtime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from triangulate import config  # noqa: E402
from triangulate import forecast as FC  # noqa: E402
from triangulate import llm as LLM_MOD  # noqa: E402
from triangulate.arms import check_naive, run_naive  # noqa: E402
from triangulate.report import _clean, final_reply  # noqa: E402
from triangulate.search_direct import DirectClient, run_search_direct  # noqa: E402

# run_test3 按文件载入（probes 不是包，也不把 probes/ 放进 sys.path）
_spec = importlib.util.spec_from_file_location("_run_test3_for_test4", HERE / "run_test3.py")
T3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T3)

SET = "test4"
OUT = config.RESULTS / "test4"
ARMS = ("naive", "search_direct", "agent")
MODES = ("off", "think")
AGENT_TAG = {"off": "test4", "think": "test4_think"}
THINKING_ON = {"naive": {"naive": "high"}, "search_direct": {"search_direct": "high"}, "agent": dict(T3.THINKING_ON["agent"])}
# 每个配置的预计时长（秒）[人为约定，取已存运行的最大值往上取整]：agent 关 = test2 的最大 wall_s 468.9（test3 最大 326.5）；
# agent 开 = test3 最大 1106.1（英国破产，思考开）；naive 同 run_test3；search_direct 关 / 开：已存的 4 次运行都是服务端默认思考
# （正式 44.3 / 45.2 秒 + 重试 2.5 / 4.0 秒，补充 36.1 / 80.3 秒），显式关 / 开思考的没有存过的运行，按 120 / 180 估（未核实）
EST_S = {("naive", "off"): 10, ("naive", "think"): 60, ("search_direct", "off"): 120, ("search_direct", "think"): 180,
         ("agent", "off"): 480, ("agent", "think"): 1200}
SAFETY = T3.SAFETY
# 预计费用（美元）[人为约定]：agent 按 Budget 的默认上限 1.0（test3 最大 0.59）；search_direct：已存运行 token 费 0.015-0.025
# + 按假设单价记的搜索费 0.06（6 次 x 0.01），按 0.10；naive 同 run_test3
EST_USD = {("naive", "off"): 0.001, ("naive", "think"): 0.01, ("search_direct", "off"): 0.10, ("search_direct", "think"): 0.10,
           ("agent", "off"): 1.0, ("agent", "think"): 1.0}
_FATAL_HTTP = re.compile(r"\bhttp_(401|402|403)\b")


def release(q: dict) -> datetime:
    return datetime.fromisoformat(q["released_at"]).astimezone(timezone.utc)


def questions(ids=None) -> list:
    """test4 的题，按首发时刻排序；ids 不为空时只取这些题。"""
    qs = sorted((q for q in FC.QUESTIONS if q.get("set") == SET), key=release)
    if ids:
        unknown = set(ids) - {q["id"] for q in qs}
        if unknown:
            raise ValueError(f"not test4 questions: {sorted(unknown)}")
        qs = [q for q in qs if q["id"] in ids]
    return qs


def configs(qs=None) -> list:
    """跑的顺序：按首发时刻一题一题跑；每题内先便宜的基线（naive、search_direct），再 agent；每个臂先关后开。"""
    qs = questions() if qs is None else qs
    out = [{"qid": q["id"], "arm": a, "mode": m} for q in qs for a in ARMS for m in MODES]
    for c in out:
        c["cid"] = f"{c['qid']}__{c['arm']}__{c['mode']}"
    return out


def thinking_for(c: dict) -> dict:
    return dict(THINKING_ON[c["arm"]]) if c["mode"] == "think" else {}


def _q(c: dict) -> dict:
    return next(q for q in FC.QUESTIONS if q["id"] == c["qid"])


def need_for(cs: list) -> timedelta:
    return timedelta(seconds=SAFETY * sum(EST_S[(c["arm"], c["mode"])] for c in cs))


# ---------- 本地日期（as_of）和午夜 ----------
def local(t: datetime, tz=None) -> datetime:
    """tz = None：本机时区（同 date.today()，agent.run.checks_published 和 fetch.fetch_live 用的就是它）。"""
    return t.astimezone(tz) if tz is not None else t.astimezone()


def next_midnight(t: datetime, tz=None) -> datetime:
    d = local(t, tz).date() + timedelta(days=1)
    m = datetime.combine(d, dtime(0), tzinfo=tz) if tz is not None else datetime.combine(d, dtime(0)).astimezone()
    return m.astimezone(timezone.utc)


# ---------- 门 ----------
def release_limits(t: datetime, cs: list) -> list:
    """门 1、2（永久）：从 t 起按顺序跑 cs，哪些配置会在首发时刻或之后才跑完。返回说明文字（空 = 没有）。"""
    out, cum = [], timedelta(0)
    for c in cs:
        cum += need_for([c])
        rel = release(_q(c))
        if t >= rel:
            out.append(f"{c['cid']}: release time {rel.isoformat(timespec='minutes')} reached (the answer may be public)")
        elif t + cum > rel:
            out.append(f"{c['cid']}: would finish after the release time {rel.isoformat(timespec='minutes')} "
                       f"(needs {cum} from now, x{SAFETY} safety)")
    return out


def clock_limits(t: datetime, cs: list, tz=None, left=None) -> list:
    """门 3、4（等得到）：高峰、离下一个高峰不够、会跨过本地午夜。left：离下一个高峰还有多久（不给就算）。"""
    need = need_for(cs)
    left = T3.offpeak_left(t) if left is None else left
    out = []
    if left == timedelta(0):
        out.append("peak hours now")
    elif left < need:
        out.append(f"only {left} left before the next peak; need {need}")
    mid = next_midnight(t, tz)
    if t + need > mid:
        out.append(f"would cross local midnight ({local(mid, tz).isoformat(timespec='minutes')}): as_of would no longer be "
                   f"today; need {need}")
    return out


def next_start(now: datetime, cs: list, tz=None):
    """最早能开跑的时刻：非高峰、离时段结束和本地午夜都至少预计时长 x SAFETY，而且每个配置都在首发时刻前跑完。
    返回 (时刻, "")；找不到时 (None, 原因)：原因 "release" = 等到能开跑时已经赶不上首发（以后也不会有），"none" = 往后
    SCAN_DAYS 天里没有够长的时段。"""
    need = need_for(cs)
    nu = now.astimezone(timezone.utc)
    for a, b in T3.offpeak_windows(now):
        t = max(a, nu)
        while t + need <= b:
            if release_limits(t, cs):   # 越往后越晚：首发时刻只会更赶不上
                return None, "release"
            mid = next_midnight(t, tz)
            if t + need <= mid:
                return t, ""
            t = mid   # 会跨过午夜：最早只能从午夜开始
        if release_limits(b, cs):
            return None, "release"
    return None, "none"


def latest_start(now: datetime, cs: list, tz=None):
    """最晚能开跑的时刻（四个门都过：非高峰、时段和本地午夜前跑得完、每个配置在首发前跑完），按分钟扫；没有就 None。--plan 用。"""
    need, last = need_for(cs), None
    nu = now.astimezone(timezone.utc)
    for a, b in T3.offpeak_windows(now):
        t = max(a, nu)
        while t + need <= b:
            if release_limits(t, cs):
                return last
            if t + need <= next_midnight(t, tz):
                last = t
            t += timedelta(minutes=1)
        if release_limits(b, cs):
            return last
    return last


class Runner(T3.Runner):
    """同 run_test3.Runner（状态文件、日志、pending 沿用），多两样可注入：tz（本地时区，None = 本机）和 direct_factory（search_direct
    的客户端，测试换成走假服务的客户端也行，默认是真的 DirectClient + 写调用记录）。"""

    def __init__(self, root: Path = OUT, now=None, sleep=time.sleep, wait: bool = False, log=print, llm_factory=None,
                 on_start=None, tz=None, direct_factory=None):
        super().__init__(root=root, now=now, sleep=sleep, wait=wait, log=log, llm_factory=llm_factory, on_start=on_start)
        self.tz = tz
        self.direct_factory = direct_factory or (lambda calls: DirectClient(_jsonl_log(calls)))

    def agent_dir(self, c):
        from triangulate.agent import run as agent_run
        return agent_run.RES / c["qid"] / AGENT_TAG[c["mode"]]

    def as_of(self) -> str:
        return local(self.now(), self.tz).date().isoformat()

    # 门
    def gate(self, cs, what: str) -> bool:
        return self.gate_status(cs, what) is None

    def gate_status(self, cs, what: str):
        """None = 可以开跑；"permanent" = 门 1、2（首发时刻；--wait 等到能开跑时也赶不上首发）；"transient" = 门 3、4 没过且没等。
        拒跑都记一行 run.log（原因原文）。--wait 时睡到 next_start 给的时刻再查一次。"""
        now = self.now()
        perm = release_limits(now, cs)
        if perm:
            self.log(event="refused", what=what, reason="; ".join(perm))
            return "permanent"
        why = clock_limits(now, cs, self.tz)
        if not why:
            return None
        if not self.wait:
            self.log(event="refused", what=what, reason="; ".join(why))
            return "transient"
        s, none_why = next_start(now, cs, self.tz)
        if s is None:
            tail = ("; waiting for a long enough off-peak window before local midnight would miss the release time"
                    if none_why == "release" else f"; no long enough off-peak window in the next {T3.SCAN_DAYS} days")
            self.log(event="refused", what=what, reason="; ".join(why) + tail)
            return "permanent" if none_why == "release" else "transient"
        self.log(event="waiting", what=what, reason="; ".join(why), until=s.isoformat(timespec="minutes"))
        self.sleep(max(0.0, (s - now.astimezone(timezone.utc)).total_seconds()))
        return self.gate_status(cs, what)

    def run(self, cs) -> dict:
        if config.THINKING:
            raise SystemExit("TRIANGULATE_THINKING must be unset: this script sets thinking per configuration")
        todo = self.pending(cs)
        if not todo:
            self.log(event="nothing to run")
            return {"ran": [], "stopped": None, "refused": []}
        refused, live = [], []
        for c in todo:   # 门 1、2 单个配置就过不了的：记下拒跑，不进这一批（以后也不会再能跑）
            perm = release_limits(self.now(), [c])
            if perm:
                self.log(event="refused", what=c["cid"], reason="; ".join(perm))
                refused.append(c["cid"])
            else:
                live.append(c)
        if not live:
            return {"ran": [], "stopped": "release", "refused": refused}
        if not self.gate(live, f"batch of {len(live)} configurations"):
            return {"ran": [], "stopped": "gate", "refused": refused}
        ran, cum = [], 0.0
        for c in live:
            g = self.gate_status([c], c["cid"])
            if g == "permanent":   # 前面的配置跑得比预计慢：这个配置赶不上首发了，后面别的配置照常
                refused.append(c["cid"])
                continue
            if g is not None:
                return {"ran": ran, "stopped": "gate", "refused": refused}
            st = self.run_one(c)
            ran.append(c["cid"])
            cum += st.get("usd") or 0.0
            self.log(event="cost", cid=c["cid"], usd=st.get("usd"), cumulative_usd=round(cum, 6))
            if st.get("outcome") == "stopped":   # key 被拒 / 余额不足：后面的配置都不跑
                return {"ran": ran, "stopped": st.get("error"), "refused": refused}
        return {"ran": ran, "stopped": None, "refused": refused}

    def run_one(self, c, rerun_reason: str = "") -> dict:
        from triangulate.agent import run as agent_run
        q = FC.with_as_of(_q(c), self.as_of())
        if c["arm"] == "agent" and not agent_run.checks_published(q):
            # as_of 取的是本机当地日期，checks_published 用 date.today()：不一致只可能是注入的时区和本机不同（脚本的错，不是结果）
            raise SystemExit(f"{c['cid']}: real-use mode would be off (as_of {q['as_of']} is not today's date); not started")
        prev = self.status(c)
        st = {"cid": c["cid"], "qid": c["qid"], "arm": c["arm"], "thinking": c["mode"], "thinking_by_role": thinking_for(c),
              "as_of": q["as_of"], "question": q["question"], "released_at": q["released_at"],
              "started_at": self.now().astimezone(timezone.utc).isoformat(timespec="seconds"), "attempts": prev.get("attempts", [])}
        if rerun_reason:
            st["attempts"] = st["attempts"] + [{k: prev.get(k) for k in ("started_at", "finished_at", "outcome", "error", "as_of")}
                                               | {"rerun_reason": rerun_reason}]
        T3._write(self.status_path(c), st)
        self.log(event="start", cid=c["cid"], as_of=q["as_of"], thinking=st["thinking_by_role"])
        if self.on_start is not None:
            self.on_start(c)
        t0 = time.time()
        try:
            with T3.thinking(thinking_for(c)):
                fn = {"naive": self._naive, "search_direct": self._search_direct, "agent": self._agent}[c["arm"]]
                st.update(fn(c, q))
            st["outcome"] = "stopped" if st.get("error") else "done"
        except (LLM_MOD.KeyRejected, LLM_MOD.BalanceExhausted) as e:
            st.update(outcome="stopped", error=f"{type(e).__name__}: {e}")
        except LLM_MOD.TransportError as e:
            # DirectClient 把 key 被拒（401 / 403）和余额不足（402）也报成 TransportError：这几种整批停下，其余算基础设施故障
            st.update(outcome="stopped" if _FATAL_HTTP.search(str(e)) else "infra_failed", error=f"TransportError: {e}")
        except Exception as e:  # noqa: BLE001  任何崩溃都记成这个配置的结果，接着跑下一个
            st.update(outcome="crashed", error=f"{type(e).__name__}: {e}"[:500], traceback=traceback.format_exc(limit=8)[-3000:])
        st["wall_s"] = round(time.time() - t0, 1)
        st["finished_at"] = self.now().astimezone(timezone.utc).isoformat(timespec="seconds")
        if st.get("usd") is None:   # 失败的配置也记已经花掉的钱
            st["usd"] = (self._agent_usd(c) if c["arm"] == "agent"
                         else T3._usd_of_calls(self.raw_dir(c) / f"{c['qid']}.calls.jsonl"))
        T3._write(self.status_path(c), st)
        self.log(event="end", cid=c["cid"], outcome=st["outcome"], wall_s=st["wall_s"], usd=st["usd"], error=st.get("error"))
        return st

    def _naive(self, c, q) -> dict:
        d = self.raw_dir(c)
        calls = d / f"{q['id']}.calls.jsonl"
        rec = run_naive(self.llm_factory(calls), q)
        rec.update(thinking_by_role=dict(config.THINKING), as_of=q["as_of"])
        T3._write(d / f"{q['id']}.json", rec)
        return {"raw": str(d / f"{q['id']}.json"), "usd": T3._usd_of_calls(calls), "attempts_in_arm": len(rec["attempts"])}

    def _search_direct(self, c, q) -> dict:
        d = self.raw_dir(c)
        calls = d / f"{q['id']}.calls.jsonl"
        rec = run_search_direct(self.direct_factory(calls), q, control_thinking=True)
        rec["thinking_by_role"] = dict(config.THINKING)
        T3._write(d / f"{q['id']}.json", rec)
        return {"raw": str(d / f"{q['id']}.json"), "usd": T3._usd_of_calls(calls), **search_summary(rec)}

    def _agent(self, c, q) -> dict:
        from triangulate.agent import run as agent_run
        state = agent_run.run_question(q, True, AGENT_TAG[c["mode"]])
        b, lk = state.get("budget") or {}, state.get("leakage") or {}
        out = {"state": str(self.agent_dir(c) / "state.json"), "usd": b.get("usd_total_assumed"),
               "usd_tokens": b.get("usd_tokens"), "settings_thinking": (state.get("settings") or {}).get("thinking"),
               "real_use": {"pages_live_dated": lk.get("pages_live_dated"), "pages_snapshot": lk.get("pages_snapshot"),
                            "published_check": (state.get("published") or {}).get("status"),
                            "published_early": (state.get("published_early") or {}).get("status")}}
        why = str(b.get("aborted") or state.get("aborted") or "")
        if "insufficient balance" in why.lower():   # 同 run_test3：agent 把余额不足变成预算中止、照常存盘；这里让整批停下
            out["error"] = f"BalanceExhausted (inside the agent run): {why}"[:500]
        return out


def _jsonl_log(path: Path):
    """search_direct 的调用记录：每次 HTTP 请求一行（DirectClient 的计量字段，不含内容和 key）。"""
    def log(rec):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return log


def search_summary(rec: dict) -> dict:
    """search_direct 一次运行的摘要：结果、搜索次数、用到的 URL（各次尝试的全部搜索结果 URL，去重保序）、思考块数。"""
    urls = []
    for a in rec.get("attempts") or []:
        for r in a.get("results") or []:
            if r.get("url") and r["url"] not in urls:
                urls.append(r["url"])
    att = rec.get("attempts") or []
    return {"attempts_in_arm": len(att), "arm_status": rec.get("status"), "estimate": rec.get("estimate"),
            "web_search_requests": sum(int(a.get("web_search_requests") or 0) for a in att),
            "n_result_urls": len(urls), "result_urls": urls,
            "n_thinking_blocks": [a.get("n_thinking_blocks") for a in att], "max_tokens": rec.get("max_tokens"),
            "thinking_requested": rec.get("thinking")}


# ---------- 打分 ----------
def official(qid: str):
    """forecast.TEST4_OFFICIAL 里登记的首发值（计分单位）；还没登记时 None。"""
    e = FC.TEST4_OFFICIAL.get(qid)
    v = e.get("value") if isinstance(e, dict) else e
    return None if v is None else float(v)


def score_config(c: dict, q: dict, runner: Runner) -> dict:
    st = runner.status(c)
    ans = official(c["qid"])
    row = {"config": c["cid"], "qid": c["qid"], "arm": c["arm"], "thinking": c["mode"],
           "outcome": st.get("outcome") or ("started, not finished" if st.get("started_at") else "not run"),
           "as_of": st.get("as_of"), "usd": st.get("usd"), "wall_s": st.get("wall_s"), "answer_value": ans,
           "scored": ans is not None, "estimate": None, "p10": None, "p90": None, "detail": ""}
    if st.get("error"):
        row["detail"] = st["error"][:200]
    if c["arm"] in ("naive", "search_direct"):
        rec = T3._read(runner.raw_dir(c) / f"{c['qid']}.json")
        if rec is not None:
            status, est, problems = check_naive(final_reply(rec), q["answer_unit"], strict_target=False)
            row.update(estimate=est, arm_status=status, attempts=len(rec["attempts"]))
            if problems:   # 最后一次回复本身不合法时，说明用那次尝试记下的原因（截断、不是合法 JSON）
                row["detail"] = "; ".join(rec["attempts"][-1]["problems"] or problems)[:200]
            if c["arm"] == "search_direct":
                s = search_summary(rec)
                row.update({k: s[k] for k in ("web_search_requests", "n_result_urls", "n_thinking_blocks", "thinking_requested")})
    else:
        state = T3._read(runner.agent_dir(c) / "state.json")
        if state is not None:
            r = (state.get("compute") or {}).get("result") or {}
            f, note = T3._unit_factor(state, q)
            est = r.get("central")
            lk = state.get("leakage") or {}
            row.update(estimate_as_run=est, unit_note=note, basis=r.get("basis"),
                       published_check=(state.get("published") or {}).get("status"),
                       pages_live_dated=lk.get("pages_live_dated"), pages_snapshot=lk.get("pages_snapshot"),
                       methods=[(m.get("id"), m.get("method"), m.get("estimate"))
                                for m in (state.get("compute") or {}).get("methods") or []])
            if est is not None and f is None:
                row.update(arm_status="unit not convertible", detail=note)
            elif est is not None:
                row.update(estimate=est * f, p10=None if r.get("p10") is None else r["p10"] * f,
                           p90=None if r.get("p90") is None else r["p90"] * f, arm_status="ok")
            else:
                row["arm_status"] = "no estimate"
                row["detail"] = row["detail"] or str(state.get("aborted") or (state.get("compute") or {}).get("error") or "")[:200]
    est = row["estimate"]
    if ans is not None and est is not None and est > 0:
        row.update(pct_err=est / ans - 1, abs_log10_err=abs(math.log10(est / ans)))
        if row["p10"] is not None and row["p90"] is not None:
            row["covered_80"] = row["p10"] <= ans <= row["p90"]
    return row


def aggregate(rows: list) -> list:
    """每个臂 x 思考一行。误差只在已登记首发值的题上算；这些题里没出数的配置误差记为无穷大、计入中位数（同 run_test3）。"""
    out = []
    for arm in ARMS:
        for mode in MODES:
            rs = [r for r in rows if r["arm"] == arm and r["thinking"] == mode]
            if not rs:
                continue
            sc = [r for r in rs if r["scored"]]
            pe = [abs(r["pct_err"]) if r.get("pct_err") is not None else math.inf for r in sc]
            le = [r["abs_log10_err"] if r.get("abs_log10_err") is not None else math.inf for r in sc]
            iv = [r for r in sc if "covered_80" in r]
            out.append({"arm": arm, "thinking": mode, "n": len(rs), "n_estimates": sum(r["estimate"] is not None for r in rs),
                        "n_scored": len(sc), "median_abs_pct_err": T3._median_inf(pe), "median_abs_log10_err": T3._median_inf(le),
                        "within_10pct": sum(x <= 0.10 for x in pe), "within_5pct": sum(x <= 0.05 for x in pe),
                        "covered_80": (f"{sum(r['covered_80'] for r in iv)}/{len(iv)}" if iv
                                       else ("n/a (no interval)" if sc else "n/a (no official value yet)")),
                        "usd": round(sum(r.get("usd") or 0 for r in rs), 4),
                        "failures": [f"{r['qid']}: {r['outcome']}" + (f" / {r.get('arm_status')}" if r.get("arm_status") not in (None, "ok") else "")
                                     for r in rs if r["estimate"] is None]})
    return out


def render_md(rows: list, agg: list, qs: list) -> str:
    f = T3._f
    L = ["# 留出测试 4（前瞻）：三臂 x 思考开关（probes/run_test4.py --score）", "",
         "误差 = 估计 / 首发值 - 1；abs(log10) = |log10(估计 / 首发值)|。只在 forecast.TEST4_OFFICIAL 登记了首发值的题上算；"
         "这些题里没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂（直接问、联网直接问没有区间）。"
         "费用：基线 = 调用记录的 usd 合计（search_direct 含按假设单价记的搜索费）；agent = 预算的 usd_total_assumed。", "",
         "## 汇总", "",
         "| 臂 | 思考 | 出数 | 已打分 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for a in agg:
        L.append(f"| {a['arm']} | {a['thinking']} | {a['n_estimates']}/{a['n']} | {a['n_scored']} | "
                 f"{f(a['median_abs_pct_err'], 'apct')} | {f(a['median_abs_log10_err'], 'log')} | {a['within_10pct']} | "
                 f"{a['within_5pct']} | {a['covered_80']} | {f(a['usd'], 'usd')} | {'; '.join(a['failures']) or '—'} |")
    L += ["", "## 逐个配置", "",
          "| 题 | 臂 | 思考 | as_of | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        cov = "—" if "covered_80" not in r else ("是" if r["covered_80"] else "否")
        note = r.get("detail") or ""
        if r["arm"] == "search_direct" and r.get("n_result_urls") is not None:
            note = (f"搜索 {r['web_search_requests']} 次、结果 URL {r['n_result_urls']} 个、思考块 {r['n_thinking_blocks']}"
                    + (f"；{note}" if note else ""))
        if r["arm"] == "agent" and r.get("published_check"):
            note = (f"已公布检查 {r['published_check']}、live 页 {r.get('pages_live_dated')}、快照 {r.get('pages_snapshot')}"
                    + (f"；{note}" if note else ""))
        L.append(f"| {r['qid']} | {r['arm']} | {r['thinking']} | {r.get('as_of') or '—'} | "
                 f"{r['outcome']}{' / ' + r['arm_status'] if r.get('arm_status') else ''} | {f(r['estimate'], 'n')} | "
                 f"{f(r.get('pct_err'), 'pct')} | {f(r.get('abs_log10_err'), 'log')} | {f(r['p10'], 'n')} | {f(r['p90'], 'n')} | "
                 f"{cov} | {f(r.get('usd'), 'usd')} | {note.replace('|', '/')[:160]} |")
    L += ["", "## 首发值和参照（去年同期的登记值，不是对照臂）", "", "| 题 | 首发时刻 | 首发值 | 去年同期 | 去年同期的误差 |",
          "|---|---|---|---|---|"]
    for q in qs:
        ans = official(q["id"])
        L.append(f"| {q['id']} | {q['released_at']} | {f(ans, 'n') if ans is not None else '还没登记'} | {q['last_year']:,} | "
                 f"{f(q['last_year'] / ans - 1, 'pct') if ans else '—'} |")
    return "\n".join(L) + "\n"


def score(runner: Runner) -> dict:
    qs = questions()
    by_id = {q["id"]: q for q in qs}
    rows = [score_config(c, by_id[c["qid"]], runner) for c in configs(qs)]
    agg = aggregate(rows)
    out = {"set": SET, "configs": rows, "summary": agg,
           "official": {q["id"]: FC.TEST4_OFFICIAL.get(q["id"]) for q in qs}}
    T3._write(runner.root / "summary.json", out)
    (runner.root / "summary.md").write_text(render_md(rows, agg, qs), encoding="utf-8")
    return out


def plan_text(runner: Runner, qs=None, cs=None) -> str:
    qs = questions() if qs is None else qs
    cs = configs(qs) if cs is None else cs
    todo = runner.pending(cs)
    now = runner.now()
    nu = now.astimezone(timezone.utc).replace(microsecond=0)   # 显示用（时长不带微秒）
    left = T3.offpeak_left(now)
    usd = sum(EST_USD[(c["arm"], c["mode"])] for c in todo)
    mid = next_midnight(now, runner.tz)
    lines = [f"{len(cs)} configurations, {len(todo)} not run yet; estimated time {need_for(todo)} (x{SAFETY} safety), "
             f"estimated cost up to ${usd:.2f}",
             f"now {nu.isoformat(timespec='minutes')} = local {local(now, runner.tz).isoformat(timespec='minutes')}; "
             f"as_of if started now: {runner.as_of()}; peak now: {config.is_peak(now)}; off-peak time left: {left}; "
             f"local midnight in {mid - nu}"]
    for q in qs:
        rel = release(q)
        mine = [c for c in todo if c["qid"] == q["id"]]
        line = (f"{q['id']}: release {rel.isoformat(timespec='minutes')} = local "
                f"{local(rel, runner.tz).isoformat(timespec='minutes')} (in {rel - nu}); {len(mine)} pending, need {need_for(mine)}")
        if mine:
            last = latest_start(now, mine, runner.tz)
            line += ("; latest start of this question's pending configurations (all four gates): "
                     + (f"local {local(last, runner.tz).isoformat(timespec='minutes')}" if last else "none"))
        lines.append(line)
    if todo:
        perm_one = {c["cid"] for c in todo if release_limits(now, [c])}
        live = [c for c in todo if c["cid"] not in perm_one]
        why = release_limits(now, live) + clock_limits(now, live, runner.tz, left) if live else []
        lines.append("batch gate now: " + ("would start" if live and not why else
                                           ("; ".join(why) if live else "nothing can run (release times)")))
        if live:
            s, none_why = next_start(now, live, runner.tz)
            lines.append("earliest start of the whole batch (off-peak, before local midnight, before release): "
                         + (f"{s.isoformat(timespec='minutes')} = local {local(s, runner.tz).isoformat(timespec='minutes')}"
                            if s else ("none: it would miss a release time" if none_why == "release" else "none found")))
    for c in cs:
        st = runner.status(c)
        state = st.get("outcome") or ("started" if st.get("started_at") else "pending")
        if state == "pending":
            r = release_limits(now, [c]) or clock_limits(now, [c], runner.tz, left)
            state += " (" + ("runnable now" if not r else "; ".join(x.split(": ", 1)[-1] if x.startswith(c["cid"]) else x
                                                                      for x in r)) + ")"
        lines.append(f"  {c['cid']:46s} thinking={thinking_for(c) or 'off'}  {state}")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="test4 (prospective): questions x 3 arms x thinking off/on, one run each")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--plan", action="store_true")
    g.add_argument("--run", action="store_true")
    g.add_argument("--rerun", metavar="CONFIG")
    g.add_argument("--score", action="store_true")
    ap.add_argument("--question", action="append", default=[], help="only these test4 questions (repeatable)")
    ap.add_argument("--config", action="append", default=[], help="with --run / --plan: only these configurations (repeatable)")
    ap.add_argument("--wait", action="store_true", help="wait for an off-peak window that is long enough instead of refusing")
    ap.add_argument("--reason", default="", help="why --rerun is an infrastructure failure (required with --rerun)")
    a = ap.parse_args(argv)
    runner = Runner(wait=a.wait)
    try:
        qs = questions(a.question)
    except ValueError as e:
        ap.error(str(e))
    cs = configs(qs)
    if a.config:
        unknown = set(a.config) - {c["cid"] for c in cs}
        if unknown:
            ap.error(f"unknown configurations (or not in --question): {sorted(unknown)}")
        cs = [c for c in cs if c["cid"] in a.config]
    if a.plan:
        print(plan_text(runner, qs, cs))
        return 0
    if a.score:
        print(json.dumps(_clean(score(runner)["summary"]), indent=1, ensure_ascii=False, default=str))
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
        if not runner.gate([c], c["cid"]):
            return 2
        runner.run_one(c, rerun_reason=a.reason)
        score(runner)
        return 0
    res = runner.run(cs)
    print(json.dumps(_clean(score(runner)["summary"]), indent=1, ensure_ascii=False, default=str))
    return 0 if res["stopped"] is None else 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())

"""网页发起的运行（只在本进程内存里登记）。

一个运行 = 后台线程：prepare_run -> 图跑到「人工确认方向」的 interrupt 停下（status = awaiting_approval）->
网页批准（可以去掉一些方向，走图里已有的 resume-with-directions 路径）-> 另一个后台线程继续跑完 -> save_run 写盘。
图本身（InMemorySaver checkpointer、节点、规则）和命令行完全一样；这里只读进度：
- 子 agent 的进度来自 Context.progress 回调（pipeline.run_direction 发出的只读事件）；
- 节点完成情况来自 graph.stream(stream_mode="updates")；
- 裁判 / 输入核对 / 修正调用来自这次运行自己的 calls.jsonl；花费来自 ctx.budget。
每个网页运行有自己的 tag（web_<UTC 时间>），结果写在 results/agent/<qid>/<tag>/，不会覆盖回测结果。
服务进程退出后，内存里的登记就没了（已写盘的结果还在，可以在「已保存的运行」里看）。

web-v0.9：网页运行一律自带 key（providers.ModelSpec，「BYOK」），没有 spec 就拒跑；永远不读服务器的 key 文件。
spec 只在这个 WebRun 和 prepare 出来的 ctx 上（内存里），运行结束（完成 / 失败 / 取消）时 _release() 先把已存的文字过一遍
redact_obj、再 drop_key()；运行中返回的状态视图也先过 redact_obj。spec.public()（provider、模型、区域、档位、上限）可以给网页看。
"""
import hashlib
import json
import threading
import time
import uuid
from datetime import date, datetime, timezone

from langgraph.types import Command

from ..agent import run as agent_run

ACTIVE = ("planning", "awaiting_approval", "running")
FINISHED = ("done", "failed", "cancelled")
MAX_ACTIVE = 2
CANCEL_REASON = "cancelled from the web UI"
ERROR_MAX_CHARS = 500
NEED_KEY = ("需要你自己的 API key：网页运行只用你填的 key，从不使用服务器上的 key 文件。"
            "/ Your own API key is required: web runs only use the key you enter and never the server's key file.")
# 运行结束清 key 之前要过一遍 redact_obj 的字段（状态视图里的文字都来自这些）
_SCRUB_FIELDS = ("q", "error", "target", "proposed", "plan_notes", "dirs", "markets", "judge", "compute", "approvals", "result")


class Busy(RuntimeError):
    pass


class BadState(RuntimeError):
    pass


def ask_id(question: str, as_of: str) -> str:
    """和命令行 --ask 相同的题 id 规则（triangulate/__main__.py）。"""
    return "ask_" + hashlib.sha1(f"{question}|{as_of}".encode("utf-8")).hexdigest()[:8]


def _iso(t):
    return None if t is None else datetime.fromtimestamp(t, timezone.utc).isoformat(timespec="seconds")


class WebRun:
    def __init__(self, run_id: str, q: dict, tag: str, prepare, save, spec=None):
        self.id, self.q, self.tag = run_id, q, tag
        self._prepare, self._save = prepare, save
        self._spec = spec   # providers.ModelSpec（含 key，只在内存里）；Registry.start 保证网页运行一定有
        self.lock = threading.Lock()
        self.status, self.error = "planning", None
        self.created, self.finished = time.time(), None
        self.h = None
        self.cancel_requested = False
        self.approvals = []
        self.target, self.proposed, self.plan_notes = None, [], []
        self.plan_done = False
        self.dirs, self.order = {}, []       # 方向 id -> 进度；批准后的方向（approve 节点会重新编号 d1..dK）+ 第二轮方向
        self.markets = None
        self.judge = {}                      # 轮次 -> 摘要
        self.compute, self.final_done = None, False
        self.result = None

    @property
    def qid_tag(self):
        return self.q["id"], self.tag

    # ---------- 后台线程 ----------
    def start(self):
        self._spawn(self._plan_phase)

    def _spawn(self, fn, *args):
        threading.Thread(target=self._guard, args=(fn, *args), daemon=True, name=f"web-run-{self.id}").start()

    def _guard(self, fn, *args):
        try:
            fn(*args)
        except Exception as e:  # noqa: BLE001  任何异常都记成 failed，不让线程悄悄死掉
            with self.lock:
                self.status, self.error, self.finished = "failed", self._clip(f"{type(e).__name__}: {e}"), time.time()
        finally:
            if self.status in FINISHED:   # 完成 / 失败 / 取消：清 key（停在人工确认时不清，批准后还要用）
                self._release()

    def _clip(self, text: str) -> str:
        """存进状态的错误文字：先把 key 换成 ***，再截断（先截断的话，截在 key 中间的半截就认不出来了）。"""
        sp = self._spec
        return (text if sp is None else sp.redact(text))[:ERROR_MAX_CHARS]

    def _release(self):
        """运行结束：已存的文字先过一遍 redact_obj（key 已清掉以后就认不出来了），再把 key 从内存里清掉。
        _after_stream 调 save 时带 keep_key=True（save_run 不清 key），由这里统一清：完成、失败、取消都走 _guard 的 finally。"""
        sp = self._spec
        if sp is None or not sp.has_key:
            return
        with self.lock:
            for name in _SCRUB_FIELDS:
                setattr(self, name, sp.redact_obj(getattr(self, name)))
            sp.drop_key()

    def _plan_phase(self):
        h = self._prepare(self.q, self.tag, spec=self._spec)
        h["ctx"].progress = self._on_event
        self.h = h
        if self.cancel_requested:
            self._abort_budget()
        self._stream(agent_run.initial_input(self.q))
        self._after_stream()

    def _resume(self, decision: dict):
        self._stream(Command(resume=decision))
        self._after_stream()

    def _stream(self, inp):
        for chunk in self.h["g"].stream(inp, self.h["cfg"], stream_mode="updates"):
            self._on_update(chunk)

    def _after_stream(self):
        snap = self.h["g"].get_state(self.h["cfg"])
        ints = getattr(snap, "interrupts", ()) or ()
        if ints:  # 停在人工确认
            payload = ints[0].value or {}
            with self.lock:
                self.target = payload.get("target") or self.target
                self.proposed = list(payload.get("directions") or [])
                cancelled = self.cancel_requested
                if cancelled:  # 规划时点了取消：不进入等待确认，直接按「不批准」结束（审查发现：否则会占着名额、还能被批准）
                    self.approvals.append({"approved": False, "by": "web-cancel"})
                else:
                    self.status = "awaiting_approval"
            if cancelled:
                self._resume(self.approvals[-1])
            return
        state = self._save(self.h, self.approvals, keep_key=True)   # key 留到 _release 统一清（先 redact 已存的文字）
        r = ((state or {}).get("compute") or {}).get("result") or {}
        with self.lock:
            self.result = {"qid": self.q["id"], "tag": self.h["tag"]}
            if self.cancel_requested:
                self.status = "cancelled"
            elif (state or {}).get("aborted") and r.get("central") is None and r.get("most_likely") is None:
                self.status, self.error = "failed", self._clip(str(state["aborted"]))
            else:
                self.status = "done"
            self.finished = time.time()

    def _abort_budget(self):
        """取消 = 用图里已有的预算中止路径：之后每次调用前的预扣都会抛 BudgetExceeded，各节点干净收尾。"""
        b = self.h["ctx"].budget
        if not b.aborted:
            b.aborted = CANCEL_REASON

    # ---------- 用户操作 ----------
    def approve(self, keep_ids=None):
        with self.lock:
            if self.status != "awaiting_approval" or self.cancel_requested:
                raise BadState(f"run is {self.status}{' (cancel requested)' if self.cancel_requested else ''}, not awaiting_approval")
            ids = [d.get("id") for d in self.proposed]
            if keep_ids is None:
                keep = ids
            else:
                unknown = sorted(set(keep_ids) - set(ids))
                if unknown:
                    raise ValueError(f"unknown direction ids: {unknown}")
                keep = [i for i in ids if i in set(keep_ids)]
                if not keep:
                    raise ValueError("至少保留一个方向（全部不要请用「取消」）")
            decision = {"approved": True, "by": "web"}
            if len(keep) < len(ids):   # 只在真的去掉了方向时才带 directions，否则和命令行的批准完全一样
                decision["directions"] = [d for d in self.proposed if d.get("id") in keep]
            self.approvals.append(decision)
            self.status = "running"
        self._spawn(self._resume, decision)
        return decision

    def cancel(self):
        with self.lock:
            if self.status not in ACTIVE:
                raise BadState(f"run is {self.status}")
            if getattr(self, "final_done", False):  # 最终答案已经写完、只差存盘：不再接受取消（否则完整结果会被标成 cancelled）
                raise BadState("run has finished computing; it is being saved")
            self.cancel_requested = True
            waiting = self.status == "awaiting_approval"
            if waiting:
                self.approvals.append({"approved": False, "by": "web-cancel"})
                self.status = "running"
        if self.h is not None:
            self._abort_budget()
        if waiting:  # 和命令行里回答 N 一样：不批准，图直接结束
            self._spawn(self._resume, self.approvals[-1])

    # ---------- 进度 ----------
    def _dir(self, did: str, rnd=None) -> dict:
        d = self.dirs.get(did)
        if d is None:
            d = self.dirs[did] = {"id": did, "round": rnd or 1, "category": "", "hypothesis": "", "status": "queued",
                                  "n_urls": None, "pages_done": 0, "pages": {"snapshot": 0, "live_dated": 0, "dropped": 0},
                                  "n_extracted": 0, "n_verified": 0, "n_points": None, "n_kept": None, "stopped": None}
            self.order.append(did)
        return d

    def _add_dirs(self, ds: list, rnd: int):
        for x in ds:
            d = self._dir(x["id"], rnd)
            d.update(category=x.get("category", ""), hypothesis=str(x.get("hypothesis", ""))[:300], round=rnd)

    def _on_event(self, ev: dict):
        with self.lock:
            d = self._dir(ev["direction_id"], ev.get("round"))
            k = ev.get("kind")
            if k == "direction_start":
                d["status"] = "searching"
            elif k == "searched":
                d.update(status="fetching", n_urls=ev.get("n_urls"))
            elif k == "page":
                d["pages_done"] += 1
                s = ev.get("status") or "dropped"
                d["pages"][s] = d["pages"].get(s, 0) + 1
                d["status"] = "fetching" if s == "dropped" else "extracting"
            elif k == "extracted":
                d["n_extracted"] += 1
                d["n_verified"] += int(ev.get("n_verified") or 0)
                d["status"] = "fetching"
            elif k == "direction_done":
                d.update(status="stopped" if ev.get("stopped") else "done", n_points=ev.get("n_points"),
                         stopped=ev.get("stopped"))

    def _on_update(self, chunk: dict):
        with self.lock:
            for node, upd in (chunk or {}).items():
                upd = upd if isinstance(upd, dict) else {}
                if node == "plan":
                    self.plan_done = True
                    self.target = (upd.get("plan") or {}).get("target") or self.target
                    self.plan_notes = upd.get("plan_notes") or []
                elif node == "approve":
                    ap = upd.get("approval") or {}
                    if ap.get("approved"):
                        self._add_dirs(upd.get("directions") or self.proposed, 1)
                elif node == "subagent":
                    for r in upd.get("results") or []:
                        d = self._dir(r["direction_id"], r.get("round"))
                        if d["status"] not in ("done", "stopped"):
                            d.update(status="stopped" if r.get("error") or r.get("aborted") else "done",
                                     stopped=r.get("error") or r.get("aborted"))
                        d["n_points"] = len(r.get("points") or [])
                elif node == "markets":
                    for r in upd.get("results") or []:
                        mk = r.get("markets") or {}
                        self.markets = {"n_markets": len(mk.get("markets") or []), "n_points": len(r.get("points") or []),
                                        "note": mk.get("note")}
                elif node == "judge":
                    for jr in upd.get("judge_rounds") or []:
                        self.judge[jr.get("round")] = _judge_summary(jr)
                        self._add_dirs(jr.get("extra_directions") or [], 2)
                    kept = {}
                    for p in upd.get("points") or []:
                        if p.get("keep") and not p.get("ablation_excluded"):
                            kept[p.get("direction_id")] = kept.get(p.get("direction_id"), 0) + 1
                    for did, d in self.dirs.items():
                        if d["status"] in ("done", "stopped"):
                            d["n_kept"] = kept.get(did, 0)
                elif node == "compute":
                    c = upd.get("compute") or {}
                    r = c.get("result") or {}
                    ms = c.get("methods") or []
                    self.compute = {"central": r.get("central"), "p10": r.get("p10"), "p90": r.get("p90"),
                                    "basis": r.get("basis"), "n_methods": len(ms), "mode": r.get("mode") or "continuous",
                                    "most_likely": r.get("most_likely"), "most_likely_prob": r.get("most_likely_prob"),
                                    "outcomes": r.get("outcomes"),
                                    "n_computed": sum(1 for m in ms if m.get("estimate") is not None or m.get("distribution")),
                                    "n_excluded_by_input_audit": len(c.get("excluded_by_input_audit") or [])}
                elif node == "final":
                    self.final_done = True

    def _roles(self) -> dict:
        """这次运行 calls.jsonl 里已经记下的调用，按 role 计数（裁判、输入核对、修正都在这里看得到）。"""
        out = {}
        p = (self.h or {}).get("out_dir")
        f = p / "calls.jsonl" if p is not None else None
        if f is None or not f.is_file():
            return out
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                arm = json.loads(line).get("arm", "")
            except ValueError:
                continue   # 正在写的最后一行
            out[arm] = out.get(arm, 0) + 1
        return out

    def _stages(self, roles: dict) -> list:
        S = []
        st = self.status

        def add(key, label, status, detail=""):
            S.append({"key": key, "label": label, "status": status, "detail": detail})
        add("plan", "规划方向", "done" if self.plan_done else ("running" if st == "planning" else "pending"),
            f"提出 {len(self.proposed)} 个方向" if self.proposed else "")
        add("approve", "人工确认", "done" if any(a.get("approved") for a in self.approvals) else
            "waiting" if st == "awaiting_approval" else "pending",
            next((f"保留 {len(a['directions'])} 个方向" if a.get("directions") else "全部保留"
                  for a in self.approvals if a.get("approved")), ""))
        for rnd in (1, 2):
            ds = [self.dirs[i] for i in self.order if self.dirs[i]["round"] == rnd]
            if rnd == 2 and not ds:
                continue
            n_done = sum(d["status"] in ("done", "stopped") for d in ds)
            add(f"subagents{rnd}", "子 agent 取证" if rnd == 1 else "追加的 base-rate 方向",
                "done" if ds and n_done == len(ds) else "running" if ds else "pending", f"{n_done}/{len(ds)} 完成" if ds else "")
            js = self.judge.get(rnd)
            called = [f"{k} x{v}" for k, v in roles.items() if k.startswith(f"judge:r{rnd}")]
            if js is None and roles.get("audit"):   # 输入核对只在最后一轮裁判里做，这一轮还没结束就是它的
                called.append(f"audit x{roles['audit']}")
            add(f"judge{rnd}", f"裁判第 {rnd} 轮", "done" if js else "running" if ds and n_done == len(ds) else "pending",
                js["text"] if js else ("已有调用：" + ", ".join(called) if called else ""))
        c = self.compute
        add("compute", "代码计算", "done" if c else "pending",
            "" if not c else f"{c['n_computed']}/{c['n_methods']} 个方法算出估计" +
            (f"，{c['n_excluded_by_input_audit']} 个被输入核对排除" if c["n_excluded_by_input_audit"] else ""))
        add("final", "终稿", "done" if self.final_done else ("running" if c and st == "running" else "pending"))
        return S

    def _public(self, view: dict) -> dict:
        """返回给网页之前：spec 的公开部分（不含 key）加进去，所有文字过一遍 redact_obj（key 已清掉时原样返回）。"""
        sp = self._spec
        if sp is None:
            return view
        return sp.redact_obj({**view, "run_spec": sp.public(), "key_in_memory": sp.has_key})

    def status_view(self) -> dict:
        with self.lock:
            roles = self._roles()
            b = self.h["ctx"].budget if self.h else None
            end = self.finished or time.time()
            view = {"id": self.id, "qid": self.q["id"], "tag": self.tag, "question": self.q["question"], "as_of": self.q["as_of"],
                    "status": self.status, "error": self.error, "cancel_requested": self.cancel_requested,
                    "created_at": _iso(self.created), "finished_at": _iso(self.finished),
                    "elapsed_s": round(end - self.created, 1),
                    "usd": None if b is None else round(b.usd, 4), "usd_cap": None if b is None else b.usd_cap,
                    "target": self.target, "plan_notes": self.plan_notes,
                    "directions_proposed": [{k: d.get(k) for k in ("id", "category", "perspective", "hypothesis", "data_to_find",
                                                                   "expected_information")} for d in self.proposed],
                    "directions": [dict(self.dirs[i], pages=dict(self.dirs[i]["pages"])) for i in self.order],
                    "markets": self.markets, "judge": {str(k): v for k, v in self.judge.items()},
                    "stages": self._stages(roles), "calls": roles, "compute": self.compute,
                    "approvals": list(self.approvals), "result": self.result}
            return self._public(view)

    def brief(self) -> dict:
        with self.lock:
            return self._public({"id": self.id, "qid": self.q["id"], "tag": self.tag, "question": self.q["question"][:200],
                                 "as_of": self.q["as_of"], "status": self.status, "created_at": _iso(self.created),
                                 "result": self.result})


def _judge_summary(jr: dict) -> dict:
    """裁判一轮的摘要（进度里显示）：丢了几个点、要了几个追加方向、输入核对和修正的结果。"""
    if jr.get("skipped") or jr.get("error"):
        why = jr.get("skipped") or jr.get("error")
        return {"round": jr.get("round"), "text": f"没有完成：{why}"[:300], "extra_directions": []}
    n_drop = sum(1 for x in jr.get("decisions") or [] if isinstance(x, dict) and not x.get("keep", False))
    parts = [f"丢弃 {n_drop} 个点", f"提出 {len(jr.get('methods') or [])} 个方法"]
    if jr.get("extra_directions"):
        parts.append(f"追加 {len(jr['extra_directions'])} 个 base-rate 方向")
    if "audit_failed" in jr:   # 只有交给 compute 的那一轮做输入核对
        parts.append(f"输入核对排除 {len(jr['audit_failed'] or {})} 个方法")
    if jr.get("audit_error"):
        parts.append(f"输入核对出错：{jr['audit_error']}"[:120])
    rp = jr.get("repair")
    if rp:
        parts.append(f"修正轮：{len(rp.get('errors') or [])} 个问题" + ("，已退回原方案" if rp.get("reverted") else "") +
                     (f"，修正调用失败：{rp['error']}"[:120] if rp.get("error") else ""))
    return {"round": jr.get("round"), "text": "；".join(parts),
            "extra_directions": [x.get("id") for x in jr.get("extra_directions") or []]}


class Registry:
    """本进程里的网页运行。prepare / save 默认是 agent.run 的 prepare_run / save_run（测试里可以换成假的）。"""

    def __init__(self, prepare=None, save=None, max_active: int = MAX_ACTIVE):
        self._prepare = prepare or agent_run.prepare_run
        self._save = save or agent_run.save_run
        self.max_active = max_active
        self.runs = {}
        self.lock = threading.Lock()

    def start(self, question: str, as_of=None, spec=None) -> WebRun:
        """spec（providers.ModelSpec）必须有：网页运行只用用户自己的 key。登记之前任何一步出错都先清掉 spec 里的 key。"""
        try:
            return self._start(question, as_of, spec)
        except BaseException:
            if spec is not None and not any(r._spec is spec for r in self.runs.values()):
                spec.drop_key()
            raise

    def _start(self, question: str, as_of, spec) -> WebRun:
        if spec is None or not getattr(spec, "has_key", False):
            raise ValueError(NEED_KEY)
        if not isinstance(question, str) or not (as_of is None or isinstance(as_of, str)):
            raise ValueError("question 必须是字符串，as_of 必须是字符串或留空")   # 审查发现：非字符串原来会 500
        question = (question or "").strip()
        if not question:
            raise ValueError("问题不能为空")
        if len(question) > 2000:
            raise ValueError("问题太长（最多 2000 字符）")
        today = date.today()
        as_of = (as_of or "").strip() or today.isoformat()
        try:
            d = date.fromisoformat(as_of)
        except ValueError:
            raise ValueError("as_of 必须是 YYYY-MM-DD") from None
        if d > today:
            raise ValueError(f"as_of 不能晚于今天（{today.isoformat()}）")
        with self.lock:
            active = [r for r in self.runs.values() if r.status in ACTIVE]
            if len(active) >= self.max_active:
                raise Busy(f"已经有 {len(active)} 个运行没有结束（上限 {self.max_active} 个）。等它们结束或取消后再开新的。")
            qid = ask_id(question, d.isoformat())
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            tag, n = f"web_{stamp}", 2
            while any(r.qid_tag == (qid, tag) for r in self.runs.values()) or (agent_run.RES / qid / tag).exists():
                tag, n = f"web_{stamp}_{n}", n + 1
            run = WebRun(uuid.uuid4().hex[:12], {"id": qid, "question": question, "as_of": d.isoformat()}, tag,
                         self._prepare, self._save, spec=spec)
            self.runs[run.id] = run
        run.start()
        return run

    def get(self, run_id: str) -> WebRun:
        r = self.runs.get(run_id)
        if r is None:
            raise KeyError(run_id)
        return r

    def list(self) -> list:
        return [r.brief() for r in sorted(self.runs.values(), key=lambda r: -r.created)]

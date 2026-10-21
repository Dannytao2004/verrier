"""子 agent 流水线与运行上下文：预算、带日志的 LLM、SEARCHER -> FETCHER -> EXTRACTOR -> 代码核对。
v2.5 真实使用（ctx.live_fetch）：一个方向的几个 URL 同时直接抓 live 页（fetch_live，不查 Wayback），按 URL 顺序抽取；
每页核对完的点交给 ctx.early（published.EarlyWatch），确认了已公布的目标值就停下其余子 agent。回测的流程没有改。"""
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import date, datetime, timezone

from ..config import MAX_TOKENS, MODEL, price
from ..llm import LLM, BalanceExhausted, TransportError
from ..providers import reserve_chars_per_token, search_fee_usd, tokens_for_model
from . import evidence as ev
from .fetch import fetch_live, fetch_page
from .prompts import EXTRACT_SYSTEM, EXTRACT_USER, SEARCH_USER
from .search import SEARCH_QUERIES_MAX_TOKENS, Searcher

MAX_CHARS_TO_EXTRACTOR = 400_000   # v2.8b 从 24_000 放宽（HTML 和 PDF 都适用）：长的统计页不再只发开头
QUOTE_STORE_CHARS = 200


class BudgetExceeded(RuntimeError):
    pass


class _Hold:
    """v2.10f：一份在途预扣（Budget.hold 的 with 里拿到）。size = 要的金额；amount = 现在占着的金额（renew 放不下时为 0）。"""
    __slots__ = ("size", "amount", "live")

    def __init__(self, size: float):
        self.size, self.amount, self.live = size, size, True


class Budget:
    """每题的上限。USD 包括 token 成本和按假设单价记的搜索费。
    每次调用前在锁里按「最坏情况」预扣（hold），调用结束后退回预扣、只留实际花费；已花 + 在途预扣 + 这次预扣
    超过上限就不发这次调用（抛 BudgetExceeded，各节点据此干净收尾）。预扣按上限估：LLM 按输入字符数 / 2 个 token
    （v2.10f：别家的模型按 1 个字符 1 个 token）和 max_tokens 个输出 token、峰时价；搜索按 token 上限加 (2 x max_uses + 2) 次搜索费
    （实测最多 6 次 / max_uses 3）。预扣是估计的最坏情况，不是严格的上界（PROVIDERS.md 第 14.3 节）。
    v2.5.5：先拿并发名额（sem）再预扣，排队等名额的调用不占预扣，在途预扣最多 llm_concurrency 份。
    方向数不写死，由页面和美元预算推出来（max_directions）。
    v2.10f（自带 key 的运行，wait_for_room = True，configure_byok 设）：放不下只是因为在途的预扣时，等在途的调用结束再预扣；
    只有「已花 + 这一次」放不下（或者没有在途的调用可等）才中止。命令行、回测没有 spec，照旧放不下就中止（行为和以前相同）。"""

    # 规划方向数用的「一个方向的典型花费」：实测搜索中位 $0.047（含假设的搜索费）+ 4 次抽取约 $0.006 + 挑页 $0.002。
    # 这是 deepseek-flash 的值（REFERENCE_MODEL）；别的模型按 DIRECTION_PROFILE 的价格比例放大（typical_direction_usd）
    TYPICAL_DIRECTION_USD = 0.06
    REFERENCE_MODEL = "deepseek-flash"
    # v2.10a：一个方向的 token 构成（已存 deepseek-flash 运行 1251 个方向的平均：搜索 + 抽取的 cache hit / miss 输入、输出 token，
    # 搜索次数），只用来算两个模型的价格比例，不用来记账
    DIRECTION_PROFILE = {"hit": 13_600, "miss": 25_700, "out": 3_600, "searches": 4}
    ROUND1_USD_SHARE = 0.6   # 第一轮方向最多用掉上限的 60%，其余留给 base-rate 方向、裁判、终稿
    model = None   # v2.10a：计价用的模型；None = config.MODEL（命令行、回测）。Budget.for_model 设
    search_tokens = None   # v2.10b：一次搜索发出的 max_tokens；None = MAX_TOKENS["search"]（有 ModelSpec 时 Context 设成实际发出的值）
    # 一次搜索请求预扣的输入 token。命令行（没有 spec）照旧 30,000；v2.10f 自带 key 的运行（模型自己搜的 provider）按已存 1,262 次
    # DeepSeek 搜索 input + cache read 的 p99（71,669；中位 27,719，p90 44,283，最大 265,681，42% 超过 30,000）取 72,000。
    # 「生成查询词 + 搜索接口」的 provider（Kimi、GLM）的模型调用只有生成查询词（输入是几千字符的 brief），照旧 30,000
    SEARCH_INPUT_TOKENS = 30_000
    SEARCH_INPUT_TOKENS_BYOK = 72_000
    search_input_tokens = None   # None = SEARCH_INPUT_TOKENS；configure_byok 设
    wait_for_room = False        # v2.10f：见类说明；configure_byok 设 True
    WAIT_POLL_S = 0.5            # 等在途调用时每隔这么久再看一次（取消、余额不足的中止不会漏看）

    def __init__(self, usd: float = 1.00, pages: int = 48, round1_pages: int = 40, llm_concurrency: int = 8,
                 extra_directions: int = 3, urls_per_direction: int = 4, search_max_uses: int = 3,
                 max_directions_hard: int = 16):
        self.usd_cap, self.pages_cap, self.round1_pages = usd, pages, round1_pages
        self.extra_directions = extra_directions
        self.urls_per_direction, self.search_max_uses = urls_per_direction, search_max_uses
        self.max_directions_hard = max_directions_hard
        self.directions = self._max_directions()
        self.usd_tokens = 0.0
        self.usd_search_fee = 0.0
        self.reserved = 0.0
        self.pages_used = 0
        self.n_calls = 0
        self.aborted = ""
        self.sem = threading.BoundedSemaphore(llm_concurrency)
        self._lock = threading.Lock()
        self._room = threading.Condition(self._lock)   # v2.10f：预扣退回、花费记入、中止时叫醒等着的预扣
        self._n_holds = 0                              # 在途的预扣份数
        self._tls = threading.local()                  # 这个线程当前占着的预扣（renew_current 用）
        self.n_waits, self.wait_s = 0, 0.0             # 等过在途调用的预扣次数、合计秒数（只有 wait_for_room 时记进 snapshot）

    @classmethod
    def for_model(cls, model: str, **kw) -> "Budget":
        """v2.10a：按这个模型的价格计价的预算（自带 key 的运行）。没有价格的模型抛 config.UnknownModel。"""
        price(model)
        b = cls(**kw)
        b.model = model
        b.directions = b._max_directions()
        return b

    @classmethod
    def typical_direction_usd(cls, model: str) -> float:
        """一个方向的典型花费：deepseek-flash 是实测的 TYPICAL_DIRECTION_USD；别的模型乘以 DIRECTION_PROFILE 按峰时价算的价格比例
        （含各家的搜索费），这样贵的模型第一轮方向少一些，上限照样守得住。"""
        if model == cls.REFERENCE_MODEL:
            return cls.TYPICAL_DIRECTION_USD
        return (cls.TYPICAL_DIRECTION_USD * cls.profile_usd(model, cls.DIRECTION_PROFILE)
                / cls.profile_usd(cls.REFERENCE_MODEL, cls.DIRECTION_PROFILE))

    @staticmethod
    def profile_usd(model: str, profile: dict) -> float:
        """一组 token（profile：hit / miss / out，可选 searches 次搜索）按这个模型的峰时价算的 USD。缓存的处理偏保守（见下）。
        typical_direction_usd 用它算价格比例；web-v0.9 网页的「每次运行的花费估计」（web/catalog.py）也用它。"""
        p = price(model)
        hit, miss, out = p["peak"]
        if p.get("prompt_cache") == "explicit":   # v2.10b Claude：不写 cache_control 就没有缓存，DeepSeek 命中的那部分按 base input 算
            hit = miss
        elif p.get("prompt_cache") == "implicit_write":   # v2.10c GPT：默认在 user 消息末尾写缓存，输入都按 30 分钟写入价（保守）
            hit = miss = p["cache_write_30m"]
        elif p.get("prompt_cache") == "implicit":   # v2.10d Kimi：自动缓存，但这里的命中率没测过，输入都按 miss / 5 分钟写入价（保守）
            hit = miss = max(miss, p.get("cache_write_5m", miss))
        return ((profile["hit"] * hit + profile["miss"] * miss + profile["out"] * out) / 1e6
                + profile.get("searches", 0) * search_fee_usd(model))

    def _max_directions(self) -> int:
        return max(1, min(self.max_directions_hard, self.round1_pages // self.urls_per_direction,
                          int(self.ROUND1_USD_SHARE * self.usd_cap / self.typical_direction_usd(self.model or MODEL))))

    def halt(self, reason: str) -> str:
        """v2.10a：立刻停下整次运行（余额不足）。之后每次预扣都抛 BudgetExceeded，各节点按预算中止的路径干净收尾
        （同网页的「取消」）。已经因为别的原因中止的，保留第一个原因。返回最终的中止原因。"""
        with self._lock:
            self.aborted = self.aborted or reason
            self._room.notify_all()
            return self.aborted

    @property
    def usd(self):
        return self.usd_tokens + self.usd_search_fee

    def add(self, rec: dict):
        with self._lock:
            self.n_calls += 1
            self.usd_tokens += float(rec.get("usd") or 0)
            self.usd_search_fee += float(rec.get("usd_search_fee_assumed") or 0)
            if self.usd > self.usd_cap and not self.aborted:
                self.aborted = f"usd cap {self.usd_cap} exceeded ({self.usd:.4f})"
            self._room.notify_all()

    def _room_for(self, amount: float) -> str:
        """在锁里调：等到放得下（返回 ""），或者返回放不下的原因。wait_for_room 时只因为在途的预扣放不下就等（在途的调用都在发 HTTP，
        一定会结束；本线程自己没有占着预扣：hold 不嵌套，renew 先退回自己那份）。"""
        t0 = None
        try:
            while True:
                if self.aborted:
                    return self.aborted
                if self.usd + self.reserved + amount <= self.usd_cap:
                    return ""
                if self.wait_for_room and self._n_holds > 0 and self.usd + amount <= self.usd_cap:
                    if t0 is None:
                        t0 = time.time()
                        self.n_waits += 1
                    self._room.wait(self.WAIT_POLL_S)
                    continue
                return (f"usd cap {self.usd_cap} would be exceeded "
                        f"(spent {self.usd:.4f} + in flight {self.reserved:.4f} + {amount:.4f})")
        finally:
            if t0 is not None:
                self.wait_s += time.time() - t0

    def _stack(self) -> list:
        st = getattr(self._tls, "stack", None)
        if st is None:
            st = self._tls.stack = []
        return st

    @contextmanager
    def hold(self, amount: float):
        """预扣 amount；已花 + 在途预扣 + amount 超过上限就抛 BudgetExceeded（v2.10f 自带 key 的运行：只是在途的预扣放不下时先等）。
        退出时退回预扣（实际花费已由 add 记入）。with 拿到的是这份预扣（_Hold）。"""
        with self._room:
            why = self._room_for(amount)
            if why:
                self.aborted = self.aborted or why
                raise BudgetExceeded(self.aborted)
            self.reserved += amount
            self._n_holds += 1
        h = _Hold(amount)
        st = self._stack()
        st.append(h)
        try:
            yield h
        finally:
            st.remove(h)
            with self._room:
                if h.live:
                    self.reserved -= h.amount
                    self._n_holds -= 1
                    h.live, h.amount = False, 0.0
                self._room.notify_all()

    def renew_current(self) -> bool:
        """v2.10f：这个线程当前那份预扣已经用掉（那次请求的实际花费已由 add 记入），换成同样大小的新一份，给同一次调用里的下一个请求
        （Claude 搜索的 pause_turn 续接）。先退回旧的那份再等，所以不会等自己。放不下就返回 False（调用方不发这个请求），不中止整次运行。
        不在任何预扣里时返回 True。"""
        st = self._stack()
        if not st:
            return True
        h = st[-1]
        with self._room:
            if h.live:
                self.reserved -= h.amount
                self._n_holds -= 1
                h.live, h.amount = False, 0.0
                self._room.notify_all()
            if self._room_for(h.size):
                return False
            self.reserved += h.size
            self._n_holds += 1
            h.live, h.amount = True, h.size
            return True

    @staticmethod
    def peak_rates(model: str, prompt_tokens: float) -> tuple:
        """预扣用的 (cache hit, 输入, 输出) 单价：峰时价；v2.10b 有按 prompt 长度分档的模型（Haiku 5.5），超过门槛按高价。"""
        p = price(model)
        lc = p.get("long_context")
        return lc["peak"] if lc and prompt_tokens > lc["threshold_tokens"] else p["peak"]

    @staticmethod
    def reserve_rates(model: str, prompt_tokens: float) -> tuple:
        """预扣用的 (cache hit, 每个输入 token 的最坏单价, 输出)：peak_rates；v2.10c 默认会写缓存的模型（GPT，prompt_cache =
        implicit_write）输入按 30 分钟写入价（1.25 倍 input 价，同一档 long context 的写入价）；v2.10d Kimi（implicit）按 miss 和
        5 分钟写入价中较高的。DeepSeek / Claude 和 peak_rates 相同。model 是计价 id（ModelSpec.price_id）。"""
        p = price(model)
        hit, miss, out = Budget.peak_rates(model, prompt_tokens)
        if p.get("prompt_cache") == "implicit_write":
            lc = p.get("long_context")
            miss = max(miss, (lc if lc and prompt_tokens > lc["threshold_tokens"] else p)["cache_write_30m"])
        elif p.get("prompt_cache") == "implicit":   # v2.10d Kimi：默认 5 分钟档写缓存（K3 的写入价 = miss 价；K2 没有单列）
            miss = max(miss, p.get("cache_write_5m", miss))
        return hit, miss, out

    @staticmethod
    def llm_reserve(prompt_chars: int, max_tokens: int, model: str | None = None) -> float:
        """一次 JSON 调用的预扣：输入按字符数换成 token（v2.10f：DeepSeek 照旧每个 token 2 个字符，别家按 1 个，
        providers.reserve_chars_per_token），输出按发出的 max_tokens，都按峰时价（reserve_rates）。"""
        m = model or MODEL
        tokens_in = prompt_chars / reserve_chars_per_token(m)
        hit, miss, out = Budget.reserve_rates(m, tokens_in)
        return (tokens_in * miss + max_tokens * out) / 1e6

    def search_reserve(self) -> float:
        """一次搜索请求的预扣：search_input_tokens 个输入 token + 发出的 max_tokens 个输出 token + (2 x max_uses + 2) 次搜索费。
        v2.10f：Claude 的 pause_turn 续接每次另预扣同样一份（Searcher.renew -> renew_current）。"""
        m = self.model or MODEL
        n_in = self.SEARCH_INPUT_TOKENS if self.search_input_tokens is None else self.search_input_tokens
        hit, miss, out = self.reserve_rates(m, n_in)
        tokens = MAX_TOKENS["search"] if self.search_tokens is None else self.search_tokens
        return (n_in * miss + tokens * out) / 1e6 + (2 * self.search_max_uses + 2) * search_fee_usd(m)

    def reserve_page(self, round_no: int) -> bool:
        cap = self.round1_pages if round_no == 1 else self.pages_cap
        with self._lock:
            if self.pages_used >= cap:
                return False
            self.pages_used += 1
            return True

    def release_page(self):
        with self._lock:
            self.pages_used -= 1

    def snapshot(self):
        out = {"usd_total_assumed": round(self.usd, 4), "usd_tokens": round(self.usd_tokens, 4),
               "usd_search_fee_assumed": round(self.usd_search_fee, 4), "usd_cap": self.usd_cap,
               "pages_used": self.pages_used, "pages_cap": self.pages_cap, "round1_pages": self.round1_pages,
               "max_directions": self.directions, "urls_per_direction": self.urls_per_direction,
               "n_calls_logged": self.n_calls, "aborted": self.aborted}
        if self.wait_for_room:   # v2.10f：只有自带 key 的运行记（命令行的 state.json 不变）
            out.update(waited_for_room=self.n_waits, wait_s=round(self.wait_s, 1),
                       search_input_tokens_reserved=self.search_input_tokens)
        return out


def configure_byok(b: Budget, model: str, level: str, adapter) -> Budget:
    """v2.10f：自带 key 的运行的预扣设置（pipeline.Context 和网页的花费估计 web/catalog.py 共用，两边一致）：
    搜索预扣按实际发出的 max_tokens（含思考余量；「生成查询词」的 provider 按那次调用的 max_tokens）、模型自己搜的 provider 输入按 p99；
    预扣放不下只是因为在途的预扣时等（wait_for_room）。"""
    queries = getattr(adapter, "search_mode", "model") == "queries"
    b.search_tokens = tokens_for_model(model, level, "search", SEARCH_QUERIES_MAX_TOKENS if queries else MAX_TOKENS["search"])[1]
    b.search_input_tokens = Budget.SEARCH_INPUT_TOKENS if queries else Budget.SEARCH_INPUT_TOKENS_BYOK
    b.wait_for_room = True
    return b


class AgentLLM(LLM):
    """llm.LLM 加两件事：调用前先占一个并发名额、再查预算；每条日志同时计入预算。"""

    def __init__(self, calls_path, budget: Budget, spec=None):
        super().__init__(calls_path=calls_path, spec=spec)
        self.budget = budget

    def _log(self, rec: dict):
        super()._log(rec)
        if "usd" in rec:
            self.budget.add(rec)

    def ask(self, system: str, user: str, *, role: str, qid: str, max_tokens: int = MAX_TOKENS["final"], tries: int = 2):
        """返回 (dict|None, error)。输出无效时带着错误信息重试一次。"""
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        err = None
        # 预扣按发出去的 max_tokens 算：有 ModelSpec 时含思考余量；没有时照旧只按 max_tokens（和 v2.9b 相同）
        reserve_tokens = max_tokens if self.spec is None else self.effort_and_tokens(role, max_tokens)[1]
        for attempt in range(1, tries + 1):
            need = Budget.llm_reserve(sum(len(m["content"]) for m in msgs), reserve_tokens, self.budget.model)
            with self.budget.sem, self.budget.hold(need):
                try:
                    out, text, err = self.json_call(msgs, arm=role, qid=qid, attempt=attempt, max_tokens=max_tokens)
                except BalanceExhausted as e:   # v2.10a：余额不足 -> 整次运行停下（预算中止的路径）
                    raise BudgetExceeded(self.budget.halt(str(e))) from None
                except TransportError as e:
                    return None, f"transport: {e}"
            if out is not None:
                return out, None
            ask_again = (f"Your reply was cut off at the output limit ({err}). Reply again with one complete, valid JSON "
                         "object that is shorter: keep notes and reasons brief."
                         if "truncated" in (err or "") else f"Your reply was rejected: {err}. Reply again with one valid JSON object.")
            msgs = msgs[:2] + [{"role": "assistant", "content": (text or "")[:2000]}, {"role": "user", "content": ask_again}]
        return None, err


class Context:
    """一题一个：预算、LLM、SEARCHER、哨兵、as_of。图的节点通过闭包拿到它，不放进 LangGraph state。
    v2.10a：spec（providers.ModelSpec）= 自带 key 的运行：LLM、SEARCHER 用它的 provider / 模型 / key / 思考档位，
    预算按它的模型计价、上限是它的 usd_cap，Jev 对照臂（服务器主人的 TypeSafe key）不跑。None = 命令行 / 回测，和以前相同。"""

    spec = None   # 类级默认：测试会用 object.__new__ 绕过 __init__

    def __init__(self, qid: str, question: str, as_of: str, calls_path, leak_value=None, budget: Budget | None = None,
                 ablate_own_history: bool = False, spec=None):
        self.spec = spec
        self.qid, self.question, self.as_of_s = qid, question, as_of
        self.as_of = date.fromisoformat(as_of)
        self.ablate_own_history = ablate_own_history  # 回测消融：见 ablation.py
        self.check_published = False  # v2.4「答案已公布」检查（published.py）：只有 run.prepare_run 在真实使用时打开
        self.live_fetch = False  # v2.5 直接抓 live 页（fetch_live）：同上，只在真实使用时打开
        self.early = None        # v2.5 提前停（published.EarlyWatch）：同上
        # v2.10d：按 spec.price_id 计价（Kimi 国内站是 "kimi-k3@cn"，其余就是模型名）
        self.budget = budget or (Budget() if spec is None else Budget.for_model(spec.price_id, usd=spec.usd_cap))
        self.calls_path = calls_path
        if spec is not None:   # v2.10b：搜索也开思考的模型（Opus 5.5 / Fable 5.1）预扣按带余量的 max_tokens
            # v2.10d：「生成查询词 + 搜索接口」的 provider（Kimi），搜索里唯一的模型调用是生成查询词，预扣按它发出的 max_tokens
            # v2.10f：搜索输入按 p99、放不下只因为在途时等（configure_byok）
            configure_byok(self.budget, spec.model, spec.thinking, spec.adapter)
        self.llm = AgentLLM(calls_path, self.budget, spec=spec)
        self.searcher = Searcher(log=self.llm._log, spec=spec)
        if spec is not None:   # v2.10f：Claude 搜索的 pause_turn 续接之前再预扣一份（放不下就不续）
            self.searcher.renew = self.budget.renew_current
        # 哨兵只在代码里用：真值（和其他 as_of 之后才公布的已知值）不进任何 prompt。可以是一个数或一组数
        self.leak_patterns = ev.leak_patterns(leak_value) if leak_value else []
        self.leak_values = leak_value   # v2.8p：抽取员读出的数（单词、分数）也按数值和它比，见 _process_page
        self.progress = None  # 可选的进度回调 progress(event: dict)，网页用；只读通知，不影响运行


def redact(ctx, text):
    """v2.10a 兜底：自带 key 的运行里，把文字中出现的 key 换成 ***（正常路径上 key 不会进任何错误文字）。"""
    spec = getattr(ctx, "spec", None)
    return text if spec is None else spec.redact(text)


def _emit(ctx, **event):
    """把进度事件交给 ctx.progress（没有就跳过）。回调出任何错都吞掉：进度显示不能影响运行。"""
    cb = getattr(ctx, "progress", None)
    if cb is not None:
        try:
            cb(event)
        except Exception:  # noqa: BLE001
            pass


def verify_point(raw: dict, text_n: str, as_of: date, page_date, allow_no_period: bool, url: str = "") -> tuple:
    """返回 (point|None, reason)。quote 逐字在页面里、value_as_written 在 quote 里、数字和倍数由代码解析、日期 <= as_of。"""
    if not isinstance(raw, dict):
        return None, "not an object"
    q, vw = ev.norm(str(raw.get("quote") or "")), ev.norm(str(raw.get("value_as_written") or ""))
    if not q or not vw:
        return None, "missing quote or value_as_written"
    if len(q) > 400:
        return None, "quote longer than 400 chars"
    span = ev.quote_span(q, text_n)
    if span is None:
        return None, "quote not found verbatim in page (elisions must skip <= 150 chars within one sentence)"
    i = ev.find_value(q, vw)
    if i < 0:
        return None, "value_as_written not in quote as a whole number"
    sw = str(raw.get("scale_word") or "")
    # v2.8o：阿拉伯数字写法照旧由代码解析（精确）。代码解析不了的写法（单词、分数、区间：披萨题 NHANES 的
    # 「males had four ... three slices」因此丢过）用抽取员给的 number（区间给 low / high），算之前由模型逐个核对
    # （value_check.py）。用户 10-18 选的：探针里模型核对阿拉伯数字会错放（4,774.10 读成 477410）也会误杀，单词写法 5 轮全对
    reading, lo_v, hi_v = None, None, None
    try:
        value, is_pct = ev.parse_value(vw, sw)
    except ValueError as e:
        if not ev.has_reading(raw):
            return None, f"number: {e}"
        try:
            value, lo_v, hi_v, is_pct, reading = ev.read_reading(raw, vw, sw)
        except ValueError as e2:
            return None, f"number: {e2}"
    if cut := ev.cjk_fragment(q, vw, sw):   # v2.6e：只写了更大的中日韩数字的一截（1億3000万 里的 1億3000）就丢，不静默读错
        return None, f"number: {cut}"
    header = text_n[max(0, span[0] - ev.HEADER_WINDOW_CHARS):span[0]]
    basis = ev.scale_supported(sw, q, header, vw)
    if not basis:
        return None, f"scale word {sw!r} not supported by quote or table header"
    why = ev.date_check(raw, as_of, page_date, allow_no_period=allow_no_period)
    if why:
        return None, why
    # 抽取员给的期间年份必须在页面正文或网址里出现过（v2.1b 韩国题：旧页面上「7 月（报告当年）」被标成了 2026 年 7 月）
    # v2.6e：页面只写纪年（令和8年、民國115年、台湾的「115年」）时也算出现过（evidence.era_years）；period_end 本身写成纪年
    # （parse_date 现在认「令和8年3月」）时换成公历年再查，不让这种写法绕过检查
    pe_s = str(raw.get("period_end") or "")
    y = pe_s[:4]
    if not y.isdigit() and not pe_s[:1].isascii() and (pe := ev.parse_date(pe_s, end=True)):
        y = str(pe.year)
    if y.isdigit() and y not in text_n and y not in url and not (y.isdecimal() and int(y) in ev.era_years(text_n)):
        return None, f"period year {y} does not appear in the page text or URL (likely mis-dated)"
    unit, unit_as_written = ("%", None) if is_pct else (str(raw.get("unit") or ""), None)
    if not is_pct:
        paired = _pair_unit(unit, vw, sw, q, header)
        if isinstance(paired, str):
            return None, f"unit: {paired}"
        if paired:
            unit_as_written, unit, g, sw2, b2 = unit, *paired
            if g != 1:   # 倍数只写在 unit 里、原文有依据：挪到数上
                value, sw, basis = value * g, sw2, b2
                lo_v, hi_v = (lo_v * g, hi_v * g) if lo_v is not None else (None, None)
    unit = unit[:60]
    lo = max(0, min(i - 80, len(q) - QUOTE_STORE_CHARS))
    point = {"name": str(raw.get("name") or "")[:160], "value": value, "value_as_written": vw, "scale_word": sw,
             "scale_basis": basis, "unit": unit, "period_start": str(raw.get("period_start") or ""),
             "period_end": str(raw.get("period_end") or ""),
             "published_at_if_visible": str(raw.get("published_at_if_visible") or ""),
             "quote": q[lo:lo + QUOTE_STORE_CHARS]}
    if unit_as_written is not None:
        point["unit_as_written"] = unit_as_written[:120]
    if reading is not None:
        point.update(reading=reading, value_check="pending")
        if lo_v is not None:
            point.update(value_low=lo_v, value_high=hi_v)
    return point, ""


def _pair_unit(unit: str, vw: str, sw: str, q: str, header: str):
    """v2.8r：一个点的数和单位必须成对（XBRL：金额以元为单位；SDMX：UNIT_MEASURE 不含倍数）。
    - 代码已乘过倍数 f（scale_word 或写法末尾的 万 / million）：unit 里同一个倍数去掉（「万元 (10,000 CNY)」->「元 (CNY)」）；
      unit 写的是别的倍数就返回原因（调用方丢点）。恒顺 v2.8p 因为没去掉，单位核对又乘了 10^4。
    - 代码没乘、倍数只写在 unit 里（「万元」「£ million」）：倍数在 quote 或表头有依据（scale_supported）就挪到数上，没依据照旧。
    返回 None（不用改）、(新 unit, 要乘的倍数, 新 scale_word, 新 scale_basis) 或原因字符串。比率分母（per 1,000 women、每万人）不动。"""
    hits = ev.unit_multipliers(unit)
    if not hits:
        return None
    try:
        f = ev.split_multiplier(vw, "" if ev.norm(sw).lower() in ev.PERCENT else sw)[1]
    except ValueError:
        f = 1.0
    if f != 1:
        new, why = ev.strip_unit_multiplier(unit, f)
        return why or (new, 1.0, sw, None)
    gs = {g for _, g in hits}
    word = ev.SCALE_FOR_FACTOR.get(gs.pop()) if len(gs) == 1 else None
    b = ev.scale_supported(word, q, header, vw) if word else ""
    if not b:
        return None
    new, _ = ev.strip_unit_multiplier(unit, ev.SCALES[ev._cjk_scale_word(word)])
    return new, ev.SCALES[ev._cjk_scale_word(word)], word, b


def _process_page(ctx: Context, target: dict, d: dict, round_no: int, page: dict, text, out: dict,
                  allow_no_period: bool) -> list:
    """取到的一页：哨兵 -> 抽取 -> 代码核对，记进 out。返回这一页核对通过的点（v2.5 提前停检查用）。"""
    _emit(ctx, kind="page", direction_id=d["id"], status=page.get("status"))
    if page["status"] == "dropped":
        ctx.budget.release_page()
        out["pages"].append(page)
        return []
    hits = ev.leak_scan(text, ctx.leak_patterns)
    page["leak_hits"] = hits
    if hits:
        page["status_detail"] = "excluded: leak sentinel hit"
        out["pages"].append(page)
        return []
    sent = text[:MAX_CHARS_TO_EXTRACTOR]
    page.update(chars_sent=len(sent), truncated=len(text) > len(sent),
                late_dates_in_sent_text=[x.isoformat() for x in ev.late_dates(sent, ctx.as_of, date.today())][:10])
    res, err = ctx.llm.ask(EXTRACT_SYSTEM, EXTRACT_USER.format(
        text=sent, **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end")},
        hypothesis=str(d.get("hypothesis", ""))[:600], data_to_find=str(d.get("data_to_find", ""))[:600]),
        role=f"extract:{d['id']}", qid=ctx.qid, max_tokens=MAX_TOKENS["extract"])
    page["extract_error"] = err
    text_n = ev.norm(sent)
    raws = (res or {}).get("points") or []
    page["n_points_raw"] = len(raws) if isinstance(raws, list) else 0
    new = []
    for j, r in enumerate(raws if isinstance(raws, list) else []):
        pd = date.fromisoformat(page["page_date"]) if page.get("page_date") else None
        p, why = verify_point(r, text_n, ctx.as_of, pd, allow_no_period, url=page["url"])
        base = {"direction_id": d["id"], "round": round_no, "source_url": page["url"], "via": page["status"],
                "page_date": page.get("page_date"), "snapshot_ts": page.get("snapshot_ts"), "order": (len(out["pages"]), j)}
        if p is None:
            out["dropped_points"].append({**base, "reason": why, "name": str((r or {}).get("name", ""))[:120]
                                          if isinstance(r, dict) else "", "value_as_written": str((r or {}).get("value_as_written", ""))[:40]
                                          if isinstance(r, dict) else ""})
        else:
            new.append({**base, **p, "verified_by": "quote_in_page"})
            out["points"].append(new[-1])
    # v2.8p：页面哨兵只搜数字写法；抽取员读出的数（单词、分数写的：two million）也按数值和登记值比，命中就整页作废
    hit = [p for p in new if p.get("reading") and any(ev.leak_number_hit(p.get(k), getattr(ctx, "leak_values", None))
                                                     for k in ("value", "value_low", "value_high"))]
    if hit:
        page["leak_hits"] = [f'{p["value_as_written"]} (read as {p["value"]:g})' for p in hit]
        page["status_detail"] = "excluded: leak sentinel hit (number read from words)"
        out["points"][:] = [p for p in out["points"] if not any(p is q for q in new)]
        new = []
    page["n_points_verified"] = len(new)
    out["pages"].append(page)
    _emit(ctx, kind="extracted", direction_id=d["id"], n_verified=len(new))
    return new


def _timed_live(url: str, as_of: date, qid: str) -> dict:
    """fetch_live 加计时（fetch_at = 开始时刻 UTC，fetch_s = 用时，含按 host 限速排队的时间）。"""
    t0, at = time.time(), datetime.now(timezone.utc).isoformat(timespec="seconds")
    page = fetch_live(url, as_of, qid)
    page.update(fetch_at=at, fetch_s=round(time.time() - t0, 2))
    return page


def _live_pages(ctx: Context, target: dict, d: dict, round_no: int, urls: list, out: dict, allow_no_period: bool):
    """v2.5 真实使用：这个方向的 URL 同时开抓（fetch_live；同一 host 的请求由 net 的限速排队，robots 照旧），按 URL 顺序
    抽取（点的编号因此可复现）。每页核对完的点交给 ctx.early；确认了已公布的值就不再抽取，没开始的抓取取消。"""
    b, w = ctx.budget, getattr(ctx, "early", None)
    ok = [b.reserve_page(round_no) for _ in urls]
    pool = ThreadPoolExecutor(max_workers=max(1, sum(ok)), thread_name_prefix=f"fetch-{d['id']}")
    futs = [pool.submit(_timed_live, u, ctx.as_of, ctx.qid) if k else None for u, k in zip(urls, ok)]
    def stopped(i):   # 已确认已公布的值：这一页和后面的页不再抽取，名额退回
        if w is None or not w.stop.is_set():
            return False
        for _ in [f for f in futs[i:] if f is not None]:
            b.release_page()
        out["stopped"] = w.stop_reason
        return True

    try:
        for i, (url, fut) in enumerate(zip(urls, futs)):
            if fut is None:
                out["pages"].append({"url": url, "status": "dropped", "reason": "page cap reached"})
                continue
            if stopped(i):
                break
            page = fut.result()
            if stopped(i):   # v2.5.1：等这一页的时候别的子 agent 已经确认了（published2 的 d5 多抽了一页）
                break
            new = _process_page(ctx, target, d, round_no, page, page.pop("text", None), out, allow_no_period)
            if w is not None and new:
                w.offer(ctx.llm, ctx.qid, target, ctx.as_of_s, ctx.as_of, new)
    finally:
        pool.shutdown(wait=False, cancel_futures=True)


class _Stopped(Exception):
    """v2.5 提前停：这个方向开始搜索之前，已经确认了已公布的值。"""


def run_direction(ctx: Context, target: dict, d: dict, round_no: int) -> dict:
    """一个子 agent：搜索（只取 URL）-> 逐个取快照 -> 哨兵 -> 抽取 -> 代码核对。异常和预算耗尽都在这里收住。
    v2.5 真实使用：同时直接抓 live 页（_live_pages）；ctx.early 确认了已公布的值以后，还没做的步骤不再做（out["stopped"]）。"""
    t0 = time.time()
    b = ctx.budget
    w = getattr(ctx, "early", None)
    out = {"direction_id": d["id"], "round": round_no, "search": {}, "pages": [], "points": [], "dropped_points": []}
    _emit(ctx, kind="direction_start", direction_id=d["id"], round=round_no)
    try:
        if w is not None and w.stop.is_set():
            out["stopped"] = w.stop_reason
            raise _Stopped
        prompt = SEARCH_USER.format(cap=b.urls_per_direction, as_of=ctx.as_of_s,
                                    hints="; ".join(map(str, d.get("search_hints") or []))[:400],
                                    **{k: target.get(k, "") for k in ("what", "unit", "period_start", "period_end", "publisher")},
                                    **{k: str(d.get(k, ""))[:600] for k in ("category", "perspective", "hypothesis", "data_to_find")})
        with b.sem, b.hold(b.search_reserve()):
            try:
                s = ctx.searcher.search(prompt, role=f"search:{d['id']}", qid=ctx.qid, max_uses=b.search_max_uses,
                                        cap=b.urls_per_direction)
            except BalanceExhausted as e:   # v2.10a：余额不足 -> 整次运行停下
                raise BudgetExceeded(b.halt(str(e))) from None
        out["search"] = s
        _emit(ctx, kind="searched", direction_id=d["id"], n_urls=len(s.get("urls", [])[: b.urls_per_direction]))
        allow_no_period = d.get("category") == "base_rates"
        urls = s.get("urls", [])[: b.urls_per_direction]
        # v2.6c 回测泄漏护栏（D3）：查询词里出现登记值（哨兵的写法），这个方向作废：不取页、不重搜，命中的写法记进
        # search.voided。真实使用没有登记值（ctx.leak_patterns 为空），不受影响
        voided = sorted({h for q in s.get("queries") or [] for h in ev.leak_scan(str(q), ctx.leak_patterns)})
        if voided:
            out["search"] = {**s, "voided": voided}
        elif w is not None and w.stop.is_set():
            out["stopped"] = w.stop_reason
        elif getattr(ctx, "live_fetch", False):
            _live_pages(ctx, target, d, round_no, urls, out, allow_no_period)
        else:
            for url in urls:
                if not b.reserve_page(round_no):
                    out["pages"].append({"url": url, "status": "dropped", "reason": "page cap reached"})
                    continue
                page = fetch_page(url, ctx.as_of, ctx.qid)
                _process_page(ctx, target, d, round_no, page, page.pop("text", None), out, allow_no_period)
    except _Stopped:
        pass
    except BudgetExceeded as e:
        out["aborted"] = str(e)
    except Exception as e:  # noqa: BLE001  一个方向的意外错误不拖垮整题，记下来
        out["error"] = redact(ctx, f"{type(e).__name__}: {e}")[:300]
    out["wall_s"] = round(time.time() - t0, 1)
    _emit(ctx, kind="direction_done", direction_id=d["id"], round=round_no, n_points=len(out["points"]),
          stopped=out.get("error") or out.get("aborted") or out.get("stopped"))
    return out


def dumps(x) -> str:
    return json.dumps(x, ensure_ascii=False, default=str)

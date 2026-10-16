"""HTTP：统一 User-Agent；每个 host 两次请求的开始时间至少隔 1 秒（Wayback 1.5 秒且单连接；robots.txt 给了更长的
Crawl-delay 就按它）；robots.txt 用我们自己的 UA 去取并遵守，取的时候跟随重定向，按 (scheme, host) 缓存；
页面重定向手动跟随（每一跳都过 robots 和限速）；gzip/deflate 由代码解压；连接失败退避重试。只用标准库。"""
import gzip
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import zlib

UA = "triangulate-agent/0.1 (research prototype)"
MIN_INTERVAL_S = 1.0
MAX_BYTES = 6_000_000
# 第一次运行时 Wayback 在并发请求下出现过连接被拒（WinError 10061），所以对它单连接、间隔放宽到 1.5 秒
HOST_INTERVAL = {"web.archive.org": 1.5}
HOST_CONCURRENCY = {"web.archive.org": 1}
DEFAULT_CONCURRENCY = 4
CONNECT_BACKOFF_S = (10, 30)
MAX_ROBOTS_REDIRECTS = 5
MAX_CRAWL_DELAY_S = 30   # robots.txt 的 Crawl-delay 照办（取 max(它, 1 秒)）；超过 30 秒的 host 不抓
# v2.5 真实使用直接抓 live 页（fetch.fetch_live）：超时短、不重试、不退避；robots 只取一次（取不到按全部禁止）。
# 限速（每个 host 两次请求的开始至少隔 1 秒、Crawl-delay）和 robots 规则与回测相同
LIVE_TIMEOUT_S = 15
LIVE_ROBOTS_TIMEOUT_S = 10
ROBOTS_WAITS = (0, 10)   # 取 robots.txt：连接失败重试一次（等 10 秒）


class HostLimiter:
    def __init__(self, interval: float = MIN_INTERVAL_S):
        self.interval = interval
        self._lock = threading.Lock()
        self._next = {}
        self._sems = {}
        self._custom = {}

    def set_interval(self, host: str, seconds: float):
        """robots.txt 的 Crawl-delay：这个 host 的间隔取 max(默认, Crawl-delay)。"""
        with self._lock:
            self._custom[host] = max(self._custom.get(host, 0.0), float(seconds))

    def sem(self, host: str):
        with self._lock:
            if host not in self._sems:
                self._sems[host] = threading.BoundedSemaphore(HOST_CONCURRENCY.get(host, DEFAULT_CONCURRENCY))
            return self._sems[host]

    def wait(self, host: str):
        with self._lock:
            now = time.monotonic()
            t = max(now, self._next.get(host, 0.0))
            self._next[host] = t + max(self.interval, HOST_INTERVAL.get(host, 0.0), self._custom.get(host, 0.0))
        if t > now:
            time.sleep(t - now)


LIMITER = HostLimiter()
_ROBOTS = {}
_ROBOTS_LOCK = threading.Lock()
_HOST_LOCKS = {}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


_OPENER = urllib.request.build_opener(_NoRedirect)


class Blocked(RuntimeError):
    """robots.txt 不允许。"""


def decompress(body: bytes, headers: dict) -> bytes:
    """Wayback 的 id_ 原样返回网站当年的字节，可能是 gzip 压缩的（即使我们请求 identity）。按头或魔数解压。"""
    enc = (headers.get("Content-Encoding") or "").lower()
    try:
        if "gzip" in enc or body[:2] == b"\x1f\x8b":
            return gzip.decompress(body)
        if "deflate" in enc:
            try:
                return zlib.decompress(body)
            except zlib.error:
                return zlib.decompress(body, -15)
    except (OSError, EOFError, zlib.error):
        return body
    return body


def _raw_get(url: str, timeout: float):
    host = urllib.parse.urlsplit(url).netloc.lower()
    with LIMITER.sem(host):
        return _raw_get_inner(url, host, timeout)


def _raw_get_inner(url: str, host: str, timeout: float):
    LIMITER.wait(host)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    try:
        with _OPENER.open(req, timeout=timeout) as r:
            h = dict(r.headers)
            return r.status, decompress(r.read(MAX_BYTES), h), h
    except urllib.error.HTTPError as e:
        try:
            body = e.read(MAX_BYTES)
        except Exception:  # noqa: BLE001
            body = b""
        return e.code, body, dict(e.headers or {})


def _fetch_robots(url: str, timeout: float = 30, waits=ROBOTS_WAITS):
    """取 robots.txt，跟随重定向（RFC 9309：至少跟 5 跳；每一跳都过限速）。返回 (status, body)。
    超过 5 跳按「取不到」处理，返回 599（下面按全部禁止）。"""
    for _ in range(MAX_ROBOTS_REDIRECTS + 1):
        status, body = 599, b""
        for wait_s in waits:  # 连接失败重试一次，再失败按 RFC 9309 视为全部禁止
            time.sleep(wait_s)
            try:
                status, body, headers = _raw_get(url, timeout=timeout)
                break
            except (urllib.error.URLError, TimeoutError, OSError):
                headers = {}
                continue
        if status in (301, 302, 303, 307, 308) and headers.get("Location"):
            url = urllib.parse.urljoin(url, headers["Location"])
            continue
        return status, body
    return 599, b""


def _robots_for(scheme: str, host: str, timeout: float = 30, waits=ROBOTS_WAITS):
    key = (scheme, host)  # http 和 https 分开缓存：http 的 robots.txt 可能只是 301 到 https
    with _ROBOTS_LOCK:
        lock = _HOST_LOCKS.setdefault(key, threading.Lock())
    with lock:  # 每个 (scheme, host) 只取一次 robots.txt；不同 host 互不阻塞
        if key in _ROBOTS:
            return _ROBOTS[key]
        rp = urllib.robotparser.RobotFileParser()
        status, body = _fetch_robots(f"{scheme}://{host}/robots.txt", timeout, waits)
        if status == 200:
            rp.parse(body.decode("utf-8", "replace").splitlines())
        elif status in (401, 403) or status >= 500:
            rp.disallow_all = True   # RFC 9309：取不到（5xx / 网络错误 / 重定向太多）按全部禁止处理
        else:
            rp.allow_all = True      # 404 等：没有 robots.txt，按惯例全部允许
        try:
            cd = float(rp.crawl_delay(UA) or 0)
        except (TypeError, ValueError):
            cd = 0.0
        if cd > MAX_CRAWL_DELAY_S:
            rp.disallow_all = True   # 要求的间隔太长，这个 host 干脆不抓
        elif cd > 0:
            LIMITER.set_interval(host, cd)
        _ROBOTS[key] = rp
        return rp


def robots_allowed(url: str, timeout: float = 30, waits=ROBOTS_WAITS) -> bool:
    p = urllib.parse.urlsplit(url)
    return _robots_for(p.scheme or "https", p.netloc.lower(), timeout, waits).can_fetch(UA, url)


def get(url: str, timeout: float = 60, max_redirects: int = 4, retries: int = 2, backoff=CONNECT_BACKOFF_S,
        robots_timeout: float = 30, robots_waits=ROBOTS_WAITS):
    """返回 (status, body, headers, final_url)。robots 不允许时抛 Blocked。429/503 退避重试。"""
    for _ in range(max_redirects + 1):
        if not robots_allowed(url, robots_timeout, robots_waits):
            raise Blocked(url)
        for attempt in range(retries + 1):
            try:
                status, body, headers = _raw_get(url, timeout)
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if attempt < len(backoff) and not isinstance(getattr(e, "reason", None), str):
                    time.sleep(backoff[attempt])
                    continue
                raise
            if status in (429, 503) and attempt < retries:
                ra = headers.get("Retry-After", "")
                time.sleep(min(float(ra), 30) if ra.isdigit() else 8 * (attempt + 1))
                continue
            break
        if status in (301, 302, 303, 307, 308) and headers.get("Location"):
            url = urllib.parse.urljoin(url, headers["Location"])
            continue
        return status, body, headers, url
    return status, body, headers, url


def get_live(url: str):
    """v2.5 真实使用的 live 页：超时短（LIVE_TIMEOUT_S）、连接失败和 429/503 都不重试；robots 取一次、超时
    LIVE_ROBOTS_TIMEOUT_S。robots 规则、手动跟随重定向（每一跳都过 robots 和限速）、每个 host 的限速与 get 相同。"""
    return get(url, timeout=LIVE_TIMEOUT_S, retries=0, backoff=(), robots_timeout=LIVE_ROBOTS_TIMEOUT_S, robots_waits=(0,))

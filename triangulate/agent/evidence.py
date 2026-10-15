"""证据层的纯函数：数字解析、quote 原文核对、日期过滤、泄漏哨兵。全部由代码完成，不交给模型。"""
import calendar
import re
import unicodedata
from datetime import date

# ---------- 文本规范化 ----------
_TRANS = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-",
                        "−": "-", " ": " ", " ": " ", " ": " "})
_WS = re.compile(r"\s+")


def norm(s: str) -> str:
    """NFKC + 弯引号/破折号/不换行空格统一 + 空白折叠。大小写保留（核对是逐字的）。"""
    return _WS.sub(" ", unicodedata.normalize("NFKC", s or "").translate(_TRANS)).strip()


def quote_in_text(quote: str, text_norm: str) -> bool:
    """quote 在规范化后的页面文字里逐字出现。允许模型用 ... / … 省略中间部分：每段都必须按顺序逐字出现。"""
    parts = [p.strip() for p in re.split("\\.\\.\\.|…", norm(quote)) if p.strip()]
    if not parts:
        return False
    pos = 0
    for p in parts:
        i = text_norm.find(p, pos)
        if i < 0:
            return False
        pos = i + len(p)
    return True


# ---------- 数字与倍数词 ----------
SCALES = {"": 1.0, "none": 1.0, "hundred": 1e2, "thousand": 1e3, "thousands": 1e3, "k": 1e3,
          "million": 1e6, "millions": 1e6, "m": 1e6, "mn": 1e6, "mln": 1e6,
          "billion": 1e9, "billions": 1e9, "bn": 1e9, "b": 1e9, "trillion": 1e12, "trillions": 1e12, "tn": 1e12}
PERCENT = {"%", "percent", "per cent", "pct"}
_NUM = re.compile(r"(?<![\d.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")
_WORD_SCALE = re.compile(r"^\s*(hundred|thousand|million|billion|trillion)s?\b", re.I)
_ABBR_SCALE = re.compile(r"^(k|m|mn|mln|bn|b|tn)\b", re.I)  # 只认紧贴数字的缩写：4.8M、$5bn


def parse_value(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (数值, 是否百分数)。数值 = 原文数字 x 倍数；只做这一次乘法。
    倍数可来自原文数字本身（"4.8 million"）或模型填的 scale_word；两者都有且不一致就报错。"""
    s = norm(value_as_written)
    m = _NUM.search(s)
    if not m:
        raise ValueError("no number in value_as_written")
    rest = s[m.end():]
    if _NUM.search(rest):
        raise ValueError("more than one number in value_as_written")
    num = float(m.group().replace(",", ""))
    if s[:m.start()].strip().startswith("(") and rest.strip().startswith(")"):
        num = -num  # 会计写法 (1,234)
    text_scale, is_pct = None, False
    if rest.strip().startswith("%") or rest.strip().lower().startswith(("percent", "per cent")):
        is_pct = True
    elif (w := _WORD_SCALE.match(rest)) or (w := _ABBR_SCALE.match(rest)):
        text_scale = w.group(1).lower()
    sw = norm(scale_word).lower()
    if sw in PERCENT:
        is_pct, sw = True, ""
    if sw not in SCALES:
        raise ValueError(f"unknown scale word {scale_word!r}")
    if text_scale and sw and SCALES[sw] != SCALES[text_scale]:
        raise ValueError(f"scale conflict: {text_scale!r} in value vs {scale_word!r}")
    factor = SCALES[text_scale or sw]
    return num * factor, is_pct


def scale_supported(scale_word: str, quote_n: str, text_n: str) -> str:
    """倍数词必须有原文依据：在 quote 里，或页面里有 "in thousands" / "(millions)" 之类的表头。返回依据，否则空串。"""
    sw = norm(scale_word).lower()
    if sw in ("", "none") or sw in PERCENT:
        return "none_needed"
    base = sw.rstrip("s")
    forms = {sw, base, base + "s"}
    if any(re.search(rf"(?<![A-Za-z]){re.escape(f)}(?![A-Za-z])", quote_n, re.I) for f in forms):
        return "quote"
    if re.search(rf"(in|\()\s*{re.escape(base)}s?\b", text_n, re.I):
        return "page_header"
    return ""


# ---------- 日期 ----------
_MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
_MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})


def parse_date(s, end: bool = False):
    """接受 YYYY-MM-DD / YYYY-MM / YYYY / "August 2025" / "Aug 5, 2025"。end=True 时不完整日期取期末。"""
    if not s or not isinstance(s, str):
        return None
    s = s.strip()
    m = re.fullmatch(r"(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?(?:T.*)?", s)
    if m:
        y, mo, d = int(m.group(1)), m.group(2), m.group(3)
    else:
        m = re.fullmatch(r"([A-Za-z]+)\.?\s+(?:(\d{1,2}),?\s+)?(\d{4})", s)
        if not m or m.group(1).lower() not in _MONTHS:
            return None
        y, mo, d = int(m.group(3)), _MONTHS[m.group(1).lower()], m.group(2)
    try:
        if mo is None:
            return date(y, 12, 31) if end else date(y, 1, 1)
        mo = int(mo)
        if d is None:
            return date(y, mo, calendar.monthrange(y, mo)[1]) if end else date(y, mo, 1)
        return date(y, mo, int(d))
    except ValueError:
        return None


def date_check(point: dict, as_of: date, page_date, allow_no_period: bool = False) -> str:
    """返回丢弃原因；空串 = 通过。period_end、文中可见的发布日期、页面日期都必须 <= as_of。"""
    pe = parse_date(point.get("period_end"), end=True)
    if pe is None and not allow_no_period:
        return "period_end missing or unparseable"
    if pe is not None and pe > as_of:
        return f"period_end {pe} after as_of"
    ps = parse_date(point.get("period_start"))
    if ps is not None and pe is not None and ps > pe:
        return "period_start after period_end"
    pub = parse_date(point.get("published_at_if_visible"))
    if pub is not None and pub > as_of:
        return f"published {pub} after as_of"
    if page_date is not None and page_date > as_of:
        return f"page date {page_date} after as_of"
    return ""


# ---------- 泄漏哨兵 ----------
def leak_forms(true_value: float) -> list:
    """真值的常见写法。整数：千分位（, 空格 .）、无分隔、四舍五入到千、x.x thousand / k、0.xxx million / x.xx million。
    小于 1000 的数太容易撞车，只登记原样写法，并在报告里说明哨兵弱。"""
    v = float(true_value)
    forms = set()
    if v == int(v):
        n = int(v)
        g = f"{n:,}"
        forms |= {g, g.replace(",", " "), g.replace(",", "."), str(n)} if abs(n) >= 1000 else {str(n)}
        if abs(n) >= 10_000:
            k1 = f"{n / 1e3:.1f}"
            forms |= {f"{k1} thousand", f"{k1}k", f"{k1}K", f"{k1} k", f"{round(n, -3):,}",
                      f"{round(n / 1e3):,} thousand"}
        if abs(n) >= 100_000:
            forms |= {f"{n / 1e6:.3f} million", f"{n / 1e6:.3f}M"}
        if abs(n) >= 1_000_000:
            forms |= {f"{n / 1e6:.2f} million", f"{n / 1e6:.2f}M"}
    else:
        forms |= {f"{v:g}", f"{v:.1f}", f"{v:.2f}"}
    return sorted(forms)


def leak_patterns(true_value: float) -> list:
    return [re.compile(rf"(?<![\d.,]){re.escape(f)}(?!\d|[.,]\d)", re.I) for f in leak_forms(true_value)]


def leak_scan(text: str, patterns: list) -> list:
    """返回命中的写法（去重）。text 先规范化，所以不换行空格等写法也能命中。"""
    t = norm(text)
    return sorted({p.pattern for p in patterns if p.search(t)})

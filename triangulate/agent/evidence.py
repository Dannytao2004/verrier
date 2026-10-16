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


MAX_ELISION_CHARS = 150
_SENTENCE_END = re.compile(r"[.!?]\s+[A-Z0-9]")


def _gap_ok(gap: str) -> bool:
    """省略号跳过的那段原文：不超过 MAX_ELISION_CHARS 个字符，且不跨句子（防止把远处的期间词和数字拼成一个 quote）。"""
    return len(gap) <= MAX_ELISION_CHARS and not _SENTENCE_END.search(gap)


def quote_span(quote: str, text_norm: str):
    """quote 在规范化后的页面文字里逐字出现时返回 (起点, 终点)，否则 None。允许模型用 ... / … 省略中间部分：
    每段都必须按顺序逐字出现，相邻两段之间跳过的原文要满足 _gap_ok。"""
    parts = [p.strip() for p in re.split(r"\.\.\.|…", norm(quote)) if p.strip()]
    if not parts:
        return None

    def match_from(k: int, pos: int):
        p = parts[k]
        i = text_norm.find(p, pos)
        while i >= 0:
            if k > 0 and not _gap_ok(text_norm[pos:i]):
                return None  # 更远的出现位置跳过的原文只会更长
            if k == len(parts) - 1:
                return i, i + len(p)
            rest = match_from(k + 1, i + len(p))
            if rest is not None:
                return i, rest[1]
            i = text_norm.find(p, i + 1)
        return None

    return match_from(0, 0)


def quote_in_text(quote: str, text_norm: str) -> bool:
    return quote_span(quote, text_norm) is not None


def find_value(quote_n: str, value_written: str) -> int:
    """value_as_written 在 quote 里作为完整的数字出现时返回位置，否则 -1：前面不能紧挨数字、小数点或千分位，
    后面不能接数字或小数/千分位部分。'2.9%' 不能从 '12.9%' 里匹配，'412' 不能从 '3,412' 里匹配。"""
    m = re.search(r"(?<![\d.,])" + re.escape(value_written) + r"(?!\d|[.,]\d)", quote_n)
    return m.start() if m else -1


# ---------- 数字与倍数词 ----------
SCALES = {"": 1.0, "none": 1.0, "hundred": 1e2, "thousand": 1e3, "thousands": 1e3, "k": 1e3,
          "million": 1e6, "millions": 1e6, "m": 1e6, "mn": 1e6, "mln": 1e6,
          "billion": 1e9, "billions": 1e9, "bn": 1e9, "b": 1e9, "trillion": 1e12, "trillions": 1e12, "tn": 1e12}
PERCENT = {"%", "percent", "per cent", "pct"}
_NUM = re.compile(r"(?<![\d.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")
_WORD_SCALE = re.compile(r"^\s*(hundred|thousand|million|billion|trillion)s?\b", re.I)
_ABBR_SCALE = re.compile(r"^(k|m|mn|mln|bn|b|tn)\b", re.I)  # 只认紧贴数字的缩写：4.8M、$5bn
_DOT_THOUSANDS = re.compile(r"\d{1,3}(?:\.\d{3}){2,}(?!\d)")  # 1.234.567（欧式千分位）：不猜，直接报错
ABBREVIATIONS = {"k", "m", "mn", "mln", "b", "bn", "tn"}
SCALE_WORDS = {"hundred", "thousand", "million", "billion", "trillion"}
HEADER_WINDOW_CHARS = 3000
# 独立的表头写法：(in thousands) / (thousands) / ($ millions) / (USD millions) / (millions of dollars) / ('000)；
# 不带括号的 "in thousands" 后面必须紧跟标点或结尾（"resulted in thousands of cancellations" 不算）
_HEADER = re.compile(r"\((?:in\s+)?(?:[A-Z]{3}\s+|US\$\s*|[$€£¥]\s*)?(hundreds|thousands|millions|billions|trillions)"
                     r"(?:\s+of\s+[^()]{1,30})?\s*\)"
                     r"|\bin\s+(hundreds|thousands|millions|billions|trillions)(?=\s*(?:[.:;,)\]]|$))"
                     r"|\(\s*'?(000)s?'?\s*\)", re.I)


def parse_value(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (数值, 是否百分数)。数值 = 原文数字 x 倍数；只做这一次乘法。
    倍数可来自原文数字本身（"4.8 million"）或模型填的 scale_word；两者都有且不一致就报错。"""
    s = norm(value_as_written)
    if _DOT_THOUSANDS.search(s):
        raise ValueError("ambiguous separators: '.' used as a thousands separator")
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


def scale_supported(scale_word: str, quote_n: str, context_n: str, value_written: str = "") -> str:
    """倍数词必须有原文依据。返回依据（quote / page_header / none_needed），否则空串。
    - 缩写（k、m、b、bn ...）：只认紧贴数字的写法（value_as_written 本身带着，或 quote 里数字后面紧跟），没有页面级依据。
    - 单词（thousand、million ...）：quote 里数字后面紧跟这个词；或者 quote / context_n（调用方给的、quote 前面
      HEADER_WINDOW_CHARS 个字符的原文）里有独立的表头写法（见 _HEADER）。"""
    sw = norm(scale_word).lower()
    if sw in ("", "none") or sw in PERCENT:
        return "none_needed"
    vw = norm(value_written)
    base = sw[:-1] if sw.endswith("s") and sw[:-1] in SCALE_WORDS else sw
    if base in ABBREVIATIONS:
        if vw and re.search(rf"\d\s?{re.escape(base)}$", vw, re.I):
            return "quote"
        if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s?{re.escape(base)}(?![A-Za-z])", quote_n, re.I):
            return "quote"
        return ""
    if base not in SCALE_WORDS:
        return ""
    if vw and re.search(rf"\d\s*{base}s?\b", vw, re.I):
        return "quote"
    if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s*(?:-\s*)?{base}s?\b", quote_n, re.I):
        return "quote"
    for m in _HEADER.finditer(quote_n + " | " + context_n):
        word = (m.group(1) or m.group(2) or "").lower()
        if (word and word[:-1] == base) or (m.group(3) and base == "thousand"):
            return "page_header"
    return ""


# ---------- 日期 ----------
_MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
_MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})
_MONTHS["sept"] = 9


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


_MON = "|".join(sorted(_MONTHS, key=len, reverse=True))
_TEXT_DATE = re.compile(rf"\b(?:(?P<m1>{_MON})\.?\s+(?P<d1>\d{{1,2}})(?:st|nd|rd|th)?,?\s+(?P<y1>(?:19|20)\d{{2}})"
                        rf"|(?P<d2>\d{{1,2}})\s+(?P<m2>{_MON})\.?,?\s+(?P<y2>(?:19|20)\d{{2}})"
                        rf"|(?P<m3>{_MON})\.?,?\s+(?P<y3>(?:19|20)\d{{2}})"
                        rf"|(?P<iso>(?:19|20)\d{{2}}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])))\b", re.I)


def text_dates(text: str) -> list:
    """正文里的显式日期：Month D, YYYY / D Month YYYY / Month YYYY（取该月 1 日）/ YYYY-MM-DD。"""
    out = []
    for m in _TEXT_DATE.finditer(text or ""):
        try:
            if m.group("iso"):
                out.append(date.fromisoformat(m.group("iso")))
            elif m.group("y1"):
                out.append(date(int(m.group("y1")), _MONTHS[m.group("m1").lower()], int(m.group("d1"))))
            elif m.group("y2"):
                out.append(date(int(m.group("y2")), _MONTHS[m.group("m2").lower()], int(m.group("d2"))))
            else:
                out.append(date(int(m.group("y3")), _MONTHS[m.group("m3").lower()], 1))
        except ValueError:
            pass
    return out


def late_dates(text: str, as_of: date, until: date) -> list:
    """正文里晚于 as_of、但不晚于 until（取页日）的显式日期，去重排序。比取页日还晚的日期多半是将来的安排
    （结算日、开放日），不算。"""
    return sorted({d for d in text_dates(text) if as_of < d <= until})


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
    """一个值的常见写法。整数：千分位（, 空格 .）、无分隔、四舍五入到百和千、x.x / x.xx thousand 和 k、整数 k、
    0.xxx / 0.xx million 和 M、x.xx million。大小写不敏感（856K = 856k）。
    小于 1000 的数太容易撞车，只登记原样写法，并在报告里说明哨兵弱。"""
    v = float(true_value)
    forms = set()
    if v == int(v):
        n = int(v)
        g = f"{n:,}"
        forms |= {g, g.replace(",", " "), g.replace(",", "."), str(n)} if abs(n) >= 1000 else {str(n)}
        if abs(n) >= 10_000:
            k0 = f"{round(n / 1e3):,}"
            forms |= {f"{round(n, -2):,}", f"{round(n, -3):,}", f"{k0} thousand", f"{k0}k", f"{k0} k"}
            for kx in (f"{n / 1e3:.1f}", f"{n / 1e3:.2f}"):
                forms |= {f"{kx} thousand", f"{kx}k", f"{kx} k"}
        if abs(n) >= 100_000:
            for mx in (f"{n / 1e6:.3f}", f"{n / 1e6:.2f}"):
                forms |= {f"{mx} million", f"{mx}M", f"{mx} M"}
    else:
        forms |= {f"{v:g}", f"{v:.1f}", f"{v:.2f}"}
    return sorted(forms)


def leak_patterns(values) -> list:
    """values：一个数或一组数（目标真值，以及同一题里所有「公布日晚于 as_of」的已知官方值）。
    v2.6c：以 k 或 M 结尾的缩写写法后面不能接字母（「7.27 M」不再命中「7.27 miles」）；thousand、million 这类写法不变。"""
    vals = values if isinstance(values, (list, tuple, set)) else [values]
    forms = sorted({f for v in vals if v is not None for f in leak_forms(v)})
    return [re.compile(rf"(?<![\d.,]){re.escape(f)}(?!\d|[.,]\d)" + ("(?![A-Za-z])" if f.endswith(("k", "M")) else ""), re.I)
            for f in forms]


def leak_scan(text: str, patterns: list) -> list:
    """返回命中的写法（去重）。text 先规范化，所以不换行空格等写法也能命中。"""
    t = norm(text)
    return sorted({p.pattern for p in patterns if p.search(t)})

"""证据层的纯函数：数字解析、quote 原文核对、日期过滤、泄漏哨兵。全部由代码完成，不交给模型。"""
import calendar
import math
import re
import unicodedata
from datetime import date

import dateparser

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


def _word_guards(vw: str) -> tuple:
    """v2.8o：value_as_written 可以写成单词 / 中日韩数词（four、三百）。两头不能紧挨着同类的字：four 不能从 fourteen 里匹配，
    one 不能从 someone 里匹配，三百 / 两万 不能从 三百五十 / 两万三千 里匹配。纯数字写法不加（照旧）。"""
    cj = re.escape(_CJK_NUMERAL_CHARS + _CJK_SC)
    pre = r"(?<![A-Za-z])" if re.match(r"[A-Za-z]", vw) else ""
    post = r"(?![A-Za-z])" if re.search(r"[A-Za-z]$", vw) else ""
    if vw[:1] in _CJK_NUMERAL_CHARS:
        pre += rf"(?<![{cj}\d])"
    if vw[-1:] and vw[-1:] in _CJK_NUMERAL_CHARS + _CJK_SC and set(vw) & set(_CJK_NUMERAL_CHARS):
        post += rf"(?![{cj}\d])"
    return pre, post


def find_value(quote_n: str, value_written: str) -> int:
    """value_as_written 在 quote 里作为完整的数字出现时返回位置，否则 -1：前面不能紧挨数字、小数点或千分位，
    后面不能接数字或小数/千分位部分。'2.9%' 不能从 '12.9%' 里匹配，'412' 不能从 '3,412' 里匹配。"""
    pre, post = _word_guards(value_written)
    m = re.search(r"(?<![\d.,])" + pre + re.escape(value_written) + r"(?!\d|[.,]\d)" + post, quote_n)
    if m:
        return m.start()
    # v2.8g：抽取员漏写千分位（原文 4,774.10，写成 4774.10）也算同一个数：只放宽逗号，数字一位都不能差（恒顺外贸收入因此丢过 4 次）
    plain = value_written.replace(",", "")
    for t in re.finditer(r"(?<![\d.,])\d{1,3}(?:,\d{3})+(?:\.\d+)?(?!\d|[.,]\d)", quote_n):
        if t.group(0).replace(",", "") == plain:
            return t.start()
    return -1


# ---------- 数字与倍数词 ----------
# v2.6e：中日韩倍数字（万 / 萬 / 만 = 1e4，億 / 亿 / 억 = 1e8，兆 / 조 = 1e12，复合倍数万亿 / 萬億 = 1e12）和英文表头 '000s
CJK_SCALES = {"万": 1e4, "萬": 1e4, "만": 1e4, "億": 1e8, "亿": 1e8, "억": 1e8, "兆": 1e12, "조": 1e12,
              "万亿": 1e12, "萬億": 1e12}
# v2.8g：只在 scale_word 和表头（「单位：千元」「单位：百万元」）里出现的复合倍数词；正文里的连写数字（519万548）仍只认 CJK_SCALES
CJK_WORD_SCALES = {"千": 1e3, "仟": 1e3, "十万": 1e5, "十萬": 1e5, "百万": 1e6, "百萬": 1e6, "千万": 1e7, "千萬": 1e7,
                   "十亿": 1e9, "十億": 1e9, "百亿": 1e10, "百億": 1e10, "千亿": 1e11, "千億": 1e11,
                   "천": 1e3, "십만": 1e5, "백만": 1e6, "천만": 1e7}
SCALES = {"": 1.0, "none": 1.0, "hundred": 1e2, "thousand": 1e3, "thousands": 1e3, "k": 1e3,
          "million": 1e6, "millions": 1e6, "m": 1e6, "mn": 1e6, "mln": 1e6,
          "billion": 1e9, "billions": 1e9, "bn": 1e9, "b": 1e9, "trillion": 1e12, "trillions": 1e12, "tn": 1e12,
          "000s": 1e3, "'000s": 1e3, **CJK_SCALES, **CJK_WORD_SCALES}
# 打头的倍数词，长的先配（千万 先于 千，万亿 先于 万）
_CJK_MULT = "|".join(sorted({*CJK_SCALES, *CJK_WORD_SCALES}, key=len, reverse=True))
_CJK_WORD_ALT = "|".join(sorted(CJK_WORD_SCALES, key=len, reverse=True))
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
_CJK_SCALE_ALT = "万亿|萬億|[万萬만億亿억兆조]"
_CJK_UNIT_HEAD = re.compile(r"(?:[单單単]位|단위)\s*[:：]\s*([^\n|，,。；;)）]{1,12})")   # v2.8g：表头的单位声明「单位：万元」「(単位:万人)」
_CJK_SCALE = re.compile(rf"^\s?({_CJK_SCALE_ALT})")   # 紧跟在数字后面的倍数字
_CJK_SEG = re.compile(rf"\s?((?:\d{{1,3}}(?:,\d{{3}})+|\d+)(?:\.\d+)?)(?:\s?({_CJK_SCALE_ALT}))?")
_CJK_NUMERAL_CHARS = "〇零一二三四五六七八九十百千拾佰仟两兩천백십"
# 汉字 / 韩文数词（三百、1千）不支持：报错，不静默丢掉；「百分点」（0.5百分点）不算数词
_CJK_NUMERAL = re.compile(rf"^\s?(?!百分)[{_CJK_NUMERAL_CHARS}]")
_CJK_WORD = re.compile(rf"^({_CJK_MULT})(.*)$")   # v2.8g：scale_word 打头的倍数词也认复合的（千万元 -> 千万，千元 -> 千）
_CJK_SC = "万萬만億亿억兆조"   # 单个倍数字：判断一个数是不是更大的中日韩数字的一截（_cjk_reads）
# 前面紧挨「数字 + 倍数字」（만 / 억 / 조 后面可以隔一个空格）：「1億2345万」里的 2345万、「1억 2345만」里的 2345만。
# 倍数字前面必须是数字：하지만、다만、만 30세 里的「만」是普通的字，不是倍数
_CJK_BEFORE = re.compile(rf"\d\s?(?:{_CJK_SCALE_ALT})$|\d\s?[만억조]\s$")
_SI_UNIT = r"\s?(?:瓦|赫|帕|焦|字节|比特)"   # 兆瓦 / 兆赫 / 兆字节 ...：这里的「兆」是 SI 前缀 mega，和 1e12 歧义，不猜
_MEGA_UNIT = re.compile("兆" + _SI_UNIT)


def _cjk_scale_word(sw: str) -> str:
    """scale_word 里倍数字后面接着的单位去掉：万人 / 万人泊 -> 万，兆円 -> 兆，만 명 -> 만（万亿元 -> 万亿）。
    单位部分必须全是文字、不含数词；不是这种写法就原样返回。"""
    m = _CJK_WORD.match(sw)
    u = m.group(2).strip() if m else ""
    return m.group(1) if m and u.isalpha() and not set(u) & set(_CJK_NUMERAL_CHARS) else sw


def _cjk_sum(s: str, m) -> tuple:
    """m 是 s 里的第一个数字，后面紧跟中日韩倍数字：读「数字 + 倍数字」连写（3409万、519万548、1億2345万、2만 9000），
    返回 (各段之和, 第一段的倍数字, 读到的位置)；加法只在这里由代码做。后一段的倍数必须比前一段小，而且整段不满前一段的
    一个倍数单位（35万6713 可以；35万67130、5万3万 报错）；有几段时每段都必须是整数。段与段之间只有韩文
    （만 / 억 / 조 后面）允许一个空格（2만 9000）；「3409万 2025」不连读，按「多于一个数字」报错。"""
    first = _CJK_SCALE.match(s[m.end():])
    segs = [(abs(float(m.group().replace(",", ""))), CJK_SCALES[first.group(1)], "." in m.group())]
    prev, pos = first.group(1), m.end() + first.end()
    while (g := _CJK_SEG.match(s, pos)) and not (s[pos:pos + 1].isspace() and prev not in "만억조"):
        segs.append((float(g.group(1).replace(",", "")), CJK_SCALES[g.group(2)] if g.group(2) else 1.0, "." in g.group(1)))
        prev, pos = g.group(2), g.end()
        if not prev:
            break
    for (_, hi, _), (n, f, _) in zip(segs, segs[1:]):
        if f >= hi or n * f >= hi:
            raise ValueError("malformed CJK number: each part must be smaller than the scale before it")
    if len(segs) > 1 and any(dec for _, _, dec in segs):
        raise ValueError("malformed CJK number: decimal in a multi-part number")
    total = sum(n * f for n, f, _ in segs)
    return (-total if m.group().startswith("-") else total), first.group(1), pos


def parse_value(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (数值, 是否百分数)。数值 = 原文数字 x 倍数；只做这一次乘法。
    倍数可来自原文数字本身（"4.8 million"、"3409万"）或模型填的 scale_word；两者都有且不一致就报错。
    v2.6e：中日韩复合写法（519万548 = 5,190,548）是各段之和（_cjk_sum）；scale_word 里倍数字后面的单位先去掉
    （万人 -> 万、兆円 -> 兆）；'000s = 千；汉字 / 韩文数词（三百、1千）不支持，报错；「兆」后面紧跟 SI 单位（兆瓦）报错；
    倍数字后面又接倍数字（15.4万億）报错。"""
    s = norm(value_as_written)
    if _DOT_THOUSANDS.search(s):
        raise ValueError("ambiguous separators: '.' used as a thousands separator")
    if _MEGA_UNIT.search(s) or _MEGA_UNIT.match(norm(scale_word)):
        raise ValueError("ambiguous '兆' before an SI unit: 10^12 or mega-")
    m = _NUM.search(s)
    if not m:
        raise ValueError("no number in value_as_written")
    cjk = _cjk_sum(s, m) if _CJK_SCALE.match(s[m.end():]) else None
    rest = s[cjk[2]:] if cjk else s[m.end():]
    word = None if cjk else re.match(rf"\s?({_CJK_WORD_ALT})", rest)   # v2.8g：数字后面紧跟复合倍数词（12.5十亿、3.2百万、12,345千人）
    if word:
        rest = rest[word.end():]
    if _NUM.search(rest):
        raise ValueError("more than one number in value_as_written")
    if cjk and _CJK_SCALE.match(rest):   # 15.4万億（混写的复合倍数）、3万万：不猜，以前把第二个倍数字当成单位文字丢掉
        raise ValueError("malformed CJK number: two scale characters in a row")
    if _CJK_NUMERAL.match(rest):
        raise ValueError("CJK numerals (e.g. 三百, 1千) are not supported")
    num = cjk[0] if cjk else float(m.group().replace(",", ""))
    if s[:m.start()].strip().startswith("(") and rest.strip().startswith(")"):
        num = -num  # 会计写法 (1,234)
    text_scale, is_pct = (cjk[1] if cjk else word.group(1) if word else None), False
    if rest.strip().startswith("%") or rest.strip().lower().startswith(("percent", "per cent")):
        is_pct = True
    elif not cjk and ((w := _WORD_SCALE.match(rest)) or (w := _ABBR_SCALE.match(rest))):
        text_scale = w.group(1).lower()
    sw = norm(scale_word).lower()
    if sw in PERCENT:
        is_pct, sw = True, ""
    sw = _cjk_scale_word(sw)
    if sw not in SCALES:
        raise ValueError(f"unknown scale word {scale_word!r}")
    if text_scale and sw and SCALES[sw] != SCALES[text_scale]:
        raise ValueError(f"scale conflict: {text_scale!r} in value vs {scale_word!r}")
    factor = 1.0 if cjk else SCALES[text_scale or sw]   # 中日韩写法的倍数已经在各段里乘过
    return num * factor, is_pct


# ---------- v2.8o：抽取员读的数（number / low / high） ----------
# 用户 10-18 的设计：value_as_written 照抄原文的写法（数字、单词、分数、区间都行），number 是它表示的数（不乘倍数词），
# 区间给 low / high。只用于 parse_value 解析不了的写法（阿拉伯数字照旧由代码解析）。代码只乘倍数、算区间中点；
# 读得对不对，算之前交给模型逐个核对（value_check.py）
_PCT_WRITTEN = re.compile(r"%|per\s?cent|\bpct\b|百分之|퍼센트|パーセント", re.I)
_FRACTION = re.compile(r"([-+]?\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)")
READING_KEYS = ("number", "low", "high")
_RANGE_MARK = re.compile(r"\s(?:to|and)\s|[-–—~～至到]", re.I)   # 3-4、3 to 4、between 10 and 12、3至4


def has_reading(raw: dict) -> bool:
    """抽取员给了 number 或 low / high（没给的旧写法照旧由 parse_value 从 value_as_written 解析）。"""
    return any(raw.get(k) not in (None, "") for k in READING_KEYS)


def _reading_num(x, what: str) -> float:
    """number / low / high：JSON 数字，或写成数字的字符串（"4774.10"、分数 "1/6"）。千分位逗号不认（和小数逗号分不清）。"""
    if isinstance(x, bool):
        raise ValueError(f"{what} is not a number")
    if isinstance(x, (int, float)):
        v = float(x)
    else:
        s = str(x).strip()
        m = _FRACTION.fullmatch(s)
        try:
            v = float(m.group(1)) / float(m.group(2)) if m else float(s)
        except (ValueError, ZeroDivisionError):
            raise ValueError(f"{what} {str(x)[:20]!r} is not a plain number") from None
    if not math.isfinite(v):
        raise ValueError(f"{what} is not a finite number")
    return v


_TRAIL_ABBR = re.compile(r"(?<=\d)(k|m|mn|mln|bn|b|tn)\b", re.I)   # 只认紧贴数字的缩写：4.8m、$5bn（4.8 m 是米）
_NUM_WORDS = re.compile(r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|"
                        r"sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|"
                        r"thousand|million|billion|trillion|dozen|half|quarter)\b", re.I)


def _trailing_multiplier(s: str, words: str):
    """value_as_written 里最后一个数后面的倍数词（4.8 million、two million cases、3409万元、两万、$5bn）；后面还有数
    （four thousand two hundred、519万548）就不算。汉字数词后面的「千」是数的一部分（三千），不算倍数。"""
    nums = re.escape(_CJK_NUMERAL_CHARS)
    cands = list(re.finditer(rf"(?<=[\da-z])\s*-?\s*({words})s?\b", s, re.I)) + list(_TRAIL_ABBR.finditer(s))
    cands += [m for m in re.finditer(rf"(?<=[\d{nums}])\s?({_CJK_MULT})", s)
              if not (m.group(1) in ("千", "仟") and not s[m.start() - 1].isdigit())]
    if not cands:
        return None
    m = max(cands, key=lambda x: x.end())
    tail = s[m.end():]
    return None if re.search(rf"[\d{nums}]", tail) or _NUM_WORDS.search(tail) else m


def split_multiplier(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (去掉倍数词的写法, 倍数)。倍数由代码定：scale_word 的，或 value_as_written 末尾写着的（_trailing_multiplier）；
    两者都有而不一致就报错。核对模型只看去掉倍数词的写法（v2.8o 探针：倍数交给模型判，「4.8 million」读成 4.8、
    表头「万」的 4,774.10 读成 477410 都被它判成对的）。
    中日韩复合写法（519万548）里的倍数字后面还有数，不算末尾的倍数：这时 scale_word 必须为空，number 写整个数。"""
    s, swn = norm(value_as_written), _cjk_scale_word(norm(scale_word).lower())
    if swn not in SCALES:
        raise ValueError(f"unknown scale word {scale_word!r}")
    words = "hundred|thousand|million|billion|trillion" if swn in ("hundred", "hundreds") else "thousand|million|billion|trillion"
    m = _trailing_multiplier(s, words)
    if m:
        key = m.group(1).lower()
        f = SCALES.get(key, SCALES.get(key + "s"))
        if swn and SCALES[swn] != f:
            raise ValueError(f"scale conflict: {m.group(1)!r} in value vs {scale_word!r}")
        return (s[:m.start()] + s[m.end():]).strip(), f
    nums = re.escape(_CJK_NUMERAL_CHARS)
    if swn and re.search(rf"[\d{nums}]\s?(?:{_CJK_SCALE_ALT})[\d{nums}]", s):
        raise ValueError("compound CJK number (519万548): leave scale_word empty and give the whole number")
    return s, SCALES[swn]


def written_number(value_as_written: str, scale_word: str = "") -> str:
    """给核对模型看的写法：value_as_written 去掉末尾的倍数词（百分号照旧留着）。"""
    return split_multiplier(value_as_written, "" if norm(scale_word).lower() in PERCENT else scale_word)[0]


def read_reading(raw: dict, value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (value, low, high, is_pct, reading)：value / low / high 已乘 scale_word 的倍数（区间时 value = 中点，没有区间时
    low = high = None）；reading 是抽取员读的数本身（不乘倍数），交给核对模型看。
    原文写法上的两条旧检查照旧：欧式千分位（1.234.567）、「兆」后面紧跟 SI 单位（兆瓦）不猜，报错。"""
    s, swn = norm(value_as_written), norm(scale_word).lower()
    if _DOT_THOUSANDS.search(s):
        raise ValueError("ambiguous separators: '.' used as a thousands separator")
    if _MEGA_UNIT.search(s) or _MEGA_UNIT.match(swn):
        raise ValueError("ambiguous '兆' before an SI unit: 10^12 or mega-")
    is_pct = bool(_PCT_WRITTEN.search(s)) or swn in PERCENT
    _, f = split_multiplier(value_as_written, "" if swn in PERCENT else scale_word)
    lo, hi = raw.get("low"), raw.get("high")
    if lo not in (None, "") or hi not in (None, ""):
        if lo in (None, "") or hi in (None, ""):
            raise ValueError("a range needs both low and high")
        if not _RANGE_MARK.search(s[1:]):   # v2.8o 探针：「12」读成 12..13 被核对模型放行；写法里没有区间就不是区间
            raise ValueError("low/high given but value_as_written is not a range")
        lo, hi = _reading_num(lo, "low"), _reading_num(hi, "high")
        if not lo < hi:
            raise ValueError("range low must be below high")
        return (lo + hi) / 2 * f, lo * f, hi * f, is_pct, {"low": lo, "high": hi}
    n = _reading_num(raw.get("number"), "number")
    return n * f, None, None, is_pct, {"number": n}


def _cjk_reads(quote_n: str, vw: str, cj: str):
    """vw 在 quote 里每一次作为完整数字出现（find_value 的规则）时，逐次给出 (是否用上了 cj, 问题)。cj 是 scale_word 给的
    中日韩倍数字：vw 不以倍数字结尾、后面（最多隔一个空格）紧跟 cj 时算进这个数。问题为空串 = 这次读到的是一个完整的数；
    "part" = 只是更大的数的一截：① 前面紧挨「数字 + 倍数字」（_CJK_BEFORE；倍数字前面不是数字的不算，하지만 24,275 里的
    24,275 是完整的数）；② 读到的数后面（最多隔一个空格）还接着倍数字；③ 读到的数以倍数字结尾、后面紧接数字（만 / 억 / 조
    后面可以隔一个空格）；④ 读到的数带中日韩倍数字、后面紧接汉字 / 韩文数词（「61万1千人」里只写 61万1，parse_value 会读成
    610,001）。①③ 的段间空格规则和 _cjk_sum 相同；② 比 _cjk_sum 宽（15.4万億 这种混写 _cjk_sum 不连读，这里也算一截）。
    不带倍数字的数后面接「千」（12,345千人 里的 12,345）不算，和 v2.6d 一样按原文数字取值。
    "mega" = 读到的数以「兆」结尾、后面紧跟 SI 单位（兆瓦）。"""
    for m in re.finditer(r"(?<![\d.,])" + re.escape(vw) + r"(?!\d|[.,]\d)", quote_n):
        tail, last, used = quote_n[m.end():], vw[-1], False
        if cj and last not in _CJK_SC and (g := re.match(r"\s?" + re.escape(cj), tail)):
            tail, last, used = tail[g.end():], cj[-1], True
        if (_CJK_BEFORE.search(quote_n[max(0, m.start() - 4):m.start()])
                or re.match(rf"\s?[{_CJK_SC}]", tail)
                or (last in _CJK_SC and re.match(r"\s?\d" if last in "만억조" else r"\d", tail))
                or ((used or set(vw) & set(_CJK_SC)) and re.match(rf"(?!百分)[{_CJK_NUMERAL_CHARS}]", tail))):
            yield used, "part"
        else:
            yield used, ("mega" if last == "兆" and re.match(_SI_UNIT, tail) else "")


def cjk_fragment(quote_n: str, value_written: str, scale_word: str = "") -> str:
    """v2.6e：value_as_written 在 quote 里的每一次出现都读不成一个完整的数时返回原因（pipeline.verify_point 据此丢点），否则空串。
    例：「1億3000万人泊」里只写 1億3000、「1億2345万人」里只写 2345万 或 2345 + 万、「15.4万亿元」里写 15.4万 或 15.4 + 万、
    scale_word 为空时「3409万」里只写 3409、「500兆瓦」里写 500兆 或 500 + 兆。前后都不挨中日韩倍数字的写法（英文页面）一律返回空串。"""
    vw = norm(value_written)
    cj = _cjk_scale_word(norm(scale_word).lower())
    reads = [why for _, why in _cjk_reads(quote_n, vw, cj if cj in CJK_SCALES else "")] if vw else []
    if not reads or "" in reads:
        return ""
    if reads[0] == "mega":
        return "ambiguous '兆' before an SI unit: 10^12 or mega-"
    return "value_as_written is only part of a larger CJK number in the quote"


def scale_supported(scale_word: str, quote_n: str, context_n: str, value_written: str = "") -> str:
    """倍数词必须有原文依据。返回依据（quote / page_header / none_needed），否则空串。
    - 缩写（k、m、b、bn ...）：只认紧贴数字的写法（value_as_written 本身带着，或 quote 里数字后面紧跟），没有页面级依据。
    - 单词（thousand、million ...）：quote 里数字后面紧跟这个词；或者 quote / context_n（调用方给的、quote 前面
      HEADER_WINDOW_CHARS 个字符的原文）里有独立的表头写法（见 _HEADER）。'000s 按 thousand 处理。
    - v2.6e 中日韩倍数字（万、億、만 ...；scale_word 里后面的单位先去掉）：和缩写一样只认紧贴数字的写法，没有页面级依据；
      quote 里「数字 + 倍数字」必须是一个完整的数（_cjk_reads）：前面不挨「数字 + 倍数字」，后面不再接
      倍数字或连读的数字（「519万548」只写 519 + 万会丢掉 548，「15.4万亿」只写 15.4 + 万会丢掉亿，「1億2345万」只写 2345 + 万会丢掉 1 億）。"""
    sw = norm(scale_word).lower()
    if sw in ("", "none") or sw in PERCENT:
        return "none_needed"
    vw = norm(value_written)
    if (cj := _cjk_scale_word(sw)) in CJK_SCALES or cj in CJK_WORD_SCALES:
        if cj in CJK_SCALES:
            if vw and re.search(rf"[\d{_CJK_NUMERAL_CHARS}]\s?{re.escape(cj)}", vw):   # v2.8o：数词写法（两万）也算紧贴
                return "quote"
            if vw and any(used and not why for used, why in _cjk_reads(quote_n, vw, cj)):
                return "quote"
        elif vw and re.search(rf"[\d{_CJK_NUMERAL_CHARS}]\s?{re.escape(cj)}$", vw):
            return "quote"   # value_as_written 本身带着复合倍数词：12.5十亿
        elif vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s?{re.escape(cj)}(?![{_CJK_SC}{_CJK_NUMERAL_CHARS}\d])", quote_n):
            return "quote"   # 复合倍数词紧跟在数字后面：12.5千万元
        # v2.8g：中文表格把单位写在表头（「单位：万元」），数字后面不带「万」。取 quote 前面最近的一个「单位：」声明（quote 里有就用 quote 里的），
        # 它打头的倍数词必须和 scale_word 的完全一样（「单位：万亿元」不能当「万」用，「单位：千万元」不能当「千」用）；
        # 最近的声明是别的单位（单位：个）就不算。恒顺年报的外贸收入因此丢过 4 次
        heads = _CJK_UNIT_HEAD.findall(context_n + " | " + quote_n)
        lead = re.match(rf"\s*(?:人民币|美元|港币|港元|日元|韩元|币种[:：]?\S*)?\s*({_CJK_MULT})", heads[-1]) if heads else None
        if lead and lead.group(1) == cj:
            return "page_header"
        return ""
    base = sw[:-1] if sw.endswith("s") and sw[:-1] in SCALE_WORDS else sw
    base = "thousand" if base in ("000s", "'000s") else base
    if base in ABBREVIATIONS:
        if vw and re.search(rf"\d\s?{re.escape(base)}$", vw, re.I):
            return "quote"
        if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s?{re.escape(base)}(?![A-Za-z])", quote_n, re.I):
            return "quote"
        return ""
    if base not in SCALE_WORDS:
        return ""
    if vw and re.search(rf"(?:\d|[a-z])\s*{base}s?\b", vw, re.I):   # v2.8o：单词写法（two million）也算紧贴
        return "quote"
    if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s*(?:-\s*)?{base}s?\b", quote_n, re.I):
        return "quote"
    for m in _HEADER.finditer(quote_n + " | " + context_n):
        word = (m.group(1) or m.group(2) or "").lower()
        if (word and word[:-1] == base) or (m.group(3) and base == "thousand"):
            return "page_header"
    return ""


# ---------- 日期 ----------
# L1（v2.8a）：parse_date 里 ISO 和中日韩的整串写法仍用原来的正则，其他写法（英文月份名等）交给 dateparser。
# 中日韩不交给它：dateparser 1.4.3 读不出 2026년 3월 27일、2026 年 3 月 27 日、2025年08月（月份补零）这些写法，也不认纪年
_MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
_MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})
_MONTHS["sept"] = 9
# v2.6e 中日韩日期：年份是公历（2026年 / 2026년）或纪年：令和 N 年 = 2018+N，平成 N 年 = 1988+N，民國 / 民国 N 年 = 1911+N（元年 = 1）
_ERA_BASE = {"令和": 2018, "平成": 1988, "民國": 1911, "民国": 1911}
_ERA = r"(?P<era>令和|平成|民國|民国)\s?(?P<n>\d{1,3}|元)"
# \d 也认全角数字（日文页面常见，int() 能直接转）；年份范围在 _cjk_year 里查
_YMD_CJK = re.compile(rf"(?:(?P<g>\d{{4}})|{_ERA})\s?年(?:\s?(?P<m>\d{{1,2}})\s?月(?:\s?(?P<d>\d{{1,2}})\s?日)?)?")
_YMD_KR = re.compile(r"(?P<g>\d{4})\s?년(?:\s?(?P<m>\d{1,2})\s?월(?:\s?(?P<d>\d{1,2})\s?일)?)?")
# 正文里只认完整的年月日；台湾常省略「民國」，不带前缀的三位数 1NN年M月D日 也按民国算
_TEXT_DATE_CJK = re.compile(rf"(?:(?<!\d)(?P<g>\d{{4}})|{_ERA}|(?<![\d.,])(?P<b>\d{{3}}))"
                            r"\s?年\s?(?P<m>\d{1,2})\s?月\s?(?P<d>\d{1,2})\s?日"
                            r"|(?<!\d)(?P<kg>\d{4})\s?년\s?(?P<km>\d{1,2})\s?월\s?(?P<kd>\d{1,2})\s?일")
_ERA_YEAR = re.compile(rf"{_ERA}\s?年|(?<![\d.,])(?P<b>\d{{3}})\s?年")


def _cjk_year(g: dict):
    """正则命中的年份 -> 公历年：公历年原样（只认 1900–2099，和英文日期的 (19|20)\\d\\d 一样）；令和 / 平成 / 民國 N 年
    加基数（元年 = 1）；不带前缀的三位数只认 100–199，按民国算（115年 = 2026）。范围外返回 None。"""
    if g.get("g") or g.get("kg"):
        y = int(g.get("g") or g["kg"])
        return y if 1900 <= y <= 2099 else None
    if g.get("era"):
        return _ERA_BASE[g["era"]] + (1 if g["n"] == "元" else int(g["n"]))
    n = int(g["b"])
    return 1911 + n if 100 <= n <= 199 else None


def era_years(text: str) -> set:
    """文字里纪年写法的年份（公历）：令和 / 平成 / 民國 / 民国 N 年，和台湾常用的不带「民國」的 1NN 年（115年 = 2026）。
    pipeline.verify_point 的期间年份检查用：页面只写纪年时，公历年份不在正文里。"""
    return {y for m in _ERA_YEAR.finditer(text or "") if (y := _cjk_year(m.groupdict())) is not None}


# dateparser 的设置：不完整的日期取期初 / 期末（PREFER_DAY_OF_MONTH、PREFER_MONTH_OF_YEAR，按 end 填）；不带时区；不往将来推。
# 和改前一样必须写明年份、不认相对现在的写法（yesterday、3 months ago、时间戳）
_DATEPARSER = {"PREFER_DATES_FROM": "past", "RETURN_AS_TIMEZONE_AWARE": False, "REQUIRE_PARTS": ["year"],
               "PARSERS": ["absolute-time"]}


def parse_date(s, end: bool = False):
    """日期串 -> date，解析不了返回 None。end=True 时不完整日期取期末（2025-08 -> 8 月 31 日，2026年 -> 12 月 31 日）。
    YYYY-MM-DD / YYYY-MM / YYYY（可带 T 时间）、2026年3月27日 / 2026年3月 / 2026年、2026년 3월 27일、令和8年3月、
    民國115年5月（这里纪年要带前缀）用原来的正则；其他写法（"August 2025"、"Aug 5, 2025"、"5 August 2025"……）交给 dateparser。"""
    if not s or not isinstance(s, str):
        return None
    s = s.strip()
    m = re.fullmatch(r"(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?(?:T.*)?", s)
    c = None if m else (_YMD_CJK.fullmatch(s) or _YMD_KR.fullmatch(s))
    if m:
        y, mo, d = int(m.group(1)), m.group(2), m.group(3)
    elif c:
        y, mo, d = _cjk_year(c.groupdict()), c["m"], c["d"]
        if y is None:
            return None
    else:
        pref = "last" if end else "first"
        dt = dateparser.parse(s, settings=dict(_DATEPARSER, PREFER_DAY_OF_MONTH=pref, PREFER_MONTH_OF_YEAR=pref))
        return dt.date() if dt else None
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
    """正文里的显式日期：Month D, YYYY / D Month YYYY / Month YYYY（取该月 1 日）/ YYYY-MM-DD；
    v2.6e 加中日韩的完整年月日（2026年3月27日、2026년 3월 27일、令和8年3月27日、民國115年5月20日 / 115年5月20日）。
    L1：候选串仍由这两个正则找，每个候选交给 parse_date 解析（不用 dateparser 的全文搜索：长页面上慢、误报多）。
    按在正文里出现的顺序返回。"""
    out = [(m.start(), parse_date(m.group(0))) for m in _TEXT_DATE.finditer(text or "")]
    for m in _TEXT_DATE_CJK.finditer(text or ""):
        if _cjk_year(m.groupdict()) is not None:   # 年份范围：公历只认 1900–2099，不带前缀的三位数只认 100–199
            out.append((m.start(), parse_date(("民國" if m["b"] else "") + m.group(0))))   # 补回台湾省略的「民國」
    return [d for _, d in sorted(out, key=lambda x: x[0]) if d is not None]


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
def _cjk_exact_forms(n: int) -> set:
    """整数 n（|n| >= 1 万）的中日韩精确写法：35万6920 / 35萬6920 / 35만6920，以及各段写千分位的 35万6,920；
    1 亿以上再加億 / 亿 / 억 一段（1億2345万6789），为 0 的段省略（300万）。不登记四舍五入写法（344万、13.4萬）。"""
    sign, a = ("-" if n < 0 else ""), abs(n)
    hi, mid, lo = a // 10**8, a // 10**4 % 10**4, a % 10**4
    forms = set()
    for wan, yi in (("万", "億"), ("万", "亿"), ("萬", "億"), ("만", "억")):
        for f in (str, "{:,}".format):
            forms.add(sign + (f(hi) + yi if hi else "") + (f(mid) + wan if mid else "") + (f(lo) if lo else ""))
    return forms


def leak_forms(true_value: float) -> list:
    """一个值的常见写法。整数：千分位（, 空格 .）、无分隔、四舍五入到百和千、x.x / x.xx thousand 和 k、整数 k、
    0.xxx / 0.xx million 和 M、x.xx million。大小写不敏感（856K = 856k）。
    v2.6e：1 万以上的整数加中日韩的精确写法（_cjk_exact_forms，例如 35万6920）；中日韩的四舍五入写法不登记（少误杀，见 C3）。
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
            forms |= _cjk_exact_forms(n)
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

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
# v2.11a：倍数只有下面这几张表（英文、中日韩各一组）。后面认倍数的正则、词表、单位里的倍数、SCALE_FOR_FACTOR 都从表里派生，
# 以前每处各抄一份，quadrillion、千万亿 在一处认、另一处不认（1.3 quadrillion 读成 1.3、1.3千万亿 读成 1.3e7）。
# 认得出的倍数要么读对，要么报错丢点（原因写进 state.json）；仍按面值读的已知情形记在 BUGS.md
# 英文单词（复数、首字母大写都认）：短级到 quintillion，sextillion 以上报错；印度英语 lakh / lac / crore、英式 milliard
EN_SCALES = {"hundred": 1e2, "thousand": 1e3, "lakh": 1e5, "lac": 1e5, "million": 1e6, "crore": 1e7, "billion": 1e9,
             "milliard": 1e9, "trillion": 1e12, "quadrillion": 1e15, "quintillion": 1e18}
# 叠加词白名单（ten thousand 是「万」的英文写法）；不在白名单里的两个倍数词连写报错（3 million billion、3万 million）
EN_STACKED = {"ten thousand": 1e4, "hundred thousand": 1e5, "hundred million": 1e8, "thousand million": 1e9,
              "hundred billion": 1e11, "thousand billion": 1e12, "thousand crore": 1e10, "lakh crore": 1e12}
# 缩写，不分大小写：k / m / b 只认紧贴数字（4.8 m 是米），前面是货币符号时隔一个空格也认（$5.8 B）；其余紧贴或隔一个空格都认
EN_ABBR = {"k": 1e3, "m": 1e6, "b": 1e9, "mn": 1e6, "mln": 1e6, "bn": 1e9, "bln": 1e9, "tn": 1e12, "trn": 1e12}
_GLUED_ONLY = ("k", "m", "b")
EN_CASED = {"MM": 1e6}   # 区分大小写、紧贴数字：4.8MM = 4.8e6（5mm 是毫米）
# 只在货币符号 / 代码后面认的缩写（紧贴或隔一个空格，不分大小写）：$5mm、$5 MM、$5 bil；别处是毫米、挪威语的 bil（汽车）
CURRENCY_ABBR = {"mm": 1e6, "bil": 1e9}
INR_ABBR = {"cr": 1e7}   # 只在 Rs / ₹ / INR 后面：Rs 500 cr（会计的 Cr 是贷方）
# 只确认、不自动认的记号（confirm-only）：scale_word 写的是同一个倍数才乘，scale_word 为空就报错；
# 小写 t 例外，scale_word 为空时按面值（吨，prompts.py:45）。1T 存储、3T MRI、3Q 2026、80 京口石油、3경기 都不是倍数
CONFIRM = {"T": 1e12, "t": 1e12, "Q": 1e15, "京": 1e16, "경": 1e16}
# scale_word 直接填这些记号也认（转小写之前看原始大小写）：T、Q、MM
_SW_CASED = {k: f for k, f in {**CONFIRM, **EN_CASED}.items() if k.isascii() and k.isupper()}
# 不是中日韩英的倍数词：不支持，报错（S24）。西语 mil / millones / billones / mdd（墨西哥：millones de dólares）/ mmdd，
# 葡语 milhão / milhões / bilhões，德语 Millionen / Milliarden / Mio / Mrd / Tsd，意大利 / 波兰 / 捷克 / 阿尔巴尼亚 milioni /
# miliony / milionë / miliard，荷兰 / 北欧 miljoen / miljoner / miljard / millioner / milliarder，捷克 / 波兰 mld。
# mdd / mld 只认小写（MDD 是抑郁症的缩写）；mln 和英文同义，在 EN_ABBR 里
_FOREIGN_SCALE = (r"mil|mill[oó]n(?:es)?|bill[oó]n(?:es)?|(?-i:m{1,2}dd|mld)|milh(?:ão|ao|ões|oes)|bilh(?:ão|ao|ões|oes)|"
                  r"millionen|milliarden?|billionen|mio|mrd|tsd|milion\w*|miliard\w*|miljo(?:en|ner|n)|miljard(?:er|en)?|"
                  r"millioner|milliarder")
_UNSUPPORTED_CJK = "垓"   # 1e20：表里没有，数字后面出现就报错（韩文「해」不处理：语料里是「1해당자녀」这类词）
# v2.6e：中日韩倍数字（万 / 萬 / 만 = 1e4，億 / 亿 / 억 = 1e8，兆 / 조 = 1e12，复合倍数万亿 / 萬億 = 1e12）和英文表头 '000s
# v2.11a：加亿亿 / 億億 = 1e16
CJK_SCALES = {"万": 1e4, "萬": 1e4, "만": 1e4, "億": 1e8, "亿": 1e8, "억": 1e8, "兆": 1e12, "조": 1e12,
              "万亿": 1e12, "萬億": 1e12, "亿亿": 1e16, "億億": 1e16}
# v2.8g：只在 scale_word 和表头（「单位：千元」「单位：百万元」）里出现的复合倍数词；正文里的连写数字（519万548）仍只认 CJK_SCALES
# v2.11a：加十万亿 / 百万亿 / 千万亿（1e13–1e15）和韩文십억 / 백억 / 천억 / 십조 / 백조 / 천조；末字是大倍数字的复合词
# （千万、천억 ...）也能当连写数字的一段（1億3千万、1조 2천억，见 _CJK_SEG）
CJK_WORD_SCALES = {"千": 1e3, "仟": 1e3, "十万": 1e5, "十萬": 1e5, "百万": 1e6, "百萬": 1e6, "千万": 1e7, "千萬": 1e7,
                   "十亿": 1e9, "十億": 1e9, "百亿": 1e10, "百億": 1e10, "千亿": 1e11, "千億": 1e11,
                   "十万亿": 1e13, "十萬億": 1e13, "百万亿": 1e14, "百萬億": 1e14, "千万亿": 1e15, "千萬億": 1e15,
                   "천": 1e3, "십만": 1e5, "백만": 1e6, "천만": 1e7, "십억": 1e9, "백억": 1e10, "천억": 1e11,
                   "십조": 1e13, "백조": 1e14, "천조": 1e15}
SCALES = {"": 1.0, "none": 1.0, **{w + s: f for w, f in {**EN_SCALES, **EN_STACKED}.items() for s in ("", "s")},
          **EN_ABBR, "000s": 1e3, "'000s": 1e3, **CJK_SCALES, **CJK_WORD_SCALES,
          **{k: f for k, f in CONFIRM.items() if not k.isascii()}}   # 京 / 경 只在 scale_word 里认（数字后面要确认）
_SW_FACTOR = {**SCALES, **_SW_CASED}


def _hangul(c: str) -> bool:
    return "가" <= c <= "힣"


def _alt(words) -> str:
    """正则的候选写法，长的先配（千万 先于 千，万亿 先于 万）；英文叠加词词间可以是空格或连字符。"""
    return "|".join(re.escape(w).replace(r"\ ", r"[\s-]+") for w in sorted(words, key=lambda w: (-len(w), w)))


def _en_key(w: str) -> str:
    """英文倍数词的表里写法：小写，词间的空格 / 连字符换成一个空格（Ten-Thousand -> ten thousand）。"""
    return re.sub(r"[\s-]+", " ", w.strip().lower())


# 打头的倍数词，长的先配（千万 先于 千，万亿 先于 万）
_CJK_MULT = _alt({*CJK_SCALES, *CJK_WORD_SCALES})
_CJK_WORD_ALT = _alt(CJK_WORD_SCALES)
PERCENT = {"%", "percent", "per cent", "pct"}
_NUM = re.compile(r"(?<![\d.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")
# 紧跟在数后面的英文倍数词：前面可以有 + 和连字符（5+ million、$1.2-billion），叠加词整体算（3 hundred million = 3e8）
_WORD_SCALE = re.compile(rf"^\+?\s*-?\s*({_alt(EN_STACKED)}|{_alt(EN_SCALES)})s?\b", re.I)
_ABBR_GLUED = re.compile(rf"^(?:{_alt(EN_ABBR)})\b", re.I)                              # 4.8M、$5bn
_ABBR_SPACED = re.compile(rf"^ (?:{_alt(set(EN_ABBR) - set(_GLUED_ONLY))})\b", re.I)    # $5 bn、5 mln
_ABBR_CURRENCY = re.compile(rf"^(?: (?:{_alt(_GLUED_ONLY)})| ?(?:{_alt(CURRENCY_ABBR)}))\b", re.I)   # 只在货币符号后面：$5.8 B、$5mm
_ABBR_INR = re.compile(rf"^ ?(?:{_alt(INR_ABBR)})\b", re.I)                                                  # Rs 500 cr、₹500 Cr
_CURRENCY = r"[$€£¥₹₩]|\b(?:USD|EUR|GBP|JPY|CNY|RMB|INR|KRW|CAD|AUD|CHF|HKD|SGD|MXN|BRL)|\bRs\.?"
_CURRENCY_BEFORE = re.compile(rf"(?:{_CURRENCY})\s?$")
_INR_BEFORE = re.compile(r"(?:₹|\bINR|\bRs\.?)\s?$")
# v2.11a：货币符号前面的负号（-$1.2B、negative US$5.9 billion、minus €3bn）和 minus / negative 后面的数；紧贴数字的负号在 _NUM 里
_SIGN_BEFORE = re.compile(rf"(?:^|[\s(])(?:-(?:[A-Z]{{1,3}})?(?:{_CURRENCY})|(?:minus|negative)\s+(?:(?:[A-Z]{{1,3}})?(?:{_CURRENCY}))?)\s?$",
                          re.I)
_CASED = re.compile(rf"^(?:{_alt(EN_CASED)})\b")
# confirm-only 记号的正则写法：韩文的后面接韩文音节（경기、경제）不是倍数，원 除外
_CONFIRM_RE = {k: re.escape(k) + ("(?!(?!원)[가-힣])" if _hangul(k) else "") for k in CONFIRM}
_CONFIRM_CJK = "|".join(r for k, r in _CONFIRM_RE.items() if not k.isascii())
_CONFIRM_TOKEN = re.compile(rf"^(?:{'|'.join(r for k, r in _CONFIRM_RE.items() if k.isascii())})\b|^\s?(?:{_CONFIRM_CJK})")
_STEMS = _alt(EN_SCALES)
_BAD_ILLION = re.compile(r"^\+?\s*-?\s*(?<![A-Za-z])([A-Za-z]*illions?)\b")              # 表里没有的 -illion 词（septillion）
_ORDINAL = re.compile(rf"^\+?\s*-?\s*((?:{_STEMS})ths?)\b", re.I)                         # 序数 / 分数（millionth）
_FOREIGN = re.compile(rf"^\+?\s*-?\s*({_FOREIGN_SCALE})\b\.?", re.I)
_DOT_THOUSANDS = re.compile(r"\d{1,3}(?:\.\d{3}){2,}(?!\d)")  # 1.234.567（欧式千分位）：不猜，直接报错
ABBREVIATIONS = set(EN_ABBR)
SCALE_WORDS = {*EN_SCALES, *EN_STACKED}
HEADER_WINDOW_CHARS = 3000
# 独立的表头写法：(in thousands) / (thousands) / ($ millions) / (USD millions) / (millions of dollars) / ('000)；
# 不带括号的 "in thousands" 后面必须紧跟标点或结尾（"resulted in thousands of cancellations" 不算）
_PLURALS = _alt(w + "s" for w in EN_SCALES)
_HEADER = re.compile(rf"\((?:in\s+)?(?:[A-Z]{{3}}\s+|US\$\s*|[$€£¥]\s*)?({_PLURALS})"
                     r"(?:\s+of\s+[^()]{1,30})?\s*\)"
                     rf"|\bin\s+({_PLURALS})(?=\s*(?:[.:;,)\]]|$))"
                     r"|\(\s*'?(000)s?'?\s*\)", re.I)
_CJK_SC = "".join(k for k in CJK_SCALES if len(k) == 1)   # 单个倍数字：判断一个数是不是更大的中日韩数字的一截（_cjk_reads）
_KR_BIG = "".join(c for c in _CJK_SC if _hangul(c))      # 만 억 조：段与段之间可以隔一个空格（2만 9000、1조 2천억）
_KR_MAN = next(c for c in _KR_BIG if CJK_SCALES[c] == 1e4)
_KR_KILO = next(w for w, f in CJK_WORD_SCALES.items() if f == 1e3 and _hangul(w))   # 천
_CJK_SCALE_ALT = _alt(CJK_SCALES)
# 连写数字的一段的倍数：大倍数字，加上末字是大倍数字的复合词（千万、十亿、천억；不含单独的 千 / 仟 / 천）
_CJK_SEGS = {*CJK_SCALES, *(w for w in CJK_WORD_SCALES if len(w) > 1 and w[-1] in _CJK_SC)}
_CJK_SEG_ALT = _alt(_CJK_SEGS)
_CJK_UNIT_HEAD = re.compile(r"(?:[单單単]位|단위)\s*[:：]\s*([^\n|，,。；;)）]{1,12})")   # v2.8g：表头的单位声明「单位：万元」「(単位:万人)」
_CJK_LEAD = re.compile(rf"^\s?({_CJK_SEG_ALT})")      # v2.11a：连写数字的第一段（3천억 5천만 的 3천억）
_SEG_NUM = r"\s?((?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)"
_CJK_SEG = re.compile(rf"{_SEG_NUM}(?:\s?({_CJK_SEG_ALT}))?")
_CJK_SEG_KR = re.compile(rf"{_SEG_NUM}(?:\s?({_CJK_SEG_ALT}|{_KR_KILO}))?")   # 韩文 만 后面的「N천」段（2만4천）
# 大倍数字后面又接一个表外的大倍数字：京 / 경 只确认不连读，垓 / 해 不支持
_CJK_BIG_AFTER = re.compile(rf"^\s?(?:{_CJK_SCALE_ALT}|{_CONFIRM_CJK}|[{_UNSUPPORTED_CJK}])")
_CJK_NUMERAL_CHARS = "〇零一二三四五六七八九十百千拾佰仟两兩천백십"
# v2.11a：韩文一组之内的「N천M」（4천802억、8천400만、2만4천275、7천478）先换成阿拉伯数字（4802억 ...），再按连写数字读。
# 只认一位数 + 천 + 1–3 位数、后面不再接数字或 백 / 십；억 / 조 后面、自己后面又没有倍数字的（1억2천500）不换：
# 口语里常省掉 만（1억2천500 = 1억2천500만，未核实语料），照字面读会错，留给后面报错
_KR_GROUP = re.compile(rf"(?<![\d.,])([1-9]){_KR_KILO}(\d{{1,3}})(?![\d{_CJK_NUMERAL_CHARS}])(?=\s?([{_KR_BIG}])?)")
# v2.11a：倍数字后面的「千 + SI 基本单位字」是单位不是数词（484亿千瓦时、万亿千瓦时）。只在紧跟倍数字时算：1万2千瓦、2万5千米ドル 照旧报错
_KILO_SI = r"千(?=\s?(?:瓦|米|克|焦|帕|赫|卡|伏|安|字节|比特))"
# 汉字 / 韩文数词（三百、1千）不支持：报错，不静默丢掉；「百分点」（0.5百分点）不算数词
_CJK_NUMERAL = re.compile(rf"^\s?(?!百分)[{_CJK_NUMERAL_CHARS}]")
_CJK_NUMERAL_AFTER_SCALE = re.compile(rf"^\s?(?!百分)(?!{_KILO_SI})[{_CJK_NUMERAL_CHARS}]")
_CJK_WORD = re.compile(rf"^({_CJK_MULT}|{_CONFIRM_CJK})(.*)$")   # v2.8g：scale_word 打头的倍数词也认复合的（千万元 -> 千万，千元 -> 千）
# 前面紧挨「数字 + 倍数字」（만 / 억 / 조 后面可以隔一个空格）：「1億2345万」里的 2345万、「1억 2345만」里的 2345만。
# 倍数字前面必须是数字：하지만、다만、만 30세 里的「만」是普通的字，不是倍数。
# v2.11a：倍数也可以是复合词（3천억 5천만 里的 5천만、3千亿5千万 里的 5千万）；前面紧贴「数字 + 千 / 百」也是一截
# （22조 4천802억 里的 802억、3千5百万 里的 5百万）。_cjk_reads 往前看 _BEFORE_WINDOW 个字符
_CJK_BEFORE = re.compile(rf"\d\s?(?:{_CJK_SEG_ALT})$|\d\s?(?:{_alt(w for w in _CJK_SEGS if w[-1] in _KR_BIG)})\s$"
                         r"|\d[千仟천百佰백]$")
_BEFORE_WINDOW = 8
_SI_UNIT = r"\s?(?:瓦|赫|帕|焦|字节|比特)"   # 兆瓦 / 兆赫 / 兆字节 ...：这里的「兆」是 SI 前缀 mega，和 1e12 歧义，不猜
_MEGA_UNIT = re.compile("兆" + _SI_UNIT)
# 제10조：韩文的法条编号，「조」不是倍数。제 前面是韩文音节的不算（결제 1조 원、실제 3조원、경제、국제）
_ARTICLE = re.compile(r"(?<![가-힣])제\s?$")
# scale_word 的单位部分以大倍数字打头（亿万、万万、千万亿亿）：读不了。韩文的 만 / 억 / 조 / 경 后面接韩文音节时是普通的词（조합원）
_BIG_CHARS = _CJK_SC + "".join(k for k in CONFIRM if not k.isascii()) + _UNSUPPORTED_CJK
_HANGUL_BIG = "".join(c for c in _BIG_CHARS if _hangul(c))
_UNIT_SCALE_LEAD = re.compile(rf"[{''.join(c for c in _BIG_CHARS if not _hangul(c))}]|[{_HANGUL_BIG}](?![가-힣])")


def _cjk_scale_word(sw: str) -> str:
    """scale_word 里倍数字后面接着的单位去掉：万人 / 万人泊 -> 万，兆円 -> 兆，만 명 -> 만（万亿元 -> 万亿）。
    单位部分必须全是文字、不含数词；不是这种写法就原样返回。
    v2.11a：单位部分含倍数字（亿万、万万、千万亿亿）也原样返回（调用方报 unknown scale word，以前 亿万 读成亿）；
    「千 + SI 基本单位字」是单位（万亿千瓦时 -> 万亿）。"""
    m = _CJK_WORD.match(sw)
    u = m.group(2).strip() if m else ""
    ok = (m and u.isalpha() and not set(re.sub(_KILO_SI, "", u)) & set(_CJK_NUMERAL_CHARS)
          and not _UNIT_SCALE_LEAD.match(u))
    return m.group(1) if ok else sw


def _sw_key(scale_word: str) -> tuple:
    """v2.11a：scale_word -> (表里的写法, 是否百分数)。T / Q / MM 照原样（区分大小写，在转小写之前看）；其余转小写，
    英文的几个词之间的空格 / 连字符统一（ten-thousand -> ten thousand），中日韩倍数字后面的单位去掉。
    不认识的写法原样返回，调用方报 unknown scale word。"""
    raw = norm(scale_word)
    if raw in _SW_CASED:
        return raw, False
    sw = raw.lower()
    if sw in PERCENT:
        return "", True
    if re.fullmatch(r"[a-z]+(?:[\s-]+[a-z]+)+", sw):
        sw = _en_key(sw)
    return _cjk_scale_word(sw), False


def _cjk_sum(s: str, m) -> tuple:
    """m 是 s 里的第一个数字，后面紧跟中日韩倍数字：读「数字 + 倍数字」连写（3409万、519万548、1億2345万、2만 9000），
    返回 (各段之和, 第一段的倍数字, 读到的位置)；加法只在这里由代码做。后一段的倍数必须比前一段小，而且整段不满前一段的
    一个倍数单位（35万6713 可以；35万67130、5万3万 报错）；有几段时每段都必须是整数。段与段之间只有韩文
    （만 / 억 / 조 后面）允许一个空格（2만 9000）；「3409万 2025」不连读，按「多于一个数字」报错。
    v2.11a：一段的倍数也可以是末字为大倍数字的复合词（1億3千万、27억6천만、1조 2천억、3万亿5千亿，第一段也行：3천억 5천만）；
    韩文 만 后面可以接「N천」段（2만4천）；韩文一组之内的「N천M」由 parse_value 先换成阿拉伯数字（_kr_groups）。
    中文单独的「千」段（61万1千）、억 / 조 后面不带倍数字的尾段「N천」（1억2천、1억2천500：口语里常指 1억2천만 ...）照旧报错。"""
    first = _CJK_LEAD.match(s[m.end():])
    segs = [(abs(float(m.group().replace(",", ""))), SCALES[first.group(1)], "." in m.group())]
    prev, pos = first.group(1), m.end() + first.end()
    while not (s[pos:pos + 1].isspace() and prev[-1:] not in _KR_BIG) and (
            g := (_CJK_SEG_KR if prev[-1:] == _KR_MAN else _CJK_SEG).match(s, pos)):
        segs.append((float(g.group(1).replace(",", "")), SCALES[g.group(2)] if g.group(2) else 1.0, "." in g.group(1)))
        prev, pos = g.group(2) or "", g.end()
        if not prev:
            break
    for (_, hi, _), (n, f, _) in zip(segs, segs[1:]):
        if f >= hi or n * f >= hi:
            raise ValueError("malformed CJK number: each part must be smaller than the scale before it")
    if len(segs) > 1 and any(dec for _, _, dec in segs):
        raise ValueError("malformed CJK number: decimal in a multi-part number")
    total = sum(n * f for n, f, _ in segs)
    return (-total if m.group().startswith("-") else total), first.group(1), pos


def _kr_groups(s: str) -> str:
    """v2.11a：韩文一组之内的「N천M」换成阿拉伯数字：22조 4천802억 -> 22조 4802억，42억8천400만 -> 42억8400만，
    2만4천275 -> 2만4275，7천478 -> 7478，1천72만 -> 1072만。억 / 조 后面、自己后面又没有倍数字的（1억2천500）不换（_KR_GROUP）。
    没有 M 的「N천」不换（3천억、5천만 是复合倍数词，2만4천 由 _cjk_sum 读）。"""
    def sub(g):
        before = s[:g.start()].rstrip()[-1:]
        if not g.group(3) and before and before in _KR_BIG.replace(_KR_MAN, ""):
            return g.group(0)
        return f"{g.group(1)}{int(g.group(2)):03d}"
    return _KR_GROUP.sub(sub, s)


def _token_at(s: str, i: int, j: int, sw_f, words_only: bool = False):
    """v2.11a：s[i:] 紧跟在一个数后面（这个数从 s[j] 开始）。读那里写着的英文倍数，返回 (倍数, 写法, 终点, 问题)，
    没有倍数返回 None。问题为空 = 按这个倍数乘；"face" = 按面值（小写 t 是吨）；其他 = 报错原因（confirm-only 记号
    没有 scale_word 确认，或者和 scale_word 不一致）。sw_f 是 scale_word 的倍数（没填是 1，不认识是 None）。"""
    rest = s[i:]
    if (w := _WORD_SCALE.match(rest)):
        k = _en_key(w.group(1))
        return SCALES[k], k, i + w.end(), ""
    if words_only:
        return None
    if (a := _CASED.match(rest)):
        return EN_CASED[a.group(0)], a.group(0), i + a.end(), ""
    if (a := _ABBR_GLUED.match(rest) or _ABBR_SPACED.match(rest)
            or (_ABBR_CURRENCY.match(rest) if _CURRENCY_BEFORE.search(s[:j]) else None)
            or (_ABBR_INR.match(rest) if _INR_BEFORE.search(s[:j]) else None)):
        k = a.group(0).strip().lower()
        return {**EN_ABBR, **CURRENCY_ABBR, **INR_ABBR}[k], k, i + a.end(), ""
    if (c := _CONFIRM_TOKEN.match(rest)):
        k = c.group(0).strip()
        f = CONFIRM[k]
        if sw_f == f:
            return f, k, i + c.end(), ""
        if k == "t":
            return f, k, i + c.end(), "face"
        why = (f"ambiguous {k!r} after the number (a multiplier or a unit): give the multiplier in scale_word"
               if sw_f in (None, 1.0) else f"scale conflict: {k!r} in value vs scale_word")
        return f, k, i + c.end(), why
    return None


def _tail_error(tail: str, consumed: bool) -> str:
    """v2.11a：数（和读到的倍数）后面紧跟的词像倍数、但读不了时返回原因（不静默按 1 倍），否则空串。
    consumed = 前面已经读到一个倍数（这时再接倍数词就是两个倍数连写）。billionaire(s)、quad(s) 不是倍数词。"""
    if consumed and (_WORD_SCALE.match(tail) or _FOREIGN.match(tail) or _CJK_BIG_AFTER.match(tail)):
        return "two multipliers in a row (only compounds like 'hundred million' are read)"
    if (b := _BAD_ILLION.match(tail)) and _en_key(b.group(1)).removesuffix("s") not in EN_SCALES:
        return f"unsupported scale word {b.group(1)!r}"
    if (o := _ORDINAL.match(tail)):
        return f"ordinal or fraction {o.group(1)!r} is not a multiplier"
    if (x := _FOREIGN.match(tail)):
        return f"scale word {x.group(1)!r} is not English or CJK (not supported)"
    if (u := re.match(rf"\s?([{_UNSUPPORTED_CJK}])", tail)):
        return f"unsupported scale character {u.group(1)!r}"
    return ""


def parse_value(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (数值, 是否百分数)。数值 = 原文数字 x 倍数；只做这一次乘法。
    倍数可来自原文数字本身（"4.8 million"、"3409万"）或模型填的 scale_word；两者都有且不一致就报错。
    v2.6e：中日韩复合写法（519万548 = 5,190,548）是各段之和（_cjk_sum）；scale_word 里倍数字后面的单位先去掉
    （万人 -> 万、兆円 -> 兆）；'000s = 千；汉字 / 韩文数词（三百、1千）不支持，报错；「兆」后面紧跟 SI 单位（兆瓦）报错；
    倍数字后面又接倍数字（15.4万億）报错。
    v2.11a：英文倍数到 quintillion，叠加词（3 hundred million = 3e8；scale_word 填末词 million 也不算冲突）、5+ million、
    $1.2-billion、缩写 bn / tn / mln / MM ...；confirm-only 记号（T、Q、京、경）要 scale_word 确认；认得出但读不了的
    倍数（septillion、millionth、Millionen、3 million billion、1千兆、垓）报错；复合词连写（3천억、1조 2천억）读成和；
    韩文一组之内的 N천M（22조 4천802억、7천478）先换成阿拉伯数字；货币符号前面的负号（-$1.2B、negative US$5.9 billion）算负数。"""
    s = _kr_groups(norm(value_as_written))
    if _DOT_THOUSANDS.search(s):
        raise ValueError("ambiguous separators: '.' used as a thousands separator")
    if _MEGA_UNIT.search(s) or _MEGA_UNIT.match(norm(scale_word)):
        raise ValueError("ambiguous '兆' before an SI unit: 10^12 or mega-")
    m = _NUM.search(s)
    if not m:
        raise ValueError("no number in value_as_written")
    sw, sw_pct = _sw_key(scale_word)
    sw_f = _SW_FACTOR.get(sw)
    article = bool(_ARTICLE.search(s[:m.start()])) and s[m.end():].lstrip()[:1] == "조"
    cjk = _cjk_sum(s, m) if _CJK_LEAD.match(s[m.end():]) and not article else None
    rest = s[cjk[2]:] if cjk else s[m.end():]
    word = None if cjk else re.match(rf"\s?({_CJK_WORD_ALT})", rest)   # v2.8g：数字后面紧跟复合倍数词（12.5十亿、3.2百万、12,345千人）
    if word:
        rest = rest[word.end():]
    if _NUM.search(rest):
        raise ValueError("more than one number in value_as_written")
    if (cjk or word) and _CJK_BIG_AFTER.match(rest):   # 15.4万億（混写的复合倍数）、3万万、1.3千万万、1千兆、5千亿亿：不猜
        raise ValueError("malformed CJK number: two scale characters in a row")
    # 「千 + SI 单位字」只在紧跟倍数字时算单位（484亿千瓦时）；1万2千瓦 的 千 跟在数字后面，照旧报错
    after_scale = s[len(s) - len(rest) - 1:len(s) - len(rest)] in _CJK_SC if rest else False
    if (_CJK_NUMERAL_AFTER_SCALE if after_scale else _CJK_NUMERAL).match(rest):
        raise ValueError("CJK numerals (e.g. 三百, 1千) are not supported")
    num = cjk[0] if cjk else float(m.group().replace(",", ""))
    # 会计写法 (1,234)；v2.11a：货币符号前面的负号 -$1.2B、negative US$5.9 billion（以前读成正数，BUGS S33）。
    # 两种同时出现（(-$1.2B)、(-1,234)）也只算一次负号
    if (s[:m.start()].strip().startswith("(") and rest.strip().startswith(")")) or _SIGN_BEFORE.search(s[:m.start()]):
        num = -abs(num)
    text_scale = cjk[1] if cjk else word.group(1) if word else None
    text_f, is_pct = (SCALES[text_scale] if text_scale else None), False
    if rest.strip().startswith("%") or rest.strip().lower().startswith(("percent", "per cent")):
        is_pct = True
    elif not cjk and not word and (hit := _token_at(s, len(s) - len(rest), m.start(), sw_f)):
        if hit[3] not in ("", "face"):
            raise ValueError(hit[3])
        if not hit[3]:
            text_f, text_scale, rest = hit[0], hit[1], s[hit[2]:]
    if (why := _tail_error(rest, consumed=text_scale is not None)):
        raise ValueError(why)
    if sw_pct:
        is_pct = True
    if sw not in _SW_FACTOR:
        raise ValueError(f"unknown scale word {scale_word!r}")
    if text_scale and sw and text_f != _SW_FACTOR[sw] and not (
            text_scale in EN_STACKED and EN_SCALES[text_scale.split()[-1]] == _SW_FACTOR[sw]):
        raise ValueError(f"scale conflict: {text_scale!r} in value vs {scale_word!r}")
    factor = 1.0 if cjk else text_f if text_scale else _SW_FACTOR[sw]   # 中日韩写法的倍数已经在各段里乘过
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


_NUM_WORDS = re.compile(r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|"
                        r"sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
                        rf"{_alt(EN_SCALES)}|dozen|half|quarter)\b", re.I)
# 末尾的倍数词：hundred 是数词的一部分（two hundred），只在 scale_word 就是 hundred 时算倍数
# 倍数词前面不能紧贴字母（v2.11a：lac 不能从 lilac、Cadillac 里切出来）
_TRAIL_WORDS = re.compile(rf"(?<=[\da-z+])\s*-?\s*(?<![a-z])({_alt(set(EN_SCALES) - {'hundred'})})s?\b", re.I)
_TRAIL_WORDS_H = re.compile(rf"(?<=[\da-z+])\s*-?\s*(?<![a-z])({_alt(EN_SCALES)})s?\b", re.I)
_TRAIL_STACKED = re.compile(rf"(?<=[\da-z+])\s*-?\s*(?<![a-z])({_alt(EN_STACKED)})s?\b", re.I)
# 认得出、读不了的倍数词：表里没有的 -illion 词、序数 / 分数、非中日韩英的倍数词
_TRAIL_BAD = re.compile(rf"(?<=[\da-z+])\s*-?\s*(?<![a-z])([a-z]*illions?|(?:{_STEMS})ths?|{_FOREIGN_SCALE})\b\.?", re.I)
# 紧挨在倍数前面的另一个倍数（hundred 是数词的一部分，不算：two hundred thousand）。中日韩倍数字只在紧跟阿拉伯数字时算：
# 数千万、近千万、超千亿元、수천억、삼천만 里的 千 / 천 是数的一部分（同 _trailing_multiplier 的候选规则），照旧切出 万 / 亿 / 억
_PREV_MULT = re.compile(rf"(?:\b({_alt(set(EN_SCALES) - {'hundred'})})s?|(?<=\d)\s?({_CJK_MULT}))\s*-?\s*$", re.I)


def _trailing_multiplier(s: str, sw: str = ""):
    """value_as_written 里最后一个数后面的倍数词（4.8 million、two million cases、3409万元、两万、$5bn），返回
    (起点, 终点, 倍数, 写法)；后面还有数（four thousand two hundred、519万548）就不算，返回 None。汉字数词后面的「千」是
    数的一部分（三千），不算倍数。sw = scale_word 的表里写法（_sw_key）。
    v2.11a：词表从倍数表派生，缩写和 confirm-only 记号的读法同 parse_value（_token_at）。叠加词（hundred million）只在紧跟
    数字、或 scale_word 就是这个叠加词时整体算；scale_word 是末词时只切末词（two hundred thousand + thousand -> two hundred,
    1e3）。以下报错：末尾是认得出、读不了的倍数（septillion、millionth、millones，后面不再有数）；confirm-only 记号没有
    scale_word 确认；倍数后面紧接大倍数字（5千亿亿）；两个倍数连写（3 million billion、3万 million）。"""
    sw_f = _SW_FACTOR.get(sw)
    nums = re.escape(_CJK_NUMERAL_CHARS)
    cands = []   # (起点, 终点, 倍数, 写法, 问题)
    for w in (_TRAIL_WORDS_H if sw in ("hundred", "hundreds") else _TRAIL_WORDS).finditer(s):
        cands.append((w.start(), w.end(), SCALES[w.group(1).lower()], w.group(1).lower(), ""))
    for w in _TRAIL_STACKED.finditer(s):
        k = _en_key(w.group(1))
        if not s[w.start() - 1].isalpha() or sw in (k, k + "s"):
            cands.append((w.start(), w.end(), SCALES[k], k, ""))
    for n in _NUM.finditer(s):
        if (t := _token_at(s, n.end(), n.start(), sw_f)) and t[1] not in SCALE_WORDS:
            cands.append((n.end(), t[2], t[0], t[1], t[3]))
    for m in re.finditer(rf"(?<=[\d{nums}])\s?({_CJK_MULT})", s):
        if m.group(1) in ("千", "仟") and not s[m.start() - 1].isdigit():
            continue
        if m.group(1) == "조" and _ARTICLE.search(re.sub(r"[\d,.]+$", "", s[:m.start()])):
            continue   # 제10조
        cands.append((m.start(), m.end(), SCALES[m.group(1)], m.group(1), ""))
    for b in _TRAIL_BAD.finditer(s):
        if _en_key(b.group(1)).removesuffix("s") not in EN_SCALES:
            cands.append((b.start(), b.end(), None, b.group(1), _tail_error(b.group(0), False)))
    for h in re.finditer(rf"(?<=[\d{nums}])\s?([{_UNSUPPORTED_CJK}])", s):
        cands.append((h.start(), h.end(), None, h.group(1), f"unsupported scale character {h.group(1)!r}"))
    if not cands:
        return None
    end = max(c[1] for c in cands)
    last = [c for c in cands if c[1] == end]   # 同一处结尾的叠加词和末词：scale_word 是哪个就取哪个，没填取叠加词（长的）
    same = [c for c in last if c[2] == sw_f] if sw_f not in (None, 1.0) else []
    st, en, f, k, why = same[0] if same else min(last, key=lambda c: c[0])
    tail = s[en:]
    if f is not None and _CJK_BIG_AFTER.match(tail):
        raise ValueError("malformed CJK number: two scale characters in a row")
    if f is not None and _WORD_SCALE.match(tail):   # 3万 million：million 前面不是数，不算候选
        raise ValueError("two multipliers in a row (only compounds like 'hundred million' are read)")
    if re.search(rf"[\d{nums}]", re.sub(_KILO_SI, "", tail)) or _NUM_WORDS.search(tail):
        return None
    if why == "face":
        return None
    if why:
        raise ValueError(why)
    if (p := _PREV_MULT.search(s[:st])) and not (p.group(1) and f"{p.group(1).lower()} {k}" in EN_STACKED):
        raise ValueError("two multipliers in a row (only compounds like 'hundred million' are read)")
    return st, en, f, k


def split_multiplier(value_as_written: str, scale_word: str = "") -> tuple:
    """返回 (去掉倍数词的写法, 倍数)。倍数由代码定：scale_word 的，或 value_as_written 末尾写着的（_trailing_multiplier）；
    两者都有而不一致就报错。核对模型只看去掉倍数词的写法（v2.8o 探针：倍数交给模型判，「4.8 million」读成 4.8、
    表头「万」的 4,774.10 读成 477410 都被它判成对的）。
    中日韩复合写法（519万548）里的倍数字后面还有数，不算末尾的倍数：这时 scale_word 必须为空，number 写整个数。"""
    s, swn = norm(value_as_written), _sw_key(scale_word)[0]
    if swn not in _SW_FACTOR:
        raise ValueError(f"unknown scale word {scale_word!r}")
    m = _trailing_multiplier(s, swn)
    if m:
        st, en, f, k = m
        if swn and _SW_FACTOR[swn] != f:
            raise ValueError(f"scale conflict: {k!r} in value vs {scale_word!r}")
        return (s[:st] + s[en:]).strip(), f
    nums = re.escape(_CJK_NUMERAL_CHARS)
    if swn and re.search(rf"[\d{nums}]\s?(?:{_CJK_SCALE_ALT})[\d{nums}]", s):
        raise ValueError("compound CJK number (519万548): leave scale_word empty and give the whole number")
    return s, _SW_FACTOR[swn]


# ---------- v2.8r：单位里的倍数（万元、USD million、(10,000 CNY)） ----------
# 用户 10-18 的调研（XBRL「金额以元为单位」、SDMX UNIT_MEASURE 不含倍数、Recognizers-Text 1000万元 -> value 10000000 + unit 元）：
# 倍数只能在一个地方、只乘一次；乘完之后单位里不能再有倍数。恒顺 v2.8p：代码按 scale_word 乘了 万，unit 仍写「万元 (10,000 CNY)」，
# 单位核对据此又乘 10^4（6089 万瓶）。per / 每 / '/' 后面的是比率的分母（births per 1,000 women、每万人），不是倍数，不动；
# 「千」单独出现不算（千克、千米、千瓦是 SI 前缀）；1,000 / 1000 这种裸数字也不算（1000 ml）
# v2.11a：cjk、word 两组从倍数表派生。不含单独的 千 / 仟 / 천 / 兆 / 조（千克、兆瓦、조합원）和 hundred；缩写只认 mn / mln / bn，
# 不加 tn / bln / trn（这个正则不分大小写，TN 是州名；现有的 mn 已经会撞 MN，见 BUGS）
_UNIT_CJK = {w for w in {*CJK_SCALES, *CJK_WORD_SCALES} if not (len(w) == 1 and SCALES[w] in (1e3, 1e12))}
_UNIT_WORDS = {w: f for w, f in EN_SCALES.items() if w != "hundred"}
_UNIT_ABBR = ("mn", "mln", "bn")
_UNIT_MULT = re.compile(
    rf"(?P<cjk>{_alt(_UNIT_CJK)})"
    r"|(?<![\w,.])(?P<num>100,000,000|100 million|10,000|10000)(?![\d,.])(?!\s*(?:ml|g|kg|km|l|cc)\b)"
    rf"|\b(?P<word>(?:{_alt(EN_STACKED).replace(r'[\s-]+', '[- ]')}|{_alt(_UNIT_WORDS)})s?|{_alt(_UNIT_ABBR)})\b"
    r"|(?P<k>'000s?|\b000s\b)", re.I)
_UNIT_MULT_FACTOR = {"100,000,000": 1e8, "100 million": 1e8, "10,000": 1e4, "10000": 1e4,
                     **{w: f for k, f in EN_STACKED.items() for w in (k, k.replace(" ", "-"))}, **_UNIT_WORDS,
                     **{a: EN_ABBR[a] for a in _UNIT_ABBR}, "'000": 1e3, "000": 1e3}
# 倍数只写在 unit 里时挪到数上用的写法（pipeline._pair_unit）：每个倍数一个写法；v2.8r 已有的 8 个不变，v2.11a 只给新增的倍数
# （1e13–1e16、1e18）各补一个。1e10 / 1e11（百亿、千亿）v2.8r 起单位里认得出、但没有写法，照旧不挪（不改已有行为）
_UNIT_SPELLING = ("thousand", "万", "十万", "million", "千万", "亿", "billion", "trillion",
                  "十万亿", "百万亿", "quadrillion", "亿亿", "quintillion")
SCALE_FOR_FACTOR = {SCALES[w]: w for w in _UNIT_SPELLING}


def unit_multipliers(unit: str) -> list:
    """unit 里的倍数：[(match, 倍数)]，比率分母（per / 每 / '/' 后面）不算。"""
    out = []
    for m in _UNIT_MULT.finditer(unit):
        if re.search(r"(?:\bper|每|/)\s*$", unit[:m.start()], re.I):
            continue
        t = m.group(0).lower()
        if m.group("cjk"):
            f = SCALES[t]
        else:
            t = re.sub(r"s$", "", t.strip("'")) if m.group("word") or m.group("k") else t
            f = _UNIT_MULT_FACTOR.get(t.replace("'", "")) or _UNIT_MULT_FACTOR.get(t)
        if f:
            out.append((m, f))
    return out


def strip_unit_multiplier(unit: str, factor: float) -> tuple:
    """去掉 unit 里倍数为 factor 的写法，返回 (新 unit, 原因)。unit 里还有别的倍数（scale_word 是万、unit 写亿元）：原因非空，调用方丢点。
    去掉后清理空括号和多余的标点、空格：「万元 (10,000 CNY)」->「元 (CNY)」，「USD million」->「USD」，「CNY yuan (100 million)」->「CNY yuan」。"""
    hits = unit_multipliers(unit)
    other = [m.group(0) for m, f in hits if not math.isclose(f, factor)]
    if other:
        return unit, f"unit {unit!r} names a different multiplier ({', '.join(other)}) than the number's ({factor:g})"
    s = unit
    for m, _ in sorted(hits, key=lambda x: -x[0].start()):
        s = s[:m.start()] + s[m.end():]
    s = re.sub(r"\(\s*[,;=]?\s*\)", "", s)
    s = re.sub(r"\(\s*[,;]\s*", "(", re.sub(r"\s*[,;]\s*\)", ")", s))
    s = re.sub(r"\(\s+", "(", re.sub(r"\s+\)", ")", s))
    s = re.sub(r"\s{2,}", " ", s).strip(" ,;")
    return s, ""


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
    不带倍数字的数后面接「千」（12,345千人 里的 12,345）不算，和 v2.6d 一样按原文数字取值。v2.11a：④ 里紧跟倍数字的
    「千 + SI 基本单位字」是单位（484亿千瓦时）；① 也认复合倍数词和「数字 + 千 / 百」（3천억 5천만 里的 5천만、
    22조 4천802억 里的 802억）。
    "mega" = 读到的数以「兆」结尾、后面紧跟 SI 单位（兆瓦）。"article" = 读到的数以「조」结尾、前面是「제」（제10조 是法条编号）。"""
    for m in re.finditer(r"(?<![\d.,])" + re.escape(vw) + r"(?!\d|[.,]\d)", quote_n):
        tail, last, used = quote_n[m.end():], vw[-1], False
        if cj and last not in _CJK_SC and (g := re.match(r"\s?" + re.escape(cj), tail)):
            tail, last, used = tail[g.end():], cj[-1], True
        kilo = rf"(?!{_KILO_SI})" if last in _CJK_SC else ""
        if last == "조" and _ARTICLE.search(quote_n[:m.start()]):
            yield used, "article"
        elif (_CJK_BEFORE.search(quote_n[max(0, m.start() - _BEFORE_WINDOW):m.start()])
                or re.match(rf"\s?[{_CJK_SC}]", tail)
                or (last in _CJK_SC and re.match(r"\s?\d" if last in _KR_BIG else r"\d", tail))
                or ((used or set(vw) & set(_CJK_SC)) and re.match(rf"(?!百分){kilo}[{_CJK_NUMERAL_CHARS}]", tail))):
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
    if reads[0] == "article":
        return "'제N조' in the quote is an article number, not a multiplier"
    return "value_as_written is only part of a larger CJK number in the quote"


def _written_factor(vw: str, sw: str):
    """v2.11a：value_as_written 末尾自带的倍数（$3.5B、100T、5+ million、3409万）；sw（表里写法）用来确认 confirm-only
    记号。没有、或者写法本身读不了时返回 None。"""
    try:
        m = _trailing_multiplier(norm(vw), sw)
    except ValueError:
        return None
    return m[2] if m else None


def _factor_after(quote_n: str, vw: str, f: float) -> bool:
    """v2.11a：quote 里 vw 后面紧跟着倍数为 f 的写法：单词、缩写、confirm-only 记号，读法同 parse_value（_token_at，
    k / m / b 只认紧贴或货币符号后面隔一个空格）；vw 不以数字结尾时只认单词（two + million）。"""
    nm = list(_NUM.finditer(vw))
    last = nm[-1] if nm and nm[-1].end() == len(vw) else None
    for m in re.finditer(r"(?<![\d.,])" + re.escape(vw), quote_n):
        t = _token_at(quote_n, m.end(), m.start() + (last.start() if last else len(vw)), f, words_only=last is None)
        if t and not t[3] and t[0] == f:
            return True
    return False


def scale_supported(scale_word: str, quote_n: str, context_n: str, value_written: str = "") -> str:
    """倍数词必须有原文依据。返回依据（quote / page_header / none_needed），否则空串。
    - 缩写（k、m、b、bn ...）：只认紧贴数字的写法（value_as_written 本身带着，或 quote 里数字后面紧跟），没有页面级依据。
    - 单词（thousand、million ...）：quote 里数字后面紧跟这个词；或者 quote / context_n（调用方给的、quote 前面
      HEADER_WINDOW_CHARS 个字符的原文）里有独立的表头写法（见 _HEADER）。'000s 按 thousand 处理。
    - v2.6e 中日韩倍数字（万、億、만 ...；scale_word 里后面的单位先去掉）：和缩写一样只认紧贴数字的写法，没有页面级依据；
      quote 里「数字 + 倍数字」必须是一个完整的数（_cjk_reads）：前面不挨「数字 + 倍数字」，后面不再接
      倍数字或连读的数字（「519万548」只写 519 + 万会丢掉 548，「15.4万亿」只写 15.4 + 万会丢掉亿，「1億2345万」只写 2345 + 万会丢掉 1 億）。
    - v2.11a 英文 scale_word 按倍数比，不按拼写比：value_as_written 自带的倍数等于 scale_word 的倍数（$3.5B 配 billion），
      或者 quote 里 vw 后面紧跟这个倍数的任一写法（100T、100t 配 trillion，5+ million，~8Q 配 quadrillion）就是 quote。
      所以 scale_word 填了 trillion 时 quote 里的 3.5t 也算依据（代码解析的数不交模型核对，pipeline.verify_point 的 v2.8o 约定）。
      表头依据照旧只认单词。京 / 경（confirm-only）：value_as_written 或 quote 里数字后面紧跟着才算。"""
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
    if cj in CONFIRM and not cj.isascii():
        tok = _CONFIRM_RE[cj]
        if vw and (re.search(rf"\d\s?{tok}", vw) or re.search(rf"(?<![\d.,]){re.escape(vw)}\s?{tok}", quote_n)):
            return "quote"
        return ""
    key = _sw_key(scale_word)[0]
    base = key[:-1] if key.endswith("s") and key[:-1] in SCALE_WORDS else key
    base = "thousand" if base in ("000s", "'000s") else base
    if base in ABBREVIATIONS:
        if vw and re.search(rf"\d\s?{re.escape(base)}$", vw, re.I):
            return "quote"
        if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s?{re.escape(base)}(?![A-Za-z])", quote_n, re.I):
            return "quote"
    elif base in SCALE_WORDS:
        b = _alt([base])
        if vw and re.search(rf"(?:\d|[a-z])\s*{b}s?\b", vw, re.I):   # v2.8o：单词写法（two million）也算紧贴
            return "quote"
        if vw and re.search(rf"(?<![\d.,]){re.escape(vw)}\s*(?:-\s*)?{b}s?\b", quote_n, re.I):
            return "quote"
    f = _SW_FACTOR.get(key)
    if f in (None, 1.0):
        return ""
    if vw and (_written_factor(vw, key) == f or _factor_after(quote_n, vw, f)):
        return "quote"
    if base not in SCALE_WORDS:
        return ""
    for m in _HEADER.finditer(quote_n + " | " + context_n):
        word = (m.group(1) or m.group(2) or "").lower()
        if (word and SCALES.get(word[:-1]) == f) or (m.group(3) and f == 1e3):
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


def leak_numbers(true_value: float) -> set:
    """v2.8p：leak_forms 各种写法对应的数值（原值、四舍五入到百 / 千、x.x / x.xx thousand、0.xxx / x.xx million），
    用来和抽取员读出的数比（单词写的数页面文字里搜不到：two million、四百万）。"""
    v = float(true_value)
    out = {v}
    if v == int(v):
        n = int(v)
        if abs(n) >= 10_000:
            out |= {float(round(n, -2)), float(round(n, -3)), round(n / 1e3, 1) * 1e3, round(n / 1e3, 2) * 1e3}
        if abs(n) >= 100_000:
            out |= {round(n / 1e6, 3) * 1e6, round(n / 1e6, 2) * 1e6}
    else:
        out |= {round(v, 1), round(v, 2)}
    return out


def leak_number_hit(x, values) -> bool:
    """x 是不是登记值（真值等）的某种写法对应的数。values：一个数或一组数，空 = 不查。"""
    if not values or not isinstance(x, (int, float)) or isinstance(x, bool):
        return False
    vals = values if isinstance(values, (list, tuple, set)) else [values]
    return any(math.isclose(x, t, rel_tol=1e-9, abs_tol=1e-9) for v in vals for t in leak_numbers(v))


def leak_point_hit(p: dict, values) -> bool:
    """一个通过核对的点是不是登记值（pipeline._process_page 命中就整页作废）。抽取员读的数（reading）：leak_number_hit，
    含四舍五入写法（v2.8p）。v2.11a：代码解析的中日韩写法（2만4천275명、1億3千万、22조 4천802억）只比精确值：这些写法
    v2.10i 解析不了、走读数路径被比过，现在代码能读，页面哨兵的写法表（_cjk_exact_forms）又没有；四舍五入写法照旧不比（C3）。
    其他代码解析的写法不比（页面哨兵已经按写法搜过整页）。"""
    if not values:
        return False
    if p.get("reading"):
        return any(leak_number_hit(p.get(k), values) for k in ("value", "value_low", "value_high"))
    if not re.search(rf"[{_BIG_CHARS}{_CJK_NUMERAL_CHARS}]", str(p.get("value_as_written") or "")):
        return False
    vals = values if isinstance(values, (list, tuple, set)) else [values]
    x = p.get("value")
    return isinstance(x, (int, float)) and not isinstance(x, bool) and any(
        v is not None and math.isclose(x, float(v), rel_tol=1e-9, abs_tol=1e-9) for v in vals)


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

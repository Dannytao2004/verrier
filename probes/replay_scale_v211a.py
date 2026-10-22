"""v2.11a 离线检查（大数单位）：新旧两份 evidence.py 对同一批输入的读法，逐条比较。不调模型、不联网，不改 results/、data/。

1. --readings：一张必读写法表（1.3 quadrillion、1.3千万亿、$3.5B 配 billion ...），旧代码和新代码各自的输出。
2. 默认：已存运行（results/**/state.json）里每个通过代码核对的点（state["points"]），页面原文在 data/raw/agent/ 有缓存的，
   用和 pipeline 一样的参数重跑一遍 verify_point：旧的（pipeline.verify_point + 旧 evidence.py）和新的各一遍，
   列出 value、保留 / 丢弃、原因、单位、倍数依据、是否走读数路径有变化的点。
   旧 evidence.py 用 `git show <ref>:triangulate/agent/evidence.py` 取出，放在系统临时目录（仓库外），按文件路径导入；
   pipeline.py 里的 verify_point / _pair_unit 要和 <ref> 的源码相同（不同就退出；v2.11a 只改了 _process_page 的泄漏比对），
   旧的 verify_point / _pair_unit 是同一份代码换成旧 evidence 的副本。
   重建的输入（和 pipeline 调用时的参数不完全一样，下面三处是近似）：quote 是存下来的 200 字以内的那段
   （QUOTE_STORE_CHARS），不是抽取员给的整句；unit 用 unit_as_written（有的话）；scale_word 用存下来的，但倍数是
   从 unit 挪到数上的点（_pair_unit 把 scale_word 改写成了 SCALE_FOR_FACTOR 的写法，抽取员原来给的是空串）复原成空串
   （判据：sw 为空时旧代码能复现存下来的 value 和 scale_word）；读数用 reading_from_extractor（核对模型改过的话）。
   as_of、page_date、url、方向是否 base_rates 都取自 state.json。
3. 丢点一侧只能部分重放：dropped_points 只存了原因、name、value_as_written[:40]，没有 quote。这里对原因串以 number: 开头、
   或者是 scale word not supported 的丢点重跑数字和倍数这一步（parse_value / 只看 vw 的 scale_supported），按原因类别计数，
   不是完整的核对。scale_word 从原因串里取得到的才用（unknown scale word 'x'、in value vs 'x'、scale word 'x'），否则用空串。
4. 回测题（triangulate.forecast.QUESTIONS 有登记值）里的保留点：新代码的 ev.leak_point_hit 会不会让这一页作废
   （v2.11a 起代码解析的中日韩写法也按精确值比）。

用法：.venv/Scripts/python.exe probes/replay_scale_v211a.py [--ref v2.10i] [--readings] [--json probes/out/x.json]
"""
import argparse
import ast
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import types
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as NEW  # noqa: E402
from triangulate.agent import pipeline as P  # noqa: E402

COMPARE = ("value", "value_low", "value_high", "unit", "scale_word", "scale_basis", "value_check")


def _func_src(src: str, name: str) -> str:
    for node in ast.parse(src).body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(src, node)
    return ""


def load_old(ref: str):
    """<ref> 的 evidence.py 放到系统临时目录（仓库外）再导入；pipeline.py 必须和 <ref> 的相同。"""
    old_pipe = subprocess.run(["git", "show", f"{ref}:triangulate/agent/pipeline.py"], cwd=ROOT, capture_output=True,
                              check=True).stdout.decode("utf-8")
    cur_pipe = (ROOT / "triangulate" / "agent" / "pipeline.py").read_text(encoding="utf-8")
    for name in ("verify_point", "_pair_unit"):
        if _func_src(old_pipe, name) != _func_src(cur_pipe, name):
            sys.exit(f"pipeline.{name} differs from {ref}: the old verify_point would not be {ref}'s")
    src = subprocess.run(["git", "show", f"{ref}:triangulate/agent/evidence.py"], cwd=ROOT, capture_output=True,
                         check=True).stdout
    d = Path(tempfile.gettempdir()) / "replay_scale_v211a"
    d.mkdir(exist_ok=True)
    f = d / f"evidence_{re.sub(r'[^A-Za-z0-9._-]', '_', ref)}.py"
    f.write_bytes(src)
    spec = importlib.util.spec_from_file_location("evidence_old", f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    g = dict(P.__dict__, ev=mod)   # 旧的 verify_point / _pair_unit：同一份代码，ev 换成旧模块
    g["_pair_unit"] = types.FunctionType(P._pair_unit.__code__, g, "_pair_unit")
    g["verify_point"] = types.FunctionType(P.verify_point.__code__, g, "verify_point", P.verify_point.__defaults__)
    return mod, g["verify_point"]


def run(fn, *a):
    try:
        return "ok", fn(*a)
    except ValueError as e:
        return "error", str(e)


# ---------- 1. 必读写法表 ----------
def _vp_case(evm, vp, quote, vw, sw, unit="tokens", **kw):
    raw = {"name": "x", "value_as_written": vw, "scale_word": sw, "unit": unit, "period_start": "2025-01-01",
           "period_end": "2025-12-31", "quote": quote, **kw}
    p, why = vp(raw, evm.norm("2025 " + quote), date(2026, 10, 22), None, False)
    if p is None:
        return f"dropped: {why}"
    extra = " (reading, pending)" if p.get("value_check") else ""
    return f"kept {p['value']:g} unit={p['unit']!r} sw={p['scale_word']!r} basis={p['scale_basis']}{extra}"


# (标签, 怎么跑, 参数)；parse = parse_value(vw, sw)，split = split_multiplier，vp = verify_point（quote 原样作页面文字）
READINGS = [
    ("1.3 quadrillion, sw quadrillion", "parse", ("1.3 quadrillion", "quadrillion")),
    ("1.3 quadrillion, sw ''", "parse", ("1.3 quadrillion", "")),
    ("40 quadrillion tokens per quarter (vw 40, unit 'quadrillion tokens per quarter')", "vp",
     ("Exponential View estimates the total tokens processed across all providers at 40 quadrillion tokens per quarter",
      "40", "", "quadrillion tokens per quarter")),
    ("1.3千万亿", "parse", ("1.3千万亿", "")),
    ("3천억", "parse", ("3천억", "")),
    ("1조 2천억", "parse", ("1조 2천억", "")),
    ("27억6천만", "parse", ("27억6천만", "")),
    ("2만4천275", "parse", ("2만4천275", "")),
    ("$3.5B + sw billion (verify_point, menlovc quote)", "vp",
     ("Enterprise LLM spend more than doubled in just six months, rising from $3.5B in November 2024", "$3.5B", "billion",
      "USD")),
    ("100T + sw trillion (verify_point, epoch.ai quote)", "vp",
     ("OpenRouter's State of AI report looks at 100T tokens worth of production data", "100T", "trillion")),
    ("100T + sw '' (parse_value)", "parse", ("100T", "")),
    ("100T + sw '' + number 100 (verify_point, reading path)", "vp",
     ("OpenRouter's State of AI report looks at 100T tokens worth of production data", "100T", "", "tokens",
      {"number": 100})),
    ("5+ million + sw million (verify_point, a16z quote)", "vp",
     ("OpenRouter now serves over 5+ million developers", "5+ million", "million", "developers")),
    ("$1.2-billion", "parse", ("$1.2-billion", "")),
    ("5 lakh", "parse", ("5 lakh", "")),
    ("3 crore", "parse", ("3 crore", "")),
    ("2 milliard", "parse", ("2 milliard", "")),
    ("$5MM", "parse", ("$5MM", "")),
    ("vw 9.8, sw 万亿千瓦时", "parse", ("9.8", "万亿千瓦时")),
    ("vw 484, sw 亿千瓦时 (verify_point, unit 千瓦时, 缓存页原句)", "vp",
     ("2026年1-2月全国绿电交易电量484亿千瓦时,同比增长7.6%", "484", "亿千瓦时", "千瓦时")),
    ("vw 484亿 (verify_point, unit 千瓦时)", "vp",
     ("2026年1-2月全国绿电交易电量484亿千瓦时,同比增长7.6%", "484亿", "", "千瓦时")),
    ("~8Q/day + sw quadrillion (verify_point)", "vp",
     ("| End-2026 effective capacity (~8Q/day) | 160,000/day |", "8", "quadrillion", "tokens/day")),
    # 反例：意思不能变
    ("3Q 2026", "parse", ("3Q 2026", "")),
    ("4.8 m", "parse", ("4.8 m", "")),
    ("3경기", "parse", ("3경기", "")),
    ("500兆瓦", "parse", ("500兆瓦", "")),
    ("3 billionaires", "parse", ("3 billionaires", "")),
    ("97.3 quads", "parse", ("97.3 quads", "")),
    ("24,500 t", "parse", ("24,500 t", "")),
    ("1.3 quintillion", "parse", ("1.3 quintillion", "")),
    ("2 septillion", "parse", ("2 septillion", "")),
    ("1 millionth", "parse", ("1 millionth", "")),
    ("60.6 mil millones", "parse", ("60.6 mil millones", "")),
    ("84 millones 176 mil 999 dólares (reading path: split_multiplier)", "split", ("84 millones 176 mil 999 dólares", "")),
    ("84 millones 176 mil 999 dólares (verify_point, number 84176999)", "vp",
     ("Las exportaciones sumaron 84 millones 176 mil 999 dólares", "84 millones 176 mil 999 dólares", "", "USD",
      {"number": 84176999})),
    # 补充：叠加词、复合写法、韩文法条
    ("two hundred thousand + sw thousand + number 200 (verify_point)", "vp",
     ("Sales reached two hundred thousand pies", "two hundred thousand", "thousand", "pies", {"number": 200})),
    ("3 hundred million", "parse", ("3 hundred million", "")),
    ("3 million billion", "parse", ("3 million billion", "")),
    ("1億3千万", "parse", ("1億3千万", "")),
    ("3万亿5千亿", "parse", ("3万亿5千亿", "")),
    ("61万1千", "parse", ("61万1千", "")),
    ("1千兆", "parse", ("1千兆", "")),
    ("5千亿亿 (split)", "split", ("5千亿亿", "")),
    ("sw 亿万", "parse", ("5", "亿万")),
    ("제10조", "parse", ("제10조", "")),
    ("2垓", "parse", ("2垓", "")),
    ("3京", "parse", ("3京", "")),
    ("$5 bn", "parse", ("$5 bn", "")),
    ("$5.8 B", "parse", ("$5.8 B", "")),
    ("5+ million, sw ''", "parse", ("5+ million", "")),
    # v2.11a 审查之后补的（quote 是缓存页原句）
    ("-$1.2B + sw billion", "parse", ("-$1.2B", "billion")),
    ("negative $9.14bn + sw billion (verify_point, fc_meta_capex)", "vp",
     ("Gross margin is seen at 80.16%, capex at $40.97bn and free cash flow at negative $9.14bn.", "negative $9.14bn",
      "billion", "USD")),
    ("negative US$5.9 billion (fc_googl_tokens p97)", "parse", ("negative US$5.9 billion", "billion")),
    ("1万2千瓦", "parse", ("1万2千瓦", "")),
    ("2万5千米ドル", "parse", ("2万5千米ドル", "")),
    ("484亿千瓦时", "parse", ("484亿千瓦时", "")),
    ("数千万 (split)", "split", ("数千万", "")),
    ("수천억 원 (split)", "split", ("수천억 원", "")),
    ("超千亿元 + sw 亿 + number 1000 (verify_point)", "vp", ("超千亿元", "超千亿元", "亿", "CNY", {"number": 1000})),
    ("결제 1조 원", "parse", ("결제 1조 원", "")),
    ("vw 10조, quote '법 제10조에 따라' (verify_point)", "vp", ("법 제10조에 따라", "10조", "", "articles")),
    ("R$ 38 milhões", "parse", ("R$ 38 milhões", "")),
    ("195 mld. (捷克)", "parse", ("195 mld.", "")),
    ("vw 5천만, quote '3천억 5천만 원' (verify_point)", "vp", ("3천억 5천만 원", "5천만", "", "원")),
    ("vw 802억, quote '22조 4천802억 원' (verify_point)", "vp", ("총액이 22조 4천802억 원으로", "802억", "", "원")),
    ("22조 4천802억", "parse", ("22조 4천802억", "")),
    ("42억8천400만", "parse", ("42억8천400만", "")),
    ("7천478", "parse", ("7천478", "")),
    ("1천72만", "parse", ("1천72만", "")),
    ("1억2천500", "parse", ("1억2천500", "")),
    ("Rs 500 cr", "parse", ("Rs 500 cr", "")),
    ("$500 Cr (会计的贷方，不是 crore)", "parse", ("$500 Cr", "")),
    ("5 Cadillac (split，lac 不能从词里切出来)", "split", ("5 Cadillac", "")),
    ("5 lacs", "parse", ("5 lacs", "")),
    ("$5 bil", "parse", ("$5 bil", "")),
    ("$5BB", "parse", ("$5BB", "")),
    ("$5mm", "parse", ("$5mm", "")),
    ("5mm", "parse", ("5mm", "")),
    ("$3MMM", "parse", ("$3MMM", "")),
    ("3千米 (BUGS S32，照旧)", "parse", ("3千米", "")),
    ("vw 3.5, unit 千亿元 (verify_point, 1e11 照旧不挪)", "vp", ("公司营收3.5千亿元", "3.5", "", "千亿元")),
]


def readings(old_ev, old_vp):
    rows = []
    for label, how, args in READINGS:
        out = []
        for evm, vp in ((old_ev, old_vp), (NEW, P.verify_point)):
            if how == "parse":
                st, r = run(evm.parse_value, *args)
                out.append(f"{r[0]:g}" if st == "ok" else f"error: {r}")
            elif how == "split":
                st, r = run(evm.split_multiplier, *args)
                out.append(f"({r[0]!r}, {r[1]:g})" if st == "ok" else f"error: {r}")
            else:
                quote, vw, sw, *rest = args
                unit = rest[0] if rest else "tokens"
                kw = rest[1] if len(rest) > 1 else {}
                out.append(_vp_case(evm, vp, quote, vw, sw, unit, **kw))
        rows.append({"case": label, "old": out[0], "new": out[1], "changed": out[0] != out[1]})
    return rows


# ---------- 2. 已存保留点的重放 ----------
def page_text(qid: str, url: str, ts):
    k = hashlib.sha1(f"{url}|{ts or 'live'}".encode("utf-8")).hexdigest()[:16]
    f = ROOT / "data" / "raw" / "agent" / qid / f"{k}.txt"
    return f.read_text(encoding="utf-8") if f.exists() else None


def categories(st: dict) -> dict:
    out = {}
    for d in (st.get("plan") or {}).get("directions") or []:
        out[d.get("id")] = d.get("category")
    for d in st.get("directions") or []:
        out[d.get("id")] = d.get("category")
    return out


def raw_of(p: dict) -> dict:
    raw = {k: p.get(k) for k in ("name", "value_as_written", "scale_word", "period_start", "period_end",
                                 "published_at_if_visible", "quote")}
    raw["unit"] = p.get("unit_as_written") if p.get("unit_as_written") is not None else p.get("unit")
    reading = p.get("reading_from_extractor") or p.get("reading")
    if reading:
        raw.update(reading)
    return raw


def summary(res) -> dict:
    p, why = res
    if p is None:
        return {"kept": False, "reason": why}
    return {"kept": True, **{k: p.get(k) for k in COMPARE}}


def _split(evm, p: dict):
    """存下来的点的 split_multiplier（unit_review._multiplier 的倍数、核对模型看的 written_number），和调用方一样百分数传空串。"""
    sw = p.get("scale_word") or ""
    st, r = run(evm.split_multiplier, p.get("value_as_written") or "", "" if evm.norm(sw).lower() in evm.PERCENT else sw)
    return list(r) if st == "ok" else f"error: {r}"


def _leak_values() -> dict:
    from triangulate.forecast import QUESTIONS
    return {q["id"]: q.get("leak_values") or ([q["answer_value"]] if q.get("answer_value") is not None else None)
            for q in QUESTIONS}


def replay(old_ev, old_vp):
    """返回 (统计, verify_point 结果有变化的点, split_multiplier 结果有变化的点, 新代码的泄漏比对会命中的点)。"""
    texts, stats, diffs, split_diffs, leaks = {}, Counter(), [], [], []
    lv = _leak_values()
    for f in sorted(ROOT.glob("results/**/state.json")):
        st = json.loads(f.read_text(encoding="utf-8"))
        pts = st.get("points") or []
        if not pts or not st.get("as_of"):
            continue
        as_of, cats, qid = date.fromisoformat(st["as_of"]), categories(st), st.get("qid")
        run_name = str(f.parent.relative_to(ROOT)).replace("\\", "/")
        for p in pts:
            stats["kept_points"] += 1
            if (so := _split(old_ev, p)) != (sn := _split(NEW, p)):
                split_diffs.append({"run": run_name, "id": p.get("id"), "value_as_written": p.get("value_as_written"),
                                    "scale_word": p.get("scale_word"), "reading": bool(p.get("reading")),
                                    "old": so, "new": sn})
            url = p.get("source_url") or ""
            key = (qid, url, p.get("snapshot_ts"))
            if key not in texts:
                t = page_text(qid, url, p.get("snapshot_ts")) if p.get("via") != "api" else None
                texts[key] = None if t is None else NEW.norm(t[:P.MAX_CHARS_TO_EXTRACTOR])
            text_n = texts[key]
            if text_n is None:
                stats["no_cached_page"] += 1
                continue
            stats["replayed"] += 1
            pd = date.fromisoformat(p["page_date"]) if p.get("page_date") else None
            rest = (text_n, as_of, pd, cats.get(p.get("direction_id")) == "base_rates")
            raw = raw_of(p)
            if p.get("unit_as_written") is not None and raw.get("scale_word"):
                stats["with_unit_as_written"] += 1
                alt = dict(raw, scale_word="")   # 倍数是从 unit 挪到数上的：抽取员原来给的 scale_word 是空串
                q, _ = old_vp(alt, *rest, url=url)
                if q and q["value"] == p.get("value") and q["scale_word"] == p.get("scale_word"):
                    raw = alt
                    stats["scale_word_restored_to_empty"] += 1
            res_o, res_n = old_vp(raw, *rest, url=url), P.verify_point(raw, *rest, url=url)
            o, n = summary(res_o), summary(res_n)
            stats["old_kept"] += o["kept"]
            stats["new_kept"] += n["kept"]
            if o["kept"] and not p.get("reading_from_extractor") and o["value"] == p.get("value"):
                stats["old_reproduces_stored_value"] += 1
            if o != n:
                diffs.append({"run": run_name, "id": p.get("id"), "value_as_written": p.get("value_as_written"),
                              "scale_word": raw.get("scale_word"), "unit": raw["unit"], "old": o, "new": n})
            if res_n[0] and lv.get(qid) and NEW.leak_point_hit(res_n[0], lv[qid]):
                leaks.append({"run": run_name, "id": p.get("id"), "value_as_written": p.get("value_as_written"),
                              "value": res_n[0]["value"], "reading": bool(res_n[0].get("reading"))})
    stats["verify_point_changed"], stats["split_multiplier_changed"] = len(diffs), len(split_diffs)
    stats["new_leak_point_hits"] = len(leaks)
    return dict(stats), diffs, split_diffs, leaks


# ---------- 3. 丢点一侧的部分重放 ----------
# 原因串里 repr 过的 scale_word：unknown scale word 'x' / scale conflict: '...' in value vs 'x' / scale word 'x' not supported
_SW_IN_REASON = re.compile(r"(?:unknown scale word |in value vs |^scale word )('(?:[^'\\]|\\.)*'|\"[^\"]*\")")
_QUOTED = re.compile(r"'(?:[^'\\]|\\.)*'|\"[^\"]*\"")


def dropped_partial(old_ev):
    """原因以 number: 开头、或者是 scale word not supported 的丢点：新旧代码在「数字 + 倍数」这一步的结果，按原因类别计数。
    number:：parse_value(vw, sw)；not supported：scale_supported(sw, "", "", vw)，也就是只看 vw 自带的倍数（没有 quote）。
    不跑 quote / 日期 / 单位 / 截断检查（cjk_fragment）那几步，也不跑读数路径，只能说明这一步还挡不挡；完整效果要实跑。"""
    c, examples = Counter(), {}
    for f in sorted(ROOT.glob("results/**/state.json")):
        st = json.loads(f.read_text(encoding="utf-8"))
        for r in st.get("results") or []:
            for d in r.get("dropped_points") or []:
                why = d.get("reason") or ""
                if not (why.startswith("number:") or (why.startswith("scale word ") and why.endswith("table header"))):
                    continue
                m = _SW_IN_REASON.search(why)
                sw, vw = (ast.literal_eval(m.group(1)) if m else ""), d.get("value_as_written") or ""
                kind = _QUOTED.sub("'.'", why)[:70]
                if len(vw) >= 40:
                    tag = "vw truncated at 40 chars, not replayed"
                elif why.startswith("number:"):
                    o, n = run(old_ev.parse_value, vw, sw), run(NEW.parse_value, vw, sw)
                    tag = (f"old {'passes' if o[0] == 'ok' else 'drops'} -> new "
                           + ("passes" if n[0] == "ok" else "drops: " + n[1][:60]))
                else:
                    o, n = old_ev.scale_supported(sw, "", "", vw), NEW.scale_supported(sw, "", "", vw)
                    tag = f"vw-only support: old {o or chr(39) * 2} -> new {n or chr(39) * 2}"
                c[(kind, tag)] += 1
                examples.setdefault((kind, tag), f"{vw!r} + {sw!r}")
    return [{"reason_kind": k, "outcome": t, "n": n, "example": examples.get((k, t), "")}
            for (k, t), n in sorted(c.items(), key=lambda x: -x[1])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="v2.10i", help="旧代码的 git ref（默认 v2.10i = 改之前的 HEAD）")
    ap.add_argument("--readings", action="store_true", help="只打印必读写法表")
    ap.add_argument("--json", help="全部结果写成 json（只允许写到 probes/out/ 下）")
    a = ap.parse_args()
    old_ev, old_vp = load_old(a.ref)
    out = {"ref": a.ref, "readings": readings(old_ev, old_vp)}
    for r in out["readings"]:
        print(f"{'*' if r['changed'] else ' '} {r['case']}\n    old: {r['old']}\n    new: {r['new']}")
    if not a.readings:
        out["stats"], out["diffs"], out["split_diffs"], out["leak_hits"] = replay(old_ev, old_vp)
        out["dropped_partial"] = dropped_partial(old_ev)
        print("\nkept-point replay:", json.dumps(out["stats"]))
        for d in out["diffs"]:
            print(json.dumps(d, ensure_ascii=False))
        print("\nsplit_multiplier changes on kept points (unit_review multiplier, written_number for the value checker):")
        for d in out["split_diffs"]:
            print(json.dumps(d, ensure_ascii=False))
        print("\nkept points the new leak_point_hit would flag (backtest questions with registered values):")
        for d in out["leak_hits"]:
            print(json.dumps(d, ensure_ascii=False))
        print("\ndropped side (partial, number/scale step only):")
        for r in out["dropped_partial"]:
            print(f"  {r['n']:5d}  {r['reason_kind']}\n         {r['outcome']}   e.g. {r['example']}")
    if a.json:
        dest = Path(a.json).resolve()
        if (ROOT / "probes" / "out") not in dest.parents:
            sys.exit("--json must be under probes/out/")
        dest.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

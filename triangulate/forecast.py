"""提前一个月预测：用现有的两个 arm（prompt 不改、不联网），站在官方公布前一个月的日期上估一个数，再对照官方公布值。

数据：Yellowstone 国家公园月度 recreation visits（NPS 新闻稿，美国政府公开信息）。模型 deepseek-flash（V4.1 Flash）
2026-09-10 上线，下面两个月的官方数字都在这之后才公布，不可能在训练数据里。本轮没有检索，「截止日之后不许搜」自然成立。
另给一个代码基线「去年同月」（NPS 公布的 2025 年同月值），它在 as_of 之前就已公开。
"""
from concurrent.futures import ThreadPoolExecutor

from .arms import check_naive, run_naive, run_structured
from .config import GRAPHS, RESULTS
from .engine import evaluate_structured
from .llm import LLM, TransportError
from .report import _clean, _load, _write, errors_for, final_reply
from .viewer import render_page

FC = RESULTS / "forecast"
NPS = "https://www.nps.gov/yell/learn/news/{}.htm"
Q = ("Assume today is {as_of}. You know nothing published after this date. Estimate the number of recreation visits "
     "to Yellowstone National Park in {month}, as it will be reported in the National Park Service's official "
     "monthly visitation statistics.")
QUESTIONS = [
    {"id": "fc_yell_2026_08", "month": "August 2026", "as_of": "2026-08-15", "released": "2026-09-15",
     "answer_value": 856467, "last_year": 881936, "source": NPS.format(26022)},
    {"id": "fc_yell_2026_09", "month": "September 2026", "as_of": "2026-09-06", "released": "2026-10-06",
     "answer_value": 868450, "last_year": 839579, "source": NPS.format(26024)},
]
# 泄漏哨兵还要认「同一序列里、公布日晚于 as_of」的其他官方值（agent 回测用；不进任何 prompt）。
# 26022（2026-09-15）：2026 年 8 月 856,467，截至 8 月的年累计 3,491,850；
# 26024（2026-10-06）：2026 年 9 月 868,450，截至 9 月的年累计 4,360,300。两题的 as_of 都早于这两个公布日。
_POST_AS_OF = [856467, 3491850, 868450, 4360300]
for _q in QUESTIONS:
    _q.update(question=Q.format(**_q), answer_unit="", unit_hint="a count of recreation visits", strict=False,
              leak_values=sorted(set(_POST_AS_OF) | {_q["answer_value"]}))

# v2.1 新增的两道题：不是黄石、不是同一类来源，用来测通用性。选题标准同上：官方数字、公布日晚于模型上线日（2026-09-10），
# as_of = 公布日前一个月；last_year = 去年同月官方值（as_of 前已公开）；leak_values = 真值 + 公布日晚于 as_of 的已知官方值。
_ASOF = "Assume today is {as_of}. You know nothing published after this date. "
QUESTIONS += [
    # JNTO 2026-09-16 估计值（-9.6% 同比）；2025 年 8 月 3,428,406；7 月 3,442,100（2026-08-19 公布）和
    # 1-8 月累计 27,626,300 都晚于 as_of。官方 PDF 文字是字体编码、读不出，数值由两篇独立报道交叉核对。
    {"id": "fc_jnto_2026_08", "as_of": "2026-08-16", "released": "2026-09-16", "answer_value": 3098900,
     "last_year": 3428406, "source": "https://www.jnto.go.jp/en/news/20260916.pdf",
     "question": _ASOF.format(as_of="2026-08-16") + "Estimate the number of foreign visitor arrivals to Japan in August 2026, "
                 "as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.",
     "unit_hint": "a count of visitor arrivals", "leak_values": [3098900, 3442100, 27626300]},
    # 韩国国家数据处（原统计厅）2026-09-23「2026年7月人口动向」：7 月出生 24,275（+11.1%）；2025 年 7 月 21,854；
    # 1-7 月累计 170,079 晚于 as_of。6 月数据约 8 月下旬公布、数值未登记（哨兵认不出，记在报告的残余风险里）。
    {"id": "fc_kr_births_2026_07", "as_of": "2026-08-23", "released": "2026-09-23", "answer_value": 24275,
     "last_year": 21854,
     "source": "https://www.koreatimes.co.kr/southkorea/society/20260923/births-up-11-in-july-extending-gains-to-25th-consecutive-month",
     "question": _ASOF.format(as_of="2026-08-23") + "Estimate the number of live births in South Korea in July 2026, "
                 "as it will be first reported in the national statistics agency's monthly Population Trends release.",
     "unit_hint": "a count of live births", "leak_values": [24275, 170079]},
]
# 留出测试集（2026-10-15 选定，在 agent 的任何修改都定型之后才第一次跑；见 EVAL_TEST_PLAN.md）。
# 选题标准同上；last_year 里标「倒推」的是按官方同比变化率从真值倒算的。
QUESTIONS += [
    # 台湾内政部户籍统计（约 2026-10-08 公布）：9 月出生 7,704（同比 -10.45%），2025 年 9 月 8,603；
    # 1-9 月累计 69,446、8 月 7,492（约 9 月 9-10 日公布）都晚于 as_of。
    {"id": "fc_tw_births_2026_09", "set": "test", "as_of": "2026-09-08", "released": "2026-10-08", "answer_value": 7704,
     "last_year": 8603, "source": "https://www.taipeitimes.com/News/taiwan/archives/2026/10/08/2003865628",
     "question": _ASOF.format(as_of="2026-09-08") + "Estimate the number of births registered in Taiwan in September 2026, "
                 "as reported in the Ministry of the Interior's monthly household registration statistics.",
     "unit_hint": "a count of births", "leak_values": [7704, 69446, 7492]},
    # 希思罗机场 2026-10-12 公布：9 月 7.18 百万（同比 -2.3%，公布值只有 3 位有效数字）；2025 年 9 月按同比倒推约 7.35 百万；
    # 1-9 月累计 62.9 百万晚于 as_of。
    {"id": "fc_lhr_pax_2026_09", "set": "test", "as_of": "2026-09-12", "released": "2026-10-12", "answer_value": 7180000,
     "last_year": 7350000, "source": "https://www.sharecast.com/news/other-company-news/heathrow-airport-travel-tourism-london-passenger-traffic-uk--23819142.html",
     "question": _ASOF.format(as_of="2026-09-12") + "Estimate the number of passengers at London Heathrow Airport in September 2026, "
                 "as reported in Heathrow's monthly traffic statistics.",
     "unit_hint": "a count of passengers", "leak_values": [7180000, 62900000]},
    # 厚生劳动省人口动态统计速报（2026-09-25 公布）：7 月出生 62,479（同比 -1.5%，-936）；2025 年 7 月倒推 63,415。
    # 速报含在日外国人和在外日本人，比日本人「概数」大。官方 PDF 解析不了，数值由两处汇总交叉核对。
    {"id": "fc_jp_births_2026_07", "set": "test", "as_of": "2026-08-25", "released": "2026-09-25", "answer_value": 62479,
     "last_year": 63415, "source": "https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/07.html",
     "question": _ASOF.format(as_of="2026-08-25") + "Estimate the number of births in Japan in July 2026, as first reported in the "
                 "Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign "
                 "nationals in Japan).",
     "unit_hint": "a count of births", "leak_values": [62479]},
]
for _q in QUESTIONS[2:]:
    _q.update(answer_unit="", strict=False)
FNS = {"naive": run_naive, "structured": run_structured}


def _raw(arm, qid):
    return FC / "raw" / arm / f"{qid}.json"


def run(force: bool = False):
    tasks = [(arm, q) for q in QUESTIONS for arm in FNS if force or not _raw(arm, q["id"]).exists()]
    if not tasks:
        return
    llm = LLM(calls_path=FC / "calls.jsonl")

    def one(t):
        arm, q = t
        try:
            rec = FNS[arm](llm, q)
        except TransportError as e:
            print(f"[skip] {arm} {q['id']}: {e}", flush=True)
            return
        _write(_raw(arm, q["id"]), rec)
        print(f"{arm:10s} {q['id']} attempts={len(rec['attempts'])} problems={len(rec['attempts'][-1]['problems'])}", flush=True)
    with ThreadPoolExecutor(len(tasks)) as ex:
        list(ex.map(one, tasks))


def _pct(est, ans):
    return None if est is None else est / ans - 1


def report():
    rows = []
    for q in QUESTIONS:
        ans = q["answer_value"]
        row = {k: q.get(k) for k in ("id", "month", "as_of", "released", "answer_value", "source")}
        row["last_year_same_month"] = {"estimate": q["last_year"], "pct_err": _pct(q["last_year"], ans)}
        if (n := _load(_raw("naive", q["id"]))) is not None:
            status, est, _ = check_naive(final_reply(n), "", strict_target=False)
            row["naive"] = {"status": status, "estimate": est, "pct_err": _pct(est, ans),
                            "log10_err": errors_for(est, ans)[0], "attempts": len(n["attempts"])}
        if (s := _load(_raw("structured", q["id"]))) is not None:
            state = _clean(evaluate_structured(final_reply(s), "", q["id"], strict_target=False, question=q["question"]))
            r = state["result"]
            est = r["central"]
            row["structured"] = {"estimate": est, "pct_err": _pct(est, ans), "log10_err": errors_for(est, ans)[0],
                                 "p10": r["p10"], "p90": r["p90"],
                                 "covered_80": est is not None and r["p10"] <= ans <= r["p90"],
                                 "n_valid_paths": r["n_valid_paths"], "attempts": len(s["attempts"]),
                                 "paths": {p["id"]: [p.get("method"), p.get("median")] for p in state["paths"]},
                                 "remaining_errors": state["errors"]}
            _write(FC / "states" / f"{q['id']}.json", state)
            extra = (f"As of {q['as_of']} (official figure released {q['released']}). Official value: <b>{ans:,}</b>. "
                     f"No retrieval: every input comes from model knowledge.")
            (GRAPHS / f"{q['id']}.html").write_text(
                render_page(state, f"Forecast: {q['question'].split('Estimate ', 1)[-1][:90]}", extra, back_link="index.html"),
                encoding="utf-8")
        rows.append(row)
    _write(FC / "summary.json", _clean(rows))
    return rows

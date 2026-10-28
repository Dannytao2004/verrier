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
# 展示集（2026-10-16 选定，在任何模型调用之前提交；见 EVAL_SHOWCASE_PLAN.md）。两道已公布题（回测，选题标准同上，
# 领域不和前 7 题重复）+ 两道未公布题（真实使用，"set": "live"，没有真值，公布后另行登记再打分）。
# last_year 只作数据留在这里，不进任何对比和展示。
QUESTIONS += [
    # NHS England 月度 A&E 统计：2026 年 9 月全部类型就诊 2.44 百万（NHS England 新闻稿，公布值只有 3 位有效数字；BMA、
    # Pharmacy Business、Open Access Government 同值）。公布日：同批的 Aug26 RTT 统计文件 2026-10-08 已被 Wayback 抓到、
    # BMA 10-08 更新时已引用 9 月数；GOV.UK 页面记 2026-10-09 09:30。取较早的 10-08，as_of = 2026-09-08。
    # 2025 年 9 月 2,309,154（NHS England 2025 年 9 月统计评述）。晚于 as_of 公布：8 月约 2.34 百万（2026-09-10 公布，
    # 精确值没读出，只登记约数）、6-8 月合计 7,268,445。
    {"id": "fc_nhs_ae_2026_09", "set": "showcase", "as_of": "2026-09-08", "released": "2026-10-08", "answer_value": 2440000,
     "last_year": 2309154,
     "source": "https://www.gov.uk/government/statistics/ae-attendances-and-emergency-admissions-for-september-2026-and-quarterly-report-q2",
     "question": _ASOF.format(as_of="2026-09-08") + "Estimate the total number of A&E attendances in England in September 2026 "
                 "(all A&E types, including minor injury units and walk-in centres), as reported in NHS England's monthly "
                 "A&E Attendances and Emergency Admissions statistics.",
     "unit_hint": "a count of A&E attendances", "leak_values": [2440000, 2340000, 7268445]},
    # 总务省统计局住民基本台帳人口移动报告 2026 年 8 月结果（令和 8 年 9 月 29 日公表）：市区町村间移动者（日本人 + 外国人）
    # 356,920（+2.4%）；2025 年 8 月 348,602（同表）。同一公布里的分项（都道府县间 164,955、都道府县内 191,965、
    # 日本人 307,665、外国人 49,255）都晚于 as_of。7 月结果 2026-08-27 公布，早于 as_of。
    {"id": "fc_jp_movers_2026_08", "set": "showcase", "as_of": "2026-08-29", "released": "2026-09-29", "answer_value": 356920,
     "last_year": 348602, "source": "https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html",
     "question": _ASOF.format(as_of="2026-08-29") + "Estimate the number of people who moved between municipalities within Japan "
                 "in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of "
                 "Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.",
     "unit_hint": "a count of people who moved", "leak_values": [356920, 164955, 191965, 307665, 49255]},
    # 未公布：JNTO 发表预定表（20260916.pdf）写 2026 年 9 月推计值 10 月 21 日（周三）16:15 公布。2025 年 9 月推计值 3,266,800。
    {"id": "fc_jnto_2026_09", "set": "live", "as_of": "2026-10-16", "expected_release": "2026-10-21",
     "last_year": 3266800, "source": "https://www.jnto.go.jp/statistics/data/20260916.pdf",
     "question": _ASOF.format(as_of="2026-10-16") + "Estimate the number of foreign visitor arrivals to Japan in September 2026, "
                 "as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.",
     "unit_hint": "a count of visitor arrivals"},
    # 未公布：国家数据处 10 月月间报道计划写「2026년 8월 인구동향」10.28（周三）12:00 公布。2025 年 8 月出生 20,867（初值）。
    {"id": "fc_kr_births_2026_08", "set": "live", "as_of": "2026-10-16", "expected_release": "2026-10-28",
     "last_year": 20867, "source": "https://mods.go.kr/newsPln.es?mid=a10305000000",
     "question": _ASOF.format(as_of="2026-10-16") + "Estimate the number of live births in South Korea in August 2026, "
                 "as it will be first reported in the national statistics agency's monthly Population Trends release.",
     "unit_hint": "a count of live births"},
]
for _q in QUESTIONS[2:]:
    _q.update(answer_unit="", strict=False)
# 留出测试 2（2026-10-18 选定，代码冻结在 frozen-v2.8r = 258a53d，在任何模型调用之前提交；见 EVAL_TEST2_PLAN.md）。
# 选题标准同上（公布日 2026-09-11..10-17、as_of = 公布日前约 30 天、领域不和前 11 题重复），数值和公布日都由一个找题、
# 一个复查的 agent 打开官方发布页核过。answer_unit 按题给（基线臂的量纲检查用；计数题留空，等于无量纲计数）。
# leak_values = 真值 + 同一序列里公布日晚于 as_of 的已知官方值。
QUESTIONS += [
    # 洛杉矶港 2026-10-09 新闻稿：9 月 1,042,652 TEU（统计表 1,042,652.30，同比 +18.07%，历史纪录）；2025 年 9 月 883,053.25
    # （historical-teu-statistics-2025）。晚于 as_of：同表的进出口分项、1-9 月累计 8,081,625.55。8 月新闻稿（09-09）没有存档。
    {"id": "fc_pola_teu_2026_09", "set": "test2", "as_of": "2026-09-10", "released": "2026-10-09", "answer_value": 1042652,
     "last_year": 883053, "source": "https://portoflosangeles.org/references/2026-news-releases/news_100926_sept_cargo",
     "question": _ASOF.format(as_of="2026-09-10") + "Estimate the total container volume handled by the Port of Los Angeles in "
                 "September 2026, in TEUs (twenty-foot equivalent units; loaded and empty imports and exports combined), as it "
                 "will be first reported in the Port of Los Angeles's monthly cargo news release.",
     "answer_unit": "", "unit_hint": "a count of TEUs",
     "leak_values": [1042652, 1042652.3, 8081625.55, 545695.6, 125750.75, 371205.95]},
    # 西班牙 INE 2026-10-09「Estadística de Transporte de Personas」TV0826：8 月公共交通乘客 371,623.271 千人次（+3.3%）；
    # 2025 年 8 月首发 362,445.48 千（TV0825，本期已修订为约 359,817 千，推算）。晚于 as_of：urbano / interurbano / especial /
    # metro / autobús urbano 分项。TV0426-TV0726 没有存档，存档里最新的 2026 年月份是 3 月。
    {"id": "fc_es_transit_2026_08", "set": "test2", "as_of": "2026-09-11", "released": "2026-10-09", "answer_value": 371623271,
     "last_year": 362445480, "source": "https://www.ine.es/dyngs/Prensa/TV0826.htm",
     "question": _ASOF.format(as_of="2026-09-11") + "Estimate the total number of passengers who used public transport in Spain "
                 "in August 2026 (urban, interurban and special/discretionary transport combined), as it will be first reported "
                 "in the provisional data of the National Statistics Institute's (INE) Passenger Transport Statistics "
                 "(Estadística de Transporte de Personas).",
     "answer_unit": "", "unit_hint": "a count of passengers",
     "leak_values": [371623271, 371623.271, 231892575, 119355913, 20374783, 88341988, 143550587]},
    # Statistics Canada 2026-09-28 The Daily「Railway carloadings, July 2026」：31,686,803 吨（31.7 Mt，+2.6%；表 23-10-0216-01，
    # v74869）。2025 年 7 月现表值 30,880,543（首发「30.7 million tonnes」）。晚于 as_of：non-intermodal 24.8 Mt、intermodal
    # 3.2 Mt、US connections 3.8 Mt，以及同日修订的 1-6 月。6 月的 Daily 没有存档。
    {"id": "fc_ca_rail_2026_07", "set": "test2", "as_of": "2026-08-29", "released": "2026-09-28", "answer_value": 31686803,
     "last_year": 30880543, "source": "https://www150.statcan.gc.ca/n1/daily-quotidien/260928/dq260928a-eng.htm",
     "question": _ASOF.format(as_of="2026-08-29") + "Estimate the total freight carried by Canadian railways in July 2026, in "
                 "tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total "
                 "traffic carried, Canada).",
     "answer_unit": "tonne", "unit_hint": "a mass of freight in tonnes",
     "leak_values": [31686803, 24800000, 3200000, 3800000]},
    # KBA 2026-10-05 pm41：9 月新注册乘用车 256.774（+9,0%）；2025 年 9 月 235.528（pm39_2025）。晚于 as_of：1-9 月 2.221.798、
    # BEV 88.599、全部 Kfz 306.292。8 月稿（09-03）首次存档是 09-08，回测里能读到的最新月份是 7 月。
    {"id": "fc_de_cars_2026_09", "set": "test2", "as_of": "2026-09-05", "released": "2026-10-05", "answer_value": 256774,
     "last_year": 235528,
     "source": "https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm41_2026_n_09_26_pm_komplett.html",
     "question": _ASOF.format(as_of="2026-09-05") + "Estimate the number of new passenger cars (Pkw) registered in Germany in "
                 "September 2026, as it will be first reported in the Kraftfahrt-Bundesamt's (KBA) monthly press release on "
                 "vehicle registrations.",
     "answer_unit": "", "unit_hint": "a count of passenger cars",
     "leak_values": [256774, 2221798, 88599, 306292]},
    # 香港旅游发展局 2026-10-15 新闻稿：9 月访港旅客临时数 4,031,090（+22%）；2025 年 9 月 3,292,197。晚于 as_of：8 月临时数
    # 5,456,320（2026-09-15 公布）、1-8 月约 36,672,650、9 月内地 3,170,122 / 非内地 860,968、1-9 月 40,703,740 / 内地 31,901,686。
    {"id": "fc_hk_visitors_2026_09", "set": "test2", "as_of": "2026-09-14", "released": "2026-10-15", "answer_value": 4031090,
     "last_year": 3292197,
     "source": "https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/press-release/hktb/2026/10-Sep-Visitor-Arrivals-E.pdf",
     "question": _ASOF.format(as_of="2026-09-14") + "Estimate the total number of visitor arrivals to Hong Kong in September 2026, "
                 "as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals "
                 "press release.",
     "answer_unit": "", "unit_hint": "a count of visitor arrivals",
     "leak_values": [4031090, 5456320, 36672650, 3170122, 860968, 40703740, 31901686]},
    # 美国 Census / HUD 2026-09-17「Monthly New Residential Construction, August 2026」：私人住宅开工季调年率 1,275,000；
    # 2025 年 8 月 1,291,000。晚于 as_of：7 月报告（08-18）的首发值约 1,239,000、7 月修订 1,309,000、8 月 permits 1,394,000、
    # completions 1,128,000、NSA 110,500；1,415,000 是找题 agent 列的同表值，出处未核实。回测必须截断在 08-17。
    {"id": "fc_us_starts_2026_08", "set": "test2", "as_of": "2026-08-17", "released": "2026-09-17", "answer_value": 1275000,
     "last_year": 1291000, "source": "https://www.census.gov/construction/nrc/pdf/newresconst.pdf",
     "question": _ASOF.format(as_of="2026-08-17") + "Estimate the seasonally adjusted annual rate of privately-owned housing starts "
                 "in the United States in August 2026 (the number of housing units at an annual rate, as in '1,300,000'), as it "
                 "will be first reported in the U.S. Census Bureau and HUD Monthly New Residential Construction release.",
     "answer_unit": "", "unit_hint": "a count of housing units (seasonally adjusted annual rate)",
     "leak_values": [1275000, 1239000, 1309000, 1394000, 1128000, 110500, 1415000]},
    # 美国 EIA 2026-09-24 Electric Power Monthly Table 1.1：7 月公用事业规模净发电量 453,744 千 MWh（= GWh）；2025 年 7 月
    # 446,320。晚于 as_of：6 月 399,671（08-26 公布）、1-7 月 2,629,899、滚动 12 个月 4,480,718、小规模光伏 10,925。
    {"id": "fc_us_gen_2026_07", "set": "test2", "as_of": "2026-08-25", "released": "2026-09-24", "answer_value": 453744,
     "last_year": 446320, "source": "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_01",
     "question": _ASOF.format(as_of="2026-08-25") + "Estimate total U.S. net electricity generation at utility-scale facilities "
                 "(all sectors, all energy sources, excluding small-scale solar) in July 2026, in gigawatt-hours (GWh, equal to "
                 "thousand megawatthours), as it will be first reported in the U.S. Energy Information Administration's Electric "
                 "Power Monthly (Table 1.1).",
     "answer_unit": "GWh", "unit_hint": "an amount of electricity in GWh",
     "leak_values": [453744, 399671, 2629899, 4480718, 10925]},
    # 韩国国家数据处（原统计厅）2026-10-01「2026년 8월 온라인쇼핑동향」：거래액 24조 2,118억원（+7.3%）、모바일 18조 9,021억원；
    # 2025 年 8 月首发 22조 4,802억원（2025-10-01）。7 月稿在 as_of 当天（09-01）发布；发布方网站上 2026 年 1-7 月的稿都没有存档。
    {"id": "fc_kr_online_2026_08", "set": "test2", "as_of": "2026-09-01", "released": "2026-10-01", "answer_value": 24211800000000,
     "last_year": 22480200000000, "source": "https://mods.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=447300",
     "question": _ASOF.format(as_of="2026-09-01") + "Estimate the total value of online shopping transactions in South Korea in "
                 "August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly "
                 "Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).",
     "answer_unit": "KRW", "unit_hint": "an amount of money in KRW",
     "leak_values": [24211800000000, 18902100000000]},
]
# 留出测试 2 的未公布题（2026-10-19 加入，在任何模型调用之前提交；见 EVAL_TEST2_PLAN.md「补充」一节）。真实使用：as_of = 跑的那天，
# 没有真值，公布后另行登记再打分。四道月度官方统计 + 两道上市公司财报里的 AI 指标（用户 10-19：token 和算力建设各一，
# 过往财报披露过、下次财报可核实）。公布日都来自官方发布日历或公司公告；计分用基本单位（磅、新台币、美元、人、token/分钟）。
_LIVE = "2026-10-19"
QUESTIONS += [
    # USDA NASS「Milk Production」：日历 Thu 10/22/26 3:00 pm ET。2025 年 9 月 24 州首发 18,279 百万磅（2025-11-10，停摆延迟；
    # 现修订为 18,230）；最新 2026 年 8 月 19,172 百万磅（+1.8%）。
    {"id": "fc_us_milk_2026_09", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-22",
     "last_year": 18279000000, "source": "https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?view=l&month=10&year=2026",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate total milk production in the 24 major States of the United States in "
                 "September 2026, in pounds (the report states it in million pounds), as it will be first reported in the USDA "
                 "National Agricultural Statistics Service's monthly Milk Production report.",
     "answer_unit": "lb", "unit_hint": "a mass of milk in pounds"},
    # 台湾经济部统计处「批發、零售及餐飲業營業額統計」：9 月份资料订于 115 年 10 月 23 日下午 4:00 公布（8 月稿原文）。
    # 2025 年 9 月餐饮业营业额 835 億元（年减 0.9%）；最新 2026 年 8 月 950 億元（+1.8%）。
    {"id": "fc_tw_restaurants_2026_09", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-23",
     "last_year": 83500000000, "source": "https://www.moea.gov.tw/Mns/dos/bulletin/Bulletin.aspx?kind=8&html=1&menu_id=6727&bull_id=16913",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate the turnover of Taiwan's food and beverage services industry (餐飲業營業額, "
                 "current prices) in September 2026, in New Taiwan dollars (TWD), as it will be first reported in the Ministry of "
                 "Economic Affairs Department of Statistics' monthly release on wholesale, retail and food services turnover "
                 "(批發、零售及餐飲業營業額統計).",
     "answer_unit": "TWD", "unit_hint": "an amount of money in TWD"},
    # INEGI「Balanza Comercial de Mercancías de México, información oportuna」：2026 日历 27/octubre（06:00 墨西哥城）。
    # 2025 年 9 月出口及时数 56,487.9 百万美元；最新 2026 年 8 月 78,010.5 百万美元（+40.4%）。计分用 10-27 的及时数。
    {"id": "fc_mx_exports_2026_09", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-27",
     "last_year": 56487900000, "source": "https://www.inegi.org.mx/contenidos/saladeprensa/doc/cal_2026.pdf",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate Mexico's total merchandise exports in September 2026, in US dollars "
                 "(original figures, not seasonally adjusted), as they will be first reported in INEGI's timely trade balance "
                 "bulletin (Balanza Comercial de Mercancías de México, información oportuna).",
     "answer_unit": "USD", "unit_hint": "an amount of money in USD"},
    # 联邦劳动局（BA）Veröffentlichungskalender：Oktober 2026，Stichtag 13.10.2026，Veröffentlichung Freitag 30.10.2026 10:00。
    # 2025 年 10 月登记失业 2.911.000（原值）；最新 2026 年 9 月 2.994.000。计分用新闻稿里取整到千的全国原值。
    {"id": "fc_de_unemployed_2026_10", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-30",
     "last_year": 2911000,
     "source": "https://statistik.arbeitsagentur.de/DE/Navigation/Service/Veroeffentlichungskalender/Veroeffentlichungskalender-Nav.html",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate the number of registered unemployed persons in Germany in October 2026 "
                 "(not seasonally adjusted, all of Germany), as it will be first reported in the Federal Employment Agency's "
                 "(Bundesagentur für Arbeit) monthly labour market press release.",
     "answer_unit": "", "unit_hint": "a count of registered unemployed persons"},
    # Alphabet：10-06 公告 Q3 2026 电话会 10-28（earnings release 在电话会前发）。过往：Q3'25 7B、Q4'25 over 10B、Q1'26 more than
    # 16B、Q2'26 22B tokens per minute（earnings release 正文）。计分取 earnings release 里的数（没有就用 CEO 电话会讲稿），
    # 忽略 over / more than / approximately；两份材料都没给这个数，本题作废（报告里写明）。
    {"id": "fc_googl_tokens_2026_q3", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-28",
     "last_year": 7000000000,
     "source": "https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/default.aspx",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate the number of tokens per minute that Alphabet's first-party models (such as "
                 "Gemini) process via direct API use by customers, as it will be first stated with Alphabet's third-quarter 2026 "
                 "results (earnings press release or CEO earnings-call remarks); in Q2 2026 Alphabet stated this as 'Gemini models "
                 "now process 22 billion API tokens per minute'. Answer in tokens per minute.",
     "answer_unit": "token/minute", "unit_hint": "a rate in tokens per minute"},
    # Meta：10-12 公告 Q3 2026 结果 10-21 盘后发布。每份新闻稿都有「Capital expenditures, including principal payments on finance
    # leases, were $X billion」：Q3'25 $19.37B、Q4'25 $22.14B、Q1'26 $19.84B、Q2'26 $31.08B；2026 全年指引 $130-145B（Q2 稿）。
    {"id": "fc_meta_capex_2026_q3", "set": "test2_live", "as_of": _LIVE, "expected_release": "2026-10-21",
     "last_year": 19370000000,
     "source": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx",
     "question": _ASOF.format(as_of=_LIVE) + "Estimate Meta Platforms' capital expenditures, including principal payments on finance "
                 "leases, for the third quarter of 2026 (quarter ended September 30, 2026), in US dollars, as it will be first "
                 "reported in Meta's third-quarter 2026 earnings press release.",
     "answer_unit": "USD", "unit_hint": "an amount of money in USD"},
]
# 留出测试 3（2026-10-23 加入，三臂 x 思考开 / 关的对比，在任何模型调用之前登记；只由 probes/run_test3.py 跑和打分，
# 下面的 run / report 跳过它）。选题和复查：复查表的 final_four
# （公布日 2026-03-01..10-22、晚于 DeepSeek 知识截止 2026-02；as_of = 公布日前 28-30 天；数值、公布日、首发都由复查 agent
# 重新打开官方页核过）。leak_values 照复查后的版本（英国破产去掉了三位数的分项）。
QUESTIONS += [
    # 国家统计局 2026-05-18「2026年4月份社会消费品零售总额」：4 月 37247亿元（+0.2%）；2025 年 4 月首发 37174亿元。
    # leak_values：真值（元和亿元两种写法）、同页的 1-4 月累计和分项、5-9 月各稿的当月值和累计（都晚于 as_of）。
    {"id": "fc_cn_retail_2026_04", "set": "test3", "as_of": "2026-04-18", "released": "2026-05-18", "answer_value": 3724700000000,
     "last_year": 3717400000000, "source": "https://www.stats.gov.cn/sj/zxfb/202605/t20260518_1963727.html",
     "question": _ASOF.format(as_of="2026-04-18") + "Estimate China's total retail sales of consumer goods (社会消费品零售总额) for "
                 "the single month of April 2026 (not the January-April cumulative total), in Chinese yuan (CNY; the release "
                 "states it in 亿元, i.e. units of 100 million yuan), as it will be first reported in the National Bureau of "
                 "Statistics of China's monthly release on retail sales of consumer goods.",
     "answer_unit": "CNY", "unit_hint": "an amount of money in CNY",
     "leak_values": [3724700000000, 37247, 164941, 34218, 152053, 32347, 142921, 22020, 32987, 146058, 18883, 14147, 63052,
                     65308, 41185, 24123, 41090, 206031, 42691, 248722, 39022, 287744, 39824, 327569, 42433, 370001]},
    # Census 2026-07-16 adv2606：6 月零售和餐饮季调额 768,553 百万美元（正文「$768.6 billion」）；2025 年 6 月首发 720,106。
    # leak_values：真值、正文的取整值、同表 6 月未季调值，7-9 月稿和 10-15 年度修订后的值。
    {"id": "fc_us_retail_2026_06", "set": "test3", "as_of": "2026-06-18", "released": "2026-07-16", "answer_value": 768553000000,
     "last_year": 720106000000, "source": "https://www2.census.gov/retail/releases/historical/marts/adv2606.pdf",
     "question": _ASOF.format(as_of="2026-06-18") + "Estimate total U.S. retail and food services sales for June 2026 (seasonally "
                 "adjusted and adjusted for holiday and trading-day differences, but not for price changes; a monthly amount, "
                 "not an annual rate), in US dollars (the release states it in millions of dollars), as it will be first "
                 "reported (advance estimate) in the U.S. Census Bureau's Advance Monthly Sales for Retail and Food Services "
                 "release.",
     "answer_unit": "USD", "unit_hint": "an amount of money in USD",
     "leak_values": [768553000000, 768600000000, 768553, 776915, 766876, 768072, 766192, 763602, 768587, 764462, 773947,
                     745021, 739322, 729915]},
    # Insolvency Service 2026-09-18：8 月登记公司破产 1,946；2025 年 8 月首发 2,048（本期稿写 2,007）。
    # leak_values：真值、7 月修订值、8 月 CVL、9 月稿的 9 月值和 8 月修订值、9 月 CVL（三位数的分项复查时去掉了：182 撞上 as_of 前的 6 月稿）。
    {"id": "fc_uk_insolv_2026_08", "set": "test3", "as_of": "2026-08-19", "released": "2026-09-18", "answer_value": 1946,
     "last_year": 2048,
     "source": "https://www.gov.uk/government/statistics/company-insolvencies-august-2026/commentary-company-insolvency-statistics-august-2026",
     "question": _ASOF.format(as_of="2026-08-19") + "Estimate the number of registered company insolvencies in England and Wales in "
                 "August 2026 (the headline monthly total of compulsory liquidations, creditors' voluntary liquidations, "
                 "administrations, company voluntary arrangements and receivership appointments, in which the first three are "
                 "seasonally adjusted), as it will be first reported in the Insolvency Service's monthly Company Insolvency "
                 "Statistics release.",
     "answer_unit": "", "unit_hint": "a count of company insolvencies",
     "leak_values": [1946, 1934, 1431, 1882, 1953, 1420]},
    # Stats NZ 2026-04-20「Overseas merchandise trade: March 2026」：3 月货物出口 7,943,894,499 新西兰元（页面 G1 图表数据；
    # 正文「$7.9 billion」）；2025 年 3 月首发 7,594,592,976。leak_values：真值、同页 3 月进口、4-9 月各稿的出口。
    {"id": "fc_nz_exports_2026_03", "set": "test3", "as_of": "2026-03-21", "released": "2026-04-20", "answer_value": 7943894499,
     "last_year": 7594592976, "source": "https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-march-2026/",
     "question": _ASOF.format(as_of="2026-03-21") + "Estimate the total value of New Zealand's goods exports in March 2026 (actual "
                 "monthly value, not seasonally adjusted), in New Zealand dollars (NZD), as it will be first reported in Stats "
                 "NZ's monthly Overseas merchandise trade release.",
     "answer_unit": "NZD", "unit_hint": "an amount of money in NZD",
     "leak_values": [7943894499, 7245909283, 8620109942, 8876680404, 8092970496, 7391317405, 6655897873, 6466753919]},
]
# 留出测试 4（前瞻，2026-10-23 登记，在任何模型调用之前；只由 probes/run_test4.py 跑和打分，下面的 run / report 跳过它）。
# 选题和复查：test4 候选题表（TEST4_QUESTIONS_ZH.md 的第 1、2 题；
# 日历页和两个数值页复查者 10-23 重新打开核过）。真实使用：没有真值；as_of = 实际跑的那天，由 run_test4 在每个配置开跑时用
# with_as_of() 填进 question_template，所以这里 as_of、question 都是 None（不经 run_test4 直接拿去跑会报错，不会带着旧日期跑）。
# released_at = 首发时刻（带时区）：到了这个时刻答案可能已公开，run_test4 拒跑（跑不完的也拒）。leak_values 先空着
# （真实使用没有登记值）。公布后把首发值填进下面的 TEST4_OFFICIAL，再 probes/run_test4.py --score。
_ASOF_T = "Assume today is {as_of}. You know nothing published after this date. "
QUESTIONS += [
    # 国家统计局发布日程表「工业经济效益月度报告」10 月一栏 27/二 9:30（北京）= 美国中部时间 2026-10-26 20:30 CDT。
    # 去年同期 2025 年 1-9 月 53732.0亿元（t20251027_1961695）；最近一期 2026 年 1-8 月 52719.8亿元（t20260928_1965425，可比口径
    # +15.7%）。各年公布的累计水平不可比（附注二：每年调查范围重置），去年值只是弱基准。
    {"id": "fc_cn_profits_2026_09", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-27T09:30:00+08:00", "last_year": 5373200000000,
     "last_year_source": "https://www.stats.gov.cn/sj/zxfbhjd/202510/t20251027_1961695.html",
     "source": "https://www.stats.gov.cn/sj/fbrc/bnxxfb/",
     "question_template": _ASOF_T + "Estimate the total profits of China's industrial enterprises above designated size "
                          "(规模以上工业企业利润总额) for January-September 2026 (the cumulative total, not the single month of "
                          "September), in Chinese yuan (CNY; the release states it in 亿元, i.e. units of 100 million yuan), as it "
                          "will be first reported in the National Bureau of Statistics of China's monthly release on profits of "
                          "industrial enterprises.",
     "answer_unit": "CNY", "unit_hint": "an amount of money in CNY", "leak_values": []},
    # 国家统计发布行事历：交通部「來臺旅客及國人出國人數」10 月 27 日 16:20（台北）= 美国中部时间 2026-10-27 03:20 CDT（条目注记：
    # 115年9月资料由 11月10日前改为 10月27日）。去年同期 2025 年 9 月 601,339、最近一期 2026 年 8 月 662,735，都取自主计总处
    # 重要指标页的镜像（交通部首发页没打开，镜像是不是首发值未核实）；同一 JSON 里的出国人数别混用。
    {"id": "fc_tw_visitors_2026_09", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-27T16:20:00+08:00", "last_year": 601339,
     "last_year_source": "https://www.stat.gov.tw/Point.aspx?sid=t.12&n=3591&sms=11480",
     "source": "https://www.stat.gov.tw/News_NoticeCalendar.aspx?n=3717&sms=11505&IsControl=0&Dept=all&_Hide=1",
     "question_template": _ASOF_T + "Estimate the number of visitor arrivals to Taiwan (來臺旅客人次) in September 2026, as it "
                          "will be first reported in the Ministry of Transportation and Communications' (Tourism Administration) "
                          "monthly statistics on visitor arrivals and outbound departures (來臺旅客及國人出國人數).",
     "answer_unit": "", "unit_hint": "a count of visitor arrivals", "leak_values": []},
]
# 第 3-7 题（2026-10-27 登记，在这几题的任何模型调用之前）：test4_candidates.json 里 selection = final、按首发时刻排在第 3-7 的题
# （用户 10-27：先跑最近会公布的 5 个）。日历、去年同期、最近一期都是 10-23 复查者打开核过的；题干 = 候选题的 question 去掉开头
# 那句 as_of。10-27 又让核验 agent 重开了一次日历页（结果见 NEXT.md）。
QUESTIONS += [
    # Equinor 3Q26 quarterly update PDF：「The 3Q results will be reported 28 October 2026 at 07:00 CEST」（10-28 挪威已是 CET，
    # 按当地 07:00 = 06:00 UTC）。去年同期 3Q25 表 2,130 mboe/d；最近一期 2Q26 2,165。报告写 mboe/d（千），计分单位 boe/d。
    {"id": "fc_eqnr_prod_2026_q3", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-28T07:00:00+01:00", "last_year": 2130000,
     "last_year_source": "https://cdn.sanity.io/files/h61q9gi9/global/1076ae946124491794687a843c115299662e71e0.pdf",
     "source": "https://cdn.sanity.io/files/h61q9gi9/global/ca519bd03b29c8b67260a968087d54ec89aee0f8.pdf",
     "question_template": _ASOF_T + "Estimate Equinor's total equity liquids and gas production in the third quarter of 2026, "
                          "in barrels of oil equivalent per day (the report states it in thousand boe per day, mboe/d), as it "
                          "will be first reported in Equinor's third quarter 2026 financial statements and review.",
     "answer_unit": "boe/d", "unit_hint": "a rate of production in barrels of oil equivalent per day", "leak_values": []},
    # SMMT Key Press Dates（制造）：September 2026 Thursday 29 October，00:01 embargo（英国已是 GMT = UTC）。去年同期 2025 年 9 月
    # 51,090（JLR 网络攻击停产压低）；最近一期 2026 年 8 月 39,328。只算轿车，不含商用车。
    {"id": "fc_uk_carprod_2026_09", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-29T00:01:00+00:00", "last_year": 51090,
     "last_year_source": "https://www.smmt.co.uk/cyber-attack-hits-vehicle-output-with-new-risk-arising-from-tax-charge-on-auto-workers/",
     "source": "https://www.smmt.co.uk/key-press-dates/",
     "question_template": _ASOF_T + "Estimate the number of cars manufactured in the United Kingdom in September 2026 (total car "
                          "production for home and export markets, excluding commercial vehicles), as it will be first reported "
                          "in the Society of Motor Manufacturers and Traders' (SMMT) monthly UK car manufacturing release.",
     "answer_unit": "", "unit_hint": "a count of cars produced", "leak_values": []},
    # 英格兰银行「Money and Credit - September 2026 (to be published at 9.30am)」，29 October 2026（GMT）。去年同期 2025 年 9 月
    # 65,900；最近一期 2026 年 8 月 54,900。季调；正文取整到百位。
    {"id": "fc_uk_mortgages_2026_09", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-29T09:30:00+00:00", "last_year": 65900,
     "last_year_source": "https://www.bankofengland.co.uk/statistics/money-and-credit/2025/september-2025",
     "source": "https://www.bankofengland.co.uk/statistics/money-and-credit/2026/september-2026",
     "question_template": _ASOF_T + "Estimate the number of net mortgage approvals for house purchase in the United Kingdom in "
                          "September 2026 (seasonally adjusted), as it will be first reported in the Bank of England's monthly "
                          "Money and Credit statistical release.",
     "answer_unit": "", "unit_hint": "a count of mortgage approvals", "leak_values": []},
    # 比亚迪 HKEX 公告 2026-10-14：董事会 2026-10-29（周四）审议未经审计的第三季度业绩。发布时刻没公布（2025 年是董事会当天
    # 19:32 HKT 上网），这里取当天 00:00 HKT（保守，宁早不晚）。去年同期 3Q25 单季营业收入 194,984,598,000 元。
    {"id": "fc_byd_rev_2026_q3", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-29T00:00:00+08:00", "last_year": 194984598000,
     "last_year_source": "https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1030/2025103001667.pdf",
     "source": "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1014/2026101400381.pdf",
     "question_template": _ASOF_T + "Estimate BYD Company Limited's operating revenue for the three months July-September 2026 "
                          "(the third quarter alone, not January-September), in Chinese yuan (CNY), as it will be first reported "
                          "in BYD's unaudited third quarterly report (key accounting data table, 'The Reporting Period' column).",
     "answer_unit": "CNY", "unit_hint": "an amount of money in CNY", "leak_values": []},
    # GOV.UK 公告「Release date: 30 October 2026 9:30am (provisional)」，HMRC 评述「The next release will be published 09:30am
    # 30 October 2026」（GMT）。去年同期 2025 年 9 月季调临时数 95,980；最近一期 2026 年 8 月 95,220。季调，别和非季调混。
    {"id": "fc_uk_homesales_2026_09", "set": "test4", "as_of": None, "question": None,
     "released_at": "2026-10-30T09:30:00+00:00", "last_year": 95980,
     "last_year_source": "http://web.archive.org/web/20251031155447/https://www.gov.uk/government/statistics/monthly-property-"
                         "transactions-completed-in-the-uk-with-value-40000-or-above/uk-monthly-property-transactions-commentary--2",
     "source": "https://www.gov.uk/government/statistics/announcements/monthly-property-transactions-completed-in-the-uk-with-"
               "the-value-of-40000-or-above--31",
     "question_template": _ASOF_T + "Estimate the number of UK residential property transactions (with a value of £40,000 or "
                          "above) in September 2026, seasonally adjusted, as it will be first reported (provisional estimate) "
                          "in HM Revenue & Customs' monthly release 'Monthly property transactions completed in the UK with value "
                          "of £40,000 or above'.",
     "answer_unit": "", "unit_hint": "a count of residential property transactions", "leak_values": []},
]
# 留出测试 4 的官方首发值：公布后填，填之前 run_test4 --score 只列估计、不算误差。填法（数用计分单位：元、人次）：
#   "fc_cn_profits_2026_09": {"value": 5.9e12, "source": "<首发页 URL>", "quote": "<原文那一句>", "checked": "2026-10-27"},
# Q1、Q2 的首发值 10-27 核过三遍：定时任务（probes/out/test4_official_Q1.md、Q2.md）+ 每题两个独立核验 agent，数都一致。
# Q2 的出处用观光署企划组「115年9月觀光市場概況摘要」（发布日期 115-10-27，附月表 1-2 总计 611755）；交通部统计库
# （statis.motc.gov.tw Seq=309、statchart api_proxy Seq=1185）同值。
TEST4_OFFICIAL = {
    "fc_cn_profits_2026_09": {"value": 6033740000000, "source": "https://www.stats.gov.cn/sj/zxfb/202610/t20261027_1965697.html",
                              "quote": "1—9月份，全国规模以上工业企业实现利润总额60337.4亿元，同比增长15.5%（按可比口径计算，详见附注二）。",
                              "checked": "2026-10-27"},
    "fc_tw_visitors_2026_09": {"value": 611755, "source": "https://admin.taiwan.net.tw/BusinessInfo/News?a=119&id=36492",
                               "quote": "115年9月來臺旅客為611,755人次，與去（114）年同期相較，成長1.73%。", "checked": "2026-10-27"},
    "fc_eqnr_prod_2026_q3": None,
    "fc_uk_carprod_2026_09": None,
    "fc_uk_mortgages_2026_09": None,
    "fc_byd_rev_2026_q3": None,
    "fc_uk_homesales_2026_09": None,
}


# 留出测试 4 的打分说明（run_test4 --score 写进 summary.md 的「打分说明」一节，并在对应配置的说明栏标出）：题 -> 适用的臂、说明原文
TEST4_SCORING_NOTES = {
    "fc_eqnr_prod_2026_q3": {
        "arms": ["agent"],
        "note": "agent 两个配置的输出单位是 mboe/d（千桶油当量/日，Equinor 报告的写法），终稿 2,195 / 2,149 mboe/d。跑的时候（v2.13b）"
                "单位库不认识 mboe，打分换不到计分单位 boe/d，记过「unit not convertible」（BUGS S75）。v2.13c 起单位库按 SPE 惯例读 "
                "mboe = 1000 boe，同一份输出按 x1000 换算打分。用户 2026-10-27 定：算。这是打分环节的修正：agent 没有重跑，输出没改。"},
}


def with_as_of(q: dict, as_of: str) -> dict:
    """留出测试 4：题目在跑的那天才定 as_of（真实使用）。返回填好 as_of 和 question 的副本（不改题库里的这一条）。"""
    if not q.get("question_template"):
        raise ValueError(f"{q['id']} has no question_template")
    return {**q, "as_of": as_of, "question": q["question_template"].format(as_of=as_of)}


for _q in QUESTIONS:
    if _q.get("set") in ("test2", "test2_live", "test3", "test4"):
        _q["strict"] = False
FNS = {"naive": run_naive, "structured": run_structured}
OWN_RUNNER = ("test3", "test4")   # 这些题集由自己的脚本跑和打分（probes/run_test3.py、run_test4.py），run / report 不碰


def _raw(arm, qid):
    return FC / "raw" / arm / f"{qid}.json"


def run(force: bool = False):
    tasks = [(arm, q) for q in QUESTIONS for arm in FNS
             if q.get("set") not in OWN_RUNNER and (force or not _raw(arm, q["id"]).exists())]
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


def run_search(force: bool = False):
    """arm (3) 联网直接答：只跑未公布题（set = live），每题一次；已有保存的回复就跳过。传输失败不保存，记一行到屏幕。"""
    import json
    import threading
    from .search_direct import ARM, DirectClient, run_search_direct
    qs = [q for q in QUESTIONS if q.get("set") == "live" and (force or not _raw(ARM, q["id"]).exists())]
    if not qs:
        return
    lock = threading.Lock()

    def log(rec):
        with lock, (FC / "calls.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    client = DirectClient(log)

    def one(q):
        try:
            rec = run_search_direct(client, q)
        except TransportError as e:
            print(f"[skip] {ARM} {q['id']}: {e}", flush=True)
            return
        _write(_raw(ARM, q["id"]), rec)
        print(f"{ARM} {q['id']} attempts={len(rec['attempts'])} status={rec['status']} estimate={rec['estimate']}", flush=True)
    with ThreadPoolExecutor(len(qs)) as ex:
        list(ex.map(one, qs))


def _pct(est, ans):
    return None if est is None else est / ans - 1


def report():
    rows = []
    for q in QUESTIONS:
        if q.get("answer_value") is None or q.get("set") in OWN_RUNNER:   # 未公布题（set = live）：公布后登记真值再打分
            continue
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

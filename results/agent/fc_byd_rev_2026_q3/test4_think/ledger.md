# Evidence ledger: fc_byd_rev_2026_q3

- Question: Assume today is 2026-10-27. You know nothing published after this date. Estimate BYD Company Limited's operating revenue for the three months July-September 2026 (the third quarter alone, not January-September), in Chinese yuan (CNY), as it will be first reported in BYD's unaudited third quarterly report (key accounting data table, 'The Reporting Period' column).
- as_of: 2026-10-27
- Pinned target: Consolidated operating revenue (营业收入/营业总收入) of BYD Company Limited and its subsidiaries for the three months 2026-07-01 to 2026-09-30, as first reported in the 'The Reporting Period' column of BYD's unaudited third quarterly report key accounting data table, in Chinese yuan. This is Q3 alone, not Ja | unit Chinese yuan (CNY) | period 2026-07-01..2026-09-30 | publisher BYD Company Limited (HKEX: 1211; SZSE: 002594), unaudited third quarterly report

## Directions and pages

### d1 [own_history] Company reporting / historical quarterly financials

Hypothesis: BYD's own quarterly revenue history provides the base for Q3 2026: Q3 revenue should track Q3 2025 revenue and adjacent 2026 quarters, updated by Q3 2026 unit-volume growth and segment mix. Symbolically, revenue_Q3_2026 is a seasonally and mix-adjusted growth on revenue_Q3_2025 or revenue_Q2_2026.

Queries issued by the searcher: 比亚迪 2025年第三季度报告 营业收入 本报告期; BYD 2026 first quarter report operating revenue; 比亚迪 2025年年度报告 营业收入 2025年全年 8040亿; 比亚迪 2026年半年度报告 营业收入 汽车 比亚迪电子 二季度; 比亚迪 2025年第三季度报告 营业收入 本报告期; BYD third quarter 2025 results revenue 194.9 billion; 比亚迪 2026年第一季度报告 营业收入; 比亚迪 2026年半年度报告 营业收入 汽车; 比亚迪 2025年第三季度报告 营业收入 本报告期; BYD 2026 first quarter report revenue operating revenue; 比亚迪 2026年半年度报告 营业收入 汽车 上半年 2026; 比亚迪 2025年年度报告 营业收入 第四季度 2025 全年营收

- `https://data.eastmoney.com/notices/detail/002594/AN202510301772001473.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.cnstock.com/commonDetail/575702` -> **live_dated** (page date 2025-10-30); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/002594/AN202604281821686560.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://stcn.com/article/detail/3458599.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/831204810293/index.phtml` -> **live_dated** (page date 2026-05-04); points raw/verified 15/15
  - p1 BYD consolidated operating revenue, Q1 2026 = **150,225,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Rounded duplicate of Q1 2026 revenue; exact p46 kept.] quote: "分别实现营收、归母净利润、扣非归母净利润1502.25 亿、40.85 亿、41.48 亿"
  - p2 BYD Q1 2026 revenue year-on-year change = **11.82** % (2026-01-01..2026-03-31) [keep: ] quote: "分别同比下降11.82%、同比下降55.38%、同比下降49.24%"
  - p3 BYD Electronics Q1 2026 sales revenue = **38,183,000,000** CNY (2026-01-01..2026-03-31) [keep: ] quote: "一季度比亚迪电子销售收入、盈利分别为381.83 亿、0.28 亿"
  - p4 BYD automotive business revenue excluding BYD Electronics, Q1 2026 = **112,042,000,000** CNY (2026-01-01..2026-03-31) [keep: ] quote: "剔除比亚迪电子收入及盈利之后,公司汽车业务收入、盈利分别为1120.42 亿、40.67 亿元,同比-16.06%、-53.5%"
  - p5 BYD automotive business revenue year-on-year change, Q1 2026 = **16.06** % (2026-01-01..2026-03-31) [keep: ] quote: "公司汽车业务收入、盈利分别为1120.42 亿、40.67 亿元,同比-16.06%、-53.5%"
  - p6 BYD revenue per vehicle, Q1 2026 = **160,000** CNY/vehicle (2026-01-01..2026-03-31) [keep: ] quote: "单车营收16 万元,同比+19.93%,环比+18.29%"
  - p7 BYD revenue per vehicle year-on-year change, Q1 2026 = **19.93** % (2026-01-01..2026-03-31) [keep: ] quote: "单车营收16 万元,同比+19.93%,环比+18.29%"
  - p8 BYD revenue per vehicle quarter-on-quarter change, Q1 2026 = **18.29** % (2026-01-01..2026-03-31) [keep: ] quote: "单车营收16 万元,同比+19.93%,环比+18.29%"
  - p9 BYD new energy vehicle sales volume, Q1 2026 = **700,500** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "2026 年一季度,公司新能源汽车销量70.05 万辆,同比-30.01%"
  - p10 BYD new energy vehicle sales volume year-on-year change, Q1 2026 = **30.01** % (2026-01-01..2026-03-31) [keep: ] quote: "公司新能源汽车销量70.05 万辆,同比-30.01%"
  - p11 BYD premium brands (Denza, Fangchengbao, Yangwang) combined sales volume, Q1 202 = **84,100** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "其中腾势、方程豹、仰望品牌总销量8.41 万辆,同比+59.98%,占公司总销量12.01%"
  - p12 BYD premium brands share of total company sales volume, Q1 2026 = **12.01** % (2026-01-01..2026-03-31) [keep: ] quote: "其中腾势、方程豹、仰望品牌总销量8.41 万辆,同比+59.98%,占公司总销量12.01%"
  - p13 BYD passenger vehicle and pickup overseas sales volume, Q1 2026 = **320,700** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "2026Q1,公司乘用车和皮卡海外市场销量为32.07 万台,同比+55.61%"
  - p14 BYD export sales share of total sales volume, Q1 2026 = **45.78** % (2026-01-01..2026-03-31) [keep: ] quote: "出口销量占总销量的45.78%,去年同期为20.59%"
  - p15 BYD export sales share of total sales volume, Q1 2025 = **20.59** % (2025-01-01..2025-03-31) [keep: ] quote: "出口销量占总销量的45.78%,去年同期为20.59%"
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/831468016144/index.phtml` -> **live_dated** (page date 2026-05-07); points raw/verified 15/15
  - p16 BYD consolidated revenue, Q1 2026 (26Q1) = **150,200,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Rounded duplicate of Q1 2026 revenue; exact p46 kept.] quote: "26Q1 公司实现营收1,502 亿元,同比-12%,环比-37%"
  - p17 BYD revenue Q1 2026 year-on-year change = **-12** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司实现营收1,502 亿元,同比-12%,环比-37%"
  - p18 BYD revenue Q1 2026 quarter-on-quarter change = **-37** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司实现营收1,502 亿元,同比-12%,环比-37%"
  - p19 BYD revenue excluding BYD Electronic, Q1 2026 = **112,000,000,000** CNY (2026-01-01..2026-03-31) [keep: ] quote: "1) 营收1,120 亿元,同比-16%,环比-38%,主要受季节性销量下滑影响"
  - p20 BYD revenue excluding BYD Electronic Q1 2026 year-on-year change = **-16** % (2026-01-01..2026-03-31) [keep: ] quote: "1) 营收1,120 亿元,同比-16%,环比-38%,主要受季节性销量下滑影响"
  - p21 BYD revenue excluding BYD Electronic Q1 2026 quarter-on-quarter change = **-38** % (2026-01-01..2026-03-31) [keep: ] quote: "1) 营收1,120 亿元,同比-16%,环比-38%,主要受季节性销量下滑影响"
  - p22 BYD ASP excluding BYD Electronic, Q1 2026 = **160,000** CNY/vehicle (2026-01-01..2026-03-31) [keep: ] quote: "ASP 16.0 万元,同比+2.7 万元,环比+2.5 万元"
  - p23 BYD total vehicle sales, Q1 2026 = **700,000** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司销量70 万辆,同比-30%,环比-48%"
  - p24 BYD total vehicle sales Q1 2026 year-on-year change = **-30** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司销量70 万辆,同比-30%,环比-48%"
  - p25 BYD total vehicle sales Q1 2026 quarter-on-quarter change = **-48** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司销量70 万辆,同比-30%,环比-48%"
  - p26 BYD overseas vehicle sales, Q1 2026 = **320,000** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司实现海外销量32 万辆,同比+56%,环比-8%"
  - p27 BYD overseas vehicle sales Q1 2026 year-on-year change = **56** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司实现海外销量32 万辆,同比+56%,环比-8%"
  - p28 BYD overseas vehicle sales Q1 2026 quarter-on-quarter change = **-8** % (2026-01-01..2026-03-31) [keep: ] quote: "26Q1 公司实现海外销量32 万辆,同比+56%,环比-8%"
  - p29 BYD full-year overseas sales target 2026 (plan) = **1,500,000** vehicle (2026-01-01..2026-12-31) [keep: ] quote: "全年出海销量目标150 万辆,同比+50%"
  - p30 BYD full-year overseas sales target 2026 year-on-year growth (plan) = **50** % (2026-01-01..2026-12-31) [keep: ] quote: "全年出海销量目标150 万辆,同比+50%"
- `https://www.cnfin.com/gs-lb/detail/20260428/4406131_1.html` -> **live_dated** (page date 2026-04-28); points raw/verified 15/15
  - p31 BYD consolidated operating revenue, Q1 2026 (three months ended 2026-03-31) = **150,225,000,000** CNY (2026-01-01..2026-03-31) [keep: ] quote: "比亚迪公布2026年一季度财报,报告期内,比亚迪实现营业收入1502.25亿元,同比下降11.82%"
  - p32 BYD consolidated operating revenue, Q1 2026, year-on-year change = **11.82** % (2026-01-01..2026-03-31) [keep: ] quote: "报告期内,比亚迪实现营业收入1502.25亿元,同比下降11.82%"
  - p33 BYD net profit attributable to shareholders, Q1 2026 = **4,085,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Net profit, not revenue.] quote: "归属于上市公司股东的净利润为40.85亿元,同比大幅下降55.38%"
  - p34 BYD net profit attributable to shareholders, Q1 2026, year-on-year change = **55.38** % (2026-01-01..2026-03-31) [DISCARD: Net profit change, not revenue.] quote: "归属于上市公司股东的净利润为40.85亿元,同比大幅下降55.38%"
  - p35 BYD non-recurring-adjusted net profit, Q1 2026 = **4,148,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Non-recurring-adjusted net profit, not revenue.] quote: "扣非净利润41.48亿元,同比下降49.24%"
  - p36 BYD basic earnings per share, Q1 2026 = **0.45** CNY/share (2026-01-01..2026-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益由上年同期的1.04元降至0.45元"
  - p37 BYD basic earnings per share, Q1 2025 (prior-year comparative) = **1.04** CNY/share (2025-01-01..2025-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益由上年同期的1.04元降至0.45元"
  - p38 BYD weighted average return on equity, Q1 2026 = **1.65** % (2026-01-01..2026-03-31) [DISCARD: ROE, not revenue.] quote: "加权平均净资产收益率由4.37%收窄至1.65%"
  - p39 BYD weighted average return on equity, Q1 2025 (prior-year comparative) = **4.37** % (2025-01-01..2025-03-31) [DISCARD: ROE, not revenue.] quote: "加权平均净资产收益率由4.37%收窄至1.65%"
  - p40 BYD R&D expense, Q1 2026 = **11,344,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: R&D expense, not revenue.] quote: "本季度比亚迪研发费用为113.44亿元,上年同期为142.23亿元,同比下降约20.2%"
  - p41 BYD R&D expense, Q1 2025 (prior-year comparative) = **14,223,000,000** CNY (2025-01-01..2025-03-31) [DISCARD: R&D expense, not revenue.] quote: "本季度比亚迪研发费用为113.44亿元,上年同期为142.23亿元,同比下降约20.2%"
  - p42 BYD net cash flow from operating activities, Q1 2026 = **2,790,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Operating cash flow, not revenue.] quote: "经营活动产生的现金流量净额仅为27.90亿元,同比大幅下降67.48%"
  - p43 BYD net cash flow from investing activities, Q1 2026 = **-20,250,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Investing cash flow, not revenue.] quote: "投资活动产生的现金流量净额为-202.5亿元,同比下降38.15%"
  - p44 BYD net cash flow from financing activities, Q1 2026 = **23,061,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Financing cash flow, not revenue.] quote: "筹资活动产生的现金流量净额230.61亿元,同比下降39.31%"
  - p45 BYD total common shareholders at end of Q1 2026 = **718,700** household (2026-03-31..2026-03-31) [DISCARD: Shareholder count, not revenue.] quote: "截至一季度末,比亚迪普通股股东总数为71.87万户"
- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=002594&id=12252088` -> **live_dated** (page date 2026-03-31); points raw/verified 15/15
  - p46 BYD consolidated operating revenue, Q1 2026 (current reporting period) = **150,225,314,000** CNY (2026-01-01..2026-03-31) [keep: ] quote: "营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p47 BYD consolidated operating revenue, Q1 2025 (prior-year comparative) = **170,360,448,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p48 BYD total operating revenue (营业总收入), Q1 2026, income statement = **150,225,314,000** CNY (2026-01-01..2026-03-31) [DISCARD: Duplicate Q1 2026 revenue in income statement; exact p46 kept.] quote: "一、营业总收入 150,225,314,000.00 170,360,448,000.00其中:营业收入 150,225,314,000.00"
  - p49 BYD total operating revenue (营业总收入), Q1 2025, income statement = **170,360,448,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "一、营业总收入 150,225,314,000.00 170,360,448,000.00其中:营业收入 150,225,314,000.00"
  - p50 BYD operating revenue year-on-year change, Q1 2026 vs Q1 2025 = **-11.82** % (2026-01-01..2026-03-31) [keep: ] quote: "营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p51 BYD operating cost, Q1 2026 = **121,973,620,000** CNY (2026-01-01..2026-03-31) [DISCARD: Operating cost, not revenue.] quote: "其中:营业成本121,973,620,000.00 136,175,385,000.00"
  - p52 BYD operating cost, Q1 2025 = **136,175,385,000** CNY (2025-01-01..2025-03-31) [DISCARD: Operating cost, not revenue.] quote: "其中:营业成本121,973,620,000.00 136,175,385,000.00"
  - p53 BYD net profit attributable to shareholders, Q1 2026 = **4,084,551,000** CNY (2026-01-01..2026-03-31) [DISCARD: Net profit, not revenue.] quote: "归属于上市公司股东的净利润(元) 4,084,551,000.00 9,154,985,000.00 -55.38%"
  - p54 BYD net profit attributable to shareholders, Q1 2025 = **9,154,985,000** CNY (2025-01-01..2025-03-31) [DISCARD: Net profit, not revenue.] quote: "归属于上市公司股东的净利润(元) 4,084,551,000.00 9,154,985,000.00 -55.38%"
  - p55 BYD basic earnings per share, Q1 2026 = **0.448** CNY/share (2026-01-01..2026-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益(元/股) 0.4480 1.0391 -56.89%"
  - p56 BYD basic earnings per share, Q1 2025 = **1.039** CNY/share (2025-01-01..2025-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益(元/股) 0.4480 1.0391 -56.89%"
  - p57 BYD shares outstanding after July 2025 stock dividend and capitalisation = **9,117,197,565** share (2025-07-01..2025-07-31) [DISCARD: Share count, not revenue.] quote: "派发后的发行在外普通股股数为9,117,197,565股"
  - p58 BYD stock dividend distributed July 2025 = **2,431,252,684** share (2025-07-01..2025-07-31) [DISCARD: Share dividend, not revenue.] quote: "于2025年7月,本公司派发股票股利2,431,252,684股,资本公积转增股本3,646,879,026股"
  - p59 BYD capital reserve capitalisation shares, July 2025 = **3,646,879,026** share (2025-07-01..2025-07-31) [DISCARD: Share capitalisation, not revenue.] quote: "派发股票股利2,431,252,684股,资本公积转增股本3,646,879,026股,派发后的发行在外普通股股数为9,117,197,565股"
  - p60 BYD total assets, end of Q1 2026 = **902,076,965,000** CNY (2026-03-31..2026-03-31) [DISCARD: Total assets, not revenue.] quote: "总资产(元) 902,076,965,000.00 883,729,883,000.00 2.08%"
- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=002594&id=12252088` -> **live_dated** (page date 2026-03-31); points raw/verified 15/15
  - p61 BYD consolidated operating revenue, Q1 2026 (current reporting period) = **150,225,314,000** CNY (2026-01-01..2026-03-31) [DISCARD: Duplicate Q1 2026 revenue; exact p46 kept.] quote: "营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p62 BYD consolidated operating revenue, Q1 2025 (prior-year comparative) = **170,360,448,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p63 BYD total operating revenue (营业总收入), Q1 2026, from consolidated income statement = **150,225,314,000** CNY (2026-01-01..2026-03-31) [DISCARD: Duplicate Q1 2026 revenue; exact p46 kept.] quote: "一、营业总收入 150,225,314,000.00 170,360,448,000.00其中:营业收入 150,225,314,000.00"
  - p64 BYD total operating revenue (营业总收入), Q1 2025, from consolidated income statement = **170,360,448,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "一、营业总收入 150,225,314,000.00 170,360,448,000.00其中:营业收入 150,225,314,000.00"
  - p65 BYD operating revenue year-on-year change, Q1 2026 vs Q1 2025 = **-11.82** % (2026-01-01..2026-03-31) [keep: ] quote: "本报告期比上年同期增 减(%)营业收入(元) 150,225,314,000.00 170,360,448,000.00 -11.82%"
  - p66 BYD operating cost (营业成本), Q1 2026 = **121,973,620,000** CNY (2026-01-01..2026-03-31) [DISCARD: Operating cost, not revenue.] quote: "其中:营业成本121,973,620,000.00 136,175,385,000.00"
  - p67 BYD operating cost (营业成本), Q1 2025 = **136,175,385,000** CNY (2025-01-01..2025-03-31) [DISCARD: Operating cost, not revenue.] quote: "其中:营业成本121,973,620,000.00 136,175,385,000.00"
  - p68 BYD net profit attributable to shareholders, Q1 2026 = **4,084,551,000** CNY (2026-01-01..2026-03-31) [DISCARD: Net profit, not revenue.] quote: "归属于上市公司股东的净利润(元) 4,084,551,000.00 9,154,985,000.00 -55.38%"
  - p69 BYD net profit attributable to shareholders, Q1 2025 = **9,154,985,000** CNY (2025-01-01..2025-03-31) [DISCARD: Net profit, not revenue.] quote: "归属于上市公司股东的净利润(元) 4,084,551,000.00 9,154,985,000.00 -55.38%"
  - p70 BYD net cash from operating activities, Q1 2026 = **2,790,305,000** CNY (2026-01-01..2026-03-31) [DISCARD: Operating cash flow, not revenue.] quote: "经营活动产生的现金流量净额(元) 2,790,305,000.00 8,580,961,000.00 -67.48%"
  - p71 BYD net cash from operating activities, Q1 2025 = **8,580,961,000** CNY (2025-01-01..2025-03-31) [DISCARD: Operating cash flow, not revenue.] quote: "经营活动产生的现金流量净额(元) 2,790,305,000.00 8,580,961,000.00 -67.48%"
  - p72 BYD basic earnings per share, Q1 2026 = **0.448** CNY/share (2026-01-01..2026-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益(元/股) 0.4480 1.0391 -56.89%"
  - p73 BYD basic earnings per share, Q1 2025 = **1.039** CNY/share (2025-01-01..2025-03-31) [DISCARD: EPS, not revenue.] quote: "基本每股收益(元/股) 0.4480 1.0391 -56.89%"
  - p74 BYD shares outstanding after July 2025 stock dividend and capitalisation = **9,117,197,565** share (2025-07-01..2025-07-31) [DISCARD: Share count, not revenue.] quote: "派发后的发行在外普通股股数为9,117,197,565股"
  - p75 BYD total assets at 2026-03-31 = **902,076,965,000** CNY (2026-03-31..2026-03-31) [DISCARD: Total assets, not revenue.] quote: "总资产(元) 902,076,965,000.00 883,729,883,000.00 2.08%"
- `https://krungthai.com/Download/generalcontent/MediaFile_236918BYDCOM2026FIRSTQUARTERLYREPORT.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://finance.people.com.cn/BIG5/n1/2026/0330/c1004-40691720.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.cnstock.com/commonDetail/658561` -> **live_dated** (page date 2026-03-27); points raw/verified 0/0

### d2 [physical_flow] Monthly production and sales announcements

Hypothesis: BYD's monthly production/sales announcements for July, August and September 2026 give the vehicle unit volume, the largest driver of automotive revenue. Multiplying Q3 volume by segment and export ASPs, then adding electronics and other revenue, gives the consolidated revenue estimate.

Queries issued by the searcher: 比亚迪 2026年9月 产销快报 新能源汽车 销量; BYD September 2026 sales production announcement; 比亚迪 2026年8月产销快报 新能源汽车 销量 出口; 比亚迪 2026年7月产销快报 新能源汽车 销量 出口; 比亚迪 2026年7月产销快报 销量 出口 新能源汽车; 比亚迪 2026年9月 产销快报 新能源汽车 销量; BYD September 2026 sales production announcement; 比亚迪 2026年7月产销快报 新能源汽车 销量 出口; 比亚迪 2026年8月产销快报 销量 出口 新能源汽车; 比亚迪 2026年9月 产销快报 新能源汽车 销量; BYD September 2026 sales production announcement; 比亚迪 2026年8月产销快报 新能源汽车 销量 出口; 比亚迪 2026年7月产销快报 销量 出口 新能源汽车

- `https://www.cnfin.com/announ/detail/index.html?id=844705253353&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/company/rptid/845640780089/index.phtml` -> **live_dated** (page date 2026-10-18); points raw/verified 15/14
  - p76 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月汽车销量463561 辆,同比增长17%,环比增长5.3%"
  - p77 BYD September 2026 NEV passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月新能源乘用车销量456713 辆,同比增长16.2%,环比增长5.4%"
  - p78 BYD September 2026 passenger BEV sales = **273,143** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中9 月纯电动乘用车销量273143 辆,同比增长33.2%"
  - p79 BYD September 2026 passenger PHEV sales = **183,570** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "插混乘用车销量183570 辆,同比下降2.4%"
  - p80 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月国内销量28.3 万辆,同比下降13%,环比增长12.8%"
  - p81 BYD September 2026 NEV exports = **181,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p82 BYD September 2026 export share of NEV sales = **39** % (2026-09-01..2026-09-30) [keep: ] quote: "销量占比39%,同比提升21pcts"
  - p83 BYD cumulative vehicle sales Jan-Sep 2026 = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计汽车销量3131576 辆,同比下降3.9%"
  - p84 BYD cumulative passenger vehicle sales Jan-Sep 2026 = **3,078,544** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计乘用车销量3078544 辆,同比下降4.4%"
  - p85 BYD cumulative domestic sales Jan-Sep 2026 = **1,789,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计国内销量178.9 万辆,同比下降30%"
  - p86 BYD September 2026 Dynasty and Ocean network sales = **395,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p87 BYD September 2026 Fangchengbao brand sales = **43,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "方程豹4.3 万辆(同比+79.0%)"
  - p88 BYD September 2026 Denza brand sales = **18,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "腾势1.8 万辆(同比+46.7%)"
  - p89 BYD September 2026 premium brands combined share of passenger vehicle sales = **13.5** % (2026-09-01..2026-09-30) [keep: ] quote: "占乘用车销量13.5%,同比提升4pcts"
- `https://data.eastmoney.com/notices/detail/01211/AN202610011830081567.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?CompanyCode=10002250&gather=1&id=12631418` -> **live_dated** (page date 2026-10-08); points raw/verified 15/10
  - p90 BYD September 2026 total NEV sales (monthly) = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
  - p91 BYD September 2026 passenger BEV sales (monthly) = **273,143** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| -纯电动 \| 274,403 \| 204,838 \| 1,636,015 \| 1,578,176 \| 3.66% \| 273,143 \| 205,050 \| 1,629,957 \| 1,605,903 \| 1.50% \|"
  - p92 BYD September 2026 passenger PHEV sales (monthly) = **183,570** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| -插电式混合动力 \| 183,713 \| 197,170 \| 1,451,767 \| 1,593,290 \| -8.88% \| 183,570 \| 188,010 \| 1,448,587 \| 1,612,959 \| -10.19% \|"
  - p93 BYD September 2026 commercial vehicle sales (monthly) = **6,848** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| -商用车 \| 5,748 \| 3,546 \| 51,164 \| 42,103 \| 21.52% \| 6,848 \| 3,210 \| 53,032 \| 41,284 \| 28.46% \|"
  - p94 BYD September 2026 NEV exports (monthly) = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "注:本公司2026年9月出口新能源汽车合计180,700辆。"
  - p95 BYD September 2026 total NEV production (monthly) = **463,864** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
  - p96 BYD cumulative Jan-Sep 2026 total NEV sales = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
  - p97 BYD cumulative Jan-Sep 2026 passenger BEV sales = **1,629,957** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "\| -纯电动 \| 274,403 \| 204,838 \| 1,636,015 \| 1,578,176 \| 3.66% \| 273,143 \| 205,050 \| 1,629,957 \| 1,605,903 \| 1.50% \|"
  - p98 BYD cumulative Jan-Sep 2026 passenger PHEV sales = **1,448,587** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "\| -插电式混合动力 \| 183,713 \| 197,170 \| 1,451,767 \| 1,593,290 \| -8.88% \| 183,570 \| 188,010 \| 1,448,587 \| 1,612,959 \| -10.19% \|"
  - p99 BYD cumulative Jan-Sep 2026 commercial vehicle sales = **53,032** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "\| -商用车 \| 5,748 \| 3,546 \| 51,164 \| 42,103 \| 21.52% \| 6,848 \| 3,210 \| 53,032 \| 41,284 \| 28.46% \|"
- `https://4g.stockstar.com/detail/AN2026100100003500` -> **live_dated** (page date 2026-10-27); points raw/verified 12/12
  - p100 BYD September 2026 NEV production (vehicles) = **463,864** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月,公司新能源汽车产量为463,864辆,同比下降2.32%"
  - p101 BYD September 2026 NEV sales (vehicles) = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为463,561辆,同比下降3.94%"
  - p102 BYD September 2026 NEV sales year-on-year change = **3.94** % (2026-09-01..2026-09-30) [keep: ] quote: "销量为463,561辆,同比下降3.94%"
  - p103 BYD September 2026 passenger vehicle production (vehicles) = **458,116** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量为458,116辆,累计同比下降2.64%"
  - p104 BYD September 2026 passenger vehicle sales (vehicles) = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为456,713辆,累计同比下降4.36%"
  - p105 BYD September 2026 passenger BEV production (vehicles) = **274,403** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "纯电动乘用车产量为274,403辆,累计同比增长3.66%"
  - p106 BYD September 2026 passenger BEV sales (vehicles) = **273,143** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为273,143辆,累计同比增长1.50%"
  - p107 BYD September 2026 passenger PHEV production (vehicles) = **183,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "插电式混合动力乘用车产量为183,713辆,累计同比下降8.88%"
  - p108 BYD September 2026 passenger PHEV sales (vehicles) = **183,570** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为183,570辆,累计同比下降10.19%"
  - p109 BYD September 2026 commercial vehicle production (vehicles) = **5,748** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "商用车方面,产量为5,748辆,累计同比增长21.52%"
  - p110 BYD September 2026 commercial vehicle sales (vehicles) = **6,848** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为6,848辆,累计同比增长28.46%"
  - p111 BYD September 2026 NEV exports (vehicles) = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月出口新能源汽车共计180,700辆"
- `https://simplywall.st/stocks/hk/automobiles/hkg-1211/byd-shares/news/does-september-sales-update-change-the-bull-case-for-byd-sto` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0
- `https://finance.eastmoney.com/a/202610013888248472.html` -> **live_dated** (page date 2026-10-01); points raw/verified 9/9
  - p112 BYD September 2026 NEV sales (total) = **463,600** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月,公司新能源汽车产量为46.39万辆,销量为46.36万辆。"
  - p113 BYD September 2026 NEV production (total) = **463,900** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月,公司新能源汽车产量为46.39万辆,销量为46.36万辆。"
  - p114 BYD September 2026 passenger vehicle production = **458,100** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量45.81万辆,销量45.67万辆;"
  - p115 BYD September 2026 passenger vehicle sales = **456,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量45.81万辆,销量45.67万辆;"
  - p116 BYD September 2026 commercial vehicle production = **5,748** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "商用车产量5748辆,销量6848辆。"
  - p117 BYD September 2026 commercial vehicle sales = **6,848** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "商用车产量5748辆,销量6848辆。"
  - p118 BYD September 2026 NEV exports = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "此外,公司9月出口新能源汽车合计18.07万辆。"
  - p119 BYD cumulative Jan-Sep 2026 NEV production = **3,138,900** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "本年累计新能源汽车产量313.89万辆,销量313.16万辆。"
  - p120 BYD cumulative Jan-Sep 2026 NEV sales = **3,131,600** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "本年累计新能源汽车产量313.89万辆,销量313.16万辆。"
- `https://data.eastmoney.com/notices/detail/02944/AN202610071830185793.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/002594/AN202610071830185793.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://wt.cfi.cn/p20261001000125.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://4g.stockstar.com/detail/JC2026101800001092` -> **live_dated** (page date 2026-10-27); points raw/verified 15/14
  - p121 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p122 BYD September 2026 total vehicle sales year-on-year growth = **17** % (2026-09-01..2026-09-30) [keep: ] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p123 BYD September 2026 total vehicle sales month-on-month growth = **5.3** % (2026-09-01..2026-09-30) [keep: ] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p124 BYD cumulative vehicle sales January-September 2026 = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计汽车销量3131576辆,同比下降3.9%"
  - p125 BYD September 2026 new energy passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车销量456713辆,同比增长16.2%,环比增长5.4%"
  - p126 BYD cumulative new energy passenger vehicle sales January-September 2026 = **3,078,544** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计乘用车销量3078544辆,同比下降4.4%"
  - p127 BYD September 2026 passenger BEV sales = **273,143** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中9月纯电动乘用车销量273143辆,同比增长33.2%"
  - p128 BYD September 2026 passenger BEV sales year-on-year growth = **33.2** % (2026-09-01..2026-09-30) [keep: ] quote: "其中9月纯电动乘用车销量273143辆,同比增长33.2%"
  - p129 BYD September 2026 passenger PHEV sales = **183,570** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "插混乘用车销量183570辆,同比下降2.4%"
  - p130 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月国内销量28.3万辆,同比下降13%,环比增长12.8%"
  - p131 BYD cumulative domestic sales January-September 2026 = **1,789,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计国内销量178.9万辆,同比下降30%"
  - p132 BYD September 2026 new energy vehicle exports = **181,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p133 BYD September 2026 export share of new energy vehicle sales = **39** % (2026-09-01..2026-09-30) [keep: ] quote: "销量占比39%,同比提升21pcts"
  - p134 BYD September 2026 premium brands (Denza/Fangchengbao/Yangwang) combined sales = **62,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "腾势/方程豹/仰望三个高端品牌合计6.2万辆(同比+65.7%),占乘用车销量13.5%"
- dropped by code checks: 7 (scale word '万' not supported by quote or table header: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 5)

### d3 [base_rates] Revenue per vehicle / model and export mix

Hypothesis: Automotive revenue equals sum over vehicle categories of volume times ASP. Historical quarterly automotive revenue divided by unit sales gives a transferable ASP, which must be adjusted for export mix, model mix and price changes. This direction constrains the largest conversion factor in d2.

Queries issued by the searcher: 比亚迪 2025年第三季度报告 营业收入 汽车业务 销量 单车均价; BYD Q3 2026 quarterly results revenue; 比亚迪 2026年半年报 汽车业务收入 销量 单车ASP 二季度; 比亚迪 2026年9月 销量 海外销量 出口 占比; 比亚迪 2026 二季度 汽车业务收入 销量 单车均价; BYD average selling price per vehicle 2026 export mix; 比亚迪 2026年9月 新能源汽车销量 快报 出口; 比亚迪 2026Q3 业绩预告 三季度 收入 销量 单车ASP 预测; 比亚迪 2026年第三季度报告 营业收入; 比亚迪 季度 汽车业务收入 销量 单车均价 2026; 比亚迪 2026年9月 销量 出口 数据 三季度 累计; BYD Q3 2026 sales volume September 2026 exports monthly

- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/841448580327/index.phtml` -> **live_dated** (page date 2026-08-30); points raw/verified 15/14
  - p135 BYD Q2 2026 total revenue = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2026 年Q2 实现收入1945.9 亿元,同环比分别-3.2%和+29.5%"
  - p136 BYD Q2 2026 automotive revenue excluding BYD Electronics = **150,540,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "扣除比亚迪电子后,汽车收入约1505.4 亿元,同环比-4.2%和+34.4%"
  - p137 BYD Q2 2026 total vehicle sales = **1,108,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 销量110.8 万台,同环比分别-3.2%和+58.2%"
  - p138 BYD Q2 2026 overseas sales share of total sales = **42.4** % (2026-04-01..2026-06-30) [keep: ] quote: "其中海外表现强势,出海占比达42.4%,同环比+19.9pct 和-3.3pct"
  - p139 BYD Q2 2026 overseas sales share change year-on-year = **19.9** pct (2026-04-01..2026-06-30) [keep: ] quote: "出海占比达42.4%,同环比+19.9pct 和-3.3pct"
  - p140 BYD Q2 2026 overseas sales share change quarter-on-quarter = **-3.3** pct (2026-04-01..2026-06-30) [keep: ] quote: "出海占比达42.4%,同环比+19.9pct 和-3.3pct"
  - p141 BYD Q2 2026 per-vehicle ASP excluding BYD Electronics = **136,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 单车ASP 约13.6 万元(扣除比电),同环比分别-0.1 和-2.4 万元"
  - p142 BYD Q2 2026 per-vehicle ASP change quarter-on-quarter = **-24,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "单车ASP 约13.6 万元(扣除比电),同环比分别-0.1 和-2.4 万元"
  - p143 BYD Q2 2026 gross margin = **18.9** % (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 毛利率约18.9%,同环比分别+2.6pct/+0.1pct"
  - p144 BYD Q2 2026 gross margin excluding BYD Electronics = **23** % (2026-04-01..2026-06-30) [keep: ] quote: "剔除比电后业务毛利率约23.0%,同环比+4.3pct/-0.4pct"
  - p145 BYD Q2 2026 per-vehicle net profit attributable to parent excluding BYD Electron = **7,200** CNY/vehicle (2026-04-01..2026-06-30) [DISCARD: Per-vehicle net profit, not revenue.] quote: "扣除比亚迪电子来看,2026Q2 单车利润0.72 万元,同比+0.23 万元,环比+0.14 万元"
  - p146 BYD Q2 2026 net profit attributable to parent = **8,240,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Net profit, not revenue.] quote: "实现归母净利润82.4 亿元,同比+29.7%,环比+101.8%"
  - p147 BYD Q2 2026 total revenue change year-on-year = **-3.2** % (2026-04-01..2026-06-30) [keep: ] quote: "2026 年Q2 实现收入1945.9 亿元,同环比分别-3.2%和+29.5%"
  - p148 BYD Q2 2026 total revenue change quarter-on-quarter = **29.5** % (2026-04-01..2026-06-30) [keep: ] quote: "2026 年Q2 实现收入1945.9 亿元,同环比分别-3.2%和+29.5%"
- `https://eu.36kr.com/zh/p/3960707064708480` -> **live_dated** (page date 2026-08-30); points raw/verified 15/15
  - p149 BYD Q2 2026 total revenue = **194,600,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "二季度,比亚迪总收入 1946 亿,同比继续下滑 3%,低于市场预期的 1995 亿"
  - p150 BYD Q2 2026 per-vehicle selling price (ASP) = **136,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "二季度,比亚迪卖车单价为 13.6 万元,环比大幅下滑 2.4 万元,也低于市场此前预期的 14.4 万元。"
  - p151 BYD Q2 2026 export share of sales = **43.3** % (2026-04-01..2026-06-30) [keep: ] quote: "出口销量占比环比回落 3.3 个百分点至 43.3%"
  - p152 BYD Q1 2026 export share of sales = **46.6** % (2026-01-01..2026-03-31) [keep: ] quote: "Q1 出口占比高达 46.6%"
  - p153 BYD Q2 2026 total vehicle sales = **1,110,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "二季度比亚迪总销量达 111 万辆,环比提升 58%"
  - p154 BYD Q1 2026 total vehicle sales = **700,000** vehicle (2026-01-01..2026-03-31) [keep: ] quote: "Q2 总销量约 111 万辆,环比 Q1 的 70 万辆增长约 58%"
  - p155 BYD Q2 2026 overseas sales volume = **470,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "海外业务在 2026 年二季度单季继续狂销 47 万辆,仍然贡献了高达 43% 的销量占比。"
  - p156 BYD Q2 2026 domestic sales volume = **640,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "Q2 国内销量环比提升 68% 至约 64 万辆"
  - p157 BYD Q2 2026 per-vehicle cost = **105,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "二季度,比亚迪单车成本约 10.5 万元,环比反而下滑约 1.8 万元"
  - p158 BYD Q2 2026 automotive gross margin = **23** % (2026-04-01..2026-06-30) [keep: ] quote: "而二季度实际汽车业务毛利率为 23%,环比仅下滑 0.4 个百分点"
  - p159 BYD Q2 2026 per-vehicle gross profit = **31,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "本季度,比亚迪实现单车毛利 3.1 万元, 环比上季度下滑了 0.6 万元"
  - p160 BYD 2026 full-year export target (raised range) = **1,750,000** (range 1,700,000..1,800,000) as written "170~180 万辆", value check pending vehicle (2026-01-01..2026-12-31) [keep: ] quote: "公司再次上调年初 150 万辆的出口目标至 170~180 万辆(实际有望向 190 万辆冲刺)"
  - p161 BYD 2026 Jan-Jul cumulative export sales = **970,000** vehicle (2026-01-01..2026-07-31) [keep: ] quote: "2026 年 1~7 月,比亚迪已实现出口销量 97 万辆,目标实现的确定度很高"
  - p162 BYD 2026 full-year total sales forecast (Haitun neutral) = **4,650,000** vehicle (2026-01-01..2026-12-31) [keep: ] quote: "最后比亚迪 2026 年总销量 465 万辆,仅同比上行 1%"
  - p163 BYD 2026 full-year domestic sales forecast (Haitun neutral) = **2,850,000** vehicle (2026-01-01..2026-12-31) [keep: ] quote: "海豚君在中性假设下预计国内销量继续同比下滑 20% 至 285 万辆"
- `https://data.eastmoney.com/report/zw_stock.jshtml?encodeUrl=X/ezSdKusjEQp1ltw6d/4ZvGRoHSw+PH+k4131wzorA=` -> **live_dated** (page date 2026-08-30); points raw/verified 15/14
  - p164 BYD 2026Q2 total revenue = **194,600,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 公司实现收入 1946亿元、同比-3%、环比+30%"
  - p165 BYD 2026Q2 automotive business revenue = **150,500,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "26Q2 汽车业务收入1505 亿元、同比-4%、环比+34%"
  - p166 BYD 2026Q2 vehicle sales volume = **1,110,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "其中汽车销售 111 万台、同比-3%、环比+58%"
  - p167 BYD 2026Q2 per-vehicle ASP = **136,000** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "单车 ASP 为 13.6 万元、同/环比分别-0.1/-2.4 万元"
  - p168 BYD 2026Q2 export volume = **470,000** vehicle (2026-04-01..2026-06-30) [keep: ] quote: "Q2 出口 47 万台,环比+47%,在销量中占比环比-3pct"
  - p169 BYD 2026Q2 export share of sales, change quarter-on-quarter = **-3** % (2026-04-01..2026-06-30) [keep: ] quote: "在销量中占比环比-3pct"
  - p170 BYD 2026H1 domestic ASP (automotive and related business) = **143,000** CNY/vehicle (2026-01-01..2026-06-30) [keep: ] quote: "26H1 出口/国内 ASP 分别为 16.3/14.3 万元"
  - p171 BYD 2026Q2 automotive business gross margin = **23** % (2026-04-01..2026-06-30) [keep: ] quote: "26Q2 汽车业务毛利率 23.0%,同比+4.3pct、环比-0.4pct"
  - p172 BYD 2026Q2 export share of sales, change year-on-year = **20** % (2026-04-01..2026-06-30) [keep: ] quote: "二是出口销量占比同比提高 20pct"
  - p173 BYD 2026H1 export gross margin (automotive and related business) = **28.4** % (2026-01-01..2026-06-30) [keep: ] quote: "26H1 出口/国内毛利率分别为 28.4%/17.0%"
  - p174 BYD 2026H1 domestic gross margin (automotive and related business) = **17** % (2026-01-01..2026-06-30) [keep: ] quote: "26H1 出口/国内毛利率分别为 28.4%/17.0%"
  - p175 BYD full-year 2026 export volume forecast (analyst, at least) = **1,800,000** vehicle (2026-01-01..2026-12-31) [keep: ] quote: "我们预计全年出口销量有望达到 180 万以上"
  - p176 BYD 2026Q2 adjusted per-vehicle profit (after FX, ex-BYD Electronics) = **9,300** CNY/vehicle (2026-04-01..2026-06-30) [keep: ] quote: "该口径下 Q2 单车利润 0.93 万元、同/环比分别上涨 0.6/0.1 万元"
  - p177 BYD 2026Q2 adjusted profit (after FX, ex-BYD Electronics) = **10,300,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "26Q2 还原后利润约 103 亿、同比+182%、环比+76%"
- `http://stockfinance.sina.cn/stock/go.php/paper/reportid/841966543372/index.phtml` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- `https://www.cnfin.com/announ/detail/index.html?id=844705253353&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/841438320321/index.phtml` -> **live_dated** (page date 2026-08-30); points raw/verified 15/15
  - p178 BYD 1H26 total revenue (营业收入), year-on-year change = **-7.1** % (2026-01-01..2026-06-30) [keep: ] quote: "1H26 总收入同比-7.1%至3,448.2 亿元"
  - p179 BYD 1H26 total revenue (营业收入) = **344,820,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "1H26 总收入同比-7.1%至3,448.2 亿元"
  - p180 BYD 2Q26 revenue (营业收入), year-on-year change = **-3.2** % (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p181 BYD 2Q26 revenue (营业收入), quarter-on-quarter change = **29.5** % (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p182 BYD 2Q26 revenue (营业收入) = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p183 BYD 2Q26 sales volume, quarter-on-quarter change = **58.2** % (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 业绩环比修复主要受益于销量改善(环比+58.2%)"
  - p184 BYD 1H26 total sales volume = **1,810,000** vehicle (2026-01-01..2026-06-30) [keep: ] quote: "1H26 比亚迪总销量同比-15.7%至181 万辆"
  - p185 BYD 1H26 total sales volume, year-on-year change = **-15.7** % (2026-01-01..2026-06-30) [keep: ] quote: "1H26 比亚迪总销量同比-15.7%至181 万辆"
  - p186 BYD 1H26 mid-to-high-end sub-brand (Fangchengbao+Denza+Yangwang) sales volume, y = **61** % (2026-01-01..2026-06-30) [keep: ] quote: "中高端子品牌(方程豹+腾势+仰望)销量同比+61%(销量占比抬升至12.8%)"
  - p187 BYD 1H26 mid-to-high-end sub-brand share of total sales volume = **12.8** % (2026-01-01..2026-06-30) [keep: ] quote: "中高端子品牌(方程豹+腾势+仰望)销量同比+61%(销量占比抬升至12.8%)"
  - p188 BYD 1H26 total exports, year-on-year change = **67.8** % (2026-01-01..2026-06-30) [keep: ] quote: "总出口同比+67.8%(销量占比抬升至近44%)"
  - p189 BYD 1H26 export share of total sales volume = **44** % (2026-01-01..2026-06-30) [keep: ] quote: "总出口同比+67.8%(销量占比抬升至近44%)"
  - p190 BYD 1H26 automotive and related business revenue, year-on-year change = **-9** % (2026-01-01..2026-06-30) [keep: ] quote: "1H26 比亚迪汽车及相关业务收入同比-9.0%,毛利率同比+2.0pcts"
  - p191 BYD 1H26 domestic automotive and related business revenue = **145,600,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "国内汽车及相关业务收入同比-33.6%至1,456 亿元、毛利率同比-0.7pcts 至17%"
  - p192 BYD 1H26 overseas automotive and related business revenue = **129,500,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "海外汽车及相关业务收入同比+55.8%至1,295 亿元、毛利率同比+1.1pcts 至28.4%"
- `https://www.aastocks.com/en/stocks/news/aafn-con/now.1549400/popular-news/aafn` -> **live_dated** (page date 2026-10-15); points raw/verified 15/12
  - p193 Goldman Sachs forecast BYD 3Q26 revenue = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p194 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p195 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p196 Goldman Sachs forecast BYD 3Q26 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p197 Goldman Sachs forecast BYD 3Q26 sales volume growth YoY = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p198 Goldman Sachs forecast BYD 3Q26 sales volume growth QoQ = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p199 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p200 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p201 BYD Hungary plant planned annual capacity (production expected by end-2026) = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Hungary plant capacity is not expected to produce until end-2026; no Q3 2026 revenue contribution.] quote: "Hungary plant is expected to commence production by the end of 2026 with planned annual capacity of 300,000 vehicles"
  - p202 China NEV export VAT rebate rate before reduction = **13** % (..2027-03-31) [DISCARD: NEV export VAT rebate change affects 2027, not Q3 2026 revenue.] quote: "the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p203 Goldman Sachs assumed cost pass-through for VAT rebate change = **67** % (not stated (page dated 2026-10-15)) [DISCARD: VAT rebate pass-through assumption for 2027, not Q3 2026 revenue.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
  - p204 Goldman Sachs estimated 2027 earnings reduction from VAT rebate change = **4** % (2027-01-01..2027-12-31) [DISCARD: Estimated 2027 earnings impact, not Q3 2026 revenue.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- `https://www.moomooapp.com/hant/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://in.investing.com/equities/byd-a-earnings?pageNum=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/815234016884/index.phtml` -> **live_dated** (page date 2025-10-31); points raw/verified 15/14
  - p205 BYD Q3 2025 total operating revenue = **195,000,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 公司实现营业收入1950 亿元、同比-3%、环比-3%"
  - p206 BYD Q3 2025 automotive business revenue = **152,300,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 公司实现汽车业务收入1523 亿元、同比-3%、环比-3%"
  - p207 BYD Q3 2025 passenger vehicle sales volume = **1,106,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 公司乘用车销售110.6 万辆,同/环比分别-2.1%/-1.9%"
  - p208 BYD Q3 2025 per-vehicle ASP = **138,000** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 单车ASP 为13.8 万元,同/环比分别-0.2/-0.2 万元"
  - p209 BYD Q3 2025 export sales volume = **233,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "1出口销售23.3 万台,同/环比分别+149%/-10%"
  - p210 BYD Q3 2025 three high-end brands sales volume (excluding 钛3) = **65,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2三大高端品牌(剔除ASP 较低的钛3)销售6.5 万台,同/环比分别+49%/-4%"
  - p211 BYD Q3 2025 automotive business gross margin = **20.6** % (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 汽车业务毛利率20.6%,同比-2.7pct、环比+1.9pct"
  - p212 BYD Q3 2025 per-vehicle profit = **7,100** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 单车利润0.71 万元"
  - p213 BYD Q3 2025 per-vehicle profit excluding non-recurring and BYD Electronics equit = **5,400** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "扣非且剔除比亚迪电子权益贡献后单车盈利0.54 万元"
  - p214 BYD Q3 2025 R&D expense = **14,200,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "研发费用同/环比+3%/-8%至142 亿元"
  - p215 BYD Q3 2025 sales expense ratio = **3.1** % (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 销售/管理/研发费用率分别为3.1%/2.5%/7.3%"
  - p216 BYD Q3 2025 management expense ratio = **2.5** % (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 销售/管理/研发费用率分别为3.1%/2.5%/7.3%"
  - p217 BYD Q3 2025 R&D expense ratio = **7.3** % (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 销售/管理/研发费用率分别为3.1%/2.5%/7.3%"
  - p218 BYD Q3 2025 net profit attributable to parent = **7,800,000,000** CNY (2025-07-01..2025-09-30) [DISCARD: Net profit, not revenue.] quote: "归母净利润78 亿元、同比-33%、环比+23%"
- `https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/816054180307/index.phtml` -> **live_dated** (page date 2025-11-10); points raw/verified 14/14
  - p219 BYD Q3 2025 consolidated operating revenue = **194,980,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "2025 年Q3 实现营业收入1949.8 亿元,同比-3.1%,环比-3.0%"
  - p220 BYD Q3 2025 automotive revenue excluding BYD Electronics = **152,310,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "扣除比亚迪电子后,汽车收入约1523.1 亿元,同环比分别下降3.3%和3.1%"
  - p221 BYD Q3 2025 total vehicle sales = **1,114,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 总销量111.4 万辆,同环比分别下降1.8%和2.7%"
  - p222 BYD Q3 2025 overseas vehicle sales = **231,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "其中海外销量维持高位,出海销量23.1 万辆,环比-10%"
  - p223 BYD Q3 2025 overseas sales share of total sales = **20.8** % (2025-07-01..2025-09-30) [keep: ] quote: "出海占比约20.8%,同环比+12.5pct 和-1.7pct"
  - p224 BYD Q3 2025 revenue per vehicle (excluding solar, rail and other businesses) = **137,000** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "2025 年Q3 单车收入约13.7 万元(不考虑光伏、轨交等其他业务),同环比分别下降0.22 万元和0.06 万元"
  - p225 BYD Q3 2025 gross margin = **17.6** % (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3 毛利率约17.6%,环比提升1.3pct,同比-2.5pct"
  - p226 BYD Q3 2025 vehicle business gross margin = **20.6** % (2025-07-01..2025-09-30) [keep: ] quote: "整车业务毛利率约20.6%,环比提升1.9pct,同比-2.7pct"
  - p227 BYD Q3 2025 net profit attributable to parent = **7,820,000,000** CNY (2025-07-01..2025-09-30) [DISCARD: Net profit, not revenue.] quote: "实现归母净利润78.2 亿元,同比-32.6%,环比+23.1%"
  - p228 BYD Q3 2025 non-recurring net profit attributable to parent = **6,890,000,000** CNY (2025-07-01..2025-09-30) [DISCARD: Non-recurring net profit, not revenue.] quote: "实现扣非归母净利润68.9 亿元,同比-36.6%,环比+26.9%"
  - p229 BYD Q3 2025 profit per vehicle excluding BYD Electronics = **6,200** CNY/vehicle (2025-07-01..2025-09-30) [DISCARD: Per-vehicle profit, not revenue.] quote: "扣除比亚迪电子来看,2025Q3 单车利润0.62万元,同比-33.7%,环比+26.0%"
  - p230 BYD Q3 2025 profit per vehicle excluding BYD Electronics, after adding back impa = **6,700** CNY/vehicle (2025-07-01..2025-09-30) [DISCARD: Per-vehicle profit, not revenue.] quote: "进一步加回减值后,单车利润0.67 万元,同比-36.7%,环比+22.8%"
  - p231 BYD Q3 2025 period expense ratio = **13** % (2025-07-01..2025-09-30) [keep: ] quote: "Q3 期间费用率约为13.0%"
  - p232 BYD full-year 2025 forecast net profit attributable to parent = **35,000,000,000** CNY (2025-01-01..2025-12-31) [DISCARD: Net profit forecast, not revenue.] quote: "预计 2025 年公司归母净利润350 亿元,对应PE 27X,维持"买入"评级"
- `https://data.eastmoney.com/report/info/AP202510311772394146.html` -> **live_dated** (page date 2025-10-31); points raw/verified 15/13
  - p233 BYD Q3 2025 vehicle sales including commercial vehicles = **1,114,000** vehicle (2025-07-01..2025-09-30) [keep: ] quote: "Q3公司销售汽车111.4万辆(包含商用车),同/环比-1.8%/-2.7%"
  - p234 BYD Q3 2025 total revenue = **194,980,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "营收1949.8亿元,同/环比-3.1%/-3.0%"
  - p235 BYD Q3 2025 automotive and battery business revenue = **152,300,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "其中汽车及电池业务营收1523亿元,同/环比-3.3%/-3.1%"
  - p236 BYD Q3 2025 per-vehicle ASP excluding BYD Electronics (analyst calculation) = **137,000** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "剔除比亚迪电子后,我们计算Q3单车ASP为13.7万元,同/环比-1.5%/-0.4%"
  - p237 BYD Q3 2025 per-vehicle ASP year-on-year change = **-1.5** % (2025-07-01..2025-09-30) [keep: ] quote: "我们计算Q3单车ASP为13.7万元,同/环比-1.5%/-0.4%"
  - p238 BYD Q3 2025 per-vehicle ASP quarter-on-quarter change = **-0.4** % (2025-07-01..2025-09-30) [keep: ] quote: "我们计算Q3单车ASP为13.7万元,同/环比-1.5%/-0.4%"
  - p239 BYD cumulative vehicle sales 2025 Q1-Q3 = **3,260,000** vehicle (2025-01-01..2025-09-30) [keep: ] quote: "25Q1-Q3,公司累计销售汽车326万辆,同比+18.9%"
  - p240 BYD cumulative revenue 2025 Q1-Q3 = **566,260,000,000** CNY (2025-01-01..2025-09-30) [keep: ] quote: "营收5662.6亿元,同比+12.7%,单车ASP13.6万元,同比-2.0%"
  - p241 BYD cumulative per-vehicle ASP 2025 Q1-Q3 = **136,000** CNY/vehicle (2025-01-01..2025-09-30) [keep: ] quote: "单车ASP13.6万元,同比-2.0%"
  - p242 BYD Q3 2025 gross margin = **17.6** % (2025-07-01..2025-09-30) [keep: ] quote: "公司Q3毛利率17.6%,同/环比-4.3pct/+1.3pct"
  - p243 BYD Q3 2025 automotive business gross margin = **20.6** % (2025-07-01..2025-09-30) [keep: ] quote: "其中汽车业务毛利率20.6%,同/环比-5.0pct/+1.9pct"
  - p244 BYD Q3 2025 net profit attributable to parent = **7,820,000,000** CNY (2025-07-01..2025-09-30) [DISCARD: Net profit, not revenue.] quote: "Q3归母净利78.2亿元,同/环比-32.6%/+23.1%"
  - p245 BYD Q3 2025 per-vehicle net profit excluding BYD Electronics = **6,200** CNY/vehicle (2025-07-01..2025-09-30) [DISCARD: Per-vehicle net profit, not revenue.] quote: "去除比电Q3单车净利0.62万元,同/环比-33.7%/+26%"
- dropped by code checks: 8 (scale word '万' not supported by quote or table header: 2; period year 2030 does not appear in the page text or URL (likely mis-dated): 2; period_end missing or unparseable: 1; scale word '亿' not supported by quote or table header: 3)

### d4 [related_series] Consolidated subsidiary BYD Electronic

Hypothesis: BYD Electronic (International) Company Limited is consolidated into BYD Company revenue and reports separately. Total operating revenue = automotive + BYD Electronic + other segments - intersegment eliminations. Its Q3 seasonality and H1 2026 run-rate can fill a material non-auto component.

Queries issued by the searcher: 比亚迪电子 2026 中期业绩 收入; BYD Electronic Q3 2026 revenue results; 比亚迪电子 2025年第三季度 收入 营业额 前三季度 同比; 比亚迪 2025年第三季度 营业收入 1949亿 三季度报告; 比亚迪电子 2026年中期业绩 收入; BYD Electronic Q3 2026 revenue; 比亚迪电子 2025年第三季度 收入 同比 前九个月 业绩; 比亚迪电子 前三季度 2026 收入 42.68亿 第三季度; 比亚迪电子 2026年中期业绩 收入; BYD Electronic Q3 2026 revenue; 比亚迪电子 2025年第三季度 营业收入 前三季度 同比; 比亚迪电子 2026年第一季度 收入 381.8亿; 比亚迪 2026年第三季度报告 营业收入 前三季度; 比亚迪 2025年第三季度 营业收入 1949亿 单季

- `https://www.zhitongcaijing.com/content/detail/1488073.html` -> **live_dated** (page date 2026-08-28); points raw/verified 15/15
  - p246 BYD Electronic H1 2026 revenue (six months ended 2026-06-30) = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 BYD Electronic revenue; p272 kept as the operative H1 revenue point.] quote: "该集团取得营业额人民币822.34亿元(单位下同),同比增加2.02%"
  - p247 BYD Electronic H1 2026 revenue year-on-year growth rate = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "营业额人民币822.34亿元(单位下同),同比增加2.02%"
  - p248 BYD Electronic H1 2026 profit attributable to owners of the parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit, not revenue.] quote: "母公司拥有人应占溢利4.26亿元,同比减少75.35%"
  - p249 BYD Electronic H1 2026 profit attributable to owners of the parent year-on-year  = **75.35** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit change, not revenue.] quote: "母公司拥有人应占溢利4.26亿元,同比减少75.35%"
  - p250 BYD Electronic H1 2026 earnings per share = **0.19** CNY per share (2026-01-01..2026-06-30) [DISCARD: BYD Electronic EPS, not revenue.] quote: "每股盈利0.19元"
  - p251 BYD Electronic H1 2026 smart terminal business revenue = **67,862,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic segment revenue detail, not needed for Q3 total.] quote: "本集团在智能终端业务领域取得678.62亿元的收入"
  - p252 BYD Electronic H1 2026 components revenue (smart terminal segment) = **11,912,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic component revenue detail, not needed for Q3 total.] quote: "其中零部件收入约 119.12亿元"
  - p253 BYD Electronic H1 2026 assembly revenue (smart terminal segment) = **55,950,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic assembly revenue detail, not needed for Q3 total.] quote: "组装收入约559.5亿元"
  - p254 BYD Electronic H1 2026 new energy vehicle business segment revenue = **13,619,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic NEV segment revenue detail, not needed for Q3 total.] quote: "本集团新能源汽车业务板块的收入约136.19亿元"
  - p255 BYD Electronic H1 2026 NEV segment share of total group revenue = **16.56** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic segment share, not needed.] quote: "占本集团总体收入约16.56%"
  - p256 BYD Electronic H1 2026 NEV segment revenue year-on-year growth = **6.43** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic NEV segment growth, not needed.] quote: "收入同比上升约6.43%"
  - p257 Global smartphone shipments H1 2026 (IDC) = **571,000,000** unit (2026-01-01..2026-06-30) [DISCARD: Global smartphone shipments, only indirect context for BYD Electronics and not needed.] quote: "2026年上半年全球智能手机出货量按年下跌4.8%至5.71亿部"
  - p258 Global smartphone shipments H1 2026 year-on-year change (IDC) = **4.8** % (2026-01-01..2026-06-30) [DISCARD: Smartphone shipment growth, only indirect context.] quote: "2026年上半年全球智能手机出货量按年下跌4.8%至5.71亿部"
  - p259 China automobile sales H1 2026 year-on-year change (CAAM) = **21.1** % (2026-01-01..2026-06-30) [DISCARD: China automobile sales growth, not direct BYD Q3 revenue.] quote: "2026年上半年国内汽车销量下降21.1%"
  - p260 China automobile exports H1 2026 year-on-year growth = **65.3** % (2026-01-01..2026-06-30) [DISCARD: China automobile export growth, not direct BYD Q3 revenue.] quote: "中国汽车出口同比增长65.3%"
- `https://il.investing.com/equities/byd-electronic-earnings` -> **dropped** (live http 403); points raw/verified -/-
- `https://stock.finance.sina.com.cn/hkstock/view/hk_report.php?reportid=815492069222` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://m.jrj.com.cn/madapter/24h/2026/08/28175558273075.shtml` -> **live_dated** (page date 2026-08-28); points raw/verified 4/2
  - p261 BYD Electronic H1 2026 operating revenue (营业收入), consolidated = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 BYD Electronic revenue; p272 kept.] quote: "2026年上半年实现营业收入822.34亿元,去年同期为806.06亿元"
  - p262 BYD Electronic H1 2026 net profit attributable to shareholders of listed company = **4,263,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit, not revenue.] quote: "归属于上市公司股东的净利润42.63亿元,去年同期为17.3亿元"
- `https://www.tipranks.com/stocks/hk:0285/revenue` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.boerse-global.de/byd-electronic-aktie-cicc-senkt-gewinnprognosen-um-12/811661` -> **live_dated** (page date 2026-07-22); points raw/verified 15/9
  - p263 BYD Electronic revenue, first nine months of 2026 (cumulative, year-on-year grow = **0.95** as written "0,95 %", value check pending % (2026-01-01..2026-09-30) [keep: ] quote: "Der Umsatz stieg im Vergleich zum Vorjahreszeitraum um 0,95 % auf 123,3 Milliarden RMB."
  - p264 BYD Electronic net profit, first nine months of 2026 (year-on-year growth) = **2.4** as written "2,4 %", value check pending % (2026-01-01..2026-09-30) [keep: ] quote: "Auch der Nettogewinn konnte leicht um 2,4 % auf 3,14 Milliarden RMB zulegen."
  - p265 BYD Electronic quarterly revenue, Q3 2026 (year-on-year change) = **2** % (2026-07-01..2026-09-30) [DISCARD: Conflicts with 9M less H1 BYD Electronic revenue arithmetic and has an implausible pre-Q3-end publication date; unusable] quote: "Der Quartalsumsatz sank im Jahresvergleich um 2 % auf 42,68 Milliarden RMB."
  - p266 BYD Electronic quarterly net profit, Q3 2026 (year-on-year change) = **9** % (2026-07-01..2026-09-30) [DISCARD: BYD Electronic Q3 net profit, not revenue, and period alignment conflicts with 9M/H1 arithmetic.] quote: "Der Nettogewinn ging im selben Zeitraum um 9 % auf 1,41 Milliarden RMB zurück"
  - p267 BYD Electronic Q3 2026 net profit, quarter-on-quarter change vs Q2 2026 = **27** % (2026-07-01..2026-09-30) [DISCARD: QoQ net profit change for BYD Electronic, not revenue and likely mis-dated.] quote: "konnte sich jedoch im Vergleich zum vorangegangenen zweiten Quartal um 27 % steigern."
  - p268 CICC cut to BYD Electronic net profit forecast for 2025 = **12** % (2025-01-01..2025-12-31) [DISCARD: Net profit forecast revision, not revenue.] quote: "Senkung der erwarteten Nettogewinne für die Jahre 2025 und 2026 um 12 % beziehungsweise 6 %."
  - p269 CICC cut to BYD Electronic net profit forecast for 2026 = **6** % (2026-01-01..2026-12-31) [DISCARD: Net profit forecast revision, not revenue.] quote: "Senkung der erwarteten Nettogewinne für die Jahre 2025 und 2026 um 12 % beziehungsweise 6 %."
  - p270 BYD Co. battery-electric vehicle deliveries, Q2 2026 = **557** vehicle (2026-04-01..2026-06-30) [DISCARD: BEV deliveries stated as 557, unit malformed; likely 557,090, not usable as monthly vehicle volume.] quote: "im zweiten Quartal 2026 mit 557.090 ausgelieferten batterieelektrischen Fahrzeugen (BEV) Tesla übertreffen konnte"
  - p271 China automotive production profit margin (media-reported low) = **1.5** as written "1,5 %", value check pending % (not stated (page dated 2026-07-22)) [DISCARD: China auto production margin, not direct BYD Q3 revenue.] quote: "In China sinken die Gewinnmargen in der Automobilproduktion laut Medienberichten auf einen Tiefstand von 1,5 %"
- `https://www.finanzen.net/schaetzungen/byd_electronic` -> **dropped** (live http 403); points raw/verified -/-
- `https://4g.stockstar.com/detail/AN2026082800053137` -> **live_dated** (page date 2026-10-27); points raw/verified 9/9
  - p272 BYD Electronic (International) Company Limited revenue, six months ended 2026-06 = **82,234,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "截至2026年6月30日止六个月,集团实现营业收入约822.34亿元人民币,同比增长2.02%"
  - p273 BYD Electronic H1 2026 revenue year-on-year growth rate = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "集团实现营业收入约822.34亿元人民币,同比增长2.02%"
  - p274 BYD Electronic profit attributable to owners of the parent, six months ended 202 = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit, not revenue.] quote: "母公司拥有人应占溢利约为4.26亿元人民币,同比下降75.35%"
  - p275 BYD Electronic profit attributable to owners of the parent H1 2026 year-on-year  = **75.35** % (2026-01-01..2026-06-30) [DISCARD: Net profit change, not revenue.] quote: "母公司拥有人应占溢利约为4.26亿元人民币,同比下降75.35%"
  - p276 BYD Electronic gross margin, H1 2026 = **4.91** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic gross margin, not revenue.] quote: "毛利率由2025年同期的6.88%下降至4.91%"
  - p277 BYD Electronic gross margin, H1 2025 (prior-year comparative) = **6.88** % (2025-01-01..2025-06-30) [DISCARD: BYD Electronic prior-year gross margin, not revenue.] quote: "毛利率由2025年同期的6.88%下降至4.91%"
  - p278 Smart terminal business share of BYD Electronic revenue, H1 2026 = **82.5** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic segment share, not consolidated revenue.] quote: "智能终端业务收入占比达82.5%"
  - p279 BYD Electronic new energy vehicle business revenue year-on-year growth, H1 2026 = **6.43** % (2026-01-01..2026-06-30) [keep: ] quote: "新能源汽车业务收入同比增长6.43%"
  - p280 BYD Electronic research and development expenditure, H1 2026 = **1,964,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic R&D expenditure, not revenue.] quote: "研发开支达19.64亿元人民币,重点投向AI相关领域"
- `https://hk.stockstar.com/IG2026083100014943.shtml` -> **live_dated** (page date 2026-08-31); points raw/verified 15/14
  - p281 BYD Electronic H1 2026 revenue (first half total) = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 BYD Electronic revenue; p272 kept.] quote: "上半年公司实现收入822.34亿元,同比微增2.02%"
  - p282 BYD Electronic H1 2026 revenue year-on-year growth rate = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "上半年公司实现收入822.34亿元,同比微增2.02%"
  - p283 BYD Electronic H1 2026 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit, not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p284 BYD Electronic H1 2026 net profit attributable to parent year-on-year change = **75.35** % (2026-01-01..2026-06-30) [DISCARD: Net profit change, not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p285 BYD Electronic H1 2026 net foreign exchange loss = **702,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic FX loss, not revenue.] quote: "期内录得外汇亏损净额约7.02亿元"
  - p286 BYD Electronic H1 2026 smart terminal business revenue = **67,862,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic smart-terminal segment revenue detail, not needed for Q3 total.] quote: "上半年智能终端业务收入678.62亿元"
  - p287 BYD Electronic H1 2026 component business revenue (within smart terminal) = **11,912,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic component segment revenue detail, not needed for Q3 total.] quote: "其中零部件业务收入119.12亿元,同比下降"
  - p288 BYD Electronic H1 2026 new energy vehicle business revenue = **13,619,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "新能源汽车业务收入136.19亿元,同比上升6.43%"
  - p289 BYD Electronic H1 2026 new energy vehicle business revenue year-on-year growth r = **6.43** % (2026-01-01..2026-06-30) [keep: ] quote: "新能源汽车业务收入136.19亿元,同比上升6.43%"
  - p290 BYD Electronic H1 2026 AI computing infrastructure revenue = **753,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic AI infrastructure revenue, immaterial and not needed.] quote: "AI算力基础设施收入7.53亿元,同比下降10.57%"
  - p291 BYD Electronic H1 2026 AI computing infrastructure revenue year-on-year change = **10.57** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic AI infrastructure revenue change, not needed.] quote: "AI算力基础设施收入7.53亿元,同比下降10.57%"
  - p292 BYD Electronic share price intraday gain on 2026-08-31 = **9.29** % (2026-08-31..2026-08-31) [DISCARD: BYD Electronic share price, not revenue.] quote: "截至发稿,涨9.29%,报27.06港元"
  - p293 BYD Electronic share price on 2026-08-31 = **27.06** HKD (2026-08-31..2026-08-31) [DISCARD: BYD Electronic share price, not revenue.] quote: "截至发稿,涨9.29%,报27.06港元"
  - p294 BYD Electronic turnover on 2026-08-31 = **1,278,000,000** HKD (2026-08-31..2026-08-31) [DISCARD: BYD Electronic turnover, not revenue.] quote: "成交额12.78亿港元"
- `https://finance.baidu.com/stock/hk-00285?mainTab=%E8%B4%A2%E5%8A%A1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://hk.stockstar.com/IG2026090100015216.shtml` -> **live_dated** (page date 2026-09-01); points raw/verified 15/15
  - p295 BYD Electronic H1 2026 total revenue = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 BYD Electronic revenue; p272 kept.] quote: "比亚迪电子(00285.HK)2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p296 BYD Electronic H1 2026 revenue year-on-year growth = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p297 BYD Electronic H1 2026 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic net profit, not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p298 BYD Electronic H1 2026 gross margin = **4.91** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic gross margin, not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p299 BYD Electronic H1 2026 gross margin year-on-year change (percentage points) = **1.97** percentage points (2026-01-01..2026-06-30) [DISCARD: BYD Electronic gross margin change, not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p300 BYD Electronic H1 2026 smart terminal business revenue = **67,348,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic segment revenue detail, not needed for Q3 total.] quote: "2026H1智能终端业务收入673.48亿元,同比增长约1.4%"
  - p301 BYD Electronic H1 2026 assembly business revenue = **55,522,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic assembly segment revenue detail, not needed for Q3 total.] quote: "其中组装业务收入555.22亿元,同比增长约5.1%"
  - p302 BYD Electronic H1 2026 component business revenue = **11,826,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic component segment revenue detail, not needed for Q3 total.] quote: "零部件业务收入118.26亿元,同比下降约13.3%"
  - p303 BYD Electronic H1 2026 new energy vehicle business revenue = **13,515,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic NEV segment revenue detail, not needed for Q3 total.] quote: "2026H1新能源汽车业务收入135.15亿元,同比增长6.4%"
  - p304 BYD Electronic H1 2026 AI computing infrastructure revenue = **751,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic AI infrastructure revenue detail, not needed for Q3 total.] quote: "AI算力基础设施方面,2026H1实现收入7.51亿元,同比下降9.74%"
  - p305 BYD Electronic server business full-year 2026 revenue forecast (at least) = **3,000,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Server business annual revenue forecast, immaterial and not Q3 2026 consolidated revenue.] quote: "服务器业务全年收入预计达30亿元以上"
  - p306 CSC forecast BYD Electronic 2026 revenue = **181,086,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: BYD Electronic annual 2026 revenue forecast, not Q3 2026 consolidated revenue.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p307 CSC forecast BYD Electronic 2027 revenue = **199,602,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: BYD Electronic annual 2027 revenue forecast, not Q3 2026 consolidated revenue.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p308 CSC forecast BYD Electronic 2026 revenue year-on-year growth = **0.9** % (2026-01-01..2026-12-31) [DISCARD: BYD Electronic annual revenue growth forecast, not Q3 2026 consolidated revenue.] quote: "同比增长0.90%和10.23%"
  - p309 CSC forecast BYD Electronic 2027 revenue year-on-year growth = **10.23** % (2027-01-01..2027-12-31) [DISCARD: BYD Electronic annual revenue growth forecast, not Q3 2026 consolidated revenue.] quote: "同比增长0.90%和10.23%"
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/285/hk6/now.1480270/hk-stock-news` -> **live_dated** (page date 2025-10-30); points raw/verified 5/5
  - p310 BYD Electronic (00285.HK) revenue for first three quarters (Jan-Sep) 2026, cumul = **123,285,000,000** CNY (2026-01-01..2026-09-30) [keep: ] quote: "公布截至今年9月底止首三季业绩,营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p311 BYD Electronic first three quarters 2026 revenue year-on-year growth = **0.9** % (2026-01-01..2026-09-30) [keep: ] quote: "营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p312 BYD Electronic first three quarters 2026 net profit, cumulative = **3,137,000,000** CNY (2026-01-01..2026-09-30) [DISCARD: Net profit, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p313 BYD Electronic first three quarters 2026 net profit year-on-year growth = **2.4** % (2026-01-01..2026-09-30) [DISCARD: Net profit growth, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p314 BYD Electronic first three quarters 2026 earnings per share = **1.39** CNY per share (2026-01-01..2026-09-30) [DISCARD: EPS, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
- dropped by code checks: 9 (period year 2025 does not appear in the page text or URL (likely mis-dated): 3; number: unknown scale word 'Milliarden': 6)

### d5 [related_series] Segment disclosures and other businesses

Hypothesis: Rechargeable batteries/PV, other businesses and intersegment eliminations bridge automotive plus BYD Electronic revenue to consolidated operating revenue. H1 2026 and 2025 segment shares can estimate the residual if quarterly segment data are unavailable.

Queries issued by the searcher: 比亚迪 2026 半年报 分部报告 营业收入 电池 光伏; BYD 2026 interim report segment revenue elimination; 比亚迪 2025年年度报告 分部报告 汽车 电子 二次充电电池及光伏 营业收入 抵销; 比亚迪 2026年第三季度报告 营业收入 第三季度; 比亚迪 2026 半年报 分部报告 营业收入 电池 光伏; BYD 2026 interim segment revenue elimination; 比亚迪 2025年年度报告 分部 二次充电电池及光伏 收入 手机部件及组装 抵销; 比亚迪 2026年第三季度报告 营业收入 第三季度; 比亚迪 2026 半年报 分部报告 营业收入 电池 光伏; BYD 2026 interim results segment revenue elimination; 比亚迪 2025年年度报告 汽车、汽车相关产品及其他产品 收入 电子 其他 分部; 比亚迪 2026年 三季度 销量 7月 8月 9月 产销快报

- `https://data.eastmoney.com/notices/detail/002594/AN202608281828646431.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://emweb.securities.eastmoney.com/BusinessAnalysis/Index?code=sz002594` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- `https://finance.jrj.com.cn/2026/08/29112458283578.shtml` -> **live_dated** (page date 2026-08-29); points raw/verified 15/14
  - p315 BYD H1 2026 consolidated operating revenue (营业收入) = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "报告期内,公司实现营业收入3448.15亿元,同比下降7.13%"
  - p316 BYD Q2 2026 consolidated operating revenue = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2026年第二季度实现营业收入1945.90亿元"
  - p317 BYD H1 2026 automobiles and related products and other products segment revenue = **275,341,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "汽车、汽车相关产品及其他产品业务收入2753.41亿元,同比下降8.98%,占总收入79.85%"
  - p318 BYD H1 2026 automobiles and related products and other products segment share of = **79.85** % (2026-01-01..2026-06-30) [keep: ] quote: "汽车、汽车相关产品及其他产品业务收入2753.41亿元,同比下降8.98%,占总收入79.85%"
  - p319 BYD H1 2026 electronics and other products segment revenue = **69,405,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "电子及其他产品业务收入694.05亿元,同比增长0.96%,占总收入20.13%"
  - p320 BYD H1 2026 electronics and other products segment share of total revenue = **20.13** % (2026-01-01..2026-06-30) [keep: ] quote: "电子及其他产品业务收入694.05亿元,同比增长0.96%,占总收入20.13%"
  - p321 BYD H1 2026 overseas revenue = **181,268,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "上半年境外收入1812.68亿元,同比增长约34%,占总营收比重从去年同期的36%跃升至52.57%"
  - p322 BYD H1 2026 overseas revenue share of total revenue = **52.57** % (2026-01-01..2026-06-30) [keep: ] quote: "占总营收比重从去年同期的36%跃升至52.57%"
  - p323 BYD H1 2026 R&D investment = **28,900,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: R&D investment, not revenue.] quote: "上半年研发投入约289亿元,现金储备达1674亿元"
  - p324 BYD H1 2026 net profit attributable to shareholders = **12,325,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit, not revenue.] quote: "归母净利润123.25亿元"
  - p325 BYD Q2 2026 gross margin = **18.9** % (2026-04-01..2026-06-30) [keep: ] quote: "二季度毛利率升至18.9%,创近一年新高"
  - p326 Guohai Securities forecast BYD FY2026 revenue = **932,200,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year 2026 revenue forecast is an outlier relative to H1 2026 and derived Q3 run-rate; not usable for Q3 2026.] quote: "国海证券预计比亚迪2026年全年将实现营收9322亿元,同比增长16%"
  - p327 BYD H1 2026 new energy vehicle cumulative sales volume = **1,808,500** vehicle (2026-01-01..2026-06-30) [keep: ] quote: "2026年上半年比亚迪新能源汽车累计销量180.85万辆,同比下降15.72%"
  - p328 BYD H1 2026 cumulative exports = **790,000** vehicle (2026-01-01..2026-06-30) [keep: ] quote: "上半年累计出口79万辆,同比增长68%,占总销量比重约44%"
- `https://news.10jqka.com.cn/tapp/notice.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://stocks.etnet.hk/www/sc/stocks/realtime/quote_ci_detail.php?code=1211` -> **live_dated** (page date 2026-10-27); points raw/verified 15/14
  - p329 BYD H1 2026 total revenue (turnover), China GAAP = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "截至2026年6月止六个月,集团营业额下降7.1%至3448.15亿元"
  - p330 BYD H1 2026 electronics and other products revenue = **69,405,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%"
  - p331 BYD H1 2026 electronics and other products share of total revenue = **20.1** % (2026-01-01..2026-06-30) [keep: ] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%"
  - p332 BYD H1 2026 automobiles and related products and other products revenue = **275,341,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元,占总营业额79.9%"
  - p333 BYD H1 2026 automobiles and related products and other products share of total r = **79.9** % (2026-01-01..2026-06-30) [keep: ] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元,占总营业额79.9%"
  - p334 BYD H1 2026 total gross profit = **64,989,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "整体毛利下降2.8%至649.89亿元,毛利率则上升0.8个百分点至18.9%"
  - p335 BYD H1 2026 gross margin = **18.9** % (2026-01-01..2026-06-30) [keep: ] quote: "毛利率则上升0.8个百分点至18.9%"
  - p336 BYD H1 2026 electronics and other products total profit = **194,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "利润总额则减少 85.5%至1.94亿元"
  - p337 BYD H1 2026 shareholders' profit attributable = **12,295,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit, not revenue.] quote: "股东应占溢利下跌19.7%至122.95亿元"
  - p338 BYD total revenue year-on-year change H1 2026 = **7.1** % (2026-01-01..2026-06-30) [keep: ] quote: "集团营业额下降7.1%至3448.15亿元"
  - p339 BYD electronics and other products revenue year-on-year change H1 2026 = **1** % (2026-01-01..2026-06-30) [keep: ] quote: "电子及其他产品:营业额上升1%至694.05亿元"
  - p340 BYD automobiles and related products revenue year-on-year change H1 2026 = **9** % (2026-01-01..2026-06-30) [keep: ] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元"
  - p341 BYD inventory turnover days at 2026-06-30 = **109** day (2026-06-30..2026-06-30) [DISCARD: Inventory turnover days, not revenue.] quote: "存货周转天数为109日(2025年6月30日:79日)"
  - p342 BYD inventory turnover days at 2025-06-30 = **79** day (2025-06-30..2025-06-30) [DISCARD: Inventory turnover days prior year, not revenue.] quote: "存货周转天数为109日(2025年6月30日:79日)"
- `https://uobkh.com.sg/strapi-uploads/2_BYD_Company_1211_HK_6d7b71fcca.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.nikihou.jp/company/company.html?code=01211&market=HKM&type=news&news_id=601487&page=1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/002594/AN202603271820812475.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://beancount.io/blog/2026/09/26/byd-h1-2026-earnings-analysis` -> **live_dated** (page date 2026-09-26); points raw/verified 15/7
  - p343 BYD H1 2026 total contract revenue from segment disaggregation (note 4) = **344,511,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Contract-revenue note total, not needed for Q3 revenue.] quote: "(These are the note's contract-revenue totals of RMB 344,511 million, RMB 304 million below operating revenue.)"
  - p344 Gap between BYD H1 2026 operating revenue and note 4 contract-revenue total = **304,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Revenue-note gap, not needed for Q3 revenue.] quote: "(These are the note's contract-revenue totals of RMB 344,511 million, RMB 304 million below operating revenue.)"
  - p345 BYD H1 2026 consolidated operating revenue = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "\| Revenue \| RMB 344,815M \| RMB 371,281M \| -7.1% \|"
  - p346 BYD H1 2025 consolidated operating revenue = **371,281,000,000** CNY (2025-01-01..2025-06-30) [keep: ] quote: "\| Revenue \| RMB 344,815M \| RMB 371,281M \| -7.1% \|"
  - p347 BYD Q1 2026 reported revenue = **150,225,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Rounded duplicate of Q1 2026 revenue; p46 kept.] quote: "Q1 figures from the 2026 First Quarterly Report (revenue RMB 150,225 million, down 11.82%; attributable profit RMB 4,085 million, down 55.38%)"
  - p348 BYD Q1 2025 comparative revenue = **170,360,000,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "and that report's comparative column for Q1 2025 (RMB 170,360 million and RMB 9,155 million)"
  - p349 BYD H1 2026 overseas automotive revenue (cost disaggregation by place of operati = **129,487,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "puts overseas automotive revenue at RMB 129,487 million against cost of RMB 92,712 million, a 28.4% gross margin"
- `https://wap.stockstar.com/detail/SN2026032800002722` -> **live_dated** (page date 2026-10-23); points raw/verified 9/7
  - p350 BYD consolidated operating revenue, full year 2025 (annual report summary) = **803,964,958,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "营业收入 803,964,958,000.00 777,102,455,000.00 3.46% 602,315,354,000.00"
  - p351 BYD consolidated operating revenue, full year 2024 (comparative column) = **777,102,455,000** CNY (2024-01-01..2024-12-31) [keep: ] quote: "营业收入 803,964,958,000.00 777,102,455,000.00 3.46% 602,315,354,000.00"
  - p352 BYD consolidated operating revenue, Q1 2025 (quarterly table) = **170,360,448,000** CNY (2025-01-01..2025-03-31) [keep: ] quote: "营业收入 170,360,448,000.00 200,920,500,000.00 194,984,598,000.00 237,699,412,000.00"
  - p353 BYD consolidated operating revenue, Q2 2025 (quarterly table) = **200,920,500,000** CNY (2025-04-01..2025-06-30) [keep: ] quote: "营业收入 170,360,448,000.00 200,920,500,000.00 194,984,598,000.00 237,699,412,000.00"
  - p354 BYD consolidated operating revenue, Q3 2025 (quarterly table) = **194,984,598,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "营业收入 170,360,448,000.00 200,920,500,000.00 194,984,598,000.00 237,699,412,000.00"
  - p355 BYD consolidated operating revenue, Q4 2025 (quarterly table) = **237,699,412,000** CNY (2025-10-01..2025-12-31) [keep: ] quote: "营业收入 170,360,448,000.00 200,920,500,000.00 194,984,598,000.00 237,699,412,000.00"
  - p356 BYD total assets, end of 2025 = **883,729,883,000** CNY (2025-12-31..2025-12-31) [DISCARD: Total assets, not revenue.] quote: "总资产 883,729,883,000.00 783,355,855,000.00 12.83% 679,547,670,000.00"
- `https://202.62.215.11/www/tc/stocks/realtime/quote_ci_detail.php?code=1211&pyear=1&eyear=0` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.sgpjbg.com/info/fe561e01a85a6c1f4b0ad539b4dd2d68.html` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 12 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word 'million' not supported by quote or table header: 8; period year 2023 does not appear in the page text or URL (likely mis-dated): 1)

### d6 [forecasts_markets] Analyst consensus and broker previews

Hypothesis: Sell-side Q3 2026 revenue previews published before the cutoff can anchor the estimate, but they are forecasts rather than actuals and may share assumptions. They are most useful as a cross-check on the volume-times-ASP and segment-sum routes.

Queries issued by the searcher: 比亚迪 2026年三季报 前瞻 营业收入 预测; BYD Q3 2026 revenue forecast analyst; 比亚迪 2026Q3 业绩 预览 营收 券商 研报 三季度 销量; 比亚迪 2026年9月 销量 三季度 累计销量 万辆; 比亚迪 2026年三季报 前瞻 营业收入 预测; BYD Q3 2026 revenue forecast analyst; 比亚迪 2026Q3 业绩 预览 营收; 比亚迪 2026年三季度 销量 预测 券商 研报; 比亚迪 2026年三季报 前瞻 营业收入 预测; BYD Q3 2026 revenue forecast analyst; 比亚迪 2026Q3 业绩 预览 营收 券商 研报 2026年10月; 比亚迪 三季度 销量 2026年9月 销量 万辆 同比

- `https://wwwhk.aastocks.com/en/stocks/news/aafn-con/NOW.1549400/popular-news/AAFN` -> **live_dated** (page date 2026-10-15); points raw/verified 15/13
  - p357 Goldman Sachs forecast BYD 3Q26 revenue = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p358 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p359 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p360 Goldman Sachs forecast BYD 3Q26 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p361 Goldman Sachs forecast BYD 3Q26 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p362 Goldman Sachs forecast BYD 3Q26 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p363 Goldman Sachs assumed BYD 3Q26 sales volume growth YoY and QoQ = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p364 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p365 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p366 BYD Hungary plant planned annual capacity (production expected to start by end-2 = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Hungary plant capacity is not expected to produce until end-2026; no Q3 2026 revenue contribution.] quote: "Hungary plant is expected to commence production by the end of 2026 with planned annual capacity of 300,000 vehicles"
  - p367 China export VAT rebate rate for new energy vehicles before reduction = **13** % (..2027-03-31) [DISCARD: VAT rebate change affects 2027, not Q3 2026 revenue.] quote: "from April 1, 2027, the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p368 Goldman Sachs assumed cost pass-through of VAT rebate change = **67** % (not stated (page dated 2026-10-15)) [DISCARD: VAT rebate pass-through assumption for 2027, not Q3 2026 revenue.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
  - p369 Goldman Sachs estimated 2027 earnings reduction from VAT rebate change = **4** % (2027-01-01..2027-12-31) [DISCARD: Estimated 2027 earnings impact, not Q3 2026 revenue.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- `https://www.aastocks.com/tc/cnhk/quote/stock-news-content/002594/NOW.1549400/` -> **live_dated** (page date 2026-10-27); points raw/verified 15/9
  - p370 Goldman Sachs forecast: BYD Q3 2026 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "該行預測其第三季收入將達2,429.36億元人民幣(下同),按年增長25%且按季增長25%"
  - p371 Goldman Sachs forecast: BYD Q3 2026 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "按年增長25%且按季增長25%,淨利潤115億元"
  - p372 Goldman Sachs forecast: BYD Q3 2026 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "淨利潤115億元,按年上升47%並按季增長39%"
  - p373 Goldman Sachs forecast: BYD Q3 2026 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "按年上升47%並按季增長39%"
  - p374 Goldman Sachs forecast: BYD Q3 2026 sales volume YoY growth = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "主要受惠於銷量增長年及按季均升19%"
  - p375 Goldman Sachs forecast: BYD Q3 2026 sales volume QoQ growth = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "主要受惠於銷量增長年及按季均升19%"
  - p376 BYD domestic NEV retail market share, Q2 2026 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "其國內新能源車零售市佔率由第二季的22%提升至第三季的25%"
  - p377 BYD domestic NEV retail market share, Q3 2026 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "其國內新能源車零售市佔率由第二季的22%提升至第三季的25%"
  - p378 China NEV export VAT rebate rate, before 2027-04-01 = **13** % (..2027-03-31) [keep: ] quote: "自2027年4月1日起將新能源車出口增值稅退稅率由13%下調至9%"
- `https://4g.stockstar.com/detail/IG2026101500019815` -> **live_dated** (page date 2026-10-27); points raw/verified 14/12
  - p379 Goldman Sachs forecast: BYD Q3 2026 revenue = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "该行预测,比亚迪股份第三季收入将达2,429.36亿元人民币,年度同比增长25%且季度环比增长25%"
  - p380 Goldman Sachs forecast: BYD Q3 2026 revenue year-on-year growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "该行预测,比亚迪股份第三季收入将达2,429.36亿元人民币,年度同比增长25%且季度环比增长25%"
  - p381 Goldman Sachs forecast: BYD Q3 2026 revenue quarter-on-quarter growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "年度同比增长25%且季度环比增长25%;净利润115亿元人民币"
  - p382 Goldman Sachs forecast: BYD Q3 2026 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast, not revenue.] quote: "净利润115亿元人民币,年度同比上升47%并季度环比增长39%"
  - p383 Goldman Sachs forecast: BYD Q3 2026 net profit year-on-year growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "净利润115亿元人民币,年度同比上升47%并季度环比增长39%"
  - p384 Goldman Sachs forecast: BYD Q3 2026 net profit quarter-on-quarter growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "年度同比上升47%并季度环比增长39%,主要受惠于销量年度同比及季度环比均升19%"
  - p385 Goldman Sachs forecast: BYD Q3 2026 sales volume year-on-year growth = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "主要受惠于销量年度同比及季度环比均升19%"
  - p386 Goldman Sachs forecast: BYD Q3 2026 sales volume quarter-on-quarter growth = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "主要受惠于销量年度同比及季度环比均升19%,以及推出更多闪充车型带动平均售价上升"
  - p387 BYD domestic NEV retail market share in Q2 2026 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "其国内新能源车零售市占率由第二季的22%提升至第三季的25%"
  - p388 BYD domestic NEV retail market share in Q3 2026 (Goldman forecast) = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "其国内新能源车零售市占率由第二季的22%提升至第三季的25%"
  - p389 BYD Hungary plant planned capacity (production expected end-2026) = **300,000** vehicle (2026-12-31..2026-12-31) [DISCARD: Hungary plant capacity is not expected to produce until end-2026; no Q3 2026 revenue contribution.] quote: "比亚迪股份在匈牙利的厂房预计于2026年底投产,规划产能达30万辆"
  - p390 Goldman Sachs BYD H-share target price = **134** HKD (2026-10-15..2026-10-15) [DISCARD: Share target price, irrelevant to operating revenue.] quote: "H股目标价维持134港元"
- `https://hk.finance.yahoo.com/quote/81211.HK/analysis/` -> **dropped** (live http 503); points raw/verified -/-
- `https://beta.finance.yahoo.com/quote/0VSO.L/analysis/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://twelvedata.com/markets/289238/stock/hkex/1211/analysis` -> **live_dated** (page date 2026-01-01); points raw/verified 15/13
  - p391 Number of analysts contributing revenue estimates for current year (Dec 2026) = **18** analyst (2026-01-01..2026-12-31) [DISCARD: Stale twelvedata consensus from January 2026, not Q3 2026 revenue.] quote: "\| Number of Analysts \| 2 \| 18 \| 20 \|"
  - p392 Average revenue estimate for current year (Dec 2026), consensus = **888,920,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year 2026 average revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p393 Low revenue estimate for current year (Dec 2026) = **820,820,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year low revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| Low estimate \| 277.97B \| 820.82B \| 928.04B \|"
  - p394 High revenue estimate for current year (Dec 2026) = **955,480,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year high revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| High estimate \| 288.74B \| 955.48B \| 1.21T \|"
  - p395 Forecast sales growth for current year (Dec 2026) = **0.11** 1 (2026-01-01..2026-12-31) [DISCARD: Full-year sales growth forecast from stale January 2026 consensus, not Q3 revenue.] quote: "\| Sales growth \| 0.19 \| 0.11 \| 0.18 \|"
  - p396 Number of analysts contributing revenue estimates for next quarter (Dec 2026) = **2** analyst (2026-10-01..2026-12-31) [DISCARD: Analyst count for Q4 2026 revenue estimate, not Q3 2026.] quote: "\| Number of Analysts \| 2 \| 18 \| 20 \|"
  - p397 Average revenue estimate for next quarter (Dec 2026) = **283,350,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Q4 2026 average revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p398 Low revenue estimate for next quarter (Dec 2026) = **277,970,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Q4 2026 low revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| Low estimate \| 277.97B \| 820.82B \| 928.04B \|"
  - p399 High revenue estimate for next quarter (Dec 2026) = **288,740,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Q4 2026 high revenue estimate from stale January 2026 consensus, not Q3 2026.] quote: "\| High estimate \| 288.74B \| 955.48B \| 1.21T \|"
  - p400 Forecast sales growth for next quarter (Dec 2026) = **0.19** 1 (2026-10-01..2026-12-31) [DISCARD: Q4 2026 sales growth forecast, not Q3 revenue.] quote: "\| Sales growth \| 0.19 \| 0.11 \| 0.18 \|"
  - p401 Average revenue estimate for next year (Dec 2027) = **1,040,000,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 average revenue estimate, not Q3 2026.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p402 Low revenue estimate for next year (Dec 2027) = **928,040,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 low revenue estimate, not Q3 2026.] quote: "\| Low estimate \| 277.97B \| 820.82B \| 928.04B \|"
  - p403 High revenue estimate for next year (Dec 2027) = **1,210,000,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 high revenue estimate, not Q3 2026.] quote: "\| High estimate \| 288.74B \| 955.48B \| 1.21T \|"
- `https://www.boerse-express.com/news/articles/byd-aktie-schnell-meldung-953946` -> **live_dated** (page date 2026-10-17); points raw/verified 13/6
  - p404 Expected revenue growth rate for BYD Q3 2026 vs prior year = **10.2** as written "10,2 %", value check pending % (2026-07-01..2026-09-30) [DISCARD: Prior-year base of CNY 213.06bn conflicts with actual Q3 2025 revenue of CNY 194.98bn; scope/period mismatch.] quote: "Beim Umsatz werden 234,80 Milliarden CNY erwartet, rund 10,2 % mehr als die 213,06 Milliarden CNY ein Jahr zuvor."
  - p405 Analyst consensus average EPS estimate for BYD Q3 2026 = **1.3** as written "1,30", value check pending CNY per share (2026-07-01..2026-09-30) [DISCARD: EPS estimate, not revenue.] quote: "Analysten rechnen im Schnitt mit 1,30 CNY Gewinn je Aktie, nach 0,94 CNY im Vorjahreszeitraum."
  - p406 Analyst consensus full-year 2026 EPS estimate for BYD = **4.3** as written "4,30", value check pending CNY per share (2026-01-01..2026-12-31) [DISCARD: Full-year EPS estimate, not revenue.] quote: "Der Konsens von mehr als drei Dutzend Analysten sieht den Gewinn je Aktie bei 4,30 CNY, nach 3,88 CNY im Vorjahr."
  - p407 BYD September 2026 new-energy vehicle sales volume = **464** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "Im September verkaufte BYD 463.561 Fahrzeuge mit alternativen Antrieben."
  - p408 BYD January-September 2026 cumulative deliveries change vs prior year = **3.94** as written "3,94 %", value check pending % (2026-01-01..2026-09-30) [keep: ] quote: "Von Januar bis September summierten sich die Auslieferungen auf 3.131.576 Einheiten und lagen damit 3,94 % unter dem Vorjahreswert."
  - p409 Scheduled date of BYD Q3 2026 results publication = **29** day of month (2026-10-29..2026-10-29) [DISCARD: Publication date, not a revenue observation.] quote: "Am 29. Oktober veröffentlicht der chinesische Autobauer seine Zahlen für das dritte Quartal 2026."
- `https://www.moomooapp.com/hant/stock/002594-SZ/earnings?chain_id=uLRoVwQF80C13y.1ldij0s` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.moomoocn.com/hans/stock/01211-HK/earnings?chain_id=gkFIi1xh9StxVC.1l38ru9` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://hk.investing.com/news/stock-market-news/article-1700055` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.moomoocn.com/hans/stock/002594-SZ/earnings?chain_id=x7QlTdMSQ_JMi6.1l8heo1` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://trade.yuanta.com.hk/Portal/cn/Article/Index/3e97266d-e574-40da-be5c-a4f07d9a179a` -> **live_dated** (page date 2026-10-26); points raw/verified 15/14
  - p410 Goldman Sachs preview: BYD Q3 2026 sales volume growth year-on-year = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "蔚来(09866.HK)、比亚迪(01211.HK)按年分别升26%及19%,受惠於具竞争力的新车型交付"
  - p411 Goldman Sachs forecast: BYD Q3 2026 gross margin (forecast) = **19.8** % (2026-07-01..2026-09-30) [DISCARD: Gross margin forecast, not revenue.] quote: "该行预期比亚迪第三季毛利率按年改善2.2个百分点至19.8%"
  - p412 Goldman Sachs forecast: BYD Q3 2026 gross margin year-on-year improvement (perce = **2.2** percentage points (2026-07-01..2026-09-30) [DISCARD: Gross margin forecast change, not revenue.] quote: "该行预期比亚迪第三季毛利率按年改善2.2个百分点至19.8%"
  - p413 Goldman Sachs forecast: BYD Q3 2026 EBIT year-on-year growth (forecast) = **134** % (2026-07-01..2026-09-30) [DISCARD: EBIT forecast growth, not revenue.] quote: "息税前利润及净利按年分别升134%及47%,评级为「买入」(确信名单)"
  - p414 Goldman Sachs forecast: BYD Q3 2026 net profit year-on-year growth (forecast) = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit forecast growth, not revenue.] quote: "息税前利润及净利按年分别升134%及47%,评级为「买入」(确信名单)"
  - p415 Goldman Sachs: China September 2026 NEV retail sales year-on-year change = **16** % (2026-09-01..2026-09-30) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "9月新能源车零售按年跌16%,对比7月及8月分别按年跌3%及跌10%"
  - p416 Goldman Sachs: China July 2026 NEV retail sales year-on-year change = **3** % (2026-07-01..2026-07-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "9月新能源车零售按年跌16%,对比7月及8月分别按年跌3%及跌10%"
  - p417 Goldman Sachs: China August 2026 NEV retail sales year-on-year change = **10** % (2026-08-01..2026-08-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "9月新能源车零售按年跌16%,对比7月及8月分别按年跌3%及跌10%"
  - p418 Goldman Sachs forecast: China 2026 passenger car retail sales year-on-year chang = **20** % (2026-01-01..2026-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "现预期2026年及2027年乘用车零售按年分别跌20%及升2%"
  - p419 Goldman Sachs forecast: China 2027 passenger car retail sales year-on-year chang = **2** % (2027-01-01..2027-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "现预期2026年及2027年乘用车零售按年分别跌20%及升2%"
  - p420 Goldman Sachs forecast: China 2026 passenger car exports year-on-year growth (fo = **70** % (2026-01-01..2026-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "出口按年分别升70%及升10%,批发销量按年分别跌1%及升5%"
  - p421 Goldman Sachs forecast: China 2027 passenger car exports year-on-year growth (fo = **10** % (2027-01-01..2027-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "出口按年分别升70%及升10%,批发销量按年分别跌1%及升5%"
  - p422 Goldman Sachs forecast: China 2026 passenger car wholesale sales year-on-year ch = **1** % (2026-01-01..2026-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "批发销量按年分别跌1%及升5%"
  - p423 Goldman Sachs forecast: China 2027 passenger car wholesale sales year-on-year gr = **5** % (2027-01-01..2027-12-31) [DISCARD: China market forecast, not BYD Q3 revenue.] quote: "批发销量按年分别跌1%及升5%"
- dropped by code checks: 20 (period year 2030 does not appear in the page text or URL (likely mis-dated): 4; period_end missing or unparseable: 3; number: value_as_written is only part of a larger CJK number in the quote: 4; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; scale word 'billion' not supported by quote or table header: 4; number: ambiguous separators: '.' used as a thousands separator: 1)

### d7 [related_series] China NEV market and BYD share

Hypothesis: China NEV wholesale/retail totals times BYD's market share provide an independent cross-check on Q3 2026 BYD volume if company monthly announcements are incomplete or revised. The bridge is BYD's share of the relevant China NEV passenger-vehicle market.

Queries issued by the searcher: 乘联会 2026年9月 新能源 乘用车 批发 销量 比亚迪 份额; BYD Q3 2026 revenue third quarterly report 营业收入; 乘联会 2026年8月 新能源乘用车 批发 销量 比亚迪 市场份额; 乘联会 2026年7月 新能源乘用车 批发 销量 比亚迪 份额; 乘联会 2026年9月 新能源乘用车 批发销量 比亚迪 份额; China NEV wholesale July August September 2026 BYD share CPCA; 乘联会 2026年7月 新能源乘用车 批发 比亚迪 销量 份额 8月; BYD July 2026 sales 新能源 销量 公告 7月 比亚迪 402000; 乘联会 2026年9月 新能源乘用车 批发销量 比亚迪 份额; China NEV wholesale July August September 2026 BYD share CPCA; 比亚迪 2026年7月 新能源乘用车 批发销量 乘联会 份额; 比亚迪 2026年第三季度报告 营业收入 前三季度

- `https://static.cdsb.com/micropub/Articles/202610/7dd5a9602755775c86ef10036ec0d6b5.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.ofweek.com/auto/2026-10/ART-70111-8420-30706755.html` -> **live_dated** (page date 2026-10-13); points raw/verified 15/15
  - p424 BYD September 2026 total sales growth (YoY, wholesale) = **17** % (2026-09-01..2026-09-30) [keep: ] quote: "比亚迪总量 +17%,扣掉海外,国内是 13%。"
  - p425 BYD September 2026 domestic sales growth after excluding overseas (YoY, derived) = **13** % (2026-09-01..2026-09-30) [keep: ] quote: "比亚迪总量 +17%,扣掉海外,国内是 13%。"
  - p426 BYD September 2026 overseas sales volume = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "比亚迪 9 月海外 18.07 万辆,同比 +153.9%,比去年同期多了 10.95 万辆,是所有车企里增量最大的。"
  - p427 BYD September 2026 overseas sales growth (YoY) = **154** % (2026-09-01..2026-09-30) [DISCARD: Export growth duplicate, not needed for level estimate.] quote: "比亚迪 9 月海外 18.07 万辆,同比 +153.9%,比去年同期多了 10.95 万辆,是所有车企里增量最大的。"
  - p428 BYD September 2026 overseas sales increase vs prior year = **109,500** vehicle (2026-09-01..2026-09-30) [DISCARD: Export increase duplicate, not needed for level estimate.] quote: "比亚迪 9 月海外 18.07 万辆,同比 +153.9%,比去年同期多了 10.95 万辆,是所有车企里增量最大的。"
  - p429 BYD January-September 2026 cumulative overseas sales = **1,338,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "比亚迪:133.8 万辆,已超过 2025 年全年的 105.4 万辆,占 42.7%"
  - p430 BYD overseas share of group sales, January-September 2026 = **42.7** % (2026-01-01..2026-09-30) [keep: ] quote: "比亚迪:133.8 万辆,已超过 2025 年全年的 105.4 万辆,占 42.7%"
  - p431 BYD September 2026 domestic NEV passenger-vehicle retail volume (CPCA) = **246,800** vehicle (2026-09-01..2026-09-30) [DISCARD: Industry retail ranking, not BYD Q3 revenue.] quote: "比亚迪 24.68 万辆,第二名吉利 11.97 万辆,第三名零跑 7.82 万辆。"
  - p432 BYD September 2026 NEV passenger-vehicle export volume (CPCA) = **175,900** vehicle (2026-09-01..2026-09-30) [DISCARD: Industry export ranking, not BYD Q3 revenue.] quote: "9 月新能源乘用车出口比亚迪 17.59 万辆、奇瑞 8.60 万辆、吉利 7.29 万辆,比亚迪一家比后两家加起来还多。"
  - p433 China September 2026 NEV domestic sales volume (CAAM) = **1,252,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV industry aggregate, not target.] quote: "9 月新能源国内销量 125.2 万辆,同比 9.4%。"
  - p434 China September 2026 NEV domestic sales share of total domestic sales = **65.8** % (2026-09-01..2026-09-30) [DISCARD: China NEV industry share, not target.] quote: "新能源这边,中汽协的标题是「新能源汽车国内销量占比逐月提升」,9 月到了 65.8%,创新高。"
  - p435 China September 2026 total vehicle sales volume (CAAM) = **2,956,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China total vehicle sales, not target.] quote: "9 月卖了 295.6 万辆,环比涨 9%,同比跌 8.4%;前三季度所有汽车产量 2327.1 万辆,同比 4.5%。"
  - p436 China September 2026 vehicle export volume (CAAM) = **1,053,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China vehicle exports, not target.] quote: "出口 105.3 万辆,同比 +61.4%,连续第 4 个月站在百万辆以上。"
  - p437 China January-September 2026 cumulative vehicle export volume (CAAM) = **8,205,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China cumulative vehicle exports, not target.] quote: "9 月 105.3 万辆,环比还涨了 4.2%;前三季度 820.5 万辆,已经比 2025 年全年的 709.8 万辆多出 110.7 万辆。"
  - p438 China September 2026 NEV share of vehicle exports = **54.2** % (2026-09-01..2026-09-30) [DISCARD: China NEV export share, not target.] quote: "新能源占 54.2%,连续第 4 个月超过一半。"
- `https://www.news18a.com/news/storys_305240.html` -> **live_dated** (page date 2026-10-15); points raw/verified 15/15
  - p439 BYD September wholesale sales (狭义乘用车厂商批售), vehicles = **455,113** vehicle (2026-09-01..2026-09-30) [DISCARD: Narrow passenger wholesale ranking, not consolidated BYD revenue.] quote: "比亚迪汽车以455,113辆的成绩位居狭义乘用车厂商批售榜首,市场份额达17.9%"
  - p440 BYD September wholesale market share of narrow passenger vehicle wholesale = **17.9** % (2026-09-01..2026-09-30) [DISCARD: Wholesale share ranking, not consolidated revenue.] quote: "市场份额达17.9%,领先第二名吉利汽车(290,100辆)16.5万辆"
  - p441 Geely September wholesale sales, vehicles = **290,100** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "领先第二名吉利汽车(290,100辆)16.5万辆,奇瑞汽车以281,738辆排名第三"
  - p442 Chery September wholesale sales, vehicles = **281,738** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "奇瑞汽车以281,738辆排名第三"
  - p443 Changan September wholesale sales, vehicles = **127,993** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "长安汽车127,993辆排第四"
  - p444 SAIC Passenger Vehicle September wholesale sales, vehicles = **107,303** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "上汽乘用车107,303辆第五"
  - p445 Great Wall September wholesale sales, vehicles = **99,914** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "长城汽车99,914辆第七"
  - p446 Leapmotor September wholesale sales, vehicles = **96,167** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "零跑汽车96,167辆第八"
  - p447 SAIC-GM-Wuling September wholesale sales, vehicles = **103,477** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "上汽通用五菱103,477辆"
  - p448 Tesla China September wholesale sales, vehicles = **95,366** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "特斯拉中国95,366辆"
  - p449 FAW-Volkswagen September wholesale sales, vehicles = **77,728** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker wholesale volume, not target.] quote: "一汽大众77,728辆"
  - p450 BYD January-September cumulative wholesale sales, vehicles = **3,076,000** vehicle (2026-01-01..2026-09-30) [DISCARD: Narrow passenger cumulative volume, different scope and duplicate.] quote: "1-9月比亚迪批售307.6万辆领跑"
  - p451 BYD September export volume, vehicles = **174,277** vehicle (2026-09-01..2026-09-30) [DISCARD: Passenger export scope differs from BYD total NEV export; duplicate and not needed.] quote: "比亚迪174,277辆紧随其后且同比暴增151.6%"
  - p452 China narrow passenger vehicle September retail sales, vehicles = **1,618,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China retail aggregate, not target.] quote: "9月国内狭义乘用车零售161.8万辆,同比下降28.0%,环比增长5.0%"
  - p453 China NEV retail penetration rate in September (NEV share of passenger vehicle r = **67** % (2026-09-01..2026-09-30) [DISCARD: China NEV penetration, not target.] quote: "9月新能源零售渗透率攀升至67.0%,创历史新高"
- `https://www.cei.cn//defaultsite/s/article/2026/10/12/4b4ff607-9d914745-01a1-2dc780e1-6770_2026.html?referCode=sxf0a&columnId=4028c7ca-39905444-0139-90` -> **live_dated** (page date 2026-10-12); points raw/verified 10/10
  - p454 China NEV passenger-vehicle wholesale volume, September 2026 (CPCA estimate) = **1,670,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale estimate, not target.] quote: "9月全国新能源乘用车厂商批发销量预估达167万辆,同比增长12%,环比增长11%,实现双位数双增。"
  - p455 China NEV passenger-vehicle wholesale volume year-on-year growth, September 2026 = **12** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "9月全国新能源乘用车厂商批发销量预估达167万辆,同比增长12%,环比增长11%"
  - p456 China NEV passenger-vehicle wholesale volume month-on-month growth, September 20 = **11** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "9月全国新能源乘用车厂商批发销量预估达167万辆,同比增长12%,环比增长11%"
  - p457 BYD NEV passenger-vehicle wholesale volume, September 2026 = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD NEV wholesale duplicate, not needed.] quote: "比亚迪汽车以456,713辆断层式领先"
  - p458 Geely NEV passenger-vehicle wholesale volume, September 2026 = **188,800** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "第二名吉利(188,800辆)"
  - p459 Chery NEV passenger-vehicle wholesale volume, September 2026 = **127,486** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "第三名奇瑞(127,486辆)"
  - p460 Leapmotor NEV passenger-vehicle wholesale volume, September 2026 = **105,656** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "第四名零跑(105,656辆)"
  - p461 Combined wholesale volume of Geely, Chery and Leapmotor, September 2026 = **421,942** vehicle (2026-09-01..2026-09-30) [DISCARD: Combined other automaker volume, not target.] quote: "三家合计421,942辆,仍比比亚迪少3.4万余辆"
  - p462 BYD wholesale lead over Geely+Chery+Leapmotor combined, September 2026 = **34,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Wholesale lead calculation, not target.] quote: "三家合计421,942辆,仍比比亚迪少3.4万余辆"
  - p463 Changan NEV passenger-vehicle wholesale volume, September 2026 (truncated in doc = **103** as written "102,9", value check pending vehicle (2026-09-01..2026-09-30) [DISCARD: Truncated other automaker value, unusable.] quote: "长安汽车102,9"
- `https://www.globalchinaev.com/post/chinas-september-nev-retail-climbs-14-as-shipments-outrun-it-by-531000` -> **live_dated** (page date 2026-10-11); points raw/verified 15/15
  - p464 China NEV passenger vehicle retail sales, September 2026 (CPCA preliminary) = **1,141,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV retail aggregate, not target.] quote: "China's retail sales of passenger new energy vehicles (NEVs) reached 1.141 million in September 2026, up 14% from August"
  - p465 China NEV passenger vehicle wholesale shipments, September 2026 (CPCA preliminar = **1,672,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale aggregate, not target.] quote: "Shipments from automakers to dealers and overseas markets grew to 1.672 million units over the same period"
  - p466 China NEV retail sales, August 2026 (CPCA) = **1,005,000** vehicle (2026-08-01..2026-08-31) [DISCARD: China NEV retail aggregate, not target.] quote: "In August, NEV retail came to 1.005 million against wholesale shipments of 1.510 million"
  - p467 China NEV wholesale shipments, August 2026 (CPCA) = **1,510,000** vehicle (2026-08-01..2026-08-31) [DISCARD: China NEV wholesale aggregate, not target.] quote: "In August, NEV retail came to 1.005 million against wholesale shipments of 1.510 million, a difference of about 505,000"
  - p468 China NEV exports, August 2026 = **518,000** vehicle (2026-08-01..2026-08-31) [DISCARD: China NEV export aggregate, not target.] quote: "NEV exports that month were 518,000, up 154.7% year over year"
  - p469 China NEV retail sales, January-September 2026 cumulative = **7,816,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China cumulative NEV retail, not target.] quote: "NEV retail sales totaled 7.816 million in the first nine months, down 12% year over year"
  - p470 China NEV wholesale shipments, January-September 2026 cumulative = **11,450,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China cumulative NEV wholesale, not target.] quote: "while wholesale shipments rose 9% to 11.45 million"
  - p471 China NEV exports, January-August 2026 cumulative = **3,329,000** vehicle (2026-01-01..2026-08-31) [DISCARD: China cumulative NEV exports, not target.] quote: "That 3.63 million-unit difference compares with 3.329 million NEV exports in January through August alone, up 135.1% on the same period of 2025."
  - p472 BYD passenger car sales, September 2026 = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: September passenger sales duplicate of p77/p125, not needed.] quote: "BYD (HKG: 1211) sold 456,713 passenger cars in September, up from 432,684 NEVs shipped in August"
  - p473 BYD NEV shipments, August 2026 = **432,684** vehicle (2026-08-01..2026-08-31) [DISCARD: August NEV shipments duplicate/context, not needed.] quote: "up from 432,684 NEVs shipped in August"
  - p474 BYD passenger cars and pickups exported, September 2026 = **179,877** vehicle (2026-09-01..2026-09-30) [DISCARD: Export duplicate of p725, not needed.] quote: "said 179,877 passenger cars and pickups went overseas, up 153.9% year over year"
  - p475 BYD domestic NEV retail, August 2026 = **233,943** vehicle (2026-08-01..2026-08-31) [DISCARD: Domestic retail, not consolidated revenue.] quote: "In August, BYD's domestic NEV retail was 233,943 units, about 54% of what it shipped that month."
  - p476 BYD share of its own August 2026 NEV shipments taken by domestic retail (numerat = **54** % (2026-08-01..2026-08-31) [DISCARD: Domestic retail share, not consolidated revenue.] quote: "BYD's domestic NEV retail was 233,943 units, about 54% of what it shipped that month"
  - p477 BYD NEV exports, August 2026 (CPCA top exporter ranking) = **184,446** vehicle (2026-08-01..2026-08-31) [DISCARD: Export duplicate, not needed.] quote: "CPCA ranked it China's top NEV exporter in August with 184,446 units, well ahead of Geely and Chery."
  - p478 China NEV share of total passenger car retail sales, September 2026 (numerator:  = **67.1** % (2026-09-01..2026-09-30) [DISCARD: China NEV penetration, not target.] quote: "NEVs took 67.1% of retail sales, up from 65.2% in August."
- `https://theelectricviking.com/byd-maintains-lead-chinas-nev-market-tesla-climbs-fourth-september/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.marchdair.com/169849/%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA-%D8%A7%D9%84%D8%AC%D9%85%D9%84%D8%A9-%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-` -> **live_dated** (page date 2026-09-06); points raw/verified 15/12
  - p479 China NEV wholesale year-on-year growth rate, August 2026 = **16** % (2026-08-01..2026-08-31) [DISCARD: China NEV wholesale growth, not target.] quote: "محققة نمواً سنويّاً بنسبة 16% مقارنة بنفس الشهر من عام 2025"
  - p480 China NEV wholesale month-on-month growth rate, August 2026 vs July 2026 = **4** % (2026-08-01..2026-08-31) [DISCARD: China NEV wholesale growth, not target.] quote: "وزيادة شهريّة بنسبة 4% عن شهر يوليو الماضي"
  - p481 BYD Group wholesale volume, August 2026 (CPCA top-5 list) = **433,384** vehicle (2026-08-01..2026-08-31) [DISCARD: August BYD wholesale duplicate, not needed.] quote: "مجموعة BYD: واصلت التحليق منفردة في الصدارة بإجمالي 433,384 سيارة."
  - p482 Geely Group wholesale volume, August 2026 (CPCA top-5 list) = **173,675** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "مجموعة جيلي (Geely): جاءت في المركز الثاني بإجمالي 173,675 سيارة."
  - p483 Chery Group wholesale volume, August 2026 (CPCA top-5 list) = **115,558** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "مجموعة شيري (Chery): حققت المركز الثالث بـ 115,558 سيارة."
  - p484 Leapmotor wholesale volume, August 2026 (CPCA top-5 list) = **103,129** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "ليب موتور (Leapmotor): واصلت قفزاتها الاستثنائية لتسجل 103,129 سيارة"
  - p485 Tesla China wholesale volume (domestic plus export), August 2026 = **86,166** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "تيسلا الصين (Tesla China): احتلت المركز الخامس بإجمالي 86,166 سيارة (شاملة المبيعات المحلية والتصدير)."
  - p486 Xiaomi Auto monthly deliveries, August 2026 (stated as above threshold) = **30,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "شاومي أوتو (Xiaomi Auto): حافظت على معدل تسليمات مستقر يتجاوز 30,000 سيارة شهرياً."
  - p487 Xpeng wholesale volume, August 2026 = **39,107** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "سجلت كل من إكسبنج (Xpeng) نحو 39,107 وحدة"
  - p488 Li Auto wholesale volume, August 2026 = **37,679** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "ولي أوتو (Li Auto) نحو 37,679 وحدة"
  - p489 Nio wholesale volume, August 2026 = **35,836** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "ونيو (Nio) نحو 35,836 وحدة"
  - p490 SAIC-GM NEV volume, August 2026 = **12,654** vehicle (2026-08-01..2026-08-31) [DISCARD: Other automaker volume, not target.] quote: "حيث سجلت SAIC-GM نحو 12,654 وحدة"
- `http://www.icbattery.com/news/show-htm-itemid-65833.html` -> **live_dated** (page date 2026-10-12); points raw/verified 15/0
- `https://greenshift.earth/electric-vehicles/china-nev/china-sept-2026-nev-wholesale-estimated-at-2026-high-cnevpost` -> **live_dated** (page date 2026-10-12); points raw/verified 15/14
  - p491 China passenger NEV wholesale sales, September 2026, year-on-year growth = **12** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "September NEV wholesale sales rose 12% year-on-year and 11% from August."
  - p492 China passenger NEV wholesale sales, September 2026, month-on-month growth = **11** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "September NEV wholesale sales rose 12% year-on-year and 11% from August."
  - p493 China passenger NEV wholesale sales, cumulative January-September 2026 = **11,420,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China cumulative NEV wholesale, not target.] quote: "China's passenger NEV wholesale sales totaled about 11.42 million in the first 9 months of the year, up about 10% year-on-year."
  - p494 China passenger NEV wholesale sales, cumulative January-September 2026, year-on- = **10** % (2026-01-01..2026-09-30) [DISCARD: China cumulative NEV wholesale growth, not target.] quote: "China's passenger NEV wholesale sales totaled about 11.42 million in the first 9 months of the year, up about 10% year-on-year."
  - p495 China passenger NEV retail sales, September 1-27 2026, year-on-year change = **20** % (2026-09-01..2026-09-27) [DISCARD: China NEV retail partial period, not target.] quote: "China's passenger NEV retail sales fell 20% year-on-year to 827,000 from September 1 to 27."
  - p496 China passenger NEV retail sales, September 1-27 2026 = **827,000** vehicle (2026-09-01..2026-09-27) [DISCARD: China NEV retail partial period, not target.] quote: "China's passenger NEV retail sales fell 20% year-on-year to 827,000 from September 1 to 27."
  - p497 BYD passenger NEV wholesale sales, September 2026 = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD NEV wholesale duplicate, not needed.] quote: "\| 1 \| BYD \| 456,713 \|"
  - p498 Geely passenger NEV wholesale sales, September 2026 = **188,800** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "\| 2 \| Geely \| 188,800 \|"
  - p499 Chery passenger NEV wholesale sales, September 2026 = **127,486** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "\| 3 \| Chery \| 127,486 \|"
  - p500 Leapmotor passenger NEV wholesale sales, September 2026 = **105,656** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "\| 4 \| Leapmotor \| 105,656 \|"
  - p501 Changan passenger NEV wholesale sales, September 2026 = **102,968** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "\| 5 \| Changan \| 102,968 \|"
  - p502 Tesla China passenger NEV wholesale sales, September 2026 = **95,366** vehicle (2026-09-01..2026-09-30) [DISCARD: Other automaker NEV wholesale, not target.] quote: "\| 6 \| Tesla China \| 95,366 \|"
  - p503 Combined September 2026 wholesale sales of manufacturers with August NEV wholesa = **1,550,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Combined other manufacturer volume, not target.] quote: "Preliminary figures put those manufacturers' combined September sales at about 1.55 million."
  - p504 Share of August 2026 passenger NEV wholesale total accounted for by manufacturer = **93** % (2026-08-01..2026-08-31) [DISCARD: China NEV wholesale coverage share, not target.] quote: "Companies with NEV wholesale sales exceeding 10,000 in August accounted for a combined 93% of that month's passenger NEV wholesale total."
- `https://finance.eastmoney.com/a/202610103891835188.html` -> **dropped** (live http 404); points raw/verified -/-
- `https://tech.ifeng.com/c/8x5ZhdkSHtj` -> **live_dated** (page date 2026-10-09); points raw/verified 4/4
  - p505 China NEV passenger-vehicle wholesale volume, September 2026 (CPCA estimate) = **1,670,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale estimate, not target.] quote: "2026 年 9 月,全国新能源乘用车厂商批发销量预估达到 167 万辆,同比增长 12%,环比增长 11%"
  - p506 China NEV passenger-vehicle wholesale volume, September 2026, year-on-year growt = **12** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "2026 年 9 月,全国新能源乘用车厂商批发销量预估达到 167 万辆,同比增长 12%,环比增长 11%"
  - p507 China NEV passenger-vehicle wholesale volume, September 2026, month-on-month gro = **11** % (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale growth, not target.] quote: "2026 年 9 月,全国新能源乘用车厂商批发销量预估达到 167 万辆,同比增长 12%,环比增长 11%"
  - p508 China NEV passenger-vehicle wholesale volume, September 2026 (CPCA preliminary m = **1,670,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale estimate duplicate, not target.] quote: "2026 年 9 月全国乘用车厂商新能源批发预估 167 万辆,同比增长 12%,环比增长 11%"
- `https://m.iautocloud.com.cn/news/detail.html?id=20790` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 19 (scale word 'million' not supported by quote or table header: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period year 2026 does not appear in the page text or URL (likely mis-dated): 14; period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b1 [related_series] BYD Electronic Q3 2026 actual

Hypothesis: A reliable Q3 2026 BYD Electronic revenue or 2026 9M cumulative would replace the a4 seasonality assumption and materially reduce uncertainty in the non-auto component of m1.

Queries issued by the searcher: 比亚迪电子 2026年第三季度 营业额; 比亚迪电子 2026年首三季 业绩; 比亚迪电子 2025年第三季度 营业额 同比增长 前三季度 业绩; 比亚迪电子 2026年第一季度 营业额 381 亿元 同比; 比亚迪电子 2026年第三季度 营业额; 比亚迪电子 2026年首三季 业绩; 比亚迪电子 2026 第三季度 收入 预测 大摩 目标价 33元 报告; BYD Electronic third quarter 2026 revenue forecast analysts; 比亚迪电子 2026年第三季度 营业额; 比亚迪电子 2026年首三季 业绩; 比亚迪电子 2025年首三季 营业额 净利润 同比增长 第三季度; 比亞迪電子 2026年第三季 收入 預測 大摩 花旗 人民幣 億元

- `https://www.etnet.com.hk/www/tc/warrants/realtime/quote_news_detail.php?newsid=ETN360829306&page=1&code=62988` -> **live_dated** (page date 2026-10-27); points raw/verified 0/0
- `https://il.investing.com/equities/byd-electronic-earnings` -> **dropped** (live http 403); points raw/verified -/-
- `https://basic.10jqka.com.cn/00285/` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.163.com/dy/article/L681KAN805198UNI.html` -> **live_dated** (page date 2026-09-07); points raw/verified 7/7
  - p509 BYD Electronic H1 2026 revenue (first half, cumulative) = **82,234,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "今年上半年,比亚迪电子实现收入822.34亿元,同比微增2.02%"
  - p510 BYD Electronic H1 2026 revenue year-on-year growth rate = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "同比微增2.02%"
  - p511 BYD Electronic H1 2026 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit, not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p512 BYD Electronic H1 2026 net profit attributable to parent year-on-year change = **75.35** % (2026-01-01..2026-06-30) [DISCARD: Net profit change, not revenue.] quote: "同比下降75.35%"
  - p513 BYD Electronic (00285) share price intraday gain at time of writing = **6.76** % (not stated (page dated 2026-09-07)) [DISCARD: Share price movement, irrelevant.] quote: "比亚迪电子(00285)涨超7%,截至发稿,涨6.76%"
  - p514 BYD Electronic (00285) share price at time of writing = **26.86** HKD (not stated (page dated 2026-09-07)) [DISCARD: Share price, irrelevant.] quote: "报26.86港元"
  - p515 BYD Electronic (00285) turnover at time of writing = **410,000,000** HKD (not stated (page dated 2026-09-07)) [DISCARD: Turnover, irrelevant.] quote: "成交额4.1亿港元"
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/00285/NOW.1542369/hk-stock-news` -> **live_dated** (page date 2026-09-01); points raw/verified 6/6
  - p516 Citi target price for BYD Electronic (00285.HK), raised from prior target = **28** HKD per share (not stated (page dated 2026-09-01)) [DISCARD: Broker target price, irrelevant to revenue.] quote: "该行将公司目标价由22.6元上调至28元"
  - p517 Citi prior target price for BYD Electronic (00285.HK) before upgrade = **22.6** HKD per share (not stated (page dated 2026-09-01)) [DISCARD: Broker target price, irrelevant to revenue.] quote: "该行将公司目标价由22.6元上调至28元"
  - p518 BYD Electronic share price change on the quote line (HKD) = **-0.6** HKD per share (not stated (page dated 2026-09-01)) [DISCARD: Share price change, irrelevant.] quote: "比亚迪电子(00285.HK) -0.600 (-2.657%)"
  - p519 BYD Electronic share price change on the quote line (percent) = **-2.657** % (not stated (page dated 2026-09-01)) [DISCARD: Share price change, irrelevant.] quote: "比亚迪电子(00285.HK) -0.600 (-2.657%)"
  - p520 BYD Electronic short-selling turnover (沽空) as of 2026-10-27 16:25 = **73,600,000** HKD (2026-10-27..2026-10-27) [DISCARD: Short-selling turnover, irrelevant.] quote: "沽空 $7.36千万; 比率 49.426%"
  - p521 BYD Electronic short-selling ratio (沽空比率) as of 2026-10-27 16:25 = **49.43** % (2026-10-27..2026-10-27) [DISCARD: Short-selling ratio, irrelevant.] quote: "沽空 $7.36千万; 比率 49.426%"
- `https://www.moomooapp.com/hans/stock/00285-HK/financials-key-indicators` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/285/hk6/now.1480270/hk-stock-news` -> **live_dated** (page date 2025-10-30); points raw/verified 5/5
  - p522 BYD Electronic first three quarters (9M) revenue, cumulative, CNY = **123,285,000,000** CNY (2026-01-01..2026-09-30) [keep: ] quote: "公布截至今年9月底止首三季业绩,营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p523 BYD Electronic first three quarters (9M) revenue year-on-year change = **0.9** % (2026-01-01..2026-09-30) [DISCARD: BYD Electronic 9M revenue growth duplicate of p311/p522 context, not needed.] quote: "营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p524 BYD Electronic first three quarters (9M) net profit, cumulative, CNY = **3,137,000,000** CNY (2026-01-01..2026-09-30) [DISCARD: Net profit, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p525 BYD Electronic first three quarters (9M) net profit year-on-year change = **2.4** % (2026-01-01..2026-09-30) [DISCARD: Net profit growth, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p526 BYD Electronic first three quarters (9M) earnings per share, CNY = **1.39** CNY per share (2026-01-01..2026-09-30) [DISCARD: EPS, not revenue.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
- `https://stock.finance.sina.com.cn/hkstock/view/hk_report.php?reportid=815492069222` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://cn.investing.com/news/stock-market-news/article-3057943` -> **dropped** (live http 403); points raw/verified -/-
- `https://id.investing.com/equities/byd-electronic-earnings` -> **dropped** (live http 403); points raw/verified -/-
- `http://hk.stockstar.com/IG2026090100015216.shtml` -> **live_dated** (page date 2026-09-01); points raw/verified 14/14
  - p527 BYD Electronic 2026H1 total revenue = **82,234,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "比亚迪电子(00285.HK)2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p528 BYD Electronic 2026H1 smart terminal business revenue = **67,348,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic segment revenue, not consolidated Q3 revenue.] quote: "2026H1智能终端业务收入673.48亿元,同比增长约1.4%"
  - p529 BYD Electronic 2026H1 assembly business revenue = **55,522,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic sub-segment revenue, not consolidated Q3 revenue.] quote: "其中组装业务收入555.22亿元,同比增长约5.1%"
  - p530 BYD Electronic 2026H1 component business revenue = **11,826,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic sub-segment revenue, not consolidated Q3 revenue.] quote: "零部件业务收入118.26亿元,同比下降约13.3%"
  - p531 BYD Electronic 2026H1 new energy vehicle business revenue = **13,515,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic sub-segment revenue, not consolidated Q3 revenue.] quote: "2026H1新能源汽车业务收入135.15亿元,同比增长6.4%"
  - p532 BYD Electronic 2026H1 AI computing infrastructure revenue = **751,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: BYD Electronic sub-segment revenue, not consolidated Q3 revenue.] quote: "AI算力基础设施方面,2026H1实现收入7.51亿元,同比下降9.74%"
  - p533 BYD Electronic 2026H1 gross margin = **4.91** % (2026-01-01..2026-06-30) [DISCARD: BYD Electronic gross margin, not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p534 BYD Electronic 2026H1 gross margin year-on-year change (percentage points) = **1.97** percentage points (2026-01-01..2026-06-30) [DISCARD: BYD Electronic gross margin change, not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p535 BYD Electronic 2026H1 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit, not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p536 CSC forecast BYD Electronic 2026 full-year revenue = **181,086,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: BYD Electronic annual forecast, not Q3 actual.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p537 CSC forecast BYD Electronic 2027 full-year revenue = **199,602,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: BYD Electronic 2027 forecast, not Q3 actual.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p538 CSC forecast BYD Electronic 2026 full-year revenue growth = **0.9** % (2026-01-01..2026-12-31) [DISCARD: BYD Electronic forecast growth, not Q3 actual.] quote: "同比增长0.90%和10.23%"
  - p539 CSC forecast BYD Electronic 2027 full-year revenue growth = **10.23** % (2027-01-01..2027-12-31) [DISCARD: BYD Electronic 2027 forecast growth, not Q3 actual.] quote: "同比增长0.90%和10.23%"
  - p540 CSC forecast BYD Electronic 2026 full-year server business revenue (at least) = **3,000,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Server business forecast, not target.] quote: "服务器业务全年收入预计达30亿元以上"
- `https://113.28.163.186/sc/stocks/analysis/stock-aafn/00285/0/hk-stock-news/1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b2 [base_rates] Q3 2026 BYD automotive ASP / auto revenue

Hypothesis: A broker preview or company disclosure of Q3 2026 automotive revenue or ASP would resolve the gap between volume-times-ASP (~CNY 222bn) and Goldman's CNY 242.9bn total forecast.

Queries issued by the searcher: 比亚迪 2026年第三季度 营收 单车ASP 研报; BYD Q3 2026 revenue forecast auto revenue ASP export mix; 比亚迪 2026Q3 汽车业务收入 单车均价 出口 业绩前瞻 券商; 比亚迪 2025年第三季度 营业收入 1944亿 汽车业务收入 单车ASP; 比亚迪 2026年第三季度 营业收入 季报; BYD Q3 2026 revenue third quarter results; 比亚迪 2026年9月 销量 出口 数据 公告; 比亚迪 2026Q3 单车均价 ASP 出口占比 研报; 比亚迪 2026年第三季度 营业收入 单车ASP 汽车业务收入; BYD Q3 2026 revenue forecast auto ASP export mix analyst; 比亚迪 2026Q3 单车ASP 12.3万 汽车业务收入 高盛 拆解; 比亚迪 2026年三季报 前瞻 营业收入 预测 券商 3Q26 汽车业务

- `https://q.stock.sohu.com/cn/news.html?textId=1069476232&tab=120&type=120&code=cn_002594&date=2026/1019` -> **live_dated** (page date 2026-05-23); points raw/verified 0/0
- `https://wwwhk.aastocks.com/en/stocks/news/aafn-con/NOW.1549400/popular-news/AAFN` -> **live_dated** (page date 2026-10-15); points raw/verified 15/13
  - p541 Goldman Sachs forecast BYD 3Q26 total revenue = **242,936,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Goldman revenue forecast duplicate of p193/p357/p379.] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p542 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [DISCARD: Goldman revenue growth duplicate.] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p543 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [DISCARD: Goldman revenue growth duplicate.] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p544 Goldman Sachs forecast BYD 3Q26 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Goldman net profit forecast, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p545 Goldman Sachs forecast BYD 3Q26 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Goldman net profit forecast growth, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p546 Goldman Sachs forecast BYD 3Q26 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Goldman net profit forecast growth, not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p547 Goldman Sachs forecast BYD 3Q26 sales volume growth YoY = **19** % (2026-07-01..2026-09-30) [DISCARD: Goldman volume forecast duplicate.] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p548 Goldman Sachs forecast BYD 3Q26 sales volume growth QoQ = **19** % (2026-07-01..2026-09-30) [DISCARD: Goldman volume forecast duplicate.] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p549 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [DISCARD: Market share forecast duplicate.] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p550 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [DISCARD: Market share forecast duplicate.] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p551 BYD Hungary plant planned annual capacity = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Plant capacity is not Q3 2026 output or revenue.] quote: "Hungary plant is expected to commence production by the end of 2026 with planned annual capacity of 300,000 vehicles"
  - p552 China NEV export VAT rebate rate before reduction = **13** % (..2027-03-31) [DISCARD: Future VAT rebate policy, not Q3 revenue.] quote: "from April 1, 2027, the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p553 Goldman Sachs assumed cost pass-through share for VAT rebate change = **67** % (not stated (page dated 2026-10-15)) [DISCARD: VAT pass-through assumption, not Q3 revenue.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- `http://mp.weixin.qq.com/s?__biz=MjM5MjcwMTkwMA==&mid=2652626645&idx=3&sn=1f27e73217575980ff65bc7a307d5742` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.163.com/dy/article/L6A2IGDG05198ETO.html` -> **live_dated** (page date 2026-09-08); points raw/verified 15/4
  - p554 BYD target: full-year 2027 overseas sales = **2,500,000** vehicle (2027-01-01..2027-12-31) [DISCARD: 2027 overseas target, not Q3 2026 revenue.] quote: "并以2027年全年海外销量250万辆为目标"
  - p555 BYD per-vehicle profit (overseas) expected to be maintained = **20,000** CNY (not stated (page dated 2026-09-08)) [DISCARD: Per-vehicle profit, not revenue.] quote: "单车利润料维持约2万元"
  - p556 BYD long-term domestic market share target = **25** % (not stated (page dated 2026-09-08)) [DISCARD: Long-term market share target, not Q3 revenue.] quote: "国内长远市占目标约25%"
  - p557 Citi target price for BYD shares = **142** HKD (not stated (page dated 2026-09-08)) [DISCARD: Share target price, irrelevant.] quote: "目标价142港元"
- `https://4g.stockstar.com/detail/JC2026101800001092` -> **live_dated** (page date 2026-10-27); points raw/verified 15/14
  - p558 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [DISCARD: September total sales duplicate of p76.] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p559 BYD cumulative 2026 vehicle sales (Jan-Sep) = **3,131,576** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative sales duplicate of p96.] quote: "今年累计汽车销量3131576辆,同比下降3.9%"
  - p560 BYD September 2026 new energy passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: September passenger sales duplicate.] quote: "9月新能源乘用车销量456713辆,同比增长16.2%,环比增长5.4%"
  - p561 BYD cumulative 2026 passenger vehicle sales (Jan-Sep) = **3,078,544** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative passenger sales duplicate.] quote: "今年累计乘用车销量3078544辆,同比下降4.4%"
  - p562 BYD September 2026 battery electric passenger vehicle sales = **273,143** vehicle (2026-09-01..2026-09-30) [DISCARD: September BEV sales duplicate.] quote: "9月纯电动乘用车销量273143辆,同比增长33.2%"
  - p563 BYD September 2026 plug-in hybrid passenger vehicle sales = **183,570** vehicle (2026-09-01..2026-09-30) [DISCARD: September PHEV sales duplicate.] quote: "插混乘用车销量183570辆,同比下降2.4%"
  - p564 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September domestic sales duplicate.] quote: "9月国内销量28.3万辆,同比下降13%,环比增长12.8%"
  - p565 BYD cumulative 2026 domestic sales (Jan-Sep) = **1,789,000** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative domestic sales duplicate.] quote: "今年累计国内销量178.9万辆,同比下降30%"
  - p566 BYD September 2026 new energy vehicle exports = **181,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p567 BYD September 2026 export share of NEV sales = **39** % (2026-09-01..2026-09-30) [DISCARD: Export share duplicate of p82/p701.] quote: "销量占比39%,同比提升21pcts"
  - p568 BYD September 2026 Dynasty and Ocean network sales = **395,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales duplicate.] quote: "9月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p569 BYD September 2026 Fangchengbao brand sales = **43,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales duplicate.] quote: "方程豹4.3万辆(同比+79.0%)"
  - p570 BYD September 2026 Denza brand sales = **18,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales duplicate.] quote: "腾势1.8万辆(同比+46.7%)"
  - p571 BYD September 2026 premium brands (Denza/Fangchengbao/Yangwang) combined sales = **62,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Premium brand sales duplicate of p134/p707.] quote: "腾势/方程豹/仰望三个高端品牌合计6.2万辆(同比+65.7%),占乘用车销量13.5%"
- `https://caifuhao.eastmoney.com/news/20261009004855425922130` -> **live_dated** (page date 2026-10-09); points raw/verified 15/13
  - p572 BYD Q3 2026 total NEV sales volume (Q3 total) = **1,323,000** vehicle (2026-07-01..2026-09-30) [keep: ] quote: "二、Q3总销量拆解:132.3万辆,同比+18.7%"
  - p573 BYD Q3 2026 export volume of NEVs (Q3 total) = **550,700** vehicle (2026-07-01..2026-09-30) [keep: ] quote: "Q3出口55.07万辆,占销量的41.6%"
  - p574 BYD Q3 2026 export share of sales (exports / total sales) = **41.6** % (2026-07-01..2026-09-30) [keep: ] quote: "Q3出口55.07万辆,占销量的41.6%--这是比亚迪历史上出口占比首次在一个完整季度内站稳40%以上。"
  - p575 BYD Q3 2026 domestic sales volume (total less exports) = **773,000** vehicle (2026-07-01..2026-09-30) [keep: ] quote: "扣除出口后,Q3国内销量约77.3万辆,月均约25.8万辆,同比小幅下滑。"
  - p576 BYD Q3 2026 estimated revenue (method 1, low end of range) = **2,220** CNY (2026-07-01..2026-09-30) [keep: ] quote: "Q3营收约2,220~2,290亿元。"
  - p577 BYD Q3 2026 estimated per-vehicle consolidated revenue (high end, incl. electron = **173,000** CNY/vehicle (2026-07-01..2026-09-30) [keep: ] quote: "按132.3万辆销量、单车综合收入16.8~17.3万元(含电子业务,参考2025年Q3单车约17.5万元"
  - p578 BYD Q3 2025 per-vehicle consolidated revenue (reference) = **175,000** CNY/vehicle (2025-07-01..2025-09-30) [keep: ] quote: "参考2025年Q3单车约17.5万元"
  - p579 BYD H1 2026 overseas sales volume = **790,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 overseas volume, not Q3 revenue.] quote: "2026年上半年:海外销量79万辆,占销量约43.6%的销量,却贡献了52.57%的营收(境外收入1813亿元)"
  - p580 BYD H1 2026 overseas sales share of total sales = **43.6** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas share, not Q3 revenue.] quote: "2026年上半年:海外销量79万辆,占销量约43.6%的销量,却贡献了52.57%的营收(境外收入1813亿元)"
  - p581 BYD H1 2026 overseas revenue share of total revenue = **52.57** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue share, not Q3 revenue.] quote: "境外收入占比首次过半(52.57%),推动整体毛利率升至18.85%"
  - p582 BYD H1 2026 overseas (outside-China) revenue = **181,300,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue, not Q3 revenue.] quote: "却贡献了52.57%的营收(境外收入1813亿元)"
  - p583 BYD H1 2026 gross margin = **18.85** % (2026-01-01..2026-06-30) [DISCARD: H1 gross margin, not Q3 revenue.] quote: "境外收入占比首次过半(52.57%),推动整体毛利率升至18.85%"
  - p584 BYD H1 2026 net margin = **3.57** % (2026-01-01..2026-06-30) [DISCARD: H1 net margin, not Q3 revenue.] quote: "净利率假设:H1净利率3.57%,但H1被汇兑显著压制"
- `https://wap.stockstar.com/detail/IG2026090100009322` -> **live_dated** (page date 2026-10-27); points raw/verified 15/15
  - p585 BYD 2Q26 revenue (group, quarterly) = **194,600,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Q2 revenue duplicate of p135/p149/p164/p182.] quote: "比亚迪股份(01211)2Q26收入1,946亿元,环比增长29.5%、较市场预期低约10%"
  - p586 BYD 2Q26 revenue quarter-on-quarter growth = **29.5** % (2026-04-01..2026-06-30) [DISCARD: Q2 revenue growth duplicate.] quote: "2Q26收入1,946亿元,环比增长29.5%、较市场预期低约10%"
  - p587 BYD 2Q26 revenue shortfall vs market expectation = **10** % (2026-04-01..2026-06-30) [DISCARD: Q2 revenue expectation gap, not level.] quote: "环比增长29.5%、较市场预期低约10%"
  - p588 BYD 2Q26 net profit attributable to parent = **8,240,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Q2 net profit, not revenue.] quote: "归母净利82.4亿元,环比翻倍、较市场预期低约8%"
  - p589 BYD 2Q26 net profit shortfall vs market expectation = **8** % (2026-04-01..2026-06-30) [DISCARD: Q2 net profit gap, not revenue.] quote: "归母净利82.4亿元,环比翻倍、较市场预期低约8%"
  - p590 BYD 1Q26 per-vehicle revenue excluding BYD Electronics (broker estimate) = **160,000** CNY/vehicle (2026-01-01..2026-03-31) [DISCARD: Q1 per-vehicle revenue, not Q3.] quote: "该机构测算剔除比亚迪电子后的单车收入由1Q26约16万元降至约14万元"
  - p591 BYD 2Q26 per-vehicle revenue excluding BYD Electronics (broker estimate) = **140,000** CNY/vehicle (2026-04-01..2026-06-30) [DISCARD: Q2 per-vehicle revenue duplicate of p141/p150/p167.] quote: "剔除比亚迪电子后的单车收入由1Q26约16万元降至约14万元"
  - p592 BYD 2Q26 gross margin = **18.9** % (2026-04-01..2026-06-30) [DISCARD: Q2 gross margin, not revenue.] quote: "但毛利率仍维持18.9%,显示盈利改善主要来自销量恢复、费用杠杆及海外高利润业务"
  - p593 BYD 1H26 overseas passenger vehicle and pickup sales = **789,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 overseas volume, not Q3 revenue.] quote: "1H26海外乘用车及皮卡销量约78.9万辆,同比增长68%,已占集团销量约44%"
  - p594 BYD 1H26 overseas passenger vehicle and pickup sales year-on-year growth = **68** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas growth, not Q3 revenue.] quote: "1H26海外乘用车及皮卡销量约78.9万辆,同比增长68%"
  - p595 BYD 1H26 overseas sales share of group sales = **44** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas share, not Q3 revenue.] quote: "已占集团销量约44%"
  - p596 BYD 1H26 overseas revenue = **181,300,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue, not Q3 revenue.] quote: "海外收入同比增长33.9%至1,813亿元"
  - p597 BYD 1H26 overseas revenue year-on-year growth = **33.9** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue growth, not Q3 revenue.] quote: "海外收入同比增长33.9%至1,813亿元"
  - p598 BYD 1H26 overseas business gross margin (broker estimate) = **28.4** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas margin, not Q3 revenue.] quote: "按该机构测算,1H26海外业务毛利率约28.4%,显著高于中国内地的17.0%"
  - p599 BYD 1H26 mainland China business gross margin (broker estimate) = **17** % (2026-01-01..2026-06-30) [DISCARD: H1 domestic margin, not Q3 revenue.] quote: "1H26海外业务毛利率约28.4%,显著高于中国内地的17.0%"
- `https://cn.aastocks.com/en/stocks/analysis/stock-aafn-con/1211/HK6/NOW.1543312/hk-stock-news` -> **live_dated** (page date 2026-09-08); points raw/verified 15/15
  - p600 Citi forecast BYD estimated monthly overseas sales lower bound in 2H26 = **180,000** vehicle (2026-07-01..2026-12-31) [keep: ] quote: "estimated monthly overseas sales to stabilize at 180,000-200,000 units in 2H26"
  - p601 Citi forecast BYD estimated monthly overseas sales upper bound in 2H26 = **200,000** vehicle (2026-07-01..2026-12-31) [keep: ] quote: "estimated monthly overseas sales to stabilize at 180,000-200,000 units in 2H26"
  - p602 Citi target BYD full-year overseas sales 2027 = **2,500,000** vehicle (2027-01-01..2027-12-31) [DISCARD: 2027 target, not Q3 2026 revenue.] quote: "targeting full-year overseas sales of 2.5 million units in 2027"
  - p603 Citi expected BYD per-vehicle profit (overseas) = **20,000** CNY (not stated (page dated 2026-09-08)) [DISCARD: Per-vehicle profit, not revenue.] quote: "while per-vehicle profit was expected to remain at about RMB20,000, Citi said in a report"
  - p604 Citi long-term domestic market share target for BYD = **25** % (not stated (page dated 2026-09-08)) [DISCARD: Long-term market share target, not Q3 revenue.] quote: "Its long-term domestic market share target is around 25%."
  - p605 Citi forecast BYD 3Q26 core net profit = **13,000,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast, not revenue.] quote: "Citi forecast BYD COMPANY's 3Q26 core net profit at about RMB13 billion"
  - p606 Citi assumed BYD domestic sales 3Q26 = **752,000** vehicle (2026-07-01..2026-09-30) [keep: ] quote: "assuming domestic sales of 752,000 units in 3Q26"
  - p607 Citi assumed BYD per-vehicle core net profit domestic 3Q26 = **2,200** CNY (2026-07-01..2026-09-30) [DISCARD: Per-vehicle profit assumption, not revenue.] quote: "with per-vehicle core net profit of RMB2,200"
  - p608 Citi assumed BYD export sales 3Q26 = **568,000** vehicle (2026-07-01..2026-09-30) [keep: ] quote: "and export sales of 568,000 units with per-vehicle core net profit of RMB20,000"
  - p609 Citi assumed BYD per-vehicle core net profit export 3Q26 = **20,000** CNY (2026-07-01..2026-09-30) [DISCARD: Per-vehicle profit assumption, not revenue.] quote: "and export sales of 568,000 units with per-vehicle core net profit of RMB20,000"
  - p610 Citi projected QoQ decline in BYD depreciation, amortization plus R&D expense pe = **2,000** CNY (2026-07-01..2026-09-30) [DISCARD: D&A/R&D per-vehicle assumption, not revenue.] quote: "Depreciation and amortization plus R&D expenses per vehicle were projected to decline by about RMB2,000 QoQ"
  - p611 BYD share price change (01211.HK) = **-0.75** HKD (2026-10-27..2026-10-27) [DISCARD: Share price change, irrelevant.] quote: "BYD COMPANY (01211.HK) -0.750 (-1.059%)"
  - p612 BYD share price change percent (01211.HK) = **-1.059** % (2026-10-27..2026-10-27) [DISCARD: Share price change, irrelevant.] quote: "BYD COMPANY (01211.HK) -0.750 (-1.059%)"
  - p613 BYD short selling turnover = **304,750,000** HKD (2026-10-27..2026-10-27) [DISCARD: Short-selling turnover, irrelevant.] quote: "Short selling $304.75M; Ratio 27.243%"
  - p614 BYD short selling ratio = **27.24** % (2026-10-27..2026-10-27) [DISCARD: Short-selling ratio, irrelevant.] quote: "Short selling $304.75M; Ratio 27.243%"
- `http://stockfinance.sina.cn/stock/go.php/paper/reportid/845640780089/index.phtml` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- `https://wap.stockstar.com/detail/IG2026090800016230` -> **live_dated** (page date 2026-10-27); points raw/verified 11/11
  - p615 BYD monthly export volume, current (approx.) = **185,000** (range 180,000..190,000) as written "18万至19万", value check pending vehicle (2026-09-01..2026-09-30) [keep: ] quote: "目前公司月度出口约18万至19万辆"
  - p616 BYD management forecast: 2026 overseas sales growth year-on-year = **85** (range 80..90) as written "80%至90%", value check pending % (2026-01-01..2026-12-31) [DISCARD: 2026 overseas growth guidance, not Q3 revenue level.] quote: "管理层预期2026年海外销量有望同比增长80%至90%"
  - p617 BYD management forecast: 2027 overseas sales volume (over) = **2,500,000** vehicle (2027-01-01..2027-12-31) [DISCARD: 2027 overseas target, not Q3 revenue.] quote: "2027年预计进一步超过250万辆"
  - p618 CMS International estimate: BYD overseas per-vehicle profit in H1 2026 excluding = **20,000** CNY (2026-01-01..2026-06-30) [DISCARD: Per-vehicle profit, not revenue.] quote: "该行估计,上半年剔除汇兑影响后,海外业务单车盈利超过2万元人民币"
  - p619 BYD 2026 target: number of flash-charging stations to be built = **20,000** station (2026-01-01..2026-12-31) [DISCARD: Charging station target, not revenue.] quote: "公司2026年目标建成2万座闪充站"
  - p620 BYD 2027 plan: new flash-charging stations added = **30,000** station (2027-01-01..2027-12-31) [DISCARD: Charging station plan, not revenue.] quote: "2027年新增3万座"
  - p621 BYD long-term plan: total flash-charging stations (over) = **90,000** station (not stated (page dated 2026-10-27)) [DISCARD: Long-term charging station plan, not revenue.] quote: "长期规划超过9万座"
  - p622 BYD company expectation: H2 2026 domestic monthly sales increase (approx.) = **20,000** vehicle (2026-07-01..2026-12-31) [DISCARD: Domestic monthly sales expectation, not revenue.] quote: "公司预计下半年国内销量每月增加约2万辆"
  - p623 Estimated per-vehicle freight saving from overseas plant ramp-up (over) = **10,000** CNY (not stated (page dated 2026-10-27)) [DISCARD: Freight saving estimate, not revenue.] quote: "预计单车可节省1万元人民币以上运费"
  - p624 Estimated European tariff per vehicle avoided (range) = **45,000** (range 40,000..50,000) as written "4万至5万", value check pending CNY (not stated (page dated 2026-10-27)) [DISCARD: Tariff estimate, not revenue.] quote: "欧洲约4万至5万元人民币关税"
  - p625 CMS International target price for BYD shares (01211) = **130** HKD (2026-09-08..2026-09-08) [DISCARD: Share target price, irrelevant.] quote: "维持比亚迪股份(01211)"增持"评级及目标价130港元"
- `https://club.autohome.com.cn/bbs/thread/609645024fb04755/116528821-1.html` -> **live_dated** (page date 2026-10-26); points raw/verified 16/16
  - p626 BYD overseas revenue H1 2026 (first half) = **181,268,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue, not Q3 revenue.] quote: "比亚迪上半年境外收入1812.68亿元,同比增长33.92%,占总营收52.57%"
  - p627 BYD overseas revenue YoY growth H1 2026 = **33.92** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue growth, not Q3 revenue.] quote: "比亚迪上半年境外收入1812.68亿元,同比增长33.92%,占总营收52.57%"
  - p628 BYD overseas revenue share of total revenue H1 2026 = **52.57** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue share, not Q3 revenue.] quote: "占总营收52.57%,首次在绝对额上越过境内"
  - p629 BYD overseas gross margin H1 2026 = **21.71** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas gross margin, not revenue.] quote: "境外毛利率21.71%,境内15.67%,相差超过6个百分点"
  - p630 BYD domestic gross margin H1 2026 = **15.67** % (2026-01-01..2026-06-30) [DISCARD: H1 domestic gross margin, not revenue.] quote: "境外毛利率21.71%,境内15.67%,相差超过6个百分点"
  - p631 BYD domestic revenue YoY change H1 2026 = **30.68** % (2026-01-01..2026-06-30) [DISCARD: H1 domestic revenue change, not Q3 level.] quote: "上半年,比亚迪境外收入同比增长33.92%,境内收入同比下降30.68%"
  - p632 BYD exports H1 2026 = **792,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 exports, not Q3 revenue.] quote: "上半年出口79.2万辆,同比增长67.8%,占总销量接近44%"
  - p633 BYD exports YoY growth H1 2026 = **67.8** % (2026-01-01..2026-06-30) [DISCARD: H1 export growth, not Q3 revenue.] quote: "上半年出口79.2万辆,同比增长67.8%,占总销量接近44%"
  - p634 BYD exports share of total sales H1 2026 = **44** % (2026-01-01..2026-06-30) [DISCARD: H1 export share, not Q3 revenue.] quote: "上半年出口79.2万辆,同比增长67.8%,占总销量接近44%"
  - p635 BYD total sales YoY change H1 2026 = **340,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 total sales change, not Q3 revenue.] quote: "总销量同比减少约34万辆,出口同比增加约32万辆"
  - p636 BYD exports YoY increase H1 2026 = **320,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 export increase, not Q3 revenue.] quote: "总销量同比减少约34万辆,出口同比增加约32万辆"
  - p637 Management guidance: overseas net profit per vehicle (target 2026) = **20,000** CNY/vehicle (2026-01-01..2026-12-31) [DISCARD: Per-vehicle profit guidance, not revenue.] quote: "管理层指引海外平均每车净利润约2万元,并有信心在2026年达标"
  - p638 Citi forecast: Q3 export core net profit per vehicle = **20,000** CNY/vehicle (2026-07-01..2026-09-30) [DISCARD: Per-vehicle profit forecast, not revenue.] quote: "花旗预测Q3出口单车核心净利约2万元,国内约2200元,出口盈利能力约为国内的9倍"
  - p639 Citi forecast: Q3 domestic core net profit per vehicle = **2,200** CNY/vehicle (2026-07-01..2026-09-30) [DISCARD: Per-vehicle profit forecast, not revenue.] quote: "花旗预测Q3出口单车核心净利约2万元,国内约2200元,出口盈利能力约为国内的9倍"
  - p640 Premium brands (Fangchengbao, Denza, Yangwang) combined sales share of passenger = **12.8** % (2026-01-01..2026-06-30) [DISCARD: H1 premium share, not Q3 revenue.] quote: "上半年方程豹、腾势、仰望三大品牌合计销量同比增长61%,占乘用车总销量比重升至12.8%"
  - p641 Premium brands combined sales September 2026 = **62,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September premium brand sales duplicate.] quote: "9月三品牌合计销售6.2万辆,同比增长65.7%,占比13.5%,方程豹单月4.3万辆,同比增长79%"
- `http://www.163.com/dy/article/L99OB3VT05198ETO.html` -> **live_dated** (page date 2026-10-15); points raw/verified 9/1
  - p642 Goldman Sachs H-share target price for BYD = **134** HKD (not stated (page dated 2026-10-15)) [DISCARD: Share target price, irrelevant.] quote: "H股目标价维持134港元"
- dropped by code checks: 24 (period year 2030 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 19; scale word '万' not supported by quote or table header: 2; number: value_as_written is only part of a larger CJK number in the quote: 1)

### b3 [physical_flow] July-August 2026 sales mix

Hypothesis: July and August 2026 premium-brand and export volumes would refine the Q3 2026 ASP assumption a1/a2 and test whether the September mix improvement persisted.

Queries issued by the searcher: 比亚迪 2026年7月 销量 腾势 方程豹 仰望 出口; 比亚迪 2026年8月 高端品牌 销量 出口; 比亚迪 2026年9月 销量 出口 腾势 方程豹 仰望; 比亚迪 2026年半年报 营业收入 单车均价 上半年; 比亚迪 2026年7月 销量 腾势 方程豹 仰望 出口; 比亚迪 2026年8月 高端品牌 销量 出口; 比亚迪 2026年9月销量 方程豹 腾势 出口 创新高; 比亚迪 2026年三季报 营业收入 预测 三季度 单车均价; 比亚迪 2026年7月 销量 腾势 方程豹 仰望 出口; 比亚迪 2026年8月 销量 高端品牌 出口; 比亚迪 2026年9月 销量 三季度 营业收入 单车均价; 比亚迪 2026年二季度 营业收入 单车ASP 元 财报

- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/company/rptid/839030501135/index.phtml` -> **live_dated** (page date 2026-08-03); points raw/verified 15/12
  - p643 BYD total vehicle sales, July 2026 = **419,000** vehicle (2026-07-01..2026-07-31) [keep: ] quote: "比亚迪7 月销售41.9 万辆,同环比+22%/+4%"
  - p644 BYD passenger vehicle sales, July 2026 = **411,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July passenger sales duplicate.] quote: "其中乘用车销售41.1 万辆,同环比+21%/+3%"
  - p645 BYD domestic sales, July 2026 = **239,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July domestic sales duplicate.] quote: "7 月本土销售23.9 万辆,同环比-9%/+5%"
  - p646 BYD overseas (export) sales, July 2026 = **180,000** vehicle (2026-07-01..2026-07-31) [keep: ] quote: "海外销售18.0 万辆,同环比+124%/+3%,再创历史新高"
  - p647 Overseas share of BYD total sales, July 2026 = **43** % (2026-07-01..2026-07-31) [keep: ] quote: "占总销量43%,占比同比提升20pct"
  - p648 BYD cumulative sales, January-July 2026 = **2,228,000** vehicle (2026-01-01..2026-07-31) [DISCARD: January-July cumulative sales duplicate.] quote: "26 年1-7 月累计销售222.8 万辆,同比-11%"
  - p649 BYD cumulative overseas sales, January-July 2026 = **969,000** vehicle (2026-01-01..2026-07-31) [DISCARD: January-July overseas cumulative duplicate.] quote: "其中海外累计销售96.9 万辆,同比+76%"
  - p650 BYD cumulative domestic sales, January-July 2026 = **1,259,000** vehicle (2026-01-01..2026-07-31) [DISCARD: January-July domestic cumulative duplicate.] quote: "本土累计销售125.9 万辆,同比-35%"
  - p651 Fangchengbao sales, July 2026 = **41,200** vehicle (2026-07-01..2026-07-31) [DISCARD: July brand sales duplicate.] quote: "7 月腾势/ 仰望/ 方程豹分别销售1.92/0.05/4.12 万辆"
  - p652 Three premium brands combined sales, July 2026 = **60,900** vehicle (2026-07-01..2026-07-31) [keep: ] quote: "三品牌合计销售6.09 万辆,同环比+135%/+8%,占乘用车销量15%"
  - p653 Three premium brands share of BYD passenger vehicle sales, July 2026 = **15** % (2026-07-01..2026-07-31) [keep: ] quote: "三品牌合计销售6.09 万辆,同环比+135%/+8%,占乘用车销量15%"
  - p654 Fangchengbao cumulative sales, January-July 2026 = **200,700** vehicle (2026-01-01..2026-07-31) [DISCARD: January-July brand cumulative duplicate.] quote: "26 年1-7 月腾势/仰望/方程豹累计销售8.57/0.25/20.07 万辆"
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/842429186459/index.phtml` -> **live_dated** (page date 2026-09-11); points raw/verified 15/15
  - p655 BYD August 2026 total vehicle sales = **440,293** vehicle (2026-08-01..2026-08-31) [keep: ] quote: "8 月汽车销售440,293 辆,同比+17.8%,环比+5.0%"
  - p656 BYD August 2026 domestic vehicle sales = **251,547** vehicle (2026-08-01..2026-08-31) [DISCARD: August domestic sales duplicate.] quote: "国内汽车销量251,547 辆,同比-14.2%,环比+5.1%"
  - p657 BYD August 2026 passenger vehicle and pickup export sales = **188,746** vehicle (2026-08-01..2026-08-31) [keep: ] quote: "乘用车及皮卡出口销量188,746 辆,同比+134.4%,环比+5.0%"
  - p658 BYD August 2026 Denza brand sales = **16,001** vehicle (2026-08-01..2026-08-31) [DISCARD: August Denza sales duplicate.] quote: "8 月王朝海洋、腾势、方程豹、仰望销量分别375,373 辆、16,001 辆、41,568 辆、442 辆"
  - p659 BYD August 2026 Fangchengbao brand sales = **41,568** vehicle (2026-08-01..2026-08-31) [DISCARD: August Fangchengbao sales duplicate.] quote: "8 月王朝海洋、腾势、方程豹、仰望销量分别375,373 辆、16,001 辆、41,568 辆、442 辆"
  - p660 BYD August 2026 Yangwang brand sales = **442** vehicle (2026-08-01..2026-08-31) [DISCARD: August Yangwang sales duplicate.] quote: "8 月王朝海洋、腾势、方程豹、仰望销量分别375,373 辆、16,001 辆、41,568 辆、442 辆"
  - p661 BYD August 2026 Dynasty+Ocean brand sales = **375,373** vehicle (2026-08-01..2026-08-31) [DISCARD: August Dynasty/Ocean sales duplicate.] quote: "8 月王朝海洋、腾势、方程豹、仰望销量分别375,373 辆、16,001 辆、41,568 辆、442 辆"
  - p662 BYD August 2026 premium brands (Denza+Yangwang+Fangchengbao) combined share of s = **13.2** % (2026-08-01..2026-08-31) [DISCARD: August premium share duplicate.] quote: "合计5.8 万辆,占比13.2%,相比2025 年8 月的占比7.7%提升明显"
  - p663 BYD August 2025 premium brands combined share of sales (comparison) = **7.7** % (2025-08-01..2025-08-31) [DISCARD: Prior-year premium share duplicate/context.] quote: "相比2025 年8 月的占比7.7%提升明显"
  - p664 BYD January-August 2026 cumulative passenger vehicle sales = **2,622,000** vehicle (2026-01-01..2026-08-31) [DISCARD: January-August cumulative passenger duplicate.] quote: "1-8 月乘用车累计销售262.2 万辆,同比-7.2%"
  - p665 BYD January-August 2026 cumulative export sales = **1,158,000** vehicle (2026-01-01..2026-08-31) [DISCARD: January-August cumulative export duplicate.] quote: "1-8 月累计出口销量115.8 万辆,同比+85.7%"
  - p666 BYD July 2026 overseas terminal sales (MarkLines) = **82,534** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines terminal sales different definition, not needed.] quote: "根据MarkLines 数据,7 月公司海外终端销量82,534 辆,同比+76.7%"
  - p667 BYD January-July 2026 cumulative overseas terminal sales (MarkLines) = **558,000** vehicle (2026-01-01..2026-07-31) [DISCARD: MarkLines cumulative terminal sales, not needed.] quote: "1-7 月累计销量55.8 万辆,同比+82.9%"
  - p668 BYD July 2026 Europe sales (MarkLines) = **28,474** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines Europe sales, not needed.] quote: "其中,欧洲销量28,474 辆,同比+109.5%"
  - p669 BYD July 2026 Brazil sales (MarkLines) = **22,937** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines Brazil sales, not needed.] quote: "拉美核心市场巴西销量22,937 辆,同比+138.1%"
- `https://news.yiche.com/hao/wenzhang/112830218/` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/841688869045/index.phtml` -> **live_dated** (page date 2026-09-02); points raw/verified 15/12
  - p670 BYD total vehicle sales, August 2026 = **440,000** vehicle (2026-08-01..2026-08-31) [DISCARD: August total sales duplicate.] quote: "比亚迪8 月销售44.0 万辆,同环比+18%/+5%"
  - p671 BYD passenger vehicle sales, August 2026 = **433,000** vehicle (2026-08-01..2026-08-31) [DISCARD: August passenger sales duplicate.] quote: "其中乘用车销售43.3 万辆,同环比+17%/+5%"
  - p672 BYD domestic sales, August 2026 = **252,000** vehicle (2026-08-01..2026-08-31) [DISCARD: August domestic sales duplicate.] quote: "8 月本土销售25.2 万辆,同环比-14%/+5%,连续三个月环比改善"
  - p673 BYD overseas (export) sales, August 2026 = **189,000** vehicle (2026-08-01..2026-08-31) [DISCARD: August overseas sales duplicate.] quote: "海外销售18.9万辆,同环比+135%/+5%,再创历史新高,占总销量43%,同比提升21pct"
  - p674 BYD overseas sales share of total sales, August 2026 = **43** % (2026-08-01..2026-08-31) [DISCARD: August overseas share duplicate.] quote: "占总销量43%,同比提升21pct"
  - p675 BYD cumulative sales, January-August 2026 = **2,668,000** vehicle (2026-01-01..2026-08-31) [DISCARD: January-August cumulative sales duplicate.] quote: "26 年1-8 月累计销售266.8 万辆,同比-7%"
  - p676 BYD cumulative overseas sales, January-August 2026 = **1,158,000** vehicle (2026-01-01..2026-08-31) [DISCARD: January-August cumulative overseas duplicate.] quote: "其中海外累计销售115.8 万辆,同比+85%"
  - p677 BYD cumulative domestic sales, January-August 2026 = **1,510,000** vehicle (2026-01-01..2026-08-31) [DISCARD: January-August cumulative domestic duplicate.] quote: "本土累计销售151.0 万辆,同比-33%"
  - p678 BYD full-year 2026 sales forecast (analyst estimate) = **5,000,000** vehicle (2026-01-01..2026-12-31) [DISCARD: Annual sales forecast, not Q3 actual.] quote: "我们预计26 年销量500万辆+"
  - p679 BYD full-year 2026 overseas sales forecast, upper bound (analyst estimate) = **1,900,000** vehicle (2026-01-01..2026-12-31) [DISCARD: Annual overseas forecast, not Q3 actual.] quote: "其中海外预计180-190 万辆、本土约315 万辆"
  - p680 BYD full-year 2026 domestic sales forecast (analyst estimate) = **3,150,000** vehicle (2026-01-01..2026-12-31) [DISCARD: Annual domestic forecast, not Q3 actual.] quote: "本土约315 万辆,出口高增持续对冲国内销量压力"
  - p681 Fangchengbao sales, August 2026 = **41,600** vehicle (2026-08-01..2026-08-31) [DISCARD: August brand sales duplicate.] quote: "8 月腾势/仰望/方程豹分别销售1.60/0.04/4.16 万辆"
- `https://data.eastmoney.com/report/info/AP202610071830188451.html` -> **live_dated** (page date 2026-10-08); points raw/verified 15/13
  - p682 BYD September 2026 total vehicle sales = **464,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September total sales rounded duplicate.] quote: "比亚迪9月销售46.4万辆,同环比+17%/+5%"
  - p683 BYD September 2026 passenger vehicle sales = **457,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September passenger sales rounded duplicate.] quote: "其中乘用车销售45.7万辆,同环比+16%/+5%"
  - p684 BYD September 2026 overseas sales = **180,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September overseas sales rounded duplicate.] quote: "海外销售18.0万辆,同比+154%、环比-5%,维持高位"
  - p685 BYD September 2026 overseas share of total sales = **39** % (2026-09-01..2026-09-30) [DISCARD: September overseas share duplicate.] quote: "占总销量39%,同比提升21pct"
  - p686 BYD September 2026 domestic sales = **284,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September domestic sales rounded duplicate.] quote: "9月本土销售28.4万辆,同环比-13%/+13%"
  - p687 BYD January-September 2026 cumulative total sales = **3,132,000** vehicle (2026-01-01..2026-09-30) [DISCARD: January-September cumulative sales rounded duplicate.] quote: "26年1-9月累计销售313.2万辆,同比-4%"
  - p688 BYD January-September 2026 cumulative overseas sales = **1,338,000** vehicle (2026-01-01..2026-09-30) [DISCARD: January-September cumulative overseas rounded duplicate.] quote: "其中海外累计销售133.8万辆,同比+92%"
  - p689 BYD January-September 2026 cumulative domestic sales = **1,794,000** vehicle (2026-01-01..2026-09-30) [DISCARD: January-September cumulative domestic rounded duplicate.] quote: "本土累计销售179.4万辆,同比-30%"
  - p690 BYD full-year 2026 forecast total sales (analyst estimate) = **4,750,000** (range 4,500,000..5,000,000) as written "450-500", value check pending vehicle (2026-01-01..2026-12-31) [DISCARD: Annual sales forecast, not Q3 actual.] quote: "我们预计26年销量450-500万辆"
  - p691 BYD full-year 2026 forecast overseas sales (analyst estimate) = **1,850,000** (range 1,800,000..1,900,000) as written "180-190", value check pending vehicle (2026-01-01..2026-12-31) [DISCARD: Annual overseas forecast, not Q3 actual.] quote: "其中海外180-190万辆,出口高增持续对冲国内销量压力"
  - p692 Fangchengbao September 2026 sales = **43,200** vehicle (2026-09-01..2026-09-30) [DISCARD: September brand sales duplicate.] quote: "9月腾势/仰望/方程豹分别销售1.82/0.04/4.32万辆"
  - p693 Denza/Yangwang/Fangchengbao combined September 2026 sales = **61,800** vehicle (2026-09-01..2026-09-30) [DISCARD: September premium brand sales duplicate.] quote: "三品牌合计销售6.18万辆,同比+66%、环比+6%,占乘用车销量14%"
  - p694 Denza/Yangwang/Fangchengbao combined share of September 2026 passenger vehicle s = **14** % (2026-09-01..2026-09-30) [DISCARD: September premium share duplicate.] quote: "三品牌合计销售6.18万辆,同比+66%、环比+6%,占乘用车销量14%"
- `https://stock.finance.sina.com.cn/stock/view/paper.php?symbol=sh000001&reportid=839078256807&autocallup=no&isfromsina=no` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- `https://4g.stockstar.com/detail/JC2026101800001092` -> **live_dated** (page date 2026-10-27); points raw/verified 15/14
  - p695 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p696 BYD cumulative vehicle sales Jan-Sep 2026 = **3,131,576** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative sales duplicate.] quote: "今年累计汽车销量3131576辆,同比下降3.9%"
  - p697 BYD September 2026 new energy passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: September passenger sales duplicate.] quote: "9月新能源乘用车销量456713辆,同比增长16.2%,环比增长5.4%"
  - p698 BYD cumulative passenger vehicle sales Jan-Sep 2026 = **3,078,544** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative passenger sales duplicate.] quote: "今年累计乘用车销量3078544辆,同比下降4.4%"
  - p699 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September domestic sales duplicate.] quote: "9月国内销量28.3万辆,同比下降13%,环比增长12.8%"
  - p700 BYD cumulative domestic sales Jan-Sep 2026 = **1,789,000** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative domestic sales duplicate.] quote: "今年累计国内销量178.9万辆,同比下降30%"
  - p701 BYD September 2026 new energy vehicle exports = **181,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September export duplicate.] quote: "9月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%,销量占比39%"
  - p702 BYD September 2026 export share of sales = **39** % (2026-09-01..2026-09-30) [DISCARD: September export share duplicate.] quote: "9月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%,销量占比39%,同比提升21pcts"
  - p703 BYD Dynasty and Ocean network September 2026 sales = **395,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September Dynasty/Ocean sales duplicate.] quote: "9月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p704 BYD Fangchengbao September 2026 sales = **43,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September Fangchengbao sales duplicate.] quote: "方程豹4.3万辆(同比+79.0%)"
  - p705 BYD Denza September 2026 sales = **18,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September Denza sales duplicate.] quote: "腾势1.8万辆(同比+46.7%)"
  - p706 BYD Yangwang September 2026 sales = **389** vehicle (2026-09-01..2026-09-30) [DISCARD: September Yangwang sales duplicate.] quote: "仰望389辆(同比-48.7%)"
  - p707 BYD premium brands (Denza/Fangchengbao/Yangwang) combined September 2026 sales = **62,000** vehicle (2026-09-01..2026-09-30) [DISCARD: September premium brand sales duplicate.] quote: "腾势/方程豹/仰望三个高端品牌合计6.2万辆(同比+65.7%),占乘用车销量13.5%"
  - p708 BYD premium brands share of passenger vehicle sales September 2026 = **13.5** % (2026-09-01..2026-09-30) [DISCARD: September premium share duplicate.] quote: "占乘用车销量13.5%,同比提升4pcts,高端品牌占比提升有助改善单车ASP"
- `http://news.cheshi.com/20260803/3425503.shtml` -> **live_dated** (page date 2026-08-03); points raw/verified 15/15
  - p709 BYD July 2026 total monthly sales (all vehicles) = **419,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July total sales duplicate.] quote: "比亚迪公布2026年7月产销数据,单月销量达41.9万辆,同比增长21.8%"
  - p710 BYD July 2026 total monthly sales year-on-year growth = **21.8** % (2026-07-01..2026-07-31) [DISCARD: July total growth duplicate.] quote: "单月销量达41.9万辆,同比增长21.8%"
  - p711 BYD H1 2026 cumulative new energy vehicle sales = **1,809,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 cumulative sales duplicate.] quote: "继2026年上半年以180.9万辆稳居中国新能源汽车销量冠军后"
  - p712 BYD Dynasty and Ocean brands July 2026 combined sales = **350,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July Dynasty/Ocean sales duplicate.] quote: "比亚迪品牌王朝、海洋依然是比亚迪销量的基本盘,7月合计销售35万辆,同比增长11.1%"
  - p713 BYD Dynasty and Ocean brands July 2026 sales year-on-year growth = **11.1** % (2026-07-01..2026-07-31) [DISCARD: July Dynasty/Ocean growth duplicate.] quote: "7月合计销售35万辆,同比增长11.1%"
  - p714 BYD premium brands (Fangchengbao, Denza, Yangwang) July 2026 combined sales, sta = **60,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July premium brand sales duplicate.] quote: "方程豹、腾势、仰望合计销售超6万辆,同比增长约135%,占集团乘用车销量14.8%"
  - p715 BYD premium brands July 2026 combined sales year-on-year growth, stated as appro = **135** % (2026-07-01..2026-07-31) [DISCARD: July premium brand growth duplicate.] quote: "方程豹、腾势、仰望合计销售超6万辆,同比增长约135%"
  - p716 BYD premium brands share of group passenger vehicle sales, July 2026 = **14.8** % (2026-07-01..2026-07-31) [DISCARD: July premium share duplicate.] quote: "占集团乘用车销量14.8%"
  - p717 Fangchengbao brand July 2026 sales = **41,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July Fangchengbao sales duplicate.] quote: "方程豹7月销售4.1万辆,创今年新高,同比增长190.6%,环比增长15.7%"
  - p718 Fangchengbao brand July 2026 sales year-on-year growth = **191** % (2026-07-01..2026-07-31) [DISCARD: July Fangchengbao growth duplicate.] quote: "方程豹7月销售4.1万辆,创今年新高,同比增长190.6%,环比增长15.7%"
  - p719 Fangchengbao brand July 2026 sales month-on-month growth = **15.7** % (2026-07-01..2026-07-31) [DISCARD: July Fangchengbao growth duplicate.] quote: "同比增长190.6%,环比增长15.7%"
  - p720 Fangchengbao brand average transaction price, July 2026, stated as over = **223,000** CNY (2026-07-01..2026-07-31) [DISCARD: Fangchengbao average transaction price, not needed.] quote: "品牌成交均价超过22.3万元"
  - p721 Denza brand July 2026 sales = **19,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July Denza sales duplicate.] quote: "腾势7月销售1.9万辆,同比增长68.8%"
  - p722 Denza brand July 2026 sales year-on-year growth = **68.8** % (2026-07-01..2026-07-31) [DISCARD: July Denza growth duplicate.] quote: "腾势7月销售1.9万辆,同比增长68.8%"
  - p723 Yangwang brand July 2026 sales = **485** vehicle (2026-07-01..2026-07-31) [DISCARD: July Yangwang sales duplicate.] quote: "仰望销售485辆,同比增长43.1%"
- `http://stockfinance.sina.cn/stock/go.php/paper/reportid/839270344235/index.phtml?&cid=79649` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/845350343886/index.phtml` -> **live_dated** (page date 2026-10-14); points raw/verified 9/9
  - p724 BYD Group total vehicle sales, September 2026 = **463,561** vehicle (2026-09-01..2026-09-30) [DISCARD: September total sales duplicate of p76.] quote: "2026 年9 月,比亚迪集团销售463,561辆"
  - p725 BYD passenger vehicle and pickup overseas sales, September 2026 = **179,877** vehicle (2026-09-01..2026-09-30) [DISCARD: September export duplicate of p81/p94/p132.] quote: "其中乘用车及皮卡海外销售179,877 辆,同比+153.9%"
  - p726 BYD overseas sales year-on-year growth, September 2026 = **154** % (2026-09-01..2026-09-30) [DISCARD: September export growth duplicate.] quote: "其中乘用车及皮卡海外销售179,877 辆,同比+153.9%"
  - p727 BYD Dynasty/Ocean brand sales, September 2026 = **394,945** vehicle (2026-09-01..2026-09-30) [DISCARD: September brand sales duplicate.] quote: "王朝/海洋、方程豹、腾势、仰望分别销售394,945 辆、43,181 辆、18,198 辆、389 辆"
  - p728 BYD Fangchengbao brand sales, September 2026 = **43,181** vehicle (2026-09-01..2026-09-30) [DISCARD: September Fangchengbao sales duplicate.] quote: "王朝/海洋、方程豹、腾势、仰望分别销售394,945 辆、43,181 辆、18,198 辆、389 辆"
  - p729 BYD Denza brand sales, September 2026 = **18,198** vehicle (2026-09-01..2026-09-30) [DISCARD: September Denza sales duplicate.] quote: "王朝/海洋、方程豹、腾势、仰望分别销售394,945 辆、43,181 辆、18,198 辆、389 辆"
  - p730 BYD Yangwang brand sales, September 2026 = **389** vehicle (2026-09-01..2026-09-30) [DISCARD: September Yangwang sales duplicate.] quote: "王朝/海洋、方程豹、腾势、仰望分别销售394,945 辆、43,181 辆、18,198 辆、389 辆"
  - p731 BYD Thailand plant cumulative NEV production milestone, as of 2026-09-21 = **100,000** vehicle (2026-09-21..2026-09-21) [DISCARD: Thailand production milestone, not Q3 revenue.] quote: "9 月21 日,比亚迪泰国工厂迎来第10 万辆新能源汽车正式下线"
  - p732 BYD overseas sales year-on-year growth, September 2026 (comment section) = **154** % (2026-09-01..2026-09-30) [DISCARD: Export growth comparison, not Q3 revenue.] quote: "比亚迪、吉利、奇瑞、长城各自口径下的出口销量同比分别增长154%、162%、51%、19%"
- `https://www.bitauto.com/article/1003111957294/` -> **dropped** (live http 404); points raw/verified -/-
- `https://m.d1ev.com/news/shichang/313327` -> **live_dated** (page date 2026-10-01); points raw/verified 11/11
  - p733 BYD Group total new vehicle sales, September 2026 = **463,561** vehicle (2026-09-01..2026-09-30) [DISCARD: September total sales duplicate.] quote: "2026年9月,比亚迪集团单月累计销售新车463,561辆"
  - p734 BYD passenger vehicle sales, September 2026 = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: September passenger sales duplicate.] quote: "其中,乘用车销售456,713辆"
  - p735 BYD Dynasty and Ocean network sales, September 2026 = **394,945** vehicle (2026-09-01..2026-09-30) [DISCARD: September Dynasty/Ocean sales duplicate.] quote: "9月份,王朝和海洋网共售出394,945辆"
  - p736 Fangchengbao brand sales, September 2026 = **43,181** vehicle (2026-09-01..2026-09-30) [DISCARD: September Fangchengbao sales duplicate.] quote: "专业个性化品牌方程豹9月销售43,181辆"
  - p737 Denza brand sales, September 2026 = **18,198** vehicle (2026-09-01..2026-09-30) [DISCARD: September Denza sales duplicate.] quote: "豪华品牌腾势9月销售18,198辆"
  - p738 Yangwang brand sales, September 2026 = **389** vehicle (2026-09-01..2026-09-30) [DISCARD: September Yangwang sales duplicate.] quote: "百万级高端品牌仰望9月销售389辆"
  - p739 BYD passenger vehicle and pickup overseas sales, September 2026 = **179,877** vehicle (2026-09-01..2026-09-30) [DISCARD: September export duplicate.] quote: "9月比亚迪乘用车及皮卡海外销售达到179,877辆"
  - p740 BYD overseas sales year-on-year growth, September 2026 = **154** % (2026-09-01..2026-09-30) [DISCARD: September export growth duplicate.] quote: "同比增长高达153.9%"
  - p741 BYD passenger vehicle and pickup cumulative overseas sales, January-September 20 = **1,337,831** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative overseas sales duplicate.] quote: "2026年1-9月的累计数据显示,其乘用车及皮卡海外累计销售已达1,337,831辆"
  - p742 BYD Group cumulative sales, January-September 2026 = **3,131,576** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative total sales duplicate of p96.] quote: "2026年1-9月,比亚迪集团累计销售3,131,576辆"
  - p743 BYD new energy vehicle historical cumulative sales to date = **18,200,000** vehicle (..2026-09-30) [DISCARD: Historical cumulative sales, not Q3 revenue.] quote: "比亚迪新能源汽车的历史累计销量已正式突破1820万辆"
- dropped by code checks: 9 (scale word '万' not supported by quote or table header: 9)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p31', 'p46', 'p48', 'p61', 'p63', 'p16', 'p347'] All report BYD Q1 2026 consolidated operating revenue near CNY 150.225bn. p46 gives the exact 150,225,314,000 figure; p1/p31/p16 are rounded versions of the same company filing, so they corroborate bu
- corroborating: ['p135', 'p149', 'p164', 'p182', 'p316'] Q2 2026 consolidated revenue is consistently about CNY 194.59bn. p149 rounds to CNY 194.6bn. These come from the same quarterly report/derived commentary, so they are one underlying source.
- corroborating: ['p315', 'p329', 'p345', 'p179'] H1 2026 operating revenue is CNY 344.815bn; p179 rounds to CNY 344.82bn. This is consistent with Q1 2026 plus Q2 2026.
- corroborating: ['p354', 'p205', 'p219', 'p234'] Q3 2025 consolidated revenue is CNY 194.9846bn exactly in the quarterly table; p205/p219/p234 round or restate the same quarter to about CNY 195bn.
- corroborating: ['p220', 'p206', 'p235'] Q3 2025 automotive revenue excluding BYD Electronics is about CNY 152.31bn. p206/p235 round to CNY 152.3bn.
- corroborating: ['p221', 'p233', 'p207'] Q3 2025 total vehicle sales were 1.114m. p207 is 1.106m passenger vehicles, which is consistent with a small commercial-vehicle component.
- corroborating: ['p96', 'p83', 'p124'] January-September 2026 cumulative NEV sales are 3,131,576. These are repeated versions of the same monthly sales announcement.
- corroborating: ['p327', 'p184', 'p185', 'p328'] H1 2026 NEV volume is 1,808,500 and H1 2026 exports are 790,000. These allow Q3 2026 volume and export share to be derived by subtracting H1 from January-September.
- corroborating: ['p76', 'p90', 'p101', 'p121', 'p112'] September 2026 total vehicle/NEV sales are about 463,561; p112 rounds to 46.36万辆. Same monthly sales announcement.
- corroborating: ['p473', 'p475', 'p481'] August 2026 BYD NEV shipments are about 432,684; CPCA wholesale 433,384 differs slightly by definition/rounding. Not a material conflict for Q3 volume.
- conflicting: ['p265', 'p310', 'p263', 'p311', 'p312', 'p313'] The period labels are inconsistent: p310/p263's CNY 123.285bn 9M revenue and p265's CNY 42.68bn Q3 revenue align with 2025 actuals, not 2026 actuals. Q3 2025 revenue of CNY 42.68bn plus H1 2025 CNY 80
- conflicting: ['p266', 'p267'] BYD Electronic Q3 net profit around CNY 1.41bn conflicts with 9M/H1 net profit arithmetic and is not needed for revenue. Likely mis-dated Q3 2025 data.
- conflicting: ['p404'] The article implies prior-year Q3 revenue of CNY 213.06bn, but BYD's actual Q3 2025 revenue was CNY 194.98bn. The base period or entity scope is inconsistent; unusable as a Q3 2026 revenue anchor.
- overlapping: ['p193', 'p357', 'p379', 'p370'] Goldman Sachs Q3 2026 revenue forecast of CNY 242.936bn, up 25% YoY/QoQ. Repeated versions of one sell-side forecast, not an actual outcome. It is a useful upper cross-check but conflicts with volume-
- corroborating: ['p141', 'p150', 'p167'] Q2 2026 BYD ASP excluding BYD Electronics is CNY 136k. Same actual/analyst calculation repeated.
- corroborating: ['p208', 'p224', 'p236'] Q3 2025 ASP is CNY 137k-138k depending on rounding/definition. Minor definitional differences, not a real conflict.
- context: ['p170', 'p191', 'p192', 'p173', 'p174'] H1 2026 export and domestic ASPs and gross margins inform mix effects, but they are H1 averages and cannot be directly substituted for Q3 2026 ASP.
- related: ['p429', 'p328', 'p96', 'p327'] January-September 2026 exports of 1.338m minus H1 2026 exports of 0.790m imply Q3 2026 exports near 0.548m, or about 41.4% of derived Q3 volume. This is slightly below Q2 2026's ~43.3% export share an
- related: ['p89', 'p187', 'p134'] September 2026 premium-brand share was 13.5%, versus H1 2026 12.8%. This suggests a small positive Q3 mix effect, but only one month is observed and the effect on ASP is modest.
- context: ['p326', 'p392', 'p393', 'p394', 'p397', 'p398', 'p399'] Full-year and stale consensus forecasts are inconsistent with H1 2026 run-rate and/or refer to later quarters. They are not suitable Q3 2026 revenue methods, only loose context.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p76', 'p90', 'p101', 'p121', 'p407', 'p643', 'p655', 'p695', 'p96', 'p327', 'p572'] September 2026 total NEV sales cluster at 463,561; July 419k and August 440,293k sum with September to about 1.323m. Official 9M 3,131,576 less H1 1,808,500 gives 1,323,076, matching p572. Multiple UR
- corroborating: ['p81', 'p94', 'p111', 'p118', 'p132', 'p426', 'p566', 'p573', 'p574', 'p608'] September NEV exports 180,700/181,000 and passenger/pickup 179,877 are consistent within scope and rounding; Q3 export 550,700 and 41.6% share match Jul-Aug-Sep monthly export totals. Citi's 568k Q3 e
- corroborating: ['p205', 'p219', 'p234', 'p354', 'p221', 'p233', 'p220', 'p206', 'p208', 'p236'] Q3 2025 consolidated revenue 194.98bn, volume 1.114m, automotive revenue 152.3bn, ASP 137-138k. The exact quarterly table p354 is preferred as the historical baseline.
- corroborating: ['p135', 'p149', 'p164', 'p182', 'p316', 'p141', 'p150', 'p167', 'p137', 'p153', 'p166'] Q2 2026 revenue 194.59-194.6bn and volume 1.108-1.11m; ex-BYD-Electronic ASP 136k. p170 H1 ASP 143k domestic/163k export is a different period and method, not a contradiction.
- corroborating: ['p315', 'p329', 'p345', 'p317', 'p332', 'p319', 'p330', 'p272', 'p509', 'p527'] H1 2026 total revenue 344.815bn; auto segment 275.341bn and electronics segment 69.405bn sum near total after eliminations. BYD Electronic company revenue 82.234bn is larger than the electronics segme
- corroborating: ['p263', 'p310', 'p522', 'p272', 'p509', 'p527'] BYD Electronic 9M 2026 revenue 123.285bn and H1 82.234bn imply Q3 of about 41.05bn. p265's 42.68bn conflicts with this arithmetic and has an implausible pre-Q3-end date, so it is discarded.
- conflicting: ['p193', 'p576', 'p577', 'p578'] Goldman's single-source forecast 242.936bn conflicts with caifuhao's 222-229bn volume-by-per-vehicle estimate. The gap is about 6-9%; treat Goldman as an upper cross-check, not independent actual.
- corroborating: ['p574', 'p138', 'p151', 'p223', 'p89', 'p134', 'p187', 'p186', 'p200', 'p365'] Q3 2026 export share about 41.6% vs Q2 about 42.4-43.3% and Q3 2025 20.8%; premium brand share 13.5% in September vs H1 12.8%. Mix supports stable-to-slightly-higher ASP but not a large jump; domestic
- corroborating: ['p606', 'p608', 'p572', 'p573'] Citi's Q3 assumptions (752k domestic plus 568k export) sum to 1.32m, consistent with actual Q3 volume 1.323m and export 550.7k; the export assumption is about 17k high but the total is close.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Q3 2026 ASP excluding BYD Electronic relative to Q2 2026 ex-electronics ASP | 1.01 | 0.94..1.08 | 0.7125..1.425 (widened) | dimensionless | m1 (m1) | Q2 2026 ex-BYD-Electronic ASP was 136k (p141), while Q3 2025 was 137k (p236). Q3 2026 export share is slightly lower than Q2 (41.6% p574 vs 42.4% p138) but premium share rose to 13.5% (p89 vs H1 12.8% p187), and domestic market share improved to 25% (p200/p365). New flash-charge models may help ASP, | Used in m1, where Q3 volume is multiplied by Q2 ex-electronics ASP and then BYD Electronic Q3 revenue is added. | Reported Q3 2026 automotive revenue per vehicle ex-BYD-Electronic outside roughly 128k-147k CNY/vehicle, or a sharp export/premium mix reversal versus Q2. |
| a2 | Q3 2026 consolidated revenue per vehicle relative to Q3 2025 | 0.96 | 0.9..1.03 | 0.6808..1.362 (widened) | dimensionless | m2 (m2) | Q3 2025 consolidated revenue per vehicle was about 175k (p354 / p221), and Q2 2026 was about 176k (p135 / p137). Q3 2026 volume rises to about 1.323m, but BYD Electronic revenue is roughly flat at about 41bn (p522 minus p272) versus about 44bn in Q2 (p272 minus p3), so electronics revenue per vehicl | Used in m2 to scale Q3 2025 consolidated revenue by the Q3 2026/Q3 2025 volume ratio. | Q3 2026 revenue per vehicle materially above Q3 2025, for example if electronics revenue or export ASP surges. |
| a3 | Q3 2026 consolidated revenue per vehicle relative to Q2 2026 | 0.96 | 0.9..1.02 | 0.6775..1.355 (widened) | dimensionless | m3 (m3) | Q2 2026 consolidated revenue per vehicle was about 176k (p135 / p137). Q3 volume is about 19% higher sequentially, but BYD Electronic revenue is roughly flat, so its per-vehicle contribution falls from about 40k to about 31k. Export share edges down from 42.4% to 41.6% (p138 vs p574), while premium  | Used in m3 to scale Q2 2026 consolidated revenue by the Q3 2026/Q2 2026 volume ratio. | Q3 2026 consolidated revenue per vehicle at or above Q2 2026, or a large upward ASP/mix surprise. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 219,760,222,076 | ['p96', 'p327', 'p141', 'p522', 'p272'] / ['a1'] | [] |  | 1.00 | B1 of 3 blocks; median of blocks: this block is the median |  |
| m2 | formula_mc | 220,287,835,890 | ['p354', 'p96', 'p327', 'p221'] / ['a2'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | formula_mc | 217,816,169,010 | ['p135', 'p96', 'p327', 'p137'] / ['a3'] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: (vol_cum - vol_h1) * asp_q2 * a1 + (be_9m - be_h1); Monte Carlo P10 to P90 121,277,448,888 to 366,669,375,657; result unit CNY converted to CNY; own 80% width x/÷1.74 (Monte Carlo of the formula inputs)
- m2 formula_mc: rev_q3_25 * ((vol_cum - vol_h1) / vol_q3_25) * a2; Monte Carlo P10 to P90 100,799,054,723 to 407,288,943,655; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷2.01 (Monte Carlo of the formula inputs)
- m3 formula_mc: rev_q2 * ((vol_cum - vol_h1) / vol_q2) * a3; Monte Carlo P10 to P90 101,605,432,520 to 407,809,255,887; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷2.00 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 219,760,222,076 (width x/÷1.74, Monte Carlo of the formula inputs); B2 = m2: 220,287,835,890 (width x/÷2.01, Monte Carlo of the formula inputs); B3 = m3: 217,816,169,010 (width x/÷2.00, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.92; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.92.

Result: central **219,760,222,076** CNY, 80% interval [114,466,292,271, 421,910,714,927] CNY, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

Unit of the estimate: CNY (Chinese yuan (CNY); total for 2026-07-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_confirmed**. 2 candidate(s); entity terms none (no entity constraint); measure stems ['chine', 'cny', 'conso', 'opera', 'reven', 'yuan']; 4 point(s) for the target period excluded as dated before the period end or quoted as a forecast
Early checks while the sub-agents were running: 1 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p577 | BYD Q3 2026 estimated per-vehicle consolidated revenue (high end, incl. electronics) | 173,000 | CNY/vehicle | 2026-07-01..2026-09-30 | caifuhao.eastmoney.com | different | This is an estimated per-vehicle revenue figure (a derived ratio), not the consolidated operating revenue total, and it is an estimate rather than a reported ac |
| p576 | BYD Q3 2026 estimated revenue (method 1, low end of range) | 2,220 | CNY | 2026-07-01..2026-09-30 | caifuhao.eastmoney.com | different | This is an estimated range (low end of a forecast range), not a reported actual value, and the unit is stated as CNY rather than the full consolidated revenue f |


## Final answer

Best estimate for BYD Company Limited's consolidated operating revenue for the single quarter 2026-[n]-[n] to 2026-[n]-[n] (Q3 alone, not January-September), as first reported in the unaudited third quarterly report, is 219,760,222,076 CNY (80% model-based interval 114,466,292,271 to 421,910,714,927 CNY).

Main evidence: Q3 volume is derived from official cumulative sales 3,131,576 vehicle less H1 1,808,500 vehicle. Method m1 multiplies that volume by Q2 ex-BYD-Electronic per-vehicle revenue 136,000 CNY/vehicle and adds Q3 BYD Electronic revenue (123,285,000,000 CNY minus 82,234,000,000 CNY). Methods m2 and m3 scale prior-quarter revenue (194,984,598,000 CNY, 194,590,000,000 CNY) by volume ratios (1,114,000 vehicle, 1,108,000 vehicle).

Observed: volumes, prior revenues, electronics revenue. Assumption-dependent: per-vehicle adjustments 1.01, 0.96, 0.96. The three blocks were combined with equal weight per block because their inputs overlap heavily; the interval reflects the blocks' own model-based widths, not demonstrated accuracy.

Key risk: the per-vehicle revenue assumptions, especially electronics revenue per vehicle and export mix. Better evidence would be monthly Q3 revenue or segment disclosures.

Unit of the estimate: CNY (Chinese yuan (CNY); total for 2026-07-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Q3 2026 ASP excluding BYD Electronic relative to Q2 2026 ex-electronics ASP: 1.01 dimensionless, range 0.7125 to 1.425 (range widened by code); used by m1. Overturned by: Reported Q3 2026 automotive revenue per vehicle ex-BYD-Electronic outside roughly [n]k-[n]k CNY/vehicle, or a sharp export/premium mix reversal versus Q2.
- a2 Q3 2026 consolidated revenue per vehicle relative to Q3 2025: 0.96 dimensionless, range 0.6808 to 1.362 (range widened by code); used by m2. Overturned by: Q3 2026 revenue per vehicle materially above Q3 2025, for example if electronics revenue or export ASP surges.
- a3 Q3 2026 consolidated revenue per vehicle relative to Q2 2026: 0.96 dimensionless, range 0.6775 to 1.355 (range widened by code); used by m3. Overturned by: Q3 2026 consolidated revenue per vehicle at or above Q2 2026, or a large upward ASP/mix surprise.

Method details (computed by code):
- m1 formula_mc: (vol_cum - vol_h1) * asp_q2 * a1 + (be_9m - be_h1); Monte Carlo P10 to P90 121,277,448,888 to 366,669,375,657; result unit CNY converted to CNY; own 80% width x/÷1.74 (Monte Carlo of the formula inputs)
- m2 formula_mc: rev_q3_25 * ((vol_cum - vol_h1) / vol_q3_25) * a2; Monte Carlo P10 to P90 100,799,054,723 to 407,288,943,655; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷2.01 (Monte Carlo of the formula inputs)
- m3 formula_mc: rev_q2 * ((vol_cum - vol_h1) / vol_q2) * a3; Monte Carlo P10 to P90 101,605,432,520 to 407,809,255,887; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷2.00 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 219,760,222,076 (width x/÷1.74, Monte Carlo of the formula inputs); B2 = m2: 220,287,835,890 (width x/÷2.01, Monte Carlo of the formula inputs); B3 = m3: 217,816,169,010 (width x/÷2.00, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.92; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.92.

# Evidence ledger: fc_byd_rev_2026_q3

- Question: Assume today is 2026-10-27. You know nothing published after this date. Estimate BYD Company Limited's operating revenue for the three months July-September 2026 (the third quarter alone, not January-September), in Chinese yuan (CNY), as it will be first reported in BYD's unaudited third quarterly report (key accounting data table, 'The Reporting Period' column).
- as_of: 2026-10-27
- Pinned target: BYD Company Limited consolidated operating revenue (营业收入) for the three months 2026-07-01 to 2026-09-30, as first reported in the 'The Reporting Period' column of the key accounting data table of BYD's unaudited Q3 2026 report (A-share/HKEX quarterly report), in CNY | unit CNY | period 2026-07-01..2026-09-30 | publisher BYD Company Limited (002594.SZ / 1211.HK), unaudited third quarterly report

## Directions and pages

### d1 [own_history] BYD's own reported quarterly revenue series and seasonality

Hypothesis: Q3 revenue can be projected from the same quarter in prior years and recent quarters, adjusted for growth trend and seasonality; Q3 2025 and Q2 2026 anchor the level and the QoQ/QoY growth rate.

Queries issued by the searcher: 比亚迪 2025年第三季度报告 营业收入; BYD Q3 2025 revenue third quarterly report 营业收入; 比亚迪 2026年半年度报告 营业收入 上半年; 比亚迪 2026年第一季度报告 营业收入 一季度; 比亚迪 2025年第三季度报告 营业收入; BYD third quarter 2025 results revenue RMB billion; 比亚迪 2026年半年报 营业收入 第二季度; BYD 2026 first quarter results revenue RMB billion Q1 2026; 比亚迪 2025年第三季度报告 营业收入; BYD Q3 2025 revenue third quarterly report 营业收入; 比亚迪 2026年半年报 营业收入 第二季度; 比亚迪 2026年第一季度报告 营业收入 同比

- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=11575623&stockid=002594` -> **live_dated** (page date 2025-10-31); points raw/verified 15/15
  - p1 BYD consolidated operating revenue (营业收入), Q3 2025 (Reporting Period, three mont = **194,984,598,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "\| 营业收入(元) \| 194,984,598,000.00 \| -3.05% \| 566,265,546,000.00 \| 12.75% \|"
  - p2 BYD consolidated operating revenue (营业收入), 9M 2025 (year-to-date to report perio = **566,265,546,000** CNY (2025-01-01..2025-09-30) [DISCARD: 9M 2025 revenue; not needed for Q3 standalone.] quote: "\| 营业收入(元) \| 194,984,598,000.00 \| -3.05% \| 566,265,546,000.00 \| 12.75% \|"
  - p3 BYD consolidated operating revenue (营业收入), 9M 2024 (prior-year comparative, rest = **502,251,312,000** CNY (2024-01-01..2024-09-30) [DISCARD: 9M 2024 revenue; not needed.] quote: "\| 其中:营业收入 \| 566,265,546,000.00 \| 502,251,312,000.00 \|"
  - p4 BYD Q3 2025 operating revenue year-on-year change (本报告期比上年同期增减) = **-3.05** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 revenue change; redundant with p1.] quote: "\| 营业收入(元) \| 194,984,598,000.00 \| -3.05% \| 566,265,546,000.00 \| 12.75% \|"
  - p5 BYD 9M 2025 operating revenue year-on-year change (年初至报告期末比上年同期增减) = **12.75** % (2025-01-01..2025-09-30) [DISCARD: 9M 2025 revenue change; not needed.] quote: "\| 营业收入(元) \| 194,984,598,000.00 \| -3.05% \| 566,265,546,000.00 \| 12.75% \|"
  - p6 BYD consolidated total operating revenue (营业总收入), 9M 2025 = **566,265,546,000** CNY (2025-01-01..2025-09-30) [DISCARD: 9M 2025 total revenue; redundant with p2.] quote: "\| 一、营业总收入 \| 566,265,546,000.00 \| 502,251,312,000.00 \|"
  - p7 BYD consolidated total operating revenue (营业总收入), 9M 2024 (prior-year comparativ = **502,251,312,000** CNY (2024-01-01..2024-09-30) [DISCARD: 9M 2024 revenue; not needed.] quote: "\| 一、营业总收入 \| 566,265,546,000.00 \| 502,251,312,000.00 \|"
  - p8 BYD consolidated operating cost (营业成本), 9M 2025 = **465,053,652,000** CNY (2025-01-01..2025-09-30) [DISCARD: Operating cost; not revenue.] quote: "\| 其中:营业成本 \| 465,053,652,000.00 \| 405,231,798,000.00 \|"
  - p9 BYD consolidated operating cost (营业成本), 9M 2024 (prior-year comparative, restate = **405,231,798,000** CNY (2024-01-01..2024-09-30) [DISCARD: Operating cost; not revenue.] quote: "\| 其中:营业成本 \| 465,053,652,000.00 \| 405,231,798,000.00 \|"
  - p10 BYD net profit attributable to shareholders, Q3 2025 (Reporting Period, three mo = **7,822,640,000** CNY (2025-07-01..2025-09-30) [DISCARD: Q3 2025 net profit; not revenue.] quote: "\| 归属于上市公司股东的净利润(元) \| 7,822,640,000.00 \| -32.60% \| 23,333,173,000.00 \| -7.55% \|"
  - p11 BYD net profit attributable to shareholders, 9M 2025 = **23,333,173,000** CNY (2025-01-01..2025-09-30) [DISCARD: 9M 2025 net profit; not revenue.] quote: "\| 归属于上市公司股东的净利润(元) \| 7,822,640,000.00 \| -32.60% \| 23,333,173,000.00 \| -7.55% \|"
  - p12 BYD net profit attributable to shareholders, 9M 2024 (prior-year comparative, re = **25,238,115,000** CNY (2024-01-01..2024-09-30) [DISCARD: 9M 2024 net profit; not revenue.] quote: "\| 1.归属于母公司股东的净利润(净亏损以"-"号填列) \| 23,333,173,000.00 \| 25,238,115,000.00 \|"
  - p13 BYD basic earnings per share, Q3 2025 (Reporting Period, three months) = **0.85** CNY per share (2025-07-01..2025-09-30) [DISCARD: EPS; not revenue.] quote: "\| 基本每股收益(元/股) \| 0.85 \| -36.09% \| 2.56 \| -11.42% \|"
  - p14 BYD basic earnings per share, 9M 2025 = **2.56** CNY per share (2025-01-01..2025-09-30) [DISCARD: EPS; not revenue.] quote: "\| 基本每股收益(元/股) \| 0.85 \| -36.09% \| 2.56 \| -11.42% \|"
  - p15 BYD total shares outstanding after 2025 bonus share and capital reserve conversi = **9,117,197,565** share (2025-07-01..2025-07-31) [DISCARD: Share count; not needed.] quote: "注:于2025年7月,本公司派发红股2,431,252,684股,资本公积转增股本3,646,879,026股,派发后的发行在外普通股股数为9,117,197,565股。"
- `https://data.eastmoney.com/notices/detail/002594/AN202510301772001473.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://stcn.com/article/detail/3458599.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://newzzbcx.cs.com.cn/cxnews_m.html?random=null&name=new20260829132415vohawgfg` -> **live_dated** (page date 2024-05-16); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/841421040277/index.phtml` -> **live_dated** (page date 2026-08-30); points raw/verified 15/14
  - p16 BYD 2026H1 consolidated operating revenue (营业收入), cumulative = **344,820,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "2026H1 实现营收3,448.2 亿元,同比-7.1%"
  - p17 BYD 2026Q2 consolidated operating revenue (营业收入), three-month = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 实现营收1,945.9 亿元, 同比/ 环比分别-3.2%/+29.5%"
  - p18 BYD 2026Q2 operating revenue YoY change = **-3.2** % (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 实现营收1,945.9 亿元, 同比/ 环比分别-3.2%/+29.5%"
  - p19 BYD 2026Q2 operating revenue QoQ change = **29.5** % (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2 实现营收1,945.9 亿元, 同比/ 环比分别-3.2%/+29.5%"
  - p20 BYD 2026H1 consolidated operating revenue YoY change = **-7.1** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; redundant.] quote: "2026H1 实现营收3,448.2 亿元,同比-7.1%"
  - p21 BYD 2026Q2 passenger vehicle sales volume = **1,108,000** vehicle (2026-04-01..2026-06-30) [DISCARD: Q2 volume; not needed.] quote: "2026Q2乘用车销售110.8 万辆,同比-3.2%,环比+58.2%"
  - p22 BYD 2026Q2 passenger vehicle sales volume QoQ change = **58.2** % (2026-04-01..2026-06-30) [DISCARD: Q2 volume change; not needed.] quote: "2026Q2乘用车销售110.8 万辆,同比-3.2%,环比+58.2%"
  - p23 BYD 2026Q2 export sales volume = **470,000** vehicle (2026-04-01..2026-06-30) [DISCARD: Q2 exports; not needed.] quote: "2026Q2 出口销量47.0 万辆,占比为42.4%"
  - p24 BYD 2026Q2 export share of sales = **42.4** % (2026-04-01..2026-06-30) [DISCARD: Q2 export share; not needed.] quote: "2026Q2 出口销量47.0 万辆,占比为42.4%"
  - p25 BYD 2026Q2 per-vehicle ASP (analyst estimate) = **136,000** CNY/vehicle (2026-04-01..2026-06-30) [DISCARD: Q2 ASP estimate; redundant with p69 for Q3 route.] quote: "经测算,单车ASP 达13.6 万元"
  - p26 BYD 2026Q2 gross profit = **36,740,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Q2 gross profit; not revenue.] quote: "2026Q2 公司毛利润367.4 亿元,环比+30.0%"
  - p27 BYD 2026Q2 gross margin = **18.9** % (2026-04-01..2026-06-30) [DISCARD: Q2 gross margin; not revenue.] quote: "毛利率18.9%,同比+2.6pct,环比+0.1pct"
  - p28 BYD 2026H1 overseas revenue (境外收入) = **181,270,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue; redundant with p157.] quote: "2026H1 公司境外收入1,812.7 亿元,同比+33.9%,占总收入的52.6%"
  - p29 BYD 2026H1 overseas revenue share of total revenue = **52.6** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas share; redundant with p56.] quote: "2026H1 公司境外收入1,812.7 亿元,同比+33.9%,占总收入的52.6%"
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/841757693561/index.phtml` -> **live_dated** (page date 2026-09-03); points raw/verified 15/13
  - p30 BYD consolidated operating revenue, 2026H1 (six months) = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "2026H1:营收 3448.15 亿元(yoy-7.13%)"
  - p31 BYD consolidated operating revenue, 2026Q2 (three months) = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2:营收 1945.90 亿元(yoy-3.15%,qoq+29.53%)"
  - p32 BYD operating revenue year-on-year change, 2026Q2 = **-3.15** % (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2:营收 1945.90 亿元(yoy-3.15%,qoq+29.53%)"
  - p33 BYD operating revenue quarter-on-quarter change, 2026Q2 vs 2026Q1 = **29.53** % (2026-04-01..2026-06-30) [keep: ] quote: "2026Q2:营收 1945.90 亿元(yoy-3.15%,qoq+29.53%)"
  - p34 BYD operating revenue year-on-year change, 2026H1 = **-7.13** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; not needed.] quote: "2026H1:营收 3448.15 亿元(yoy-7.13%)"
  - p35 BYD net profit attributable to parent, 2026H1 = **12,325,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 net profit; not revenue.] quote: "归母净利润 123.25 亿元(yoy-20.54%)"
  - p36 BYD net profit attributable to parent, 2026Q2 = **8,241,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Q2 net profit; not revenue.] quote: "归母净利润 82.41 亿元(yoy+29.66%,qoq+101.74)"
  - p37 BYD gross margin, 2026H1 = **18.85** % (2026-01-01..2026-06-30) [DISCARD: H1 gross margin; not revenue.] quote: "毛利率 18.85%(yoy+0.84pct)"
  - p38 BYD gross margin, 2026Q2 = **18.88** % (2026-04-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率 18.88%(yoy+2.61pct,qoq+0.07pct)"
  - p39 BYD net margin, 2026H1 = **3.58** % (2026-01-01..2026-06-30) [DISCARD: Net margin; not revenue.] quote: "净利率 3.58%(yoy-0.74pct)"
  - p40 BYD net margin, 2026Q2 = **4.28** % (2026-04-01..2026-06-30) [DISCARD: Net margin; not revenue.] quote: "净利率 4.28%(yoy+1.00pct,qoq+1.61pct)"
  - p41 BYD forecast net profit attributable to parent, 2028 (full year) = **51,589,000,000** CNY (2028-01-01..2028-12-31) [DISCARD: 2028 profit forecast; irrelevant.] quote: "我们下修2026、2027、2028 年归母净利润预测至341.93、425.04、515.89 亿元"
  - p42 BYD planned overseas flash-charging stations (plan) = **6,000** station (not stated (page dated 2026-09-03)) [DISCARD: Charging station plan; irrelevant.] quote: "计划在海外布局6,000 座闪充站"
- `https://data.eastmoney.com/report/info/AP202609091829165837.html` -> **live_dated** (page date 2026-09-09); points raw/verified 15/15
  - p43 BYD consolidated operating revenue, H1 2026 (cumulative) = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "2026H1公司营收3448.15亿元、同比-7.1%"
  - p44 BYD consolidated operating revenue, Q2 2026 (single quarter) = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "其中Q2营收1945.90亿元、同比-3.15%"
  - p45 BYD consolidated operating revenue, YoY change, Q2 2026 = **-3.15** % (2026-04-01..2026-06-30) [keep: ] quote: "其中Q2营收1945.90亿元、同比-3.15%"
  - p46 BYD consolidated operating revenue, YoY change, H1 2026 = **-7.1** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; redundant.] quote: "2026H1公司营收3448.15亿元、同比-7.1%"
  - p47 BYD net profit attributable to parent, H1 2026 (cumulative) = **12,325,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "归母净利润123.25亿元、同比-20.5%"
  - p48 BYD net profit attributable to parent, Q2 2026 (single quarter) = **8,241,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "归母净利润82.41亿元、同比+29.7%"
  - p49 BYD gross margin, H1 2026 = **18.8** % (2026-01-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率18.8%、同比+0.8pcts"
  - p50 BYD gross margin, Q2 2026 = **18.9** % (2026-04-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率18.9%、同比+2.6pcts"
  - p51 BYD period expense ratio (total), Q2 2026 = **13.8** % (2026-04-01..2026-06-30) [DISCARD: Expense ratio; not revenue.] quote: "2026Q2公司期间费率合计13.8%"
  - p52 BYD period expense ratio (total), Q1 2026 = **16.2** % (2026-01-01..2026-03-31) [DISCARD: Expense ratio; not revenue.] quote: "较26Q1(16.2%)明显改善"
  - p53 BYD automotive + battery segment revenue, H1 2026 (cumulative) = **275,341,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 auto revenue; redundant with p173.] quote: "2026H1公司汽车+电池板块营收达到2753.41亿元、同比-9.0%"
  - p54 BYD automotive + battery segment revenue, YoY change, H1 2026 = **-9** % (2026-01-01..2026-06-30) [DISCARD: H1 auto change; not needed.] quote: "2026H1公司汽车+电池板块营收达到2753.41亿元、同比-9.0%"
  - p55 BYD overseas revenue, H1 2026 (cumulative) = **181,270,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue; redundant with p157.] quote: "境外收入1812.7亿元、同比+33.9%"
  - p56 BYD overseas revenue share of total revenue, H1 2026 = **52.6** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas share; not needed.] quote: "境外收入1812.7亿元、同比+33.9%,占比达到52.6%"
  - p57 BYD overseas vehicle sales volume, H1 2026 (cumulative) = **792,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 overseas volume; not needed.] quote: "公司海外销量达到79.2万辆、同比+67.8%"
- `https://www.stcn.com/article/detail/3463083.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/002594/AN202608280006758528.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.cnfin.com/announ/detail/index.html?id=841279251474&code=002594` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `https://www.9fzt.com/detail/sz_002594_10_815223727828.html` -> **live_dated** (page date 2025-10-31); points raw/verified 15/0
- `https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/815749732354/index.phtml` -> **live_dated** (page date 2025-11-06); points raw/verified 15/13
  - p58 BYD consolidated operating revenue, Q3 2025 (three months) = **194,985,000,000** CNY (2025-07-01..2025-09-30) [keep: ] quote: "2025Q3,公司实现营业收入1,949.85 亿元,同/环比-3.05%/-2.95%"
  - p59 BYD operating revenue year-on-year change, Q3 2025 vs Q3 2024 = **-3.05** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 revenue change; redundant with p1.] quote: "2025Q3 营业收入1,949.85 亿元,同/环比-3.05%/-2.95%"
  - p60 BYD operating revenue quarter-on-quarter change, Q3 2025 vs Q2 2025 = **-2.95** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 QoQ; not needed.] quote: "2025Q3 营业收入1,949.85 亿元,同/环比-3.05%/-2.95%"
  - p61 BYD net profit attributable to parent, Q3 2025 (three months) = **7,823,000,000** CNY (2025-07-01..2025-09-30) [DISCARD: Q3 2025 net profit; not revenue.] quote: "实现归母净利润78.23 亿元,同/环比-32.60%/+23.07%"
  - p62 BYD net profit attributable to parent year-on-year change, Q3 2025 = **-32.6** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 profit change; not revenue.] quote: "实现归母净利润78.23 亿元,同/环比-32.60%/+23.07%"
  - p63 BYD net profit attributable to parent quarter-on-quarter change, Q3 2025 = **23.07** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 profit change; not revenue.] quote: "实现归母净利润78.23 亿元,同/环比-32.60%/+23.07%"
  - p64 BYD overall gross margin, Q3 2025 = **17.6** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 gross margin; not revenue.] quote: "公司整体毛利率为17.6%。同/ 环比-4.3pct/+1.3pct"
  - p65 BYD automobile business gross margin, Q3 2025 = **20.6** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 auto gross margin; not revenue.] quote: "汽车业务毛利率为20.6% , 同/ 环比-5.4pct/+1.9pct"
  - p66 BYD vehicle sales volume, Q3 2025 (three months) = **1,114,200** vehicle (2025-07-01..2025-09-30) [DISCARD: Q3 2025 volume; not needed as separate input.] quote: "2025Q3 公司汽车销量111.42 万辆,同/环比-1.8%/-2.7%"
  - p67 BYD vehicle sales volume year-on-year change, Q3 2025 = **-1.8** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 volume change; not needed.] quote: "2025Q3 公司汽车销量111.42 万辆,同/环比-1.8%/-2.7%"
  - p68 BYD vehicle sales volume quarter-on-quarter change, Q3 2025 = **-2.7** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 volume change; not needed.] quote: "2025Q3 公司汽车销量111.42 万辆,同/环比-1.8%/-2.7%"
  - p69 BYD revenue per vehicle sold, Q3 2025 = **136,700** CNY/vehicle (2025-07-01..2025-09-30) [DISCARD: Q3 2025 ASP; used only via p1/p66 consistency, not needed as separate input.] quote: "当季单车收入为13.67 万元,同/环比-0.22pct/-0.06pct"
  - p70 BYD net profit per vehicle sold, Q3 2025 = **6,200** CNY/vehicle (2025-07-01..2025-09-30) [DISCARD: Q3 2025 profit per vehicle; not revenue.] quote: "单车盈利0.62 万元,环比+0.13 万元"
- dropped by code checks: 20 (scale word '亿' not supported by quote or table header: 5; period year 2025 does not appear in the page text or URL (likely mis-dated): 15)

### d2 [physical_flow] Vehicle unit sales as the dominant revenue driver

Hypothesis: Revenue ≈ (vehicle units sold in Q3 2026 × average revenue per vehicle) + non-vehicle segment revenue; Q3 2026 monthly wholesale sales are published and can be multiplied by an ASP derived from historical revenue/unit.

Queries issued by the searcher: 比亚迪 2026年9月 产销快报 销量; BYD September 2026 sales figures NEV; 比亚迪 2026年8月 产销快报 新能源汽车销量; 比亚迪 2026年7月 产销快报 销量 同比; 比亚迪 2026年9月 产销快报 销量; BYD September 2026 sales figures; 比亚迪 2026年8月 产销快报 销量 新能源汽车; 比亚迪 2026年7月 产销快报 销量; 比亚迪 2026年9月 产销快报 销量; BYD September 2026 sales figures; 比亚迪 2026年8月产销快报 销量 新能源汽车; 比亚迪 2026年7月产销快报 销量 同比

- `https://www.cnfin.com/announ/detail/index.html?id=841609872904&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/company/rptid/845640780089/index.phtml` -> **live_dated** (page date 2026-10-18); points raw/verified 15/13
  - p71 BYD September 2026 total vehicle sales (wholesale, 汽车销量) = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月汽车销量463561 辆,同比增长17%,环比增长5.3%"
  - p72 BYD September 2026 NEV passenger vehicle sales (新能源乘用车销量) = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月新能源乘用车销量456713 辆,同比增长16.2%,环比增长5.4%"
  - p73 BYD September 2026 BEV passenger vehicle sales (纯电动乘用车销量) = **273,143** vehicle (2026-09-01..2026-09-30) [DISCARD: BEV split; not needed.] quote: "其中9 月纯电动乘用车销量273143 辆,同比增长33.2%"
  - p74 BYD September 2026 PHEV passenger vehicle sales (插混乘用车销量) = **183,570** vehicle (2026-09-01..2026-09-30) [DISCARD: PHEV split; not needed.] quote: "插混乘用车销量183570 辆,同比下降2.4%"
  - p75 BYD year-to-date 2026 cumulative vehicle sales (今年累计汽车销量) = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计汽车销量3131576 辆,同比下降3.9%"
  - p76 BYD year-to-date 2026 cumulative passenger vehicle sales (今年累计乘用车销量) = **3,078,544** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative PV; redundant with p465.] quote: "今年累计乘用车销量3078544 辆,同比下降4.4%"
  - p77 BYD September 2026 domestic sales (9月国内销量) = **283,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月国内销量28.3 万辆,同比下降13%,环比增长12.8%"
  - p78 BYD year-to-date 2026 cumulative domestic sales (今年累计国内销量) = **1,789,000** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative domestic; redundant with p469.] quote: "今年累计国内销量178.9 万辆,同比下降30%"
  - p79 BYD September 2026 NEV exports (9月新能源汽车出口) = **181,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p80 BYD September 2026 export share of NEV sales (销量占比) = **39** % (2026-09-01..2026-09-30) [DISCARD: Export share; not needed.] quote: "销量占比39%,同比提升21pcts"
  - p81 BYD September 2026 Dynasty and Ocean network sales (王朝与海洋网合计) = **395,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Dynasty/Ocean; not needed.] quote: "9 月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p82 BYD September 2026 premium brand sales combined (腾势/方程豹/仰望三个高端品牌合计) = **62,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Premium brands; not needed.] quote: "腾势/方程豹/仰望三个高端品牌合计6.2 万辆(同比+65.7%),占乘用车销量13.5%"
  - p83 BYD September 2026 premium brands share of passenger vehicle sales (占乘用车销量) = **13.5** % (2026-09-01..2026-09-30) [DISCARD: Premium share; not needed.] quote: "占乘用车销量13.5%,同比提升4pcts"
- `https://www.cnfin.com/announ/detail/index.html?id=844705253353&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?CompanyCode=10002250&gather=1&id=12631418` -> **live_dated** (page date 2026-10-08); points raw/verified 10/8
  - p84 BYD September 2026 NEV sales (wholesale, monthly) = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
  - p85 BYD cumulative NEV sales Jan-Sep 2026 (year-to-date) = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
  - p86 BYD September 2026 passenger vehicle sales (wholesale, monthly) = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| -乘用车 \| 458,116 \| 402,008 \| 3,087,782 \| 3,171,466 \| -2.64% \| 456,713 \| 393,060 \| 3,078,544 \| 3,218,862 \| -4.36% \|"
  - p87 BYD September 2026 battery electric passenger vehicle sales (wholesale, monthly) = **273,143** vehicle (2026-09-01..2026-09-30) [DISCARD: BEV split; not needed.] quote: "\| -纯电动 \| 274,403 \| 204,838 \| 1,636,015 \| 1,578,176 \| 3.66% \| 273,143 \| 205,050 \| 1,629,957 \| 1,605,903 \| 1.50% \|"
  - p88 BYD September 2026 plug-in hybrid passenger vehicle sales (wholesale, monthly) = **183,570** vehicle (2026-09-01..2026-09-30) [DISCARD: PHEV split; not needed.] quote: "\| -插电式混合动力 \| 183,713 \| 197,170 \| 1,451,767 \| 1,593,290 \| -8.88% \| 183,570 \| 188,010 \| 1,448,587 \| 1,612,959 \| -10.19% \|"
  - p89 BYD September 2026 commercial vehicle sales (wholesale, monthly) = **6,848** vehicle (2026-09-01..2026-09-30) [DISCARD: Commercial split; not needed.] quote: "\| -商用车 \| 5,748 \| 3,546 \| 51,164 \| 42,103 \| 21.52% \| 6,848 \| 3,210 \| 53,032 \| 41,284 \| 28.46% \|"
  - p90 BYD September 2026 NEV exports (monthly) = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "注:本公司2026年9月出口新能源汽车合计180,700辆。"
  - p91 BYD cumulative NEV sales Jan-Sep 2026 year-on-year change = **-3.94** % (2026-01-01..2026-09-30) [DISCARD: Cumulative change; redundant with p384.] quote: "\| 新能源汽车 \| 463,864 \| 405,554 \| 3,138,946 \| 3,213,569 \| -2.32% \| 463,561 \| 396,270 \| 3,131,576 \| 3,260,146 \| -3.94% \|"
- `https://data.eastmoney.com/notices/detail/002594/AN202610071830185793.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://paper.cnstock.com/html/2026-10/08/content_2274628.htm` -> **live_dated** (page date 2026-10-08); points raw/verified 1/1
  - p92 BYD September 2026 export total of new energy vehicles (cumulative for the month = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "注:本公司2026年9月出口新能源汽车合计180,700辆。"
- `https://data.eastmoney.com/notices/detail/002594/AN202609011828888163.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://autonews.gasgoo.com/articles/news/2107803611743870977` -> **live_dated** (page date 2026-10-07); points raw/verified 11/11
  - p93 BYD total new vehicle sales, September 2026 = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "it sold 463,561 new vehicles in September 2026, including 456,713 passenger vehicles."
  - p94 BYD passenger vehicle sales, September 2026 = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "it sold 463,561 new vehicles in September 2026, including 456,713 passenger vehicles."
  - p95 BYD Dynasty and Ocean series combined sales, September 2026 = **394,945** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "BYD's Dynasty and Ocean series remained its main volume contributors, with combined September sales of 394,945 vehicles."
  - p96 FANGCHENGBAO sales, September 2026 = **43,181** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "FANGCHENGBAO sold 43,181 vehicles during the month, while DENZA recorded 18,198 units and YANGWANG sold 389 units."
  - p97 DENZA sales, September 2026 = **18,198** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "FANGCHENGBAO sold 43,181 vehicles during the month, while DENZA recorded 18,198 units and YANGWANG sold 389 units."
  - p98 YANGWANG sales, September 2026 = **389** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "FANGCHENGBAO sold 43,181 vehicles during the month, while DENZA recorded 18,198 units and YANGWANG sold 389 units."
  - p99 BYD overseas sales of passenger vehicles and pickup trucks, September 2026 = **179,877** vehicle (2026-09-01..2026-09-30) [DISCARD: Overseas sales; redundant with p106.] quote: "Overseas sales of BYD passenger vehicles and pickup trucks reached 179,877 units in September, up 153.9% year on year."
  - p100 BYD overseas sales of passenger vehicles and pickup trucks, year-on-year growth, = **154** % (2026-09-01..2026-09-30) [DISCARD: Overseas growth; not needed.] quote: "Overseas sales of BYD passenger vehicles and pickup trucks reached 179,877 units in September, up 153.9% year on year."
  - p101 BYD overseas sales of passenger vehicles and pickup trucks, January–September 20 = **1,337,831** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative overseas; redundant with p109.] quote: "Their January-September total stood at 1,337,831 units."
  - p102 BYD total vehicle sales, first nine months of 2026 cumulative = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "BYD Company Limited sold 3,131,576 vehicles in the first nine months of 2026."
  - p103 BYD cumulative new energy vehicle sales as of September 2026 = **18,200,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Cumulative NEV; irrelevant.] quote: "As of Sept. this year, its cumulative new energy vehicle sales had surpassed 18.2 million units."
- `https://finance.yahoo.com/news/byd-global-sales-rise-17-121750216.html` -> **live_dated** (page date 2026-10-08); points raw/verified 14/13
  - p104 BYD global NEV sales, September 2026 = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "BYD Auto has reported a 17% rise in global sales to 463,561 units in September 2026"
  - p105 BYD domestic sales, September 2026 = **282,861** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "Domestic sales fell by 13% year-on-year to 282,861 units in September"
  - p106 BYD overseas sales of passenger vehicles and pickup trucks, September 2026 = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "overseas sales of passenger vehicles and pickup trucks surged by 154% to 180,700 vehicles"
  - p107 BYD global sales, first nine months of 2026 (cumulative) = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "In the first nine months of 2026, BYD sold a total of 3,131,576 vehicles globally"
  - p108 BYD domestic sales, first nine months of 2026 (cumulative) = **1,788,616** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "domestic sales plunging by 33% to 1,788,616 units"
  - p109 BYD overseas sales, first nine months of 2026 (cumulative) = **1,342,960** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "overseas sales surged by 92% to 1,342,960 units to account for 43% of total vehicle sales"
  - p110 Overseas share of BYD total vehicle sales, first nine months of 2026 = **43** % (2026-01-01..2026-09-30) [DISCARD: Overseas share; not needed.] quote: "to account for 43% of total vehicle sales"
  - p111 BYD overseas sales, prior cumulative period (as stated) = **697,072** vehicle (not stated (page dated 2026-10-08)) [DISCARD: Prior overseas; not needed.] quote: "after having grown by 134% to 697,072 units previously"
  - p112 BYD passenger and pickup BEV sales, first nine months of 2026 (cumulative) = **1,629,957** vehicle (2026-01-01..2026-09-30) [DISCARD: BEV cumulative; not needed.] quote: "Global sales of passenger and pickup battery electric vehicles (BEV) rose by 1.5% to 1,629,957 units year-to-date"
  - p113 BYD passenger and pickup PHEV sales, first nine months of 2026 (cumulative) = **1,448,587** vehicle (2026-01-01..2026-09-30) [DISCARD: PHEV cumulative; not needed.] quote: "sales of passenger and pickup plug-in-hybrid vehicles (PHEVs) fell by 10% to 1,448,587 units"
  - p114 BYD commercial vehicle sales, first nine months of 2026 (cumulative) = **53,032** vehicle (2026-01-01..2026-09-30) [DISCARD: Commercial cumulative; not needed.] quote: "Commercial vehicle sales rose by over 28% to 53,032 units in this period."
  - p115 BYD target overseas sales, 2027 (plan) = **2,500,000** vehicle (2027-01-01..2027-12-31) [DISCARD: 2027 target; irrelevant.] quote: "BYD has set a target of further increasing its overseas sales to 2.5 million vehicles in 2027"
  - p116 BYD expected overseas sales, 2026 (expectation) = **2,000,000** vehicle (2026-01-01..2026-12-31) [DISCARD: 2026 expectation; not needed.] quote: "up from an expected 2.0 million units in 2026"
- `https://big5.askci.com/news/data/qiye/20261008/101919279142595981222461.shtml` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.askci.com/news/data/qiye/20260907/095822278874630241852067.shtml` -> **live_dated** (page date 2026-09-07); points raw/verified 13/13
  - p117 BYD new energy vehicle (NEV) sales, August 2026, monthly wholesale = **440,300** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug sales; redundant with p491.] quote: "2026年8月,比亚迪新能源汽车产量44.07万辆,同比增长24.81%。销量44.03万辆,同比增长17.84%。"
  - p118 BYD NEV sales, August 2026, year-on-year growth rate = **17.84** % (2026-08-01..2026-08-31) [DISCARD: Aug growth; not needed.] quote: "销量44.03万辆,同比增长17.84%。"
  - p119 BYD NEV production, August 2026 = **440,700** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug production; not needed.] quote: "2026年8月,比亚迪新能源汽车产量44.07万辆,同比增长24.81%。"
  - p120 BYD NEV cumulative sales, January-August 2026 = **2,668,000** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative Aug; not needed.] quote: "2026年1-8月,比亚迪新能源汽车累计产量267.51万辆,同比减少4.73%。累计销量266.80万辆,同比减少6.84%。"
  - p121 BYD NEV cumulative sales, January-August 2026, year-on-year change = **6.84** % (2026-01-01..2026-08-31) [DISCARD: Cumulative Aug change; not needed.] quote: "累计销量266.80万辆,同比减少6.84%。"
  - p122 BYD NEV cumulative production, January-August 2026 = **2,675,100** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative production; not needed.] quote: "2026年1-8月,比亚迪新能源汽车累计产量267.51万辆,同比减少4.73%。"
  - p123 BYD new energy passenger vehicle sales, August 2026 = **433,400** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug PV; redundant with p524.] quote: "2026年8月,比亚迪新能源乘用车产量43.36万辆,同比增长23.50%。销量43.34万辆,同比增长16.66%。"
  - p124 BYD new energy passenger vehicle sales, August 2026, year-on-year growth rate = **16.66** % (2026-08-01..2026-08-31) [DISCARD: Aug PV growth; not needed.] quote: "销量43.34万辆,同比增长16.66%。"
  - p125 BYD new energy passenger vehicle cumulative sales, January-August 2026 = **2,621,800** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative PV; not needed.] quote: "2026年1-8月,比亚迪新能源乘用车累计产量262.97万辆,同比减少5.05%。累计销量262.18万辆,同比减少7.22%。"
  - p126 BYD new energy passenger vehicle cumulative sales, January-August 2026, year-on- = **7.22** % (2026-01-01..2026-08-31) [DISCARD: Cumulative PV change; not needed.] quote: "累计销量262.18万辆,同比减少7.22%。"
  - p127 BYD new energy commercial vehicle sales, August 2026 = **6,909** vehicle (2026-08-01..2026-08-31) [DISCARD: Commercial; not needed.] quote: "2026年8月,比亚迪新能源商用车产量7129辆,同比增长254.68%。销量6909辆,同比增长225.13%。"
  - p128 BYD new energy commercial vehicle cumulative sales, January-August 2026 = **46,200** vehicle (2026-01-01..2026-08-31) [DISCARD: Commercial cumulative; not needed.] quote: "2026年1-8月,比亚迪新能源商用车累计产量4.54万辆,同比增长17.79%。累计销量4.62万辆,同比增长21.30%。"
  - p129 BYD new energy commercial vehicle cumulative sales, January-August 2026, year-on = **21.3** % (2026-01-01..2026-08-31) [DISCARD: Commercial growth; not needed.] quote: "累计销量4.62万辆,同比增长21.30%。"
- `https://stock.finance.sina.com.cn/stock/view/paper.php?symbol=sh000001&reportid=845350343886` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- dropped by code checks: 5 (scale word '万' not supported by quote or table header: 1; scale word '亿' not supported by quote or table header: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 3)

### d3 [related_series] Segment split: automobiles vs BYD Electronic vs other

Hypothesis: Total revenue = automotive and related products revenue + phone components/assembly (BYD Electronic) revenue + other; BYD Electronic reports its own quarterly revenue (HKD) which can be converted and added to an automotive estimate.

Queries issued by the searcher: 比亚迪电子 2026 第三季度 营收; BYD Electronic Q3 2026 revenue; 比亚迪 2026 半年报 营业收入 汽车 手机部件及组装 分部 占比; 比亚迪 2026年第三季度报告 披露时间 营业收入; 比亚迪电子 2026 第三季度 营收; BYD Electronic Q3 2026 revenue quarterly results; 比亚迪 2026年三季报 营业收入 第三季度; 比亚迪 2026年半年报 营业收入 汽车 手机部件 分部; 比亚迪电子 2026 第三季度 营收; BYD Electronic Q3 2026 revenue; 比亚迪 2026年三季报 营业收入 第三季度 披露时间; 比亚迪 2026年半年报 汽车 手机部件 组装 营业收入 分部

- `http://hk.stockstar.com/IG2026090100015216.shtml` -> **live_dated** (page date 2026-09-01); points raw/verified 15/15
  - p130 BYD Electronic (00285.HK) H1 2026 revenue = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 electronics revenue; redundant with p536.] quote: "比亚迪电子(00285.HK)2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p131 BYD Electronic H1 2026 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics profit; not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p132 BYD Electronic H1 2026 gross margin (year-on-year change) = **1.97** percentage points (2026-01-01..2026-06-30) [DISCARD: Electronics margin; not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p133 BYD Electronic H1 2026 gross margin level = **4.91** % (2026-01-01..2026-06-30) [DISCARD: Electronics margin; not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p134 BYD Electronic H1 2026 smart terminal business revenue = **67,348,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "2026H1智能终端业务收入673.48亿元,同比增长约1.4%"
  - p135 BYD Electronic H1 2026 assembly business revenue = **55,522,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "其中组装业务收入555.22亿元,同比增长约5.1%"
  - p136 BYD Electronic H1 2026 component business revenue = **11,826,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "零部件业务收入118.26亿元,同比下降约13.3%"
  - p137 BYD Electronic H1 2026 new energy vehicle business revenue = **13,515,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "2026H1新能源汽车业务收入135.15亿元,同比增长6.4%"
  - p138 BYD Electronic H1 2026 AI computing infrastructure revenue = **751,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "AI算力基础设施方面,2026H1实现收入7.51亿元,同比下降9.74%"
  - p139 BYD Electronic full-year 2026 server business revenue forecast (at least) = **3,000,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Server forecast; not needed.] quote: "服务器业务全年收入预计达30亿元以上"
  - p140 BYD Electronic planned liquid-cooling products to enter mass production in Q4 20 = **3.5** (range 3..4) as written "3-4", value check pending product (2026-10-01..2026-12-31) [DISCARD: Product count; irrelevant.] quote: "另有3-4款液冷产品计划于Q4陆续量产"
  - p141 CSC forecast BYD Electronic 2026 revenue = **181,086,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year electronics forecast; not Q3.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p142 CSC forecast BYD Electronic 2027 revenue = **199,602,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 electronics forecast; irrelevant.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p143 CSC forecast BYD Electronic 2026 net profit attributable to parent = **2,156,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Electronics profit forecast; not revenue.] quote: "归母净利润分别为21.56亿元和36.27亿元"
  - p144 CSC target price for BYD Electronic (HKD) = **29.78** HKD (not stated (page dated 2026-09-01)) [DISCARD: Target price; irrelevant.] quote: "维持"买入"评级,给予目标价29.78港元,对应2027年16倍PE"
- `https://www.163.com/dy/article/L97FJB4U05198ETO.html` -> **live_dated** (page date 2026-10-14); points raw/verified 2/2
  - p145 BYD Electronic board meeting date to approve unaudited Q3 results for nine month = **20,261,029** as written "2026年10月29日", value check pending date (2026-10-29..2026-10-29) [DISCARD: Board meeting date; redundant with p533.] quote: "谨定于2026年10月29日(星期四)举行董事会会议,以考虑及批准(其中包括)公司截至2026年9月30日止九个月之未经审核第三季度业绩及其发布"
  - p146 BYD Electronic reporting period end for unaudited Q3/nine-month results = **20,260,930** as written "2026年9月30日", value check pending date (2026-09-30..2026-09-30) [DISCARD: Period end; redundant with p534.] quote: "公司截至2026年9月30日止九个月之未经审核第三季度业绩及其发布"
- `https://www.finanzen.net/schaetzungen/byd_electronic` -> **dropped** (live http 403); points raw/verified -/-
- `https://basic.10jqka.com.cn/00285/` -> **live_dated** (page date 2026-06-30); points raw/verified 15/6
  - p147 BYD Electronic H1 2026 sales revenue YoY growth = **2.02** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics growth; redundant with p537.] quote: "二零二六年上半年,集团录得销售额约人民币82,234百万元,同比上升约2.02%。"
  - p148 BYD Electronic H1 2026 NEV segment share of group total revenue = **16.56** % (2026-01-01..2026-06-30) [DISCARD: Electronics NEV share; not needed.] quote: "期内,集团新能源汽车业务板块的收入约人民币13,619百万元,占集团总体收入约16.56%,收入同比上升约6.43%。"
  - p149 BYD Electronic H1 2026 NEV segment revenue YoY growth = **6.43** % (2026-01-01..2026-06-30) [DISCARD: Electronics NEV growth; not needed.] quote: "占集团总体收入约16.56%,收入同比上升约6.43%。"
  - p150 BYD Electronic H1 2026 AI computing infrastructure segment revenue YoY change = **10.57** % (2026-01-01..2026-06-30) [DISCARD: Electronics AI growth; not needed.] quote: "集团的AI算力基础设施业务板块录得收入约为人民币753百万元,同比下降约10.57%。"
  - p151 BYD Electronic H1 2026 profit attributable to shareholders YoY decline = **75.35** % (2026-01-01..2026-06-30) [DISCARD: Electronics profit decline; not revenue.] quote: "股东应占溢利同比下降约75.35%至约人民币426百万元"
  - p152 Global smartphone shipments H1 2026 (IDC) = **571,000,000** unit (2026-01-01..2026-06-30) [DISCARD: Smartphone shipments; irrelevant.] quote: "根据IDC的统计,二零二六年上半年全球智能手机出货量按年下跌4.8%至5.71亿部。"
- `https://il.investing.com/equities/byd-electronic-earnings` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.tipranks.com/stocks/hk:0285/revenue` -> **dropped** (live http 403); points raw/verified -/-
- `http://202.62.215.11/www/tc//stocks/realtime/quote_news_detail.php?section=related&code=00285&newsid=ETN360829306` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://stockanalysis.com/quote/hkg/0285/statistics/` -> **live_dated** (page date 2026-10-27); points raw/verified 15/0
- `https://fund.eastmoney.com/a/202608293858858516.html` -> **live_dated** (page date 2026-08-29); points raw/verified 15/15
  - p153 BYD consolidated operating revenue, H1 2026, year-on-year change = **7.13** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; redundant with p34.] quote: "2026年上半年,比亚迪的营业收入、归母净利润、扣非后净利润,同比分别下降7.13%、20.54%、9.02%。"
  - p154 BYD automotive business revenue, H1 2026, year-on-year change = **8.98** % (2026-01-01..2026-06-30) [DISCARD: H1 segment change; redundant with p175/p172.] quote: "2026年上半年,比亚迪汽车业务的收入同比下降8.98%,电子及其他产品业务的收入同比增长0.96%。"
  - p155 BYD electronics and other products business revenue, H1 2026, year-on-year chang = **0.96** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics change; redundant with p172.] quote: "2026年上半年,比亚迪汽车业务的收入同比下降8.98%,电子及其他产品业务的收入同比增长0.96%。"
  - p156 BYD automotive business share of total revenue (approximate, as stated) = **80** as written "八成左右", value check pending % (automotive revenue / total revenue) (2026-01-01..2026-06-30) [DISCARD: Approximate share; redundant with p174.] quote: "比亚迪的营业收入主要来自汽车业务、电子及其他产品业务,其中汽车业务的收入占比在八成左右。"
  - p157 BYD overseas (outside mainland China) revenue, H1 2026 = **181,268,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue; not needed for Q3.] quote: "2026年上半年,比亚迪的境外收入同比增长33.92%至1812.68亿元,境内收入同比下降30.68%至1635.47亿元。"
  - p158 BYD overseas revenue, H1 2026, year-on-year change = **33.92** % (2026-01-01..2026-06-30) [DISCARD: H1 overseas revenue change; not needed.] quote: "2026年上半年,比亚迪的境外收入同比增长33.92%至1812.68亿元,境内收入同比下降30.68%至1635.47亿元。"
  - p159 BYD domestic (mainland China) revenue, H1 2026 = **163,547,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 domestic revenue; not needed.] quote: "2026年上半年,比亚迪的境外收入同比增长33.92%至1812.68亿元,境内收入同比下降30.68%至1635.47亿元。"
  - p160 BYD domestic revenue, H1 2026, year-on-year change = **30.68** % (2026-01-01..2026-06-30) [DISCARD: H1 domestic revenue change; not needed.] quote: "2026年上半年,比亚迪的境外收入同比增长33.92%至1812.68亿元,境内收入同比下降30.68%至1635.47亿元。"
  - p161 BYD overseas revenue share of total revenue, H1 2026 (stated as first time above = **50** % (2026-01-01..2026-06-30) [DISCARD: Approximate share; redundant with p56.] quote: "2026年上半年,比亚迪的境外收入首次超过境内收入,并且境外收入占总收入的比例首次超50%。"
  - p162 BYD automotive business gross margin, H1 2026 = **22.33** % (2026-01-01..2026-06-30) [DISCARD: Auto gross margin; not revenue.] quote: "这助力比亚迪的汽车业务毛利率,在2026年上半年同比上升1.98个百分点至22.33%。"
  - p163 BYD automotive business gross margin, H1 2026, year-on-year change in percentage = **1.98** percentage points (2026-01-01..2026-06-30) [DISCARD: Auto gross margin change; not revenue.] quote: "这助力比亚迪的汽车业务毛利率,在2026年上半年同比上升1.98个百分点至22.33%。"
  - p164 BYD vehicle sales, H1 2026, year-on-year change = **15.72** % (2026-01-01..2026-06-30) [DISCARD: H1 volume change; not needed.] quote: "2026年上半年,比亚迪的汽车销量同比下降15.72%,其中主要是国内汽车销量大幅下降。"
  - p165 BYD vehicle exports, H1 2026 = **792,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 exports; not needed.] quote: "根据中汽协数据,2026年上半年,比亚迪的汽车出口同比增长67.8%至79.2万辆,占总销量的比重大幅跃升。"
  - p166 BYD vehicle exports, H1 2026, year-on-year change = **67.8** % (2026-01-01..2026-06-30) [DISCARD: H1 export change; not needed.] quote: "根据中汽协数据,2026年上半年,比亚迪的汽车出口同比增长67.8%至79.2万辆,占总销量的比重大幅跃升。"
  - p167 BYD R&D expenditure (研发投入), H1 2026 = **28,861,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: R&D spend; not revenue.] quote: "2026年上半年,比亚迪的研发投入同比下降6.54%至288.61亿元,但比亚迪没有在2026年半年报中提及原因。"
- `https://emweb.securities.eastmoney.com/BusinessAnalysis/Index?code=sz002594` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- `http://stocks.etnet.hk/www/sc/stocks/realtime/quote_ci_detail.php?code=1211` -> **live_dated** (page date 2026-10-27); points raw/verified 15/15
  - p168 BYD Group revenue, first six months of 2026 (H1 2026), PRC GAAP = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "截至2026年6月止六个月,集团营业额下降7.1%至3448.15亿元(人民币 ;下同)"
  - p169 BYD Group revenue year-on-year change, H1 2026 = **7.1** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; redundant.] quote: "截至2026年6月止六个月,集团营业额下降7.1%至3448.15亿元"
  - p170 BYD electronics and other products segment revenue, H1 2026 = **69,405,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 electronics revenue; redundant with p130.] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%"
  - p171 BYD electronics and other products segment share of total revenue, H1 2026 = **20.1** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics share; not needed.] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%"
  - p172 BYD electronics and other products segment revenue year-on-year change, H1 2026 = **1** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics change; redundant with p147.] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%"
  - p173 BYD automotive, auto-related products and other products segment revenue, H1 202 = **275,341,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 auto revenue; not needed for Q3.] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元,占总营业额79.9%"
  - p174 BYD automotive, auto-related products and other products segment share of total  = **79.9** % (2026-01-01..2026-06-30) [DISCARD: H1 auto share; not needed.] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元,占总营业额79.9%"
  - p175 BYD automotive, auto-related products and other products segment revenue year-on = **9** % (2026-01-01..2026-06-30) [DISCARD: H1 auto change; redundant with p54.] quote: "汽车、汽车相关产品及其他产品:营业额下降9%至2753.41亿元,占总营业额79.9%"
  - p176 BYD Group gross profit, H1 2026 = **64,989,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Gross profit; not revenue.] quote: "整体毛利下降2.8%至649.89亿元,毛利率则上升0.8个百分点至18.9%"
  - p177 BYD Group gross margin, H1 2026 = **18.9** % (2026-01-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "整体毛利下降2.8%至649.89亿元,毛利率则上升0.8个百分点至18.9%"
  - p178 BYD Group gross profit year-on-year change, H1 2026 = **2.8** % (2026-01-01..2026-06-30) [DISCARD: Gross profit change; not revenue.] quote: "整体毛利下降2.8%至649.89亿元,毛利率则上升0.8个百分点至18.9%"
  - p179 BYD Group gross margin change, H1 2026 = **0.8** percentage points (2026-01-01..2026-06-30) [DISCARD: Gross margin change; not revenue.] quote: "毛利率则上升0.8个百分点至18.9%"
  - p180 BYD Group profit attributable to shareholders, H1 2026 = **12,295,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "股东应占溢利下跌19.7%至122.95亿元"
  - p181 BYD Group profit attributable to shareholders year-on-year change, H1 2026 = **19.7** % (2026-01-01..2026-06-30) [DISCARD: Net profit change; not revenue.] quote: "股东应占溢利下跌19.7%至122.95亿元"
  - p182 BYD electronics and other products segment total profit, H1 2026 = **194,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Segment profit; not revenue.] quote: "电子及其他产品:营业额上升1%至694.05亿元,占总营业额20.1%,利润总额则减少 85.5%至1.94亿元"
- `https://www.itiger.com/hant/news/1153614644` -> **live_dated** (page date 2026-08-28); points raw/verified 14/5
  - p183 BYD Company H1 2026 revenue year-on-year change = **7.13** % (2026-01-01..2026-06-30) [DISCARD: H1 revenue change; redundant.] quote: "上半年實現營收3448.15億元,按年下降7.13%"
  - p184 BYD Company H1 2026 gross margin = **18.85** % (2026-01-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率從上年同期的18.01%提升至18.85%"
  - p185 BYD Company H1 2026 employee cost as share of revenue = **17.9** % (2026-01-01..2026-06-30) [DISCARD: Employee cost share; not revenue.] quote: "員工成本投入佔比約為17.9%"
  - p186 BYD automotive and related products segment H1 2026 revenue year-on-year change = **8.98** % (2026-01-01..2026-06-30) [DISCARD: H1 auto change; redundant with p175.] quote: "汽車及相關產品業務實現營收2753.41億元,按年下降8.98%"
  - p187 BYD electronics and other products segment H1 2026 revenue year-on-year change = **0.96** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics change; redundant with p172.] quote: "電子及其他產品業務錄得營收694.05億元,按年微增0.96%"
- dropped by code checks: 33 (scale word 'million' not supported by quote or table header: 9; value_as_written not in quote as a whole number: 3; period_end missing or unparseable: 12; number: value_as_written is only part of a larger CJK number in the quote: 8; period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d4 [forecasts_markets] Sell-side consensus and company guidance for Q3 2026

Hypothesis: Analyst consensus revenue estimates for BYD Q3 2026 provide an independent anchor; consensus typically tracks reported sales and ASP trends.

Queries issued by the searcher: BYD Q3 2026 revenue consensus estimate analysts; 比亚迪 2026年 三季度 营收 一致预期 预测; 比亚迪 2026年9月 销量 三季度 累计销量 公告; BYD September 2026 sales volume third quarter 2026 deliveries record; 比亚迪 2026 三季度 营收 预测 一致预期; BYD Q3 2026 revenue consensus estimate; 比亚迪 2026年9月 销量 三季度 销量 公告; 比亚迪 2026 销量目标 营收 指引; 比亚迪 2026年 三季度 营收 一致预期; BYD Q3 2026 revenue consensus estimate analysts; 比亚迪 2026年 销量目标 550万辆 营收 指引; BYD third quarter 2026 results preview revenue forecast October 2026

- `https://wwwhk.aastocks.com/en/stocks/news/aafn-con/NOW.1549400/popular-news/AAFN` -> **live_dated** (page date 2026-10-15); points raw/verified 15/12
  - p188 Goldman Sachs forecast BYD 3Q26 revenue = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p189 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p190 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p191 Goldman Sachs forecast BYD 3Q26 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p192 Goldman Sachs forecast BYD 3Q26 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p193 Goldman Sachs forecast BYD 3Q26 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p194 Goldman Sachs forecast BYD 3Q26 sales volume growth YoY and QoQ = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p195 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p196 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p197 BYD Hungary plant planned annual capacity = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Hungary capacity; not realised output.] quote: "Hungary plant is expected to commence production by the end of 2026 with planned annual capacity of 300,000 vehicles"
  - p198 China NEV export VAT rebate rate before 2027-04-01 = **13** % (..2027-03-31) [DISCARD: VAT rate; irrelevant.] quote: "the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p199 Goldman Sachs assumed cost pass-through of VAT rebate cut = **67** % (not stated (page dated 2026-10-15)) [DISCARD: VAT pass-through; irrelevant.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- `https://in.investing.com/equities/byd-a-earnings?pageNum=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://beta.finance.yahoo.com/quote/0VSO.L/analysis/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://hk.finance.yahoo.com/quote/81211.HK/analysis/` -> **dropped** (live http 503); points raw/verified -/-
- `https://sg.finance.yahoo.com/quote/0HKY.L/analysis/` -> **dropped** (live http 503); points raw/verified -/-
- `https://www.moomoocn.com/hans/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.moomooapp.com/hant/stock/002594-SZ/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://za.investing.com/equities/byd-co.-earnings?pageNum=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.boerse-express.com/news/articles/byd-aktie-schnell-meldung-953946` -> **live_dated** (page date 2026-10-17); points raw/verified 12/5
  - p200 Expected revenue growth rate for BYD Q3 2026 vs prior year = **10.2** as written "10,2 %", value check pending % (2026-07-01..2026-09-30) [keep: ] quote: "rund 10,2 % mehr als die 213,06 Milliarden CNY ein Jahr zuvor."
  - p201 Analyst consensus average EPS estimate for BYD Q3 2026 = **1.3** as written "1,30", value check pending CNY per share (2026-07-01..2026-09-30) [DISCARD: EPS estimate; not revenue.] quote: "Analysten rechnen im Schnitt mit 1,30 CNY Gewinn je Aktie, nach 0,94 CNY im Vorjahreszeitraum."
  - p202 Analyst consensus EPS estimate for BYD FY2026 = **4.3** as written "4,30", value check pending CNY per share (2026-01-01..2026-12-31) [DISCARD: EPS estimate; not revenue.] quote: "Der Konsens von mehr als drei Dutzend Analysten sieht den Gewinn je Aktie bei 4,30 CNY, nach 3,88 CNY im Vorjahr."
  - p203 BYD new energy vehicle sales in September 2026 = **464** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept sales; redundant with p71.] quote: "Im September verkaufte BYD 463.561 Fahrzeuge mit alternativen Antrieben."
  - p204 Change in BYD cumulative deliveries January to September 2026 vs prior year = **3.94** as written "3,94 %", value check pending % (2026-01-01..2026-09-30) [DISCARD: Cumulative change; redundant with p384.] quote: "Von Januar bis September summierten sich die Auslieferungen auf 3.131.576 Einheiten und lagen damit 3,94 % unter dem Vorjahreswert."
- `https://ca.investing.com/equities/byd-co.-earnings?cid=1203686` -> **dropped** (live http 403); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/002594/AN202610071830185793.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.moomooapp.com/hans/stock/002594-SZ/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 10 (period year 2030 does not appear in the page text or URL (likely mis-dated): 2; period_end missing or unparseable: 1; number: unknown scale word 'Milliarden': 4; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; number: ambiguous separators: '.' used as a thousands separator: 1)

### d5 [related_series] China NEV market and BYD share as a cross-check

Hypothesis: BYD Q3 revenue growth should be consistent with China NEV passenger-vehicle wholesale growth and BYD's share; a market-total × share × ASP route constrains the unit-sales route.

Queries issued by the searcher: 乘联会 2026年9月 新能源 乘用车 批发 销量; China NEV passenger vehicle wholesale September 2026 CPCA; 比亚迪 2026年9月 新能源汽车销量 产销快报 同比下降; 比亚迪 2026年三季度 营业收入 季报 前三季度; 乘联会 2026年9月 新能源 批发 销量; China NEV wholesale September 2026 CPCA; 乘联分会 2026年8月 新能源乘用车 批发 销量 比亚迪; 比亚迪 2026年8月 销量 新能源汽车 45万辆; 乘联会 2026年9月 新能源乘用车 批发销量; China NEV wholesale September 2026 CPCA passenger vehicle; 乘联分会 2026年8月 新能源乘用车 批发销量 万辆 同比; 乘联分会 2026年7月 新能源乘用车 批发销量 同比

- `https://caifuhao.eastmoney.com/news/20261012134827202325570` -> **live_dated** (page date 2023-08-02); points raw/verified 15/15
  - p205 China new-energy passenger vehicle wholesale volume, September 2026 = **1,666,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车批发销量达到166.6万辆,同比增长11.3%,环比增长10.0%"
  - p206 China new-energy passenger vehicle wholesale volume, January-September 2026 cumu = **11,448,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月新能源乘用车批发销量达到1,144.8万辆,同比增长9.4%"
  - p207 China new-energy passenger vehicle retail volume, September 2026 = **1,084,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV retail; not needed.] quote: "9月新能源乘用车市场零售108.4万辆,同比下降16.7%,环比增长7.8%"
  - p208 China new-energy passenger vehicle retail volume, January-September 2026 cumulat = **7,758,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China NEV retail cumulative; not needed.] quote: "1-9月新能源乘用车市场零售775.8万辆,同比下降12.8%"
  - p209 China new-energy passenger vehicle wholesale penetration rate (NEV wholesale / t = **65.4** % (2026-09-01..2026-09-30) [DISCARD: Penetration; not needed.] quote: "9月新能源车厂商批发渗透率65.4%,较2025年9月提升12个百分点"
  - p210 China new-energy passenger vehicle retail penetration rate (NEV retail / total p = **67** % (2026-09-01..2026-09-30) [DISCARD: Penetration; not needed.] quote: "9月新能源车在国内总体乘用车的零售渗透率67.0%,较去年同期增长9.1个百分点,环比增长1.7个百分点"
  - p211 China total passenger vehicle wholesale volume, September 2026 = **2,549,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China PV wholesale; redundant with p320.] quote: "9月全国乘用车厂商批发254.9万辆,同比下降8.9%,环比增长8.1%"
  - p212 China total passenger vehicle retail volume, September 2026 = **1,618,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China PV retail; redundant with p321.] quote: "2026年9月全国乘用车市场零售161.8万辆,同比下降28.0%,环比增长5.0%"
  - p213 China total passenger vehicle retail volume, January-September 2026 cumulative = **13,334,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China PV retail cumulative; redundant with p322.] quote: "1-9月乘用车累计零售1,333.4万辆,同比下降21.7%"
  - p214 BYD new-energy passenger vehicle wholesale volume, September 2026 = **455,113** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,比亚迪汽车(455,113辆)、吉利汽车(188,800辆)、奇瑞汽车(126,703辆)"
  - p215 BYD new-energy passenger vehicle domestic retail volume, September 2026 = **246,816** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD domestic retail; not needed.] quote: "国内新能源乘用车零售突破2万辆的企业品牌是:比亚迪汽车(246,816辆)、吉利汽车(119,682辆)"
  - p216 BYD new-energy passenger vehicle export volume, September 2026 = **175,877** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD export; redundant with p325.] quote: "9月新能源出口方面优秀的企业是:比亚迪汽车(175,877辆)、奇瑞汽车(85,990辆)"
  - p217 China new-energy passenger vehicle production, September 2026 = **1,655,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV production; not needed.] quote: "9月新能源乘用车生产达到165.5万辆,同比增长9.8%,环比增长8.3%"
  - p218 China new-energy passenger vehicle production, January-September 2026 cumulative = **11,413,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China NEV production cumulative; not needed.] quote: "1-9月累计新能源乘用车生产达到1,141.3万辆,同比增长9.7%"
  - p219 China new-energy passenger vehicle export volume, September 2026 = **558,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV exports; redundant with p283.] quote: "9月新能源乘用车厂商出口55.8万辆,同比增长163.5%,环比增长7.7%"
- `https://autonews.gasgoo.com/articles/market-industry/chinas-september-passenger-vehicle-market-retail-sales-slump-exports-cushion-wholesale-decline-21` -> **live_dated** (page date 2026-10-12); points raw/verified 15/15
  - p220 China passenger vehicle retail sales, September 2026 (CPCA) = **1,618,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "passenger vehicle retail sales totaled 1.618 million units in September 2026, down 28.0% year on year but up 5.0% month on month."
  - p221 China passenger vehicle retail sales, January–September 2026 cumulative (CPCA) = **13,334,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "Retail sales for January-September reached 13.334 million units, down 21.7%."
  - p222 China passenger vehicle wholesale sales, September 2026 (CPCA) = **2,549,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "total passenger vehicle wholesale sales reached 2.549 million units, down 8.9%-a considerably smaller decline than in domestic retail sales."
  - p223 China passenger vehicle exports (complete vehicles + CKD), September 2026 = **917,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China PV exports; not needed.] quote: "Passenger vehicle exports, including complete vehicles and completely knocked-down (CKD) kits, rose 73.7% year on year to 917,000 units, accounting for 36% of manufacturers' wholesale sales."
  - p224 China NEV passenger vehicle retail sales, September 2026 = **1,084,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "September retail sales of NEV passenger vehicles totaled 1.084 million units, down 16.7% year on year but up 7.8% month on month."
  - p225 China NEV passenger vehicle retail sales, January–September 2026 cumulative = **7,758,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "Retail sales over the first three quarters reached 7.758 million units, down 12.8%."
  - p226 China NEV passenger vehicle wholesale sales, September 2026 = **1,666,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "September NEV passenger vehicle wholesale sales rose 11.3% year on year to 1.666 million units, while domestic retail sales fell 16.7%."
  - p227 China NEV passenger vehicle exports, September 2026 = **558,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "September NEV passenger vehicle exports reached 558,000 units, up 163.5% year on year and 7.7% month on month."
  - p228 China NEV passenger vehicle exports, January–September 2026 cumulative = **3,887,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China NEV exports cumulative; not needed.] quote: "Exports over the first three quarters totaled 3.887 million units, up 138.8% year on year."
  - p229 NEV share of China domestic passenger vehicle retail sales, September 2026 = **67** % (2026-09-01..2026-09-30) [keep: ] quote: "NEVs accounted for 67.0% of domestic passenger vehicle retail sales in September, up 9.1 percentage points year on year and 1.7 percentage points month on month."
  - p230 BYD retail sales of locally made passenger vehicles, September 2026 = **247,000** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD retail; not needed.] quote: "BYD remained the retail leader for locally made passenger vehicles, with approximately 247,000 units sold and a 15.3% market share, despite a 28.9% year-on-year decline."
  - p231 BYD share of China domestic passenger vehicle retail sales, September 2026 = **15.3** % (2026-09-01..2026-09-30) [DISCARD: BYD retail share; not needed.] quote: "BYD remained the retail leader for locally made passenger vehicles, with approximately 247,000 units sold and a 15.3% market share, despite a 28.9% year-on-year decline."
  - p232 BYD wholesale sales, September 2026 = **455,000** vehicle (2026-09-01..2026-09-30) [DISCARD: BYD wholesale; redundant with p71.] quote: "BYD, Geely Auto and Chery Auto took the top three positions, with approximately 455,000, 290,000 and 282,000 units, respectively."
  - p233 BYD share of China passenger vehicle wholesale sales, September 2026 = **17.9** % (2026-09-01..2026-09-30) [DISCARD: BYD wholesale share; not needed.] quote: "Their respective shares of the wholesale market were 17.9%, 11.4% and 11.1%."
  - p234 Chinese brands domestic retail sales, September 2026 = **1,130,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Chinese brands retail; not needed.] quote: "Their domestic retail sales fell 25% year on year to 1.130 million units, while wholesale sales declined just 0.2% to 1.965 million units."
- `https://cnevpost.com/2026/10/09/china-sept-2026-nev-wholesale-estimated-at-2026-high/` -> **live_dated** (page date 2026-10-09); points raw/verified 15/15
  - p235 China passenger NEV wholesale sales, September 2026, CPCA preliminary estimate = **1,670,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV wholesale; redundant with p303.] quote: "China's passenger new energy vehicle (NEV) wholesale sales are estimated to have reached 1.67 million in September 2026"
  - p236 China passenger NEV wholesale sales, September 2026, year-on-year growth (CPCA e = **12** % (2026-09-01..2026-09-30) [DISCARD: China NEV growth; redundant with p260.] quote: "September NEV wholesale sales rose 12% year-on-year and 11% from August."
  - p237 China passenger NEV wholesale sales, September 2026, month-on-month growth (CPCA = **11** % (2026-09-01..2026-09-30) [DISCARD: China NEV growth; redundant with p261.] quote: "September NEV wholesale sales rose 12% year-on-year and 11% from August."
  - p238 China passenger NEV wholesale sales, cumulative January-September 2026 (CPCA-bas = **11,420,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China NEV cumulative; redundant with p291.] quote: "China's passenger NEV wholesale sales totaled about 11.42 million in the first 9 months of the year, up about 10% year-on-year."
  - p239 China passenger NEV wholesale sales, cumulative January-September 2026, year-on- = **10** % (2026-01-01..2026-09-30) [DISCARD: China NEV cumulative growth; not needed.] quote: "China's passenger NEV wholesale sales totaled about 11.42 million in the first 9 months of the year, up about 10% year-on-year."
  - p240 China passenger NEV retail sales, September 1-27 2026, year-on-year change (CPCA = **20** % (2026-09-01..2026-09-27) [DISCARD: Weekly retail; not needed.] quote: "China's passenger NEV retail sales fell 20% year-on-year to 827,000 from September 1 to 27."
  - p241 China passenger NEV retail sales, September 1-27 2026 (CPCA weekly data) = **827,000** vehicle (2026-09-01..2026-09-27) [DISCARD: Weekly retail; not needed.] quote: "China's passenger NEV retail sales fell 20% year-on-year to 827,000 from September 1 to 27."
  - p242 BYD passenger NEV wholesale sales, September 2026 (rank 1) = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "\| 1 \| BYD \| 456,713 \|"
  - p243 Geely passenger NEV wholesale sales, September 2026 (rank 2) = **188,800** vehicle (2026-09-01..2026-09-30) [DISCARD: Geely sales; not needed.] quote: "\| 2 \| Geely \| 188,800 \|"
  - p244 Chery passenger NEV wholesale sales, September 2026 (rank 3) = **127,486** vehicle (2026-09-01..2026-09-30) [DISCARD: Chery sales; not needed.] quote: "\| 3 \| Chery \| 127,486 \|"
  - p245 Leapmotor passenger NEV wholesale sales, September 2026 (rank 4) = **105,656** vehicle (2026-09-01..2026-09-30) [DISCARD: Leapmotor sales; not needed.] quote: "\| 4 \| Leapmotor \| 105,656 \|"
  - p246 Changan passenger NEV wholesale sales, September 2026 (rank 5) = **102,968** vehicle (2026-09-01..2026-09-30) [DISCARD: Changan sales; not needed.] quote: "\| 5 \| Changan \| 102,968 \|"
  - p247 Combined September 2026 sales of manufacturers with August NEV wholesale above 1 = **1,550,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Aggregate sales; not needed.] quote: "Preliminary figures put those manufacturers' combined September sales at about 1.55 million."
  - p248 Share of August 2026 passenger NEV wholesale total held by manufacturers with NE = **93** % (2026-08-01..2026-08-31) [DISCARD: Share; not needed.] quote: "Companies with NEV wholesale sales exceeding 10,000 in August accounted for a combined 93% of that month's passenger NEV wholesale total."
  - p249 Tesla China passenger NEV wholesale sales, September 2026 (rank 6) = **95,366** vehicle (2026-09-01..2026-09-30) [DISCARD: Tesla sales; not needed.] quote: "\| 6 \| Tesla China \| 95,366 \|"
- `https://www.zhitongcaijing.com/content/detail/1505346.html` -> **live_dated** (page date 2026-10-09); points raw/verified 9/9
  - p250 China NEV passenger vehicle wholesale (CPCA preliminary estimate), September 202 = **1,670,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月全国乘用车厂商新能源批发预估167万辆,同比增长12%,环比增长11%"
  - p251 China NEV passenger vehicle wholesale year-on-year growth, September 2026 = **12** % (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月全国乘用车厂商新能源批发预估167万辆,同比增长12%,环比增长11%"
  - p252 China NEV passenger vehicle wholesale month-on-month growth, September 2026 = **11** % (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月全国乘用车厂商新能源批发预估167万辆,同比增长12%,环比增长11%"
  - p253 Share of August 2026 China NEV passenger vehicle wholesale held by manufacturers = **93** % (2026-08-01..2026-08-31) [DISCARD: Share; not needed.] quote: "2026年8月,全国乘用车市场新能源销量万辆以上厂商批发销量之和,占总体新能源乘用车当月销量的93%"
  - p254 September 2026 wholesale sales of manufacturers that each sold above 10,000 NEV  = **1,550,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Aggregate sales; not needed.] quote: "这些8月新能源销量的万辆以上厂商企业的9月销量为155万辆"
  - p255 China NEV passenger vehicle wholesale (CPCA estimate derived from August structu = **1,670,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Derived estimate; not needed.] quote: "测算9月的全国新能源乘用车批发销量为167万辆"
  - p256 China passenger vehicle retail volume, 1-20 September 2026 = **878,000** vehicle (2026-09-01..2026-09-20) [DISCARD: Weekly retail; not needed.] quote: "乘联分会:9月1-20日全国乘用车市场零售87.8万辆 环比增长8%"
  - p257 China passenger vehicle retail month-on-month growth, 1-20 September 2026 = **8** % (2026-09-01..2026-09-20) [DISCARD: Weekly growth; not needed.] quote: "乘联分会:9月1-20日全国乘用车市场零售87.8万辆 环比增长8%"
  - p258 China passenger vehicle intelligence index, August 2026 = **40.8** 1 (2026-08-01..2026-08-31) [DISCARD: Intelligence index; irrelevant.] quote: "乘联分会:8月乘用车智能化指数为40.8"
- `http://wdatacn.aastocks.com/en/stocks/analysis/stock-aafn-con/81810/HK6/NOW.1549224/hk-stock-news` -> **live_dated** (page date 2026-10-14); points raw/verified 10/10
  - p259 China NEV passenger vehicle wholesale sales, Sep 2026 (CPCA) = **1,670,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "China's wholesale sales of new energy passenger vehicles reached 1.67 million units in Sep 2026, up 12% YoY and 10% MoM."
  - p260 China NEV passenger vehicle wholesale sales YoY growth, Sep 2026 = **12** % (2026-09-01..2026-09-30) [keep: ] quote: "China's wholesale sales of new energy passenger vehicles reached 1.67 million units in Sep 2026, up 12% YoY and 10% MoM."
  - p261 China NEV passenger vehicle wholesale sales MoM growth, Sep 2026 = **10** % (2026-09-01..2026-09-30) [keep: ] quote: "China's wholesale sales of new energy passenger vehicles reached 1.67 million units in Sep 2026, up 12% YoY and 10% MoM."
  - p262 China NEV penetration rate (share of NEV in passenger vehicle sales), Sep 2026 = **65.4** % (2026-09-01..2026-09-30) [keep: ] quote: "NEV penetration rate reached 65.4%, up 12 ppts YoY and 1.2 ppts MoM."
  - p263 China NEV penetration rate YoY change, Sep 2026 = **12** pp (2026-09-01..2026-09-30) [DISCARD: Penetration change; not needed.] quote: "NEV penetration rate reached 65.4%, up 12 ppts YoY and 1.2 ppts MoM."
  - p264 China NEV penetration rate MoM change, Sep 2026 = **1.2** pp (2026-09-01..2026-09-30) [DISCARD: Penetration change; not needed.] quote: "NEV penetration rate reached 65.4%, up 12 ppts YoY and 1.2 ppts MoM."
  - p265 China battery electric passenger vehicle wholesale sales, Sep 2026 = **1,130,000** vehicle (2026-09-01..2026-09-30) [DISCARD: BEV wholesale; not needed.] quote: "wholesale sales of battery electric vehicles rose 19% YoY to 1.13 million units in Sep"
  - p266 China battery electric passenger vehicle wholesale sales YoY growth, Sep 2026 = **19** % (2026-09-01..2026-09-30) [DISCARD: BEV growth; not needed.] quote: "wholesale sales of battery electric vehicles rose 19% YoY to 1.13 million units in Sep"
  - p267 China plug-in hybrid passenger vehicle wholesale sales, Sep 2026 = **539,500** vehicle (2026-09-01..2026-09-30) [DISCARD: PHEV wholesale; not needed.] quote: "plug-in hybrid vehicle sales edged down 1% YoY to 539,500 units"
  - p268 China plug-in hybrid passenger vehicle wholesale sales YoY change, Sep 2026 = **1** % (2026-09-01..2026-09-30) [DISCARD: PHEV change; not needed.] quote: "plug-in hybrid vehicle sales edged down 1% YoY to 539,500 units"
- `https://auto.cnr.cn/djfb/20261013/t20261013_527840868.shtml` -> **live_dated** (page date 2026-10-13); points raw/verified 15/15
  - p269 China narrow passenger vehicle retail sales, September 2026 = **1,618,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月狭义乘用车零售161.8万辆,同比下降28.0%,环比增长5.0%"
  - p270 China narrow passenger vehicle retail sales, January-September 2026 cumulative = **13,334,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月累计零售1333.4万辆,同比下滑21.7%"
  - p271 China narrow passenger vehicle wholesale sales, September 2026 = **2,549,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月狭义乘用车厂商批售254.9万辆,同比下降8.9%,环比提升8.1%"
  - p272 China self-owned brand narrow passenger vehicle wholesale sales, September 2026 = **1,965,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Self-owned wholesale; not needed.] quote: "自主品牌批发196.5万辆,同比微降0.2%"
  - p273 China NEV passenger vehicle retail sales, September 2026 = **1,084,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车零售108.4万辆,同比下降16.7%,环比增长7.8%"
  - p274 China NEV passenger vehicle wholesale sales, September 2026 = **1,666,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "批发166.6万辆,同比增长11.3%,环比增长10.0%"
  - p275 China NEV retail penetration rate (NEV retail / narrow PV retail), September 202 = **67** % (2026-09-01..2026-09-30) [keep: ] quote: "零售渗透率67.0%,批发渗透率65.4%,两项指标均刷新历史纪录"
  - p276 China NEV wholesale penetration rate (NEV wholesale / narrow PV wholesale), Sept = **65.4** % (2026-09-01..2026-09-30) [keep: ] quote: "零售渗透率67.0%,批发渗透率65.4%,两项指标均刷新历史纪录"
  - p277 China battery electric passenger vehicle wholesale sales, September 2026 = **1,126,000** vehicle (2026-09-01..2026-09-30) [DISCARD: BEV wholesale; not needed.] quote: "9月纯电动车型批发112.6万辆,同比增长18.3%"
  - p278 China plug-in hybrid passenger vehicle wholesale sales, September 2026 = **423,000** vehicle (2026-09-01..2026-09-30) [DISCARD: PHEV wholesale; not needed.] quote: "插电混动车型批发42.3万辆,同比基本持平"
  - p279 China extended-range passenger vehicle wholesale sales, September 2026 = **117,000** vehicle (2026-09-01..2026-09-30) [DISCARD: EREV wholesale; not needed.] quote: "增程式车型批发11.7万辆,同比小幅下滑4%"
  - p280 China B-segment battery electric vehicle wholesale sales, September 2026 = **329,000** vehicle (2026-09-01..2026-09-30) [DISCARD: B-segment; not needed.] quote: "B级电动车批发32.9万辆,同比上涨21%"
  - p281 China self-owned brand NEV domestic retail penetration rate, September 2026 = **84.5** % (2026-09-01..2026-09-30) [DISCARD: Penetration; not needed.] quote: "自主品牌新能源国内零售渗透率84.5%"
  - p282 China new-force brand retail share, September 2026 = **23.6** % (2026-09-01..2026-09-30) [DISCARD: New-force share; not needed.] quote: "新势力品牌零售份额23.6%,同比提升3.4个百分点"
  - p283 China NEV passenger vehicle exports, September 2026 = **558,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车出口55.8万辆,同比上涨163.5%,环比增长7.7%"
- `https://cnevpost.com/2026/10/10/china-sept-nev-retail-preliminary-cpca/` -> **live_dated** (page date 2026-10-10); points raw/verified 15/15
  - p284 China passenger NEV retail sales, September 2026 (CPCA preliminary) = **1,141,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China NEV retail; redundant with p307.] quote: "China's retail sales of passenger new energy vehicles (NEVs) totaled 1.141 million in September, down 12% year-on-year but up 14% from August"
  - p285 China passenger NEV retail sales, September 1-27 2026 = **827,000** vehicle (2026-09-01..2026-09-27) [DISCARD: Weekly retail; not needed.] quote: "From September 1 to 27, retail sales of passenger NEVs in China totaled 827,000 units, a 20% year-on-year decline."
  - p286 China passenger NEV retail sales, final 3 days of September 2026 (CnEVPost calcu = **310,000** vehicle (2026-09-28..2026-09-30) [DISCARD: Derived; not needed.] quote: "the final 3 days of September contributed about 310,000 NEV retail sales, or nearly 28% of the monthly total"
  - p287 NEV share of China passenger vehicle retail sales, September 2026 = **67.1** % (2026-09-01..2026-09-30) [keep: ] quote: "NEVs accounted for 67.1% of passenger vehicle retail sales in September, up from 65.7% in the first 27 days."
  - p288 NEV share of China passenger vehicle retail sales, September 1-27 2026 = **65.7** % (2026-09-01..2026-09-27) [DISCARD: Penetration; not needed.] quote: "NEVs accounted for 67.1% of passenger vehicle retail sales in September, up from 65.7% in the first 27 days."
  - p289 China passenger NEV retail sales, year-to-date through September 2026 = **7,816,000** vehicle (2026-01-01..2026-09-30) [DISCARD: China NEV retail cumulative; not needed.] quote: "Year-to-date NEV retail sales totaled 7.816 million, down 12% year-on-year."
  - p290 China passenger NEV wholesale sales, September 2026 (CnEVPost compiled) = **1,672,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "Wholesale sales of passenger NEVs reached 1.672 million in September, up 11% both year-on-year and from August, marking the highest monthly total this year"
  - p291 China passenger NEV wholesale sales, year-to-date through September 2026 = **11,450,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "Year-to-date NEV wholesale sales totaled 11.45 million, up 9% year-on-year."
  - p292 NEV share of China passenger vehicle wholesale sales, September 2026 = **66.1** % (2026-09-01..2026-09-30) [DISCARD: Penetration; not needed.] quote: "NEVs accounted for 66.1% of passenger vehicle wholesale sales in September."
  - p293 China passenger vehicle retail sales, September 2026 = **1,702,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "Retail sales totaled 1.702 million in September, down 24% year-on-year but up 10% from August."
  - p294 China passenger vehicle retail sales, year-to-date through September 2026 = **13,420,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "Year-to-date retail sales reached 13.42 million, down 21% year-on-year."
  - p295 China passenger vehicle wholesale sales, September 2026 = **2,528,000** vehicle (2026-09-01..2026-09-30) [DISCARD: China PV wholesale; redundant with p320.] quote: "Total passenger vehicle wholesale sales were 2.528 million, down 10% year-on-year but up 7% from August."
  - p296 China share of global passenger NEV sales, first 8 months of 2026 = **62** % (2026-01-01..2026-08-31) [DISCARD: Global share; not needed.] quote: "The country accounted for 62% of global passenger NEV sales in the first 8 months of 2026, with that share rising to 65.3% in July-August"
  - p297 China share of global passenger NEV sales, July-August 2026 = **65.3** % (2026-07-01..2026-08-31) [DISCARD: Global share; not needed.] quote: "The country accounted for 62% of global passenger NEV sales in the first 8 months of 2026, with that share rising to 65.3% in July-August"
  - p298 China share of global plug-in hybrid market, first 8 months of 2026 = **71** % (2026-01-01..2026-08-31) [DISCARD: Global share; not needed.] quote: "China's share of the global plug-in hybrid market reached 71% over the same 8-month period and rose to 74% in August."
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/846387231445/index.phtml` -> **live_dated** (page date 2026-10-26); points raw/verified 15/15
  - p299 China NEV vehicle sales (CAAM, incl. commercial), September 2026 = **1,823,000** vehicle (2026-09-01..2026-09-30) [DISCARD: CAAM NEV sales; not needed.] quote: "9月中汽协口径国内新能源车销量 182.3万辆,同/环比+13.6%/+10.9%"
  - p300 China NEV vehicle sales YoY growth (CAAM), September 2026 = **13.6** % (2026-09-01..2026-09-30) [DISCARD: CAAM growth; not needed.] quote: "9月中汽协口径国内新能源车销量 182.3万辆,同/环比+13.6%/+10.9%"
  - p301 China NEV vehicle sales MoM growth (CAAM), September 2026 = **10.9** % (2026-09-01..2026-09-30) [DISCARD: CAAM growth; not needed.] quote: "9月中汽协口径国内新能源车销量 182.3万辆,同/环比+13.6%/+10.9%"
  - p302 China NEV vehicle production (CAAM, incl. commercial), September 2026 = **1,814,000** vehicle (2026-09-01..2026-09-30) [DISCARD: CAAM production; not needed.] quote: "2026 年 9 月国内新能源车(含商用)产量 181.4 万辆,同比+12.2%,环比+9.7%"
  - p303 China NEV passenger vehicle wholesale (CPCA), September 2026 = **1,666,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "乘 联 会 口 径 新 能 源 乘 用 车 批 售 166.6 万 辆 , 同/环比+11.3%/+10.0%,渗透率 65.4%"
  - p304 China NEV passenger vehicle wholesale YoY growth (CPCA), September 2026 = **11.3** % (2026-09-01..2026-09-30) [DISCARD: China NEV growth; redundant with p260.] quote: "乘 联 会 口 径 新 能 源 乘 用 车 批 售 166.6 万 辆 , 同/环比+11.3%/+10.0%"
  - p305 China NEV passenger vehicle wholesale MoM growth (CPCA), September 2026 = **10** % (2026-09-01..2026-09-30) [DISCARD: China NEV growth; redundant with p261.] quote: "乘 联 会 口 径 新 能 源 乘 用 车 批 售 166.6 万 辆 , 同/环比+11.3%/+10.0%"
  - p306 China NEV passenger vehicle wholesale penetration rate (CPCA), September 2026 = **65.4** % (2026-09-01..2026-09-30) [keep: ] quote: "乘 联 会 口 径 新 能 源 乘 用 车 批 售 166.6 万 辆 , 同/环比+11.3%/+10.0%,渗透率 65.4%,环比+1.2pct"
  - p307 China NEV passenger vehicle retail (CPCA), September 2026 = **1,084,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "零售 108.4 万辆,同比-16.7%,环比+7.8%;渗透率 67.0%,环比+1.8pct"
  - p308 China NEV passenger vehicle retail YoY growth (CPCA), September 2026 = **16.7** % (2026-09-01..2026-09-30) [DISCARD: China NEV retail growth; not needed.] quote: "零售 108.4 万辆,同比-16.7%,环比+7.8%"
  - p309 BYD NEV sales (CPCA), September 2026 = **455,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "比亚迪以 45.5 万辆销量保持第一,环比+5.2%,市占率27.3%,环比-1.3pct"
  - p310 BYD NEV sales MoM growth (CPCA), September 2026 = **5.2** % (2026-09-01..2026-09-30) [DISCARD: BYD MoM; not needed.] quote: "比亚迪以 45.5 万辆销量保持第一,环比+5.2%,市占率27.3%,环比-1.3pct"
  - p311 BYD market share of China NEV passenger vehicle sales (CPCA), September 2026 = **27.3** % (2026-09-01..2026-09-30) [DISCARD: BYD share; not needed.] quote: "比亚迪以 45.5 万辆销量保持第一,环比+5.2%,市占率27.3%,环比-1.3pct"
  - p312 China NEV vehicle exports (CAAM), September 2026 = **571,000** vehicle (2026-09-01..2026-09-30) [DISCARD: CAAM exports; not needed.] quote: "其中出口 57.1 万辆,同/环比+157.0%/+8.6%,维持高增趋势"
  - p313 China NEV full-year 2026 sales forecast (stated expectation) = **18,560,000** vehicle (2026-01-01..2026-12-31) [DISCARD: Full-year forecast; irrelevant.] quote: "2026 全年销量预期 1856万辆,同比+13%"
- `https://www.cpcaauto.com/newslist.php?types=csjd&id=4366` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.iautocloud.com.cn/news/detail.html?id=20790` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.marklines.com/cn/report/cpca084_202610` -> **live_dated** (page date 2026-10-12); points raw/verified 15/15
  - p314 China new energy passenger vehicle wholesale volume, September 2026 = **1,666,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车批发销量达到166.6万辆,同比增长11.3%,环比增长10.0%"
  - p315 China new energy passenger vehicle wholesale volume, January-September 2026 cumu = **11,448,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月新能源乘用车批发销量达到1,144.8万辆,同比增长9.4%"
  - p316 China new energy passenger vehicle retail volume, September 2026 = **1,084,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车市场零售108.4万辆,同比下降16.7%,环比增长7.8%"
  - p317 China new energy passenger vehicle retail volume, January-September 2026 cumulat = **7,758,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月新能源乘用车市场零售775.8万辆,同比下降12.8%"
  - p318 China new energy passenger vehicle wholesale penetration rate (NEV share of whol = **65.4** % (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源车厂商批发渗透率65.4%,较2025年9月提升12个百分点"
  - p319 China new energy passenger vehicle retail penetration rate (NEV share of retail) = **67** % (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源车在国内总体乘用车的零售渗透率67.0%,较去年同期增加9.1个百分点"
  - p320 China total passenger vehicle wholesale volume, September 2026 = **2,549,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月全国乘用车厂商批发254.9万辆,同比下降8.9%,环比增长8.1%"
  - p321 China total passenger vehicle retail volume, September 2026 = **1,618,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月全国乘用车市场零售161.8万辆,同比下降28.0%,环比增长5.0%"
  - p322 China total passenger vehicle retail volume, January-September 2026 cumulative = **13,334,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月乘用车累计零售1,333.4万辆,同比下降21.7%"
  - p323 BYD new energy passenger vehicle wholesale volume, September 2026 = **455,113** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,比亚迪汽车(455,113辆)、吉利汽车(188,800辆)"
  - p324 BYD new energy passenger vehicle domestic retail volume, September 2026 = **246,816** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "国内新能源乘用车零售突破2万辆的企业品牌:比亚迪汽车(246,816辆)"
  - p325 BYD new energy passenger vehicle export volume, September 2026 = **175,877** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源出口方面优秀的企业是:比亚迪汽车(175,877辆)"
  - p326 China new energy passenger vehicle production, September 2026 = **1,655,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车生产达到165.5万辆,同比增长9.8%,环比增长8.3%"
  - p327 China new energy passenger vehicle production, January-September 2026 cumulative = **11,413,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "1-9月累计新能源乘用车生产达到1,141.3万辆,同比增长9.7%"
  - p328 China passenger vehicle export volume (including CBU and CKD), September 2026 = **917,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月乘用车出口(含整车与CKD)91.7万辆,同比增长73.7%,环比增长3.2%"
- `https://www.jiemian.com/article/15047031.html` -> **live_dated** (page date 2026-01-01); points raw/verified 3/3
  - p329 China NEV passenger vehicle manufacturer wholesale sales estimate, August 2026 ( = **1,510,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug forecast; not needed.] quote: "2026年8月,全国新能源乘用车厂商批发销量预估达到151.0万辆,同比增长16%,环比增长4%"
  - p330 China NEV passenger vehicle manufacturer wholesale sales year-on-year growth, Au = **16** % (2026-08-01..2026-08-31) [DISCARD: Aug growth; not needed.] quote: "2026年8月,全国新能源乘用车厂商批发销量预估达到151.0万辆,同比增长16%,环比增长4%"
  - p331 China NEV passenger vehicle manufacturer wholesale sales month-on-month growth,  = **4** % (2026-08-01..2026-08-31) [DISCARD: Aug growth; not needed.] quote: "2026年8月,全国新能源乘用车厂商批发销量预估达到151.0万辆,同比增长16%,环比增长4%"

### d6 [shocks] Price cuts, mix shift, and export mix affecting ASP

Hypothesis: Q3 2026 ASP may differ from history due to price competition, richer export/Denza mix, or new model launches; adjusting ASP for these effects narrows the revenue-per-unit uncertainty.

Queries issued by the searcher: 比亚迪 2026年第三季度 营业收入 季报; BYD Q3 2026 revenue quarterly report; 比亚迪 2026年9月 销量 新能源汽车 出口 万辆; BYD September 2026 sales NEV exports monthly figures; 比亚迪 2026年第三季度 营业收入 季报; BYD Q3 2026 revenue results; 比亚迪 2026年9月 销量 快报 新能源汽车 出口; BYD September 2026 sales NEV exports monthly figures; 比亚迪 2026年第三季度报告 营业收入; BYD Q3 2026 revenue quarterly report; 比亚迪 2026年9月销量 海外销量 腾势 方程豹 仰望 销量; BYD September 2026 sales overseas exports monthly

- `https://4g.stockstar.com/detail/JC2026101800001092` -> **live_dated** (page date 2026-10-27); points raw/verified 15/13
  - p332 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月汽车销量463561辆,同比增长17%,环比增长5.3%"
  - p333 BYD September 2026 new energy passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源乘用车销量456713辆,同比增长16.2%,环比增长5.4%"
  - p334 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月国内销量28.3万辆,同比下降13%,环比增长12.8%"
  - p335 BYD September 2026 new energy vehicle exports = **181,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p336 BYD September 2026 export share of sales = **39** % (2026-09-01..2026-09-30) [keep: ] quote: "销量占比39%,同比提升21pcts"
  - p337 BYD September 2026 Denza brand sales = **18,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "腾势1.8万辆(同比+46.7%)"
  - p338 BYD September 2026 Fangchengbao brand sales = **43,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "方程豹4.3万辆(同比+79.0%)"
  - p339 BYD September 2026 Yangwang brand sales = **389** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "仰望389辆(同比-48.7%)"
  - p340 BYD September 2026 premium brands (Denza/Fangchengbao/Yangwang) combined sales = **62,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "腾势/方程豹/仰望三个高端品牌合计6.2万辆(同比+65.7%)"
  - p341 BYD September 2026 premium brands share of passenger vehicle sales = **13.5** % (2026-09-01..2026-09-30) [keep: ] quote: "占乘用车销量13.5%,同比提升4pcts"
  - p342 BYD September 2026 Dynasty and Ocean network combined sales = **395,000** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p343 BYD cumulative 2026 total vehicle sales (Jan-Sep) = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计汽车销量3131576辆,同比下降3.9%"
  - p344 BYD cumulative 2026 domestic sales (Jan-Sep) = **1,789,000** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计国内销量178.9万辆,同比下降30%"
- `http://mp.weixin.qq.com/s?__biz=MjM5MjcwMTkwMA==&mid=2652626645&idx=3&sn=1f27e73217575980ff65bc7a307d5742` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://in.investing.com/equities/byd-a-earnings?pageNum=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.cnfin.com/announ/detail/index.html?id=844705253353&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `https://www.aastocks.com/en/stocks/news/aafn-con/now.1549400/popular-news/aafn?totc=1` -> **live_dated** (page date 2026-10-15); points raw/verified 15/9
  - p345 Goldman Sachs forecast: BYD Q3 2026 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "按年增長25%且按季增長25%"
  - p346 Goldman Sachs forecast: BYD Q3 2026 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "按年增長25%且按季增長25%"
  - p347 Goldman Sachs forecast: BYD Q3 2026 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "淨利潤115億元,按年上升47%並按季增長39%"
  - p348 Goldman Sachs forecast: BYD Q3 2026 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "淨利潤115億元,按年上升47%並按季增長39%"
  - p349 Goldman Sachs forecast: BYD Q3 2026 sales volume YoY growth = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "主要受惠於銷量增長年及按季均升19%"
  - p350 Goldman Sachs forecast: BYD Q3 2026 sales volume QoQ growth = **19** % (2026-07-01..2026-09-30) [DISCARD: Volume growth; not needed.] quote: "主要受惠於銷量增長年及按季均升19%"
  - p351 BYD domestic NEV retail market share, Q2 2026 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "其國內新能源車零售市佔率由第二季的22%提升至第三季的25%"
  - p352 BYD domestic NEV retail market share, Q3 2026 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "其國內新能源車零售市佔率由第二季的22%提升至第三季的25%"
  - p353 China NEV export VAT rebate rate, before 2027-04-01 = **13** % (..2027-03-31) [DISCARD: VAT rate; irrelevant.] quote: "自2027年4月1日起將新能源車出口增值稅退稅率由13%下調至9%"
- `https://sg.finance.yahoo.com/quote/0HKY.L/analysis/` -> **dropped** (live http 503); points raw/verified -/-
- `https://www.moomoocn.com/hans/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://wwwhk.aastocks.com/en/stocks/news/aafn-con/NOW.1549400/popular-news/AAFN` -> **live_dated** (page date 2026-10-15); points raw/verified 15/12
  - p354 Goldman Sachs forecast BYD 3Q26 revenue (RMB) = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p355 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p356 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p357 Goldman Sachs forecast BYD 3Q26 net profit (RMB) = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p358 Goldman Sachs forecast BYD 3Q26 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p359 Goldman Sachs forecast BYD 3Q26 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p360 Goldman Sachs forecast BYD 3Q26 sales volume growth YoY and QoQ = **19** % (2026-07-01..2026-09-30) [keep: ] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p361 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p362 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [keep: ] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p363 BYD Hungary plant planned annual capacity = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Hungary capacity; not realised output.] quote: "Hungary plant is expected to commence production by the end of 2026 with planned annual capacity of 300,000 vehicles"
  - p364 China NEV export VAT rebate rate before 2027-04-01 = **13** % (..2027-03-31) [DISCARD: VAT rebate rate; no Q3 2026 revenue effect.] quote: "the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p365 Goldman Sachs assumed cost pass-through for VAT rebate cut = **67** % (2027-01-01..2027-12-31) [DISCARD: VAT pass-through; irrelevant.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- `https://www.moomoocn.com/hans/stock/002594-SZ/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://finance.eastmoney.com/a/202610013888248472.html` -> **live_dated** (page date 2026-10-01); points raw/verified 9/9
  - p366 BYD September 2026 new energy vehicle sales volume = **463,600** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月,公司新能源汽车产量为46.39万辆,销量为46.36万辆。"
  - p367 BYD September 2026 new energy vehicle production volume = **463,900** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept production; not needed.] quote: "2026年9月,公司新能源汽车产量为46.39万辆,销量为46.36万辆。"
  - p368 BYD September 2026 passenger vehicle production volume = **458,100** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept production; not needed.] quote: "其中,乘用车产量45.81万辆,销量45.67万辆;"
  - p369 BYD September 2026 passenger vehicle sales volume = **456,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量45.81万辆,销量45.67万辆;"
  - p370 BYD September 2026 commercial vehicle production volume = **5,748** vehicle (2026-09-01..2026-09-30) [DISCARD: Commercial production; not needed.] quote: "商用车产量5748辆,销量6848辆。"
  - p371 BYD September 2026 commercial vehicle sales volume = **6,848** vehicle (2026-09-01..2026-09-30) [DISCARD: Commercial sales; not needed.] quote: "商用车产量5748辆,销量6848辆。"
  - p372 BYD cumulative year-to-date 2026 new energy vehicle production volume = **3,138,900** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative production; not needed.] quote: "本年累计新能源汽车产量313.89万辆,销量313.16万辆。"
  - p373 BYD cumulative year-to-date 2026 new energy vehicle sales volume = **3,131,600** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "本年累计新能源汽车产量313.89万辆,销量313.16万辆。"
  - p374 BYD September 2026 new energy vehicle export volume = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "此外,公司9月出口新能源汽车合计18.07万辆。"
- `https://wap.stockstar.com/detail/AN2026100700005520` -> **live_dated** (page date 2026-10-27); points raw/verified 13/13
  - p375 BYD September 2026 new energy vehicle production volume = **463,864** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "当月新能源汽车产量为463,864辆,同比增长14.38%"
  - p376 BYD September 2026 new energy vehicle sales volume = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "销量为463,561辆,同比增长16.98%"
  - p377 BYD September 2026 new energy vehicle sales volume year-on-year growth = **16.98** % (2026-09-01..2026-09-30) [DISCARD: Sept growth; not needed.] quote: "销量为463,561辆,同比增长16.98%"
  - p378 BYD September 2026 passenger vehicle production volume = **458,116** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量458,116辆,销量456,713辆"
  - p379 BYD September 2026 passenger vehicle sales volume = **456,713** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "其中,乘用车产量458,116辆,销量456,713辆"
  - p380 BYD September 2026 commercial vehicle production volume = **5,748** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "商用车产量5,748辆,销量6,848辆"
  - p381 BYD September 2026 commercial vehicle sales volume = **6,848** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "商用车产量5,748辆,销量6,848辆"
  - p382 BYD cumulative Jan-Sep 2026 new energy vehicle production volume = **3,138,946** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "本年累计新能源汽车产量3,138,946辆,同比下降2.32%"
  - p383 BYD cumulative Jan-Sep 2026 new energy vehicle sales volume = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "累计销量3,131,576辆,同比下降3.94%"
  - p384 BYD cumulative Jan-Sep 2026 new energy vehicle sales volume year-on-year growth = **3.94** % (2026-01-01..2026-09-30) [keep: ] quote: "累计销量3,131,576辆,同比下降3.94%"
  - p385 BYD cumulative Jan-Sep 2026 battery electric vehicle sales volume year-on-year g = **1.5** % (2026-01-01..2026-09-30) [DISCARD: BEV cumulative growth; not needed.] quote: "纯电动车型累计销量同比增长1.50%"
  - p386 BYD cumulative Jan-Sep 2026 plug-in hybrid vehicle sales volume year-on-year gro = **10.19** % (2026-01-01..2026-09-30) [DISCARD: PHEV cumulative growth; not needed.] quote: "插电式混合动力车型累计销量同比下降10.19%"
  - p387 BYD September 2026 new energy vehicle export volume = **180,700** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月出口新能源汽车180,700辆"
- `https://www.163.com/dy/article/L867EADG05568W0A.html` -> **live_dated** (page date 2026-10-01); points raw/verified 7/7
  - p388 BYD September 2026 total vehicle production (approx.) = **463,900** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept production; not needed.] quote: "2026年9月,该公司汽车产量合计约46.39万辆,同比增加14.38%"
  - p389 BYD September 2026 total vehicle production year-on-year growth = **14.38** % (2026-09-01..2026-09-30) [DISCARD: Production growth; not needed.] quote: "2026年9月,该公司汽车产量合计约46.39万辆,同比增加14.38%"
  - p390 BYD cumulative vehicle production January-September 2026 (approx.) = **3,138,900** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative production; not needed.] quote: "前9个月累计产量约313.89万辆"
  - p391 BYD September 2026 total vehicle sales (approx.) = **463,600** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月该公司汽车销量约46.36万辆,同比增长16.98%"
  - p392 BYD September 2026 total vehicle sales year-on-year growth = **16.98** % (2026-09-01..2026-09-30) [DISCARD: Sept growth; not needed.] quote: "2026年9月该公司汽车销量约46.36万辆,同比增长16.98%"
  - p393 BYD September 2026 new energy vehicle export volume (approx.) = **180,700** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept exports; redundant with p90.] quote: "出口新能源汽车合计约18.07万辆"
  - p394 BYD cumulative vehicle sales January-September 2026 (approx.) = **3,131,600** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "前9个月销量约313.16万辆"
- dropped by code checks: 11 (scale word '万' not supported by quote or table header: 3; scale word '亿' not supported by quote or table header: 3; period_end missing or unparseable: 3; period year 2030 does not appear in the page text or URL (likely mis-dated): 2)

### d7 [administrative] Regulatory filings and exchange disclosures

Hypothesis: Any BYD production/sales announcements filed with Shenzhen Stock Exchange or HKEX before cutoff, and the timing of the Q3 report, confirm the reporting basis and may include preliminary figures.

Queries issued by the searcher: 比亚迪 2026年第三季度报告 披露时间; BYD September 2026 sales announcement HKEX; 比亚迪 2026年半年报 营业收入 上半年 亿元; 比亚迪 2025年第三季度报告 营业收入 第三季度 单季度; 比亚迪 2026年第三季度报告 披露 时间; BYD HKEX announcement October 2026 quarterly results board meeting; 比亚迪 2026年9月 产销快报 新能源汽车销量 公告; 比亚迪 2026年半年报 营业收入 上半年 亿元; 比亚迪 2026年第三季度报告 披露 时间; BYD HKEX announcement October 2026 third quarterly report; 比亚迪 2026年9月 产销快报 新能源汽车销量 公告; 比亚迪 2026年半年度报告 营业收入 上半年

- `https://basic.10jqka.com.cn/002594/` -> **live_dated** (page date 2026-10-23); points raw/verified 15/15
  - p395 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2026-06- = **344,815,000,000** CNY (2026-01-01..2026-06-30) [keep: ] quote: "\| 2026-06-30 \| 1.35 \| 26.32 \| 10.49 \| 13.72 \| 4.10 \| 3448.15亿 \| 123.25亿 \| 4.86% \| \|"
  - p396 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2026-03- = **150,225,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Q1 2026 revenue; not needed for Q3.] quote: "\| 2026-03-31 \| 0.45 \| 25.44 \| 10.47 \| 13.18 \| 0.31 \| 1502.25亿 \| 40.85亿 \| 1.65% \| \|"
  - p397 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2025-09- = **566,266,000,000** CNY (2025-01-01..2025-09-30) [DISCARD: 9M 2025 revenue; redundant with p2.] quote: "\| 2025-09-30 \| 2.56 \| 24.11 \| 10.60 \| 11.76 \| 4.48 \| 5662.66亿 \| 233.33亿 \| 10.83% \| \|"
  - p398 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2025-12- = **803,965,000,000** CNY (2025-01-01..2025-12-31) [DISCARD: FY2025 revenue; not needed.] quote: "\| 2025-12-31 \| 3.58 \| 24.96 \| 10.45 \| 12.73 \| 6.49 \| 8039.65亿 \| 326.19亿 \| 15.31% \| \|"
  - p399 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2025-07- = **371,281,000,000** CNY (2025-01-01..2025-07-29) [DISCARD: H1 2025 revenue; not needed.] quote: "\| 2025-07-29 \| 1.70 \| 23.08 \| 11.01 \| 11.19 \| 3.49 \| 3712.81亿 \| 155.11亿 \| 7.43% \| 分红转增 \|"
  - p400 BYD consolidated operating revenue (营业总收入) cumulative for period ending 2026-06- = **7.13** % (2026-01-01..2026-06-30) [DISCARD: Revenue YoY change; redundant with p153.] quote: "营业总收入: 3448.15亿元 同比下降7.13%"
  - p401 BYD net profit (净利润) cumulative for period ending 2026-06-30 = **12,325,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "\| 2026-06-30 \| 1.35 \| 26.32 \| 10.49 \| 13.72 \| 4.10 \| 3448.15亿 \| 123.25亿 \| 4.86% \| \|"
  - p402 BYD net profit (净利润) cumulative for period ending 2026-06-30, year-on-year chang = **20.54** % (2026-01-01..2026-06-30) [DISCARD: Net profit change; not revenue.] quote: "净利润: 123.25亿元 同比下降20.54%"
  - p403 BYD basic earnings per share cumulative for period ending 2026-06-30 = **1.35** CNY/share (2026-01-01..2026-06-30) [DISCARD: EPS; not revenue.] quote: "\| 2026-06-30 \| 1.35 \| 26.32 \| 10.49 \| 13.72 \| 4.10 \| 3448.15亿 \| 123.25亿 \| 4.86% \| \|"
  - p404 BYD gross margin for period ending 2026-06-30 = **18.85** % (2026-01-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "\| 每股净资产:26.32元 \| 毛利率:18.85% \| 净资产收益率:4.86% \| 流通A股:34.87亿股 \|"
  - p405 BYD total shares outstanding (总股本) = **9,117,000,000** share (2026-10-23..2026-10-23) [DISCARD: Share count; not needed.] quote: "\| 市盈率(静态): 22.92 \| 营业总收入: 3448.15亿元 同比下降7.13% \| 每股未分配利润:13.72元 \| 总股本: 91.17亿股 \|"
  - p406 BYD total market capitalisation (总市值) = **747,600,000,000** CNY (2026-10-23..2026-10-23) [DISCARD: Market cap; irrelevant.] quote: "\| 市净率: 3.12 \| 净利润: 123.25亿元 同比下降20.54% \| 每股经营现金流:4.09元 \| 总市值:7476亿 \|"
  - p407 BYD dynamic price-to-earnings ratio (市盈率(动态)) = **30.33** 1 (2026-10-23..2026-10-23) [DISCARD: P/E; irrelevant.] quote: "\| 市盈率(动态): 30.332 \| 每股收益:1.35元 \| 每股资本公积金:10.49元 \| 分类: 超大盘股 \|"
  - p408 BYD static price-to-earnings ratio (市盈率(静态)) = **22.92** 1 (2026-10-23..2026-10-23) [DISCARD: P/E; irrelevant.] quote: "\| 市盈率(静态): 22.92 \| 营业总收入: 3448.15亿元 同比下降7.13% \| 每股未分配利润:13.72元 \| 总股本: 91.17亿股 \|"
  - p409 BYD page data update date (更新日期) = **2,026** as written "2026-10-23", value check pending date (2026-10-23..2026-10-23) [DISCARD: Page update date; not a quantity.] quote: "\| 更新日期: 2026-10-23 \| 总质押股份数量: 2.44亿股 \|"
- `https://data.eastmoney.com/notices/detail/002594/AN202610141830468476,%E6%AF%94%E4%BA%9A%E8%BF%AA.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.cnfin.com/announ/detail/index.html?id=845334185104&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1014/2026101400381.pdf` -> **live_dated** (page date 2026-10-14); points raw/verified 4/4
  - p410 BYD board meeting date to approve unaudited Q3 2026 results = **29** as written "29 October 2026", value check pending date (day of month) (2026-10-29..2026-10-29) [DISCARD: Board meeting date; administrative.] quote: "a meeting of the Board will be held on Thursday, 29 October 2026 for the purposes"
  - p411 BYD unaudited third quarterly results reporting period end (nine months ended) = **30** as written "30 September 2026", value check pending date (day of month) (2026-09-30..2026-09-30) [DISCARD: Period end; administrative.] quote: "the unaudited third quarterly results of the Company for the nine months ended 30 September 2026"
  - p412 BYD Q3 report cumulative period length (nine months ended 30 September 2026) = **9** as written "nine", value check pending month (2026-01-01..2026-09-30) [DISCARD: Period length; administrative.] quote: "the unaudited third quarterly results of the Company for the nine months ended 30 September 2026"
  - p413 Notice of board meeting publication date (Shenzhen) = **14** as written "14 October 2026", value check pending date (day of month) (2026-10-14..2026-10-14) [DISCARD: Publication date; administrative.] quote: "Shenzhen, PRC, 14 October 2026"
- `https://www.cnfin.com/announ/detail/index.html?id=844705253353&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `https://wt.cfi.cn/p20261001000125.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.moomooapp.com/hant/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.tipranks.com/news/company-announcements/byd-sets-late-october-board-meeting-to-approve-q3-2026-results` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.cnfin.com/announ/detail/index.html?id=841279251474&code=002594&dannoun=lcdetail&announ=lc` -> **live_dated** (page date 2010-01-01); points raw/verified 0/0
- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/841438320321/index.phtml` -> **live_dated** (page date 2026-08-30); points raw/verified 15/14
  - p414 BYD 1H26 total revenue (analyst report, CNY) = **344,820,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 2026 revenue; redundant with p16.] quote: "1H26 总收入同比-7.1%至3,448.2 亿元(约占我们原全年预测的38%)"
  - p415 BYD 1H26 total revenue as share of prior full-year forecast (numerator 1H26 reve = **38** % (2026-01-01..2026-06-30) [DISCARD: Share of forecast; not a quantity.] quote: "1H26 总收入同比-7.1%至3,448.2 亿元(约占我们原全年预测的38%)"
  - p416 BYD 2Q26 operating revenue (analyst report, CNY) = **194,590,000,000** CNY (2026-04-01..2026-06-30) [keep: ] quote: "其中,2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p417 BYD 2Q26 operating revenue quarter-on-quarter change = **29.5** % (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p418 BYD 2Q26 operating revenue year-on-year change = **3.2** % (2026-04-01..2026-06-30) [keep: ] quote: "2Q26 营业收入同比-3.2%/环比+29.5%至1,945.9 亿元"
  - p419 BYD 1H26 total sales volume (vehicles) = **1,810,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 volume; not needed.] quote: "1H26 比亚迪总销量同比-15.7%至181 万辆"
  - p420 BYD 2Q26 sales volume quarter-on-quarter change = **58.2** % (2026-04-01..2026-06-30) [DISCARD: Q2 volume QoQ; not needed.] quote: "2Q26 业绩环比修复主要受益于销量改善(环比+58.2%)"
  - p421 BYD 1H26 domestic automotive and related business revenue (CNY) = **145,600,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 domestic auto revenue; not needed.] quote: "国内汽车及相关业务收入同比-33.6%至1,456 亿元、毛利率同比-0.7pcts 至17%"
  - p422 BYD 1H26 overseas automotive and related business revenue (CNY) = **129,500,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 overseas auto revenue; not needed.] quote: "海外汽车及相关业务收入同比+55.8%至1,295 亿元、毛利率同比+1.1pcts 至28.4%"
  - p423 BYD 1H26 gross margin = **18.8** % (2026-01-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率同比+0.8pcts 至18.8%"
  - p424 BYD 2Q26 gross margin = **18.9** % (2026-04-01..2026-06-30) [DISCARD: Gross margin; not revenue.] quote: "毛利率同比+2.6pcts/环比+0.1pcts 至18.9%"
  - p425 BYD 1H26 net profit attributable to parent (CNY) = **12,330,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "归母净利润同比-20.5%至123.3 亿元(约占我们原全年预测的33%)"
  - p426 BYD 2Q26 net profit attributable to parent (CNY) = **8,240,000,000** CNY (2026-04-01..2026-06-30) [DISCARD: Net profit; not revenue.] quote: "归母净利润同比+29.6%/环比+101.7%至82.4 亿元"
  - p427 BYD 1H26 R&D capitalisation rate (analyst estimate) = **19.2** % (2026-01-01..2026-06-30) [DISCARD: R&D capitalisation; not revenue.] quote: "我们测算1H26 研发资本化率约19.2% vs. 1H25 与2025 年分别约4.2%与8.6%"
- `https://data.eastmoney.com/notices/detail/01211/AN202610011830081567.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.moomooapp.com/hans/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 1 (scale word '亿' not supported by quote or table header: 1)

### b1 [forecasts_markets] Analyst consensus for BYD Q3 2026 revenue

Hypothesis: A broader consensus (not just Goldman) would resolve the material disagreement between the +10.2% (p200) and +25% (p188) revenue forecasts and anchor the level route; the Goldman volume premise (+19% YoY) looks inconsistent with reported September +17% and Jan-Sep -3.9%.

Queries issued by the searcher: BYD 3Q26 revenue consensus Wind 比亚迪 2026年三季度 营收 一致预期; BYD Q3 2026 revenue estimate Bloomberg consensus analysts; 比亚迪 2026年第三季度 营业收入 预测 券商 三季报前瞻 2300亿; 比亚迪 2025年第三季度 营业收入 1949.8亿 三季报; BYD 3Q26 revenue consensus Wind; 比亚迪 2026Q3 营收 一致预期; 比亚迪 2026年三季报 预测 营业收入 亿元 券商 三季度 同比; BYD Q3 2026 revenue estimate Bloomberg consensus analysts September quarter; BYD 3Q26 revenue consensus Wind; 比亚迪 2026年三季度 营业收入 一致预期; 比亚迪 2026年三季报 前瞻 营业收入 预测 券商 亿元; BYD 3Q26 preview revenue forecast October 2026 broker note RMB billion

- `https://www.cmbi.com.hk/article/13675.html?lang=en` -> **live_dated** (page date 2026-10-27); points raw/verified 0/0
- `https://hk.finance.yahoo.com/quote/81211.HK/analysis/` -> **dropped** (live http 503); points raw/verified -/-
- `https://twelvedata.com/markets/289238/stock/hkex/1211/analysis` -> **live_dated** (page date 2026-01-01); points raw/verified 15/13
  - p428 Number of analysts contributing to revenue estimate, next quarter (Dec 2026) = **2** analyst (2026-10-01..2026-12-31) [DISCARD: Analyst count for Dec quarter; irrelevant.] quote: "\| Number of Analysts \| 2 \| 18 \| 20 \|"
  - p429 Average revenue estimate, next quarter (Dec 2026) = **283,350,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Dec 2026 quarter estimate from stale 2026-01-01 snapshot; not Q3 and superseded.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p430 Low revenue estimate, next quarter (Dec 2026) = **277,970,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Stale Dec 2026 estimate; not target period.] quote: "\| Low estimate \| 277.97B \| 820.82B \| 928.04B \|"
  - p431 High revenue estimate, next quarter (Dec 2026) = **288,740,000,000** CNY (2026-10-01..2026-12-31) [DISCARD: Stale Dec 2026 estimate; not target period.] quote: "\| High estimate \| 288.74B \| 955.48B \| 1.21T \|"
  - p432 Sales growth (YoY) implied for next quarter (Dec 2026) = **0.19** 1 (2026-10-01..2026-12-31) [DISCARD: Stale Dec 2026 growth; not target period.] quote: "\| Sales growth \| 0.19 \| 0.11 \| 0.18 \|"
  - p433 Number of analysts contributing to revenue estimate, current year (Dec 2026) = **18** analyst (2026-01-01..2026-12-31) [DISCARD: Analyst count; irrelevant.] quote: "\| Number of Analysts \| 2 \| 18 \| 20 \|"
  - p434 Average revenue estimate, current year (Dec 2026) = **888,920,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Stale full-year 2026 estimate from Jan snapshot; superseded by later consensus.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p435 Low revenue estimate, current year (Dec 2026) = **820,820,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Stale full-year estimate.] quote: "\| Low estimate \| 277.97B \| 820.82B \| 928.04B \|"
  - p436 High revenue estimate, current year (Dec 2026) = **955,480,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Stale full-year estimate.] quote: "\| High estimate \| 288.74B \| 955.48B \| 1.21T \|"
  - p437 Sales growth (YoY) implied for current year (Dec 2026) = **0.11** 1 (2026-01-01..2026-12-31) [DISCARD: Stale full-year growth.] quote: "\| Sales growth \| 0.19 \| 0.11 \| 0.18 \|"
  - p438 Average revenue estimate, next year (Dec 2027) = **1,040,000,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 estimate; irrelevant.] quote: "\| Avg. estimate \| 283.35B \| 888.92B \| 1.04T \|"
  - p439 Number of analysts contributing to EPS estimate, current quarter (Sep 2026) = **2** analyst (2026-07-01..2026-09-30) [DISCARD: EPS analyst count; irrelevant.] quote: "\| Number of analysts \| 2 \| 2 \| 3 \| 4 \|"
  - p440 Average EPS estimate, current quarter (Sep 2026) = **1.3** CNY/share (2026-07-01..2026-09-30) [DISCARD: Stale EPS estimate from Jan snapshot; superseded by p442.] quote: "\| Average estimate \| 1.30 \| 1.54 \| 4.46 \| 5.67 \|"
- `https://beta.finance.yahoo.com/quote/0VSO.L/analysis/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.moomooapp.com/hans/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://mp.weixin.qq.com/s?__biz=MjM5MjcwMTkwMA==&mid=2652626645&idx=3&sn=1f27e73217575980ff65bc7a307d5742` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.moomooapp.com/hant/stock/01211-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://za.investing.com/equities/byd-co.-earnings?pageNum=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.boerse-express.com/news/articles/byd-aktie-schnell-meldung-953946` -> **live_dated** (page date 2026-10-17); points raw/verified 15/8
  - p441 Implied consensus Q3 2026 revenue YoY growth = **10.2** as written "10,2 %", value check pending % (2026-07-01..2026-09-30) [keep: ] quote: "Beim Umsatz werden 234,80 Milliarden CNY erwartet, rund 10,2 % mehr als die 213,06 Milliarden CNY ein Jahr zuvor."
  - p442 BYD consensus average Q3 2026 EPS estimate = **1.3** as written "1,30 CNY", value check pending CNY (2026-07-01..2026-09-30) [DISCARD: EPS estimate; not revenue.] quote: "Analysten rechnen im Schnitt mit 1,30 CNY Gewinn je Aktie, nach 0,94 CNY im Vorjahreszeitraum."
  - p443 BYD consensus full-year 2026 EPS estimate = **4.3** as written "4,30 CNY", value check pending CNY (2026-01-01..2026-12-31) [DISCARD: Full-year EPS; not revenue.] quote: "Der Konsens von mehr als drei Dutzend Analysten sieht den Gewinn je Aktie bei 4,30 CNY, nach 3,88 CNY im Vorjahr."
  - p444 BYD September 2026 NEV vehicle sales = **464** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "Im September verkaufte BYD 463.561 Fahrzeuge mit alternativen Antrieben."
  - p445 BYD January-September 2026 cumulative deliveries YoY change = **3.94** as written "3,94 %", value check pending % (2026-01-01..2026-09-30) [DISCARD: Cumulative change; redundant with p384.] quote: "Von Januar bis September summierten sich die Auslieferungen auf 3.131.576 Einheiten und lagen damit 3,94 % unter dem Vorjahreswert."
  - p446 BYD share price weekly change = **3.7** as written "3,7 %", value check pending % (not stated (page dated 2026-10-17)) [DISCARD: Share price; irrelevant.] quote: "BYD hat die Woche mit einem Minus von 3,7 % beendet und verlor am Freitag weitere 0,48 % auf 8,34 Euro."
  - p447 BYD share price below 200-day moving average = **17.6** as written "17,6 %", value check pending % (not stated (page dated 2026-10-17)) [DISCARD: Share price; irrelevant.] quote: "Damit liegt die Aktie inzwischen 17,6 % unter ihrer 200-Tage-Linie."
  - p448 BYD Q3 2026 results publication date = **29** day of month (2026-10-29..2026-10-29) [DISCARD: Results date; administrative.] quote: "Am 29. Oktober veröffentlicht der chinesische Autobauer seine Zahlen für das dritte Quartal 2026."
- `https://blog.tipranks.com/is-byddf-a-buy-before-earnings-pre-earnings-news/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://ru.investing.com/equities/byd-co.-earnings?cid=13884` -> **dropped** (live http 403); points raw/verified -/-
- `https://wwwhk.aastocks.com/en/stocks/news/aafn-con/NOW.1549400/popular-news/AAFN` -> **live_dated** (page date 2026-10-15); points raw/verified 15/13
  - p449 Goldman Sachs forecast BYD 3Q26 revenue (single-broker estimate, not consensus) = **242,936,000,000** CNY (2026-07-01..2026-09-30) [keep: ] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p450 Goldman Sachs forecast BYD 3Q26 revenue YoY growth = **25** % (2026-07-01..2026-09-30) [DISCARD: Goldman growth; redundant with p189.] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p451 Goldman Sachs forecast BYD 3Q26 revenue QoQ growth = **25** % (2026-07-01..2026-09-30) [DISCARD: Goldman growth; redundant with p190.] quote: "The broker forecast 3Q26 revenue of RMB242.936 billion, up 25% YoY and 25% QoQ"
  - p452 Goldman Sachs forecast BYD 3Q26 net profit = **11,500,000,000** CNY (2026-07-01..2026-09-30) [DISCARD: Net profit forecast; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p453 Goldman Sachs forecast BYD 3Q26 net profit YoY growth = **47** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p454 Goldman Sachs forecast BYD 3Q26 net profit QoQ growth = **39** % (2026-07-01..2026-09-30) [DISCARD: Net profit growth; not revenue.] quote: "while net profit is expected to reach RMB11.5 billion, up 47% YoY and 39% QoQ"
  - p455 Goldman Sachs assumed BYD 3Q26 sales volume growth YoY and QoQ = **19** % (2026-07-01..2026-09-30) [DISCARD: Goldman volume; redundant with p194.] quote: "The growth is mainly driven by a 19% increase in sales volume both YoY and QoQ"
  - p456 BYD domestic NEV retail market share in 2Q26 = **22** % (2026-04-01..2026-06-30) [DISCARD: Share; redundant with p195.] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p457 BYD domestic NEV retail market share in 3Q26 = **25** % (2026-07-01..2026-09-30) [DISCARD: Share; redundant with p196.] quote: "the company's domestic new energy vehicle retail market share increased from 22% in 2Q26 to 25% in 3Q26"
  - p458 BYD Hungary plant planned annual capacity (production expected to start by end-2 = **300,000** vehicle (not stated (page dated 2026-10-15)) [DISCARD: Hungary capacity; not realised output in Q3 2026.] quote: "planned annual capacity of 300,000 vehicles"
  - p459 China NEV export VAT rebate rate before 2027-04-01 = **13** % (..2027-03-31) [DISCARD: VAT rebate rate; irrelevant to Q3 2026.] quote: "the export VAT rebate rate for new energy vehicles will be reduced from 13% to 9%"
  - p460 Goldman Sachs assumed cost pass-through of VAT rebate cut = **67** % (not stated (page dated 2026-10-15)) [DISCARD: VAT pass-through assumption for 2027; irrelevant to Q3 2026.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
  - p461 Goldman Sachs estimated 2027 earnings reduction from VAT rebate cut = **4** % (2027-01-01..2027-12-31) [DISCARD: 2027 earnings effect; irrelevant.] quote: "assuming 67% cost pass-through, the change would reduce 2027 earnings by 4%"
- dropped by code checks: 11 (period year 2025 does not appear in the page text or URL (likely mis-dated): 4; number: unknown scale word 'Milliarden': 4; number: ambiguous separators: '.' used as a thousands separator: 1; period_end missing or unparseable: 2)

### b2 [physical_flow] Q3 2026 monthly sales and ASP decomposition

Hypothesis: July and August 2026 monthly wholesale volumes plus a Q3 ASP would let the unit-sales route (d2) be built directly rather than inferred from September and cumulative figures; the ASP is the largest uncertainty in that route.

Queries issued by the searcher: 比亚迪 2026年7月 销量 新能源汽车; 比亚迪 2026年8月 销量; 比亚迪 2026年9月 销量 产销快报; 比亚迪 单车均价 ASP 2026年 Q3 出口 国内 均价; 比亚迪 2026年7月 销量; 比亚迪 2026年8月 销量; 比亚迪 2026年9月 销量 产销快报; 比亚迪 2026 Q3 单车均价 ASP 三季度 营收 预测; 比亚迪 2026年7月 销量 新能源汽车; 比亚迪 2026年8月 销量 新能源汽车; 比亚迪 2026年9月 销量 产销快报; 比亚迪 3Q26 单车均价 ASP 三季度 预测

- `https://data.eastmoney.com/notices/detail/002594/AN202609011828888163.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/002594/AN202608021827568386.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/company/rptid/845640780089/index.phtml` -> **live_dated** (page date 2026-10-18); points raw/verified 15/14
  - p462 BYD September 2026 total vehicle sales = **463,561** vehicle (2026-09-01..2026-09-30) [keep: ] quote: "9 月汽车销量463561 辆,同比增长17%,环比增长5.3%"
  - p463 BYD cumulative 2026 year-to-date total vehicle sales (Jan-Sep) = **3,131,576** vehicle (2026-01-01..2026-09-30) [keep: ] quote: "今年累计汽车销量3131576 辆,同比下降3.9%"
  - p464 BYD September 2026 NEV passenger vehicle sales = **456,713** vehicle (2026-09-01..2026-09-30) [DISCARD: Sept PV; redundant with p72.] quote: "9 月新能源乘用车销量456713 辆,同比增长16.2%,环比增长5.4%"
  - p465 BYD cumulative 2026 year-to-date passenger vehicle sales (Jan-Sep) = **3,078,544** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative PV; not needed.] quote: "今年累计乘用车销量3078544 辆,同比下降4.4%"
  - p466 BYD September 2026 battery-electric passenger vehicle sales = **273,143** vehicle (2026-09-01..2026-09-30) [DISCARD: BEV split; not needed.] quote: "9 月纯电动乘用车销量273143 辆,同比增长33.2%"
  - p467 BYD September 2026 plug-in hybrid passenger vehicle sales = **183,570** vehicle (2026-09-01..2026-09-30) [DISCARD: PHEV split; not needed.] quote: "插混乘用车销量183570 辆,同比下降2.4%"
  - p468 BYD September 2026 domestic sales = **283,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Domestic; redundant with p77.] quote: "9 月国内销量28.3 万辆,同比下降13%,环比增长12.8%"
  - p469 BYD cumulative 2026 year-to-date domestic sales (Jan-Sep) = **1,789,000** vehicle (2026-01-01..2026-09-30) [DISCARD: Cumulative domestic; redundant with p108.] quote: "今年累计国内销量178.9 万辆,同比下降30%"
  - p470 BYD September 2026 NEV exports = **181,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Exports; redundant with p79.] quote: "9 月新能源汽车出口18.1万辆,同比增长153.6%,环比下降4.6%"
  - p471 BYD September 2026 export share of NEV sales = **39** % (2026-09-01..2026-09-30) [DISCARD: Export share; not needed.] quote: "销量占比39%,同比提升21pcts"
  - p472 BYD September 2026 Dynasty and Ocean network combined sales = **395,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Dynasty/Ocean; not needed.] quote: "9 月王朝与海洋网合计39.5万辆(同比+11.0%)"
  - p473 BYD September 2026 Fangchengbao brand sales = **43,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "方程豹4.3 万辆(同比+79.0%)"
  - p474 BYD September 2026 Denza brand sales = **18,000** vehicle (2026-09-01..2026-09-30) [DISCARD: Brand sales; not needed.] quote: "腾势1.8 万辆(同比+46.7%)"
  - p475 BYD September 2026 premium brands (Denza+Fangchengbao+Yangwang) combined share o = **13.5** % (2026-09-01..2026-09-30) [DISCARD: Premium share; not needed.] quote: "占乘用车销量13.5%,同比提升4pcts,高端品牌占比提升有助改善单车ASP"
- `https://irnews.cfbond.com/detail.html?newsid=Tey7c%2Fz7diI%3D` -> **live_dated** (page date 2026-08-04); points raw/verified 15/15
  - p476 BYD July 2026 NEV sales (monthly wholesale volume) = **419,000** vehicle (2026-07-01..2026-07-31) [keep: ] quote: "2026年7月,比亚迪新能源汽车销量达41.9万辆,同比增长21.8%"
  - p477 BYD July 2026 NEV sales year-on-year growth rate = **21.8** % (2026-07-01..2026-07-31) [DISCARD: July growth; not needed.] quote: "2026年7月,比亚迪新能源汽车销量达41.9万辆,同比增长21.8%"
  - p478 BYD H1 2026 NEV sales (cumulative, first half) = **1,809,000** vehicle (2026-01-01..2026-06-30) [DISCARD: H1 volume; not needed.] quote: "继2026年上半年以180.9万辆居中国新能源汽车销量首位后"
  - p479 BYD Dynasty + Ocean series July 2026 combined sales = **350,000** vehicle (2026-07-01..2026-07-31) [DISCARD: Dynasty/Ocean; not needed.] quote: "王朝、海洋系列依然是比亚迪销量的基本盘,7月合计销售35万辆,同比增长11.1%"
  - p480 BYD Dynasty + Ocean series July 2026 year-on-year growth rate = **11.1** % (2026-07-01..2026-07-31) [DISCARD: Dynasty/Ocean growth; not needed.] quote: "7月合计销售35万辆,同比增长11.1%"
  - p481 BYD premium brands (Fangchengbao, Denza, Yangwang) July 2026 combined sales, sta = **60,000** vehicle (2026-07-01..2026-07-31) [DISCARD: Premium brands; not needed.] quote: "方程豹、腾势、仰望合计销售超6万辆,同比增长约135%,占集团乘用车销量的14.8%"
  - p482 BYD premium brands July 2026 year-on-year growth rate, stated as approximately = **135** % (2026-07-01..2026-07-31) [DISCARD: Premium growth; not needed.] quote: "方程豹、腾势、仰望合计销售超6万辆,同比增长约135%"
  - p483 BYD premium brands share of group passenger vehicle sales, July 2026 = **14.8** % (2026-07-01..2026-07-31) [DISCARD: Premium share; not needed.] quote: "占集团乘用车销量的14.8%"
  - p484 Fangchengbao brand July 2026 sales = **41,000** vehicle (2026-07-01..2026-07-31) [DISCARD: Brand sales; not needed.] quote: "方程豹7月销售4.1万辆,创年内新高,同比增长190.6%,环比增长15.7%"
  - p485 Fangchengbao brand average transaction price (ASP), stated as over = **223,000** CNY (2026-07-01..2026-07-31) [DISCARD: Fangchengbao brand ASP; brand-level, not group ASP, and not needed.] quote: "品牌成交均价超过22.3万元,累计销量即将突破50万辆"
  - p486 Fangchengbao brand cumulative sales, stated as about to exceed = **500,000** vehicle (not stated (page dated 2026-08-04)) [DISCARD: Cumulative brand sales; irrelevant.] quote: "品牌成交均价超过22.3万元,累计销量即将突破50万辆"
  - p487 Denza brand July 2026 sales = **19,000** vehicle (2026-07-01..2026-07-31) [DISCARD: Brand sales; not needed.] quote: "腾势7月销售1.9万辆,同比增长68.8%"
  - p488 Yangwang brand July 2026 sales = **485** vehicle (2026-07-01..2026-07-31) [DISCARD: Brand sales; not needed.] quote: "仰望销售485辆,同比增长43.1%"
  - p489 BYD passenger vehicle and pickup overseas sales, July 2026, stated as nearly = **180,000** vehicle (2026-07-01..2026-07-31) [DISCARD: July overseas; not needed.] quote: "7月比亚迪乘用车及皮卡海外销售近18万辆,同比增长124.3%,创历史新高"
  - p490 BYD passenger vehicle and pickup overseas cumulative sales, January-July 2026 = **969,000** vehicle (2026-01-01..2026-07-31) [DISCARD: Cumulative overseas; not needed.] quote: "今年前7个月,比亚迪乘用车及皮卡海外累计销售96.9万辆"
- `https://data.eastmoney.com/notices/detail/002594/AN202610071830185793.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://stock.finance.sina.com.cn/stock/view/paper.php?symbol=sh000001&reportid=841688869045&autocallup=no&isfromsina=no` -> **live_dated** (page date 2022-01-01); points raw/verified 0/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/842429186459/index.phtml` -> **live_dated** (page date 2026-09-11); points raw/verified 15/14
  - p491 BYD August 2026 total vehicle sales (wholesale) = **440,293** vehicle (2026-08-01..2026-08-31) [keep: ] quote: "8 月汽车销售440,293 辆,同比+17.8%,环比+5.0%"
  - p492 BYD August 2026 domestic vehicle sales = **251,547** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug domestic; not needed.] quote: "国内汽车销量251,547 辆,同比-14.2%,环比+5.1%"
  - p493 BYD August 2026 passenger vehicle and pickup export sales = **188,746** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug exports; not needed.] quote: "乘用车及皮卡出口销量188,746 辆,同比+134.4%,环比+5.0%"
  - p494 BYD August 2026 passenger vehicle sales = **433,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug PV; redundant with p524.] quote: "公司8 月乘用车销售43.3 万辆,同比+16.7%,环比+5.4%"
  - p495 BYD January-August 2026 cumulative passenger vehicle sales = **2,622,000** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative PV; not needed.] quote: "1-8 月乘用车累计销售262.2 万辆,同比-7.2%"
  - p496 BYD August 2026 NEV export sales = **189,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug exports; not needed.] quote: "8 月新能源出口销量18.9 万辆,再创2026年单月新高,同比+134.4%,环比+5.0%"
  - p497 BYD January-August 2026 cumulative export sales = **1,158,000** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative exports; not needed.] quote: "1-8 月累计出口销量115.8 万辆,同比+85.7%"
  - p498 BYD July 2026 overseas terminal sales (MarkLines) = **82,534** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines terminal sales differ in definition from wholesale; not used.] quote: "根据MarkLines 数据,7 月公司海外终端销量82,534 辆,同比+76.7%"
  - p499 BYD January-July 2026 cumulative overseas terminal sales (MarkLines) = **558,000** vehicle (2026-01-01..2026-07-31) [DISCARD: MarkLines terminal sales; different definition.] quote: "1-7 月累计销量55.8 万辆,同比+82.9%"
  - p500 BYD July 2026 Europe sales (MarkLines) = **28,474** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines Europe terminal sales; not needed.] quote: "其中,欧洲销量28,474 辆,同比+109.5%"
  - p501 BYD July 2026 Brazil sales (MarkLines) = **22,937** vehicle (2026-07-01..2026-07-31) [DISCARD: MarkLines Brazil terminal sales; not needed.] quote: "拉美核心市场巴西销量22,937 辆,同比+138.1%"
  - p502 BYD August 2026 premium brand (Denza/Yangwang/Fangchengbao) combined sales = **58,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Premium brands; not needed.] quote: "腾势/仰望/方程豹销量分别1.6/0.04/4.2 万辆,合计5.8 万辆,占比13.2%"
  - p503 BYD August 2026 premium brand share of passenger vehicle sales = **13.2** % (2026-08-01..2026-08-31) [DISCARD: Premium share; not needed.] quote: "合计5.8 万辆,占比13.2%,相比2025 年8 月的占比7.7%提升明显"
  - p504 BYD August 2025 premium brand share of passenger vehicle sales (comparison) = **7.7** % (2025-08-01..2025-08-31) [DISCARD: Prior premium share; not needed.] quote: "相比2025 年8 月的占比7.7%提升明显,高端化持续推进"
- `https://wt.cfi.cn/p20261001000125.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://finance.sina.com.cn/jjxw/2026-09-02/doc-iniqmwqq4525262.shtml` -> **live_dated** (page date 2026-09-02); points raw/verified 15/15
  - p505 BYD August 2026 NEV sales (monthly wholesale, China) = **440,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug sales; redundant with p491.] quote: "当月,比亚迪销售新能源汽车超44万辆,获得中国车企销量冠军及新能源汽车销量冠军。"
  - p506 BYD August 2026 overseas sales of passenger vehicles and pickups = **189,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug overseas; redundant with p493.] quote: "8月,比亚迪乘用车及皮卡海外销售18.9万辆,同比增长134.6%"
  - p507 BYD August 2026 overseas sales year-on-year growth rate = **135** % (2026-08-01..2026-08-31) [DISCARD: Aug overseas growth; not needed.] quote: "8月,比亚迪乘用车及皮卡海外销售18.9万辆,同比增长134.6%"
  - p508 BYD August 2026 overseas sales increase over same month last year = **100,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug overseas increase; not needed.] quote: "较去年同期增加超过10万辆,连续第五个月刷新海外销量纪录。"
  - p509 BYD January-August 2026 cumulative overseas sales = **1,158,000** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative overseas; not needed.] quote: "1月至8月,比亚迪海外累计销售115.8万辆,已超过2025年全年104.96万辆的海外销量。"
  - p510 BYD full-year 2025 overseas sales (comparison base) = **1,049,600** vehicle (2025-01-01..2025-12-31) [DISCARD: FY2025 overseas; not needed.] quote: "已超过2025年全年104.96万辆的海外销量"
  - p511 BYD August 2026 sales lead over second-place automaker = **250,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Lead over second place; irrelevant.] quote: "比亚迪8月新能源汽车销量领先第二名近25万辆,夯实行业领先地位。"
  - p512 BYD Yuan family August 2026 sales = **84,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Model-level sales; not needed.] quote: "元家族销售8.4万辆,海豹家族销售4.7万辆"
  - p513 BYD Seal family August 2026 sales = **47,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Model-level sales; not needed.] quote: "元家族销售8.4万辆,海豹家族销售4.7万辆"
  - p514 BYD Fangchengbao plus Denza combined August 2026 sales = **58,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Brand sales; not needed.] quote: "8月方程豹、腾势合计销售5.8万辆,较去年同期增长超过一倍。"
  - p515 BYD Fangchengbao August 2026 sales = **42,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Brand sales; not needed.] quote: "方程豹销售4.2万辆,同比增长155.6%"
  - p516 BYD Fangchengbao August 2026 year-on-year sales growth rate = **156** % (2026-08-01..2026-08-31) [DISCARD: Brand growth; not needed.] quote: "方程豹销售4.2万辆,同比增长155.6%"
  - p517 BYD Denza August 2026 sales = **16,000** vehicle (2026-08-01..2026-08-31) [DISCARD: Brand sales; not needed.] quote: "腾势销售1.6万辆,同比增长33.4%"
  - p518 BYD Denza August 2026 year-on-year sales growth rate = **33.4** % (2026-08-01..2026-08-31) [DISCARD: Brand growth; not needed.] quote: "腾势销售1.6万辆,同比增长33.4%"
  - p519 BYD consecutive months ranked first in China NEV monthly sales (through August 2 = **63** month (2026-08-01..2026-08-31) [DISCARD: Ranking streak; irrelevant.] quote: "至此,比亚迪已连续63个月位居中国新能源汽车月度销量首位。"
- `https://qichejingwei.com/article-25700.html` -> **live_dated** (page date 2026-09-02); points raw/verified 9/9
  - p520 BYD August 2026 total vehicle sales (all vehicles, group) = **440,293** vehicle (2026-08-01..2026-08-31) [keep: ] quote: "比亚迪 8 月汽车销量达 440293 辆"
  - p521 BYD August 2026 NEV production volume = **440,703** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug production; not needed.] quote: "比亚迪 8 月新能源汽车产量为 440703 辆"
  - p522 BYD August 2026 battery-electric passenger vehicle sales = **256,230** vehicle (2026-08-01..2026-08-31) [DISCARD: BEV split; not needed.] quote: "其中纯电动乘用车销量 256230 辆"
  - p523 BYD August 2026 plug-in hybrid passenger vehicle sales = **177,154** vehicle (2026-08-01..2026-08-31) [DISCARD: PHEV split; not needed.] quote: "插电式混合动力乘用车销量 177154 辆"
  - p524 BYD August 2026 passenger vehicle sales (group) = **433,384** vehicle (2026-08-01..2026-08-31) [keep: ] quote: "8 月集团乘用车销量达 433384 辆"
  - p525 BYD August 2026 overseas sales of passenger vehicles and pickups = **188,746** vehicle (2026-08-01..2026-08-31) [DISCARD: Aug overseas; redundant with p493.] quote: "8 月比亚迪乘用车及皮卡海外销量达 188746 辆"
  - p526 BYD August 2026 overseas sales year-on-year growth rate (passenger vehicles and  = **135** % (2026-08-01..2026-08-31) [DISCARD: Aug overseas growth; not needed.] quote: "同比大幅增长 134.6%"
  - p527 BYD cumulative January-August 2026 group vehicle sales = **2,668,015** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative Aug; not needed.] quote: "2026 年 1-8 月集团汽车累计销量突破 266 万辆,达 2668015 辆"
  - p528 BYD cumulative January-August 2026 group vehicle sales (rounded, as stated in te = **2,660,000** vehicle (2026-01-01..2026-08-31) [DISCARD: Cumulative Aug; not needed.] quote: "比亚迪累计销量超 266 万辆"
- `https://finance.sina.com.cn/roll/2026-08-02/doc-inikxmtc2853464.shtml` -> **live_dated** (page date 2026-08-02); points raw/verified 6/4
  - p529 BYD July 2026 NEV sales (vehicles) = **419,211** vehicle (2026-07-01..2026-07-31) [keep: ] quote: "新能源汽车销量为419,211辆,去年同期为344,296辆,同比增长21.76%"
  - p530 BYD July 2026 NEV production (vehicles) = **420,249** vehicle (2026-07-01..2026-07-31) [DISCARD: July production; not needed.] quote: "公司2026年7月新能源汽车产量为420,249辆,去年同期为317,892辆,同比增长32.20%"
  - p531 BYD July 2026 NEV sales year-on-year growth rate = **21.76** % (2026-07-01..2026-07-31) [DISCARD: July growth; not needed.] quote: "新能源汽车销量为419,211辆,去年同期为344,296辆,同比增长21.76%"
  - p532 BYD July 2026 NEV production year-on-year growth rate = **32.2** % (2026-07-01..2026-07-31) [DISCARD: July production growth; not needed.] quote: "公司2026年7月新能源汽车产量为420,249辆,去年同期为317,892辆,同比增长32.20%"
- `https://data.eastmoney.com/notices/detail/81211/AN202608021827568386.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- dropped by code checks: 4 (scale word '万' not supported by quote or table header: 1; scale word '亿' not supported by quote or table header: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### b3 [related_series] BYD Electronic Q3 2026 revenue

Hypothesis: BYD Electronic reports Q3 results on 29 Oct 2026; its standalone Q3 revenue (converted to CNY) would complete the segment-sum route (d3) for the electronics/other ~20% of group revenue.

Queries issued by the searcher: 比亚迪电子 2026 第三季度 营收; BYD Electronic 00285.HK 2026 interim results revenue; 比亚迪电子 2025年 前三季度 营业额 第三季度 业绩 截至2025年9月30日止九个月; 比亚迪电子 2026年第一季度 营业额 381.83亿; 比亚迪电子 2026 中期业绩 营业额; BYD Electronic 00285.HK 2026 interim results revenue; 比亚迪电子 2025年第三季度 营业额 前三季度 业绩公告; 比亚迪电子 2026年第一季度 营业额 381.83亿; BYD Electronic 2026 third quarter revenue 00285.HK; 比亚迪电子 2026 第三季度 营收; 比亚迪电子 2025年第三季度 收入 前三季度 营收 亿元; 比亚迪电子 2026 三季度 业绩预测 收入 环比 改善 研报

- `https://stock.finance.sina.com.cn/hkstock/view/hk_report.php?reportid=815492069222` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://simplywall.st/stocks/hk/tech/hkg-285/byd-electronic-international-shares/news/byd-electronic-sehk285-profit-slump-deepens-pressure-on-rich` -> **live_dated** (page date 2026-08-29); points raw/verified 0/0
- `https://www.163.com/dy/article/L97FJB4U05198ETO.html` -> **live_dated** (page date 2026-10-14); points raw/verified 3/3
  - p533 BYD Electronic board meeting date to approve unaudited Q3 results for nine month = **20,261,029** as written "2026年10月29日", value check pending date (2026-10-29..2026-10-29) [DISCARD: Board meeting date; administrative, not revenue.] quote: "谨定于2026年10月29日(星期四)举行董事会会议"
  - p534 BYD Electronic unaudited Q3 results period end date (nine months ended) = **20,260,930** as written "2026年9月30日", value check pending date (2026-09-30..2026-09-30) [DISCARD: Period end; administrative.] quote: "公司截至2026年9月30日止九个月之未经审核第三季度业绩"
  - p535 Number of months in BYD Electronic's reported cumulative period (nine months) = **9** as written "九个月", value check pending month (2026-01-01..2026-09-30) [DISCARD: Period length; administrative.] quote: "公司截至2026年9月30日止九个月之未经审核第三季度业绩"
- `http://202.62.215.11/www/tc//stocks/realtime/quote_news_detail.php?section=related&code=00285&newsid=ETN360829306` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://hk.stockstar.com/IG2026090100015216.shtml` -> **live_dated** (page date 2026-09-01); points raw/verified 15/15
  - p536 BYD Electronic 2026H1 total revenue = **82,234,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: H1 electronics revenue; not needed for Q3 level.] quote: "比亚迪电子(00285.HK)2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p537 BYD Electronic 2026H1 revenue year-on-year growth = **2.02** % (2026-01-01..2026-06-30) [DISCARD: H1 electronics growth; not needed for Q3 level.] quote: "2026年上半年实现营收822.34亿元,同比增长2.02%"
  - p538 BYD Electronic 2026H1 net profit attributable to parent = **426,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics net profit; not revenue.] quote: "归母净利润4.26亿元,同比下降75.35%"
  - p539 BYD Electronic 2026H1 gross margin year-on-year change (percentage points) = **1.97** percentage points (2026-01-01..2026-06-30) [DISCARD: Electronics gross margin change; not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p540 BYD Electronic 2026H1 gross margin = **4.91** % (2026-01-01..2026-06-30) [DISCARD: Electronics gross margin; not revenue.] quote: "毛利率同比下降1.97个百分点至4.91%"
  - p541 BYD Electronic 2026H1 smart terminal business revenue = **67,348,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "2026H1智能终端业务收入673.48亿元,同比增长约1.4%"
  - p542 BYD Electronic 2026H1 assembly business revenue = **55,522,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "其中组装业务收入555.22亿元,同比增长约5.1%"
  - p543 BYD Electronic 2026H1 components business revenue = **11,826,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "零部件业务收入118.26亿元,同比下降约13.3%"
  - p544 BYD Electronic 2026H1 new energy vehicle business revenue = **13,515,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "2026H1新能源汽车业务收入135.15亿元,同比增长6.4%"
  - p545 BYD Electronic 2026H1 AI computing infrastructure revenue = **751,000,000** CNY (2026-01-01..2026-06-30) [DISCARD: Electronics sub-segment; not needed.] quote: "AI算力基础设施方面,2026H1实现收入7.51亿元,同比下降9.74%"
  - p546 BYD Electronic server business full-year 2026 revenue forecast (at least) = **3,000,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Server revenue forecast; immaterial and not needed.] quote: "服务器业务全年收入预计达30亿元以上"
  - p547 CSC forecast BYD Electronic 2026 revenue = **181,086,000,000** CNY (2026-01-01..2026-12-31) [DISCARD: Full-year electronics forecast; not Q3.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p548 CSC forecast BYD Electronic 2027 revenue = **199,602,000,000** CNY (2027-01-01..2027-12-31) [DISCARD: 2027 electronics forecast; irrelevant.] quote: "中信建投预计2026-2027年公司收入分别为1810.86亿元和1996.02亿元"
  - p549 CSC forecast BYD Electronic 2026 revenue year-on-year growth = **0.9** % (2026-01-01..2026-12-31) [DISCARD: Full-year electronics growth; not Q3.] quote: "同比增长0.90%和10.23%"
  - p550 CSC forecast BYD Electronic 2027 revenue year-on-year growth = **10.23** % (2027-01-01..2027-12-31) [DISCARD: 2027 electronics growth; irrelevant.] quote: "同比增长0.90%和10.23%"
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/00285/NOW.1542369/hk-stock-news` -> **live_dated** (page date 2026-09-01); points raw/verified 6/6
  - p551 Citi target price for BYD Electronic, raised from prior target (upper bound of t = **28** HKD (2026-10-27..2026-10-27) [DISCARD: Target price; irrelevant to revenue.] quote: "将公司目标价由22.6元上调至28元"
  - p552 Citi prior target price for BYD Electronic before upgrade = **22.6** HKD (2026-10-27..2026-10-27) [DISCARD: Target price; irrelevant.] quote: "将公司目标价由22.6元上调至28元"
  - p553 BYD Electronic share price change on the report day (absolute) = **-0.6** HKD (2026-10-27..2026-10-27) [DISCARD: Share price move; irrelevant.] quote: "比亚迪电子(00285.HK) -0.600 (-2.657%)"
  - p554 BYD Electronic share price change on the report day (percent) = **-2.657** % (2026-10-27..2026-10-27) [DISCARD: Share price move; irrelevant.] quote: "比亚迪电子(00285.HK) -0.600 (-2.657%)"
  - p555 BYD Electronic short-selling turnover (as of 2026-10-27 16:25) = **73,600,000** HKD (2026-10-27..2026-10-27) [DISCARD: Short-selling; irrelevant.] quote: "沽空 $7.36千万; 比率 49.426%"
  - p556 BYD Electronic short-selling ratio (short turnover as share of total turnover) = **49.43** % (2026-10-27..2026-10-27) [DISCARD: Short-selling; irrelevant.] quote: "沽空 $7.36千万; 比率 49.426%"
- `https://basic.10jqka.com.cn/00285/` -> **live_dated** (page date 2026-06-30); points raw/verified 15/5
  - p557 BYD Electronic H1 2026 sales revenue year-on-year growth rate = **2.02** % (2026-01-01..2026-06-30) [keep: ] quote: "二零二六年上半年,集团录得销售额约人民币82,234百万元,同比上升约2.02%。"
  - p558 BYD Electronic H1 2026 profit attributable to shareholders year-on-year decline  = **75.35** % (2026-01-01..2026-06-30) [DISCARD: Electronics profit decline; not revenue.] quote: "股东应占溢利同比下降约75.35%至约人民币426百万元"
  - p559 BYD Electronic H1 2026 new energy vehicle business share of group total revenue = **16.56** % (2026-01-01..2026-06-30) [DISCARD: Electronics NEV share; not needed.] quote: "占集团总体收入约16.56%"
  - p560 BYD Electronic H1 2026 new energy vehicle business revenue year-on-year growth r = **6.43** % (2026-01-01..2026-06-30) [DISCARD: Electronics NEV growth; not needed.] quote: "收入同比上升约6.43%"
  - p561 BYD Electronic H1 2026 AI computing infrastructure business revenue year-on-year = **10.57** % (2026-01-01..2026-06-30) [DISCARD: Electronics AI growth; not needed.] quote: "同比下降约10.57%"
- `https://data.eastmoney.com/notices/detail/00285/AN202608281828634287.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.moomooapp.com/hans/stock/00285-HK/earnings` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://stockanalysis.com/quote/hkg/0285/statistics/` -> **live_dated** (page date 2026-10-27); points raw/verified 15/0
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/285/hk6/now.1480270/hk-stock-news` -> **live_dated** (page date 2025-10-30); points raw/verified 5/5
  - p562 BYD Electronic first three quarters (Jan-Sep 2026) revenue, CNY = **123,285,000,000** CNY (2026-01-01..2026-09-30) [DISCARD: Mislabeled: 1,232.85bn is 9M 2025 (per p567), not 2026; would corrupt electronics Q3 route.] quote: "公布截至今年9月底止首三季业绩,营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p563 BYD Electronic first three quarters (Jan-Sep 2026) revenue year-on-year change = **0.9** % (2026-01-01..2026-09-30) [DISCARD: Same mislabeled 2025 vintage as p562.] quote: "营业额1,232.85亿元人民币(下同),按年升0.9%。"
  - p564 BYD Electronic first three quarters (Jan-Sep 2026) net profit, CNY = **3,137,000,000** CNY (2026-01-01..2026-09-30) [DISCARD: Same mislabeled 2025 vintage as p562.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p565 BYD Electronic first three quarters (Jan-Sep 2026) net profit year-on-year chang = **2.4** % (2026-01-01..2026-09-30) [DISCARD: Same mislabeled 2025 vintage as p562.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
  - p566 BYD Electronic first three quarters (Jan-Sep 2026) earnings per share, CNY = **1.39** CNY/share (2026-01-01..2026-09-30) [DISCARD: Same mislabeled 2025 vintage as p562.] quote: "纯利31.37亿元,按年升2.4%;每股盈利1.39元。"
- `https://wap.stockstar.com/detail/AN2025103000040467` -> **live_dated** (page date 2026-10-27); points raw/verified 15/9
  - p567 BYD Electronic nine-month revenue, nine months ended 2025-09-30 (as written, 萬人民 = **1,232,852,500,000** CNY (2025-01-01..2025-09-30) [DISCARD: Unit error: stated 萬人民幣千元 but value 1000x too large; 9M 2025 electronics revenue not needed for Q3 2026.] quote: "截至二零二五年九月三十日止九個月,本集團營業額為123,285,250萬人民幣千元"
  - p568 BYD Electronic nine-month revenue year-on-year change, nine months ended 2025-09 = **0.95** % (2025-01-01..2025-09-30) [DISCARD: 9M 2025 electronics growth; not needed.] quote: "較二零二四年同期的122,126,912萬人民幣千元上升0.95%"
  - p569 BYD Electronic nine-month gross profit, nine months ended 2025-09-30 (as written = **84,892,520,000** CNY (2025-01-01..2025-09-30) [DISCARD: Unit error (萬千元) and gross profit not needed.] quote: "毛利為8,489,252萬人民幣千元"
  - p570 BYD Electronic nine-month gross profit year-on-year change, nine months ended 20 = **6.32** % (2025-01-01..2025-09-30) [DISCARD: Electronics gross profit; not revenue.] quote: "較去年同期的9,062,077萬人民幣千元減少6.32%"
  - p571 BYD Electronic profit attributable to owners of the parent, nine months ended 20 = **31,367,770,000** CNY (2025-01-01..2025-09-30) [DISCARD: Unit error and profit not needed.] quote: "母公司權益擁有人應佔溢利為3,136,777萬人民幣千元"
  - p572 BYD Electronic basic and diluted earnings per share, nine months ended 2025-09-3 = **1.39** CNY per share (2025-01-01..2025-09-30) [DISCARD: EPS; not revenue.] quote: "每股盈利(基本及攤薄)為人民幣1.39元"
  - p573 BYD Electronic total assets at 2025-09-30 (as written, 萬人民幣千元) = **869,743,030,000** CNY (2025-09-30..2025-09-30) [DISCARD: Unit error; balance sheet not needed.] quote: "於二零二五年九月三十日,總資產為86,974,303萬人民幣千元"
  - p574 BYD Electronic total liabilities at 2025-09-30 (as written, 萬人民幣千元) = **528,706,800,000** CNY (2025-09-30..2025-09-30) [DISCARD: Unit error; balance sheet not needed.] quote: "總負債為52,870,680萬人民幣千元"
  - p575 BYD Electronic net assets at 2025-09-30 (as written, 萬人民幣千元) = **341,036,230,000** CNY (2025-09-30..2025-09-30) [DISCARD: Unit error; balance sheet not needed.] quote: "資產淨值為34,103,623萬人民幣千元"
- dropped by code checks: 31 (scale word 'million' not supported by quote or table header: 10; value_as_written not in quote as a whole number: 5; period_end missing or unparseable: 10; period year 2024 does not appear in the page text or URL (likely mis-dated): 6)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['byd revenue', 'byd q3 2026', 'byd quarterly results']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p58', 'p2', 'p6', 'p397'] All describe BYD Q3 2025 / 9M 2025 consolidated revenue; p1 and p58 are the same Q3 2025 figure (194.98-194.99bn) from the same Sina-family source, so they are one measurement, not two.
- corroborating: ['p16', 'p30', 'p43', 'p168', 'p395', 'p414'] H1 2026 revenue ~344.8bn CNY repeated across Sina, Eastmoney, etnet, 10jqka and an analyst note; largely the same reported H1 filing re-quoted, so effectively one underlying measurement.
- corroborating: ['p17', 'p31', 'p44', 'p416'] Q2 2026 single-quarter revenue 194.59bn repeated; same H1 filing, one measurement.
- corroborating: ['p18', 'p32', 'p45', 'p418'] Q2 2026 YoY -3.15% to -3.2%, consistent across re-quotes.
- corroborating: ['p19', 'p33', 'p417'] Q2 2026 QoQ +29.5%, consistent; implies Q1 2026 ~150.2bn, matching p396.
- corroborating: ['p396', 'p17', 'p30'] Q1 2026 150.225bn + Q2 194.59bn = H1 344.815bn, internally consistent.
- corroborating: ['p71', 'p84', 'p93', 'p104', 'p332', 'p366', 'p376', 'p391'] September 2026 total NEV sales 463,561 units, repeated across many outlets; one monthly sales announcement.
- corroborating: ['p72', 'p86', 'p94', 'p333', 'p369', 'p379'] September 2026 passenger vehicle sales 456,713 units, consistent.
- corroborating: ['p79', 'p90', 'p92', 'p106', 'p335', 'p374', 'p387', 'p393'] September 2026 NEV exports ~180,700 units, consistent; p79/p335 round to 181,000.
- corroborating: ['p75', 'p85', 'p102', 'p107', 'p343', 'p373', 'p383', 'p394'] Jan-Sep 2026 cumulative sales 3,131,576 units, consistent.
- corroborating: ['p77', 'p105', 'p334'] September 2026 domestic sales ~283,000 units, consistent.
- corroborating: ['p188', 'p354', 'p189', 'p355', 'p190', 'p356', 'p345', 'p346'] Goldman Sachs Q3 2026 revenue forecast 242.936bn, +25% YoY / +25% QoQ; same broker note re-quoted, one forecast.
- conflicting: ['p200', 'p188'] Consensus-style +10.2% YoY (implying ~214.9bn) vs Goldman +25% (~242.9bn). Material disagreement; p200's stated prior-year base of 213.06bn does not match the reported Q3 2025 194.98bn, so its base is
- conflicting: ['p194', 'p349', 'p360', 'p71', 'p84'] Goldman's +19% YoY volume growth for Q3 2026 is inconsistent with reported September +17% and Jan-Sep -3.9%; the volume premise behind the +25% revenue forecast looks too high.
- corroborating: ['p195', 'p196', 'p351', 'p352', 'p361', 'p362'] BYD domestic NEV retail share 22% (Q2) to 25% (Q3) 2026; same Goldman note.
- corroborating: ['p205', 'p226', 'p274', 'p303', 'p314'] China NEV passenger wholesale September 2026 1.666m, +11.3% YoY; CPCA-based, multiple re-quotes.
- corroborating: ['p214', 'p323', 'p242', 'p309'] BYD September NEV passenger wholesale ~455-457k; CPCA vs company figures differ slightly by definition (passenger vs total).
- corroborating: ['p130', 'p147', 'p170', 'p187'] BYD Electronic H1 2026 revenue ~82.2bn CNY, +2%; consistent across sources.
- corroborating: ['p173', 'p53', 'p186', 'p154'] Automotive segment H1 2026 revenue 275.341bn, -9% YoY; consistent.
- corroborating: ['p410', 'p411', 'p412', 'p145', 'p146'] Q3 2026 results board meeting 29 Oct 2026, nine months ended 30 Sep 2026; confirms reporting basis and that Q3 standalone must be derived from 9M minus H1 if not shown separately.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p58'] Q3 2025 revenue ~194.98bn; same report, not independent.
- corroborating: ['p16', 'p30', 'p43', 'p168', 'p395'] H1 2026 revenue ~344.8bn; same figure, redundant copies.
- corroborating: ['p17', 'p31', 'p44', 'p416'] Q2 2026 revenue 194.59bn; same figure.
- corroborating: ['p18', 'p32', 'p45', 'p418'] Q2 YoY ~-3.2%; same figure.
- corroborating: ['p19', 'p33', 'p417'] Q2 QoQ +29.5%; same figure.
- corroborating: ['p71', 'p84', 'p93', 'p104', 'p332', 'p366', 'p376', 'p391', 'p444', 'p462'] Sept 2026 sales 463,561; same company disclosure.
- corroborating: ['p75', 'p85', 'p102', 'p107', 'p343', 'p373', 'p383', 'p394', 'p463'] Jan-Sep 3,131,576 units, -3.9%; same disclosure.
- corroborating: ['p476', 'p529'] July 2026 sales 419,000 vs 419,211; rounding.
- corroborating: ['p491', 'p520'] Aug 2026 sales 440,293; same disclosure.
- corroborating: ['p188', 'p354', 'p449'] Goldman 3Q26 242.9bn (+25%); single broker.
- conflicting: ['p188', 'p200', 'p441'] Goldman +25% vs consensus +10.2%; Goldman volume premise (+19%) inconsistent with reported -3.9% YTD.
- corroborating: ['p66', 'p69', 'p1'] Q3 2025: 1.1142m units x 136.7k ASP ~ 194.98bn revenue; internally consistent.
- corroborating: ['p53', 'p173', 'p170'] H1 2026 segments: auto 2753.41bn + electronics 694.05bn = 3447.46bn ~ total; consistent split.
- corroborating: ['p130', 'p536', 'p147', 'p557'] BYD Electronic H1 2026 revenue 822.34bn, +2.02%; same figure.
- conflicting: ['p562', 'p567'] p562 labels 1,232.85bn as Jan-Sep 2026 but p567 shows same value is 9M 2025; p562 is a mislabeled 2025 vintage.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Q3 2026 revenue growth factor vs Q3 2025 | 1.08 | 0.95..1.22 | 0.95..1.22 | 1 | m1 (m1) | Consensus ~+10.2% (p441) vs Goldman +25% (p189); reported Jan-Sep volume -3.9% (p384) and September +17% (p376) argue for modest growth, closer to consensus than Goldman. | Q3 2026 revenue tracks volume and ASP trends similar to reported months. | Q3 volume or ASP materially above/below reported monthly trend. |
| a2 | Q3 2026 revenue QoQ growth factor vs Q2 2026 | 1.05 | 0.92..1.2 | 0.92..1.2 | 1 | m2 (m2) | Q3 volume (July 419k, Aug 440k, Sep 464k) modestly above Q2 average; seasonal Q3/Q2 ratio historically near 1.0-1.1. | Q3 volume and ASP follow reported monthly pattern. | Q3 volume or ASP materially different from monthly reports. |
| a3 | Q3 2026 group revenue per vehicle (ASP) | 138,000 | 122,000..155,000 | 97,237..194,474 (widened) | CNY/vehicle | unused | Q3 2025 ASP 136.7k (p69); richer export/premium mix (p475, p336) supports slight uplift; price competition caps upside. | Group ASP stays near recent history with modest mix improvement. | Sharp ASP decline from price war or mix shift. |
| a4 | Q3 2026 share of Jan-Sep volume falling in Q3 | 0.42 | 0.38..0.46 | 0.2956..0.5913 (widened) | 1 | unused | Q3 volume = 419k+440k+464k ~ 1.32m of 3.13m YTD ~ 0.42; derived from monthly reports. | Monthly reported volumes are accurate. | Revised monthly volumes. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 211,875,655,499 | ['p1'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 206,063,306,262 | ['p17'] / ['a2'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p1 * a1; Monte Carlo P10 to P90 169,823,969,003 to 263,877,393,124; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p17 * a2; Monte Carlo P10 to P90 164,428,348,210 to 259,477,406,261; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 211,875,655,499 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 206,063,306,262 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.08 (not above one, so no widening); final width x/÷1.38.

Result: central **208,949,271,568** CNY, 80% interval [151,669,469,654, 287,861,480,549] CNY, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

Unit of the estimate: CNY (total for 2026-07-01 to 2026-09-30)

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['bcl', 'byd', 'byd company limited', 'cny', 'hkex', 'limited']; measure stems ['byd', 'cny', 'conso', 'limit', 'opera', 'reven']; 3 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

Best estimate for BYD Company Limited consolidated operating revenue (营业收入) for the three months 2026-[n]-[n] to 2026-[n]-[n], as first reported in the 'The Reporting Period' column of the unaudited Q3 2026 report: 208,949,271,568 CNY (80% model-based interval 151,669,469,654 to 287,861,480,549 CNY).

Evidence: m1 scales observed Q3 2025 revenue 194,984,598,000 CNY by assumption a1 (1.08, range 0.95 to 1.22); m2 scales observed Q2 2026 revenue 194,590,000,000 CNY by assumption a2 (1.05, range 0.92 to 1.2). Both observed points are actual reported figures; the growth factors are analyst assumptions, not observations. Code combined the two blocks by geometric mean with equal weight per block (50% and 50%), because their inputs overlap by at least half; no backtest error evidence was available, so widths are default.

Main risk: the growth factors are judgmental, and volume trends (Jan-Sep down, September up) conflict with consensus-versus-bull-case disagreement. Missing evidence that would most improve this: actual Q3 monthly revenue or a reliable consensus figure for the standalone quarter.

Unit of the estimate: CNY (total for 2026-07-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Q3 2026 revenue growth factor vs Q3 2025: 1.08 [n], range 0.95 to 1.22; used by m1. Overturned by: Q3 volume or ASP materially above/below reported monthly trend.
- a2 Q3 2026 revenue QoQ growth factor vs Q2 2026: 1.05 [n], range 0.92 to 1.2; used by m2. Overturned by: Q3 volume or ASP materially different from monthly reports.

Method details (computed by code):
- m1 formula_mc: p1 * a1; Monte Carlo P10 to P90 169,823,969,003 to 263,877,393,124; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p17 * a2; Monte Carlo P10 to P90 164,428,348,210 to 259,477,406,261; result unit (0.3333333333 CNY/month) * 92 day converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 211,875,655,499 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 206,063,306,262 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.08 (not above one, so no widening); final width x/÷1.38.

# Evidence ledger: fc_cn_profits_2026_09

- Question: Assume today is 2026-10-24. You know nothing published after this date. Estimate the total profits of China's industrial enterprises above designated size (规模以上工业企业利润总额) for January-September 2026 (the cumulative total, not the single month of September), in Chinese yuan (CNY; the release states it in 亿元, i.e. units of 100 million yuan), as it will be first reported in the National Bureau of Statistics of China's monthly release on profits of industrial enterprises.
- as_of: 2026-10-24
- Pinned target: Cumulative total profits of industrial enterprises above designated size (规模以上工业企业利润总额) in mainland China for January-September 2026, as first reported by the National Bureau of Statistics of China in its monthly industrial profits release. This is the year-to-date cumulative total at current prices | unit 亿元 (100 million CNY) | period 2026-01-01..2026-09-30 | publisher National Bureau of Statistics of China (NBS)

## Directions and pages

### d1 [own_history] NBS monthly release / time-series analyst

Hypothesis: The January-September cumulative figure is the January-August cumulative figure plus September monthly profit. January-August 2026 is likely published before the cutoff; September monthly can be anchored by the historical September increment as a share of January-August or by September 2025 monthly profit updated with current growth. This route directly constrains the level.

Queries issued by the searcher: 2026年1-8月份全国规模以上工业企业利润总额 国家统计局; 2025年1-9月份全国规模以上工业企业利润总额 亿元 国家统计局; 2025年1-8月份全国规模以上工业企业利润总额 46929 亿元; 2026年9月 规模以上工业企业利润 单月 同比 预测 1-9月累计

- `https://www.stats.gov.cn/sj/zxfbhjd/202609/t20260928_1965425.html` -> **live_dated** (page date 2026-09-28); points raw/verified 15/7
  - p1 Year-on-year growth of cumulative total profits of industrial enterprises above  = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,全国规模以上工业企业实现利润总额52719.8亿元,同比增长15.7%(按可比口径计算,详见附注二)。"
  - p2 Year-on-year growth of monthly total profits of industrial enterprises above des = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月份,规模以上工业企业利润同比增长4.2%。"
  - p3 Cumulative operating revenue of industrial enterprises above designated size, Ch = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;"
  - p4 Operating revenue profit ratio (profit total / operating revenue) of industrial  = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p5 Cumulative total profits of industrial enterprises above designated size, comput = **8,475** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "\| 计算机、通信和其他电子设备制造业 \| 128102.9 \| 20.1 \| 108422.9 \| 16.7 \| 8474.7 \| 109.9 \|"
  - p6 Cumulative total profits of industrial enterprises above designated size, automo = **2,534** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "\| 汽车制造业 \| 70061.6 \| 2.9 \| 62370.3 \| 4.0 \| 2533.8 \| -16.0 \|"
  - p7 Statistical scope threshold: annual main business revenue for industrial enterpr = **20,000,000** CNY (not stated (page dated 2026-09-28)) [keep: ] quote: "规模以上工业企业,即年主营业务收入为2000万元及以上的工业法人单位。"
- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202510/t20251027_1961695.html` -> **live_dated** (page date 2025-10-27); points raw/verified 15/7
  - p8 China industrial enterprises above designated size cumulative total profit year- = **3.2** % (2025-01-01..2025-09-30) [keep: ] quote: "1-9月份,全国规模以上工业企业实现利润总额53732.0亿元,同比增长3.2%(按可比口径计算,详见附注二)。"
  - p9 China industrial enterprises above designated size total profit year-on-year gro = **21.6** % (2025-09-01..2025-09-30) [keep: ] quote: "9月份,规模以上工业企业利润同比增长21.6%。"
  - p10 China industrial enterprises above designated size cumulative revenue, January-S = **102,080,000,000,000** CNY (2025-01-01..2025-09-30) [keep: ] quote: "1-9月份,规模以上工业企业实现营业收入102.08万亿元,同比增长2.4%"
  - p11 China industrial enterprises above designated size revenue profit margin (profit = **5.26** % (2025-01-01..2025-09-30) [keep: ] quote: "营业收入利润率为5.26%,同比提高0.04个百分点。"
  - p12 China industrial enterprises above designated size cumulative total profit, Janu = **53,732** 亿元 (100 million CNY) (2025-01-01..2025-09-30) [keep: ] quote: "\| 总计 \| 1020846.7 \| 2.4 \| 873426.0 \| 2.6 \| 53732.0 \| 3.2 \|"
  - p13 Statistical scope threshold: annual main business revenue for industrial enterpr = **20,000,000** CNY (not stated (page dated 2025-10-27)) [keep: ] quote: "规模以上工业企业,即年主营业务收入为2000万元及以上的工业法人单位。"
  - p14 China industrial enterprises above designated size cumulative revenue, January-S = **1,020,847** 亿元 (100 million CNY) (2025-01-01..2025-09-30) [keep: ] quote: "\| 总计 \| 1020846.7 \| 2.4 \| 873426.0 \| 2.6 \| 53732.0 \| 3.2 \|"
- `https://www.gov.cn/lianbo/bumen/202509/content_7042518.htm` -> **live_dated** (page date 2025-09-27); points raw/verified 15/7
  - p15 Year-on-year growth of cumulative total profits of industrial enterprises above  = **0.9** % (2025-01-01..2025-08-31) [keep: ] quote: "1-8月份,全国规模以上工业企业实现利润总额46929.7亿元,同比增长0.9%(按可比口径计算,详见附注二)。"
  - p16 Year-on-year growth of monthly total profits of industrial enterprises above des = **20.4** % (2025-08-01..2025-08-31) [keep: ] quote: "8月份,规模以上工业企业利润同比由上月下降1.5%转为增长20.4%。"
  - p17 Year-on-year change of monthly total profits of industrial enterprises above des = **1.5** % (2025-07-01..2025-07-31) [keep: ] quote: "8月份,规模以上工业企业利润同比由上月下降1.5%转为增长20.4%。"
  - p18 Cumulative operating revenue of industrial enterprises above designated size, Ch = **89,620,000,000,000** CNY (2025-01-01..2025-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入89.62万亿元,同比增长2.3%"
  - p19 Operating revenue profit margin of industrial enterprises above designated size, = **5.24** % (2025-01-01..2025-08-31) [keep: ] quote: "营业收入利润率为5.24%,同比下降0.06个百分点。"
  - p20 Statistical scope threshold: annual main business revenue for industrial enterpr = **20,000,000** CNY (not stated (page dated 2025-09-01)) [keep: ] quote: "规模以上工业企业,即年主营业务收入为2000万元及以上的工业法人单位。"
  - p21 NBS note: year-on-year growth rates of industrial profits computed on comparable = **2** as written "二", value check pending note number (not stated (page dated 2025-09-01)) [keep: ] quote: "二、规模以上工业企业利润总额、营业收入等指标的增速均按可比口径计算。报告期数据与上年所公布的同指标数据之间有不可比因素,不能直接相比计算增速。"
- `https://finance.sina.cn/2026-09-29/detail-initmzhm9296668.d.html` -> **live_dated** (page date 2026-09-29); points raw/verified 15/15
  - p22 NBS cumulative total profits of industrial enterprises above designated size, Ch = **5,271,980,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月份,全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p23 Year-on-year growth rate of cumulative total profits of industrial enterprises a = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月份,全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p24 Prior year-on-year growth rate of cumulative total profits of industrial enterpr = **17.6** % (2026-01-01..2026-07-31) [keep: ] quote: "同比增长15.7%(前值17.6%)"
  - p25 Year-on-year growth rate of monthly total profits of industrial enterprises abov = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "单月看,8月利润当月同比上涨4.2%(前值11.2%),较前值快速回落,单月利润增速回到个位数。"
  - p26 Prior year-on-year growth rate of monthly total profits of industrial enterprise = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "单月看,8月利润当月同比上涨4.2%(前值11.2%)"
  - p27 Cumulative operating revenue of industrial enterprises above designated size, Ch = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "规模以上工业企业实现营业收入93.09万亿,同比增长6.6%(前值6.5%)"
  - p28 Operating revenue profit margin of industrial enterprises above designated size, = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月规上工业企业营业收入利润率为5.66%,同比提高0.44个百分点"
  - p29 Year-on-year change in operating revenue profit margin of industrial enterprises = **0.44** percentage points (2026-01-01..2026-08-31) [keep: ] quote: "1-8月规上工业企业营业收入利润率为5.66%,同比提高0.44个百分点"
  - p30 Year-on-year growth rate of industrial value added above designated size, China, = **5.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月工业生产有所加快,规上工业增加值同比增长5.2%,出口交货值同比增长11.1%"
  - p31 Year-on-year growth rate of PPI, China, August 2026 = **3.8** % (2026-08-01..2026-08-31) [keep: ] quote: "8月PPI同比上涨3.8%,环比上涨0.4%"
  - p32 Year-on-year growth rate of finished goods inventory of industrial enterprises a = **11** % (2026-08-01..2026-08-31) [keep: ] quote: "产成品库存同比增长约11%,快于营收增速"
  - p33 Year-on-year growth rate of monthly operating revenue, industrial enterprises ab = **5.3** % (2026-08-01..2026-08-31) [keep: ] quote: "按照月度金额计算,8月单月营业收入同比增长约5.3%,营业成本同比增长约5.2%"
  - p34 Year-on-year growth rate of monthly operating cost, industrial enterprises above = **5.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月单月营业收入同比增长约5.3%,营业成本同比增长约5.2%"
  - p35 Year-on-year growth rate of high-tech manufacturing value added, China, August 2 = **16.7** % (2026-08-01..2026-08-31) [keep: ] quote: "高技术制造业增加值同比增长16.7%,结构性生产动能较强"
  - p36 Year-on-year growth rate of export delivery value, industrial enterprises above  = **11.1** % (2026-08-01..2026-08-31) [keep: ] quote: "出口交货值同比增长11.1%,生产和外需仍提供支撑"
- dropped by code checks: 24 (number: value_as_written is only part of a larger CJK number in the quote: 24)

### d2 [related_series] Revenue-margin decomposition

Hypothesis: Cumulative profit equals cumulative industrial enterprise revenue multiplied by the profit margin. NBS publishes revenue and margin alongside profits; January-August 2026 revenue and margin plus a September revenue estimate from industrial production and PPI can produce an independent level estimate.

Queries issued by the searcher: 2026年1-8月 规模以上工业企业 营业收入 利润率; 2026年9月 规模以上工业增加值 同比 PPI 国家统计局; 2025年1-9月份 规模以上工业企业 营业收入 利润总额 利润率; 2026年9月份 全国工业生产者出厂价格 PPI 同比上涨5.0% 国家统计局

- `https://www.stats.gov.cn/sj/zxfbhjd/202609/t20260928_1965425.html` -> **live_dated** (page date 2026-09-28); points raw/verified 14/13
  - p37 Cumulative operating revenue of industrial enterprises above designated size, Ch = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%"
  - p38 Cumulative operating revenue of industrial enterprises above designated size, Ch = **930,851** CNY (2026-01-01..2026-08-31) [keep: ] quote: "\| 总计 \| 930851.2 \| 6.6 \| 791893.6 \| 6.1 \| 52719.8 \| 15.7 \|"
  - p39 Operating revenue profit margin (profit/revenue) of industrial enterprises above = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "营业收入利润率为5.66%,同比提高0.44个百分点"
  - p40 Cumulative operating cost of industrial enterprises above designated size, China = **79,190,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "发生营业成本79.19万亿元,增长6.1%"
  - p41 Cumulative operating revenue of mining enterprises above designated size, China, = **36,385** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "\| 其中:采矿业 \| 36384.9 \| 8.6 \| 23537.3 \| 2.1 \| 7661.5 \| 35.1 \|"
  - p42 Cumulative operating revenue of manufacturing enterprises above designated size, = **809,221** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "\| 制造业 \| 809220.6 \| 7.2 \| 691755.6 \| 6.7 \| 39695.3 \| 17.4 \|"
  - p43 Cumulative operating revenue of electricity, heat, gas and water production and  = **85,246** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "\| 电力、热力、燃气及水生产和供应业 \| 85245.6 \| 0.9 \| 76600.7 \| 2.1 \| 5363.0 \| -12.0 \|"
  - p44 Operating revenue profit margin of mining enterprises above designated size, Chi = **21.06** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 其中:采矿业 \| 21.06 \| 64.69 \| 9.43 \| 36.6 \| 143.2 \| 56.9 \| 15.5 \| 54.3 \|"
  - p45 Operating revenue profit margin of manufacturing enterprises above designated si = **4.91** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 制造业 \| 4.91 \| 85.48 \| 8.65 \| 84.9 \| 185.3 \| 58.2 \| 23.7 \| 74.1 \|"
  - p46 Operating revenue profit margin of electricity, heat, gas and water production a = **6.29** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 电力、热力、燃气及水生产和供应业 \| 6.29 \| 89.86 \| 5.00 \| 36.5 \| 385.4 \| 60.4 \| 1.2 \| 62.5 \|"
  - p47 Year-on-year growth of total profit of industrial enterprises above designated s = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月份,规模以上工业企业利润同比增长4.2%。"
  - p48 Year-on-year growth of cumulative operating revenue of industrial enterprises ab = **6.6** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 总计 \| 930851.2 \| 6.6 \| 791893.6 \| 6.1 \| 52719.8 \| 15.7 \|"
  - p49 Cost per 100 yuan of operating revenue of industrial enterprises above designate = **85.07** CNY per 100 CNY revenue (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业每百元营业收入中的成本为85.07元,同比减少0.41元"
- `https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261019_1965617.html` -> **live_dated** (page date 2026-10-19); points raw/verified 15/14
  - p50 September 2026 industrial value added above designated size, year-on-year growth = **5.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业增加值同比实际增长5.5%(增加值增速均为扣除价格因素的实际增长率)"
  - p51 September 2026 industrial value added above designated size, month-on-month grow = **0.61** % (2026-09-01..2026-09-30) [keep: ] quote: "从环比看,9月份,规模以上工业增加值比上月增长0.61%。"
  - p52 January-September 2026 industrial value added above designated size, year-on-yea = **5.3** % (2026-01-01..2026-09-30) [keep: ] quote: "1-9月份,规模以上工业增加值同比增长5.3%。"
  - p53 September 2026 manufacturing value added, year-on-year growth = **6** % (2026-09-01..2026-09-30) [keep: ] quote: "分三大门类看,9月份,采矿业增加值同比增长1.3%,制造业增长6.0%,电力、热力、燃气及水生产和供应业增长5.6%。"
  - p54 September 2026 industrial enterprises above designated size product sales rate = **97** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业企业产品销售率为97.0%,同比下降0.2个百分点"
  - p55 January-September 2026 industrial enterprises above designated size product sale = **96.4** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 产品销售率(%) \| 97.0 \| -0.2(百分点) \| 96.4 \| 0.1(百分点) \|"
  - p56 January-September 2026 industrial enterprises above designated size export deliv = **127,416** 100 million CNY (2026-01-01..2026-09-30) [keep: ] quote: "\| 出口交货值(亿元) \| 17132 \| 17.0 \| 127416 \| 10.7 \|"
  - p57 September 2026 industrial enterprises above designated size export delivery valu = **17** % (2026-09-01..2026-09-30) [keep: ] quote: "规模以上工业企业实现出口交货值17132亿元,同比名义增长17.0%。"
  - p58 January-September 2026 industrial enterprises above designated size export deliv = **10.7** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 出口交货值(亿元) \| 17132 \| 17.0 \| 127416 \| 10.7 \|"
  - p59 September 2026 industrial enterprises above designated size product sales rate,  = **0.2** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业企业产品销售率为97.0%,同比下降0.2个百分点"
  - p60 January-September 2026 industrial enterprises above designated size product sale = **0.1** percentage points (2026-01-01..2026-09-30) [keep: ] quote: "\| 产品销售率(%) \| 97.0 \| -0.2(百分点) \| 96.4 \| 0.1(百分点) \|"
  - p61 September 2026 industrial value added above designated size, month-on-month grow = **0.61** percent (2026-09-01..2026-09-30) [keep: ] quote: "\| \| 9月 \| 0.61 \|"
  - p62 August 2026 industrial value added above designated size, month-on-month growth  = **0.54** percent (2026-08-01..2026-08-31) [keep: ] quote: "\| \| 8月 \| 0.54 \|"
  - p63 September 2025 industrial value added above designated size, month-on-month grow = **0.65** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| 2025年 \| 9月 \| 0.65 \|"
- `https://finance.cnr.cn/ycbd/20251027/t20251027_527408699.shtml` -> **live_dated** (page date 2025-10-27); points raw/verified 15/0
- `https://view.inews.qq.com/wxn/20261019A05PC000` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 17 (number: value_as_written is only part of a larger CJK number in the quote: 6; published 2026-10-27 after as_of: 11)

### d3 [related_series] Sector decomposition

Hypothesis: Total profit is the sum of mining, manufacturing, and electricity/heat/gas/water profits. Sector-level January-August 2026 profits and September sector-specific price and production signals can reduce aggregation error and capture divergent shocks.

Queries issued by the searcher: 2026年1-8月 规模以上工业企业利润 采矿业 制造业 电力热力燃气及水生产和供应业 利润总额; 2026年8月 分行业 工业企业利润 国家统计局; 2026年9月 全国PPI 采矿业 制造业 电力热力 出厂价格 同比 国家统计局; 2025年1-9月 采矿业 制造业 电力热力燃气及水生产和供应业 利润总额 亿元

- `https://www.stats.gov.cn/sj/zxfbhjd/202609/t20260928_1965425.html` -> **live_dated** (page date 2026-09-28); points raw/verified 15/10
  - p64 Year-on-year growth of total industrial profit above designated size, China, Jan = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,全国规模以上工业企业实现利润总额52719.8亿元,同比增长15.7%"
  - p65 Year-on-year growth of mining profit above designated size, China, January-Augus = **35.1** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,采矿业实现利润总额7661.5亿元,同比增长35.1%"
  - p66 Year-on-year growth of manufacturing profit above designated size, China, Januar = **17.4** % (2026-01-01..2026-08-31) [keep: ] quote: "制造业实现利润总额39695.3亿元,增长17.4%"
  - p67 Year-on-year growth of total industrial profit above designated size, China, Aug = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月份,规模以上工业企业利润同比增长4.2%"
  - p68 Cumulative profit of coal mining and washing (煤炭开采和洗选业) above designated size, C = **2,944** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "煤炭开采和洗选业 \| 18267.0 \| 10.4 \| 12573.2 \| 4.1 \| 2943.8 \| 51.6"
  - p69 Cumulative profit of oil and natural gas extraction (石油和天然气开采业) above designated = **2,766** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "石油和天然气开采业 \| 8693.5 \| 13.0 \| 4593.0 \| 8.7 \| 2765.5 \| 17.0"
  - p70 Cumulative profit of electricity and heat production and supply (电力、热力生产和供应业) ab = **4,462** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "电力、热力生产和供应业 \| 67008.3 \| 0.4 \| 60212.0 \| 1.9 \| 4462.5 \| -15.1"
  - p71 Cumulative profit of gas production and supply (燃气生产和供应业) above designated size, = **607** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "燃气生产和供应业 \| 15196.4 \| 3.2 \| 14196.3 \| 3.2 \| 607.0 \| 10.2"
  - p72 Cumulative profit of water production and supply (水的生产和供应业) above designated siz = **294** 亿元 (100 million CNY) (2026-01-01..2026-08-31) [keep: ] quote: "水的生产和供应业 \| 3041.0 \| -0.2 \| 2192.5 \| 0.0 \| 293.5 \| 0.8"
  - p73 Cumulative revenue of industrial enterprises above designated size, China, Janua = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%"
- `https://www.zhitongcaijing.com/content/detail/1506835.html` -> **live_dated** (page date 2026-10-14); points raw/verified 15/15
  - p74 China PPI for mining industry (采掘工业) year-on-year change, September 2026 = **25.4** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨25.4%,原材料工业价格上涨9.4%,加工工业价格上涨3.4%。"
  - p75 China PPI for raw materials industry (原材料工业) year-on-year change, September 2026 = **9.4** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨25.4%,原材料工业价格上涨9.4%,加工工业价格上涨3.4%。"
  - p76 China PPI for processing industry (加工工业) year-on-year change, September 2026 = **3.4** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨25.4%,原材料工业价格上涨9.4%,加工工业价格上涨3.4%。"
  - p77 China PPI for mining industry (采掘工业) month-on-month change, September 2026 = **7.7** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨7.7%,原材料工业价格上涨2.6%,加工工业价格上涨0.2%。"
  - p78 China PPI for raw materials industry (原材料工业) month-on-month change, September 20 = **2.6** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨7.7%,原材料工业价格上涨2.6%,加工工业价格上涨0.2%。"
  - p79 China PPI for processing industry (加工工业) month-on-month change, September 2026 = **0.2** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,采掘工业价格上涨7.7%,原材料工业价格上涨2.6%,加工工业价格上涨0.2%。"
  - p80 China PPI for means of production (生产资料) year-on-year change, September 2026 = **6.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,工业生产者出厂价格中,生产资料价格同比上涨6.5%,影响工业生产者出厂价格总水平上涨约5.07个百分点。"
  - p81 China PPI for means of production (生产资料) month-on-month change, September 2026 = **1.4** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,工业生产者出厂价格中,生产资料价格环比上涨1.4%,影响工业生产者出厂价格总水平上涨约1.14个百分点。"
  - p82 China PPI for consumer goods (生活资料) year-on-year change, September 2026 = **0.1** % (2026-09-01..2026-09-30) [keep: ] quote: "生活资料价格下降0.1%,影响工业生产者出厂价格总水平下降约0.03个百分点。"
  - p83 China PPI for consumer goods (生活资料) month-on-month change, September 2026 = **0.1** % (2026-09-01..2026-09-30) [keep: ] quote: "生活资料价格上涨0.1%,影响工业生产者出厂价格总水平上涨约0.03个百分点。"
  - p84 China PPI for fuel and power purchase (燃料动力类) year-on-year change, September 202 = **13.6** % (2026-09-01..2026-09-30) [keep: ] quote: "工业生产者购进价格中,有色金属材料及电线类价格上涨20.0%,燃料动力类价格上涨13.6%,化工原料类价格上涨12.6%,纺织原料类价格上涨4.5%;"
  - p85 China PPI for fuel and power purchase (燃料动力类) month-on-month change, September 2 = **3.7** % (2026-09-01..2026-09-30) [keep: ] quote: "工业生产者购进价格中,燃料动力类价格上涨3.7%,化工原料类价格上涨2.4%,有色金属材料及电线类价格上涨1.4%,建筑材料及非金属类价格上涨0.7%,纺织原料类价格上涨0.6%,农副产品类价格上涨0.1%;"
  - p86 China PPI overall year-on-year change, September 2026 = **5** % (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月份,全国工业生产者出厂价格同比上涨5.0%,环比上涨1.2%。"
  - p87 China PPI overall month-on-month change, September 2026 = **1.2** % (2026-09-01..2026-09-30) [keep: ] quote: "2026年9月份,全国工业生产者出厂价格同比上涨5.0%,环比上涨1.2%。"
  - p88 China PPI average year-on-year change, January-September 2026 = **2.3** % (2026-01-01..2026-09-30) [keep: ] quote: "1-9月平均,工业生产者出厂价格比上年同期上涨2.3%,工业生产者购进价格上涨3.6%。"
- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/843942150471/index.phtml` -> **live_dated** (page date 2026-09-28); points raw/verified 15/9
  - p89 Cumulative profit growth of industrial enterprises above designated size, China, = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月,根据统计局数据,规模以上工业企业利润同比增长15.7%。"
  - p90 August 2026 monthly profit growth of industrial enterprises above designated siz = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月当月同比为4.2%,低于前值11.2%。"
  - p91 July 2026 monthly profit growth of industrial enterprises above designated size, = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "8 月当月同比为4.2%,低于前值11.2%。"
  - p92 August 2026 profit growth of mining industry (采矿业), China, year-on-year = **36.4** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月,采矿业同比为36.4%,制造业同比为9.09%,电热气水同比为-43.0%。"
  - p93 August 2026 profit growth of manufacturing industry (制造业), China, year-on-year = **9.09** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月,采矿业同比为36.4%,制造业同比为9.09%,电热气水同比为-43.0%。"
  - p94 August 2026 profit growth of electricity/heat/gas/water sector (电热气水), China, ye = **-43** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月,采矿业同比为36.4%,制造业同比为9.09%,电热气水同比为-43.0%。"
  - p95 August 2026 profit margin of industrial enterprises above designated size, China = **5.67** % (2026-08-01..2026-08-31) [keep: ] quote: "利润率方面,8 月为5.67%,去年同期(可比口径)为 5.82%。"
  - p96 August 2026 revenue growth of mining industry (采矿业), China, year-on-year = **9.48** % (2026-08-01..2026-08-31) [keep: ] quote: "制造业上游收入增速为3.6%,制造业下游增速为-0.03%,采矿业增速为9.48%,电热气水增速为0.69%。"
  - p97 August 2026 revenue growth of electricity/heat/gas/water sector (电热气水), China, y = **0.69** % (2026-08-01..2026-08-31) [keep: ] quote: "制造业上游收入增速为3.6%,制造业下游增速为-0.03%,采矿业增速为9.48%,电热气水增速为0.69%。"
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/macro/rptid/843966430747/index.phtml` -> **live_dated** (page date 2026-09-28); points raw/verified 15/15
  - p98 Cumulative total profit of industrial enterprises above designated size, China,  = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月规上工业企业利润总额同比增长15.7%"
  - p99 Cumulative total profit of industrial enterprises above designated size, China,  = **1.9** percentage points (2026-01-01..2026-07-31) [keep: ] quote: "1-8 月规上工业企业利润总额同比增长15.7%,较1-7 月回落1.9pp"
  - p100 Estimated total profit of industrial enterprises above designated size, China, A = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "估算8 月当月利润总额同比增长4.2%,较7 月的11.2%回落"
  - p101 Total profit of industrial enterprises above designated size, China, July 2026 s = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "估算8 月当月利润总额同比增长4.2%,较7 月的11.2%回落"
  - p102 Mining industry (采矿业) profit, China, August 2026 single month, year-on-year grow = **36.4** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月采矿业利润当月同比增长36.4%,较上月回落8.0pp"
  - p103 Mining industry (采矿业) profit, China, July 2026 single month, year-on-year growth = **8** percentage points (2026-07-01..2026-07-31) [keep: ] quote: "8 月采矿业利润当月同比增长36.4%,较上月回落8.0pp"
  - p104 Manufacturing industry (制造业) profit, China, August 2026 single month, year-on-ye = **9.1** % (2026-08-01..2026-08-31) [keep: ] quote: "制造业增长9.1%"
  - p105 Utilities (公用事业) profit, China, August 2026 single month, year-on-year decline = **43** % (2026-08-01..2026-08-31) [keep: ] quote: "公用事业当月利润同比降幅由13.4%大幅扩大至43.0%"
  - p106 Utilities (公用事业) profit, China, July 2026 single month, year-on-year decline = **13.4** % (2026-07-01..2026-07-31) [keep: ] quote: "公用事业当月利润同比降幅由13.4%大幅扩大至43.0%"
  - p107 PPI, China, August 2026 single month, year-on-year growth = **3.8** % (2026-08-01..2026-08-31) [keep: ] quote: "PPI 当月同比增速回升0.3pp 至3.8%"
  - p108 Revenue (excluding price effect) of industrial enterprises above designated size = **3.4** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月剔除价格的营业收入当月同比增速回升0.5pp 至3.4%"
  - p109 Profit margin contribution to August 2026 single-month profit year-on-year growt = **-2.3** percentage points (2026-08-01..2026-08-31) [keep: ] quote: "利润率对当月利润同比的拉动由7 月的约4.2pp 转为-2.3pp"
  - p110 Profit margin contribution to July 2026 single-month profit year-on-year growth, = **4.2** percentage points (2026-07-01..2026-07-31) [keep: ] quote: "利润率对当月利润同比的拉动由7 月的约4.2pp 转为-2.3pp"
  - p111 Finished goods inventory of industrial enterprises above designated size, China, = **11** % (2026-08-01..2026-08-31) [keep: ] quote: "8 月末产成品存货同比增长11.0%,较上月回升0.2pp"
  - p112 Finished goods inventory turnover days, industrial enterprises above designated  = **21.3** days (2026-08-01..2026-08-31) [keep: ] quote: "产成品周转天数21.3 天、持平上月"
- dropped by code checks: 11 (number: value_as_written is only part of a larger CJK number in the quote: 8; value_as_written not in quote as a whole number: 3)

### d4 [physical_flow] Volume-price-cost bridge

Hypothesis: Profit growth can be bridged from volume (industrial value added), price (PPI), and unit cost or margin. September monthly profit growth estimated from August plus September PPI and production changes constrains the direction and size of the September increment.

Queries issued by the searcher: 2026年9月 规模以上工业增加值 同比; 2026年9月 PPI 同比 国家统计局; 2026年1-8月 规模以上工业企业利润总额 同比增长 国家统计局; 2026年1-9月 规模以上工业企业利润总额 国家统计局 10月

- `https://www.stats.gov.cn/sj/zxfbhjd/202609/t20260928_1965425.html` -> **live_dated** (page date 2026-09-28); points raw/verified 15/14
  - p113 Year-on-year growth of cumulative total profits of industrial enterprises above  = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,全国规模以上工业企业实现利润总额52719.8亿元,同比增长15.7%(按可比口径计算,详见附注二)。"
  - p114 Year-on-year growth of industrial enterprise profits above designated size, Chin = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月份,规模以上工业企业利润同比增长4.2%。"
  - p115 Cumulative operating revenue of industrial enterprises above designated size, Ch = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p116 Year-on-year growth of cumulative operating revenue of industrial enterprises ab = **6.6** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p117 Cumulative operating cost of industrial enterprises above designated size, China = **79,190,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p118 Year-on-year growth of cumulative operating cost of industrial enterprises above = **6.1** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p119 Operating revenue profit margin (total profit / operating revenue) of industrial = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p120 Year-on-year change in operating revenue profit margin of industrial enterprises = **0.44** percentage points (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业实现营业收入93.09万亿元,同比增长6.6%;发生营业成本79.19万亿元,增长6.1%;营业收入利润率为5.66%,同比提高0.44个百分点。"
  - p121 Cost per 100 yuan of operating revenue of industrial enterprises above designate = **85.07** CNY per 100 CNY of operating revenue (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业每百元营业收入中的成本为85.07元,同比减少0.41元;每百元营业收入中的费用为8.35元,同比减少0.14元。"
  - p122 Year-on-year change in cost per 100 yuan of operating revenue of industrial ente = **0.41** CNY per 100 CNY of operating revenue (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业每百元营业收入中的成本为85.07元,同比减少0.41元;每百元营业收入中的费用为8.35元,同比减少0.14元。"
  - p123 Expenses per 100 yuan of operating revenue of industrial enterprises above desig = **8.35** CNY per 100 CNY of operating revenue (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,规模以上工业企业每百元营业收入中的成本为85.07元,同比减少0.41元;每百元营业收入中的费用为8.35元,同比减少0.14元。"
  - p124 Finished goods inventory of industrial enterprises above designated size, China, = **7,360,000,000,000** CNY (2026-08-31..2026-08-31) [keep: ] quote: "8月末,规模以上工业企业应收账款29.48万亿元,同比增长9.0%;产成品存货7.36万亿元,增长11.0%。"
  - p125 Year-on-year growth of finished goods inventory of industrial enterprises above  = **11** % (2026-08-31..2026-08-31) [keep: ] quote: "8月末,规模以上工业企业应收账款29.48万亿元,同比增长9.0%;产成品存货7.36万亿元,增长11.0%。"
  - p126 Finished goods inventory turnover days of industrial enterprises above designate = **21.3** days (2026-08-31..2026-08-31) [keep: ] quote: "8月末,规模以上工业企业每百元资产实现的营业收入为72.4元,同比增加0.4元;人均营业收入为192.2万元,同比增加12.5万元;产成品存货周转天数为21.3天,同比增加0.6天;应收账款平均回收期为72.2天,同比增加0.9天。"
- `https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261014_1965475.html` -> **live_dated** (page date 2026-10-14); points raw/verified 15/14
  - p127 China PPI year-on-year change, September 2026 = **5** % (2026-09-01..2026-09-30) [keep: ] quote: "工业生产者出厂价格指数(PPI)环比上涨1.2%,涨幅比上月扩大0.8个百分点;同比上涨5.0%,涨幅比上月扩大1.2个百分点。"
  - p128 China PPI year-on-year change, August 2026 (implied prior month) = **1.2** percentage points (2026-08-01..2026-08-31) [keep: ] quote: "同比上涨5.0%,涨幅比上月扩大1.2个百分点。"
  - p129 China PPI month-on-month change, September 2026 = **1.2** % (2026-09-01..2026-09-30) [keep: ] quote: "工业生产者出厂价格指数(PPI)环比上涨1.2%,涨幅比上月扩大0.8个百分点"
  - p130 China PPI month-on-month change, August 2026 (implied prior month) = **0.8** percentage points (2026-08-01..2026-08-31) [keep: ] quote: "工业生产者出厂价格指数(PPI)环比上涨1.2%,涨幅比上月扩大0.8个百分点"
  - p131 China CPI year-on-year change, September 2026 = **0.9** % (2026-09-01..2026-09-30) [keep: ] quote: "同比上涨0.9%,涨幅比上月扩大0.1个百分点"
  - p132 China CPI month-on-month change, September 2026 = **0.2** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,居民消费价格指数(CPI)环比上涨0.2%,涨幅比上月回落0.2个百分点"
  - p133 China core CPI year-on-year change (excluding food and energy), September 2026 = **1** % (2026-09-01..2026-09-30) [keep: ] quote: "扣除食品和能源价格的核心CPI同比上涨1.0%,涨幅与上月相同。"
  - p134 PPI year-on-year contribution from 8 rising industries, September 2026 = **5.42** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "8个行业涨幅比上月均扩大,合计影响PPI同比上涨约5.42个百分点,上拉影响比上月增加1.12个百分点。"
  - p135 Increase in upward pull on PPI year-on-year from 8 rising industries, September  = **1.12** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "合计影响PPI同比上涨约5.42个百分点,上拉影响比上月增加1.12个百分点。"
  - p136 PPI year-on-year drag from 5 falling industries, September 2026 = **0.66** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "5个行业合计下拉PPI同比约0.66个百分点。"
  - p137 Coal mining and washing PPI year-on-year change, September 2026 = **35.3** % (2026-09-01..2026-09-30) [keep: ] quote: "煤炭开采和洗选业上涨35.3%"
  - p138 Oil and natural gas extraction PPI year-on-year change, September 2026 = **24.5** % (2026-09-01..2026-09-30) [keep: ] quote: "石油和天然气开采业、石油煤炭及其他燃料加工业、化学原料和化学制品制造业分别上涨24.5%、21.6%和12.1%"
  - p139 Electrical machinery and equipment manufacturing PPI year-on-year change, Septem = **6.2** % (2026-09-01..2026-09-30) [keep: ] quote: "电气机械和器材制造业上涨6.2%,计算机通信和其他电子设备制造业上涨5.8%"
  - p140 Computer, communications and other electronic equipment manufacturing PPI year-o = **5.8** % (2026-09-01..2026-09-30) [keep: ] quote: "电气机械和器材制造业上涨6.2%,计算机通信和其他电子设备制造业上涨5.8%"
- `https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261019_1965617.html` -> **live_dated** (page date 2026-10-19); points raw/verified 15/12
  - p141 September 2026 industrial value added above designated size, year-on-year real g = **5.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业增加值同比实际增长5.5%(增加值增速均为扣除价格因素的实际增长率),增速比上月加快0.3个百分点。"
  - p142 September 2026 industrial value added above designated size, month-on-month grow = **0.61** % (2026-09-01..2026-09-30) [keep: ] quote: "从环比看,9月份,规模以上工业增加值比上月增长0.61%。"
  - p143 January-September 2026 industrial value added above designated size, year-on-yea = **5.3** % (2026-01-01..2026-09-30) [keep: ] quote: "1-9月份,规模以上工业增加值同比增长5.3%。"
  - p144 September 2026 manufacturing value added, year-on-year growth = **6** % (2026-09-01..2026-09-30) [keep: ] quote: "分三大门类看,9月份,采矿业增加值同比增长1.3%,制造业增长6.0%,电力、热力、燃气及水生产和供应业增长5.6%。"
  - p145 September 2026 industrial enterprises above designated size product sales rate = **97** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业企业产品销售率为97.0%,同比下降0.2个百分点;规模以上工业企业实现出口交货值17132亿元,同比名义增长17.0%。"
  - p146 September 2026 industrial enterprises above designated size export delivery valu = **17** % (2026-09-01..2026-09-30) [keep: ] quote: "规模以上工业企业实现出口交货值17132亿元,同比名义增长17.0%。"
  - p147 January-September 2026 industrial enterprises above designated size export deliv = **127,416** 亿元 (100 million CNY) (2026-01-01..2026-09-30) [keep: ] quote: "\| 出口交货值(亿元) \| 17132 \| 17.0 \| 127416 \| 10.7 \|"
  - p148 January-September 2026 industrial enterprises above designated size export deliv = **10.7** % (2026-01-01..2026-09-30) [keep: ] quote: "\| 出口交货值(亿元) \| 17132 \| 17.0 \| 127416 \| 10.7 \|"
  - p149 January-September 2026 total electricity generation above designated size, year- = **2.2** % (2026-01-01..2026-09-30) [keep: ] quote: "\| 规模以上工业发电量(亿千瓦时) \| 8294 \| -1.2 \| 74916 \| 2.2 \|"
  - p150 September 2026 industrial value added above designated size, month-on-month grow = **0.61** % (2026-09-01..2026-09-30) [keep: ] quote: "\| \| 9月 \| 0.61 \|"
  - p151 August 2026 industrial value added above designated size, month-on-month growth  = **0.54** % (2026-08-01..2026-08-31) [keep: ] quote: "\| \| 8月 \| 0.54 \|"
  - p152 September 2026 high-tech manufacturing value added, year-on-year growth = **15.3** % (2026-09-01..2026-09-30) [keep: ] quote: "\| 其中:高技术制造业 \| ... \| 15.3 \| ... \| 14.3 \|"
- `https://4g.stockstar.com/detail/JC2026092800024124` -> **live_dated** (page date 2026-10-24); points raw/verified 15/15
  - p153 China industrial enterprises above designated size cumulative profit total, Janu = **5,271,980,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月份,全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p154 China industrial enterprises above designated size cumulative profit year-on-yea = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月份,全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p155 China industrial enterprises above designated size cumulative profit year-on-yea = **17.6** % (2026-01-01..2026-07-31) [keep: ] quote: "同比增长15.7%(前值17.6%)"
  - p156 China industrial enterprises above designated size single-month profit year-on-y = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月利润当月同比上涨4.2%(前值11.2%),较前值快速回落"
  - p157 China industrial enterprises above designated size single-month profit year-on-y = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "8月利润当月同比上涨4.2%(前值11.2%)"
  - p158 China industrial value added above designated size year-on-year growth, August 2 = **5.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月工业生产有所加快,规上工业增加值同比增长5.2%"
  - p159 China PPI year-on-year change, August 2026 = **3.8** % (2026-08-01..2026-08-31) [keep: ] quote: "8月PPI同比上涨3.8%,环比上涨0.4%"
  - p160 China PPI month-on-month change, August 2026 = **0.4** % (2026-08-01..2026-08-31) [keep: ] quote: "8月PPI同比上涨3.8%,环比上涨0.4%"
  - p161 China industrial enterprises above designated size export delivery value year-on = **11.1** % (2026-08-01..2026-08-31) [keep: ] quote: "出口交货值同比增长11.1%,生产和外需仍提供支撑"
  - p162 China high-tech manufacturing value added year-on-year growth, August 2026 = **16.7** % (2026-08-01..2026-08-31) [keep: ] quote: "高技术制造业增加值同比增长16.7%,结构性生产动能较强"
  - p163 China industrial enterprises above designated size operating revenue profit marg = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月规上工业企业营业收入利润率为5.66%,同比提高0.44个百分点"
  - p164 China industrial enterprises above designated size profit margin year-on-year ch = **0.44** percentage points (2026-01-01..2026-08-31) [keep: ] quote: "1-8月规上工业企业营业收入利润率为5.66%,同比提高0.44个百分点"
  - p165 China industrial enterprises above designated size finished goods inventory year = **11** % (2026-08-01..2026-08-31) [keep: ] quote: "产成品库存同比增长约11%,快于营收增速"
  - p166 China industrial enterprises above designated size cost per 100 yuan of operatin = **0.41** CNY (2026-01-01..2026-08-31) [keep: ] quote: "每百元营业收入中的成本和费用分别同比减少0.41元和0.14元"
  - p167 China industrial enterprises above designated size operating revenue cumulative  = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "规模以上工业企业实现营业收入93.09万亿,同比增长6.6%(前值6.5%)"
- dropped by code checks: 5 (number: value_as_written is only part of a larger CJK number in the quote: 3; value_as_written not in quote as a whole number: 2)

### d5 [forecasts_markets] Forecast and nowcast aggregator

Hypothesis: Published NBS release previews, bank research, and data-calendar expectations may contain a consensus or nowcast for January-September 2026 industrial profits. Even a growth-rate forecast can be applied to the 2025 base, providing an independent check.

Queries issued by the searcher: China industrial profits September 2026 forecast; 2026年9月 规模以上工业企业利润 预测; 2026年1-9月 工业企业利润 预测 9月 高基数 同比; 2025年1-9月 规模以上工业企业利润总额 亿元 同比 国家统计局

- `https://4g.stockstar.com/detail/IG2026092900008105` -> **live_dated** (page date 2026-10-24); points raw/verified 8/8
  - p168 China industrial enterprises above designated size cumulative total profits, Jan = **5,271,980,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月份,全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p169 China industrial enterprises above designated size cumulative profit growth year = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "全国规模以上工业企业实现利润总额52,719.8亿元,同比增长15.7%(前值17.6%)"
  - p170 China industrial enterprises above designated size cumulative profit growth year = **17.6** % (2026-01-01..2026-07-31) [keep: ] quote: "同比增长15.7%(前值17.6%)"
  - p171 China industrial enterprises above designated size cumulative operating revenue, = **93,090,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "规模以上工业企业实现营业收入93.09万亿,同比增长6.6%(前值6.5%)"
  - p172 China industrial enterprises above designated size cumulative operating revenue  = **6.6** % (2026-01-01..2026-08-31) [keep: ] quote: "规模以上工业企业实现营业收入93.09万亿,同比增长6.6%(前值6.5%)"
  - p173 China industrial enterprises above designated size cumulative operating revenue  = **6.5** % (2026-01-01..2026-07-31) [keep: ] quote: "同比增长6.6%(前值6.5%)"
  - p174 China industrial enterprises above designated size single-month profit growth ye = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月利润当月同比上涨4.2%(前值11.2%)"
  - p175 China industrial enterprises above designated size single-month profit growth ye = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "8月利润当月同比上涨4.2%(前值11.2%)"
- `https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/844016508236/index.phtml` -> **live_dated** (page date 2026-09-29); points raw/verified 15/12
  - p176 China industrial enterprises above designated size cumulative total profits, Jan = **5,270,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "2026 年1-8 月,全国规模以上工业企业实现利润总额5.27 万亿元,同比+15.7%"
  - p177 China industrial enterprises above designated size cumulative profit year-on-yea = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "2026 年1-8 月,全国规模以上工业企业实现利润总额5.27 万亿元,同比+15.7%"
  - p178 China industrial enterprises above designated size single-month profit year-on-y = **11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "8 月单月利润同比增速为+4.2%,较7 月的+11.2%明显收窄"
  - p179 China industrial enterprises above designated size cumulative profit year-on-yea = **17.6** % (2026-01-01..2026-07-31) [keep: ] quote: "规模以上工业企业利润同比增长+15.7%(前值+17.6%)"
  - p180 China industrial enterprises above designated size operating revenue profit marg = **5.66** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月营业收入利润率为5.66%,同比提高0.42 个pct"
  - p181 China industrial enterprises above designated size operating revenue profit marg = **0.42** percentage points (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月营业收入利润率为5.66%,同比提高0.42 个pct"
  - p182 China manufacturing sector cumulative total profits, January-August 2026 = **3,970,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月,制造业实现利润总额3.97 万亿元,同比+17.4%"
  - p183 China mining sector cumulative total profits, January-August 2026 = **770,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "采矿业实现利润总额0.77 万亿元,同比+35.1%"
  - p184 China electricity, heat, gas and water production and supply sector cumulative t = **540,000,000,000** CNY (2026-01-01..2026-08-31) [keep: ] quote: "电力、热力、燃气及水生产和供应业实现利润总额0.54 万亿元,同比-12%"
  - p185 China PPI cumulative year-on-year growth, January-August 2026 = **2** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月PPI 累计同比增速录得+2.0%"
  - p186 China industrial enterprises above designated size operating cost ratio, January = **85.07** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8 月营业成本率为85.07%,较上年大幅回落"
  - p187 China industrial enterprises above designated size finished goods inventory year = **11** % (2026-01-01..2026-08-31) [keep: ] quote: "2026 年1-8 月规模以上工业企业产成品存货同比+11.0%,较前值+10.8%有所提升"
- `http://m.hibor.com.cn/wap_detail.aspx?id=9122087795f162d6b062861ec64db68a` -> **live_dated** (page date 2026-09-28); points raw/verified 15/13
  - p188 China industrial enterprises above designated size cumulative profit year-on-yea = **17.6** % (2026-01-01..2026-07-31) [keep: ] quote: "1)2026年1-8月工业企业利润累计同比增速+15.7%,1-7月累计同比增速+17.6%"
  - p189 China industrial enterprises above designated size revenue year-on-year growth,  = **6.5** % (2026-01-01..2026-07-31) [keep: ] quote: "2)1-8月工业企业营收累计同比增速+6.6%,1-7月累计同比增速+6.5%"
  - p190 China industrial enterprises above designated size single-month profit year-on-y = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月工业企业利润单月同比增速降至+4.2%,增速较7月回落7个百分点。"
  - p191 China industrial enterprises above designated size single-month profit margin, A = **5.7** % (2026-08-01..2026-08-31) [keep: ] quote: "利润率方面,8月工业企业单月利润率为5.7%,高于上月的5.4%,但较去年同期减少0.15个百分点"
  - p192 China industrial enterprises above designated size single-month profit margin, J = **5.4** % (2026-07-01..2026-07-31) [keep: ] quote: "利润率方面,8月工业企业单月利润率为5.7%,高于上月的5.4%,但较去年同期减少0.15个百分点"
  - p193 China industrial value added above designated size year-on-year growth, August 2 = **5.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月全国规模以上工业增加值同比增速升至+5.2%,高于7月的+4.5%"
  - p194 China PPI year-on-year growth, August 2026 = **3.8** % (2026-08-01..2026-08-31) [keep: ] quote: "8月PPI同比增速升至+3.8%,高于7月的+3.5%"
  - p195 China PPI year-on-year growth, July 2026 = **3.5** % (2026-07-01..2026-07-31) [keep: ] quote: "8月PPI同比增速升至+3.8%,高于7月的+3.5%"
  - p196 China mining industry cumulative profit year-on-year growth, January-August 2026 = **35.1** % (2026-01-01..2026-08-31) [keep: ] quote: "2026年1-8月,采矿业盈利累计同比增速自1-7月的+34.9%升至+35.1%"
  - p197 China manufacturing industry cumulative profit year-on-year growth, January-Augu = **17.4** % (2026-01-01..2026-08-31) [keep: ] quote: "制造业利润累计同比增速降至+17.4%(1-7月为+18.8%)"
  - p198 China electricity, gas and water supply industry cumulative profit year-on-year  = **-12** % (2026-01-01..2026-08-31) [keep: ] quote: "电燃水供应业利润累计同比增速降至-12.0%(1-7月为-5.8%)"
  - p199 China industrial enterprises above designated size finished goods inventory year = **11** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月工业企业产成品库存累计同比增长11.0%,较7月回升0.2个百分点"
  - p200 China industrial enterprises above designated size finished goods inventory turn = **21.3** days (2026-08-01..2026-08-31) [keep: ] quote: "从8月份数据来看,产成品存货周转天数为21.3天,同比增加0.6天"
- `https://wap.stockstar.com/detail/IG2026092900008106` -> **live_dated** (page date 2026-10-24); points raw/verified 1/1
  - p201 China industrial enterprise profits growth rate, August 2026 (as reported by CIT = **4.2** % (2026-08-01..2026-08-31) [keep: ] quote: "8月工业企业利润增速进一步回落至4.2%,营收同步放缓,基数压力开始显现"
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 3; period_end 2026-12-31 after as_of: 2)

### d6 [shocks] Policy and cost shock monitor

Hypothesis: September 2026 profits may deviate from seasonal patterns because of policy, commodity, trade, or energy shocks. Measurable shocks such as tariffs, export controls, fuel and coal prices, equipment renewal subsidies, or property activity can adjust the September increment estimate.

Queries issued by the searcher: 2026年1-9月 规模以上工业企业利润总额 国家统计局; China industrial profits September 2026 National Bureau of Statistics; 2026年9月 PPI 同比 上涨 5.0% 工业生产者出厂价格 国家统计局 10月; 2025年1-9月 规模以上工业企业利润总额 53732.0亿元 同比增长3.2%

- `https://m.cnstock.com/commonDetail/795983` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.news.cn/fortune/20261014/2ca7672b7f7741e29a1421cbc3dcf9b8/c.html` -> **live_dated** (page date 2026-10-14); points raw/verified 15/15
  - p202 China PPI month-on-month change, September 2026 = **1.2** % (2026-09-01..2026-09-30) [keep: ] quote: "工业生产者出厂价格指数(PPI)环比上涨1.2%,涨幅比上月扩大0.8个百分点"
  - p203 China PPI year-on-year change, September 2026 = **5** % (2026-09-01..2026-09-30) [keep: ] quote: "同比上涨5.0%,涨幅比上月扩大1.2个百分点"
  - p204 China CPI month-on-month change, September 2026 = **0.2** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,居民消费价格指数(CPI)环比上涨0.2%,涨幅比上月回落0.2个百分点"
  - p205 China CPI year-on-year change, September 2026 = **0.9** % (2026-09-01..2026-09-30) [keep: ] quote: "同比上涨0.9%,涨幅比上月扩大0.1个百分点"
  - p206 China core CPI year-on-year change (excluding food and energy), September 2026 = **1** % (2026-09-01..2026-09-30) [keep: ] quote: "扣除食品和能源价格的核心CPI同比上涨1.0%,涨幅与上月相同"
  - p207 China coal mining and washing industry PPI month-on-month change, September 2026 = **9.5** % (2026-09-01..2026-09-30) [keep: ] quote: "煤炭开采和洗选业、煤炭加工价格分别上涨9.5%和13.6%"
  - p208 China coal processing industry PPI month-on-month change, September 2026 = **13.6** % (2026-09-01..2026-09-30) [keep: ] quote: "煤炭开采和洗选业、煤炭加工价格分别上涨9.5%和13.6%"
  - p209 China oil extraction industry PPI month-on-month change, September 2026 = **14.5** % (2026-09-01..2026-09-30) [keep: ] quote: "石油开采、精炼石油产品制造、有机化学原料制造价格分别上涨14.5%、7.4%和5.4%"
  - p210 China refined petroleum products manufacturing PPI month-on-month change, Septem = **7.4** % (2026-09-01..2026-09-30) [keep: ] quote: "石油开采、精炼石油产品制造、有机化学原料制造价格分别上涨14.5%、7.4%和5.4%"
  - p211 China organic chemical raw materials manufacturing PPI month-on-month change, Se = **5.4** % (2026-09-01..2026-09-30) [keep: ] quote: "石油开采、精炼石油产品制造、有机化学原料制造价格分别上涨14.5%、7.4%和5.4%"
  - p212 China non-metallic mineral products PPI month-on-month change, September 2026 (f = **0.3** % (2026-09-01..2026-09-30) [keep: ] quote: "非金属矿物制品业价格在连降7个月后转为上涨0.3%"
  - p213 China ferrous metal smelting and rolling PPI month-on-month change, September 20 = **0.2** % (2026-09-01..2026-09-30) [keep: ] quote: "黑色金属冶炼和压延加工业价格上涨0.2%"
  - p214 China electricity and heat production and supply PPI year-on-year change, Septem = **3.9** % (2026-09-01..2026-09-30) [keep: ] quote: "电力热力生产和供应业下降3.9%"
  - p215 China coal mining and washing industry PPI year-on-year change, September 2026 = **35.3** % (2026-09-01..2026-09-30) [keep: ] quote: "煤炭开采和洗选业上涨35.3%"
  - p216 China chemical raw materials and chemical products manufacturing PPI year-on-yea = **12.1** % (2026-09-01..2026-09-30) [keep: ] quote: "石油和天然气开采业、石油煤炭及其他燃料加工业、化学原料和化学制品制造业分别上涨24.5%、21.6%和12.1%"
- `https://finance.cnr.cn/ycbd/20261014/t20261014_527841877.shtml` -> **live_dated** (page date 2026-10-14); points raw/verified 15/14
  - p217 China PPI year-on-year change, September 2026 = **5** % (2026-09-01..2026-09-30) [keep: ] quote: "PPI(工业生产者出厂价格指数)环比上涨1.2%,涨幅比上月扩大0.8个百分点;同比上涨5.0%,涨幅比上月扩大1.2个百分点。"
  - p218 China PPI month-on-month change, September 2026 = **1.2** % (2026-09-01..2026-09-30) [keep: ] quote: "PPI(工业生产者出厂价格指数)环比上涨1.2%,涨幅比上月扩大0.8个百分点"
  - p219 Combined contribution of 8 industries with widening price increases to PPI year- = **5.42** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "8个行业涨幅比上月均扩大,合计影响PPI同比上涨约5.42个百分点,上拉影响比上月增加1.12个百分点。"
  - p220 China oil and gas extraction industry PPI year-on-year change, September 2026 = **24.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,石油和天然气开采业、石油煤炭及其他燃料加工业价格同比分别上涨24.5%、21.6%"
  - p221 China petroleum, coal and other fuel processing industry PPI year-on-year change = **21.6** % (2026-09-01..2026-09-30) [keep: ] quote: "石油和天然气开采业、石油煤炭及其他燃料加工业价格同比分别上涨24.5%、21.6%"
  - p222 China chemical raw materials and chemical products manufacturing PPI year-on-yea = **12.1** % (2026-09-01..2026-09-30) [keep: ] quote: "化学原料和化学制品制造业、有色金属冶炼和压延加工业分别上涨12.1%、21.4%"
  - p223 China non-ferrous metal smelting and rolling processing industry PPI year-on-yea = **21.4** % (2026-09-01..2026-09-30) [keep: ] quote: "化学原料和化学制品制造业、有色金属冶炼和压延加工业分别上涨12.1%、21.4%"
  - p224 International oil price increase, mid-August to mid-September 2026 = **13.5** % (2026-08-15..2026-09-15) [keep: ] quote: "数据上8月中旬至9月中旬油价回升13.5%,直接带动9月油气开采PPI环比上行10.4%"
  - p225 China oil and gas extraction PPI month-on-month change, September 2026 = **10.4** % (2026-09-01..2026-09-30) [keep: ] quote: "直接带动9月油气开采PPI环比上行10.4%"
  - p226 Imported crude oil freight index increase, September 2026 = **150** % (2026-09-01..2026-09-30) [keep: ] quote: "同时9月进口原油运价指数大幅上涨近150%,也加剧输入性通胀压力。"
  - p227 Crude oil chain contribution to PPI month-on-month change, September 2026 = **0.5** percentage points (2026-09-01..2026-09-30) [keep: ] quote: "综合测算,原油链条对9月PPI环比贡献为0.5个百分点。"
  - p228 China producer goods PPI year-on-year change, September 2026 = **6.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月生产资料价格同比上涨6.5%,生活资料价格仍下降0.1%,PPI与CPI同比涨幅差扩大至4.1个百分点。"
  - p229 China industrial enterprise profits growth, January-August 2026 = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "前8个月工业企业利润增长15.7%,其中电子行业利润增长1.1倍"
  - p230 China automobile manufacturing industry profit change, January-August 2026 = **16** % (2026-01-01..2026-08-31) [keep: ] quote: "但汽车制造业营业收入增长2.9%、利润下降16.0%,部分中下游企业仍面临成本上涨、增收不增利的压力。"
- `https://data.eastmoney.com/report/zw_macresearch.jshtml?encodeUrl=sSrzFU7ZQF7OHytrGVkkUxhuoktJ8qD0DnFfkbWj0CA=` -> **live_dated** (page date 2026-10-19); points raw/verified 15/14
  - p231 China industrial enterprises above designated size cumulative profits year-on-ye = **15.7** % (2026-01-01..2026-08-31) [keep: ] quote: "1-8月份,全国规模以上工业企业实现利润总额52720亿元,同比增长15.7%。"
  - p232 China PPI year-on-year change, September 2026 = **5** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,9月份同比上涨5.0%,涨幅比上月扩大1.2个百分点;环比上涨1.2%。"
  - p233 China PPI month-on-month change, September 2026 = **1.2** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,9月份同比上涨5.0%,涨幅比上月扩大1.2个百分点;环比上涨1.2%。"
  - p234 China PPI year-on-year change, January-September 2026 cumulative = **2.3** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季度,全国工业生产者出厂价格同比下降2.3%。"
  - p235 China industrial producer purchase price year-on-year change, September 2026 = **6.9** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,9月份同比上涨6.9%,环比上涨1.2%。"
  - p236 China industrial producer purchase price year-on-year change, January-September  = **3.6** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季度,全国工业生产者购进价格同比上涨3.6%。"
  - p237 China industrial value added above designated size year-on-year growth, Septembe = **5.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业增加值同比增长5.5%,比上月加快0.3个百分点;环比增长0.61%。"
  - p238 China industrial value added above designated size month-on-month growth, Septem = **0.61** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业增加值同比增长5.5%,比上月加快0.3个百分点;环比增长0.61%。"
  - p239 China industrial value added above designated size year-on-year growth, January- = **5.3** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季度,全国规模以上工业增加值同比增长5.3%。"
  - p240 China manufacturing PMI, September 2026 = **50.1** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,制造业采购经理指数为50.1%,比上月上升0.3个百分点;企业生产经营活动预期指数为53.8%,与上月持平。"
  - p241 China exports year-on-year growth, September 2026 = **29.6** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,出口30344亿元,增长29.6%;进口21284亿元,增长24.6%。"
  - p242 China imports year-on-year growth, September 2026 = **24.6** % (2026-09-01..2026-09-30) [keep: ] quote: "其中,出口30344亿元,增长29.6%;进口21284亿元,增长24.6%。"
  - p243 China real estate development investment year-on-year change, January-September  = **20.6** % (2026-01-01..2026-09-30) [keep: ] quote: "分领域看,基础设施投资同比下降4.2%,制造业投资下降2.1%,房地产开发投资下降20.6%。"
  - p244 China infrastructure investment year-on-year change, January-September 2026 cumu = **4.2** % (2026-01-01..2026-09-30) [keep: ] quote: "分领域看,基础设施投资同比下降4.2%,制造业投资下降2.1%,房地产开发投资下降20.6%。"
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 1; number: value_as_written is only part of a larger CJK number in the quote: 1)

### d7 [base_rates] Stable ratio / comparable year

Hypothesis: The ratio of industrial profits to nominal industrial value added or GDP has some persistence. Applying the 2025 January-September ratio to estimated 2026 nominal industrial value added gives a rough level check, though coverage mismatch means it is only a constraint.

Queries issued by the searcher: 2025年1-9月 规模以上工业企业利润总额 统计局; 2026年1-9月 规模以上工业增加值 同比增长; 2026年1-9月 全国 PPI 工业生产者出厂价格 同比下降 统计局; 2026年前三季度 GDP 工业增加值 绝对额 亿元 分行业

- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202510/t20251027_1961695.html` -> **live_dated** (page date 2025-10-27); points raw/verified 15/7
  - p245 China total operating revenue of industrial enterprises above designated size, J = **1,020,847** 亿元 (100 million CNY) (2025-01-01..2025-09-30) [keep: ] quote: "\| 总计 \| 1020846.7 \| 2.4 \| 873426.0 \| 2.6 \| 53732.0 \| 3.2 \|"
  - p246 China operating revenue profit margin (profit total / operating revenue) for ind = **5.26** % (2025-01-01..2025-09-30) [keep: ] quote: "营业收入利润率为5.26%,同比提高0.04个百分点。"
  - p247 China total operating cost of industrial enterprises above designated size, Janu = **873,426** 亿元 (100 million CNY) (2025-01-01..2025-09-30) [keep: ] quote: "\| 总计 \| 1020846.7 \| 2.4 \| 873426.0 \| 2.6 \| 53732.0 \| 3.2 \|"
  - p248 China total profits of industrial enterprises above designated size, January-Sep = **3.2** % (2025-01-01..2025-09-30) [keep: ] quote: "2025年1-9月份全国规模以上工业企业利润增长3.2%"
  - p249 China total operating revenue of industrial enterprises above designated size, J = **2.4** % (2025-01-01..2025-09-30) [keep: ] quote: "1-9月份,规模以上工业企业实现营业收入102.08万亿元,同比增长2.4%"
  - p250 China industrial enterprises above designated size monthly profit year-on-year g = **21.6** % (2025-09-01..2025-09-30) [keep: ] quote: "9月份,规模以上工业企业利润同比增长21.6%。"
  - p251 Threshold for inclusion as industrial enterprise above designated size (annual m = **20,000,000** 元 (CNY) (not stated (page dated 2025-10-27)) [keep: ] quote: "规模以上工业企业,即年主营业务收入为2000万元及以上的工业法人单位。"
- `https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261019_1965617.html` -> **live_dated** (page date 2026-10-19); points raw/verified 15/14
  - p252 China industrial value added above designated size, January-September 2026, year = **5.3** % (2026-01-01..2026-09-30) [keep: ] quote: "1-9月份,规模以上工业增加值同比增长5.3%。"
  - p253 China industrial value added above designated size, September 2026, year-on-year = **5.5** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业增加值同比实际增长5.5%(增加值增速均为扣除价格因素的实际增长率)"
  - p254 China industrial value added above designated size, September 2026, month-on-mon = **0.61** % (2026-09-01..2026-09-30) [keep: ] quote: "从环比看,9月份,规模以上工业增加值比上月增长0.61%。"
  - p255 China manufacturing value added above designated size, January-September 2026, y = **5.7** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 制造业 \| ... \| 6.0 \| ... \| 5.7 \|"
  - p256 China high-tech manufacturing value added above designated size, January-Septemb = **14.3** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 其中:高技术制造业 \| ... \| 15.3 \| ... \| 14.3 \|"
  - p257 China mining value added above designated size, January-September 2026, year-on- = **2** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 采矿业 \| ... \| 1.3 \| ... \| 2.0 \|"
  - p258 China electricity, heat, gas and water production and supply value added above d = **5.4** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 电力、热力、燃气及水生产和供应业 \| ... \| 5.6 \| ... \| 5.4 \|"
  - p259 China industrial enterprises above designated size, January-September 2026, expo = **127,416** 亿元 (100 million CNY) (2026-01-01..2026-09-30) [keep: ] quote: "\| 出口交货值(亿元) \| 17132 \| 17.0 \| 127416 \| 10.7 \|"
  - p260 China industrial enterprises above designated size, January-September 2026, prod = **96.4** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 产品销售率(%) \| 97.0 \| -0.2(百分点) \| 96.4 \| 0.1(百分点) \|"
  - p261 China industrial enterprises above designated size, September 2026, product sale = **97** % (2026-09-01..2026-09-30) [keep: ] quote: "9月份,规模以上工业企业产品销售率为97.0%,同比下降0.2个百分点"
  - p262 China industrial enterprises above designated size, January-September 2026, elec = **74,916** 亿千瓦时 (100 million kWh) (2026-01-01..2026-09-30) [keep: ] quote: "\| 规模以上工业发电量(亿千瓦时) \| 8294 \| -1.2 \| 74916 \| 2.2 \|"
  - p263 China industrial enterprises above designated size, January-September 2026, crud = **72,477** 万吨 (10 thousand tonnes) (2026-01-01..2026-09-30) [keep: ] quote: "\| 粗钢(万吨) \| 7359 \| 0.1 \| 72477 \| -2.9 \|"
  - p264 China industrial enterprises above designated size, January-September 2026, ceme = **113,119** 万吨 (10 thousand tonnes) (2026-01-01..2026-09-30) [keep: ] quote: "\| 水泥(万吨) \| 14401 \| -5.3 \| 113119 \| -8.6 \|"
  - p265 China industrial enterprises above designated size, January-September 2026, auto = **2,337** 万辆 (10 thousand vehicles) (2026-01-01..2026-09-30) [keep: ] quote: "\| 汽车(万辆) \| 306.3 \| -5.7 \| 2337.2 \| -3.7 \|"
- `https://china-data-online.com/acmr-cndata-pub/report/reportshow.htm?id=2412` -> **live_dated** (page date 2026-10-15); points raw/verified 0/0
- `https://calendar.cngold.org/content/304103.htm` -> **live_dated** (page date 2026-10-14); points raw/verified 0/0
- dropped by code checks: 9 (number: value_as_written is only part of a larger CJK number in the quote: 9)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a** CNY, 80% interval [n/a, n/a] CNY, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms none (no entity constraint); measure stems ['above', 'cny', 'cumul', 'desig', 'enter', 'indus', 'milli', 'profi', 'size']
Early checks while the sub-agents were running: 3 (not_confirmed); details in state.json -> published_early.


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

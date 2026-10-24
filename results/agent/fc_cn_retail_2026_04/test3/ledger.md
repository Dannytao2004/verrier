# Evidence ledger: fc_cn_retail_2026_04

- Question: Assume today is 2026-04-18. You know nothing published after this date. Estimate China's total retail sales of consumer goods (社会消费品零售总额) for the single month of April 2026 (not the January-April cumulative total), in Chinese yuan (CNY; the release states it in 亿元, i.e. units of 100 million yuan), as it will be first reported in the National Bureau of Statistics of China's monthly release on retail sales of consumer goods.
- as_of: 2026-04-18
- Pinned target: China's total retail sales of consumer goods (社会消费品零售总额), single month of April 2026, as first reported by NBS in the monthly release (亿元) | unit 100 million CNY (亿元) | period 2026-04-01..2026-04-30 | publisher National Bureau of Statistics of China (NBS)

- Official value (scoring only, never shown to the agent): 3,724,700,000,000

## Directions and pages

### d1 [own_history] NBS monthly releases

Hypothesis: April 2026 level = April 2025 level × (1 + April 2026 y/y growth). April 2025 single-month value and recent 2025-2026 monthly values anchor the base; seasonal April pattern (post-Q1, pre-May holiday) constrains the level.

Queries issued by the searcher: 国家统计局 社会消费品零售总额 2025年4月份 同比; 社会消费品零售总额 2026年3月份 同比 国家统计局; 2026年1-2月份社会消费品零售总额 同比增长 国家统计局; 2025年12月份社会消费品零售总额 亿元 同比增长 全年

- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/4
  - p1 China total retail sales of consumer goods, March 2026 y/y growth = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p6/p21/p35/p49 (same March 2026 1.7% growth); no added information.] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p2 China retail sales excluding automobiles, March 2026 y/y growth = **3.2** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p8/p23/p36/p51 (March ex-auto 3.2%).] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p3 China total retail sales of consumer goods, Jan-Mar 2026 cumulative y/y growth = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p10/p25/p37/p53 (Q1 2.4%).] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p4 Share of online goods retail sales in total retail sales of consumer goods, Jan- = **24.8** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p19/p34/p39 (online share 24.8%).] quote: "其中,网上商品零售额31614亿元,增长7.5%,占社会消费品零售总额的比重为24.8%;"
- `https://data.mofcom.gov.cn/article/zxtj/202603/64405.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://big5.www.gov.cn/gate/big5/www.gov.cn/lianbo/bumen/202505/content_7024242.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (number: value_as_written is only part of a larger CJK number in the quote: 11)

### d2 [related_series] NBS monthly release structure

Hypothesis: April 2026 y/y growth can be estimated from Q1 2026 cumulative growth and March 2026 monthly growth, adjusted for base effects and calendar (April 2026 has same number of days; Qingming timing). Target = April 2025 × (1+g).

Queries issued by the searcher: 2026年一季度 社会消费品零售总额 同比 国家统计局; 国家统计局 2026年3月份 社会消费品零售总额; 2025年4月份社会消费品零售总额 37174亿元 同比增长5.1%; 4月 社会消费品零售总额 预测 2026年4月 同比 基数 高基数

- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/15
  - p5 China total retail sales of consumer goods, March 2026 single month = **4,161,600,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p20/p48 (March total 41616亿元).] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p6 China total retail sales of consumer goods, March 2026 y/y growth = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p21/p35/p49.] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p7 China retail sales excluding automobiles, March 2026 single month = **3,787,500,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p22/p50 (March ex-auto level).] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p8 China retail sales excluding automobiles, March 2026 y/y growth = **3.2** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p23/p36/p51.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p9 China total retail sales of consumer goods, Q1 2026 (Jan-Mar) cumulative = **12,769,500,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p24/p52 (Q1 total).] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p10 China total retail sales of consumer goods, Q1 2026 (Jan-Mar) cumulative y/y gro = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p25/p37/p53.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p11 China retail sales excluding automobiles, Q1 2026 cumulative = **11,772,700,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p26/p54 (Q1 ex-auto level).] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p12 China retail sales excluding automobiles, Q1 2026 cumulative y/y growth = **3.6** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p27/p38/p55.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p13 China urban retail sales, March 2026 single month = **3,612,500,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: March urban level; not needed and duplicated in scope by total/goods splits.] quote: "3月份,城镇消费品零售额36125亿元,同比增长1.5%;乡村消费品零售额5491亿元,增长2.7%。"
  - p14 China rural retail sales, March 2026 single month = **549,100,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: March rural level; not needed.] quote: "3月份,城镇消费品零售额36125亿元,同比增长1.5%;乡村消费品零售额5491亿元,增长2.7%。"
  - p15 China goods retail sales, March 2026 single month = **3,725,700,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p28/p56 (March goods level).] quote: "3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p16 China catering revenue, March 2026 single month = **435,900,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p30/p58 (March catering level).] quote: "3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p17 China goods retail sales, Q1 2026 cumulative = **11,307,200,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p32/p62 (Q1 goods level).] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p18 China catering revenue, Q1 2026 cumulative = **1,462,300,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p33/p60 (Q1 catering level).] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p19 China online goods retail sales share of total retail sales, Q1 2026 cumulative = **24.8** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p34/p39.] quote: "其中,网上商品零售额31614亿元,增长7.5%,占社会消费品零售总额的比重为24.8%;"
- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.cnr.cn/native/gd/kx/20260416/t20260416_527586744.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.xinhuanet.com/fortune/20260416/c89c2dcc907447a18b6c4e2813e443ce/c.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Sub-component decomposition

Hypothesis: Total = goods retail (above-designated-size + below) + catering; or by category (autos, petroleum, home appliances, food, apparel, cosmetics, gold/jewelry). Summing major category y/y contributions weighted by April 2025 shares gives an alternative growth estimate.

Queries issued by the searcher: 社会消费品零售总额 分品类 2025 占比 汽车 石油 粮油食品; 2026年3月 限额以上 商品零售 同比 汽车 石油 家电 统计局; 国家统计局 2026年3月份社会消费品零售总额 41,616亿元 限额以上单位商品零售额 分品类 汽车 石油 通讯器材; 2025年4月份社会消费品零售总额 限额以上 汽车类 石油及制品类 零售额 亿元 同比

- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/15
  - p20 China total retail sales of consumer goods, March 2026, single month = **4,161,600,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p48 (March total).] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p21 China total retail sales of consumer goods, March 2026, year-on-year growth = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p49.] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p22 China retail sales excluding automobiles, March 2026, single month = **3,787,500,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p50.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p23 China retail sales excluding automobiles, March 2026, year-on-year growth = **3.2** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p51.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p24 China total retail sales of consumer goods, January-March 2026 cumulative = **12,769,500,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p52.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p25 China total retail sales of consumer goods, January-March 2026 cumulative, year- = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p53.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p26 China retail sales excluding automobiles, January-March 2026 cumulative = **11,772,700,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p54.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p27 China retail sales excluding automobiles, January-March 2026 cumulative, year-on = **3.6** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p55.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p28 China goods retail sales, March 2026, single month = **3,725,700,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p56.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p29 China goods retail sales, March 2026, year-on-year growth = **1.5** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p57.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p30 China catering revenue, March 2026, single month = **435,900,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p58.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p31 China catering revenue, March 2026, year-on-year growth = **2.9** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p59.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p32 China goods retail sales, January-March 2026 cumulative = **11,307,200,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p62.] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p33 China catering revenue, January-March 2026 cumulative = **1,462,300,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p60.] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p34 China online retail sales of goods and services as share of total retail sales o = **24.8** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p39.] quote: "其中,网上商品零售额31614亿元,增长7.5%,占社会消费品零售总额的比重为24.8%;"
- `http://fgw.yichang.gov.cn/content-39409-984262-1.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://biz.haiwainet.cn/n/2026/0228/c3545018-32934287.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/829922655547/index.phtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [shocks] Policy and calendar effects

Hypothesis: Trade-in / consumer subsidy programs (以旧换新) for autos and home appliances boosted 2024-2025 sales and may fade or extend in 2026; policy changes shift April 2026 growth versus trend. Calendar: April 2026 has 30 days; Qingming and pre-May-Day effects.

Queries issued by the searcher: 以旧换新 2026 汽车 家电 补贴 政策 延续; 乘联会 2026年4月 零售 销量 预测; 2026年3月 社会消费品零售总额 同比增长 国家统计局 一季度; 乘联会 2026年4月 第一周 第二周 日均零售 同比

- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/5
  - p35 China total retail sales of consumer goods, March 2026, year-on-year growth = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p49.] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p36 China retail sales excluding autos, March 2026, year-on-year growth = **3.2** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p51.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p37 China total retail sales of consumer goods, Jan-Mar 2026 cumulative year-on-year = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p53.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p38 China retail sales excluding autos, Jan-Mar 2026 cumulative year-on-year growth = **3.6** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p55.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p39 Share of online goods retail sales in total retail sales of consumer goods, Jan- = **24.8** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p34/p19.] quote: "网上商品零售额31614亿元,增长7.5%,占社会消费品零售总额的比重为24.8%"
- `https://www.gov.cn/zhengce/zhengceku/202512/content_7053397.htm` -> **snapshot** (snapshot 20260209164046); points raw/verified 0/0
- `https://stcn.com/article/detail/3566506.html` -> **snapshot** (snapshot 20251231095500); points raw/verified 15/2
  - p40 2025 auto trade-in vehicles (cumulative through 2025-12-28) = **11,500,000** vehicles (2025-01-01..2025-12-28) [keep: Context for subsidy-inflated 2025 auto base; not used numerically but informative for a3.] quote: "截至2025年12月28日,2025年汽车以旧换新超1150万辆"
  - p41 2025 new car sales value driven by auto trade-in (cumulative through 2025-12-28) = **1,600,000,000,000** CNY (2025-01-01..2025-12-28) [keep: Same context as p40.] quote: "带动新车销售额超1.6万亿元"
- `https://www.d1ev.com/news/shichang/297153` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 23 (number: value_as_written is only part of a larger CJK number in the quote: 10; period_end 2026-12-31 after as_of: 12; value_as_written not in quote as a whole number: 1)

### d5 [related_series] Online vs offline split

Hypothesis: Total = online retail of physical goods + offline retail. Online physical goods retail has been growing faster; using its share (~25-27%) and growth plus offline growth gives a cross-check on total growth.

Queries issued by the searcher: 实物商品网上零售额 2026年一季度 同比 增长; 2026年一季度 社会消费品零售总额 网上零售额 占比; 2026年4月 社会消费品零售总额 预测 同比 机构 前瞻; 2026年1-2月 实物商品网上零售额 占社会消费品零售总额比重 两年

- `http://www.jingjiribao.cn/static/detail.jsp?id=650307` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stock.finance.sina.com.cn/stock/view/paper.php?symbol=sh000001&reportid=829755844571&autocallup=no&isfromsina=no` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.cnr.cn/native/gd/kx/20260416/t20260416_527586744.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.scio.gov.cn/live/2026/38333/tw/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Analyst and institutional forecasts

Hypothesis: Published forecasts for April 2026 or Q2 2026 retail sales growth (from brokers, IMF, World Bank, or NBS-adjacent commentary) constrain the y/y growth input; consensus forecasts cluster around a central value.

Queries issued by the searcher: China retail sales April 2026 forecast y/y growth; 中国 社会消费品零售总额 2026年4月 预测 同比; China March 2026 retail sales forecast preview Q1 GDP April 2026 expectations; 中国 2026年3月 社会消费品零售总额 同比 预测 一季度 GDP 前瞻

- `https://investinglive.com/news/economic-calendar-in-asia-thursday-april-16-australian-jobs-china-gdp-eco-activity-20260415/` -> **snapshot** (snapshot 20260416163615); points raw/verified 9/6
  - p42 China retail sales forecast, March, year-on-year growth = **2.5** % (2026-03-01..2026-03-31) [DISCARD: March 2026 retail forecast (2.5%) already superseded by actual March (1.7%); not an April 2026 input.] quote: "March activity indicators are expected to remain soft overall, with retail sales forecast to slow to around 2.5% year-on-year"
  - p43 China GDP forecast, Q1 2026, year-on-year growth (lower bound) = **4.7** % year-on-year (2026-01-01..2026-03-31) [DISCARD: Q1 GDP forecast; not a retail input.] quote: "Economists broadly expect the January-March expansion to come in around 4.7-4.8% year-on-year"
  - p44 China GDP forecast, Q1 2026, year-on-year growth (upper bound) = **4.8** % year-on-year (2026-01-01..2026-03-31) [DISCARD: Q1 GDP forecast; not a retail input.] quote: "Economists broadly expect the January-March expansion to come in around 4.7-4.8% year-on-year"
  - p45 China GDP forecast, Q1 2026, quarter-on-quarter growth = **1.3** % (2026-01-01..2026-03-31) [DISCARD: Q1 GDP q/q forecast; not a retail input.] quote: "On a quarterly basis, activity is seen improving slightly to around 1.3%"
  - p46 China fixed-asset investment forecast, year-to-date growth = **1.9** % (2026-01-01..2026-03-31) [DISCARD: Fixed-asset investment forecast; not a retail input.] quote: "Fixed-asset investment is also seen subdued at roughly 1.9% year-to-date"
  - p47 China industrial production forecast, year-on-year growth = **5.5** % (2026-03-01..2026-03-31) [DISCARD: Industrial production forecast; not a retail input.] quote: "Industrial production is a relative bright spot, projected to grow around 5.5% year-on-year"
- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/828782520181/index.phtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://latam.vtmarkets.com/live-updates/el-dr-henry-hao-de-commerzbank-preve-que-el-pib-de-china-en-el-primer-trimestre-de-2026-supere-el-4-6-impulsa` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.eastmoney.com/report/zw_strategy.jshtml?encodeUrl=XGWmSSG17O1invCqsvizvlQ+J+I3wUyojYU3/usfmWY=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 3)

### d7 [physical_flow] Upstream activity proxies

Hypothesis: Auto retail (passenger vehicle retail sales), petroleum retail, and catering revenue are large components; CPCA weekly/monthly retail and restaurant data provide early April 2026 signals that map to component growth.

Queries issued by the searcher: 乘联会 2026年4月 乘用车 零售 同比; China passenger vehicle retail April 2026 CPCA weekly; 2026年3月 社会消费品零售总额 同比 国家统计局 一季度 餐饮收入; 乘联会 2026年3月 乘用车零售 同比 3月1-31日

- `https://m.gasgoo.com/news/70453894.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/15
  - p48 China total retail sales of consumer goods, March 2026, monthly = **4,161,600,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p20/p5 (March total).] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p49 China total retail sales of consumer goods, March 2026, y/y growth = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p21/p35/p6.] quote: "3月份,社会消费品零售总额41616亿元,同比增长1.7%。"
  - p50 China retail sales excluding automobiles, March 2026, monthly = **3,787,500,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p22/p7.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p51 China retail sales excluding automobiles, March 2026, y/y growth = **3.2** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p23/p36/p8.] quote: "其中,除汽车以外的消费品零售额37875亿元,增长3.2%。"
  - p52 China total retail sales of consumer goods, Jan-Mar 2026, cumulative = **12,769,500,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p24/p9.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p53 China total retail sales of consumer goods, Jan-Mar 2026, cumulative y/y growth = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p25/p37/p10.] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
  - p54 China retail sales excluding automobiles, Jan-Mar 2026, cumulative = **11,772,700,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p26/p11.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p55 China retail sales excluding automobiles, Jan-Mar 2026, cumulative y/y growth = **3.6** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p27/p38/p12.] quote: "其中,除汽车以外的消费品零售额117727亿元,增长3.6%。"
  - p56 China goods retail sales, March 2026, monthly = **3,725,700,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p28/p15.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p57 China goods retail sales, March 2026, y/y growth = **1.5** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p29.] quote: "按消费类型分,3月份,商品零售额37257亿元,同比增长1.5%;餐饮收入4359亿元,增长2.9%。"
  - p58 China catering revenue, March 2026, monthly = **435,900,000,000** CNY (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p30/p16.] quote: "餐饮收入4359亿元,增长2.9%。"
  - p59 China catering revenue, March 2026, y/y growth = **2.9** % (2026-03-01..2026-03-31) [DISCARD: Redundant copy of p31.] quote: "餐饮收入4359亿元,增长2.9%。"
  - p60 China catering revenue, Jan-Mar 2026, cumulative = **1,462,300,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p33/p18.] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p61 China catering revenue, Jan-Mar 2026, cumulative y/y growth = **4.2** % (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p33/p18 growth.] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
  - p62 China goods retail sales, Jan-Mar 2026, cumulative = **11,307,200,000,000** CNY (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p32/p17.] quote: "1-3月份,商品零售额113072亿元,同比增长2.2%;餐饮收入14623亿元,增长4.2%。"
- `http://www.cada.cn/Trends/info_91_10469.html` -> **snapshot** (snapshot 20260411011155); points raw/verified 15/15
  - p63 China nationwide passenger vehicle retail sales, April 1-6 2026 (CPCA) = **149,000** vehicles (2026-04-01..2026-04-06) [DISCARD: Redundant with p66 (same CPCA first-week retail signal, 2.5万/day, -29%).] quote: "4月1-6日,全国乘用车市场零售14.9万辆,同比去年4月同期下降29%,较上月同期下降20%"
  - p64 China nationwide passenger vehicle retail sales y/y change, April 1-6 2026 (CPCA = **29** % (2026-04-01..2026-04-06) [DISCARD: Redundant with p66/p70 growth signal.] quote: "4月1-6日,全国乘用车市场零售14.9万辆,同比去年4月同期下降29%,较上月同期下降20%"
  - p65 China nationwide passenger vehicle retail sales m/m change, April 1-6 2026 (CPCA = **20** % (2026-04-01..2026-04-06) [DISCARD: m/m change; not needed for a y/y April estimate.] quote: "4月1-6日,全国乘用车市场零售14.9万辆,同比去年4月同期下降29%,较上月同期下降20%"
  - p66 China nationwide passenger vehicle daily average retail sales, first week of Apr = **25,000** vehicles per day (2026-04-01..2026-04-07) [keep: ] quote: "4月第一周全国乘用车市场日均零售2.5万辆,同比去年4月同期下降29%,较上月同期下降20%"
  - p67 China nationwide passenger vehicle wholesale sales, April 1-6 2026 (CPCA) = **153,000** vehicles (2026-04-01..2026-04-06) [DISCARD: Wholesale, not retail; not a retail-sales input.] quote: "4月1-6日,全国乘用车厂商批发15.3万辆,同比去年4月同期下降28%,较上月同期下降17%"
  - p68 China nationwide passenger vehicle wholesale sales y/y change, April 1-6 2026 (C = **28** % (2026-04-01..2026-04-06) [DISCARD: Wholesale growth; not a retail-sales input.] quote: "4月1-6日,全国乘用车厂商批发15.3万辆,同比去年4月同期下降28%,较上月同期下降17%"
  - p69 China nationwide new energy passenger vehicle retail sales, April 1-6 2026 (CPCA = **86,000** vehicles (2026-04-01..2026-04-06) [DISCARD: Redundant with p70/p71 NEV signal.] quote: "4月1-6日,全国乘用车市场新能源零售8.6万辆,同比去年4月同期下降24%,较上月同期增长3%"
  - p70 China nationwide new energy passenger vehicle retail sales y/y change, April 1-6 = **24** % (2026-04-01..2026-04-06) [keep: ] quote: "4月1-6日,全国乘用车市场新能源零售8.6万辆,同比去年4月同期下降24%,较上月同期增长3%"
  - p71 China nationwide new energy passenger vehicle retail penetration rate, April 1-6 = **57.7** % (2026-04-01..2026-04-06) [keep: ] quote: "4月1-6日,全国乘用车市场新能源零售渗透率57.7%"
  - p72 China nationwide new energy passenger vehicle wholesale penetration rate, April  = **47.5** % (2026-04-01..2026-04-06) [DISCARD: Wholesale NEV penetration; not a retail input.] quote: "4月1-6日,全国乘用车厂商新能源批发渗透率47.5%"
  - p73 China nationwide pure-fuel light vehicle production, first week of April 2026 (C = **176,000** vehicles (2026-04-01..2026-04-07) [DISCARD: Production, not retail; not a retail-sales input.] quote: "4月第一周,全国纯燃料轻型车生产17.6万辆,同比去年4月同期下降6%,较上月同期增长7%"
  - p74 China nationwide hybrid and plug-in hybrid production, first week of April 2026  = **85,000** vehicles (2026-04-01..2026-04-07) [DISCARD: Production, not retail; not a retail-sales input.] quote: "4月第一周,混合动力与插混总体生产8.5万辆,同比去年4月同期增长16%,较上月同期增长60%"
  - p75 China auto trade-in subsidy applications, January-March 2026 (MOFCOM) = **1,408,000** applications (2026-01-01..2026-03-31) [keep: ] quote: "1-3月,汽车以旧换新共计收到补贴申请140.8万份,报废更新补贴申请40.3万份;置换更新补贴申请100.5万份"
  - p76 China scrappage-update subsidy applications, January-March 2026 (MOFCOM) = **403,000** applications (2026-01-01..2026-03-31) [DISCARD: Sub-component of p75; redundant.] quote: "1-3月,汽车以旧换新共计收到补贴申请140.8万份,报废更新补贴申请40.3万份;置换更新补贴申请100.5万份"
  - p77 China replacement-update subsidy applications, January-March 2026 (MOFCOM) = **1,005,000** applications (2026-01-01..2026-03-31) [DISCARD: Sub-component of p75; redundant.] quote: "1-3月,汽车以旧换新共计收到补贴申请140.8万份,报废更新补贴申请40.3万份;置换更新补贴申请100.5万份"
- `https://www.jwview.com/jingwei/html/m/04-16/667280.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [base_rates] Seasonal share structure

Hypothesis: April typically accounts for a stable share (~7.5-8%) of annual retail sales; annual 2026 total (or 2025 annual × growth) × April share gives an independent level estimate.

Queries issued by the searcher: 2025年社会消费品零售总额 全年 501202亿; 社会消费品零售总额 2024年全年 487895亿元 12月份; 2025年4月份社会消费品零售总额增长5.1% 37174亿元; 2024年4月份社会消费品零售总额 35699亿元 同比增长2.3%

- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962323.html` -> **snapshot** (snapshot 20260119203021); points raw/verified 15/6
  - p78 China total retail sales of consumer goods, full year 2025 year-on-year growth = **3.7** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年,社会消费品零售总额501202亿元,比上年增长3.7%。"
  - p79 Physical goods online retail sales share of total retail sales, full year 2025 = **26.1** % (2025-01-01..2025-12-31) [keep: ] quote: "实物商品网上零售额130923亿元,增长5.2%,占社会消费品零售总额的比重为26.1%;"
  - p80 China total retail sales of consumer goods, April 2025 month-on-month growth (se = **0.26** percent (2025-04-01..2025-04-30) [DISCARD: Seasonally adjusted m/m; not usable to level April 2026 without a full SA series.] quote: "\| \| 4月 \| 0.26 \|"
  - p81 China total retail sales of consumer goods, December 2025 month-on-month growth  = **-0.12** percent (2025-12-01..2025-12-31) [DISCARD: Dec 2025 SA m/m; not an April 2026 input.] quote: "\| \| 12月 \| -0.12 \|"
  - p82 China above-designated-size units retail sales, full year 2025 = **201,618** 100 million CNY (亿元) (2025-01-01..2025-12-31) [DISCARD: Annual above-size total; not needed for April single-month estimate.] quote: "\| 其中:限额以上单位消费品零售额 \| 19547 \| -1.9 \| 201618 \| 3.3 \|"
  - p83 China above-designated-size units retail sales, December 2025 single month = **19,547** 100 million CNY (亿元) (2025-12-01..2025-12-31) [DISCARD: Dec 2025 above-size level; not an April 2026 input.] quote: "\| 其中:限额以上单位消费品零售额 \| 19547 \| -1.9 \| 201618 \| 3.3 \|"
- `http://big5.www.gov.cn/gate/big5/www.gov.cn/lianbo/bumen/202501/content_6999271.htm` -> **snapshot** (snapshot 20260117033548); points raw/verified 15/3
  - p84 China total retail sales of consumer goods, full year 2024, year-on-year growth = **3.5** % (2024-01-01..2024-12-31) [DISCARD: 2024 annual growth; superseded by 2025 (p78).] quote: "2024年,社會消費品零售總額487895億元,比上年增長3.5%。"
  - p85 Share of physical goods online retail sales in total retail sales of consumer go = **26.8** % (2024-01-01..2024-12-31) [DISCARD: 2024 online share; superseded by 2025 (p79).] quote: "實物商品網上零售額130816億元,增長6.5%,佔社會消費品零售總額的比重為26.8%"
  - p86 China total retail sales of consumer goods, December 2024, year-on-year growth = **3.7** % (2024-12-01..2024-12-31) [DISCARD: Dec 2024 total; not an April 2026 input.] quote: "12月份,社會消費品零售總額45172億元,同比增長3.7%。"
- `https://www.cnfin.com/yb-lb/detail/20250520/4236557_1.html` -> **snapshot** (snapshot 20250617204259); points raw/verified 15/15
  - p87 China total retail sales of consumer goods, April 2025, single month (NBS monthl = **3,717,400,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "4月份,社会消费品零售总额37174亿元,同比增长5.1%"
  - p88 China total retail sales of consumer goods, January-April 2025 cumulative = **16,184,500,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "1-4月份,社会消费品零售总额161845亿元,增长4.7%"
  - p89 China retail sales excluding automobiles, April 2025, single month = **3,354,800,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "除汽车以外的消费品零售额33548亿元,增长5.6%"
  - p90 China retail sales excluding automobiles, January-April 2025 cumulative = **14,700,500,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "除汽车以外的消费品零售额147005亿元,增长5.2%"
  - p91 China urban consumer goods retail sales, April 2025, single month = **3,237,600,000,000** CNY (2025-04-01..2025-04-30) [DISCARD: April 2025 urban level; not needed given total and goods/catering splits.] quote: "4月份,城镇消费品零售额32376亿元,同比增长5.2%"
  - p92 China rural consumer goods retail sales, April 2025, single month = **479,800,000,000** CNY (2025-04-01..2025-04-30) [DISCARD: April 2025 rural level; not needed.] quote: "乡村消费品零售额4798亿元,增长4.7%"
  - p93 China urban consumer goods retail sales, January-April 2025 cumulative = **14,043,300,000,000** CNY (2025-01-01..2025-04-30) [DISCARD: April 2025 urban cumulative; not needed.] quote: "1-4月份,城镇消费品零售额140433亿元,增长4.7%"
  - p94 China rural consumer goods retail sales, January-April 2025 cumulative = **2,141,200,000,000** CNY (2025-01-01..2025-04-30) [DISCARD: April 2025 rural cumulative; not needed.] quote: "乡村消费品零售额21412亿元,增长4.8%"
  - p95 China goods retail sales, April 2025, single month = **3,300,700,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "4月份,商品零售额33007亿元,同比增长5.1%"
  - p96 China catering revenue, April 2025, single month = **416,700,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "餐饮收入4167亿元,增长5.2%"
  - p97 China goods retail sales, January-April 2025 cumulative = **14,365,100,000,000** CNY (2025-01-01..2025-04-30) [DISCARD: April 2025 goods cumulative; single-month p95 suffices.] quote: "1-4月份,商品零售额143651亿元,增长4.7%"
  - p98 China catering revenue, January-April 2025 cumulative = **1,819,400,000,000** CNY (2025-01-01..2025-04-30) [DISCARD: April 2025 catering cumulative; single-month p96 suffices.] quote: "餐饮收入18194亿元,增长4.8%"
  - p99 China online retail sales, January-April 2025 cumulative = **4,741,900,000,000** CNY (2025-01-01..2025-04-30) [DISCARD: April 2025 total online (goods+services); p100 physical-goods is the relevant one.] quote: "1-4月份,全国网上零售额47419亿元,同比增长7.7%"
  - p100 China physical goods online retail sales, January-April 2025 cumulative = **3,926,500,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "实物商品网上零售额39265亿元,增长5.8%"
  - p101 County and township share of China total retail sales of consumer goods, January = **39.4** % (2025-01-01..2025-04-30) [DISCARD: County/township share; not needed.] quote: "县乡消费品市场规模占社会消费品零售总额的比重达到39.4%"
- dropped by code checks: 21 (number: value_as_written is only part of a larger CJK number in the quote: 21)

### b1 [related_series] d7 physical_flow

Hypothesis: Full-April 2026 CPCA passenger-vehicle retail (weeks 1-4) would let us size the auto drag on April retail. First-week data (p66) shows -29% y/y; if the full month confirms a large auto decline, the total April y/y growth is pulled well below the ex-auto trend, materially changing the estimate.

Queries issued by the searcher: 乘联会 2026年4月 第一周 乘用车零售 同比; CPCA April 2026 passenger vehicle retail weekly -29%; 国家统计局 2025年4月份 社会消费品零售总额 汽车类 零售额 亿元; 2026年4月 车市扫描 乘联会 4月1-12日 零售 37.7万辆 同比降20%

- `https://m.mysteel.com/a/26041516/BA335CEA530D790C_abc.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.eastmoney.com/a/202505193408630152.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.163.com/dy/article/KQD0GJDI0550B6IS.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.shanqx.com/index.php?m=home&c=View&a=index&aid=3323` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [forecasts_markets] d6 forecasts_markets

Hypothesis: Broker/consensus forecasts for April 2026 retail sales y/y growth (published early May) would directly constrain the growth input in the yoy_scaling route and resolve the tension between the weak auto signal and the ~2-3% ex-auto trend.

Queries issued by the searcher: China March 2026 retail sales y/y National Bureau of Statistics; 中国 2026年3月 社会消费品零售总额 同比 增长; 2025年4月份社会消费品零售总额 37174亿元 同比增长5.1%; 券商 预测 2026年4月 社会消费品零售总额 同比 增速 预测

- `https://www.stats.gov.cn/english/PressRelease/202604/t20260417_1963351.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=679968&year=2026&ctyall=10737566&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/829835008728/index.phtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] d8 base_rates

Hypothesis: A clean April seasonal share of annual retail sales (April 2025 / 2025 annual) would enable an independent annual×share route to cross-check the yoy_scaling level; currently no kept point gives the April share directly.

Queries issued by the searcher: NBS 2025 annual total retail sales consumer goods 501202亿元 2025; 国家统计局 2025年4月份 社会消费品零售总额 37174亿元; 2024年4月份 社会消费品零售总额 35699亿元 国家统计局; 2023年4月份 社会消费品零售总额 34910亿元 国家统计局

- `https://www.chinanews.com.cn/cj/2025/05-19/10417916.shtml` -> **snapshot** (snapshot 20250520154443); points raw/verified 15/15
  - p102 China total retail sales of consumer goods, April 2025 single month = **3,717,400,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "4月份,社会消费品零售总额37174亿元,同比增长5.1%。"
  - p103 China total retail sales of consumer goods, April 2025 yoy growth = **5.1** % (2025-04-01..2025-04-30) [keep: ] quote: "4月份,社会消费品零售总额37174亿元,同比增长5.1%。"
  - p104 China retail sales excluding automobiles, April 2025 single month = **3,354,800,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "其中,除汽车以外的消费品零售额33548亿元,增长5.6%。"
  - p105 China total retail sales of consumer goods, Jan-Apr 2025 cumulative = **16,184,500,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "1-4月份,社会消费品零售总额161845亿元,增长4.7%。"
  - p106 China retail sales excluding automobiles, Jan-Apr 2025 cumulative = **14,700,500,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "其中,除汽车以外的消费品零售额147005亿元,增长5.2%。"
  - p107 China urban retail sales, April 2025 single month = **3,237,600,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "4月份,城镇消费品零售额32376亿元,同比增长5.2%;"
  - p108 China rural retail sales, April 2025 single month = **479,800,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "乡村消费品零售额4798亿元,增长4.7%。"
  - p109 China urban retail sales, Jan-Apr 2025 cumulative = **14,043,300,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "1-4月份,城镇消费品零售额140433亿元,增长4.7%;"
  - p110 China rural retail sales, Jan-Apr 2025 cumulative = **2,141,200,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "乡村消费品零售额21412亿元,增长4.8%。"
  - p111 China goods retail sales, April 2025 single month = **3,300,700,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "4月份,商品零售额33007亿元,同比增长5.1%;"
  - p112 China catering revenue, April 2025 single month = **416,700,000,000** CNY (2025-04-01..2025-04-30) [keep: ] quote: "餐饮收入4167亿元,增长5.2%。"
  - p113 China goods retail sales, Jan-Apr 2025 cumulative = **14,365,100,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "1-4月份,商品零售额143651亿元,增长4.7%;"
  - p114 China catering revenue, Jan-Apr 2025 cumulative = **1,819,400,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "餐饮收入18194亿元,增长4.8%。"
  - p115 China online retail sales, Jan-Apr 2025 cumulative = **4,741,900,000,000** CNY (2025-01-01..2025-04-30) [keep: ] quote: "1-4月份,全国网上零售额47419亿元,同比增长7.7%。"
  - p116 China physical goods online retail sales share of total retail sales, Jan-Apr 20 = **24.3** % (2025-01-01..2025-04-30) [keep: ] quote: "实物商品网上零售额39265亿元,增长5.8%,占社会消费品零售总额的比重为24.3%;"
- `https://www.stcn.com/article/detail/3599344.html` -> **snapshot** (snapshot 20260119023656); points raw/verified 12/12
  - p117 China total retail sales of consumer goods, 2025 annual = **50,120,200,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "2025年社会消费品零售总额501202亿元,比上年增长3.7%"
  - p118 China total retail sales of consumer goods, 2025 annual, year-on-year growth = **3.7** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年社会消费品零售总额501202亿元,比上年增长3.7%"
  - p119 China urban consumer goods retail sales, 2025 annual = **43,297,200,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "城镇消费品零售额432972亿元,增长3.6%"
  - p120 China rural consumer goods retail sales, 2025 annual = **6,823,000,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "乡村消费品零售额68230亿元,增长4.1%"
  - p121 China goods retail sales, 2025 annual = **44,322,000,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "商品零售额443220亿元,增长3.8%"
  - p122 China catering revenue, 2025 annual = **5,798,200,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "餐饮收入57982亿元,增长3.2%"
  - p123 China online retail sales, 2025 annual = **15,972,200,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "全国网上零售额159722亿元,比上年增长8.6%"
  - p124 China online retail sales of physical goods, 2025 annual = **13,092,300,000,000** CNY (2025-01-01..2025-12-31) [keep: ] quote: "实物商品网上零售额130923亿元,增长5.2%"
  - p125 China online retail sales of physical goods as share of total retail sales, 2025 = **26.1** % (2025-01-01..2025-12-31) [keep: ] quote: "占社会消费品零售总额的比重为26.1%"
  - p126 China total retail sales of consumer goods, December 2025, year-on-year growth = **0.9** % (2025-12-01..2025-12-31) [keep: ] quote: "12月份,社会消费品零售总额同比增长0.9%,环比下降0.12%"
  - p127 China total retail sales of consumer goods, December 2025, month-on-month change = **0.12** % (2025-12-01..2025-12-31) [keep: ] quote: "12月份,社会消费品零售总额同比增长0.9%,环比下降0.12%"
  - p128 China services retail sales, 2025 annual, year-on-year growth = **5.5** % (2025-01-01..2025-12-31) [keep: ] quote: "全年服务零售额比上年增长5.5%"
- `https://www.gov.cn/lianbo/bumen/202405/content_6951495.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stats.gov.cn/sj/zxfb/202502/t20250228_1958817.html` -> **snapshot** (snapshot 20260303003936); points raw/verified 14/4
  - p129 China total retail sales of consumer goods, annual yoy growth 2024 = **3.5** percent (2024-01-01..2024-12-31) [keep: 2024 annual growth 3.5% — historical context for trend.] quote: "全年社会消费品零售总额[38]483345亿元,比上年增长3.5%。"
  - p130 Physical goods online retail sales as share of total retail sales, annual 2024 = **26.5** percent (2024-01-01..2024-12-31) [keep: 2024 online share 26.5% — context.] quote: "全年实物商品网上零售额[40]127878亿元,比上年增长6.5%,占社会消费品零售总额比重为26.5%。"
  - p131 China service retail sales yoy growth, annual 2024 = **6.2** percent (2024-01-01..2024-12-31) [keep: 2024 services retail growth — context.] quote: "服务零售额[39]比上年增长6.2%。"
  - p132 China final consumption expenditure contribution to GDP growth, annual 2024 = **2.2** percentage points (2024-01-01..2024-12-31) [keep: Consumption contribution to GDP — context.] quote: "最终消费支出拉动国内生产总值增长2.2个百分点,"
- dropped by code checks: 10 (number: value_as_written is only part of a larger CJK number in the quote: 10)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['china retail sales', 'china consumption', 'april retail sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p5', 'p6', 'p20', 'p21', 'p35', 'p48', 'p49'] All are the same NBS March 2026 single-month total (41616亿元) and its 1.7% y/y growth, repeated across snapshots. They are one underlying measurement, not independent confirmation.
- corroborating: ['p3', 'p9', 'p10', 'p24', 'p25', 'p37', 'p52', 'p53'] Same NBS Q1 2026 cumulative total (127695亿元) and 2.4% y/y growth, repeated. One measurement.
- corroborating: ['p2', 'p7', 'p8', 'p22', 'p23', 'p36', 'p50', 'p51'] Same NBS March 2026 ex-auto figure (37875亿元, +3.2%), repeated. Implies autos were a drag in March, consistent with total growth (1.7%) below ex-auto growth (3.2%).
- corroborating: ['p11', 'p12', 'p26', 'p27', 'p54', 'p55'] Same NBS Q1 2026 ex-auto cumulative (117727亿元, +3.6%), repeated.
- corroborating: ['p15', 'p16', 'p28', 'p29', 'p30', 'p31', 'p56', 'p57', 'p58', 'p59'] March 2026 goods (37257亿元, +1.5%) and catering (4359亿元, +2.9%) split; sums to the March total. Same NBS release.
- corroborating: ['p17', 'p18', 'p32', 'p33', 'p60', 'p61', 'p62'] Q1 2026 goods (113072亿元, +2.2%) and catering (14623亿元, +4.2%) cumulative; sums to Q1 total. Same release.
- corroborating: ['p4', 'p19', 'p34', 'p39'] Online goods share 24.8% of Q1 2026 total, repeated; consistent with 31614/127695.
- corroborating: ['p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74'] CPCA first-week April 2026 signals: passenger vehicle retail down ~29% y/y, NEV down 24%, NEV penetration 57.7%. These are early-month, partial-period signals for the auto component only; they conflic
- corroborating: ['p75', 'p76', 'p77'] MOFCOM Q1 2026 trade-in applications (1.408m total = 0.403m scrappage + 1.005m replacement). Context for auto subsidy support fading versus 2025's 11.5m full-year pace (p40).
- corroborating: ['p40', 'p41'] 2025 full-year auto trade-in volume (11.5m vehicles) and value (1.6万亿元). Shows the 2025 base was heavily subsidy-supported, implying a harder April 2026 y/y comparison for autos.
- corroborating: ['p78', 'p79', 'p84', 'p85'] Annual totals and online shares for 2024/2025; consistent growth deceleration (3.5%→3.7%) and online share drift (26.8%→26.1%).
- corroborating: ['p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101'] April 2025 NBS release: single-month total 37174亿元 (+5.1%), ex-auto 33548亿元 (+5.6%), goods 33007, catering 4167, urban 32376, rural 4798, online 47419. Internally consistent; provides the April 2025 b
- corroborating: ['p80', 'p81'] Seasonally adjusted m/m growth for April 2025 (+0.26%) and Dec 2025 (-0.12%); context for seasonal shape, not a direct April 2026 level.
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46', 'p47'] Consensus forecasts for March/Q1 2026 activity; retail forecast ~2.5% for March (actual 1.7% came in below), GDP 4.7-4.8%. Useful as a soft prior on the growth regime, not a direct April 2026 retail f
- corroborating: ['p82', 'p83'] Above-designated-size retail (2025 full year 201618亿元; Dec 19547亿元, -1.9%). Shows large-unit weakness late 2025; context only.
- corroborating: ['p86'] Dec 2024 total 45172亿元 (+3.7%); annual context.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p87', 'p102', 'p103'] Same April 2025 single-month total (37174亿元) and 5.1% y/y from two outlets; identical underlying NBS release, so one measurement, not independent confirmation. p87 is the base level for all yoy routes
- corroborating: ['p88', 'p105'] Jan-Apr 2025 cumulative 161845亿元, 4.7% — duplicate of same NBS release; consistent with p87 (April = cumulative minus Q1).
- corroborating: ['p89', 'p104'] April 2025 ex-auto 33548亿元, 5.6% — duplicate. Implies auto retail ≈ 37174−33548 = 3626亿元, i.e. ~9.8% of total; this is the basis for assumption a4.
- corroborating: ['p95', 'p111', 'p96', 'p112'] April 2025 goods 33007亿元 (+5.1%) and catering 4167亿元 (+5.2%) sum to the total; consistent decomposition, same release.
- corroborating: ['p107', 'p108', 'p91', 'p92'] Urban 32376 + rural 4798 = 37174亿元; consistent split, same release.
- corroborating: ['p78', 'p117', 'p118'] 2025 annual 501202亿元, +3.7% — same NBS release; p78 is the annual growth signal used in m1.
- corroborating: ['p66', 'p70', 'p71'] CPCA early-April 2026: PV daily retail −29% y/y, NEV retail −24% y/y, NEV penetration 57.7%. Consistent picture of a sharp auto contraction in the first week; only a partial-month signal, not the full
- corroborating: ['p75'] Trade-in subsidy applications 1.408m in Q1 2026 — shows the 2025 trade-in boost is fading/being absorbed; supports weaker 2026 auto growth than 2025.
- corroborating: ['p40', 'p41'] 2025 auto trade-in 11.5m vehicles / 1.6万亿元 — context for the 2025 base being subsidy-inflated, hence a negative base effect for April 2026 autos.
- corroborating: ['p79', 'p125', 'p124'] Online physical goods share 26.1% of 2025 total; consistent across releases. Context only.
- corroborating: ['p126', 'p127'] December 2025 total +0.9% y/y, −0.12% m/m — shows late-2025 momentum was very weak, a downside anchor for early-2026 growth.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | April 2026 y/y growth of total retail sales | 1.8 | 0.2..4.5 | 0.2..4.5 | % | m2 (m3) | Late-2025 momentum was very weak (Dec +0.9% y/y, p126) and the 2025 trade-in boost is fading (p75 shows only 1.4m applications in Q1 2026 vs 11.5m for all 2025, p40). Early-April CPCA shows autos −29% y/y (p66), a large drag. Ex-auto trend likely ~2-3%; with autos ~10% of total at −8% to −15%, total | April 2026 is a normal 30-day month with no major policy shock beyond the fading trade-in program. | A new large stimulus announced in April 2026, or CPCA full-month auto retail recovering to positive y/y. |
| a2 | April 2026 y/y growth of ex-auto retail | 3 | 1.5..4.5 | 1.5..4.5 | % | m1 (m2) | Ex-auto retail grew 5.6% in April 2025 (p89) but late-2025 momentum weakened sharply (Dec total +0.9%, p126). Ex-auto has been the resilient component; ~3% is a moderate continuation, below the 2025 pace. | Ex-auto categories (food, apparel, home appliances, catering) continue near their recent trend. | Evidence of a sharp ex-auto slowdown (e.g. weak catering or appliance data) in April 2026. |
| a3 | April 2026 y/y decline of auto retail (magnitude) | 10 | 1..22 | 1..22 | % | m1 (m2) | CPCA first-week April 2026 PV retail −29% y/y (p66); the 2025 base was subsidy-inflated (p40) and 2026 trade-in applications are far lower (p75). Full-month auto retail likely declines but less than the first-week −29% as the base normalizes; ~10% central with wide range. Expressed as a positive mag | CPCA first-week weakness persists through the month but moderates. | CPCA weeks 2-4 showing auto retail recovering to flat or positive y/y. |
| a4 | Auto share of April 2025 total retail sales | 9.8 | 8.5..11 | 6.837..13.67 (widened) | % | m1 (m2) | Derived from p87 (37174) minus p89 (33548) = 3626亿元 auto retail, i.e. 9.75% of total. Range reflects definitional uncertainty in the 'ex-auto' residual. | Auto share of total retail is stable between April 2025 and April 2026. | NBS reporting a materially different auto share for April 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,780,702,198,374 | ['p87'] / ['a2', 'a3', 'a4'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 3,787,168,173,407 | ['p87'] / ['a1'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p87 * (a4 * (1 - a3) + (1 - a4) * (1 + a2)); Monte Carlo P10 to P90 3,145,049,969,218 to 4,536,550,383,953; result unit CNY converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p87 * (1 + a1); Monte Carlo P10 to P90 3,149,852,467,215 to 4,560,552,587,580; result unit CNY converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 3,780,702,198,374 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 3,787,168,173,407 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.00 (not above one, so no widening); final width x/÷1.38.

Result: central **3,783,933,804,761** CNY, 80% interval [2,746,634,286,242, 5,212,981,979,631] CNY, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for China's total retail sales of consumer goods, single month of April 2026 (first-reported NBS value): 3,783,933,804,761 CNY (80% model-based interval 2,746,634,286,242 to 5,212,981,979,631 CNY).

Observed anchor: April 2025 single-month total was 3,717,400,000,000 CNY. The two routes scale this base: one applies an aggregate y/y growth of 1.8% (range 0.2% to 4.5%); the other splits auto and ex-auto, using ex-auto growth 3% (1.5% to 4.5%), auto decline 10% (1% to 22%), and auto share 9.8% (6.837% to 13.67%). Only the 2025 base is observed; all 2026 growth inputs are analyst assumptions, informed by weak late-2025 momentum, fading trade-in effects, and early-April auto weakness. Code combined the two overlapping routes as equal-weight blocks (50% and 50%), not from backtest evidence. Main risk: an unanticipated stimulus or a sharper auto collapse. Better early-April and full-month auto data plus trade-in application counts would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 April 2026 y/y growth of total retail sales: 1.8%, range 0.2% to 4.5%; used by m2. Overturned by: A new large stimulus announced in April 2026, or CPCA full-month auto retail recovering to positive y/y.
- a2 April 2026 y/y growth of ex-auto retail: 3%, range 1.5% to 4.5%; used by m1. Overturned by: Evidence of a sharp ex-auto slowdown (e.g. weak catering or appliance data) in April 2026.
- a3 April 2026 y/y decline of auto retail (magnitude): 10%, range 1% to 22%; used by m1. Overturned by: CPCA weeks [n]-[n] showing auto retail recovering to flat or positive y/y.
- a4 Auto share of April 2025 total retail sales: 9.8%, range 6.837% to 13.67% (range widened by code); used by m1. Overturned by: NBS reporting a materially different auto share for April 2026.

Method details (computed by code):
- m1 formula_mc: p87 * (a4 * (1 - a3) + (1 - a4) * (1 + a2)); Monte Carlo P10 to P90 3,145,049,969,218 to 4,536,550,383,953; result unit CNY converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p87 * (1 + a1); Monte Carlo P10 to P90 3,149,852,467,215 to 4,560,552,587,580; result unit CNY converted to CNY; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 3,780,702,198,374 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 3,787,168,173,407 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.00 (not above one, so no widening); final width x/÷1.38.

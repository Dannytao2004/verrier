# Evidence ledger: fc_cn_retail_2026_04

- Question: Assume today is 2026-04-18. You know nothing published after this date. Estimate China's total retail sales of consumer goods (社会消费品零售总额) for the single month of April 2026 (not the January-April cumulative total), in Chinese yuan (CNY; the release states it in 亿元, i.e. units of 100 million yuan), as it will be first reported in the National Bureau of Statistics of China's monthly release on retail sales of consumer goods.
- as_of: 2026-04-18
- Pinned target: Single-month total retail sales of consumer goods (社会消费品零售总额) in mainland China, covering retail sales of goods and catering services to consumers, as first reported by NBS for April 2026; excludes services retail sales outside goods/catering and excludes Hong Kong, Macao, and Taiwan. | unit 100 million CNY (亿元) | period 2026-04-01..2026-04-30 | publisher National Bureau of Statistics of China (NBS)

- Official value (scoring only, never shown to the agent): 3,724,700,000,000

## Directions and pages

### d1 [own_history] NBS monthly statistical releases and historical time series

Hypothesis: April 2026 retail sales can be bridged from recent NBS monthly history using April/March seasonal ratios or April-vs-Q1 patterns; recent 2026 momentum (January-February and March, if released by cutoff) constrains the year-on-year growth rate applied to the April 2025 level.

Queries issued by the searcher: 国家统计局 社会消费品零售总额 2026年3月; 社会消费品零售总额 2026年一季度 同比增长; 2025年4月份社会消费品零售总额 37174亿元 增长5.1% 国家统计局; 2026年1-2月份社会消费品零售总额 同比增长 国家统计局

- `https://www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416125004); points raw/verified 15/2
  - p1 March 2026 total retail sales year-on-year growth rate = **1.7** % (2026-03-01..2026-03-31) [DISCARD: Redundant duplicate of the March 2026 growth already contained in p3; p3 also supplies the March level.] quote: "2026年3月份社会消费品零售总额增长1.7%"
  - p2 Q1 2026 total retail sales year-on-year growth rate = **2.4** % (2026-01-01..2026-03-31) [keep: ] quote: "1-3月份,社会消费品零售总额127695亿元,同比增长2.4%。"
- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.cnr.cn/native/gd/kx/20260416/t20260416_527586744.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://big5.www.gov.cn/gate/big5/www.gov.cn/lianbo/202604/content_7065903.htm` -> **snapshot** (snapshot 20260416152146); points raw/verified 15/3
  - p3 March 2026 total retail sales year-on-year growth rate = **1.7** % (2026-03-01..2026-03-31) [keep: ] quote: "3月份,社會消費品零售總額41616億元,同比增長1.7%。"
  - p4 Q1 2026 total retail sales year-on-year growth rate = **2.4** % (2026-01-01..2026-03-31) [DISCARD: Redundant duplicate of the Q1 2026 growth already contained in p2; p2 also supplies the Q1 level.] quote: "1-3月份,社會消費品零售總額127695億元,同比增長2.4%。"
  - p5 Q1 2026 online goods retail sales share of total retail sales = **24.8** % (2026-01-01..2026-03-31) [keep: ] quote: "網上商品零售額31614億元,增長7.5%,佔社會消費品零售總額的比重為24.8%;"
- dropped by code checks: 25 (number: value_as_written is only part of a larger CJK number in the quote: 24; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d2 [related_series] NBS consumption category tables and industry associations

Hypothesis: Total retail sales is the sum of goods retail and catering; within goods, auto, petroleum, food, apparel, home appliances, and online physical goods have large weights. Forecasting large components separately plus a residual can reduce error, especially if early-April auto and appliance signals reveal deviations from the March trend.

Queries issued by the searcher: 乘联会 2026年4月 零售 销量 周度; 国家统计局 2026年3月 社会消费品零售总额 汽车 石油; 2025年4月份社会消费品零售总额 汽车类 石油及制品类 家用电器 餐饮收入 亿元 国家统计局; 2025年4月 社零 商品零售 餐饮收入 汽车类 服装鞋帽 网上商品零售额 数据表

- `https://www.stats.gov.cn//xxgk/sjfb/zxfb2020/202604/t20260416_1963325.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://field.10jqka.com.cn/20260415/c676015302.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.eastmoney.com/a/202505193408630152.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [physical_flow] E-commerce platforms, express logistics operators, and State Post Bureau

Hypothesis: Online physical goods retail is a large and timely component of total retail sales; express parcel volume and e-commerce promotion intensity can proxy its April momentum. Total retail can be approximated as online physical goods retail divided by a seasonal online share.

Queries issued by the searcher: 国家邮政局 2026年3月 快递业务量; 全国网上零售额 实物商品 2026年一季度; 2025年1-4月 全国网上零售额 实物商品网上零售额 亿元 国家统计局; 2025年4月 社会消费品零售总额 37174亿元 网上零售

- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stock.finance.sina.com.cn/stock/view/paper.php?symbol=sh000001&reportid=829755844571&autocallup=no&isfromsina=no` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.scio.gov.cn/live/2026/38333/tw/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.chinawuliu.com.cn/zixun/202604/16/665543.shtml` -> **snapshot** (snapshot 20260416024106); points raw/verified 14/14
  - p6 China express delivery business volume, March 2026, estimated (预计在...左右) = **17,300,000,000** parcels (2026-03-01..2026-03-31) [keep: ] quote: "3月快递业务量预计在173亿件左右,快递业务收入预计同比增长4%"
  - p7 China express delivery business revenue, March 2026, estimated year-on-year grow = **4** % (2026-03-01..2026-03-31) [DISCARD: March express revenue growth is not directly linked to NBS retail and is not needed given the kept volume measures.] quote: "3月快递业务量预计在173亿件左右,快递业务收入预计同比增长4%"
  - p8 China express delivery business volume, Q1 2026, estimated year-on-year growth = **6** % (2026-01-01..2026-03-31) [keep: ] quote: "一季度,快递业务量预计同比增长6%,快递业务收入预计同比增长6.5%"
  - p9 China express delivery business revenue, Q1 2026, estimated year-on-year growth = **6.5** % (2026-01-01..2026-03-31) [DISCARD: Q1 express revenue growth is redundant with kept express volume growth and is not linked to April retail.] quote: "一季度,快递业务量预计同比增长6%,快递业务收入预计同比增长6.5%"
  - p10 China express delivery average daily business volume, March 2026 = **550,000,000** parcels per day (2026-03-01..2026-03-31) [DISCARD: Derived from p6's March volume; adds no independent information.] quote: "3月,快递业务规模与业务收入均平稳增长,日均业务量超5.5亿件"
  - p11 China express delivery development index, March 2026 = **411** index points (2026-03-01..2026-03-31) [DISCARD: March express development index summary is not April-specific and is not directly linked to NBS retail sales.] quote: "经测算,2026年3月中国快递发展指数为410.9,同比提升2.4%"
  - p12 China express delivery development index, March 2026, year-on-year change = **2.4** % (2026-03-01..2026-03-31) [DISCARD: Growth rate of the same express development index; redundant with p11 and not April-specific.] quote: "经测算,2026年3月中国快递发展指数为410.9,同比提升2.4%"
  - p13 China express delivery development scale index, March 2026 = **608** index points (2026-03-01..2026-03-31) [DISCARD: Express scale subindex is March-only and less directly relevant than kept volume measures.] quote: "其中发展规模指数为608.2,同比提升5.1%"
  - p14 China express delivery development scale index, March 2026, year-on-year change = **5.1** % (2026-03-01..2026-03-31) [DISCARD: Growth rate of p13; redundant and not April-specific.] quote: "3月,发展规模指数为608.2,同比提升5.1%"
  - p15 China express delivery service quality index, March 2026 = **504** index points (2026-03-01..2026-03-31) [DISCARD: Express service-quality subindex is not a retail-sales indicator.] quote: "服务质量指数为503.9,与去年同期基本持平"
  - p16 China express delivery development capability index, March 2026 = **237** index points (2026-03-01..2026-03-31) [DISCARD: Express development-capability subindex is not a retail-sales indicator.] quote: "发展能力指数为237.4,同比提升3.2%"
  - p17 China express delivery development trend index, March 2026 = **60** index points (2026-03-01..2026-03-31) [DISCARD: Express trend index is a March-only logistics indicator, not an April retail input.] quote: "3月,发展趋势指数为60"
  - p18 China express delivery public satisfaction score, March 2026, estimated = **84.9** points (satisfaction score) (2026-03-01..2026-03-31) [DISCARD: Express satisfaction score is unrelated to total retail sales levels.] quote: "快递服务公众满意度预计为84.9分,同比提升0.2分"
  - p19 China key regions 72-hour on-time delivery rate, March 2026, estimated = **85.3** % (2026-03-01..2026-03-31) [DISCARD: On-time delivery rate is unrelated to total retail sales levels.] quote: "重点地区72小时妥投率预计为85.3%"

### d4 [shocks] Policy announcements and early-month sales indicators

Hypothesis: Consumer goods trade-in subsidies, auto purchase incentives, and local consumption vouchers in 2026 alter April year-on-year growth; measuring announced subsidy scale and early-April redemption can adjust a base forecast derived from history.

Queries issued by the searcher: 2026 消费品以旧换新 资金 政策 4月 国家发改委; 汽车以旧换新 2026 一季度 数据 补贴; 2026年一季度 社会消费品零售总额 同比 国家统计局 4月16日; 2026年 消费品以旧换新 超长期特别国债 资金 第一批 全年 规模 亿元

- `https://www.gov.cn/lianbo/202604/content_7065162.htm` -> **snapshot** (snapshot 20260412165040); points raw/verified 5/5
  - p20 Second batch of ultra-long special treasury bond funds allocated in 2026 to supp = **62,500,000,000** CNY (2026-01-01..2026-04-10) [keep: ] quote: "及时向地方下达了今年第二批625亿元超长期特别国债资金,支持地方继续平稳有序实施消费品以旧换新政策。"
  - p21 Cumulative nationwide consumer goods trade-in sales in 2026 year-to-date = **433,200,000,000** CNY (2026-01-01..2026-04-10) [keep: ] quote: "今年以来,全国消费品以旧换新销售额超过4332亿元"
  - p22 Cumulative beneficiaries (person-times) of consumer goods trade-in in 2026 year- = **60,930,000** person-times (2026-01-01..2026-04-10) [DISCARD: Beneficiary count is a redundant administrative detail of the same trade-in announcement and is not used to size retail ] quote: "惠及超过6093万人次"
  - p23 Year-on-year growth of total retail sales of consumer goods, January-February 20 = **2.8** % (2026-01-01..2026-02-28) [keep: ] quote: "带动1至2月社会消费品零售总额同比增长2.8%"
  - p24 Acceleration of Jan-Feb 2026 retail sales growth versus December 2025 (percentag = **1.9** percentage points (2026-01-01..2026-02-28) [DISCARD: Acceleration versus December 2025 is contextual but not directly useful for the April 2026 single-month forecast.] quote: "比上年12月份加快1.9个百分点"
- `http://big5.www.gov.cn/gate/big5/www.gov.cn/lianbo/202604/content_7064663.htm` -> **snapshot** (snapshot 20260416153816); points raw/verified 14/0
- `https://news.cnr.cn/native/gd/kx/20260416/t20260416_527586744.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.sina.com.cn/wm/2026-04-04/doc-inhtichc3062376.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (number: value_as_written is only part of a larger CJK number in the quote: 14)

### d5 [administrative] State Taxation Administration, Ministry of Commerce, and holiday consumption releases

Hypothesis: VAT invoice retail sales revenue and Ministry of Commerce key retail enterprise sales are independent administrative traces of consumption activity; their Q1 2026 growth and Qingming holiday consumption data can validate or adjust an NBS-based April forecast, especially as partial-month signals.

Queries issued by the searcher: 税务总局 增值税发票 零售 2026年一季度 销售收入; 2026年清明 消费 数据 零售 商务部; 税务总局 增值税发票数据 2026年一季度 消费品 零售 销售收入 同比增长; 国家统计局 2026年一季度 社会消费品零售总额 同比增长 3月份

- `https://mrdx.cn/h5/mrdx/content/20260407/Articel01006NR.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.cctv.com/2026/04/07/ARTIYePaRsp25N7mDZK2rFEC260407.shtml` -> **snapshot** (snapshot 20260407071117); points raw/verified 0/0
- `http://yule.qlwb.com.cn/detail/25931815.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://guoyanwang.clcn.net.cn/webui/DocSummary.aspx?docid=8186840&leafid=14099` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Analyst consensus and research institutes

Hypothesis: Published forecasts for China March 2026 retail sales, Q1 2026 consumption, and Q2/2026 retail sales growth can anchor April growth expectations; April-specific forecasts may not exist, so these are mainly sanity checks on the historical and component routes.

Queries issued by the searcher: China March 2026 retail sales forecast consensus; 中国 2026年3月 社会消费品零售总额 预测 同比; 2026年 社会消费品零售总额 全年增速 预测 机构 展望; China April 2026 retail sales forecast analyst poll Reuters

- `https://cmegroup.econoday.com/byevent?fid=679968&year=2026&ctyall=10737566&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.aastock.com/sc/stocks/analysis/china-hot-topic-content.aspx?id=NOW.1518049&catg=4&source=AAFN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://vip.stock.finance.sina.com.cn/q/go.php/vReport_Show/kind/lastest/rptid/828782520181/index.phtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://guoyanwang.clcn.net.cn/webui/DocSummary.aspx?docid=8155690&leafid=26601` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Historical NBS monthly total retail sales levels

Hypothesis: The forecast currently relies on assumed seasonal ratios because no kept point gives April 2025 single-month retail or 2025 Q1 total. Retrieving 2024-2025 monthly NBS total retail levels would replace assumptions a1/a2 with measured April/March and April/Q1 ratios and permit a backtested seasonal bridge.

Queries issued by the searcher: 2025年4月 社会消费品零售总额 37174亿元 国家统计局; 国家统计局 2025年4月份社会消费品零售总额增长 同比增长; 2025年3月份社会消费品零售总额 40330亿元 1—3月份 124671亿元 国家统计局; 2024年4月份社会消费品零售总额 35699亿元 3月份 39020亿元 国家统计局

- `https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202505/t20250519_1959858.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stats.gov.cn/zwfwck/sjfb/202504/t20250416_1959317.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.stats.gov.cn/easyquery.htm?cn=A01` -> **snapshot** (snapshot 20260310162942); points raw/verified 0/0
- `http://big5.www.gov.cn/gate/big5/www.gov.cn/lianbo/bumen/202505/content_7024220.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Early-April 2026 high-frequency consumption signals

Hypothesis: April-specific auto, appliance/trade-in, and e-commerce parcel data would allow adjustment of the assumed April/March and April/Q1 seasonal ratios for 2026 momentum, especially after March growth of 1.7% versus Q1 growth of 2.4%.

Queries issued by the searcher: 乘联分会 2026年4月1-15日 乘用车零售 销量; 2026年4月 全国快递业务量 日均 亿件 国家邮政局; 以旧换新 2026年4月 汽车报废更新 补贴 申请 数量 商务部; 国家邮政局 2026年4月中国快递发展指数 443.2 日均快递业务量 5.5亿件

- `http://field.10jqka.com.cn/20260415/c676015302.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nmg.gov.cn/zwyw/qgyw/202604/t20260416_2890346.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://app.lanjinger.com/t/973896` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://wdatacn.aastocks.com/sc/(Z(@@78XMF=@@sPxRU%7B%7B%7Bthis9377701%7D%7D%7Dxca` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] Trade-in subsidy intensity and timing

Hypothesis: p21 cumulative trade-in sales and p20's second batch allocation may indicate an April subsidy boost, but without comparable 2025 trade-in sales and redemption timing they cannot be converted into an incremental April retail adjustment over the seasonal baseline.

Queries issued by the searcher: 2025年消费品以旧换新累计销售额 4月中旬 商务部; 以旧换新 拉动社会消费品零售总额 增速 个百分点 2025 商务部 数据; 2026年 消费品以旧换新 第二批 资金 下达 超长期特别国债 亿元 4月; 2025年4月 社会消费品零售总额 同比增长5.1% 以旧换新 拉动 增速 百分点

- `http://finance.people.com.cn/BIG5/n1/2025/0426/c1004-40468546.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://bgimg.ce.cn/cysc/newmain/yc/jsxw/202601/t20260102_2679232.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://paper.people.com.cn/rmrb/pc/content/202604/11/content_30150415.html` -> **snapshot** (snapshot 20260414232159); points raw/verified 5/5
  - p25 Cumulative nationwide trade-in sales of consumer goods, year-to-date (as of repo = **433,200,000,000** CNY (2026-01-01..2026-04-10) [DISCARD: Duplicate of p21: same 4332亿元 cumulative trade-in sales, same 2026-01-01..2026-04-10 period, and same underlying People'] quote: "今年以来,全国消费品以旧换新销售额超过4332亿元"
  - p26 Cumulative beneficiaries (person-times) of trade-in program, year-to-date (as of = **60,930,000** person-times (2026-01-01..2026-04-10) [keep: ] quote: "惠及超过6093万人次"
  - p27 Year-on-year growth of total retail sales of consumer goods, January-February 20 = **2.8** % (2026-01-01..2026-02-28) [DISCARD: Duplicate of p23: same 2.8% Jan-Feb 2026 retail growth and same policy-report context; p23 is the retained copy.] quote: "带动1至2月社会消费品零售总额同比增长2.8%"
  - p28 Acceleration of Jan-Feb 2026 retail sales growth versus December 2025 (percentag = **1.9** percentage points (2026-01-01..2026-02-28) [keep: ] quote: "比上年12月份加快1.9个百分点"
  - p29 Second batch of ultra-long special treasury bond funds allocated to localities f = **62,500,000,000** CNY (2026-04-01..2026-04-10) [DISCARD: Duplicate of p20: same 625亿元 second-batch ultra-long special treasury bond allocation; p20 is the retained copy.] quote: "及时向地方下达了今年第二批625亿元超长期特别国债资金"
- `https://finance.people.com.cn/BIG5/n1/2025/0426/c1004-40468546.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['china retail sales', 'china consumption', 'april retail sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p3'] Both report March 2026 total retail sales year-on-year growth of 1.7%; p3 additionally gives the March level of 41616亿元. They are the same NBS release in different language versions, so agreement is n
- corroborating: ['p2', 'p4'] Both report Q1 2026 total retail sales year-on-year growth of 2.4%; p2 gives the cumulative Q1 level of 127695亿元. They are duplicate language versions of the same NBS release, not independent measurem
- corroborating: ['p2', 'p3', 'p23'] Q1 level p2 minus March level p3 implies Jan-Feb level of 86079亿元; Jan-Feb growth p23 of 2.8% is arithmetically consistent with Q1 growth 2.4% and March growth 1.7% given the relative month sizes. Thi
- corroborating: ['p5', 'p2'] p5 states Q1 2026 online goods retail of 31614亿元 and a 24.8% share of total retail; dividing implies total retail close to p2's 127695亿元. Same release, so useful as a scope/share check, not as indepen
- corroborating: ['p6', 'p8', 'p10'] p6 gives March express volume near 173亿 parcels, p10 states daily average over 5.5亿 (consistent with 31 days), and p8 gives Q1 express volume growth near 6%. They share the same logistics-association 
- corroborating: ['p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19'] These are March 2026 express development indices and subindices from the same source. Several are index levels and their growth rates, so they overlap mechanically. They are March-only, logistics-sect
- corroborating: ['p20', 'p21', 'p22'] All three come from the same 2026-04-10 policy announcement: second batch of 625亿元 ultra-long special treasury bonds, cumulative trade-in sales over 4332亿元, and over 6093万人次 beneficiaries. p20 is fund
- corroborating: ['p23', 'p24'] Both come from the same trade-in policy article: Jan-Feb 2026 retail growth 2.8% and acceleration of 1.9 percentage points versus December 2025. p23 is useful as a consistency check on Q1/March growth
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p2', 'p3', 'p23', 'p28'] All are NBS total-retail growth rates for overlapping 2026 periods: Q1 2.4%, March 1.7%, Jan-Feb 2.8%. p28 says Jan-Feb accelerated 1.9 pp versus December 2025, consistent with a weak December base. T
- corroborating: ['p21', 'p25', 'p26', 'p20', 'p29'] These describe the same 2026 consumer-goods trade-in program. p21 and p25 are duplicate 4332亿元 YTD trade-in sales through 2026-04-10; p20 and p29 are duplicate 625亿元 second-batch funding allocations; 
- corroborating: ['p5', 'p6', 'p8'] p5 gives the Q1 2026 NBS online-goods share of total retail (24.8%); p6 gives estimated March express parcel volume (17.3 billion parcels); p8 gives estimated Q1 express volume growth (6%). They point
- conflicting: ['p3', 'p2'] This is a timing/speed conflict rather than a definitional one: March 2026 growth at 1.7% is materially below Q1 2026 growth at 2.4%, so momentum weakened into March. Any April forecast must allow for

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | April 2026 express parcel volume divided by March 2026 express parcel volume | 0.94 | 0.88..1 | 0.6633..1.327 (widened) | ratio | m1 (m1) | March has 31 days and April 30, and April normally lacks a major e-commerce festival while still having Qingming and spring demand. March 2026 parcel volume was estimated at 17.3 billion; a ratio slightly below 1 is more plausible than a large increase. The range allows flat April volume or a modest | Used in m1 to project April 2026 parcels from p6 March 2026 estimated parcels; it should not be used if April contains an unusual promotion or a parcel-data disruption. | Published April express parcel volume implying an April/March ratio outside roughly 0.88-1.00. |
| a2 | Online physical goods retail sales per express parcel, April 2026 | 66 | 58..75 | 46.64..93.27 (widened) | CNY/parcel | m1 (m1) | A large share of express volume is online physical-goods delivery. The p5 quote implies Q1 2026 online goods retail of 31614亿元, and p6/p8 imply Q1 parcel volume near the high-40-billion range, giving an average near 60-70 CNY per parcel. I use 66 CNY/parcel as a central conversion, with a range for  | Used in m1 to convert total express parcels into online physical-goods retail value; it assumes the average online-goods value per parcel remains near the Q1/historical range and that returns/non-online parcels are broadly stable in the average. | Evidence that April online physical-goods value per express parcel fell below 58 or rose above 75 CNY, for example from a large shift in parcel mix or promotional discounting. |
| a3 | April 2026 online goods share relative to Q1 2026 online goods share | 1.1 | 1.04..1.16 | 0.7767..1.553 (widened) | ratio | m1 (m1) | p5 gives a Q1 2026 online-goods share of 24.8%. April online share is usually higher than the Q1 average because Q1 includes the Jan-Feb holiday period with more offline spending. A modest upward adjustment of about 10% is consistent with historical April-versus-Q1 patterns; the range keeps the shar | Used in m1 to adjust p5 Q1 online share to an April share; if April online share were exactly the Q1 share, this ratio would be 1.0. | April online-goods share below about 25.8% or above about 28.8%, or direct evidence that April online share moved very differently from the Q1 share. |
| a4 | April 2026 full-month trade-in sales divided by cumulative trade-in sales Jan 1-Apr 10 2026 | 0.3 | 0.25..0.36 | 0.2121..0.4243 (widened) | ratio | m2 (m2) | p21 covers Jan 1-Apr 10, about 100 days, while April has 30 days. Constant daily trade-in sales would give roughly 30/100 = 0.30 of p21 as the April full-month amount. The second batch of 625亿元 was allocated around Apr 10 (p20), which could lift late-April redemption, so the high end is above the co | Used in m2 to convert p21 cumulative trade-in sales through Apr 10 into an April full-month trade-in sales estimate; it assumes the daily trade-in pace does not shift drastically after Apr 10. | Evidence that April trade-in sales were far below 25% or far above 36% of the Jan 1-Apr 10 cumulative total, such as a sudden program suspension or a large late-April surge. |
| a5 | Consumer goods trade-in sales share of total retail sales in April 2026 | 3.3 | 2.8..3.9 | 2.337..4.673 (widened) | % | m2 (m2) | p21 reports 4332亿元 of trade-in sales through Apr 10. Relative to China's monthly total retail scale, this is a small component, roughly low-3% of total retail sales. Trade-in sales are included in goods retail but do not cover all retail, so the share should be treated as a conversion ratio, not as  | Used in m2 to scale trade-in sales up to total retail sales; it assumes the April trade-in sales share is near the early-2026 ratio and that trade-in sales remain within NBS goods retail coverage. | Evidence that trade-in sales were below 2.8% or above 3.9% of April total retail sales, or that a large part of trade-in sales fell outside the NBS retail definition. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 39,008 | ['p6', 'p5'] / ['a1', 'a2', 'a3'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 39,176 | ['p21'] / ['a4', 'a5'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p6 * a1 * a2 / (p5 * a3); Monte Carlo P10 to P90 20,360 to 75,929; result unit CNY converted to CNY*10**8; own 80% width x/÷1.93 (Monte Carlo of the formula inputs)
- m2 formula_mc: p21 * a4 / a5; Monte Carlo P10 to P90 23,356 to 66,487; result unit CNY converted to CNY*10**8; own 80% width x/÷1.69 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 39,008 (width x/÷1.93, Monte Carlo of the formula inputs); B2 = m2: 39,176 (width x/÷1.69, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.81; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.81.

Result: central **39,092** CNY*10**8, 80% interval [21,574, 70,836] CNY*10**8, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The estimate for mainland China's single-month total retail sales of consumer goods (goods retail plus catering) in April 2026 is 39,092 CNY*10**8 (80% model-based interval 21,574 to 70,836 CNY*10**8).

Two routes were combined with equal weight per block. m1 (39,008 CNY*10**8, weight 50%) divides online physical-goods retail by the online share: March parcels 17,300,000,000 parcels times an April ratio 0.94 and per-parcel value 66, divided by the Q1 online share 24.8% adjusted by 1.1. m2 (39,176 CNY*10**8, weight 50%) scales cumulative trade-in sales 433,200,000,000 CNY by an April fraction 0.3 and a trade-in share 3.3%.

Only the parcel level, online share, and trade-in total are observed; the transfers (0.94, 66, 1.1, 0.3, 3.3%) are analyst assumptions. The interval is conditional on these. The biggest risk is the parcel-to-CNY and trade-in-share conversions. Better evidence would be actual April parcel volumes and monthly online-retail data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 April 2026 express parcel volume divided by March 2026 express parcel volume: 0.94 ratio, range 0.6633 to 1.327 (range widened by code); used by m1. Overturned by: Published April express parcel volume implying an April/March ratio outside roughly [n]-[n].
- a2 Online physical goods retail sales per express parcel, April 2026: 66 CNY/parcel, range 46.64 to 93.27 (range widened by code); used by m1. Overturned by: Evidence that April online physical-goods value per express parcel fell below [n] or rose above [n] CNY, for example from a large shift in parcel mix or promotional discounting.
- a3 April 2026 online goods share relative to Q1 2026 online goods share: 1.1 ratio, range 0.7767 to 1.553 (range widened by code); used by m1. Overturned by: April online-goods share below about [n] or above about [n], or direct evidence that April online share moved very differently from the Q1 share.
- a4 April 2026 full-month trade-in sales divided by cumulative trade-in sales Jan [n]-Apr [n] 2026: 0.3 ratio, range 0.2121 to 0.4243 (range widened by code); used by m2. Overturned by: Evidence that April trade-in sales were far below [n] or far above [n] of the Jan [n]-Apr [n] cumulative total, such as a sudden program suspension or a large late-April surge.
- a5 Consumer goods trade-in sales share of total retail sales in April 2026: 3.3%, range 2.337% to 4.673% (range widened by code); used by m2. Overturned by: Evidence that trade-in sales were below [n] or above [n] of April total retail sales, or that a large part of trade-in sales fell outside the NBS retail definition.

Method details (computed by code):
- m1 formula_mc: p6 * a1 * a2 / (p5 * a3); Monte Carlo P10 to P90 20,360 to 75,929; result unit CNY converted to CNY*10**8; own 80% width x/÷1.93 (Monte Carlo of the formula inputs)
- m2 formula_mc: p21 * a4 / a5; Monte Carlo P10 to P90 23,356 to 66,487; result unit CNY converted to CNY*10**8; own 80% width x/÷1.69 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 39,008 (width x/÷1.93, Monte Carlo of the formula inputs); B2 = m2: 39,176 (width x/÷1.69, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.81; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.81.

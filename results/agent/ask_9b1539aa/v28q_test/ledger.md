# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types combined, excluding bulk/industrial drums) sold/exported to the United States by Jiangsu Hengshun Group (镇江恒顺集团 / 江苏恒顺醋业股份有限公司) in a full calendar year | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; Hengshun Group / Jiangsu Hengshun Vinegar-Industry Co., Ltd. (SH:600305) annual report and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Hengshun Group / Jiangsu Hengshun Vinegar-Industry Co. (SH:600305) investor disclosures

Hypothesis: Hengshun's annual reports disclose total revenue, vinegar segment revenue, and overseas/export revenue (境外收入 or 出口收入). If export revenue and the US share of exports are known, US bottle count = (export revenue × US share) / (average bottle price). Role: provides the top-line export denominator and any disclosed US/overseas breakdown.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外收入 出口; Jiangsu Hengshun Vinegar annual report export revenue overseas; 恒顺醋业 2024年年度与行业相关的定期经营数据公告 外贸模式 销售收入 4774; 恒顺醋业 年报 境外收入 占比 出口 美国 市场

- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 14/14
  - p1 Hengshun vinegar (醋系列) segment sales revenue, 2024 = **1,265,596,300** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p2 Hengshun vinegar (醋系列) segment sales revenue, 2023 = **1,294,067,600** 万元 RMB (2023-01-01..2023-12-31) [DISCARD: Redundant with p96 (same 2023 vinegar revenue, different rounding); p96 is the more precise annual-report figure.] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p3 Hengshun foreign trade (外贸模式) sales revenue, 2024 = **47,741,300** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p4 Hengshun foreign trade (外贸模式) sales revenue, 2023 = **45,133,900** 万元 RMB (2023-01-01..2023-12-31) [DISCARD: Redundant with p93 (same 2023 foreign-trade revenue); p93 is more precise.] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p5 Hengshun foreign trade (外贸模式) revenue year-on-year change, 2024 vs 2023 = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p6 Hengshun total sales revenue (all channels), 2024 = **2,093,006,800** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p7 Hengshun total sales revenue (all channels), 2023 = **2,077,821,800** 万元 RMB (2023-01-01..2023-12-31) [DISCARD: Redundant with p98/p99 for 2023 total revenue; adds no new information.] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p8 Hengshun product-category total sales revenue (vinegar+wine+sauce), 2024 = **1,774,174,300** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p9 Hengshun product-category total sales revenue (vinegar+wine+sauce), 2023 = **1,816,930,700** 万元 RMB (2023-01-01..2023-12-31) [DISCARD: Redundant with p8 for the category total; 2023 value not needed separately.] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p10 Hengshun vinegar segment revenue year-on-year change, 2024 vs 2023 = **-2.2** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p11 Hengshun direct sales (直销模式) revenue, 2024 = **103,817,200** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 直销模式 \| 10,381.72 \| 10,072.35 \| 3.07 \|"
  - p12 Hengshun dealer (经销模式) revenue, 2024 = **1,941,448,600** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 经销模式 \| 194,144.86 \| 193,196.45 \| 0.49 \|"
  - p13 Hengshun online sales revenue, 2024 = **274,378,100** 万元 RMB (2024-01-01..2024-12-31) [keep: ] quote: "\| 线上销售 \| 27,437.81 \| 26,471.68 \| 3.65 \|"
  - p14 Hengshun total dealer count at end of 2024 = **2,014** dealers (2024-12-31..2024-12-31) [keep: ] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://cfi.cn/p20250422000502.html` -> **dropped** (live page has no readable date); points raw/verified -/-

### d2 [related_series] China customs / UN Comtrade vinegar export statistics

Hypothesis: China's HS 2209 (vinegar and substitutes) exports to the US give total Chinese vinegar export volume/value to the US. Hengshun's share of China's vinegar exports (by value or volume) times total US-bound volume gives Hengshun's US bottle count. Role: provides the total US-bound flow; Hengshun share is the bridge.

Queries issued by the searcher: 中国 醋 出口 美国 HS 2209 海关 出口量; China vinegar exports United States HS 2209 volume UN Comtrade; 恒顺醋业 2024年年报 境外 营业收入 出口; 恒顺 醋 出口 占全国 醋出口 比例 美国市场

- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 9/9
  - p15 China HS 22090000 vinegar exports, total volume, 2022 full year = **19,604,254** liters (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p16 China HS 22090000 vinegar exports, total value, 2022 full year = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p17 China HS 22090000 vinegar exports, total volume, 2023 full year = **21,832,831** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p18 China HS 22090000 vinegar exports, total value, 2023 full year = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p19 China HS 22090000 vinegar exports, total volume, 2024 full year = **25,760,168** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p20 China HS 22090000 vinegar exports, total value, 2024 full year = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p21 China HS 22090000 vinegar exports, average unit price, 2024 full year = **1.15** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p22 China HS 22090000 vinegar exports, average unit price, 2023 full year = **1.18** USD per liter (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p23 China HS 22090000 vinegar exports, average unit price, 2022 full year = **1.25** USD per liter (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p24 China HS 22090000 vinegar exports to the United States, volume, cumulative 2020- = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p25 China HS 22090000 vinegar exports to the United States, value, cumulative 2020-0 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p26 US share of China HS 22090000 vinegar export volume, cumulative 2020-01 to 2022- = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p27 China HS 22090000 vinegar exports worldwide, total volume, cumulative 2020-01 to = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p28 Number of destination countries for China HS 22090000 vinegar exports, cumulativ = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p29 China HS 22090000 vinegar exports to Hong Kong, volume, cumulative 2020-01 to 20 = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p30 China HS 22090000 vinegar exports to Hong Kong, value, cumulative 2020-01 to 202 = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "出口中国香港金额最高,总计15,656,412美元"
  - p31 Hong Kong share of China HS 22090000 vinegar export volume, cumulative 2020-01 t = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p32 China HS 22090000 vinegar exports to Singapore, volume, cumulative 2020-01 to 20 = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p33 China HS 22090000 vinegar exports to Australia, volume, cumulative 2020-01 to 20 = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p34 China HS 22090000 vinegar exports to Netherlands, volume, cumulative 2020-01 to  = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p35 China HS 22090000 vinegar exports to Malaysia, volume, cumulative 2020-01 to 202 = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p36 China HS 22090000 vinegar exports to Canada, volume, cumulative 2020-01 to 2022- = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p37 China HS 22090000 vinegar exports to Japan, volume, cumulative 2020-01 to 2022-1 = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [physical_flow] Hengshun production capacity and export logistics

Hypothesis: Hengshun's total vinegar production (liters/tons) × export share × US share of exports ÷ average bottle volume = US bottle count. Role: physical throughput route independent of revenue; requires production volume, export share, US share, and bottle size.

Queries issued by the searcher: 恒顺醋业 2024 年报 产量 万吨 醋; 恒顺 出口 占比 海外 销量 醋; 恒顺 外贸 出口 美国 市场 占比 食醋 出口量 吨; 中国 食醋 出口 美国 占比 出口量 万吨 2023

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://www.lhratings.com/reports/B008658-P47071-2019-GZ2021.pdf` -> **live_dated** (page date 2021-06-25); points raw/verified 15/13
  - p38 Hengshun Cuoye black vinegar production volume 2020 (capacity utilisation 100%) = **30** 万吨 (10,000 tons) (2020-01-01..2020-12-31) [keep: ] quote: "2020 年 黑醋 30.00 30.00 100.00"
  - p39 Hengshun Cuoye white vinegar production volume 2020 = **4.55** 万吨 (10,000 tons) (2020-01-01..2020-12-31) [keep: ] quote: "白醋 5.00 4.55 90.99"
  - p40 Hengshun Cuoye total (black+white+cooking wine) production volume 2020 = **41.37** 万吨 (10,000 tons) (2020-01-01..2020-12-31) [keep: ] quote: "合计 43.00 41.37 96.21"
  - p41 Hengshun Cuoye black vinegar production volume 2019 = **30** 万吨 (10,000 tons) (2019-01-01..2019-12-31) [DISCARD: Black vinegar 2019 = 30万吨 identical to 2018/2020 capacity-bound value; redundant.] quote: "2019 年 黑醋 30.00 30.00 100.00"
  - p42 Hengshun Cuoye white vinegar production volume 2019 = **4.42** 万吨 (10,000 tons) (2019-01-01..2019-12-31) [keep: ] quote: "白醋 5.00 4.42 88.34"
  - p43 Hengshun Cuoye black vinegar production volume 2018 = **30** 万吨 (10,000 tons) (2018-01-01..2018-12-31) [DISCARD: Black vinegar 2018 = 30万吨 identical to later years; redundant.] quote: "2018 年 黑醋 30.00 30.00 100.00"
  - p44 Hengshun Cuoye white vinegar production volume 2018 = **4.3** 万吨 (10,000 tons) (2018-01-01..2018-12-31) [keep: ] quote: "白醋 5.00 4.30 86.02"
  - p45 Hengshun Cuoye black vinegar production volume 2021 Q1 = **10.27** 万吨 (10,000 tons) (2021-01-01..2021-03-31) [DISCARD: 2021 Q1 partial-year black vinegar volume; not comparable to annual figures and not needed.] quote: "2021 年 1-3 月 黑醋 30.00 10.27 34.24"
  - p46 Hengshun Cuoye white vinegar production volume 2021 Q1 = **1.33** 万吨 (10,000 tons) (2021-01-01..2021-03-31) [DISCARD: 2021 Q1 partial-year white vinegar volume; not comparable to annual figures.] quote: "白醋 5.00 1.33 26.67"
  - p47 Hengshun Cuoye glass bottle purchases 2020 (count of bottles, packaging input) = **35,706** 万只 (10,000 bottles) (2020-01-01..2020-12-31) [keep: ] quote: "玻璃瓶 31049 0.57 35706 0.59 9248 0.60"
  - p48 Hengshun Cuoye glass bottle purchases 2019 (count of bottles) = **31,049** 万只 (10,000 bottles) (2019-01-01..2019-12-31) [DISCARD: 2019 bottle count redundant with 2020 (p47) for conversion purposes.] quote: "玻璃瓶 31049 0.57 35706 0.59 9248 0.60"
  - p49 Hengshun Cuoye glass bottle purchases 2021 Q1 (count of bottles) = **9,248** 万只 (10,000 bottles) (2021-01-01..2021-03-31) [DISCARD: 2021 Q1 partial-year bottle count; not comparable to annual.] quote: "玻璃瓶 31049 0.57 35706 0.59 9248 0.60"
  - p50 Hengshun Cuoye glass bottle average purchase price 2020 = **0.59** 元/只 (yuan per bottle) (2020-01-01..2020-12-31) [keep: ] quote: "玻璃瓶 31049 0.57 35706 0.59 9248 0.60"
- `http://mp.cnfol.com/54972/article/1764648112-142144983.html` -> **live_dated** (page date 2025-12-02); points raw/verified 15/10
  - p51 Hengshun vinegar series production volume, 2024 = **210,600** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨,销量也超过21.27万吨。"
  - p52 Hengshun vinegar series sales volume, 2024 = **212,700** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨,销量也超过21.27万吨。"
  - p53 Hengshun total revenue, 2024 = **2,196,000,000** 元 (2024-01-01..2024-12-31) [keep: ] quote: "年报显示,去年,其总营收为21.96亿元,醋系列就实现12.66亿元,占据过半营收。"
  - p54 Hengshun vinegar series revenue, 2024 = **1,266,000,000** 元 (2024-01-01..2024-12-31) [keep: ] quote: "年报显示,去年,其总营收为21.96亿元,醋系列就实现12.66亿元,占据过半营收。"
  - p55 Hengshun offline distributors covered nationwide, end of last year = **1,700** 家 (2024-12-31..2024-12-31) [keep: ] quote: "截至去年底,在线下渠道,恒顺醋业已经覆盖全国超1700家经销商,终端网点突破35万家。"
  - p56 Hengshun terminal outlets, end of last year = **350,000** 家 (2024-12-31..2024-12-31) [keep: ] quote: "终端网点突破35万家。"
  - p57 Hengshun self-media cumulative followers, end of last year = **280,000** 人 (2024-12-31..2024-12-31) [keep: ] quote: "截止去年底累计粉丝超28万。"
  - p58 Hengshun research and pilot base area, end of last year = **6,000** 平方米 (2024-12-31..2024-12-31) [keep: ] quote: "截至去年底,恒顺醋业的研究实验场所和中试基地占地 6000多平方米"
  - p59 Hengshun high-end R&D equipment count, end of last year = **50** 台套 (2024-12-31..2024-12-31) [keep: ] quote: "各类高端研发设备50余台套、省级以上科研平台6个"
  - p60 Hengshun provincial-level and above research platforms, end of last year = **6** 个 (2024-12-31..2024-12-31) [keep: ] quote: "各类高端研发设备50余台套、省级以上科研平台6个"
- dropped by code checks: 22 (value_as_written not in quote as a whole number: 16; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; period_end missing or unparseable: 4; scale word '亿' not supported by quote or table header: 1)

### d4 [related_series] US import / retail data for Chinese vinegar and Asian condiments

Hypothesis: US imports of Chinese vinegar (HS 2209) and Hengshun's brand share in US Asian grocery channels give US sell-through volume; combined with average bottle size gives bottle count. Role: validates the shipment route from the demand side and captures distributor imports.

Queries issued by the searcher: US imports Chinese vinegar HS 2209 2024 volume kg; Hengshun vinegar US Asian supermarket market share; Hengshun 恒顺 醋业 2024年报 境外 出口 收入 占比; "black vinegar" US retail sales market share brand Kikkoman Hengshun Chinese vinegar category

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1974663940947992576` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-

### d5 [base_rates] Bottle-size and unit-price conversion

Hypothesis: US-bound Hengshun vinegar is sold mostly in 500ml glass bottles (with some 300ml/250ml). Average bottle volume ≈ 0.4-0.5 L; average export price per bottle can be derived from export revenue ÷ estimated bottle count or from US retail price ÷ markup. Role: converts volume or revenue routes into bottle counts; constrains the largest conversion uncertainty.

Queries issued by the searcher: Hengshun vinegar 500ml Amazon price; 恒顺香醋 出口 500ml 美国; 恒顺醋业 2024年年报 境外收入 出口 营业收入; weee Hengshun Chinkiang vinegar 500ml price

- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://www.renrendoc.com/paper/157916955.html` -> **live_dated** (page date 2021-10-25); points raw/verified 15/15
  - p61 Hengshun vinegar overseas retail price in USD (stated overseas selling price) = **7.99** USD per unit (bottle) (..) [keep: ] quote: "镇江香醋采取"物美价廉"战略,将香醋的海外售价控制在7.99美元,与老干妈辣酱的11.99美元相比便宜了许多"
  - p62 Lao Gan Ma chili sauce overseas retail price in USD (comparison price point) = **11.99** USD per unit (bottle) (..) [DISCARD: Lao Gan Ma comparison price; irrelevant to Hengshun bottle count.] quote: "将香醋的海外售价控制在7.99美元,与老干妈辣酱的11.99美元相比便宜了许多"
  - p63 Share of US vinegar-condiment consumers buying Hengshun vinegar among total Heng = **91.3** % (..) [DISCARD: Garbled/ambiguous '91.3%' claim; not a usable share of any defined population.] quote: "以美国醋类调味品消费者为例,购买恒顺香醋的消费者占恒顺产品总数的百分之91.3%"
  - p64 Zhenjiang Hengshun vinegar annual production volume (approx., tonnes) = **100,000** tonnes (..) [keep: ] quote: "但近几年香醋产量徘徊在 10万吨,仅占了全国食醋生产总量的 5%左右"
  - p65 Zhenjiang Hengshun vinegar share of national vinegar production total = **5** % (..) [DISCARD: National production share; not needed for US bottle count.] quote: "但近几年香醋产量徘徊在 10万吨,仅占了全国食醋生产总量的 5%左右"
  - p66 Number of countries where Hengshun vinegar is sold (abstract claim) = **43** countries (..) [DISCARD: Abstract '43 countries' claim; superseded by p67 and not quantitative for US.] quote: "生产的香醋畅销中国和世界43个国家"
  - p67 Number of countries Hengshun vinegar is widely sold to (abstract claim) = **50** countries (..) [keep: ] quote: "在国际市场上逐渐崭露头角,广销50多个国家并供应我国驻外160多个国家使馆"
  - p68 Number of Chinese embassies abroad supplied by Hengshun products = **160** embassies (..) [DISCARD: Embassy supply count; irrelevant to US bottle volume.] quote: "广销50多个国家并供应我国驻外160多个国家使馆"
  - p69 Japan per-capita annual vinegar consumption = **7.9** kg per person per year (..) [DISCARD: Japan per-capita consumption; irrelevant to Hengshun US exports.] quote: "其中日本每年的人均食醋消费量为7.9公斤,是我过每年人均食醋消费量的3.4倍,占世界第一"
  - p70 US per-capita annual vinegar consumption = **6.5** kg per person per year (..) [DISCARD: US per-capita consumption; too aggregate to convert to Hengshun bottles without brand share, which is missing.] quote: "美国每年的人均食醋消费量为6.5公斤,为我过每年人均食醋消费量的2.8倍,位于世界第二"
  - p71 Hengshun vinegar business revenue (2014) = **1,040,000,000** CNY (亿元) (2014-01-01..2014-12-31) [DISCARD: 2014 vinegar revenue; too old and superseded by 2024 segment revenue.] quote: "2014年,海天味业酱油业务营收达到63亿元,占行业比重为9.84%,恒顺醋业醋业务营收达到10.4亿元,行业占比约为3.85%"
  - p72 Hengshun vinegar business share of vinegar industry (2014) = **3.85** % (2014-01-01..2014-12-31) [DISCARD: 2014 industry share; too old and not needed.] quote: "恒顺醋业醋业务营收达到10.4亿元,行业占比约为3.85%"
  - p73 Haitian soy sauce business revenue (2014) = **6,300,000,000** CNY (亿元) (2014-01-01..2014-12-31) [DISCARD: Haitian soy sauce revenue; irrelevant.] quote: "2014年,海天味业酱油业务营收达到63亿元,占行业比重为9.84%"
  - p74 China vinegar industry CR5 (top-5 concentration) = **15** % (..) [DISCARD: Industry CR5; irrelevant to US bottle count.] quote: "目前我国食醋行业的CR5不足15%"
  - p75 Zhenjiang Hengshun share of Zhenjiang vinegar market = **80** as written "百分之八十", value check pending % (..) [DISCARD: Zhenjiang market share; domestic, not US-relevant.] quote: "镇江恒顺香醋一枝独秀,占据了百分之八十的镇江市场份额"

### d6 [persona] Hengshun overseas distributors and US importers

Hypothesis: Hengshun's US distributor(s) (e.g., Asian food importers) may disclose volumes or container counts; container count × bottles per container gives an independent shipment estimate. Role: bottom-up shipment check.

Queries issued by the searcher: 恒顺 美国 经销商 进口商 醋; Hengshun vinegar US distributor importer; 恒顺醋业 2024年年度报告 境外 营业收入 出口; Well Luck Co Hengshun Zhenjiang vinegar containers shipments 2024

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **live_dated** (page date 2024-11-01); points raw/verified 2/0
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### d7 [forecasts_markets] Hengshun strategic/investor guidance on overseas expansion

Hypothesis: Hengshun has publicly discussed overseas market expansion (including North America) in investor relations or strategy documents; stated targets or growth rates for overseas revenue constrain the US share trend. Role: bounds the US share and its growth, and flags whether US is a material market.

Queries issued by the searcher: 恒顺醋业 海外 市场 拓展 美国; 恒顺醋业 投资者关系 出口 增长 海外收入; 恒顺醋业 外贸模式 出口 收入 占比 2024年 境外; Hengshun vinegar exports United States Well Luck distributor North America

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1974663940947992576` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%90%84%E4%BA%9E%E6%B4%B2%E8%B6%85%E5%B8%82%E6%8E%A8%E5%87%BA%E6%81%86%E9%A0%86%E7%B3%BB%E5%88%97%E7%94%A2%E5%93%81%E9%BB%` -> **live_dated** (page date 2024-11-29); points raw/verified 0/0

### d8 [shocks] Trade policy and tariff exposure

Hypothesis: US-China tariffs on food products (Section 301) affect Chinese vinegar export volumes/prices to the US; a tariff change in 2018-2024 could shift US-bound volumes and thus bottle counts. Role: adjusts historical relationships and flags period-specific distortions.

Queries issued by the searcher: Section 301 tariff vinegar HS 2209 China; 中国 醋 出口 美国 关税 影响 恒顺; Section 301 List 3 $200 billion tariff 2209 vinegar effective September 24 2018 10 percent raised 25 percent May 2019; China vinegar exports to United States volume tons 2024 HS 2209 US import statistics

- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 9/0
- `https://www.akingump.com/en/insights/alerts/ustr-increases-section-301-tariffs-on-list-3-products-and` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.alston.com/en/insights/publications/2022/05/section-301-actions-against-chinese-imports` -> **live_dated** (page date 2022-05-26); points raw/verified 15/14
  - p76 Section 301 List 1 tariff rate on US imports from China (announced June 20, 2018 = **25** % (2018-07-06..2018-07-06) [keep: ] quote: "List 1 tariffs were announced on June 20, 2018 on $34 billion of U.S. imports at a tariff rate of 25%, effective July 6, 2018."
  - p77 Section 301 List 1 value of US imports from China covered = **34,000,000,000** USD of imports (2018-07-06..2018-07-06) [DISCARD: List 1 covered-import value; not a quantity usable in the bottle formula.] quote: "List 1 tariffs were announced on June 20, 2018 on $34 billion of U.S. imports at a tariff rate of 25%, effective July 6, 2018."
  - p78 Section 301 List 2 tariff rate on US imports from China (announced August 16, 20 = **25** % (2018-08-23..2018-08-23) [keep: ] quote: "List 2 tariffs were announced on August 16, 2018 on $16 billion of U.S. imports at a tariff rate of 25%, effective August 23, 2018."
  - p79 Section 301 List 2 value of US imports from China covered = **16,000,000,000** USD of imports (2018-08-23..2018-08-23) [DISCARD: List 2 covered-import value; not usable.] quote: "List 2 tariffs were announced on August 16, 2018 on $16 billion of U.S. imports at a tariff rate of 25%, effective August 23, 2018."
  - p80 Section 301 List 3 value of US imports from China covered = **200,000,000,000** USD of imports (2018-09-24..2018-09-24) [DISCARD: List 3 covered-import value; not usable.] quote: "List 3 tariffs were announced on September 21, 2018 on $200 billion of U.S. imports at a tariff rate of 10%, effective September 24, 2018"
  - p81 Section 301 List 3 initial tariff rate on US imports from China = **10** % (2018-09-24..2019-05-09) [keep: ] quote: "List 3 tariffs were announced on September 21, 2018 on $200 billion of U.S. imports at a tariff rate of 10%, effective September 24, 2018"
  - p82 Section 301 List 3 increased tariff rate on US imports from China = **25** % (2019-05-10..2019-05-10) [keep: ] quote: "This rate increased to 25%, effective May 10, 2019."
  - p83 Section 301 List 4 value of US imports from China covered (announced August 20,  = **300,000,000,000** USD of imports (2019-08-20..2019-08-20) [DISCARD: List 4 covered-import value; not usable.] quote: "List 4 tariffs were announced on August 20, 2019 on $300 billion of U.S. imports, but the list was split into Lists 4A and 4B."
  - p84 Section 301 List 4A initial tariff rate on US imports from China = **15** % (2019-09-01..2020-02-13) [keep: ] quote: "Tariffs on List 4A started at 15%, effective September 1, 2019, and then decreased to 7.5%, effective February 14, 2020."
  - p85 Section 301 List 4A reduced tariff rate on US imports from China = **7.5** % (2020-02-14..2020-02-14) [keep: ] quote: "Tariffs on List 4A started at 15%, effective September 1, 2019, and then decreased to 7.5%, effective February 14, 2020."
  - p86 China Phase One commitment to expand purchases of US goods and services (vs 2017 = **200,000,000,000** USD of additional purchases (2020-01-01..2021-12-31) [DISCARD: Phase One purchase commitment; macro, not usable for vinegar bottles.] quote: "to expand purchases of certain U.S. goods and services by $200 billion (compared to 2017 levels) during 2020 and 2021."
  - p87 Share of Phase One purchase commitment met by China = **57** % (2020-01-01..2021-12-31) [DISCARD: Phase One compliance share; not usable.] quote: "China has met only 57% of its commitment to increase purchases of U.S. goods and services"
  - p88 Number of exclusions covered by USTR October 2021 targeted exclusion process = **549** exclusions (2021-10-04..2021-10-04) [DISCARD: Exclusion count; not usable.] quote: "covering only the 549 exclusions that the USTR previously granted and extended"
  - p89 Number of exclusions reinstated by USTR through December 31, 2022 = **352** exclusions (2021-10-04..2022-12-31) [DISCARD: Reinstated exclusion count; not usable.] quote: "The USTR eventually reinstated 352 of these exclusions through December 31, 2022."
- `https://php.cnstock.com/texts/2024/20240429/928E372036F0B1A21D7B14C20FD87AD6.pdf` -> **live_dated** (page date 2024-04-29); points raw/verified 15/11
  - p90 Hengshun vinegar-series (醋系列) sales volume, tonnes, 2023 = **209,959** tonnes (2023-01-01..2023-12-31) [keep: ] quote: "醋系列 吨 207,648.56 209,958.69 12,985.41 -0.83 1.57 -15.10"
  - p91 Hengshun vinegar-series (醋系列) production volume, tonnes, 2023 = **207,649** tonnes (2023-01-01..2023-12-31) [keep: ] quote: "醋系列 吨 207,648.56 209,958.69 12,985.41 -0.83 1.57 -15.10"
  - p92 Hengshun vinegar-series sales volume year-on-year change, 2023 = **1.57** % (2023-01-01..2023-12-31) [DISCARD: YoY change redundant with p90/p91 levels.] quote: "醋系列 吨 207,648.56 209,958.69 12,985.41 -0.83 1.57 -15.10"
  - p93 Hengshun foreign-trade (外贸模式) revenue, RMB, 2023 = **45,133,890** RMB yuan (2023-01-01..2023-12-31) [keep: ] quote: "外贸模式 45,133,890.44 33,201,719.93 26.44 3.30 -4.09 增加 5.67 个百"
  - p94 Hengshun foreign-trade revenue year-on-year change, 2023 = **3.3** % (2023-01-01..2023-12-31) [keep: ] quote: "外贸模式 45,133,890.44 33,201,719.93 26.44 3.30 -4.09 增加 5.67 个百"
  - p95 Hengshun foreign-trade gross margin, 2023 = **26.44** % (2023-01-01..2023-12-31) [keep: ] quote: "外贸模式 45,133,890.44 33,201,719.93 26.44 3.30 -4.09 增加 5.67 个百"
  - p96 Hengshun vinegar-series revenue, RMB, 2023 = **1,294,067,634** RMB yuan (2023-01-01..2023-12-31) [keep: ] quote: "醋系列 1,294,067,634.34 736,233,037.46 43.11 0.79 -1.91 增加 1.57 个百"
  - p97 Hengshun vinegar-series gross margin, 2023 = **43.11** % (2023-01-01..2023-12-31) [keep: ] quote: "醋系列 1,294,067,634.34 736,233,037.46 43.11 0.79 -1.91 增加 1.57 个百"
  - p98 Hengshun total revenue (consolidated), RMB, 2023 = **2,106,410,685** RMB yuan (2023-01-01..2023-12-31) [keep: ] quote: "营业收入 2,106,410,685.37 2,139,020,033.23 -1.52 1,893,347,829.74"
  - p99 Hengshun main condiment business revenue, RMB, 2023 = **2,077,821,815** RMB yuan (2023-01-01..2023-12-31) [keep: ] quote: "调味品 2,077,821,815.46 1,405,296,479.87 32.37 2.27 4.87 减少 1.67 个百"
  - p100 Hengshun online sales channel revenue, RMB, 2023 = **264,716,814** RMB yuan (2023-01-01..2023-12-31) [keep: ] quote: "线上销售 264,716,814.16 12.74 50.22 281,213,097.35 13.84 50.16"
- dropped by code checks: 14 (period year 2024 does not appear in the page text or URL (likely mis-dated): 9; period_end missing or unparseable: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### b1 [own_history] Hengshun annual report geographic/overseas revenue split

Hypothesis: If Hengshun's annual report discloses 境外/出口 revenue and, ideally, a North America or US sub-line, this converts the foreign-trade revenue (p3) directly into a US revenue base, removing the need to assume a US share of exports. This is the single largest missing input for the revenue route.

Queries issued by the searcher: 600305 恒顺醋业 2024 年报 境外收入 分地区; 恒顺醋业 出口 海外 收入 占比 美国; 恒顺醋业 2024年 国外营业收入 36,910,481.37 元 占比 0.71%; 恒顺醋业 出口 美国市场 占比 40% 互动 2024

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1856807881049677824` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0

### b2 [related_series] China customs HS 22090000 exports to US, 2024

Hypothesis: A 2024 US-specific HS 22090000 volume (rather than the 2020-2022 cumulative 11.35% share) would let us apply Hengshun's share of China vinegar exports to a current US-bound volume, replacing the stale share with a current one and anchoring the physical-flow route.

Queries issued by the searcher: HS 22090000 出口 美国 2024 数量 醋; China vinegar exports United States 2024 HS 2209 Comtrade; 2209 vinegar US imports China 2024 volume liters; UN Comtrade China exports United States 220900 2024 quantity liters; wits worldbank 220900 China United States 2024 exports quantity; "220900" China exports "United States" 2024 quantity; 中国 醋 出口 美国 2024 升 海关

- `https://wits.worldbank.org/trade/comtrade/en/country/All/year/2024/tradeflow/Exports/partner/CHN/product/220900` -> **live_dated** (page date 2024-01-01); points raw/verified 15/7
  - p101 US exports of HS 220900 vinegar to China, 2024 quantity = **3,991,150** liter (2024-01-01..2024-12-31) [DISCARD: US exports of vinegar to China — wrong trade direction for China→US flow.] quote: "\| United States \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 2,644.23 \| 3,991,150 \| Liter \|"
  - p102 EU exports of HS 220900 vinegar to China, 2024 quantity = **1,970,610,000,000** liter (2024-01-01..2024-12-31) [DISCARD: EU exports to China, wrong direction and implausible magnitude (1.97e12 L) indicating a unit error.] quote: "\| European Union \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 4,348.96 \| 1,970,610,000,000 \| Liter \|"
  - p103 Italy exports of HS 220900 vinegar to China, 2024 quantity = **1,015,620** liter (2024-01-01..2024-12-31) [DISCARD: Italy exports to China — wrong trade direction.] quote: "\| Italy \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 2,700.16 \| 1,015,620 \| Liter \|"
  - p104 Japan exports of HS 220900 vinegar to China, 2024 quantity = **1,762,440** liter (2024-01-01..2024-12-31) [DISCARD: Japan exports to China — wrong trade direction.] quote: "\| Japan \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 1,406.64 \| 1,762,440 \| Liter \|"
  - p105 Germany exports of HS 220900 vinegar to China, 2024 quantity = **675,238** liter (2024-01-01..2024-12-31) [DISCARD: Germany exports to China — wrong trade direction.] quote: "\| Germany \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 1,230.31 \| 675,238 \| Liter \|"
  - p106 Korea Rep. exports of HS 220900 vinegar to China, 2024 quantity = **511,845** liter (2024-01-01..2024-12-31) [DISCARD: Korea exports to China — wrong trade direction.] quote: "\| Korea, Rep. \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 843.82 \| 511,845 \| Liter \|"
  - p107 Malaysia exports of HS 220900 vinegar to China, 2024 quantity = **939,971** liter (2024-01-01..2024-12-31) [DISCARD: Malaysia exports to China — wrong trade direction.] quote: "\| Malaysia \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| China \| 439.54 \| 939,971 \| Liter \|"
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p108 China HS 22090000 vinegar exports to United States, cumulative volume, 2020-01 t = **6,597,078** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p24 (same 2020–2022 US cumulative volume).] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p109 China HS 22090000 vinegar exports to United States, cumulative value, 2020-01 to = **8,459,027** USD (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p25.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p110 United States share of China HS 22090000 vinegar export volume, 2020-01 to 2022- = **11.35** % (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p26.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p111 China HS 22090000 vinegar exports worldwide, cumulative volume, 2020-01 to 2022- = **58,119,878** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p27.] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p112 Number of destination countries for China HS 22090000 vinegar exports, 2020-01 t = **129** countries (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p28.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p113 China HS 22090000 vinegar exports to Hong Kong, cumulative volume, 2020-01 to 20 = **13,624,552** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p29.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p114 China HS 22090000 vinegar exports to Hong Kong, cumulative value, 2020-01 to 202 = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p30.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p115 Hong Kong share of China HS 22090000 vinegar export volume, 2020-01 to 2022-12 = **23.44** % (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p31.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p116 China HS 22090000 vinegar exports to Singapore, cumulative volume, 2020-01 to 20 = **4,057,620** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p32.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p117 China HS 22090000 vinegar exports to Australia, cumulative volume, 2020-01 to 20 = **3,691,524** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p33.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p118 China HS 22090000 vinegar exports to Netherlands, cumulative volume, 2020-01 to  = **3,519,273** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p34.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p119 China HS 22090000 vinegar exports to Malaysia, cumulative volume, 2020-01 to 202 = **3,160,711** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p35.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p120 China HS 22090000 vinegar exports to Canada, cumulative volume, 2020-01 to 2022- = **2,537,372** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p36.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p121 China HS 22090000 vinegar exports to Japan, cumulative volume, 2020-01 to 2022-1 = **2,404,533** liters (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p37.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- dropped by code checks: 9 (scale word 'thousand' not supported by quote or table header: 8; value_as_written not in quote as a whole number: 1)

### b3 [persona] Hengshun US distributor / importer shipment data

Hypothesis: US import records (bill of lading / Panjiva-style) for Hengshun-branded vinegar would give container counts and thus bottle counts directly, providing an independent bottom-up check on the revenue and physical-flow routes and resolving the US-share assumption.

Queries issued by the searcher: Hengshun vinegar US import bill of lading 2024; Jiangsu Hengshun Vinegar shipment USA container export; Panjiva Hengshun vinegar importer; 恒顺醋业 出口 美国 2024 年报

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-group-zhenjiang-in` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us', 'zhenjiang vinegar']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p10', 'p54', 'p96'] All describe Hengshun's 醋系列 segment revenue; p1/p2/p54/p96 agree at ~1.27bn RMB (2024) and ~1.29bn RMB (2023), p10 is the derived YoY change. Same underlying annual-report disclosure, so not independe
- corroborating: ['p3', 'p4', 'p5', 'p93', 'p94'] Foreign-trade (外贸模式) revenue: 2023 = 45.13m RMB (p4, p93), 2024 = 47.74m RMB (p3), +5.78% (p5) consistent with p94's 2023 +3.3%. Same disclosure lineage.
- corroborating: ['p6', 'p7', 'p53', 'p98'] Total revenue ~2.09-2.11bn RMB; p53 rounds to 2.196bn (slightly different consolidation/rounding). Broad agreement on scale.
- corroborating: ['p8', 'p9', 'p99'] Product-category total (vinegar+wine+sauce) ~1.77-1.82bn RMB; consistent with segment sums.
- corroborating: ['p51', 'p52', 'p90', 'p91', 'p92'] Vinegar-series physical volumes: 2023 ~207.6-210.0 kt, 2024 ~210.6-212.7 kt; consistent growth. Physical throughput anchor.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23'] China HS 22090000 total export volume/value/unit price 2022-2024; internally consistent (value/volume = unit price).
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28'] US is #2 destination at 11.35% of China vinegar export volume (2020-2022 cumulative); consistent with p24/p25/p27.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37'] Destination breakdown shares sum plausibly; Hong Kong #1, US #2. Same source, not independent of p24-p28.
- corroborating: ['p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] Hengshun Cuoye production volumes 2018-2021Q1 from rating report; black vinegar flat at 30万吨 capacity-bound, white ~4.3-4.55万吨.
- corroborating: ['p47', 'p48', 'p49', 'p50'] Glass bottle purchase counts and unit price from same rating report; useful for bottle-size/price conversion but 2019-2021 vintage.
- corroborating: ['p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75'] Single undated secondary document (renrendoc); internally consistent but low reliability and undated. Use only as loose context/price anchor.
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89'] Section 301 tariff timeline from one law-firm source; contextual for US-bound flow, not a direct quantity.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p3', 'p5', 'p93', 'p94'] All describe Hengshun's 外贸模式 (foreign-trade) revenue and its growth; p3 (2024, 4,774.13万元) and p93 (2023, 45.13M RMB) are the same series in consecutive years, and p5/p94 are the matching YoY changes.
- corroborating: ['p1', 'p10', 'p54', 'p96'] Vinegar-segment revenue 2024 (p1/p54 ≈ 1.266bn RMB) and 2023 (p96 ≈ 1.294bn RMB) with the -2.2% YoY change (p10). Same annual-report source; p54 is a rounded restatement of p1.
- corroborating: ['p6', 'p53', 'p98'] Total revenue 2024 (p6/p53 ≈ 2.09–2.20bn RMB) and 2023 (p98 ≈ 2.106bn RMB). Minor rounding differences between the Sina table and the cnfol article; same disclosure.
- corroborating: ['p51', 'p52', 'p90', 'p91'] Vinegar-series physical volumes: 2024 production 210,600 t / sales 212,700 t (p51/p52) vs 2023 production 207,649 t / sales 209,959 t (p90/p91). Consistent small growth; same annual-report basis.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23'] China HS 22090000 total export volume/value/unit price for 2022–2024 from one customs-derived source. Internally consistent (value/volume = unit price). Gives the 2024 total export volume denominator 
- corroborating: ['p24', 'p25', 'p26', 'p108', 'p109', 'p110'] Duplicate copies of the same 2020–2022 cumulative US-bound HS 22090000 volume/value and 11.35% US share. One underlying measurement; the 11.35% share is stale (2020–2022) and must be transferred to 20
- corroborating: ['p27', 'p28', 'p29', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p111', 'p112', 'p113', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121'] Same 2020–2022 cumulative destination breakdown; duplicates of p24–p26 family. Useful only as context on the US being the #2 destination (~11% of volume).
- corroborating: ['p38', 'p39', 'p40', 'p42', 'p44', 'p47', 'p50'] 2020 credit-rating report production and glass-bottle purchase data for Hengshun Cuoye. Older period; bottle purchases (35,706万只) and average bottle price (0.59元) are useful only as a packaging-intens
- corroborating: ['p61', 'p64', 'p67'] Overseas retail price ($7.99/unit), approximate annual production (100,000 t) and 'sold to 50+ countries' from a single undated secondary document. Weak, undated; usable only as loose context, not as 
- corroborating: ['p76', 'p78', 'p81', 'p82', 'p84', 'p85'] Section 301 tariff schedule; contextual for why US-bound volumes may be suppressed, but no direct quantitative link to Hengshun bottle counts.
- conflicting: ['p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107'] These are US/EU/other exports of HS 220900 TO China, i.e. the reverse trade direction, not China's exports to the US. p102 (1.97e12 L) is also obviously a unit error. Not usable for the target flow.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a2 | Average Hengshun export bottle volume | 0.5 | 0.35..0.6 | 0.324..0.6481 (widened) | L per bottle | m1 (m1), m2 (m2) | US-bound Chinese vinegar is predominantly sold in 500 ml glass bottles with some 300/250 ml; a 0.5 L central value with a 0.35–0.6 L range reflects the mix of retail bottle sizes. The 2020 glass-bottle purchase data (p47/p50) imply an all-product average near 1.1 L/bottle including large formats, so | Export packaging is dominated by retail glass bottles in the 250–600 ml range, excluding bulk drums. | Evidence that a large share of US-bound volume is bulk/industrial or in much larger retail formats. |
| a3 | Hengshun export FOB price per liter (RMB) | 12 | 8..18 | 8..18 | RMB per liter | m1 (m1) | China's average HS 22090000 export unit price is ~1.15 USD/L (p21), i.e. ~8 RMB/L at ~7 RMB/USD; Hengshun is a premium branded Zhenjiang vinegar, so its FOB price should sit above the national average, around 12 RMB/L with a range of 8–18. | Hengshun's export price is a premium multiple of the national average unit value. | Disclosed export revenue and volume implying a per-liter price far outside 8–18 RMB. |
| a4 | Hengshun share of China HS 22090000 vinegar export volume, 2024 | 3 | 1..6 | 1..6 | % | m2 (m2) | Hengshun is the largest branded Zhenjiang-vinegar producer but China's vinegar exports are fragmented across many producers and unbranded bulk; a 3% volume share (1–6% range) is a reasonable order-of-magnitude for a leading branded exporter. | Hengshun's export volume is a small single-digit share of total Chinese vinegar exports. | Customs or company data showing Hengshun's export volume share outside 1–6%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 987,060 | ['p3', 'p26'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 156,178 | ['p19', 'p26'] / ['a2', 'a4'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **392,629** bottle, 80% interval [120,475, 1,279,575] bottle, basis method_spread (interval width set from the disagreement between the methods' estimates), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 11 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 2 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p1 | Hengshun vinegar (醋系列) segment sales revenue, 2024 | 1,265,596,300 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Revenue in RMB for the vinegar segment, not a bottle count of US exports; wrong measure, unit, and scope. |
| p3 | Hengshun foreign trade (外贸模式) sales revenue, 2024 | 47,741,300 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Foreign-trade revenue in RMB for all products, not a bottle count of US-bound vinegar; wrong measure, unit, and scope. |
| p6 | Hengshun total sales revenue (all channels), 2024 | 2,093,006,800 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Total company revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p8 | Hengshun product-category total sales revenue (vinegar+wine+sauce), 2024 | 1,774,174,300 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Combined product-category revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p11 | Hengshun direct sales (直销模式) revenue, 2024 | 103,817,200 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Direct-sales revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p12 | Hengshun dealer (经销模式) revenue, 2024 | 1,941,448,600 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Dealer-channel revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p13 | Hengshun online sales revenue, 2024 | 274,378,100 | 万元 RMB | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Online sales revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p51 | Hengshun vinegar series production volume, 2024 | 210,600 | 吨 | 2024-01-01..2024-12-31 | mp.cnfol.com | different | Production volume in tonnes for all vinegar series, not bottles exported to the US; wrong measure, unit, and scope. |
| p52 | Hengshun vinegar series sales volume, 2024 | 212,700 | 吨 | 2024-01-01..2024-12-31 | mp.cnfol.com | different | Sales volume in tonnes for all vinegar series, not bottles exported to the US; wrong measure, unit, and scope. |
| p53 | Hengshun total revenue, 2024 | 2,196,000,000 | 元 | 2024-01-01..2024-12-31 | mp.cnfol.com | different | Total revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |
| p54 | Hengshun vinegar series revenue, 2024 | 1,266,000,000 | 元 | 2024-01-01..2024-12-31 | mp.cnfol.com | different | Vinegar series revenue in RMB, not a bottle count of US exports; wrong measure, unit, and scope. |


## Final answer

Best estimate: 392,629 bottle of Hengshun bottled vinegar exported to the United States in calendar 2024 (all bottle types, excluding bulk drums), with a 80% model-based interval of 120,475 to 1,279,575 bottle.

Two routes were averaged at 50% and 50%. The revenue route (987,060 bottle) divides disclosed 2024 foreign-trade revenue of 47,741,300 万元 RMB by an assumed FOB price of 12 (range 8–18) and assumed bottle size 0.5 L (range 0.324–0.6481), applying the US share 11.35%. The physical route (156,178 bottle) scales China's 2024 vinegar export volume of 25,760,168 liters by that same US share, an assumed Hengshun export share of 3% (range 1%–6%), and bottle size.

Only the revenue, export volume and US share are observed; the price, bottle size and Hengshun share are analyst assumptions. The interval reflects disagreement between methods, not demonstrated accuracy. The biggest risk is the stale US share (2020–2022) and the assumed Hengshun share. Company-level US export volumes would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 Average Hengshun export bottle volume: 0.5 L per bottle, range 0.324 to 0.6481 (range widened by code); used by m1, m2. Overturned by: Evidence that a large share of US-bound volume is bulk/industrial or in much larger retail formats.
- a3 Hengshun export FOB price per liter (RMB): 12 RMB per liter, range 8 to 18; used by m1. Overturned by: Disclosed export revenue and volume implying a per-liter price far outside [n]–[n] RMB.
- a4 Hengshun share of China HS [n] vinegar export volume, 2024: 3%, range 1% to 6%; used by m2. Overturned by: Customs or company data showing Hengshun's export volume share outside [n]–[n].

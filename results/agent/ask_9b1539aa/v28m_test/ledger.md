# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (Jiangsu Hengshun Vinegar-Industry Co., Ltd.) vinegar sold/exported to the United States in a full year, all bottled vinegar types combined, counted as physical bottles (not cases, not liters, not revenue) | unit bottle | period 2024-01-01..2024-12-31 | publisher No official publisher discloses this figure; Jiangsu Hengshun Vinegar-Industry Co., Ltd. (SSE: 600305) annual reports and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Company investor-relations / annual-report analyst

Hypothesis: Hengshun's annual reports disclose total revenue, vinegar-segment revenue, and export (境外/出口) revenue or tonnage; the US share of export revenue times export volume, divided by average bottle size, gives bottles to the US. Direction: higher export revenue and higher US share imply more bottles.

Queries issued by the searcher: 恒顺醋业 年报 2024 境外收入 出口; 江苏恒顺醋业 2024年年度报告 醋 销量 吨 营业收入; 恒顺醋业 2024 经营数据公告 外贸模式 销售收入 4774.13万元 吨; Hengshun Vinegar annual report overseas revenue export United States share

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 15/15
  - p1 Hengshun vinegar series (醋系列) sales revenue, 2024 = **1,265,596,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p2 Hengshun vinegar series (醋系列) sales revenue, 2023 = **1,294,067,600** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p3 Hengshun vinegar series revenue year-on-year change, 2024 vs 2023 = **-2.2** % (2024-01-01..2024-12-31) [DISCARD: A year-on-year percentage change, not a level; redundant with p1/p2 which give the levels directly.] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p4 Hengshun foreign trade (外贸模式) sales revenue, 2024 = **47,741,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p5 Hengshun foreign trade (外贸模式) sales revenue, 2023 = **45,133,900** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p6 Hengshun foreign trade revenue year-on-year change, 2024 vs 2023 = **5.78** % (2024-01-01..2024-12-31) [DISCARD: YoY change of foreign-trade revenue; redundant with p4/p5 levels.] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p7 Hengshun total sales revenue (all products, by sales mode), 2024 = **2,093,006,800** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p8 Hengshun total sales revenue (all products, by sales mode), 2023 = **2,077,821,800** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p9 Hengshun total revenue (product category table), 2024 = **1,774,174,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p10 Hengshun total revenue (product category table), 2023 = **1,816,930,700** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p11 Hengshun wine series (酒系列) sales revenue, 2024 = **328,515,500** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Wine-series revenue — not vinegar; outside target scope.] quote: "\| 酒系列 \| 32,851.55 \| 32,699.19 \| 0.47 \|"
  - p12 Hengshun sauce series (酱系列) sales revenue, 2024 = **180,062,500** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Sauce-series revenue — not vinegar; outside target scope.] quote: "\| 酱系列 \| 18,006.25 \| 19,587.11 \| -8.07 \|"
  - p13 Hengshun direct sales (直销模式) revenue, 2024 = **103,817,200** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Direct-sales channel revenue, domestic-oriented; not a US export quantity and redundant with channel totals.] quote: "\| 直销模式 \| 10,381.72 \| 10,072.35 \| 3.07 \|"
  - p14 Hengshun dealer/distribution (经销模式) revenue, 2024 = **1,941,448,600** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Dealer-channel revenue, overwhelmingly domestic; not usable for US export volume.] quote: "\| 经销模式 \| 194,144.86 \| 193,196.45 \| 0.49 \|"
  - p15 Hengshun online sales revenue, 2024 = **274,378,100** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Online sales revenue, mostly domestic e-commerce; not a US export measure.] quote: "\| 线上销售 \| 27,437.81 \| 26,471.68 \| 3.65 \|"
- `https://www.lhratings.com/reports/B008658-P51234-2020-GZ2025.pdf` -> **live_dated** (page date 2025-06-25); points raw/verified 15/9
  - p16 Hengshun CuYe vinegar series (醋系列) revenue 2024 = **12.66** 亿元 (100 million RMB) (2024-01-01..2024-12-31) [keep: ] quote: "其中:醋系列 12.94 12.66"
  - p17 Hengshun CuYe vinegar series (醋系列) revenue 2023 = **12.94** 亿元 (100 million RMB) (2023-01-01..2023-12-31) [keep: ] quote: "其中:醋系列 12.94 12.66"
  - p18 Hengshun CuYe total operating revenue 2024 = **21.96** 亿元 (100 million RMB) (2024-01-01..2024-12-31) [keep: ] quote: "营业总收入 21.06 21.96"
  - p19 Hengshun CuYe total operating revenue 2023 = **21.06** 亿元 (100 million RMB) (2023-01-01..2023-12-31) [keep: ] quote: "营业总收入 21.06 21.96"
  - p20 Hengshun CuYe share of sales via distribution (经销) channel, approx share of reve = **95** % of revenue (2024-01-01..2024-12-31) [DISCARD: Distribution-channel share (~95%) is a domestic channel mix, not a US/export share; would mislead if used as export shar] quote: "恒顺醋业销售模式以经销为主(占收入的 95%左右),少量为直销和外贸"
  - p21 Zhenjiang city vinegar (食醋) output 2024 = **333,300** 万吨 (10,000 tons) (2024-01-01..2024-12-31) [DISCARD: Zhenjiang city total vinegar output (33.33万吨) is a city-wide figure, not Hengshun's; would overstate the company by a la] quote: "重点工业产品产量中,食醋产量 33.33 万吨,比上年增长 5.6%"
  - p22 Hengshun CuYe net profit 2024 = **1.12** 亿元 (100 million RMB) (2024-01-01..2024-12-31) [DISCARD: Net profit — irrelevant to bottle count.] quote: "江苏恒顺醋业股份有限公司 恒顺醋业 酱醋调味品 40.36% 43.64 33.29 21.96 1.12 0.80"
  - p23 Hengshun CuYe gross margin 2024 = **34.72** % (2024-01-01..2024-12-31) [DISCARD: Gross margin — irrelevant to bottle count.] quote: "毛利率 32.98% 34.72%"
  - p24 Hengshun CuYe sales revenue YoY growth 2024 = **4.27** % (2024-01-01..2024-12-31) [DISCARD: Revenue growth rate — redundant with revenue levels.] quote: "2024 年,恒顺醋业销售收入同比增长 4.27%"
- `https://user.guancha.cn/main/content?id=1557862` -> **live_dated** (page date 2025-12-02); points raw/verified 15/8
  - p25 Hengshun vinegar-series production volume, 2024 = **210,600** tons (2024-01-01..2024-12-31) [keep: ] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨"
  - p26 Hengshun vinegar-series sales volume, 2024 = **212,700** tons (2024-01-01..2024-12-31) [keep: ] quote: "销量也超过21.27万吨"
  - p27 Hengshun total revenue, 2024 = **2,196,000,000** yuan (RMB) (2024-01-01..2024-12-31) [keep: ] quote: "去年,其总营收为21.96亿元"
  - p28 Hengshun vinegar-series revenue, 2024 = **1,266,000,000** yuan (RMB) (2024-01-01..2024-12-31) [keep: ] quote: "醋系列就实现12.66亿元,占据过半营收"
  - p29 Number of Hengshun distributors covered nationwide, end of last year = **1,700** distributors (2024-12-31..2024-12-31) [DISCARD: Domestic distributor count — irrelevant to US export volume.] quote: "恒顺醋业已经覆盖全国超1700家经销商"
  - p30 Number of Hengshun terminal outlets, end of last year = **350,000** outlets (2024-12-31..2024-12-31) [DISCARD: Domestic terminal outlets — irrelevant to US export volume.] quote: "终端网点突破35万家"
  - p31 Hengshun self-media matrix cumulative followers, end of last year = **280,000** followers (2024-12-31..2024-12-31) [DISCARD: Social-media followers — irrelevant.] quote: "截止去年底累计粉丝超28万"
  - p32 Hengshun research and pilot-test site area, end of last year = **6,000** square meters (2024-12-31..2024-12-31) [DISCARD: R&D site area — irrelevant.] quote: "研究实验场所和中试基地占地 6000多平方米"
- dropped by code checks: 13 (scale word '万吨' not supported by quote or table header: 4; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; number: no number in value_as_written: 1; period_end missing or unparseable: 2)

### d2 [related_series] China customs trade-statistics analyst

Hypothesis: China customs HS code 2209 (vinegar and substitutes) export data to the US gives total Chinese vinegar export volume/value to the US; Hengshun's share of China's vinegar exports (from company export revenue vs. national total) times that volume, divided by bottle size, yields bottles. Direction: larger US-bound Chinese vinegar volume or larger Hengshun share implies more bottles.

Queries issued by the searcher: China customs HS 2209 vinegar exports United States 2024 volume value; UN Comtrade 220900 vinegar China exports USA; 恒顺醋业 2024年年度报告 境外营业收入 出口 占比; Hengshun vinegar overseas revenue export share of China vinegar exports

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p33 China HS 22090000 vinegar exports to the United States, quantity, cumulative 202 = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p34 China HS 22090000 vinegar exports to the United States, value, cumulative 2020-2 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p35 US share of China HS 22090000 vinegar export quantity, cumulative 2020-2022 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p36 Total China HS 22090000 vinegar exports worldwide, quantity, cumulative 2020-202 = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p37 Number of destination countries for China HS 22090000 vinegar exports, cumulativ = **129** countries (2020-01-01..2022-12-31) [DISCARD: Count of destination countries — no volume information.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p38 China HS 22090000 vinegar exports to Hong Kong, quantity, cumulative 2020-2022 ( = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p39 China HS 22090000 vinegar exports to Hong Kong, value, cumulative 2020-2022 = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p40 Hong Kong share of China HS 22090000 vinegar export quantity, cumulative 2020-20 = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p41 China HS 22090000 vinegar exports to Singapore, quantity, cumulative 2020-2022 = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p42 China HS 22090000 vinegar exports to Australia, quantity, cumulative 2020-2022 = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p43 China HS 22090000 vinegar exports to Netherlands, quantity, cumulative 2020-2022 = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p44 China HS 22090000 vinegar exports to Malaysia, quantity, cumulative 2020-2022 = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p45 China HS 22090000 vinegar exports to Canada, quantity, cumulative 2020-2022 = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p46 China HS 22090000 vinegar exports to Japan, quantity, cumulative 2020-2022 = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [physical_flow] US importer/distributor and retail-scan analyst

Hypothesis: US retail sales of Hengshun-branded vinegar (e.g., in Asian supermarkets, Amazon) in dollars divided by average retail bottle price gives bottles sold at retail; adjusted for retail-vs-import markup and inventory, this approximates import bottles. Direction: higher US retail dollar sales or lower bottle price implies more bottles.

Queries issued by the searcher: Hengshun vinegar Amazon US price bottle; 恒顺香醋 美国 销售 超市 价格; 恒顺醋业 2024年年报 境外 营业收入 出口; "Hengshun" vinegar export United States sales volume tons

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.sayweee.com/en/product/Hengshun-Zhenjiang-Vinegar/99090` -> **live_dated** (page date 2026-10-18); points raw/verified 0/0
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://foodmapnyc.com/blog/%E7%BE%8E%E5%9B%BD-%E6%81%92%E9%A1%BA%E9%A6%99%E9%86%8B-202011/` -> **live_dated** (page date 2020-11-01); points raw/verified 8/2
  - p47 Retail price range for Hengshun Xiangcu (Hengshun fragrant vinegar) in North Ame = **3** USD per bottle (2020-11-01..2020-11-01) [keep: ] quote: "价格:$3-$7"
  - p48 Retail price range for Hengshun Xiangcu (Hengshun fragrant vinegar) in North Ame = **7** USD per bottle (2020-11-01..2020-11-01) [keep: ] quote: "价格:$3-$7"
- dropped by code checks: 6 (number: no number in value_as_written: 2; period_end missing or unparseable: 4)

### d4 [capacity_consumption] Hengshun production/export operations analyst

Hypothesis: Hengshun's total vinegar production capacity times capacity utilisation gives total output; export share of output times US share of exports gives US-bound volume; divided by average bottle fill volume gives bottles. Direction: higher capacity, utilisation, export share, or US share implies more bottles.

Queries issued by the searcher: 恒顺醋业 产能 万吨 2024 年报; 恒顺醋业 出口 占比 美国 海外; 镇江香醋 出口 美国 市场 占比 食醋出口; Hengshun vinegar USA export distributor bottles 500ml Amazon

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://stock.stockstar.com/notice/SN2026041500001922.shtml` -> **live_dated** (page date 2026-04-15); points raw/verified 13/13
  - p49 Hengshun vinegar series (醋系列) sales revenue, 2024 = **126,560** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 132,109.25 126,559.63 4.38"
  - p50 Hengshun vinegar series (醋系列) sales revenue, 2025 = **132,109** 万元 (10,000 CNY) (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 132,109.25 126,559.63 4.38"
  - p51 Hengshun total sales revenue (all products), 2024 = **177,417** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "合计 179,867.41 177,417.43 1.38"
  - p52 Hengshun total sales revenue (all products), 2025 = **179,867** 万元 (10,000 CNY) (2025-01-01..2025-12-31) [keep: ] quote: "合计 179,867.41 177,417.43 1.38"
  - p53 Hengshun foreign trade (外贸模式) channel sales revenue, 2024 = **4,774** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "外贸模式 3,917.16 4,774.10 -17.95"
  - p54 Hengshun foreign trade (外贸模式) channel sales revenue, 2025 = **3,917** 万元 (10,000 CNY) (2025-01-01..2025-12-31) [keep: ] quote: "外贸模式 3,917.16 4,774.10 -17.95"
  - p55 Hengshun total sales revenue by channel (all channels), 2024 = **209,301** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "合计 226,646.62 209,300.68 8.29"
  - p56 Hengshun total sales revenue by channel (all channels), 2025 = **226,647** 万元 (10,000 CNY) (2025-01-01..2025-12-31) [keep: ] quote: "合计 226,646.62 209,300.68 8.29"
  - p57 Hengshun dealer (经销模式) channel sales revenue, 2024 = **194,145** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Dealer-channel revenue duplicate of p14; domestic.] quote: "经销模式 203,851.13 194,144.86 5.00"
  - p58 Hengshun direct sales (直销模式) channel sales revenue, 2024 = **10,382** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Direct-sales revenue duplicate of p13; domestic.] quote: "直销模式 18,878.32 10,381.72 81.84"
  - p59 Hengshun online sales revenue, 2024 = **27,438** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Online sales revenue duplicate of p15; domestic.] quote: "线上销售 30,323.15 27,437.81 10.52"
  - p60 Hengshun offline sales revenue, 2024 = **181,863** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Offline sales revenue — domestic channel total, not US export.] quote: "线下销售 196,323.46 181,862.87 7.95"
  - p61 Hengshun total number of dealers at end of 2025 = **2,107** 个 (dealers) (2025-12-31..2025-12-31) [DISCARD: Dealer count at end-2025 — irrelevant to US bottle volume.] quote: "合计 2107 266 173"
- `https://user.guancha.cn/main/content?id=1557862&s=fwzwyzzwzbt` -> **live_dated** (page date 2025-12-02); points raw/verified 15/10
  - p62 Hengshun vinegar-series production volume in 2024 = **210,600** tons (2024-01-01..2024-12-31) [keep: ] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨"
  - p63 Hengshun vinegar-series sales volume in 2024 = **212,700** tons (2024-01-01..2024-12-31) [keep: ] quote: "销量也超过21.27万吨"
  - p64 Hengshun total revenue in 2024 = **2,196,000,000** yuan (2024-01-01..2024-12-31) [keep: ] quote: "去年,其总营收为21.96亿元"
  - p65 Hengshun vinegar-series revenue in 2024 = **1,266,000,000** yuan (2024-01-01..2024-12-31) [keep: ] quote: "醋系列就实现12.66亿元,占据过半营收"
  - p66 Hengshun offline distributors covered nationwide as of end of 2024 = **1,700** distributors (2024-12-31..2024-12-31) [DISCARD: Duplicate of p29 (domestic distributors).] quote: "截至去年底,在线下渠道,恒顺醋业已经覆盖全国超1700家经销商"
  - p67 Hengshun terminal retail outlets as of end of 2024 = **350,000** outlets (2024-12-31..2024-12-31) [DISCARD: Duplicate of p30 (domestic outlets).] quote: "终端网点突破35万家"
  - p68 Hengshun self-media matrix cumulative followers as of end of 2024 = **280,000** followers (2024-12-31..2024-12-31) [DISCARD: Duplicate of p31 (followers).] quote: "截止去年底累计粉丝超28万"
  - p69 Hengshun research and pilot-test site area as of end of 2024 = **6,000** square meters (2024-12-31..2024-12-31) [DISCARD: Duplicate of p32 (R&D area).] quote: "截至去年底,恒顺醋业的研究实验场所和中试基地占地 6000多平方米"
  - p70 Hengshun high-end R&D equipment count as of end of 2024 = **50** sets (2024-12-31..2024-12-31) [DISCARD: R&D equipment count — irrelevant.] quote: "各类高端研发设备50余台套"
  - p71 Hengshun provincial-level and above research platforms as of end of 2024 = **6** platforms (2024-12-31..2024-12-31) [DISCARD: Research platform count — irrelevant.] quote: "省级以上科研平台6个"
- `https://max.book118.com/try_down/558011103137006073.pdf` -> **live_dated** (page date 2024-11-16); points raw/verified 15/10
  - p72 Zhenjiang vinegar export volume in 2015 (Zhenjiang Customs) = **280** tons (2015-01-01..2015-12-31) [keep: ] quote: "2015 280 25"
  - p73 Zhenjiang vinegar export volume in 2016 (Zhenjiang Customs) = **400** tons (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p74 Zhenjiang vinegar export volume in 2017 (Zhenjiang Customs) = **600** tons (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p75 Zhenjiang vinegar export volume in 2018 (Zhenjiang Customs) = **727** tons (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p76 Zhenjiang vinegar export volume in 2019 (Zhenjiang Customs) = **622** tons (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
  - p77 Zhenjiang vinegar export value in 2015 (Zhenjiang Customs) = **25** ten thousand USD (2015-01-01..2015-12-31) [keep: ] quote: "2015 280 25"
  - p78 Zhenjiang vinegar export value in 2016 (Zhenjiang Customs) = **36** ten thousand USD (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p79 Zhenjiang vinegar export value in 2017 (Zhenjiang Customs) = **55** ten thousand USD (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p80 Zhenjiang vinegar export value in 2018 (Zhenjiang Customs) = **66.7** ten thousand USD (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p81 Zhenjiang vinegar export value in 2019 (Zhenjiang Customs) = **58.6** ten thousand USD (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
- dropped by code checks: 10 (period year 2025 does not appear in the page text or URL (likely mis-dated): 4; number: no number in value_as_written: 1; period_end missing or unparseable: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; number: more than one number in value_as_written: 1)

### d5 [base_rates] Packaging/conversion-factor analyst

Hypothesis: Converting any volume estimate (tons or liters) to bottles requires average bottle size and density of vinegar (~1.01 kg/L); export bottles are typically 500 mL. Direction: smaller assumed bottle size implies more bottles per ton.

Queries issued by the searcher: Hengshun vinegar 500ml bottle export; 恒顺香醋 出口 500ml 瓶; vinegar density kg per liter 1.01 g/mL acetic acid solution; 恒顺醋业 2024年年报 境外收入 出口 营业收入

- `https://fivecontinentsintl.com/en/product/hengshun-brand-9-degrees-rice-vinegar/` -> **live_dated** (page date 2024-11-01); points raw/verified 11/11
  - p82 HengShun Brand 9 Degrees Rice Vinegar bottle size (500ml) = **500** mL per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p83 HengShun Brand 9 Degrees Rice Vinegar case pack (bottles per case) = **12** bottles per case (..) [keep: ] quote: "Case Size: 500ml*12btls"
  - p84 HengShun Brand Six Years Vinegar bottle size (580ml) = **580** mL per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p85 HengShun Brand Three Years Vinegar bottle size (580ml) = **580** mL per bottle (..) [keep: ] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p86 HengShun Brand Vinegar 0 Additives bottle size (500ml) = **500** mL per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p87 HengShun Brand Vinegar 0 Additives bottle size (535ml) = **535** mL per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p88 HengShun Brand Vinegar for Dumpling bottle size (500ml) = **500** mL per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p89 HengShun Brand Vinegar for Steamed Buns bottle size (550ml) = **550** mL per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p90 HengShun Brand White Rice Vinegar bottle size (500ml) = **500** mL per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p91 HengShun Brand Zhenjiang Eight Years Vinegar bottle size (300ml) = **300** mL per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
  - p92 HengShun Brand Cooking Wine with Shallot And Ginger bottle size (500ml) = **500** mL per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
- `https://www.weee.com/vi/product/Hengshun-9-Degree-Rice-Vinegar/28868` -> **live_dated** (page date 2026-10-18); points raw/verified 4/4
  - p93 Hengshun Rice Vinegar 9° bottle size listed on Weee! product page = **500** mL (..) [keep: ] quote: "Giấm Gạo 9°Hengshun 500 ml"
  - p94 Hengshun Rice Vinegar 9° 500 mL bottle price on Weee! (USD) = **3** USD (..) [keep: ] quote: "Giấm Gạo 9°Hengshun 500 ml $ 3 29"
  - p95 Hengshun Rice Vinegar 9° 500 mL bottle price cents portion on Weee! (USD) = **29** USD cents (..) [DISCARD: Cents portion of the $3.29 price; redundant with p94.] quote: "Giấm Gạo 9°Hengshun 500 ml $ 3 29"
  - p96 Hengshun Rice Vinegar 9° unit price per fluid ounce on Weee! (USD) = **0.19** USD per fl.oz (..) [DISCARD: Per-fluid-ounce price; redundant with p94 and adds no bottle-count information.] quote: "$0.19/fl.oz"
- `https://www.jd.com/chanpin/2284470.html` -> **live_dated** (page date 2015-01-01); points raw/verified 7/7
  - p97 Hengshun Cu Li Jian Feng Gu gift box vinegar bottle size (6.4 degree, 200ml per  = **200** mL per bottle (..) [DISCARD: 200 mL gift-box bottle — a niche domestic gift SKU, not representative of US export bottles.] quote: "恒顺醋里见风骨礼盒6.4度200ml*3瓶【0添加】 中华老字号中秋年货礼盒"
  - p98 Hengshun Cu Li Jian Feng Gu gift box bottle count per pack = **3** bottles per gift box (..) [DISCARD: Gift-box pack count — tied to the discarded p97 SKU.] quote: "恒顺醋里见风骨礼盒6.4度200ml*3瓶【0添加】 中华老字号中秋年货礼盒"
  - p99 Hengshun three-year aged Xiangcu bottle size (Zhenjiang specialty) = **580** mL per bottle (..) [keep: ] quote: "恒顺香醋凉拌炒菜煲汤蘸汁酿造工艺镇江特产0添加防腐剂 三年陈香醋580ml"
  - p100 Hengshun Zhenjiang Xiangcu bottle size = **500** mL per bottle (..) [keep: ] quote: "恒顺香醋凉拌炒菜煲汤蘸汁酿造工艺镇江特产0添加防腐剂 镇江-香醋500ml"
  - p101 Jin Hengshun Xiangcu bottle size = **550** mL per bottle (..) [keep: ] quote: "恒顺香醋凉拌炒菜煲汤蘸汁酿造工艺镇江特产0添加防腐剂 金恒顺香醋550ml"
  - p102 Hengshun B Xiangcu bottle size = **500** mL per bottle (..) [keep: ] quote: "恒顺香醋凉拌炒菜煲汤蘸汁酿造工艺镇江特产0添加防腐剂 B香醋500ml"
  - p103 Hengshun Youji (premium grade) Xiangcu bottle size = **500** mL per bottle (..) [keep: ] quote: "恒顺香醋凉拌炒菜煲汤蘸汁酿造工艺镇江特产0添加防腐剂 优级香醋500ml"
- `https://www.pearson.com/channels/general-chemistry/asset/35963978/assuming-the-density-of-a-5-by-mass-acetic-ac` -> **live_dated** (page date 2025-05-01); points raw/verified 5/5
  - p104 Density of a 5% (by mass) acetic acid solution = **1.01** g/cm^3 (..) [keep: ] quote: "Assuming the density of a 5% (by mass) acetic acid solution is 1.01 g/cm^3"
  - p105 Volume of acetic acid solution in the worked example = **250** mL (..) [DISCARD: Worked-example volume in a chemistry problem — irrelevant.] quote: "what is the mass of acetic acid present in 250 mL of this solution?"
  - p106 Mass percent concentration of acetic acid in the solution = **5** % by mass (..) [DISCARD: 5% acetic-acid concentration — not needed; density alone suffices.] quote: "Assuming the density of a 5% (by mass) acetic acid solution is 1.01 g/cm^3"
  - p107 Density of an unspecified lab liquid in the multiple-choice question = **1.24** g/cm^3 (..) [DISCARD: Density of an unrelated lab liquid (1.24 g/cm³) — misleading for vinegar.] quote: "A liquid in the lab has a density of 1.24 g/cm^3."
  - p108 Volume of the unspecified lab liquid in the multiple-choice question = **250** mL (..) [DISCARD: Volume in an unrelated lab problem — irrelevant.] quote: "What is the mass of 250 mL of this liquid?"

### d6 [persona] US-based Chinese-grocery distributor / importer

Hypothesis: Interviews or trade press with US importers/distributors of Chinese vinegar reveal order volumes or container counts for Hengshun; containers per year times bottles per container gives bottles. Direction: more containers or larger orders imply more bottles.

Queries issued by the searcher: Hengshun vinegar US distributor importer; 镇江香醋 美国 进口商 集装箱 恒顺; importgenius "Jiangsu Hengshun" shipments 2024 vinegar bill of lading container; panjiva Jiangsu Hengshun International Trade vinegar shipments Walong Marketing

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 8/5
  - p109 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24, a = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p110 Bottle size and pack configuration stated in cargo description: 550 mL bottles p = **550** mL per bottle (packed @24) (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p111 Container length in cm for the 20-foot general purpose container on bill of ladi = **240** cm (container length) (2022-08-13..2022-08-13) [DISCARD: Container length 240 cm is not a real 20-ft container dimension; unusable.] quote: "Length 240"
  - p112 Container height in cm for the 20-foot general purpose container on bill of ladi = **102** cm (container height) (2022-08-13..2022-08-13) [DISCARD: Container height 102 cm — implausible/garbled; unusable.] quote: "Height 102"
  - p113 Container width in cm for the 20-foot general purpose container on bill of ladin = **96** cm (container width) (2022-08-13..2022-08-13) [DISCARD: Container width 96 cm — implausible/garbled; unusable.] quote: "Width 96"
- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **live_dated** (page date 2024-11-01); points raw/verified 2/0
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 3; period_end missing or unparseable: 2)

### d7 [shocks] Trade-policy and market-access analyst

Hypothesis: US-China tariff changes, shipping costs, and COVID-era disruptions alter Hengshun's US export volumes; identifying the direction and magnitude of these effects constrains which years are representative and whether 2024 volumes deviate from trend. Direction: tariff increases or shipping disruptions reduce US-bound bottles.

Queries issued by the searcher: US tariff Chinese vinegar HS 2209 Section 301; 恒顺 美国 关税 影响 出口; China US shipping cost 2024 container freight index food exports; 恒顺醋业 2024年年度报告 境外 营业收入 出口; USTR Section 301 List 3 vinegar 2209 25 percent final list September 2018; 恒顺醋业 美国市场 出口 占比 关税 投资者关系

- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 8/0
- `https://agmanager.info/sites/default/files/pdf/Allen_Exports_03-01-24.pdf` -> **live_dated** (page date 2024-03-01); points raw/verified 0/0
- `https://kxstock.hexun.com/2024-05-14/212845455.html` -> **live_dated** (page date 2024-05-14); points raw/verified 0/0
- `http://images.mofcom.gov.cn/bn/202201/20220117154403707.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 8 (period year 2024 does not appear in the page text or URL (likely mis-dated): 8)

### d8 [forecasts_markets] Company guidance and strategy analyst

Hypothesis: Hengshun's stated internationalization/export growth targets and any disclosed overseas expansion plans indicate the trajectory of export volumes, helping bound the US share and growth. Direction: aggressive overseas targets imply higher recent and future US volumes.

Queries issued by the searcher: 恒顺醋业 海外 市场 拓展 出口 目标; Hengshun vinegar international expansion export growth overseas markets; 恒顺醋业 2024年报 外贸 出口 营业收入 亿元; Zhenjiang vinegar exports United States share 镇江香醋 出口 美国 占比

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://stock.hexun.com/2026-04-20/224024413.html` -> **live_dated** (page date 2026-04-20); points raw/verified 0/0
- `https://www.sdlib.com.cn/home/sdms/detail/id/139061.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0

### b1 [related_series] customs/trade data

Hypothesis: Annual (2023-2024) China HS 22090000 vinegar export volume and value to the US, plus the share attributable to Jiangsu/Zhenjiang-origin exporters, would convert the kept 2020-2022 cumulative customs figures (p33-p36) into a 2024 US-bound volume and let us apply a Hengshun share. This is the single missing input that completes the d2 route.

Queries issued by the searcher: UN Comtrade HS 2209 China exports to United States 2024 quantity liters vinegar; 中国海关 22090000 醋 出口 美国 2024 数量 金额; hs.bianmachaxun.com 22090000 美国 出口 总量 升; 镇江 醋 出口 2024 海关 统计 恒顺 出口量

- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 14/14
  - p114 China HS 22090000 vinegar total export volume, 2023 full year = **21,832,831** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p115 China HS 22090000 vinegar total export value, 2023 full year = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p116 China HS 22090000 vinegar total export volume, 2024 full year = **25,760,168** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p117 China HS 22090000 vinegar total export value, 2024 full year = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p118 China HS 22090000 vinegar average export price per liter, 2024 full year = **1.15** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p119 China HS 22090000 vinegar average export price per liter, 2023 full year = **1.18** USD per liter (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p120 China HS 22090000 vinegar total export volume, 2022 full year = **19,604,254** liters (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p121 China HS 22090000 vinegar total export value, 2022 full year = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p122 China HS 22090000 vinegar total export volume, 2021 full year = **20,249,374** liters (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p123 China HS 22090000 vinegar total export value, 2021 full year = **25,590,784** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p124 China HS 22090000 vinegar total export volume, 2020 full year = **17,414,624** liters (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
  - p125 China HS 22090000 vinegar total export value, 2020 full year = **23,362,688** USD (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
  - p126 China HS 22090000 vinegar total export volume, 2025 full year = **25,428,030** liters (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025年 1月-12月份 \| 25428030 \| $28176312 \| $1.11 \| 导出 \|"
  - p127 China HS 22090000 vinegar total export value, 2025 full year = **28,176,312** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025年 1月-12月份 \| 25428030 \| $28176312 \| $1.11 \| 导出 \|"
- `https://www.jcksj.com/report/22090000.html` -> **live_dated** (page date 2026-09-08); points raw/verified 15/15
  - p128 China HS 22090000 vinegar exports to the United States, 2024, value in USD = **4,992,092** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p129 China HS 22090000 vinegar exports to the United States, 2025, value in USD = **3,787,074** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p130 Year-on-year change in China HS 22090000 vinegar exports to the United States, 2 = **-24.14** % (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p131 China HS 22090000 vinegar total exports, 2024, value in USD = **29,676,894** USD (2024-01-01..2024-12-31) [keep: ] quote: "2024 29,676,894 美元29676894"
  - p132 China HS 22090000 vinegar total exports, 2025, value in USD = **27,891,245** USD (2025-01-01..2025-12-31) [keep: ] quote: "2025 27,891,245 美元27891245"
  - p133 China HS 22090000 vinegar total exports, 2025, value in ten-thousand USD = **27,891,200** USD (ten-thousand) (2025-01-01..2025-12-31) [keep: ] quote: "2789.12万美元"
  - p134 Year-on-year change in China HS 22090000 vinegar total exports, 2025 vs 2024 = **-6.02** % (2025-01-01..2025-12-31) [keep: ] quote: "较2024年-6.02%"
  - p135 China HS 22090000 vinegar total imports, 2024, value in USD = **9,806,210** USD (2024-01-01..2024-12-31) [keep: ] quote: "2024 9,806,210 美元9806210"
  - p136 China HS 22090000 vinegar total imports, 2025, value in USD = **11,979,467** USD (2025-01-01..2025-12-31) [keep: ] quote: "2025 11,979,467 美元11979467"
  - p137 China HS 22090000 vinegar imports from the United States, 2024, value in USD = **2,269,319** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p138 China HS 22090000 vinegar imports from the United States, 2025, value in USD = **1,875,118** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p139 China HS 22090000 vinegar exports to Hong Kong, 2024, value in USD = **4,093,608** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 中国香港 \| 4,205,407 \| 4,093,608 \| +111,799 \| +2.73% \| 查询该市场买家 ↗ \|"
  - p140 China HS 22090000 vinegar exports to Australia, 2024, value in USD = **1,959,491** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 澳大利亚 \| 2,079,038 \| 1,959,491 \| +119,547 \| +6.10% \| 查询该市场买家 ↗ \|"
  - p141 China HS 22090000 vinegar exports to the Netherlands, 2024, value in USD = **2,398,669** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 荷兰 \| 2,153,886 \| 2,398,669 \| -244,783 \| -10.20% \| 查询该市场买家 ↗ \|"
  - p142 China HS 22090000 vinegar exports to Singapore, 2024, value in USD = **1,493,383** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 新加坡 \| 1,654,888 \| 1,493,383 \| +161,505 \| +10.81% \| 查询该市场买家 ↗ \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p143 Cumulative HS22090000 vinegar exports to the United States, volume (2020-01 to 2 = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p144 Cumulative HS22090000 vinegar exports to the United States, value (2020-01 to 20 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p145 US share of cumulative HS22090000 vinegar export volume (2020-01 to 2022-12) = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p146 Cumulative HS22090000 vinegar exports worldwide, volume (2020-01 to 2022-12) = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p147 Number of destination countries for cumulative HS22090000 vinegar exports (2020- = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p148 Cumulative HS22090000 vinegar exports to Hong Kong, volume (2020-01 to 2022-12) = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p149 Cumulative HS22090000 vinegar exports to Hong Kong, value (2020-01 to 2022-12) = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p150 Hong Kong share of cumulative HS22090000 vinegar export volume (2020-01 to 2022- = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p151 Cumulative HS22090000 vinegar exports to Singapore, volume (2020-01 to 2022-12) = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p152 Cumulative HS22090000 vinegar exports to Australia, volume (2020-01 to 2022-12) = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p153 Cumulative HS22090000 vinegar exports to Netherlands, volume (2020-01 to 2022-12 = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p154 Cumulative HS22090000 vinegar exports to Malaysia, volume (2020-01 to 2022-12) = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p155 Cumulative HS22090000 vinegar exports to Canada, volume (2020-01 to 2022-12) = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p156 Cumulative HS22090000 vinegar exports to Japan, volume (2020-01 to 2022-12) = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b2 [own_history] company disclosure

Hypothesis: Hengshun annual report segment note splitting 外贸/overseas revenue by product (vinegar vs sauce vs wine) and by destination region (North America/US share) would let us apply the export-revenue anchor (p4) directly to vinegar and to the US, removing the two largest transfer assumptions in the d1 route.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外 收入 分地区; Hengshun Vinegar 2024 annual report overseas revenue by region; 恒顺醋业 2024年 境外地区 营业收入 839.98万元 出口 美国; 恒顺醋业 2024年报 主营业务分地区 境内 境外 营业收入 毛利率

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2109609107272691712` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-

### b3 [persona] US importer/distributor

Hypothesis: US importer order volumes or container counts for Hengshun-branded vinegar (e.g., from import bills of lading naming Hengshun or its US distributors) would give a direct physical-flow estimate (d6) and cross-check the revenue-derived bottle count.

Queries issued by the searcher: ImportYeti Hengshun vinegar shipments USA; Panjiva Hengshun Chinkiang vinegar consignee 2024; 52wmb well luck hengshun vinegar 2024 提单 重量; 恒顺 香醋 出口 美国 集装箱 进口商

- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/7
  - p157 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 sh = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p158 Bottle size in cargo description for Chinkiang vinegar (550ML@24 packing) = **550** milliliters per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p159 Bottles per case in cargo description (550ML@24 packing) = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p160 Container length in centimeters on bill of lading EGLV142252207486 = **240** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p161 Container height in centimeters on bill of lading EGLV142252207486 = **102** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p162 Container width in centimeters on bill of lading EGLV142252207486 = **96** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
  - p163 Container type on bill of lading EGLV142252207486 (20 foot general purpose) = **20** foot container (2022-08-13..2022-08-13) [keep: ] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us', 'zhenjiang vinegar sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p16', 'p17', 'p28', 'p49', 'p50', 'p65'] All report Hengshun vinegar-series (醋系列) revenue: 2024 ≈ 12.66亿元 and 2023 ≈ 12.94亿元. p1/p2/p49/p50 are the same Sina/Stockstar annual-report table (shared underlying source, not independent); p16/p17 
- corroborating: ['p4', 'p5', 'p53', 'p54'] Foreign-trade (外贸模式) channel revenue: 2024 ≈ 4,774万元, 2023 ≈ 4,513万元, 2025 ≈ 3,917万元. p4/p5 and p53/p54 are the same annual-report channel table from two aggregators; treat as one source. This is the 
- corroborating: ['p7', 'p8', 'p55', 'p56', 'p9', 'p10', 'p51', 'p52', 'p18', 'p19', 'p27', 'p64'] Total revenue ~21.96亿元 (2024) / 21.06亿元 (2023) appears in several tables with different subtotals (by-channel 209,301万 vs by-product 177,417万 vs operating revenue 21.96亿). These are different table sc
- corroborating: ['p25', 'p26', 'p62', 'p63'] Vinegar-series production 21.06万吨 and sales 21.27万吨 in 2024, from a single guancha article (duplicated ids). Gives a physical volume anchor for the vinegar segment.
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] One customs-derived dataset (m.x315.cn) for HS 22090000 exports, cumulative 2020-2022: US 6.60 million L (11.35% of 58.1 million L worldwide). Internally consistent; single source, three-year cumulati
- corroborating: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Zhenjiang Customs series of Zhenjiang vinegar exports 2015-2019 (280→622 t, ~$0.9-1.0/kg). Consistent internally but old, city-wide (all Zhenjiang producers), and all destinations — usable only as a s
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p99', 'p100', 'p101', 'p102', 'p103'] Hengshun export/US retail bottle sizes cluster at 500-580 mL, mostly 500 mL; supports a ~500 mL average bottle assumption with a modest spread.
- corroborating: ['p47', 'p48', 'p94', 'p95', 'p96'] US retail prices for Hengshun 500 mL vinegar: $3-$7 (2020) and $3.29 (2026 Weee). Consistent order of magnitude; retail, not import, price.
- corroborating: ['p109', 'p110', 'p111', 'p112', 'p113'] One bill of lading for Chinkiang (not Hengshun-branded) vinegar, 550 mL×24; container dimensions are garbled (240×102×96 cm is not a real 20-ft box). Illustrates pack configuration only; cannot anchor
- corroborating: ['p104', 'p105', 'p106', 'p107', 'p108'] Density ~1.01 g/cm³ for dilute acetic acid; supports ton↔liter conversion. p107/p108 (1.24 g/cm³ lab liquid) are a different substance and irrelevant.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p16', 'p17', 'p28', 'p49', 'p65'] All report Hengshun vinegar-series (醋系列) revenue: 2024 ≈12.66亿元 and 2023 ≈12.94亿元. p1/p2 (Sina), p16/p17 (lhratings), p28/p65 (guancha), p49 (stockstar) are the same annual-report figure re-reported; 
- corroborating: ['p4', 'p5', 'p53', 'p54'] Foreign-trade (外贸模式) channel revenue: 2024 ≈4,774万元, 2023 ≈4,513万元. p4/p5 and p53/p54 agree; same underlying annual-report disclosure, so not independent.
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p18', 'p19', 'p27', 'p51', 'p52', 'p55', 'p56', 'p64'] Total revenue figures (~21.96亿 by one table, ~17.74亿 by product-category table, ~20.93亿 by channel table). These are different tables/definitions of 'total' (operating revenue vs product-category sum 
- corroborating: ['p25', 'p26', 'p62', 'p63'] Vinegar-series production 21.06万吨 and sales 21.27万吨 in 2024; p25/p62 and p26/p63 are duplicate reports of the same figures.
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p143', 'p144', 'p145', 'p146'] Cumulative 2020-2022 HS22090000 export totals and US share; p33-p36 and p143-p146 are duplicate copies of the same x315.cn dataset.
- corroborating: ['p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p131', 'p132', 'p133', 'p134'] National HS22090000 total export volume/value by year from two customs aggregators (bianmachaxun and jcksj); values agree closely (2024 ~29.6M USD, 2025 ~27.9M USD), so they corroborate the national t
- corroborating: ['p128', 'p129', 'p130'] US-bound HS22090000 value: 2024 ≈4.99M USD, 2025 ≈3.79M USD, -24.14% YoY; internally consistent single-source series.
- corroborating: ['p109', 'p110', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163'] Single bill-of-lading record (EGLV142252207486): 700 pieces, 550mL@24 Chinkiang vinegar, 20-ft container. p109/p110 and p157-p163 are the same shipment; useful only as a pack-size/container analogue, 
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p99', 'p100', 'p101', 'p102', 'p103'] Hengshun export/retail bottle sizes cluster at 500-580 mL (mostly 500 mL); consistent pack-size evidence for a bottle-size conversion.
- corroborating: ['p47', 'p48', 'p94'] US retail price of Hengshun vinegar ~$3-$7 per bottle (2020) and $3.29 for 500 mL (2026); consistent order of magnitude for a retail-value cross-check.
- corroborating: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Zhenjiang Customs vinegar export volume/value 2015-2019 (280-727 t, $25-67万). Old and city-wide (not Hengshun-only), but internally consistent and useful as a scale/trend analogue.
- corroborating: ['p1', 'p4'] Vinegar revenue (12.66亿) and foreign-trade revenue (4,774万) are from the same annual report; foreign trade is ~3.8% of vinegar revenue, a key ratio for the d1 route.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a3 | Average export bottle fill volume | 520 | 450..600 | 367..735 (widened) | mL | m1 (m2) | Hengshun export/US SKUs observed at 500, 535, 550, 580 mL (p82-p92, p99-p103), with 500 mL most common; a volume-weighted average slightly above 500 mL reflects the mix. | US-bound Hengshun product is in the 500-580 mL range typical of its US SKUs. | Evidence that US-bound Hengshun product is predominantly small (200-300 mL) or bulk packaging. |
| a5 | Hengshun share of China HS22090000 vinegar export value | 12 | 6..22 | 6..22 | % | m1 (m2) | Hengshun is the largest branded Chinese vinegar exporter but its customs-recorded HS22090000 exports are a modest share of the ~$29.7M national total (p131); the company's 外贸模式 revenue (p4) is booked at company value and includes non-vinegar and possibly HK-routed trade, so it cannot be taken at fac | Hengshun's customs-recorded vinegar exports are a leading but minority share of national HS22090000 exports. | Customs or company data showing Hengshun's vinegar exports are <3% or >30% of national HS22090000 exports. |
| a7 | US share of Hengshun's HS22090000 vinegar export value | 25 | 12..45 | 12..45 | % | m1 (m2) | National HS22090000 data put the US at ~11-17% of China's vinegar export value (p128 vs p131; p35), but Hengshun is a premium branded exporter with stronger US retail presence than the average Chinese exporter, so its US share should sit above the national average. Range spans a national-average-lik | Hengshun's export destinations are spread roughly in line with branded Chinese vinegar trade, with the US a leading single market. | Evidence that Hengshun's US sales are <5% or >60% of its vinegar export value. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 223,313 | ['p128', 'p118'] / ['a3', 'a5', 'a7'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **223,313** bottle/year, 80% interval [80,147, 622,212] bottle/year, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 18 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 5 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p1 | Hengshun vinegar series (醋系列) sales revenue, 2024 | 1,265,596,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Revenue in CNY for all vinegar series, not a count of bottles exported to the US; wrong measure and scope. |
| p4 | Hengshun foreign trade (外贸模式) sales revenue, 2024 | 47,741,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Foreign-trade channel revenue in CNY for all products, not bottle count to the US; wrong measure and scope. |
| p7 | Hengshun total sales revenue (all products, by sales mode), 2024 | 2,093,006,800 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Total company revenue by sales mode, not bottles exported to the US; wrong measure and broader scope. |
| p9 | Hengshun total revenue (product category table), 2024 | 1,774,174,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Total revenue by product category, not bottle count to the US; wrong measure and scope. |
| p16 | Hengshun CuYe vinegar series (醋系列) revenue 2024 | 12.66 | 亿元 (100 million RMB) | 2024-01-01..2024-12-31 | www.lhratings.com | different | Vinegar-series revenue in RMB, not bottles exported to the US; wrong measure and scope. |
| p18 | Hengshun CuYe total operating revenue 2024 | 21.96 | 亿元 (100 million RMB) | 2024-01-01..2024-12-31 | www.lhratings.com | different | Total operating revenue, not bottle count to the US; wrong measure and broader scope. |
| p25 | Hengshun vinegar-series production volume, 2024 | 210,600 | tons | 2024-01-01..2024-12-31 | user.guancha.cn | different | Production volume in tons, not bottles exported to the US; wrong measure and scope. |
| p26 | Hengshun vinegar-series sales volume, 2024 | 212,700 | tons | 2024-01-01..2024-12-31 | user.guancha.cn | different | Sales volume in tons, not bottles exported to the US; wrong measure and scope. |
| p27 | Hengshun total revenue, 2024 | 2,196,000,000 | yuan (RMB) | 2024-01-01..2024-12-31 | user.guancha.cn | different | Total revenue in yuan, not bottle count to the US; wrong measure and broader scope. |
| p28 | Hengshun vinegar-series revenue, 2024 | 1,266,000,000 | yuan (RMB) | 2024-01-01..2024-12-31 | user.guancha.cn | different | Vinegar-series revenue in yuan, not bottles exported to the US; wrong measure and scope. |
| p49 | Hengshun vinegar series (醋系列) sales revenue, 2024 | 126,560 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | stock.stockstar.com | different | Vinegar-series revenue in CNY, not bottle count to the US; wrong measure and scope. |
| p51 | Hengshun total sales revenue (all products), 2024 | 177,417 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | stock.stockstar.com | different | Total sales revenue, not bottle count to the US; wrong measure and broader scope. |
| p53 | Hengshun foreign trade (外贸模式) channel sales revenue, 2024 | 4,774 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | stock.stockstar.com | different | Foreign-trade channel revenue in CNY, not bottle count to the US; wrong measure and scope. |
| p55 | Hengshun total sales revenue by channel (all channels), 2024 | 209,301 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | stock.stockstar.com | different | Total revenue by channel, not bottle count to the US; wrong measure and broader scope. |
| p62 | Hengshun vinegar-series production volume in 2024 | 210,600 | tons | 2024-01-01..2024-12-31 | user.guancha.cn | different | Production volume in tons, not bottles exported to the US; wrong measure and scope. |
| p63 | Hengshun vinegar-series sales volume in 2024 | 212,700 | tons | 2024-01-01..2024-12-31 | user.guancha.cn | different | Sales volume in tons, not bottles exported to the US; wrong measure and scope. |
| p64 | Hengshun total revenue in 2024 | 2,196,000,000 | yuan | 2024-01-01..2024-12-31 | user.guancha.cn | different | Total revenue in yuan, not bottle count to the US; wrong measure and broader scope. |
| p65 | Hengshun vinegar-series revenue in 2024 | 1,266,000,000 | yuan | 2024-01-01..2024-12-31 | user.guancha.cn | different | Vinegar-series revenue in yuan, not bottles exported to the US; wrong measure and scope. |


## Final answer

Best estimate: 223,313 bottle/year of Hengshun bottled vinegar exported to the United States in calendar year 2024, all bottled types combined, counted as physical bottles (80% model-based interval 80,147 to 622,212 bottle/year).

Evidence chain: observed China HS [n] vinegar exports to the US in 2024 were 4,992,092 USD, at an observed national average export price of 1.15 USD per liter. Dividing value by price gives liters; applying Hengshun's assumed share of national vinegar export value (12%, range 6% to 22%), the assumed US share of Hengshun's exports (25%, range 12% to 45%), and an assumed average fill of 520 mL (range 367 to 735) yields bottles. Only the two customs points are observed; the three shares/fill factors are analyst assumptions, so the result is conditional.

Code used a single method (223,313 bottle/year, weight 100%), so no combination rationale applies. The biggest risk is that Hengshun's true customs-recorded export share and US share are unverified. Company-level export disclosures or US import records by brand would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a3 Average export bottle fill volume: 520 mL, range 367 to 735 (range widened by code); used by m1. Overturned by: Evidence that US-bound Hengshun product is predominantly small ([n]-[n] mL) or bulk packaging.
- a5 Hengshun share of China HS[n] vinegar export value: 12%, range 6% to 22%; used by m1. Overturned by: Customs or company data showing Hengshun's vinegar exports are <[n] or >[n] of national HS[n] exports.
- a7 US share of Hengshun's HS[n] vinegar export value: 25%, range 12% to 45%; used by m1. Overturned by: Evidence that Hengshun's US sales are <[n] or >[n] of its vinegar export value.

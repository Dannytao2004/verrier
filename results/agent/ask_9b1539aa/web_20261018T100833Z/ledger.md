# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (Jiangsu Hengshun Vinegar-Industry Co., Ltd.) vinegar sold/exported to the United States in a full year, all bottled vinegar types combined, counted as physical bottles (not cases, not liters, not revenue) | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; Hengshun annual reports (Shanghai-listed, 600305) disclose export revenue/volume by region only in aggregate, not US bottle counts

## Directions and pages

### d1 [related_series] Hengshun corporate disclosure

Hypothesis: Hengshun annual/interim reports disclose total export revenue and possibly export volume; US share of exports can be bridged via regional breakdown or customs data. Bottles = US export volume / avg bottle size.

Queries issued by the searcher: 恒顺醋业 年报 出口 销量 吨 国外; Hengshun Vinegar annual report export volume North America revenue; 恒顺醋业 2024年年度与行业相关的定期经营数据公告 外贸模式 销售收入; 恒顺 美国 子公司 销售收入 境外 营业收入 2024 年报

- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 15/2
  - p1 Hengshun foreign trade revenue YoY change, FY2024 vs FY2023 = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p2 Hengshun total dealer count at end of FY2024 = **2,014** 个 (dealers) (2024-12-31..2024-12-31) [DISCARD: Domestic dealer count; no bearing on US bottle volume and cannot enter any route.] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1974663940947992576` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://stock.tianyancha.com/ResearchReport/eastmoney/dda07ea1866cc216e7eadadd8c442cd6.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 13 (scale word '万元' not supported by quote or table header: 13)

### d2 [physical_flow] China customs trade statistics

Hypothesis: China customs HS code 2209 (vinegar) exports to US give total Chinese vinegar export volume to US; Hengshun's share of China vinegar exports (by value/volume) times that total gives Hengshun US volume; divide by bottle size.

Queries issued by the searcher: China vinegar exports United States HS 220900 volume value; 中国 醋 出口 美国 海关 2209 数量 吨; 恒顺醋业 出口 美国 数量 年报 境外收入; Hengshun Vinegar export revenue annual report overseas sales 2024

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p3 China HS22090000 vinegar exports to United States, volume, cumulative 2020-01 to = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p4 China HS22090000 vinegar exports to United States, value, cumulative 2020-01 to  = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p5 United States share of China HS22090000 vinegar export volume, cumulative 2020-0 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p6 China HS22090000 vinegar exports worldwide, total volume, cumulative 2020-01 to  = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p7 Number of destination countries for China HS22090000 vinegar exports, cumulative = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p8 China HS22090000 vinegar exports to Hong Kong, volume, cumulative 2020-01 to 202 = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p9 China HS22090000 vinegar exports to Hong Kong, value, cumulative 2020-01 to 2022 = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p10 Hong Kong share of China HS22090000 vinegar export volume, cumulative 2020-01 to = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p11 China HS22090000 vinegar exports to Singapore, volume, cumulative 2020-01 to 202 = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p12 China HS22090000 vinegar exports to Australia, volume, cumulative 2020-01 to 202 = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p13 China HS22090000 vinegar exports to Netherlands, volume, cumulative 2020-01 to 2 = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p14 China HS22090000 vinegar exports to Malaysia, volume, cumulative 2020-01 to 2022 = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p15 China HS22090000 vinegar exports to Canada, volume, cumulative 2020-01 to 2022-1 = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p16 China HS22090000 vinegar exports to Japan, volume, cumulative 2020-01 to 2022-12 = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://m.x315.cn/doc/wsK8k8` -> **live_dated** (page date 2021-07-28); points raw/verified 15/15
  - p17 China HS22090000 vinegar exports to United States, trade volume (2019-07 to 2020 = **4,378,300** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p18 China HS22090000 vinegar exports to United States, trade value (2019-07 to 2020- = **5,156,000** USD (万美元 = ten-thousand USD) (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p19 Average export price of China HS22090000 vinegar to United States (2019-07 to 20 = **1.18** USD per liter (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p20 Number of destination countries/regions for China HS22090000 vinegar exports = **114** countries/regions (2019-07-01..2020-06-30) [keep: ] quote: "中国HS22090000的主要出口国/地区有114个,相关贸易数据如下:"
  - p21 China HS22090000 vinegar exports to Australia, trade volume (2019-07 to 2020-06) = **2,319,000** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 2 \| 澳大利亚 \| 231.90 万升 \| 359.41 万美元 \| 1.55 美元/升 \|"
  - p22 China HS22090000 vinegar exports to Singapore, trade volume (2019-07 to 2020-06) = **2,763,900** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 3 \| 新加坡 \| 276.39 万升 \| 289.36 万美元 \| 1.05 美元/升 \|"
  - p23 China HS22090000 vinegar exports to Malaysia, trade volume (2019-07 to 2020-06) = **2,126,100** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 4 \| 马来西亚 \| 212.61 万升 \| 246.69 万美元 \| 1.16 美元/升 \|"
  - p24 China HS22090000 vinegar exports to Netherlands, trade volume (2019-07 to 2020-0 = **1,673,000** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 5 \| 荷兰 \| 167.30 万升 \| 245.41 万美元 \| 1.47 美元/升 \|"
  - p25 China HS22090000 vinegar exports to Japan, trade volume (2019-07 to 2020-06) = **1,593,300** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 6 \| 日本 \| 159.33 万升 \| 211.71 万美元 \| 1.33 美元/升 \|"
  - p26 China HS22090000 vinegar exports to Canada, trade volume (2019-07 to 2020-06) = **1,533,400** liters (万升 = ten-thousand liters) (2019-07-01..2020-06-30) [keep: ] quote: "\| 7 \| 加拿大 \| 153.34 万升 \| 202.81 万美元 \| 1.32 美元/升 \|"
  - p27 China HS22090000 vinegar exports to France, trade volume (2019-07 to 2020-06) = **987,475** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 8 \| 法国 \| 987475 升 \| 116.91 万美元 \| 1.18 美元/升 \|"
  - p28 China HS22090000 vinegar exports to Russia, trade volume (2019-07 to 2020-06) = **924,261** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 9 \| 俄罗斯联邦 \| 924261 升 \| 111.84 万美元 \| 1.21 美元/升 \|"
  - p29 China HS22090000 vinegar exports to South Korea, trade volume (2019-07 to 2020-0 = **841,835** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 10 \| 韩国 \| 841835 升 \| 108.17 万美元 \| 1.28 美元/升 \|"
  - p30 China HS22090000 vinegar exports to Germany, trade volume (2019-07 to 2020-06) = **661,939** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 12 \| 德国 \| 661939 升 \| 783385 美元 \| 1.18 美元/升 \|"
  - p31 China HS22090000 vinegar exports to United Kingdom, trade volume (2019-07 to 202 = **308,333** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 14 \| 英国 \| 308333 升 \| 559473 美元 \| 1.81 美元/升 \|"
- dropped by code checks: 16 (value_as_written not in quote as a whole number: 16)

### d3 [related_series] US import statistics

Hypothesis: US Census/BEA import data for HS 2209 from China gives mirror estimate of US-bound vinegar volume; combined with Hengshun share of Chinese vinegar sold in US, yields Hengshun volume.

Queries issued by the searcher: USITC HS 220900 imports China vinegar volume 2024; US Census vinegar imports from China 220900 value 2023 2024; OEC vinegar imports United States from China quantity tonnes 2024; 恒顺醋业 2024年年报 出口 境外 收入 美国

- `https://oec.world/en/profile/bilateral-product/vinegar/reporter/usa` -> **live_dated** (page date 2024-11-01); points raw/verified 0/0
- `https://chinadata.live/china-trade/hs/220900/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.usimportdata.com/data/us-220900-condiments-import-data/country-china` -> **dropped** (live http 500); points raw/verified -/-
- `https://wits.worldbank.org/trade/comtrade/en/country/All/year/2024/tradeflow/Exports/partner/MEX/product/220900` -> **live_dated** (page date 2024-01-01); points raw/verified 10/5
  - p32 China exports of vinegar and substitutes for vinegar (HS 2209) to Mexico, volume = **61,258** liter (2024-01-01..2024-12-31) [DISCARD: China-to-Mexico HS2209 volume; wrong destination for the target and adds no conversion or share information.] quote: "China ($140.37K , 61,258 Liter)"
  - p33 United States exports of vinegar and substitutes for vinegar to Mexico, volume,  = **12,747,300** liter (2024-01-01..2024-12-31) [DISCARD: US-to-Mexico flow; wrong origin and destination for the target.] quote: "United States ($8,673.59K , 12,747,300 Liter)"
  - p34 European Union exports of vinegar and substitutes for vinegar to Mexico, volume, = **1,265,830,000,000** liter (2024-01-01..2024-12-31) [DISCARD: Physically impossible volume (1.27e12 liters of vinegar to Mexico) — a unit/parse error; unusable.] quote: "European Union ($4,696.62K , 1,265,830,000,000 Liter)"
  - p35 Italy exports of vinegar and substitutes for vinegar to Mexico, volume, 2024 = **882,720** liter (2024-01-01..2024-12-31) [DISCARD: Italy-to-Mexico flow; irrelevant to Hengshun US exports.] quote: "Italy ($3,245.05K , 882,720 Liter)"
  - p36 Spain exports of vinegar and substitutes for vinegar to Mexico, volume, 2024 = **352,351** liter (2024-01-01..2024-12-31) [DISCARD: Spain-to-Mexico flow; irrelevant to Hengshun US exports.] quote: "Spain ($1,303.80K , 352,351 Liter)"
- dropped by code checks: 5 (scale word 'thousand' not supported by quote or table header: 5)

### d4 [capacity_consumption] US retail/Asian grocery channel

Hypothesis: US retail sales of Hengshun-branded vinegar (scanner/Amazon data) in bottles can be summed; retail sell-through approximates export shipments plus inventory change. Bottles = retail unit sales adjusted for channel coverage.

Queries issued by the searcher: Hengshun vinegar Amazon US sales units bottles; 恒顺香醋 美国 销量 瓶; Chinkiang vinegar US retail sales units Nielsen; Hengshun vinegar US market share export

- `https://www.sayweee.com/zht/mkpl/category/seasoning10/Vinegar?filters=%7B%22catalogue_num%22%3A%22seasoning10%22%7D` -> **live_dated** (page date 2015-01-01); points raw/verified 9/0
- `https://www.sayweee.com/zh/product/Heng-Shun-Zhenjiang-Vinegar/64693` -> **live_dated** (page date 2026-10-18); points raw/verified 3/0
- `https://www.freshgogo.com/pc/goodsDescribe?id=10004&language=zh` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.weee.com/zh/social/video/56118?id=56118` -> **live_dated** (page date 2026-10-18); points raw/verified 3/0
- dropped by code checks: 15 (period_end missing or unparseable: 14; scale word 'thousand' not supported by quote or table header: 1)

### d5 [base_rates] Product/packaging structure

Hypothesis: Average bottle size for Hengshun export vinegar (commonly 500ml) converts volume to bottles; bottled share vs bulk share of exports is a key multiplier.

Queries issued by the searcher: 恒顺香醋 出口 500ml 规格 装箱; Hengshun vinegar 500ml bottle export carton; 恒顺醋业 2024年年度报告 境外 营业收入 出口 销量; 恒顺醋业 出口 瓶装 散装 原醋 比例

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://fivecontinentsintl.com/en/product/hengshun-brand-9-degrees-rice-vinegar/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p37 HengShun Brand 9 Degrees Rice Vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p38 HengShun Brand 9 Degrees Rice Vinegar bottles per case = **12** bottles per case (..) [keep: ] quote: "Case Size: 500ml*12btls"
  - p39 HengShun Brand Cooking Wine with Shallot And Ginger bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p40 HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p41 HengShun Brand Six Years Vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p42 HengShun Brand Three Years Vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p43 HengShun Brand Vinegar 0 Additives bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p44 HengShun Brand Vinegar 0 Additives alternate bottle size = **535** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p45 HengShun Brand Vinegar for Dumpling bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p46 HengShun Brand Vinegar for Steamed Buns bottle size = **550** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p47 HengShun Brand White Rice Vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p48 HengShun Brand Zhenjiang Eight Years Vinegar bottle size = **300** ml per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://order.asiaexpressfood.nl/en/catalog/product/view/id/39820/s/schwarzer-essig-chinkiang/category/3207/` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.eximpedia.app/product-balsamic-vinegar-import-data/coo-china` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d6 [own_history] Hengshun historical export trend

Hypothesis: Prior-year export volumes and growth rates constrain the current-year US volume; if US-specific history is unavailable, total overseas growth applied to a base US estimate.

Queries issued by the searcher: 恒顺醋业 年报 境外 收入 出口 2021 2022 2023; 恒顺醋业 历年 出口 收入 海外 增长; 恒顺醋业 2023年度 与行业相关的定期经营数据公告 外贸模式 销售收入; 镇江香醋 出口 美国 市场 占比 食醋出口量 吨 2023

- `https://stock.stockstar.com/notice/SN2026041500001922.shtml` -> **live_dated** (page date 2026-04-15); points raw/verified 15/3
  - p49 Hengshun foreign trade channel revenue YoY change, FY2025 vs FY2024 = **-17.95** % (2025-01-01..2025-12-31) [keep: ] quote: "外贸模式 3,917.16 4,774.10 -17.95"
  - p50 Hengshun vinegar series revenue YoY change, FY2025 vs FY2024 = **4.38** % (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 132,109.25 126,559.63 4.38"
  - p51 Hengshun total revenue YoY change (channel table), FY2025 vs FY2024 = **8.29** % (2025-01-01..2025-12-31) [keep: ] quote: "合计 226,646.62 209,300.68 8.29"
- `https://www.aijingu.com/notices/600305/AN202404291631610629.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.zhenjiang.gov.cn/zhenjiang/zwyw/202407/9f238a06efa24fceb13d613b698c8bff.shtml` -> **dropped** (live http 301); points raw/verified -/-
- `http://jsgzw.jiangsu.gov.cn/art/2019/9/26/art_11776_8722336.html` -> **live_dated** (page date 2019-09-26); points raw/verified 8/2
  - p52 Hengshun import-export trade value 2018 = **7,473,830** 万美元 (ten-thousand USD) (2018-01-01..2018-12-31) [DISCARD: 2018 import-export trade value with an internally inconsistent unit (747.383 万美元 vs 7,473,830); too old and ambiguous to] quote: "2018年进出口贸易额达747.383万美元"
  - p53 Hengshun import-export trade value growth over 5 years (2018 vs 5 years earlier) = **54.37** % (2018-01-01..2018-12-31) [DISCARD: Redundant restatement of p52's growth context; adds no independent information.] quote: "2018年进出口贸易额达747.383万美元,比5年前增长了54.37%"
- dropped by code checks: 18 (scale word '万元' not supported by quote or table header: 12; period_end missing or unparseable: 6)

### d7 [persona] US distributor/importer

Hypothesis: US importers/distributors of Hengshun (e.g., Asian food distributors) may disclose shipment volumes or container counts; containers × bottles per container gives an upper-bound flow.

Queries issued by the searcher: Hengshun vinegar US distributor importer; Chinkiang vinegar container shipment US importer; importyeti Jiangsu Hengshun International Trad shipments containers; Hengshun Zhenjiang vinegar 20ft container 550ml bottles per container cases

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p54 Total shipments recorded for Jiangsu Hengshun Group (US customs records, all pro = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Duplicate of p69 (same ImportGenius 44-shipment total); keep one copy.] quote: "Total Shipments 44"
  - p55 Number of trading partners for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p56 Number of ports in Jiangsu Hengshun Group shipment records = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p57 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p70 (same bill-of-lading piece count).] quote: "Piece Count 700"
  - p58 Bottle size in vinegar description on bill of lading (550ML per bottle, 24 per u = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p71 (same 550ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p59 Bottles per case/pack in vinegar description (24 per unit) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p72 (same 24-per-case pack).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p60 Container length dimension on bill of lading (cm) = **240** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p73 (container length).] quote: "Length 240"
  - p61 Container height dimension on bill of lading (cm) = **102** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p74 (container height).] quote: "Height 102"
  - p62 Container width dimension on bill of lading (cm) = **96** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p75 (container width).] quote: "Width 96"
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-

### b1 [related_series] Hengshun share of Chinese vinegar exports

Hypothesis: If Hengshun's share of China's HS2209 export value (or volume) can be found from company reports, industry associations, or customs rankings, then p3/p17 US-bound totals can be converted into a Hengshun US volume — the single largest missing multiplier in route d2.

Queries issued by the searcher: 恒顺醋业 年报 出口 收入 占比 食醋 出口; 中国食醋出口 HS22090000 企业排名 恒顺; 中国 食醋 出口量 2024年 万吨 海关 出口额 亿美元; 中国调味品协会 食醋 出口 2024 出口额 恒顺 占比

- `https://www.sohu.com/a/821678279_121823071` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://finance.sina.com.cn/stock/relnews/cn/2026-06-10/doc-iniawpnc1440816.shtml` -> **live_dated** (page date 2026-06-10); points raw/verified 15/6
  - p63 China vinegar (食醋) total output, 2024 = **4,800,000** 万吨 (10,000 tonnes) (2024-01-01..2024-12-31) [keep: ] quote: "2024年全国食醋产量达480万吨,产值突破300亿元,年均复合增长率保持在6.5%以上"
  - p64 China vinegar industry output value, 2024 = **30,000,000,000** 亿元 (100 million yuan) (2024-01-01..2024-12-31) [keep: ] quote: "2024年全国食醋产量达480万吨,产值突破300亿元,年均复合增长率保持在6.5%以上"
  - p65 Number of above-scale vinegar enterprises in China, as of 2025 = **1,200** enterprises (2025-01-01..2025-12-31) [keep: ] quote: "截至 2025 年,全国规上食醋企业约 1200 家,中小作坊超 2800 家"
  - p66 Number of small vinegar workshops in China, as of 2025 = **2,800** workshops (2025-01-01..2025-12-31) [keep: ] quote: "全国规上食醋企业约 1200 家,中小作坊超 2800 家"
  - p67 Hengshun (恒顺醋业) R&D expenditure, 2025 = **93,920,000** 万元 (10,000 yuan) (2025-01-01..2025-12-31) [DISCARD: R&D expenditure; irrelevant to US bottle volume.] quote: "2025 年研发费9392 万元 (+4.67%),研发人员 152 人 (占比 8.11%)"
  - p68 Hengshun R&D personnel headcount, 2025 = **152** people (2025-01-01..2025-12-31) [DISCARD: R&D headcount; irrelevant to US bottle volume.] quote: "2025 年研发费9392 万元 (+4.67%),研发人员 152 人 (占比 8.11%)"
- `https://www.sgpjbg.com/labelsyh/shicuxingyebaogao/2/7069120.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 24 (value_as_written not in quote as a whole number: 15; period_end missing or unparseable: 9)

### b2 [physical_flow] US import records for Hengshun

Hypothesis: A refreshed ImportGenius/Panjiva/ImportYeti pull for Jiangsu Hengshun Group covering 2023-2024 would give shipment counts, container counts, and piece counts, letting us build an annual bottle flow directly (shipments/year × bottles/shipment) instead of relying on the stale 44-shipment total.

Queries issued by the searcher: ImportYeti Jiangsu Hengshun Group shipments 2024; Panjiva Hengshun vinegar US imports 2024; importyeti.com "Hengshun" supplier vinegar United States shipments; bill of lading "Chinkiang vinegar" 2024 importer United States shipment

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/7
  - p69 Total US customs shipments recorded for Jiangsu Hengshun Group, cumulative 2006- = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p70 Piece count on bill of lading EGLV142252207486 (Chinkiang vinegar 550ml@24), arr = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p71 Bottle size in product description on bill of lading EGLV142252207486 (Chinkiang = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p72 Bottles per case in product description on bill of lading EGLV142252207486 (550m = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p73 Container length in centimetres on bill of lading EGLV142252207486 = **240** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p74 Container height in centimetres on bill of lading EGLV142252207486 = **102** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p75 Container width in centimetres on bill of lading EGLV142252207486 = **96** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
- `https://pdf.marketpublishers.com/bosson_research/global-white-vinegar-market-research-report-2022status-n-outlook.pdf` -> **live_dated** (page date 2026-10-17); points raw/verified 15/5
  - p76 Global White Vinegar market size estimate, 2025 (USD) = **4,157,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global white-vinegar market size; wrong product scope (not Zhenjiang/Chinese aromatic vinegar) and no Hengshun or US-bot] quote: "The global White Vinegar market size was estimated at USD 4157.0 million in 2025 and"
  - p77 North America White Vinegar Sales Market Share by Country reference year = **2,024** year (2024-01-01..2024-12-31) [DISCARD: White-vinegar regional share figure reference year only; no numeric share and wrong product scope.] quote: "Figure 42. North America White Vinegar Sales Market Share by Country in 2024"
  - p78 Global White Vinegar Sales Share by Manufacturers reference year = **2,025** year (2025-01-01..2025-12-31) [DISCARD: White-vinegar manufacturer share reference year only; no numeric value, wrong scope.] quote: "Figure 13. White Vinegar Sales Share by Manufacturers in 2025"
  - p79 Global White Vinegar Revenue Share by Manufacturers reference year = **2,025** year (2025-01-01..2025-12-31) [DISCARD: White-vinegar revenue share reference year only; no numeric value, wrong scope.] quote: "Figure 14. Global White Vinegar Revenue Share by Manufacturers in 2025"
  - p80 Global White Vinegar Average Price (USD/KG) of Key Manufacturers reference year = **2,025** year (2025-01-01..2025-12-31) [DISCARD: White-vinegar average price reference year only; no numeric value, wrong scope.] quote: "Figure 16. Global Market White Vinegar Average Price (USD/KG) of Key Manufacturers in 2025"
- dropped by code checks: 12 (period_end missing or unparseable: 3; number: more than one number in value_as_written: 9)

### b3 [base_rates] US retail sell-through of Hengshun

Hypothesis: Amazon/Nielsen/SPINS unit sales of Hengshun-branded vinegar in the US, scaled by channel coverage, would give an independent retail-side estimate to cross-check the export-flow route and reveal whether export shipments and sell-through diverge materially.

Queries issued by the searcher: Hengshun vinegar Amazon US best sellers units; Nielsen Hengshun vinegar US sales; SPINS Asian vinegar Hengshun US retail; "Hengshun" vinegar "Amazon" "bought in past month"; "Hengshun" "best seller" vinegar US Amazon units sold; "Hengshun" vinegar import records US shipments; Jiangsu Hengshun Vinegar annual report 2024 export revenue United States

- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE/r` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://www.weee.com/ko/product/Hengshun-Zhenjiang-Vinegar/99090` -> **live_dated** (page date 2026-10-18); points raw/verified 0/0
- `https://www.sayweee.com/zht/mkpl/category/seasoning10/Vinegar?filters=%7B%22catalogue_num%22%3A%22seasoning10%22%7D` -> **live_dated** (page date 2015-01-01); points raw/verified 15/14
  - p81 Weekly sales of Hengshun Zhenjiang Xiangcu 18.6 fl oz (weekly units) = **600** bottles per week (..) [keep: ] quote: "恒順鎮江香醋 18.6 液盎司 ... 週銷量 600+"
  - p82 Weekly sales of Jinshan Zhenjiang Xiangcu 550 ml (weekly units) = **400** bottles per week (..) [keep: ] quote: "金梅 鎮江香醋【正常包装 带泡沫盒包装随机发】 550 毫升 ... 週銷量 400+"
  - p83 Weekly sales of Shuitala five-year aged vinegar 500 ml (weekly units) = **200** bottles per week (..) [keep: ] quote: "【水塔牌】五年老陳醋 500ml 500 毫升 ... 週銷量 200+"
  - p84 Weekly sales of Donghu Shanxi aged vinegar 500 ml (weekly units) = **400** bottles per week (..) [keep: ] quote: "東湖山西老陳醋 500 毫升 ... 週銷量 400+"
  - p85 Weekly sales of Lee Kum Kee pure brewed rice vinegar 16.9 fl oz (weekly units) = **300** bottles per week (..) [keep: ] quote: "李錦記 純釀米醋 16.9 液盎司 ... 週銷量 300+"
  - p86 Weekly sales of Koon Yick white rice vinegar 20.2 fl oz (weekly units) = **600** bottles per week (..) [keep: ] quote: "工研 白米醋 20.2 液盎司 ... 週銷量 600+"
  - p87 Weekly sales of Lee Kum Kee pure brewed aged vinegar 16.9 fl oz (weekly units) = **50** bottles per week (..) [keep: ] quote: "香港【李錦記】純釀陳醋 16.9 液盎司 ... 週銷量 50+"
  - p88 Weekly sales of Baoding Kangle vinegar 500 ml (weekly units) = **300** bottles per week (..) [keep: ] quote: "宝鼎 康乐醋 500 毫升 ... 週銷量 300+"
  - p89 Weekly sales of Mizkan sushi seasoning vinegar 24 fl oz (weekly units) = **100** bottles per week (..) [keep: ] quote: "Mizkan 壽司調味醋 24 液盎司 ... 週銷量 100+"
  - p90 Weekly sales of Marukan Japanese rice/sushi vinegar 710 ml (weekly units) = **50** bottles per week (..) [keep: ] quote: "Marukan 日式米醋 壽司醋 710 毫升 ... 週銷量 50+"
  - p91 Weekly sales of Kikkoman sushi vinegar 591 ml (weekly units) = **50** bottles per week (..) [keep: ] quote: "萬字 壽司醋 591 毫升 ... 週銷量 50+"
  - p92 Package size of Hengshun Jinshan Zhenjiang Xiangcu = **18.6** fluid ounces per bottle (..) [keep: ] quote: "恒順 金山 鎮江香醋 18.6 液盎司"
  - p93 Package size of Hengshun Zhenjiang Xiangcu = **18.6** fluid ounces per bottle (..) [keep: ] quote: "恒順鎮江香醋 18.6 液盎司"
  - p94 Package size of Jinshan Zhenjiang Xiangcu = **550** milliliters per bottle (..) [keep: ] quote: "金梅 鎮江香醋【正常包装 带泡沫盒包装随机发】 550 毫升"
- `https://www.weee.com/ko/search/hengshun%20zhenjiang%20vinegar?keyword=hengshun%20zhenjiang%20vinegar&trigger_type=search_active` -> **live_dated** (page date 2026-10-18); points raw/verified 15/15
  - p95 Amazon search results count for 'hengshun zhenjiang vinegar' (product listings,  = **505** search results (..) [DISCARD: Amazon search-result count (505 listings), not a sales quantity; redundant with p109.] quote: "hengshun zhenjiang vinegar(505)"
  - p96 Amazon listed sales volume for Heng Shun Zhenjiang vinegar 18.6 fl oz (lower bou = **600** units sold (..) [keep: ] quote: "Heng Shun Zhenjiang 식초 18.6 액량 온스 SNAP 600개+ 판매"
  - p97 Amazon listed sales volume for Hengshun 6-year aged Zhenjiang vinegar 580 mL (lo = **50** units sold (..) [keep: ] quote: "Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터 SNAP 50개+ 판매"
  - p98 Price per bottle of Heng Shun Zhenjiang vinegar 18.6 fl oz = **2.99** USD per bottle (..) [keep: ] quote: "$2.99 $0.16/액량 온스 Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p99 Price per fluid ounce of Heng Shun Zhenjiang vinegar 18.6 fl oz = **0.16** USD per fluid ounce (..) [DISCARD: Price per fluid ounce is a derived restatement of p98/p100; redundant.] quote: "$2.99 $0.16/액량 온스 Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p100 Bottle volume of Heng Shun Zhenjiang vinegar (18.6 fl oz) = **18.6** fluid ounces per bottle (..) [keep: ] quote: "Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p101 Price per bottle of Heng shun Zhenjiang vinegar Tianchu 18.6 fl oz = **3.49** USD per bottle (..) [keep: ] quote: "$3.49 $0.19/액량 온스 Heng shun 진강식초 천추 18.6 액량 온스"
  - p102 Price per fluid ounce of Heng shun Zhenjiang vinegar Tianchu 18.6 fl oz = **0.19** USD per fluid ounce (..) [DISCARD: Price per fluid ounce derived from p101/p103; redundant.] quote: "$3.49 $0.19/액량 온스 Heng shun 진강식초 천추 18.6 액량 온스"
  - p103 Bottle volume of Heng shun Zhenjiang vinegar Tianchu (18.6 fl oz) = **18.6** fluid ounces per bottle (..) [keep: ] quote: "Heng shun 진강식초 천추 18.6 액량 온스"
  - p104 Price per bottle of Hengshun 6-year aged Zhenjiang vinegar Tianchu 580 mL = **12.99** USD per bottle (..) [keep: ] quote: "$12.99 $0.66/액량 온스 Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p105 Price per fluid ounce of Hengshun 6-year aged Zhenjiang vinegar Tianchu 580 mL = **0.66** USD per fluid ounce (..) [DISCARD: Price per fluid ounce derived from p104/p106; redundant.] quote: "$12.99 $0.66/액량 온스 Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p106 Bottle volume of Hengshun 6-year aged Zhenjiang vinegar Tianchu (580 mL) = **580** milliliters per bottle (..) [keep: ] quote: "Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p107 Amazon search results count in Pantry/Sauces & Seasonings category for the query = **193** search results (..) [DISCARD: Category-filtered search-result count; not a sales quantity.] quote: "장류 • 양념류(193)"
  - p108 Amazon search results count in Health category for the query = **59** search results (..) [DISCARD: Category-filtered search-result count; not a sales quantity.] quote: "헬스(59)"
  - p109 Total Amazon search results count for the query (all categories) = **505** search results (..) [DISCARD: Total search-result count; listings are not bottles sold.] quote: "전체 결과(505)"
- dropped by code checks: 1 (scale word 'thousand' not supported by quote or table header: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us', 'zhenjiang vinegar']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p3', 'p4', 'p5', 'p6', 'p7'] All from one m.x315.cn HS22090000 export summary for 2020-2022; p5 is derived from p3/p6, so they are not independent. Usable only as a scale anchor for total Chinese vinegar exports to the US, not fo
- corroborating: ['p17', 'p18', 'p19'] Same source family (m.x315.cn) for a different period (2019-07 to 2020-06); p19 is p18/p17. Provides an earlier US-bound volume anchor and a unit price, but overlaps conceptually with p3-p5 and is not
- corroborating: ['p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16'] Same 2020-2022 HS22090000 export table; destination shares are internally consistent with p6. Useful only as context on where Chinese vinegar goes; none is US-specific.
- corroborating: ['p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p20'] Same 2019-07 to 2020-06 export table as p17-p19; non-US destinations, context only.
- conflicting: ['p32', 'p33', 'p34', 'p35', 'p36'] WITS HS2209-to-Mexico rows; p34 (EU 1.27e12 liters) is physically impossible and the set is about Mexico, not the US. Not usable for the target; p34 is clearly a data error.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] US distributor (fivecontinentsintl.com) product listings give Hengshun export bottle sizes: mostly 500 ml, some 535/550/580/300 ml. These are the right conversion factors for liters-to-bottles; they d
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62'] One bill of lading (2022-08-13) for Chinkiang vinegar 550ml@24, 700 pieces, container dims. Confirms export packaging convention (24 bottles/case, 550 ml) and that Hengshun-group shipments to the US e
- corroborating: ['p54', 'p55', 'p56'] ImportGenius summary: 44 total shipments 2006-2022 across 6 partners and 5 ports. Establishes order of magnitude of shipment frequency (a few per year) but is stale and covers all products.
- corroborating: ['p1', 'p49', 'p50', 'p51'] Hengshun channel revenue YoY: foreign trade +5.78% in FY2024, -17.95% in FY2025; vinegar series +4.38% FY2025. These are company-wide foreign-trade growth signals, not US-specific, and are the only gr
- corroborating: ['p52', 'p53'] 2018 Hengshun import-export trade value 747.383万美元 (note: the unit label in the table is inconsistent with the quote; the quote says 万美元). Old, all-products, all-destinations; context only.
- corroborating: ['p2'] Dealer count 2,014; domestic distribution context, not directly relevant to US export bottles.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p3', 'p4', 'p5', 'p6'] Same source (m.x315.cn customs summary) for China HS22090000 vinegar exports 2020-2022; p5 is the US share implied by p3/p6. All share one underlying customs measurement, so they are not independent o
- corroborating: ['p17', 'p18', 'p19'] Same customs snapshot for 2019-07 to 2020-06; p19 is p18/p17. Consistent with p3/p4 order of magnitude (US ~2.2M L/yr vs ~4.4M L/yr in the earlier window), suggesting a decline or definitional shift, 
- corroborating: ['p54', 'p55', 'p56', 'p69'] p54 and p69 are duplicate copies of the same ImportGenius total (44 shipments, 2006-2022). p55/p56 are facets of the same record set. All are stale (ends 2022-08) and cover all products, not just vine
- corroborating: ['p57', 'p58', 'p59', 'p70', 'p71', 'p72'] Duplicate copies of one bill of lading: 550ml@24, 700 pieces. Gives a bottle-size and case-pack anchor but a single shipment, not an annual flow.
- corroborating: ['p60', 'p61', 'p62', 'p73', 'p74', 'p75'] Duplicate container dimensions from the same bill of lading; usable only as a container-volume sanity check, not a flow.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] Distributor catalog bottle sizes for Hengshun export SKUs: mostly 500ml, some 535/550/580/300ml. Supports an average bottle size near 500-550ml for the volume-to-bottle conversion.
- corroborating: ['p81', 'p92', 'p93', 'p96', 'p98', 'p100'] Weee/Amazon retail listings for Hengshun 18.6 fl oz (~550ml) SKU; p81 (2015 weekly 600+) and p96 (600+ sold) are lower bounds on one SKU in one channel, not US totals.
- corroborating: ['p97', 'p104', 'p106'] Hengshun 6-year 580ml SKU retail evidence; small-volume premium SKU, useful only for bottle-size mix.
- conflicting: ['p1', 'p49'] Hengshun foreign-trade revenue grew +5.78% in FY2024 but fell -17.95% in FY2025; different years, so not a contradiction but a strong signal that a 2024-based estimate should not be extrapolated forwa
- corroborating: ['p63', 'p64', 'p65', 'p66'] Same industry article on China vinegar output and enterprise counts; contextual only, no US or Hengshun-specific split.
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80'] Same market-report family on global white vinegar; white vinegar is a different product scope from Zhenjiang aromatic vinegar and gives no Hengshun US bottle count.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Hengshun share of China HS2209 vinegar export volume to the US | 0.15 | 0.05..0.35 | 0.05..0.35 | fraction | unused | Hengshun is the leading branded Zhenjiang vinegar exporter, but HS2209 US-bound volume includes many producers and bulk/industrial vinegar; a mid-teens volume share is plausible. No kept point gives this share. | Hengshun competes in the same US-bound HS2209 flow and its brand share is in the stated range. | Customs or company disclosure showing Hengshun's US export volume below 5% or above 35% of China's HS2209 US volume. |
| a2 | Annual US-bound China HS2209 vinegar volume, 2024 (liters/year) | 2,200,000 | 1,200,000..4,000,000 | 1,200,000..4,000,000 | liters/year | unused | p3 gives 6.60M L over 2020-2022 (~2.2M L/yr); p17 gives 4.38M L for 2019-07..2020-06. The two windows bracket a plausible 2024 level near 2.2M L/yr with wide uncertainty from trend and definitional drift. | 2024 China-to-US HS2209 volume is near the 2020-2022 average rather than the earlier 2019-20 peak. | 2024 customs data showing US-bound HS2209 volume outside 1.2-4.0M L. |
| a3 | Average Hengshun export bottle size (liters per bottle) | 0.52 | 0.45..0.6 | 0.3674..0.7348 (widened) | liters/bottle | unused | Catalog SKUs (p37-p48) cluster at 500ml with some 535/550/580ml and a 300ml premium SKU; bill of lading p71 shows 550ml. A volume-weighted average near 0.52L is consistent. | Hengshun's US-bound bottled mix resembles the export catalog SKU mix. | Evidence that most US-bound Hengshun volume is bulk/drum or in much smaller/larger bottles. |
| a4 | Bottled (vs bulk) share of Hengshun US-bound vinegar volume | 0.85 | 0.6..0.97 | 0.5394..1.079 (widened) | fraction | unused | Retail listings (p81, p96, p98, p100) show Hengshun sold in consumer bottles in the US; some HS2209 flow is bulk/industrial, so a high but not complete bottled share is assumed. | Most Hengshun US shipments are consumer bottles rather than food-service bulk. | Evidence of large bulk/drum Hengshun shipments to US food manufacturers. |
| a5 | Hengshun share of China HS2209 export value to the US | 0.2 | 0.07..0.4 | 0.07..0.4 | fraction | unused | Hengshun's branded premium positioning implies a higher value share than volume share; used in the value-based route as an alternative to the volume-share route. | Hengshun's US export price per liter is above the HS2209 average, so value share exceeds volume share. | Evidence that Hengshun's US export prices are at or below the HS2209 average. |
| a6 | Annual US-bound China HS2209 vinegar value, 2024 (USD/year) | 2,800,000 | 1,500,000..5,000,000 | 1,500,000..5,000,000 | USD/year | unused | p4 gives $8.46M over 2020-2022 (~$2.8M/yr); p18 gives $5.16M for 2019-07..2020-06. A 2024 level near $2.8M/yr with wide uncertainty is consistent with the volume trend. | 2024 US-bound HS2209 value is near the 2020-2022 average. | 2024 customs value outside $1.5-5.0M. |
| a7 | Average Hengshun US export price per liter (USD/liter) | 2.2 | 1.4..3.5 | 1.4..3.5 | USD/liter | unused | p19 gives $1.18/L for all HS2209 to the US in 2019-20; Hengshun branded retail prices (p98, p101, p104) imply higher FOB prices for branded Zhenjiang vinegar, so a premium over the HS2209 average is assumed. | Hengshun's US FOB price per liter is above the HS2209 average, consistent with branded retail pricing. | Evidence that Hengshun US FOB prices are near or below $1.18/L. |
| a8 | Hengshun US retail unit sales coverage multiplier (one observed SKU/platform to national sell-through) | 40 | 10..150 | 10..150 | multiplier | unused | p81/p96 give 600+ weekly units for one SKU on one platform; scaling to all US channels (Asian grocers, mainstream retail, food service) requires a large multiplier with wide uncertainty. | The observed 600+/week SKU is representative of Hengshun's US retail velocity and channel coverage is in the stated range. | Scanner data showing Hengshun US retail sales far outside the implied range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p3'] / ['a1', 'a2', 'a3', 'a4'] | [] |  | 0.00 |  | formula_mc uses 4 assumptions (at most 3) |
| m2 | formula_mc | n/a | ['p4'] / ['a5', 'a6', 'a7'] | [] |  | 0.00 |  | formula names ['a5', 'a6', 'a7'] != inputs ['a5', 'a6', 'a7', 'p4'] |
| m3 | formula_mc | n/a | ['p81'] / ['a8'] | [] |  | 0.00 |  | covers only retail sell-through of channel, so code does not combine it with full estimates; sum it with its siblings (export shipments) in one method, with an allowance assumption for parts without e |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: only retail sell-through of channel (siblings export shipments); not combined (its own estimate 1,213,264)

Result: central **n/a** bottle/year, 80% interval [n/a, n/a] bottle/year, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

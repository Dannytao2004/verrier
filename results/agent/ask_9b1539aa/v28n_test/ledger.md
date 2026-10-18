# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types combined, including aromatic/sharp vinegar 香醋 and other bottled vinegar products) sold by Jiangsu Hengshun Group / Hengshun Vinegar-Industry Co. into the United States market, counted as bottles (retail units) delivered/ | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; Hengshun Vinegar-Industry Co., Ltd. (600305.SH) annual report and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Hengshun Vinegar-Industry Co. (600305.SH) investor disclosures

Hypothesis: Hengshun's annual report discloses total revenue, export/overseas revenue, and sometimes export volume; overseas revenue multiplied by a US share of exports gives a route to US sales value, then divided by average bottle price gives bottle count. Direction: higher overseas revenue and higher US share imply more bottles.

Queries issued by the searcher: 恒顺醋业 2024 年度报告 境外收入 出口; 恒顺醋业 年报 出口 境外收入 亿元; 恒顺醋业 外贸 出口 美国 占比 海外市场 北美; 恒顺醋业 2024年年度与行业相关的定期经营数据公告 外贸 4774.10万元 分地区

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 11/9
  - p1 Hengshun total operating revenue, FY2025 (full year) = **2,287,000,000** yuan (RMB) (2025-01-01..2025-12-31) [DISCARD: FY2025 revenue is outside the 2024 target period and is a total-revenue figure with no export/US split; not usable for a] quote: "\| 2025-12-31 \| 0.13 \| 3.04 \| 0.81 \| 1.03 \| 0.22 \| 22.87亿 \| 1.44亿 \| 4.27% \| \|"
  - p2 Hengshun total operating revenue, H1 2026 = **1,224,000,000** yuan (RMB) (2026-01-01..2026-06-30) [DISCARD: H1 2026 revenue, outside target period and no export/US breakdown.] quote: "\| 2026-06-30 \| 0.11 \| 3.02 \| 0.81 \| 1.02 \| -0.0076 \| 12.24亿 \| 1.21亿 \| 3.61% \| \|"
  - p3 Hengshun total operating revenue, Q1 2026 = **648,000,000** yuan (RMB) (2026-01-01..2026-03-31) [DISCARD: Q1 2026 revenue, outside target period and no export/US breakdown.] quote: "\| 2026-03-31 \| 0.06 \| 3.10 \| 0.81 \| 1.09 \| -0.04 \| 6.48亿 \| 6700.00万 \| 1.96% \| \|"
  - p4 Hengshun total operating revenue, 9M 2025 = **1,628,000,000** yuan (RMB) (2025-01-01..2025-09-30) [DISCARD: 9M 2025 revenue, outside target period and no export/US breakdown.] quote: "\| 2025-09-30 \| 0.13 \| 3.04 \| 0.81 \| 1.04 \| 0.03 \| 16.28亿 \| 1.42亿 \| 4.23% \| \|"
  - p5 Hengshun total operating revenue, H1 2025 = **1,125,000,000** yuan (RMB) (2025-01-01..2025-06-30) [DISCARD: H1 2025 revenue, outside target period and no export/US breakdown.] quote: "\| 2025-06-30 \| 0.10 \| 3.01 \| 0.81 \| 1.01 \| -0.04 \| 11.25亿 \| 1.11亿 \| 3.33% \| \|"
  - p6 Hengshun total operating revenue, H1 2026, year-on-year growth rate = **8.79** % (2026-01-01..2026-06-30) [DISCARD: Growth rate for H1 2026, outside target period and not a level.] quote: "营业总收入: 12.24亿元 同比增长8.79%"
  - p7 Hengshun net profit, FY2025 = **144,000,000** yuan (RMB) (2025-01-01..2025-12-31) [DISCARD: Net profit, not revenue or volume; irrelevant to bottle count.] quote: "\| 2025-12-31 \| 0.13 \| 3.04 \| 0.81 \| 1.03 \| 0.22 \| 22.87亿 \| 1.44亿 \| 4.27% \| \|"
  - p8 Hengshun gross margin, H1 2026 = **36.08** % (2026-01-01..2026-06-30) [DISCARD: Gross margin, not a volume or revenue input for the target.] quote: "毛利率:36.08%"
  - p9 Hengshun shareholder count, 2025-12-31 = **82,283** shareholders (2025-12-31..2025-12-31) [DISCARD: Shareholder count, irrelevant to vinegar sales.] quote: "\| 股东总数 \| 112866 \| 79781 \| 82283 \| 85684 \| 89478 \| 92329 \|"
- dropped by code checks: 17 (value_as_written not in quote as a whole number: 15; period_end missing or unparseable: 2)

### d2 [related_series] China customs export statistics by HS code

Hypothesis: China customs data report vinegar (HS 2209) exports by destination country in volume (kg/litres) and value. US-bound Chinese vinegar volume multiplied by Hengshun's share of China's vinegar exports to the US gives Hengshun US volume; divided by average bottle fill gives bottles.

Queries issued by the searcher: China vinegar exports to United States HS 2209 volume 2023; UN Comtrade 2209 China USA vinegar exports kg; 中国 海关 醋 出口 美国 HS 2209 2024; 2024年 我国 醋 出口 美国 出口量 升 海关; 2023 醋及用醋酸制得的醋代用品 出口 美国 数量 升; 恒顺醋业 出口 美国 占比 2023 年报

- `https://www.leadingir.com/datacenter/view/10031.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p10 China HS 22090000 vinegar exports to the United States, volume (2020-2022 cumula = **6,597,078** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p83 (same m.x315.cn cumulative US volume).] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p11 China HS 22090000 vinegar exports to the United States, value (2020-2022 cumulat = **8,459,027** USD (2020-01-01..2022-12-31) [DISCARD: Duplicate of p84.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p12 United States share of China HS 22090000 vinegar export volume (2020-2022 cumula = **11.35** % (2020-01-01..2022-12-31) [DISCARD: Duplicate of p85.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p13 China HS 22090000 vinegar exports to all destinations, total volume (2020-2022 c = **58,119,878** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p86.] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p14 Number of destination countries for China HS 22090000 vinegar exports (2020-2022 = **129** countries (2020-01-01..2022-12-31) [DISCARD: Count of destination countries; no bearing on US volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p15 China HS 22090000 vinegar exports to Hong Kong, volume (2020-2022 cumulative, la = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Hong Kong export volume; not the US destination.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p16 China HS 22090000 vinegar exports to Hong Kong, value (2020-2022 cumulative, hig = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Hong Kong export value; not the US destination.] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p17 Hong Kong share of China HS 22090000 vinegar export volume (2020-2022 cumulative = **23.44** % (2020-01-01..2022-12-31) [DISCARD: Hong Kong share; not the US destination.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p18 China HS 22090000 vinegar exports to Singapore, volume (2020-2022 cumulative) = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Singapore volume; not the US destination.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p19 China HS 22090000 vinegar exports to Australia, volume (2020-2022 cumulative) = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Australia volume; not the US destination.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p20 China HS 22090000 vinegar exports to Netherlands, volume (2020-2022 cumulative) = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Netherlands volume; not the US destination.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p21 China HS 22090000 vinegar exports to Malaysia, volume (2020-2022 cumulative) = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Malaysia volume; not the US destination.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p22 China HS 22090000 vinegar exports to Canada, volume (2020-2022 cumulative) = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Canada volume; not the US destination.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p23 China HS 22090000 vinegar exports to Japan, volume (2020-2022 cumulative) = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Japan volume; not the US destination.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 12/12
  - p24 China HS 22090000 vinegar exports, total volume, 2023 full year = **21,832,831** litres (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p25 China HS 22090000 vinegar exports, total value, 2023 full year = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p26 China HS 22090000 vinegar exports, total volume, 2024 full year = **25,760,168** litres (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p27 China HS 22090000 vinegar exports, total value, 2024 full year = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p28 China HS 22090000 vinegar exports, average unit price, 2024 full year = **1.15** USD per litre (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p29 China HS 22090000 vinegar exports, average unit price, 2023 full year = **1.18** USD per litre (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p30 China HS 22090000 vinegar imports, total volume, 2024 full year = **6,382,197** litres (2024-01-01..2024-12-31) [DISCARD: China vinegar imports, not exports to the US; wrong direction of trade.] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p31 China HS 22090000 vinegar imports, total value, 2024 full year = **11,585,503** USD (2024-01-01..2024-12-31) [DISCARD: China vinegar import value; wrong direction of trade.] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p32 China HS 22090000 vinegar exports, total volume, 2022 full year = **19,604,254** litres (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p33 China HS 22090000 vinegar exports, total value, 2022 full year = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p34 China HS 22090000 vinegar exports, total volume, 2021 full year = **20,249,374** litres (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p35 China HS 22090000 vinegar exports, total value, 2021 full year = **25,590,784** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] US import statistics (Census/USITC) for vinegar

Hypothesis: US import data for HS 2209 from China give the total US-bound volume; Hengshun's share of Chinese vinegar imports into the US (by brand presence or company share) converts to Hengshun bottles. Direction: larger US imports and larger Hengshun share imply more bottles.

Queries issued by the searcher: USITC HS 2209 imports China vinegar 2024 kg; US Census vinegar imports from China 2209 2023 2024; Hengshun vinegar US market share Chinese vinegar; "2209" "China" "2024" vinegar imports United States kg; US imports of vinegar from China 2024 value quantity; Hengshun annual report 2024 export revenue overseas vinegar

- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://dataweb.usitc.gov/trade/search/Import/HTS` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://usatrade.census.gov/` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.perplexity.ai/app/finance/600305.SS?comparing=600305.SS%2CSAP.TO%2CSMLKF%2C600597.SS%2C0322.HK%2CA2M.AX%2CWHGLY%2CNSRGY&preset=peers&symbo` -> **dropped** (live http 403); points raw/verified -/-

### d4 [physical_flow] Bottle-size and packaging conversion

Hypothesis: Export volume in tonnes or litres converts to bottles via average fill size (commonly 500 ml) and vinegar density (~1.01 kg/L). Bottles = volume / bottle fill. Direction: smaller average bottle size implies more bottles per tonne.

Queries issued by the searcher: Hengshun vinegar 500ml bottle US Chinkiang; 恒顺香醋 出口 规格 瓶装 500ml; 恒顺醋业 2024年年度报告 境外 出口 营业收入 吨; Hengshun vinegar 16.9 oz bottle weee Amazon "Hengshun" 550ml Chinkiang vinegar US

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://fivecontinentsintl.com/zh/product/hengshun-brand-vinegar-0-additives/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/0
- dropped by code checks: 12 (period_end missing or unparseable: 12)

### d5 [capacity_consumption] Hengshun production and export capacity

Hypothesis: Hengshun's total vinegar production capacity and utilisation, combined with export share of sales, bounds the US volume. US bottles <= total bottles produced * export share * US share of exports. Direction: higher capacity/utilisation and export share raise the upper bound.

Queries issued by the searcher: 恒顺醋业 2024 年报 食醋 产量 万吨; 恒顺醋业 产能 利用率 食醋 万吨; 恒顺醋业 2024年 设计产能 产能利用率 食醋 白醋 料酒 吨; 恒顺醋业 出口 美国 占比 外贸 收入 亿元 海外

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_XKUV.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `http://static.sse.com.cn/disclosure/bond/announcement/company/c/new/2022-03-24/185585_20220324_3_kH1Vy1GC.pdf` -> **live_dated** (page date 2022-03-24); points raw/verified 15/11
  - p36 Black vinegar (黑醋) capacity 2020 (tonnes) = **300,000** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "2020 年度 黑醋 300,000 300,000 100.00%"
  - p37 Black vinegar (黑醋) output 2020 (tonnes) = **300,000** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "2020 年度 黑醋 300,000 300,000 100.00%"
  - p38 White vinegar (白醋) capacity 2020 (tonnes) = **50,000** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "白醋 50,000 45,497 90.99%"
  - p39 White vinegar (白醋) output 2020 (tonnes) = **45,497** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "白醋 50,000 45,497 90.99%"
  - p40 Total condiment capacity 2020 (black vinegar + white vinegar + cooking wine, ton = **430,000** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "合计 430,000 413,686 96.21%"
  - p41 Total condiment output 2020 (tonnes) = **413,686** tonnes (2020-01-01..2020-12-31) [keep: ] quote: "合计 430,000 413,686 96.21%"
  - p42 Total condiment capacity utilisation rate 2020 = **96.21** % (2020-01-01..2020-12-31) [keep: ] quote: "合计 430,000 413,686 96.21%"
  - p43 Total condiment output 2021 Jan-Sep (tonnes) = **386,893** tonnes (2021-01-01..2021-09-30) [keep: ] quote: "合计 430,000 386,893 89.98"
  - p44 Total condiment capacity utilisation rate 2021 Jan-Sep = **89.98** percent (2021-01-01..2021-09-30) [keep: ] quote: "合计 430,000 386,893 89.98"
  - p45 Export share of Hengshun condiment sales 2020 (share of sales by region) = **0.99** percent (2020-01-01..2020-12-31) [DISCARD: Duplicate of p99 (2020 export share).] quote: "出口 1.00 0.99 1.00 1.00"
  - p46 Export share of Hengshun condiment sales 2019 = **1** percent (2019-01-01..2019-12-31) [DISCARD: Duplicate of p98 (2019 export share).] quote: "出口 1.00 0.99 1.00 1.00"
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0
- dropped by code checks: 4 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4)

### d6 [base_rates] Industry association and export-share benchmarks

Hypothesis: China Vinegar Industry Association or Zhenjiang vinegar industry data give total Zhenjiang aromatic vinegar exports and Hengshun's share; US share of Zhenjiang vinegar exports gives US-bound volume. Bottles = volume / fill size.

Queries issued by the searcher: 镇江香醋 出口 美国 数量; Zhenjiang vinegar export volume North America; 镇江海关 2024年 出口香醋 吨 同比增长; 恒顺醋业 2024年报 境外 营业收入 出口

- `https://m.sohu.com/a/926081799_120388781/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://www.ourjiangsu.com/a/20221101/1667308877263.shtml` -> **live_dated** (page date 2022-11-01); points raw/verified 5/3
  - p47 Number of countries and regions to which Zhenjiang aromatic vinegar is exported = **64** countries and regions (..) [DISCARD: Count of export destination countries; no volume information.] quote: "也是中国国家地理标志产品,远销海外64个国家和地区"
  - p48 Bottle count in a single shipment of 550ml Zhenjiang aromatic vinegar exported t = **24** bottles (..) [DISCARD: Single-shipment bottle count, not a rate; unusable as a volume input.] quote: "为即将出口到的日本的24瓶550ml装镇江香醋办理了RCEP原产地证"
  - p49 Fill size of bottled Zhenjiang aromatic vinegar in the Japan shipment = **550** ml per bottle (..) [keep: ] quote: "为即将出口到的日本的24瓶550ml装镇江香醋办理了RCEP原产地证"
- `https://max.book118.com/try_down/558011103137006073.pdf` -> **live_dated** (page date 2024-11-16); points raw/verified 15/15
  - p50 Zhenjiang aromatic vinegar export volume, 2015 (table 1, unit written as 顿/tonne = **280** tonnes (written 顿) (2015-01-01..2015-12-31) [keep: ] quote: "2015 280 25"
  - p51 Zhenjiang aromatic vinegar export volume, 2016 (table 1) = **400** tonnes (written 顿) (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p52 Zhenjiang aromatic vinegar export volume, 2017 (table 1) = **600** tonnes (written 顿) (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p53 Zhenjiang aromatic vinegar export volume, 2018 (table 1) = **727** tonnes (written 顿) (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p54 Zhenjiang aromatic vinegar export volume, 2019 (table 1) = **622** tonnes (written 顿) (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
  - p55 Zhenjiang aromatic vinegar export value, 2016 (table 1, 万美元) = **36** ten thousand USD (万美元) (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p56 Zhenjiang aromatic vinegar export value, 2017 (table 1, 万美元) = **55** ten thousand USD (万美元) (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p57 Zhenjiang aromatic vinegar export value, 2018 (table 1, 万美元) = **66.7** ten thousand USD (万美元) (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p58 Zhenjiang aromatic vinegar export value, 2019 (table 1, 万美元) = **58.6** ten thousand USD (万美元) (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
  - p59 US share of Zhenjiang vinegar export market structure (figure 1, percent) = **31** percent of export market (..) [keep: ] quote: "美国, 31"
  - p60 Canada share of Zhenjiang vinegar export market structure (figure 1, percent) = **15** percent of export market (..) [keep: ] quote: "加拿大, 15"
  - p61 Japan share of Zhenjiang vinegar export market structure (figure 1, percent) = **15** percent of export market (..) [keep: ] quote: "日本, 15"
  - p62 South Korea share of Zhenjiang vinegar export market structure (figure 1, percen = **15** percent of export market (..) [keep: ] quote: "韩国, 15"
  - p63 Hong Kong share of Zhenjiang vinegar export market structure (figure 1, percent) = **6** percent of export market (..) [keep: ] quote: "香港, 6"
  - p64 Australia share of Zhenjiang vinegar export market structure (figure 1, percent) = **6** percent of export market (..) [keep: ] quote: "澳大利亚, 6"
- `https://english.cnipa.gov.cn/attach/0/8d58d6b60eae471bbf85880b662843e3.pdf` -> **live_dated** (page date 2020-07-08); points raw/verified 1/1
  - p65 Annual Zhenjiang vinegar export volume by local enterprises to the international = **2,800** tons (..) [keep: ] quote: "The local enterprises export more than 2800 tons of Zhenjiang vinegar to the international market every year."
- dropped by code checks: 2 (period year 2024 does not appear in the page text or URL (likely mis-dated): 2)

### d7 [attention] US retail and e-commerce presence

Hypothesis: Hengshun/Chinkiang vinegar sales on US platforms (Amazon, Walmart, Asian grocers) indicate relative US demand; unit sales or review counts can proxy bottle volumes if scaled by a known conversion. Direction: higher US retail presence implies more bottles, but only as a cross-check.

Queries issued by the searcher: Hengshun vinegar Amazon best sellers Chinkiang vinegar sales rank; 恒顺香醋 美国 亚马逊 销量; "Hengshun" vinegar amazon.com "bought in past month"; Chinkiang vinegar Walmart Hengshun 550ml listing reviews

- `https://www.weee.com/ko/product/Hengshun-Zhenjiang-Vinegar/99090` -> **live_dated** (page date 2026-10-18); points raw/verified 0/0
- `https://www.weee.com/zh/social/video/56118?id=56118` -> **live_dated** (page date 2026-10-18); points raw/verified 5/2
  - p66 Number of comments on the Weee! community post about Hengshun Zhenjiang vinegar = **16** comments (2023-03-22..2023-03-22) [DISCARD: Social-media comment count; no quantitative link to bottle volume.] quote: "16 评论"
  - p67 Number of likes on the Weee! community post about Hengshun Zhenjiang vinegar = **41** likes (2023-03-22..2023-03-22) [DISCARD: Social-media like count; no quantitative link to bottle volume.] quote: "41"
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE/r` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://www.sayweee.com/ko/category/seasonings07/Vinegar?page=1&offset=0&filters=%7B%22catalogue_num%22%3A%22seasonings07%22%7D&trigger_type=taxonomy_` -> **live_dated** (page date 2026-10-18); points raw/verified 13/0
- dropped by code checks: 16 (scale word 'thousand' not supported by quote or table header: 1; period_end missing or unparseable: 15)

### d8 [shocks] Trade policy and tariff exposure

Hypothesis: US tariffs on Chinese food products and shipping costs affect US-bound volumes; a tariff change in 2018-2024 could shift the trend. Direction: higher tariffs reduce US-bound volume. Used to adjust historical export trend to 2024.

Queries issued by the searcher: US tariff Chinese vinegar HS 2209 Section 301; 中国 食醋 出口 美国 关税 恒顺; 恒顺醋业 2024年年度报告 境外 营业收入 出口; USTR Section 301 List 3 2018 HTS 2209 vinegar 10 percent Federal Register

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 8/0
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b1 [related_series] customs destination detail

Hypothesis: A 2024 US-specific HS 22090000 export volume (or US import volume from China) would replace the 2020-2022 cumulative US figure (p10) and the 31% Zhenjiang share (p59) with a current, directly measured US-bound volume, removing the largest transfer assumption in the customs route.

Queries issued by the searcher: China customs HS 22090000 vinegar exports to United States 2024 volume; UN Comtrade 220900 vinegar exports China United States 2024; WITS Comtrade China exports vinegar 220900 to United States 2024 Liter; 格兰德 HS22090000 2024年 出口美国 升 醋

- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://hs.bianmachaxun.com/report_hs_22090000` -> **live_dated** (page date 2021-01-01); points raw/verified 15/15
  - p68 China total vinegar export volume 2021 = **20,249,374** litres (2021-01-01..2021-12-31) [DISCARD: Duplicate of p34 (2021 total volume).] quote: "\| 2021年 \| 20249374 \| $25590784 \| $1.26 /升 \|"
  - p69 China total vinegar export volume 2020 = **17,414,624** litres (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 \| 17414624 \| $23362688 \| $1.34 /升 \|"
  - p70 China total vinegar export volume 2019 = **16,866,780** litres (2019-01-01..2019-12-31) [keep: ] quote: "\| 2019年 \| 16866780 \| $20005507 \| $1.19 /升 \|"
  - p71 China total vinegar export volume 2018 = **16,095,699** litres (2018-01-01..2018-12-31) [keep: ] quote: "\| 2018年 \| 16095699 \| $19047798 \| $1.18 /升 \|"
  - p72 China total vinegar export volume 2017 = **14,887,337** litres (2017-01-01..2017-12-31) [keep: ] quote: "\| 2017年 \| 14887337 \| $16936013 \| $1.14 /升 \|"
  - p73 China vinegar export value to United States 2021 = **2,702,517** US dollars (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p74 China vinegar export value to United States 2020 = **2,484,932** US dollars (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p75 China vinegar export value to United States 2019 = **1,932,681** US dollars (2019-01-01..2019-12-31) [keep: ] quote: "\| \| 美国 \| 10% \| $1932681 \| $1.17 \|"
  - p76 China vinegar export value to United States 2018 = **2,662,832** US dollars (2018-01-01..2018-12-31) [keep: ] quote: "\| \| 美国 \| 14% \| $2662832 \| $1.2 \|"
  - p77 China vinegar export value to United States 2017 = **2,054,779** US dollars (2017-01-01..2017-12-31) [keep: ] quote: "\| \| 美国 \| 12% \| $2054779 \| $1.17 \|"
  - p78 United States share of China vinegar export value 2021 = **11** % (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p79 United States share of China vinegar export value 2020 = **11** % (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p80 China vinegar export average price to United States 2021 = **1.37** US dollars per litre (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p81 China vinegar export average price to United States 2020 = **1.21** US dollars per litre (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p82 China total vinegar export value 2021 = **25,590,784** US dollars (2021-01-01..2021-12-31) [DISCARD: Duplicate of p35 (2021 total value).] quote: "\| 2021年 \| 20249374 \| $25590784 \| $1.26 /升 \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p83 Cumulative China HS22090000 vinegar exports to the United States, volume (2020-0 = **6,597,078** litres (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p84 Cumulative China HS22090000 vinegar exports to the United States, value (2020-01 = **8,459,027** US dollars (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p85 US share of China HS22090000 vinegar export volume (numerator US volume, denomin = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p86 Cumulative total China HS22090000 vinegar exports to all countries, volume (2020 = **58,119,878** litres (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p87 Number of destination countries for China HS22090000 vinegar exports (2020-01 to = **129** countries (2020-01-01..2022-12-31) [DISCARD: Country count, irrelevant to bottle volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p88 China HS22090000 vinegar exports to Hong Kong, volume (2020-01 to 2022-12) = **13,624,552** litres (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p89 China HS22090000 vinegar exports to Hong Kong, value (2020-01 to 2022-12) = **15,656,412** US dollars (2020-01-01..2022-12-31) [keep: ] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p90 Hong Kong share of China HS22090000 vinegar export volume (numerator Hong Kong v = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p91 China HS22090000 vinegar exports to Singapore, volume (2020-01 to 2022-12) = **4,057,620** litres (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p92 China HS22090000 vinegar exports to Australia, volume (2020-01 to 2022-12) = **3,691,524** litres (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p93 China HS22090000 vinegar exports to Canada, volume (2020-01 to 2022-12) = **2,537,372** litres (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p94 China HS22090000 vinegar exports to Japan, volume (2020-01 to 2022-12) = **2,404,533** litres (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p95 China HS22090000 vinegar exports to Netherlands, volume (2020-01 to 2022-12) = **3,519,273** litres (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p96 China HS22090000 vinegar exports to Malaysia, volume (2020-01 to 2022-12) = **3,160,711** litres (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b2 [own_history] company disclosure

Hypothesis: Hengshun's 2024 annual report overseas/export revenue (or export volume) would let the US share of exports convert to a US sales value, giving an independent route to bottles via average bottle price.

Queries issued by the searcher: 恒顺醋业 600305 2024年年度报告 境外收入 出口; 恒顺醋业 2024年报 营业收入 分地区 境外 国外; 恒顺醋业 出口 美国 市场 占比 海外 销售 2024; 镇江香醋 出口 2024 海关 美国 出口量 吨

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1856807881049677824` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-

### b3 [base_rates] industry association

Hypothesis: A current (2023-2024) Zhenjiang vinegar export volume and Hengshun's share of it would update the stale 2015-2019 series (p50-p54) and the 2800 t figure (p65), resolving the 10x scope conflict and anchoring the Zhenjiang-share route.

Queries issued by the searcher: 镇江香醋 出口 2023 吨 恒顺 份额; 镇江醋 2024 出口 量 吨 恒顺; 中国调味品协会 食醋 出口 2023 镇江香醋; Hengshun vinegar export United States 2023 2024 tons

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_XKUV.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://cfi.cn/p20250422000502.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://cfe-expo.com/nd.jsp?_ngc=-1&fromColId=-1&groupId=1&id=950` -> **dropped** (live http 204); points raw/verified -/-
- `https://static.sse.com.cn/bond/bridge2/disclosure/announcement/c/202403/041105_20240312_C4VH.pdf` -> **live_dated** (page date 2024-03-12); points raw/verified 15/14
  - p97 Hengshun Group condiment (jiangcu) sales share from export, 2022 = **2.15** % of condiment sales (2022-01-01..2022-12-31) [keep: ] quote: "出口 2.15 1.24 0.99"
  - p98 Hengshun Group condiment (jiangcu) sales share from export, 2021 = **1.24** % of condiment sales (2021-01-01..2021-12-31) [keep: ] quote: "出口 2.15 1.24 0.99"
  - p99 Hengshun Group condiment (jiangcu) sales share from export, 2020 = **0.99** % of condiment sales (2020-01-01..2020-12-31) [keep: ] quote: "出口 2.15 1.24 0.99"
  - p100 Hengshun Group jiangcu condiment revenue, 2022 = **265,296** 万元 (2022-01-01..2022-12-31) [keep: ] quote: "酱醋调味品 (国控集团) 190,504.75 13.09 265,295.60 12.96 253,472.43 12.93 243,011.22 12.93"
  - p101 Hengshun Group jiangcu condiment revenue, 2021 = **253,472** 万元 (2021-01-01..2021-12-31) [keep: ] quote: "酱醋调味品 (国控集团) 190,504.75 13.09 265,295.60 12.96 253,472.43 12.93 243,011.22 12.93"
  - p102 Hengshun Group jiangcu condiment revenue, 2020 = **243,011** 万元 (2020-01-01..2020-12-31) [keep: ] quote: "酱醋调味品 (国控集团) 190,504.75 13.09 265,295.60 12.96 253,472.43 12.93 243,011.22 12.93"
  - p103 Hengshun Group jiangcu condiment revenue, 2023 Jan-Sep = **190,505** 万元 (2023-01-01..2023-09-30) [keep: ] quote: "酱醋调味品 (国控集团) 190,504.75 13.09 265,295.60 12.96 253,472.43 12.93 243,011.22 12.93"
  - p104 Hengshun Group vinegar (cu) series production cost, 2022 = **75,055** 万元 (2022-01-01..2022-12-31) [keep: ] quote: "合计 75,055.00 61.38 67,846.31 65.02 73,452.16 78.01"
  - p105 Hengshun Group vinegar (cu) series production cost, 2021 = **67,846** 万元 (2021-01-01..2021-12-31) [keep: ] quote: "合计 75,055.00 61.38 67,846.31 65.02 73,452.16 78.01"
  - p106 Hengshun Group vinegar (cu) series production cost, 2020 = **73,452** 万元 (2020-01-01..2020-12-31) [keep: ] quote: "合计 75,055.00 61.38 67,846.31 65.02 73,452.16 78.01"
  - p107 Hengshun Group vinegar (cu) series capacity, 2022 = **350,000** 吨 (2022-01-01..2022-12-31) [keep: ] quote: "醋系列 350,000 350,000 100.00"
  - p108 Hengshun Group vinegar (cu) series output, 2022 = **350,000** 吨 (2022-01-01..2022-12-31) [keep: ] quote: "醋系列 350,000 350,000 100.00"
  - p109 Hengshun Group vinegar (cu) series capacity, 2023 Jan-Sep = **350,000** 吨 (2023-01-01..2023-09-30) [keep: ] quote: "醋系列 350,000 240,000 68.57"
  - p110 Hengshun Group vinegar (cu) series output, 2023 Jan-Sep = **240,000** 吨 (2023-01-01..2023-09-30) [keep: ] quote: "醋系列 350,000 240,000 68.57"
- dropped by code checks: 1 (number: value_as_written is only part of a larger CJK number in the quote: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us import', 'zhenjiang vinegar sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p10', 'p11', 'p12', 'p13'] Same customs dataset (2020-2022 cumulative HS 22090000): p10/p11 are the US line, p12 its share, p13 the all-destination total. Internally consistent (p10/p13 ≈ 11.35%). Single underlying source, so n
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p32', 'p33', 'p34', 'p35'] One customs aggregator series of China HS 22090000 total exports by year; value/volume/unit-price triples are internally derived (value/volume = unit price). Use as a single trend signal, not as multi
- corroborating: ['p10', 'p26'] Both are China HS 22090000 export totals; the 2020-2022 cumulative US volume (p10) is consistent in magnitude with the annual totals (p26 ~25.8M L/yr in 2024), so the US is a modest but non-trivial de
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] One Zhenjiang-aromatic-vinegar export table (volume and value by year 2015-2019); volume/value pairs are internally consistent. Single source; the '顿' unit is a typo for tonnes.
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64'] One pie chart of Zhenjiang vinegar export destination shares; sums to ~88% with a residual 'other'. US is the largest single destination at 31%.
- conflicting: ['p50', 'p65'] p50 gives 280 t for 2015 while p65 states >2800 t/yr for local Zhenjiang enterprises — a 10x discrepancy. Likely different scope (one firm/one product line vs all local enterprises) or a units/typo er
- corroborating: ['p45', 'p46'] Both show Hengshun export share of condiment sales ~1% in 2019-2020; consistent, but this is a share of total sales, not a US-specific figure.
- corroborating: ['p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] One 2020-2021 capacity/output table; black+white vinegar output ~345k t in 2020. Provides an upper bound on total vinegar production, not US sales.
- corroborating: ['p66', 'p67'] Single Weee! social post engagement counts; only a weak qualitative demand signal, not a volume measure.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p10', 'p11', 'p12', 'p83', 'p84', 'p85'] Same underlying m.x315.cn 2020-2022 cumulative US HS22090000 export figure, duplicated across two id sets; one measurement, not independent confirmation.
- corroborating: ['p13', 'p86', 'p87'] Same m.x315.cn 2020-2022 all-destination total; p13 and p86 are identical values, p87 is the country count from the same page.
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p32', 'p33', 'p34', 'p35', 'p68', 'p69', 'p70', 'p71', 'p72', 'p82'] China HS22090000 annual export totals from bianmachaxun; p68/p82 duplicate p34/p35 for 2021. Consistent rising trend 2017-2024.
- corroborating: ['p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] US-bound China vinegar value and share 2017-2021 from bianmachaxun; US share ~10-14% of value, consistent with p12/p85 volume share ~11.35%.
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] Zhenjiang aromatic vinegar export volume/value 2015-2019 from one document; internally consistent series but stale and small (~600-700 t) versus p65's 2800 t.
- conflicting: ['p65', 'p50', 'p51', 'p52', 'p53', 'p54'] p65 states >2800 t/yr Zhenjiang vinegar exports while the 2015-2019 table shows 280-727 t; likely different scope (all local enterprises vs a subset, or different years). Material 4-10x scope conflict
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64'] Zhenjiang export market structure shares summing to ~88%; US 31% is the largest destination. Undated, so period transfer is uncertain.
- corroborating: ['p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103'] Hengshun export share of condiment sales rising 0.99%->1.24%->2.15% (2020-2022); export is a small fraction of Hengshun sales.
- corroborating: ['p107', 'p108', 'p109', 'p110', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] Hengshun vinegar capacity/output ~350,000 t (2022) and 2020 condiment capacity 430,000 t; capacity is not realised export volume, only an upper bound.
- corroborating: ['p45', 'p46', 'p97', 'p98', 'p99'] p45/p46 duplicate the 2019-2020 export share values in p98/p99; same source, redundant.
- corroborating: ['p49', 'p48'] 550 ml bottle fill for Zhenjiang aromatic vinegar export shipment; p48 (24 bottles) is a single-shipment count, not a rate.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Hengshun share of China vinegar exports to the US | 0.25 | 0.1..0.45 | 0.1..0.45 | fraction | m1 (m1) | Hengshun is the largest branded Chinese vinegar exporter and dominant Zhenjiang producer, but HS22090000 includes many bulk and other-brand vinegars; a leading-brand share of a fragmented export pool plausibly sits at 10-45%. | Converts total US-bound Chinese vinegar volume into Hengshun-attributable volume. | Evidence that Hengshun's share of Chinese vinegar exports to the US is below 10% or above 45%. |
| a2 | Average bottle fill for Hengshun bottled vinegar sold in the US | 0.5 | 0.35..0.75 | 0.35..0.75 | litre per bottle | m1 (m1), m2 (m2) | Export bottles are commonly 500-550 ml (p49); US retail also carries 750 ml-1 L formats, so a mean near 0.5 L with a wide range is reasonable. | Converts litres of Hengshun US-bound vinegar into retail bottle units. | Evidence that US-bound Hengshun bottles are predominantly much smaller or larger than 0.35-0.75 L. |
| a3 | US share of China vinegar export volume, 2024 | 0.11 | 0.08..0.15 | 0.07746..0.1549 (widened) | fraction | m1 (m1), m2 (m2) | US share of China vinegar export volume was 11.35% (2020-2022, p12) and 10-14% by value 2017-2021 (p78-p79); carrying ~11% into 2024 with a modest range is consistent with the stable historical share. | Applied to 2024 total China vinegar export volume (p26) to get US-bound litres. | 2024 customs data showing US share outside 8-15%. |
| a4 | Zhenjiang-type share of US-bound Chinese vinegar | 0.31 | 0.15..0.5 | 0.15..0.5 | fraction | m2 (m2) | p59 shows the US takes 31% of Zhenjiang vinegar exports; conversely Zhenjiang aromatic vinegar is a major but not exclusive component of Chinese vinegar shipped to the US, so 15-50% of US-bound Chinese vinegar being Zhenjiang-type is plausible. | Used with p26 and a3 to estimate Zhenjiang-type US-bound volume, then scaled by Hengshun's share of Zhenjiang exports. | Evidence that Zhenjiang-type vinegar is a much smaller or larger fraction of US-bound Chinese vinegar. |
| a5 | Hengshun share of Zhenjiang-type vinegar exports | 0.5 | 0.3..0.7 | 0.3..0.7 | fraction | m2 (m2) | Hengshun is the flagship Zhenjiang vinegar enterprise and by far the largest exporter of the style; a majority-to-plurality share of Zhenjiang-type exports is plausible, tempered by many smaller registered producers. | Converts Zhenjiang-type US-bound volume into Hengshun-attributable volume. | Evidence that Hengshun holds well under 30% or over 70% of Zhenjiang vinegar exports. |
| a6 | Hengshun export share of condiment sales, 2024 | 0.025 | 0.015..0.04 | 0.015..0.04 | fraction | unused | Export share rose 0.99% (2020) to 1.24% (2021) to 2.15% (2022) per p97-p99; extrapolating a continued gradual rise to ~2.5% in 2024 with a range is consistent with the trend. | Used with Hengshun condiment revenue to bound export value, then US share of exports. | 2024 annual report showing export share below 1.5% or above 4%. |
| a7 | US share of Hengshun exports | 0.3 | 0.15..0.45 | 0.15..0.45 | fraction | unused | The US is the largest overseas market for Chinese vinegar (p59 shows US 31% of Zhenjiang exports); Hengshun's US share of its own exports plausibly sits near 30%. | Converts Hengshun total export value into US-bound value. | Evidence that the US is a minor (<15%) or dominant (>45%) destination of Hengshun exports. |
| a8 | Hengshun average export bottle price | 2 | 1.2..3.5 | 1.2..3.5 | USD per bottle | unused | China vinegar export unit value is ~$1.15/L (p28); branded Hengshun export bottles carry a premium over bulk, so ~$2 per 500 ml bottle with a wide range is plausible. | Converts US-bound Hengshun export value into bottle count. | Evidence that Hengshun export bottle price is below $1.2 or above $3.5. |
| a9 | USD to CNY exchange rate, 2024 average | 7.2 | 6.8..7.6 | 5.083..10.17 (widened) | CNY per USD | unused | The 2024 average USD/CNY rate was around 7.1-7.2; a narrow range covers plausible annual averages. Needed only to convert the 万元 revenue figure into USD before dividing by a USD bottle price. | Used in the own-history value route to put Hengshun revenue and export bottle price on the same currency basis. | A 2024 average USD/CNY rate outside 6.8-7.6. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,169,703 | ['p26'] / ['a1', 'a2', 'a3'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 692,908 | ['p26'] / ['a2', 'a3', 'a4', 'a5'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **900,276** bottle, 80% interval [354,573, 2,285,837] bottle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']


## Final answer

Best computed estimate: 900,276 bottle of Hengshun bottled vinegar sold into the US in calendar year 2024 (all bottled vinegar types, export shipments rather than US retail sell-through). The 80% model-based interval is 354,573 to 2,285,837 bottle, conditional on the assumptions and reflecting input uncertainty only.

Two routes were combined at 50% and 50%: a customs route (1,169,703 bottle) and a Zhenjiang-share route (692,908 bottle). Both start from the observed 2024 China vinegar export volume of 25,760,168 litres, then apply the US share (0.11, range 0.07746 to 0.1549), a Hengshun share (0.25 or 0.5), and average bottle fill (0.5 L, range 0.35 to 0.75). Only the customs total is observed; every share and the fill are analyst assumptions, so the result is a transfer-based estimate.

The biggest risk is that Hengshun's US-bound mix may be more premium or smaller-bottle than the customs average, and the two routes share correlated shares. US-specific shipment data from Hengshun or customs would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Hengshun share of China vinegar exports to the US: 0.25 fraction, range 0.1 to 0.45; used by m1. Overturned by: Evidence that Hengshun's share of Chinese vinegar exports to the US is below [n] or above [n].
- a2 Average bottle fill for Hengshun bottled vinegar sold in the US: 0.5 litre per bottle, range 0.35 to 0.75; used by m1, m2. Overturned by: Evidence that US-bound Hengshun bottles are predominantly much smaller or larger than [n]-[n] L.
- a3 US share of China vinegar export volume, 2024: 0.11 fraction, range 0.07746 to 0.1549 (range widened by code); used by m1, m2. Overturned by: 2024 customs data showing US share outside [n]-[n].
- a4 Zhenjiang-type share of US-bound Chinese vinegar: 0.31 fraction, range 0.15 to 0.5; used by m2. Overturned by: Evidence that Zhenjiang-type vinegar is a much smaller or larger fraction of US-bound Chinese vinegar.
- a5 Hengshun share of Zhenjiang-type vinegar exports: 0.5 fraction, range 0.3 to 0.7; used by m2. Overturned by: Evidence that Hengshun holds well under [n] or over [n] of Zhenjiang vinegar exports.

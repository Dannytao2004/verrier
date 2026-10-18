# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar sold/exported to the United States in a full year, all bottle types combined (working interpretation: annual export volume in bottles, latest completed year before cutoff, i.e. 2025; alternative: most recent reported fiscal year or trailing 12 mon | unit bottles per year | period 2025-01-01..2025-12-31 | publisher No official publisher of this figure; Hengshun Group (江苏恒顺醋业股份有限公司) annual reports and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Hengshun corporate reporting

Hypothesis: Hengshun's annual reports disclose total export revenue and possibly export volume; US share of exports can be estimated from regional breakdowns or disclosed major markets. Target = total export bottles × US share.

Queries issued by the searcher: 恒顺醋业 年报 境外收入 出口; 恒顺醋业 2024年年度报告 境外收入 美国; 恒顺醋业 出口 美国 占比 海外市场; 恒顺 香醋 出口量 吨 镇江 海关 出口

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 13/0
- `https://www.9fzt.com/detail/sh_600305_9_eeda55b1c527cc3d1df240904019c864.html` -> **live_dated** (page date 2026-04-15); points raw/verified 14/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.sgpjbg.com/baogao/631780.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 27 (value_as_written not in quote as a whole number: 25; period_end missing or unparseable: 2)

### d2 [related_series] China customs trade statistics

Hypothesis: China customs HS code 2209 (vinegar) exports to US give total Chinese vinegar export volume to US; Hengshun's share of China vinegar exports (by value or volume) can be applied. Target = US-bound Chinese vinegar bottles × Hengshun share.

Queries issued by the searcher: 中国 海关 醋 出口 美国 HS 2209 数量 金额; China vinegar exports to United States HS 220900 value volume; 恒顺醋业 2024年年报 境外 出口 营业收入 占比; 恒顺醋业 出口 美国 销量 吨 海外收入

- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 11/11
  - p1 China total exports of HS 22090000 vinegar and vinegar substitutes, volume, 2025 = **25,428,030** liters (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025年 1月-12月份 \| 25428030 \| $28176312 \| $1.11 \| 导出 \|"
  - p2 China total exports of HS 22090000 vinegar and vinegar substitutes, value, 2025  = **28,176,312** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025年 1月-12月份 \| 25428030 \| $28176312 \| $1.11 \| 导出 \|"
  - p3 China total exports of HS 22090000 vinegar and vinegar substitutes, volume, 2024 = **25,760,168** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p4 China total exports of HS 22090000 vinegar and vinegar substitutes, value, 2024  = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p5 China total exports of HS 22090000 vinegar and vinegar substitutes, volume, 2023 = **21,832,831** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p6 China total exports of HS 22090000 vinegar and vinegar substitutes, value, 2023  = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p7 China average export price of HS 22090000 vinegar, per liter, 2025 Jan-Dec = **1.11** USD per liter (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025年 1月-12月份 \| 25428030 \| $28176312 \| $1.11 \| 导出 \|"
  - p8 China average export price of HS 22090000 vinegar, per liter, 2024 Jan-Dec = **1.15** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p9 China average export price of HS 22090000 vinegar, per liter, 2023 Jan-Dec = **1.18** USD per liter (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p10 China total imports of HS 22090000 vinegar and vinegar substitutes, volume, 2025 = **7,007,699** liters (2025-01-01..2025-12-31) [DISCARD: China vinegar imports into China; irrelevant to Hengshun exports to the US.] quote: "\| 2025年 1月-12月份 \| 7007699 \| $12319801 \| $1.76 \| 导出 \|"
  - p11 China total imports of HS 22090000 vinegar and vinegar substitutes, value, 2025  = **12,319,801** USD (2025-01-01..2025-12-31) [DISCARD: China vinegar import value; irrelevant to the export target.] quote: "\| 2025年 1月-12月份 \| 7007699 \| $12319801 \| $1.76 \| 导出 \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p12 China HS 22090000 vinegar exports to the United States, total quantity, cumulati = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p13 China HS 22090000 vinegar exports to the United States, total value, cumulative  = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p14 United States share of China HS 22090000 vinegar export quantity, cumulative 202 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p15 China HS 22090000 vinegar exports worldwide, total quantity, cumulative 2020-01  = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p16 Number of destination countries for China HS 22090000 vinegar exports, cumulativ = **129** countries (2020-01-01..2022-12-31) [DISCARD: Count of destination countries; no bearing on US volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p17 China HS 22090000 vinegar exports to Hong Kong, quantity (largest destination),  = **13,624,552** liters (2020-01-01..2022-12-31) [DISCARD: Hong Kong export volume; not the US and not Hengshun.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p18 China HS 22090000 vinegar exports to Hong Kong, value (largest destination), cum = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Hong Kong export value; not the US and not Hengshun.] quote: "出口中国香港金额最高,总计15,656,412美元"
  - p19 China HS 22090000 vinegar exports to Singapore, quantity, cumulative 2020-01 to  = **4,057,620** liters (2020-01-01..2022-12-31) [DISCARD: Singapore export volume; not the US.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p20 China HS 22090000 vinegar exports to Australia, quantity, cumulative 2020-01 to  = **3,691,524** liters (2020-01-01..2022-12-31) [DISCARD: Australia export volume; not the US.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p21 China HS 22090000 vinegar exports to Netherlands, quantity, cumulative 2020-01 t = **3,519,273** liters (2020-01-01..2022-12-31) [DISCARD: Netherlands export volume; not the US.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p22 China HS 22090000 vinegar exports to Malaysia, quantity, cumulative 2020-01 to 2 = **3,160,711** liters (2020-01-01..2022-12-31) [DISCARD: Malaysia export volume; not the US.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p23 China HS 22090000 vinegar exports to Canada, quantity, cumulative 2020-01 to 202 = **2,537,372** liters (2020-01-01..2022-12-31) [DISCARD: Canada export volume; not the US.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p24 China HS 22090000 vinegar exports to Japan, quantity, cumulative 2020-01 to 2022 = **2,404,533** liters (2020-01-01..2022-12-31) [DISCARD: Japan export volume; not the US.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p25 China HS 22090000 vinegar exports to France, quantity, cumulative 2020-01 to 202 = **1,754,906** liters (2020-01-01..2022-12-31) [DISCARD: France export volume; not the US.] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [physical_flow] US import/retail channel

Hypothesis: US imports of Chinese vinegar (via US Census/UN Comtrade) times Hengshun's brand share in US Asian grocery channel gives Hengshun US volume; convert to bottles via average bottle size. Target = US Chinese vinegar imports (liters) × Hengshun share ÷ bottle size.

Queries issued by the searcher: US imports vinegar from China HS 2209 volume liters; Chinkiang vinegar US market share Hengshun; UN Comtrade United States imports 2209 vinegar China 2024 quantity kg; 恒顺醋业 年报 2024 境外 营业收入 出口

- `https://m.x315.cn/doc/a66NUr` -> **live_dated** (page date 2023-09-26); points raw/verified 15/14
  - p26 China Hengshun brand white rice vinegar (HS 22090000) total import volume from a = **20,664,582** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,恒顺牌白米醋(HS22090000)共从海外38个国家进口,总计20,664,582升,3,430万美元。"
  - p27 China Hengshun brand white rice vinegar import volume from Japan (rank 1), 2020- = **5,311,063** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Japan figure from the ambiguous p26 dataset; not the US.] quote: "第一日本:总数量为5,311,063升;金额5,396,893美元;总占比25.70%。"
  - p28 China Hengshun brand white rice vinegar import volume from United States (rank 2 = **3,817,694** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为3,817,694升;金额13,523,057美元;总占比18.47%。"
  - p29 China Hengshun brand white rice vinegar import value from United States (rank 2) = **13,523,057** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为3,817,694升;金额13,523,057美元;总占比18.47%。"
  - p30 United States share of China Hengshun brand white rice vinegar import volume (nu = **18.47** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为3,817,694升;金额13,523,057美元;总占比18.47%。"
  - p31 China Hengshun brand white rice vinegar import volume from South Korea (rank 3), = **3,721,730** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand South Korea figure; not the US.] quote: "第三韩国:总数量为3,721,730升;金额2,898,559美元;总占比18.01%。"
  - p32 China Hengshun brand white rice vinegar import volume from Malaysia (rank 4), 20 = **3,300,015** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Malaysia figure; not the US.] quote: "第四马来西亚:总数量为3,300,015升;金额1,455,937美元;总占比15.97%。"
  - p33 China Hengshun brand white rice vinegar import volume from Italy (rank 5), 2020- = **2,212,699** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Italy figure; not the US.] quote: "第五意大利:总数量为2,212,699升;金额6,492,715美元;总占比10.71%。"
  - p34 China Hengshun brand white rice vinegar import volume from Germany (rank 6), 202 = **763,124** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Germany figure; not the US.] quote: "第六德国:总数量为763,124升;金额1,628,043美元;总占比3.69%。"
  - p35 China Hengshun brand white rice vinegar import volume from Taiwan (rank 7), 2020 = **640,562** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Taiwan figure; not the US.] quote: "第七中国台湾:总数量为640,562升;金额652,997美元;总占比3.10%。"
  - p36 China Hengshun brand white rice vinegar import volume from Spain (rank 8), 2020- = **477,363** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Spain figure; not the US.] quote: "第八西班牙:总数量为477,363升;金额944,600美元;总占比2.31%。"
  - p37 China Hengshun brand white rice vinegar import volume from Hong Kong (rank 9), 2 = **108,839** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Hong Kong figure; not the US.] quote: "第九中国香港:总数量为108,839升;金额391,772美元;总占比0.53%。"
  - p38 China Hengshun brand white rice vinegar import volume from Belgium (rank 10), 20 = **72,837** liters (2020-01-01..2022-12-31) [DISCARD: Hengshun-brand Belgium figure; not the US.] quote: "第十比利时:总数量为72,837升;金额146,414美元;总占比0.35%。"
  - p39 Number of countries China Hengshun brand white rice vinegar was imported from, 2 = **38** countries (2020-01-01..2022-12-31) [DISCARD: Count of source countries in the ambiguous p26 dataset; no bearing on US volume.] quote: "近三年来,恒顺牌白米醋(HS22090000)共从海外38个国家进口,总计20,664,582升,3,430万美元。"
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 6/6
  - p40 Total US customs shipments recorded for Jiangsu Hengshun Group (cumulative, 2006 = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p41 Number of trading partners for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p42 Number of ports used by Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p43 Bottle size of Chinkiang vinegar (Asian Taste brand) in a Hengshun bill of ladin = **550** mL per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p44 Bottles per case for Chinkiang vinegar (550ML@24) in a Hengshun bill of lading = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p45 Piece count on a Hengshun Chinkiang vinegar bill of lading (arrival 2022-08-13) = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://oec.world/zh/profile/bilateral-product/vinegar/reporter/usa` -> **live_dated** (page date 2024-11-01); points raw/verified 0/0
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d4 [capacity_consumption] Hengshun production and export capacity

Hypothesis: Hengshun total vinegar production capacity × export share × US share of exports gives US volume; convert tons to bottles at ~1 kg per 500ml bottle. Target = capacity × utilization × export share × US share ÷ bottle mass.

Queries issued by the searcher: 恒顺醋业 产能 产量 万吨 年报; 恒顺醋业 出口 占比 海外收入; 恒顺香醋 出口 美国 市场 占比 海外销售; 中国 食醋 出口 美国 金额 占比 海关 2024

- `http://rdfile.dzh.com.cn/new/dzh/tb_gg/2026/4/15/77AA686320AA5087BD02D34CD73424CE_12089193.pdf` -> **live_dated** (page date 2026-04-14); points raw/verified 14/8
  - p46 Hengshun vinegar (醋系列) production volume 2025, tons = **235,643** tons (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 吨 235,643.35 228,113.05 18,409.49 11.87 7.22 69.22"
  - p47 Hengshun vinegar (醋系列) sales volume 2025, tons = **228,113** tons (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 吨 235,643.35 228,113.05 18,409.49 11.87 7.22 69.22"
  - p48 Hengshun foreign trade (外贸模式) revenue 2025, CNY = **39,171,647** CNY (2025-01-01..2025-12-31) [keep: ] quote: "外贸 模式 39,171,647.23 29,715,440.56 24.14 -17.95 -14.38 减少 3.16"
  - p49 Hengshun total main business revenue 2025 (denominator for export share), CNY = **2,266,466,159** CNY (2025-01-01..2025-12-31) [keep: ] quote: "小计 2,266,466,159.39 1,537,411,067.26 32.17 8.29 13.18 减少2.93个百分点"
  - p50 Hengshun vinegar (醋系列) revenue 2025, CNY = **1,321,092,496** CNY (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 1,321,092,495.56 709,855,429.02 46.27 4.38 2.57 增加 0.95"
  - p51 Hengshun condiment (调味品) revenue 2025, CNY = **2,266,466,159** CNY (2025-01-01..2025-12-31) [keep: ] quote: "调味品 2,266,466,159.39 1,537,411,067.26 32.17 8.29 13.18 减少 2.93"
  - p52 Hengshun total revenue 2025, CNY = **2,286,538,594** CNY (2025-01-01..2025-12-31) [keep: ] quote: "营业收入 2,286,538,593.94 2,195,870,508.45 4.13 2,106,410,685.37"
  - p53 Hengshun foreign trade revenue 2024 (prior year comparison), CNY = **29,715,441** CNY (2024-01-01..2024-12-31) [keep: ] quote: "外贸 模式 39,171,647.23 29,715,440.56 24.14 -17.95 -14.38 减少 3.16"
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 14/0
- `https://www.renrendoc.com/paper/157916955.html` -> **live_dated** (page date 2021-10-25); points raw/verified 12/2
  - p54 Hengshun vinegar business revenue 2014 (CNY) = **1,040,000,000** CNY (2014-01-01..2014-12-31) [DISCARD: 2014 Hengshun vinegar revenue is superseded by 2024/2025 annual-report figures (p50, p59); redundant and stale.] quote: "2014年,海天味业酱油业务营收达到63亿元,占行业比重为9.84%,恒顺醋业醋业务营收达到10.4亿元,行业占比约为3.85%"
  - p55 Hengshun vinegar business share of vinegar industry 2014 (percent) = **3.85** % (2014-01-01..2014-12-31) [DISCARD: 2014 industry-share figure is stale and not used in any current route; superseded by current revenue data.] quote: "恒顺醋业醋业务营收达到10.4亿元,行业占比约为3.85%"
- `https://m.canyin88.com/zixun/2025/12/02/110232.html` -> **live_dated** (page date 2025-12-02); points raw/verified 13/11
  - p56 Hengshun vinegar series production volume 2024 = **210,600** tons (2024-01-01..2024-12-31) [keep: ] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨"
  - p57 Hengshun vinegar series sales volume 2024 = **212,700** tons (2024-01-01..2024-12-31) [keep: ] quote: "销量也超过21.27万吨"
  - p58 Hengshun total revenue 2024 = **2,196,000,000** CNY (2024-01-01..2024-12-31) [keep: ] quote: "去年,其总营收为21.96亿元"
  - p59 Hengshun vinegar series revenue 2024 = **1,266,000,000** CNY (2024-01-01..2024-12-31) [keep: ] quote: "醋系列就实现12.66亿元,占据过半营收"
  - p60 Hengshun vinegar series revenue H1 2025 = **739,000,000** CNY (2025-01-01..2025-06-30) [DISCARD: H1 2025 vinegar revenue; superseded by full-year p50 and not needed for the export route.] quote: "醋系列仍是恒顺醋业的营收主力,贡献了7.39亿元收入"
  - p61 Hengshun wine and sauce series combined revenue H1 2025 = **231,000,000** CNY (2025-01-01..2025-06-30) [DISCARD: H1 2025 wine/sauce revenue; irrelevant to vinegar exports.] quote: "酒系列、酱系列的销售收入合计仅2.31亿元左右"
  - p62 Hengshun wine series revenue year-on-year change H1 2025 = **5.42** % (2025-01-01..2025-06-30) [DISCARD: H1 2025 wine series change; irrelevant.] quote: "分别同比减少了5.42%、3.53%"
  - p63 Hengshun sauce series revenue year-on-year change H1 2025 = **3.53** % (2025-01-01..2025-06-30) [DISCARD: H1 2025 sauce series change; irrelevant.] quote: "分别同比减少了5.42%、3.53%"
  - p64 Hengshun offline distributors covered as of end-2024 = **1,700** distributors (2024-12-31..2024-12-31) [DISCARD: Domestic distributor count; domestic channel, not US exports.] quote: "恒顺醋业已经覆盖全国超1700家经销商"
  - p65 Hengshun terminal outlets as of end-2024 = **350,000** outlets (2024-12-31..2024-12-31) [DISCARD: Domestic terminal outlets; not US exports.] quote: "终端网点突破35万家"
  - p66 Hengshun self-media cumulative followers as of end-2024 = **280,000** followers (2024-12-31..2024-12-31) [DISCARD: Social-media followers; irrelevant.] quote: "截止去年底累计粉丝超28万"
- dropped by code checks: 32 (period_end missing or unparseable: 15; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; value_as_written not in quote as a whole number: 14; scale word '亿' not supported by quote or table header: 1)

### d5 [base_rates] Bottle size and unit conversion

Hypothesis: Converting tonnage or liters to bottle counts requires average bottle size; Hengshun US exports likely dominated by 500ml glass bottles. Target bottles = volume (liters) ÷ average bottle volume (liters).

Queries issued by the searcher: 恒顺香醋 出口 美国 500ml 包装; Hengshun vinegar 500ml US bottle; Chinkiang vinegar bottle size export; site:fivecontinentsintl.com HengShun Brand Zhenjiang Chinkiang Vinegar 500ml case size; Hengshun Chinkiang vinegar 550ml 24 bottles US distributor; 恒顺 出口 美国 产品 规格 500ml 550ml

- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p67 Hengshun Brand Zhenjiang/Chinkiang Vinegar bottle size (3L SKU) = **3** liters per bottle (..) [DISCARD: Duplicate of the 3L SKU size already captured by p91; adds no information.] quote: "HengShun Brand Zhenjiang / Chinkiang Vinegar(3L)"
  - p68 Hengshun Brand Zhenjiang/Chinkiang Vinegar case pack (bottles per case) = **4** bottles per case (..) [DISCARD: 3L case pack; not needed for bottle-count conversion.] quote: "Case Size: 3L*4btls"
  - p69 Hengshun Brand 9 Degrees Rice Vinegar bottle size = **500** milliliters per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p70 Hengshun Brand Cooking Wine with Shallot And Ginger bottle size = **500** milliliters per bottle (..) [DISCARD: Cooking-wine SKU (not vinegar) and duplicate of p82.] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p71 Hengshun Brand Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** milliliters per bottle (..) [DISCARD: Cooking-wine SKU (not vinegar) and duplicate of p83.] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p72 Hengshun Brand Six Years Vinegar bottle size = **580** milliliters per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p73 Hengshun Brand Vinegar 0 Additives bottle size = **500** milliliters per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p74 Hengshun Brand Vinegar 0 Additives bottle size (535ml SKU) = **535** milliliters per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p75 Hengshun Brand Vinegar for Dumpling bottle size = **500** milliliters per bottle (..) [DISCARD: Duplicate of p87 (500ml dumpling vinegar).] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p76 Hengshun Brand Vinegar for Steamed Buns bottle size = **550** milliliters per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p77 Hengshun Brand White Rice Vinegar bottle size = **500** milliliters per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p78 Hengshun Brand Zhenjiang Eight Years Vinegar bottle size = **300** milliliters per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://fivecontinentsintl.com/en/product/hengshun-brand-vinegar-0-additives/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p79 Hengshun Brand Vinegar 0 Additives bottle size (SKU volume) = **500** ml per bottle (..) [DISCARD: Duplicate of p73 (500ml 0-additives vinegar).] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p80 Hengshun Brand Vinegar 0 Additives case pack (bottles per case) = **12** bottles per case (..) [DISCARD: Case pack; not needed for bottle-count conversion.] quote: "Case Size: 500ml*12btls"
  - p81 Hengshun Brand 9 Degrees Rice Vinegar bottle size = **500** ml per bottle (..) [DISCARD: Duplicate of p69 (500ml rice vinegar).] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p82 Hengshun Brand Cooking Wine with Shallot And Ginger bottle size = **500** ml per bottle (..) [DISCARD: Cooking-wine SKU; not vinegar.] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p83 Hengshun Brand Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** ml per bottle (..) [DISCARD: Cooking-wine SKU; not vinegar.] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p84 Hengshun Brand Six Years Vinegar bottle size = **580** ml per bottle (..) [DISCARD: Duplicate of p72 (580ml six-year).] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p85 Hengshun Brand Three Years Vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p86 Hengshun Brand Vinegar 0 Additives (535ml variant) bottle size = **535** ml per bottle (..) [DISCARD: Duplicate of p74 (535ml).] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p87 Hengshun Brand Vinegar for Dumpling bottle size = **500** ml per bottle (..) [DISCARD: Duplicate of p75 (500ml dumpling).] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p88 Hengshun Brand Vinegar for Steamed Buns bottle size = **550** ml per bottle (..) [DISCARD: Duplicate of p76 (550ml steamed-bun).] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p89 Hengshun Brand White Rice Vinegar bottle size = **500** ml per bottle (..) [DISCARD: Duplicate of p77 (500ml white rice).] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p90 Hengshun Brand Zhenjiang Eight Years Vinegar bottle size = **300** ml per bottle (..) [DISCARD: Duplicate of p78 (300ml eight-year).] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://emmefoods.com/zh/brand/4-%E6%81%92%E9%A1%BA` -> **live_dated** (page date 2007-01-01); points raw/verified 7/7
  - p91 Hengshun large-bucket Zhenjiang aromatic vinegar bottle size (3L) = **3** liters per bottle (..) [keep: ] quote: "恒顺大桶镇江香醋 3L"
  - p92 Hengshun Zhenjiang aromatic vinegar 6-year aged bottle size (580mL) = **580** milliliters per bottle (..) [DISCARD: Duplicate of p72/p84 (580ml six-year).] quote: "恒顺镇江香醋 6年陈 580mL"
  - p93 Hengshun Zhenjiang aromatic vinegar 3-year aged bottle size (580mL) = **580** milliliters per bottle (..) [DISCARD: Duplicate of p85 (580ml three-year).] quote: "恒顺镇江香醋3年陈 580mL"
  - p94 Hengshun Zhenjiang aromatic vinegar 8-year aged bottle size (300mL) = **300** milliliters per bottle (..) [DISCARD: Duplicate of p78/p90 (300ml eight-year).] quote: "恒顺镇江香醋8年熟成 300mL"
  - p95 Hengshun Zhenjiang aromatic vinegar K-type bottle size (550ml) = **550** milliliters per bottle (..) [DISCARD: Duplicate of p96 (550ml).] quote: "恒顺镇江香醋K型 550ml"
  - p96 Hengshun Zhenjiang aromatic vinegar bottle size (550ml) = **550** milliliters per bottle (..) [DISCARD: Duplicate of p95 (550ml).] quote: "恒顺镇江香醋 550ml"
  - p97 Number of Hengshun products listed on this brand page = **5** products (..) [DISCARD: Count of products on a brand page is not a volume or conversion factor; no numerical role.] quote: "这里有5件商品。"
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-

### d6 [persona] US distributor/importer

Hypothesis: Hengshun's US importer/distributor (e.g., Asian food distributors) may disclose shipment volumes or sales; alternatively trade press interviews mention container volumes. Target = containers/year × bottles per container.

Queries issued by the searcher: Hengshun vinegar US distributor importer Chinkiang vinegar; Chinkiang vinegar container shipment US importer; 镇江香醋 美国 经销商 进口 恒顺; "Jiangsu Hengshun" "Well Luck" shipments; "Hengshun" vinegar "container" "20ft" bottles; "Zhenjiang vinegar" export US 2023 tons Hengshun; site:importyeti.com Hengshun vinegar

- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/10
  - p98 Total US customs shipments recorded for Jiangsu Hengshun Group, 2006-11-01 to 20 = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p40 (same ImportGenius shipment count).] quote: "Total Shipments 44"
  - p99 Trading partners recorded for Jiangsu Hengshun Group in US customs data = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p41.] quote: "Trading Partners 6"
  - p100 Ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p42.] quote: "Ports 5"
  - p101 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p45 (same bill of lading piece count).] quote: "Piece Count 700"
  - p102 Bottle size in Chinkiang vinegar shipment description (550ML@24) = **550** ml per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p43 (550 mL).] quote: "Description VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p103 Bottles per case in Chinkiang vinegar shipment description (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p44 (24 bottles/case).] quote: "Description VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p104 Container length on bill of lading EGLV142252207486 (20 Foot General Purpose Con = **20** feet (2022-08-13..2022-08-13) [DISCARD: Container length; not needed for bottle-count conversion.] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
  - p105 Container length field on bill of lading EGLV142252207486 = **240** container length units (as recorded) (2022-08-13..2022-08-13) [DISCARD: Container dimension field in ambiguous units; not usable as a volume without a defined unit.] quote: "Length 240"
  - p106 Container height field on bill of lading EGLV142252207486 = **102** container height units (as recorded) (2022-08-13..2022-08-13) [DISCARD: Container dimension field in ambiguous units; not usable.] quote: "Height 102"
  - p107 Container width field on bill of lading EGLV142252207486 = **96** container width units (as recorded) (2022-08-13..2022-08-13) [DISCARD: Container dimension field in ambiguous units; not usable.] quote: "Width 96"
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%90%84%E4%BA%9E%E6%B4%B2%E8%B6%85%E5%B8%82%E6%8E%A8%E5%87%BA%E6%81%86%E9%A0%86%E7%B3%BB%E5%88%97%E7%94%A2%E5%93%81%E9%BB%` -> **live_dated** (page date 2024-11-29); points raw/verified 3/1
  - p108 Hengshun brand US agent/distributor company name (Well Luck Co., Inc) — no volum = **1,840** year (brand founding year) (1840-01-01..1840-12-31) [DISCARD: Value is the brand founding year (1840), not a volume; the distributor name is qualitative only and cannot enter a numer] quote: "恆順品牌始於1840年清朝道光年間,迄今已有185多年曆史。"
- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **live_dated** (page date 2024-11-01); points raw/verified 2/0
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### d7 [forecasts_markets] Industry and trade forecasts

Hypothesis: Chinese vinegar industry reports or Hengshun guidance may state export growth targets or US market plans; these constrain the scale and direction but are intentions, not realized sales. Target = prior-year estimate × (1 + stated growth).

Queries issued by the searcher: 恒顺醋业 海外 扩张 美国 计划 出口; Hengshun vinegar overseas expansion US export growth; 恒顺醋业 2024年 年报 境外 营业收入 出口; 中国 食醋 出口 美国 万吨 2024 海关 220900

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0

### d8 [attention] US retail/e-commerce presence

Hypothesis: Hengshun product listings and review counts on Amazon/Walmart/Asian grocers can proxy relative sales volume; combined with category sales estimates gives a rough bottle count. Target = US Chinese vinegar category sales × Hengshun share (from review/listing proxy).

Queries issued by the searcher: Hengshun vinegar Amazon US reviews Chinkiang vinegar; Chinese black vinegar US market size; 恒顺醋业 2024年报 境外收入 出口 调味品; China vinegar exports to United States volume tons annual customs statistics

- `https://www.marketresearch.com/LP-Information-Inc-v4134/Global-Black-Vinegar-Growth-42230027/` -> **live_dated** (page date 2025-09-09); points raw/verified 4/1
  - p109 Global Black Vinegar market size, 2025 (forecast) = **193,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global black-vinegar market size is a different product category and not Hengshun-specific; irrelevant to Hengshun US bo] quote: "The global Black Vinegar market size is predicted to grow from US$ 193 million in 2025 to US$ 270 million in 2031"
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://cfi.cn/p20250422000502.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.sayweee.com/ko/product/Zhengjiang-Vinegar--3-Year/12908` -> **live_dated** (page date 2026-10-18); points raw/verified 4/0
- dropped by code checks: 7 (period_end 2031-12-31 after as_of: 2; period_end missing or unparseable: 5)

### b1 [related_series] trade statistics

Hypothesis: US Census/UN Comtrade imports of HS 22090000 from China for 2024-2025 give a current US-bound Chinese vinegar volume; combined with a Hengshun brand share this completes the d3 route and replaces the stale 2020-2022 p12 figure.

Queries issued by the searcher: US imports HS 22090000 vinegar from China 2024 liters; UN Comtrade HS 220900 vinegar China exports United States 2024; USITC DataWeb 2209000000 China imports 2025; OEC vinegar United States imports from China 2024 2025; "220900" "China" "United States" imports 2025 quantity kg; US Census imports 220900 China 2024 quantity liters vinegar; UN Comtrade 220900 USA imports China 2024 netweight

- `https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=842&period=2024%2C2025&partnerCode=156&cmdCode=220900&flowCode=M` -> **dropped** (live http 400); points raw/verified -/-
- `https://dataweb.usitc.gov/trade/search/Import/HTS` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://hs.bianmachaxun.com/report_hs_22090000` -> **live_dated** (page date 2021-01-01); points raw/verified 15/15
  - p110 China total vinegar export volume, 2021 = **20,249,374** liters (2021-01-01..2021-12-31) [DISCARD: Duplicate of p125 (2021 China vinegar export volume).] quote: "\| 2021年 \| 20249374 \| $25590784 \| $1.26 /升 \|"
  - p111 China total vinegar export volume, 2020 = **17,414,624** liters (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 \| 17414624 \| $23362688 \| $1.34 /升 \|"
  - p112 China total vinegar export volume, 2019 = **16,866,780** liters (2019-01-01..2019-12-31) [keep: ] quote: "\| 2019年 \| 16866780 \| $20005507 \| $1.19 /升 \|"
  - p113 China total vinegar export volume, 2018 = **16,095,699** liters (2018-01-01..2018-12-31) [keep: ] quote: "\| 2018年 \| 16095699 \| $19047798 \| $1.18 /升 \|"
  - p114 China total vinegar export volume, 2017 = **14,887,337** liters (2017-01-01..2017-12-31) [keep: ] quote: "\| 2017年 \| 14887337 \| $16936013 \| $1.14 /升 \|"
  - p115 China vinegar export share to United States, 2021 = **11** % (2021-01-01..2021-12-31) [DISCARD: Duplicate of p127 (2021 US share).] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p116 China vinegar export value to United States, 2021 = **2,702,517** USD (2021-01-01..2021-12-31) [DISCARD: Duplicate of p128 (2021 US export value).] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p117 China vinegar export average price to United States, 2021 = **1.37** USD per liter (2021-01-01..2021-12-31) [DISCARD: Duplicate of p129 (2021 US unit price).] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p118 China vinegar export share to United States, 2020 = **11** % (2020-01-01..2020-12-31) [DISCARD: Duplicate of p130 (2020 US share).] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p119 China vinegar export value to United States, 2020 = **2,484,932** USD (2020-01-01..2020-12-31) [DISCARD: Duplicate of p131 (2020 US export value).] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p120 China vinegar export average price to United States, 2020 = **1.21** USD per liter (2020-01-01..2020-12-31) [DISCARD: Duplicate of p132 (2020 US unit price).] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p121 China vinegar export share to United States, 2019 = **10** % (2019-01-01..2019-12-31) [DISCARD: Duplicate of p133 (2019 US share).] quote: "\| \| 美国 \| 10% \| $1932681 \| $1.17 \|"
  - p122 China vinegar export value to United States, 2019 = **1,932,681** USD (2019-01-01..2019-12-31) [DISCARD: Duplicate of p134 (2019 US export value).] quote: "\| \| 美国 \| 10% \| $1932681 \| $1.17 \|"
  - p123 China vinegar export share to United States, 2018 = **14** % (2018-01-01..2018-12-31) [DISCARD: Duplicate of p135 (2018 US share).] quote: "\| \| 美国 \| 14% \| $2662832 \| $1.2 \|"
  - p124 China vinegar export value to United States, 2018 = **2,662,832** USD (2018-01-01..2018-12-31) [DISCARD: Duplicate of p136 (2018 US export value).] quote: "\| \| 美国 \| 14% \| $2662832 \| $1.2 \|"

### b2 [own_history] company disclosure

Hypothesis: Hengshun annual report segment/regional breakdown or investor Q&A may disclose overseas revenue split by region or US export volume, directly resolving the US share of the 39.2M CNY foreign-trade revenue (p48).

Queries issued by the searcher: 恒顺醋业 2025年年度报告 境外 营业收入 分地区; 恒顺醋业 年报 外贸 营业收入 境外 分地区 醋; 中国 食醋 出口 美国 数量 吨 平均价格 海关 2209 2025; Hengshun vinegar 500ml price Amazon US Chinkiang vinegar import

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 14/0
- `https://www.sohu.com/a/821678279_121823071` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://hs.bianmachaxun.com/report_hs_22090000` -> **live_dated** (page date 2021-01-01); points raw/verified 15/15
  - p125 China total vinegar export volume 2021 (all destinations) = **20,249,374** liters (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 \| 20249374 \| $25590784 \| $1.26 /升 \|"
  - p126 China total vinegar export value 2021 (all destinations) = **25,590,784** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 \| 20249374 \| $25590784 \| $1.26 /升 \|"
  - p127 China vinegar export share to United States 2021 = **11** % (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p128 China vinegar export value to United States 2021 = **2,702,517** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p129 China vinegar export average price to United States 2021 = **1.37** USD per liter (2021-01-01..2021-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2702517 \| $1.37 \|"
  - p130 China vinegar export share to United States 2020 = **11** % (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p131 China vinegar export value to United States 2020 = **2,484,932** USD (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p132 China vinegar export average price to United States 2020 = **1.21** USD per liter (2020-01-01..2020-12-31) [keep: ] quote: "\| \| 美国 \| 11% \| $2484932 \| $1.21 \|"
  - p133 China vinegar export share to United States 2019 = **10** % (2019-01-01..2019-12-31) [keep: ] quote: "\| \| 美国 \| 10% \| $1932681 \| $1.17 \|"
  - p134 China vinegar export value to United States 2019 = **1,932,681** USD (2019-01-01..2019-12-31) [keep: ] quote: "\| \| 美国 \| 10% \| $1932681 \| $1.17 \|"
  - p135 China vinegar export share to United States 2018 = **14** % (2018-01-01..2018-12-31) [keep: ] quote: "\| \| 美国 \| 14% \| $2662832 \| $1.2 \|"
  - p136 China vinegar export value to United States 2018 = **2,662,832** USD (2018-01-01..2018-12-31) [keep: ] quote: "\| \| 美国 \| 14% \| $2662832 \| $1.2 \|"
  - p137 China vinegar export share to United States 2017 = **12** % (2017-01-01..2017-12-31) [DISCARD: Duplicate of p135/p123 family; 2017 US share already represented by p135/p123 trend.] quote: "\| \| 美国 \| 12% \| $2054779 \| $1.17 \|"
  - p138 China vinegar export value to United States 2017 = **2,054,779** USD (2017-01-01..2017-12-31) [DISCARD: 2017 US export value; not needed for the volume route.] quote: "\| \| 美国 \| 12% \| $2054779 \| $1.17 \|"
  - p139 China total vinegar export volume 2017 (all destinations) = **14,887,337** liters (2017-01-01..2017-12-31) [DISCARD: Duplicate of p114 (2017 China vinegar export volume).] quote: "\| 2017年 \| 14887337 \| $16936013 \| $1.14 /升 \|"
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0
- dropped by code checks: 14 (value_as_written not in quote as a whole number: 14)

### b3 [base_rates] brand share

Hypothesis: Hengshun's share of Chinese vinegar sold in the US Asian-grocery channel (from retail scan data, Amazon share, or distributor catalogs) is the key uncertain multiplier in the d3 route; a defensible share estimate would materially tighten the estimate.

Queries issued by the searcher: Hengshun vinegar US market share Chinese vinegar retail; Chinkiang vinegar US imports volume customs statistics; 恒顺醋业 年报 2024 境外 营业收入 出口; 镇江香醋 出口 美国 数量 吨 2024

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.qyresearch.com/reports/4704078/vinegar` -> **dropped** (live page has no readable date); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us', 'zhenjiang vinegar']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p7'] Same 2025 China HS 22090000 export record: volume, value, and implied unit price are internally consistent (value/volume ≈ 1.11 USD/L). One measurement, not three independent ones.
- corroborating: ['p3', 'p4', 'p8'] Same 2024 China HS 22090000 export record; internally consistent. Independent year from p1/p2 but same source family (customs-derived aggregator).
- corroborating: ['p5', 'p6', 'p9'] Same 2023 China HS 22090000 export record; internally consistent.
- corroborating: ['p1', 'p3', 'p5'] Consistent multi-year series of China vinegar export volume (21.8M → 25.8M → 25.4M L), usable as a stable denominator for share-based routes.
- corroborating: ['p12', 'p13', 'p14', 'p15'] US cumulative 2020-2022 quantity/value and 11.35% share are mutually consistent with the worldwide total (6.60M/58.12M ≈ 11.35%). One source, one period.
- corroborating: ['p12', 'p17', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25'] Destination breakdown sums plausibly toward the worldwide total; US is the #2 destination. Same source and period, so not independent of each other.
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39'] Hengshun-brand 'white rice vinegar' import breakdown by country, 2020-2022 cumulative; shares sum to ~100%. Internally consistent but the label ('imported from 38 countries' for a Chinese brand) is se
- corroborating: ['p28', 'p29', 'p30'] US quantity, value, and 18.47% share are mutually consistent (3.82M/20.66M ≈ 18.47%).
- corroborating: ['p40', 'p98'] Duplicate records of the same ImportGenius shipment count (44 shipments, 2006-2022). Same underlying source.
- corroborating: ['p41', 'p99'] Duplicate: 6 trading partners, same ImportGenius source.
- corroborating: ['p42', 'p100'] Duplicate: 5 ports, same ImportGenius source.
- corroborating: ['p43', 'p102'] Same bill-of-lading bottle size (550 mL).
- corroborating: ['p44', 'p103'] Same bill-of-lading case pack (24 bottles/case).
- corroborating: ['p45', 'p101'] Same bill-of-lading piece count (700).
- corroborating: ['p46', 'p47', 'p50', 'p51', 'p52'] 2025 annual-report figures: vinegar production/sales tonnage and revenue, condiment revenue, total revenue — internally consistent company disclosure.
- corroborating: ['p48', 'p49', 'p53'] Foreign-trade revenue 2025 (39.2M CNY) vs 2024 (29.7M CNY) and total main-business revenue give an export share of total revenue; consistent within the annual report.
- corroborating: ['p56', 'p57', 'p58', 'p59'] 2024 vinegar production/sales tonnage and revenue from a secondary article; broadly consistent with 2025 annual-report magnitudes.
- corroborating: ['p67', 'p68', 'p91'] 3L large-format SKU appears in both distributor listings; consistent bottle size.
- corroborating: ['p69', 'p73', 'p75', 'p77', 'p79', 'p81', 'p82', 'p83', 'p87', 'p89'] 500 mL is the modal Hengshun SKU size across the distributor catalog; supports a 500 mL average-bottle assumption.
- corroborating: ['p72', 'p84', 'p85', 'p92', 'p93'] 580 mL aged-vinegar SKUs consistent across two listings.
- corroborating: ['p78', 'p90', 'p94'] 300 mL 8-year SKU consistent across listings.
- corroborating: ['p76', 'p88', 'p95', 'p96'] 550 mL SKUs consistent across listings and the bill of lading.
- conflicting: ['p12', 'p28'] China total US vinegar exports 2020-2022 (6.60M L) vs Hengshun-brand US 'imports' (3.82M L) would imply Hengshun is ~58% of all Chinese vinegar to the US — implausibly high for one brand and suggests 
- conflicting: ['p40', 'p45'] Only 44 US customs shipments over 16 years (≈3/yr) is far too small to carry millions of liters; the ImportGenius record likely captures only a subset of Hengshun's US trade (or a single importer). Co
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p7'] Same 2025 China HS 22090000 export record: volume, value and unit price are internally consistent (value/volume = price). One measurement, not three independent ones.
- corroborating: ['p3', 'p4', 'p8'] Same 2024 export record; consistent internally. Forms a series with p1/p2/p7 and p5/p6/p9.
- corroborating: ['p5', 'p6', 'p9'] Same 2023 export record; consistent internally.
- corroborating: ['p1', 'p3', 'p5'] Consistent year-over-year series of China vinegar export volume (21.8M L 2023, 25.8M L 2024, 25.4M L 2025); same source family (hs.bianmachaxun.com), so not independent of each other but a coherent tr
- corroborating: ['p110', 'p111', 'p112', 'p113', 'p114', 'p125', 'p139'] Earlier-year China vinegar export volumes from the same source family; p110 and p125 are duplicate records of 2021 and should not be treated as two observations.
- corroborating: ['p12', 'p13', 'p14', 'p15'] US cumulative 2020-2022 quantity/value and the 11.35% US share are internally consistent with the worldwide total p15 (6.60M/58.12M ≈ 11.35%).
- corroborating: ['p14', 'p115', 'p118', 'p121', 'p123', 'p127', 'p130', 'p133', 'p135', 'p137'] US share of China vinegar exports is stable at roughly 10-14% across 2017-2022 from two related sources; supports using ~11% as a transferable share for 2025.
- corroborating: ['p26', 'p28', 'p29', 'p30'] Hengshun-brand 'import' figures are internally consistent (US 3.82M L, 18.47% of 20.66M L total). Note the framing is confusing (labelled imports into China from 38 countries) and the period is 2020-2
- conflicting: ['p28', 'p12'] Hengshun-brand US volume (3.82M L over 2020-2022) is ~58% of all China-to-US vinegar volume in the same period (6.60M L), which is implausibly high for one brand and suggests the p26-p38 dataset measu
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p104'] US customs bill-of-lading evidence for Hengshun: 44 shipments 2006-2022, 6 partners, 5 ports, 550ml@24 case pack, 700 pieces, 20ft container. Establishes bottle format and shipment mechanics but not a
- corroborating: ['p46', 'p47', 'p50', 'p51', 'p52', 'p49'] 2025 annual-report figures: vinegar production 235.6kt, sales 228.1kt, vinegar revenue 1.32bn CNY, condiment revenue 2.27bn CNY, total revenue 2.29bn CNY. Internally consistent (implied ~5.8 CNY/kg vi
- corroborating: ['p48', 'p53'] Foreign-trade revenue 39.2M CNY in 2025 vs 29.7M CNY in 2024 (+24%); same annual-report table.
- corroborating: ['p56', 'p57', 'p58', 'p59'] 2024 vinegar production 210.6kt, sales 212.7kt, total revenue 2.196bn CNY, vinegar revenue 1.266bn CNY — consistent with the 2025 annual-report prior-year column.
- corroborating: ['p67', 'p68', 'p69', 'p72', 'p73', 'p74', 'p76', 'p77', 'p78', 'p80', 'p85', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96'] Product-catalogue bottle sizes cluster at 500ml (most common), 550ml, 580ml, 300ml and 3L; supports a ~0.5L average bottle with a modest spread.
- corroborating: ['p69', 'p81', 'p70', 'p82', 'p71', 'p83', 'p73', 'p79', 'p75', 'p87', 'p77', 'p89', 'p72', 'p84', 'p74', 'p86', 'p76', 'p88', 'p78', 'p90', 'p92', 'p93', 'p94', 'p95', 'p96'] Many duplicate records of the same SKU sizes across two catalogue snapshots; they add no independent information beyond the size distribution.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Hengshun share of US-bound Chinese vinegar volume | 12 | 4..30 | 4..30 | % | m1 (m2) | Hengshun is China's largest vinegar producer but Chinese vinegar exports to the US are spread across many regional producers and unbranded bulk; the p26-p38 keyword-matched table implies an implausible ~58% share, so we anchor well below it. 12% is consistent with Hengshun being the leading branded  | Used to convert total China-to-US vinegar volume into Hengshun's US-bound volume. | Retail scan, distributor or customs data showing Hengshun holds a much larger or much smaller share of US Chinese-vinegar volume. |
| a2 | Average Hengshun US bottle size | 0.5 | 0.3..0.58 | 0.295..0.5899 (widened) | liters per bottle | m1 (m2), m2 (m3) | US distributor catalogues (p79, p81, p87, p89) and the 2022 bill of lading (p43, 550ml) cluster at 500-550ml, with 580ml, 535ml, 300ml and 3L variants; 500ml is the modal retail size for US Asian-grocery Chinkiang vinegar. | Converts liters of Hengshun US-bound vinegar into bottle counts. | Evidence that US-bound Hengshun shipments are predominantly bulk or large-format (3L+) rather than 500ml retail bottles. |
| a3 | US share of Hengshun foreign-trade revenue | 20 | 8..40 | 8..40 | % | m2 (m3) | Hengshun's overseas sales span Southeast Asia, Japan, Europe and North America; the US is a major but not dominant market. The p28/p30 table (18.5% US share of a Hengshun-labelled overseas flow) supports a value near 20%, though that table's scope is ambiguous. | Used to split Hengshun's 2025 foreign-trade revenue into the US portion. | Disclosure of regional export revenue showing the US is a much smaller or much larger fraction. |
| a4 | Hengshun export price per liter (CNY) | 10.5 | 7..18 | 7..18 | CNY per liter | m2 (m3) | China average vinegar export price is ~1.1-1.2 USD/L (p7, p8, p9); at ~7.1 CNY/USD that is ~8 CNY/L. Hengshun is a premium branded Zhenjiang vinegar, so its export price should sit above the national average, near 10.5 CNY/L. Stated in CNY so it is directly compatible with p48. | Converts Hengshun US foreign-trade revenue (CNY) into liters. | Evidence that Hengshun export prices are at or below the national average, or far above 18 CNY/L. |
| a5 | Hengshun export share of total revenue | 1.7 | 1..3 | 1..3 | % | unused | Foreign-trade revenue 39.2M CNY (p48) over total revenue 2.29bn CNY (p52) is ~1.7%; this assumption is a cross-check factor for the capacity route, consistent with the observed ratio. | Used in the capacity-times-export-share route to scale total vinegar sales to export volume. | Evidence that foreign-trade revenue includes substantial non-vinegar products or that export share differs materially. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 760,105 | ['p1', 'p14'] / ['a1', 'a2'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 1,483,531 | ['p48'] / ['a2', 'a3', 'a4'] | [] |  | 0.50 | equal |  |
| m3 | formula_mc | n/a | ['p47'] / ['a2', 'a3', 'a5'] | [] |  | 0.00 |  | formula: numeric constant 1000 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the u |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **1,061,904** bottle/year, 80% interval [355,603, 3,171,068] bottle/year, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 7 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 1 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p46 | Hengshun vinegar (醋系列) production volume 2025, tons | 235,643 | tons | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Production volume in tons for all vinegar, not US export bottle count; wrong measure, unit, and scope. |
| p47 | Hengshun vinegar (醋系列) sales volume 2025, tons | 228,113 | tons | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Total vinegar sales volume in tons, not US-specific export volume in bottles; wrong measure, unit, and scope. |
| p48 | Hengshun foreign trade (外贸模式) revenue 2025, CNY | 39,171,647 | CNY | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Foreign trade revenue in CNY, not a bottle count and not US-specific; wrong measure and unit. |
| p49 | Hengshun total main business revenue 2025 (denominator for export share), CNY | 2,266,466,159 | CNY | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Total main business revenue in CNY, not US export bottle count; wrong measure and scope. |
| p50 | Hengshun vinegar (醋系列) revenue 2025, CNY | 1,321,092,496 | CNY | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Vinegar segment revenue in CNY, not US export bottle count; wrong measure and scope. |
| p51 | Hengshun condiment (调味品) revenue 2025, CNY | 2,266,466,159 | CNY | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Condiment revenue in CNY, not US export bottle count; wrong measure and scope. |
| p52 | Hengshun total revenue 2025, CNY | 2,286,538,594 | CNY | 2025-01-01..2025-12-31 | rdfile.dzh.com.cn | different | Total company revenue in CNY, not US export bottle count; wrong measure and scope. |


## Final answer

Best estimate: 1,061,904 bottle/year of Hengshun bottled vinegar exported to the United States in calendar year 2025 (all bottle types combined), with a model-based 80% model-based interval of 355,603 to 3,171,068 bottle/year. This is an export-shipment interpretation, not US retail sales.

Two routes were averaged at equal weight. The volume route multiplies China's total vinegar export volume (25,428,030 liters) by the US share (11.35%) and by Hengshun's assumed share (12%, range 4% to 30%), then converts liters to bottles at 0.5 L per bottle. The company route splits Hengshun's 2025 foreign-trade revenue (39,171,647 CNY) by an assumed US share (20%) and export price (10.5), then converts to bottles. A third capacity route was dropped for a formula error.

Only the export volume, US share, foreign-trade revenue and vinegar tonnage are observed; the Hengshun share, US revenue share, price and bottle size are analyst assumptions. The interval reflects input uncertainty only, not demonstrated accuracy. The biggest risk is that Hengshun's US-bound volume is largely bulk rather than retail bottles, or that foreign-trade revenue includes non-vinegar goods. US-specific customs or bill-of-lading data for Hengshun would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Hengshun share of US-bound Chinese vinegar volume: 12%, range 4% to 30%; used by m1. Overturned by: Retail scan, distributor or customs data showing Hengshun holds a much larger or much smaller share of US Chinese-vinegar volume.
- a2 Average Hengshun US bottle size: 0.5 liters per bottle, range 0.295 to 0.5899 (range widened by code); used by m1, m2. Overturned by: Evidence that US-bound Hengshun shipments are predominantly bulk or large-format ([n]L+) rather than [n]ml retail bottles.
- a3 US share of Hengshun foreign-trade revenue: 20%, range 8% to 40%; used by m2. Overturned by: Disclosure of regional export revenue showing the US is a much smaller or much larger fraction.
- a4 Hengshun export price per liter (CNY): 10.5 CNY per liter, range 7 to 18; used by m2. Overturned by: Evidence that Hengshun export prices are at or below the national average, or far above [n] CNY/L.

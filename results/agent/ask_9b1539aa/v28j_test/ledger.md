# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types combined, excluding bulk/industrial drums) sold/exported to the United States by Jiangsu Hengshun Group (镇江恒顺集团 / 江苏恒顺醋业股份有限公司) in a full calendar year | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; Hengshun Group / Jiangsu Hengshun Vinegar-Industry Co., Ltd. (SH:600305) annual report and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Hengshun corporate reporting

Hypothesis: Hengshun's annual report discloses total revenue and possibly overseas/export revenue or volume; overseas revenue × US share of overseas revenue gives US export value, which divided by average export bottle price gives bottle count. Direction: higher overseas revenue implies more US bottles.

Queries issued by the searcher: 恒顺醋业 年报 境外收入 出口; 江苏恒顺醋业 2024年年度报告 营业收入 境外; 恒顺醋业 2024年年度报告 分地区 境外 营业收入 外贸 4774.10万元; 恒顺醋业 2024 醋系列 销量 吨 生产量 销售量 年报

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://m.tianyancha.com/pilu/announcement/ecb34582b36dfab937c972937a835563` -> **dropped** (live http 419); points raw/verified -/-

### d2 [related_series] China customs / trade statistics

Hypothesis: China customs HS 2209 (vinegar and substitutes) export data to the US gives total Chinese vinegar exported to the US in tonnes/USD; Hengshun's share of China's vinegar exports (or of branded exports) times that total, converted by bottle fill, gives US bottles. Direction: larger US imports or larger Hengshun share raises the estimate.

Queries issued by the searcher: China vinegar exports to United States HS 220900 volume tonnes; 中国 海关 醋 出口 美国 HS 2209 数量 吨; 恒顺醋业 2024年 年报 境外 营业收入 出口 占比; 镇江香醋 出口 美国 数量 吨 恒顺 出口量

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p1 China HS 22090000 vinegar exports to United States, volume, cumulative 2020-01 t = **6,597,078** litres (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p2 China HS 22090000 vinegar exports to United States, value in USD, cumulative 202 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p3 United States share of China HS 22090000 vinegar export volume, cumulative 2020- = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p4 China HS 22090000 vinegar exports worldwide, total volume, cumulative 2020-01 to = **58,119,878** litres (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p5 Number of destination countries for China HS 22090000 vinegar exports, cumulativ = **129** countries (2020-01-01..2022-12-31) [DISCARD: Destination-country count; irrelevant.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p6 China HS 22090000 vinegar exports to Hong Kong, volume, cumulative 2020-01 to 20 = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Hong Kong volume; not the US target.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p7 China HS 22090000 vinegar exports to Hong Kong, value in USD, cumulative 2020-01 = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Hong Kong value; not the US target.] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p8 Hong Kong share of China HS 22090000 vinegar export volume, cumulative 2020-01 t = **23.44** % (2020-01-01..2022-12-31) [DISCARD: Hong Kong share; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p9 China HS 22090000 vinegar exports to Singapore, volume, cumulative 2020-01 to 20 = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Singapore volume; not the US target.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p10 China HS 22090000 vinegar exports to Australia, volume, cumulative 2020-01 to 20 = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Australia volume; not the US target.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p11 China HS 22090000 vinegar exports to Netherlands, volume, cumulative 2020-01 to  = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Netherlands volume; not the US target.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p12 China HS 22090000 vinegar exports to Malaysia, volume, cumulative 2020-01 to 202 = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Malaysia volume; not the US target.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p13 China HS 22090000 vinegar exports to Canada, volume, cumulative 2020-01 to 2022- = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Canada volume; not the US target.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p14 China HS 22090000 vinegar exports to Japan, volume, cumulative 2020-01 to 2022-1 = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Japan volume; not the US target.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] US import statistics

Hypothesis: US Census/BEA import data for HS 2209 from China gives total Chinese vinegar entering the US; Hengshun's brand share of Chinese vinegar sold in the US (from retail scan or distributor data) times total, converted by bottle size, gives bottles. Direction: consistent with d2 but from the destination side, providing an independent check.

Queries issued by the searcher: US imports HS 2209 vinegar from China volume 2023 2024; Hengshun vinegar US retail market share Chinese vinegar; OEC United States imports vinegar from China 2024 value; 恒顺醋业 2024年报 境外 营业收入 出口 占比

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p15 China exports of HS22090000 (vinegar and vinegar substitutes) to the United Stat = **6,597,078** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p1 (same customs measurement, d3 framing).] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p16 China exports of HS22090000 to the United States, total value, 2020-2022 cumulat = **8,459,027** US dollars (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p2.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p17 United States share of China's total HS22090000 export quantity, 2020-2022 cumul = **11.35** percent (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p3.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p18 China total exports of HS22090000 to all countries, quantity, 2020-2022 cumulati = **58,119,878** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p4.] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p19 Number of destination countries for China's HS22090000 exports, 2020-2022 cumula = **129** countries (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p5.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p20 China exports of HS22090000 to Hong Kong, quantity (largest destination), 2020-2 = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p6.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p21 China exports of HS22090000 to Hong Kong, value (largest destination), 2020-2022 = **15,656,412** US dollars (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p7.] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p22 Hong Kong share of China's total HS22090000 export quantity, 2020-2022 cumulativ = **23.44** percent (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p8.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p23 China exports of HS22090000 to Singapore, quantity, 2020-2022 cumulative = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p9.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p24 China exports of HS22090000 to Australia, quantity, 2020-2022 cumulative = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p10.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p25 China exports of HS22090000 to Canada, quantity, 2020-2022 cumulative = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p13.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p26 China exports of HS22090000 to Japan, quantity, 2020-2022 cumulative = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p14.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p27 China exports of HS22090000 to Netherlands, quantity, 2020-2022 cumulative = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p11.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p28 China exports of HS22090000 to Malaysia, quantity, 2020-2022 cumulative = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Redundant duplicate of p12.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
- `https://oec.world/en/profile/bilateral-product/vinegar/reporter/usa` -> **live_dated** (page date 2024-11-01); points raw/verified 0/0
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d4 [physical_flow] Hengshun export operations / shipping

Hypothesis: Hengshun export shipments to the US move in container loads; container count × bottles per container (based on bottle size and pallet configuration) gives an upper-bound physical flow. Direction: more containers implies more bottles.

Queries issued by the searcher: Hengshun vinegar bill of lading US import shipment; Panjiva Hengshun vinegar shipment United States; 52wmb Jiangsu Hengshun International Trad supplier shipment records vinegar; 恒顺醋业 2024年年报 境外 营业收入 出口

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/7
  - p29 Piece count on a single Hengshun bill of lading (Chinkiang vinegar 550ml@24) arr = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p30 Bottle size stated in the bill of lading cargo description for Chinkiang vinegar = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p31 Bottles per case implied by the packing notation 550ML@24 in the bill of lading  = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p32 Container length in centimetres for the single Hengshun vinegar shipment (20ft c = **240** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p33 Container height in centimetres for the single Hengshun vinegar shipment = **102** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p34 Container width in centimetres for the single Hengshun vinegar shipment = **96** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
  - p35 Container type of the single Hengshun vinegar shipment (20 Foot General Purpose) = **20** foot container (2022-08-13..2022-08-13) [DISCARD: Container type label; redundant with p32-p34 dimensions.] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://pdf.marketpublishers.com/bosson_research/global-white-vinegar-market-research-report-2022status-n-outlook.pdf` -> **live_dated** (page date 2026-10-17); points raw/verified 2/1
  - p36 Global White Vinegar market size estimate, 2025 (USD) = **4,157,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global white vinegar market size is a different product/scope and cannot be converted to Hengshun US bottle count.] quote: "The global White Vinegar market size was estimated at USD 4157.0 million in 2025"
- dropped by code checks: 4 (value_as_written not in quote as a whole number: 3; period_end missing or unparseable: 1)

### d5 [capacity_consumption] Hengshun production and export capacity

Hypothesis: Hengshun total vinegar production capacity × utilisation × export share × US share of exports gives US bottles. Direction: higher capacity/utilisation/export share raises the estimate; this bounds the answer from above.

Queries issued by the searcher: 恒顺醋业 产能 产量 万吨 2024; 恒顺醋业 出口 占比 海外 收入; 恒顺醋业 出口 美国 占比 海外 销售 2024 年报; Hengshun vinegar exports United States share of sales

- `https://q.stock.sohu.com/cn/news.html?textId=100018443238&tab=100&type=100&code=cn_600305&date=2026/0415` -> **live_dated** (page date 2026-05-23); points raw/verified 0/0
- `https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_0R9N.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://m.canyin88.com/zixun/2025/12/02/110232.html` -> **live_dated** (page date 2025-12-02); points raw/verified 15/14
  - p37 Hengshun vinegar series production volume, 2024 = **210,600** tonnes (2024-01-01..2024-12-31) [DISCARD: Production volume; superseded by the more precise p141.] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨"
  - p38 Hengshun vinegar series sales volume, 2024 = **212,700** tonnes (2024-01-01..2024-12-31) [DISCARD: Sales volume; superseded by the more precise p140.] quote: "销量也超过21.27万吨"
  - p39 Hengshun total revenue, 2024 = **2,196,000,000** yuan (2024-01-01..2024-12-31) [DISCARD: Total revenue; superseded by the more precise p145.] quote: "去年,其总营收为21.96亿元"
  - p40 Hengshun vinegar series revenue, 2024 = **1,266,000,000** yuan (2024-01-01..2024-12-31) [DISCARD: Vinegar revenue; superseded by the more precise p142.] quote: "醋系列就实现12.66亿元,占据过半营收"
  - p41 Hengshun vinegar series revenue, H1 of current year = **739,000,000** yuan (2025-01-01..2025-06-30) [DISCARD: H1 2025 vinegar revenue; different period, not needed for 2024 target.] quote: "以今年上半年的业绩表现来看,醋系列仍是恒顺醋业的营收主力,贡献了7.39亿元收入。"
  - p42 Hengshun wine and sauce series combined revenue, H1 of current year = **231,000,000** yuan (2025-01-01..2025-06-30) [DISCARD: H1 2025 wine/sauce revenue; irrelevant.] quote: "而酒系列、酱系列的销售收入合计仅2.31亿元左右"
  - p43 Hengshun wine series revenue year-on-year change, H1 of current year = **5.42** % (2025-01-01..2025-06-30) [DISCARD: H1 2025 wine YoY; irrelevant.] quote: "分别同比减少了5.42%、3.53%"
  - p44 Hengshun sauce series revenue year-on-year change, H1 of current year = **3.53** % (2025-01-01..2025-06-30) [DISCARD: H1 2025 sauce YoY; irrelevant.] quote: "分别同比减少了5.42%、3.53%"
  - p45 Hengshun offline distributors covered nationwide, as of end of last year = **1,700** distributors (2024-12-31..2024-12-31) [DISCARD: Domestic distributor count; no bearing on US bottles.] quote: "截至去年底,在线下渠道,恒顺醋业已经覆盖全国超1700家经销商"
  - p46 Hengshun terminal outlets nationwide, as of end of last year = **350,000** outlets (2024-12-31..2024-12-31) [DISCARD: Domestic terminal outlets; no bearing on US bottles.] quote: "终端网点突破35万家"
  - p47 Hengshun self-media matrix cumulative followers, as of end of last year = **280,000** followers (2024-12-31..2024-12-31) [DISCARD: Social-media followers; irrelevant.] quote: "截止去年底累计粉丝超28万"
  - p48 Hengshun research and pilot base area, as of end of last year = **6,000** square metres (2024-12-31..2024-12-31) [DISCARD: R&D base area; irrelevant.] quote: "截至去年底,恒顺醋业的研究实验场所和中试基地占地 6000多平方米"
  - p49 Hengshun high-end R&D equipment count, as of end of last year = **50** sets (2024-12-31..2024-12-31) [DISCARD: R&D equipment count; irrelevant.] quote: "各类高端研发设备50余台套、省级以上科研平台6个"
  - p50 Hengshun provincial-level and above research platforms, as of end of last year = **6** platforms (2024-12-31..2024-12-31) [DISCARD: Research platforms; irrelevant.] quote: "各类高端研发设备50余台套、省级以上科研平台6个"
- `https://www.zjhengshun.com/cn_wap/list/12/284.htm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### d6 [base_rates] Bottle-size and conversion conventions

Hypothesis: Converting any volume-based estimate to bottles requires average bottle fill for US-bound Hengshun products (commonly 500ml or 16.9oz). Direction: smaller average bottle size means more bottles per tonne.

Queries issued by the searcher: Hengshun vinegar 500ml US bottle; 恒顺香醋 出口 规格 500ml; Chinkiang vinegar bottle size US 16.9 oz; Jiangsu Hengshun Vinegar-Industry 2024 annual report export revenue overseas; 恒顺醋业 2024 年报 出口 境外 收入; vinegar density 1.01 kg/L

- `https://fivecontinentsintl.com/en/product/hengshun-brand-vinegar-0-additives/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p51 Hengshun Brand Vinegar 0 Additives bottle size (product page title) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p52 Hengshun Brand Vinegar 0 Additives case pack (bottles per case) = **12** bottles per case (..) [keep: ] quote: "Case Size: 500ml*12btls"
  - p53 Hengshun Brand 9 Degrees Rice Vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p54 Hengshun Brand Cooking Wine with Shallot And Ginger bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p55 Hengshun Brand Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p56 Hengshun Brand Six Years Vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p57 Hengshun Brand Three Years Vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p58 Hengshun Brand Vinegar 0 Additives (535ml variant) bottle size = **535** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p59 Hengshun Brand Vinegar for Dumpling bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p60 Hengshun Brand Vinegar for Steamed Buns bottle size = **550** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p61 Hengshun Brand White Rice Vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p62 Hengshun Brand Zhenjiang Eight Years Vinegar bottle size = **300** ml per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://fivecontinentsintl.com/en/product/hengshun-brand-9-degrees-rice-vinegar/` -> **live_dated** (page date 2024-11-01); points raw/verified 13/13
  - p63 HengShun Brand 9 Degrees Rice Vinegar bottle size (product title) = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p53.] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p64 HengShun Brand 9 Degrees Rice Vinegar case pack (bottles per case) = **12** bottles per case (..) [DISCARD: Redundant duplicate of p52.] quote: "Case Size: 500ml*12btls"
  - p65 HengShun Brand 9 Degrees Rice Vinegar case volume per bottle in case size listin = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p53.] quote: "Case Size: 500ml*12btls"
  - p66 HengShun Brand Cooking Wine with Shallot And Ginger bottle size = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p54.] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p67 HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p55.] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p68 HengShun Brand Six Years Vinegar bottle size = **580** ml per bottle (..) [DISCARD: Redundant duplicate of p56.] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p69 HengShun Brand Three Years Vinegar bottle size = **580** ml per bottle (..) [DISCARD: Redundant duplicate of p57.] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p70 HengShun Brand Vinegar 0 Additives bottle size (500ml variant) = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p51.] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p71 HengShun Brand Vinegar 0 Additives bottle size (535ml variant) = **535** ml per bottle (..) [DISCARD: Redundant duplicate of p58.] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p72 HengShun Brand Vinegar for Dumpling bottle size = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p59.] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p73 HengShun Brand Vinegar for Steamed Buns bottle size = **550** ml per bottle (..) [DISCARD: Redundant duplicate of p60.] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p74 HengShun Brand White Rice Vinegar bottle size = **500** ml per bottle (..) [DISCARD: Redundant duplicate of p61.] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p75 HengShun Brand Zhenjiang Eight Years Vinegar bottle size = **300** ml per bottle (..) [DISCARD: Redundant duplicate of p62.] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://hypertextbook.com/facts/2000/IngaKarlson.shtml` -> **dropped** (live http 404); points raw/verified -/-

### d7 [persona] US distributor / importer

Hypothesis: US importers/distributors of Hengshun (e.g., Asian grocery wholesalers) may disclose case volumes or sales; case count × bottles per case gives US bottles. Direction: distributor disclosures directly constrain the answer.

Queries issued by the searcher: Hengshun vinegar US distributor importer Chinkiang; 恒顺醋业 美国 出口 经销商; importyeti Jiangsu Hengshun shipments vinegar; 恒顺醋业 2024年年度报告 海外 出口 收入 境外

- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p76 Total US customs shipments recorded for Jiangsu Hengshun Group (supplier), cumul = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p77 Number of US trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Trading-partner count; contextual only, not a volume input.] quote: "Trading Partners 6"
  - p78 Number of US ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Port count; contextual only, not a volume input.] quote: "Ports 5"
  - p79 Bill of lading piece count for Chinkiang vinegar 550ML@24 shipment (arrival 2022 = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p29.] quote: "Piece Count 700"
  - p80 Bottle size in ml for Chinkiang vinegar SKU on bill of lading = **550** ml per bottle (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p30.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p81 Bottles per case (pack count) for Chinkiang vinegar 550ML SKU = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p31.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p82 Container length in cm for the vinegar shipment container = **240** cm (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p32.] quote: "Length 240"
  - p83 Container height in cm for the vinegar shipment container = **102** cm (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p33.] quote: "Height 102"
  - p84 Container width in cm for the vinegar shipment container = **96** cm (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p34.] quote: "Width 96"
- `https://m.x315.cn/doc/a66NUr` -> **live_dated** (page date 2023-09-26); points raw/verified 14/13
  - p85 China imports of Hengshun brand white rice vinegar (HS22090000) from the United  = **3,817,694** liters (2020-01-01..2022-12-31) [DISCARD: Directionally implausible: 'China imports of Hengshun brand white rice vinegar from the United States' — China does not ] quote: "第二美国:总数量为3,817,694升;金额13,523,057美元;总占比18.47%。"
  - p86 China imports of Hengshun brand white rice vinegar (HS22090000) from the United  = **13,523,057** USD (2020-01-01..2022-12-31) [DISCARD: Same mislabeled import-direction dataset as p85; not US-bound export evidence.] quote: "进口美国金额最高,总计13,523,057美元"
  - p87 US share of China's Hengshun brand white rice vinegar (HS22090000) imports by qu = **18.47** % (2020-01-01..2022-12-31) [DISCARD: Share derived from the mislabeled import dataset; not applicable.] quote: "第二美国:总数量为3,817,694升;金额13,523,057美元;总占比18.47%。"
  - p88 China total imports of Hengshun brand white rice vinegar (HS22090000) from all c = **20,664,582** liters (2020-01-01..2022-12-31) [DISCARD: Total of the mislabeled import dataset; not applicable.] quote: "恒顺牌白米醋(HS22090000)共从海外38个国家进口,总计20,664,582升,3,430万美元。"
  - p89 Number of countries China imported Hengshun brand white rice vinegar (HS22090000 = **38** countries (2020-01-01..2022-12-31) [DISCARD: Country count from mislabeled import dataset; not applicable.] quote: "恒顺牌白米醋(HS22090000)共从海外38个国家进口"
  - p90 China imports of Hengshun brand white rice vinegar (HS22090000) from Japan, quan = **5,311,063** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第一日本:总数量为5,311,063升;金额5,396,893美元;总占比25.70%。"
  - p91 Japan share of China's Hengshun brand white rice vinegar (HS22090000) imports by = **25.7** % (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第一日本:总数量为5,311,063升;金额5,396,893美元;总占比25.70%。"
  - p92 China imports of Hengshun brand white rice vinegar (HS22090000) from South Korea = **3,721,730** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第三韩国:总数量为3,721,730升;金额2,898,559美元;总占比18.01%。"
  - p93 China imports of Hengshun brand white rice vinegar (HS22090000) from Malaysia, q = **3,300,015** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第四马来西亚:总数量为3,300,015升;金额1,455,937美元;总占比15.97%。"
  - p94 China imports of Hengshun brand white rice vinegar (HS22090000) from Italy, quan = **2,212,699** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第五意大利:总数量为2,212,699升;金额6,492,715美元;总占比10.71%。"
  - p95 China imports of Hengshun brand white rice vinegar (HS22090000) from Germany, qu = **763,124** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第六德国:总数量为763,124升;金额1,628,043美元;总占比3.69%。"
  - p96 China imports of Hengshun brand white rice vinegar (HS22090000) from Taiwan, qua = **640,562** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第七中国台湾:总数量为640,562升;金额652,997美元;总占比3.10%。"
  - p97 China imports of Hengshun brand white rice vinegar (HS22090000) from Spain, quan = **477,363** liters (2020-01-01..2022-12-31) [DISCARD: Mislabeled import dataset; not applicable.] quote: "第八西班牙:总数量为477,363升;金额944,600美元;总占比2.31%。"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d8 [shocks] Trade policy and market context

Hypothesis: US-China tariff changes and shipping disruptions affect Hengshun's US export volumes; identifying whether 2024 saw tariff-driven shifts helps choose the right year and adjust a historical ratio. Direction: higher tariffs reduce US-bound volume.

Queries issued by the searcher: US tariff Chinese vinegar HS 2209 Section 301 rate; 恒顺醋业 2024 年报 出口 美国 销量; USTR List 3 2209 vinegar 25 percent Section 301 2024 Federal Register; 恒顺醋业 2024年 境外收入 出口 占比 年报

- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 8/0
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.sgpjbg.com/baogao/631780.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://cfi.cn/p20250422000502.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b1 [own_history] company disclosure

Hypothesis: Hengshun annual report (600305) discloses overseas/export revenue or export volume; combined with a US share of overseas sales this unlocks a direct value-to-bottle route (d1). Currently no kept point gives Hengshun's export revenue or export share, which is the single biggest missing input.

Queries issued by the searcher: 600305 恒顺醋业 2024 年报 境外收入 出口; 恒顺醋业 2024 年度报告 海外 出口 占比; 恒顺醋业 海外业务 占营业收入 4.36% 海外 收入 亿元 2024; 恒顺 香醋 出口 美国 占比 出口量 吨

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1974663940947992576` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://rdfile.dzh.com.cn/new/dzh/dbcData/594/DA27C670A75BFAB6DDF3A4FD773CA233_2510196.pdf` -> **live_dated** (page date 2023-05-06); points raw/verified 15/10
  - p98 Hengshun Vinegar 23Q1 foreign trade (外贸) channel operating revenue = **8,000,000** CNY yuan (100 million) (2023-01-01..2023-03-31) [keep: ] quote: "公司 Q1 经销/直 销 / 外贸 渠道 分 别 实 现 营业 收入 5.71 亿 /0.22 亿 /0.08 亿 , 同 比 +7.02%/+26.58%/+2.22%。"
  - p99 Hengshun Vinegar 23Q1 foreign trade (外贸) channel revenue YoY growth = **2.22** % (2023-01-01..2023-03-31) [DISCARD: YoY growth of foreign-trade channel; only the level p98 is used as a consistency check.] quote: "公司 Q1 经销/直 销 / 外贸 渠道 分 别 实 现 营业 收入 5.71 亿 /0.22 亿 /0.08 亿 , 同 比 +7.02%/+26.58%/+2.22%。"
  - p100 Hengshun Vinegar 23Q1 vinegar series revenue = **382,000,000** CNY yuan (100 million) (2023-01-01..2023-03-31) [DISCARD: 23Q1 vinegar revenue; not needed.] quote: "分单品看,23Q1 醋/酒/酱系列分别 实现收入 3.82 亿/1.11 亿/0.65 亿,同比+8.04%/+4.35%/-2.43%"
  - p101 Hengshun Vinegar 23Q1 total operating revenue = **613,000,000** CNY yuan (100 million) (2023-01-01..2023-03-31) [DISCARD: 23Q1 total revenue; not needed.] quote: "23Q1 实现营业收入 6.13 亿元,同比+7.15%"
  - p102 Hengshun Vinegar 2023 non-recurring net profit growth target (stated plan) = **20** % (2023-01-01..2023-12-31) [DISCARD: 2023 profit target; irrelevant to volume.] quote: "23 年公司目标收入双位数 以上增长,扣非净利润增长 20%以上"
  - p103 Hengshun Vinegar 2023 large-single-product channel coverage target (stated plan) = **60** % (2023-01-01..2023-12-31) [DISCARD: Channel-coverage target; irrelevant to US volume.] quote: "大单品渠道覆盖率 60%以上"
  - p104 Hengshun Vinegar 2022 gross margin (FY) = **34.4** % (2022-01-01..2022-12-31) [DISCARD: Gross margin; not needed for a volume route.] quote: "毛利率 37.0% 42.6% 33.4% 37.9% 33.2% 33.9% 32.0% 35.1% 37.6% 34.4%"
  - p105 Hengshun Vinegar 23Q1 gross margin = **35.08** % (2023-01-01..2023-03-31) [DISCARD: Gross margin; not needed for a volume route.] quote: "23Q1 公司实现毛利率 35.08%, 同比-2.82pcts"
  - p106 Hengshun Vinegar 2024E EPS (forecast) = **0.3** CNY yuan per share (2024-01-01..2024-12-31) [DISCARD: EPS forecast; irrelevant to volume.] quote: "我们预计 23-24 年 EPS 分别为 0.22、0.30 元"
  - p107 Hengshun Vinegar 23Q1 dealer count net increase vs end-2022 = **44** dealers (net increase) (2023-01-01..2023-03-31) [DISCARD: Dealer net increase; domestic, irrelevant.] quote: "截止 23Q1 末,公 司经销商数量环比 22 年末净增 44 个"
- dropped by code checks: 5 (scale word 'million' not supported by quote or table header: 4; number: no number in value_as_written: 1)

### b2 [related_series] customs/trade data

Hypothesis: A 2024-specific China customs HS22090000 export-to-US volume (rather than the 2020-2022 cumulative) plus Hengshun's share of branded Chinese vinegar exports would let the d2 route be applied to the target year directly, removing the need to extrapolate a 3-year average.

Queries issued by the searcher: HS22090000 出口 美国 2024 数量 食醋; China vinegar exports to US 2024 HS 2209 quantity; 恒顺醋业 2024年 出口 海外 收入 占比 年报; 中国 食醋 出口 量 2024 恒顺 占 品牌 出口 比例

- `https://chinadata.live/china-trade/hs/220900/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.jcksj.com/report/22090000.html` -> **live_dated** (page date 2026-09-08); points raw/verified 15/15
  - p108 China HS 22090000 exports to the United States, 2024 annual value = **4,992,092** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p109 China HS 22090000 exports to the United States, 2025 annual value = **3,787,074** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p110 China HS 22090000 total exports, 2024 annual value = **29,676,894** USD (2024-01-01..2024-12-31) [keep: ] quote: "2024 29,676,894 美元29676894"
  - p111 China HS 22090000 total exports, 2025 annual value = **27,891,245** USD (2025-01-01..2025-12-31) [keep: ] quote: "2025 27,891,245 美元27891245"
  - p112 China HS 22090000 total exports, 2025 annual value in ten-thousand USD = **27,891,200** USD (ten-thousand) (2025-01-01..2025-12-31) [DISCARD: Redundant restatement of p111 in ten-thousand USD; same value, adds no information.] quote: "2789.12万美元"
  - p113 China HS 22090000 total exports, year-on-year change 2025 vs 2024 = **-6.02** % (2025-01-01..2025-12-31) [keep: ] quote: "较2024年-6.02%"
  - p114 China HS 22090000 total imports, 2024 annual value = **9,806,210** USD (2024-01-01..2024-12-31) [DISCARD: China HS22090000 imports (inbound to China) — wrong direction, irrelevant to US-bound exports.] quote: "2024 9,806,210 美元9806210"
  - p115 China HS 22090000 total imports, 2025 annual value = **11,979,467** USD (2025-01-01..2025-12-31) [DISCARD: China HS22090000 imports 2025 — wrong direction.] quote: "2025 11,979,467 美元11979467"
  - p116 China HS 22090000 imports from the United States, 2024 annual value = **2,269,319** USD (2024-01-01..2024-12-31) [DISCARD: China imports from the US — wrong direction.] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p117 China HS 22090000 imports from the United States, 2025 annual value = **1,875,118** USD (2025-01-01..2025-12-31) [DISCARD: China imports from the US 2025 — wrong direction.] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p118 China HS 22090000 exports to Hong Kong, 2024 annual value = **4,093,608** USD (2024-01-01..2024-12-31) [DISCARD: Hong Kong destination value; not the US target, and only used as context.] quote: "\| 中国香港 \| 4,205,407 \| 4,093,608 \| +111,799 \| +2.73% \| 查询该市场买家 ↗ \|"
  - p119 China HS 22090000 exports to Singapore, 2024 annual value = **1,493,383** USD (2024-01-01..2024-12-31) [DISCARD: Singapore destination; not the US target.] quote: "\| 新加坡 \| 1,654,888 \| 1,493,383 \| +161,505 \| +10.81% \| 查询该市场买家 ↗ \|"
  - p120 China HS 22090000 exports to Australia, 2024 annual value = **1,959,491** USD (2024-01-01..2024-12-31) [DISCARD: Australia destination; not the US target.] quote: "\| 澳大利亚 \| 2,079,038 \| 1,959,491 \| +119,547 \| +6.10% \| 查询该市场买家 ↗ \|"
  - p121 China HS 22090000 exports to Canada, 2024 annual value = **1,015,187** USD (2024-01-01..2024-12-31) [DISCARD: Canada destination; not the US target.] quote: "\| 加拿大 \| 980,594 \| 1,015,187 \| -34,593 \| -3.41% \| 查询该市场买家 ↗ \|"
  - p122 China HS 22090000 exports to Japan, 2024 annual value = **1,300,409** USD (2024-01-01..2024-12-31) [DISCARD: Japan destination; not the US target.] quote: "\| 日本 \| 1,275,219 \| 1,300,409 \| -25,190 \| -1.94% \| 查询该市场买家 ↗ \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p123 China HS22090000 vinegar exports to the United States, cumulative volume, 2020-0 = **6,597,078** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p1 (same m.x315.cn 2020-2022 US volume).] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p124 China HS22090000 vinegar exports to the United States, cumulative value, 2020-01 = **8,459,027** US dollars (2020-01-01..2022-12-31) [DISCARD: Duplicate of p2.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p125 United States share of China HS22090000 vinegar export volume, 2020-01 to 2022-1 = **11.35** percent (2020-01-01..2022-12-31) [DISCARD: Duplicate of p3.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p126 China HS22090000 vinegar exports worldwide, cumulative volume, 2020-01 to 2022-1 = **58,119,878** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p4.] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p127 Number of destination countries for China HS22090000 vinegar exports, 2020-01 to = **129** countries (2020-01-01..2022-12-31) [DISCARD: Destination-country count; no bearing on US bottle volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p128 China HS22090000 vinegar exports to Hong Kong, cumulative volume, 2020-01 to 202 = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Hong Kong volume; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p129 China HS22090000 vinegar exports to Hong Kong, cumulative value, 2020-01 to 2022 = **15,656,412** US dollars (2020-01-01..2022-12-31) [DISCARD: Hong Kong value; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p130 Hong Kong share of China HS22090000 vinegar export volume, 2020-01 to 2022-12 = **23.44** percent (2020-01-01..2022-12-31) [DISCARD: Hong Kong share; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p131 China HS22090000 vinegar exports to Singapore, cumulative volume, 2020-01 to 202 = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Singapore volume; not the US target.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p132 China HS22090000 vinegar exports to Australia, cumulative volume, 2020-01 to 202 = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Australia volume; not the US target.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p133 China HS22090000 vinegar exports to Netherlands, cumulative volume, 2020-01 to 2 = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Netherlands volume; not the US target.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p134 China HS22090000 vinegar exports to Malaysia, cumulative volume, 2020-01 to 2022 = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Malaysia volume; not the US target.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p135 China HS22090000 vinegar exports to Canada, cumulative volume, 2020-01 to 2022-1 = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Canada volume; not the US target.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p136 China HS22090000 vinegar exports to Japan, cumulative volume, 2020-01 to 2022-12 = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Japan volume; not the US target.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `http://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918927` -> **live_dated** (page date 2024-07-26); points raw/verified 14/12
  - p137 Hengshun (Jiangsu Hengshun Vinegar-Industry) 2024 export-mode (外贸模式) revenue, al = **47,741,038** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点 \|"
  - p138 Hengshun 2024 export-mode (外贸模式) revenue year-on-year change = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点 \|"
  - p139 Hengshun 2024 export-mode (外贸模式) gross margin = **27.3** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点 \|"
  - p140 Hengshun 2024 vinegar series (醋系列) sales volume = **212,747** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22 \|"
  - p141 Hengshun 2024 vinegar series (醋系列) production volume = **210,641** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22 \|"
  - p142 Hengshun 2024 vinegar series (醋系列) revenue = **1,265,596,326** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点 \|"
  - p143 Hengshun 2024 vinegar series (醋系列) gross margin = **45.31** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点 \|"
  - p144 Hengshun 2024 total condiment (调味品) revenue = **2,093,006,845** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "\| 调味品 \| 2,093,006,844.54 \| 1,358,355,887.39 \| 35.10 \| 0.73 \| -3.34 \| 增加2.73个百分点 \|"
  - p145 Hengshun 2024 total revenue (consolidated) = **2,195,870,508** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "\| 营业收入 \| 2,195,870,508.45 \| 2,106,410,685.37 \| 4.25 \| 2,139,020,033.23 \|"
  - p146 Hengshun 2024 year-end USD-denominated accounts receivable (foreign currency mon = **463,828** 美元 (2024-12-31..2024-12-31) [DISCARD: USD accounts receivable balance; not a flow of US-bound vinegar.] quote: "\| 其中:美元 \| 463,828.49 \| 7.1884 \| 3,334,184.72 \|"
  - p147 Hengshun 2024 year-end USD/RMB conversion rate used for foreign currency monetar = **7.188** 人民币元/美元 (2024-12-31..2024-12-31) [DISCARD: FX rate; only needed to convert p146, which is discarded.] quote: "\| 其中:美元 \| 463,828.49 \| 7.1884 \| 3,334,184.72 \|"
  - p148 Hengshun 2024 online sales channel revenue = **274,378,141** 人民币元 (2024-01-01..2024-12-31) [DISCARD: Online channel revenue; domestic e-commerce, not US export.] quote: "\| 线上销售 \| 274,378,140.67 \| 13.11 \| 53.17 \| 264,716,814.16 \| 12.74 \| 50.22 \|"
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 1; number: value_as_written is only part of a larger CJK number in the quote: 1; period_end missing or unparseable: 1)

### b3 [persona] US distributor/importer

Hypothesis: US importers/distributors of Hengshun (e.g., Five Continents, Asian grocery wholesalers) may disclose annual case volumes or container counts; this would directly constrain the d4/d7 physical-flow route and resolve the largest uncertainty (Hengshun's US shipment frequency).

Queries issued by the searcher: Hengshun vinegar US importer annual volume cases; ImportGenius Jiangsu Hengshun shipments 2024 vinegar; 52wmb Jiangsu Hengshun International Trade 出口美国 提单 数量; importyeti Jiangsu Hengshun vinegar shipments buyer

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 8/5
  - p149 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24, a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p29 (same bill of lading piece count).] quote: "Piece Count 700"
  - p150 Bottle size and pack configuration stated in cargo description: 550ML per bottle = **550** millilitres per bottle (packed 24 per case) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p30/p31 packing notation.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p151 Container length dimension on bill of lading (20-foot general purpose container) = **240** container length (cm, as listed) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p32 container length.] quote: "Length 240"
  - p152 Container height dimension on bill of lading = **102** container height (cm, as listed) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p33 container height.] quote: "Height 102"
  - p153 Container width dimension on bill of lading = **96** container width (cm, as listed) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p34 container width.] quote: "Width 96"
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'chinese vinegar us imports', 'zhenjiang vinegar sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p15', 'p16', 'p17'] Same underlying China customs HS22090000 export-to-US measurement (2020-2022 cumulative), duplicated across d2 and d3. One measurement, not independent confirmation. Establishes US is ~11.35% of China
- corroborating: ['p4', 'p18', 'p5', 'p19'] Same total China HS22090000 export volume (~58.1M L) and 129 destination countries; duplicate framing of the same customs aggregate.
- corroborating: ['p6', 'p7', 'p8', 'p20', 'p21', 'p22'] Hong Kong is the largest destination (~23.4% of volume); same customs dataset, duplicated across d2/d3.
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28'] Other destination volumes from the same customs aggregate; useful for context on the export mix but not directly about Hengshun or the US.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84'] Single Hengshun bill of lading (2022-08-13): 550ml@24, 700 pieces, 20ft container. Duplicated across d4 and d7. Gives a real bottle size (550ml) and case pack (24) for US-bound Hengshun product, and a
- corroborating: ['p76', 'p77', 'p78'] ImportGenius supplier profile: 44 cumulative US shipments 2006-2022, 6 partners, 5 ports. Same source as the bill of lading; indicates low but nonzero US shipment frequency.
- corroborating: ['p37', 'p38', 'p39', 'p40'] Hengshun 2024 company scale: ~210.6kt vinegar production, ~212.7kt sales, ¥2.196bn total revenue, ¥1.266bn vinegar revenue. Same article; establishes the denominator for any export-share route.
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50'] H1-2025 and structural company facts; contextual, not directly about US exports.
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75'] US distributor (Five Continents) product catalog: Hengshun bottle sizes cluster at 500ml (some 535/550/580/300ml), case packs 12 or 24. Duplicated across d6. Provides the bottle-fill conversion factor
- conflicting: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97'] These are labeled 'China imports of Hengshun brand white rice vinegar FROM the United States' — directionally implausible (China does not import Hengshun vinegar from the US). Likely a mislabeled/mirr
- conflicting: ['p36'] Global white vinegar market size (USD 4.16bn) is a different product/scope and cannot be tied to Hengshun US bottles.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p123', 'p124', 'p125', 'p126'] Same underlying m.x315.cn HS22090000 2020-2022 cumulative dataset; p123-p126 are duplicate copies of p1-p4. They establish the US is ~11.35% of China's vinegar export volume and give an implied ~1.28 
- corroborating: ['p108', 'p109', 'p110', 'p111', 'p112', 'p113'] Same jcksj.com customs mirror; 2024 US-bound HS22090000 value ~4.99M USD, total exports ~29.68M USD, 2025 down 24% to US and 6% overall. Value-only, no volume, so needs a price-per-litre bridge.
- corroborating: ['p137', 'p138', 'p139', 'p142', 'p143', 'p144', 'p145'] Hengshun 2024 annual report figures: export-mode revenue 47.74M CNY (all products, all destinations), vinegar series revenue 1.266bn CNY, total revenue 2.196bn CNY. Export mode is ~2.2% of total reven
- corroborating: ['p37', 'p38', 'p140', 'p141'] Hengshun 2024 vinegar production ~210.6kt and sales ~212.7kt, consistent across the trade-press and annual-report sources. Gives the denominator for an export-share route.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p149', 'p150', 'p151', 'p152', 'p153'] Duplicate copies of one 2022 bill of lading: 700 pieces, 550ml@24, 20ft container. Establishes a real Hengshun US shipment exists and typical SKU/pack format, but a single shipment is not an annual vo
- corroborating: ['p76', 'p77', 'p78'] ImportGenius shows only 44 total US customs shipments for Jiangsu Hengshun Group over 2006-2022 across 6 partners and 5 ports. This is a lower bound on shipment records (bill-of-lading coverage is inc
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62'] Five Continents (US distributor) product list shows Hengshun US SKUs mostly 500ml, some 535/550/580/300ml, case pack 12. Supports an average fill near 500-550ml for US-bound bottles.
- corroborating: ['p98', 'p99', 'p100', 'p101'] 23Q1 foreign-trade channel revenue 0.08亿 CNY (~8M CNY/quarter) vs total 6.13亿; consistent order of magnitude with the 2024 annual export-mode figure of 47.7M CNY. Older period, used only as a consiste
- corroborating: ['p104', 'p105', 'p106', 'p107', 'p102', 'p103'] Margin, EPS forecast, dealer-count and target figures; contextual only, not directly usable for US bottle volume.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | US share of Hengshun export-mode revenue | 0.2 | 0.08..0.4 | 0.08..0.4 | fraction | unused | Hengshun export-mode revenue (p137) covers all destinations and products. The US is ~11-17% of China's vinegar export volume/value (p3, p108/p110), the largest non-Hong-Kong market. ImportGenius shows only 44 US shipments over 2006-2022 (p76), suggesting the US is important but not dominant; set 20% | Hengshun's export destination mix resembles the national HS22090000 mix with the US as a leading branded market. | Distributor disclosures showing only a few containers/year, or evidence most exports go to Hong Kong/SE Asia. |
| a2 | Vinegar share of Hengshun export-mode revenue | 0.6 | 0.4..0.8 | 0.4..0.8 | fraction | unused | Vinegar is ~58% of Hengshun total revenue (p142/p145) and is the flagship export product; export mix likely skews toward vinegar but includes sauce and wine. Set 60% central. | Export product mix broadly resembles domestic mix, tilted toward vinegar. | Evidence Hengshun exports mostly sauce or cooking wine. |
| a3 | Average Hengshun export price per litre (CNY) | 8 | 5..13 | 5..13 | CNY per litre | unused | China HS22090000 export unit value from p2/p1 is ~1.28 USD/litre (~9.2 CNY/litre at ~7.2 CNY/USD); Hengshun branded product sells at a premium but export FOB prices are below US retail. Set 8 CNY/litre central. | Hengshun export FOB price per litre is near the national HS22090000 average, adjusted for brand premium. | Evidence of Hengshun export invoice prices materially different from the national average. |
| a4 | Average bottle fill for US-bound Hengshun vinegar | 0.52 | 0.45..0.6 | 0.3674..0.7348 (widened) | litres per bottle | m2 (m2) | US distributor SKU list (p51-p62) is dominated by 500ml with some 535/550/580ml; weighted average ~0.52L. Bill of lading (p30) shows 550ml. | US-bound SKU mix resembles the Five Continents catalogue. | Evidence that US-bound Hengshun is mostly large-format or bulk packaging. |
| a5 | Hengshun share of China HS22090000 exports to the US by value | 0.3 | 0.12..0.55 | 0.12..0.55 | fraction | m2 (m2) | Hengshun is China's largest vinegar producer and best-known branded exporter; branded product commands a value premium over many small bulk exporters. Set 30% central with wide range. | Hengshun is the leading branded supplier among Chinese vinegar exporters to the US. | Evidence that Hengshun's US-bound value is a small share of the ~5M USD total. |
| a6 | Average Hengshun US-bound export price per litre (USD) | 1.6 | 1..2.6 | 1..2.6 | USD per litre | m2 (m2) | National HS22090000 US-bound unit value from p2/p1 is ~1.28 USD/litre; Hengshun branded product should price above the national average. Set 1.6 USD/litre central. | Hengshun US FOB price is modestly above the national HS22090000 average. | Evidence of Hengshun US invoice prices near or below the national average. |
| a7 | Hengshun export share of vinegar sales volume | 0.03 | 0.015..0.06 | 0.015..0.06 | fraction | unused | Export-mode revenue is ~2.2% of total revenue (p137/p145); vinegar export share of vinegar volume should be similar order, slightly higher if export mix skews to vinegar. Set 3% central. | Export revenue share approximates export volume share for vinegar. | Evidence that export prices are much higher or lower than domestic, shifting the volume share. |
| a8 | US share of Hengshun vinegar export volume | 0.2 | 0.08..0.4 | 0.08..0.4 | fraction | unused | Same logic as a1: the US is a leading branded market for Chinese vinegar; set 20% central. | Hengshun's vinegar export destination mix resembles the national mix. | Evidence that Hengshun's US volume is a small fraction of its exports. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p137'] / ['a1', 'a2', 'a3', 'a4'] | [] |  | 0.00 |  | formula_mc uses 4 assumptions (at most 3) |
| m2 | formula_mc | 1,519,475 | ['p108'] / ['a4', 'a5', 'a6'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **1,519,475** bottle, 80% interval [569,006, 4,057,607] bottle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']; 9 point(s) for the target period excluded as dated before the period end or quoted as a forecast
Early checks while the sub-agents were running: 1 (not_confirmed); details in state.json -> published_early.


## Final answer

Best computed estimate: 1,519,475 bottle of Hengshun bottled vinegar exported to the United States in calendar year 2024 (all bottled SKUs, excluding bulk/industrial drums), with an 80% model-based interval of 569,006 to 4,057,607 bottle (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

The retained method (weight 100%) is a destination-side route: observed China HS [n] exports to the US in 2024 (4,992,092 USD) multiplied by an assumed Hengshun value share (0.3, range 0.12 to 0.55), divided by an assumed Hengshun US-bound price per litre (1.6, range 1 to 2.6) and an assumed bottle fill (0.52, range 0.3674 to 0.7348). The company-side route using observed export revenue (47,741,038 人民币元) was not usable because it required more assumptions than allowed.

Only the customs total is observed; the share, price and fill are analyst assumptions, so the result is conditional. The biggest risk is that Hengshun's true share of US-bound value is far from 0.3. Better evidence would be Hengshun's own US shipment or customs records.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a4 Average bottle fill for US-bound Hengshun vinegar: 0.52 litres per bottle, range 0.3674 to 0.7348 (range widened by code); used by m2. Overturned by: Evidence that US-bound Hengshun is mostly large-format or bulk packaging.
- a5 Hengshun share of China HS[n] exports to the US by value: 0.3 fraction, range 0.12 to 0.55; used by m2. Overturned by: Evidence that Hengshun's US-bound value is a small share of the ~[n]M USD total.
- a6 Average Hengshun US-bound export price per litre (USD): 1.6 USD per litre, range 1 to 2.6; used by m2. Overturned by: Evidence of Hengshun US invoice prices near or below the national average.

# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types combined, excluding bulk/industrial drums) sold by Jiangsu Hengshun Vinegar-Industry Co. (镇江恒顺集团/恒顺醋业) into the United States market, counted as bottles shipped/sold to US customers | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; best proxies are Jiangsu Hengshun Vinegar-Industry Co. annual report (SSE: 600305) export/overseas revenue disclosures and Chinese customs HS 2209 export statistics

## Directions and pages

### d1 [related_series] Company financial disclosure analyst

Hypothesis: Hengshun's annual report discloses overseas/export revenue (and possibly export volume); US share of that overseas revenue times total export volume, divided by average bottle size, gives US bottle count. Role: provides the top-level export total to be split.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外 营业收入 出口; 恒顺醋业 出口 销量 吨 海外 2024; 恒顺醋业 2024年报 分地区 境内 境外 营业收入 主营业务分地区情况; 恒顺醋业 食醋 产量 销量 吨 2024年 年报 产销量

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.zhenjiang.gov.cn/zhenjiang/zwyw/202407/9f238a06efa24fceb13d613b698c8bff.shtml` -> **dropped** (live http 301); points raw/verified -/-
- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-

### d2 [physical_flow] Customs trade statistician

Hypothesis: China customs HS 2209 (vinegar and substitutes) exports to the US give total Chinese vinegar volume entering the US; Hengshun's share of China's vinegar exports (from company or industry data) times that volume, divided by bottle size, approximates Hengshun US bottles. Role: independent physical-flow cross-check on d1.

Queries issued by the searcher: 中国 海关 HS 2209 醋 出口 美国 数量 吨; UN Comtrade 2209 vinegar US imports from China quantity; 恒顺醋业 2024年年报 境外 营业收入 出口; 镇江香醋 出口 占全国 醋 出口 比例 恒顺 出口量

- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p1 China HS 22090000 vinegar exports to the United States, quantity (2020-2022 cumu = **6,597,078** litres (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p2 China HS 22090000 vinegar exports to the United States, value (2020-2022 cumulat = **8,459,027** US dollars (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p3 US share of China HS 22090000 vinegar export quantity (2020-2022 cumulative) = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p4 Total China HS 22090000 vinegar exports, quantity, all destinations (2020-2022 c = **58,119,878** litres (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p5 Number of destination countries for China HS 22090000 vinegar exports (2020-2022 = **129** countries (2020-01-01..2022-12-31) [DISCARD: Count of destination countries; no bearing on US bottle volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p6 China HS 22090000 vinegar exports to Hong Kong, quantity (2020-2022 cumulative) = **13,624,552** litres (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p7 China HS 22090000 vinegar exports to Hong Kong, value (2020-2022 cumulative) = **15,656,412** US dollars (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p8 Hong Kong share of China HS 22090000 vinegar export quantity (2020-2022 cumulati = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p9 China HS 22090000 vinegar exports to Singapore, quantity (2020-2022 cumulative) = **4,057,620** litres (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p10 China HS 22090000 vinegar exports to Australia, quantity (2020-2022 cumulative) = **3,691,524** litres (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p11 China HS 22090000 vinegar exports to Netherlands, quantity (2020-2022 cumulative = **3,519,273** litres (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p12 China HS 22090000 vinegar exports to Malaysia, quantity (2020-2022 cumulative) = **3,160,711** litres (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p13 China HS 22090000 vinegar exports to Canada, quantity (2020-2022 cumulative) = **2,537,372** litres (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p14 China HS 22090000 vinegar exports to Japan, quantity (2020-2022 cumulative) = **2,404,533** litres (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] US import/retail channel analyst

Hypothesis: US import records (bill of lading / import database) for Hengshun-branded vinegar shipments give container/weight volumes directly attributable to Hengshun; weight divided by bottle size yields bottle count. Role: direct US-side measurement independent of Chinese reporting.

Queries issued by the searcher: Hengshun vinegar US import bill of lading; Jiangsu Hengshun Vinegar Panjiva import shipment; importyeti Hengshun vinegar shipments Well Luck 2024; volza "Jiangsu Hengshun" vinegar US imports shipments 2024

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-group-zhenjiang-in` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p15 Total US customs shipments recorded for Jiangsu Hengshun Group (supplier), cumul = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p16 Number of trading partners recorded for Jiangsu Hengshun Group in US customs dat = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Trading-partner count for Hengshun in US customs data; a count of partners, not volume, and redundant with p15/p17 conte] quote: "Trading Partners 6"
  - p17 Number of ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Port count; no volume information.] quote: "Ports 5"
  - p18 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p19 Bottle size stated in cargo description on bill of lading EGLV142252207486 (Chin = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p20 Bottles per case stated in cargo description on bill of lading EGLV142252207486  = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p21 Container length on bill of lading EGLV142252207486 = **240** container length (cm) (2022-08-13..2022-08-13) [DISCARD: Container dimension on a single bill of lading; not a volume and not needed once p18-p20 give the case/bottle spec.] quote: "Length 240"
  - p22 Container height on bill of lading EGLV142252207486 = **102** container height (cm) (2022-08-13..2022-08-13) [DISCARD: Container dimension; redundant with p21.] quote: "Height 102"
  - p23 Container width on bill of lading EGLV142252207486 = **96** container width (cm) (2022-08-13..2022-08-13) [DISCARD: Container dimension; redundant with p21.] quote: "Width 96"

### d4 [base_rates] Packaging/conversion analyst

Hypothesis: Bottle count = volume / average bottle size; Hengshun's US retail SKUs are predominantly 500 ml (also 16.9 oz) glass bottles, with some larger food-service sizes. Role: supplies the conversion factor and its mix for d1-d3.

Queries issued by the searcher: Hengshun Chinkiang vinegar 500ml US retail bottle sizes; 恒顺 香醋 出口 规格 500ml 瓶 美国; 恒顺醋业 2024年 年报 境外 营业收入 出口; Five Continents International Hengshun vinegar case size 500ml 12 bottles

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p24 Hengshun Zhenjiang/Chinkiang Vinegar 3L bottle size (case of 4 bottles) = **3** litres per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang / Chinkiang Vinegar(3L)"
  - p25 Hengshun Zhenjiang/Chinkiang Vinegar 3L case pack count (bottles per case) = **4** bottles per case (..) [keep: ] quote: "Case Size: 3L*4btls"
  - p26 Hengshun 9 Degrees Rice Vinegar bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p27 Hengshun Cooking Wine with Shallot And Ginger bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p28 Hengshun Cooking Wine With Shallot And Ginger 0 Additives bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p29 Hengshun Six Years Vinegar bottle size = **580** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p30 Hengshun Vinegar 0 Additives bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p31 Hengshun Vinegar 0 Additives (535ml variant) bottle size = **535** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p32 Hengshun Vinegar for Dumpling bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p33 Hengshun Vinegar for Steamed Buns bottle size = **550** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p34 Hengshun White Rice Vinegar bottle size = **500** millilitres per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p35 Hengshun Zhenjiang Eight Years Vinegar bottle size = **300** millilitres per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0

### d5 [own_history] Company history analyst

Hypothesis: Hengshun's prior-year export/overseas revenue and any disclosed export growth rates anchor the 2024 level and reveal trend; role: constrains d1 and validates magnitude.

Queries issued by the searcher: 恒顺醋业 历年 境外收入 出口; 恒顺醋业 年报 海外 销售 增长; 恒顺醋业 2024年年度 主要经营数据公告 外贸模式 销售收入 2023年; 恒顺醋业 2022年 主要经营数据 外贸模式 万元 同比

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 15/4
  - p36 Hengshun foreign trade (export) mode revenue year-on-year growth rate, 2024 vs 2 = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p37 Hengshun vinegar (醋系列) revenue year-on-year growth rate, 2024 vs 2023 = **-2.2** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p38 Hengshun total revenue year-on-year growth rate, 2024 vs 2023 = **0.73** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p39 Hengshun total dealer count at end of 2024 = **2,014** 个 (dealers) (2024-12-31..2024-12-31) [keep: ] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0
- `https://baijiahao.baidu.com/s?id=1650217165547499158` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 11 (scale word '万元' not supported by quote or table header: 11)

### d6 [related_series] Zhenjiang vinegar industry association analyst

Hypothesis: Zhenjiang vinegar industry total exports (and US share) provide a broader total; Hengshun's share of Zhenjiang vinegar production/exports times that total gives Hengshun US volume. Role: alternative top-down when company split unavailable.

Queries issued by the searcher: 镇江香醋 出口 美国 总量 吨; 镇江 醋业协会 出口 数据 恒顺 占比; 恒顺醋业 2024年 年报 境外 营业收入 出口; 镇江香醋 出口 2023年 吨 镇江海关 出口量

- `https://max.book118.com/try_down/558011103137006073.pdf` -> **live_dated** (page date 2024-11-16); points raw/verified 15/9
  - p40 Zhenjiang fragrant vinegar export volume, 2015 = **280** tons (顿, as written) (2015-01-01..2015-12-31) [keep: ] quote: "2015 280 25"
  - p41 Zhenjiang fragrant vinegar export volume, 2016 = **400** tons (顿, as written) (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p42 Zhenjiang fragrant vinegar export volume, 2017 = **600** tons (顿, as written) (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p43 Zhenjiang fragrant vinegar export volume, 2018 = **727** tons (顿, as written) (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p44 Zhenjiang fragrant vinegar export volume, 2019 = **622** tons (顿, as written) (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
  - p45 Zhenjiang fragrant vinegar export value, 2016 = **36** ten thousand USD (万美元) (2016-01-01..2016-12-31) [keep: ] quote: "2016 400 43 36 44"
  - p46 Zhenjiang fragrant vinegar export value, 2017 = **55** ten thousand USD (万美元) (2017-01-01..2017-12-31) [keep: ] quote: "2017 600 50 55 43"
  - p47 Zhenjiang fragrant vinegar export value, 2018 = **66.7** ten thousand USD (万美元) (2018-01-01..2018-12-31) [keep: ] quote: "2018 727 21 66.7 21"
  - p48 Zhenjiang fragrant vinegar export value, 2019 = **58.6** ten thousand USD (万美元) (2019-01-01..2019-12-31) [keep: ] quote: "2019 621.6 -15 58.6 -12"
- `https://english.cnipa.gov.cn/attach/0/8d58d6b60eae471bbf85880b662843e3.pdf` -> **live_dated** (page date 2020-07-08); points raw/verified 1/0
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.thepaper.cn/newsDetail_forward_9815122` -> **live_dated** (page date 2020-11-08); points raw/verified 8/1
  - p49 Hengshun founding year (Qing Daoguang 20th year) = **1,840** year (1840-01-01..1840-12-31) [DISCARD: Founding year 1840; historical trivia with no bearing on 2024 US bottle volume.] quote: "公司创建于清道光二十年(1840年),今年迎来了创建180周年"
- dropped by code checks: 14 (period_end missing or unparseable: 13; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d7 [capacity_consumption] US ethnic-food retail analyst

Hypothesis: US retail sell-through of Hengshun vinegar = number of US retail outlets carrying it × average annual units per store; role: bottom-up cross-check on shipment-based routes, capturing channel breadth.

Queries issued by the searcher: Hengshun vinegar Weee H Mart 99 Ranch Chinkiang vinegar US retail; 恒顺醋业 2024年年报 境外 收入 出口; China HS 2209 vinegar exports to United States 2024 volume tonnes customs statistics; 99 Ranch Market number of stores 2024 H Mart number of stores US

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.amazon.com/-/zh_TW/%E7%B5%84-%E9%8E%AE%E6%B1%9F%E9%8E%AE%E6%B1%9F%E9%86%8B-%E6%81%86%E9%A0%86%E5%93%81%E7%89%8C-500-%E6%AF%AB%E5%8D%87/dp/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://sameday.hmart.com/store/hmart/products/19479266-heng-shun-vinegar-21-1-fl-oz` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d8 [shocks] Trade-policy and tariff analyst

Hypothesis: US-China tariff actions and shipping disruptions affect 2024 US-bound vinegar volumes and could shift Hengshun's US shipments versus trend; role: adjusts historical relationships and flags period anomalies.

Queries issued by the searcher: US tariff Chinese vinegar HS 2209 2024 Section 301; Section 301 Chinese condiments vinegar tariff rate 2024; 恒顺醋业 2024年年度报告 境外 营业收入 出口; China HS 2209 vinegar exports to United States 2024 value volume customs statistics

- `https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 8/0
- `https://www.nfncb.cn/a49250/49250.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b1 [related_series] company export split

Hypothesis: Hengshun's 2024 annual report (SSE 600305) may disclose overseas/foreign-trade revenue in RMB (p36 implies ~47.74 million RMB foreign-trade mode) and possibly export volume or a regional revenue split. If a US/North-America share or export tonnage is disclosed, d1 becomes a direct route: export volume × US share ÷ average bottle size. This is the single most valuable missing input because it converts the known foreign-trade revenue into a physical US bottle count.

Queries issued by the searcher: 恒顺醋业 2024 年年度报告 境外 营业收入 出口 吨; 600305 2024 annual report overseas revenue export volume; 恒顺 外贸 出口量 2024 吨; "恒顺醋业" "外贸" "2024" "营业收入"; "恒顺" "境外" "营业收入" 2024 年报; "600305_20250422_2SFY.pdf" 外贸 境外

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_XKUV.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1974663940947992576` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://www.jsw.com.cn/2024/1010/1868634.shtml` -> **live_dated** (page date 2024-10-10); points raw/verified 5/2
  - p50 Hengshun cooking wine (料酒) total export volume, cumulative Jan–Sep 2024 = **51.86** tonnes (2024-01-01..2024-09-30) [keep: ] quote: "2024年截止至9月,恒顺料酒总出口量达51.86吨,出口额达7.61万美元"
  - p51 Bottle size of top-exported Hengshun cooking wine products (500ml scallion-ginge = **500** millilitres per bottle (2024-01-01..2024-09-30) [keep: ] quote: "500ml恒顺葱姜料酒、500ml恒顺料酒、500ml恒顺红烧料酒分别占据出口产品前三位"
- dropped by code checks: 3 (number: value_as_written is only part of a larger CJK number in the quote: 1; number: no number in value_as_written: 2)

### b2 [physical_flow] customs flow 2024

Hypothesis: China customs HS 22090000 exports to the US for calendar 2024 (quantity in litres) would replace the stale 2020-2022 p1 figure and let d2 run for the target year. Combined with a Hengshun share of China vinegar exports, this gives an independent physical-flow cross-check on d1.

Queries issued by the searcher: HS 22090000 2024 出口 美国 数量 升 醋; UN Comtrade 2209 vinegar China United States 2024 export quantity; wits.worldbank.org 2024 Exports partner USA product 220900 vinegar China Liter; "22090000" 2024年 出口 美国 升 醋 海关 数量 金额

- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 15/15
  - p52 China HS 22090000 vinegar exports, total quantity, calendar 2024 = **25,760,168** litres (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p53 China HS 22090000 vinegar exports, total value, calendar 2024 = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p54 China HS 22090000 vinegar exports, average unit price, calendar 2024 = **1.15** USD per litre (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p55 China HS 22090000 vinegar exports, total quantity, calendar 2023 = **21,832,831** litres (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p56 China HS 22090000 vinegar exports, total value, calendar 2023 = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p57 China HS 22090000 vinegar exports, average unit price, calendar 2023 = **1.18** USD per litre (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p58 China HS 22090000 vinegar exports, total quantity, calendar 2022 = **19,604,254** litres (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p59 China HS 22090000 vinegar exports, total value, calendar 2022 = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p60 China HS 22090000 vinegar exports, total quantity, calendar 2021 = **20,249,374** litres (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p61 China HS 22090000 vinegar exports, total value, calendar 2021 = **25,590,784** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p62 China HS 22090000 vinegar exports, total quantity, calendar 2020 = **17,414,624** litres (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
  - p63 China HS 22090000 vinegar exports, total value, calendar 2020 = **23,362,688** USD (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
  - p64 China HS 22090000 vinegar imports, total quantity, calendar 2024 = **6,382,197** litres (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p65 China HS 22090000 vinegar imports, total value, calendar 2024 = **11,585,503** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p66 China HS 22090000 vinegar imports, average unit price, calendar 2024 = **1.82** USD per litre (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
- `https://wits.worldbank.org/trade/comtrade/en/country/All/year/2024/tradeflow/Exports/partner/USA/product/220900` -> **live_dated** (page date 2024-01-01); points raw/verified 15/12
  - p67 China exports of HS 220900 vinegar to United States, 2024, quantity = **4,782,550** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| China \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 4,992.09 \| 4,782,550 \| Liter \|"
  - p68 European Union exports of HS 220900 vinegar to United States, 2024, quantity (as = **49,159,700,000,000** Liter (2024-01-01..2024-12-31) [DISCARD: EU→US 2024 quantity of 4.9e13 L is a unit/parse error (implausible by ~6 orders of magnitude); unusable.] quote: "\| European Union \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 141,787.10 \| 49,159,700,000,000 \| Liter \|"
  - p69 Italy exports of HS 220900 vinegar to United States, 2024, quantity = **37,833,100** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Italy \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 116,567.06 \| 37,833,100 \| Liter \|"
  - p70 Spain exports of HS 220900 vinegar to United States, 2024, quantity = **6,684,730** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Spain \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 15,203.75 \| 6,684,730 \| Liter \|"
  - p71 Canada exports of HS 220900 vinegar to United States, 2024, quantity = **6,797,850** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Canada \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 6,284.60 \| 6,797,850 \| Liter \|"
  - p72 Japan exports of HS 220900 vinegar to United States, 2024, quantity = **5,386,850** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Japan \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 5,822.87 \| 5,386,850 \| Liter \|"
  - p73 Philippines exports of HS 220900 vinegar to United States, 2024, quantity = **2,356,270** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Philippines \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 2,981.09 \| 2,356,270 \| Liter \|"
  - p74 Other Asia, nes exports of HS 220900 vinegar to United States, 2024, quantity = **1,191,510** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Other Asia, nes \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 1,772.12 \| 1,191,510 \| Liter \|"
  - p75 Korea, Rep. exports of HS 220900 vinegar to United States, 2024, quantity = **1,067,620** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Korea, Rep. \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 1,760.07 \| 1,067,620 \| Liter \|"
  - p76 Hong Kong, China exports of HS 220900 vinegar to United States, 2024, quantity = **517,937** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Hong Kong, China \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 1,603.68 \| 517,937 \| Liter \|"
  - p77 Thailand exports of HS 220900 vinegar to United States, 2024, quantity = **147,901** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| Thailand \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 168.09 \| 147,901 \| Liter \|"
  - p78 France exports of HS 220900 vinegar to United States, 2024, quantity = **2,817,740** Liter (2024-01-01..2024-12-31) [keep: ] quote: "\| France \| Export \| 220900 \| Vinegar and substitutes for vinegar obtained fr \| 2024 \| United States \| 5,929.41 \| 2,817,740 \| Liter \|"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p79 China HS 22090000 vinegar exports to the United States, quantity, cumulative 202 = **6,597,078** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p1 (same 2020-2022 US quantity).] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p80 China HS 22090000 vinegar exports to the United States, value, cumulative 2020-0 = **8,459,027** US dollars (2020-01-01..2022-12-31) [DISCARD: Duplicate of p2.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p81 United States share of China HS 22090000 vinegar export quantity, cumulative 202 = **11.35** % (2020-01-01..2022-12-31) [DISCARD: Duplicate of p3.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p82 China HS 22090000 vinegar exports worldwide, total quantity, cumulative 2020-01  = **58,119,878** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p4.] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p83 Number of destination countries for China HS 22090000 vinegar exports, cumulativ = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p84 China HS 22090000 vinegar exports to Hong Kong, quantity (largest destination),  = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p6 (Hong Kong quantity).] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p85 China HS 22090000 vinegar exports to Hong Kong, value (largest destination), cum = **15,656,412** US dollars (2020-01-01..2022-12-31) [DISCARD: Duplicate of p7.] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p86 Hong Kong share of China HS 22090000 vinegar export quantity, cumulative 2020-01 = **23.44** % (2020-01-01..2022-12-31) [DISCARD: Duplicate of p8.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p87 China HS 22090000 vinegar exports to Singapore, quantity, cumulative 2020-01 to  = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p9.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p88 China HS 22090000 vinegar exports to Australia, quantity, cumulative 2020-01 to  = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p10.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p89 China HS 22090000 vinegar exports to Netherlands, quantity, cumulative 2020-01 t = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p11.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p90 China HS 22090000 vinegar exports to Malaysia, quantity, cumulative 2020-01 to 2 = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p12.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p91 China HS 22090000 vinegar exports to Canada, quantity, cumulative 2020-01 to 202 = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p13.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p92 China HS 22090000 vinegar exports to Japan, quantity, cumulative 2020-01 to 2022 = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Duplicate of p14.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- dropped by code checks: 4 (scale word 'thousand' not supported by quote or table header: 3; value_as_written not in quote as a whole number: 1)

### b3 [related_series] US import records

Hypothesis: A 2024 US import/bill-of-lading pull for Hengshun/Chinkiang vinegar consignees would give container counts and weights directly attributable to Hengshun, converting via the p19/p24-p35 bottle sizes. This is the only route that measures the US side independently and could resolve disagreement between d1 and d2.

Queries issued by the searcher: ImportYeti Hengshun vinegar shipments; Panjiva Chinkiang vinegar US imports 2024 Hengshun; importgenius "Jiangsu Hengshun" vinegar 2024 bill of lading 550ML 24; 52wmb 镇江恒顺 醋 出口 美国 2024 提单 重量

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/6
  - p93 Piece count on bill of lading EGLV142252207486 for Chinkiang Vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p18.] quote: "Piece Count 700"
  - p94 Bottle size in bill of lading description: Chinkiang Vinegar 550ML per case of 2 = **550** millilitres per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p19.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p95 Bottles per case in bill of lading description (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p20.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p96 Container length dimension on bill of lading EGLV142252207486 = **240** centimetres (container length) (2022-08-13..2022-08-13) [DISCARD: Container dimension, not needed for bottle count.] quote: "Length 240"
  - p97 Container height dimension on bill of lading EGLV142252207486 = **102** centimetres (container height) (2022-08-13..2022-08-13) [DISCARD: Container dimension, not needed for bottle count.] quote: "Height 102"
  - p98 Container width dimension on bill of lading EGLV142252207486 = **96** centimetres (container width) (2022-08-13..2022-08-13) [DISCARD: Container dimension, not needed for bottle count.] quote: "Width 96"
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar', 'china vinegar exports', 'us vinegar imports']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] Same source (m.x315.cn) reporting China HS 22090000 export totals; p1/p2 are the US line, p3 is its share, p4 the all-destination total. Internally consistent (p1/p4 ≈ p3) but a single underlying meas
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] Same source, same 2020-2022 window, other destination lines. Useful only as context on the destination mix (US is the #2 destination after Hong Kong); they do not measure Hengshun.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23'] All from one ImportGenius supplier page / one bill of lading. p15-p17 are cumulative 2006-2022 counts (44 shipments, 6 partners, 5 ports) — a sparse, stale footprint. p18-p23 describe a single 2022 co
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35'] One distributor catalogue (fivecontinentsintl.com) listing Hengshun US SKUs. Establishes the bottle-size mix: mostly 500 ml, some 535/550/580 ml, a 300 ml premium and a 3 L food-service size. Supplies
- corroborating: ['p36', 'p37', 'p38', 'p39'] Same annual-report extract (Sina, 2025-04-22). p36 gives 2024 foreign-trade-mode revenue growth +5.78%; p37/p38 give vinegar-series and total revenue growth. These are growth rates and dealer counts, 
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] One secondary document on Zhenjiang fragrant-vinegar exports 2015-2019 (volume in tons, value in 万美元). Consistent internal trend but ends in 2019, is all-destination, and is Zhenjiang-region not Hengs
- conflicting: ['p1', 'p40'] Scope/period mismatch rather than true contradiction: p1 is China-wide HS2209 to the US for 2020-2022; p40-p44 are Zhenjiang-region all-destination exports 2015-2019. They cannot be combined by per-ye
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p79', 'p80', 'p81', 'p82'] Same underlying m.x315.cn HS 22090000 dataset; p1/p79, p2/p80, p3/p81, p4/p82 are duplicate copies of the same 2020-2022 cumulative figures. They establish that the US took ~11.35% of China's vinegar 
- corroborating: ['p52', 'p53', '54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63'] Consistent annual HS 22090000 total-export series from one customs aggregator; shows China's total vinegar exports grew from ~17.4M L (2020) to ~25.8M L (2024). Provides the denominator for a US-share
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78'] WITS 2024 bilateral HS 220900 export quantities to the US. p67 (China→US 4.78M L) is the key figure; p68 (EU 4.9e13 L) is an obvious unit/parse error and unusable. Other origins are context only.
- corroborating: ['p15', 'p18', 'p19', 'p20', 'p93', 'p94', 'p95'] ImportGenius bill-of-lading evidence: Hengshun has US shipments, and a 550ml@24 case format is documented. p18/p93, p19/p94, p20/p95 are duplicate copies. Only one shipment is visible, so this cannot 
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35'] US-facing Hengshun SKU list from a distributor; bottle sizes cluster at 500ml with 300-580ml and 3L outliers. Supplies the bottle-size conversion factor and mix.
- corroborating: ['p36', 'p37', 'p38', 'p39'] Hengshun 2024 annual-report segment data: foreign-trade revenue ~47.74M RMB (+5.78%), vinegar series revenue down 2.2%, total revenue +0.73%, 2014 dealers. Gives the export revenue envelope but no US 
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] Zhenjiang fragrant-vinegar export tonnage/value 2015-2019, peaking ~727 t in 2018. Old and industry-wide, not Hengshun-specific or US-specific; useful only as an order-of-magnitude sanity check.
- corroborating: ['p50', 'p51'] 2024 Jan-Sep Hengshun cooking-wine export volume 51.86 t at 500ml; shows Hengshun's total export physical volume is small (tens of tonnes), which bounds any US vinegar bottle count.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Hengshun share of China HS 220900 vinegar export volume to the US, 2024 | 8 | 2..25 | 2..25 | % | m1 (m1) | Hengshun is the largest branded Zhenjiang vinegar exporter but China's HS 220900 US flow includes many other producers and non-Zhenjiang vinegars; a single-digit-to-low-double-digit share is plausible. Anchored loosely on Hengshun's foreign-trade revenue (~47.7M RMB) being a modest fraction of China | Used to split the 2024 China→US HS 220900 volume (p67) into Hengshun's portion. | A disclosed Hengshun US export tonnage or a bill-of-lading total showing a materially different share. |
| a2 | Average Hengshun US bottle size (litres per bottle) | 0.5 | 0.35..0.75 | 0.35..0.75 | litres per bottle | m1 (m1) | US SKU list (p26-p35) clusters at 500 ml with 300-580 ml variants and a 3 L food-service outlier; volume-weighted mean near 0.5 L. | Converts Hengshun US vinegar litres to bottles. | Evidence that 3 L food-service sizes dominate US volume. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 659,014 | ['p67'] / ['a1', 'a2'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **659,014** bottle, 80% interval [174,390, 2,490,389] bottle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['hengshun', 'us', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']; 11 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

The best computed estimate is 659,014 bottle (80% model-based interval 174,390 to 2,490,389 bottle) for bottles of Hengshun bottled vinegar shipped/sold into the United States in calendar 2024, all bottled types combined, excluding bulk drums.

This comes from a single physical-flow method (659,014 bottle, weight 100%): China's 2024 HS [n] vinegar exports to the US of 4,782,550 Liter multiplied by Hengshun's assumed share (8%, range 2% to 25%) and divided by average bottle size (0.5 litres, range 0.35 to 0.75).

Only the customs flow is observed; the Hengshun share and bottle size are analyst assumptions, not measured. The interval is conditional on those assumptions, not a demonstrated accuracy guarantee.

The biggest risk is the assumed Hengshun share, since the HS flow mixes many producers and vinegars. Better evidence would be Hengshun's own US export volumes or distributor shipment records.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Hengshun share of China HS [n] vinegar export volume to the US, 2024: 8%, range 2% to 25%; used by m1. Overturned by: A disclosed Hengshun US export tonnage or a bill-of-lading total showing a materially different share.
- a2 Average Hengshun US bottle size (litres per bottle): 0.5 litres per bottle, range 0.35 to 0.75; used by m1. Overturned by: Evidence that [n] L food-service sizes dominate US volume.

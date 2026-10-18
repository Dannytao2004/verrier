# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types, including aromatic vinegar/香醋 and other bottled vinegars) sold by Jiangsu Hengshun Group into the United States market, counted as bottles (retail units) delivered/sold in the period | unit bottle | period 2025-01-01..2025-12-31 | publisher None official; Jiangsu Hengshun Vinegar-Industry Co., Ltd. (600305.SH) annual report and China customs export statistics are the closest reporting sources

## Directions and pages

### d1 [own_history] Hengshun corporate reporting

Hypothesis: Hengshun's annual report discloses total export revenue and possibly export volume; if US is a named market or if overseas revenue share and US share of exports can be estimated, US bottle volume = total export volume × US share of exports. Direction: higher export revenue and higher US share imply more bottles.

Queries issued by the searcher: 恒顺醋业 年报 出口 境外收入; 600305 恒顺 出口 美国 销量; Hengshun vinegar annual report export revenue overseas; 恒顺醋业 2025年年度报告 产销量 醋系列 销售量 吨; 恒顺 香醋 出口 吨 美国 占比 出口量; 中国 食醋 出口 美国 出口量 海关 统计 2024

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=12089193` -> **live_dated** (page date 2026-04-15); points raw/verified 14/11
  - p1 Jiangsu Hengshun Vinegar-Industry total operating revenue 2025 = **2,286,538,594** CNY (2025-01-01..2025-12-31) [keep: ] quote: "营业收入 \| 2,286,538,593.94 \| 2,195,870,508.45 \| 4.13 \| 2,106,410,685.37"
  - p2 Hengshun foreign trade (外贸模式) revenue 2025 = **39,171,647** CNY (2025-01-01..2025-12-31) [keep: ] quote: "外贸模式 \| 39,171,647.23 \| 29,715,440.56 \| 24.14 \| -17.95 \| -14.38 \| 减少3.16个百分点"
  - p3 Hengshun foreign trade (外贸模式) revenue year-on-year change 2025 = **-17.95** % (2025-01-01..2025-12-31) [keep: Kept as a change descriptor; useful only as a YoY signal, not a level.] quote: "外贸模式 \| 39,171,647.23 \| 29,715,440.56 \| 24.14 \| -17.95 \| -14.38 \| 减少3.16个百分点"
  - p4 Hengshun foreign trade (外贸模式) gross margin 2025 = **24.14** % (2025-01-01..2025-12-31) [keep: Kept as context on foreign-trade margin; not directly usable in a volume formula.] quote: "外贸模式 \| 39,171,647.23 \| 29,715,440.56 \| 24.14 \| -17.95 \| -14.38 \| 减少3.16个百分点"
  - p5 Hengshun vinegar (醋系列) sales volume 2025 = **228,113** tonnes (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22"
  - p6 Hengshun vinegar (醋系列) production volume 2025 = **235,643** tonnes (2025-01-01..2025-12-31) [keep: Production volume; useful as a capacity/consistency check against sales volume p5.] quote: "醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22"
  - p7 Hengshun vinegar (醋系列) revenue 2025 = **1,321,092,496** CNY (2025-01-01..2025-12-31) [keep: ] quote: "醋系列 \| 1,321,092,495.56 \| 709,855,429.02 \| 46.27 \| 4.38 \| 2.57 \| 增加0.95个百分点"
  - p8 Hengshun condiment (调味品) revenue 2025 = **2,266,466,159** CNY (2025-01-01..2025-12-31) [DISCARD: Condiment segment revenue; broader than vinegar and not needed.] quote: "调味品 \| 2,266,466,159.39 \| 1,537,411,067.26 \| 32.17 \| 8.29 \| 13.18 \| 减少2.93个百分点"
  - p9 Hengshun online sales revenue 2025 = **303,231,521** CNY (2025-01-01..2025-12-31) [DISCARD: Online sales revenue (domestic e-commerce); not US export.] quote: "线上销售 \| 303,231,520.67 \| 13.38 \| 61.94 \| 274,378,140.67 \| 13.11 \| 53.17"
  - p10 Hengshun products sold to countries/regions (breadth of export footprint) = **85** countries and regions (2025-01-01..2025-12-31) [keep: 85-country export footprint; needed to reason about US share of exports.] quote: "产品连续20多年销量全国领先,广销85个国家和地区"
  - p11 Hengshun USD accounts receivable foreign-currency balance at year-end 2025 = **344,022** USD (2025-12-31..2025-12-31) [keep: USD receivable balance; weak corroboration of USD-denominated export activity.] quote: "其中:美元 \| 344,021.67 \| 7.0288 \| 2,418,059.51"
- `https://stock.hexun.com/2026-04-20/224024413.html` -> **live_dated** (page date 2026-04-20); points raw/verified 0/0
- `http://europe.chinadaily.com.cn/china/2016-06/10/content_25663416_7.htm` -> **dropped** (live http 404); points raw/verified -/-
- dropped by code checks: 18 (value_as_written not in quote as a whole number: 15; number: value_as_written is only part of a larger CJK number in the quote: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; number: no number in value_as_written: 1)

### d2 [related_series] China customs trade statistics

Hypothesis: China customs HS code 2209 (vinegar and substitutes) exports to the US give total Chinese vinegar export volume/value to the US; Hengshun's share of China's vinegar exports to the US (by value or volume) times that total gives Hengshun's US volume. Direction: larger total US-bound vinegar exports or larger Hengshun share imply more bottles.

Queries issued by the searcher: China vinegar exports United States HS 2209 volume value; 中国 海关 醋 出口 美国 2209 数量 金额; 恒顺醋业 年报 出口 境外 收入 占比 2024; Hengshun vinegar export share China vinegar exports percentage largest exporter

- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p12 China HS 22090000 vinegar exports to the United States, quantity (cumulative, 20 = **6,597,078** litres (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p13 China HS 22090000 vinegar exports to the United States, value (cumulative, 2020- = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p14 United States share of China HS 22090000 vinegar export quantity (cumulative, 20 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p15 China HS 22090000 vinegar exports worldwide, total quantity (cumulative, 2020-01 = **58,119,878** litres (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p16 Number of destination countries for China HS 22090000 vinegar exports (cumulativ = **129** countries (2020-01-01..2022-12-31) [DISCARD: Count of destination countries; no volume information, redundant with p10 context.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p17 China HS 22090000 vinegar exports to Hong Kong, quantity (cumulative, 2020-01 to = **13,624,552** litres (2020-01-01..2022-12-31) [DISCARD: Hong Kong quantity; not the US target and not needed for the US route.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p18 China HS 22090000 vinegar exports to Hong Kong, value (cumulative, 2020-01 to 20 = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Hong Kong value; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p19 China HS 22090000 vinegar exports to Singapore, quantity (cumulative, 2020-01 to = **4,057,620** litres (2020-01-01..2022-12-31) [DISCARD: Singapore quantity; not the US target.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p20 China HS 22090000 vinegar exports to Australia, quantity (cumulative, 2020-01 to = **3,691,524** litres (2020-01-01..2022-12-31) [DISCARD: Australia quantity; not the US target.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p21 China HS 22090000 vinegar exports to Netherlands, quantity (cumulative, 2020-01  = **3,519,273** litres (2020-01-01..2022-12-31) [DISCARD: Netherlands quantity; not the US target.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p22 China HS 22090000 vinegar exports to Malaysia, quantity (cumulative, 2020-01 to  = **3,160,711** litres (2020-01-01..2022-12-31) [DISCARD: Malaysia quantity; not the US target.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p23 China HS 22090000 vinegar exports to Canada, quantity (cumulative, 2020-01 to 20 = **2,537,372** litres (2020-01-01..2022-12-31) [DISCARD: Canada quantity; not the US target.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p24 China HS 22090000 vinegar exports to Japan, quantity (cumulative, 2020-01 to 202 = **2,404,533** litres (2020-01-01..2022-12-31) [DISCARD: Japan quantity; not the US target.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p25 China HS 22090000 vinegar exports to France, quantity (cumulative, 2020-01 to 20 = **1,754,906** litres (2020-01-01..2022-12-31) [DISCARD: France quantity; not the US target.] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `https://chinadata.live/china-trade/hs/220900/` -> **dropped** (live http 403); points raw/verified -/-
- `https://q.stock.sohu.com/cn/news.html?textId=100018443238&tab=100&type=100&code=cn_600305&date=2026/0415` -> **live_dated** (page date 2026-05-23); points raw/verified 0/0
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [physical_flow] US import records / bill of lading data

Hypothesis: US import bill-of-lading and customs entry data (e.g., Panjiva, ImportGenius, US Census USA Trade Online) record shipments of vinegar from Chinese exporters including Hengshun to US importers; summing shipment weights and converting to bottles via average bottle size yields the target. Direction: more recorded shipments/weight imply more bottles.

Queries issued by the searcher: Panjiva Hengshun vinegar US imports bill of lading; "Hengshun" vinegar US import shipments customs records; ImportYeti "Hengshun" vinegar supplier shipments; 52wmb 恒顺 香醋 美国 进口 提单 2025

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p26 Total US import shipments recorded for Jiangsu Hengshun Group (cumulative, 2006- = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p27 Number of trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p28 Number of ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p29 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p30 Bottle size stated in cargo description for Chinkiang vinegar (550ML@24) = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p31 Bottles per case stated in cargo description (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p32 Container length on bill of lading EGLV142252207486 = **240** container length (cm) (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p33 Container height on bill of lading EGLV142252207486 = **102** container height (cm) (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p34 Container width on bill of lading EGLV142252207486 = **96** container width (cm) (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-

### d4 [capacity_consumption] US retail/wholesale channel

Hypothesis: US Asian grocery retail sales of Hengshun-brand vinegar (scanner or distributor data) times bottles per unit gives sell-through; if only retail dollar sales are available, divide by average retail price per bottle. Direction: higher US retail sales of Hengshun vinegar imply more bottles.

Queries issued by the searcher: Hengshun vinegar US retail sales; 恒顺醋业 年报 境外 收入 出口 占比; 恒顺 美国 出口 北美 市场 香醋 销售额; Hengshun vinegar USA distributor importer Asian grocery wholesale case

- `https://www.9fzt.com/detail/sh_600305_9_eeda55b1c527cc3d1df240904019c864.html` -> **live_dated** (page date 2026-04-15); points raw/verified 15/2
  - p35 Hengshun self-operated e-commerce sales growth, 2025 (year-on-year) = **76** % (2025-01-01..2025-12-31) [DISCARD: Domestic self-operated e-commerce growth; irrelevant to US export bottle count.] quote: "充分从市场端着手,自营电商实现销售增长76%"
  - p36 Hengshun domestic distributor count (全国经销商), 2025 = **1,800** distributors (2025-01-01..2025-12-31) [DISCARD: Domestic distributor count; irrelevant to US export volume.] quote: "覆盖全国超1800家经销商,终端网点突破"
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://www.weee.com/th/product/Hengshun-Zhenjiang-Vinegar/99090` -> **live_dated** (page date 2026-10-18); points raw/verified 3/0
- `https://www.inst.cr/store/products/17891988-heng-shun-hs-6-yr-aged-zhenjian-vinegar-19-6-fl-oz` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 31 (value_as_written not in quote as a whole number: 26; period_end missing or unparseable: 5)

### d5 [base_rates] Conversion and product-mix

Hypothesis: Bottle count = export volume (litres or kg) / average bottle size (litres or kg per bottle), adjusted for product mix (500 ml dominant, some 250 ml/1 L) and bulk/non-retail exports. Direction: smaller average bottle size or larger volume implies more bottles.

Queries issued by the searcher: 恒顺香醋 出口 规格 500ml 瓶; Hengshun vinegar bottle size export US 500ml; 恒顺醋业 年报 境外 营业收入 出口 占比 2024; Chinkiang vinegar US imports volume litres customs HS 2209 China

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://fivecontinentsintl.com/en/product/hengshun-brand-cooking-wine-with-shallot-and-ginger/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p37 HengShun cooking wine with shallot and ginger case size, bottles per case (500ml = **12** bottles per case (..) [keep: Bottles-per-case 12 for a 500 ml SKU; conversion factor for case-to-bottle.] quote: "Case Size: 500ml*12btls"
  - p38 HengShun cooking wine with shallot and ginger bottle size (ml per bottle) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine with Shallot And Ginger(500ml)"
  - p39 HengShun 9 Degrees Rice Vinegar bottle size (ml per bottle) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand 9 Degrees Rice Vinegar(500ml)"
  - p40 HengShun Cooking Wine With Shallot And Ginger 0 Additives bottle size (ml per bo = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Cooking Wine With Shallot And Ginger 0 Additives(500ml)"
  - p41 HengShun Six Years Vinegar bottle size (ml per bottle) = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Six Years Vinegar(580ml)"
  - p42 HengShun Three Years Vinegar bottle size (ml per bottle) = **580** ml per bottle (..) [keep: ] quote: "HengShun Brand Three Years Vinegar(580ml)"
  - p43 HengShun Vinegar 0 Additives bottle size (ml per bottle) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar 0 Additives(500ml)"
  - p44 HengShun Vinegar 0 Additives alternate bottle size (ml per bottle) = **535** ml per bottle (..) [DISCARD: 535 ml alternate SKU; minor variant, redundant with 500/550 ml cluster.] quote: "HengShun Brand Vinegar 0 Additives(535ml)"
  - p45 HengShun Vinegar for Dumpling bottle size (ml per bottle) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Dumpling(500ml)"
  - p46 HengShun Vinegar for Steamed Buns bottle size (ml per bottle) = **550** ml per bottle (..) [keep: ] quote: "HengShun Brand Vinegar for Steamed Buns(550ml)"
  - p47 HengShun White Rice Vinegar bottle size (ml per bottle) = **500** ml per bottle (..) [keep: ] quote: "HengShun Brand White Rice Vinegar(500ml)"
  - p48 HengShun Zhenjiang Eight Years Vinegar bottle size (ml per bottle) = **300** ml per bottle (..) [keep: ] quote: "HengShun Brand Zhenjiang Eight Years Vinegar(300ml)"
- `https://emmefoods.com/zh/2-%e4%b8%bb%e9%a1%b5?q=%E5%88%86%E7%B1%BB-%E8%B0%83%E6%96%99%E9%85%B1%E6%96%99/%E5%93%81%E7%89%8C-%E5%9D%9B%E5%9D%9B%E4%B9%A1` -> **live_dated** (page date 2007-01-01); points raw/verified 11/11
  - p49 Hengshun large-bucket Zhenjiang aromatic vinegar bottle size (3L retail unit) = **3** litres per bottle (..) [DISCARD: 3 L bulk bucket SKU; atypical for US retail and would distort average bottle size if included.] quote: "恒顺大桶镇江香醋 3L"
  - p50 Hengshun Zhenjiang aromatic vinegar 6-year aged bottle size = **580** mL per bottle (..) [keep: ] quote: "恒顺镇江香醋 6年陈 580mL"
  - p51 Hengshun Zhenjiang aromatic vinegar 3-year aged bottle size = **580** mL per bottle (..) [keep: ] quote: "恒顺镇江香醋3年陈 580mL"
  - p52 Hengshun Zhenjiang aromatic vinegar 8-year aged bottle size = **300** mL per bottle (..) [keep: ] quote: "恒顺镇江香醋8年熟成 300mL"
  - p53 Hengshun Zhenjiang aromatic vinegar K-type bottle size = **550** ml per bottle (..) [keep: ] quote: "恒顺镇江香醋K型 550ml"
  - p54 Hengshun Zhenjiang aromatic vinegar (K-type) retail price = **2.39** USD per bottle (..) [keep: ] quote: "恒顺镇江香醋K型 550ml $2.39"
  - p55 Hengshun large-bucket Zhenjiang aromatic vinegar retail price = **12.99** USD per bottle (..) [keep: ] quote: "恒顺大桶镇江香醋 3L $12.99"
  - p56 Hengshun Zhenjiang aromatic vinegar 6-year aged retail price = **7.49** USD per bottle (..) [keep: ] quote: "恒顺镇江香醋 6年陈 580mL $7.49"
  - p57 Hengshun Zhenjiang aromatic vinegar 3-year aged retail price = **5.79** USD per bottle (..) [keep: ] quote: "恒顺镇江香醋3年陈 580mL $5.79"
  - p58 Hengshun Zhenjiang aromatic vinegar 8-year aged retail price = **9.29** USD per bottle (..) [keep: ] quote: "恒顺镇江香醋8年熟成 300mL $9.29"
  - p59 Total number of products listed on the page = **52** products (..) [DISCARD: Count of products on a 2007 retailer page; no bearing on US volume.] quote: "这里有52件商品。"
- `https://www.sgpjbg.com/baogao/631780.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 15 (value_as_written not in quote as a whole number: 15)

### d6 [persona] US importer/distributor

Hypothesis: US importers/distributors of Hengshun vinegar (e.g., Asian food distributors) may disclose purchase volumes or container counts; containers per year × bottles per container gives an upper-bound flow. Direction: more containers or larger container loads imply more bottles.

Queries issued by the searcher: Hengshun vinegar US distributor importer; 镇江香醋 美国 进口商 经销商; Chinkiang vinegar container import US; Hengshun vinegar 40ft container bottles

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p60 Total shipments recorded for Jiangsu Hengshun Group (supplier), all destinations = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Duplicate of p26/p108 (same ImportGenius 44-shipment count); adds no information.] quote: "Total Shipments 44"
  - p61 Trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Duplicate of p27/p109 (6 trading partners).] quote: "Trading Partners 6"
  - p62 Ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Duplicate of p28/p110 (5 ports).] quote: "Ports 5"
  - p63 Piece count on bill of lading EGLV142252207486 (Chinkiang vinegar 550ML@24), arr = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p29/p111 (700 pieces).] quote: "Piece Count 700"
  - p64 Bottles per case for Chinkiang vinegar 550ML SKU on bill of lading (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p31/p113 (24 bottles/case).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p65 Bottle size of Chinkiang vinegar SKU on bill of lading = **550** ml per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p30/p112 (550 ml).] quote: "CHINKIANG VINEGAR 550ML@24"
  - p66 Container length (cm) of 20-foot general purpose container on bill of lading = **240** cm (container length) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p32/p114 (240 cm).] quote: "Length 240 \| Height 102 \|"
  - p67 Container height (cm) of 20-foot general purpose container on bill of lading = **102** cm (container height) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p33/p115 (102 cm).] quote: "Length 240 \| Height 102 \|"
  - p68 Container width (cm) of 20-foot general purpose container on bill of lading = **96** cm (container width) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p34/p116 (96 cm).] quote: "Width 96 \| Load Status Loaded"
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-

### d7 [shocks] Trade policy and market conditions

Hypothesis: US-China tariffs, shipping costs, and demand shifts (e.g., 2025 tariff changes) affect Hengshun's US export volume; identifying year-over-year change in US-bound vinegar trade adjusts a base-year estimate. Direction: tariff increases or demand declines reduce bottles; tariff relief increases them.

Queries issued by the searcher: US tariff Chinese vinegar 2209 2025; China vinegar exports to United States 2024 2025 HS 2209; 恒顺醋业 美国 出口 关税 影响 2025; Hengshun vinegar US export tariff impact

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=1969487190114107392` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/` -> **dropped** (live http 403); points raw/verified -/-
- `https://tariffs.wove.com/us/tariff/2209.00.00.00/champagne-vinegar/from/CN` -> **live_dated** (page date 2026-01-01); points raw/verified 3/0
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 3 (period_end missing or unparseable: 1; value_as_written not in quote as a whole number: 2)

### d8 [forecasts_markets] Industry and company guidance

Hypothesis: Hengshun's strategic plans and industry reports may state overseas expansion targets or US market entry volumes; these are intentions, not realized sales, but can bound the estimate. Direction: higher stated overseas/US targets imply higher expected bottles.

Queries issued by the searcher: 恒顺醋业 海外 战略 美国 市场 出口 目标; Hengshun vinegar overseas expansion US market plan; 恒顺醋业 2024年 年报 境外 营业收入 出口 占比; 恒顺醋业 海外市场 出口 亿元 目标 2025

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2180983407054532608` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.sgpjbg.com/baogao/631780.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.fxbaogao.com/detail/5157109` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b1 [own_history] company disclosure

Hypothesis: Hengshun's annual report or investor Q&A may disclose the US/overseas share of foreign-trade revenue or export volume by region. This would convert p2 (foreign-trade revenue) directly into a US vinegar volume, unlocking the d1 route without needing a customs-share assumption.

Queries issued by the searcher: 600305 2025 年报 境外 收入 分地区 恒顺; 恒顺 出口 美国 销量 吨 香醋; 恒顺醋业 外贸 出口 美国 占比 投资者关系 互动; 中国 食醋 出口 美国 数量 吨 海关 2024 镇江香醋

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/company/rptid/830029140893/index.phtml` -> **live_dated** (page date 2026-04-20); points raw/verified 15/10
  - p69 Hengshun 2025 total operating revenue = **2,287,000,000** CNY yuan (2025-01-01..2025-12-31) [keep: ] quote: "25 年公司实现营业收入22.87 亿,同比+4.13%"
  - p70 Hengshun 2025 foreign trade (外贸) revenue = **39,000,000** CNY yuan (2025-01-01..2025-12-31) [keep: ] quote: "25 年公司经销/直销/外贸分别实现营收20.39/1.89/0.39 亿元,同比+5.0%/+81.84%/-17.95%"
  - p71 Hengshun 2025 foreign trade revenue YoY change = **-17.95** % (2025-01-01..2025-12-31) [keep: ] quote: "外贸分别实现营收20.39/1.89/0.39 亿元,同比+5.0%/+81.84%/-17.95%"
  - p72 Hengshun 2025 vinegar product revenue YoY change = **4.38** % (2025-01-01..2025-12-31) [DISCARD: Vinegar revenue YoY change; not needed for US bottle decomposition.] quote: "分别同比+4.38%/-7.60%/-3.34%/+46.72%"
  - p73 Hengshun 2025 gross margin = **32.4** % (2025-01-01..2025-12-31) [DISCARD: Overall gross margin; not used in any US bottle route.] quote: "25 年公司毛利率32.4%,同比-2.3pcts"
  - p74 Hengshun 2025 net margin attributable to parent = **6.3** % (2025-01-01..2025-12-31) [DISCARD: Net margin; not used.] quote: "最终公司归母净利率6.3%,同比+0.5pcts"
  - p75 Hengshun 2025 net profit attributable to parent = **144,000,000** CNY yuan (2025-01-01..2025-12-31) [DISCARD: Net profit; not used.] quote: "归母净利润1.44 亿,同比+12.80%"
  - p76 Hengshun 2025Q4 operating revenue = **659,000,000** CNY yuan (2025-10-01..2025-12-31) [DISCARD: Q4 revenue; not used.] quote: "其中Q4 公司实现营业收入6.59 亿,同比-0.88%"
  - p77 Hengshun 2025Q4 gross margin = **20.4** % (2025-10-01..2025-12-31) [DISCARD: Q4 gross margin; not used.] quote: "25Q4 公司毛利率20.4%,同比-10.9pcts"
  - p78 Hengshun 2025 sales expense ratio = **16.5** % (2025-01-01..2025-12-31) [DISCARD: Sales expense ratio; not used.] quote: "25 年公司销售/管理费用率分别为16.5/4.3pcts"
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2262519666433040384` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.9fzt.com/detail/sh_600305_9_eeda55b1c527cc3d1df240904019c864.html` -> **live_dated** (page date 2026-04-15); points raw/verified 15/0
- dropped by code checks: 35 (value_as_written not in quote as a whole number: 27; scale word '亿' not supported by quote or table header: 4; number: no number in value_as_written: 1; number: value_as_written is only part of a larger CJK number in the quote: 1; period_end missing or unparseable: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b2 [related_series] customs trade statistics

Hypothesis: Annual (not 3-year cumulative) China HS 22090000 exports to the US for 2023-2025, plus Hengshun's share of China's vinegar exports, would let us scale p12 to the target year and carve out Hengshun's portion. This is the missing input for the d2 route.

Queries issued by the searcher: HS 22090000 出口 美国 2024 数量 食醋; China vinegar exports to US 2024 2025 UN Comtrade HS 220900; 恒顺 占 中国 食醋 出口 份额 出口量 全国; 恒顺醋业 2024年 年报 境外 出口 收入 海外

- `https://chinadata.live/china-trade/hs8/22090000/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.jcksj.com/report/22090000.html` -> **live_dated** (page date 2026-09-08); points raw/verified 15/15
  - p79 China HS 22090000 exports to the United States, 2025 annual value = **3,787,074** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p80 China HS 22090000 exports to the United States, 2024 annual value = **4,992,092** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p81 China HS 22090000 exports to the United States, 2025 vs 2024 year-on-year change = **-24.14** % (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p82 China HS 22090000 total exports, 2025 annual value (all destinations) = **27,891,245** USD (2025-01-01..2025-12-31) [keep: ] quote: "27,891,245 美元"
  - p83 China HS 22090000 total exports, 2024 annual value (all destinations) = **29,676,894** USD (2024-01-01..2024-12-31) [keep: ] quote: "29,676,894 美元29676894"
  - p84 China HS 22090000 total exports, 2025 vs 2024 year-on-year change = **-6.02** % (2025-01-01..2025-12-31) [keep: ] quote: "较2024年-6.02%"
  - p85 China HS 22090000 total exports, 2025 annual value in ten-thousand USD = **27,891,200** USD (ten-thousand) (2025-01-01..2025-12-31) [keep: ] quote: "2789.12万美元"
  - p86 China HS 22090000 total imports, 2025 annual value (all origins) = **11,979,467** USD (2025-01-01..2025-12-31) [DISCARD: China HS22090000 imports (all origins) — wrong direction of trade, irrelevant.] quote: "11,979,467 美元"
  - p87 China HS 22090000 total imports, 2024 annual value (all origins) = **9,806,210** USD (2024-01-01..2024-12-31) [DISCARD: China HS22090000 imports 2024 — wrong direction of trade, irrelevant.] quote: "9,806,210 美元9806210"
  - p88 China HS 22090000 imports from the United States, 2025 annual value = **1,875,118** USD (2025-01-01..2025-12-31) [DISCARD: China imports of vinegar from the US — wrong direction, irrelevant.] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p89 China HS 22090000 imports from the United States, 2024 annual value = **2,269,319** USD (2024-01-01..2024-12-31) [DISCARD: China imports of vinegar from the US 2024 — wrong direction, irrelevant.] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p90 China HS 22090000 exports to Hong Kong, 2025 annual value = **4,205,407** USD (2025-01-01..2025-12-31) [DISCARD: Hong Kong 2025 value; not the US target.] quote: "\| 中国香港 \| 4,205,407 \| 4,093,608 \| +111,799 \| +2.73% \| 查询该市场买家 ↗ \|"
  - p91 China HS 22090000 exports to Australia, 2025 annual value = **2,079,038** USD (2025-01-01..2025-12-31) [DISCARD: Australia 2025 value; not the US target.] quote: "\| 澳大利亚 \| 2,079,038 \| 1,959,491 \| +119,547 \| +6.10% \| 查询该市场买家 ↗ \|"
  - p92 China HS 22090000 exports to Netherlands, 2025 annual value = **2,153,886** USD (2025-01-01..2025-12-31) [DISCARD: Netherlands 2025 value; not the US target.] quote: "\| 荷兰 \| 2,153,886 \| 2,398,669 \| -244,783 \| -10.20% \| 查询该市场买家 ↗ \|"
  - p93 China HS 22090000 exports to Singapore, 2025 annual value = **1,654,888** USD (2025-01-01..2025-12-31) [DISCARD: Singapore 2025 value; not the US target.] quote: "\| 新加坡 \| 1,654,888 \| 1,493,383 \| +161,505 \| +10.81% \| 查询该市场买家 ↗ \|"
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p94 China HS 22090000 total vinegar exports to all countries, quantity, 2020-01 to 2 = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p95 China HS 22090000 vinegar exports to the United States, quantity, 2020-01 to 202 = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p96 China HS 22090000 vinegar exports to the United States, value, 2020-01 to 2022-1 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p97 United States share of China HS 22090000 vinegar exports (by quantity), 2020-01  = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p98 Hong Kong share of China HS 22090000 vinegar exports (by quantity), 2020-01 to 2 = **23.44** % (2020-01-01..2022-12-31) [DISCARD: Hong Kong share; not the US target.] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p99 China HS 22090000 vinegar exports to Hong Kong, quantity, 2020-01 to 2022-12 cum = **13,624,552** liters (2020-01-01..2022-12-31) [DISCARD: Hong Kong quantity; not the US target.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p100 China HS 22090000 vinegar exports to Singapore, quantity, 2020-01 to 2022-12 cum = **4,057,620** liters (2020-01-01..2022-12-31) [DISCARD: Singapore quantity; not the US target.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p101 China HS 22090000 vinegar exports to Australia, quantity, 2020-01 to 2022-12 cum = **3,691,524** liters (2020-01-01..2022-12-31) [DISCARD: Australia quantity; not the US target.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p102 China HS 22090000 vinegar exports to Netherlands, quantity, 2020-01 to 2022-12 c = **3,519,273** liters (2020-01-01..2022-12-31) [DISCARD: Netherlands quantity; not the US target.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p103 China HS 22090000 vinegar exports to Malaysia, quantity, 2020-01 to 2022-12 cumu = **3,160,711** liters (2020-01-01..2022-12-31) [DISCARD: Malaysia quantity; not the US target.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p104 China HS 22090000 vinegar exports to Canada, quantity, 2020-01 to 2022-12 cumula = **2,537,372** liters (2020-01-01..2022-12-31) [DISCARD: Canada quantity; not the US target.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p105 China HS 22090000 vinegar exports to Japan, quantity, 2020-01 to 2022-12 cumulat = **2,404,533** liters (2020-01-01..2022-12-31) [DISCARD: Japan quantity; not the US target.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p106 China HS 22090000 vinegar exports to Macau, quantity, 2020-01 to 2022-12 cumulat = **2,087,101** liters (2020-01-01..2022-12-31) [DISCARD: Macau quantity; not the US target.] quote: "第九中国澳门:总数量为2,087,101升;金额2,294,008美元;总占比3.59%。"
  - p107 China HS 22090000 vinegar exports to France, quantity, 2020-01 to 2022-12 cumula = **1,754,906** liters (2020-01-01..2022-12-31) [DISCARD: France quantity; not the US target.] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `http://www.zhenjiang.gov.cn/zhenjiang/sdbd/202409/7528a33328db415cb7cc1a710aac37e3.shtml` -> **dropped** (live http 301); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b3 [physical_flow] import records

Hypothesis: Recent (2023-2025) US import bill-of-lading records for Hengshun/Chinkiang vinegar would give container counts and case counts, converting directly to bottles via p31/p37. This resolves the largest uncertainty (US share of Hengshun exports) and updates the stale 2022 ImportGenius snapshot.

Queries issued by the searcher: Panjiva Hengshun vinegar US imports 2024; ImportGenius Chinkiang vinegar shipments 2024 2025; "Hengshun" vinegar US import bill of lading container; importyeti Chinkiang vinegar shipments Hengshun

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/9
  - p108 Total US customs shipments recorded for Jiangsu Hengshun Group (supplier), cumul = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p109 Trading partners count for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p110 Ports count associated with Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p111 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p112 Bottle size stated in cargo description: Chinkiang vinegar 550ML packed 24 per c = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p113 Bottles per case stated in cargo description (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p114 Container length dimension on bill of lading EGLV142252207486 (20-foot container = **240** container length (cm, as stated) (2022-08-13..2022-08-13) [keep: ] quote: "Length 240 \| Height 102 \|"
  - p115 Container height dimension on bill of lading EGLV142252207486 = **102** container height (cm, as stated) (2022-08-13..2022-08-13) [keep: ] quote: "Length 240 \| Height 102 \|"
  - p116 Container width dimension on bill of lading EGLV142252207486 = **96** container width (cm, as stated) (2022-08-13..2022-08-13) [keep: ] quote: "Width 96 \| Load Status Loaded"
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar', 'china vinegar exports', 'us vinegar imports']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p2', 'p3', 'p4'] All three come from the same annual-report segment table row for 外贸模式 (foreign-trade mode) 2025: revenue, YoY change, and gross margin. They are one underlying measurement, not independent confirmatio
- corroborating: ['p5', 'p6', 'p7'] Same 醋系列 segment table: production, sales volume, and revenue. Internally consistent (sales slightly below production, implied ~5.8 CNY/kg revenue). Shared source, so agreement is not independent.
- corroborating: ['p1', 'p8'] Total operating revenue and condiment revenue are near-equal, implying condiments are almost all of Hengshun's revenue; consistent with the company being a condiment pure-play. Same report.
- redundant: ['p26', 'p60'] Identical ImportGenius 'Total Shipments 44' figure for Jiangsu Hengshun Group, 2006-11 to 2022-08. Same measurement, duplicated across d3 and d6.
- redundant: ['p27', 'p61'] Identical '6 trading partners' figure, same ImportGenius snapshot.
- redundant: ['p28', 'p62'] Identical '5 ports' figure, same ImportGenius snapshot.
- redundant: ['p29', 'p63'] Identical piece count 700 on the same bill of lading EGLV142252207486.
- corroborating: ['p30', 'p31', 'p65', 'p64'] Same bill-of-lading cargo description '550ML@24' parsed into bottle size and bottles-per-case; one underlying document.
- redundant: ['p32', 'p33', 'p34', 'p66', 'p67', 'p68'] Same container dimensions (240x102x96 cm) from the same bill of lading, duplicated across d3 and d6.
- corroborating: ['p12', 'p13', 'p14', 'p15'] Customs HS 22090000 aggregates: US quantity/value and US share of worldwide quantity are internally consistent (6.60M/58.12M ≈ 11.35%). One source (m.x315.cn), 2020-2022 cumulative, not annual and not
- corroborating: ['p38', 'p39', 'p40', 'p43', 'p45', 'p47'] Multiple 500 ml SKUs from the same distributor catalog page; establishes 500 ml as the modal retail bottle size for Hengshun exports.
- corroborating: ['p41', 'p42', 'p50', 'p51'] 580 ml aged-vinegar SKUs, consistent across two catalog snapshots (fivecontinentsintl and emmefoods).
- corroborating: ['p48', 'p52'] 300 ml eight-year SKU appears in both catalogs; consistent.
- corroborating: ['p46', 'p53'] 550 ml SKU (steamed-bun vinegar / K-type) consistent with the 550 ml bill-of-lading SKU.
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58'] Retail prices from a single 2007-era catalog snapshot; internally consistent price ladder by age/size but badly stale for 2025.
- conflicting: ['p2', 'p12'] Not a true contradiction but a scope mismatch: p2 is Hengshun's total foreign-trade revenue (~39M CNY, all destinations, all products), while p12 is all-China vinegar exports to the US. Hengshun's US 
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p69'] Both report Hengshun 2025 total operating revenue ~CNY 2.287bn; p69 is a rounded restatement of p1, same underlying annual report.
- corroborating: ['p2', 'p70'] Both give 2025 foreign-trade revenue ~CNY 39.17m (p70 rounds to 0.39亿); same annual-report disclosure.
- corroborating: ['p3', 'p71'] Both give -17.95% YoY change in foreign-trade revenue; identical source figure.
- corroborating: ['p2', 'p3', 'p4'] Same revenue table row: level, YoY change, and gross margin are internally consistent components of one disclosure.
- corroborating: ['p5', 'p6'] Vinegar production 235,643 t vs sales 228,113 t; sales slightly below production is plausible inventory build, not a conflict.
- corroborating: ['p7', 'p5'] Vinegar revenue CNY 1.321bn over 228,113 t implies ~CNY 5.8k/t, a plausible bulk/retail blended price; consistent scale.
- corroborating: ['p12', 'p95'] Identical 2020-2022 cumulative US-bound HS22090000 quantity (6,597,078 L); duplicate of same source.
- corroborating: ['p13', 'p96'] Identical 2020-2022 cumulative US-bound value (USD 8,459,027); duplicate.
- corroborating: ['p14', 'p97'] Identical 11.35% US share of quantity; duplicate.
- corroborating: ['p15', 'p94'] Identical 58,119,878 L total 2020-2022 exports; duplicate.
- corroborating: ['p12', 'p13'] US quantity and value imply ~USD 1.28/L, a plausible export unit value for bottled vinegar; internally consistent.
- corroborating: ['p79', 'p80', 'p81'] 2025 US-bound HS22090000 value USD 3.787m vs 2024 USD 4.992m, -24.14%; internally consistent annual series.
- corroborating: ['p82', 'p83', 'p84', 'p85'] Total HS22090000 exports 2025 USD 27.89m vs 2024 USD 29.68m, -6.02%; p85 is the same figure in 万美元.
- corroborating: ['p79', 'p82'] US share of China vinegar export value 2025 = 3.787/27.89 ≈ 13.6%, close to the 2020-2022 quantity share of 11.35%; consistent order of magnitude.
- corroborating: ['p26', 'p108'] Identical ImportGenius 44-shipment cumulative count for Hengshun; duplicate.
- corroborating: ['p27', 'p109'] Identical 6 trading partners; duplicate.
- corroborating: ['p28', 'p110'] Identical 5 ports; duplicate.
- corroborating: ['p29', 'p111'] Identical 700 piece count on same bill of lading; duplicate.
- corroborating: ['p30', 'p112'] Identical 550 ml bottle size; duplicate.
- corroborating: ['p31', 'p113'] Identical 24 bottles/case; duplicate.
- corroborating: ['p32', 'p114'] Identical 240 cm container length; duplicate.
- corroborating: ['p33', 'p115'] Identical 102 cm container height; duplicate.
- corroborating: ['p34', 'p116'] Identical 96 cm container width; duplicate.
- corroborating: ['p26', 'p29'] 44 shipments over 2006-2022 with a 700-piece (16,800-bottle) sample shipment implies low annual US volume; consistent with a small US channel.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p43', 'p45', 'p47'] Multiple Hengshun export SKUs at 500 ml; supports 500 ml as the modal bottle size.
- corroborating: ['p41', 'p42', 'p50', 'p51'] 580 ml aged-vinegar SKUs corroborate a secondary bottle size cluster.
- corroborating: ['p46', 'p53'] 550 ml SKUs corroborate the bill-of-lading 550 ml bottle size.
- corroborating: ['p48', 'p52'] 300 ml premium aged SKUs corroborate a smaller-size cluster.
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58'] US retail prices for Hengshun SKUs; consistent with a low-price commodity retail product, useful only as context (2007 vintage).
- corroborating: ['p2', 'p79'] Hengshun foreign-trade revenue fell -17.95% while US-bound HS22090000 value fell -24.14% in 2025; same direction, consistent with a weak US export year.
- corroborating: ['p10', 'p2'] 85-country footprint with only CNY 39m foreign-trade revenue implies a very thin per-country average, so US is a small slice.
- corroborating: ['p11', 'p2'] USD receivables of only ~USD 344k at year-end is consistent with modest US/foreign-trade billing.
- contextual: ['p12', 'p79'] 2020-2022 cumulative US quantity and 2025 US value are different periods/units; used only to derive a unit-value bridge, not as a direct series.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Hengshun share of China HS22090000 vinegar exports to the US, by value, 2025 | 8 | 2..25 | 2..25 | % | m1 (m1) | Hengshun is China's largest vinegar brand but its total foreign-trade revenue (CNY 39m ≈ USD 5.5m) is small relative to China's total HS22090000 exports (USD 27.9m) and US-bound exports (USD 3.8m). A share of ~8% of US-bound value is plausible; wide range reflects that Hengshun may be a minority or  | Hengshun's US-bound vinegar is a subset of China's HS22090000 exports to the US and is priced comparably to the Chinese average. | Bill-of-lading or customs data showing Hengshun's US shipments are a much larger or much smaller fraction of total US-bound Chinese vinegar. |
| a2 | Average retail bottle size for Hengshun US-bound bottled vinegar | 0.52 | 0.35..0.75 | 0.35..0.75 | litres per bottle | m1 (m1) | Kept SKU evidence clusters at 500-580 ml (p38, p39, p41, p42, p46, p53) with some 300 ml premium (p48, p52); a volume-weighted average near 0.52 L is reasonable, with wide range for mix uncertainty. | US-bound Hengshun vinegar is predominantly retail bottled in the 300-580 ml range, not bulk. | Evidence that US shipments are dominated by bulk drums or by 3 L buckets. |
| a3 | Share of Hengshun foreign-trade revenue that is US-bound | 15 | 5..35 | 5..35 | % | unused | Hengshun sells to 85 countries (p10); the US is a major but not dominant overseas market. With CNY 39m total foreign-trade revenue, a 15% US share is a reasonable central value; wide range reflects absence of disclosed regional split. | Hengshun's foreign-trade revenue is spread across many countries with the US as one significant market. | Disclosure or bill-of-lading data showing the US is a much larger or much smaller share of Hengshun's exports. |
| a4 | Hengshun vinegar share of foreign-trade revenue | 70 | 50..90 | 47.43..94.87 (widened) | % | unused | Vinegar is Hengshun's core product (CNY 1.32bn of CNY 2.29bn total revenue, p7/p1); foreign-trade revenue is likely mostly vinegar but may include sauces and cooking wine. | Foreign-trade revenue is predominantly vinegar rather than other condiments. | Disclosure that foreign-trade revenue is mostly non-vinegar condiments. |
| a5 | Hengshun export FOB price per litre of bottled vinegar | 1.3 | 0.8..2.2 | 0.8..2.2 | USD per litre | m1 (m1) | China HS22090000 US-bound unit value from p13/p12 is ~USD 1.28/L; Hengshun branded product may command a premium, so a central ~1.3 USD/L with wide range is reasonable. | Hengshun's US-bound export price per litre is comparable to the Chinese HS22090000 average to the US. | Evidence of much higher or lower Hengshun FOB pricing. |
| a6 | CNY per USD exchange rate, 2025 average | 7.1 | 6.8..7.4 | 5.016..10.03 (widened) | CNY per USD | unused | 2025 CNY/USD traded in a narrow band around 7.1; used to convert Hengshun's CNY foreign-trade revenue into USD before dividing by the USD/L price. | Converting Hengshun's CNY-denominated foreign-trade revenue to USD for the price division. | A materially different 2025 average CNY/USD rate. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 398,545 | ['p79'] / ['a1', 'a2', 'a5'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a | ['p2'] / ['a2', 'a3', 'a4', 'a5', 'a6'] | [] |  | 0.00 |  | formula_mc uses 5 assumptions (at most 3) |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **398,545** bottle, 80% interval [97,522, 1,628,741] bottle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 8 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 3 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p1 | Jiangsu Hengshun Vinegar-Industry total operating revenue 2025 | 2,286,538,594 | CNY | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Total operating revenue in CNY, not bottles of vinegar sold to the US; wrong measure and scope. |
| p2 | Hengshun foreign trade (外贸模式) revenue 2025 | 39,171,647 | CNY | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Foreign trade revenue in CNY for all export markets, not US-specific bottle count; wrong measure, unit, and scope. |
| p5 | Hengshun vinegar (醋系列) sales volume 2025 | 228,113 | tonnes | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Vinegar sales volume in tonnes globally, not bottles sold to the US; wrong unit and scope. |
| p6 | Hengshun vinegar (醋系列) production volume 2025 | 235,643 | tonnes | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Production volume in tonnes, not US bottle sales; wrong measure, unit, and scope. |
| p7 | Hengshun vinegar (醋系列) revenue 2025 | 1,321,092,496 | CNY | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Vinegar revenue in CNY globally, not US bottle count; wrong measure, unit, and scope. |
| p10 | Hengshun products sold to countries/regions (breadth of export footprint) | 85 | countries and regions | 2025-01-01..2025-12-31 | vip.stock.finance.sina.com.cn | different | Count of countries/regions, not bottles sold to the US; wrong measure and unit. |
| p69 | Hengshun 2025 total operating revenue | 2,287,000,000 | CNY yuan | 2025-01-01..2025-12-31 | stock.finance.sina.com.cn | different | Total operating revenue in CNY, not US bottle sales; wrong measure and scope. |
| p70 | Hengshun 2025 foreign trade (外贸) revenue | 39,000,000 | CNY yuan | 2025-01-01..2025-12-31 | stock.finance.sina.com.cn | different | Foreign trade revenue in CNY for all exports, not US-specific bottle count; wrong measure, unit, and scope. |


## Final answer

Best estimate: 398,545 bottle of Hengshun bottled vinegar sold into the United States in calendar 2025 (all bottled vinegar types), with an 80% model-based interval of 97,522 to 1,628,741 bottle.

The estimate comes from one method (100% weight): US-bound Chinese vinegar export value 3,787,074 USD divided by an assumed FOB price of 1.3 USD/litre (range 0.8–2.2), scaled by Hengshun's assumed value share 8% (range 2%–25%), then divided by assumed bottle size 0.52 litres (range 0.35–0.75).

Only the customs export value is observed; the share, price and bottle size are analyst assumptions, so the result is conditional on them. The alternative bottom-up route using Hengshun's foreign-trade revenue 39,171,647 CNY was not used (0% weight).

The biggest risk is that 8% is a guess: if Hengshun's US-bound share is far from it, the estimate moves proportionally. Better evidence would be Hengshun's disclosed US export volumes or SKU-level shipment data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Hengshun share of China HS[n] vinegar exports to the US, by value, 2025: 8%, range 2% to 25%; used by m1. Overturned by: Bill-of-lading or customs data showing Hengshun's US shipments are a much larger or much smaller fraction of total US-bound Chinese vinegar.
- a2 Average retail bottle size for Hengshun US-bound bottled vinegar: 0.52 litres per bottle, range 0.35 to 0.75; used by m1. Overturned by: Evidence that US shipments are dominated by bulk drums or by [n] L buckets.
- a5 Hengshun export FOB price per litre of bottled vinegar: 1.3 USD per litre, range 0.8 to 2.2; used by m1. Overturned by: Evidence of much higher or lower Hengshun FOB pricing.

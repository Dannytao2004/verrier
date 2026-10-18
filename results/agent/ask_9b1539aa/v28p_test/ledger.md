# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun Group (镇江恒顺集团 / Jiangsu Hengshun Vinegar-Industry Co., Ltd.) vinegar sold/exported to the United States in a full year, all bottle types and vinegar varieties combined | unit bottle | period 2024-01-01..2024-12-31 | publisher None official; would be derived from Hengshun annual report export disclosures, Chinese customs export statistics, or US import records

## Directions and pages

### d1 [own_history] Hengshun corporate reporting / investor relations

Hypothesis: Hengshun's annual report discloses total revenue, export/overseas revenue, and possibly export volume or tonnage; US share of exports can be bounded. Bottle count = (US export revenue) / (average revenue per bottle), or (US export tonnage) / (average bottle fill volume).

Queries issued by the searcher: 恒顺醋业 年报 2024 境外 收入 出口; Hengshun Vinegar annual report 2024 overseas export revenue; 恒顺醋业 2024年年度与行业相关的定期经营数据公告 外贸模式 醋 销售收入 万元; 恒顺 出口 美国 销量 吨 镇江香醋 出口

- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 14/14
  - p1 Hengshun foreign trade (export) mode sales revenue, 2024 = **47,741,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p2 Hengshun foreign trade (export) mode sales revenue, 2023 = **45,133,900** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p3 Hengshun foreign trade mode revenue year-on-year change, 2024 vs 2023 = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p4 Hengshun vinegar series (醋系列) sales revenue, 2024 = **1,265,596,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p5 Hengshun vinegar series (醋系列) sales revenue, 2023 = **1,294,067,600** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p6 Hengshun total sales revenue by product category, 2024 = **1,774,174,300** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p7 Hengshun total sales revenue by product category, 2023 = **1,816,930,700** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p8 Hengshun total sales revenue by sales mode, 2024 = **2,093,006,800** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p9 Hengshun total sales revenue by sales mode, 2023 = **2,077,821,800** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [keep: ] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p10 Hengshun dealer (经销) mode sales revenue, 2024 = **1,941,448,600** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 经销模式 \| 194,144.86 \| 193,196.45 \| 0.49 \|"
  - p11 Hengshun direct sales (直销) mode sales revenue, 2024 = **103,817,200** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 直销模式 \| 10,381.72 \| 10,072.35 \| 3.07 \|"
  - p12 Hengshun online sales revenue, 2024 = **274,378,100** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 线上销售 \| 27,437.81 \| 26,471.68 \| 3.65 \|"
  - p13 Hengshun offline sales revenue, 2024 = **1,818,628,700** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [keep: ] quote: "\| 线下销售 \| 181,862.87 \| 181,310.50 \| 0.30 \|"
  - p14 Hengshun total dealer count at end of 2024 = **2,014** 个 (dealers) (2024-12-31..2024-12-31) [keep: ] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://stockanalysis.com/quote/sha/600305/financials/metrics/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0

### d2 [related_series] Chinese customs / trade statistics

Hypothesis: China customs export data by HS code (vinegar HS 2209) and destination US gives total Chinese vinegar exports to the US in value and quantity (kg/liters); Hengshun's share of China's vinegar exports (or of Zhenjiang-origin exports) times that total gives Hengshun US volume, then divide by average bottle volume.

Queries issued by the searcher: 中国 醋 出口 美国 HS 2209 数量 吨; China vinegar exports United States HS 2209 quantity tonnes; 镇江 香醋 出口 美国 吨 2024; 恒顺醋业 年报 2024 境外 收入 出口

- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p15 China HS22090000 vinegar exports to United States, quantity (2020-01 to 2022-12  = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p16 China HS22090000 vinegar exports to United States, value in USD (2020-01 to 2022 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p17 United States share of China HS22090000 vinegar export quantity (2020-01 to 2022 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p18 China HS22090000 vinegar exports to all countries, total quantity (2020-01 to 20 = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p19 Number of destination countries for China HS22090000 vinegar exports (2020-01 to = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p20 China HS22090000 vinegar exports to Hong Kong, quantity (2020-01 to 2022-12 cumu = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p21 China HS22090000 vinegar exports to Hong Kong, value in USD (2020-01 to 2022-12  = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p22 Hong Kong share of China HS22090000 vinegar export quantity (2020-01 to 2022-12  = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p23 China HS22090000 vinegar exports to Singapore, quantity (2020-01 to 2022-12 cumu = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p24 China HS22090000 vinegar exports to Australia, quantity (2020-01 to 2022-12 cumu = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p25 China HS22090000 vinegar exports to Netherlands, quantity (2020-01 to 2022-12 cu = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p26 China HS22090000 vinegar exports to Malaysia, quantity (2020-01 to 2022-12 cumul = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p27 China HS22090000 vinegar exports to Canada, quantity (2020-01 to 2022-12 cumulat = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p28 China HS22090000 vinegar exports to Japan, quantity (2020-01 to 2022-12 cumulati = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_XKUV.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://english.cnipa.gov.cn/attach/0/8d58d6b60eae471bbf85880b662843e3.pdf` -> **live_dated** (page date 2020-07-08); points raw/verified 3/0
- dropped by code checks: 4 (value_as_written not in quote as a whole number: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d3 [related_series] US import records / trade data

Hypothesis: US Census/ITC import data for HS 2209 from China, combined with Hengshun's estimated share of Chinese vinegar imports into the US, yields US-bound Hengshun volume; convert to bottles via typical retail bottle size (e.g., 500 mL).

Queries issued by the searcher: US imports vinegar HS 2209 from China quantity kg 2024 USITC DataWeb; Hengshun vinegar bill of lading importer USA Chinkiang; "2209" vinegar US imports from China 2024 kilograms census data; 恒顺醋业 年报 2024 境外 营业收入 出口

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p29 Total US customs shipments recorded for Jiangsu Hengshun Group (supplier), cumul = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p30 Number of trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p31 Number of ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p32 Bill of lading piece count for Chinkiang vinegar 550ML@24 shipment (EGLV14225220 = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p33 Bottle size stated in cargo description for Chinkiang vinegar (550ML@24) = **550** mL per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p34 Bottles per case implied by packing notation 550ML@24 in cargo description = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p35 Container length in inches for shipment EGLV142252207486 = **240** inches (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p36 Container height in inches for shipment EGLV142252207486 = **102** inches (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p37 Container width in inches for shipment EGLV142252207486 = **96** inches (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"

### d4 [base_rates] Industry association / export conversion factors

Hypothesis: Zhenjiang vinegar industry association or local government reports total Zhenjiang vinegar exports (tonnage/value) and Hengshun's share; combined with average bottle fill (e.g., 500 mL, density ~1.05 kg/L) converts tonnage to bottles. US share of Zhenjiang exports estimated from destination breakdown.

Queries issued by the searcher: 镇江香醋 出口 统计 美国 吨; Zhenjiang vinegar export volume destination countries tonnes; 镇江香醋 出口 2024 吨 镇江海关 监管出口香醋; 恒顺醋业 出口 占比 境外 收入 年报 2024 国外

- `https://english.cnipa.gov.cn/attach/0/8d58d6b60eae471bbf85880b662843e3.pdf` -> **live_dated** (page date 2020-07-08); points raw/verified 2/1
  - p38 Annual Zhenjiang vinegar exports by local enterprises to the international marke = **2,800** tons (..) [keep: ] quote: "The local enterprises export more than 2800 tons of Zhenjiang vinegar to the international market every year."
- `http://www.ourjiangsu.com/a/20221101/1667308877263.shtml` -> **live_dated** (page date 2022-11-01); points raw/verified 5/3
  - p39 Bottle fill volume of 550ml Zhenjiang aromatic vinegar bottles in a shipment to  = **550** millilitres per bottle (..) [keep: ] quote: "为即将出口到的日本的24瓶550ml装镇江香醋办理了RCEP原产地证"
  - p40 Number of bottles in the shipment of 550ml Zhenjiang aromatic vinegar to Japan = **24** bottles (..) [keep: ] quote: "为即将出口到的日本的24瓶550ml装镇江香醋办理了RCEP原产地证"
  - p41 Number of countries and regions to which Zhenjiang aromatic vinegar is exported = **64** countries and regions (..) [keep: ] quote: "也是中国国家地理标志产品,远销海外64个国家和地区"
- `http://jsnews.jschina.com.cn/zq/focus/201905/t20190523_2314543.shtml` -> **live_dated** (page date 2019-05-23); points raw/verified 4/1
  - p42 Zhenjiang vinegar export volume, 2018 = **6,186** tonnes (2018-01-01..2018-12-31) [keep: ] quote: "2018年,镇江香醋产业链实现主营业务收入29.81亿元,出口6186吨,达829.7万美元"
- `https://max.book118.com/try_down/558011103137006073.pdf` -> **live_dated** (page date 2024-11-16); points raw/verified 15/14
  - p43 Zhenjiang vinegar export volume, 2015 (table 1, unit written as 顿/tonnes) = **280** tonnes (2015-01-01..2015-12-31) [DISCARD: Discarded earlier; unit '顿' ambiguous and series conflicts with p42/p38.] quote: "2015 280 25"
  - p44 Zhenjiang vinegar export volume, 2016 (table 1) = **400** tonnes (2016-01-01..2016-12-31) [DISCARD: Same discarded ambiguous-unit series.] quote: "2016 400 43 36 44"
  - p45 Zhenjiang vinegar export volume, 2017 (table 1) = **600** tonnes (2017-01-01..2017-12-31) [DISCARD: Same discarded ambiguous-unit series.] quote: "2017 600 50 55 43"
  - p46 Zhenjiang vinegar export volume, 2018 (table 1) = **727** tonnes (2018-01-01..2018-12-31) [DISCARD: Same discarded ambiguous-unit series.] quote: "2018 727 21 66.7 21"
  - p47 Zhenjiang vinegar export volume, 2019 (table 1) = **622** tonnes (2019-01-01..2019-12-31) [DISCARD: Same discarded ambiguous-unit series.] quote: "2019 621.6 -15 58.6 -12"
  - p48 Zhenjiang vinegar export value, 2015 (table 1, 万美元) = **25** ten thousand USD (2015-01-01..2015-12-31) [DISCARD: Same discarded series.] quote: "2015 280 25"
  - p49 Zhenjiang vinegar export value, 2016 (table 1, 万美元) = **36** ten thousand USD (2016-01-01..2016-12-31) [DISCARD: Same discarded series.] quote: "2016 400 43 36 44"
  - p50 Zhenjiang vinegar export value, 2017 (table 1, 万美元) = **55** ten thousand USD (2017-01-01..2017-12-31) [DISCARD: Same discarded series.] quote: "2017 600 50 55 43"
  - p51 Zhenjiang vinegar export value, 2018 (table 1, 万美元) = **66.7** ten thousand USD (2018-01-01..2018-12-31) [DISCARD: Same discarded series.] quote: "2018 727 21 66.7 21"
  - p52 Zhenjiang vinegar export value, 2019 (table 1, 万美元) = **58.6** ten thousand USD (2019-01-01..2019-12-31) [DISCARD: Same discarded series.] quote: "2019 621.6 -15 58.6 -12"
  - p53 US share of Zhenjiang vinegar export market structure (figure 1, percent) = **31** % (..) [DISCARD: Figure-1 market-structure share of unclear base/period; not usable as a numeric input.] quote: "美国, 31"
  - p54 Canada share of Zhenjiang vinegar export market structure (figure 1, percent) = **15** % (..) [DISCARD: Same unclear figure.] quote: "加拿大, 15"
  - p55 Share of Zhenjiang vinegar exports going to remaining countries, percent = **12** % (..) [DISCARD: Same unclear figure.] quote: "其余十几个国家的总销售量和市场份额仅仅约为 12%"
  - p56 Number of countries Zhenjiang vinegar exported to annually (recent three years) = **13.5** (range 12..15) as written "12-15", value check pending countries (..) [DISCARD: Fractional country count from unclear figure.] quote: "近三年来镇江醋产品每年约出口至 12-15 个国家"
- dropped by code checks: 7 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period year 2024 does not appear in the page text or URL (likely mis-dated): 2; number: value_as_written is only part of a larger CJK number in the quote: 3)

### d5 [physical_flow] Container/shipment logistics

Hypothesis: Export shipments move in standard containers; number of containers of Hengshun vinegar to US per year times bottles per container (based on bottle size and pallet loading) gives bottle count. Container count can come from shipping/bill-of-lading data or company logistics disclosures.

Queries issued by the searcher: Hengshun vinegar container shipment USA bill of lading; Chinkiang vinegar 40ft container bottles export; 52wmb "jiangsu hengshun" 美国 提单 数量 出口; ImportYeti "Jiangsu Hengshun" shipments United States

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-group-zhenjiang-in` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/10
  - p57 Total US customs shipments recorded for Jiangsu Hengshun Group, 2006-11-01 to 20 = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p29.] quote: "Total Shipments 44"
  - p58 Trading partners count for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p30.] quote: "Trading Partners 6"
  - p59 Ports count for Jiangsu Hengshun Group in US customs records = **5** ports (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p31.] quote: "Ports 5"
  - p60 Piece count on bill of lading EGLV142252207486 (Chinkiang vinegar 550mL@24) = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p32.] quote: "Piece Count 700"
  - p61 Bottle size on bill of lading EGLV142252207486 (Chinkiang vinegar) = **550** mL per bottle (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p33.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p62 Bottles per case on bill of lading EGLV142252207486 (550mL@24) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p34.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p63 Container length on bill of lading EGLV142252207486 = **240** cm (container length) (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p35.] quote: "Length 240"
  - p64 Container height on bill of lading EGLV142252207486 = **102** cm (container height) (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p36.] quote: "Height 102"
  - p65 Container width on bill of lading EGLV142252207486 = **96** cm (container width) (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p37.] quote: "Width 96"
  - p66 Container type on bill of lading EGLV142252207486 (20 foot general purpose) = **20** feet (container type) (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p73.] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-

### d6 [capacity_consumption] US retail sell-through / distributor

Hypothesis: US retail sales of Hengshun/Chinkiang vinegar (e.g., in Asian supermarkets, Amazon) divided by average retail price per bottle gives bottles sold; this measures sell-through rather than export shipments but constrains magnitude. Can be built from store counts × velocity or e-commerce review/rank proxies.

Queries issued by the searcher: Hengshun vinegar Amazon best seller rank Chinkiang vinegar US; 镇江香醋 美国 超市 销量 恒顺; 恒顺醋业 2024年报 境外 收入 出口 占比; Hengshun vinegar import records US customs shipments Well Luck

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.sayweee.com/zh/product/Heng-Shun-Zhenjiang-Vinegar/64693` -> **live_dated** (page date 2026-10-18); points raw/verified 3/0
- `https://www.freshgogo.com/pc/goodsDescribe?id=10004&language=zh` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%90%84%E4%BA%9E%E6%B4%B2%E8%B6%85%E5%B8%82%E6%8E%A8%E5%87%BA%E6%81%86%E9%A0%86%E7%B3%BB%E5%88%97%E7%94%A2%E5%93%81%E9%BB%` -> **live_dated** (page date 2024-11-29); points raw/verified 0/0
- dropped by code checks: 3 (period_end missing or unparseable: 3)

### d7 [persona] US distributor / importer

Hypothesis: Hengshun's US importer/distributor (e.g., specialty Asian food importers) may disclose annual case volumes or purchase quantities; cases × bottles per case gives bottle count. Distributor interviews, trade press, or company profiles may reveal order sizes.

Queries issued by the searcher: Hengshun vinegar US distributor importer; Chinkiang vinegar distributor USA case bottles per case; 52wmb jiangsu hengshun international trad 供应商 美国 提单 2024; Well Luck Co Inc Hengshun vinegar importer cases annual volume

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/10
  - p67 Total US customs shipments recorded for Jiangsu Hengshun Group (2006-11-01 to 20 = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p29.] quote: "Total Shipments 44"
  - p68 Number of trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p30.] quote: "Trading Partners 6"
  - p69 Number of ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Redundant duplicate of p31.] quote: "Ports 5"
  - p70 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p32.] quote: "Piece Count 700"
  - p71 Bottle size in SKU description 'CHINKIANG VINEGAR 550ML@24' on bill of lading EG = **550** millilitres per bottle (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p33.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p72 Bottles per case implied by SKU notation '550ML@24' on bill of lading EGLV142252 = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p34.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p73 Container length (feet) for shipment on bill of lading EGLV142252207486 = **20** feet (container) (2022-08-13..2022-08-13) [keep: ] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
  - p74 Container internal length dimension on bill of lading EGLV142252207486 = **240** container length units (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p35.] quote: "Length 240 \| Height 102 \|"
  - p75 Container internal height dimension on bill of lading EGLV142252207486 = **102** container height units (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p36.] quote: "Length 240 \| Height 102 \|"
  - p76 Container internal width dimension on bill of lading EGLV142252207486 = **96** container width units (2022-08-13..2022-08-13) [DISCARD: Redundant duplicate of p37.] quote: "Width 96 \| Load Status Loaded \|"
- `https://fivecontinentsintl.com/en/product/hengshun-brand-zhenjiang-chinkiang-vinegar-3l/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d8 [shocks] Trade policy / tariff and demand shifts

Hypothesis: US-China tariffs, shipping costs, and post-2020 demand changes affect Hengshun's US export volume; identifying direction and magnitude of recent changes helps adjust a base-year estimate to 2024. Also COVID-era stockpiling and subsequent normalization.

Queries issued by the searcher: US tariff Chinese vinegar HS 2209 Section 301 rate; 恒顺醋业 出口 美国 关税 影响 年报 海外收入; 恒顺醋业 2024年度 与行业相关的定期经营数据公告 外贸模式 销售收入 2023年度 同比; Hengshun vinegar US imports distributor "Hengshun" vinegar United States market share Chinese vinegar exports America

- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918924` -> **live_dated** (page date 2025-04-22); points raw/verified 15/15
  - p77 Hengshun vinegar series (醋系列) sales revenue, 2024 = **126,560** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p4.] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p78 Hengshun vinegar series (醋系列) sales revenue, 2023 = **129,407** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p5.] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p79 Hengshun vinegar series (醋系列) year-on-year revenue change, 2024 vs 2023 = **-2.2** % (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p5/p4 change.] quote: "\| 醋系列 \| 126,559.63 \| 129,406.76 \| -2.20 \|"
  - p80 Hengshun foreign trade (外贸模式) sales revenue, 2024 = **4,774** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p1.] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p81 Hengshun foreign trade (外贸模式) sales revenue, 2023 = **4,513** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p2.] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p82 Hengshun foreign trade (外贸模式) year-on-year revenue change, 2024 vs 2023 = **5.78** % (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p3.] quote: "\| 外贸模式 \| 4,774.13 \| 4,513.39 \| 5.78 \|"
  - p83 Hengshun total sales revenue (all products), 2024 = **209,301** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p8.] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p84 Hengshun total sales revenue (all products), 2023 = **207,782** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p9.] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p85 Hengshun total sales revenue year-on-year change, 2024 vs 2023 = **0.73** % (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p8/p9 change.] quote: "\| 合计 \| 209,300.68 \| 207,782.18 \| 0.73 \|"
  - p86 Hengshun product-category total revenue (醋+酒+酱), 2024 = **177,417** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p6.] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p87 Hengshun product-category total revenue (醋+酒+酱), 2023 = **181,693** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p7.] quote: "\| 合计 \| 177,417.43 \| 181,693.07 \| -2.35 \|"
  - p88 Hengshun online sales revenue, 2024 = **27,438** 万元 (10,000 CNY) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p12.] quote: "\| 线上销售 \| 27,437.81 \| 26,471.68 \| 3.65 \|"
  - p89 Hengshun online sales revenue, 2023 = **26,472** 万元 (10,000 CNY) (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p12/p13 context.] quote: "\| 线上销售 \| 27,437.81 \| 26,471.68 \| 3.65 \|"
  - p90 Hengshun distributor (经销商) count, total at end of 2024 = **2,014** 个 (distributors) (2024-12-31..2024-12-31) [DISCARD: Redundant duplicate of p14.] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
  - p91 Hengshun distributors added during 2024, total = **272** 个 (distributors) (2024-01-01..2024-12-31) [DISCARD: Redundant duplicate of p14.] quote: "\| 合计 \| 2014 \| 272 \| 302 \|"
- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 15/0
- `https://www.htshub.com/us-hs/detail/22090000` -> **live_dated** (page date 2026-10-09); points raw/verified 4/3
  - p92 US HTS general rate of duty on vinegar and substitutes for vinegar obtained from = **0.5** cents per proof liter (2026-10-09..2026-10-09) [DISCARD: MFN duty rate, superseded by p94 for the 2024 tariff context; not a quantity input.] quote: "\| Rates of Duty (1-General) \| 0.5¢/pf.liter \|"
  - p93 US HTS column 2 rate of duty on vinegar (HS 2209.00.00) for Cuba and North Korea = **2.1** cents per proof liter (2026-10-09..2026-10-09) [DISCARD: Column-2 rate for Cuba/North Korea, irrelevant to China-US trade.] quote: "\| Rates of Duty (2-Cuba and North Korea) \| 2.1¢/pf.liter \|"
  - p94 Additional duty on vinegar (HS 2209.00.00) products of China: applicable subhead = **25** % (2026-10-09..2026-10-09) [keep: ] quote: "\| Additional Duty(products of China) \| The duty provided in the applicable subheading + 25% \|"
- `https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2024-04-30/600305_20240430_ANJE.pdf` -> **live_dated** (page date 2024-04-30); points raw/verified 0/0
- dropped by code checks: 16 (value_as_written not in quote as a whole number: 15; number: no number in value_as_written: 1)

### b1 [own_history] Hengshun annual report / investor relations

Hypothesis: Hengshun's annual report may disclose overseas/export revenue split by region or by product, or export volume in tonnes. If a US or North America regional breakdown exists, it directly converts p1's 外贸模式 revenue into a US-specific revenue, unlocking a revenue-per-bottle route (m1) without a share assumption.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外 收入 分地区; 江苏恒顺醋业 2024年年度报告 主营业务分地区 境外 营业收入; 恒顺醋业 2024 年报 国外 营业收入 36,910,481.37 分地区 境外; 镇江香醋 出口 美国 数量 吨 2024 海关

- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://stock.qianzhan.com/hs/zhuyingdiqu_600305.SH.html` -> **live_dated** (page date 2026-10-18); points raw/verified 0/0

### b2 [related_series] China customs / UN Comtrade

Hypothesis: Annual (not 3-year cumulative) China HS22090000 exports to the US for 2023-2024, plus a Zhenjiang/Hengshun share of that flow, would replace the stale 2020-2022 cumulative p15 with a target-year figure. This is the missing input for the customs-based route (m2).

Queries issued by the searcher: 中国 海关 HS22090000 出口 美国 2024 数量 金额 醋; UN Comtrade 2209 China exports USA 2024 vinegar quantity; 恒顺醋业 2024年年报 境外 出口 营业收入 美国; 镇江 香醋 出口 2024 吨 美国 海关 镇江海关

- `https://www.jcksj.com/report/22090000.html` -> **live_dated** (page date 2026-09-08); points raw/verified 15/15
  - p95 China HS22090000 exports to the United States, value, calendar 2024 = **4,992,092** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p96 China HS22090000 exports to the United States, value, calendar 2025 = **3,787,074** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p97 China HS22090000 exports to the United States, year-on-year change, 2025 vs 2024 = **-24.14** % (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 3,787,074 \| 4,992,092 \| -1,205,018 \| -24.14% \| 查询该市场买家 ↗ \|"
  - p98 China HS22090000 total exports, value, calendar 2024 = **29,676,894** USD (2024-01-01..2024-12-31) [keep: ] quote: "2024 29,676,894 美元29676894"
  - p99 China HS22090000 total exports, value, calendar 2025 = **27,891,245** USD (2025-01-01..2025-12-31) [keep: ] quote: "2025 27,891,245 美元27891245"
  - p100 China HS22090000 total exports, year-on-year change, 2025 vs 2024 = **-6.02** % (2025-01-01..2025-12-31) [keep: ] quote: "较2024年-6.02%"
  - p101 China HS22090000 total imports, value, calendar 2024 = **9,806,210** USD (2024-01-01..2024-12-31) [keep: ] quote: "2024 9,806,210 美元9806210"
  - p102 China HS22090000 total imports, value, calendar 2025 = **11,979,467** USD (2025-01-01..2025-12-31) [keep: ] quote: "2025 11,979,467 美元11979467"
  - p103 China HS22090000 imports from the United States, value, calendar 2024 = **2,269,319** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p104 China HS22090000 imports from the United States, value, calendar 2025 = **1,875,118** USD (2025-01-01..2025-12-31) [keep: ] quote: "\| 美国 \| 1,875,118 \| 2,269,319 \| -394,201 \| -17.37% \| 查询该市场供应商 ↗ \|"
  - p105 China HS22090000 exports to Hong Kong, value, calendar 2024 = **4,093,608** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 中国香港 \| 4,205,407 \| 4,093,608 \| +111,799 \| +2.73% \| 查询该市场买家 ↗ \|"
  - p106 China HS22090000 exports to Australia, value, calendar 2024 = **1,959,491** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 澳大利亚 \| 2,079,038 \| 1,959,491 \| +119,547 \| +6.10% \| 查询该市场买家 ↗ \|"
  - p107 China HS22090000 exports to Netherlands, value, calendar 2024 = **2,398,669** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 荷兰 \| 2,153,886 \| 2,398,669 \| -244,783 \| -10.20% \| 查询该市场买家 ↗ \|"
  - p108 China HS22090000 exports to Singapore, value, calendar 2024 = **1,493,383** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 新加坡 \| 1,654,888 \| 1,493,383 \| +161,505 \| +10.81% \| 查询该市场买家 ↗ \|"
  - p109 China HS22090000 exports to Malaysia, value, calendar 2024 = **1,320,323** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 马来西亚 \| 1,634,565 \| 1,320,323 \| +314,242 \| +23.80% \| 查询该市场买家 ↗ \|"
- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 15/15
  - p110 China HS22090000 vinegar exports total quantity, calendar 2024 (all destinations = **25,760,168** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p111 China HS22090000 vinegar exports total value, calendar 2024 (all destinations) = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p112 China HS22090000 vinegar export average price per liter, calendar 2024 (all dest = **1.15** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p113 China HS22090000 vinegar exports total quantity, calendar 2023 (all destinations = **21,832,831** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p114 China HS22090000 vinegar exports total value, calendar 2023 (all destinations) = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p115 China HS22090000 vinegar export average price per liter, calendar 2023 (all dest = **1.18** USD per liter (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p116 China HS22090000 vinegar imports total quantity, calendar 2024 (all origins) = **6,382,197** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p117 China HS22090000 vinegar imports total value, calendar 2024 (all origins) = **11,585,503** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p118 China HS22090000 vinegar imports total quantity, calendar 2023 (all origins) = **6,345,028** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 6345028 \| $9213638 \| $1.45 \| 导出 \|"
  - p119 China HS22090000 vinegar imports total value, calendar 2023 (all origins) = **9,213,638** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 6345028 \| $9213638 \| $1.45 \| 导出 \|"
  - p120 China HS22090000 vinegar exports total quantity, calendar 2022 (all destinations = **19,604,254** liters (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p121 China HS22090000 vinegar exports total value, calendar 2022 (all destinations) = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p122 China HS22090000 vinegar exports total quantity, calendar 2021 (all destinations = **20,249,374** liters (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p123 China HS22090000 vinegar exports total value, calendar 2021 (all destinations) = **25,590,784** USD (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p124 China HS22090000 vinegar exports total quantity, calendar 2020 (all destinations = **17,414,624** liters (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p125 China HS22090000 vinegar exports to the US, quantity, cumulative 2020-01 to 2022 = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p126 China HS22090000 vinegar exports to the US, value, cumulative 2020-01 to 2022-12 = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p127 US share of China HS22090000 export quantity, cumulative 2020-01 to 2022-12 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p128 China HS22090000 total vinegar exports, quantity, cumulative 2020-01 to 2022-12 = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p129 Number of destination countries for China HS22090000 vinegar exports, cumulative = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p130 China HS22090000 vinegar exports to Hong Kong, quantity, cumulative 2020-01 to 2 = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p131 China HS22090000 vinegar exports to Hong Kong, value, cumulative 2020-01 to 2022 = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "出口中国香港金额最高,总计15,656,412美元"
  - p132 Hong Kong share of China HS22090000 export quantity, cumulative 2020-01 to 2022- = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p133 China HS22090000 vinegar exports to Singapore, quantity, cumulative 2020-01 to 2 = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p134 China HS22090000 vinegar exports to Australia, quantity, cumulative 2020-01 to 2 = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p135 China HS22090000 vinegar exports to Netherlands, quantity, cumulative 2020-01 to = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p136 China HS22090000 vinegar exports to Malaysia, quantity, cumulative 2020-01 to 20 = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p137 China HS22090000 vinegar exports to Canada, quantity, cumulative 2020-01 to 2022 = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p138 China HS22090000 vinegar exports to Japan, quantity, cumulative 2020-01 to 2022- = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b3 [persona] US importer / distributor

Hypothesis: A US importer of Hengshun/Chinkiang vinegar (e.g., Asian Taste, Wing Yip, or a specialty grocer) may disclose annual case volumes or container counts. Container count × bottles per container (from p32/p33/p34) would give a direct physical-flow estimate, resolving the largest uncertainty in the container route (m3).

Queries issued by the searcher: Hengshun vinegar US importer annual volume cases; Chinkiang vinegar container imports USA distributor annual cases; importyeti "Well Luck" Zhenjiang vinegar supplier shipments; panjiva "Jiangsu Hengshun" supplier shipments vinegar United States buyer

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 8/7
  - p139 Total US customs shipments recorded for Jiangsu Hengshun Group (supplier), all p = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p140 Trading partners recorded for Jiangsu Hengshun Group (supplier), all products = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p141 Ports recorded for Jiangsu Hengshun Group (supplier) shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p142 Bottle size and pack configuration stated for Asian Taste Brand Chinkiang Vinega = **550** as written "550ML@24", value check pending mL per bottle, 24 bottles per unit (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p143 Container length (cm) on bill of lading EGLV142252207486, 20-foot general purpos = **240** cm (2022-08-13..2022-08-13) [keep: ] quote: "Length 240 \| Height 102 \|"
  - p144 Container height (cm) on bill of lading EGLV142252207486, 20-foot general purpos = **102** cm (2022-08-13..2022-08-13) [keep: ] quote: "Length 240 \| Height 102 \|"
  - p145 Container width (cm) on bill of lading EGLV142252207486, 20-foot general purpose = **96** cm (2022-08-13..2022-08-13) [keep: ] quote: "Width 96 \| Load Status Loaded \|"
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar export', 'china vinegar us imports', 'zhenjiang vinegar sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p80', 'p81', 'p82'] Same Hengshun 外贸模式 revenue series (2024, 2023, YoY); p80-p82 are rounded duplicates of p1-p3. One underlying disclosure, not independent confirmation.
- corroborating: ['p4', 'p5', 'p77', 'p78', 'p79'] Same 醋系列 revenue series; p77-p79 rounded duplicates of p4/p5. Shows vinegar is ~71% of product-category revenue but gives no export split.
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p83', 'p84', 'p85', 'p86', 'p87'] Total revenue by product category and by sales mode; p83-p87 rounded duplicates. Note p8 (209,301万元) exceeds p6 (177,417万元) because sales-mode total includes non-vinegar/liquor/sauce products — differ
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p88', 'p89'] Dealer/direct/online/offline splits; p88-p89 duplicate p12. Domestic channel structure, not export.
- corroborating: ['p14', 'p90', 'p91'] Dealer counts; p90-p91 duplicate p14. Domestic distribution, weak relevance to US exports.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28'] One Chinese customs HS22090000 dataset (2020-2022 cumulative) by destination; internally consistent (US 11.35% of 58.1M L). Single source, single period — not independent of each other.
- corroborating: ['p29', 'p30', 'p31', 'p57', 'p58', 'p59', 'p67', 'p68', 'p69'] Same ImportGenius supplier profile (44 shipments, 6 partners, 5 ports, 2006-2022); p57-p59 and p67-p69 are duplicates of p29-p31. One underlying customs-record extract.
- corroborating: ['p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76'] All describe the same single bill of lading EGLV142252207486 (550mL@24, 700 pieces, 20ft container). Duplicates across d3/d5/d7. One shipment — a conversion factor, not a volume estimate.
- conflicting: ['p38', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56'] Zhenjiang export tonnage figures disagree by an order of magnitude: p38 says >2,800 t/yr (all destinations), p42 says 6,186 t in 2018, while p43-p47 table says 280-727 t. Different definitions/periods
- corroborating: ['p39', 'p40', 'p41'] Zhenjiang vinegar export context: 550mL×24 packing (consistent with p33/p34) and 64 destination countries (conflicts in scope with p56's 12-15 countries — different definitions).
- corroborating: ['p92', 'p93', 'p94'] US HTS duty schedule for HS2209; p94 shows 25% additional China duty. Contextual for trade flow, not a volume input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] Same Sina annual-report table: 2024 export-mode revenue 4,774.13万元, 2023 4,513.39万元, +5.78% consistent. One underlying disclosure, not independent.
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] Same 2024 annual-report segment table; vinegar series ~126.6亿? (actually 12.66亿元) is ~71% of product-category total, consistent with Hengshun being a vinegar-led firm. Shared source.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138'] Duplicated copies of the same m.x315.cn 2020-2022 cumulative HS22090000 destination table; identical values, one measurement. Period is 3-year cumulative, not annual.
- corroborating: ['p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p105', 'p106', 'p107', 'p108', 'p109'] Same jcksj.com HS22090000 trade-value table: 2024 US 4.99M USD, 2025 3.79M (-24.14%); total exports 29.68M USD 2024. Value only, no quantity.
- corroborating: ['p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p120', 'p121', 'p122', 'p123', 'p124'] Same bianmachaxun HS22090000 export quantity/value series 2020-2024; 2024 25.76M L at 1.15 USD/L. Gives a price-per-liter bridge for converting US value to volume.
- conflicting: ['p95', 'p98', 'p111'] 2024 total export value 29.68M (jcksj) vs 29.65M (bianmachaxun) — trivial vintage difference, effectively corroborating; US value 4.99M is ~17% of total, above the 11.35% 2020-22 quantity share, sugge
- corroborating: ['p29', 'p30', 'p31', 'p139', 'p140', 'p141'] Duplicate ImportGenius supplier profile: 44 shipments 2006-2022, 6 partners, 5 ports. Very low shipment count over 16 years implies small, sporadic direct Hengshun-labeled US flows — possibly under-ca
- corroborating: ['p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p73', 'p142', 'p143', 'p144', 'p145'] Same bill of lading EGLV142252207486: 550mL@24 Chinkiang vinegar, 700 pieces, 20-ft container. Gives bottle size, case pack, and container type for physical-flow conversion.
- conflicting: ['p38', 'p42'] Zhenjiang export tonnage: 2,800 t/yr (undated, ~2020) vs 6,186 t in 2018. Different scope/period; 2018 figure may include re-exports or broader definition. Use only as order-of-magnitude bound.
- corroborating: ['p39', 'p40', 'p41'] 550mL×24 export pack and 64 destination countries for Zhenjiang vinegar — supports 550mL as modal export bottle size.
- corroborating: ['p94'] 25% Section 301 additional duty on Chinese vinegar — context for the 2025 decline in p96/p97, not a quantity input.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | US share of Hengshun export-mode revenue | 20 | 8..40 | 8..40 | % | m1 (m1) | Hengshun exports to many markets. The US took 11.35% of China's HS2209 export quantity in 2020-22 (p127) and ~17% of export value in 2024 (p95/p98), and is the #2 destination by volume (p125 vs p130). Hengshun's branded Chinkiang vinegar is well represented in US Asian retail, so its US share should | Hengshun's export revenue mix resembles the national HS2209 destination mix, adjusted upward for brand strength in the US. | A disclosed regional export breakdown showing a US share outside 8-40%. |
| a2 | Average revenue per bottle of Hengshun export vinegar | 12 | 6..25 | 6..25 | CNY per bottle | m1 (m1) | China HS2209 export average is ~1.15 USD/L (p112), i.e. ~8 CNY per 550 mL bottle at FOB; branded Hengshun export bottles carry a premium over bulk, so 12 CNY central with a range spanning bulk-like to premium FOB. | Export-mode revenue is predominantly bottled vinegar at roughly 550 mL pack sizes. | Evidence that export revenue is dominated by bulk/industrial drums or by much larger/smaller pack sizes. |
| a3 | Hengshun share of China vinegar exports to the US | 15 | 5..35 | 5..35 | % | unused | Hengshun is the largest Zhenjiang vinegar producer and Zhenjiang is the dominant export origin, but Shanxi and other Zhenjiang firms also ship to the US; 15% central with a wide range. | Hengshun's share of US-bound Chinese vinegar volume is comparable to its share of Zhenjiang-origin exports. | Customs or company data showing Hengshun's US share far outside 5-35%. |
| a4 | Trend factor from the 2020-2022 US annual average to 2024 | 1 | 0.6..1.6 | 0.6..1.6 | dimensionless | unused | China HS2209 total exports grew from ~19.6M L (2022, p120) to 25.8M L (2024, p110), ~+15%/yr, while US-bound value in 2024 was 4,992,092 USD (p95) versus ~2.8M USD/yr implied by the 2020-22 cumulative (p126/3); net 2024 vs the 2020-22 average is plausibly near flat with wide uncertainty. | US-bound volume in 2024 is within a factor of ~1.6 of the 2020-22 annual average. | US-specific quantity data for 2024 showing a large deviation from the 2020-22 average. |
| a5 | Share of US-bound Chinese HS2209 volume that is bottled retail vinegar rather than bulk/industrial | 60 | 30..85 | 30..85 | % | unused | The US flow's unit value (~1.28 USD/L, p126/p125) is close to the national export average (1.15 USD/L, p112), indicating a substantial bulk/industrial component in US shipments; bottled retail vinegar is therefore a minority-to-majority share; 60% central, 30-85% range. | The customs quantity for US-bound HS2209 includes both bottled retail packs and bulk drums, and only the bottled part counts toward the target. | Bill-of-lading or importer evidence that US-bound Hengshun/Chinese vinegar is almost entirely bottled retail packs (or almost entirely bulk). |
| a6 | Annual Hengshun 20-ft-equivalent containers of vinegar to the US | 40 | 10..120 | 10..120 | containers per year | m3 (m3) | ImportGenius records only 44 shipments over 2006-2022 (p139), but consignee naming almost certainly under-captures; a mid-size branded exporter shipping to US distributors plausibly moves tens of 20-ft containers per year. 40 central, 10-120 range. | Hengshun ships bottled vinegar to the US in 20-ft containers at roughly the documented loading. | Bill-of-lading or distributor data showing container counts far outside 10-120. |
| a7 | Average container fill relative to the documented 700-case shipment | 1 | 0.5..1.6 | 0.5..1.6 | dimensionless | m3 (m3) | The one observed bill of lading (p32) declares 700 cases = 16,800 bottles ≈ 9.2 t, well under a 20-ft container's ~20 t payload, so that shipment was partial. Typical consolidated LCL/FCL loads for a mid-size exporter range from about half to somewhat above that observed load; 1.0 central, 0.5-1.6 r | The observed 700-case shipment is representative of the order of magnitude of a typical Hengshun US container load. | Bill-of-lading data showing typical loads far above ~1,120 cases or far below ~350 cases per container. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 6,952,074,307 | ['p1'] / ['a1', 'a2'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | n/a | ['p125', 'p33'] / ['a3', 'a4', 'a5'] | [] |  | 0.00 |  | formula: numeric constant 1000 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the u |
| m3 | formula_mc | 533,347 | ['p32', 'p34'] / ['a6', 'a7'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **60,892,237** bottle, 80% interval [140,508, 26,388,914,491] bottle, basis method_spread (interval width set from the disagreement between the methods' estimates), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 8 candidate(s); entity terms ['hengshun', 'zhenjiang', 'zhenjiang hengshun group', 'zhg']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 2 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p1 | Hengshun foreign trade (export) mode sales revenue, 2024 | 47,741,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Revenue in CNY for all foreign trade exports, not a bottle count for US sales; wrong measure, unit, and scope. |
| p4 | Hengshun vinegar series (醋系列) sales revenue, 2024 | 1,265,596,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Vinegar series revenue in CNY for all markets, not a bottle count for US sales; wrong measure, unit, and scope. |
| p6 | Hengshun total sales revenue by product category, 2024 | 1,774,174,300 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Total sales revenue by product category in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |
| p8 | Hengshun total sales revenue by sales mode, 2024 | 2,093,006,800 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Total sales revenue by sales mode in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |
| p10 | Hengshun dealer (经销) mode sales revenue, 2024 | 1,941,448,600 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Dealer mode revenue in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |
| p11 | Hengshun direct sales (直销) mode sales revenue, 2024 | 103,817,200 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Direct sales mode revenue in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |
| p12 | Hengshun online sales revenue, 2024 | 274,378,100 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Online sales revenue in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |
| p13 | Hengshun offline sales revenue, 2024 | 1,818,628,700 | 万元 (10,000 CNY) | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | Offline sales revenue in CNY, not a bottle count for US sales; wrong measure, unit, and scope. |


## Final answer

The best computed estimate for Hengshun bottled vinegar sold to the United States in 2024 is 60,892,237 bottle (80% model-based interval 140,508 to 26,388,914,491 bottle). Scope: all bottle types and vinegar varieties, full year 2024.

Evidence: the revenue route (weight 50%) divides export-mode revenue 47,741,300 万元 (10,000 CNY) by a US share of 20% (range 8%–40%) and revenue per bottle of 12 CNY (range 6–25). The physical-flow route (weight 50%) scales the observed [n]-piece shipment 700 pieces by container count 40 (range 10–120) and fill factor 1 (range 0.5–1.6), using 24 bottles per case and 550 mL per bottle. The customs route was unusable.

Only the shipment counts and bottle size are observed; the US share, per-bottle revenue, container count and fill are analyst assumptions. The interval reflects disagreement between methods, not demonstrated accuracy. The dominant risk is the assumed US share and container count. Better evidence: Hengshun's own US export volumes or US customs import records.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 US share of Hengshun export-mode revenue: 20%, range 8% to 40%; used by m1. Overturned by: A disclosed regional export breakdown showing a US share outside [n]-[n].
- a2 Average revenue per bottle of Hengshun export vinegar: 12 CNY per bottle, range 6 to 25; used by m1. Overturned by: Evidence that export revenue is dominated by bulk/industrial drums or by much larger/smaller pack sizes.
- a6 Annual Hengshun [n]-ft-equivalent containers of vinegar to the US: 40 containers per year, range 10 to 120; used by m3. Overturned by: Bill-of-lading or distributor data showing container counts far outside [n]-[n].
- a7 Average container fill relative to the documented [n]-case shipment: 1 dimensionless, range 0.5 to 1.6; used by m3. Overturned by: Bill-of-lading data showing typical loads far above ~[n] cases or far below ~[n] cases per container.

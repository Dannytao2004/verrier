# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (Jiangsu Hengshun Vinegar-Industry Co., Ltd.) vinegar sold/exported to the United States in a full year, all bottled vinegar types combined, counted as physical bottles (not cases, not liters, not revenue) | unit bottle | period 2024-01-01..2024-12-31 | publisher No official publisher discloses this; best proxies are Jiangsu Hengshun Vinegar-Industry Co., Ltd. annual reports (export revenue / overseas segment), China customs HS 2209 export statistics, and US import records (USITC/CBP)

## Directions and pages

### d1 [own_history] Hengshun listed-company disclosure

Hypothesis: Hengshun's annual report discloses overseas/export revenue and possibly export volume in tons; US share of that export revenue times total export tonnage, divided by average bottle size, gives bottle count. Direction: higher overseas revenue implies more bottles.

Queries issued by the searcher: 恒顺醋业 2024年年度报告 境外 营业收入 出口; 江苏恒顺醋业 年度报告 国外 营业收入 销量 吨; 恒顺醋业 2024 年报 醋系列 销售量 吨 生产量 库存量; ImportYeti Hengshun vinegar supplier US imports; Hengshun vinegar 500ml bottle US retail price imported Zhenjiang vinegar

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://news.10jqka.com.cn/tapp/notice.html` -> **dropped** (live page has no readable date); points raw/verified -/-

### d2 [related_series] China customs trade statistics

Hypothesis: China HS 2209 (vinegar) exports to US total tonnage; Hengshun's share of China vinegar exports to US (by value or brand presence) times that tonnage, converted at average bottle fill, gives bottles. Direction: larger US-bound HS2209 tonnage implies more Hengshun bottles if share stable.

Queries issued by the searcher: UN Comtrade China vinegar HS 2209 exports United States quantity kg; 中国 海关 HS2209 醋 出口 美国 数量 吨; 恒顺醋业 2024年年度报告 境外 营业收入 出口; Hengshun vinegar export revenue overseas sales annual report 2024 Jiangsu Hengshun Vinegar-Industry

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p1 China HS22090000 vinegar exports to United States, quantity (2020-2022 cumulativ = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p2 China HS22090000 vinegar exports to United States, value USD (2020-2022 cumulati = **8,459,027** USD (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p3 United States share of China HS22090000 vinegar export quantity (2020-2022 cumul = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p4 China HS22090000 vinegar exports worldwide, total quantity (2020-2022 cumulative = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p5 Number of destination countries for China HS22090000 vinegar exports (2020-2022  = **129** countries (2020-01-01..2022-12-31) [DISCARD: Destination-country count; no bearing on US bottle volume.] quote: "近三年来,HS22090000共销往海外129个国家"
  - p6 China HS22090000 vinegar exports to Hong Kong, quantity (2020-2022 cumulative) = **13,624,552** liters (2020-01-01..2022-12-31) [DISCARD: Hong Kong quantity; not US flow.] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p7 China HS22090000 vinegar exports to Hong Kong, value USD (2020-2022 cumulative) = **15,656,412** USD (2020-01-01..2022-12-31) [DISCARD: Hong Kong value; not US flow.] quote: "出口中国香港金额最高,总计15,656,412美元。"
  - p8 China HS22090000 vinegar exports to Singapore, quantity (2020-2022 cumulative) = **4,057,620** liters (2020-01-01..2022-12-31) [DISCARD: Singapore quantity; not US flow.] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p9 China HS22090000 vinegar exports to Australia, quantity (2020-2022 cumulative) = **3,691,524** liters (2020-01-01..2022-12-31) [DISCARD: Australia quantity; not US flow.] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p10 China HS22090000 vinegar exports to Netherlands, quantity (2020-2022 cumulative) = **3,519,273** liters (2020-01-01..2022-12-31) [DISCARD: Netherlands quantity; not US flow.] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p11 China HS22090000 vinegar exports to Malaysia, quantity (2020-2022 cumulative) = **3,160,711** liters (2020-01-01..2022-12-31) [DISCARD: Malaysia quantity; not US flow.] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p12 China HS22090000 vinegar exports to Canada, quantity (2020-2022 cumulative) = **2,537,372** liters (2020-01-01..2022-12-31) [DISCARD: Canada quantity; not US flow.] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p13 China HS22090000 vinegar exports to Japan, quantity (2020-2022 cumulative) = **2,404,533** liters (2020-01-01..2022-12-31) [DISCARD: Japan quantity; not US flow.] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p14 China HS22090000 vinegar exports to France, quantity (2020-2022 cumulative) = **1,754,906** liters (2020-01-01..2022-12-31) [DISCARD: France quantity; not US flow.] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://m.x315.cn/doc/wsK8k8` -> **live_dated** (page date 2021-07-28); points raw/verified 15/15
  - p15 China HS22090000 vinegar exports to United States, trade volume (liters) = **4,378,300** liters (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p16 China HS22090000 vinegar exports to United States, trade value (USD) = **5,156,000** USD (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p17 China HS22090000 vinegar exports to United States, average price (USD per liter) = **1.18** USD per liter (2019-07-01..2020-06-30) [keep: ] quote: "\| 1 \| 美国 \| 437.83 万升 \| 515.60 万美元 \| 1.18 美元/升 \|"
  - p18 Number of destination countries/regions for China HS22090000 vinegar exports = **114** countries/regions (2019-07-01..2020-06-30) [DISCARD: Destination-country count for a different period; no bearing on US bottle volume.] quote: "中国HS22090000的主要出口国/地区有114个,相关贸易数据如下:"
  - p19 China HS22090000 vinegar exports to Australia, trade volume (liters) = **2,319,000** liters (2019-07-01..2020-06-30) [DISCARD: Australia quantity; not US flow.] quote: "\| 2 \| 澳大利亚 \| 231.90 万升 \| 359.41 万美元 \| 1.55 美元/升 \|"
  - p20 China HS22090000 vinegar exports to Singapore, trade volume (liters) = **2,763,900** liters (2019-07-01..2020-06-30) [DISCARD: Singapore quantity; not US flow.] quote: "\| 3 \| 新加坡 \| 276.39 万升 \| 289.36 万美元 \| 1.05 美元/升 \|"
  - p21 China HS22090000 vinegar exports to Malaysia, trade volume (liters) = **2,126,100** liters (2019-07-01..2020-06-30) [DISCARD: Malaysia quantity; not US flow.] quote: "\| 4 \| 马来西亚 \| 212.61 万升 \| 246.69 万美元 \| 1.16 美元/升 \|"
  - p22 China HS22090000 vinegar exports to Netherlands, trade volume (liters) = **1,673,000** liters (2019-07-01..2020-06-30) [DISCARD: Netherlands quantity; not US flow.] quote: "\| 5 \| 荷兰 \| 167.30 万升 \| 245.41 万美元 \| 1.47 美元/升 \|"
  - p23 China HS22090000 vinegar exports to Japan, trade volume (liters) = **1,593,300** liters (2019-07-01..2020-06-30) [DISCARD: Japan quantity; not US flow.] quote: "\| 6 \| 日本 \| 159.33 万升 \| 211.71 万美元 \| 1.33 美元/升 \|"
  - p24 China HS22090000 vinegar exports to Canada, trade volume (liters) = **1,533,400** liters (2019-07-01..2020-06-30) [DISCARD: Canada quantity; not US flow.] quote: "\| 7 \| 加拿大 \| 153.34 万升 \| 202.81 万美元 \| 1.32 美元/升 \|"
  - p25 China HS22090000 vinegar exports to France, trade volume (liters) = **987,475** liters (2019-07-01..2020-06-30) [DISCARD: France quantity; not US flow.] quote: "\| 8 \| 法国 \| 987475 升 \| 116.91 万美元 \| 1.18 美元/升 \|"
  - p26 China HS22090000 vinegar exports to Russia, trade volume (liters) = **924,261** liters (2019-07-01..2020-06-30) [DISCARD: Russia quantity; not US flow.] quote: "\| 9 \| 俄罗斯联邦 \| 924261 升 \| 111.84 万美元 \| 1.21 美元/升 \|"
  - p27 China HS22090000 vinegar exports to South Korea, trade volume (liters) = **841,835** liters (2019-07-01..2020-06-30) [DISCARD: South Korea quantity; not US flow.] quote: "\| 10 \| 韩国 \| 841835 升 \| 108.17 万美元 \| 1.28 美元/升 \|"
  - p28 China HS22090000 vinegar exports to United Kingdom, average price (USD per liter = **1.81** USD per liter (2019-07-01..2020-06-30) [DISCARD: UK average price; irrelevant to US volume.] quote: "\| 14 \| 英国 \| 308333 升 \| 559473 美元 \| 1.81 美元/升 \|"
  - p29 China HS22090000 vinegar exports to Switzerland, average price (USD per liter) = **4.08** USD per liter (2019-07-01..2020-06-30) [DISCARD: Switzerland average price; irrelevant to US volume.] quote: "\| 26 \| 瑞士 \| 21892 升 \| 89280 美元 \| 4.08 美元/升 \|"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] US import records

Hypothesis: US import data (USITC DataWeb / CBP) for HS 2209 from China, and bill-of-lading/import records naming Hengshun or its US importer, give US-bound shipment tonnage attributable to Hengshun; divide by bottle fill to get bottles. Direction: more Hengshun-named shipments imply more bottles.

Queries issued by the searcher: ImportYeti Hengshun vinegar US imports; Panjiva Jiangsu Hengshun Vinegar shipments United States; ImportYeti "Well Luck" Jiangsu Hengshun International Trad shipments per year; USITC DataWeb HS 2209 vinegar imports from China 2023 2024 value kg

- `https://www.importinfo.com/jiangsu-hengshun-international-trad` -> **live_dated** (page date 2026-10-02); points raw/verified 15/9
  - p30 Total bills of lading on file for Jiangsu Hengshun International TRAD (cumulativ = **169** bills of lading (2022-02-22..2026-10-01) [keep: ] quote: "There are a total of 169 bills of lading on file for Jiangsu Hengshun International TRAD between February 22nd, 2022 and October 1st, 2026."
  - p31 Shipment quantity of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU65019314 = **1,150** cartons (CTN) (2026-08-03..2026-08-03) [keep: ] quote: "\| 2026-08-03 \| COSU6501931420 \| \| 0XRBB \| Regular Bill \| COSU \| 9780897 \| CMA CGM J. MADISON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,150 CTN \| 24,95"
  - p32 Shipment weight of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU6501931420 = **24,955** KG (2026-08-03..2026-08-03) [keep: ] quote: "\| 2026-08-03 \| COSU6501931420 \| \| 0XRBB \| Regular Bill \| COSU \| 9780897 \| CMA CGM J. MADISON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,150 CTN \| 24,95"
  - p33 Shipment quantity of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU95074228 = **1,320** cartons (CTN) (2026-07-27..2026-07-27) [keep: ] quote: "\| 2026-07-27 \| COSU9507422820 \| \| 115E \| Regular Bill \| COSU \| 9448798 \| COSCO THAILAND \| 2026-07-25 \| HOUSTON, TEXAS \| SHANGHAI CHINA (MAINLAND) \| ZHENJIANG \| 1,320 CTN \| 24,386 KG \|"
  - p34 Shipment weight of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU9507422820 = **24,386** KG (2026-07-27..2026-07-27) [keep: ] quote: "\| 2026-07-27 \| COSU9507422820 \| \| 115E \| Regular Bill \| COSU \| 9448798 \| COSCO THAILAND \| 2026-07-25 \| HOUSTON, TEXAS \| SHANGHAI CHINA (MAINLAND) \| ZHENJIANG \| 1,320 CTN \| 24,386 KG \|"
  - p35 Shipment quantity of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU64637676 = **1,170** cartons (CTN) (2026-10-01..2026-10-01) [keep: ] quote: "\| Quantity \| 1170 CTN \|"
  - p36 Shipment weight of Hengshun brand Zhenjiang vinegar 550ML 24, BOL COSU6463767620 = **24,819** KG (2026-10-01..2026-10-01) [keep: ] quote: "\| Weight in KG \| 24,819 KG \|"
  - p37 Shipment quantity of XXXXXXX brand Zhenjiang vinegar 550ML 24, BOL COSU650193159 = **1,575** cartons (CTN) (2026-08-03..2026-08-03) [DISCARD: Brand redacted ('XXXXXXX'); cannot be attributed to Hengshun, so unusable as brand-specific evidence.] quote: "\| 2026-08-03 \| COSU6501931590 \| \| 0XRBB \| Regular Bill \| COSU \| 9780897 \| CMA CGM J. MADISON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,575 CTN \| 24,97"
  - p38 Shipment weight of XXXXXXX brand Zhenjiang vinegar 550ML 24, BOL COSU6501931590, = **24,971** KG (2026-08-03..2026-08-03) [DISCARD: Same redacted shipment as p37; no brand attribution.] quote: "\| 2026-08-03 \| COSU6501931590 \| \| 0XRBB \| Regular Bill \| COSU \| 9780897 \| CMA CGM J. MADISON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,575 CTN \| 24,97"
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.52wmb.com/buyer/114641345` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- dropped by code checks: 6 (period_end missing or unparseable: 6)

### d4 [base_rates] Product/packaging specification

Hypothesis: Bottle count = tonnage / (average net fill per bottle). Hengshun US retail SKUs are typically 500ml (approx 0.5 kg) glass bottles; export bulk may differ. Direction: smaller average bottle size implies more bottles per ton.

Queries issued by the searcher: Hengshun vinegar 500ml Amazon US Chinkiang; 恒顺香醋 出口 规格 500ml 瓶; Hengshun Chinkiang vinegar 16.9 oz case 12 bottles wholesale US distributor; "Hengshun" vinegar "18.6" oz OR "550ml" Weee Walmart bottle

- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 6/6
  - p39 Bottle size of Chinkiang vinegar in a Hengshun US-bound shipment (per descriptio = **550** ml per bottle (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p40 Bottles per carton in a Hengshun US-bound shipment (pack configuration) = **24** bottles per carton (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p41 Piece count on a Hengshun vinegar bill of lading (cargo #1) = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p74/p80/p87 (same 2022 BOL piece count).] quote: "Piece Count 700"
  - p42 Total shipments recorded for Jiangsu Hengshun Group (US customs, 2006-11-01 to 2 = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p43 Trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p44 Ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
- `https://fivecontinentsintl.com/zh/product/hengshun-brand-vinegar-0-additives/` -> **live_dated** (page date 2024-11-01); points raw/verified 12/12
  - p45 Hengshun Jin You zero-additive fragrant vinegar (US listing) bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺金优零添加香醋500ml"
  - p46 Hengshun Jin You zero-additive fragrant vinegar (US listing) case configuration = **12** bottles per case (..) [keep: ] quote: "Case Size: 500ml*12btls"
  - p47 Hengshun nine-degree rice vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺九度米醋500ml"
  - p48 Hengshun scallion-ginger cooking wine bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺葱姜料酒500ml"
  - p49 Hengshun Jin You zero-additive ginger-scallion cooking wine bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺金优零添加姜葱料酒500ml"
  - p50 Hengshun six-year fragrant vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "恒顺六年香醋580ml"
  - p51 Hengshun three-year fragrant vinegar bottle size = **580** ml per bottle (..) [keep: ] quote: "恒顺三年香醋580ml"
  - p52 Hengshun Jin You zero-additive aged vinegar bottle size = **535** ml per bottle (..) [keep: ] quote: "恒顺金优零添加陈醋535ml"
  - p53 Hengshun dumpling vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺饺子醋500ml"
  - p54 Hengshun xiaolongbao fragrant vinegar bottle size = **550** ml per bottle (..) [keep: ] quote: "恒顺香醋-小笼包(550ml)"
  - p55 Hengshun white rice vinegar bottle size = **500** ml per bottle (..) [keep: ] quote: "恒顺白米醋500ml"
  - p56 Hengshun premium eight-year fragrant vinegar bottle size = **300** ml per bottle (..) [keep: ] quote: "恒顺极品八年香醋300ml"
- `https://www.weee.com/ko/search/hengshun%20zhenjiang%20vinegar?keyword=hengshun%20zhenjiang%20vinegar&trigger_type=search_active` -> **live_dated** (page date 2026-10-18); points raw/verified 12/12
  - p57 Heng Shun Zhenjiang vinegar bottle size listed on Weee! (US Asian grocery), flui = **18.6** fluid ounces (..) [keep: ] quote: "Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p58 Heng Shun Zhenjiang vinegar unit price per fluid ounce on Weee! listing = **0.16** USD per fluid ounce (..) [keep: ] quote: "$0.16/액량 온스 Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p59 Heng Shun Zhenjiang vinegar bottle price on Weee! listing = **2.99** USD per bottle (..) [keep: ] quote: "$2.99 $0.16/액량 온스 Heng Shun Zhenjiang 식초 18.6 액량 온스"
  - p60 Heng Shun Zhenjiang vinegar listing cumulative units sold label on Weee! ("600+  = **600** bottles sold (listing label) (..) [DISCARD: Per-listing '600+ sold' floor on one Weee! SKU; not a market total and too small/ambiguous to use as a level.] quote: "600개+ 판매"
  - p61 Heng shun Zhenjiang vinegar Tianchu bottle size listed on Weee!, fluid ounces = **18.6** fluid ounces (..) [keep: ] quote: "Heng shun 진강식초 천추 18.6 액량 온스"
  - p62 Heng shun Zhenjiang vinegar Tianchu unit price per fluid ounce on Weee! listing = **0.19** USD per fluid ounce (..) [keep: ] quote: "$0.19/액량 온스 Heng shun 진강식초 천추 18.6 액량 온스"
  - p63 Heng shun Zhenjiang vinegar Tianchu bottle price on Weee! listing = **3.49** USD per bottle (..) [keep: ] quote: "$3.49 $0.19/액량 온스 Heng shun 진강식초 천추 18.6 액량 온스"
  - p64 Hengshun 6-year aged Zhenjiang vinegar Tianchu bottle size listed on Weee!, mill = **580** milliliters (..) [keep: ] quote: "Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p65 Hengshun 6-year aged Zhenjiang vinegar Tianchu unit price per fluid ounce on Wee = **0.66** USD per fluid ounce (..) [keep: ] quote: "$0.66/액량 온스 Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p66 Hengshun 6-year aged Zhenjiang vinegar Tianchu bottle price on Weee! listing = **12.99** USD per bottle (..) [keep: ] quote: "$12.99 $0.66/액량 온스 Hengshun 6년 묵힌 쩐지앙 식초 천추 580 밀리리터"
  - p67 Hengshun 6-year aged Zhenjiang vinegar listing cumulative units sold label on We = **50** bottles sold (listing label) (..) [DISCARD: Per-listing '50+ sold' floor on one Weee! SKU; not a market total.] quote: "50개+ 판매"
  - p68 Total search results for "hengshun zhenjiang vinegar" on Weee! (listing count) = **505** product listings (..) [DISCARD: Search-result count (505 listings) is a search artifact, not a sales quantity.] quote: "hengshun zhenjiang vinegar(505)"
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0

### d5 [capacity_consumption] US retail sell-through / consumer demand

Hypothesis: US Chinese-vinegar retail market size (or Asian condiment category) times Hengshun brand share, divided by average retail price per bottle, gives bottles sold in US; should approximate export shipments plus inventory change. Direction: larger category or share implies more bottles.

Queries issued by the searcher: US Chinese black vinegar market size retail sales; Chinkiang vinegar US sales brand share Hengshun; Asian condiments sauces US market size retail 2024 Statista billion; Hengshun vinegar export revenue overseas annual report 2024 恒顺醋业 出口

- `https://www.foodandbeverage.business/manufacturing/asian-flavors-fuel-growth-surge-in-us-food-industry/?amp=1` -> **live_dated** (page date 2025-11-04); points raw/verified 6/3
  - p69 US retail sales of Asian packaged foods, 2024 (Circana) = **14,700,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "According to Circana, retail sales of Asian packaged foods hit $14.7 billion in 2024"
  - p70 Year-over-year growth rate of US Asian packaged food retail sales, 2024 = **10** % (2024-01-01..2024-12-31) [keep: ] quote: "reflecting over 10% year-over-year growth"
  - p71 Year-over-year unit sales growth of US Asian packaged foods, 2024 = **7** % (2024-01-01..2024-12-31) [keep: ] quote: "with unit sales increasing nearly 7%"
- `https://www.globalinforesearch.com.cn/reports/1278540/black-vinegar` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/8
  - p72 Trading partners count for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Duplicate of p43 (trading partners count).] quote: "Trading Partners 6"
  - p73 Ports count for Jiangsu Hengshun Group shipments in US customs records = **5** ports (2006-11-01..2022-08-14) [DISCARD: Duplicate of p44 (ports count).] quote: "Ports 5"
  - p74 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24, a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p80/p87 (same BOL piece count).] quote: "Piece Count 700"
  - p75 Bottle size in shipment description: Chinkiang vinegar 550ML packed 24 per unit = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p39/p81/p88 (550 ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p76 Bottles per case in shipment description: Chinkiang vinegar 550ML@24 = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p40/p82/p89 (24 per case).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p77 Container length in centimeters on bill of lading EGLV142252207486 = **240** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p83/p90 (container length).] quote: "Length 240"
  - p78 Container height in centimeters on bill of lading EGLV142252207486 = **102** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p84/p91 (container height).] quote: "Height 102"
  - p79 Container width in centimeters on bill of lading EGLV142252207486 = **96** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p85/p92 (container width).] quote: "Width 96"
- `https://consillar.com/blog/chinese-black-vinegar-cooking` -> **live_dated** (page date 2026-06-16); points raw/verified 12/0
- dropped by code checks: 16 (period_end missing or unparseable: 14; period_end 2031-12-31 after as_of: 1; value_as_written not in quote as a whole number: 1)

### d6 [physical_flow] Container/shipment logistics

Hypothesis: Number of Hengshun containers shipped to US per year times bottles per container (cartons/container x bottles/carton) gives bottles. Direction: more containers or higher fill implies more bottles.

Queries issued by the searcher: Hengshun vinegar container shipment US bill of lading; Jiangsu Hengshun Vinegar export revenue overseas annual report 2024; 52wmb Jiangsu Hengshun International Trade supplier shipments US; Panjiva "Jiangsu Hengshun" supplier shipments United States vinegar

- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 10/7
  - p80 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p87 (same BOL piece count).] quote: "Piece Count 700"
  - p81 Bottle size in vinegar packing description (Chinkiang vinegar 550ML@24) = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p88 (550 ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p82 Bottles per carton in vinegar packing description (550ML@24) = **24** bottles per carton (2022-08-13..2022-08-13) [DISCARD: Duplicate of p89 (24 per unit).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p83 Container length in centimeters for the vinegar shipment container = **240** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p84 Container height in centimeters for the vinegar shipment container = **102** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p85 Container width in centimeters for the vinegar shipment container = **96** centimeters (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
  - p86 Container type for the vinegar shipment (20 Foot General Purpose Container) = **20** foot container (2022-08-13..2022-08-13) [keep: ] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://portexaminer.com/trade-data/hengshun-international-trade-hong-vertex-distribution/hjscshcm4s349300/` -> **live_dated** (page date 2014-09-19); points raw/verified 4/0
- `https://hk.marketscreener.com/quote/stock/JIANGSU-HENGSHUN-VINEGAR--6497578/finances-segments/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 7 (value_as_written not in quote as a whole number: 3; period_end missing or unparseable: 3; number: more than one number in value_as_written: 1)

### d7 [persona] US importer/distributor

Hypothesis: Hengshun's US importer/distributor (e.g., Asian food wholesalers) purchase volumes or stated annual sales of Hengshun vinegar approximate US-bound bottles. Direction: larger distributor purchases imply more bottles.

Queries issued by the searcher: Hengshun vinegar US distributor importer; 恒顺 美国 经销商 进口商 香醋; "Well Luck" Hengshun vinegar shipment bill of lading 2024 550ML; 恒顺醋业 2024年年报 境外 出口 收入 海外

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/6
  - p87 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 (a = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p41/p74/p80 (same BOL piece count).] quote: "Piece Count 700"
  - p88 Bottle size in vinegar cargo description on bill of lading (550ML@24) = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p39/p75/p81 (550 ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p89 Bottles per unit in vinegar cargo description on bill of lading (550ML@24) = **24** bottles per unit (2022-08-13..2022-08-13) [DISCARD: Duplicate of p40/p76/p82 (24 per unit).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p90 Container length in centimeters on bill of lading EGLV142252207486 = **240** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p77/p83 (container length).] quote: "Length 240"
  - p91 Container height in centimeters on bill of lading EGLV142252207486 = **102** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p78/p84 (container height).] quote: "Height 102"
  - p92 Container width in centimeters on bill of lading EGLV142252207486 = **96** centimeters (2022-08-13..2022-08-13) [DISCARD: Duplicate of p79/p85 (container width).] quote: "Width 96"
- `https://tw.news.yahoo.com/%E5%90%84%E4%BA%9E%E6%B4%B2%E8%B6%85%E5%B8%82%E6%8E%A8%E5%87%BA%E6%81%86%E9%A0%86%E7%B3%BB%E5%88%97%E7%94%A2%E5%93%81%E9%BB%` -> **live_dated** (page date 2024-11-29); points raw/verified 0/0
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### d8 [shocks] Trade policy and demand shifts

Hypothesis: US-China tariffs, shipping costs, and post-2020 demand shifts change US-bound volume; adjusting a base-year estimate by observed export growth or tariff-driven decline constrains the 2024 figure. Direction: tariff increases or demand growth shift bottles up/down.

Queries issued by the searcher: Section 301 tariff vinegar HS 2209 China; 恒顺醋业 2024年年度报告 出口 境外 营业收入; 恒顺醋业 2024 年报 境外地区 营业收入 出口 占比; US imports vinegar HS 2209 from China value 2024 USITC

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://tariff.gatewaylines.com/hts/2209000060` -> **live_dated** (page date 2026-10-18); points raw/verified 8/0
- `http://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918927` -> **live_dated** (page date 2024-07-26); points raw/verified 15/13
  - p93 Hengshun (Jiangsu Hengshun Vinegar-Industry) foreign-trade (export) mode revenue = **47,741,038** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p94 Hengshun foreign-trade (export) mode revenue year-on-year change, 2024 = **5.78** % (2024-01-01..2024-12-31) [keep: ] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p95 Hengshun foreign-trade (export) mode gross margin, 2024 = **27.3** % (2024-01-01..2024-12-31) [keep: ] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p96 Hengshun vinegar (醋) series revenue, 2024 = **1,265,596,326** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点"
  - p97 Hengshun vinegar (醋) series revenue year-on-year change, 2024 = **-2.2** % (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点"
  - p98 Hengshun vinegar (醋) series sales volume, 2024 = **212,747** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22"
  - p99 Hengshun vinegar (醋) series sales volume year-on-year change, 2024 = **1.33** % (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22"
  - p100 Hengshun vinegar (醋) series production volume, 2024 = **210,641** 吨 (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22"
  - p101 Hengshun total operating revenue, 2024 = **2,195,870,508** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "营业收入 \| 2,195,870,508.45 \| 2,106,410,685.37 \| 4.25 \| 2,139,020,033.23"
  - p102 Hengshun total operating revenue year-on-year change, 2024 = **4.25** % (2024-01-01..2024-12-31) [keep: ] quote: "营业收入 \| 2,195,870,508.45 \| 2,106,410,685.37 \| 4.25 \| 2,139,020,033.23"
  - p103 Hengshun main condiment business revenue, 2024 = **2,093,006,845** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "调味品 \| 2,093,006,844.54 \| 1,358,355,887.39 \| 35.10 \| 0.73 \| -3.34 \| 增加2.73个百分点"
  - p104 Hengshun online sales channel revenue, 2024 = **274,378,141** 人民币元 (2024-01-01..2024-12-31) [keep: ] quote: "线上销售 \| 274,378,140.67 \| 13.11 \| 53.17 \| 264,716,814.16 \| 12.74 \| 50.22"
  - p105 Hengshun vinegar (醋) series gross margin, 2024 = **45.31** % (2024-01-01..2024-12-31) [keep: ] quote: "醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点"
- dropped by code checks: 10 (period_end missing or unparseable: 10)

### b1 [own_history] Hengshun annual report segment/region disclosure

Hypothesis: If Hengshun's annual report breaks export revenue or volume by destination region (North America / US), that share times p93 export revenue and p98 vinegar volume would replace the assumed US share of exports, the largest uncertainty in m1/m2.

Queries issued by the searcher: 江苏恒顺醋业 2024年年度报告 主营业务分地区 境外; 恒顺醋业 2024年报 出口 收入 境外 美国; 恒顺醋业 2024 年报 食醋 销售量 吨 生产量 库存量; 恒顺醋业 出口 美国 占比 海外 收入 2024 外贸

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_XKUV.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=10918927` -> **live_dated** (page date 2024-07-26); points raw/verified 14/11
  - p106 Hengshun 2024 export (foreign trade) segment revenue, RMB = **47,741,038** RMB yuan (2024-01-01..2024-12-31) [DISCARD: Duplicate of p93 (2024 foreign-trade revenue).] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p107 Hengshun 2024 export (foreign trade) segment cost, RMB = **34,706,632** RMB yuan (2024-01-01..2024-12-31) [DISCARD: Duplicate of p93 line (export segment cost).] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p108 Hengshun 2024 export (foreign trade) segment gross margin = **27.3** % (2024-01-01..2024-12-31) [DISCARD: Duplicate of p95 (export gross margin).] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p109 Hengshun 2024 export (foreign trade) revenue YoY change = **5.78** % (2024-01-01..2024-12-31) [DISCARD: Duplicate of p94 (export revenue YoY).] quote: "外贸模式 \| 47,741,038.39 \| 34,706,631.54 \| 27.30 \| 5.78 \| 4.53 \| 增加0.87个百分点"
  - p110 Hengshun 2024 vinegar series (醋系列) sales volume = **212,747** tonnes (2024-01-01..2024-12-31) [DISCARD: Duplicate of p98 (2024 vinegar volume).] quote: "醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22"
  - p111 Hengshun 2024 vinegar series (醋系列) production volume = **210,641** tonnes (2024-01-01..2024-12-31) [DISCARD: Duplicate of p100 (2024 vinegar production).] quote: "醋系列 \| 吨 \| 210,640.70 \| 212,746.92 \| 10,879.19 \| 1.44 \| 1.33 \| -16.22"
  - p112 Hengshun 2024 vinegar series (醋系列) revenue, RMB = **1,265,596,326** RMB yuan (2024-01-01..2024-12-31) [DISCARD: Duplicate of p96 (2024 vinegar revenue).] quote: "醋系列 \| 1,265,596,326.34 \| 692,098,301.14 \| 45.31 \| -2.20 \| -5.99 \| 增加2.21个百分点"
  - p113 Hengshun 2024 total condiment (调味品) revenue, RMB = **2,093,006,845** RMB yuan (2024-01-01..2024-12-31) [DISCARD: Duplicate of p103 (2024 condiment revenue).] quote: "调味品 \| 2,093,006,844.54 \| 1,358,355,887.39 \| 35.10 \| 0.73 \| -3.34 \| 增加2.73个百分点"
  - p114 Hengshun 2024 total revenue (consolidated), RMB = **2,195,870,508** RMB yuan (2024-01-01..2024-12-31) [DISCARD: Duplicate of p101 (2024 total revenue).] quote: "营业收入 \| 2,195,870,508.45 \| 2,106,410,685.37 \| 4.25 \| 2,139,020,033.23"
  - p115 Hengshun 2024 year-end USD-denominated accounts receivable, RMB equivalent = **3,334,185** RMB yuan (2024-12-31..2024-12-31) [keep: ] quote: "其中:美元 \| 463,828.49 \| 7.1884 \| 3,334,184.72"
  - p116 Hengshun 2024 year-end USD/RMB conversion rate used = **7.188** RMB per USD (2024-12-31..2024-12-31) [keep: ] quote: "其中:美元 \| 463,828.49 \| 7.1884 \| 3,334,184.72"
- dropped by code checks: 3 (period_end missing or unparseable: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b2 [related_series] US customs / import records

Hypothesis: A full-year 2024 count of Hengshun-named bills of lading (or Panjiva/ImportGenius shipment totals for Jiangsu Hengshun International Trading) times bottles per shipment from p31-p36 would give a direct physical-flow estimate, bypassing the export-share assumption.

Queries issued by the searcher: Panjiva Jiangsu Hengshun International Trading 2024 shipments US; ImportGenius Hengshun vinegar bill of lading cartons 2024; panjiva.com Jiangsu Hengshun International Trading supplier shipments; "importinfo.com" Hengshun vinegar bills of lading consignee CTN

- `https://www.importinfo.com/jiangsu-hengshun-international-trad` -> **live_dated** (page date 2026-10-02); points raw/verified 15/8
  - p117 Total bills of lading on file for Jiangsu Hengshun International TRAD (Feb 2022– = **169** bills of lading (2022-02-22..2026-10-01) [DISCARD: Exact duplicate of p30 (same ImportInfo 169-BOL count); adds no information.] quote: "There are a total of 169 bills of lading on file for Jiangsu Hengshun International TRAD between February 22nd, 2022 and October 1st, 2026."
  - p118 Shipment quantity on one bill of lading (Hengshun brand Zhenjiang vinegar 550ML  = **1,150** CTN (cartons) (2026-08-03..2026-08-03) [DISCARD: Duplicate of p31 (same 1,150 CTN Newark BOL).] quote: "SON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,150 CTN \| 24,955 KG \| House to House \| JIANGSU HENGSHUN INTERNATIONAL TRAD \| WELL LUCK COMPANY INCORPORATED \"
  - p119 Shipment quantity on one bill of lading (XXXXXXX brand Zhenjiang vinegar 550ML 2 = **1,575** CTN (cartons) (2026-08-03..2026-08-03) [DISCARD: A 1,575 CTN BOL for an 'XXXXXXX' brand, not confirmed Hengshun-branded; excluded to avoid attributing another brand's vo] quote: "SON \| 2026-07-31 \| NEWARK, NEW JERSEY \| YANGSHAN CHINA (MAINLAND) \| ZHENJIANG \| 1,575 CTN \| 24,971 KG \| House to House \| JIANGSU HENGSHUN INTERNATIONAL TRAD \| WELL LUCK COMPANY INCORPORATED \"
  - p120 Shipment quantity on one bill of lading (Hengshun brand Zhenjiang vinegar 550ML  = **1,320** CTN (cartons) (2026-07-27..2026-07-27) [DISCARD: Duplicate of p33 (same 1,320 CTN Houston BOL).] quote: "HAILAND \| 2026-07-25 \| HOUSTON, TEXAS \| SHANGHAI CHINA (MAINLAND) \| ZHENJIANG \| 1,320 CTN \| 24,386 KG \| House to House \| JIANGSU HENGSHUN INTERNATIONAL TRAD \| WELL LUCK COMPANY INCORPORATED \"
  - p121 Shipment quantity on one bill of lading (Hengshun brand Zhenjiang vinegar 550ML  = **1,170** CTN (cartons) (2026-10-01..2026-10-01) [DISCARD: Duplicate of p35 (same 1,170 CTN Oakland BOL).] quote: "\| Quantity \| 1170 CTN \|"
  - p122 Bills of lading for Jiangsu Hengshun International TRAD unlading at Newark, New  = **76** bills of lading (..2026-08-03) [keep: ] quote: "\| Newark, New Jersey \| 76 \| 2026-08-03 \|"
  - p123 Bills of lading for Jiangsu Hengshun International TRAD unlading at Long Beach,  = **42** bills of lading (..2026-07-07) [keep: ] quote: "\| Long Beach, California \| 42 \| 2026-07-07 \|"
  - p124 Bills of lading for Jiangsu Hengshun International TRAD unlading at Oakland, Cal = **19** bills of lading (..2026-10-02) [keep: ] quote: "\| Oakland, California \| 19 \| 2026-10-02 \|"
- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p125 Total US customs shipments recorded for Jiangsu Hengshun Group (ImportGenius, al = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p42 (ImportGenius 44 shipments, 2006-2022).] quote: "Total Shipments 44"
  - p126 Number of trading partners for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p43 (6 trading partners).] quote: "Trading Partners 6"
  - p127 Number of ports in Jiangsu Hengshun Group US customs records = **5** ports (2006-11-01..2022-08-14) [DISCARD: Exact duplicate of p44 (5 ports).] quote: "Ports 5"
  - p128 Piece count on bill of lading EGLV142252207486 (Chinkiang vinegar 550ML@24) = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p129 Bottle size in vinegar description on bill of lading EGLV142252207486 = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p39 (550 ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p130 Bottles per carton in vinegar description on bill of lading EGLV142252207486 = **24** bottles per carton (2022-08-13..2022-08-13) [DISCARD: Duplicate of p40 (24 bottles per carton).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p131 Container length on bill of lading EGLV142252207486 = **240** container length (cm) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p83 (container length 240 cm).] quote: "Length 240"
  - p132 Container height on bill of lading EGLV142252207486 = **102** container height (cm) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p84 (container height 102 cm).] quote: "Height 102"
  - p133 Container width on bill of lading EGLV142252207486 = **96** container width (cm) (2022-08-13..2022-08-13) [DISCARD: Duplicate of p85 (container width 96 cm).] quote: "Width 96"
- `https://www.tradeint.com/search/china/export-data/company/jiangsu-hengshun-international-trad/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 7 (period_end missing or unparseable: 7)

### b3 [base_rates] US retail scanner / distributor data

Hypothesis: US retail dollar sales of Hengshun-branded vinegar (Nielsen/Circana or a major Asian wholesaler's Hengshun purchases) divided by the retail price per bottle (p59/p63) would give a demand-side bottle count to cross-check the export-side estimate and resolve the p1-vs-p15 period disagreement.

Queries issued by the searcher: Hengshun vinegar US retail sales Nielsen Circana 2024; Chinkiang vinegar US market size brand share; Hengshun vinegar US distributor annual purchases importer Chinkiang vinegar container; 恒顺醋业 2024年报 境外 出口 收入 海外

- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-
- `https://listthe.com/manufacturers-of/five-continents-international-limit` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 7/4
  - p134 Piece count on one Hengshun bill of lading (container ASCU2200167) of Chinkiang  = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p128 (700 pieces on the 2022 BOL).] quote: "Piece Count 700"
  - p135 Bottle size in cargo description of Hengshun Chinkiang vinegar shipment (550ML@2 = **550** milliliters per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p39 (550 ml bottle size).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p136 Bottles per unit in cargo description of Hengshun Chinkiang vinegar shipment (@2 = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p40 (24 bottles per case).] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p137 Container length in feet for the Hengshun vinegar bill of lading = **20** foot container (2022-08-13..2022-08-13) [DISCARD: Duplicate of p86 (20-ft GP container type).] quote: "Type 20 Foot General Purpose Container, Passive vents at upper part of cargo space"
- `https://blog.themalamarket.com/sourcing-zhenjiang-vinegar/` -> **live_dated** (page date 2024-05-04); points raw/verified 0/0
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar exports', 'china vinegar us imports', 'vinegar export volume']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] Same m.x315.cn HS22090000 dataset; p1/p2 are the US line, p3 the US share, p4 the worldwide total. Internally consistent (p1/p4 ≈ 11.35%). Shared single source, so not independent confirmation.
- corroborating: ['p15', 'p16', 'p17'] Same HS22090000 US line for 2019-07..2020-06; value/quantity = 1.18 USD/L consistent. Different period from p1-p4, so a level shift is a period difference, not a contradiction.
- conflicting: ['p1', 'p15'] US-bound HS2209 quantity: p15 implies ~4.38M L/yr in 2019-20 while p1 implies ~2.2M L/yr averaged over 2020-22. Plausible real decline (COVID/tariffs) rather than error, but the two cannot be pooled; 
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] importinfo.com bill-of-lading records naming Jiangsu Hengshun International Trading; three 2026 shipments of 550ML@24 with ~24-25 t each, consistent carton weights (~21 kg/CTN). Same aggregator source
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] p37/p38 are the same shipment pattern with brand redacted; same weight/carton structure, so they corroborate the per-container fill but add no new brand-specific information.
- corroborating: ['p39', 'p40', 'p41', 'p74', 'p75', 'p76', 'p80', 'p81', 'p82', 'p87', 'p88', 'p89'] Repeated copies of the same 2022 importgenius bill of lading (550ML@24, 700 pieces). One underlying record, many duplicate ids.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p61', 'p64'] US retail SKU bottle sizes cluster at 500-580 ml (mostly 500/550/580). Supports an average fill near 0.5-0.55 L per bottle for bottled retail vinegar.
- corroborating: ['p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105'] Same Hengshun 2024 annual-report extract (Sina mirror). p93 export-mode revenue 47.7M RMB is the only company-level export figure; p98 vinegar volume 212,747 t is worldwide (mostly domestic), so it bo
- corroborating: ['p69', 'p70', 'p71'] Same Circana/industry article; Asian packaged foods $14.7bn, +10% value, +7% units in 2024. Category context only; vinegar is a tiny sub-slice.
- corroborating: ['p42', 'p43', 'p44', 'p72', 'p73'] Same importgenius profile: 44 shipments 2006-2022, 6 partners, 5 ports. p43/p72 and p44/p73 are duplicate pairs.
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68'] Weee! retail listings: 18.6 fl oz (~550 ml) at $2.99-$3.49, 580 ml at $12.99. Gives retail price anchors and confirms 550 ml dominant size; '600+ sold' labels are per-listing floors, not market totals
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4'] Same m.x315.cn HS22090000 dataset for 2020-2022 cumulative; p3 (11.35%) is consistent with p1/p4 (6.597/58.12 = 11.35%). One underlying measurement, not four independent ones. Period is 2020-2022, not
- corroborating: ['p15', 'p16', 'p17'] Same 2019-07..2020-06 HS22090000 US export record; p17 = p16/p15. Different period from p1-p4 (mid-2019 to mid-2020 vs 2020-2022 cumulative), so the two are not contradictory but cannot be medianed to
- corroborating: ['p30', 'p117'] Identical ImportInfo count (169 BOLs, Feb 2022-Oct 2026) for Jiangsu Hengshun International Trading; duplicate of one source.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p118', 'p119', 'p120', 'p121'] ImportInfo BOL lines for Hengshun 550ML@24 shipments in 2026; carton counts 1,150-1,575 and weights ~24.4-25.0 t per BOL are mutually consistent (about 21-22 kg per carton gross). These are 2026 shipm
- corroborating: ['p39', 'p40', 'p129', 'p130', 'p135', 'p136'] Same 550ML@24 packing description repeated across ImportGenius/ImportInfo records; one packing fact, not independent confirmations.
- corroborating: ['p42', 'p125'] Identical ImportGenius all-years shipment count (44, 2006-2022) for Jiangsu Hengshun Group; duplicate.
- corroborating: ['p43', 'p126'] Identical trading-partner count (6); duplicate.
- corroborating: ['p44', 'p127'] Identical port count (5); duplicate.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p61', 'p64'] US retail SKU bottle sizes cluster at 500-580 ml (mostly 500/550/580), with one 300 ml premium SKU. Supports an average net fill near 0.5-0.55 L per bottle for bottled vinegar; p57/p61 (18.6 fl oz = 5
- corroborating: ['p59', 'p63', 'p66'] US retail bottle prices $2.99-$12.99 depending on SKU/age; consistent with a low-price commodity SKU and premium aged SKUs. Useful for a demand-side cross-check, not for export volume directly.
- corroborating: ['p93', 'p94', 'p95', 'p106', 'p107', 'p108', 'p109'] Same 2024 annual-report foreign-trade segment line (revenue RMB 47.74m, cost 34.71m, margin 27.3%, +5.78% YoY); duplicates of one disclosure. This is total export revenue, all destinations and all pro
- corroborating: ['p96', 'p97', 'p98', 'p99', 'p100', 'p105', 'p110', 'p111', 'p112'] Same 2024 annual-report vinegar-series line (revenue RMB 1.266bn, volume 212,747 t, margin 45.31%, -2.2% revenue, +1.33% volume); duplicates. Gives a domestic-weighted average realization of about RMB
- corroborating: ['p101', 'p102', 'p103', 'p104', 'p113', 'p114'] Same 2024 consolidated income statement lines; duplicates. Context only.
- corroborating: ['p115', 'p116'] USD receivable and the 7.1884 RMB/USD rate used at 2024 year-end; the rate is a usable conversion constant.
- corroborating: ['p122', 'p123', 'p124'] Port-level BOL counts (Newark 76, Long Beach 42, Oakland 19) sum to 137 of the 169 total; consistent with the same ImportInfo universe and showing US West and East Coast distribution.
- corroborating: ['p128', 'p134'] Same 700-piece count on the 2022 Chinkiang 550ML@24 BOL; duplicate.
- corroborating: ['p131', 'p132', 'p133', 'p83', 'p84', 'p85', 'p86', 'p137'] Same 20-ft container dimensions (240x102x96 cm) on the 2022 BOL; duplicate. A 20-ft GP holds roughly 1,100-1,600 cartons of 24x550ml, consistent with the observed 1,150-1,575 carton BOLs.
- corroborating: ['p69', 'p70', 'p71'] Same Circana 2024 Asian packaged foods release; category is far broader than Hengshun vinegar and cannot be used without a very small share assumption.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | US share of Hengshun 2024 export revenue | 15 | 5..35 | 5..35 | % | unused | Hengshun's export segment is dominated by Asian diaspora markets (SE Asia, Japan, Hong Kong, North America). All-China HS2209 exports put the US at ~11% of vinegar export volume (p3); Hengshun's brand is stronger in SE Asia than in the US, so set near but not above the HS2209 US share, widened for b | Hengshun's US revenue share of exports is similar to the all-China HS2209 US share; transfers to a bottled-vinegar export flow. | Annual-report or customs evidence that North America is a much larger or much smaller share of Hengshun exports. |
| a2 | Vinegar share of Hengshun export revenue | 70 | 50..85 | 46.1..92.2 (widened) | % | unused | Vinegar is Hengshun's core product (~58% of condiment revenue per p96/p103), but the export segment also carries cooking wine, soy sauce and other condiments. Vinegar is the flagship export item, so set above its domestic revenue share. | The export mix is more vinegar-heavy than the domestic mix, as brand strength suggests. | Export product-mix disclosure showing vinegar below half of export revenue. |
| a3 | Average net fill per exported bottle | 0.52 | 0.45..0.58 | 0.3612..0.7225 (widened) | liter per bottle | unused | US retail SKUs cluster at 500-580 ml (p45-p56, p57, p61, p64) and the export pack is 550 ml (p39). Weighted toward 500-550 ml commodity SKUs, with some 580 ml and a few 300 ml premium bottles, gives about 0.52 L. | Bottled (not bulk) vinegar dominates the US-bound flow, as the BOL descriptions indicate. | Evidence that a large share of US-bound volume is bulk/drum or very small bottles. |
| a4 | Hengshun share of China HS2209 vinegar exports to the US | 12 | 5..25 | 5..25 | % | unused | Hengshun is China's largest vinegar producer and the best-known Zhenjiang vinegar brand, but China's US vinegar exports include many other producers and private-label brands. Set at a modest share of the value/volume flow, above a generic producer but well below dominance. | Hengshun's US-bound volume is a meaningful but minority slice of all Chinese vinegar entering the US. | Import records showing Hengshun-named shipments account for a much larger or smaller fraction of Chinese vinegar imports. |
| a5 | Growth factor from the 2020-2022 average annual US-bound HS2209 volume to 2024 | 1.1 | 0.8..1.5 | 0.8..1.5 | factor | unused | US Asian packaged-food retail sales grew ~10% in 2024 (p70) and unit sales ~7% (p71), while Hengshun's total export revenue grew 5.78% in 2024 (p94). A modest upward adjustment from the 2020-2022 average annual level to 2024 is consistent with these trends; tariffs and shipping costs could push it d | US demand for Chinese vinegar grew modestly between the 2020-2022 window and 2024. | Customs data showing flat or declining China-to-US vinegar volumes in 2023-2024. |
| a6 | Bottles per Hengshun US bill of lading | 30,000 | 18,000..45,000 | 18,000..45,000 | bottle per bill of lading | unused | Observed 2026 BOLs carry 1,150-1,575 cartons at 24 bottles per carton (p31, p33, p35, p40), i.e. 27,600-37,800 bottles per BOL. A 20-ft container (p86) holds roughly this range. Set the central value near the middle of the observed range. | 2024 BOLs had similar carton counts and 24-bottle packs as the 2026 records. | Evidence that 2024 shipments were much smaller (LCL) or used different pack sizes. |
| a7 | Hengshun US-bound bills of lading per year in 2024 | 40 | 20..70 | 20..70 | bill of lading per year | unused | ImportInfo records 169 BOLs over Feb 2022-Oct 2026 (~4.6 years), implying roughly 37 per year on average (p30). Some records may be non-vinegar or non-US; set the central value near the implied annual rate with a wide range. | The 2022-2026 BOL rate is representative of 2024 and most BOLs are US-bound vinegar. | Evidence that 2024 had far fewer or far more Hengshun US shipments than the multi-year average. |
| a8 | Density of bottled vinegar | 1 | 0.98..1.05 | 0.7173..1.435 (widened) | kg per liter | unused | Vinegar is essentially a dilute acetic-acid solution with density close to water. The observed BOLs corroborate this: 1,150 CTN x 24 x 550 ml = 15.18 kL against 24,955 kg (p31/p32) implies ~1.64 kg/L gross including glass and cartons; net vinegar density is near 1.0. Used to convert tonnes to liters | The vinegar-series tonnage in p98 is net product mass, so dividing by density gives net liters. | Evidence that p98 tonnage is gross shipping weight including packaging. |
| a9 | Years spanned by the 2020-2022 cumulative HS2209 window | 3 | 2.9..3.1 | 2.12..4.24 (widened) | year | unused | p1 is a cumulative 2020-01-01..2022-12-31 total; dividing by the number of years in the window converts it to an annual average. Three calendar years is exact; the narrow range only reflects that the window may not be perfectly aligned to full years. | p1 covers exactly the three calendar years 2020-2022. | Evidence that the p1 window is shorter or longer than three years. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p93', 'p96', 'p98'] / ['a1', 'a2', 'a3', 'a8'] | [] |  | 0.00 |  | formula_mc uses 4 assumptions (at most 3) |
| m2 | formula_mc | n/a | ['p1'] / ['a3', 'a4', 'a5', 'a9'] | [] |  | 0.00 |  | formula_mc uses 4 assumptions (at most 3) |
| m3 | formula_mc | n/a |  | [] |  | 0.00 |  | input a10: id a10 unknown or discarded |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **n/a** bottle, 80% interval [n/a, n/a] bottle, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']; 13 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

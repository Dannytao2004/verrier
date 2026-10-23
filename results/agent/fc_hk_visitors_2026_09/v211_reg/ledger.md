# Evidence ledger: fc_hk_visitors_2026_09

- Question: Assume today is 2026-09-14. You know nothing published after this date. Estimate the total number of visitor arrivals to Hong Kong in September 2026, as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals press release.
- as_of: 2026-09-14
- Pinned target: Total visitor arrivals to Hong Kong (all source markets, worldwide, arrivals counted at immigration/entry, i.e. visitor trips not unique persons) during calendar September 2026, as first reported provisionally by the Hong Kong Tourism Board in its monthly visitor arrivals press release | unit visitor arrivals | period 2026-09-01..2026-09-30 | publisher Hong Kong Tourism Board (HKTB)

- Official value (scoring only, never shown to the agent): 4,031,090

## Directions and pages

### d1 [own_history] HKTB monthly arrivals series

Hypothesis: September 2026 arrivals ≈ September 2025 arrivals × (recent YoY growth trend). September is seasonally lower than summer peak; own history gives level and seasonality.

Queries issued by the searcher: HKTB monthly visitor arrivals September 2025 Hong Kong Tourism Board; Hong Kong visitor arrivals 2026 statistics monthly; 旅發局 2025年9月 訪港旅客 3,047,000 2024年9月 按年; partnernet.hktb.com 旅發局公佈2026年7月初步訪港旅客數字 450萬

- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=4&id=9130` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/research_statistics/latest_statistics/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.discoverhongkong.cn/content/dam/dhk/sc/corporate/newsroom/press-release/hktb/2026/03-Feb-2026-Visitor-Arrivals-C.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Immigration Department / airport and land boundary throughput

Hypothesis: Total arrivals ≈ sum of air, land, sea arrivals; airport passenger and land-crossing (Lo Wu, Lok Ma Chau, HZMB) daily counts constrain the total and give a cross-check.

Queries issued by the searcher: Hong Kong International Airport passenger traffic monthly 2026; Hong Kong Immigration Department daily arrival statistics control points 2026; HKTB visitor arrivals September 2025 monthly press release million visitors; immd.gov.hk passenger-statistics d=20260913 arrivals Mainland visitors other visitors

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20260524` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dailyhongkong.com/wp-content/uploads/2025/10/10-September-Arrivals-E.pdf` -> **snapshot** (snapshot 20251015203835); points raw/verified 15/15
  - p1 Total provisional visitor arrivals to Hong Kong, September 2025 = **3,292,197** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p2 Total provisional visitor arrivals to Hong Kong, September 2025 (rounded, stated = **3,300,000** visitor arrivals (2025-09-01..2025-09-30) [DISCARD: Rounded restatement of p1; redundant.] quote: "provisional visitor arrivals to Hong Kong for September were close to 3.3 million, an 8% increase compared to the same month last year."
  - p3 Year-on-year change in total visitor arrivals to Hong Kong, September 2025 = **8** % (2025-09-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p4 Chinese Mainland visitor arrivals to Hong Kong, September 2025 = **2,458,439** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "Chinese Mainland 2,458,439 (+7%) 27,985,883 (+11%)"
  - p5 Non-Chinese Mainland visitor arrivals to Hong Kong, September 2025 = **833,758** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "Non-Chinese Mainland 833,758 (+9%) 8,485,765 (+16%)"
  - p6 Short-haul visitor arrivals to Hong Kong, September 2025 = **461,889** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "Short-haul 461,889 (+9%) 4,661,848 (+17%)"
  - p7 Long-haul visitor arrivals to Hong Kong, September 2025 = **239,475** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "Long-haul 239,475 (+14%) 2,412,106 (+18%)"
  - p8 New markets visitor arrivals to Hong Kong, September 2025 = **59,196** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "New markets 59,196 (+13%) 535,522 (+14%)"
  - p9 Total provisional visitor arrivals to Hong Kong, January to September 2025 = **36,471,648** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p10 Total visitor arrivals to Hong Kong, first three quarters 2025 (rounded, stated  = **36,000,000** visitor arrivals (2025-01-01..2025-09-30) [DISCARD: Rounded restatement of p9; redundant.] quote: "The preliminary visitor arrivals for the first three quarters of this year stand at over 36 million,"
  - p11 Year-on-year change in total visitor arrivals to Hong Kong, January to September = **12** % (2025-01-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p12 Chinese Mainland visitor arrivals to Hong Kong, January to September 2025 = **27,985,883** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Chinese Mainland 2,458,439 (+7%) 27,985,883 (+11%)"
  - p13 Non-Chinese Mainland visitor arrivals to Hong Kong, January to September 2025 = **8,485,765** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Non-Chinese Mainland 833,758 (+9%) 8,485,765 (+16%)"
  - p14 Short-haul visitor arrivals to Hong Kong, January to September 2025 = **4,661,848** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Short-haul 461,889 (+9%) 4,661,848 (+17%)"
  - p15 Long-haul visitor arrivals to Hong Kong, January to September 2025 = **2,412,106** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Long-haul 239,475 (+14%) 2,412,106 (+18%)"
- `https://www.immd.gov.hk/pdf/sb-e.pdf` -> **snapshot** (snapshot 20240510125523); points raw/verified 15/15
  - p16 Total inbound and outbound passenger trips at all HK control points, 2023 (actua = **211,754,100** as written "211 754 100", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p53; redundant.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p17 Total inbound and outbound passenger trips at all HK control points, 2024 (estim = **289,086,000** as written "289 086 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p54; redundant.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p18 Airport control point inbound and outbound passenger trips, 2023 (actual) = **31,716,381** as written "31 716 381", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p55; redundant.] quote: "Airport 48 997 829 5 709 065 677 108 4 141 363 31 716 381 41 648 000"
  - p19 Airport control point inbound and outbound passenger trips, 2024 (estimate) = **41,648,000** as written "41 648 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p56; redundant.] quote: "Airport 48 997 829 5 709 065 677 108 4 141 363 31 716 381 41 648 000"
  - p20 Lo Wu control point inbound and outbound passenger trips, 2023 (actual) = **45,334,772** as written "45 334 772", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p57; redundant.] quote: "Lo WuNote 3 78 234 223 5 455 893 10 179 0 45 334 772 62 261 000"
  - p21 Lo Wu control point inbound and outbound passenger trips, 2024 (estimate) = **62,261,000** as written "62 261 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p58; redundant.] quote: "Lo WuNote 3 78 234 223 5 455 893 10 179 0 45 334 772 62 261 000"
  - p22 Lok Ma Chau Spur Line control point inbound and outbound passenger trips, 2023 ( = **40,845,069** as written "40 845 069", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p59; redundant.] quote: "Lok Ma Chau Spur LineNote 3 50 156 435 3 516 742 13 955 0 40 845 069 56 095 000"
  - p23 Lok Ma Chau Spur Line control point inbound and outbound passenger trips, 2024 ( = **56,095,000** as written "56 095 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p60; redundant.] quote: "Lok Ma Chau Spur LineNote 3 50 156 435 3 516 742 13 955 0 40 845 069 56 095 000"
  - p24 Hong Kong-Zhuhai-Macao Bridge control point inbound and outbound passenger trips = **21,570,170** as written "21 570 170", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p61; redundant.] quote: "Hong Kong￾Zhuhai-Macao Bridge 19 423 296 1 641 553 122 698 192 883 21 570 170 29 623 000"
  - p25 Hong Kong-Zhuhai-Macao Bridge control point inbound and outbound passenger trips = **29,623,000** as written "29 623 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p62; redundant.] quote: "Hong Kong￾Zhuhai-Macao Bridge 19 423 296 1 641 553 122 698 192 883 21 570 170 29 623 000"
  - p26 West Kowloon Station (Guangzhou-Shenzhen-Hong Kong Express Rail Link) inbound an = **19,653,992** as written "19 653 992", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p27's companion; redundant with p27.] quote: "West Kowloon Station of the Guangzhou￾Shenzhen-Hong Kong Express Rail Link 16 732 428 975 897 0 0 19 653 992 26 992 000"
  - p27 West Kowloon Station (Guangzhou-Shenzhen-Hong Kong Express Rail Link) inbound an = **26,992,000** as written "26 992 000", value check pending passenger trips (2024-01-01..2024-12-31) [keep: ] quote: "West Kowloon Station of the Guangzhou￾Shenzhen-Hong Kong Express Rail Link 16 732 428 975 897 0 0 19 653 992 26 992 000"
  - p28 Heung Yuen Wai BCP designed daily handling capacity (passenger trips per day) = **30,000** as written "30 000", value check pending passenger trips per day (not stated (page dated 2024-04-17)) [DISCARD: Duplicate of p63; redundant.] quote: "the designed daily handling capacity of the Heung Yuen Wai BCP is 30 000 passenger trips"
  - p29 Heung Yuen Wai BCP average daily passenger throughput, 2023 = **34,000** as written "34 000", value check pending passenger trips per day (2023-01-01..2023-12-31) [DISCARD: Duplicate of p64; redundant.] quote: "average daily passenger throughput of about 34 000 in 2023"
  - p30 Total visitor arrivals to Hong Kong (all markets), 2023 = **33,999,660** as written "33 999 660", value check pending visitor arrivals (2023-01-01..2023-12-31) [DISCARD: Duplicate of p65; redundant.] quote: "Total 33 999 660"
- `https://www.hongkongairport.com/en/media-centre/press-release/2026/pr_1865` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Mainland vs non-mainland split

Hypothesis: Total = mainland arrivals + short-haul + long-haul; mainland dominates (~75%). Mainland outbound travel and Shenzhen border crossing data constrain the largest component.

Queries issued by the searcher: mainland visitors Hong Kong monthly arrivals 2026 Hong Kong Tourism Board; 香港旅游发展局 2026年 访港旅客 统计 内地; 旅發局 2025年9月 初步訪港旅客數字 內地; Shenzhen border crossings 2026 daily average Shenzhen Bay Huanggang visitor volumes

- `https://www.workercn.cn/c/2026-08-19/8873317.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=9129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?id=8869` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [capacity_consumption] Hotel occupancy and room supply

Hypothesis: Overnight arrivals ≈ hotel rooms × occupancy × avg stay × persons/room; hotel data constrains overnight segment, which is a stable share of total.

Queries issued by the searcher: Hong Kong hotel occupancy rate 2026 average length of stay overnight visitors; Hong Kong hotel room supply 2026 rooms number HKTB; HKTB September 2025 visitor arrivals overnight visitors average length of stay hotel occupancy; 香港 酒店 入住率 2026年7月 旅發局 過夜旅客

- `https://www.info.gov.hk/gia/general/202604/01/P2026040100340.htm` -> **snapshot** (snapshot 20260416120445); points raw/verified 15/6
  - p31 Hong Kong hotel room supply (number of hotel rooms), as at end-February 2026 = **93,481** as written "93 481", value check pending hotel rooms (2026-02-28..2026-02-28) [keep: ] quote: "截至二○二六年二月底,香港有333間酒店,合共提供93 481間房間,房間數目一直按年上升。"
  - p32 Number of hotels in Hong Kong, as at end-February 2026 = **333** hotels (2026-02-28..2026-02-28) [keep: ] quote: "截至二○二六年二月底,香港有333間酒店,合共提供93 481間房間,房間數目一直按年上升。"
  - p33 Hong Kong hotel occupancy rate during February Mainland Chinese New Year golden  = **90** as written "百分之九十", value check pending % (2026-02-01..2026-02-28) [keep: ] quote: "二月內地春節黃金周期間,酒店入住率更普遍達到百分之九十。"
  - p34 Total visitor arrivals to Hong Kong, first three months of 2026 (cumulative) = **14,310,000** as written "1 431萬", value check pending visitor arrivals (2026-01-01..2026-03-31) [keep: ] quote: "今年旅遊業的發展勢頭持續良好,首三個月訪港旅客為1 431萬人次,按年上升百分之十七"
  - p35 Year-on-year change in total visitor arrivals to Hong Kong, first three months o = **17** as written "百分之十七", value check pending % (2026-01-01..2026-03-31) [keep: ] quote: "首三個月訪港旅客為1 431萬人次,按年上升百分之十七"
  - p36 Proposed threshold for resuming hotel accommodation tax: year-on-year growth in  = **3** as written "百分之三", value check pending % (not stated (page dated 2026-04-01)) [keep: ] quote: "即業內「平均每間可供出租客房收入」按年增幅超過百分之三(即足以抵銷稅項成本水平)為恢復徵稅參考條件"
- `https://www.censtatd.gov.hk/en/web_table.html?id=650-80005&param=N4IgxgbiBcoMJwJqJqAjDEBmAtgBjxABoQB9AF1M0JNIAcro0BfEgNQEkBlAFUQAUAoqhAZo2YmUrVJ9Rnmas` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.colliers.com/download-article?itemId=955bd292-2dc3-48b3-bdbc-2d0dc901690c` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/research_statistics/research_publications/index.html?id=4091` -> **snapshot** (snapshot 20250807193954); points raw/verified 0/0
- dropped by code checks: 9 (period year 2025 does not appear in the page text or URL (likely mis-dated): 6; number: scale conflict: '千萬' in value vs '萬': 1; period_end 2026-12-31 after as_of: 2)

### d5 [forecasts_markets] Official and analyst forecasts

Hypothesis: HKTB/ government full-year 2026 arrival forecasts and growth targets can be apportioned to September using seasonal shares.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast; Hong Kong tourism 2026 target visitor arrivals government forecast; HKTB provisional visitor arrivals September 2025 press release; Hong Kong monthly visitor arrivals 2025 table January February March April May June July August September October November December

- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/japan/jp/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p37 Preliminary total visitor arrivals to Hong Kong, first five months of 2026 (Janu = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [keep: ] quote: "in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://partnernet.hktb.com/usa/en/home/index.html?cat_id=628&doc_id=137528` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d6 [shocks] Calendar, weather, policy effects

Hypothesis: September 2026 has no major holiday (Mid-Autumn timing varies); typhoon season and any visa/policy changes shift arrivals. Adjust trend for calendar and event effects.

Queries issued by the searcher: Mid-Autumn Festival 2026 date September 25; Hong Kong Tourism Board visitor arrivals 2025 monthly statistics September 2025; 旅發局 2026年8月 訪港旅客 初步數字 按年; HKTB provisional visitor arrivals August 2026 Hong Kong million year-on-year

- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bbc.com/newsround/articles/c539memjzkdwo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.mingpao.com/ins/%e6%b8%af%e8%81%9e/article/20260915/s00001/1789443939170/8%e6%9c%88%e5%88%9d%e6%ad%a5%e8%a8%aa%e6%b8%af%e6%97%85%e5%ae%a2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] HKTB monthly arrivals series

Hypothesis: A full monthly HKTB arrivals series for 2024–2026 (especially Jul–Aug 2026 and the 2025 monthly pattern) would let us fit a September seasonal factor and a 2026 YoY growth trend, directly anchoring the level rather than relying on a single September 2025 point.

Queries issued by the searcher: HKTB monthly visitor arrivals press release 2026; partnernet.hktb.com research statistics monthly arrivals visitor arrivals 2025; HKTB September 2025 visitor arrivals 3.29 million up year-on-year; censtatd table 650-80001 visitor arrivals 2026 monthly July August Chinese Mainland total

- `https://www.censtatd.gov.hk/en/web_table.html?id=650-80001&param=N4IgxgbiBcoMJwJqJqAjDEB5ADHkANCAPoAuxmOhJADhdDgL5ECyLqIG0JFRZ9IKnzowmRAEoBRAOIBJLADkO` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=4&id=9130` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Border/airport throughput

Hypothesis: Daily or monthly inbound passenger counts at Lo Wu, Lok Ma Chau, HZMB and HKIA for mid-2026 would constrain the land/air channel totals and provide an independent cross-check on the September 2026 level.

Queries issued by the searcher: Immigration Department Hong Kong statistics control point passenger 2026; HKIA monthly traffic figures 2026 passenger throughput; Hong Kong Tourism Board monthly visitor arrivals statistics July 2026; td.gov.hk Table 8.2 passenger arrivals departures by control point 2026 monthly

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=26` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ttrweekly.com/site/2026/08/passenger-traffic-grows-at-hkia-in-july/` -> **snapshot** (snapshot 20260824035118); points raw/verified 15/15
  - p38 HKIA total passengers handled, July 2026 = **5,620,000** passengers (2026-07-01..2026-07-31) [keep: ] quote: "Hong Kong International Airport (HKIA) handled 5.62 million passengers and 34,230 flight movements in July 2026"
  - p39 HKIA passenger year-on-year increase, July 2026 = **8.4** % (2026-07-01..2026-07-31) [keep: ] quote: "marking year-on-year increases of 8.4% and 1.7% respectively"
  - p40 HKIA flight movements, July 2026 = **34,230** flight movements (2026-07-01..2026-07-31) [keep: ] quote: "34,230 flight movements in July 2026"
  - p41 HKIA flight movements year-on-year increase, July 2026 = **1.7** % (2026-07-01..2026-07-31) [keep: ] quote: "year-on-year increases of 8.4% and 1.7% respectively"
  - p42 HKIA cumulative passenger volume, January–July 2026 = **38,400,000** passengers (2026-01-01..2026-07-31) [keep: ] quote: "Over the first seven months of the year, passenger volume saw 11.2% year-on-year growth to 38.4 million"
  - p43 HKIA passenger volume year-on-year growth, January–July 2026 = **11.2** % (2026-01-01..2026-07-31) [keep: ] quote: "passenger volume saw 11.2% year-on-year growth to 38.4 million"
  - p44 HKIA cumulative flight movements, January–July 2026 = **234,905** flight movements (2026-01-01..2026-07-31) [keep: ] quote: "flight movements increased by 4.0% to 234,905"
  - p45 HKIA flight movements year-on-year growth, January–July 2026 = **4** % (2026-01-01..2026-07-31) [keep: ] quote: "flight movements increased by 4.0% to 234,905"
  - p46 HKIA 12-month rolling passenger volume = **64,800,000** passengers (2025-08-01..2026-07-31) [keep: ] quote: "On a 12-month rolling basis, passenger volume rose by 12.6% year-on-year to 64.8 million"
  - p47 HKIA 12-month rolling passenger volume year-on-year growth = **12.6** % (2025-08-01..2026-07-31) [keep: ] quote: "On a 12-month rolling basis, passenger volume rose by 12.6% year-on-year to 64.8 million"
  - p48 HKIA 12-month rolling flight movements = **403,670** flight movements (2025-08-01..2026-07-31) [keep: ] quote: "flight movements increased by 5.3% to 403,670"
  - p49 HKIA 12-month rolling flight movements year-on-year growth = **5.3** % (2025-08-01..2026-07-31) [keep: ] quote: "flight movements increased by 5.3% to 403,670"
  - p50 HKIA cargo volume, July 2026 = **422,000** tonnes (2026-07-01..2026-07-31) [keep: ] quote: "cargo volume recorded a year-on-year decline of 1.9% to 422,000 tonnes in July 2026"
  - p51 HKIA cumulative cargo throughput, January–July 2026 = **2,920,000** tonnes (2026-01-01..2026-07-31) [keep: ] quote: "driving total cargo throughput over the seven months up 3.2% year on year to 2.92 million tonnes"
  - p52 HKIA 12-month rolling cargo throughput = **5,160,000** tonnes (2025-08-01..2026-07-31) [keep: ] quote: "Over the past 12 months, total cargo throughput grew 3.2% year on year to 5.16 million tonnes"
- `https://www.immd.gov.hk/pdf/sb-e.pdf` -> **snapshot** (snapshot 20240510125523); points raw/verified 15/15
  - p53 Total inbound and outbound passenger trips at all control points, 2023 (actual) = **211,754,100** as written "211 754 100", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p16; redundant.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p54 Total inbound and outbound passenger trips at all control points, 2024 (estimate = **289,086,000** as written "289 086 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p17; redundant.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p55 Airport control point inbound and outbound passenger trips, 2023 = **31,716,381** as written "31 716 381", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p18; redundant.] quote: "Airport 48 997 829 5 709 065 677 108 4 141 363 31 716 381 41 648 000"
  - p56 Airport control point inbound and outbound passenger trips, 2024 (estimate) = **41,648,000** as written "41 648 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p19; redundant.] quote: "Airport 48 997 829 5 709 065 677 108 4 141 363 31 716 381 41 648 000"
  - p57 Lo Wu control point inbound and outbound passenger trips, 2023 = **45,334,772** as written "45 334 772", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p20; redundant.] quote: "Lo WuNote 3 78 234 223 5 455 893 10 179 0 45 334 772 62 261 000"
  - p58 Lo Wu control point inbound and outbound passenger trips, 2024 (estimate) = **62,261,000** as written "62 261 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p21; redundant.] quote: "Lo WuNote 3 78 234 223 5 455 893 10 179 0 45 334 772 62 261 000"
  - p59 Lok Ma Chau Spur Line control point inbound and outbound passenger trips, 2023 = **40,845,069** as written "40 845 069", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p22; redundant.] quote: "Lok Ma Chau Spur LineNote 3 50 156 435 3 516 742 13 955 0 40 845 069 56 095 000"
  - p60 Lok Ma Chau Spur Line control point inbound and outbound passenger trips, 2024 ( = **56,095,000** as written "56 095 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p23; redundant.] quote: "Lok Ma Chau Spur LineNote 3 50 156 435 3 516 742 13 955 0 40 845 069 56 095 000"
  - p61 Hong Kong-Zhuhai-Macao Bridge control point inbound and outbound passenger trips = **21,570,170** as written "21 570 170", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Duplicate of p24; redundant.] quote: "Bridge 19 423 296 1 641 553 122 698 192 883 21 570 170 29 623 000"
  - p62 Hong Kong-Zhuhai-Macao Bridge control point inbound and outbound passenger trips = **29,623,000** as written "29 623 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p25; redundant.] quote: "Bridge 19 423 296 1 641 553 122 698 192 883 21 570 170 29 623 000"
  - p63 Heung Yuen Wai BCP designed daily handling capacity (passenger trips per day) = **30,000** as written "30 000", value check pending passenger trips per day (not stated (page dated 2024-04-17)) [keep: ] quote: "the designed daily handling capacity of the Heung Yuen Wai BCP is 30 000 passenger trips"
  - p64 Heung Yuen Wai BCP average daily passenger throughput, 2023 = **34,000** as written "34 000", value check pending passenger trips per day (2023-01-01..2023-12-31) [keep: ] quote: "average daily passenger throughput of about 34 000 in 2023"
  - p65 Total visitor arrivals to Hong Kong (all markets), 2023 = **33,999,660** as written "33 999 660", value check pending visitor arrivals (2023-01-01..2023-12-31) [DISCARD: Duplicate of p30; redundant.] quote: "Total 33 999 660"
  - p66 Total visitor arrivals to Hong Kong (all markets), 2019 = **55,912,609** as written "55 912 609", value check pending visitor arrivals (2019-01-01..2019-12-31) [keep: ] quote: "Total 55 912 609"
  - p67 Mainland China visitor arrivals to Hong Kong, 2023 = **26,760,453** as written "26 760 453", value check pending visitor arrivals (2023-01-01..2023-12-31) [keep: ] quote: "Mainland China* 26 760 453"

### b3 [forecasts_markets] Official 2026 forecast

Hypothesis: HKTB/government full-year 2026 arrival forecast and any mid-year update would let us apportion to September via seasonal share, resolving the growth-trend uncertainty that dominates the estimate.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast; Hong Kong 2026 visitor arrivals projection government tourism bureau; HKTB provisional visitor arrivals September 2025 3.3 million year-on-year; "August 2026" HKTB provisional visitor arrivals

- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p68 Preliminary total visitor arrivals to Hong Kong, first five months of 2026 (appr = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [DISCARD: Duplicate of p37; redundant.] quote: "According to preliminary figures, in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals - putting us firmly on track to meet our annual forecast."
- `https://partnernet.hktb.com/japan/jp/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://zijing.com.cn/web/article/1532139274674561024/web/content_1532139274674561024.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hong kong tourism', 'visitor arrivals', 'hk tourist']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] Same HKTB September 2025 release: p1 is the precise total, p2 the rounded text version of the same figure, p3 the YoY change for the same month. Not independent — one underlying measurement.
- corroborating: ['p1', 'p4', 'p5'] p4 + p5 = p1 exactly (mainland + non-mainland partition of the same total). Consistent internal decomposition, not independent evidence.
- corroborating: ['p5', 'p6', 'p7', 'p8'] Non-mainland total p5 is the sum of short-haul p6, long-haul p7 and new markets p8; consistent segment split of the same release.
- corroborating: ['p1', 'p9', 'p11'] September 2025 monthly figure and Jan–Sep 2025 cumulative come from the same release; p11 is the cumulative YoY change. Same source, so agreement is not independent confirmation.
- corroborating: ['p9', 'p10'] p10 is the rounded text restatement of p9; redundant copy of the same cumulative figure.
- corroborating: ['p34', 'p35'] Q1 2026 arrivals level and its +17% YoY come from the same government release; internally consistent but one source.
- corroborating: ['p34', 'p37'] Q1 2026 (14.31m, +17%) and Jan–May 2026 (~23m) are consistent with continued strong growth through spring 2026; both government/HKTB-family figures, so shared-source.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] Immigration Department control-point passenger trips (inbound+outbound, all travellers including residents) for 2023 actual and 2024 estimate. Internally consistent table; different definition from vi
- conflicting: ['p28', 'p29'] Heung Yuen Wai designed capacity 30,000/day vs 2023 average throughput ~34,000/day — throughput exceeds design capacity, showing capacity figures are not hard ceilings and cannot be used as realised-a
- corroborating: ['p30', 'p16'] 2023 visitor arrivals (34.0m) vs 2023 total control-point passenger trips (211.8m): the ~6x ratio reflects residents and both-direction counting; consistent order of magnitude, useful only as a sanity
- corroborating: ['p31', 'p32', 'p33'] Hotel room supply, hotel count and peak-period occupancy from the same Feb 2026 government release; occupancy is a holiday-peak figure, not a September average, so it is an upper-bound style input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p3'] Same HKTB September 2025 release: p1 is the level and p3 the +8% YoY change; consistent internally but not independent.
- corroborating: ['p1', 'p4', 'p5', 'p6', 'p7', 'p8'] Components of the same September 2025 HKTB release; p4+p5 and p6+p7+p8 approximately reconcile to p1, confirming internal consistency of the market split. Shared source, so not independent confirmatio
- corroborating: ['p1', 'p9', 'p11'] September 2025 and Jan–Sep 2025 cumulative from the same release; September is a modest share of the 9-month total, consistent with a normal seasonal month.
- corroborating: ['p34', 'p35', 'p37', 'p68'] Q1 2026 (14.31m, +17%) and Jan–May 2026 (~23m) are successive cumulative HKTB/government figures; together they imply a decelerating but still strong 2026 growth trend. p37 and p68 are duplicate state
- corroborating: ['p38', 'p39', 'p42', 'p43', 'p46', 'p47'] HKIA July 2026 and Jan–Jul 2026 passenger growth (+8.4% July, +11.2% YTD, +12.6% rolling) indicate air-channel demand still growing in mid-2026, supporting a positive YoY factor for September 2026.
- corroborating: ['p16', 'p17', 'p53', 'p54', 'p18', 'p19', 'p55', 'p56', 'p20', 'p21', 'p57', 'p58', 'p24', 'p25', 'p61', 'p62', 'p26', 'p27'] Duplicate copies of the same ImmD control-point table (2023 actual, 2024 estimate). They describe passenger trips (inbound+outbound, residents and visitors), not visitor arrivals, so they are contextu
- corroborating: ['p30', 'p65'] Duplicate copies of the 2023 total visitor arrivals figure (33,999,660) from ImmD; a historical anchor only, far from 2026 level.
- corroborating: ['p31', 'p32', 'p33'] Hotel supply (93,481 rooms, 333 hotels) and February 2026 golden-week occupancy (~90%) are from the same government release; they constrain overnight capacity but not total arrivals directly.
- conflicting: ['p63', 'p64'] Heung Yuen Wai designed capacity (30,000/day) is below observed 2023 average throughput (34,000/day); the capacity figure is a design parameter, not a realised-flow constraint, so it should not be use

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth factor vs September 2025 | 1.1 | 1..1.22 | 0.9879..1.235 (widened) | ratio | m1 (m1) | Q1 2026 arrivals grew +17% YoY (p34/p35) and Jan–May 2026 reached ~23m (p37), while HKIA passenger growth moderated to +8.4% in July 2026 (p39) from +11.2% YTD (p43). September 2025 was already a strong base (+8%, p3), so a decelerating but still positive YoY factor around 1.10 is plausible; range s | September 2026 arrivals are forecast from the September 2025 level using the mid-2026 growth trajectory. | Evidence that H2 2026 arrivals growth turned negative (e.g. a reported YoY decline in Jul/Aug 2026 HKTB figures) or accelerated well above +20%. |
| a2 | September 2026 level relative to the Jan–May 2026 monthly average | 1 | 0.9..1.11 | 0.7068..1.414 (widened) | ratio | m2 (m2) | September is a normal, non-peak month with no major holiday (Mid-Autumn timing varies). The September 2025 share of the Jan–Sep 2025 total (p1/p9 ≈ 0.090) is close to the 1/9 average, so September sits near the average month. This factor is a relative-to-average ratio near 1.0, not a monthly share o | Scaling the Jan–May 2026 monthly average run-rate to a September 2026 monthly level. | Evidence of a strong September-specific event (major festival, policy change, or typhoon disruption) pushing September well above or below the average month. |
| a3 | Months spanned by the Jan–May 2026 preliminary arrivals figure | 5 | 5..5 | 3.536..7.071 (widened) | months | m2 (m2) | p37 states arrivals for the first five months of 2026 (January–May). The divisor is the fixed calendar count of months in that stated period, needed to convert the cumulative level to a monthly average; it is a period-length constant, not an empirical estimate. | Converting the Jan–May 2026 cumulative arrivals (p37) to a monthly average. | A restatement of p37 covering a different number of months. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,640,190 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 4,593,892 | ['p37'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **4,089,332** visitor, 80% interval [2,418,236, 6,915,223] visitor, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total visitor arrivals to Hong Kong (all source markets, trips counted at immigration, same-day and overnight) during calendar September 2026, as provisionally reported by the HKTB, is 4,089,332 visitor (80% model-based interval 2,418,236 to 6,915,223 visitor).

Two methods were averaged with weights 50% and 50%. Method [n] anchors on observed September 2025 arrivals of 3,292,197 visitor arrivals and applies an assumed YoY growth factor of 1.1 (range 0.9879 to 1.235). Method [n] divides the observed Jan–May 2026 total of 23,000,000 visitor arrivals by an assumed 5 months and scales by an assumed September-to-average factor of 1 (range 0.7068 to 1.414).

Only the two anchor levels are observed; the growth and seasonal factors are analyst assumptions, and the interval reflects input uncertainty, not demonstrated accuracy. The main risk is a sharper H2 2026 slowdown or acceleration than mid-year data show. Actual July–August 2026 arrivals would most improve the forecast.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth factor vs September 2025: 1.1 ratio, range 0.9879 to 1.235 (range widened by code); used by m1. Overturned by: Evidence that H2 2026 arrivals growth turned negative (e.g. a reported YoY decline in Jul/Aug 2026 HKTB figures) or accelerated well above +[n].
- a2 September 2026 level relative to the Jan–May 2026 monthly average: 1 ratio, range 0.7068 to 1.414 (range widened by code); used by m2. Overturned by: Evidence of a strong September-specific event (major festival, policy change, or typhoon disruption) pushing September well above or below the average month.
- a3 Months spanned by the Jan–May 2026 preliminary arrivals figure: 5 months, range 3.536 to 7.071 (range widened by code); used by m2. Overturned by: A restatement of p37 covering a different number of months.

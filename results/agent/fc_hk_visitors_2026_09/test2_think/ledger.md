# Evidence ledger: fc_hk_visitors_2026_09

- Question: Assume today is 2026-09-14. You know nothing published after this date. Estimate the total number of visitor arrivals to Hong Kong in September 2026, as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals press release.
- as_of: 2026-09-14
- Pinned target: Total visitor arrivals to Hong Kong from all source markets and travel modes, counted as person-trip arrivals of visitors (non-Hong Kong residents, including overnight and same-day visitors) during the calendar month, as the first provisional figure in the Hong Kong Tourism Board monthly visitor arr | unit visitor arrivals (person-trips) | period 2026-09-01..2026-09-30 | publisher Hong Kong Tourism Board (HKTB)

- Official value (scoring only, never shown to the agent): 4,031,090

## Directions and pages

### d1 [own_history] tourism statistician

Hypothesis: September 2026 arrivals can be projected from the latest 2026 monthly run-rate, adjusted by historical September seasonal factors relative to adjacent months and by recent year-on-year growth. Own history constrains both level and seasonality; transfer assumes 2023-2025 September patterns remain informative unless a known shock alters them.

Queries issued by the searcher: Hong Kong Tourism Board monthly visitor arrivals 2026 July August press release; HKTB visitor arrivals September 2025 statistics; "Provisional Visitor Arrivals for July 2026" HKTB 4.5 million first seven months; partnernet.hktb.com visitor arrivals monthly statistics 2026 table January February March April May June July

- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indiaoutbound.info/trade-news/indian-arrivals-in-hong-kong-rise-22-3-pc-to-32416-in-july/` -> **snapshot** (snapshot 20260831150100); points raw/verified 15/15
  - p1 Hong Kong total visitor arrivals, July 2026 = **4,500,000** visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "Hong Kong recorded 4.50 million visitor arrivals in July 2026, up 2.6 pc year-on-year"
  - p2 Hong Kong total visitor arrivals, January-July 2026 cumulative = **31,220,000** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "Total visitor arrivals in Hong Kong increase 11.4 pc to 31.22 million in January-July"
  - p3 Hong Kong overnight visitor arrivals, July 2026 = **1,970,000** overnight visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "Hong Kong recorded 1.97 million overnight visitor arrivals in July, down 3.9 pc year-on-year"
  - p4 Hong Kong cumulative overnight visitor arrivals, January-July 2026 = **13,490,000** overnight visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "cumulative overnight arrivals during January-July increased 1.1 pc to 13.49 million"
  - p5 Hong Kong same-day visitor arrivals, January-July 2026 cumulative = **17,730,000** same-day visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "Same-day arrivals rose 20.7 pc to 17.73 million during the seven-month period."
  - p6 Chinese Mainland visitor arrivals to Hong Kong, January-July 2026 cumulative = **24,160,000** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "arrivals from the Chinese Mainland, the largest market, rose 13.4 pc to 24.16 million"
  - p7 Non-Chinese Mainland visitor arrivals to Hong Kong, January-July 2026 cumulative = **7,050,000** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "non-Chinese Mainland arrivals increased 4.9 pc to 7.05 million"
  - p8 Indian visitor arrivals to Hong Kong, January-July 2026 cumulative = **239,544** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "Indian visitors to Hong Kong stood at 239,544 during January-July this year, up 3 pc year-on-year"
  - p9 Indian visitor arrivals to Hong Kong, July 2026 = **32,416** visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "In July, arrivals from India increased 22.3 pc to 32,416, compared with the same month last year."
  - p10 Indian overnight visitor arrivals to Hong Kong, July 2026 = **20,490** overnight visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "overnight visitors, which increased 40.5 pc to 20,490"
  - p11 Indian same-day visitor arrivals to Hong Kong, July 2026 = **11,926** same-day visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "same-day arrivals edged up 0.1 pc to 11,926"
  - p12 Indian overnight visitor arrivals to Hong Kong, January-July 2026 cumulative = **161,920** overnight visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "overnight arrivals from India rose 11.8 pc to 161,920, compared with 144,838 in the same period last year"
  - p13 Indian overnight visitor arrivals to Hong Kong, January-July 2025 cumulative = **144,838** overnight visitor arrivals (person-trips) (2025-01-01..2025-07-31) [keep: ] quote: "compared with 144,838 in the same period last year"
  - p14 Indian same-day visitor arrivals to Hong Kong, January-July 2026 cumulative = **77,624** same-day visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "Same-day arrivals, however, declined 11.6 pc to 77,624."
  - p15 New markets total visitor arrivals to Hong Kong, January-July 2026 cumulative = **484,932** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "total arrivals increased by 16.3 pc to 484,932 during January-July"
- `https://news.rthk.hk/rthk/en/component/k2/1870067-20260915.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] immigration and transport analyst

Hypothesis: Total visitor arrivals should equal non-Hong Kong resident inbound person-trips across all control points; Immigration Department arrival counts by port/status and HKIA passenger traffic can validate and bridge to HKTB totals. The bridge requires the visitor share of non-resident arrivals and mode shares.

Queries issued by the searcher: Hong Kong Immigration Department arrival statistics 2026 monthly passenger counts by control point; Hong Kong Tourism Board monthly visitor arrivals 2026 statistics; 旅發局 2025年9月 初步訪港旅客數字 萬人次; HKTB visitor arrivals by mode of transport share land air sea 2025

- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=4&id=9130` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.search.gov.hk/viewer.html?url=https%3A%2F%2Fwww.td.gov.hk%2Ffilemanager%2Fen%2Fcontent_5413%2Ftable82.xls` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [capacity_consumption] airline capacity planner

Hypothesis: Air visitor arrivals approximately equal scheduled inbound seat capacity times load factor times visitor share; land and sea visitor arrivals are similarly constrained by cross-boundary transport capacity. Capacity and utilisation bracket the plausible monthly total.

Queries issued by the searcher: Hong Kong International Airport passenger traffic August 2026 load factor; Hong Kong Tourism Board monthly visitor arrivals 2026; HKIA July 2026 passenger traffic flight movements press release; HKTB visitor arrivals by mode of transport air land sea percentage 2025

- `https://www.hongkongairport.com/en/media-centre/press-release/2026/pr_1884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=4&id=9130` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.rthk.hk/rthk/en/component/k2/1870067-20260915.htm?spTabChangeable=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://en.people.cn/n3/2026/0416/c90000-20447215.html` -> **snapshot** (snapshot 20260416094210); points raw/verified 8/8
  - p16 Hong Kong total visitor arrivals, Q1 2026 (first quarter) = **14,310,000** visitor arrivals (2026-01-01..2026-03-31) [keep: ] quote: "Hong Kong recorded around 14.31 million visitor arrivals in the first quarter of 2026, a 17 percent year-on-year increase"
  - p17 Hong Kong total visitor arrivals year-on-year change, Q1 2026 = **17** % (2026-01-01..2026-03-31) [keep: ] quote: "a 17 percent year-on-year increase, the Hong Kong Tourism Board said on Wednesday."
  - p18 Chinese mainland visitor arrivals to Hong Kong, Q1 2026 = **11,080,000** visitor arrivals (2026-01-01..2026-03-31) [keep: ] quote: "Chinese mainland visitor arrivals, the biggest source of arrivals, reached 11.08 million during the period"
  - p19 Chinese mainland visitor arrivals to Hong Kong year-on-year change, Q1 2026 = **20** % (2026-01-01..2026-03-31) [keep: ] quote: "reached 11.08 million during the period, up 20 percent from the same quarter last year"
  - p20 Hong Kong total visitor arrivals, March 2026 = **4,350,000** visitor arrivals (2026-03-01..2026-03-31) [keep: ] quote: "In March alone, the city recorded approximately 4.35 million visitor arrivals, up 14 percent year on year"
  - p21 Hong Kong total visitor arrivals year-on-year change, March 2026 = **14** % (2026-03-01..2026-03-31) [keep: ] quote: "approximately 4.35 million visitor arrivals, up 14 percent year on year, monthly figures indicated."
  - p22 Long-haul market visitor arrivals to Hong Kong, Q1 2026 = **990,000** visitor arrivals (2026-01-01..2026-03-31) [keep: ] quote: "Visitor numbers from long-haul markets rose 19 percent year on year to about 990,000 in the first three months."
  - p23 Long-haul market visitor arrivals to Hong Kong year-on-year change, Q1 2026 = **19** % (2026-01-01..2026-03-31) [keep: ] quote: "Visitor numbers from long-haul markets rose 19 percent year on year to about 990,000 in the first three months."

### d4 [administrative] immigration officer

Hypothesis: Administrative arrival counts for Sep 1-13 2026 can be scaled to full month using day-of-week and holiday patterns plus the same-period share in earlier months; this gives a near-direct partial total. Coverage gap: HKTB may exclude some transit/transfer passengers and residents.

Queries issued by the searcher: Hong Kong visitor arrivals September 2026 HKTB monthly statistics; Hong Kong Immigration Department daily arrival statistics 2026; immd.gov.hk passenger statistics 2026年9月13日 入境 內地訪客 其他訪客; "passenger-statistics" immd.gov.hk d=20260910 機場 入境 香港居民

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html` -> **snapshot** (snapshot 20240705182341); points raw/verified 0/0
- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic` -> **snapshot** (snapshot 20260521200912); points raw/verified 0/0
- `https://partnernet.hktb.com/france/fr/industry_news/hktb_updates/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/pdf/sb-e.pdf` -> **snapshot** (snapshot 20240510125523); points raw/verified 15/13
  - p24 Total inbound and outbound passenger trips at all control points, 2023 (actual) = **211,754,100** as written "211 754 100", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Total inbound+outbound passenger trips including residents, not HKTB visitor arrivals; no 2026 monthly bridge.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p25 Total inbound and outbound passenger trips at all control points, 2024 (estimate = **289,086,000** as written "289 086 000", value check pending passenger trips (2024-01-01..2024-12-31) [DISCARD: Total inbound+outbound passenger trips including residents, not HKTB visitor arrivals; no 2026 monthly bridge.] quote: "Total Note 2 301 264 106 24 207 075 1 951 875 5 295 430 211 754 100 289 086 000"
  - p26 Estimated number of passengers/vehicles/vessels examined by land in 2024 = **252,470,000** as written "252 470 000", value check pending passengers/vehicles/vessels (2024-01-01..2024-12-31) [DISCARD: Mixes passengers, vehicles and vessels; not a visitor-arrival count.] quote: "It is estimated that the number of passengers/vehicles/vessels examined by land in 2024 will be 252 470 000, representing an increase of about 38% over the actual number in 2023."
  - p27 Year-on-year increase in land passengers/vehicles/vessels examined, 2024 estimat = **38** % (2024-01-01..2024-12-31) [DISCARD: Growth rate for mixed passenger/vehicle/vessel examinations, not visitor arrivals.] quote: "representing an increase of about 38% over the actual number in 2023"
  - p28 Inbound and outbound passenger trips at Airport control point, 2023 = **31,716,381** as written "31 716 381", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Airport control-point passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "Airport 48 997 829 5 709 065 677 108 4 141 363 31 716 381 41 648 000"
  - p29 Inbound and outbound passenger trips at Lo Wu control point, 2023 = **45,334,772** as written "45 334 772", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Lo Wu passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "Lo WuNote 3 78 234 223 5 455 893 10 179 0 45 334 772 62 261 000"
  - p30 Inbound and outbound passenger trips at Shenzhen Bay control point, 2023 = **22,685,338** as written "22 685 338", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Shenzhen Bay passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "Shenzhen Bay 38 526 032 3 713 745 836 891 927 608 22 685 338 31 155 000"
  - p31 Inbound and outbound passenger trips at Hong Kong-Zhuhai-Macao Bridge Hong Kong  = **21,570,170** as written "21 570 170", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: HZMB Hong Kong Port passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "Bridge 19 423 296 1 641 553 122 698 192 883 21 570 170 29 623 000"
  - p32 Inbound and outbound passenger trips at West Kowloon Station XRL control point,  = **19,653,992** as written "19 653 992", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: West Kowloon XRL passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "Hong Kong Express Rail Link 16 732 428 975 897 0 0 19 653 992 26 992 000"
  - p33 Inbound and outbound passenger trips at Heung Yuen Wai BCP, 2023 = **12,450,061** as written "12 450 061", value check pending passenger trips (2023-01-01..2023-12-31) [DISCARD: Heung Yuen Wai passenger trips are inbound+outbound and include residents; not comparable to visitor arrivals.] quote: "WaiNotes 3 & 4 - - 10 470 301 12 450 061 17 098 000"
  - p34 Total visitor arrivals to Hong Kong, 2019 (HKTB, by country/territory of residen = **55,912,609** as written "55 912 609", value check pending visitor arrivals (2019-01-01..2019-12-31) [keep: ] quote: "Total 55 912 609"
  - p35 Total visitor arrivals to Hong Kong, 2023 (HKTB, by country/territory of residen = **33,999,660** as written "33 999 660", value check pending visitor arrivals (2023-01-01..2023-12-31) [keep: ] quote: "Total 33 999 660"
  - p36 Mainland China visitor arrivals to Hong Kong, 2023 (HKTB) = **26,760,453** as written "26 760 453", value check pending visitor arrivals (2023-01-01..2023-12-31) [keep: ] quote: "Mainland China* 26 760 453"
- dropped by code checks: 2 (period_end missing or unparseable: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d5 [forecasts_markets] forecaster

Hypothesis: Published 2026 tourism forecasts and HKTB targets can be allocated to September using historical monthly shares; consensus forecasts provide an external level check. Distinguish forecasts and targets from realised outcomes.

Queries issued by the searcher: Hong Kong Tourism Board 2026 visitor arrivals forecast; HKTB 2026 visitor arrivals target 53 million; Hong Kong September 2025 visitor arrivals million HKTB monthly; HKTB monthly visitor arrival report September 2024 2023 statistics

- `https://www.censtatd.gov.hk/en/web_table.html?id=650-80001` -> **snapshot** (snapshot 20260225075742); points raw/verified 0/0
- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p37 Preliminary total visitor arrivals to Hong Kong, first five months of 2026 (appr = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [keep: ] quote: "According to preliminary figures, in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/327072/HKs-2026-tourism-vision-takes-shape-to-diversify-visitor-base-boost-competitiveness` -> **snapshot** (snapshot 20260417023934); points raw/verified 8/2
  - p38 Restaurants recommended in 'Taste. Hong Kong' Gourmet Guide (published January) = **250** restaurants (2026-01-01..2026-01-31) [DISCARD: Restaurant-guide count is irrelevant to visitor arrivals.] quote: "the "Taste. Hong Kong" Gourmet Guide published in January, which covers 250 restaurants recommended by over 50 master chefs"
  - p39 Master chefs recommending restaurants in 'Taste. Hong Kong' Gourmet Guide = **50** master chefs (2026-01-01..2026-01-31) [DISCARD: Chef count is irrelevant to visitor arrivals.] quote: "which covers 250 restaurants recommended by over 50 master chefs, has received an impressive response"
- dropped by code checks: 10 (period_end 2026-12-31 after as_of: 8; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d6 [physical_flow] hotel and accommodation operator

Hypothesis: Overnight visitor arrivals can be inferred from occupied room-nights divided by average length of stay and average visitors per room, with same-day visitors added via historical share. Hotel occupancy and room supply provide a physical constraint on overnight visitor flow.

Queries issued by the searcher: HKTB hotel occupancy room nights 2025 statistics average length of stay overnight visitors; Hong Kong average length of stay visitors 2025 HKTB overnight same-day visitor arrivals; HKTB visitor arrivals 2026 July August monthly provisional statistics hotel occupancy; Hong Kong September 2025 visitor arrivals 3.2 million HKTB monthly

- `https://partnernet.hktb.com/filemanager/sc/content_4925/HK_Tourism_Industry_Snapshot_published_in_Aug_2026_ENSC.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.censtatd.gov.hk/en/web_table.html?id=650-80005&param=N4IgxgbiBcoMJwJqJqAjDEBmAtgBjxABoQB9AF1M0JNIAcro0BfEgNQEkBlAFUQAUAoqhAZo2YmUrVJ9Rnmas` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/home/index.html` -> **snapshot** (snapshot 20260304073602); points raw/verified 0/0
- `https://bmvh162.ust.hk/zh-cn/school-in-media/2026/08/summer-spending-uncertain-despite-major-events-chinese-version-only` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] risk analyst

Hypothesis: Typhoons, border policy, currency and airline disruptions can shift September arrivals from the seasonal baseline; measurable exposure in the first half of the month and forecasts for the remainder should adjust the estimate.

Queries issued by the searcher: Hong Kong typhoon September 2026 signal T8; Hong Kong Observatory tropical cyclone warning September 2026; HKTB visitor arrivals August 2026 provisional figure; Hong Kong visitor arrivals September 2025 HKTB monthly

- `https://www.chinadailyhk.com/hk/article/638800` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.info.gov.hk/gia/wr/202609/03/P2026090300756.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html` -> **snapshot** (snapshot 20240808110150); points raw/verified 13/13
  - p40 Hong Kong visitor arrivals, H1 2024 cumulative total = **21,000,000** visitors (2024-01-01..2024-06-30) [keep: ] quote: "Hong Kong Received 21 Million Visitors in H1 2024 for a 64% Year-on-Year Increase"
  - p41 Hong Kong H1 2024 visitor arrivals year-on-year increase (percentage) = **64** % (2024-01-01..2024-06-30) [keep: ] quote: "Hong Kong Received 21 Million Visitors in H1 2024 for a 64% Year-on-Year Increase"
  - p42 Hong Kong June 2024 provisional visitor arrivals = **3,130,000** visitors (2024-06-01..2024-06-30) [keep: ] quote: "the June provisional visitor arrivals reached 3.13 million, marking a 14% increase year on year."
  - p43 Hong Kong June 2024 visitor arrivals year-on-year increase (percentage) = **14** % (2024-06-01..2024-06-30) [keep: ] quote: "the June provisional visitor arrivals reached 3.13 million, marking a 14% increase year on year."
  - p44 Hong Kong May 2024 provisional visitor arrivals = **3,400,000** visitors (2024-05-01..2024-05-31) [keep: ] quote: "the provisional visitor arrivals for May were 3.4 million, showing a 20% year-on-year increase."
  - p45 Hong Kong May 2024 visitor arrivals year-on-year increase (percentage) = **20** % (2024-05-01..2024-05-31) [keep: ] quote: "the provisional visitor arrivals for May were 3.4 million, showing a 20% year-on-year increase."
  - p46 Hong Kong visitor arrivals first 5 months of 2024 year-on-year increase (percent = **80** % (2024-01-01..2024-05-31) [keep: ] quote: "HKTB Announces an 80% Year-on-Year Increase for Visitor Arrivals of the First 5 Months of 2024"
  - p47 Visitors given travel advice by HKTB frontline team, 2023/24 = **2,000,000** as written "two million", value check pending visitors (2023-04-01..2024-03-31) [DISCARD: Visitors advised by frontline team is an operational contact count, not arrivals.] quote: "In 2023/24, the team provided travel advice to more than two million visitors and resolved more than 2.3 million inquiries."
  - p48 Inquiries resolved by HKTB frontline team, 2023/24 = **2,300,000** inquiries (2023-04-01..2024-03-31) [DISCARD: Inquiries resolved is an operational count, not arrivals.] quote: "In 2023/24, the team provided travel advice to more than two million visitors and resolved more than 2.3 million inquiries."
  - p49 Hong Kong Pals volunteer team size (more than) = **100** volunteers (2024-07-28..2024-07-28) [DISCARD: Volunteer team size is irrelevant to arrivals.] quote: "HKTB Introduces New "Hong Kong Pals" Team with More Than 100 Volunteers after Record High Applications"
  - p50 Summer Triple Rewards sets to be handed out to overnight visitors = **500,000** sets (2024-07-11..2024-07-11) [DISCARD: Reward sets are promotional inventory, not visitor arrivals.] quote: "HKTB will hand out 500,000 sets of "Summer Triple Rewards" to all overnight visitors to Hong Kong."
  - p51 Summer Triple Rewards total offer value (over) = **100,000,000** HKD (2024-07-11..2024-07-11) [DISCARD: Reward value is promotional spend, not visitor arrivals.] quote: "offering all overnight visitors to Hong Kong with 500,000 sets of rewards, with offers in transport / sightseeing, dining and retail totalling over HK$100 million."
  - p52 Asia’s 50 Best Bars 2024 ceremony attendees in Hong Kong (about) = **1,000** people (2024-07-16..2024-07-16) [DISCARD: Bar-event attendees are not a representative visitor-arrival measure.] quote: "The event attracted about 1,000 of the world's bar investors, mixologists and media representatives to Hong Kong"
- `https://www.hk01.com/%E9%A3%9F%E7%8E%A9%E8%B2%B7/60397216/%E6%89%93%E9%A2%A8-%E5%A4%A9%E6%96%87%E5%8F%B0%E6%8F%AD2026%E5%B9%B4%E9%A2%A8%E5%AD%A3%E5%AE` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [attention] tourism marketer

Hypothesis: Search and booking interest for Hong Kong travel in Sep 2026 indicates deviation from the baseline; useful mainly to adjust around events, promotions or shocks. Without a calibrated attention-to-arrivals bridge, use as context rather than direct conversion.

Queries issued by the searcher: Hong Kong hotel bookings September 2026; Hong Kong Tourism Board monthly visitor arrivals 2026; 旅發局 2025年9月 訪港旅客 初步數字 按年; Hong Kong International Airport passenger traffic August 2026 record

- `https://partnernet.hktb.com/france/fr/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/research_statistics/latest_statistics/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://en.people.cn/n3/2026/0416/c90000-20447215.html` -> **snapshot** (snapshot 20260416094210); points raw/verified 8/8
  - p53 Hong Kong total visitor arrivals, Q1 2026 (first quarter cumulative) = **14,310,000** visitor arrivals (person-trips) (2026-01-01..2026-03-31) [DISCARD: Duplicate of p16 Q1 2026 total.] quote: "Hong Kong recorded around 14.31 million visitor arrivals in the first quarter of 2026, a 17 percent year-on-year increase"
  - p54 Hong Kong total visitor arrivals, Q1 2026 year-on-year increase (percent) = **17** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of p17 Q1 2026 growth.] quote: "Hong Kong recorded around 14.31 million visitor arrivals in the first quarter of 2026, a 17 percent year-on-year increase"
  - p55 Chinese mainland visitor arrivals to Hong Kong, Q1 2026 (largest source market) = **11,080,000** visitor arrivals (person-trips) (2026-01-01..2026-03-31) [DISCARD: Duplicate of p18 Q1 2026 Mainland total.] quote: "Chinese mainland visitor arrivals, the biggest source of arrivals, reached 11.08 million during the period"
  - p56 Chinese mainland visitor arrivals to Hong Kong, Q1 2026 year-on-year increase (p = **20** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of p19 Q1 2026 Mainland growth.] quote: "reached 11.08 million during the period, up 20 percent from the same quarter last year"
  - p57 Hong Kong total visitor arrivals, March 2026 (monthly) = **4,350,000** visitor arrivals (person-trips) (2026-03-01..2026-03-31) [DISCARD: Duplicate of p20 March 2026 total.] quote: "In March alone, the city recorded approximately 4.35 million visitor arrivals, up 14 percent year on year"
  - p58 Hong Kong total visitor arrivals, March 2026 year-on-year increase (percent) = **14** % (2026-03-01..2026-03-31) [DISCARD: Duplicate of p21 March 2026 growth.] quote: "approximately 4.35 million visitor arrivals, up 14 percent year on year, monthly figures indicated"
  - p59 Long-haul market visitor arrivals to Hong Kong, Q1 2026 = **990,000** visitor arrivals (person-trips) (2026-01-01..2026-03-31) [DISCARD: Duplicate of p22 Q1 2026 long-haul total.] quote: "Visitor numbers from long-haul markets rose 19 percent year on year to about 990,000 in the first three months."
  - p60 Long-haul market visitor arrivals to Hong Kong, Q1 2026 year-on-year increase (p = **19** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of p23 Q1 2026 long-haul growth.] quote: "Visitor numbers from long-haul markets rose 19 percent year on year to about 990,000 in the first three months."

### b1 [own_history] seasonality calibration

Hypothesis: Observed HKTB September/July ratios for 2023-2025 would replace the main seasonal assumption a1 and validate a3; if September is consistently near 0.85 of July, the current a1 value near 0.92 would be too high.

Queries issued by the searcher: site:partnernet.hktb.com "September 2025" visitor arrivals; HKTB Monthly Report Visitor Arrival Statistics September 2024; HKTB provisional visitor arrivals July 2025 4 million press release; HKTB "July 2023" visitor arrivals 3.6 million provisional

- `https://partnernet.hktb.com/france/fr/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/canada/en/industry_news/hktb_updates/index.html?id=8127` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/press-release/hktb/2023/08-HKTB-Mid-year-Trade-Online-Briefing-E.pdf` -> **snapshot** (snapshot 20231019150852); points raw/verified 15/15
  - p61 HKTB provisional total visitor arrivals to Hong Kong, July 2023 = **3,588,530** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "Total 3,588,530"
  - p62 HKTB preliminary total visitor arrivals to Hong Kong, July 2023 (rounded, stated = **3,600,000** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [DISCARD: Rounded duplicate of p61 (about 3.6 million vs 3,588,530); no additional information.] quote: "the preliminary visitor arrivals in July were about 3.6 million"
  - p63 Month-on-month change in total visitor arrivals, July 2023 vs June 2023 = **31** % (2023-07-01..2023-07-31) [keep: ] quote: "an increase of 31% from the previous month"
  - p64 Average daily visitor arrivals to Hong Kong, July 2023 = **116,000** visitor arrivals per day (2023-07-01..2023-07-31) [keep: ] quote: "The average daily visitor arrivals were 116,000."
  - p65 Cumulative total visitor arrivals to Hong Kong, January–July 2023 = **16,472,409** visitor arrivals (person-trips) (2023-01-01..2023-07-31) [keep: ] quote: "16,472,409"
  - p66 Cumulative total visitor arrivals to Hong Kong, January–July 2023 (rounded, stat = **16,500,000** visitor arrivals (person-trips) (2023-01-01..2023-07-31) [DISCARD: Rounded duplicate of p65 (nearly 16.5 million vs 16,472,409); no additional information.] quote: "nearly 16.5 million visitor arrivals were recorded in the first seven months of this year"
  - p67 Mainland visitor arrivals to Hong Kong, July 2023 = **2,975,902** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "Mainland 2,975,902 13,086,652"
  - p68 Non-Mainland visitor arrivals to Hong Kong, July 2023 = **612,628** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "Non-Mainland* 612,628 3,385,757"
  - p69 Short-haul visitor arrivals to Hong Kong, July 2023 = **306,861** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "Short-haul 306,861 1,658,716"
  - p70 Long-haul visitor arrivals to Hong Kong, July 2023 = **164,746** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "Long-haul 164,746 892,084"
  - p71 New markets visitor arrivals to Hong Kong, July 2023 = **28,613** visitor arrivals (person-trips) (2023-07-01..2023-07-31) [keep: ] quote: "New markets 28,613 154,057"
  - p72 Mainland cumulative visitor arrivals to Hong Kong, January–July 2023 = **13,086,652** visitor arrivals (person-trips) (2023-01-01..2023-07-31) [keep: ] quote: "Mainland 2,975,902 13,086,652"
  - p73 Non-Mainland cumulative visitor arrivals to Hong Kong, January–July 2023 = **3,385,757** visitor arrivals (person-trips) (2023-01-01..2023-07-31) [keep: ] quote: "Non-Mainland* 612,628 3,385,757"
  - p74 Share of all visitors who are overnight visitors, July 2023 (stated as about hal = **0.5** as written "half", value check pending share of visitor arrivals (2023-07-01..2023-07-31) [keep: ] quote: "About half of all visitors are overnight visitors, slightly higher than pre-pandemic levels."
  - p75 Mainland visitor arrivals recovery vs pre-pandemic level, July 2023 = **70** % (2023-07-01..2023-07-31) [keep: ] quote: "followed by Mainland, which has recovered by about 70%"
- `https://www.businesstimes.com.sg/international/hong-kong-september-retail-sales-fall-6-9` -> **snapshot** (snapshot 20260411050945); points raw/verified 8/8
  - p76 HKTB total visitor arrivals, September 2024 = **3,060,000** visitor arrivals (person-trips) (2024-09-01..2024-09-30) [keep: ] quote: "September visitor arrivals stood at 3.06 million, up 10.5 per cent from a year ago period, data from the Hong Kong Tourism Board showed."
  - p77 HKTB total visitor arrivals, August 2024 = **4,450,000** visitor arrivals (person-trips) (2024-08-01..2024-08-31) [keep: ] quote: "That compared with 4.45 million in August and 3.92 million in July."
  - p78 HKTB total visitor arrivals, July 2024 = **3,920,000** visitor arrivals (person-trips) (2024-07-01..2024-07-31) [keep: ] quote: "That compared with 4.45 million in August and 3.92 million in July."
  - p79 HKTB mainland Chinese visitor arrivals, September 2024 = **2,290,000** visitor arrivals (person-trips) (2024-09-01..2024-09-30) [keep: ] quote: "The number of mainland Chinese visitors stood at 2.29 million in September, up 6.1 per cent from the same period in 2023."
  - p80 HKTB mainland Chinese visitor arrivals, August 2024 = **3,660,000** visitor arrivals (person-trips) (2024-08-01..2024-08-31) [keep: ] quote: "That compared to August's 3.66 million and July's 3.14 million."
  - p81 HKTB mainland Chinese visitor arrivals, July 2024 = **3,140,000** visitor arrivals (person-trips) (2024-07-01..2024-07-31) [keep: ] quote: "That compared to August's 3.66 million and July's 3.14 million."
  - p82 HKTB total visitor arrivals year-on-year growth, September 2024 = **10.5** % (2024-09-01..2024-09-30) [keep: ] quote: "September visitor arrivals stood at 3.06 million, up 10.5 per cent from a year ago period, data from the Hong Kong Tourism Board showed."
  - p83 HKTB mainland Chinese visitor arrivals year-on-year growth, September 2024 = **6.1** % (2024-09-01..2024-09-30) [keep: ] quote: "The number of mainland Chinese visitors stood at 2.29 million in September, up 6.1 per cent from the same period in 2023."

### b2 [administrative] near-term run-rate

Hypothesis: Immigration Department daily inbound counts for Sep 1-13 2026, or an August 2026 HKTB provisional total, would anchor the current run-rate and reduce reliance on July/June anchors; this is the closest route to a near-direct partial total.

Queries issued by the searcher: Immigration Department daily passenger statistics September 2026 Hong Kong arrivals; HKTB August 2026 visitor arrivals provisional total; Hong Kong International Airport passenger traffic August 2026 monthly figures; HKTB July 2026 visitor arrivals provisional 3.9 million press release August 2026

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20260911` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/hks/facts/passenger-statistics.html?d=20260901` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/russia/ru/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hongkongairport.com/en/media-centre/press-release/2026/pr_1890` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] bridge and coverage

Hypothesis: A measured ratio of HKTB visitor arrivals to ImmD non-resident inbound trips or HKIA inbound passengers would allow control-point data to validate the total and correct for residents/transit coverage; this would unlock the d2 bridge.

Queries issued by the searcher: ImmD arrival statistics by residency status 2025 2026 Hong Kong resident non-resident; HKTB visitor arrivals methodology transit exclusion same-day visitors; HKTB monthly visitor arrivals 2026 statistics report July 2026; Immigration Department monthly passenger traffic statistics 2026 arrivals Hong Kong residents mainland visitors other visitors table

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html` -> **snapshot** (snapshot 20240705182341); points raw/verified 0/0
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.info.gov.hk/gia/general/202602/13/P2026021300683.htm` -> **snapshot** (snapshot 20260730193140); points raw/verified 15/15
  - p84 Total visitor arrivals to Hong Kong, 2025 (ImmD review) = **49,890,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "The total number of visitor arrivals was around 49.89 million, representing an increase of about 12 per cent as compared with that of 2024"
  - p85 Mainland visitor arrivals to Hong Kong, 2025 = **37,830,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "of which Mainland visitor arrivals were around 37.83 million, representing an increase of about 11 per cent when compared with that of 2024"
  - p86 Other (non-Mainland) visitor arrivals to Hong Kong, 2025 = **12,060,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "the number of arrivals of other visitors was around 12.06 million, representing an increase of about 15 per cent over 2024"
  - p87 Visitor arrivals through Airport Control Point, 2025 = **11,220,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "around 11.22 million visitors travelled through the Airport Control Point"
  - p88 Visitor arrivals through land control points, 2025 = **36,870,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "around 36.87 million visitors and around 1.81 million visitors passed through land control points and sea control points respectively"
  - p89 Visitor arrivals through sea control points, 2025 = **1,810,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "around 36.87 million visitors and around 1.81 million visitors passed through land control points and sea control points respectively"
  - p90 Total passengers through Hong Kong control points (all persons), 2025 = **335,000,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, a total of around 335 million passengers passed through Hong Kong's control points, representing an increase of about 12 per cent over 2024"
  - p91 Year-on-year increase in total control point passengers, 2025 vs 2024 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "a total of around 335 million passengers passed through Hong Kong's control points, representing an increase of about 12 per cent over 2024"
  - p92 Year-on-year increase in total visitor arrivals, 2025 vs 2024 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "The total number of visitor arrivals was around 49.89 million, representing an increase of about 12 per cent as compared with that of 2024"
  - p93 Year-on-year increase in Mainland visitor arrivals, 2025 vs 2024 = **11** % (2025-01-01..2025-12-31) [keep: ] quote: "Mainland visitor arrivals were around 37.83 million, representing an increase of about 11 per cent when compared with that of 2024"
  - p94 Year-on-year increase in other visitor arrivals, 2025 vs 2024 = **15** % (2025-01-01..2025-12-31) [keep: ] quote: "the number of arrivals of other visitors was around 12.06 million, representing an increase of about 15 per cent over 2024"
  - p95 Prior record high of control point passengers, 2019 (300 million level) = **300,000,000** passengers (2019-01-01..2019-12-31) [keep: ] quote: "a new record high surpassing the 300 million level in 2019"
  - p96 Existing e-Channels at HKIA arrival hall to be replaced (from Q1 2026) = **26** e-Channels (2026-01-01..2026-03-31) [DISCARD: e-Channel count at HKIA; infrastructure metric with no calibrated link to visitor arrivals.] quote: "a total of 26 new additional e-Channels will be installed gradually at the arrival hall, and the existing 26 e-Channels will be replaced progressively"
  - p97 New additional e-Channels to be installed at HKIA arrival hall (from Q1 2026) = **26** e-Channels (2026-01-01..2026-03-31) [DISCARD: New e-Channel count at HKIA; same infrastructure metric, not arrivals.] quote: "a total of 26 new additional e-Channels will be installed gradually at the arrival hall, and the existing 26 e-Channels will be replaced progressively"
  - p98 e-Channels at Heung Yuen Wai BCP arrival and departure halls after phase 1 (Sep  = **18** e-Channels (2025-09-01..2025-09-30) [DISCARD: e-Channel count at Heung Yuen Wai BCP; no visitor-arrival content.] quote: "the first phase of the enhancement works at Heung Yuen Wai Boundary Control Point was completed in September 2025, increasing the number of e-Channels to 18 both at the arrival and departure halls"
- `https://partnernet.hktb.com/filemanager/researchpub/ir/ResearchStatistics/paper/Tourism-Rec/TEAIT2019/TEAIT%202019.pdf` -> **snapshot** (snapshot 20240812163154); points raw/verified 15/4
  - p99 HKTB short-haul (excl. Mainland) total visitor arrivals, 2019 calendar year, tho = **7,939,600** visitor arrivals (person-trips) (2019-01-01..2019-12-31) [keep: ] quote: "短途地區市場 (不包括中國內地) 3,356.6 3,313.8 - 1.3 5,934.2 4,620.5 - 22.1 9,301.0 7,939.6 - 14.6 2.9 3.0 + 0.1"
  - p100 HKTB long-haul market total visitor arrivals, 2019 calendar year, thousands = **4,198,300** visitor arrivals (person-trips) (2019-01-01..2019-12-31) [keep: ] quote: "長途地區市場 Long Haul Markets 1,329.2 1,244.7 - 6.4 3,426.6 2,905.2 - 15.2 4,808.3 4,198.3 - 12.7 3.8 3.9 + 0.1"
  - p101 HKTB overnight visitor average length of stay (all markets), 2019, nights = **3.3** nights per overnight visitor (2019-01-01..2019-12-31) [keep: ] quote: "合計 Total 35,773.4 32,037.1 - 10.4 29,262.7 23,752.4 - 18.8 65,147.6 55,912.6 - 14.2 3.1 3.3 + 0.2"
  - p102 HKTB overnight visitor average length of stay (all markets), 2018, nights = **3.1** nights per overnight visitor (2018-01-01..2018-12-31) [keep: ] quote: "合計 Total 35,773.4 32,037.1 - 10.4 29,262.7 23,752.4 - 18.8 65,147.6 55,912.6 - 14.2 3.1 3.3 + 0.2"
- dropped by code checks: 11 (scale word 'thousand' not supported by quote or table header: 9; period_end missing or unparseable: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hong kong tourism', 'visitor arrivals', 'september 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p37'] Same HKTB monthly/cumulative release lineage. Internally consistent: p2≈p4+p5 (13.49m+17.73m) and p2≈p6+p7 (24.16m+7.05m). p37 first-five-months ≈23m fits the p2 Jan-Jul total. July total growth (+2.6
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23'] Q1 and March 2026 HKTB figures reported through en.people.cn. They are internally consistent and establish 2026 level/growth, but not independent of HKTB.
- redundant: ['p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60'] Verbatim/duplicate Q1 and March 2026 figures already represented by p16-p23; no additional measurement.
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45'] 2024 HKTB provisional releases: H1 21m, May 3.4m, June 3.13m are mutually plausible. Older, but useful as level/seasonal anchors when adjusted for 2026 growth.
- corroborating: ['p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] India market internally consistent: July p10+p11≈p9; Jan-Jul p12+p14≈p8. Small market share, so mainly context/validation rather than a direct total driver.
- scope_mismatch: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33'] Immigration Department control-point counts are total inbound+outbound passenger trips (including Hong Kong residents) and some rows mix passengers/vehicles/vessels. They are not HKTB visitor arrivals
- context: ['p34', 'p35', 'p36'] Annual HKTB visitor totals for 2019 and 2023, plus 2023 Mainland subset. Pre-pandemic vs post-reopening levels differ by period; useful only as historical scale, not as a current contradiction.
- irrelevant: ['p38', 'p39', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52'] Promotional, operational, volunteer, restaurant-guide, reward-set and event-attendance counts. They do not measure visitor arrivals and cannot be converted credibly to September 2026 person-trips.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] One HKTB July/Jan-Jul 2026 release via indiaoutbound. Internally coherent: p4+p5=p2, p6+p7=p2 within rounding, p9=p10+p11, p12+p14=p8. Shared source, so not independent confirmation. p1 July total and
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23'] HKTB Q1/March 2026 figures via People's Daily. p16 Q1 and p20 March are consistent subsets of p2 Jan-Jul; p18 Mainland Q1 and p22 long-haul Q1 are market detail. Higher Q1/March growth than Jan-Jul an
- corroborating: ['p37'] Preliminary first five months 2026 about 23M from info.gov.hk. Together with p2 Jan-Jul 31.22M it implies June+July around 8.22M, and with p1 July 4.5M it implies June around 3.72M. Approximate and ea
- corroborating: ['p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75'] HKTB July/Jan-Jul 2023 release. p61 exact total and p62 rounded duplicate; p65 exact cumulative and p66 rounded duplicate; p67+p68=p61; p69+p70+p71 are non-Mainland components. Provides 2023 seasonal 
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83'] Business Times citing HKTB. Sep 2024 total 3.06M, Aug 4.45M, Jul 3.92M; Mainland Sep 2.29M, Aug 3.66M, Jul 3.14M; Sep YoY +10.5%. Strongest direct evidence on September seasonal level relative to July
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] HKTB 2024 monthly/H1 release via partnernet. June 2024 3.13M (+14%), May 3.4M (+20%), H1 21M (+64%), first five months +80%. p42 is used as the June 2024 anchor and compared with p76; not independent 
- corroborating: ['p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95'] 2025 ImmD review via info.gov.hk. p85+p86 approximately p84; p87+p88+p89 approximately p84; annual growth p92 matches p91, with market growths p93/p94. p90 control-point passengers (all persons, 335M)
- contextual: ['p34', 'p35', 'p36', 'p99', 'p100', 'p101', 'p102'] Pre-pandemic/2023 annual totals, 2019 market totals, and average length of stay. Useful for long-run scale and conversion context, but too old or aggregated for direct September 2026 substitution with
- contextual: ['p96', 'p97', 'p98'] e-Channel installation counts at HKIA and Heung Yuen Wai. These are infrastructure indicators, not visitor arrivals, and there is no calibrated e-channel-to-arrival bridge; discarded as irrelevant.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 total visitor arrivals relative to July 2026 | 0.8 | 0.74..0.86 | 0.5641..1.128 (widened) | ratio | m1 (m1) | p76 September 2024 over p78 July 2024 gives ~0.78; the 2023 analogue from p61, p63 and p82 also gives ~0.77. September is post-summer and normally below July. I put the point at 0.80 because July 2026 growth was unusually weak in p1, which depresses this route's denominator. Range covers timing and  | September 2026 follows a normal post-summer pattern without a border, aviation or severe-weather shock, and p1 is a valid same-year pre-season anchor. | Evidence that September 2026 arrivals are far above or below this fraction of July, e.g. a typhoon-driven closure, a new border policy, or a major event shifting September demand. |
| a2 | September 2026 total visitor arrivals relative to June+July 2026 combined | 0.44 | 0.4..0.48 | 0.3098..0.6197 (widened) | ratio | m2 (m2) | p76 September 2024 divided by p42 June 2024 plus p78 July 2024 gives ~0.43; the 2023 analogue from p76/p82, p61/p63 and p61 gives a similar ~0.44. The denominator built from p2 minus p37 inherits p37's approximate nature, which is inside the range. | The 2023-2024 seasonal ratio of September to the June+July block remains representative, and p37 is a usable approximation of first-five-month 2026 arrivals. | September 2026 deviating far from the historical range relative to the June+July block, or evidence that p37 is materially misstated. |
| a3 | September 2026 total visitor arrivals relative to September 2025 | 1.05 | 0.97..1.13 | 0.7403..1.481 (widened) | ratio | m3 (m3) | 2026 growth decelerated from +17% in Q1 (p17) and +14% in March (p21) to +11.4% for Jan-Jul (p2) and +2.6% in July (p1). p84 with p92 shows 2025 annual arrivals about 12% above 2024. I therefore assume September 2026 is modestly above September 2025 rather than another double-digit year. This is a c | Recent deceleration continues and September 2026 YoY growth lands in the low-to-mid single digits. | August/September 2026 data showing renewed double-digit growth or a year-on-year decline outside the stated range. |
| a4 | September 2026 total visitor arrivals relative to June 2024 provisional | 1.18 | 1.08..1.28 | 0.8314..1.663 (widened) | ratio | m4 (m4) | p76 September 2024 is close to p42 June 2024, so September/June seasonality is near one. From June 2024 to September 2026, p84 with p92 gives ~12% for 2025 and p2 gives ~11.4% for Jan-Jul 2026, implying roughly a fifth of cumulative growth; the weak July 2026 growth in p1 argues against the top of t | June 2024 is a valid seasonal base and the 2024-2026 growth path is not structurally broken. | Evidence of a large structural break in 2025-2026 arrivals, or a September/June seasonal ratio far from one. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,600,278 | ['p1'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 3,490,841 | ['p2', 'p37'] / ['a2'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 3,593,383 | ['p76', 'p92'] / ['a3'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 3,670,989 | ['p42'] / ['a4'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **3,588,295** visitor, 80% interval [995,937, 12,928,398] visitor, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total visitor arrivals to Hong Kong (all source markets and travel modes, overnight plus same-day person-trips) for September 2026, as first provisionally reported by HKTB, is 3,588,295 visitor (80% model-based interval 995,937 to 12,928,398 visitor). This is a model-based combination of 4 methods, each weighted 25%; no backtest error was available, so the interval reflects input uncertainty only.

Observed anchors include July 2026 at 4,500,000 visitor arrivals (person-trips), Jan–Jul 2026 cumulative at 31,220,000 visitor arrivals (person-trips), September 2024 at 3,060,000 visitor arrivals (person-trips), and June 2024 at 3,130,000 visitors. Methods scale these by assumed September ratios: 0.8 of July (0.5641–1.128), 0.44 of June+July (0.3098–0.6197), 1.05 year-on-year (0.7403–1.481), and 1.18 of June 2024 (0.8314–1.663).

The main risk is a September-specific shock or a changed seasonal pattern; the most useful missing evidence would be actual September 2026 daily arrivals or a reliable September 2025 level.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 total visitor arrivals relative to July 2026: 0.8 ratio, range 0.5641 to 1.128 (range widened by code); used by m1. Overturned by: Evidence that September 2026 arrivals are far above or below this fraction of July, e.g. a typhoon-driven closure, a new border policy, or a major event shifting September demand.
- a2 September 2026 total visitor arrivals relative to June+July 2026 combined: 0.44 ratio, range 0.3098 to 0.6197 (range widened by code); used by m2. Overturned by: September 2026 deviating far from the historical range relative to the June+July block, or evidence that p37 is materially misstated.
- a3 September 2026 total visitor arrivals relative to September 2025: 1.05 ratio, range 0.7403 to 1.481 (range widened by code); used by m3. Overturned by: August/September 2026 data showing renewed double-digit growth or a year-on-year decline outside the stated range.
- a4 September 2026 total visitor arrivals relative to June 2024 provisional: 1.18 ratio, range 0.8314 to 1.663 (range widened by code); used by m4. Overturned by: Evidence of a large structural break in 2025-2026 arrivals, or a September/June seasonal ratio far from one.

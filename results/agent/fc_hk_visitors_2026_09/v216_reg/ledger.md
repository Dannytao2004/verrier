# Evidence ledger: fc_hk_visitors_2026_09

- Question: Assume today is 2026-09-14. You know nothing published after this date. Estimate the total number of visitor arrivals to Hong Kong in September 2026, as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals press release.
- as_of: 2026-09-14
- Pinned target: Total visitor arrivals to Hong Kong (all source markets, all arrival channels) during September 2026, as first published provisionally by the Hong Kong Tourism Board in its monthly visitor arrivals press release | unit visitor arrivals (person-trips) | period 2026-09-01..2026-09-30 | publisher Hong Kong Tourism Board (HKTB), Monthly Visitor Arrivals press release / tourism statistics

- Official value (scoring only, never shown to the agent): 4,031,090

## Directions and pages

### d1 [own_history] HKTB statistical releases

Hypothesis: September 2026 arrivals ≈ September 2025 arrivals × (recent YoY growth trend). September is a seasonally moderate month (post-summer, pre-October Golden Week). Prior-year September totals and the 2026 monthly YoY growth path anchor the level and trend.

Queries issued by the searcher: HKTB monthly visitor arrivals September 2025 statistics; Hong Kong visitor arrivals 2026 statistics monthly; partnernet.hktb.com "Visitor Arrivals To Hong Kong In July 2026"; 旅發局 2026年7月 初步訪港旅客 450萬人次 按年上升3%; HKTB monthly visitor arrivals September 2025 statistics; Hong Kong visitor arrivals 2026 statistics monthly; 旅發局 2026年7月 初步訪港旅客 450萬 按年上升3%; partnernet.hktb.com Tourism Statistics 2026 monthly visitor arrivals pdf September 2025; HKTB monthly visitor arrivals September 2025 press release; Hong Kong visitor arrivals 2026 statistics monthly; "Visitor Arrivals To Hong Kong In August 2026" HKTB partnernet; 旅發局 2026年7月 初步訪港旅客 450萬人次 按年上升3%

- `https://partnernet.hktb.com/en/research_statistics/latest_statistics/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/tourisum-statistics/2026/tourism_stat_06_2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/314146/HK-sees-sustained-tourism-growth-with-33m-visitors-in-September` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=5&print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3367569/hong-kong-visitor-arrivals-hit-post-pandemic-monthly-high-august` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/press-release/hktb/2026/04-Mar-2026-Visitor-Arrivals-E.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/filemanager/LatestStatistics/1121/Tourism_Statistics_08_2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nordot.app/1353658222707556815` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nordot.app/1353658222707556815?c=428427385053398113` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/filemanager/LatestStatistics/1101/Tourism_Statistics_07_2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.mingpao.com/ins/%e6%b8%af%e8%81%9e/article/20260817/s00001/1786952150238/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Immigration Department / airport authority

Hypothesis: Total arrivals can be built from entry-channel components: land (Lo Wu, Lok Ma Chau, Shenzhen Bay, HK-Zhuhai-Macau Bridge), air (HKIA), sea. Sum of channel passenger throughput × visitor share ≈ total visitor arrivals. Early-September daily figures constrain the month.

Queries issued by the searcher: Immigration Department daily passenger arrivals statistics 2026 Hong Kong control points; Hong Kong airport passenger traffic September 2026; Hong Kong Tourism Board monthly visitor arrivals August 2026 press release; HKTB visitor arrivals September 2025 monthly statistics; Immigration Department daily passenger arrivals statistics 2026 Hong Kong control points; Hong Kong airport passenger traffic September 2026; HKTB monthly visitor arrivals August 2026 press release statistics; 旅發局 2026年8月 訪港旅客 人數 統計; Immigration Department daily passenger arrivals by control point September 2026; 香港 入境事務處 各口岸 入境人次 2026年9月; immd.gov.hk passenger-statistics d=20260913 入境 機場 羅湖 內地訪客; 旅發局 2026年8月 訪港旅客 初步數字 按年升

- `https://everything.hk/en/population/passenger-traffic` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=26` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic/resource/e06a2a45-fe05-4eb4-9302-237d74343d52` -> **snapshot** (snapshot 20260312141129); points raw/verified 0/0
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news.gov.hk/eng/2026/03/20260331/20260331_170206_334.html` -> **snapshot** (snapshot 20260720153425); points raw/verified 8/8
  - p1 Immigration Department estimate of total passengers through Hong Kong sea, land  = **6,440,000** passenger (2026-04-03..2026-04-07) [keep: ] quote: "around 6.44 million passengers will pass through Hong Kong's sea, land and air control points during the upcoming Easter and Ching Ming festive period from April 3 to 7"
  - p2 Immigration Department estimate of passengers through land boundary control poin = **5,430,000** passenger (2026-04-03..2026-04-07) [keep: ] quote: "around 5.43 million passengers will pass through land boundary control points"
  - p3 Anticipated passengers using land boundary control points on April 3 (peak outbo = **712,000** passenger (2026-04-03..2026-04-03) [keep: ] quote: "highest on April 3 and April 7, with around 712,000 passengers and 671,000 passengers anticipated on those days respectively"
  - p4 Anticipated passengers using land boundary control points on April 7 (peak outbo = **671,000** passenger (2026-04-07..2026-04-07) [keep: ] quote: "highest on April 3 and April 7, with around 712,000 passengers and 671,000 passengers anticipated on those days respectively"
  - p5 Forecast daily average passengers at Lo Wu Control Point during festive period = **240,000** passenger (2026-04-03..2026-04-07) [keep: ] quote: "daily average forecasts of about 240,000, 220,000 and 184,000 passengers respectively"
  - p6 Forecast daily average passengers at Lok Ma Chau Spur Line Control Point during  = **220,000** passenger (2026-04-03..2026-04-07) [keep: ] quote: "daily average forecasts of about 240,000, 220,000 and 184,000 passengers respectively"
  - p7 Forecast daily average passengers at Shenzhen Bay Control Point during festive p = **184,000** passenger (2026-04-03..2026-04-07) [keep: ] quote: "daily average forecasts of about 240,000, 220,000 and 184,000 passengers respectively"
  - p8 New e-channels installed at HKIA arrival hall (capacity addition) = **12** e-channel (not stated (page dated 2026-03-31)) [DISCARD: E-channel count is a capacity addition, not a flow; unusable for arrivals.] quote: "12 additional new e-channels, equipped with the "Face Easy e-Channel" function, were installed at the Hong Kong International Airport arrival hall today"
- `https://www.ceicdata.com/en/hong-kong/departures-passenger-by-control-point/pd-control-point-heung-yuen-wai` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.search.gov.hk/viewer.html?url=https%3A%2F%2Fwww.news.gov.hk%2Feng%2F2026%2F03%2F20260331%2F20260331_170206_334.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hongkongairport.com/en/media-centre/press-release/2026/pr_1894` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.visahq.news/2026-07-23/hk/daily-passenger-traffic-data-show-record-summer-surge-across-hong-kong-control-points/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/324789/Over-682000-passenger-trips-recorded-by-Lunar-New-Year-Day-3` -> **snapshot** (snapshot 20260308162646); points raw/verified 0/0
- `https://www.thestandard.com.hk/news/article/324498/LNY-travel-rush-221000-crossings-by-10am-airport-busiest-checkpoint` -> **snapshot** (snapshot 20260308164511); points raw/verified 0/0
- `https://www.fedhotelowners.com.hk/en/industry-information/special-traffic-and-transport-arrangements-during-the-national-day-golden-week-1-7-october-2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [capacity_consumption] Airlines and hotels

Hypothesis: Air arrivals ≈ seat capacity into HKIA × load factor × visitor share. Hotel occupancy and bookings for September 2026 give a demand signal. Capacity × utilisation bounds the air component.

Queries issued by the searcher: HKIA seat capacity September 2026 forecast; Hong Kong hotel occupancy September 2026 forecast; Hong Kong air passenger forecast 2026 HKIA; HKIA monthly traffic August 2026 passenger throughput; Cathay Pacific August 2026 traffic passengers load factor; Hong Kong hotel occupancy 2026 forecast CBRE JLL; HKTB visitor arrivals August 2026 statistics; HKIA seat capacity September 2026; Hong Kong hotel occupancy forecast 2026; Hong Kong International Airport passenger traffic August 2026 monthly figures; OAG Hong Kong airport scheduled seats September 2026 capacity outlook; HKIA seat capacity September 2026; Hong Kong airport passenger traffic 2026 forecast; HKTB monthly visitor arrivals 2026 statistics July August; Hong Kong International Airport August 2026 passenger traffic million

- `https://hongkongbusiness.hk/aviation/news/hkia-rises-8th-busiest-intl-airport-remains-14-below-2019-capacity` -> **snapshot** (snapshot 20260517030801); points raw/verified 15/15
  - p9 HKIA annual scheduled seat capacity, 2025 (OAG World's Busiest Airports) = **38,700,000** seat (2025-01-01..2025-12-31) [keep: ] quote: "The Hong Kong International Airport recorded the largest year-on-year increase in capacity amongst the busiest international airports, with 38.7 million seats in 2025."
  - p10 HKIA annual seat capacity year-on-year growth, 2025 vs 2024 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "According to travel data platform OAG's World's Busiest Airports of 2025, this reflects a 12% increase from last year, improving its ranking to eighth place from ninth in 2024."
  - p11 HKIA seat capacity shortfall vs 2019 level, 2025 = **14** % (2025-01-01..2025-12-31) [keep: ] quote: "Despite this strong recovery, it remains 14% below 2019 capacity levels."
  - p12 Dubai International Airport international seats, 2025 (rank 1) = **62,400,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airports' seat counts irrelevant to Hong Kong arrivals.] quote: "The Dubai International Airport led the 2025 list of the world's busiest international airports, with 62.4 million international seats, maintaining its long-standing lead from 2024, 2023 and 2019."
  - p13 London Heathrow Airport international seats, 2025 (rank 2) = **49,000,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "London Heathrow Airport followed with 49.0 million international seats, up 1% compared to 2024 and 4% above 2019 levels."
  - p14 London Heathrow international seats year-on-year growth, 2025 vs 2024 = **1** % (2025-01-01..2025-12-31) [DISCARD: Other airport growth irrelevant.] quote: "London Heathrow Airport followed with 49.0 million international seats, up 1% compared to 2024 and 4% above 2019 levels."
  - p15 London Heathrow international seats vs 2019 level, 2025 = **4** % (2025-01-01..2025-12-31) [DISCARD: Other airport vs-2019 irrelevant.] quote: "London Heathrow Airport followed with 49.0 million international seats, up 1% compared to 2024 and 4% above 2019 levels."
  - p16 Seoul Incheon International Airport seats, 2025 (rank 3) = **43,000,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "Seoul Incheon International Airport remained third with 43.0 million seats, a 3% increase compared to 2024 and now 2% above 2019 levels, signalling a full recovery in international travel at the airpo"
  - p17 Seoul Incheon seats year-on-year growth, 2025 vs 2024 = **3** % (2025-01-01..2025-12-31) [DISCARD: Other airport growth irrelevant.] quote: "Seoul Incheon International Airport remained third with 43.0 million seats, a 3% increase compared to 2024 and now 2% above 2019 levels, signalling a full recovery in international travel at the airpo"
  - p18 Seoul Incheon seats vs 2019 level, 2025 = **2** % (2025-01-01..2025-12-31) [DISCARD: Other airport vs-2019 irrelevant.] quote: "ul Incheon International Airport remained third with 43.0 million seats, a 3% increase compared to 2024 and now 2% above 2019 levels, signalling a full recovery in international travel at the airport."
  - p19 Singapore Changi Airport seats, 2025 (rank 4) = **42,600,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "The Singapore Changi Airport ranked fourth, with 42.6 million seats, a 3% year-on-year increase, bringing capacity back in line with 2019 levels."
  - p20 Istanbul Airport international seats, 2025 (rank 5) = **41,200,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "Meanwhile, the Istanbul Airport reached 41.2 million international seats, a 7% increase from 2024. This saw the largest growth compared to 2019, up 27%."
  - p21 Istanbul Airport seats vs 2019 level, 2025 = **27** % (2025-01-01..2025-12-31) [DISCARD: Other airport vs-2019 irrelevant.] quote: "Meanwhile, the Istanbul Airport reached 41.2 million international seats, a 7% increase from 2024. This saw the largest growth compared to 2019, up 27%."
  - p22 Frankfurt Airport seats, 2025 (rank 9) = **36,400,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "Ranking ninth and tenth are the Frankfurt and Doha airports, with 36.4 million seats and 32.7 million seats, respectively."
  - p23 Doha Airport seats, 2025 (rank 10) = **32,700,000** seat (2025-01-01..2025-12-31) [DISCARD: Other airport seats irrelevant.] quote: "Ranking ninth and tenth are the Frankfurt and Doha airports, with 36.4 million seats and 32.7 million seats, respectively."
- `https://theasiansun.com/hong-kong-international-airport-opens-terminal-2-in-push-to-reach-100-million-passengers/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://threerunwaysystem.hongkongairport.com/media/1290/iata.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://threerunwaysystem.hongkongairport.com/media/1277/tr_24may_eng_contents.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://threerunwaysystem.hongkongairport.com/media/1280/tr_24may_eng_ch3.pdf` -> **snapshot** (snapshot 20251206084136); points raw/verified 15/14
  - p24 HKIA North Runway (arrivals only) potential runway capacity, movements per hour = **33** movements per hour (not stated (page dated 2011-05-24)) [DISCARD: Runway movement capacity, not passenger flow; unusable without a full conversion chain.] quote: "North Runway (Arrivals Only) 3 NM * 33 per hour"
  - p25 HKIA South Runway (departures only) potential runway capacity, movements per hou = **35** movements per hour (not stated (page dated 2011-05-24)) [DISCARD: Runway movement capacity, not passenger flow.] quote: "South Runway (Departures Only) 90 seconds ** 35 per hour"
  - p26 HKIA single runway declared capacity during night-time single runway period, mov = **37** movements per hour (not stated (page dated 2011-05-24)) [DISCARD: Runway movement capacity, not passenger flow.] quote: "the current declared capacity of a single runway at HKIA is 37 movements per hour"
  - p27 HKIA theoretical maximum movements per day (8 x 37 + 16 x 68) = **1,384** movements per day (not stated (page dated 2011-05-24)) [DISCARD: Theoretical movement maximum, not realised passengers.] quote: "a maximum of 1,384 (8 x 37 + 16 x 68) movements per day is possible in theory"
  - p28 HKIA design daily movement profile, movements per day = **1,200** movements per day (not stated (page dated 2011-05-24)) [DISCARD: Design movement profile, not realised passengers.] quote: "the above design day profile to be scaled to a daily movement profile of 1,200 movements"
  - p29 HKIA achievable daily capacity range, movements per day (lower bound) = **1,100** movements per day (not stated (page dated 2011-05-24)) [DISCARD: Capacity bound, not realised flow.] quote: "a daily capacity in the range of 1,100 to 1,200 movements is achievable"
  - p30 HKIA achievable daily capacity range, movements per day (upper bound) = **1,200** movements per day (not stated (page dated 2011-05-24)) [DISCARD: Capacity bound, not realised flow.] quote: "a daily capacity in the range of 1,100 to 1,200 movements is achievable"
  - p31 HKIA historical design day/annual ratio = **0.0029** 1 (not stated (page dated 2011-05-24)) [DISCARD: Design ratio, not a flow.] quote: "Applying the historical design day/annual ratio of 0.0029"
  - p32 HKIA annual capacity range from daily capacity, movements per year (lower bound) = **379,310** movements per year (not stated (page dated 2011-05-24)) [DISCARD: Derived capacity, not realised flow.] quote: "this would provide an annual capacity in the range of 379,310 to 413,793 movements"
  - p33 HKIA annual capacity range from daily capacity, movements per year (upper bound) = **413,793** movements per year (not stated (page dated 2011-05-24)) [DISCARD: Derived capacity, not realised flow.] quote: "this would provide an annual capacity in the range of 379,310 to 413,793 movements"
  - p34 HKIA ultimate practical maximum annual ATM capacity, two-runway system, movement = **420,000** movements per year (not stated (page dated 2011-05-24)) [DISCARD: Ultimate capacity, not realised flow.] quote: "420,000 can be assumed to be the ultimate practical maximum annual ATM capacity if HKIA stays with the two-runway system"
  - p35 HKIA design day (24 Aug 2007) total air traffic movements = **863** movements per day (2007-08-24..2007-08-24) [DISCARD: 2007 design-day movements, irrelevant to 2026 visitors.] quote: "Total Movement 23 14 9 20 6 13 8 17 32 43 53 54 48 58 50 53 53 45 44 48 45 43 45 39 863"
  - p36 HKIA design day (24 Aug 2007) arrival movements = **432** movements per day (2007-08-24..2007-08-24) [DISCARD: 2007 design-day movements, irrelevant.] quote: "Arrival Movement 11 7 2 6 3 8 8 12 8 18 27 30 20 30 29 25 21 26 23 21 23 28 32 14 432"
  - p37 HKIA passengers travelling via land or sea to/from PRD, 2009 = **2,800,000** passengers per year (2009-01-01..2009-12-31) [DISCARD: 2009 PRD land/sea transfer passengers, too old and wrong scope.] quote: "In 2009, HKIA served about 2.8 million passengers travelling via land or sea to and from the PRD"
- `https://bm.hkust.edu.hk/zh-hk/school-in-media/2026/08/summer-spending-uncertain-despite-major-events-chinese-version-only` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://airserviceone.com/hong-kongs-q3-capacity-up-7-united-airlines-joins-top-10-143-destinations-served/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://orientaviation.com/articles/15632` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ebook.hkcd.com.hk/PC/content/202606/14/content_3455398.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3351196/hong-kong-airports-revenue-expected-grow-10-despite-mideast-war` -> **snapshot** (snapshot 20260423124001); points raw/verified 3/3
  - p38 Hong Kong International Airport expected passenger throughput, current year (sta = **70,000,000** passenger (not stated (page dated 2026-04-23)) [keep: ] quote: "Hong Kong airport was expected to welcome about 70 million passengers this year"
  - p39 Hong Kong International Airport passenger throughput, last year (prior year), ac = **61,000,000** passenger (not stated (page dated 2026-04-23)) [keep: ] quote: "an increase from around 61 million last year"
  - p40 Airport Authority Hong Kong expected revenue growth, current year, upper bound o = **10** % (not stated (page dated 2026-04-23)) [DISCARD: Airport revenue growth, not arrivals.] quote: "expects revenue to grow by up to 10 per cent this year"
- `https://dev.theedgemalaysia.com/author/Julia%20Zhong?page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.atkinsrealis.com/~/media/Files/A/atkinsrealis/download-centre/en/mp2030-full-en.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d4 [forecasts_markets] HKTB and government forecasts

Hypothesis: HKTB or government full-year 2026 visitor arrival targets/forecasts, if published before cutoff, can be decomposed into months using historical monthly shares to yield a September estimate.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast full year target; 旅發局 2026 全年 訪港旅客 預測; HKTB monthly visitor arrivals September 2025 statistics 3.2 million; 旅發局 2025年9月 訪港旅客 數字 按月 統計; HKTB 2026 visitor arrivals forecast target; 旅發局 2026 全年 訪港旅客 預測; 旅發局 2025年9月 訪港旅客 約 萬人次 按年; HKTB monthly visitor arrivals September 2025 statistics 3.2 million; HKTB 2026 visitor arrivals forecast target full year; 旅發局 2026 全年 訪港旅客 預測; Hong Kong tourism 2026 full year forecast visitor arrivals; HKTB monthly visitor arrivals September 2025 statistics

- `https://sc.isd.gov.hk/gb/www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bau.com.hk/web/article/1532139274674561024/web/content_1532139274674561024.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tvb.com/tc/1190651-%E9%A6%96%E4%B8%83%E5%80%8B%E6%9C%88%E9%8C%843100%E8%90%AC%E5%90%8D%E6%97%85%E5%AE%A2%E8%A8%AA%E6%B8%AF%E7%BE%85%E6%B7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stheadline.com/society/3540735/%e7%be%85%e6%b7%91%e4%bd%a9%e6%9c%89%e4%bf%a1%e5%bf%83%e4%bb%8a%e5%b9%b4%e6%97%85%e5%ae%a2%e4%ba%ba%e6%ac%a` -> **snapshot** (snapshot 20260204075019); points raw/verified 5/3
  - p41 HKTB/Government 2026 full-year visitor arrivals forecast (Secretary for Culture, = **50,000,000** visitor arrivals (2026-01-01..2026-12-31) [keep: ] quote: "有信心2026年全年訪港旅客突破5000萬人次"
  - p42 Hong Kong hotel rooms currently available (capacity, all hotels) = **94,000** hotel rooms (2026-02-01..2026-02-01) [DISCARD: Hotel room capacity, not arrivals; no occupancy bridge supplied.] quote: "現時全港約有9.4萬酒店房間"
  - p43 Mainland Spring Festival Golden Week length (days) = **8.5** (range 8..9) as written "8至9天", value check pending days (not stated (page dated 2026-02-01)) [DISCARD: Spring Festival length, irrelevant to September.] quote: "內地春節黃金周長達8至9天"
- `https://e.vnexpress.net/news/travel/places/world-s-second-most-visited-city-welcomes-4-million-tourists-in-september-5132677.html?vn_source=Detail&vn_` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/327072/HKs-2026-tourism-vision-takes-shape-to-diversify-visitor-base-boost-competitiveness` -> **snapshot** (snapshot 20260417023934); points raw/verified 8/8
  - p44 Hong Kong 2026 visitor arrival target (all source markets, all channels), stated = **53,800,000** visitor arrivals (2026-01-01..2026-12-31) [keep: ] quote: "The city aims to attract 53.8 million visitors-an 8 percent rise on 2025-and Law is confident the target is attainable"
  - p45 Year-on-year rise in 2026 visitor arrival target versus 2025 = **8** % (2026-01-01..2026-12-31) [keep: ] quote: "The city aims to attract 53.8 million visitors-an 8 percent rise on 2025-and Law is confident the target is attainable"
  - p46 Share of HKTB promotional resources deployed to international markets (2026) = **75** % (2026-01-01..2026-12-31) [DISCARD: Promotional resource share, not arrivals.] quote: "The plan includes reallocating promotional resources, with 75 percent deployed to international markets."
  - p47 Share of HKTB promotional resources targeting the mainland market (2026) = **25** % (2026-01-01..2026-12-31) [DISCARD: Promotional resource share, not arrivals.] quote: "The remaining 25 percent will target the mainland market, focusing on non‐Guangdong cities to boost overnight arrivals."
  - p48 Number of flagship events HKTB will stage (2026) = **6** as written "six", value check pending events (2026-01-01..2026-12-31) [DISCARD: Event count, not arrivals.] quote: "HKTB said it will stage six flagship events and will expand its scale and promotional efforts"
  - p49 Restaurants covered by the January "Taste. Hong Kong" Gourmet Guide = **250** restaurants (2026-01-01..2026-01-31) [DISCARD: Restaurant count, not arrivals.] quote: "the "Taste. Hong Kong" Gourmet Guide published in January, which covers 250 restaurants recommended by over 50 master chefs"
  - p50 Master chefs recommending restaurants in the Gourmet Guide (stated as over 50) = **50** master chefs (2026-01-01..2026-01-31) [DISCARD: Chef count, not arrivals.] quote: "which covers 250 restaurants recommended by over 50 master chefs, has received an impressive response"
  - p51 Number of districts to be covered by HKTB themed travel guides = **18** districts (2026-01-01..2026-12-31) [DISCARD: District count, not arrivals.] quote: "The Board plans to release more themed travel guides covering all 18 districts."
- `https://epaper.tkww.hk/a/202607/17/AP6a593eece4b04773b072818d.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ttgchina.com/2026/06/03/%e9%a6%99%e6%b8%af%e7%aa%81%e6%98%be%e6%96%87%e4%bd%93%e7%9b%9b%e4%ba%8b%e4%bc%98%e5%8a%bf-%e6%8f%90%e5%8d%87%e5%85%a8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bastillepost.com/global/article/5920570-scst-highlighting-hong-kongs-tourism-growth-at-2026-hong-kong-tourism-development-forum-opening-di` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/korea/kr/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=true&gvHelperp=2&id=7008` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/314146/HK-sees-sustained-tourism-growth-with-33m-visitors-in-September` -> **snapshot** (snapshot 20260812235344); points raw/verified 13/0
- `https://news.rthk.hk/rthk/en/component/k2/1827331-20251015.htm` -> **snapshot** (snapshot 20251015110247); points raw/verified 12/12
  - p52 Total visitor arrivals to Hong Kong, first three quarters of 2025 (preliminary) = **36,000,000** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p53 Year-on-year growth in total visitor arrivals to Hong Kong, first three quarters = **12** % (2025-01-01..2025-09-30) [keep: ] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p54 Visitor arrivals to Hong Kong from non-mainland markets, first three quarters of = **8,500,000** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "the number of inbound travellers from places other than the mainland, which stood at about 8.5 million during the period, up 16 percent year on year."
  - p55 Year-on-year growth in non-mainland visitor arrivals to Hong Kong, first three q = **16** % (2025-01-01..2025-09-30) [keep: ] quote: "which stood at about 8.5 million during the period, up 16 percent year on year."
  - p56 Mainland visitor arrivals to Hong Kong, first three quarters of 2025 (preliminar = **28,000,000** visitor arrivals (2025-01-01..2025-09-30) [keep: ] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p57 Mainland share of total visitor arrivals to Hong Kong, first three quarters of 2 = **78** % (2025-01-01..2025-09-30) [keep: ] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p58 Year-on-year growth in mainland visitor arrivals to Hong Kong, first three quart = **11** % (2025-01-01..2025-09-30) [keep: ] quote: "accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p59 Total visitor arrivals to Hong Kong, September 2025 (preliminary) = **3,300,000** visitor arrivals (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year"
  - p60 Year-on-year growth in total visitor arrivals to Hong Kong, September 2025 = **8** as written "eight percent", value check pending % (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year"
  - p61 Year-on-year growth in long-haul market visitor arrivals to Hong Kong, September = **14** % (2025-09-01..2025-09-30) [keep: ] quote: "with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p62 Year-on-year growth in short-haul market visitor arrivals to Hong Kong, Septembe = **9** % (2025-09-01..2025-09-30) [keep: ] quote: "with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p63 Year-on-year growth in new market visitor arrivals to Hong Kong, September 2025 = **13** % (2025-09-01..2025-09-30) [keep: ] quote: "Travellers from new markets grew by 13 percent in September, compared to the same period last year."
- dropped by code checks: 15 (period year 2029 does not appear in the page text or URL (likely mis-dated): 1; number: low/high given but value_as_written is not a range: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 13)

### d5 [base_rates] Source-market mix

Hypothesis: Total = sum over source markets (Mainland China, short-haul, long-haul) of arrivals; each market's September 2026 level ≈ its September 2025 level × market-specific growth. Mainland share and its trend dominate.

Queries issued by the searcher: HKTB monthly visitor arrivals 2026 Mainland share; 香港旅遊發展局 2026年 訪港旅客 內地 統計; HKTB September 2025 provisional visitor arrivals 3.3 million Mainland year-on-year; 旅發局 2026年7月 初步訪港旅客數字 短途 長途; HKTB monthly visitor arrivals 2026 Mainland China share; Hong Kong visitor arrivals September 2025 3.2 million Mainland; HKTB provisional visitor arrivals August 2026 year-on-year; 旅發局 2026年7月 訪港旅客 初步數字 內地 按年; HKTB monthly visitor arrivals 2026 Mainland China short-haul long-haul; 香港旅遊發展局 2026 訪港旅客 統計 內地; HKTB provisional visitor arrivals September 2025 3.3 million Mainland short-haul long-haul; 旅發局 2025年9月 訪港旅客 初步 數字 內地 短途 長途

- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=8869` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://zijing.com.cn/web/article/1428026818736693248/web/content_1428026818736693248.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/japan/jp/industry_news/hktb_updates/index.html?id=8948` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?id=9129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stheadline.com/society/3594314/%e6%97%85%e7%99%bc%e5%b1%80%e4%b8%8a%e5%8d%8a%e5%b9%b4%e8%a8%aa%e6%b8%af%e6%97%85%e5%ae%a2%e5%a2%9e13%e9%81` -> **snapshot** (snapshot 20260723113601); points raw/verified 15/15
  - p64 Total visitor arrivals to Hong Kong, June 2026 (provisional HKTB monthly figure) = **3,722,694** visitor (2026-06-01..2026-06-30) [keep: ] quote: "\| 總數 \| 3,722,694 (+7%) \| 26,712,488 (+13%) \|"
  - p65 Total visitor arrivals to Hong Kong, January-June 2026 cumulative = **26,712,488** visitor (2026-01-01..2026-06-30) [keep: ] quote: "\| 總數 \| 3,722,694 (+7%) \| 26,712,488 (+13%) \|"
  - p66 Mainland China visitor arrivals to Hong Kong, June 2026 = **2,884,732** visitor (2026-06-01..2026-06-30) [keep: ] quote: "\| 中國內地 \| 2,884,732 (+10%) \| 20,555,086 (+16%) \|"
  - p67 Mainland China visitor arrivals to Hong Kong, January-June 2026 cumulative = **20,555,086** visitor (2026-01-01..2026-06-30) [keep: ] quote: "\| 中國內地 \| 2,884,732 (+10%) \| 20,555,086 (+16%) \|"
  - p68 Mainland China visitor arrivals YoY growth, June 2026 = **10** % (2026-06-01..2026-06-30) [keep: ] quote: "\| 中國內地 \| 2,884,732 (+10%) \| 20,555,086 (+16%) \|"
  - p69 Mainland China visitor arrivals YoY growth, January-June 2026 cumulative = **16** % (2026-01-01..2026-06-30) [keep: ] quote: "\| 中國內地 \| 2,884,732 (+10%) \| 20,555,086 (+16%) \|"
  - p70 Short-haul market visitor arrivals to Hong Kong, June 2026 = **415,185** visitor (2026-06-01..2026-06-30) [keep: ] quote: "\| 短途 \| 415,185 (-15%) \| 3,209,069 (-2%) \|"
  - p71 Short-haul market visitor arrivals to Hong Kong, January-June 2026 cumulative = **3,209,069** visitor (2026-01-01..2026-06-30) [keep: ] quote: "\| 短途 \| 415,185 (-15%) \| 3,209,069 (-2%) \|"
  - p72 Short-haul market visitor arrivals YoY growth, June 2026 = **-15** % (2026-06-01..2026-06-30) [keep: ] quote: "\| 短途 \| 415,185 (-15%) \| 3,209,069 (-2%) \|"
  - p73 Long-haul market visitor arrivals to Hong Kong, June 2026 = **277,034** visitor (2026-06-01..2026-06-30) [keep: ] quote: "\| 長途 \| 277,034 (+16%) \| 1,985,526 (+19%) \|"
  - p74 Long-haul market visitor arrivals to Hong Kong, January-June 2026 cumulative = **1,985,526** visitor (2026-01-01..2026-06-30) [keep: ] quote: "\| 長途 \| 277,034 (+16%) \| 1,985,526 (+19%) \|"
  - p75 Long-haul market visitor arrivals YoY growth, January-June 2026 cumulative = **19** % (2026-01-01..2026-06-30) [keep: ] quote: "\| 長途 \| 277,034 (+16%) \| 1,985,526 (+19%) \|"
  - p76 Non-Mainland visitor arrivals to Hong Kong, June 2026 = **837,962** visitor (2026-06-01..2026-06-30) [keep: ] quote: "\| 非中國內地* \| 837,962 (-4%) \| 6,157,402 (+5%) \|"
  - p77 Non-Mainland visitor arrivals to Hong Kong, January-June 2026 cumulative = **6,157,402** visitor (2026-01-01..2026-06-30) [keep: ] quote: "\| 非中國內地* \| 837,962 (-4%) \| 6,157,402 (+5%) \|"
  - p78 Overnight MICE visitor arrivals to Hong Kong YoY growth, January-May 2026 cumula = **12** % (2026-01-01..2026-05-31) [keep: ] quote: "今年1至5月份的訪港過夜會展旅客,較去年同期上升12%。"
- `https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/tourisum-statistics/2026/tourism_stat_02_2026.pdf` -> **snapshot** (snapshot 20260403023450); points raw/verified 15/15
  - p79 Total visitor arrivals to Hong Kong, February 2026 (provisional monthly total) = **5,141,714** visitor (2026-02-01..2026-02-28) [keep: ] quote: "合計 TOTAL 3,667,671 5,141,714 + 40.2 8,409,737 9,953,414 + 18.4"
  - p80 Total visitor arrivals to Hong Kong, February 2025 = **3,667,671** visitor (2025-02-01..2025-02-28) [keep: ] quote: "合計 TOTAL 3,667,671 5,141,714 + 40.2 8,409,737 9,953,414 + 18.4"
  - p81 Total visitor arrivals to Hong Kong, January-February 2026 cumulative = **9,953,414** visitor (2026-01-01..2026-02-28) [keep: ] quote: "合計 TOTAL 3,667,671 5,141,714 + 40.2 8,409,737 9,953,414 + 18.4"
  - p82 Total visitor arrivals to Hong Kong, January-February 2025 cumulative = **8,409,737** visitor (2025-01-01..2025-02-28) [keep: ] quote: "合計 TOTAL 3,667,671 5,141,714 + 40.2 8,409,737 9,953,414 + 18.4"
  - p83 Chinese Mainland visitor arrivals to Hong Kong, February 2026 = **4,248,174** visitor (2026-02-01..2026-02-28) [keep: ] quote: "中國內地 Chinese Mainland 2,769,404 4,248,174 + 53.4 6,495,640 7,893,820 + 21.5"
  - p84 Chinese Mainland visitor arrivals to Hong Kong, February 2025 = **2,769,404** visitor (2025-02-01..2025-02-28) [keep: ] quote: "中國內地 Chinese Mainland 2,769,404 4,248,174 + 53.4 6,495,640 7,893,820 + 21.5"
  - p85 Chinese Mainland visitor arrivals YoY growth, February 2026 = **53.4** % (2026-02-01..2026-02-28) [keep: ] quote: "中國內地 Chinese Mainland 2,769,404 4,248,174 + 53.4 6,495,640 7,893,820 + 21.5"
  - p86 Chinese Mainland visitor arrivals to Hong Kong, January-February 2026 cumulative = **7,893,820** visitor (2026-01-01..2026-02-28) [keep: ] quote: "中國內地 Chinese Mainland 2,769,404 4,248,174 + 53.4 6,495,640 7,893,820 + 21.5"
  - p87 Chinese Mainland visitor arrivals YoY growth, January-February 2026 cumulative = **21.5** % (2026-01-01..2026-02-28) [keep: ] quote: "中國內地 Chinese Mainland 2,769,404 4,248,174 + 53.4 6,495,640 7,893,820 + 21.5"
  - p88 Non-Chinese Mainland visitor arrivals to Hong Kong, February 2026 = **893,540** visitor (2026-02-01..2026-02-28) [keep: ] quote: "非中國內地 Non-Chinese Mainland 898,267 893,540 - 0.5 1,914,097 2,059,594 + 7.6"
  - p89 Short Haul Markets (excl. Chinese Mainland) visitor arrivals to Hong Kong, Febru = **590,684** visitor (2026-02-01..2026-02-28) [keep: ] quote: "Short Haul Markets ( Exclude Chinese Mainland ) 631,795 590,684 - 6.5 1,320,829 1,325,245 + 0.3"
  - p90 Short Haul Markets (excl. Chinese Mainland) visitor arrivals YoY growth, Februar = **6.5** % (2026-02-01..2026-02-28) [keep: ] quote: "Short Haul Markets ( Exclude Chinese Mainland ) 631,795 590,684 - 6.5 1,320,829 1,325,245 + 0.3"
  - p91 Long Haul Markets visitor arrivals to Hong Kong, February 2026 = **258,248** visitor (2026-02-01..2026-02-28) [keep: ] quote: "長途地區市場 Long Haul Markets 227,098 258,248 + 13.7 503,518 617,227 + 22.6"
  - p92 Long Haul Markets visitor arrivals YoY growth, February 2026 = **13.7** % (2026-02-01..2026-02-28) [keep: ] quote: "長途地區市場 Long Haul Markets 227,098 258,248 + 13.7 503,518 617,227 + 22.6"
  - p93 Total visitor arrivals YoY growth, February 2026 = **40.2** % (2026-02-01..2026-02-28) [keep: ] quote: "合計 TOTAL 3,667,671 5,141,714 + 40.2 8,409,737 9,953,414 + 18.4"
- `https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3346858/did-chinese-new-year-help-boost-hong-kongs-visitor-figures-january-february` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.rthk.hk/rthk/en/component/k2/1827331-20251015.htm` -> **snapshot** (snapshot 20251015110247); points raw/verified 12/12
  - p94 Total visitor arrivals to Hong Kong, first three quarters of 2025 (cumulative) = **36,000,000** visitor (2025-01-01..2025-09-30) [DISCARD: Duplicate of p52/p108 (9M-2025 total).] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p95 Total visitor arrivals to Hong Kong YoY growth, first three quarters of 2025 = **12** % (2025-01-01..2025-09-30) [DISCARD: Duplicate of p53/p109.] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p96 Non-mainland visitor arrivals to Hong Kong, first three quarters of 2025 (cumula = **8,500,000** visitor (2025-01-01..2025-09-30) [DISCARD: Duplicate of p54/p110.] quote: "robust growth in the number of inbound travellers from places other than the mainland, which stood at about 8.5 million during the period, up 16 percent year on year."
  - p97 Non-mainland visitor arrivals to Hong Kong YoY growth, first three quarters of 2 = **16** % (2025-01-01..2025-09-30) [DISCARD: Duplicate of p55/p111.] quote: "which stood at about 8.5 million during the period, up 16 percent year on year."
  - p98 Mainland visitor arrivals to Hong Kong, first three quarters of 2025 (cumulative = **28,000,000** visitor (2025-01-01..2025-09-30) [DISCARD: Duplicate of p56/p112.] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p99 Mainland share of total visitor arrivals to Hong Kong, first three quarters of 2 = **78** % (2025-01-01..2025-09-30) [DISCARD: Duplicate of p57/p113.] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p100 Mainland visitor arrivals to Hong Kong YoY growth, first three quarters of 2025 = **11** % (2025-01-01..2025-09-30) [DISCARD: Duplicate of p58/p114.] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p101 Total visitor arrivals to Hong Kong, September 2025 (preliminary) = **3,300,000** visitor (2025-09-01..2025-09-30) [DISCARD: Duplicate of p59/p115.] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p102 Total visitor arrivals to Hong Kong YoY growth, September 2025 = **8** as written "eight percent", value check pending % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p60/p116.] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p103 Long-haul market visitor arrivals to Hong Kong YoY growth, September 2025 = **14** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p61/p117.] quote: "with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p104 Short-haul market visitor arrivals to Hong Kong YoY growth, September 2025 = **9** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p62/p118.] quote: "with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p105 New market visitor arrivals to Hong Kong YoY growth, September 2025 = **13** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p63/p119.] quote: "Travellers from new markets grew by 13 percent in September, compared to the same period last year."
- `https://www.thestandard.com.hk/news/article/314146/HK-sees-sustained-tourism-growth-with-33m-visitors-in-September` -> **snapshot** (snapshot 20260812235344); points raw/verified 13/0
- `https://partnernet.hktb.com/germany/de/industry_news/hktb_updates/index.html?id=9048` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (period year 2025 does not appear in the page text or URL (likely mis-dated): 13)

### d6 [shocks] Event and calendar effects

Hypothesis: September 2026 calendar (weekday/weekend mix, Mid-Autumn Festival timing, any typhoon/typhoon-season disruption, policy changes such as visa or tax-refund schemes, currency effects) shifts arrivals relative to a naive trend. Quantify exposure where measurable.

Queries issued by the searcher: Mid-Autumn Festival 2026 date Hong Kong public holiday; Hong Kong events September 2026 conferences; Hong Kong Tourism Board monthly visitor arrivals 2026 statistics July August; typhoon Hong Kong September 2026 T8 signal; Mid-Autumn Festival 2026 date Hong Kong public holiday; Hong Kong events September 2026; HKTB monthly visitor arrivals 2026 provisional statistics July August 2026; Hong Kong visitor arrivals September 2025 total HKTB press release; Mid-Autumn Festival 2026 date Hong Kong public holiday September; Hong Kong Tourism Board monthly visitor arrivals statistics 2026; Hong Kong events September 2026 exhibitions jewellery gem fair watch clock fair calendar; typhoon Hong Kong September 2026 signal No 8 disruption

- `https://www.gov.hk/en/about/abouthk/holiday/2026.htm` -> **snapshot** (snapshot 20260830105600); points raw/verified 2/2
  - p106 Hong Kong general holiday: day following the Chinese Mid-Autumn Festival (2026) = **26** day of month (2026-09-26..2026-09-26) [keep: ] quote: "\| The day following the Chinese Mid-Autumn Festival \| 26 September \| Saturday \|"
  - p107 Number of general holidays listed for 2026 (excluding every Sunday) = **17** holiday (2026-01-01..2026-12-31) [DISCARD: Holiday count, not arrivals.] quote: "\| Lunar New Year's Day \| 17 February \| Tuesday \|"
- `https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3367569/hong-kong-visitor-arrivals-hit-post-pandemic-monthly-high-august` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.info.gov.hk/gia/general/202505/16/P2025051300353.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mehongkong.com/eng/home/planning/events/detail/2026-09-06-87902-PBC-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.novotelhongkongcentury.com/mid-autumn-festival-hong-kong-2026-busines-travel-guide/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=5&print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bm.hkust.edu.hk/zh-hk/school-in-media/2026/08/summer-spending-uncertain-despite-major-events-chinese-version-only` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.timeanddate.com/holidays/hong-kong/2026?hol=96` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.search.gov.hk/viewer.html?url=https%3A%2F%2Fwww.investhk.gov.hk%2Fzh-hk%2Fevents%2Fthe-belt-and-road-summit-2026%2F` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bio-hk.com/media/news-press-releases/23` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] HKTB monthly visitor arrivals series

Hypothesis: A complete monthly HKTB series for July and August 2026 (and the 2025 monthly path) would let series_auto and yoy_scaling run on the target's own recent trajectory, replacing the June-only anchor and capturing the deceleration from +13% (H1) to +7% (June).

Queries issued by the searcher: HKTB monthly visitor arrivals press release July 2026; Hong Kong visitor arrivals August 2026 provisional HKTB; HKTB provisional visitor arrivals September 2025 total 3.3 million year-on-year; "September 2024" Hong Kong visitor arrivals provisional total HKTB 3.1 million; HKTB monthly visitor arrivals July 2026 press release; Hong Kong visitor arrivals August 2026; HKTB provisional visitor arrivals September 2025 total 3.2 million year-on-year; partnernet.hktb.com Tourism_Statistics monthly visitor arrivals 2025 table total; HKTB monthly visitor arrivals press release July 2026; Hong Kong visitor arrivals August 2026 provisional total; HKTB provisional visitor arrivals September 2025 total 3.2 million press release; Hong Kong September 2024 visitor arrivals 3.1 million HKTB monthly

- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.discoverhongkong.com/content/dam/dhk/intl/corporate/newsroom/press-release/hktb/2026/08-July-Visitor-Arrivals-E.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=5&print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/314146/HK-sees-sustained-tourism-growth-with-33m-visitors-in-September` -> **snapshot** (snapshot 20260812235344); points raw/verified 13/0
- `https://www.hkej.com/landing/articleprint/id/4223190` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.rthk.hk/rthk/en/component/k2/1827331-20251015.htm` -> **snapshot** (snapshot 20251015110247); points raw/verified 12/12
  - p108 Total visitor arrivals to Hong Kong, first three quarters of 2025 (cumulative) = **36,000,000** visitor (2025-01-01..2025-09-30) [keep: ] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p109 Year-on-year change in total visitor arrivals to Hong Kong, first three quarters = **12** % (2025-01-01..2025-09-30) [keep: ] quote: "Hong Kong welcomed over 36 million visitors in the first three quarters of 2025, marking a 12 percent increase year on year."
  - p110 Visitor arrivals to Hong Kong from non-mainland markets, first three quarters of = **8,500,000** visitor (2025-01-01..2025-09-30) [keep: ] quote: "the number of inbound travellers from places other than the mainland, which stood at about 8.5 million during the period, up 16 percent year on year."
  - p111 Year-on-year change in visitor arrivals to Hong Kong from non-mainland markets,  = **16** % (2025-01-01..2025-09-30) [keep: ] quote: "the number of inbound travellers from places other than the mainland, which stood at about 8.5 million during the period, up 16 percent year on year."
  - p112 Visitor arrivals to Hong Kong from mainland China, first three quarters of 2025  = **28,000,000** visitor (2025-01-01..2025-09-30) [keep: ] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p113 Mainland China share of total visitor arrivals to Hong Kong, first three quarter = **78** % (2025-01-01..2025-09-30) [keep: ] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p114 Year-on-year change in visitor arrivals to Hong Kong from mainland China, first  = **11** % (2025-01-01..2025-09-30) [keep: ] quote: "The 28 million travellers from the mainland, meanwhile, accounted for about 78 percent of the overall number, up 11 percent year on year."
  - p115 Total visitor arrivals to Hong Kong, September 2025 (provisional) = **3,300,000** visitor (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p116 Year-on-year change in total visitor arrivals to Hong Kong, September 2025 = **8** as written "eight percent", value check pending % (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p117 Year-on-year change in visitor arrivals to Hong Kong from long-haul markets, Sep = **14** % (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p118 Year-on-year change in visitor arrivals to Hong Kong from short-haul markets, Se = **9** % (2025-09-01..2025-09-30) [keep: ] quote: "In September alone, visitor arrivals were about 3.3 million, up eight percent on the year, with those from long-haul markets up 14 percent and those from short-haul markets rising by 9 percent."
  - p119 Year-on-year change in visitor arrivals to Hong Kong from new markets, September = **13** % (2025-09-01..2025-09-30) [keep: ] quote: "Travellers from new markets grew by 13 percent in September, compared to the same period last year."
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wenweipo.com/epaper/view/newsDetail/1978514343884623872.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.es/noticias/art%C3%ADculo/4txosv634n8i/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jiji.com/jc/article?k=2026100700545&g=jnb` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/korea/kr/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=true&gvHelperp=2&id=7008` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (period year 2025 does not appear in the page text or URL (likely mis-dated): 13)

### b2 [related_series] Immigration Department daily passenger statistics

Hypothesis: Daily or monthly total passenger throughput at land control points for September 2026 (or early September) would let a partial_period or channel-sum route constrain the month directly, resolving the largest uncertainty (whether the June deceleration continues).

Queries issued by the searcher: Immigration Department daily passenger statistics September 2026; HKTB visitor arrivals September 2026 provisional; HKTB visitor arrivals August 2026 preliminary 7.6 million January-August; news.gov.hk Immigration Department passenger traffic estimate Mid-Autumn Festival National Day 2026 control points; Immigration Department daily passenger statistics September 2026; HKTB visitor arrivals September 2026 provisional; HKTB visitor arrivals August 2026 preliminary press release; HKTB visitor arrivals July 2026 million year-on-year; Hong Kong Tourism Board visitor arrivals September 2026 provisional; Immigration Department daily passenger statistics September 2026; HKTB visitor arrivals July 2026 preliminary million year-on-year; " Immigration Department" daily passenger traffic early September 2026 arrivals Mid-Autumn

- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic/resource/e06a2a45-fe05-4eb4-9302-237d74343d52` -> **snapshot** (snapshot 20260312141129); points raw/verified 0/0
- `https://everything.hk/en/population/passenger-traffic` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20260924` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/data_specification_for_statistics_on_daily_passenger_traffic.pdf` -> **snapshot** (snapshot 20260309185128); points raw/verified 0/0
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/342800/HK-welcomes-3667m-visitors-in-first-eight-months-of-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?gvHelpera=false&gvHelperp=2&gvHelpers=TITLE&id=4588%2f1000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.gov.hk/en-datasets/provider/hk-immd` -> **snapshot** (snapshot 20260609082107); points raw/verified 0/0
- `https://www.immd.gov.hk/pdf/Annual%20Open%20Data%20Plan%20for%202020%20(EN)%20(ImmD).pdf` -> **snapshot** (snapshot 20240611010108); points raw/verified 0/0
- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html` -> **snapshot** (snapshot 20240705182341); points raw/verified 0/0
- `https://www.info.gov.hk/gia/general/202602/13/P2026021300683.htm` -> **snapshot** (snapshot 20260730193140); points raw/verified 12/12
  - p120 Total passengers through Hong Kong control points, 2025 (annual total) = **335,000,000** passenger (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, a total of around 335 million passengers passed through Hong Kong's control points"
  - p121 Year-on-year increase in total passengers through Hong Kong control points, 2025 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "representing an increase of about 12 per cent over 2024 - a new record high surpassing the 300 million level in 2019"
  - p122 Total visitor arrivals to Hong Kong, 2025 (annual total) = **49,890,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "The total number of visitor arrivals was around 49.89 million, representing an increase of about 12 per cent as compared with that of 2024"
  - p123 Mainland visitor arrivals to Hong Kong, 2025 (annual total) = **37,830,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "of which Mainland visitor arrivals were around 37.83 million, representing an increase of about 11 per cent when compared with that of 2024"
  - p124 Non-Mainland (other) visitor arrivals to Hong Kong, 2025 (annual total) = **12,060,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "the number of arrivals of other visitors was around 12.06 million, representing an increase of about 15 per cent over 2024"
  - p125 Visitor arrivals via Airport Control Point, 2025 (annual total) = **11,220,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "Among the visitor arrivals in 2025, around 11.22 million visitors travelled through the Airport Control Point"
  - p126 Visitor arrivals via land control points, 2025 (annual total) = **36,870,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "while around 36.87 million visitors and around 1.81 million visitors passed through land control points and sea control points respectively"
  - p127 Visitor arrivals via sea control points, 2025 (annual total) = **1,810,000** visitor (2025-01-01..2025-12-31) [keep: ] quote: "around 36.87 million visitors and around 1.81 million visitors passed through land control points and sea control points respectively"
  - p128 Total passengers through Hong Kong control points, 2019 (pre-pandemic reference  = **300,000,000** passenger (2019-01-01..2019-12-31) [keep: ] quote: "a new record high surpassing the 300 million level in 2019"
  - p129 Year-on-year increase in Mainland visitor arrivals, 2025 vs 2024 = **11** % (2025-01-01..2025-12-31) [keep: ] quote: "Mainland visitor arrivals were around 37.83 million, representing an increase of about 11 per cent when compared with that of 2024"
  - p130 Year-on-year increase in other (non-Mainland) visitor arrivals, 2025 vs 2024 = **15** % (2025-01-01..2025-12-31) [keep: ] quote: "the number of arrivals of other visitors was around 12.06 million, representing an increase of about 15 per cent over 2024"
  - p131 Year-on-year increase in total visitor arrivals, 2025 vs 2024 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "The total number of visitor arrivals was around 49.89 million, representing an increase of about 12 per cent as compared with that of 2024"

### b3 [forecasts_markets] HKTB market-level 2026 outlook

Hypothesis: Market-level 2026 growth guidance (mainland vs short-haul vs long-haul) published mid-2026 would sharpen the market-sum route, since short-haul turned negative (-15% in June) while long-haul stayed strong (+16%), and the mix matters for September.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast by market mid-year; Legislative Council tourism briefing 2026 visitor arrivals by market HKTB; HKTB provisional visitor arrivals July 2026; "September 2025" HKTB provisional visitor arrivals million year-on-year; HKTB 2026 visitor arrivals forecast by market mid-year review; Hong Kong visitor arrivals June 2026 short-haul long-haul HKTB monthly statistics; HKTB August 2026 visitor arrivals provisional 4.4 million; Legislative Council briefing 2026 Hong Kong tourism visitor arrivals forecast by market 53.8 million; HKTB 2026 visitor arrivals forecast by market mid-year review; Hong Kong Tourism Board half-year 2026 tourism performance visitor arrivals by market; 旅發局 2026年8月 訪港旅客 臨時數字 公布; HKTB August 2026 visitor arrivals provisional 4.4 million year-on-year

- `https://www.visahq.news/ja/2026-06-15/hk/hong-kong-logs-446-million-may-arrivals-and-unveils-summer-fun-campaign/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.micetraveladvisor.com/news/article/the-pearl-of-the-orient-shines-again-how-hong-kong-welcomed-26-7-million-travelers-to-reclaim-its-sacre` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mandosapp.com/blog/article/hong-kong-tourism-2026-comeback` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.budget.gov.hk/2026/eng/pdf/head132.pdf` -> **snapshot** (snapshot 20260510200932); points raw/verified 15/9
  - p132 HKTB visitor arrivals year-on-year increase, 2024 (actual) = **31** % (2024-01-01..2024-12-31) [keep: ] quote: "increase on previous year (%)Ψ................................................................................................ +31 ............................... +12 +8"
  - p133 HKTB visitor arrivals year-on-year increase, 2025 (revised estimate) = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "increase on previous year (%)Ψ................................................................................................ +31 ............................... +12 +8"
  - p134 HKTB visitor arrivals year-on-year increase, 2026 (estimate/forecast) = **8** % (2026-01-01..2026-12-31) [keep: ] quote: "increase on previous year (%)Ψ................................................................................................ +31 ............................... +12 +8"
  - p135 Per capita expenditure of overnight visitor, 2024 (actual) = **5,490** HKD per overnight visitor (2024-01-01..2024-12-31) [keep: ] quote: "per capita expenditure of overnight visitor ($)Ω................................................................ 5,490 ................................ 5,503 ...... 5,530"
  - p136 Per capita expenditure of overnight visitor, 2025 (revised estimate) = **5,503** HKD per overnight visitor (2025-01-01..2025-12-31) [keep: ] quote: "per capita expenditure of overnight visitor ($)Ω................................................................ 5,490 ................................ 5,503 ...... 5,530"
  - p137 Per capita expenditure of overnight visitor, 2026 (estimate/forecast) = **5,530** HKD per overnight visitor (2026-01-01..2026-12-31) [keep: ] quote: "per capita expenditure of overnight visitor ($)Ω................................................................ 5,490 ................................ 5,503 ...... 5,530"
  - p138 Length of stay of overnight visitors, 2024 (actual) = **3.2** nights per overnight visitor (2024-01-01..2024-12-31) [keep: ] quote: "length of stay of overnight visitors (nights)β................................................................ 3.2 ................................ 3.1 ...........3.1"
  - p139 Length of stay of overnight visitors, 2025 (revised estimate) = **3.1** nights per overnight visitor (2025-01-01..2025-12-31) [keep: ] quote: "length of stay of overnight visitors (nights)β................................................................ 3.2 ................................ 3.1 ...........3.1"
  - p140 Length of stay of overnight visitors, 2026 (estimate/forecast) = **3.1** nights per overnight visitor (2026-01-01..2026-12-31) [keep: ] quote: "length of stay of overnight visitors (nights)β................................................................ 3.2 ................................ 3.1 ...........3.1"
- `https://partnernet.hktb.com/en/research_statistics/tourism_performance/index.html` -> **snapshot** (snapshot 20260518002411); points raw/verified 0/0
- `https://partnernet.hktb.com/japan/jp/industry_news/hktb_updates/index.html?id=9129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bastillepost.com/global/article/5780413-scst-the-development-of-hong-kongs-tourism-sports-and-culture-sectors-in-2025-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://axtravelguide.com/hong-kong-welcomes-26-7-million-visitors-in-h1-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://en.people.cn/n3/2026/0818/c90000-20489664.html` -> **snapshot** (snapshot 20260818062325); points raw/verified 6/6
  - p141 Total visitor arrivals to Hong Kong, cumulative January–July 2026 (provisional H = **31,220,000** visitor (2026-01-01..2026-07-31) [keep: ] quote: "Hong Kong recorded approximately 31.22 million visitor arrivals in the first seven months of 2026, up 11 percent year on year"
  - p142 Year-on-year growth rate of total visitor arrivals to Hong Kong, January–July 20 = **11** % (2026-01-01..2026-07-31) [keep: ] quote: "Hong Kong recorded approximately 31.22 million visitor arrivals in the first seven months of 2026, up 11 percent year on year"
  - p143 Visitor arrivals to Hong Kong from the Chinese mainland, cumulative January–July = **24,160,000** visitor (2026-01-01..2026-07-31) [keep: ] quote: "From January to July, visitor arrivals from the Chinese mainland reached 24.16 million, representing a year-on-year increase of 13 percent."
  - p144 Year-on-year growth rate of visitor arrivals to Hong Kong from the Chinese mainl = **13** % (2026-01-01..2026-07-31) [keep: ] quote: "From January to July, visitor arrivals from the Chinese mainland reached 24.16 million, representing a year-on-year increase of 13 percent."
  - p145 Total visitor arrivals to Hong Kong, July 2026 = **4,500,000** visitor (2026-07-01..2026-07-31) [keep: ] quote: "In July alone, visitor arrivals reached approximately 4.5 million, up 3 percent compared with the same period last year."
  - p146 Year-on-year growth rate of total visitor arrivals to Hong Kong, July 2026 = **3** % (2026-07-01..2026-07-31) [keep: ] quote: "In July alone, visitor arrivals reached approximately 4.5 million, up 3 percent compared with the same period last year."
- `http://hkcna.hk/docDetail.jsp?id=101397630&channel=5773` -> **snapshot** (snapshot 20260818014134); points raw/verified 11/7
  - p147 July 2026 year-on-year change in total visitor arrivals to Hong Kong = **3** % (2026-07-01..2026-07-31) [keep: ] quote: "2026年7月香港初步訪港旅客達450萬人次,按年上升3%"
  - p148 First 7 months of 2026 year-on-year change in cumulative visitor arrivals to Hon = **11** % (2026-01-01..2026-07-31) [keep: ] quote: "今年首7個月,香港訪港旅客初步錄得約3122萬人次,按年上升11%"
  - p149 July 2026 year-on-year change in long-haul market visitor arrivals to Hong Kong = **17** % (2026-07-01..2026-07-31) [keep: ] quote: "7月訪港遊客的長途市場延續增長勢頭,按年上升17%至30.72萬人次"
  - p150 July 2026 year-on-year change in short-haul market visitor arrivals to Hong Kong = **9** % (2026-07-01..2026-07-31) [keep: ] quote: "短途市場則按年減少9%至約41.37萬人次"
  - p151 July 2026 year-on-year change in mainland market visitor arrivals to Hong Kong = **3** % (2026-07-01..2026-07-31) [keep: ] quote: "內地旅客數字亦按年增長3%"
  - p152 First 7 months of 2026 year-on-year change in long-haul (Europe/US) market visit = **19** % (2026-01-01..2026-07-31) [keep: ] quote: "歐美等長途市場延續增長勢頭,按年增19%"
  - p153 First 7 months of 2026 year-on-year change in short-haul (Taiwan, Southeast Asia = **3** % (2026-01-01..2026-07-31) [keep: ] quote: "台灣地區、東南亞等短途市場面臨增長壓力,按年減少3%"
- `https://www.legco.gov.hk/yr2026/english/panels/edev/papers/edev20260410cb2-411-4-e.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (scale word 'million' not supported by quote or table header: 3; scale word 'billion' not supported by quote or table header: 3; scale word '万' not supported by quote or table header: 4)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hong kong tourism', 'visitor arrivals', 'september 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p59', 'p101'] Same RTHK report of September 2025 preliminary arrivals (~3.3 million); duplicate copies of one measurement, not independent confirmation.
- corroborating: ['p60', 'p102'] Same 8% September 2025 YoY growth figure from the same RTHK article; duplicate.
- corroborating: ['p52', 'p94'] Same 36 million first-three-quarters-2025 figure; duplicate.
- corroborating: ['p53', 'p95'] Same 12% Q1-Q3 2025 growth; duplicate.
- corroborating: ['p54', 'p96'] Same 8.5 million non-mainland Q1-Q3 2025 figure; duplicate.
- corroborating: ['p55', 'p97'] Same 16% non-mainland growth; duplicate.
- corroborating: ['p56', 'p98'] Same 28 million mainland Q1-Q3 2025 figure; duplicate.
- corroborating: ['p57', 'p99'] Same 78% mainland share; duplicate.
- corroborating: ['p58', 'p100'] Same 11% mainland growth; duplicate.
- corroborating: ['p61', 'p103'] Same 14% long-haul September 2025 growth; duplicate.
- corroborating: ['p62', 'p104'] Same 9% short-haul September 2025 growth; duplicate.
- corroborating: ['p63', 'p105'] Same 13% new-market September 2025 growth; duplicate.
- corroborating: ['p41', 'p44'] Two 2026 full-year visitor targets (50 million stated in Feb, 53.8 million in April); the later, higher figure supersedes but both indicate a 2026 level well above 2025.
- corroborating: ['p44', 'p45'] 53.8 million target and its 8% YoY rise are internally consistent (implies ~49.8 million in 2025).
- corroborating: ['p64', 'p65', 'p66', 'p67', 'p70', 'p71', 'p73', 'p74', 'p76', 'p77'] June 2026 and Jan-Jun 2026 cumulative figures from one HKTB-derived table; internally consistent (June components sum to total) but a single source.
- corroborating: ['p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93'] February 2026 HKTB table; internally consistent, but February is distorted by Lunar New Year timing (53% mainland growth) and is not representative of September.
- corroborating: ['p64', 'p79'] Both are HKTB provisional monthly totals for 2026; together they show a decelerating YoY path (Feb +40%, Jun +7%).
- corroborating: ['p38', 'p39'] HKIA 2026 expected ~70 million vs 61 million in 2025; consistent with continued air-side recovery.
- corroborating: ['p9', 'p10', 'p11'] HKIA 2025 seat capacity 38.7 million, +12% YoY, still 14% below 2019; one OAG-derived source.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'] Immigration Department Easter/Ching Ming passenger forecasts; internally consistent (land ~5.43m of 6.44m total) but describe a holiday peak in April 2026, not September.
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] HKIA runway/ATM capacity documents from 2011 and a 2007 design day; describe theoretical capacity, not realised 2026 throughput.
- corroborating: ['p106', 'p107'] 2026 public holiday calendar; Mid-Autumn day-after holiday falls on 26 September 2026 (Saturday), relevant to September demand timing.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p59', 'p115', 'p101'] Same RTHK-sourced September 2025 preliminary figure (~3.3 million, +8% YoY); p59/p115/p101 are duplicate vintages of one measurement, not independent confirmation. Use one as the September 2025 base.
- corroborating: ['p52', 'p108', 'p94'] Duplicate copies of the same 9M-2025 cumulative (~36 million, +12%); single underlying RTHK release.
- corroborating: ['p56', 'p112', 'p98', 'p57', 'p113', 'p99'] Duplicate copies of the same 9M-2025 mainland figure (28 million, 78% share, +11%).
- corroborating: ['p54', 'p110', 'p96', 'p55', 'p111', 'p97'] Duplicate copies of the same 9M-2025 non-mainland figure (8.5 million, +16%).
- corroborating: ['p61', 'p117', 'p103', 'p62', 'p118', 'p104', 'p63', 'p119', 'p105'] Duplicate copies of the same September 2025 market-growth breakdown (long-haul +14%, short-haul +9%, new +13%).
- corroborating: ['p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77'] One HKTB June 2026 release: total 3.72m (+7%), H1 26.71m (+13%), mainland +10%/+16%, short-haul -15%/-2%, long-haul +16%/+19%, non-mainland -4%/+5%. Internally consistent; components sum to total.
- corroborating: ['p141', 'p142', 'p148', 'p143', 'p144'] Jan-Jul 2026 cumulative ~31.22m (+11%) and mainland 24.16m (+13%) from People's Daily and HKCNA; two outlets but same HKTB release, so one measurement.
- corroborating: ['p145', 'p146', 'p147'] July 2026 ~4.5m (+3%) from People's Daily and HKCNA; same HKTB release, duplicate.
- corroborating: ['p149', 'p150', 'p151', 'p152', 'p153'] July 2026 market detail: long-haul +17%, short-haul -9%, mainland +3%; Jan-Jul long-haul +19%, short-haul -3%. Consistent with June pattern of mainland-led growth and short-haul weakness.
- corroborating: ['p64', 'p141', 'p145'] Monthly YoY deceleration path: H1 +13%, June +7%, July +3%. Implies August/September growth likely in low-to-mid single digits, anchoring the YoY factor assumption.
- corroborating: ['p44', 'p45', 'p134', 'p41'] Full-year 2026 targets: 53.8m (+8%) and 'break 50m'; Budget forecast +8%. These are forecasts/targets, not outcomes, and are already being outpaced by H1 +13% then decelerating; useful only as a loose
- corroborating: ['p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p131', 'p129', 'p130'] 2025 annual actuals: 49.89m total, 37.83m mainland, 12.06m non-mainland; channel split air 11.22m, land 36.87m, sea 1.81m. Single ImmD/HKTB release; channel split sums to total.
- corroborating: ['p120', 'p121', 'p128'] Control-point passenger totals (335m in 2025, +12%, above 2019's 300m) — passengers, not visitors; only usable with a visitor-share conversion, and the share is not directly supplied.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'] ImmD Easter/Ching Ming 2026 festive-period passenger forecasts; internally consistent (land 5.43m of 6.44m total). These are April holiday peaks, not September, and are passengers not visitors — weak 
- corroborating: ['p9', 'p10', 'p11', 'p38', 'p39'] HKIA capacity/passenger context: 38.7m seats 2025 (+12%, 14% below 2019), ~61m passengers 2025 rising to ~70m expected 2026. Airport passengers include transfers and residents, so only a loose capacit
- corroborating: ['p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93'] Feb 2026 HKTB release: total 5.14m (+40.2%, CNY timing distortion), Jan-Feb 9.95m (+18.4%), mainland +53.4%/+21.5%, short-haul -6.5%/+0.3%, long-haul +13.7%/+22.6%. Consistent with the H1 growth story
- corroborating: ['p106'] Mid-Autumn day-after holiday falls 26 Sep 2026 (Saturday), giving a long weekend inside September — a mild positive for September arrivals vs a September without it.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth factor vs September 2025 | 1.05 | 0.94..1.17 | 0.938..1.172 (widened) | 1 | m2 (m3) | Monthly YoY path decelerated from H1 +13% (p65) to June +7% (p64) to July +3% (p145/p146). September 2025 base was itself +8% (p59), so a further low-single-digit YoY is plausible; Mid-Autumn long weekend (p106) gives a mild upside. Central 1.05 with wide band spanning a continued slide to ~-6% and  | September 2026 behaves like the June-July 2026 deceleration trend with no major new shock. | August 2026 data showing a sharp re-acceleration above +10% or a collapse below -10% YoY. |
| a2 | September share of full-year 2026 arrivals | 0.062 | 0.055..0.07 | 0.04387..0.08775 (widened) | 1 | m1 (m2) | September is a seasonally moderate month (post-summer, pre-Golden Week). September 2025 ~3.3m (p59) against 2025 annual 49.89m (p122) implies ~6.6%; with 2026 running above 2025 in H1 the share is similar. Central 6.2% with a band reflecting seasonal and trend uncertainty. | Full-year 2026 arrivals land near the 53.8m target (p44) and September's seasonal share is close to its 2025 value. | Evidence that September 2026 is unusually weak or strong relative to the annual run-rate (e.g. a major typhoon or festival shift). |
| a4 | September 2026 YoY growth factor vs September 2025, anchored on July 2026 +3% monthly growth | 1.03 | 0.92..1.14 | 0.916..1.145 (widened) | 1 | m3 (m4) | Latest observed monthly YoY growth before the target is July 2026 +3% (p146). September 2025 was +8% (p60), so a low-single-digit 2026 growth is consistent with the deceleration from June +7% (p64) to July +3%. Mid-Autumn long weekend (p106) gives mild upside; typhoon season gives downside. Central  | September 2026 continues the June-July 2026 deceleration without a new shock. | August 2026 data showing a sharp re-acceleration above +10% or a collapse below -10% YoY. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,347,030 | ['p44'] / ['a2'] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 3,458,891 | ['p59'] / ['a1'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | formula_mc | 3,374,611 | ['p59'] / ['a4'] | [] |  | 1.00 | B3 of 3 blocks; median of blocks: this block is the median |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p44 * a2; Monte Carlo P10 to P90 2,256,570 to 4,966,093; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m2 formula_mc: p59 * a1; Monte Carlo P10 to P90 2,791,953 to 4,285,753; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p59 * a4; Monte Carlo P10 to P90 2,728,888 to 4,181,614; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 3,347,030 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m2: 3,458,891 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 3,374,611 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.41; Birge ratio 0.06 (not above one, so no widening); final width x/÷1.41.

Result: central **3,374,611** visitor, 80% interval [2,385,633, 4,773,576] visitor, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

Unit of the estimate: visitor (visitor arrivals (person-trips); total for 2026-09-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total visitor arrivals to Hong Kong (all source markets, all arrival channels, person-trips) during September 2026, as first provisionally reported by the HKTB, is 3,374,611 visitor (80% model-based interval 2,385,633 to 4,773,576 visitor).

Main evidence: September 2025 arrivals were 3,300,000 visitor arrivals, and the 2026 annual target is 53,800,000 visitor arrivals. The three routes apply a September 2026 YoY factor to the 2025 base (1.05, range 0.938 to 1.172; 1.03, range 0.916 to 1.145) or a September share of the annual target (0.062, range 0.04387 to 0.08775). The base and target are observed; the growth factors and seasonal share are analyst assumptions, not observations.

Combination: code grouped overlapping-input methods into blocks and took the median of block estimates with equal block weight; no backtest errors were available, so widths are default.

Key risk: an unobserved August/September shock (typhoon, policy, currency) not captured by the deceleration trend. Better evidence would be actual August 2026 arrivals and early September booking/arrival data.

Unit of the estimate: visitor (visitor arrivals (person-trips); total for 2026-09-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth factor vs September 2025: 1.05 [n], range 0.938 to 1.172 (range widened by code); used by m2. Overturned by: August 2026 data showing a sharp re-acceleration above +[n] or a collapse below -[n] YoY.
- a2 September share of full-year 2026 arrivals: 0.062 [n], range 0.04387 to 0.08775 (range widened by code); used by m1. Overturned by: Evidence that September 2026 is unusually weak or strong relative to the annual run-rate (e.g. a major typhoon or festival shift).
- a4 September 2026 YoY growth factor vs September 2025, anchored on July 2026 +[n] monthly growth: 1.03 [n], range 0.916 to 1.145 (range widened by code); used by m3. Overturned by: August 2026 data showing a sharp re-acceleration above +[n] or a collapse below -[n] YoY.

Method details (computed by code):
- m1 formula_mc: p44 * a2; Monte Carlo P10 to P90 2,256,570 to 4,966,093; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m2 formula_mc: p59 * a1; Monte Carlo P10 to P90 2,791,953 to 4,285,753; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p59 * a4; Monte Carlo P10 to P90 2,728,888 to 4,181,614; result unit (visitor/month) * 1 month converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 3,347,030 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m2: 3,458,891 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 3,374,611 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.41; Birge ratio 0.06 (not above one, so no widening); final width x/÷1.41.

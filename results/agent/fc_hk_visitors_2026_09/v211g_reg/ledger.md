# Evidence ledger: fc_hk_visitors_2026_09

- Question: Assume today is 2026-09-14. You know nothing published after this date. Estimate the total number of visitor arrivals to Hong Kong in September 2026, as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals press release.
- as_of: 2026-09-14
- Pinned target: Total visitor arrivals to Hong Kong (all source markets, worldwide, arrivals counted at immigration/entry, i.e. visitor trips not unique persons) during calendar September 2026, as first reported provisionally by the Hong Kong Tourism Board in its monthly visitor arrivals press release | unit visitor arrivals | period 2026-09-01..2026-09-30 | publisher Hong Kong Tourism Board (HKTB)

- Official value (scoring only, never shown to the agent): 4,031,090

## Directions and pages

### d1 [own_history] HKTB monthly arrivals series

Hypothesis: September 2026 arrivals ≈ September 2025 arrivals × (recent YoY growth trend) × (September seasonal factor relative to adjacent months). Own history gives the seasonal shape and the base level; recent months published before cutoff give the momentum.

Queries issued by the searcher: HKTB monthly visitor arrivals September 2025 press release; Hong Kong visitor arrivals 2026 monthly statistics HKTB; 旅發局 2025年9月 訪港旅客 3,292,197 2024年9月 比較; HKTB visitor arrivals monthly statistics table 2023 2024 2025 total arrivals by month

- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/taiwan/tc/industry_news/hktb_updates/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=4&id=9130` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/research_statistics/latest_statistics/index.html?gvHelpers=TITLE&gvHelpera=false&gvHelperp=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/filemanager/sc/content_4925/HK_Tourism_Industry_Snapshot_published_in_Aug_2026_ENSC.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Immigration Department / airport and land boundary throughput

Hypothesis: Total arrivals at Hong Kong control points (Immigration Department daily/monthly passenger statistics) scale with visitor arrivals; visitor share of total inbound passenger flow can bridge to the target. Early-September 2026 daily immigration figures constrain the month.

Queries issued by the searcher: Immigration Department Hong Kong daily passenger statistics September 2025 arrivals; 香港旅遊發展局 2025年9月 訪港旅客 數字 新聞稿; immd.gov.hk passenger statistics 2026年9月1日 出入境人次; 旅發局 2026年 訪港旅客 上半年 初步數字 按年上升

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20250901` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic/resource/749ae4e2-9190-40a7-a6a0-818f8995a82a` -> **snapshot** (snapshot 20260312140532); points raw/verified 0/0
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/hks/facts/passenger-statistics.html?d=20250909` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Source-market decomposition (Mainland vs short-haul vs long-haul)

Hypothesis: Total = sum over source markets of arrivals; Mainland China dominates (~70-75%). Mainland arrivals track mainland outbound travel and Shenzhen border crossings; long-haul tracks flight capacity. Build total from market-level September 2025 values grown by market-specific signals.

Queries issued by the searcher: HKTB visitor arrivals by market September 2025 mainland China short-haul long-haul; Hong Kong Tourism Board monthly visitor arrivals 2026 mainland statistics; 旅發局 2026年7月 初步訪港旅客數字 450萬 短途 長途 partnernet; 深圳口岸 出入境 客流 2026年7月 暑假 出入境人員 人次

- `https://partnernet.hktb.com/korea/kr/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/tc/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.hket.com/article/4177634/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/germany/de/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [capacity_consumption] Air and cross-border transport capacity

Hypothesis: Arrivals are bounded by seat capacity and load factors on flights into HKG plus land/sea crossings. September 2026 flight schedules, seat capacity and hotel occupancy/bookings give an upper bound and a utilisation-based estimate.

Queries issued by the searcher: Hong Kong International Airport passenger traffic August 2026 flight movements; Hong Kong hotel occupancy rate 2026 room nights; HKIA July 2026 passenger volume flight movements press release; Hong Kong Tourism Board visitor arrivals July 2026 statistics monthly

- `https://www.hongkongairport.com/iwov-resources/file/the-airport/hkia-at-a-glance/facts-figures/Jul2026_statistics_e.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hongkongairport.com/en/media-centre/press-release/2026/pr_1884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/usa/en/home/index.html` -> **snapshot** (snapshot 20260402061340); points raw/verified 0/0
- `https://www.colliers.com/download-article?itemId=955bd292-2dc3-48b3-bdbc-2d0dc901690c` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Calendar, weather and policy effects

Hypothesis: September 2026 calendar (Mid-Autumn Festival timing, typhoon season, any visa/policy changes, currency) shifts arrivals vs the seasonal norm; identify measurable deviations (typhoon signal days, festival dates, new visa-free schemes) to adjust the base projection.

Queries issued by the searcher: Hong Kong Mid-Autumn Festival 2026 date public holiday; Hong Kong Tourism Board monthly visitor arrivals September 2025 press release; HKTB provisional visitor arrivals 2026 first half year-on-year increase press release; Hong Kong typhoon signal No. 8 September 2025 arrivals impact Ragasa tourism

- `https://partnernet.hktb.com/korea/kr/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/russia/ru/industry_news/hktb_updates/index.html?id=9328` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.hk/en/about/abouthk/holiday/2026.htm` -> **snapshot** (snapshot 20260830105600); points raw/verified 3/0
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?gvHelperp=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period_end 2026-09-26 after as_of: 1; period_end 2026-10-01 after as_of: 1; period_end 2026-10-19 after as_of: 1)

### d6 [forecasts_markets] Official and analyst forecasts

Hypothesis: HKTB or government full-year 2026 visitor arrival forecasts and quarterly guidance, plus airline/analyst commentary, imply a September level when combined with seasonal shares; use as a cross-check on the bottom-up routes.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast full year; 旅發局 2026 全年 訪港旅客 預測; 2025年9月 訪港旅客 旅發局 公布 人次 按年; HKTB monthly visitor arrivals 2025 September 3.2 million total year 2025 49 million

- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p1 Preliminary total visitor arrivals to Hong Kong, first five months of 2026 (Jan- = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [keep: ] quote: "in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/usa/en/home/index.html?cat_id=628&doc_id=137528` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wenweipo.com/a/202608/23/AP6a8a06ffe4b0c1e50025d8b5.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d7 [attention] Search and booking-platform interest

Hypothesis: Google Trends / booking-platform search interest for Hong Kong travel from key source markets in the weeks before September correlates with arrivals; use as a directional adjustment to the seasonal base rather than a direct quantity.

Queries issued by the searcher: Google Trends Hong Kong travel search interest 2026; Hong Kong Tourism Board visitor arrivals August 2026 provisional; HKTB provisional visitor arrivals September 2025 million year-on-year; Trip.com Hong Kong bookings inbound search interest 2026 surge

- `https://partnernet.hktb.com/russia/ru/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/hong-kong/google-search-trends-by-categories/google-search-trends-travel--accommodations-bookingcom` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hongkongbusiness.hk/hotels-tourism/news/visitor-arrivals-rise-6-in-august-short-haul-traffic-sinks` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] HKTB monthly visitor arrivals series

Hypothesis: September 2025 (and September 2024/2023) total visitor arrivals, plus monthly 2026 arrivals for June, July and August, would let a seasonal-ratio route convert the Jan–May 2026 level (p1) into a September 2026 estimate and provide a YoY momentum signal. Without these, the September level must rest on an assumption about the September-to-annual-average ratio.

Queries issued by the searcher: HKTB monthly visitor arrivals press release September 2025; info.gov.hk press releases visitor arrivals September 2025 Hong Kong Tourism Board; HKTB provisional visitor arrivals September 2024 3.05 million press release October 2024; 旅發局 2026年7月 訪港旅客 初步數字 按年

- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinadailyhk.com/hk/article/620022` -> **snapshot** (snapshot 20251014195346); points raw/verified 15/15
  - p2 Hong Kong total visitor arrivals, August 2025 (preliminary HKTB) = **5,150,000** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "Hong Kong logged 5.15 million visitor arrivals in August, representing a 16 percent year-on-year surge"
  - p3 Hong Kong total visitor arrivals, January–August 2025 cumulative = **33,000,000** visitor arrivals (2025-01-01..2025-08-31) [keep: ] quote: "The cumulative figure of inbound tourist trips from January to August surpassed 33 million"
  - p4 Hong Kong Mainland visitor arrivals, January–August 2025 cumulative = **25,530,000** visitor arrivals (2025-01-01..2025-08-31) [keep: ] quote: "25.53 million from the Chinese mainland and 7.65 million from other places"
  - p5 Hong Kong non-Mainland visitor arrivals, January–August 2025 cumulative = **7,650,000** visitor arrivals (2025-01-01..2025-08-31) [keep: ] quote: "25.53 million from the Chinese mainland and 7.65 million from other places"
  - p6 Hong Kong Mainland visitor arrivals, August 2025 = **4,220,000** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "Among August's arrivals, Chinese mainland travelers numbered 4.22 million, a growth of 15 percent compared to the same period last year"
  - p7 Mainland share of August 2025 total visitor arrivals = **82** % (2025-08-01..2025-08-31) [keep: ] quote: "accounting for 82 percent of the total"
  - p8 Hong Kong non-Mainland visitor arrivals, August 2025 = **930,000** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "Non-mainland visitor arrivals also grew by 17 percent last month, reaching around 930,000."
  - p9 Hong Kong total visitor arrivals, August 2025 year-on-year growth = **16** % (2025-08-01..2025-08-31) [keep: ] quote: "representing a 16 percent year-on-year surge"
  - p10 Hong Kong total visitor arrivals, January–August 2025 year-on-year growth = **12** % (2025-01-01..2025-08-31) [keep: ] quote: "a 12 percent year-on-year increase, the HKTB said"
  - p11 Hong Kong Mainland visitor arrivals, August 2025 year-on-year growth = **15** % (2025-08-01..2025-08-31) [keep: ] quote: "a growth of 15 percent compared to the same period last year"
  - p12 Hong Kong non-Mainland visitor arrivals, August 2025 year-on-year growth = **17** % (2025-08-01..2025-08-31) [keep: ] quote: "Non-mainland visitor arrivals also grew by 17 percent last month"
  - p13 Hong Kong short-haul market arrivals, January–August 2025 year-on-year growth = **18** % (2025-01-01..2025-08-31) [keep: ] quote: "the city saw 18 percent growth in arrivals from short-haul markets"
  - p14 Hong Kong long-haul market arrivals, January–August 2025 year-on-year growth = **19** % year-on-year (2025-01-01..2025-08-31) [keep: ] quote: "Long-haul visitors showed a healthy 19-percent increase, led by Australia."
  - p15 Hong Kong full-year 2025 visitor arrivals target (stated goal, forecast) = **49,000,000** visitor trips (2025-01-01..2025-12-31) [keep: ] quote: "she was confident that Hong Kong would achieve the goal of receiving 49 million visitor trips this year"
  - p16 Hong Kong full-year 2025 visitor arrivals target year-on-year growth (stated goa = **10** % year-on-year (2025-01-01..2025-12-31) [keep: ] quote: "a 10-percent increase compared to 2024"
- `https://www.aastocks.com/sc/stocks/analysis/stock-aafn-con/02360/aafn/now.1392971/hk-stock-news` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/filemanager/communication/enewsletter/8015/file/Deck_HKTB%20Quarterly%20Update_10Sep.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Immigration Department control-point passenger statistics

Hypothesis: Daily/monthly total inbound passenger counts at Hong Kong control points for early September 2026, combined with a visitor-share conversion factor, would constrain the September 2026 month directly and reduce reliance on the seasonal assumption. This is the only route that uses partial-month 2026 signal before the cutoff.

Queries issued by the searcher: Immigration Department daily passenger traffic statistics Hong Kong control points 2026; immd.gov.hk traffic statistics control point passenger arrivals monthly; immd.gov.hk passenger-statistics.html "September 2026" arrivals total control point; Hong Kong Tourism Board July 2026 visitor arrivals provisional million press release

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20260911` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/hks/facts/passenger-statistics.html?d=20260901` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic/resource/e06a2a45-fe05-4eb4-9302-237d74343d52` -> **snapshot** (snapshot 20260312141129); points raw/verified 0/0
- `https://www.censtatd.gov.hk/en/data/stat_report/product/B1010002/att/B10100022025MM11B0100.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] HKTB / government 2026 visitor forecast

Hypothesis: An official full-year 2026 visitor arrival forecast or quarterly guidance, combined with the historical September share of annual arrivals, would provide an independent cross-check on the seasonal-ratio route and help resolve the largest uncertainty (the September seasonal factor).

Queries issued by the searcher: HKTB 2026 visitor arrival forecast; Hong Kong 2026 tourist arrivals target government forecast; HKTB provisional visitor arrivals September 2025 million year-on-year; HKTB monthly visitor arrivals 2025 annual total 49.9 million table month

- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p17 Hong Kong total visitor arrivals, first five months of 2026 (preliminary, approx = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [DISCARD: Exact duplicate of p1 (same figure, same source, same period); adds no information.] quote: "in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/research_statistics/tourism_performance/index.html` -> **snapshot** (snapshot 20260518002411); points raw/verified 0/0
- `https://zijing.com.cn/web/article/1532139274674561024/web/content_1532139274674561024.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period year 2025 does not appear in the page text or URL (likely mis-dated): 2; period_end 2026-12-31 after as_of: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hong kong tourism', 'visitor arrivals', 'hktb september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1'] p1 is the only kept data point. It gives Jan–May 2026 total visitor arrivals (~23 million), a partial-year level from the HKTB/government source. It is not the target period (September 2026) and canno
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p17'] Same figure (~23 million Jan–May 2026) from the same government source; p17 is a duplicate of p1 and adds no independent information.
- corroborating: ['p2', 'p6', 'p7', 'p8', 'p9', 'p11', 'p12'] All from the same HKTB August 2025 release; internally consistent (4.22M Mainland + 0.93M non-Mainland ≈ 5.15M; 82% Mainland share). Shared underlying source, so not independent confirmation of each o
- corroborating: ['p3', 'p4', 'p5'] Jan–Aug 2025 cumulative: 25.53M Mainland + 7.65M non-Mainland ≈ 33M total. Same release, internally consistent.
- corroborating: ['p2', 'p3'] August 2025 (5.15M) is consistent with Jan–Aug cumulative 33M given a plausible Jan–Jul average; same source.
- corroborating: ['p13', 'p14'] Short-haul +18% and long-haul +19% Jan–Aug 2025 growth are consistent with the overall non-Mainland growth picture; same release.
- corroborating: ['p15', 'p16'] 49M full-year 2025 target and 10% YoY growth are internally consistent (implies ~44.5M in 2024); both are stated goals, not outcomes.
- contextual: ['p1', 'p3'] Jan–May 2026 (23M) vs Jan–Aug 2025 (33M) are different periods; not directly comparable but together bracket the 2026 run-rate. Jan–May 2026 monthly average (~4.6M) is above the Jan–Aug 2025 average (

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 arrivals as ratio of Jan–May 2026 monthly average (seasonal + momentum) | 0.95 | 0.78..1.15 | 0.6697..1.339 (widened) | ratio | m1 (m1) | September is a shoulder month in Hong Kong: post-summer-family, pre-October Golden Week, typically somewhat below the annual average. Jan–May 2026 monthly average is ~4.6M (p1/5). September historically runs modestly below the spring average; a ratio near 0.95 with wide range reflects shoulder-seaso | September 2026 behaves like a typical shoulder month relative to the Jan–May 2026 run-rate, with no major shock. | Evidence that September 2026 arrivals were at or above the spring average (e.g., a major event or festival boost) or a sharp collapse (typhoon, policy shock). |
| a2 | 2026-vs-2025 momentum factor applied to September seasonal ratio | 1.08 | 0.95..1.25 | 0.7706..1.541 (widened) | ratio | m2 (m2) | 2025 saw strong YoY growth (Aug +16%, Jan–Aug +12%, p9/p10). Jan–May 2026 monthly average (~4.6M) exceeds the Jan–Aug 2025 average (~4.1M), implying continued positive momentum into 2026. A modest 8% uplift over a neutral seasonal ratio is consistent with decelerating but still-positive growth; rang | 2026 growth momentum persists at a moderate pace through September 2026. | Signs of a 2026 slowdown (e.g., flat or negative YoY in mid-2026 monthly releases) or an acceleration well beyond 2025's pace. |
| a3 | Months in the Jan–May 2026 window | 5 | 5..5 | 3.536..7.071 (widened) | months | m1 (m1), m2 (m2) | Calendar constant: the Jan–May 2026 window in p1 spans exactly five months; used to convert the five-month total to a monthly average. | p1 covers exactly January through May 2026. | Evidence that p1's window is not five months. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 4,375,177 | ['p1'] / ['a1', 'a3'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 5,019,171 | ['p1'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **4,686,124** visitor, 80% interval [2,775,365, 7,912,387] visitor, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total visitor arrivals to Hong Kong (all source markets, visitor trips including same-day and overnight) during calendar September 2026, as first provisionally reported by the HKTB, is 4,686,124 visitor (80% model-based interval 2,775,365 to 7,912,387 visitor; too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

The only 2026 anchor is observed point p1, preliminary arrivals for Jan–May 2026 of 23,000,000 visitor arrivals. Both methods convert this to a September figure: m1 (4,375,177 visitor, weight 50%) applies a shoulder-season ratio of 0.95 (range 0.6697 to 1.339) to the five-month monthly average, using 5 months; m2 (5,019,171 visitor, weight 50%) instead applies a momentum factor of 1.08 (range 0.7706 to 1.541). The two share p1 and are not independent; they differ only in framing, hence the equal weighting.

Main risk: p1 is the sole 2026 anchor, so any error propagates directly, and typhoon/festival timing is uncertain. Missing evidence: actual September 2026 daily arrival counts.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 arrivals as ratio of Jan–May 2026 monthly average (seasonal + momentum): 0.95 ratio, range 0.6697 to 1.339 (range widened by code); used by m1. Overturned by: Evidence that September 2026 arrivals were at or above the spring average (e.g., a major event or festival boost) or a sharp collapse (typhoon, policy shock).
- a2 2026-vs-2025 momentum factor applied to September seasonal ratio: 1.08 ratio, range 0.7706 to 1.541 (range widened by code); used by m2. Overturned by: Signs of a 2026 slowdown (e.g., flat or negative YoY in mid-2026 monthly releases) or an acceleration well beyond 2025's pace.
- a3 Months in the Jan–May 2026 window: 5 months, range 3.536 to 7.071 (range widened by code); used by m1, m2. Overturned by: Evidence that p1's window is not five months.

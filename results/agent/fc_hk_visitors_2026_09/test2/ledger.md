# Evidence ledger: fc_hk_visitors_2026_09

- Question: Assume today is 2026-09-14. You know nothing published after this date. Estimate the total number of visitor arrivals to Hong Kong in September 2026, as it will be first reported (provisional figure) in the Hong Kong Tourism Board's monthly visitor arrivals press release.
- as_of: 2026-09-14
- Pinned target: Total visitor arrivals to Hong Kong (all source markets, all trip purposes, including same-day and overnight visitors) during the calendar month of September 2026, as the provisional figure first published by the Hong Kong Tourism Board in its monthly visitor arrivals press release | unit visitor arrivals (person-trips) | period 2026-09-01..2026-09-30 | publisher Hong Kong Tourism Board (HKTB), monthly visitor arrivals statistics / press release

- Official value (scoring only, never shown to the agent): 4,031,090

## Directions and pages

### d1 [own_history] HKTB monthly statistics

Hypothesis: September 2026 arrivals = most recent reported monthly arrivals (e.g. July/August 2026) scaled by the historical September-to-summer seasonal ratio and by the year-on-year growth trend. Own history gives both the level and the seasonal shape.

Queries issued by the searcher: HKTB monthly visitor arrivals statistics September 2025 provisional; Hong Kong visitor arrivals July 2026 provisional HKTB; HKTB visitor arrivals August 2026 provisional total; 旅發局 2025年8月 訪港旅客 初步 數字 400萬 按年

- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/russia/ru/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indiaoutbound.info/trade-news/indian-arrivals-in-hong-kong-rise-22-3-pc-to-32416-in-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Immigration Department / boundary control points

Hypothesis: HKTB arrivals are derived from Immigration Department arrival records; monthly or daily passenger throughput at land, sea and air control points (especially Mainland visitors via Lo Wu/Lok Ma Chau/High Speed Rail) tracks total arrivals with a stable coverage ratio.

Queries issued by the searcher: Immigration Department Hong Kong passenger traffic statistics monthly 2026 control point arrivals; 入境事務處 各管制站 旅客 統計 2026 入境人次; immd.gov.hk passenger-statistics 20260901 annual passenger statistics monthly total arrivals; HKTB visitor arrivals September 2025 monthly press release total arrivals million

- `https://www.immd.gov.hk/hks/facts/passenger-statistics.html?d=20260901` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.td.gov.hk/filemanager/en/content_5413/table82.xls` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.customs.gov.hk/hcms/filemanager/common/pdf/statistics/passenger_entry_exit_en.pdf` -> **snapshot** (snapshot 20250823075409); points raw/verified 15/0
- `https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/data_specification_for_statistics_passenger_visitor_vehicular_traffic.pdf` -> **snapshot** (snapshot 20230210044128); points raw/verified 0/0
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 15)

### d3 [related_series] Mainland source-market split

Hypothesis: Mainland visitors are ~75-80% of total arrivals; estimating Mainland September 2026 arrivals (from mainland outbound travel data, Greater Bay Area travel patterns, or HKTB Mainland figures) and dividing by the Mainland share gives the total.

Queries issued by the searcher: HKTB monthly visitor arrivals 2026 Mainland visitors July 2026; 香港旅游发展局 2026年7月 访港旅客 数字 内地; HKTB provisional visitor arrivals September 2025 total Mainland 3.2 million; 2026 中秋节 国庆 香港 旅游 预订 内地游客 9月 携程

- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/sc/industry_news/hktb_updates/index.html?id=8291` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nna.jp/news/2957143?media=yahoo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://global.hk01.com/%E7%A4%BE%E4%BC%9A%E6%96%B0%E9%97%BB/60380787/7%E6%9C%88%E8%AE%BF%E6%B8%AF%E6%97%85%E5%AE%A2450%E4%B8%87%E4%BA%BA%E6%AC%A1%E5%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [base_rates] Seasonal and growth base rates

Hypothesis: The September-to-August ratio and September YoY growth rate are stable enough across 2023-2025 to transfer to 2026; deriving these base rates from multi-year history lets code apply them to the latest known 2026 level.

Queries issued by the searcher: Hong Kong visitor arrivals monthly 2023 2024 2025 table HKTB; HKTB monthly visitor arrivals statistics press release September 2025; HKTB provisional visitor arrivals 2025 full year December 2025 49 million monthly breakdown; Hong Kong visitor arrivals July 2026 provisional HKTB monthly

- `https://www.censtatd.gov.hk/en/data/stat_report/product/B1010002/att/B10100022024MM11B0100.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/research_statistics/research_publications/index.html?id=3631` -> **snapshot** (snapshot 20260309210037); points raw/verified 0/0
- `https://dailyhongkong.com/wp-content/uploads/2025/10/10-September-Arrivals-E.pdf` -> **snapshot** (snapshot 20251015203835); points raw/verified 15/15
  - p1 Provisional total visitor arrivals to Hong Kong, September 2025 = **3,292,197** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p2 Year-on-year change in total visitor arrivals to Hong Kong, September 2025 = **8** % (2025-09-01..2025-09-30) [keep: ] quote: "Hong Kong for September were close to 3.3 million, an 8% increase compared to the same month last year."
  - p3 Provisional total visitor arrivals to Hong Kong, January to September 2025 (cumu = **36,471,648** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "Total 3,292,197 (+8%) 36,471,648 (+12%)"
  - p4 Year-on-year change in total visitor arrivals to Hong Kong, January to September = **12** % (2025-01-01..2025-09-30) [keep: ] quote: "The preliminary visitor arrivals for the first three quarters of this year stand at over 36 million, representing a 12% increase compared to the same period last year."
  - p5 Provisional Chinese Mainland visitor arrivals to Hong Kong, September 2025 = **2,458,439** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "Chinese Mainland 2,458,439 (+7%) 27,985,883 (+11%)"
  - p6 Year-on-year change in Chinese Mainland visitor arrivals to Hong Kong, September = **7** % (2025-09-01..2025-09-30) [keep: ] quote: "Chinese Mainland 2,458,439 (+7%) 27,985,883 (+11%)"
  - p7 Provisional non-Chinese Mainland visitor arrivals to Hong Kong, September 2025 = **833,758** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "Non-Chinese Mainland 833,758 (+9%) 8,485,765 (+16%)"
  - p8 Year-on-year change in non-Chinese Mainland visitor arrivals to Hong Kong, Septe = **9** % (2025-09-01..2025-09-30) [keep: ] quote: "Non-Chinese Mainland 833,758 (+9%) 8,485,765 (+16%)"
  - p9 Provisional short-haul visitor arrivals to Hong Kong, September 2025 = **461,889** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "Short-haul 461,889 (+9%) 4,661,848 (+17%)"
  - p10 Provisional long-haul visitor arrivals to Hong Kong, September 2025 = **239,475** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "Long-haul 239,475 (+14%) 2,412,106 (+18%)"
  - p11 Provisional new markets visitor arrivals to Hong Kong, September 2025 = **59,196** visitor arrivals (person-trips) (2025-09-01..2025-09-30) [keep: ] quote: "New markets 59,196 (+13%) 535,522 (+14%)"
  - p12 Provisional Chinese Mainland visitor arrivals to Hong Kong, January to September = **27,985,883** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "Chinese Mainland 2,458,439 (+7%) 27,985,883 (+11%)"
  - p13 Provisional non-Chinese Mainland visitor arrivals to Hong Kong, January to Septe = **8,485,765** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "Non-Chinese Mainland 833,758 (+9%) 8,485,765 (+16%)"
  - p14 Provisional short-haul visitor arrivals to Hong Kong, January to September 2025  = **4,661,848** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "Short-haul 461,889 (+9%) 4,661,848 (+17%)"
  - p15 Provisional long-haul visitor arrivals to Hong Kong, January to September 2025 ( = **2,412,106** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "Long-haul 239,475 (+14%) 2,412,106 (+18%)"
- `https://partnernet.hktb.com/india/en/industry_news/hktb_updates/index.html?id=8688` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] Hotels and aviation

Hypothesis: Overnight visitor arrivals scale with hotel room-nights sold and with airport/HSR inbound seat capacity times load factor; September 2026 hotel occupancy and inbound flight/HSR bookings constrain the overnight component, which can be grossed up to total arrivals via the overnight share.

Queries issued by the searcher: Hong Kong hotel occupancy rate 2026 monthly room nights sold; Hong Kong International Airport passenger traffic August 2026; High Speed Rail West Kowloon passenger numbers 2026 daily average MTR; HKTB visitor arrivals July 2026 overnight visitors share same-day

- `https://partnernet.hktb.com/china/sc/home/index.html` -> **snapshot** (snapshot 20260730164207); points raw/verified 0/0
- `https://cbsa.hkust.edu.hk/news/summer-events-draw-tourists-summer-spending-faces-uncertainty-chinese` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=20260801` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/research_statistics/research_publications/index.html?id=3634` -> **snapshot** (snapshot 20251107130830); points raw/verified 0/0

### d6 [shocks] Calendar and event effects

Hypothesis: September 2026 calendar effects (Mid-Autumn Festival date, National Day Golden Week starting Oct 1 pulling travel forward or back, typhoon disruptions, any visa or policy changes) shift arrivals relative to a naive seasonal extrapolation; quantifying the holiday timing and any known disruptions adjusts the seasonal factor.

Queries issued by the searcher: Hong Kong Mid-Autumn Festival 2026 date September 25; Hong Kong Tourism Board monthly visitor arrivals statistics September; Hong Kong 2026 public holidays gazette Mid-Autumn Festival day following day September 26; Hong Kong typhoon signal September 2026 tropical cyclone disruption

- `https://www.gov.hk/en/about/abouthk/holiday/2026.htm` -> **snapshot** (snapshot 20260830105600); points raw/verified 2/0
- `https://www.gld.gov.hk/egazette/english/gazette/file.php?year=2025&vol=29&no=20&extra=0&type=0&number=2965` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hko.gov.hk/en/Press-Releases/110730/Moon-watching-tips-for-Mid-Autumn-Festival-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinadailyhk.com/hk/article/641143` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end 2026-09-26 after as_of: 1; period_end 2026-10-01 after as_of: 1)

### d7 [forecasts_markets] Official and analyst forecasts

Hypothesis: HKTB or government full-year 2026 visitor arrival targets/forecasts, and analyst or airline forecasts, imply a September level when combined with year-to-date actuals and the historical monthly distribution; forecasts constrain the plausible range.

Queries issued by the searcher: HKTB 2026 visitor arrivals forecast target full year; 旅發局 2026 全年 訪港旅客 預測; 旅發局 2026年8月 訪港旅客 初步數字 按年; HKTB August 2026 visitor arrivals million year-on-year; "September" 2025 Hong Kong visitor arrivals 3.3 million HKTB monthly

- `https://www.chinadailyhk.com/hk/article/629562` -> **snapshot** (snapshot 20260421102435); points raw/verified 12/0
- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p16 Hong Kong visitor arrivals in first five months of 2026 (preliminary, approximat = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [keep: ] quote: "in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://e.vnexpress.net/news/travel/places/world-s-second-most-visited-city-records-40-million-tourists-in-nine-months-5133459.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stheadline.com/daily-hongkong/3627277/%e7%9b%9b%e4%ba%8b%e6%b5%aa%e6%8e%a5%e6%b5%aa%e5%85%a8%e5%b9%b4%e6%97%85%e5%ae%a2%e5%8b%a2%e9%81%94%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (period_end 2026-12-31 after as_of: 8; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end missing or unparseable: 4)

### b1 [own_history] HKTB monthly release

Hypothesis: The most recent reported monthly arrivals (July and August 2026) would anchor the level for a September 2026 extrapolation via the September-to-August seasonal ratio; without them the estimate relies on the Jan-May 2026 run-rate and a transfer assumption.

Queries issued by the searcher: HKTB provisional visitor arrivals August 2026; 香港旅發局 2026年7月 訪港旅客 初步數字; 旅發局 2026年6月 初步訪港旅客 數字 公布; HKTB September 2025 visitor arrivals provisional total 3.2 million

- `https://partnernet.hktb.com/germany/de/industry_news/hktb_updates/index.html?id=9568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/china/sc/industry_news/hktb_updates/index.html?id=9328` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/research_statistics/visitor_arrival_statistics/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Immigration Department / control points

Hypothesis: Daily/monthly passenger throughput at land, sea and air control points for mid-2026 tracks HKTB arrivals with a stable coverage ratio, giving a near-real-time level for the September 2026 run-rate.

Queries issued by the searcher: Immigration Department monthly arrival passenger statistics 2026 Hong Kong control points; Hong Kong Tourism Board visitor arrivals July 2026 provisional figure; immd.gov.hk passenger-statistics 20260913 入境 內地訪客 其他訪客 總計; 入境事務處 2026年8月 訪港旅客 初步數字 旅發局 公布

- `https://www.immd.gov.hk/eng/facts/passenger-statistics.html?d=26` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.td.gov.hk/filemanager/en/content_5413/table82.xls` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic` -> **snapshot** (snapshot 20260521200912); points raw/verified 0/0

### b3 [forecasts_markets] Government/HKTB full-year 2026 target

Hypothesis: A full-year 2026 visitor arrival target combined with Jan-May 2026 actuals (p16) and the historical monthly distribution would constrain the September level and resolve uncertainty in the growth trend.

Queries issued by the searcher: HKTB 2026 full-year visitor arrivals forecast target; Hong Kong visitor arrivals 2026 forecast 46 million; Hong Kong Tourism Board visitor arrivals May 2026 monthly statistics press release; Hong Kong September 2025 visitor arrivals HKTB 3.3 million September

- `https://www.info.gov.hk/gia/general/202606/09/P2026060900749.htm` -> **snapshot** (snapshot 20260610103727); points raw/verified 5/1
  - p17 Total visitor arrivals to Hong Kong, preliminary, first five months of 2026 = **23,000,000** visitor arrivals (2026-01-01..2026-05-31) [DISCARD: Redundant duplicate of p16 (same ~23 million Jan-May 2026 preliminary figure from the same government speech); keeping b] quote: "According to preliminary figures, in the first five months of this year alone, we welcomed approximately 23 million visitor arrivals"
- `https://partnernet.hktb.com/en/industry_news/hktb_updates/index.html?id=9129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestandard.com.hk/news/article/328325/HKs-average-overnight-visitor-stay-shortens-by-01-night-despite-rise-in-numbers` -> **snapshot** (snapshot 20260418073806); points raw/verified 11/8
  - p18 Overall visitor arrivals to Hong Kong, full year 2025 (actual) = **49,900,000** visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "with overall visitor arrivals in 2025 reaching approximately 49.9 million, a 12 percent increase, the HKTB's 2026/27 work plan shows."
  - p19 Year-on-year increase in overall visitor arrivals, full year 2025 = **12** % (2025-01-01..2025-12-31) [keep: ] quote: "with overall visitor arrivals in 2025 reaching approximately 49.9 million, a 12 percent increase, the HKTB's 2026/27 work plan shows."
  - p20 Overnight visitor arrivals to Hong Kong, full year 2025 (actual) = **23,190,000** overnight visitor arrivals (2025-01-01..2025-12-31) [keep: ] quote: "despite their numbers increasing by 6 percent year-on-year to 23.19 million, according to the Hong Kong Tourism Board (HKTB)."
  - p21 Year-on-year increase in overnight visitor arrivals, full year 2025 = **6** % (2025-01-01..2025-12-31) [keep: ] quote: "despite their numbers increasing by 6 percent year-on-year to 23.19 million, according to the Hong Kong Tourism Board (HKTB)."
  - p22 Average length of stay for overnight visitors, full year 2025 = **3.1** nights (2025-01-01..2025-12-31) [keep: ] quote: "Hong Kong saw a decrease in the average length of stay for overnight visitors to 3.1 nights last year"
  - p23 Year-on-year change in average length of stay for overnight visitors, full year  = **0.1** nights (2025-01-01..2025-12-31) [keep: ] quote: "a slight decrease of 0.1 nights compared to the previous year"
  - p24 Per capita spending for overnight visitors, full year 2025 = **5,503** HKD per overnight visitor (2025-01-01..2025-12-31) [keep: ] quote: "Per capita spending for overnight visitors last year was HK$5,503, a figure similar to 2024"
  - p25 Visitor satisfaction score (scale of 10), full year 2025 = **8.9** score out of 10 (2025-01-01..2025-12-31) [keep: ] quote: "while visitor satisfaction, on a scale of 10, rose to 8.9, an increase of 0.1 points."
- `https://www.chinadailyhk.com/hk/article/629562` -> **snapshot** (snapshot 20260421102435); points raw/verified 13/0
- dropped by code checks: 20 (period_end 2026-12-31 after as_of: 12; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end missing or unparseable: 4)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hong kong tourism', 'visitor arrivals', 'september 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Same HKTB September 2025 release: p1 is the level and p2 the YoY change; internally consistent (3.29m, +8%). Both are the same underlying measurement, not independent.
- corroborating: ['p1', 'p5', 'p7'] September 2025 total decomposes into Mainland (p5) + non-Mainland (p7); the parts sum to the total, confirming internal consistency of the same release.
- corroborating: ['p5', 'p6'] Mainland September 2025 level and its YoY change from the same release.
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11'] Non-Mainland sub-segments (short-haul, long-haul, new markets) are nested within the non-Mainland total; overlapping coverage, same source.
- corroborating: ['p3', 'p4', 'p12', 'p13'] Cumulative Jan-Sep 2025 totals and their components from the same release; consistent with the monthly figures.
- corroborating: ['p1', 'p16'] p16 (approx 23m in first five months of 2026) implies a 2026 run-rate well above 2025; consistent with continued growth from the 2025 base in p1/p3. Different period and source (govt speech vs HKTB re
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] p1 is the September 2025 total level and p2 is its YoY growth; both come from the same HKTB release, so they are internally consistent but not independent. p2 implies a September 2024 base of about 3.
- corroborating: ['p1', 'p5', 'p7'] p5 (Mainland) + p7 (non-Mainland) sum to p1 (total), confirming the segment split is exhaustive for September 2025. Same source/release, so this is a definitional check, not independent confirmation.
- corroborating: ['p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11'] Segment YoY growth rates (Mainland +7%, non-Mainland +9%, short-haul +9%, long-haul +14%, new markets +13%) are all positive and bracket the total +8%, consistent with a broad-based recovery in Septem
- corroborating: ['p3', 'p4', 'p12', 'p13'] Cumulative Jan-Sep 2025 totals and their YoY growth are internally consistent with the monthly September figures; same HKTB release.
- redundant: ['p16', 'p17'] p16 and p17 are the same ~23 million Jan-May 2026 preliminary figure from the same government speech; they are duplicate copies, not independent corroboration.
- corroborating: ['p16', 'p18', 'p19'] Full-year 2025 ~49.9m (p18) with +12% growth (p19) and Jan-May 2026 ~23m (p16) are consistent with continued strong 2026 momentum; the Jan-May 2026 run-rate (~4.6m/month) is above the 2025 monthly ave
- corroborating: ['p20', 'p21', 'p22', 'p23', 'p24', 'p25'] Overnight arrivals, length of stay, per-capita spend and satisfaction are contextual quality metrics from the same HKTB work-plan reporting; they do not directly measure September 2026 total arrivals 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | 2026 YoY growth factor for September total arrivals vs September 2025 | 1.1 | 1.02..1.2 | 0.9895..1.237 (widened) | ratio | m1 (m1) | September 2025 grew +8% YoY (p2). The Jan-May 2026 run-rate (~23m in 5 months, p16) is above the 2025 monthly average implied by p18 (~4.16m/month), indicating continued positive but moderating growth. Central factor 1.10 with a wide range reflecting uncertainty about H2 2026 momentum and any policy | September 2026 growth continues the 2025-2026 recovery trend without major disruption (typhoon, visa policy, economic shock). | Evidence of a sharp 2026 slowdown, new travel restrictions, or a major disruption in September 2026 that breaks the trend. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,646,153 | ['p1'] / ['a1'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **3,646,153** visitor, 80% interval [2,646,623, 5,023,166] visitor, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total visitor arrivals to Hong Kong (all source markets, all trip purposes, same-day and overnight) during September 2026, as the provisional HKTB figure, is 3,646,153 visitor (80% model-based interval 2,646,623 to 5,023,166 visitor).

The estimate anchors on the observed September 2025 provisional total of 3,292,197 visitor arrivals (person-trips) and applies a YoY growth factor of 1.1 (range 0.9895 to 1.237). That factor is an assumption, not an observation: it reflects September 2025's growth and the stronger early-2026 run-rate, with moderating momentum assumed. The YoY factor already embeds September seasonality, so no separate seasonal adjustment is applied. Only one method was used (1), carrying weight 100%, so the combination is effectively that single method rather than an independent cross-check.

The main risk is the assumed growth factor: H2 2026 momentum, policy changes, or a Mainland travel shift could move arrivals well outside the range. The most useful missing evidence would be actual July–August 2026 monthly arrivals, which would pin down the current run-rate before September.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 2026 YoY growth factor for September total arrivals vs September 2025: 1.1 ratio, range 0.9895 to 1.237 (range widened by code); used by m1. Overturned by: Evidence of a sharp 2026 slowdown, new travel restrictions, or a major disruption in September 2026 that breaks the trend.

# Evidence ledger: fc_pola_teu_2026_09

- Question: Assume today is 2026-09-10. You know nothing published after this date. Estimate the total container volume handled by the Port of Los Angeles in September 2026, in TEUs (twenty-foot equivalent units; loaded and empty imports and exports combined), as it will be first reported in the Port of Los Angeles's monthly cargo news release.
- as_of: 2026-09-10
- Pinned target: Total container volume (loaded + empty, imports + exports, all containerized cargo) handled by the Port of Los Angeles during September 2026, as first reported in the Port's monthly cargo news release (TEUs) | unit TEU | period 2026-09-01..2026-09-30 | publisher Port of Los Angeles (Port of Los Angeles monthly cargo news release / TEU statistics)

- Official value (scoring only, never shown to the agent): 1,042,652

## Directions and pages

### d1 [own_history] Port of Los Angeles published monthly TEU statistics

Hypothesis: September 2026 total TEU will follow the Port's own recent monthly levels adjusted for September seasonality; the most recent months published before cutoff (through ~July/August 2026) anchor the level, and prior Septembers give the seasonal multiplier.

Queries issued by the searcher: Port of Los Angeles monthly container statistics 2026 TEU; Port of Los Angeles cargo news release August 2026 TEU; Port of Los Angeles September 2025 cargo volume TEUs news release record; "Port of Los Angeles" September 2024 TEU container volume total monthly

- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 15/15
  - p1 Port of LA total container volume (TEUs), July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p2 Port of LA total container volume (TEUs), July 2025 = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p3 Port of LA loaded imports (TEUs), July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p4 Port of LA loaded exports (TEUs), July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p5 Port of LA total loaded (TEUs), July 2026 = **611,327** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p6 Port of LA total empty (TEUs), July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p7 Port of LA loaded imports (TEUs), July 2025 = **543,728** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p8 Port of LA loaded exports (TEUs), July 2025 = **121,507** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p9 Port of LA total loaded (TEUs), July 2025 = **665,235** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p10 Port of LA total empty (TEUs), July 2025 = **354,602** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p11 Port of LA calendar year 2026 cumulative total container volume (TEUs), through  = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p12 Port of LA calendar year 2025 cumulative total container volume (TEUs), through  = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p13 Port of LA annual total container volume (TEUs), calendar year 2025 = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
  - p14 Port of LA annual total container volume (TEUs), calendar year 2024 = **10,297,352** TEU (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p15 Port of LA annual total container volume (TEUs), calendar year 2023 = **8,629,681** TEU (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023 \| 8,629,681 \| 2013 \| 7,868,582 \| 2003 \| 7,178,940 \| 1993 \| 2,318,920 \| 1983 \| 733,979 \|"
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/august-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://app.eesea.com/news/september-cargo-volume-boosts-port-of-los-angeles-to-record-quarter` -> **snapshot** (snapshot 20260510110354); points raw/verified 11/10
  - p16 Port of Los Angeles total TEUs processed in September 2025 = **883,053** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "The Port of Los Angeles processed 883,053 Twenty-Foot Equivalent Units (TEUs) in September."
  - p17 Port of Los Angeles September 2025 total TEU change vs prior year = **7.5** % (2025-09-01..2025-09-30) [DISCARD: Redundant restatement of the -7.5% YoY change already implied by p16 vs prior year; adds no new information.] quote: "While cargo eased 7.5% compared to last year, it helped propel the Port to its best quarter on record."
  - p18 Port of Los Angeles September 2025 loaded imports TEUs = **460,044** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "September 2025 loaded imports came in at 460,044 TEUs, 7.6% less than last year."
  - p19 Port of Los Angeles September 2025 loaded imports change vs prior year = **7.6** % (2025-09-01..2025-09-30) [DISCARD: Redundant restatement of the -7.6% import change; the level p18 is kept.] quote: "September 2025 loaded imports came in at 460,044 TEUs, 7.6% less than last year."
  - p20 Port of Los Angeles September 2025 loaded exports TEUs = **114,693** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "Loaded exports landed at 114,693 TEUs, about the same as 2024."
  - p21 Port of Los Angeles September 2025 empty container units = **308,317** empty container units (2025-09-01..2025-09-30) [keep: ] quote: "The Port handled 308,317 empty container units, 10% less than last year."
  - p22 Port of Los Angeles September 2025 empty container units change vs prior year = **10** % (2025-09-01..2025-09-30) [DISCARD: Redundant restatement of the -10% empty change; level p21 kept.] quote: "The Port handled 308,317 empty container units, 10% less than last year."
  - p23 Port of Los Angeles third quarter 2025 total TEUs = **2,900,000** TEUs (2025-07-01..2025-09-30) [keep: ] quote: "The Port closed out the third quarter moving 2.9 million TEUs, its best three-month quarter ever."
  - p24 Port of Los Angeles cumulative TEUs January through September 2025 = **7,817,057** TEUs (2025-01-01..2025-09-30) [keep: ] quote: "Nine months into 2025, the Port of Los Angeles has handled 7,817,057 TEUs, 3% more than the same period in 2024."
  - p25 Port of Los Angeles cumulative TEUs Jan-Sep 2025 change vs same period 2024 = **3** % (2025-01-01..2025-09-30) [DISCARD: Redundant restatement of Jan-Sep 2025 +3%; level p24 kept.] quote: "Nine months into 2025, the Port of Los Angeles has handled 7,817,057 TEUs, 3% more than the same period in 2024."
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d2 [related_series] San Pedro Bay complex / Port of Long Beach and combined LA-LB

Hypothesis: LA's share of the San Pedro Bay complex is relatively stable; if Long Beach September 2026 or combined complex data are available, LA TEU ≈ complex total × LA share. Also LA+LB combined can be cross-checked against national import volumes.

Queries issued by the searcher: Port of Long Beach monthly TEU August 2026 cargo; Port of Los Angeles monthly cargo TEU July 2026; Port of Long Beach July 2026 928,508 TEU second-busiest July; Port of Los Angeles September 2025 TEU cargo volume monthly

- `https://www.pmsaship.com/maritime-insights-blog/july-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.porttechnology.org/port-of-long-beach-posts-second-busiest-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/news/economic-indicators/port-of-los-angeles-posts-high-july-volume-helped-by-retail-goods-ai-project-parts-4866098` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National containerized import/export flows (Census/CBP, Descartes, NRF imports)

Hypothesis: LA handles a roughly stable share of US containerized imports; national September 2026 import volumes (or forecasts) times LA's share gives an independent estimate of loaded imports, to which empties and exports are added.

Queries issued by the searcher: NRF Global Port Tracker September 2026 forecast container imports; Descartes US container imports TEU August 2026; Port of Los Angeles share of US container imports percent 2026 Descartes port rankings; "Port of Los Angeles" August 2026 cargo 955,907 TEU monthly release

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hellenicshippingnews.com/descartes-releases-september-global-shipping-report-august-u-s-containerized-imports-reach-third-highest-level-on` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.cargonews.co.kr/news/articleView.html?idxno=60080` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.indexbox.io/blog/nrf-raises-us-container-import-forecast-for-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Industry forecasts and Port guidance

Hypothesis: Published forecasts (Global Port Tracker, Port of LA executive statements, PMA/ILWU commentary) for late-2026 volumes constrain the September level; direction of forecast vs. prior year indicates growth/decline.

Queries issued by the searcher: Port of Los Angeles 2026 cargo forecast container volume; Global Port Tracker 2026 second half imports forecast; Port of Los Angeles August 2026 container volumes Seroka September outlook; "Global Port Tracker" September 2026 forecast 2.28 million TEU released

- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gcaptain.com/port-of-los-angeles-caps-record-summer-as-u-s-import-strength-holds-up/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.freightwaves.com/news/port-of-los-angeles-forecasts-7-container-volume-decline` -> **snapshot** (snapshot 20260823020107); points raw/verified 15/2
  - p26 China share of all containerized imports through Los Angeles, 2025 = **53.4** % (2025-01-01..2025-12-31) [keep: ] quote: "China's share of all containerized imports through Los Angeles has fallen to about 40% in 2026, down from 53.4% in 2025 and 61% in 2020."
  - p27 China share of all containerized imports through Los Angeles, 2020 = **61** % (2020-01-01..2020-12-31) [keep: ] quote: "China's share of all containerized imports through Los Angeles has fallen to about 40% in 2026, down from 53.4% in 2025 and 61% in 2020."
- dropped by code checks: 13 (period_end 2027-06-30 after as_of: 10; period_end 2026-12-31 after as_of: 1; period_end missing or unparseable: 2)

### d5 [shocks] Tariff policy and trade shocks affecting transpacific flows

Hypothesis: Tariff changes, front-loading/pull-forward effects, and any 2026 policy shifts alter the seasonal pattern; identifying whether September 2026 is in a pull-forward, payback, or steady state adjusts the seasonal multiplier.

Queries issued by the searcher: US China tariff 2026 container imports impact Port of Los Angeles; transpacific front-loading 2026 imports pull-forward tariffs; Port of Los Angeles July 2026 cargo volume TEUs monthly; Port of Los Angeles cargo briefing August 2026 volumes outlook peak season

- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p28 Total TEUs handled by Port of Los Angeles in July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p29 Total TEUs handled by Port of Los Angeles in June 2026 (stated as topping 1 mill = **1,000,000** TEU (2026-06-01..2026-06-30) [DISCARD: Already discarded; imprecise 'topping 1 million' statement.] quote: "After topping 1 million container units in June, we nearly reached that mark again in July"
  - p30 Year-over-year change in Port of Los Angeles July 2026 cargo volume = **6** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -6%; level p28 kept.] quote: "July cargo was 6% lower than last year's all-time record for the month"
  - p31 Port of Los Angeles July 2026 volume above five-year July average (share) = **7.5** % (2026-07-01..2026-07-31) [keep: ] quote: "Despite the year-over-year decline, July volume was 7.5% above the Port's five-year average for the month."
  - p32 Loaded imports at Port of Los Angeles in July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p33 Year-over-year change in Port of Los Angeles loaded imports, July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -8%; level p32 kept.] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p34 Port of Los Angeles July 2026 loaded imports above five-year July average (share = **6** % (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p35 Loaded exports at Port of Los Angeles in July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p36 Year-over-year change in Port of Los Angeles loaded exports, July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -8%; level p35 kept.] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p37 Empty containers at Port of Los Angeles in July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p38 Year-over-year change in Port of Los Angeles empty containers, July 2026 = **2** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -2%; level p37 kept.] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p39 Cumulative total TEUs handled by Port of Los Angeles, first seven months of 2026 = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p40 Year-over-year change in Port of Los Angeles cumulative TEUs, first seven months = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Redundant restatement of +1.8%; level p39 kept.] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
- `https://hk.marketscreener.com/news/port-of-los-angeles-posts-high-july-volume-helped-by-retail-goods-ai-project-parts--ce7859dddc89f121` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://theloadstar.com/transpacifc/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.freightwaves.com/news/port-of-los-angeles-forecasts-7-container-volume-decline` -> **snapshot** (snapshot 20260823020107); points raw/verified 15/2
  - p41 China's share of all containerized imports through Port of Los Angeles, 2025 = **53.4** % (2025-01-01..2025-12-31) [keep: ] quote: "China's share of all containerized imports through Los Angeles has fallen to about 40% in 2026, down from 53.4% in 2025 and 61% in 2020."
  - p42 China's share of all containerized imports through Port of Los Angeles, 2020 = **61** % (2020-01-01..2020-12-31) [keep: ] quote: "China's share of all containerized imports through Los Angeles has fallen to about 40% in 2026, down from 53.4% in 2025 and 61% in 2020."
- dropped by code checks: 13 (period_end 2027-06-30 after as_of: 10; period_end 2026-12-31 after as_of: 1; period_end missing or unparseable: 2)

### d6 [base_rates] Empty container share and export/import balance

Hypothesis: Total TEU = loaded imports × (1 + export/import ratio + empty/loaded ratio). Historical ratios for LA (empties ~20-25% of total, exports ~25-30% of imports) let a loaded-import estimate be scaled to total.

Queries issued by the searcher: Port of Los Angeles TEU loaded empty exports imports monthly 2025; Port of Los Angeles empty container share of total TEU percent; portoflosangeles.org historical-teu-statistics-2026 container statistics July 2026; "Port of Los Angeles" July 2026 TEU loaded imports loaded exports empty containers

- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2025` -> **snapshot** (snapshot 20260122223542); points raw/verified 15/15
  - p43 Port of LA September 2025 loaded imports (TEUs) = **460,044** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p44 Port of LA September 2025 loaded exports (TEUs) = **114,693** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p45 Port of LA September 2025 empty exports (TEUs) = **308,040** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p46 Port of LA September 2025 total TEUs = **883,053** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p47 Port of LA September 2025 total exports (TEUs) = **422,734** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p48 Port of LA September 2025 empty imports (TEUs) = **276** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p49 Port of LA calendar year 2025 loaded imports (TEUs) = **5,316,713** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p50 Port of LA calendar year 2025 loaded exports (TEUs) = **1,429,260** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p51 Port of LA calendar year 2025 empty exports (TEUs) = **3,489,552** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p52 Port of LA calendar year 2025 total TEUs = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p53 Port of LA fiscal year 2024/25 loaded imports (TEUs) = **5,438,495** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year 2024/25 loaded imports; different period, not usable for September 2026 and redundant with calendar-year p49] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
  - p54 Port of LA fiscal year 2024/25 loaded exports (TEUs) = **1,428,787** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year 2024/25 loaded exports; different period, redundant with p50.] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
  - p55 Port of LA fiscal year 2024/25 empty exports (TEUs) = **3,647,009** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year 2024/25 empty exports; different period, redundant with p51.] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
  - p56 Port of LA fiscal year 2024/25 total TEUs = **10,521,673** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year 2024/25 total; different period, redundant with p52.] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
  - p57 Port of LA fiscal year 2025/26 in progress loaded imports (TEUs) = **2,768,485** TEU (2025-07-01..2025-12-31) [DISCARD: Already discarded in round 1; fiscal-year partial, not usable.] quote: "\| Total Fiscal Year 2025/26 (in progress) \| 2,768,485.30 \| 1,338.15 \| 2,769,823.45 \| 709,124.00 \| 1,804,559.25 \| 2,513.683.25 \| 5,283,506.70 \| -5.07% \|"
- `https://gcaptain.com/port-of-los-angeles-nears-1-million-teus-in-second-busiest-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://english.news.cn/northamerica/20251016/536c5ce80a8f44beb71a75015b218be0/c.html` -> **snapshot** (snapshot 20251016101956); points raw/verified 14/14
  - p58 Port of Los Angeles total container volume (loaded + empty, imports + exports),  = **883,053** TEU (2025-09-01..2025-09-30) [keep: ] quote: "The Port of Los Angeles (POLA) handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p59 Port of Los Angeles total container volume year-on-year change, September = **7.5** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p17/p87 (September 2025 -7.5% YoY).] quote: "handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p60 Port of Los Angeles loaded imports, September = **460,044** TEU (2025-09-01..2025-09-30) [keep: ] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p61 Port of Los Angeles loaded imports year-on-year change, September = **7.6** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p19/p89.] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p62 Port of Los Angeles loaded exports, September = **114,693** TEU (2025-09-01..2025-09-30) [keep: ] quote: "while loaded exports stood at 114,693 TEUs, roughly the same as in 2024"
  - p63 Port of Los Angeles empty containers processed, September = **308,317** TEU (2025-09-01..2025-09-30) [keep: ] quote: "The port also processed 308,317 empty containers last month, 10 percent fewer than a year ago."
  - p64 Port of Los Angeles empty containers year-on-year change, September = **10** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p22/p92.] quote: "processed 308,317 empty containers last month, 10 percent fewer than a year ago"
  - p65 Forecast: major U.S. ports total container volume, October (NRF/Hackett Associat = **1,970,000** TEU (2025-10-01..2025-10-31) [keep: ] quote: "It projected that major U.S. ports could see 1.97 million TEUs in October, down 12.3 percent year on year"
  - p66 Forecast: major U.S. ports total container volume year-on-year change, October = **12.3** % (2025-10-01..2025-10-31) [DISCARD: Redundant restatement of -12.3%; level p65 kept.] quote: "major U.S. ports could see 1.97 million TEUs in October, down 12.3 percent year on year"
  - p67 Forecast: major U.S. ports total container volume, November (NRF/Hackett Associa = **1,750,000** TEU (2025-11-01..2025-11-30) [keep: ] quote: "1.75 million in November, down 19.2 percent"
  - p68 Forecast: major U.S. ports total container volume year-on-year change, November = **19.2** % (2025-11-01..2025-11-30) [DISCARD: Redundant restatement of -19.2%; level p67 kept.] quote: "1.75 million in November, down 19.2 percent"
  - p69 Forecast: major U.S. ports total container volume, December (NRF/Hackett Associa = **1,720,000** TEU (2025-12-01..2025-12-31) [keep: ] quote: "and 1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"
  - p70 Forecast: major U.S. ports total container volume year-on-year change, December = **19.4** % (2025-12-01..2025-12-31) [DISCARD: Redundant restatement of -19.4%; level p69 kept.] quote: "and 1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"
  - p71 Predicted threshold: monthly import volumes at major U.S. container ports (indus = **2,000,000** TEU (..) [DISCARD: Already discarded; industry threshold, not a measurement.] quote: "Industry insiders predict that current U.S. trade policies could cause monthly import volumes at major container ports to drop below the 2 million TEU mark for the rest of the year."
- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 14/14
  - p72 Port of LA loaded imports, July 2026 (TEUs) = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p73 Port of LA loaded exports, July 2026 (TEUs) = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p74 Port of LA total loaded, July 2026 (TEUs) = **611,327** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p75 Port of LA total empty, July 2026 (TEUs) = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p76 Port of LA total container volume, July 2026 (TEUs) = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p77 Port of LA loaded imports, July 2025 (TEUs) = **543,728** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p78 Port of LA loaded exports, July 2025 (TEUs) = **121,507** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p79 Port of LA total loaded, July 2025 (TEUs) = **665,235** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p80 Port of LA total empty, July 2025 (TEUs) = **354,602** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p81 Port of LA total container volume, July 2025 (TEUs) = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p82 Port of LA calendar year 2026 cumulative total container volume (TEUs) = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p83 Port of LA calendar year 2025 cumulative total container volume (TEUs) = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p84 Port of LA annual total container volume, 2024 (TEUs) = **10,297,352** TEU (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p85 Port of LA annual total container volume, 2025 (TEUs) = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"

### d7 [physical_flow] Terminal capacity and vessel calls at LA terminals

Hypothesis: Total TEU ≈ terminal capacity × utilization × days; vessel arrival schedules and terminal throughput capacity bound the September figure.

Queries issued by the searcher: Port of Los Angeles terminal capacity TEU annual; Port of Los Angeles monthly cargo news release TEU statistics 2025; Port of Los Angeles container terminal capacity million TEU per year Pier 400 APM Terminals capacity; Port of Los Angeles container vessel calls 2025 average TEU per vessel call

- `https://english.news.cn/northamerica/20251016/536c5ce80a8f44beb71a75015b218be0/c.html` -> **snapshot** (snapshot 20251016101956); points raw/verified 14/13
  - p86 Total TEUs handled by Port of Los Angeles in September = **883,053** TEU (2025-09-01..2025-09-30) [keep: ] quote: "The Port of Los Angeles (POLA) handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p87 Year-on-year percent change in total TEUs at Port of Los Angeles in September = **7.5** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p59/p17.] quote: "handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p88 Loaded imports at Port of Los Angeles in September = **460,044** TEU (2025-09-01..2025-09-30) [keep: ] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p89 Year-on-year percent change in loaded imports at Port of Los Angeles in Septembe = **7.6** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p61/p19.] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p90 Loaded exports at Port of Los Angeles in September = **114,693** TEU (2025-09-01..2025-09-30) [keep: ] quote: "while loaded exports stood at 114,693 TEUs, roughly the same as in 2024"
  - p91 Empty containers processed at Port of Los Angeles in September = **308,317** TEU (2025-09-01..2025-09-30) [keep: ] quote: "The port also processed 308,317 empty containers last month, 10 percent fewer than a year ago."
  - p92 Year-on-year percent change in empty containers at Port of Los Angeles in Septem = **10** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p64/p22.] quote: "processed 308,317 empty containers last month, 10 percent fewer than a year ago"
  - p93 NRF/Hackett projected total TEUs at major U.S. ports in October = **1,970,000** TEU (2025-10-01..2025-10-31) [keep: ] quote: "It projected that major U.S. ports could see 1.97 million TEUs in October, down 12.3 percent year on year"
  - p94 Year-on-year percent change in projected October TEUs at major U.S. ports = **12.3** % (2025-10-01..2025-10-31) [DISCARD: Redundant restatement of -12.3%; level p93 kept.] quote: "major U.S. ports could see 1.97 million TEUs in October, down 12.3 percent year on year"
  - p95 NRF/Hackett projected total TEUs at major U.S. ports in November = **1,750,000** TEU (2025-11-01..2025-11-30) [keep: ] quote: "1.75 million in November, down 19.2 percent"
  - p96 Year-on-year percent change in projected November TEUs at major U.S. ports = **19.2** % (2025-11-01..2025-11-30) [DISCARD: Redundant restatement of -19.2%; level p95 kept.] quote: "1.75 million in November, down 19.2 percent"
  - p97 NRF/Hackett projected total TEUs at major U.S. ports in December = **1,720,000** TEU (2025-12-01..2025-12-31) [keep: ] quote: "and 1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"
  - p98 Year-on-year percent change in projected December TEUs at major U.S. ports = **19.4** % (2025-12-01..2025-12-31) [DISCARD: Redundant restatement of -19.4%; level p97 kept.] quote: "1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"
- `https://theloadstar.com/analysis-los-angeles-pier-500-the-only-answer-for-a-port-already-at-full-capacity/` -> **snapshot** (snapshot 20251028145406); points raw/verified 0/0
- `https://www.apmterminals.com/en/los-angeles/focus/2025-annual-impact-report` -> **snapshot** (snapshot 20260617194522); points raw/verified 11/11
  - p99 Container throughput handled by APM Terminals Los Angeles at Pier 400 in 2025 = **3,250,000** TEU (2025-01-01..2025-12-31) [DISCARD: Already discarded; terminal-level annual throughput, not port total.] quote: "3.25 million TEUs handled in 2025"
  - p100 Increase in cargo throughput at Pier 400 since 2023 (percent) = **62** % (2023-01-01..2025-12-31) [DISCARD: Already discarded; terminal-level change, irrelevant.] quote: "Since 2023, Pier 400 has increased cargo throughput by 62 percent while significantly reducing overall emissions."
  - p101 Average truck turn time at Pier 400 in 2025 = **39** minutes (2025-01-01..2025-12-31) [DISCARD: Already discarded; truck turn time, irrelevant.] quote: "Truck turn times have been cut to 39 minutes - the fastest in the San Pedro Bay Complex"
  - p102 Reduction in greenhouse gas emissions at Pier 400 since 2017 (percent) = **59** % (2017-01-01..2025-12-31) [DISCARD: Already discarded; emissions, irrelevant.] quote: "59% reduction in greenhouse gas emissions since 2017"
  - p103 Lost Time Injury rate at Pier 400 in 2025 = **0.56** Lost Time Injury rate (2025-01-01..2025-12-31) [DISCARD: Already discarded; injury rate, irrelevant.] quote: "0.56 Lost Time Injury rate"
  - p104 Electric container-handling units in service at Pier 400 = **71** electric units (2025-01-01..2025-12-31) [DISCARD: Already discarded; equipment count, irrelevant.] quote: "with 71 electric units in service and nearly 95 more funded or on order"
  - p105 Additional electric units funded or on order at Pier 400 = **95** electric units (2025-01-01..2025-12-31) [DISCARD: Already discarded; equipment count, irrelevant.] quote: "with 71 electric units in service and nearly 95 more funded or on order"
  - p106 Charitable giving by Pier 400 to local nonprofits in 2025 (USD) = **400,000** USD (2025-01-01..2025-12-31) [DISCARD: Already discarded; charitable giving, irrelevant.] quote: "$400,000+ in charitable giving"
  - p107 Community partners supported by Pier 400 in 2025 = **40** community partners (2025-01-01..2025-12-31) [DISCARD: Already discarded; community partners, irrelevant.] quote: "supported over 40 community partners"
  - p108 Employee volunteer hours logged by Pier 400 in 2025 = **750** volunteer hours (2025-01-01..2025-12-31) [DISCARD: Already discarded; volunteer hours, irrelevant.] quote: "750+ community volunteer hours"
  - p109 Number of facilities in APM Terminals global network = **60** facilities (2025-01-01..2025-12-31) [DISCARD: Already discarded; network size, irrelevant.] quote: "across the entire APM Terminals global network of more than 60 facilities worldwide"
- `https://portoflosangeles.org/references/2025-news-releases/news_081325_july_cargo` -> **snapshot** (snapshot 20251003230943); points raw/verified 13/13
  - p110 Total TEUs handled by Port of Los Angeles, July 2025 (busiest month on record) = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "The Port handled 1,019,837 Twenty-Foot Equivalent Units (TEUs), 8.5% more than last July."
  - p111 Year-over-year growth in total TEUs, Port of Los Angeles, July 2025 vs July 2024 = **8.5** % (2025-07-01..2025-07-31) [DISCARD: Redundant restatement of July 2025 +8.5% YoY; level p110 kept.] quote: "The Port handled 1,019,837 Twenty-Foot Equivalent Units (TEUs), 8.5% more than last July."
  - p112 Loaded imports in TEUs, Port of Los Angeles, July 2025 = **543,728** TEU (2025-07-01..2025-07-31) [keep: ] quote: "July 2025 loaded imports came in at 543,728 TEUs, 8% more than last year and the most imports ever in a month at the Port."
  - p113 Year-over-year growth in loaded imports, Port of Los Angeles, July 2025 = **8** % (2025-07-01..2025-07-31) [DISCARD: Redundant restatement of July 2025 import +8%; level p112 kept.] quote: "July 2025 loaded imports came in at 543,728 TEUs, 8% more than last year and the most imports ever in a month at the Port."
  - p114 Loaded exports in TEUs, Port of Los Angeles, July 2025 = **121,507** TEU (2025-07-01..2025-07-31) [keep: ] quote: "Loaded exports landed at 121,507 TEUs, a 6% improvement from 2024."
  - p115 Year-over-year improvement in loaded exports, Port of Los Angeles, July 2025 = **6** % (2025-07-01..2025-07-31) [DISCARD: Redundant restatement of July 2025 export +6%; level p114 kept.] quote: "Loaded exports landed at 121,507 TEUs, a 6% improvement from 2024."
  - p116 Empty container units processed, Port of Los Angeles, July 2025 = **354,602** TEU (2025-07-01..2025-07-31) [keep: ] quote: "The Port processed 354,602 empty container units, 10% more than last year."
  - p117 Year-over-year growth in empty container units, Port of Los Angeles, July 2025 = **10** % (2025-07-01..2025-07-31) [DISCARD: Redundant restatement of July 2025 empty +10%; level p116 kept.] quote: "The Port processed 354,602 empty container units, 10% more than last year."
  - p118 Cumulative TEUs handled by Port of Los Angeles, first seven months of 2025 = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "Seven months into 2025, the Port of Los Angeles has handled 5,975,649 TEUs, 5% more than the same period in 2024."
  - p119 Year-over-year growth in cumulative TEUs, Port of Los Angeles, first seven month = **5** % (2025-01-01..2025-07-31) [DISCARD: Redundant restatement of Jan-Jul 2025 +5%; level p118 kept.] quote: "Seven months into 2025, the Port of Los Angeles has handled 5,975,649 TEUs, 5% more than the same period in 2024."
  - p120 Total TEUs handled by Port of Los Angeles, May 2021 (second busiest month) = **1,012,048** TEU (2021-05-01..2021-05-31) [DISCARD: Already discarded; May 2021 record, not September.] quote: "st time a Western Hemisphere port handled more than 1 million TEUs in a single month was in May 2021, when the Port of Los Angeles recorded 1,012,048 TEUs, now the second busiest month in its history."
  - p121 Threshold of monthly TEUs first exceeded by a Western Hemisphere port (May 2021, = **1,000,000** TEU (2021-05-01..2021-05-31) [DISCARD: Already discarded; threshold, not a measurement.] quote: "The first time a Western Hemisphere port handled more than 1 million TEUs in a single month was in May 2021"
  - p122 Age in years of Port of Los Angeles at July 2025 record month = **117** years (2025-07-01..2025-07-31) [DISCARD: Already discarded; port age, irrelevant.] quote: "July was the busiest month on record in the 117-year history of the Port of Los Angeles."
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b1 [own_history] Port of LA monthly release

Hypothesis: August 2026 total TEU (published ~mid-September 2026) would anchor the level immediately before September and let a month-over-month seasonal ratio replace the year-over-year route; it is the single most valuable missing input.

Queries issued by the searcher: Port of Los Angeles August 2026 cargo TEU; portoflosangeles.org cargo news July 2026 TEU

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 15/15
  - p123 Port of Los Angeles July 2026 total container volume (loaded + empty, TEUs) = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p124 Port of Los Angeles July 2026 loaded imports (TEUs) = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p125 Port of Los Angeles July 2026 loaded exports (TEUs) = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p126 Port of Los Angeles July 2026 total loaded (TEUs) = **611,327** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p127 Port of Los Angeles July 2026 total empty (TEUs) = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p128 Port of Los Angeles July 2025 total container volume (prior-year comparison, TEU = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p129 Port of Los Angeles July 2026 total TEU year-over-year percent change = **-5.82** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -5.82%; level p123 kept.] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p130 Port of Los Angeles calendar year 2026 cumulative total TEUs (through July) = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p131 Port of Los Angeles calendar year 2025 cumulative total TEUs (comparison) = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p132 Port of Los Angeles calendar year 2026 cumulative total TEU year-over-year perce = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Redundant restatement of +1.8%; level p130 kept.] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p133 Port of Los Angeles annual total container volume 2025 (TEUs) = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
  - p134 Port of Los Angeles annual total container volume 2024 (TEUs) = **10,297,352** TEU (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p135 Port of Los Angeles annual total container volume 2023 (TEUs) = **8,629,681** TEU (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023 \| 8,629,681 \| 2013 \| 7,868,582 \| 2003 \| 7,178,940 \| 1993 \| 2,318,920 \| 1983 \| 733,979 \|"
  - p136 Port of Los Angeles annual total container volume 2022 (TEUs) = **9,911,159** TEU (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022 \| 9,911,159 \| 2012 \| 8,077,714 \| 2002 \| 6,105,863 \| 1992 \| 2,289,271 \| 1982 \| 606,189 \|"
  - p137 Port of Los Angeles annual total container volume 2021 (TEUs) = **10,677,610** TEU (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021 \| 10,677,610 \| 2011 \| 7,940,511 \| 2001 \| 5,183,520 \| 1991 \| 2,039,165 \| 1981 \| 476,249 \|"
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p138 Port of Los Angeles total TEUs processed in July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p139 Port of Los Angeles loaded imports in July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p140 Port of Los Angeles loaded exports in July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p141 Port of Los Angeles empty containers in July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p142 Port of Los Angeles cumulative total TEUs, first seven months of 2026 = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p143 Port of Los Angeles cumulative total TEU year-over-year change, first seven mont = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Redundant restatement of +1.8%; level p142 kept.] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p144 Port of Los Angeles July 2026 total TEU year-over-year change = **6** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -6%; level p138 kept.] quote: "July cargo was 6% lower than last year's all-time record for the month, when businesses surged cargo ahead of anticipated trade policy changes."
  - p145 Port of Los Angeles July 2026 total TEU vs five-year July average = **7.5** % (2026-07-01..2026-07-31) [keep: ] quote: "Despite the year-over-year decline, July volume was 7.5% above the Port's five-year average for the month."
  - p146 Port of Los Angeles July 2026 loaded imports year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -8%; level p139 kept.] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p147 Port of Los Angeles July 2026 loaded imports vs five-year July average = **6** % (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p148 Port of Los Angeles July 2026 loaded exports year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -8%; level p140 kept.] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p149 Port of Los Angeles July 2026 empty containers year-over-year change = **2** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -2%; level p141 kept.] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p150 Port of Los Angeles June 2026 total container units (stated as topping 1 million = **1,000,000** TEU (2026-06-01..2026-06-30) [keep: ] quote: ""After topping 1 million container units in June, we nearly reached that mark again in July," said Port of Los Angeles Executive Director Gene Seroka."

### b2 [related_series] San Pedro Bay complex

Hypothesis: Long Beach September 2026 (or combined complex) would let LA TEU be estimated as complex total times LA's stable share, providing an independent cross-check on the own-history route.

Queries issued by the searcher: Port of Long Beach monthly cargo September 2025 TEU; Port of Los Angeles September 2025 cargo volume TEU news release; Port of Los Angeles August 2026 TEU cargo volume; Port of Long Beach August 2026 cargo volumes TEU

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/august-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/initial-port-volumes-for-september-2025` -> **snapshot** (snapshot 20251028170238); points raw/verified 9/9
  - p151 Port of Long Beach laden inbound TEUs, September 2025 = **388,084** TEU (2025-09-01..2025-09-30) [keep: ] quote: "Over at the Port of Long Beach, 388,084 laden inbound TEUs were discharged in September, a 6.9% year-over-year decline but a 9.3% gain over September 2019."
  - p152 Port of Long Beach outbound loaded TEUs, September 2025 = **85,081** TEU (2025-09-01..2025-09-30) [keep: ] quote: "Outbound loads amounted to 85,081 TEUs, down 3.6% from a year earlier as well as down 30.9% from September 2019."
  - p153 Port of Long Beach total YTD container traffic through September 2025 = **7,390,245** TEU (2025-01-01..2025-09-30) [keep: ] quote: "Total YTD container traffic through September (7,390,245 TEUs) represented a 6.8% gain over the same period six years ago."
  - p154 Port of Los Angeles inbound loaded TEUs, September 2025 = **460,044** TEU (2025-09-01..2025-09-30) [keep: ] quote: "the 460,044 inbound loaded TEUs handled at the Southern California gateway down 7.6% from a year earlier"
  - p155 Port of Los Angeles outbound loaded TEUs, September 2025 = **114,693** TEU (2025-09-01..2025-09-30) [keep: ] quote: "outbound loads of 114,693 TEUs a shade below the 114,702 TEUs shipped from the port last September"
  - p156 Port of Los Angeles total loaded and empty TEUs, first three quarters 2025 = **7,817,057** TEU (2025-01-01..2025-09-30) [keep: ] quote: "Total container movements through America's busiest container port through the first three quarters of this year amounted to 7,817,057 loaded and empty TEUs"
  - p157 Combined San Pedro Bay ports (LA + Long Beach) total TEUs, first three quarters  = **15,207,302** TEU (2025-01-01..2025-09-30) [keep: ] quote: "Together, the two San Pedro Bay ports handled 15,207,302 total TEUs during the first three quarters of this year, an increase of 4.9% from the same period last year"
  - p158 NRF Global Port Tracker preliminary forecast of laden import TEUs at 13 U.S. mai = **2,120,000** TEU (2025-09-01..2025-09-30) [keep: ] quote: "projecting that 2.12 million TEUs laden with goods from abroad would arrive at the thirteen U.S. mainland ports it surveys"
  - p159 Descartes Systems Group estimate of TEUs at all U.S. ports, September 2025 = **2,307,933** TEU (2025-09-01..2025-09-30) [keep: ] quote: "the Descartes Systems Group has estimated that 2,307,933 TEUs arrived at all U.S. ports in September, an 8.4% falloff from a year earlier"
- `https://www.freightwaves.com/news/port-of-los-angeles-posts-record-2-9m-teus-eyes-strong-finish-to-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Global Port Tracker / NRF

Hypothesis: A September 2026 national import forecast and LA's share of US containerized imports would give an independent loaded-import estimate; direction of forecast vs 2025 constrains the YoY change factor.

Queries issued by the searcher: Global Port Tracker September 2026 forecast imports; NRF Hackett Associates September 2026 import forecast TEU; Seroka Port of Los Angeles September 2026 forecast 900,000 TEU briefing; Port of Los Angeles share of US containerized imports 2026 percent

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.yahoo.com/economy/articles/nrf-walks-back-peak-season-175759004.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-11` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gcaptain.com/u-s-container-imports-defy-expectations-as-peak-season-stretches-into-september/` -> **snapshot** (snapshot 20260910101111); points raw/verified 15/7
  - p160 Global Port Tracker: US covered ports container imports, July 2026 (actual) = **2,300,000** TEU (2026-07-01..2026-07-31) [keep: ] quote: "slightly above July's 2.3 million TEU"
  - p161 Global Port Tracker: US covered ports container imports, July 2026 (final figure = **2,300,000** TEU (2026-07-01..2026-07-31) [keep: ] quote: "U.S. ports covered by Global Port Tracker handled 2.3 million TEU in July, the latest month for which final figures are available."
  - p162 Global Port Tracker: US covered ports imports, July 2026 year-over-year change = **3.9** % (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of -3.9%; level p161 kept.] quote: "although still down 3.9% from a year earlier"
  - p163 Global Port Tracker estimate: US covered ports container imports, August 2026 = **2,290,000** TEU (2026-08-01..2026-08-31) [keep: ] quote: "August, which has yet to be finalized, is now estimated at 2.29 million TEU, down 1.3% year over year."
  - p164 Global Port Tracker: US covered ports container imports, full year 2025 = **25,400,000** TEU (2025-01-01..2025-12-31) [keep: ] quote: "up 1% from 25.4 million TEU last year"
  - p165 Global Port Tracker: US covered ports container imports, first half 2026 = **12,700,000** TEU (2026-01-01..2026-06-30) [keep: ] quote: "The first half of 2026 totaled 12.7 million TEU, up 1.1% from the same period in 2025."
  - p166 Prior-month Global Port Tracker forecast: US covered ports container imports, Au = **2,220,000** TEU (2026-08-01..2026-08-31) [DISCARD: Prior-month forecast for August 2026; superseded by the updated p163 estimate, adds no independent information.] quote: "Last month, Global Port Tracker had forecast August at 2.22 million TEU."
- dropped by code checks: 8 (period_end 2026-09-30 after as_of: 3; period_end 2026-10-31 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-12-31 after as_of: 2; period_end 2027-01-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['port los angeles teu', 'container volume september', 'la port throughput']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p28', 'p76', 'p81', 'p110'] All report Port of LA July total TEUs; p1/p28/p76 are the same July 2026 figure (960,464) from the same Port release, and p2/p81/p110 are the same July 2025 record (1,019,837). These are duplicate vin
- corroborating: ['p3', 'p4', 'p5', 'p6', 'p72', 'p73', 'p74', 'p75', 'p32', 'p35', 'p37'] July 2026 component breakdown (imports 499,552; exports 111,776; loaded 611,327; empty 349,137) is internally consistent and repeated across snapshots; components sum to the July total. Same underlyin
- corroborating: ['p16', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p58', 'p60', 'p62', 'p63', 'p86', 'p88', 'p90', 'p91'] September 2025 total 883,053 TEU with components (imports 460,044; exports 114,693; empties ~308,000-308,317) agree across Port table and news reports. p21/p63/p91 differ slightly (308,317 vs 308,040)
- corroborating: ['p17', 'p19', 'p22', 'p59', 'p61', 'p64', 'p87', 'p89', 'p92'] September 2025 YoY changes (-7.5% total, -7.6% imports, -10% empties) consistent across sources; same Port release.
- corroborating: ['p11', 'p12', 'p39', 'p40', 'p82', 'p83'] Jan-Jul 2026 cumulative 6,083,067 TEU, +1.8% vs 2025's 5,975,649; consistent across snapshots.
- corroborating: ['p26', 'p27', 'p41', 'p42'] China share of LA containerized imports: 53.4% (2025), 61% (2020), ~40% (2026). Contextual for import mix, not a direct volume input.
- corroborating: ['p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98'] NRF/Hackett national forecasts for Oct-Dec 2025 (down 12-19% YoY) — national context only, not LA-specific and for 2025 not 2026.
- corroborating: ['p13', 'p14', 'p15', 'p84', 'p85'] Annual totals 2023-2025 consistent; useful for level context and seasonal share checks.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p28', 'p76', 'p81', 'p110', 'p123', 'p128', 'p138'] All report the same July 2025 and July 2026 total TEU figures (1,019,837 and 960,464) from the Port's own monthly release; multiple URLs but one underlying measurement. July 2026 is 5.82% below July 2
- corroborating: ['p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p32', 'p35', 'p37', 'p72', 'p73', 'p74', 'p75', 'p77', 'p78', 'p79', 'p80', 'p124', 'p125', 'p126', 'p127', 'p139', 'p140', 'p141'] Component breakdown for July 2026 and July 2025: loaded imports 499,552 (down 8%), loaded exports 111,776 (down 8%), empties 349,137 (down 2%). Components sum to totals; consistent single source.
- corroborating: ['p16', 'p18', 'p20', 'p21', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p58', 'p60', 'p62', 'p63', 'p86', 'p88', 'p90', 'p91', 'p154', 'p155'] September 2025 actuals: total 883,053; loaded imports 460,044; loaded exports 114,693; empties ~308,000-308,317. Two vintages (eesea/portoflosangeles and Xinhua) agree; the Port table gives empty expo
- corroborating: ['p11', 'p12', 'p39', 'p40', 'p82', 'p83', 'p130', 'p131', 'p132', 'p142', 'p143'] Cumulative Jan-Jul 2026 = 6,083,067, +1.8% vs Jan-Jul 2025 = 5,975,649. Consistent across snapshots; implies 2026 running slightly ahead of 2025 despite July being down.
- corroborating: ['p13', 'p14', 'p15', 'p52', 'p84', 'p85', 'p133', 'p134', 'p135', 'p136', 'p137'] Annual totals: 2025 10,239,318; 2024 10,297,352; 2023 8,629,681; 2022 9,911,159; 2021 10,677,610. Context for level; 2025 essentially flat vs 2024.
- corroborating: ['p23', 'p24', 'p25', 'p156', 'p157'] Q3 2025 ~2.9M TEU (best quarter), Jan-Sep 2025 7,817,057 (+3%), combined LA+LB Jan-Sep 2025 15,207,302. Implies LA share of complex ~51.4% in 2025 YTD.
- corroborating: ['p26', 'p27', 'p41', 'p42'] China share of LA containerized imports fell from 61% (2020) to 53.4% (2025) to ~40% (2026). Structural headwind on import volumes; supports a modest YoY decline in September 2026.
- corroborating: ['p30', 'p33', 'p36', 'p38', 'p129', 'p144', 'p146', 'p148', 'p149'] July 2026 YoY: total -6%, imports -8%, exports -8%, empties -2%. Consistent with the level data; the -5.82% precise figure is the table-derived value.
- corroborating: ['p31', 'p34', 'p145', 'p147'] July 2026 was 7.5% above the five-year July average (imports 6% above), indicating 2026 is a normal-to-strong year, not a collapse; the YoY decline reflects the exceptional 2025 front-loading.
- corroborating: ['p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166'] Global Port Tracker: US covered ports July 2026 2.3M TEU (-3.9% YoY), August 2026 est 2.29M (-1.3% YoY), H1 2026 12.7M (+1.1%). National imports mildly down YoY in mid-2026, consistent with LA's modes
- corroborating: ['p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98'] NRF/Hackett Oct-Dec 2025 forecasts showed steep YoY declines (-12% to -19%) after the 2025 front-loading; context for why late-2025/2026 comparisons are soft.
- corroborating: ['p151', 'p152', 'p153'] Long Beach September 2025: laden inbound 388,084 (-6.9%), outbound 85,081; YTD 7,390,245. Used only as context for complex share; no September 2026 LB data available.
- corroborating: ['p158', 'p159'] September 2025 national import estimates: NRF 2.12M laden TEU at 13 ports; Descartes 2,307,933 TEU all US ports (-8.4%). Different scopes; both indicate September 2025 was a high base.
- corroborating: ['p150'] June 2026 'topped 1 million container units' — qualitative, consistent with a strong mid-2026 level; not a precise figure.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 total TEU change factor vs September 2025 | 0.97 | 0.85..1.1 | 0.85..1.1 | ratio | m1 (m1) | July 2026 was -5.82% YoY (p129) and imports -8% (p33), but cumulative Jan-Jul 2026 was +1.8% (p40) and July was 7.5% above the five-year average (p31). National imports were -3.9% in July and -1.3% in August 2026 (p162, p163). September 2025 was a high base (883,053, p16). A modest decline of ~3% is | September 2026 follows the mid-2026 trend of modest YoY decline rather than a sharp collapse or rebound. | Evidence of a sharp September 2026 rebound (e.g., August 2026 well above 2025) or a collapse (e.g., new tariffs cutting volumes >15%). |
| a2 | September-to-July seasonal ratio of total TEU | 0.9 | 0.82..0.98 | 0.6339..1.268 (widened) | ratio | m2 (m2) | In 2025, September (883,053, p16) was 0.866 of July (1,019,837, p2); in 2024 the ratio was similar. September is typically slightly below July at LA. Central 0.90 with range reflecting year-to-year variation. | September 2026 seasonal pattern resembles recent years (no unusual front-loading distortion). | Evidence that 2026 September is unusually strong or weak relative to July (e.g., a port strike or tariff deadline). |
| a3 | September 2026 loaded-import share of total TEU | 0.52 | 0.48..0.56 | 0.3666..0.7332 (widened) | ratio | m4 (m4) | September 2025: imports 460,044 / total 883,053 = 0.521 (p18, p16). July 2026: 499,552/960,464 = 0.520 (p3, p1). Stable ~52%. | Import share remains near its recent ~52% level. | Evidence of a large shift in import/empty mix (e.g., empty repositioning surge). |
| a4 | September 2026 loaded-export share of total TEU | 0.13 | 0.11..0.15 | 0.09083..0.1817 (widened) | ratio | m4 (m4) | September 2025: exports 114,693/883,053 = 0.130 (p20, p16). July 2026: 111,776/960,464 = 0.116 (p4, p1). Central 0.13. | Export share remains near recent levels. | Evidence of a large export surge or collapse. |
| a5 | September 2026 empty share of total TEU | 0.35 | 0.31..0.39 | 0.2459..0.4917 (widened) | ratio | m4 (m4) | September 2025: empties 308,317/883,053 = 0.349 (p21, p16). July 2026: 349,137/960,464 = 0.364 (p6, p1). Central 0.35. | Empty share remains near recent levels. | Evidence of a large empty-repositioning shift. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 853,616 | ['p16'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 862,935 | ['p1'] / ['a2'] | [] |  | 0.25 | equal |  |
| m3 | series_naive | 883,053 |  | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 896,400 | ['p16'] / ['a3', 'a4', 'a5'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **873,841** TEU, 80% interval [591,260, 1,291,476] TEU, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.75

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total container volume (loaded and empty imports plus exports combined) handled by the Port of Los Angeles during September 2026 is 873,841 TEU (80% model-based interval 591,260 to 1,291,476 TEU). This combines 4 methods at equal weight: a year-over-year route (853,616 TEU, weight 25%) anchored on September 2025 (883,053 TEUs) with a change factor of 0.97; a seasonal route (862,935 TEU, weight 25%) scaling July 2026 (960,464 TEU) by a September/July ratio of 0.9; a naive baseline (883,053 TEU, weight 25%); and a component-share check (896,400 TEU, weight 25%) using shares of 0.52, 0.13, and 0.35. Only the September 2025 and July 2026 totals are observed; the change factor, seasonal ratio, and shares are analyst assumptions, not measured. The interval reflects input uncertainty, not demonstrated accuracy. The main risk is a tariff-driven discontinuity making mid-2026 trends unrepresentative. Early September 2026 port data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 total TEU change factor vs September 2025: 0.97 ratio, range 0.85 to 1.1; used by m1. Overturned by: Evidence of a sharp September 2026 rebound (e.g., August 2026 well above 2025) or a collapse (e.g., new tariffs cutting volumes >[n]).
- a2 September-to-July seasonal ratio of total TEU: 0.9 ratio, range 0.6339 to 1.268 (range widened by code); used by m2. Overturned by: Evidence that 2026 September is unusually strong or weak relative to July (e.g., a port strike or tariff deadline).
- a3 September 2026 loaded-import share of total TEU: 0.52 ratio, range 0.3666 to 0.7332 (range widened by code); used by m4. Overturned by: Evidence of a large shift in import/empty mix (e.g., empty repositioning surge).
- a4 September 2026 loaded-export share of total TEU: 0.13 ratio, range 0.09083 to 0.1817 (range widened by code); used by m4. Overturned by: Evidence of a large export surge or collapse.
- a5 September 2026 empty share of total TEU: 0.35 ratio, range 0.2459 to 0.4917 (range widened by code); used by m4. Overturned by: Evidence of a large empty-repositioning shift.

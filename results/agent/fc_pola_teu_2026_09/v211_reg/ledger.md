# Evidence ledger: fc_pola_teu_2026_09

- Question: Assume today is 2026-09-10. You know nothing published after this date. Estimate the total container volume handled by the Port of Los Angeles in September 2026, in TEUs (twenty-foot equivalent units; loaded and empty imports and exports combined), as it will be first reported in the Port of Los Angeles's monthly cargo news release.
- as_of: 2026-09-10
- Pinned target: Total container volume handled by the Port of Los Angeles (loaded + empty, imports + exports combined) during September 2026, as first reported in the Port's monthly cargo news release | unit TEU | period 2026-09-01..2026-09-30 | publisher Port of Los Angeles (Port of Los Angeles monthly cargo news release / TEU statistics)

- Official value (scoring only, never shown to the agent): 1,042,652

## Directions and pages

### d1 [own_history] Port of LA monthly cargo statistics

Hypothesis: September 2026 total TEU will follow the Port's own seasonal pattern and recent trend; the same month in prior years (Sep 2023, Sep 2024, Sep 2025) plus the most recent months published before cutoff (Jul/Aug 2026) anchor a level-and-seasonality projection.

Queries issued by the searcher: Port of Los Angeles September 2025 cargo volume TEU monthly; Port of Los Angeles monthly container statistics 2026 TEU; portoflosangeles.org container statistics historical TEU statistics 2024 September 954,706; Port of Los Angeles August 2025 cargo volume TEU news release

- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2025` -> **snapshot** (snapshot 20260122223542); points raw/verified 15/14
  - p1 Port of LA total TEUs, September 2025 = **883,053** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p2 Port of LA total TEUs, August 2025 = **958,355** TEU (2025-08-01..2025-08-31) [keep: ] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p3 Port of LA total TEUs, July 2025 = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| July \| 543,727.80 \| 503.00 \| 544,230.80 \| 121,507.00 \| 354,099.50 \| 475,606.50 \| 1,019,837.30 \| 8.54% \|"
  - p4 Port of LA total TEUs, June 2025 = **892,340** TEU (2025-06-01..2025-06-30) [DISCARD: June 2025; not needed for a September seasonal ratio.] quote: "\| June \| 470,449.75 \| 148.00 \| 470,597.75 \| 126,144.25 \| 295,597.75 \| 421,742.00 \| 892,339.75 \| 7.80% \|"
  - p5 Port of LA total TEUs, October 2025 = **848,424** TEU (2025-10-01..2025-10-31) [keep: ] quote: "\| October \| 429,279.75 \| 21.00 \| 429,303.75 \| 123,764.25 \| 295,359.25 \| 419,127.50 \| 848,424.25 \| -6.25% \|"
  - p6 Port of LA total TEUs, November 2025 = **782,249** TEU (2025-11-01..2025-11-30) [DISCARD: November 2025; not needed for a September seasonal ratio.] quote: "\| November \| 406,421.00 \| 69.50 \| 406,490.50 \| 113,706.25 \| 262,052.25 \| 375,758.50 \| 782,249.00 \| -11.54% \|"
  - p7 Port of LA total TEUs, December 2025 = **791,588** TEU (2025-12-01..2025-12-31) [DISCARD: December 2025; not needed for a September seasonal ratio.] quote: "\| December \| 424,498.75 \| 12.00 \| 424,510.75 \| 108,074.75 \| 259,002.25 \| 367,077.00 \| 791,587.75 \| -14.11% \|"
  - p8 Port of LA total TEUs, calendar year 2025 = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p9 Port of LA total TEUs, fiscal year 2024/25 = **10,521,673** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year total; different period, not usable in a September series.] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
  - p10 Port of LA loaded imports TEUs, September 2025 = **460,044** TEU (2025-09-01..2025-09-30) [DISCARD: Loaded-imports component of p1's release; p1 already carries the total and p10 is not needed separately for a total-TEU ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p11 Port of LA loaded exports TEUs, September 2025 = **114,693** TEU (2025-09-01..2025-09-30) [DISCARD: Loaded-exports component of p1's release; redundant for total-TEU estimation.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p12 Port of LA empty exports TEUs, September 2025 = **308,040** TEU (2025-09-01..2025-09-30) [DISCARD: Empty-exports component of p1's release; redundant for total-TEU estimation.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p13 Port of LA total TEUs prior-year change, September 2025 = **-7.51** % (2025-09-01..2025-09-30) [DISCARD: YoY change embedded in p1's release; redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p14 Port of LA total TEUs prior-year change, August 2025 = **-0.23** % (2025-08-01..2025-08-31) [DISCARD: YoY change embedded in p2's release; redundant.] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 11/11
  - p15 Port of LA total container volume (loaded + empty) July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p16 Port of LA total container volume (loaded + empty) July 2025 = **1,019,837** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3 (July 2025 total) from a later snapshot; same measurement.] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p17 Port of LA loaded imports July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [DISCARD: Component of p15's July 2026 release; p15 total suffices.] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p18 Port of LA loaded exports July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [DISCARD: Component of p15's July 2026 release; redundant.] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p19 Port of LA total loaded July 2026 = **611,327** TEU (2026-07-01..2026-07-31) [DISCARD: Component of p15's July 2026 release; redundant.] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p20 Port of LA total empty July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [DISCARD: Component of p15's July 2026 release; redundant.] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p21 Port of LA calendar year 2026 cumulative total TEU (through July) = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p22 Port of LA calendar year 2025 cumulative total TEU (through July) = **5,975,649** TEU (2025-01-01..2025-07-31) [DISCARD: Prior-year cumulative embedded in p21's comparison; redundant.] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p23 Port of LA annual total TEU 2023 = **8,629,681** TEU (2023-01-01..2023-12-31) [DISCARD: Annual 2023 total; context only, no September role.] quote: "\| 2023 \| 8,629,681 \| 2013 \| 7,868,582 \| 2003 \| 7,178,940 \| 1993 \| 2,318,920 \| 1983 \| 733,979 \|"
  - p24 Port of LA annual total TEU 2024 = **10,297,352** TEU (2024-01-01..2024-12-31) [DISCARD: Annual 2024 total; context only.] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p25 Port of LA annual total TEU 2025 = **10,239,318** TEU (2025-01-01..2025-12-31) [DISCARD: Duplicate of p8 (annual 2025).] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
- `https://www.supplychain247.com/article/pola_turns_in_its_second_best_july_volumes/global_trade` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2024-news-releases/news_101824_sept_cargo` -> **snapshot** (snapshot 20251205184257); points raw/verified 11/11
  - p26 Port of Los Angeles total TEU handled, September 2024 (record month) = **954,706** TEU (2024-09-01..2024-09-30) [keep: ] quote: "The Port of Los Angeles handled a record 954,706 Twenty-Foot Equivalent Units (TEUs) in September, a 27% increase over the previous year."
  - p27 Port of Los Angeles total TEU, September 2024 vs September 2023, year-over-year  = **27** % (2024-09-01..2024-09-30) [DISCARD: YoY change embedded in p26's release; redundant.] quote: "in September, a 27% increase over the previous year"
  - p28 Port of Los Angeles total TEU handled, busiest quarter ever (Jul-Sep 2024) = **2,854,904** TEU (2024-07-01..2024-09-30) [DISCARD: Quarterly total, not a September monthly value; not usable in a September series.] quote: "It marked the close of the busiest quarter ever at the Port, which processed 2,854,904 TEUs in the last three months."
  - p29 Port of Los Angeles cumulative total TEU, first nine months of 2024 = **7,586,395** TEU (2024-01-01..2024-09-30) [DISCARD: Nine-month cumulative, not a September monthly value; not usable in a September series.] quote: "Overall, the Port has moved 7,586,395 TEUs the first nine months of 2024, an 18% increase over the 2023 mark."
  - p30 Port of Los Angeles cumulative TEU, first nine months of 2024 vs same period 202 = **18** % (2024-01-01..2024-09-30) [DISCARD: Nine-month YoY change; not a September monthly value.] quote: "Nine months into 2024, the Port of Los Angeles is 18% ahead of its 2023 pace."
  - p31 Port of Los Angeles loaded imports, September 2024 = **497,803** TEU (2024-09-01..2024-09-30) [DISCARD: Component of p26's September 2024 release; redundant for total-TEU route.] quote: "September 2024 loaded imports landed at 497,803 TEUs, a 26% increase compared to the previous year."
  - p32 Port of Los Angeles loaded imports, September 2024 vs September 2023, increase = **26** % (2024-09-01..2024-09-30) [DISCARD: Loaded-imports YoY change; not a total-TEU September input.] quote: "September 2024 loaded imports landed at 497,803 TEUs, a 26% increase compared to the previous year."
  - p33 Port of Los Angeles loaded exports, September 2024 = **114,702** TEU (2024-09-01..2024-09-30) [DISCARD: Component of p26's September 2024 release; redundant.] quote: "Loaded exports came in at 114,702 TEUs, a 5% decrease compared to 2023."
  - p34 Port of Los Angeles loaded exports, September 2024 vs September 2023, decrease = **5** % (2024-09-01..2024-09-30) [DISCARD: Loaded-exports YoY change; not a total-TEU September input.] quote: "Loaded exports came in at 114,702 TEUs, a 5% decrease compared to 2023."
  - p35 Port of Los Angeles empty containers processed, September 2024 = **342,201** TEU (2024-09-01..2024-09-30) [DISCARD: Component of p26's September 2024 release; redundant.] quote: "The Port processed 342,201 empty containers, a 45% jump compared to 2023."
  - p36 Port of Los Angeles empty containers, September 2024 vs September 2023, increase = **45** % (2024-09-01..2024-09-30) [DISCARD: Empty-container YoY change; not a total-TEU September input.] quote: "The Port processed 342,201 empty containers, a 45% jump compared to 2023."
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d2 [related_series] Port of Long Beach and San Pedro Bay complex

Hypothesis: LA and Long Beach volumes are correlated and share regional drivers; Long Beach's September 2026 (or recent) figures and the LA share of the San Pedro Bay total can constrain LA's level.

Queries issued by the searcher: Port of Long Beach September 2025 TEU cargo container volume monthly; San Pedro Bay ports combined container volume 2026 Los Angeles Long Beach TEU; Port of Los Angeles September 2025 total TEU 758,000 cargo news release; pmsaship.com monthly TEU tallies total container traffic Los Angeles Long Beach port total TEU table

- `https://www.marineinsight.com/two-major-u-s-container-gateways-handled-nearly-1-88-million-teus-in-august/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.industrialinfo.com/iirenergy/industry-news/article/tariffs-hit-major-california-port-cargo-activity--347783` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/outlook-for-container-volumes-in-san-pedro-bay` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.opis.com/resources/energy-market-news-from-opis/southern-california-cargo-volumes-neared-2026-high-in-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National container import/export data (Census/CBP, Descartes, NRF imports)

Hypothesis: LA handles a roughly stable share of US containerized imports; national container import volumes for September 2026 (or forecasts) times LA's share gives an independent route.

Queries issued by the searcher: NRF Global Port Tracker September 2026 imports TEU; Descartes US container imports September 2025 TEU; Port of Los Angeles share of US container imports 2025 percent; Port of Los Angeles September 2025 cargo TEU monthly release

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.descartes.com/resources/knowledge-center/global-shipping-report-September-US-imports-contract-amid-tariff-uncertainty?language=en` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/historicuswctrafficaug25` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.theatlantic.com/economy/archive/2025/05/trump-tariff-shipping-ports/682673/` -> **snapshot** (snapshot 20251217071740); points raw/verified 10/10
  - p37 Port of Los Angeles share of all US containerized imports and exports (combined) = **17** % (not stated (page dated 2025-05-01)) [DISCARD: LA share of US combined imports+exports; not a September-specific or import-only share, and dated 2025.] quote: "The Port of Los Angeles, the busiest containerized-cargo port in the Western Hemisphere, processes about 17 percent of everything the United States imports or exports in shipping containers."
  - p38 Port of Long Beach share of all US containerized imports and exports (combined) = **14** % (not stated (page dated 2025-05-01)) [DISCARD: LB share of US combined trade; not needed for an LA-only route.] quote: "The adjoining Port of Long Beach accounts for another 14 percent."
  - p39 Seroka estimate of near-term Port of LA cargo arrivals decline vs same time last = **35** % (not stated (page dated 2025-05-01)) [DISCARD: Seroka's May 2025 -35% near-term warning was not realized (2025 volumes held near record); using it would mislead.] quote: "Seroka estimated that cargo arrivals would soon be down 35 percent over the same time last year."
  - p40 Duration to work out supply-chain bumps after tariff resolution (low end) = **9** as written "nine", value check pending months (not stated (page dated 2025-05-01)) [DISCARD: Qualitative supply-chain recovery duration; no numerical role in a September 2026 level.] quote: "Even if there is resolution, it will take nine to 12 months to work out these bumps."
  - p41 Duration to work out supply-chain bumps after tariff resolution (high end) = **12** months (not stated (page dated 2025-05-01)) [DISCARD: Qualitative supply-chain recovery duration; no numerical role.] quote: "Even if there is resolution, it will take nine to 12 months to work out these bumps."
  - p42 Tariff suspension duration announced by Trump = **90** days (not stated (page dated 2025-05-01)) [DISCARD: 90-day tariff suspension from 2025; expired long before September 2026, no direct role.] quote: "The sell-off ebbed only when he suspended most, but not all, of the new measures for 90 days."
  - p43 Advance booking lead time for shipping reservations before vessel launch (Forto) = **2** as written "two weeks", value check pending weeks (not stated (page dated 2025-05-01)) [DISCARD: Booking lead time; too indirect to constrain a monthly total.] quote: "According to Forto, a cargo-management and -tracking company, reservations for shipping products must normally be placed two weeks before a cargo vessel launches."
  - p44 Minimum additional transit time from China to California = **2** as written "two or more additional weeks", value check pending weeks (not stated (page dated 2025-05-01)) [DISCARD: Transit time; too indirect to constrain a monthly total.] quote: "The trip from China from California typically takes two or more additional weeks."
  - p45 Share of greater Los Angeles region jobs arising directly or indirectly from its = **0.1111** as written "one in nine", value check pending jobs per job (not stated (page dated 2025-05-01)) [DISCARD: Regional jobs share; irrelevant to container volume.] quote: "describing how one in nine jobs in the greater Los Angeles region arises directly or indirectly from its ports."
  - p46 Date of Trump's 'Liberation Day' tariff announcement = **2** day of month (April) (2025-04-02..2025-04-02) [DISCARD: Date of 2025 tariff announcement; historical context only, no numerical role.] quote: "A number of shipments now under way were instigated before Trump's so-called Liberation Day tariff announcement, on April 2."

### d4 [forecasts_markets] Industry forecasters (NRF Global Port Tracker, port guidance)

Hypothesis: Published forecasts for September 2026 US port volumes and any Port of LA guidance/outlook give a direct projected level; forecast direction indicates whether Sep 2026 is above or below the prior-year month.

Queries issued by the searcher: Global Port Tracker September 2026 forecast; Port of Los Angeles 2026 volume outlook TEU forecast; Seroka "900,000" TEU September 2026 Port of Los Angeles August volumes briefing; "Port of Los Angeles" August 2026 cargo volumes 955,907 TEU press release

- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.yahoo.com/economy/articles/nrf-walks-back-peak-season-175759004.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.porttechnology.org/news/global-trade/september-set-to-cap-extended-us-peak-season-rush/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Tariff/trade policy and calendar effects

Hypothesis: Tariff deadlines, front-loading, and holiday-season timing shift monthly volumes; identifying September 2026 policy/calendar effects adjusts the seasonal baseline up or down.

Queries issued by the searcher: tariffs container imports 2026 front-loading port volumes; Port of Los Angeles cargo volumes July 2026; Port of Los Angeles September 2025 cargo volume TEU news release; "Port of Los Angeles" August 2026 cargo volume outlook Seroka peak season winding down

- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p47 Total TEUs processed by Port of Los Angeles in July 2026 = **960,464** TEUs (2026-07-01..2026-07-31) [DISCARD: Duplicate of p15 (July 2026 total).] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p48 Total container units (TEUs) handled by Port of Los Angeles in June 2026 (stated = **1,000,000** container units (TEUs) (2026-06-01..2026-06-30) [DISCARD: June 2026 'topped 1 million' is a rounded threshold, not a precise monthly value; July p15 is the better anchor.] quote: ""After topping 1 million container units in June, we nearly reached that mark again in July,""
  - p49 Year-over-year change in Port of Los Angeles July 2026 cargo volume = **6** % (2026-07-01..2026-07-31) [DISCARD: YoY change embedded in p15's release; redundant.] quote: "July cargo was 6% lower than last year's all-time record for the month"
  - p50 Port of Los Angeles July 2026 volume above five-year July average = **7.5** % (2026-07-01..2026-07-31) [DISCARD: Five-year-average comparison embedded in p15's release; redundant.] quote: "July volume was 7.5% above the Port's five-year average for the month."
  - p51 Loaded imports at Port of Los Angeles in July 2026 = **499,552** TEUs (2026-07-01..2026-07-31) [DISCARD: Duplicate of p17 (July 2026 loaded imports).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p52 Year-over-year change in Port of Los Angeles loaded imports, July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p49/p166 (July 2026 loaded imports YoY).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month"
  - p53 Port of Los Angeles July 2026 loaded imports above five-year July average = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p167 (July 2026 loaded imports vs five-year average).] quote: "down 8% compared with last year's record month but 6% above the five-year July average"
  - p54 Loaded exports at Port of Los Angeles in July 2026 = **111,776** TEUs (2026-07-01..2026-07-31) [DISCARD: Duplicate of p18 (July 2026 loaded exports).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p55 Year-over-year change in Port of Los Angeles loaded exports, July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p168 (July 2026 loaded exports YoY).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p56 Empty containers at Port of Los Angeles in July 2026 = **349,137** TEUs (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20 (July 2026 empty).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p57 Year-over-year change in Port of Los Angeles empty containers, July 2026 = **2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p169 (July 2026 empty YoY).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p58 Cumulative TEUs handled by Port of Los Angeles, first seven months of 2026 = **6,083,067** TEUs (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21 (cumulative Jan–Jul 2026).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p59 Year-over-year change in Port of Los Angeles cumulative TEUs, first seven months = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21's YoY change; redundant.] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
- `https://money.usnews.com/investing/news/articles/2026-08-07/early-surge-in-us-container-imports-coming-to-an-end-shippers-say` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cdn.nrf.com/media-center/press-releases/import-cargo-expected-to-set-new-record-ahead-of-potential-august-tariffs` -> **snapshot** (snapshot 20260713101134); points raw/verified 15/12
  - p60 Global Port Tracker forecast: total U.S. major container port import volume, Aug = **2,220,000** TEU (2026-08-01..2026-08-31) [DISCARD: National August 2026 import forecast; not a September value and not LA-specific.] quote: "Imports are expected to drop to 2.22 million TEU in August, down 4.5% year over year."
  - p61 Global Port Tracker forecast: year-over-year change in U.S. major port import vo = **4.5** % (2026-08-01..2026-08-31) [DISCARD: National August 2026 YoY change; not a September value.] quote: "Imports are expected to drop to 2.22 million TEU in August, down 4.5% year over year."
  - p62 Global Port Tracker forecast: total U.S. major container port import volume, Jul = **2,470,000** TEU (2026-07-01..2026-07-31) [DISCARD: National July 2026 import forecast; not a September value.] quote: "July is forecast at 2.47 million TEU, which would be up 3.3% from last year"
  - p63 Global Port Tracker forecast: year-over-year change in U.S. major port import vo = **3.3** % (2026-07-01..2026-07-31) [DISCARD: National July 2026 YoY change; not a September value.] quote: "July is forecast at 2.47 million TEU, which would be up 3.3% from last year"
  - p64 Previous monthly record for U.S. major port import volume (May 2022) = **2,400,000** TEU (2022-05-01..2022-05-31) [DISCARD: May 2022 record; historical context only, no September 2026 role.] quote: "would top the previous monthly record of 2.4 million TEU set in May 2022"
  - p65 Global Port Tracker projection: total U.S. major container port import volume, J = **2,330,000** TEU (2026-06-01..2026-06-30) [DISCARD: National June 2026 import projection; not a September value.] quote: "Global Port Tracker projected the month at 2.33 million TEU, up 18.7% year over year."
  - p66 Global Port Tracker projection: year-over-year change in U.S. major port import  = **18.7** % (2026-06-01..2026-06-30) [DISCARD: National June 2026 YoY change; not a September value.] quote: "Global Port Tracker projected the month at 2.33 million TEU, up 18.7% year over year."
  - p67 Global Port Tracker: total U.S. major container port import volume, May 2026 (fi = **2,240,000** TEU (2026-05-01..2026-05-31) [DISCARD: National May 2026 final; not a September value.] quote: "U.S. ports covered by Global Port Tracker handled 2.24 million Twenty-Foot Equivalent Units"
  - p68 Year-over-year change in U.S. major port import volume, May 2026 = **14.9** % (2026-05-01..2026-05-31) [DISCARD: National May 2026 YoY change; not a September value.] quote: "That was up 14.9% from a year earlier"
  - p69 Month-over-month change in U.S. major port import volume, May 2026 vs April 2026 = **10.1** % (2026-05-01..2026-05-31) [DISCARD: National May 2026 MoM change; not a September value.] quote: "and up 10.1% from April"
  - p70 Global Port Tracker projection: cumulative U.S. major port import volume, first  = **12,770,000** TEU (2026-01-01..2026-06-30) [DISCARD: National H1 2026 cumulative; not a September value.] quote: "That would bring the first half of 2026 to 12.77 million TEU, up 2% from the same period in 2025."
  - p71 Year-over-year change in cumulative U.S. major port import volume, first half 20 = **2** % (2026-01-01..2026-06-30) [DISCARD: National H1 2026 YoY change; not a September value.] quote: "That would bring the first half of 2026 to 12.77 million TEU, up 2% from the same period in 2025."
- `https://airfreight.news/articles/full/september-cargo-volume-boosts-port-of-los-angeles-to-record-quarter` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period_end 2026-09-30 after as_of: 2; period_end 2026-10-31 after as_of: 1)

### d6 [physical_flow] Vessel calls and terminal throughput

Hypothesis: September TEU ≈ number of container vessel calls × average TEU per call × days; vessel schedule/call data for Sep 2026 constrains realised throughput.

Queries issued by the searcher: Port of Los Angeles container vessel calls per month average TEU per call; Port of Los Angeles monthly cargo news release 2026 TEU; Port of Los Angeles vessel calls 2026 container ships per month wharfinger; "Port of Los Angeles" August 2026 cargo TEU news release

- `https://www.bts.gov/sites/bts.dot.gov/files/2025-12/BTS_TSAR-2025_Annual-Report_123125.pdf` -> **snapshot** (snapshot 20260903022741); points raw/verified 15/15
  - p72 Total container vessel calls at Ports of Los Angeles and Long Beach combined, 20 = **1,828** ship calls (2024-01-01..2024-12-31) [DISCARD: LA+LB combined annual call count; combined-port scope, not LA September.] quote: "the total number of ship calls decreased, from 2,811 in 2005 to 1,828 in 2024"
  - p73 Total container vessel calls at Ports of Los Angeles and Long Beach combined, 20 = **2,811** ship calls (2005-01-01..2005-12-31) [DISCARD: 2005 call count; obsolete.] quote: "the total number of ship calls decreased, from 2,811 in 2005 to 1,828 in 2024"
  - p74 Average container volume per ship call at Ports of Los Angeles and Long Beach co = **10,912** TEUs per call (2024-01-01..2024-12-31) [DISCARD: LA+LB combined TEU per call; combined-port annual average, not LA September.] quote: "more than doubling from 5,050 TEUs per call in 2005 to 10,912 TEUs per call in 2024"
  - p75 Average container volume per ship call at Ports of Los Angeles and Long Beach co = **5,050** TEUs per call (2005-01-01..2005-12-31) [DISCARD: 2005 TEU per call; obsolete.] quote: "more than doubling from 5,050 TEUs per call in 2005 to 10,912 TEUs per call in 2024"
  - p76 Number of vessels greater than 15,000 TEU calling at Ports of Los Angeles and Lo = **69** vessels (2024-01-01..2024-12-31) [DISCARD: Large-vessel count; too indirect for a monthly total.] quote: "the number of greater than 15,000 TEU vessels increased from 45 to 69"
  - p77 Number of vessels greater than 15,000 TEU calling at Ports of Los Angeles and Lo = **45** vessels (2023-01-01..2023-12-31) [DISCARD: Large-vessel count 2023; too indirect.] quote: "the number of greater than 15,000 TEU vessels increased from 45 to 69"
  - p78 Port of Los Angeles imports handled, 2023 (over 4.4 million TEUs) = **4,400,000** TEUs (imports) (2023-01-01..2023-12-31) [DISCARD: BTS 'over 4.4 million TEUs in imports' for 2023 is a rounded, ambiguous-scope figure (imports only, possibly loaded) tha] quote: "The Port of Los Angeles, for instance, handled over 4.4 million TEUs in imports"
  - p79 Port of Los Angeles standard deviation of container vessel berthing time, Jan–Oc = **33** hours (2025-01-01..2025-10-31) [DISCARD: Berthing-time standard deviation — operational quality metric, no route to monthly TEU volume.] quote: "the port with the highest standard deviation of berthing time is the Port of Los Angeles at 33 hours"
  - p80 Port of Virginia standard deviation of container vessel berthing time, Jan–Oct 2 = **8** hours (2025-01-01..2025-10-31) [DISCARD: Virginia berthing-time comparison — irrelevant to LA volume.] quote: "The Port of Virginia had the lowest berthing time standard deviation at 8 hours."
  - p81 Port of Los Angeles LSCI connectivity score change, 2024 to 2025 = **6** points (2025-01-01..2025-12-31) [DISCARD: LSCI connectivity point change — no quantitative bridge to September TEU.] quote: "In contrast, the Port of Los Angeles decreased by 6 points."
  - p82 Los Angeles, CA gateway combined export and import freight value, 2024 (top-rank = **332,400,000,000** USD (2024-01-01..2024-12-31) [DISCARD: Freight value (USD) for LA gateway — value, not TEU; no usable conversion.] quote: "Los Angeles, CA, emerged as the leading gateway, processing a substantial $332.4 billion in combined export and import freight value."
  - p83 Vessel freight value for U.S.–Asia trade, 2024 = **1,130,000,000,000** USD (2024-01-01..2024-12-31) [DISCARD: US–Asia vessel freight value — value, not TEU; no usable conversion.] quote: "the value of goods moved by vessels amounting to $1.13 trillion in 2024"
  - p84 Vessel tonnage between United States and Asia, 2024 = **304,700,000** short tons (2024-01-01..2024-12-31) [DISCARD: US–Asia vessel tonnage — tonnage, not TEU; no usable conversion.] quote: "Vessel transport dominates the United States-Asia trade, with 304.7 million tons of goods moved by vessels in 2024."
  - p85 Average annual truck speed within 5 miles of Port of Los Angeles/Long Beach (PLA = **20.45** mph (2024-01-01..2024-12-31) [DISCARD: Truck speed near ports — congestion context, no route to monthly TEU.] quote: "2024 20.73 20.90 19.97 20.20 20.45"
  - p86 Average annual truck speed within 5 miles of Port of Los Angeles/Long Beach (PLA = **20.96** mph (2023-01-01..2023-12-31) [DISCARD: Truck speed near ports — congestion context, no route to monthly TEU.] quote: "culminating in a higher average of 20.96 mph in 2023"
- `https://portoflosangeles.org/business/supply-chain/ships` -> **snapshot** (snapshot 20260304155853); points raw/verified 0/0
- `https://container-mag.com/2026/02/18/san-pedro-bay-terminal-data-blank-sailings-dwell-spike-february-2026/` -> **snapshot** (snapshot 20260306171654); points raw/verified 15/15
  - p87 Port of Los Angeles container vessels at berth on 18 February 2026 = **9** as written "nine", value check pending container vessels (2026-02-18..2026-02-18) [DISCARD: Single-day berth count (Feb 2026) — snapshot, not a September volume input.] quote: "The Port of Los Angeles had nine container vessels at berth on 18 February."
  - p88 Port of Los Angeles average berth time, 30-day rolling basis, as of 18 February  = **4** days (2026-02-18..2026-02-18) [DISCARD: Berth time — operational metric, no route to monthly TEU.] quote: "nine container vessels at berth with an average berth time of 4.0 days on a 30-day rolling basis"
  - p89 Port of Los Angeles container vessels currently inbound as of 18 February 2026 = **7** as written "seven", value check pending container vessels (2026-02-18..2026-02-18) [DISCARD: Single-day inbound count — snapshot, not a September volume input.] quote: "Only seven container vessels are currently inbound to the port"
  - p90 Port of Los Angeles vessels planned further out, estimated containers carried = **254,908** containers (not stated (page dated 2026-02-18)) [DISCARD: Vessels planned further out with estimated containers — ambiguous horizon/scope, stale (Feb 2026), not a September 2026 ] quote: "A total of 94 vessels are planned further out, carrying an estimated 254,908 containers."
  - p91 Port of Los Angeles vessels planned further out (count) = **94** vessels (not stated (page dated 2026-02-18)) [DISCARD: Vessel count for ambiguous future horizon — stale, no September 2026 mapping.] quote: "A total of 94 vessels are planned further out, carrying an estimated 254,908 containers."
  - p92 Port of Los Angeles Week 7 (15-21 Feb) forecast import volume = **109,862** teu (2026-02-15..2026-02-21) [DISCARD: Feb 2026 weekly import forecast — stale, import-only, not September.] quote: "Week 7 (15-21 February): 109,862 teu across 20 scheduled vessels, down 14.5% year on year and 5.2% week on week."
  - p93 Port of Los Angeles Week 7 scheduled vessels = **20** vessels (2026-02-15..2026-02-21) [DISCARD: Feb 2026 weekly vessel count — stale, not September.] quote: "Week 7 (15-21 February): 109,862 teu across 20 scheduled vessels"
  - p94 Port of Los Angeles Week 8 (22-28 Feb) forecast import volume = **116,557** teu (2026-02-22..2026-02-28) [DISCARD: Feb 2026 weekly import forecast — stale, not September.] quote: "Week 8 (22-28 February): 116,557 teu across 21 vessels"
  - p95 Port of Los Angeles Week 8 scheduled vessels = **21** vessels (2026-02-22..2026-02-28) [DISCARD: Feb 2026 weekly vessel count — stale, not September.] quote: "Week 8 (22-28 February): 116,557 teu across 21 vessels"
  - p96 Port of Los Angeles Week 9 (1-7 Mar) forecast import volume = **98,533** teu (2026-03-01..2026-03-07) [DISCARD: Mar 2026 weekly import forecast — stale, not September.] quote: "Week 9 (1-7 March): 98,533 teu across 17 vessels, down 15.5% week on week."
  - p97 Port of Los Angeles Week 9 scheduled vessels = **17** vessels (2026-03-01..2026-03-07) [DISCARD: Mar 2026 weekly vessel count — stale, not September.] quote: "Week 9 (1-7 March): 98,533 teu across 17 vessels"
  - p98 Port of Los Angeles January 2026 total throughput = **812,000** teu (2026-01-01..2026-01-31) [DISCARD: January 2026 total; too distant from September and not a September value.] quote: "The Port of Los Angeles processed 812,000 teu in January 2026, a 12% drop year on year"
  - p99 Port of Los Angeles January 2026 loaded imports = **421,594** teu (2026-01-01..2026-01-31) [DISCARD: January 2026 loaded imports; too distant and a component.] quote: "Loaded imports fell 13% to 421,594 teu."
  - p100 Port of Long Beach projected weekly vessel calls, Week 11 (8 March) = **16** vessel calls (2026-03-08..2026-03-14) [DISCARD: Long Beach weekly vessel calls — different port, stale, no LA conversion.] quote: "Projected weekly vessel calls show a dip to 16 in Week 11 (8 March) - down 20% year on year - before recovering to 18 in Week 12 (15 March)."
  - p101 Port of Long Beach projected weekly vessel calls, Week 12 (15 March) = **18** vessel calls (2026-03-15..2026-03-21) [DISCARD: Long Beach weekly vessel calls — different port, stale, no LA conversion.] quote: "before recovering to 18 in Week 12 (15 March)"
- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p102 Total TEUs processed by Port of Los Angeles in July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p15/p47 (July 2026 total).] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p103 Total container units (TEUs) topped by Port of Los Angeles in June 2026 = **1,000,000** TEU (2026-06-01..2026-06-30) [DISCARD: Duplicate of p48 (June 2026 rounded 1M).] quote: "After topping 1 million container units in June, we nearly reached that mark again in July"
  - p104 Loaded imports at Port of Los Angeles in July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p17/p51/p116/p127 (July 2026 loaded imports).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p105 Loaded exports at Port of Los Angeles in July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p18/p54/p117/p128 (July 2026 loaded exports).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p106 Empty containers at Port of Los Angeles in July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20/p56/p118/p130 (July 2026 empties).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p107 Cumulative TEUs handled by Port of Los Angeles in first seven months of 2026 = **6,083,067** TEU (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21/p58/p119/p137 (Jan–Jul 2026 cumulative).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p108 Year-over-year change in Port of Los Angeles July 2026 cargo volume = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p49/p120 (July 2026 -6%).] quote: "July cargo was 6% lower than last year's all-time record for the month"
  - p109 Port of Los Angeles July 2026 volume above its five-year July average = **7.5** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p50/p121 (July 2026 +7.5% vs 5-yr avg).] quote: "July volume was 7.5% above the Port's five-year average for the month."
  - p110 Year-over-year change in Port of Los Angeles loaded imports in July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p52/p122 (July 2026 imports -8%).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month"
  - p111 Port of Los Angeles July 2026 loaded imports above five-year July average = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p53/p123 (July 2026 imports +6% vs 5-yr avg).] quote: "but 6% above the five-year July average"
  - p112 Year-over-year change in Port of Los Angeles loaded exports in July 2026 = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p55/p124 (July 2026 exports -8%).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p113 Year-over-year change in Port of Los Angeles empty containers in July 2026 = **2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p57/p125 (July 2026 empties -2%).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p114 Year-over-year change in Port of Los Angeles cumulative TEUs, first seven months = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p59/p126 (Jan–Jul 2026 +1.8%).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."

### d7 [base_rates] Loaded vs empty and import vs export split

Hypothesis: Total TEU = loaded imports + loaded exports + empty imports + empty exports; if only loaded or only import figures are found, the historical component shares convert them to total TEU.

Queries issued by the searcher: Port of Los Angeles July 2026 cargo loaded imports exports empties TEU; Port of Los Angeles monthly cargo news release 2026 loaded imports loaded exports empty TEU

- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 12/12
  - p115 Port of Los Angeles total TEUs processed in July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p15 (July 2026 total).] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July"
  - p116 Port of Los Angeles loaded imports in July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p17/p51/p127 (July 2026 loaded imports).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month"
  - p117 Port of Los Angeles loaded exports in July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p18/p54/p128 (July 2026 loaded exports).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p118 Port of Los Angeles empty containers in July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20/p56/p130 (July 2026 empties).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p119 Port of Los Angeles cumulative total TEUs handled in first seven months of 2026 = **6,083,067** TEU (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21/p58/p137 (Jan–Jul 2026 cumulative).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p120 Port of Los Angeles July 2026 total TEU change vs prior year record July (percen = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p49/p108 (July 2026 -6%).] quote: "July cargo was 6% lower than last year's all-time record for the month"
  - p121 Port of Los Angeles July 2026 total TEU vs five-year July average (percent above = **7.5** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p50/p109 (July 2026 +7.5%).] quote: "July volume was 7.5% above the Port's five-year average for the month."
  - p122 Port of Los Angeles July 2026 loaded imports change vs prior year (percent) = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p52/p110 (July 2026 imports -8%).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month"
  - p123 Port of Los Angeles July 2026 loaded imports vs five-year July average (percent  = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p53/p111 (July 2026 imports +6%).] quote: "but 6% above the five-year July average"
  - p124 Port of Los Angeles July 2026 loaded exports change vs prior year (percent) = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p55/p112 (July 2026 exports -8%).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p125 Port of Los Angeles July 2026 empty containers change vs prior year (percent) = **2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p57/p113 (July 2026 empties -2%).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p126 Port of Los Angeles cumulative total TEU change in first seven months of 2026 vs = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p59/p114 (Jan–Jul 2026 +1.8%).] quote: "the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 14/14
  - p127 Port of LA loaded imports, July 2026 (TEUs) = **499,552** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p17/p51 (July 2026 loaded imports).] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p128 Port of LA loaded exports, July 2026 (TEUs) = **111,776** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p18/p54 (July 2026 loaded exports).] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p129 Port of LA total loaded, July 2026 (TEUs) = **611,327** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p19 (July 2026 total loaded).] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p130 Port of LA total empty, July 2026 (TEUs) = **349,137** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20/p56 (July 2026 empties).] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p131 Port of LA total container volume, July 2026 (TEUs) = **960,464** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p15 (July 2026 total).] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p132 Port of LA loaded imports, July 2025 (TEUs) = **543,728** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p16 (July 2025 loaded imports).] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p133 Port of LA loaded exports, July 2025 (TEUs) = **121,507** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p16 (July 2025 loaded exports).] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p134 Port of LA total loaded, July 2025 (TEUs) = **665,235** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p16 (July 2025 total loaded).] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p135 Port of LA total empty, July 2025 (TEUs) = **354,602** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p16 (July 2025 empties).] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p136 Port of LA total container volume, July 2025 (TEUs) = **1,019,837** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p16 (July 2025 total).] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p137 Port of LA calendar year 2026 cumulative total container volume (TEUs) = **6,083,067** TEU (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21/p58 (Jan–Jul 2026 cumulative).] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p138 Port of LA calendar year 2025 cumulative total container volume (TEUs) = **5,975,649** TEU (2025-01-01..2025-07-31) [DISCARD: Duplicate of p22 (Jan–Jul 2025 cumulative).] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p139 Port of LA annual total container volume, 2025 (TEUs) = **10,239,318** TEU (2025-01-01..2025-12-31) [DISCARD: Duplicate of p25 (2025 annual).] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
  - p140 Port of LA annual total container volume, 2024 (TEUs) = **10,297,352** TEU (2024-01-01..2024-12-31) [DISCARD: Duplicate of p24 (2024 annual).] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
- `https://www.pmsaship.com/maritime-insights-blog/july-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_021726_jan_cargo` -> **snapshot** (snapshot 20260226175907); points raw/verified 8/8
  - p141 Port of Los Angeles total TEUs processed, January 2026 = **812,000** TEU (2026-01-01..2026-01-31) [DISCARD: Duplicate of p98 (Jan 2026 total).] quote: "The Port of Los Angeles processed 812,000 Twenty-Foot Equivalent Units (TEUs) in January, a decrease of 12% compared to last year's cargo levels."
  - p142 Port of Los Angeles total TEU change, January 2026 vs January 2025 = **12** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p98 (Jan 2026 -12%).] quote: "processed 812,000 Twenty-Foot Equivalent Units (TEUs) in January, a decrease of 12% compared to last year's cargo levels."
  - p143 Port of Los Angeles loaded imports, January 2026 = **421,594** TEU (2026-01-01..2026-01-31) [DISCARD: Duplicate of p99 (Jan 2026 loaded imports).] quote: "January 2026 loaded imports came in at 421,594 TEUs, 13% less than last year."
  - p144 Port of Los Angeles loaded imports change, January 2026 vs January 2025 = **13** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p99 (Jan 2026 imports -13%).] quote: "January 2026 loaded imports came in at 421,594 TEUs, 13% less than last year."
  - p145 Port of Los Angeles loaded exports, January 2026 = **104,297** TEU (2026-01-01..2026-01-31) [DISCARD: Duplicate of p99 context (Jan 2026 loaded exports); same release, redundant.] quote: "Loaded exports landed at 104,297 TEUs, an 8% drop compared to 2025."
  - p146 Port of Los Angeles loaded exports change, January 2026 vs January 2025 = **8** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p145 (Jan 2026 exports -8%).] quote: "Loaded exports landed at 104,297 TEUs, an 8% drop compared to 2025."
  - p147 Port of Los Angeles empty container units, January 2026 = **286,110** TEU (2026-01-01..2026-01-31) [DISCARD: Duplicate of p98 context (Jan 2026 empties); same release, redundant.] quote: "The Port handled 286,110 empty container units, 12% less than last year."
  - p148 Port of Los Angeles empty container units change, January 2026 vs January 2025 = **12** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p147 (Jan 2026 empties -12%).] quote: "The Port handled 286,110 empty container units, 12% less than last year."

### b1 [own_history] Port of LA monthly release

Hypothesis: August 2026 total TEU (published ~mid-September 2026) is the single most informative missing input: it would anchor the level entering September and let a month-over-month seasonal ratio (Sep/Aug) replace the weaker year-over-year route. Without it, September must be projected from July.

Queries issued by the searcher: Port of Los Angeles cargo news August 2026 TEU; portoflosangeles.org cargo news release July 2026 TEU; Port of Los Angeles September 2025 cargo release TEU monthly statistics 2025; portoflosangeles.org container statistics 2026 monthly TEUs August September table; "Port of Los Angeles" 2024 container statistics September 2024 954,706 TEU August 2024

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2025` -> **snapshot** (snapshot 20260122223542); points raw/verified 12/11
  - p149 Port of Los Angeles total TEUs, August 2025 = **958,355** TEU (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 (August 2025 total).] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p150 Port of Los Angeles loaded imports, August 2025 = **504,514** TEU (2025-08-01..2025-08-31) [DISCARD: Duplicate of the August 2025 loaded-imports figure already carried by p2's release; p2 and component points p151-p153 su] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p151 Port of Los Angeles loaded exports, August 2025 = **127,379** TEU (2025-08-01..2025-08-31) [DISCARD: Duplicate August 2025 loaded exports; redundant with p2 release.] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p152 Port of Los Angeles empty exports, August 2025 = **326,006** TEU (2025-08-01..2025-08-31) [DISCARD: Duplicate August 2025 empty exports; redundant with p2 release.] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p153 Port of Los Angeles empty imports, August 2025 = **457** TEU (2025-08-01..2025-08-31) [DISCARD: Duplicate August 2025 empty imports (457 TEU, negligible); redundant.] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p154 Port of Los Angeles total TEUs, prior year change, August 2025 = **-0.23** % (2025-08-01..2025-08-31) [DISCARD: Duplicate August 2025 YoY change; redundant with p2/p14.] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p155 Port of Los Angeles total TEUs, September 2025 = **883,053** TEU (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1 (same September 2025 total); redundant copy adds no information.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p156 Port of Los Angeles total TEUs, July 2025 = **1,019,837** TEU (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3 (July 2025 total).] quote: "\| July \| 543,727.80 \| 503.00 \| 544,230.80 \| 121,507.00 \| 354,099.50 \| 475,606.50 \| 1,019,837.30 \| 8.54% \|"
  - p157 Port of Los Angeles total TEUs, October 2025 = **848,424** TEU (2025-10-01..2025-10-31) [DISCARD: Duplicate of p5 (October 2025 total).] quote: "\| October \| 429,279.75 \| 21.00 \| 429,303.75 \| 123,764.25 \| 295,359.25 \| 419,127.50 \| 848,424.25 \| -6.25% \|"
  - p158 Port of Los Angeles total TEUs, calendar year 2025 = **10,239,318** TEU (2025-01-01..2025-12-31) [DISCARD: Duplicate of p8 (calendar 2025 total).] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p159 Port of Los Angeles total TEUs, fiscal year 2024/25 = **10,521,673** TEU (2024-07-01..2025-06-30) [DISCARD: Duplicate of p9 (fiscal year 2024/25 total).] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p160 Port of Los Angeles total TEU handled, July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p15 (July 2026 total).] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p161 Port of Los Angeles loaded imports, July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p17 (July 2026 loaded imports).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p162 Port of Los Angeles loaded exports, July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p18 (July 2026 loaded exports).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p163 Port of Los Angeles empty containers, July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20 (July 2026 empty).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p164 Port of Los Angeles total TEU, July 2026 year-over-year change = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p49 (July 2026 YoY change).] quote: "July cargo was 6% lower than last year's all-time record for the month"
  - p165 Port of Los Angeles July 2026 volume above five-year July average = **7.5** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p50 (July 2026 vs five-year average).] quote: "Despite the year-over-year decline, July volume was 7.5% above the Port's five-year average for the month."
  - p166 Port of Los Angeles loaded imports, July 2026 year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p52 (July 2026 loaded imports YoY).] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month"
  - p167 Port of Los Angeles loaded imports, July 2026 above five-year July average = **6** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p53 (July 2026 loaded imports vs five-year average).] quote: "but 6% above the five-year July average"
  - p168 Port of Los Angeles loaded exports, July 2026 year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p55 (July 2026 loaded exports YoY).] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p169 Port of Los Angeles empty containers, July 2026 year-over-year change = **2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p57 (July 2026 empty YoY).] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p170 Port of Los Angeles cumulative total TEU, first seven months of 2026 = **6,083,067** TEU (2026-01-01..2026-07-31) [DISCARD: Duplicate of p21 (cumulative Jan–Jul 2026).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p171 Port of Los Angeles cumulative total TEU, first seven months of 2026 year-over-y = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p59 (cumulative YoY change).] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p172 Port of Los Angeles total container units, June 2026 (stated as topping this lev = **1,000,000** TEU (2026-06-01..2026-06-30) [DISCARD: Duplicate of p48 (June 2026 topped 1 million).] quote: "After topping 1 million container units in June, we nearly reached that mark again in July"
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b2 [related_series] San Pedro Bay sibling port

Hypothesis: Port of Long Beach August/September 2026 volumes and the LA share of the LA+LB total would provide an independent level check and a cross-port consistency test; if LA and LB diverge sharply, the LA-only projection from July is suspect.

Queries issued by the searcher: Port of Long Beach cargo statistics July 2026 TEU; Port of Long Beach monthly TEU August 2026; Two Major U.S. Container Gateways Handled Nearly 1.88 Million TEUs In August Los Angeles Long Beach; Port of Los Angeles August 2026 cargo TEU monthly release

- `https://www.pmsaship.com/maritime-insights-blog/july-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/the-final-august-teu-volumes` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.worldports.org/two-major-u-s-container-gateways-handled-nearly-1-88-million-teus-in-august/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/august-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] National container tracker

Hypothesis: Global Port Tracker's September 2026 national import forecast (and any LA-specific guidance) would let the national YoY trend be applied to LA's September 2025 base, resolving whether September 2026 is above or below the prior-year month — the largest uncertainty in the year-over-year route.

Queries issued by the searcher: Global Port Tracker September 2026 forecast imports; NRF Hackett Global Port Tracker 2026 monthly import forecast; Seroka Port of Los Angeles September 2026 cargo briefing 900,000 TEUs forecast; "Port of Los Angeles" August 2026 cargo volumes TEU Seroka September outlook

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.yahoo.com/economy/articles/nrf-walks-back-peak-season-175759004.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chrobinson.com/es-us/resources/insights-and-advisories/north-america-freight-insights/sep-2026-freight-market-update/ocean/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['port los angeles teu', 'container volume september', 'la port throughput']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p10', 'p11', 'p12', 'p13'] Same September 2025 release row: total 883,053 = loaded imports 460,044 + loaded exports 114,693 + empty exports 308,040 (plus ~276 empty imports). Internally consistent; single source, not independen
- corroborating: ['p1', 'p26', 'p27'] September 2024 record 954,706 and +27% YoY imply Sep 2023 ≈ 751,700; Sep 2025 at 883,053 is -7.5% vs Sep 2024, consistent with the 2024 record being a peak. Establishes Sep 2023 < Sep 2024 > Sep 2025 
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p47', 'p102', 'p115', 'p131'] Redundant copies of the same July 2026 release (total 960,464; loaded 611,327; empty 349,137). One underlying measurement; keep one representative set.
- corroborating: ['p21', 'p22', 'p58', 'p59', 'p107', 'p114', 'p119', 'p126', 'p137', 'p138'] Same cumulative Jan–Jul 2026 (6,083,067) vs 2025 (5,975,649), +1.8%. Redundant copies of one release.
- corroborating: ['p23', 'p24', 'p25', 'p139', 'p140'] Annual totals 2023–2025 consistent across snapshots; 2025 (10.24M) slightly below 2024 (10.30M), consistent with a 2025 H2 slowdown after front-loading.
- corroborating: ['p60', 'p61', 'p62', 'p63', 'p65', 'p66', 'p67', 'p68', 'p70', 'p71'] Global Port Tracker (NRF/Hackett) national import series: strong H1 2026 (+2%), July +3.3%, then August -4.5% — a decelerating national backdrop. National imports only, not LA total TEU.
- corroborating: ['p98', 'p99', 'p141', 'p142', 'p143', 'p147'] January 2026: 812,000 total, -12% YoY; loaded imports 421,594 (-13%); empties 286,110 (-12%). Consistent internal decomposition; shows a weak start to 2026 followed by a strong June/July.
- corroborating: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77'] BTS LA+LB vessel-call and TEU-per-call series; combined-port scope, not LA alone, and annual — usable only as a scale/context check, not a direct September LA input.
- corroborating: ['p37', 'p38'] LA ~17% and LB ~14% of US containerized trade (combined imports+exports), May 2025 vintage. Share-based, not a September 2026 level.
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] May 2025 tariff-shock context (Seroka -35% warning, 90-day suspension, 2-week booking lead). Directional context for 2025 front-loading; not a 2026 level.
- corroborating: ['p92', 'p93', 'p94', 'p95', 'p96', 'p97'] Feb–Mar 2026 weekly LA import forecasts (~100–117k TEU/week, 17–21 vessels). Weekly import-only, stale for September; scale check only.
- corroborating: ['p87', 'p88', 'p89', 'p90', 'p91'] Feb 2026 berth/inbound snapshot; operational context, not a September volume input.
- corroborating: ['p48', 'p103'] June 2026 'topped 1 million' — rounded statement, consistent with a strong Q2/Q3 2026.
- corroborating: ['p49', 'p108', 'p120'] July 2026 -6% vs record July 2025; consistent with p15/p16.
- corroborating: ['p50', 'p109', 'p121'] July 2026 +7.5% vs five-year July average — indicates 2026 is running above its own recent norm despite being below the 2025 record.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p10', 'p11', 'p12', 'p13'] Same September 2025 LA release: total 883,053 TEU decomposes into loaded imports 460,044 + loaded exports 114,693 + empty exports 308,040 (+ tiny empty imports 276); the -7.51% YoY is the same release
- corroborating: ['p1', 'p155'] Duplicate records of the same September 2025 total (883,053). Redundant copy; keep one for series use.
- corroborating: ['p2', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154'] August 2025 release: total 958,355 with component split and -0.23% YoY. Same underlying release; useful for Sep/Aug seasonal ratio and component shares, not independent confirmation.
- corroborating: ['p15', 'p17', 'p18', 'p19', 'p20', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165'] July 2026 LA release: total 960,464 = loaded 611,327 + empty 349,137; -5.82%/-6% YoY and +7.5% vs five-year July average. Consistent internally; the latest observed level entering the projection.
- corroborating: ['p21', 'p22', 'p58', 'p59', 'p170', 'p171'] Cumulative Jan–Jul 2026 6,083,067 vs 5,975,649 in 2025 (+1.8%). Same release, consistent with July level; supports a modest positive YoY drift for 2026 overall.
- corroborating: ['p3', 'p156', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p158', 'p159'] 2025 monthly and annual LA totals from the same statistical table; establish the seasonal shape (July peak, autumn decline) and annual level ~10.24M TEU.
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p33', 'p35'] September 2024 LA release: record 954,706 TEU, +27% YoY, with loaded imports 497,803, loaded exports 114,702, empties 342,201. Same publisher, earlier vintage; gives the prior-year September level for
- corroborating: ['p23', 'p24', 'p25'] Annual LA totals 2023–2025 (8.63M, 10.30M, 10.24M) consistent with monthly table; context for level, not a September input.
- corroborating: ['p60', 'p61', 'p62', 'p63', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71'] Global Port Tracker (NRF/Hackett) national import forecasts: strong H1 2026 (+2%), July +3.3%, August -4.5%. Same forecast family; indicates national imports turning slightly negative YoY by late summ
- corroborating: ['p37', 'p38'] LA ~17% and LB ~14% of US containerized trade (combined imports+exports), same article. Gives a rough LA share of national volume for a top-down route, but the share is of combined trade, not imports 
- corroborating: ['p72', 'p74', 'p76'] BTS: LA+LB combined 1,828 calls in 2024 at 10,912 TEU/call. Physical-flow cross-check only; combined-port scope and annual average, not LA September.
- corroborating: ['p98', 'p99'] January 2026 LA 812,000 TEU, -12% YoY, loaded imports 421,594. Consistent with a weak start to 2026 followed by a strong spring/summer; context only.
- corroborating: ['p48', 'p172'] June 2026 topped 1 million TEU; July nearly reached it (960,464). Same executive quote; confirms a high summer 2026 plateau.
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] May 2025 Atlantic article on tariff shocks: Seroka's -35% near-term warning, 90-day suspension, 2-week booking/transit lags. Contextual for tariff-driven volatility; the -35% warning was not realized 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 vs September 2025 total TEU change factor | 0.97 | 0.85..1.1 | 0.85..1.1 | ratio | m1 (m1) | LA's 2026 cumulative is +1.8% YoY through July, but July was -6% YoY and Global Port Tracker shows national imports turning negative by August 2026 (-4.5%). September 2025 was already a weak month (-7.5% YoY), so a near-flat to slightly negative YoY factor is plausible; range spans a modest recovery | LA September 2026 tracks its own September 2025 base with a small YoY drift consistent with mid-2026 trends. | Evidence of a sharp September 2026 surge or collapse (e.g., a new tariff deadline front-loading or a port disruption) that moves YoY well outside the range. |
| a2 | September/August seasonal ratio for LA total TEU | 0.92 | 0.85..1 | 0.6519..1.304 (widened) | ratio | unused | In 2025 September/August was 883,053/958,355 ≈ 0.92; in 2024 September was a record and roughly flat to August. A ratio near 0.92 with a range down to 0.85 reflects the typical autumn decline after the summer peak. | September 2026 follows the normal post-summer seasonal decline from the August level. | Evidence that September 2026 is unusually strong (e.g., holiday front-loading) or unusually weak relative to August. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 855,260 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | series_naive | 918,880 |  | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target

Result: central **886,499** TEU, 80% interval [643,481, 1,221,296] TEU, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total container volume handled by the Port of Los Angeles (loaded plus empty, imports plus exports combined) during September 2026 is 886,499 TEU (80% model-based interval 643,481 to 1,221,296 TEU). This is a projection: September 2026 was only partly elapsed at the cutoff, so most of the month is forecast.

Two methods were combined at 50% and 50% weight. The first applies an assumed year-over-year factor of 0.97 (range 0.85 to 1.1) to the observed September 2025 total of 883,053 TEU, giving 855,260 TEU. The second is a naive seasonal average of the two most recent Septembers, 883,053 TEU and 954,706 TEU, giving 918,880 TEU. Only those observed points are data; the drift factor is an assumption.

The main risk is that the assumed factor is wrong, since 2026 trends were mixed. Actual September 2026 daily throughput data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 vs September 2025 total TEU change factor: 0.97 ratio, range 0.85 to 1.1; used by m1. Overturned by: Evidence of a sharp September 2026 surge or collapse (e.g., a new tariff deadline front-loading or a port disruption) that moves YoY well outside the range.

# Evidence ledger: fc_pola_teu_2026_09

- Question: Assume today is 2026-09-10. You know nothing published after this date. Estimate the total container volume handled by the Port of Los Angeles in September 2026, in TEUs (twenty-foot equivalent units; loaded and empty imports and exports combined), as it will be first reported in the Port of Los Angeles's monthly cargo news release.
- as_of: 2026-09-10
- Pinned target: Total container volume handled by the Port of Los Angeles (loaded + empty, imports + exports combined) during September 2026, as first reported in the Port's monthly cargo news release | unit TEU | period 2026-09-01..2026-09-30 | publisher Port of Los Angeles (Port of Los Angeles monthly cargo news release / TEU statistics)

- Official value (scoring only, never shown to the agent): 1,042,652

## Directions and pages

### d1 [own_history] Port of Los Angeles monthly cargo statistics

Hypothesis: September 2026 total TEU will follow the Port's own recent monthly levels adjusted for September seasonality; the most recent months published before cutoff (through ~July/August 2026) anchor the level, and prior Septembers give the seasonal factor.

Queries issued by the searcher: Port of Los Angeles monthly container statistics TEU 2026 cargo news release; Port of Los Angeles September 2025 container volume TEU record; Port of Los Angeles August 2026 TEU cargo volume monthly; Port of Los Angeles July 2026 container volume TEU

- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 11/11
  - p1 Port of Los Angeles total container volume (loaded + empty) July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p2 Port of Los Angeles total container volume (loaded + empty) July 2025 = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p3 Port of Los Angeles loaded imports July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p4 Port of Los Angeles loaded exports July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p5 Port of Los Angeles total loaded July 2026 = **611,327** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p6 Port of Los Angeles total empty July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p7 Port of Los Angeles cumulative calendar year 2026 total container volume through = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p8 Port of Los Angeles cumulative calendar year 2025 total container volume through = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p9 Port of Los Angeles annual total container volume 2023 = **8,629,681** TEU (2023-01-01..2023-12-31) [DISCARD: 2023 annual total; not needed for September routes.] quote: "\| 2023 \| 8,629,681 \| 2013 \| 7,868,582 \| 2003 \| 7,178,940 \| 1993 \| 2,318,920 \| 1983 \| 733,979 \|"
  - p10 Port of Los Angeles annual total container volume 2024 = **10,297,352** TEU (2024-01-01..2024-12-31) [DISCARD: 2024 annual total; not needed for September routes.] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p11 Port of Los Angeles annual total container volume 2025 = **10,239,318** TEU (2025-01-01..2025-12-31) [DISCARD: 2025 annual total; not needed for September routes.] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.porttechnology.org/port-of-los-angeles-records-q3-high-despite-september-dip/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [forecasts_markets] Industry forecasts and port guidance

Hypothesis: Published container-volume forecasts (NRF/Global Port Tracker, port guidance, carrier outlooks) for September 2026 give an independent level estimate for US West Coast / LA imports.

Queries issued by the searcher: Global Port Tracker September 2026 forecast imports; NRF import cargo forecast fall 2026; Port of Los Angeles August 2026 955,907 TEU Seroka September forecast 900,000 TEU; "Port of Los Angeles" September 2025 883,053 TEU loaded imports empties

- `https://finance.yahoo.com/economy/articles/nrf-walks-back-peak-season-175759004.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.worldcargonews.com/news/2026/09/nrf-september-could-be-busiest-import-month-for-us-ports/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] San Pedro Bay combined / Port of Long Beach

Hypothesis: POLA share of San Pedro Bay combined TEU is fairly stable; if combined or POLB September 2026 figures or forecasts exist, POLA = combined * POLA share, or POLA = POLB * (POLA/POLB ratio).

Queries issued by the searcher: Port of Long Beach monthly TEU 2026 cargo volume; POLA POLB TEU ratio monthly San Pedro Bay combined container volume; PMSA Container Statistics 2026 total TEUs Los Angeles Long Beach monthly table; Port of Los Angeles July 2026 TEU cargo volume monthly

- `https://www.presstelegram.com/2026/10/12/long-beach-port-reports-record-cargo-numbers-for-september/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/topic/tag/Port_of_Long_Beach` -> **snapshot** (snapshot 20260107163711); points raw/verified 12/12
  - p12 Port of Long Beach total August TEU (all-time monthly high) = **913,873** TEU (2024-08-01..2024-08-31) [DISCARD: Long Beach August 2024 record; not used in POLA routes.] quote: "Total August volume came in at 913,873 TEU (Twenty-Foot Equivalent Units), marking a 33% annual gain"
  - p13 Port of Long Beach previous all-time monthly high TEU (prior to August 2024) = **907,216** TEU (not stated (page dated 2026-01-01)) [DISCARD: Prior Long Beach record, superseded by p12 and not needed for any POLA route.] quote: "topping the previous all-time monthly high of 907,216 TEU by 6,657 TEU or less than 1%"
  - p14 Port of Long Beach August 2024 annual volume gain (percent) = **33** % (2024-08-01..2024-08-31) [DISCARD: Long Beach growth rate, not used in any POLA estimation route.] quote: "Total August volume came in at 913,873 TEU (Twenty-Foot Equivalent Units), marking a 33% annual gain"
  - p15 Port of Los Angeles total September TEU = **748,440** TEU (2023-09-01..2023-09-30) [DISCARD: September 2023 total; only one prior September level, insufficient for a naive series and superseded by the more recent ] quote: "The Port of Los Angeles reported that total September volume, at 748,440 TEU, was up 5% annually"
  - p16 Port of Los Angeles September 2023 annual volume growth (percent) = **5** % (2023-09-01..2023-09-30) [DISCARD: September 2023 YoY growth; level p15 kept, rate redundant.] quote: "total September volume, at 748,440 TEU, was up 5% annually, marking its second consecutive month of annual growth"
  - p17 Port of Long Beach total September TEU (record September) = **829,429** TEU (2023-09-01..2023-09-30) [DISCARD: Long Beach September 2023 level; not used in POLA routes.] quote: "The Port of Long Beach reported that September marked its highest-volume September on record, with volume at 829,429 TEU, increasing 11.8% annually"
  - p18 Port of Long Beach September 2023 annual volume growth (percent) = **11.8** % (2023-09-01..2023-09-30) [DISCARD: Long Beach September 2023 growth rate; not used in POLA routes.] quote: "with volume at 829,429 TEU, increasing 11.8% annually, and topping the previous September high in 2020 by 78,849 TEU"
  - p19 Port of Long Beach previous September high TEU (2020) = **78,849** TEU (2020-09-01..2020-09-30) [DISCARD: Value is a margin over the prior record (78,849 TEU), not a September TEU level; using it as a level would be a category] quote: "topping the previous September high in 2020 by 78,849 TEU"
  - p20 Port of Los Angeles total August TEU = **828,016** TEU (2023-08-01..2023-08-31) [DISCARD: August 2023 total; not needed for September routes.] quote: "POLA reported that August volume was up 3% annually, coming in at 828,016 TEU (Twenty-Foot Equivalent Units)"
  - p21 Port of Los Angeles August 2023 annual volume growth (percent) = **3** % (2023-08-01..2023-08-31) [DISCARD: POLA August 2023 growth rate; the level p20 is kept, the rate is redundant.] quote: "POLA reported that August volume was up 3% annually, coming in at 828,016 TEU"
  - p22 Port of Long Beach total August TEU = **682,312** TEU (2023-08-01..2023-08-31) [DISCARD: Long Beach August 2023 level; not used in POLA routes.] quote: "The Port of Long Beach reported that total August volume, at 682,312 TEU, was off 15.4% annually."
  - p23 Port of Long Beach August 2023 annual volume change (percent, decline) = **15.4** % (2023-08-01..2023-08-31) [DISCARD: Long Beach August 2023 decline rate; not used.] quote: "The Port of Long Beach reported that total August volume, at 682,312 TEU, was off 15.4% annually."
- `https://the-dwell.com/busiest/us-container-ports` -> **snapshot** (snapshot 20260810040659); points raw/verified 15/14
  - p24 Port of Los Angeles loaded-import TEU, year to date through May 2026 = **2,145,334** TEU (2026-01-01..2026-05-31) [DISCARD: POLA loaded-import YTD through May 2026; not needed for September routes.] quote: "Los Angeles is the busiest tracked US container port by loaded imports, 2,145,334 TEU over the first 5 months of 2026."
  - p25 Port of Long Beach loaded-import TEU, year to date through May 2026 = **1,960,976** TEU (2026-01-01..2026-05-31) [DISCARD: Long Beach loaded-import YTD; not used in POLA routes.] quote: "\| Long Beach \| 1,960,976 \| +1.1% \| 418,851 \| 36.1% \|"
  - p26 Port of Los Angeles loaded-import TEU, latest month (May 2026) = **449,370** TEU (2026-05-01..2026-05-31) [DISCARD: POLA May 2026 loaded imports; not needed for September routes.] quote: "\| Los Angeles \| 2,145,334 \| +3.3% \| 449,370 \| 33.7% \|"
  - p27 Port of Long Beach loaded-import TEU, latest month (May 2026) = **418,851** TEU (2026-05-01..2026-05-31) [DISCARD: Long Beach May 2026 loaded imports; not used in POLA routes.] quote: "\| Long Beach \| 1,960,976 \| +1.1% \| 418,851 \| 36.1% \|"
  - p28 Port of Los Angeles empty-container share, latest month (May 2026) = **33.7** % (2026-05-01..2026-05-31) [DISCARD: POLA May 2026 empty share; not needed for September routes.] quote: "\| Los Angeles \| 2,145,334 \| +3.3% \| 449,370 \| 33.7% \|"
  - p29 Port of Long Beach empty-container share, latest month (May 2026) = **36.1** % (2026-05-01..2026-05-31) [DISCARD: Long Beach empty share; not used in POLA routes.] quote: "\| Long Beach \| 1,960,976 \| +1.1% \| 418,851 \| 36.1% \|"
  - p30 All 9 tracked US container ports loaded-import TEU, year to date through May 202 = **9,944,452** TEU (2026-01-01..2026-05-31) [DISCARD: National 9-port YTD loaded imports; not used in POLA routes.] quote: "\| All 9 tracked ports \| 9,944,452 \| -0.8% \| 2,138,421 \| - \|"
  - p31 All 9 tracked US container ports loaded-import TEU, latest month (May 2026) = **2,138,421** TEU (2026-05-01..2026-05-31) [DISCARD: National 9-port May 2026 loaded imports; not used in POLA routes.] quote: "\| All 9 tracked ports \| 9,944,452 \| -0.8% \| 2,138,421 \| - \|"
  - p32 All 9 tracked US container ports loaded-import TEU, year to date through May 202 = **9,900,000** TEU (2026-01-01..2026-05-31) [DISCARD: Rounded duplicate of p30 (9.9M vs 9,944,452); adds no information.] quote: "Loaded-import volume across 9 tracked US container ports totaled 9.9 million TEU through May, down 0.8% versus the same months of 2025."
  - p33 All 9 tracked US container ports loaded-import TEU, May 2026 (rounded, stated in = **2,140,000** TEU (2026-05-01..2026-05-31) [DISCARD: Rounded duplicate of p31 (2.14M vs 2,138,421); adds no information.] quote: "May loaded imports across the 9 tracked US container ports totaled 2.14 million TEU, with year-to-date volume at 9.94 million TEU, down 0.8% versus 2025."
  - p34 All 9 tracked US container ports loaded-import TEU, year to date through May 202 = **9,940,000** TEU (2026-01-01..2026-05-31) [DISCARD: Rounded duplicate of p30; adds no information.] quote: "May loaded imports across the 9 tracked US container ports totaled 2.14 million TEU, with year-to-date volume at 9.94 million TEU, down 0.8% versus 2025."
  - p35 All 9 tracked US container ports loaded-import TEU, year-to-date change vs same  = **0.8** % (2026-01-01..2026-05-31) [DISCARD: National 9-port YTD change; not used in POLA routes.] quote: "Across all 9 tracked ports, loaded imports are 9,944,452 TEU year to date, down 0.8% versus the same months of 2025."
  - p36 Port of Long Beach loaded-import TEU, year-to-date change vs same months of 2025 = **1.1** % (2026-01-01..2026-05-31) [DISCARD: Long Beach YTD growth rate; not used in POLA routes.] quote: "\| Long Beach \| 1,960,976 \| +1.1% \| 418,851 \| 36.1% \|"
  - p37 Port of New York/New Jersey loaded-import TEU, latest month (May 2026) = **400,995** TEU (2026-05-01..2026-05-31) [DISCARD: New York/New Jersey figure; different port, not used.] quote: "\| New York/New Jersey \| 1,840,605 \| -2.4% \| 400,995 \| 33.8% \|"
- `https://globalmaritimehub.com/north-american-port-volumes-remain-strong-in-june/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d4 [shocks] Tariffs, trade policy, and calendar effects

Hypothesis: 2025-2026 tariff actions and any front-loading/pull-forward effects distort the normal seasonal pattern; September 2026 may be depressed or elevated relative to history depending on tariff timing, so the seasonal factor from prior years must be adjusted.

Queries issued by the searcher: Port of Los Angeles cargo volume tariffs 2026; tariffs US container imports front-loading West Coast 2026 forecast; Port of Los Angeles July 2026 cargo TEUs news release; Port of Los Angeles August 2026 cargo volume TEUs

- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p38 Port of Los Angeles total container volume, July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p39 Port of Los Angeles total container volume, June 2026 (stated as topping 1 milli = **1,000,000** TEU (2026-06-01..2026-06-30) [DISCARD: Rounded 'topping 1 million' statement, not an exact June 2026 total; redundant with the exact July figure and unusable i] quote: ""After topping 1 million container units in June, we nearly reached that mark again in July,""
  - p40 Port of Los Angeles July 2026 total volume, year-over-year change = **6** % (2026-07-01..2026-07-31) [DISCARD: July 2026 YoY change; level p1/p2 kept, rate redundant.] quote: "July cargo was 6% lower than last year's all-time record for the month, when businesses surged cargo ahead of anticipated trade policy changes."
  - p41 Port of Los Angeles July 2026 total volume, deviation above five-year July avera = **7.5** % (2026-07-01..2026-07-31) [DISCARD: July 2026 deviation above 5-yr average; level p1 kept, rate redundant.] quote: "Despite the year-over-year decline, July volume was 7.5% above the Port's five-year average for the month."
  - p42 Port of Los Angeles loaded imports, July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p43 Port of Los Angeles loaded imports, July 2026 year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: July 2026 loaded-import YoY change; level p42 kept, rate redundant.] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p44 Port of Los Angeles loaded imports, July 2026 deviation above five-year July ave = **6** % (2026-07-01..2026-07-31) [DISCARD: July 2026 loaded-import deviation from 5-yr average; level p42 kept, rate redundant.] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p45 Port of Los Angeles loaded exports, July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p46 Port of Los Angeles loaded exports, July 2026 year-over-year change = **8** % (2026-07-01..2026-07-31) [DISCARD: July 2026 loaded-export YoY change; level p45 kept, rate redundant.] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p47 Port of Los Angeles empty containers, July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p48 Port of Los Angeles empty containers, July 2026 year-over-year change = **2** % (2026-07-01..2026-07-31) [DISCARD: July 2026 empty YoY change; level p47 kept, rate redundant.] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p49 Port of Los Angeles cumulative total container volume, first seven months of 202 = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p50 Port of Los Angeles cumulative total volume, first seven months of 2026, year-ov = **1.8** % (2026-01-01..2026-07-31) [DISCARD: Cumulative YoY change; level p49 kept, rate redundant.] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
- `https://globalmaritimehub.com/us-container-ports-surge-ahead-of-tariff-deadlines/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ca.finance.yahoo.com/news/early-surge-us-container-imports-170035204.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://theloadstar.com/transpacifc/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [base_rates] Loaded vs empty and import vs export composition

Hypothesis: Total TEU = loaded imports + loaded exports + empties; if a forecast or partial figure is loaded-only, apply the historical loaded share and empty share to reach total TEU.

Queries issued by the searcher: Port of Los Angeles loaded imports exports empty TEU monthly statistics; Port of Los Angeles September 2025 cargo volume TEU loaded empties; "Port of Los Angeles" July 2026 cargo volume TEU loaded imports empties news release August 2026; Port of Los Angeles container statistics historical TEU statistics 2024 empty imports empty exports September

- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2025` -> **snapshot** (snapshot 20260122223542); points raw/verified 15/13
  - p51 Port of LA September 2025 total TEUs (loaded + empty, imports + exports) = **883,053** TEU (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p52 Port of LA September 2025 loaded imports = **460,044** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 loaded imports; component of p51, redundant for total routes.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p53 Port of LA September 2025 loaded exports = **114,693** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 loaded exports; component of p51, redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p54 Port of LA September 2025 empty imports = **276** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 empty imports; component of p51, redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p55 Port of LA September 2025 empty exports = **308,040** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 empty exports; component of p51, redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p56 Port of LA September 2025 total imports (loaded + empty) = **460,320** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 total imports; component of p51, redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p57 Port of LA September 2025 total exports (loaded + empty) = **422,734** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 total exports; component of p51, redundant.] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p58 Port of LA calendar year 2025 total TEUs = **10,239,318** TEU (2025-01-01..2025-12-31) [DISCARD: CY2025 total; redundant with p11 and not needed for September routes.] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p59 Port of LA calendar year 2025 loaded imports = **5,316,713** TEU (2025-01-01..2025-12-31) [DISCARD: CY2025 loaded imports; not needed for September routes.] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p60 Port of LA calendar year 2025 loaded exports = **1,429,260** TEU (2025-01-01..2025-12-31) [DISCARD: CY2025 loaded exports; not needed for September routes.] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p61 Port of LA calendar year 2025 empty exports = **3,489,552** TEU (2025-01-01..2025-12-31) [DISCARD: CY2025 empty exports; not needed for September routes.] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p62 Port of LA calendar year 2025 empty imports = **3,793** TEU (2025-01-01..2025-12-31) [DISCARD: CY2025 empty imports; not needed for September routes.] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p63 Port of LA fiscal year 2024/25 total TEUs = **10,521,673** TEU (2024-07-01..2025-06-30) [DISCARD: Fiscal-year total; different period definition, not needed for September routes.] quote: "\| Total Fiscal Year 2024/25 \| 5,438,495.10 \| 7,382.00 \| 5,445,877.10 \| 1,428,787.25 \| 3,647,008.70 \| 5,075,795.95 \| 10,521,673.05 \| 14.07% \|"
- `https://ebs.publicnow.com/view/0E0D69315C173CCD05ADA0591E08AA6DCA3A6E3D` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2024` -> **snapshot** (snapshot 20250515145621); points raw/verified 15/15
  - p64 Port of LA September 2024 loaded imports (TEU) = **497,803** TEU (2024-09-01..2024-09-30) [DISCARD: September 2024 loaded imports; component of p68, redundant for total routes.] quote: "\| September \| 497,803.05 \| 2,083.85 \| 499,886.90 \| 114,702.25 \| 340,117.25 \| 454,819.50 \| 954,706.40 \| 27.56% \|"
  - p65 Port of LA September 2024 empty imports (TEU) = **2,084** TEU (2024-09-01..2024-09-30) [DISCARD: September 2024 empty imports; component of p68, redundant.] quote: "\| September \| 497,803.05 \| 2,083.85 \| 499,886.90 \| 114,702.25 \| 340,117.25 \| 454,819.50 \| 954,706.40 \| 27.56% \|"
  - p66 Port of LA September 2024 loaded exports (TEU) = **114,702** TEU (2024-09-01..2024-09-30) [DISCARD: September 2024 loaded exports; component of p68, redundant.] quote: "\| September \| 497,803.05 \| 2,083.85 \| 499,886.90 \| 114,702.25 \| 340,117.25 \| 454,819.50 \| 954,706.40 \| 27.56% \|"
  - p67 Port of LA September 2024 empty exports (TEU) = **340,117** TEU (2024-09-01..2024-09-30) [DISCARD: September 2024 empty exports; component of p68, redundant.] quote: "\| September \| 497,803.05 \| 2,083.85 \| 499,886.90 \| 114,702.25 \| 340,117.25 \| 454,819.50 \| 954,706.40 \| 27.56% \|"
  - p68 Port of LA September 2024 total TEUs = **954,706** TEU (2024-09-01..2024-09-30) [keep: ] quote: "\| September \| 497,803.05 \| 2,083.85 \| 499,886.90 \| 114,702.25 \| 340,117.25 \| 454,819.50 \| 954,706.40 \| 27.56% \|"
  - p69 Port of LA August 2024 total TEUs = **960,597** TEU (2024-08-01..2024-08-31) [DISCARD: August 2024 total; not needed for September routes.] quote: "\| August \| 509,362.70 \| 1,336.60 \| 510,699.30 \| 121,743.75 \| 328,154.00 \| 449,897.75 \| 960,597.05 \| 16.01% \|"
  - p70 Port of LA August 2024 loaded imports (TEU) = **509,363** TEU (2024-08-01..2024-08-31) [DISCARD: August 2024 loaded imports; not needed for September routes.] quote: "\| August \| 509,362.70 \| 1,336.60 \| 510,699.30 \| 121,743.75 \| 328,154.00 \| 449,897.75 \| 960,597.05 \| 16.01% \|"
  - p71 Port of LA August 2024 empty exports (TEU) = **328,154** TEU (2024-08-01..2024-08-31) [DISCARD: August 2024 empty exports; not needed for September routes.] quote: "\| August \| 509,362.70 \| 1,336.60 \| 510,699.30 \| 121,743.75 \| 328,154.00 \| 449,897.75 \| 960,597.05 \| 16.01% \|"
  - p72 Port of LA October 2024 total TEUs = **905,026** TEU (2024-10-01..2024-10-31) [DISCARD: October 2024 total; not needed for September routes.] quote: "\| October \| 462,740.25 \| 512.25 \| 463,252.50 \| 122,715.75 \| 319,057.50 \| 441,773.25 \| 905,025.75 \| 24.70% \|"
  - p73 Port of LA October 2024 loaded imports (TEU) = **462,740** TEU (2024-10-01..2024-10-31) [DISCARD: October 2024 loaded imports; not needed for September routes.] quote: "\| October \| 462,740.25 \| 512.25 \| 463,252.50 \| 122,715.75 \| 319,057.50 \| 441,773.25 \| 905,025.75 \| 24.70% \|"
  - p74 Port of LA October 2024 empty exports (TEU) = **319,058** TEU (2024-10-01..2024-10-31) [DISCARD: October 2024 empty exports; not needed for September routes.] quote: "\| October \| 462,740.25 \| 512.25 \| 463,252.50 \| 122,715.75 \| 319,057.50 \| 441,773.25 \| 905,025.75 \| 24.70% \|"
  - p75 Port of LA Total Calendar Year 2024 loaded imports (TEU) = **5,356,680** TEU (2024-01-01..2024-12-31) [DISCARD: CY2024 loaded imports; not needed for September routes.] quote: "\| Total Calendar Year 2024 \| 5,356,680.15 \| 7,529.30 \| 5,364,209.45 \| 1,494,201.30 \| 3,438,941.50 \| 4,933,142.80 \| 10,297,352.25 \| 19.32% \|"
  - p76 Port of LA Total Calendar Year 2024 empty exports (TEU) = **3,438,942** TEU (2024-01-01..2024-12-31) [DISCARD: CY2024 empty exports; not needed for September routes.] quote: "\| Total Calendar Year 2024 \| 5,356,680.15 \| 7,529.30 \| 5,364,209.45 \| 1,494,201.30 \| 3,438,941.50 \| 4,933,142.80 \| 10,297,352.25 \| 19.32% \|"
  - p77 Port of LA Total Calendar Year 2024 total TEUs = **10,297,352** TEU (2024-01-01..2024-12-31) [DISCARD: CY2024 total; redundant with p10.] quote: "\| Total Calendar Year 2024 \| 5,356,680.15 \| 7,529.30 \| 5,364,209.45 \| 1,494,201.30 \| 3,438,941.50 \| 4,933,142.80 \| 10,297,352.25 \| 19.32% \|"
  - p78 Port of LA Total Calendar Year 2024 loaded exports (TEU) = **1,494,201** TEU (2024-01-01..2024-12-31) [DISCARD: CY2024 loaded exports; not needed for September routes.] quote: "\| Total Calendar Year 2024 \| 5,356,680.15 \| 7,529.30 \| 5,364,209.45 \| 1,494,201.30 \| 3,438,941.50 \| 4,933,142.80 \| 10,297,352.25 \| 19.32% \|"
- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2026` -> **snapshot** (snapshot 20260325083853); points raw/verified 15/15
  - p79 Port of LA January 2026 loaded imports = **421,594** TEU (2026-01-01..2026-01-31) [DISCARD: January 2026 loaded imports; not needed for September routes.] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p80 Port of LA January 2026 empty imports = **115** TEU (2026-01-01..2026-01-31) [DISCARD: January 2026 empty imports; not needed for September routes.] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p81 Port of LA January 2026 loaded exports = **104,297** TEU (2026-01-01..2026-01-31) [DISCARD: January 2026 loaded exports; not needed for September routes.] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p82 Port of LA January 2026 empty exports = **285,994** TEU (2026-01-01..2026-01-31) [DISCARD: January 2026 empty exports; not needed for September routes.] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p83 Port of LA January 2026 total TEUs = **812,000** TEU (2026-01-01..2026-01-31) [DISCARD: January 2026 total; not needed for September routes.] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p84 Port of LA February 2026 loaded imports = **433,812** TEU (2026-02-01..2026-02-28) [DISCARD: February 2026 loaded imports; not needed for September routes.] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p85 Port of LA February 2026 empty imports = **17.25** TEU (2026-02-01..2026-02-28) [DISCARD: February 2026 empty imports; not needed for September routes.] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p86 Port of LA February 2026 loaded exports = **116,633** TEU (2026-02-01..2026-02-28) [DISCARD: February 2026 loaded exports; not needed for September routes.] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p87 Port of LA February 2026 empty exports = **273,860** TEU (2026-02-01..2026-02-28) [DISCARD: February 2026 empty exports; not needed for September routes.] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p88 Port of LA February 2026 total TEUs = **824,323** TEU (2026-02-01..2026-02-28) [DISCARD: February 2026 total; not needed for September routes.] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p89 Port of LA calendar year 2026 to date loaded imports = **855,406** TEU (2026-01-01..2026-02-28) [DISCARD: YTD Jan-Feb 2026 loaded imports; not needed for September routes.] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p90 Port of LA calendar year 2026 to date empty imports = **132** TEU (2026-01-01..2026-02-28) [DISCARD: YTD Jan-Feb 2026 empty imports; not needed for September routes.] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p91 Port of LA calendar year 2026 to date loaded exports = **220,930** TEU (2026-01-01..2026-02-28) [DISCARD: YTD Jan-Feb 2026 loaded exports; not needed for September routes.] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p92 Port of LA calendar year 2026 to date empty exports = **559,855** TEU (2026-01-01..2026-02-28) [DISCARD: YTD Jan-Feb 2026 empty exports; not needed for September routes.] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p93 Port of LA calendar year 2026 to date total TEUs = **1,636,324** TEU (2026-01-01..2026-02-28) [DISCARD: YTD Jan-Feb 2026 total; not needed for September routes.] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
- dropped by code checks: 2 (period year 2026 does not appear in the page text or URL (likely mis-dated): 2)

### d6 [physical_flow] Container ship calls and terminal throughput

Hypothesis: September TEU ≈ number of container vessel calls * average TEU exchanged per call * days, constrained by berth capacity and utilisation; vessel-call schedules and terminal capacity give a physical cross-check.

Queries issued by the searcher: Port of Los Angeles container vessel calls per month 2025; Port of Los Angeles TEU monthly cargo statistics 2025 September; Port of Los Angeles terminal throughput capacity TEU annual berth; Marine Exchange of Southern California container ship arrivals 2026 LA Long Beach daily; Port of Los Angeles July 2026 cargo volume TEU release; Port of Los Angeles container ship calls per month 2026 average TEU per call

- `https://en.portnews.ru/news/print/394249/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/topic/category/news/P220` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://prod.seatrade-maritime.com/ports-logistics/port-of-la-july-volumes-beat-pandemic-high` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://english.news.cn/northamerica/20251016/536c5ce80a8f44beb71a75015b218be0/c.html` -> **snapshot** (snapshot 20251016101956); points raw/verified 14/14
  - p94 Total TEU handled by Port of Los Angeles in September (loaded + empty, imports + = **883,053** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 total; duplicate of p51, redundant.] quote: "The Port of Los Angeles (POLA) handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p95 Year-on-year change in total TEU handled by Port of Los Angeles in September = **7.5** % (2025-09-01..2025-09-30) [DISCARD: Total YoY change for September 2025; level p94 kept, rate redundant.] quote: "handled 883,053 Twenty-Foot Equivalent Units (TEUs) in September, down 7.5 percent year on year"
  - p96 Loaded import TEUs at Port of Los Angeles in September = **460,044** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 loaded imports; duplicate of p52, redundant.] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p97 Year-on-year change in loaded import TEUs at Port of Los Angeles in September = **7.6** % (2025-09-01..2025-09-30) [DISCARD: Loaded-import YoY change for September 2025; level p96 kept, rate redundant.] quote: "loaded imports totaled 460,044 TEUs, a decrease of 7.6 percent from a year earlier"
  - p98 Loaded export TEUs at Port of Los Angeles in September = **114,693** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 loaded exports; duplicate of p53, redundant.] quote: "loaded exports stood at 114,693 TEUs, roughly the same as in 2024"
  - p99 Empty container TEUs processed by Port of Los Angeles in September = **308,317** TEU (2025-09-01..2025-09-30) [DISCARD: September 2025 empties; duplicate of p54+p55, redundant.] quote: "The port also processed 308,317 empty containers last month, 10 percent fewer than a year ago."
  - p100 Year-on-year change in empty container TEUs at Port of Los Angeles in September = **10** % (2025-09-01..2025-09-30) [DISCARD: Empty-container YoY change for September 2025; the level p99 is kept, the rate is redundant.] quote: "processed 308,317 empty containers last month, 10 percent fewer than a year ago"
  - p101 Forecast monthly import volume threshold for major U.S. container ports (below 2 = **2,000,000** TEU (2025-10-01..2025-12-31) [DISCARD: Qualitative threshold for late-2025 national imports; not a usable numeric input for September 2026 POLA.] quote: "current U.S. trade policies could cause monthly import volumes at major container ports to drop below the 2 million TEU mark for the rest of the year"
  - p102 Projected major U.S. ports import TEUs in October (NRF/Hackett forecast) = **1,970,000** TEU (2025-10-01..2025-10-31) [DISCARD: October 2025 national import forecast; wrong period and scope for September 2026 POLA.] quote: "It projected that major U.S. ports could see 1.97 million TEUs in October, down 12.3 percent year on year"
  - p103 Year-on-year change in projected major U.S. ports import TEUs in October = **12.3** % (2025-10-01..2025-10-31) [DISCARD: YoY change for October 2025 forecast; not used.] quote: "1.97 million TEUs in October, down 12.3 percent year on year"
  - p104 Projected major U.S. ports import TEUs in November (NRF/Hackett forecast) = **1,750,000** TEU (2025-11-01..2025-11-30) [DISCARD: November 2025 national import forecast; wrong period and scope.] quote: "1.75 million in November, down 19.2 percent"
  - p105 Year-on-year change in projected major U.S. ports import TEUs in November = **19.2** % (2025-11-01..2025-11-30) [DISCARD: YoY change for November 2025 forecast; not used.] quote: "1.75 million in November, down 19.2 percent"
  - p106 Projected major U.S. ports import TEUs in December (NRF/Hackett forecast) = **1,720,000** TEU (2025-12-01..2025-12-31) [DISCARD: December 2025 national import forecast; wrong period and scope.] quote: "1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"
  - p107 Year-on-year change in projected major U.S. ports import TEUs in December = **19.4** % (2025-12-01..2025-12-31) [DISCARD: YoY change for December 2025 forecast; not used.] quote: "1.72 million in December, dropping 19.4 percent -- the lowest since March 2023"

### b1 [own_history] Port of Los Angeles monthly cargo releases

Hypothesis: August 2026 POLA total TEU (published ~mid-September 2026) would anchor the level immediately before the target month and let a Sep/Aug seasonal ratio be applied; it is the single most valuable missing input for the own-history route.

Queries issued by the searcher: Port of Los Angeles July 2026 cargo volumes TEU; portoflosangeles.org cargo news August 2026 TEU; Port of Los Angeles monthly TEU statistics 2026 loaded imports exports empties; Port of Los Angeles September 2026 cargo news release

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_081826_july_cargo` -> **snapshot** (snapshot 20260825030911); points raw/verified 13/13
  - p108 Port of Los Angeles total TEU handled, July 2026 = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "The Port of Los Angeles processed 960,464 Twenty-Foot Equivalent Units (TEUs) in July, making it the second-busiest July in the Port's history."
  - p109 Port of Los Angeles loaded imports, July 2026 = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p110 Port of Los Angeles loaded exports, July 2026 = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p111 Port of Los Angeles empty containers, July 2026 = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p112 Port of Los Angeles cumulative total TEU handled, first seven months of 2026 (Ja = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p113 Port of Los Angeles cumulative total TEU, first seven months of 2026, year-over- = **1.8** % (2026-01-01..2026-07-31) [keep: ] quote: "During the first seven months of 2026, the Port handled 6,083,067 TEUs, 1.8% ahead of the same period last year."
  - p114 Port of Los Angeles July 2026 total TEU, year-over-year change = **6** % (2026-07-01..2026-07-31) [keep: ] quote: "July cargo was 6% lower than last year's all-time record for the month, when businesses surged cargo ahead of anticipated trade policy changes."
  - p115 Port of Los Angeles July 2026 total TEU, deviation above five-year July average = **7.5** % (2026-07-01..2026-07-31) [keep: ] quote: "Despite the year-over-year decline, July volume was 7.5% above the Port's five-year average for the month."
  - p116 Port of Los Angeles loaded imports, July 2026, year-over-year change = **8** % (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p117 Port of Los Angeles loaded imports, July 2026, deviation above five-year July av = **6** % (2026-07-01..2026-07-31) [keep: ] quote: "Loaded imports reached 499,552 TEUs in July, down 8% compared with last year's record month but 6% above the five-year July average."
  - p118 Port of Los Angeles loaded exports, July 2026, year-over-year change = **8** % (2026-07-01..2026-07-31) [keep: ] quote: "Loaded exports totaled 111,776 TEUs, down 8% compared with last year."
  - p119 Port of Los Angeles empty containers, July 2026, year-over-year change = **2** % (2026-07-01..2026-07-31) [keep: ] quote: "Empty containers totaled 349,137 TEUs, down 2% year over year."
  - p120 Port of Los Angeles June 2026 total container volume (stated as topping 1 millio = **1,000,000** container units (TEU) (2026-06-01..2026-06-30) [DISCARD: Rounded 'topping 1 million' statement; redundant with the precise July figure and not usable as a level.] quote: ""After topping 1 million container units in June, we nearly reached that mark again in July," said Port of Los Angeles Executive Director Gene Seroka."
- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 14/14
  - p121 Port of Los Angeles July 2026 total container volume (loaded + empty, TEU) = **960,464** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p122 Port of Los Angeles July 2026 loaded imports (TEU) = **499,552** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p123 Port of Los Angeles July 2026 loaded exports (TEU) = **111,776** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p124 Port of Los Angeles July 2026 total loaded (imports + exports, TEU) = **611,327** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p125 Port of Los Angeles July 2026 total empty containers (TEU) = **349,137** TEU (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p126 Port of Los Angeles July 2025 total container volume (prior-year comparison, TEU = **1,019,837** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p127 Port of Los Angeles July 2025 loaded imports (TEU) = **543,728** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p128 Port of Los Angeles July 2025 loaded exports (TEU) = **121,507** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p129 Port of Los Angeles July 2025 total loaded (TEU) = **665,235** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p130 Port of Los Angeles July 2025 total empty containers (TEU) = **354,602** TEU (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p131 Port of Los Angeles calendar year 2026 year-to-date total container volume (TEU) = **6,083,067** TEU (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p132 Port of Los Angeles calendar year 2025 same-period year-to-date total container  = **5,975,649** TEU (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p133 Port of Los Angeles calendar year 2025 total container volume (annual, TEU) = **10,239,318** TEU (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
  - p134 Port of Los Angeles calendar year 2024 total container volume (annual, TEU) = **10,297,352** TEU (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"

### b2 [forecasts_markets] NRF/Global Port Tracker and carrier outlooks

Hypothesis: A September 2026 national or West Coast import forecast would give an independent level and a tariff-adjusted trend factor; combined with POLA's stable share of West Coast imports it would cross-check the own-history route.

Queries issued by the searcher: Global Port Tracker September 2026 forecast US imports; NRF Global Port Tracker 2026 forecast West Coast ports import volume; Port of Los Angeles share of West Coast container imports 2026 percent; Port of Los Angeles July 2026 cargo news release 960,464 TEU loaded imports

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gcaptain.com/u-s-container-imports-defy-expectations-as-peak-season-stretches-into-september/` -> **snapshot** (snapshot 20260910101111); points raw/verified 15/9
  - p135 NRF Global Port Tracker July 2026 imports at covered ports = **2,300,000** TEU (2026-07-01..2026-07-31) [keep: ] quote: "slightly above July's 2.3 million TEU"
  - p136 NRF Global Port Tracker May 2026 imports at covered ports = **2,240,000** TEU (2026-05-01..2026-05-31) [keep: ] quote: "May's 2.24 million TEU appeared likely to remain the high-water mark for 2026"
  - p137 NRF Global Port Tracker final July 2026 imports at covered ports = **2,300,000** TEU (2026-07-01..2026-07-31) [keep: ] quote: "U.S. ports covered by Global Port Tracker handled 2.3 million TEU in July, the latest month for which final figures are available."
  - p138 Month-over-month change in July 2026 imports at covered ports = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "That was up 3.2% from June, although still down 3.9% from a year earlier."
  - p139 Year-over-year change in July 2026 imports at covered ports = **3.9** % (2026-07-01..2026-07-31) [keep: ] quote: "That was up 3.2% from June, although still down 3.9% from a year earlier."
  - p140 NRF Global Port Tracker estimate: August 2026 imports at covered ports = **2,290,000** TEU (2026-08-01..2026-08-31) [keep: ] quote: "August, which has yet to be finalized, is now estimated at 2.29 million TEU, down 1.3% year over year."
  - p141 Prior-month NRF Global Port Tracker forecast for August 2026 imports = **2,220,000** TEU (2026-08-01..2026-08-31) [keep: ] quote: "Last month, Global Port Tracker had forecast August at 2.22 million TEU."
  - p142 Full-year 2025 imports at covered ports = **25,400,000** TEU (2025-01-01..2025-12-31) [keep: ] quote: "up 1% from 25.4 million TEU last year"
  - p143 First-half 2026 imports at covered ports = **12,700,000** TEU (2026-01-01..2026-06-30) [keep: ] quote: "The first half of 2026 totaled 12.7 million TEU, up 1.1% from the same period in 2025."
- `https://www.pmsaship.com/maritime-insights-blog/uswc-shares-of-container-traffic-through-us-ports-in-august-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kbcadvisors.com/insights/mid-year-2026-top-us-container-report` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end 2026-09-30 after as_of: 3; period_end 2026-10-31 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-12-31 after as_of: 1)

### b3 [related_series] San Pedro Bay sibling port

Hypothesis: Port of Long Beach August/September 2026 TEU and the POLA/POLB ratio would let POLA September be inferred from the combined bay volume; the ratio is fairly stable and would resolve uncertainty in the tariff-driven level.

Queries issued by the searcher: Port of Long Beach cargo news August 2026 TEU; POLB TEU September 2026 container volume; Port of Los Angeles September 2026 TEU record cargo news release; San Pedro Bay ports combined container volume 2026 Los Angeles Long Beach TEU monthly

- `https://portoflosangeles.org/references/2026-news-releases/news_100926_sept_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.worldports.org/port-of-long-beach-records-increased-cargo-growth/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.supplychain247.com/article/polb_sets_new_all_time_monthly_volume_record_for_the_port_in_september` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.shippingnewsnet.com/news/articleView.html?idxno=72550` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['port los angeles teu', 'container volume september', 'pola cargo']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p38', 'p49'] Same July 2026 total TEU (960,464) reported in the statistics table and the August 2026 news release; same underlying Port measurement, so this is one fact, not independent confirmation.
- corroborating: ['p3', 'p42'] July 2026 loaded imports 499,552 TEU appear in both the table and the news release; identical underlying source.
- corroborating: ['p4', 'p45'] July 2026 loaded exports 111,776 TEU in table and release; same source.
- corroborating: ['p6', 'p47'] July 2026 empties 349,137 TEU in table and release; same source.
- corroborating: ['p1', 'p2', 'p40'] July 2026 vs July 2025 totals (960,464 vs 1,019,837) imply about -5.8%, consistent with the release's '6% lower' statement; rounding-level agreement.
- corroborating: ['p7', 'p8', 'p49', 'p50'] Cumulative Jan-Jul 2026 6,083,067 vs 5,975,649 in 2025 implies +1.8%, matching the release; same source.
- corroborating: ['p51', 'p94', 'p96', 'p98', 'p99'] September 2025 total 883,053 TEU and component figures agree between the Port table and the Xinhua report; Xinhua is reporting the Port's release, so not independent.
- corroborating: ['p54', 'p55', 'p99'] Empty imports 276 + empty exports 308,040 = 308,316, matching the reported 308,317 empties; internally consistent.
- corroborating: ['p15', 'p20'] September 2023 (748,440) vs August 2023 (828,016) gives a plausible Sep/Aug ratio for POLA; both from the same trade-press reporting of Port releases.
- corroborating: ['p12', 'p13', 'p14'] Long Beach August 2024 record and prior record are internally consistent; only contextual for POLA share, not a POLA level.
- corroborating: ['p24', 'p26', 'p28'] POLA loaded imports YTD and May 2026 month, plus empty share, come from one Dwell dataset; useful for composition but not for September level.
- corroborating: ['p101', 'p102', 'p104', 'p106'] NRF/Hackett forecasts for Oct-Dec 2025 are one forecast family; they describe late-2025 national imports, not September 2026, so only directional context.
- conflicting: ['p39', 'p1'] June 2026 is described only as 'topping 1 million' (rounded, no exact figure); cannot be combined with the exact July total in a series without a conversion.
- conflicting: ['p19'] The 'previous September high in 2020 by 78,849 TEU' is a margin, not a level; the value field (78,849 TEU) is a mislabeled difference and must not be used as a September volume.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p38', 'p108', 'p121'] Same July 2026 total TEU (960,464) reported in the statistics table and the August 18 news release; identical measurement, not independent.
- corroborating: ['p3', 'p42', 'p109', 'p122'] Same July 2026 loaded imports (499,552) across table and release.
- corroborating: ['p4', 'p45', 'p110', 'p123'] Same July 2026 loaded exports (111,776).
- corroborating: ['p6', 'p47', 'p111', 'p125'] Same July 2026 empties (349,137).
- corroborating: ['p7', 'p49', 'p112', 'p131'] Same Jan–Jul 2026 cumulative (6,083,067).
- corroborating: ['p5', 'p124'] Same July 2026 total loaded (611,327); consistent with p3+p4.
- corroborating: ['p2', 'p126'] Same July 2025 total (1,019,837) used as prior-year comparison.
- corroborating: ['p114', 'p116', 'p118', 'p119'] Component YoY declines (imports -8%, exports -8%, empties -2%) are consistent with the -5.8% total decline in p1 vs p2.
- corroborating: ['p51', 'p68'] September totals for 2025 and 2024 form the target's own seasonal series; 2025 lower than 2024 reflects the post-front-loading pullback.
- corroborating: ['p135', 'p137', 'p138', 'p139'] NRF GPT July 2026 imports 2.3M TEU, +3.2% MoM, -3.9% YoY; consistent internally.
- corroborating: ['p140', 'p141'] August 2026 GPT estimate revised up from 2.22M to 2.29M; shows forecast revision direction, not independent confirmation.
- corroborating: ['p1', 'p135'] POLA July 2026 down ~6% YoY while national covered-port imports down 3.9% YoY; broadly consistent direction of a tariff-driven pullback.
- corroborating: ['p120', 'p1'] June 2026 'topping 1 million' and July 960,464 imply a modest June-to-July decline, consistent with a high but easing level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 vs September 2025 POLA total TEU change factor | 0.97 | 0.85..1.1 | 0.85..1.1 | ratio | m1 (m1) | July 2026 was 5.8% below July 2025 (p1 vs p2) and national covered-port imports were 3.9% below year-earlier in July (p139); September 2025 was itself already down 7.5% YoY (p51), so the YoY gap should narrow. A near-flat to slightly-down factor centered at 0.97 with wide range reflects tariff-drive | September 2026 demand tracks the mid-2026 YoY decline rather than a renewed front-loading surge. | Evidence of a September 2026 import surge or collapse (e.g., August/September GPT or POLB figures far from trend). |
| a2 | September/August seasonal ratio for POLA total TEU | 0.95 | 0.88..1.02 | 0.6699..1.34 (widened) | ratio | unused | September is typically a modest step down from August as peak season ends; using July 2026 (p1) as an August proxy, a ~0.95 ratio with wide range captures normal seasonal easing plus tariff distortion. | August 2026 level is close to July 2026 (p1) and normal post-peak easing applies. | A published August 2026 POLA figure materially different from July, or evidence of atypical September seasonality. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 853,883 | ['p51'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | series_naive | 918,880 |  | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target

Result: central **885,785** TEU, 80% interval [642,963, 1,220,313] TEU, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total container volume handled by the Port of Los Angeles (loaded plus empty, imports plus exports combined) during September 2026 is 885,785 TEU (80% model-based interval 642,963 to 1,220,313 TEU).

Evidence: one method anchors on the observed September 2025 total of 883,053 TEU and applies a September 2026 year-over-year change factor of 0.97 (range 0.85 to 1.1), giving 853,883 TEU at weight 50%. The second method is a history-only seasonal baseline averaging the two most recent Septembers (883,053 TEU and 954,706 TEU), giving 918,880 TEU at weight 50%. The two are combined at equal weight because no backtest error was available to discriminate between them.

The change factor is an analyst assumption, not an observation; the September totals are observed. The main risk is a tariff-driven September surprise that the near-flat factor misses. Better evidence would be actual September 2026 port throughput or weekly terminal data before the release.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 vs September 2025 POLA total TEU change factor: 0.97 ratio, range 0.85 to 1.1; used by m1. Overturned by: Evidence of a September 2026 import surge or collapse (e.g., August/September GPT or POLB figures far from trend).

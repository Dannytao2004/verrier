# Evidence ledger: fc_pola_teu_2026_09

- Question: Assume today is 2026-09-10. You know nothing published after this date. Estimate the total container volume handled by the Port of Los Angeles in September 2026, in TEUs (twenty-foot equivalent units; loaded and empty imports and exports combined), as it will be first reported in the Port of Los Angeles's monthly cargo news release.
- as_of: 2026-09-10
- Pinned target: Total container throughput handled by the Port of Los Angeles in September 2026, reported as TEUs and combining loaded and empty imports and exports, as first published in the Port of Los Angeles monthly cargo news release. | unit TEUs | period 2026-09-01..2026-09-30 | publisher Port of Los Angeles (monthly cargo news release)

- Official value (scoring only, never shown to the agent): 1,042,652

## Directions and pages

### d1 [own_history] Port of Los Angeles time-series analyst

Hypothesis: September 2026 total TEU is best anchored by recent monthly totals and repeated September seasonal ratios. If the 2026 run-rate and seasonal pattern remain stable, a September seasonal factor applied to the latest available run-rate narrows the estimate. Main transfer assumption: no definitional break in TEU accounting and no extraordinary September shock.

Queries issued by the searcher: Port of Los Angeles monthly cargo September 2025 total TEUs; Port of Los Angeles cargo statistics August 2026 TEUs; Port of Los Angeles September 2024 cargo 954,706 TEUs; Port of Los Angeles monthly container statistics history TEU 2022 2023 2024 September annual table

- `https://portoflosangeles.org/business/statistics/container-statistics` -> **snapshot** (snapshot 20260908074418); points raw/verified 14/14
  - p1 Port of Los Angeles total TEUs, July 2026 = **960,464** TEUs (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p2 Port of Los Angeles total TEUs, July 2025 = **1,019,837** TEUs (2025-07-01..2025-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p3 Port of Los Angeles total TEUs year-over-year change, July 2026 vs July 2025 = **-5.82** % (2026-07-01..2026-07-31) [keep: ] quote: "\| Total \| 960,464.25 \| 1,019,837.30 \| (59,373.05) \| -5.82% \|"
  - p4 Port of Los Angeles loaded imports TEUs, July 2026 = **499,552** TEUs (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Imports \| 499,551.50 \| 543,727.80 \| (44,176.30) \| -8.12% \|"
  - p5 Port of Los Angeles loaded exports TEUs, July 2026 = **111,776** TEUs (2026-07-01..2026-07-31) [keep: ] quote: "\| Loaded Exports \| 111,775.50 \| 121,507.00 \| (9,731.50) \| -8.01% \|"
  - p6 Port of Los Angeles total loaded TEUs, July 2026 = **611,327** TEUs (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Loaded \| 611,327.00 \| 665,234.80 \| (53,907.80) \| -8.10% \|"
  - p7 Port of Los Angeles total empty TEUs, July 2026 = **349,137** TEUs (2026-07-01..2026-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p8 Port of Los Angeles total empty TEUs, July 2025 = **354,602** TEUs (2025-07-01..2025-07-31) [keep: ] quote: "\| Total Empty \| 349,137.25 \| 354,602.50 \| (5,465.25) \| -1.54% \|"
  - p9 Port of Los Angeles calendar year 2026 cumulative total TEUs (year-to-date) = **6,083,067** TEUs (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p10 Port of Los Angeles calendar year 2025 cumulative total TEUs same period = **5,975,649** TEUs (2025-01-01..2025-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p11 Port of Los Angeles calendar year 2026 cumulative total TEUs year-over-year % ch = **1.8** % (2026-01-01..2026-07-31) [keep: ] quote: "\| Calendar Year 2026 \| 6,083,066.75 \| 5,975,649.00 \| 107,417.75 \| 1.80% \|"
  - p12 Port of Los Angeles annual total TEUs, 2025 = **10,239,318** TEUs (2025-01-01..2025-12-31) [DISCARD: Exact duplicate of p60 (2025 annual total 10,239,318 TEUs); retaining both would double-count one figure in any median-b] quote: "\| 2025 \| 10,239,318 \| 2015 \| 8,160,458 \| 2005 \| 7,484,624 \| 1995 \| 2,555,206 \| 1985 \| 1,103,722 \|"
  - p13 Port of Los Angeles annual total TEUs, 2024 = **10,297,352** TEUs (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 10,297,352 \| 2014 \| 8,340,066 \| 2004 \| 7,321,440 \| 1994 \| 2,518,619 \| 1984 \| 908,417 \|"
  - p14 Port of Los Angeles annual total TEUs, 2023 = **8,629,681** TEUs (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023 \| 8,629,681 \| 2013 \| 7,868,582 \| 2003 \| 7,178,940 \| 1993 \| 2,318,920 \| 1983 \| 733,979 \|"
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2024-news-releases/news_101824_sept_cargo` -> **snapshot** (snapshot 20251205184257); points raw/verified 11/11
  - p15 Port of Los Angeles total TEUs handled in September 2024 (record month) = **954,706** TEUs (2024-09-01..2024-09-30) [keep: ] quote: "The Port of Los Angeles handled a record 954,706 Twenty-Foot Equivalent Units (TEUs) in September, a 27% increase over the previous year."
  - p16 Port of Los Angeles September 2024 total TEU year-over-year change = **27** % (2024-09-01..2024-09-30) [keep: ] quote: "a 27% increase over the previous year"
  - p17 Port of Los Angeles total TEUs in the three months ending September 2024 (busies = **2,854,904** TEUs (2024-07-01..2024-09-30) [keep: ] quote: "which processed 2,854,904 TEUs in the last three months"
  - p18 Port of Los Angeles cumulative total TEUs January-September 2024 = **7,586,395** TEUs (2024-01-01..2024-09-30) [keep: ] quote: "Overall, the Port has moved 7,586,395 TEUs the first nine months of 2024, an 18% increase over the 2023 mark."
  - p19 Port of Los Angeles cumulative total TEU year-over-year change January-September = **18** % (2024-01-01..2024-09-30) [keep: ] quote: "Nine months into 2024, the Port of Los Angeles is 18% ahead of its 2023 pace."
  - p20 Port of Los Angeles loaded imports in September 2024 = **497,803** TEUs (2024-09-01..2024-09-30) [keep: ] quote: "September 2024 loaded imports landed at 497,803 TEUs, a 26% increase compared to the previous year."
  - p21 Port of Los Angeles loaded imports September 2024 year-over-year change = **26** % (2024-09-01..2024-09-30) [keep: ] quote: "loaded imports landed at 497,803 TEUs, a 26% increase compared to the previous year"
  - p22 Port of Los Angeles loaded exports in September 2024 = **114,702** TEUs (2024-09-01..2024-09-30) [keep: ] quote: "Loaded exports came in at 114,702 TEUs, a 5% decrease compared to 2023."
  - p23 Port of Los Angeles loaded exports September 2024 year-over-year change = **5** % (2024-09-01..2024-09-30) [keep: ] quote: "Loaded exports came in at 114,702 TEUs, a 5% decrease compared to 2023."
  - p24 Port of Los Angeles empty containers processed in September 2024 = **342,201** TEUs (2024-09-01..2024-09-30) [keep: ] quote: "The Port processed 342,201 empty containers, a 45% jump compared to 2023."
  - p25 Port of Los Angeles empty containers September 2024 year-over-year change = **45** % (2024-09-01..2024-09-30) [keep: ] quote: "The Port processed 342,201 empty containers, a 45% jump compared to 2023."
- `https://airfreight.news/articles/full/september-cargo-volume-boosts-port-of-los-angeles-to-record-quarter` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [physical_flow] Vessel and terminal operations planner

Hypothesis: Monthly throughput equals scheduled container-vessel calls times average TEU exchange per call, adjusted for omitted or missed calls. September 2026 vessel arrival schedules and service strings observed before or during the month provide an independent exposure measure. Transfer assumption: average moves per call from recent months by vessel class or service remains applicable.

Queries issued by the searcher: Port of Los Angeles monthly cargo news release August 2026 TEUs; Port of Los Angeles vessel arrival schedule September 2026 container; Whisk Logistics weekly drayage roundup September 2026 Port Optimizer LA forecast vessels; Port of Los Angeles "vessel calls" per month container ships statistic 2026

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-03` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://airliftusa.com/sealanes/port/USLAX` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/august-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] San Pedro Bay port-complex analyst

Hypothesis: LA throughput can be bridged from San Pedro Bay combined throughput multiplied by LA's share. If LA's share of the adjacent port complex is stable around recent values, an independent forecast or early indicator for Long Beach/San Pedro Bay constrains September 2026. Transfer assumption: adjacent ports face similar regional trade and carrier service rotations, though share can shift with service strings.

Queries issued by the searcher: Port of Long Beach monthly cargo September 2025 TEUs; San Pedro Bay container throughput August 2026; Los Angeles Long Beach port market share TEU; Port of Los Angeles August 2026 cargo volumes TEUs

- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-03` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/august-2026-container-traffic-at-north-american-ports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://labusinessjournal.com/ports/strong-august-continues-trade-trend-at-twin-ports/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/topic/category/news/P220` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Trade forecast and carrier-guidance analyst

Hypothesis: Published port or trade forecasts for 2026 and national container-import forecasts can be converted to September LA TEUs via LA share and monthly seasonality. Forecast error and policy changes are the main uncertainties. Transfer assumption: forecast coverage and definitions match Port of Los Angeles total TEUs after adjustment.

Queries issued by the searcher: Port of Los Angeles 2026 cargo forecast TEU budget; Global Port Tracker September 2026 container imports forecast; Port of Los Angeles share of US container imports 2026 percent West Coast market share; Port of Los Angeles monthly container volume 2026 TEU July August Seroka

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_061126_budget` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/uswc-shares-of-container-traffic-through-us-ports-in-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.connectcre.com/stories/at-connect-industrial-west-2026-port-of-las-seroka-charts-new-course/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Trade-policy and operations risk analyst

Hypothesis: Tariff changes, port labor actions, carrier blank sailings, canal or Red Sea diversions, and calendar effects can shift September 2026 away from seasonal history. Measure exposure via announced blank sailings, service changes, and policy effective dates before the cutoff; use these as scenario adjustments to baseline routes, not as a direct estimate.

Queries issued by the searcher: transpacific blank sailings September 2026; Port of Los Angeles monthly cargo news release container throughput TEU; Global Port Tracker September 2026 forecast imports NRF Hackett; Port of Los Angeles August 2026 cargo volume TEUs release

- `https://finance.yahoo.com/economy/articles/nrf-walks-back-peak-season-175759004.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mundomaritimo.cl/noticias/lineas-navieras-aplicaran-45-cancelaciones-de-itinerarios-entre-el-31-de-agosto-y-el-4-de-octubre` -> **snapshot** (snapshot 20260904130444); points raw/verified 11/5
  - p26 Drewry World Container Index spot freight rate, as of Aug 27, 2026 = **4.473** USD per FEU (2026-08-27..2026-08-27) [keep: ] quote: "El World Container Index (WCI)de Drewry-que sigue la evolución de las tarifas de fletes spot se ubicó en US$4.473/FEU al 27 de agosto"
  - p27 Week-over-week change in WCI spot freight rate, week to Aug 27, 2026 = **1** % (2026-08-20..2026-08-27) [keep: ] quote: "tras registrar una disminución de 1% respecto de la semana anterior."
  - p28 Week-over-week change in Transpacific and Transatlantic freight rates, week to A = **1** % (2026-08-20..2026-08-27) [keep: ] quote: "las tarifas en las rutas Transpacífico y Transatlántico disminuyeron 1% semanal"
  - p29 Week-over-week change in Asia-North Europe/Mediterranean freight rates, week to  = **2** % (2026-08-20..2026-08-27) [keep: ] quote: "mientras que las correspondientes a la ruta Asia-Norte de Europa/Mediterráneo cayeron 2%."
  - p30 WCI spot freight rate level versus one year earlier, as of Aug 27, 2026 = **111** % (2026-08-27..2026-08-27) [keep: ] quote: "el WCI se mantiene 111% por encima de su nivel registrado un año atrás, es decir, más del doble."
- `https://www.maersk.com.cn/ko-kr/news/articles/2026/09/09/north-america-market-update-september` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end 2026-10-04 after as_of: 6)

### d6 [related_series] Component-level throughput forecaster

Hypothesis: Total TEU equals loaded imports plus loaded exports plus empty imports plus empty exports. Forecasting loaded imports from national import demand and LA share, with exports and empties from recent ratios, reduces reliance on total-seasonality assumptions. Transfer assumption: component shares and empty-repositioning ratios remain near recent ranges.

Queries issued by the searcher: Port of Los Angeles loaded imports empty exports TEUs August 2026; Port of Los Angeles monthly container component TEU loaded imports loaded exports empties; NRF Global Port Tracker September 2026 forecast import TEUs; Port of Los Angeles September 2026 outlook Seroka expects strong September volumes

- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2026` -> **snapshot** (snapshot 20260325083853); points raw/verified 15/15
  - p31 Port of Los Angeles loaded imports, January 2026 = **421,594** TEUs (2026-01-01..2026-01-31) [keep: ] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p32 Port of Los Angeles empty imports, January 2026 = **115** TEUs (2026-01-01..2026-01-31) [keep: ] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p33 Port of Los Angeles loaded exports, January 2026 = **104,297** TEUs (2026-01-01..2026-01-31) [keep: ] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p34 Port of Los Angeles empty exports, January 2026 = **285,994** TEUs (2026-01-01..2026-01-31) [keep: ] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p35 Port of Los Angeles total TEUs, January 2026 = **812,000** TEUs (2026-01-01..2026-01-31) [keep: ] quote: "\| January \| 421,593.75 \| 115.00 \| 421,708.75 \| 104,297.00 \| 285,994.50 \| 390,291.50 \| 812,000.25 \| -12.14% \|"
  - p36 Port of Los Angeles loaded imports, February 2026 = **433,812** TEUs (2026-02-01..2026-02-28) [keep: ] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p37 Port of Los Angeles empty imports, February 2026 = **17.25** TEUs (2026-02-01..2026-02-28) [keep: ] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p38 Port of Los Angeles loaded exports, February 2026 = **116,633** TEUs (2026-02-01..2026-02-28) [keep: ] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p39 Port of Los Angeles empty exports, February 2026 = **273,860** TEUs (2026-02-01..2026-02-28) [keep: ] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p40 Port of Los Angeles total TEUs, February 2026 = **824,323** TEUs (2026-02-01..2026-02-28) [keep: ] quote: "\| February \| 433,812.25 \| 17.25 \| 433,829.50 \| 116,633.25 \| 273,860.50 \| 390,493.75 \| 824,323.25 \| 2.86% \|"
  - p41 Port of Los Angeles cumulative loaded imports, calendar year 2026 to date = **855,406** TEUs (2026-01-01..2026-02-28) [keep: ] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p42 Port of Los Angeles cumulative loaded exports, calendar year 2026 to date = **220,930** TEUs (2026-01-01..2026-02-28) [keep: ] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p43 Port of Los Angeles cumulative empty exports, calendar year 2026 to date = **559,855** TEUs (2026-01-01..2026-02-28) [keep: ] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p44 Port of Los Angeles cumulative total TEUs, calendar year 2026 to date = **1,636,324** TEUs (2026-01-01..2026-02-28) [keep: ] quote: "\| Total Calendar Year 2026 \| 855,406.00 \| 132.25 \| 855,538.25 \| 220,930.25 \| 559,855.00 \| 780,785.25 \| 1,636,323.50 \| -5.18% \|"
  - p45 Port of Los Angeles cumulative total TEUs, fiscal year 2025/26 in progress = **6,919,830** TEUs (2025-07-01..2026-02-28) [keep: ] quote: "\| Total Fiscal Year 2025/26 (in progress) \| 3,623,891.30 \| 1,470.40 \| 3,625,361.70 \| 930,054.25 \| 2,364,414.25 \| 3,294,468.50 \| 6,919,830.20 \| -5.10% \|"
- `https://portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2025` -> **snapshot** (snapshot 20260122223542); points raw/verified 15/15
  - p46 Port of Los Angeles loaded imports, September 2025 = **460,044** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p47 Port of Los Angeles loaded exports, September 2025 = **114,693** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p48 Port of Los Angeles empty imports, September 2025 = **276** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p49 Port of Los Angeles empty exports, September 2025 = **308,040** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p50 Port of Los Angeles total TEUs, September 2025 = **883,053** TEUs (2025-09-01..2025-09-30) [keep: ] quote: "\| September \| 460,043.75 \| 276.00 \| 460,319.75 \| 114,693.00 \| 308,040.50 \| 422,733.50 \| 883,053.25 \| -7.51% \|"
  - p51 Port of Los Angeles loaded imports, August 2025 = **504,514** TEUs (2025-08-01..2025-08-31) [keep: ] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p52 Port of Los Angeles loaded exports, August 2025 = **127,379** TEUs (2025-08-01..2025-08-31) [keep: ] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p53 Port of Los Angeles empty exports, August 2025 = **326,006** TEUs (2025-08-01..2025-08-31) [keep: ] quote: "\| August \| 504,514.25 \| 456.65 \| 504,970.90 \| 127,378.75 \| 326,005.50 \| 453,384.25 \| 958,355.15 \| -0.23% \|"
  - p54 Port of Los Angeles loaded imports, October 2025 = **429,280** TEUs (2025-10-01..2025-10-31) [keep: ] quote: "\| October \| 429,279.75 \| 21.00 \| 429,303.75 \| 123,764.25 \| 295,359.25 \| 419,127.50 \| 848,424.25 \| -6.25% \|"
  - p55 Port of Los Angeles loaded exports, October 2025 = **123,764** TEUs (2025-10-01..2025-10-31) [keep: ] quote: "\| October \| 429,279.75 \| 21.00 \| 429,303.75 \| 123,764.25 \| 295,359.25 \| 419,127.50 \| 848,424.25 \| -6.25% \|"
  - p56 Port of Los Angeles empty exports, October 2025 = **295,359** TEUs (2025-10-01..2025-10-31) [keep: ] quote: "\| October \| 429,279.75 \| 21.00 \| 429,303.75 \| 123,764.25 \| 295,359.25 \| 419,127.50 \| 848,424.25 \| -6.25% \|"
  - p57 Port of Los Angeles loaded imports, calendar year 2025 total = **5,316,713** TEUs (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p58 Port of Los Angeles loaded exports, calendar year 2025 total = **1,429,260** TEUs (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p59 Port of Los Angeles empty exports, calendar year 2025 total = **3,489,552** TEUs (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
  - p60 Port of Los Angeles total TEUs, calendar year 2025 total = **10,239,318** TEUs (2025-01-01..2025-12-31) [keep: ] quote: "\| Total Calendar Year 2025 \| 5,316,713.30 \| 3,793.15 \| 5,320,506.45 \| 1,429,260.00 \| 3,489,551.95 \| 4,918,811.95 \| 10,239,318.40 \| -0.56% \|"
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [capacity_consumption] Terminal capacity planner

Hypothesis: Realized throughput is bounded by terminal and berth capacity times utilization and operating days. If September schedules imply near-normal utilization, the capacity route checks plausibility and sets a ceiling or floor. Transfer assumption: publicly known terminal capacity and utilization are reasonably representative of realized container moves.

Queries issued by the searcher: Port of Los Angeles monthly cargo news release TEU September record; Port of Los Angeles container terminal capacity TEU annual throughput; Port of Los Angeles August 2026 cargo volume news release 955,907 TEU; Port of Los Angeles July 2025 record 1,019,837 TEU monthly cargo

- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pmsaship.com/maritime-insights-blog/outlook-for-container-volumes-in-san-pedro-bay` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://maritime-executive.com/index.php/article/port-of-la-displays-resilience-achieving-third-best-year-in-2025` -> **snapshot** (snapshot 20260218061518); points raw/verified 15/11
  - p61 Port of Los Angeles total container throughput, 2025 (annual) = **10,200,000** TEU (2025-01-01..2025-12-31) [DISCARD: Rounded secondary restatement ('10.2 million TEU') of the publisher's own annual total already held exactly in p12/p60; ] quote: "Los Angeles saw its container throughput take a one percent dip to 10.2 million TEU."
  - p62 Port of Los Angeles annual container throughput decline, 2025 vs prior year (per = **1** as written "one percent", value check pending % (2025-01-01..2025-12-31) [DISCARD: Percentage restatement of the same secondary annual figure; duplicates the level-change information already implied by p] quote: "Los Angeles saw its container throughput take a one percent dip to 10.2 million TEU."
  - p63 Port of Los Angeles monthly container throughput, June 2025 = **892,340** TEU (2025-06-01..2025-06-30) [keep: ] quote: "While June saw the port record an eight percent increase in throughput to handle 892,340 TEUs and go down in history as one of the busiest months"
  - p64 Port of Los Angeles June 2025 throughput increase (percent) = **8** as written "eight percent", value check pending % (2025-06-01..2025-06-30) [DISCARD: Redundant derived percentage attached to p63; the level in p63 is retained.] quote: "While June saw the port record an eight percent increase in throughput to handle 892,340 TEUs"
  - p65 Port of Los Angeles monthly container throughput, December 2025 = **791,587** TEU (2025-12-01..2025-12-31) [keep: ] quote: "December was a rather bleak month, posting a 14 percent decline to 791,587 TEU."
  - p66 Port of Los Angeles December 2025 throughput decline (percent) = **14** % (2025-12-01..2025-12-31) [DISCARD: Redundant derived percentage attached to p65; the December 2025 level in p65 is retained.] quote: "December was a rather bleak month, posting a 14 percent decline to 791,587 TEU."
  - p67 Port of Los Angeles monthly container throughput, July 2025 = **1,000,000** as written "one million", value check pending TEU (2025-07-01..2025-07-31) [DISCARD: Rounded restatement ('one million TEUs') of the exact July 2025 value already in p2; less precise, no added information.] quote: "In July, for instance, Los Angeles recorded another busy month after handling one million TEUs"
  - p68 Port of Los Angeles July 2025 throughput increase vs July 2024 (percent) = **8.5** % (2025-07-01..2025-07-31) [keep: ] quote: "handling one million TEUs, 8.5 percent more than the same month in 2024"
  - p69 Port of Los Angeles consecutive years as top U.S. port = **26** years (2025-01-01..2025-12-31) [DISCARD: Ranking milestone (26 consecutive years as top US port), not a volume quantity and irrelevant to the September 2026 TEU ] quote: "Despite maintaining its position as the top U.S. port for the 26th consecutive year"
  - p70 Port of Los Angeles annual TEU threshold exceeded (only North American port) = **10,000,000** TEU (2025-01-01..2025-12-31) [DISCARD: Threshold statement ('only North American port to exceed 10 million TEU in a year') with no new numeric quantity beyond ] quote: "the only North American port to exceed 10 million TEU in a year"
  - p71 Port of Los Angeles cruise passengers handled, prior year (record) = **1,600,000** passengers (2025-01-01..2025-12-31) [DISCARD: Cruise passenger count; a different population (people, not containers) with no usable conversion to container throughpu] quote: "Having handled a record 1.6 million passengers and 241 cruise calls last year"
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### d8 [administrative] Customs and ocean-booking intermediary

Hypothesis: Advance manifest, ISF, booking, or port-community-system counts for containers moving through Los Angeles in September 2026 provide an early physical-flow count. Conversion from bookings or manifests to TEUs requires cancellation/no-show and empty-container adjustments; at the cutoff, only partial-month data may exist.

Queries issued by the searcher: Port of Los Angeles monthly cargo news release container throughput TEU; Port of Los Angeles weekly container volume September 2026; Whisk Logistics weekly drayage roundup September 10 2026 Port Optimizer forecast TEU; Port of Los Angeles August 2026 cargo volume TEUs news release September 2026

- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-03` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-11` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.whisklogistics.com/news/weekly-drayage-roundup-2026-09-24` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_100926_sept_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [forecasts_markets] d4

Hypothesis: The NRF/Hackett Global Port Tracker edition for September 2026 is normally published in the first ~10 days of the month and carries monthly US import forecasts plus LA/Long Beach commentary. Converting its LA/LB September 2026 import forecast to LA total TEU via the stable ~52% loaded-import share (p4/p1, p46/p50) would give an independent level anchor and show whether professional forecasters expected the July 2026 dip (p3) to persist — exactly the assumption (a1) carrying most of our uncertainty.

Queries issued by the searcher: NRF Hackett Associates Global Port Tracker September 2026 import forecast; "Global Port Tracker" 2026 container imports forecast Los Angeles Long Beach; Port of Los Angeles August 2026 cargo 955,907 TEU loaded imports 500,302; nrf.com press release "Import Cargo's Peak Season Not Over Yet" September 9 2026 Global Port Tracker Los Angeles/Long Beach

- `https://cdn.nrf.com/media-center/press-releases/import-cargo-s-peak-season-not-over-yet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.logisticsmgmt.com/article/august_volumes_cap_best_three_month_volume_run_on_record_for_the_port_of_los_angeles/Imports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portoflosangeles.org/references/2026-news-releases/news_090926_aug_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gcaptain.com/port-of-los-angeles-caps-record-summer-as-u-s-import-strength-holds-up/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [physical_flow] d2

Hypothesis: Scheduled Transpacific capacity calling San Pedro Bay in September 2026, net of announced blank sailings, is the physical exposure behind any September total. Comparing pro-forma September 2026 weekly capacity with the same weeks of September 2025 would reveal whether the July 2026 decline (p3) was service/blank-sailing driven (persistent) or demand noise (transitory), and would supply the missing bridge between scheduled calls and realised TEUs.

Queries issued by the searcher: Transpacific capacity September 2026 blank sailings Asia-USWC weekly capacity; Port of Los Angeles September 2026 cargo volumes TEUs; Sea-Intelligence Asia-North America West Coast weekly capacity September 2026 TEU blank sailings week 36 37 38 39; Port of Los Angeles August 2026 cargo 956,000 TEUs news release September 2026

- `https://portoflosangeles.org/references/2026-news-releases/news_100926_sept_cargo` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://blog.coleintl.com/tradenews/49-blank-sailings-expected-across-major-ocean-trade-routes-through-september` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chemanalyst.com/NewsAndDeals/NewsDetails/asia-us-container-rates-rise-as-panama-canal-cuts-44067` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mykn.kuehne-nagel.com/news/article/golden-week-schedules-push-capacity-across` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [administrative] d8

Hypothesis: Partial-month physical-flow gauges for 1-10 September 2026 (Port of LA Signal/Port Optimizer weekly volumes, Marine Exchange of Southern California container-ship arrivals, terminal gate-move notices) would set an early run-rate. Calibrated against the historical ratio of first-ten-day activity to full-month TEU, this would directly narrow the YoY factor a1 rather than leaving it to a judgemental blend of YTD growth and the July dip.

Queries issued by the searcher: Port of Los Angeles September 2026 container volume TEU; Port of LA Signal weekly TEU volumes August 2026; Marine Exchange of Southern California container ship arrivals September 2026 San Pedro Bay; "Port Optimizer" Signal weekly container volumes September 2026 Los Angeles

- `https://portalportuario.cl/ee-uu-puerto-de-los-angeles-logra-record-historico-mensual-en-manejo-de-carga/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://container-mag.com/update/port-of-los-angeles-caps-record-summer-with-955-907-teu-in-a-mtuo10fj` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/news/commodities-news/port-of-los-angeles-sets-september-volume-record-executive-director-says-4941593` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cargoxplorer.com/blog/2026-09-11-port-los-angeles-record-2-9m-teu-inland-velocity` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] Single release, one measurement: July 2026 total (960,464), July 2025 total (1,019,837) and the -5.82% YoY change are internally consistent restatements of the same table. They are not three independe
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p1'] July 2026 component rows (loaded imports, loaded exports, total loaded, total empty) sum arithmetically to the July 2026 total, and p8 supplies the July 2025 empty level. Same source and same table, s
- corroborating: ['p9', 'p10', 'p11'] Cumulative Jan-Jul 2026 (6,083,067) vs Jan-Jul 2025 (5,975,649) and the stated +1.80% agree; again one measurement restated three ways.
- related: ['p9', 'p11', 'p1', 'p3'] Not a contradiction but a material tension: a positive year-to-date change through July coexisting with a -5.82% July means the year ran stronger earlier and decelerated in the most recent month. This
- corroborating: ['p12', 'p13', 'p14', 'p60'] Annual series 2023-2025 from the same publisher; p60 is a duplicate of p12 from a different snapshot. Establishes the ~10.2-10.3M TEU annual scale used only as context and for share arithmetic.
- overlapping: ['p15', 'p16', 'p17', 'p18', 'p19'] All from the same October 2024 release. Q3 2024 is nested inside the January-September 2024 cumulative, so these are not independent; the September 2024 record is partly a tariff/port-strike front-loa
- corroborating: ['p20', 'p22', 'p24', 'p15'] September 2024 loaded imports, loaded exports and empties sum to the stated record total. Note the 2024 release reports only a combined empty figure, whereas 2025/2026 releases split empty imports and
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50'] September 2025 component rows sum to 883,053 TEUs. Critically, empty imports are only 276 TEUs: in this accounting 'empty' is almost entirely empty exports outward, so an empty-container split is unne
- related: ['p15', 'p50'] September 2025 was roughly 7.5% below September 2024, i.e. the base month for a 2026 YoY transfer is already depressed. A flat 2026 September would still be well below the 2024 record, which limits ho
- corroborating: ['p51', 'p52', 'p53'] August 2025 components and total from the same table are arithmetically consistent; August 2025 was a strong month relative to September 2025, showing a within-Q3 decline in 2025 that a September 2026
- corroborating: ['p54', 'p55', 'p56'] October 2025 components and total consistent; confirms the 2025 autumn downslope continued past September (context only, not used in a series method).
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] January and February 2026 component splits are internally consistent and, like September 2025, show near-zero empty imports and a stable ~52% loaded-import share of total. This stability is why a sing
- related: ['p45'] Fiscal-year-to-date cumulative covering Jul 2025-Feb 2026; different period definition from the target, kept only as context for the level and consistency of the accounting.
- related: ['p61', 'p62', 'p67', 'p68', 'p63', 'p64', 'p65', 'p66', 'p12', 'p2'] Secondary trade-press restatements derived from the port's own figures, with rounding ('one million TEUs' for 1,019,837; '10.2 million' for 10,239,318). They corroborate the port data at coarse precis
- related: ['p26', 'p27', 'p28', 'p29', 'p30'] Freight-rate market data, not volumes. Internally consistent (level 111% above a year earlier, -1% week on week, transpacific -1%). Role is scenario/context only: elevated and firming spot rates are c
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'] Single Port of Los Angeles July 2026/July 2025 release. p3 is the derived p1/p2 change; p4+p5 approximates p6; p6+p7 approximates p1; p7 vs p8 shows empties nearly flat. Internally consistent accounti
- corroborating: ['p9', 'p10', 'p11'] Year-to-date Jan-Jul 2026 and 2025 totals in the same release; p11 (+1.8%) is p9/p10. Same source as the monthly figures, so it corroborates the YTD trend but adds no independent measurement.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45'] Jan/Feb 2026 component rows sum to the monthly totals and to the cumulative total; the near-zero 'empty imports' column recurs in p48, so it is a consistent reporting convention, not a typo in one cel
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50'] September 2025 components sum to p50. This is the key base period for any September 2026 year-over-year route; loaded imports are ~52% of the total, empties ~35%.
- corroborating: ['p15', 'p16', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p17', 'p18', 'p19'] September 2024 record release; components p20+p22+p24 sum to p15. Shows September has repeatedly been a strong month (record 2024), which is why 2024-2025 September values, not an average of older yea
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p12'] Aug/Oct 2025 monthly components and 2025 annual totals; p60 and p12 are the same 2025 annual total. Implied annual empty imports are negligible, consistent with p32/p37/p48. Same publisher throughout.
- corroborating: ['p63', 'p65', 'p68', 'p67'] Secondary-source monthly context (June 2025 892k, Dec 2025 792k, July 2025 up 8.5% YoY, July 2025 'one million TEUs'). These restate the port's own numbers, so they are context and a plausibility chec
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30'] Freight-rate context as of late Aug 2026: WCI near $4,473/FEU, roughly flat week-on-week, still 111% above a year earlier. High spot rates with flat momentum are consistent with soft-but-not-collapsin
- conflicting: ['p1', 'p3', 'p11'] Tension within the kept evidence: YTD 2026 is +1.8% (p11) while July 2026 is -5.82% YoY (p3) with loaded imports -8.12%. Either the early-2026 strength is fading in H2, or July was noise/frontloading 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 vs September 2025 total TEU change factor, Port of Los Angeles | 0.98 | 0.88..1.09 | 0.876..1.095 (widened) | ratio | m4 (m4) | Anchored on kept evidence: YTD 2026 is +1.8% (p11) but July 2026 was -5.82% YoY (p3) with loaded imports -8.12% (p4 vs its 2025 row), implying the early-2026 strength is fading in H2 as frontloaded/tariff-driven volumes normalize. September 2025 (p50, 883,053) was itself a -7.5% month, so the base i | No definitional break in Port of Los Angeles TEU accounting (loaded + empty, imports + exports) and no port-wide disruption or new tariff shock between September 2025 and September 2026. | Evidence of sharply stronger September 2026 bookings/gate moves (e.g. a renewed pre-tariff pull-forward or sustained double-digit YoY gains in weekly volumes), or of major terminal disruption, labor action, or mass blank sailings that would push the outcome outside the stated range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_naive | 883,053 |  | [2025] | 0.078 | 0.25 | backtest |  |
| m2 | yoy_scaling | 831,644 |  | [] |  | 0.25 | median_of_backtested |  |
| m3 | formula_mc | 900,286 | ['p50', 'p11'] / [] | [] |  | 0.25 | median_of_backtested |  |
| m4 | formula_mc | 864,392 | ['p50'] / ['a1'] | [] |  | 0.25 | median_of_backtested |  |

- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **869,468** TEU, 80% interval [631,119, 1,197,834] TEU, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule inverse_backtest_error, weight on methods that use assumptions 0.25

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for Port of Los Angeles total container throughput (loaded and empty imports plus exports combined) in September 2026 is 869,468 TEU (80% model-based interval 631,119 to 1,197,834 TEU). The combination averages 4 methods at equal weights: 883,053 TEU (25%), 831,644 TEU (25%), 900,286 TEU (25%), and 864,392 TEU (25%). All four rest on the observed September 2025 base of 883,053 TEUs; m2 applies the July 2025-to-July 2026 change (1,019,837 TEUs to 960,464 TEUs), m3 carries the observed YTD growth of 1.8%, and m4 applies an assumed change factor of 0.98 (range 0.876 to 1.095). Only the historical points are observed; the September 2026 level is a transfer or assumption. The interval is conditional, not a demonstrated accuracy guarantee. The main risk is a September-specific shock, since July 2026 already fell year-over-year. Actual September 2026 data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 vs September 2025 total TEU change factor, Port of Los Angeles: 0.98 ratio, range 0.876 to 1.095 (range widened by code); used by m4. Overturned by: Evidence of sharply stronger September 2026 bookings/gate moves (e.g. a renewed pre-tariff pull-forward or sustained double-digit YoY gains in weekly volumes), or of major terminal disruption, labor action, or mass blank sailings that would push the outcome outside the stated range.

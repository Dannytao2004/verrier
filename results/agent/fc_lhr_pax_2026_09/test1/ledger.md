# Evidence ledger: fc_lhr_pax_2026_09

- Question: Assume today is 2026-09-12. You know nothing published after this date. Estimate the number of passengers at London Heathrow Airport in September 2026, as reported in Heathrow's monthly traffic statistics.
- as_of: 2026-09-12
- Pinned target: Total passengers at London Heathrow Airport (LHR) during September 2026, as reported in Heathrow's monthly traffic statistics. This is the sum of terminal and transit passengers (arrivals + departures) for the calendar month. | unit passengers (count of passenger movements, i.e., arrivals plus departures; transit passengers may be included depending on Heathrow's definition) | period 2026-09-01..2026-09-30 | publisher Heathrow Airport Holdings (monthly traffic statistics)

- Official value (scoring only, never shown to the agent): 7,180,000

## Directions and pages

### d1 [own_history] Heathrow Airport Holdings monthly traffic statistics

Hypothesis: September 2026 passengers can be estimated by applying the historical September-to-August ratio (or September-to-annual ratio) to the most recent available monthly figure (e.g., August 2026 or July 2026) and adjusting for year-over-year growth. The relationship is: P_Sep2026 = P_Aug2026 * (P_Sep_prev / P_Aug_prev) * (1 + growth adjustment).

Queries issued by the searcher: Heathrow monthly traffic statistics September 2025 passengers; Heathrow passenger numbers August 2026 monthly traffic report; Heathrow mediacentre August 2026 traffic statistics 7.87 million passengers; Heathrow September 2024 passengers 7.3 million busiest September

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/26027` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/10
  - p1 Heathrow total terminal passengers, September 2025 = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p2 Heathrow total terminal passengers, January to September 2025 cumulative = **63,275,000** passengers (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p3 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p4 Heathrow UK market terminal passengers, September 2025 = **383,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p5 Heathrow EU market terminal passengers, September 2025 = **2,599,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p6 Heathrow North America market terminal passengers, September 2025 = **1,859,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p7 Heathrow Asia / Pacific market terminal passengers, September 2025 = **904,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p8 Heathrow Middle East market terminal passengers, September 2025 = **702,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p9 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p10 Heathrow total cargo, September 2025 = **124,637** metric tonnes (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.travelwires.com/heathrow-handles-23-million-summer-passengers-as-more-than-40-airlines-seek-slots/` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- dropped by code checks: 5 (period_end missing or unparseable: 4; scale word 'billion' not supported by quote or table header: 1)

### d2 [related_series] UK Civil Aviation Authority (CAA) airport data

Hypothesis: CAA publishes monthly airport passenger data for UK airports, including Heathrow. The CAA figure for September 2026 may be available earlier or with a different definition. The relationship is: Heathrow monthly passengers from CAA = Heathrow monthly passengers from Heathrow report (approximately, after coverage adjustments).

Queries issued by the searcher: CAA airport data Heathrow monthly passengers 2025; UK Civil Aviation Authority Heathrow terminal passengers September monthly statistics; CAA "Table 09" monthly terminal and transit passengers Heathrow airport data 2025; CAA airport statistics September 2025 Heathrow passengers monthly record

- `https://www.caa.co.uk/Documents/Download/24003/a90c0dd7-e580-4607-b1d9-0b4fc72566fc/17360` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/2
  - p11 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Exact duplicate of p9 (September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p12 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Exact duplicate of p10 (September 2025 cargo).] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.caa.co.uk/media/hvmi0rb4/steer-h8-traffic-review-for-ips.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://apify.com/rainminer/airport-traffic-report-scraper` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (number: unknown scale word '000s': 11; period_end missing or unparseable: 2)

### d3 [capacity_consumption] Heathrow Airport slot coordination and airline schedules

Hypothesis: Passenger numbers are constrained by available seat capacity and load factors. September 2026 passengers = sum over flights of (seats per flight * load factor). Scheduled seats can be obtained from airline schedule data (e.g., OAG, Cirium) and load factors from historical averages or airline guidance. The relationship is: P = Σ (seats_i * LF_i).

Queries issued by the searcher: Heathrow monthly traffic statistics September 2025 passengers load factor; OAG Heathrow seat capacity 2026 schedule

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/12
  - p13 Heathrow total terminal passengers, September 2025 (monthly total, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1 (September 2025 total terminal passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p14 Heathrow total terminal passengers, January to September 2025 (cumulative, thous = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2 (Jan-Sep 2025 cumulative).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p15 Heathrow total terminal passengers, October 2024 to September 2025 (12-month rol = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3 (rolling 12 months).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p16 Heathrow total air transport movements, September 2025 (monthly total) = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p17 Heathrow total air transport movements, January to September 2025 (cumulative) = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p9's cumulative companion; no new information beyond p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p18 Heathrow total air transport movements, October 2024 to September 2025 (12-month = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p9's rolling companion; no new information beyond p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p19 Heathrow passengers, September 2025, described as busiest September ever (millio = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1; no independent measurement.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p20 Heathrow passengers, September 2025, CEO statement (millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance in punctuality and security"
  - p21 Heathrow UK market terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p4 (UK market September 2025).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p22 Heathrow EU market terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p5 (EU market September 2025).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p23 Heathrow North America market terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p6 (North America September 2025).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p24 Heathrow Asia / Pacific market terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7 (Asia/Pacific September 2025).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
- `https://www.thenationalnews.com/news/uk/2025/10/13/heathrow-records-bumper-september-despite-third-runway-row/` -> **snapshot** (snapshot 20251207122909); points raw/verified 14/1
  - p25 Heathrow passenger numbers increase between 2023 and 2024 = **4,700,000** passengers (2023-01-01..2024-12-31) [DISCARD: Redundant duplicate of p8 (same Middle East market September 2025 passengers).] quote: "Between 2023 and 2024, Heathrow's passenger numbers increased by 4.7 million, beating its pre-Covid record."
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://airport-world.com/traffic-continues-to-soar-at-london-heathrow/?utm_source=rss&utm_medium=rss&utm_campaign=traffic-continues-to-soar-at-london` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (period_end missing or unparseable: 14; scale word 'billion' not supported by quote or table header: 1; period_end 2029-12-31 after as_of: 1)

### d4 [physical_flow] Air traffic control and airport operations

Hypothesis: Passenger numbers can be estimated from aircraft movements and average passengers per movement. September 2026 passengers = (air transport movements) * (average passengers per movement). Movements data may be available from NATS or Heathrow's operational reports. The relationship is: P = ATM * avg_pax_per_ATM.

Queries issued by the searcher: Heathrow air transport movements September 2025 monthly traffic statistics; average passengers per flight Heathrow 2025; Heathrow 2026 passenger forecast air transport movements capacity 480,000 cap; CAA airport data Heathrow air transport movements September 2025 terminal passengers

- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/media/hvmi0rb4/steer-h8-traffic-review-for-ips.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.caa.co.uk/media/czmfoezz/airline-community-response-to-h8-ip_annex-skylark-report-passenger-forecasting-may-2026.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.caa.co.uk/Documents/Download/24003/a90c0dd7-e580-4607-b1d9-0b4fc72566fc/17355` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Airline and airport forecasts, industry outlooks

Hypothesis: Published forecasts for Heathrow passenger traffic in 2026 (e.g., from Heathrow's own guidance, IATA, ACI, or airline capacity plans) can provide a growth rate to apply to September 2025 actuals. The relationship is: P_Sep2026 = P_Sep2025 * (1 + forecasted annual growth rate).

Queries issued by the searcher: Heathrow 2026 passenger forecast guidance traffic outlook; IATA passenger growth forecast 2026 Europe; Heathrow September 2025 passenger traffic statistics million; Heathrow monthly traffic statistics 2026 passengers

- `https://www.flightglobal.com/strategy/2026/06/heathrow-airport-braced-for-drop-in-passenger-numbers-this-year/` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://centreforaviation.com/news/iata-air-passenger-demand-to-expand-in-2026-but-at-a-significantly-slower-pace-1362704` -> **snapshot** (snapshot 20260720043713); points raw/verified 10/0
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p26 Heathrow total terminal passengers, September 2025 (actual) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p27 Heathrow total terminal passengers, January to September 2025 (cumulative actual = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p28 Heathrow total terminal passengers, October 2024 to September 2025 (trailing 12  = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p29 Heathrow total terminal passengers, September 2025 year-on-year percentage chang = **0.8** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p30 Heathrow total terminal passengers, January to September 2025 year-on-year perce = **0.3** percent (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p31 Heathrow total terminal passengers, October 2024 to September 2025 year-on-year  = **1.5** percent (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p32 Heathrow passengers welcomed in September (narrative, busiest September ever) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p33 Heathrow passengers welcomed in September (CEO quote) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "welcoming nearly 7.4 million passengers in September alone"
  - p34 Heathrow total air transport movements, September 2025 (actual) = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p35 Heathrow total air transport movements, January to September 2025 (cumulative ac = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p9's cumulative companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p36 Heathrow total air transport movements, October 2024 to September 2025 (trailing = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p9's rolling companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p37 Heathrow total air transport movements, September 2025 year-on-year percentage c = **0.5** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p38 Heathrow total cargo, September 2025 (actual) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p39 Heathrow total cargo, January to September 2025 (cumulative actual) = **1,175,019** metric tonnes (2025-01-01..2025-09-30) [DISCARD: Duplicate of p10's cumulative companion.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p40 Heathrow total cargo, October 2024 to September 2025 (trailing 12 months actual) = **1,601,195** metric tonnes (2024-10-01..2025-09-30) [DISCARD: Duplicate of p10's rolling companion.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.businesstravelnewseurope.com/Air-Travel/London-Heathrow-traffic-set-to-fall-in-2026-as-demand-softens-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (period_end 2026-12-31 after as_of: 10)

### d6 [base_rates] Seasonal patterns and monthly shares

Hypothesis: September typically accounts for a stable share of annual passengers (e.g., around 8.5-9.0% for Heathrow). If a 2026 annual total is forecast or partially known, September can be estimated as annual_total * September_share. The relationship is: P_Sep = P_annual * share_Sep.

Queries issued by the searcher: Heathrow annual passengers 2025 monthly traffic statistics; Heathrow September 2025 passengers monthly traffic statistics; Heathrow 2026 annual passenger forecast; Heathrow passenger numbers 2024 annual total

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p41 Heathrow total terminal passengers, September 2025 (monthly total, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p42 Heathrow total terminal passengers, January to September 2025 cumulative (thousa = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p43 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p44 Heathrow passengers welcomed in September, stated as nearly 7.4 million (busiest = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p45 Heathrow passengers welcomed in September alone, stated as nearly 7.4 million = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance"
  - p46 Heathrow UK market terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p47 Heathrow EU market terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p5.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p48 Heathrow North America market terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p49 Heathrow Asia / Pacific market terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p50 Heathrow Middle East market terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p51 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p52 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p9's cumulative companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p53 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p54 Heathrow trade facilitated last year, stated as over £215 billion = **215,000,000,000** pounds sterling (trade value) (..) [DISCARD: Trade-value figure, irrelevant to passenger counts.] quote: "we helped drive over £215 billion in trade last year"
- `https://www.flightglobal.com/strategy/2026/06/heathrow-airport-braced-for-drop-in-passenger-numbers-this-year/` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.businesstravelnewseurope.com/Air-Travel/London-Heathrow-sets-passenger-record-of-84-5-million-for-2025` -> **snapshot** (snapshot 20260212001700); points raw/verified 15/15
  - p55 Heathrow annual passengers 2025 (record annual traffic) = **84,500,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "catered for 84.5 million passengers during 2025, despite its constrained capacity"
  - p56 Heathrow annual passengers 2024 (previous traffic record) = **83,900,000** passengers (2024-01-01..2024-12-31) [keep: ] quote: "only 0.7 per cent higher than the previous traffic record of 83.9 million, set in 2024"
  - p57 Heathrow December 2025 passengers (busiest-ever December) = **7,200,000** passengers (2025-12-01..2025-12-31) [keep: ] quote: "its busiest-ever December with traffic rising by 1.6 per cent year-on-year to reach 7.2 million passengers for the festive month"
  - p58 Heathrow annual flights 2025 (just under 480,000 services) = **480,000** flights/services (2025-01-01..2025-12-31) [keep: ] quote: "the number of flights only going up by 0.8 per cent year-on-year to just under 480,000 services in 2025"
  - p59 Heathrow busiest-ever day passengers (1 August) = **270,000** travellers (..) [DISCARD: Busiest-day passenger count is a single-day record, not a September 2026 monthly input; it cannot be scaled without an u] quote: "1 August was Heathrow's busiest-ever day with 270,000 travellers using the airport"
  - p60 Heathrow EU destinations passengers 2025 = **28,400,000** travellers (2025-01-01..2025-12-31) [keep: ] quote: "EU destinations again recorded the largest number of passengers to and from Heathrow in 2025 with 28.4 million travellers"
  - p61 Heathrow North America market passengers 2025 = **20,600,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "North America was the second biggest market with 20.6 million, which represented a dip of 0.3 per cent on 2024's traffic"
  - p62 Heathrow expansion proposal cost (government-backed) = **49,000,000,000** pounds sterling (..) [DISCARD: Expansion capital cost, irrelevant to September 2026 passenger volume.] quote: "the UK government has formally backed Heathrow's £49 billion expansion proposal"
  - p63 Heathrow annual passenger growth 2025 vs 2024 = **0.7** per cent (2025-01-01..2025-12-31) [keep: ] quote: "The UK hub airport's new milestone was only 0.7 per cent higher than the previous traffic record of 83.9 million"
  - p64 Heathrow annual flights growth 2025 year-on-year = **0.8** per cent (2025-01-01..2025-12-31) [keep: ] quote: "with the number of flights only going up by 0.8 per cent year-on-year"
  - p65 Heathrow December 2025 traffic growth year-on-year = **1.6** per cent (2025-12-01..2025-12-31) [keep: ] quote: "traffic rising by 1.6 per cent year-on-year to reach 7.2 million passengers"
  - p66 Heathrow EU destinations traffic growth 2025 year-on-year = **1.1** per cent (2025-01-01..2025-12-31) [keep: ] quote: "28.4 million travellers, up by 1.1 per cent on the previous year"
  - p67 Heathrow North America traffic change 2025 vs 2024 = **0.3** per cent (2025-01-01..2025-12-31) [keep: ] quote: "20.6 million, which represented a dip of 0.3 per cent on 2024's traffic"
  - p68 Heathrow domestic UK flights passenger decline 2025 year-on-year = **1.7** per cent (2025-01-01..2025-12-31) [DISCARD: Domestic UK passenger decline is a market-share detail already embedded in the total; not needed as a separate input.] quote: "there were declines in passenger numbers on domestic UK flights, down by 1.7 per cent year-on-year"
  - p69 Heathrow Latin America flights traffic decline 2025 year-on-year = **1.8** per cent (2025-01-01..2025-12-31) [DISCARD: Latin America decline is a market-share detail already embedded in the total; not needed as a separate input.] quote: "Traffic was also reduced by 1.8 per cent on flights to and from Latin America"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (scale word 'billion' not supported by quote or table header: 1)

### d7 [shocks] News and operational disruptions

Hypothesis: Any major disruptions (strikes, weather, airspace closures, pandemics, fuel shortages) in September 2026 would reduce passenger numbers relative to the seasonal baseline. The relationship is: P_Sep2026 = baseline * (1 - disruption_impact).

Queries issued by the searcher: Heathrow strike September 2026; UK air travel disruption September 2026; NATS technical failure 8 September 2026 flight cancellations Heathrow Reuters; Heathrow September 2026 monthly traffic statistics passengers

- `https://www.usnews.com/news/world/articles/2026-09-08/air-traffic-control-issue-disrupts-departing-flights-at-major-uk-airports` -> **snapshot** (snapshot 20260909070750); points raw/verified 15/10
  - p70 Flights cancelled to and from UK airports on Tuesday (NATS technical fault, per  = **1,300** flights (2026-09-08..2026-09-08) [DISCARD: UK-wide cancellation count includes airports other than Heathrow and is not a Heathrow passenger measure.] quote: "According to data from flight-tracking website Flightradar24, 1,300 flights to and from UK airports were cancelled on Tuesday."
  - p71 Flights cancelled for Wednesday, nearly all at Heathrow (per Flightradar24) = **177** flights (2026-09-09..2026-09-09) [DISCARD: Wednesday cancellations are a partial-day operational count; useful only as context for the disruption, not as a direct ] quote: "Another 177 flights had been cancelled for Wednesday, nearly all of them at Heathrow, the country's largest airport, it added."
  - p72 Departures delayed at six UK airports as of 1518 GMT (per FlightAware) = **490** departures (2026-09-08..2026-09-08) [DISCARD: Delayed departures at six UK airports are not Heathrow-specific passenger counts.] quote: "some 490 departures were delayed at six airports, including Heathrow, Gatwick, London City, Luton, Edinburgh and Bristol as of 1518 GMT"
  - p73 Arrivals cancelled or delayed at six UK airports as of 1518 GMT (per FlightAware = **525** arrivals (2026-09-08..2026-09-08) [DISCARD: Arrivals cancelled or delayed at six UK airports are not Heathrow-specific passenger counts.] quote: "Some 525 arrivals at those six airports were either cancelled or delayed, the website data showed."
  - p74 Heathrow scheduled arrivals cancelled or unable to operate (per Cirium) = **38** arrivals (2026-09-08..2026-09-08) [keep: ] quote: "At Heathrow, 38 of 661 scheduled arrivals had been cancelled or were unable to operate, according to aviation analytics company Cirium."
  - p75 Heathrow total scheduled arrivals on the day (per Cirium) = **661** arrivals (2026-09-08..2026-09-08) [keep: ] quote: "At Heathrow, 38 of 661 scheduled arrivals had been cancelled or were unable to operate, according to aviation analytics company Cirium."
  - p76 British Airways departures cancelled at Heathrow (per Cirium) = **16** departures (2026-09-08..2026-09-08) [DISCARD: British Airways cancelled departures are a carrier-specific operational detail; not needed for the aggregate passenger e] quote: "British Airways was the most affected carrier at the airport, cancelling 16 of 333 scheduled departures."
  - p77 British Airways total scheduled departures at Heathrow (per Cirium) = **333** departures (2026-09-08..2026-09-08) [DISCARD: British Airways scheduled departures are a carrier-specific operational detail; not needed for the aggregate passenger e] quote: "British Airways was the most affected carrier at the airport, cancelling 16 of 333 scheduled departures."
  - p78 Ryanair passengers affected by delays of up to eight hours = **150,000** passengers (2026-09-08..2026-09-08) [DISCARD: Ryanair passengers affected are not Heathrow passengers.] quote: "Ryanair said around 150,000 of its passengers had been affected by delays of up to eight hours"
  - p79 Ryanair flights cancelled due to NATS fault = **200** flights (2026-09-08..2026-09-08) [DISCARD: Ryanair cancelled flights are not Heathrow-specific.] quote: "it had cancelled more than 200 flights, and called on NATS Chief Executive Martin Rolfe to resign"
- `https://beta.rtbf.be/article/plus-de-2000-vols-annules-depuis-mardi-au-royaume-uni-trafic-toujours-perturbe-11782617` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.irishnews.com/news/uk/flight-delay-recovery-caused-by-technical-issue-will-take-some-time-nats-QT7KLJN5IJLOPK6IS64LDFXDMQ/` -> **snapshot** (snapshot 20260909021647); points raw/verified 15/14
  - p80 Flights cancelled to and from UK airports as of 5pm following air traffic contro = **425** flights (2026-09-08..2026-09-08) [DISCARD: UK-wide cancellation count is not a Heathrow passenger measure.] quote: "Some 425 flights were cancelled to and from UK airports as of 5pm following the issue, flight monitoring website Flightradar24 said."
  - p81 Share of UK flights cancelled or delayed due to air traffic control issue (Fligh = **4** % (2026-09-08..2026-09-08) [DISCARD: Share of UK flights cancelled or delayed is a UK-wide operational statistic, not a Heathrow passenger input.] quote: "approximately 4% of UK flights have been cancelled or delayed as a result of the issue."
  - p82 Heathrow flights delayed due to air traffic control issue = **352** flights (2026-09-08..2026-09-08) [keep: ] quote: "The air tracker found 352 flights to and from Heathrow were delayed out of its daily average of about 1,300."
  - p83 Heathrow daily average total flight operations = **1,300** flights (2026-09-08..2026-09-08) [keep: ] quote: "The air tracker found 352 flights to and from Heathrow were delayed out of its daily average of about 1,300."
  - p84 Gatwick flights delayed due to air traffic control issue = **281** flights (2026-09-08..2026-09-08) [DISCARD: Gatwick operational data are not Heathrow passenger data.] quote: "Meanwhile, 281 Gatwick flights were delayed out of its 850 total operations average."
  - p85 Gatwick daily average total flight operations = **850** flights (2026-09-08..2026-09-08) [DISCARD: Gatwick operational data are not Heathrow passenger data.] quote: "Meanwhile, 281 Gatwick flights were delayed out of its 850 total operations average."
  - p86 Manchester flights delayed due to air traffic control issue = **249** flights (2026-09-08..2026-09-08) [DISCARD: Manchester operational data are not Heathrow passenger data.] quote: "This was 249 out of 650 for Manchester, and 101 out of 300 for Birmingham."
  - p87 Manchester daily average total flight operations = **650** flights (2026-09-08..2026-09-08) [DISCARD: Manchester operational data are not Heathrow passenger data.] quote: "This was 249 out of 650 for Manchester, and 101 out of 300 for Birmingham."
  - p88 Birmingham flights delayed due to air traffic control issue = **101** flights (2026-09-08..2026-09-08) [DISCARD: Birmingham operational data are not Heathrow passenger data.] quote: "This was 249 out of 650 for Manchester, and 101 out of 300 for Birmingham."
  - p89 Birmingham daily average total flight operations = **300** flights (2026-09-08..2026-09-08) [DISCARD: Birmingham operational data are not Heathrow passenger data.] quote: "This was 249 out of 650 for Manchester, and 101 out of 300 for Birmingham."
  - p90 Ryanair passengers disrupted by air traffic control issue = **65,000** passengers (2026-09-08..2026-09-08) [DISCARD: Ryanair passengers disrupted are not Heathrow passengers.] quote: "Ryanair said more than 65,000 of its passengers had been disrupted as a result of the issue and it had cancelled more than 50 scheduled flights."
  - p91 Ryanair scheduled flights cancelled due to air traffic control issue = **50** flights (2026-09-08..2026-09-08) [DISCARD: Ryanair cancelled flights are not Heathrow-specific.] quote: "Ryanair said more than 65,000 of its passengers had been disrupted as a result of the issue and it had cancelled more than 50 scheduled flights."
  - p92 British Airways flights cancelled or diverted on Tuesday due to air traffic cont = **100** flights (2026-09-08..2026-09-08) [DISCARD: British Airways cancelled or diverted flights are a carrier-specific operational detail; not needed for the aggregate pa] quote: "British Airways said it was forced to cancel or divert more than 100 flights on Tuesday which had impacted "tens of thousands of customers"."
  - p93 Passengers disrupted in August 2023 Nats technical glitch (comparison event) = **700,000** passengers (2023-08-01..2023-08-31) [keep: ] quote: "In August 2023, more than 700,000 passengers experienced disruption when flights were grounded at UK airports when Nats suffered a technical glitch while processing a flight plan."
- `https://www.bernama.com/en/region/news.php?id=2604830` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (number: no number in value_as_written: 2; period_end missing or unparseable: 4)

### d8 [related_series] European airport comparables

Hypothesis: Heathrow's September 2026 growth may track that of comparable European hubs (e.g., Paris CDG, Frankfurt, Amsterdam). If those airports report September 2026 data earlier, their growth rates can inform Heathrow's. The relationship is: growth_Heathrow ≈ growth_comparable (adjusted for market differences).

Queries issued by the searcher: Heathrow airport monthly traffic statistics 2026 passengers; Frankfurt airport September 2026 passenger traffic; Amsterdam Schiphol September 2026 passengers traffic figures; Paris CDG airport September 2026 passenger traffic ADP

- `https://www.fraport.com/de/newsroom/pressemitteilungen/2026/verkehrszahlen/fraport---verkehrszahlen-im-september-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradearabia.com/News/467407/Dubai-retains-global-international-airport-crown-Atlanta-leads-overall-traffic/TTN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.schiphol.nl/nl/schiphol-als-buur/vooruitblik-vliegverkeer/` -> **snapshot** (snapshot 20260707123927); points raw/verified 11/9
  - p94 Schiphol forecast average flights per day, week 6-12 July 2026 = **1.4** flights per day (average) (2026-07-06..2026-07-12) [DISCARD: Schiphol flight forecast is a different airport and a different quantity; not usable as a Heathrow passenger input.] quote: "In de periode van 6 - 12 juli 2026 verwachten we gemiddeld zo'n 1.400 vluchten per dag op Schiphol."
  - p95 Schiphol forecast peak moments per day, week 6-12 July 2026 = **11** peak moments per day (2026-07-06..2026-07-12) [DISCARD: Schiphol peak moments are a different airport and quantity.] quote: "11 piekmomenten per dag verwacht"
  - p96 Schiphol actual average flights per day, 8-21 June 2026 = **1.365** flights per day (average) (2026-06-08..2026-06-21) [DISCARD: Schiphol actual flights are a different airport and quantity.] quote: "In de periode van 8 - 21 juni 2026 waren er gemiddeld 1.365 vluchten per dag op Schiphol."
  - p97 Schiphol expected average flights per day, 8-21 June 2026 = **1.366** flights per day (average) (2026-06-08..2026-06-21) [DISCARD: Schiphol expected flights are a different airport and quantity.] quote: "We hadden gemiddeld 1.366 vluchten verwacht."
  - p98 Kaagbaan share of runway use, 8-21 June 2026 = **33** % (2026-06-08..2026-06-21) [DISCARD: Schiphol runway share is irrelevant to Heathrow passenger volume.] quote: "De Kaagbaan (33%) en Polderbaan (29%) zijn de afgelopen periode het meest gebruikt."
  - p99 Polderbaan share of runway use, 8-21 June 2026 = **29** % (2026-06-08..2026-06-21) [DISCARD: Schiphol runway share is irrelevant to Heathrow passenger volume.] quote: "De Kaagbaan (33%) en Polderbaan (29%) zijn de afgelopen periode het meest gebruikt."
  - p100 Aalsmeerbaan share of runway use, 8-21 June 2026 = **15** % (2026-06-08..2026-06-21) [DISCARD: Schiphol runway share is irrelevant to Heathrow passenger volume.] quote: "De Aalsmeerbaan (15%), Zwanenburgbaan (13%) en Buitenveldertbaan (10%) zijn vooral gebruikt als tweede baan."
  - p101 Zwanenburgbaan share of runway use, 8-21 June 2026 = **13** % (2026-06-08..2026-06-21) [DISCARD: Schiphol runway share is irrelevant to Heathrow passenger volume.] quote: "De Aalsmeerbaan (15%), Zwanenburgbaan (13%) en Buitenveldertbaan (10%) zijn vooral gebruikt als tweede baan."
  - p102 Buitenveldertbaan share of runway use, 8-21 June 2026 = **10** % (2026-06-08..2026-06-21) [DISCARD: Schiphol runway share is irrelevant to Heathrow passenger volume.] quote: "De Aalsmeerbaan (15%), Zwanenburgbaan (13%) en Buitenveldertbaan (10%) zijn vooral gebruikt als tweede baan."
- `https://simpleflying.com/why-european-airport-quietly-became-busier-london-heathrow/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: no number in value_as_written: 2)

### b1 [own_history] Heathrow monthly traffic statistics

Hypothesis: A complete monthly series of Heathrow total terminal passengers for 2024 and 2025 (and any available 2026 months) would allow a proper seasonal ratio and trend estimate for September 2026. The current evidence has only September 2025 and annual totals, so the September-to-August ratio and recent monthly growth cannot be computed.

Queries issued by the searcher: Heathrow monthly traffic statistics August 2025 passengers; Heathrow monthly passenger totals September 2024 August 2024; Heathrow traffic statistics September 2025 passengers million; Heathrow monthly passenger statistics 2026 January February March

- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0
- `https://londonheathrowairportguide.com/statistics/` -> **snapshot** (snapshot 20250902010115); points raw/verified 0/0
- `https://mediacentre.heathrow.com/pressrelease/detail/23757` -> **snapshot** (snapshot 20251102201700); points raw/verified 15/15
  - p103 Heathrow total terminal passengers, August 2025 (monthly) = **8,036,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p104 Heathrow total terminal passengers, January to August 2025 (cumulative) = **55,927,000** terminal passengers (2025-01-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p105 Heathrow total terminal passengers, September 2024 to August 2025 (rolling 12 mo = **84,003,000** terminal passengers (2024-09-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p106 Heathrow UK market terminal passengers, August 2025 = **397,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| UK \| 397 \| -2.0 \| 3,000 \| -2.6 \| 4,585 \| 0.9 \|"
  - p107 Heathrow EU market terminal passengers, August 2025 = **2,844,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| EU \| 2,844 \| 1.8 \| 18,781 \| 0.3 \| 28,166 \| 2.2 \|"
  - p108 Heathrow Non-EU Europe market terminal passengers, August 2025 = **518,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Non-EU Europe \| 518 \| -1.2 \| 3,711 \| -2.8 \| 5,543 \| -1.3 \|"
  - p109 Heathrow Africa market terminal passengers, August 2025 = **296,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Africa \| 296 \| 4.9 \| 2,204 \| -0.3 \| 3,313 \| -2.8 \|"
  - p110 Heathrow North America market terminal passengers, August 2025 = **1,996,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| North America \| 1,996 \| -0.5 \| 13,713 \| -0.1 \| 20,618 \| 1.0 \|"
  - p111 Heathrow Latin America market terminal passengers, August 2025 = **174,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Latin America \| 174 \| -3.6 \| 1,457 \| 1.1 \| 2,217 \| 4.3 \|"
  - p112 Heathrow Middle East market terminal passengers, August 2025 = **833,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Middle East \| 833 \| 2.7 \| 5,717 \| 1.6 \| 8,636 \| 2.7 \|"
  - p113 Heathrow Asia / Pacific market terminal passengers, August 2025 = **977,000** terminal passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Asia / Pacific \| 977 \| 0.9 \| 7,344 \| 2.5 \| 10,925 \| 3.3 \|"
  - p114 Heathrow total air transport movements, August 2025 = **41,585** air transport movements (2025-08-01..2025-08-31) [keep: ] quote: "\| Total \| 41,585 \| 0.0 \| 317,825 \| 0.6 \| 475,733 \| 1.0 \|"
  - p115 Heathrow total air transport movements, January to August 2025 (cumulative) = **317,825** air transport movements (2025-01-01..2025-08-31) [keep: ] quote: "\| Total \| 41,585 \| 0.0 \| 317,825 \| 0.6 \| 475,733 \| 1.0 \|"
  - p116 Heathrow busiest ever day passengers, 1 August (over 270,000) = **270,000** passengers (2025-08-01..2025-08-01) [keep: ] quote: "we hit our busiest ever day on 1st August with over 270,000 passengers"
  - p117 Heathrow Terminal 5 single-day record passengers, 22 August (more than 112,000) = **112,000** travellers (2025-08-22..2025-08-22) [keep: ] quote: "Terminal 5 set a new single-day record on 22nd August - successfully welcoming more than 112,000 travellers"
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p118 Heathrow total terminal passengers, September 2025 (monthly traffic statistics) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p119 Heathrow total terminal passengers, January to September 2025 cumulative = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p120 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p121 Heathrow passengers welcomed in September (narrative, busiest September ever) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p122 Heathrow passengers welcomed in September alone (CEO quote) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance"
  - p123 Heathrow UK market terminal passengers, September 2025 = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p124 Heathrow EU market terminal passengers, September 2025 = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p5.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p125 Heathrow Non-EU Europe market terminal passengers, September 2025 = **459,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Non-EU Europe \| 459 \| -1.9 \| 4,170 \| -2.7 \| 5,535 \| -1.8 \|"
  - p126 Heathrow Africa market terminal passengers, September 2025 = **277,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Africa \| 277 \| 5.1 \| 2,481 \| 0.3 \| 3,326 \| -1.4 \|"
  - p127 Heathrow North America market terminal passengers, September 2025 = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p128 Heathrow Latin America market terminal passengers, September 2025 = **165,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Latin America \| 165 \| -3.8 \| 1,622 \| 0.6 \| 2,211 \| 3.7 \|"
  - p129 Heathrow Middle East market terminal passengers, September 2025 = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p130 Heathrow Asia / Pacific market terminal passengers, September 2025 = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p131 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p132 Heathrow total cargo, September 2025 = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"

### b2 [capacity_consumption] Airline schedule and seat capacity

Hypothesis: Scheduled seat capacity at Heathrow for September 2026, combined with a load factor, would provide an independent capacity-based estimate. The current evidence has no seat or load-factor data, so the capacity route cannot be executed.

Queries issued by the searcher: Heathrow Airport September 2025 monthly traffic statistics passengers; OAG Heathrow scheduled seats summer 2026; OAG world's busiest airports August 2026 Heathrow 4.26 million seats; Heathrow load factor 2025 passenger load factor percentage annual report

- `https://aviationexpress.news/news/dubai-airport-retains-title-as-worlds-busiest-for-international-travel` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/9
  - p133 Heathrow total terminal passengers, September 2025 (monthly total, thousands) = **7,348,000** passengers (terminal passengers, thousands) (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p134 Heathrow total terminal passengers, January to September 2025 (cumulative, thous = **63,275,000** passengers (terminal passengers, thousands) (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p135 Heathrow total terminal passengers, October 2024 to September 2025 (rolling 12 m = **84,065,000** passengers (terminal passengers, thousands) (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p136 Heathrow total air transport movements, September 2025 (monthly total) = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p137 Heathrow total air transport movements, January to September 2025 (cumulative) = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p9's cumulative companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p138 Heathrow total air transport movements, October 2024 to September 2025 (rolling  = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p9's rolling companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p139 Heathrow passengers per air transport movement, September 2025 (derived ratio of = **7,348,000** passengers (terminal passengers, thousands) (2025-09-01..2025-09-30) [DISCARD: Derived ratio mislabelled with passenger units; duplicates p1/p9 information.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p140 Heathrow passengers per air transport movement, January to September 2025 (deriv = **63,275,000** passengers (terminal passengers, thousands) (2025-01-01..2025-09-30) [DISCARD: Derived ratio mislabelled with passenger units; duplicates p2/p17 information.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p141 Heathrow passengers per air transport movement, October 2024 to September 2025 ( = **84,065,000** passengers (terminal passengers, thousands) (2024-10-01..2025-09-30) [DISCARD: Derived ratio mislabelled with passenger units; duplicates p3/p18 information.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://economymiddleeast.com/news/dubai-international-retains-worlds-busiest-international-airport-ranking-with-4-57-million-seats-ahead-of-heathrow/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end missing or unparseable: 5; scale word 'billion' not supported by quote or table header: 1)

### b3 [shocks] NATS disruption impact

Hypothesis: The 8 September 2026 NATS disruption is the largest known shock to September 2026 traffic. Quantifying the number of Heathrow passengers lost (cancelled or severely delayed flights times average passengers per flight) would allow a disruption adjustment to the seasonal baseline. The current evidence gives flight counts but not the passenger loss.

Queries issued by the searcher: Heathrow passengers September 2026 NATS disruption impact; 8 September 2026 NATS air traffic control fault flight cancellations Heathrow; Heathrow monthly traffic statistics September 2025 passengers record; Heathrow average passengers per flight 2025 load factor

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p142 Heathrow total terminal passengers, September 2025 (monthly traffic statistics) = **7,348,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p143 Heathrow total air transport movements, September 2025 (monthly traffic statisti = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p144 Heathrow passengers welcomed in September, described as busiest September ever ( = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p145 Heathrow passengers welcomed in September alone, CEO statement (nearly 7.4 milli = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative restatement of p1.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance"
  - p146 Heathrow total terminal passengers, January to September 2025 cumulative = **63,275,000** terminal passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p147 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** terminal passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p148 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p9's cumulative companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p149 Heathrow total air transport movements, October 2024 to September 2025 rolling 1 = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p9's rolling companion.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p150 Heathrow EU market terminal passengers, September 2025 = **2,599,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p5.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p151 Heathrow North America market terminal passengers, September 2025 = **1,859,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p152 Heathrow Asia / Pacific market terminal passengers, September 2025 = **904,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p153 Heathrow Middle East market terminal passengers, September 2025 = **702,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p154 Heathrow UK market terminal passengers, September 2025 = **383,000** terminal passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p155 Heathrow total cargo tonnage, September 2025 = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.usnews.com/news/world/articles/2026-09-08/air-traffic-control-issue-disrupts-departing-flights-at-major-uk-airports` -> **snapshot** (snapshot 20260909070750); points raw/verified 15/10
  - p156 Flights cancelled to and from UK airports on Tuesday 8 September 2026 (Flightrad = **1,300** flights (2026-09-08..2026-09-08) [DISCARD: Duplicate of p70 (UK-wide cancellations, 8 Sep 2026).] quote: "According to data from flight-tracking website Flightradar24, 1,300 flights to and from UK airports were cancelled on Tuesday."
  - p157 Flights cancelled for Wednesday 9 September 2026, nearly all at Heathrow (Flight = **177** flights (2026-09-09..2026-09-09) [DISCARD: Duplicate of p71 (Wednesday cancellations, nearly all Heathrow).] quote: "Another 177 flights had been cancelled for Wednesday, nearly all of them at Heathrow, the country's largest airport, it added."
  - p158 Departures delayed at six UK airports as of 1518 GMT on 8 September 2026 (Flight = **490** departures (2026-09-08..2026-09-08) [DISCARD: Duplicate of p72 (delayed departures, six UK airports).] quote: "data on flight-tracking platform FlightAware said some 490 departures were delayed at six airports, including Heathrow, Gatwick, London City, Luton, Edinburgh and Bristol as of 1518 GMT."
  - p159 Arrivals cancelled or delayed at six UK airports as of 1518 GMT on 8 September 2 = **525** arrivals (2026-09-08..2026-09-08) [DISCARD: Duplicate of p73 (cancelled/delayed arrivals, six UK airports).] quote: "Some 525 arrivals at those six airports were either cancelled or delayed, the website data showed."
  - p160 Heathrow scheduled arrivals cancelled or unable to operate on 8 September 2026 ( = **38** arrivals (2026-09-08..2026-09-08) [DISCARD: Duplicate of p74 (Heathrow arrivals cancelled, Cirium).] quote: "At Heathrow, 38 of 661 scheduled arrivals had been cancelled or were unable to operate, according to aviation analytics company Cirium."
  - p161 Heathrow total scheduled arrivals on 8 September 2026 (Cirium) = **661** scheduled arrivals (2026-09-08..2026-09-08) [DISCARD: Duplicate of p75 (Heathrow scheduled arrivals, Cirium).] quote: "At Heathrow, 38 of 661 scheduled arrivals had been cancelled or were unable to operate, according to aviation analytics company Cirium."
  - p162 British Airways scheduled departures cancelled at Heathrow on 8 September 2026 ( = **16** departures (2026-09-08..2026-09-08) [DISCARD: Duplicate of p76 (BA departures cancelled, Cirium).] quote: "British Airways was the most affected carrier at the airport, cancelling 16 of 333 scheduled departures."
  - p163 British Airways total scheduled departures at Heathrow on 8 September 2026 (Ciri = **333** scheduled departures (2026-09-08..2026-09-08) [DISCARD: Duplicate of p77 (BA scheduled departures, Cirium).] quote: "British Airways was the most affected carrier at the airport, cancelling 16 of 333 scheduled departures."
  - p164 Ryanair passengers affected by delays of up to eight hours on 8 September 2026 = **150,000** passengers (2026-09-08..2026-09-08) [DISCARD: Duplicate of p78 (Ryanair passengers affected).] quote: "Ryanair said around 150,000 of its passengers had been affected by delays of up to eight hours and that it had cancelled more than 200 flights"
  - p165 Ryanair flights cancelled on 8 September 2026 (more than) = **200** flights (2026-09-08..2026-09-08) [DISCARD: Duplicate of p79 (Ryanair flights cancelled).] quote: "Ryanair said around 150,000 of its passengers had been affected by delays of up to eight hours and that it had cancelled more than 200 flights"
- `https://www.bbc.co.uk/news/articles/ce8x3dp1zpxo` -> **snapshot** (snapshot 20260911151014); points raw/verified 12/0
- `https://beta.rtbf.be/article/plus-de-2000-vols-annules-depuis-mardi-au-royaume-uni-trafic-toujours-perturbe-11782617` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 18 (period_end missing or unparseable: 13; number: no number in value_as_written: 5)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['heathrow passengers', 'lhr traffic', 'september 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p13', 'p26', 'p41'] All report Heathrow total terminal passengers for September 2025 at 7,348,000; they are repeated extractions of the same monthly traffic-statistics table, not independent measurements.
- corroborating: ['p19', 'p20', 'p32', 'p33', 'p44', 'p45'] Narrative and CEO-quote statements that September 2025 was nearly 7.4 million passengers are rounded versions of the same Heathrow release as p1; they corroborate the level but add no independent meas
- corroborating: ['p2', 'p14', 'p27', 'p42'] Same January-September 2025 cumulative total of 63,275,000 passengers, repeated from the same Heathrow monthly release.
- corroborating: ['p3', 'p15', 'p28', 'p43'] Same October 2024-September 2025 rolling 12-month total of 84,065,000 passengers, repeated from the same Heathrow release.
- corroborating: ['p4', 'p21', 'p46'] Same September 2025 UK market terminal passengers, 383,000, repeated from the same Heathrow table.
- corroborating: ['p5', 'p22', 'p47'] Same September 2025 EU market terminal passengers, 2,599,000, repeated from the same Heathrow table.
- corroborating: ['p6', 'p23', 'p48'] Same September 2025 North America market terminal passengers, 1,859,000, repeated from the same Heathrow table.
- corroborating: ['p7', 'p24', 'p49'] Same September 2025 Asia/Pacific market terminal passengers, 904,000, repeated from the same Heathrow table.
- corroborating: ['p8', 'p25', 'p50'] Same September 2025 Middle East market terminal passengers, 702,000, repeated from the same Heathrow table.
- corroborating: ['p9', 'p11', 'p16', 'p34', 'p51'] Same September 2025 air transport movements, 40,193, repeated from the same Heathrow table.
- corroborating: ['p10', 'p12', 'p38', 'p53'] Same September 2025 cargo tonnage, 124,637 tonnes, repeated from the same Heathrow table.
- corroborating: ['p17', 'p35', 'p52'] Same January-September 2025 cumulative air transport movements, 358,018, repeated from the same Heathrow table.
- corroborating: ['p18', 'p36'] Same October 2024-September 2025 rolling 12-month air transport movements, 475,936, repeated from the same Heathrow table.
- corroborating: ['p29', 'p30', 'p31', 'p37'] Year-on-year percentage changes for September 2025, January-September 2025, rolling 12 months, and movements, all from the same Heathrow release; they are derived from the same table.
- corroborating: ['p55', 'p56', 'p63'] 2025 annual passengers of 84.5 million and 2024 annual passengers of 83.9 million imply 0.7% growth, matching p63; these are consistent annual totals from the same news report.
- corroborating: ['p57', 'p65'] December 2025 passengers of 7.2 million and 1.6% year-on-year growth are internally consistent within the same news report.
- corroborating: ['p58', 'p64'] 2025 flights just under 480,000 and 0.8% year-on-year growth are internally consistent within the same news report.
- corroborating: ['p60', 'p61', 'p66', 'p67'] 2025 EU and North America market totals and their growth rates are internally consistent within the same news report.
- corroborating: ['p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92'] All describe the same 8 September 2026 NATS air-traffic-control disruption; they are different cuts of the same event and should not be treated as independent estimates of September 2026 traffic.
- contextual: ['p93'] The August 2023 NATS glitch disrupted over 700,000 passengers; it is a useful analogue for the scale of the September 2026 disruption but is a different event and period.
- contextual: ['p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102'] Schiphol operational data for June-July 2026 show a comparable European hub operating near forecast, but they do not measure Heathrow passengers and cannot be directly substituted.
- contextual: ['p54', 'p59', 'p62'] Trade value, busiest-day passengers, and expansion cost are background facts about Heathrow; they do not measure September 2026 passenger volume.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p13', 'p26', 'p41', 'p118', 'p133', 'p142'] All are the same Heathrow monthly traffic-statistics figure for September 2025 total terminal passengers (7,348 thousand). They are repeated copies of one measurement, not independent confirmations.
- corroborating: ['p19', 'p20', 'p32', 'p33', 'p44', 'p45', 'p121', 'p122', 'p144', 'p145'] Narrative 'nearly 7.4 million' statements for September 2025 round the same 7,348 thousand figure upward; consistent with p1 but not an independent measurement.
- corroborating: ['p2', 'p14', 'p27', 'p42', 'p119', 'p134', 'p146'] Identical January-September 2025 cumulative total (63,275 thousand); one underlying statistic repeated.
- corroborating: ['p3', 'p15', 'p28', 'p43', 'p120', 'p135', 'p147'] Identical October 2024-September 2025 rolling-12-month total (84,065 thousand); one underlying statistic repeated.
- corroborating: ['p9', 'p11', 'p16', 'p34', 'p51', 'p131', 'p136', 'p143'] Identical September 2025 air transport movements (40,193); repeated copies of one measurement.
- corroborating: ['p10', 'p12', 'p38', 'p53', 'p132', 'p155'] Identical September 2025 cargo tonnage (124,637 t); repeated copies.
- corroborating: ['p4', 'p21', 'p46', 'p123', 'p154'] Identical September 2025 UK-market terminal passengers (383 thousand).
- corroborating: ['p5', 'p22', 'p47', 'p124', 'p150'] Identical September 2025 EU-market terminal passengers (2,599 thousand).
- corroborating: ['p6', 'p23', 'p48', 'p127', 'p151'] Identical September 2025 North America terminal passengers (1,859 thousand).
- corroborating: ['p7', 'p24', 'p49', 'p130', 'p152'] Identical September 2025 Asia/Pacific terminal passengers (904 thousand).
- corroborating: ['p8', 'p50', 'p129', 'p153'] Identical September 2025 Middle East terminal passengers (702 thousand).
- corroborating: ['p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117'] August 2025 Heathrow monthly statistics block from the same publisher; internally consistent with the September 2025 block and supplies the August denominator for a September/August seasonal ratio.
- corroborating: ['p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] 2025 annual and December 2025 Heathrow figures from a trade-news summary; consistent with the monthly-statistics series (84.5m 2025 vs 83.9m 2024, +0.7%) and useful for the 2026 growth prior.
- corroborating: ['p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165'] All describe the 8-9 September 2026 NATS technical fault. They are consistent in direction (a one-to-two-day disruption centred on Heathrow) but come from a small set of trackers (Flightradar24, Fligh
- corroborating: ['p74', 'p75', 'p76', 'p77', 'p160', 'p161', 'p162', 'p163'] Cirium-based Heathrow-specific counts for 8 September 2026: 38 of 661 scheduled arrivals cancelled/unable to operate, and BA 16 of 333 departures cancelled. These give the best Heathrow-specific disru
- conflicting: ['p70', 'p80', 'p156'] UK-wide cancellation counts for 8 September 2026 differ (1,300 vs 425) because they are snapshots at different times of day and cover different airport sets; they are not directly comparable and shoul
- conflicting: ['p78', 'p90', 'p164'] Ryanair passenger-disruption counts differ (150,000 vs 65,000) across sources/snapshots; both are Ryanair-wide, not Heathrow-specific, so neither transfers directly to Heathrow.
- corroborating: ['p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102'] Schiphol operational statistics for mid-2026; internally consistent but about a different airport, so they are contextual only for the d8 comparable-hub route.
- corroborating: ['p25', 'p55', 'p56'] Heathrow annual passenger growth narrative (2023-2024 +4.7m; 2024 83.9m; 2025 84.5m) is mutually consistent and anchors the low single-digit growth regime.
- corroborating: ['p139', 'p140', 'p141'] These are derived ratios (passengers per ATM) mislabelled with passenger units; they duplicate p1/p2/p3 and p9/p17/p18 and add no new information.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 vs September 2025 passenger growth factor | 1.01 | 0.97..1.05 | 0.9027..1.128 (widened) | ratio | m1 (m1), m4 (m4) | Heathrow is capacity-constrained and grew only 0.7% in 2025 (p63) with December 2025 up 1.6% (p65); a low single-digit 2026 growth factor is the central case, with the range wide enough to cover a flat or modestly negative outcome from the September 2026 NATS disruption. | Transfers to the target only if 2026 demand growth at Heathrow remains in the low single-digit regime seen in 2024-2025 and the September 2026 disruption is a one-to-two-day event rather than a sustained capacity cut. | Evidence of a large 2026 capacity increase or decrease at Heathrow, a sustained strike/closure, or published 2026 monthly growth far outside the low single digits. |
| a2 | September-to-August seasonal ratio for Heathrow total passengers | 0.914 | 0.88..0.95 | 0.6465..1.293 (widened) | ratio | m2 (m2) | September is a shoulder month below the August peak; the ratio is anchored on the kept September 2025 (p1) and August 2025 (p103) totals, with a range allowing for year-to-year shifts in the summer/shoulder boundary. | Transfers to 2026 only if the seasonal shape of Heathrow traffic is stable between 2025 and 2026 and August 2026 is a comparable peak month. | A materially different August-to-September pattern in 2026, e.g. a late-summer event that shifts traffic between the two months. |

Rejected by code:

- a3 Share of September 2026 passengers lost to the 8-9 September NATS disruption: value, low and high must be numbers

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,423,488 | ['p1'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 7,340,366 | ['p103'] / ['a2'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (value, low and high must be numbers) |
| m4 | formula_mc | 7,423,488 | ['p9', 'p1'] / ['a1'] | [] |  | 0.33 | equal |  |

Result: central **7,395,676**, 80% interval [4,989,648, 10,961,901], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for total passengers at London Heathrow Airport during September 2026, as reported in Heathrow's monthly traffic statistics, is 7,395,676 passenger movements (arrivals plus departures, calendar month). The supplied interval is 4,989,648 to 10,961,901, a model-based range conditional on the stated assumptions rather than a demonstrated accuracy guarantee.

Methods scaled the kept September 2025 total by a low-single-digit growth factor (1.01, range 0.9027 to 1.128), applied a September-to-August seasonal ratio (0.914, range 0.6465 to 1.293) to the kept August 2025 total, and checked movement/load-factor consistency. The observed inputs are historical totals; the growth and seasonal factors are assumptions. The combination weighted the usable methods equally, with one method rejected for invalid inputs.

The main risk is a structural break in 2026 demand or capacity, or a larger NATS disruption. Full September 2026 data, unavailable at cutoff, would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 vs September 2025 passenger growth factor: 1.01 ratio, range 0.9027 to 1.128 (range widened by code); used by m1, m4. Overturned by: Evidence of a large [n] capacity increase or decrease at Heathrow, a sustained strike/closure, or published [n] monthly growth far outside the low single digits.
- a2 September-to-August seasonal ratio for Heathrow total passengers: 0.914 ratio, range 0.6465 to 1.293 (range widened by code); used by m2. Overturned by: A materially different August-to-September pattern in 2026, e.g. a late-summer event that shifts traffic between the two months.

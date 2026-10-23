# Evidence ledger: fc_lhr_pax_2026_09

- Question: Assume today is 2026-09-12. You know nothing published after this date. Estimate the number of passengers at London Heathrow Airport in September 2026, as reported in Heathrow's monthly traffic statistics.
- as_of: 2026-09-12
- Pinned target: Total passengers passing through London Heathrow Airport (LHR) during the calendar month of September 2026, as reported in Heathrow's monthly traffic statistics (total terminal passengers, all domestic and international, arriving and departing, including transfers counted per Heathrow's standard met | unit passenger | period 2026-09-01..2026-09-30 | publisher Heathrow Airport Limited (monthly traffic statistics / operational figures)

- Official value (scoring only, never shown to the agent): 7,180,000

## Directions and pages

### d1 [own_history] Airport operator's published monthly traffic series

Hypothesis: September 2026 passengers ≈ September 2025 passengers scaled by recent year-on-year growth trend observed in months published before cutoff (Jan–Aug 2026 vs 2025). Own history gives the seasonal level and the growth rate to extrapolate.

Queries issued by the searcher: Heathrow monthly traffic statistics passengers September 2025; Heathrow airport passenger numbers 2025 monthly total; Heathrow traffic figures July 2026 passengers monthly; Heathrow mediacentre press release August 2026 passengers record

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p1 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p2 Heathrow total terminal passengers, September 2025 (narrative, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative duplicate of p1 (7.4m vs 7.348m); adds no information.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p3 Heathrow total terminal passengers, September 2025 year-on-year % change = **0.8** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p4 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p5 Heathrow total terminal passengers, Jan to Sep 2025 year-on-year % change = **0.3** % (2025-01-01..2025-09-30) [DISCARD: Jan–Sep 2025 cumulative YoY % — redundant with p4/p1 and not needed for any route.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p6 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p7 Heathrow total terminal passengers, Oct 2024 to Sep 2025 year-on-year % change = **1.5** % (2024-10-01..2025-09-30) [DISCARD: Rolling-12m YoY % — redundant with p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p8 Heathrow UK market terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p9 Heathrow EU market terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p10 Heathrow North America market terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p11 Heathrow Asia/Pacific market terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p12 Heathrow Middle East market terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p13 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p14 Heathrow total air transport movements, Jan to Sep 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p15 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Cargo tonnage — irrelevant to passenger target.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://safariindia.com/heathrow-records-busiest-day-of-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://centreforaviation.com/news/case-for-expansion-has-never-been-clearer-amid-jul-2026-pax-performance-at-london-heathrow-airport-1369277` -> **snapshot** (snapshot 20260813211834); points raw/verified 5/5
  - p16 Heathrow total passengers, July 2026 = **7,900,000** passengers (2026-07-01..2026-07-31) [keep: ] quote: "it handled 7.9 million passengers in Jul-2026, a decline of 1.5% year-on-year"
  - p17 Heathrow year-on-year passenger change, July 2026 = **1.5** % (2026-07-01..2026-07-31) [keep: ] quote: "a decline of 1.5% year-on-year"
  - p18 Heathrow passengers on busiest day of 2026, 19-Jul-2026 = **267,000** passengers (2026-07-19..2026-07-19) [DISCARD: Single-day peak passenger count — not a monthly level; no route uses it.] quote: "The airport recorded 267,000 passengers on 19-Jul-2026, its busiest day of 2026 thus far."
  - p19 Heathrow cargo handled on 12-Jul-2026 = **5,000** tonnes (2026-07-12..2026-07-12) [DISCARD: Single-day cargo — irrelevant.] quote: "handling 5000 tonnes on 12-Jul-2026"
  - p20 Passengers carried by Riyadh Air at Heathrow, July 2026 = **136,000** passengers (2026-07-01..2026-07-31) [DISCARD: One carrier's July 2026 passengers — too narrow, no route.] quote: "Riyadh Air - which carried more than 136,000 passengers in Jul-2026"
- `https://airport-world.com/record-breaking-year-for-londons-heathrow-airport/` -> **snapshot** (snapshot 20260616150125); points raw/verified 8/6
  - p21 Heathrow Airport total passengers, December 2025 (busiest ever December) = **7,200,000** passengers (2025-12-01..2025-12-31) [DISCARD: December 2025 passengers — different calendar month, not usable for September.] quote: "its busiest ever December when it handled 7.2 million passengers"
  - p22 Heathrow Airport total passengers, full year 2025 = **84,400,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "the monthly total bringing its yearly tally to 84.4 million"
  - p23 Heathrow Airport passengers on busiest day ever (August 1, 2025) = **270,000** passengers (2025-08-01..2025-08-01) [DISCARD: Single-day record — not a monthly level.] quote: "its busiest day ever on August 1, when passenger numbers surpassed 270,000"
  - p24 Number of months in 2025 in which Heathrow outperformed 2024 (out of twelve) = **9** as written "nine of twelve", value check pending months (2025-01-01..2025-12-31) [DISCARD: Count of outperforming months — no numerical role.] quote: "outperforming 2024 in nine of twelve months"
  - p25 Share of Heathrow passengers in December 2025 waiting less than five minutes for = **97** % (2025-12-01..2025-12-31) [DISCARD: Security wait share — irrelevant.] quote: "with over 97% of passengers waiting less than five minutes for security"
  - p26 Heathrow baggage load rate in 2025 = **98** % (2025-01-01..2025-12-31) [DISCARD: Baggage load rate — irrelevant.] quote: "baggage performance also improved to over 98% load rate in 2025"
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 1; period_end 2026-12-31 after as_of: 1)

### d2 [related_series] UK Civil Aviation Authority / ONS airport passenger data

Hypothesis: CAA monthly airport statistics for Heathrow provide an independent, consistent passenger series that can cross-check and fill Heathrow's own reported totals; September 2026 can be built from CAA 2025 September level times growth.

Queries issued by the searcher: CAA Heathrow airport monthly terminal passengers statistics 2025; Heathrow monthly traffic statistics September 2025 passengers; Heathrow passenger numbers July 2026 traffic statistics record; CAA airport data terminal passengers Heathrow 2026 monthly table 09

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p27 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p28 Heathrow total passengers, September 2025, stated in narrative (millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2/p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p29 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p30 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p31 Heathrow total terminal passengers year-on-year % change, September 2025 = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p32 Heathrow UK market terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p33 Heathrow EU market terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p34 Heathrow Non-EU Europe market terminal passengers, September 2025 (thousands) = **459,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p139.] quote: "\| Non-EU Europe \| 459 \| -1.9 \| 4,170 \| -2.7 \| 5,535 \| -1.8 \|"
  - p35 Heathrow Africa market terminal passengers, September 2025 (thousands) = **277,000** passengers (2025-09-01..2025-09-30) [DISCARD: Africa market Sept 2025 — no route uses it; redundant with total.] quote: "\| Africa \| 277 \| 5.1 \| 2,481 \| 0.3 \| 3,326 \| -1.4 \|"
  - p36 Heathrow North America market terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p37 Heathrow Latin America market terminal passengers, September 2025 (thousands) = **165,000** passengers (2025-09-01..2025-09-30) [DISCARD: Latin America market — no route uses it.] quote: "\| Latin America \| 165 \| -3.8 \| 1,622 \| 0.6 \| 2,211 \| 3.7 \|"
  - p38 Heathrow Middle East market terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p39 Heathrow Asia/Pacific market terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p40 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p41 Heathrow total air transport movements, Jan to Sep 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p14.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://mediacentre.heathrow.com/pressrelease/detail/26027` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/Documents/Download/24000/70cf208e-d8f7-4cab-8da0-ab741d4bad38/17225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/media/hvmi0rb4/steer-h8-traffic-review-for-ips.pdf` -> **snapshot** (snapshot 20260711081541); points raw/verified 15/8
  - p42 Heathrow passengers 12 months ending March 2025 (HAL traffic statistics) = **83,600,000** passengers (2024-04-01..2025-03-31) [DISCARD: 12m to March 2025 — different period, no route.] quote: "Heathrow served 83.6 million passengers in the 12 months ending March 2025 according to the traffic statistics published on the airport's website."
  - p43 Heathrow passengers 12 months rolling growth to September 2025 = **1.5** % (2024-10-01..2025-09-30) [DISCARD: Rolling growth % — redundant.] quote: "Latest September data show a +1.5% growth vs the previous 12 months (12 months rolling),"
  - p44 Heathrow annual passengers 2024 (HAL, 2024 versus 2023 KPI) = **83,900,000** passengers (2024-01-01..2024-12-31) [DISCARD: 2024 annual — superseded by 2025 annual points.] quote: "83.9m passengers +5.9%"
  - p45 Heathrow annual passengers 2025 (HAL P50 forecast) = **84,200,000** passengers (2025-01-01..2025-12-31) [DISCARD: 2025 forecast — superseded by actual 2025.] quote: "HAL's P50 Case starts at 84.2m passengers in 2025, an estimation based on latest actuals and schedules for the rest of the year, it then grows at 1.1% CAGR for H8."
  - p46 Heathrow annual passengers 2025 (Airlines Base forecast) = **84,900,000** passengers (2025-01-01..2025-12-31) [DISCARD: 2025 forecast — superseded by actual 2025.] quote: "This starts at 84.9m in 2025 which, based on latest schedule could potentially be an optimistic view (HAL BP forecasts 84.2), then grows to 88m in 2027 and to 91.4m in 2031 at 1.2% CAGR for H8."
  - p47 Heathrow annual PATMs 2024 (CAA Airport Statistics) = **471,280** passenger ATMs (2024-01-01..2024-12-31) [DISCARD: 2024 PATMs — no route.] quote: "In 2024 the airport served 471,280 PATMs, representing 99.6% of the pre-pandemic 2019 value."
  - p48 Heathrow passengers per PATM 2024 (CAA Airport Statistics) = **178** passengers per PATM (2024-01-01..2024-12-31) [DISCARD: 2024 pax/PATM — no route.] quote: "160 161 166 170 171 125 121 168 176 178"
  - p49 Heathrow annual load factor 2024 (approximate) = **80.7** % (2024-01-01..2024-12-31) [DISCARD: 2024 load factor — superseded by p67.] quote: "2024 approximate Load Factor: 80.7%"
- dropped by code checks: 7 (scale word 'million' not supported by quote or table header: 7)

### d3 [capacity_consumption] Airline schedules and seat capacity

Hypothesis: Passengers ≈ available seats × load factor × (1 + transfer share adjustment). September 2026 seat capacity at LHR from schedules (OAG/Cirium) times achieved load factor gives a bottom-up estimate.

Queries issued by the searcher: Heathrow airport monthly traffic statistics passengers 2025; Heathrow seat capacity 2026 OAG airline schedules seats; Heathrow September 2025 busiest ever month passengers 8 million; OAG busiest airports September 2026 seats Heathrow

- `https://aviationweek.com/air-transport/airports-networks/record-half-heathrow-driven-asia-pacific-growth` -> **snapshot** (snapshot 20260724232927); points raw/verified 15/13
  - p50 LHR total passengers, first half 2026 (record) = **40,000,000** passengers (2026-01-01..2026-06-30) [keep: ] quote: "handled a record 40 million passengers in the first half of 2026"
  - p51 LHR departing seats offered by airlines, first half 2026 (OAG Schedules Analyser = **25,300,000** departing seats (2026-01-01..2026-06-30) [keep: ] quote: "airlines offered about 25.3 million departing seats from LHR during the first six months of 2026"
  - p52 LHR departing seat capacity year-on-year change, first half 2026 = **1.4** % (2026-01-01..2026-06-30) [keep: ] quote: "down 1.4% year on year"
  - p53 LHR North American capacity, first half 2026 (departure seats) = **6,170,000** departure seats (2026-01-01..2026-06-30) [keep: ] quote: "North American capacity was broadly stable, declining 0.9% to about 6.17 million departure seats"
  - p54 LHR transfer traffic growth, first half 2026 = **5.4** % (2026-01-01..2026-06-30) [keep: ] quote: "with transfer traffic rising 5.4% amid weaker demand to and from the Middle East"
  - p55 LHR overall passenger numbers year-on-year change, first half 2026 = **0.2** % (2026-01-01..2026-06-30) [keep: ] quote: "Overall passenger numbers at the UK hub increased 0.2% from 39.9 million a year earlier"
  - p56 LHR Asia-Pacific traffic growth, first half 2026 = **7.9** % (2026-01-01..2026-06-30) [keep: ] quote: "Asia-Pacific traffic grew 7.9%, while North American volumes rose 1.6%"
  - p57 LHR North American volumes growth, first half 2026 = **1.6** % (2026-01-01..2026-06-30) [keep: ] quote: "Asia-Pacific traffic grew 7.9%, while North American volumes rose 1.6%"
  - p58 LHR scheduled Asia-Pacific capacity growth, first half 2026 = **6.7** % (2026-01-01..2026-06-30) [keep: ] quote: "Heathrow's scheduled Asia-Pacific capacity increased 6.7%"
  - p59 LHR-Middle East capacity change, first half 2026 = **16.5** % (2026-01-01..2026-06-30) [keep: ] quote: "Capacity between Heathrow and the Middle East fell 16.5%"
  - p60 LHR destinations served, first half 2026 = **223** destinations (2026-01-01..2026-06-30) [DISCARD: Destination count — no numerical role.] quote: "the number of destinations served increased from 218 to 223"
  - p61 LHR carrier count, first half 2026 = **83** carriers (2026-01-01..2026-06-30) [DISCARD: Carrier count — no numerical role.] quote: "the carrier count rose from 76 to 83"
  - p62 Heathrow average daily flights, week of July 13-19 (Eurocontrol) = **1,331** flights per day (2026-07-13..2026-07-19) [DISCARD: One-week daily flights — not a monthly level.] quote: "Heathrow ranked as the fourth-busiest airport with an average of 1,331 flights per day"
- `https://simpleflying.com/britain-busiest-airport-busier-record-breaking-year/` -> **snapshot** (snapshot 20260215014044); points raw/verified 15/11
  - p63 LHR total passengers handled, full-year 2025 = **84,463,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "London Heathrow Airport handled a grand total of 84.463 million passengers in 2025"
  - p64 LHR year-on-year passenger growth, full-year 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [DISCARD: 2025 growth % — redundant with p147.] quote: "representing an increase of 0.7% compared to the full-year figure that it posted in 2024"
  - p65 LHR available seats (Cirium scheduling data), full-year 2025 = **106,089,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p66 LHR passenger-carrying flights, full-year 2025 = **482,000** flights (2025-01-01..2025-12-31) [keep: ] quote: "almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p67 LHR mean load factor (passengers per available seat), full-year 2025 = **79.6** % (2025-01-01..2025-12-31) [keep: ] quote: "equating to a mean load factor of 79.6%"
  - p68 LHR passengers, December 2025 = **7,189,000** passengers (2025-12-01..2025-12-31) [DISCARD: December 2025 — different month.] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p69 LHR December 2025 passenger growth year-on-year = **1.6** % (2025-12-01..2025-12-31) [DISCARD: December 2025 growth — different month.] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p70 LHR record single-day passengers, August 1 2025 (lower bound) = **270,000** passengers (2025-08-01..2025-08-01) [DISCARD: Single-day record — not a monthly level.] quote: "with August 1 seeing a record-breaking total of more than 270,000 guests passing through its doors"
  - p71 LHR cargo handled, December 2025 = **138,000** tonnes (2025-12-01..2025-12-31) [DISCARD: Cargo — irrelevant.] quote: "with 138,000 tonnes handled in December alone"
  - p72 LHR annual passenger total threshold first exceeded, 2025 = **84,000,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "This saw its annual passenger total rise above the 84-million mark for the first time"
  - p73 LHR Middle East market passenger growth year-on-year, 2025 = **2.8** % (2025-01-01..2025-12-31) [DISCARD: 2025 Middle East growth — no route.] quote: "The biggest growth in terms of passenger numbers came in the Middle East market, where the total was up by 2.8% year-on-year"
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p74 Heathrow total terminal passengers, September 2025 (thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p75 Heathrow passengers welcomed in September (nearly, narrative) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p76 Heathrow total terminal passengers, Jan to Sep 2025 (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p77 Heathrow total terminal passengers, Oct 2024 to Sep 2025 (thousands) = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p78 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p79 Heathrow total air transport movements, Jan to Sep 2025 = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p14.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p80 Heathrow total air transport movements, Oct 2024 to Sep 2025 = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p14 rolling.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p81 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p82 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p83 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p84 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p85 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p86 Heathrow total terminal passengers year-on-year % change, September 2025 = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p87 Heathrow total air transport movements year-on-year % change, September 2025 = **0.5** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.caa.co.uk/media/czmfoezz/airline-community-response-to-h8-ip_annex-skylark-report-passenger-forecasting-may-2026.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- dropped by code checks: 7 (period year 2025 does not appear in the page text or URL (likely mis-dated): 2; period_end 2026-12-31 after as_of: 4; period_end missing or unparseable: 1)

### d4 [forecasts_markets] Airport guidance and industry forecasts

Hypothesis: Heathrow's own annual passenger guidance/traffic forecasts for 2026, and IATA/ACI Europe forecasts, constrain the annual total; September is a share of the year. Annual forecast × September seasonal share ≈ target.

Queries issued by the searcher: Heathrow 2026 passenger guidance forecast annual results; Heathrow monthly traffic statistics September passengers 2025; Heathrow traffic commentary July 2026 passengers million; ACI Europe 2026 passenger traffic forecast Europe growth percent

- `https://www.investegate.co.uk/announcement/rns/heathrow-funding-limited--44bi/june-2026-investor-report-/9638044` -> **snapshot** (snapshot 20260724141741); points raw/verified 15/6
  - p88 Heathrow passenger numbers first five months of 2026 (cumulative) = **32,800,000** passengers (2026-01-01..2026-05-31) [keep: ] quote: "In the 5 months to May 2026, passenger numbers reached 32.8 million, a 0.7% increase year on year"
  - p89 Heathrow passenger numbers first five months of 2026 year-on-year increase = **0.7** % (2026-01-01..2026-05-31) [keep: ] quote: "In the 5 months to May 2026, passenger numbers reached 32.8 million, a 0.7% increase year on year"
  - p90 Heathrow H7 period forecast capex = **4,700,000,000** GBP (not stated (page dated 2026-06-26)) [DISCARD: Capex — irrelevant.] quote: "We forecast capex for the H7 period to remain at £4.7 billion (£1,266 million for 2026)"
  - p91 Heathrow 2025 SAF uptake = **3.1** % (2025-01-01..2025-12-31) [DISCARD: SAF uptake — irrelevant.] quote: "strong progress on Sustainable Aviation Fuel ("SAF") saw uptake reach 3.1% in 2025 exceeding targets"
  - p92 Heathrow 2026 arrivals within 15 minutes of schedule (first 5 months) = **80.1** % (2026-01-01..2026-05-31) [DISCARD: Punctuality — irrelevant.] quote: "80.1% of arrivals and 81.6% of departures within 15 minutes of schedule (2025: 81.8% and 81.7%)"
  - p93 Heathrow 2026 departures within 15 minutes of schedule (first 5 months) = **81.6** % (2026-01-01..2026-05-31) [DISCARD: Punctuality — irrelevant.] quote: "80.1% of arrivals and 81.6% of departures within 15 minutes of schedule (2025: 81.8% and 81.7%)"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://safariindia.com/heathrow-records-busiest-day-of-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://traveltomorrow.com/istanbul-overtakes-heathrow-as-europes-busiest-airport-strengthening-case-for-third-runway/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (period_end 2026-12-31 after as_of: 9)

### d5 [capacity_consumption] Airport operational constraint (passenger cap / slot coordination)

Hypothesis: Heathrow's passenger cap and runway slot limits bound monthly throughput; if demand exceeds cap, September 2026 passengers approach the cap-implied monthly maximum. Cap × days × utilisation gives an upper bound.

Queries issued by the searcher: Heathrow passenger cap 82 million 2026; Heathrow runway slots daily movement limit passengers per movement; Heathrow September 2025 traffic statistics passengers 7.7 million; Heathrow monthly traffic statistics August 2026 passengers record

- `https://www.acl-uk.org/wp-content/uploads/2026/04/W26-Declaration-Appendices-RSL1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p94 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p95 Heathrow total passengers, September (narrative, nearly) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p96 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p97 Heathrow total terminal passengers, Jan to Sep 2025 (table, thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p98 Heathrow total terminal passengers, Oct 2024 to Sep 2025 trailing twelve months  = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p99 Heathrow total air transport movements, Jan to Sep 2025 = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p14.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p100 Heathrow total air transport movements, Oct 2024 to Sep 2025 trailing twelve mon = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p14 rolling.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p101 Heathrow UK (domestic) terminal passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p102 Heathrow EU terminal passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p103 Heathrow North America terminal passengers, September 2025 (table, thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p104 Heathrow Asia/Pacific terminal passengers, September 2025 (table, thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p105 Heathrow Middle East terminal passengers, September 2025 (table, thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p106 Heathrow total terminal passengers, September 2025 year-on-year % change = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p107 Heathrow total air transport movements, September 2025 year-on-year % change = **0.5** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.thisismoney.co.uk/money/markets/article-16043981/Heathrow-says-case-runway-never-clearer-loses-spot-Istanbul.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.heathrow.com/content/dam/heathrow/web/common/documents/company/about/economic-regulation/Heathrow-H8-Business-Plan-July25-website.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d6 [shocks] Disruption, strikes, and demand events affecting September 2026

Hypothesis: Known events before cutoff (strikes, ATC disruptions, weather, route launches/closures, economic conditions) shift September 2026 away from trend; quantify exposure to adjust the trend-based estimate.

Queries issued by the searcher: Heathrow strike September 2026; Heathrow new routes 2026 airline capacity autumn; NATS outage 8 September 2026 Heathrow flights cancelled passengers; PCS Border Force Heathrow strike September 2026 overtime ban 4 September

- `https://www.usnews.com/news/world/articles/2026-09-09/uk-flights-resume-but-airports-warn-of-ongoing-disruption-from-air-traffic-outage` -> **snapshot** (snapshot 20260910051347); points raw/verified 15/14
  - p108 Flights cancelled due to NATS outage (Tuesday-Wednesday combined) = **2,000** flights (2026-09-08..2026-09-09) [keep: ] quote: "which led to 2,000 cancellations and cost airlines millions of pounds"
  - p109 Flights to and from UK airports affected by outage (Cirium, Tuesday and Wednesda = **2,000** flights (2026-09-08..2026-09-09) [keep: ] quote: "Aviation analytics company Cirium confirmed about 2,000 flights to and from UK airports had been affected by the outage on Tuesday and Wednesday combined"
  - p110 Share of scheduled UK departures grounded on Tuesday (numerator: grounded depart = **30** % (2026-09-08..2026-09-08) [keep: ] quote: "with 30% of scheduled departures grounded on Tuesday and 5% on Wednesday"
  - p111 Share of scheduled UK departures grounded on Wednesday (numerator: grounded depa = **5** % (2026-09-09..2026-09-09) [keep: ] quote: "with 30% of scheduled departures grounded on Tuesday and 5% on Wednesday"
  - p112 Ryanair flights cancelled from Tuesday's outage = **260** flights (2026-09-08..2026-09-09) [keep: ] quote: "after it cancelled 260 flights affecting 48,000 passengers"
  - p113 Passengers affected by Ryanair cancellations from Tuesday's outage = **48,000** passengers (2026-09-08..2026-09-09) [keep: ] quote: "after it cancelled 260 flights affecting 48,000 passengers"
  - p114 Ryanair losses from Tuesday's outage so far = **3,000,000** GBP (2026-09-08..2026-09-09) [DISCARD: Ryanair loss figure — irrelevant to passenger count.] quote: "Ryanair said its losses from Tuesday's outage were £3 million ($4 million) so far"
  - p115 Ryanair losses from Tuesday's outage so far (USD equivalent) = **4,000,000** USD (2026-09-08..2026-09-09) [DISCARD: Ryanair loss USD — irrelevant.] quote: "Ryanair said its losses from Tuesday's outage were £3 million ($4 million) so far"
  - p116 British Airways flights cancelled or diverted on Tuesday = **100** flights (2026-09-08..2026-09-08) [keep: ] quote: "British Airways on Tuesday cancelled or diverted 100 flights with tens of thousands impacted"
  - p117 British Airways flights cancelled as of Wednesday = **190** flights (2026-09-09..2026-09-09) [keep: ] quote: "and said on Wednesday 190 flights had been cancelled"
  - p118 Cost to airlines of August 2023 NATS shutdown (GBP) = **100,000,000** GBP (2023-08-01..2023-08-31) [DISCARD: 2023 outage cost — irrelevant.] quote: "The last NATS shutdown in August 2023 caused travel chaos, costing airlines £100 million ($136 million)"
  - p119 Cost to airlines of August 2023 NATS shutdown (USD equivalent) = **136,000,000** USD (2023-08-01..2023-08-31) [DISCARD: 2023 outage cost USD — irrelevant.] quote: "costing airlines £100 million ($136 million)"
  - p120 NATS dividends paid to owners in 2025 = **175,000,000** GBP (2025-01-01..2025-12-31) [DISCARD: NATS dividends — irrelevant.] quote: "paid its owners £175 million in dividends in 2025"
  - p121 Ryanair lawsuit claim against NATS over 2023 outage = **7,000,000** GBP (2023-08-01..2023-08-31) [DISCARD: Ryanair lawsuit — irrelevant.] quote: "Ryanair is suing NATS in London's High Court for more than £7 million over the 2023 outage"
- `https://premium.kentonline.co.uk/news/national/passengers-affected-by-air-traffic-control-issue-unlikely-to-get-compensation-171492/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bbc.co.uk/news/articles/ce8x3dp1zpxo` -> **snapshot** (snapshot 20260911151014); points raw/verified 10/10
  - p122 Flights cancelled across airlines on Wednesday (second day of NATS disruption),  = **327** flights (not stated (page dated 2026-09-08)) [keep: ] quote: "airlines cancelled 327 flights, according to aviation analytics firm Cirium"
  - p123 Flights axed on Tuesday after NATS technical problem emerged = **1,750** flights (not stated (page dated 2026-09-08)) [keep: ] quote: "after 1,750 flights were axed on Tuesday after the problem emerged"
  - p124 Passengers affected by 2023 NATS computer shutdown over August bank holiday week = **700,000** passengers (2023-08-01..2023-08-31) [keep: ] quote: "In 2023, a computer shutdown over the August bank holiday weekend caused chaos for 700,000 passengers."
  - p125 Cancellations caused by smaller NATS outage in 2025 = **150** cancellations (2025-01-01..2025-12-31) [DISCARD: 2025 minor outage cancellations — not used.] quote: "There was another, smaller Nats outage in 2025, which caused 150 cancellations."
  - p126 Government stake in NATS (public-private partnership) = **49** % (not stated (page dated 2026-09-08)) [DISCARD: NATS ownership — irrelevant.] quote: "Downing Street said Nats - which is 49% owned by the government - must report back in one week"
  - p127 NATS CEO Martin Rolfe total pay for year ended 31 March = **1,400,000** GBP (2024-04-01..2025-03-31) [DISCARD: CEO pay — irrelevant.] quote: "Rolfe was paid £1.4m for the year ended 31 March, including a £343,000 bonus."
  - p128 NATS CEO Martin Rolfe bonus component for year ended 31 March = **343,000** GBP (2024-04-01..2025-03-31) [DISCARD: CEO bonus — irrelevant.] quote: "Rolfe was paid £1.4m for the year ended 31 March, including a £343,000 bonus."
  - p129 Years Martin Rolfe has led NATS = **11** years (not stated (page dated 2026-09-08)) [DISCARD: CEO tenure — irrelevant.] quote: "Martin Rolfe, who has led Nats for 11 years, met with Transport Secretary Heidi Alexander"
  - p130 Hours for engineer to reach work during 2023 NATS outage = **3** as written "three", value check pending hours (2023-08-01..2023-08-31) [DISCARD: Engineer travel time — irrelevant.] quote: "It took an engineer, who had been unable to correct the fault from home, three hours to get to work."
  - p131 Deadline in weeks for NATS to report on Tuesday incident = **1** as written "one week", value check pending weeks (not stated (page dated 2026-09-08)) [DISCARD: Report deadline — irrelevant.] quote: "must report back in one week detailing what went wrong during Tuesday's incident"
- `https://www.standard.co.uk/news/london/heathrow-flights-cancelled-latest-wednesday-gatwick-nats-b1295995.html` -> **snapshot** (snapshot 20260909195116); points raw/verified 15/0
- dropped by code checks: 16 (period_end 2026-09-16 after as_of: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 15)

### d7 [base_rates] Seasonal share decomposition

Hypothesis: September's share of annual passengers is stable across years; applying the historical September share to a 2026 annual estimate yields the monthly figure. Provides a cross-check on trend extrapolation.

Queries issued by the searcher: Heathrow annual passengers 2024 2025 traffic statistics; Heathrow monthly passenger numbers September 2023 2024; Heathrow business and traffic commentary September 2025 passengers; Heathrow monthly traffic statistics passengers by month 2019 2018 2017 table

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p132 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p133 Heathrow total terminal passengers, January to September 2025 cumulative (table, = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p134 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p135 Heathrow passengers in September (narrative, nearly, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever and rounding off a record-breaking summer."
  - p136 Heathrow passengers in September alone (CEO quote, nearly, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance in punctuality and security."
  - p137 Heathrow UK market terminal passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p138 Heathrow EU market terminal passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p139 Heathrow Non-EU Europe market terminal passengers, September 2025 (table, thousa = **459,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Non-EU Europe \| 459 \| -1.9 \| 4,170 \| -2.7 \| 5,535 \| -1.8 \|"
  - p140 Heathrow North America market terminal passengers, September 2025 (table, thousa = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p141 Heathrow Asia/Pacific market terminal passengers, September 2025 (table, thousan = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p142 Heathrow Middle East market terminal passengers, September 2025 (table, thousand = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p143 Heathrow total air transport movements, September 2025 (table) = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p144 Heathrow total air transport movements, January to September 2025 cumulative (ta = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p14.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p145 Heathrow total cargo, September 2025 (table, metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Cargo — irrelevant.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p146 Heathrow trade value last year (over, billions GBP) = **215,000,000,000** GBP (2024-01-01..2024-12-31) [DISCARD: Trade value — irrelevant.] quote: "As the UK's largest port by value, we helped drive over £215 billion in trade last year"
- `https://www.investegate.eu/announcement/rns/heathrow-finance-plc--80cx/business-and-traffic-commentary-sept-2024/8479491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://prod.gk.heathrow.com/content/dam/heathrow/web/common/documents/company/investor/reports-and-presentations/annual-accounts/finance/Heathrow_ARA` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://centreforaviation.com/news/london-heathrow-airport-handles-record-pax-in-dec-2025-and-full-year-2025-1344700` -> **snapshot** (snapshot 20260212045639); points raw/verified 7/7
  - p147 Heathrow annual passenger total, 2025 = **84,500,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "it handled 84.5 million passengers in 2025, an increase of 0.7% year-on-year"
  - p148 Heathrow annual passenger total, 2024 (prior annual record) = **83,900,000** passengers (2024-01-01..2024-12-31) [DISCARD: 2024 annual — superseded.] quote: "The airport exceeded its 2024 annual record of 83.9 million passengers"
  - p149 Heathrow monthly passenger total, December 2025 = **7,200,000** passengers (2025-12-01..2025-12-31) [DISCARD: December 2025 — different month.] quote: "The airport handled 7.2 million passengers in Dec-2025, an increase of 1.6% and its "busiest December on record""
  - p150 Heathrow annual passenger growth, 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [DISCARD: 2025 growth — redundant.] quote: "an increase of 0.7% year-on-year and the first time the airport has surpassed the 84 million passenger mark"
  - p151 Heathrow December 2025 passenger growth year-on-year = **1.6** % (2025-12-01..2025-12-31) [DISCARD: December growth — different month.] quote: "The airport handled 7.2 million passengers in Dec-2025, an increase of 1.6%"
  - p152 Heathrow annual passenger threshold first surpassed, 2025 (84 million mark) = **84,000,000** passengers (2025-01-01..2025-12-31) [DISCARD: Threshold — redundant with p72.] quote: "the first time the airport has surpassed the 84 million passenger mark"
  - p153 Heathrow monthly passenger threshold first surpassed, August 2025 (eight million = **8,000,000** as written "eight million", value check pending passengers (2025-08-01..2025-08-31) [DISCARD: August 2025 threshold — not used.] quote: "surpassed eight million passengers in August for the first time at any European airport"

### d8 [physical_flow] Air transport movements and average passengers per movement

Hypothesis: Passengers = air transport movements (ATMs) × average passengers per ATM. September 2026 ATMs from schedule/coordination data times recent pax-per-ATM gives an independent estimate.

Queries issued by the searcher: Heathrow air transport movements monthly 2025 statistics; Heathrow passengers per movement average 2025; Heathrow summer 2026 schedule seats capacity Cirium flights 2026; Heathrow September 2025 passengers 7.6 million traffic commentary

- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.enginecowl.com/qatar-air-france-slot-swap-lhr/` -> **snapshot** (snapshot 20260712061127); points raw/verified 8/1
  - p154 Qatar Airways weekly departures from DOH to LHR, July (summer 2026 season) = **66** weekly departures (2026-07-01..2026-07-31) [DISCARD: Qatar weekly departures — too narrow.] quote: "in July, for example, whenQatar Airways will have 66 weekly departures from the airport"
- `https://www.simpleflying.com/britain-busiest-airport-busier-record-breaking-year/` -> **snapshot** (snapshot 20260215014044); points raw/verified 15/11
  - p155 London Heathrow Airport total passengers, full year 2025 = **84,463,000** passengers (2025-01-01..2025-12-31) [DISCARD: Duplicate of p63.] quote: "All in all, London Heathrow Airport handled a grand total of 84.463 million passengers in 2025"
  - p156 London Heathrow Airport year-on-year passenger increase, full year 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p64.] quote: "representing an increase of 0.7% compared to the full-year figure that it posted in 2024"
  - p157 Seats available on flights to and from London Heathrow Airport, 2025 (Cirium sch = **106,089,000** seats (2025-01-01..2025-12-31) [DISCARD: Duplicate of p65.] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p158 Passenger-carrying flights to and from London Heathrow Airport, 2025 (Cirium sch = **482,000** flights (2025-01-01..2025-12-31) [DISCARD: Duplicate of p66.] quote: "almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p159 Mean load factor at London Heathrow Airport, 2025 = **79.6** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p67.] quote: "equating to a mean load factor of 79.6%"
  - p160 London Heathrow Airport passengers, December 2025 = **7,189,000** passengers (2025-12-01..2025-12-31) [DISCARD: Duplicate of p68.] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p161 London Heathrow Airport December 2025 passenger growth year-on-year = **1.6** % (2025-12-01..2025-12-31) [DISCARD: Duplicate of p69.] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p162 London Heathrow Airport record single-day passengers, August 1 2025 = **270,000** passengers (2025-08-01..2025-08-01) [DISCARD: Duplicate of p70.] quote: "with August 1 seeing a record-breaking total of more than 270,000 guests passing through its doors"
  - p163 London Heathrow Airport cargo handled, December 2025 = **138,000** tonnes (2025-12-01..2025-12-31) [DISCARD: Duplicate of p71.] quote: "with 138,000 tonnes handled in December alone"
  - p164 London Heathrow Airport annual passenger total threshold first exceeded, 2025 = **84,000,000** passengers (2025-01-01..2025-12-31) [DISCARD: Duplicate of p72.] quote: "This saw its annual passenger total rise above the 84-million mark for the first time"
  - p165 London Heathrow Airport Middle East market passenger growth year-on-year, 2025 = **2.8** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p73.] quote: "The biggest growth in terms of passenger numbers came in the Middle East market, where the total was up by 2.8% year-on-year"
- `https://www.mirror.co.uk/news/uk-news/flight-cuts-threaten-summer-holidays-37115516` -> **snapshot** (snapshot 20260510195402); points raw/verified 9/4
  - p166 Lufthansa short-haul flights cut by CityLine subsidiary = **20,000** short-haul flights (not stated (page dated 2026-05-06)) [DISCARD: Lufthansa CityLine cuts — irrelevant to LHR.] quote: "Lufthansa has cut 20,000 short-haul flights, operated by its CityLine subsidiary."
  - p167 Share of global oil traded passing through Strait of Hormuz = **20** % (not stated (page dated 2026-05-06)) [DISCARD: Hormuz oil share — irrelevant.] quote: "Iran retaliated by striking sites across the Middle East and closing the critical Strait of Hormuz trade route, through which 20% of global oil traded passes."
  - p168 Duration of US-Iran war at time of writing = **2** as written "two", value check pending months (not stated (page dated 2026-05-06)) [DISCARD: War duration — irrelevant.] quote: "Oil prices have soared since the start of the US-Iran war more than two months ago, when the US and Israel carried out joint strikes on several key Iranian sites."
  - p169 Usual visibility of jet fuel supply = **6** as written "six", value check pending weeks (not stated (page dated 2026-05-06)) [DISCARD: Jet fuel visibility — irrelevant.] quote: "The industry says it is not experiencing any current shortages, given the usual six weeks' visibility of supply, but international agencies have predicted that Europe faces shortages of jet fuel if th"
- dropped by code checks: 16 (period_end 2026-10-24 after as_of: 5; period_end missing or unparseable: 1; number: no number in value_as_written: 1; period_end 2026-12-31 after as_of: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 5)

### b1 [own_history] HAL monthly traffic release

Hypothesis: An August 2026 Heathrow monthly passenger figure (published ~early September 2026) would give the most recent YoY growth signal and let the September 2026 forecast anchor on Aug-2026 rather than July-2026, materially reducing trend uncertainty.

Queries issued by the searcher: Heathrow August 2026 traffic statistics passengers; Heathrow mediacentre monthly traffic statistics 2026; mediacentre.heathrow.com press release "August 2026" passenger numbers 7.9 million; Heathrow September 2025 passenger numbers traffic statistics million

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ebs.publicnow.com/view/CAA641AE0FF5E46CA12772ABC89A9B4BDCDBB33F` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://safariindia.com/heathrow-sees-strong-summer/` -> **snapshot** (snapshot 20260911133436); points raw/verified 15/15
  - p170 Heathrow total terminal passengers, August 2026 (table, thousands) = **7,867,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p171 Heathrow total terminal passengers YoY % change, August 2026 = **-2.1** % (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p172 Heathrow passengers in August 2026 (narrative, millions) = **7,800,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "with 7.8 million passengers travelling through the airport in August alone"
  - p173 Heathrow total passengers June–August 2026 (summer, millions) = **23,000,000** passengers (2026-06-01..2026-08-31) [keep: ] quote: "Heathrow recorded 23 million passengers between June and August 2026"
  - p174 Heathrow total terminal passengers, Jan–Aug 2026 cumulative (table, thousands) = **55,721,000** passengers (2026-01-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p175 Heathrow total terminal passengers YoY % change, Jan–Aug 2026 cumulative = **-0.4** % (2026-01-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p176 Heathrow total terminal passengers, Sep 2025–Aug 2026 rolling 12 months (table,  = **84,257,000** passengers (2025-09-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p177 Heathrow total terminal passengers YoY % change, Sep 2025–Aug 2026 rolling 12 mo = **0.3** % (2025-09-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p178 Heathrow UK market passengers, August 2026 (table, thousands) = **390,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| UK \| 390 \| -1.7 \| 3,008 \| 0.2 \| 4,596 \| 0.2 \|"
  - p179 Heathrow EU market passengers, August 2026 (table, thousands) = **2,835,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| EU \| 2,835 \| -0.3 \| 19,161 \| 2.0 \| 28,793 \| 2.2 \|"
  - p180 Heathrow North America market passengers, August 2026 (table, thousands) = **1,975,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| North America \| 1,975 \| -1.1 \| 13,783 \| 0.5 \| 20,626 \| 0.0 \|"
  - p181 Heathrow Middle East market passengers, August 2026 (table, thousands) = **668,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| Middle East \| 668 \| -19.8 \| 4,367 \| -23.6 \| 7,429 \| -14.0 \|"
  - p182 Heathrow Asia/Pacific market passengers, August 2026 (table, thousands) = **989,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| Asia / Pacific \| 989 \| 1.2 \| 7,826 \| 6.6 \| 11,505 \| 5.3 \|"
  - p183 Heathrow total air transport movements, August 2026 = **41,048** air transport movements (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p184 Heathrow busiest day passengers, 2 August 2026 (nearly) = **272,000** passengers (2026-08-02..2026-08-02) [keep: ] quote: "The airport also recorded its busiest day on 2 August, when nearly 272,000 passengers travelled through its terminals."
- `https://www.etravel.pl/en/news/1642/august-splits-europes-largest-airports` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [shocks] NATS outage impact

Hypothesis: Quantifying how many Heathrow passengers were actually disrupted by the 8–9 Sep 2026 NATS outage (cancelled LHR flights × pax per flight, plus rebooked/diverted) would let us subtract a concrete disruption loss from the trend estimate instead of an assumption.

Queries issued by the searcher: Heathrow NATS outage September 2026 cancelled flights; NATS air traffic control outage 8 September 2026 flight cancellations; Cirium Heathrow 209 flights cancelled Wednesday 9 September 2026; Heathrow "estimated" passengers affected Nats outage "Heathrow" cancelled flights number 8 September 2026

- `https://www.eluniversal.com.mx/mundo/sube-a-2-mil-los-vuelos-cancelados-por-un-problema-tecnico-en-reino-unido-descartan-ciberataque/` -> **snapshot** (snapshot 20260910182324); points raw/verified 13/0
- `https://top-channel.tv/2026/09/09/kaos-ne-fluturimet-britanike-afro-2100-anulime-ultimatum-shefit-te-kontrollit-te-trafikut-ajror-raporto-brenda-nje-j` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bbc.com/news/live/c6x2z0yy32ejt` -> **snapshot** (snapshot 20260911115605); points raw/verified 2/0
- `https://www.the-independent.com/travel/news-and-advice/uk-airport-delays-gatwick-heathrow-air-traffic-control-live-updates-b3047300.html` -> **snapshot** (snapshot 20260909162456); points raw/verified 15/3
  - p185 Normal daily share of flights affected (lower bound of normal range) = **1** as written "one", value check pending percent of flights (not stated (page dated 2026-09-09)) [keep: ] quote: "A normal day is between one and two per cent."
  - p186 Normal daily share of flights affected (upper bound of normal range) = **2** as written "two", value check pending percent of flights (not stated (page dated 2026-09-09)) [keep: ] quote: "A normal day is between one and two per cent."
  - p187 Number of major NATS system failures in three years (including this one) = **3** as written "third", value check pending failures (not stated (page dated 2026-09-09)) [keep: ] quote: "following the major disruption caused from Nats third major system failure in three years"
- dropped by code checks: 27 (period year 2026 does not appear in the page text or URL (likely mis-dated): 24; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; number: scale word 'mil' is not English or CJK (not supported): 2)

### b3 [capacity_consumption] Schedule data

Hypothesis: September 2026 LHR scheduled departing seats (OAG/Cirium) times achieved load factor would give an independent bottom-up estimate and cross-check the trend route.

Queries issued by the searcher: OAG Heathrow September 2026 seats capacity; Heathrow monthly traffic statistics load factor 2026; Heathrow August 2026 passengers traffic summary record; "Heathrow" load factor 2026 seats per aircraft OAG average

- `https://www.gdnonline.com/Details/1405057` -> **snapshot** (snapshot 20260902082941); points raw/verified 15/0
- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://economymiddleeast.com/news/dubai-international-retains-worlds-busiest-international-airport-ranking-with-4-57-million-seats-ahead-of-heathrow/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.oag.com/hubfs/Free_Reports/Heathrow%20Forecast%20/The%20Heathrow%20Forecast.pdf` -> **snapshot** (snapshot 20240810224950); points raw/verified 15/14
  - p188 Heathrow current annual movement limit (pre-third-runway cap) = **480,000** movements per annum (not stated (page dated 2018-08-01)) [keep: ] quote: "an increase of some 260,000 per annum on the current limit of 480,000"
  - p189 Heathrow forecast capacity after third runway (movements per annum) = **740,000** movements per annum (not stated (page dated 2018-08-01)) [keep: ] quote: "The new runway will increase capacity to some 740,000 movements which"
  - p190 Heathrow forecast passenger capacity after third runway (per annum) = **130,000,000** passengers per annum (not stated (page dated 2018-08-01)) [keep: ] quote: "Those additional movements will increase the airport's capacity to 130 million passengers per annum; an increase of 54 million."
  - p191 Assumed average passenger load factor for new domestic services to Heathrow = **75** % (not stated (page dated 2018-08-01)) [keep: ] quote: "Apply an average 75 percent passenger load factor to those services"
  - p192 Assumed average capacity per movement for new domestic services to Heathrow = **143** seats per movement (not stated (page dated 2018-08-01)) [keep: ] quote: "Assuming that on average, the capacity of these flights would be around 143 seats"
  - p193 Assumed load factor for potential new European inbound services to Heathrow = **92** % (not stated (page dated 2018-08-01)) [keep: ] quote: "Passengers At 92% Load Factor"
  - p194 Assumed load factor for potential long-haul leisure moves to Heathrow = **85** % (not stated (page dated 2018-08-01)) [keep: ] quote: "Yearly Capacity Assumed 85% Load Factor"
  - p195 Assumed year-round load factor for long-haul low-cost services from Heathrow = **90** % (not stated (page dated 2018-08-01)) [keep: ] quote: "Assuming a slightly higher and perhaps challenging 90 percent year-round load factor"
  - p196 Assumed seat configuration for long-haul low-cost services from Heathrow = **320** seats per aircraft (not stated (page dated 2018-08-01)) [keep: ] quote: "a higher density configuration of 320 seats"
  - p197 London Gatwick annual passengers (comparison airport scale) = **46,000,000** passengers per annum (not stated (page dated 2018-08-01)) [keep: ] quote: "valuable slots and market strength at an airport with 46 million passengers per annum?"
  - p198 Heathrow scheduled seats 2018 total for top 20 long-haul low-cost markets (sum) = **12,992,657** scheduled seats (2018-01-01..2018-12-31) [keep: ] quote: "Total 12,992,657 147 15,288 4,892,160 4,402,944"
  - p199 Heathrow scheduled seats 2018 to Los Angeles (largest long-haul low-cost market) = **1,170,759** scheduled seats (2018-01-01..2018-12-31) [keep: ] quote: "Los Angeles 1,170,759 7 728 232,960 209,664"
  - p200 Heathrow scheduled seats 2018 to New York = **1,112,783** scheduled seats (2018-01-01..2018-12-31) [keep: ] quote: "New York 1,112,783 14 1,456 465,920 419,328"
  - p201 Forecast total new passengers from all identified segments with third runway = **30,462,536** passengers (not stated (page dated 2018-08-01)) [keep: ] quote: "Total 140,556 30,462,536 54.1% 50.0%"
- dropped by code checks: 16 (period_end 2026-09-30 after as_of: 15; value_as_written not in quote as a whole number: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['heathrow passengers', 'lhr traffic', 'heathrow september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p27', 'p28', 'p74', 'p75', 'p94', 'p95', 'p132', 'p135', 'p136'] All describe Heathrow September 2025 total terminal passengers: table value 7,348 thousand and narrative 'nearly 7.4 million'. Same underlying HAL release, so not independent; the table figure is the 
- corroborating: ['p3', 'p31', 'p86', 'p106'] Same September 2025 YoY +0.8% from the same HAL table; identical source, not independent.
- corroborating: ['p4', 'p29', 'p76', 'p97', 'p133'] Same Jan–Sep 2025 cumulative 63,275 thousand from one HAL table.
- corroborating: ['p6', 'p30', 'p77', 'p98', 'p134'] Same Oct2024–Sep2025 rolling 12-month 84,065 thousand from one HAL table.
- corroborating: ['p13', 'p40', 'p78', 'p96', 'p143'] Same September 2025 ATM count 40,193 from one HAL table.
- corroborating: ['p8', 'p32', 'p85', 'p101', 'p137'] Same UK market September 2025 figure 383 thousand.
- corroborating: ['p9', 'p33', 'p81', 'p102', 'p138'] Same EU market September 2025 figure 2,599 thousand.
- corroborating: ['p10', 'p36', 'p82', 'p103', 'p140'] Same North America September 2025 figure 1,859 thousand.
- corroborating: ['p11', 'p39', 'p83', 'p104', 'p141'] Same Asia/Pacific September 2025 figure 904 thousand.
- corroborating: ['p12', 'p38', 'p84', 'p105', 'p142'] Same Middle East September 2025 figure 702 thousand.
- corroborating: ['p21', 'p68', 'p149', 'p160'] December 2025 ~7.19–7.2 million, busiest December; consistent across sources but likely shared HAL origin.
- corroborating: ['p22', 'p63', 'p147', 'p155'] Full-year 2025 total 84.4–84.5 million; consistent, shared HAL origin.
- corroborating: ['p23', 'p70', 'p162'] Record single day >270,000 on 1 Aug 2025; same fact restated.
- corroborating: ['p16', 'p17'] July 2026 7.9 million, down 1.5% YoY — the key recent growth signal before cutoff.
- corroborating: ['p50', 'p55', 'p88', 'p89'] H1 2026 record 40.0m (+0.2%) and 5M 2026 32.8m (+0.7%) are consistent with very slow 2026 growth; different periods but same direction.
- conflicting: ['p16', 'p50', 'p55', 'p88'] H1/5M 2026 showed slight growth (+0.2%/+0.7%) but July 2026 turned to −1.5% YoY. This is a genuine regime shift, not a definitional conflict; the September forecast must weight the more recent negativ
- corroborating: ['p108', 'p109', 'p110', 'p111', 'p122', 'p123'] NATS outage 8–9 Sep 2026: ~2,000 UK flights affected, 30% departures grounded Tuesday, 5% Wednesday, 1,750 axed Tuesday + 327 Wednesday. Same event, multiple restatements.
- corroborating: ['p112', 'p113', 'p116', 'p117'] Airline-level cancellation counts (Ryanair 260 flights/48,000 pax; BA 100 then 190 flights) are components of the same outage.
- corroborating: ['p124', 'p118', 'p119'] 2023 NATS shutdown analogue: 700,000 passengers affected, £100m cost — useful scale analogue for the September 2026 disruption.
- corroborating: ['p65', 'p157'] Same Cirium 2025 seat total 106.089 million.
- corroborating: ['p66', 'p158'] Same Cirium 2025 flight count ~482,000.
- corroborating: ['p67', 'p159'] Same 2025 mean load factor 79.6%.
- corroborating: ['p42', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49'] CAA/HAL annual and PATM statistics for 2024–2025; consistent with HAL totals and provide capacity/load-factor context.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p3', 'p4', 'p6'] Same Heathrow monthly traffic table (Sept 2025 snapshot): Sept 2025 total 7.348m, +0.8% YoY, Jan–Sep cumulative 63.275m, rolling 12m 84.065m. Internally consistent; one underlying measurement.
- corroborating: ['p22', 'p63', 'p147'] Three independent write-ups of Heathrow's 2025 annual total (84.4m, 84.463m, 84.5m) — same underlying HAL figure, rounding differences only.
- corroborating: ['p16', 'p17', 'p170', 'p171', 'p172', 'p174', 'p175', 'p176', 'p177'] 2026 monthly/cumulative traffic: July 7.9m (-1.5%), August 7.867m (-2.1%), Jan–Aug 55.721m (-0.4%), rolling 12m 84.257m (+0.3%). Consistent picture of a flat-to-slightly-negative 2026 with a weakening
- corroborating: ['p50', 'p55', 'p88', 'p89'] H1 2026 record 40.0m (+0.2%) and 5M 2026 32.8m (+0.7%) imply a decelerating year; consistent with the negative July/August prints.
- corroborating: ['p51', 'p52', 'p65', 'p67'] Capacity/load-factor evidence: H1 2026 departing seats 25.3m (-1.4%); 2025 full-year 106.089m seats at 79.6% load factor. Both point to capacity-constrained, high-load-factor operation.
- corroborating: ['p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p116', 'p117', 'p122', 'p123'] 8–9 Sep 2026 NATS outage: ~2,000 UK flights affected, 30% of Tuesday departures grounded, 5% Wednesday; BA and Ryanair cancellation counts. Same event, multiple reporters; gives the scale of a Septemb
- corroborating: ['p185', 'p186'] Normal daily share of flights affected is 1–2%, so the outage's 30%/5% grounding is a genuine but short-lived excess.
- corroborating: ['p188', 'p189', 'p190'] Heathrow movement cap 480,000/yr (pre-third-runway) and post-expansion 740k/130m pax — capacity context, not a September level.
- corroborating: ['p191', 'p192', 'p193', 'p194', 'p195', 'p196'] 2018 OAG load-factor/seat assumptions for hypothetical new routes — generic planning parameters, not LHR realised values.
- corroborating: ['p198', 'p199', 'p200', 'p201'] 2018 OAG long-haul low-cost seat tables and third-runway segment forecast — historical planning context only.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth factor vs September 2025 | 0.985 | 0.95..1.02 | 0.8805..1.101 (widened) | ratio | m1 (m1), m2 (m2) | Anchored on kept 2026 evidence: Jan–Aug cumulative -0.4% (p175), July -1.5% (p17), August -2.1% (p171), H1 +0.2% (p55). The trend decelerates into late summer, so September sits slightly below flat; range spans mild recovery to continued decline. | September 2026 behaves like the recent Jul–Aug 2026 run-rate rather than reverting to H1 strength. | A September 2026 print showing growth clearly above +2% or below -5% YoY. |
| a2 | Net share of September 2026 passengers lost to the 8–9 Sep NATS outage | 0.01 | 0.003..0.025 | 0.003..0.025 | ratio | m2 (m2) | Outage grounded 30% of Tuesday and 5% of Wednesday UK departures (p110, p111) against a normal 1–2% (p185, p186); ~2,000 UK flights affected (p109). LHR's share of that, net of rebooking and the fact that most cancelled passengers travel later in the month, is a small fraction of a ~7.3m monthly tot | The outage's LHR-specific cancellations are not fully recovered within September. | Evidence that LHR cancellations exceeded ~5% of monthly flights or that rebooking was negligible. |
| a3 | September share of annual passengers, 2026 capacity/growth adjusted | 0.087 | 0.08..0.094 | 0.07756..0.09695 (widened) | ratio | m3 (m3) | September is a shoulder month: 7.348m of 84.4m in 2025 ≈ 8.7%. Applied to a 2026 annual level near 84.3m (rolling 12m p176) with a small downward adjustment for the negative summer trend. | September's seasonal share of the year is stable at its 2025 value. | A September share materially outside the 8–9.5% band seen in recent years. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,240,847 | ['p1'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 7,155,553 | ['p1'] / ['a1', 'a2'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 609,608 | ['p63'] / ['a3'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **3,161,023** person, 80% interval [711,370, 14,046,235] person, basis method_spread (interval width set from the disagreement between the methods' estimates), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total terminal passengers at London Heathrow Airport (all domestic and international, arriving and departing, transfers per Heathrow's convention) during September 2026: 3,161,023 person (80% model-based interval 711,370 to 14,046,235 person).

Evidence: the observed September 2025 level was 7,348,000 passengers, and full-year 2025 was 84,463,000 passengers. Two trend methods scale the September 2025 figure by a growth factor of 0.985 (range 0.8805 to 1.101), anchored on kept 2026 prints; one applies an outage haircut of 0.01 (range 0.003 to 0.025). The third multiplies the annual total by a September share of 0.087 (range 0.07756 to 0.09695).

Only the two observed points are data; the growth, outage and seasonal-share inputs are analyst assumptions. The methods were weighted equally (33%, 33%, 33%); the first two share inputs, so they are not independent. The interval reflects method disagreement, not demonstrated accuracy. The biggest risk is the annual-share method's scale error and the uncertain 2026 growth path. Actual September 2026 traffic data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth factor vs September 2025: 0.985 ratio, range 0.8805 to 1.101 (range widened by code); used by m1, m2. Overturned by: A September 2026 print showing growth clearly above +[n] or below -[n] YoY.
- a2 Net share of September 2026 passengers lost to the [n]–[n] Sep NATS outage: 0.01 ratio, range 0.003 to 0.025; used by m2. Overturned by: Evidence that LHR cancellations exceeded ~[n] of monthly flights or that rebooking was negligible.
- a3 September share of annual passengers, 2026 capacity/growth adjusted: 0.087 ratio, range 0.07756 to 0.09695 (range widened by code); used by m3. Overturned by: A September share materially outside the [n]–[n] band seen in recent years.

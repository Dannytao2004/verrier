# Evidence ledger: fc_lhr_pax_2026_09

- Question: Assume today is 2026-09-12. You know nothing published after this date. Estimate the number of passengers at London Heathrow Airport in September 2026, as reported in Heathrow's monthly traffic statistics.
- as_of: 2026-09-12
- Pinned target: Total passengers passing through London Heathrow Airport (LHR) during the calendar month of September 2026, as reported in Heathrow's monthly traffic statistics (terminal and transit passengers counted per airport traffic convention) | unit passengers | period 2026-09-01..2026-09-30 | publisher Heathrow Airport Limited (monthly traffic statistics / operational figures)

- Official value (scoring only, never shown to the agent): 7,180,000

## Directions and pages

### d1 [own_history] Airport operator reporting

Hypothesis: September 2026 passengers ≈ September 2025 actual scaled by recent year-on-year growth trend observed in months published before cutoff (Jan–Jul 2026). September is a peak summer-shoulder month with stable seasonal shape.

Queries issued by the searcher: Heathrow monthly traffic statistics September 2025 passengers; Heathrow airport passenger numbers July 2026 year on year; Heathrow August 2026 passengers monthly traffic figures; Heathrow September 2023 passengers 7.0 million traffic statistics

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p1 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p2 Heathrow total passengers, September 2025, stated in narrative (millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant narrative restatement of p1 (7.4m vs 7.348m); p1 is the precise table value.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p3 Heathrow total terminal passengers YoY % change, September 2025 = **0.8** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p4 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p5 Heathrow total terminal passengers YoY % change, Jan to Sep 2025 = **0.3** % (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p6 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p7 Heathrow total terminal passengers YoY % change, Oct 2024 to Sep 2025 = **1.5** % (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p8 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p9 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p10 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p11 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p12 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p13 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p14 Heathrow total air transport movements YoY % change, September 2025 = **0.5** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://safariindia.com/heathrow-records-busiest-day-of-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d2 [capacity_consumption] Airline schedule / seat capacity

Hypothesis: Passengers = seat capacity offered at LHR in September 2026 × load factor × (1 − transit share). Schedule data (OAG/Cirium) gives seats; load factors ~80-85%; transit small.

Queries issued by the searcher: Heathrow airport departing seat capacity 2025 monthly passengers load factor; Heathrow monthly traffic statistics September 2025 passengers; ACL Heathrow summer 2026 slot coordination seats capacity report; Heathrow monthly traffic statistics transit passengers definition terminal passengers

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p15 Heathrow total terminal passengers, September 2025 (monthly traffic statistics) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1 (same September 2025 table value).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p16 Heathrow passengers welcomed in September (narrative, 'nearly 7.4 million') = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Narrative 'nearly 7.4 million' duplicate of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p17 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13 (September 2025 ATMs).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p18 Heathrow total terminal passengers, Jan to Sep 2025 cumulative = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4 (Jan–Sep 2025 cumulative).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p19 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6 (rolling 12-month total).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p20 Heathrow total air transport movements, Oct 2024 to Sep 2025 rolling 12 months = **475,936** air transport movements (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p21 Heathrow EU terminal passengers, September 2025 = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8 (EU September 2025).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p22 Heathrow North America terminal passengers, September 2025 = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9 (North America September 2025).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p23 Heathrow Asia/Pacific terminal passengers, September 2025 = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10 (Asia/Pacific September 2025).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p24 Heathrow Middle East terminal passengers, September 2025 = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11 (Middle East September 2025).] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p25 Heathrow UK terminal passengers, September 2025 = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12 (UK September 2025).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p26 Heathrow Non-EU Europe terminal passengers, September 2025 = **459,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Non-EU Europe \| 459 \| -1.9 \| 4,170 \| -2.7 \| 5,535 \| -1.8 \|"
  - p27 Heathrow Africa terminal passengers, September 2025 = **277,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Africa \| 277 \| 5.1 \| 2,481 \| 0.3 \| 3,326 \| -1.4 \|"
  - p28 Heathrow Latin America terminal passengers, September 2025 = **165,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Latin America \| 165 \| -3.8 \| 1,622 \| 0.6 \| 2,211 \| 3.7 \|"
- `https://www.enginecowl.com/qatar-air-france-slot-swap-lhr/` -> **snapshot** (snapshot 20260712061127); points raw/verified 11/4
  - p29 Qatar Airways weekly departures from DOH to LHR, July (current schedules) = **66** weekly departures (2026-07-01..2026-07-31) [DISCARD: Qatar Airways weekly departures — irrelevant to total Heathrow monthly passengers.] quote: "in July, for example, whenQatar Airways will have 66 weekly departures from the airport"
  - p30 Qatar Airways rank at LHR by weekly flights, July = **11** rank (2026-07-01..2026-07-31) [DISCARD: Airline rank at LHR — irrelevant to total passenger count.] quote: "the Qatari carrier will be the 11th busiest airline at the airport in terms of weekly flights"
  - p31 Qatar Airways rank at LHR by weekly departing seats, July = **6** as written "sixth", value check pending rank (2026-07-01..2026-07-31) [DISCARD: Airline rank by seats — irrelevant to total passenger count.] quote: "and the sixth in terms of weekly departing seats"
  - p32 ACL slot alleviation period beyond disturbance (weeks) = **6** as written "six weeks", value check pending weeks (not stated (page dated 2026-03-23)) [DISCARD: Slot alleviation period — irrelevant to September 2026 passenger level.] quote: "ACL will grant alleviation for the period of the disturbance plus six weeks"
- `https://simpleflying.com/britain-busiest-airport-busier-record-breaking-year/` -> **snapshot** (snapshot 20260215014044); points raw/verified 14/9
  - p33 LHR total passengers handled, full year 2025 = **84,463,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "London Heathrow Airport handled a grand total of 84.463 million passengers in 2025"
  - p34 LHR year-on-year passenger increase, full year 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "representing an increase of 0.7% compared to the full-year figure that it posted in 2024"
  - p35 LHR seats available (Cirium schedule data), full year 2025 = **106,089,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p36 LHR passenger-carrying flights (Cirium schedule data), full year 2025 = **482,000** flights (2025-01-01..2025-12-31) [keep: ] quote: "almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p37 LHR mean load factor (passengers per seat), full year 2025 = **79.6** % (2025-01-01..2025-12-31) [keep: ] quote: "equating to a mean load factor of 79.6%"
  - p38 LHR passengers, December 2025 = **7,189,000** passengers (2025-12-01..2025-12-31) [keep: ] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p39 LHR December 2025 passenger growth year-on-year = **1.6** % (2025-12-01..2025-12-31) [keep: ] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p40 LHR record single-day passengers, August 1 2025 (lower bound 'more than') = **270,000** passengers (2025-08-01..2025-08-01) [keep: ] quote: "with August 1 seeing a record-breaking total of more than 270,000 guests passing through its doors"
  - p41 LHR cargo handled, December 2025 = **138,000** tonnes (2025-12-01..2025-12-31) [DISCARD: Cargo tonnage — different quantity, not passengers.] quote: "with 138,000 tonnes handled in December alone"
- `https://www.caa.co.uk/media/hvmi0rb4/steer-h8-traffic-review-for-ips.pdf` -> **snapshot** (snapshot 20260711081541); points raw/verified 15/5
  - p42 Heathrow 2024 actual load factor (approximate) = **80.7** % (2024-01-01..2024-12-31) [keep: ] quote: "2024 approximate Load Factor: 80.7%"
  - p43 Heathrow 2024 actual passengers = **83,900,000** passengers (2024-01-01..2024-12-31) [keep: ] quote: "83.9m passengers +5.9%"
  - p44 Heathrow 2024 actual passengers per PATM = **178** passengers per passenger ATM (2024-01-01..2024-12-31) [keep: ] quote: "Pax/ATM 160 161 166 170 171 125 121 168 176 178"
  - p45 Heathrow 2024 connecting (transfer) share of passengers = **27** % (2024-01-01..2024-12-31) [keep: ] quote: "Origin/Destination 73% Connecting 27%"
  - p46 Heathrow 2024 actual passenger ATMs = **471,280** passenger ATMs (2024-01-01..2024-12-31) [keep: ] quote: "In 2024 the airport served 471,280 PATMs, representing 99.6% of the pre-pandemic 2019 value."
- dropped by code checks: 23 (period_end missing or unparseable: 2; period_end 2026-10-24 after as_of: 6; period_end 2026-12-31 after as_of: 12; scale word 'million' not supported by quote or table header: 3)

### d3 [related_series] UK CAA airport statistics

Hypothesis: CAA publishes monthly terminal passenger totals for UK airports including Heathrow; September 2026 CAA data may lag but Sept 2025 and 2026 partials constrain the level and seasonality.

Queries issued by the searcher: CAA airport statistics Heathrow monthly terminal passengers 2025; Heathrow monthly traffic statistics September 2025 passengers; Heathrow business and traffic commentary July 2026 passengers; Heathrow August 2026 passenger numbers record

- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-jul-2026/9714388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/13
  - p47 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p48 Heathrow passengers welcomed in September (narrative, nearly) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate narrative of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p49 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p50 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p51 Heathrow total terminal passengers year-on-year % change, September 2025 = **0.8** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p52 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p53 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p54 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p55 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p56 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p57 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p58 Heathrow total air transport movements, Jan to Sep 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4/p13 cumulative ATMs.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p59 Heathrow total air transport movements, Oct 2024 to Sep 2025 rolling 12 months = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p20.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.caa.co.uk/Documents/Download/24000/70cf208e-d8f7-4cab-8da0-ab741d4bad38/17225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tripyana.com/london-airport-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### d4 [capacity_consumption] Airport infrastructure constraint

Hypothesis: Passengers ≈ daily passenger throughput × 30 days; throughput bounded by runway movement cap (~1,300 movements/day) × passengers per movement (~150-160). Gives an upper bound and central estimate.

Queries issued by the searcher: Heathrow monthly traffic statistics air transport movements 2025; Heathrow passengers per aircraft movement 2024 2025; Heathrow "traffic statistics" September 2025 passengers terminal passengers 7.4 million report; Heathrow August 2026 passenger numbers record monthly traffic

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p60 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p61 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p62 Heathrow total terminal passengers, Jan to Sep 2025 (table, thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p63 Heathrow total air transport movements, Jan to Sep 2025 = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4/p13 cumulative ATMs.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p64 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (tabl = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p6.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p65 Heathrow total air transport movements, Oct 2024 to Sep 2025 rolling 12 months = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Duplicate of p20.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p66 Heathrow passengers welcomed in September (stated as nearly 7.4 million, busiest = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate narrative of p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever and rounding off a record-breaking summer."
  - p67 Heathrow passengers welcomed in September (CEO quote, nearly 7.4 million) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate narrative of p1.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance in punctuality and security."
  - p68 Heathrow UK market terminal passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p69 Heathrow EU market terminal passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p70 Heathrow North America market terminal passengers, September 2025 (table, thousa = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p71 Heathrow EU market air transport movements, September 2025 = **18,090** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 18,090 \| 1.7 \| 157,967 \| 1.6 \| 208,860 \| 1.9 \|"
  - p72 Heathrow North America market air transport movements, September 2025 = **8,197** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 8,197 \| 2.4 \| 69,522 \| 0.7 \| 91,548 \| -0.1 \|"
  - p73 Heathrow UK market air transport movements, September 2025 = **2,893** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 2,893 \| -1.3 \| 27,541 \| 1.7 \| 37,605 \| 5.3 \|"
  - p74 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Cargo tonnage — different quantity.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://planning.hillingdon.gov.uk/OcellaWeb/viewDocument?file=dv_pl_files%5C41573_APP_2024_2838%5C6.7+-+ES+Chapter+7+Noise+and+Vibration.pdf&module=p` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://simpleflying.com/britain-busiest-airport-busier-record-breaking-year/` -> **snapshot** (snapshot 20260215014044); points raw/verified 12/8
  - p75 Heathrow annual passengers 2025 = **84,463,000** passengers (2025-01-01..2025-12-31) [DISCARD: Duplicate of p33/p147.] quote: "London Heathrow Airport handled a grand total of 84.463 million passengers in 2025"
  - p76 Heathrow annual passenger-carrying flights 2025 (Cirium) = **482,000** flights (2025-01-01..2025-12-31) [keep: ] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p77 Heathrow annual available seats 2025 (Cirium) = **106,089,000** seats (2025-01-01..2025-12-31) [DISCARD: Duplicate of p35/p148.] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p78 Heathrow mean load factor 2025 (Cirium) = **79.6** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p37/p150.] quote: "equating to a mean load factor of 79.6%"
  - p79 Heathrow December 2025 passengers = **7,189,000** passengers (2025-12-01..2025-12-31) [DISCARD: Duplicate of p38/p151.] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p80 Heathrow busiest-ever single day passengers (August 1, 2025), lower bound = **270,000** passengers (2025-08-01..2025-08-01) [DISCARD: Duplicate of p40.] quote: "with August 1 seeing a record-breaking total of more than 270,000 guests passing through its doors"
  - p81 Heathrow December 2025 cargo tonnes = **138,000** tonnes (2025-12-01..2025-12-31) [DISCARD: Cargo tonnage — different quantity.] quote: "with 138,000 tonnes handled in December alone"
  - p82 Heathrow 2025 annual passenger growth vs 2024 = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "representing an increase of 0.7% compared to the full-year figure that it posted in 2024"
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d5 [forecasts_markets] Airport guidance and analyst forecasts

Hypothesis: Heathrow or parent (FGP/ADR) guidance and analyst traffic forecasts for 2026 imply an annual passenger total; September share of annual (~8.5-9%) converts to monthly.

Queries issued by the searcher: Heathrow 2026 passenger forecast guidance annual passengers; Heathrow monthly traffic statistics September passengers 2024 2025; Heathrow annual passenger totals 2015 2016 2017 2018 2019 September monthly passengers table; Heathrow July 2026 traffic commentary passengers monthly

- `https://www.standard.co.uk/business/business-news/heathrow-middle-east-iran-london-b1287694.html` -> **snapshot** (snapshot 20260627174253); points raw/verified 8/2
  - p83 Heathrow 2025 passenger total (all-time high, comparison year) = **84,500,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "That is compared with 84.5 million in 2025, which was an all-time high."
  - p84 Middle East routes passenger decline (percentage) = **25** % (not stated (page dated 2026-06-26)) [keep: ] quote: "with Middle East routes down 25%, the west London airport said in an investor report."
- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/Documents/Download/24003/a90c0dd7-e580-4607-b1d9-0b4fc72566fc/17360` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end 2026-12-31 after as_of: 6)

### d6 [shocks] Disruption and demand events

Hypothesis: September 2026 level may deviate from trend due to strikes, ATC disruptions, geopolitical events, or demand shocks between cutoff and month-end; these shift the estimate around the trend baseline.

Queries issued by the searcher: Heathrow strike September 2026; Heathrow flight cancellations September 2026; Heathrow monthly traffic statistics August 2026 passengers; Heathrow September 2025 passengers monthly traffic statistics record

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://beta.rtbf.be/article/plus-de-2000-vols-annules-depuis-mardi-au-royaume-uni-trafic-toujours-perturbe-11782617` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hindustantimes.com/india-news/indians-stranded-as-uk-air-traffic-failure-cancels-2000-flights-air-india-indigo-services-hit-10178900405717` -> **snapshot** (snapshot 20260911094115); points raw/verified 15/15
  - p85 Flights cancelled at UK airports on Day 2 of ATC disruption (Wednesday) = **291** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "On Wednesday, 291 flights - 120 departures and 171 arrivals - were cancelled at UK airports"
  - p86 Departures cancelled at UK airports on Day 2 of ATC disruption (Wednesday) = **120** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "291 flights - 120 departures and 171 arrivals - were cancelled at UK airports"
  - p87 Arrivals cancelled at UK airports on Day 2 of ATC disruption (Wednesday) = **171** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "291 flights - 120 departures and 171 arrivals - were cancelled at UK airports"
  - p88 Share of scheduled UK flights cancelled on Day 2 (Wednesday) = **5** % (not stated (page dated 2026-09-10)) [keep: ] quote: "were cancelled at UK airports, about 5% of the 5,869 scheduled, aviation analytics company Cirium said."
  - p89 Scheduled flights at UK airports on Day 2 (Wednesday) = **5,869** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "about 5% of the 5,869 scheduled, aviation analytics company Cirium said."
  - p90 Normal-day cancellation rate range at UK airports (lower bound) = **1** % (not stated (page dated 2026-09-10)) [keep: ] quote: "Cancellations on a normal day run between 1% and 2%."
  - p91 Normal-day cancellation rate range at UK airports (upper bound) = **2** % (not stated (page dated 2026-09-10)) [keep: ] quote: "Cancellations on a normal day run between 1% and 2%."
  - p92 Share of scheduled UK flights cancelled or not operated on Day 1 (Tuesday) = **30.1** % (not stated (page dated 2026-09-10)) [keep: ] quote: "Tuesday was worse, with about 30.1% of 5,800 scheduled flights cancelled or not operated."
  - p93 Scheduled flights at UK airports on Day 1 (Tuesday) = **5,800** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "Tuesday was worse, with about 30.1% of 5,800 scheduled flights cancelled or not operated."
  - p94 Flights cancelled over two days of ATC disruption (UK) = **2,000** flights (not stated (page dated 2026-09-10)) [keep: ] quote: "A technical failure in UK's air traffic control system forced the cancellation of more than 2,000 flights over two days"
  - p95 Airports affected by UK ATC disruption = **15** airports (not stated (page dated 2026-09-10)) [keep: ] quote: "disrupting operations at 15 airports including Heathrow"
  - p96 India-UK flights cancelled as of 4pm Wednesday = **7** as written "Seven", value check pending flights (not stated (page dated 2026-09-10)) [DISCARD: India-UK flight cancellations — too narrow and not Heathrow-specific.] quote: "Seven of the 24 flights scheduled from India to the UK had been cancelled as of 4pm on Wednesday, Cirium said."
  - p97 Flights scheduled from India to the UK on Wednesday = **24** flights (not stated (page dated 2026-09-10)) [DISCARD: India-UK scheduled flights — irrelevant to total.] quote: "Seven of the 24 flights scheduled from India to the UK had been cancelled as of 4pm on Wednesday, Cirium said."
  - p98 Air India London flights diverted Tuesday and cancelled Wednesday = **4** as written "four", value check pending flights (not stated (page dated 2026-09-10)) [DISCARD: Air India diversions — irrelevant to total.] quote: "Air India's four London flights were diverted on Tuesday and cancelled the following day."
  - p99 Government ownership share of NATS = **49** % (not stated (page dated 2026-09-10)) [DISCARD: NATS ownership share — irrelevant to passenger count.] quote: "The government, which owns 49% of NATS, said Rolfe retains its confidence."
- `https://www.standard.co.uk/business/business-news/heathrow-london-istanbul-heidi-alexander-john-healey-b1296548.html` -> **snapshot** (snapshot 20260911194013); points raw/verified 11/2
  - p100 Flights arriving or departing UK cancelled due to Nats technical fault = **2,000** flights (not stated (page dated 2026-09-11)) [keep: ] quote: "which caused more than 2,000 flights arriving or departing the UK to be cancelled following the fault on Tuesday"
  - p101 Airlines seeking slots at Heathrow without availability = **40** airlines (not stated (page dated 2026-09-11)) [DISCARD: Airlines seeking slots — irrelevant to September 2026 passenger level.] quote: "The longest queue at Heathrow is now the one made up of over 40 airlines that want to better connect the UK but can't secure a slot because our runways are full"
- dropped by code checks: 9 (period year 2025 does not appear in the page text or URL (likely mis-dated): 9)

### b1 [own_history] Heathrow monthly traffic statistics

Hypothesis: Heathrow monthly passenger totals for Jan–Jul 2026 (published before cutoff) would give the actual 2026 YoY growth trend, replacing the assumption-based growth factor in the d1 route and anchoring the September 2026 level.

Queries issued by the searcher: Heathrow monthly traffic statistics 2026 passengers; Heathrow mediacentre July 2026 passenger numbers

- `https://mediacentre.heathrow.com/pressrelease/detail/26027` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/25925` -> **snapshot** (snapshot 20260824084305); points raw/verified 15/15
  - p102 Heathrow total passengers, first half 2026 (record), millions = **40,000,000** passengers (2026-01-01..2026-06-30) [keep: ] quote: "Heathrow welcomed a record 40 million passengers in the first half of 2026"
  - p103 Heathrow passengers, six months ended 30 June 2026, millions = **40,000,000** passengers (2026-01-01..2026-06-30) [keep: ] quote: "\| Passengers (millions)(7) \| 40.0 \| 39.9 \| 0.2 \|"
  - p104 Heathrow passengers, six months ended 30 June 2025, millions = **39,900,000** passengers (2025-01-01..2025-06-30) [keep: ] quote: "\| Passengers (millions)(7) \| 40.0 \| 39.9 \| 0.2 \|"
  - p105 Heathrow passengers YoY change, six months ended 30 June 2026 vs 2025, percent = **0.2** percent (2026-01-01..2026-06-30) [keep: ] quote: "\| Passengers (millions)(7) \| 40.0 \| 39.9 \| 0.2 \|"
  - p106 Heathrow North America passenger growth, first half 2026, percent = **1.6** % (2026-01-01..2026-06-30) [keep: ] quote: "significant growth in North America (up 1.6%) and Asia-Pacific (up 7.9%)"
  - p107 Heathrow Asia-Pacific passenger growth, first half 2026, percent = **7.9** % (2026-01-01..2026-06-30) [keep: ] quote: "significant growth in North America (up 1.6%) and Asia-Pacific (up 7.9%)"
  - p108 Heathrow transfer passenger increase, first half 2026, percent = **5.4** % (2026-01-01..2026-06-30) [keep: ] quote: "a 5.4% increase in transfer passengers"
  - p109 Heathrow cargo increase, first half 2026, percent = **1** % (2026-01-01..2026-06-30) [keep: ] quote: "nearly a 1% increase in cargo through the UK's largest port"
  - p110 Heathrow revenue, six months ended 30 June 2026, £m = **1,729,000,000** GBP (2026-01-01..2026-06-30) [keep: ] quote: "revenue grew by 0.3% to £1,729 million (six months ended 30 June 2025: £1,724 million)"
  - p111 Heathrow revenue, six months ended 30 June 2025, £m = **1,724,000,000** GBP (2025-01-01..2025-06-30) [keep: ] quote: "revenue grew by 0.3% to £1,729 million (six months ended 30 June 2025: £1,724 million)"
  - p112 Heathrow revenue growth, six months ended 30 June 2026, percent = **0.3** % (2026-01-01..2026-06-30) [keep: ] quote: "revenue grew by 0.3% to £1,729 million (six months ended 30 June 2025: £1,724 million)"
  - p113 Heathrow adjusted EBITDA, six months ended 30 June 2026, £m = **915,000,000** GBP (2026-01-01..2026-06-30) [keep: ] quote: "Adjusted EBITDA fell by 4.6% to £915 million (six months ended 30 June 2025: £959 million)"
  - p114 Heathrow adjusted EBITDA, six months ended 30 June 2025, £m = **959,000,000** GBP (2025-01-01..2025-06-30) [keep: ] quote: "Adjusted EBITDA fell by 4.6% to £915 million (six months ended 30 June 2025: £959 million)"
  - p115 Heathrow adjusted EBITDA change, six months ended 30 June 2026, percent = **4.6** % (2026-01-01..2026-06-30) [keep: ] quote: "Adjusted EBITDA fell by 4.6% to £915 million (six months ended 30 June 2025: £959 million)"
  - p116 Heathrow liquidity, as at 30 June 2026, £ billion = **3,800,000,000** GBP (2026-06-30..2026-06-30) [keep: ] quote: "liquidity is strong at £3.8 billion, sufficient to meet all of our obligations for at least the next 18 months"
- `https://mediacentre.heathrow.com/pressrelease/detail/25368` -> **snapshot** (snapshot 20260511072728); points raw/verified 15/15
  - p117 Heathrow April 2026 total terminal passengers (thousands) = **6,721,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p118 Heathrow April 2026 total terminal passengers YoY % change = **-5.3** percent (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p119 Heathrow Jan to Apr 2026 cumulative total terminal passengers (thousands) = **25,646,000** passengers (2026-01-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p120 Heathrow Jan to Apr 2026 cumulative total terminal passengers YoY % change = **1.2** percent (2026-01-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p121 Heathrow May 2025 to Apr 2026 rolling 12-month total terminal passengers (thousa = **84,763,000** passengers (2025-05-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p122 Heathrow May 2025 to Apr 2026 rolling 12-month total terminal passengers YoY % c = **0.9** percent (2025-05-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p123 Heathrow April 2026 passenger numbers YoY decrease (narrative) = **5** % (2026-04-01..2026-04-30) [keep: ] quote: "April passenger numbers decreased by 5% year on year to 6.7 million"
  - p124 Heathrow April 2026 passenger numbers (narrative, millions) = **6,700,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "April passenger numbers decreased by 5% year on year to 6.7 million"
  - p125 Heathrow April 2026 transfer passenger demand YoY increase = **10** % (2026-04-01..2026-04-30) [keep: ] quote: "strong transfer passenger demand continuing into April with a 10% increase year on year"
  - p126 Heathrow April 2026 Middle East terminal passengers (thousands) = **360,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p127 Heathrow April 2026 Middle East terminal passengers YoY % change = **-52.4** percent (2026-04-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p128 Heathrow Jan to Apr 2026 Middle East cumulative terminal passengers (thousands) = **2,159,000** passengers (2026-01-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p129 Heathrow Jan to Apr 2026 Middle East cumulative terminal passengers YoY % change = **-23.4** percent (2026-01-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p130 Heathrow April 2026 total Air Transport Movements = **38,496** air transport movements (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 38,496 \| -4.6 \| 150,878 \| -1.5 \| 475,547 \| 0.1 \|"
  - p131 Heathrow Jan to Apr 2026 cumulative total Air Transport Movements = **150,878** air transport movements (2026-01-01..2026-04-30) [keep: ] quote: "\| Total \| \| 38,496 \| -4.6 \| 150,878 \| -1.5 \| 475,547 \| 0.1 \|"

### b2 [capacity_consumption] Schedule data

Hypothesis: September 2026 scheduled seat capacity at LHR (OAG/Cirium) times a load factor would give an independent capacity-based estimate, resolving the largest uncertainty in the d2 route (load factor and capacity).

Queries issued by the searcher: Heathrow September 2026 scheduled seats capacity OAG Cirium; Heathrow monthly traffic statistics passengers 2025 record; OAG September 2025 busiest airports international seats Heathrow 4.1 million; Heathrow passenger numbers September 2025 record 7.9 million monthly traffic statistics

- `http://sahafati.com/bh/en/post/5615/353242773/dubai-stays-on-top-dxb-named-world-s-busiest-international-airport-for-the-month.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news.flylinkers.com/dubai-lidera-el-ranking-de-aeropuertos-internacionales-mas-transitados-en-septiembre-de-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businesstravelnewseurope.com/Air-Travel/OAG-London-Heathrow-remains-Europe-s-busiest-airport` -> **snapshot** (snapshot 20260120111549); points raw/verified 15/15
  - p132 London Heathrow total departing seats, 2025 (OAG annual capacity) = **52,100,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "London Heathrow retained its place as Europe's busiest airport in 2025 with a total of 52.1 million departing seats"
  - p133 Istanbul total departing seats, 2025 (OAG annual capacity) = **51,500,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "which was just ahead of Istanbul with 51.5 million seats, according to aviation data firm OAG."
  - p134 Atlanta total departing seats, 2025 (OAG annual capacity) = **63,100,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "behind Atlanta (63.1 million seats)"
  - p135 Dubai total departing seats, 2025 (OAG annual capacity) = **62,400,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "Dubai (62.4 million seats)"
  - p136 Tokyo Haneda total departing seats, 2025 (OAG annual capacity) = **55,400,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "Tokyo Haneda (55.4 million)"
  - p137 Heathrow capacity change in 2025 vs 2019 (pre-Covid year) = **4** % (2025-01-01..2025-12-31) [keep: ] quote: "with Heathrow's capacity up by 4 per cent on the pre-Covid year"
  - p138 Istanbul total seats change in 2025 vs 2019 = **22** % (2025-01-01..2025-12-31) [keep: ] quote: "Istanbul's total seats rising by 22 per cent over the same period."
  - p139 Paris Charles de Gaulle departing seats capacity, 2025 = **43,200,000** departing seats (2025-01-01..2025-12-31) [keep: ] quote: "Paris Charles de Gaulle was the third busiest European airport with a capacity of 43.2 million departing seats in 2025."
  - p140 Paris Charles de Gaulle capacity change in 2025 vs 2024 = **3** % (2025-01-01..2025-12-31) [keep: ] quote: "While this was a 3 per cent increase on 2024"
  - p141 Paris Charles de Gaulle capacity change in 2025 vs 2019 = **4** % (2025-01-01..2025-12-31) [keep: ] quote: "it was still 4 per cent below 2019 levels"
  - p142 Amsterdam Schiphol departing seats, 2025 = **41,340,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "Amsterdam Schiphol was in fourth place with 41.34 million seats"
  - p143 Amsterdam Schiphol seats, 2019 = **41,360,000** seats (2019-01-01..2019-12-31) [keep: ] quote: "just fractionally down on 2019's figure of 41.36 million."
  - p144 Frankfurt departing seats, 2025 = **40,700,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "The German hubs of Frankfurt and Munich were ranked as Europe's fifth and tenth busiest airports with 40.7 million and 28.1 million seats respectively in 2025."
  - p145 Munich departing seats, 2025 = **28,100,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "with 40.7 million and 28.1 million seats respectively in 2025."
  - p146 Frankfurt capacity change in 2025 vs 2019 = **10** % (2025-01-01..2025-12-31) [keep: ] quote: "Frankfurt's capacity is 10 per cent lower than in 2019"
- `https://simpleflying.com/britain-busiest-airport-busier-record-breaking-year/` -> **snapshot** (snapshot 20260215014044); points raw/verified 15/12
  - p147 LHR 2025 total passengers handled (full year) = **84,463,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "London Heathrow Airport handled a grand total of 84.463 million passengers in 2025"
  - p148 LHR 2025 seats available on passenger-carrying flights to/from LHR (Cirium sched = **106,089,000** seats (2025-01-01..2025-12-31) [keep: ] quote: "106.089 million seats were available on almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p149 LHR 2025 passenger-carrying flights to/from LHR (Cirium scheduling data) = **482,000** flights (2025-01-01..2025-12-31) [keep: ] quote: "almost 482,000 passenger-carrying flights to and from London Heathrow Airport in 2025"
  - p150 LHR 2025 mean load factor (passengers as share of available seats) = **79.6** % (2025-01-01..2025-12-31) [keep: ] quote: "equating to a mean load factor of 79.6%"
  - p151 LHR December 2025 passengers (busiest-ever December) = **7,189,000** passengers (2025-12-01..2025-12-31) [keep: ] quote: "with 7.189 million passengers passing through its doors (up 1.6% year-on-year) during what was its busiest-ever December"
  - p152 LHR 2025 annual passenger total growth vs 2024 = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "representing an increase of 0.7% compared to the full-year figure that it posted in 2024"
  - p153 LHR December 2025 passenger growth year-on-year = **1.6** % (2025-12-01..2025-12-31) [keep: ] quote: "7.189 million passengers passing through its doors (up 1.6% year-on-year)"
  - p154 LHR 2025 Middle East market passenger growth year-on-year = **2.8** % (2025-01-01..2025-12-31) [keep: ] quote: "The biggest growth in terms of passenger numbers came in the Middle East market, where the total was up by 2.8% year-on-year"
  - p155 LHR 2025 Asia/Pacific market passenger growth year-on-year = **2.6** % (2025-01-01..2025-12-31) [keep: ] quote: "followed by the Asia / Pacific region (2.6%), Africa (2.1%), and the EU (1.1%)"
  - p156 LHR 2025 Africa market passenger growth year-on-year = **2.1** % (2025-01-01..2025-12-31) [keep: ] quote: "Africa (2.1%), and the EU (1.1%)"
  - p157 LHR 2025 EU market passenger growth year-on-year = **1.1** % (2025-01-01..2025-12-31) [keep: ] quote: "and the EU (1.1%)"
  - p158 LHR 2025 North America market passenger change year-on-year = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "non-EU European destinations (-1.7%), UK domestic destinations (-1.1%), and North America (-0.3%)"
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 3)

### b3 [shocks] ATC disruption impact

Hypothesis: A Heathrow-specific count of flights/passengers cancelled during the early-September 2026 NATS disruption would let us size the shock deduction rather than assume a Heathrow share of the UK-wide 2,000 cancellations.

Queries issued by the searcher: Heathrow flights cancelled September 2026 NATS ATC failure; NATS ATC disruption September 2026 2000 flights cancelled; Heathrow airport statement September 2026 "passengers" affected cancellations NATS number of flights cancelled at Heathrow; Cirium Heathrow September 8 2026 cancelled flights total departures arrivals percentage

- `https://prod.khaleejtimes.com/business/aviation/air-traffic-control-issue-major-uk-airports-flights-cancelled-delayed` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.standard.co.uk/news/london/heathrow-flights-cancelled-thursday-nats-compensation-martin-rolfe-b1295995.html?page=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indy-web-prod.brightsites.co.uk/travel/news-and-advice/uk-airport-delays-gatwick-heathrow-air-traffic-control-live-updates-b3047300.html?page=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://qazinform.com/news/more-than-1400-flights-canceled-at-uk-airports-after-air-traffic-control-failure-42b5cb` -> **snapshot** (snapshot 20260910193734); points raw/verified 4/4
  - p159 Flights canceled to/from UK airports on Tuesday after NATS ATC failure = **1,300** flights (2026-09-08..2026-09-08) [keep: ] quote: "A total of 1,300 flights to and from UK airports were canceled on Tuesday"
  - p160 Flights canceled by Wednesday at UK airports (nearly all at London Heathrow) = **177** flights (2026-09-09..2026-09-09) [keep: ] quote: "177 flights have been canceled so far on Wednesday, nearly all at London-Heathrow."
  - p161 Total flights canceled at UK airports after ATC failure (cumulative, more than) = **1,400** flights (2026-09-08..2026-09-09) [keep: ] quote: "More than 1,400 flights have been canceled at airports across the United Kingdom following a technical failure at a NATS air traffic control facility earlier Tuesday"
  - p162 Flights canceled to/from UK airports on Tuesday (restated) = **1,300** flights (2026-09-08..2026-09-08) [keep: ] quote: "All told, 1300 flights were canceled to/from airports in the UK on Tuesday."

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['heathrow passengers', 'lhr traffic', 'heathrow september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p15', 'p47', 'p60'] Identical September 2025 total terminal passenger figure (7,348,000) repeated across directions; same underlying Heathrow monthly traffic table, so this is one measurement, not four independent confir
- corroborating: ['p2', 'p16', 'p48', 'p66', 'p67'] Narrative 'nearly 7.4 million' is a rounded restatement of the same September 2025 table value; consistent with p1 but not independent.
- corroborating: ['p1', 'p3', 'p51'] September 2025 level and its +0.8% YoY are from the same table row; internally consistent.
- corroborating: ['p4', 'p18', 'p49', 'p62'] Jan–Sep 2025 cumulative 63,275k repeated; same source table.
- corroborating: ['p6', 'p19', 'p50', 'p64'] Rolling 12-month 84,065k repeated; same source table.
- corroborating: ['p13', 'p17', 'p57', 'p61'] September 2025 ATMs 40,193 repeated; same table.
- corroborating: ['p33', 'p75'] Full-year 2025 passengers 84.463m from same Simple Flying article; consistent with p83's 84.5m rounded figure.
- corroborating: ['p35', 'p77'] 2025 available seats 106.089m, same Cirium-derived article.
- corroborating: ['p37', 'p78'] 2025 mean load factor 79.6%, same article.
- corroborating: ['p38', 'p79'] December 2025 passengers 7.189m, same article.
- corroborating: ['p40', 'p80'] Record single-day >270,000 on 1 Aug 2025, same article.
- corroborating: ['p41', 'p81'] December 2025 cargo 138,000t, same article.
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46'] CAA 2024 Heathrow statistics: 83.9m passengers, 471,280 PATMs, 178 pax/PATM, 80.7% load factor, 27% connecting share — internally consistent (83.9m/471,280 ≈ 178).
- corroborating: ['p33', 'p43'] 2025 84.463m vs 2024 83.9m implies ~0.7% growth, matching p34/p82.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p92', 'p93', 'p94', 'p100'] UK-wide NATS ATC disruption early September 2026: ~2,000 flights cancelled over two days across 15 airports including Heathrow. UK-wide scope, not Heathrow-specific; needs a Heathrow share assumption 
- corroborating: ['p90', 'p91'] Normal-day UK cancellation rate 1–2%, giving a baseline against which the disruption excess is measured.
- corroborating: ['p84', 'p83'] Same Standard article: 2025 all-time high 84.5m and Middle East routes down 25% in an investor report — a 2026 headwind signal.
- corroborating: ['p29', 'p30', 'p31'] Qatar Airways July 2026 schedule detail; contextual only, not a Heathrow total.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p3', 'p51'] Same Heathrow September 2025 release: p1 is the September 2025 terminal passenger level (7.348m) and p3/p51 are the same 0.8% YoY figure quoted twice. They are one measurement, not independent confirm
- corroborating: ['p4', 'p5', 'p6', 'p7'] Same September 2025 Heathrow traffic release: Jan–Sep 2025 cumulative 63.275m (+0.3%) and Oct 2024–Sep 2025 rolling 84.065m (+1.5%). Consistent internally; useful for level/seasonality context but not
- corroborating: ['p8', 'p9', 'p10', 'p11', 'p12', 'p26', 'p27', 'p28'] Regional breakdown of the same September 2025 total; sums approximately to p1. Useful for understanding which regions drive 2026 change (Middle East collapse), not as separate estimates of the total.
- corroborating: ['p13', 'p14', 'p20', 'p71', 'p72', 'p73'] September 2025 air transport movements (40,193, +0.5%) and regional movement splits from the same release. Supports a movements × passengers-per-movement cross-check.
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p76', 'p82', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153'] Simple Flying/Cirium 2025 annual figures: 84.463m passengers, 106.089m seats, 79.6% load factor, 482k flights, December 7.189m. p33/p147, p35/p148, p36/p149, p37/p150, p38/p151, p39/p153, p34/p152 are
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46'] CAA 2024 Heathrow data: 83.9m passengers, 80.7% load factor, 178 pax/PATM, 471,280 PATMs, 27% connecting share. Independent of Heathrow's own release and of Cirium; gives a passengers-per-movement anc
- corroborating: ['p83', 'p84'] Standard/Heathrow investor report: 2025 all-time high 84.5m (consistent with p33's 84.463m) and Middle East routes down 25% in the 2026 investor report — corroborates the Middle East weakness seen in 
- corroborating: ['p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108'] H1 2026 Heathrow results: 40.0m passengers vs 39.9m H1 2025 (+0.2%), with North America +1.6%, Asia-Pacific +7.9%, transfers +5.4%. This is the key 2026 growth anchor; p102 and p103 are the same 40.0m
- corroborating: ['p117', 'p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131'] April 2026 Heathrow release: April 6.721m (−5.3%), Jan–Apr 25.646m (+1.2%), rolling 84.763m (+0.9%), Middle East April −52.4% and Jan–Apr −23.4%, April ATMs 38,496 (−4.6%). Shows 2026 growth is near-f
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p100', 'p159', 'p160', 'p161', 'p162'] Early-September 2026 NATS ATC disruption: ~2,000 UK flights cancelled over two days (p94/p100/p161), 15 airports affected including Heathrow (p95), Wednesday cancellations 'nearly all at Heathrow' (p1
- corroborating: ['p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p139', 'p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p146'] OAG 2025 departing-seat rankings: Heathrow 52.1m departing seats (≈104.2m both directions, consistent with Cirium's 106.089m), capacity +4% vs 2019. Cross-source corroboration of capacity level.
- corroborating: ['p1', 'p35', 'p37', 'p42', 'p43', 'p44', 'p46'] Cross-check: 84.463m/106.089m ≈ 79.6% load factor (p33/p35/p37); CAA 2024 83.9m/471,280 PATM ≈ 178 pax/PATM (p43/p44/p46). These are mutually consistent and give a defensible passengers-per-movement b

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth factor vs September 2025 | 1.005 | 0.97..1.04 | 0.8984..1.123 (widened) | ratio | m1 (m1), m3 (m3) | H1 2026 was +0.2% (p105), Jan–Apr +1.2% (p120), rolling 12m +0.9% (p122), but April was −5.3% (p118) with a severe Middle East drag (p127, p84). September 2025 was already a strong month (+0.8%, p3). Net: near-flat to slightly positive, with downside from continued Middle East weakness and the early | September 2026 demand tracks the 2026 H1/spring trend with no major new shock beyond the early-September ATC event. | Published Aug/Sep 2026 Heathrow figures showing a sharp acceleration or a much deeper decline than the H1 trend. |
| a2 | Heathrow share of UK-wide ATC-disruption cancellations | 0.15 | 0.06..0.3 | 0.06..0.3 | share | m3 (m3) | p160 says Wednesday cancellations were 'nearly all at Heathrow', but Heathrow is one of 15 affected airports (p95) and handles a large but not dominant share of UK movements. A 15% central share with wide range reflects the ambiguity between the 'nearly all' Wednesday statement and the UK-wide two-d | The ~2,000 UK-wide cancellations (p94/p100) are distributed across airports roughly in proportion to Heathrow's share of UK traffic, adjusted upward for the Wednesday concentration. | A Heathrow-specific cancellation count showing a materially different share. |
| a3 | Passengers per cancelled Heathrow flight | 160 | 120..200 | 110..219 (widened) | passengers per flight | m3 (m3) | CAA 2024 gives 178 pax/PATM (p44) and Cirium 2025 gives ~175 passengers per flight (84.463m/482k, p33/p36). Cancelled flights are typically short-haul/high-frequency, so slightly below the airport average; 160 with a wide range. | Cancelled flights carry roughly the airport-average passenger load, slightly reduced for short-haul mix. | Evidence that cancelled flights were predominantly long-haul high-load or empty ferry flights. |
| a4 | September 2026 load factor relative to 2025 mean | 1 | 0.95..1.05 | 0.7062..1.412 (widened) | ratio | m2 (m2) | 2025 mean load factor was 79.6% (p37) and 2024 was 80.7% (p42); September is a peak-shoulder month typically at or above the annual mean. A factor near 1.0 with modest range. | September 2026 load factor is close to the 2025 annual mean, adjusted for seasonal peak. | Evidence of a sharp load-factor drop (e.g., demand shock) or a step-up in capacity utilisation. |
| a5 | September share of annual passengers | 0.087 | 0.082..0.092 | 0.06142..0.1228 (widened) | share | m4 (m4) | September 2025 was 7.348m (p1) against a 2025 annual of 84.463m (p33), implying ~8.7%. September is a peak-shoulder month; the share is stable year to year. | September 2026 retains the same seasonal share of the annual total as September 2025. | Evidence of a material change in seasonal shape (e.g., summer peak shifting). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,388,053 | ['p1'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 6,996,505 | ['p35', 'p37'] / ['a4'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 7,337,354 | ['p1', 'p94'] / ['a1', 'a2', 'a3'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 7,333,588 | ['p33'] / ['a5'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **7,262,176** person, 80% interval [4,699,819, 11,221,540] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total passengers passing through London Heathrow Airport during September 2026 (calendar month, terminal/transit passengers per airport traffic convention) is 7,262,176 person (80% model-based interval 4,699,819 to 11,221,540 person; too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

Four routes were averaged at equal weights: own-history scaling of September 2025 (7,348,000 passengers) by a near-flat growth factor (1.005); a capacity route from annual seats (106,089,000 seats) and load factor (79.6%) with a September load-factor factor (1); the trend baseline minus an early-September ATC-disruption deduction using UK cancellations (2,000 flights) times Heathrow share (0.15) times passengers per cancelled flight (160); and an annual-total route (84,463,000 passengers) times September share (0.087).

Only the observed points are data; growth, disruption share, passengers per flight, load factor and seasonal share are analyst assumptions, and the routes share inputs, so they are not independent. The main risk is a 2026 demand shock or a larger-than-assumed disruption effect. Actual September 2026 schedule and booking data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth factor vs September 2025: 1.005 ratio, range 0.8984 to 1.123 (range widened by code); used by m1, m3. Overturned by: Published Aug/Sep 2026 Heathrow figures showing a sharp acceleration or a much deeper decline than the H1 trend.
- a2 Heathrow share of UK-wide ATC-disruption cancellations: 0.15 share, range 0.06 to 0.3; used by m3. Overturned by: A Heathrow-specific cancellation count showing a materially different share.
- a3 Passengers per cancelled Heathrow flight: 160 passengers per flight, range 110 to 219 (range widened by code); used by m3. Overturned by: Evidence that cancelled flights were predominantly long-haul high-load or empty ferry flights.
- a4 September 2026 load factor relative to 2025 mean: 1 ratio, range 0.7062 to 1.412 (range widened by code); used by m2. Overturned by: Evidence of a sharp load-factor drop (e.g., demand shock) or a step-up in capacity utilisation.
- a5 September share of annual passengers: 0.087 share, range 0.06142 to 0.1228 (range widened by code); used by m4. Overturned by: Evidence of a material change in seasonal shape (e.g., summer peak shifting).

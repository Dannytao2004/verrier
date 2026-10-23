# Evidence ledger: fc_lhr_pax_2026_09

- Question: Assume today is 2026-09-12. You know nothing published after this date. Estimate the number of passengers at London Heathrow Airport in September 2026, as reported in Heathrow's monthly traffic statistics.
- as_of: 2026-09-12
- Pinned target: Total passengers passing through London Heathrow Airport (LHR) during the calendar month of September 2026, as reported in Heathrow's monthly traffic statistics (all terminals, arrivals plus departures, domestic and international combined) | unit passengers | period 2026-09-01..2026-09-30 | publisher Heathrow Airport Limited (monthly traffic statistics / operational figures)

- Official value (scoring only, never shown to the agent): 7,180,000

## Directions and pages

### d1 [own_history] Heathrow monthly traffic statistics publisher

Hypothesis: September 2026 passengers ≈ September 2025 passengers × (recent YoY growth trend) × (calendar/seasonal adjustment for September). September is a strong shoulder-season month; prior-year September levels and the 2026 monthly YoY growth rates (Jan–Aug 2026 vs 2025) anchor the level and trend.

Queries issued by the searcher: Heathrow monthly traffic statistics passengers September 2025; Heathrow airport passengers July 2026 monthly traffic figures; Heathrow August 2026 passengers monthly traffic statistics; "Heathrow" "August 2026" passenger figures year-on-year decline

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p1 Heathrow total passengers, September 2025 (all terminals, arrivals plus departur = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p2 Heathrow total passengers, September 2025, YoY % change = **0.8** % (2025-09-01..2025-09-30) [DISCARD: September 2025 YoY; not needed for level forecast.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p3 Heathrow total passengers, January to September 2025 cumulative = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Jan–Sep 2025 cumulative; not needed given monthly September 2025 level.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p4 Heathrow total passengers, January to September 2025 cumulative, YoY % change = **0.3** % (2025-01-01..2025-09-30) [DISCARD: Jan–Sep 2025 YoY; not needed.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p5 Heathrow total passengers, October 2024 to September 2025 rolling 12 months = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Rolling 12-month to Sep 2025; not needed.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p6 Heathrow total passengers, October 2024 to September 2025 rolling 12 months, YoY = **1.5** % (2024-10-01..2025-09-30) [DISCARD: Rolling 12-month YoY; not needed.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p7 Heathrow passengers, September 2025, stated in narrative as 'nearly 7.4 million' = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative; superseded by precise p1.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever and rounding off a record-breaking summer."
  - p8 Heathrow passengers, September 2025, stated in CEO quote as 'nearly 7.4 million' = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7 narrative.] quote: "welcoming nearly 7.4 million passengers in September alone while maintaining strong performance in punctuality and security"
  - p9 Heathrow EU market passengers, September 2025 = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: September 2025 market split; not needed for total-level methods.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p10 Heathrow North America market passengers, September 2025 = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: September 2025 market split; not needed.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p11 Heathrow Asia/Pacific market passengers, September 2025 = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: September 2025 market split; not needed.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p12 Heathrow Middle East market passengers, September 2025 = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: September 2025 market split; not needed.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p13 Heathrow UK market passengers, September 2025 = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: September 2025 market split; not needed.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p14 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: September 2025 ATMs; not needed for passenger-level methods.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p15 Heathrow total air transport movements, September 2025, YoY % change = **0.5** % (2025-09-01..2025-09-30) [DISCARD: September 2025 ATM YoY; not needed.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.travelwires.com/heathrow-handles-23-million-summer-passengers-as-more-than-40-airlines-seek-slots/` -> **snapshot** (snapshot 20260912073154); points raw/verified 15/15
  - p16 Heathrow passengers, August 2026 (single month, all terminals) = **7,870,000** passengers (2026-08-01..2026-08-31) [DISCARD: Redundant rounded copy of p171/p175 August 2026 level; p171 is the precise table value.] quote: "August alone accounted for 7.87 million passengers, despite traffic being 2.1% lower than in the same month last year."
  - p17 Heathrow August 2026 passenger traffic YoY change = **2.1** % (2026-08-01..2026-08-31) [keep: ] quote: "August alone accounted for 7.87 million passengers, despite traffic being 2.1% lower than in the same month last year."
  - p18 Heathrow passengers, peak summer period June–August 2026 (cumulative) = **23,000,000** passengers (2026-06-01..2026-08-31) [DISCARD: Redundant copy of p174 summer cumulative; adds no new information.] quote: "Between June and August 2026, 23 million passengers travelled through the UK's largest airport."
  - p19 Heathrow passengers, first eight months of 2026 (Jan–Aug cumulative) = **55,720,000** passengers (2026-01-01..2026-08-31) [DISCARD: Redundant rounded copy of p172 Jan–Aug cumulative.] quote: "Passenger traffic for the first eight months of 2026 reached 55.72 million, 0.4% below the equivalent period in 2025."
  - p20 Heathrow Jan–Aug 2026 passenger traffic YoY change vs Jan–Aug 2025 = **0.4** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p178 Jan–Aug YoY change.] quote: "Passenger traffic for the first eight months of 2026 reached 55.72 million, 0.4% below the equivalent period in 2025."
  - p21 Heathrow passengers, 12 months ending August 2026 (trailing 12-month total) = **84,260,000** passengers (2025-09-01..2026-08-31) [DISCARD: Redundant copy of p173 trailing 12-month total.] quote: "Over the 12 months ending August 2026, Heathrow handled 84.26 million passengers, representing a 0.3% increase."
  - p22 Heathrow trailing 12-month (to August 2026) passenger YoY change = **0.3** % (2025-09-01..2026-08-31) [DISCARD: Redundant copy of p179 trailing 12-month YoY change.] quote: "Over the 12 months ending August 2026, Heathrow handled 84.26 million passengers, representing a 0.3% increase."
  - p23 Heathrow aircraft movements, August 2026 = **41,048** aircraft movements (2026-08-01..2026-08-31) [DISCARD: August 2026 ATMs; not needed for passenger-level methods.] quote: "The airport handled 41,048 aircraft movements in August, down 1.3% year-on-year."
  - p24 Heathrow August 2026 aircraft movements YoY change = **1.3** % (2026-08-01..2026-08-31) [DISCARD: August 2026 ATM YoY; not needed.] quote: "The airport handled 41,048 aircraft movements in August, down 1.3% year-on-year."
  - p25 Heathrow busiest-ever single day passengers (August 2, 2026) = **272,000** passengers (2026-08-02..2026-08-02) [DISCARD: Busiest-day count; not needed for monthly total.] quote: "Heathrow also recorded its busiest-ever single day on August 2, when nearly 272,000 passengers passed through the airport."
  - p26 Heathrow Middle East passengers, August 2026 = **668,000** passengers (2026-08-01..2026-08-31) [DISCARD: Middle East August level; not needed for total-level methods.] quote: "Traffic between Heathrow and the Middle East fell 19.8% year-on-year, to approximately 668,000 passengers."
  - p27 Heathrow Middle East passenger YoY change, August 2026 = **19.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p48.] quote: "Traffic between Heathrow and the Middle East fell 19.8% year-on-year, to approximately 668,000 passengers."
  - p28 Heathrow Asia-Pacific passengers, August 2026 = **989,000** passengers (2026-08-01..2026-08-31) [DISCARD: Asia-Pacific August level; not needed.] quote: "Heathrow handled approximately 989,000 Asia-Pacific passengers in August, up 1.2%, while traffic during the first eight months of the year increased 6.6%."
  - p29 Heathrow Asia-Pacific passenger YoY change, Jan–Aug 2026 = **6.6** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p49.] quote: "Heathrow handled approximately 989,000 Asia-Pacific passengers in August, up 1.2%, while traffic during the first eight months of the year increased 6.6%."
  - p30 Heathrow cargo volume, August 2026 = **137,115** metric tonnes (2026-08-01..2026-08-31) [DISCARD: Cargo volume; irrelevant to passenger count.] quote: "Cargo performance was stronger during August, with Heathrow handling approximately 137,115 metric tonnes, up 3.1% year-on-year."
- `https://centreforaviation.com/news/case-for-expansion-has-never-been-clearer-amid-jul-2026-pax-performance-at-london-heathrow-airport-1369277` -> **snapshot** (snapshot 20260813211834); points raw/verified 5/5
  - p31 London Heathrow Airport passengers handled, Jul-2026 = **7,900,000** passengers (2026-07-01..2026-07-31) [DISCARD: July 2026 level; not needed given August and Jan–Aug data.] quote: "it handled 7.9 million passengers in Jul-2026"
  - p32 London Heathrow Airport year-on-year passenger change, Jul-2026 vs Jul-2025 = **1.5** % (2026-07-01..2026-07-31) [DISCARD: July 2026 YoY; not needed.] quote: "a decline of 1.5% year-on-year"
  - p33 London Heathrow Airport passengers on busiest day of 2026, 19-Jul-2026 = **267,000** passengers (2026-07-19..2026-07-19) [DISCARD: Busiest day July 2026; redundant with August busiest-day evidence.] quote: "The airport recorded 267,000 passengers on 19-Jul-2026, its busiest day of 2026 thus far."
  - p34 London Heathrow Airport cargo handled on busiest cargo day of 2026, 12-Jul-2026 = **5,000** tonnes (2026-07-12..2026-07-12) [DISCARD: Busiest cargo day tonnage; irrelevant to passengers.] quote: "handling 5000 tonnes on 12-Jul-2026"
  - p35 Passengers carried by Riyadh Air at London Heathrow Airport, Jul-2026 = **136,000** passengers (2026-07-01..2026-07-31) [DISCARD: Single-carrier (Riyadh Air) passengers; not usable for total and no full carrier breakdown.] quote: "Riyadh Air - which carried more than 136,000 passengers in Jul-2026"
- `https://safariindia.com/heathrow-sees-strong-summer/` -> **snapshot** (snapshot 20260911133436); points raw/verified 15/15
  - p36 Heathrow total passengers, August 2026 (table, thousands) = **7,867,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p16 (table).] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p37 Heathrow total passengers, August 2026 YoY % change = **-2.1** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p17.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p38 Heathrow total passengers, January–August 2026 cumulative (table, thousands) = **55,721,000** passengers (2026-01-01..2026-08-31) [DISCARD: Duplicate of p19.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p39 Heathrow total passengers, January–August 2026 YoY % change = **-0.4** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p20.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p40 Heathrow total passengers, September 2025–August 2026 rolling 12 months (table,  = **84,257,000** passengers (2025-09-01..2026-08-31) [DISCARD: Duplicate of p21.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p41 Heathrow total passengers, September 2025–August 2026 rolling 12 months YoY % ch = **0.3** % (2025-09-01..2026-08-31) [DISCARD: Duplicate of p22.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p42 Heathrow passengers, June–August 2026 summer total (stated in text) = **23,000,000** passengers (2026-06-01..2026-08-31) [DISCARD: Duplicate of p18.] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p43 Heathrow passengers, August 2026 (stated in text) = **7,800,000** passengers (2026-08-01..2026-08-31) [DISCARD: Rounded August narrative; superseded by p16.] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p44 Heathrow passengers on busiest day, 2 August 2026 = **272,000** passengers (2026-08-02..2026-08-02) [DISCARD: Duplicate of p25.] quote: "The airport also recorded its busiest day on 2 August, when nearly 272,000 passengers travelled through its terminals."
  - p45 Heathrow UK market passengers, August 2026 (table, thousands) = **390,000** passengers (2026-08-01..2026-08-31) [DISCARD: UK market August 2026; not needed.] quote: "\| UK \| 390 \| -1.7 \| 3,008 \| 0.2 \| 4,596 \| 0.2 \|"
  - p46 Heathrow EU market passengers, August 2026 (table, thousands) = **2,835,000** passengers (2026-08-01..2026-08-31) [DISCARD: EU market August 2026; not needed.] quote: "\| EU \| 2,835 \| -0.3 \| 19,161 \| 2.0 \| 28,793 \| 2.2 \|"
  - p47 Heathrow North America market passengers, August 2026 (table, thousands) = **1,975,000** passengers (2026-08-01..2026-08-31) [DISCARD: North America August 2026; not needed.] quote: "\| North America \| 1,975 \| -1.1 \| 13,783 \| 0.5 \| 20,626 \| 0.0 \|"
  - p48 Heathrow Middle East market passengers, August 2026 YoY % change = **-19.8** % (2026-08-01..2026-08-31) [DISCARD: Middle East YoY; not needed.] quote: "\| Middle East \| 668 \| -19.8 \| 4,367 \| -23.6 \| 7,429 \| -14.0 \|"
  - p49 Heathrow Asia/Pacific market passengers, January–August 2026 YoY % change = **6.6** % (2026-01-01..2026-08-31) [DISCARD: Asia-Pacific YoY; not needed.] quote: "\| Asia / Pacific \| 989 \| 1.2 \| 7,826 \| 6.6 \| 11,505 \| 5.3 \|"
  - p50 Heathrow total air transport movements, August 2026 YoY % change = **-1.3** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p24.] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"

### d2 [capacity_consumption] Airport slot/ATM and seat capacity planner

Hypothesis: Passengers = air transport movements (ATMs) × average seats per movement × load factor × 2 (arrivals+departures counted once each). Heathrow operates near its ~480,000 ATM annual cap (~40,000/month); September ATMs × seats × load factor gives a capacity-based estimate.

Queries issued by the searcher: Heathrow monthly traffic statistics air transport movements September 2025; CAA Heathrow airport terminal passengers movements statistics 2025; Heathrow business and traffic commentary August 2026 air transport movements; Heathrow 2026 monthly traffic statistics passengers movements July 2026

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/13
  - p51 Heathrow total terminal passengers, September 2025 (000s) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p52 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p14.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p53 Heathrow total air transport movements, Jan to Sep 2025 (cumulative) = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Jan–Sep 2025 cumulative ATMs; redundant with monthly ATM points.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p54 Heathrow total air transport movements, Oct 2024 to Sep 2025 (rolling 12 months) = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Rolling 12-month ATMs to Sep 2025; redundant.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p55 Heathrow total terminal passengers, Jan to Sep 2025 (cumulative, 000s) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Jan–Sep 2025 cumulative passengers; redundant with p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p56 Heathrow total terminal passengers, Oct 2024 to Sep 2025 (rolling 12 months, 000 = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Rolling 12-month passengers to Sep 2025; redundant with p5.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p57 Heathrow passengers welcomed in September (nearly, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p58 Heathrow EU air transport movements, September 2025 = **18,090** air transport movements (2025-09-01..2025-09-30) [DISCARD: September 2025 EU ATMs; not needed for total-level methods.] quote: "\| EU \| 18,090 \| 1.7 \| 157,967 \| 1.6 \| 208,860 \| 1.9 \|"
  - p59 Heathrow North America air transport movements, September 2025 = **8,197** air transport movements (2025-09-01..2025-09-30) [DISCARD: September 2025 North America ATMs; not needed.] quote: "\| North America \| 8,197 \| 2.4 \| 69,522 \| 0.7 \| 91,548 \| -0.1 \|"
  - p60 Heathrow Asia/Pacific air transport movements, September 2025 = **3,588** air transport movements (2025-09-01..2025-09-30) [DISCARD: September 2025 Asia-Pacific ATMs; not needed.] quote: "\| Asia / Pacific \| 3,588 \| 1.8 \| 32,586 \| 0.8 \| 43,494 \| 0.6 \|"
  - p61 Heathrow UK air transport movements, September 2025 = **2,893** air transport movements (2025-09-01..2025-09-30) [DISCARD: September 2025 UK ATMs; not needed.] quote: "\| UK \| 2,893 \| -1.3 \| 27,541 \| 1.7 \| 37,605 \| 5.3 \|"
  - p62 Heathrow total air transport movements, September 2025, year-on-year % change = **0.5** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p15.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p63 Heathrow total terminal passengers, September 2025, year-on-year % change = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-aug-2026/9766701` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/media/i0amphka/cap3286-richmond-heathrow-campaign.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/publication/download/29889` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### d3 [related_series] UK CAA airport statistics compiler

Hypothesis: CAA publishes Heathrow terminal passenger totals monthly; September 2026 CAA figure should match Heathrow's own statistic. CAA 2025 September value and 2026 monthly pattern provide an independent cross-check and a bridge if Heathrow's own release is unavailable.

Queries issued by the searcher: CAA airport statistics Heathrow terminal passengers monthly; UK airport passenger numbers September 2025 Heathrow CAA; Heathrow business and traffic commentary July 2026 passengers; CAA "UK airport data" July 2026 Heathrow terminal passengers table 09

- `https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/uk-airport-data-2025/september-2025/` -> **snapshot** (snapshot 20260606080524); points raw/verified 2/2
  - p64 CAA data completeness status for September (year not stated in quote) = **1** day of month (2025-12-01..2025-12-01) [DISCARD: CAA data-completeness status with ambiguous year; adds no quantitative input.] quote: "As of 1 December 2025, September data is complete"
  - p65 Number of UK airports from which CAA collects statistics = **60** airports (not stated (page dated 2026-06-03)) [DISCARD: Number of UK airports CAA covers; irrelevant to Heathrow September 2026 level.] quote: "The CAA collects statistics from more than 60 UK Airports."
- `https://www.caa.co.uk/Documents/Download/24003/a90c0dd7-e580-4607-b1d9-0b4fc72566fc/17360` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p66 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p67 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p3/p55.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p68 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p5/p56.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p69 Heathrow total terminal passengers, September 2025 year-on-year % change = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2/p63.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p70 Heathrow total terminal passengers, Jan to Sep 2025 year-on-year % change = **0.3** % (2025-01-01..2025-09-30) [DISCARD: Duplicate of p4.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p71 Heathrow passengers in September (narrative, 'nearly 7.4 million') = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p72 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p73 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p74 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p75 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p76 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p77 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p78 Heathrow total air transport movements, Jan to Sep 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p53.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p79 Heathrow total air transport movements, September 2025 year-on-year % change = **0.5** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p15/p62.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-jul-2026/9714388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d4 [related_series] Airline and alliance capacity analyst

Hypothesis: Heathrow passengers ≈ sum over airlines of (seats offered × load factor). Major carriers (BA, Virgin, and foreign flag carriers) publish or are tracked for Heathrow seat capacity; aggregating scheduled seats for September 2026 and applying a load factor yields the total.

Queries issued by the searcher: Heathrow airport monthly traffic statistics September 2025 passengers; Heathrow scheduled seats summer 2026 airline seat capacity OAG; Heathrow traffic statistics August 2026 passengers record; OAG Heathrow departing seats September 2026 million

- `https://safariindia.com/heathrow-sees-strong-summer/` -> **snapshot** (snapshot 20260911133436); points raw/verified 15/15
  - p80 Heathrow total passengers, August 2026 (table, thousands) = **7,867,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p16.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p81 Heathrow total passengers, August 2026 (narrative, millions) = **7,800,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p43.] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p82 Heathrow total passengers, June–August 2026 (summer) = **23,000,000** passengers (2026-06-01..2026-08-31) [DISCARD: Duplicate of p18/p42.] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p83 Heathrow total passengers, Jan–Aug 2026 cumulative (table, thousands) = **55,721,000** passengers (2026-01-01..2026-08-31) [DISCARD: Duplicate of p19.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p84 Heathrow total passengers, Sep 2025–Aug 2026 rolling 12 months (table, thousands = **84,257,000** passengers (2025-09-01..2026-08-31) [DISCARD: Duplicate of p21.] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p85 Heathrow total air transport movements, August 2026 = **41,048** air transport movements (2026-08-01..2026-08-31) [DISCARD: Duplicate of p23.] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p86 Heathrow total air transport movements, Jan–Aug 2026 cumulative = **312,559** air transport movements (2026-01-01..2026-08-31) [DISCARD: Jan–Aug 2026 cumulative ATMs; not needed for passenger-level methods.] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p87 Heathrow total air transport movements, Sep 2025–Aug 2026 rolling 12 months = **472,617** air transport movements (2025-09-01..2026-08-31) [DISCARD: Rolling 12-month ATMs; not needed.] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p88 Heathrow busiest day passengers, 2 August 2026 = **272,000** passengers (2026-08-02..2026-08-02) [DISCARD: Duplicate of p25.] quote: "The airport also recorded its busiest day on 2 August, when nearly 272,000 passengers travelled through its terminals."
  - p89 Heathrow passengers, August 2026, North America market (table, thousands) = **1,975,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p47.] quote: "\| North America \| 1,975 \| -1.1 \| 13,783 \| 0.5 \| 20,626 \| 0.0 \|"
  - p90 Heathrow passengers, August 2026, EU market (table, thousands) = **2,835,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p46.] quote: "\| EU \| 2,835 \| -0.3 \| 19,161 \| 2.0 \| 28,793 \| 2.2 \|"
  - p91 Heathrow passengers, August 2026, Asia/Pacific market (table, thousands) = **989,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p28.] quote: "\| Asia / Pacific \| 989 \| 1.2 \| 7,826 \| 6.6 \| 11,505 \| 5.3 \|"
  - p92 Heathrow passengers, August 2026, Middle East market (table, thousands) = **668,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p26.] quote: "\| Middle East \| 668 \| -19.8 \| 4,367 \| -23.6 \| 7,429 \| -14.0 \|"
  - p93 Heathrow passengers, August 2026, UK market (table, thousands) = **390,000** passengers (2026-08-01..2026-08-31) [DISCARD: Duplicate of p45.] quote: "\| UK \| 390 \| -1.7 \| 3,008 \| 0.2 \| 4,596 \| 0.2 \|"
  - p94 Heathrow passengers, August 2026, Africa market (table, thousands) = **302,000** passengers (2026-08-01..2026-08-31) [DISCARD: Africa market August 2026; not needed for total-level methods.] quote: "\| Africa \| 302 \| 2.0 \| 2,325 \| 5.5 \| 3,508 \| 5.9 \|"
- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://aviationweek.com/air-transport/airports-networks/record-half-heathrow-driven-asia-pacific-growth` -> **snapshot** (snapshot 20260724232927); points raw/verified 15/12
  - p95 Heathrow total passengers, first half 2026 (record) = **40,000,000** passengers (2026-01-01..2026-06-30) [DISCARD: H1 2026 rounded 40m; superseded by precise Jan–Aug cumulative.] quote: "handled a record 40 million passengers in the first half of 2026"
  - p96 Heathrow overall passenger growth, first half 2026 vs prior year = **0.2** % (2026-01-01..2026-06-30) [DISCARD: H1 2026 +0.2%; superseded by Jan–Aug -0.4% for the target period.] quote: "Overall passenger numbers at the UK hub increased 0.2% from 39.9 million a year earlier."
  - p97 Heathrow transfer traffic growth, first half 2026 = **5.4** % (2026-01-01..2026-06-30) [DISCARD: Transfer traffic growth; no usable level for the target.] quote: "with transfer traffic rising 5.4% amid weaker demand to and from the Middle East"
  - p98 Scheduled departing seats offered from LHR, first half 2026 (OAG Schedules Analy = **25,300,000** departing seats (2026-01-01..2026-06-30) [DISCARD: H1 2026 seats; no route to September total.] quote: "airlines offered about 25.3 million departing seats from LHR during the first six months of 2026, down 1.4% year on year"
  - p99 LHR scheduled departing seat capacity change, first half 2026 vs prior year = **1.4** % (2026-01-01..2026-06-30) [DISCARD: H1 2026 seat change; not needed.] quote: "about 25.3 million departing seats from LHR during the first six months of 2026, down 1.4% year on year"
  - p100 LHR flight frequency change, first half 2026 vs prior year = **1.6** % (2026-01-01..2026-06-30) [DISCARD: H1 2026 frequency change; not needed.] quote: "Frequencies declined 1.6%, although the number of destinations served increased from 218 to 223"
  - p101 LHR destinations served, first half 2026 = **223** destinations (2026-01-01..2026-06-30) [DISCARD: Destination count; contextual only, no numeric role.] quote: "the number of destinations served increased from 218 to 223"
  - p102 LHR carrier count, first half 2026 = **83** carriers (2026-01-01..2026-06-30) [DISCARD: Carrier count; contextual only, no numeric role.] quote: "the carrier count rose from 76 to 83"
  - p103 LHR North America scheduled departing seats, first half 2026 = **6,170,000** departure seats (2026-01-01..2026-06-30) [DISCARD: H1 2026 North America seats; no route to September total.] quote: "North American capacity was broadly stable, declining 0.9% to about 6.17 million departure seats"
  - p104 LHR North America capacity change, first half 2026 vs prior year = **0.9** % (2026-01-01..2026-06-30) [DISCARD: H1 2026 North America capacity change; not needed.] quote: "North American capacity was broadly stable, declining 0.9% to about 6.17 million departure seats"
  - p105 LHR-Middle East capacity change, first half 2026 vs prior year = **16.5** % (2026-01-01..2026-06-30) [DISCARD: H1 2026 Middle East capacity change; superseded by August market data.] quote: "Capacity between Heathrow and the Middle East fell 16.5% due to the geopolitical crisis in the region."
  - p106 Heathrow average daily flights, week of July 13-19 2026 (Eurocontrol, fourth-bus = **1,331** flights per day (2026-07-13..2026-07-19) [DISCARD: Eurocontrol weekly average flights; redundant with monthly ATM data.] quote: "Heathrow ranked as the fourth-busiest airport with an average of 1,331 flights per day"
- `https://www.caa.co.uk/media/czmfoezz/airline-community-response-to-h8-ip_annex-skylark-report-passenger-forecasting-may-2026.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- dropped by code checks: 3 (period year 2025 does not appear in the page text or URL (likely mis-dated): 3)

### d5 [shocks] Operations and disruption monitor

Hypothesis: September 2026 passengers could deviate from trend due to strikes, ATC disruptions, weather, capacity caps, or new routes/airline failures. Identifying known scheduled disruptions or capacity changes before the cutoff adjusts the trend-based estimate up or down.

Queries issued by the searcher: Heathrow passenger guidance 2026 traffic statistics; Heathrow September 2026 strike disruption; Heathrow July 2026 passenger numbers million monthly traffic statistics; Heathrow September 2025 passengers record monthly traffic statistics

- `https://observatornews.ro/extern/cauza-haosului-cu-2000-de-zboruri-anulate-in-uk-un-document-militar-gresit-introdus-in-sistem-a-blocat-tot-665735.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.flightglobal.com/strategy/2026/06/heathrow-airport-braced-for-drop-in-passenger-numbers-this-year/` -> **snapshot** (snapshot 20260627080206); points raw/verified 12/8
  - p107 Heathrow passenger numbers in 2025 = **84,500,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 rounded 84.5m; superseded by p146.] quote: "a 1.1% fall on the 84.5 million it handled in 2025"
  - p108 Heathrow passenger numbers first five months of 2026 = **32,800,000** passengers (2026-01-01..2026-05-31) [DISCARD: Jan–May 2026 cumulative; superseded by Jan–Aug.] quote: "Heathrow passenger numbers over the first five months of the year are up 0.7% to 32.8 million"
  - p109 Heathrow passenger numbers change first five months of 2026 vs prior year = **0.7** % (2026-01-01..2026-05-31) [DISCARD: Jan–May 2026 YoY; superseded by Jan–Aug.] quote: "Heathrow passenger numbers over the first five months of the year are up 0.7% to 32.8 million"
  - p110 Heathrow overall passenger numbers change in April 2026 = **5** % (2026-04-01..2026-04-30) [DISCARD: April 2026 YoY; not needed for September forecast.] quote: "overall passenger numbers were down 5% in April and 1% in May"
  - p111 Heathrow overall passenger numbers change in May 2026 = **1** % (2026-05-01..2026-05-31) [DISCARD: May 2026 YoY; not needed.] quote: "overall passenger numbers were down 5% in April and 1% in May"
  - p112 Heathrow Middle East traffic reduction in April 2026 = **52** % (2026-04-01..2026-04-30) [DISCARD: April Middle East decline; not needed.] quote: "driven by a 52% and 31% reduction respectively in Middle East traffic"
  - p113 Heathrow Middle East traffic reduction in May 2026 = **31** % (2026-05-01..2026-05-31) [DISCARD: May Middle East decline; not needed.] quote: "driven by a 52% and 31% reduction respectively in Middle East traffic"
  - p114 Middle East share of Heathrow passenger numbers in 2025 (more than) = **10** % (2025-01-01..2025-12-31) [DISCARD: Middle East share >10% of 2025; superseded by monthly market levels.] quote: "accounting for more than 10% of its passenger numbers last year"
- `https://safariindia.com/heathrow-records-busiest-day-of-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bnrnews.bg/main/post/527414/danni-ot-voenen-samolet-sa-prichinili-transportniya-haos-vav-velikobritaniya` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 4)

### d6 [forecasts_markets] Airport and aviation forecasters

Hypothesis: Heathrow, IATA, ACI Europe, or Oxford Economics publish 2026 passenger forecasts or Heathrow guidance; a full-year 2026 forecast can be decomposed into months using 2025 monthly shares to isolate September.

Queries issued by the searcher: Heathrow 2026 passenger forecast guidance annual passengers outlook; ACI Europe 2026 passenger growth forecast; Heathrow monthly traffic statistics September 2025 passengers million; Heathrow Airport monthly traffic statistics 2026 July August passengers million

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/13
  - p115 Heathrow total passengers, September 2025 (all terminals, arrivals plus departur = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p116 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p117 Heathrow total terminal passengers, January to September 2025 cumulative (table, = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p118 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p5.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p119 Heathrow total passengers year-on-year % change, September 2025 = **0.8** percent (2025-09-01..2025-09-30) [DISCARD: Duplicate of p2.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p120 Heathrow EU market terminal passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p121 Heathrow North America market terminal passengers, September 2025 (table, thousa = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p122 Heathrow Asia/Pacific market terminal passengers, September 2025 (table, thousan = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p123 Heathrow Middle East market terminal passengers, September 2025 (table, thousand = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p124 Heathrow UK market terminal passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p125 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p77/p167 September 2025 ATM total.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p126 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p53.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p127 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: September 2025 cargo; irrelevant to passenger count.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.businesstravelnewseurope.com/Air-Travel/London-Heathrow-traffic-set-to-fall-in-2026-as-demand-softens-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://travelandtourworld.fr/news/article/m33pdcth22ra/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://travelweekly.co.uk/news/europes-airports-need-massive-investment-to-avoid-increasing-bottleneck` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### d7 [base_rates] Seasonal pattern analyst

Hypothesis: September's share of annual Heathrow passengers is stable (~8.0–8.5%); annual 2026 passengers × September share gives the monthly figure. This route needs the annual level and the seasonal share rather than monthly history.

Queries issued by the searcher: Heathrow annual passengers 2025 total record; Heathrow monthly traffic statistics passengers by month 2025; Heathrow September 2025 passengers busiest September record press release; Heathrow monthly traffic statistics 2024 passengers by month table January February March April May June July August September October November December

- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p128 Heathrow total passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p129 Heathrow total passengers, January to September 2025 (table, thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p3.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p130 Heathrow total passengers, October 2024 to September 2025 rolling 12 months (tab = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p5.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p131 Heathrow passengers in September (narrative, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p7.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p132 Heathrow passengers in September (CEO quote, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p8.] quote: "welcoming nearly 7.4 million passengers in September alone"
  - p133 Heathrow UK market passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p13.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p134 Heathrow EU market passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p9.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p135 Heathrow North America market passengers, September 2025 (table, thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p10.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p136 Heathrow Asia/Pacific market passengers, September 2025 (table, thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p11.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p137 Heathrow Middle East market passengers, September 2025 (table, thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p12.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p138 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p77/p167 September 2025 ATM total.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p139 Heathrow total air transport movements, January to September 2025 = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p53.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p140 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: September 2025 cargo; irrelevant to passenger count.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p141 Heathrow trade supported last year (GBP billions) = **215,000,000,000** GBP (2024-01-01..2024-12-31) [DISCARD: Trade value supported; irrelevant to passenger count.] quote: "As the UK's largest port by value, we helped drive over £215 billion in trade last year"
- `https://mediacentre.heathrow.com/pressrelease/detail/24843` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rte.ie/news/business/2025/1013/1538235-heathrow-airport-figures/` -> **snapshot** (snapshot 20251021024539); points raw/verified 10/4
  - p142 Heathrow current annual flight movements (today) = **480,000** flights per year (not stated (page dated 2025-10-13)) [DISCARD: Annual ATM cap; contextual, not needed for passenger-level methods.] quote: "which it said would enable an additional 276,000 flights per year, from 480,000 today to 756,000."
  - p143 Heathrow additional flights per year enabled by proposed third runway = **276,000** flights per year (not stated (page dated 2025-10-13)) [DISCARD: Third-runway additional flights; not applicable to 2026 operations.] quote: "which it said would enable an additional 276,000 flights per year, from 480,000 today to 756,000."
  - p144 Heathrow total flights per year with third runway = **756,000** flights per year (not stated (page dated 2025-10-13)) [DISCARD: Third-runway future capacity; not applicable to 2026.] quote: "which it said would enable an additional 276,000 flights per year, from 480,000 today to 756,000."
  - p145 Heathrow third runway expansion proposed private financing cost = **21,000,000,000** GBP (not stated (page dated 2025-10-13)) [DISCARD: Expansion financing cost; irrelevant.] quote: "It proposed that the expansion would be privately financed at a cost of £21 billion, but there are concerns over the impact on passenger charges."
- `https://mediacentre.heathrow.com/pressrelease/detail/24570` -> **snapshot** (snapshot 20260212174417); points raw/verified 13/12
  - p146 Heathrow total passengers, full year 2025 (Jan to Dec), all terminals = **84,463,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "\| Total \| 7,189 \| 1.6 \| 84,463 \| 0.7 \| 84,463 \| 0.7 \|"
  - p147 Heathrow total passengers, December 2025 = **7,189,000** passengers (2025-12-01..2025-12-31) [DISCARD: December 2025 level; not needed for September forecast.] quote: "\| Total \| 7,189 \| 1.6 \| 84,463 \| 0.7 \| 84,463 \| 0.7 \|"
  - p148 Heathrow annual passengers 2025 stated in text (surpassed for first time ever) = **84,000,000** passengers (2025-01-01..2025-12-31) [DISCARD: Rounded '84 million' 2025; superseded by precise p146.] quote: "Passenger numbers for the year surpassed 84 million for the first time ever"
  - p149 Heathrow passengers in December 2025 stated in text (busiest December on record) = **7,200,000** passengers (2025-12-01..2025-12-31) [DISCARD: December 2025 rounded; not needed.] quote: "we achieved our busiest December on record, with almost 7.2 million passengers travelling through the UK's hub"
  - p150 Heathrow busiest day ever passenger count, 1 August = **270,000** passengers (2025-08-01..2025-08-01) [DISCARD: Busiest day 1 Aug 2025; superseded by 2026 busiest-day points and not needed.] quote: "our busiest day ever on 1 August, when passenger numbers surpassed 270,000"
  - p151 Heathrow UK market passengers, full year 2025 (Jan to Dec) = **4,588,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 market split; not needed given monthly market data.] quote: "\| UK \| 397 \| -1.0 \| 4,588 \| -1.7 \| 4,588 \| -1.7 \|"
  - p152 Heathrow EU market passengers, full year 2025 (Jan to Dec) = **28,413,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 market split; not needed.] quote: "\| EU \| 2,291 \| 2.8 \| 28,413 \| 1.1 \| 28,413 \| 1.1 \|"
  - p153 Heathrow North America market passengers, full year 2025 (Jan to Dec) = **20,555,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 market split; not needed.] quote: "\| North America \| 1,656 \| -2.6 \| 20,555 \| -0.3 \| 20,555 \| -0.3 \|"
  - p154 Heathrow Asia/Pacific market passengers, full year 2025 (Jan to Dec) = **11,022,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 market split; not needed.] quote: "\| Asia / Pacific \| 966 \| 1.6 \| 11,022 \| 2.6 \| 11,022 \| 2.6 \|"
  - p155 Heathrow Middle East market passengers, full year 2025 (Jan to Dec) = **8,780,000** passengers (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 market split; not needed.] quote: "\| Middle East \| 865 \| 7.9 \| 8,780 \| 2.8 \| 8,780 \| 2.8 \|"
  - p156 Heathrow total air transport movements, full year 2025 (Jan to Dec) = **477,883** air transport movements (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 ATMs; not needed.] quote: "\| Total \| 39,903 \| 2.7 \| 477,883 \| 0.8 \| 477,883 \| 0.8 \|"
  - p157 Heathrow total passengers, full year 2025 year-on-year % change = **0.7** percent (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 YoY; not needed.] quote: "\| Total \| 7,189 \| 1.6 \| 84,463 \| 0.7 \| 84,463 \| 0.7 \|"
- dropped by code checks: 8 (period_end 2026-12-31 after as_of: 2; period_end 2026-09-30 after as_of: 5; period_end 2029-12-31 after as_of: 1)

### b1 [own_history] Heathrow monthly release

Hypothesis: A September 2026 Heathrow monthly traffic release (or a September 2025–August 2026 monthly table) would give the exact September 2025 base and any early-September 2026 partial data, anchoring the YoY-scaling route (m1) and reducing reliance on the rounded narrative.

Queries issued by the searcher: Heathrow monthly traffic statistics September 2025 passengers; Heathrow mediacentre traffic statistics August 2026; "Business and traffic commentary Aug 2026" Heathrow mediacentre; Heathrow traffic statistics monthly passengers 2026 January February March April May June July

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/13
  - p158 Heathrow total passengers, September 2025 (narrative, 'nearly 7.4 million') = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative duplicate of p1/p159 September 2025 total.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p159 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p160 Heathrow total terminal passengers, January to September 2025 cumulative (thousa = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Duplicate of p203 Jan–Sep 2025 cumulative.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p161 Heathrow total terminal passengers, October 2024 to September 2025 rolling 12 mo = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Duplicate of p204 rolling 12-month total.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p162 Heathrow EU market passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p208 EU September 2025.] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p163 Heathrow North America market passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p209 North America September 2025.] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p164 Heathrow Asia/Pacific market passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p210 Asia/Pacific September 2025.] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p165 Heathrow Middle East market passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p211 Middle East September 2025.] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p166 Heathrow UK market passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p212 UK September 2025.] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p167 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p168 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Duplicate of p206 Jan–Sep 2025 ATM cumulative.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p169 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Cargo tonnage, irrelevant to passenger target.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p170 Heathrow total cargo, January to September 2025 cumulative (metric tonnes) = **1,175,019** metric tonnes (2025-01-01..2025-09-30) [DISCARD: Cargo tonnage, irrelevant to passenger target.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.investegate.co.uk/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-aug-2026/9766701` -> **snapshot** (snapshot 20260911062239); points raw/verified 15/15
  - p171 Heathrow total terminal passengers, August 2026 (thousands) = **7,867,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p172 Heathrow total terminal passengers, January to August 2026 cumulative (thousands = **55,721,000** passengers (2026-01-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p173 Heathrow total terminal passengers, September 2025 to August 2026 rolling 12 mon = **84,257,000** passengers (2025-09-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p174 Heathrow total passengers, June to August 2026 summer period (millions) = **23,000,000** passengers (2026-06-01..2026-08-31) [keep: ] quote: "Heathrow ended the peak summer period with 23 million passengers choosing to fly through the UK's only hub in June to August."
  - p175 Heathrow passengers in August 2026 alone (millions) = **7,800,000** passengers (2026-08-01..2026-08-31) [DISCARD: Rounded narrative duplicate of p171 August 2026 level.] quote: "In August alone, 7.8m passengers were welcomed, including a busiest ever day on 2 August with nearly 272,000 passengers"
  - p176 Heathrow busiest ever day passengers, 2 August 2026 (nearly) = **272,000** passengers (2026-08-02..2026-08-02) [DISCARD: Single-day peak, not a monthly level; no role in monthly estimate.] quote: "including a busiest ever day on 2 August with nearly 272,000 passengers"
  - p177 Heathrow total terminal passengers, August 2026 year-on-year % change = **-2.1** % (2026-08-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p178 Heathrow total terminal passengers, January to August 2026 year-on-year % change = **-0.4** % (2026-01-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p179 Heathrow total terminal passengers, September 2025 to August 2026 year-on-year % = **0.3** % (2025-09-01..2026-08-31) [keep: ] quote: "\| \| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \| \|"
  - p180 Heathrow EU market terminal passengers, August 2026 (thousands) = **2,835,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| \| EU \| 2,835 \| -0.3 \| 19,161 \| 2.0 \| 28,793 \| 2.2 \| \|"
  - p181 Heathrow North America market terminal passengers, August 2026 (thousands) = **1,975,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| \| North America \| 1,975 \| -1.1 \| 13,783 \| 0.5 \| 20,626 \| 0.0 \| \|"
  - p182 Heathrow Asia/Pacific market terminal passengers, August 2026 (thousands) = **989,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| \| Asia / Pacific \| 989 \| 1.2 \| 7,826 \| 6.6 \| 11,505 \| 5.3 \| \|"
  - p183 Heathrow Middle East market terminal passengers, August 2026 (thousands) = **668,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| \| Middle East \| 668 \| -19.8 \| 4,367 \| -23.6 \| 7,429 \| -14.0 \| \|"
  - p184 Heathrow total air transport movements, August 2026 = **41,048** air transport movements (2026-08-01..2026-08-31) [keep: ] quote: "\| \| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \| \|"
  - p185 Heathrow total air transport movements, January to August 2026 cumulative = **312,559** air transport movements (2026-01-01..2026-08-31) [keep: ] quote: "\| \| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \| \|"
- `https://www.ticker.app/lse/XU82/rns/2026-08-11/Business-and-traffic-commentary-Jul-2026/0342Q` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### b2 [related_series] CAA airport statistics

Hypothesis: CAA monthly Heathrow terminal passenger data for 2025–2026 would provide an independent cross-check and a monthly series to fit the 2026 trend, resolving whether the -0.4% Jan–Aug trend or the -2.1% August trend better predicts September.

Queries issued by the searcher: CAA airport data Heathrow terminal passengers monthly 2026; UK CAA aviation statistics Heathrow monthly terminal passengers 2025; CAA "UK airport data" monthly 2026 Heathrow terminal passengers table 09; Heathrow September 2025 passenger numbers 7. million monthly traffic statistics

- `https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/uk-airport-data-2026/may-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/Documents/Download/26833/11a95c0b-983c-49fc-ba36-4599da419397/17750` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/25368` -> **snapshot** (snapshot 20260511072728); points raw/verified 15/15
  - p186 Heathrow total terminal passengers, April 2026 (all markets, arrivals plus depar = **6,721,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p187 Heathrow total terminal passengers, January to April 2026 cumulative = **25,646,000** passengers (2026-01-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p188 Heathrow total terminal passengers, May 2025 to April 2026 rolling 12 months = **84,763,000** passengers (2025-05-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p189 Heathrow total terminal passengers year-on-year change, April 2026 = **-5.3** % (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p190 Heathrow total terminal passengers year-on-year change, January to April 2026 cu = **1.2** % (2026-01-01..2026-04-30) [keep: ] quote: "\| Total \| \| 6,721 \| -5.3 \| 25,646 \| 1.2 \| 84,763 \| 0.9 \|"
  - p191 Heathrow April passenger numbers (narrative), April 2026 = **6,700,000** passengers (2026-04-01..2026-04-30) [DISCARD: Rounded narrative duplicate of p186 April 2026.] quote: "April passenger numbers decreased by 5% year on year to 6.7 million"
  - p192 Heathrow April passenger numbers year-on-year decrease (narrative), April 2026 = **5** % (2026-04-01..2026-04-30) [DISCARD: Rounded narrative duplicate of p189 April 2026 YoY.] quote: "April passenger numbers decreased by 5% year on year to 6.7 million"
  - p193 Heathrow transfer passenger demand year-on-year increase, April 2026 = **10** % (2026-04-01..2026-04-30) [keep: ] quote: "strong transfer passenger demand continuing into April with a 10% increase year on year"
  - p194 Heathrow UK market terminal passengers, April 2026 = **376,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| UK \| \| 376 \| -1.3 \| 1,455 \| 1.2 \| 4,605 \| -0.1 \|"
  - p195 Heathrow EU market terminal passengers, April 2026 = **2,413,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| EU \| \| 2,413 \| 0.1 \| 8,339 \| 3.8 \| 28,720 \| 2.5 \|"
  - p196 Heathrow North America market terminal passengers, April 2026 = **1,730,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| North America \| \| 1,730 \| -1.3 \| 5,926 \| 1.8 \| 20,660 \| -0.3 \|"
  - p197 Heathrow Middle East market terminal passengers, April 2026 = **360,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p198 Heathrow Middle East market terminal passengers year-on-year change, April 2026 = **-52.4** % (2026-04-01..2026-04-30) [keep: ] quote: "\| Middle East \| \| 360 \| -52.4 \| 2,159 \| -23.4 \| 8,120 \| -6.2 \|"
  - p199 Heathrow Asia / Pacific market terminal passengers, April 2026 = **949,000** passengers (2026-04-01..2026-04-30) [keep: ] quote: "\| Asia / Pacific \| \| 949 \| 5.6 \| 3,976 \| 10.6 \| 11,404 \| 4.9 \|"
  - p200 Heathrow total air transport movements, April 2026 = **38,496** air transport movements (2026-04-01..2026-04-30) [keep: ] quote: "\| Total \| \| 38,496 \| -4.6 \| 150,878 \| -1.5 \| 475,547 \| 0.1 \|"
- `https://whichterminal.co.uk/london-heathrow-airport/statistics` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [capacity_consumption] OAG/airline schedules

Hypothesis: September 2026 scheduled seat capacity and load factor at Heathrow would enable the capacity×utilisation route (d2/d4), providing an independent structural estimate and testing the trend-based forecast.

Queries issued by the searcher: OAG Heathrow September 2026 seat capacity; Heathrow monthly traffic statistics September 2025 passengers load factor; Heathrow load factor 2026 seats passengers "load factor" airport capacity; Heathrow September 2026 passengers traffic statistics

- `https://www.gulftoday.ae/business/2026/08/31/dubai-airport-ranked-first-globally-in-capacity-with-434-million-seats-during-september` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/14
  - p201 Heathrow total passengers, September (busiest September ever, 'nearly 7.4 millio = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative duplicate of p1/p159 September 2025.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p202 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate of p1/p159 September 2025 table total.] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p203 Heathrow total terminal passengers, Jan to Sep 2025 (table, thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p204 Heathrow total terminal passengers, Oct 2024 to Sep 2025 (table, thousands) = **84,065,000** passengers (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p205 Heathrow total air transport movements, September 2025 (table) = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Duplicate of p77/p167 September 2025 ATM total.] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p206 Heathrow total air transport movements, Jan to Sep 2025 (table) = **358,018** air transport movements (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p207 Heathrow total air transport movements, Oct 2024 to Sep 2025 (table) = **475,936** air transport movements (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p208 Heathrow EU terminal passengers, September 2025 (table, thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p209 Heathrow North America terminal passengers, September 2025 (table, thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p210 Heathrow Asia/Pacific terminal passengers, September 2025 (table, thousands) = **904,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p211 Heathrow Middle East terminal passengers, September 2025 (table, thousands) = **702,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p212 Heathrow UK terminal passengers, September 2025 (table, thousands) = **383,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p213 Heathrow total terminal passengers, September 2025, year-on-year % change (table = **0.8** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p214 Heathrow total air transport movements, September 2025, year-on-year % change (t = **0.5** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://www.caa.co.uk/media/hvmi0rb4/steer-h8-traffic-review-for-ips.pdf` -> **snapshot** (snapshot 20260711081541); points raw/verified 15/3
  - p215 Heathrow actual annual passengers 2024 = **83,900,000** passengers (2024-01-01..2024-12-31) [keep: ] quote: "83.9m passengers +5.9%"
  - p216 Heathrow actual annual PATMs 2024 = **471,280** passenger ATMs (2024-01-01..2024-12-31) [keep: ] quote: "In 2024 the airport served 471,280 PATMs, representing 99.6% of the pre-pandemic 2019 value."
  - p217 Heathrow approximate load factor 2024 = **80.7** % (2024-01-01..2024-12-31) [keep: ] quote: "2024 approximate Load Factor: 80.7%"
- `https://dmnews.co.uk/heathrow-passenger-numbers-fall-0-6-in-first-nine-months-of-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (period_end missing or unparseable: 1; scale word 'million' not supported by quote or table header: 3; period_end 2026-12-31 after as_of: 8; scale word 'thousand' not supported by quote or table header: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['heathrow passengers', 'lhr traffic', 'uk airport traffic']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p51', 'p66', 'p116', 'p128', 'p7', 'p8', 'p57', 'p71', 'p115', 'p131', 'p132'] All are the same Heathrow September 2025 total (~7.348m table; 'nearly 7.4m' narrative). Same underlying Heathrow release, so not independent; the table value p1 is the precise one to use.
- corroborating: ['p16', 'p36', 'p80', 'p43', 'p81'] August 2026 total: 7.867m table vs 7.8m rounded narrative; same Heathrow release reproduced by two outlets. Use table value.
- corroborating: ['p19', 'p38', 'p83'] Jan–Aug 2026 cumulative 55.72m, consistent across outlets; same source.
- corroborating: ['p21', 'p40', 'p84'] Trailing 12-month to Aug 2026 = 84.26m, consistent; same source.
- corroborating: ['p17', 'p37'] August 2026 YoY -2.1%, consistent.
- corroborating: ['p23', 'p85'] August 2026 ATMs 41,048, consistent.
- corroborating: ['p25', 'p44', 'p88'] Busiest day 2 Aug 2026 ~272k, consistent.
- corroborating: ['p26', 'p92', 'p48'] Middle East Aug 2026 668k, -19.8%, consistent.
- corroborating: ['p28', 'p91', 'p49'] Asia-Pacific Aug 2026 989k, +1.2%; Jan–Aug +6.6%, consistent.
- corroborating: ['p31', 'p32'] July 2026 7.9m, -1.5% YoY; consistent with the weak 2026 trend.
- conflicting: ['p107', 'p146'] Full-year 2025: 84.5m (FlightGlobal) vs 84.463m (Heathrow table). Minor rounding/vintage difference; Heathrow table preferred.
- conflicting: ['p108', 'p109'] Jan–May 2026 +0.7% (FlightGlobal, June snapshot) vs Jan–Aug 2026 -0.4% (later release). Not a contradiction: different periods and the trend deteriorated in June–August; later data supersedes for the 
- corroborating: ['p110', 'p111', 'p112', 'p113'] April/May 2026 declines driven by Middle East traffic collapse; consistent with p26/p48 and p105.
- corroborating: ['p98', 'p99', 'p100'] H1 2026 seat capacity -1.4%, frequencies -1.6%; consistent with the modest passenger decline.
- corroborating: ['p14', 'p52', 'p77', 'p125', 'p138'] September 2025 ATMs 40,193, same Heathrow release.
- corroborating: ['p142', 'p156'] ~480k annual ATM cap vs 477,883 actual 2025 ATMs; consistent with near-cap operation.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p159', 'p202'] All three are the same Heathrow September 2025 table total (7,348 thousand); identical underlying measurement, not independent confirmation.
- corroborating: ['p158', 'p201'] Narrative 'nearly 7.4 million' for September 2025 rounds the same table figure; consistent but same source.
- corroborating: ['p16', 'p171', 'p175', 'p177'] August 2026 level ~7.87m and -2.1% YoY agree across travelwires and the Investegate release; same Heathrow release underlying both.
- corroborating: ['p19', 'p172', 'p178'] Jan–Aug 2026 cumulative 55.72m and -0.4% YoY agree; same release.
- corroborating: ['p21', 'p173', 'p179'] Trailing 12-month to Aug 2026 84.26m, +0.3% agree; same release.
- corroborating: ['p77', 'p125', 'p138', 'p167', 'p205'] Duplicate copies of September 2025 ATM total 40,193; one measurement.
- corroborating: ['p146', 'p215'] Heathrow 2025 annual 84.46m vs CAA 2024 83.9m; different years but consistent growth path.
- corroborating: ['p186', 'p189', 'p191', 'p192'] April 2026 6.72m and -5.3% YoY agree between table and narrative.
- corroborating: ['p183', 'p197', 'p198'] Middle East weakness (April -52%, August -20%) is a consistent regional shock, not a contradiction.
- corroborating: ['p1', 'p146'] September 2025 7.348m is ~8.7% of full-year 2025 84.463m, consistent with a stable September share.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY change factor vs September 2025 | 0.985 | 0.95..1.02 | 0.8805..1.101 (widened) | ratio | m1 (m1), m3 (m3) | Jan–Aug 2026 was -0.4% YoY (p178) but August deteriorated to -2.1% (p177), driven by Middle East weakness (p183). September 2025 was a record base (p1). A modest decline slightly worse than the 8-month average but not as steep as August is the central case; range spans flat-to-soft recovery and cont | September 2026 traffic follows the recent 2026 trend rather than a new shock. | Evidence of a sharp capacity cut, strike, or ATC closure in September 2026, or a rebound in Middle East traffic. |
| a2 | September share of annual passengers | 0.087 | 0.082..0.092 | 0.06142..0.1228 (widened) | ratio | m2 (m2) | September 2025 (7.348m, p1) was ~8.7% of full-year 2025 (84.463m, p146); September is a stable shoulder-season month, so the same share applied to a 2026 annual level is a reasonable seasonal decomposition. | September's seasonal share of the year is stable between 2025 and 2026. | Evidence that September 2026 demand is materially more or less seasonal than 2025. |
| a3 | September 2026 annual passenger level factor vs 2025 | 0.995 | 0.97..1.02 | 0.7033..1.407 (widened) | ratio | m2 (m2) | Trailing 12-month to Aug 2026 was +0.3% (p179) but recent months turned negative (p177); a roughly flat full-year 2026 vs 2025 is the central case. | Full-year 2026 passengers are close to 2025. | Evidence of a large full-year 2026 shortfall or surge. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,240,847 | ['p1'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 7,289,951 | ['p146'] / ['a2', 'a3'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 7,586,859 | ['p77', 'p171', 'p184'] / ['a1'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **7,370,982** person, 80% interval [4,369,056, 12,435,493] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total passengers at London Heathrow Airport (all terminals, arrivals plus departures, domestic and international) during September 2026: 7,370,982 person (80% model-based interval 4,369,056 to 12,435,493 person). This is a forecast; the month is future relative to the cutoff and unreported.

Evidence: September 2025 throughput was 7,348,000 passengers; full-year 2025 was 84,463,000 passengers; September 2025 movements were 40,193 air transport movements. August 2026 gave 7,867,000 passengers passengers on 41,048 air transport movements. Three methods were averaged at equal weights (33%, 33%, 33%): a YoY trend on the September 2025 base (7,240,847), a seasonal-share route (7,289,951), and a capacity/load cross-check (7,586,859).

Observed inputs are the historical points; the YoY factor 0.985, September share 0.087, and annual level factor 0.995 are analyst assumptions. The interval is conditional on these assumptions, not a demonstrated accuracy guarantee.

Main risk: an unanticipated September shock or a shift in September's seasonal share. Better evidence would be early-September 2026 weekly traffic and booking data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY change factor vs September 2025: 0.985 ratio, range 0.8805 to 1.101 (range widened by code); used by m1, m3. Overturned by: Evidence of a sharp capacity cut, strike, or ATC closure in September 2026, or a rebound in Middle East traffic.
- a2 September share of annual passengers: 0.087 ratio, range 0.06142 to 0.1228 (range widened by code); used by m2. Overturned by: Evidence that September 2026 demand is materially more or less seasonal than 2025.
- a3 September 2026 annual passenger level factor vs 2025: 0.995 ratio, range 0.7033 to 1.407 (range widened by code); used by m2. Overturned by: Evidence of a large full-year 2026 shortfall or surge.

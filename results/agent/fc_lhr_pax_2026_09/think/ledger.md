# Evidence ledger: fc_lhr_pax_2026_09

- Question: Assume today is 2026-09-12. You know nothing published after this date. Estimate the number of passengers at London Heathrow Airport in September 2026, as reported in Heathrow's monthly traffic statistics.
- as_of: 2026-09-12
- Pinned target: Total passengers counted at London Heathrow Airport in Heathrow's published monthly traffic statistics for the calendar month of September 2026 | unit passengers | period 2026-09-01..2026-09-30 | publisher Heathrow Airport Limited / Heathrow Airport Holdings (Heathrow monthly traffic statistics)

- Official value (scoring only, never shown to the agent): 7,180,000

## Directions and pages

### d1 [own_history] Heathrow monthly traffic statistics publisher

Hypothesis: September 2026 passengers should be anchored by previous September levels, adjusted by 2026 year-to-date growth and the normal September-to-August seasonal ratio; published adjacent 2026 months constrain the current level.

Queries issued by the searcher: Heathrow monthly traffic statistics passengers September 2025; Heathrow Airport monthly traffic statistics 2026 passengers July August; Heathrow "business and traffic commentary" August 2026 7,867 passengers; Heathrow September 2024 passengers 7.29 million record September

- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-aug-2026/9766701` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p1 Heathrow total passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p2 Heathrow total passengers, September 2025 year-on-year % change = **0.8** percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p3 Heathrow total passengers, January to September 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p4 Heathrow total passengers, October 2024 to September 2025 rolling 12 months (tho = **84,065,000** passengers (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p5 Heathrow passengers, September 2025 (narrative, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Rounded narrative duplicate of p1; same underlying Heathrow September 2025 total but less precise.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p6 Heathrow passengers, September 2025 (CEO quote, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Duplicate narrative/CEO rounding of September 2025 passengers; p5 already captures the rounded check and p1 is precise.] quote: "welcoming nearly 7.4 million passengers in September alone"
  - p7 Heathrow UK market passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p8 Heathrow EU market passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p9 Heathrow Non-EU Europe market passengers, September 2025 (thousands) = **459,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Non-EU Europe \| 459 \| -1.9 \| 4,170 \| -2.7 \| 5,535 \| -1.8 \|"
  - p10 Heathrow Africa market passengers, September 2025 (thousands) = **277,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Africa \| 277 \| 5.1 \| 2,481 \| 0.3 \| 3,326 \| -1.4 \|"
  - p11 Heathrow North America market passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p12 Heathrow Latin America market passengers, September 2025 (thousands) = **165,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Latin America \| 165 \| -3.8 \| 1,622 \| 0.6 \| 2,211 \| 3.7 \|"
  - p13 Heathrow Middle East market passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p14 Heathrow Asia / Pacific market passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [keep: ] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p15 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
- `https://dmnews.co.uk/heathrow-handles-23-million-passengers-during-summer-peak/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.borsaitaliana.it/borsa/notizie/radiocor/finance/dettaglio/heathrow-aug-passenger-traffic-7867-mln-down-21-yryr-nRC_11092026_0854_166647343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [capacity_consumption] airline schedule and seat-capacity data provider such as OAG, Cirium, or ACL

Hypothesis: September 2026 passengers are approximately total scheduled seats on all Heathrow arrivals and departures in the month multiplied by achieved load factor, adjusted for cancellations and the airport's passenger definition; schedules for September are largely known before the cutoff.

Queries issued by the searcher: Heathrow September 2026 scheduled seat capacity OAG; Heathrow monthly traffic statistics 2025 passengers September; Heathrow seat factor load factor 2026 passengers per ATM OAG scheduled seats both directions; Heathrow traffic statistics August 2026 passengers monthly

- `https://www.gulftoday.ae/business/2026/08/31/dubai-airport-ranked-first-globally-in-capacity-with-434-million-seats-during-september` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p16 Heathrow total passengers, September (stated as 'last month', nearly 7.4 million = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p5's rounded September 2025 narrative.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p17 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p1 (same September 2025 Heathrow table total).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p18 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p3 (January-September 2025 cumulative passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p19 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Redundant duplicate of p4 (October 2024-September 2025 rolling passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p20 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p15 (September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p21 Heathrow total air transport movements, Jan to Sep 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p22 Heathrow total air transport movements, Oct 2024 to Sep 2025 rolling 12 months = **475,936** air transport movements (2024-10-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p23 Heathrow total terminal passengers, September 2025, year-on-year % change = **0.8** % (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p2 (September 2025 passenger year-on-year change).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p24 Heathrow total air transport movements, September 2025, year-on-year % change = **0.5** % (2025-09-01..2025-09-30) [keep: ] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p25 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p8 (September 2025 EU market passengers).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p26 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p11 (September 2025 North America market passengers).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p27 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p14 (September 2025 Asia/Pacific market passengers).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p28 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p13 (September 2025 Middle East market passengers).] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p29 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p7 (September 2025 UK market passengers).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p30 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Cargo tonnage, irrelevant to the passenger target.] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.heathrow.com/content/dam/heathrow/web/common/documents/company/about/economic-regulation/heathrow_response_to_caa_%20proposals.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://aviationweek.com/air-transport/airports-networks/record-half-heathrow-driven-asia-pacific-growth` -> **snapshot** (snapshot 20260724232927); points raw/verified 15/13
  - p31 Heathrow departing seats offered by airlines, first half 2026 (OAG Schedules Ana = **25,300,000** departing seats (2026-01-01..2026-06-30) [keep: ] quote: "OAG Schedules Analyser data shows airlines offered about 25.3 million departing seats from LHR during the first six months of 2026, down 1.4% year on year."
  - p32 Year-on-year change in Heathrow departing seats, first half 2026 = **1.4** % (2026-01-01..2026-06-30) [keep: ] quote: "OAG Schedules Analyser data shows airlines offered about 25.3 million departing seats from LHR during the first six months of 2026, down 1.4% year on year."
  - p33 Year-on-year change in Heathrow flight frequencies, first half 2026 = **1.6** % (2026-01-01..2026-06-30) [keep: ] quote: "Frequencies declined 1.6%, although the number of destinations served increased from 218 to 223 and the carrier count rose from 76 to 83."
  - p34 Heathrow North American scheduled capacity, first half 2026 (departure seats) = **6,170,000** departure seats (2026-01-01..2026-06-30) [keep: ] quote: "North American capacity was broadly stable, declining 0.9% to about 6.17 million departure seats."
  - p35 Year-on-year change in Heathrow North American capacity, first half 2026 = **0.9** % (2026-01-01..2026-06-30) [keep: ] quote: "North American capacity was broadly stable, declining 0.9% to about 6.17 million departure seats."
  - p36 Year-on-year change in Heathrow-Middle East capacity, first half 2026 = **16.5** % (2026-01-01..2026-06-30) [keep: ] quote: "Capacity between Heathrow and the Middle East fell 16.5% due to the geopolitical crisis in the region."
  - p37 Year-on-year change in Heathrow Asia-Pacific scheduled capacity, first half 2026 = **6.7** % (2026-01-01..2026-06-30) [keep: ] quote: "By contrast, Heathrow's scheduled Asia-Pacific capacity increased 6.7% as airlines added more nonstop Europe-Asia flights amid disruption to connecting traffic through the Middle East."
  - p38 Heathrow total passengers, first half 2026 (record) = **40,000,000** passengers (2026-01-01..2026-06-30) [keep: ] quote: "London Heathrow Airport (LHR) handled a record 40 million passengers in the first half of 2026, with transfer traffic rising 5.4% amid weaker demand to and from the Middle East."
  - p39 Year-on-year change in Heathrow total passengers, first half 2026 = **0.2** % (2026-01-01..2026-06-30) [keep: ] quote: "Overall passenger numbers at the UK hub increased 0.2% from 39.9 million a year earlier."
  - p40 Year-on-year change in Heathrow transfer traffic, first half 2026 = **5.4** % (2026-01-01..2026-06-30) [keep: ] quote: "London Heathrow Airport (LHR) handled a record 40 million passengers in the first half of 2026, with transfer traffic rising 5.4% amid weaker demand to and from the Middle East."
  - p41 Eurocontrol network average daily flights, week of July 13-19 2026 = **36,201** flights per day (2026-07-13..2026-07-19) [DISCARD: Eurocontrol network daily flights, not Heathrow-specific and not used in any passenger route.] quote: "Eurocontrol recorded an average of 36,201 daily flights across its network during the week of July 13-19, up 1.9% year on year."
  - p42 Year-on-year change in Eurocontrol network daily flights, week of July 13-19 202 = **1.9** % (2026-07-13..2026-07-19) [DISCARD: Eurocontrol network flight growth, not Heathrow-specific and not used.] quote: "Eurocontrol recorded an average of 36,201 daily flights across its network during the week of July 13-19, up 1.9% year on year."
  - p43 UK average daily arrivals and departures, week of July 13-19 2026, Eurocontrol = **6,523** arrivals and departures per day (2026-07-13..2026-07-19) [keep: ] quote: "The UK was Europe's busiest state, with 6,523 daily arrivals and departures, while Heathrow ranked as the fourth-busiest airport with an average of 1,331 flights per day."
- dropped by code checks: 2 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d3 [related_series] UK Civil Aviation Authority airport statistics compiler

Hypothesis: CAA monthly airport data for Heathrow provides an independent passenger series that can validate or fill gaps in Heathrow's own history after aligning terminal/transit definitions and reporting periods.

Queries issued by the searcher: CAA airport data Heathrow monthly terminal passengers 2026; Heathrow monthly traffic statistics September 2025 passengers; Heathrow business and traffic commentary July 2026 passengers million; CAA UK airport data table 09 terminal transit passengers Heathrow 2026 monthly

- `https://www.caa.co.uk/Documents/Download/26833/11a95c0b-983c-49fc-ba36-4599da419397/17750` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/12
  - p44 Heathrow total terminal passengers, September 2025 (table, thousands) = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p1 (same September 2025 Heathrow table total).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p45 Heathrow passengers welcomed in September (narrative, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p5's rounded September 2025 narrative.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever"
  - p46 Heathrow passengers welcomed in September (CEO quote, millions) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p5's rounded September 2025 narrative.] quote: "welcoming nearly 7.4 million passengers in September alone"
  - p47 Heathrow total terminal passengers, Jan to Sep 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p3 (January-September 2025 cumulative passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p48 Heathrow total terminal passengers, Oct 2024 to Sep 2025 rolling 12 months (thou = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Redundant duplicate of p4 (rolling 12-month passengers to September 2025).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p49 Heathrow EU terminal passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p8 (September 2025 EU market passengers).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p50 Heathrow North America terminal passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p11 (September 2025 North America market passengers).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p51 Heathrow Asia/Pacific terminal passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p14 (September 2025 Asia/Pacific market passengers).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p52 Heathrow Middle East terminal passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p13 (September 2025 Middle East market passengers).] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p53 Heathrow UK terminal passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p7 (September 2025 UK market passengers).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p54 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p15 (September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p55 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p30 (September 2025 cargo).] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-jul-2026/9714388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://whichterminal.co.uk/london-heathrow-airport/statistics` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period_end missing or unparseable: 2; scale word 'billion' not supported by quote or table header: 1)

### d4 [physical_flow] air traffic and airport operations analyst

Hypothesis: Monthly passengers are approximately air transport movements multiplied by average passengers per ATM; Heathrow movement counts, ACL/NATS schedules, and historical passengers per movement provide a flow-based cross-check.

Queries issued by the searcher: Heathrow monthly traffic statistics air transport movements passengers 2025; Heathrow airport traffic statistics August 2026 passengers; Heathrow September 2026 flight schedule slots ACL movements planned; Heathrow annual air transport movement cap 480,000 2026

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.enginecowl.com/qatar-air-france-slot-swap-lhr/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://safariindia.com/heathrow-sees-strong-summer/` -> **snapshot** (snapshot 20260911133436); points raw/verified 15/11
  - p56 Heathrow total passengers, August 2026 (table, thousands) = **7,867,000** passengers (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p57 Heathrow total passengers, Jan–Aug 2026 cumulative (table, thousands) = **55,721,000** passengers (2026-01-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p58 Heathrow total passengers, Sep 2025–Aug 2026 rolling 12 months (table, thousands = **84,257,000** passengers (2025-09-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p59 Heathrow total air transport movements, August 2026 (table) = **41,048** air transport movements (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p60 Heathrow total air transport movements, Jan–Aug 2026 cumulative (table) = **312,559** air transport movements (2026-01-01..2026-08-31) [keep: ] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p61 Heathrow total air transport movements, Sep 2025–Aug 2026 rolling 12 months (tab = **472,617** air transport movements (2025-09-01..2026-08-31) [keep: ] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p62 Heathrow passengers over summer (June–August 2026) = **23,000,000** passengers (2026-06-01..2026-08-31) [keep: ] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p63 Heathrow passengers in August 2026 (narrative) = **7,800,000** passengers (2026-08-01..2026-08-31) [DISCARD: Rounded narrative duplicate of p56 (August 2026 passenger total); p56 is the precise table value.] quote: "Heathrow recorded 23 million passengers between June and August 2026, with 7.8 million passengers travelling through the airport in August alone."
  - p64 Heathrow busiest day passengers, 2 August 2026 = **272,000** passengers (2026-08-02..2026-08-02) [keep: ] quote: "The airport also recorded its busiest day on 2 August, when nearly 272,000 passengers travelled through its terminals."
  - p65 Heathrow share of passengers waiting less than five minutes at security, summer  = **98** % (2026-06-01..2026-08-31) [DISCARD: Security wait metric, not a passenger count and not used in any passenger-estimation route.] quote: "Heathrow said 98% of passengers waited less than five minutes at security, while 98% of bags departed as planned."
  - p66 Heathrow share of bags departing as planned, summer 2026 = **98** % (2026-06-01..2026-08-31) [DISCARD: Baggage performance metric, not a passenger count and not used in any passenger-estimation route.] quote: "Heathrow said 98% of passengers waited less than five minutes at security, while 98% of bags departed as planned."
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### d5 [base_rates] air travel demand seasonality analyst

Hypothesis: September is a transition month after the summer peak; historical September/August and September/July passenger ratios plus calendar effects such as school return, business travel resumption, and bank holidays can transfer the 2026 August level into September.

Queries issued by the searcher: Heathrow monthly passenger statistics September 2024 2023 2019 annual traffic; Heathrow passengers September 2025 traffic figures record; Heathrow August 2026 passengers traffic figures monthly; "Heathrow" traffic statistics monthly passengers table 2015 2016 2017 2018 2019 September August

- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/15
  - p67 Heathrow total passengers, September 2025 (monthly traffic statistics, thousands = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p1 (September 2025 Heathrow table total).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p68 Heathrow total passengers, September 2025, as stated in narrative (nearly, milli = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p5's rounded September 2025 narrative.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever and rounding off a record-breaking summer."
  - p69 Heathrow total passengers, January to September 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p3 (January-September 2025 cumulative passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p70 Heathrow total passengers, October 2024 to September 2025 rolling 12 months (tho = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Redundant duplicate of p4 (rolling 12-month passengers to September 2025).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p71 Heathrow total passengers, September 2025, year-on-year % change = **0.8** percent (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p2 (September 2025 passenger year-on-year change).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p72 Heathrow EU market passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p8 (September 2025 EU market passengers).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p73 Heathrow North America market passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p11 (September 2025 North America market passengers).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p74 Heathrow Asia/Pacific market passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p14 (September 2025 Asia/Pacific market passengers).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p75 Heathrow Middle East market passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p13 (September 2025 Middle East market passengers).] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p76 Heathrow UK market passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p7 (September 2025 UK market passengers).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p77 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p15 (September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p78 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p21 (January-September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p79 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p30 (September 2025 cargo).] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
  - p80 Share of Heathrow passengers waiting less than five minutes in security = **95** % (..) [DISCARD: Older security wait metric, not a passenger count and not used in any route.] quote: "Security performance also remained consistent, with 95% of passengers waiting less than five minutes in security, underscoring our focus on efficiency and customer experience."
  - p81 Heathrow trade facilitated last year (GBP, billions) = **215,000,000,000** GBP (..) [DISCARD: Trade value metric, not a passenger count and not convertible to September 2026 passengers.] quote: "As the UK's largest port by value, we helped drive over £215 billion in trade last year, connecting businesses to global markets"
- `https://es.investing.com/news/company-news/heathrow-registra-78-millones-de-pasajeros-en-agosto-en-plena-expansion-93CH-3831037` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://londonheathrowairportguide.com/zh-hans/statistics/` -> **snapshot** (snapshot 20250902110959); points raw/verified 0/0

### d6 [forecasts_markets] Heathrow, airline, and aviation industry outlook

Hypothesis: Heathrow or industry annual 2026 passenger guidance, allocated with historical monthly shares, gives an independent level check; airline capacity guidance for London/UK in Q3 2026 may constrain September activity.

Queries issued by the searcher: Heathrow 2026 passenger forecast guidance annual passengers outlook; IATA Europe passenger forecast 2026 UK air travel growth; Heathrow monthly traffic statistics September 2025 passengers 7.7 million; IAG second quarter 2026 results capacity guidance full year capacity growth outlook

- `https://www.flightglobal.com/strategy/2026/06/heathrow-airport-braced-for-drop-in-passenger-numbers-this-year/` -> **snapshot** (snapshot 20260627080206); points raw/verified 12/8
  - p82 Heathrow 2025 annual passenger numbers (prior year actual) = **84,500,000** passengers (2025-01-01..2025-12-31) [keep: ] quote: "a 1.1% fall on the 84.5 million it handled in 2025"
  - p83 Heathrow passenger numbers first five months of 2026 (cumulative) = **32,800,000** passengers (2026-01-01..2026-05-31) [keep: ] quote: "Heathrow passenger numbers over the first five months of the year are up 0.7% to 32.8 million"
  - p84 Heathrow passenger numbers first five months of 2026 percentage change = **0.7** % (2026-01-01..2026-05-31) [keep: ] quote: "over the first five months of the year are up 0.7% to 32.8 million"
  - p85 Heathrow overall passenger numbers change in April 2026 = **5** % (2026-04-01..2026-04-30) [keep: ] quote: "overall passenger numbers were down 5% in April"
  - p86 Heathrow overall passenger numbers change in May 2026 = **1** % (2026-05-01..2026-05-31) [keep: ] quote: "and 1% in May"
  - p87 Heathrow Middle East traffic reduction in April 2026 = **52** % (2026-04-01..2026-04-30) [keep: ] quote: "driven by a 52% and 31% reduction respectively in Middle East traffic"
  - p88 Heathrow Middle East traffic reduction in May 2026 = **31** % (2026-05-01..2026-05-31) [keep: ] quote: "driven by a 52% and 31% reduction respectively in Middle East traffic"
  - p89 Middle East share of Heathrow passenger numbers in 2025 (lower bound of 'more th = **10** % (2025-01-01..2025-12-31) [keep: ] quote: "accounting for more than 10% of its passenger numbers last year"
- `https://mediacentre.heathrow.com/pressrelease/detail/24006` -> **snapshot** (snapshot 20251026161245); points raw/verified 15/13
  - p90 Heathrow total passengers, September 2025 (monthly traffic statistics, thousands = **7,348,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p1 (September 2025 Heathrow table total).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p91 Heathrow total passengers, January to September 2025 cumulative (thousands) = **63,275,000** passengers (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p3 (January-September 2025 cumulative passengers).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p92 Heathrow total passengers, October 2024 to September 2025 rolling 12 months (tho = **84,065,000** passengers (2024-10-01..2025-09-30) [DISCARD: Redundant duplicate of p4 (rolling 12-month passengers to September 2025).] quote: "\| Total \| 7,348 \| 0.8 \| 63,275 \| 0.3 \| 84,065 \| 1.5 \|"
  - p93 Heathrow passengers described as 'nearly 7.4 million' in September (narrative) = **7,400,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p5's rounded September 2025 narrative.] quote: "Heathrow welcomed nearly 7.4 million passengers last month, making it our busiest September ever and rounding off a record-breaking summer."
  - p94 Heathrow total air transport movements, September 2025 = **40,193** air transport movements (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p15 (September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p95 Heathrow total air transport movements, January to September 2025 cumulative = **358,018** air transport movements (2025-01-01..2025-09-30) [DISCARD: Redundant duplicate of p21 (January-September 2025 air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p96 Heathrow total air transport movements, October 2024 to September 2025 rolling 1 = **475,936** air transport movements (2024-10-01..2025-09-30) [DISCARD: Redundant duplicate of p22 (rolling 12-month air transport movements).] quote: "\| Total \| 40,193 \| 0.5 \| 358,018 \| 0.6 \| 475,936 \| 0.9 \|"
  - p97 Heathrow EU market passengers, September 2025 (thousands) = **2,599,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p8 (September 2025 EU market passengers).] quote: "\| EU \| 2,599 \| 2.5 \| 21,381 \| 0.6 \| 28,230 \| 2.0 \|"
  - p98 Heathrow North America market passengers, September 2025 (thousands) = **1,859,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p11 (September 2025 North America market passengers).] quote: "\| North America \| 1,859 \| -0.6 \| 15,572 \| -0.1 \| 20,607 \| 0.7 \|"
  - p99 Heathrow Asia/Pacific market passengers, September 2025 (thousands) = **904,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p14 (September 2025 Asia/Pacific market passengers).] quote: "\| Asia / Pacific \| 904 \| 1.2 \| 8,248 \| 2.3 \| 10,936 \| 3.3 \|"
  - p100 Heathrow Middle East market passengers, September 2025 (thousands) = **702,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p13 (September 2025 Middle East market passengers).] quote: "\| Middle East \| 702 \| -0.7 \| 6,419 \| 1.4 \| 8,631 \| 2.4 \|"
  - p101 Heathrow UK market passengers, September 2025 (thousands) = **383,000** passengers (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p7 (September 2025 UK market passengers).] quote: "\| UK \| 383 \| 1.2 \| 3,383 \| -2.2 \| 4,589 \| 0.6 \|"
  - p102 Heathrow total cargo, September 2025 (metric tonnes) = **124,637** metric tonnes (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p30 (September 2025 cargo).] quote: "\| Total \| 124,637 \| -2.3 \| 1,175,019 \| 1.8 \| 1,601,195 \| 2.6 \|"
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.iata.org/en/iata-repository/publications/economic-reports/quarterly-air-transport-chartbook-q4-2025/` -> **snapshot** (snapshot 20260406013019); points raw/verified 15/15
  - p103 IATA global scheduled seat capacity growth forecast, Q1 2026, YoY = **3.3** % (2026-01-01..2026-03-31) [DISCARD: Global seat-capacity forecast; not Heathrow-specific September evidence.] quote: "Global scheduled seat capacity is forecast to grow by 3.3% YoY in Q1 2026, moderating slightly from 3.7% YoY in Q4 2025 (Chart 17)."
  - p104 IATA global scheduled seat capacity growth, Q4 2025, YoY = **3.7** % (2025-10-01..2025-12-31) [DISCARD: Global seat-capacity growth; not Heathrow-specific.] quote: "Global scheduled seat capacity is forecast to grow by 3.3% YoY in Q1 2026, moderating slightly from 3.7% YoY in Q4 2025 (Chart 17)."
  - p105 Europe scheduled seat capacity growth forecast, Q1 2026, YoY = **4.8** % (2026-01-01..2026-03-31) [DISCARD: Europe seat-capacity forecast; too broad for Heathrow September.] quote: "The Middle East is set to lead with a 6.1% YoY increase, followed by Africa at 5.3% YoY and Europe at 4.8% YoY."
  - p106 UK scheduled seat capacity growth forecast, Q1 2026, YoY (largest market in Euro = **1.7** % (2026-01-01..2026-03-31) [DISCARD: UK Q1 2026 seat-capacity forecast, not Heathrow September; superseded by Heathrow-specific H1 seat data p31/p32.] quote: "In Q1 2026, the seat schedule for the UK, which is the largest market in Europe, is expected to increase by 1.7% YoY (Chart 46)."
  - p107 European carriers passenger traffic (RPK) growth, Q4 2025, YoY = **6.6** % (2025-10-01..2025-12-31) [DISCARD: European carriers RPK growth; not Heathrow-specific.] quote: "In Q4 2025, passenger demand grew by 6.6% YoY, with capacity rising 6.0% YoY (Chart 14)."
  - p108 European carriers capacity (ASK) growth, Q4 2025, YoY = **6** % (2025-10-01..2025-12-31) [DISCARD: European carriers ASK growth; not Heathrow-specific.] quote: "In Q4 2025, passenger demand grew by 6.6% YoY, with capacity rising 6.0% YoY (Chart 14)."
  - p109 European carriers passenger load factor, Q4 2025 = **86.4** % (2025-10-01..2025-12-31) [DISCARD: European carrier load factor; Heathrow-specific CAA seat factor p145 is more applicable.] quote: "As a result, the PLF increased marginally by 0.4 ppt YoY, to 86.4%, the highest of all regions."
  - p110 Europe share of industry RPKs, 2025 = **26.6** % of industry RPKs (2025-01-01..2025-12-31) [DISCARD: Europe share of industry RPKs; irrelevant to Heathrow September passengers.] quote: "Europe2 26.6 6.6 6.0 5.1 4.2 86.4 56.3"
  - p111 Industry-wide passenger traffic (RPK), Q4 2025 = **2,400,000,000,000** RPK (revenue passenger kilometers) (2025-10-01..2025-12-31) [DISCARD: Industry-wide RPK level; not Heathrow-specific.] quote: "Industry-wide passenger traffic reached 2.4 trillion Revenue Passenger Kilometers (RPK) in Q4 2025, representing a 6.0% YoY increase (Chart 12)."
  - p112 Industry-wide passenger traffic (RPK) growth, Q4 2025, YoY = **6** % (2025-10-01..2025-12-31) [DISCARD: Industry-wide RPK growth; not Heathrow-specific.] quote: "Industry-wide passenger traffic reached 2.4 trillion Revenue Passenger Kilometers (RPK) in Q4 2025, representing a 6.0% YoY increase (Chart 12)."
  - p113 Industry-wide capacity (ASK) growth, Q4 2025, YoY = **5.7** % (2025-10-01..2025-12-31) [DISCARD: Industry-wide ASK growth; not Heathrow-specific.] quote: "dustry-wide capacity, measured in Available Seat Kilometers (ASK), increased by 5.7% YoY, but at a slower pace than passenger traffic, leading to a 0.2 percentage point (ppt) rise in the Passenger Loa"
  - p114 Industry-wide passenger load factor, Q4 2025 = **84** % (2025-10-01..2025-12-31) [DISCARD: Industry-wide load factor; not Heathrow-specific.] quote: "leading to a 0.2 percentage point (ppt) rise in the Passenger Load Factor (PLF) to 84.0%."
  - p115 Europe-UK (Spain-UK corridor) passenger traffic, Q4 2025, level = **10,000,000** passengers (2025-10-01..2025-12-31) [DISCARD: Spain-UK corridor traffic; not Heathrow-specific.] quote: "Passenger traffic between the two countries rose by 8.3% YoY in Q4 2025, surpassing 10 million passengers (Chart 45)."
  - p116 Spain-UK corridor passenger traffic growth, Q4 2025, YoY = **8.3** % (2025-10-01..2025-12-31) [DISCARD: Spain-UK corridor growth; not Heathrow-specific.] quote: "Passenger traffic between the two countries rose by 8.3% YoY in Q4 2025, surpassing 10 million passengers (Chart 45)."
  - p117 Global GDP real growth estimate, 2025 = **3.2** % (2025-01-01..2025-12-31) [DISCARD: Global GDP growth; too indirect and not used.] quote: "Global GDP probably grew by around 3.2% (real) in 2025, reaching over USD 117 trillion in nominal terms"
- dropped by code checks: 6 (period_end 2026-12-31 after as_of: 4; period_end missing or unparseable: 1; scale word 'billion' not supported by quote or table header: 1)

### d7 [administrative] airport coordinator and Heathrow capacity planner

Hypothesis: Declared runway and slot capacity for summer 2026 bounds September movements and seats; allocated slots compared with achieved movements give a capacity-utilisation check independent of airline schedules.

Queries issued by the searcher: ACL Heathrow summer 2026 slot allocation declared capacity; Heathrow 480,000 air transport movements cap annual; acl-uk.org LHR summer 2026 start of season report slot allocation movements; Heathrow monthly traffic statistics September 2025 passengers 7.8 million

- `https://www.acl-uk.org/wp-content/uploads/2026/03/LHR-Local-Rule-3-0326-ACL.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.enginecowl.com/qatar-air-france-slot-swap-lhr/` -> **snapshot** (snapshot 20260712061127); points raw/verified 12/3
  - p118 Qatar Airways weekly departures from Doha Hamad International Airport to London  = **66** weekly departures (2026-07-01..2026-07-31) [DISCARD: Airline-specific Qatar weekly departures; not convertible to Heathrow's total September 2026 passenger count.] quote: "in July, for example, whenQatar Airways will have 66 weekly departures from the airport"
  - p119 Qatar Airways rank at London Heathrow by weekly flights, July (current schedules = **11** rank (2026-07-01..2026-07-31) [DISCARD: Airline rank by weekly flights; airline-specific context, not a total passenger quantity.] quote: "the Qatari carrier will be the 11th busiest airline at the airport in terms of weekly flights"
  - p120 Qatar Airways rank at London Heathrow by weekly departing seats, July (current s = **6** as written "sixth", value check pending rank (2026-07-01..2026-07-31) [DISCARD: Airline rank by departing seats; airline-specific context, not a total passenger quantity.] quote: "and the sixth in terms of weekly departing seats."
- `https://www.enginecowl.com/alaska-airlines-lhr-slots/` -> **snapshot** (snapshot 20260518131841); points raw/verified 15/1
  - p121 Summer 2026 season start date at London Heathrow = **29** as written "March 29, 2026", value check pending date (day of month) (2026-03-29..2026-03-29) [DISCARD: Summer season start date; not a passenger-count quantity.] quote: "for the summer 2026 season, which will begin on March 29, 2026"
- `https://www.acl-uk.org/news/uk-alleviation-related-to-fuel-related-issues-returned-slot-data-as-at-10-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 23 (period_end 2026-10-24 after as_of: 21; period_end missing or unparseable: 2)

### d8 [shocks] airport operational risk and news monitor

Hypothesis: Known disruptions, strikes, weather, security incidents, ATC constraints, runway works, or policy changes affecting September 2026 could shift achieved passengers away from the schedule/history relationship; measurable cancelled movements or seats should adjust the estimate.

Queries issued by the searcher: Heathrow airport September 2026 disruption cancellations; Heathrow operational notice September 2026 capacity restrictions; Heathrow August 2026 passenger traffic 7.8 million monthly statistics; Heathrow passengers September 2025 7 million monthly traffic statistics

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://safariindia.com/heathrow-sees-strong-summer/` -> **snapshot** (snapshot 20260911133436); points raw/verified 15/13
  - p122 Heathrow total passengers, August 2026 (monthly) = **7,867,000** passengers (2026-08-01..2026-08-31) [DISCARD: Redundant duplicate of p56 (August 2026 total passengers).] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p123 Heathrow total passengers, August 2026 (narrative) = **7,800,000** passengers (2026-08-01..2026-08-31) [DISCARD: Rounded narrative duplicate of p56 (August 2026 total passengers).] quote: "with 7.8 million passengers travelling through the airport in August alone"
  - p124 Heathrow total passengers, June–August 2026 (summer cumulative) = **23,000,000** passengers (2026-06-01..2026-08-31) [DISCARD: Redundant duplicate of p62 (June-August 2026 summer passengers).] quote: "Heathrow recorded 23 million passengers between June and August 2026"
  - p125 Heathrow total passengers, January–August 2026 (cumulative) = **55,721,000** passengers (2026-01-01..2026-08-31) [DISCARD: Redundant duplicate of p57 (January-August 2026 cumulative passengers).] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p126 Heathrow total passengers, September 2025–August 2026 (trailing 12 months) = **84,257,000** passengers (2025-09-01..2026-08-31) [DISCARD: Redundant duplicate of p58 (September 2025-August 2026 trailing 12-month passengers).] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p127 Heathrow total passengers, August 2026 year-on-year % change = **-2.1** percent (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p128 Heathrow total passengers, January–August 2026 year-on-year % change = **-0.4** percent (2026-01-01..2026-08-31) [keep: ] quote: "\| Total \| 7,867 \| -2.1 \| 55,721 \| -0.4 \| 84,257 \| 0.3 \|"
  - p129 Heathrow total air transport movements, August 2026 = **41,048** air transport movements (2026-08-01..2026-08-31) [DISCARD: Redundant duplicate of p59 (August 2026 air transport movements).] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p130 Heathrow total air transport movements, January–August 2026 (cumulative) = **312,559** air transport movements (2026-01-01..2026-08-31) [DISCARD: Redundant duplicate of p60 (January-August 2026 cumulative air transport movements).] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p131 Heathrow total air transport movements, August 2026 year-on-year % change = **-1.3** percent (2026-08-01..2026-08-31) [keep: ] quote: "\| Total \| 41,048 \| -1.3 \| 312,559 \| -1.7 \| 472,617 \| -0.7 \|"
  - p132 Heathrow busiest day passengers, 2 August 2026 = **272,000** passengers (2026-08-02..2026-08-02) [DISCARD: Redundant duplicate of p64 (2 August 2026 busiest-day passengers).] quote: "The airport also recorded its busiest day on 2 August, when nearly 272,000 passengers travelled through its terminals."
  - p133 Share of Heathrow passengers waiting less than five minutes at security, summer  = **98** % (2026-06-01..2026-08-31) [DISCARD: Duplicate of p65; security wait metric, not a passenger count.] quote: "Heathrow said 98% of passengers waited less than five minutes at security"
  - p134 Share of Heathrow bags departing as planned, summer 2026 = **98** % (2026-06-01..2026-08-31) [DISCARD: Duplicate of p66; baggage performance metric, not a passenger count.] quote: "while 98% of bags departed as planned"
- `https://www.hindustantimes.com/india-news/indians-stranded-as-uk-air-traffic-failure-cancels-2000-flights-air-india-indigo-services-hit-10178900405717` -> **snapshot** (snapshot 20260911094115); points raw/verified 15/0
- `https://www.pap.pl/aktualnosci/chaos-na-lotniskach-w-wielkiej-brytanii-pasazerowie-nadal-odczuwaja-efekty-paralizu` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 17 (period_end missing or unparseable: 17)

### b1 [capacity_consumption] September 2026 scheduled capacity at Heathrow

Hypothesis: Monthly scheduled departing seats and air transport movements for Heathrow in September 2026, paired with an achieved load factor, would provide a direct capacity-times-utilisation estimate. This is the missing input that could replace the seasonal-transfer route and reduce reliance on August 2026 as the only adjacent-month anchor.

Queries issued by the searcher: Heathrow monthly traffic statistics September 2026 passengers; Heathrow Airport September 2026 scheduled departing seats movements; Heathrow August 2026 traffic statistics 7.8 million passengers seat factor air transport movements; OAG Heathrow September 2026 departing seats capacity schedule analysis

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://prod.gk.heathrow.com/content/dam/heathrow/web/common/documents/company/investor/reports-and-presentations/financial-results/2026/Heathrow_(SP` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.caa.co.uk/media/v5gdnznn/iag-empirical-tests-of-the-starting-scarcity-rent-hypothesis-heathrow.pdf` -> **snapshot** (snapshot 20260423184614); points raw/verified 15/12
  - p135 Heathrow annual passengers, 2025 (Heathrow Traffic Statistics) = **84,463,061** passengers (2025-01-01..2025-12-31) [keep: ] quote: "2025 477,883 0.8 84,463,061 0.7 176.7 -0.1 1.1"
  - p136 Heathrow annual air transport movements (ATMs), 2025 = **477,883** air transport movements (2025-01-01..2025-12-31) [keep: ] quote: "2025 477,883 0.8 84,463,061 0.7 176.7 -0.1 1.1"
  - p137 Heathrow passengers per ATM, 2025 = **177** passengers per ATM (2025-01-01..2025-12-31) [keep: ] quote: "2025 477,883 0.8 84,463,061 0.7 176.7 -0.1 1.1"
  - p138 Heathrow annual passengers, 2024 = **83,859,729** passengers (2024-01-01..2024-12-31) [keep: ] quote: "2024 473,965 4.4 83,859,729 5.9 176.9 1.5 1.1"
  - p139 Heathrow annual air transport movements (ATMs), 2024 = **473,965** air transport movements (2024-01-01..2024-12-31) [keep: ] quote: "2024 473,965 4.4 83,859,729 5.9 176.9 1.5 1.1"
  - p140 Heathrow passengers per ATM, 2024 = **177** passengers per ATM (2024-01-01..2024-12-31) [keep: ] quote: "2024 473,965 4.4 83,859,729 5.9 176.9 1.5 1.1"
  - p141 Heathrow passengers per ATM, September 2025 (monthly series) = **183** passengers per ATM (2025-09-01..2025-09-30) [keep: ] quote: "163 159 162 176 174 184 192 193 183 179 171 180"
  - p142 Heathrow passengers per ATM, August 2025 (monthly series) = **193** passengers per ATM (2025-08-01..2025-08-31) [keep: ] quote: "163 159 162 176 174 184 192 193 183 179 171 180"
  - p143 Heathrow passengers per ATM, September 2024 (monthly series) = **182** passengers per ATM (2024-09-01..2024-09-30) [keep: ] quote: "162 160 170 171 174 187 192 192 182 176 171 182"
  - p144 Heathrow passengers per ATM, August 2024 (monthly series) = **192** passengers per ATM (2024-08-01..2024-08-31) [keep: ] quote: "162 160 170 171 174 187 192 192 182 176 171 182"
  - p145 Heathrow system-level seat factor, CY2024 (total passengers / total seats) = **80.9** % (2024-01-01..2024-12-31) [keep: ] quote: "London Heathrow 80.9 201 79 4110 81.0"
  - p146 Heathrow scheduled flights, 2024 (all carriers, OAG schedule) = **480,221** flights (2024-01-01..2024-12-31) [keep: ] quote: "Total 480,221 100.0% 105.2 100.0% 431.2 100.0%"
- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0
- dropped by code checks: 3 (scale word 'million' not supported by quote or table header: 2; scale word 'billion' not supported by quote or table header: 1)

### b2 [own_history] Seasonal stability of Heathrow September/August passengers

Hypothesis: The primary seasonal route uses the 2025 September/August ratio, with August 2025 inferred from a rounded year-on-year change. Direct 2024 and 2025 September and August monthly table values would test whether that ratio is stable and reduce calendar-weekday noise.

Queries issued by the searcher: Heathrow monthly traffic statistics September 2025 passengers; Heathrow Airport monthly traffic statistics August 2025 8.2 million passengers; Heathrow monthly traffic statistics 2024 September passengers table; "Business and traffic commentary Aug 2024" Heathrow investegate passengers August 2024; Heathrow August 2024 passengers 7.9 million record August investegate "Aug 2024"

- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-funding-limited--44bi/business-and-traffic-commentary-sept-2025/9165976` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investegate.co.uk/index.php/announcement/rns/heathrow-finance-plc--80cx/business-and-traffic-commentary-sept-2024/8479491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mediacentre.heathrow.com/pressrelease/detail/23757` -> **snapshot** (snapshot 20251102201700); points raw/verified 15/15
  - p147 Heathrow total terminal passengers, August 2025 (table, thousands) = **8,036,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p148 Heathrow total terminal passengers, August 2025 year-on-year % change = **0.8** percent (2025-08-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p149 Heathrow total terminal passengers, January to August 2025 cumulative (thousands = **55,927,000** passengers (2025-01-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p150 Heathrow total terminal passengers, September 2024 to August 2025 rolling 12 mon = **84,003,000** passengers (2024-09-01..2025-08-31) [keep: ] quote: "\| Total \| 8,036 \| 0.8 \| 55,927 \| 0.3 \| 84,003 \| 1.6 \|"
  - p151 Heathrow UK market terminal passengers, August 2025 (thousands) = **397,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| UK \| 397 \| -2.0 \| 3,000 \| -2.6 \| 4,585 \| 0.9 \|"
  - p152 Heathrow EU market terminal passengers, August 2025 (thousands) = **2,844,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| EU \| 2,844 \| 1.8 \| 18,781 \| 0.3 \| 28,166 \| 2.2 \|"
  - p153 Heathrow Non-EU Europe market terminal passengers, August 2025 (thousands) = **518,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Non-EU Europe \| 518 \| -1.2 \| 3,711 \| -2.8 \| 5,543 \| -1.3 \|"
  - p154 Heathrow Africa market terminal passengers, August 2025 (thousands) = **296,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Africa \| 296 \| 4.9 \| 2,204 \| -0.3 \| 3,313 \| -2.8 \|"
  - p155 Heathrow North America market terminal passengers, August 2025 (thousands) = **1,996,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| North America \| 1,996 \| -0.5 \| 13,713 \| -0.1 \| 20,618 \| 1.0 \|"
  - p156 Heathrow Latin America market terminal passengers, August 2025 (thousands) = **174,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Latin America \| 174 \| -3.6 \| 1,457 \| 1.1 \| 2,217 \| 4.3 \|"
  - p157 Heathrow Middle East market terminal passengers, August 2025 (thousands) = **833,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Middle East \| 833 \| 2.7 \| 5,717 \| 1.6 \| 8,636 \| 2.7 \|"
  - p158 Heathrow Asia/Pacific market terminal passengers, August 2025 (thousands) = **977,000** passengers (2025-08-01..2025-08-31) [keep: ] quote: "\| Asia / Pacific \| 977 \| 0.9 \| 7,344 \| 2.5 \| 10,925 \| 3.3 \|"
  - p159 Heathrow total air transport movements, August 2025 = **41,585** air transport movements (2025-08-01..2025-08-31) [keep: ] quote: "\| Total \| 41,585 \| 0.0 \| 317,825 \| 0.6 \| 475,733 \| 1.0 \|"
  - p160 Heathrow busiest ever day passengers, 1 August (over) = **270,000** passengers (2025-08-01..2025-08-01) [keep: ] quote: "we hit our busiest ever day on 1st August with over 270,000 passengers"
  - p161 Heathrow Terminal 5 single-day record passengers, 22 August (more than) = **112,000** passengers (2025-08-22..2025-08-22) [keep: ] quote: "Terminal 5 set a new single-day record on 22nd August - successfully welcoming more than 112,000 travellers"

### b3 [shocks] Early September 2026 realised operations and disruptions

Hypothesis: If early September 2026 daily passenger or movement counts, strike/ATC/weather cancellations, or Heathrow operational notices are available, they would show whether September 2026 is tracking the August 2026 weakness or the milder year-to-date trend. This would directly reduce the largest uncertainty in the seasonal-transfer methods.

Queries issued by the searcher: Heathrow monthly traffic statistics September 2026 passengers; Heathrow airport August 2026 passenger numbers; Heathrow September 2026 strike cancellations disruption NATS air traffic control; "Heathrow" September 2026 daily passenger record week

- `https://mediacentre.heathrow.com/pressrelease/detail/26126` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bluewin.ch/it/attualita/mondo/ecco-cosa-potrebbe-aver-mandato-in-tilt-il-traffico-aereo-nei-cieli-britannici-li.3593917` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thepeninsulaqatar.com/article/09/09/2026/cyberattack-ruled-out-in-uk-air-traffic-glitch-as-more-flights-axed` -> **snapshot** (snapshot 20260909113737); points raw/verified 5/5
  - p162 Flights scrapped across the UK on Wednesday following NATS air traffic control d = **177** flights (2026-09-09..2026-09-09) [keep: ] quote: "UK air travellers faced more misery Wednesday with 177 flights scrapped across the country"
  - p163 Flights to and from UK airports axed Tuesday due to NATS technical glitch = **1,300** flights (2026-09-08..2026-09-08) [keep: ] quote: "after 1,300 flights to and from UK airports were axed Tuesday"
  - p164 Passengers affected by Britain's worst air systems failure in 2023 = **700,000** passengers (2023-01-01..2023-12-31) [keep: ] quote: "Britain meanwhile suffered its worst air systems failure in years in 2023, with more than 700,000 passengers affected"
  - p165 Ryanair passengers disrupted by the NATS glitch = **65,000** passengers (2026-09-08..2026-09-09) [keep: ] quote: "Ryanair said more than 65,000 of its passengers had been disrupted"
  - p166 Ryanair flights cancelled due to the NATS glitch = **50** flights (2026-09-08..2026-09-09) [keep: ] quote: "it had cancelled more than 50 flights"
- `https://www.heathrow.com/company/investor-centre/reports/traffic-statistics` -> **snapshot** (snapshot 20260806125204); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p5'] Both report September 2025 Heathrow passengers. p1 is the precise monthly table total (7.348m); p5 is the same publisher's rounded 'nearly 7.4m' narrative. They are not independent.
- corroborating: ['p1', 'p2'] September 2025 passenger level and +0.8% year-on-year change come from the same Heathrow table and are internally consistent.
- related: ['p3', 'p4', 'p82'] January-September 2025 cumulative, October 2024-September 2025 rolling 12 months, and calendar 2025 annual passengers cover different periods but are mutually consistent around an 84 million annual sc
- related: ['p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p64'] All are from the August 2026 Heathrow release. Monthly total, year-to-date cumulative, trailing 12 months, movements, summer total, and busiest day are internally consistent. Shared source, so not ind
- corroborating: ['p56', 'p127'] August 2026 passenger total and -2.1% year-on-year change are from the same table; the level and negative change are consistent.
- related: ['p127', 'p128'] August 2026 passengers were -2.1% year-on-year while January-August 2026 was -0.4%, indicating weakening after the first half. This is an adjacent-period difference, not a contradiction; September sho
- corroborating: ['p31', 'p32', 'p33', 'p38', 'p39', 'p40'] First-half 2026 passengers rose 0.2% while departing seats fell 1.4% and frequencies fell 1.6%, implying a higher achieved load factor; transfer traffic rose 5.4%. These are different metrics but mutu
- corroborating: ['p36', 'p87', 'p88', 'p89'] Middle East capacity and traffic reductions in first-half 2026 and in April/May 2026 are consistent. p89 indicates the Middle East is a material but minority share of 2025 passengers, explaining sensi
- related: ['p15', 'p24', 'p1'] September 2025 movements, movement change, and passenger total provide a passengers-per-movement baseline. Passenger and movement changes differ, so this is a cross-check rather than an independent pa
- related: ['p41', 'p42', 'p43'] Eurocontrol network and UK daily flight counts are aviation-activity context, but they are not Heathrow-specific monthly passenger evidence and require large transfer assumptions.
- related: ['p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117'] IATA global, European, and UK capacity/demand forecasts are industry context. They are not Heathrow September 2026 levels and cannot be directly substituted without strong transfer assumptions.
- corroborating: ['p56', 'p62', 'p64'] August 2026 monthly total, June-August summer total, and the 2 August busiest-day count are consistent with a busy August. Same source, not independent.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5'] Heathrow September 2025 monthly statistics: p1 precise table value 7.348M; p5 narrative 'nearly 7.4M' is a rounded version of the same figure. p2 YoY +0.8%, p3 Jan-Sep cumulative 63.275M, and p4 trail
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p1'] September 2025 market breakdown sums exactly to p1: 383+2599+459+277+1859+165+702+904 thousand = 7,348 thousand. This confirms internal consistency and shows Middle East was about 702k (9.6% of the mo
- corroborating: ['p15', 'p21', 'p22', 'p24'] September 2025 air transport movements: 40,193 monthly; 358,018 Jan-Sep cumulative; 475,936 trailing 12 months; +0.5% YoY. Implied passengers per ATM is about 183, matching CAA monthly p141. Consisten
- corroborating: ['p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p64'] August 2026 Heathrow table: 7.867M passengers, 55.721M Jan-Aug cumulative, 84.257M trailing 12 months, 41,048 ATMs. p62 narrative 7.8M August and 23M June-August, and p64 busiest day 272k, are rounded
- corroborating: ['p127', 'p128', 'p131', 'p56', 'p57', 'p59'] August 2026 YoY changes: passengers -2.1%, Jan-Aug -0.4%, ATMs -1.3%. These match p56 7.867M versus p147 8.036M (about -2.1%) and p59 41,048 versus p159 41,585 (about -1.3%).
- corroborating: ['p82', 'p135', 'p136', 'p137', 'p138', 'p139', 'p140'] 2025 annual passengers: FlightGlobal p82 84.5M and CAA p135 84,463,061 are consistent to rounding. CAA p136 ATMs 477,883 and p137 passengers/ATM 177; 2024 p138 83,859,729, p139 473,965, p140 177. No m
- corroborating: ['p141', 'p142', 'p143', 'p144', 'p1', 'p15'] CAA monthly passengers/ATM: September 2025 183, August 2025 193, September 2024 182, August 2024 192. Confirms a strong August-to-September seasonal drop and year-over-year stability. p1/p15 = about 1
- corroborating: ['p147', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159'] August 2025 total 8.036M and market breakdown sum to about 8.035M (rounding only); ATMs 41,585. Used as prior-year August denominator for the 2025 September/August seasonal transfer.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40'] H1 2026 Heathrow: record 40M passengers (+0.2%) but departing seats -1.4% and frequencies -1.6%; transfer traffic +5.4%. Segment capacity: North America -0.9%, Middle East -16.5%, Asia-Pacific +6.7%. 
- corroborating: ['p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p128'] 2026 demand weakened after early-year growth: Jan-May +0.7% (p84), April -5% and May +1% (p85/p86) driven by Middle East cuts (p87/p88); Jan-Aug now -0.4% (p128). Middle East was >10% of 2025 passenge
- contextual: ['p162', 'p163', 'p165', 'p166', 'p43', 'p59', 'p141'] Early September 2026 NATS disruption: 1,300 UK flights axed Tuesday 8 Sep and 177 Wednesday 9 Sep (p162/p163); Ryanair reported 50 flights and 65k passengers disrupted (p165/p166). Heathrow-specific c

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 Heathrow passenger loss from early-September NATS disruption | 0.5 | 0.1..1.5 | 0.1..1.5 | % | unused | Based on p162/p163: 1,477 UK flights cancelled over 8-9 September 2026. Heathrow is roughly one-fifth of UK movements (p59 monthly ATMs versus p43 daily UK movements), and at about 183 passengers/ATM (p141) a full loss would be roughly 0.7% of a 7M+ month. Rebooking and passenger reaccommodation red | The NATS disruption actually affected Heathrow movements and the net passenger loss was not fully offset by rebooking within September. | Evidence that Heathrow had no material cancellations, or that disrupted passengers were fully reaccommodated within September. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a1: assumption a1 restates kept data point p24 (same value and unit); reference p24 instead |
| m2 | formula_mc | 7,363,359 | ['p57', 'p1', 'p3'] / [] | [] |  | 0.50 | equal |  |
| m3 | formula_mc | 7,317,174 | ['p58', 'p1', 'p82'] / [] | [] |  | 0.50 | equal |  |
| m4 | formula_mc | n/a |  | [] |  | 0.00 |  | input p128 must be positive for lognormal sampling |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **7,340,230** passenger, 80% interval [5,211,689, 10,338,103] passenger, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total passengers counted at London Heathrow Airport in Heathrow's published monthly traffic statistics for the full calendar month of September 2026 is 7,340,230 passenger (80% model-based interval 5,211,689 to 10,338,103 passenger). The interval is conditional on the formula inputs and assumptions, not a demonstrated accuracy guarantee.

Main evidence: September 2025 was 7,348,000 passengers; Jan–Aug 2026 cumulative was 55,721,000 passengers; Jan–Sep 2025 cumulative was 63,275,000 passengers; the Sep 2025–Aug 2026 rolling [n] months was 84,257,000 passengers; and 2025 annual passengers were 84,500,000 passengers. Method m2 scales the 2025 September share of Jan–Aug cumulative traffic to 2026 (7,363,359 passenger, weight 50%); m3 applies September 2025's share of the 2025 calendar year to the trailing-[n]-month run-rate (7,317,174 passenger, weight 50%). Both are weighted equally; the other routes were not usable.

Observed inputs are the Heathrow monthly and annual totals above; the transfer of seasonal shares to 2026 is an assumption. The biggest risk is a changed 2026 monthly profile, especially from early-September disruption. Actual September 2026 monthly data would most improve the estimate.

Key assumptions: none (every formula input is an observed data point).

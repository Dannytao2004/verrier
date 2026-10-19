# Evidence ledger: fc_us_gen_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate total U.S. net electricity generation at utility-scale facilities (all sectors, all energy sources, excluding small-scale solar) in July 2026, in gigawatt-hours (GWh, equal to thousand megawatthours), as it will be first reported in the U.S. Energy Information Administration's Electric Power Monthly (Table 1.1).
- as_of: 2026-08-25
- Pinned target: Total U.S. net electricity generation at utility-scale facilities, all sectors and all energy sources, excluding small-scale solar (EIA Electric Power Monthly Table 1.1, 'Net Generation' total) | unit gigawatt-hours (GWh, thousand megawatthours) | period 2026-07-01..2026-07-31 | publisher U.S. Energy Information Administration (EIA), Electric Power Monthly

- Official value (scoring only, never shown to the agent): 453,744

## Directions and pages

### d1 [own_history] EIA historical Table 1.1 monthly totals

Hypothesis: July 2026 total generation ≈ July 2025 total adjusted for year-over-year load growth trend; July is the seasonal peak month, so prior Julys (2023, 2024, 2025) anchor level and seasonal shape.

Queries issued by the searcher: EIA Electric Power Monthly Table 1.1 net generation July 2025 total all sectors thousand megawatthours; EIA total US utility-scale net generation July 2024 July 2023 gigawatt-hours monthly; "July 2025" total net generation "429,317" OR "429,3" thousand megawatthours EIA; EIA Electric Power Monthly July 2025 release "total net generation" year-to-date "3.3%" increase July 2025 record

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?month=july2024&t=table_1_01` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/tables/pdf/7atab.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.enerwrap.com/p/us-power-generation-monthly` -> **snapshot** (snapshot 20260418072731); points raw/verified 15/9
  - p1 Month-over-month change in total U.S. power generation, July 2024 vs June 2024 = **12.7** % (2024-07-01..2024-07-31) [DISCARD: Month-over-month change (June to July 2024) is a seasonal-shape statistic, not a year-over-year level anchor; redundant ] quote: "Total power generation in July 2024 was 381 TWh, up 12.7% from last month and higher by 9.4% from July 2023"
  - p2 Year-over-year change in total U.S. power generation, July 2024 vs July 2023 = **9.4** % (2024-07-01..2024-07-31) [keep: ] quote: "Total power generation in July 2024 was 381 TWh, up 12.7% from last month and higher by 9.4% from July 2023"
  - p3 Natural gas share of total U.S. power stack, July 2024 = **46.2** % (2024-07-01..2024-07-31) [keep: ] quote: "Natural gas was 46.2% of the power stack, the highest in recent years"
  - p4 Year-over-year change in solar generation, July 2024 = **29** % (2024-07-01..2024-07-31) [keep: ] quote: "Solar generation slipped slightly versus last month coming in at 22.1 TWh versus 22.5 TWh in June 2024, with a 29.0% increase versus last year"
  - p5 Month-over-month change in wind generation, July 2024 = **27.5** % (2024-07-01..2024-07-31) [DISCARD: Month-over-month wind change (June to July 2024) is a within-year seasonal artifact, not a year-over-year signal and not] quote: "Wind power continues to be choppy at 28.2 TWh, down a whopping 27.5% compared to the prior month"
  - p6 Wind share of total U.S. power stack, July 2024 = **6.8** % (2024-07-01..2024-07-31) [keep: ] quote: "Wind share was a meager 6.8% of the total power stack, with the data continuing to show reduced rates in hotter weather - the prior five months of wind were 10-15% stack share"
  - p7 Solar plus wind share of total U.S. power stack, July 2024 = **12.1** % (2024-07-01..2024-07-31) [keep: ] quote: "Solar plus wind were 12.1% of the stack, the lowest since August 2023"
  - p8 Coal share of total U.S. generation, July 2024 = **17.8** % (2024-07-01..2024-07-31) [keep: ] quote: "Coal was 17.8% of total generation - for comparison it was 27.3% in July 2018"
  - p9 Coal share of total U.S. generation, July 2018 = **27.3** % (2018-07-01..2018-07-31) [DISCARD: July 2018 coal share (27.3%) is a historical comparison cited only to illustrate decline; too old and redundant with p8 ] quote: "Coal was 17.8% of total generation - for comparison it was 27.3% in July 2018"
- `https://www.enerdata.net/publications/daily-energy-news/us-electricity-generation-hits-new-record-4430-twh-2025-says-eia.html` -> **snapshot** (snapshot 20260318183408); points raw/verified 5/4
  - p10 Year-over-year growth rate of U.S. net electricity generation, 2025 vs 2024 = **2.8** % (2025-01-01..2025-12-31) [keep: ] quote: "an increase of 2.8% compared with 2024, which had previously been the highest annual total in the EIA's dataset dating back to 1949"
  - p11 Year-over-year growth rate of U.S. retail electricity sales, residential sector, = **2.2** % (2025-01-01..2025-12-31) [keep: ] quote: "residential (+2.2%), commercial (by 2.9%), and industrial (by 0.7%)"
  - p12 Year-over-year growth rate of U.S. retail electricity sales, commercial sector,  = **2.9** % (2025-01-01..2025-12-31) [keep: ] quote: "residential (+2.2%), commercial (by 2.9%), and industrial (by 0.7%)"
  - p13 Year-over-year growth rate of U.S. retail electricity sales, industrial sector,  = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "residential (+2.2%), commercial (by 2.9%), and industrial (by 0.7%)"
- dropped by code checks: 7 (number: unknown scale word 'TWh': 7)

### d2 [related_series] EIA-930 daily/hourly balancing authority demand and generation

Hypothesis: Sum of daily balancing-authority net generation (EIA-930) for July 2026 approximates the monthly Table 1.1 total; EIA-930 covers ~all utility-scale generation and can be aggregated to a July total.

Queries issued by the searcher: EIA-930 daily net generation July 2026 balancing authority total; EIA Hourly Electric Grid Monitor monthly net generation July 2026; EIA Short-Term Energy Outlook August 2026 total electricity generation July 2026 forecast; "EIA-930" July 2026 net generation total GWh United States Lower 48 monthly

- `https://www.eia.gov/electricity/monthly/update/` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/tables/pdf/7atab.pdf` -> **snapshot** (snapshot 20260504233906); points raw/verified 15/0
- `https://catalystcoop-pudl.readthedocs.io/en/stable/data_sources/eia930.html` -> **snapshot** (snapshot 20260415235520); points raw/verified 12/0
- `https://www.eia.gov/realtime_grid/docs/UserGuideAndKnownIssues.pdf` -> **snapshot** (snapshot 20200311102941); points raw/verified 15/0
- dropped by code checks: 42 (scale word 'billion' not supported by quote or table header: 15; period_end missing or unparseable: 19; number: more than one number in value_as_written: 8)

### d3 [related_series] EIA Short-Term Energy Outlook (STEO)

Hypothesis: STEO publishes monthly total generation forecasts; the July 2026 STEO value (published before cutoff) is a direct forecast of the target, possibly needing a small bias correction based on STEO's historical forecast errors.

Queries issued by the searcher: EIA Short-Term Energy Outlook July 2026 electricity generation forecast; STEO table 7 electricity generation forecast 2026 monthly gigawatthours; eia.gov/outlooks/steo/archives/jul26.pdf; EIA STEO Table 7a total electricity generation monthly "July 2026" forecast gigawatthours

- `https://www.eia.gov/outlooks/steo/archives/jul26.pdf` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/archives/aug26.pdf` -> **snapshot** (snapshot 20260823130023); points raw/verified 15/6
  - p14 U.S. total utility-scale electricity generation, Q3 2025 (historical) = **1,235** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Electricity generation (a) ................................................. 1,075 1,058 1,235 1,062 1,091 1,077 1,266 1,074 1,100 1,108 1,317 1,108 4,430 4,508 4,632"
  - p15 U.S. total generation, Q3 2025 (Table 7d, electric power sector, historical) = **1,195** billion kilowatthours (2025-07-01..2025-09-30) [DISCARD: Electric-power-sector-only Q3 2025 total is a subset of p14 (all sectors); using both would double-count and p14 is the ] quote: "Total generation ......................... 1,035.8 1,021.1 1,194.8 1,023.6 1,053.6 1,040.1 1,225.2 1,034.0 1,061.3 1,070.1 1,274.9 1,067.8 4,275.2 4,352.9 4,474.0"
  - p16 U.S. electricity generation change, 1H26 vs 1H25 (total electric power sector) = **37,000,000,000** kilowatthours (2026-01-01..2026-06-30) [keep: ] quote: "During the first half of 2026 (1H26), total generation by the U.S. electric power sector was up 37 billion kilowatthours (BkWh), or 1.8%, compared with the first six months of 2025."
  - p17 U.S. electricity generation growth rate, 1H26 vs 1H25 (total electric power sect = **1.8** % (2026-01-01..2026-06-30) [keep: ] quote: "During the first half of 2026 (1H26), total generation by the U.S. electric power sector was up 37 billion kilowatthours (BkWh), or 1.8%, compared with the first six months of 2025."
  - p18 U.S. coal-fired generation change, 1H26 vs 1H25 = **39** billion kilowatthours (2026-01-01..2026-06-30) [keep: ] quote: "During 1H26, U.S. coal generation was down 39 BkWh (11%), reversing the increases that occurred in 2025."
  - p19 U.S. solar generation growth rate, 1H26 vs 1H25 = **21** % (2026-01-01..2026-06-30) [keep: ] quote: "Generation from solar and wind was up 21% and 6%, respectively, in 1H26, reflecting continuing growth in renewable energy generating capacity."
- `https://zenodo.org/records/21321403` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/outlook.php` -> **snapshot** (snapshot 20260820060059); points raw/verified 10/0
- dropped by code checks: 19 (period_end 2026-09-30 after as_of: 6; period_end 2026-12-31 after as_of: 3; number: more than one number in value_as_written: 10)

### d4 [capacity_consumption] Generation capacity by source and capacity factors

Hypothesis: Total = Σ_source (capacity_source × capacity factor_source × hours in July); July capacity factors for gas, coal, nuclear, wind, solar, hydro are seasonal and can be taken from prior Julys.

Queries issued by the searcher: EIA Electric Power Monthly Table 6.7.B capacity factors by energy source; EIA monthly generating capacity by energy source 2026 gigawatts table 6.1; EIA Electric Power Monthly Table 6.07.A capacity factors fossil fuels natural gas coal 2025 July; EIA Table 6.2.A Net Summer Capacity of Utility Scale Units by Technology and by State 2026

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_6_07_a` -> **snapshot** (snapshot 20260803162153); points raw/verified 0/0
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b` -> **snapshot** (snapshot 20260818214621); points raw/verified 0/0
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_6_01` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.energy.gov/sites/default/files/2026-02/Ex.%206%20Short%20Term%20Energy%20Outlook%20Feb%202026.pdf` -> **snapshot** (snapshot 20260704194745) **LEAK SENTINEL HIT ['(?<![\\d.,])400,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-

### d5 [physical_flow] Demand-side: retail sales plus losses

Hypothesis: Net generation ≈ retail electricity sales + direct use + transmission/distribution losses; July retail sales can be forecast from prior Julys and weather/CDD, then grossed up by loss factor (~5-6%).

Queries issued by the searcher: EIA Electric Power Monthly July 2025 retail electricity sales table 1.1 net generation; EIA monthly retail electricity sales July 2025 gigawatthours; EIA electricity losses percent of generation transmission distribution; EIA Short-Term Energy Outlook August 2026 electricity sales July 2026 forecast; EIA Electric Power Monthly July 2025 table 5.2 retail sales thousand megawatthours July 2024 2025; "July 2025" "retail sales" electricity "billion kWh" EIA; EIA Monthly Energy Review July 2026 electricity sales table 7.6

- `https://www.eia.gov/electricity/monthly/current_month/september2025.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/tables/pdf/7btab.pdf` -> **snapshot** (snapshot 20260820213917); points raw/verified 15/0
- `http://large.stanford.edu/courses/2025/ph240/eliades1/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://osr.ashrae.org/Online-Comment-Database/ShowDoc2/Table/DocumentAttachments/FileName/4700-189.1-2023%20Addendum%20s%201st%20APR%20draft%20v2.pdf` -> **snapshot** (snapshot 20251026085856); points raw/verified 15/4
  - p20 U.S. electricity generated at domestic power plants, 2024 (EIA) = **4,150,000,000,000** kWh (2024-01-01..2024-12-31) [keep: ] quote: "For 2024 the U.S. Energy Information Agency (EIA) reports that, 4.15 trillion kWh were generated at domestic power plants in the United States"
  - p21 U.S. electricity lost through transmission and distribution (T&D) or otherwise u = **220,000,000,000** kWh (2024-01-01..2024-12-31) [keep: ] quote: "220 billion kWh (5.3%) were lost through the transmission and distribution (T&D) system or otherwise unaccounted for"
  - p22 U.S. T&D loss share of generation, 2024 (losses / generation) = **5.3** % (2024-01-01..2024-12-31) [keep: ] quote: "220 billion kWh (5.3%) were lost through the transmission and distribution (T&D) system or otherwise unaccounted for"
  - p23 U.S. distribution efficiency (1 minus T&D loss share), 2024 = **94.7** % (2024-01-01..2024-12-31) [keep: ] quote: "This results in a distribution efficiency of 94.7%."
- dropped by code checks: 26 (scale word 'billion' not supported by quote or table header: 15; period_end missing or unparseable: 10; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d6 [shocks] Weather and cooling-degree-days

Hypothesis: July generation is strongly driven by cooling demand; 2026 July CDD anomaly vs prior Julys shifts the total. Hotter-than-normal July raises generation; milder lowers it.

Queries issued by the searcher: NOAA population weighted cooling degree days July 2026; EIA electricity demand temperature sensitivity GWh per cooling degree day; NOAA National Climate Report July 2026 cooling degree days above average; EIA STEO "cooling degree days" summer electricity demand sensitivity percent per degree

- `https://www.mtsinsights.com/summaries/10377/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://climateimpactcompany.com/u-s-gas-power-report-the-2026-u-s-population-weight-cdd-forecast-2/` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://climateimpactcompany.com/u-s-early-notes-significant-heat-risk-early-july-for-u-s-2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://emlab.ucsb.edu/blog/summertime-blues` -> **snapshot** (snapshot 20260216031225); points raw/verified 11/3
  - p24 Share of U.S. homes using air conditioning (2015 RECS) = **87** % (2015-01-01..2015-12-31) [keep: ] quote: "87% of homes in the United States use air conditioning at an average annual operating cost of $265"
  - p25 Average annual A/C operating cost per U.S. home (2015 RECS) = **265** USD per home per year (2015-01-01..2015-12-31) [DISCARD: Average annual A/C operating cost per home ($265/yr, 2015) is a cost, not an energy quantity; cannot be converted to GWh] quote: "at an average annual operating cost of $265"
  - p26 A/C share of total home energy expenditures (2015 RECS) = **12** % (2015-01-01..2015-12-31) [DISCARD: A/C share of home energy expenditures (12%) is an expenditure share, not an electricity share; misleading if used as an ] quote: "This amounts to 12% of total home energy expenditures."
- dropped by code checks: 8 (number: unknown scale word 'quadrillion': 2; period_end missing or unparseable: 4; period year 1984 does not appear in the page text or URL (likely mis-dated): 1; period year 2019 does not appear in the page text or URL (likely mis-dated): 1)

### d7 [related_series] Regional ISO/RTO demand totals

Hypothesis: Sum of major RTO/ISO July 2026 load (PJM, MISO, ERCOT, CAISO, SPP, NYISO, ISO-NE) plus non-RTO areas approximates national generation; RTOs publish monthly load promptly.

Queries issued by the searcher: PJM July 2026 monthly load report; ERCOT July 2026 monthly generation GWh; PJM 2026 monthly generation by fuel type July 2026 GWh; ISO-NE July 2026 monthly generation load energy report

- `https://www.ercot.com/files/docs/2026/08/17/ERCOT-Monthly-Operational-Overview-July-2026.pdf` -> **snapshot** (snapshot 20260818033351); points raw/verified 15/15
  - p27 ERCOT monthly energy generation, July 2026 (preliminary settlements) = **51,550** GWh (2026-07-01..2026-07-31) [keep: ] quote: "Monthly energy generation increased by 7.7% year-over-year to 51,550 GWh in July 2026, compared to 47,846 GWh in July 2025"
  - p28 ERCOT monthly energy generation, July 2025 (comparison year) = **47,846** GWh (2025-07-01..2025-07-31) [DISCARD: Redundant with p27/p29: same ERCOT July 2025 level already implied by p27 and p29; keeping all three adds no information] quote: "Monthly energy generation increased by 7.7% year-over-year to 51,550 GWh in July 2026, compared to 47,846 GWh in July 2025"
  - p29 ERCOT year-over-year growth rate of monthly energy generation, July 2026 vs July = **7.7** % (2026-07-01..2026-07-31) [DISCARD: Redundant with p27 and p28 (same ERCOT growth statement); p27 is the level needed for the ERCOT-share route.] quote: "Monthly energy generation increased by 7.7% year-over-year to 51,550 GWh in July 2026, compared to 47,846 GWh in July 2025"
  - p30 ERCOT unofficial all-time peak demand record, 7/22/2026 HE18 (preliminary) = **91,134** MW (2026-07-22..2026-07-22) [DISCARD: Duplicate of p33 (same 91,134 MW ERCOT July 2026 peak); peak demand is not directly the energy target anyway.] quote: "ERCOT set a new unofficial all-time peak demand record of 91,134 MW* at hour ending 18 on 7/22/2026"
  - p31 ERCOT July 2025 peak demand, 7/30/2025 = **81,734** MW (2025-07-30..2025-07-30) [DISCARD: July 2025 ERCOT peak demand is a capacity/peak metric, not energy; not usable in an energy-total formula and redundant w] quote: "This is 9,400 MW more than the July 2025 demand of 81,734 MW on 7/30/2025"
  - p32 ERCOT previous all-time peak demand record, 8/10/2023 = **85,508** MW (2023-08-10..2023-08-10) [DISCARD: Prior all-time ERCOT peak (85,508 MW, Aug 2023) is redundant with p30/p31 for establishing the July 2026 peak level; the] quote: "5,581 MW more than the previous all-time peak demand record of 85,508 MW set on 8/10/2023"
  - p33 ERCOT July 2026 maximum net system hourly value (July 2026 Demand and Energy rep = **91,134** MW (2026-07-01..2026-07-31) [DISCARD: Peak demand (MW) is not a generation-energy quantity; cannot enter a GWh formula without an unsupported load-factor assu] quote: "ERCOT set a new record of 91,134 MW* for the month of July on 7/22/2026"
  - p34 ERCOT July 2026 minimum net system 15-minute interval value = **51,412** MW (2026-07-01..2026-07-31) [DISCARD: ERCOT July 2026 minimum 15-minute interval (51,412 MW) is a within-month trough, not a monthly energy or peak quantity; ] quote: "51,412 MW**"
  - p35 ERCOT active generation interconnection requests, total MW as of July 31, 2026 = **456,578** MW (2026-07-31..2026-07-31) [DISCARD: Total interconnection-queue MW (456,578) is requested capacity, not installed capacity or generation; unusable as a leve] quote: "ERCOT is tracking 1,906 active generation interconnection requests totaling 456,578 MW as of July 31."
  - p36 ERCOT interconnection queue solar capacity (share of queue) = **34.6** % (2026-07-01..2026-07-31) [DISCARD: Queue solar share (34.6%) is a composition of requested capacity, not realized generation; irrelevant to July 2026 outpu] quote: "Totals: Solar 158 GW (34.6%), Wind 49 GW (10.7%), Gas 80 GW (17.6%), Battery 166 GW / 398 GWh (36.3%), Other 4 GW (0.9%)"
  - p37 ERCOT interconnection queue battery capacity (share of queue) = **36.3** % (2026-07-01..2026-07-31) [DISCARD: Queue battery share (36.3%) is a composition of requested capacity, not realized generation; irrelevant to July 2026 out] quote: "Totals: Solar 158 GW (34.6%), Wind 49 GW (10.7%), Gas 80 GW (17.6%), Battery 166 GW / 398 GWh (36.3%), Other 4 GW (0.9%)"
  - p38 ERCOT RUC total effective Resource-hours, July 2026 = **422** Resource-hours (2026-07-01..2026-07-31) [DISCARD: RUC total effective Resource-hours (422.4) is a reliability-commitment count, not energy; no conversion to GWh.] quote: "There were 422.4 RUC total effective Resource-hours in July."
  - p39 ERCOT RUC effective Resource-hours committed to address capacity concerns, July  = **375** Resource-hours (2026-07-01..2026-07-31) [DISCARD: RUC hours committed to capacity concerns (375.2) is a reliability-commitment count, not energy; no conversion to GWh.] quote: "375.2 hours (89%) were committed to address capacity concerns and 47.3 hours (11%) were committed to alleviate congestion."
  - p40 ERCOT loads approved to energize, observed non-simultaneous monthly peak consump = **4,370** MW (2026-07-01..2026-07-31) [DISCARD: ERCOT loads approved to energize (4,370 MW non-simultaneous peak) is a connection-pipeline statistic, not generation or ] quote: "Of the 9,456 MW that have received Approval to Energize, ERCOT has observed a non-simultaneous monthly peak consumption of 4,370 MW in July 2026"
  - p41 ERCOT 12-month rolling average CPS1 (frequency control measure) = **183** % (2025-08-01..2026-07-31) [DISCARD: ERCOT CPS1 frequency-control percentage is a reliability metric with no quantitative link to national generation volume.] quote: "Current 12-Month Rolling Average: 183.01% Jul CPS1 (%): 186.86"
- `https://www.eia.gov/electricity/monthly/update/` -> **snapshot** (snapshot 20260807140411); points raw/verified 3/3
  - p42 U.S. net electricity generation change, May 2026 vs May 2025 = **3.1** % (2026-05-01..2026-05-31) [keep: ] quote: "Net electricity generation in the United States increased 3.1% compared to May 2025."
  - p43 Total U.S. coal stockpiles, May 2026 = **120,000,000** tons (2026-05-01..2026-05-31) [DISCARD: Coal stockpile level (120 million tons) is a fuel-inventory quantity, not generation; no conversion to July 2026 GWh is ] quote: "Total U.S. coal stockpiles increased by 2.9% to 120 million tons compared to the previous month."
  - p44 Total U.S. coal stockpiles change, May 2026 vs previous month = **2.9** % (2026-05-01..2026-05-31) [DISCARD: Coal stockpile month-over-month change (+2.9%) is an inventory change, not a generation signal; unusable for the target.] quote: "Total U.S. coal stockpiles increased by 2.9% to 120 million tons compared to the previous month."
- `https://www.monitoringanalytics.com/reports/pjm_state_of_the_market/2026/2026q2-som-pjm.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eprinc.org/first-summer-2026-heat-wave-how-pjms-fuel-mix-responded/` -> **snapshot** (snapshot 20260814054606); points raw/verified 13/7
  - p45 PJM all-time record load set in 2006 = **165,563** MW (2006-01-01..2006-12-31) [DISCARD: PJM 2006 all-time record load is a peak-demand benchmark, not a July 2026 energy observation; not usable numerically for] quote: "approaching the all-time record of 165,563 MW set in 2006"
  - p46 Share of PJM total supply from nuclear, coal and natural gas during heat wave = **88** % (2026-07-01..2026-07-09) [DISCARD: PJM fuel-mix share during a heat wave is a regional composition statistic, not a national generation level; no valid con] quote: "Nuclear, coal, and natural gas delivered 88% of the total"
  - p47 PJM coal generation week-over-week increase = **69** % (2026-07-01..2026-07-09) [DISCARD: PJM coal week-over-week change is a short-window regional swing, not a July national level; unusable as a numeric input.] quote: "coal rose from 14.3 to 24.2 GW (up roughly 69%) week-over-week"
  - p48 PJM natural gas generation week-over-week increase = **26** % (2026-07-01..2026-07-09) [DISCARD: PJM gas week-over-week change is a short-window regional swing, not a July national level; unusable as a numeric input.] quote: "gas from 43.6 to 55.0 GW (up 26%)"
  - p49 Wholesale power price level topped during PJM heat wave = **2,000** USD/MWh (2026-07-01..2026-07-09) [DISCARD: Wholesale price ($2,000/MWh) is a price spike, not a quantity of generation; no route converts it to GWh.] quote: "waiving plant emissions limits as wholesale prices topped $2,000/MWh"
  - p50 Temperatures regularly exceeded during early July 2026 heat wave = **100** °F (2026-07-01..2026-07-09) [DISCARD: Temperature threshold (>100°F) is qualitative weather context, not a quantity that can enter a GWh formula.] quote: "with temperatures regularly above 100°F"
  - p51 Number of DOE Section 202(c) emergency orders issued in 2026 as of this event = **3** as written "third", value check pending orders (2026-01-01..2026-07-09) [DISCARD: Count of DOE 202(c) emergency orders is a policy-event count with no quantitative mapping to generation volume.] quote: "The load event also triggered DOE's third Section 202(c) emergency order of 2026"
- dropped by code checks: 6 (number: unknown scale word 'GW': 6)

### d8 [forecasts_markets] Third-party forecasts and nowcasts

Hypothesis: Analyst/consultancy nowcasts of July 2026 U.S. power demand or generation provide an independent check on the STEO and history-based routes.

Queries issued by the searcher: US power demand July 2026 forecast EIA electricity generation; summer 2026 US electricity demand record forecast NERC; "July 2026" US electricity generation record demand heat wave grid operator peak; EIA-930 July 2026 total US generation terawatt-hours monthly estimate

- `https://cms.eei.org/News/news/All/2026-grid-record` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/tables/pdf/7atab.pdf` -> **snapshot** (snapshot 20260504233906); points raw/verified 15/0
- `https://www.amperon.co/blog/july-2026-heat-event-how-amperon-performed` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cms.ferc.gov/sites/default/files/2026-05/26_Summer%20Assessment_0529.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'billion' not supported by quote or table header: 15)

### b1 [related_series] EIA-930 daily balancing-authority data

Hypothesis: Summing EIA-930 daily net generation across all balancing authorities for July 2026 would give a near-complete, near-real-time estimate of the Table 1.1 total, unlocking route d2 and providing an independent check on the STEO-based route. It matters because it is the only route that observes July 2026 directly rather than forecasting it.

Queries issued by the searcher: EIA Hourly Electric Grid Monitor July 2026 monthly generation; EIA-930 balancing authority net generation July 2026; EIA-930 net generation compared with Electric Power Monthly "Table 1.1" coverage ratio lower than other electricity publications; "July 2026" U.S. electricity generation total TWh month EIA grid monitor national

- `https://catalystcoop-pudl.readthedocs.io/en/stable/data_sources/eia930.html` -> **snapshot** (snapshot 20260415235520); points raw/verified 12/8
  - p52 EIA-930 temporal coverage start (half-year) = **2,015** as written "2015half2", value check pending half-year label (2015-07-01..2015-12-31) [DISCARD: EIA-930 coverage start metadata; no numeric role in any executable method.] quote: "\| Temporal Coverage \| 2015half2-2026half1 \|"
  - p53 EIA-930 temporal coverage end (half-year) = **2,026** as written "2026half1", value check pending half-year label (2026-01-01..2026-06-30) [DISCARD: EIA-930 coverage end metadata (2026half1); confirms no July 2026 EIA-930 aggregate is available, but supplies no number.] quote: "\| Temporal Coverage \| 2015half2-2026half1 \|"
  - p54 Start date for EIA-930 demand-by-subregion data availability = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [DISCARD: Schema start-date metadata; no numeric role.] quote: "Demand by subregion (available for select BAs beginning 2018-07-01)"
  - p55 Start date for EIA-930 net generation by energy source availability = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [DISCARD: Schema start-date metadata; no numeric role.] quote: "Net generation by energy source (beginning 2018-07-01)"
  - p56 Start date for EIA-930 estimated total CO2 emissions data = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [DISCARD: Schema start-date metadata; no numeric role.] quote: "Estimated total CO2 emissions (beginning 2018-07-01)"
  - p57 Start date for EIA-930 estimated CO2 emissions by fuel type = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [DISCARD: Schema start-date metadata; no numeric role.] quote: "Estimated CO2 emissions by fuel type (beginning 2018-07-01)"
  - p58 Start date for EIA-930 estimated CO2 emissions for electricity imports or export = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [DISCARD: Schema start-date metadata; no numeric role.] quote: "Estimated CO2 emissions for electricity imports or exports (beginning 2018-07-01)"
  - p59 Effective start of new wind/solar/hydro/storage energy source columns (Q1 2025 r = **2,024** as written "2024half2", value check pending half-year label (2024-07-01..2024-12-31) [DISCARD: Schema change-date metadata; no numeric role.] quote: "The change takes effect starting in 2024half2."
- `https://docs.sugra.ai/doc-2263605` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.linecurrents.live/reports/western-electric-supply-2026-07-05` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/` -> **snapshot** (snapshot 20260825203529); points raw/verified 0/0
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### b2 [related_series] STEO monthly forecast table

Hypothesis: The August 2026 STEO (published before cutoff) contains an explicit monthly total-generation forecast for July 2026, which would be a direct forecast of the target and could be bias-corrected using STEO's historical monthly forecast errors. It matters because it is the single most direct available forecast and would anchor the estimate.

Queries issued by the searcher: EIA STEO August 2026 Table 7 monthly electricity generation forecast; Short-Term Energy Outlook Table 7 electricity generation gigawatthours monthly forecast 2026; zenodo "EIA STEO" archive "Published August 2026" version Short-Term Energy Outlook; web.archive.org eia.gov/outlooks/steo/tables/pdf/7atab.pdf August 2026

- `https://www.eia.gov/outlooks/steo/outlook.php` -> **snapshot** (snapshot 20260820060059); points raw/verified 15/14
  - p60 August 2026 STEO release date (archive listing) = **8** as written "08/11/2026", value check pending date (month/day/year) (2026-08-11..2026-08-11) [DISCARD: STEO release-date metadata only; the actual August 2026 STEO July 2026 forecast value is not in the kept data, so this c] quote: "\| August 2026 \| 08/11/2026 \| aug26.pdf \| aug26_base.xlsx \| \|"
  - p61 July 2026 STEO release date (archive listing) = **7** as written "07/07/2026", value check pending date (month/day/year) (2026-07-07..2026-07-07) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| July 2026 \| 07/07/2026 \| jul26.pdf \| jul26_base.xlsx \| \|"
  - p62 June 2026 STEO release date (archive listing) = **6** as written "06/09/2026", value check pending date (month/day/year) (2026-06-09..2026-06-09) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| June 2026 \| 06/09/2026 \| jun26.pdf \| jun26_base.xlsx \| \|"
  - p63 May 2026 STEO release date (archive listing) = **5** as written "05/12/2026", value check pending date (month/day/year) (2026-05-12..2026-05-12) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| May 2026 \| 05/12/2026 \| may26.pdf \| may26_base.xlsx \| \|"
  - p64 April 2026 STEO release date (archive listing) = **4** as written "04/07/2026", value check pending date (month/day/year) (2026-04-07..2026-04-07) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| April 2026 \| 04/07/2026 \| apr26.pdf \| apr26_base.xlsx \| \|"
  - p65 March 2026 STEO release date (archive listing) = **3** as written "03/10/2026", value check pending date (month/day/year) (2026-03-10..2026-03-10) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| March 2026 \| 03/10/2026 \| mar26.pdf \| mar26_base.xlsx \| \|"
  - p66 February 2026 STEO release date (archive listing) = **2** as written "02/10/2026", value check pending date (month/day/year) (2026-02-10..2026-02-10) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| February 2026 \| 02/10/2026 \| feb26.pdf \| feb26_base.xlsx \| \|"
  - p67 July 2025 STEO release date (archive listing) = **7** as written "7/8/2025", value check pending date (month/day/year) (2025-07-08..2025-07-08) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| July 2025 \| 7/8/2025 \| jul25.pdf \| jul25_base.xlsx \| \|"
  - p68 August 2025 STEO release date (archive listing) = **8** as written "8/12/2025", value check pending date (month/day/year) (2025-08-12..2025-08-12) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| August 2025 \| 8/12/2025 \| aug25.pdf \| aug25_base.xlsx \| \|"
  - p69 July 2024 STEO release date (archive listing) = **7** as written "7/9/2024", value check pending date (month/day/year) (2024-07-09..2024-07-09) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| July 2024 \| 7/9/2024 \| jul24.pdf \| jul24_base.xlsx \| \|"
  - p70 August 2024 STEO release date (archive listing) = **8** as written "8/6/2024", value check pending date (month/day/year) (2024-08-06..2024-08-06) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| August 2024 \| 8/6/2024 \| aug24.pdf \| aug24_base.xlsx \| \|"
  - p71 July 2023 STEO release date (archive listing) = **7** as written "07/11/2023", value check pending date (month/day/year) (2023-07-11..2023-07-11) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| July 2023 \| 07/11/2023 \| jul23.pdf \| jul23_base.xlsx \| \|"
  - p72 August 2023 STEO release date (archive listing) = **8** as written "08/08/2023", value check pending date (month/day/year) (2023-08-08..2023-08-08) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| August 2023 \| 08/08/2023 \| aug23.pdf \| aug23_base.xlsx \| \|"
  - p73 July 2022 STEO release date (archive listing) = **7** as written "07/12/2022", value check pending date (month/day/year) (2022-07-12..2022-07-12) [DISCARD: STEO release-date metadata; no numeric forecast value.] quote: "\| July 2022 \| 07/12/2022 \| jul22.pdf \| jul22_base.xlsx \| \|"
- `https://www.eia.gov/outlooks/steo/tables/pdf/7atab.pdf` -> **snapshot** (snapshot 20260504233906); points raw/verified 15/0
- `https://zenodo.org/records/21321403` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://beyond-coal.jp/en/documents/eia_short-term-energy-outlook-202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; scale word 'billion' not supported by quote or table header: 15)

### b3 [related_series] Regional load and weather

Hypothesis: July 2026 CDD anomalies and RTO monthly load (PJM, MISO, CAISO, SPP, NYISO, ISO-NE) would let us scale the national total from the ERCOT/PJM heat-wave evidence and quantify the weather-driven uplift, resolving the largest uncertainty in the history-based route. It matters because the ERCOT +7.7% and PJM heat-wave evidence suggest a hotter-than-normal July, but the national magnitude is unknown.

Queries issued by the searcher: NOAA July 2026 cooling degree days national; PJM July 2026 monthly load report; NOAA National Climate Report July 2026 cooling degree days above average; EIA Electric Power Monthly July 2026 net generation total utility-scale table 1.1

- `https://www.mtsinsights.com/summaries/10377/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://modoenergy.com/research/en/pjm-bess-july-2026-benchmark` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://climateimpactcompany.com/u-s-gas-power-report-the-2026-u-s-population-weight-cdd-forecast-2/` -> **snapshot** (snapshot 20260417084210); points raw/verified 15/13
  - p74 U.S. population-weight CDD projection for July 2026 = **355** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p75 U.S. 30-year normal CDD for July = **321** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p76 U.S. 10-year normal CDD for July = **372** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p77 U.S. July CDD in the most recent prior year (first of past 3 years) = **376** cooling degree days (2025-07-01..2025-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p78 U.S. July CDD two years prior (second of past 3 years) = **370** cooling degree days (2024-07-01..2024-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p79 U.S. July CDD three years prior (third of past 3 years) = **371** cooling degree days (2023-07-01..2023-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p80 U.S. CDD projection for June 2026 = **246** cooling degree days (2026-06-01..2026-06-30) [DISCARD: June 2026 CDD projection is not July; no valid transfer to the July target without an unsupported coefficient.] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p81 U.S. 10-year normal CDD for June = **253** cooling degree days (2026-06-01..2026-06-30) [DISCARD: June 10-yr normal CDD; not July and not a generation quantity.] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p82 U.S. CDD projection for May 2026 = **121** cooling degree days (2026-05-01..2026-05-31) [DISCARD: May 2026 CDD projection; wrong month for the July target.] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
  - p83 U.S. May CDD last year (2025) = **102** cooling degree days (2025-05-01..2025-05-31) [DISCARD: May 2025 CDD; wrong month and prior year.] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
  - p84 Texas region CDD for April (observed early-season count) = **142** cooling degree days (2026-04-01..2026-04-30) [DISCARD: Texas April CDD; wrong month and regional, no valid conversion to July national generation.] quote: "The Texas region is warmest at 142 CDD (compared to the 30-year [94] and 10-year [127]) normal."
  - p85 Texas region 30-year normal CDD for April = **94** cooling degree days (2026-04-01..2026-04-30) [DISCARD: Texas April 30-yr normal CDD; wrong month/region.] quote: "The Texas region is warmest at 142 CDD (compared to the 30-year [94] and 10-year [127]) normal."
  - p86 Texas region 10-year normal CDD for April = **127** cooling degree days (2026-04-01..2026-04-30) [DISCARD: Texas April 10-yr normal CDD; wrong month/region.] quote: "The Texas region is warmest at 142 CDD (compared to the 30-year [94] and 10-year [127]) normal."
- `https://www.getarcresearch.com/feed_runs/1221` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end 2026-08-31 after as_of: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['us electricity generation', 'july power demand', 'eia generation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p14', 'p15'] Both EIA STEO Table 7 series for Q3 2025; p14 is all-sector utility-scale (1,235 BkWh), p15 electric-power-sector only (1,195 BkWh). Consistent: all-sector exceeds electric-power-sector by the industr
- corroborating: ['p16', 'p17'] Same EIA STEO statement: 1H26 electric-power-sector generation up 37 BkWh = 1.8% vs 1H25. Same measurement expressed two ways, not independent.
- corroborating: ['p16', 'p17', 'p18', 'p19'] All from the same August 2026 STEO narrative; internally consistent (coal -39 BkWh, solar +21%, wind +6%, net +37 BkWh). Shared source, so they corroborate only as a single STEO vintage.
- corroborating: ['p10', 'p11', 'p12', 'p13'] Enerdata summary of EIA 2025 data: total net generation +2.8%, retail sales by sector +2.2/+2.9/+0.7%. Consistent direction and magnitude; retail growth slightly below generation growth is plausible g
- corroborating: ['p27', 'p28', 'p29'] ERCOT July 2026 generation 51,550 GWh vs July 2025 47,846 GWh = +7.7%; the three points are the same ERCOT statement (level, comparison level, growth rate).
- corroborating: ['p30', 'p31', 'p32', 'p33'] ERCOT peak-demand records: July 2026 peak 91,134 MW, 9,400 MW above July 2025's 81,734 MW and 5,581 MW above the prior all-time record 85,508 MW. Arithmetic internally consistent.
- corroborating: ['p27', 'p30', 'p33'] ERCOT July 2026 energy (+7.7% YoY) and peak demand (+11.5% YoY) both point to a hot, high-load July 2026 in ERCOT; consistent with the PJM heat-wave evidence.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51'] Single eprinc.org account of the early-July 2026 PJM heat wave: temperatures above 100F, coal +69% and gas +26% week-over-week, prices above $2,000/MWh, third DOE 202(c) order. Shared source; corrobor
- corroborating: ['p42', 'p16', 'p17'] EIA May 2026 net generation +3.1% YoY and 1H26 electric-power-sector +1.8% YoY are consistent with a year of moderate growth; different months and slightly different scopes (all-sector vs electric-pow
- corroborating: ['p1', 'p2'] Same enerwrap statement: July 2024 381 TWh, +12.7% MoM and +9.4% YoY. Same measurement, not independent.
- corroborating: ['p3', 'p6', 'p7', 'p8'] July 2024 fuel shares from one enerwrap article: gas 46.2%, wind 6.8%, solar+wind 12.1%, coal 17.8%. Internally consistent (solar ~5.3% implied). Shared source.
- corroborating: ['p8', 'p9'] Coal share fell from 27.3% (July 2018) to 17.8% (July 2024); same source, consistent secular decline.
- corroborating: ['p20', 'p21', 'p22', 'p23'] Same ASHRAE source: 4.15 trillion kWh generated 2024, 220 BkWh (5.3%) T&D losses, 94.7% distribution efficiency. Internally consistent (220/4150=5.3%).
- corroborating: ['p24', 'p25', 'p26'] Same 2015 RECS summary: 87% of homes have A/C, $265/yr average cost, 12% of home energy expenditures. Shared source; old (2015) and only contextual for cooling-driven seasonality.
- corroborating: ['p35', 'p36', 'p37'] ERCOT interconnection queue: 456,578 MW total, solar 34.6%, battery 36.3%. Same source; queue is not realized capacity and is only contextual.
- corroborating: ['p38', 'p39'] ERCOT RUC hours: 422.4 total, 375.2 (89%) for capacity concerns. Same source; contextual reliability signal, not a generation quantity.
- corroborating: ['p27', 'p42'] ERCOT +7.7% YoY in July 2026 and national +3.1% YoY in May 2026 are consistent with ERCOT growing faster than the national average; supports using ERCOT as a high-growth regional indicator rather than
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p14', 'p15'] Both are EIA STEO Table 7 series for Q3 2025; p14 is total generation (all sectors) and p15 is electric-power-sector only, so p15 is a subset of p14. They are consistent in level and share a single un
- corroborating: ['p16', 'p17'] Same STEO statement: 1H26 electric-power-sector generation up 37 BkWh = 1.8% vs 1H25. Same measurement, so redundant as two separate signals; use as one growth anchor.
- corroborating: ['p16', 'p18', 'p19'] All from the same August 2026 STEO narrative: total +1.8%, coal -11%, solar +21%, wind +6% in 1H26. Internally consistent (renewables growth offsetting coal decline) but a single source, not independe
- corroborating: ['p27', 'p28', 'p29', 'p30', 'p31', 'p33'] All ERCOT July 2026/July 2025 reports from the same publisher. p27/p28/p29 are the same energy figures (level, prior-year level, growth rate); p30/p33 are the same 91,134 MW peak; p31 is the July 2025
- corroborating: ['p74', 'p75', 'p76', 'p77', 'p78', 'p79'] Same Climate Impact Company projection: July 2026 CDD 355 vs 30-yr 321, 10-yr 372, and prior three Julys 376/370/371. Consistent picture of a July 2026 that is warmer than the 30-yr normal but cooler 
- conflicting: ['p74', 'p77', 'p78', 'p79'] July 2026 projected CDD (355) is below each of the last three Julys (376, 370, 371), implying a mild negative weather-driven pull on July 2026 national generation relative to July 2025 — in tension wi
- corroborating: ['p42', 'p16', 'p17'] May 2026 net generation +3.1% YoY (p42) and 1H26 electric-power-sector +1.8% (p17) both point to modest positive 2026 growth; different months/scopes but same direction.
- corroborating: ['p10', 'p11', 'p12', 'p13'] 2025 annual generation +2.8% and retail sales growth by sector (res +2.2%, com +2.9%, ind +0.7%) are consistent with a demand-driven growth trend of roughly 2-3%/yr entering 2026.
- corroborating: ['p20', 'p21', 'p22', 'p23'] Same ASHRAE/OSR source: 4.15 trillion kWh generated, 220 BkWh (5.3%) T&D losses, 94.7% distribution efficiency. Internally consistent; useful only as a loss-factor conversion, not as a July level.
- corroborating: ['p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59'] All from the same PUDL documentation describing EIA-930 coverage and schema. They establish that EIA-930 data exist through 2026half1 but do not themselves supply a July 2026 total; they are metadata,
- corroborating: ['p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73'] STEO archive release dates. They confirm the August 2026 STEO (p60) was published 2026-08-11, before cutoff, so a July 2026 forecast exists in principle — but the numeric forecast value is not in the 
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p50'] Same EPRI/EPRINC article on the early-July 2026 PJM heat wave: record-approaching load, 88% from nuclear/coal/gas, coal +69% and gas +26% week-over-week, temperatures above 100°F. Consistent regional 
- corroborating: ['p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86'] Same Climate Impact Company source for May/June 2026 CDD and Texas April CDD. They support a warm spring/early summer 2026 but are not July national CDD.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 national utility-scale generation growth vs July 2025 | 2.5 | 0.5..4.5 | 0.5..4.5 | % | unused | Anchored on kept evidence: 1H26 electric-power-sector generation +1.8% YoY (p17), May 2026 net generation +3.1% (p42), and 2025 annual growth +2.8% (p10). July 2026 national CDD (355, p74) is below the last three Julys (376/370/371, p77-p79), arguing for a weather drag relative to July 2025, while E | July 2026 national generation tracks the 1H26/May 2026 growth trend with modest weather adjustment; used to scale a July 2025 base. | Evidence that July 2026 national CDD was far below 355 (large weather drag) or that national load growth accelerated well above ~4% (e.g., a broad-based heat wave across all regions). |
| a4 | July share of Q3 total generation (seasonal shape factor) | 0.345 | 0.32..0.37 | 0.2433..0.4866 (widened) | fraction | unused | July is the seasonal peak month, so it exceeds the Q3 monthly average (1/3 = 0.333). A July share of Q3 near 0.345 reflects July being modestly above the Q3 mean, with August close behind and September lower. Range spans 0.32-0.37 to cover year-to-year weather variation in the July-vs-Q3 shape. | Used to convert the Q3 2025 total (p14) into a July 2025 proxy before applying the YoY growth factor. | Monthly EIA data showing July's share of Q3 generation outside 0.32-0.37 in recent years. |
| a6 | ERCOT share of U.S. utility-scale net generation | 11 | 9..13 | 7.649..15.3 (widened) | % | unused | ERCOT (p27, 51,550 GWh in July 2026) is one of the largest U.S. balancing authorities. ERCOT's ~50 TWh monthly output against a national July total near 400 TWh implies roughly 12-13%; allowing for ERCOT's above-average growth and summer concentration, a central 11% with a 9-13% range is used. This  | Used to scale observed ERCOT July 2026 generation up to the national total. | Evidence that ERCOT's share of national utility-scale generation is outside 9-13% (e.g., a published ERCOT-vs-U.S. generation ratio). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p14'] / ['a1', 'a4'] | [] |  | 0.00 |  | formula: numeric constant 100 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the un |
| m2 | formula_mc | n/a | ['p27'] / ['a6'] | [] |  | 0.00 |  | formula: numeric constant 100 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the un |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **n/a** GWh, 80% interval [n/a, n/a] GWh, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

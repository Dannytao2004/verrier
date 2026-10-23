# Evidence ledger: fc_us_gen_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate total U.S. net electricity generation at utility-scale facilities (all sectors, all energy sources, excluding small-scale solar) in July 2026, in gigawatt-hours (GWh, equal to thousand megawatthours), as it will be first reported in the U.S. Energy Information Administration's Electric Power Monthly (Table 1.1).
- as_of: 2026-08-25
- Pinned target: Total U.S. net electricity generation at utility-scale facilities, all sectors and all energy sources, excluding small-scale solar (EIA Electric Power Monthly Table 1.1, 'Net Generation by Energy Source: Total (All Sectors)'), for the calendar month of July 2026 | unit gigawatt-hours (GWh, = thousand megawatthours) | period 2026-07-01..2026-07-31 | publisher U.S. Energy Information Administration (EIA), Electric Power Monthly

- Official value (scoring only, never shown to the agent): 453,744

## Directions and pages

### d1 [own_history] EIA historical monthly series

Hypothesis: July 2026 utility-scale net generation will be close to the July values of recent years (2023-2025) adjusted for trend growth and weather; July is the seasonal peak month. The same-month prior-year values anchor the level and the year-over-year growth rate.

Queries issued by the searcher: EIA Electric Power Monthly Table 1.1 net generation July 2025 total all sectors; EIA total net generation all sectors monthly gigawatt-hours 2024 2025; "epmt_1_1" net generation July 2025 thousand megawatthours total generation at utility scale facilities; EIA electricity generation July 2025 record total net generation GWh monthly

- `https://www.eia.gov/electricity/monthly/current_month/january2026.pdf` -> **snapshot** (snapshot 20260201161814) **LEAK SENTINEL HIT ['(?<![\\d.,])10,925(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://hugo.lv/lv/TranslateProxy/https/www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/totalenergy/data/monthly/pdf/sec7.pdf` -> **snapshot** (snapshot 20260804131454) **LEAK SENTINEL HIT ['(?<![\\d.,])10,925(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.eia.gov/todayinenergy/detail.php?id=67284` -> **snapshot** (snapshot 20260815182121); points raw/verified 5/5
  - p1 U.S. total electricity net generation, annual 2025 = **4,430** terawatthours (TWh) (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, the United States generated 4.43 thousand terawatthours (TWh) of electricity"
  - p2 U.S. total electricity net generation, year-over-year growth 2025 vs 2024 = **2.8** % (2025-01-01..2025-12-31) [keep: ] quote: "up 2.8% from 2024 generation, which previously had been the highest annual total"
  - p3 U.S. retail electricity sales to residential ultimate customers, change 2025 vs  = **2.2** % (2025-01-01..2025-12-31) [keep: ] quote: "increased compared with 2024 in all three sectors: residential (by 2.2%), commercial (by 2.9%), and industrial (by 0.7%)"
  - p4 U.S. retail electricity sales to commercial ultimate customers, change 2025 vs 2 = **2.9** % (2025-01-01..2025-12-31) [keep: ] quote: "residential (by 2.2%), commercial (by 2.9%), and industrial (by 0.7%)"
  - p5 U.S. retail electricity sales to industrial ultimate customers, change 2025 vs 2 = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "commercial (by 2.9%), and industrial (by 0.7%)"

### d2 [related_series] EIA-930 hourly/grid monitor and weekly data

Hypothesis: Lower-48 daily/hourly generation from EIA-930 (Hourly Electric Grid Monitor) aggregated over July 2026 gives a near-complete proxy for utility-scale net generation; summing daily totals and scaling for non-lower-48 (Alaska/Hawaii) gives the monthly total.

Queries issued by the searcher: EIA-930 Hourly Electric Grid Monitor July 2026 net generation lower 48 GWh; EIA weekly electricity generation 2026 lower 48 gigawatthours; naturalgasintel total US generation week ended July 2026 EIA-930 "GW" record gas-fired; EIA-930 net generation lower 48 versus Electric Power Monthly total difference ratio percent lower

- `https://naturalgasintel.com/news/natural-gas-power-burn-slips-from-one-year-high-as-wind-roars-back/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.naturalgasintel.com/news/natural-gas-power-burn-hits-11-month-high-as-heat-lifts-demand/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://catalystcoop-pudl.readthedocs.io/en/stable/data_sources/eia930.html` -> **snapshot** (snapshot 20260415235520); points raw/verified 0/0
- `https://www.naturalgasintel.com/news/wind-doldrums-lift-natural-gas-share-toward-summer-power-peak/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [physical_flow] Grid operator / ISO demand data

Hypothesis: Summing load (which tracks generation plus net imports) across major balancing authorities (PJM, MISO, ERCOT, CAISO, SPP, ISO-NE, NYISO, Southeast, etc.) for July 2026, then scaling to national total via each region's historical share of US generation, yields the target. Net imports are small relative to total generation.

Queries issued by the searcher: ERCOT July 2026 monthly load record peak demand; PJM July 2026 generation load record heat; EIA Electric Power Monthly July 2026 net generation total all sectors table 1.1; MISO July 2026 monthly generation GWh load

- `https://www.eia.gov/electricity/monthly/update/resource-use.php` -> **snapshot** (snapshot 20260816200925); points raw/verified 11/11
  - p6 Year-over-year change in U.S. net electricity generation, May 2026 vs May 2025 = **3.1** % (2026-05-01..2026-05-31) [keep: ] quote: "Net electricity generation in the United States increased 3.1% compared to May 2025."
  - p7 Henry Hub natural gas spot price, May 2026 = **2.9** USD per MMBtu (2026-05-01..2026-05-31) [keep: ] quote: "going from $2.78/MMBtu in April 2026 to $2.90/MMBtu in May 2026"
  - p8 Henry Hub natural gas spot price, April 2026 = **2.78** USD per MMBtu (2026-04-01..2026-04-30) [keep: ] quote: "going from $2.78/MMBtu in April 2026 to $2.90/MMBtu in May 2026"
  - p9 New York City (Transco Zone 6 NY) natural gas price, May 2026 = **2.07** USD per MMBtu (2026-05-01..2026-05-31) [keep: ] quote: "going from $2.13/MMBtu in April 2026 to $2.07/MMBtu in May 2026"
  - p10 New York City (Transco Zone 6 NY) natural gas price, April 2026 = **2.13** USD per MMBtu (2026-04-01..2026-04-30) [keep: ] quote: "going from $2.13/MMBtu in April 2026 to $2.07/MMBtu in May 2026"
  - p11 Central Appalachian coal spot price, May 2026 = **3.48** USD per MMBtu (2026-05-01..2026-05-31) [keep: ] quote: "The average spot price of Central Appalachian coal was unchanged from the previous month at $3.48/MMBtu in May 2026."
  - p12 Henry Hub natural gas price on equivalent energy content and efficiency basis, M = **23.26** USD per MWh (2026-05-01..2026-05-31) [keep: ] quote: "The Henry Hub natural gas price ($23.26/MWh) saw an increase from the previous month ($22.30/MWh)"
  - p13 Henry Hub natural gas price on equivalent energy content and efficiency basis, A = **22.3** USD per MWh (2026-04-01..2026-04-30) [DISCARD: Redundant April 2026 equivalent-basis gas price; p12 (May) supersedes it and no formula needs the April value.] quote: "The Henry Hub natural gas price ($23.26/MWh) saw an increase from the previous month ($22.30/MWh)"
  - p14 Central Appalachian coal price on equivalent energy content and efficiency basis = **37.58** USD per MWh (2026-05-01..2026-05-31) [keep: ] quote: "was below the Central Appalachian coal price ($37.58/MWh) in May 2026"
  - p15 New York City natural gas price on equivalent energy content and efficiency basi = **16.61** USD per MWh (2026-05-01..2026-05-31) [keep: ] quote: "The price of natural gas at New York City ($16.61/MWh) saw a decrease compared to the previous month ($17.10/MWh)"
  - p16 New York City natural gas price on equivalent energy content and efficiency basi = **17.1** USD per MWh (2026-04-01..2026-04-30) [DISCARD: Redundant April 2026 NYC equivalent-basis gas price; p15 (May) supersedes it.] quote: "The price of natural gas at New York City ($16.61/MWh) saw a decrease compared to the previous month ($17.10/MWh)"
- `https://prod.spglobal.com/energy/en/news-research/latest-news/electric-power/071026-pjm-interconnection-sets-new-all-time-peakload-record-of-168158-gw` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://prod.spglobal.com/energy/en/news-research/latest-news/electric-power/072326-triple-digit-high-temperatures-boost-texas-power-grid-to-new-peakl` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eprinc.org/wp-content/uploads/2026/07/EPRINC-Chart2026-24-FirstSummerHeatWaveAndPowerGeneration.pdf` -> **snapshot** (snapshot 20260814054617); points raw/verified 9/9
  - p17 PJM hourly load peak at midday during first U.S. summer 2026 heat wave = **160** gigawatts (2026-06-29..2026-07-05) [keep: ] quote: "Hourly load at midday requirements peaked close to 160 gigawatts (GWs)."
  - p18 PJM hourly average dispatchable generation (nuclear, coal, natural gas) during h = **112** gigawatts (2026-06-29..2026-07-05) [keep: ] quote: "an hourly average of 111.5 GWs (88% of total), was delivered by dispatchable generation"
  - p19 Share of PJM total hourly load met by dispatchable generation during heat wave = **88** % (2026-06-29..2026-07-05) [keep: ] quote: "an hourly average of 111.5 GWs (88% of total), was delivered by dispatchable generation"
  - p20 PJM hourly average nuclear generation during heat wave = **32.4** gigawatts (2026-06-29..2026-07-05) [keep: ] quote: "nuclear, coal, and natural gas -- at average rates of 32.4, 24.2, and 55 GWs, respectively."
  - p21 PJM hourly average coal generation during heat wave = **24.2** gigawatts (2026-06-29..2026-07-05) [keep: ] quote: "nuclear, coal, and natural gas -- at average rates of 32.4, 24.2, and 55 GWs, respectively."
  - p22 PJM hourly average natural gas generation during heat wave = **55** gigawatts (2026-06-29..2026-07-05) [keep: ] quote: "nuclear, coal, and natural gas -- at average rates of 32.4, 24.2, and 55 GWs, respectively."
  - p23 PJM hourly average coal generation in prior week = **14.3** gigawatts (2026-06-22..2026-06-28) [keep: ] quote: "In the case of coal and natural generation, this was up from 14.3 and 43.6 GWs in the prior week."
  - p24 PJM hourly average natural gas generation in prior week = **43.6** gigawatts (2026-06-22..2026-06-28) [keep: ] quote: "In the case of coal and natural generation, this was up from 14.3 and 43.6 GWs in the prior week."
  - p25 PJM hourly average solar and wind generation during heat wave and prior week = **7.5** gigawatts (2026-06-22..2026-07-05) [keep: ] quote: "Solar and wind accounted for an hourly average of 7.5 GWs of generation both during the heat wave and in the prior week."

### d4 [shocks] Weather and demand drivers

Hypothesis: July 2026 generation is strongly driven by cooling demand; a hotter-than-normal July raises generation above the seasonal baseline, a milder one lowers it. Degree-day anomalies and record peak-demand events in July 2026 indicate the direction and rough magnitude of deviation from the prior-year July.

Queries issued by the searcher: July 2026 heat wave electricity demand record peak load; cooling degree days July 2026 NOAA national population-weighted; NOAA July 2026 national climate report hottest July cooling degree days record; EIA "July 2026" electricity generation record demand Short-Term Energy Outlook August 2026

- `https://www.eia.gov/todayinenergy/detail.php?id=67906` -> **snapshot** (snapshot 20260823205518); points raw/verified 6/3
  - p26 ERCOT July 22, 2026 peak load increase vs previous record peak = **6** % (2026-07-22..2026-07-22) [keep: ] quote: "The July 22 peak was 6% greater than the previous peak of 85.5 GW, set on August 10, 2023 according to ERCOT."
  - p27 Share of ERCOT July 22, 2026 peak met by natural gas generation = **48** % (2026-07-22..2026-07-22) [keep: ] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
  - p28 Share of ERCOT July 22, 2026 peak met by solar generation = **32** % (2026-07-22..2026-07-22) [keep: ] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
- `https://prod.spglobal.com/energy/en/news-research/latest-news/electric-power/072326-triple-digit-high-temperatures-boost-texas-power-grid-to-new-peakl` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bostonglobe.com/2026/08/11/metro/hottest-ever-july-united-states/` -> **snapshot** (snapshot 20260817230207); points raw/verified 13/0
- `https://climateimpactcompany.com/u-s-early-notes-significant-heat-risk-early-july-for-u-s-2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (number: unknown scale word 'gigawatts': 3; period year 2023 does not appear in the page text or URL (likely mis-dated): 13)

### d5 [forecasts_markets] EIA STEO and analyst forecasts

Hypothesis: EIA Short-Term Energy Outlook published before cutoff gives monthly or quarterly total generation forecasts for 2026 that can be used directly or as a cross-check; STEO forecasts are close to realized values at short horizons.

Queries issued by the searcher: EIA Short-Term Energy Outlook total electricity generation forecast 2026 TWh; STEO electricity generation third quarter 2026 forecast billion kWh; "Short-Term Energy Outlook" August 2026 electricity generation forecast; EIA STEO July 2026 electricity generation 2026 forecast billion kilowatthours third quarter

- `https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf` -> **snapshot** (snapshot 20260821040641); points raw/verified 15/1
  - p29 EIA STEO August 2026: 1H26 total U.S. electric power sector generation increase  = **37,000,000,000** kilowatthours (2026-01-01..2026-06-30) [keep: ] quote: "During the first half of 2026 (1H26), total generation by the U.S. electric power sector was up 37 billion kilowatthours (BkWh), or 1.8%, compared with the first six months of 2025."
- `https://www.eia.gov/outlooks/steo/pdf/steo_tables.pdf` -> **snapshot** (snapshot 20251123072750); points raw/verified 15/2
  - p30 EIA STEO forecast: U.S. total electricity generation, all sectors, Q3 2025 (bill = **1,232** billion kilowatthours (2025-07-01..2025-09-30) [DISCARD: STEO forecast of Q3 2025 generation; p34 is the realized/updated Q3 2025 value from the same table and is preferred. Kee] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
  - p31 EIA STEO forecast: U.S. total electricity generation, all sectors, Q3 2024 (bill = **1,212** billion kilowatthours (2024-07-01..2024-09-30) [DISCARD: STEO forecast of Q3 2024 generation; p35 is the corresponding updated value. Redundant and a forecast vintage.] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
- `https://beyond-coal.jp/en/documents/eia_short-term-energy-outlook-202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.sxcoal.com/news/detail/2087418656466280449` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 27 (period_end 2026-09-30 after as_of: 24; period_end 2026-12-31 after as_of: 3)

### d6 [capacity_consumption] Capacity and utilisation

Hypothesis: Total generation = installed utility-scale capacity by fuel × capacity factor × hours in July, summed across fuels. July capacity factors are high for gas and low for wind/solar relative to annual averages; using July-specific capacity factors and current capacity estimates constrains the total.

Queries issued by the searcher: EIA capacity by energy source 2026 utility-scale installed capacity megawatts; EIA monthly capacity factor July natural gas coal nuclear wind solar table; EIA Electric Power Monthly table 1.1 net generation by energy source total all sectors July 2025 thousand megawatthours; "Electric Power Monthly" May 2026 total net summer capacity all sources megawatts table 6.2.A

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?month=july2024&t=table_1_01` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_6_02_a&year=2020` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/monthly/archive/march2026.pdf` -> **snapshot** (snapshot 20260505021405) **LEAK SENTINEL HIT ['(?<![\\d.,])10,925(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.eia.gov/todayinenergy/detail.php?id=67205` -> **snapshot** (snapshot 20260825093133); points raw/verified 15/0
- dropped by code checks: 15 (number: unknown scale word 'gigawatts': 1; period_end 2026-12-31 after as_of: 3; number: unknown scale word 'GW': 11)

### d7 [related_series] Fuel-by-fuel decomposition

Hypothesis: Summing generation by fuel (natural gas, coal, nuclear, hydro, wind, solar utility-scale, other) for July 2026, each estimated from its own driver (gas prices/gas burn, nuclear outages, hydro conditions, wind/solar capacity), reconstructs the total and reveals which fuel drives deviation from prior July.

Queries issued by the searcher: EIA Electric Power Monthly July 2026 net generation by energy source; natural gas power burn July 2026 EIA; nuclear generation July 2026 outages refueling EIA; EIA-930 July 2026 total US generation coal year-over-year down 9% natural gas

- `https://naturalgasintel.com/news/natural-gas-power-burn-slips-from-one-year-high-as-wind-roars-back/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://blog.synmax.com/hyperion-client/weekly-storage-and-s/d-brief-week-ending-7/10/2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01` -> **snapshot** (snapshot 20260811222555); points raw/verified 0/0
- `https://aegis-hedging.com/insights/gas-power-demand-underperforms` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [base_rates] Seasonal share of annual total

Hypothesis: July typically accounts for a stable share (~9-10%) of annual US utility-scale generation; applying that share to a 2026 annual total (from STEO or trend) yields the July estimate. The share is stable but shifts slightly with weather and renewables growth.

Queries issued by the searcher: EIA Short-Term Energy Outlook 2026 total electricity generation forecast billion kilowatthours; EIA Electric Power Monthly July 2025 net generation all sectors total table 1.1; July share annual US electricity generation percent 2024 2023 EIA; site:eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_1 July 2025 425,455; EIA total net generation July 2024 2023 2022 2021 thousand megawatthours annual total; EIA STEO July 2026 electricity generation 2026 forecast table

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_1` -> **snapshot** (snapshot 20260724011053); points raw/verified 0/0
- `https://www.eia.gov/outlooks/steo/pdf/steo_tables.pdf` -> **snapshot** (snapshot 20251123072750); points raw/verified 15/6
  - p32 U.S. total utility-scale electricity generation, all sectors, annual total (2025 = **4,408** billion kilowatthours (2025-01-01..2025-12-31) [keep: ] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
  - p33 U.S. total utility-scale electricity generation, all sectors, annual total (2024 = **4,309** billion kilowatthours (2024-01-01..2024-12-31) [keep: ] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
  - p34 U.S. total utility-scale electricity generation, all sectors, Q3 2025 = **1,232** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
  - p35 U.S. total utility-scale electricity generation, all sectors, Q3 2024 = **1,212** billion kilowatthours (2024-07-01..2024-09-30) [keep: ] quote: "Electricity generation (a) ................................................. 1,028 1,051 1,212 1,018 1,074 1,057 1,232 1,044 1,068 1,084 1,298 1,086 4,309 4,408 4,536"
  - p36 U.S. electric power sector total generation, Q3 2025 = **1,193** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Total generation .......................... 989.6 1,013.9 1,172.3 980.9 1,035.7 1,020.7 1,192.6 1,005.9 1,029.7 1,046.4 1,258.2 1,047.4 4,156.6 4,254.8 4,381.7"
  - p37 U.S. electric power sector total generation, Q3 2024 = **1,172** billion kilowatthours (2024-07-01..2024-09-30) [keep: ] quote: "Total generation .......................... 989.6 1,013.9 1,172.3 980.9 1,035.7 1,020.7 1,192.6 1,005.9 1,029.7 1,046.4 1,258.2 1,047.4 4,156.6 4,254.8 4,381.7"
- `https://www.eia.gov/todayinenergy/detail.php?id=67005` -> **snapshot** (snapshot 20260802184508); points raw/verified 15/4
  - p38 U.S. electric power sector total electricity generation, 2025 (STEO January 2026 = **4,260,000,000,000** kilowatthours (BkWh) (2025-01-01..2025-12-31) [keep: ] quote: "Electricity generation by the U.S. electric power sector totaled about 4,260 billion kilowatthours (BkWh) in 2025."
  - p39 Combined share of natural gas, coal, and nuclear in U.S. total generation, 2025 = **75** % (2025-01-01..2025-12-31) [keep: ] quote: "The three main dispatchable sources of electricity generation (natural gas, coal, and nuclear) accounted for 75% of total generation in 2025"
  - p40 Combined share of solar and wind in U.S. total generation, 2025 = **18** % (2025-01-01..2025-12-31) [keep: ] quote: "We expect the combined share of generation from solar power and wind power to rise from about 18% in 2025 to about 21% in 2027."
  - p41 Natural gas share of U.S. total power generation, 2025 = **40** % (2025-01-01..2025-12-31) [keep: ] quote: "natural gas's share of total power generation falls to 39% in 2027 compared to 40% in 2025"
- `https://www.eia.gov/totalenergy/data/monthly/pdf/sec7.pdf` -> **snapshot** (snapshot 20260804131454) **LEAK SENTINEL HIT ['(?<![\\d.,])10,925(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- dropped by code checks: 20 (period_end 2026-12-31 after as_of: 6; period_end 2026-09-30 after as_of: 4; period_end 2027-12-31 after as_of: 3; scale word 'billion' not supported by quote or table header: 7)

### b1 [related_series] d2/d3

Hypothesis: EIA-930 Hourly Electric Grid Monitor daily Lower-48 net generation summed over July 2026 would give a near-complete utility-scale proxy; scaling by the historical Lower-48 share of total U.S. utility-scale generation (~98-99%) yields the target. This is the single most direct route and would dominate the estimate if available.

Queries issued by the searcher: EIA-930 Hourly Electric Grid Monitor daily net generation Lower-48 July 2026; EIA Electric Power Monthly Table 1.1 Net Generation by Energy Source Total All Sectors July 2026; EIA hourly electric grid monitor "Lower 48" net generation July 2026 daily total GWh; "EIA-930" net generation lower than Electric Power Monthly utility-scale comparison percent

- `https://worldpowermonitor.com/data/eia-us-grid-daily/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/gridmonitor/about` -> **snapshot** (snapshot 20260804211839); points raw/verified 0/0
- `https://catalystcoop-pudl.readthedocs.io/en/stable/data_sources/eia930.html` -> **snapshot** (snapshot 20260415235520); points raw/verified 15/14
  - p42 EIA-930 temporal coverage start (half-year) = **2,015** as written "2015half2", value check pending half-year label (2015-07-01..2015-12-31) [keep: ] quote: "\| Temporal Coverage \| 2015half2-2026half1 \|"
  - p43 EIA-930 temporal coverage end (half-year) = **2,026** as written "2026half1", value check pending half-year label (2026-01-01..2026-06-30) [keep: ] quote: "\| Temporal Coverage \| 2015half2-2026half1 \|"
  - p44 Example asymmetric interchange: entity A reported receiving (MWh) = **100** MWh (not stated (page dated 2018-07-01)) [keep: ] quote: "entity A might report receiving 100 MWh of energy from entity B"
  - p45 Example asymmetric interchange: entity B reported sending (MWh) = **50** MWh (not stated (page dated 2018-07-01)) [keep: ] quote: "while entity B only reports sending 50 MWh of energy to entity A"
  - p46 Factor by which sum of net generation by energy source can differ from total rep = **10** factor (ratio) (not stated (page dated 2018-07-01)) [keep: ] quote: "for some BAs (typically the smaller ones) it can be off by factor of 10 or more"
  - p47 Start date for demand by subregion availability for select BAs = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [keep: ] quote: "Demand by subregion (available for select BAs beginning 2018-07-01)"
  - p48 Start date for net generation by energy source availability = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [keep: ] quote: "Net generation by energy source (beginning 2018-07-01)"
  - p49 Start date for estimated total CO2 emissions data = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [keep: ] quote: "Estimated total CO2 emissions (beginning 2018-07-01)"
  - p50 Start date for estimated CO2 emissions by fuel type = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [keep: ] quote: "Estimated CO2 emissions by fuel type (beginning 2018-07-01)"
  - p51 Start date for estimated CO2 emissions for electricity imports or exports = **2,018** as written "2018-07-01", value check pending date (2018-07-01..2018-07-01) [keep: ] quote: "Estimated CO2 emissions for electricity imports or exports (beginning 2018-07-01)"
  - p52 Effective start (half-year) of new wind/solar/hydro/storage energy source column = **2,024** as written "2024half2", value check pending half-year label (2024-07-01..2024-12-31) [keep: ] quote: "The change takes effect starting in 2024half2."
  - p53 Data release quarter when wind/solar/hydro columns were removed and new columns  = **1** as written "Q1 2025", value check pending quarter of year (2025-01-01..2025-03-31) [keep: ] quote: "In the Q1 2025 data release, the wind, solar, and hydro power energy source columns were removed from the raw dataset"
  - p54 Data release quarter when imputed/adjusted 'unknown' energy source columns were  = **2** as written "Q2 2025", value check pending quarter of year (2025-04-01..2025-06-30) [keep: ] quote: "In the Q2 2025 data release, imputed and adjusted columns for the "unknown" energy source were added to the raw dataset"
  - p55 Zenodo archive DOI identifier for unprocessed EIA-930 source data = **10.53** DOI (not stated (page dated 2018-07-01)) [keep: ] quote: "\| Unprocessed Source Data Archive \| 10.5281/zenodo.10840077 \|"
- `https://www.eia.gov/electricity/gridmonitor/` -> **snapshot** (snapshot 20260822121031); points raw/verified 0/0
- dropped by code checks: 1 (number: unknown scale word 'MB': 1)

### b2 [own_history] d1/d8

Hypothesis: Monthly utility-scale net generation for July 2023, July 2024, and July 2025 (EIA EPM Table 1.1 or equivalent) would anchor the July level and let a YoY growth factor (from p6/p29) project July 2026. Without these monthly July values the series methods cannot run.

Queries issued by the searcher: EIA Electric Power Monthly Table 1.1 Net Generation by Energy Source Total All Sectors July 2025; EIA electricity net generation July 2024 total all sectors gigawatt-hours monthly; "Electric Power Monthly" September 2025 pdf "Table 1.1" Net Generation by Energy Source Total All Sectors 2016-July 2025; Electric Power Monthly September 2023 data for July 2023 total net generation thousand megawatthours table 1.1

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01` -> **snapshot** (snapshot 20260811222555); points raw/verified 0/0
- `https://www.eia.gov/electricity/monthly/archive/september2025.pdf` -> **snapshot** (snapshot 20260505021148) **LEAK SENTINEL HIT ['(?<![\\d.,])10,900(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.eia.gov/electricity/monthly/archive/september2023.pdf` -> **snapshot** (snapshot 20260505021155); points raw/verified 14/1
  - p56 U.S. total utility-scale net generation, all sectors, all energy sources, July 2 = **0.4** % (2023-07-01..2023-07-31) [keep: ] quote: "All Energy Sources Utility Scale Facilities 425,655 424,013 0.4%"
- `https://www.eia.gov/electricity/monthly/update/archive/september2024/resource-use.php` -> **snapshot** (snapshot 20260505215139); points raw/verified 15/15
  - p57 U.S. net electricity generation year-over-year change, July 2024 vs July 2023 = **1.1** % (2024-07-01..2024-07-31) [keep: ] quote: "Net electricity generation in the United States increased 1.1% compared to the previous July."
  - p58 Texas year-over-year change in electricity generation, July 2024 vs July 2023 = **4.1** % (2024-07-01..2024-07-31) [keep: ] quote: "Texas, in particular, saw a large year-over-year drop in electricity generation (down 4.1%)"
  - p59 Henry Hub natural gas spot price, July 2024 = **2.1** USD per MMBtu (2024-07-01..2024-07-31) [keep: ] quote: "going from $2.54/MMBtu in June 2024 to $2.10/MMBtu in July 2024"
  - p60 Henry Hub natural gas spot price, June 2024 = **2.54** USD per MMBtu (2024-06-01..2024-06-30) [keep: ] quote: "going from $2.54/MMBtu in June 2024 to $2.10/MMBtu in July 2024"
  - p61 Transco Zone 6 NY natural gas price, July 2024 = **1.62** USD per MMBtu (2024-07-01..2024-07-31) [keep: ] quote: "going from $1.82/MMBtu in June 2024 to $1.62/MMBtu in July 2024"
  - p62 Transco Zone 6 NY natural gas price, June 2024 = **1.82** USD per MMBtu (2024-06-01..2024-06-30) [keep: ] quote: "going from $1.82/MMBtu in June 2024 to $1.62/MMBtu in July 2024"
  - p63 Central Appalachian coal spot price, July 2024 = **3.26** USD per MMBtu (2024-07-01..2024-07-31) [keep: ] quote: "going from $3.46/MMBtu in June 2024 to $3.26/MMBtu in July 2024"
  - p64 Central Appalachian coal spot price, June 2024 = **3.46** USD per MMBtu (2024-06-01..2024-06-30) [keep: ] quote: "going from $3.46/MMBtu in June 2024 to $3.26/MMBtu in July 2024"
  - p65 New York Harbor residual oil price, July 2024 = **12.91** USD per MMBtu (2024-07-01..2024-07-31) [keep: ] quote: "going from $12.93/MMBtu in June 2024 to $12.91/MMBtu in July 2024"
  - p66 New York Harbor residual oil price, June 2024 = **12.93** USD per MMBtu (2024-06-01..2024-06-30) [keep: ] quote: "going from $12.93/MMBtu in June 2024 to $12.91/MMBtu in July 2024"
  - p67 Henry Hub natural gas price on equivalent energy content and efficiency basis, J = **16.82** USD per MWh (2024-07-01..2024-07-31) [keep: ] quote: "The Henry Hub natural gas price ($16.82/MWh) saw a decrease from the previous month ($20.31/MWh)"
  - p68 Henry Hub natural gas price on equivalent energy content and efficiency basis, J = **20.31** USD per MWh (2024-06-01..2024-06-30) [keep: ] quote: "saw a decrease from the previous month ($20.31/MWh)"
  - p69 Central Appalachian coal price on equivalent energy content and efficiency basis = **35.22** USD per MWh (2024-07-01..2024-07-31) [keep: ] quote: "was well below the Central Appalachian coal price ($35.22/MWh) in July 2024"
  - p70 New York City natural gas price on equivalent energy content and efficiency basi = **13** USD per MWh (2024-07-01..2024-07-31) [keep: ] quote: "The price of natural gas at New York City ($13.00/MWh) decreased from the previous month ($14.58/MWh)"
  - p71 New York City natural gas price on equivalent energy content and efficiency basi = **14.58** USD per MWh (2024-06-01..2024-06-30) [keep: ] quote: "decreased from the previous month ($14.58/MWh)"
- dropped by code checks: 13 (scale word 'thousand' not supported by quote or table header: 13)

### b3 [shocks] d4

Hypothesis: National cooling-degree-day anomalies for July 2026 versus July 2025 (NOAA CPC) would quantify the weather-driven deviation from the prior-year July, resolving whether the hot PJM/ERCOT signals (p17-p28) imply a national above-normal July or a regionally concentrated one.

Queries issued by the searcher: NOAA CPC population-weighted cooling degree days July 2026; cooling degree days July 2026 United States above normal NOAA; AGA "Weekly Cooling Degree Day Data" August 2026 July 2026 percent warmer than normal; cpc.ncep.noaa.gov daily degree days CONUS monthly statistics July 2026 population weighted

- `https://www.aga.org/wp-content/uploads/2026/08/Current-Cooling-Degree-Day-Data_Paul-Pierson-80.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://climateimpactcompany.com/u-s-gas-power-report-the-2026-u-s-population-weight-cdd-forecast-2/` -> **snapshot** (snapshot 20260417084210); points raw/verified 15/11
  - p72 U.S. population-weighted CDD projection for July 2026 = **355** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p73 U.S. 30-year normal CDD for July = **321** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p74 U.S. 10-year normal CDD for July = **372** cooling degree days (2026-07-01..2026-07-31) [keep: ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p75 U.S. July CDD, most recent past year (2025) = **376** cooling degree days (2025-07-01..2025-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p76 U.S. July CDD, second past year (2024) = **370** cooling degree days (2024-07-01..2024-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p77 U.S. July CDD, third past year (2023) = **371** cooling degree days (2023-07-01..2023-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p78 U.S. CDD projection for June 2026 = **246** cooling degree days (2026-06-01..2026-06-30) [keep: ] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p79 U.S. 10-year normal CDD for June = **253** cooling degree days (2026-06-01..2026-06-30) [keep: ] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p80 U.S. CDD projection for May 2026 = **121** cooling degree days (2026-05-01..2026-05-31) [keep: ] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
  - p81 U.S. 10-year normal CDD for May = **116** cooling degree days (2026-05-01..2026-05-31) [keep: ] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
  - p82 U.S. CDD for May 2025 (last year) = **102** cooling degree days (2025-05-01..2025-05-31) [keep: ] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
- `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/cdus/degree_days/` -> **snapshot** (snapshot 20260517113300); points raw/verified 0/0
- `https://www.aga.org/research-policy/resource-library/natural-gas-market-indicators-july-23-2026/` -> **snapshot** (snapshot 20260810195523); points raw/verified 15/14
  - p83 U.S. cooling degree days weighted by electric home air conditioning customers, w = **4.7** % (2026-07-12..2026-07-18) [keep: ] quote: "For the week ending July 18, temperatures in the U.S. were 4.7 percent warmer than last year"
  - p84 U.S. cooling degree days weighted by electric home air conditioning customers, w = **21.6** % (2026-07-12..2026-07-18) [keep: ] quote: "and 21.6 percent warmer than the 30-year normal, according to cooling degree days weighted by electric home air conditioning customers."
  - p85 U.S. total natural gas demand including exports, month-to-date through July 23,  = **2.7** % (2026-07-01..2026-07-23) [keep: ] quote: "total demand, including exports, is 7.7 percent higher month-to-date through July 23 than during the same period in June and 2.7 percent higher than last year."
  - p86 U.S. total natural gas demand including exports, month-to-date through July 23,  = **2.7** % (2026-07-01..2026-07-23) [keep: ] quote: "Total demand is also tracking 2.7 percent above the previous July record, putting the month on pace to set a new high."
  - p87 U.S. domestic natural gas consumption, month-to-date through July 23, 2026, perc = **0.6** % (2026-07-01..2026-07-23) [keep: ] quote: "Exports are the primary source of year-over-year demand growth, while domestic consumption is 0.6 percent higher."
  - p88 U.S. electric power natural gas demand, month-to-date through July 23, 2026, per = **1.1** % (2026-07-01..2026-07-23) [keep: ] quote: "Year-over-year domestic consumption growth reflects a 1.1 percent increase in electric power demand"
  - p89 U.S. electric power natural gas demand, month-to-date through July 23, 2026, per = **4.2** % (2026-07-01..2026-07-23) [keep: ] quote: "Despite above-normal temperatures and higher power-sector consumption than last year, electric power demand remains 4.2 percent below the July 2024 record."
  - p90 Planned or early-stage fossil-fueled generating capacity, Q2 2026, total (GW) = **157** gigawatts (2026-04-01..2026-06-30) [keep: ] quote: "Planned or early-stage fossil-fueled generating capacity increased only 1 percent from the previous quarter to 156.9 GW"
  - p91 Natural gas share of planned or early-stage fossil-fueled generating capacity, Q = **98** % (2026-04-01..2026-06-30) [keep: ] quote: "Natural gas still accounts for approximately 98 percent of that capacity"
  - p92 U.S. LNG feedgas deliveries, week ending July 22, 2026, average (Bcf per day) = **16.9** Bcf per day (2026-07-16..2026-07-22) [keep: ] quote: "feedgas deliveries averaged 16.9 Bcf per day for the week ending July 22, down 1.6 percent from the previous week but still 6.8 percent higher than last year."
  - p93 U.S. LNG feedgas deliveries, month-to-date through July 23, 2026, average (Bcf p = **17.4** Bcf per day (2026-07-01..2026-07-23) [keep: ] quote: "Month-to-date flows have averaged 17.4 Bcf per day, above the latest weekly average but below the 18 to 19 Bcf per day range recorded earlier this year."
  - p94 U.S. LNG feedgas deliveries earlier in 2026, lower bound of recorded range (Bcf  = **18** Bcf per day (2026-01-01..2026-07-23) [keep: ] quote: "below the 18 to 19 Bcf per day range recorded earlier this year"
  - p95 U.S. LNG feedgas deliveries earlier in 2026, upper bound of recorded range (Bcf  = **19** Bcf per day (2026-01-01..2026-07-23) [keep: ] quote: "below the 18 to 19 Bcf per day range recorded earlier this year"
  - p96 Lower 48 dry natural gas production, month-to-date through July 23, 2026, percen = **2.5** % (2026-07-01..2026-07-23) [keep: ] quote: "dry natural gas output for the lower 48 is up 0.2 percent compared to the same period in June and 2.5 percent higher than the same period last year."
- dropped by code checks: 5 (period_end 2026-08-31 after as_of: 2; period_end 2026-09-30 after as_of: 2; period_end 2026-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['us electricity generation', 'july power demand', 'eia generation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p32', 'p33'] All describe U.S. annual utility-scale net generation levels and growth; p1 (4,430 TWh, 2025) and p32 (4,408 BkWh, 2025 STEO) are close but from different vintages/definitions (all-sectors vs utility-
- corroborating: ['p30', 'p31', 'p34', 'p35', 'p36', 'p37'] STEO quarterly generation figures for Q3 2024 and Q3 2025; p30/p34 are the same Q3 2025 value (1,232 BkWh) and p31/p35 the same Q3 2024 value (1,212 BkWh), so they are redundant copies of one STEO vin
- corroborating: ['p38', 'p39', 'p40', 'p41'] January 2026 STEO statements about 2025 electric power sector generation (4,260 BkWh) and fuel shares; internally consistent with p32/p1 and useful for fuel-mix structure, but all from one EIA STEO vi
- corroborating: ['p6', 'p29'] Both indicate 2026 generation running above 2025: p6 gives +3.1% YoY for May 2026, p29 gives +1.8% for 1H26. Different periods but same direction and similar magnitude; both from EIA, so not fully ind
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25'] All from one EPRI article on a late-June/early-July 2026 PJM heat wave; internally consistent (dispatchable 88% of ~127 GW average load; nuclear+coal+gas = 111.6 GW). They describe PJM only and a sing
- corroborating: ['p26', 'p27', 'p28'] All from one EIA Today-in-Energy piece on the ERCOT July 22, 2026 record peak; the 6% record increase and gas/solar shares are consistent with a hot July 2026 in ERCOT. Regional, not national.
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16'] May 2026 fuel prices from one EIA STEO/merchant report; gas and coal prices are moderate, implying gas remains economic for marginal generation. Prices are inputs to fuel-switching, not generation lev
- corroborating: ['p3', 'p4', 'p5'] 2025 retail sales growth by sector (residential 2.2%, commercial 2.9%, industrial 0.7%) from one EIA report; supports modest demand growth into 2026 but is a different quantity (retail sales, not net 
- conflicting: ['p1', 'p32'] Minor definitional/vintage discrepancy: 4,430 TWh (all-sector, March 2026 report) vs 4,408 BkWh (utility-scale, Nov 2025 STEO). Not a true contradiction; reflects scope (all sectors vs utility-scale) 
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p32', 'p38'] All three are 2025 annual U.S. generation totals from EIA, but they differ in scope and vintage: p1 (4,430 TWh) is all-sector net generation, p32 (4,408 BkWh) is all-sector utility-scale from the Nove
- corroborating: ['p34', 'p35', 'p36', 'p37'] Q3 totals from the same STEO table. p34/p35 are all-sector utility-scale Q3 2025/2024; p36/p37 are electric-power-sector Q3 2025/2024. The all-sector vs power-sector gap (~39 BkWh/quarter) is consiste
- corroborating: ['p56', 'p57'] Both are July YoY growth rates for all-sector utility-scale net generation (2023: +0.4%, 2024: +1.1%). They establish that recent July YoY growth has been modest and positive, supporting a low-single-
- corroborating: ['p6', 'p29'] p6 (May 2026 YoY +3.1%) and p29 (1H26 electric-power-sector generation +37 BkWh, +1.8% vs 1H25) both indicate 2026 generation is running above 2025. They differ in scope (p6 all-sector monthly, p29 po
- conflicting: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77'] The April 2026 CDD projection (p72, 355) is below the 10-year normal (p74, 372) and below each of the last three Julys (p75-p77: 376, 370, 371). If realized, July 2026 would be cooler than July 2025, 
- corroborating: ['p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89'] AGA data through July 23, 2026 show temperatures 4.7% warmer than last year and 21.6% above 30-year normal (p83-p84), total gas demand 2.7% above last July's record (p85-p86), and electric-power gas d
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28'] Regional heat-wave and peak-demand evidence (PJM late-June/early-July heat wave, ERCOT July 22 record peak 6% above prior record) confirms strong summer 2026 cooling demand in major regions. These are
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p14', 'p15'] May 2026 fuel prices (Henry Hub $2.90/MMBtu, coal $3.48/MMBtu, NYC gas $2.07/MMBtu) are low and stable, with gas far cheaper than coal on an efficiency-adjusted basis ($23.26 vs $37.58/MWh). This favo
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71'] July/June 2024 fuel prices from the same EIA series provide historical context for the fuel-price-to-generation relationship. They are older and not directly needed for a July 2026 level, but they are
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55'] EIA-930 documentation points describe data availability and known quality issues (asymmetric interchange, factor-of-10 discrepancies in small BAs, schema changes). They confirm that a direct EIA-930 J
- corroborating: ['p2', 'p3', 'p4', 'p5'] 2025 annual growth (+2.8% generation; retail sales +2.2% residential, +2.9% commercial, +0.7% industrial) establishes the recent demand trend. Retail sales growth is a demand-side corroboration of gen
- corroborating: ['p39', 'p40', 'p41'] 2025 fuel-mix shares (75% dispatchable gas+coal+nuclear; 18% solar+wind; 40% gas) describe the generation mix structure. They are context for fuel-mix reasoning (route d7) but do not supply a July 202
- corroborating: ['p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96'] Planned fossil capacity (157 GW, 98% gas), LNG feedgas flows, and dry gas production growth describe supply-side conditions. They are not generation measurements and cannot directly enter a generation

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 YoY generation growth factor vs July 2025 | 1.022 | 1.005..1.04 | 0.9144..1.143 (widened) | ratio | unused | Anchored on p29 (1H26 +1.8% YoY), p6 (May 2026 +3.1%), p88 (July electric-power gas demand +1.1% YoY), p83/p84 (July warmer than last year and than normal), and p56/p57 (recent July YoY growth of +0.4% and +1.1%). July 2025 was itself hot (CDD 376, p75) and p72 projects July 2026 cooler than 2025, s | July 2026 national weather and demand resemble the observed month-to-date AGA signals and the 1H26 trend. | A national July 2026 CDD observation well below July 2025, or a reported July 2026 YoY decline. |
| a2 | July share of annual utility-scale generation | 0.093 | 0.088..0.098 | 0.06567..0.1313 (widened) | fraction | m1 (m2) | July is the seasonal peak month; historical monthly shares of annual U.S. generation put July near 9-10%. The range reflects weather-driven variation in the peak month's share. | 2026 monthly seasonal shape resembles recent years. | A July 2026 share outside 8.8-9.8% of the annual total. |
| a3 | 2026 annual utility-scale generation growth vs 2025 | 1.02 | 1.005..1.04 | 0.9144..1.143 (widened) | ratio | m1 (m2) | Based on p29 (1H26 +1.8%), p6 (May +3.1%), and the 2025 trend (p2, +2.8%). Full-year 2026 growth should be in the low single digits, slightly above the 1H26 pace if summer demand is strong. | 2026 demand growth continues at the 1H26 pace through year-end. | A reported 2026 annual growth below 0.5% or above 4.5%. |
| a4 | July-to-quarterly-average ratio for Q3 generation | 1.02 | 0.98..1.06 | 0.7207..1.441 (widened) | ratio | unused | July is typically the hottest month and slightly above the Q3 average (August is also hot but September cools). A small uplift over one-third of Q3 is appropriate; range allows July to be near or modestly above the quarterly average. | Q3 2026 seasonal shape resembles recent years with July as the peak month. | Evidence that August 2026 was substantially hotter than July 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 418,471 | ['p32'] / ['a2', 'a3'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **418,471** GWh, 80% interval [278,477, 628,843] GWh, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total U.S. net utility-scale electricity generation (all sectors, all energy sources, excluding small-scale solar) for July 2026 is 418,471 GWh (80% model-based interval 278,477 to 628,843 GWh). This is a model-based interval conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate scales the observed 2025 annual total (4,408 billion kilowatthours) by an assumed 2026 growth ratio (1.02, range 0.9144 to 1.143) and an assumed July share of the year (0.093, range 0.06567 to 0.1313). Only the annual total is observed; the July share and growth are analyst assumptions. Code used a single method (1), so no weighting across methods applies.

The main risk is that July's share is weather-sensitive, and the growth and share assumptions share seasonal-pattern dependencies, so errors could compound. Better evidence would be recent monthly seasonal shares and mid-2026 generation data to pin down the July share and growth.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 July share of annual utility-scale generation: 0.093 fraction, range 0.06567 to 0.1313 (range widened by code); used by m1. Overturned by: A July 2026 share outside [n]-[n] of the annual total.
- a3 2026 annual utility-scale generation growth vs 2025: 1.02 ratio, range 0.9144 to 1.143 (range widened by code); used by m1. Overturned by: A reported 2026 annual growth below [n] or above [n].

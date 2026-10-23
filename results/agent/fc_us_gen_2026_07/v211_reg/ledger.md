# Evidence ledger: fc_us_gen_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate total U.S. net electricity generation at utility-scale facilities (all sectors, all energy sources, excluding small-scale solar) in July 2026, in gigawatt-hours (GWh, equal to thousand megawatthours), as it will be first reported in the U.S. Energy Information Administration's Electric Power Monthly (Table 1.1).
- as_of: 2026-08-25
- Pinned target: Total U.S. net electricity generation at utility-scale facilities, all sectors and all energy sources, excluding small-scale solar (EIA Electric Power Monthly Table 1.1 'Net Generation by Energy Source: Total (All Sectors)'), as first reported | unit gigawatt-hours (GWh, thousand megawatthours) | period 2026-07-01..2026-07-31 | publisher U.S. Energy Information Administration (EIA), Electric Power Monthly

- Official value (scoring only, never shown to the agent): 453,744

## Directions and pages

### d1 [own_history] EIA historical Table 1.1 monthly totals

Hypothesis: July 2026 total generation ≈ July 2025 total adjusted for year-over-year load growth and weather; July is typically the annual peak month. Prior July values and recent monthly values (through the latest published month before cutoff, likely May or June 2026) anchor the level and trend.

Queries issued by the searcher: EIA Electric Power Monthly Table 1.1 net generation by energy source total all sectors July 2025; EIA total net generation monthly 2026 utility-scale gigawatthours; "June 2026" EIA net generation total all sectors "Electric Power Monthly" release August 2026; July 2025 total U.S. net generation "billion kilowatthours" utility-scale record July EIA 433

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01` -> **snapshot** (snapshot 20260811222555); points raw/verified 0/0
- `https://www.eia.gov/totalenergy/data/monthly/pdf/sec7.pdf` -> **snapshot** (snapshot 20260804131454) **LEAK SENTINEL HIT ['(?<![\\d.,])10,925(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://topedb.com/p/280031` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://electrek.co/2025/09/24/eia-solar-and-wind-crush-coal-with-20-percent-more-power-in-2025/` -> **snapshot** (snapshot 20260601153516); points raw/verified 15/15
  - p1 Utility-scale solar net generation, US, July 2025 = **33,119** GWh (2025-07-01..2025-07-31) [keep: ] quote: "4% more electricity was generated in July by utility-scale solar (33,119-GWh)"
  - p2 Wind net generation, US, July 2025 = **31,831** GWh (2025-07-01..2025-07-31) [keep: ] quote: "than by wind farms (31,831-GWh)"
  - p3 Combined utility-scale and small-scale solar net generation, US, July 2025 = **43,092** GWh (2025-07-01..2025-07-31) [keep: ] quote: "solar outproduced wind by over 35% during the month (43,092 GWh)"
  - p4 Year-over-year growth rate of utility-scale solar generation, US, July 2025 vs J = **36.9** % (2025-07-01..2025-07-31) [keep: ] quote: "electrical generation by utility-scale solar (i.e., >1-megawatt (MW)) surged by 36.9% compared to July 2024"
  - p5 Year-over-year growth rate of estimated small-scale solar PV generation, US, Jul = **12.7** % (2025-07-01..2025-07-31) [keep: ] quote: "while "estimated" small-scale (e.g., rooftop) solar PV increased by 12.7%"
  - p6 Year-over-year growth rate of combined utility-scale and small-scale solar gener = **30.4** % (2025-07-01..2025-07-31) [keep: ] quote: "Combined, they grew by 30.4% and provided 9.4% of US electrical output"
  - p7 Share of US electrical output from combined utility-scale and small-scale solar, = **9.4** % (2025-07-01..2025-07-31) [keep: ] quote: "Combined, they grew by 30.4% and provided 9.4% of US electrical output, up from 7.5% year-over-year."
  - p8 Share of US electrical output from combined utility-scale and small-scale solar, = **7.5** % (2024-07-01..2024-07-31) [keep: ] quote: "provided 9.4% of US electrical output, up from 7.5% year-over-year"
  - p9 Year-over-year growth rate of wind generation, US, July 2025 vs July 2024 = **13.8** % (2025-07-01..2025-07-31) [keep: ] quote: "In July alone, wind-generated electricity was 13.8% greater than a year before."
  - p10 Year-over-year growth rate of total US electrical generation, January-July 2025  = **3.3** % (2025-01-01..2025-07-31) [keep: ] quote: "Electrical generation by the combination of all renewables grew three times faster than total US electrical generation (9.9% vs. 3.3%)."
  - p11 Year-over-year growth rate of all renewables combined generation, US, January-Ju = **9.9** % (2025-01-01..2025-07-31) [keep: ] quote: "All renewables combined (wind, solar, hydropower, biomass, and geothermal) produced 9.9% more electricity between January and July than they did a year ago"
  - p12 Share of total US electrical generation from all renewables combined, January-Ju = **26.7** % (2025-01-01..2025-07-31) [keep: ] quote: "and provided 26.7% of total US electricity production compared to 25.1% 12 months earlier"
  - p13 Share of total US electrical generation from all renewables combined, January-Ju = **25.1** % (2024-01-01..2024-07-31) [keep: ] quote: "provided 26.7% of total US electricity production compared to 25.1% 12 months earlier"
  - p14 Share of total US electrical generation from wind, January-July 2025 = **10.8** % (2025-01-01..2025-07-31) [keep: ] quote: "US wind turbines produced 10.8% of US electricity in the first seven months of 2025"
  - p15 Year-over-year change in natural gas electrical output, US, January-July 2025 vs = **3.5** % (2025-01-01..2025-07-31) [keep: ] quote: "natural gas, which saw a decline in electrical output by almost 3.5% during the first seven months of 2025"

### d2 [related_series] EIA-930 hourly/grid monitor and weekly generation data

Hypothesis: EIA-930 daily/hourly balancing-authority generation summed over July 2026 gives a near-complete utility-scale total; scaling by coverage share yields the Table 1.1 total. Weekly EIA data through July 2026 may be published before the cutoff.

Queries issued by the searcher: EIA-930 hourly electric grid monitor July 2026 net generation; EIA weekly electricity generation 2026 thousand megawatthours; EIA-930 net generation lower than Electric Power Monthly coverage share percent utility-scale; "July 2026" total US electricity generation terawatt-hours EIA-930 record demand summer

- `https://naturalgasintel.com/news/natural-gas-power-burn-slips-from-one-year-high-as-wind-roars-back/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.naturalgasintel.com/news/natural-gas-power-generation-trails-year-ago-by-10-as-wind-output-soars-96/` -> **snapshot** (snapshot 20260707205710); points raw/verified 2/2
  - p16 Year-over-year change in wind generation, US, latest EIA storage week = **96** % (not stated (page dated 2026-07-07)) [DISCARD: A 96% YoY wind jump for an unspecified 'latest EIA storage week' is implausible as a level signal and the period is not ] quote: "Wind output jumps 96% year/year"
  - p17 Year-over-year change in total US power demand, latest EIA storage week = **2** % (not stated (page dated 2026-07-07)) [DISCARD: 2% YoY demand change for an unspecified week; period undefined and redundant with p98/p99/p60 which give cleaner 2026 gr] quote: "Total power demand rose 2% year/year"
- `https://catalystcoop-pudl.readthedocs.io/en/stable/data_sources/eia930.html` -> **snapshot** (snapshot 20260415235520); points raw/verified 0/0
- `https://www.eia.gov/todayinenergy/detail.php?id=67906` -> **snapshot** (snapshot 20260823205518); points raw/verified 6/6
  - p18 ERCOT record hourly peak load, July 22, 2026 = **91.1** gigawatts (2026-07-22..2026-07-22) [keep: ] quote: "Hourly peak load in the Electric Reliability Council of Texas (ERCOT), the regional transmission organization serving most of Texas, reached a record 91.1 gigawatts (GW) on July 22, 2026"
  - p19 ERCOT previous record hourly peak load, August 10, 2023 = **85.5** gigawatts (2023-08-10..2023-08-10) [DISCARD: Duplicate of p91 (same ERCOT previous record figure); redundant copy.] quote: "The July 22 peak was 6% greater than the previous peak of 85.5 GW, set on August 10, 2023 according to ERCOT."
  - p20 Percent by which July 22, 2026 ERCOT peak exceeded previous peak = **6** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p90 (same 6% figure); redundant copy.] quote: "The July 22 peak was 6% greater than the previous peak of 85.5 GW, set on August 10, 2023 according to ERCOT."
  - p21 Share of July 22, 2026 ERCOT peak met with natural gas generation = **48** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p92 (same ERCOT gas share); redundant copy.] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
  - p22 Share of July 22, 2026 ERCOT peak met with solar generation = **32** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p93 (same ERCOT solar share); redundant copy.] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
  - p23 Southwest Power Pool record electricity demand, July 27, 2026 = **57.9** gigawatts (2026-07-27..2026-07-27) [keep: ] quote: "More recently, electricity demand in the Southwest Power Pool reached a record 57.9 GW on July 27 at 5:00 p.m. CT."

### d3 [forecasts_markets] EIA Short-Term Energy Outlook and other forecasts

Hypothesis: EIA STEO (published before cutoff, e.g., July or August 2026) forecasts monthly U.S. electricity generation; its July 2026 projection is a direct estimate of the target, subject to forecast error.

Queries issued by the searcher: EIA Short-Term Energy Outlook July 2026 electricity generation forecast; STEO forecast US power generation 2026 total generation billion kWh; EIA STEO Table 7 electricity generation monthly forecast "2026" July August September billion kilowatthours; "Short-Term Energy Outlook" August 2026 electricity generation forecast monthly July 2026

- `https://zenodo.org/records/21321403` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://journal.jogmec.go.jp/coal/news-flash/news-flash_11402.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestar.com.my/tech/tech-news/2026/07/08/us-power-use-to-beat-record-highs-in-2026-and-2027-as-ai-use-surges-eia-says` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/pdf/steo_tables.pdf` -> **snapshot** (snapshot 20251123072750); points raw/verified 15/0
- dropped by code checks: 15 (period_end 2026-09-30 after as_of: 14; period_end 2026-12-31 after as_of: 1)

### d4 [capacity_consumption] Grid operators and capacity/utilisation

Hypothesis: Total generation = installed utility-scale capacity × capacity factor × hours in July. Summer peak capacity factors and record demand (load) drive July output; peak demand records and reserve margins constrain the total.

Queries issued by the searcher: EIA Electric Power Monthly July 2026 net generation by energy source total all sectors; EIA installed generating capacity 2026 summer capacity by source megawatts; EIA Short-Term Energy Outlook July 2026 electricity generation forecast total U.S. billion kWh 2026; July 2026 peak demand record ERCOT PJM MISO ISO record load

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_01` -> **snapshot** (snapshot 20260505052814); points raw/verified 15/15
  - p24 Total U.S. utility-scale net summer capacity, all sectors and energy sources (TO = **1,284,922** megawatts (not stated (page dated 2026-05-01)) [DISCARD: Duplicate of p25 (same existing-capacity total, different column); redundant copy.] quote: "\| TOTAL \| UTILITY SCALE FACILITIES \| 1,284,921.9 \| 6,138.3 \| 832.0 \| 1,290,228.2 \|"
  - p25 Total U.S. utility-scale net summer capacity after reported additions (TOTAL row = **1,290,228** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| TOTAL \| UTILITY SCALE FACILITIES \| 1,284,921.9 \| 6,138.3 \| 832.0 \| 1,290,228.2 \| 5,306.3 \| 9,421.5 \| 53,390.7 \|"
  - p26 Total U.S. utility-scale net summer capacity including planned additions (TOTAL  = **1,366,122** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| 10,732.1 \| 75,893.4 \| 1,300,960.3 \| 1,366,121.6 \|"
  - p27 Natural gas subtotal utility-scale net summer capacity = **511,621** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Natural Gas Subtotal \| Utility Scale Facilities \| 511,620.8 \| 1,050.1 \| 326.1 \| 512,344.8 \|"
  - p28 Coal subtotal utility-scale net summer capacity = **169,972** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Coal Subtotal \| Utility Scale Facilities \| 169,971.6 \| 1,841.1 \| 5.6 \| 171,807.1 \|"
  - p29 Nuclear utility-scale net summer capacity = **98,438** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ... Nuclear \| Utility Scale Facilities \| 98,437.9 \| 17.0 \| 14.0 \| 98,440.9 \|"
  - p30 Renewable sources subtotal utility-scale net summer capacity = **407,260** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ... Renewable Sources Subtotal \| Utility Scale Facilities \| 407,260.1 \| 1,719.7 \| 190.7 \| 408,789.1 \|"
  - p31 Wind (summer capacity) subtotal utility-scale net summer capacity = **159,509** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Wind (Summer Capacity) \| Utility Scale Facilities \| 159,508.9 \| 17.6 \| 10.3 \| 159,516.2 \|"
  - p32 Solar subtotal utility-scale net summer capacity = **153,934** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Solar Subtotal \| Utility Scale Facilities \| 153,934.3 \| 1,683.4 \| 139.7 \| 155,478.0 \|"
  - p33 Conventional hydroelectric utility-scale net summer capacity = **79,944** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Conventional Hydroelectric \| Utility Scale Facilities \| 79,943.6 \| 6.5 \| 0.0 \| 79,950.1 \|"
  - p34 Batteries utility-scale net summer capacity = **43,372** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ...... Batteries \| Utility Scale Facilities \| 43,372.0 \| 1,316.2 \| 57.5 \| 44,630.7 \|"
  - p35 Energy storage subtotal utility-scale net summer capacity = **66,578** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ... Energy Storage Subtotal \| Utility Scale Facilities \| 66,577.5 \| 1,316.2 \| 57.5 \| 67,836.2 \|"
  - p36 Fossil fuels subtotal utility-scale net summer capacity = **711,190** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ... Fossil Fuels Subtotal \| Utility Scale Facilities \| 711,189.5 \| 3,077.8 \| 569.8 \| 713,697.5 \|"
  - p37 Estimated small-scale solar photovoltaic capacity (small scale facilities) = **59,950** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ......... Estimated Small Scale Solar Photovoltaic \| Small Scale Facilities \| 59,950.1 \| \| \| 60,197.9 \|"
  - p38 Natural gas fired combined cycle utility-scale net summer capacity = **293,935** megawatts (not stated (page dated 2026-05-01)) [keep: ] quote: "\| ......... Natural Gas Fired Combined Cycle \| Utility Scale Facilities \| 293,935.2 \| 273.0 \| 130.8 \| 294,077.4 \|"
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01` -> **snapshot** (snapshot 20260811222555); points raw/verified 0/0
- `https://acore.org/resources/when-it-comes-to-electricity-capacity-the-market-is-telling-us-the-story/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/pdf/steo_tables.pdf` -> **snapshot** (snapshot 20251123072750); points raw/verified 15/0
- dropped by code checks: 15 (period_end 2026-09-30 after as_of: 14; period_end 2026-12-31 after as_of: 1)

### d5 [related_series] Fuel-specific generation components

Hypothesis: Total = sum of generation by source (natural gas, coal, nuclear, hydro, wind, solar utility-scale, other). Each source has its own trend; summing component forecasts (e.g., gas up, coal, nuclear steady, renewables growing) yields the total.

Queries issued by the searcher: EIA Electric Power Monthly net generation by energy source total all sectors table 1.1; EIA electricity generation by source monthly 2026 natural gas coal nuclear wind solar; EIA Short-Term Energy Outlook August 2026 electricity generation forecast; EIA STEO August 2026 table electricity generation billion kWh by source forecast 2026 coal natural gas nuclear wind solar; "July 2025" net generation thousand megawatthours total all sectors coal natural gas nuclear EIA table 1.1; EIA Electricity Monthly Update data for May 2026 net generation compared May 2025 coal natural gas

- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?lang=en&t=table_1_01` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cleantechnica.com/2026/07/23/renewables-provide-more-than-30-of-us-electricity/` -> **snapshot** (snapshot 20260824042732); points raw/verified 15/15
  - p39 U.S. utility-scale solar net generation, January-May 2026 cumulative = **135,813** GWh (2026-01-01..2026-05-31) [keep: ] quote: "Utility-scale solar totaled 135,813-GWh for the same period."
  - p40 U.S. small-scale solar estimated net generation, January-May 2026 cumulative = **41,973** GWh (2026-01-01..2026-05-31) [keep: ] quote: "EIA estimates to have totaled 41,973-GWh in January-May 2026."
  - p41 U.S. wind net generation, January-May 2026 cumulative = **226,653** GWh (2026-01-01..2026-05-31) [keep: ] quote: "In January-May 2026, wind produced 226,653 gigawatt-hours (GWh) - 12.5% of total U.S. electrical generation"
  - p42 U.S. hydropower net generation, January-May 2026 cumulative = **122,525** GWh (2026-01-01..2026-05-31) [keep: ] quote: "hydropower produced 122,525-GWh (6.7%)"
  - p43 U.S. biomass net generation, January-May 2026 cumulative = **18,243** GWh (2026-01-01..2026-05-31) [keep: ] quote: "biomass produced 18,243-GWh (1.0%)"
  - p44 U.S. geothermal net generation, January-May 2026 cumulative = **6,515** GWh (2026-01-01..2026-05-31) [keep: ] quote: "geothermal produced 6,515-GWh (0.36%)"
  - p45 U.S. nuclear net generation, January-May 2026 cumulative = **320,105** GWh (2026-01-01..2026-05-31) [keep: ] quote: "nuclear power generated 320,105-GWh and coal provided 257,389-GWh"
  - p46 U.S. coal net generation, January-May 2026 cumulative = **257,389** GWh (2026-01-01..2026-05-31) [keep: ] quote: "nuclear power generated 320,105-GWh and coal provided 257,389-GWh"
  - p47 U.S. utility-scale plus small-scale solar net generation, May 2026 = **47,147** GWh (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026 alone, utility-scale and small-scale solar generated 47,147-GWh."
  - p48 U.S. coal net generation, May 2026 = **45,119** GWh (2026-05-01..2026-05-31) [keep: ] quote: "Coal generated 45,119-GWh while wind generated 41,157-GWh."
  - p49 U.S. wind net generation, May 2026 = **41,157** GWh (2026-05-01..2026-05-31) [keep: ] quote: "Coal generated 45,119-GWh while wind generated 41,157-GWh."
  - p50 U.S. nuclear net generation, May 2026 = **65,001** GWh (2026-05-01..2026-05-31) [keep: ] quote: "Nuclear power generated 65,001-GWh."
  - p51 U.S. solar plus wind net generation (incl. small-scale solar), May 2026 = **88,304** GWh (2026-05-01..2026-05-31) [keep: ] quote: "Solar and wind combined generated 88,304-GWh."
  - p52 Renewables share of total U.S. electrical generation, January-May 2026 = **30.3** % (2026-01-01..2026-05-31) [keep: ] quote: "The mix of all renewables, including biomass and geothermal, accounted for 30.3% of total U.S. electrical generation during the first five months of 2026"
  - p53 U.S. natural gas net generation growth rate, January-May 2026 vs January-May 202 = **2.5** % (2026-01-01..2026-05-31) [keep: ] quote: "the electrical output of the nation's nuclear power and natural gas plants experienced much slower growth - just 1.3% and 2.5% respectively."
- `https://beyond-coal.jp/en/documents/eia_short-term-energy-outlook-202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf` -> **snapshot** (snapshot 20260821040641); points raw/verified 15/6
  - p54 U.S. total generation, electric power sector, 3Q25 (July 2025 quarter) (Table 7d = **1,195** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Total generation ......................... 1,035.8 1,021.1 1,194.8 1,023.6 1,053.6 1,040.1 1,225.2 1,034.0 1,061.3 1,070.1 1,274.9 1,067.8 4,275.2 4,352.9 4,474.0"
  - p55 U.S. natural gas generation, electric power sector, 3Q25 (Table 7d) = **536** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Natural gas .............................. 379.9 389.5 535.6 397.0 385.6 395.4 543.2 407.6 398.6 393.2 562.3 421.1 1,702.0 1,731.7 1,775.2"
  - p56 U.S. coal generation, electric power sector, 3Q25 (Table 7d) = **207** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Coal ......................................... 193.5 157.7 207.1 174.3 171.4 140.7 204.9 161.8 159.7 139.5 201.4 160.1 732.7 678.9 660.7"
  - p57 U.S. nuclear generation, electric power sector, 3Q25 (Table 7d) = **207** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Nuclear .................................... 196.0 186.3 206.9 195.6 197.7 189.9 206.2 196.7 198.8 193.7 209.0 195.4 784.8 790.5 796.9"
  - p58 U.S. wind generation, electric power sector, 3Q25 (Table 7d) = **84.7** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Wind .................................... 133.5 118.5 84.7 127.4 136.3 130.6 93.5 132.5 146.5 136.3 96.7 140.5 464.1 492.9 520.0"
  - p59 U.S. utility-scale solar generation, electric power sector, 3Q25 (Table 7d) = **92.6** billion kilowatthours (2025-07-01..2025-09-30) [keep: ] quote: "Solar (a) ............................. 54.9 88.0 92.6 58.0 67.6 105.2 110.7 69.7 79.7 125.8 134.2 84.3 293.5 353.2 424.0"
- dropped by code checks: 9 (period_end 2026-09-30 after as_of: 9)

### d6 [physical_flow] Demand-side load and weather

Hypothesis: Generation ≈ electricity demand (plus losses). July 2026 demand depends on cooling-degree-days and economic activity; hot-weather-driven load can be estimated from population-weighted CDD and historical generation-per-CDD relationships.

Queries issued by the searcher: NOAA cooling degree days July 2026 national temperature; EIA Electric Power Monthly July 2026 net generation; NOAA July 2026 national climate report cooling degree days population-weighted anomaly; EIA Short-Term Energy Outlook August 2026 electricity generation forecast summer

- `https://www.eia.gov/electricity/monthly/update/` -> **snapshot** (snapshot 20260807140411); points raw/verified 3/3
  - p60 U.S. net electricity generation change, May 2026 vs May 2025 = **3.1** % (2026-05-01..2026-05-31) [keep: ] quote: "Net electricity generation in the United States increased 3.1% compared to May 2025."
  - p61 Total U.S. coal stockpiles, May 2026 = **120,000,000** tons (2026-05-01..2026-05-31) [keep: ] quote: "Total U.S. coal stockpiles increased by 2.9% to 120 million tons compared to the previous month."
  - p62 Total U.S. coal stockpiles change, May 2026 vs previous month = **2.9** % (2026-05-01..2026-05-31) [keep: ] quote: "Total U.S. coal stockpiles increased by 2.9% to 120 million tons compared to the previous month."
- `https://www.ncei.noaa.gov/news/national-climate-202607` -> **snapshot** (snapshot 20260820150519); points raw/verified 15/15
  - p63 CONUS average temperature, July 2026 (warmest month on record) = **76.9** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "Warmest on record: July 2026 averaged 76.9°F, the warmest month on record (1895-present) for the contiguous United States (CONUS)."
  - p64 CONUS July 2026 temperature anomaly above 20th-century average = **3.3** degrees Fahrenheit above average (2026-07-01..2026-07-31) [keep: ] quote: "The average temperature for the CONUS in July was 76.9°F, 3.3°F above the 20th-century average."
  - p65 CONUS July 2026 margin warmer than July 1936 and July 2012 (lower bound) = **0.1** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "This was the warmest July-and warmest month-in the 132-year record, 0.1-0.2°F warmer than July 1936 and July 2012."
  - p66 CONUS July 2026 margin warmer than July 1936 and July 2012 (upper bound) = **0.2** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "This was the warmest July-and warmest month-in the 132-year record, 0.1-0.2°F warmer than July 1936 and July 2012."
  - p67 CONUS July 2026 average daytime maximum temperature = **89.5** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "Daytime maximum temperatures averaged 89.5°F, 2.9°F above average, ranking as the sixth-warmest month on record for average high temperatures"
  - p68 CONUS July 2026 average overnight minimum temperature (warmest on record) = **64.2** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "overnight minimum temperatures averaged 64.2°F, 3.7°F above average, ranking as the warmest month on record for average low temperatures"
  - p69 CONUS July 2026 overnight minimum anomaly above average = **3.7** degrees Fahrenheit above average (2026-07-01..2026-07-31) [keep: ] quote: "overnight minimum temperatures averaged 64.2°F, 3.7°F above average, ranking as the warmest month on record for average low temperatures"
  - p70 CONUS July 2026 overnight minimum margin over July 2022 = **0.7** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "surpassing July 2022 by 0.7°F."
  - p71 Minimum state-level July 2026 temperature anomaly above 20th-century average (al = **1** degrees Fahrenheit above average (2026-07-01..2026-07-31) [keep: ] quote: "All CONUS states were at least 1°F above their 20th-century average, with 13 states ranking among their five warmest Julys."
  - p72 Number of CONUS states ranking among their five warmest Julys, July 2026 = **13** states (2026-07-01..2026-07-31) [keep: ] quote: "All CONUS states were at least 1°F above their 20th-century average, with 13 states ranking among their five warmest Julys."
  - p73 Wyoming July 2026 temperature anomaly above average (warmest July on record) = **6.3** degrees Fahrenheit above average (2026-07-01..2026-07-31) [keep: ] quote: "Wyoming recorded its warmest July and warmest month on record, with temperatures 6.3°F above average and 0.9°F warmer than its previous July record set in 2007."
  - p74 Alaska July 2026 average temperature (coldest July since 2008) = **51.8** degrees Fahrenheit (2026-07-01..2026-07-31) [keep: ] quote: "Alaska's average temperature was 51.8°F, 0.9°F below the 1925-2000 average, ranking in the coolest third of the 102-year record."
  - p75 Alaska July 2026 temperature anomaly below 1925–2000 average = **0.9** degrees Fahrenheit below average (2026-07-01..2026-07-31) [keep: ] quote: "Alaska's average temperature was 51.8°F, 0.9°F below the 1925-2000 average, ranking in the coolest third of the 102-year record."
  - p76 Hawai'i July 2026 average temperature anomaly above 1991–2020 average = **0.6** degrees Fahrenheit above average (2026-07-01..2026-07-31) [keep: ] quote: "Hawai'i's average temperature was 69.4°F, 0.6°F above the 1991-2020 average, ranking in the middle third of the 36-year record."
  - p77 CONUS July 2026 total precipitation (driest third of record) = **2.55** inches (2026-07-01..2026-07-31) [keep: ] quote: "Total precipitation averaged across the CONUS in July was 2.55 inches, 0.23 inch below the 20th-century average, ranking in the driest third of the 132-year record."
- `https://climateimpactcompany.com/u-s-gas-power-report-the-2026-u-s-population-weight-cdd-forecast-2/` -> **snapshot** (snapshot 20260417084210); points raw/verified 15/11
  - p78 U.S. population-weighted CDD projection for July 2026 = **355** cooling degree days (2026-07-01..2026-07-31) [DISCARD: March 2026 CDD projection of 355 for July 2026 is contradicted by NOAA's observed record-warmest July 2026 (p63–p70); us] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p79 U.S. 30-year normal CDD for July = **321** cooling degree days (2026-07-01..2026-07-31) [DISCARD: 30-year normal CDD is a climatological benchmark, not a July 2026 observation; superseded by observed record warmth and ] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p80 U.S. 10-year normal CDD for July = **372** cooling degree days (2026-07-01..2026-07-31) [DISCARD: 10-year normal CDD is a benchmark, not a July 2026 observation; the observed record warmth (p63–p70) already indicates J] quote: "The projected CDD for July is 355 compared to the 30-year (321) and 10-year (372) normal."
  - p81 U.S. July CDD, most recent past year (first of past 3 years) = **376** cooling degree days (2025-07-01..2025-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p82 U.S. July CDD, second of past 3 years = **370** cooling degree days (2024-07-01..2024-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p83 U.S. July CDD, third of past 3 years = **371** cooling degree days (2023-07-01..2023-07-31) [keep: ] quote: "The July forecast is not as hot as the past 3 years, which were 376, 370, and 371."
  - p84 U.S. CDD projection for June 2026 = **246** cooling degree days (2026-06-01..2026-06-30) [DISCARD: June 2026 CDD projection is for a different month and was made in March; not applicable to July 2026 target.] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p85 U.S. 10-year normal CDD for June = **253** cooling degree days (2026-06-01..2026-06-30) [DISCARD: June 10-year normal CDD is a benchmark for a different month; not applicable.] quote: "The June CDD projection is 246 which is very close to the warm 10-year normal (253)."
  - p86 U.S. CDD projection for May 2026 = **121** cooling degree days (2026-05-01..2026-05-31) [DISCARD: May 2026 CDD projection is for a different month; not applicable to July 2026.] quote: "The U.S. CDD projection is 121 which is above the 30-year normal (97) and 10-year normal (116) and warmer than last year (102)."
  - p87 U.S. CDD projection for April 2026 = **43** cooling degree days (2026-04-01..2026-04-30) [DISCARD: April 2026 CDD projection is for a different month; not applicable.] quote: "The early season CDD count for the U.S. is 43 which is warmer than the 10-year (40) and 30-year (30) normal."
  - p88 Texas region CDD projection for May 2026 = **290** cooling degree days (2026-05-01..2026-05-31) [DISCARD: Texas-region May 2026 CDD projection is for a different month and sub-region; not applicable.] quote: "Once again, the jackpot for May CDD is the Texas region (290) which matches last May compared to the 30-year (252) and 10-year (284) normal."
- `https://www.aga.org/wp-content/uploads/2026/08/Current-Cooling-Degree-Day-Data_Paul-Pierson-80.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2026-08-31 after as_of: 2; period_end 2026-09-30 after as_of: 1; period_end 2026-10-31 after as_of: 1)

### d7 [shocks] Disruptions, policy, and calendar effects

Hypothesis: July 2026 has 31 days; heat waves, data-center load growth, plant retirements/additions, and fuel prices shift the total versus prior Julys. Quantifying these effects adjusts the historical baseline.

Queries issued by the searcher: EIA Electric Power Monthly July 2026 net generation by energy source; July 2026 heat wave US power demand record electricity load; EIA Short-Term Energy Outlook August 2026 electricity generation forecast 2026 growth percent; EIA Electric Power Monthly June 2026 net generation total utility scale August 2026 release

- `https://www.eia.gov/todayinenergy/detail.php?id=67906` -> **snapshot** (snapshot 20260823205518); points raw/verified 6/6
  - p89 Record hourly peak load in ERCOT on July 22, 2026 = **91.1** gigawatts (2026-07-22..2026-07-22) [DISCARD: Duplicate of p18 (same ERCOT record peak); redundant copy.] quote: "Hourly peak load in the Electric Reliability Council of Texas (ERCOT), the regional transmission organization serving most of Texas, reached a record 91.1 gigawatts (GW) on July 22, 2026"
  - p90 Percentage by which the July 22, 2026 ERCOT peak exceeded the previous peak = **6** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p20/p90 figure; redundant copy.] quote: "The July 22 peak was 6% greater than the previous peak of 85.5 GW, set on August 10, 2023 according to ERCOT."
  - p91 Previous ERCOT peak load record set August 10, 2023 = **85.5** gigawatts (2023-08-10..2023-08-10) [DISCARD: Duplicate of p19 (same ERCOT previous record); redundant copy.] quote: "The July 22 peak was 6% greater than the previous peak of 85.5 GW, set on August 10, 2023 according to ERCOT."
  - p92 Share of July 22, 2026 ERCOT peak met with natural gas generation = **48** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p21 (same ERCOT gas share); redundant copy.] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
  - p93 Share of July 22, 2026 ERCOT peak met with solar generation = **32** % (2026-07-22..2026-07-22) [DISCARD: Duplicate of p22 (same ERCOT solar share); redundant copy.] quote: "The July 22 peak occurred at 6:00 p.m. CT and was primarily met with generation from natural gas (48%) and solar (32%) resources according to data reported to us."
  - p94 Record electricity demand in Southwest Power Pool on July 27, 2026 = **57.9** gigawatts (2026-07-27..2026-07-27) [DISCARD: Duplicate of p23 (same SPP record demand); redundant copy.] quote: "More recently, electricity demand in the Southwest Power Pool reached a record 57.9 GW on July 27 at 5:00 p.m. CT."
- `https://beyond-coal.jp/en/documents/eia_short-term-energy-outlook-202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://governorswindenergycoalition.org/extreme-heat-pushed-electricity-demand-to-near-record-levels/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01` -> **snapshot** (snapshot 20260811222555); points raw/verified 0/0

### b1 [related_series] EIA-930 / hourly grid data

Hypothesis: Summing EIA-930 balancing-authority net generation over July 2026 and scaling by coverage share would give a near-complete utility-scale total, directly anchoring the target and resolving the gap between the historical-baseline and component routes.

Queries issued by the searcher: EIA Hourly Electric Grid Monitor July 2026 net generation balancing authority; EIA-930 coverage of total US utility-scale generation percent; EIA-930 net generation lower than Electric Power Monthly percent coverage share balancing authorities metered generators; "July 2026" EIA-930 monthly net generation Lower 48 terawatthours grid monitor

- `https://www.eia.gov/todayinenergy/detail.php?id=65344` -> **snapshot** (snapshot 20260505001938); points raw/verified 3/3
  - p95 Minimum nameplate capacity threshold for grid-connected power plants included in = **1** megawatts (MW) of nameplate capacity (not stated (page dated 2026-05-01)) [DISCARD: Definitional threshold (1 MW) for EIA-930 inclusion; no numerical role in estimating July 2026 GWh.] quote: "monthly net generation for every grid-connected power plant located in the United States with at least 1 megawatt (MW) of nameplate capacity"
  - p96 Number of power plants physically located in Mexico metered by CAISO and include = **4** as written "four", value check pending power plants (not stated (page dated 2026-05-01)) [DISCARD: Count of Mexico-located plants metered by CAISO; negligible and not a generation quantity.] quote: "Because CAISO also meters four power plants physically located in Mexico"
  - p97 Number of Mexico-located power plants whose generation is excluded from Electric = **4** as written "four", value check pending facilities (not stated (page dated 2026-05-01)) [DISCARD: Redundant with p96; exclusion of 4 Mexican plants is immaterial to the national total.] quote: "the generation from these four facilities in Mexico is excluded"
- `https://www.eia.gov/electricity/gridmonitor/about` -> **snapshot** (snapshot 20260804211839); points raw/verified 0/0
- `https://docs.sugra.ai/doc-2263605` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://basekick.net/demos/energy` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [forecasts_markets] EIA STEO

Hypothesis: The July or August 2026 STEO monthly generation forecast for July 2026 is a direct, model-based estimate of the target and would provide an independent anchor to compare against the historical-baseline route.

Queries issued by the searcher: EIA Short-Term Energy Outlook August 2026 electricity generation forecast; STEO Table 7 electricity July 2026 total generation forecast; EIA STEO August 2026 "total generation" table 7a billion kWh monthly July 2026; "Short-Term Energy Outlook" July 2026 EIA electricity generation forecast released July 2026

- `https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf` -> **snapshot** (snapshot 20260821040641); points raw/verified 15/2
  - p98 U.S. total electricity generation, all sectors, 1H26 year-over-year increase = **37,000,000,000** kilowatthours (2026-01-01..2026-06-30) [keep: ] quote: "During the first half of 2026 (1H26), total generation by the U.S. electric power sector was up 37 billion kilowatthours (BkWh), or 1.8%, compared with the first six months of 2025."
  - p99 U.S. total electricity generation, all sectors, 1H26 year-over-year percentage i = **1.8** % (2026-01-01..2026-06-30) [keep: ] quote: "During the first half of 2026 (1H26), total generation by the U.S. electric power sector was up 37 billion kilowatthours (BkWh), or 1.8%, compared with the first six months of 2025."
- `https://www.eia.gov/outlooks/steo/pdf/steo_tables.pdf` -> **snapshot** (snapshot 20251123072750); points raw/verified 15/0
- `https://zenodo.org/records/21321403` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://beyond-coal.jp/en/documents/eia_short-term-energy-outlook-202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 28 (period_end 2026-09-30 after as_of: 26; period_end 2026-12-31 after as_of: 2)

### b3 [base_rates] weather-to-load transfer

Hypothesis: A historical relationship between population-weighted CDD and monthly utility-scale generation would let the observed record-warm July 2026 (p63–p70) be converted into a generation uplift over July 2025, resolving the largest uncertainty in the historical-baseline route.

Queries issued by the searcher: EIA monthly electricity generation vs cooling degree days regression sensitivity; population-weighted cooling degree days US monthly NOAA EIA electricity demand; EIA Electric Power Monthly Table 1.1 net generation by energy source total all sectors July 2025 thousand megawatthours; EIA Monthly Energy Review cooling degree days population weighted table July 2024 2025; EIA STEO electricity model cooling degree days coefficient retail sales summer demand response percent per CDD

- `https://doi.org/10.2172/5429913` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://math.nist.gov/~JBernal/nbsir83-2672.pdf` -> **snapshot** (snapshot 20250314183957); points raw/verified 15/15
  - p100 Electricity demand model CDD coefficient (B1) estimate, national 1976 population = **29.9** coefficient on CDD in electricity demand model (1982-05-01..1982-05-31) [keep: ] quote: "Cooling Degree Days B1 29.9 2.0"
  - p101 Electricity demand model HDD coefficient (B2) estimate, May 1982 Outlook = **126** coefficient on HDD in electricity demand model (1982-05-01..1982-05-31) [keep: ] quote: "Heating Degree Days B2 126.2 6.2"
  - p102 Standard error of CDD coefficient in electricity demand model = **2** standard error of CDD coefficient (1982-05-01..1982-05-31) [keep: ] quote: "Cooling Degree Days B1 29.9 2.0"
  - p103 Adjusted R-square of electricity demand model, May 1982 Outlook = **0.94** adjusted R-square (1982-05-01..1982-05-31) [keep: ] quote: "Adjusted R-Square 0.94"
  - p104 Electricity demand model estimation sample length, monthly data January 1975 to  = **60** monthly observations (1975-01-01..1979-12-31) [keep: ] quote: "on monthly data from January 1975 to December 1979, representing 60 observations"
  - p105 Base case total electricity generation for 50 states, 1980 Q3 (billions of kWh p = **628,780,000,000** of kilowatt hours per quarter (1980-07-01..1980-09-30) [keep: ] quote: "Base Case Total for 566.90 555.73 628.78 568.92 582.70 571.22"
  - p106 Base case total electricity generation for 50 states, 1980 Q2 (billions of kWh p = **555,730,000,000** of kilowatt hours per quarter (1980-04-01..1980-06-30) [keep: ] quote: "Base Case Total for 566.90 555.73 628.78 568.92 582.70 571.22"
  - p107 Total electricity generation, favorable weather scenario (25th percentile), 1980 = **628,770,000,000** of kilowatt hours per quarter (1980-07-01..1980-09-30) [keep: ] quote: "Favorable 565.61 555.72 628.77 567.76 581.41 571.21"
  - p108 Total electricity generation, adverse weather scenario (75th percentile), 1980 Q = **628,800,000,000** of kilowatt hours per quarter (1980-07-01..1980-09-30) [keep: ] quote: "Adverse 567.81 555.73 628.80 569.93 583.61 571.22"
  - p109 Maximum interquartile range of total electricity generation due to weather varia = **0.5** percent (1980-01-01..1981-06-30) [keep: ] quote: "a maximum interquartile range of less than 0.5 percent"
  - p110 Mean cooling degree days for July (normal degree-day distribution parameter) = **311** cooling degree days (monthly mean) (not stated (page dated 2016-02-26)) [keep: ] quote: "Jul X 311.2600 21.7882"
  - p111 Standard deviation of July cooling degree days (normal degree-day distribution p = **21.79** cooling degree days (standard deviation) (not stated (page dated 2016-02-26)) [keep: ] quote: "Jul X 311.2600 21.7882"
  - p112 Mean cooling degree days for August (normal degree-day distribution parameter) = **282** cooling degree days (monthly mean) (not stated (page dated 2016-02-26)) [keep: ] quote: "Aug X 282.3200 19.7624"
  - p113 Mean cooling degree days for June (normal degree-day distribution parameter) = **207** cooling degree days (monthly mean) (not stated (page dated 2016-02-26)) [keep: ] quote: "Jun X 207.3000 14.5110"
  - p114 CDD coefficient in log(distillate/residual) fuel share equation, February 1980 O = **0.000754** coefficient on CDD in log share equation (1980-02-01..1980-02-29) [DISCARD: CDD coefficient in a fuel-share equation, not a generation relationship; irrelevant to the target.] quote: "CDD 0.000754 -0.0000014 -0.000537"
- `https://www.eia.gov/outlooks/steo/documentation/electric_supply.pdf` -> **snapshot** (snapshot 20250502224704) **LEAK SENTINEL HIT ['(?<![\\d.,])11,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://dukespace.lib.duke.edu/server/api/core/bitstreams/781323f6-23ca-4c3c-bc12-1355d4dd9095/content` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['us electricity generation', 'july power demand', 'eia generation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'] All from the same electrek/EIA-derived July 2025 solar-and-wind article; internally consistent (utility-scale solar 33,119 + small-scale ~9,973 = 43,092 combined; 43,092/0.094 ≈ 458,000 GWh total July
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Same electrek article, Jan–Jul 2025 cumulative shares and growth rates; consistent internally (renewables 26.7% vs 25.1%, wind 10.8%). Same source as p1–p9.
- corroborating: ['p39', 'p40', '41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53'] Cleantechnica article (2026-07-23) reporting EIA Jan–May 2026 and May 2026 figures; internally consistent (solar+wind May 2026 = 47,147 + 41,157 = 88,304 matches p51). Same underlying EIA data, so mut
- corroborating: ['p18', 'p19', 'p20', 'p89', 'p90', 'p91'] EIA Today in Energy (2026-08-03) ERCOT record peak; p18/p89 and p19/p91 are duplicate copies of the same figures. 91.1/85.5 ≈ 1.065 consistent with the stated 6%.
- corroborating: ['p21', 'p22', 'p92', 'p93'] Same EIA article, ERCOT peak-hour fuel mix; duplicates of each other.
- corroborating: ['p23', 'p94'] Same EIA article, SPP record demand; duplicate copies.
- corroborating: ['p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77'] NOAA NCEI July 2026 climate report; internally consistent (76.9°F = 3.3°F above 20th-century average; warmest July by 0.1–0.2°F). Single source, so not independent of itself.
- conflicting: ['p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88'] Climate Impact Company March 2026 projection of 355 CDD for July 2026 conflicts with NOAA's observed record-warm July 2026 (p63–p70), which implies CDD well above the 372 ten-year normal and above the
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] EIA capacity table (May 2026 snapshot); internally consistent subtotals. p24/p25 are the same total (existing vs existing+planned additions columns).
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58', 'p59'] EIA Table 7d electric-power-sector quarterly generation; components sum to totals. Electric power sector only, so narrower than the all-sectors target.
- corroborating: ['p60', 'p61', 'p62'] EIA snapshot (2026-08-07) May 2026 generation growth and coal stockpiles; same source.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'] All from the same Electrek/SUN DAY summary of EIA data for July 2025; internally consistent (utility-scale solar 33,119 + small-scale ~9,973 = 43,092 combined; 43,092/0.094 ≈ 458,000 GWh total). Share
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Same Electrek article, Jan–Jul 2025 shares and growth rates; consistent with each other but a single source and a different period (7-month cumulative) than the July target.
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53'] One CleanTechnica article reporting EIA Jan–May 2026 and May 2026 figures; internally consistent (wind 12.5% of total implies ~1.81 million GWh for Jan–May; renewables 30.3% share). Single source, cum
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58', 'p59'] EIA Table 7d electric-power-sector quarterly/monthly generation for 2025; the July 2025 column values (gas 543.2, coal 204.9, nuclear 206.2, wind 93.5, solar 92.6, total 1,225.2 BkWh) are the most aut
- conflicting: ['p54', 'p3', 'p7'] Table 7d July 2025 electric-power-sector total is 1,225.2 BkWh, while the Electrek combined-solar-share route implies ~458,000 GWh for July 2025 — a ~30% gap. The Electrek 'total US electrical output'
- corroborating: ['p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p77'] NOAA NCEI July 2026 climate report: record-warm CONUS July, warmest overnight minima, all states above average. Consistent internally; indicates elevated cooling demand versus typical Julys.
- corroborating: ['p81', 'p82', 'p83'] Climate Impact Company July CDD for 2023–2025 (376, 370, 371) — a consistent recent baseline of hot Julys; useful as the CDD level against which July 2026's record warmth is compared.
- corroborating: ['p18', 'p23'] EIA Today in Energy: ERCOT record 91.1 GW (July 22, 2026) and SPP record 57.9 GW (July 27, 2026). Both indicate strong July 2026 peak demand, consistent with the record-warm July; regional, not nation
- corroborating: ['p98', 'p99', 'p60'] EIA STEO: 1H26 total generation up 37 BkWh (+1.8%) vs 1H25; EIA May 2026 net generation +3.1% YoY. Both point to modest positive YoY growth in 2026, supporting a ~1.02–1.04 July 2026/July 2025 factor.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] EIA-860M May 2026 capacity table; internally consistent (subtotals sum to total). Capacity is not output; useful only as a structural check on the generation mix and for capacity-factor reasoning.
- corroborating: ['p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114'] 1982-vintage NIST electricity-demand model: CDD coefficient 29.9 (SE 2.0), adjusted R² 0.94, July normal CDD 311 (SD 21.8). Old (1975–79 sample) and a different era/scale, so the coefficient cannot be

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 vs July 2025 total utility-scale generation change factor | 1.03 | 0.99..1.07 | 0.9206..1.151 (widened) | ratio | unused | EIA reports 1H26 electric-power-sector generation +1.8% YoY (p98/p99) and May 2026 +3.1% YoY (p60); July 2026 was the warmest CONUS July on record (p63/p64), which should push cooling load above the 2023-25 hot-July CDD cluster (p81-p83). A ~3% YoY factor with a wide range reflects record heat plus  | July 2026 weather-driven demand is at least as high as July 2025 and the 1H26 growth trend persists into July. | Evidence that July 2026 CDD was below July 2025, or that 2026 generation growth stalled or reversed. |
| a2 | All-sectors utility-scale total as a multiple of the electric-power-sector total | 1.05 | 1.02..1.09 | 0.7456..1.491 (widened) | ratio | unused | EIA Table 7d reports the electric-power-sector total; the all-sectors total adds industrial and commercial CHP, which historically runs roughly 4-6% of the electric-power-sector total. A 1.05 multiple with a 1.02-1.09 range reflects that CHP margin and revision uncertainty. | The all-sectors total exceeds the electric-power-sector total by a modest CHP margin. | An EIA all-sectors July 2025 total materially outside 1.02-1.09 times the electric-power-sector total. |
| a3 | Months per quarter (calendar constant as named input) | 3 | 3..3 | 2.121..4.243 (widened) | months per quarter | unused | A quarter contains three months; used to convert the 3Q25 quarterly total (p54) to a monthly average. This is a fixed calendar constant, not an empirical estimate. | Converting a quarterly total to a monthly average. | Nothing; it is a definitional calendar constant. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a** GWh, 80% interval [n/a, n/a] GWh, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

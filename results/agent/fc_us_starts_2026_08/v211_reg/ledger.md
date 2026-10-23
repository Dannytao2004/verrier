# Evidence ledger: fc_us_starts_2026_08

- Question: Assume today is 2026-08-17. You know nothing published after this date. Estimate the seasonally adjusted annual rate of privately-owned housing starts in the United States in August 2026 (the number of housing units at an annual rate, as in '1,300,000'), as it will be first reported in the U.S. Census Bureau and HUD Monthly New Residential Construction release.
- as_of: 2026-08-17
- Pinned target: Seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026, as first reported in the Census Bureau/HUD Monthly New Residential Construction release (units started during the month, expressed at an annual rate) | unit housing units at annual rate | period 2026-08-01..2026-08-31 | publisher U.S. Census Bureau and U.S. Department of Housing and Urban Development (HUD), Monthly New Residential Construction (New Residential Construction, series under Construction Reports C20)

- Official value (scoring only, never shown to the agent): 1,275,000

## Directions and pages

### d1 [own_history] Census Bureau time series

Hypothesis: Recent monthly private housing starts SAAR (through June/July 2026) plus seasonal and trend patterns anchor a short-horizon forecast; August typically shows a modest seasonal-adjustment-neutral continuation of the recent level with month-to-month noise.

Queries issued by the searcher: Census Bureau new residential construction housing starts June 2026; privately owned housing starts seasonally adjusted annual rate July 2026; FRED HOUST New Privately-Owned Housing Units Started Total Units 2025 2026 table data; "August 2025" housing starts privately owned seasonally adjusted annual rate 1,3 Census September 2025 release

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/6
  - p1 Privately-owned housing starts, total, SAAR, United States, March 2024 (prelimin = **1,321,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p122/p127 (same March 2024 Census figure); adds no information.] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p2 Privately-owned housing starts, total, SAAR, United States, February 2024 (revis = **1,549,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p124/p128 (same February 2024 revised figure).] quote: "below the revised February estimate of 1,549,000"
  - p3 Privately-owned housing starts, total, SAAR, United States, March 2023 = **1,380,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Redundant duplicate of p129 (same March 2023 figure).] quote: "below the March 2023 rate of 1,380,000"
  - p4 Single-family housing starts, SAAR, United States, March 2024 = **1,022,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p123/p130 (same March 2024 SF starts).] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p5 Single-family housing starts, SAAR, United States, February 2024 (revised) = **1,167,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p125/p131 (same February 2024 SF starts).] quote: "below the revised February figure of 1,167,000"
  - p6 Housing starts in buildings with five units or more, SAAR, United States, March  = **290,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p126/p132 (same March 2024 5+ unit starts).] quote: "The March rate for units in buildings with five units or more was 290,000."
- `https://fred.stlouisfed.org/release/tables?rid=27&eid=20911` -> **snapshot** (snapshot 20260521145513); points raw/verified 15/0
- `https://www.sbcacomponents.com/media/multifamily-starts-surge-in-june-as-single-family-drops` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://equibles.com/economicdata/houst` -> **snapshot** (snapshot 20260420212757); points raw/verified 15/11
  - p7 New Privately-Owned Housing Units Started: Total Units, latest observation (2026 = **1,487,000** housing units at annual rate (2026-01-01..2026-01-31) [keep: ] quote: "\| 2026-01-01 \| 1,487.00 \|"
  - p8 New Privately-Owned Housing Units Started: Total Units, 2025-12-01 = **1,387,000** housing units at annual rate (2025-12-01..2025-12-31) [keep: ] quote: "\| 2025-12-01 \| 1,387.00 \|"
  - p9 New Privately-Owned Housing Units Started: Total Units, 2025-11-01 = **1,324,000** housing units at annual rate (2025-11-01..2025-11-30) [keep: ] quote: "\| 2025-11-01 \| 1,324.00 \|"
  - p10 New Privately-Owned Housing Units Started: Total Units, 2025-10-01 = **1,272,000** housing units at annual rate (2025-10-01..2025-10-31) [keep: ] quote: "\| 2025-10-01 \| 1,272.00 \|"
  - p11 New Privately-Owned Housing Units Started: Total Units, 2025-09-01 = **1,328,000** housing units at annual rate (2025-09-01..2025-09-30) [keep: ] quote: "\| 2025-09-01 \| 1,328.00 \|"
  - p12 New Privately-Owned Housing Units Started: Total Units, prior-year August (2025- = **1,291,000** housing units at annual rate (2025-08-01..2025-08-31) [keep: ] quote: "\| 2025-08-01 \| 1,291.00 \|"
  - p13 New Privately-Owned Housing Units Started: Total Units, 2025-07-01 = **1,420,000** housing units at annual rate (2025-07-01..2025-07-31) [keep: ] quote: "\| 2025-07-01 \| 1,420.00 \|"
  - p14 New Privately-Owned Housing Units Started: Total Units, 2025-06-01 = **1,382,000** housing units at annual rate (2025-06-01..2025-06-30) [keep: ] quote: "\| 2025-06-01 \| 1,382.00 \|"
  - p15 New Privately-Owned Housing Units Started: Total Units, 2025-05-01 = **1,282,000** housing units at annual rate (2025-05-01..2025-05-31) [keep: ] quote: "\| 2025-05-01 \| 1,282.00 \|"
  - p16 New Privately-Owned Housing Units Started: Total Units, 2024-08-01 = **1,391,000** housing units at annual rate (2024-08-01..2024-08-31) [keep: ] quote: "\| 2024-08-01 \| 1,391.00 \|"
  - p17 New Privately-Owned Housing Units Started: Total Units, 2024-12-01 = **1,514,000** housing units at annual rate (2024-12-01..2024-12-31) [keep: ] quote: "\| 2024-12-01 \| 1,514.00 \|"
- dropped by code checks: 28 (scale word 'thousand' not supported by quote or table header: 28)

### d2 [related_series] Building permits as leading indicator

Hypothesis: Permits precede starts; the permit-to-start ratio (starts SAAR / permits SAAR) is fairly stable near 1, so August permits level times that ratio constrains August starts. Permits for August 2026 are also unreleased, so use July 2026 permits and recent permit trend.

Queries issued by the searcher: building permits seasonally adjusted annual rate July 2026 Census Bureau; housing units authorized by building permits 2026 monthly Census new residential construction; census.gov construction nrc historical data housing units authorized by building permits seasonally adjusted annual rate table; "housing starts" "building permits" ratio 2025 2026 starts as percent of permits single-family

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/8
  - p18 US privately-owned housing units authorized by building permits, SAAR, March 202 = **1,458,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p116 (same March 2024 permits).] quote: "Privately‐owned housing units authorized by building permits in March were at a seasonally adjusted annual rate of 1,458,000."
  - p19 US privately-owned housing units authorized by building permits, SAAR, February  = **1,523,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p118 (same February 2024 permits).] quote: "This is 4.3 percent below the revised February rate of 1,523,000"
  - p20 US privately-owned housing units authorized by building permits, SAAR, March 202 = **1,437,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Redundant duplicate of p121 (same March 2023 permits).] quote: "but is 1.5 percent above the March 2023 rate of 1,437,000"
  - p21 US single-family housing units authorized by building permits, SAAR, March 2024 = **973,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p117 (same March 2024 SF permits).] quote: "Single‐family authorizations in March were at a rate of 973,000"
  - p22 US privately-owned housing starts, SAAR, March 2024 (preliminary) = **1,321,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p1 (same March 2024 total starts figure).] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p23 US privately-owned housing starts, SAAR, February 2024 (revised) = **1,549,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Duplicate of p2.] quote: "below the revised February estimate of 1,549,000"
  - p24 US privately-owned housing starts, SAAR, March 2023 = **1,380,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Duplicate of p3.] quote: "below the March 2023 rate of 1,380,000"
  - p25 Average revision to preliminary seasonally adjusted estimates of total building  = **1.9** % (not stated (page dated 2024-04-12)) [DISCARD: Average revision magnitude; general context, not needed for a level forecast.] quote: "On average, the preliminary seasonally adjusted estimates of total building permits, housing starts and housing completions are revised 1.9 percent or less."
- `https://www.census.gov/construction/nrc/starts_rates.html` -> **snapshot** (snapshot 20251006233704); points raw/verified 0/0
- `https://www.census.gov/economic-indicators/econ/econ/currentdata/?programCode=RESCONST&startYear=1959&endYear=2026&categories[` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ycharts.com/indicators/us_building_permits` -> **snapshot** (snapshot 20230524130245); points raw/verified 15/14
  - p26 US Building Permits SAAR, latest value (April 2023) = **1,416,000** building permits at annual rate (2023-04-01..2023-04-30) [DISCARD: April 2023 permits level; too old for current forecast.] quote: "\| Last Value \| 1.416M \|"
  - p27 US Building Permits SAAR, prior month (March 2023) = **1,437,000** building permits at annual rate (2023-03-01..2023-03-31) [DISCARD: March 2023 permits; too old.] quote: "\| Value from Last Month \| 1.437M \|"
  - p28 US Building Permits SAAR, one year ago (April 2022) = **1,795,000** building permits at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 permits; too old.] quote: "\| Value from 1 Year Ago \| 1.795M \|"
  - p29 US Building Permits SAAR, month-over-month change (April 2023) = **-1.46** % (2023-04-01..2023-04-30) [DISCARD: April 2023 m/m change; too old.] quote: "\| Change from Last Month \| -1.46% \|"
  - p30 US Building Permits SAAR, year-over-year change (April 2023) = **-21.11** % (2023-04-01..2023-04-30) [DISCARD: April 2023 YoY change; too old.] quote: "\| Change from 1 Year Ago \| -21.11% \|"
  - p31 US Building Permits SAAR, February 2023 = **1,482,000** building permits at annual rate (2023-02-01..2023-02-28) [DISCARD: Feb 2023 permits; too old.] quote: "\| February 28, 2023 \| 1.482M \|"
  - p32 US Building Permits SAAR, January 2023 = **1,354,000** building permits at annual rate (2023-01-01..2023-01-31) [DISCARD: Jan 2023 permits; too old.] quote: "\| January 31, 2023 \| 1.354M \|"
  - p33 US Building Permits SAAR, December 2022 = **1,409,000** building permits at annual rate (2022-12-01..2022-12-31) [DISCARD: Dec 2022 permits; too old.] quote: "\| December 31, 2022 \| 1.409M \|"
  - p34 US Building Permits SAAR, November 2022 = **1,402,000** building permits at annual rate (2022-11-01..2022-11-30) [DISCARD: Nov 2022 permits; too old.] quote: "\| November 30, 2022 \| 1.402M \|"
  - p35 US Building Permits SAAR, October 2022 = **1,555,000** building permits at annual rate (2022-10-01..2022-10-31) [DISCARD: Oct 2022 permits; too old.] quote: "\| October 31, 2022 \| 1.555M \|"
  - p36 US Building Permits SAAR, September 2022 = **1,588,000** building permits at annual rate (2022-09-01..2022-09-30) [DISCARD: Sep 2022 permits; too old.] quote: "\| September 30, 2022 \| 1.588M \|"
  - p37 US Building Permits SAAR, August 2022 = **1,586,000** building permits at annual rate (2022-08-01..2022-08-31) [DISCARD: Aug 2022 permits; too old.] quote: "\| August 31, 2022 \| 1.586M \|"
  - p38 US Building Permits SAAR, July 2022 = **1,658,000** building permits at annual rate (2022-07-01..2022-07-31) [DISCARD: Jul 2022 permits; too old.] quote: "\| July 31, 2022 \| 1.658M \|"
  - p39 US Building Permits SAAR, trough March 2009 = **513,000** building permits (2009-03-01..2009-03-31) [DISCARD: 2009 trough; historical bound only, not a level input.] quote: "reaching a trough on March 2009 of 513,000 building permits"
- dropped by code checks: 8 (scale word 'thousand' not supported by quote or table header: 7; period_end missing or unparseable: 1)

### d3 [forecasts_markets] Professional forecasters and nowcasts

Hypothesis: Published forecasts or nowcasts for August 2026 housing starts (e.g., from banks, Fannie Mae, NAHB, or consensus panels) made before the cutoff give a direct point estimate to compare against model routes.

Queries issued by the searcher: housing starts forecast August 2026; Fannie Mae housing starts forecast 2026; yieldpro Fannie Mae housing forecast July 2026 starts single-family Q3 2026; NAHB Wells Fargo housing market index August 2026 single-family starts

- `https://yieldpro.com/2026/06/more-multifamily-starts-predicted-in-june-forecast/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://theclose.com/news-2026-us-housing-market-outlook-balanced-not-equal/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=667073&year=2026&cty=US&ctyall=10738893&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thestreet.com/real-estate/fannie-mae-july-2026-housing-forecast-mortgage-rates` -> **snapshot** (snapshot 20260725112117); points raw/verified 15/6
  - p40 Fannie Mae Q2 2026 Home Price Index: year-over-year average home price increase  = **3.2** % (2026-04-01..2026-06-30) [DISCARD: Home price index growth; not a starts input.] quote: "Average home prices increased 3.2% year over year (non-seasonally adjusted), according to the HPI."
  - p41 Fannie Mae Q1 2026 Home Price Index: year-over-year average home price growth = **2.6** % (2026-01-01..2026-03-31) [DISCARD: Home price index growth; not a starts input.] quote: "This is higher than Q1 2026 growth, which was 2.6%."
  - p42 Freddie Mac average 30-year fixed mortgage rate, week of July 16 = **6.55** % (2026-07-16..2026-07-16) [DISCARD: Redundant duplicate of p63 (same Freddie Mac July 16 rate).] quote: "The average 30-year fixed mortgage rate hit 6.55% the week of July 16, according to Freddie Mac."
  - p43 Freddie Mac 30-year fixed mortgage rate, week of June 30 = **6.49** % (2026-06-30..2026-06-30) [DISCARD: Redundant with p64/p66 (same ~6.49% late-June/early-July rate); adds no new information.] quote: "the Freddie Mac rate was 6.49% the week of June 30 and the week of July 14, when Fannie Mae released its July forecast."
  - p44 U.S. week-over-week pending home sales change, four-week period ending July 12 = **2.2** % (2026-06-15..2026-07-12) [DISCARD: Pending home sales change; demand-side context only, not a starts level input.] quote: "During the four-week period ending July 12, week-over-week pending home sales in the U.S. dropped by 2.2%, according to a Redfin report."
  - p45 NAR month-over-month existing-home sales decrease = **2.4** % (not stated (page dated 2026-07-18)) [DISCARD: Existing-home sales change; not a starts input.] quote: "The National Association of Realtors announced that month-over-month existing-home sales decreased by 2.4%."
- dropped by code checks: 9 (period_end 2026-12-31 after as_of: 4; period_end 2027-12-31 after as_of: 5)

### d4 [related_series] Completions and under-construction stock

Hypothesis: Units under construction and completions reflect the pipeline; a high under-construction stock with slowing completions implies starts continue at a moderate pace. Provides a consistency check on the level.

Queries issued by the searcher: housing units under construction 2026 Census Bureau new residential construction completions; "new residential construction" June 2026 housing starts completions under construction annual rate; FRED units under construction housing UNDCONS 2026 monthly value thousands; "under construction" "June 2026" housing units Census table 1.26 million private housing

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/0
- `https://eyeonhousing.org/2026/07/multifamily-gains-lift-overall-starts-despite-single-family-decline/` -> **snapshot** (snapshot 20260802065645); points raw/verified 15/15
  - p46 Total housing units under construction, United States, June = **1,260,000** housing units (2026-06-01..2026-06-30) [keep: ] quote: "The total number of housing units under construction stood at 1.26 million in June, down 6.2% from a year earlier."
  - p47 Single-family homes under construction, United States, June = **582,000** housing units (2026-06-01..2026-06-30) [keep: ] quote: "Single-family homes under construction stood at 582,000 units, a 6.9% year-over-year decline."
  - p48 Multifamily units under construction, United States, June = **682,000** housing units (2026-06-01..2026-06-30) [keep: ] quote: "Multifamily units under construction slowed down to 682,000, down from peaks above 1 million units in December 2023 and 5.7% lower than a year ago."
  - p49 Multifamily units under construction peak, United States, December 2023 = **1,000,000** housing units (2023-12-01..2023-12-31) [DISCARD: December 2023 multifamily peak; historical context only, not needed for August 2026 level.] quote: "Multifamily units under construction slowed down to 682,000, down from peaks above 1 million units in December 2023 and 5.7% lower than a year ago."
  - p50 Single-family completions, United States, annual rate, June = **964,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Completions of single-family homes have improved to an annual rate of about 964,000 units."
  - p51 Multifamily completions (buildings with five or more units), United States, annu = **413,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "multifamily completions for buildings with five or more units were down 5.1% year over year to a 413,000-unit pace."
  - p52 Total housing starts, United States, seasonally adjusted annual rate, June = **1,430,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Overall housing starts increased 19.0% in June to a seasonally adjusted annual rate of 1.43 million units"
  - p53 Single-family starts, United States, seasonally adjusted annual rate, June = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "single-family starts decreased 0.2% to an 895,000 seasonally adjusted annual rate"
  - p54 Single-family starts, three-month moving average, United States, June = **902,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Three-month moving average of SF starts; derived from same data as p53, redundant for a level forecast.] quote: "the three-month moving average provides a clearer signal, falling to 902,000 units."
  - p55 Multifamily starts, United States, annualized rate, June = **532,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Multifamily starts, which include apartment buildings and condominiums, rose 76.2% from May to June to an annualized 532,000 pace."
  - p56 Multifamily starts, three-month moving average, United States, June = **445,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Three-month moving average of MF starts; derived, redundant with p55.] quote: "The three-month moving average for multifamily construction has trended higher to 445,000 units"
  - p57 Total permits, United States, annualized rate, June = **1,370,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Overall permits declined 3.0% to a 1.37-million-unit annualized rate in June."
  - p58 Single-family permits, United States, annualized rate, June = **871,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Single-family permits decreased 2.4% to an 871,000-unit rate and are essentially flat compared to June 2025."
  - p59 Multifamily permits, United States, annualized rate, June = **496,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Multifamily permits are down 4.2% to an annualized 496,000 pace and are down 5.7% compared to June 2025."
  - p60 Total completions, United States, year-to-date change, June = **9.5** % (2026-01-01..2026-06-30) [DISCARD: Completions YTD change; not a direct starts level input.] quote: "On a year-to-date basis, total completions across both sectors are down 9.5% reflecting ongoing challenges in the residential construction sector."
- `https://marketxls.com/indicators/housing-under-construction` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.realtor.com/research/new-home-construction-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 11; value_as_written not in quote as a whole number: 4)

### d5 [shocks] Mortgage rates, affordability, and policy

Hypothesis: Mortgage rates, homebuilder sentiment, and any policy/credit shocks before the cutoff shift the level of starts; a rate decline raises starts with a lag. Quantify direction and rough magnitude.

Queries issued by the searcher: 30-year mortgage rate July 2026 Freddie Mac Primary Mortgage Market Survey; NAHB housing market index July 2026 builder sentiment; Freddie Mac mortgage rates August 13 2026 30-year fixed average; housing starts July 2026 Census Bureau new residential construction single-family rate

- `https://www.freddiemac.com/pmms/archive` -> **snapshot** (snapshot 20260731224527); points raw/verified 15/15
  - p61 30-year fixed-rate mortgage average rate, week of July 30, 2026 = **6.66** % (2026-07-30..2026-07-30) [keep: ] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
  - p62 30-year fixed-rate mortgage average rate, week of July 23, 2026 = **6.58** % (2026-07-23..2026-07-23) [keep: ] quote: "July 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.58% \| 5.96% \|"
  - p63 30-year fixed-rate mortgage average rate, week of July 16, 2026 = **6.55** % (2026-07-16..2026-07-16) [keep: ] quote: "July 16, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.55% \| 5.93% \|"
  - p64 30-year fixed-rate mortgage average rate, week of July 09, 2026 = **6.49** % (2026-07-09..2026-07-09) [keep: ] quote: "July 09, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.82% \|"
  - p65 30-year fixed-rate mortgage average rate, week of July 02, 2026 = **6.43** % (2026-07-02..2026-07-02) [keep: ] quote: "July 02, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.43% \| 5.79% \|"
  - p66 30-year fixed-rate mortgage average rate, week of June 25, 2026 = **6.49** % (2026-06-25..2026-06-25) [keep: ] quote: "June 25, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.84% \|"
  - p67 30-year fixed-rate mortgage average rate, week of June 18, 2026 = **6.47** % (2026-06-18..2026-06-18) [keep: ] quote: "June 18, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.47% \| 5.81% \|"
  - p68 30-year fixed-rate mortgage average rate, week of June 11, 2026 = **6.52** % (2026-06-11..2026-06-11) [keep: ] quote: "June 11, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.52% \| 5.84% \|"
  - p69 30-year fixed-rate mortgage average rate, week of June 04, 2026 = **6.48** % (2026-06-04..2026-06-04) [keep: ] quote: "June 04, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.48% \| 5.79% \|"
  - p70 30-year fixed-rate mortgage average rate, week of May 28, 2026 = **6.53** % (2026-05-28..2026-05-28) [keep: ] quote: "May 28, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.53% \| 5.87% \|"
  - p71 30-year fixed-rate mortgage average rate, week of May 14, 2026 = **6.36** % (2026-05-14..2026-05-14) [keep: ] quote: "May 14, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.36% \| 5.71% \|"
  - p72 30-year fixed-rate mortgage average rate, week of April 30, 2026 = **6.3** % (2026-04-30..2026-04-30) [keep: ] quote: "April 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.30% \| 5.64% \|"
  - p73 30-year fixed-rate mortgage average rate, week of April 23, 2026 = **6.23** % (2026-04-23..2026-04-23) [keep: ] quote: "April 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.23% \| 5.58% \|"
  - p74 30-year fixed-rate mortgage average rate, week of March 05, 2026 = **6** % (2026-03-05..2026-03-05) [keep: ] quote: "March 05, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.00% \| 5.43% \|"
  - p75 30-year fixed-rate mortgage average rate, week of February 26, 2026 (2026 low in = **5.98** % (2026-02-26..2026-02-26) [keep: ] quote: "February 26, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 5.98% \| 5.44% \|"
- `https://tradingeconomics.com/united-states/nahb-housing-market-index/news/575884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.housingwire.com/articles/builder-confidence-dips-again-in-july/` -> **snapshot** (snapshot 20260803112655); points raw/verified 15/15
  - p76 NAHB/Wells Fargo Housing Market Index (HMI) reading, July = **34** index points (2026-07-01..2026-07-31) [keep: ] quote: "homebuilder confidence in July fell 2 points to a reading of 34, marking the 15th consecutive month with a reading below 40"
  - p77 NAHB HMI month-over-month change in July = **2** index points (2026-07-01..2026-07-31) [DISCARD: HMI month-over-month change; redundant with p76 level.] quote: "homebuilder confidence in July fell 2 points to a reading of 34"
  - p78 NAHB HMI consecutive months with reading below 40, through July = **15** months (2026-07-01..2026-07-31) [DISCARD: Count of months below 40; qualitative context, redundant with p76.] quote: "marking the 15th consecutive month with a reading below 40"
  - p79 NAHB HMI present sales component, July = **37** index points (2026-07-01..2026-07-31) [DISCARD: HMI component; redundant with headline HMI p76 for directional signal.] quote: "The HMI additionally reported a negative reading on present sales (37), traffic of prospective buyers (23) and the outlook for the next six months (43)."
  - p80 NAHB HMI traffic of prospective buyers component, July = **23** index points (2026-07-01..2026-07-31) [DISCARD: HMI component; redundant with headline HMI p76.] quote: "traffic of prospective buyers (23)"
  - p81 NAHB HMI six-month outlook component, July = **43** index points (2026-07-01..2026-07-31) [DISCARD: HMI component; redundant with headline HMI p76.] quote: "the outlook for the next six months (43)"
  - p82 Share of builders reporting price cuts, July = **37** % (2026-07-01..2026-07-31) [DISCARD: Price-cut share; qualitative context, not needed numerically.] quote: "In July, 37% of builders reported price cuts, an increase from 35% in June."
  - p83 Share of builders reporting price cuts, June = **35** % (2026-06-01..2026-06-30) [DISCARD: June price-cut share; redundant with July p82 for current sentiment.] quote: "In July, 37% of builders reported price cuts, an increase from 35% in June."
  - p84 Average price reduction among builders, July = **6** % (2026-07-01..2026-07-31) [DISCARD: Average price reduction; qualitative context, not needed numerically.] quote: "The average price reduction held steady at 6%"
  - p85 Share of builders using sales incentives, July = **63** % (2026-07-01..2026-07-31) [DISCARD: Incentive share; qualitative context, not needed numerically.] quote: "the share of builders that reported using sales incentives ticked up slightly to 63%"
  - p86 Share of builders reporting higher year-over-year sales, June (BTIG/HomeSphere s = **35** % (2026-06-01..2026-06-30) [DISCARD: Builder sales survey share; weak contextual, not a level input.] quote: "only 35% of builders reported higher year-over-year sales, while 27% reported lower year-over-year sales"
  - p87 Share of builders reporting higher year-over-year traffic, June (BTIG/HomeSphere = **38** % (2026-06-01..2026-06-30) [DISCARD: Builder traffic survey share; contextual only.] quote: "In June, 38% of builders reported higher year-over-year traffic, nearly doubling the 20% who reported higher traffic in May and nearing February's recent high of 43%."
  - p88 Share of builders reporting higher year-over-year traffic, May (BTIG/HomeSphere  = **20** % (2026-05-01..2026-05-31) [DISCARD: Builder traffic survey share; contextual only.] quote: "nearly doubling the 20% who reported higher traffic in May"
  - p89 New home sales, seasonally adjusted annual rate, April = **622,000** housing units at annual rate (2026-04-01..2026-04-30) [keep: ] quote: "In April, new home sales fell to a seasonally adjusted annual rate of 622,000, representing a 6.2% decline from March and an 11.3% annual decline."
  - p90 New home sales, seasonally adjusted annual rate, May = **580,000** housing units at annual rate (2026-05-01..2026-05-31) [keep: ] quote: "In May, new home sales fell to a seasonally adjusted annual rate of 580,000, down 7.3% from April and down 6.8% year over year."
- `https://www.mpamag.com/us/mortgage-industry/market-updates/housing-starts-tumble-as-rate-pressure-squeezes-builders/586522` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [related_series] Regional permits and starts

Hypothesis: Starts are the sum of four Census regions; regional permit trends (South, West, Midwest, Northeast) can be aggregated to a national level and reveal whether national momentum is broad or concentrated.

Queries issued by the searcher: housing starts by region 2026 Census building permits south west midwest northeast; Monthly New Residential Construction July 2026 building permits housing starts annual rate; "MONTHLY NEW RESIDENTIAL CONSTRUCTION, JUNE 2026" census press release housing starts region; census.gov construction nrc pdf newresconst June 2026 table 3a seasonally adjusted annual rate Northeast Midwest South West

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/10
  - p91 US total privately-owned housing starts SAAR, March 2024 (preliminary) = **1,321,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p1.] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p92 US total privately-owned housing starts SAAR, February 2024 (revised) = **1,549,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Duplicate of p2.] quote: "below the revised February estimate of 1,549,000"
  - p93 US total privately-owned housing starts SAAR, March 2023 = **1,380,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Duplicate of p3.] quote: "below the March 2023 rate of 1,380,000"
  - p94 US single-family housing starts SAAR, March 2024 = **1,022,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p4.] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p95 US housing starts in buildings with five units or more SAAR, March 2024 = **290,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p6.] quote: "The March rate for units in buildings with five units or more was 290,000."
  - p96 US total privately-owned housing units authorized by building permits SAAR, Marc = **1,458,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p18.] quote: "Privately‐owned housing units authorized by building permits in March were at a seasonally adjusted annual rate of 1,458,000."
  - p97 US total privately-owned housing units authorized by building permits SAAR, Febr = **1,523,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Duplicate of p19.] quote: "This is 4.3 percent below the revised February rate of 1,523,000"
  - p98 US total privately-owned housing units authorized by building permits SAAR, Marc = **1,437,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Duplicate of p20.] quote: "but is 1.5 percent above the March 2023 rate of 1,437,000"
  - p99 US single-family building permit authorizations SAAR, March 2024 = **973,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Duplicate of p21.] quote: "Single‐family authorizations in March were at a rate of 973,000"
  - p100 US building permit authorizations for units in buildings with five units or more = **433,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: March 2024 5+ unit permits; not needed and no matching current-period use.] quote: "Authorizations of units in buildings with five units or more were at a rate of 433,000 in March."
- `https://www.realtor.com/research/new-home-construction-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://economics.td.com/us-housing-starts-and-permits?linkId=165656202` -> **snapshot** (snapshot 20220518135305); points raw/verified 15/15
  - p101 U.S. housing starts, total, annualized rate, April 2022 = **1,724,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 starts level; too old and superseded by recent series.] quote: "U.S. housing starts fell by 0.2% month-on-month (m/m) to 1.724 million units (annualized) in April"
  - p102 U.S. housing starts, month-on-month percent change, April 2022 = **0.2** % (2022-04-01..2022-04-30) [DISCARD: April 2022 m/m change; irrelevant to August 2026 level.] quote: "U.S. housing starts fell by 0.2% month-on-month (m/m) to 1.724 million units (annualized) in April"
  - p103 Market expectation for U.S. housing starts, annualized rate, April 2022 = **1,766,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 market expectation; stale, not applicable.] quote: "coming in even lower than market expectations which called for a decline to 1.766 million units"
  - p104 Revision to March 2022 U.S. housing starts, units = **65,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: March 2022 revision; not usable for level forecast.] quote: "Revisions to last month's data lopped 65k units off of March starts"
  - p105 Revision to March 2022 single-family starts, units = **-13,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: March 2022 SF revision; not usable.] quote: "with downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p106 Revision to March 2022 multifamily starts, units = **-52,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: March 2022 MF revision; not usable.] quote: "with downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p107 U.S. multifamily housing starts, month-on-month percent change, April 2022 = **15.3** % (2022-04-01..2022-04-30) [DISCARD: April 2022 MF m/m change; stale.] quote: "multifamily starts rose by 15.3% m/m (or 83k)"
  - p108 U.S. multifamily housing starts, month-on-month change, units, April 2022 = **83,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 MF change; stale.] quote: "multifamily starts rose by 15.3% m/m (or 83k)"
  - p109 U.S. single-family housing starts, month-on-month percent change, April 2022 = **7.3** % (2022-04-01..2022-04-30) [DISCARD: April 2022 SF m/m change; stale.] quote: "Single-family starts, however, fell by 7.3% m/m (or -87k)"
  - p110 U.S. single-family housing starts, month-on-month change, units, April 2022 = **-87,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 SF change; stale.] quote: "Single-family starts, however, fell by 7.3% m/m (or -87k)"
  - p111 U.S. building permits, total, annualized rate, April 2022 = **1,819,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 permits level; stale.] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p112 U.S. building permits, month-on-month percent change, April 2022 = **3.2** % (2022-04-01..2022-04-30) [DISCARD: April 2022 permits change; stale.] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p113 U.S. building permits, month-on-month change, units, April 2022 = **60,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: April 2022 permits change; stale.] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p114 U.S. multifamily building permits, month-on-month percent change, April 2022 = **1** % (2022-04-01..2022-04-30) [DISCARD: April 2022 MF permits change; stale.] quote: "Multifamily permits fell by 1% (or 7k)"
  - p115 U.S. single-family building permits, month-on-month percent change, April 2022 = **4.6** % (2022-04-01..2022-04-30) [DISCARD: April 2022 SF permits change; stale.] quote: "single-family permits fell even further by 4.6% (or -53k)"
- `https://ace.rismedia.com/2026/07/17/housing-construction-starts-rebound-june-2026-multifamily/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (scale word 'thousand' not supported by quote or table header: 5)

### d7 [base_rates] Seasonal factor and month-to-month volatility

Hypothesis: August SAAR relates to the unadjusted August count via the Census seasonal factor; historical August seasonal factors and typical month-to-month SAAR volatility bound the forecast error.

Queries issued by the searcher: Census housing starts seasonal factors table monthly; Monthly New Residential Construction seasonal adjustment housing starts August seasonal factor; census.gov new residential construction "seasonal factors" housing starts table 2026 xls; "housing starts" August 2026 seasonally adjusted annual rate forecast; "New Residential Construction" release pdf "Seasonal Factors" "Housing Units Started" August 2025 census; housing starts August 2025 1,307,000 seasonally adjusted annual rate census release September 2025 unadjusted August

- `https://webharvest.gov/peth04/20041108163020/http://www.census.gov/prod/99pubs/c22-9901.pdf` -> **snapshot** (snapshot 20240424094823) **LEAK SENTINEL HIT ['(?<![\\d.,])110,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://books.google.com.sg/books/download/Construction_Reports.pdf?id=N1rlsXnlVewC&hl=zh-CN&output=pdf&sig=ACfU3U0nsYpZj_FZGJqhdAi_2TERj1Tx3w` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://permanent.access.gpo.gov/lps1499/2001/c25-0103.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://permanent.access.gpo.gov/lps1499/1996/c25_9609.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] permit pipeline

Hypothesis: July 2026 total and single-family permits (SAAR) would anchor a permit-to-start ratio route; June permits (p57) are the latest kept, but July permits would tighten the August starts forecast and resolve whether the June starts>permits gap persists.

Queries issued by the searcher: July 2026 building permits housing starts Census Bureau new residential construction; Census HUD building permits July 2026 seasonally adjusted annual rate; "June 2026" housing starts 1,427,000 permits 1,367,000 single-family 871,000 Census; housing starts forecast August 2026 July data preview permits expected consensus

- `https://www.redbooklumberdata.com/2026/07/17/u-s-census-bureau-monthly-new-residential-consctruction-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/11
  - p116 US total privately-owned housing units authorized by building permits, SAAR, Mar = **1,458,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p18/p96; March 2024 permits not needed for August 2026 forecast.] quote: "Privately‐owned housing units authorized by building permits in March were at a seasonally adjusted annual rate of 1,458,000."
  - p117 US single-family housing units authorized by building permits, SAAR, March 2024  = **973,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p21/p99; March 2024 SF permits not needed.] quote: "Single‐family authorizations in March were at a rate of 973,000; this is 5.7 percent below the revised February figure of 1,032,000."
  - p118 US total privately-owned housing units authorized by building permits, SAAR, Feb = **1,523,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p19/p97; February 2024 permits not needed.] quote: "This is 4.3 percent below the revised February rate of 1,523,000, but is 1.5 percent above the March 2023 rate of 1,437,000."
  - p119 US single-family housing units authorized by building permits, SAAR, February 20 = **1,032,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p21/p99; February 2024 SF permits not needed.] quote: "Single‐family authorizations in March were at a rate of 973,000; this is 5.7 percent below the revised February figure of 1,032,000."
  - p120 US housing units in buildings with five units or more authorized by building per = **433,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: March 2024 5+ unit permits; old and not needed for August 2026 forecast.] quote: "Authorizations of units in buildings with five units or more were at a rate of 433,000 in March."
  - p121 US total privately-owned housing units authorized by building permits, SAAR, Mar = **1,437,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Redundant duplicate of p20/p98; March 2023 permits not needed.] quote: "but is 1.5 percent above the March 2023 rate of 1,437,000"
  - p122 US total privately-owned housing starts, SAAR, March 2024 (preliminary) = **1,321,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p1/p127; March 2024 starts not needed.] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p123 US single-family housing starts, SAAR, March 2024 (preliminary) = **1,022,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p4/p130; March 2024 SF starts not needed.] quote: "Single‐family housing starts in March were at a rate of 1,022,000; this is 12.4 percent (±12.5 percent)* below the revised February figure of 1,167,000."
  - p124 US total privately-owned housing starts, SAAR, February 2024 (revised) = **1,549,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p2/p128; February 2024 starts not needed.] quote: "This is 14.7 percent (±9.9 percent) below the revised February estimate of 1,549,000"
  - p125 US single-family housing starts, SAAR, February 2024 (revised) = **1,167,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p5/p131; February 2024 SF starts not needed.] quote: "below the revised February figure of 1,167,000"
  - p126 US housing units in buildings with five units or more started, SAAR, March 2024 = **290,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p6/p132; March 2024 5+ unit starts not needed.] quote: "The March rate for units in buildings with five units or more was 290,000."
- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.housingaffordabilityinstitute.org/june-2026-census-bps/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (scale word 'thousand' not supported by quote or table header: 4)

### b2 [own_history] recent starts

Hypothesis: July 2026 starts SAAR (released ~mid-August 2026) would give the most recent level and momentum, materially improving the short-horizon forecast versus June-only data.

Queries issued by the searcher: Census HUD July 2026 privately-owned housing starts seasonally adjusted annual rate; new residential construction July 2026 housing starts single-family multifamily SAAR; "June 2026" housing starts 1,427,000 single-family multifamily SAAR Census July 17 2026 release; housing starts forecast August 2026 SAAR outlook published early August 2026

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/6
  - p127 US privately-owned housing starts, total, SAAR, March 2024 (preliminary) = **1,321,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p1/p122; March 2024 starts not needed.] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p128 US privately-owned housing starts, total, SAAR, February 2024 (revised) = **1,549,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p2/p124; February 2024 starts not needed.] quote: "below the revised February estimate of 1,549,000"
  - p129 US privately-owned housing starts, total, SAAR, March 2023 = **1,380,000** housing units at annual rate (2023-03-01..2023-03-31) [DISCARD: Redundant duplicate of p3; March 2023 starts not needed.] quote: "below the March 2023 rate of 1,380,000"
  - p130 US single-family housing starts, SAAR, March 2024 = **1,022,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p4/p123; March 2024 SF starts not needed.] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p131 US single-family housing starts, SAAR, February 2024 (revised) = **1,167,000** housing units at annual rate (2024-02-01..2024-02-29) [DISCARD: Redundant duplicate of p5/p125; February 2024 SF starts not needed.] quote: "below the revised February figure of 1,167,000"
  - p132 US housing starts in buildings with five units or more, SAAR, March 2024 = **290,000** housing units at annual rate (2024-03-01..2024-03-31) [DISCARD: Redundant duplicate of p6/p126; March 2024 5+ unit starts not needed.] quote: "The March rate for units in buildings with five units or more was 290,000."
- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/housing-starts/news/567898` -> **snapshot** (snapshot 20260804063649); points raw/verified 14/14
  - p133 US housing starts SAAR, total, June 2026 = **1,427,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Housing starts in the US jumped 19% to a seasonally adjusted annualized rate of 1427 thousand units in June 2026, the highest in three months, compared to forecasts of 1310 thousand."
  - p134 US housing starts SAAR, total, June 2026, percent change from prior month = **19** % (2026-06-01..2026-06-30) [DISCARD: June percent change; redundant with p133 level.] quote: "Housing starts in the US jumped 19% to a seasonally adjusted annualized rate of 1427 thousand units in June 2026"
  - p135 US housing starts SAAR, total, June 2026, forecast = **1,310,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: June 2026 forecast (1,310k) is a forecast, not an outcome; not usable as data.] quote: "compared to forecasts of 1310 thousand."
  - p136 US housing starts SAAR, total, May 2026, revised percent change = **15.4** % (2026-05-01..2026-05-31) [DISCARD: May revised percent change; redundant with level context.] quote: "It follows a revised 15.4% jump in May that sent housing starts to a six-year low."
  - p137 US multifamily housing starts SAAR, June 2026 = **513,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p138 US multifamily housing starts, June 2026, percent change from prior month = **76.3** % (2026-06-01..2026-06-30) [DISCARD: MF percent change; redundant with p137 level.] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p139 US multifamily housing starts, May 2026, percent change from prior month = **41** % (2026-05-01..2026-05-31) [DISCARD: May MF percent change; redundant with p137.] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p140 US single-family housing starts SAAR, June 2026 = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Meanwhile, single-family starts edged down 0.2% to 895 thousand, a third consecutive month of falls, as high prices and mortgage rates are weighing on demand."
  - p141 US single-family housing starts, June 2026, percent change from prior month = **0.2** % (2026-06-01..2026-06-30) [DISCARD: SF percent change; redundant with p140 level.] quote: "Meanwhile, single-family starts edged down 0.2% to 895 thousand, a third consecutive month of falls, as high prices and mortgage rates are weighing on demand."
  - p142 US housing starts SAAR, South region, June 2026 = **741,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Starts soared in all four main regions: the South (15.2% to 741 thousand), the Midwest (33.3% to 248 thousand, the highest since 2024), the Northeast (10.3% to 129 thousand) and the West (22.1% to 309"
  - p143 US housing starts, South region, June 2026, percent change from prior month = **15.2** % (2026-06-01..2026-06-30) [DISCARD: South percent change; redundant with p142 level.] quote: "Starts soared in all four main regions: the South (15.2% to 741 thousand), the Midwest (33.3% to 248 thousand, the highest since 2024), the Northeast (10.3% to 129 thousand) and the West (22.1% to 309"
  - p144 US housing starts SAAR, Midwest region, June 2026 = **248,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "ed in all four main regions: the South (15.2% to 741 thousand), the Midwest (33.3% to 248 thousand, the highest since 2024), the Northeast (10.3% to 129 thousand) and the West (22.1% to 309 thousand)."
  - p145 US housing starts SAAR, Northeast region, June 2026 = **129,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "ed in all four main regions: the South (15.2% to 741 thousand), the Midwest (33.3% to 248 thousand, the highest since 2024), the Northeast (10.3% to 129 thousand) and the West (22.1% to 309 thousand)."
  - p146 US housing starts SAAR, West region, June 2026 = **309,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "ed in all four main regions: the South (15.2% to 741 thousand), the Midwest (33.3% to 248 thousand, the highest since 2024), the Northeast (10.3% to 129 thousand) and the West (22.1% to 309 thousand)."
- `https://novascotia.ca/finance/statistics//archive_news.asp?id=22187&dg=&df=&dto=0&dti=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (scale word 'thousand' not supported by quote or table header: 9)

### b3 [forecasts_markets] consensus nowcast

Hypothesis: A published August 2026 starts nowcast/consensus (Fannie Mae, NAHB, bank research) made before the cutoff would provide a direct point estimate to compare against model routes.

Queries issued by the searcher: Fannie Mae housing starts forecast August 2026; NAHB housing starts forecast 2026 housing market; "Housing Forecast: August 2026" Fannie Mae quarterly housing starts single-family multifamily 2026 Q3; Fannie Mae August 2026 Economic and Housing Outlook housing starts 1.3 million forecast

- `https://www.fanniemae.com/media/document/pdf/housing-forecast-082026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/housing-starts/news/584595` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yieldpro.com/2026/07/future-multifamily-starts-seen-rising-in-july-forecast/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://theclose.com/news-2026-us-housing-market-outlook-balanced-not-equal/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['housing starts', 'us housing', 'new construction']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p22', 'p91'] Identical March 2024 total starts SAAR (1,321,000) repeated across d1/d2/d6; same Census release, not independent.
- corroborating: ['p2', 'p23', 'p92'] Identical revised February 2024 total starts (1,549,000); same underlying Census figure.
- corroborating: ['p3', 'p24', 'p93'] Identical March 2023 total starts (1,380,000); same source.
- corroborating: ['p4', 'p94'] Identical March 2024 single-family starts (1,022,000).
- corroborating: ['p6', 'p95'] Identical March 2024 5+ unit starts (290,000).
- corroborating: ['p18', 'p96'] Identical March 2024 total permits (1,458,000).
- corroborating: ['p19', 'p97'] Identical revised February 2024 permits (1,523,000).
- corroborating: ['p20', 'p98'] Identical March 2023 permits (1,437,000).
- corroborating: ['p21', 'p99'] Identical March 2024 single-family permits (973,000).
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17'] Consistent monthly SAAR starts series from equibles mirroring Census; shows 2025 level ~1.27-1.42M with August 2025 at 1,291,000. Single source, so internal consistency is not independent confirmation
- corroborating: ['p52', 'p53', 'p55'] June 2026 total starts 1.43M = single-family 895k + multifamily 532k (approx); internally consistent decomposition from eyeonhousing.
- conflicting: ['p52', 'p57'] June 2026 starts (1.43M) exceed June permits (1.37M); starts running above permits is unusual and suggests a multifamily surge (p55 +76.2%) that may not persist, a key uncertainty for August.
- corroborating: ['p46', 'p47', 'p48'] Under-construction stock (1.26M total = 582k SF + 682k MF) declining YoY, consistent with a soft but not collapsing starts pipeline.
- corroborating: ['p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75'] Freddie Mac weekly 30-yr rates: rose from ~5.98% Feb low to 6.66% by late July 2026, a headwind for starts with a lag.
- corroborating: ['p42', 'p43', 'p63', 'p64'] TheStreet and Freddie Mac agree on 6.55% (Jul 16) and 6.49% (Jun 30/Jul 9); same underlying Freddie survey.
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85'] NAHB HMI at 34, 15th month below 40, weak traffic (23) and rising price cuts — consistent weak-demand backdrop for starts.
- corroborating: ['p89', 'p90'] New home sales falling (622k Apr, 580k May) corroborate weak builder demand and HMI weakness.
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39'] 2022-2023 permit series from ycharts; older period, useful only as historical context/analogue, not for current level.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p52', 'p133'] Both report June 2026 total starts SAAR near 1.43 million (1,430k vs 1,427k); same underlying Census release, so agreement is not independent confirmation, but confirms the June level.
- corroborating: ['p53', 'p140'] Both give June 2026 single-family starts SAAR of 895k; same Census source.
- corroborating: ['p55', 'p137'] Multifamily June 2026 starts ~513k vs 532k; small definitional difference (5+ units vs multifamily) and rounding; broadly consistent.
- corroborating: ['p52', 'p53', 'p55'] SF 895k + MF 532k ≈ 1,427k, consistent with total 1,430k; internally coherent decomposition.
- corroborating: ['p142', 'p144', 'p145', 'p146'] Regional June starts sum to ~1,427k, matching national total; confirms regional decomposition.
- corroborating: ['p57', 'p58', 'p59'] June permits: SF 871k + MF 496k ≈ 1,367k, consistent with total 1,370k.
- conflicting: ['p52', 'p57'] June starts (1,430k) exceed June permits (1,370k); starts running above permits is unusual and suggests either a temporary multifamily surge (p55) or that the June starts spike is noisy and likely to 
- corroborating: ['p46', 'p47', 'p48'] Under-construction components sum to 1,264k ≈ 1,260k total; internally consistent pipeline picture showing declining construction.
- corroborating: ['p50', 'p51'] SF completions 964k + MF completions 413k ≈ 1,377k total completions pace; consistent with a pipeline drawing down.
- corroborating: ['p61', 'p62', 'p63', 'p64', 'p65'] Freddie Mac weekly rates show a rising trend from ~6.43% early July to 6.66% end-July; single source, sequential weeks.
- corroborating: ['p42', 'p63'] Both cite ~6.55% for week of July 16; same Freddie Mac measurement via different articles.
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85'] NAHB HMI components all point to weak builder sentiment (HMI 34, falling, 15 months below 40, rising price cuts/incentives); single survey source.
- corroborating: ['p89', 'p90'] New home sales falling April→May 2026 (622k→580k); consistent with weak demand backdrop shown by HMI.
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17'] Equibles monthly starts series 2024-2026; single aggregator source, useful for own-history trend but not independent of Census.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] March/February 2024 Census figures; older vintage, useful only as historical context, not for current level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 starts-to-June-permits ratio | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | unused | Historically starts/permits ratio hovers near 1.0; June 2026 starts (1,430k) exceeded permits (1,370k) due to a multifamily surge (p55), so August starts likely revert toward or slightly below the permit level. Wide range reflects month-to-month noise and the June gap. | Permit pipeline is the binding constraint on starts and the June multifamily spike mean-reverts. | Evidence that August multifamily starts sustain the June surge, pushing starts well above permits. |
| a2 | August 2026 change factor vs August 2025 starts | 0.97 | 0.82..1.15 | 0.82..1.15 | ratio | m1 (m1) | Weak builder sentiment (HMI 34, p76), rising mortgage rates (6.66% end-July, p61), and declining under-construction stock (p46) point to a modest year-over-year decline from August 2025's 1,291k (p12). Range reflects uncertainty. | Year-over-year momentum in starts is broadly stable with a slight downward tilt from weak demand. | A sharp rate decline or policy stimulus before August that lifts starts well above last year. |
| a3 | August 2026 SF starts change factor vs June 2026 | 0.98 | 0.85..1.12 | 0.85..1.12 | ratio | m2 (m3) | SF starts have fallen three consecutive months (p140) on high prices and rates; modest further softening expected by August. | SF weakness persists through August. | A rebound in SF permits or sales that reverses the SF downtrend. |
| a4 | August 2026 MF starts change factor vs June 2026 | 0.75 | 0.55..1 | 0.55..1 | ratio | m2 (m3) | June MF starts spiked 76% (p55/p137) after a 41% May plunge; such volatility typically mean-reverts. MF permits declining (p59) and under-construction falling (p48) support a pullback. | The June multifamily surge is a one-off and reverts toward the 3-month average (p56 ~445k). | Evidence of sustained multifamily permit strength or large project starts in July-August. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,249,651 | ['p12'] / ['a2'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 1,282,499 | ['p53', 'p55'] / ['a3', 'a4'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of single-family, multifamily

Result: central **1,265,969** unit/year, 80% interval [918,925, 1,744,077] unit/year, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for the seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026 is 1,265,969 unit/year (80% model-based interval 918,925 to 1,744,077 unit/year). This is a forecast for a future period; no August 2026 observation exists at the cutoff.

Two methods were combined with equal weights: 50% for a year-over-year seasonal-naive route (1,249,651 unit/year) and 50% for a single-family/multifamily decomposition (1,282,499 unit/year). Observed inputs are prior-year August starts of 1,291,000 housing units at annual rate, June single-family starts of 895,000 housing units at annual rate, and June multifamily starts of 532,000 housing units at annual rate. The forecast depends on analyst assumptions: a year-over-year factor of 0.97 (range 0.82 to 1.15), a single-family factor of 0.98 (range 0.85 to 1.12), and a multifamily factor of 0.75 (range 0.55 to 1).

The interval is conditional on these assumptions, not a demonstrated accuracy guarantee. The biggest risk is multifamily volatility and mean reversion. Better evidence would be July and August starts and permits, unavailable before the cutoff.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 August 2026 change factor vs August 2025 starts: 0.97 ratio, range 0.82 to 1.15; used by m1. Overturned by: A sharp rate decline or policy stimulus before August that lifts starts well above last year.
- a3 August 2026 SF starts change factor vs June 2026: 0.98 ratio, range 0.85 to 1.12; used by m2. Overturned by: A rebound in SF permits or sales that reverses the SF downtrend.
- a4 August 2026 MF starts change factor vs June 2026: 0.75 ratio, range 0.55 to 1; used by m2. Overturned by: Evidence of sustained multifamily permit strength or large project starts in July-August.

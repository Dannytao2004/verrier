# Evidence ledger: fc_us_starts_2026_08

- Question: Assume today is 2026-08-17. You know nothing published after this date. Estimate the seasonally adjusted annual rate of privately-owned housing starts in the United States in August 2026 (the number of housing units at an annual rate, as in '1,300,000'), as it will be first reported in the U.S. Census Bureau and HUD Monthly New Residential Construction release.
- as_of: 2026-08-17
- Pinned target: Seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026, covering all privately owned residential units (single-family and multifamily) that began construction during the month, as first estimated by the U.S. Census Bureau and HUD. | unit housing units at a seasonally adjusted annual rate | period 2026-08-01..2026-08-31 | publisher U.S. Census Bureau and U.S. Department of Housing and Urban Development (HUD)

- Official value (scoring only, never shown to the agent): 1,275,000

## Directions and pages

### d1 [own_history] Census/HUD time-series analyst

Hypothesis: The August 2026 private starts SAAR will be anchored by the most recent published private starts level and recent momentum, with August seasonal factors and historical month-to-month volatility defining a plausible range.

Queries issued by the searcher: Census New Residential Construction private housing starts 2026 seasonally adjusted annual rate; New Residential Construction historical table private housing starts monthly 2024 2025 2026; Census "New Residential Construction" seasonal adjustment factors housing starts August table; Census construction nrc historical releases June 2026 newresconst pdf housing starts 1,427,000

- `https://www.investing.com/analysis/us-housing-data-show-why-the-construction-recovery-looks-uneven-200684160` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.census.gov/construction/nrc/pdf/summeas_nrc.pdf` -> **snapshot** (snapshot 20251115180927); points raw/verified 15/15
  - p1 Housing units started, U.S. total, seasonally adjusted series, average month-to- = **6.44** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Started U. S. total 9.56 6.44 6.27 1.09 7"
  - p2 Housing units started, U.S. total, original series, average month-to-month perce = **9.56** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Started U. S. total 9.56 6.44 6.27 1.09 7"
  - p3 Housing units started, U.S. total, irregular component, average month-to-month p = **6.27** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Started U. S. total 9.56 6.44 6.27 1.09 7"
  - p4 Housing units started, U.S. total, trend-cycle component, average month-to-month = **1.09** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Started U. S. total 9.56 6.44 6.27 1.09 7"
  - p5 Housing units started, U.S. total, months for cyclical dominance (2024 seasonal  = **7** months (2024-01-01..2024-12-31) [DISCARD: Months for cyclical dominance is a descriptive timing statistic, not a level or volatility input for the August SAAR est] quote: "Housing Units Started U. S. total 9.56 6.44 6.27 1.09 7"
  - p6 Housing units started, 1 unit, Northeast, seasonally adjusted series, average mo = **12.52** percent (2024-01-01..2024-12-31) [keep: ] quote: "1 unit: Northeast 19.28 12.52 12.51 1.41 12"
  - p7 Housing units started, 1 unit, Midwest, seasonally adjusted series, average mont = **11.87** percent (2024-01-01..2024-12-31) [keep: ] quote: "Midwest 20.78 11.87 11.72 1.37 10"
  - p8 Housing units started, 1 unit, South, seasonally adjusted series, average month- = **7.08** percent (2024-01-01..2024-12-31) [keep: ] quote: "South 9.32 7.08 6.75 1.69 4"
  - p9 Housing units started, 1 unit, West, seasonally adjusted series, average month-t = **9.8** percent (2024-01-01..2024-12-31) [keep: ] quote: "West 12.49 9.80 9.51 1.64 7"
  - p10 Housing units started, 2 units or more, seasonally adjusted series, average mont = **16.41** percent (2024-01-01..2024-12-31) [keep: ] quote: "2 units or more 17.98 16.41 16.11 1.92 10"
  - p11 Housing units started, 2 units or more, original series, average month-to-month  = **17.98** percent (2024-01-01..2024-12-31) [keep: ] quote: "2 units or more 17.98 16.41 16.11 1.92 10"
  - p12 Housing units authorized by building permits, U.S. total, seasonally adjusted se = **3.58** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Authorized by Building Permits U. S. total 9.80 3.58 3.24 1.31 3"
  - p13 Housing units authorized but not started, U.S. total, seasonally adjusted series = **3.21** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Authorized but Not Started U. S. total 3.76 3.21 2.86 1.24 3"
  - p14 Housing units under construction, U.S. total, seasonally adjusted series, averag = **1.13** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Under Construction U. S. total 1.64 1.13 0.45 1.01 1"
  - p15 Housing units completed, U.S. total, seasonally adjusted series, average month-t = **5** percent (2024-01-01..2024-12-31) [keep: ] quote: "Housing Units Completed U. S. total 9.26 5.00 4.86 0.88 6"
- `https://www.economx.hu/documents/549/newresconst.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0

### d2 [related_series] building permit and pipeline analyst

Hypothesis: Private housing starts are constrained by recent private building permits and the backlog of authorized-but-not-started units, so August starts should be near a lagged conversion of permits plus backlog drawdown.

Queries issued by the searcher: private housing units authorized by building permits SAAR July 2026 Census; housing units authorized but not started 2026 Census; "June 2026" housing starts 1,415,000 permits Eye on Housing NAHB July 17 2026; starts to permits ratio single-family multifamily lags housing 2026 analysis

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])1,415,000(?!\\d|[.,]\\d)']; no pages fetched**


### d3 [physical_flow] construction pipeline accountant

Hypothesis: For a given month, private starts approximately equal private completions plus the net change in private units under construction, so recent completions and under-construction stocks can constrain the implied August starts flow.

Queries issued by the searcher: Census Bureau privately owned housing completions seasonally adjusted annual rate 2026; units under construction privately owned housing Census 2026; "MONTHLY NEW RESIDENTIAL CONSTRUCTION, JUNE 2026" under construction "Table 1a" seasonally adjusted annual rate units under construction; Census Survey of Construction methodology units under construction derived starts completions demolitions adjustment

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/3
  - p16 Private housing completions, United States, seasonally adjusted annual rate, Jun = **1,392,000** housing units at seasonally adjusted annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing completions in June were at a seasonally adjusted annual rate of 1,392,000."
  - p17 Private housing completions, United States, seasonally adjusted annual rate, May = **1,347,000** housing units at seasonally adjusted annual rate (2026-05-01..2026-05-31) [keep: ] quote: "above the revised May estimate of 1,347,000"
  - p18 Private housing starts, United States, seasonally adjusted annual rate, June 202 = **1,427,000** housing units at seasonally adjusted annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0
- `https://fred.stlouisfed.org/data/UNDCONTSA` -> **snapshot** (snapshot 20241027061520); points raw/verified 15/0
- `https://www.census.gov/construction/nrc/methodology.html` -> **snapshot** (snapshot 20260723225717); points raw/verified 0/0
- dropped by code checks: 27 (scale word 'thousand' not supported by quote or table header: 26; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d4 [related_series] homebuilder and multifamily developer

Hypothesis: Private starts are the sum of single-family and multifamily starts, whose drivers differ; estimating each component separately reduces error from volatile multifamily projects.

Queries issued by the searcher: single-family multifamily housing starts SAAR June 2026 Census Bureau; NAHB housing market index August 2026; Census rental vacancy rate second quarter 2026 multifamily completions absorption; apartment construction starts 2026 multifamily permits July 2026 forecast

- `https://www.sbcacomponents.com/media/multifamily-starts-surge-in-june-as-single-family-drops` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mpamag.com/us/mortgage-industry/market-updates/us-housing-starts-rebound-in-june-but-single-family-woes-deepen/582788` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sa.marketscreener.com/news/us-home-builder-sentiment-ticks-up-in-august-but-remains-weak-overall-ce7859dcdb8df224` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.globest.com/2026/08/12/lower-vacancy-does-not-tell-the-full-apartment-story/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] single-family demand and inventory analyst

Hypothesis: Single-family starts respond to new-home sales, inventory of homes under construction, and mortgage rates; weak or strong demand signals should shift the single-family component relative to its recent baseline.

Queries issued by the searcher: new single-family home sales 2026 months supply inventory Census; mortgage rate August 2026 30-year fixed Freddie Mac; new residential sales June 2026 Census Bureau release July 24 2026 months supply; housing starts June 2026 Census Bureau single-family rate permits

- `https://www.hud.gov/news/hud-no-26-056` -> **snapshot** (snapshot 20260811211448); points raw/verified 13/11
  - p19 New single-family houses sold, US, seasonally adjusted annual rate, June 2026 = **628,000** houses per year (2026-06-01..2026-06-30) [keep: ] quote: "Sales of new single-family houses in June 2026 were at a seasonally-adjusted annual rate of 628,000"
  - p20 New single-family houses sold, US, seasonally adjusted annual rate, May 2026 = **618,000** houses per year (2026-05-01..2026-05-31) [keep: ] quote: "above the May 2026 rate of 618,000"
  - p21 New single-family houses sold, US, seasonally adjusted annual rate, June 2025 = **665,000** houses per year (2025-06-01..2025-06-30) [keep: ] quote: "below the June 2025 rate of 665,000"
  - p22 New houses for sale, US, seasonally adjusted estimate, end of June 2026 = **485,000** houses (2026-06-30..2026-06-30) [keep: ] quote: "The seasonally-adjusted estimate of new houses for sale at the end of June 2026 was 485,000."
  - p23 New houses for sale, US, seasonally adjusted estimate, end of May 2026 = **486,000** houses (2026-05-31..2026-05-31) [keep: ] quote: "below the May 2026 estimate of 486,000"
  - p24 New houses for sale, US, seasonally adjusted estimate, end of June 2025 = **501,000** houses (2025-06-30..2025-06-30) [keep: ] quote: "below the June 2025 estimate of 501,000"
  - p25 Months' supply of new houses at current sales rate, US, June 2026 = **9.3** months (2026-06-01..2026-06-30) [keep: ] quote: "This represents a supply of 9.3 months at the current sales rate."
  - p26 Months' supply of new houses at current sales rate, US, May 2026 = **9.4** months (2026-05-01..2026-05-31) [keep: ] quote: "below the May 2026 estimate of 9.4 months"
  - p27 Months' supply of new houses at current sales rate, US, June 2025 = **9** months (2025-06-01..2025-06-30) [keep: ] quote: "above the June 2025 estimate of 9.0 months"
  - p28 Median sales price of new houses sold, US, June 2026 = **398,300** USD (2026-06-01..2026-06-30) [keep: ] quote: "The median sales price of new houses sold in June 2026 was $398,300."
  - p29 Average sales price of new houses sold, US, June 2026 = **475,400** USD (2026-06-01..2026-06-30) [keep: ] quote: "The average sales price of new houses sold in June 2026 was $475,400."
- `https://www.freddiemac.com/pmms/archive` -> **snapshot** (snapshot 20260731224527); points raw/verified 15/15
  - p30 30-year fixed rate mortgage average, week of July 30, 2026 = **6.66** % (2026-07-30..2026-07-30) [keep: ] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
  - p31 30-year fixed rate mortgage average, week of July 23, 2026 = **6.58** % (2026-07-23..2026-07-23) [keep: ] quote: "July 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.58% \| 5.96% \|"
  - p32 30-year fixed rate mortgage average, week of July 16, 2026 = **6.55** % (2026-07-16..2026-07-16) [keep: ] quote: "July 16, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.55% \| 5.93% \|"
  - p33 30-year fixed rate mortgage average, week of July 09, 2026 = **6.49** % (2026-07-09..2026-07-09) [keep: ] quote: "July 09, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.82% \|"
  - p34 30-year fixed rate mortgage average, week of July 02, 2026 = **6.43** % (2026-07-02..2026-07-02) [keep: ] quote: "July 02, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.43% \| 5.79% \|"
  - p35 30-year fixed rate mortgage average, week of June 25, 2026 = **6.49** % (2026-06-25..2026-06-25) [keep: ] quote: "June 25, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.84% \|"
  - p36 30-year fixed rate mortgage average, week of June 18, 2026 = **6.47** % (2026-06-18..2026-06-18) [keep: ] quote: "June 18, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.47% \| 5.81% \|"
  - p37 30-year fixed rate mortgage average, week of June 11, 2026 = **6.52** % (2026-06-11..2026-06-11) [keep: ] quote: "June 11, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.52% \| 5.84% \|"
  - p38 30-year fixed rate mortgage average, week of June 04, 2026 = **6.48** % (2026-06-04..2026-06-04) [keep: ] quote: "June 04, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.48% \| 5.79% \|"
  - p39 30-year fixed rate mortgage average, week of May 28, 2026 = **6.53** % (2026-05-28..2026-05-28) [keep: ] quote: "May 28, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.53% \| 5.87% \|"
  - p40 30-year fixed rate mortgage average, week of May 21, 2026 = **6.51** % (2026-05-21..2026-05-21) [keep: ] quote: "May 21, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.51% \| 5.85% \|"
  - p41 30-year fixed rate mortgage average, week of May 14, 2026 = **6.36** % (2026-05-14..2026-05-14) [keep: ] quote: "May 14, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.36% \| 5.71% \|"
  - p42 30-year fixed rate mortgage average, week of May 07, 2026 = **6.37** % (2026-05-07..2026-05-07) [keep: ] quote: "May 07, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.37% \| 5.72% \|"
  - p43 30-year fixed rate mortgage average, week of April 30, 2026 = **6.3** % (2026-04-30..2026-04-30) [keep: ] quote: "April 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.30% \| 5.64% \|"
  - p44 30-year fixed rate mortgage average, week of April 23, 2026 = **6.23** % (2026-04-23..2026-04-23) [keep: ] quote: "April 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.23% \| 5.58% \|"
- `https://www.homes.com/news/lower-prices-lift-new-home-sales-despite-high-rates/551181421/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eyeonhousing.org/2026/05/new-home-sales-rise-supported-by-limited-existing-inventory/` -> **snapshot** (snapshot 20260517220456); points raw/verified 15/14
  - p45 New single-family home sales SAAR, United States, March = **682,000** housing units at a seasonally adjusted annual rate (2026-03-01..2026-03-31) [keep: ] quote: "Sales of newly built single-family homes increased 7.4% month-over-month in March to a seasonally adjusted annual rate of 682,000 units"
  - p46 Month-over-month change in new single-family home sales, March = **7.4** % (2026-03-01..2026-03-31) [keep: ] quote: "Sales of newly built single-family homes increased 7.4% month-over-month in March"
  - p47 Year-over-year change in new single-family home sales, March = **3.3** % (2026-03-01..2026-03-31) [keep: ] quote: "This represented a 3.3% increase compared to a year earlier."
  - p48 New single-family home inventory, United States, March = **481,000** housing units (2026-03-01..2026-03-31) [keep: ] quote: "New single-family home inventory totaled 481,000 units in March, down 0.4% from the prior month and 4.6% from a year earlier."
  - p49 Months' supply of new homes at current sales pace, March = **8.5** months (2026-03-01..2026-03-31) [keep: ] quote: "At the current sales pace, the months' supply of new homes stood at 8.5 months, down from 9.2 months one year ago"
  - p50 Months' supply of new homes one year earlier = **9.2** months (2025-03-01..2025-03-31) [keep: ] quote: "down from 9.2 months one year ago, though still above the six-month level generally considered to indicate a balanced market"
  - p51 Completed ready-to-occupy new homes for sale, end of March, non-seasonally adjus = **119,000** housing units (2026-03-01..2026-03-31) [keep: ] quote: "At the end of March, there were 119,000 completed, ready-to-occupy homes available for sale on a non-seasonally adjusted basis, up 5.3% from a year earlier."
  - p52 Share of total new home inventory that was completed homes, March = **0.25** as written "one-quarter", value check pending share of total inventory (2026-03-01..2026-03-31) [keep: ] quote: "Completed homes accounted for one-quarter of total inventory, while homes under construction made up 51%."
  - p53 Share of total new home inventory that was homes under construction, March = **51** % (2026-03-01..2026-03-31) [keep: ] quote: "Completed homes accounted for one-quarter of total inventory, while homes under construction made up 51%."
  - p54 Share of March new home sales not yet started construction at contract signing = **24** % (2026-03-01..2026-03-31) [keep: ] quote: "The remaining 24% of homes sold in March had not yet started construction at the time the sales contract was signed."
  - p55 Median new home sale price, United States, March = **387,400** USD (2026-03-01..2026-03-31) [keep: ] quote: "The median new home sale price was $387,400, down 6.2% from a year ago"
  - p56 Year-over-year change in median new home sale price, March = **6.2** % (2026-03-01..2026-03-31) [DISCARD: Sign/definition ambiguity: the quote says median price was down 6.2%, but the recorded value is positive 6.2.] quote: "The median new home sale price was $387,400, down 6.2% from a year ago"
  - p57 Share of new homes priced below $300,000, March = **20** % (2026-03-01..2026-03-31) [keep: ] quote: "Affordability improved at the lower end of the market, with 20 percent of new homes priced below $300,000."
  - p58 Year-over-year change in new home sales, Northeast, March = **17.6** % (2026-03-01..2026-03-31) [DISCARD: Sign/scope ambiguity: the quote says Northeast sales declined 17.6%, but the recorded value is positive 17.6 and is regi] quote: "New home sales declined 17.6% in the Northeast, 14.0% in the West and 2.6% in the South."
- dropped by code checks: 3 (period_end missing or unparseable: 3)

### d6 [capacity_consumption] construction economist

Hypothesis: Real residential construction activity, construction employment, and material use provide a cross-check on whether starts are running near capacity or are constrained by labor and materials.

Queries issued by the searcher: residential construction spending June 2026 Census Bureau; housing starts July 2026 Census Bureau HUD; June 2026 housing starts 1,415,000 Census Bureau July 17 2026 release; residential construction employment July 2026 BLS construction sector jobs

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])1,415,000(?!\\d|[.,]\\d)']; no pages fetched**


### d7 [shocks] risk and calendar analyst

Hypothesis: Weather, mortgage-rate moves, material costs, tariffs, and regional disruptions in August 2026 could push starts away from the recent trend; measurable exposure should be used to adjust or widen the estimate.

Queries issued by the searcher: 30-year mortgage rate August 2026 Freddie Mac Primary Mortgage Market Survey; housing starts July 2026 Census Bureau seasonally adjusted annual rate; NAHB/Wells Fargo Housing Market Index August 2026 builder confidence; lumber prices tariffs August 2026 homebuilders construction costs

- `https://finance-commerce.com/2026/08/homebuilder-sentiment-rises-high-mortgage-rates-costs/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.freddiemac.com/pmms/archive` -> **snapshot** (snapshot 20260731224527); points raw/verified 15/15
  - p59 30-year fixed-rate mortgage average rate, week of July 30, 2026 = **6.66** % (2026-07-30..2026-07-30) [DISCARD: Exact duplicate of p30; redundant Freddie Mac weekly rate.] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
  - p60 30-year fixed-rate mortgage average rate, week of July 23, 2026 = **6.58** % (2026-07-23..2026-07-23) [DISCARD: Exact duplicate of p31; redundant Freddie Mac weekly rate.] quote: "July 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.58% \| 5.96% \|"
  - p61 30-year fixed-rate mortgage average rate, week of July 16, 2026 = **6.55** % (2026-07-16..2026-07-16) [DISCARD: Exact duplicate of p32; redundant Freddie Mac weekly rate.] quote: "July 16, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.55% \| 5.93% \|"
  - p62 30-year fixed-rate mortgage average rate, week of July 09, 2026 = **6.49** % (2026-07-09..2026-07-09) [DISCARD: Exact duplicate of p33; redundant Freddie Mac weekly rate.] quote: "July 09, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.82% \|"
  - p63 30-year fixed-rate mortgage average rate, week of July 02, 2026 = **6.43** % (2026-07-02..2026-07-02) [DISCARD: Exact duplicate of p34; redundant Freddie Mac weekly rate.] quote: "July 02, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.43% \| 5.79% \|"
  - p64 30-year fixed-rate mortgage average rate, week of June 25, 2026 = **6.49** % (2026-06-25..2026-06-25) [DISCARD: Exact duplicate of p35; redundant Freddie Mac weekly rate.] quote: "June 25, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.84% \|"
  - p65 30-year fixed-rate mortgage average rate, week of June 18, 2026 = **6.47** % (2026-06-18..2026-06-18) [DISCARD: Exact duplicate of p36; redundant Freddie Mac weekly rate.] quote: "June 18, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.47% \| 5.81% \|"
  - p66 30-year fixed-rate mortgage average rate, week of June 11, 2026 = **6.52** % (2026-06-11..2026-06-11) [DISCARD: Exact duplicate of p37; redundant Freddie Mac weekly rate.] quote: "June 11, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.52% \| 5.84% \|"
  - p67 30-year fixed-rate mortgage average rate, week of June 04, 2026 = **6.48** % (2026-06-04..2026-06-04) [DISCARD: Exact duplicate of p38; redundant Freddie Mac weekly rate.] quote: "June 04, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.48% \| 5.79% \|"
  - p68 30-year fixed-rate mortgage average rate, week of May 28, 2026 = **6.53** % (2026-05-28..2026-05-28) [DISCARD: Exact duplicate of p39; redundant Freddie Mac weekly rate.] quote: "May 28, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.53% \| 5.87% \|"
  - p69 30-year fixed-rate mortgage average rate, week of May 21, 2026 = **6.51** % (2026-05-21..2026-05-21) [DISCARD: Exact duplicate of p40; redundant Freddie Mac weekly rate.] quote: "May 21, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.51% \| 5.85% \|"
  - p70 30-year fixed-rate mortgage average rate, week of May 14, 2026 = **6.36** % (2026-05-14..2026-05-14) [DISCARD: Exact duplicate of p41; redundant Freddie Mac weekly rate.] quote: "May 14, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.36% \| 5.71% \|"
  - p71 30-year fixed-rate mortgage average rate, week of May 07, 2026 = **6.37** % (2026-05-07..2026-05-07) [DISCARD: Exact duplicate of p42; redundant Freddie Mac weekly rate.] quote: "May 07, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.37% \| 5.72% \|"
  - p72 30-year fixed-rate mortgage average rate, week of April 30, 2026 = **6.3** % (2026-04-30..2026-04-30) [DISCARD: Exact duplicate of p43; redundant Freddie Mac weekly rate.] quote: "April 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.30% \| 5.64% \|"
  - p73 30-year fixed-rate mortgage average rate, week of April 23, 2026 = **6.23** % (2026-04-23..2026-04-23) [DISCARD: Exact duplicate of p44; redundant Freddie Mac weekly rate.] quote: "April 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.23% \| 5.58% \|"
- `https://freddiemac.gcs-web.com/news-releases/news-release-details/mortgage-rates-average-667` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.builderonline.com/data-analysis/builder-sentiment-shows-little-improvement-in-august/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [forecasts_markets] market forecaster

Hypothesis: Published professional forecasts and consensus estimates for August 2026 housing starts provide a comparison anchor, though they may rely on the same recent Census data and should not be treated as independent observations.

Queries issued by the searcher: US housing starts forecast August 2026; housing starts consensus estimate September 2026 Census Bureau; Fannie Mae housing forecast August 2026 housing starts 2026 annual; NAHB forecast housing starts 2026 July 2026 outlook single-family; "Housing Forecast: August 2026" Fannie Mae

- `https://cmegroup.econoday.com/byevent?fid=667073&year=2026&cty=US&ctyall=10738893&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://us.econoday.com/byevent?fid=667073&year=2026&cty=US&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/forecast/housing-starts?continent=g20` -> **snapshot** (snapshot 20210819091006); points raw/verified 0/0
- `https://newslink.mba.org/cmf-newslinks/2026/september/mba-commercial-multifamily-newslink-jan-30/chart-of-the-week-new-residential-construction/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Fill the one-month gap between the June 2026 Census starts observation and the August target.

Hypothesis: If July 2026 private housing starts and permits are available before the August target, they will directly update the anchor and reduce reliance on a large June-to-August change factor. A July print would also show whether the June level was sustained.

Queries issued by the searcher: July 2026 housing starts building permits Census HUD release; "housing starts" July 2026 seasonally adjusted annual rate private; NAHB Wells Fargo Housing Market Index August 2026 released August 17 2026 builder confidence 35; census.gov new residential construction June 2026 "1,427,000" privately-owned housing starts table

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/13
  - p74 U.S. privately-owned housing starts, total, SAAR (March 2024) = **1,321,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p75 U.S. single-family housing starts, SAAR (March 2024) = **1,022,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p76 U.S. housing starts in buildings with five units or more, SAAR (March 2024) = **290,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "The March rate for units in buildings with five units or more was 290,000."
  - p77 U.S. privately-owned housing starts, total, SAAR, revised February 2024 = **1,549,000** housing units at seasonally adjusted annual rate (2024-02-01..2024-02-29) [keep: ] quote: "This is 14.7 percent (±9.9 percent) below the revised February estimate of 1,549,000"
  - p78 U.S. single-family housing starts, SAAR, revised February 2024 = **1,167,000** housing units at seasonally adjusted annual rate (2024-02-01..2024-02-29) [keep: ] quote: "below the revised February figure of 1,167,000"
  - p79 U.S. privately-owned housing units authorized by building permits, total, SAAR ( = **1,458,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Privately‐owned housing units authorized by building permits in March were at a seasonally adjusted annual rate of 1,458,000."
  - p80 U.S. single-family building permit authorizations, SAAR (March 2024) = **973,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Single‐family authorizations in March were at a rate of 973,000"
  - p81 U.S. building permit authorizations in buildings with five units or more, SAAR ( = **433,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Authorizations of units in buildings with five units or more were at a rate of 433,000 in March."
  - p82 U.S. total building permits, SAAR, revised February 2024 = **1,523,000** housing units at seasonally adjusted annual rate (2024-02-01..2024-02-29) [keep: ] quote: "This is 4.3 percent below the revised February rate of 1,523,000"
  - p83 U.S. single-family building permits, SAAR, revised February 2024 = **1,032,000** housing units at seasonally adjusted annual rate (2024-02-01..2024-02-29) [keep: ] quote: "this is 5.7 percent below the revised February figure of 1,032,000"
  - p84 U.S. privately-owned housing completions, total, SAAR (March 2024) = **1,469,000** housing units at seasonally adjusted annual rate (2024-03-01..2024-03-31) [keep: ] quote: "Privately‐owned housing completions in March were at a seasonally adjusted annual rate of 1,469,000."
  - p85 U.S. privately-owned housing starts, total, SAAR (March 2023) = **1,380,000** housing units at seasonally adjusted annual rate (2023-03-01..2023-03-31) [keep: ] quote: "below the March 2023 rate of 1,380,000"
  - p86 U.S. total building permits, SAAR (March 2023) = **1,437,000** housing units at seasonally adjusted annual rate (2023-03-01..2023-03-31) [keep: ] quote: "but is 1.5 percent above the March 2023 rate of 1,437,000"
- `https://www.investing.com/news/economy-news/us-home-builder-sentiment-ticks-up-in-august-but-remains-weak-overall-4863446` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fidelity-advisor.econoday.com/byevent?fid=667072&cust=fidelity-advisor&lid=0&year=2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/series/HOUST` -> **snapshot** (snapshot 20260729074521); points raw/verified 5/0
- dropped by code checks: 7 (scale word 'thousand' not supported by quote or table header: 7)

### b2 [related_series] Constrain the physical flow identity and the single-family/multifamily split.

Hypothesis: Private units under construction and authorized-but-not-started for June or July 2026 would let us reconcile starts with completions and reduce dependence on assumed ratios. A single-family versus multifamily starts split would make the component route direct rather than assumption-heavy.

Queries issued by the searcher: Census Bureau HUD new residential construction July 2026 housing starts privately owned units under construction; "new residential construction" June 2026 housing starts seasonally adjusted annual rate single-family multifamily; census "new residential construction" June 2026 table "units under construction" "authorized, but not started" 1,2xx,000; Fannie Mae housing forecast August 2026 housing starts 2026 total single-family multifamily forecast

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/0
- `https://www.investing.com/analysis/us-housing-data-show-why-the-construction-recovery-looks-uneven-200684160` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0
- `https://www.innowave-studio.com/post/builders-stopped-digging-they-did-not-stop-filing` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 15)

### b3 [shocks] Measure August 2026 high-frequency conditions that could move starts away from the June anchor.

Hypothesis: July residential construction employment, the August NAHB housing market index, early-August mortgage rates, and regional weather/permit disruptions would help set the sign and size of the June-to-August change factor and the mortgage-rate pass-through. Without them the main uncertainty is an unobserved August shock.

Queries issued by the searcher: NAHB/Wells Fargo Housing Market Index August 2026; Freddie Mac Primary Mortgage Market Survey August 2026 30-year fixed rate; BLS July 2026 residential building construction employment NAICS 2361 construction employees; June 2026 housing starts seasonally adjusted annual rate Census Bureau privately owned

- `https://www.sbcacomponents.com/media/builder-sentiment-remains-low-on-affordability-concerns` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bls.gov/iag/tgs/iag236.htm` -> **snapshot** (snapshot 20260612211239); points raw/verified 15/15
  - p87 Employment, all employees (seasonally adjusted) in construction of buildings, Fe = **1,863,000** jobs (2026-02-01..2026-02-28) [keep: ] quote: "\| Employment, all employees (seasonally adjusted) \| \| 1,863.0 \| 1,864.9 \| (p)1,868.9 \| (p)1,868.9 \|"
  - p88 Employment, all employees (seasonally adjusted) in construction of buildings, Ma = **1,864,900** jobs (2026-03-01..2026-03-31) [keep: ] quote: "\| Employment, all employees (seasonally adjusted) \| \| 1,863.0 \| 1,864.9 \| (p)1,868.9 \| (p)1,868.9 \|"
  - p89 Employment, all employees (seasonally adjusted) in construction of buildings, Ap = **1,868,900** jobs (2026-04-01..2026-04-30) [keep: ] quote: "\| Employment, all employees (seasonally adjusted) \| \| 1,863.0 \| 1,864.9 \| (p)1,868.9 \| (p)1,868.9 \|"
  - p90 Employment, all employees (seasonally adjusted) in construction of buildings, Ma = **1,868,900** jobs (2026-05-01..2026-05-31) [keep: ] quote: "\| Employment, all employees (seasonally adjusted) \| \| 1,863.0 \| 1,864.9 \| (p)1,868.9 \| (p)1,868.9 \|"
  - p91 Employment, production and nonsupervisory employees in construction of buildings = **1,131,200** jobs (2026-02-01..2026-02-28) [keep: ] quote: "\| Employment, production and nonsupervisory employees \| \| 1,131.2 \| 1,144.1 \| (p)1,160.8 \| \|"
  - p92 Employment, production and nonsupervisory employees in construction of buildings = **1,144,100** jobs (2026-03-01..2026-03-31) [keep: ] quote: "\| Employment, production and nonsupervisory employees \| \| 1,131.2 \| 1,144.1 \| (p)1,160.8 \| \|"
  - p93 Employment, production and nonsupervisory employees in construction of buildings = **1,160,800** jobs (2026-04-01..2026-04-30) [keep: ] quote: "\| Employment, production and nonsupervisory employees \| \| 1,131.2 \| 1,144.1 \| (p)1,160.8 \| \|"
  - p94 Average weekly hours, all employees in construction of buildings, Jan. 2026 = **38** hours per week (2026-01-01..2026-01-31) [keep: ] quote: "\| Average weekly hours \| \| 38.0 \| 38.4 \| 38.3 \| (p)38.5 \|"
  - p95 Average weekly hours, all employees in construction of buildings, Feb. 2026 = **38.4** hours per week (2026-02-01..2026-02-28) [keep: ] quote: "\| Average weekly hours \| \| 38.0 \| 38.4 \| 38.3 \| (p)38.5 \|"
  - p96 Average weekly hours, all employees in construction of buildings, Mar. 2026 = **38.3** hours per week (2026-03-01..2026-03-31) [keep: ] quote: "\| Average weekly hours \| \| 38.0 \| 38.4 \| 38.3 \| (p)38.5 \|"
  - p97 Average weekly hours, all employees in construction of buildings, Apr. 2026 (pre = **38.5** hours per week (2026-04-01..2026-04-30) [keep: ] quote: "\| Average weekly hours \| \| 38.0 \| 38.4 \| 38.3 \| (p)38.5 \|"
  - p98 Average weekly hours, production and nonsupervisory employees in construction of = **39.2** hours per week (2026-04-01..2026-04-30) [keep: ] quote: "\| Average weekly hours \| \| 38.7 \| 39.0 \| 39.0 \| (p)39.2 \|"
  - p99 Average hourly earnings, all employees in construction of buildings, Apr. 2026 ( = **43.51** USD per hour (2026-04-01..2026-04-30) [keep: ] quote: "\| Average hourly earnings \| \| $43.13 \| $43.37 \| $43.40 \| (p)$43.51 \|"
  - p100 Number of private industry establishments in construction of buildings, 4th quar = **297,677** establishments (2025-10-01..2025-12-31) [keep: ] quote: "\| Private industry \| \| (p)291,629 \| (p)293,977 \| (p)295,845 \| (p)297,677 \|"
  - p101 Carpenters employment in construction of buildings, 2025 = **312,950** jobs (2025-01-01..2025-12-31) [keep: ] quote: "\| Carpenters \| 312,950 \|"
- `https://www.freddiemac.com/pmms/archive` -> **snapshot** (snapshot 20260731224527); points raw/verified 14/14
  - p102 Freddie Mac 30-year fixed rate mortgage average, week of July 30, 2026 = **6.66** % (2026-07-30..2026-07-30) [DISCARD: Identical duplicate of p30; 30-year fixed rate for week of July 30, 2026 adds no independent information.] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
  - p103 Freddie Mac 15-year fixed rate mortgage average, week of July 30, 2026 = **6.04** % (2026-07-30..2026-07-30) [keep: ] quote: "\| Average Rates \| 6.66% \| 6.04% \|"
  - p104 Freddie Mac 30-year fixed rate mortgage average, week of July 23, 2026 = **6.58** % (2026-07-23..2026-07-23) [DISCARD: Identical duplicate of p31; redundant copy of the 30-year rate for week of July 23, 2026.] quote: "July 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.58% \| 5.96% \|"
  - p105 Freddie Mac 15-year fixed rate mortgage average, week of July 23, 2026 = **5.96** % (2026-07-23..2026-07-23) [keep: ] quote: "\| Average Rates \| 6.58% \| 5.96% \|"
  - p106 Freddie Mac 30-year fixed rate mortgage average, week of July 16, 2026 = **6.55** % (2026-07-16..2026-07-16) [DISCARD: Identical duplicate of p32; redundant copy of the 30-year rate for week of July 16, 2026.] quote: "July 16, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.55% \| 5.93% \|"
  - p107 Freddie Mac 15-year fixed rate mortgage average, week of July 16, 2026 = **5.93** % (2026-07-16..2026-07-16) [keep: ] quote: "\| Average Rates \| 6.55% \| 5.93% \|"
  - p108 Freddie Mac 30-year fixed rate mortgage average, week of July 09, 2026 = **6.49** % (2026-07-09..2026-07-09) [DISCARD: Identical duplicate of p33; redundant copy of the 30-year rate for week of July 09, 2026.] quote: "July 09, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.82% \|"
  - p109 Freddie Mac 15-year fixed rate mortgage average, week of July 09, 2026 = **5.82** % (2026-07-09..2026-07-09) [keep: ] quote: "\| Average Rates \| 6.49% \| 5.82% \|"
  - p110 Freddie Mac 30-year fixed rate mortgage average, week of July 02, 2026 = **6.43** % (2026-07-02..2026-07-02) [DISCARD: Identical duplicate of p34; redundant copy of the 30-year rate for week of July 02, 2026.] quote: "July 02, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.43% \| 5.79% \|"
  - p111 Freddie Mac 15-year fixed rate mortgage average, week of July 02, 2026 = **5.79** % (2026-07-02..2026-07-02) [keep: ] quote: "\| Average Rates \| 6.43% \| 5.79% \|"
  - p112 Freddie Mac 30-year fixed rate mortgage average, week of June 25, 2026 = **6.49** % (2026-06-25..2026-06-25) [DISCARD: Identical duplicate of p35; redundant copy of the 30-year rate for week of June 25, 2026.] quote: "June 25, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.84% \|"
  - p113 Freddie Mac 15-year fixed rate mortgage average, week of June 25, 2026 = **5.84** % (2026-06-25..2026-06-25) [keep: ] quote: "\| Average Rates \| 6.49% \| 5.84% \|"
  - p114 Freddie Mac 30-year fixed rate mortgage average, week of June 18, 2026 = **6.47** % (2026-06-18..2026-06-18) [DISCARD: Identical duplicate of p36; redundant copy of the 30-year rate for week of June 18, 2026.] quote: "June 18, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.47% \| 5.81% \|"
  - p115 Freddie Mac 15-year fixed rate mortgage average, week of June 18, 2026 = **5.81** % (2026-06-18..2026-06-18) [keep: ] quote: "\| Average Rates \| 6.47% \| 5.81% \|"
- `https://www.woodfloorbusiness.com/news/article/15832021/residential-construction-jobs-rise-in-july` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['housing starts', 'us housing', 'august housing starts']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p16', 'p17', 'p18'] Same Census/HUD Monthly New Residential Construction release. p18 is June 2026 private starts SAAR 1,427,000; p16 is June private completions 1,392,000; p17 is May completions 1,347,000. Starts are sl
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] Same HUD new-home-sales release. June 2026 sales 628,000 are above May 618,000 but below June 2025 665,000; inventory 485,000 is near May 486,000 and below June 2025 501,000; months' supply 9.3 is sli
- contextual: ['p28', 'p29', 'p55'] New-home price levels from June 2026 and March 2026. They are different months and median versus average measures, so they are not direct contradictions; p55 is older context and not used as an August
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73'] Freddie Mac weekly 30-year fixed mortgage rates. p30-p44 and p59-p73 are exact duplicate copies of the same weekly series and values. Rates rise from 6.49% in late June (p35) to 6.66% by July 30 (p30)
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p57'] March 2026 NAHB/Eye on Housing summary: new-home sales 682,000, inventory 481,000, months' supply 8.5 versus 9.2 a year earlier but still above the balanced-market benchmark; 25% of inventory complete
- contextual: ['p1', 'p3', 'p4'] Census 2024 seasonal summary: total SA starts average month-to-month change 6.44%, irregular component 6.27%, trend-cycle 1.09%. These support high monthly noise and low recent trend; they are volatil
- contextual: ['p6', 'p7', 'p8', 'p9', 'p10'] 2024 regional single-family and multifamily SA month-to-month volatility. Multifamily p10 is much more volatile than single-family regions, so total starts uncertainty should be wide; these are not di
- contextual: ['p12', 'p13', 'p14', 'p15', 'p2', 'p11'] 2024 permit, authorized-not-started, under-construction, completion, and original-series volatility. These indicate pipeline and flow volatility but are not target levels. The original-series p2 and p
- conflicting: ['p56', 'p58'] Sign/definition ambiguity. p56 says the median price was 'down 6.2%' but records a positive 6.2; p58 says Northeast new-home sales 'declined 17.6%' but records a positive 17.6 and is regional. These a
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p16', 'p17', 'p18'] Same Census/HUD release and same construction flow. June private starts 1.427M exceed June completions 1.392M; completions rose from 1.347M in May. The gap implies a positive net change in units under
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] New single-family sales: June 628k, May 618k, June 2025 665k. Inventory 485k and 9.3 months' supply (May 486k/9.4; June 2025 501k/9.0). Modest MoM sales gain but YoY decline and elevated months' suppl
- context: ['p28', 'p29', 'p55'] New-home prices (June median 398.3k, average 475.4k; March median 387.4k) reflect affordability pressure but do not map directly to starts. Kept as context for demand.
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43'] Freddie Mac 30-year fixed rates rose from about 6.49% in late June to 6.66% by July 30, 2026. Same source, sequential weeks; a modest financing headwind for SF starts. p30 and p35 are the endpoints us
- redundant: ['p102', 'p104', 'p106', 'p108', 'p110', 'p112', 'p114'] Identical 30-year rate copies of p30, p31, p32, p33, p34, p35, p36 respectively; no additional information, discarded. The 15-year rate points p103,p105,p107,p109,p111,p113,p115 are unique but not use
- context: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54'] March 2026 new-home data: sales 682k, inventory 481k, 8.5 months' supply, 24% of sales not started, 51% of inventory under construction. Older than June but consistent with elevated inventory and a pi
- context: ['p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86'] March 2023/2024 Census starts/permits/completions: March 2024 total private starts 1.321M, SF 1.022M, MF 290k; permits 1.458M. Used only for historical component scaling (p74/p75) and share benchmarks
- context: ['p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101'] BLS construction-of-buildings employment stable/slightly rising through May 2026; weekly hours stable. Suggests capacity is not collapsing, but no direct starts conversion is available.
- context: ['p1', 'p2', 'p3', 'p4', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Census 2024 seasonal-summary volatility: total starts average MoM 6.44% SA, MF 16.41%, completions 5.00%, under construction 1.13%, permits 3.58%. Used to judge plausible month-to-month range, not lev
- context: ['p18', 'p19', 'p22', 'p25'] June private starts 1.427M and new SF sales 628k with 485k inventory/9.3 months jointly imply single-family starts per sale near 1.5 only if multifamily share is about one-third; this is a model bridg

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August-to-June private starts ratio | 0.97 | 0.86..1.09 | 0.6846..1.369 (widened) | ratio | m1 (m1) | Anchor p18 is June 2026 private starts. p1 shows total starts average month-to-month absolute change 6.44% SA in 2024 and p10 shows multifamily 16.41%, so a two-month move of roughly 9-13% is plausible. p30/p35 shows mortgage rates up about 17 bp, p19/p20 shows June SF sales only 10k above May, and  | August 2026 conditions remain near the June-July trend and no large weather/credit shock hits starts. | A July 2026 starts print far from 1.4M or evidence of a large August shock. |
| a2 | mortgage-rate pass-through to private starts | 0.5 | 0.1..1.5 | 0.1..1.5 | ratio | m2 (m2) | Maps the p30/p35 rate ratio into a proportional starts adjustment. A 17 bp rise is small; pass-through is lagged and uncertain. 0.5 means the rate ratio effect is halved; range admits near-zero to strong response. | The July rate increase is a useful proxy for August financing conditions. | Evidence that starts are insensitive to mortgage rates or that a much larger August rate move dominates. |
| a3 | single-family private starts per new single-family home sold | 1.5 | 1.2..1.8 | 1.039..2.078 (widened) | ratio | m3 (m3) | p19 June 2026 new SF sales 628k; p18 total private starts 1.427M and p74/p75 historical split imply SF starts around 0.95M if MF share is about one-third, giving a ratio near 1.5. p25 9.3 months' supply is above balanced 6 months, so the value should be at the lower end; p54 24% of March sales not s | Builders keep starting homes in line with current sales and sold-not-started backlog. | A Census SF/MF starts split showing SF starts per sale outside 1.2-1.8 or a sharp inventory correction. |
| a4 | total-to-single-family starts ratio adjustment, 2026 vs March 2024 | 1.15 | 0.9..1.45 | 0.8078..1.616 (widened) | ratio | m3 (m3) | p74/p75 gives March 2024 total/SF starts ratio 1,321/1,022=1.293. p76/p74 shows MF share then about 22%; p81/p79 shows MF permit share about 30%. If August 2026 MF share is near one-third, total/SF ratio should be near 1.49, about 1.15 times the 2024 ratio. Range covers MF share from low to high. | Multifamily's share of private starts is not radically different from the late-2024/2026 range. | Current SF/MF split showing multifamily share near the 2024 22% level or far above one-third. |
| a5 | August private starts to June private completions ratio | 1 | 0.84..1.18 | 0.704..1.408 (widened) | ratio | m4 (m4) | p16 June completions 1.392M; p18 June starts 1.427M gives a June ratio of 1.025. p16/p17 shows completions rising 45k from May, while p14 shows under-construction stock changes slowly (1.13% average monthly). A ratio near 1.0 is a physical-flow anchor, with uncertainty from unobserved net under-cons | The net change in private units under construction between June and August is not large. | Evidence of a large drawdown or build-up in units under construction, or a July completions print far from 1.4M. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,380,507 | ['p18'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 1,398,075 | ['p18', 'p30', 'p35'] / ['a2'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 1,347,099 | ['p19', 'p74', 'p75'] / ['a3', 'a4'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 1,386,168 | ['p16'] / ['a5'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **1,377,831** housing unit/year, 80% interval [768,497, 2,470,303] housing unit/year, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The estimate for the seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026 is 1,377,831 housing unit/year (80% model-based interval 768,497 to 2,470,303 housing unit/year). This covers all private single-family and multifamily units, national total, SAAR.

The anchor is June 2026 private starts of 1,427,000 housing units at seasonally adjusted annual rate, carried forward by a two-month change factor (0.97, range 0.6846 to 1.369). Supporting routes adjust that anchor for the mortgage-rate rise from 6.49% to 6.66% (0.5), build single-family starts from June new sales of 628,000 houses per year using the March 2024 total/SF split (1,321,000 housing units at seasonally adjusted annual rate, 1,022,000 housing units at seasonally adjusted annual rate) with ratios 1.5 and 1.15, and cross-check against June completions of 1,392,000 housing units at seasonally adjusted annual rate via 1. Only the observed points are data; the ratios are analyst assumptions. The four methods were combined with equal weights (25%, 25%, 25%, 25%); no backtest errors were available.

The main risk is that the June anchor is preliminary and may be revised, and August shocks are unobserved. The interval reflects input uncertainty only. A July revision and August permit data would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August-to-June private starts ratio: 0.97 ratio, range 0.6846 to 1.369 (range widened by code); used by m1. Overturned by: A July 2026 starts print far from [n]M or evidence of a large August shock.
- a2 mortgage-rate pass-through to private starts: 0.5 ratio, range 0.1 to 1.5; used by m2. Overturned by: Evidence that starts are insensitive to mortgage rates or that a much larger August rate move dominates.
- a3 single-family private starts per new single-family home sold: 1.5 ratio, range 1.039 to 2.078 (range widened by code); used by m3. Overturned by: A Census SF/MF starts split showing SF starts per sale outside [n]-[n] or a sharp inventory correction.
- a4 total-to-single-family starts ratio adjustment, 2026 vs March 2024: 1.15 ratio, range 0.8078 to 1.616 (range widened by code); used by m3. Overturned by: Current SF/MF split showing multifamily share near the 2024 [n] level or far above one-third.
- a5 August private starts to June private completions ratio: 1 ratio, range 0.704 to 1.408 (range widened by code); used by m4. Overturned by: Evidence of a large drawdown or build-up in units under construction, or a July completions print far from [n]M.

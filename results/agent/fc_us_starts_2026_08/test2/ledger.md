# Evidence ledger: fc_us_starts_2026_08

- Question: Assume today is 2026-08-17. You know nothing published after this date. Estimate the seasonally adjusted annual rate of privately-owned housing starts in the United States in August 2026 (the number of housing units at an annual rate, as in '1,300,000'), as it will be first reported in the U.S. Census Bureau and HUD Monthly New Residential Construction release.
- as_of: 2026-08-17
- Pinned target: Seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026, as first reported in the Census Bureau/HUD Monthly New Residential Construction release (units started during the month, expressed at an annual rate) | unit housing units at annual rate | period 2026-08-01..2026-08-31 | publisher U.S. Census Bureau and U.S. Department of Housing and Urban Development (HUD)

- Official value (scoring only, never shown to the agent): 1,275,000

## Directions and pages

### d1 [own_history] Census Bureau time series

Hypothesis: Recent monthly private housing starts SAAR (through June/July 2026) plus seasonal and trend patterns anchor a short-horizon forecast; August typically shows a modest seasonal-adjustment-neutral move from July.

Queries issued by the searcher: Census Bureau new residential construction housing starts July 2026; privately owned housing starts seasonally adjusted annual rate June 2026; FRED HOUST Housing Starts Total New Privately Owned Housing Units Started monthly 2024 2025 2026 data; Census Bureau new residential construction historical data table housing starts single-family 5 units or more 2024 2025

- `https://macrotrends.net/1314/housing-starts-historical-chart` -> **snapshot** (snapshot 20260806015323); points raw/verified 0/0
- `https://bankingjournal.aba.com/2026/07/housing-starts-increased-19-in-june/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.advisorperspectives.com/dshort/updates/2026/07/17/housing-starts-june-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/data/HOUST` -> **snapshot** (snapshot 20260117043121); points raw/verified 15/0
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 15)

### d2 [related_series] Building permits as leading indicator

Hypothesis: Permits precede starts; the permit-to-start ratio is fairly stable over 1-3 months, so recent permit levels (especially single-family) constrain August starts.

Queries issued by the searcher: Census building permits June 2026 seasonally adjusted annual rate; single-family building permits 2026 monthly trend Census HUD; permits to housing starts ratio historical average Census single-family; "housing starts" July 2026 SAAR forecast August 2026 NAHB

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/8
  - p1 Total building permits SAAR, United States, June 2026 (preliminary) = **1,367,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing units authorized by building permits in June were at a seasonally adjusted annual rate of 1,367,000."
  - p2 Single-family building permits SAAR, United States, June 2026 = **871,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p3 Total building permits SAAR, United States, May 2026 (revised) = **1,410,000** housing units at annual rate (2026-05-01..2026-05-31) [keep: ] quote: "This is 3.0 percent below the revised May rate of 1,410,000 and is 2.3 percent below the June 2025 rate of 1,399,000."
  - p4 Single-family building permits SAAR, United States, May 2026 (revised) = **892,000** housing units at annual rate (2026-05-01..2026-05-31) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p5 Total housing starts SAAR, United States, June 2026 (preliminary) = **1,427,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p6 Single-family housing starts SAAR, United States, June 2026 = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Single-family housing starts in June were at a rate of 895,000; this is 0.2 percent (±10.2 percent)* below the revised May figure of 897,000."
  - p7 Total housing starts SAAR, United States, May 2026 (revised) = **1,199,000** housing units at annual rate (2026-05-01..2026-05-31) [keep: ] quote: "This is 19.0 percent (±15.9 percent) above the revised May estimate of 1,199,000 and is 3.5 percent (±14.3 percent)* above the June 2025 rate of 1,379,000."
  - p8 Single-family housing starts SAAR, United States, May 2026 (revised) = **897,000** housing units at annual rate (2026-05-01..2026-05-31) [keep: ] quote: "Single-family housing starts in June were at a rate of 895,000; this is 0.2 percent (±10.2 percent)* below the revised May figure of 897,000."
- `https://www.census.gov/construction/nrc/starts_rates.html` -> **snapshot** (snapshot 20251006233704); points raw/verified 0/0
- `https://ycharts.com/indicators/us_building_permits` -> **snapshot** (snapshot 20230524130245); points raw/verified 15/3
  - p9 US Building Permits SAAR, trough March 2009 = **513,000** building permits at annual rate (2009-03-01..2009-03-31) [DISCARD: 2009 trough is far outside the relevant horizon and adds no usable signal for August 2026.] quote: "reaching a trough on March 2009 of 513,000 building permits"
  - p10 US Building Permits month-over-month change, April 2023 = **-1.46** % (2023-04-01..2023-04-30) [DISCARD: April 2023 permit MoM change is stale and not applicable to August 2026 level.] quote: "\| Change from Last Month \| -1.46% \|"
  - p11 US Building Permits year-over-year change, April 2023 = **-21.11** % (2023-04-01..2023-04-30) [DISCARD: April 2023 permit YoY change is stale and not applicable.] quote: "\| Change from 1 Year Ago \| -21.11% \|"
- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 19 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word 'thousand' not supported by quote or table header: 5; scale word 'million' not supported by quote or table header: 11; period_end missing or unparseable: 1)

### d3 [forecasts_markets] Professional forecasters and nowcasts

Hypothesis: Published forecasts or nowcasts for August 2026 housing starts (or Q3 2026) provide a direct anchor; treat as forecast, not observation.

Queries issued by the searcher: housing starts forecast August 2026; Fannie Mae housing starts forecast 2026 Housing Forecast; Fannie Mae Housing Forecast August 2026 total housing starts 2026 2027 quarterly; NAHB Wells Fargo Housing Market Index August 2026 builder sentiment

- `https://yieldpro.com/2026/06/more-multifamily-starts-predicted-in-june-forecast/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fanniemae.com/media/document/pdf/housing-forecast-082026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yieldpro.com/2026/05/multifamily-starts-forecasts-mostly-lower-in-may/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://theclose.com/news-2026-us-housing-market-outlook-balanced-not-equal/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Completions and under-construction stock

Hypothesis: Units under construction and completions reflect the pipeline; a large under-construction backlog with declining completions implies starts momentum, while a shrinking pipeline implies weakness.

Queries issued by the searcher: housing units under construction 2026 Census new residential construction; housing completions SAAR June 2026 Census HUD; FRED UNDCONS New Privately-Owned Housing Units Under Construction Total 2026 values; "under construction" housing units June 2026 "1.26 million" single-family multifamily NAHB Eye on Housing

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 0/0
- `https://fred.stlouisfed.org/release/tables?rid=27&eid=20948` -> **snapshot** (snapshot 20260612230614); points raw/verified 15/0
- `https://www.sbcacomponents.com/media/multifamily-starts-surge-in-june-as-single-family-drops` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ycharts.com/indicators/us_housing_completed` -> **snapshot** (snapshot 20240223005220) **LEAK SENTINEL HIT ['(?<![\\d.,])1\\.39M(?!\\d|[.,]\\d)(?![A-Za-z])'] (excluded)**; points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 15)

### d5 [shocks] Mortgage rates and macro conditions

Hypothesis: Mortgage rates, Fed policy, and builder sentiment drive single-family starts with a lag; a rate environment shift in mid-2026 changes the August level.

Queries issued by the searcher: 30-year mortgage rate July 2026; NAHB housing market index July 2026; housing starts June 2026 Census Bureau annual rate single-family; housing starts July 2026 report August 2026 release

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/7
  - p12 Privately-owned housing starts, United States, June 2026, seasonally adjusted an = **1,427,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p5/p36 (same June 2026 total starts value).] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p13 Single-family housing starts, United States, June 2026, seasonally adjusted annu = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p6/p34 (same June 2026 single-family starts value).] quote: "Single-family housing starts in June were at a rate of 895,000"
  - p14 Housing starts in buildings with five units or more, United States, June 2026, s = **513,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "The June rate for units in buildings with five units or more was 513,000."
  - p15 Privately-owned housing starts, United States, May 2026 (revised), seasonally ad = **1,199,000** housing units at annual rate (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p7/p37 (same May 2026 total starts value).] quote: "above the revised May estimate of 1,199,000"
  - p16 Privately-owned housing starts, United States, June 2025, seasonally adjusted an = **1,379,000** housing units at annual rate (2025-06-01..2025-06-30) [keep: ] quote: "above the June 2025 rate of 1,379,000"
  - p17 Privately-owned housing units authorized by building permits, United States, Jun = **1,367,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1/p40 (same June 2026 total permits value).] quote: "Privately-owned housing units authorized by building permits in June were at a seasonally adjusted annual rate of 1,367,000."
  - p18 Single-family building permit authorizations, United States, June 2026, seasonal = **871,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2/p38 (same June 2026 single-family permits value).] quote: "Single-family authorizations in June were at a rate of 871,000"
- `https://www.freddiemac.com/pmms/archive` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.housingwire.com/articles/builder-confidence-dips-again-in-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fa-mag.com/news/mortgage-rates-rise-to-6-66---highest-level-in-a-year-87934.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (scale word 'thousand' not supported by quote or table header: 6; period_end missing or unparseable: 2)

### d6 [related_series] Regional and multifamily detail

Hypothesis: Multifamily (5+ unit) starts are volatile and regionally concentrated; separating single-family (stable) from multifamily (lumpy) improves the forecast, since August multifamily could swing the total.

Queries issued by the searcher: multifamily housing starts 2026 Census Bureau new residential construction; housing starts by region 2026 Northeast Midwest South West multifamily; Eye on Housing housing starts June 2026 multifamily 513,000 regional year-to-date; Fannie Mae July 2026 housing forecast multifamily starts 441,000 2026

- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sbcacomponents.com/media/multifamily-starts-surge-in-june-as-single-family-drops` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kpmg.com/us/en/articles/2026/june-2026-housing-starts.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/housing-starts/news/567898` -> **snapshot** (snapshot 20260804063649); points raw/verified 15/15
  - p19 Total US housing starts, seasonally adjusted annualized rate, June 2026 = **1,427,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p5/p36 (same June 2026 total starts value).] quote: "Housing starts in the US jumped 19% to a seasonally adjusted annualized rate of 1427 thousand units in June 2026, the highest in three months"
  - p20 Forecast for total US housing starts, seasonally adjusted annualized rate, June  = **1,310,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "compared to forecasts of 1310 thousand"
  - p21 Month-over-month change in total US housing starts, June 2026 = **19** % (2026-06-01..2026-06-30) [keep: ] quote: "Housing starts in the US jumped 19% to a seasonally adjusted annualized rate of 1427 thousand units in June 2026"
  - p22 Month-over-month change in total US housing starts, May 2026 (revised) = **15.4** % (2026-05-01..2026-05-31) [keep: ] quote: "It follows a revised 15.4% jump in May that sent housing starts to a six-year low."
  - p23 Multifamily (5+ unit) housing starts, seasonally adjusted annualized rate, June  = **513,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p14 (same June 2026 5+ unit starts value).] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p24 Month-over-month change in multifamily housing starts, June 2026 = **76.3** % (2026-06-01..2026-06-30) [keep: ] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p25 Month-over-month change in multifamily housing starts, May 2026 = **41** % (2026-05-01..2026-05-31) [keep: ] quote: "Multi-family starts soared 76.3% to 513 thousand, following a 41% plunge in the previous month."
  - p26 Single-family housing starts, seasonally adjusted annualized rate, June 2026 = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p6/p34 (same June 2026 single-family starts value).] quote: "Meanwhile, single-family starts edged down 0.2% to 895 thousand, a third consecutive month of falls"
  - p27 Month-over-month change in single-family housing starts, June 2026 = **0.2** % (2026-06-01..2026-06-30) [keep: ] quote: "Meanwhile, single-family starts edged down 0.2% to 895 thousand, a third consecutive month of falls"
  - p28 Housing starts in the South region, seasonally adjusted annualized rate, June 20 = **741,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Starts soared in all four main regions: the South (15.2% to 741 thousand)"
  - p29 Month-over-month change in housing starts, South region, June 2026 = **15.2** % (2026-06-01..2026-06-30) [keep: ] quote: "the South (15.2% to 741 thousand)"
  - p30 Housing starts in the Midwest region, seasonally adjusted annualized rate, June  = **248,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "the Midwest (33.3% to 248 thousand, the highest since 2024)"
  - p31 Month-over-month change in housing starts, Midwest region, June 2026 = **33.3** % (2026-06-01..2026-06-30) [keep: ] quote: "the Midwest (33.3% to 248 thousand, the highest since 2024)"
  - p32 Housing starts in the Northeast region, seasonally adjusted annualized rate, Jun = **129,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "the Northeast (10.3% to 129 thousand)"
  - p33 Housing starts in the West region, seasonally adjusted annualized rate, June 202 = **309,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "and the West (22.1% to 309 thousand)"

### d7 [base_rates] Seasonal adjustment factors

Hypothesis: August unadjusted starts and the Census seasonal factors determine the SAAR; knowing the typical August seasonal factor and unadjusted August level helps translate any unadjusted signal.

Queries issued by the searcher: Census housing starts seasonal adjustment factors by month; housing starts unadjusted August seasonal factor Census New Residential Construction; census.gov construction nrc seasonal adjustment tables housing starts seasonal factors 2026; "new residential construction" August 2025 housing starts unadjusted 1, seasonally adjusted annual rate census

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/0
- `https://www.census.gov/prod/3/98pubs/c20-9808.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fraser.stlouisfed.org/files/docs/publications/BusConD/pages/1965-1969/2031_1965-1969.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://api.fxmacrodata.com/v1/announcements/usd/housing_starts` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 12; value_as_written not in quote as a whole number: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b1 [own_history] Census New Residential Construction historical series

Hypothesis: A full monthly SAAR history of private starts (and SF vs 5+ split) through July 2026 would let series_naive and permit-to-start ratio methods be backtested and would anchor the August level; currently only May/June 2026 are available, so trend and seasonal context are thin.

Queries issued by the searcher: FRED HOUST housing starts monthly SAAR historical data 2025 2026; Census New Residential Construction historical table private housing starts seasonally adjusted annual rate; fred.stlouisfed.org/data/HOUST1F table data New Privately-Owned Housing Units Started Single-Family; "New Residential Construction" June 2026 housing starts seasonally adjusted annual rate 1,415,000 press release July 2026

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])1,415,000(?!\\d|[.,]\\d)']; no pages fetched**


### b2 [related_series] Permit-to-start conversion

Hypothesis: A stable historical ratio of starts to permits (total and single-family) would convert the June 2026 permit levels (p1, p2) into an August starts estimate; this is the most direct structural route and currently lacks a calibrated ratio.

Queries issued by the searcher: Census Bureau New Residential Construction historical table permits and housing starts 2023-2026 monthly; FRED HOUST Housing Starts Total New Privately-Owned Housing Units Started monthly seasonally adjusted annual rate 2026; fred.stlouisfed.org/data/PERMIT "New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units" table data 2026; census.gov construction nrc historical data "Housing Units Authorized by Building Permits" "Housing Starts" monthly seasonally adjusted table 2023 2024 2025

- `https://www.census.gov/construction/nrc/starts_rates.html` -> **snapshot** (snapshot 20251006233704); points raw/verified 0/0
- `https://fred.stlouisfed.org/data/HOUST` -> **snapshot** (snapshot 20260117043121); points raw/verified 15/0
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0
- `https://www.macrotrends.net/3098/new-housing-unit-permits` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 15)

### b3 [shocks] Mortgage rates and builder sentiment mid-2026

Hypothesis: A mid-2026 shift in 30-year mortgage rates or NAHB builder sentiment would shift single-family starts with a 1–3 month lag, materially changing the August level; without it the forecast relies on June momentum alone.

Queries issued by the searcher: Freddie Mac Primary Mortgage Market Survey 30-year fixed rate July 2026; NAHB Wells Fargo Housing Market Index July 2026; Census Bureau housing starts June 2026 seasonally adjusted annual rate release July 2026; Freddie Mac mortgage rates August 13 2026 30-year fixed

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 14/7
  - p34 US single-family housing starts, seasonally adjusted annual rate, June 2026 (pre = **895,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Single-family housing starts in June were at a rate of 895,000; this is 0.2 percent (±10.2 percent)* below the revised May figure of 897,000."
  - p35 US single-family housing starts, seasonally adjusted annual rate, May 2026 (revi = **897,000** housing units at annual rate (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p8 (same May 2026 single-family starts value).] quote: "Single-family housing starts in June were at a rate of 895,000; this is 0.2 percent (±10.2 percent)* below the revised May figure of 897,000."
  - p36 US total privately-owned housing starts, seasonally adjusted annual rate, June 2 = **1,427,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p37 US total privately-owned housing starts, seasonally adjusted annual rate, May 20 = **1,199,000** housing units at annual rate (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p7/p15 (same May 2026 total starts value).] quote: "This is 19.0 percent (±15.9 percent) above the revised May estimate of 1,199,000"
  - p38 US single-family building permits, seasonally adjusted annual rate, June 2026 = **871,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p39 US single-family building permits, seasonally adjusted annual rate, May 2026 (re = **892,000** housing units at annual rate (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p4 (same May 2026 single-family permits value).] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p40 US total building permits, seasonally adjusted annual rate, June 2026 = **1,367,000** housing units at annual rate (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing units authorized by building permits in June were at a seasonally adjusted annual rate of 1,367,000."
- `https://freddiemac.gcs-web.com/` -> **snapshot** (snapshot 20260721054614); points raw/verified 8/8
  - p41 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of July = **6.55** % (2026-07-16..2026-07-16) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.55%."
  - p42 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of July = **6.49** % (2026-07-09..2026-07-09) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.49%."
  - p43 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of July = **6.43** % (2026-07-02..2026-07-02) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.43%."
  - p44 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of June = **6.49** % (2026-06-25..2026-06-25) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.49%."
  - p45 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of June = **6.47** % (2026-06-18..2026-06-18) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.47%."
  - p46 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of June = **6.52** % (2026-06-11..2026-06-11) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.52%."
  - p47 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of June = **6.48** % (2026-06-04..2026-06-04) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.48%."
  - p48 30-year fixed-rate mortgage (FRM) weekly average, Freddie Mac PMMS, week of May  = **6.53** % (2026-05-28..2026-05-28) [keep: ] quote: "showing the 30-year fixed-rate mortgage (FRM) averaged 6.53%."
- `https://www.housingwire.com/articles/builder-confidence-dips-again-in-july/` -> **snapshot** (snapshot 20260803112655); points raw/verified 15/15
  - p49 NAHB/Wells Fargo Housing Market Index (HMI) reading, July = **34** index points (2026-07-01..2026-07-31) [keep: ] quote: "homebuilder confidence in July fell 2 points to a reading of 34"
  - p50 Change in NAHB/Wells Fargo HMI, July vs prior month = **2** index points (2026-07-01..2026-07-31) [keep: ] quote: "homebuilder confidence in July fell 2 points to a reading of 34"
  - p51 Consecutive months with HMI reading below 40, through July = **15** months (2026-07-01..2026-07-31) [keep: ] quote: "marking the 15th consecutive month with a reading below 40"
  - p52 HMI present sales component reading, July = **37** index points (2026-07-01..2026-07-31) [keep: ] quote: "negative reading on present sales (37), traffic of prospective buyers (23) and the outlook for the next six months (43)"
  - p53 HMI traffic of prospective buyers component reading, July = **23** index points (2026-07-01..2026-07-31) [keep: ] quote: "negative reading on present sales (37), traffic of prospective buyers (23) and the outlook for the next six months (43)"
  - p54 HMI outlook for next six months component reading, July = **43** index points (2026-07-01..2026-07-31) [keep: ] quote: "negative reading on present sales (37), traffic of prospective buyers (23) and the outlook for the next six months (43)"
  - p55 Share of builders reporting price cuts, July = **37** % (2026-07-01..2026-07-31) [keep: ] quote: "In July, 37% of builders reported price cuts, an increase from 35% in June."
  - p56 Share of builders reporting price cuts, June = **35** % (2026-06-01..2026-06-30) [keep: ] quote: "In July, 37% of builders reported price cuts, an increase from 35% in June."
  - p57 Average price reduction among builders, July = **6** % (2026-07-01..2026-07-31) [keep: ] quote: "The average price reduction held steady at 6%"
  - p58 Share of builders reporting use of sales incentives, July = **63** % (2026-07-01..2026-07-31) [keep: ] quote: "the share of builders that reported using sales incentives ticked up slightly to 63%"
  - p59 Consecutive months incentive share at 60% or higher, through July = **16** months (2026-07-01..2026-07-31) [keep: ] quote: "representing the 16th consecutive month this share has reached 60% or higher"
  - p60 Share of builders reporting higher year-over-year sales, June (BTIG/HomeSphere s = **35** % (2026-06-01..2026-06-30) [keep: ] quote: "only 35% of builders reported higher year-over-year sales, while 27% reported lower year-over-year sales"
  - p61 Share of builders reporting lower year-over-year sales, June (BTIG/HomeSphere su = **27** % (2026-06-01..2026-06-30) [keep: ] quote: "only 35% of builders reported higher year-over-year sales, while 27% reported lower year-over-year sales"
  - p62 Share of builders reporting higher year-over-year traffic, June (BTIG/HomeSphere = **38** % (2026-06-01..2026-06-30) [keep: ] quote: "In June, 38% of builders reported higher year-over-year traffic, nearly doubling the 20% who reported higher traffic in May"
  - p63 Share of builders reporting higher year-over-year traffic, May (BTIG/HomeSphere  = **20** % (2026-05-01..2026-05-31) [keep: ] quote: "nearly doubling the 20% who reported higher traffic in May and nearing February's recent high of 43%"
- `https://www.investing.com/analysis/housing-starts-jumped-19-but-the-singlefamily-pipeline-barely-moved-200684563` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (scale word 'thousand' not supported by quote or table header: 6; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['housing starts', 'us housing', 'new construction']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p5', 'p12', 'p19'] Same June 2026 total private starts SAAR (1,427,000) reported by Census and echoed by TradingEconomics; one underlying measurement, not independent confirmation.
- corroborating: ['p6', 'p13', 'p26'] Same June 2026 single-family starts (895,000) from Census and TradingEconomics; shared source.
- corroborating: ['p14', 'p23'] Same June 2026 5+ unit starts (513,000); shared Census origin.
- corroborating: ['p1', 'p17'] Same June 2026 total permits (1,367,000); duplicate of one measurement.
- corroborating: ['p2', 'p18'] Same June 2026 single-family permits (871,000); duplicate.
- corroborating: ['p3', 'p4', 'p7', 'p8', 'p15'] Revised May 2026 values: total permits 1,410,000, SF permits 892,000, total starts 1,199,000, SF starts 897,000. Consistent internally and with June figures.
- corroborating: ['p5', 'p7'] June total starts 1,427,000 vs revised May 1,199,000 implies ~19% MoM, matching p21; internally consistent.
- corroborating: ['p14', 'p24', 'p25'] Multifamily 513,000 after +76.3% following -41% is arithmetically consistent with a very low May multifamily base; confirms multifamily volatility.
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33'] Regional June starts sum to 741+248+129+309 = 1,427 thousand, matching total; regional detail is consistent but shares the same source.
- contextual: ['p9', 'p10', 'p11'] 2009 trough and 2023 permit changes are historical context only; not directly usable for August 2026 level.
- contextual: ['p20'] June 2026 forecast of 1,310,000 vs actual 1,427,000 shows forecast error magnitude (~9%), useful for uncertainty calibration but not a level input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p5', 'p36', 'p12', 'p19'] All are the same June 2026 total private starts SAAR (1,427,000) from the same Census/HUD release; p12 and p19 are redundant copies of p5/p36 and add no independent information.
- corroborating: ['p6', 'p34', 'p13', 'p26'] Same June 2026 single-family starts SAAR (895,000) from the same release; p13/p26 are redundant duplicates.
- corroborating: ['p1', 'p40', 'p17'] Same June 2026 total permits SAAR (1,367,000) from the same release; p17 is a duplicate.
- corroborating: ['p2', 'p38', 'p18'] Same June 2026 single-family permits SAAR (871,000); p18 is a duplicate.
- corroborating: ['p3', 'p4', 'p39'] May 2026 revised permits: total 1,410,000 and single-family 892,000; p39 duplicates p4.
- corroborating: ['p7', 'p15', 'p37'] May 2026 revised total starts 1,199,000; p15/p37 duplicate p7. The quoted 19.0% MoM in p7 is the June-over-May change, not a May change.
- corroborating: ['p8', 'p35'] May 2026 revised single-family starts 897,000; p35 duplicates p8.
- corroborating: ['p5', 'p6', 'p14'] June total 1,427,000 decomposes into single-family 895,000 plus 5+ unit 513,000 plus a small 2-4 unit residual (~19,000); internally consistent.
- corroborating: ['p21', 'p22', 'p24', 'p25', 'p27'] Trading Economics MoM changes are consistent with the Census levels: June total +19%, May +15.4% off a six-year low, multifamily +76.3% after -41%, single-family -0.2% (third consecutive decline). Sam
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33'] Regional June starts sum to ~1,427,000 (South 741k, Midwest 248k, Northeast 129k, West 309k), consistent with the national total; regional detail shows the June jump was broad but led by multifamily-h
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] Freddie Mac PMMS 30-year rate hovered 6.43-6.55% through June-July 2026, drifting slightly up into mid-July; a stable, elevated rate environment, not a sharp mid-2026 shift.
- corroborating: ['p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63'] NAHB HMI at 34 in July (down 2, 15th month below 40), weak present sales/traffic, rising price cuts and incentives, and mixed builder sales/traffic surveys all point to subdued single-family demand mo
- conflicting: ['p20', 'p5'] The Trading Economics forecast of 1,310,000 for June was far below the actual 1,427,000; this forecast is a forecast, not an observation, and shows forecast error magnitude for this series.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 total starts relative to June 2026 level | 0.95 | 0.78..1.15 | 0.6697..1.339 (widened) | ratio | m1 (m1) | June's 1,427,000 was inflated by a 76.3% multifamily surge off a six-year low; July/August typically give back part of such a spike. Weak HMI (34, 15th month below 40), rising price cuts/incentives, and slightly higher mortgage rates (6.55% mid-July vs 6.43% early July) argue for modest softening, b | August 2026 starts are driven by the same demand/pipeline conditions as June-July 2026 with no major rate or policy shock. | A sharp mortgage-rate move or a large multifamily permit surge/plunge between July and August 2026. |
| a2 | August 2026 single-family starts relative to June 2026 level | 0.97 | 0.85..1.1 | 0.6837..1.367 (widened) | ratio | m2 (m2) | Single-family starts have fallen three consecutive months to 895k; single-family permits (871k) are below starts, implying mild further softening. Weak builder sentiment and traffic support a small decline, but the level is already low and rates are stable, so a modest factor near 0.97. | Single-family demand and permit flow continue the June-July 2026 trajectory. | A rebound in single-family permits or a sharp drop in mortgage rates before August 2026. |
| a3 | August 2026 multifamily (5+) starts relative to June 2026 level | 0.7 | 0.4..1.2 | 0.4..1.2 | ratio | m2 (m2) | June's 513k multifamily figure followed a 76.3% surge after a 41% plunge in May; such swings mean-revert. Multifamily is lumpy and regionally concentrated, so a partial give-back toward the recent average is expected, with a very wide range. | No new large multifamily project starts cluster in August 2026. | Evidence of a large multifamily permit/start cluster in August 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,352,220 | ['p5'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 1,257,238 | ['p6', 'p14'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of single_family, multifamily_5plus, other_2to4

Result: central **1,303,864** unit/year, 80% interval [878,781, 1,934,568] unit/year, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for the seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026 is 1,303,864 unit/year (80% model-based interval 878,781 to 1,934,568 unit/year). This targets units started during August 2026, first reported around mid-September 2026.

Two methods were combined at equal weight (50% and 50%). Method [n] anchors on total starts of 1,427,000 housing units at annual rate and applies a change factor of 0.95 (range 0.6697 to 1.339). Method [n] splits single-family starts of 895,000 housing units at annual rate and [n]+ unit starts of 513,000 housing units at annual rate, applying factors of 0.97 (range 0.6837 to 1.367) and 0.7 (range 0.4 to 1.2).

The June observations are observed; all August factors are analyst assumptions, not data. The interval reflects input uncertainty only, not demonstrated accuracy. The main risk is an unobserved July/August multifamily swing, since that component is lumpy. July data and August permits would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 total starts relative to June 2026 level: 0.95 ratio, range 0.6697 to 1.339 (range widened by code); used by m1. Overturned by: A sharp mortgage-rate move or a large multifamily permit surge/plunge between July and August 2026.
- a2 August 2026 single-family starts relative to June 2026 level: 0.97 ratio, range 0.6837 to 1.367 (range widened by code); used by m2. Overturned by: A rebound in single-family permits or a sharp drop in mortgage rates before August 2026.
- a3 August 2026 multifamily ([n]+) starts relative to June 2026 level: 0.7 ratio, range 0.4 to 1.2; used by m2. Overturned by: Evidence of a large multifamily permit/start cluster in August 2026.

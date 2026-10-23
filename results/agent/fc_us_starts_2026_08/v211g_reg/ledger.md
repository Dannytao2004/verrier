# Evidence ledger: fc_us_starts_2026_08

- Question: Assume today is 2026-08-17. You know nothing published after this date. Estimate the seasonally adjusted annual rate of privately-owned housing starts in the United States in August 2026 (the number of housing units at an annual rate, as in '1,300,000'), as it will be first reported in the U.S. Census Bureau and HUD Monthly New Residential Construction release.
- as_of: 2026-08-17
- Pinned target: Seasonally adjusted annual rate of privately-owned housing starts (new privately-owned housing units started) in the United States, as first reported by the U.S. Census Bureau and HUD in the Monthly New Residential Construction release for August 2026 | unit housing units at annual rate (SAAR) | period 2026-08-01..2026-08-31 | publisher U.S. Census Bureau and U.S. Department of Housing and Urban Development (HUD), Monthly New Residential Construction (joint release)

- Official value (scoring only, never shown to the agent): 1,275,000

## Directions and pages

### d1 [own_history] Census Bureau time series

Hypothesis: Recent monthly SAAR prints (through July 2026, published before cutoff) plus seasonal factors and month-to-month momentum anchor a short-horizon forecast of the August 2026 SAAR; August typically shows a modest seasonal-adjustment-neutral pattern relative to July.

Queries issued by the searcher: Census Bureau new residential construction housing starts July 2026; privately owned housing starts seasonally adjusted annual rate historical table 2025 2026; "newresconst" PDF June 2026 housing starts "FOR RELEASE" July 17 2026; Census housing starts seasonal factors not seasonally adjusted August table 3b new residential construction

- `https://www.census.gov/construction/nrc/pdf/newresconst_202606.pdf` -> **snapshot** (snapshot 20260720224510); points raw/verified 15/2
  - p1 Privately-owned housing starts SAAR, United States, June 2026 (preliminary) = **1,427,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p2 Privately-owned housing starts SAAR, United States, May 2026 (revised) = **1,199,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "above the revised May estimate of 1,199,000"
- `https://www.economx.hu/documents/549/newresconst.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.redbooklumberdata.com/2026/07/17/u-s-census-bureau-monthly-new-residential-consctruction-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=667071&year=2026&cty=US` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (scale word 'thousand' not supported by quote or table header: 9; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4)

### d2 [related_series] Census building permits

Hypothesis: Building permits (especially single-family authorizations) lead starts by roughly one to two months; the July 2026 permit SAAR and single-family permit trend constrain the August starts level, since starts cannot persistently exceed authorized pipeline.

Queries issued by the searcher: building permits July 2026 Census single-family housing permits SAAR; Census monthly new residential construction July 2026 building permits housing starts; "June 2026" building permits SAAR single-family authorizations Census new residential construction July release; housing permits June 2026 housing starts June 2026 Census report released July 2026

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/10
  - p3 US total building permits SAAR, June 2026 (preliminary) = **1,367,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing units authorized by building permits in June were at a seasonally adjusted annual rate of 1,367,000."
  - p4 US single-family building permits SAAR, June 2026 = **871,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p5 US total building permits SAAR, May 2026 (revised) = **1,410,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "This is 3.0 percent below the revised May rate of 1,410,000 and is 2.3 percent below the June 2025 rate of 1,399,000."
  - p6 US single-family building permits SAAR, May 2026 (revised) = **892,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000; this is 2.4 percent below the revised May figure of 892,000."
  - p7 US building permits SAAR, 5+ unit buildings, June 2026 = **445,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Authorizations of units in buildings with five units or more were at a rate of 445,000 in June."
  - p8 US total building permits SAAR, June 2025 = **1,399,000** housing units at annual rate (SAAR) (2025-06-01..2025-06-30) [keep: ] quote: "and is 2.3 percent below the June 2025 rate of 1,399,000."
  - p9 US total housing starts SAAR, June 2026 (preliminary) = **1,427,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p10 US single-family housing starts SAAR, June 2026 = **895,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Single-family housing starts in June were at a rate of 895,000; this is 0.2 percent (±10.2 percent)* below the revised May figure of 897,000."
  - p11 US total housing starts SAAR, May 2026 (revised) = **1,199,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "This is 19.0 percent (±15.9 percent) above the revised May estimate of 1,199,000"
  - p12 Average revision to preliminary seasonally adjusted permits/starts/completions e = **2.9** % (not stated (page dated 2026-07-15)) [keep: ] quote: "On average, the preliminary seasonally adjusted estimates of total building permits, housing starts and housing completions are revised 2.9 percent or less."
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0
- `https://wiplash.ai/preston_basis/posts/2LvpmVGXR0OYcD-PShr8nQ` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; scale word 'thousand' not supported by quote or table header: 1)

### d3 [forecasts_markets] Professional forecasters and nowcasts

Hypothesis: Published forecasts or nowcasts of August 2026 housing starts (e.g., from banks, Fannie Mae, MBA, or consensus panels) made before cutoff provide a direct anchor, though they may share underlying data sources.

Queries issued by the searcher: housing starts forecast August 2026 SAAR; Fannie Mae housing starts forecast 2026 Housing Forecast; yieldpro multifamily starts forecast August 2026 Fannie Mae; "Housing Forecast" Fannie Mae August 2026 total housing starts 2026 2027

- `https://cmegroup.econoday.com/byevent?fid=667073&year=2026&cty=US&ctyall=10738893&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yieldpro.com/2026/06/more-multifamily-starts-predicted-in-june-forecast/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newslink.mba.org/cmf-newslinks/2026/september/mba-newslink-thursday-apr-14-2021/chart-of-the-week-new-residential-construction/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/housing-starts` -> **snapshot** (snapshot 20260816062649) **LEAK SENTINEL HIT ['(?<![\\d.,])1\\.31M(?!\\d|[.,]\\d)(?![A-Za-z])'] (excluded)**; points raw/verified -/-

### d4 [related_series] Census housing completions and under-construction stock

Hypothesis: Units under construction and completions reflect the pipeline; a large under-construction backlog supports continued starts, while a shrinking backlog signals deceleration. Completions and under-construction stock bracket plausible starts.

Queries issued by the searcher: housing units under construction 2026 Census residential construction; housing completions SAAR 2026 Census Monthly New Residential Construction; "MONTHLY NEW RESIDENTIAL CONSTRUCTION, JUNE 2026" Census release July 17 2026 units under construction; FRED New Privately-Owned Housing Units Under Construction total UNDCONS 2026

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/1
  - p13 Average revision to preliminary seasonally adjusted estimates of permits, starts = **1.9** percent (not stated (page dated 2024-04-12)) [keep: ] quote: "On average, the preliminary seasonally adjusted estimates of total building permits, housing starts and housing completions are revised 1.9 percent or less."
- `https://www.investing.com/analysis/us-housing-data-show-why-the-construction-recovery-looks-uneven-200684160` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sbcacomponents.com/media/multifamily-starts-surge-in-june-as-single-family-drops` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://develop.housingwire.com/articles/housing-starts-accelerated-in-march-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'thousand' not supported by quote or table header: 9; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; value_as_written not in quote as a whole number: 4)

### d5 [related_series] NAHB / builder sentiment and single-family market

Hypothesis: NAHB/Wells Fargo Housing Market Index and single-family starts move together; a mid-2026 HMI reading and mortgage-rate environment indicate whether single-family starts are trending up or down into August.

Queries issued by the searcher: NAHB housing market index August 2026 builder sentiment; NAHB/Wells Fargo Housing Market Index July 2026; housing starts June 2026 single-family rate Census Bureau; "housing starts" July 2026 single-family annual rate

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/5
  - p14 Privately-owned housing starts, total, SAAR, United States, March 2024 (prelimin = **1,321,000** housing units at annual rate (SAAR) (2024-03-01..2024-03-31) [keep: ] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p15 Single-family housing starts, SAAR, United States, March 2024 (preliminary) = **1,022,000** housing units at annual rate (SAAR) (2024-03-01..2024-03-31) [keep: ] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p16 Single-family housing starts, SAAR, United States, February 2024 (revised) = **1,167,000** housing units at annual rate (SAAR) (2024-02-01..2024-02-29) [keep: ] quote: "this is 12.4 percent (±12.5 percent)* below the revised February figure of 1,167,000"
  - p17 Total housing starts, SAAR, United States, February 2024 (revised) = **1,549,000** housing units at annual rate (SAAR) (2024-02-01..2024-02-29) [keep: ] quote: "This is 14.7 percent (±9.9 percent) below the revised February estimate of 1,549,000"
  - p18 Months needed to establish an underlying trend in total housing starts = **6** as written "six months", value check pending months (not stated (page dated 2024-04-12)) [keep: ] quote: "It may take three months to establish an underlying trend for building permit authorizations, six months for total starts, and six months for total completions."
- `https://www.investing.com/news/economy-news/us-home-builder-sentiment-ticks-up-in-august-but-remains-weak-overall-4863446` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/analysis/housing-starts-jumped-19-but-the-singlefamily-pipeline-barely-moved-200684563` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sbcacomponents.com/media/builder-sentiment-remains-low-on-affordability-concerns` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (scale word 'thousand' not supported by quote or table header: 10)

### d6 [physical_flow] Regional/state building activity

Hypothesis: Starts are the sum of regional activity; Census regional (Northeast, Midwest, South, West) starts data through July 2026 and any state-level permit surges (e.g., South multifamily) can be aggregated and trended to August.

Queries issued by the searcher: Census housing starts by region July 2026; Monthly New Residential Construction July 2026 regional housing starts SAAR; "MONTHLY NEW RESIDENTIAL CONSTRUCTION, JUNE 2026" census pdf housing starts region; state building permits surge 2026 multifamily South Census regional permits June 2026

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/7
  - p19 US total privately-owned housing starts SAAR, March 2024 (preliminary) = **1,321,000** housing units at annual rate (SAAR) (2024-03-01..2024-03-31) [keep: ] quote: "Privately‐owned housing starts in March were at a seasonally adjusted annual rate of 1,321,000."
  - p20 US total privately-owned housing starts SAAR, February 2024 (revised) = **1,549,000** housing units at annual rate (SAAR) (2024-02-01..2024-02-29) [keep: ] quote: "below the revised February estimate of 1,549,000"
  - p21 US total privately-owned housing starts SAAR, March 2023 = **1,380,000** housing units at annual rate (SAAR) (2023-03-01..2023-03-31) [keep: ] quote: "below the March 2023 rate of 1,380,000"
  - p22 US single-family housing starts SAAR, March 2024 = **1,022,000** housing units at annual rate (SAAR) (2024-03-01..2024-03-31) [keep: ] quote: "Single‐family housing starts in March were at a rate of 1,022,000"
  - p23 US single-family housing starts SAAR, February 2024 (revised) = **1,167,000** housing units at annual rate (SAAR) (2024-02-01..2024-02-29) [keep: ] quote: "below the revised February figure of 1,167,000"
  - p24 US housing starts in buildings with five units or more SAAR, March 2024 = **290,000** housing units at annual rate (SAAR) (2024-03-01..2024-03-31) [keep: ] quote: "The March rate for units in buildings with five units or more was 290,000."
  - p25 Average revision to preliminary seasonally adjusted estimates of total building  = **1.9** % (not stated (page dated 2024-04-12)) [keep: ] quote: "On average, the preliminary seasonally adjusted estimates of total building permits, housing starts and housing completions are revised 1.9 percent or less."
- `https://hn24.hnonline.sk/hn24/96292400-vystavba-obytnych-domov-v-usa-v-juni-vzrastla` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://economics.td.com/us-housing-starts-and-permits?linkId=165656202` -> **snapshot** (snapshot 20220518135305); points raw/verified 15/15
  - p26 U.S. total housing starts, April 2022, seasonally adjusted annualized rate = **1,724,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p72 (April 2022 starts); redundant copy.] quote: "U.S. housing starts fell by 0.2% month-on-month (m/m) to 1.724 million units (annualized) in April"
  - p27 Market expectation for U.S. housing starts, April 2022 = **1,766,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p74 (April 2022 market expectation); redundant.] quote: "market expectations which called for a decline to 1.766 million units"
  - p28 Revision to March 2022 U.S. housing starts (level change) = **65,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: Duplicate of p75 (March 2022 revision); redundant.] quote: "Revisions to last month's data lopped 65k units off of March starts"
  - p29 Revision to March 2022 single-family starts (level change) = **-13,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: Duplicate of p76; redundant.] quote: "downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p30 Revision to March 2022 multifamily starts (level change) = **-52,000** housing units at annual rate (2022-03-01..2022-03-31) [DISCARD: Duplicate of p77; redundant.] quote: "downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p31 U.S. multifamily starts, April 2022, month-on-month change (level) = **83,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p79; redundant.] quote: "multifamily starts rose by 15.3% m/m (or 83k)"
  - p32 U.S. single-family starts, April 2022, month-on-month change (level) = **-87,000** housing units at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p81; redundant.] quote: "Single-family starts, however, fell by 7.3% m/m (or -87k)."
  - p33 U.S. total building permits, April 2022, seasonally adjusted annualized rate = **1,819,000** permits at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p82; redundant.] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million."
  - p34 U.S. total building permits, April 2022, month-on-month change (level) = **60,000** permits at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p84; redundant.] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million."
  - p35 U.S. multifamily permits, April 2022, month-on-month change (level) = **7,000** permits at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p85; redundant.] quote: "Multifamily permits fell by 1% (or 7k)"
  - p36 U.S. single-family permits, April 2022, month-on-month change (level) = **-53,000** permits at annual rate (2022-04-01..2022-04-30) [DISCARD: Duplicate of p86; redundant.] quote: "single-family permits fell even further by 4.6% (or -53k)"
  - p37 U.S. housing starts, South region, April 2022, month-on-month percent change = **10.6** % (2022-04-01..2022-04-30) [DISCARD: Regional April 2022 percent change; too old and too aggregated to inform August 2026 level; discarded in round 1.] quote: "Housing starts were up in two of the four regions, rising by 10.6% in the South and 3.3% in the West."
  - p38 U.S. housing starts, West region, April 2022, month-on-month percent change = **3.3** % (2022-04-01..2022-04-30) [DISCARD: Regional April 2022 percent change; too old and not usable for a 2026 level; discarded in round 1.] quote: "rising by 10.6% in the South and 3.3% in the West"
  - p39 U.S. housing starts, Northeast region, April 2022, month-on-month percent change = **23.2** % (2022-04-01..2022-04-30) [DISCARD: Regional April 2022 percent change; too old and not usable for a 2026 level; discarded in round 1.] quote: "Starts fell a more sizeable 23.2% and 22% in the Northeast and Midwest, respectively."
  - p40 U.S. housing starts, Midwest region, April 2022, month-on-month percent change = **22** % (2022-04-01..2022-04-30) [DISCARD: Regional April 2022 percent change; too old and not usable for a 2026 level; discarded in round 1.] quote: "Starts fell a more sizeable 23.2% and 22% in the Northeast and Midwest, respectively."
- `https://www.census.gov/construction/nrc/data/releases.html` -> **snapshot** (snapshot 20250702171443); points raw/verified 0/0
- dropped by code checks: 8 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; scale word 'thousand' not supported by quote or table header: 4)

### d7 [base_rates] Seasonal adjustment methodology

Hypothesis: The SAAR is the NSA monthly count times a seasonal factor times 12; knowing the typical August seasonal factor and the NSA August level relative to July lets us convert a July NSA base into an August SAAR estimate.

Queries issued by the searcher: Census housing starts seasonal factors table monthly not seasonally adjusted; new residential construction August 2025 housing starts not seasonally adjusted 130,000; housing starts June 2026 Census new residential construction release; Census "residential construction" seasonal factors table xlsx "not seasonally adjusted" housing starts 2025

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf?mod=article_inline` -> **snapshot** (snapshot 20240419055633); points raw/verified 15/0
- `https://www.census.gov/construction/nrc/historical_data/index.html` -> **snapshot** (snapshot 20250314000430); points raw/verified 0/0
- `https://fred.stlouisfed.org/series/HOUSTNSA` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://books.google.com.sg/books/download/Construction_Reports.pdf?id=N1rlsXnlVewC&hl=zh-CN&output=pdf&sig=ACfU3U0nsYpZj_FZGJqhdAi_2TERj1Tx3w` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'thousand' not supported by quote or table header: 14; value_as_written not in quote as a whole number: 1)

### d8 [shocks] Macro/credit and policy environment

Hypothesis: Mortgage rates, labor market, tariffs on building materials, and any mid-2026 policy or weather shocks shift the August starts level relative to trend; measurable exposure (rate changes, material cost indices) adjusts the baseline.

Queries issued by the searcher: mortgage rates August 2026 30-year fixed Freddie Mac; lumber prices 2026 tariffs construction costs; housing starts June 2026 annual rate Census Bureau new residential construction; Freddie Mac mortgage rates June 2026 July 2026 30-year average

- `https://www.census.gov/construction/nrc/pdf/newresconst.pdf` -> **snapshot** (snapshot 20260730015329); points raw/verified 15/11
  - p41 Privately-owned housing starts, United States, June 2026, seasonally adjusted an = **1,427,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing starts in June were at a seasonally adjusted annual rate of 1,427,000."
  - p42 Privately-owned housing starts, United States, May 2026, revised seasonally adju = **1,199,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "This is 19.0 percent (±15.9 percent) above the revised May estimate of 1,199,000"
  - p43 Privately-owned housing starts, United States, June 2025, seasonally adjusted an = **1,379,000** housing units at annual rate (SAAR) (2025-06-01..2025-06-30) [keep: ] quote: "above the June 2025 rate of 1,379,000"
  - p44 Single-family housing starts, United States, June 2026, seasonally adjusted annu = **895,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Single-family housing starts in June were at a rate of 895,000"
  - p45 Single-family housing starts, United States, May 2026, revised seasonally adjust = **897,000** housing units at annual rate (SAAR) (2026-05-01..2026-05-31) [keep: ] quote: "below the revised May figure of 897,000"
  - p46 Housing starts in buildings with five units or more, United States, June 2026, s = **513,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "The June rate for units in buildings with five units or more was 513,000."
  - p47 Privately-owned housing units authorized by building permits, United States, Jun = **1,367,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing units authorized by building permits in June were at a seasonally adjusted annual rate of 1,367,000."
  - p48 Single-family building permit authorizations, United States, June 2026, seasonal = **871,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Single-family authorizations in June were at a rate of 871,000"
  - p49 Privately-owned housing completions, United States, June 2026, seasonally adjust = **1,392,000** housing units at annual rate (SAAR) (2026-06-01..2026-06-30) [keep: ] quote: "Privately-owned housing completions in June were at a seasonally adjusted annual rate of 1,392,000."
  - p50 Average revision to preliminary seasonally adjusted estimates of total building  = **2.9** percent (not stated (page dated 2026-07-15)) [keep: ] quote: "On average, the preliminary seasonally adjusted estimates of total building permits, housing starts and housing completions are revised 2.9 percent or less."
  - p51 Months needed to establish an underlying trend for total housing starts = **6** as written "six", value check pending months (not stated (page dated 2026-07-15)) [keep: ] quote: "It may take three months to establish an underlying trend for building permit authorizations, six months for total starts, and six months for total completions."
- `https://www.freddiemac.com/pmms/archive` -> **snapshot** (snapshot 20260731224527); points raw/verified 11/11
  - p52 30-year fixed-rate mortgage average rate, week of June 4, 2026 = **6.48** % (2026-06-04..2026-06-04) [keep: ] quote: "June 04, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.48% \| 5.79% \|"
  - p53 30-year fixed-rate mortgage average rate, week of June 11, 2026 = **6.52** % (2026-06-11..2026-06-11) [keep: ] quote: "June 11, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.52% \| 5.84% \|"
  - p54 30-year fixed-rate mortgage average rate, week of June 18, 2026 = **6.47** % (2026-06-18..2026-06-18) [keep: ] quote: "June 18, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.47% \| 5.81% \|"
  - p55 30-year fixed-rate mortgage average rate, week of June 25, 2026 = **6.49** % (2026-06-25..2026-06-25) [keep: ] quote: "June 25, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.84% \|"
  - p56 30-year fixed-rate mortgage average rate, week of July 2, 2026 = **6.43** % (2026-07-02..2026-07-02) [keep: ] quote: "July 02, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.43% \| 5.79% \|"
  - p57 30-year fixed-rate mortgage average rate, week of July 9, 2026 = **6.49** % (2026-07-09..2026-07-09) [keep: ] quote: "July 09, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.49% \| 5.82% \|"
  - p58 30-year fixed-rate mortgage average rate, week of July 16, 2026 = **6.55** % (2026-07-16..2026-07-16) [keep: ] quote: "July 16, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.55% \| 5.93% \|"
  - p59 30-year fixed-rate mortgage average rate, week of July 23, 2026 = **6.58** % (2026-07-23..2026-07-23) [keep: ] quote: "July 23, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.58% \| 5.96% \|"
  - p60 30-year fixed-rate mortgage average rate, week of July 30, 2026 = **6.66** % (2026-07-30..2026-07-30) [keep: ] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
  - p61 15-year fixed-rate mortgage average rate, week of June 4, 2026 = **5.79** % (2026-06-04..2026-06-04) [keep: ] quote: "June 04, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.48% \| 5.79% \|"
  - p62 15-year fixed-rate mortgage average rate, week of July 30, 2026 = **6.04** % (2026-07-30..2026-07-30) [keep: ] quote: "July 30, 2026 \| \| 30-Yr FRM \| 15-Yr FRM \| \|---\|---\|---\| \| Average Rates \| 6.66% \| 6.04% \|"
- `https://g2capitaladvisors.com/wp-content/uploads/2026/08/G2CA-Building-Materials-Monitor.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://therealdeal.com/national/2026/05/27/construction-costs-pile-up-as-copper-lumber-spike/` -> **snapshot** (snapshot 20260721185710); points raw/verified 7/7
  - p63 Average 30-year fixed mortgage rate, Freddie Mac, latest week reported = **6.51** % (not stated (page dated 2026-05-27)) [DISCARD: Discarded in round 1; a 'latest week' mortgage rate that duplicates the dated weekly series p52-p60 and adds no new info] quote: "Freddie Mac last week pegged the average 30-year fixed mortgage rate at 6.51 percent, its highest level since August."
  - p64 Increase in diesel prices since late February = **50** % (not stated (page dated 2026-05-27)) [keep: ] quote: "The war involving Iran has disrupted global oil and petrochemical supplies, pushing diesel prices roughly 50 percent higher since late February."
  - p65 Import taxes on some Canadian lumber producers (duties plus Trump-era tariffs) = **45** % (not stated (page dated 2026-05-27)) [keep: ] quote: "Duties and Trump-era tariffs together have pushed import taxes on some Canadian lumber producers to roughly 45 percent."
  - p66 Increase in Random Lengths framing lumber composite index since December lows = **30** % (not stated (page dated 2026-05-27)) [keep: ] quote: "Random Lengths' framing lumber composite index has jumped more than 30 percent since December lows."
  - p67 Share of NAHB April confidence survey respondents reporting difficulty pricing h = **70** % (2026-04-01..2026-04-30) [keep: ] quote: "The National Association of Home Builders said 70 percent of respondents in its April confidence survey reported difficulty pricing homes because of volatility in material costs."
  - p68 Copper content in the average American house = **400** pounds (not stated (page dated 2026-05-27)) [keep: ] quote: "The average American house contains more than 400 pounds of the metal across electrical wiring, plumbing and appliances, and prices recently hit record highs."
  - p69 Eagle Materials added fuel cost to wallboard shipping expenses, fourth quarter,  = **2** USD per thousand square feet (not stated (page dated 2026-05-27)) [keep: ] quote: "Eagle Materials recently said rising fuel costs added more than $2 per thousand square feet to wallboard shipping expenses during the fourth quarter."
- dropped by code checks: 4 (scale word 'thousand' not supported by quote or table header: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b1 [own_history] Recent monthly prints

Hypothesis: The July 2026 starts print (published ~mid-Aug 2026, before cutoff) is the single most important missing anchor; it would let a naive/momentum method forecast August directly and reveal whether June's 1,427k spike reverted.

Queries issued by the searcher: Census Bureau new residential construction July 2026 housing starts; privately-owned housing starts July 2026 SAAR; census.gov "New Residential Construction" July 2026 CB26-127 release; NAHB Eye on Housing housing starts July 2026 single-family multifamily analysis

- `https://www.census.gov/construction/nrc/current/index.html` -> **snapshot** (snapshot 20260808220529); points raw/verified 15/2
  - p70 Privately-owned housing starts SAAR, June 2025 (year-ago comparison) = **1,379,000** housing units at annual rate (SAAR) (2025-06-01..2025-06-30) [keep: ] quote: "is 3.5 percent (±14.3 percent)* above the June 2025 rate of 1,379,000"
  - p71 Privately-owned housing units authorized by building permits SAAR, June 2025 = **1,399,000** housing units at annual rate (SAAR) (2025-06-01..2025-06-30) [keep: ] quote: "is 2.3 percent below the June 2025 rate of 1,399,000"
- `https://economics.td.com/us-housing-starts-and-permits?linkId=165656202` -> **snapshot** (snapshot 20220518135305); points raw/verified 15/15
  - p72 U.S. housing starts, total, annualized, April 2022 = **1,724,000** housing units at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "U.S. housing starts fell by 0.2% month-on-month (m/m) to 1.724 million units (annualized) in April"
  - p73 U.S. housing starts, month-on-month change, April 2022 = **0.2** % (2022-04-01..2022-04-30) [keep: ] quote: "U.S. housing starts fell by 0.2% month-on-month (m/m) to 1.724 million units (annualized) in April"
  - p74 Market expectation for U.S. housing starts, annualized, April 2022 = **1,766,000** housing units at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "coming in even lower than market expectations which called for a decline to 1.766 million units"
  - p75 Revision to March 2022 total housing starts = **65,000** housing units at annual rate (2022-03-01..2022-03-31) [keep: ] quote: "Revisions to last month's data lopped 65k units off of March starts"
  - p76 Revision to March 2022 single-family housing starts = **-13,000** housing units at annual rate (2022-03-01..2022-03-31) [keep: ] quote: "with downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p77 Revision to March 2022 multifamily housing starts = **-52,000** housing units at annual rate (2022-03-01..2022-03-31) [keep: ] quote: "with downward revisions to both the single-family (-13k) and multifamily (-52k) segments"
  - p78 Multifamily housing starts, month-on-month change, April 2022 = **15.3** % (2022-04-01..2022-04-30) [keep: ] quote: "multifamily starts rose by 15.3% m/m (or 83k)"
  - p79 Multifamily housing starts, month-on-month change in units, April 2022 = **83,000** housing units at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "multifamily starts rose by 15.3% m/m (or 83k)"
  - p80 Single-family housing starts, month-on-month change, April 2022 = **7.3** % (2022-04-01..2022-04-30) [keep: ] quote: "Single-family starts, however, fell by 7.3% m/m (or -87k)"
  - p81 Single-family housing starts, month-on-month change in units, April 2022 = **-87,000** housing units at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "Single-family starts, however, fell by 7.3% m/m (or -87k)"
  - p82 U.S. building permits, total, annualized, April 2022 = **1,819,000** permits at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p83 U.S. building permits, month-on-month change, April 2022 = **3.2** % (2022-04-01..2022-04-30) [keep: ] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p84 U.S. building permits, month-on-month change in units, April 2022 = **60,000** permits at annual rate (2022-04-01..2022-04-30) [keep: ] quote: "Permitting activity also retreated on the month, falling by 3.2% (or 60k) to 1.819 million"
  - p85 Multifamily permits, month-on-month change, April 2022 = **1** % (2022-04-01..2022-04-30) [keep: ] quote: "Multifamily permits fell by 1% (or 7k) while single-family permits fell even further by 4.6% (or -53k)"
  - p86 Single-family permits, month-on-month change, April 2022 = **4.6** % (2022-04-01..2022-04-30) [keep: ] quote: "Multifamily permits fell by 1% (or 7k) while single-family permits fell even further by 4.6% (or -53k)"
- `https://www.realpage.com/analytics/july-2026-us-permit-update/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mdm.com/news/top-distributor-sectors/building-materials-construction/july-u-s-housing-starts-fall-as-permits-rise/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (period year 2026 does not appear in the page text or URL (likely mis-dated): 13)

### b2 [related_series] Permit pipeline

Hypothesis: July 2026 building permits (total and single-family) would tighten the starts forecast via the permit-lead route; June permits (1,367k) sit below June starts, suggesting a pullback that July permits would confirm or refute.

Queries issued by the searcher: census building permits July 2026; single-family authorizations July 2026; "June 2026" new residential construction building permits 1,367,000 single-family authorizations; Census "New Residential Construction" June 2026 release July 17 2026 permits rate

- `https://www.redbooklumberdata.com/2026/07/17/u-s-census-bureau-monthly-new-residential-consctruction-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/building-permits` -> **snapshot** (snapshot 20260815062753) **LEAK SENTINEL HIT ['(?<![\\d.,])1\\.39M(?!\\d|[.,]\\d)(?![A-Za-z])'] (excluded)**; points raw/verified -/-
- `https://www.realpage.com/analytics/us-permits-june-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.housingaffordabilityinstitute.org/june-2026-census-bps/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Consensus nowcast

Hypothesis: A published August 2026 housing-starts nowcast/consensus (e.g., Trading Economics, MBA, Fannie Mae) made before cutoff would provide a direct anchor and help resolve the June-spike-reversion question.

Queries issued by the searcher: housing starts forecast August 2026; US housing starts consensus August 2026; Fannie Mae housing forecast August 2026 housing starts; MBA mortgage finance forecast August 2026 housing starts 2026 total; yieldpro Fannie Mae multifamily starts forecast August 2026 quarterly Q3 2026 single-family starts forecast; "housing starts" forecast "August 2026" economists expectations before release August 18 2026

- `https://cmegroup.econoday.com/byevent?fid=667073&year=2026&cty=US&ctyall=10738893&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://us.econoday.com/byevent?fid=667073&year=2026&cty=US&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newslink.mba.org/cmf-newslinks/2026/september/mba-newslink-thursday-apr-14-2021/chart-of-the-week-new-residential-construction/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/united-states/housing-starts?stream=future&utm_campaign=newsletter_axiosfutureofwork&utm_medium=email&utm_source=newslett` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['housing starts', 'us housing starts', 'housing starts august']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p9', 'p41'] Same June 2026 total starts figure (1,427,000) repeated across d1/d2/d8; identical underlying Census release, not independent confirmation.
- corroborating: ['p2', 'p11', 'p42'] Same revised May 2026 total starts (1,199,000) repeated; single underlying measurement.
- corroborating: ['p10', 'p44'] Same June 2026 single-family starts (895,000); duplicate of one measurement.
- corroborating: ['p3', 'p47'] Same June 2026 total permits (1,367,000); duplicate.
- corroborating: ['p4', 'p48'] Same June 2026 single-family permits (871,000); duplicate.
- corroborating: ['p1', 'p3', 'p7'] June starts (1,427k) roughly consistent with June permits (1,367k) and 5+ unit permits (445k); permits slightly below starts implies pipeline modestly tightening, consistent with a pullback from June'
- corroborating: ['p1', 'p2'] June 1,427k vs revised May 1,199k shows a large +19% monthly jump; June is an outlier high, so July/August likely revert toward the ~1.2-1.3M range.
- corroborating: ['p12', 'p13', 'p25', 'p50'] Revision magnitudes (1.9-2.9%) are the same Census methodology statement across vintages; they bound first-print noise, not a level.
- corroborating: ['p14', 'p19'] March 2024 total starts (1,321k) duplicated; older-period analogue only.
- corroborating: ['p15', 'p22'] March 2024 single-family starts (1,022k) duplicated.
- corroborating: ['p16', 'p23'] Feb 2024 single-family starts (1,167k) duplicated.
- corroborating: ['p17', 'p20'] Feb 2024 total starts (1,549k) duplicated.
- corroborating: ['p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60'] Freddie Mac 30-yr mortgage series June-July 2026 shows rates drifting up from ~6.48% to 6.66%, a mild headwind for single-family starts into August.
- conflicting: ['p63', 'p52'] p63 (6.51%, 'highest since August') is a secondary restatement of the Freddie Mac series; the primary weekly series (p52-p60) is more reliable and shows a rising path, so p63 is redundant/less precise
- corroborating: ['p64', 'p65', '66', 'p67', 'p68', 'p69'] Cost-side pressures (diesel, lumber, copper, wallboard) raise builder costs and lean toward softer starts; qualitative direction only, no direct level.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p9', 'p41'] Same June 2026 total starts SAAR (1,427,000) reported in three snapshots; identical underlying Census release, so this is one measurement, not independent confirmation.
- corroborating: ['p2', 'p11', 'p42'] Same revised May 2026 total starts SAAR (1,199,000); one underlying figure repeated.
- corroborating: ['p1', 'p2'] June 2026 (1,427k) vs revised May (1,199k) implies a large ~19% jump; the June spike is the key momentum question for August.
- corroborating: ['p3', 'p5', 'p8', 'p71'] Total permits: June 2026 1,367k below May 1,410k and below June 2025 1,399k; consistent picture of a softening permit pipeline.
- corroborating: ['p4', 'p6'] Single-family permits June 871k vs revised May 892k, a 2.4% decline; same release, consistent with total permit softening.
- corroborating: ['p3', 'p7', 'p4'] June permits decompose: 871k single-family + 445k 5+ unit ≈ 1,316k, close to 1,367k total (remainder 2-4 unit); internally consistent.
- corroborating: ['p10', 'p44', 'p45'] Single-family starts June 895k vs May 897k, essentially flat; single-family is stable while multifamily drives the June spike.
- corroborating: ['p46', 'p1', 'p10'] June 5+ unit starts 513k plus single-family 895k ≈ 1,408k, close to total 1,427k; the June spike is multifamily-driven and volatile.
- corroborating: ['p49', 'p1'] June completions 1,392k near starts 1,427k; pipeline roughly balanced, no strong backlog signal.
- corroborating: ['p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60'] 30-year mortgage rate drifted up from ~6.48% early June to 6.66% end-July 2026; modest headwind to single-family demand and starts.
- corroborating: ['p64', 'p65', 'p66', 'p67'] Material cost pressures (diesel +50%, lumber +30%, Canadian lumber duties ~45%, 70% of builders reporting pricing difficulty) point to a supply-cost drag on starts.
- corroborating: ['p12', 'p13', 'p25', 'p50'] Census revision magnitudes (1.9-2.9%) indicate preliminary prints carry meaningful noise; supports wide uncertainty on any forecast.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24'] 2023-2024 starts history (1.3-1.55M range) provides context for the current ~1.2-1.4M level; older vintage, used only as background.
- corroborating: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86'] 2022 TD commentary on starts/permits volatility and revisions; illustrates that monthly starts are noisy and multifamily swings dominate; contextual only.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August-to-June total starts ratio (reversion factor) | 0.9 | 0.72..1.05 | 0.6148..1.23 (widened) | ratio | m1 (m1) | June 2026 total starts (1,427k) were a multifamily-driven spike well above May (1,199k); permits (1,367k) and rising mortgage rates suggest partial reversion by August. A ratio near 0.9 reflects typical mean reversion of a spike month toward the permit-implied level, with wide range for monthly nois | June 2026 is a representative base and August reverts partway toward the permit-implied trend. | A July 2026 starts print near or above 1,427k, or a July permit surge, would indicate no reversion. |
| a2 | August-to-June single-family starts ratio | 0.97 | 0.85..1.08 | 0.6775..1.355 (widened) | ratio | m2 (m2) | Single-family starts were flat May-to-June (897k to 895k) and single-family permits softened modestly (892k to 871k); rising mortgage rates (6.48% to 6.66%) and material costs are mild headwinds, so a near-flat ratio with modest downside is appropriate. | Single-family starts continue their stable trend into August. | A sharp single-family permit drop or mortgage-rate spike above ~7% would push the ratio lower. |
| a3 | August-to-June multifamily (5+ unit) starts ratio | 0.85 | 0.6..1.1 | 0.5745..1.149 (widened) | ratio | m2 (m2) | June 5+ unit starts (513k) were unusually high and multifamily is the most volatile component; permits for 5+ units (445k) sit well below the June starts rate, implying a pullback. A ratio below 1 with a wide range reflects this volatility. | Multifamily starts revert toward the lower permit-implied pace. | A July 5+ unit permit surge or a large multifamily starts print would overturn the reversion assumption. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,244,352 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 1,299,650 | ['p10', 'p46'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of single-family, multifamily

Result: central **1,271,700** unit/year, 80% interval [860,831, 1,878,675] unit/year, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for the seasonally adjusted annual rate of privately-owned housing starts in the United States for August 2026 is 1,271,700 unit/year (80% model-based interval 860,831 to 1,878,675 unit/year). This covers privately-owned starts only, excluding publicly-owned units.

Two methods were combined at equal weight (50% and 50%). The first anchors on the June 2026 total starts print of 1,427,000 housing units at annual rate (SAAR) and applies a reversion factor of 0.9 (range 0.6148 to 1.23). The second decomposes starts into single-family (895,000 housing units at annual rate (SAAR)) and [n]+ unit components (513,000 housing units at annual rate (SAAR)), trended with ratios of 0.97 (range 0.6775 to 1.355) and 0.85 (range 0.5745 to 1.149).

Only the June prints are observed; all August ratios are analyst assumptions. The interval reflects input uncertainty, not demonstrated accuracy. The main risk is that the June multifamily spike either fully persists or fully reverses. Timelier July/August permits and starts data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August-to-June total starts ratio (reversion factor): 0.9 ratio, range 0.6148 to 1.23 (range widened by code); used by m1. Overturned by: A July 2026 starts print near or above [n]k, or a July permit surge, would indicate no reversion.
- a2 August-to-June single-family starts ratio: 0.97 ratio, range 0.6775 to 1.355 (range widened by code); used by m2. Overturned by: A sharp single-family permit drop or mortgage-rate spike above ~[n] would push the ratio lower.
- a3 August-to-June multifamily ([n]+ unit) starts ratio: 0.85 ratio, range 0.5745 to 1.149 (range widened by code); used by m2. Overturned by: A July [n]+ unit permit surge or a large multifamily starts print would overturn the reversion assumption.

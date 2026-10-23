# Evidence ledger: fc_ca_rail_2026_07

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the total freight carried by Canadian railways in July 2026, in tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total traffic carried, Canada).
- as_of: 2026-08-29
- Pinned target: Total freight carried by Canadian railways (all traffic carried, Canada) during July 2026, as first reported by Statistics Canada in its monthly Railway carloadings release (Table 23-10-0079-01 / The Daily release). Counts all revenue freight loaded and carried by Canadian Class I and regional railw | unit metric tonnes | period 2026-07-01..2026-07-31 | publisher Statistics Canada

- Official value (scoring only, never shown to the agent): 31,686,803

## Directions and pages

### d1 [own_history] Statistics Canada time series

Hypothesis: July tonnage follows a stable seasonal pattern relative to adjacent months and prior Julys; the July 2026 value can be anchored on July 2023-2025 reported totals plus recent monthly levels, adjusted for trend. Role: provides the base level and seasonal shape.

Queries issued by the searcher: Statistics Canada railway carloadings total traffic carried tonnes monthly 2025; The Daily railway carloadings July 2025 Statistics Canada tonnes; "Railway carloadings, June 2026" Statistics Canada The Daily; Table 23-10-0079-01 railway carloadings total tonnage transported monthly Canada

- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/250924/dq250924f-eng.htm` -> **snapshot** (snapshot 20260520140850); points raw/verified 11/10
  - p1 Total cargo carried by Canadian railways, all traffic, Canada, July 2025 = **30,700,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "The volume of cargo carried by Canadian railways reached 30.7 million tonnes in July 2025, down 0.4% from one year earlier."
  - p2 Five-year historical average total freight volume for the month of July = **29,800,000** metric tonnes (not stated (page dated 2025-09-24)) [keep: ] quote: "the overall freight volume in July 2025 was slightly above the five-year historical average of 29.8 million tonnes for the month of July."
  - p3 Freight loadings from US rail connections, July 2025 = **3,300,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "freight loadings from US rail connections dropped 19.2% (-794 000 tonnes) to 3.3 million tonnes"
  - p4 Year-over-year change in freight loadings from US rail connections, July 2025 = **-794,000** as written "-794 000", value check pending metric tonnes (2025-07-01..2025-07-31) [DISCARD: Duplicate of the -794,000 tonnes change already embedded in p3; redundant.] quote: "freight loadings from US rail connections dropped 19.2% (-794 000 tonnes) to 3.3 million tonnes"
  - p5 Non-intermodal freight traffic in Canada, July 2025 = **24,200,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "Non-intermodal freight traffic in Canada rose 1.6% year over year to 24.2 million tonnes in July 2025"
  - p6 Intermodal shipments originating in Canada, July 2025 = **3,200,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "intermodal shipments-mainly containers-originating in Canada increased 9.4% compared with July 2024 to 3.2 million tonnes"
  - p7 Average share of total rail tonnage represented by traffic received from US conn = **12** % (2023-01-01..2024-12-31) [keep: ] quote: "In 2023 and 2024, traffic received from US connections represented an average 12.0% of total rail tonnage each month."
  - p8 Share of total rail tonnage from US connections, Q1 2025 = **10.7** % (2025-01-01..2025-03-31) [keep: ] quote: "During the first quarter of 2025, this proportion edged down to 10.7%"
  - p9 Share of total rail tonnage from US connections, Q2 2025 = **10.5** % (2025-04-01..2025-06-30) [keep: ] quote: "then to 10.5% in the second quarter"
  - p10 Share of total rail tonnage from US connections, July 2025 = **10.8** % (2025-07-01..2025-07-31) [keep: ] quote: "and settled at 10.8% in July 2025"
- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3ATotal%20traffic%20carried&23100216_facets` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-eng.pdf` -> **snapshot** (snapshot 20260225062029); points raw/verified 15/15
  - p11 Total freight transported by Canadian railways, December 2025 (monthly total ton = **31,000,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "In December, Canadian railways transported 31.0 million tonnes of freight, down 2.0% compared with December 2024"
  - p12 Total freight moved by Canadian railways, annual 2025 = **376,600,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, the volume of goods moved by rail totalled 376.6 million tonnes, down slightly (-0.2%) from the total volume in 2024."
  - p13 Total freight moved by Canadian railways, annual 2024 = **377,300,000** metric tonnes (2024-01-01..2024-12-31) [keep: ] quote: "the overall total was similar to that in 2024 (377.3 million tonnes)."
  - p14 Non-intermodal freight loaded in Canada, December 2025 = **24,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "The volume of non-intermodal freight (mainly commodities) in Canada was down 1.7% year over year to 24.8 million tonnes in December"
  - p15 Intermodal freight loadings in Canada, December 2025 = **2,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "Intermodal freight loadings (mainly containers) rose 2.0% year over year to 2.8 million tonnes in December 2025"
  - p16 Freight traffic from US rail connections in Canada, December 2025 = **3,300,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "freight traffic from US rail connections declined year over year for the 11th straight month, down 7.4% to 3.3 million tonnes in December 2025."
  - p17 Non-intermodal freight loadings in Canada, annual 2025 = **299,800,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, non-intermodal freight loadings in Canada totalled 299.8 million tonnes, up marginally (+0.9%) from 2024."
  - p18 Intermodal freight traffic in Canada, annual 2025 = **37,500,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "intermodal freight traffic (mainly containers) rose 7.4% from 2024, reaching an-all time high of 37.5 million tonnes in 2025."
  - p19 Freight loadings from US rail connections in Canada, annual 2025 = **39,300,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "annual tonnage fell by 13.3% from 2024 to 39.3 million tonnes in 2025, representing the lowest annual level since 2020"
  - p20 Share of total rail tonnage from US rail connections, average monthly 2023-2024 = **12** % (2023-01-01..2024-12-31) [keep: ] quote: "Over 2023 and 2024, freight traffic received from US rail connections in Canada represented an average of 12.0% of total rail tonnage each month."
  - p21 Share of total rail tonnage from US rail connections, Q4 2025 = **10** % (2025-10-01..2025-12-31) [keep: ] quote: "The proportion dipped further to 10.0% in the fourth quarter."
  - p22 Wheat loadings by Canadian railways, annual 2025 = **31,100,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "with loadings rising 14.3% (+3.9 million tonnes) from 2024 to reach 31.1 million tonnes in 2025."
  - p23 Coal loadings by Canadian railways, annual 2025 = **38,500,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "A notable increase was also reported for coal, rising 4.4% from 2024 to 38.5 million tonnes in 2025"
  - p24 Iron ores and concentrates loadings, December 2025 year-over-year change = **-515,000** as written "-515 000", value check pending metric tonnes (2025-12-01..2025-12-31) [DISCARD: December 2025 iron ore change; single commodity, not a July 2026 input.] quote: "loadings of iron ores and concentrates fell 10.1% (-515 000 tonnes) from the same month in 2024"
  - p25 Coal loadings, December 2025 year-over-year change = **-324,000** as written "-324 000", value check pending metric tonnes (2025-12-01..2025-12-31) [DISCARD: December 2025 coal change; single commodity, not a July 2026 input.] quote: "loadings of coal were down 9.8% (-324 000 tonnes)."
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d2 [related_series] Statistics Canada commodity detail

Hypothesis: Total tonnage is the sum over commodity groups (coal, grain, potash, crude oil, forest products, chemicals, intermodal). Summing the largest commodity groups' July 2026 tonnages (or their recent run-rates) plus a residual gives the total. Role: builds the total bottom-up and cross-checks the top-down history.

Queries issued by the searcher: Statistics Canada railway carloadings by commodity coal potash grain tonnes monthly 2026; StatCan Table 23-10-0080 principal commodities tonnage railway carloadings; "Railway carloadings, June 2026" Statistics Canada Daily; Statistics Canada table 23-10-0079-01 railway carloadings tonnage commodity Canada

- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3ACanola&23100216_facets%5B1%5D=23100216_co` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p26 Canada railway intermodal traffic loaded, May 2020 = **3,040,663** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p96 (same May 2020 intermodal value); adds no information.] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p27 Canada railway intermodal traffic loaded, Apr 2020 = **3,087,415** tonnes (2020-04-01..2020-04-30) [DISCARD: April 2020 intermodal value; pandemic-distorted and superseded.] quote: "This records a decrease from the previous number of 3,087,415.000 Tonne for Apr 2020."
  - p28 Canada railway intermodal traffic loaded, all-time high, May 2019 = **3,255,376** tonnes (2019-05-01..2019-05-31) [DISCARD: All-time-high intermodal value from 2019; superseded by p18 (2025 all-time high) and not usable for July 2026.] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p29 Canada railway intermodal traffic loaded, monthly average Jan 1999-May 2020 = **2,381,505** tonnes (1999-01-01..2020-05-31) [DISCARD: 1999-2020 intermodal monthly average; too old and superseded by recent intermodal levels (p18).] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p30 Canada railway non-intermodal traffic loaded, May 2020 = **24,396,926** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p95 (same May 2020 non-intermodal value); adds no information.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p31 Canada railway non-intermodal traffic loaded, Apr 2020 = **24,371,149** tonnes (2020-04-01..2020-04-30) [DISCARD: April 2020 non-intermodal value; pandemic-distorted and superseded.] quote: "This records an increase from the previous number of 24,371,149.000 Tonne for Apr 2020."
  - p32 Canada railway non-intermodal traffic loaded, all-time high, Oct 2018 = **28,258,207** tonnes (2018-10-01..2018-10-31) [DISCARD: 2018 all-time-high non-intermodal value; too old and superseded by recent levels, no conversion route.] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p33 Canada railway non-intermodal traffic loaded, record low, Jul 2009 = **16,818,939** tonnes (2009-07-01..2009-07-31) [DISCARD: 2009 record-low non-intermodal value; irrelevant to 2026 level.] quote: "and a record low of 16,818,939.000 Tonne in Jul 2009"
  - p34 Canada railway non-intermodal traffic loaded, monthly average Jan 1999-May 2020 = **21,490,478** tonnes (1999-01-01..2020-05-31) [DISCARD: 1999-2020 non-intermodal monthly average; too old to inform 2026 without a large trend adjustment.] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p35 Canada railway non-intermodal alumina loaded, May 2020 = **126,378** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity (alumina) May 2020; too granular and old to inform total.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p36 Canada railway non-intermodal animal feed & products loaded, May 2020 = **409,186** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p37 Canada railway non-intermodal animal or vegetable fats, oils & flours loaded, Ma = **414,481** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p38 Canada railway non-intermodal cement loaded, May 2020 = **247,356** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p39 Canada railway non-intermodal cement loaded, all-time high, Jul 2019 = **361,023** tonnes (2019-07-01..2019-07-31) [DISCARD: Cement all-time high July 2019; single commodity, too old and granular.] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p40 Canada railway non-intermodal aluminum loaded, May 2020 = **291,832** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-fra.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] US Surface Transportation Board / AAR

Hypothesis: Canadian rail traffic correlates with US Class I carload and intermodal volumes and with Canadian carrier (CN, CPKC) reported volumes; a growth rate from these related series can scale the prior-year July Canadian total. Role: provides a year-over-year growth adjustment.

Queries issued by the searcher: Statistics Canada railway carloadings July 2025 metric tonnes monthly; AAR weekly rail traffic Canada carloads July 2026; "Railway carloadings, July 2026" Statistics Canada The Daily; AAR weekly rail traffic week ending July 25 2026 Canadian railroads carloads

- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aar.org/news/aar-reports-weekly-rail-traffic-for-the-week-ending-july-4-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.progressiverailroading.com/rail_industry_trends/news/US-freight-rail-traffic-rises-34-in-Week-28--77398` -> **snapshot** (snapshot 20260723170244); points raw/verified 15/15
  - p41 U.S. freight railroads total carloads and intermodal units, week ending July 18, = **523,900** carloads and intermodal units (2026-07-12..2026-07-18) [keep: ] quote: "U.S. freight railroads hauled 523,900 carloads and intermodal units during the week ending July 18, up 3.4% compared with traffic from the same week in 2025"
  - p42 U.S. freight-rail traffic year-over-year change, week ending July 18, 2026 = **3.4** % (2026-07-12..2026-07-18) [keep: ] quote: "U.S. freight-rail traffic rises 3.4% in Week 28"
  - p43 U.S. carloads, week ending July 18, 2026 = **226,883** carloads (2026-07-12..2026-07-18) [keep: ] quote: "Carloads for the week totaled 226,883 down 1.2%"
  - p44 U.S. carloads year-over-year change, week ending July 18, 2026 = **1.2** % (2026-07-12..2026-07-18) [keep: ] quote: "Carloads for the week totaled 226,883 down 1.2%"
  - p45 U.S. intermodal volume, week ending July 18, 2026 = **297,017** containers and trailers (2026-07-12..2026-07-18) [keep: ] quote: "weekly intermodal volume totaled 297,017 containers and trailers, up 7.2%"
  - p46 U.S. intermodal volume year-over-year change, week ending July 18, 2026 = **7.2** % (2026-07-12..2026-07-18) [keep: ] quote: "weekly intermodal volume totaled 297,017 containers and trailers, up 7.2%"
  - p47 Canadian railroads carloads, week ending July 18, 2026 = **88,318** carloads (2026-07-12..2026-07-18) [keep: ] quote: "Canadian railroads reported 88,318 carloads for the week, up 3.8%, and 71,076 intermodal units, down 3.2%."
  - p48 Canadian railroads carloads year-over-year change, week ending July 18, 2026 = **3.8** % (2026-07-12..2026-07-18) [keep: ] quote: "Canadian railroads reported 88,318 carloads for the week, up 3.8%, and 71,076 intermodal units, down 3.2%."
  - p49 Canadian railroads intermodal units, week ending July 18, 2026 = **71,076** intermodal units (2026-07-12..2026-07-18) [keep: ] quote: "Canadian railroads reported 88,318 carloads for the week, up 3.8%, and 71,076 intermodal units, down 3.2%."
  - p50 Canadian railroads intermodal units year-over-year change, week ending July 18,  = **3.2** % (2026-07-12..2026-07-18) [keep: ] quote: "Canadian railroads reported 88,318 carloads for the week, up 3.8%, and 71,076 intermodal units, down 3.2%."
  - p51 Canadian railroads cumulative carloads and intermodal units, first 28 weeks of 2 = **4,599,829** carloads and intermodal units (2026-01-01..2026-07-18) [keep: ] quote: "Canadian railroads reported 4,599,829 carloads and intermodal units, up 0.6%"
  - p52 Canadian railroads cumulative carloads and intermodal units year-over-year chang = **0.6** % (2026-01-01..2026-07-18) [keep: ] quote: "Canadian railroads reported 4,599,829 carloads and intermodal units, up 0.6%"
  - p53 U.S. railroads cumulative carloads and intermodal units, first 28 weeks of 2026 = **14,176,139** carloads and intermodal units (2026-01-01..2026-07-18) [keep: ] quote: "U.S. railroads posted 14,176,139 carloads and intermodal units, up 3.4%"
  - p54 U.S. railroads cumulative carloads and intermodal units year-over-year change, f = **3.4** % (2026-01-01..2026-07-18) [keep: ] quote: "U.S. railroads posted 14,176,139 carloads and intermodal units, up 3.4%"
  - p55 Mexican railroads cumulative carloads and intermodal units year-over-year change = **10.5** % (2026-01-01..2026-07-18) [DISCARD: Mexican rail traffic; different entity, not transferable to Canadian total.] quote: "Mexican railroads logged 727,653 carloads and intermodal units, up 10.5%."
- `https://www.progressiverailroading.com/rail_industry_trends/news/US-freight-railroads-post-slight-traffic-increase-for-Week-27--77352` -> **snapshot** (snapshot 20260717054803); points raw/verified 15/15
  - p56 Canadian railroads carloads, week ending July 11 2026 = **89,784** carloads (2026-07-05..2026-07-11) [keep: ] quote: "Meanwhile, Canadian railroads posted 89,784 carloads for the week, up 1.9%, and 73,506 intermodal units, down 1.4%."
  - p57 Canadian railroads carloads year-over-year change, week ending July 11 2026 = **1.9** % (2026-07-05..2026-07-11) [keep: ] quote: "Meanwhile, Canadian railroads posted 89,784 carloads for the week, up 1.9%, and 73,506 intermodal units, down 1.4%."
  - p58 Canadian railroads intermodal units, week ending July 11 2026 = **73,506** intermodal units (2026-07-05..2026-07-11) [keep: ] quote: "Meanwhile, Canadian railroads posted 89,784 carloads for the week, up 1.9%, and 73,506 intermodal units, down 1.4%."
  - p59 Canadian railroads intermodal units year-over-year change, week ending July 11 2 = **1.4** % (2026-07-05..2026-07-11) [keep: ] quote: "Meanwhile, Canadian railroads posted 89,784 carloads for the week, up 1.9%, and 73,506 intermodal units, down 1.4%."
  - p60 Canadian railroads cumulative carloads and intermodal units, first 27 weeks of 2 = **4,440,435** carloads and intermodal units (2026-01-01..2026-07-11) [keep: ] quote: "Canadian railroads logged 4,440,435 carloads and intermodal units, up 0.6%"
  - p61 Canadian railroads cumulative carloads and intermodal units year-over-year chang = **0.6** % (2026-01-01..2026-07-11) [keep: ] quote: "Canadian railroads logged 4,440,435 carloads and intermodal units, up 0.6%"
  - p62 U.S. freight railroads total carloads and intermodal units, week ending July 11  = **503,525** carloads and intermodal units (2026-07-05..2026-07-11) [keep: ] quote: "U.S. freight railroads hauled 503,525 carloads and intermodal units in the week ending July 11, a 1.5% increase compared with traffic in the same week in 2025"
  - p63 U.S. freight railroads total carloads and intermodal units year-over-year change = **1.5** % (2026-07-05..2026-07-11) [keep: ] quote: "U.S. freight railroads hauled 503,525 carloads and intermodal units in the week ending July 11, a 1.5% increase compared with traffic in the same week in 2025"
  - p64 U.S. freight railroads carloads, week ending July 11 2026 = **233,040** carloads (2026-07-05..2026-07-11) [keep: ] quote: "Total carloads slumped 0.4% to 233,040, while intermodal volume increased 3% to 280,485 containers and trailers."
  - p65 U.S. freight railroads carloads year-over-year change, week ending July 11 2026 = **0.4** % (2026-07-05..2026-07-11) [keep: ] quote: "Total carloads slumped 0.4% to 233,040, while intermodal volume increased 3% to 280,485 containers and trailers."
  - p66 U.S. freight railroads intermodal volume, week ending July 11 2026 = **280,485** containers and trailers (2026-07-05..2026-07-11) [keep: ] quote: "Total carloads slumped 0.4% to 233,040, while intermodal volume increased 3% to 280,485 containers and trailers."
  - p67 U.S. freight railroads intermodal volume year-over-year change, week ending July = **3** % (2026-07-05..2026-07-11) [keep: ] quote: "Total carloads slumped 0.4% to 233,040, while intermodal volume increased 3% to 280,485 containers and trailers."
  - p68 U.S. railroads cumulative carloads and intermodal units, first 27 weeks of 2026 = **13,652,239** carloads and intermodal units (2026-01-01..2026-07-11) [keep: ] quote: "U.S. railroads hauled 13,652,239 carloads and intermodal units, up 3.4%"
  - p69 U.S. railroads cumulative carloads and intermodal units year-over-year change, f = **3.4** % (2026-01-01..2026-07-11) [keep: ] quote: "U.S. railroads hauled 13,652,239 carloads and intermodal units, up 3.4%"
  - p70 Mexican railroads cumulative carloads and intermodal units year-over-year change = **9.8** % (2026-01-01..2026-07-11) [DISCARD: Mexican rail traffic; different entity, not transferable.] quote: "Mexican railroads posted 700,187 carloads and intermodal units, up 9.8%"

### d4 [physical_flow] Grain and potash supply chain

Hypothesis: Grain and potash are large, seasonally variable components; their July 2026 rail movements can be inferred from port terminal receipts (Vancouver, Prince Rupert, Thunder Bay) and crop/potash production. Role: constrains the two largest seasonal swing components.

Queries issued by the searcher: Port of Vancouver grain rail receipts July 2026; Canadian Grain Commission weekly rail shipments July 2026; Statistics Canada railway carloadings July 2026; potash rail shipments Canada 2026 guidance; Nutrien potash sales volumes guidance 2026 rail shipments Canpotex; "grain monitor" July 2026 western Canadian railway grain shipments potash carloadings Statistics Canada Daily August 2026

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grainmonitor.ca/Downloads/Presentations/20240909_BusinessOfShipping_GHTS.pdf` -> **snapshot** (snapshot 20260613123112); points raw/verified 15/9
  - p71 Vancouver share of Western port grain volumes, 5-year average 2019-20 to 2022-23 = **67** % (2019-08-01..2023-07-31) [keep: ] quote: "Vancouver 67%"
  - p72 Prince Rupert share of Western port grain volumes, 5-year average 2019-20 to 202 = **13** % (2019-08-01..2023-07-31) [keep: ] quote: "Prince Rupert 13%"
  - p73 Thunder Bay share of Western port grain volumes, 5-year average 2019-20 to 2022- = **20** % (2019-08-01..2023-07-31) [keep: ] quote: "Thunder Bay 20%"
  - p74 Western Canadian car cycle time, 2023-24 crop year = **15.3** days (2023-08-01..2024-07-31) [DISCARD: Car cycle time; not a tonnage input.] quote: "2023-24 = 15.3 days"
  - p75 Western Canadian car cycle time, 2022-23 crop year = **14** days (2022-08-01..2023-07-31) [DISCARD: Car cycle time; not a tonnage input.] quote: "2022-23 = 14.0 days"
  - p76 Canada share of crop exported against total grains production = **60** % (not stated (page dated 2024-09-09)) [keep: ] quote: "Canada: 60% (62 M of 95 M)"
  - p77 Canada length of haul to port of export, rail share = **95** % (not stated (page dated 2024-09-09)) [keep: ] quote: "Canada: 790 - 1,150 miles (Rail 95%, Truck 5%)"
  - p78 Number of licensed loop-track country elevator facilities, July 2024 = **51** facilities (2024-07-01..2024-07-31) [DISCARD: Elevator count; not a tonnage input.] quote: "July 2024 - 51 licensed loop - track facilities"
  - p79 Share of elevators within 160km of an interchange (extended interswitching limit = **88** % (not stated (page dated 2024-09-09)) [DISCARD: Interswitching share; not a tonnage input.] quote: "88% of elevators are within 160km of an interchange, the extended limit"
- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202603.pdf?utm_source=lakelandtoday.ca&utm_campaign=lakelandtoday.ca%3A%20outbound&utm_m` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (scale word 'million' not supported by quote or table header: 6)

### d5 [shocks] Rail network operations

Hypothesis: Strikes, wildfires, floods, derailments, or labour disruptions in July 2026 would reduce tonnage versus trend; absence of disruption supports a normal seasonal level. Role: adjusts the base estimate for realized disruptions.

Queries issued by the searcher: Canada rail strike July 2026; Statistics Canada railway carloadings July 2026; wildfires rail disruption Northern Ontario CN CPKC July 2026; CPKC IBEW strike ends signal workers July 2026 Canada

- `https://www.theglobeandmail.com/business/article-northern-ontario-wildfires-disrupt-rail-forestry-operations/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tsb-bst.gc.ca/eng/enquetes-investigations/rail/2026/r26t0219/r26t0219.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cbc.ca/lite/story/9.7274475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.trains.com/pro/freight/class-i/?filter_tag=signals-train-control%2Cnew-york-central%2Ccanada%2Cfamily-friendly` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Industry forecasts and carrier guidance

Hypothesis: Published 2026 rail volume forecasts or carrier guidance imply a growth rate applicable to the July total. Role: provides an independent growth assumption to scale prior-year July.

Queries issued by the searcher: CN 2026 guidance Q2 2026 results carloads revenue ton miles; CPKC Q2 2026 results carloads volumes guidance; Canada rail freight volumes forecast 2026 growth carloadings outlook; Statistics Canada railway carloadings July 2026 monthly

- `https://ecprod.cn.ca/corp/en/news/2026/07/cn-delivers-on-commitments-with-strong-second-quarter-results-an/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railwayage.com/wp-content/uploads/2026/07/Exhibit-99-1-Q2-2026-Earnings-Release.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/wp-content/uploads/2026/07/2026_Q1_RAC_Quarterly_Report_FR_v1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.trains.com/pro/freight/class-i/cn-boosts-outlook-as-volume-growth-tops-expectations/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Statistics Canada monthly Railway carloadings releases for July 2023 and July 2024 (total traffic carried, Canada)

Hypothesis: Adding July 2023 and July 2024 total tonnage to the target history would let series_naive and yoy_scaling use a proper multi-year July series rather than a single July 2025 anchor, materially tightening the base level and seasonal shape (d1).

Queries issued by the searcher: site:www150.statcan.gc.ca railway carloadings July 2024 total tonnes; StatCan Daily railway carloadings July 2023 million tonnes carried; "Railway carloadings, July 2023" The Daily statcan 28.9 million tonnes released September 2023; The Daily Railway carloadings July 2025 total tonnage million metric tonnes statcan

- `https://www150.statcan.gc.ca/n1/daily-quotidien/240920/dq240920c-eng.htm` -> **snapshot** (snapshot 20260712054259); points raw/verified 15/15
  - p80 Total freight carried by Canadian railways, all traffic, Canada, July 2024 = **29,900,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "In July, Canadian railways transported 29.9 million tonnes of freight, up 1.6% from July 2023"
  - p81 Year-over-year change in total freight carried, Canada, July 2024 vs July 2023 = **1.6** % (2024-07-01..2024-07-31) [keep: ] quote: "In July, Canadian railways transported 29.9 million tonnes of freight, up 1.6% from July 2023"
  - p82 Five-year average total freight carried for the month of July, Canada = **30,300,000** metric tonnes (not stated (page dated 2024-09-20)) [keep: ] quote: "The overall freight volume was just under the five-year average of 30.3 million tonnes for the month of July."
  - p83 Intermodal shipments (mainly containers) originating in Canada, July 2024 = **2,800,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "rising sharply by 19.2% year over year to 2.8 million tonnes"
  - p84 Year-over-year change in intermodal shipments originating in Canada, July 2024 = **19.2** % (2024-07-01..2024-07-31) [keep: ] quote: "rising sharply by 19.2% year over year to 2.8 million tonnes"
  - p85 Freight traffic arriving from the United States, July 2024 = **3,800,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "increasing 1.7% year over year to 3.8 million tonnes"
  - p86 Year-over-year change in freight traffic arriving from the United States, July 2 = **1.7** % (2024-07-01..2024-07-31) [keep: ] quote: "increasing 1.7% year over year to 3.8 million tonnes"
  - p87 Non-intermodal freight loadings, Canada, July 2024 = **23,200,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "edging down 0.2% to 23.2 million tonnes in July"
  - p88 Year-over-year change in non-intermodal freight loadings, Canada, July 2024 = **0.2** % (2024-07-01..2024-07-31) [keep: ] quote: "edging down 0.2% to 23.2 million tonnes in July"
  - p89 Year-over-year change in iron ores and concentrates loadings, Canada, July 2024 = **12.3** % (2024-07-01..2024-07-31) [keep: ] quote: "loadings of iron ores and concentrates, down by 12.3% (-627 000 tonnes) in July compared with the same month in 2023"
  - p90 Year-over-year change in iron ores and concentrates loadings, Canada, July 2024, = **627,000** as written "627 000", value check pending metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "loadings of iron ores and concentrates, down by 12.3% (-627 000 tonnes) in July compared with the same month in 2023"
  - p91 Year-over-year change in wheat loadings, Canada, July 2024 = **10.3** % (2024-07-01..2024-07-31) [keep: ] quote: "Wheat loadings, for example, posted a year-over-year decrease of 10.3% (-207 000 tonnes)"
  - p92 Year-over-year change in potash loadings, Canada, July 2024 = **21** % (2024-07-01..2024-07-31) [keep: ] quote: "Loadings of potash were up 21.0% (+351 000 tonnes) from July 2023"
  - p93 Year-over-year change in potash loadings, Canada, July 2024, in tonnes = **351,000** as written "351 000", value check pending metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "Loadings of potash were up 21.0% (+351 000 tonnes) from July 2023"
  - p94 Year-over-year change in fuel oils and crude petroleum loadings, Canada, July 20 = **18.5** % (2024-07-01..2024-07-31) [keep: ] quote: "loadings of fuel oils and crude petroleum-on an upward trend since November 2023-rose 18.5% (+148 000 tonnes) in July 2024 compared with July 2023"
- `https://www.statcan.gc.ca/o1/en/node/4564` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260325/cg-d001-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/251124/cg-c001-png-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] CN and CPKC Q2 2026 / July 2026 reported revenue ton-miles or carloads

Hypothesis: Carrier-reported volumes for July 2026 would provide a direct year-over-year growth factor to scale the July 2025 total (d3/d6), resolving the tension between the +0.6% cumulative carload growth and the mixed weekly signals.

Queries issued by the searcher: CN Rail July 2026 traffic statistics revenue ton miles; CPKC July 2026 carloads revenue ton miles; Statistics Canada "Railway carloadings" June 2026 The Daily tonnes; CN weekly carloads revenue ton-miles July 2026 week ended

- `https://investor.cpkcr.com/key-metrics/default.aspx` -> **snapshot** (snapshot 20250916012815); points raw/verified 0/0
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecprod.cn.ca/corp/en/news/2026/07/cn-delivers-on-commitments-with-strong-second-quarter-results-an/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/en/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [physical_flow] Grain and potash rail movements July 2026 via port terminal receipts

Hypothesis: Grain and potash are the largest seasonal swing components; port receipts at Vancouver/Prince Rupert/Thunder Bay for July 2026 would constrain the two biggest commodity groups (d4) and reduce uncertainty in the bottom-up sum.

Queries issued by the searcher: Grain Monitor week ending July 2026 Vancouver Prince Rupert grain receipts; Statistics Canada railway carloadings July 2026 monthly release; potash rail shipments July 2026 Canada Canpotex tonnes; "railway carloadings" June 2026 Statistics Canada The Daily million tonnes

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 14/14
  - p95 Canada railway carloadings: non-intermodal traffic loaded, total, May 2020 = **24,396,926** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p96 Canada railway carloadings: intermodal traffic loaded, total, May 2020 = **3,040,663** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p97 Canada railway carloadings: non-intermodal traffic loaded, monthly average Jan 1 = **21,490,478** tonnes (1999-01-01..2020-05-31) [DISCARD: Duplicate of p34; redundant.] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p98 Canada railway carloadings: non-intermodal traffic loaded, record low, July 2009 = **16,818,939** tonnes (2009-07-01..2009-07-31) [DISCARD: Duplicate of p33 (2009 record low); redundant.] quote: "a record low of 16,818,939.000 Tonne in Jul 2009"
  - p99 Canada railway carloadings: non-intermodal traffic loaded, all-time high, Octobe = **28,258,207** tonnes (2018-10-01..2018-10-31) [DISCARD: Duplicate of p32 (2018 all-time high); redundant.] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p100 Canada railway carloadings: non-intermodal animal feed & products, May 2020 = **409,186** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p36; redundant.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p101 Canada railway carloadings: non-intermodal animal or vegetable fats, oils & flou = **414,481** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p37; redundant.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p102 Canada railway carloadings: non-intermodal alumina, May 2020 = **126,378** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p35; redundant.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p103 Canada railway carloadings: non-intermodal aluminum, May 2020 = **291,832** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p40; redundant.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p104 Canada railway carloadings: non-intermodal cement, May 2020 = **247,356** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p38; redundant.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p105 Canada railway carloadings: non-intermodal cement, all-time high, July 2019 = **361,023** tonnes (2019-07-01..2019-07-31) [DISCARD: Duplicate of p39 (cement all-time high); redundant.] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p106 Canada railway carloadings: non-intermodal articles of base metal, May 2020 = **66,429** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Articles of Base Metal data was reported at 66,429.000 Tonne in May 2020."
  - p107 Canada railway carloadings: non-intermodal alcoholic & non-alcoholic beverages,  = **7,344** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alcoholic & Non-Alcoholic Beverages data was reported at 7,344.000 Tonne in May 2020."
  - p108 Canada railway carloadings: non-intermodal automobiles & mini-vans, May 2020 = **20,703** tonnes (2020-05-01..2020-05-31) [DISCARD: Single small commodity May 2020; too granular and old.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."
- `https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=2732` -> **snapshot** (snapshot 20241028223604); points raw/verified 4/4
  - p109 Number of rail carriers reporting monthly on intermodal and non-intermodal traff = **21** rail carriers (2024-08-01..2024-08-31) [keep: ] quote: "Approximately 21 rail carriers report each month on their total intermodal and non-intermodal traffic of the previous month."
  - p110 Survey response rate, recent years = **95** % (not stated (page dated 2024-10-23)) [keep: ] quote: "The response rate for this survey has been slightly above 95% for the last several years."
  - p111 Number of prior months revised with each release = **12** months (not stated (page dated 2024-10-23)) [keep: ] quote: "Estimates are provided for the reference month and the previous 12 months are revised if necessary."
  - p112 Days after reference month that respondents submit questionnaires = **8** as written "eight", value check pending working days (not stated (page dated 2024-10-23)) [keep: ] quote: "The data are collected via electronic questionnaires that are submitted by respondents eight working days after the reference month."

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['canada rail freight', 'railway carloadings', 'canada freight tonnes']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Both describe July total freight tonnage; p1 is the July 2025 level and p2 the five-year July average, consistent with a stable July level near 30 Mt.
- corroborating: ['p1', 'p5', 'p6', 'p3'] July 2025 total (p1) decomposes into non-intermodal (p5), intermodal (p6) and US-connection traffic (p3); these are components of the same StatCan release and share a source, so they corroborate the l
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p20', 'p21'] US-connection share of total tonnage declining from ~12% (2023-24) to 10.5-10.8% in 2025 and 10.0% in Q4 2025; consistent series from the same source.
- corroborating: ['p11', 'p14', 'p15', 'p16'] December 2025 total decomposes into non-intermodal, intermodal and US-connection components; internally consistent with p1's July decomposition structure.
- corroborating: ['p12', 'p13', 'p17', 'p18', 'p19'] Annual 2024/2025 totals and components; 2025 total 376.6 Mt vs 2024 377.3 Mt, essentially flat, consistent with monthly levels near 31 Mt.
- corroborating: ['p22', 'p23'] Wheat and coal annual loadings for 2025; large commodity components consistent with the non-intermodal total.
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46'] US weekly rail traffic for July 2026; carloads down 1.2%, intermodal up 7.2%, total up 3.4% — a related but different entity (US, not Canada).
- corroborating: ['p47', 'p48', 'p49', 'p50', 'p56', 'p57', 'p58', 'p59'] Canadian railroad weekly carloads and intermodal units for early/mid July 2026; carloads up ~2-4%, intermodal down ~1-3% year over year.
- corroborating: ['p51', 'p52', 'p60', 'p61'] Cumulative Canadian carloads+intermodal through weeks 27-28 of 2026, up 0.6% year over year — a modest growth signal.
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] CEIC historical intermodal and non-intermodal monthly levels from 1999-2020; older vintage but consistent with the structure of the StatCan series.
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p39', 'p40'] CEIC commodity-level non-intermodal loadings for May 2020; small components, useful only as context.
- corroborating: ['p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79'] Grain logistics context (port shares, cycle times, rail share); not directly a tonnage level but supports the grain component's plausibility.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p80', 'p81'] July 2025 total (30.7 Mt) and July 2024 total (29.9 Mt) are the same StatCan series in consecutive years; p81's +1.6% is consistent with p80 vs July 2023. These form the only usable multi-year July ta
- corroborating: ['p2', 'p82'] Both are five-year July averages from StatCan but from different vintages (29.8 Mt as of 2025 release, 30.3 Mt as of 2024 release). They are rolling windows, not the same fixed series, so they corrobo
- corroborating: ['p5', 'p6', 'p3', 'p1'] July 2025 components: non-intermodal 24.2 Mt + intermodal 3.2 Mt + US-connection loadings 3.3 Mt ≈ 30.7 Mt total (p1). Consistent decomposition, though US-connection traffic is a separate channel from
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p20', 'p21'] US-connection share of total tonnage declining from ~12% (2023-24) to 10.5-10.8% (2025) to 10.0% (Q4 2025); consistent with p3/p16/p19 showing falling US-connection tonnage. Same underlying StatCan me
- corroborating: ['p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19'] December 2025 and annual 2025 figures from the same StatCan release; annual 2025 (376.6 Mt) is essentially flat vs 2024 (377.3 Mt), consistent with monthly levels near 31 Mt in December and ~30.7 Mt i
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61'] Weekly and cumulative 2026 Canadian/US rail traffic from Progressive Railroading (AAR data). Canadian cumulative +0.6% through week 28; recent weeks mixed (carloads +1.9%/+3.8%, intermodal -1.4%/-3.2%
- corroborating: ['p26', 'p28', 'p29', 'p30', 'p32', 'p33', 'p34', 'p95', 'p96', 'p97', 'p98', 'p99'] CEIC 1999-2020 carloadings series; p26/p96 and p30/p95 are duplicate copies of the same May 2020 values. Old-period context only; not usable as a July 2026 level without a large trend adjustment.
- corroborating: ['p71', 'p72', 'p73', 'p76', 'p77'] Grain port shares and rail-share-of-export context; useful for structural understanding of grain flows but not a direct July 2026 tonnage input.
- corroborating: ['p109', 'p110', 'p111', 'p112'] Survey metadata: ~21 carriers, ~95% response, 12-month revision window, 8 working days collection. Supports treating the first-reported figure as close to final but subject to revision.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 year-over-year growth factor for Canadian rail tonnage | 1.006 | 0.97..1.04 | 0.8984..1.123 (widened) | dimensionless | m1 (m1) | Canadian cumulative carloads+intermodal through week 28 of 2026 are +0.6% (p52), and recent weeks are mixed (carloads up, intermodal down). Tonnage growth is assumed to track this modest volume growth, centered at +0.6% with a range reflecting commodity-mix and intermodal weakness. | July 2026 Canadian rail tonnage grows roughly in line with cumulative 2026 carload/intermodal volume growth. | Evidence that July 2026 tonnage diverged sharply from the +0.6% cumulative volume trend (e.g., a major disruption or commodity surge). |
| a2 | July 2026 year-over-year growth factor transferred from US rail traffic | 1.02 | 0.98..1.06 | 0.9116..1.14 (widened) | dimensionless | m2 (m2) | US cumulative carloads+intermodal are +3.4% (p54) and recent weeks +1.5% to +3.4% (p42, p63); Canadian traffic historically correlates with US but grew more slowly (+0.6%), so the transfer is centered near +2% with a wide range. | US rail growth is a reasonable proxy for Canadian rail tonnage growth in July 2026. | Evidence that Canadian and US rail traffic decoupled in mid-2026 (e.g., Canadian-specific disruptions or commodity divergence). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 30,867,342 | ['p1'] / ['a1'] | [] |  | 0.33 | median_of_backtested |  |
| m2 | formula_mc | 31,252,826 | ['p1'] / ['a2'] | [] |  | 0.33 | median_of_backtested |  |
| m3 | series_naive | 30,700,000 |  | [2025] | 0.026 | 0.33 | backtest |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **30,939,192** t, 80% interval [22,457,752, 42,623,751] t, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule inverse_backtest_error, weight on methods that use assumptions 0.67

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total freight carried by Canadian railways (all traffic carried, Canada) during July 2026 is 30,939,192 t (80% model-based interval 22,457,752 to 42,623,751 t). This targets the headline total tonnage loaded and carried in the month, not tonnage-km.

Evidence: the anchor is the observed July 2025 total of 30,700,000 metric tonnes, with July 2024 (29,900,000 metric tonnes) used for backtesting. Two methods scale that anchor by growth signals: a Canadian carload/intermodal growth factor of 1.006 (range 0.8984 to 1.123) and a US-transferred factor of 1.02 (range 0.9116 to 1.14). A third method carries the prior July forward. The three methods were combined with roughly equal weights (33%, 33%, 33%); the naive method's backtest error was 2.7%.

Only the anchor years are observed; the growth factors are assumptions, and the US transfer is a cross-border proxy. The main risk is that tonnage growth diverges from carload growth due to commodity mix and intermodal weakness. Better evidence would be actual July 2026 Canadian tonnage or commodity-level carload data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 year-over-year growth factor for Canadian rail tonnage: 1.006 dimensionless, range 0.8984 to 1.123 (range widened by code); used by m1. Overturned by: Evidence that July 2026 tonnage diverged sharply from the +[n] cumulative volume trend (e.g., a major disruption or commodity surge).
- a2 July 2026 year-over-year growth factor transferred from US rail traffic: 1.02 dimensionless, range 0.9116 to 1.14 (range widened by code); used by m2. Overturned by: Evidence that Canadian and US rail traffic decoupled in mid-2026 (e.g., Canadian-specific disruptions or commodity divergence).

# Evidence ledger: fc_ca_rail_2026_07

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the total freight carried by Canadian railways in July 2026, in tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total traffic carried, Canada).
- as_of: 2026-08-29
- Pinned target: Total freight carried by Canadian railways (all traffic carried, Canada) as first reported by Statistics Canada in the monthly Railway carloadings release for the reference month July 2026; this is the total tonnage carried (carloadings traffic), not revenue ton-km or revenue. | unit metric tonnes | period 2026-07-01..2026-07-31 | publisher Statistics Canada

- Official value (scoring only, never shown to the agent): 31,686,803

## Directions and pages

### d1 [own_history] Statistics Canada Railway carloadings time series

Hypothesis: July total tonnage follows a stable seasonal pattern relative to adjacent months and prior Julys; the target equals the most recent published monthly total scaled by the historical July-to-recent-month ratio and year-over-year trend.

Queries issued by the searcher: Statistics Canada Railway carloadings monthly total traffic carried tonnes July 2025; Table 23-10-0219-01 railway carloadings total tonnes; "Railway carloadings, July 2024" million tonnes Statistics Canada Daily; "Railway carloadings, July 2023" total tonnage million tonnes Statcan

- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/240920/dq240920c-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/251218/cg-f001-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Statistics Canada commodity-level carloadings tables

Hypothesis: Total tonnage equals the sum over commodity groups (grain, coal, potash, forest products, chemicals, intermodal, etc.); summing the largest commodity groups' July 2026 tonnages plus a residual share reproduces the headline total.

Queries issued by the searcher: Statistics Canada railway carloadings by commodity tonnes table 23-10-0219-01 principal commodities; railway carloadings Canada July 2025 total tonnage million tonnes Statistics Canada Daily; "Railway carloadings" July 2026 Statistics Canada The Daily million tonnes; Chargements ferroviaires juin 2026 Statistique Canada Le Quotidien tonnes

- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/en/canada/railway-carloadings` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.grainews.ca/daily/strong-grain-shipments-by-rail-offset-freight-losses-in-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [physical_flow] Grain, potash and coal supply chains

Hypothesis: Bulk commodities dominate tonnage; July tonnage is constrained by western grain movement, potash mine shipments and coal exports, so summing these physical flows (with rail share) plus other commodities approximates the total.

Queries issued by the searcher: Statistics Canada monthly railway carloadings July 2026 total tonnage; Quorum weekly grain carloadings July 2026 western Canadian grain rail shipments tonnes; Statistics Canada The Daily railway carloadings June 2026 million tonnes release July 2026; potash rail shipments Canada 2026 tonnes monthly Canpotex rail carloadings

- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradersunion.com/news/financial-news/show/3543020-canadian-rail-freight-july-rise/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p1 Canada railway carloadings: Non-Intermodal Traffic Loaded, total tonnage, May 20 = **24,396,926** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p2 Canada railway carloadings: Non-Intermodal Traffic Loaded, all-time high monthly = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p3 Canada railway carloadings: Non-Intermodal Traffic Loaded, record low monthly to = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [keep: ] quote: "and a record low of 16,818,939.000 Tonne in Jul 2009"
  - p4 Canada railway carloadings: Non-Intermodal Traffic Loaded, monthly average Jan 1 = **21,490,478** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p5 Canada railway carloadings: Intermodal Traffic Loaded, May 2020 = **3,040,663** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p6 Canada railway carloadings: Intermodal Traffic Loaded, all-time high monthly ton = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p7 Canada railway carloadings: Non-Intermodal: Alumina, May 2020 = **126,378** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p8 Canada railway carloadings: Non-Intermodal: Aluminum, May 2020 = **291,832** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p9 Canada railway carloadings: Non-Intermodal: Animal Feed & Products, May 2020 = **409,186** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p10 Canada railway carloadings: Non-Intermodal: Animal or Vegetable Fats, Oils & Flo = **414,481** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p11 Canada railway carloadings: Non-Intermodal: Cement, May 2020 = **247,356** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p12 Canada railway carloadings: Non-Intermodal: Cement, all-time high monthly tonnag = **361,023** metric tonnes (2019-07-01..2019-07-31) [keep: ] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p13 Canada railway carloadings: Non-Intermodal: Articles of Base Metal, May 2020 = **66,429** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Articles of Base Metal data was reported at 66,429.000 Tonne in May 2020."
  - p14 Canada railway carloadings: Non-Intermodal: Automobiles & Mini-Vans, May 2020 = **20,703** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."
  - p15 Canada railway carloadings: Non-Intermodal: Alcoholic & Non-Alcoholic Beverages, = **7,344** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alcoholic & Non-Alcoholic Beverages data was reported at 7,344.000 Tonne in May 2020."

### d4 [capacity_consumption] Railway operators (CN, CPKC) and carload capacity

Hypothesis: Total tonnage equals loaded car count times average tonnes per car; operator carload volumes and average payload give an independent check on the headline total.

Queries issued by the searcher: Statistics Canada Railway carloadings July 2026 total tonnes; CN Rail monthly carloads July 2026 average tonnes per car; CN second quarter 2026 results carloads revenue ton miles July 2026; CPKC second quarter 2026 results carloads volumes

- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecprod.cn.ca/corp/en/news/2026/07/cn-delivers-on-commitments-with-strong-second-quarter-results-an/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://getfea.com/transportation/canadian-rail-freight-volume-rises-2-6-year-over-year-in-july` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/searchindicators?title=Chargements+ferroviaires,+tonnage+total&wbdisable=true` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] US Surface Transportation Board / AAR rail traffic

Hypothesis: North American rail traffic moves with similar macro drivers; US rail carload tonnage trends in July 2026 can indicate the direction and magnitude of Canadian July tonnage relative to prior-year Julys.

Queries issued by the searcher: AAR rail traffic July 2026 carloads year over year; US rail carloadings July 2026 STB tonnage; Statistics Canada railway carloadings July 2025 total tonnage million tonnes monthly; "railway carloadings" Statistics Canada 2026 monthly tonnes "July"

- `https://www.aar.org/wp-content/uploads/2026/08/AAR-RIO-August-2026-Final.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railwayage.com/freight/class-i/aar-u-s-rail-volume-up-modestly-through-week-29/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p16 Canada railway carloadings: intermodal traffic loaded, monthly total (May 2020) = **3,040,663** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p5/p43 (same May 2020 intermodal value); adds no information.] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p17 Canada railway carloadings: non-intermodal traffic loaded, monthly total (May 20 = **24,396,926** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p1/p47 (same May 2020 non-intermodal value).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p18 Canada railway carloadings: non-intermodal traffic loaded, monthly total (Apr 20 = **24,371,149** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "This records an increase from the previous number of 24,371,149.000 Tonne for Apr 2020."
  - p19 Canada railway carloadings: non-intermodal traffic loaded, all-time monthly high = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [DISCARD: Duplicate of p2/p49 (Oct 2018 high).] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p20 Canada railway carloadings: non-intermodal traffic loaded, record monthly low (J = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [DISCARD: Duplicate of p3/p50 (Jul 2009 low).] quote: "and a record low of 16,818,939.000 Tonne in Jul 2009"
  - p21 Canada railway carloadings: non-intermodal traffic loaded, monthly average Jan 1 = **21,490,478** metric tonnes (1999-01-01..2020-05-31) [DISCARD: Duplicate of p4/p51 (1999-2020 average).] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p22 Canada railway carloadings: intermodal traffic loaded, monthly average Jan 1999- = **2,381,505** metric tonnes (1999-01-01..2020-05-31) [DISCARD: Duplicate of p46 (intermodal long-run average).] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p23 Canada railway carloadings: intermodal traffic loaded, all-time monthly high (Ma = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [DISCARD: Duplicate of p6/p45 (May 2019 intermodal high).] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p24 Canada railway carloadings: intermodal traffic loaded, record monthly low (Jan 1 = **1,264,980** metric tonnes (1999-01-01..1999-01-31) [DISCARD: Intermodal record low Jan 1999; not in the kept table and not needed for any route.] quote: "and a record low of 1,264,980.000 Tonne in Jan 1999"
  - p25 Canada railway carloadings: non-intermodal cement, all-time monthly high (Jul 20 = **361,023** metric tonnes (2019-07-01..2019-07-31) [DISCARD: Duplicate of p12/p53 (cement July 2019 high).] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p26 Canada railway carloadings: non-intermodal cement, monthly total (May 2020) = **247,356** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p11/p52 (cement May 2020).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p27 Canada railway carloadings: non-intermodal animal feed & products, monthly total = **409,186** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p9/p54 (animal feed May 2020).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p28 Canada railway carloadings: non-intermodal alumina, monthly total (May 2020) = **126,378** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p7/p56 (alumina May 2020).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p29 Canada railway carloadings: non-intermodal aluminum, monthly total (May 2020) = **291,832** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p8/p57 (aluminum May 2020).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p30 Canada railway carloadings: non-intermodal automobiles & mini-vans, monthly tota = **20,703** metric tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p14 (automobiles May 2020).] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."

### d6 [shocks] Disruptions, weather, strikes, tariffs

Hypothesis: July 2026 tonnage may deviate from seasonal norms due to strikes, wildfires, port disruptions, tariffs or trade policy; measurable exposure (days lost, affected corridors) adjusts the baseline estimate.

Queries issued by the searcher: Canada rail strike July 2026 CN CPKC disruption; wildfire rail closure Canada July 2026 CN CPKC; Teamsters Canada Rail Conference strike July 2026 CIRB decision CN CPKC; CN rail mainline north of Lake Superior reopened wildfire July 2026 service recovery

- `https://www.portvancouver.com/article/port-vancouver-operations-update-1-wildfire-near-boston-bar-british-columbia` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ca.one-line.com/news/all-news/2026/07` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.theglobeandmail.com/business/article-northern-ontario-wildfires-disrupt-rail-forestry-operations/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cbc.ca/lite/story/9.7274475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Industry forecasts and trade outlook

Hypothesis: Published freight or trade forecasts for 2026 and commodity export outlooks constrain the plausible range of July 2026 tonnage relative to 2025.

Queries issued by the searcher: Canada rail freight forecast 2026; grain production 2026 Canada outlook; potash exports 2026 forecast Canada; Railway Association of Canada 2026 outlook grain potash coal rail volumes; CN rail Q2 2026 earnings guidance low single digit RTM growth July 24 2026; CPKC 2026 volume guidance July 2026; Canada coal production exports forecast 2026

- `https://in.marketscreener.com/news/cn-raises-2026-volume-outlook-as-2q-profit-revenue-rise-ce7f51dfdc8df121` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://agriculture.canada.ca/sites/default/files/documents/2026-05/Canada%20Outlook%20for%20Principal%20Field%20Crops_202605.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fas.usda.gov/data/gain/2026/04/canada-grain-and-feed-annual` -> **snapshot** (snapshot 20260430101704); points raw/verified 5/0
- `https://www.railcan.ca/wp-content/uploads/2026/03/2025_Q4_RAC_Quarterly_Report_FR_v2.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period_end 2027-07-31 after as_of: 3; scale word 'million' not supported by quote or table header: 2)

### d8 [base_rates] Conversion ratios and coverage

Hypothesis: If only car counts or ton-km are available, total tonnage can be recovered using average tonnes per car or tonnes per revenue ton-km; the coverage ratio between the survey universe and total Canadian rail traffic is needed.

Queries issued by the searcher: Statistics Canada railway carloadings methodology average tonnes per car; average tonnes per carload Canada railway statistics commodity; RAC rail trends 2025 carloads originated and tonnage commodity group average tonnes per carload; Statistics Canada table 23-10-0016-01 railway carloadings number of cars tonnes by commodity

- `https://publications.gc.ca/collections/Collection-R/Statcan/52-216-XIB/0009752-216-XIB.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/pub/52-001-x/2013004/part-partie3-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-eng.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ctrf.ca/wp-content/uploads/2014/07/17JacquesKarangwaMeasuringFreightProduction.pdf` -> **snapshot** (snapshot 20250815195831); points raw/verified 15/12
  - p31 Class 1 rail network cargo weight limit per railcar (lower bound) = **75** tonnes per railcar (..) [keep: ] quote: "Knowing that most of Class 1 rail networks impose a cargo weight limit of between 75 to 85 tonnes per railcars6"
  - p32 Class 1 rail network cargo weight limit per railcar (upper bound) = **85** tonnes per railcar (..) [keep: ] quote: "Knowing that most of Class 1 rail networks impose a cargo weight limit of between 75 to 85 tonnes per railcars6"
  - p33 Share of loaded railcars with average weight smaller than 20 t, Canada 2000-2009 = **40** % (2000-01-01..2009-12-31) [keep: ] quote: "close to 40% of loaded railcars had an average weight smaller than 20 t"
  - p34 Share of railcar movements with average weight less than 70 t, Canada 2000-2009 = **62** % (2000-01-01..2009-12-31) [keep: ] quote: "62% of railcar movements had an average weight of less than 70 t"
  - p35 Share of rail tonnage carried by volume-constrained railcars, Canada 2000-2009 = **29** % (2000-01-01..2009-12-31) [keep: ] quote: "these volume-constrained railcars carried only 29% of the rail tonnage during that decade"
  - p36 Share of railcar movements that were volume-constrained, Canada 2000-2009 = **60** % (2000-01-01..2009-12-31) [keep: ] quote: "more than 60% of the railcar movements were volume-constrained"
  - p37 Container share of railcar movements, Canada 2000-2009 = **48.8** % (2000-01-01..2009-12-31) [keep: ] quote: "Container 48.8% 14.7%"
  - p38 Container share of rail tonnage, Canada 2000-2009 = **14.7** % (2000-01-01..2009-12-31) [keep: ] quote: "Container 48.8% 14.7%"
  - p39 Covered hopper share of railcar movements, Canada 2000-2009 = **16.8** % (2000-01-01..2009-12-31) [keep: ] quote: "Covered Hopper 16.8% 31.0%"
  - p40 Covered hopper share of rail tonnage, Canada 2000-2009 = **31** % (2000-01-01..2009-12-31) [keep: ] quote: "Covered Hopper 16.8% 31.0%"
  - p41 Gondola share of rail tonnage, Canada 2000-2009 = **28.4** % (2000-01-01..2009-12-31) [keep: ] quote: "Gondola 13.8% 28.4%"
  - p42 Tank car share of rail tonnage, Canada 2000-2009 = **10.7** % (2000-01-01..2009-12-31) [keep: ] quote: "Tank 6.6% 10.7%"
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; scale word 'billion' not supported by quote or table header: 2)

### b1 [own_history] Statistics Canada Railway carloadings monthly table

Hypothesis: A recent (2024-2025) published monthly total-traffic tonnage series would anchor the July 2026 level via seasonal July ratio and YoY trend, replacing the stale 2020 CEIC snapshot as the base.

Queries issued by the searcher: Statistics Canada railway carloadings total traffic carried tonnes monthly 23-10-0219-01; Statistics Canada Table 23-10-0219-01 railway carloadings by commodity total tonnage Canada 2025; "Chargements ferroviaires, juillet 2025" millions de tonnes Statistique Canada; Statistics Canada "Railway carloadings, July 2025" million tonnes total freight

- `https://www150.statcan.gc.ca/n1/daily-quotidien/250924/dq250924f-fra.htm` -> **snapshot** (snapshot 20251010112647) **LEAK SENTINEL HIT ['3,2 millions (read as 3.2e+06)'] (excluded)**; points raw/verified 14/0
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-fra.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/251024/dq251024c-fra.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2310021601` -> **snapshot** (snapshot 20260313212755); points raw/verified 0/0
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b2 [related_series] Commodity-level July tonnage

Hypothesis: Summing July 2025/2026 tonnages for grain, coal, potash, forest products, chemicals and intermodal plus residual would give a bottom-up total and cross-check the top-down seasonal route.

Queries issued by the searcher: Statistics Canada railway carloadings July 2025 tonnes by commodity; railway carloadings by commodity tonnes Canada monthly grain coal potash intermodal; "Railway carloadings" June 2026 The Daily Statistics Canada; table 23-10-0216-01 railway carloadings by commodity tonnes Canada

- `https://tdih-cdit.tc.canada.ca/en/search/23100216` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p43 Canada railway carloadings: Intermodal traffic loaded, total tonnage, May 2020 = **3,040,663** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p44 Canada railway carloadings: Intermodal traffic loaded, total tonnage, Apr 2020 = **3,087,415** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "This records a decrease from the previous number of 3,087,415.000 Tonne for Apr 2020."
  - p45 Canada railway carloadings: Intermodal traffic loaded, all-time high monthly ton = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p46 Canada railway carloadings: Intermodal traffic loaded, monthly average Jan 1999- = **2,381,505** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p47 Canada railway carloadings: Non-intermodal traffic loaded, total tonnage, May 20 = **24,396,926** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p48 Canada railway carloadings: Non-intermodal traffic loaded, total tonnage, Apr 20 = **24,371,149** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "This records an increase from the previous number of 24,371,149.000 Tonne for Apr 2020."
  - p49 Canada railway carloadings: Non-intermodal traffic loaded, all-time high monthly = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p50 Canada railway carloadings: Non-intermodal traffic loaded, record low monthly to = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [keep: ] quote: "a record low of 16,818,939.000 Tonne in Jul 2009"
  - p51 Canada railway carloadings: Non-intermodal traffic loaded, monthly average Jan 1 = **21,490,478** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p52 Canada railway carloadings: Non-intermodal cement tonnage, May 2020 = **247,356** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p53 Canada railway carloadings: Non-intermodal cement tonnage, all-time high monthly = **361,023** metric tonnes (2019-07-01..2019-07-31) [keep: ] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p54 Canada railway carloadings: Non-intermodal animal feed & products tonnage, May 2 = **409,186** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p55 Canada railway carloadings: Non-intermodal animal or vegetable fats, oils & flou = **414,481** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p56 Canada railway carloadings: Non-intermodal alumina tonnage, May 2020 = **126,378** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p57 Canada railway carloadings: Non-intermodal aluminum tonnage, May 2020 = **291,832** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/cg-c001-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] 2026 operational disruptions

Hypothesis: Strikes, wildfires, port or tariff disruptions in July 2026 would shift tonnage from the seasonal baseline; quantifying affected days/corridors would set the shock adjustment factor.

Queries issued by the searcher: Canada rail strike 2026; wildfire rail disruption Canada July 2026; CN resumes service Boston Bar Fraser Canyon rail July 2026 wildfire reopened; Statistics Canada railway carloadings July 2025 total tonnage million tonnes

- `https://www.portvancouver.com/article/port-vancouver-operations-update-1-wildfire-near-boston-bar-british-columbia` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bisontransport.com/customer-advisory/customer-advisory-cn-rail-service-disruption-in-northwestern-ontario` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tsb-bst.gc.ca/eng/enquetes-investigations/rail/2026/r26t0219/r26t0219.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://iamovers.org/news/b-c-wildfires-keep-pressure-on-rail-corridor/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['railway carloadings', 'canada freight tonnes', 'statcan rail']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p17'] Same May 2020 non-intermodal total (24,396,926 t) reported twice; identical underlying StatCan measurement, not independent.
- corroborating: ['p5', 'p16'] Same May 2020 intermodal total (3,040,663 t); duplicate of one source.
- corroborating: ['p2', 'p19'] Same Oct 2018 all-time high non-intermodal total; duplicate.
- corroborating: ['p3', 'p20'] Same Jul 2009 record low non-intermodal total; duplicate.
- corroborating: ['p4', 'p21'] Same Jan1999-May2020 non-intermodal monthly average; duplicate.
- corroborating: ['p6', 'p23'] Same May 2019 intermodal all-time high; duplicate.
- corroborating: ['p7', 'p28'] Same May 2020 alumina value; duplicate.
- corroborating: ['p8', 'p29'] Same May 2020 aluminum value; duplicate.
- corroborating: ['p9', 'p27'] Same May 2020 animal feed value; duplicate.
- corroborating: ['p11', 'p26'] Same May 2020 cement value; duplicate.
- corroborating: ['p12', 'p25'] Same Jul 2019 cement all-time high; duplicate.
- corroborating: ['p14', 'p30'] Same May 2020 automobiles value; duplicate.
- corroborating: ['p1', 'p5'] Non-intermodal plus intermodal are complementary components of total traffic; together they define the headline total scope.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Car payload limits and load-weight distribution describe the same carload capacity structure; consistent with average payload well below the 75-85 t ceiling.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42'] Car-type shares of movements and tonnage from one study; internally consistent (containers many movements, low tonnage share; hoppers/gondolas high tonnage share).
- conflicting: ['p1', 'p4'] May 2020 (24.4 Mt) is above the 1999-2020 average (21.5 Mt) but the average spans a different period; not a true contradiction, just different reference windows.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p47', 'p18', 'p48'] Same CEIC/StatCan non-intermodal monthly total series; p1 and p47 are duplicate copies of May 2020, p18/p48 duplicate April 2020. They establish the 2020 level (~24.4 Mt/month non-intermodal) but are 
- corroborating: ['p5', 'p43', 'p44', 'p46'] Intermodal series: p5/p43 duplicate May 2020 (3.04 Mt), p44 April 2020, p46 long-run average. Same source; establishes intermodal is roughly 11-12% of total tonnage.
- corroborating: ['p2', 'p49', 'p4', 'p51', 'p3', 'p50'] Non-intermodal high (Oct 2018, 28.26 Mt), low (Jul 2009, 16.82 Mt) and 1999-2020 average (21.49 Mt) all describe the same series and bracket a plausible July level; they are bounds/context, not separa
- corroborating: ['p12', 'p53', 'p11', 'p52'] Cement: May 2020 level and July 2019 all-time high; a small commodity (~0.25-0.36 Mt) that shows July can exceed May for construction-linked commodities, supporting a July/May ratio above 1.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42'] All from one CTRF analysis of 2000-2009 carload data: weight limits 75-85 t, many light/volume-constrained cars, container 14.7% of tonnage. Consistent internally but a single source and a stale decad
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p13', 'p14', 'p15', 'p56', 'p57', 'p54', 'p55'] Small non-intermodal commodity components for May 2020; each is a few hundred thousand tonnes or less, confirming that the headline total is dominated by a handful of large bulk commodities not itemiz

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July-to-May seasonal ratio for total traffic | 1.05 | 0.95..1.18 | 0.7487..1.497 (widened) | ratio | m2 (m3) | July is peak grain/potash/construction season; cement July 2019 high (p12) exceeds May 2020 (p11), and the 1999-2020 mean (p4) sits between the July 2009 low and October 2018 high, implying July is typically near or slightly above the annual mean. May 2020 was COVID-depressed, so July/May should be  | The May 2020 base is representative of a normal May after adjusting for the 2026 level factor. | Evidence that July tonnage is systematically below May in recent years, or that May 2020 was not depressed relative to July. |
| a2 | 2026 level factor vs 2020 total traffic | 1.08 | 0.92..1.25 | 0.7583..1.517 (widened) | ratio | m2 (m3) | Canadian rail tonnage grew from the 2020 COVID trough; the 1999-2020 mean (p4) and 2018 high (p2) bracket a recovery. A modest factor above 1 reflects post-2020 recovery plus grain/potash growth, tempered by tariff and wildfire risk in 2026. | 2026 traffic is broadly comparable in scope to the 2020 CEIC series (all traffic, Canada). | Published 2024-2026 totals showing tonnage flat or below 2020 levels. |
| a3 | Average tonnes per loaded car | 68 | 55..80 | 46.9..93.81 (widened) | tonnes per car | m1 (m2) | CTRF weight limits are 75-85 t (p31, p32) but 62% of movements are under 70 t (p34) and 60% are volume-constrained (p36); a tonnage-weighted average near 68 t is consistent with bulk hoppers/gondolas dominating tonnage (p40, p41) while light cars dominate counts. | Applied to loaded car counts for all traffic. | Operator data showing average payload materially outside 55-80 t. |
| a4 | Loaded cars per month (all traffic) | 380,000 | 300,000..460,000 | 262,679..525,357 (widened) | cars per month | m1 (m2) | Canadian Class 1 railways load on the order of 350-400k cars per month across all traffic; scaled from typical weekly loadings (~85-95k) times ~4.3 weeks, with a wide range for seasonal and shock variation. | Used as a capacity-utilisation cross-check on the tonnage total. | Published monthly loaded car counts outside 300-460k. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 24,524,434 | ['p1', 'p5'] / ['a3', 'a4'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 31,139,613 | ['p1', 'p5'] / ['a1', 'a2'] | [] |  | 0.50 | equal |  |

Result: central **27,634,786** t, 80% interval [16,413,249, 46,528,349] t, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total freight carried by Canadian railways (all traffic, Canada, freight only) in July 2026, as first reported by Statistics Canada in the monthly Railway carloadings release: 27,634,786 t (80% model-based interval 16,413,249 to 46,528,349 t).

Two methods were combined with equal weight (50% and 50%). The top-down route (31,139,613 t) sums observed May 2020 non-intermodal (24,396,926 metric tonnes) and intermodal (3,040,663 metric tonnes) tonnages, scaled by a July-to-May seasonal ratio (1.05) and a 2026 level factor (1.08). The capacity cross-check (24,524,434 t) multiplies average payload (68) by monthly loaded cars (380,000).

Only the May 2020 points are observed; the seasonal ratio, level factor, payload and car counts are analyst assumptions, so the interval reflects input uncertainty, not demonstrated accuracy. The biggest risk is that the 2020 base is COVID-depressed and the scaling factors are unmeasured. Actual 2026 monthly loadings and payload data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July-to-May seasonal ratio for total traffic: 1.05 ratio, range 0.7487 to 1.497 (range widened by code); used by m2. Overturned by: Evidence that July tonnage is systematically below May in recent years, or that May 2020 was not depressed relative to July.
- a2 2026 level factor vs 2020 total traffic: 1.08 ratio, range 0.7583 to 1.517 (range widened by code); used by m2. Overturned by: Published 2024-2026 totals showing tonnage flat or below 2020 levels.
- a3 Average tonnes per loaded car: 68 tonnes per car, range 46.9 to 93.81 (range widened by code); used by m1. Overturned by: Operator data showing average payload materially outside [n]-[n] t.
- a4 Loaded cars per month (all traffic): 380,000 cars per month, range 262,679 to 525,357 (range widened by code); used by m1. Overturned by: Published monthly loaded car counts outside [n]-[n]k.

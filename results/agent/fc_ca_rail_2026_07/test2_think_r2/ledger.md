# Evidence ledger: fc_ca_rail_2026_07

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the total freight carried by Canadian railways in July 2026, in tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total traffic carried, Canada).
- as_of: 2026-08-29
- Pinned target: Total tonnage of freight carried by Canadian railways in Canada during July 2026, as first reported by Statistics Canada in its monthly Railway carloadings release under total traffic carried. | unit metric tonnes | period 2026-07-01..2026-07-31 | publisher Statistics Canada

- Official value (scoring only, never shown to the agent): 31,686,803

## Directions and pages

### d1 [own_history] Statistics Canada time-series analyst

Hypothesis: July total tonnes has a recurring seasonal structure and a recent trend; July values from earlier years plus the latest published 2025-2026 monthly values can anchor a baseline. Symbolically, T_Jul2026 is inferred from the July seasonal level and the recent year-over-year run-rate, adjusted for known shocks.

Queries issued by the searcher: Statistics Canada railway carloadings total traffic carried tonnes July 2025; Table 23-10-0218 railway carloadings total traffic carried tonnes monthly; "Railway carloadings, June 2026" Statistics Canada daily; Statistics Canada Table 23-10-0216 railway carloadings total traffic carried tonnes

- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/en/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/11027/11030-railway-carloadings-april-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tdih-cdit.tc.canada.ca/fr/search/23100216` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] commodity supply-chain analyst

Hypothesis: Total rail tonnage is the sum of major commodity groups such as coal, grain, potash, crude oil, forest products, chemicals, intermodal, and other. Prior-year July commodity tonnages plus current production, export, and harvest signals can estimate each component and reduce reliance on a single aggregate trend.

Queries issued by the searcher: Statistics Canada railway carloadings by commodity tonnes July 2025; Canada rail shipments coal grain potash July 2026; Statistics Canada Table 23-10-0216-01 railway carloadings tonnage by commodity coal potash wheat July 2025; Port of Vancouver July 2026 grain potash coal rail volumes monthly statistics

- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/resources/traffic-dashboard/` -> **snapshot** (snapshot 20260826130548); points raw/verified 15/14
  - p1 Canadian Class 1 (CN and CPKC) network-wide carloads, week 32 of 2026 (August 9- = **7** % (2026-08-09..2026-08-15) [keep: ] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p2 Canadian Class 1 (CN and CPKC) network-wide revenue ton-miles (RTMs), week 32 of = **13** % (2026-08-09..2026-08-15) [keep: ] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p3 Canadian Class 1 carloads of grains & fertilizers (incl. potash), week 32 of 202 = **24** % (2026-08-09..2026-08-15) [keep: ] quote: "North American networks, carloads increased in grains & fertilizers by a marked 24%, as well as in intermodal; metals and minerals (+11%); energy, chemicals and plastics; and forest products, while de"
  - p4 Canadian Class 1 carloads of metals and minerals, week 32 of 2026, year-over-yea = **11** % (2026-08-09..2026-08-15) [keep: ] quote: "increased in grains & fertilizers by a marked 24%, as well as in intermodal; metals and minerals (+11%); energy, chemicals and plastics; and forest products, while decreasing for coal; and automotive."
  - p5 Canadian Class 1 RTMs of grains & fertilizers, week 32 of 2026, year-over-year c = **29** % (2026-08-09..2026-08-15) [keep: ] quote: "RTMs of grain & fertilizers increased significantly, by 29%, while RTMs also increased in all commodities except for coal."
  - p6 Canadian Class 1 network-wide RTMs, first 32 weeks of 2026, year-over-year chang = **4** % (2026-01-01..2026-08-15) [keep: ] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p7 Canadian Class 1 network-wide carloads, first 32 weeks of 2026, year-over-year c = **21,738** carloads (2026-01-01..2026-08-15) [keep: ] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p8 Canadian Class 1 network-wide RTMs, first 32 weeks of 2026, year-over-year chang = **11,687,000,000** RTMs (2026-01-01..2026-08-15) [keep: ] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p9 Canadian Class 1 carloads of grains & fertilizers, first 32 weeks of 2026, year- = **98,516** carloads (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p10 Canadian Class 1 carloads of grains & fertilizers, first 32 weeks of 2026, year- = **11** % (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p11 Canadian Class 1 RTMs of grains & fertilizers, first 32 weeks of 2026, year-over = **11,822,000,000** RTMs (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p12 Canadian Class 1 RTMs of grains & fertilizers, first 32 weeks of 2026, year-over = **13** % (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p13 Canadian Class 1 carloads of metals and minerals, first 32 weeks of 2026, year-o = **1** % (2026-01-01..2026-08-15) [keep: ] quote: "Carloads of metals and minerals are up 1% on a year-to-date basis while RTMs are relatively flat."
  - p14 CN and CPKC Canadian grain and grain products moved, 2025-2026 crop year (August = **64,000,000** metric tonnes (2025-08-01..2026-07-31) [keep: ] quote: "In the 2025-2026 crop year (August 2025 - July 2026), CN and CPKC moved 64.0 million metric tonnes of Canadian grain and grain products - 15% higher than the previous 3-year average."
- `https://tdih-cdit.tc.canada.ca/en/search/23100216` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.trains.com/pro/freight/class-i/cn-boosts-outlook-as-volume-growth-tops-expectations/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### d3 [related_series] CN and CPKC investor-relations analyst

Hypothesis: CN and CPKC carry most Canadian rail freight and report carloads and revenue ton-miles. Their Canadian traffic plus an allowance for shortlines and other carriers can bridge to Canada total; revenue ton-miles divided by average length of haul gives tonnage, while carloads times average tonnes per carload gives a cross-check.

Queries issued by the searcher: CN Rail July 2026 carloads revenue ton-miles; CPKC July 2026 carloads revenue ton-miles; CN key weekly metrics July 2026 revenue ton-miles carloads week; Statistics Canada Railway carloadings July 2026 total traffic carried metric tonnes

- `https://investor.cpkcr.com/key-metrics/default.aspx` -> **snapshot** (snapshot 20250916012815); points raw/verified 0/0
- `https://ecprod.cn.ca/corp/en/news/2026/07/cn-delivers-on-commitments-with-strong-second-quarter-results-an/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stockhouse.com/news/press-releases/2026/07/29/cpkc-reports-strong-q2-results-poised-for-accelerated-growth-in-second-half-of` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecprod.cn.ca/corp/en/investors/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] port and export logistics analyst

Hypothesis: A large share of Canadian rail freight is export-bound. Port throughput for coal, grain, potash, crude, and containers, divided by rail's share of inland transport and adjusted for non-port destinations and U.S. routing, can constrain export-related rail tonnage; domestic traffic is added separately.

Queries issued by the searcher: Port of Vancouver July 2026 cargo statistics rail; Prince Rupert grain coal exports July 2026; Thunder Bay port grain shipments July 2026; Statistics Canada Railway carloadings July 2026 total traffic carried metric tonnes

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://maritimemag.com/en/port-of-thunder-bay-posts-strong-july-cargo-results/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://coal.mysteel.com/a/26082609/A849CD92468EF9A5.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4040000201` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] rail operations analyst

Hypothesis: Total tonnes equals total carloads times average tonnes per carload. Total carloads can be estimated from historical July carloads adjusted for current activity, and average tonnes per carload from the commodity mix; this provides an independent check on aggregate tonnage.

Queries issued by the searcher: Statistics Canada railway carloadings total carloads July 2025; average tonnes per railcar Canada commodity Statistics Canada carloadings; Railway Association of Canada Rail Trends 2025 carloads tonnes per commodity group table; Statistics Canada table 23-10-0216 railway carloadings number of rail cars total tonnes July

- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p15 Canada railway intermodal traffic loaded, total tonnes, May 2020 = **3,040,663** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p16 Canada railway non-intermodal traffic loaded, total tonnes, May 2020 = **24,396,926** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p17 Canada railway non-intermodal traffic loaded, monthly average tonnes Jan 1999-Ma = **21,490,478** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p18 Canada railway non-intermodal traffic loaded, record low tonnes, July 2009 = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [keep: ] quote: "a record low of 16,818,939.000 Tonne in Jul 2009"
  - p19 Canada railway non-intermodal traffic loaded, record high tonnes, October 2018 = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p20 Canada railway intermodal traffic loaded, monthly average tonnes Jan 1999-May 20 = **2,381,505** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p21 Canada railway intermodal traffic loaded, record high tonnes, May 2019 = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p22 Canada railway intermodal traffic loaded, record low tonnes, January 1999 = **1,264,980** metric tonnes (1999-01-01..1999-01-31) [keep: ] quote: "a record low of 1,264,980.000 Tonne in Jan 1999"
  - p23 Canada railway non-intermodal cement tonnes, record high, July 2019 = **361,023** metric tonnes (2019-07-01..2019-07-31) [DISCARD: May 2020 cement detail/record high is too granular and not used for the aggregate target.] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p24 Canada railway non-intermodal cement tonnes, May 2020 = **247,356** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p25 Canada railway non-intermodal animal feed & products tonnes, May 2020 = **409,186** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p26 Canada railway non-intermodal animal or vegetable fats, oils & flours tonnes, Ma = **414,481** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p27 Canada railway non-intermodal aluminum tonnes, May 2020 = **291,832** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p28 Canada railway non-intermodal alumina tonnes, May 2020 = **126,378** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p29 Canada railway non-intermodal automobiles & mini-vans tonnes, May 2020 = **20,703** metric tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 commodity detail too granular for the aggregate estimate and not used.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3ACanola&23100216_facets%5B1%5D=23100216_co` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/wp-content/uploads/2026/01/2025_Q3_RAC_Quarterly_Report_EN_v1.pdf` -> **snapshot** (snapshot 20260417085253); points raw/verified 15/9
  - p30 Canadian Railways intermodal units, July 2025 (thousands of units) = **208,000** intermodal units (2025-07-01..2025-07-31) [keep: ] quote: "181 165 190 184 207 192 156 195 187 177 187 207 210 208 192 190 169 191 198 168 219 215 223 209 211 207 201 0 50 100 150 200 250 Intermodal Units (thousands)"
  - p31 Canadian Railways intermodal units, July 2024 (thousands of units) = **192,000** intermodal units (2024-07-01..2024-07-31) [keep: ] quote: "181 165 190 184 207 192 156 195 187 177 187 207 210 208 192 190 169 191 198 168 219 215 223 209 211 207 201 0 50 100 150 200 250 Intermodal Units (thousands)"
  - p32 Canadian Railways intermodal units, July 2023 (thousands of units) = **195,000** intermodal units (2023-07-01..2023-07-31) [keep: ] quote: "181 165 190 184 207 192 156 195 187 177 187 207 210 208 192 190 169 191 198 168 219 215 223 209 211 207 201 0 50 100 150 200 250 Intermodal Units (thousands)"
  - p33 Canadian Class 1 average train weight, Q3-2025 (tons) = **9,262** tons per train (2025-07-01..2025-09-30) [keep: ] quote: "9,143 9,262 Train weight (Tons) 1% Favourable"
  - p34 Canadian Class 1 average train weight, Q3-2024 (tons) = **9,143** tons per train (2024-07-01..2024-09-30) [keep: ] quote: "9,143 9,262 Train weight (Tons) 1% Favourable"
  - p35 Canadian Class 1 average train length, Q3-2025 (feet) = **7,995** feet per train (2025-07-01..2025-09-30) [keep: ] quote: "7,835 7,995 Train length (feet) 2% Favourable"
  - p36 Canadian Class 1 cars on line, Q3-2025 (thousands of cars) = **168,000** rail cars on line (2025-07-01..2025-09-30) [keep: ] quote: "167 168 Cars on line (thousands) No change"
  - p37 Canadian Class 1 cars on line, Q3-2024 (thousands of cars) = **167,000** rail cars on line (2024-07-01..2024-09-30) [keep: ] quote: "167 168 Cars on line (thousands) No change"
  - p38 Canadian Class 1 total RTMs, Q3-2025 (millions of revenue ton-miles) = **111,388,000,000** revenue ton-miles (2025-07-01..2025-09-30) [keep: ] quote: "Total 111,388 108,068 3% 3,320"
- dropped by code checks: 6 (value_as_written not in quote as a whole number: 6)

### d6 [related_series] macro nowcast analyst

Hypothesis: Rail tonnage co-moves with industrial production, manufacturing shipments, merchandise exports, retail/wholesale inventories, energy output, and grain harvest conditions. July 2026 macro and trade indicators can adjust the historical July seasonal baseline up or down.

Queries issued by the searcher: Statistics Canada Railway carloadings July 2026 total tonnage; Canada manufacturing shipments July 2026 Statistics Canada; Statistics Canada GDP July 2026 advance estimate industrial production; Canada merchandise exports July 2026 Statistics Canada trade balance

- `https://www.ceicdata.com.cn/en/canada/railway-carloadings` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://in.marketscreener.com/news/canada-factory-sales-estimated-down-slightly-in-july-after-five-straight-months-of-growth-ce7858dbda80f727` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradersunion.com/news/financial-news/show/3543020-canadian-rail-freight-july-rise/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/searchindicators?title=Chargements+ferroviaires,+tonnage+total&wbdisable=true` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] rail risk analyst

Hypothesis: July 2026 may include disruptions or calendar effects that shift tonnage from the seasonal baseline, such as wildfires, labour actions, port closures, track outages, tariffs, or harvest timing. Measurable duration and affected traffic can constrain the adjustment.

Queries issued by the searcher: Canada railway strike July 2026; wildfire rail disruption Canada July 2026; Statistics Canada Railway carloadings July 2026 total traffic carried metric tonnes; CN rail strike July 2026 duration tonnage impact grain shipments

- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/searchindicators?title=Chargements+ferroviaires,+tonnage+total&wbdisable=true` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.portvancouver.com/article/port-vancouver-operations-update-1-wildfire-near-boston-bar-british-columbia` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cbc.ca/lite/story/9.7274475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cargopress.co.kr/korean/news_view.php?nd=4848` -> **snapshot** (snapshot 20250118094519); points raw/verified 6/0
- dropped by code checks: 6 (period_end missing or unparseable: 4; period year 2026 does not appear in the page text or URL (likely mis-dated): 2)

### d8 [forecasts_markets] industry forecast analyst

Hypothesis: Published 2026 Canadian rail-volume forecasts or company guidance, multiplied by July's historical share of annual tonnage, can provide a top-down constraint. This is weaker than direct history but useful for bounding the estimate.

Queries issued by the searcher: Canada rail freight forecast 2026 tonnes carloads; Railway Association of Canada 2026 outlook freight volumes; CN Rail Q2 2026 earnings guidance revenue ton miles full year 2026 outlook; CPKC second quarter 2026 results guidance carloads revenue ton-miles full year

- `https://www.insidelogistics.ca/economic-performance/cn-raises-2026-guidance-after-second-quarter-revenue-earnings-growth/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2310021601` -> **snapshot** (snapshot 20260313212755); points raw/verified 0/0
- `https://www.railcan.ca/resources/traffic-dashboard/` -> **snapshot** (snapshot 20260826130548); points raw/verified 15/14
  - p39 CN and CPKC Canadian grain and grain products moved, 2025-2026 crop year (August = **64,000,000** metric tonnes (2025-08-01..2026-07-31) [DISCARD: Duplicate of p14; same grain crop-year total with no additional information.] quote: "In the 2025-2026 crop year (August 2025 - July 2026), CN and CPKC moved 64.0 million metric tonnes of Canadian grain and grain products - 15% higher than the previous 3-year average."
  - p40 CN and CPKC Canadian grain and grain products moved, week 1 of 2026-2027 crop ye = **1,100,000** metric tonnes (2026-08-02..2026-08-08) [keep: ] quote: "In week 1 (August 2 - August 8) of the 2026-2027 crop year, CN and CPKC moved nearly 1.1 million metric tonnes of Canadian grain and grain products."
  - p41 Crop year-to-date grain volumes (2 week), CN and CPKC = **2,200,000** metric tonnes (2026-08-02..2026-08-15) [keep: ] quote: "Crop year-to-date grain volumes (2 week) 2.2 million metric tonnes \| +49% vs previous 3-year average"
  - p42 Canadian Class 1 (CN and CPKC) network-wide carloads change, week 32 of 2026 vs  = **7** % (2026-08-09..2026-08-15) [DISCARD: Redundant copy of p1.] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p43 Canadian Class 1 (CN and CPKC) network-wide RTMs change, week 32 of 2026 vs same = **13** % (2026-08-09..2026-08-15) [DISCARD: Redundant copy of p2.] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p44 Canadian Class 1 network-wide RTMs change, first 32 weeks of 2026 vs same period = **4** % (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p6.] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p45 Canadian Class 1 network-wide carloads change, first 32 weeks of 2026 vs same pe = **21,738** carloads (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p7.] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p46 Canadian Class 1 network-wide RTMs change, first 32 weeks of 2026 vs same period = **11,687,000,000** RTMs (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p8.] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025 (+21,738 carloads and +11,687 million RTMs)."
  - p47 Grain & fertilizers carloads change, first 32 weeks of 2026 vs same period 2025  = **98,516** carloads (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p9.] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p48 Grain & fertilizers carloads change, first 32 weeks of 2026 vs same period 2025  = **11** % (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p10.] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p49 Grain & fertilizers RTMs change, first 32 weeks of 2026 vs same period 2025 (abs = **11,822,000,000** RTMs (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p11.] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p50 Grain & fertilizers RTMs change, first 32 weeks of 2026 vs same period 2025 (per = **13** % (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p12.] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%), followed by energy, chemicals and plastics."
  - p51 Metals and minerals carloads change, first 32 weeks of 2026 vs same period 2025 = **1** % (2026-01-01..2026-08-15) [DISCARD: Redundant copy of p13.] quote: "Carloads of metals and minerals are up 1% on a year-to-date basis while RTMs are relatively flat."
  - p52 Grain & fertilizers carloads change, week 32 of 2026 vs same week 2025 (North Am = **24** % (2026-08-09..2026-08-15) [DISCARD: Redundant copy of p3.] quote: "North American networks, carloads increased in grains & fertilizers by a marked 24%, as well as in intermodal; metals and minerals (+11%); energy, chemicals and plastics; and forest products, while de"
- `https://www.railcan.ca/wp-content/uploads/2026/07/2026_Q1_RAC_Quarterly_Report_FR_v1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### b1 [own_history] Statistics Canada Table 23-10-0069 and The Daily railway carloadings releases

Hypothesis: Direct July total traffic carried values for earlier years would provide a true target_history for series_naive and calibrate the level/seasonality. This is the largest missing input because no kept point is both the exact total-carried concept and the July calendar period, forcing the May 2020-to-July 2026 adjustment assumptions a1/a2/a7 to carry most uncertainty.

Queries issued by the searcher: Statistics Canada railway carloadings July 2025 total traffic carried metric tonnes; "railway carloadings" The Daily Statistics Canada July 2024 "total traffic carried"; ceicdata Canada Railway Carloadings Total Traffic Carried 2026-07 tonnes; "Total traffic carried" Canada "2025-07" tonnes tdih-cdit monthly railway car loadings

- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/240920/dq240920c-eng.htm?indid=3668-1&indgeo=0` -> **snapshot** (snapshot 20250908054139); points raw/verified 15/14
  - p53 Total freight carried by Canadian railways, Canada, July 2024 = **29,900,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "In July, Canadian railways transported 29.9 million tonnes of freight, up 1.6% from July 2023"
  - p54 Year-over-year change in total freight carried, Canada, July 2024 vs July 2023 = **1.6** % (2024-07-01..2024-07-31) [keep: ] quote: "transported 29.9 million tonnes of freight, up 1.6% from July 2023"
  - p55 Intermodal shipments (mainly containers) originating in Canada, July 2024 = **2,800,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "rising sharply by 19.2% year over year to 2.8 million tonnes"
  - p56 Year-over-year change in intermodal shipments originating in Canada, July 2024 = **19.2** % (2024-07-01..2024-07-31) [keep: ] quote: "intermodal shipments (mainly containers) originating in Canada led the overall increase in rail freight, rising sharply by 19.2% year over year"
  - p57 Freight traffic arriving from the United States, July 2024 = **3,800,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "Freight traffic arriving from the United States also contributed to the overall growth in July, increasing 1.7% year over year to 3.8 million tonnes."
  - p58 Year-over-year change in freight traffic arriving from the United States, July 2 = **1.7** % (2024-07-01..2024-07-31) [keep: ] quote: "increasing 1.7% year over year to 3.8 million tonnes"
  - p59 Non-intermodal freight loadings, Canada, July 2024 = **23,200,000** metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "Non-intermodal freight loadings declined for the first time after three months of year-over-year increases, edging down 0.2% to 23.2 million tonnes in July."
  - p60 Year-over-year change in non-intermodal freight loadings, Canada, July 2024 = **0.2** % (2024-07-01..2024-07-31) [keep: ] quote: "edging down 0.2% to 23.2 million tonnes in July"
  - p61 Year-over-year change in iron ores and concentrates loadings, Canada, July 2024 = **12.3** % (2024-07-01..2024-07-31) [keep: ] quote: "loadings of iron ores and concentrates, down by 12.3% (-627 000 tonnes) in July compared with the same month in 2023"
  - p62 Year-over-year change in iron ores and concentrates loadings, Canada, July 2024, = **-627,000** as written "-627 000", value check pending metric tonnes (2024-07-01..2024-07-31) [keep: ] quote: "down by 12.3% (-627 000 tonnes) in July compared with the same month in 2023"
  - p63 Year-over-year change in wheat loadings, Canada, July 2024 = **10.3** % (2024-07-01..2024-07-31) [keep: ] quote: "Wheat loadings, for example, posted a year-over-year decrease of 10.3% (-207 000 tonnes)"
  - p64 Year-over-year change in potash loadings, Canada, July 2024 = **21** % (2024-07-01..2024-07-31) [keep: ] quote: "Loadings of potash were up 21.0% (+351 000 tonnes) from July 2023"
  - p65 Year-over-year change in fuel oils and crude petroleum loadings, Canada, July 20 = **18.5** % (2024-07-01..2024-07-31) [keep: ] quote: "loadings of fuel oils and crude petroleum-on an upward trend since November 2023-rose 18.5% (+148 000 tonnes) in July 2024 compared with July 2023"
  - p66 Year-over-year change in sulfur loadings, Canada, July 2024 = **37.3** % (2024-07-01..2024-07-31) [keep: ] quote: "loadings of sulfur grew 37.3% (+115 000 tonnes) year over year in July 2024"
- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3AFreight%20motor%20vehicles&23100216_facet` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b2 [base_rates] CN/CPKC annual reports, Rail Trends, and Statistics Canada length-of-haul data

Hypothesis: p38 gives Q3 2025 Class 1 revenue ton-miles but no average length of haul or Canada-only share. A Canada-specific average haul or Canadian share of CN/CPKC RTMs/tonnage would convert p38 to Canada tonnage and materially reduce the uncertainty from assumptions a5 and a6 in method m3.

Queries issued by the searcher: Statistics Canada railway carloadings average length of haul kilometres per tonne 2025; Rail Trends Canadian railways revenue ton-kilometres average length of haul table; CN annual report 2024 revenue ton miles Canada transborder "ton miles" percentage of total; Rail Trends 2025 "revenue ton-miles" Class 1 Canada average length of haul 2024 statistics canada shortline share tonnage

- `https://open.canada.ca/data/dataset/057180f9-9c2e-47e2-ba2e-d3f5ab9df5a4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/wp-content/uploads/2019/03/SPARK-RAC-INFOGRAPHIC-TRENDS-2026-EN2.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-eng.htm` -> **snapshot** (snapshot 20260225032721); points raw/verified 15/15
  - p67 Total freight tonnage carried by Canadian railways, December 2025 = **31,000,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "In December, Canadian railways transported 31.0 million tonnes of freight, down 2.0% compared with December 2024"
  - p68 Total freight tonnage carried by Canadian railways, full year 2025 = **376,600,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, the volume of goods moved by rail totalled 376.6 million tonnes, down slightly (-0.2%) from the total volume in 2024."
  - p69 Total freight tonnage carried by Canadian railways, full year 2024 = **377,300,000** metric tonnes (2024-01-01..2024-12-31) [keep: ] quote: "the overall total was similar to that in 2024 (377.3 million tonnes)"
  - p70 Non-intermodal freight tonnage in Canada, December 2025 = **24,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "The volume of non-intermodal freight (mainly commodities) in Canada was down 1.7% year over year to 24.8 million tonnes in December"
  - p71 Intermodal freight tonnage in Canada, December 2025 = **2,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "Intermodal freight loadings (mainly containers) rose 2.0% year over year to 2.8 million tonnes in December 2025"
  - p72 Freight traffic from US rail connections in Canada, December 2025 = **3,300,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "freight traffic from US rail connections declined year over year for the 11th straight month, down 7.4% to 3.3 million tonnes in December 2025"
  - p73 Non-intermodal freight tonnage in Canada, full year 2025 = **299,800,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, non-intermodal freight loadings in Canada totalled 299.8 million tonnes, up marginally (+0.9%) from 2024."
  - p74 Intermodal freight tonnage in Canada, full year 2025 (all-time high) = **37,500,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "intermodal freight traffic (mainly containers) rose 7.4% from 2024, reaching an-all time high of 37.5 million tonnes in 2025"
  - p75 Freight tonnage from US rail connections in Canada, full year 2025 = **39,300,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "annual tonnage fell by 13.3% from 2024 to 39.3 million tonnes in 2025, representing the lowest annual level since 2020"
  - p76 Share of total rail tonnage in Canada from US rail connections, average monthly  = **12** % (2023-01-01..2024-12-31) [keep: ] quote: "Over 2023 and 2024, freight traffic received from US rail connections in Canada represented an average of 12.0% of total rail tonnage each month."
  - p77 Share of total rail tonnage in Canada from US rail connections, Q1 2025 average = **10.7** % (2025-01-01..2025-03-31) [keep: ] quote: "averaging 10.7% during the first quarter of 2025, then 10.5% during the second quarter and 10.6% during the third quarter"
  - p78 Share of total rail tonnage in Canada from US rail connections, Q2 2025 average = **10.5** % (2025-04-01..2025-06-30) [keep: ] quote: "averaging 10.7% during the first quarter of 2025, then 10.5% during the second quarter and 10.6% during the third quarter"
  - p79 Share of total rail tonnage in Canada from US rail connections, Q3 2025 average = **10.6** % (2025-07-01..2025-09-30) [keep: ] quote: "averaging 10.7% during the first quarter of 2025, then 10.5% during the second quarter and 10.6% during the third quarter"
  - p80 Share of total rail tonnage in Canada from US rail connections, Q4 2025 = **10** % (2025-10-01..2025-12-31) [keep: ] quote: "The proportion dipped further to 10.0% in the fourth quarter."
  - p81 Wheat carloadings tonnage in Canada, full year 2025 = **31,100,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "Carloadings of wheat led the increases, with loadings rising 14.3% (+3.9 million tonnes) from 2024 to reach 31.1 million tonnes in 2025."
- `https://www.cn.ca/-/media/files/investors/investor-fact-book/2025-cn-investor-fact-book-en.pdf` -> **snapshot** (snapshot 20251212174017); points raw/verified 15/15
  - p82 CN average length of haul, all traffic, 2024 (system-wide, Canada and U.S.) = **742** miles (2024-01-01..2024-12-31) [keep: ] quote: "742 miles AVERAGE LENGTH OF HAUL"
  - p83 CN total revenue ton miles (RTMs), 2024 (system-wide, Canada and U.S.) = **235,538** millions of revenue ton miles (2024-01-01..2024-12-31) [keep: ] quote: "Total 230,390 233,138 235,788 232,614 235,538 1% 5.74 5.96 7.03 6.98 6.96 0%"
  - p84 CN total carloads, 2024 (system-wide, Canada and U.S.) = **5,390** thousands of carloads (2024-01-01..2024-12-31) [keep: ] quote: "Total rail freight 13,218 13,888 16,569 16,236 16,395 1% 5,595 5,701 5,697 5,436 5,390 (1%)"
  - p85 CN total gross ton miles (GTMs), 2024 (system-wide) = **457,700,000,000** gross ton miles (2024-01-01..2024-12-31) [keep: ] quote: "Gross ton miles (GTMs) (billions) 455.4 458.4 463.7 452.0 457.7"
  - p86 CN annual cargo carried (over 300 million tons, system-wide) = **300,000,000** tons of cargo (..) [keep: ] quote: ">300M TONS OF CARGO CARRIED ANNUALLY"
  - p87 CN annual tonnage transported (more than 300 million tons, North America) = **300,000,000** tons (..) [DISCARD: Duplicate of p86; both state CN carries over 300 million tons annually.] quote: "CN powers the economy by safely transporting more than 300 million tons of natural resources, manufactured products and finished goods throughout North America every year for its customers."
  - p88 Share of CN traffic originating and terminating on CN's network (2024) = **65** % (2024-01-01..2024-12-31) [keep: ] quote: "65%of traffic ORIGINATES AND TERMINATES ON CN'S NETWORK"
  - p89 Share of CN traffic originating on CN's network (2024) = **85** % (2024-01-01..2024-12-31) [keep: ] quote: "85% OF TRAFFIC ORIGINATES ON CN'S NETWORK"
  - p90 CN traffic by geography: Canadian domestic share of 2024 freight revenues = **17** % (2024-01-01..2024-12-31) [keep: ] quote: "W 17% Canadian domestic"
  - p91 CN traffic by geography: Transborder share of 2024 freight revenues = **32** % (2024-01-01..2024-12-31) [keep: ] quote: "W 32% Transborder"
  - p92 CN traffic by geography: Overseas share of 2024 freight revenues = **35** % (2024-01-01..2024-12-31) [keep: ] quote: "W 35% Overseas"
  - p93 CN traffic by geography: U.S. domestic share of 2024 freight revenues = **16** % (2024-01-01..2024-12-31) [keep: ] quote: "W 16% U.S. domestic"
  - p94 CN GTMs by region: Western Region share of 2024 total GTMs = **52** % (2024-01-01..2024-12-31) [keep: ] quote: "W 52% Western Region"
  - p95 CN GTMs by region: Eastern Region share of 2024 total GTMs = **21** % (2024-01-01..2024-12-31) [keep: ] quote: "W 21% Eastern Region"
  - p96 CN GTMs by region: Southern Region share of 2024 total GTMs = **27** % (2024-01-01..2024-12-31) [keep: ] quote: "W 27% Southern Region"

### b3 [related_series] Statistics Canada carloads and tonnes-per-carload tables

Hypothesis: Total tonnes equals carloads times average tonnes per carload. We have intermodal unit counts but not total carloads or average tonnes per carload for July 2026. A July carload count and commodity mix would provide an independent check on m1/m2 and constrain the average intermodal weight assumption a3.

Queries issued by the searcher: Statistics Canada Railway carloadings total traffic carried tonnes July 2025; Statistics Canada table 23-10-0064-01 railway carloadings by commodity tonnes per carload; tdih-cdit.tc.canada.ca "Monthly railway car loadings" 2025-07 "Total, non-intermodal traffic loaded" number of rail cars tonnes; "23-10-0064-01" railway carloadings statistics Canada data table tonnes number of rail cars

- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3AAnimal%20or%20vegetable%20fats%2C%20oils%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2310006401` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/wp-content/uploads/2026/02/RAC-RAIL-TRENDS-2025-FR5.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['canada rail freight', 'rail carloadings', 'july 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p40', 'p41'] All from the Railway Association of Canada 2026 weekly/YTD and crop-year reports. They show recent 2026 strength: week-32 carloads and RTMs up, YTD RTMs up, grain & fertilizers up, and early 2026-27 c
- corroborating: ['p15', 'p16', 'p17', 'p20', 'p18', 'p19', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] CEIC snapshot of Statistics Canada railway carloadings, all same underlying source and vintage. p15 and p16 are the May 2020 intermodal and non-intermodal loaded components; p17 and p20 are their long
- corroborating: ['p30', 'p31', 'p32'] Rail Association intermodal unit counts for July 2023-2025 show moderate growth and support a mid-teens tonnes-per-intermodal-unit bridge to intermodal tonnage. They do not directly give total tonnes.
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p37', 'p38'] Q3 2025 Class 1 operating metrics. p38 is the only direct volume measure, total revenue ton-miles, but it is network-wide Class 1 and likely includes some U.S./Mexico operations, so it needs average-h
- corroborating: ['p40', 'p41'] Early 2026-27 crop-year grain volumes are strong and consistent with p14's higher 2025-26 crop-year grain volume, though the period is August 2026 rather than July 2026.
- corroborating: ['p1', 'p6', 'p13'] No material conflict: p1 week-32 carloads up and p6 YTD carloads flat/RTMs up indicate recent acceleration; p13 metals/minerals YTD near flat versus p4 week-32 stronger is a weekly-versus-YTD differen
- corroborating: ['p15', 'p16', 'p17', 'p20'] p15/p16 May 2020 levels and p17/p20 historical averages are mutually consistent in level, but because they share the same CEIC/StatCan source they are not independent confirmation.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66'] Same Statistics Canada July 2024 release. p53 total is consistent with the p59 non-intermodal, p55 intermodal and p57 US-origin components within rounding; p54/p56/p58/p60 and p61-p66 give the commodi
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Same Statistics Canada 2025 annual/December release. p70+p71+p72 is consistent with p67 within rounding; p68 and p69 show near-flat annual totals; p73-p75 split annual components; p76-p80 track the fa
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13'] Railcan 2026 weekly indicators all point to positive 2026 traffic versus 2025: week 32 carloads/RTMs up, grain & fertilizers strongly up, metals positive, YTD RTMs up while carloads are near flat. p5 
- corroborating: ['p14', 'p40', 'p41'] Railcan grain data support the strong grain picture in p3/p10: 2025-26 crop-year grain movements were high and early 2026-27 weekly volumes were well above the prior three-year average. Different peri
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22'] Same CEIC/StatCan historical rail series. p15+p16 gives May 2020 loaded tonnage; p17/p20 give long-run averages; p18/p19/p21/p22 give historical extremes. Consistent as levels and ranges but old and n
- corroborating: ['p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] Same May 2020 CEIC commodity detail. They are internally consistent component context but too granular for an aggregate July 2026 estimate and are not used directly.
- corroborating: ['p30', 'p31', 'p32', 'p55', 'p74'] Railcan intermodal unit counts and StatCan intermodal tonnage both indicate strong intermodal growth: p30 is above p31/p32, and p74 shows a 2025 all-time high. Different units and scopes, so they supp
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p37', 'p38'] Same railcan Q3 operational snapshot. p33/p34 and p35 show small efficiency gains; p36/p37 show stable cars on line; p38 gives Class 1 RTMs. Useful context and a scope-limited RTM route, not a direct 
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96'] CN annual report metrics. p82-p85 provide internal consistency for CN system-wide haul and RTMs; p86-p96 document CN scope and regional/geographic mix. They are CN-only, not Canada total, and require 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 versus July 2024 total freight carried factor | 1.02 | 0.93..1.11 | 0.7184..1.437 (widened) | dimensionless | m1 (m1) | p53 is the exact StatCan July 2024 total. p68 shows 2025 annual tonnage essentially flat against p69's 2024 total, p67 shows December 2025 slightly down year over year, while p6/p7 show 2026 year-to-date RTMs up 4% with carloads flat and p1/p2 show week 32 of 2026 positive. Net two years out is near | StatCan's total-traffic-carried definition and coverage are unchanged between July 2024 and July 2026 and no major strike, wildfire or track outage hits July 2026. | Evidence of a large July 2026 disruption, a definition change in total traffic carried, or a 2026 monthly print far from 30 Mt. |
| a2 | July 2026 versus July 2024 non-intermodal tonnage factor | 1.01 | 0.93..1.09 | 0.7119..1.424 (widened) | dimensionless | m2 (m2), m4 (m6) | p73 shows 2025 non-intermodal annual tonnage up only marginally on 2024, p70 shows December 2025 down slightly, and p13 shows metals and minerals roughly flat year to date, while p3/p5 show grain and fertilizers strongly positive and p5 notes coal is the one declining RTM commodity. Offsetting commo | The non-intermodal commodity mix and StatCan classification remain comparable between 2024 and 2026. | Commodity-level evidence of a sharp 2026 fall in grain, potash, coal, iron ore or metals loadings relative to 2024. |
| a3 | July 2026 versus July 2024 intermodal tonnage factor | 1.12 | 1..1.26 | 0.7937..1.587 (widened) | dimensionless | m2 (m2) | p74 shows 2025 intermodal tonnage at an all-time high, up 7.4% on 2024, and p55/p56 show July 2024 was already up sharply; p30 versus p31 shows July unit counts rising further in 2025, and p1 reports intermodal carloads still increasing in week 32 of 2026. Two years of low-single-digit compounding s | Containerized traffic keeps growing at roughly the 2025-2026 pace and port/terminal throughput is not disrupted. | Falling intermodal unit counts in mid-2026, a port labour disruption, or evidence that 2026 intermodal volumes fell below 2025. |
| a4 | July 2026 versus July 2024 US-origin tonnage factor | 0.86 | 0.7..1 | 0.5916..1.183 (widened) | dimensionless | m2 (m2), m4 (m6) | p57 gives the July 2024 US-origin base. p75 shows 2025 annual US-origin tonnage down 13.3% and the lowest since 2020, p72 shows December 2025 down 7.4% on an eleventh consecutive decline, and p76-p80 show the share falling from 12.0% in 2023-24 to 10.6% in Q3 2025 and 10.0% in Q4 2025. With the tota | US rail-connection volumes remain on the 2025-early 2026 downward trajectory through July 2026. | A rebound in US-origin traffic, or a Q3 2026 share back above roughly 11.5%. |
| a5 | 2026 versus 2025 annual-level factor applied to the July share of annual tonnage | 1.01 | 0.93..1.09 | 0.7119..1.424 (widened) | dimensionless | unused | p68/p69 show the 2025 annual total essentially flat versus 2024, while p6/p7 show 2026 year-to-date RTMs up 4% with carloads flat and p1/p2 show week 32 positive. A near-flat 2026 annual level with a slight positive tilt is the central case; the band admits weakening or acceleration. This factor adj | The 2026 full-year level stays close to 2025 plus the observed year-to-date trend, and July 2026 seasonality resembles July 2024. | A large divergence between 2026 year-to-date rail indicators and the eventual monthly outcome, or a major 2026 disruption. |
| a6 | Average length of haul for the traffic represented by p38 | 1,050 | 850..1,350 | 757..1,515 (widened) | miles | m3 (m5) | p82 gives CN's system-wide average haul of 742 miles, but p38 is Canadian Class 1 (CN plus CPKC) network-wide and is weighted toward long western bulk hauls (grain, potash, coal) and overseas movements through Canadian ports; p6/p7 show RTMs growing while carloads are flat, which means the average h | The commodity mix behind p38 keeps a Canada-weighted haul inside this band from Q3 2025 to July 2026. | A published Canada-specific average length of haul outside this range for Class 1 traffic. |
| a7 | July 2026 versus Q3 2025 monthly-average Class 1 tonnage factor | 1.02 | 0.92..1.13 | 0.721..1.442 (widened) | dimensionless | m3 (m5) | p38 is a Q3 2025 quarter centred on August, and July is normally slightly below the quarter average, but p6/p7 show 2026 year-to-date RTMs up 4% versus 2025 and p1/p2 show week 32 of 2026 positive, so the net calendar-plus-trend effect is close to flat with upside risk. | The Q3 2025 quarter average is a serviceable base for a July 2026 month after applying the 2026 year-to-date trend. | A sharp month-specific change in 2026 RTMs relative to the year-to-date pattern, or a July-specific disruption. |
| a8 | Share of p38-derived Class 1 network-wide tonnage falling inside StatCan's Canada total traffic carried | 0.85 | 0.65..1 | 0.5701..1.14 (widened) | share | m3 (m5) | p38 is a Class 1 network-wide measure while the target is StatCan's Canada total; p90-p93 show CN's Canadian domestic business is only 17% of freight revenue with transborder (32%), overseas (35%) and U.S. domestic (16%) making up the rest, so a share below 1 is required. Overseas traffic (grain, po | p38's geographic scope is broader than StatCan's Canada total and the overlap can be captured by a single share in this band. | Documentation that p38 is already exactly the Canada-only traffic StatCan counts, or a CN/CPKC disclosure allowing a direct Canada-only RTM split. |
| a9 | July 2026 versus July 2025 intermodal unit growth factor | 1.05 | 0.94..1.18 | 0.94..1.18 | dimensionless | m4 (m6) | p30/p31/p32 show July units of 195k, 192k and 208k in 2023-2025, so July 2025 rose on July 2024; p74 shows 2025 intermodal tonnage at an all-time high and p1 reports intermodal carloads still increasing in week 32 of 2026. Modest further growth is the central case, with a decline possible if tariffs | Intermodal demand continues along the 2025-2026 growth path through July 2026. | Falling intermodal unit counts or port container throughput in mid-2026. |
| a10 | Ratio of shortline and other non-Class-1 carrier tonnage to Canada-covered Class 1 tonnage, July 2026 | 0.06 | 0.03..0.12 | 0.03..0.12 | dimensionless | m3 (m5) | StatCan's total traffic carried covers all federal railways, while p38 covers only CN and CPKC. Canadian shortlines and regional/other carriers (e.g. Ontario Northland, G&W Canada properties, regional forest-product and potash feeders) are small relative to the two Class 1s, and much of their line-h | StatCan's 'all railways' coverage exceeds CN plus CPKC by shortlines and other reporting carriers of roughly this relative size in July 2026. | StatCan documentation or carrier data showing non-Class-1 carriers account for more than about a tenth of Canadian rail tonnage. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 30,434,491 | ['p53'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 30,021,582 | ['p59', 'p55', 'p57'] / ['a2', 'a3', 'a4'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 27,497,816 | ['p38'] / ['a10', 'a6', 'a7', 'a8'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 30,032,670 | ['p59', 'p30', 'p55', 'p31', 'p57'] / ['a2', 'a4', 'a9'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of non-intermodal, intermodal, US-origin
- m3 coverage: sum over channel of Class 1 (CN and CPKC) Canada-covered traffic, shortlines and other non-Class-1 carriers
- m4 coverage: sum over channel of non-intermodal, intermodal, US-origin

Result: central **29,472,905** t, 80% interval [15,641,780, 55,534,098] t, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total freight carried by Canadian railways in Canada during July 2026 is 29,472,905 t (80% model-based interval 15,641,780 to 55,534,098 t). This targets StatCan's total traffic carried series, first release.

The anchor is 29,900,000 metric tonnes, the exact July 2024 total. Methods rebuild it three ways: a direct drift factor (1.02), a channel sum of non-intermodal 23,200,000 metric tonnes, intermodal 2,800,000 metric tonnes and US-origin 3,800,000 metric tonnes traffic scaled by 1.01, 1.12 and 0.86, and a Class [n] RTM route from 111,388,000,000 revenue ton-miles with haul, share and shortline assumptions. Intermodal units 208,000 intermodal units and 192,000 intermodal units support a fourth cross-check. Only the July 2024 points are observed; every 2026 factor is an assumption. Code weighted the methods equally because backtest years were too few to calibrate errors, so the interval reflects input uncertainty only.

The main risk is a definition break or a July 2026-specific shock. A published July 2025 total would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 versus July 2024 total freight carried factor: 1.02 dimensionless, range 0.7184 to 1.437 (range widened by code); used by m1. Overturned by: Evidence of a large July 2026 disruption, a definition change in total traffic carried, or a 2026 monthly print far from [n] Mt.
- a2 July 2026 versus July 2024 non-intermodal tonnage factor: 1.01 dimensionless, range 0.7119 to 1.424 (range widened by code); used by m2, m4. Overturned by: Commodity-level evidence of a sharp 2026 fall in grain, potash, coal, iron ore or metals loadings relative to 2024.
- a3 July 2026 versus July 2024 intermodal tonnage factor: 1.12 dimensionless, range 0.7937 to 1.587 (range widened by code); used by m2. Overturned by: Falling intermodal unit counts in mid-2026, a port labour disruption, or evidence that 2026 intermodal volumes fell below 2025.
- a4 July 2026 versus July 2024 US-origin tonnage factor: 0.86 dimensionless, range 0.5916 to 1.183 (range widened by code); used by m2, m4. Overturned by: A rebound in US-origin traffic, or a Q3 2026 share back above roughly [n].
- a6 Average length of haul for the traffic represented by p38: 1,050 miles, range 757 to 1,515 (range widened by code); used by m3. Overturned by: A published Canada-specific average length of haul outside this range for Class [n] traffic.
- a7 July 2026 versus Q3 2025 monthly-average Class [n] tonnage factor: 1.02 dimensionless, range 0.721 to 1.442 (range widened by code); used by m3. Overturned by: A sharp month-specific change in 2026 RTMs relative to the year-to-date pattern, or a July-specific disruption.
- a8 Share of p38-derived Class [n] network-wide tonnage falling inside StatCan's Canada total traffic carried: 0.85 share, range 0.5701 to 1.14 (range widened by code); used by m3. Overturned by: Documentation that p38 is already exactly the Canada-only traffic StatCan counts, or a CN/CPKC disclosure allowing a direct Canada-only RTM split.
- a9 July 2026 versus July 2025 intermodal unit growth factor: 1.05 dimensionless, range 0.94 to 1.18; used by m4. Overturned by: Falling intermodal unit counts or port container throughput in mid-2026.
- a10 Ratio of shortline and other non-Class-[n] carrier tonnage to Canada-covered Class [n] tonnage, July 2026: 0.06 dimensionless, range 0.03 to 0.12; used by m3. Overturned by: StatCan documentation or carrier data showing non-Class-[n] carriers account for more than about a tenth of Canadian rail tonnage.

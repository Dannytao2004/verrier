# Evidence ledger: fc_ca_rail_2026_07

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the total freight carried by Canadian railways in July 2026, in tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total traffic carried, Canada).
- as_of: 2026-08-29
- Pinned target: Total freight carried by Canadian railways (all traffic carried, Canada) during July 2026, as first reported by Statistics Canada in its monthly Railway carloadings release (Table 23-10-0219-01 / The Daily release 'Railway carloadings, monthly'). Counts all revenue freight loaded and carried by Cana | unit metric tonnes | period 2026-07-01..2026-07-31 | publisher Statistics Canada

- Official value (scoring only, never shown to the agent): 31,686,803

## Directions and pages

### d1 [own_history] Statistics Canada monthly Railway carloadings time series

Hypothesis: July 2026 total traffic carried will be close to the same month in prior years adjusted for trend and any 2026-specific shocks; July is a seasonal peak month for grain and potash. The historical July values and recent monthly values (through the last release before the cutoff, likely June 2026) anchor the level and seasonality.

Queries issued by the searcher: Statistics Canada table 23-10-0219-01 railway carloadings total traffic carried tonnes; The Daily Railway carloadings monthly July 2025 Statistics Canada total tonnes; "Railway carloadings" June 2026 Statistics Canada The Daily million tonnes; "Railway carloadings, July 2024" Statistics Canada tonnes The Daily

- `https://www150.statcan.gc.ca/n1/daily-quotidien/250924/dq250924f-eng.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **snapshot** (snapshot 20210125231348); points raw/verified 6/6
  - p1 Canada railway total traffic carried, October 2020 = **32,577,741** tonnes (2020-10-01..2020-10-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Total Traffic Carried data was reported at 32,577,741.000 Tonne in Oct 2020."
  - p2 Canada railway total traffic carried, September 2020 = **31,136,134** tonnes (2020-09-01..2020-09-30) [keep: ] quote: "This records an increase from the previous number of 31,136,134.000 Tonne for Sep 2020."
  - p3 Canada railway total traffic carried, monthly average Jan 1999 to Oct 2020 = **26,443,500** tonnes (1999-01-01..2020-10-31) [keep: ] quote: "averaging 26,443,499.500 Tonne from Jan 1999 to Oct 2020, with 262 observations"
  - p4 Canada railway total traffic carried, all-time high, October 2018 = **34,846,417** tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 34,846,417.000 Tonne in Oct 2018"
  - p5 Canada railway total traffic carried, record low, February 2009 = **20,656,974** tonnes (2009-02-01..2009-02-28) [keep: ] quote: "a record low of 20,656,974.000 Tonne in Feb 2009"
  - p6 Number of monthly observations in Canada railway total traffic series, Jan 1999  = **262** observations (1999-01-01..2020-10-31) [DISCARD: Count of observations, not a tonnage; no role in any route.] quote: "averaging 26,443,499.500 Tonne from Jan 1999 to Oct 2020, with 262 observations"
- `https://www.ceicdata.com/zh-hans/canada/railway-carloadings` -> **snapshot** (snapshot 20200706020213); points raw/verified 15/15
  - p7 Canada railway carloadings: non-intermodal loaded traffic, monthly total (April  = **24,073,997** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "加拿大的Railway Carloadings:已负载的非联合运输在04-01-2020达24,073,997.000吨"
  - p8 Canada railway carloadings: non-intermodal loaded traffic, prior month (March 20 = **26,561,133** metric tonnes (2020-03-01..2020-03-31) [keep: ] quote: "相较于03-01-2020的26,561,133.000吨有所下降"
  - p9 Canada railway carloadings: non-intermodal loaded traffic, monthly average 1999- = **21,479,188** metric tonnes (1999-01-01..2020-04-30) [keep: ] quote: "01-01-1999至04-01-2020期间平均值为21,479,187.500吨"
  - p10 Canada railway carloadings: non-intermodal loaded traffic, historical maximum (O = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [keep: ] quote: "历史最高值出现于10-01-2018,达28,258,207.000吨"
  - p11 Canada railway carloadings: non-intermodal loaded traffic, historical minimum (J = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [keep: ] quote: "历史最低值则出现于07-01-2009,为16,818,939.000吨"
  - p12 Canada railway carloadings: intermodal freight, monthly total (April 2020) = **3,081,691** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "加拿大的Railway Carloadings:货物联合运输在04-01-2020达3,081,691.000吨"
  - p13 Canada railway carloadings: intermodal freight, prior month (March 2020) = **3,112,570** metric tonnes (2020-03-01..2020-03-31) [keep: ] quote: "相较于03-01-2020的3,112,570.000吨有所下降"
  - p14 Canada railway carloadings: intermodal freight, monthly average 1999-01 to 2020- = **2,380,480** metric tonnes (1999-01-01..2020-04-30) [keep: ] quote: "01-01-1999至04-01-2020期间平均值为2,380,480.500吨"
  - p15 Canada railway carloadings: intermodal freight, historical maximum (May 2019) = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [keep: ] quote: "历史最高值出现于05-01-2019,达3,255,376.000吨"
  - p16 Canada railway carloadings: intermodal freight, historical minimum (January 1999 = **1,264,980** metric tonnes (1999-01-01..1999-01-31) [keep: ] quote: "历史最低值则出现于01-01-1999,为1,264,980.000吨"
  - p17 Canada railway carloadings: non-intermodal cement, historical maximum (July 2019 = **361,023** metric tonnes (2019-07-01..2019-07-31) [DISCARD: Duplicate of p35/p96/p117 (cement July 2019 all-time high); adds no information.] quote: "历史最高值出现于07-01-2019,达361,023.000吨"
  - p18 Canada railway carloadings: non-intermodal cement, monthly total (April 2020) = **188,246** metric tonnes (2020-04-01..2020-04-30) [DISCARD: April 2020 cement; superseded by May 2020 p34/p97 and too small/old to matter.] quote: "加拿大的Railway Carloadings:非联运:水泥在04-01-2020达188,246.000吨"
  - p19 Canada railway carloadings: non-intermodal animal feed and products, monthly tot = **401,796** metric tonnes (2020-04-01..2020-04-30) [DISCARD: April 2020 animal feed; duplicate role of p30/p98, no added information.] quote: "加拿大的Railway Carloadings:非联运:动物饲料和产品在04-01-2020达401,796.000吨"
  - p20 Canada railway carloadings: non-intermodal alumina, monthly total (April 2020) = **324,090** metric tonnes (2020-04-01..2020-04-30) [DISCARD: April 2020 alumina; duplicate of p28/p101/p112.] quote: "加拿大的Railway Carloadings:非联运:氧化铝在04-01-2020达324,090.000吨"
  - p21 Canada railway carloadings: non-intermodal animal or vegetable oils and flours,  = **450,823** metric tonnes (2020-03-01..2020-03-31) [DISCARD: April 2020 fats/oils; duplicate of p31/p99/p115.] quote: "\| 数值 \| 450,823.000 2020-03 \|"

### d2 [related_series] Commodity-level carloadings breakdown

Hypothesis: Total tonnes = sum over commodity groups (grain, potash, coal, chemicals, forest products, metals, intermodal, etc.) of tonnes carried. Commodity-level July history plus known 2026 supply signals (grain harvest/carryover, potash output, coal exports) constrain the total and its largest swing components.

Queries issued by the searcher: Statistics Canada railway carloadings by commodity tonnes grain potash coal table 23-10-0219-01; StatCan rail commodity tonnes July 2025 railway carloadings monthly principal commodities; "Railway carloadings, June 2026" Statistics Canada Daily; "Railway carloadings, July 2025" Statistics Canada tonnes wheat potash coal

- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tdih-cdit.tc.canada.ca/en/search/23100216` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p22 Canada railway carloadings: intermodal traffic loaded, May 2020 = **3,040,663** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p23 Canada railway carloadings: non-intermodal traffic loaded, May 2020 = **24,396,926** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p24 Canada railway carloadings: non-intermodal traffic loaded, all-time high (Oct 20 = **28,258,207** tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018 and a record low of 16,818,939.000 Tonne in Jul 2009."
  - p25 Canada railway carloadings: non-intermodal traffic loaded, record low (Jul 2009) = **16,818,939** tonnes (2009-07-01..2009-07-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018 and a record low of 16,818,939.000 Tonne in Jul 2009."
  - p26 Canada railway carloadings: intermodal traffic loaded, all-time high (May 2019) = **3,255,376** tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019 and a record low of 1,264,980.000 Tonne in Jan 1999."
  - p27 Canada railway carloadings: intermodal traffic loaded, record low (Jan 1999) = **1,264,980** tonnes (1999-01-01..1999-01-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019 and a record low of 1,264,980.000 Tonne in Jan 1999."
  - p28 Canada railway carloadings: non-intermodal alumina, May 2020 = **126,378** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p29 Canada railway carloadings: non-intermodal aluminum, May 2020 = **291,832** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p30 Canada railway carloadings: non-intermodal animal feed & products, May 2020 = **409,186** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p31 Canada railway carloadings: non-intermodal animal or vegetable fats, oils & flou = **414,481** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p32 Canada railway carloadings: non-intermodal articles of base metal, May 2020 = **66,429** tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 base metal articles; tiny commodity, no role.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Articles of Base Metal data was reported at 66,429.000 Tonne in May 2020."
  - p33 Canada railway carloadings: non-intermodal automobiles & mini-vans, May 2020 = **20,703** tonnes (2020-05-01..2020-05-31) [DISCARD: Duplicate of p102 (automobiles May 2020); no role.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."
  - p34 Canada railway carloadings: non-intermodal cement, May 2020 = **247,356** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p35 Canada railway carloadings: non-intermodal cement, all-time high (Jul 2019) = **361,023** tonnes (2019-07-01..2019-07-31) [keep: ] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019 and a record low of 102,723.000 Tonne in Feb 2003."
  - p36 Canada railway carloadings: non-intermodal alcoholic & non-alcoholic beverages,  = **7,344** tonnes (2020-05-01..2020-05-31) [DISCARD: May 2020 beverages; negligible commodity, no role.] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alcoholic & Non-Alcoholic Beverages data was reported at 7,344.000 Tonne in May 2020."
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/dq260224c-eng.pdf` -> **snapshot** (snapshot 20260225062029); points raw/verified 15/15
  - p37 Total freight transported by Canadian railways, December 2025 = **31,000,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "In December, Canadian railways transported 31.0 million tonnes of freight, down 2.0% compared with December 2024"
  - p38 Total freight moved by rail in Canada, full year 2025 = **376,600,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, the volume of goods moved by rail totalled 376.6 million tonnes, down slightly (-0.2%) from the total volume in 2024."
  - p39 Total freight moved by rail in Canada, full year 2024 = **377,300,000** metric tonnes (2024-01-01..2024-12-31) [keep: ] quote: "the overall total was similar to that in 2024 (377.3 million tonnes)."
  - p40 Non-intermodal freight loadings in Canada, December 2025 = **24,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "The volume of non-intermodal freight (mainly commodities) in Canada was down 1.7% year over year to 24.8 million tonnes in December"
  - p41 Intermodal freight loadings in Canada, December 2025 = **2,800,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "Intermodal freight loadings (mainly containers) rose 2.0% year over year to 2.8 million tonnes in December 2025"
  - p42 Freight traffic from US rail connections in Canada, December 2025 = **3,300,000** metric tonnes (2025-12-01..2025-12-31) [keep: ] quote: "freight traffic from US rail connections declined year over year for the 11th straight month, down 7.4% to 3.3 million tonnes in December 2025."
  - p43 Non-intermodal freight loadings in Canada, full year 2025 = **299,800,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, non-intermodal freight loadings in Canada totalled 299.8 million tonnes, up marginally (+0.9%) from 2024."
  - p44 Intermodal freight traffic in Canada, full year 2025 (all-time high) = **37,500,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "intermodal freight traffic (mainly containers) rose 7.4% from 2024, reaching an-all time high of 37.5 million tonnes in 2025."
  - p45 Freight loadings from US rail connections in Canada, full year 2025 = **39,300,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "annual tonnage fell by 13.3% from 2024 to 39.3 million tonnes in 2025, representing the lowest annual level since 2020"
  - p46 Wheat carloadings in Canada, full year 2025 = **31,100,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "loadings rising 14.3% (+3.9 million tonnes) from 2024 to reach 31.1 million tonnes in 2025."
  - p47 Other cereal grains carloadings in Canada, full year 2025 = **7,800,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "loadings of other cereal grains grew 23.4%, from 6.3 million tonnes in 2024 to 7.8 million tonnes in 2025"
  - p48 Coal carloadings in Canada, full year 2025 = **38,500,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "A notable increase was also reported for coal, rising 4.4% from 2024 to 38.5 million tonnes in 2025, driven by strong international demand from Asia."
  - p49 Fuel oils and crude petroleum carloadings in Canada, full year 2025 = **10,000,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "Loadings of fuel oils and crude petroleum fell sharply by 11.0% (-1.2 million tonnes) from 2024 to 10.0 million tonnes in 2025."
  - p50 Canola carloadings in Canada, full year 2025 = **8,800,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "loadings of canola fell 12.4% from 10.0 million tonnes in 2024 to 8.8 million tonnes in 2025"
  - p51 Lumber carloadings in Canada, full year 2025 = **7,300,000** metric tonnes (2025-01-01..2025-12-31) [keep: ] quote: "loadings of lumber were down 12.1% from 2024 to total 7.3 million tonnes in 2025, marking the largest drop in tonnage in over five years."

### d3 [related_series] Railway company operational reports (CN, CPKC)

Hypothesis: CN and CPKC together carry the large majority of Canadian rail tonnage; their reported revenue ton-miles, carloads, or grain/potash volumes for Q2/Q3 2026 and July 2026 can be scaled to a Canada total using their historical share of StatCan total tonnes.

Queries issued by the searcher: CN rail July 2026 carloads revenue ton miles; CPKC July 2026 monthly operating metrics grain carloads; CPKC July 2026 grain Canadian tonnes carloads monthly record; CN "July 2026" grain tonnes moved press release

- `https://ecprod.cn.ca/corp/en/news/2026/07/cn-delivers-on-commitments-with-strong-second-quarter-results-an/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://seekingalpha.com/pr/20600181-cpkc-reports-strong-q2-results-poised-for-accelerated-growth-in-second-half-of-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.progressiverailroading.com/canadian_pacific_kansas_city/news/CPKC-closes-out-crop-year-with-new-annual-grain-record--77488` -> **snapshot** (snapshot 20260819213712); points raw/verified 7/6
  - p52 CPKC Canadian grain and grain products transported, 2025-26 crop year (annual re = **30,660,000** metric tons (2025-08-01..2026-07-31) [keep: ] quote: "moving 30.66 million metric tons (MMT) of grain during the 2025-26 crop year"
  - p53 CPKC margin by which 2025-26 grain record exceeds previous record (2020-21 crop  = **72,500** metric tons (2025-08-01..2026-07-31) [DISCARD: CPKC record margin in tonnes; not needed and not a level of the target.] quote: "exceeds the previous record, set in the 2020-21 crop year, by about 72,500 metric tons"
  - p54 CPKC total volume growth in 2025-26 crop year vs previous year = **11** % (2025-08-01..2026-07-31) [DISCARD: CPKC volume growth %; redundant with p70 RAC grain growth and not directly usable.] quote: "Total volume transported in the 2025-26 crop year was 11% higher than the previous year"
  - p55 CPKC total volume growth in 2025-26 crop year vs three-year average = **16** % (2025-08-01..2026-07-31) [DISCARD: CPKC growth vs 3-yr avg; redundant with p70/p72.] quote: "16% higher than the three-year average"
  - p56 CPKC total volume growth in 2025-26 crop year vs five-year average = **20** % (2025-08-01..2026-07-31) [DISCARD: CPKC growth vs 5-yr avg; redundant with p70/p72.] quote: "20% higher than the five-year average"
  - p57 Elevator length capability referenced by CPKC VP (customer investments) = **8,500** feet (not stated (page dated 2025-10-17)) [DISCARD: Elevator length capability; not a tonnage and not needed.] quote: "Our customers' investments in 8,500-foot-capable elevators"
- `https://reportify.cn/reports/1276891656662159360` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: unknown scale word 'MMT': 1)

### d4 [physical_flow] Grain and potash export logistics

Hypothesis: Grain and potash are the largest seasonal tonnage drivers in July; port and terminal throughput (Vancouver, Prince Rupert, Thunder Bay; potash ports) and weekly rail grain carloadings (e.g., Ag Transport Coalition, Quorum weekly data) can be converted to rail tonnes via known rail-to-port shares.

Queries issued by the searcher: Ag Transport Coalition weekly rail performance July 2026 grain cars ordered; Port of Vancouver grain shipments July 2026; grainmonitor.ca MonthlyReport202607 July 2026 grain rail tonnes western Canadian ports; potash rail shipments Canada July 2026 tonnes Canpotex Port of Vancouver potash exports

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://author.cpkcr.com/en/our-markets/canadian-grain/grain-performance-scorecard/GS-Archive` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.620ckrm.com/2026/07/20/canadas-major-railways-report-strong-grain-shipments-in-week-49-ag-transport-coalition/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://okotoksonline.com/articles/atc-grain-rail-performance-shows-modest-improvement` -> **snapshot** (snapshot 20260829073607); points raw/verified 15/1
  - p58 Overall hopper car fulfillment rate, Western Canada, previous week (week one of  = **88** % (2026-08-23..2026-08-29) [keep: ] quote: "overall hopper car fulfillment reached 90 percent, up from 88 percent the previous week"
- dropped by code checks: 14 (period_end 2026-09-05 after as_of: 13; period_end 2026-09-12 after as_of: 1)

### d5 [shocks] Disruptions, strikes, weather, and policy affecting July 2026 rail

Hypothesis: Any 2026 labour disruption (CN/CPKC/Teamsters), wildfire, flood, or trade policy (e.g., tariffs on Canadian commodities) would shift July 2026 tonnage away from the historical seasonal pattern; quantifying exposure adjusts the base-rate estimate.

Queries issued by the searcher: Canada railway strike 2026 CN CPKC Teamsters; wildfire rail disruption Canada July 2026; CN CPKC Teamsters work stoppage July 2026 CIRB decision rail strike averted; Statistics Canada railway carloadings July 2026

- `https://www.cbc.ca/lite/story/9.7274475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tsb-bst.gc.ca/eng/enquetes-investigations/rail/2026/r26t0219/r26t0219.html?wbdisable=false` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.trains.com/pro/passenger/intercity/wildfires-stop-vias-canadian-again-this-time-in-ontario/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.worldports.org/threat-of-canadian-rail-strike-looms-again-after-bid-for-conciliation-fails/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Industry forecasts and outlooks

Hypothesis: Rail association (RAC) or analyst outlooks for 2026 Canadian rail volumes, and any StatCan nowcast/leading indicators, provide an independent level check on July 2026 tonnage.

Queries issued by the searcher: Railway Association of Canada 2026 traffic statistics forecast; Statistics Canada railway carloadings monthly July 2026; "Railway carloadings" Statistics Canada The Daily June 2026 release July 27 2026; Canadian rail volume outlook 2026 analyst CN CPKC carload growth forecast

- `https://www.railcan.ca/resources/traffic-dashboard/` -> **snapshot** (snapshot 20260826130548); points raw/verified 15/14
  - p59 Canadian Class 1 (CN and CPKC) network-wide carloads change, week 32 of 2026 vs  = **7** % (2026-08-09..2026-08-15) [keep: ] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p60 Canadian Class 1 (CN and CPKC) network-wide revenue ton-miles change, week 32 of = **13** % (2026-08-09..2026-08-15) [keep: ] quote: "In week 32 of 2026 (August 9 - August 15), Canadian Class 1 (CN and CPKC) network-wide carloads increased by 7% and revenue ton-miles (RTMs) increased by 13% compared to the same week in 2025."
  - p61 Canadian Class 1 network-wide revenue ton-miles change, first 32 weeks of 2026 v = **4** % (2026-01-01..2026-08-15) [keep: ] quote: "Across the first 32 weeks of 2026, Canadian Class 1 network-wide carloads were flat while RTMs were up 4% compared to the same period in 2025"
  - p62 Canadian Class 1 network-wide carloads change, first 32 weeks of 2026 vs same pe = **21,738** carloads (2026-01-01..2026-08-15) [keep: ] quote: "(+21,738 carloads and +11,687 million RTMs)"
  - p63 Canadian Class 1 network-wide revenue ton-miles change, first 32 weeks of 2026 v = **11,687,000,000** revenue ton-miles (2026-01-01..2026-08-15) [keep: ] quote: "(+21,738 carloads and +11,687 million RTMs)"
  - p64 Grain & fertilizers carloads change, Canadian Class 1, first 32 weeks of 2026 vs = **98,516** carloads (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%)"
  - p65 Grain & fertilizers carloads change, Canadian Class 1, first 32 weeks of 2026 vs = **11** % (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%)"
  - p66 Grain & fertilizers revenue ton-miles change, Canadian Class 1, first 32 weeks o = **11,822,000,000** revenue ton-miles (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%)"
  - p67 Grain & fertilizers revenue ton-miles change, Canadian Class 1, first 32 weeks o = **13** % (2026-01-01..2026-08-15) [keep: ] quote: "Growth was driven by increases of grain & fertilizers (+98,516 carloads, or +11%; +11,822 million RTMs, or +13%)"
  - p68 Metals and minerals carloads change, Canadian Class 1, year-to-date 2026 vs same = **1** % (2026-01-01..2026-08-15) [keep: ] quote: "Carloads of metals and minerals are up 1% on a year-to-date basis while RTMs are relatively flat."
  - p69 Canadian grain and grain products moved by CN and CPKC, 2025-2026 crop year = **64,000,000** metric tonnes (2025-08-01..2026-07-31) [keep: ] quote: "In the 2025-2026 crop year (August 2025 - July 2026), CN and CPKC moved 64.0 million metric tonnes of Canadian grain and grain products - 15% higher than the previous 3-year average."
  - p70 Canadian grain and grain products moved by CN and CPKC, 2025-2026 crop year vs p = **15** % (2025-08-01..2026-07-31) [keep: ] quote: "In the 2025-2026 crop year (August 2025 - July 2026), CN and CPKC moved 64.0 million metric tonnes of Canadian grain and grain products - 15% higher than the previous 3-year average."
  - p71 Canadian grain and grain products moved by CN and CPKC, week 1 of 2026-2027 crop = **1,100,000** metric tonnes (2026-08-02..2026-08-08) [keep: ] quote: "In week 1 (August 2 - August 8) of the 2026-2027 crop year, CN and CPKC moved nearly 1.1 million metric tonnes of Canadian grain and grain products."
  - p72 Crop year-to-date grain volumes (2 week), CN and CPKC, 2026-2027 crop year = **2,200,000** metric tonnes (2026-08-02..2026-08-15) [keep: ] quote: "Crop year-to-date grain volumes (2 week) 2.2 million metric tonnes \| +49% vs previous 3-year average"
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?tblId=23-10-0216-01` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railcan.ca/wp-content/uploads/2019/03/SPARK-RAC-INFOGRAPHIC-TRENDS-2026-EN2.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### b1 [own_history] StatCan monthly series

Hypothesis: A July 2025 (and July 2024/2023) total traffic carried value from StatCan Table 23-10-0219-01 would let a yoy_scaling method use the RAC 2026-vs-2025 change signal (p59-p67) directly, anchoring the level far better than the 2020-vintage series. This is the single most valuable missing input.

Queries issued by the searcher: Statistics Canada Table 23-10-0219-01 railway carloadings monthly total traffic carried; The Daily "Railway carloadings" July 2025 Statistics Canada tonnes; "23-10-0219-01" railway carloadings total tonnage transported monthly data table; "Railway carloadings, July 2024" The Daily Statistics Canada 31 million tonnes

- `https://www150.statcan.gc.ca/n1/daily-quotidien/250924/dq250924f-eng.htm` -> **snapshot** (snapshot 20260520140850); points raw/verified 15/15
  - p73 Total cargo carried by Canadian railways, all traffic, Canada, July 2025 = **30,700,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "The volume of cargo carried by Canadian railways reached 30.7 million tonnes in July 2025, down 0.4% from one year earlier."
  - p74 Year-over-year change in total cargo carried by Canadian railways, July 2025 vs  = **-0.4** % (2025-07-01..2025-07-31) [keep: ] quote: "30.7 million metric tonnes July 2025 -0.4% (12-month change)"
  - p75 Five-year historical average total freight volume for the month of July = **29,800,000** metric tonnes (not stated (page dated 2025-09-24)) [keep: ] quote: "the overall freight volume in July 2025 was slightly above the five-year historical average of 29.8 million tonnes for the month of July."
  - p76 Freight loadings from US rail connections, Canada, July 2025 = **3,300,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "freight loadings from US rail connections dropped 19.2% (-794 000 tonnes) to 3.3 million tonnes"
  - p77 Year-over-year change in freight loadings from US rail connections, July 2025 = **-794,000** as written "-794 000", value check pending metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "freight loadings from US rail connections dropped 19.2% (-794 000 tonnes) to 3.3 million tonnes"
  - p78 Non-intermodal freight traffic in Canada, July 2025 = **24,200,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "Non-intermodal freight traffic in Canada rose 1.6% year over year to 24.2 million tonnes in July 2025"
  - p79 Intermodal shipments originating in Canada, July 2025 = **3,200,000** metric tonnes (2025-07-01..2025-07-31) [keep: ] quote: "intermodal shipments-mainly containers-originating in Canada increased 9.4% compared with July 2024 to 3.2 million tonnes"
  - p80 Share of total rail tonnage represented by traffic received from US connections, = **12** % (2023-01-01..2024-12-31) [keep: ] quote: "In 2023 and 2024, traffic received from US connections represented an average 12.0% of total rail tonnage each month."
  - p81 Share of total rail tonnage represented by traffic received from US connections, = **10.7** % (2025-01-01..2025-03-31) [keep: ] quote: "During the first quarter of 2025, this proportion edged down to 10.7%"
  - p82 Share of total rail tonnage represented by traffic received from US connections, = **10.5** % (2025-04-01..2025-06-30) [keep: ] quote: "then to 10.5% in the second quarter and settled at 10.8% in July 2025."
  - p83 Share of total rail tonnage represented by traffic received from US connections, = **10.8** % (2025-07-01..2025-07-31) [keep: ] quote: "then to 10.5% in the second quarter and settled at 10.8% in July 2025."
  - p84 Year-over-year change in Canada's rail imports from the United States, July 2025 = **-16.7** % (2025-07-01..2025-07-31) [keep: ] quote: "Canada's rail imports (-16.7%) and exports (-14.1%) with the United States were also down year over year."
  - p85 Year-over-year change in Canada's rail exports to the United States, July 2025 = **-14.1** % (2025-07-01..2025-07-31) [keep: ] quote: "Canada's rail imports (-16.7%) and exports (-14.1%) with the United States were also down year over year."
  - p86 Year-over-year change in non-intermodal freight traffic in Canada, July 2025 = **1.6** % (2025-07-01..2025-07-31) [keep: ] quote: "Non-intermodal freight traffic in Canada rose 1.6% year over year to 24.2 million tonnes in July 2025"
  - p87 Year-over-year change in intermodal shipments originating in Canada, July 2025 = **9.4** % (2025-07-01..2025-07-31) [keep: ] quote: "intermodal shipments-mainly containers-originating in Canada increased 9.4% compared with July 2024 to 3.2 million tonnes"
- `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2310021901` -> **snapshot** (snapshot 20251115095814); points raw/verified 0/0
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p88 Canada railway carloadings: Intermodal traffic loaded, total, May 2020 = **3,040,663** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p89 Canada railway carloadings: Non-Intermodal traffic loaded, total, May 2020 = **24,396,926** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p90 Canada railway carloadings: Non-Intermodal traffic loaded, total, Apr 2020 = **24,371,149** tonnes (2020-04-01..2020-04-30) [keep: ] quote: "This records an increase from the previous number of 24,371,149.000 Tonne for Apr 2020."
  - p91 Canada railway carloadings: Intermodal traffic loaded, all-time high, May 2019 = **3,255,376** tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p92 Canada railway carloadings: Non-Intermodal traffic loaded, all-time high, Oct 20 = **28,258,207** tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p93 Canada railway carloadings: Non-Intermodal traffic loaded, record low, Jul 2009 = **16,818,939** tonnes (2009-07-01..2009-07-31) [keep: ] quote: "and a record low of 16,818,939.000 Tonne in Jul 2009"
  - p94 Canada railway carloadings: Intermodal traffic loaded, monthly average Jan 1999- = **2,381,505** tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p95 Canada railway carloadings: Non-Intermodal traffic loaded, monthly average Jan 1 = **21,490,478** tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p96 Canada railway carloadings: Non-Intermodal Cement, all-time high, Jul 2019 = **361,023** tonnes (2019-07-01..2019-07-31) [keep: ] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
  - p97 Canada railway carloadings: Non-Intermodal Cement, May 2020 = **247,356** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p98 Canada railway carloadings: Non-Intermodal Animal Feed & Products, May 2020 = **409,186** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p99 Canada railway carloadings: Non-Intermodal Animal or Vegetable Fats, Oils & Flou = **414,481** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p100 Canada railway carloadings: Non-Intermodal Aluminum, May 2020 = **291,832** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p101 Canada railway carloadings: Non-Intermodal Alumina, May 2020 = **126,378** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p102 Canada railway carloadings: Non-Intermodal Automobiles & Mini-Vans, May 2020 = **20,703** tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Automobiles & Mini-Vans data was reported at 20,703.000 Tonne in May 2020."
- `https://www.statcan.gc.ca/o1/fr/app/8532-chargements-ferroviaires-juillet-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] commodity decomposition

Hypothesis: July 2026 commodity-level tonnages (grain, potash, coal, intermodal) from StatCan or RAC would allow a sum-of-components formula_mc, resolving which component drives the total and reducing reliance on a single aggregate change factor.

Queries issued by the searcher: Statistics Canada Table 23-10-0219-01 railway carloadings by commodity tonnes; Railway carloadings monthly July 2025 Statistics Canada The Daily tonnes; "Railway carloadings, July 2026" Statistics Canada; StatCan daily "carloadings" 2026 potash coal wheat tonnes July 2026

- `https://www150.statcan.gc.ca/n1/daily-quotidien/250924/dq250924f-eng.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/canada/railway-carloadings` -> **snapshot** (snapshot 20200821110901); points raw/verified 15/15
  - p103 Canada railway carloadings: intermodal traffic loaded, May 2020 = **3,040,663** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Intermodal Traffic Loaded data was reported at 3,040,663.000 Tonne in May 2020."
  - p104 Canada railway carloadings: non-intermodal traffic loaded, May 2020 = **24,396,926** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal Traffic Loaded data was reported at 24,396,926.000 Tonne in May 2020."
  - p105 Canada railway carloadings: non-intermodal traffic loaded, April 2020 = **24,371,149** metric tonnes (2020-04-01..2020-04-30) [keep: ] quote: "This records an increase from the previous number of 24,371,149.000 Tonne for Apr 2020."
  - p106 Canada railway carloadings: non-intermodal traffic loaded, all-time high (Oct 20 = **28,258,207** metric tonnes (2018-10-01..2018-10-31) [keep: ] quote: "The data reached an all-time high of 28,258,207.000 Tonne in Oct 2018"
  - p107 Canada railway carloadings: non-intermodal traffic loaded, record low (Jul 2009) = **16,818,939** metric tonnes (2009-07-01..2009-07-31) [keep: ] quote: "and a record low of 16,818,939.000 Tonne in Jul 2009"
  - p108 Canada railway carloadings: intermodal traffic loaded, all-time high (May 2019) = **3,255,376** metric tonnes (2019-05-01..2019-05-31) [keep: ] quote: "The data reached an all-time high of 3,255,376.000 Tonne in May 2019"
  - p109 Canada railway carloadings: intermodal traffic loaded, record low (Jan 1999) = **1,264,980** metric tonnes (1999-01-01..1999-01-31) [keep: ] quote: "and a record low of 1,264,980.000 Tonne in Jan 1999"
  - p110 Canada railway carloadings: intermodal traffic loaded, monthly average Jan 1999- = **2,381,505** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 2,381,505.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p111 Canada railway carloadings: non-intermodal traffic loaded, monthly average Jan 1 = **21,490,478** metric tonnes (1999-01-01..2020-05-31) [keep: ] quote: "averaging 21,490,478.000 Tonne from Jan 1999 to May 2020, with 257 observations"
  - p112 Canada railway carloadings: non-intermodal alumina loaded, May 2020 = **126,378** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Alumina data was reported at 126,378.000 Tonne in May 2020."
  - p113 Canada railway carloadings: non-intermodal aluminum loaded, May 2020 = **291,832** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Aluminum data was reported at 291,832.000 Tonne in May 2020."
  - p114 Canada railway carloadings: non-intermodal animal feed & products loaded, May 20 = **409,186** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal Feed & Products data was reported at 409,186.000 Tonne in May 2020."
  - p115 Canada railway carloadings: non-intermodal animal or vegetable fats, oils & flou = **414,481** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Animal or Vegetable Fats, Oils & Flours data was reported at 414,481.000 Tonne in May 2020."
  - p116 Canada railway carloadings: non-intermodal cement loaded, May 2020 = **247,356** metric tonnes (2020-05-01..2020-05-31) [keep: ] quote: "Canada's Railway Carloading Statistics: Non-Intermodal: Cement data was reported at 247,356.000 Tonne in May 2020."
  - p117 Canada railway carloadings: non-intermodal cement loaded, all-time high (Jul 201 = **361,023** metric tonnes (2019-07-01..2019-07-31) [keep: ] quote: "The data reached an all-time high of 361,023.000 Tonne in Jul 2019"
- `https://www150.statcan.gc.ca/n1/en/subjects/transportation/rail_transportation?sourcecode=2732` -> **snapshot** (snapshot 20221001035008); points raw/verified 11/10
  - p118 Canada rail transportation key indicator: metric tonnes (monthly, latest period  = **30,200,000** metric tonnes (not stated (page dated 2022-09-30)) [keep: ] quote: "30.2 million metric tonnes5.6%(12-month change)"
  - p119 Canada rail transportation key indicator: 12-month change in metric tonnes = **5.6** % (not stated (page dated 2022-09-30)) [keep: ] quote: "30.2 million metric tonnes5.6%(12-month change)"
  - p120 Canada rail transportation key indicator: annual change in operating revenue = **5.6** % (not stated (page dated 2022-09-30)) [keep: ] quote: "$16.5 billion5.6%(annual change)"
  - p121 Canada rail transportation key indicator: cumulative tonnes (annual total) = **321,700,000** metric tonnes (not stated (page dated 2022-09-30)) [keep: ] quote: "321.7 million tonnes2.6%(annual change)"
  - p122 Canada rail transportation key indicator: annual change in cumulative tonnes = **2.6** % (not stated (page dated 2022-09-30)) [keep: ] quote: "321.7 million tonnes2.6%(annual change)"
  - p123 Number of commodity groupings in Monthly Railway Carloadings publication tables = **64** commodity groupings (not stated (page dated 2022-09-30)) [keep: ] quote: "a number of tables showing car loadings and tonnes carried by 64 commodity groupings"
  - p124 Number of series in Railway carloadings statistics by commodity table 23-10-0092 = **26** series (not stated (page dated 2022-09-30)) [keep: ] quote: "This table contains 26 series, with data for years 1970 - 1998"
  - p125 Number of commodity items in table 23-10-0092-01 dimension = **26** commodity items (not stated (page dated 2022-09-30)) [keep: ] quote: "Commodity (26 items: Total revenue; cars loaded; Wheat; Other grain and grain products; Fresh fruits and vegetables; ...)"
  - p126 Start year of data coverage in table 23-10-0092-01 = **1,970** year (1970-01-01..1970-12-31) [keep: ] quote: "This table contains 26 series, with data for years 1970 - 1998"
  - p127 End year of data coverage in table 23-10-0092-01 = **1,998** year (1998-01-01..1998-12-31) [keep: ] quote: "This table contains 26 series, with data for years 1970 - 1998"
- `https://in.tradingview.com/news/DJN_DN20260928003565:0/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b3 [shocks] 2026 disruptions

Hypothesis: Any 2026 labour disruption, wildfire, or tariff shock affecting July 2026 rail tonnage would shift the estimate away from the trend; confirming absence or magnitude resolves the largest uncertainty in the change factor.

Queries issued by the searcher: CN CPKC Teamsters strike 2026 Canada rail labour disruption; Statistics Canada Railway carloadings July 2026; "Railway carloadings" June 2026 Statistics Canada The Daily total tonnage million tonnes; Canada wildfires rail disruption July 2026 CN CPKC northern Ontario British Columbia track outage

- `https://www150.statcan.gc.ca/n1/daily-quotidien/260825/dq260825b-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/en/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://author.cpkcr.com/es/medios-de-comunicacion/Bargaining-Updates-IBEW` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.trains.com/pro/freight/class-i/?filter_tag=fallen-flags%2Cshort-lines-regionals%2Ckansas-city-southern%2Ccanada` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['railway carloadings', 'canada freight tonnes', 'statcan rail']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45'] All from the same StatCan December 2025 / annual 2025 release; internally consistent decomposition (non-intermodal + intermodal + US-connection traffic ≈ total). Shared source, so not independent conf
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50', 'p51'] Commodity-level 2025 annual tonnages from the same StatCan release; sum to a large share of non-intermodal loadings. Useful for commodity decomposition and for judging which components swing in July.
- corroborating: ['p52', 'p53', 'p54', 'p55', 'p56', 'p69', 'p70'] CPKC and CN+CPKC crop-year grain records for 2025-26 (Aug 2025-Jul 2026). p52 (CPKC 30.66 Mt) is a subset of p69 (CN+CPKC 64.0 Mt); consistent with a strong grain year running through July 2026.
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68'] RAC weekly/period data for 2026: flat carloads, +4% RTMs YTD, grain & fertilizers +11% carloads/+13% RTMs. Same underlying source (RAC), so mutually dependent; provides the 2026-vs-2025 change signal.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] CEIC-sourced StatCan total traffic carried series 1999-2020; consistent levels (monthly avg 26.4 Mt, Oct 2018 peak 34.8 Mt). Older vintage but same definition family as the target.
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] Non-intermodal and intermodal loaded traffic series (2020 vintage). p7+p12 ≈ total for April 2020; p23+p22 ≈ total for May 2020. Consistent with the p37-p45 decomposition, though a different (older) v
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Commodity-level non-intermodal tonnages for 2020; small components relative to total, useful only as context for commodity mix.
- corroborating: ['p58', 'p71', 'p72'] Early 2026-27 crop-year grain flow signals (hopper fulfillment 88-90%, ~1.1 Mt/week grain). Indicates grain flows remained strong into August 2026, supporting a strong July 2026 grain component.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45'] All from the same StatCan December 2025 / annual 2025 release; internally consistent (Dec total 31.0 = 24.8 non-intermodal + 2.8 intermodal + 3.3 US connections). Shared source, so not independent con
- corroborating: ['p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87'] All from the same StatCan July 2025 Daily release. July 2025 total 30.7 Mt (24.2 non-intermodal + 3.2 intermodal + 3.3 US connections = 30.7). This is the single most valuable anchor: same month, same
- corroborating: ['p73', 'p75'] July 2025 (30.7 Mt) is slightly above the five-year July average (29.8 Mt), consistent with a stable July seasonal level around 30 Mt.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5'] CEIC 2020-vintage series of total traffic carried; internally consistent but a different vintage/definition era than the 2025 StatCan Daily figures. Useful only as long-run level context, not for dire
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111'] CEIC 2020-vintage non-intermodal + intermodal series; many are duplicate copies of the same underlying StatCan table. They corroborate the ~24-28 Mt non-intermodal / ~3 Mt intermodal split but are 202
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p34', 'p35', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117'] Commodity-level May 2020 / July 2019 CEIC points; duplicates of each other. Too small and too old to drive the total; only contextual.
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72'] RAC 2026 weekly/YTD data: carloads flat, RTMs +4% YTD, grain & fertilizers +11% carloads / +13% RTMs, grain crop-year 64.0 Mt (+15%). Consistent picture of a modestly stronger 2026 than 2025, driven b
- corroborating: ['p52', 'p69', 'p70'] CPKC 30.66 Mt grain 2025-26 and RAC 64.0 Mt CN+CPKC grain 2025-26 (+15%) are consistent (CPKC ~48% share).
- corroborating: ['p58', 'p71', 'p72'] Hopper fulfillment 88-90% and strong early 2026-27 crop-year grain volumes (+49% vs 3-yr avg) indicate no grain-supply constraint into July/August 2026.
- corroborating: ['p37', 'p73'] December 2025 (31.0 Mt) and July 2025 (30.7 Mt) are close, consistent with a stable ~30-31 Mt monthly level in 2025.
- corroborating: ['p118', 'p119', 'p121', 'p122'] 2022-vintage StatCan key indicator (30.2 Mt monthly, 321.7 Mt annual) is consistent with the ~30 Mt monthly level; older vintage, contextual only.
- corroborating: ['p123', 'p124', 'p125', 'p126', 'p127'] Metadata about table structure; not numeric evidence for the target.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 total traffic vs July 2025 change factor | 1.03 | 0.95..1.11 | 0.9185..1.148 (widened) | ratio | m2 (m2) | RAC 2026 YTD shows carloads flat and RTMs +4% (p61), with grain & fertilizers +11% carloads / +13% RTMs (p64-p67) and grain crop-year +15% (p70). Grain is a large July component, so a modest positive change is expected; metals/minerals flat (p68) and US-connection traffic weak in 2025 (p42, p76) tem | July 2026 tonnage tracks the RAC YTD direction and no major disruption hits July 2026. | Evidence of a July 2026 labour disruption, wildfire, or tariff shock cutting volumes, or RAC data showing a sharp July decline. |
| a2 | July seasonal factor relative to annual monthly average | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m1 (m1), m3 (m3) | July 2025 (30.7 Mt, p73) is close to the 2025 monthly average (376.6/12 = 31.4 Mt, p38) and slightly above the five-year July average (29.8 Mt, p75). July is a moderate-to-strong month but not a sharp peak; factor near 1.0 with modest spread. | The 2026 annual level is similar to 2025 and July is a near-average month. | Evidence that July 2026 is a strong grain peak far above the annual average, or a collapse below it. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 31,386,602 | ['p38'] / ['a2'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 31,454,543 | ['p73'] / ['a1'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 26,395,421 | ['p3'] / ['a2'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **29,647,319** t, 80% interval [20,062,099, 43,812,140] t, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total freight carried by Canadian railways (all traffic, Canada) in July 2026 is 29,647,319 t (80% model-based interval 20,062,099 to 43,812,140 t). This targets the headline total traffic tonnage for the calendar month, as first published.

Three methods were combined with equal weights (33%, 33%, 33%): an annual-average scaling (31,386,602), a year-over-year scaling of July 2025 (31,454,543), and a long-run average cross-check (26,395,421). Observed anchors are the 2025 annual total (376,600,000 metric tonnes), July 2025 (30,700,000 metric tonnes) and the [n]-2020 monthly average (26,443,500 tonnes). The 2026 change factor (1.03, range 0.9185 to 1.148) and July seasonal factor (1, range 0.7058 to 1.412) are analyst assumptions, not observations. Equal weighting reflects the absence of backtest years, not demonstrated accuracy.

The main risk is that the assumed 2026 change factor is wrong, especially for grain and weak US-connection traffic. Actual July 2026 carloadings data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 total traffic vs July 2025 change factor: 1.03 ratio, range 0.9185 to 1.148 (range widened by code); used by m2. Overturned by: Evidence of a July 2026 labour disruption, wildfire, or tariff shock cutting volumes, or RAC data showing a sharp July decline.
- a2 July seasonal factor relative to annual monthly average: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m1, m3. Overturned by: Evidence that July 2026 is a strong grain peak far above the annual average, or a collapse below it.

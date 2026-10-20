# Evidence ledger: fc_ca_rail_2026_07

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the total freight carried by Canadian railways in July 2026, in tonnes, as it will be first reported by Statistics Canada in its monthly Railway carloadings release (total traffic carried, Canada).
- as_of: 2026-08-29
- Pinned target: Total freight carried by Canadian railways in July 2026, as first reported by Statistics Canada in its monthly Railway carloadings release; working interpretation is Canada-level total revenue-freight tonnage carried during the calendar month, including all commodities and intermodal traffic in the  | unit metric tonnes | period 2026-07-01..2026-07-31 | publisher Statistics Canada (Railway carloadings, Table 23-10-0086-01)

- Official value (scoring only, never shown to the agent): 31,686,803

## Directions and pages

### d1 [own_history] Statistics Canada historical-series analyst

Hypothesis: July total tonnage has recurring seasonal patterns and a recent trend; prior July values and Jan-Jun 2026 year-over-year changes constrain July 2026 even without the July print.

Queries issued by the searcher: Statistics Canada railway carloadings July 2025 total tonnes; Table 23-10-0086-01 railway carloadings monthly Canada; "Railway carloadings" June 2026 Statistics Canada Daily tonnes; statcan 23-10-0086-01 railway carloadings total tonnage transported monthly table

- `https://tdih-cdit.tc.canada.ca/en/search/23100216?facets_query=&23100216_facets%5B0%5D=23100216_components%3ACanola&23100216_facets%5B1%5D=23100216_co` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.statcan.gc.ca/o1/en/app/8532-railway-carloadings-july-2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/250226/cg-d001-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] rail operator weekly performance monitor

Hypothesis: July 2026 total tonnes can be reconstructed from weekly carloads by commodity multiplied by average payloads; weekly carloads are an early indicator of the monthly total.

Queries issued by the searcher: July 2026 weekly railway carloadings Canada Statistics Canada; Canadian railways carloads week ending July 2026; AAR week 30 2026 Canadian railroads carloads week ending August 1; StatCan table 23-10-0086-01 railway carloadings weekly tonnage July 2026

- `https://ycharts.com/indicators/canadian_weekly_rail_traffic` -> **snapshot** (snapshot 20150512061019); points raw/verified 15/15
  - p1 Canadian rail traffic weekly carloads, week of May 2 2015 (AAR Weekly Rail Traff = **143,722** carloads (2015-04-26..2015-05-02) [keep: ] quote: "Canadian Rail Traffic is at a current level of 143722.0, up from last week and down from 146911.0 one year ago."
  - p2 Canadian rail traffic weekly carloads, week of April 25 2015 = **144,067** carloads (2015-04-19..2015-04-25) [keep: ] quote: "\| April 25, 2015 \| 144067.0 \|"
  - p3 Canadian rail traffic weekly carloads, week of April 18 2015 = **144,149** carloads (2015-04-12..2015-04-18) [keep: ] quote: "\| April 18, 2015 \| 144149.0 \|"
  - p4 Canadian rail traffic weekly carloads, week of April 11 2015 = **142,746** carloads (2015-04-05..2015-04-11) [keep: ] quote: "\| April 11, 2015 \| 142746.0 \|"
  - p5 Canadian rail traffic weekly carloads, week of April 4 2015 = **139,656** carloads (2015-03-29..2015-04-04) [keep: ] quote: "\| April 4, 2015 \| 139656.0 \|"
  - p6 Canadian rail traffic weekly carloads, week of March 28 2015 = **145,439** carloads (2015-03-22..2015-03-28) [keep: ] quote: "\| March 28, 2015 \| 145439.0 \|"
  - p7 Canadian rail traffic weekly carloads, week of March 21 2015 = **136,550** carloads (2015-03-15..2015-03-21) [keep: ] quote: "\| March 21, 2015 \| 136550.0 \|"
  - p8 Canadian rail traffic weekly carloads, week of March 14 2015 = **138,016** carloads (2015-03-08..2015-03-14) [keep: ] quote: "\| March 14, 2015 \| 138016.0 \|"
  - p9 Canadian rail traffic weekly carloads, week of March 7 2015 = **134,937** carloads (2015-03-01..2015-03-07) [keep: ] quote: "\| March 7, 2015 \| 134937.0 \|"
  - p10 Canadian rail traffic weekly carloads, week of Feb. 28 2015 = **133,541** carloads (2015-02-22..2015-02-28) [keep: ] quote: "\| Feb. 28, 2015 \| 133541.0 \|"
  - p11 Canadian rail traffic weekly carloads, week of Feb. 21 2015 = **119,858** carloads (2015-02-15..2015-02-21) [keep: ] quote: "\| Feb. 21, 2015 \| 119858.0 \|"
  - p12 Canadian rail traffic weekly carloads, week of Feb. 14 2015 = **137,383** carloads (2015-02-08..2015-02-14) [keep: ] quote: "\| Feb. 14, 2015 \| 137383.0 \|"
  - p13 Canadian rail traffic weekly carloads, week of Feb. 7 2015 = **131,685** carloads (2015-02-01..2015-02-07) [keep: ] quote: "\| Feb. 7, 2015 \| 131685.0 \|"
  - p14 Canadian rail traffic weekly carloads, week of Jan. 31 2015 = **141,291** carloads (2015-01-25..2015-01-31) [keep: ] quote: "\| Jan. 31, 2015 \| 141291.0 \|"
  - p15 Canadian rail traffic weekly carloads, week of Jan. 24 2015 = **139,540** carloads (2015-01-18..2015-01-24) [keep: ] quote: "\| Jan. 24, 2015 \| 139540.0 \|"
- `https://local.newsbreak.com/trains-com-315688185/4785269414182-upswing-continues-for-u-s-rail-traffic` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aar.org/news/aar-reports-weekly-rail-traffic-for-the-week-ending-august-1-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aar.org/wp-content/uploads/2026/07/2026-07-08-railtraffic.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] commodity supply and export analyst

Hypothesis: Total rail tonnage is the sum of major commodity flows (grain, coal, potash, crude oil, forest products, metals, intermodal); July 2026 export/production indicators for these commodities plus rail shares can approximate most of the total, with a residual allowance.

Queries issued by the searcher: Canada grain rail shipments July 2026 Statistics Canada railway carloadings; Statistics Canada railway carloadings July 2026 total tonnage; Canada potash rail shipments July 2026 potash exports Canpotex; Canada coal exports July 2026 Vancouver Prince Rupert coal terminal volumes

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradersunion.com/news/financial-news/show/3543020-canadian-rail-freight-july-rise/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.railwayage.com/intermodal/potash-is-in-the-headlines-here-is-where-it-actually-goes/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] port terminal throughput analyst

Hypothesis: Rail-served export throughput at major Canadian ports is a large identifiable component of total rail tonnage; port July 2026 cargo by rail plus an allowance for domestic and transborder traffic constrains the total.

Queries issued by the searcher: Port of Vancouver July 2026 grain rail shipments; Prince Rupert port July 2026 coal grain volumes; Vancouver Fraser Port Authority July 2026 monthly cargo volumes statistics; Statistics Canada Railway carloadings July 2026 million tonnes

- `https://www.grainmonitor.ca/Downloads/MonthlyReports/MonthlyReport202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://coal.mysteel.com/a/26082609/A849CD92468EF9A5.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://airfreight.news/articles/full/ajot-robust-cargo-trends-continue-at-port-of-prince-rupert` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jetro.go.jp/biznews/2026/07/bdc45ab5cefd02fb.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] rail operations planner

Hypothesis: Realised tonnage is constrained by loaded-car capacity, loaded-car utilisation, train starts, and operating days; July 2026 operating metrics such as car miles, average train weight, and loaded cars track the tonnage level.

Queries issued by the searcher: Statistics Canada Railway carloadings July 2026; CN Rail July 2026 carloads revenue ton miles; CPKC July 2026 carloads operating metrics; Canadian railway operating metrics July 2026 car miles train starts

- `https://www.ceicdata.com.cn/zh-hans/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://getfea.com/transportation/canadian-rail-freight-volume-rises-2-6-year-over-year-in-july` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://investor.cpkcr.com/key-metrics/default.aspx?section=Definitions` -> **snapshot** (snapshot 20260222082659); points raw/verified 0/0
- `http://ecprod.cn.ca/corp/en/investors/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [related_series] industrial statistics and modal-share analyst

Hypothesis: Non-export domestic rail tonnage relates to Canadian industrial shipments by sector multiplied by rail mode share; July 2026 manufacturing, mining, and agricultural marketings constrain the domestic component.

Queries issued by the searcher: Statistics Canada Railway carloadings monthly total tonnage 2026; Statistics Canada manufacturing shipments June 2026; "Railway carloadings, June 2026" Statistics Canada The Daily; "Railway carloadings, July 2025" Statistics Canada million tonnes

- `https://www.ceicdata.com.cn/en/canada/railway-carloadings/railway-carloading-statistics-total-traffic-carried` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260224/cg-c001-eng.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/daily-quotidien/260427/dq260427a-eng.htm` -> **snapshot** (snapshot 20260615232806); points raw/verified 15/15
  - p16 Total cargo carried by Canadian railways, February 2026 = **29,400,000** metric tonnes (2026-02-01..2026-02-28) [keep: ] quote: "In February, the volume of cargo carried by Canadian railways totalled 29.4 million tonnes, up 9.8% from February 2025"
  - p17 Year-over-year change in total cargo carried by Canadian railways, February 2026 = **9.8** % (2026-02-01..2026-02-28) [keep: ] quote: "29.4 million metric tonnes February 2026 9.8% (12-month change)"
  - p18 High for February total cargo carried by Canadian railways (February 2024) = **30,700,000** metric tonnes (2024-02-01..2024-02-29) [keep: ] quote: "just under the high of 30.7 million tonnes from February 2024"
  - p19 Non-intermodal commodity traffic in Canada, February 2026 = **23,200,000** metric tonnes (2026-02-01..2026-02-28) [keep: ] quote: "commodity traffic in Canada grew 8.3% to 23.2 million tonnes in February 2026"
  - p20 Year-over-year growth in commodity traffic in Canada, February 2026 = **8.3** % (2026-02-01..2026-02-28) [keep: ] quote: "commodity traffic in Canada grew 8.3% to 23.2 million tonnes in February 2026"
  - p21 Intermodal shipments originating in Canada, February 2026 = **3,000,000** metric tonnes (2026-02-01..2026-02-28) [keep: ] quote: "intermodal shipments-mainly containers-originating in Canada rose 15.0% year over year to 3.0 million tonnes"
  - p22 Year-over-year change in intermodal shipments originating in Canada, February 20 = **15** % (2026-02-01..2026-02-28) [keep: ] quote: "intermodal shipments-mainly containers-originating in Canada rose 15.0% year over year to 3.0 million tonnes"
  - p23 Freight loadings from US rail connections into Canada, February 2026 = **3,200,000** metric tonnes (2026-02-01..2026-02-28) [keep: ] quote: "Tonnage was up 16.1% from February 2025 to reach 3.2 million tonnes"
  - p24 Year-over-year change in freight loadings from US rail connections into Canada,  = **16.1** % (2026-02-01..2026-02-28) [keep: ] quote: "Tonnage was up 16.1% from February 2025 to reach 3.2 million tonnes"
  - p25 Five-year average of February freight loadings from US rail connections into Can = **3,400,000** metric tonnes (2026-02-01..2026-02-28) [keep: ] quote: "remained below the previous five-year average of 3.4 million tonnes for the month of February"
  - p26 Average monthly share of total rail tonnage from US rail connections into Canada = **12** % (2023-01-01..2024-12-31) [keep: ] quote: "Over 2023 and 2024, freight loadings from US rail connections into Canada represented an average of 12.0% of total rail tonnage each month."
  - p27 Average share of total rail tonnage from US rail connections into Canada, 2025 = **10.4** % (2025-01-01..2025-12-31) [keep: ] quote: "This share declined throughout 2025, averaging 10.4% during the year"
  - p28 Share of total rail tonnage from US rail connections into Canada, January and Fe = **11** % (2026-01-01..2026-02-28) [keep: ] quote: "then approached 11.0% in January and February 2026"
  - p29 Year-over-year increase in potash loadings, February 2026 = **26.8** % (2026-02-01..2026-02-28) [keep: ] quote: "Leading the gain was potash, with loadings rising sharply by 26.8% (+438 000 tonnes) from February 2025."
  - p30 Year-over-year increase in canola loadings, February 2026 = **59.1** % (2026-02-01..2026-02-28) [keep: ] quote: "loadings of canola grew 59.1% (+325 000 tonnes) in February 2026 compared with February 2025"
- `https://in.marketscreener.com/news/canada-manufacturing-sales-rise-for-fifth-straight-month-in-june-update-ce7859ded08aff23` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [base_rates] freight conversion analyst

Hypothesis: Carload counts convert to tonnes via commodity-specific average payloads and intermodal TEU weights; these parameters bridge weekly carload evidence to the tonnage target.

Queries issued by the searcher: Statistics Canada railway carloadings average tonnes per carload by commodity; average tonnes per railcar grain coal potash Canada payload; intermodal rail container average tonnes Canada Statistics Canada carloadings; Table 23-10-0086-01 railway carloadings weight tonnes commodity Canada

- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/11027/11030-railway-carloadings-april-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/en/daily-quotidien/240920/dq240920c-eng.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tdih-cdit.tc.canada.ca/en/search/23100216` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www150.statcan.gc.ca/n1/pub/52-001-x/2013010/t003-eng.htm` -> **snapshot** (snapshot 20230222132509); points raw/verified 15/15
  - p31 Wheat carloads, Eastern Division, October 2013 = **929** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Wheat \| 929 \| 85,951 \| 848 \| 79,007 \|"
  - p32 Wheat tonnage, Eastern Division, October 2013 = **85,951** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Wheat \| 929 \| 85,951 \| 848 \| 79,007 \|"
  - p33 Coal carloads, Eastern Division, October 2013 = **1,305** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Coal \| 1,305 \| 106,400 \| 1,221 \| 101,492 \|"
  - p34 Coal tonnage, Eastern Division, October 2013 = **106,400** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Coal \| 1,305 \| 106,400 \| 1,221 \| 101,492 \|"
  - p35 Potash carloads, Eastern Division, October 2013 = **547** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Potash \| 547 \| 55,003 \| 811 \| 81,502 \|"
  - p36 Potash tonnage, Eastern Division, October 2013 = **55,003** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Potash \| 547 \| 55,003 \| 811 \| 81,502 \|"
  - p37 Fuel oils and crude petroleum carloads, Eastern Division, October 2013 = **4,084** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Fuel oils and crude petroleum \| 4,084 \| 336,576 \| 4,536 \| 368,629 \|"
  - p38 Fuel oils and crude petroleum tonnage, Eastern Division, October 2013 = **336,576** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Fuel oils and crude petroleum \| 4,084 \| 336,576 \| 4,536 \| 368,629 \|"
  - p39 Iron ores and concentrates carloads, Eastern Division, October 2013 = **36,986** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Iron ores and concentrates \| 36,986 \| 3,422,749 \| 33,783 \| 3,103,328 \|"
  - p40 Iron ores and concentrates tonnage, Eastern Division, October 2013 = **3,422,749** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Iron ores and concentrates \| 36,986 \| 3,422,749 \| 33,783 \| 3,103,328 \|"
  - p41 Total non-intermodal traffic loaded, number of rail cars, Eastern Division, Octo = **138,465** rail cars (2013-10-01..2013-10-31) [keep: ] quote: "\| Total non-intermodal traffic loaded 2 \| 138,465 \| 9,922,701 \| 132,810 \| 9,378,990 \|"
  - p42 Total non-intermodal traffic loaded, metric tonnes, Eastern Division, October 20 = **9,922,701** metric tonnes (2013-10-01..2013-10-31) [keep: ] quote: "\| Total non-intermodal traffic loaded 2 \| 138,465 \| 9,922,701 \| 132,810 \| 9,378,990 \|"
  - p43 Total non-intermodal traffic loaded, number of rail cars, Eastern Division, Octo = **132,810** rail cars (2012-10-01..2012-10-31) [keep: ] quote: "\| Total non-intermodal traffic loaded 2 \| 138,465 \| 9,922,701 \| 132,810 \| 9,378,990 \|"
  - p44 Total non-intermodal traffic loaded, metric tonnes, Eastern Division, October 20 = **9,378,990** metric tonnes (2012-10-01..2012-10-31) [keep: ] quote: "\| Total non-intermodal traffic loaded 2 \| 138,465 \| 9,922,701 \| 132,810 \| 9,378,990 \|"
  - p45 Coal tonnage, Eastern Division, October 2012 = **101,492** metric tonnes (2012-10-01..2012-10-31) [keep: ] quote: "\| Coal \| 1,305 \| 106,400 \| 1,221 \| 101,492 \|"

### d8 [shocks] disruption and calendar-effects analyst

Hypothesis: July 2026 tonnage may deviate from seasonal baseline because of wildfires, labour disruptions, port closures, tariffs, or grain harvest timing; dated events up to the cutoff can adjust the baseline directionally or quantitatively.

Queries issued by the searcher: Canada railway disruption July 2026 wildfires rail; Statistics Canada Railway carloadings July 2026; British Columbia wildfires railway CN CPKC service disruption July 2026; Vancouver port rail strike July 2026 Canada freight disruption

- `https://www.portvancouver.com/article/port-vancouver-operations-update-1-wildfire-near-boston-bar-british-columbia` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.theglobeandmail.com/business/article-northern-ontario-wildfires-disrupt-rail-forestry-operations/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sdr-daily-alpha.cloud.statcan.ca/en/thedaily/searchindicators?title=Chargements+ferroviaires,+tonnage+total&wbdisable=true` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://iamovers.org/news/b-c-wildfires-keep-pressure-on-rail-corridor/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a** t, 80% interval [n/a, n/a] t, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

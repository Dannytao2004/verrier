# Evidence ledger: fc_nz_exports_2026_03

- Question: Assume today is 2026-03-21. You know nothing published after this date. Estimate the total value of New Zealand's goods exports in March 2026 (actual monthly value, not seasonally adjusted), in New Zealand dollars (NZD), as it will be first reported in Stats NZ's monthly Overseas merchandise trade release.
- as_of: 2026-03-21
- Pinned target: Total value of New Zealand goods exports (overseas merchandise trade, exports f.o.b.) for the calendar month of March 2026, as first published by Stats NZ in its monthly Overseas Merchandise Trade release | unit NZD | period 2026-03-01..2026-03-31 | publisher Stats NZ (Statistics New Zealand)

- Official value (scoring only, never shown to the agent): 7,943,894,499

## Directions and pages

### d1 [own_history] Stats NZ time series

Hypothesis: March export values follow a recurring seasonal pattern; the March 2026 value can be projected from prior March values plus recent monthly trend. Role: baseline level and seasonality.

Queries issued by the searcher: Stats NZ overseas merchandise trade March 2025 exports monthly value; New Zealand goods exports monthly value March 2024 March 2023 Stats NZ overseas merchandise trade; figure.nz table "total exports" monthly overseas merchandise trade exports fob New Zealand dollars; "overseas merchandise trade" February 2026 exports Stats NZ

- `https://www.stats.govt.nz/insights/?dateFiltersID=100&filters=Information+releases%2COverseas+merchandise+trade&sort=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.scoop.co.nz/stories/BU2504/S00380/overseas-merchandise-trade-march-2025.htm` -> **snapshot** (snapshot 20250524003041); points raw/verified 7/7
  - p1 New Zealand goods exports, March 2025 (actual, f.o.b.) = **7,600,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p2 New Zealand goods exports, March 2025 vs March 2024, change in value = **1,200,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p3 New Zealand goods exports, March 2025 vs March 2024, percentage change = **19** % (2025-03-01..2025-03-31) [keep: ] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p4 New Zealand goods imports, March 2025 (actual) = **6,600,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p5 New Zealand goods imports, March 2025 vs March 2024, change in value = **723,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p6 New Zealand goods imports, March 2025 vs March 2024, percentage change = **12** % (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p7 New Zealand monthly goods trade balance, March 2025 (surplus) = **970,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "the monthly trade balance was a surplus of $970 million."
- `https://www.scoop.co.nz/stories/print.html?path=BU2404/S00337/overseas-merchandise-trade-march-2024-information-release.htm` -> **snapshot** (snapshot 20240424013423); points raw/verified 7/7
  - p8 New Zealand goods exports, March 2024, level = **6,500,000,000** NZD (2024-03-01..2024-03-31) [keep: ] quote: "goods exports rose by $240 million (3.8 percent), to $6.5 billion"
  - p9 New Zealand goods exports, March 2024 vs March 2023, change in NZD = **240,000,000** NZD (2024-03-01..2024-03-31) [keep: ] quote: "goods exports rose by $240 million (3.8 percent), to $6.5 billion"
  - p10 New Zealand goods exports, March 2024 vs March 2023, percent change = **3.8** % (2024-03-01..2024-03-31) [keep: ] quote: "goods exports rose by $240 million (3.8 percent), to $6.5 billion"
  - p11 New Zealand goods imports, March 2024, level = **5,900,000,000** NZD (2024-03-01..2024-03-31) [keep: ] quote: "goods imports fell by $1.9 billion (25 percent), to $5.9 billion"
  - p12 New Zealand goods imports, March 2024 vs March 2023, change in NZD = **1,900,000,000** NZD (2024-03-01..2024-03-31) [keep: ] quote: "goods imports fell by $1.9 billion (25 percent), to $5.9 billion"
  - p13 New Zealand goods imports, March 2024 vs March 2023, percent change = **25** % (2024-03-01..2024-03-31) [keep: ] quote: "goods imports fell by $1.9 billion (25 percent), to $5.9 billion"
  - p14 New Zealand monthly goods trade balance, March 2024, surplus = **588,000,000** NZD (2024-03-01..2024-03-31) [keep: ] quote: "the monthly trade balance was a surplus of $588 million."
- `https://www.interest.co.nz/economy/132967/bumper-exports-dairy-meat-and-fruit-give-nz-its-biggest-monthly-goods-trade-surplus` -> **snapshot** (snapshot 20260207084214); points raw/verified 15/15
  - p15 New Zealand monthly goods exports, March 2025 (actual, f.o.b.) = **7,590,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "the $7.59 billion worth of the exports in March 2025 is, just in pure in dollar terms, the biggest figure ever."
  - p16 New Zealand monthly merchandise trade surplus, March 2025 = **970,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "we need to go back to April 2011 to find a larger monthly trade surplus than the $970 million recorded in March 2025."
  - p17 Year-on-year change in New Zealand goods exports, March 2025 vs March 2024 (perc = **19** % (2025-03-01..2025-03-31) [keep: ] quote: "Statistics NZ said the $7.59 billion export figure was up 19% ($1.2 billion) on the figure for March 2024."
  - p18 Year-on-year change in New Zealand goods exports, March 2025 vs March 2024 (NZD) = **1,200,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "Statistics NZ said the $7.59 billion export figure was up 19% ($1.2 billion) on the figure for March 2024."
  - p19 New Zealand annual goods exports, year ended March 2025 = **74,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Looking at the 12 month picture, annual goods exports were valued at $74.1 billion, up $5.1 billion from the previous year."
  - p20 Year-on-year change in New Zealand annual goods exports, year ended March 2025 = **5,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "annual goods exports were valued at $74.1 billion, up $5.1 billion from the previous year."
  - p21 New Zealand annual goods imports, year ended March 2025 = **80,200,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Annual goods imports were valued at $80.2 billion, up $1.3 billion from the previous year."
  - p22 Year-on-year change in New Zealand annual goods imports, year ended March 2025 = **1,300,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Annual goods imports were valued at $80.2 billion, up $1.3 billion from the previous year."
  - p23 New Zealand annual trade deficit, year ended March 2025 = **6,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "The annual trade deficit was $6.1 billion, which was down on the $10.0 billion in the year ended March 2024."
  - p24 New Zealand annual trade deficit, year ended March 2024 = **10,000,000,000** NZD (2023-04-01..2024-03-31) [keep: ] quote: "The annual trade deficit was $6.1 billion, which was down on the $10.0 billion in the year ended March 2024."
  - p25 March 2025 rise in New Zealand exports of milk powder, butter, and cheese (NZD) = **596,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "Big contributions to the rise came from milk powder, butter, and cheese, up $596 million (35%);"
  - p26 March 2025 rise in New Zealand exports of meat and edible offal (NZD) = **286,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "meat and edible offal, up $286 million (34%);"
  - p27 March 2025 rise in New Zealand exports of fruit (NZD) = **271,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "fruit, up $271 million (74%);"
  - p28 March 2025 rise in New Zealand exports of mechanical machinery and equipment (NZ = **93,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "mechanical machinery and equipment, up $93 million (50%)"
  - p29 March 2025 rise in New Zealand exports to China (NZD) = **371,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "there were big rises compared with March 2024 in exports to China, up $371 million (23 percent), the EU, up $223 million (51%) and the US, up $176 million (22%)."

### d2 [related_series] Stats NZ / trading partners

Hypothesis: March exports are dominated by dairy, meat, and forestry; projecting each major commodity's March value and summing gives the total. Role: component decomposition.

Queries issued by the searcher: Stats NZ overseas merchandise trade exports by commodity monthly dairy meat logs; New Zealand goods exports March 2025 total value Stats NZ overseas merchandise trade; "Overseas merchandise trade" February 2026 Stats NZ goods exports dairy; New Zealand exports January 2026 Stats NZ dairy meat logs monthly value

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://www.publicnow.com/view/10C229F2A0627E8C1F9652979D43D04A41D80E51?1745282740` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/1037/2026-03-16/1313374/ams_1037_00184.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mfat.govt.nz/assets/Trade-General/Trade-Market-reports/Trade-and-Economic-Update-Q1-2025-July-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Trading partner import statistics

Hypothesis: Partner-reported imports from NZ (e.g., China, Australia, US customs) for March 2026 approximate NZ exports to those partners; summing major partners gives total. Role: independent cross-check via mirror statistics.

Queries issued by the searcher: Stats NZ overseas merchandise trade February 2026 exports China Australia United States; China customs imports from New Zealand January 2026 monthly; ABS Australia merchandise imports country New Zealand January 2026 monthly; Census Bureau US imports from New Zealand January 2026 goods trade

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://www.ceicdata.com.cn/zh-hans/indicator/new-zealand/total-exports-to-china` -> **snapshot** (snapshot 20250921232513); points raw/verified 15/1
  - p30 New Zealand total goods exports growth, monthly, percent (Jan 2025) = **28.3** percent (2025-01-01..2025-01-31) [DISCARD: Single-month Jan 2025 YoY growth from a secondary aggregator; wrong month, not a March anchor, and not part of a usable ] quote: "出口总额增长 (%) \| 28.3 Jan 2025"
- `http://english.customs.gov.cn/Statics/9748b88f-8f32-4d68-9df1-d13ad7ad18e6.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ycharts.com/indicators/australia_imports_from_new_zealand` -> **snapshot** (snapshot 20151225145412); points raw/verified 12/12
  - p31 Australia imports from New Zealand, latest value (Oct 2015), AUD = **720,000,000** AUD (2015-10-01..2015-10-31) [DISCARD: Australia mirror import series is 2015 vintage, AUD, single partner; too stale and narrow to project March 2026 total ex] quote: "Australia Imports from New Zealand is at a current level of 720.00M, up from 671.00M last month and up from 709.00M one year ago."
  - p32 Australia imports from New Zealand, previous month (Sept 2015), AUD = **671,000,000** AUD (2015-09-01..2015-09-30) [DISCARD: Same stale 2015 Australia mirror series; redundant and unusable for 2026.] quote: "Australia Imports from New Zealand is at a current level of 720.00M, up from 671.00M last month and up from 709.00M one year ago."
  - p33 Australia imports from New Zealand, one year ago (Oct 2014), AUD = **709,000,000** AUD (2014-10-01..2014-10-31) [DISCARD: Same stale 2015 Australia mirror series; redundant and unusable for 2026.] quote: "Australia Imports from New Zealand is at a current level of 720.00M, up from 671.00M last month and up from 709.00M one year ago."
  - p34 Australia imports from New Zealand, month-over-month change (Oct 2015 vs Sept 20 = **7.3** % (2015-10-01..2015-10-31) [DISCARD: Same stale 2015 Australia mirror series; redundant and unusable for 2026.] quote: "This is a change of 7.30% from last month and 1.55% from one year ago."
  - p35 Australia imports from New Zealand, year-over-year change (Oct 2015 vs Oct 2014) = **1.55** % (2015-10-01..2015-10-31) [DISCARD: Same stale 2015 Australia mirror series; redundant and unusable for 2026.] quote: "This is a change of 7.30% from last month and 1.55% from one year ago."
  - p36 Australia imports from New Zealand, March 2015, AUD = **673,000,000** AUD (2015-03-01..2015-03-31) [DISCARD: 2015 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| March 31, 2015 \| 673.00M \|"
  - p37 Australia imports from New Zealand, March 2014, AUD = **742,000,000** AUD (2014-03-01..2014-03-31) [DISCARD: 2014 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| March 31, 2014 \| 742.00M \|"
  - p38 Australia imports from New Zealand, March 2013, AUD = **627,000,000** AUD (2013-03-01..2013-03-31) [DISCARD: 2013 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| March 31, 2013 \| 627.00M \|"
  - p39 Australia imports from New Zealand, March 2012, AUD = **650,000,000** AUD (2012-03-01..2012-03-31) [DISCARD: 2012 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| March 31, 2012 \| 650.00M \|"
  - p40 Australia imports from New Zealand, first period value (Jan 1988), AUD = **109,000,000** AUD (1988-01-01..1988-01-31) [DISCARD: 1988 Australia mirror value; irrelevant to 2026.] quote: "First Value: 109.00M"
  - p41 Australia imports from New Zealand, December 2014, AUD = **726,000,000** AUD (2014-12-01..2014-12-31) [DISCARD: 2014 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| Dec. 31, 2014 \| 726.00M \|"
  - p42 Australia imports from New Zealand, January 2015, AUD = **487,000,000** AUD (2015-01-01..2015-01-31) [DISCARD: 2015 Australia mirror value; too old and narrow for 2026 projection.] quote: "\| Jan. 31, 2015 \| 487.00M \|"
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 14)

### d4 [forecasts_markets] Forecasters / Treasury / banks

Hypothesis: Published forecasts or nowcasts of NZ goods exports for Q1 2026 or March 2026 provide a direct anchor. Role: forecast input.

Queries issued by the searcher: New Zealand goods exports forecast March 2026 Overseas Merchandise Trade; NZ trade balance forecast Q1 2026 exports ANZ Westpac; NZIER Consensus Forecasts March 2026 exports volume; "trade balance" New Zealand February 2026 exports NZ$ billion Stats NZ release March 2026

- `https://www.nzier.org.nz/publications/nzier-consensus-forecasts-show-expectations-of-a-recovery-in-the-new-zealand-economy-over-the-coming-year-march-` -> **snapshot** (snapshot 20260316073455); points raw/verified 0/0
- `https://fxverify.com/bg/tools/economic-calendar/eksport-6489d5ba9a2596ec5c56e5a2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://calendar.cngold.org/content/712412.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rubixds.com/assets/uploads/attachment/acaa1-rubix-country-insights-new-zealand-january-2026.pdf` -> **snapshot** (snapshot 20260109135039); points raw/verified 15/7
  - p43 New Zealand goods exports, calendar year 2024 (USD) = **42,400,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "Goods exports stood at USD 42.4 billion in CY2024 recording a CAGR of 3.2% since CY2020."
  - p44 New Zealand goods exports growth, January–September 2025 vs same period prior ye = **10.4** % (2025-01-01..2025-09-30) [keep: ] quote: "Goods exports grew by 10.4% during the 9 months of January-September 2025 compared to the corresponding period of the previous year"
  - p45 New Zealand goods exports CAGR since CY2020 (to CY2024) = **3.2** % (2020-01-01..2024-12-31) [keep: ] quote: "Goods exports stood at USD 42.4 billion in CY2024, recording a CAGR of 3.2% since CY2020."
  - p46 Share of New Zealand exports absorbed by China, January–September 2025 = **25** % (2025-01-01..2025-09-30) [keep: ] quote: "China emerges as an even more dominant partner, absorbing 25% of New Zealand's exports, while the US and Australia both account for 12%."
  - p47 Share of New Zealand exports absorbed by the US, January–September 2025 = **12** % (2025-01-01..2025-09-30) [keep: ] quote: "China emerges as an even more dominant partner, absorbing 25% of New Zealand's exports, while the US and Australia both account for 12%."
  - p48 Dairy products share of New Zealand goods exports, January–September 2025 = **29** % (2025-01-01..2025-09-30) [keep: ] quote: "Exports are concentrated in primary and food products, led by dairy products (29%), meat products (13%), and edible fruits (10%)"
  - p49 Meat products share of New Zealand goods exports, January–September 2025 = **13** % (2025-01-01..2025-09-30) [keep: ] quote: "Exports are concentrated in primary and food products, led by dairy products (29%), meat products (13%), and edible fruits (10%)"
- dropped by code checks: 8 (scale word 'billion' not supported by quote or table header: 7; scale word 'million' not supported by quote or table header: 1)

### d5 [shocks] Macro/commodity

Hypothesis: Exchange rate (NZD/USD), global dairy prices (GDT), and any disruptions in March 2026 shift export values versus seasonal baseline. Role: adjust baseline for price/FX shocks.

Queries issued by the searcher: NZD USD March 2026 exchange rate trade weighted index; Global Dairy Trade auction March 2026 results; New Zealand exports disruption March 2026 port logistics Middle East conflict shipping; Stats NZ overseas merchandise trade February 2026 exports value annual

- `https://www.interest.co.nz/currencies/70228/roger-j-kerr-says-retreat-nzd-has-been-due-unwinding-carry-trades-and-nzdaud` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cache-blue.aws.rnz.net.nz/news/country/588581/global-dairy-prices-continue-to-rise-in-wake-of-middle-east-conflict` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://uadairy.org/en/results-of-the-gdt-auction-on-17-march-event-400/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www-green.cache-green.aws.rnz.net.nz/news/business/589064/iran-conflict-sparks-freight-chaos-new-zealand-faces-soaring-costs-and-months-long-d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [physical_flow] Ports / shipping

Hypothesis: Port container and bulk throughput (dairy, logs) in March 2026 scaled by value-per-unit approximates export value. Role: physical throughput cross-check.

Queries issued by the searcher: Port of Tauranga container volume March 2026; New Zealand log export volumes March 2026; Stats NZ overseas merchandise trade February 2026 exports released March 2026; New Zealand dairy export volumes March 2026 Fonterra shipments

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://www.mpi.govt.nz/dmsdocument/71763-Forestry-industry-insights-Issue-6-March-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.port-tauranga.co.nz/news/category/results-announcements/` -> **snapshot** (snapshot 20251113004434); points raw/verified 12/2
  - p50 Port of Tauranga Group Net Profit After Tax, six months ended 31 December 2024 = **60,200,000** NZD (2024-07-01..2024-12-31) [keep: ] quote: "for the six months ended 31 December 2024, with Group Net Profit After Tax of $60.2 million"
  - p51 Port of Tauranga Group Net Profit After Tax change, six months ended 31 December = **27.4** % (2024-07-01..2024-12-31) [keep: ] quote: "Group Net Profit After Tax of $60.2 million - a 27.4% increase on the same period last year"
- `https://www.port-tauranga.co.nz/news/category/presentations/` -> **snapshot** (snapshot 20260308110727); points raw/verified 14/14
  - p52 Port of Tauranga total trade volumes, six months ended 31 December 2025 = **12,600,000** tonnes (2025-07-01..2025-12-31) [keep: ] quote: "total trade volumes increasing 1.2% to 12.6 million tonnes"
  - p53 Port of Tauranga total trade volume growth, six months ended 31 December 2025 vs = **1.2** % (2025-07-01..2025-12-31) [keep: ] quote: "total trade volumes increasing 1.2% to 12.6 million tonnes"
  - p54 Port of Tauranga total trade volumes, three months to 30 September 2025 (Q1 FY20 = **6,600,000** tonnes (2025-07-01..2025-09-30) [keep: ] quote: "total trade increased 5.9% in volume compared to the same period last year, to 6.6 million tonnes"
  - p55 Port of Tauranga total trade volume growth, three months to 30 September 2025 = **5.9** % (2025-07-01..2025-09-30) [keep: ] quote: "total trade increased 5.9% in volume compared to the same period last year, to 6.6 million tonnes"
  - p56 Port of Tauranga container volumes, three months to 30 September 2025 (Q1 FY2026 = **319,649** TEUs (2025-07-01..2025-09-30) [keep: ] quote: "Container volumes increased 9% to 319,649"
  - p57 Port of Tauranga container volume growth, three months to 30 September 2025 = **9** % (2025-07-01..2025-09-30) [keep: ] quote: "Container volumes increased 9% to 319,649"
  - p58 Port of Tauranga total trade volumes, full year ended 30 June (annual result) = **25,300,000** tonnes (2024-07-01..2025-06-30) [keep: ] quote: "total trade increase 7% on the previous year, to 25.3 million tonnes"
  - p59 Port of Tauranga total trade volume growth, full year vs previous year = **7** % (2024-07-01..2025-06-30) [keep: ] quote: "total trade increase 7% on the previous year, to 25.3 million tonnes"
  - p60 Port of Tauranga container volumes, full year (annual result) = **1,200,000** TEUs (2024-07-01..2025-06-30) [keep: ] quote: "Container volumes increased 5.3% to 1.2 million TEUs"
  - p61 Port of Tauranga container volume growth, full year = **5.3** % (2024-07-01..2025-06-30) [keep: ] quote: "Container volumes increased 5.3% to 1.2 million TEUs"
  - p62 Port of Tauranga total trade volumes, three months to 30 September 2024 (Q1 FY20 = **6,200,000** tonnes (2024-07-01..2024-09-30) [keep: ] quote: "total trade increased 7.6% in volume compared to the same period last year, to 6.2 million tonnes"
  - p63 Port of Tauranga total trade volume growth, three months to 30 September 2024 = **7.6** % (2024-07-01..2024-09-30) [keep: ] quote: "total trade increased 7.6% in volume compared to the same period last year, to 6.2 million tonnes"
  - p64 Port of Tauranga container volumes, three months to 30 September 2024 (Q1 FY2025 = **292,860** TEUs (2024-07-01..2024-09-30) [keep: ] quote: "Container volumes increased 17.0% to 292,860 TEUs"
  - p65 Port of Tauranga container volume growth, three months to 30 September 2024 = **17** % (2024-07-01..2024-09-30) [keep: ] quote: "Container volumes increased 17.0% to 292,860 TEUs"
- dropped by code checks: 10 (period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end missing or unparseable: 6)

### b1 [related_series] Stats NZ monthly Overseas Merchandise Trade releases for Jan-Feb 2026 and any Q1 2026 nowcast

Hypothesis: Recent monthly export values (Jan/Feb 2026) and any published Q1 2026 export nowcast would anchor the level and trend entering March 2026, materially tightening the series_auto and yoy_scaling routes that currently rely only on March 2024/2025 anchors.

Queries issued by the searcher: Stats NZ Overseas Merchandise Trade January 2026 goods exports; Stats NZ Overseas Merchandise Trade February 2026 exports f.o.b.; stats.govt.nz "overseas-merchandise-trade-january-2026" goods exports; New Zealand Q1 2026 exports forecast ANZ Westpac Treasury trade balance March 2026

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://www.nationaltribune.com.au/overseas-merchandise-trade-20-march/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ebs.publicnow.com/view/D5E7C9E294900475E47E4A1D1AB2B82B16FC5D97` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.finanzen.at/nachrichten/zinsen/new-zealand-has-nz$519-million-trade-deficit-1035847648` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Global dairy prices (GDT) and NZD/USD in early 2026

Hypothesis: Dairy is ~29% of exports; a GDT price index and NZD/USD level for March 2026 would let a price/FX adjustment be applied to the March 2025 baseline, addressing the largest uncertainty (price vs volume).

Queries issued by the searcher: Global Dairy Trade auction March 2026 price index; NZD USD March 2026 exchange rate average; "Global Dairy Trade" price index level index points March 2026 5.7% rise index; New Zealand dollar falls March 2026 Middle East conflict NZD/USD 0.58

- `https://www.agriland.ie/farming-news/gdt-records-another-strong-rise-after-latest-trading-event/` -> **snapshot** (snapshot 20260309224849); points raw/verified 15/15
  - p66 GDT Price Index level after March 3 2026 trading event = **1,271** index points (2026-03-03..2026-03-03) [keep: ] quote: "The result of the auction saw the index jump by a further 5.7% to 1,271."
  - p67 GDT Price Index percentage change at March 3 2026 trading event = **5.7** % (2026-03-03..2026-03-03) [keep: ] quote: "The result of the auction saw the index jump by a further 5.7% to 1,271."
  - p68 GDT Price Index percentage change at February 17 2026 trading event = **3.6** % (2026-02-17..2026-02-17) [keep: ] quote: "The previous trading event held on February 17 resulted in the index increasing by 3.6%."
  - p69 GDT Price Index percentage change at February 3 2026 trading event = **6.7** % (2026-02-03..2026-02-03) [keep: ] quote: "This followed a 6.7% increase on February 3, 1.5% increase on January 20, and a 6.3% increase on January 6, the first index update for the year."
  - p70 GDT Price Index percentage change at January 20 2026 trading event = **1.5** % (2026-01-20..2026-01-20) [keep: ] quote: "This followed a 6.7% increase on February 3, 1.5% increase on January 20, and a 6.3% increase on January 6, the first index update for the year."
  - p71 GDT Price Index percentage change at January 6 2026 trading event = **6.3** % (2026-01-06..2026-01-06) [keep: ] quote: "This followed a 6.7% increase on February 3, 1.5% increase on January 20, and a 6.3% increase on January 6, the first index update for the year."
  - p72 GDT auction average selling price at March 3 2026 event = **3,676** EUR per metric tonne (2026-03-03..2026-03-03) [keep: ] quote: "The average selling price was €3,676/mt in the auction, which lasted for two hours and 57 minutes."
  - p73 GDT auction volume sold at March 3 2026 event = **18,861** metric tonnes (2026-03-03..2026-03-03) [keep: ] quote: "A total of 165 bidders took part in today's auction, which saw 18,861 metric tonne (mt) of product sold."
  - p74 GDT auction bidders at March 3 2026 event = **165** bidders (2026-03-03..2026-03-03) [keep: ] quote: "A total of 165 bidders took part in today's auction, which saw 18,861 metric tonne (mt) of product sold."
  - p75 GDT auction winning bidders at March 3 2026 event = **97** winning bidders (2026-03-03..2026-03-03) [keep: ] quote: "There were 97 winning bidders and 18 bidding rounds."
  - p76 GDT auction bidding rounds at March 3 2026 event = **18** bidding rounds (2026-03-03..2026-03-03) [keep: ] quote: "There were 97 winning bidders and 18 bidding rounds."
  - p77 GDT weighted average butter price at March 3 2026 event = **5,751** EUR per metric tonne (2026-03-03..2026-03-03) [keep: ] quote: "The results show a 6.1% rise in the weighted average price of butter to €5,751/mt."
  - p78 GDT weighted average butter price percentage change at March 3 2026 event = **6.1** % (2026-03-03..2026-03-03) [keep: ] quote: "The results show a 6.1% rise in the weighted average price of butter to €5,751/mt."
  - p79 GDT skim milk powder price at March 3 2026 event = **2,772** EUR per metric tonne (2026-03-03..2026-03-03) [keep: ] quote: "There was a 9.1% rise in the price of skim milk powder to €2,772/mt, while mozzarella was up 7.9% to €3,581/mt."
  - p80 GDT skim milk powder price percentage change at March 3 2026 event = **9.1** % (2026-03-03..2026-03-03) [keep: ] quote: "There was a 9.1% rise in the price of skim milk powder to €2,772/mt, while mozzarella was up 7.9% to €3,581/mt."
- `https://uadairy.org/en/results-of-the-gdt-auction-on-17-march-event-400/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fxconverter.tech/nzd-to-usd/history/2026/03` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.exchangerates.org.uk/USD-NZD-spot-exchange-rates-history-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] Seasonal March uplift relative to adjacent months

Hypothesis: A March seasonal factor (March vs Feb/Jan ratio) from recent years would let a Feb 2026 level be scaled to March, completing a partial-period route if Feb 2026 data is found.

Queries issued by the searcher: Stats NZ overseas merchandise trade monthly goods exports March 2025 table; NZ goods exports March 2025 $ billion Stats NZ overseas merchandise trade release; figure.nz table "Overseas Merchandise Trade" monthly exports 2022 2023 2024 2025 total exports fob; "Overseas merchandise trade: February 2025" goods exports February 2025 Stats NZ; figure.nz "Total exports" monthly New Zealand goods fob 2023 2024 2025 table Stats NZ; stats.govt.nz "overseas-merchandise-trade-march-2025" monthly exports January February March table actual values

- `http://media.nzherald.co.nz/webcontent/document/pdf/201243/Trade.pdf` -> **snapshot** (snapshot 20121125074830); points raw/verified 15/0
- `https://www.forexfactory.com/news/1338527-nz-overseas-merchandise-trade-march-2025` -> **snapshot** (snapshot 20250422022338); points raw/verified 10/10
  - p81 NZ goods exports, March 2025, level = **7,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p1 (same Stats NZ release, same rounded $7.6b); adds no information beyond p1/p15.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p82 NZ goods exports, March 2025, change vs March 2024 = **1,200,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p2.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p83 NZ goods exports, March 2025, percent change vs March 2024 = **19** % (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p3.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p84 NZ goods imports, March 2025, level = **6,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p4 (imports, not target).] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p85 NZ goods imports, March 2025, change vs March 2024 = **723,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p5.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p86 NZ goods imports, March 2025, percent change vs March 2024 = **12** % (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p6.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p87 NZ monthly goods trade balance, March 2025, surplus = **970,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p7.] quote: "the monthly trade balance was a surplus of $970 million"
  - p88 NZ exports of milk powder, butter, and cheese, March 2025, level = **2,300,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of the dairy level already implied by p25/p89; same release.] quote: "Milk powder, butter, and cheese rose $596 million (35 percent), to $2.3 billion"
  - p89 NZ exports of milk powder, butter, and cheese, March 2025, change vs March 2024 = **596,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Redundant copy of p25.] quote: "Milk powder, butter, and cheese rose $596 million (35 percent), to $2.3 billion"
  - p90 NZ exports of milk powder, butter, and cheese, March 2025, percent change vs Mar = **35** % (2025-03-01..2025-03-31) [DISCARD: Redundant copy of the 35% dairy growth in p25.] quote: "Milk powder, butter, and cheese rose $596 million (35 percent), to $2.3 billion"
- `https://www.mfat.govt.nz/assets/Trade-General/Trade-Market-reports/Trade-and-Economic-Update-Q1-2025-July-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.publicnow.com/view/ED3855E3ACDDB6BF7A3FBCBE93ADF207D42D7D16` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'million' not supported by quote or table header: 15)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['nz exports', 'new zealand trade', 'nz goods exports']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p15', 'p17', 'p18'] Two independent outlets (Scoop, interest.co.nz) both report March 2025 goods exports of ~$7.6bn, up 19% ($1.2bn) on March 2024. Same underlying Stats NZ release, so not independent measurements, but c
- corroborating: ['p8', 'p9', 'p10', 'p18'] March 2024 level $6.5bn and +$240m/+3.8% is consistent with March 2025 being +$1.2bn/+19% to $7.6bn (6.5+1.2=7.7, close to 7.6 given rounding). Establishes the two most recent March anchors.
- corroborating: ['p7', 'p16'] Both report March 2025 monthly surplus of $970m; consistent with exports $7.6bn minus imports $6.6bn.
- corroborating: ['p4', 'p5', 'p6', 'p11', 'p12', 'p13'] Import side figures are internally consistent and corroborate the export/balance arithmetic; useful only as context, not for the export target.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29'] Commodity and partner contributions to the March 2025 rise sum to a large share of the $1.2bn increase, confirming the composition (dairy, meat, fruit, machinery; China/EU/US). Contextual for decompos
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24'] Annual year-ended-March 2025 figures are internally consistent (74.1 exports, 80.2 imports, 6.1 deficit). Provide scale/trend context only.
- corroborating: ['p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49'] Rubix CY2024 USD level and Jan-Sep 2025 growth/shares are a different source but broadly consistent with Stats NZ scale; shares (dairy 29%, meat 13%, China 25%) are useful structural context, not Marc
- conflicting: ['p30'] Jan 2025 export growth of 28.3% is a single-month YoY figure from a secondary aggregator; not comparable to March and not usable as a March 2026 anchor.
- conflicting: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42'] Australia-imports-from-NZ mirror series is from 2012-2015, a decade stale, in AUD, and covers only one partner. Not usable to project March 2026 total NZ exports.
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65'] Port of Tauranga volume data (FY2025/FY2026) shows modest volume growth (~1-7%); supports a low-single-digit real volume trend but gives no direct NZD value and covers only one port.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p15', 'p81'] Three independent write-ups of the same Stats NZ March 2025 release; p1/p81 round to $7.6b, p15 gives $7.59b. Same underlying measurement, so they count as one observation, not three. Use p15 as the m
- corroborating: ['p2', 'p3', 'p17', 'p18', 'p82', 'p83'] All restate the same March 2025 vs March 2024 change ($1.2b / 19%). Redundant with each other and with p1; useful only as a consistency check that p8 ≈ p1 - p2.
- corroborating: ['p8', 'p9', 'p10'] March 2024 level $6.5b with +$240m / +3.8% vs March 2023; internally consistent and consistent with p1 - p2.
- corroborating: ['p1', 'p8'] March 2024 $6.5b and March 2025 $7.6b give the 19% YoY growth; the two March anchors are compatible.
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p11', 'p12', 'p13', 'p14', 'p16', 'p84', 'p85', 'p86', 'p87'] Import and trade-balance figures are internally consistent (exports minus imports equals the stated surplus in both years) but describe imports, not the export target. Context only.
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24'] Annual year-ended-March figures; consistent with the monthly March values but a different period (12-month total). Not a substitute for a March monthly level.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p88', 'p89', 'p90'] Commodity and partner contributions to the March 2025 rise; p25/p88/p89/p90 are the same dairy figure. They explain the March 2025 spike (dairy +35%, meat +34%, fruit +74%) and warn that March 2025 wa
- corroborating: ['p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49'] USD-denominated annual/9-month aggregates and shares from a secondary compiler. Shares (dairy 29%, meat 13%, China 25%) are usable as structure; the USD level is not directly comparable to NZD monthly
- corroborating: ['p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80'] GDT auctions Jan–Mar 2026 show a strong run-up (index 1,271 after +5.7% on 3 Mar 2026; butter +6.1%, SMP +9.1%). This is a price signal for dairy, ~29% of exports, and supports an upward adjustment to
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65'] Port of Tauranga volumes (trade +1.2% in H1 FY2026, containers +9% in Q1) indicate modest volume growth, not a collapse. Only one port and no value-per-tonne conversion, so usable only as a directiona

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | March 2026 vs March 2025 total goods export change factor | 1.03 | 0.88..1.2 | 0.88..1.2 | ratio | m1 (m1) | March 2025 was an exceptionally strong base (largest ever month, +19% YoY, dairy +35%, meat +34%, fruit +74%). GDT prices rose strongly into March 2026 (index 1,271, +5.7% on 3 Mar 2026; butter +6.1%, SMP +9.1%), supporting dairy values, while Port of Tauranga volumes grew only ~1–6%, so volume is r | March 2026 dairy prices remain near the early-March 2026 GDT level and no major disruption hits meat/forestry volumes. | A sharp GDT reversal in late March 2026, a large NZD appreciation, or a reported collapse in meat/log volumes. |
| a2 | March 2026 vs March 2024 two-year export change factor | 1.22 | 1..1.45 | 1..1.45 | ratio | m2 (m2) | Two-year growth from the more normal March 2024 base ($6.5b). March 2025 alone added 19%; a further small price-led gain in 2026 gives roughly 1.19 × 1.03 ≈ 1.22, with a wide range reflecting uncertainty in both years. | The March 2025 spike is treated as a genuine level shift rather than a one-off that fully reverses. | Evidence that March 2025's surge was a one-off timing/price anomaly that reverses in 2026. |
| a3 | Dairy price uplift factor for March 2026 vs March 2025 | 1.08 | 0.9..1.3 | 0.7649..1.53 (widened) | ratio | m3 (m4) | GDT index rose through Jan–Mar 2026 (cumulative gains of 6.3%, 1.5%, 6.7%, 3.6%, 5.7% across five auctions), implying dairy prices well above year-earlier levels; applied to the dairy component only, with a wide range because auction prices pass through to export values with lags and FX effects. | GDT gains pass through to NZ dairy export unit values within the month. | A late-March GDT crash or a large NZD appreciation against USD/EUR. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,781,110,241 | ['p15'] / ['a1'] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 7,831,513,663 | ['p8'] / ['a2'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | formula_mc | 7,797,331,504 | ['p15', 'p48'] / ['a3'] | [] |  | 1.00 | B3 of 3 blocks; median of blocks: this block is the median |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p15 * a1; Monte Carlo P10 to P90 6,144,528,038 to 9,895,152,244; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p8 * a2; Monte Carlo P10 to P90 6,033,732,132 to 10,136,829,548; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p15 * (1 + p48 * (a3 - 1)); Monte Carlo P10 to P90 6,336,628,435 to 9,680,147,334; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,781,110,241 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,831,513,663 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 7,797,331,504 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.38.

Result: central **7,797,331,504** NZD, 80% interval [5,659,828,938, 10,742,087,657] NZD, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total New Zealand goods exports (overseas merchandise trade, exports f.o.b., not seasonally adjusted) for March 2026 is 7,797,331,504 NZD (80% model-based interval 5,659,828,938 to 10,742,087,657 NZD). This is a projection: only about three weeks of March had elapsed at the cutoff, so the month is not yet observed.

Evidence: the March 2025 level was 7,590,000,000 NZD, March 2024 was 6,500,000,000 NZD, and dairy's share of exports was 29%. Method m3 (weight 100%) applies a dairy-only price uplift of 1.08 (range 0.7649 to 1.53) to that dairy share, leaving non-dairy flat; m1 uses a total change factor of 1.03 and m2 a two-year factor of 1.22. The combination is the median of three blocks, with overlapping inputs grouped rather than treated as independent.

Main risk: March 2025 may have been a one-off spike, and non-dairy prices are assumed flat. Better evidence would be actual March 2026 export values or reliable monthly volume and price data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 March 2026 vs March 2025 total goods export change factor: 1.03 ratio, range 0.88 to 1.2; used by m1. Overturned by: A sharp GDT reversal in late March 2026, a large NZD appreciation, or a reported collapse in meat/log volumes.
- a2 March 2026 vs March 2024 two-year export change factor: 1.22 ratio, range 1 to 1.45; used by m2. Overturned by: Evidence that March 2025's surge was a one-off timing/price anomaly that reverses in 2026.
- a3 Dairy price uplift factor for March 2026 vs March 2025: 1.08 ratio, range 0.7649 to 1.53 (range widened by code); used by m3. Overturned by: A late-March GDT crash or a large NZD appreciation against USD/EUR.

Method details (computed by code):
- m1 formula_mc: p15 * a1; Monte Carlo P10 to P90 6,144,528,038 to 9,895,152,244; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p8 * a2; Monte Carlo P10 to P90 6,033,732,132 to 10,136,829,548; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p15 * (1 + p48 * (a3 - 1)); Monte Carlo P10 to P90 6,336,628,435 to 9,680,147,334; result unit NZD converted to NZD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,781,110,241 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,831,513,663 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 7,797,331,504 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.01 (not above one, so no widening); final width x/÷1.38.

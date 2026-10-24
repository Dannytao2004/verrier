# Evidence ledger: fc_nz_exports_2026_03

- Question: Assume today is 2026-03-21. You know nothing published after this date. Estimate the total value of New Zealand's goods exports in March 2026 (actual monthly value, not seasonally adjusted), in New Zealand dollars (NZD), as it will be first reported in Stats NZ's monthly Overseas merchandise trade release.
- as_of: 2026-03-21
- Pinned target: Total value of New Zealand's goods exports (merchandise exports, valued free on board, actual and not seasonally adjusted) for March 2026, as it will be first reported in Stats NZ's monthly Overseas merchandise trade release. | unit NZD (total goods export value for March 2026, actual, not seasonally adjusted) | period 2026-03-01..2026-03-31 | publisher Stats NZ (Tatauranga Aotearoa)

- Official value (scoring only, never shown to the agent): 7,943,894,499

## Directions and pages

### d1 [own_history] Stats NZ published monthly export series; analyst anchoring on recent actuals and seasonality.

Hypothesis: The March 2026 headline export value is closely tied to March 2025 and to y/y growth in Jan-Feb 2026; historical March/February ratios and recent monthly revisions can form an anchor. Symbolically: March_2026 ~ March_2025 * (1 + recent_yoy_growth) * seasonal_adjustment, or latest run-rate * March/Feb seasonal factor.

Queries issued by the searcher: Stats NZ Overseas merchandise trade February 2026 exports; Stats NZ overseas merchandise trade March 2025 goods exports NZD billion; "Overseas merchandise trade: February 2026" stats.govt.nz monthly exports imports table actual values; Stats NZ overseas merchandise trade January 2026 exports fell 3.4 percent

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://www.scoop.co.nz/stories/BU2504/S00380/overseas-merchandise-trade-march-2025.htm` -> **snapshot** (snapshot 20250524003041); points raw/verified 7/7
  - p1 New Zealand total goods exports value, March 2025, actual, not seasonally adjust = **7,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Rounded duplicate of p34 for March 2025 exports; p34 supplies the more precise same measure.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p2 New Zealand total goods exports value, March 2024 (implied base of March 2025 co = **1,200,000,000** NZD (2024-03-01..2024-03-31) [DISCARD: Misparsed level: the quoted NZ$1.2B is the March 2025 year-on-year change, not March 2024 total exports.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p3 Year-on-year growth in New Zealand goods exports, March 2025 vs March 2024 = **19** % (2025-03-01..2025-03-31) [DISCARD: Duplicate of p35/p54 for March 2025 export growth.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p4 New Zealand total goods imports value, March 2025, actual, not seasonally adjust = **6,600,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p5 New Zealand total goods imports value, March 2024 (implied base of March 2025 co = **723,000,000** NZD (2024-03-01..2024-03-31) [DISCARD: Misparsed level: the quoted NZ$723M is the March 2025 import change, not March 2024 total imports.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p6 Year-on-year growth in New Zealand goods imports, March 2025 vs March 2024 = **12** % (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p7 New Zealand monthly goods trade balance (surplus), March 2025 = **970,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "the monthly trade balance was a surplus of $970 million."
- `https://www.nationaltribune.com.au/overseas-merchandise-trade-20-march/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=674067&year=2026&ctyall=10741572&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] commodity-level export values and price indicators.

Hypothesis: Total exports is the sum of major commodity groups; March 2026 value can be built from latest available commodity export values adjusted by March 2026 price and volume signals for dairy, meat, logs/wood, fruit, fuels, machinery, seafood and other groups. Symbolically: Total = sum(commodity_value_recent * price_index_change * volume_index_change) plus uncovered residual.

Queries issued by the searcher: Stats NZ overseas merchandise trade February 2026 exports dairy meat logs; GlobalDairyTrade auction March 2026 prices; ANZ world commodity price index March 2026 New Zealand dollar; Stats NZ "Overseas merchandise trade" March 2025 exports $ million goods exports March 2025

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://ebs.publicnow.com/view/D5E7C9E294900475E47E4A1D1AB2B82B16FC5D97` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://uadairy.org/en/results-of-the-gdt-auction-on-17-march-event-400/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cache-blue.aws.rnz.net.nz/news/country/588581/global-dairy-prices-continue-to-rise-in-wake-of-middle-east-conflict` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [forecasts_markets] macro forecasters and market economists publishing NZ trade forecasts before cutoff.

Hypothesis: If a Q1 2026 or March 2026 goods-export forecast exists, March can be derived as the Q1 forecast minus published January and February actuals, or taken as the March forecast directly, subject to definitional consistency. Symbolically: March_2026 ~ Q1_forecast - Jan_actual - Feb_actual.

Queries issued by the searcher: New Zealand Q1 2026 exports forecast goods trade; Trading Economics New Zealand exports March 2026; New Zealand exports February 2026 monthly overseas merchandise trade NZ$ billion Stats NZ; "March 2026" New Zealand exports forecast economic calendar NZD billion

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://investinglive.com/news/new-zealand-february-trade-deficit-narrows-exports-and-imports-both-beat-expectations-20260319/` -> **snapshot** (snapshot 20260320025217); points raw/verified 10/10
  - p8 New Zealand February goods exports (actual, NZD) = **6,630,000,000** NZD (2026-02-01..2026-02-28) [keep: ] quote: "exports NZ$6.63B vs NZ$6.60B expected (prev. NZ$6.21B)"
  - p9 New Zealand February goods exports expected (consensus forecast, NZD) = **6,600,000,000** NZD (2026-02-01..2026-02-28) [DISCARD: Consensus forecast, not an observed February 2026 export outcome; p8 supersedes it.] quote: "exports NZ$6.63B vs NZ$6.60B expected (prev. NZ$6.21B)"
  - p10 New Zealand prior (January) goods exports (actual, NZD) = **6,210,000,000** NZD (2026-01-01..2026-01-31) [keep: ] quote: "exports NZ$6.63B vs NZ$6.60B expected (prev. NZ$6.21B)"
  - p11 New Zealand February goods imports (actual, NZD) = **6,890,000,000** NZD (2026-02-01..2026-02-28) [keep: ] quote: "imports NZ$6.89B vs NZ$6.20B expected (prev. NZ$6.73B)"
  - p12 New Zealand February goods imports expected (consensus forecast, NZD) = **6,200,000,000** NZD (2026-02-01..2026-02-28) [DISCARD: Consensus forecast, not an observed February 2026 import outcome; p11 supersedes it.] quote: "imports NZ$6.89B vs NZ$6.20B expected (prev. NZ$6.73B)"
  - p13 New Zealand prior (January) goods imports (actual, NZD) = **6,730,000,000** NZD (2026-01-01..2026-01-31) [keep: ] quote: "imports NZ$6.89B vs NZ$6.20B expected (prev. NZ$6.73B)"
  - p14 New Zealand February monthly goods trade balance (actual, NZD) = **-257,000,000** NZD (2026-02-01..2026-02-28) [keep: ] quote: "balance -NZ$257M vs -NZ$740M expected (prev. -NZ$519M)"
  - p15 New Zealand February monthly goods trade balance expected (consensus forecast, N = **-740,000,000** NZD (2026-02-01..2026-02-28) [DISCARD: Consensus forecast, not an observed February 2026 trade balance; p14 supersedes it.] quote: "balance -NZ$257M vs -NZ$740M expected (prev. -NZ$519M)"
  - p16 New Zealand prior (January) monthly goods trade balance (actual, NZD) = **-519,000,000** NZD (2026-01-01..2026-01-31) [keep: ] quote: "balance -NZ$257M vs -NZ$740M expected (prev. -NZ$519M)"
  - p17 New Zealand annual goods trade deficit (actual, NZD) = **3,000,000,000** NZD (not stated (page dated 2026-03-19)) [keep: ] quote: "Statistics New Zealand reported the annual trade deficit stood at NZ$3B."
- `https://www.nzier.org.nz/hubfs/Public%20Publications/Consensus%20Forecasts/Consensus%20Forecasts%20Mar%202026_FINAL.pdf` -> **snapshot** (snapshot 20260316073517); points raw/verified 0/0
- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-january-2026/` -> **snapshot** (snapshot 20260220145154); points raw/verified 0/0

### d4 [physical_flow] ports, shipping, processors and exporters observing cargo throughput in March 2026.

Hypothesis: Observed March 2026 cargo and shipment volumes for key exports, scaled from 1-21 March to the full month and converted using unit values, should track export value and can constrain commodity-level estimates. Symbolically: March_value ~ sum(observed_partial_volume * days_scale * unit_value) for covered commodities plus residual.

Queries issued by the searcher: Port of Tauranga cargo volumes March 2026; New Zealand log exports March 2026 volumes; 木联数据 新西兰12港原木离港发运 周度统计 2026年3月18日; Fonterra export shipments March 2026 dairy volumes

- `https://www.quheqihuo.com/qhyb/2026031629626.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mpi.govt.nz/dmsdocument/71763-Forestry-industry-insights-Issue-6-March-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fruitnet.com/asiafruit/port-of-tauranga-gears-up-for-strong-kiwifruit-season/270723.article` -> **snapshot** (snapshot 20260227101335); points raw/verified 0/0
- `https://www.morningstar.com/company-reports/1482956-port-of-tauranga-strong-import-growth-supports-outlook?listing=0P00007XV0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [base_rates] seasonal and calendar base rates for March within annual and quarterly exports.

Hypothesis: March typically accounts for a stable share of Q1 or annual goods exports; applying that share to a known or forecast Q1/annual total, then adjusting for working days and commodity seasonality, gives an independent route. Symbolically: March_2026 ~ Q1_2026_total * March_Q1_share_adjusted_for_working_days.

Queries issued by the searcher: Stats NZ Overseas merchandise trade March 2025 monthly goods exports value actual; New Zealand goods exports March quarter 2025 total Stats NZ; "Overseas merchandise trade" March 2025 Stats NZ "March 2024" exports $ billion monthly table; New Zealand goods exports January 2026 February 2026 monthly value billion Stats NZ

- `https://www.publicnow.com/view/10C229F2A0627E8C1F9652979D43D04A41D80E51?1745282740` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.treasury.govt.nz/sites/default/files/2025-05/feu-2%20may25.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mfat.govt.nz/en/trade/mfat-market-reports/trade-and-economic-update-q1-2025-new-zealand-exports-show-growth-and-resilience-despite-global-` -> **snapshot** (snapshot 20260210101732); points raw/verified 15/15
  - p18 New Zealand total goods exports, year ended March 2025 = **74,000,000,000** NZD (2024-04-01..2025-03-31) [DISCARD: Rounded duplicate of p45 for year-ended-March-2025 goods exports; p20 preserves the growth context.] quote: "Goods exports grew 7.1% to $74 billion, with favourable domestic production conditions and rising global commodity prices driving kiwifruit, dairy, and meat revenue growth."
  - p19 New Zealand total exports (goods and services), year ended March 2025 = **105,000,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "exports rising by 7.4% to reach $105 billion in the year to March 2025"
  - p20 New Zealand goods exports growth rate, year ended March 2025 = **7.1** % (2024-04-01..2025-03-31) [keep: ] quote: "Goods exports grew 7.1% to $74 billion"
  - p21 New Zealand exports growth, three months to March 2025 vs same period previous y = **14.6** % (2025-01-01..2025-03-31) [keep: ] quote: "Exports for the three months to March were 14.6% higher than the same period in the previous year."
  - p22 New Zealand dairy exports, year ended March 2025 = **26,200,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Dairy exports rose 7.1% to $26.2 billion in the year to March 2025."
  - p23 New Zealand meat exports, year ended March 2025 = **11,700,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Meat exports rose 5.4% to $11.7 billion in the year to March 2025."
  - p24 New Zealand sheep meat exports, year ended March 2025 = **3,900,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "sheep meat rose 7.3% to $3.9 billion"
  - p25 New Zealand beef exports, year ended March 2025 = **4,700,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "beef rose 6.9% to $4.7 billion"
  - p26 New Zealand horticulture exports, year ended March 2025 = **6,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Horticulture exports rose 33.2% to $6.1 billion in the year to March 2025."
  - p27 New Zealand kiwifruit export revenue, year ended March 2025 = **3,700,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "kiwifruit was the standout performer, increasing 45.9% and now contributes to more than half ($3.7 billion) of the revenue generated by horticulture exports"
  - p28 New Zealand forestry exports, year ended March 2025 = **6,000,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "supported an overall export increase of 2.8% to $6 billion in the year to March 2025"
  - p29 New Zealand goods exports to China, year ended March 2025 = **21,000,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Exports to China grew a modest 3.0% to reach $21 billion in the year to March 2025."
  - p30 New Zealand total exports to the US, year ended March 2025 = **16,800,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "total exports growing 6.4% to $16.8 billion over the past year"
  - p31 New Zealand exports to the US growth, March quarter 2025 vs previous year = **17.2** % (2025-01-01..2025-03-31) [keep: ] quote: "Exports in the March quarter were 17.2% higher than the previous year"
  - p32 New Zealand goods imports, year ended March 2025 = **109,000,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "imports grew by 3.4% to reach $109 billion in the year to March 2025"
- `https://www.interest.co.nz/economy/132967/bumper-exports-dairy-meat-and-fruit-give-nz-its-biggest-monthly-goods-trade-surplus` -> **snapshot** (snapshot 20260207084214); points raw/verified 15/15
  - p33 New Zealand monthly merchandise trade surplus, March 2025 = **970,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p7/p58 for the March 2025 goods trade surplus.] quote: "we need to go back to April 2011 to find a larger monthly trade surplus than the $970 million recorded in March 2025."
  - p34 New Zealand total goods exports, March 2025 (actual, not seasonally adjusted) = **7,590,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "Additionally, the $7.59 billion worth of the exports in March 2025 is, just in pure in dollar terms, the biggest figure ever."
  - p35 New Zealand total goods exports, March 2025, year-on-year percentage change = **19** % (2025-03-01..2025-03-31) [keep: ] quote: "Statistics NZ said the $7.59 billion export figure was up 19% ($1.2 billion) on the figure for March 2024."
  - p36 New Zealand total goods exports, March 2025, year-on-year dollar change = **1,200,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "Statistics NZ said the $7.59 billion export figure was up 19% ($1.2 billion) on the figure for March 2024."
  - p37 New Zealand exports of milk powder, butter, and cheese, March 2025, year-on-year = **596,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "Big contributions to the rise came from milk powder, butter, and cheese, up $596 million (35%);"
  - p38 New Zealand exports of milk powder, butter, and cheese, March 2025, year-on-year = **35** % (2025-03-01..2025-03-31) [keep: ] quote: "Big contributions to the rise came from milk powder, butter, and cheese, up $596 million (35%);"
  - p39 New Zealand exports of meat and edible offal, March 2025, year-on-year dollar ch = **286,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "meat and edible offal, up $286 million (34%);"
  - p40 New Zealand exports of meat and edible offal, March 2025, year-on-year percentag = **34** % (2025-03-01..2025-03-31) [keep: ] quote: "meat and edible offal, up $286 million (34%);"
  - p41 New Zealand exports of fruit, March 2025, year-on-year dollar change = **271,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "fruit, up $271 million (74%);"
  - p42 New Zealand exports of fruit, March 2025, year-on-year percentage change = **74** % (2025-03-01..2025-03-31) [keep: ] quote: "fruit, up $271 million (74%);"
  - p43 New Zealand exports of mechanical machinery and equipment, March 2025, year-on-y = **93,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "and mechanical machinery and equipment, up $93 million (50%)"
  - p44 New Zealand exports to China, March 2025, year-on-year dollar change = **371,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "there were big rises compared with March 2024 in exports to China, up $371 million (23 percent)"
  - p45 New Zealand annual goods exports, year ended March 2025 = **74,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "Looking at the 12 month picture, annual goods exports were valued at $74.1 billion, up $5.1 billion from the previous year."
  - p46 New Zealand annual goods exports, year ended March 2025, year-on-year dollar cha = **5,100,000,000** NZD (2024-04-01..2025-03-31) [keep: ] quote: "annual goods exports were valued at $74.1 billion, up $5.1 billion from the previous year."
  - p47 New Zealand annual trade deficit, year ended March 2024 = **10,000,000,000** NZD (2023-04-01..2024-03-31) [keep: ] quote: "The annual trade deficit was $6.1 billion, which was down on the $10.0 billion in the year ended March 2024."

### d6 [shocks] disruption and news signals affecting March 2026 export flows and prices.

Hypothesis: March 2026 shocks such as weather or drought, port congestion, China demand or tariffs, biosecurity issues, shipping schedules and exchange-rate moves can shift the historical or commodity-based estimate; measurable exposure should be used to adjust the chosen route. Symbolically: March_value = baseline_estimate * (1 + net_shock_effect).

Queries issued by the searcher: New Zealand exports disruption March 2026; New Zealand drought dairy March 2026 exports; Stats NZ overseas merchandise trade February 2026 goods exports released March 2026; MFAT weekly global economic report 17 March 2026 New Zealand exports

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/1037/2026-03-16/1313374/ams_1037_00184.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://berl.co.nz/economic-insights/strait-crisis-reveals-our-agricultural-vulnerabilities` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mfat.govt.nz/en/trade/mfat-market-reports/weekly-global-economic-report-17-march-2026` -> **snapshot** (snapshot 20260319005601); points raw/verified 4/4
  - p48 Brent crude oil price per barrel (over, USD) = **103** USD per barrel (not stated (page dated 2026-03-17)) [keep: ] quote: "Brent crude oil prices have risen to over US$103 per barrel"
  - p49 Increase in per litre diesel price in New Zealand since start of conflict = **38** % (not stated (page dated 2026-03-17)) [keep: ] quote: "the per litre price of diesel has increased 38%"
  - p50 Increase in per litre petrol price in New Zealand since start of conflict = **17** % (not stated (page dated 2026-03-17)) [keep: ] quote: "the per litre price of petrol by 17% since the start of the conflict"
  - p51 Number of other markets covered by MFAT tariff finder = **136** markets (not stated (page dated 2026-03-17)) [DISCARD: Count of markets in an MFAT tariff finder; irrelevant to the value of March 2026 goods exports.] quote: "compare tariffs in 136 other markets"

### d7 [administrative] customs filings and export documentation as early traces of March shipments.

Hypothesis: Customs export entries or permit and manifest counts in March 2026 may be available before value statistics and, with an average value per entry or shipment, can proxy the first-reported export value. Symbolically: March_value ~ export_entry_count * average_value_per_entry, adjusted for coverage and timing.

Queries issued by the searcher: Stats NZ overseas merchandise trade March 2025 goods exports value actual; New Zealand Customs export entries number per month statistics; "overseas merchandise trade" "January 2026" Stats NZ goods exports; Stats NZ overseas merchandise trade February 2026 goods exports billion

- `https://www.scoop.co.nz/stories/BU2504/S00380/overseas-merchandise-trade-march-2025.htm` -> **snapshot** (snapshot 20250524003041); points raw/verified 7/7
  - p52 New Zealand total goods exports, March 2025, actual (not seasonally adjusted), N = **7,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p1/p34 for March 2025 total goods exports.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p53 New Zealand total goods exports, March 2025 vs March 2024, change in NZD = **1,200,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p36 for the dollar change in March 2025 exports.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p54 New Zealand total goods exports, March 2025 vs March 2024, percent change = **19** % (2025-03-01..2025-03-31) [DISCARD: Duplicate of p35 for March 2025 export growth.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p55 New Zealand total goods imports, March 2025, actual (not seasonally adjusted), N = **6,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p4 for March 2025 total goods imports.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p56 New Zealand total goods imports, March 2025 vs March 2024, change in NZD = **723,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of the import-change information in p4/p6.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p57 New Zealand total goods imports, March 2025 vs March 2024, percent change = **12** % (2025-03-01..2025-03-31) [DISCARD: Duplicate of p6 for March 2025 import growth.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p58 New Zealand monthly goods trade balance, March 2025, surplus in NZD = **970,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p7/p33 for the March 2025 goods trade surplus.] quote: "the monthly trade balance was a surplus of $970 million."
- `https://www.publicnow.com/view/999388FB4438C2FA3AF69832EC3D68046DF1B47A` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.customs.govt.nz/about-us/news/our-stories/customs-publishes-our-latest-cargo-clearance-study` -> **snapshot** (snapshot 20260206053210); points raw/verified 10/6
  - p59 Export entries counted in Customs Time Release Study 2025 (one week, sea and air = **6,226** export entries (2025-08-28..2025-09-03) [keep: ] quote: "Customs used one weeks' data from 12,039 import entries and 6,226 export entries across both sea and air cargo."
  - p60 Import entries counted in Customs Time Release Study 2025 (one week, sea and air = **12,039** import entries (2025-08-28..2025-09-03) [DISCARD: Import-entry count, not an export value and not the target population.] quote: "Customs used one weeks' data from 12,039 import entries and 6,226 export entries across both sea and air cargo."
  - p61 Share of transactions cleared within five minutes of lodgement, TRS 2025 study w = **98.49** % (2025-08-28..2025-09-03) [DISCARD: Customs clearance timing share, not an export value or conversion factor.] quote: "This year, 98.49% of transactions during the study were cleared within five minutes of lodgement."
  - p62 Share of export entries for sea cargo full container load lodged at least 48 hou = **89.28** % (2025-08-28..2025-09-03) [DISCARD: Export-entry lodgement timing share, not an export value or conversion factor.] quote: "89.28% of export entries for sea cargo full container load were lodged at least 48 hours before loading on the vessel for export, compared to 87.7% in the 2023 study."
  - p63 Share of import entries for air cargo lodged and cleared in advance of arrival,  = **86.24** % (2025-08-28..2025-09-03) [DISCARD: Import air-cargo timing share, not relevant to export value.] quote: "86.24% of import entries for air cargo were lodged and cleared by Customs in advance of arrival into NZ, compared to 78.3% in the 2023 study."
  - p64 Share of import entries for sea cargo full container load lodged and cleared in  = **95.35** % (2025-08-28..2025-09-03) [DISCARD: Import sea-cargo timing share, not relevant to export value.] quote: "95.35% of import entries for sea cargo full container load were lodged and cleared by Customs in advance of arrival into NZ, compared to 93.9% in the 2023 study."
- `https://www.customs.govt.nz/media/423e2m0y/oia-24-787-trade-data-request.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end missing or unparseable: 3; number: unknown scale word 'MB': 1)

### b1 [own_history] Complete the missing year-on-year comparison for the latest monthly export run-rate.

Hypothesis: Monthly total goods exports for January and February 2025 would let us compute the 2026 y/y growth directly and replace the wide assumption a2 in m2; it would also validate whether February 2026 p8 is unusually strong or weak.

Queries issued by the searcher: Stats NZ Overseas merchandise trade February 2025 goods exports actual values; Stats NZ overseas merchandise trade January 2025 exports $ billion; "overseas merchandise trade: February 2025" stats.govt.nz goods exports "$6.7 billion"; Stats NZ overseas merchandise trade March 2025 exports value actual $ billion April 2025

- `https://www.stats.govt.nz/search/?Search=Overseas%20merchandise%20trade%3A%20February%202025&start=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://livenews.co.nz/2025/02/21/agriculture-export-growth-narrows-goods-trade-deficit-stats-nz-media-and-information-release-overseas-merchandise-tr` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.interest.co.nz/economy/132499/new-zealand-records-510-million-february-trade-surplus-dairy-exports-soar-led-milk` -> **snapshot** (snapshot 20260207065004); points raw/verified 15/15
  - p65 NZ total monthly goods exports, February 2025, actual (not seasonally adjusted) = **6,700,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "NZ's monthly exports jumped 16%, or $954 million, to $6.7 billion in February, compared to 12 months earlier."
  - p66 NZ total monthly goods exports, February 2025, year-on-year increase in value = **954,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "NZ's monthly exports jumped 16%, or $954 million, to $6.7 billion in February, compared to 12 months earlier."
  - p67 NZ total monthly goods exports, February 2025, year-on-year percentage change = **16** % (2025-02-01..2025-02-28) [keep: ] quote: "NZ's monthly exports jumped 16%, or $954 million, to $6.7 billion in February, compared to 12 months earlier."
  - p68 NZ monthly trade balance, February 2025, surplus = **510,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Statistics New Zealand says February's monthly trade balance came in at a surplus of $510 million, bouncing up from the previous month's deficit of $486 million."
  - p69 NZ monthly trade balance, January 2025, deficit = **486,000,000** NZD (2025-01-01..2025-01-31) [keep: ] quote: "Statistics New Zealand says February's monthly trade balance came in at a surplus of $510 million, bouncing up from the previous month's deficit of $486 million."
  - p70 NZ monthly goods imports, February 2025, actual = **6,200,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Imports rose 2.1%, or $125 million, to $6.2 billion, led by mechanical machinery and equipment."
  - p71 NZ monthly goods imports, February 2025, year-on-year increase in value = **125,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Imports rose 2.1%, or $125 million, to $6.2 billion, led by mechanical machinery and equipment."
  - p72 NZ monthly goods imports, February 2025, year-on-year percentage change = **2.1** % (2025-02-01..2025-02-28) [keep: ] quote: "Imports rose 2.1%, or $125 million, to $6.2 billion, led by mechanical machinery and equipment."
  - p73 NZ exports of milk powder, butter, and cheese, February 2025, total value = **2,300,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Milk powder, butter, and cheese led the rise in exports, up 27%, or $486 million, to a total of $2.3 billion."
  - p74 NZ exports of milk powder, butter, and cheese, February 2025, year-on-year incre = **486,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Milk powder, butter, and cheese led the rise in exports, up 27%, or $486 million, to a total of $2.3 billion."
  - p75 NZ exports of meat and edible offal, February 2025, total value = **1,000,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Stats NZ said on Friday that meat and edible offal rose by 28%, or $227 million, to $1 billion in February 2025 compared with February 2024."
  - p76 NZ exports of meat and edible offal, February 2025, year-on-year increase in val = **227,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Stats NZ said on Friday that meat and edible offal rose by 28%, or $227 million, to $1 billion in February 2025 compared with February 2024."
  - p77 NZ exports of infant formula, February 2025, total value = **303,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Infant formula exports were also high, coming in at $303 million last month, increasing by 61%, or $114 million, compared to a year ago."
  - p78 NZ total exports to China, February 2025, year-on-year increase in value = **249,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Total exports to China were up 16%, or $249 million in February 2025 compared with February 2024."
  - p79 NZ exports of aircraft and parts, February 2025, year-on-year decrease in value = **47,000,000** NZD (2025-02-01..2025-02-28) [keep: ] quote: "Export commodities that fell included aircraft and parts which plummeted 77%, or $47 million, in February 2025, and mechanical machinery and equipment exports which fell 21%, or $42 million."
- `https://www.stats.govt.nz/information-releases/?dateFiltersID=100&filters=Overseas%20merchandise%20trade&start=12` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] Calibrate the March/February seasonal ratio used in m1.

Hypothesis: Recent actual March and February goods export levels would constrain a1, the March 2026/February 2026 seasonal ratio. A stable recent ratio would materially narrow m1; an unstable one would show that m1 should carry less weight.

Queries issued by the searcher: Stats NZ Overseas merchandise trade March 2025 exports tables; Stats NZ overseas merchandise trade March 2024 goods exports actual not seasonally adjusted; "Overseas merchandise trade: February 2025" goods exports $ billion February 2025 Stats NZ; figure.nz table monthly total goods exports New Zealand 2015-2025 Stats NZ series

- `https://www.stats.govt.nz/large-datasets/csv-files-for-download/overseas-merchandise-trade-datasets/` -> **snapshot** (snapshot 20260321181424); points raw/verified 0/0
- `https://www.scoop.co.nz/stories/BU2504/S00380/overseas-merchandise-trade-march-2025.htm` -> **snapshot** (snapshot 20250524003041); points raw/verified 7/7
  - p80 New Zealand total goods exports, March 2025, actual, not seasonally adjusted = **7,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Rounded duplicate of p34 ($7.6b vs $7.59b); p34 is more precise.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p81 New Zealand total goods exports, March 2025 vs March 2024, change in value = **1,200,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p36: same March 2025 y/y dollar change.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p82 New Zealand total goods exports, March 2025 vs March 2024, percent change = **19** % (2025-03-01..2025-03-31) [DISCARD: Duplicate of p35: same March 2025 y/y percentage change.] quote: "goods exports rose by $1.2 billion (19 percent), to $7.6 billion"
  - p83 New Zealand total goods imports, March 2025, actual, not seasonally adjusted = **6,600,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p4: same March 2025 import level.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p84 New Zealand total goods imports, March 2025 vs March 2024, change in value = **723,000,000** NZD (2025-03-01..2025-03-31) [keep: ] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p85 New Zealand total goods imports, March 2025 vs March 2024, percent change = **12** % (2025-03-01..2025-03-31) [DISCARD: Duplicate of p6: same March 2025 import y/y percentage.] quote: "goods imports rose by $723 million (12 percent), to $6.6 billion"
  - p86 New Zealand monthly goods trade balance, March 2025, surplus = **970,000,000** NZD (2025-03-01..2025-03-31) [DISCARD: Duplicate of p7: same March 2025 trade balance.] quote: "the monthly trade balance was a surplus of $970 million."
- `https://www.forexfactory.com/news/1333446-nz-overseas-merchandise-trade-february-2025` -> **snapshot** (snapshot 20250323065128); points raw/verified 10/10
  - p87 New Zealand total goods exports, February 2025, actual, not seasonally adjusted = **6,700,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p65: same February 2025 export level.] quote: "goods exports rose by $954 million (16 percent), to $6.7 billion"
  - p88 New Zealand total goods exports, February 2024, actual, not seasonally adjusted  = **954,000,000** NZD (2024-02-01..2025-02-28) [DISCARD: Mislabelled: named as an implied February 2024 level but value is the $954m change; p66 already records that change.] quote: "goods exports rose by $954 million (16 percent), to $6.7 billion"
  - p89 New Zealand total goods exports, February 2025, year-on-year percentage change = **16** % (2025-02-01..2025-02-28) [DISCARD: Duplicate of p67: same February 2025 export y/y percentage.] quote: "goods exports rose by $954 million (16 percent), to $6.7 billion"
  - p90 New Zealand goods imports, February 2025, actual, not seasonally adjusted = **6,200,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p70: same February 2025 import level.] quote: "goods imports rose by $125 million (2.1 percent), to $6.2 billion"
  - p91 New Zealand goods imports, February 2025, year-on-year change = **125,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p71: same February 2025 import y/y dollar change.] quote: "goods imports rose by $125 million (2.1 percent), to $6.2 billion"
  - p92 New Zealand goods imports, February 2025, year-on-year percentage change = **2.1** % (2025-02-01..2025-02-28) [DISCARD: Duplicate of p72: same February 2025 import y/y percentage.] quote: "goods imports rose by $125 million (2.1 percent), to $6.2 billion"
  - p93 New Zealand monthly goods trade balance, February 2025, surplus = **510,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p68: same February 2025 trade balance.] quote: "the monthly trade balance was a surplus of $510 million"
  - p94 New Zealand milk powder, butter, and cheese exports, February 2025, year-on-year = **486,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p74: same February 2025 dairy y/y dollar change.] quote: "Milk powder, butter, and cheese rose $486 million (27 percent), to $2.3 billion"
  - p95 New Zealand milk powder, butter, and cheese exports, February 2025, year-on-year = **27** % (2025-02-01..2025-02-28) [keep: ] quote: "Milk powder, butter, and cheese rose $486 million (27 percent), to $2.3 billion"
  - p96 New Zealand milk powder, butter, and cheese exports, February 2025, actual, not  = **2,300,000,000** NZD (2025-02-01..2025-02-28) [DISCARD: Duplicate of p73: same February 2025 dairy export level.] quote: "Milk powder, butter, and cheese rose $486 million (27 percent), to $2.3 billion"
- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-march-2025/` -> **snapshot** (snapshot 20260201001822); points raw/verified 0/0

### b3 [related_series] Obtain February 2026 commodity detail and early March 2026 commodity/price signals to test the aggregate routes.

Hypothesis: The February 2026 Stats NZ release likely contains commodity-group export values and y/y changes for dairy, meat, logs/wood, fruit, machinery and other groups. These would enable a bottom-up d2 check and reveal whether the aggregate p8 level was driven by groups that typically peak in March.

Queries issued by the searcher: Stats NZ Overseas merchandise trade February 2026; GlobalDairyTrade auction results March 2026; "February 2026" New Zealand exports logs wood meat fruit dairy "year ended February 2026" commodity; ebs.publicnow.com "Overseas merchandise trade: February 2026" commodity tables logs

- `https://www.stats.govt.nz/information-releases/overseas-merchandise-trade-february-2026/` -> **snapshot** (snapshot 20260321203007); points raw/verified 0/0
- `https://ebs.publicnow.com/view/D5E7C9E294900475E47E4A1D1AB2B82B16FC5D97` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://uadairy.org/en/results-of-the-gdt-auction-on-17-march-event-400/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.china.org.cn/world/Off_the_Wire/2026-03/04/content_118360012.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p34', 'p52'] All report March 2025 total goods exports. p34 gives the more precise NZ$7.59B figure; p1 and p52 round the same Stats NZ result to NZ$7.6B. p1/p52 are duplicate reports of one release, not independen
- corroborating: ['p4', 'p7', 'p33', 'p34', 'p55', 'p58'] March 2025 exports (p34), imports (p4/p55), and surplus (p7/p33/p58) are mutually consistent within rounding. p33 and p58 duplicate p7, and p55 duplicates p4.
- conflicting: ['p2', 'p35', 'p36'] p2 cannot be March 2024 total exports: the quoted NZ$1.2B is the year-on-year change, not the level. The 19% rise to NZ$7.59B implies a March 2024 base near NZ$6.4B, so p2 is a misparse and should not
- corroborating: ['p3', 'p35', 'p36', 'p54'] p35 and p36 give the same March 2025 year-on-year growth: 19%, or NZ$1.2B. p3 and p54 duplicate p35 from another snapshot/URL.
- conflicting: ['p5', 'p6', 'p55', 'p56', 'p57'] p5 cannot be March 2024 imports: the quoted NZ$723M is the change, not the level. p55-p57 duplicate p4/p6 and add no new import information.
- corroborating: ['p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16'] The February 2026 release is internally consistent: exports NZ$6.63B vs NZ$6.60B consensus, January exports NZ$6.21B, February imports NZ$6.89B, January imports NZ$6.73B, and balances of -NZ$257M and 
- context: ['p17'] Annual goods trade deficit of NZ$3B from the same March 2026 release gives context on the external balance but is not a March 2026 export level.
- context: ['p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p45', 'p46', 'p47'] MFAT/Stats NZ annual and quarterly context. p18 and p45 both put year-ended-March-2025 goods exports at about NZ$74B; p19 and p32 are total goods-and-services exports/imports, not goods-only values; p
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] March 2025 commodity and market year-on-year gains from the same Stats NZ release are consistent with the record March 2025 export total. They show broad-based strength in dairy, meat, fruit, machiner
- context: ['p48', 'p49', 'p50'] MFAT page dated 17 March 2026 reports higher Brent crude and NZ retail diesel/petrol prices. These are related cost/inflation shocks and may affect export prices and margins, but there is no direct co
- context: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64'] Customs Time Release Study gives one week of export and import entries plus process shares. p60 is an import-entry count, and p61-p64 are process/timing shares, not export values. Only p59 can potenti
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p34', 'p35', 'p36'] March 2025 goods exports $7.59b, up 19% or $1.2b; level and change imply a March 2024 base near $6.39b and are internally consistent.
- redundant: ['p80', 'p81', 'p82'] Scoop copies of the same March 2025 export level and y/y change; p80 rounds $7.59b to $7.6b. Keep p34-p36 for precision.
- corroborating: ['p65', 'p66', 'p67'] February 2025 exports $6.7b, up $954m/16%; level and change imply February 2024 near $5.746b.
- conflicting: ['p87', 'p88', 'p89'] p87/p89 repeat the Feb 2025 level/growth. p88 is labelled as an implied February 2024 level but its value is the $954m change, so its role is mislabelled; do not use p88 as a level.
- corroborating: ['p8', 'p10', 'p11', 'p13', 'p14', 'p16'] Feb 2026 exports $6.63b and imports $6.89b imply balance -$257m (p14); Jan 2026 exports $6.21b and imports $6.73b imply -$519m (p16). Internally consistent.
- corroborating: ['p4', 'p6', 'p7', 'p84'] March 2025 imports $6.6b, up $723m/12%; March 2025 exports $7.59b less imports $6.6b gives ~$0.99b surplus, close to reported $0.97b after rounding.
- redundant: ['p83', 'p85', 'p86'] Scoop copies of March 2025 import level, growth and balance; p84 is the separate dollar change and adds information.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] March 2025 commodity y/y contributions sum to $1.246b across dairy, meat, fruit and machinery, near the total $1.2b rise (p36), with small offset in other groups; they can reconstruct March 2025 group
- context: ['p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79'] February 2025 commodity detail: dairy $2.3b and meat $1.0b, plus infant formula/China/aircraft changes; useful for seasonal composition but not direct March 2026 values.
- context: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p45', 'p46'] Annual and Q1 2025 export/import totals and commodity totals establish scale and composition; p20 $74b and p45 $74.1b agree within rounding. They do not give March 2026 level.
- context: ['p17', 'p47'] Annual goods deficits: year ended March 2024 ~$10b and the 19 March 2026 page reports a $3b annual deficit, indicating a smaller trade imbalance recently; not a direct March 2026 export level.
- context: ['p48', 'p49', 'p50'] March 2026 oil-price and fuel-cost shock: Brent >$103/bbl and diesel/petrol up since conflict. This is a risk to freight costs and nominal fuel/commodity values, not a measured export value.
- context: ['p59'] Customs Time Release Study one-week count of 6,226 export entries in Aug-Sep 2025. It is an administrative count, needing scaling to March and an average value per entry to proxy export value.
- context: ['p68', 'p69', 'p93'] February 2025 trade surplus $510m and January 2025 deficit $486m; p93 duplicates p68. Monthly balances are volatile and not directly the export level.
- redundant: ['p70', 'p71', 'p72', 'p90', 'p91', 'p92'] Feb 2025 imports $6.2b, up $125m/2.1%; p90-p92 repeat p70-p72. Useful only as import-side context.
- redundant: ['p73', 'p95', 'p96'] p73 gives Feb 2025 dairy $2.3b with 27%/486m quoted; p96 repeats the level and p95 isolates the 27% growth. Keep p73/p74 and p95 only as context.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | March 2026/February 2026 seasonal ratio relative to average March/February ratio in 2024 and 2025 | 1 | 0.96..1.04 | 0.7065..1.413 (widened) | dimensionless | m1 (m1) | Observed March/February ratios from 2024 and 2025 provide the seasonal anchor; this factor allows a modest 2026 deviation from that average. February 2026 p8 is used as the current level anchor. | March 2026 seasonal timing is similar to 2024-25 and there is no large port, biosecurity or working-day disruption. | Evidence of an unusual March dairy/meat/fruit shipping peak, a major port closure, or a large working-day effect distinct from 2024-25. |
| a2 | Average value per customs export entry, March 2026 | 280,000 | 210,000..370,000 | 197,104..394,208 (widened) | NZD per entry | m2 (m2) | p59 gives a weekly export-entry count. Scaling to a monthly rate and calibrating against the March 2025 total p34 implies an average value per entry in this range; uncertainty covers commodity prices, high oil/freight costs and entry-size mix. | The customs entry count per month is comparable to the TRS study-week rate and average export value per entry is not dominated by a few unusually large aircraft/fuel shipments. | Evidence that the TRS week was not representative or that average export value per entry shifted materially because of large single shipments or a changed entry-size distribution. |
| a3 | March 2026 export-entry count relative to the 2025 TRS study-week monthly rate | 1 | 0.9..1.12 | 0.7099..1.42 (widened) | dimensionless | m2 (m2) | p59 is a single week in August-September 2025, not a March average. March is often a peak month, but entry counts depend on shipment consolidation, so the central value is neutral and the range is wide. | March 2026 export-entry counts per week are within roughly plus or minus 10-12% of the scaled TRS study-week rate. | Observed March 2026 manifest or entry counts far outside the range, or known port congestion/schedule changes shifting clearance timing. |
| a4 | March 2026/March 2025 change factor for milk powder, butter and cheese exports | 0.98 | 0.85..1.13 | 0.85..1.13 | dimensionless | unused | March 2025 dairy exports were very strong, up 35% per p38, creating a high base. February 2026 total exports were about flat year-on-year versus p65, and no 2026 dairy price/volume data are available here. | Global dairy prices and New Zealand dairy export volumes do not move far from their early-2025 relationship. | GDT auction or dairy export volume data showing a large 2026 price or volume swing. |
| a5 | March 2026/March 2025 change factor for meat and edible offal exports | 1 | 0.86..1.15 | 0.86..1.15 | dimensionless | unused | March 2025 meat exports were up 34% per p40, a high base. Recent total export growth is roughly flat, and no March 2026 meat price/volume data are available. | Meat prices, slaughter volumes and export demand are broadly similar to March 2025. | Large changes in lamb/beef prices, Chinese demand, or slaughter/processing volumes. |
| a8 | March 2026/March 2025 change factor for all other goods exports | 1 | 0.88..1.12 | 0.88..1.12 | dimensionless | unused | The residual includes fruit, machinery, logs/wood, seafood, fuels and other manufactures. February 2026 total exports were roughly flat year-on-year, but high oil prices and China demand could shift nominal values. | The heterogeneous other-goods groups move roughly in line with the recent total export trend. | Large moves in log prices, China demand, seafood volumes, or fuel exports. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,445,334,285 | ['p8', 'p34', 'p65', 'p36', 'p66'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 7,575,011,663 | ['p59'] / ['a2', 'a3'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |
| m3 | formula_mc | n/a | ['p34', 'p37', 'p38', 'p39', 'p40'] / ['a4', 'a5', 'a8'] | [] |  | 0.00 |  | formula has more than 60 nodes |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: sum over commodity of dairy, meat, other

Method details (computed by code):

- m1 formula_mc: p8 * mean(p34 / p65, (p34 - p36) / (p65 - p66)) * a1; Monte Carlo P10 to P90 4,586,110,893 to 12,095,869,721; result unit NZD converted to NZD; own 80% width x/÷1.62 (Monte Carlo of the formula inputs)
- m2 formula_mc: p59 * k_weeks_per_year / k_months_per_year * a2 * a3; Monte Carlo P10 to P90 4,495,168,211 to 12,809,753,397; result unit (NZD/month) * 1 month converted to NZD; own 80% width x/÷1.69 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,445,334,285 (width x/÷1.62, Monte Carlo of the formula inputs); B2 = m2: 7,575,011,663 (width x/÷1.69, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.66; Birge ratio 0.03 (not above one, so no widening); final width x/÷1.66.

Result: central **7,509,893,078** NZD, 80% interval [4,533,940,855, 12,439,177,274] NZD, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for New Zealand's total goods exports (merchandise exports, FOB, actual and not seasonally adjusted) for March 2026 is 7,509,893,078 NZD (80% model-based interval 4,533,940,855 to 12,439,177,274 NZD).

Two routes were combined with equal weight per block. The first scales February 2026 exports of 6,630,000,000 NZD by observed March/February ratios from 2025 (7,590,000,000 NZD over 6,700,000,000 NZD) and 2024 (recovered from 1,200,000,000 NZD and 954,000,000 NZD), adjusted by assumption a1 (1, range 0.7065 to 1.413). The second scales the customs study-week entry count 6,226 export entries to a monthly rate, times assumed average value per entry a2 (280,000) and entry-count factor a3 (1).

The main risk is that a2 and a3 are analyst assumptions, not observations, and the study week may not represent March 2026. Better evidence would be actual March 2026 customs entry counts and commodity-level export values.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 March 2026/February 2026 seasonal ratio relative to average March/February ratio in 2024 and 2025: 1 dimensionless, range 0.7065 to 1.413 (range widened by code); used by m1. Overturned by: Evidence of an unusual March dairy/meat/fruit shipping peak, a major port closure, or a large working-day effect distinct from 2024-[n].
- a2 Average value per customs export entry, March 2026: 280,000 NZD per entry, range 197,104 to 394,208 (range widened by code); used by m2. Overturned by: Evidence that the TRS week was not representative or that average export value per entry shifted materially because of large single shipments or a changed entry-size distribution.
- a3 March 2026 export-entry count relative to the 2025 TRS study-week monthly rate: 1 dimensionless, range 0.7099 to 1.42 (range widened by code); used by m2. Overturned by: Observed March 2026 manifest or entry counts far outside the range, or known port congestion/schedule changes shifting clearance timing.

Method details (computed by code):
- m1 formula_mc: p8 * mean(p34 / p65, (p34 - p36) / (p65 - p66)) * a1; Monte Carlo P10 to P90 4,586,110,893 to 12,095,869,721; result unit NZD converted to NZD; own 80% width x/÷1.62 (Monte Carlo of the formula inputs)
- m2 formula_mc: p59 * k_weeks_per_year / k_months_per_year * a2 * a3; Monte Carlo P10 to P90 4,495,168,211 to 12,809,753,397; result unit (NZD/month) * 1 month converted to NZD; own 80% width x/÷1.69 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,445,334,285 (width x/÷1.62, Monte Carlo of the formula inputs); B2 = m2: 7,575,011,663 (width x/÷1.69, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.66; Birge ratio 0.03 (not above one, so no widening); final width x/÷1.66.

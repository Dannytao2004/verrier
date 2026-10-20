# Evidence ledger: fc_meta_capex_2026_q3

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate Meta Platforms' capital expenditures, including principal payments on finance leases, for the third quarter of 2026 (quarter ended September 30, 2026), in US dollars, as it will be first reported in Meta's third-quarter 2026 earnings press release.
- as_of: 2026-10-19
- Pinned target: Capital expenditures, including principal payments on finance leases, as first reported by Meta Platforms, Inc. in its third-quarter 2026 earnings press release for the quarter ended 2026-09-30; consolidated worldwide, in US dollars. Working interpretation is Meta's supplemental cash-flow measure ge | unit USD (total for the quarter) | period 2026-07-01..2026-09-30 | publisher Meta Platforms, Inc.

## Directions and pages

### d1 [own_history] Meta investor-relations-reported history and guidance

Hypothesis: The Q3 2026 first-reported value should be a continuation of Meta's recent quarterly trajectory for 'capital expenditures, including principal payments on finance leases'; prior quarterly levels, any seasonal or back-end-loaded ramp pattern, and FY2026 capex guidance constrain the estimate.

Queries issued by the searcher: Meta second quarter 2026 capital expenditures including principal payments on finance leases; Meta Platforms 2026 capital expenditures guidance earnings release; "Meta Reports Third Quarter 2025 Results" capital expenditures including principal payments on finance leases cash flow; "Meta Reports Fourth Quarter and Full Year 2025 Results" capital expenditures finance leases

- `https://www.nasdaq.com/press-release/meta-reports-second-quarter-2026-results-2026-07-29` -> **live_dated** (page date 2026-07-29); points raw/verified 15/10
  - p1 Meta capital expenditures, including principal payments on finance leases, Q2 20 = **31,080,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Capital expenditures - Capital expenditures, including principal payments on finance leases, were $31.08 billion."
  - p2 Meta purchases of property and equipment, Q2 2026 (cash flow statement) = **-30,116,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p3 Meta principal payments on finance leases, Q2 2026 (cash flow statement) = **-962,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p4 Meta purchases of property and equipment, Q2 2025 (cash flow statement) = **-16,538,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p5 Meta principal payments on finance leases, Q2 2025 (cash flow statement) = **-474,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p6 Meta purchases of property and equipment, six months ended June 30, 2026 = **-49,113,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p7 Meta principal payments on finance leases, six months ended June 30, 2026 = **-1,805,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p8 Meta purchases of property and equipment, six months ended June 30, 2025 = **-29,479,000,000** USD (2025-01-01..2025-06-30) [keep: ] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p9 Meta principal payments on finance leases, six months ended June 30, 2025 = **-1,225,000,000** USD (2025-01-01..2025-06-30) [keep: ] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p10 Meta free cash flow, Q2 2026 = **784,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Cash flow - Cash flow from operating activities was $31.86 billion, and free cash flow was $784 million.(1)"
- `https://finance.yahoo.com/markets/stocks/articles/meta-now-owes-22-billion-112355817.html` -> **live_dated** (page date 2026-10-01); points raw/verified 15/9
  - p11 Meta capex on TIKR's narrower measure, June 2026 quarter = **30,120,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Meta's capex reached $30.12 billion in the June 2026 quarter against $31.86 billion of operating cash flow"
  - p12 Meta operating cash flow, June 2026 quarter = **31,860,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Redundant OCF duplicate of p66/p34.] quote: "against $31.86 billion of operating cash flow, leaving $1.75 billion of free cash flow on TIKR's measure"
  - p13 Meta free cash flow on TIKR's measure, June 2026 quarter = **1,750,000,000** USD (2026-04-01..2026-06-30) [DISCARD: TIKR free cash flow on a different measure; not the target capex metric and adds no independent capex information.] quote: "leaving $1.75 billion of free cash flow on TIKR's measure, down from $9.02 billion a year earlier"
  - p14 Meta free cash flow on TIKR's measure, June 2025 quarter = **9,020,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate TIKR prior-year FCF; p134 contains the same underlying figure.] quote: "down from $9.02 billion a year earlier"
  - p15 Meta first-half 2026 capex on Meta's own measure = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 company-measure capex; p21 carries the same value and useful H2 guidance context.] quote: "The first half used about $50.9 billion of capex on Meta's measure."
  - p16 Meta capex on TIKR's measure, June 2025 quarter = **16,540,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 TIKR capex; p30 carries the same comparison.] quote: "Capex went from $16.54 billion to $30.12 billion, up 82%"
  - p17 Meta capex on TIKR's measure, trailing four quarters through June 2026 = **89,330,000,000** USD (2025-07-01..2026-06-30) [DISCARD: TIKR trailing-four-quarter capex on a narrower measure; redundant context for the target quarter.] quote: "Capex totaled $89.33 billion against $52.17 billion in the four quarters before"
  - p18 Meta capex on TIKR's measure, prior trailing four quarters through June 2025 = **52,170,000,000** USD (2024-07-01..2025-06-30) [DISCARD: Prior TIKR trailing-four-quarter capex on a narrower measure; redundant context.] quote: "Capex totaled $89.33 billion against $52.17 billion in the four quarters before"
  - p19 Meta capex as share of operating cash flow, September 2024 quarter = **33** % (2024-07-01..2024-09-30) [keep: ] quote: "absorbed about 95% of operating cash flow, against 33% in the September 2024 quarter"
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.barchart.com/story/news/35772952/meta-reports-third-quarter-2025-results` -> **dropped** (live http 202); points raw/verified -/-
- dropped by code checks: 11 (scale word 'billion' not supported by quote or table header: 3; period_end 2026-12-31 after as_of: 8)

### d2 [forecasts_markets] Sell-side consensus and company guidance

Hypothesis: Analyst consensus for Meta Q3 2026 capex and management's FY2026 capex guidance directly anchor the first-reported figure; if FY guidance and Q1/Q2 2026 actuals are known, the implied second-half or Q3 level can be inferred.

Queries issued by the searcher: Meta Platforms 2026 capital expenditures guidance 2026 capex outlook; Meta Q2 2026 earnings capital expenditures including finance leases second quarter 2026; Meta third quarter 2026 capex estimate analysts expect Q3 2026 capital expenditures consensus; Meta Q3 2026 earnings preview October 2026 capital expenditures expected analysts

- `https://wap.stockstar.com/detail/IG2026101900012961` -> **live_dated** (page date 2026-10-01); points raw/verified 15/8
  - p20 Analyst consensus Q3 2026 Meta capital expenditures (single-quarter capex) = **40,970,000,000** USD (2026-07-01..2026-09-30) [keep: ] quote: "机构一致预期显示,自由现金流将转负至-91.4亿美元,单季资本开支达到409.7亿美元。"
  - p21 Meta first-half 2026 capital expenditures consumed (cumulative) = **50,900,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "上半年已消耗约509亿美元,按此推算下半年资本开支将达790亿至940亿美元。"
  - p22 Meta Q2 2026 capital expenditures (reported) = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of the exact Q2 2026 company-measure capex in p1.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元"
  - p23 Meta Q2 2026 operating cash flow = **31,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 OCF; p66 is exact.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元"
  - p24 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 carries the same figure.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元"
  - p25 Meta Q3 2026 consensus free cash flow (forecast, negative) = **-9,140,000,000** USD (2026-07-01..2026-09-30) [keep: ] quote: "机构一致预期显示,自由现金流将转负至-91.4亿美元,单季资本开支达到409.7亿美元。"
  - p26 Meta Q3 2026 revenue guidance lower bound = **61,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Lower bound already contained in p67 revenue guidance range.] quote: "Meta此前给出的三季度营收指引为610亿至640亿美元"
  - p27 Meta Q3 2026 revenue guidance upper bound = **64,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Upper bound already contained in p67 revenue guidance range.] quote: "Meta此前给出的三季度营收指引为610亿至640亿美元"
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://finance.yahoo.com/markets/stocks/articles/meta-now-owes-22-billion-112355817.html` -> **live_dated** (page date 2026-10-01); points raw/verified 15/9
  - p28 Meta first-half 2026 capex on company measure (including finance lease principal = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 company-measure capex; p21 is kept.] quote: "The first half used about $50.9 billion of capex on Meta's measure."
  - p29 Meta Q2 2026 capex (TIKR measure, narrower than company measure) = **30,120,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate TIKR Q2 2026 capex; p11 is kept.] quote: "Capex went from $16.54 billion to $30.12 billion, up 82%"
  - p30 Meta Q2 2025 capex (TIKR measure, prior-year comparison) = **16,540,000,000** USD (2025-04-01..2025-06-30) [DISCARD: TIKR Q2 2025 capex duplicate of the cash-flow PP&E component; narrower than the company capex measure used for the targe] quote: "Capex went from $16.54 billion to $30.12 billion, up 82%"
  - p31 Meta Q2 2026 capex year-over-year growth rate = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Capex went from $16.54 billion to $30.12 billion, up 82%"
  - p32 Meta trailing four-quarter capex (TIKR measure) = **89,330,000,000** USD (2025-07-01..2026-06-30) [DISCARD: Duplicate trailing-four-quarter capex; p17 is kept.] quote: "Capex totaled $89.33 billion against $52.17 billion in the four quarters before"
  - p33 Meta prior trailing four-quarter capex (TIKR measure) = **52,170,000,000** USD (2024-07-01..2025-06-30) [DISCARD: Duplicate prior trailing-four-quarter capex; p18 is kept.] quote: "Capex totaled $89.33 billion against $52.17 billion in the four quarters before"
  - p34 Meta Q2 2026 operating cash flow = **31,860,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate OCF; p66 is the exact cash-flow-statement figure.] quote: "Operating cash flow rose from $25.56 billion to $31.86 billion in a year"
  - p35 Meta Q2 2026 free cash flow (company measure) = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 company FCF; p10 is kept.] quote: ""Free cash flow was $784 million.""
  - p36 Meta Q2 2026 capex as share of operating cash flow = **95** % (2026-04-01..2026-06-30) [keep: ] quote: "absorbed about 95% of operating cash flow, against 33% in the September 2024 quarter"
- `https://markets.businessinsider.com/news/stocks/meta-platforms-narrows-fy26-capital-expenditure-view-to-130b--145b-1036381681` -> **live_dated** (page date 2026-07-29); points raw/verified 11/1
  - p37 Meta legal proceedings charges recognized in Q2 2026 = **2,400,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Legal-proceedings charge is not capex and does not enter the capex build.] quote: "to incorporate the $2.4 billion charges related to legal proceedings recognized in the second quarter"
- dropped by code checks: 23 (period_end 2026-12-31 after as_of: 16; period_end 2027-12-31 after as_of: 1; scale word 'billion' not supported by quote or table header: 3; value_as_written not in quote as a whole number: 3)

### d3 [related_series] Revenue-linked capex intensity

Hypothesis: Meta's capex including finance leases has been rising as a share of revenue during the AI infrastructure build; Q3 2026 capex can be estimated as estimated Q3 2026 revenue multiplied by a recent or expected capex-intensity ratio, adjusted for any known step-up.

Queries issued by the searcher: Meta Q3 2026 revenue consensus estimate; Meta Platforms Q2 2026 results capital expenditures including finance leases; "Meta Reports First Quarter 2026 Results" capital expenditures including principal payments on finance leases revenue; Meta third quarter 2025 results capital expenditures including finance leases $19 billion revenue $51.24 billion

- `https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://pepperstone.com/en-au/insights/market-analysis/equities/q3-2026-earnings-preview-can-ai-deliver-the-next-breakout` -> **live_dated** (page date 2026-10-16); points raw/verified 15/6
  - p38 Meta Q3 2026 gross margin consensus (Bloomberg median estimate) = **80.16** % (2026-07-01..2026-09-30) [DISCARD: Gross-margin consensus is not a capex input.] quote: "Gross margin is seen at 80.16%, capex at $40.97bn and free cash flow at negative $9.14bn."
  - p39 Meta Q3 2026 adjusted EPS consensus (Bloomberg median estimate) = **6.85** USD per share (2026-07-01..2026-09-30) [DISCARD: EPS consensus is not a capex input; the revenue number in its quote has no separate data-point id.] quote: "Bloomberg median estimates point to Q3 revenue of $63.29bn, adjusted EPS of $6.85, operating income of $18.53bn and EBITDA of $26.99bn."
  - p40 Meta Q3 2026 implied operating margin (consensus-derived) = **29.3** % (2026-07-01..2026-09-30) [DISCARD: Operating-margin consensus is not a capex input.] quote: "Q3 operating margin is implied at roughly 29.3%, versus 40.1% a year earlier."
  - p41 Meta Q2 2026 advertising revenue year-on-year growth = **27** % (2026-04-01..2026-06-30) [DISCARD: Ad revenue growth is not a capex input.] quote: "Q2 advertising revenue rose 27% year-on-year, with impressions up 14% and average price per ad up 12%."
  - p42 Meta Q2 2026 ad impressions year-on-year growth = **14** % (2026-04-01..2026-06-30) [DISCARD: Ad impressions growth is not a capex input.] quote: "Q2 advertising revenue rose 27% year-on-year, with impressions up 14% and average price per ad up 12%."
  - p43 Meta Q2 2026 average price per ad year-on-year growth = **12** % (2026-04-01..2026-06-30) [DISCARD: Average price per ad growth is not a capex input.] quote: "Q2 advertising revenue rose 27% year-on-year, with impressions up 14% and average price per ad up 12%."
- `https://www.nasdaq.com/press-release/meta-reports-second-quarter-2026-results-2026-07-29` -> **live_dated** (page date 2026-07-29); points raw/verified 15/12
  - p44 Meta Q3 2026 total revenue guidance range (upper bound) = **64,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 revenue guidance upper bound; p67 contains the range and midpoint.] quote: "We expect third quarter 2026 total revenue to be in the range of $61-64 billion."
  - p45 Meta Q2 2026 capital expenditures including principal payments on finance leases = **31,080,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 company-measure capex; p1 is kept.] quote: "Capital expenditures - Capital expenditures, including principal payments on finance leases, were $31.08 billion."
  - p46 Meta Q2 2026 revenue = **60,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 revenue; p47 gives the exact table value.] quote: "Revenue - Revenue was $60.80 billion, an increase of 28% year-over-year."
  - p47 Meta Q2 2026 revenue (table, in millions) = **60,801,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "\| Revenue \| $ 60,801 \| \| $ 47,516 \| \| 28 % \|"
  - p48 Meta Q2 2025 revenue (table, in millions) = **47,516,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "\| Revenue \| $ 60,801 \| \| $ 47,516 \| \| 28 % \|"
  - p49 Meta Q2 2026 purchases of property and equipment = **-30,116,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 PP&E; p2 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p50 Meta Q2 2026 principal payments on finance leases = **-962,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 finance-lease principal; p3 is kept.] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p51 Meta Q2 2025 principal payments on finance leases = **-474,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 finance-lease principal; p5 is kept.] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p52 Meta Q2 2025 purchases of property and equipment = **-16,538,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 PP&E; p4 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p53 Meta H1 2026 purchases of property and equipment = **-49,113,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 PP&E; p6 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p54 Meta H1 2026 principal payments on finance leases = **-1,805,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 finance-lease principal; p7 is kept.] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p55 Meta H1 2026 revenue = **117,111,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "\| Revenue \| $ 60,801 \| \| $ 47,516 \| \| $ 117,111 \| \| $ 89,830 \|"
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 12 (scale word 'billion' not supported by quote or table header: 10; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end 2026-12-31 after as_of: 1)

### d4 [base_rates] Cash-flow accounting components

Hypothesis: The press-release metric is generally the sum of purchases of property and equipment and principal payments on finance leases; estimating those components separately, with the recent share of finance-lease principal in total capex, provides an independent build and a check on definitional differences.

Queries issued by the searcher: Meta cash flow statement purchases of property and equipment principal payments finance leases Q2 2026; Meta 10-Q principal payments on finance leases quarterly; "Meta Reports Third Quarter 2025 Results" "Principal payments on finance leases" purchases of property and equipment cash flow; "Meta Reports First Quarter 2026 Results" cash flows investing activities purchases of property and equipment principal payments finance leases

- `https://www.sec.gov/Archives/edgar/data/1326801/000162828025047114/meta-09302025xexhibit991.htm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nasdaq.com/press-release/meta-reports-second-quarter-2026-results-2026-07-29` -> **live_dated** (page date 2026-07-29); points raw/verified 15/13
  - p56 Meta capital expenditures including principal payments on finance leases, Q2 202 = **31,080,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 company-measure capex; p1 is kept.] quote: "Capital expenditures - Capital expenditures, including principal payments on finance leases, were $31.08 billion."
  - p57 Meta purchases of property and equipment, Q2 2026 (cash-flow statement) = **-30,116,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 PP&E; p2 is kept.] quote: "Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479)"
  - p58 Meta principal payments on finance leases, Q2 2026 (cash-flow statement) = **-962,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 finance-lease principal; p3 is kept.] quote: "Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225)"
  - p59 Meta purchases of property and equipment, Q2 2025 (cash-flow statement) = **-16,538,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 PP&E; p4 is kept.] quote: "Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479)"
  - p60 Meta principal payments on finance leases, Q2 2025 (cash-flow statement) = **-474,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 finance-lease principal; p5 is kept.] quote: "Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225)"
  - p61 Meta purchases of property and equipment, six months ended June 30, 2026 = **-49,113,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 PP&E; p6 is kept.] quote: "Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479)"
  - p62 Meta principal payments on finance leases, six months ended June 30, 2026 = **-1,805,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 finance-lease principal; p7 is kept.] quote: "Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225)"
  - p63 Meta purchases of property and equipment, six months ended June 30, 2025 = **-29,479,000,000** USD (2025-01-01..2025-06-30) [DISCARD: Duplicate H1 2025 PP&E; p8 is kept.] quote: "Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479)"
  - p64 Meta principal payments on finance leases, six months ended June 30, 2025 = **-1,225,000,000** USD (2025-01-01..2025-06-30) [DISCARD: Duplicate H1 2025 finance-lease principal; p9 is kept.] quote: "Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225)"
  - p65 Meta free cash flow, Q2 2026 (after subtracting purchases of PP&E and finance-le = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 is kept.] quote: "Free cash flow \| $ 784 \| \| $ 8,549 \| \| $ 13,170 \| \| $ 18,883"
  - p66 Meta net cash provided by operating activities, Q2 2026 = **31,862,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Net cash provided by operating activities \| $ 31,862 \| \| $ 25,561 \| \| $ 64,088 \| \| $ 49,587"
  - p67 Meta Q3 2026 total revenue guidance (forecast range) = **62,500,000,000** (range 61,000,000,000..64,000,000,000) as written "61-64 billion", value check ok USD (2026-07-01..2026-09-30) [keep: ] quote: "We expect third quarter 2026 total revenue to be in the range of $61-64 billion."
  - p68 Meta operating lease right-of-use assets, June 30, 2026 (balance sheet; no separ = **23,985,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Duplicate operating lease ROU asset; p112 is kept.] quote: "Operating lease right-of-use assets \| 23,985 \| \| 20,404"
- `https://finance.yahoo.com/news/meta-reports-third-quarter-2024-200500813.html` -> **dropped** (live http 404); points raw/verified -/-
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 2 (period_end 2026-12-31 after as_of: 2)

### d5 [shocks] Management outlook and supply/timing shocks

Hypothesis: Q2 2026 earnings-call commentary about raising or timing 2026 capex, AI supply constraints, data-center construction timing, or tariffs could shift Q3 spend away from a simple trend; measurable guidance changes and lead-time signals should be used to adjust any historical route.

Queries issued by the searcher: Meta Q2 2026 earnings call capex outlook Susan Li; Meta capital expenditures 2026 raised guidance; Meta Q2 2026 earnings call "capex" second half 2026 ramp Susan Li phasing; Meta data center 2026 AI compute supply constraint memory pricing tariff capex Q3 2026

- `https://www.marketbeat.com/earnings/reports/2026-7-29-facebook-inc-stock/` -> **live_dated** (page date 2026-07-29); points raw/verified 15/10
  - p69 Meta Q2 2026 capital expenditures including principal payments on finance leases = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 company-measure capex.] quote: "Capital expenditures, including principal payments on finance leases, were $31.1 billion, driven by investments in servers, data centers, and network infrastructure."
  - p70 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 is kept.] quote: "Free cash flow was $784 million."
  - p71 Meta Q2 2026 total expenses = **42,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Total expenses are not a capex input.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year"
  - p72 Meta Q2 2026 total revenue = **60,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 revenue; p47 is exact.] quote: "Q2 total revenue was $60.8 billion, up 28%, or 27% on a constant currency basis."
  - p73 Meta Q3 2026 total revenue guidance range = **62,500,000,000** (range 61,000,000,000..64,000,000,000) as written "$61 billion- $64 billion", value check pending USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 revenue guidance; p67 is kept.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion- $64 billion."
  - p74 Meta Q2 2026 GAAP operating income = **18,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: GAAP operating income is not a capex input.] quote: "Second quarter GAAP operating income was $18.8 billion, representing an 8% decline year-over-year and a 31% operating margin."
  - p75 Meta Q2 2026 legal proceedings charges = **2,400,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate legal-proceedings charge; not a capex input.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year, and included $2.4 billion in charges related to legal proceedings"
  - p76 Meta Q2 2026 severance expenses from May 2026 headcount reduction = **1,200,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Severance expense is not a capex input.] quote: "and $1.2 billion in severance expenses in connection with the May 2026 headcount reduction."
  - p77 Meta cash and marketable securities at end of Q2 2026 = **90,300,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Cash/securities is not a capex input and duplicates p87/p136.] quote: "We ended the quarter with $90.3 billion in cash and marketable securities and $83.7 billion in debt."
  - p78 Meta debt at end of Q2 2026 = **83,700,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Debt balance is not a capex input and duplicates p88/p105.] quote: "We ended the quarter with $90.3 billion in cash and marketable securities and $83.7 billion in debt."
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tikr.com/de/blog/meta-now-owes-22-billion-more-than-it-holds-heres-why-that-matters` -> **live_dated** (page date 2026-10-01); points raw/verified 15/1
  - p79 Meta capex as share of operating cash flow, quarter ended June 2026 = **95** % (2026-04-01..2026-06-30) [DISCARD: Duplicate capex/OCF ratio; p36 carries the same Q2 2026 context.] quote: "absorbierten etwa 95 % des operativen Cashflows - gegenüber 33 % im Quartal September 2024"
- `https://www.fool.com/earnings/call-transcripts/2026/08/07/meta-meta-q2-2026-earnings-call-transcript/` -> **live_dated** (page date 2026-08-07); points raw/verified 15/10
  - p80 Meta Q2 2026 capital expenditures including principal payments on finance leases = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 company-measure capex.] quote: "Capital expenditures, including principal payments on finance leases, were $31.1 billion, driven by investments in servers, data centers and network infrastructure."
  - p81 Meta Q3 2026 total revenue guidance range = **62,500,000,000** (range 61,000,000,000..64,000,000,000) as written "$61 billion to $64 billion", value check pending USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 revenue guidance; p67 is kept.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion to $64 billion."
  - p82 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 is kept.] quote: "Free cash flow was $784 million."
  - p83 Meta prior year period free cash flow = **8,500,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Prior-year FCF round duplicate; p100 gives the more precise figure but neither is a capex input.] quote: "a decrease from $8.5 billion in the prior year period due to higher infrastructure spending"
  - p84 Meta Q2 2026 total expenses = **42,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate total expenses; not a capex input.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year"
  - p85 Meta Q2 2026 legal proceedings charges = **2,400,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate legal-proceedings charge; not a capex input.] quote: "included $2.4 billion in charges related to legal proceedings"
  - p86 Meta Q2 2026 severance expenses from May 2026 headcount reduction = **1,200,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate severance expense; not a capex input.] quote: "and $1.2 billion in severance expenses in connection with the May 2026 head count reduction"
  - p87 Meta cash and marketable securities at end of Q2 2026 = **90,300,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Duplicate cash/securities; not a capex input.] quote: "We ended the quarter with $90.3 billion in cash and marketable securities and $83.7 billion in debt."
  - p88 Meta debt at end of Q2 2026 = **83,700,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Duplicate debt balance; not a capex input.] quote: "We ended the quarter with $90.3 billion in cash and marketable securities and $83.7 billion in debt."
  - p89 Meta employees impacted by May 2026 headcount reduction = **8,000** employees (2026-05-01..2026-05-31) [DISCARD: Employee headcount reduction is not a capex input.] quote: "This total includes approximately 8,000 employees impacted by the May 2026 head count reduction."
- dropped by code checks: 24 (period_end 2026-12-31 after as_of: 8; period_end missing or unparseable: 2; scale word 'billion' not supported by quote or table header: 10; scale word 'million' not supported by quote or table header: 1; number: low/high given but value_as_written is not a range: 3)

### d6 [capacity_consumption] AI infrastructure supply chain and data-center capacity

Hypothesis: Meta's capex is dominated by AI data centers, servers, and network infrastructure; announced data-center capacity additions, supplier backlogs or contract awards tied to Meta, and management's category-level spending plans can bound quarterly capex, especially if guidance splits server versus data-center spend.

Queries issued by the searcher: Meta 2026 capital expenditures guidance AI infrastructure servers data centers network; Meta 2026 capex $60 billion data center spending; Meta second quarter 2026 results capital expenditures $31.1 billion press release guidance $130 billion $145 billion; Meta Q2 2026 earnings call Susan Li capex "servers" percentage data center 2026 split

- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.datacenterdynamics.com/en/news/meta-raises-planned-capex-for-2026-plans-layoffs-for-efficiency-reasons/` -> **live_dated** (page date 2026-10-15); points raw/verified 15/3
  - p90 Meta step up in contractual commitments in Q1 2026 from multiyear cloud deals an = **107,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "These multiyear cloud deals and our infrastructure purchase agreements drove a $107 billion step up in our contractual commitments this quarter."
  - p91 Meta employees at end of Q1 2026 = **77,900** employees (2026-03-31..2026-03-31) [DISCARD: Employee count is not a capex input.] quote: "The company ended Q1 with around 77,900 employees, approximately one percent fewer than the quarter prior"
  - p92 Meta bond sale coupon range across tranches = **5.5** (range 4.55..6.45) as written "4.55 percent and 6.45 percent", value check pending % (2026-04-30..2026-04-30) [DISCARD: Bond coupon range is not a capex input.] quote: "with between a 4.55 percent and 6.45 percent rate"
- `https://www.webpronews.com/metas-60-billion-ai-bet-how-massive-data-center-spending-powers-ad-gains-and-tests-investor-patience/` -> **live_dated** (page date 2026-08-31); points raw/verified 15/2
  - p93 Meta second-quarter capital expenditures = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 company-measure capex.] quote: "Second-quarter capital expenditures reached $31.1 billion."
  - p94 Meta capital expenditures in 2025 = **72,000,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "Those forecasts dwarf the $72 billion spent in 2025."
- `https://www.outlookbusiness.com/deeptech/meta-to-spend-up-to-135b-in-2026-to-build-superintelligence-unit` -> **live_dated** (page date 2026-01-29); points raw/verified 13/0
- dropped by code checks: 38 (scale word 'billion' not supported by quote or table header: 9; period_end 2026-12-31 after as_of: 6; period_end missing or unparseable: 18; number: no number in value_as_written: 1; period_end 2027-12-31 after as_of: 1; period_end 2028-12-31 after as_of: 1; value_as_written not in quote as a whole number: 1; period_end 2030-12-31 after as_of: 1)

### d7 [related_series] Hyperscaler peer capex cycle

Hypothesis: Meta's capex cycle shares drivers with Microsoft, Alphabet, and Amazon; peer Q3 2026 capex levels and 2026 guidance can constrain Meta's growth rate and the direction of any surprise, though company-specific AI plans limit precision.

Queries issued by the searcher: hyperscaler capex Q3 2026 Microsoft Alphabet Amazon capital expenditures; Microsoft Alphabet Amazon 2026 capital expenditures guidance raised July 2026 earnings; Meta third quarter 2026 earnings capital expenditures guidance October 2026 outlook; "Q3 2026" capex consensus estimate Microsoft Alphabet Amazon preview October 2026 earnings

- `https://www.tmtfinance.com/intel/2026-hyperscaler-capex-tops-us700bn-analysis?trk=article-ssr-frontend-pulse_little-text-block` -> **live_dated** (page date 2026-08-18); points raw/verified 15/0
- `https://wap.stockstar.com/detail/IG2026101900012961` -> **live_dated** (page date 2026-10-01); points raw/verified 15/11
  - p95 Meta Q3 2026 consensus quarterly capital expenditure estimate = **40,970,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 2026 consensus capex; p20 is kept.] quote: "单季资本开支达到409.7亿美元"
  - p96 Meta H1 2026 capital expenditure consumed = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 company-measure capex; p21 is kept.] quote: "上半年已消耗约509亿美元"
  - p97 Meta Q2 2026 capital expenditure = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 company-measure capex.] quote: "资本开支高达311亿美元"
  - p98 Meta Q2 2026 operating cash flow = **31,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Rounded duplicate of Q2 2026 OCF; p66 is exact.] quote: "二季度,Meta经营性现金流为319亿美元"
  - p99 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 is kept.] quote: "自由现金流仅7.84亿美元"
  - p100 Meta prior-year Q2 free cash flow = **8,549,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Prior-year FCF duplicate; not a capex input.] quote: "远低于上年同期的85.49亿美元"
  - p101 Meta Q3 2026 consensus free cash flow estimate (negative) = **-9,140,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 2026 consensus FCF; p25 is kept.] quote: "自由现金流将转负至-91.4亿美元"
  - p102 Meta Q3 2026 revenue guidance range = **62,500,000,000** (range 61,000,000,000..64,000,000,000) as written "610亿至640亿", value check pending USD (2026-07-01..2026-09-30) [DISCARD: Duplicate Q3 revenue guidance; p67 is kept.] quote: "Meta此前给出的三季度营收指引为610亿至640亿美元"
  - p103 Meta Q3 2026 revenue guidance growth rate range vs prior year = **22** (range 19..25) as written "19%至25%", value check pending % (2026-07-01..2026-09-30) [keep: ] quote: "较上年同期的512亿美元增长19%至25%"
  - p104 Meta Q2 2026 long-term debt issued = **24,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Debt issuance is not a capex input.] quote: "二季度Meta发行了249亿美元长期债务"
  - p105 Meta long-term debt balance after Q2 2026 issuance = **83,700,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Duplicate debt balance; not a capex input.] quote: "长期债务余额升至837亿美元"
- `https://finance.yahoo.com/technology/ai/articles/ai-10-trillion-buildout-reach-175151308.html` -> **live_dated** (page date 2026-09-27); points raw/verified 15/0
- `https://www.digitaltoday.co.kr/en/view/115985/ai-data-centres-face-shortages-now-but-risk-overinvestment-shock-longer-term` -> **live_dated** (page date 2026-10-18); points raw/verified 12/0
- dropped by code checks: 46 (scale word 'billion' not supported by quote or table header: 20; value_as_written not in quote as a whole number: 1; period_end 2026-12-31 after as_of: 7; period_end 2027-12-31 after as_of: 1; period_end missing or unparseable: 12; scale word 'million' not supported by quote or table header: 1; period_end 2032-12-31 after as_of: 2; period_end 2030-12-31 after as_of: 2)

### d8 [base_rates] Balance-sheet and depreciation accounting

Hypothesis: Capex including finance leases can be cross-checked from the change in gross property and equipment and finance-lease assets plus retirements or disposals; historical relations among capex, depreciation, and gross asset growth can forecast Q3 from the Q2 2026 balance sheet.

Queries issued by the searcher: Meta Platforms second quarter 2026 results capital expenditures including finance leases; Meta Q2 2026 balance sheet property and equipment net accumulated depreciation; Meta Q2 2026 10-Q depreciation and amortization cash flow statement finance lease right-of-use assets; Meta Q3 2026 capital expenditures forecast estimate analysts September quarter 2026 preview

- `https://www.nasdaq.com/press-release/meta-reports-second-quarter-2026-results-2026-07-29` -> **live_dated** (page date 2026-07-29); points raw/verified 15/14
  - p106 Meta Q2 2026 capital expenditures including principal payments on finance leases = **31,080,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 company-measure capex; p1 is kept.] quote: "Capital expenditures - Capital expenditures, including principal payments on finance leases, were $31.08 billion."
  - p107 Meta Q2 2026 purchases of property and equipment (cash flow statement, quarterly = **-30,116,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 PP&E; p2 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p108 Meta Q2 2026 principal payments on finance leases (quarterly) = **-962,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 finance-lease principal; p3 is kept.] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p109 Meta Q2 2026 depreciation and amortization (quarterly) = **6,356,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "\| Depreciation and amortization \| 6,356 \| \| 4,342 \| \| 12,355 \| \| 8,242 \|"
  - p110 Meta property and equipment, net as of June 30, 2026 = **225,724,000,000** USD (2026-06-30..2026-06-30) [keep: ] quote: "\| Property and equipment, net \| 225,724 \| \| 176,400 \|"
  - p111 Meta property and equipment, net as of December 31, 2025 = **176,400,000,000** USD (2025-12-31..2025-12-31) [keep: ] quote: "\| Property and equipment, net \| 225,724 \| \| 176,400 \|"
  - p112 Meta operating lease right-of-use assets as of June 30, 2026 = **23,985,000,000** USD (2026-06-30..2026-06-30) [keep: ] quote: "\| Operating lease right-of-use assets \| 23,985 \| \| 20,404 \|"
  - p113 Meta operating lease right-of-use assets as of December 31, 2025 = **20,404,000,000** USD (2025-12-31..2025-12-31) [keep: ] quote: "\| Operating lease right-of-use assets \| 23,985 \| \| 20,404 \|"
  - p114 Meta operating lease liabilities, current as of June 30, 2026 = **2,425,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Operating-lease liability is not the capex measure and is not used.] quote: "\| Operating lease liabilities, current \| 2,425 \| \| 2,213 \|"
  - p115 Meta operating lease liabilities, non-current as of June 30, 2026 = **26,229,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Operating-lease liability is not the capex measure and is not used.] quote: "\| Operating lease liabilities, non-current \| 26,229 \| \| 22,940 \|"
  - p116 Meta H1 2026 purchases of property and equipment (six months) = **-49,113,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 PP&E; p6 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
  - p117 Meta H1 2026 principal payments on finance leases (six months) = **-1,805,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 finance-lease principal; p7 is kept.] quote: "\| Principal payments on finance leases \| (962) \| \| (474) \| \| (1,805) \| \| (1,225) \|"
  - p118 Meta H1 2026 depreciation and amortization (six months) = **12,355,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "\| Depreciation and amortization \| 6,356 \| \| 4,342 \| \| 12,355 \| \| 8,242 \|"
  - p119 Meta Q2 2025 purchases of property and equipment (prior-year quarter) = **-16,538,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 PP&E; p4 is kept.] quote: "\| Purchases of property and equipment \| (30,116) \| \| (16,538) \| \| (49,113) \| \| (29,479) \|"
- `http://archive.fast-edgar.com/20260811/AA22U62FZZ2R8ZZA229M2ZYSFPRH4Z22Z282/R34.htm` -> **live_dated** (page date 2026-08-11); points raw/verified 15/11
  - p120 Finance lease right-of-use assets (vehicles), Meta Platforms, as of June 30, 202 = **24,517,000** USD (2026-06-30..2026-06-30) [DISCARD: Vehicle finance-lease ROU asset is tiny and not the total finance-lease principal measure; misleading for p3.] quote: "Vehicles \| \| $ \| \| 24,517 \| \| \| $ \| \| 25,861"
  - p121 Finance lease right-of-use assets (vehicles), Meta Platforms, as of December 31, = **25,861,000** USD (2025-12-31..2025-12-31) [DISCARD: Vehicle finance-lease ROU asset is tiny and not the total finance-lease principal measure.] quote: "Vehicles \| \| $ \| \| 24,517 \| \| \| $ \| \| 25,861"
  - p122 Finance lease liabilities, current, Meta Platforms, as of June 30, 2026 = **13,044,000** USD (2026-06-30..2026-06-30) [DISCARD: Vehicle finance-lease liability is tiny and not the total finance-lease principal measure.] quote: "Current \| \| $ \| \| 13,044 \| \| \| $ \| \| 12,895"
  - p123 Finance lease liabilities, non-current, Meta Platforms, as of June 30, 2026 = **9,151,000** USD (2026-06-30..2026-06-30) [DISCARD: Vehicle finance-lease liability is tiny and not the total finance-lease principal measure.] quote: "Non-current \| \| \| \| 9,151 \| \| \| \| \| 10,862"
  - p124 Depreciation of vehicles finance right-of-use assets, Meta Platforms, three mont = **3,641,000** USD (2026-04-01..2026-06-30) [DISCARD: Vehicle finance-lease depreciation is tiny and not the total finance-lease principal measure.] quote: "(included in depreciation and amortization) \| \| $ \| \| 3,641 \| \| \| $ \| \| 1,587"
  - p125 Depreciation of vehicles finance right-of-use assets, Meta Platforms, six months = **7,122,000** USD (2026-01-01..2026-06-30) [DISCARD: Vehicle finance-lease depreciation is tiny and not the total finance-lease principal measure.] quote: "\| \| $ \| \| 7,122 \| \| \| $ \| \| 3,741"
  - p126 Financing cash flows from finance leases, Meta Platforms, three months ended Jun = **4,165,000** USD (2026-04-01..2026-06-30) [DISCARD: Vehicle finance-lease financing cash flow is tiny and not the total finance-lease principal measure.] quote: "Financing cash flows from finance leases \| \| \| \| 4,165 \| \| \| \| \| 2,834"
  - p127 Financing cash flows from finance leases, Meta Platforms, six months ended June  = **8,220,000** USD (2026-01-01..2026-06-30) [DISCARD: Vehicle finance-lease financing cash flow is tiny and not the total finance-lease principal measure.] quote: "\| \| \| \| 8,220 \| \| \| \| \| 5,663"
  - p128 Interest expense (recovery) of vehicles finance right-of-use assets, Meta Platfo = **358,000** USD (2026-04-01..2026-06-30) [DISCARD: Vehicle finance-lease interest is tiny and not the total finance-lease principal measure.] quote: "(included in interest expense) \| \| $ \| \| 358 \| \| \| $ \| \| 1,794"
  - p129 Operating right-of-use assets (real property), Meta Platforms, as of June 30, 20 = **21,323,000** USD (2026-06-30..2026-06-30) [DISCARD: Operating right-of-use real-property asset is not capex.] quote: "Real property \| \| $ \| \| 21,323 \| \| \| $ \| \| 17,556"
  - p130 Finance lease total future minimum lease payments, Meta Platforms, as of June 30 = **23,457,000** USD (2026-06-30..2026-06-30) [DISCARD: Vehicle finance-lease future minimum payments are tiny and not the total finance-lease principal measure.] quote: "Total future minimum lease payments \| \| \| \| 24,561 \| \| \| \| \| 23,457"
- `https://www.advfn.com/stock-market/NASDAQ/META/stock-news/99005866/form-8-k-current-report` -> **dropped** (live http 403); points raw/verified -/-
- `https://finance.yahoo.com/markets/stocks/articles/meta-now-owes-22-billion-112355817.html` -> **live_dated** (page date 2026-10-01); points raw/verified 15/11
  - p131 Meta capex on TIKR's narrower measure, June 2026 quarter = **30,120,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate TIKR Q2 2026 capex; p11 is kept.] quote: "Meta's capex reached $30.12 billion in the June 2026 quarter against $31.86 billion of operating cash flow"
  - p132 Meta operating cash flow, June 2026 quarter = **31,860,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 OCF; p66 is exact.] quote: "against $31.86 billion of operating cash flow, leaving $1.75 billion of free cash flow on TIKR's measure"
  - p133 Meta free cash flow on TIKR's measure, June 2026 quarter = **1,750,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate TIKR Q2 2026 FCF; p13 is kept.] quote: "leaving $1.75 billion of free cash flow on TIKR's measure, down from $9.02 billion a year earlier"
  - p134 Meta free cash flow on TIKR's measure, June 2025 quarter = **9,020,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate TIKR prior-year FCF; not a capex input.] quote: "leaving $1.75 billion of free cash flow on TIKR's measure, down from $9.02 billion a year earlier"
  - p135 Meta total debt including lease liabilities (TIKR measure), June 2026 = **112,320,000,000** USD (2026-06-30..2026-06-30) [DISCARD: TIKR total debt including leases is not the capex measure.] quote: "TIKR's total debt measure, including lease liabilities, stood at $112.32 billion against $90.26 billion of cash and marketable securities."
  - p136 Meta cash and marketable securities, June 2026 = **90,260,000,000** USD (2026-06-30..2026-06-30) [DISCARD: Cash/securities is not a capex input.] quote: "stood at $112.32 billion against $90.26 billion of cash and marketable securities."
  - p137 Meta free cash flow as reported on earnings call, June 2026 quarter = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate Q2 2026 FCF; p10 is kept.] quote: ""Free cash flow was $784 million.""
  - p138 Meta operating cash flow, June 2025 quarter = **25,560,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "Operating cash flow rose from $25.56 billion to $31.86 billion in a year"
  - p139 Meta capex, June 2025 quarter = **16,540,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate Q2 2025 TIKR capex; p30 is kept.] quote: "Capex went from $16.54 billion to $30.12 billion, up 82%"
  - p140 Meta capex, trailing four quarters through June 2026 = **89,330,000,000** USD (2025-07-01..2026-06-30) [DISCARD: Duplicate trailing-four-quarter capex; p17 is kept.] quote: "Capex totaled $89.33 billion against $52.17 billion in the four quarters before"
  - p141 Meta first-half 2026 capex on Meta's measure = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate H1 2026 company-measure capex; p21 is kept.] quote: "The first half used about $50.9 billion of capex on Meta's measure."
- dropped by code checks: 9 (period_end 2026-12-31 after as_of: 6; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### b1 [forecasts_markets] Consensus definition and dispersion

Hypothesis: Confirming whether the Q3 2026 consensus capex in p20 is on Meta's including-finance-lease measure, and obtaining its analyst range and count, would directly narrow the m1 adjustment factor a1. This is the single strongest market anchor and currently its definition is the main unresolved issue.

Queries issued by the searcher: Meta Q3 2026 capex consensus analysts estimate capital expenditures including finance leases; Meta Platforms third quarter 2026 earnings capital expenditures including principal payments on finance leases; "40.97 billion" OR "40.9 billion" Meta Q3 2026 capex consensus estimate range analysts; Meta Q3 2026 earnings preview "capital expenditures" consensus estimate LSEG Visible Alpha analysts expect

- `https://finance.eastmoney.com/a/202610193899817454.html` -> **live_dated** (page date 2026-10-19); points raw/verified 15/11
  - p142 Meta Q3 2026 consensus revenue estimate (institutional expectation) = **63,390,000,000** USD (2026-07-01..2026-09-30) [keep: ] quote: "机构预期Q3实现营收633.9亿美元,同比增加23.71%"
  - p143 Meta Q3 2026 consensus EPS estimate (institutional expectation) = **5.7** USD per share (2026-07-01..2026-09-30) [DISCARD: Q3 2026 EPS consensus is irrelevant to the capex level.] quote: "预期每股收益5.70美元,同比增加442.86%"
  - p144 Meta Q2 2026 revenue (actual) = **60,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 revenue p47.] quote: "二季度,Meta实现营收608亿美元,同比增长28%"
  - p145 Meta Q2 2026 advertising revenue (actual) = **59,360,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Advertising revenue is irrelevant to the capex estimate.] quote: "广告收入593.6亿美元,同比增长27%"
  - p146 Meta Q2 2026 net profit (actual) = **15,850,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Net profit is irrelevant to the capex estimate.] quote: "净利润158.5亿美元,同比下降14%"
  - p147 Meta Q3 2026 company revenue guidance range (lower bound) = **61,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "公司此前给出的三季度营收指引为610亿至640亿美元"
  - p148 Meta Q3 2026 company revenue guidance range (upper bound) = **64,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "公司此前给出的三季度营收指引为610亿至640亿美元"
  - p149 Meta Q2 2026 operating cash flow (actual) = **31,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 operating cash flow p66.] quote: "Q2 Meta经营性现金流319亿美元"
  - p150 Meta Q2 2026 capital expenditures including finance leases (actual) = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 capex p1.] quote: "但资本开支(含融资租赁)高达311亿美元"
  - p151 Meta Q2 2026 free cash flow (actual) = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 free cash flow p10.] quote: "自由现金流仅7.84亿美元"
  - p152 Meta H1 2026 capital expenditures spent (cumulative) = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate of H1 2026 capex p21.] quote: "上半年已花掉约509亿美元"
- `https://www.businesstimescn.com/articles/630035.html` -> **live_dated** (page date 2026-10-17); points raw/verified 15/0
- `https://wap.stockstar.com/detail/IG2026101900012961` -> **live_dated** (page date 2026-10-01); points raw/verified 15/8
  - p153 Meta Q3 2026 consensus quarterly capital expenditure (institution consensus, sin = **40,970,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 consensus capex p20.] quote: "机构一致预期显示,自由现金流将转负至-91.4亿美元,单季资本开支达到409.7亿美元。"
  - p154 Meta Q3 2026 consensus free cash flow (institution consensus, single quarter) = **-9,140,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 consensus free cash flow p25.] quote: "机构一致预期显示,自由现金流将转负至-91.4亿美元,单季资本开支达到409.7亿美元。"
  - p155 Meta first-half 2026 capital expenditure consumed (cumulative) = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate of H1 2026 capex p21.] quote: "上半年已消耗约509亿美元,按此推算下半年资本开支将达790亿至940亿美元。"
  - p156 Meta Q2 2026 capital expenditure (actual, single quarter) = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 capex p1.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元"
  - p157 Meta Q2 2026 operating cash flow (actual, single quarter) = **31,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 operating cash flow p66.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元"
  - p158 Meta Q2 2026 free cash flow (actual, single quarter) = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 free cash flow p10.] quote: "二季度,Meta经营性现金流为319亿美元,资本开支高达311亿美元,自由现金流仅7.84亿美元,远低于上年同期的85.49亿美元。"
  - p159 Meta Q2 2025 free cash flow (prior-year comparable, single quarter) = **8,549,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "自由现金流仅7.84亿美元,远低于上年同期的85.49亿美元。"
  - p160 Meta Q3 2026 revenue guidance given by company (low end) = **61,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance lower bound p67.] quote: "Meta此前给出的三季度营收指引为610亿至640亿美元,较上年同期的512亿美元增长19%至25%"
- `https://polymarket.com/zh-hant/event/will-meta-meta-q3-capital-expenditures-including-principal-payments-on-finance-leases-be-above-20261008120055000` -> **live_dated** (page date 2026-10-18); points raw/verified 5/2
  - p161 Meta Q2 2026 capital expenditures (actual, quarterly) = **31,080,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 capex p1.] quote: "After spending $31.08 billion in Q2"
  - p162 Meta capital expenditures through first half of 2026 (cumulative) = **50,900,000,000** USD (2026-01-01..2026-06-30) [DISCARD: Duplicate of H1 2026 capex p21.] quote: "roughly $50.9 billion through the first half"
- dropped by code checks: 29 (period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end 2026-12-31 after as_of: 10; period year 2026 does not appear in the page text or URL (likely mis-dated): 8; period_end missing or unparseable: 4; period_end 2027-12-31 after as_of: 2; scale word 'billion' not supported by quote or table header: 1)

### b2 [own_history] Seasonal and sequential Q3 pattern

Hypothesis: Q3 2025 actual capex including finance leases, purchases of PP&E, and finance-lease principal would let us apply a YoY or sequential Q3 ramp and calibrate the Q3 share of H2 capex in m2 and the PP&E step-up in m4. Lack of a prior Q3 value is the main reason we cannot use historical-series methods directly.

Queries issued by the searcher: Meta Q3 2025 earnings release capital expenditures including principal payments on finance leases; Meta third quarter 2025 results "purchases of property and equipment" "principal payments on finance leases" cash flow; "Capital expenditures, including principal payments on finance leases" 19,370 Meta "September 30, 2025" press release; prnewswire "Meta Reports Third Quarter 2025 Results" capital expenditures 19,370

- `https://www.sec.gov/Archives/edgar/data/1326801/000162828025047114/meta-09302025xexhibit991.htm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nasdaq.com/press-release/meta-reports-third-quarter-2025-results-2025-10-29` -> **live_dated** (page date 2025-10-29); points raw/verified 15/13
  - p163 Meta Q3 2025 capital expenditures including principal payments on finance leases = **19,370,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "Capital expenditures - Capital expenditures, including principal payments on finance leases, were $19.37 billion."
  - p164 Meta Q3 2025 purchases of property and equipment (cash-flow statement), consolid = **18,829,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "\| Purchases of property and equipment \| \| (18,829) \| \| (8,258) \| \| (48,308) \| \| (22,831) \|"
  - p165 Meta Q3 2025 principal payments on finance leases (cash-flow statement), consoli = **545,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "\| Principal payments on finance leases \| \| (545) \| \| (944) \| \| (1,770) \| \| (1,558) \|"
  - p166 Meta Q3 2024 purchases of property and equipment (cash-flow statement), consolid = **8,258,000,000** USD (2024-07-01..2024-09-30) [keep: ] quote: "\| Purchases of property and equipment \| \| (18,829) \| \| (8,258) \| \| (48,308) \| \| (22,831) \|"
  - p167 Meta Q3 2024 principal payments on finance leases (cash-flow statement), consoli = **944,000,000** USD (2024-07-01..2024-09-30) [keep: ] quote: "\| Principal payments on finance leases \| \| (545) \| \| (944) \| \| (1,770) \| \| (1,558) \|"
  - p168 Meta nine months 2025 purchases of property and equipment (cash-flow statement), = **48,308,000,000** USD (2025-01-01..2025-09-30) [keep: ] quote: "\| Purchases of property and equipment \| \| (18,829) \| \| (8,258) \| \| (48,308) \| \| (22,831) \|"
  - p169 Meta nine months 2025 principal payments on finance leases (cash-flow statement) = **1,770,000,000** USD (2025-01-01..2025-09-30) [keep: ] quote: "\| Principal payments on finance leases \| \| (545) \| \| (944) \| \| (1,770) \| \| (1,558) \|"
  - p170 Meta nine months 2024 purchases of property and equipment (cash-flow statement), = **22,831,000,000** USD (2024-01-01..2024-09-30) [keep: ] quote: "\| Purchases of property and equipment \| \| (18,829) \| \| (8,258) \| \| (48,308) \| \| (22,831) \|"
  - p171 Meta nine months 2024 principal payments on finance leases (cash-flow statement) = **1,558,000,000** USD (2024-01-01..2024-09-30) [keep: ] quote: "\| Principal payments on finance leases \| \| (545) \| \| (944) \| \| (1,770) \| \| (1,558) \|"
  - p172 Meta full year 2025 capital expenditures including principal payments on finance = **72,000,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "We currently expect 2025 capital expenditures, including principal payments on finance leases, to be in the range of $70-72 billion, increased from our prior outlook of $66-72 billion."
  - p173 Meta Q3 2025 free cash flow (net cash from operations less PP&E purchases and fi = **10,625,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "\| Free cash flow \| $ 10,625 \| \| $ 15,522 \| \| $ 29,508 \| \| $ 38,951 \|"
  - p174 Meta Q3 2025 net cash provided by operating activities, consolidated worldwide = **29,999,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "\| Net cash provided by operating activities \| $ 29,999 \| \| $ 24,724 \| \| $ 79,586 \| \| $ 63,340 \|"
  - p175 Meta property and equipment, net, balance at 2025-09-30 = **160,270,000,000** USD (2025-09-30..2025-09-30) [keep: ] quote: "\| Property and equipment, net \| \| 160,270 \| \| 121,346 \|"
- `https://www.fool.com/earnings/call-transcripts/2025/10/29/meta-platforms-meta-q3-2025-earnings-call-transcript/` -> **live_dated** (page date 2025-10-29); points raw/verified 15/12
  - p176 Meta Q3 2025 capital expenditures including principal payments on finance leases = **19,400,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Rounded duplicate of Q3 2025 capex p163.] quote: "Capital expenditures including principal payments on finance leases were $19.4 billion, driven by investments in servers data centers, and network infrastructure."
  - p177 Meta full-year 2025 capital expenditures including principal payments on finance = **72,000,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of FY2025 capex guidance p172.] quote: "We currently expect 2025 capital expenditures including principal payments on finance leases, to be in the range of $70 to $72 billion increased from our prior outlook of $66 to $72 billion."
  - p178 Meta prior full-year 2025 capital expenditures including principal payments on f = **72,000,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of FY2025 capex guidance p172.] quote: "increased from our prior outlook of $66 to $72 billion."
  - p179 Meta Q3 2025 free cash flow = **10,600,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Duplicate of Q3 2025 free cash flow p173.] quote: "Free cash flow was $10.6 billion."
  - p180 Meta Q3 2025 total expenses = **30,700,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Q3 2025 total expenses are irrelevant to the capex level.] quote: "Q3 total expenses were $30.7 billion, up 32% compared to last year."
  - p181 Meta Q3 2025 total revenue = **51,200,000,000** USD (2025-07-01..2025-09-30) [keep: ] quote: "Q3 total revenue was $51.2 billion, up 26% or 25% on a constant currency basis."
  - p182 Meta Q3 2025 operating income = **20,500,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Q3 2025 operating income is irrelevant to the capex level.] quote: "Third quarter operating income was $20.5 billion, representing a 40% operating margin."
  - p183 Meta Q4 2025 total revenue guidance, lower bound = **56,000,000,000** USD (2025-10-01..2025-12-31) [DISCARD: Q4 2025 revenue guidance is from an earlier period and irrelevant to Q3 2026 capex.] quote: "We expect fourth quarter 2025 total revenue to be in the range of $56 billion to $59 billion."
  - p184 Meta Q4 2025 total revenue guidance, upper bound = **59,000,000,000** USD (2025-10-01..2025-12-31) [DISCARD: Q4 2025 revenue guidance is from an earlier period and irrelevant to Q3 2026 capex.] quote: "We expect fourth quarter 2025 total revenue to be in the range of $56 billion to $59 billion."
  - p185 Meta full-year 2025 total expenses outlook, lower bound = **116,000,000,000** USD (2025-01-01..2025-12-31) [DISCARD: FY2025 total expenses outlook is irrelevant to the capex level.] quote: "We expect full year 2025 total expenses to be in the range of $116 billion to $118 billion updated from our prior outlook of $114 a $118 billion"
  - p186 Meta full-year 2025 total expenses outlook, upper bound = **118,000,000,000** USD (2025-01-01..2025-12-31) [DISCARD: FY2025 total expenses outlook is irrelevant to the capex level.] quote: "We expect full year 2025 total expenses to be in the range of $116 billion to $118 billion updated from our prior outlook of $114 a $118 billion"
  - p187 Meta Q3 2025 cash and marketable securities on hand = **44,400,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Cash and debt balances do not directly determine the Q3 2026 capex level.] quote: "We ended the quarter with $44.4 billion in cash and marketable securities and $28.8 billion in debt."
- `https://cdn1.benzinga.com/markets/earnings/25/10/48513171/meta-stock-drops-after-q3-earnings-capex-will-be-notably-larger-in-2026` -> **dropped** (live http 404); points raw/verified -/-
- dropped by code checks: 5 (scale word 'billion' not supported by quote or table header: 4; period_end missing or unparseable: 1)

### b3 [shocks] Official FY2026 guidance and H2 split

Hypothesis: Official FY2026 capex guidance and Q2 2026 call commentary on H2 ramp, AI supply timing, and data-center deliveries would pin the H2 total and Q3/Q4 split more tightly than the secondary article quote in p21. That would reduce a2 and a3 uncertainty in m2 and provide a check on m3 and m4.

Queries issued by the searcher: Meta Q2 2026 earnings call capex guidance 2026 capital expenditures; Meta second quarter 2026 results capital expenditures guidance CFO Susan Li; Meta Q2 2026 earnings call transcript Susan Li "second half" capex ramp data center deliveries; Meta capital expenditures first quarter 2026 $21 billion Q1 2026 capex including finance leases

- `https://www.marketbeat.com/earnings/reports/2026-7-29-facebook-inc-stock/` -> **live_dated** (page date 2026-07-29); points raw/verified 15/9
  - p188 Meta Q2 2026 capital expenditures including principal payments on finance leases = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 capex p1.] quote: "Capital expenditures, including principal payments on finance leases, were $31.1 billion, driven by investments in servers, data centers, and network infrastructure."
  - p189 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 free cash flow p10.] quote: "Free cash flow was $784 million."
  - p190 Meta Q2 2026 total expenses = **42,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Q2 2026 total expenses are irrelevant to the capex level.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year"
  - p191 Meta Q3 2026 total revenue guidance (lower bound) = **61,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion- $64 billion."
  - p192 Meta Q3 2026 total revenue guidance (upper bound) = **64,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion- $64 billion."
  - p193 Meta Q2 2026 total revenue = **60,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 revenue p47.] quote: "Q2 total revenue was $60.8 billion, up 28%, or 27% on a constant currency basis."
  - p194 Meta Q2 2026 GAAP operating income = **18,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Q2 2026 operating income is irrelevant to the capex level.] quote: "Second quarter GAAP operating income was $18.8 billion, representing an 8% decline year-over-year and a 31% operating margin."
  - p195 Meta Q2 2026 legal proceedings charges = **2,400,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Legal-proceedings charges are irrelevant to the capex level.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year, and included $2.4 billion in charges related to legal proceedings"
  - p196 Meta Q2 2026 severance expenses from May 2026 headcount reduction = **1,200,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Severance expenses are irrelevant to the capex level.] quote: "and $1.2 billion in severance expenses in connection with the May 2026 headcount reduction"
- `https://www.fool.com/earnings/call-transcripts/2026/08/07/meta-meta-q2-2026-earnings-call-transcript/` -> **live_dated** (page date 2026-08-07); points raw/verified 15/8
  - p197 Meta Q2 2026 capital expenditures, including principal payments on finance lease = **31,100,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 capex p1.] quote: "Capital expenditures, including principal payments on finance leases, were $31.1 billion, driven by investments in servers, data centers and network infrastructure."
  - p198 Meta Q2 2026 free cash flow = **784,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 free cash flow p10.] quote: "Free cash flow was $784 million."
  - p199 Meta prior-year Q2 free cash flow = **8,500,000,000** USD (2025-04-01..2025-06-30) [DISCARD: Duplicate of prior-year Q2 free cash flow p159.] quote: "Free Cash Flow -- $784 million, a decrease from $8.5 billion in the prior year period due to higher infrastructure spending."
  - p200 Meta Q3 2026 total revenue guidance, lower bound = **61,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion to $64 billion."
  - p201 Meta Q3 2026 total revenue guidance, upper bound = **64,000,000,000** USD (2026-07-01..2026-09-30) [DISCARD: Duplicate of Q3 2026 revenue guidance p67.] quote: "We expect third quarter 2026 total revenue to be in the range of $61 billion to $64 billion."
  - p202 Meta Q2 2026 total expenses = **42,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 2026 total expenses p190.] quote: "Q2 total expenses were $42 billion, up 55% compared to last year"
  - p203 Meta Q2 2026 legal proceedings charges included in total expenses = **2,400,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of legal-proceedings charges p195.] quote: "included $2.4 billion in charges related to legal proceedings and $1.2 billion in severance expenses"
  - p204 Meta Q2 2026 severance expenses from May 2026 headcount reduction = **1,200,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of severance expenses p196.] quote: "included $2.4 billion in charges related to legal proceedings and $1.2 billion in severance expenses in connection with the May 2026 head count reduction"
- `https://blockspace.media/insight/meta-lifts-2026-capex-ai-infrastructure-spending/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.metricduck.com/company/meta/earnings` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 13 (period_end 2026-12-31 after as_of: 12; period_end missing or unparseable: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['meta capex', 'meta capital expenditures', 'meta earnings']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p45', 'p56', 'p106'] All are the same Q2 2026 first-reported company-measure capex figure ($31.08B) from the same earnings release; duplicates of one underlying measurement, not independent confirmation.
- corroborating: ['p2', 'p49', 'p57', 'p107'] Same Q2 2026 purchases of property and equipment from the cash-flow statement; duplicates. p2 plus p3 reconciles closely to p1, supporting the press-release definition.
- corroborating: ['p3', 'p50', 'p58', 'p108'] Same Q2 2026 principal payments on finance leases; duplicates. This is the finance-lease bridge between the narrower PP&E component and Meta's including-finance-lease capex measure.
- corroborating: ['p6', 'p7', 'p15', 'p21', 'p28', 'p53', 'p54', 'p61', 'p62', 'p96', 'p116', 'p117', 'p141'] H1 2026 PP&E and finance-lease principal components reconcile approximately to the reported H1 company-measure capex of about $50.9B; duplicates and rounding variants of the same release.
- corroborating: ['p11', 'p13', 'p29', 'p131', 'p133'] TIKR/Yahoo narrower capex and TIKR free cash flow for Q2 2026. They corroborate the company release after allowing for the roughly $0.96B finance-lease principal gap between TIKR capex and Meta's incl
- corroborating: ['p20', 'p95'] Same Q3 2026 analyst consensus single-quarter capex figure ($40.97B); same underlying consensus source, so not independent.
- corroborating: ['p22', 'p69', 'p80', 'p93', 'p97'] Rounded Q2 2026 company-measure capex around $31.1B, consistent with the exact $31.08B figure; rounding duplicates rather than separate evidence.
- corroborating: ['p10', 'p24', 'p65', 'p70', 'p82', 'p99', 'p137'] Same Q2 2026 free cash flow figure ($784M) repeated across sources/articles; one underlying company measure.
- corroborating: ['p26', 'p27', 'p44', 'p67', 'p73', 'p81', 'p102'] Same Q3 2026 revenue guidance range ($61-64B); p67 supplies the midpoint and range. Duplicates from multiple articles.
- corroborating: ['p12', 'p34', 'p66', 'p132'] Same Q2 2026 operating cash flow, around $31.86B; p66 gives the exact cash-flow-statement figure.
- context: ['p19', 'p36', 'p79'] Capex as a share of operating cash flow rose from about 33% in the September 2024 quarter to about 95% in Q2 2026. Different periods and not contradictory; supports a steep AI-infrastructure ramp.
- corroborating: ['p25', 'p101'] Same Q3 2026 consensus free cash flow forecast of -$9.14B. Because it comes from the same consensus article as p20, it is not an independent capex source.
- corroborating: ['p4', 'p5', 'p8', 'p9', 'p16', 'p30', 'p52', 'p59', 'p60', 'p63', 'p64', 'p119', 'p139'] Prior-year PP&E, finance-lease principal, and TIKR capex provide a consistent history after definitional differences; duplicates and narrower-measure variants are not independent.
- conflicting: ['p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130'] These finance-lease note items appear to cover vehicle finance leases and are on a much smaller scale than the $962M quarterly principal payments on finance leases in the cash-flow statement. They are
- context: ['p90', 'p94'] The $107B step-up in contractual commitments and the $72B 2025 capex base support the direction of a large 2026 infrastructure ramp, but do not pin the Q3 2026 quarter.
- context: ['p109', 'p110', 'p111', 'p118'] PP&E net, D&A, and H1 D&A are consistent with a large ongoing capex program, but they are not a direct quarterly capex estimate.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p150', 'p156', 'p161', 'p188', 'p197'] Q2 2026 capex including finance leases is reported around $31.08-31.1B; p2 plus p3 reconciles to p1. The other ids are rounded or repeated versions of the same quarterly release, not independent measu
- corroborating: ['p4', 'p5', 'p31', 'p1'] Q2 2025 PP&E purchases plus finance-lease principal give the prior-year company-capex base. Comparing p1 with that base implies high-80s percent YoY growth, consistent with p31's 82% growth on a sligh
- corroborating: ['p163', 'p164', 'p165', 'p166', 'p167'] Q3 2025 capex including finance leases is $19.37B; p164 plus p165 reconciles to that total. p166-p167 show the same cash-flow definition for Q3 2024, confirming the component mapping.
- corroborating: ['p20', 'p25'] Same article: Q3 2026 consensus capex $40.97B and consensus free cash flow -$9.14B. The capex consensus is a useful market anchor, but p25 is not an independent confirmation of capex.
- corroborating: ['p21', 'p152', 'p155', 'p162'] H1 2026 capex around $50.9B is repeated across secondary sources. p21's quote also projects H2 2026 capex at $79-94B, but that H2 projection is a secondary article projection, not official company gui
- corroborating: ['p67', 'p142'] Q3 2026 company revenue guidance is $61-64B; the $63.39B institutional consensus in p142 lies inside that range. This supports using p67 as a revenue base for capex-intensity routes.
- corroborating: ['p47', 'p48', 'p55'] Q2 2026 revenue is $60.801B versus $47.516B in Q2 2025, and H1 2026 revenue is $117.111B. These are the revenue denominators for capex-intensity and growth checks.
- corroborating: ['p10', 'p66', 'p1'] Q2 2026 free cash flow of $0.784B is consistent with operating cash flow p66 less capex p1. This supports treating p1 as the cash capex measure including finance-lease principal, not an accrual capex 
- corroborating: ['p109', 'p118', 'p110', 'p111', 'p112', 'p113'] Rising D&A and net PP&E/operating lease ROU assets confirm heavy infrastructure investment, but they do not directly pin Q3 2026 capex timing.
- corroborating: ['p11', 'p1', 'p2', 'p3'] p11's $30.12B is TIKR's narrower PP&E-only measure, not a contradiction to p1's $31.08B company measure including finance leases; the difference is the finance-lease principal component.
- corroborating: ['p19', 'p36'] Capex/operating cash flow rose from 33% in the September 2024 quarter to 95% in Q2 2026 on TIKR's measure. Different periods and definitions limit precision, but the direction confirms the AI infrastr
- corroborating: ['p90'] A $107B step-up in contractual commitments from multiyear cloud and infrastructure purchase agreements supports elevated infrastructure spend, but it does not give a Q3 2026 cash-capex amount by itsel
- corroborating: ['p94', 'p172'] FY2025 capex of $72B and FY2025 guidance of $70-72B provide the prior-year base for the 2026 step-up. These are context, not a direct forecast of Q3 2026.
- corroborating: ['p8', 'p9', 'p21', 'p94', 'p163'] H1 2025 components, FY2025 capex, and Q3 2025 capex imply that Q3 2025 was a little under half of H2 2025 capex. This supports a Q3 share of H2 near 0.47 in the H2-split route.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Consensus-to-company-capex-measure adjustment | 1.01 | 0.98..1.04 | 0.7139..1.428 (widened) | dimensionless | m1 (m1) | p20 gives a Q3 2026 single-quarter capex consensus of $40.97B but does not explicitly state whether it is Meta's including-finance-lease measure or a narrower PP&E-only measure. Q2 2026 shows the finance-lease principal component is small relative to total capex, so the adjustment should be close to | The p20 consensus is a forecast of Meta's consolidated quarterly capex under either the company measure or a closely related PP&E-only measure. | Evidence that the consensus excludes or includes a materially different item, such as large accrued capex, acquisitions, or finance leases far outside the stated adjustment range. |
| a2 | H2 2026 capex divided by H1 2026 capex | 1.7 | 1.55..1.85 | 1.197..2.395 (widened) | ratio | m2 (m2) | The p21 quote projects H2 2026 capex at $79-94B against H1 2026 capex of about $50.9B. The ratio range spans that secondary projection. This is not official company guidance, so the range is kept wide. | The H2 2026 capex projection in the p21 quote is usable as a central allocation constraint for the second half. | Official FY2026 capex guidance or quarterly disclosures implying H2 2026 capex outside the $79-94B range. |
| a3 | Q3 2026 share of H2 2026 capex | 0.47 | 0.43..0.52 | 0.3344..0.6687 (widened) | share | m2 (m2) | Q3 2026 consensus capex p20 divided by the p21 H2 2026 capex projection implies a Q3 share of roughly 0.44-0.52. Historical Q3 2025 capex p163 relative to the H2 2025 total implied by p94 less H1 2025 components p8-p9 is also close to 0.47. | Q3/Q4 2026 capex is split similarly to recent years and the p21 H2 projection is approximately right. | Evidence of a much more back-end-loaded H2 2026, with Q3 capex materially below 43% or above 52% of the H2 total. |
| a4 | Q3 2026 capex intensity uplift versus Q2 2026 | 1.28 | 1.18..1.38 | 0.9023..1.805 (widened) | factor | m3 (m3) | Q2 2026 capex intensity is p1 divided by p47. Applying Q3 revenue guidance p67 at its midpoint and Q3 consensus capex p20 implies a materially higher Q3 intensity, about 1.28 times the Q2 level. The uplift reflects the AI infrastructure ramp and back-end-loaded data-center/server spending discussed  | Q3 2026 revenue is near the $61-64B guidance range and capex intensity steps up from Q2 2026 as the consensus and H2 ramp imply. | Q3 2026 capex remaining near Q2 2026 intensity, or revenue landing far from guidance while capex is unchanged. |
| a5 | Q3 2026 YoY capex growth acceleration versus Q2 2026 | 1.16 | 1.05..1.3 | 1.045..1.306 (widened) | factor | m4 (m4) | p163 is the Q3 2025 company capex base, and p31 gives Q2 2026 YoY capex growth of 82% on a slightly narrower TIKR measure. Applying that Q2 growth rate to p163 would leave Q3 2026 well below the p20 consensus, so the consensus implies an acceleration factor of roughly 1.16. The range covers measurem | Q3 2026 YoY capex growth continues above the Q2 2026 rate and p31 is a usable proxy for the company's underlying capex growth entering Q3. | Q3 2026 capex indicating no acceleration, or a deceleration, relative to the Q2 2026 YoY growth rate. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 41,507,585,407 | ['p20'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 40,692,945,600 | ['p21'] / ['a2', 'a3'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 40,699,805,600 | ['p67', 'p1', 'p47'] / ['a4'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 41,306,582,834 | ['p163', 'p31'] / ['a5'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **41,050,131,283** USD, 80% interval [24,344,552,315, 69,219,316,771] USD, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['us']; measure stems ['capit', 'expen', 'usd']


## Final answer

Best estimate for Meta Platforms' capital expenditures, including principal payments on finance leases, for Q3 2026 (quarter ended 2026-[n]-[n]), consolidated worldwide: 41,050,131,283 USD (80% model-based interval 24,344,552,315 to 69,219,316,771 USD; too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

Evidence: the consensus anchor 40,970,000,000 USD; H1 2026 capex 50,900,000,000 USD split into H2 via assumptions a2/a3; revenue-intensity route using Q3 revenue guidance 62,500,000,000 USD, Q2 capex 31,080,000,000 USD and Q2 revenue 60,801,000,000 USD with uplift a4; and YoY route from Q3 2025 capex 19,370,000,000 USD and Q2 2026 growth 82% with acceleration a5. Observed points are the anchors; the ratios and uplifts (a1-a5) are analyst assumptions, not observations. Code weighted the four routes equally (25% each) without backtest calibration.

Main risk: the consensus and H2 projection share a source and may not match Meta's including-finance-lease definition, and the implied Q3 intensity step-up is large. Official H2 2026 capex guidance and the finance-lease component would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Consensus-to-company-capex-measure adjustment: 1.01 dimensionless, range 0.7139 to 1.428 (range widened by code); used by m1. Overturned by: Evidence that the consensus excludes or includes a materially different item, such as large accrued capex, acquisitions, or finance leases far outside the stated adjustment range.
- a2 H2 2026 capex divided by H1 2026 capex: 1.7 ratio, range 1.197 to 2.395 (range widened by code); used by m2. Overturned by: Official FY[n] capex guidance or quarterly disclosures implying H2 2026 capex outside the $[n]-[n]B range.
- a3 Q3 2026 share of H2 2026 capex: 0.47 share, range 0.3344 to 0.6687 (range widened by code); used by m2. Overturned by: Evidence of a much more back-end-loaded H2 2026, with Q3 capex materially below [n] or above [n] of the H2 total.
- a4 Q3 2026 capex intensity uplift versus Q2 2026: 1.28 factor, range 0.9023 to 1.805 (range widened by code); used by m3. Overturned by: Q3 2026 capex remaining near Q2 2026 intensity, or revenue landing far from guidance while capex is unchanged.
- a5 Q3 2026 YoY capex growth acceleration versus Q2 2026: 1.16 factor, range 1.045 to 1.306 (range widened by code); used by m4. Overturned by: Q3 2026 capex indicating no acceleration, or a deceleration, relative to the Q2 2026 YoY growth rate.

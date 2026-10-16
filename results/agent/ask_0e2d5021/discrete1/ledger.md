# Evidence ledger: ask_0e2d5021

- Question: What will the upper bound of the US federal funds target range be, in percent, after the next FOMC meeting following today (the decision announced at the end of that meeting)?
- as_of: 2026-10-15
- Pinned target: Upper bound of the US federal funds target range after the next FOMC meeting following 2026-10-15 | unit percent | period 2026-10-16..2026-12-31 | publisher Federal Open Market Committee (FOMC), Board of Governors of the Federal Reserve System

## Directions and pages

### d1 [own_history] FOMC policy history

Hypothesis: The current target range and recent changes are the starting point. The next decision will be a change from the current level. Historical policy inertia suggests the most likely outcome is no change or a small change, but the direction depends on economic conditions.

Queries issued by the searcher: FOMC meeting calendar 2026; federal funds target range October 2026

- `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` -> **snapshot** (snapshot 20261012041551); points raw/verified 0/0
- `https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm` -> **snapshot** (snapshot 20261014061727); points raw/verified 9/6
  - p1 Upper bound of the federal funds target range effective September 17, 2026 = **4** percent (2026-09-17..2026-09-17) [keep: ] quote: "Undertake open market operations as necessary to maintain the federal funds rate in a target range of 3-3/4 to 4 percent."
  - p2 Interest rate paid on reserve balances effective September 17, 2026 = **3.9** percent (2026-09-17..2026-09-17) [keep: ] quote: "The Board of Governors of the Federal Reserve System voted unanimously to raise the interest rate paid on reserve balances to 3.90 percent, effective September 17, 2026."
  - p3 Primary credit rate effective September 17, 2026 = **4** percent (2026-09-17..2026-09-17) [keep: ] quote: "voted unanimously to approve a 1/4 percentage point increase in the primary credit rate to 4.0 percent, effective September 17, 2026."
  - p4 Standing overnight repurchase agreement operation rate effective September 17, 2 = **4** percent (2026-09-17..2026-09-17) [keep: ] quote: "Conduct standing overnight repurchase agreement operations at a rate of 4.0 percent."
  - p5 Standing overnight reverse repurchase agreement offering rate effective Septembe = **3.75** percent (2026-09-17..2026-09-17) [keep: ] quote: "Conduct standing overnight reverse repurchase agreement operations at an offering rate of 3.75 percent and with a per-counterparty limit of $160 billion per day."
  - p6 Per-counterparty daily limit for standing overnight reverse repurchase agreement = **160,000,000,000** US dollars per day (2026-09-17..2026-09-17) [DISCARD: Per-counterparty reverse repo limit is an operational parameter, not evidence about the target rate.] quote: "Conduct standing overnight reverse repurchase agreement operations at an offering rate of 3.75 percent and with a per-counterparty limit of $160 billion per day."
- `https://www.federalreserve.gov/default.htm` -> **snapshot** (snapshot 20261015101922); points raw/verified 0/0
- `https://admiralmarkets.com/analytics/traders-blog/fed-rate-decision-october-2026` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 3 (number: more than one number in value_as_written: 2; period_end missing or unparseable: 1)

### d2 [forecasts_markets] Financial market participants

Hypothesis: Fed funds futures and options prices reflect market expectations of the target rate after the next FOMC meeting. The implied probability distribution can be used to estimate the most likely upper bound.

Queries issued by the searcher: CME FedWatch next FOMC meeting implied probability target rate range; fed funds futures implied probability October 2026 FOMC; Kalshi Fed decision market interest rate; FOMC meeting dates 2026 schedule October December

- `https://en.infomaxai.com/news/articleView.html?idxno=143360` -> **live_dated** (page date 2026-10-15); points raw/verified 13/0
- `https://seekingalpha.com/news/4652903-october-rate-hike-probability-pops-to-49-now-a-coin-flip-chance-after-cpi-data` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-
- `https://www.talos.com/insights/fed-odds-defi-yields-and-ethereums-glamsterdam-upgrade` -> **live_dated** (page date 2026-10-13); points raw/verified 15/3
  - p7 Kalshi Fed decision markets volume growth multiple from April to September = **7.3** multiple (2026-04-01..2026-09-30) [DISCARD: Kalshi volume growth multiple is irrelevant to the level of the target rate.] quote: "Volume in Kalshi's Fed decision markets grew 7.3x from April to September."
  - p8 September Fed rate hike size = **25** basis points (2026-09-01..2026-09-30) [keep: ] quote: "the Fed raised rates in September by 25 bps, the first rate hike since July 2023."
  - p9 DeFi rates increase 12 days after September 17 Fed announcement = **12** basis points (2026-09-17..2026-09-29) [DISCARD: DeFi rate response is unrelated to the FOMC target decision.] quote: "12 days after the Fed announcement on September 17 to raise interest rates by 25 bps, select DeFi rates only increased by at most 12 bps"
- `https://www.barrons.com/livecoverage/stock-market-news-today-101526/card/after-hot-ppi-an-october-rate-hike-still-seen-as-less-likely-L08y5ueHByZvCdjg` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 25 (period_end missing or unparseable: 11; period year 2025 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-10-31 after as_of: 1; scale word 'thousand' not supported by quote or table header: 2; scale word 'million' not supported by quote or table header: 3; value_as_written not in quote as a whole number: 1; scale word 'billion' not supported by quote or table header: 1)

### d3 [related_series] Macroeconomic data watchers

Hypothesis: The FOMC reacts to inflation and employment data. Recent CPI, PCE, and unemployment reports before the next meeting will influence the decision. A deterioration in inflation or employment could prompt a cut; strong data could prompt a hold or hike.

Queries issued by the searcher: FOMC meeting schedule 2026 October December; US CPI September 2026 inflation rate; US unemployment rate September 2026 jobs report; core PCE inflation August 2026; FOMC September 2026 statement federal funds rate decision

- `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` -> **snapshot** (snapshot 20261012041551); points raw/verified 0/0
- `https://economics.td.com/us-cpi` -> **snapshot** (snapshot 20260930084847); points raw/verified 15/14
  - p10 US CPI month-on-month change, August 2026 = **0.4** percent (2026-08-01..2026-08-31) [keep: ] quote: "The Consumer Price Index (CPI) rose by 0.4% month-on-month (m/m) in August, meeting the Bloomberg consensus."
  - p11 US CPI twelve-month change, August 2026 = **3.4** percent (2026-08-01..2026-08-31) [keep: ] quote: "On a twelve-month basis, CPI held at 3.4%."
  - p12 US energy costs month-on-month change, August 2026 = **2.1** percent (2026-08-01..2026-08-31) [DISCARD: Energy cost detail is subsumed by headline and core CPI; no separate role.] quote: "Energy costs rose by 2.1% m/m, led by a 3.9% m/m gain in gasoline prices."
  - p13 US gasoline prices month-on-month change, August 2026 = **3.9** percent (2026-08-01..2026-08-31) [DISCARD: Gasoline price detail is subsumed by energy/headline CPI.] quote: "Energy costs rose by 2.1% m/m, led by a 3.9% m/m gain in gasoline prices."
  - p14 US food prices month-on-month change, August 2026 = **0.1** percent (2026-08-01..2026-08-31) [DISCARD: Food price m/m detail is subsumed by headline CPI.] quote: "Food prices rose by a subdued 0.1% m/m for a second consecutive month and are up 2.7% over the last year."
  - p15 US food prices twelve-month change, August 2026 = **2.7** percent (2026-08-01..2026-08-31) [DISCARD: Food price y/y detail is subsumed by headline CPI.] quote: "Food prices rose by a subdued 0.1% m/m for a second consecutive month and are up 2.7% over the last year."
  - p16 US core CPI month-on-month change, August 2026 = **0.3** percent (2026-08-01..2026-08-31) [DISCARD: August core CPI m/m is superseded by the September core CPI reading (p151) for the next-meeting decision.] quote: "Excluding food and energy, core prices rose 0.3% m/m, a tick hotter than expectations."
  - p17 US core CPI twelve-month change, August 2026 = **2.4** percent (2026-08-01..2026-08-31) [DISCARD: August core CPI y/y is superseded by September core CPI (p152).] quote: "On a twelve-month basis, price growth edged down to 2.4%, while the three-month annualized sits at a slightly softer 2.0%."
  - p18 US core CPI three-month annualized rate, August 2026 = **2** percent (2026-08-01..2026-08-31) [DISCARD: August 3-month annualized core CPI is a redundant summary of the same August release.] quote: "On a twelve-month basis, price growth edged down to 2.4%, while the three-month annualized sits at a slightly softer 2.0%."
  - p19 US core services prices month-on-month change, August 2026 = **0.3** percent (2026-08-01..2026-08-31) [DISCARD: Core services detail is subsumed by core CPI.] quote: "Price growth for core services rose 0.3% m/m, a modest acceleration from the month prior."
  - p20 US non-housing services prices month-on-month change, August 2026 = **0.6** percent (2026-08-01..2026-08-31) [DISCARD: Non-housing services detail is subsumed by core CPI.] quote: "The rebound was driven by a sharp acceleration in non-housing services (+0.6% m/m vs. +0.2% m/m in July), while primary shelter costs (+0.2% m/m) were a touch softer."
  - p21 US non-housing services prices month-on-month change, July 2026 = **0.2** percent (2026-07-01..2026-07-31) [DISCARD: July non-housing services detail is subsumed by core CPI.] quote: "The rebound was driven by a sharp acceleration in non-housing services (+0.6% m/m vs. +0.2% m/m in July), while primary shelter costs (+0.2% m/m) were a touch softer."
  - p22 US primary shelter costs month-on-month change, August 2026 = **0.2** percent (2026-08-01..2026-08-31) [DISCARD: Shelter cost detail is subsumed by core CPI.] quote: "while primary shelter costs (+0.2% m/m) were a touch softer."
  - p23 US wireless phone services prices month-on-month change, August 2026 = **5.9** percent (2026-08-01..2026-08-31) [DISCARD: Wireless phone services detail is subsumed by core CPI.] quote: "notable price increases in airfares (+2.7% m/m), hotels (+2.4%), vehicle maintenance costs (+0.6% m/m) and a sharp increase in wireless phone services (+5.9% m/m)."
- `https://www.stlouisfed.org/on-the-economy/2026/oct/flash-report-unemployment-rises-slightly-job-growth-slows-september` -> **snapshot** (snapshot 20261008012446); points raw/verified 15/12
  - p24 US unemployment rate, September 2026, headline = **4.2** percent (2026-09-01..2026-09-30) [keep: ] quote: "The U.S. unemployment rate rose from 4.1% in August to 4.2% in September, a value similar to its 12-month average."
  - p25 US unemployment rate, August 2026, headline = **4.1** percent (2026-08-01..2026-08-31) [DISCARD: August unemployment rate is redundant with p24/p36 which give the September level and the change.] quote: "The U.S. unemployment rate rose from 4.1% in August to 4.2% in September, a value similar to its 12-month average."
  - p26 US unemployment rate, September 2026, precise (unrounded) = **4.175** percent (2026-09-01..2026-09-30) [DISCARD: Precise unrounded September unemployment rate is redundant with p24/p36.] quote: "September 2026 4.175% Precise Rate"
  - p27 US unemployment rate, August 2026, precise (unrounded) = **4.141** percent (2026-08-01..2026-08-31) [DISCARD: Precise unrounded August unemployment rate is redundant with p25.] quote: "More precise data show the rate increased slightly from 4.141% to 4.175%."
  - p28 US unemployment rate, September 2026, precise (four decimals) = **4.175** percent (2026-09-01..2026-09-30) [DISCARD: Four-decimal September unemployment rate is redundant with p24/p36.] quote: "for example, the unemployment rates were 4.1754% in September and 4.1413% in August."
  - p29 US unemployment rate, August 2026, precise (four decimals) = **4.141** percent (2026-08-01..2026-08-31) [DISCARD: Four-decimal August unemployment rate is redundant with p25.] quote: "for example, the unemployment rates were 4.1754% in September and 4.1413% in August."
  - p30 US nonfarm payroll growth, September 2026 = **29,000** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Nonfarm payroll growth slowed in September to 29,000 jobs - less than half as many as forecasts expected."
  - p31 Combined downward revision to August and July 2026 nonfarm payroll gains = **60,000** jobs (2026-07-01..2026-08-31) [DISCARD: Combined revision is redundant with p50 and p32.] quote: "payroll gains in August and July were revised downward by a combined 60,000 jobs - or 30,000 each month, on average."
  - p32 Average monthly downward revision to nonfarm payroll gains, July and August 2026 = **30,000** jobs (2026-07-01..2026-08-31) [DISCARD: Average monthly revision is redundant with p50.] quote: "payroll gains in August and July were revised downward by a combined 60,000 jobs - or 30,000 each month, on average."
  - p33 US labor force participation rate, September 2026 = **61.8** percent (2026-09-01..2026-09-30) [DISCARD: Labor force participation is redundant with p44.] quote: "The labor force participation rate rose 0.2 percentage points to 61.8%"
  - p34 US employment-to-population ratio, September 2026 = **59.2** percent (2026-09-01..2026-09-30) [DISCARD: Employment-population ratio is redundant with p45.] quote: "the employment-to-population ratio rose 0.1 percentage points to 59.2%."
  - p35 Contribution of people losing or leaving jobs and becoming unemployed to Septemb = **0.85** percentage points (2026-09-01..2026-09-30) [DISCARD: Unemployment flow decomposition is not needed for the target level.] quote: "\| September 2026 \| +0.03 \| +0.85 \| -1.09 \| +1.11 \| -0.82 \|"
- `https://www.bls.gov/news.release/empsit.nr0.htm` -> **snapshot** (snapshot 20261012062422); points raw/verified 15/15
  - p36 US unemployment rate, September 2026 = **4.2** percent (2026-09-01..2026-09-30) [keep: ] quote: "Both nonfarm payroll employment (+29,000) and the unemployment rate (4.2 percent) changed little in September"
  - p37 US number of unemployed people, September 2026 = **7,100,000** people (2026-09-01..2026-09-30) [DISCARD: Number of unemployed is redundant with the unemployment rate.] quote: "the number of unemployed people, at 7.1 million, changed little in September"
  - p38 Lower bound of US unemployment rate narrow range since March 2026 = **4.1** percent (2026-03-01..2026-09-30) [DISCARD: Lower bound of unemployment range is redundant with p39.] quote: "The unemployment rate has remained in a narrow range of 4.1 percent to 4.3 percent since March."
  - p39 Upper bound of US unemployment rate narrow range since March 2026 = **4.3** percent (2026-03-01..2026-09-30) [DISCARD: Upper bound of unemployment range is contextual but not needed for the target level.] quote: "The unemployment rate has remained in a narrow range of 4.1 percent to 4.3 percent since March."
  - p40 US total nonfarm payroll employment change, September 2026 = **29,000** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Total nonfarm payroll employment changed little in September (+29,000), following an average monthly gain of 45,000 over the prior 12 months."
  - p41 US average monthly nonfarm payroll gain over prior 12 months, as of September 20 = **45,000** jobs per month (2025-10-01..2026-09-30) [DISCARD: 12-month average payroll gain is redundant with p40.] quote: "following an average monthly gain of 45,000 over the prior 12 months"
  - p42 US average hourly earnings, all employees on private nonfarm payrolls, September = **37.81** US dollars per hour (2026-09-01..2026-09-30) [DISCARD: Average hourly earnings level is redundant with p43/p160.] quote: "average hourly earnings for all employees on private nonfarm payrolls edged up by 5 cents, or 0.1 percent, to $37.81"
  - p43 US average hourly earnings 12-month percent increase, September 2026 = **3** percent (2025-10-01..2026-09-30) [DISCARD: Average hourly earnings y/y is redundant with p160.] quote: "Over the past 12 months, average hourly earnings have increased by 3.0 percent."
  - p44 US labor force participation rate, September 2026 = **61.8** percent (2026-09-01..2026-09-30) [keep: ] quote: "Both the labor force participation rate, at 61.8 percent, and the employment-population ratio, at 59.2 percent, changed little in September."
  - p45 US employment-population ratio, September 2026 = **59.2** percent (2026-09-01..2026-09-30) [keep: ] quote: "Both the labor force participation rate, at 61.8 percent, and the employment-population ratio, at 59.2 percent, changed little in September."
  - p46 US long-term unemployed (27 weeks or more), September 2026 = **1,900,000** people (2026-09-01..2026-09-30) [DISCARD: Long-term unemployed count is not needed for the target level.] quote: "The number of long-term unemployed (those jobless for 27 weeks or more) was essentially unchanged at 1.9 million in September."
  - p47 US long-term unemployed share of all unemployed, September 2026 = **27.1** percent (2026-09-01..2026-09-30) [DISCARD: Long-term unemployed share is not needed for the target level.] quote: "The long-term unemployed accounted for 27.1 percent of all unemployed people."
  - p48 US nonfarm payroll employment change for July 2026, revised = **-10,000** jobs (2026-07-01..2026-07-31) [DISCARD: July payroll revision is redundant with p50.] quote: "The change in total nonfarm payroll employment for July was revised down by 31,000, from +21,000 to -10,000"
  - p49 US nonfarm payroll employment change for August 2026, revised = **133,000** jobs (2026-08-01..2026-08-31) [DISCARD: August payroll revision is redundant with p50.] quote: "the change for August was revised down by 29,000, from +162,000 to +133,000"
  - p50 US combined downward revision to July and August 2026 nonfarm payroll employment = **60,000** jobs (2026-07-01..2026-08-31) [keep: ] quote: "With these revisions, employment in July and August combined is 60,000 lower than previously reported."
- dropped by code checks: 4 (period_end missing or unparseable: 3; value_as_written not in quote as a whole number: 1)

### d4 [attention] Media and analyst commentary

Hypothesis: News articles and analyst notes often summarize the consensus expectation for the next FOMC meeting. The consensus view can be a strong predictor of the actual decision.

Queries issued by the searcher: FOMC meeting October 2026 rate decision expectations; Fed meeting November 2026 rate cut odds; Reuters Fed expected hold October 28 2026 meeting December hike; "October" FOMC 2026 consensus hold rates analysts forecast upper bound 4.00%

- `https://www.cnbctv18.com/world/us-fed-officials-signal-october-hike-is-unlikely-as-markets-cut-bets-20003488.htm/amp` -> **snapshot** (snapshot 20261006183956); points raw/verified 0/0
- `https://finance-commerce.com/2026/10/fed-rate-hike-october-jobs-report/` -> **snapshot** (snapshot 20261009022553); points raw/verified 11/5
  - p51 US September nonfarm payroll job gains = **29,000** jobs (2026-09-01..2026-09-30) [keep: ] quote: "U.S. employers added just 29,000 jobs in September, well below economists' expectations of 90,000."
  - p52 Economists' expected US September nonfarm payroll job gains = **90,000** jobs (2026-09-01..2026-09-30) [keep: ] quote: "U.S. employers added just 29,000 jobs in September, well below economists' expectations of 90,000."
  - p53 US September unemployment rate = **4.2** % (2026-09-01..2026-09-30) [keep: ] quote: "The September unemployment rate was 4.2%, up from 4.1%."
  - p54 US August unemployment rate = **4.1** % (2026-08-01..2026-08-31) [DISCARD: August unemployment rate is redundant with p25/p24.] quote: "The September unemployment rate was 4.2%, up from 4.1%."
  - p55 Fed's targeted inflation measure in August = **3.4** % (2026-08-01..2026-08-31) [keep: ] quote: "Inflation by the Fed's targeted measure was 3.4% in August, data showed this week - far above the 2% goal though not as bad as economists had projected."
- `https://ovs.entrust.com.tw/entrustOverseas/announcement/nowInner.do?id=6631554` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.marketscreener.com/news/take-a-step-back-to-jump-further-ce785dd3da80f624` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 6 (number: no number in value_as_written: 2; period_end missing or unparseable: 4)

### d5 [administrative] Federal Reserve communications

Hypothesis: The FOMC's own communications (statements, minutes, speeches) provide guidance on the likely path of policy. The dot plot from the most recent meeting may indicate the expected rate by year-end.

Queries issued by the searcher: FOMC statement September 2026; FOMC dot plot 2026 median federal funds rate year-end; Fed speeches October 2026 rate hike odds next FOMC meeting October 27-28; FOMC Summary of Economic Projections September 2026 median federal funds rate 4.125

- `https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm` -> **snapshot** (snapshot 20261014061702); points raw/verified 6/3
  - p56 FOMC target range for the federal funds rate, upper bound, after September 16, 2 = **4** percent (2026-09-16..2026-09-16) [keep: ] quote: "raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4 percent"
  - p57 FOMC vote in favor of the September 16, 2026 statement = **12** votes (2026-09-16..2026-09-16) [DISCARD: Vote in favor is redundant with p112.] quote: "approved the following statement for release by a 12 - 0 vote"
  - p58 FOMC vote against the September 16, 2026 statement = **0** votes (2026-09-16..2026-09-16) [DISCARD: Vote against is redundant with p113.] quote: "approved the following statement for release by a 12 - 0 vote"
- `https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm` -> **snapshot** (snapshot 20261014061809); points raw/verified 15/11
  - p59 FOMC target range for the federal funds rate after September 2026 meeting, upper = **4** percent (2026-09-16..2026-09-16) [keep: ] quote: "all participants supported raising the target range for the federal funds rate 1/4 percentage point to 3-3/4 to 4 percent."
  - p60 Market-implied probability of a 25 basis point increase in the target range at t = **25** basis points (2026-09-15..2026-09-16) [keep: ] quote: "investors placed high odds on a 25 basis point increase in the target range for the federal funds rate at the September meeting."
  - p61 Desk survey-implied probability of at least 25 basis points of policy firming by = **25** basis points (2026-09-15..2026-09-16) [keep: ] quote: "a considerable probability was placed on at least 25 basis points of policy firming by the end of the year."
  - p62 Staff estimate of 12-month total PCE price inflation in August 2026 = **3.8** percent (2026-08-01..2026-08-31) [keep: ] quote: "the staff estimated that price inflation-as measured by the 12-month change in the price index for total personal consumption expenditures (PCE)-edged up to 3.8 percent in August"
  - p63 Staff estimate of 12-month core PCE price inflation in August 2026 = **3.4** percent (2026-08-01..2026-08-31) [keep: ] quote: "Core PCE price inflation, which excludes changes in consumer energy prices and many consumer food prices, was estimated to have remained at 3.4 percent in August."
  - p64 Staff estimate of total PCE inflation in August 2026 under new BEA methodology = **3.6** percent (2026-08-01..2026-08-31) [DISCARD: New-methodology total PCE is redundant with p62/p70.] quote: "Under the new methodology that the Bureau of Economic Analysis (BEA) had announced would be implemented at the end of September, the staff estimated that total inflation would be 3.6 percent in August"
  - p65 Staff estimate of core PCE inflation in August 2026 under new BEA methodology = **3.2** percent (2026-08-01..2026-08-31) [DISCARD: New-methodology core PCE is redundant with p63/p72.] quote: "with core inflation at 3.2 percent."
  - p66 Unemployment rate in July and August 2026 = **4.1** percent (2026-07-01..2026-08-31) [DISCARD: July/August unemployment rate is redundant with p24/p25.] quote: "The unemployment rate moved down to 4.1 percent in July and August, 0.3 percentage point lower than its average in the second half of last year."
  - p67 12-month change in employment cost index for private-sector workers through June = **3.3** percent (2025-07-01..2026-06-30) [DISCARD: Employment cost index is contextual but not needed for the target level.] quote: "The 12-month change in the employment cost index for private-sector workers was 3.3 percent through June"
  - p68 Average hourly earnings increase over 12 months ending August 2026 = **3.1** percent (2025-09-01..2026-08-31) [DISCARD: Average hourly earnings through August is redundant with p43/p160.] quote: "average hourly earnings increased 3.1 percent over the 12 months ending in August."
  - p69 Number of FOMC participants submitting projections at September 2026 meeting = **18** participants (2026-09-15..2026-09-16) [DISCARD: Number of SEP participants is not needed for the target level.] quote: "18 participants submitted projections of the most likely outcomes for real GDP growth, the unemployment rate, and inflation."
- `https://investinglive.com/central-banks/fed-dot-plot-signals-another-2026-rate-hike-as-growth-strengthens-and-inflation-remains-elevated/` -> **snapshot** (snapshot 20260917105506); points raw/verified 15/0
- `https://forex.cfi.cn/p20261014000082.html` -> **live_dated** (page date 2023-07-18); points raw/verified 14/6
  - p70 US PCE inflation rate, August (Fed's preferred inflation gauge) = **3.4** percent (2026-08-01..2026-08-31) [keep: ] quote: "美国8月PCE通胀率--美联储首选的通胀指标--降至3.4%,低于预期的3.7%。"
  - p71 Expected US PCE inflation rate, August (consensus expectation) = **3.7** percent (2026-08-01..2026-08-31) [DISCARD: Consensus PCE expectation is redundant with p70.] quote: "美国8月PCE通胀率--美联储首选的通胀指标--降至3.4%,低于预期的3.7%。"
  - p72 US core PCE inflation rate (excluding food and energy), August = **3** percent (2026-08-01..2026-08-31) [keep: ] quote: "剔除食品和能源成本的核心PCE通胀率降至3.0%,低于预期的3.3%"
  - p73 Expected US core PCE inflation rate (excluding food and energy), August (consens = **3.3** percent (2026-08-01..2026-08-31) [DISCARD: Consensus core PCE expectation is redundant with p72.] quote: "剔除食品和能源成本的核心PCE通胀率降至3.0%,低于预期的3.3%"
  - p74 Probability that the federal overnight rate at end-2027 will be at least 50 basi = **90** percent (2026-10-13..2026-10-13) [keep: ] quote: "最新交易定价显示,2027年末联邦隔夜利率较当前水平上调至少50个基点的概率约90%。"
  - p75 Year of the Fed's first rate hike since 2023 (September) = **2,023** year (2023-01-01..2023-12-31) [DISCARD: Year of first hike is redundant with p8/p110.] quote: "美联储9月进行了自2023年以来的首次加息。"
- dropped by code checks: 30 (number: more than one number in value_as_written: 4; period_end missing or unparseable: 8; period_end 2029-12-31 after as_of: 2; period_end 2026-12-31 after as_of: 6; period_end 2027-12-31 after as_of: 4; period_end 2028-12-31 after as_of: 2; period_end 2026-10-28 after as_of: 2; value_as_written not in quote as a whole number: 2)

### d6 [base_rates] Historical FOMC behavior

Hypothesis: Historically, the FOMC changes the target rate in discrete increments of 25 basis points, and often holds steady when uncertainty is high. The base rate of no change at a given meeting is high, but this depends on the economic cycle.

Queries issued by the searcher: FOMC historical decisions frequency how often target rate unchanged raised lowered; FOMC meeting decisions history 2020s rate holds versus changes statistics; FOMC September 2026 meeting decision rate hike hold 3.50-3.75; FOMC 2026 meeting schedule October November December dates

- `https://fredblog.stlouisfed.org/2020/04/unexpected-changes-to-the-benchmark-u-s-interest-rate/` -> **snapshot** (snapshot 20260830110622); points raw/verified 14/12
  - p76 Increases in federal funds target rate, June 2004 to August 2006 = **17** increases (2004-06-01..2006-08-31) [DISCARD: Count of 2004–06 increases is redundant with p77/p101.] quote: "we've zoomed in to the months between June 2004 and August 2006, showing 17 increases in the target rate"
  - p77 Size of each federal funds target rate change, June 2004 to August 2006 = **0.25** % (2004-06-01..2006-08-31) [keep: ] quote: "All the changes in the target rate were of the same size: 0.25% (or 25 basis points)."
  - p78 Decreases in federal funds target rate, August 2007 to July 2009 = **10** decreases (2007-08-01..2009-07-31) [DISCARD: Count of 2007–09 decreases is redundant with p89/p92.] quote: "look at the months between August 2007 and July 2009. You can see 10 decreases in the target rate"
  - p79 Decreases in federal funds target rate announced at regular FOMC meetings, Augus = **8** decreases (2007-08-01..2009-07-31) [DISCARD: Scheduled vs unscheduled decrease split is redundant with p80/p93.] quote: "8 were announced at the regular FOMC meetings and 2 were in between meetings"
  - p80 Decreases in federal funds target rate announced between meetings, August 2007 t = **2** decreases (2007-08-01..2009-07-31) [DISCARD: Between-meeting decreases are redundant with p93.] quote: "8 were announced at the regular FOMC meetings and 2 were in between meetings (January 22 and October 8, 2008)"
  - p81 Lower bound of size of federal funds target rate changes, August 2007 to July 20 = **0.25** % (2007-08-01..2009-07-31) [keep: ] quote: "The changes in the target rate were of different sizes, ranging from 0.25% to 0.75% (or 25 to 75 basis points)."
  - p82 Upper bound of size of federal funds target rate changes, August 2007 to July 20 = **0.75** % (2007-08-01..2009-07-31) [keep: ] quote: "The changes in the target rate were of different sizes, ranging from 0.25% to 0.75% (or 25 to 75 basis points)."
  - p83 FOMC meetings held over the past 20 years = **184** meetings (..) [DISCARD: Meeting count is context; not a direct driver.] quote: "Over the past 20 years, the FOMC has held 184 meetings, 30 of which were unscheduled."
  - p84 Unscheduled FOMC meetings over the past 20 years = **30** meetings (..) [DISCARD: Unscheduled meeting count is context; not a direct driver.] quote: "Over the past 20 years, the FOMC has held 184 meetings, 30 of which were unscheduled."
  - p85 Changes in FOMC monetary policy target over the past 20 years = **54** changes (..) [DISCARD: Change count is context; p88-p92 give a longer and more recent sample.] quote: "During the same period, the FOMC changed its monetary policy target 54 times, 7 of which occurred after unscheduled meetings"
  - p86 Changes in FOMC monetary policy target after unscheduled meetings over the past  = **7** changes (..) [DISCARD: Subset of p85; redundant.] quote: "the FOMC changed its monetary policy target 54 times, 7 of which occurred after unscheduled meetings"
  - p87 Share of all FOMC policy target changes occurring after unscheduled meetings ove = **13** % (..) [DISCARD: Share of changes after unscheduled meetings is context; not a direct driver.] quote: "7 of which occurred after unscheduled meetings, which amounts to 13% of all policy target changes"
- `https://eco3min.fr/en/every-fomc-rate-decision-since-1990/` -> **live_dated** (page date 2026-10-06); points raw/verified 15/15
  - p88 Total FOMC rate decisions from February 1990 to September 2026 = **316** decisions (1990-02-01..2026-09-30) [DISCARD: Total decisions count is redundant with p89/p90.] quote: "Since February 1990 the Federal Open Market Committee has taken 316 rate decisions: 293 scheduled meetings plus 23 changes made outside them."
  - p89 FOMC target rate changes from February 1990 to September 2026 = **110** changes (1990-02-01..2026-09-30) [keep: ] quote: "316 decisions from February 1990 to September 2026: 110 changes of the target (52 hikes, 58 cuts) and 206 holds."
  - p90 FOMC target rate holds from February 1990 to September 2026 = **206** holds (1990-02-01..2026-09-30) [keep: ] quote: "316 decisions from February 1990 to September 2026: 110 changes of the target (52 hikes, 58 cuts) and 206 holds."
  - p91 FOMC target rate hikes from February 1990 to September 2026 = **52** hikes (1990-02-01..2026-09-30) [keep: ] quote: "316 decisions from February 1990 to September 2026: 110 changes of the target (52 hikes, 58 cuts) and 206 holds."
  - p92 FOMC target rate cuts from February 1990 to September 2026 = **58** cuts (1990-02-01..2026-09-30) [keep: ] quote: "316 decisions from February 1990 to September 2026: 110 changes of the target (52 hikes, 58 cuts) and 206 holds."
  - p93 FOMC target rate changes made outside a scheduled meeting from February 1990 to  = **23** changes (1990-02-01..2026-09-30) [DISCARD: Outside-meeting changes are context; not a direct driver.] quote: "23 of the changes were made outside a scheduled meeting, and 18 of them were never announced, before the first statement of February 1994."
  - p94 FOMC target rate changes made outside a scheduled meeting and never announced be = **18** changes (1990-02-01..1994-02-28) [DISCARD: Pre-1994 unannounced changes are not relevant to the current transparent regime.] quote: "23 of the changes were made outside a scheduled meeting, and 18 of them were never announced, before the first statement of February 1994."
  - p95 FOMC recorded votes with at least one dissent from February 1990 to September 20 = **111** votes (1990-02-01..2026-09-30) [DISCARD: Dissent count is redundant with p96/p97–p100.] quote: "111 of the 292 recorded votes had at least one dissent."
  - p96 FOMC recorded votes from February 1990 to September 2026 = **292** votes (1990-02-01..2026-09-30) [DISCARD: Recorded vote count is redundant with p95/p97–p100.] quote: "111 of the 292 recorded votes had at least one dissent."
  - p97 Share of FOMC recorded votes with at least one dissent under Ben Bernanke = **62** % (..) [DISCARD: Dissent share under Bernanke is not needed for the target level.] quote: "Under Ben Bernanke the share was 62%, under Alan Greenspan 24%, under Janet Yellen 47%, under Jerome Powell 27%."
  - p98 Share of FOMC recorded votes with at least one dissent under Alan Greenspan = **24** % (..) [DISCARD: Dissent share under Greenspan is not needed for the target level.] quote: "Under Ben Bernanke the share was 62%, under Alan Greenspan 24%, under Janet Yellen 47%, under Jerome Powell 27%."
  - p99 Share of FOMC recorded votes with at least one dissent under Janet Yellen = **47** % (..) [DISCARD: Dissent share under Yellen is not needed for the target level.] quote: "Under Ben Bernanke the share was 62%, under Alan Greenspan 24%, under Janet Yellen 47%, under Jerome Powell 27%."
  - p100 Share of FOMC recorded votes with at least one dissent under Jerome Powell = **27** % (..) [DISCARD: Dissent share under Powell is not needed for the target level.] quote: "Under Ben Bernanke the share was 62%, under Alan Greenspan 24%, under Janet Yellen 47%, under Jerome Powell 27%."
  - p101 FOMC moves of 25 basis points out of 110 target changes from February 1990 to Se = **77** moves (1990-02-01..2026-09-30) [keep: ] quote: "The 25 basis point step is the norm, 77 moves out of 110; the 24 steps of 50 and the 8 of 75 cluster in 1991-95, 2000-02, 2007-08, 2020, 2022 and September 2024"
  - p102 FOMC moves of 50 basis points out of 110 target changes from February 1990 to Se = **24** moves (1990-02-01..2026-09-30) [keep: ] quote: "The 25 basis point step is the norm, 77 moves out of 110; the 24 steps of 50 and the 8 of 75 cluster in 1991-95, 2000-02, 2007-08, 2020, 2022 and September 2024"
- `https://am.jpmorgan.com/us/en/asset-management/adv/insights/portfolio-insights/fixed-income/fixed-income-perspectives/fomc-statement-september-2026/` -> **live_dated** (page date 2026-09-17); points raw/verified 15/4
  - p103 FOMC federal funds rate target range increase at the meeting, in basis points = **25** basis points (..) [keep: ] quote: "The Federal Open Market Committee (FOMC) unanimously voted to increase the federal funds rate target range by 25 basis points (bps) to 3.75%-4.00%."
  - p104 Upper bound of the federal funds rate target range after the FOMC vote = **4** % (..) [keep: ] quote: "increase the federal funds rate target range by 25 basis points (bps) to 3.75%-4.00%."
  - p105 Lower bound of the federal funds rate target range after the FOMC vote = **3.75** % (..) [DISCARD: Lower bound is redundant with p104/p124.] quote: "increase the federal funds rate target range by 25 basis points (bps) to 3.75%-4.00%."
  - p106 Longer-run median FOMC participant projection for the fed funds rate = **3.2** % (..) [keep: ] quote: "The long run dot rose slightly to 3.2%."
- `https://investinglive.com/central-banks/fomc-rate-decision-fed-hikes-for-the-first-time-in-three-years/` -> **snapshot** (snapshot 20260917122635); points raw/verified 13/10
  - p107 FOMC target range upper bound after September 16, 2026 hike = **4** percent (2026-09-16..2026-09-16) [keep: ] quote: "raise the target range for the federal funds rate by 1/4 percentage pointto 3-3/4to 4 percent"
  - p108 FOMC target range prior to September 16, 2026 decision (upper bound) = **3.75** percent (..2026-09-16) [DISCARD: Prior upper bound is redundant with p109/p124.] quote: "Prior was 3.50%-3.75%"
  - p109 FOMC target range prior to September 16, 2026 decision (lower bound) = **3.5** percent (..2026-09-16) [DISCARD: Prior lower bound is redundant with p108/p124.] quote: "Prior was 3.50%-3.75%"
  - p110 Size of September 16, 2026 federal funds rate hike = **25** basis points (2026-09-16..2026-09-16) [keep: ] quote: "Rates hiked by 25 basis points, as expected"
  - p111 Market-implied probability of a rate hike at the September 16, 2026 meeting = **90** percent (2026-09-16..2026-09-16) [keep: ] quote: "The market was pricing in a 90% chance of a rate hike today"
  - p112 FOMC vote tally approving the September 16, 2026 statement = **12** votes in favor (2026-09-16..2026-09-16) [keep: ] quote: "approved the following statement for release by a 12 - 0 vote"
  - p113 FOMC votes against the September 16, 2026 statement = **0** votes against (2026-09-16..2026-09-16) [keep: ] quote: "approved the following statement for release by a 12 - 0 vote"
  - p114 Committee's longer-run inflation goal = **2** percent (..) [keep: ] quote: "support a timelier return to the Committee's 2 percent goal"
  - p115 Change in 10-year Treasury yield on September 16, 2026 = **4** basis points (2026-09-16..2026-09-16) [DISCARD: 10-year yield change on the decision day is not needed for the target level.] quote: "10s are down 4 bps and 30s down 5 bps"
  - p116 Change in 30-year Treasury yield on September 16, 2026 = **5** basis points (2026-09-16..2026-09-16) [DISCARD: 30-year yield change on the decision day is not needed for the target level.] quote: "10s are down 4 bps and 30s down 5 bps"
- dropped by code checks: 16 (number: no number in value_as_written: 5; value_as_written not in quote as a whole number: 1; period_end 2026-12-31 after as_of: 4; period_end 2027-12-31 after as_of: 3; period_end 2028-12-31 after as_of: 1; period_end 2029-12-31 after as_of: 1; number: more than one number in value_as_written: 1)

### d7 [shocks] Economic and geopolitical risk monitors

Hypothesis: Major shocks (e.g., financial crises, geopolitical events, pandemics) can force the FOMC to change rates unexpectedly. The absence or presence of such shocks before the next meeting could alter the decision.

Queries issued by the searcher: FOMC meeting schedule 2026 dates; federal funds target range October 2026 FOMC; VIX October 2026 financial market volatility; geopolitical risk October 2026 Iran war energy shock markets

- `https://www.investing.com/news/economic-indicators/exclusivefeds-daly-says-rate-hikes-likely-needed-but-not-urgently-4950157` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-
- `https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm` -> **snapshot** (snapshot 20261014061727); points raw/verified 9/6
  - p117 Federal funds target range upper bound after September 2026 FOMC decision = **4** percent (2026-09-17..2026-09-17) [keep: ] quote: "Undertake open market operations as necessary to maintain the federal funds rate in a target range of 3-3/4 to 4 percent."
  - p118 Interest rate paid on reserve balances effective September 17, 2026 = **3.9** percent (2026-09-17..2026-09-17) [DISCARD: IORB is redundant with p2.] quote: "The Board of Governors of the Federal Reserve System voted unanimously to raise the interest rate paid on reserve balances to 3.90 percent, effective September 17, 2026."
  - p119 Standing overnight repurchase agreement operation rate = **4** percent (2026-09-17..2026-09-17) [DISCARD: Repo rate is redundant with p4.] quote: "Conduct standing overnight repurchase agreement operations at a rate of 4.0 percent."
  - p120 Standing overnight reverse repurchase agreement offering rate = **3.75** percent (2026-09-17..2026-09-17) [DISCARD: Reverse repo rate is redundant with p5.] quote: "Conduct standing overnight reverse repurchase agreement operations at an offering rate of 3.75 percent and with a per-counterparty limit of $160 billion per day."
  - p121 Per-counterparty daily limit for standing overnight reverse repurchase agreement = **160,000,000,000** USD per day (2026-09-17..2026-09-17) [DISCARD: Reverse repo limit is redundant with p6.] quote: "Conduct standing overnight reverse repurchase agreement operations at an offering rate of 3.75 percent and with a per-counterparty limit of $160 billion per day."
  - p122 Primary credit rate effective September 17, 2026 = **4** percent (2026-09-17..2026-09-17) [DISCARD: Primary credit rate is redundant with p3.] quote: "the Board of Governors of the Federal Reserve System voted unanimously to approve a 1/4 percentage point increase in the primary credit rate to 4.0 percent, effective September 17, 2026."
- `https://tradingeconomics.com/united-states/interest-rate/news/590264` -> **snapshot** (snapshot 20261008065632); points raw/verified 3/3
  - p123 FOMC target range for the federal funds rate, upper bound, after September 15–16 = **4** percent (2026-09-16..2026-09-16) [keep: ] quote: "raising the target range for the federal funds rate by 25bps to 3.75%-4%"
  - p124 FOMC target range for the federal funds rate, lower bound, after September 15–16 = **3.75** percent (2026-09-16..2026-09-16) [DISCARD: Lower bound is redundant with the upper bound.] quote: "raising the target range for the federal funds rate by 25bps to 3.75%-4%"
  - p125 FOMC target range increase at September 15–16, 2026 meeting = **25** basis points (2026-09-16..2026-09-16) [keep: ] quote: "raising the target range for the federal funds rate by 25bps to 3.75%-4%"
- `https://www.marquetteassociates.com/spooky-season/` -> **live_dated** (page date 2026-10-05); points raw/verified 5/3
  - p126 VIX intra-month high on October 24, 2008 during Global Financial Crisis = **89.5** index points (2008-10-24..2008-10-24) [DISCARD: 2008 VIX high is not relevant to the current decision.] quote: "the VIX reached an intra-month high of roughly 89.5 on October 24, 2008, as the crisis intensified"
  - p127 VIX level sustained for most of October 2008 = **60** index points (2008-10-01..2008-10-31) [DISCARD: October 2008 VIX level is not relevant to the current decision.] quote: "spent most of that month above 60"
  - p128 S&P 500 Index decline on Black Monday, October 19, 1987 = **20** % (1987-10-19..1987-10-19) [DISCARD: 1987 crash is not relevant to the current decision.] quote: "the infamous "Black Monday" crash of 1987 that saw the S&P 500 Index plummet by more than 20% occurred on October 19"
- dropped by code checks: 5 (number: more than one number in value_as_written: 2; period_end missing or unparseable: 3)

### b1 [forecasts_markets] Market-implied probabilities for the next FOMC meeting

Hypothesis: Fed funds futures or options prices as of the cutoff date would give a direct probability distribution over the target range after the next meeting, which is the single most valuable missing input for this discrete target.

Queries issued by the searcher: CME FedWatch tool FOMC meeting probabilities October 2026; fed funds futures implied probability target range December 2026 FOMC; "fed funds" futures October 28 FOMC 2026 probability upper bound 4.00% 4.25% October 15 2026; FOMC calendar 2026 October 27-28 meeting statement target range

- `https://www.barrons.com/livecoverage/stock-market-news-today-101526/card/after-hot-ppi-an-october-rate-hike-still-seen-as-less-likely-L08y5ueHByZvCdjg` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://finance.eastmoney.com/a/202610153895898754.html` -> **live_dated** (page date 2026-10-15); points raw/verified 5/0
- `https://www.cnbc.com/2026/10/14/fed-may-now-have-to-hike-twice-or-increase-by-a-half-point-in-december-traders-bet.html` -> **live_dated** (page date 2026-10-14); points raw/verified 14/4
  - p129 US consumer price index headline year-over-year change for September = **3.7** % (2026-09-01..2026-09-30) [keep: ] quote: "The consumer price index rose 3.7% on a year-over-year basis, exceeding a Dow Jones forecast of a 3.6% gain."
  - p130 Dow Jones forecast for September headline CPI year-over-year change = **3.6** % (2026-09-01..2026-09-30) [DISCARD: Dow Jones CPI forecast is redundant with p136.] quote: "The consumer price index rose 3.7% on a year-over-year basis, exceeding a Dow Jones forecast of a 3.6% gain."
  - p131 US core CPI (excluding food and energy) year-over-year change for September = **2.6** % (2026-09-01..2026-09-30) [keep: ] quote: "Core CPI, which removes food and energy inputs, increased by 2.6%, also more than economists expected."
  - p132 Core inflation annualized pace in September (Carson Group) = **3.7** % (2026-09-01..2026-09-30) [DISCARD: Carson Group annualized core pace is a derived commentary, redundant with p131/p151.] quote: "CPI came in hot and it wasn't just fuel prices, as core inflation ran at a 3.7% annualized pace in September and 3.2% over three years."
- `https://www.9fzt.com/724info/c6c08b989d1cced9370c2f29677540f0.html` -> **live_dated** (page date 2026-10-14); points raw/verified 6/4
  - p133 CME FedWatch implied probability of a 25bp Fed rate hike at the October 2026 FOM = **43.7** % (2026-10-14..2026-10-14) [keep: ] quote: "CME FedWatch工具显示,交易员对美联储10月加息25个基点的押注继续升温,加息概率升至43.7%"
  - p134 CME FedWatch implied probability of Fed holding rates unchanged at the October 2 = **56.3** % (2026-10-14..2026-10-14) [keep: ] quote: "维持利率不变的概率降至56.3%"
  - p135 US September CPI year-over-year change (actual) = **3.7** % (2026-09-01..2026-09-30) [keep: ] quote: "美国9月CPI同比上涨3.7%,高于市场预期的3.6%"
  - p136 US September CPI year-over-year change (market expectation) = **3.6** % (2026-09-01..2026-09-30) [DISCARD: Market CPI expectation is redundant with p130.] quote: "美国9月CPI同比上涨3.7%,高于市场预期的3.6%"
- dropped by code checks: 17 (period_end 2026-10-31 after as_of: 2; period_end 2026-12-31 after as_of: 6; period_end 2026-10-28 after as_of: 2; period_end missing or unparseable: 5; number: more than one number in value_as_written: 2)

### b2 [administrative] FOMC meeting calendar and dot plot

Hypothesis: The exact date of the next FOMC meeting after 2026-10-15 and the September 2026 dot plot median for end-2026 would anchor the expected policy path and reduce uncertainty about the timing and direction of the next move.

Queries issued by the searcher: FOMC 2026 meeting calendar dates; September 2026 Summary of Economic Projections dot plot median federal funds rate end-2026

- `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` -> **snapshot** (snapshot 20261012041551); points raw/verified 0/0
- `https://www.richmondfed.org/research/national_economy/macro_minute/2026/sep_by_sep_how_fed_walks_inflation_back_to_2_percent` -> **live_dated** (page date 2026-09-29); points raw/verified 12/4
  - p137 Start of FOMC publication of fed funds rate projections (SEP) = **2,012** month (2012-01-01..2012-01-31) [DISCARD: Start of SEP fed funds projections is not needed for the target level.] quote: "the FOMC only began publishing policymakers' projections of the fed funds rate in January 2012."
  - p138 Start of SEP publication = **2,007** month (2007-11-01..2007-11-30) [DISCARD: Start of SEP publication is not needed for the target level.] quote: "since the SEP's inception in November 2007."
  - p139 End of black-line midpoint of fed funds target range series in Figure 3 = **2,026** month (2026-08-01..2026-08-31) [DISCARD: End date of a chart series is not needed for the target level.] quote: "The black line shows the midpoint of the fed funds target range from January 2012 to August 2026."
  - p140 End of gray-line median projections of appropriate fed funds rate series in Figu = **2,026** month (2026-09-01..2026-09-30) [DISCARD: End date of a chart series is not needed for the target level.] quote: "The gray line shows median projections for the appropriate fed funds rate from January 2012 to September 2026."
- `https://economics.td.com/us-fomc-statement` -> **snapshot** (snapshot 20260930084847); points raw/verified 15/3
  - p141 FOMC target range upper bound after September 2026 meeting = **4** percent (2026-09-16..2026-09-16) [keep: ] quote: "lifting the target range to 3.75%-4.0%"
  - p142 FOMC target range lower bound after September 2026 meeting = **3.75** percent (2026-09-16..2026-09-16) [DISCARD: Lower bound is redundant with p141/p124.] quote: "lifting the target range to 3.75%-4.0%"
  - p143 FOMC policy rate increase at September 2026 meeting = **25** basis points (2026-09-16..2026-09-16) [keep: ] quote: "raised the policy rate by 25 basis points (bps)"
- `https://investinglive.com/central-banks/fed-dot-plot-signals-another-2026-rate-hike-as-growth-strengthens-and-inflation-remains-elevated/` -> **snapshot** (snapshot 20260917105506); points raw/verified 15/0
- dropped by code checks: 35 (period_end 2026-12-31 after as_of: 18; period_end missing or unparseable: 9; number: no number in value_as_written: 1; period_end 2027-12-31 after as_of: 4; period_end 2028-12-31 after as_of: 2; period_end 2029-12-31 after as_of: 1)

### b3 [attention] Analyst consensus for the next FOMC meeting

Hypothesis: Published analyst consensus and Fed communications after the weak September jobs report and below-consensus PCE would clarify whether the Committee is expected to hold, hike, or cut at the next meeting, resolving the tension between hawkish market pricing and dovish data.

Queries issued by the searcher: analyst consensus next FOMC meeting October 2026 federal funds rate expected; FOMC October 2026 rate cut expectations weak September jobs report

- `https://www.marketscreener.com/news/major-brokerages-expect-next-fed-rate-hike-in-december-ce785dd3dd8ff125` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chase.com/personal/investments/learning-and-insights/article/will-the-federal-reserve-hike-rates-at-october-2026-fomc-meeting` -> **live_dated** (page date 2026-10-14); points raw/verified 13/9
  - p144 Fed rate hike at September 2026 meeting = **25** basis points (2026-09-01..2026-09-30) [keep: ] quote: "After the 25 basis-point move in September, we expect the Federal Reserve to tighten an additional 50 basis points into 2027."
  - p145 Fed rate easing at end of 2025 = **75** basis points (2025-10-01..2025-12-31) [DISCARD: 2025 easing is historical context, not needed for the next-meeting level.] quote: "This would serve to offset the 75 basis points of easing they did at the end of 2025."
  - p146 US jobs added in September 2026 = **29,000** jobs (2026-09-01..2026-09-30) [keep: ] quote: "The economy added just 29,000 jobs (below expectations), and downward revisions were made to prior months while the unemployment rate ticked higher to 4.2%."
  - p147 US unemployment rate in September 2026 = **4.2** percent (2026-09-01..2026-09-30) [keep: ] quote: "the unemployment rate ticked higher to 4.2%"
  - p148 US CPI annual rate in September 2026 = **3.7** percent (2026-09-01..2026-09-30) [keep: ] quote: "Consumer prices rose at an annual rate of 3.7% in September, up from 3.4% in August, and slightly higher than expectations."
  - p149 US CPI annual rate in August 2026 = **3.4** percent (2026-08-01..2026-08-31) [keep: ] quote: "Consumer prices rose at an annual rate of 3.7% in September, up from 3.4% in August, and slightly higher than expectations."
  - p150 US CPI month-over-month change in September 2026 = **0.6** percent (2026-09-01..2026-09-30) [keep: ] quote: "Prices were up 0.6% month over month from August, the biggest increase since April."
  - p151 US core CPI month-over-month change in September 2026 = **0.3** percent (2026-09-01..2026-09-30) [keep: ] quote: "core CPI rose 0.3% since the prior month and 2.6% since last September, both also higher than expectations."
  - p152 US core CPI annual rate in September 2026 = **2.6** percent (2026-09-01..2026-09-30) [keep: ] quote: "core CPI rose 0.3% since the prior month and 2.6% since last September, both also higher than expectations."
- `https://admiralmarkets.com/analytics/traders-blog/fed-rate-decision-october-2026` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://finance.eastmoney.com/a/202610023888399160.html` -> **snapshot** (snapshot 20261008040124); points raw/verified 13/8
  - p153 US unemployment rate, September 2026 = **4.2** percent (2026-09-01..2026-09-30) [keep: ] quote: "失业率从4.1%升至4.2%"
  - p154 US unemployment rate, August 2026 = **4.1** percent (2026-08-01..2026-08-31) [DISCARD: August unemployment rate is redundant with p25/p24.] quote: "失业率从4.1%升至4.2%"
  - p155 US 10-year Treasury yield, 2026-10-02 = **5.18** percent (2026-10-02..2026-10-02) [keep: ] quote: "基准10年期国债收益率下跌近6个基点,至5.18%"
  - p156 US 30-year Treasury yield, 2026-10-02 = **5.57** percent (2026-10-02..2026-10-02) [keep: ] quote: "30年期国债收益率则下跌3个基点,至5.57%"
  - p157 US 2-year Treasury yield, 2026-10-02 = **4.73** percent (2026-10-02..2026-10-02) [keep: ] quote: "2年期国债收益率下跌6个基点,至4.73%"
  - p158 Market-implied probability of Fed holding rates unchanged at October 2026 meetin = **84** percent (2026-10-02..2026-10-02) [keep: ] quote: "交易员目前认为美联储在10月会议上维持利率不变的概率升至84%"
  - p159 US average hourly earnings month-over-month change, September 2026 = **0.1** percent (2026-09-01..2026-09-30) [DISCARD: Average hourly earnings m/m is redundant with p160.] quote: "平均小时工资较8月份增长了0.1%"
  - p160 US average hourly earnings year-over-year change, September 2026 = **3** percent (2026-09-01..2026-09-30) [keep: ] quote: "同比增长3%"
- dropped by code checks: 9 (period_end missing or unparseable: 3; period_end 2027-12-31 after as_of: 1; number: unknown scale word '万': 5)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['fed funds rate', 'fomc decision', 'interest rate']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p56', 'p59', 'p103', 'p104', 'p107', 'p117', 'p123'] All state the same post-September-2026 FOMC target range upper bound of 4.00% (range 3.75%-4.00%). They are not independent measurements: p1/p117 are the same Federal Reserve implementation note, p56/
- corroborating: ['p2', 'p118', 'p3', 'p122', 'p4', 'p119', 'p5', 'p120'] Administered rates (IORB 3.90%, primary credit 4.00%, repo 4.00%, reverse repo 3.75%) are consistent with a 3.75%-4.00% target range. They corroborate the current policy stance but do not directly for
- corroborating: ['p8', 'p110', 'p125', 'p103'] All report the September 2026 hike as 25 basis points. Same underlying event, so not independent confirmation.
- corroborating: ['p24', 'p36', 'p53', 'p26', 'p28'] September 2026 unemployment rate of 4.2% (precise 4.175%) from BLS, St. Louis Fed, and a news report. Same underlying BLS data.
- corroborating: ['p30', 'p40', 'p51'] September 2026 nonfarm payroll gain of 29,000 jobs. Same BLS release.
- corroborating: ['p31', 'p32', 'p50'] Combined 60,000 downward revision to July and August payrolls. Same BLS revision.
- corroborating: ['p10', 'p11', 'p16', 'p17', 'p18', 'p19', 'p20', 'p22', 'p23'] August 2026 CPI details from one TD Economics report. Internally consistent; single source.
- corroborating: ['p55', 'p70', 'p62', 'p63'] PCE inflation around 3.4% in August 2026, above the 2% goal. p55 and p70 are the same headline PCE figure; p62/p63 are Fed staff estimates. Same underlying inflation picture.
- corroborating: ['p60', 'p111'] Market-implied probability of about 90% for the September 2026 hike. Same market pricing, not independent.
- corroborating: ['p61', 'p74'] Both indicate market/survey expectations of further tightening by end-2026/2027. p61 is a Desk survey from September; p74 is a later market pricing for end-2027. They support a hawkish tilt but do not
- corroborating: ['p88', 'p89', 'p90', 'p91', 'p92'] Historical FOMC decision counts from one source. Internally consistent; useful for base rates.
- corroborating: ['p101', 'p102', 'p77', 'p81', 'p82'] Historical step sizes: 25bp is the norm, with occasional 50bp and 75bp moves. Different periods but consistent with discrete 25bp increments.
- corroborating: ['p106', 'p114'] Longer-run dot at 3.2% and 2% inflation goal. Context for the policy path, not a direct forecast for the next meeting.
- corroborating: ['p70', 'p71', 'p72', 'p73'] August PCE inflation came in below consensus (3.4% vs 3.7% expected; core 3.0% vs 3.3% expected). This is a dovish data surprise relative to expectations.
- corroborating: ['p24', 'p30', 'p51', 'p52'] September jobs report was weak relative to expectations (29k vs 90k expected) and unemployment ticked up to 4.2%. This is a dovish data surprise.
- corroborating: ['p8', 'p75'] September 2026 was the first rate hike since 2023. Confirms the policy cycle turned to tightening.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p56', 'p59', 'p103', 'p104', 'p107', 'p117', 'p123', 'p141'] All report the same post-September-2026 FOMC target range upper bound of 4.00% (range 3.75–4.00%). They are not independent: they trace to the same September 16, 2026 FOMC decision and statement, so t
- corroborating: ['p2', 'p3', 'p4', 'p5', 'p118', 'p119', 'p120', 'p122'] Administered rates (IORB 3.90%, primary credit 4.00%, repo 4.00%, reverse repo 3.75%) are consistent with a 3.75–4.00% target range. They are implementation details of the same decision, not independe
- corroborating: ['p8', 'p110', 'p125', 'p143'] All state the September 2026 move was 25 bp. Same underlying event; useful for confirming the current level and the 25 bp step convention.
- corroborating: ['p24', 'p36', 'p53', 'p147', 'p153'] September 2026 unemployment rate 4.2%, up from 4.1% in August. Multiple outlets but same BLS source; treat as one measurement.
- corroborating: ['p30', 'p40', 'p51', 'p146'] September 2026 nonfarm payroll gain 29,000, well below expectations. Same BLS release; the consensus expectation (p52) is a separate input.
- corroborating: ['p10', 'p11', 'p149'] August 2026 CPI 3.4% y/y. Same BLS CPI release.
- corroborating: ['p129', 'p135', 'p148'] September 2026 CPI 3.7% y/y, above expectations. Same BLS release; the hot September CPI is the key new inflation datum before the next meeting.
- corroborating: ['p131', 'p151', 'p152'] September 2026 core CPI 2.6% y/y and 0.3% m/m. Same BLS release.
- corroborating: ['p55', 'p62', 'p63', 'p70', 'p72'] August 2026 PCE inflation around 3.4% (core 3.0–3.4% depending on methodology). Same BEA/PCE family; the Fed staff and market reports agree inflation is well above 2%.
- corroborating: ['p133', 'p134'] CME FedWatch as of 2026-10-14: 43.7% probability of a 25 bp hike at the October 2026 FOMC meeting, 56.3% hold. These are complementary and sum to 100%; they are the most direct market-implied probabil
- conflicting: ['p158', 'p133'] On 2026-10-02 traders put 84% probability on a hold at the October meeting; by 2026-10-14 the hike probability had risen to 43.7%. This is a genuine time-series shift, not a contradiction: the hot Sep
- corroborating: ['p60', 'p61', 'p111'] Market and Desk survey probabilities before the September 2026 meeting correctly anticipated the 25 bp hike. Useful as a check on market-implied probabilities, but they refer to the September meeting,
- corroborating: ['p74', 'p144'] Market pricing and Chase both expect further tightening into 2027 (at least 50 bp more). This supports a non-trivial probability of a hike at the next meeting, but is not a direct probability for the 
- corroborating: ['p89', 'p90', 'p91', 'p92'] Since 1990, 206 holds vs 110 changes (52 hikes, 58 cuts). Base rate of no change at a given meeting is high, but the current regime is a hiking cycle, so the unconditional base rate must be conditione
- corroborating: ['p101', 'p102', 'p77', 'p81', 'p82'] 25 bp is the dominant step size (77 of 110 changes since 1990; all changes in 2004–06 were 25 bp). Larger steps cluster in crises. This supports modeling the next move as 0 or ±25 bp with high probabi
- corroborating: ['p83', 'p84', 'p85', 'p86', 'p87', 'p93'] Unscheduled meetings are rare and account for only 13% of target changes. The next decision is almost certainly at a scheduled meeting, so the meeting date is not a major source of uncertainty for the
- corroborating: ['p106', 'p114'] Longer-run median dot 3.2% and 2% inflation goal indicate the Committee views the current 4.00% upper bound as restrictive relative to the longer run, which could argue against aggressive further hike
- corroborating: ['p155', 'p156', 'p157'] On 2026-10-02 the 2-year yield was 4.73%, 10-year 5.18%, 30-year 5.57%. A steep curve with high long yields is consistent with elevated inflation and term premium, and with market pricing of further t

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|

Rejected by code:

- a1 Probability of a 25 bp cut at the October 2026 FOMC meeting: need 0 < low <= value <= high

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | outcome_probs | n/a |  | [] |  | 0.00 |  | outcome '3.75%': assumption a1 was rejected (need 0 < low <= value <= high) |

## Outcome probabilities (computed by code)

Most likely: **** (n/a); pooling equal_linear_pool over 0 method(s); weight on methods that use assumptions 0.00.

| outcome | value | agent (pooled) | Jev (not pooled) |
|---|---|---|---|
| 3.00% | 3 | **n/a** | n/a |
| 3.25% | 3.25 | **n/a** | n/a |
| 3.50% | 3.5 | **n/a** | n/a |
| 3.75% | 3.75 | **n/a** | n/a |
| 4.00% | 4 | **n/a** | n/a |
| 4.25% | 4.25 | **n/a** | n/a |
| 4.50% | 4.5 | **n/a** | n/a |
| 4.75% | 4.75 | **n/a** | n/a |
| 5.00% | 5 | **n/a** | n/a |
| 5.25% | 5.25 | **n/a** | n/a |

Jev arm (TypeSafe, not pooled): not_configured: TYPESAFE_KEY_FILE is not set; Jev arm skipped

## Final answer

No estimate: no outcome-probability method could be computed from the verified evidence.

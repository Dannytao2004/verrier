# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park, as counted by the National Park Service's official monthly visitation statistics (the NPS Social Science Program's monthly 'Recreation Visits' series for Yellowstone NP). | unit recreation visits (count of park entries, not unique visitors) | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), Social Science Program / Public Use Statistics Office, published via nps.gov/stats and the NPS Visitor Use Statistics database (irma.nps.gov).

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [own_history] NPS official monthly visitation statistics for Yellowstone National Park

Hypothesis: The August 2026 value will be close to the August values of 2023, 2024, and 2025, adjusted for any known trend or shocks. The most recent published months (June and July 2026) will indicate the current level and trajectory.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics 2026; NPS visitor use statistics Yellowstone August 2024 recreation visits; Yellowstone visitation statistics for August 2025 nps.gov news release; irma.nps.gov STATS Yellowstone NP recreation visits by month report

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 0/0
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 9/9
  - p1 Yellowstone NP recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: Direct August 2025 Yellowstone recreation visits; key base for same-period naive and YoY methods.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p2 Yellowstone NP recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: Direct August 2024 Yellowstone recreation visits; key base for same-period naive and YoY methods.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p3 Yellowstone NP recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: Direct August 2021 Yellowstone recreation visits; useful historical reference for same-period level.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p4 Yellowstone NP recreation visits, year-to-date through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: YTD-through-August 2025 Yellowstone; supports trend context but not directly the August monthly target.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p5 Yellowstone NP recreation visits, year-to-date through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: YTD-through-August 2024 Yellowstone; supports trend context.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p6 Yellowstone NP recreation visits, year-to-date through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: YTD-through-August 2021 Yellowstone; supports trend context.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p7 Yellowstone NP recreation visits, year-to-date through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: YTD-through-August 2023 Yellowstone; supports trend context.] quote: "2023 - 3,308,924"
  - p8 Yellowstone NP recreation visits, year-to-date through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: YTD-through-August 2022 Yellowstone; flood-affected, useful as shock reference.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p9 Yellowstone NP recreation visits, year-to-date through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: YTD-through-August 2020 Yellowstone; COVID-affected, useful as shock reference.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/Park/YELL` -> **snapshot** (snapshot 20260113011158); points raw/verified 0/0

### d2 [related_series] NPS monthly visitation for other large western national parks and the National Park System total

Hypothesis: Yellowstone's visitation often moves with that of other destination parks (Grand Teton, Glacier, Zion, Yosemite) and with the system-wide total. If these parks show a strong August 2026 (or July 2026) trend, Yellowstone likely follows. Grand Teton is especially correlated because many visitors combine the two parks.

Queries issued by the searcher: NPS Visitor Use Statistics monthly recreation visits Grand Teton Yellowstone 2026; national park system monthly visitation 2026 statistics; NPS Visitor Use Statistics Yellowstone August 2025 recreation visits 856,467 monthly report; Zion Yosemite Glacier national park monthly recreation visits July 2026

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 9/9
  - p10 Yellowstone NP recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1 (same August 2025 value).] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p11 Yellowstone NP recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of p2 (same August 2024 value).] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p12 Yellowstone NP recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of p3 (same August 2021 value).] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p13 Yellowstone NP recreation visits, year-to-date through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p4 (same YTD-through-August 2025 value).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p14 Yellowstone NP recreation visits, year-to-date through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p5 (same YTD-through-August 2024 value).] quote: "up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p15 Yellowstone NP recreation visits, year-to-date through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p6 (same YTD-through-August 2021 value).] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p16 Yellowstone NP recreation visits, year-to-date through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p7 (same YTD-through-August 2023 value).] quote: "2023 - 3,308,924"
  - p17 Yellowstone NP recreation visits, year-to-date through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p8 (same YTD-through-August 2022 value).] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p18 Yellowstone NP recreation visits, year-to-date through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p9 (same YTD-through-August 2020 value).] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.jhnewsandguide.com/news/business/market-watch-airport-sets-all-time-record-for-monthly-traffic/article_bd0ceec6-da2f-42df-9994-3f32b7e1546` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-02 > as_of); points raw/verified -/-
- `https://buckrail.com/grand-teton-sees-third-busiest-june-with-more-than-660000-visitors/` -> **live_dated** (page date 2026-07-24); points raw/verified 14/14
  - p19 Grand Teton NP recreation visits, June 2026 = **666,422** recreation visits (2026-06-01..2026-06-30) [keep: Grand Teton June 2026 recreation visits; related-park signal for current-year trend.] quote: "Grand Teton National Park (GTNP) saw its third-busiest June this year, with 666,422 recreation visits."
  - p20 Grand Teton NP recreation visits, June 2025 = **680,406** recreation visits (2025-06-01..2025-06-30) [keep: Grand Teton June 2025 recreation visits; prior-year signal for YoY scaling.] quote: "the total for the month is a 2% decrease from June of 2025, when 680,406 people visited the park."
  - p21 Grand Teton NP recreation visits, June 2021 = **757,897** recreation visits (2021-06-01..2021-06-30) [keep: Grand Teton June 2021 recreation visits; historical reference for related-park series.] quote: "Visitation showed a 12% decrease from June 2021 (757,897 recreation visits)"
  - p22 Grand Teton NP recreation visits, year 2021 total = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Grand Teton annual 2021 total; wrong period for monthly target and not needed.] quote: "which was the park's record-breaking year with over 3.88 million visits."
  - p23 Grand Teton NP year-to-date recreation visits through June 2026 = **1,300,932** recreation visits (2026-01-01..2026-06-30) [keep: Grand Teton YTD-through-June 2026; corroborates current-year trend.] quote: "So far this year, GTNP has hosted 1,300,932 recreation visits."
  - p24 Grand Teton NP year-to-date recreation visits through June 2025 = **1,268,597** recreation visits (2025-01-01..2025-06-30) [keep: Grand Teton YTD-through-June 2025; prior-year comparison for trend.] quote: "a 2.5% increase over January through June of 2025, which recorded 1,268,597 visits."
  - p25 Grand Teton NP year-to-date recreation visits through June 2021 = **1,404,959** recreation visits (2021-01-01..2021-06-30) [keep: Grand Teton YTD-through-June 2021; historical reference.] quote: "the total number of visits is down 7.4% from 2021, which saw 1,404,959 recreation visits."
  - p26 Yellowstone NP recreation visits, June 2026 = **903,000** recreation visits (2026-06-01..2026-06-30) [keep: Yellowstone June 2026 recreation visits; most recent monthly level for current-year trajectory.] quote: "Yellowstone hosted just over 903,000 visitors in June."
  - p27 Grand Teton NP year-to-date recreation visits through June 2026 = **1,300,932** recreation visits (2026-01-01..2026-06-30) [DISCARD: Duplicate of p23 (same Grand Teton YTD-through-June 2026 value).] quote: "- 2026 - 1,300,932"
  - p28 Grand Teton NP year-to-date recreation visits through June 2025 = **1,268,597** recreation visits (2025-01-01..2025-06-30) [DISCARD: Duplicate of p24 (same Grand Teton YTD-through-June 2025 value).] quote: "- 2025 - 1,268,597"
  - p29 Grand Teton NP year-to-date recreation visits through June 2024 = **1,214,488** recreation visits (2024-01-01..2024-06-30) [keep: Grand Teton YTD-through-June 2024; historical reference for related-park series.] quote: "- 2024 - 1,214,488"
  - p30 Grand Teton NP year-to-date recreation visits through June 2023 = **1,080,336** recreation visits (2023-01-01..2023-06-30) [keep: Grand Teton YTD-through-June 2023; historical reference for related-park series.] quote: "- 2023 - 1,080,336"
  - p31 Grand Teton NP year-to-date recreation visits through June 2022 = **989,072** recreation visits (2022-01-01..2022-06-30) [keep: Grand Teton YTD-through-June 2022; historical reference for related-park series.] quote: "- 2022 - 989,072"
  - p32 Grand Teton NP year-to-date recreation visits through June 2021 = **1,404,959** recreation visits (2021-01-01..2021-06-30) [DISCARD: Duplicate of p25 (same Grand Teton YTD-through-June 2021 value).] quote: "- 2021 - 1,404,959"
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-

### d3 [physical_flow] Transportation and entry-point data: vehicle counts at Yellowstone entrances, airport arrivals, and highway traffic

Hypothesis: Yellowstone visits are largely by personal vehicle. Counts of vehicles entering the park (if published) or traffic volumes on approach highways (US-89, US-191, US-20) and passenger arrivals at Bozeman Yellowstone International Airport (BZN) and Jackson Hole Airport (JAC) will correlate with park visits. Increases in these flows suggest higher August 2026 visits.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits statistics 2026; Bozeman Yellowstone airport passenger statistics 2026; Yellowstone visitation statistics for August 2026 NPS news release recreation visits; Jackson Hole Airport enplanements 2026 passenger statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.ypradio.org/regional-news/2026-06-10/another-record-month` -> **live_dated** (page date 2026-06-10); points raw/verified 3/2
  - p33 Yellowstone National Park recreation visits in May = **570,272** recreation visits (2026-05-01..2026-05-31) [keep: Yellowstone May 2026 recreation visits; recent monthly level for current-year trajectory.] quote: "the park hosted 570,272 visits in May, up 1% from May 2025"
  - p34 Yellowstone National Park recreation visits year-to-date = **773,653** recreation visits (2026-01-01..2026-05-31) [keep: Yellowstone YTD-through-May 2026; corroborates current-year trend.] quote: "So far this year, the park has hosted 773,653 recreation visits"
- `https://dailymontanan.com/2026/06/10/yellowstone-national-park-visitation-on-record-pace-through-may/` -> **live_dated** (page date 2026-06-10); points raw/verified 4/4
  - p35 Yellowstone National Park recreation visits in May = **570,000** recreation visits (2026-05-01..2026-05-31) [DISCARD: Duplicate/rounded version of p33 (same May 2026 value).] quote: "Yellowstone National Park saw more than 570,000 visitors pass through its entrance stations last month, the busiest May on record"
  - p36 Yellowstone National Park recreation visits through first five months of 2026 = **773,653** recreation visits (2026-01-01..2026-05-31) [DISCARD: Duplicate of p34 (same YTD-through-May 2026 value).] quote: "Through the first five months of 2026, Yellowstone has hosted 773,653 recreation visits, up 1.1% from 2025"
  - p37 Yellowstone National Park total visitors in record-breaking year 2021 = **4,800,000** visitors (2021-01-01..2021-12-31) [DISCARD: Yellowstone annual 2021 total; wrong period for monthly target and not needed.] quote: "a whopping 20% higher than May of 2021, which was Yellowstone's record-breaking year with more than 4.8 million visitors"
  - p38 Yellowstone National Park total visitors in 2025 = **4,700,000** visitors (2025-01-01..2025-12-31) [DISCARD: Yellowstone annual 2025 total; wrong period for monthly target and not needed.] quote: "In 2025, Yellowstone saw its second-highest visitation on record with more than 4.7 million visitors"
- `https://nbcmontana.com/news/local/yellowstone-hosts-busiest-may-with-visits-up-20-from-2021` -> **snapshot** (snapshot 20260620181014); points raw/verified 0/0
- `https://buckrail.com/yellowstone-reports-slightly-slower-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-17 > as_of); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d4 [capacity_consumption] Accommodation providers, campgrounds, and local tourism businesses in gateway communities

Hypothesis: Occupancy rates and room revenues in gateway towns (West Yellowstone, Gardiner, Cody, Jackson) and inside-park lodging/campground reservations reflect visitor demand. Higher occupancy and revenue in August 2026 imply higher park visits. Inside-park campground and lodge occupancy data may be available from concessioners (Xanterra, Delaware North).

Queries issued by the searcher: Yellowstone National Park monthly recreation visits 2026 NPS statistics; West Yellowstone hotel occupancy 2026 lodging tax revenue Park County Montana; "Yellowstone visitation statistics" July 2026 nps.gov news release; Yellowstone National Park campground occupancy Xanterra August 2026

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 0/0
- `https://irma.nps.gov/Stats/Reports/Park/YELL` -> **snapshot** (snapshot 20260113011158); points raw/verified 0/0
- `https://www.nps.gov/yell/learn/news/26016.htm` -> **dropped** (snapshot fetch failed (http -1); live page has no readable date); points raw/verified -/-
- `https://www.publicnow.com/view/6E6BE9C15EBB4DEF9CE036E94398FD914F71DF47` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-

### d5 [administrative] Park permits, reservations, and entrance fee transactions

Hypothesis: The number of advance reservations for Yellowstone lodging/campgrounds, backcountry permits, and commercial tour permits for August 2026 indicates expected demand. Entrance fee revenue (if published monthly) is a direct proxy for visits. Any changes in reservation policies or fees could shift counts.

Queries issued by the searcher: Yellowstone National Park recreation visits August 2026 NPS statistics; Yellowstone backcountry permits statistics 2025; Yellowstone entrance fee revenue 2026; Recreation.gov Yellowstone reservations August 2026

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://ebs.publicnow.com/view/FCBC7BE758668E5A1DB645205801D4438187CF6B` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/fees.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://publiclandsdata.com/reservations/yell` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-

### d6 [attention] Public attention and interest signals: web search, social media, news coverage

Hypothesis: Google Trends search interest for 'Yellowstone National Park' and related terms in the weeks before and during August 2026 correlates with actual visits. A spike or drop in search interest, social media posts, or news coverage (e.g., about closures, wildlife, wildfires) can signal changes in visitation.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits statistics 2026; NPS Visitor Use Statistics Yellowstone recreation visits August 2026; Yellowstone National Park news August 2026 visitation; Google Trends Yellowstone National Park search interest 2026

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://buckrail.com/yellowstone-reports-slightly-slower-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-17 > as_of); points raw/verified -/-
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-

### d7 [shocks] Events and conditions in or just before August 2026 that could affect visitation

Hypothesis: Wildfires, road closures, flooding, wildlife incidents, government shutdowns, gas prices, or policy changes (e.g., reservation requirements) can significantly alter August 2026 visits. The 2022 flood and 2020 COVID closure caused major drops. Any such event in 2026 must be accounted for.

Queries issued by the searcher: Yellowstone National Park recreation visits 2026 monthly visitation statistics; Yellowstone National Park closure 2026; Yellowstone wildfire 2026; Yellowstone road construction 2026

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://buckrail.com/yellowstone-reports-slightly-slower-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-17 > as_of); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 0/0
- `https://www.nps.gov/yell/learn/management/current-fire-activity.htm` -> **snapshot** (snapshot 20260722025734); points raw/verified 0/0

### d8 [forecasts_markets] Published forecasts, tourism outlooks, and prediction markets

Hypothesis: Tourism forecasts for Montana/Wyoming or national park visitation in 2026, and any prediction market contracts on Yellowstone visitation, provide direct estimates. These may incorporate expert judgment and current conditions.

Queries issued by the searcher: Montana tourism forecast 2026 Institute for Tourism and Recreation Research; Yellowstone National Park visitation forecast 2026; Yellowstone visitation prediction market Polymarket Kalshi 2026; NPS Yellowstone monthly recreation visits August 2026 statistics nps.gov/stats

- `https://www.travelandtourworld.pl/aktualno%C5%9Bci/artyku%C5%82/63ykvnvt60ul/` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live page dated 2026-08-17 > as_of); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://scholarworks.umt.edu/cgi/viewcontent.cgi?params=%2Fcontext%2Fitrr_pubs%2Farticle%2F1499%2F&path_info=2026_BBER_Economic_Outlook_Seminar.pdf` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p10'] Same August 2025 Yellowstone value (881,936) from the same NPS source, duplicated across d1 and d2.
- corroborating: ['p2', 'p11'] Same August 2024 Yellowstone value (868,259), duplicated across d1 and d2.
- corroborating: ['p3', 'p12'] Same August 2021 Yellowstone value (921,844), duplicated across d1 and d2.
- corroborating: ['p4', 'p13'] Same YTD-through-August 2025 Yellowstone value (3,547,967), duplicated across d1 and d2.
- corroborating: ['p5', 'p14'] Same YTD-through-August 2024 Yellowstone value (3,494,350), duplicated across d1 and d2.
- corroborating: ['p6', 'p15'] Same YTD-through-August 2021 Yellowstone value (3,590,609), duplicated across d1 and d2.
- corroborating: ['p7', 'p16'] Same YTD-through-August 2023 Yellowstone value (3,308,924), duplicated across d1 and d2.
- corroborating: ['p8', 'p17'] Same YTD-through-August 2022 Yellowstone value (2,437,607), duplicated across d1 and d2.
- corroborating: ['p9', 'p18'] Same YTD-through-August 2020 Yellowstone value (2,556,528), duplicated across d1 and d2.
- corroborating: ['p19', 'p20', 'p21', 'p23', 'p24', 'p25'] Grand Teton June 2026 and historical June/YTD values from Buckrail; internally consistent and from a single live-dated source.
- corroborating: ['p23', 'p27'] Same Grand Teton YTD-through-June 2026 value (1,300,932), duplicated within the same source.
- corroborating: ['p24', 'p28'] Same Grand Teton YTD-through-June 2025 value (1,268,597), duplicated within the same source.
- corroborating: ['p25', 'p32'] Same Grand Teton YTD-through-June 2021 value (1,404,959), duplicated within the same source.
- corroborating: ['p33', 'p35'] Yellowstone May 2026 visits reported as 570,272 (ypradio) and 'more than 570,000' (dailymontanan); consistent.
- corroborating: ['p34', 'p36'] Yellowstone YTD-through-May 2026 visits reported as 773,653 by two independent outlets.
- corroborating: ['p26'] Yellowstone June 2026 visits (~903,000) from Buckrail; no conflicting value found.
- corroborating: ['p37', 'p38'] Yellowstone annual totals for 2021 (~4.8M) and 2025 (~4.7M) from dailymontanan; consistent with NPS records.

## Methods (computed by code)

| id | method | estimate | backtest years | mean abs ln err | weight | notes / error |
|---|---|---|---|---|---|---|
| m1 | series_naive | 875,098 | [] |  | 0.33 |  |
| m2 | yoy_scaling | 863,810 | [] |  | 0.33 |  |
| m3 | linear_fit | n/a | [] |  | 0.00 | linear_fit needs >= 3 aligned years, has 2 |
| m4 | ratio | 837,196 | [2021, 2025] | 0.064 | 0.33 |  |

Result: central **858,553**, 80% interval [791,350, 931,464], basis historical_errors, weight rule inverse_backtest_error

## Final answer

We estimate 858,553 recreation visits to Yellowstone in August 2026, with an [n] interval of 791,350 to 931,464 (historical errors). The estimate blends 3 methods: a naive two-August base (875,098, weight 33%), year-over-year scaling by Grand Teton's June 2026/2025 ratio (863,810, weight 33%), and a historical Yellowstone-August-to-Grand-Teton-June ratio (837,196, weight 33%, backtest error 6.6%). A regression method was dropped for insufficient aligned years, leaving 21 usable points. Equal weights reflect that no method clearly dominates. The true value could differ because Yellowstone counts depend on entrance vehicle counts and occupancy factors, weather, road closures, and reservation rules, and because Grand Teton June is an imperfect proxy. Missing evidence includes 2026 summer traffic data, post-2025 methodology changes, and a longer consistent August history for backtesting.

# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics. A recreation visit is defined by NPS as a visit by a person entering the park for recreational purposes; one person entering multiple times counts as multiple visits. Thi | unit recreation visits (count) | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), typically via the Visitor Use Statistics program and the monthly 'National Park Service Visitor Use Report' or park-level monthly reports.

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from vehicle entries at park entrances multiplied by average persons per vehicle. Target = (number of vehicles entering in August) × (average occupancy). This requires data on vehicle counts and occupancy rates.

Queries issued by the searcher: Yellowstone vehicle entries August statistics; Yellowstone average vehicle occupancy visitation study; Yellowstone persons-per-vehicle multiplier Table 1 NPS visitor use reporting instructions; irma.nps.gov Yellowstone monthly public use report August recreation visits vehicles

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://ravallirepublic.com/outdoors/article_8902f5e0-bbea-5962-b86d-545832082acf.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstonegate.com/?p=7848` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/getinvolved/upload/YELL_Phase-2-Traffic-Parking-Analysis_508-reduced.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d2 [shocks] Known disruptions or events affecting 2026 visitation

Hypothesis: Any major closures, road construction, wildfires, or policy changes in 2026 could significantly alter visitation relative to historical patterns. The direction and magnitude of the effect must be estimated. Target = baseline × (1 + shock adjustment).

Queries issued by the searcher: Yellowstone National Park closures 2026; Yellowstone road construction summer 2026 visitation; Yellowstone visitation statistics July 2026 recreation visits; Yellowstone June 2026 visitation statistics recreation visits record

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p1 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p2 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p3 Yellowstone National Park recreation visits, July 2021 (record-breaking year, bu = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p4 Yellowstone National Park recreation visits, full year 2021 (record-breaking yea = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p5 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p6 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p7 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p8 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p9 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p10 Yellowstone National Park year-to-date recreation visits through July 2022 (park = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm?pubDate=20260625` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26009.htm` -> **snapshot** (snapshot 20260812105204); points raw/verified 6/0
- dropped by code checks: 6 (period_end missing or unparseable: 5; number: no number in value_as_written: 1)

### d3 [related_series] NPS total national park visitation and Yellowstone's share

Hypothesis: Yellowstone's August visits can be estimated as a share of total NPS August visitation, or by comparing to other large parks. The share may be stable over time. Target = (total NPS August visits) × (Yellowstone share of total).

Queries issued by the searcher: NPS total recreation visits August 2025 monthly visitation report; Yellowstone National Park August 2024 visitation record recreation visits; NPS monthly recreation visits summary August 2024 total national park system IRMA monthly report; "Yellowstone" August 2025 visitation 881,936 recreation visits

- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://idahonews.com/news/local/park-population-peaks-yellowstone-sees-slight-rise-in-august-visitors` -> **snapshot** (snapshot 20250906003304); points raw/verified 8/8
  - p11 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park experienced a slight uptick in visitors this August, with 881,936 recreation visits recorded."
  - p12 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "This marks a 2% increase from August 2024, which saw 868,259 visits."
  - p13 Yellowstone National Park recreation visits, August 2021 (record-breaking) = **921,844** visitors (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "this year's August visitation was still 4% lower than the record-breaking August of 2021, when 921,844 visitors flocked to the park."
  - p14 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone has welcomed 3,547,967 recreation visits so far, according to the National Park Service"
  - p15 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "reflecting a 2% rise from the same period in 2024, which had 3,494,350 visits."
  - p16 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "the current year's numbers are down 1% from 2021, when the park recorded 3,590,609 visits by the end of August."
  - p17 Yellowstone National Park year-to-date visits through August 2022 (flood closure = **2,437,607** visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "In 2022, the park was closed for several days in June due to a historic flood event, resulting in 2,437,607 visits by August."
  - p18 Yellowstone National Park year-to-date visits through August 2020 (COVID closure = **2,556,528** visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "In 2020, the park faced closures from March to May due to the COVID-19 pandemic, leading to 2,556,528 visits by the end of August."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [capacity_consumption] Lodging, campground, and hotel occupancy in and around Yellowstone

Hypothesis: Overnight stays are a component of visits. Total visits can be approximated by (overnight visitors) + (day visitors). Overnight visitors can be estimated from lodging capacity and occupancy rates. Target = (available rooms/campsites × occupancy × average persons per room) + day-use estimate.

Queries issued by the searcher: Yellowstone lodging occupancy August hotel rooms gateway communities; Yellowstone campground occupancy statistics capacity number of campsites; Yellowstone National Park annual visitation statistics overnight stays; Yellowstone gateway community hotel occupancy rate August Montana Wyoming

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=2c222867-d550-4094-a6ae-1cb6d0659aab&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fP` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://igbconline.org/wp-content/uploads/Yellowstone-Grizzly-Bear-Investigations-2024-IGBST-Annual-Report.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://yellowstone.co/camping.htm` -> **snapshot** (snapshot 20260615181604); points raw/verified 0/0

### d5 [forecasts_markets] Published forecasts or predictions for 2026 Yellowstone visitation

Hypothesis: Any available forecasts for 2026 annual or summer visitation can be used to anchor the August estimate. Target = forecasted annual visits × (August share of annual visits).

Queries issued by the searcher: Yellowstone visitation forecast 2026; Yellowstone National Park monthly visitation statistics August share of annual visits; GeoJournal of Tourism and Geosites 2026 forecasting tourism demand Yellowstone 4.19 million 2026; Yellowstone recreation visits June 2026 visitation report 903,025

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 15/15
  - p19 Average August visits to Yellowstone National Park, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [EXCLUDED (ablation): ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p20 August share of average annual visits to Yellowstone National Park, 2014-2018 av = **20.89** % (2014-08-01..2018-08-31) [EXCLUDED (ablation): ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p21 Average July visits to Yellowstone National Park, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [EXCLUDED (ablation): ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p22 July share of average annual visits to Yellowstone National Park, 2014-2018 aver = **23.57** % (2014-07-01..2018-07-31) [EXCLUDED (ablation): ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p23 Average June visits to Yellowstone National Park, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [EXCLUDED (ablation): ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p24 June share of average annual visits to Yellowstone National Park, 2014-2018 aver = **19.42** % (2014-06-01..2018-06-30) [EXCLUDED (ablation): ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p25 Average September visits to Yellowstone National Park, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p26 September share of average annual visits to Yellowstone National Park, 2014-2018 = **16.51** % (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p27 Average May visits to Yellowstone National Park, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [EXCLUDED (ablation): ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p28 May share of average annual visits to Yellowstone National Park, 2014-2018 avera = **9.99** % (2014-05-01..2018-05-31) [EXCLUDED (ablation): ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p29 Average October visits to Yellowstone National Park, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [EXCLUDED (ablation): ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p30 October share of average annual visits to Yellowstone National Park, 2014-2018 a = **5.57** % (2014-10-01..2018-10-31) [EXCLUDED (ablation): ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p31 Average April visits to Yellowstone National Park, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [EXCLUDED (ablation): ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p32 Average February visits to Yellowstone National Park, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [EXCLUDED (ablation): ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p33 Average January visits to Yellowstone National Park, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [EXCLUDED (ablation): ] quote: "\| January \| 28,837 \| 0.72% \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [base_rates] Average length of stay and party size for Yellowstone visitors

Hypothesis: If total visitor-days or person-days are known, visits can be derived by dividing by average length of stay. Alternatively, if total unique visitors are known, visits = unique visitors × average number of visits per person. Target = (total visitor-days) / (average length of stay).

Queries issued by the searcher: Yellowstone average length of stay visitors visitor survey; Yellowstone National Park visitor use statistics average length of stay days; NPS Visitor Use Statistics Yellowstone August 2026 recreation visits monthly report; Yellowstone average length of stay days visitor-days 2024 2025

- `https://www.nps.gov/yell/getinvolved/upload/R-YELL_VUS_FINAL-Report-2.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.hereandthere.club/national-park-visitation/yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.degruyterbrill.com/document/doi/10.1525/9780520976924-039/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [attention] Search interest and social media activity as a proxy for visitation

Hypothesis: Google Trends or social media mentions for Yellowstone in August 2026 may correlate with actual visits. If a stable relationship exists, target = (attention index) × (conversion factor). This is indirect and requires a bridge.

Queries issued by the searcher: Google Trends Yellowstone National Park August visitation correlation; Yellowstone National Park monthly visitation statistics August 2025; NPS Visitor Use Statistics monthly report August 2026 recreation visits Yellowstone; Google Trends search interest national parks correlates with visitation research study

- `https://www.cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p34 Yellowstone Google search lead over Grand Canyon, July 2025 to June 2026 = **1,420,000** searches (2025-07-01..2026-06-30) [DISCARD: Attention proxy with no stable, sourced conversion factor to NPS recreation visits; using it would require inventing a c] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p35 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p36 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p37 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p38 Yellowstone National Park record-breaking year 2021 total recreation visits (sta = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p39 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p40 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p41 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p42 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2025 - 3,547,967"
  - p43 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "2024 - 3,494,350"
  - p44 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p45 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p46 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p47 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [base_rates] Historical NPS monthly visitation series

Hypothesis: A clean monthly series of Yellowstone recreation visits for August 2015–2025 would provide the baseline level and recent trend needed for a credible August 2026 forecast. This is the single most important missing input because no kept point currently supplies any level of Yellowstone visitation.

Queries issued by the searcher: NPS Visitor Use Statistics Yellowstone monthly recreation visits August; Yellowstone National Park monthly visitation report August 2024 2025; Yellowstone monthly visitation statistics 2020 2021 2022 2023 August recreation visits table; nps.gov/yell visitation statistics August 2023 846,389 recreation visits news release

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p48 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p49 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p50 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p51 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p52 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p53 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p54 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p55 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2025 - 3,547,967"
  - p56 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "2024 - 3,494,350"
  - p57 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p58 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p59 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p60 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.nps.gov/yell/learn/news/23037.htm` -> **snapshot** (snapshot 20260617061634); points raw/verified 13/13
  - p61 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p62 Yellowstone National Park recreational visits, August 2022 = **582,211** recreational visits (2022-08-01..2022-08-31) [EXCLUDED (ablation): ] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p63 Yellowstone National Park recreational visits, August 2019 = **820,006** recreational visits (2019-08-01..2019-08-31) [EXCLUDED (ablation): ] quote: "and a 3% increase from August 2019* (820,006 recreational visits)."
  - p64 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "So far in 2023, the park has hosted 3,313,244 recreation visits"
  - p65 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "up 36% from 2022 (2,437,607 recreation visits)"
  - p66 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [EXCLUDED (ablation): ] quote: "and up 6% from 2019 (3,114,697 recreation visits)."
  - p67 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p68 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528"
  - p69 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [EXCLUDED (ablation): ] quote: "2018 - 3,136,241"
  - p70 Percent increase in Yellowstone recreation visits, August 2023 vs August 2022 = **45** % (2023-08-01..2023-08-31) [EXCLUDED (ablation): ] quote: "This is a 45% increase from August 2022"
  - p71 Percent increase in Yellowstone recreation visits, August 2023 vs August 2019 = **3** % (2023-08-01..2023-08-31) [EXCLUDED (ablation): ] quote: "and a 3% increase from August 2019*"
  - p72 Percent increase in Yellowstone year-to-date recreation visits, 2023 vs 2022 thr = **36** % (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "up 36% from 2022"
  - p73 Percent increase in Yellowstone year-to-date recreation visits, 2023 vs 2019 thr = **6** % (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "and up 6% from 2019"
- `https://yellowstonenotebooknews.blogspot.com/search/label/visitation%20statistics` -> **snapshot** (snapshot 20231224073643); points raw/verified 15/15
  - p74 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p75 Yellowstone National Park recreation visits, August 2022 = **582,211** recreation visits (2022-08-01..2022-08-31) [EXCLUDED (ablation): ] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p76 Yellowstone National Park recreation visits, August 2019 = **820,006** recreation visits (2019-08-01..2019-08-31) [EXCLUDED (ablation): ] quote: "and a 3% increase from August 2019* (820,006 recreational visits)"
  - p77 Yellowstone National Park recreation visits, August 2021 (most-visited August on = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This is a 37% decrease from August 2021 (921,844 recreational visits), the most-visited August on record"
  - p78 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "So far in 2023, the park has hosted 3,313,244 recreation visits"
  - p79 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "up 36% from 2022 (2,437,607 recreation visits)"
  - p80 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p81 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528"
  - p82 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [EXCLUDED (ablation): ] quote: "2019 - 3,114,697"
  - p83 Yellowstone National Park recreation visits, July 2023 = **969,692** recreation visits (2023-07-01..2023-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 969,692 recreation visits in July 2023."
  - p84 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 838,458 recreation visits in September 2023."
  - p85 Yellowstone National Park recreation visits, June 2023 = **847,864** recreation visits (2023-06-01..2023-06-30) [EXCLUDED (ablation): ] quote: "The park hosted 847,864 recreation visits in June 2023."
  - p86 Yellowstone National Park recreation visits, October 2023 = **299,127** recreation visits (2023-10-01..2023-10-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 299,127 recreation visits in October 2023."
  - p87 Yellowstone National Park recreation visits, May 2023 = **454,929** recreation visits (2023-05-01..2023-05-31) [EXCLUDED (ablation): ] quote: "The park hosted 454,929 recreation visits in May 2023."
  - p88 Yellowstone National Park year-to-date recreation visits through October 2023 = **4,446,509** recreation visits (2023-01-01..2023-10-31) [EXCLUDED (ablation): ] quote: "So far in 2023, the park has hosted 4,446,509 recreation visits"

### b2 [shocks] 2026 park operations and access conditions

Hypothesis: Any 2026-specific closures, road construction, wildfire smoke, reservation requirements, or policy changes affecting Yellowstone access in August 2026 would determine whether the historical August baseline should be adjusted up or down. Without this, the baseline route carries unquantified shock risk.

Queries issued by the searcher: Yellowstone 2026 road construction closures August; Yellowstone National Park 2026 reservation entry requirement; Yellowstone wildfire smoke air quality advisory August 2026; Yellowstone National Park August 2025 recreation visits record monthly report

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 16/5
  - p89 Yellowstone road improvement project delays along the road between Canyon Villag = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Redundant detail of the same road-project announcement as p90-p93; no independent quantitative visitation signal.] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p90 Yellowstone road improvement project delays in the Old Faithful area, up to 15-m = **15** minutes (2026-07-15..2026-08-15) [DISCARD: Redundant detail of the same road-project announcement; delay minutes cannot be converted to a visitation change without] quote: "expect up to 15-minute delays from mid-July through mid-August."
  - p91 Yellowstone road improvement project along the road between Canyon Village and W = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Redundant detail of the same road-project announcement; no independent quantitative visitation signal.] quote: "One lane will be closed while crews work; traffic lights will operate in 10-minute increments."
  - p92 Yellowstone road improvement project along the road between Canyon Village and W = **7** a.m. (start time) (2026-07-01..2026-08-14) [DISCARD: Redundant detail of the same road-project announcement; no independent quantitative visitation signal.] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p93 Yellowstone road improvement project along the road between Canyon Village and W = **6** p.m. (end time) (2026-07-01..2026-08-14) [DISCARD: Redundant detail of the same road-project announcement; no independent quantitative visitation signal.] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
- `https://www.yellowstonenationalparklodges.com/alerts/` -> **snapshot** (snapshot 20260703035945); points raw/verified 15/0
- `https://www.nps.gov/yell/learn/news/26009.htm` -> **snapshot** (snapshot 20260812105204); points raw/verified 6/0
- `https://kamala.cod.edu/wy/latest.aeus75.KRIW.html` -> **snapshot** (snapshot 20211024114540); points raw/verified 0/0
- dropped by code checks: 32 (period_end 2026-10-31 after as_of: 3; period_end 2026-09-07 after as_of: 1; period_end 2026-09-15 after as_of: 1; period_end 2026-11-30 after as_of: 2; period_end 2026-08-31 after as_of: 1; period_end 2026-12-31 after as_of: 1; value_as_written not in quote as a whole number: 1; period_end missing or unparseable: 14; number: more than one number in value_as_written: 4; period_end 2026-09-30 after as_of: 1; period_end 2027-10-31 after as_of: 1; number: no number in value_as_written: 2)

### b3 [related_series] NPS system-wide summer visitation

Hypothesis: If total NPS August visitation and Yellowstone's historical share of that total are available, a share-based route can cross-check the direct baseline route. This would help resolve uncertainty if the direct Yellowstone series is incomplete or if 2026 system-wide conditions differ from park-specific conditions.

Queries issued by the searcher: NPS total monthly recreation visits August National Park Service visitor use report; Yellowstone National Park monthly visitation statistics August recreation visits; NPS total recreation visits August 2025 300 million monthly summary report National Park Service; "Yellowstone" August 2024 868,259 recreation visits NPS press release

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p94 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p95 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p96 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p97 Yellowstone National Park record-breaking year 2021 recreation visits (over 4.8  = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p98 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p99 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p100 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p101 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p102 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p103 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260727191555); points raw/verified 0/0
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://publiclandsdata.com/national-park-visitation/data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visitation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- contextual: ['p34'] Single attention proxy for Yellowstone relative to Grand Canyon over July 2025–June 2026. It is not a level of visits and has no established conversion factor to August 2026 recreation visits; usable 
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p89', 'p90', 'p91', 'p92', 'p93'] All five points describe the same 2026 Yellowstone road-improvement project and its expected delays. They are not independent measurements; they are multiple details from one NPS announcement. They ar
- contextual: ['p34'] Google search lead over Grand Canyon is an attention proxy, not a visitation count. It may indicate relative interest but has no established conversion to Yellowstone August recreation visits. It is k

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 97 of 103
- methods allowed: ['formula_mc']

  - p1 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p2 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p3 Yellowstone National Park recreation visits, July 2021 (record-breaking year, busiest July = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p4 Yellowstone National Park recreation visits, full year 2021 (record-breaking year) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p5 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p6 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p7 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p8 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p9 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p10 Yellowstone National Park year-to-date recreation visits through July 2022 (park closed Ju = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p11 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p12 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p13 Yellowstone National Park recreation visits, August 2021 (record-breaking) = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p14 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p15 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p16 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p17 Yellowstone National Park year-to-date visits through August 2022 (flood closures) = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p18 Yellowstone National Park year-to-date visits through August 2020 (COVID closures) = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p19 Average August visits to Yellowstone National Park, 2014-2018 average = 839,787 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p20 August share of average annual visits to Yellowstone National Park, 2014-2018 average = 20.89 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p21 Average July visits to Yellowstone National Park, 2014-2018 average = 947,688 (2018-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p22 July share of average annual visits to Yellowstone National Park, 2014-2018 average = 23.57 (2018-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p23 Average June visits to Yellowstone National Park, 2014-2018 average = 780,652 (2018-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p24 June share of average annual visits to Yellowstone National Park, 2014-2018 average = 19.42 (2018-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p25 Average September visits to Yellowstone National Park, 2014-2018 average = 663,651 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p26 September share of average annual visits to Yellowstone National Park, 2014-2018 average = 16.51 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p27 Average May visits to Yellowstone National Park, 2014-2018 average = 401,449 (2018-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p28 May share of average annual visits to Yellowstone National Park, 2014-2018 average = 9.99 (2018-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p29 Average October visits to Yellowstone National Park, 2014-2018 average = 223,777 (2018-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p30 October share of average annual visits to Yellowstone National Park, 2014-2018 average = 5.57 (2018-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p31 Average April visits to Yellowstone National Park, 2014-2018 average = 44,027 (2018-04-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p32 Average February visits to Yellowstone National Park, 2014-2018 average = 33,088 (2018-02-28): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p33 Average January visits to Yellowstone National Park, 2014-2018 average = 28,837 (2018-01-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p35 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p36 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p37 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p38 Yellowstone National Park record-breaking year 2021 total recreation visits (stated as ove = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p39 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p40 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p41 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p42 Yellowstone National Park year-to-date recreation visits through August 2025 (list) = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p43 Yellowstone National Park year-to-date recreation visits through August 2024 (list) = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p44 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p45 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p46 Yellowstone National Park year-to-date recreation visits through August 2021 (list) = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p47 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p48 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p49 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p50 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p51 Yellowstone National Park record-breaking year 2021 recreation visits = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p52 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p53 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p54 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p55 Yellowstone National Park year-to-date recreation visits through August 2025 (list) = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p56 Yellowstone National Park year-to-date recreation visits through August 2024 (list) = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p57 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p58 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p59 Yellowstone National Park year-to-date recreation visits through August 2021 (list) = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p60 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p61 Yellowstone National Park recreation visits, August 2023 = 846,389 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p62 Yellowstone National Park recreational visits, August 2022 = 582,211 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p63 Yellowstone National Park recreational visits, August 2019 = 820,006 (2019-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p64 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,313,244 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p65 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p66 Yellowstone National Park year-to-date recreation visits through August 2019 = 3,114,697 (2019-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p67 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p68 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p69 Yellowstone National Park year-to-date recreation visits through August 2018 = 3,136,241 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p70 Percent increase in Yellowstone recreation visits, August 2023 vs August 2022 = 45 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p71 Percent increase in Yellowstone recreation visits, August 2023 vs August 2019 = 3 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p72 Percent increase in Yellowstone year-to-date recreation visits, 2023 vs 2022 through Augus = 36 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p73 Percent increase in Yellowstone year-to-date recreation visits, 2023 vs 2019 through Augus = 6 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p74 Yellowstone National Park recreation visits, August 2023 = 846,389 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p75 Yellowstone National Park recreation visits, August 2022 = 582,211 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p76 Yellowstone National Park recreation visits, August 2019 = 820,006 (2019-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p77 Yellowstone National Park recreation visits, August 2021 (most-visited August on record) = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p78 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,313,244 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p79 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p80 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p81 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p82 Yellowstone National Park year-to-date recreation visits through August 2019 = 3,114,697 (2019-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p83 Yellowstone National Park recreation visits, July 2023 = 969,692 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p84 Yellowstone National Park recreation visits, September 2023 = 838,458 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p85 Yellowstone National Park recreation visits, June 2023 = 847,864 (2023-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p86 Yellowstone National Park recreation visits, October 2023 = 299,127 (2023-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p87 Yellowstone National Park recreation visits, May 2023 = 454,929 (2023-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p88 Yellowstone National Park year-to-date recreation visits through October 2023 = 4,446,509 (2023-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p94 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p95 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p96 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p97 Yellowstone National Park record-breaking year 2021 recreation visits (over 4.8 million) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p98 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p99 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p100 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p101 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p102 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p103 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

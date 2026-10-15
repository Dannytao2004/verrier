# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions c | unit recreation visits (count) | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from the number of vehicles entering the park multiplied by average occupancy. Entrance station counts may be available from park records or traffic counters.

Queries issued by the searcher: Yellowstone entrance vehicle counts August traffic volume study; Yellowstone average vehicle occupancy persons per vehicle survey NPS; NPS Visitor Use Statistics Yellowstone monthly recreation visits August 2025 2024 report; Yellowstone August 2024 recreational vehicles entered park number entrance stations monthly report

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p1 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p2 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p3 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p4 Yellowstone National Park record-breaking year 2021 recreation visits (over 4.8  = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p5 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p6 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p7 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p8 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p9 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p10 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.nps.gov/yell/getinvolved/upload/YELL_Phase-2-Traffic-Parking-Analysis_508-reduced.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://irma.nps.gov/DataStore/DownloadFile/691038` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-

### d2 [shocks] Closures, weather, and policy changes

Hypothesis: Any major closures (e.g., road washouts, wildfires, government shutdown) or policy changes (e.g., reservation requirements) in August 2026 would alter visitation relative to the historical baseline. The direction and magnitude of the effect can be estimated from past similar events.

Queries issued by the searcher: Yellowstone closure August 2026; Yellowstone visitation statistics August 2025 record; Yellowstone wildfire closure August 2026; Yellowstone reservation system 2026 entrance

- `https://www.imdb.com/es-es/news/ni65361747/?ref_=tt_nwr_1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://local.newsbreak.com/news/4623970203291-yellowstone-season-6-isn-t-happening-here-s-what-s-replacing-it` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cowboystatedaily.com/2026/10/12/collision-with-2-000-pound-yellowstone-bison-leaves-seasonal-workers-in-a-jam/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://local.newsbreak.com/news/4942922736770-yellowstone-closes-beartooth-highway-for-season-what-fall-visitors-need-to-know` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National Park Service overall visitation and Yellowstone's share

Hypothesis: Yellowstone's August visitation is a relatively stable share of total NPS August visitation or of visitation to a comparable set of large western parks. If total NPS August 2026 or a proxy is available, the share can be applied.

Queries issued by the searcher: NPS total recreation visits August 2025; Yellowstone National Park August 2025 visitation record; Yellowstone visitation statistics July 2026; Grand Teton National Park visitation July 2026

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p11 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p12 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p13 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p14 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p15 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p16 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p17 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p18 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p19 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p20 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p21 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p22 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p23 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p24 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p25 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p26 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p27 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p28 Yellowstone National Park year-to-date recreation visits through August 2025 (tr = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2025 - 3,547,967"
  - p29 Yellowstone National Park year-to-date recreation visits through August 2024 (tr = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "2024 - 3,494,350"
  - p30 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p31 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p32 Yellowstone National Park year-to-date recreation visits through August 2021 (tr = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p33 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/orgs/1207/03-13-26-2025-visitation-statsitics.htm` -> **snapshot** (snapshot 20260811053736); points raw/verified 15/15
  - p34 Total NPS recreation visits, 2025 (all reporting parks) = **323,014,305** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- 323,014,305 recreation visits (406 parks report visitation figures)"
  - p35 Total NPS recreation visits, 2025 (stated as more than, headline figure) = **323,000,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Rounded headline duplicate of p34; adds no information beyond the precise 2025 NPS-wide total.] quote: "The National Park Service today announced it recorded more than 323 million recreation visits in 2025"
  - p36 Total NPS overnight stays, 2025 (headline figure) = **13,000,000** overnight stays (2025-01-01..2025-12-31) [DISCARD: Rounded headline duplicate of p37; the precise overnight-stay figure is retained.] quote: "including over 13 million overnight stays, with 26 parks setting new visitation records"
  - p37 Total NPS overnight stays, 2025 (detailed figure) = **13,016,577** overnight stays (2025-01-01..2025-12-31) [keep: ] quote: "- 13,016,577 overnight stays"
  - p38 Total NPS recreation visitor hours, 2025 = **1,386,749,187** recreation visitor hours (2025-01-01..2025-12-31) [DISCARD: NPS-wide recreation visitor hours for 2025 cannot be converted to Yellowstone August 2026 visits without an unsupported ] quote: "- 1,386,749,187 recreation visitor hours"
  - p39 Number of parks setting visitation records, 2025 = **26** parks (2025-01-01..2025-12-31) [DISCARD: Count of parks setting records in 2025 is irrelevant to the level of Yellowstone August 2026 visitation.] quote: "- 26 parks set visitation records"
  - p40 Number of parks reporting visitation figures, 2025 = **406** parks (2025-01-01..2025-12-31) [DISCARD: Count of reporting parks is a metadata item, not a quantity usable in any route to Yellowstone August 2026 visits.] quote: "- 323,014,305 recreation visits (406 parks report visitation figures)"
  - p41 Yellowstone NP recreation visits, 2025 (Top 10 National Parks) = **4,762,988** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "- Yellowstone NP 4,762,988"
  - p42 Grand Teton NP recreation visits, 2025 (Top 10 National Parks) = **3,800,648** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Teton NP 3,800,648"
  - p43 Glacier NP recreation visits, 2025 (Top 10 National Parks) = **3,136,557** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Glacier NP 3,136,557"
  - p44 Great Smoky Mountains NP recreation visits, 2025 (Top 10 National Parks) = **11,527,939** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Great Smoky Mountains NP 11,527,939"
  - p45 Zion NP recreation visits, 2025 (Top 10 National Parks) = **4,984,525** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Zion NP 4,984,525"
  - p46 Grand Canyon NP recreation visits, 2025 (Top 10 National Parks) = **4,430,653** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Canyon NP 4,430,653"
  - p47 Yosemite NP recreation visits, 2025 (Top 10 National Parks) = **4,278,413** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Yosemite NP 4,278,413"
  - p48 Rocky Mountain NP recreation visits, 2025 (Top 10 National Parks) = **4,171,431** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Rocky Mountain NP 4,171,431"

### d4 [capacity_consumption] Lodging, campground, and parking capacity

Hypothesis: Overnight stays and campground occupancy provide a lower bound or component of total visits. Total visits = overnight visitors + day-use visitors. Overnight capacity and occupancy rates can estimate the overnight component; day-use can be estimated from parking capacity and turnover.

Queries issued by the searcher: Yellowstone National Park lodging occupancy August statistics; Yellowstone campground capacity number of sites statistics; Yellowstone National Park lodging rooms number units Xanterra 2000 rooms statistics; NPS Visitor Use Statistics Yellowstone overnight stays August 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/campgrounds.htm` -> **snapshot** (snapshot 20260731011505); points raw/verified 15/0
- `https://www.nationalparkstraveler.org/parks/yellowstone-national-park/camping-yellowstone` -> **snapshot** (snapshot 20250327165432); points raw/verified 15/0
- `https://www.yellowstoneexplored.com/yellowstone-lodging` -> **snapshot** (snapshot 20260513223606); points raw/verified 2/0
- dropped by code checks: 32 (period_end missing or unparseable: 22; period_end 2026-09-13 after as_of: 1; period_end 2026-09-19 after as_of: 1; period_end 2026-10-17 after as_of: 2; period_end 2026-09-26 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-10-11 after as_of: 1; period_end 2026-10-12 after as_of: 1; period_end 2026-09-27 after as_of: 1; number: no number in value_as_written: 1)

### d5 [base_rates] Seasonal share of annual visitation

Hypothesis: August typically accounts for a stable percentage of Yellowstone's annual visitation (e.g., around 15–20%). If a preliminary annual total for 2026 is available or can be forecast, the August share can be applied.

Queries issued by the searcher: Yellowstone annual visitation 2025 NPS visitor use statistics; Yellowstone August visitation share of annual visits 2019 2020 2021 2022 2023 2024; Yellowstone National Park 2026 visitation projection year-to-date July; Yellowstone monthly visitation August 2025 recreation visits NPS

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p49 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p50 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p51 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p52 Yellowstone National Park annual recreation visits, 2021 record-breaking year = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p53 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p54 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p55 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p56 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p57 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p58 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Tourism forecasts and industry outlooks

Hypothesis: National or regional tourism forecasts for summer 2026 may indicate whether travel to Yellowstone is expected to be higher or lower than 2025. These forecasts can adjust the baseline estimate.

Queries issued by the searcher: summer 2026 national park visitation forecast; Yellowstone tourism outlook 2026 visitation forecast; Bozeman Yellowstone International Airport passenger traffic 2026 record; Yellowstone July 2026 visitation record recreation visits

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.cn/消息/刊文/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bozemanairport.com/content/files/Newsletter-2026-Enplanement-Projection.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.bostonglobe.com/2026/06/22/lifestyle/national-parks-what-to-know/` -> **snapshot** (snapshot 20260802112801); points raw/verified 15/0
- dropped by code checks: 15 (period_end missing or unparseable: 14; value_as_written not in quote as a whole number: 1)

### d7 [attention] Search and social media interest

Hypothesis: Online attention (Google Trends, social media mentions) for Yellowstone in August 2026 relative to August 2025 may correlate with visitation changes. This can serve as a leading indicator if a stable relationship exists.

Queries issued by the searcher: Google Trends Yellowstone National Park August 2026 visitation; Yellowstone National Park visitation statistics July 2026 record; Yellowstone National Park Google Trends search interest 2026 vs 2025; "Yellowstone" social media mentions August 2026 tourism

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p59 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p60 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p61 Yellowstone National Park recreation visits, July 2021 (record-breaking year, bu = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p62 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p63 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p64 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p65 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p66 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p67 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p68 Yellowstone National Park year-to-date recreation visits through July 2022 (park = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p69 Yellowstone Google search margin over Grand Canyon National Park, July 2025 to J = **1,420,000** searches (2025-07-01..2026-06-30) [DISCARD: Search-volume margin is not a visitation measurement and no stable search-to-visit conversion is available; using it wou] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://creators.yahoo.com/lifestyle/story/the-most-searched-national-park-in-every-state-reveals-one-clear-favorite-174747097.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [base_rates] Yellowstone monthly seasonality

Hypothesis: If Yellowstone's August share of annual recreation visits is stable (roughly 15-20%), then a preliminary 2026 annual total or a forecast annual total would allow a direct August 2026 estimate. This would unlock a base-rate route and reduce reliance on NPS-wide share assumptions.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits August 2024 NPS Visitor Use Statistics; Yellowstone National Park 2025 visitation record year-end recreation visits; Yellowstone visitation statistics for August 2025 news release; Yellowstone National Park August share of annual recreation visits percentage month by month 2019 2021 2023

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p70 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p71 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p72 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p73 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p74 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p75 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p76 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p77 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p78 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p79 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] NPS-wide August seasonality and Yellowstone share

Hypothesis: If NPS-wide August recreation visits for 2025 (or recent years) and Yellowstone's share of NPS-wide August visits are available, then a 2026 NPS-wide August total or forecast could be scaled to Yellowstone. This would provide a top-down cross-check on the bottom-up route.

Queries issued by the searcher: Yellowstone National Park August 2025 visitation statistics recreation visits; NPS Visitor Use Statistics monthly recreation visits August 2025 all parks total; NPS national park service monthly public use report August 2025 recreation visits total all parks; National Park Service 2026 visitation statistics monthly recreation visits June July 2026

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p80 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p81 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p82 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p83 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p84 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p85 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p86 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p87 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2025 - 3,547,967"
  - p88 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "2024 - 3,494,350"
  - p89 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p90 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p91 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "2021 - 3,590,609"
  - p92 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260727191555); points raw/verified 0/0
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] August 2026 conditions at Yellowstone

Hypothesis: Any major closure, reservation requirement, wildfire, or policy change in August 2026 would materially shift visitation relative to the historical baseline. Identifying such events would allow a directional adjustment and reduce uncertainty in the central estimate.

Queries issued by the searcher: Yellowstone National Park August 2026 visitation; Yellowstone National Park alerts road closures 2026; Yellowstone National Park July 2026 visitation statistics recreation visits; Yellowstone wildfire August 2026 smoke closure

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p93 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p94 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p95 Yellowstone National Park recreation visits, July 2021 (record-breaking July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p96 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p97 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p98 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p99 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p100 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p101 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p102 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-visitation-down-in-august` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26009.htm` -> **snapshot** (snapshot 20260812105204); points raw/verified 6/0
- dropped by code checks: 6 (period_end missing or unparseable: 5; number: no number in value_as_written: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visitation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p34', 'p35'] Both report the same 2025 NPS-wide recreation-visit total; p35 is the rounded headline version of p34. They share one underlying NPS measurement and are not independent.
- corroborating: ['p36', 'p37'] Both report the same 2025 NPS-wide overnight-stay total; p36 is the rounded headline version of p37. Same underlying source.
- corroborating: ['p34', 'p38', 'p39', 'p40'] These are different metrics from the same 2025 NPS annual visitation release (visits, visitor hours, record-setting parks, reporting parks). They are mutually consistent context but do not independent
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] These are 2025 annual recreation-visit totals for individual large parks from the same NPS Top-10 list. They provide a comparable-park context set but are not independent of the NPS annual release.
- corroborating: ['p34', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] The park-level totals are components/context within the same NPS 2025 annual visitation release as the NPS-wide total; they share the same publisher and measurement system.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p34', 'p35'] Same NPS 2025 annual release; p35 is the rounded headline of the same measurement as p34, so they are not independent. p34 is the precise figure and should be preferred if a 2025 NPS-wide total is nee
- corroborating: ['p36', 'p37'] Same NPS 2025 release; p37 is the precise overnight-stay total and p36 its rounded headline. Not independent.
- corroborating: ['p38', 'p39', 'p40'] All from the same NPS 2025 annual announcement; they describe different quantities (visitor hours, record-setting parks, reporting parks) and share a single underlying source, so they corroborate the 
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] All are 2025 annual park-level totals from the same NPS Top-10 list. They are mutually consistent and useful as scale/context for Yellowstone's magnitude, but they are annual totals for other parks, n
- corroborating: ['p34', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] Park-level 2025 totals are a subset of the NPS-wide 2025 total; they share the same NPS reporting system and are not independent of p34.
- contextual: ['p69', 'p34'] p69 is a search-attention margin for Yellowstone over Grand Canyon, not a visitation measurement. It can only serve as a weak directional indicator and cannot be converted to visits without an unsuppo

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Yellowstone August share of annual recreation visits | 17 | 14..20 | 11.83..23.66 (widened) | % | m1 (m1) | Yellowstone's summer peak is concentrated in July-August; the August share of annual recreation visits has historically been in the mid-to-high teens. The range spans plausible recent values and is used only to scale an annual total to August. | A credible 2026 annual Yellowstone recreation-visit total is available or can be forecast, and August 2026 is not disrupted by a major closure or policy change relative to the annual pattern. | Evidence that Yellowstone's August share of annual visits has moved outside roughly 14-20% in recent years, or a major August-specific disruption that changes the seasonal distribution. |
| a2 | Yellowstone share of NPS-wide annual recreation visits | 1.5 | 1.2..1.8 | 1.039..2.078 (widened) | % | m2 (m2) | Yellowstone is one of the largest parks but its annual visits are a small share of the roughly 323 million NPS-wide total; the range reflects plausible recent shares consistent with the park's scale relative to the Top-10 parks listed. | An NPS-wide 2026 annual recreation-visit total or forecast is available and Yellowstone's relative share is stable. | Evidence that Yellowstone's share of NPS-wide visits has shifted materially outside the stated range, or that NPS-wide reporting scope changed. |
| a3 | August share of NPS-wide annual recreation visits | 12 | 10..14 | 8.367..16.73 (widened) | % | m2 (m2) | Summer months dominate NPS-wide visitation; August is typically one of the highest months. The range is a broad prior for the August share of the annual NPS-wide total. | An NPS-wide 2026 annual total is available and the August seasonal share is stable. | Evidence that the NPS-wide August share of annual visits falls outside roughly 10-14%. |

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 87 of 102
- methods allowed: ['formula_mc']

  - p1 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p2 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p3 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p4 Yellowstone National Park record-breaking year 2021 recreation visits (over 4.8 million) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p5 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p6 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p7 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p8 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p9 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p10 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p11 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p12 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p13 Yellowstone National Park recreation visits, July 2021 (record busiest July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p14 Yellowstone National Park total recreation visits in record-breaking year 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p15 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p16 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p17 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p18 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p19 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p20 Yellowstone National Park year-to-date recreation visits through July 2022 = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p21 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p22 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p23 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p24 Yellowstone National Park record-breaking year 2021 recreation visits = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p25 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p26 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p27 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p28 Yellowstone National Park year-to-date recreation visits through August 2025 (trend list) = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p29 Yellowstone National Park year-to-date recreation visits through August 2024 (trend list) = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p30 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p31 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p32 Yellowstone National Park year-to-date recreation visits through August 2021 (trend list) = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p33 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p41 Yellowstone NP recreation visits, 2025 (Top 10 National Parks) = 4,762,988 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p49 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p50 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p51 Yellowstone National Park recreation visits, July 2021 (record July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p52 Yellowstone National Park annual recreation visits, 2021 record-breaking year = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p53 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p54 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p55 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p56 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p57 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p58 Yellowstone National Park year-to-date recreation visits through July 2022 = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p59 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p60 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p61 Yellowstone National Park recreation visits, July 2021 (record-breaking year, busiest July = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p62 Yellowstone National Park total recreation visits in record-breaking year 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p63 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p64 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p65 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p66 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p67 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p68 Yellowstone National Park year-to-date recreation visits through July 2022 (park closed Ju = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p70 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p71 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p72 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p73 Yellowstone National Park record-breaking annual recreation visits, 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p74 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p75 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p76 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p77 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p78 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p79 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p80 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p81 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p82 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p83 Yellowstone National Park record-breaking year 2021 recreation visits = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p84 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p85 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p86 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p87 Yellowstone National Park year-to-date recreation visits through August 2025 (list) = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p88 Yellowstone National Park year-to-date recreation visits through August 2024 (list) = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p89 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p90 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p91 Yellowstone National Park year-to-date recreation visits through August 2021 (list) = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p92 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p93 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p94 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p95 Yellowstone National Park recreation visits, July 2021 (record-breaking July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p96 Yellowstone National Park total recreation visits in record-breaking year 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p97 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p98 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p99 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p100 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p101 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p102 Yellowstone National Park year-to-date recreation visits through July 2022 = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 636,601 | ['p42'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 562,177 | ['p34'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

Result: central **598,232**, 80% interval [354,179, 1,010,455], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for recreation visits to Yellowstone National Park during August 2026, as reported in NPS monthly visitation statistics, is 598,232 visits. This is a model-based combination of 2 methods, with an interval of 354,179 to 1,010,455 (80% level, monte carlo). Method [n] gives 636,601 (weight 50%), scaling a comparable park's annual visits by Yellowstone's August share (17%, range 11.83%–23.66%). Method [n] gives 562,177 (weight 50%), applying Yellowstone's NPS-wide share (1.5%, range 1.039%–2.078%) and August's NPS-wide share (12%, range 8.367%–16.73%). Only the anchor totals are observed; all shares are analyst assumptions, and the comparable-park transfer is weak. The main risk is a Yellowstone-specific shock or changed reporting scope. The most useful missing evidence would be recent monthly Yellowstone counts to calibrate the August share.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Yellowstone August share of annual recreation visits: 17%, range 11.83% to 23.66% (range widened by code); used by m1. Overturned by: Evidence that Yellowstone's August share of annual visits has moved outside roughly [n]-[n] in recent years, or a major August-specific disruption that changes the seasonal distribution.
- a2 Yellowstone share of NPS-wide annual recreation visits: 1.5%, range 1.039% to 2.078% (range widened by code); used by m2. Overturned by: Evidence that Yellowstone's share of NPS-wide visits has shifted materially outside the stated range, or that NPS-wide reporting scope changed.
- a3 August share of NPS-wide annual recreation visits: 12%, range 8.367% to 16.73% (range widened by code); used by m2. Overturned by: Evidence that the NPS-wide August share of annual visits falls outside roughly [n]-[n].

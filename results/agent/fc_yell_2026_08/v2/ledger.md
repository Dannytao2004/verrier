# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times counts as multiple visi | unit recreation visits | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [own_history] NPS official monthly visitation reports

Hypothesis: August recreation visits in recent years (e.g., 2023, 2024, 2025) provide a baseline. The 2026 value is likely to be similar to recent August values, adjusted for any known shocks or trends. The relationship is direct: target = recent August value × adjustment factor.

Queries issued by the searcher: Yellowstone National Park August 2025 visitation statistics recreation visits; NPS visitor use statistics Yellowstone August 2024 recreation visits; Yellowstone National Park visitation statistics July 2026; Yellowstone recreation visits June 2026 NPS visitation

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p1 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p2 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p3 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p4 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p5 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p6 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p7 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p8 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p9 Yellowstone National Park year-to-date recreation visits through July 2022 (floo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
  - p10 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p11 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p12 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p13 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p14 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p15 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p16 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p17 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p18 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p19 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p20 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from vehicle entries multiplied by average occupancy. If vehicle entry counts for August 2026 are available (even partial), they can be scaled. Historical vehicle counts and occupancy rates provide conversion factors.

Queries issued by the searcher: Yellowstone vehicle entries August 2025 visitation statistics; Yellowstone average occupancy per vehicle entrance station counts; Yellowstone persons-per-vehicle multiplier August 2.7 visitor use reporting instructions; Yellowstone park-wide vehicle entries August 2024 entrance station total

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p21 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p22 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p23 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p24 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p25 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p26 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p27 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p28 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "2025 - 3,547,967"
  - p29 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "2024 - 3,494,350"
  - p30 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p31 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p32 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "2021 - 3,590,609"
  - p33 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://thefederalnewswire.com/stories/633132361-yellowstone-national-park-visitation-statistics-on-memorial-day-weekend-2021` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://NPS.gov/yell/getinvolved/upload/YELL_Phase-2-Traffic-Parking-Analysis_508-reduced.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d3 [shocks] Park closures, weather, and policy changes

Hypothesis: Any major closures (e.g., road washouts, fires, government shutdown) or policy changes (e.g., reservation requirements) in August 2026 would alter visitation relative to baseline. The direction and magnitude depend on the shock. Historical analogues (e.g., 2022 flood closure) provide adjustment factors.

Queries issued by the searcher: Yellowstone National Park 2026 reservation system changes; Yellowstone closure August 2026 road washout; Yellowstone July 2026 recreation visits NPS visitor use statistics; Yellowstone fire August 2026 closure

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p34 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [DISCARD: Duplicate of p1.] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p35 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [DISCARD: Duplicate of p2.] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p36 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [DISCARD: Duplicate of p3.] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p37 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p38 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [DISCARD: Duplicate of p4.] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p39 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [DISCARD: Duplicate of p5.] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p40 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Duplicate of p6.] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p41 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [DISCARD: Duplicate of p7.] quote: "2024 - 2,626,091"
  - p42 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [DISCARD: Duplicate of p8.] quote: "2023 - 2,462,535"
  - p43 Yellowstone National Park year-to-date recreation visits through July 2022 (floo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Duplicate of p9.] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 15/7
  - p44 Yellowstone West Entrance to Madison road projected open period start date 2026 = **17** date (2026-04-17..2026-04-17) [DISCARD: Road schedule date encoded as day-of-month; not a usable numeric input.] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris, Mammoth Hot Springs to Norris, Norris to Canyon Village"
  - p45 Yellowstone East Entrance to Fishing Bridge (Sylvan Pass) and Canyon Village to  = **1** date (2026-05-01..2026-05-01) [DISCARD: Road schedule date encoded as day-of-month; not usable.] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p46 Yellowstone South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass = **8** date (2026-05-08..2026-05-08) [DISCARD: Road schedule date encoded as day-of-month; not usable.] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass), West Thumb to Lake Village, Tower-Roosevelt to Tower Fall"
  - p47 Yellowstone Canyon Village to Tower Fall (Dunraven Pass) projected open period s = **22** date (2026-05-22..2026-05-22) [DISCARD: Road schedule date encoded as day-of-month; not usable.] quote: "Open May 22 - October 12, 2026: Canyon Village to Tower Fall (Dunraven Pass)."
  - p48 Beartooth Highway (US-212) and Chief Joseph Scenic Byway (WY-296) projected open = **22** date (2026-05-22..2026-05-22) [DISCARD: Road schedule date encoded as day-of-month; not usable.] quote: "Open May 22 - October 12, 2026: Beartooth Highway (US-212), Chief Joseph Scenic Byway (WY-296)."
  - p49 Yellowstone road improvement project along road between Canyon Village and West  = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Construction delay magnitude; no quantitative visit bridge.] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p50 Yellowstone road improvement project along road between Canyon Village and West  = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Traffic-light increment; no quantitative visit bridge.] quote: "One lane will be closed while crews work; traffic lights will operate in 10-minute increments."
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (period_end 2026-10-31 after as_of: 4; period_end 2026-10-12 after as_of: 2; period_end 2026-08-31 after as_of: 1; period_end 2026-12-31 after as_of: 1)

### d4 [related_series] NPS-wide or regional visitation trends

Hypothesis: Yellowstone's August visits are a share of total NPS August visits or of visits to a comparable set of parks. If NPS-wide August 2026 data or forecasts are available, the share can be applied. Alternatively, nearby parks (Grand Teton, Glacier) may show correlated trends.

Queries issued by the searcher: NPS total recreation visits August 2025 national parks visitation statistics; Yellowstone National Park August 2025 visitation statistics; NPS total recreation visits August 2025 33 million monthly report systemwide; Grand Teton National Park August 2025 visitation recreation visits

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p51 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p52 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of p12.] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p53 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of p13.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p54 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p55 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p56 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p16.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p57 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p58 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p18.] quote: "2023 - 3,308,924"
  - p59 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p19.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p60 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p20.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260727191555); points raw/verified 0/0
- `https://www.nps.gov/subjects/socialscience/visitor-use-statistics-dashboard.htm` -> **snapshot** (snapshot 20260815113111); points raw/verified 15/10
  - p61 Total NPS recreation visits, calendar year 2025 = **323,000,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: NPS-wide annual total; no bridge to Yellowstone August.] quote: "The National Park Service reported 323 million recreation visits in calendar year 2025."
  - p62 Decrease in NPS recreation visits, 2025 vs 2024 record year = **8,850,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: NPS-wide annual change; no bridge.] quote: "This is a decrease of 8.85 million recreation visits, or 2.7%, from the record year in 2024."
  - p63 Percent decrease in NPS recreation visits, 2025 vs 2024 = **2.7** % (2025-01-01..2025-12-31) [DISCARD: NPS-wide annual percent change; no bridge.] quote: "This is a decrease of 8.85 million recreation visits, or 2.7%, from the record year in 2024."
  - p64 Number of National Park System units reporting visitor use = **406** park units (2025-01-01..2025-12-31) [DISCARD: Count of reporting units; irrelevant.] quote: "406 of the 433 National Park System units report visitor use."
  - p65 Total National Park System units = **433** park units (2025-01-01..2025-12-31) [DISCARD: Total system units; irrelevant.] quote: "406 of the 433 National Park System units report visitor use."
  - p66 NPS recreation visitor hours, calendar year 2025 = **1,390,000,000** recreation visitor hours (2025-01-01..2025-12-31) [DISCARD: NPS-wide visitor hours; no bridge.] quote: "Recreation visitor hours were 1.39 billion; a decrease of 0.7% from 2024."
  - p67 Percent decrease in NPS recreation visitor hours, 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [DISCARD: NPS-wide visitor-hour change; no bridge.] quote: "Recreation visitor hours were 1.39 billion; a decrease of 0.7% from 2024."
  - p68 Percent decrease in NPS overnight stays, 2025 vs 2024 = **2.4** % (2025-01-01..2025-12-31) [DISCARD: NPS-wide overnight-stay change; no bridge.] quote: "There was a 2.4% decrease from 2024 for overnight stays."
  - p69 Number of parks setting annual recreation visit records, 2025 = **26** parks (2025-01-01..2025-12-31) [DISCARD: Count of record parks; irrelevant.] quote: "26 parks, 6% of reporting parks, set a record for annual recreation visits."
  - p70 Share of reporting parks setting annual recreation visit records, 2025 = **6** % (2025-01-01..2025-12-31) [DISCARD: Share of record parks; irrelevant.] quote: "26 parks, 6% of reporting parks, set a record for annual recreation visits."
- dropped by code checks: 5 (period_end missing or unparseable: 5)

### d5 [capacity_consumption] Accommodation and campground occupancy

Hypothesis: Overnight stays in Yellowstone (lodges, campgrounds) are a component of visits. If occupancy rates and capacity are known for August 2026, they can be converted to visits using average party size and length of stay. This route may only cover overnight visitors, not day visitors.

Queries issued by the searcher: Yellowstone lodging occupancy August 2025 Xanterra; Yellowstone campground occupancy statistics capacity; Yellowstone August 2025 visitation 881,936 recreation visits NPS; Xanterra Yellowstone lodges number of rooms cabins capacity 2,000

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p71 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p72 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of p12.] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p73 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of p13.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p74 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p75 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p76 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p16.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p77 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p78 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p18.] quote: "2023 - 3,308,924"
  - p79 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p19.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p80 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p20.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.nps.gov/yell/planyourvisit/campgrounds.htm` -> **snapshot** (snapshot 20260731011505); points raw/verified 15/0
- `https://yellowstone.co/camping.htm` -> **snapshot** (snapshot 20260615181604); points raw/verified 0/0
- dropped by code checks: 15 (period_end missing or unparseable: 6; period_end 2026-09-13 after as_of: 1; period_end 2026-09-19 after as_of: 1; period_end 2026-10-17 after as_of: 2; period_end 2026-09-26 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-10-11 after as_of: 1; period_end 2026-10-12 after as_of: 1; period_end 2026-09-27 after as_of: 1)

### d6 [base_rates] Seasonal share of annual visits

Hypothesis: August typically accounts for a stable share of Yellowstone's annual recreation visits (e.g., around 20-25%). If a reliable estimate of total 2026 annual visits exists (from forecasts or year-to-date), the August share can be applied.

Queries issued by the searcher: Yellowstone annual visitation 2025 recreation visits; Yellowstone August share of annual recreation visits NPS; Yellowstone National Park 2024 annual visitation 4,744,000 recreation visits; NPS Visitor Use Statistics Yellowstone monthly report August 2025 881,936

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://oilcity.news/community/wyoming-community-2/2026/08/11/yellowstone-reports-958k-visitors-in-july-visits-down-2-from-2025/` -> **snapshot** (snapshot 20260812092842); points raw/verified 10/10
  - p81 Yellowstone National Park recreation visits in July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [DISCARD: Duplicate of p1.] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025"
  - p82 Yellowstone National Park recreation visits in July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [DISCARD: Duplicate of p2.] quote: "down 2% from July 2025, when 975,109 people visited the park."
  - p83 Yellowstone National Park recreation visits in July 2021 = **1,080,767** recreation visits (2021-07-01..2021-07-31) [DISCARD: Duplicate of p3.] quote: "an 11% decrease from July 2021, when the park hosted 1,080,767 visits"
  - p84 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "both part of Yellowstone's record-breaking year with over 4.8 million recreation visits"
  - p85 Yellowstone National Park year-to-date recreation visits in 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [DISCARD: Duplicate of p4.] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits"
  - p86 Yellowstone National Park year-to-date recreation visits in 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [DISCARD: Duplicate of p5.] quote: "down 1% from 2025's 2,666,031 recreation visits"
  - p87 Yellowstone National Park year-to-date recreation visits in 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Duplicate of p6.] quote: "down 1% from 2021's 2,668,765 recreation visits"
  - p88 Yellowstone National Park year-to-date recreation visits in 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [DISCARD: Duplicate of p7.] quote: "2024 - 2,626,091"
  - p89 Yellowstone National Park year-to-date recreation visits in 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [DISCARD: Duplicate of p8.] quote: "2023 - 2,462,535"
  - p90 Yellowstone National Park year-to-date recreation visits in 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Duplicate of p9.] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."

### d7 [forecasts_markets] Tourism forecasts and prediction markets

Hypothesis: Published forecasts for Yellowstone or national park tourism in summer 2026 may provide a direct estimate or a growth rate to apply to 2025 August. Prediction markets on total visits or specific thresholds could also be informative.

Queries issued by the searcher: Yellowstone visitation forecast 2026; prediction market Yellowstone national park visits 2026; Yellowstone National Park August 2025 visitation record recreation visits; Kalshi Yellowstone recreation visits 2026 market KXYELLVISITS

- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 12/12
  - p91 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p92 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of p12.] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p93 Year-over-year change in Yellowstone August recreation visits, August 2025 vs Au = **2** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11/p12 relationship.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p94 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of p13.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p95 Change in Yellowstone August recreation visits, August 2025 vs August 2021 = **4** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p13/p11 relationship.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p96 Yellowstone National Park record annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p97 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p98 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p16.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p99 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p100 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p18.] quote: "2023 - 3,308,924"
  - p101 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p19.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p102 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p20.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [attention] Search and social media interest

Hypothesis: Google Trends or social media mentions for Yellowstone in summer 2026 may correlate with visitation. If a stable relationship between search interest and visits exists, it can be used to adjust the baseline. Without a bridge, this is only context.

Queries issued by the searcher: Google Trends search interest predicts national park visitation correlation Yellowstone; Yellowstone National Park monthly visitation statistics August 2025 NPS; Google Trends "Yellowstone National Park" August 2024 search interest; search volume Google Trends national park attendance regression study

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p103 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p104 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of p12.] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p105 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of p13.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p106 Yellowstone National Park record-breaking year 2021 recreation visits (over 4.8  = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p10.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p107 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p108 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p16.] quote: "up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p109 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p110 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "2025 - 3,547,967"
  - p111 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p16.] quote: "2024 - 3,494,350"
  - p112 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p18.] quote: "2023 - 3,308,924"
  - p113 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p19.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p114 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "2021 - 3,590,609"
  - p115 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p20.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://businessupturn.com/usa/lifestyle/travel/most-searched-national-park-every-state-2026-yellowstone/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://pmc.ncbi.nlm.nih.gov/articles/instance/11009645/bin/pnas.2310417121.sapp.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### b1 [own_history] NPS monthly visitation series

Hypothesis: Obtaining the full monthly August recreation-visit series for Yellowstone (2015-2025, not just the 2021/2024/2025 values already kept) would let a naive or trend method use a longer, more stable August baseline and would reveal whether the 2021-2025 August values are representative. This directly strengthens the primary d1 route.

Queries issued by the searcher: NPS Visitor Use Statistics Yellowstone monthly recreation visits August 2015 2016 2017 2018 2019; Yellowstone National Park August visitation 2023 news release record; irma.nps.gov Stats Park Specific Reports Recreation Visitors By Month Yellowstone YELL; Yellowstone visitation statistics August 2021 news release 2022 monthly

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/23037.htm` -> **snapshot** (snapshot 20260617061634); points raw/verified 12/12
  - p116 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [keep: ] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p117 Yellowstone National Park recreation visits, August 2022 = **582,211** recreation visits (2022-08-01..2022-08-31) [keep: ] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p118 Yellowstone National Park recreation visits, August 2019 = **820,006** recreation visits (2019-08-01..2019-08-31) [keep: ] quote: "and a 3% increase from August 2019* (820,006 recreational visits)."
  - p119 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Superseded 2023 YTD vintage; conflicts with p18.] quote: "So far in 2023, the park has hosted 3,313,244 recreation visits"
  - p120 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "up 36% from 2022 (2,437,607 recreation visits)"
  - p121 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [keep: ] quote: "and up 6% from 2019 (3,114,697 recreation visits)."
  - p122 Yellowstone National Park year-to-date recreation visits through August 2023 (li = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p119.] quote: "2023 - 3,313,244"
  - p123 Yellowstone National Park year-to-date recreation visits through August 2022 (li = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p19.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21. Three entrances opened June 22.)"
  - p124 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p17.] quote: "2021 - 3,590,609"
  - p125 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p20.] quote: "2020 - 2,556,528 (The park was closed May 1 through May 17. Two entrances opened May 18 and the remaining three opened June 1.)"
  - p126 Yellowstone National Park year-to-date recreation visits through August 2019 (li = **3,114,697** recreation visits (2019-01-01..2019-08-31) [DISCARD: Duplicate of p121.] quote: "2019 - 3,114,697"
  - p127 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [keep: ] quote: "2018 - 3,136,241"
- `https://www.eastidahonews.com/2020/09/yellowstone-national-park-has-second-busiest-august-ever/` -> **snapshot** (snapshot 20201026073441); points raw/verified 9/9
  - p128 Yellowstone National Park recreation visits in August 2020 = **881,543** recreation visits (2020-08-01..2020-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,543 recreation visits in August 2020."
  - p129 Year-over-year percentage increase in Yellowstone recreation visits, August 2020 = **7.5** % (2020-08-01..2020-08-31) [DISCARD: Percent change already implied by p118/p128.] quote: "This is a 7.5% increase from August 2019, making it the second busiest August on record."
  - p130 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,546,373** recreation visits (2020-01-01..2020-08-31) [DISCARD: Superseded 2020 YTD vintage; conflicts with p20.] quote: "So far in 2020, the park has hosted 2,546,373 recreation visits, down 18% from the same period last year."
  - p131 Year-over-year percentage change in Yellowstone year-to-date recreation visits t = **18** % (2020-01-01..2020-08-31) [DISCARD: Percent change already implied by p130/p132.] quote: "So far in 2020, the park has hosted 2,546,373 recreation visits, down 18% from the same period last year."
  - p132 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [DISCARD: Duplicate of p121.] quote: "2019 - 3,114,697"
  - p133 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [DISCARD: Duplicate of p127.] quote: "2018 - 3,136,241"
  - p134 Yellowstone National Park year-to-date recreation visits through August 2017 = **3,232,707** recreation visits (2017-01-01..2017-08-31) [DISCARD: Duplicate of p127.] quote: "2017 - 3,232,707"
  - p135 Yellowstone National Park year-to-date recreation visits through August 2016 = **3,269,024** recreation visits (2016-01-01..2016-08-31) [DISCARD: Duplicate of p127.] quote: "2016 - 3,269,024"
  - p136 Yellowstone National Park year-to-date recreation visits through August 2015 = **3,133,965** recreation visits (2015-01-01..2015-08-31) [DISCARD: Duplicate of p127.] quote: "2015 - 3,133,965"
- `https://www.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260615211304); points raw/verified 13/13
  - p137 Yellowstone National Park average August visits, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p138 Yellowstone National Park August share of average annual visits, 2014-2018 avera = **20.89** % (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p139 Yellowstone National Park average July visits, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [DISCARD: July seasonal average; not needed for August target.] quote: "\| July \| 947,688 \| 23.57% \|"
  - p140 Yellowstone National Park average September visits, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [DISCARD: September seasonal average; not needed.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p141 Yellowstone National Park average June visits, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [DISCARD: June seasonal average; not needed.] quote: "\| June \| 780,652 \| 19.42% \|"
  - p142 Yellowstone National Park average May visits, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [DISCARD: May seasonal average; not needed.] quote: "\| May \| 401,449 \| 9.99% \|"
  - p143 Yellowstone National Park average October visits, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [DISCARD: October seasonal average; not needed.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p144 Yellowstone National Park average April visits, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [DISCARD: April seasonal average; not needed.] quote: "\| April \| 44,027 \| 1.10% \|"
  - p145 Yellowstone National Park average February visits, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [DISCARD: February seasonal average; not needed.] quote: "\| February \| 33,088 \| 0.82% \|"
  - p146 Yellowstone National Park average January visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [DISCARD: January seasonal average; not needed.] quote: "\| January \| 28,837 \| 0.72% \|"
  - p147 Yellowstone National Park average March visits, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [DISCARD: March seasonal average; not needed.] quote: "\| March \| 22,266 \| 0.55% \|"
  - p148 Yellowstone National Park average December visits, 2014-2018 average = **20,434** visits (2014-12-01..2018-12-31) [DISCARD: December seasonal average; not needed.] quote: "\| December \| 20,434 \| 0.51% \|"
  - p149 Yellowstone National Park average November visits, 2014-2018 average = **14,323** visits (2014-11-01..2018-11-30) [DISCARD: November seasonal average; not needed.] quote: "\| November \| 14,323 \| 0.36% \|"

### b2 [physical_flow] Entrance/vehicle counts

Hypothesis: August 2026 entrance-vehicle counts (or partial-month counts) would allow a vehicle-entries times occupancy decomposition, giving an independent check on the d1 baseline and capturing any within-August shock. This unlocks the d2 route, which currently has no 2026 vehicle data.

Queries issued by the searcher: Yellowstone traffic counter report August 2026 vehicle entries; Yellowstone National Park monthly visitation report 2026 vehicle entries by entrance; Yellowstone persons per vehicle multiplier NPS visitor use counting instructions Table 1; irma.nps.gov Yellowstone monthly public use report August 2026 West Gate vehicles

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://local.newsbreak.com/kifi-local-news-8-1276858/4891489150987-yellowstone-2026-summer-tourism-shows-decline-in-visitors` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grizzlyrv.com/which-yellowstone-entrance-should-rvers-stay-near/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] Park operations and closures

Hypothesis: Any August 2026 operational disruption (fire, road closure, reservation policy, government shutdown) would explain a deviation from the recent-August baseline. The kept road schedule shows normal access, but a targeted check for late-July/August 2026 incidents would confirm or falsify the no-shock assumption underlying the baseline methods.

Queries issued by the searcher: Yellowstone National Park alerts August 2026; Yellowstone fire activity summer 2026 road closure; Yellowstone National Park news release August 2026 road closure; Yellowstone visitation statistics 2026 monthly record July

- `https://www.nps.gov/yell/learn/management/current-fire-activity.htm` -> **snapshot** (snapshot 20260722025734); points raw/verified 6/0
- `https://www.nps.gov/yell/planyourvisit/situationreport.htm` -> **snapshot** (snapshot 20260618033531); points raw/verified 0/0
- `https://k2radio.com/ixp/102/p/yellowstone-road-closures-winter-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://deeparrival.com/news/yellowstone-old-faithful-overpass-delays-july-august-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (missing quote or value_as_written: 1; period_end missing or unparseable: 5)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p34', 'p81'] Same July 2026 figure (958,706) reported by NPS and echoed by oilcity.news; the news item is a secondary retransmission of the NPS release, not an independent measurement.
- corroborating: ['p2', 'p35', 'p82'] Same July 2025 comparison value (975,109) from NPS and news echo; single underlying source.
- corroborating: ['p3', 'p36', 'p83'] Same July 2021 record value (1,080,767); one underlying NPS measurement.
- corroborating: ['p4', 'p38', 'p85'] Same 2026 YTD-through-July value (2,635,384); news copy of NPS release.
- corroborating: ['p5', 'p39', 'p86'] Same 2025 YTD-through-July value (2,666,031).
- corroborating: ['p6', 'p40', 'p87'] Same 2021 YTD-through-July value (2,668,765).
- corroborating: ['p7', 'p41', 'p88'] Same 2024 YTD-through-July value (2,626,091).
- corroborating: ['p8', 'p42', 'p89'] Same 2023 YTD-through-July value (2,462,535).
- corroborating: ['p9', 'p43', 'p90'] Same 2022 YTD-through-July flood-affected value (1,855,396).
- corroborating: ['p11', 'p21', 'p51', 'p71', 'p91', 'p103'] August 2025 value (881,936) repeated across directions; all trace to the same NPS September 2025 release.
- corroborating: ['p12', 'p22', 'p52', 'p72', 'p92', 'p104'] August 2024 value (868,259) repeated; single NPS source.
- corroborating: ['p13', 'p23', 'p53', 'p73', 'p94', 'p105'] August 2021 value (921,844) repeated; single NPS source.
- corroborating: ['p15', 'p25', 'p28', 'p55', 'p75', 'p97', 'p107', 'p110'] 2025 YTD-through-August (3,547,967) repeated; same NPS release.
- corroborating: ['p16', 'p26', 'p29', 'p56', 'p76', 'p98', 'p108', 'p111'] 2024 YTD-through-August (3,494,350) repeated.
- corroborating: ['p17', 'p27', 'p32', 'p57', 'p77', 'p99', 'p109', 'p114'] 2021 YTD-through-August (3,590,609) repeated.
- corroborating: ['p18', 'p30', 'p58', 'p78', 'p100', 'p112'] 2023 YTD-through-August (3,308,924) repeated.
- corroborating: ['p19', 'p31', 'p59', 'p79', 'p101', 'p113'] 2022 YTD-through-August (2,437,607) repeated; flood-affected year.
- corroborating: ['p20', 'p33', 'p60', 'p80', 'p102', 'p115'] 2020 YTD-through-August (2,556,528) repeated; COVID-affected year.
- corroborating: ['p10', 'p14', 'p24', 'p37', 'p54', 'p74', 'p84', 'p96', 'p106'] 2021 annual record (~4.8 million) repeated; rounded figure, same source.
- corroborating: ['p44', 'p45', 'p46', 'p47', 'p48'] 2026 road-opening schedule shows all major park roads open through August 2026, i.e. no seasonal-access shock in the target month.
- corroborating: ['p49', 'p50'] Canyon-to-West-Thumb construction delays run only through 2026-08-14, so they affect at most the first half of August and are a minor negative factor.
- corroborating: ['p61', 'p62', 'p63'] NPS-wide 2025 total and its 2.7% decline are internally consistent; useful only as weak context for a national softness in park visitation.
- corroborating: ['p66', 'p67', 'p68'] NPS-wide visitor-hours and overnight-stay declines in 2025 are consistent with the visit decline; context only.
- corroborating: ['p64', 'p65', 'p69', 'p70'] Reporting-unit counts and record-park share are internally consistent NPS system statistics; context only.
- conflicting: ['p1', 'p11'] Not a true conflict: July 2026 is down 2% vs July 2025 while August 2025 was up 2% vs August 2024. The two months have different seasonal levels and different year-over-year momentum, so the August 20
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p34', 'p81'] Same July 2026 count; news is a copy of NPS.
- corroborating: ['p2', 'p35', 'p82'] Same July 2025 count; shared NPS origin.
- corroborating: ['p3', 'p36', 'p83'] Same July 2021 record count; shared origin.
- corroborating: ['p4', 'p38', 'p85'] Same 2026 YTD-through-July; shared origin.
- corroborating: ['p5', 'p39', 'p86'] Same 2025 YTD-through-July.
- corroborating: ['p6', 'p40', 'p87'] Same 2021 YTD-through-July.
- corroborating: ['p7', 'p41', 'p88'] Same 2024 YTD-through-July.
- corroborating: ['p8', 'p42', 'p89'] Same 2023 YTD-through-July.
- corroborating: ['p9', 'p43', 'p90'] Same 2022 YTD-through-July with flood context.
- corroborating: ['p10', 'p14', 'p24', 'p37', 'p54', 'p74', 'p84', 'p96', 'p106'] Repeated 2021 record-year fact; same NPS source.
- corroborating: ['p11', 'p21', 'p51', 'p71', 'p91', 'p103'] Same August 2025 count (881,936); shared NPS origin.
- corroborating: ['p12', 'p22', 'p52', 'p72', 'p92', 'p104'] Same August 2024 count (868,259).
- corroborating: ['p13', 'p23', 'p53', 'p73', 'p94', 'p105'] Same August 2021 count (921,844).
- corroborating: ['p15', 'p25', 'p28', 'p55', 'p75', 'p97', 'p107', 'p110'] Same 2025 YTD-through-August (3,547,967).
- corroborating: ['p16', 'p26', 'p29', 'p56', 'p76', 'p98', 'p108', 'p111'] Same 2024 YTD-through-August (3,494,350).
- corroborating: ['p17', 'p27', 'p32', 'p57', 'p77', 'p99', 'p109', 'p114'] Same 2021 YTD-through-August (3,590,609).
- corroborating: ['p18', 'p30', 'p58', 'p78', 'p100', 'p112'] Same 2023 YTD-through-August (3,308,924).
- corroborating: ['p19', 'p31', 'p59', 'p79', 'p101', 'p113'] Same 2022 YTD-through-August (2,437,607).
- corroborating: ['p20', 'p33', 'p60', 'p80', 'p102', 'p115'] Same 2020 YTD-through-August (2,556,528).
- corroborating: ['p116', 'p119', 'p122'] August 2023 count and 2023 YTD from same NPS release; note p119 (3,313,244) differs slightly from p18 (3,308,924), a revision.
- corroborating: ['p117', 'p120', 'p123'] August 2022 and 2022 YTD from same release.
- corroborating: ['p118', 'p121', 'p126'] August 2019 and 2019 YTD from same release.
- corroborating: ['p128', 'p130'] August 2020 and 2020 YTD from same news report; p130 (2,546,373) differs slightly from p20 (2,556,528), a revision.
- corroborating: ['p137', 'p138'] August 2014-2018 average and its annual share from same NPS table.
- corroborating: ['p61', 'p62', 'p63'] NPS 2025 annual total and its decline from 2024; same release.
- corroborating: ['p44', 'p45', 'p46', 'p47', 'p48'] 2026 road-opening schedule shows normal summer access; no August closure indicated.
- corroborating: ['p49', 'p50'] Canyon-West Thumb construction delays through Aug 14, 2026; minor friction, not closure.
- corroborating: ['p116', 'p117', 'p118'] Historical August levels 2019-2023 bracket recent August values.
- conflicting: ['p11', 'p137'] Recent August (868k-922k) exceeds the 2014-2018 average (839,787), so the old seasonal share understates current August levels.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|

Rejected by code:

- a1 August 2026 recreation visits as a fraction of August 2025 recreation visits: target-like: names the target period (2026)
- a2 August 2026 recreation visits as a fraction of August 2024 recreation visits: target-like: names the target period (2026)
- a3 August 2026 recreation visits as a fraction of August 2021 recreation visits: target-like: names the target period (2026)

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a1: assumption a1 was rejected (target-like: names the target period (2026)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a2: assumption a2 was rejected (target-like: names the target period (2026)) |
| m3 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: names the target period (2026)) |
| m4 | series_naive | 865,528 |  | [2022, 2023, 2024, 2025] | 0.178 | 0.50 | backtest |  |
| m5 | yoy_scaling | 867,100 |  | [] |  | 0.50 | median_of_backtested |  |
| m6 | ratio | n/a |  | [] |  | 0.00 |  | signal has no value for 2026 |

Result: central **866,314**, 80% interval [650,499, 1,153,728], basis historical_errors, weight rule inverse_backtest_error, weight on methods that use assumptions 0.00

## Final answer

The best estimate for recreation visits to Yellowstone National Park in August 2026, as reported in NPS monthly visitation statistics, is 866,314 recreation visits. The supplied interval is 650,499 to 1,153,728, a model-based range conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate combines 2 methods. The main anchors are a mean of recent August values (865,528, weight 50%) and a year-over-year scaling of last August by the July 2026/July 2025 ratio (867,100, weight 50%). The other methods were rejected or given no weight.

Observed inputs are prior August and July figures; the [n] August value is future and depends on transferring July softness to August. The main risk is that July and August shocks differ. The most useful missing evidence would be partial August 2026 counts or park-level operational data.

Key assumptions: none (every formula input is an observed data point).

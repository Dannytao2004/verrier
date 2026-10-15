# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park, as counted by the National Park Service's official monthly visitation statistics (reported in the NPS Visitor Use Statistics database and monthly public use reports). | unit recreation visits (person-visits) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), Visitor Use Statistics program / Public Use Statistics Office

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS official monthly visitation statistics for Yellowstone National Park

Hypothesis: September 2026 visitation will be similar to September 2023-2025, adjusted for any known trend or shocks. The 2-3 previous Septembers provide a baseline and recent trend.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September 2025; NPS visitor use statistics Yellowstone September 2024 recreation visits; Yellowstone visitation statistics September 2025 recreation visits 839,579; Yellowstone visitation statistics August 2026 recreation visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-national-park-september-visits-up-2-from-last-year` -> **snapshot** (snapshot 20241010002924); points raw/verified 9/9
  - p1 Yellowstone National Park recreation visits, September 2024 = **852,435** recreation visits (2024-09-01..2024-09-30) [keep: Direct September 2024 Yellowstone recreation visits, most recent September baseline.] quote: "Yellowstone National Park hosted 852,435 recreation visits in September 2024."
  - p2 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: Direct September 2023 Yellowstone recreation visits, prior-year baseline.] quote: "This is a 2% increase from September 2023 (838,458 recreational visits)."
  - p3 Yellowstone National Park recreation visits, September 2021 = **882,078** recreation visits (2021-09-01..2021-09-30) [keep: Direct September 2021 Yellowstone recreation visits, useful for trend but older.] quote: "This September's visitation showed an 3% decrease from September 2021 (882,078 recreation visits)."
  - p4 Yellowstone National Park year-to-date recreation visits through September 2024 = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: Year-to-date through September 2024, supports trend context.] quote: "So far in 2024, the park has hosted 4,349,689 recreation visits, up 5% from 2023 (4,147,382 recreation visits)"
  - p5 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,147,382** recreation visits (2023-01-01..2023-09-30) [keep: Year-to-date through September 2023, supports trend context.] quote: "2023 - 4,147,382"
  - p6 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [keep: Year-to-date through September 2022, flood-affected but useful context.] quote: "2022 - 3,005,194 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p7 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: Year-to-date through September 2021, supports trend context.] quote: "2021 - 4,472,687"
  - p8 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [keep: Year-to-date through September 2020, COVID-affected but useful context.] quote: "2020 - 3,393,642 (The park was closed March 24 through May 17 due to COVID. Two entrances opened on May 18 and the remaining three opened on June 1.)"
  - p9 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [keep: Year-to-date through September 2019, pre-COVID baseline context.] quote: "2019 - 3,807,815"
- `https://buckrail.com/ynp-september-visitation-up-2-from-last-year/` -> **snapshot** (snapshot 20250904205842); points raw/verified 12/11
  - p10 Yellowstone National Park recreation visits in September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: Duplicate of p2 but from independent source; corroborates September 2023.] quote: "838,458 recreation visits in September 2023"
  - p11 Yellowstone National Park recreation visits in September 2021 = **882,078** recreation visits (2021-09-01..2021-09-30) [keep: Duplicate of p3 but from independent source; corroborates September 2021.] quote: "September 2021's 882,078 visits"
  - p12 Yellowstone National Park year-to-date recreation visits through September 2024 = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: Duplicate of p4; corroborates year-to-date 2024.] quote: "YNP hosted 4,349,689 recreation visits this year through September"
  - p13 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,147,382** recreation visits (2023-01-01..2023-09-30) [keep: Duplicate of p5; corroborates year-to-date 2023.] quote: "2023 saw 4,147,382 visits"
  - p14 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: Duplicate of p7; corroborates year-to-date 2021.] quote: "2021, which hosted 4,472,687 visits"
  - p15 Yellowstone National Park year-to-date recreation visits through September 2024  = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: Duplicate of p4; corroborates year-to-date 2024.] quote: "2024: 4,349,689"
  - p16 Yellowstone National Park year-to-date recreation visits through September 2023  = **4,147,382** recreation visits (2023-01-01..2023-09-30) [keep: Duplicate of p5; corroborates year-to-date 2023.] quote: "2023: 4,147,382"
  - p17 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [keep: Duplicate of p6; corroborates year-to-date 2022.] quote: "2022: 3,005,194"
  - p18 Yellowstone National Park year-to-date recreation visits through September 2021  = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: Duplicate of p7; corroborates year-to-date 2021.] quote: "2021: 4,472,687"
  - p19 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [keep: Duplicate of p8; corroborates year-to-date 2020.] quote: "2020: 3,393,642"
  - p20 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [keep: Duplicate of p9; corroborates year-to-date 2019.] quote: "2019: 3,807,815"
- dropped by code checks: 1 (period_end 2026-09-30 after as_of: 1)

### d2 [related_series] NPS monthly visitation for other nearby or comparable parks (Grand Teton, Glacier, Zion, Yosemite) and total NPS-wide visitation

Hypothesis: Yellowstone visitation often moves with regional and national park visitation trends. If other parks show a strong increase or decrease in September 2026, Yellowstone likely follows. Also, Grand Teton is a close substitute/complement and its September numbers can indicate regional travel demand.

Queries issued by the searcher: Grand Teton National Park monthly visitation September 2025 NPS statistics; NPS total recreation visits September 2025 Visitor Use Statistics; Glacier National Park September 2025 visitation statistics NPS; NPS monthly public use report August 2026 recreation visits

- `https://irma.nps.gov/Stats/` -> **snapshot** (snapshot 20260826152358); points raw/verified 0/0
- `https://www.nps.gov/subjects/socialscience/visitor-use-statistics-dashboard.htm` -> **snapshot** (snapshot 20260904180349); points raw/verified 15/8
  - p21 Total NPS recreation visits, calendar year 2025 = **323,000,000** recreation visits (2025-01-01..2025-12-31) [keep: National NPS 2025 total, useful for national trend signal.] quote: "The National Park Service reported 323 million recreation visits in calendar year 2025."
  - p22 Decrease in NPS recreation visits from 2024 to 2025 = **8,850,000** recreation visits (2025-01-01..2025-12-31) [keep: National NPS 2025 decline, useful for national trend signal.] quote: "This is a decrease of 8.85 million recreation visits, or 2.7%, from the record year in 2024."
  - p23 Percent decrease in NPS recreation visits from 2024 to 2025 = **2.7** % (2025-01-01..2025-12-31) [keep: National NPS 2025 percent decline, useful for national trend signal.] quote: "This is a decrease of 8.85 million recreation visits, or 2.7%, from the record year in 2024."
  - p24 Recreation visitor hours, calendar year 2025 = **1,390,000,000** visitor hours (2025-01-01..2025-12-31) [keep: National visitor hours 2025, secondary context.] quote: "Recreation visitor hours were 1.39 billion; a decrease of 0.7% from 2024."
  - p25 Percent decrease in recreation visitor hours from 2024 to 2025 = **0.7** % (2025-01-01..2025-12-31) [keep: National visitor hours decline 2025, secondary context.] quote: "Recreation visitor hours were 1.39 billion; a decrease of 0.7% from 2024."
  - p26 Percent decrease in overnight stays from 2024 to 2025 = **2.4** % (2025-01-01..2025-12-31) [keep: National overnight stays decline 2025, secondary context.] quote: "There was a 2.4% decrease from 2024 for overnight stays."
  - p27 Number of parks setting annual recreation visit records = **26** parks (2025-01-01..2025-12-31) [keep: Number of parks setting records 2025, context on national trend.] quote: "26 parks, 6% of reporting parks, set a record for annual recreation visits."
  - p28 Percent of reporting parks setting annual recreation visit records = **6** % (2025-01-01..2025-12-31) [keep: Percent of parks setting records 2025, context on national trend.] quote: "26 parks, 6% of reporting parks, set a record for annual recreation visits."
- `https://tourism.az.gov/wp-content/uploads/2025/12/NPS-September-2025-12-26-25.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://hungryhorsenews.com/news/2025/dec/23/glacier-park-visitation-tops-3-million-again-in-2025/` -> **snapshot** (snapshot 20251226002825); points raw/verified 8/8
  - p29 Glacier National Park estimated visitation through October 2025 = **3,086,000** people (2025-01-01..2025-10-31) [keep: Glacier 2025 visitation, regional signal.] quote: "with 3.086 million people estimated to have visited Glacier through October."
  - p30 Glacier National Park visitation change through October 2025 vs last season = **2.5** % (2025-01-01..2025-10-31) [keep: Glacier 2025 change, regional signal.] quote: "Through October, visitation is off slightly compared to last season by just 2.5%."
  - p31 Glacier National Park October visitation change 2025 = **22.7** % (2025-10-01..2025-10-31) [keep: Glacier October 2025 change, regional signal.] quote: "All told visitation in October was down 22.7% as snows closed the alpine section of the Going-to-the-Sun Road on Oct. 11."
  - p32 Glacier National Park September visitation decline vs previous year = **53,000** visitors (2025-09-01..2025-09-30) [keep: Glacier September 2025 decline, regional signal for September.] quote: "September was also down from the previous year about 53,000 visitors, as the park had its reservation system through the entire month"
  - p33 Glacier National Park October 2025 visits = **127,537** visits (2025-10-01..2025-10-31) [keep: Glacier October 2025 visits, regional context.] quote: "All told, October saw 127,537 visits, while September saw 552,479."
  - p34 Glacier National Park September 2025 visits = **552,479** visits (2025-09-01..2025-09-30) [keep: Glacier September 2025 visits, regional September signal.] quote: "All told, October saw 127,537 visits, while September saw 552,479."
  - p35 Glacier National Park total visitation last year (2024) = **3,208,000** people (2024-01-01..2024-12-31) [keep: Glacier 2024 total, regional context.] quote: "Last year the total was 3.208 million for the year."
  - p36 Glacier National Park busiest year ever visitation (2017) = **3,305,000** people (2017-01-01..2017-12-31) [keep: Glacier record year, regional context.] quote: "The busiest year ever was 2017, when 3.305 million people visited."
- `https://catalog.data.gov/dataset/nps-visitor-use-statistics-data-package-2025` -> **snapshot** (snapshot 20260823152220); points raw/verified 0/0
- dropped by code checks: 7 (period_end missing or unparseable: 7)

### d3 [physical_flow] State departments of transportation and park entrance station counts

Hypothesis: Vehicle traffic counts on highways leading to Yellowstone (e.g., US-89, US-191, US-20) and entrance station vehicle counts correlate with park visitation. Higher traffic in September 2026 implies higher visitation.

Queries issued by the searcher: Wyoming DOT traffic counts Yellowstone September; Montana DOT traffic data West Yellowstone September; Yellowstone entrance station vehicle counts September; Yellowstone National Park monthly visitation statistics September 2025

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 15/15
  - p37 Yellowstone East entrance vehicle entries, Friday September 3, 2021 = **882** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone East entrance vehicle count, physical flow signal.] quote: "\| East \| 882 \| 725 \| 22% \|"
  - p38 Yellowstone North entrance vehicle entries, Friday September 3, 2021 = **1,718** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone North entrance vehicle count, physical flow signal.] quote: "\| North \| 1,718 \| 1,361 \| 26% \|"
  - p39 Yellowstone Northeast entrance vehicle entries, Friday September 3, 2021 = **477** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone Northeast entrance vehicle count, physical flow signal.] quote: "\| Northeast \| 477 \| 522 \| -9% \|"
  - p40 Yellowstone South entrance vehicle entries, Friday September 3, 2021 = **1,750** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone South entrance vehicle count, physical flow signal.] quote: "\| South \| 1,750 \| 1,189 \| 47% \|"
  - p41 Yellowstone West entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone West entrance vehicle count, physical flow signal.] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p42 Yellowstone parkwide total vehicle entries, Friday September 3, 2021 = **8,945** vehicles (2021-09-03..2021-09-03) [keep: Yellowstone parkwide total vehicle entries, physical flow signal.] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p43 Yellowstone East entrance vehicle entries, Saturday September 4, 2021 = **1,018** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone East entrance vehicle count, physical flow signal.] quote: "\| East \| 1,018 \| 919 \| 11% \|"
  - p44 Yellowstone North entrance vehicle entries, Saturday September 4, 2021 = **2,152** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone North entrance vehicle count, physical flow signal.] quote: "\| North \| 2,152 \| 1,771 \| 22% \|"
  - p45 Yellowstone Northeast entrance vehicle entries, Saturday September 4, 2021 = **710** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone Northeast entrance vehicle count, physical flow signal.] quote: "\| Northeast \| 710 \| 687 \| 3% \|"
  - p46 Yellowstone South entrance vehicle entries, Saturday September 4, 2021 = **1,960** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone South entrance vehicle count, physical flow signal.] quote: "\| South \| 1,960 \| 896 \| 119% \|"
  - p47 Yellowstone West entrance vehicle entries, Saturday September 4, 2021 = **5,222** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone West entrance vehicle count, physical flow signal.] quote: "\| West \| 5,222 \| 4,640 \| 13% \|"
  - p48 Yellowstone parkwide total vehicle entries, Saturday September 4, 2021 = **11,062** vehicles (2021-09-04..2021-09-04) [keep: Yellowstone parkwide total vehicle entries, physical flow signal.] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p49 Yellowstone East entrance vehicle entries, Sunday September 5, 2021 = **1,506** vehicles (2021-09-05..2021-09-05) [keep: Yellowstone East entrance vehicle count, physical flow signal.] quote: "\| East \| 1,506 \| 1,204 \| 25% \|"
  - p50 Yellowstone North entrance vehicle entries, Sunday September 5, 2021 = **2,435** vehicles (2021-09-05..2021-09-05) [keep: Yellowstone North entrance vehicle count, physical flow signal.] quote: "\| North \| 2,435 \| 1,964 \| 24% \|"
  - p51 Yellowstone parkwide total vehicle entries, Sunday September 5, 2021 = **12,380** vehicles (2021-09-05..2021-09-05) [keep: Yellowstone parkwide total vehicle entries, physical flow signal.] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
- `https://dot.state.wy.us/files/live/sites/wydot/files/shared/Planning/Traffic%20Data%20ATR%20%26%20VMB%20Book%20PDF` -> **dropped** (no snapshot <= as_of; live http 404); points raw/verified -/-
- `https://192.146.215.45/sites/wydot/home/planning_projects/Traffic_Data.html` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://mdt.mt.gov/other/webdata/external/planning/traffic_reports/Montana_TM_Handbook.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d4 [capacity_consumption] Local accommodation providers, campgrounds, and tourism businesses

Hypothesis: Occupancy rates, bookings, and sales tax receipts in gateway communities (West Yellowstone, Gardiner, Cody, Jackson) reflect park visitation. Higher occupancy in September 2026 suggests higher visitation.

Queries issued by the searcher: Yellowstone National Park recreation visits September 2026 monthly public use statistics; West Yellowstone hotel occupancy September 2025 lodging tax revenue; Montana lodging facility use tax revenue September 2025 West Yellowstone; West Yellowstone chamber of commerce occupancy September 2026

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.wyomingnews.com/news/local_news/yellowstone-national-park-reports-september-2026-visitation-statistics/article_3df9c932-70de-46b1-b898-372` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-
- `https://missoulian.com/news/state-regional/article_3e735d1b-fa36-5f8d-85d2-f3250e609131.html` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-06 > as_of); points raw/verified -/-
- `https://sheridanmedia.com/news/253113/yellowstone-national-park-september-2026-visitor-numbers-are-up-from-previous-year/` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-13 > as_of); points raw/verified -/-

### d5 [administrative] National Park Service permits, reservations, and park management records

Hypothesis: Backcountry permits, campground reservations, and tour permits issued for September 2026 indicate demand. Also, any changes in reservation policies or fees could affect visitation.

Queries issued by the searcher: Yellowstone backcountry permits September statistics NPS; Yellowstone campground reservations September 2025 Recreation.gov; Yellowstone visitation statistics September 2025 monthly report NPS; NPS Visitor Use Statistics Yellowstone monthly public use report backcountry overnight stays; Yellowstone commercial tour permits statistics 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-
- `https://www.recreation.gov/permits/4675323` -> **snapshot** (snapshot 20260710045718); points raw/verified 0/0
- `https://home.nps.gov/yell/planyourvisit/backcountryhiking.htm/index.htm` -> **snapshot** (snapshot 20260119191931); points raw/verified 15/0
- `https://www.yellowstonepark.com/park/faqs/reserve-hotels-campgrounds/` -> **snapshot** (snapshot 20230328113913); points raw/verified 1/1
  - p52 Yellowstone visitors in a single month (August) = **900,000** visitors (2021-08-01..2021-08-31) [keep: Yellowstone August 2021 monthly visitors, context on peak season.] quote: "August is an especially busy time for the park, with more than 900,000 visitors in a single month in 2021."
- dropped by code checks: 15 (period_end missing or unparseable: 13; value_as_written not in quote: 2)

### d6 [attention] Online search interest, social media, and news coverage

Hypothesis: Google Trends search interest for 'Yellowstone National Park' in September 2026 relative to previous Septembers correlates with actual visitation. Increased attention (e.g., due to a viral event) may boost visits.

Queries issued by the searcher: Yellowstone National Park recreation visits September NPS visitor use statistics; Google Trends Yellowstone National Park September; Yellowstone National Park news September 2026; Yellowstone National Park September 2025 visitation 839,579 recreation visits

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://nypost.com/2026/09/05/us-news/10-best-national-parks-in-america-ranked-as-yellowstone-no-1/` -> **snapshot** (snapshot 20260906015105); points raw/verified 13/0
- `https://www.newsbreak.com/news/4906159277072-the-most-searched-national-park-in-every-state-reveals-one-clear-favorite` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-24 > as_of); points raw/verified -/-
- `https://buckrail.com/yellowstone-visitation-september-sees-3-bump/` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-
- dropped by code checks: 13 (period_end missing or unparseable: 13)

### d7 [shocks] Weather, wildfires, road closures, and policy changes

Hypothesis: September visitation is highly sensitive to weather (early snow, heat), wildfires (smoke, closures), and road construction. A major closure or poor weather in September 2026 would reduce visitation; good weather would increase it.

Queries issued by the searcher: Yellowstone National Park September 2026 recreation visits NPS visitor use statistics; Yellowstone September 2026 weather road closures wildfire; Yellowstone National Park September 2025 visitation 839,579 NPS; Yellowstone 2026 reservation requirement entrance policy change; Yellowstone National Park road construction closures 2026 season; Yellowstone wildfire 2026 smoke closure

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-
- `https://buckrail.com/yellowstone-visitation-september-sees-3-bump/` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-
- `https://www.wyomingnews.com/news/local_news/yellowstone-national-park-reports-september-2026-visitation-statistics/article_3df9c932-70de-46b1-b898-372` -> **dropped** (no snapshot <= as_of; live page dated 2026-10-07 > as_of); points raw/verified -/-

### d8 [forecasts_markets] Tourism forecasts, economic projections, and prediction markets

Hypothesis: Published forecasts for national park tourism or Wyoming/Montana travel in 2026 can provide a baseline expectation. Prediction markets (if any) on Yellowstone visitation would directly reflect expectations.

Queries issued by the searcher: Wyoming tourism forecast 2026; Montana tourism forecast 2026; Yellowstone visitation prediction market 2026; Yellowstone National Park visitation forecast 2026

- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **live_dated** (page date 2026-08-17); points raw/verified 13/0
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://scholarworks.umt.edu/cgi/viewcontent.cgi?params=%2Fcontext%2Fitrr_pubs%2Farticle%2F1499%2F&path_info=2026_BBER_Economic_Outlook_Seminar.pdf` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-
- `https://montanaeconomist.org/a-steady-year-amid-shifting-trends/` -> **snapshot** (snapshot 20260511092735); points raw/verified 15/15
  - p53 Canadian border crossings decline year-to-date, Montana = **17** % (2025-01-01..2025-11-30) [keep: Montana Canadian border crossings decline, regional demand signal.] quote: "Canadian border crossings were down 17% year-to-date (as of November 2025)"
  - p54 Canadian border crossings decline in third quarter 2025, Montana = **24** % (2025-07-01..2025-09-30) [keep: Montana Q3 2025 border crossings decline, regional demand signal.] quote: "nearly 24% in the third quarter of 2025"
  - p55 Tourism businesses reporting increased visitor volume in 2025, Montana = **31** % (2025-01-01..2025-12-31) [keep: Montana tourism business volume 2025, regional demand signal.] quote: "Only 31% of businesses reported increased visitor volume in 2025 compared to 43% in 2024"
  - p56 Tourism businesses reporting increased visitor volume in 2024, Montana = **43** % (2024-01-01..2024-12-31) [keep: Montana tourism business volume 2024, regional demand signal.] quote: "Only 31% of businesses reported increased visitor volume in 2025 compared to 43% in 2024"
  - p57 Tourism businesses experiencing visitor volume declines in 2024, Montana = **27** % (2024-01-01..2024-12-31) [keep: Montana tourism business declines 2024, regional demand signal.] quote: "those experiencing declines rose sharply from 27% to 44%"
  - p58 Tourism businesses experiencing visitor volume declines in 2025, Montana = **44** % (2025-01-01..2025-12-31) [keep: Montana tourism business declines 2025, regional demand signal.] quote: "those experiencing declines rose sharply from 27% to 44%"
  - p59 Tourism businesses expecting customer volume to increase or remain steady in 202 = **81** % (2025-01-01..2025-12-31) [keep: Montana tourism expectations 2025, regional demand signal.] quote: "although 81% expect customer volume to increase or remain steady in 2025, this marks a decline from 87% last year"
  - p60 Tourism businesses expecting customer volume to increase or remain steady in 202 = **87** % (2024-01-01..2024-12-31) [keep: Montana tourism expectations 2024, regional demand signal.] quote: "this marks a decline from 87% last year"
  - p61 Tourism businesses anticipating no change in customer volume, Montana = **44** % (2025-01-01..2025-12-31) [keep: Montana tourism no-change expectation, regional demand signal.] quote: "with 44% anticipating no change at all"
  - p62 Tourism operators citing rising costs as biggest operational hurdle, Montana = **67** % (2025-01-01..2025-12-31) [keep: Montana tourism cost hurdle, regional demand signal.] quote: "67% of operators cited rising costs for fuel, goods, and services as their biggest operational hurdle"
  - p63 Tourism operators citing workforce shortages, Montana = **46** % (2025-01-01..2025-12-31) [keep: Montana tourism workforce hurdle, regional demand signal.] quote: "followed by workforce shortages (46%)"
  - p64 Tourism operators citing visitor behavior changes, Montana = **37** % (2025-01-01..2025-12-31) [keep: Montana tourism behavior change, regional demand signal.] quote: "visitor behavior changes (37%)"
  - p65 Tourism operators citing employee housing constraints, Montana = **24** % (2025-01-01..2025-12-31) [keep: Montana tourism housing constraint, regional demand signal.] quote: "and employee housing constraints (24%)"
  - p66 Tourism operators citing weather and climate impacts, Montana = **24** % (2025-01-01..2025-12-31) [keep: Montana tourism weather impact, regional demand signal.] quote: "Additional pressures included weather and climate impacts (24%)"
  - p67 Tourism operators citing infrastructure or transportation issues, Montana = **9** % (2025-01-01..2025-12-31) [keep: Montana tourism infrastructure issue, regional demand signal.] quote: "and infrastructure or transportation issues (9%)"
- `https://www.sheridanwyoming.org/wp-content/uploads/2026/08/2026-Q3-Summer-Industry-Update-WEB.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 13 (period_end 2026-10-15 after as_of: 1; period_end 2026-12-31 after as_of: 1; period_end missing or unparseable: 11)

### b1 [base_rates] Yellowstone September visitation as a share of annual visitation

Hypothesis: September typically accounts for a stable fraction of Yellowstone's annual recreation visits, allowing a September estimate from a projected annual total.

Queries issued by the searcher: Yellowstone annual visitation statistics NPS Visitor Use Statistics; Yellowstone National Park monthly public use report September recreation visits; Yellowstone September share of annual recreation visits NPS; Yellowstone National Park reports September 2025 visitation statistics nps.gov; nps.gov yell planyourvisit visitationstats annual visitation table 2015 2024; irma.nps.gov Stats Recreation Visits by Month Yellowstone NP 1979 report

- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p68 Yellowstone National Park average September recreation visits (2014-2018) = **663,651** recreation visits (person-visits) (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p69 Yellowstone National Park September share of average annual visits (2014-2018) = **16.51** % (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p70 Yellowstone National Park average January recreation visits (2014-2018) = **28,837** recreation visits (person-visits) (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p71 Yellowstone National Park average February recreation visits (2014-2018) = **33,088** recreation visits (person-visits) (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p72 Yellowstone National Park average March recreation visits (2014-2018) = **22,266** recreation visits (person-visits) (2014-03-01..2018-03-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p73 Yellowstone National Park average April recreation visits (2014-2018) = **44,027** recreation visits (person-visits) (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p74 Yellowstone National Park average May recreation visits (2014-2018) = **401,449** recreation visits (person-visits) (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p75 Yellowstone National Park average June recreation visits (2014-2018) = **780,652** recreation visits (person-visits) (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p76 Yellowstone National Park average July recreation visits (2014-2018) = **947,688** recreation visits (person-visits) (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p77 Yellowstone National Park average August recreation visits (2014-2018) = **839,787** recreation visits (person-visits) (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p78 Yellowstone National Park average October recreation visits (2014-2018) = **223,777** recreation visits (person-visits) (2014-10-01..2018-10-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p79 Yellowstone National Park average November recreation visits (2014-2018) = **14,323** recreation visits (person-visits) (2014-11-01..2018-11-30) [keep: ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p80 Yellowstone National Park average December recreation visits (2014-2018) = **20,434** recreation visits (person-visits) (2014-12-01..2018-12-31) [keep: ] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://nbcmontana.com/topic/Recreation%20visits` -> **snapshot** (snapshot 20250612132434); points raw/verified 13/13
  - p81 Yellowstone National Park recreation visits in May 2025 = **566,363** recreation visits (2025-05-01..2025-05-31) [keep: ] quote: "Yellowstone National Park hosted 566,363 recreation visits in May 2025, this is up 8% from May of 2024."
  - p82 Yellowstone National Park recreation visits in October 2024 = **346,025** recreation visits (2024-10-01..2024-10-31) [keep: ] quote: "Yellowstone National Park saw a 16% increase in October visits with 346,025 recreational visits in 2024, up from 299,127 in 2023."
  - p83 Yellowstone National Park recreation visits in October 2023 = **299,127** recreation visits (2023-10-01..2023-10-31) [keep: ] quote: "Yellowstone National Park saw a 16% increase in October visits with 346,025 recreational visits in 2024, up from 299,127 in 2023."
  - p84 Yellowstone National Park recreation visits in September 2024 = **852,435** recreation visits (2024-09-01..2024-09-30) [keep: ] quote: "Yellowstone National Park announced they hosted852,435 recreation visitors in Sept. 2024, which is a 2% increase from last year's total of838,458 visits."
  - p85 Yellowstone National Park recreation visits in September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: ] quote: "Yellowstone National Park announced they hosted852,435 recreation visitors in Sept. 2024, which is a 2% increase from last year's total of838,458 visits."
  - p86 Yellowstone National Park recreation visits in August 2024 = **871,163** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "Yellowstone National Park hosted 871,163 recreation visits in August 2024, up 3% from August 2023 (846,389 recreation visits)."
  - p87 Yellowstone National Park recreation visits in August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [keep: ] quote: "Yellowstone National Park hosted 871,163 recreation visits in August 2024, up 3% from August 2023 (846,389 recreation visits)."
  - p88 Yellowstone National Park recreation visits in July 2024 = **992,352** recreation visits (2024-07-01..2024-07-31) [keep: ] quote: "Yellowstone National Park hosted 992,352 recreation visits in July 2024, up 2% from Jul"
  - p89 Yellowstone National Park recreation visits in June 2024 = **914,612** recreation visits (2024-06-01..2024-06-30) [keep: ] quote: "Yellowstone National Park hosted 914,612 recreation visits in June 2024, up 8% from June 2023."
  - p90 Yellowstone National Park year-to-date recreation visits in 2024 = **1,633,739** recreation visits (2024-01-01..2024-06-30) [keep: ] quote: "The park has hosted 1,633,739 visitors this year, which is up 9% f"
  - p91 Yellowstone National Park recreation visits in May 2024 = **522,450** recreation visits (2024-05-01..2024-05-31) [keep: ] quote: "There were 522,450 visits in May 2024, compared to 454,262 visits i"
  - p92 Yellowstone National Park recreation visits in May 2023 = **454,262** recreation visits (2023-05-01..2023-05-31) [keep: ] quote: "There were 522,450 visits in May 2024, compared to 454,262 visits i"
  - p93 Glacier National Park recreation visits in 2023 = **2,933,616** recreation visits (2023-01-01..2023-12-31) [keep: ] quote: "Glacier National Park had2,933,616 recreation visits in 2023, placing in the top 15 most visited national parks."

### b2 [base_rates] Relationship between national park visitation trends and Yellowstone visitation

Hypothesis: Yellowstone September visitation moves with national NPS visitation with a stable elasticity, so the 2025 national decline can be applied to Yellowstone.

Queries issued by the searcher: NPS national visitation statistics annual recreation visits 2015-2025; Yellowstone National Park annual recreation visits 2015-2025; NPS 2025 annual visitation report national recreation visits 323 million press release; Yellowstone visitation statistics September 2026 recreation visits

- `https://www.nps.gov/aboutus/visitation-numbers.htm` -> **snapshot** (snapshot 20260904180019); points raw/verified 10/10
  - p94 National NPS recreation visits, 2015 = **307,247,252** recreation visits (2015-01-01..2015-12-31) [keep: ] quote: "\| 2015 \| 307,247,252 \|"
  - p95 National NPS recreation visits, 2016 = **330,971,689** recreation visits (2016-01-01..2016-12-31) [keep: ] quote: "\| 2016 \| 330,971,689 \|"
  - p96 National NPS recreation visits, 2017 = **330,882,751** recreation visits (2017-01-01..2017-12-31) [keep: ] quote: "\| 2017 \| 330,882,751 \|"
  - p97 National NPS recreation visits, 2018 = **318,211,833** recreation visits (2018-01-01..2018-12-31) [keep: ] quote: "\| 2018 \| 318,211,833 \|"
  - p98 National NPS recreation visits, 2019 = **327,516,619** recreation visits (2019-01-01..2019-12-31) [keep: ] quote: "\| 2019 \| 327,516,619 \|"
  - p99 National NPS recreation visits, 2020 = **237,064,332** recreation visits (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020 \| 237,064,332 \|"
  - p100 National NPS recreation visits, 2021 = **297,115,406** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021 \| 297,115,406 \|"
  - p101 National NPS recreation visits, 2022 = **311,985,998** recreation visits (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022 \| 311,985,998 \|"
  - p102 National NPS recreation visits, 2023 = **325,498,646** recreation visits (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023 \| 325,498,646 \|"
  - p103 National NPS recreation visits, 2024 = **331,863,358** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024 \| 331,863,358 \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.nps.gov/orgs/1207/03-13-26-2025-visitation-statsitics.htm` -> **snapshot** (snapshot 20260903155721); points raw/verified 15/15
  - p104 National Park Service total recreation visits, 2025 = **323,014,305** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- 323,014,305 recreation visits (406 parks report visitation figures)"
  - p105 Yellowstone National Park recreation visits, 2025 = **4,762,988** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Yellowstone NP 4,762,988"
  - p106 National Park Service total recreation visits, 2025 (rounded, headline) = **323,000,000** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "The National Park Service today announced it recorded more than 323 million recreation visits in 2025"
  - p107 National Park Service overnight stays, 2025 = **13,016,577** overnight stays (2025-01-01..2025-12-31) [keep: ] quote: "- 13,016,577 overnight stays"
  - p108 National Park Service recreation visitor hours, 2025 = **1,386,749,187** recreation visitor hours (2025-01-01..2025-12-31) [keep: ] quote: "- 1,386,749,187 recreation visitor hours"
  - p109 National Park Service overnight stays, 2025 (rounded, headline) = **13,000,000** overnight stays (2025-01-01..2025-12-31) [keep: ] quote: "including over 13 million overnight stays"
  - p110 Great Smoky Mountains NP recreation visits, 2025 = **11,527,939** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Great Smoky Mountains NP 11,527,939"
  - p111 Zion NP recreation visits, 2025 = **4,984,525** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Zion NP 4,984,525"
  - p112 Grand Canyon NP recreation visits, 2025 = **4,430,653** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Canyon NP 4,430,653"
  - p113 Yosemite NP recreation visits, 2025 = **4,278,413** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Yosemite NP 4,278,413"
  - p114 Rocky Mountain NP recreation visits, 2025 = **4,171,431** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Rocky Mountain NP 4,171,431"
  - p115 Acadia NP recreation visits, 2025 = **4,079,318** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Acadia NP 4,079,318"
  - p116 Grand Teton NP recreation visits, 2025 = **3,800,648** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Teton NP 3,800,648"
  - p117 Olympic NP recreation visits, 2025 = **3,584,187** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Olympic NP 3,584,187"
  - p118 Glacier NP recreation visits, 2025 = **3,136,557** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Glacier NP 3,136,557"
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://catalog.data.gov/dataset/nps-visitor-use-statistics-data-package-2025` -> **snapshot** (snapshot 20260823152220); points raw/verified 0/0

### b3 [base_rates] Regional park September visitation trends as a proxy for Yellowstone

Hypothesis: Grand Teton and Glacier September visitation changes are a good proxy for Yellowstone September changes.

Queries issued by the searcher: Grand Teton National Park September recreation visits NPS statistics; Glacier National Park September visitation statistics NPS; irma.nps.gov Stats Recreation Visitors By Month Grand Teton NP GRTE; NPS Visitor Use Statistics Grand Teton monthly recreation visits September 2022 2023 2024 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=b2ad0ac9-e392-471f-8a2f-0ce728a337be&_m=Remote&_r=%2FIRMA+Prod%2FSTATS%2FPark+Specific+Reports%2FR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/Park/GRTE` -> **snapshot** (snapshot 20250225114905); points raw/verified 0/0
- `https://www.nps.gov/grte/learn/news/grand-teton-sees-second-busiest-september-for-visitation.htm` -> **snapshot** (snapshot 20260121074437); points raw/verified 10/10
  - p119 Grand Teton National Park September recreation visits, 2021 = **570,584** recreation visits (2021-09-01..2021-09-30) [keep: ] quote: "The park hosted an estimated 570,584 recreation visits in September 2021."
  - p120 Grand Teton National Park September recreation visits, 2020 = **603,789** recreation visits (2020-09-01..2020-09-30) [keep: ] quote: "September 2020 603,789* COVID-19 pandemic"
  - p121 Grand Teton National Park September recreation visits, 2019 = **517,265** recreation visits (2019-09-01..2019-09-30) [keep: ] quote: "September 2019 517,265"
  - p122 Grand Teton National Park September recreation visits, 2018 = **558,788** recreation visits (2018-09-01..2018-09-30) [keep: ] quote: "September 2018 558,788"
  - p123 Grand Teton National Park September recreation visits, 2017 = **482,661** recreation visits (2017-09-01..2017-09-30) [keep: ] quote: "September 2017 482,661"
  - p124 Grand Teton National Park September recreation visits, 2016 = **492,451** recreation visits (2016-09-01..2016-09-30) [keep: ] quote: "September 2016 492,451"
  - p125 Grand Teton National Park September overnight stays, 2021 = **74,348** overnight stays (2021-09-01..2021-09-30) [keep: ] quote: "Camping in the park increased 25% in September 2021 (74,348 overnight stays)"
  - p126 Grand Teton National Park September overnight stays, 2019 = **59,340** overnight stays (2019-09-01..2019-09-30) [keep: ] quote: "compared to September 2019 (59,340 overnight stays)"
  - p127 Grand Teton National Park September backcountry camper nights, 2021 = **7,229** backcountry camper nights (2021-09-01..2021-09-30) [keep: ] quote: "Backcountry camping increased 49% in September 2021 (7,229 backcountry camper nights)"
  - p128 Grand Teton National Park September backcountry camper nights, 2019 = **4,837** backcountry camper nights (2019-09-01..2019-09-30) [keep: ] quote: "compared to September 2019 (4,837 backcountry camper nights)"
- `https://hungryhorsenews.com/news/2025/dec/23/glacier-park-visitation-tops-3-million-again-in-2025/` -> **snapshot** (snapshot 20251226002825); points raw/verified 8/8
  - p129 Glacier National Park recreation visits, September = **552,479** recreation visits (person-visits) (2025-09-01..2025-09-30) [keep: ] quote: "All told, October saw 127,537 visits, while September saw 552,479."
  - p130 Glacier National Park recreation visits, October = **127,537** recreation visits (person-visits) (2025-10-01..2025-10-31) [keep: ] quote: "All told, October saw 127,537 visits, while September saw 552,479."
  - p131 Glacier National Park estimated visitation through October = **3,086,000** people (2025-01-01..2025-10-31) [keep: ] quote: "with 3.086 million people estimated to have visited Glacier through October."
  - p132 Glacier National Park total visitation, previous year = **3,208,000** people (2024-01-01..2024-12-31) [keep: ] quote: "Last year the total was 3.208 million for the year."
  - p133 Glacier National Park busiest year visitation = **3,305,000** people (2017-01-01..2017-12-31) [keep: ] quote: "The busiest year ever was 2017, when 3.305 million people visited."
  - p134 Glacier National Park September visitation change vs previous year = **53,000** visitors (2025-09-01..2025-09-30) [keep: ] quote: "September was also down from the previous year about 53,000 visitors"
  - p135 Glacier National Park visitation change through October vs last season = **2.5** % (2025-01-01..2025-10-31) [keep: ] quote: "Through October, visitation is off slightly compared to last season by just 2.5%."
  - p136 Glacier National Park October visitation change = **22.7** % (2025-10-01..2025-10-31) [keep: ] quote: "All told visitation in October was down 22.7% as snows closed the alpine section of the Going-to-the-Sun Road on Oct. 11."
- `https://dailymontanan.com/2024/10/21/glacier-yellowstone-national-parks-see-boost-in-visitor-numbers/` -> **snapshot** (snapshot 20260709095832); points raw/verified 15/15
  - p137 Glacier National Park September visitors = **600,000** visitors (2024-09-01..2024-09-30) [keep: ] quote: "More than 600,000 visitors passed through one of Glacier's entrances during September, nearly 50,000 more than in 2023."
  - p138 Glacier National Park September visitors increase over 2023 = **50,000** visitors (2024-09-01..2024-09-30) [keep: ] quote: "More than 600,000 visitors passed through one of Glacier's entrances during September, nearly 50,000 more than in 2023."
  - p139 Glacier National Park year-to-date visitors = **3,001,595** people (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, 3,001,595 people have visited the park, just the third time that number has eclipsed 3 million and a 9% increase over last year."
  - p140 Glacier National Park year-to-date visitors increase over last year = **9** % (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, 3,001,595 people have visited the park, just the third time that number has eclipsed 3 million and a 9% increase over last year."
  - p141 Glacier National Park October visitors in recent years = **150,000** visitors (..) [keep: ] quote: "In recent years, Glacier has seen around 150,000 visitors during October and 20,000 each in November and December, which would bring total numbers for 2024 just shy of the 2017 record of 3.3 million v"
  - p142 Glacier National Park November visitors in recent years = **20,000** visitors (..) [keep: ] quote: "In recent years, Glacier has seen around 150,000 visitors during October and 20,000 each in November and December, which would bring total numbers for 2024 just shy of the 2017 record of 3.3 million v"
  - p143 Glacier National Park December visitors in recent years = **20,000** visitors (..) [keep: ] quote: "In recent years, Glacier has seen around 150,000 visitors during October and 20,000 each in November and December, which would bring total numbers for 2024 just shy of the 2017 record of 3.3 million v"
  - p144 Glacier National Park 2017 record annual visitors = **3,300,000** visitors (2017-01-01..2017-12-31) [keep: ] quote: "which would bring total numbers for 2024 just shy of the 2017 record of 3.3 million visitors."
  - p145 Yellowstone National Park September visitors = **838,458** visitors (2024-09-01..2024-09-30) [keep: ] quote: "Yellowstone National Park hosted 838,458 visitors last month, the second highest September on record, according to National Park Service data."
  - p146 Yellowstone National Park year-to-date recreation visits = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, the park has hosted 4,349,689 recreation visits, up 5% from 2023."
  - p147 Yellowstone National Park year-to-date recreation visits increase from 2023 = **5** % (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, the park has hosted 4,349,689 recreation visits, up 5% from 2023."
  - p148 Yellowstone National Park year-to-date visits shortfall versus 2021 record = **120,000** visits (2024-01-01..2024-09-30) [keep: ] quote: "The year-to-date numbers are just 120,000 lower than in 2021, the park's record-setting year."
  - p149 Montana national parks recreation economy spending = **716,000,000** USD (2023-01-01..2023-12-31) [keep: ] quote: "which brought in more than $716 million in spending to communities near the parks in 2023."
  - p150 Montana Park Service sites supported jobs = **10,900** jobs (2023-01-01..2023-12-31) [keep: ] quote: "supported about 10,900 jobs in Montana, and contributed about $1.1 billion in economic output."
  - p151 Montana Park Service sites economic output = **1,100,000,000** USD (2023-01-01..2023-12-31) [keep: ] quote: "supported about 10,900 jobs in Montana, and contributed about $1.1 billion in economic output."

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'september', 'visitation']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] September 2024, 2023, and 2021 recreation visits from the same NPS-derived report, consistent with each other and with the year-to-date figures.
- corroborating: ['p1', 'p10'] September 2023 value 838,458 appears in both nbcmontana.com and buckrail.com, independent snapshots agreeing.
- corroborating: ['p3', 'p11'] September 2021 value 882,078 appears in both nbcmontana.com and buckrail.com.
- corroborating: ['p4', 'p12', 'p15'] Year-to-date through September 2024 = 4,349,689 appears in three separate snapshots/sources.
- corroborating: ['p5', 'p13', 'p16'] Year-to-date through September 2023 = 4,147,382 appears in multiple snapshots.
- corroborating: ['p7', 'p14', 'p18'] Year-to-date through September 2021 = 4,472,687 appears in multiple snapshots.
- corroborating: ['p6', 'p17'] Year-to-date through September 2022 = 3,005,194 appears in both sources.
- corroborating: ['p8', 'p19'] Year-to-date through September 2020 = 3,393,642 appears in both sources.
- corroborating: ['p9', 'p20'] Year-to-date through September 2019 = 3,807,815 appears in both sources.
- corroborating: ['p21', 'p22', 'p23'] NPS national 2025 totals and the 2.7% decline from 2024 are internally consistent.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Glacier National Park 2025 visitation figures from one article, internally consistent and showing a regional September decline.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51'] Yellowstone entrance vehicle counts for early September 2021, consistent with each other and with the high September 2021 visitation.
- corroborating: ['p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67'] Montana tourism survey indicators for 2024-2025, consistent in showing weakening demand.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2

## Methods (computed by code)

| id | method | estimate | backtest years | mean abs ln err | weight | notes / error |
|---|---|---|---|---|---|---|
| m1 | series_naive | 845,446 | [] |  | 0.50 |  |
| m2 | series_naive | 857,657 | [] |  | 0.50 |  |
| m3 | yoy_scaling | n/a | [] |  | 0.00 | yoy_scaling needs target for 2025 |
| m4 | ratio | n/a | [] |  | 0.00 | signal has no value for 2026 |

Result: central **851,530**, 80% interval [843,742, 859,390], basis method_spread, weight rule equal

## Final answer

We estimate 851,530 recreation visits to Yellowstone National Park in September 2026, with an [n] interval of 843,742 to 859,390 (basis: method spread). The estimate rests on 2 methods. The first, weighted 50%, uses the two most recent September values and gives 845,446; the second, weighted 50%, averages the three most recent Septembers and gives 857,657. Both are simple seasonal baselines, so they were weighted equally. Two further methods were dropped: one needed a 2025 target, the other a regional signal with no 2026 value. The true figure could differ because of weather, fire or smoke closures, road and lodging availability, and shifts in travel demand. Missing evidence includes September 2025 actuals, any 2026 monthly data, and park-specific counter or methodology changes. The interval reflects method spread, not full uncertainty.

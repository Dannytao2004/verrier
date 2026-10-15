# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park, as counted by the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics program). A recreation visit is defined as a visit to a park for recreational purposes; each person entering the park is counted once per day,  | unit recreation visits (count) | period 2026-08-01..2026-08-31 | publisher National Park Service, Visitor Use Statistics program (https://irma.nps.gov/Stats/)

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [own_history] NPS official monthly visitation statistics for Yellowstone National Park

Hypothesis: The target is strongly autocorrelated with its own history. August is typically the peak month. The 2023, 2024, and 2025 August values provide a baseline; the 2026 value will likely be within a few percent of these, adjusted for any known shocks.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics August 2025 NPS; Yellowstone recreation visits August 2024 NPS visitor use statistics; nps.gov Yellowstone visitation statistics August 2023 846,389 recreation visits; Yellowstone National Park visitation statistics July 2025 975,109 monthly

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p1 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: Most recent August value (2025), directly relevant own-history for the target month.] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024"
  - p2 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: August 2024 value, directly relevant own-history.] quote: "up 2% from August 2024 (868,259 recreation visits)"
  - p3 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: August 2021 value, a recent high year, useful for range and trend.] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p4 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: Annual 2021 total, corroborates the 2021 peak and can be used with seasonal share.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p5 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: YTD through August 2025, corroborates 2025 level and trend.] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024"
  - p6 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: YTD through August 2024, corroborates 2024 level and trend.] quote: "up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021"
  - p7 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: YTD through August 2021, corroborates 2021 peak.] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p8 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of p5 (same value, same period).] quote: "2025 - 3,547,967"
  - p9 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of p6 (same value, same period).] quote: "2024 - 3,494,350"
  - p10 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: YTD through August 2023; one of two conflicting values, but useful for trend.] quote: "2023 - 3,308,924"
  - p11 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: YTD through August 2022, shows flood-depressed year; useful context.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event."
  - p12 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p7 (same value, same period).] quote: "2021 - 3,590,609"
  - p13 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: YTD through August 2020, COVID-depressed year; useful context for shocks.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19."
- `http://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/23037.htm` -> **snapshot** (snapshot 20260617061634); points raw/verified 12/12
  - p14 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [keep: August 2023 value, directly relevant own-history.] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p15 Yellowstone National Park recreation visits, August 2022 = **582,211** recreation visits (2022-08-01..2022-08-31) [keep: August 2022 value, flood-depressed; useful context.] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p16 Yellowstone National Park recreation visits, August 2019 = **820,006** recreation visits (2019-08-01..2019-08-31) [keep: August 2019 value, pre-COVID baseline; useful for longer trend.] quote: "a 3% increase from August 2019* (820,006 recreational visits)."
  - p17 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [keep: YTD through August 2023; conflicting with p10 but close; keep for trend.] quote: "So far in 2023, the park has hosted 3,313,244 recreation visits"
  - p18 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p11 (same value, same period).] quote: "up 36% from 2022 (2,437,607 recreation visits)"
  - p19 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [keep: YTD through August 2019, pre-COVID baseline.] quote: "up 6% from 2019 (3,114,697 recreation visits)."
  - p20 Yellowstone National Park year-to-date recreation visits through August 2023 (tr = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of p17 (same value, same period).] quote: "2023 - 3,313,244"
  - p21 Yellowstone National Park year-to-date recreation visits through August 2022 (tr = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p11 (same value, same period).] quote: "2022 - 2,437,607"
  - p22 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p7 (same value, same period).] quote: "2021 - 3,590,609"
  - p23 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p13 (same value, same period).] quote: "2020 - 2,556,528"
  - p24 Yellowstone National Park year-to-date recreation visits through August 2019 (tr = **3,114,697** recreation visits (2019-01-01..2019-08-31) [DISCARD: Duplicate of p19 (same value, same period).] quote: "2019 - 3,114,697"
  - p25 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [keep: YTD through August 2018, adds a pre-COVID year for trend.] quote: "2018 - 3,136,241"

### d2 [related_series] Other NPS units in the region (Grand Teton, Glacier, etc.) and national totals

Hypothesis: Visitation to Yellowstone is correlated with visitation to other nearby national parks (e.g., Grand Teton) and with overall national park visitation trends. If Grand Teton's August 2026 data are available (or if national trends are known), they can inform Yellowstone's expected value. However, note that Grand Teton's data may also not be published yet.

Queries issued by the searcher: Grand Teton National Park monthly visitation 2025 recreation visits; NPS total visitation August 2025 national park visitation statistics; Glacier National Park August 2025 recreation visits monthly visitation statistics; Yellowstone August 2026 visitation record visitors

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=b2ad0ac9-e392-471f-8a2f-0ce728a337be&_m=Remote&_r=%2FIRMA+Prod%2FSTATS%2FPark+Specific+Reports%2FR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/Park/GLAC` -> **snapshot** (snapshot 20260317072521); points raw/verified 0/0
- `https://tourism.az.gov/wp-content/uploads/2026/04/NPS-August-2025-Final.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://flatheadbeacon.com/2025/09/13/as-canadian-tourism-slows-and-many-glacier-restricts-access-summer-traffic-to-glacier-dips/` -> **snapshot** (snapshot 20251011172053); points raw/verified 11/9
  - p26 Glacier National Park visitors in August = **718,000** visitors (2025-08-01..2025-08-31) [keep: Glacier August 2025, related-series signal for regional August trend.] quote: "Glacier National Park logged more than 718,000 visitors in August, according to new park data, marking a 4.1% decrease compared to the same month last year."
  - p27 Glacier National Park year-to-date visitors through end of August = **2,400,000** visitors (2025-01-01..2025-08-31) [keep: Glacier YTD through August 2025, related-series signal.] quote: "Through the end of August, more than 2.4 million had visited the park this year - a negligible increase from the 2.4 million visitors logged by the end of last August."
  - p28 Glacier National Park year-to-date visitors through end of August last year = **2,400,000** visitors (2024-01-01..2024-08-31) [keep: Glacier YTD through August 2024, related-series signal for year-over-year.] quote: "Through the end of August, more than 2.4 million had visited the park this year - a negligible increase from the 2.4 million visitors logged by the end of last August."
  - p29 Glacier National Park visitors in July = **765,000** people (2025-07-01..2025-07-31) [keep: Glacier July 2025, related-series signal for summer season.] quote: "July was again the park's busiest month, with more than 765,000 people passing through the park's gates."
  - p30 Glacier National Park visitors in June = **576,577** visitors (2025-06-01..2025-06-30) [keep: Glacier June 2025, related-series signal.] quote: "June's 576,577 visitors marked a nearly 5% increase over last year, despite a summer-solstice snowstorm that temporarily shut down the alpine sections of the Going-to-the-Sun Road."
  - p31 Glacier National Park visitors in May = **238,766** people (2025-05-01..2025-05-31) [keep: Glacier May 2025, related-series signal.] quote: "May also saw strong numbers, with 238,766 people visiting the park, nearly 14% more than the 209,650 visitors in May 2024."
  - p32 Glacier National Park visitors in May 2024 = **209,650** visitors (2024-05-01..2024-05-31) [keep: Glacier May 2024, related-series signal for year-over-year.] quote: "May also saw strong numbers, with 238,766 people visiting the park, nearly 14% more than the 209,650 visitors in May 2024."
  - p33 Many Glacier visitors in August = **11,792** visitors (2025-08-01..2025-08-31) [keep: Many Glacier August 2025, related-series signal (localized).] quote: "Many Glacier saw the most dramatic decline in visitation, with 11,792 visitors in August compared to 31,603 visitors in August 2024."
  - p34 Many Glacier visitors in August 2024 = **31,603** visitors (2024-08-01..2024-08-31) [keep: Many Glacier August 2024, related-series signal (localized).] quote: "Many Glacier saw the most dramatic decline in visitation, with 11,792 visitors in August compared to 31,603 visitors in August 2024."
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### d3 [physical_flow] Entrance station traffic counts and road usage

Hypothesis: The number of vehicles entering Yellowstone's entrances is a direct physical trace of visitation. Traffic counts from state DOTs (Montana, Wyoming, Idaho) on roads leading to the park, or from the park's own entrance counters, can be used to estimate visits. If August 2026 traffic data are available (e.g., from WYDOT or MDT), they can be scaled to visits using historical ratios.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics August recreation visits NPS; WYDOT traffic counts Yellowstone August 2025; Yellowstone National Park reports August 2026 visitation statistics 856,467 recreation visits; Montana DOT traffic data Yellowstone entrance North Gate US-89 counts

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://ebs.publicnow.com/view/FCBC7BE758668E5A1DB645205801D4438187CF6B` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://unofficialnetworks.com/2026/09/15/yellowstone-visitation-falls-in-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-15 > as_of); points raw/verified -/-
- `https://www.cookecityareacouncil.org/_files/ugd/69e9d2_ff019c8dd4d54f4b98ce2b2343517a8e.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d4 [capacity_consumption] Accommodation occupancy, campground reservations, and gateway community data

Hypothesis: Hotel occupancy, campground reservations, and short-term rental bookings in gateway towns (West Yellowstone, Gardiner, Cody, Jackson) are strong proxies for park visitation. High occupancy in August 2026 would suggest high visitation. Data may be available from local tourism boards, Airbnb/VRBO analytics, or reservation systems (e.g., Recreation.gov for campgrounds).

Queries issued by the searcher: Yellowstone National Park recreation visits August 2026 NPS visitor use statistics; West Yellowstone hotel occupancy August 2025 tourism statistics

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://ebs.publicnow.com/view/FCBC7BE758668E5A1DB645205801D4438187CF6B` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://unofficialnetworks.com/2026/09/15/yellowstone-visitation-falls-in-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-15 > as_of); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-visitation-down-in-august` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-16 > as_of); points raw/verified -/-

### d5 [administrative] Park permits, licenses, and concessionaire reports

Hypothesis: The number of commercial tour permits, fishing licenses, and concessionaire activity (e.g., guided tours, boat rentals) can indicate visitation levels. Concessionaire reports (e.g., Xanterra, Delaware North) may include visitor numbers or revenue that correlate with visits.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics NPS Visitor Use Statistics; Yellowstone commercial use authorization statistics August; Montana fishing license sales August 2025 statistics; Yellowstone concessionaire revenue 2025 Xanterra annual report

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 15/15
  - p35 Average number of visits to Yellowstone National Park in August (2014-2018) = **839,787** visits (2014-08-01..2018-08-31) [keep: Average August visits 2014-2018, base rate for August level.] quote: "\| August \| 839,787 \| 20.89% \|"
  - p36 August share of average annual visits to Yellowstone National Park (2014-2018) = **20.89** % (2014-08-01..2018-08-31) [keep: August share of annual visits 2014-2018, base rate for converting annual to August.] quote: "\| August \| 839,787 \| 20.89% \|"
  - p37 Average number of visits to Yellowstone National Park in July (2014-2018) = **947,688** visits (2014-07-01..2018-07-31) [keep: Average July visits 2014-2018, base rate for seasonal pattern.] quote: "\| July \| 947,688 \| 23.57% \|"
  - p38 July share of average annual visits to Yellowstone National Park (2014-2018) = **23.57** % (2014-07-01..2018-07-31) [keep: July share of annual visits 2014-2018, base rate for seasonal pattern.] quote: "\| July \| 947,688 \| 23.57% \|"
  - p39 Average number of visits to Yellowstone National Park in June (2014-2018) = **780,652** visits (2014-06-01..2018-06-30) [keep: Average June visits 2014-2018, base rate for seasonal pattern.] quote: "\| June \| 780,652 \| 19.42% \|"
  - p40 June share of average annual visits to Yellowstone National Park (2014-2018) = **19.42** % (2014-06-01..2018-06-30) [keep: June share of annual visits 2014-2018, base rate for seasonal pattern.] quote: "\| June \| 780,652 \| 19.42% \|"
  - p41 Average number of visits to Yellowstone National Park in September (2014-2018) = **663,651** visits (2014-09-01..2018-09-30) [keep: Average September visits 2014-2018, base rate for seasonal pattern.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p42 September share of average annual visits to Yellowstone National Park (2014-2018 = **16.51** % (2014-09-01..2018-09-30) [keep: September share of annual visits 2014-2018, base rate for seasonal pattern.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p43 Average number of visits to Yellowstone National Park in May (2014-2018) = **401,449** visits (2014-05-01..2018-05-31) [keep: Average May visits 2014-2018, base rate for seasonal pattern.] quote: "\| May \| 401,449 \| 9.99% \|"
  - p44 May share of average annual visits to Yellowstone National Park (2014-2018) = **9.99** % (2014-05-01..2018-05-31) [keep: May share of annual visits 2014-2018, base rate for seasonal pattern.] quote: "\| May \| 401,449 \| 9.99% \|"
  - p45 Average number of visits to Yellowstone National Park in October (2014-2018) = **223,777** visits (2014-10-01..2018-10-31) [keep: Average October visits 2014-2018, base rate for seasonal pattern.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p46 October share of average annual visits to Yellowstone National Park (2014-2018) = **5.57** % (2014-10-01..2018-10-31) [keep: October share of annual visits 2014-2018, base rate for seasonal pattern.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p47 Average number of visits to Yellowstone National Park in April (2014-2018) = **44,027** visits (2014-04-01..2018-04-30) [keep: Average April visits 2014-2018, base rate for seasonal pattern.] quote: "\| April \| 44,027 \| 1.10% \|"
  - p48 Average number of visits to Yellowstone National Park in February (2014-2018) = **33,088** visits (2014-02-01..2018-02-28) [keep: Average February visits 2014-2018, base rate for seasonal pattern.] quote: "\| February \| 33,088 \| 0.82% \|"
  - p49 Average number of visits to Yellowstone National Park in January (2014-2018) = **28,837** visits (2014-01-01..2018-01-31) [keep: Average January visits 2014-2018, base rate for seasonal pattern.] quote: "\| January \| 28,837 \| 0.72% \|"
- `https://www.trailguidesyellowstone.com/information/yellowstone-news-and-events` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live http 403); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/Park/YELL` -> **snapshot** (snapshot 20260113011158); points raw/verified 0/0

### d6 [attention] Search interest, social media, and news coverage

Hypothesis: Google Trends for 'Yellowstone National Park' and related terms in the months leading up to August 2026 can indicate interest and potential visitation. A spike in search interest may precede higher visitation. Social media posts and news articles about the park can also signal demand.

Queries issued by the searcher: Yellowstone National Park visitation statistics August 2026 NPS; NPS Visitor Use Statistics Yellowstone recreation visits 2026; irma.nps.gov Stats Yellowstone monthly public use report August 2026 recreation visits; Google Trends Yellowstone National Park 2026 search interest

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://ebs.publicnow.com/view/FCBC7BE758668E5A1DB645205801D4438187CF6B` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://unofficialnetworks.com/2026/09/15/yellowstone-visitation-falls-in-august/` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-15 > as_of); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-visitation-down-in-august` -> **dropped** (no snapshot <= as_of; live page dated 2026-09-16 > as_of); points raw/verified -/-

### d7 [shocks] Events affecting park access and attractiveness in 2026

Hypothesis: Any major events in or around August 2026 (e.g., wildfires, road closures, flooding, wildlife incidents, policy changes like reservation requirements, gas prices, economic conditions) could push visitation up or down. For example, a new timed-entry reservation system could reduce visits, while a major anniversary or media event could increase them.

Queries issued by the searcher: Yellowstone National Park recreation visits August 2026 NPS Visitor Use Statistics; Yellowstone National Park closures August 2026; Yellowstone National Park alerts conditions August 2026 road closures; Yellowstone visitation July 2026 NPS news release recreation visits; Yellowstone National Park news June 2026 July 2026 wildfire reservation

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live page has no readable date); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/situationreport.htm` -> **snapshot** (snapshot 20260618033531); points raw/verified 0/0
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 0/0
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 13/6
  - p50 Yellowstone National Park recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [keep: Annual 2025 total, most recent annual level; useful with August share.] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p51 Yellowstone National Park recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [keep: Annual 2024 total, useful with August share.] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p52 Yellowstone National Park recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [keep: Annual 2021 total, peak year; useful with August share.] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p53 Grand Teton National Park recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [keep: Grand Teton annual 2025, related-series signal for regional trend.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p54 Grand Teton National Park recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [keep: Grand Teton annual 2024, related-series signal for regional trend.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p55 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [keep: Grand Teton annual 2021 peak, related-series signal for regional trend.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
- dropped by code checks: 7 (period_end missing or unparseable: 4; period_end 2026-09-07 after as_of: 1; value_as_written not in quote: 2)

### d8 [forecasts_markets] Published forecasts and prediction markets

Hypothesis: Any forecasts for Yellowstone visitation in 2026 from tourism boards, economists, or industry analysts can provide a baseline. Prediction markets (e.g., Polymarket, Kalshi) may have contracts on national park visitation or related metrics.

Queries issued by the searcher: Yellowstone visitation forecast 2026; national park visitation prediction market Polymarket Kalshi; Montana tourism forecast 2026 Institute for Tourism and Recreation Research; Wyoming Office of Tourism Yellowstone visitation forecast 2026

- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live page dated 2026-08-17 > as_of); points raw/verified -/-
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live fetch blocked by robots.txt); points raw/verified -/-
- `https://montanaeconomist.org/a-steady-year-amid-shifting-trends/` -> **snapshot** (snapshot 20260511092735); points raw/verified 0/0
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 7/6
  - p56 Yellowstone National Park recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Duplicate of p50 (same value, same period).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p57 Yellowstone National Park recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Duplicate of p51 (same value, same period).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p58 Yellowstone National Park recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p52 (same value, same period).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p59 Grand Teton National Park recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Duplicate of p53 (same value, same period).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p60 Grand Teton National Park recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Duplicate of p54 (same value, same period).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p61 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of p55 (same value, same period).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'visitation', 'august']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p14', 'p15', 'p16'] All are NPS-reported August recreation visits for Yellowstone in different years (2025, 2024, 2021, 2023, 2022, 2019). They form a consistent own-history series for the same calendar month, with the 2
- corroborating: ['p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25'] Year-to-date through August recreation visits for Yellowstone across many years. They corroborate the August monthly values and the annual totals, and show the same year-over-year pattern (2025 up ~2%
- corroborating: ['p4', 'p50', 'p51', 'p52', 'p56', 'p57', 'p58'] Annual recreation visits for Yellowstone. p4 (2021 >4.8M) and p50/p52/p56/p58 (2021 4.86M) agree on the 2021 peak; p50/p51/p56/p57 agree on 2025 4.76M and 2024 4.74M. Minor rounding differences only.
- corroborating: ['p53', 'p54', 'p55', 'p59', 'p60', 'p61'] Annual recreation visits for Grand Teton, a nearby park. They corroborate each other and show a similar regional visitation trend (2025 up from 2024, below 2021 peak).
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] Glacier National Park monthly visitation for 2025 and some 2024 comparisons. They corroborate a regional pattern of high but slightly declining August visitation in 2025, useful as a related-series si
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49'] NPS seasonal averages and shares for Yellowstone (2014-2018). They corroborate the strong summer peak and give a base-rate August share (~20.9% of annual visits) that can be used to convert annual est
- conflicting: ['p10', 'p17', 'p20'] Year-to-date through August 2023 for Yellowstone: p10 says 3,308,924 while p17/p20 say 3,313,244. Likely a revision or different snapshot date; the difference is small (~0.13%).

## Methods (computed by code)

| id | method | estimate | backtest years | mean abs ln err | weight | notes / error |
|---|---|---|---|---|---|---|
| m1 | series_naive | 890,680 | [] |  | 0.33 |  |
| m2 | series_naive | 875,098 | [] |  | 0.33 |  |
| m3 | yoy_scaling | n/a | [] |  | 0.00 | yoy_scaling needs signal for 2026 |
| m4 | ratio | n/a | [] |  | 0.00 | signal has no value for 2026 |
| m5 | formula_mc | 994,858 | [] |  | 0.33 |  |

Result: central **918,713**, 80% interval [825,786, 1,022,096], basis monte_carlo, weight rule equal

## Final answer

Our estimate for Yellowstone National Park recreation visits in August 2026 is 918,713, with an [n] interval of 825,786 to 1,022,096 (basis: monte carlo). This rests on 3 methods. The first two use recent August values directly: 890,680 (weight 33%) and 875,098 (weight 33%). A third multiplies the 2025 annual total by the historical August share: 994,858 (weight 33%). Two further methods (YoY scaling from Glacier, and a Grand Teton ratio) were dropped because they lacked 2026 signal. The true value could differ because NPS counts are estimates from traffic counters, definitions exclude non-recreation entries, and 2026 conditions (fires, closures, weather, travel demand) are unknown. Missing evidence includes actual 2026 monthly data, Glacier's 2026 August figures, and Grand Teton's 2026 annual level.

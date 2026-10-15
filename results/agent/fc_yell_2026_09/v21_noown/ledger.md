# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics. A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions counts as multiple visits. | unit recreation visits (count) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), typically via the Visitor Use Statistics program / Integrated Resource Management Applications (IRMA) and the NPS monthly visitation report.

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [shocks] Closures, weather, and calendar effects

Hypothesis: September visitation is sensitive to road closures, wildfires, weather events, and the timing of Labor Day. In 2026, any known closures or major events (e.g., road construction) could shift visitation. The 2022 flood caused a dramatic drop; other years had minor disruptions.

Queries issued by the searcher: Yellowstone visitation September 2025 National Park Service monthly report; Yellowstone road closures September 2026 construction; Yellowstone National Park visitation statistics September by year; Yellowstone 2022 flood visitation drop September

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://outdoor-society.com/2025/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] National Park Service overall visitation and Yellowstone's share

Hypothesis: Yellowstone's September recreation visits are a roughly stable share of total NPS September recreation visits or of visitation to a comparable set of large western parks. If NPS-wide September 2026 data or a nowcast is available, Yellowstone's share can be applied.

Queries issued by the searcher: NPS total recreation visits September 2025 monthly visitation report; Yellowstone National Park September 2025 visitation statistics; NPS national total recreation visits September 2025 IRMA monthly report all parks; Yellowstone September recreation visits 2024 2023 2022 2021 history; Grand Teton Glacier Yosemite September 2025 visitation statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260821013908); points raw/verified 0/0
- `https://publiclandsdata.com/national-park-visitation/data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from the number of vehicles entering Yellowstone in September multiplied by average persons per vehicle, plus pedestrian/bicycle entries. Entrance counts may be available from park traffic counters or gateway community data.

Queries issued by the searcher: Yellowstone entrance vehicle counts September visitation statistics; Yellowstone average persons per vehicle visitation study occupancy; Yellowstone traffic counter data monthly entrance stations NPS; National Park Service visitor use statistics Yellowstone monthly recreation visits September 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=d585c74f-f89b-4f43-a00e-e02e315496a9&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fT` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.tripadvisor.com.au/ShowTopic-g60999-i481-k15386767-West_entrance_wait_times-Yellowstone_National_Park_Wyoming.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstonegate.com/?p=7848` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [capacity_consumption] Accommodation occupancy and campground use in Yellowstone and gateway communities

Hypothesis: Overnight stays in the park and surrounding areas are a major component of visits. September occupancy rates and room/campsite capacity can be used to estimate overnight visits, which can be combined with day-use estimates.

Queries issued by the searcher: Yellowstone lodge occupancy September 2025 Xanterra; Yellowstone campground occupancy statistics overnight stays September; Yellowstone lodges total rooms campground sites capacity Xanterra number; Park County Wyoming lodging tax September 2025 occupancy rate

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://powelltribune.com/stories/region-continues-to-buck-downward-trend-of-tourism,170327` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstoneparknet.com/park_lodging` -> **snapshot** (snapshot 20260707123119); points raw/verified 15/0
- `https://www.travelandtourworld.cz/zpr%C3%A1vy/%C4%8Dl%C3%A1nek/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end missing or unparseable: 15)

### d5 [forecasts_markets] Published forecasts or nowcasts for Yellowstone 2026 visitation

Hypothesis: Tourism forecasts, park concessionaire projections, or economic outlooks for the Yellowstone region may provide a September 2026 visitation estimate or a growth rate that can be applied to historical September data.

Queries issued by the searcher: Yellowstone visitation forecast 2026; Wyoming tourism forecast 2026 Yellowstone; Yellowstone National Park September 2025 visitation statistics recreation visits; Yellowstone monthly visitation September 2024 2023 NPS recreation visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://wyofile.com/new-100-fee-on-yellowstone-grand-tetons-foreign-visitors-brings-uncertain-impacts/` -> **snapshot** (snapshot 20260410030005); points raw/verified 15/6
  - p1 Yellowstone National Park total visitation in 2024 = **4,700,000** visitors (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "Yellowstone counted 4.7 million visitors in 2024, down from a high of 4.8 million in 2021."
  - p2 Yellowstone National Park total visitation high in 2021 = **4,800,000** visitors (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "Yellowstone counted 4.7 million visitors in 2024, down from a high of 4.8 million in 2021."
  - p3 Foreign visitation share of total Yellowstone visitors in 2024 = **14.8** percent of total visitors (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "Between 2018 and 2024, foreign visitation to Yellowstone dropped from about 30% of total visitors to 14.8%, according to the park's statistics."
  - p4 Foreign visitation share of total Yellowstone visitors in 2018 = **30** percent of total visitors (2018-01-01..2018-12-31) [EXCLUDED (ablation): ] quote: "Between 2018 and 2024, foreign visitation to Yellowstone dropped from about 30% of total visitors to 14.8%, according to the park's statistics."
  - p5 Foreign visitors to Yellowstone National Park in 2018 = **1,200,000** foreign visitors (2018-01-01..2018-12-31) [EXCLUDED (ablation): ] quote: "In 2018, Yellowstone attracted 1.2 million foreign visitors, he said, citing park figures."
  - p6 Foreign visitors to Yellowstone National Park in 2024 = **712,089** foreign visitors (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "In 2024, that number was down to 712,089."
- dropped by code checks: 9 (period_end missing or unparseable: 5; period_end 2026-12-31 after as_of: 4)

### d6 [base_rates] Seasonal decomposition and day-of-week effects

Hypothesis: September visitation can be modeled as a function of the number of days, weekends, and Labor Day timing. Historical September data can yield a base rate per day, which can be adjusted for the 2026 calendar (e.g., Labor Day on September 7).

Queries issued by the searcher: Yellowstone National Park September visitation statistics monthly; Yellowstone visitation September 2024 2023 monthly total NPS; Yellowstone daily visitation by day of week September analysis; Yellowstone recreation visits by month 2019 2021 2022 2023 September table NPS stats

- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p7 Yellowstone National Park average September visits, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p8 Yellowstone National Park September visits as share of average annual visits, 20 = **16.51** % (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p9 Yellowstone National Park average January visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [EXCLUDED (ablation): ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p10 Yellowstone National Park average February visits, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [EXCLUDED (ablation): ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p11 Yellowstone National Park average March visits, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [EXCLUDED (ablation): ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p12 Yellowstone National Park average April visits, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [EXCLUDED (ablation): ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p13 Yellowstone National Park average May visits, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [EXCLUDED (ablation): ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p14 Yellowstone National Park average June visits, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [EXCLUDED (ablation): ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p15 Yellowstone National Park average July visits, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [EXCLUDED (ablation): ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p16 Yellowstone National Park average August visits, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [EXCLUDED (ablation): ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p17 Yellowstone National Park average October visits, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [EXCLUDED (ablation): ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p18 Yellowstone National Park average November visits, 2014-2018 average = **14,323** visits (2014-11-01..2018-11-30) [EXCLUDED (ablation): ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p19 Yellowstone National Park average December visits, 2014-2018 average = **20,434** visits (2014-12-01..2018-12-31) [EXCLUDED (ablation): ] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 15/15
  - p20 Yellowstone parkwide total vehicle entries, Friday September 3, 2021 (Labor Day  = **8,945** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p21 Yellowstone parkwide total vehicle entries, Saturday September 4, 2021 (Labor Da = **11,062** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p22 Yellowstone parkwide total vehicle entries, Sunday September 5, 2021 (Labor Day  = **12,380** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p23 Yellowstone parkwide total vehicle entries, Monday September 6, 2021 (Labor Day) = **9,982** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p24 Yellowstone parkwide total vehicle entries, Friday August 30, 2019 (comparison d = **7,134** vehicle entries (2019-08-30..2019-08-30) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p25 Yellowstone parkwide total vehicle entries, Saturday August 31, 2019 (comparison = **8,913** vehicle entries (2019-08-31..2019-08-31) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p26 Yellowstone parkwide total vehicle entries, Sunday September 1, 2019 (comparison = **10,307** vehicle entries (2019-09-01..2019-09-01) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p27 Yellowstone parkwide total vehicle entries, Monday September 2, 2019 (Labor Day  = **8,551** vehicle entries (2019-09-02..2019-09-02) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p28 Yellowstone East entrance vehicle entries, Friday September 3, 2021 = **882** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| East \| 882 \| 725 \| 22% \|"
  - p29 Yellowstone North entrance vehicle entries, Friday September 3, 2021 = **1,718** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| North \| 1,718 \| 1,361 \| 26% \|"
  - p30 Yellowstone Northeast entrance vehicle entries, Friday September 3, 2021 = **477** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| Northeast \| 477 \| 522 \| -9% \|"
  - p31 Yellowstone South entrance vehicle entries, Friday September 3, 2021 = **1,750** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| South \| 1,750 \| 1,189 \| 47% \|"
  - p32 Yellowstone West entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p33 Yellowstone parkwide vehicle entries percent increase, Labor Day weekend 2021 ov = **21** % (2021-09-03..2021-09-06) [keep: ] quote: "Parkwide vehicle entries through the Labor Day weekend showed a 21% increase over the same weekend in 2019."
  - p34 Yellowstone West entrance vehicle entries, Saturday September 4, 2021 = **5,222** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Entrance-level daily count for a single 2021 holiday day; redundant with the parkwide totals and adds no independent inf] quote: "\| West \| 5,222 \| 4,640 \| 13% \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [attention] Search interest and social media activity as a leading indicator

Hypothesis: Google Trends search volume for 'Yellowstone National Park' or related terms in the weeks before and during September 2026 may correlate with actual visitation. A historical correlation can be used to nowcast September visits.

Queries issued by the searcher: Google Trends Yellowstone National Park visitation correlation; Yellowstone National Park monthly visitation statistics September 2025; Yellowstone September recreation visits history 2015 2016 2017 2018 2019 2021 2022 2023 2024; Google Trends predicts national park visitation search volume leading indicator study

- `https://www.outsideonline.com/adventure-travel/national-parks/top-searched-national-parks/?scope=anon` -> **dropped** (unsupported content type text/x-component); points raw/verified -/-
- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p35 Yellowstone Google search lead over Grand Canyon National Park, July 2025–June 2 = **1,420,000** searches (2025-07-01..2026-06-30) [DISCARD: Google search-volume lead is an attention proxy with no defensible conversion to Yellowstone September recreation visits] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://creators.yahoo.com/lifestyle/story/the-most-searched-national-park-in-every-state-reveals-one-clear-favorite-174747097.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://businessupturn.com/usa/lifestyle/travel/most-searched-national-park-every-state-2026-yellowstone/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [base_rates] NPS monthly visitation statistics

Hypothesis: Yellowstone September recreation visits for recent full years (2015-2025, excluding 2022 flood year) would provide the seasonal level and year-to-year variability needed to anchor a September 2026 estimate. This is the single most important missing input because the current kept points are only daily vehicle entries for one holiday weekend in 2021 and 2019, not monthly recreation visits.

Queries issued by the searcher: Yellowstone National Park September recreation visits NPS visitation statistics; NPS IRMA Visitor Use Statistics Yellowstone monthly recreation visits September 2015 2016 2017 2018 2019 2020; Yellowstone September 2024 visitation statistics recreation visits news release; Yellowstone National Park September 2020 visitation record 901,000 recreation visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p36 Yellowstone National Park average number of visits in September, 2014-2018 avera = **663,651** visits (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p37 September share of average annual visits at Yellowstone National Park, 2014-2018 = **16.51** % (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p38 Yellowstone National Park average number of visits in January, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [EXCLUDED (ablation): ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p39 Yellowstone National Park average number of visits in February, 2014-2018 averag = **33,088** visits (2014-02-01..2018-02-28) [EXCLUDED (ablation): ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p40 Yellowstone National Park average number of visits in March, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [EXCLUDED (ablation): ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p41 Yellowstone National Park average number of visits in April, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [EXCLUDED (ablation): ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p42 Yellowstone National Park average number of visits in May, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [EXCLUDED (ablation): ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p43 Yellowstone National Park average number of visits in June, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [EXCLUDED (ablation): ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p44 Yellowstone National Park average number of visits in July, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [EXCLUDED (ablation): ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p45 Yellowstone National Park average number of visits in August, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [EXCLUDED (ablation): ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p46 Yellowstone National Park average number of visits in October, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [EXCLUDED (ablation): ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p47 Yellowstone National Park average number of visits in November, 2014-2018 averag = **14,323** visits (2014-11-01..2018-11-30) [EXCLUDED (ablation): ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p48 Yellowstone National Park average number of visits in December, 2014-2018 averag = **20,434** visits (2014-12-01..2018-12-31) [EXCLUDED (ablation): ] quote: "\| December \| 20,434 \| 0.51% \|"

### b2 [related_series] NPS-wide or western-parks monthly statistics

Hypothesis: If NPS-wide September 2026 recreation visits or a nowcast is published, Yellowstone's historical September share of NPS-wide visits can be applied. This would unlock a top-down estimate and provide an independent check on any bottom-up vehicle-entry route.

Queries issued by the searcher: NPS monthly visitation report September Yellowstone National Park recreation visits; Yellowstone National Park visitation statistics September 2025 record; NPS national park system total recreation visits September 2026 monthly report; Yellowstone September recreation visits history 2019 2020 2021 2022 2023 2024 IRMA

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260821013908); points raw/verified 0/0

### b3 [physical_flow] Yellowstone entrance traffic counters

Hypothesis: Daily vehicle-entry counts for September 2026 (or at least early September 2026) would allow a direct physical-flow estimate using persons-per-vehicle. The kept 2021 daily counts show the method is feasible; the missing piece is the 2026 daily count level and a defensible persons-per-vehicle factor.

Queries issued by the searcher: Yellowstone National Park persons per vehicle average occupancy NPS visitation statistics; Yellowstone visitation September 2025 monthly report vehicle entries; Yellowstone persons-per-vehicle multiplier Table 1 September month NPS counting instructions; "Yellowstone" September 2024 recreation visits 852,435 monthly visitation report NPS

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.pl/aktualno%C5%9Bci/artyku%C5%82/63ykvnvt60ul/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://outdoor-society.com/no-yellowstone-national-park-is-not-empty-in-september/` -> **snapshot** (snapshot 20260607172725); points raw/verified 8/5
  - p49 Yellowstone recreation visits in August 2024 = **871,163** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "In August 2024, Yellowstone welcomed 871,163 recreation visits, up about 3 percent from the previous year."
  - p50 Yellowstone recreation visits in September 2024 = **852,435** recreation visits (2024-09-01..2024-09-30) [EXCLUDED (ablation): ] quote: "Just a month later, in September 2024, the park recorded 852,435 visits, a drop of only 2.2%."
  - p51 Year-over-year change in Yellowstone August recreation visits (2024 vs 2023) = **3** percent (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "In August 2024, Yellowstone welcomed 871,163 recreation visits, up about 3 percent from the previous year."
  - p52 September 2024 recreation visits as a share of August 2024 recreation visits (dr = **2.2** percent (2024-09-01..2024-09-30) [keep: ] quote: "Just a month later, in September 2024, the park recorded 852,435 visits, a drop of only 2.2%."
  - p53 Difference between August 2024 and September 2024 Yellowstone recreation visits = **16,000** recreation visits (2024-09-01..2024-09-30) [EXCLUDED (ablation): ] quote: "In 2024, September was teeming with visitors, only about 16,000 fewer than August, a negligible dip overall."
- dropped by code checks: 3 (period_end missing or unparseable: 1; number: no number in value_as_written: 1; number: more than one number in value_as_written: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone september visits', 'yellowstone visitation 2026', 'nps monthly visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p20', 'p21', 'p22', 'p23'] These four daily parkwide vehicle-entry counts form a coherent Labor Day weekend 2021 series (Fri-Mon). They are internally consistent with the entrance-level counts p28-p32 and p34 for the same weeke
- corroborating: ['p24', 'p25', 'p26', 'p27'] These are the 2019 comparison days for the same Labor Day weekend window. They are used only as a historical analogue for the calendar structure of early September, not as a direct level for 2026. The
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p34'] Entrance-level vehicle entries for Friday and Saturday of Labor Day weekend 2021. They sum approximately to the parkwide totals p20 and p21, so they are not independent measurements; they are useful f
- corroborating: ['p33'] The 21% parkwide increase for Labor Day weekend 2021 over 2019 is consistent with the ratio of p20-p23 to p24-p27. It is a derived summary of the same underlying counts, not an independent observation
- contextual: ['p35'] Google search lead over Grand Canyon for July 2025-June 2026 is a demand/attention signal, not a visit count. It can only support a qualitative or wide-bounded adjustment; it does not provide a Septem
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p20', 'p21', 'p22', 'p23'] These four daily parkwide vehicle-entry counts for the 2021 Labor Day weekend are internally consistent and show the expected holiday pattern (Saturday/Sunday peak, Monday decline). They are the only 
- corroborating: ['p24', 'p25', 'p26', 'p27'] These four daily parkwide vehicle-entry counts for the 2019 Labor Day weekend are the comparison-year counterpart to p20–p23. They are consistent with the 2021 series and support the 21% weekend-over-
- corroborating: ['p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p33'] The 2019 and 2021 daily counts and the reported 21% parkwide increase are mutually consistent. They share the same NPS source and measurement basis, so they are not independent of one another, but the
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p34'] Entrance-level counts for Friday and Saturday of the 2021 Labor Day weekend sum approximately to the parkwide totals in p20 and p21, confirming internal consistency of the entrance decomposition. They
- contextual: ['p35'] Google search lead over Grand Canyon is a demand-attention signal, not a visitation count. It has no established conversion to Yellowstone September recreation visits and covers a 12-month window endi
- corroborating: ['p52'] The September 2024 recreation-visit total of 852,435 and its 2.2% drop from August 2024 provide a recent full-month September level and a seasonal August-to-September ratio. This is the single most re

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 recreation visits relative to September 2024 | 1 | 0.85..1.18 | 0.7082..1.416 (widened) | ratio | m1 (m1) | No kept point gives a 2025 or 2026 September level. The 2024 September total (p52) is the most recent full-month September observation. A ratio of 1.0 with a wide range reflects uncertainty about 2025 and 2026 trends, possible post-2024 normalization, and unknown 2026 shocks. The range is deliberate | Used to transfer the September 2024 level to September 2026; valid only if no major park closure, wildfire, or demand shock materially changes September 2026 relative to the 2024 baseline. | Published 2025 or 2026 monthly NPS data showing September visitation outside the 0.85–1.18 range, or documented major closures/events in September 2026. |
| a2 | Persons per vehicle for Yellowstone in September | 2.6 | 2.2..3.1 | 1.847..3.693 (widened) | persons per vehicle | unused | No kept point supplies persons-per-vehicle. Yellowstone is a family/road-trip park; typical NPS persons-per-vehicle estimates for western parks range roughly 2.2–3.1. The value 2.6 is a central working figure, with the range reflecting uncertainty across vehicle types and occupancy. | Used to convert September vehicle entries to recreation visits; valid if the vehicle mix and occupancy in September 2026 resemble typical recent September conditions. | Park or NPS survey data showing September persons-per-vehicle outside 2.2–3.1, or a major shift toward buses/motorcycles that changes the average. |
| a3 | September 2026 vehicle entries relative to the 2021 Labor Day weekend daily average | 0.55 | 0.4..0.75 | 0.3873..0.7746 (widened) | ratio | unused | The kept daily vehicle-entry counts (p20–p23) cover only the four-day Labor Day weekend, which is a peak period. A full September includes many lower-demand weekdays and post-holiday days. The ratio 0.55 approximates the average September day relative to the holiday-weekend daily average, based on t | Used to scale the 2021 holiday-weekend daily vehicle-entry average to a full-month September 2026 vehicle-entry total; valid if the within-September seasonal shape in 2026 resembles the historical pattern. | Daily September 2026 vehicle-entry data showing a materially different ratio of month-average to Labor-Day-weekend-average entries. |

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 36 of 53
- methods allowed: ['formula_mc']

  - p1 Yellowstone National Park total visitation in 2024 = 4,700,000 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p2 Yellowstone National Park total visitation high in 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p3 Foreign visitation share of total Yellowstone visitors in 2024 = 14.8 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p4 Foreign visitation share of total Yellowstone visitors in 2018 = 30 (2018-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p5 Foreign visitors to Yellowstone National Park in 2018 = 1,200,000 (2018-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p6 Foreign visitors to Yellowstone National Park in 2024 = 712,089 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p7 Yellowstone National Park average September visits, 2014-2018 average = 663,651 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p8 Yellowstone National Park September visits as share of average annual visits, 2014-2018 av = 16.51 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p9 Yellowstone National Park average January visits, 2014-2018 average = 28,837 (2018-01-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p10 Yellowstone National Park average February visits, 2014-2018 average = 33,088 (2018-02-28): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p11 Yellowstone National Park average March visits, 2014-2018 average = 22,266 (2018-03-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p12 Yellowstone National Park average April visits, 2014-2018 average = 44,027 (2018-04-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p13 Yellowstone National Park average May visits, 2014-2018 average = 401,449 (2018-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p14 Yellowstone National Park average June visits, 2014-2018 average = 780,652 (2018-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p15 Yellowstone National Park average July visits, 2014-2018 average = 947,688 (2018-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p16 Yellowstone National Park average August visits, 2014-2018 average = 839,787 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p17 Yellowstone National Park average October visits, 2014-2018 average = 223,777 (2018-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p18 Yellowstone National Park average November visits, 2014-2018 average = 14,323 (2018-11-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p19 Yellowstone National Park average December visits, 2014-2018 average = 20,434 (2018-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p36 Yellowstone National Park average number of visits in September, 2014-2018 average = 663,651 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p37 September share of average annual visits at Yellowstone National Park, 2014-2018 average = 16.51 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p38 Yellowstone National Park average number of visits in January, 2014-2018 average = 28,837 (2018-01-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p39 Yellowstone National Park average number of visits in February, 2014-2018 average = 33,088 (2018-02-28): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p40 Yellowstone National Park average number of visits in March, 2014-2018 average = 22,266 (2018-03-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p41 Yellowstone National Park average number of visits in April, 2014-2018 average = 44,027 (2018-04-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p42 Yellowstone National Park average number of visits in May, 2014-2018 average = 401,449 (2018-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p43 Yellowstone National Park average number of visits in June, 2014-2018 average = 780,652 (2018-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p44 Yellowstone National Park average number of visits in July, 2014-2018 average = 947,688 (2018-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p45 Yellowstone National Park average number of visits in August, 2014-2018 average = 839,787 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p46 Yellowstone National Park average number of visits in October, 2014-2018 average = 223,777 (2018-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p47 Yellowstone National Park average number of visits in November, 2014-2018 average = 14,323 (2018-11-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p48 Yellowstone National Park average number of visits in December, 2014-2018 average = 20,434 (2018-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p49 Yellowstone recreation visits in August 2024 = 871,163 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p50 Yellowstone recreation visits in September 2024 = 852,435 (2024-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p51 Year-over-year change in Yellowstone August recreation visits (2024 vs 2023) = 3 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p53 Difference between August 2024 and September 2024 Yellowstone recreation visits = 16,000 (2024-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2.209 | ['p52'] / ['a1'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a | ['p20', 'p21', 'p22', 'p23'] / ['a2', 'a3'] | [] |  | 0.00 |  | formula: numeric constant 4 not allowed (only 1 and exponents); make it a named input |

Result: central **2.209**, 80% interval [1.494, 3.267], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for recreation visits to Yellowstone National Park during September 2026 (2026-[n]-[n] to 2026-[n]-[n]), as reported in NPS monthly visitation statistics, is 2.209 visits, with a model-based interval of 1.494 to 3.267 at the 80% level (monte carlo). This rests on 10 observed point(s) and 1 method(s); the sole contributing method carries weight 100% and estimate 2.209. The anchor is the most recent full-month September observation, transferred to 2026 by an assumed ratio of 1 (range 0.7082 to 1.416). The level is observed; the [n]-to-2026 change is assumption, not evidence. The main risk is that [n] or 2026 visitation diverged sharply from 2024, or that a September shock occurred. The most valuable missing evidence would be published [n] and 2026 September figures, or recent monthly [n] data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 recreation visits relative to September 2024: 1 ratio, range 0.7082 to 1.416 (range widened by code); used by m1. Overturned by: Published [n] or 2026 monthly NPS data showing September visitation outside the [n]–[n] range, or documented major closures/events in September 2026.

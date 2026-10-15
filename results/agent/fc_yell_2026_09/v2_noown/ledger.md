# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Monthly Public Use Report). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times counts as multiple v | unit recreation visits (count) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), Public Use Statistics Office / Social Science Program

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [physical_flow] Entrance station counts and vehicle traffic

Hypothesis: Recreation visits can be approximated by vehicle entries multiplied by average occupancy, plus pedestrian/bicycle entries. If entrance station data or road traffic counts for September 2026 are available, they can provide a direct physical flow estimate.

Queries issued by the searcher: Yellowstone National Park September 2025 visitation statistics recreation visits; Yellowstone entrance station vehicle counts September average vehicle occupancy; NPS Yellowstone monthly public use report 2025 recreation visits; Yellowstone persons per vehicle multiplier NPS visitor use reporting counting instructions; Yellowstone National Park September 2025 visitation statistics news release 839,579; Yellowstone average vehicle occupancy 2.5 persons per vehicle entrance station study

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 14/13
  - p1 Yellowstone East entrance vehicle entries, Friday September 3, 2021 = **882** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| East \| 882 \| 725 \| 22% \|"
  - p2 Yellowstone North entrance vehicle entries, Friday September 3, 2021 = **1,718** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| North \| 1,718 \| 1,361 \| 26% \|"
  - p3 Yellowstone Northeast entrance vehicle entries, Friday September 3, 2021 = **477** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| Northeast \| 477 \| 522 \| -9% \|"
  - p4 Yellowstone South entrance vehicle entries, Friday September 3, 2021 = **1,750** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| South \| 1,750 \| 1,189 \| 47% \|"
  - p5 Yellowstone West entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p6 Yellowstone parkwide total vehicle entries, Friday September 3, 2021 = **8,945** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p7 Yellowstone parkwide total vehicle entries, Saturday September 4, 2021 = **11,062** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p8 Yellowstone parkwide total vehicle entries, Sunday September 5, 2021 = **12,380** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p9 Yellowstone parkwide total vehicle entries, Monday September 6, 2021 = **9,982** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p10 Yellowstone parkwide total vehicle entries, Friday August 30, 2019 = **7,134** vehicle entries (2019-08-30..2019-08-30) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p11 Yellowstone parkwide total vehicle entries, Saturday August 31, 2019 = **8,913** vehicle entries (2019-08-31..2019-08-31) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p12 Yellowstone parkwide total vehicle entries, Sunday September 1, 2019 = **10,307** vehicle entries (2019-09-01..2019-09-01) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p13 Yellowstone parkwide total vehicle entries, Monday September 2, 2019 = **8,551** vehicle entries (2019-09-02..2019-09-02) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d2 [shocks] Park closures, weather, and policy events

Hypothesis: September 2026 visitation could be affected by road closures, wildfires, government shutdown, or changes in reservation policies. Identifying any known disruptions before the cutoff and their expected impact can adjust the seasonal baseline.

Queries issued by the searcher: Yellowstone National Park closure September 2026; Yellowstone reservation system 2026 entrance; Yellowstone wildfire September 2026 closure; government shutdown September 2026 national parks; Yellowstone September 2025 visitation statistics million

- `https://home.nps.gov/yell/planyourvisit/operating-dates.htm` -> **snapshot** (snapshot 20260614230148); points raw/verified 15/3
  - p14 Canyon Repair Service last day open, Summer 2026 = **6** date (2026-09-06..2026-09-06) [keep: ] quote: "Repair Service \| Open \| May 22 \| September 6"
  - p15 Fishing Bridge Repair Service last day open, Summer 2026 = **1** date (2026-09-01..2026-09-01) [keep: ] quote: "Repair Service \| Open \| May 22 \| September 1"
  - p16 Fishing Bridge Wrecker (Towing) Service last day open, Summer 2026 = **6** date (2026-09-06..2026-09-06) [keep: ] quote: "Wrecker (Towing) Service \| Open \| May 22 \| September 6"
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/0
- `https://www.nps.gov/yell/planyourvisit/situationreport.htm` -> **snapshot** (snapshot 20260618033531); points raw/verified 0/0
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 27 (period_end 2026-09-13 after as_of: 5; period_end 2026-09-09 after as_of: 1; period_end 2026-09-20 after as_of: 1; period_end 2026-09-26 after as_of: 1; period_end 2026-09-27 after as_of: 2; period_end 2026-09-14 after as_of: 1; period_end 2026-09-07 after as_of: 1; period_end 2026-10-31 after as_of: 7; period_end 2026-10-12 after as_of: 4; period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 1; number: no number in value_as_written: 1)

### d3 [related_series] NPS-wide or park-group visitation trends

Hypothesis: Yellowstone's visitation is correlated with overall National Park System visitation and with other large western parks. If NPS-wide or regional September 2026 data are available, they can provide a scaling factor or trend adjustment for Yellowstone.

Queries issued by the searcher: NPS national visitation statistics September 2025 recreation visits; Yellowstone National Park visitation September 2025; NPS monthly public use report September 2025 total recreation visits national park system; Grand Teton September 2025 recreation visits 2026 monthly visitation

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/orgs/1207/03-13-26-2025-visitation-statsitics.htm` -> **snapshot** (snapshot 20260903155721); points raw/verified 15/15
  - p17 NPS-wide recreation visits, 2025 annual total (all reporting parks) = **323,014,305** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- 323,014,305 recreation visits (406 parks report visitation figures)"
  - p18 NPS-wide recreation visits, 2025 annual total as stated in release text = **323,000,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Rounded restatement of p17; adds no independent information and would double-count the same NPS-wide 2025 total.] quote: "The National Park Service today announced it recorded more than 323 million recreation visits in 2025"
  - p19 NPS-wide overnight stays, 2025 annual total = **13,016,577** overnight stays (2025-01-01..2025-12-31) [keep: ] quote: "- 13,016,577 overnight stays"
  - p20 NPS-wide recreation visitor hours, 2025 annual total = **1,386,749,187** recreation visitor hours (2025-01-01..2025-12-31) [keep: ] quote: "- 1,386,749,187 recreation visitor hours"
  - p21 Number of parks setting visitation records, 2025 = **26** parks (2025-01-01..2025-12-31) [keep: ] quote: "- 26 parks set visitation records"
  - p22 Number of parks reporting visitation figures, 2025 = **406** parks (2025-01-01..2025-12-31) [keep: ] quote: "- 323,014,305 recreation visits (406 parks report visitation figures)"
  - p23 Yellowstone NP recreation visits, 2025 annual total = **4,762,988** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "- Yellowstone NP 4,762,988"
  - p24 Grand Teton NP recreation visits, 2025 annual total = **3,800,648** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Teton NP 3,800,648"
  - p25 Glacier NP recreation visits, 2025 annual total = **3,136,557** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Glacier NP 3,136,557"
  - p26 Yosemite NP recreation visits, 2025 annual total = **4,278,413** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Yosemite NP 4,278,413"
  - p27 Great Smoky Mountains NP recreation visits, 2025 annual total (top national park = **11,527,939** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Great Smoky Mountains NP 11,527,939"
  - p28 Zion NP recreation visits, 2025 annual total = **4,984,525** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Zion NP 4,984,525"
  - p29 Grand Canyon NP recreation visits, 2025 annual total = **4,430,653** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Grand Canyon NP 4,430,653"
  - p30 Rocky Mountain NP recreation visits, 2025 annual total = **4,171,431** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Rocky Mountain NP 4,171,431"
  - p31 Acadia NP recreation visits, 2025 annual total = **4,079,318** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "- Acadia NP 4,079,318"
- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260821013908); points raw/verified 0/0

### d4 [capacity_consumption] Lodging, campground, and gateway community occupancy

Hypothesis: Overnight stays in Yellowstone (lodges, campgrounds) and in gateway communities are a major component of visitation. September occupancy rates and room/campsite capacity can be used to estimate overnight visitors, which combined with day-use ratios yields total recreation visits.

Queries issued by the searcher: Yellowstone lodging occupancy September 2025 overnight stays; Yellowstone National Park campground occupancy statistics number of sites; Yellowstone September 2025 visitation 839,579 recreation visits; Xanterra Yellowstone lodging rooms 2026 occupancy September bookings

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/campgrounds.htm` -> **snapshot** (snapshot 20260821140207); points raw/verified 15/0
- `https://spotonwyoming.com/northwest-wyoming/655822/region-continues-to-buck-downward-trend.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end missing or unparseable: 6; period_end 2026-09-13 after as_of: 1; period_end 2026-09-19 after as_of: 1; period_end 2026-10-17 after as_of: 2; period_end 2026-09-26 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-10-11 after as_of: 1; period_end 2026-10-12 after as_of: 1; period_end 2026-09-27 after as_of: 1)

### d5 [base_rates] Seasonal decomposition and day-of-week effects

Hypothesis: September visitation is influenced by the number of weekends, holidays (Labor Day), and school schedules. The 2026 September calendar can be compared to prior years to adjust the seasonal baseline.

Queries issued by the searcher: Yellowstone visitation September 2025 monthly total NPS; Yellowstone daily visitation September 2025 Labor Day weekend; Yellowstone September recreation visits 2021 2022 2023 2024 monthly NPS; NPS Public Use Statistics Office monthly report Yellowstone September 2025 visitation press release

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.miamiherald.com/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aol.com/articles/data-shows-national-parks-could-194320000.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Published forecasts or tourism outlooks

Hypothesis: Tourism forecasts for Yellowstone or Wyoming may provide a directional signal for September 2026 visitation. These could be from state tourism offices, economic forecasters, or industry reports.

Queries issued by the searcher: Yellowstone visitation forecast 2026; Wyoming tourism forecast fall 2026; Yellowstone National Park economic impact 2026 visitation; National Park Service monthly public use report Yellowstone September 2025 visitation

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.com/news/article/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 7/6
  - p32 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p33 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p34 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p35 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Rounded restatement of p24 for Grand Teton 2025; redundant with the more precise NPS figure.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p36 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Rounded news figure for Grand Teton 2024; not needed for the Yellowstone September estimate and less precise than the NP] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p37 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded news figure for Grand Teton 2021; not needed for the Yellowstone September estimate and less precise than the NP] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
- `https://www.sheridanwyoming.org/wp-content/uploads/2026/08/2026-Q3-Summer-Industry-Update-WEB.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d7 [attention] Search and social media interest

Hypothesis: Online attention (Google Trends, social media mentions) for Yellowstone in the weeks before and during September 2026 may correlate with visitation. If a stable relationship exists, attention data can provide a nowcast.

Queries issued by the searcher: Google Trends Yellowstone National Park September search interest visitation correlation; Yellowstone National Park September visitation statistics NPS monthly public use report; Google Trends search interest predict national park visitation correlation study; Yellowstone September visitation 2024 2023 recreation visits month by month NPS

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p38 Average number of visits to Yellowstone National Park in September, 2014-2018 av = **663,651** visits (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p39 September visits as percentage of average annual visits to Yellowstone National  = **16.51** % (2014-09-01..2018-09-30) [EXCLUDED (ablation): ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p40 Average number of visits to Yellowstone National Park in January, 2014-2018 aver = **28,837** visits (2014-01-01..2018-01-31) [EXCLUDED (ablation): ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p41 Average number of visits to Yellowstone National Park in February, 2014-2018 ave = **33,088** visits (2014-02-01..2018-02-28) [EXCLUDED (ablation): ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p42 Average number of visits to Yellowstone National Park in March, 2014-2018 averag = **22,266** visits (2014-03-01..2018-03-31) [EXCLUDED (ablation): ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p43 Average number of visits to Yellowstone National Park in April, 2014-2018 averag = **44,027** visits (2014-04-01..2018-04-30) [EXCLUDED (ablation): ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p44 Average number of visits to Yellowstone National Park in May, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [EXCLUDED (ablation): ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p45 Average number of visits to Yellowstone National Park in June, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [EXCLUDED (ablation): ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p46 Average number of visits to Yellowstone National Park in July, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [EXCLUDED (ablation): ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p47 Average number of visits to Yellowstone National Park in August, 2014-2018 avera = **839,787** visits (2014-08-01..2018-08-31) [EXCLUDED (ablation): ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p48 Average number of visits to Yellowstone National Park in October, 2014-2018 aver = **223,777** visits (2014-10-01..2018-10-31) [EXCLUDED (ablation): ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p49 Average number of visits to Yellowstone National Park in November, 2014-2018 ave = **14,323** visits (2014-11-01..2018-11-30) [EXCLUDED (ablation): ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p50 Average number of visits to Yellowstone National Park in December, 2014-2018 ave = **20,434** visits (2014-12-01..2018-12-31) [EXCLUDED (ablation): ] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://experts.boisestate.edu/en/publications/bringing-forecasting-into-the-future-using-google-to-predict-visi/` -> **snapshot** (snapshot 20260514201457); points raw/verified 5/1
  - p51 Share of total visitation variation to all U.S. National Parks predicted one yea = **97** % (2013-01-01..2017-12-31) [DISCARD: General NPS-wide Google Trends result from 2013-2017; no Yellowstone-specific September 2026 attention series is availab] quote: "our Google Trends model accurately predicted 97% of the total visitation variation to all parks one year in advance from 2013-2017"
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### b1 [physical_flow] d1

Hypothesis: A parkwide daily vehicle-entry count for any day in September 2026, or a September 2026 monthly vehicle-entry total, would directly anchor the physical-flow route and reduce reliance on the 2019/2021 Labor Day analogue.

Queries issued by the searcher: Yellowstone National Park September 2026 visitation statistics; NPS Yellowstone monthly public use report September 2026 recreation visits; Yellowstone National Park vehicle entries September 2026 entrance station counts; Yellowstone visitation August 2026 news release recreation visits

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://local.newsbreak.com/news/4893899508406-yellowstone-sees-millions-of-summer-tourists-in-2026-as-west-entrance-handles-43-of-vehicle-traffic` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://creators.yahoo.com/lifestyle/story/for-the-first-time-in-hi-210710452.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] d3

Hypothesis: Yellowstone September recreation visits for 2022-2025 would provide a recent seasonal baseline and a year-over-year trend, replacing the older 2019/2021 vehicle-entry analogue.

Queries issued by the searcher: NPS Monthly Public Use Report Yellowstone September recreation visits 2024; Yellowstone visitation September 2023 recreation visits NPS statistics; Yellowstone visitation statistics September 2025 recreation visits; "Yellowstone" September 2025 visitation "recreation visits" park hosted

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/23038.htm` -> **snapshot** (snapshot 20260214203637); points raw/verified 13/13
  - p52 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 838,458 recreation visits in September 2023."
  - p53 Yellowstone National Park recreation visits, September 2022 = **567,587** recreation visits (2022-09-01..2022-09-30) [EXCLUDED (ablation): ] quote: "This is a 48% increase from September 2022 (567,587 recreational visits)"
  - p54 Yellowstone National Park recreation visits, September 2019 = **693,118** recreation visits (2019-09-01..2019-09-30) [EXCLUDED (ablation): ] quote: "a 21% increase from September 2019* (693,118 recreational visits)."
  - p55 Year-over-year percent increase in Yellowstone recreation visits, September 2023 = **48** % (2023-09-01..2023-09-30) [EXCLUDED (ablation): ] quote: "This is a 48% increase from September 2022 (567,587 recreational visits)"
  - p56 Percent increase in Yellowstone recreation visits, September 2023 vs September 2 = **21** % (2023-09-01..2023-09-30) [EXCLUDED (ablation): ] quote: "and a 21% increase from September 2019* (693,118 recreational visits)."
  - p57 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,161,602** recreation visits (2023-01-01..2023-09-30) [EXCLUDED (ablation): ] quote: "So far in 2023, the park has hosted 4,161,602 recreation visits"
  - p58 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [EXCLUDED (ablation): ] quote: "up 38% from 2022 (3,005,194 recreation visits)"
  - p59 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [EXCLUDED (ablation): ] quote: "and up 9% from 2019 (3,807,815 recreation visits)."
  - p60 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [EXCLUDED (ablation): ] quote: "2021 - 4,472,687"
  - p61 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [EXCLUDED (ablation): ] quote: "2020 - 3,393,642 (The park was closed March 24 through May 17."
  - p62 Yellowstone National Park year-to-date recreation visits through September 2018 = **3,860,695** recreation visits (2018-01-01..2018-09-30) [EXCLUDED (ablation): ] quote: "2018 - 3,860,695"
  - p63 Percent increase in Yellowstone year-to-date recreation visits through September = **38** % (2023-01-01..2023-09-30) [EXCLUDED (ablation): ] quote: "the park has hosted 4,161,602 recreation visits, up 38% from 2022"
  - p64 Percent increase in Yellowstone year-to-date recreation visits through September = **9** % (2023-01-01..2023-09-30) [EXCLUDED (ablation): ] quote: "and up 9% from 2019 (3,807,815 recreation visits)."
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] d2

Hypothesis: Any September 2026 road closure, wildfire, reservation policy, or government shutdown would materially shift September 2026 visitation away from the seasonal baseline; identifying it would determine whether an adjustment is needed.

Queries issued by the searcher: Yellowstone National Park September 2026 road closure construction; Yellowstone National Park 2026 reservation system timed entry; Yellowstone wildfire September 2026 closure; government shutdown 2026 national parks September 30 funding deadline

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm?pubDate=20260625` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://local.newsbreak.com/news/4863047323691-yellowstone-and-grand-teton-fall-guide-plan-around-fire-road-and-service-changes` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grizzlyrv.com/does-yellowstone-have-timed-entry/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone september visits', 'yellowstone visitation 2026', 'nps monthly visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] Entrance-level vehicle counts for Friday 2021-09-03 sum to the parkwide total p6 (882+1718+477+1750+4118=8945), so these are internally consistent components of the same measurement system, not indepe
- corroborating: ['p6', 'p7', 'p8', 'p9'] Parkwide daily vehicle-entry counts for the 2021 Labor Day weekend form a coherent Friday-Monday profile from the same NPS entrance-station source.
- corroborating: ['p10', 'p11', 'p12', 'p13'] Parkwide daily vehicle-entry counts for the 2019 Labor Day weekend form a second coherent Friday-Monday profile from the same NPS source; they are a different year and therefore a useful analogue, not
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13'] The 2019 and 2021 Labor Day weekend vehicle-entry profiles are similar in shape and level, supporting use of a Labor Day weekend vehicle-entry profile as a stable seasonal anchor.
- corroborating: ['p17', 'p18'] p17 and p18 are the same NPS 2025 annual visitation release, one exact and one rounded; they are redundant copies of the same underlying statistic.
- corroborating: ['p24', 'p35'] Grand Teton 2025 annual recreation visits are reported as 3,800,648 (p24) and 3.8 million (p35), consistent rounded versions of the same NPS figure.
- corroborating: ['p14', 'p15', 'p16'] Canyon and Fishing Bridge repair/towing service end dates in early September 2026 indicate the summer 2026 visitor-services season is winding down in the first week of September, consistent with norma
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] Entrance-level vehicle counts for Friday 2021-09-03 sum to the parkwide total p6 (882+1718+477+1750+4118=8945), so these are internally consistent components of the same measurement system, not indepe
- corroborating: ['p6', 'p7', 'p8', 'p9'] Consecutive daily parkwide vehicle-entry counts for Labor Day weekend 2021 form a single coherent daily series; they share the same measurement source and are not independent of one another.
- corroborating: ['p10', 'p11', 'p12', 'p13'] Consecutive daily parkwide vehicle-entry counts for Labor Day weekend 2019 form a single coherent daily series from the same source; they are a prior-year analogue, not an independent confirmation of 
- corroborating: ['p6', 'p10'] The 2021 and 2019 Labor Day weekend daily vehicle-entry series show similar day-of-week shape and magnitude, supporting use of the 2019/2021 weekend pattern as a seasonal analogue for early September.
- corroborating: ['p17', 'p18'] The precise 2025 NPS-wide recreation-visit total and the rounded figure in the release text describe the same quantity; p18 is a rounded restatement of p17, not an independent measurement.
- corroborating: ['p24', 'p35'] Grand Teton 2025 annual recreation visits are reported as 3,800,648 (p24) and 3.8 million (p35); these are the same underlying figure at different precision.
- corroborating: ['p35', 'p36', 'p37'] The Grand Teton 2024 and 2021 annual figures come from the same news article and are consistent with the 2025 figure; they provide a recent trend context for a nearby large western park.
- corroborating: ['p17', 'p19', 'p20', 'p21', 'p22'] These are different metrics from the same 2025 NPS annual visitation release; they describe the same reporting system and are not independent estimates of one another.
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31'] These are individual park annual totals from the same 2025 NPS release; they share the same source and reporting system and are useful as scale context, not as independent confirmations.
- corroborating: ['p14', 'p15', 'p16'] These are summer 2026 service-closure dates from the same NPS page; they indicate the end of the summer season but do not directly measure visitation.
- corroborating: ['p51'] The Google Trends predictive result is a general finding about NPS-wide visitation and is consistent with the idea that attention data can carry a visitation signal, but it is not a Yellowstone-specif

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a2 | Recreation visits per parkwide vehicle entry at Yellowstone in September | 2.6 | 2..3.4 | 1.844..3.688 (widened) | recreation visits per vehicle entry | unused | NPS recreation visits count persons, while vehicle entries count vehicles. Yellowstone is a drive-through park with high average vehicle occupancy in summer/early fall. The range reflects uncertainty in occupancy, motorcycles, pedestrians, bicycles, and repeat entries. | September 2026 vehicle mix and occupancy are broadly similar to recent September conditions at Yellowstone. | Evidence of a large shift in average vehicle occupancy, such as a major change in group travel, motorcycle share, or pedestrian/bicycle entries. |
| a4 | Recreation visits per parkwide vehicle entry at Yellowstone in September, 2019 analogue | 2.6 | 2..3.4 | 1.844..3.688 (widened) | recreation visits per vehicle entry | unused | Same conversion concept as a2 but applied to the 2019 vehicle-entry analogue. NPS recreation visits count persons, while vehicle entries count vehicles; the range reflects uncertainty in occupancy and non-vehicle entries. | September 2026 vehicle mix and occupancy are broadly similar to recent September conditions at Yellowstone. | Evidence of a large shift in average vehicle occupancy, such as a major change in group travel, motorcycle share, or pedestrian/bicycle entries. |

Rejected by code:

- a1 Ratio of September 2026 parkwide vehicle entries to the 2021 Labor Day weekend d: target-like: names the target period (2026)
- a3 Ratio of September 2026 recreation visits to the 2019 Labor Day weekend daily av: target-like: names the target period (2026)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 30 of 64
- methods allowed: ['formula_mc']

  - p23 Yellowstone NP recreation visits, 2025 annual total = 4,762,988 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p32 Yellowstone National Park annual recreation visits in 2025 = 4,760,000 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p33 Yellowstone National Park annual recreation visits in 2024 = 4,740,000 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p34 Yellowstone National Park annual recreation visits in 2021 = 4,860,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p38 Average number of visits to Yellowstone National Park in September, 2014-2018 average = 663,651 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p39 September visits as percentage of average annual visits to Yellowstone National Park, 2014 = 16.51 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p40 Average number of visits to Yellowstone National Park in January, 2014-2018 average = 28,837 (2018-01-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p41 Average number of visits to Yellowstone National Park in February, 2014-2018 average = 33,088 (2018-02-28): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p42 Average number of visits to Yellowstone National Park in March, 2014-2018 average = 22,266 (2018-03-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p43 Average number of visits to Yellowstone National Park in April, 2014-2018 average = 44,027 (2018-04-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p44 Average number of visits to Yellowstone National Park in May, 2014-2018 average = 401,449 (2018-05-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p45 Average number of visits to Yellowstone National Park in June, 2014-2018 average = 780,652 (2018-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p46 Average number of visits to Yellowstone National Park in July, 2014-2018 average = 947,688 (2018-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p47 Average number of visits to Yellowstone National Park in August, 2014-2018 average = 839,787 (2018-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p48 Average number of visits to Yellowstone National Park in October, 2014-2018 average = 223,777 (2018-10-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p49 Average number of visits to Yellowstone National Park in November, 2014-2018 average = 14,323 (2018-11-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p50 Average number of visits to Yellowstone National Park in December, 2014-2018 average = 20,434 (2018-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p52 Yellowstone National Park recreation visits, September 2023 = 838,458 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p53 Yellowstone National Park recreation visits, September 2022 = 567,587 (2022-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p54 Yellowstone National Park recreation visits, September 2019 = 693,118 (2019-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p55 Year-over-year percent increase in Yellowstone recreation visits, September 2023 vs Septem = 48 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p56 Percent increase in Yellowstone recreation visits, September 2023 vs September 2019 = 21 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p57 Yellowstone National Park year-to-date recreation visits through September 2023 = 4,161,602 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p58 Yellowstone National Park year-to-date recreation visits through September 2022 = 3,005,194 (2022-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p59 Yellowstone National Park year-to-date recreation visits through September 2019 = 3,807,815 (2019-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p60 Yellowstone National Park year-to-date recreation visits through September 2021 = 4,472,687 (2021-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p61 Yellowstone National Park year-to-date recreation visits through September 2020 = 3,393,642 (2020-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p62 Yellowstone National Park year-to-date recreation visits through September 2018 = 3,860,695 (2018-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p63 Percent increase in Yellowstone year-to-date recreation visits through September 2023 vs s = 38 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p64 Percent increase in Yellowstone year-to-date recreation visits through September 2023 vs s = 9 (2023-09-30): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a1: assumption a1 was rejected (target-like: names the target period (2026)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: names the target period (2026)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics. A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions counts as multiple visits. Thi | unit recreation visits | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), via the Visitor Use Statistics program / monthly visitation reports

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS historical monthly visitation statistics

Hypothesis: September recreation visits to Yellowstone in recent years (e.g., 2021–2025) provide a baseline seasonal level. The 2026 September value is likely to be similar to recent Septembers, adjusted for any known trend or shocks. The ratio of September visits to the preceding August visits, or to the same year's annual total, can be used to project from known 2026 data.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September 2025; NPS Yellowstone recreation visits September 2024; Yellowstone visitation report August 2026; Yellowstone National Park visitation statistics monthly 2025 annual total

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [physical_flow] Entrance station counts and vehicle traffic

Hypothesis: Recreation visits can be approximated by vehicle entries multiplied by average occupancy, plus pedestrian/bicycle entries. If entrance station counts or traffic data for Yellowstone in September 2026 are available (e.g., from park records or road counters), they can provide a direct physical flow estimate. Historical conversion factors from vehicle counts to recreation visits can be applied.

Queries issued by the searcher: Yellowstone entrance station vehicle counts September visitation; Yellowstone average vehicle occupancy rate visitation NPS; Yellowstone National Park visitation August 2026 recreation visits news release; NPS Yellowstone September 2025 visitation 839,579 recreation visits

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 15/15
  - p1 Yellowstone parkwide total vehicle entries, Friday September 3, 2021 (Labor Day  = **8,945** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p2 Yellowstone parkwide total vehicle entries, Saturday September 4, 2021 (Labor Da = **11,062** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p3 Yellowstone parkwide total vehicle entries, Sunday September 5, 2021 (Labor Day  = **12,380** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p4 Yellowstone parkwide total vehicle entries, Monday September 6, 2021 (Labor Day  = **9,982** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p5 Yellowstone parkwide total vehicle entries, Friday August 30, 2019 (comparison d = **7,134** vehicle entries (2019-08-30..2019-08-30) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p6 Yellowstone parkwide total vehicle entries, Saturday August 31, 2019 (comparison = **8,913** vehicle entries (2019-08-31..2019-08-31) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p7 Yellowstone parkwide total vehicle entries, Sunday September 1, 2019 (comparison = **10,307** vehicle entries (2019-09-01..2019-09-01) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p8 Yellowstone parkwide total vehicle entries, Monday September 2, 2019 (comparison = **8,551** vehicle entries (2019-09-02..2019-09-02) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p9 Yellowstone West Entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p10 Yellowstone West Entrance vehicle entries, Saturday September 4, 2021 = **5,222** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| West \| 5,222 \| 4,640 \| 13% \|"
  - p11 Yellowstone West Entrance vehicle entries, Sunday September 5, 2021 = **5,536** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| West \| 5,536 \| 5,064 \| 9% \|"
  - p12 Yellowstone West Entrance vehicle entries, Monday September 6, 2021 = **4,293** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| West \| 4,293 \| 3,599 \| 19% \|"
  - p13 Yellowstone East Entrance vehicle entries, Sunday September 5, 2021 = **1,506** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| East \| 1,506 \| 1,204 \| 25% \|"
  - p14 Yellowstone North Entrance vehicle entries, Sunday September 5, 2021 = **2,435** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| North \| 2,435 \| 1,964 \| 24% \|"
  - p15 Yellowstone South Entrance vehicle entries, Sunday September 5, 2021 = **2,100** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| South \| 2,100 \| 1,116 \| 88% \|"
- `https://discoverdreamlands.com/journey/yellowstone-national-park-tourism-statistics` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [shocks] Park closures, weather, and travel disruptions

Hypothesis: September 2026 visitation could be affected by road closures, wildfires, flooding, government shutdown, or unusual weather. Identifying any such events and their expected impact (e.g., closure days, area affected) can adjust a baseline estimate. Historical analogues (e.g., 2022 flood, 2013 shutdown) show the magnitude of impact.

Queries issued by the searcher: Yellowstone closure September 2026; Yellowstone National Park visitation statistics September 2025; Yellowstone road closure August 2026; Yellowstone National Park wildfire 2026 closure

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 16/0
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cz/zpr%C3%A1vy/%C4%8Dl%C3%A1nek/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 2; period_end 2026-10-31 after as_of: 3; number: more than one number in value_as_written: 4; number: no number in value_as_written: 4; period_end 2026-12-31 after as_of: 1)

### d4 [related_series] NPS-wide or regional visitation trends

Hypothesis: Yellowstone's visitation often moves with broader National Park System visitation or with other large western parks (e.g., Grand Teton, Glacier). If NPS-wide or regional September 2026 data are available earlier, they can indicate whether 2026 is a high or low year relative to 2025, and the share Yellowstone typically represents can be applied.

Queries issued by the searcher: National Park Service monthly visitation statistics 2026; Yellowstone National Park visitation July 2026 record; Grand Teton National Park visitation July 2026 recreation visits; Yellowstone September 2025 visitation statistics 839,000 recreation visits

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p16 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p17 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p18 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p19 Yellowstone National Park recreation visits, year-to-date through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p20 Yellowstone National Park recreation visits, year-to-date through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p21 Yellowstone National Park recreation visits, year-to-date through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p22 Yellowstone National Park recreation visits, year-to-date through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p23 Yellowstone National Park recreation visits, year-to-date through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p24 Yellowstone National Park recreation visits, year-to-date through July 2022 (flo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
  - p25 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Redundant duplicate of p39/p62 (2021 record annual visits, 'over 4.8 million'); the rounded 'over 4.8 million' form is n] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67a0670c-6a6d-4e32-be3f-0d4aa6730b8a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/july-numbers-in-grand-teton-push-2026-visitation-over-2-million/` -> **snapshot** (snapshot 20260815071816); points raw/verified 10/10
  - p26 Grand Teton National Park recreation visits, July 2026 = **773,094** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "The park saw 773,094 recreation visits during July, a nearly 2% decrease from July 2025"
  - p27 Grand Teton National Park recreation visits, July 2025 = **787,186** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "a nearly 2% decrease from July 2025, when the park saw 787,186 visits"
  - p28 Grand Teton National Park recreation visits, July 2021 (record year) = **835,846** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation was down 7.5% from July 2021 (835,846 recreation visits), which was the park's record-breaking year"
  - p29 Grand Teton National Park total recreation visits, record year 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded 'over 3.88 million' Grand Teton 2021 annual total; not needed because Grand Teton enters only as a same-period r] quote: "which was the park's record-breaking year with over 3.88 million visits"
  - p30 Grand Teton National Park recreation visits, January–July 2026 year-to-date = **2,074,026** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far this year, GTNP has hosted 2,074,026 recreation visits, up almost 1% over the same time frame in 2025"
  - p31 Grand Teton National Park recreation visits, January–July 2025 year-to-date = **2,055,783** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "up almost 1% over the same time frame in 2025 (2,055,783 visits)"
  - p32 Grand Teton National Park recreation visits, January–July 2021 year-to-date = **2,240,805** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "This year's January through July total is down about 7% from 2021's numbers (2,240,805 visits)"
  - p33 Grand Teton National Park recreation visits, January–July 2024 year-to-date = **1,987,288** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "- 2024 - 1,987,288"
  - p34 Grand Teton National Park recreation visits, January–July 2023 year-to-date = **1,787,695** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "- 2023 - 1,787,695"
  - p35 Grand Teton National Park recreation visits, January–July 2022 year-to-date = **1,547,782** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "- 2022 - 1,547,782"
- `https://www.nps.gov/yell/learn/news/26016.htm` -> **snapshot** (snapshot 20260714213711); points raw/verified 10/10
  - p36 Yellowstone National Park recreation visits, June 2026 = **903,025** recreation visits (2026-06-01..2026-06-30) [keep: ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p37 Yellowstone National Park recreation visits, June 2025 = **928,250** recreation visits (2025-06-01..2025-06-30) [keep: ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p38 Yellowstone National Park recreation visits, June 2021 = **938,845** recreation visits (2021-06-01..2021-06-30) [keep: ] quote: "Visitation in June 2026 showed a 4% decrease from June 2021 (938,845 recreation visits)."
  - p39 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Redundant duplicate of p62 (2021 record annual visits, 'over 4.8 million'); rounded and not usable as a precise annual d] quote: "The park's record-breaking year was 2021 with over 4.8 million recreation visits."
  - p40 Yellowstone National Park year-to-date recreation visits through June 2026 = **1,676,678** recreation visits (2026-01-01..2026-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p41 Yellowstone National Park year-to-date recreation visits through June 2025 = **1,690,922** recreation visits (2025-01-01..2025-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p42 Yellowstone National Park year-to-date recreation visits through June 2021 = **1,587,998** recreation visits (2021-01-01..2021-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p43 Yellowstone National Park year-to-date recreation visits through June 2024 = **1,633,739** recreation visits (2024-01-01..2024-06-30) [keep: ] quote: "2024 - 1,633,739"
  - p44 Yellowstone National Park year-to-date recreation visits through June 2023 = **1,492,843** recreation visits (2023-01-01..2023-06-30) [keep: ] quote: "2023 - 1,492,843"
  - p45 Yellowstone National Park year-to-date recreation visits through June 2022 = **1,258,834** recreation visits (2022-01-01..2022-06-30) [keep: ] quote: "2022 - 1,258,834 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"

### d5 [capacity_consumption] Accommodation and campground occupancy

Hypothesis: Overnight stays in Yellowstone (lodges, campgrounds) are a component of recreation visits. Occupancy rates and available rooms/campsites in September 2026 can indicate the level of overnight visitation, which can be combined with day-use estimates. Historical ratios of overnight stays to total recreation visits can bridge to the target.

Queries issued by the searcher: Yellowstone lodging occupancy September 2026; Yellowstone National Park monthly visitation statistics September 2025; Yellowstone September 2025 recreation visits NPS press release 839,579; Yellowstone National Park Lodges occupancy rate 2025 Xanterra lodging

- `https://www.bnbcalc.com/fr/markets/us/yellowstone-national-park-wy` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bnbcalc.com/markets/us/yellowstone-national-park-wy` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bnbcalc.com/pt/markets/us/yellowstone-national-park-wy` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://localaisource.com/industries/hospitality/wyoming` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [base_rates] Seasonal decomposition and day-count effects

Hypothesis: September visitation is influenced by the number of weekends, holidays (Labor Day), and school schedules. The timing of Labor Day (first Monday in September) and the number of weekend days can shift visitation. Historical September daily patterns can be used to adjust for calendar differences between 2026 and prior years.

Queries issued by the searcher: Yellowstone National Park September visitation statistics NPS monthly; Yellowstone visitation Labor Day weekend September 2025; Yellowstone September 2025 visitation statistics news release NPS recreation visits; Yellowstone weekly visitation pattern September daily entries 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p46 Yellowstone National Park average September visits, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p47 September share of average annual visits at Yellowstone, 2014-2018 average = **16.51** % (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p48 Yellowstone National Park average August visits, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p49 Yellowstone National Park average October visits, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p50 Yellowstone National Park average July visits, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p51 Yellowstone National Park average June visits, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p52 Yellowstone National Park average May visits, 2014-2018 average = **401,449** visits (2014-05-01..2014-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p53 Yellowstone National Park average January visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p54 Yellowstone National Park average February visits, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p55 Yellowstone National Park average March visits, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p56 Yellowstone National Park average April visits, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p57 Yellowstone National Park average November visits, 2014-2018 average = **14,323** visits (2014-11-01..2018-11-30) [keep: ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p58 Yellowstone National Park average December visits, 2014-2018 average = **20,434** visits (2014-12-01..2018-12-31) [keep: ] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://www.newsfromthestates.com/article/yellowstone-national-park-sees-bump-2025-visits-so-far` -> **snapshot** (snapshot 20260708061202); points raw/verified 10/10
  - p59 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone said it hosted 881,936 recreation visits in August 2025 compared to 868,259 recreation visits one year ago."
  - p60 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "Yellowstone said it hosted 881,936 recreation visits in August 2025 compared to 868,259 recreation visits one year ago."
  - p61 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021, with 921,844 recreation visits then, the park said."
  - p62 Yellowstone National Park record-breaking year 2021 recreation visits (more than = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded 'more than 4.8 million' 2021 annual figure; superseded by the precise 2021 monthly/YTD values already kept, and ] quote: "The park's record-breaking year was 2021, with more than 4.8 million recreation visits."
  - p63 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p64 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p65 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p66 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p67 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood. Three entrances opened on June 22.)"
  - p68 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://thegirlwithabigbag.com/yellowstone-in-fall/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Travel industry forecasts and prediction markets

Hypothesis: Travel forecasts for national parks in 2026, or prediction markets on Yellowstone visitation, could provide a direct or indirect estimate. If a market exists for Yellowstone September 2026 visits, its price can be used as a forecast. Otherwise, travel industry reports on summer 2026 park travel may indicate overall demand.

Queries issued by the searcher: Yellowstone visitation prediction market 2026; national park tourism forecast 2026; Yellowstone National Park visitation statistics September monthly report; Yellowstone travel bookings September 2026

- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 14/14
  - p69 Yellowstone National Park average September recreation visits, 2014-2018 average = **663,651** recreation visits (2014-09-01..2018-09-30) [DISCARD: Redundant duplicate of p46 (same September 2014-2018 average, same source and snapshot); adds no independent information] quote: "\| September \| 663,651 \| 16.51% \|"
  - p70 Yellowstone National Park average annual recreation visits, 2014-2018 average = **663,651** recreation visits (2014-01-01..2018-12-31) [DISCARD: Mislabeled: the quote gives the September monthly value (663,651) but the row is named 'average annual recreation visits] quote: "\| September \| 663,651 \| 16.51% \|"
  - p71 September share of average annual Yellowstone recreation visits, 2014-2018 avera = **16.51** % (2014-01-01..2018-12-31) [DISCARD: Duplicate of the September share already present as p47; same underlying NPS table.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p72 Yellowstone National Park average January recreation visits, 2014-2018 average = **28,837** recreation visits (2014-01-01..2018-01-31) [DISCARD: Redundant duplicate of p53 (January 2014-2018 average).] quote: "\| January \| 28,837 \| 0.72% \|"
  - p73 Yellowstone National Park average February recreation visits, 2014-2018 average = **33,088** recreation visits (2014-02-01..2018-02-28) [DISCARD: Redundant duplicate of p54 (February 2014-2018 average).] quote: "\| February \| 33,088 \| 0.82% \|"
  - p74 Yellowstone National Park average March recreation visits, 2014-2018 average = **22,266** recreation visits (2014-03-01..2018-03-31) [DISCARD: Redundant duplicate of p55 (March 2014-2018 average).] quote: "\| March \| 22,266 \| 0.55% \|"
  - p75 Yellowstone National Park average April recreation visits, 2014-2018 average = **44,027** recreation visits (2014-04-01..2018-04-30) [DISCARD: Redundant duplicate of p56 (April 2014-2018 average).] quote: "\| April \| 44,027 \| 1.10% \|"
  - p76 Yellowstone National Park average May recreation visits, 2014-2018 average = **401,449** recreation visits (2014-05-01..2018-05-31) [DISCARD: Redundant duplicate of p52 (May 2014-2018 average).] quote: "\| May \| 401,449 \| 9.99% \|"
  - p77 Yellowstone National Park average June recreation visits, 2014-2018 average = **780,652** recreation visits (2014-06-01..2018-06-30) [DISCARD: Redundant duplicate of p51 (June 2014-2018 average).] quote: "\| June \| 780,652 \| 19.42% \|"
  - p78 Yellowstone National Park average July recreation visits, 2014-2018 average = **947,688** recreation visits (2014-07-01..2018-07-31) [DISCARD: Redundant duplicate of p50 (July 2014-2018 average).] quote: "\| July \| 947,688 \| 23.57% \|"
  - p79 Yellowstone National Park average August recreation visits, 2014-2018 average = **839,787** recreation visits (2014-08-01..2018-08-31) [DISCARD: Redundant duplicate of p48 (August 2014-2018 average).] quote: "\| August \| 839,787 \| 20.89% \|"
  - p80 Yellowstone National Park average October recreation visits, 2014-2018 average = **223,777** recreation visits (2014-10-01..2018-10-31) [DISCARD: Redundant duplicate of p49 (October 2014-2018 average).] quote: "\| October \| 223,777 \| 5.57% \|"
  - p81 Yellowstone National Park average November recreation visits, 2014-2018 average = **14,323** recreation visits (2014-11-01..2018-11-30) [DISCARD: Redundant duplicate of p57 (November 2014-2018 average).] quote: "\| November \| 14,323 \| 0.36% \|"
  - p82 Yellowstone National Park average December recreation visits, 2014-2018 average = **20,434** recreation visits (2014-12-01..2018-12-31) [DISCARD: Redundant duplicate of p58 (December 2014-2018 average).] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://www.travelweekly.com/Travel-News/Tour-Operators/National-park-bookings-summer-2026` -> **snapshot** (snapshot 20260512135409); points raw/verified 8/0
- dropped by code checks: 8 (period_end 2026-12-31 after as_of: 2; period_end missing or unparseable: 5; number: no number in value_as_written: 1)

### d8 [administrative] Permits, reservations, and fees

Hypothesis: Administrative data such as backcountry permits, fishing licenses, or entrance fee receipts can serve as proxies for visitation levels. Changes in these administrative counts relative to total visits can indicate whether September 2026 is above or below historical norms.

Queries issued by the searcher: Yellowstone backcountry permits September statistics; Yellowstone National Park monthly visitation statistics September 2025; Yellowstone backcountry campsite overnight stays September 2025 NPS visitor use statistics; Yellowstone entrance fee revenue monthly 2025 recreation fee collection; Yellowstone National Park September 2025 visitation news release 839,579

- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://publiclandsdata.com/national-park-visitation/yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://publiclandsdata.com/reservations/yell` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] NPS monthly visitation series

Hypothesis: September recreation visits for Yellowstone in 2021–2025 would provide the direct target-history series needed for series_naive and for a September-to-August ratio; currently only the 2014–2018 average September level is available, so the estimate relies on an older seasonal profile.

Queries issued by the searcher: Yellowstone National Park September 2024 recreation visits NPS monthly visitation statistics; NPS Visitor Use Statistics Yellowstone monthly recreation visits September 2021 2022 2023; Yellowstone visitation statistics for September 2025 recreation visits; Yellowstone National Park monthly visitation 2025 August September recreation visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Regional park demand

Hypothesis: Grand Teton September 2026 or August 2026 recreation visits would provide a same-period regional signal to scale Yellowstone's September level; currently only Grand Teton July and year-to-date data are available, which limits the transfer to a summer-season indicator.

Queries issued by the searcher: Grand Teton National Park monthly recreation visits August 2026; NPS Visitor Use Statistics monthly visitation report September 2026; buckrail Grand Teton visitation July 2026 recreation visits; Yellowstone visitation August 2026 recreation visits monthly report

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67a0670c-6a6d-4e32-be3f-0d4aa6730b8a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/year-to-date-visitation-in-grand-teton-nearly-identical-to-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mtstandard.com/outdoors/article_123dc146-aca3-5941-a680-55bd0ff36d57.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jhnewsandguide.com/news/business/market-watch-airport-sets-all-time-record-for-monthly-traffic/article_bd0ceec6-da2f-42df-9994-3f32b7e1546` -> **snapshot** (snapshot 20260903100652); points raw/verified 13/13
  - p83 Grand Teton National Park recreational visitation total, July 2026 = **773,094** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "In July, Grand Teton National Park's recreational visitation total was 773,094, a 1.8% decrease from the number visiting in July 2025."
  - p84 Grand Teton National Park recreational visitation, July 2026 vs July 2025 percen = **1.8** % (2026-07-01..2026-07-31) [keep: ] quote: "In July, Grand Teton National Park's recreational visitation total was 773,094, a 1.8% decrease from the number visiting in July 2025."
  - p85 Grand Teton National Park recreational visits, fiscal year ending July 2026 = **3,806,677** recreation visits (2025-08-01..2026-07-31) [keep: ] quote: "During the fiscal year ending in July 2026, 3,806,677 people paid a recreational visit to Grand Teton, 3.0% more than visited during the previous 12 months."
  - p86 Grand Teton National Park recreational visits, fiscal year ending July 2026 vs p = **3** % (2025-08-01..2026-07-31) [keep: ] quote: "During the fiscal year ending in July 2026, 3,806,677 people paid a recreational visit to Grand Teton, 3.0% more than visited during the previous 12 months."
  - p87 Yellowstone National Park recreational visitation count, July 2026 = **958,705** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "In July, Yellowstone National Park's recreational visitation count totaled 958,705, 1.7% lower than July 2025's figure."
  - p88 Yellowstone National Park recreational visitation, July 2026 vs July 2025 percen = **1.7** % (2026-07-01..2026-07-31) [keep: ] quote: "In July, Yellowstone National Park's recreational visitation count totaled 958,705, 1.7% lower than July 2025's figure."
  - p89 Yellowstone National Park recreational visits, fiscal year ending July 2026 = **4,732,516** recreation visits (2025-08-01..2026-07-31) [keep: ] quote: "During the fiscal year ending in July, 4,732,516 people paid a recreational visit to Yellowstone, 1.1% fewer than during the previous 12 months."
  - p90 Yellowstone National Park recreational visits, fiscal year ending July 2026 vs p = **1.1** % (2025-08-01..2026-07-31) [keep: ] quote: "During the fiscal year ending in July, 4,732,516 people paid a recreational visit to Yellowstone, 1.1% fewer than during the previous 12 months."
  - p91 Jackson Hole Airport enplanements, July 2026 = **83,388** passengers enplaning a commercial airline flight (2026-07-01..2026-07-31) [keep: ] quote: "In July, enplanements at Jackson Hole Airport totaled 83,388, 8.6% more than the number of passengers who enplaned a commercial airline flight in July 2025."
  - p92 Jackson Hole Airport enplanements, July 2026 vs July 2025 percent change = **8.6** % (2026-07-01..2026-07-31) [keep: ] quote: "In July, enplanements at Jackson Hole Airport totaled 83,388, 8.6% more than the number of passengers who enplaned a commercial airline flight in July 2025."
  - p93 Jackson Hole Airport enplanements, fiscal year ending July 2026 = **598,923** passengers enplaning a commercial airline flight (2025-08-01..2026-07-31) [keep: ] quote: "during the fiscal year ending in July enplanements were up overall, totaling 598,923."
  - p94 Jackson Hole Airport enplanements, fiscal year ending July 2026 vs previous 12 m = **8.2** % (2025-08-01..2026-07-31) [keep: ] quote: "This was 8.2% higher than the previous 12 months and is the highest fiscal year total in the airport's history."
  - p95 Jackson Hole Airport previous monthly enplanement high, July 2021 = **7.2** % (2026-07-01..2026-07-31) [DISCARD: Percent comparison of July 2026 enplanements to the July 2021 high; redundant with p91/p92 and not usable as a level inp] quote: "eclipsing the previous high of July 2021 by a healthy 7.2%."

### b3 [shocks] Park operations and access

Hypothesis: Any September 2026 road closures, wildfire smoke, flooding, or government shutdown affecting Yellowstone would materially change September visitation relative to the seasonal baseline; no such event is currently represented in the kept data.

Queries issued by the searcher: Yellowstone National Park September 2026 road closures; Yellowstone visitation statistics September monthly report NPS; Yellowstone National Park wildfire September 2026 smoke; Yellowstone National Park news release August 2026 visitation July 2026

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/0
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p96 Average number of visits to Yellowstone National Park in September, 2014-2018 av = **663,651** visits (2014-09-01..2018-09-30) [DISCARD: Redundant duplicate of p46 (September 2014-2018 average).] quote: "\| September \| 663,651 \| 16.51% \|"
  - p97 September share of average annual visits to Yellowstone National Park, 2014-2018 = **16.51** % (2014-09-01..2018-09-30) [DISCARD: Redundant duplicate of p47 (September share of annual visits).] quote: "\| September \| 663,651 \| 16.51% \|"
  - p98 Average number of visits to Yellowstone National Park in January, 2014-2018 aver = **28,837** visits (2014-01-01..2018-01-31) [DISCARD: Redundant duplicate of p53 (January 2014-2018 average).] quote: "\| January \| 28,837 \| 0.72% \|"
  - p99 Average number of visits to Yellowstone National Park in February, 2014-2018 ave = **33,088** visits (2014-02-01..2018-02-28) [DISCARD: Redundant duplicate of p54 (February 2014-2018 average).] quote: "\| February \| 33,088 \| 0.82% \|"
  - p100 Average number of visits to Yellowstone National Park in March, 2014-2018 averag = **22,266** visits (2014-03-01..2018-03-31) [DISCARD: Redundant duplicate of p55 (March 2014-2018 average).] quote: "\| March \| 22,266 \| 0.55% \|"
  - p101 Average number of visits to Yellowstone National Park in April, 2014-2018 averag = **44,027** visits (2014-04-01..2018-04-30) [DISCARD: Redundant duplicate of p56 (April 2014-2018 average).] quote: "\| April \| 44,027 \| 1.10% \|"
  - p102 Average number of visits to Yellowstone National Park in May, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [DISCARD: Redundant duplicate of p52 (May 2014-2018 average).] quote: "\| May \| 401,449 \| 9.99% \|"
  - p103 Average number of visits to Yellowstone National Park in June, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [DISCARD: Redundant duplicate of p51 (June 2014-2018 average).] quote: "\| June \| 780,652 \| 19.42% \|"
  - p104 Average number of visits to Yellowstone National Park in July, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [DISCARD: Redundant duplicate of p50 (July 2014-2018 average).] quote: "\| July \| 947,688 \| 23.57% \|"
  - p105 Average number of visits to Yellowstone National Park in August, 2014-2018 avera = **839,787** visits (2014-08-01..2018-08-31) [DISCARD: Redundant duplicate of p48 (August 2014-2018 average).] quote: "\| August \| 839,787 \| 20.89% \|"
  - p106 Average number of visits to Yellowstone National Park in October, 2014-2018 aver = **223,777** visits (2014-10-01..2018-10-31) [DISCARD: Redundant duplicate of p49 (October 2014-2018 average).] quote: "\| October \| 223,777 \| 5.57% \|"
  - p107 Average number of visits to Yellowstone National Park in November, 2014-2018 ave = **14,323** visits (2014-11-01..2018-11-30) [DISCARD: Redundant duplicate of p57 (November 2014-2018 average).] quote: "\| November \| 14,323 \| 0.36% \|"
  - p108 Average number of visits to Yellowstone National Park in December, 2014-2018 ave = **20,434** visits (2014-12-01..2018-12-31) [DISCARD: Redundant duplicate of p58 (December 2014-2018 average).] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 1; period_end 2026-10-31 after as_of: 3; number: no number in value_as_written: 4; number: more than one number in value_as_written: 1; period_end 2026-09-15 after as_of: 1; period_end 2026-12-31 after as_of: 1; period_end missing or unparseable: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone september visits', 'yellowstone visitation 2026', 'national park visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] Daily parkwide vehicle-entry counts for the 2021 Labor Day weekend; same measurement system and source, useful as a physical-flow analogue for early-September demand but not a recreation-visit count.
- corroborating: ['p5', 'p6', 'p7', 'p8'] 2019 comparison days for the same Labor Day weekend dates; same entrance-count system, useful for calendar-alignment and year-over-year comparison, but not a September total.
- corroborating: ['p9', 'p10', 'p11', 'p12'] West Entrance daily vehicle entries for the 2021 Labor Day weekend; a component of the parkwide totals p1–p4, not independent of them.
- corroborating: ['p13', 'p14', 'p15'] East, North, and South Entrance daily vehicle entries for Sunday 2021-09-05; components of the parkwide total p3, not independent of it.
- corroborating: ['p16', 'p17', 'p18'] July recreation visits for 2026, 2025, and 2021 from the same NPS release; consistent with a modest 2026 decline from 2025 and a larger decline from the 2021 record.
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24'] Year-to-date through July recreation visits for 2026, 2025, 2021, 2024, 2023, and 2022; same NPS series, showing 2026 slightly below 2025 and well above the flood-affected 2022.
- corroborating: ['p36', 'p37', 'p38'] June recreation visits for 2026, 2025, and 2021; same NPS series, showing a 3% year-over-year decline in June 2026.
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45'] Year-to-date through June recreation visits for 2026, 2025, 2021, 2024, 2023, and 2022; same NPS series, consistent with the through-July pattern.
- corroborating: ['p59', 'p60', 'p61'] August recreation visits for 2025, 2024, and 2021; same NPS series, showing August 2025 slightly above August 2024 but below August 2021.
- corroborating: ['p63', 'p64', 'p65', 'p66', 'p67', 'p68'] Year-to-date through August recreation visits for 2025, 2024, 2021, 2023, 2022, and 2020; same NPS series, useful for seasonal-share and trend context.
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] 2014–2018 average monthly visitation and September share; same NPS seasonal profile, useful for the September-to-August ratio and September share of annual visits, but based on an older period.
- corroborating: ['p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82'] Duplicate copies of the 2014–2018 monthly averages and September share already represented by p46–p58; same underlying NPS table.
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35'] Grand Teton July and year-to-date recreation visits for 2026, 2025, 2021, 2024, 2023, and 2022; a related western-park series that can indicate regional demand, but not a direct Yellowstone input.
- corroborating: ['p25', 'p39', 'p62'] Repeated statements that 2021 was Yellowstone's record year with over 4.8 million recreation visits; same fact from NPS releases, useful only as context.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p16', 'p87'] Two independent outlets report Yellowstone July 2026 recreation visits at essentially the same level (958,706 vs 958,705); the 1-unit difference is rounding, not a real discrepancy. Both trace to the 
- corroborating: ['p16', 'p17', 'p18', 'p36', 'p37', 'p38', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45'] Consistent NPS monthly/YTD series for 2021-2026: 2026 is running about 1-3% below 2025 and well below the 2021 record, with 2022 depressed by the flood. These establish the recent level and the mild 2
- corroborating: ['p59', 'p60', 'p61', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68'] August 2021/2024/2025 levels and August YTD totals are mutually consistent with the NPS monthly series and give the most recent August anchor (881,936 in 2025) needed for a September/August ratio.
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108'] Repeated copies of the same 2014-2018 NPS seasonal profile (September 663,651; August 839,787; July 947,688; etc.). They are one underlying source; the September/August and September/annual shares are
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Labor Day weekend 2021 daily vehicle-entry counts by entrance sum consistently to the parkwide totals (e.g., p9+p13+p14+p15 = p3), confirming internal consistency of the entrance-station flow data. Th
- corroborating: ['p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p83', 'p84', 'p85', 'p86'] Grand Teton July 2026 and YTD figures agree across outlets and show a regional pattern (July down ~2%, YTD up ~1%) very similar to Yellowstone's, supporting use of Grand Teton as a same-region signal 
- corroborating: ['p91', 'p92', 'p93', 'p94', 'p95'] Jackson Hole Airport enplanements (July 2026 up 8.6%, record fiscal year) indicate strong regional air access even as park visits softened; this is a demand-side signal that does not directly contradi
- corroborating: ['p89', 'p90'] Yellowstone fiscal-year-ending-July 2026 visits (4,732,516, -1.1%) are consistent with the calendar YTD series and provide an independent 12-month level check.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 Yellowstone visits relative to September 2025 | 0.98 | 0.9..1.07 | 0.6939..1.388 (widened) | ratio | m2 (m2), m3 (m3) | 2026 monthly and YTD NPS figures show Yellowstone running about 1-3% below 2025 (p16 vs p17, p19 vs p20, p36 vs p37, p89/p90), while the regional Grand Teton signal is roughly flat to slightly up (p30 vs p31, p85/p86). A modest 2% decline with a wide band centered near parity reflects the mild 2026  | September 2026 has no major closure, wildfire, flood, or shutdown materially different from September 2025, and the 2026-vs-2025 relationship seen in June-July persists into September. | Evidence of a September 2026 road closure, wildfire smoke episode, flood, or government shutdown, or a September 2026 monthly report showing a change outside the stated band. |
| a2 | September-to-August recreation-visit ratio at Yellowstone | 0.79 | 0.72..0.87 | 0.5596..1.119 (widened) | ratio | m2 (m2), m3 (m3) | The 2014-2018 NPS seasonal profile gives September 663,651 and August 839,787 (p46, p48), implying a September/August ratio near 0.79. This is the only kept seasonal-shape evidence; the band allows for year-to-year variation in shoulder-season timing and for the profile being older than the target y | The 2026 September/August seasonal shape resembles the 2014-2018 average shape, with no unusual September weather or closure. | A September 2026 monthly report showing a September/August ratio well outside the band, or evidence that shoulder-season visitation patterns have shifted materially since 2018. |
| a3 | September share of annual recreation visits at Yellowstone | 0.1651 | 0.15..0.18 | 0.1162..0.2324 (widened) | share | m4 (m4) | The 2014-2018 NPS profile reports September as 16.51% of average annual visits (p47). This share is the bridge from a 2026 annual total to the September component; the band reflects uncertainty in whether the shoulder-season share has drifted since 2018. | The 2026 seasonal distribution of visits is similar to the 2014-2018 average, and a credible 2026 annual total can be formed from the kept monthly/YTD data. | Evidence that September's share of annual visits has moved materially (e.g., a recent September monthly report implying a share outside the band). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_naive | n/a |  | [] |  | 0.00 |  | series_naive needs 1 earlier years, has 0 |
| m2 | formula_mc | 684,126 | ['p59'] / ['a1', 'a2'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 684,126 | ['p59'] / ['a1', 'a2'] | [] |  | 0.33 | equal |  |
| m4 | formula_mc | 777,522 | ['p89'] / ['a3'] | [] |  | 0.33 | equal |  |
| m5 | yoy_scaling | n/a |  | [] |  | 0.00 |  | yoy_scaling needs target for 2025 |
| m6 | ratio | n/a |  | [] |  | 0.00 |  | ratio needs >= 1 aligned year |

Result: central **713,940**, 80% interval [423,285, 1,204,178], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for recreation visits to Yellowstone National Park during September 2026, as reported in NPS monthly visitation statistics, is 713,940 visits, with an 80% interval of 423,285 to 1,204,178 (monte carlo). Code combined 3 methods, each weighted 33%; the naive and ratio routes were unusable. The estimate rests on observed August 2025 visits, a fiscal-year 2026 total, and the [n]-2018 seasonal profile, bridged by assumptions: a September 2026 change factor of 0.98 (0.6939 to 1.388), a September/August ratio of 0.79 (0.5596 to 1.119), and a September annual share of 0.1651 (0.1162 to 0.2324). The interval is model-based, conditional on these assumptions, not a demonstrated accuracy guarantee. The main risk is that the [n] softness or shoulder-season shape differs from the assumed factors. Actual September 2026 counts would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 Yellowstone visits relative to September 2025: 0.98 ratio, range 0.6939 to 1.388 (range widened by code); used by m2, m3. Overturned by: Evidence of a September 2026 road closure, wildfire smoke episode, flood, or government shutdown, or a September 2026 monthly report showing a change outside the stated band.
- a2 September-to-August recreation-visit ratio at Yellowstone: 0.79 ratio, range 0.5596 to 1.119 (range widened by code); used by m2, m3. Overturned by: A September 2026 monthly report showing a September/August ratio well outside the band, or evidence that shoulder-season visitation patterns have shifted materially since 2018.
- a3 September share of annual recreation visits at Yellowstone: 0.1651 share, range 0.1162 to 0.2324 (range widened by code); used by m4. Overturned by: Evidence that September's share of annual visits has moved materially (e.g., a recent September monthly report implying a share outside the band).

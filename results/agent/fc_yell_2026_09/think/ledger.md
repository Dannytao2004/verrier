# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Number of recreation visits to Yellowstone National Park during the full calendar month of September 2026, as reported in the National Park Service's official monthly visitation statistics (Visitor Use Statistics), not unique visitors and not a year-to-date total. | unit recreation visit | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), U.S. Department of the Interior

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS visitor-use statistician using long-run monthly tables

Hypothesis: Yellowstone September visitation has a stable seasonal relationship to adjacent months and annual totals; the 2026 September value can be estimated as V_Sep2026 = V_Sep2025 × current-year growth factor, or as a September share of the 2026 annual/YTD level. Prior September values and the latest 2026 published YTD values anchor the baseline.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits September 2025 NPS visitor use statistics; Yellowstone visitation July 2026 record visitors; "Yellowstone" visitation statistics September 2025 news release nps.gov/yell/learn/news recreation visits; Yellowstone 2025 annual visitation total 4.7 million recreation visits year end

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p1 Yellowstone recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p2 Yellowstone recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p3 Yellowstone recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p4 Yellowstone annual recreation visits, 2021 (over 4.8 million) = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded 'over 4.8 million' phrasing of the same NPS 2021 annual total given exactly in p12.] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits"
  - p5 Yellowstone year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p6 Yellowstone year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p7 Yellowstone year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p8 Yellowstone year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p9 Yellowstone year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p10 Yellowstone year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/yellowstone-reports-4-76-million-visitors-in-2025-second-busiest-year-on-record/` -> **snapshot** (snapshot 20260319072433); points raw/verified 15/14
  - p11 Yellowstone National Park annual recreation visits, 2025 = **4,762,988** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "According to a Tuesday announcement by the park, 4,762,988 recreation visits were logged in 2025"
  - p12 Yellowstone National Park annual recreation visits, 2021 (second-busiest referen = **4,860,242** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "since the post-pandemic boom of 2021, which saw 4,860,242 visits"
  - p13 Yellowstone National Park annual recreation visits, 2024 = **4,744,353** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "In 2024, YNP reported 4,744,353 visits"
  - p14 Yellowstone National Park annual recreation visits, 2023 = **4,501,382** recreation visits (2023-01-01..2023-12-31) [keep: ] quote: "preceded by 4,501,382 visits in 2023"
  - p15 Yellowstone National Park cumulative recreation visits since 1904 (through 2025) = **213,257,451** recreation visits (1904-01-01..2025-12-31) [DISCARD: Cumulative visits since 1904; multi-decade total with no bearing on a single future month.] quote: "since then, the park has welcomed a recorded 213,257,451 recreation visits"
  - p16 Yellowstone National Park overnight stays, 2025 = **1,238,983** overnight stays (2025-01-01..2025-12-31) [DISCARD: Duplicate of the 2025 overnight-stay total p123.] quote: "Last year saw 1,238,983 overnight stays in the park, too."
  - p17 Grand Teton National Park annual recreation visits, 2025 = **3,800,648** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "Grand Teton National Park also saw its second-busiest year on record, notching 3,800,648 recreation visits in 2025."
  - p18 Grand Teton National Park annual recreation visits, 2021 = **3,885,230** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "second only to 2021, when GTNP saw 3,885,230 recreation visits"
  - p19 Grand Teton National Park annual recreation visits, 2024 = **3,628,222** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "In 2024, the total was 3,628,222."
  - p20 Grand Teton National Park cumulative recreation visits since 1929 = **178,939,234** recreation visits (1929-01-01..2025-12-31) [DISCARD: Grand Teton cumulative visits since 1929; irrelevant to a Yellowstone monthly forecast.] quote: "Since 1929, the park's total visitation is recorded as 178,939,234."
  - p21 Number of parks setting new visitation records in 2025 (NPS) = **23** parks (2025-01-01..2025-12-31) [DISCARD: Count of parks setting records in 2025; no quantitative role for the target.] quote: "According to NPS, 23 parks set new visitation records in 2025."
  - p22 Great Smoky Mountains National Park annual recreation visits, 2025 (top park) = **11,527,939** recreation visits (2025-01-01..2025-12-31) [DISCARD: Great Smoky Mountains annual total; different park, not a regional signal usable for September.] quote: "- Great Smoky Mountains: 11,527,939"
  - p23 Zion National Park annual recreation visits, 2025 = **4,984,525** recreation visits (2025-01-01..2025-12-31) [DISCARD: Zion annual total; different park and region, no role.] quote: "- Zion: 4,984,525"
  - p24 Duration of 2025 partial government shutdown affecting park operations = **43** days (2025-01-01..2025-12-31) [DISCARD: Duplicate of the 43-day shutdown length p131.] quote: ""Despite a 43-day partial government shutdown - the longest ever"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d2 [shocks] Park operations and calendar-effects analyst

Hypothesis: September 2026 deviates from a historical baseline because of the Labor Day date, school calendars, scheduled road/bridge construction, closures, fire/smoke, and entry/reservation policies known by the cutoff. Quantifying affected entrance-days or capacity can adjust the baseline up or down.

Queries issued by the searcher: Yellowstone 2026 road construction closures September; Yellowstone National Park 2026 fire closures; Yellowstone visitation statistics September 2025 recreation visits 839,579; nps.gov/yell road construction delays 2026 bridge project Yellowstone River Bridge Bridge Bay Firehole

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/management/current-fire-activity.htm` -> **snapshot** (snapshot 20260722025734); points raw/verified 4/3
  - p25 Suspension fire acres reported in Yellowstone 2026 wildfire table = **0.01** acres (2026-06-25..2026-06-25) [keep: ] quote: "\| Suspension \| June 25 \| Lightning \| 0.01 \| Out \|"
  - p26 Bridge fire acres reported in Yellowstone 2026 wildfire table = **0.01** acres (2026-07-12..2026-07-12) [keep: ] quote: "\| Bridge \| July 12 \| Human \| 0.01 \| Out \|"
  - p27 Cowan Creek fire acres reported in Yellowstone 2026 wildfire table = **0.1** acres (2026-07-18..2026-07-18) [keep: ] quote: "\| Cowan Creek \| July 18 \| Lightning \| 0.1 \| Active \|"
- dropped by code checks: 1 (period_end 2026-10-31 after as_of: 1)

### d3 [related_series] Regional park comparability analyst

Hypothesis: Nearby parks such as Grand Teton share regional travel demand, Labor Day timing, and school calendars. A historical Yellowstone/Grand Teton September ratio, combined with Grand Teton 2026 YTD growth or September data if available, can provide an independent forecast; park-specific closures or policies alter the ratio.

Queries issued by the searcher: Grand Teton National Park monthly visitation September 2025 recreation visits; Grand Teton 2026 year to date visitation record; Yellowstone National Park September 2025 recreation visits monthly report approximately; Grand Teton September recreation visits 2024 2023 2022 monthly table NPS

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=614a8d05-b524-4085-9144-b814f8015e23&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/july-numbers-in-grand-teton-push-2026-visitation-over-2-million/` -> **snapshot** (snapshot 20260815071816); points raw/verified 10/10
  - p28 Grand Teton National Park recreation visits, July 2026 = **773,094** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "The park saw 773,094 recreation visits during July, a nearly 2% decrease from July 2025"
  - p29 Grand Teton National Park recreation visits, July 2025 = **787,186** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "a nearly 2% decrease from July 2025, when the park saw 787,186 visits"
  - p30 Grand Teton National Park recreation visits, July 2021 = **835,846** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation was down 7.5% from July 2021 (835,846 recreation visits)"
  - p31 Grand Teton National Park total recreation visits, full year 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of the exact 2021 Grand Teton annual total p18.] quote: "which was the park's record-breaking year with over 3.88 million visits"
  - p32 Grand Teton National Park year-to-date recreation visits, January-July 2026 = **2,074,026** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far this year, GTNP has hosted 2,074,026 recreation visits, up almost 1% over the same time frame in 2025"
  - p33 Grand Teton National Park year-to-date recreation visits, January-July 2025 = **2,055,783** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "up almost 1% over the same time frame in 2025 (2,055,783 visits)"
  - p34 Grand Teton National Park year-to-date recreation visits, January-July 2021 = **2,240,805** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "This year's January through July total is down about 7% from 2021's numbers (2,240,805 visits)"
  - p35 Grand Teton National Park year-to-date recreation visits through July, 2024 = **1,987,288** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "- 2024 - 1,987,288"
  - p36 Grand Teton National Park year-to-date recreation visits through July, 2023 = **1,787,695** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "- 2023 - 1,787,695"
  - p37 Grand Teton National Park year-to-date recreation visits through July, 2022 = **1,547,782** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "- 2022 - 1,547,782"
- `https://data.hereandthere.club/national-park-visitation/grand-teton` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] Entrance traffic-counter and vehicle-occupancy analyst

Hypothesis: Reported recreation visits are derived from or constrained by vehicle entries at Yellowstone's entrances. A physical-flow estimate V_Sep = sum over entrances of vehicle counts × average persons per vehicle, adjusted for buses/non-recreation entries, can validate or replace the historical route if entrance counts are available.

Queries issued by the searcher: Yellowstone National Park September 2025 visitation statistics recreation visits; Yellowstone entrance vehicle counts monthly by entrance NPS Visitor Use Statistics; nps.gov/yell news release "September 2025" visitation statistics recreation visits 839,579; IRMA NPS Stats "Entrance Stations" report Yellowstone vehicles by month recreational automobiles

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **snapshot** (snapshot 20251127005128); points raw/verified 12/5
  - p38 Persons-per-vehicle multiplier, North Gate, September = **2.6** persons per vehicle (2024-09-01..2024-09-30) [keep: ] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p39 Persons-per-vehicle multiplier, West Gate, September = **2.6** persons per vehicle (2024-09-01..2024-09-30) [keep: ] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p40 Persons-per-vehicle multiplier, South Gate, September = **2.7** persons per vehicle (2024-09-01..2024-09-30) [keep: ] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p41 Persons-per-vehicle multiplier, East Gate, September = **2.7** persons per vehicle (2024-09-01..2024-09-30) [keep: ] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p42 Persons-per-vehicle multiplier, Northeast Gate, September = **2.3** persons per vehicle (2024-09-01..2024-09-30) [keep: ] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://outdoor-society.com/a-closer-look-at-yellowstone-national-park-visitation-may-2024/` -> **snapshot** (snapshot 20260313210412); points raw/verified 15/15
  - p43 Yellowstone recreation visits, May 2024 = **522,450** recreation visits (2024-05-01..2024-05-31) [keep: ] quote: "The park hosted 522,450 recreation visits in May 2024, up 15% from May 2023 (454,262 recreation visits)."
  - p44 Yellowstone recreation visits, May 2023 = **454,262** recreation visits (2023-05-01..2023-05-31) [keep: ] quote: "up 15% from May 2023 (454,262 recreation visits)"
  - p45 Yellowstone recreation visits, May 2022 = **523,680** recreation visits (2022-05-01..2022-05-31) [keep: ] quote: "In May of 2022, 523,680 people entered the park."
  - p46 Yellowstone recreation visits, May 2021 = **473,799** recreation visits (2021-05-01..2021-05-31) [keep: ] quote: "This May's visitation showed a 10% increase from May 2021 (473,799 recreation visits)."
  - p47 Yellowstone recreation visits, June 2021 = **928,845** recreation visits (2021-06-01..2021-06-30) [keep: ] quote: "June of 2021 saw 928,845 visitors, nearly double that of May 2021."
  - p48 Yellowstone year-to-date recreation visits, 2024 = **719,127** recreation visits (2024-01-01..2024-05-31) [keep: ] quote: "So far in 2024, the park has hosted 719,127 recreation visits, up 11% from 2023 (644,979), and up 11% from 2021 (649,153 recreation visits)."
  - p49 Yellowstone year-to-date recreation visits, 2023 = **644,979** recreation visits (2023-01-01..2023-05-31) [keep: ] quote: "up 11% from 2023 (644,979)"
  - p50 Yellowstone year-to-date recreation visits, 2021 = **649,153** recreation visits (2021-01-01..2021-05-31) [keep: ] quote: "up 11% from 2021 (649,153 recreation visits)"
  - p51 Cars entering Yellowstone, May 2024 = **198,227** cars (2024-05-01..2024-05-31) [keep: ] quote: "According to the park's visitation website, 198,227 cars entered the park in May 2024."
  - p52 Cars entering Yellowstone, May 2022 = **199,446** cars (2022-05-01..2022-05-31) [keep: ] quote: "In May 2022, 199,446 cars entered the park, while May 2021 saw 184,939 cars."
  - p53 Cars entering Yellowstone, May 2021 = **184,939** cars (2021-05-01..2021-05-31) [keep: ] quote: "In May 2022, 199,446 cars entered the park, while May 2021 saw 184,939 cars."
  - p54 Average persons per car, Yellowstone, May 2024 (excludes tour buses) = **2.64** people per car (2024-05-01..2024-05-31) [keep: ] quote: "2.64 people per car in 2024"
  - p55 Average persons per car, Yellowstone, May 2023 (excludes tour buses) = **2.62** people per car (2023-05-01..2023-05-31) [keep: ] quote: "2.62 people per car in 2023"
  - p56 Tour buses entering Yellowstone, May 2024 = **558** tour buses (2024-05-01..2024-05-31) [keep: ] quote: "In 2024 there were 558 tour buses"
  - p57 Average daily cars entering Yellowstone, May 2024 = **6,426** cars per day (2024-05-01..2024-05-31) [keep: ] quote: "During May 2024, 6,426 cars entered Yellowstone National Park on average each day, totaling roughly 16,853 people every 24 hours."
- `https://yellowstone.co/entrances/southentrance.htm` -> **snapshot** (snapshot 20260518210310); points raw/verified 13/13
  - p58 Yellowstone South Entrance visitors, September 2025 = **147,529** visitors (2025-09-01..2025-09-30) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p59 Yellowstone South Entrance visitors, total 2025 = **794,280** visitors (2025-01-01..2025-12-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p60 Yellowstone South Entrance visitors, August 2025 = **157,131** visitors (2025-08-01..2025-08-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p61 Yellowstone South Entrance visitors, July 2025 = **174,080** visitors (2025-07-01..2025-07-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p62 Yellowstone South Entrance visitors, June 2025 = **166,981** visitors (2025-06-01..2025-06-30) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p63 Yellowstone South Entrance visitors, May 2025 = **81,649** visitors (2025-05-01..2025-05-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p64 Yellowstone South Entrance visitors, October 2025 = **57,086** visitors (2025-10-01..2025-10-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p65 Yellowstone South Entrance visitors, November 2025 = **0** visitors (2025-11-01..2025-11-30) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p66 Yellowstone South Entrance visitors, December 2025 = **2,479** visitors (2025-12-01..2025-12-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p67 Yellowstone South Entrance visitors, January 2025 = **3,049** visitors (2025-01-01..2025-01-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p68 Yellowstone South Entrance visitors, February 2025 = **2,948** visitors (2025-02-01..2025-02-28) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p69 Yellowstone South Entrance visitors, March 2025 = **1,345** visitors (2025-03-01..2025-03-31) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
  - p70 Yellowstone South Entrance visitors, April 2025 = **3** visitors (2025-04-01..2025-04-30) [keep: ] quote: "\| 3,049 \| 2,948 \| 1,345 \| 3 \| 81,649 \| 166,981 \| 174,080 \| 157,131 \| 147,529 \| 57,086 \| 0 \| 2,479 \| 794,280 \|"
- dropped by code checks: 7 (period_end missing or unparseable: 7)

### d5 [administrative] NPS public-affairs and statistics-release analyst

Hypothesis: The official NPS release schedule and definitions determine what will be counted and when; the latest pre-cutoff NPS release and any revision notes indicate the current 2026 level and reporting lag. This route mostly validates the definition and supplies the most recent official YTD benchmark for other routes.

Queries issued by the searcher: NPS Visitor Use Statistics Yellowstone monthly report 2026 recreation visits; Yellowstone National Park news release visitation 2026; NPS "recreation visits" definition visitor use statistics "how we calculate" irma.nps.gov Stats frequently asked questions; "Yellowstone visitation statistics for July 2026" nps.gov news release 958,706

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://oilcity.news/community/wyoming-community-2/2026/08/11/yellowstone-reports-958k-visitors-in-july-visits-down-2-from-2025/` -> **snapshot** (snapshot 20260823050010); points raw/verified 12/12
  - p71 Yellowstone recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [DISCARD: Exact duplicate of p1 (same NPS July 2026 figure) from a second outlet; adds no independent information.] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025, when 975,109 people visited the park."
  - p72 Yellowstone recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [DISCARD: Exact duplicate of p2.] quote: "down 2% from July 2025, when 975,109 people visited the park."
  - p73 Percent change in Yellowstone recreation visits, July 2026 vs July 2025 = **2** % (2026-07-01..2026-07-31) [DISCARD: Percentage change derived from the same July levels (p1, p2); no new measurement.] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025, when 975,109 people visited the park."
  - p74 Percent change in Yellowstone recreation visits, July 2026 vs July 2021 = **11** % (2026-07-01..2026-07-31) [DISCARD: Percentage change derived from p1 and p3; no new measurement.] quote: "Visitation in July 2026 showed an 11% decrease from July 2021, when the park hosted 1,080,767 visits"
  - p75 Yellowstone recreation visits, July 2021 = **1,080,767** recreation visits (2021-07-01..2021-07-31) [DISCARD: Exact duplicate of p3.] quote: "an 11% decrease from July 2021, when the park hosted 1,080,767 visits"
  - p76 Yellowstone record annual recreation visits (2021), over 4.8 million = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Same rounded 2021 annual figure as p4/p12; redundant.] quote: "both part of Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p77 Yellowstone year-to-date recreation visits, 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [DISCARD: Exact duplicate of p5.] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025's 2,666,031 recreation visits"
  - p78 Yellowstone year-to-date recreation visits, 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [DISCARD: Exact duplicate of p6.] quote: "down 1% from 2025's 2,666,031 recreation visits and down 1% from 2021's 2,668,765 recreation visits."
  - p79 Yellowstone year-to-date recreation visits, 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Exact duplicate of p7.] quote: "down 1% from 2021's 2,668,765 recreation visits."
  - p80 Yellowstone year-to-date recreation visits, 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [DISCARD: Exact duplicate of p8.] quote: "- 2024 - 2,626,091"
  - p81 Yellowstone year-to-date recreation visits, 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [DISCARD: Exact duplicate of p9.] quote: "- 2023 - 2,462,535"
  - p82 Yellowstone year-to-date recreation visits, 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Exact duplicate of p10.] quote: "- 2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://home.nps.gov/subjects/socialscience/statistics-faq.htm` -> **snapshot** (snapshot 20260123080907); points raw/verified 11/5
  - p83 Annual recreation visits by reporting park available from year = **1,904** year (1904-01-01..1904-12-31) [DISCARD: Start year of annual NPS reporting; administrative metadata with no numerical role (monthly availability is covered by p] quote: "Annual recreation visits by reporting park are available from 1904 to present."
  - p84 Monthly visitation data available for reporting parks from year = **1,979** year (1979-01-01..1979-12-31) [keep: ] quote: "are available for reporting parks from 1979 to present."
  - p85 Traffic counts available from year = **1,985** year (1985-01-01..1985-12-31) [keep: ] quote: "Some traffic counts are available from 1985 to present."
  - p86 Socioeconomic Monitoring Program launch year = **2,022** year (2022-01-01..2022-12-31) [DISCARD: Launch year of the Socioeconomic Monitoring Program; no role in estimating September visits.] quote: "However in 2022 the Socioeconomic Monitoring Program was launched to survey visitors at a sample of 24 parks a year"
  - p87 Federal Executive Policy year establishing visitor use statistics mandate = **1,965** year (1965-01-01..1965-12-31) [DISCARD: 1965 policy mandate year; no numerical role.] quote: "This responsibility is recognized by legal mandate, various interagency agreements and a 1965 Federal Executive Policy."
- `https://www.nps.gov/subjects/socialscience/nps-visitor-use-statistics-definitions.htm?lv=true` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end missing or unparseable: 6)

### d6 [capacity_consumption] Concessioner and campground occupancy analyst

Hypothesis: Overnight capacity utilization provides a lower-bound component: total visits = overnight visits / historical overnight share. September lodging room-nights and campground site-nights, converted to overnight visitors, constrain plausible September totals and can be compared with the historical route.

Queries issued by the searcher: Yellowstone National Park visitation statistics September overnight stays lodging campground; Xanterra Yellowstone lodging occupancy September room nights; Yellowstone September 2025 visitation 839,579 recreation visits; nps.gov Yellowstone total overnight stays September concession lodging campers visitor use statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://powelltribune.com/stories/region-continues-to-buck-downward-trend-of-tourism,170327` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://industry.visitjacksonhole.com/wp-content/uploads/2023/06/Situational-Analysis-Report.pdf` -> **snapshot** (snapshot 20241126152755); points raw/verified 15/10
  - p88 Yellowstone NP reported reduction in overnight stays in 2021 due to reduced camp = **20** % (2021-01-01..2021-12-31) [DISCARD: 2021 COVID-era overnight-capacity anomaly; a one-off supply restriction not transferable to September 2026.] quote: "one National Park reported that visitation levels in 2021 were comparable to 2019, with increased re-entry and about 20% fewer overnight stays due to reduced availability of campsites and hotel rooms."
  - p89 Yellowstone NP overcounted entries due to multiple re-entries amid 20% drop in a = **900,000** people (2021-01-01..2021-12-31) [DISCARD: Unadopted claim that ~900,000 entries were overcounted; not an official NPS figure and would corrupt any level built on ] quote: "the National Park Service announced that they had overcounted about 900,000 people who entered the park multiple times due to a 20% drop in available in-park accommodation."
  - p90 Yellowstone NP revised 2021 visitation (approx.) = **4,000,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Speculative 'revised ~4.0 million' for 2021 that contradicts the official NPS series (p12); misleading as a level.] quote: "The revised numbers for Yellowstone would be around 4.0 million, which is just under the peak numbers of 2016."
  - p91 Yellowstone NP initially reported 2021 visits = **4,900,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Approximate initial 2021 total (4.9M) superseded by the exact official value (p12); redundant and imprecise.] quote: "Yellowstone initially reported an increase in visits from 4.0 million in 2019 to 4.9 million in 2021."
  - p92 Yellowstone NP visits in 2019 = **4,000,000** recreation visits (2019-01-01..2019-12-31) [DISCARD: Rounded 2019 park total from the same non-official article; not needed and not part of any route.] quote: "Yellowstone initially reported an increase in visits from 4.0 million in 2019 to 4.9 million in 2021."
  - p93 Yellowstone NP visits January–July 2021 = **3,500,000** visits (2021-01-01..2021-07-31) [DISCARD: January-July 2021 '3.5 million' conflicts materially with the official NPS YTD value (p7 = 2,668,765).] quote: "YNP registered 3.5 million visits between January and July of 2021 and 2.5 million visits during that same period in 2022."
  - p94 Yellowstone NP visits January–July 2022 = **2,500,000** visits (2022-01-01..2022-07-31) [DISCARD: January-July 2022 '2.5 million' conflicts with official NPS YTD (p10 = 1,855,396).] quote: "YNP registered 3.5 million visits between January and July of 2021 and 2.5 million visits during that same period in 2022."
  - p95 Yellowstone NP recreational visits drop first seven months 2022 vs same period 2 = **30** % (2022-01-01..2022-07-31) [DISCARD: Percent drop for 2022 derived from the erroneous p93/p94 levels.] quote: "During the first seven months of 2022, recreational visits dropped by 30% compared to the same period in 2021 and 19% compared to 2019."
  - p96 Yellowstone NP recreational visits drop first seven months 2022 vs same period 2 = **19** % (2022-01-01..2022-07-31) [DISCARD: Percent drop versus 2019 derived from the same erroneous base levels.] quote: "During the first seven months of 2022, recreational visits dropped by 30% compared to the same period in 2021 and 19% compared to 2019."
  - p97 Yellowstone NP visitation index (2015=100) in 2021 = **118** index (2015=100) (2021-01-01..2021-12-31) [DISCARD: Visitation index (2015=100) built on the non-official 2021 level; unit and base are not usable for a monthly forecast.] quote: "For Yellowstone NP, the index was 98 in 2019; this fell to 93 in 2020 before rising to118 in 2021."
- `https://www.travelandtourworld.com/news/article/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-occupancy-amid-` -> **snapshot** (snapshot 20250924004157); points raw/verified 9/3
  - p98 Projected decline in U.S. tourism this year (forecast) = **8** % (2025-01-01..2025-12-31) [DISCARD: Forecast of national tourism decline for 2025: wrong year, wrong scope, and a forecast rather than an outcome.] quote: "According to industry forecasts, U.S. tourism is projected to decline by around 8% this year."
  - p99 Park County lodging tax receipts, August, year-over-year increase = **1.2** % (2025-08-01..2025-08-31) [DISCARD: Park County lodging tax for August 2025 only; no 2026 counterpart, so it cannot form a signal series for September 2026.] quote: "Lodging tax receipts for August increased by 1.2% compared with the same period last year"
  - p100 Park County lodging tax collections, year-to-date increase = **2.5** % (2025-01-01..2025-08-31) [DISCARD: Park County YTD lodging tax for 2025 only; no 2026 counterpart and an indirect proxy that cannot be aligned to the targe] quote: "while year-to-date collections show a 2.5% increase overall"
- dropped by code checks: 11 (period_end missing or unparseable: 9; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b1 [own_history] NPS official monthly series (irma.nps.gov / Visitor Use Statistics monthly tables, available from 1979 per p84)

Hypothesis: Retrieving Yellowstone park-total recreation visits for September 2019-2025 (and August 2021-2025) would replace the seasonal-share assumptions a1/a2, which carry nearly all the uncertainty in every current route, and would enable series_naive and yoy_scaling as genuine backtested methods instead of assumption-driven formulas.

Queries issued by the searcher: irma.nps.gov STATS monthly visitation Yellowstone National Park September recreation visits; Yellowstone hosted recreation visits in September 2025 press release; "Yellowstone" "recreation visits in September" 2024 2023 press release visitation statistics nps.gov/yell; Yellowstone August 2026 visitation statistics recreation visits press release

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.publicnow.com/view/472F1877364B37693E164F398C1367B3C0AA9310` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-national-park-september-visits-up-2-from-last-year` -> **snapshot** (snapshot 20241010002924); points raw/verified 13/13
  - p101 Yellowstone National Park recreation visits, September 2024 = **852,435** recreation visits (2024-09-01..2024-09-30) [keep: ] quote: "Yellowstone National Park hosted 852,435 recreation visits in September 2024."
  - p102 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: ] quote: "This is a 2% increase from September 2023 (838,458 recreational visits)."
  - p103 Yellowstone National Park recreation visits, September 2021 = **882,078** recreation visits (2021-09-01..2021-09-30) [keep: ] quote: "This September's visitation showed an 3% decrease from September 2021 (882,078 recreation visits)."
  - p104 Yellowstone National Park year-to-date recreation visits through September 2024 = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, the park has hosted 4,349,689 recreation visits"
  - p105 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,147,382** recreation visits (2023-01-01..2023-09-30) [keep: ] quote: "2023 - 4,147,382"
  - p106 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [keep: ] quote: "2022 - 3,005,194"
  - p107 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: ] quote: "2021 - 4,472,687"
  - p108 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [keep: ] quote: "2020 - 3,393,642"
  - p109 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [keep: ] quote: "2019 - 3,807,815"
  - p110 Yellowstone National Park September 2024 recreation visits, year-over-year perce = **2** % (2024-09-01..2024-09-30) [DISCARD: Derived percentage restatement of p101/p102; no independent measurement.] quote: "This is a 2% increase from September 2023 (838,458 recreational visits)."
  - p111 Yellowstone National Park September 2024 recreation visits, percent decrease vs  = **3** % (2024-09-01..2024-09-30) [DISCARD: Derived percentage restatement of p103; no independent measurement.] quote: "This September's visitation showed an 3% decrease from September 2021 (882,078 recreation visits)."
  - p112 Yellowstone National Park year-to-date 2024 recreation visits, percent increase  = **5** % (2024-01-01..2024-09-30) [DISCARD: Derived percentage restatement of p104/p105; no independent measurement.] quote: "the park has hosted 4,349,689 recreation visits, up 5% from 2023 (4,147,382 recreation visits)"
  - p113 Yellowstone National Park year-to-date 2024 recreation visits, percent decrease  = **3** % (2024-01-01..2024-09-30) [DISCARD: Derived percentage restatement of p104/p107; no independent measurement.] quote: "and down 3% from 2021 (4,472,687 recreation visits)"
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [physical_flow] Gate-level entrance counts (North, West, South, East, Northeast) for September

Hypothesis: September gate counts for 2025 (and partial 2026) would replace assumption a3 — the departure of the September park/South-Entrance ratio from its annual value — with an observed ratio, and combined with the persons-per-vehicle factors (p38-p42) would give an independent physical-flow check on the ~0.5-1.0 million visit level.

Queries issued by the searcher: Yellowstone National Park visitation statistics by entrance September 2025 vehicle counts; nps.gov/yell vehicle counts by entrance station monthly table; Yellowstone September 2025 recreation visits monthly report; "Yellowstone" "September 2025" visitation entrance West South North Cody

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **snapshot** (snapshot 20251127005128); points raw/verified 12/5
  - p114 September persons-per-vehicle multiplier, North Gate = **2.6** persons per vehicle (2024-09-01..2024-09-30) [DISCARD: Exact duplicate of p38; adds no independent information.] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p115 September persons-per-vehicle multiplier, West Gate = **2.6** persons per vehicle (2024-09-01..2024-09-30) [DISCARD: Exact duplicate of p39; adds no independent information.] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p116 September persons-per-vehicle multiplier, South Gate = **2.7** persons per vehicle (2024-09-01..2024-09-30) [DISCARD: Exact duplicate of p40; adds no independent information.] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p117 September persons-per-vehicle multiplier, East Gate = **2.7** persons per vehicle (2024-09-01..2024-09-30) [DISCARD: Exact duplicate of p41; adds no independent information.] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
  - p118 September persons-per-vehicle multiplier, Northeast Gate = **2.3** persons per vehicle (2024-09-01..2024-09-30) [DISCARD: Exact duplicate of p42; adds no independent information.] quote: "SEPTEMBER 2.6 2.6 2.7 2.7 2.3"
- `https://powelltribune.com/stories/yellowstone-2025-attendance-is-second-highest,173812` -> **snapshot** (snapshot 20260321074542); points raw/verified 15/13
  - p119 Yellowstone National Park total recreation visits, full year 2025 = **4,762,988** recreation visits (2025-01-01..2025-12-31) [DISCARD: Duplicate of the 2025 annual Yellowstone total p11.] quote: "Yellowstone National Park welcomed 4,762,988 recreation visits in 2025."
  - p120 Yellowstone National Park record annual recreation visits, 2021 = **4,860,242** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of the 2021 annual Yellowstone total p12.] quote: "The number is just shy of the 2021 record of 4,860,242"
  - p121 Yellowstone National Park total recreation visits, full year 2024 = **4,744,363** recreation visits (2024-01-01..2024-12-31) [DISCARD: Near-duplicate/rounded vintage of the 2024 annual Yellowstone total p13.] quote: "about 20,000 visits higher than last year's total of 4,744,363"
  - p122 Yellowstone visitors' total hours spent in park, 2025 = **86,891,452** hours (2025-01-01..2025-12-31) [keep: ] quote: "visitors spent 86,891,452 hours in the park"
  - p123 Yellowstone overnight stays, 2025 = **1,238,983** overnight stays (2025-01-01..2025-12-31) [keep: ] quote: "along with 1,238,983 overnight stays"
  - p124 Share of Yellowstone 2025 visits occurring May through August = **75** % (2025-01-01..2025-12-31) [keep: ] quote: "More than 75% of all visits in 2025 happened between May and August."
  - p125 Yellowstone East Entrance visits, 2025 = **167,500** visits (2025-01-01..2025-12-31) [DISCARD: Entrance-level annual count that does not reconcile with park-total recreation visits and appears to be a different oper] quote: "Just under 167,500 came through the entrance last year."
  - p126 Yellowstone East Entrance year-over-year visitation change, 2025 vs 2024 = **0.3** as written ".3%", value check pending % (2025-01-01..2025-12-31) [DISCARD: Entrance-level annual count with ambiguous scope; not usable as a recreation-visit component without a validated vehicle] quote: "Visitation last year at the East Entrance, near Cody, was up .3% over 2024."
  - p127 Yellowstone West Entrance visits, 2025 = **778,075** visits (2025-01-01..2025-12-31) [DISCARD: Entrance-level annual count that does not reconcile with park-total recreation visits; likely not a recreation-visit tot] quote: "The West Entrance had the most visits, with 778,075."
  - p128 Yellowstone North Entrance visits, 2025 = **561,290** visits (2025-01-01..2025-12-31) [DISCARD: Entrance-level annual count with ambiguous scope; cannot be combined directly with park-total recreation visits.] quote: "The North Entrance was the second busiest with 561,290"
  - p129 Yellowstone South Entrance visits, 2025 = **291,693** visits (2025-01-01..2025-12-31) [DISCARD: Conflicts with the South Entrance visitor total p59 and is likely a vehicle or other non-visitor count.] quote: "the South Entrance was third with 291,693"
  - p130 Yellowstone Northeast Entrance visits, 2025 = **136,768** visits (2025-01-01..2025-12-31) [DISCARD: Entrance-level annual count with ambiguous scope; not usable as a recreation-visit component.] quote: "The Northeast Entrance had the lowest attendance with 136,768."
  - p131 Length of 2025 partial government shutdown affecting park operations = **43** days (2025-01-01..2025-12-31) [keep: ] quote: "Despite a 43-day partial government shutdown - the longest ever"
- `http://www.degruyterbrill.com/document/doi/10.1525/9780520976924-039/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (period_end missing or unparseable: 9)

### b3 [shocks] Scheduled 2026 construction, closures, entry policies and Labor Day timing

Hypothesis: September 2026-specific road/bridge projects, any reservation or timed-entry policy extension past summer, and the Labor Day date (September 7, 2026, a late date that pushes the holiday weekend fully into September) determine whether the baseline should be shifted materially; without a known schedule the forecast cannot reflect a capacity loss at a specific gate.

Queries issued by the searcher: Yellowstone 2026 road construction closures fall schedule; Yellowstone 2026 timed entry reservation pilot end date; Yellowstone National Park September 2025 visitation statistics recreation visits monthly; Yellowstone visitation Labor Day weekend 2025 press release record

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://wakeupwyo.com/ixp/102/p/yellowstone-road-closures-winter-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grizzlyrv.com/does-yellowstone-have-timed-entry/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone september visits', 'yellowstone visitation', 'nps monthly visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p71', 'p72', 'p75'] July park-total levels (2026, 2025, 2021) come from one NPS monthly release; the oilcity versions (p71, p72, p75) restate the identical numbers, so they are duplicate vintages of the same measurement,
- corroborating: ['p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82'] One NPS year-to-date table (through July, 2021-2026) restated by a second outlet; 2026 is ~1% below 2025, 2025 ~1% below 2021. p77-p82 are exact duplicates of p5-p10.
- corroborating: ['p11', 'p13', 'p14', 'p12'] Annual park totals 2023-2025 and 2021 from one outlet summarizing NPS annual figures; magnitudes are consistent with the YTD path (p5, p6, p7) and with p11 being the second-busiest year after p12.
- corroborating: ['p4', 'p12', 'p76'] p4 and p76 are rounded press phrasing ('over 4.8 million') of the same NPS 2021 figure given exactly in p12 (4,860,242); they are lower-precision duplicates, not separate observations.
- conflicting: ['p90', 'p91', 'p92', 'p12', 'p7'] An advocacy/industry article asserts an initial ~4.9M for 2021 'revised' to ~4.0M, versus the official NPS series (4,860,242 annual, 2,668,765 through July). No such official revision exists in the ke
- conflicting: ['p93', 'p94', 'p7', 'p10'] The same article's January-July levels (~3.5M for 2021, ~2.5M for 2022) are grossly inconsistent with the official NPS YTD values (p7 = 2,668,765; p10 = 1,855,396), and the derived p95/p96 percentage 
- corroborating: ['p28', 'p29', 'p30', 'p32', 'p33'] Grand Teton July 2026 down ~2% year over year while YTD is up ~1% — the same 'roughly flat, slightly soft mid-summer' pattern as Yellowstone (p1 vs p2; p5 vs p6). Supports treating the 2026 regional d
- scope_difference: ['p58', 'p59', 'p60', 'p61', 'p62', 'p11'] South Entrance counts (p58-p70) are a gate-level component inside park totals (p11), not a rival measure. Their seasonality is flatter than the park's: September (p58) retains most of July's (p61) tra
- corroborating: ['p38', 'p39', 'p40', 'p41', 'p42', 'p54', 'p55'] September 2024 gate-level persons-per-vehicle (2.3-2.7) agrees with May 2023-2024 persons-per-car (2.62-2.64), giving a stable ~2.6 conversion for any physical-flow route; no September 2026 vehicle co
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p43', 'p45', 'p46'] May car counts times ~2.6 persons per car reproduce May visit totals of the right magnitude, indicating the visit metric is entry-based and re-entry-sensitive; it warns that any gate-based estimate mu
- corroborating: ['p25', 'p26', 'p27'] All 2026 fires listed are 0.01-0.1 acre and mostly out by late July; as of the cutoff there is no evidence of a smoke/closure shock to carry into September, so no fire adjustment is applied.
- corroborating: ['p16', 'p11'] 2025 overnight stays (1,238,983) are a plausible ~quarter of annual visits; useful only as a sanity check on magnitude, since no September overnight split is available.
- context: ['p11', 'p24'] The 43-day autumn 2025 shutdown (p24) can only have depressed late-2025 months, so September's share of the 2025 annual total is slightly inflated relative to a normal year; a September-share-of-annua
- conflicting: ['p98', 'p99', 'p100'] A national tourism forecast of -8% for 2025 and Park County lodging tax up 2.5% YTD 2025 point in different directions and, more importantly, cover 2025 and different scopes (national tourism, county 
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'] Same-park, same-measure Yellowstone recreation-visit levels. p1/p2 and p5/p6 show 2026 slightly below 2025; p7/p8 are close to 2026; p9 is lower and p10 is flood-affected. These support a soft current
- corroborating: ['p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109'] Yellowstone September park-total history and September year-to-date levels. p101-p103 provide the only direct September park totals for 2024, 2023, and 2021; p104-p109 provide September YTD context bu
- corroborating: ['p11', 'p12', 'p13', 'p14', 'p119', 'p120', 'p121'] Annual Yellowstone recreation-visit totals. p119 duplicates p11, p120 duplicates p12, and p121 is a near-duplicate/rounded vintage of p13. They corroborate the annual levels but should not be treated 
- corroborating: ['p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70'] South Entrance 2025 monthly visitor series. p58 is the September 2025 gate-level count and p59 is the annual South Entrance total from the same series. The zero in p65 is a seasonal road-closure month
- conflicting: ['p125', 'p126', 'p127', 'p128', 'p129', 'p130'] These entrance-level annual figures do not reconcile with park-total recreation visits (their sum is far below p11) and p129 conflicts with the South Entrance visitor total p59. They appear to be a di
- corroborating: ['p38', 'p39', 'p40', 'p41', 'p42', 'p114', 'p115', 'p116', 'p117', 'p118'] September persons-per-vehicle multipliers by gate. p114-p118 are exact duplicates of p38-p42. They are useful conversion factors, but full September vehicle counts for all gates are not present, so th
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p17', 'p18', 'p19'] Grand Teton monthly, YTD, and annual recreation-visit levels. They provide a regional-demand signal for Yellowstone. p31 is a rounded duplicate of the exact 2021 annual value p18.
- corroborating: ['p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57'] May Yellowstone visits, car counts, persons-per-car, and tour-bus counts. They validate the physical-flow conversion logic but cover May, not September, so they are contextual conversion evidence rath
- corroborating: ['p16', 'p123', 'p24', 'p131'] p16 and p123 report the same 2025 overnight-stay total; p24 and p131 report the same 43-day shutdown length. Each pair is duplicate reporting of one underlying quantity.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Departure factor of the 2026 September-to-July recreation-visit ratio from the observed 2021 September-to-July ratio | 1.08 | 0.97..1.2 | 0.7629..1.526 (widened) | ratio | m1 (m1) | The 2021 pair p103 and p3 fixes one observed same-year September/July ratio (roughly four-fifths). September levels have since held up much better than July: p101 (September 2024) is only a little below p103 (September 2021), while p1 (July 2026) is about a tenth below p3 (July 2021). Because July 2 | September 2026 has a shoulder-season shape broadly like recent Yellowstone years, with no major September road closure, reservation change, or heavy smoke episode. | A published September 2026 total implying a September/July ratio at or below the 2021 ratio, or evidence of a major September closure or smoke event cutting park access. |
| a2 | Departure factor of the 2026 September share of annual recreation visits from the mean observed September share in 2021, 2023 and 2024 | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m2 (m2) | The three observed September totals divided by their own-year annual totals (p101/p13, p102/p14, p103/p12) cluster tightly near one-fifth, with no trend, so the historical mean is a good center for 2026. Two offsetting effects are allowed for in the range: the 2025 annual base p11 is depressed by th | 2026 September behaves like a normal shoulder month and the 2025 annual total is a usable base after applying the January-July 2026/2025 growth ratio. | A 2026 September share of annual visits far outside the historical cluster, for example from a late-September closure or a large shift in the shoulder-season travel calendar. |
| a3 | Departure factor of the September park-total-to-South-Entrance ratio from the 2025 annual park-total-to-South-Entrance ratio | 0.97 | 0.88..1.07 | 0.6861..1.372 (widened) | ratio | m3 (m3) | South Entrance's September share of its own annual people count (p58 against p59) is slightly larger than the park's typical September share of its annual total, because the South Entrance carries Grand Teton/Jackson day traffic that is relatively more concentrated in the warm months. The September  | September 2026 South Entrance traffic keeps a seasonal profile close to 2025 and the South Entrance people count is proportional to park recreation visits apart from a small seasonal tilt. | A 2026 South Entrance road closure or diversion (for example construction on the South approach), or evidence that the South Entrance September share is much flatter or much more peaked than assumed. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 846,346 | ['p1', 'p103', 'p3'] / ['a1'] | [] |  | 0.20 | median_of_backtested |  |
| m2 | formula_mc | 863,356 | ['p11', 'p5', 'p6', 'p101', 'p13', 'p102', 'p14', 'p103', 'p12'] / ['a2'] | [] |  | 0.20 | median_of_backtested |  |
| m3 | formula_mc | 851,210 | ['p58', 'p11', 'p59', 'p5', 'p6'] / ['a3'] | [] |  | 0.20 | median_of_backtested |  |
| m4 | ratio | 892,940 |  | [2023, 2024] | 0.090 | 0.06 | backtest |  |
| m5 | series_naive | 845,446 |  | [2024] | 0.009 | 0.34 | backtest |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target
- m5 coverage: the whole target

Result: central **853,317** visit, 80% interval [800,034, 910,149] visit, basis historical_errors (interval width set from the methods' backtest errors on earlier years of the target), weight rule inverse_backtest_error, weight on methods that use assumptions 0.60

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The estimate is 853,317 visit (80% model-based interval 800,034 to 910,149 visit) for Yellowstone National Park recreation visits during September 2026, as NPS monthly Visitor Use Statistics should report them—counted entries, not unique visitors, and not a year-to-date figure. The combination draws on 5 routes. The largest weight goes to a transparent baseline averaging the two most recent observed Septembers, 852,435 recreation visits and 838,458 recreation visits, which anchors the recent level. Other routes scale July 2026 (958,706 recreation visits) by the observed 2021 September/July ratio (882,078 recreation visits over 1,080,767 recreation visits), partition the 2025 annual total (4,762,988 recreation visits) using year-to-date growth (2,635,384 recreation visits versus 2,666,031 recreation visits) and historical September shares, and bridge from South Entrance counts (147,529 visitors, 794,280 visitors). A Grand Teton ratio check (2,074,026 recreation visits) carries little weight. Assumptions 1.08, 1 and 0.97 are analyst departures, not observations. The main risk is a September-specific closure, smoke episode, or a ratio pinned by a single year. The most useful missing evidence is an observed September 2025 park total.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Departure factor of the 2026 September-to-July recreation-visit ratio from the observed 2021 September-to-July ratio: 1.08 ratio, range 0.7629 to 1.526 (range widened by code); used by m1. Overturned by: A published September 2026 total implying a September/July ratio at or below the 2021 ratio, or evidence of a major September closure or smoke event cutting park access.
- a2 Departure factor of the 2026 September share of annual recreation visits from the mean observed September share in 2021, 2023 and 2024: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m2. Overturned by: A 2026 September share of annual visits far outside the historical cluster, for example from a late-September closure or a large shift in the shoulder-season travel calendar.
- a3 Departure factor of the September park-total-to-South-Entrance ratio from the 2025 annual park-total-to-South-Entrance ratio: 0.97 ratio, range 0.6861 to 1.372 (range widened by code); used by m3. Overturned by: A 2026 South Entrance road closure or diversion (for example construction on the South approach), or evidence that the South Entrance September share is much flatter or much more peaked than assumed.

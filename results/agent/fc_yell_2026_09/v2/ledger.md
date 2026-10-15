# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics / Monthly Public Use Reports). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple  | unit recreation visits (count) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS official monthly visitation reports

Hypothesis: September recreation visits in recent years (2019–2025) provide a seasonal baseline. The 2026 September value is likely to be similar to the same month in recent years, adjusted for any trend or unusual events. The ratio of September visits to the preceding January–August total can be used to project September 2026 from the known 2026 year-to-date total.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September 2025 NPS; NPS visitor use statistics Yellowstone monthly recreation visits 2024; Yellowstone National Park visitation August 2026 recreation visits year-to-date; Yellowstone September 2023 recreation visits 838,458 September 2022 NPS press release

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bozemandailychronicle.com/news/yellowstone-national-park-glacier-national-park-see-boost-in-visitor-numbers/article_d449a6e0-9001-11ef-9e0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [physical_flow] Entrance station counts and vehicle traffic

Hypothesis: Recreation visits are derived from entrance station counts and vehicle occupancy factors. If entrance station data or traffic counts for Yellowstone in September 2026 are available (e.g., from park reports or traffic monitoring), they can be converted to visits using historical vehicle occupancy rates.

Queries issued by the searcher: Yellowstone entrance station counts September 2025 visitation; Yellowstone vehicle occupancy rate persons per vehicle visitation study; Yellowstone National Park September 2025 visitation monthly report NPS; NPS visitor use statistics monthly public use report Yellowstone 2025 2026

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.travelandtourworld.pl/aktualno%C5%9Bci/artyku%C5%82/63ykvnvt60ul/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [shocks] Park closures, weather, and access restrictions

Hypothesis: Any closures, road construction, wildfire smoke, or policy changes in September 2026 could significantly alter visitation. Conversely, if no major disruptions are known, visitation may follow normal patterns. The 2022 flood drastically reduced June visitation that year, showing sensitivity to shocks.

Queries issued by the searcher: Yellowstone National Park closures September 2026; Yellowstone road construction 2026 access restrictions; Yellowstone visitation September 2025 recreation visits NPS; Yellowstone temporary closure September 2026 fire smoke

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/3
  - p1 Projected 2026 opening date of West Entrance to Madison, Madison to Old Faithful = **17** date (2026-04-17..2026-04-17) [keep: ] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris, Mammoth Hot Springs to Norris, Norris to Canyon Village"
  - p2 Projected 2026 opening date of East Entrance to Fishing Bridge (Sylvan Pass), Ca = **1** date (2026-05-01..2026-05-01) [keep: ] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p3 Projected 2026 opening date of South Entrance to West Thumb, West Thumb to Old F = **8** date (2026-05-08..2026-05-08) [keep: ] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass), West Thumb to Lake Village, Tower-Roosevelt to Tower Fall"
- `https://www.nps.gov/yell/planyourvisit/situationreport.htm` -> **snapshot** (snapshot 20260618033531); points raw/verified 0/0
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (number: no number in value_as_written: 5; period_end 2026-10-31 after as_of: 4; period_end 2026-10-12 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-09-30 after as_of: 1)

### d4 [base_rates] Seasonal share of annual visitation

Hypothesis: September typically accounts for a stable share of Yellowstone's annual recreation visits (e.g., around 10–12% in recent years). If a forecast for total 2026 visitation exists, or if the year-to-date total is known, the September share can be applied to estimate the target.

Queries issued by the searcher: Yellowstone annual visitation 2025 total recreation visits; Yellowstone September visitation share annual recreation visits NPS; Yellowstone National Park reports August 2026 visitation statistics; Yellowstone 2026 visitation forecast annual total projection

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p4 Yellowstone National Park average September recreation visits, 2014-2018 average = **663,651** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p5 September share of average annual recreation visits at Yellowstone, 2014-2018 av = **16.51** % (2014-01-01..2018-12-31) [DISCARD: Duplicate of p18 (same 16.51% September share from the same table); keep one copy.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p6 Yellowstone National Park average January recreation visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p7 Yellowstone National Park average February recreation visits, 2014-2018 average = **33,088** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p8 Yellowstone National Park average March recreation visits, 2014-2018 average = **22,266** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p9 Yellowstone National Park average April recreation visits, 2014-2018 average = **44,027** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p10 Yellowstone National Park average May recreation visits, 2014-2018 average = **401,449** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p11 Yellowstone National Park average June recreation visits, 2014-2018 average = **780,652** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p12 Yellowstone National Park average July recreation visits, 2014-2018 average = **947,688** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p13 Yellowstone National Park average August recreation visits, 2014-2018 average = **839,787** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p14 Yellowstone National Park average October recreation visits, 2014-2018 average = **223,777** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p15 Yellowstone National Park average November recreation visits, 2014-2018 average = **14,323** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p16 Yellowstone National Park average December recreation visits, 2014-2018 average = **20,434** visits (2014-01-01..2018-12-31) [keep: ] quote: "\| December \| 20,434 \| 0.51% \|"
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] NPS-wide or regional visitation trends

Hypothesis: Yellowstone's visitation may move with broader National Park System or Rocky Mountain region visitation. If NPS-wide or regional September visitation trends are available for 2026, they can indicate whether Yellowstone is likely above or below its historical seasonal pattern.

Queries issued by the searcher: NPS national visitation statistics 2026 monthly recreation visits; Yellowstone National Park visitation September 2025 statistics; Yellowstone visitation 2026 year to date August recreation visits; National Park Service system-wide visitation 2026 record January July; Grand Teton Glacier Zion visitation September 2025 statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/Reports/National` -> **snapshot** (snapshot 20260821013908); points raw/verified 0/0
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [capacity_consumption] Lodging, campground, and tour bookings

Hypothesis: Overnight stays and tours are a component of recreation visits. Occupancy rates and bookings for Yellowstone lodging and campgrounds in September 2026 can indicate whether visitation is likely high or low relative to historical norms. However, day-use visits dominate, so this is a partial signal.

Queries issued by the searcher: Yellowstone lodging occupancy September 2025 Xanterra bookings; Yellowstone National Park monthly visitation statistics September 2025; Xanterra Yellowstone 2026 reservations bookings; Yellowstone campground occupancy statistics 2025 overnight stays

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://powelltribune.com/stories/region-continues-to-buck-downward-trend-of-tourism,170327` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cz/zpr%C3%A1vy/%C4%8Dl%C3%A1nek/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yellowstonetrips.com/when-to-book-yellowstone-lodging/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Prediction markets and expert forecasts

Hypothesis: If any prediction market or expert forecast exists for Yellowstone September 2026 visitation, it could provide a direct estimate. However, such markets are unlikely for this specific target.

Queries issued by the searcher: Yellowstone visitation prediction market 2026; Yellowstone September 2026 visitation forecast; national park visitation forecast 2026; Yellowstone National Park monthly visitation statistics September

- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://doaj.org/article/a9a34a9eb7224f0a87d38d34da1d1b69` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sacbee.com/entertainment/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [attention] Search and social media interest

Hypothesis: Online attention (Google Trends, social media mentions) for Yellowstone in September 2026 may correlate with actual visitation, but the relationship is noisy and not a direct count. It can serve as a directional check.

Queries issued by the searcher: Yellowstone National Park September visitation statistics monthly public use reports; Google Trends Yellowstone National Park September 2026 interest; Yellowstone September 2025 recreation visits 839,579 news release; "Google Trends" Yellowstone National Park interest over time September 2025

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p17 Yellowstone National Park average number of recreation visits in September, 2014 = **663,651** visits (2014-09-01..2018-09-30) [DISCARD: Duplicate of p4 (same 663,651 September average); keep one copy.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p18 September share of average annual visits at Yellowstone National Park, 2014-2018 = **16.51** % (2014-09-01..2018-09-30) [DISCARD: Duplicate of p5; the September share is retained once via p5.] quote: "\| September \| 663,651 \| 16.51% \|"
  - p19 Yellowstone National Park average number of recreation visits in January, 2014-2 = **28,837** visits (2014-01-01..2018-01-31) [DISCARD: Duplicate of p6.] quote: "\| January \| 28,837 \| 0.72% \|"
  - p20 Yellowstone National Park average number of recreation visits in February, 2014- = **33,088** visits (2014-02-01..2018-02-28) [DISCARD: Duplicate of p7.] quote: "\| February \| 33,088 \| 0.82% \|"
  - p21 Yellowstone National Park average number of recreation visits in March, 2014-201 = **22,266** visits (2014-03-01..2018-03-31) [DISCARD: Duplicate of p8.] quote: "\| March \| 22,266 \| 0.55% \|"
  - p22 Yellowstone National Park average number of recreation visits in April, 2014-201 = **44,027** visits (2014-04-01..2018-04-30) [DISCARD: Duplicate of p9.] quote: "\| April \| 44,027 \| 1.10% \|"
  - p23 Yellowstone National Park average number of recreation visits in May, 2014-2018  = **401,449** visits (2014-05-01..2018-05-31) [DISCARD: Duplicate of p10.] quote: "\| May \| 401,449 \| 9.99% \|"
  - p24 Yellowstone National Park average number of recreation visits in June, 2014-2018 = **780,652** visits (2014-06-01..2018-06-30) [DISCARD: Duplicate of p11.] quote: "\| June \| 780,652 \| 19.42% \|"
  - p25 Yellowstone National Park average number of recreation visits in July, 2014-2018 = **947,688** visits (2014-07-01..2018-07-31) [DISCARD: Duplicate of p12.] quote: "\| July \| 947,688 \| 23.57% \|"
  - p26 Yellowstone National Park average number of recreation visits in August, 2014-20 = **839,787** visits (2014-08-01..2018-08-31) [DISCARD: Duplicate of p13.] quote: "\| August \| 839,787 \| 20.89% \|"
  - p27 Yellowstone National Park average number of recreation visits in October, 2014-2 = **223,777** visits (2014-10-01..2018-10-31) [DISCARD: Duplicate of p14.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p28 Yellowstone National Park average number of recreation visits in November, 2014- = **14,323** visits (2014-11-01..2018-11-30) [DISCARD: Duplicate of p15.] quote: "\| November \| 14,323 \| 0.36% \|"
  - p29 Yellowstone National Park average number of recreation visits in December, 2014- = **20,434** visits (2014-12-01..2018-12-31) [DISCARD: Duplicate of p16.] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nypost.com/2026/09/05/us-news/10-best-national-parks-in-america-ranked-as-yellowstone-no-1/` -> **snapshot** (snapshot 20260906015105); points raw/verified 15/0
- dropped by code checks: 15 (period_end missing or unparseable: 14; number: more than one number in value_as_written: 1)

### b1 [own_history] NPS monthly visitation statistics

Hypothesis: Recent September recreation-visit counts for Yellowstone (2019-2025) would provide the target's own historical series, enabling series_naive and yoy_scaling routes. The 2014-2018 average is too old to capture post-COVID and post-2022-flood levels, so this is the single most valuable missing input.

Queries issued by the searcher: Yellowstone National Park September recreation visits 2024 2023 NPS monthly visitation statistics; NPS Visitor Use Statistics Yellowstone monthly public use report September 2022 visitation; Yellowstone visitation statistics September 2025 recreation visits NPS news release; Yellowstone National Park September 2020 recreation visits 871,000 monthly

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] NPS monthly visitation statistics

Hypothesis: Yellowstone January-August 2026 recreation visits would allow a September-to-year-to-date ratio projection. The 2014-2018 seasonal share is the only current basis, but a recent-year ratio would be more representative of 2026 conditions.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits 2026; NPS Visitor Use Statistics Yellowstone monthly public use report 2026; "Yellowstone visitation statistics for August 2026" year-to-date trend recreation visits; Yellowstone recreation visits by month 2019 2020 2021 2022 2023 2024 2025 September totals table

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dailymontanan.com/2026/06/10/yellowstone-national-park-visitation-on-record-pace-through-may/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ypradio.org/regional-news/2026-06-10/another-record-month` -> **snapshot** (snapshot 20260810124904); points raw/verified 9/7
  - p30 Yellowstone National Park recreation visits, May 2026 = **570,272** recreation visits (2026-05-01..2026-05-31) [keep: ] quote: "the park hosted 570,272 visits in May, up 1% from May 2025"
  - p31 Yellowstone National Park recreation visits, May 2025 = **1** percent change in recreation visits (May 2026 vs May 2025) (2025-05-01..2025-05-31) [DISCARD: A percent-change figure (1%) whose base value is already carried by p30; it adds no independent level information and ca] quote: "570,272 visits in May, up 1% from May 2025"
  - p32 Yellowstone National Park recreation visits, May 2021 = **20** percent change in recreation visits (May 2026 vs May 2021) (2021-05-01..2021-05-31) [DISCARD: Percent change vs May 2021, a comparison year not otherwise used; redundant with p30/p34 and not a level.] quote: "up 20 % from May 2021, which was Yellowstone's record-breaking year"
  - p33 Yellowstone National Park annual visitors, 2021 record-breaking year = **4,800,000** visitors (2021-01-01..2021-12-31) [DISCARD: 2021 annual total (4.8M) is a different period and a rounded figure; it is not the target period and cannot be combined ] quote: "record-breaking year with more than 4.8 million visitors"
  - p34 Yellowstone National Park recreation visits, year-to-date 2026 (through May) = **773,653** recreation visits (2026-01-01..2026-05-31) [keep: ] quote: "So far this year, the park has hosted 773,653 recreation visits"
  - p35 Yellowstone National Park recreation visits, year-to-date 2026 vs same time 2025 = **1** percent change in recreation visits (year-to-date 2026 vs ye (2026-01-01..2026-05-31) [DISCARD: Percent change of YTD 2026 vs YTD 2025; the level is already in p34 and the comparison year's level is absent, so it can] quote: "773,653 recreation visits, up 1% from last year at the same time"
  - p36 Yellowstone National Park recreation visits, year-to-date 2026 vs same time 2021 = **19** percent change in recreation visits (year-to-date 2026 vs ye (2026-01-01..2026-05-31) [DISCARD: Percent change of YTD 2026 vs 2021; no 2021 YTD level is supplied, so it is not convertible to a visit count.] quote: "up 19 % from 2021"
- dropped by code checks: 2 (period_end missing or unparseable: 2)

### b3 [shocks] Park operations and access

Hypothesis: Any September 2026 closures, wildfire smoke, road construction, or reservation requirements would materially shift visitation away from the historical seasonal pattern. The road-opening schedule shows normal access, but operational disruptions are not fully covered.

Queries issued by the searcher: Yellowstone National Park September 2026 road status alerts; Yellowstone National Park September 2026 reservation timed entry; Yellowstone National Park visitation statistics September 2025 monthly public use report; Yellowstone National Park fire 2026 August closure smoke

- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm?pubDate=20260625` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'visitation', 'september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p4', 'p5', 'p17', 'p18'] Same underlying NPS 2014-2018 monthly average table; p4/p17 are the same September visit level and p5/p18 the same September share. They are redundant copies, not independent measurements.
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] All are monthly components of the same 2014-2018 NPS average table. They are mutually consistent by construction and provide the seasonal shape, but they are not independent of p4/p5/p17/p18.
- corroborating: ['p1', 'p2', 'p3'] Road-opening schedules for 2026 show all major entrances and interior routes open through October 31, 2026, so no September 2026 access closure is indicated. They are contextual access evidence, not v
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p4', 'p5', 'p17', 'p18'] Same underlying NPS 2014-2018 monthly-average table: p4/p17 are the September visit level (663,651) and p5/p18 its 16.51% annual share. They are duplicate renderings of one measurement, not independen
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] All from the same 2014-2018 NPS monthly-average table; they jointly define the seasonal shape (Jan-Aug sum and September share) used for a share-of-year projection. Duplicated across d4 and d8 directi
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] All from one Yellowstone Public Radio report on 2026 YTD data: May 2026 = 570,272 visits, YTD through May 2026 = 773,653, up ~1% vs 2025 and ~19% vs 2021. Shared source, so they are one evidence clust
- corroborating: ['p1', 'p2', 'p3'] 2026 road-opening schedule shows all five entrances open through October 31, 2026, i.e. normal September access with no scheduled seasonal closure. This is a shock-absence check, not a visit count.
- conflicting: ['p4', 'p30'] The 2014-2018 September average (663,651) predates the post-COVID surge and the 2022 flood; 2026 YTD is running ~1% above 2025 and ~19% above 2021, so the old level is likely too low for 2026. The old

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|

Rejected by code:

- a1 September 2026 visits as a multiple of the 2014-2018 September average level: target-like: names the target period (2026)
- a2 September share of 2026 annual recreation visits: target-like: names the target period (2026)
- a3 2026 annual recreation visits at Yellowstone: target-like: names the target period (2026)

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a1: assumption a1 was rejected (target-like: names the target period (2026)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: names the target period (2026)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

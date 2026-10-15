# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics. A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions counts as multiple visits. | unit recreation visits (count) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), typically via the Visitor Use Statistics program / Integrated Resource Management Applications (IRMA) and the NPS monthly visitation report.

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS historical monthly visitation statistics for Yellowstone National Park

Hypothesis: September recreation visits in recent years (2019, 2021, 2022, 2023, 2024, 2025) provide a seasonal baseline. The 2026 September value is likely to be similar to recent Septembers, adjusted for any known trend or shock. The ratio of September visits to the preceding summer months (July/August) is a stable seasonal pattern.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September 2025 recreation visits; NPS Yellowstone recreation visits September 2024 2023 monthly report; Yellowstone visitation statistics September 2025 NPS news release recreation visits 839,579; Yellowstone recreation visits July August 2025 monthly visitation report

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.miamiherald.com/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [shocks] Known disruptions or events affecting September 2026 visitation

Hypothesis: Any major closures, weather events, road construction, or policy changes in 2026 could shift September visitation away from historical patterns. For example, the 2022 flood caused a drop in June but recovery by September. Identifying such shocks and their expected impact can adjust the baseline estimate.

Queries issued by the searcher: Yellowstone National Park closures 2026; Yellowstone road construction 2026; Yellowstone visitation September 2026; Yellowstone National Park September 2026 closures fire smoke

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/5
  - p1 Yellowstone road opening date: West Entrance to Madison, Madison to Old Faithful = **17** day of month (April 2026) (2026-04-17..2026-04-17) [keep: ] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris, Mammoth Hot Springs to Norris, Norris to Canyon Village"
  - p2 Yellowstone road opening date: East Entrance to Fishing Bridge (Sylvan Pass), Ca = **1** day of month (May 2026) (2026-05-01..2026-05-01) [keep: ] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p3 Yellowstone road opening date: South Entrance to West Thumb, West Thumb to Old F = **8** day of month (May 2026) (2026-05-08..2026-05-08) [keep: ] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass), West Thumb to Lake Village, Tower-Roosevelt to Tower Fall"
  - p4 Yellowstone road opening date: Canyon Village to Tower Fall (Dunraven Pass) (pro = **22** day of month (May 2026) (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Canyon Village to Tower Fall (Dunraven Pass)."
  - p5 Beartooth Highway (US-212) and Chief Joseph Scenic Byway (WY-296) opening date ( = **22** day of month (May 2026) (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Beartooth Highway (US-212), Chief Joseph Scenic Byway (WY-296)."
- `https://www.yellowstonenationalparklodges.com/alerts/` -> **snapshot** (snapshot 20260703035945); points raw/verified 15/0
- `https://highways.fhwa.dot.gov/sites/fhwa.dot.gov/files/2026-05/WY_NPS_YELL_12%282%29_YRB_Newsletter_05.01.2026.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26001.htm` -> **snapshot** (snapshot 20260602225748); points raw/verified 10/4
  - p6 Yellowstone flood event return interval (500-year flood), June 13, 2022 = **500** years (flood return interval) (2022-06-13..2022-06-13) [DISCARD: 2022 flood return-interval fact. It explains the 2022 anomaly but supplies no numeric input for September 2026 and is no] quote: "Yellowstone experienced a 500-year flood event on June 13, 2022."
  - p7 Public comment period length for North Entrance Road EA (days) = **30** days (2026-01-05..2026-02-04) [DISCARD: Length of a 2026 EA comment period. Administrative process detail with no quantitative bearing on September 2026 visitat] quote: "At the conclusion of the 30-day public comment period, NPS will analyze and consider all comments received."
  - p8 Public comment period start date for North Entrance Road EA = **5** date (2026-01-05..2026-01-05) [DISCARD: Start date of the EA comment period. Administrative detail, not a visitation input.] quote: "NPS will accept comments on the EA Jan. 5 - Feb. 4, 2026."
  - p9 Planned timing of final decision on North Entrance Road EA (stated plan) = **2,026** season/year (planned decision timing) (2026-03-20..2026-06-20) [DISCARD: Planned spring-2026 decision timing for the North Entrance Road EA. No confirmed closure or capacity change for Septembe] quote: "A final decision will be made in spring 2026."
- dropped by code checks: 31 (period_end 2026-10-31 after as_of: 5; period_end 2026-10-12 after as_of: 2; period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 1; number: no number in value_as_written: 3; period_end 2026-09-15 after as_of: 1; number: more than one number in value_as_written: 9; period_end missing or unparseable: 7; period_end 2027-10-31 after as_of: 1)

### d3 [base_rates] Seasonal decomposition and day-of-week effects

Hypothesis: September visitation is influenced by the number of weekends, holidays (Labor Day), and weather. The ratio of September visits to annual visits is a stable base rate. Also, the timing of Labor Day (first Monday in September) affects the distribution of visits within the month.

Queries issued by the searcher: Yellowstone annual visitation 2024 record recreation visits; Yellowstone September visitation monthly statistics; Yellowstone visitation statistics September percent annual visits NPS month table; Yellowstone September 2025 recreation visits 839,579

- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 15/15
  - p10 Yellowstone National Park average September recreation visits, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p11 September share of average annual visits, Yellowstone National Park, 2014-2018 a = **16.51** % (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p12 Yellowstone National Park average January visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p13 January share of average annual visits, Yellowstone National Park, 2014-2018 ave = **0.72** % (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p14 Yellowstone National Park average February visits, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p15 February share of average annual visits, Yellowstone National Park, 2014-2018 av = **0.82** % (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p16 Yellowstone National Park average March visits, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p17 March share of average annual visits, Yellowstone National Park, 2014-2018 avera = **0.55** % (2014-03-01..2018-03-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p18 Yellowstone National Park average April visits, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p19 April share of average annual visits, Yellowstone National Park, 2014-2018 avera = **1.1** % (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p20 Yellowstone National Park average May visits, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p21 May share of average annual visits, Yellowstone National Park, 2014-2018 average = **9.99** % (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p22 Yellowstone National Park average June visits, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p23 June share of average annual visits, Yellowstone National Park, 2014-2018 averag = **19.42** % (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p24 Yellowstone National Park average July visits, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260615211304); points raw/verified 13/13
  - p25 Yellowstone National Park average September visits, 2014-2018 average = **663,651** visits (2014-09-01..2018-09-30) [DISCARD: Duplicate of p10 (same 2014-2018 September average, same NPS table, different snapshot). Keeping both would double-count] quote: "\| September \| 663,651 \| 16.51% \|"
  - p26 September share of average annual visits, Yellowstone National Park, 2014-2018 a = **16.51** % (2014-09-01..2018-09-30) [DISCARD: Duplicate of p11 (same 16.51% September share, same NPS table).] quote: "\| September \| 663,651 \| 16.51% \|"
  - p27 Yellowstone National Park average January visits, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [DISCARD: Duplicate of p12 (January 2014-2018 average).] quote: "\| January \| 28,837 \| 0.72% \|"
  - p28 Yellowstone National Park average February visits, 2014-2018 average = **33,088** visits (2014-02-01..2018-02-28) [DISCARD: Duplicate of p14 (February 2014-2018 average).] quote: "\| February \| 33,088 \| 0.82% \|"
  - p29 Yellowstone National Park average March visits, 2014-2018 average = **22,266** visits (2014-03-01..2018-03-31) [DISCARD: Duplicate of p16 (March 2014-2018 average).] quote: "\| March \| 22,266 \| 0.55% \|"
  - p30 Yellowstone National Park average April visits, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [DISCARD: Duplicate of p18 (April 2014-2018 average).] quote: "\| April \| 44,027 \| 1.10% \|"
  - p31 Yellowstone National Park average May visits, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [DISCARD: Duplicate of p20 (May 2014-2018 average).] quote: "\| May \| 401,449 \| 9.99% \|"
  - p32 Yellowstone National Park average June visits, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [DISCARD: Duplicate of p22 (June 2014-2018 average).] quote: "\| June \| 780,652 \| 19.42% \|"
  - p33 Yellowstone National Park average July visits, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [DISCARD: Duplicate of p24 (July 2014-2018 average).] quote: "\| July \| 947,688 \| 23.57% \|"
  - p34 Yellowstone National Park average August visits, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [DISCARD: Duplicate of the August 2014-2018 average already represented in the same NPS table; the August value is available once ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p35 Yellowstone National Park average October visits, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [DISCARD: Duplicate of the October 2014-2018 average from the same NPS table.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p36 Yellowstone National Park average November visits, 2014-2018 average = **14,323** visits (2014-11-01..2018-11-30) [DISCARD: Duplicate of the November 2014-2018 average from the same NPS table.] quote: "\| November \| 14,323 \| 0.36% \|"
  - p37 Yellowstone National Park average December visits, 2014-2018 average = **20,434** visits (2014-12-01..2018-12-31) [DISCARD: Duplicate of the December 2014-2018 average from the same NPS table.] quote: "\| December \| 20,434 \| 0.51% \|"

### d4 [related_series] National Park Service overall visitation and Yellowstone's share

Hypothesis: Yellowstone's September visits can be estimated as a share of total NPS September recreation visits, or as a share of visits to a comparable set of large nature parks. The share may be stable over time. Alternatively, use total U.S. park visitation in September and apply Yellowstone's historical share.

Queries issued by the searcher: NPS total recreation visits September 2025 monthly visitation report; Yellowstone National Park September visitation statistics 2024; NPS national recreation visits September 2025 total monthly summary; Yellowstone September 2023 recreation visits 838,458 park hosted

- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-national-park-september-visits-up-2-from-last-year` -> **snapshot** (snapshot 20241010002924); points raw/verified 9/9
  - p38 Yellowstone National Park recreation visits, September 2024 = **852,435** recreation visits (2024-09-01..2024-09-30) [keep: ] quote: "Yellowstone National Park hosted 852,435 recreation visits in September 2024."
  - p39 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: ] quote: "This is a 2% increase from September 2023 (838,458 recreational visits)."
  - p40 Yellowstone National Park recreation visits, September 2021 = **882,078** recreation visits (2021-09-01..2021-09-30) [keep: ] quote: "This September's visitation showed an 3% decrease from September 2021 (882,078 recreation visits)."
  - p41 Yellowstone National Park year-to-date recreation visits through September 2024 = **4,349,689** recreation visits (2024-01-01..2024-09-30) [keep: ] quote: "So far in 2024, the park has hosted 4,349,689 recreation visits, up 5% from 2023 (4,147,382 recreation visits)"
  - p42 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,147,382** recreation visits (2023-01-01..2023-09-30) [keep: ] quote: "up 5% from 2023 (4,147,382 recreation visits), and down 3% from 2021 (4,472,687 recreation visits)."
  - p43 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [keep: ] quote: "2022 - 3,005,194 (The park was closed June 13 through June 21 due to the historic flood event."
  - p44 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: ] quote: "2021 - 4,472,687"
  - p45 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [keep: ] quote: "2020 - 3,393,642 (The park was closed March 24 through May 17 due to COVID."
  - p46 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [keep: ] quote: "2019 - 3,807,815"
- `https://publiclandsdata.com/national-park-visitation/data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from the number of vehicles entering Yellowstone in September multiplied by average occupancy. Entrance counts may be available from NPS traffic counters or from state DOT data on park entrances. This route requires converting vehicle entries to person visits.

Queries issued by the searcher: Yellowstone entrance vehicle counts September visitation statistics; Yellowstone average vehicle occupancy visitation study; Yellowstone monthly visitation report September recreation visits NPS; Yellowstone traffic counter entrance data monthly vehicles

- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 14/14
  - p47 Yellowstone total vehicle entries, Friday September 3, 2021 (Labor Day weekend) = **8,945** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p48 Yellowstone total vehicle entries, Saturday September 4, 2021 (Labor Day weekend = **11,062** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p49 Yellowstone total vehicle entries, Sunday September 5, 2021 (Labor Day weekend) = **12,380** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p50 Yellowstone total vehicle entries, Monday September 6, 2021 (Labor Day weekend) = **9,982** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p51 Yellowstone total vehicle entries, Friday August 30, 2019 (comparison day) = **7,134** vehicle entries (2019-08-30..2019-08-30) [keep: ] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p52 Yellowstone total vehicle entries, Saturday August 31, 2019 (comparison day) = **8,913** vehicle entries (2019-08-31..2019-08-31) [keep: ] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p53 Yellowstone total vehicle entries, Sunday September 1, 2019 (comparison day) = **10,307** vehicle entries (2019-09-01..2019-09-01) [keep: ] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p54 Yellowstone total vehicle entries, Monday September 2, 2019 (comparison day) = **8,551** vehicle entries (2019-09-02..2019-09-02) [keep: ] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p55 Yellowstone West Entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [keep: ] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p56 Yellowstone South Entrance vehicle entries, Saturday September 4, 2021 = **1,960** vehicle entries (2021-09-04..2021-09-04) [keep: ] quote: "\| South \| 1,960 \| 896 \| 119% \|"
  - p57 Yellowstone East Entrance vehicle entries, Sunday September 5, 2021 = **1,506** vehicle entries (2021-09-05..2021-09-05) [keep: ] quote: "\| East \| 1,506 \| 1,204 \| 25% \|"
  - p58 Yellowstone North Entrance vehicle entries, Monday September 6, 2021 = **1,980** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| North \| 1,980 \| 1,575 \| 26% \|"
  - p59 Yellowstone Northeast Entrance vehicle entries, Monday September 6, 2021 = **745** vehicle entries (2021-09-06..2021-09-06) [keep: ] quote: "\| Northeast \| 745 \| 854 \| -13% \|"
  - p60 Parkwide vehicle entries increase over Labor Day weekend 2021 vs 2019 = **21** % (2021-09-03..2021-09-06) [keep: ] quote: "Parkwide vehicle entries through the Labor Day weekend showed a 21% increase over the same weekend in 2019."
- `https://www.sweetwaternow.com/yellowstone-sees-increase-in-labor-day-weekend-visits/` -> **snapshot** (snapshot 20250723010404); points raw/verified 15/14
  - p61 Yellowstone park-wide total vehicle entries, Friday September 3, 2021 = **8,945** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Duplicate of p47 (same 8,945 parkwide entries, 2021-09-03) republished by sweetwaternow.com.] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p62 Yellowstone park-wide total vehicle entries, Saturday September 4, 2021 = **11,062** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of p48 (same 11,062 parkwide entries, 2021-09-04).] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p63 Yellowstone park-wide total vehicle entries, Sunday September 5, 2021 = **12,380** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of p49 (same 12,380 parkwide entries, 2021-09-05).] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p64 Yellowstone park-wide total vehicle entries, Monday September 6, 2021 = **9,982** vehicle entries (2021-09-06..2021-09-06) [DISCARD: Duplicate of p50 (same 9,982 parkwide entries, 2021-09-06).] quote: "\| Total \| 9,982 \| \| \|"
  - p65 Yellowstone West Entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Duplicate of p55 (same 4,118 West Entrance entries, 2021-09-03).] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p66 Yellowstone West Entrance vehicle entries, Saturday September 4, 2021 = **5,222** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of the West Entrance 2021-09-04 count already represented by p107.] quote: "\| West \| 5,222 \| 4,640 \| 13% \|"
  - p67 Yellowstone West Entrance vehicle entries, Sunday September 5, 2021 = **5,536** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of the West Entrance 2021-09-05 count already represented by p108.] quote: "\| West \| 5,536 \| 5,064 \| 9% \|"
  - p68 Yellowstone West Entrance vehicle entries, Monday September 6, 2021 = **4,293** vehicle entries (2021-09-06..2021-09-06) [DISCARD: Duplicate of the West Entrance 2021-09-06 count already represented by p109.] quote: "\| West \| 4,293 \| 3,599 \| 19% \|"
  - p69 Yellowstone South Entrance vehicle entries, Saturday September 4, 2021 = **1,960** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of p56 (same 1,960 South Entrance entries, 2021-09-04).] quote: "\| South \| 1,960 \| 896 \| 119% \|"
  - p70 Yellowstone North Entrance vehicle entries, Sunday September 5, 2021 = **2,435** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of the North Entrance 2021-09-05 count already represented by p111.] quote: "\| North \| 2,435 \| 1,964 \| 24% \|"
  - p71 Yellowstone East Entrance vehicle entries, Sunday September 5, 2021 = **1,506** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of p57 (same 1,506 East Entrance entries, 2021-09-05).] quote: "\| East \| 1,506 \| 1,204 \| 25% \|"
  - p72 Yellowstone Northeast Entrance vehicle entries, Sunday September 5, 2021 = **803** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of the Northeast Entrance 2021-09-05 count already represented by p59's companion table.] quote: "\| Northeast \| 803 \| 959 \| -16% \|"
  - p73 Yellowstone park-wide total vehicle entries, Friday August 30, 2019 = **7,134** vehicle entries (2019-08-30..2019-08-30) [DISCARD: Duplicate of p51 (same 7,134 parkwide entries, 2019-08-30).] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p74 Yellowstone park-wide total vehicle entries, Sunday September 1, 2019 = **10,307** vehicle entries (2019-09-01..2019-09-01) [DISCARD: Duplicate of p53 (same 10,307 parkwide entries, 2019-09-01).] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
- `https://thefederalnewswire.com/stories/633118309-september-visitation-increases-by-three-percent` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstonegate.com/?p=10256` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d6 [capacity_consumption] Accommodation occupancy and campground use

Hypothesis: Overnight stays in Yellowstone (lodges, campgrounds) are a component of recreation visits. Total visits can be estimated from overnight stays plus day-use visits. September overnight stays may be available from Xanterra or NPS concession reports. The ratio of total visits to overnight stays is a stable multiplier.

Queries issued by the searcher: Yellowstone overnight stays September statistics NPS visitation; Xanterra Yellowstone lodging occupancy September; Yellowstone September 2025 visitation 839,579 overnight stays; NPS Yellowstone total overnight stays September concession lodging backcountry campers IRMA

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.ae/news/article/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-occupancy-amid-n` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cz/zpr%C3%A1vy/%C4%8Dl%C3%A1nek/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.org.es/noticia/artigo/O-turismo-en-Yellowstone-aumenta-durante-a-tempada-baixa--xa-que-os-hoteis-e-aloxamentos-mante%C3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Published forecasts or projections for Yellowstone visitation

Hypothesis: If any travel industry forecasts, NPS projections, or academic models predict 2026 visitation, they can provide a direct estimate or a range. These may be based on economic indicators, past trends, or expert judgment.

Queries issued by the searcher: Yellowstone visitation forecast 2026; Yellowstone National Park tourism projection 2026; Yellowstone September 2025 recreation visits NPS monthly visitation; Yellowstone visitation 2026 forecast economic outlook national park tourism

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/ua44b5bxskoj/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://commerce.mt.gov/_shared/brand/Regions-CVBs/docs/Marketing-Plans/FY26-Marketing-Plans/Gardiner-FY26-DMO-Plan.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d8 [attention] Search interest and social media activity as a leading indicator

Hypothesis: Google Trends or social media mentions for Yellowstone in the weeks before September 2026 may correlate with actual visitation. If search interest is unusually high or low compared to previous years, it could signal a deviation from the historical baseline.

Queries issued by the searcher: Google Trends Yellowstone National Park 2026 search interest; Yellowstone National Park visitation September 2026 forecast; Yellowstone National Park August 2026 visitation statistics NPS monthly report; Yellowstone Google Trends search interest up 27% national parks 2026 vs 2025

- `https://local.newsbreak.com/new-york-post-509648/4868653317141-yellowstone-tops-list-of-americas-most-googled-national-parks-as-interest-in-wild-us-su` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p75 Yellowstone Google search margin over Grand Canyon National Park, July 2025 to J = **1,420,000** searches (2025-07-01..2026-06-30) [DISCARD: Google search margin over Grand Canyon for 2025-07 to 2026-06. No historical series for the same measure, so it cannot b] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://creators.yahoo.com/lifestyle/story/the-most-searched-national-park-in-every-state-reveals-one-clear-favorite-174747097.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [own_history] NPS monthly visitation statistics

Hypothesis: Direct September 2025 and 2026 monthly recreation-visit totals for Yellowstone (and the 2026 July/August values) would let the recent-year series method use the most recent vintage and would let a September-to-summer ratio be computed on 2025-2026 data rather than 2014-2018. This is the single largest gap: the kept September history stops at 2024, so the estimate must extrapolate two years.

Queries issued by the searcher: Yellowstone National Park September 2025 visitation recreation visits NPS; NPS Visitor Use Statistics Yellowstone monthly report 2025; Yellowstone National Park reports August 2026 visitation statistics nps.gov; Yellowstone National Park September 2025 visitation statistics press release 839,579

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-national-park-visits-up-2-in-2025` -> **snapshot** (snapshot 20250905032517); points raw/verified 11/11
  - p76 Yellowstone National Park recreation visits in August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "The park hosted 881,936 visits, showing a 4% decrease from the record year 2021."
  - p77 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far this year the park has hosted 3,547,967 recreation visits, down 1% from 2021."
  - p78 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "2024 - 3,494,350"
  - p79 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p80 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p81 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "2021 - 3,590,609"
  - p82 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
  - p83 Yellowstone National Park record-breaking year 2021 recreation visits (stated as = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was in 2021 with over 4.8 million recreation visits to the park."
  - p84 Yellowstone National Park August 2025 recreation visits change vs. last year (pe = **2** % (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park recreation visits were up 2% in August, compared to last year."
  - p85 Yellowstone National Park August 2025 recreation visits change vs. record year 2 = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "The park hosted 881,936 visits, showing a 4% decrease from the record year 2021."
  - p86 Yellowstone National Park year-to-date through August 2025 recreation visits cha = **1** % (2025-01-01..2025-08-31) [keep: ] quote: "So far this year the park has hosted 3,547,967 recreation visits, down 1% from 2021."

### b2 [physical_flow] entrance traffic counters

Hypothesis: A September vehicle-entry total (or a full-month entrance count) for a recent year would convert the kept Labor-Day-window vehicle counts (p47-p54) into a full-month flow and supply the persons-per-vehicle factor needed to bridge vehicle entries to recreation visits. Without a full-month vehicle total, the vehicle route cannot be executed.

Queries issued by the searcher: Yellowstone vehicle entries September monthly NPS traffic counter; Yellowstone average occupancy per vehicle NPS traffic counter; Yellowstone September 2024 visitation vehicle entries by entrance NPS news release; NPS Yellowstone monthly public use report vehicle entries September 2023 2024 irma.nps.gov

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.publicnow.com/view/472F1877364B37693E164F398C1367B3C0AA9310` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sheridanmedia.com/news/192399/numbers-show-yellowstone-np-had-second-highest-visitor-numbers-in-2024/` -> **snapshot** (snapshot 20250408185445); points raw/verified 12/11
  - p87 Yellowstone National Park combined total visitors through 5 entrances, 2024 = **4,744,000** visitors (2024-01-01..2024-12-31) [keep: ] quote: "In 2024, the park recorded a combined total of 4.744 million visitors through the 5 entrances to the park."
  - p88 Yellowstone National Park combined total visitors through 5 entrances, 2021 (hig = **4,860,000** visitors (2021-01-01..2021-12-31) [keep: ] quote: "only behind 2021, when there were 4.86 million."
  - p89 Yellowstone West Entrance automobile count year-over-year change, 2024 vs 2023 = **1.1** percent (2024-01-01..2024-12-31) [keep: ] quote: "more than 777-thousand automobiles passed through in 2024, which is a 1.1% increase from 2023."
  - p90 Yellowstone Northeast Entrance visitors, 2024 (record year for that entrance) = **133,000** visitors (2024-01-01..2024-12-31) [keep: ] quote: "more visitors used that entrance last year, than any other year and numbers were up 9.7% (133-thousand plus visitors)."
  - p91 Yellowstone Northeast Entrance visitor count year-over-year change, 2024 vs 2023 = **9.7** percent (2024-01-01..2024-12-31) [keep: ] quote: "numbers were up 9.7% (133-thousand plus visitors)."
  - p92 Yellowstone North Entrance visitor count year-over-year change, 2024 vs 2023 = **10** percent (2024-01-01..2024-12-31) [keep: ] quote: "Numbers at the North entrance were up nearly 10% from the previous year"
  - p93 Yellowstone South Entrance visitor count year-over-year change, 2024 vs 2023 = **4.6** percent (2024-01-01..2024-12-31) [keep: ] quote: "the South entrance was up 4.6%"
  - p94 Yellowstone East Entrance visitor count year-over-year change, 2024 vs 2023 = **2.9** percent (2024-01-01..2024-12-31) [keep: ] quote: "the East entrance saw a decline down 2.9%."
  - p95 Yellowstone West Entrance scheduled road opening date = **18** day of month (April) (2025-04-18..2025-04-18) [keep: ] quote: "scheduled to open the west entrance on April 18th"
  - p96 Yellowstone East Entrance scheduled road opening date = **2** day of month (May) (2025-05-02..2025-05-02) [keep: ] quote: "the East entrance on May 2nd"
  - p97 Yellowstone South Entrance scheduled road opening date = **9** day of month (May) (2025-05-09..2025-05-09) [keep: ] quote: "the South entrance on May 9th."
- `https://www.nps.gov/yell/learn/news/21025.htm` -> **snapshot** (snapshot 20260606114436); points raw/verified 15/15
  - p98 Yellowstone parkwide vehicle entries, Friday September 3, 2021 (Labor Day weeken = **8,945** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Duplicate of p47 (same 8,945 parkwide entries, 2021-09-03).] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p99 Yellowstone parkwide vehicle entries, Saturday September 4, 2021 (Labor Day week = **11,062** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of p48 (same 11,062 parkwide entries, 2021-09-04).] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p100 Yellowstone parkwide vehicle entries, Sunday September 5, 2021 (Labor Day weeken = **12,380** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of p49 (same 12,380 parkwide entries, 2021-09-05).] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p101 Yellowstone parkwide vehicle entries, Monday September 6, 2021 (Labor Day weeken = **9,982** vehicle entries (2021-09-06..2021-09-06) [DISCARD: Duplicate of p50 (same 9,982 parkwide entries, 2021-09-06).] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p102 Yellowstone parkwide vehicle entries, Friday August 30, 2019 (comparison day) = **7,134** vehicle entries (2019-08-30..2019-08-30) [DISCARD: Duplicate of p51 (same 7,134 parkwide entries, 2019-08-30).] quote: "\| Total \| 8,945 \| 7,134 \| 25% \|"
  - p103 Yellowstone parkwide vehicle entries, Saturday August 31, 2019 (comparison day) = **8,913** vehicle entries (2019-08-31..2019-08-31) [DISCARD: Duplicate of p52 (same 8,913 parkwide entries, 2019-08-31).] quote: "\| Total \| 11,062 \| 8,913 \| 24% \|"
  - p104 Yellowstone parkwide vehicle entries, Sunday September 1, 2019 (comparison day) = **10,307** vehicle entries (2019-09-01..2019-09-01) [DISCARD: Duplicate of p53 (same 10,307 parkwide entries, 2019-09-01).] quote: "\| Total \| 12,380 \| 10,307 \| 20% \|"
  - p105 Yellowstone parkwide vehicle entries, Monday September 2, 2019 (comparison day) = **8,551** vehicle entries (2019-09-02..2019-09-02) [DISCARD: Duplicate of p54 (same 8,551 parkwide entries, 2019-09-02).] quote: "\| Total \| 9,982 \| 8,551 \| 17% \|"
  - p106 Yellowstone West Entrance vehicle entries, Friday September 3, 2021 = **4,118** vehicle entries (2021-09-03..2021-09-03) [DISCARD: Duplicate of p55 (same 4,118 West Entrance entries, 2021-09-03).] quote: "\| West \| 4,118 \| 3,337 \| 23% \|"
  - p107 Yellowstone West Entrance vehicle entries, Saturday September 4, 2021 = **5,222** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of the West Entrance 2021-09-04 count already represented by p66.] quote: "\| West \| 5,222 \| 4,640 \| 13% \|"
  - p108 Yellowstone West Entrance vehicle entries, Sunday September 5, 2021 = **5,536** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of the West Entrance 2021-09-05 count already represented by p67.] quote: "\| West \| 5,536 \| 5,064 \| 9% \|"
  - p109 Yellowstone West Entrance vehicle entries, Monday September 6, 2021 = **4,293** vehicle entries (2021-09-06..2021-09-06) [DISCARD: Duplicate of the West Entrance 2021-09-06 count already represented by p68.] quote: "\| West \| 4,293 \| 3,599 \| 19% \|"
  - p110 Yellowstone South Entrance vehicle entries, Saturday September 4, 2021 = **1,960** vehicle entries (2021-09-04..2021-09-04) [DISCARD: Duplicate of p56 (same 1,960 South Entrance entries, 2021-09-04).] quote: "\| South \| 1,960 \| 896 \| 119% \|"
  - p111 Yellowstone North Entrance vehicle entries, Sunday September 5, 2021 = **2,435** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of the North Entrance 2021-09-05 count already represented by p70.] quote: "\| North \| 2,435 \| 1,964 \| 24% \|"
  - p112 Yellowstone East Entrance vehicle entries, Sunday September 5, 2021 = **1,506** vehicle entries (2021-09-05..2021-09-05) [DISCARD: Duplicate of p57 (same 1,506 East Entrance entries, 2021-09-05).] quote: "\| East \| 1,506 \| 1,204 \| 25% \|"
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b3 [shocks] 2026 conditions

Hypothesis: Any confirmed 2026 September closure, construction, fire, or reservation policy change would resolve whether September 2026 should be shifted below the recent-year baseline. The kept road schedule (p1-p5) shows normal access, but the North Entrance Road EA (p7-p9) leaves a construction risk unresolved.

Queries issued by the searcher: Yellowstone 2026 road construction closures September; Yellowstone 2026 reservation timed entry policy; Yellowstone 2026 fire smoke closure; Yellowstone North Entrance Road construction 2026 environmental assessment

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/5
  - p113 Yellowstone 2026 projected road opening date: West Entrance to Madison, Madison  = **17** day of month (April 2026) (2026-04-17..2026-04-17) [DISCARD: Duplicate of p1 (same 2026 West Entrance opening date, April 17).] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris, Mammoth Hot Springs to Norris, Norris to Canyon Village"
  - p114 Yellowstone 2026 projected road opening date: East Entrance to Fishing Bridge (S = **1** day of month (May 2026) (2026-05-01..2026-05-01) [DISCARD: Duplicate of p2 (same 2026 East Entrance opening date, May 1).] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p115 Yellowstone 2026 projected road opening date: South Entrance to West Thumb, West = **8** day of month (May 2026) (2026-05-08..2026-05-08) [DISCARD: Duplicate of p3 (same 2026 South Entrance opening date, May 8).] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass), West Thumb to Lake Village, Tower-Roosevelt to Tower Fall"
  - p116 Yellowstone 2026 projected road opening date: Canyon Village to Tower Fall (Dunr = **22** day of month (May 2026) (2026-05-22..2026-05-22) [DISCARD: Duplicate of p4 (same 2026 Dunraven Pass opening date, May 22).] quote: "Open May 22 - October 12, 2026: Canyon Village to Tower Fall (Dunraven Pass)."
  - p117 Yellowstone 2026 projected road opening date: Beartooth Highway (US-212), Chief  = **22** day of month (May 2026) (2026-05-22..2026-05-22) [DISCARD: Duplicate of p5 (same 2026 Beartooth/Chief Joseph opening date, May 22).] quote: "Open May 22 - October 12, 2026: Beartooth Highway (US-212), Chief Joseph Scenic Byway (WY-296)."
- `https://home.nps.gov/yell/learn/management/current-fire-activity.htm` -> **snapshot** (snapshot 20260207162557); points raw/verified 11/1
  - p118 Document last updated date = **13** day of month (November 2025) (2025-11-13..2025-11-13) [DISCARD: A page last-updated date, not a measurement of visitation or of any quantity that enters the estimate.] quote: "Last updated: November 13, 2025"
- `https://www.recreation.gov/sitepass/72451` -> **snapshot** (snapshot 20260628224112); points raw/verified 0/0
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 20 (period_end 2026-10-31 after as_of: 4; period_end 2026-10-12 after as_of: 2; period_end 2026-11-30 after as_of: 1; period_end 2026-09-30 after as_of: 1; number: no number in value_as_written: 1; period_end 2026-09-15 after as_of: 1; missing quote or value_as_written: 3; period_end missing or unparseable: 7)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'visitation', 'september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p38', 'p39', 'p40'] Three consecutive recent September recreation-visit totals (2021, 2023, 2024) from the same NPS monthly-statistics lineage, all quoted via the same news outlet. They establish the recent September lev
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46'] Year-to-date-through-September totals for 2019-2024. These are cumulative, not September-only, but they corroborate the level and the 2022 flood dip (p43) and the 2020 COVID dip (p45). Useful as conte
- corroborating: ['p10', 'p11', 'p25', 'p26'] Duplicate copies of the same 2014-2018 September average (663,651 visits; 16.51% of annual). Same underlying NPS table, two snapshots. They give a pre-2020 seasonal baseline that is materially lower t
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37'] Monthly 2014-2018 averages and shares. They define the seasonal shape (July peak, September ~16.5% of annual) and let September be expressed as a ratio to July/August. Same source and vintage as p10/p
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5'] 2026 road-opening/closing schedule. All entrances and the Beartooth/Chief Joseph routes are open through at least October 12-31, 2026, so no September 2026 access restriction is implied. This supports
- corroborating: ['p6', 'p7', 'p8', 'p9'] 2022 flood and 2026 North Entrance Road EA process. The flood (p6) explains the 2022 anomaly; the EA comment period and planned spring-2026 decision (p7-p9) indicate possible construction/closure risk
- corroborating: ['p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p60', 'p61', 'p62', 'p63', 'p64', 'p73', 'p74'] Labor Day weekend 2021 vs 2019 vehicle-entry counts, park-wide. Two URLs (nps.gov and sweetwaternow.com) carry the same numbers, so they are one underlying measurement, not independent confirmation. T
- corroborating: ['p55', 'p56', 'p57', 'p58', 'p59', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72'] Entrance-level vehicle entries for the same Labor Day weekend. Same underlying counts as the park-wide totals; useful only for entrance-mix context, not as independent evidence.
- corroborating: ['p75'] Google search margin for Yellowstone over Grand Canyon, July 2025-June 2026. Weak attention signal; no historical series to calibrate against, so it can only support a qualitative 'no collapse in inte
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p38', 'p39', 'p40'] Three consecutive recent Septembers (2024, 2023, 2021) from the same NPS monthly-reporting lineage, all in the 838k-882k band. They establish the recent September level and its mild downward drift fro
- corroborating: ['p10', 'p25'] Duplicate copies of the same 2014-2018 September average (663,651) from two snapshots of the same NPS seasonal table. Same underlying measurement; keep one as the older-vintage seasonal anchor.
- corroborating: ['p11', 'p26'] Duplicate copies of the September share of annual visits (16.51%) from the same NPS table. Same measurement, two snapshots.
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37'] The full 2014-2018 monthly seasonal profile from the same NPS table. Internally consistent (monthly values and shares sum to the annual total). Useful for the September share and for the summer-to-Sep
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46'] Year-to-date-through-September totals for 2019-2024 from one NPS-derived article. They are consistent with the September monthly values (e.g. 2024 YTD 4,349,689 minus August YTD 3,494,350 is close to 
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86'] August 2025 level and YTD-through-August series 2020-2025 from one NPS-derived article. These are the most recent pre-cutoff vintages and let the September-to-summer ratio be computed on 2024-2025 dat
- corroborating: ['p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112'] Labor-Day-window vehicle-entry counts for 2019 and 2021, duplicated across three URLs (nps.gov, sweetwaternow.com) that all reproduce the same NPS table. Same underlying measurement; the duplicates ad
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p113', 'p114', 'p115', 'p116', 'p117'] 2026 road-opening schedule, duplicated across two snapshots of the same NPS page. Shows all five entrances open through September 2026 with normal season dates, i.e. no access restriction in the targe
- corroborating: ['p7', 'p8', 'p9'] North Entrance Road EA process: 30-day comment window Jan 5-Feb 4, 2026, with a final decision planned for spring 2026. This is a construction/closure risk for the North Entrance corridor that could d
- contextual: ['p6'] The June 2022 flood was a 500-year event that closed the park for nine days. It explains the 2022 YTD anomaly (p43, p80) and is a reminder that a low-probability shock can move a single month far from
- corroborating: ['p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97'] Entrance-level 2024 counts and year-over-year changes, plus 2025 opening dates, from one regional outlet. They confirm the 2024 annual level (~4.74M) and that no entrance was structurally suppressed i
- contextual: ['p75'] Google search margin for Yellowstone over Grand Canyon, July 2025-June 2026. Attention is elevated but the metric is a relative search margin, not a visitation level, and no comparable prior-year valu
- contextual: ['p118'] Page last-updated date for the NPS seasonal table. Confirms the 2014-2018 seasonal profile is an old vintage and should be down-weighted relative to 2021-2025 data.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 recreation visits as a multiple of September 2024 recreation visits | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m1 (m1) | The kept September series is 882,078 (2021), 838,458 (2023), 852,435 (2024), i.e. a mild decline then stabilization. The 2025 August level (881,936, p76) is up 2% on 2024 (p84) and YTD through August 2025 is 3,547,967 (p77) versus 3,494,350 in 2024 (p78), so 2025 is running slightly above 2024. With | No confirmed September 2026 closure, fire, or reservation change materially different from 2021-2024 conditions; the North Entrance Road EA (p7-p9) does not result in a September 2026 corridor closure. | A confirmed September 2026 closure or construction restriction on a major entrance, a published 2026 July/August total far below the 2024-2025 pattern, or a published September 2025 value outside the 838k-882k band. |
| a2 | September 2026 recreation visits as a multiple of the 2024-2025 September-to-August ratio applied to August 2025 | 0.97 | 0.85..1.1 | 0.6837..1.367 (widened) | ratio | m2 (m2) | The 2014-2018 seasonal profile gives September/August = 663,651/839,787 = 0.79, but recent Septembers have been unusually strong relative to August (2024 September 852,435 versus 2024 August implied near 900k). The 2024-2025 data (p38, p76) imply a September-to-August ratio near 0.95-1.0. This facto | The 2025-2026 seasonal shape resembles 2024-2025 rather than the 2014-2018 profile, and no September-specific shock occurs. | Evidence that September 2026 demand is following the older 0.79 seasonal ratio, e.g. a sharp post-Labor-Day drop reported for 2026. |
| a3 | Persons per vehicle entering Yellowstone in September | 2.6 | 2..3.4 | 1.844..3.688 (widened) | persons per vehicle | unused | NPS recreation-visit counts are person entries; the kept vehicle-entry counts (p47-p54) are vehicle entries. A parkwide average occupancy of about 2.6 persons per vehicle is the standard bridge for Yellowstone-type parks, with a wide band reflecting buses, motorcycles, and single-occupant vehicles.  | Used only to convert a September vehicle-entry total into person visits; the vehicle total itself must come from a kept or assumed full-month flow. | A published NPS persons-per-vehicle factor for Yellowstone September outside 2.0-3.4. |
| a4 | September 2026 full-month vehicle entries at Yellowstone | 330,000 | 250,000..430,000 | 231,840..463,681 (widened) | vehicle entries | unused | The kept Labor-Day-window counts (p47-p54) show roughly 42,000 parkwide vehicle entries over four days in 2021. Scaling a comparable early-September peak to a full 30-day month with a post-Labor-Day taper gives a full-month total in the low hundreds of thousands. No kept point supplies a full-month  | September 2026 traffic resembles the 2021 early-September pattern and no entrance is closed. | A published September 2026 or recent-September full-month vehicle-entry total outside 250k-430k. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 843,346 | ['p38'] / ['a1'] | [] |  | 0.33 | median_of_backtested |  |
| m2 | formula_mc | 852,885 | ['p76'] / ['a2'] | [] |  | 0.33 | median_of_backtested |  |
| m3 | formula_mc | n/a | [] / ['a3', 'a4'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |
| m4 | series_naive | 845,446 |  | [2024] | 0.009 | 0.33 | backtest |  |
| m5 | ratio | n/a |  | [] |  | 0.00 |  | signal has no value for 2026 |

Result: central **847,216**, 80% interval [571,724, 1,255,458], basis monte_carlo, weight rule inverse_backtest_error, weight on methods that use assumptions 0.67

## Final answer

The best computed estimate for recreation visits to Yellowstone National Park during September 2026, as reported in NPS monthly visitation statistics, is 847,216 visits. The supplied interval is 571,724 to 1,255,458, a model-based range conditional on the assumptions rather than a demonstrated accuracy guarantee.

Evidence combines 3 weighted routes. The most direct transfers the most recent kept September level (843,346, weight 33%) using assumption a1 (1, range 0.6991 to 1.398). A second route scales the recent summer level by a September-to-August ratio (852,885, weight 33%; a2 0.97, 0.6837 to 1.367). A naive September mean (845,446, weight 33%) serves as a robustness check. Observed inputs are historical NPS monthly values; the [n] transfer and seasonal ratios are assumptions.

Main risk: a September-specific shock or definitional revision. Missing evidence: any published [n] monthly data or September vehicle-flow totals.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 recreation visits as a multiple of September 2024 recreation visits: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m1. Overturned by: A confirmed September 2026 closure or construction restriction on a major entrance, a published [n] July/August total far below the [n]-2025 pattern, or a published September 2025 value outside the [n]k-[n]k band.
- a2 September 2026 recreation visits as a multiple of the [n]-2025 September-to-August ratio applied to August 2025: 0.97 ratio, range 0.6837 to 1.367 (range widened by code); used by m2. Overturned by: Evidence that September 2026 demand is following the older [n] seasonal ratio, e.g. a sharp post-Labor-Day drop reported for 2026.

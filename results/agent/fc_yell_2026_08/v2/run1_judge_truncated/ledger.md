# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics. A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on different days counts as multiple visits. | unit recreation visits | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), typically via the Visitor Use Statistics program (IRMA/NPS Stats).

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [own_history] NPS historical monthly visitation statistics

Hypothesis: August recreation visits in recent years (2019-2025) provide a baseline for the seasonal peak. The 2026 value is likely to be similar to recent Augusts, adjusted for any known shocks (e.g., 2022 flood, 2020 COVID).

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics August 2025; NPS Yellowstone visitation August 2024 2023 recreation visits; Yellowstone visitation statistics August 2020 recreation visits COVID; Yellowstone National Park visitation statistics July 2026

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p1 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p2 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p3 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p4 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p5 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p6 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p7 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p8 Yellowstone National Park year-to-date recreation visits through August 2025 (li = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "2025 - 3,547,967"
  - p9 Yellowstone National Park year-to-date recreation visits through August 2024 (li = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "2024 - 3,494,350"
  - p10 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p11 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p12 Yellowstone National Park year-to-date recreation visits through August 2021 (li = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "2021 - 3,590,609"
  - p13 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/20038.htm` -> **snapshot** (snapshot 20260208212322); points raw/verified 9/9
  - p14 Yellowstone National Park recreation visits, August 2020 = **881,543** recreation visits (2020-08-01..2020-08-31) [keep: ] quote: "The park hosted 881,543 recreation visits in August 2020."
  - p15 Percent change in Yellowstone recreation visits, August 2020 vs August 2019 = **7.5** % (2020-08-01..2020-08-31) [keep: ] quote: "This is a 7.5% increase from August 2019, making it the second busiest August on record."
  - p16 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,546,373** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "So far in 2020, the park has hosted 2,546,373 recreation visits, down 18% from the same period last year."
  - p17 Percent change in Yellowstone year-to-date recreation visits through August 2020 = **18** % (2020-01-01..2020-08-31) [keep: ] quote: "So far in 2020, the park has hosted 2,546,373 recreation visits, down 18% from the same period last year."
  - p18 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [keep: ] quote: "2019 - 3,114,697"
  - p19 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [keep: ] quote: "2018 - 3,136,241"
  - p20 Yellowstone National Park year-to-date recreation visits through August 2017 = **3,232,707** recreation visits (2017-01-01..2017-08-31) [keep: ] quote: "2017 - 3,232,707"
  - p21 Yellowstone National Park year-to-date recreation visits through August 2016 = **3,269,024** recreation visits (2016-01-01..2016-08-31) [keep: ] quote: "2016 - 3,269,024"
  - p22 Yellowstone National Park year-to-date recreation visits through August 2015 = **3,133,965** recreation visits (2015-01-01..2015-08-31) [keep: ] quote: "2015 - 3,133,965"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] NPS year-to-date visitation reports

Hypothesis: Year-to-date recreation visits through July 2026 can be used to estimate August 2026 by applying the historical share of August in the annual total or the historical ratio of August to July visits.

Queries issued by the searcher: Yellowstone year-to-date visitation 2026; NPS Yellowstone visitation July 2026; Yellowstone National Park August 2025 visitation statistics recreation visits; Yellowstone monthly visitation 2025 total annual recreation visits 4.7 million August

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p23 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p24 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p25 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p26 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p27 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p28 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "down 1% from 2021 (2,668,765 recreation visits)."
  - p29 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p30 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p31 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
  - p32 Yellowstone National Park annual recreation visits, 2021 record-breaking year = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p33 Yellowstone National Park recreation visits in August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p34 Yellowstone National Park recreation visits in August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p35 Yellowstone National Park recreation visits in August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p36 Yellowstone National Park record-breaking annual recreation visits in 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p37 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p38 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p39 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p40 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p41 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p42 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26016.htm` -> **snapshot** (snapshot 20260714213711); points raw/verified 13/13
  - p43 Yellowstone National Park recreation visits, June 2026 = **903,025** recreation visits (2026-06-01..2026-06-30) [keep: ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p44 Yellowstone National Park recreation visits, June 2025 = **928,250** recreation visits (2025-06-01..2025-06-30) [keep: ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p45 Yellowstone National Park recreation visits, June 2021 = **938,845** recreation visits (2021-06-01..2021-06-30) [keep: ] quote: "Visitation in June 2026 showed a 4% decrease from June 2021 (938,845 recreation visits)."
  - p46 Yellowstone National Park record annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021 with over 4.8 million recreation visits."
  - p47 Yellowstone National Park year-to-date recreation visits through June 2026 = **1,676,678** recreation visits (2026-01-01..2026-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p48 Yellowstone National Park year-to-date recreation visits through June 2025 = **1,690,922** recreation visits (2025-01-01..2025-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p49 Yellowstone National Park year-to-date recreation visits through June 2021 = **1,587,998** recreation visits (2021-01-01..2021-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p50 Yellowstone National Park year-to-date recreation visits through June 2026 (tren = **1,676,678** recreation visits (2026-01-01..2026-06-30) [keep: ] quote: "2026 - 1,676,678"
  - p51 Yellowstone National Park year-to-date recreation visits through June 2025 (tren = **1,690,922** recreation visits (2025-01-01..2025-06-30) [keep: ] quote: "2025 - 1,690,922"
  - p52 Yellowstone National Park year-to-date recreation visits through June 2024 = **1,633,739** recreation visits (2024-01-01..2024-06-30) [keep: ] quote: "2024 - 1,633,739"
  - p53 Yellowstone National Park year-to-date recreation visits through June 2023 = **1,492,843** recreation visits (2023-01-01..2023-06-30) [keep: ] quote: "2023 - 1,492,843"
  - p54 Yellowstone National Park year-to-date recreation visits through June 2022 = **1,258,834** recreation visits (2022-01-01..2022-06-30) [keep: ] quote: "2022 - 1,258,834 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p55 Yellowstone National Park year-to-date recreation visits through June 2021 (tren = **1,587,998** recreation visits (2021-01-01..2021-06-30) [keep: ] quote: "2021 - 1,587,998"

### d3 [shocks] News and park alerts for 2026

Hypothesis: Any closures, road construction, wildfires, or policy changes in 2026 could significantly affect August visitation. Identifying such events helps adjust the historical baseline.

Queries issued by the searcher: Yellowstone National Park closures 2026; Yellowstone visitation 2026 news record; Yellowstone National Park visitation statistics July 2026 news release; Yellowstone wildfire 2026 smoke closures August

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p56 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p57 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p58 Yellowstone National Park recreation visits, July 2021 (record-breaking year, bu = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p59 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p60 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p61 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p62 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p63 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p64 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p65 Yellowstone National Park year-to-date recreation visits through July 2022 (park = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm?pubDate=20260625` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26011.htm` -> **snapshot** (snapshot 20260807220206); points raw/verified 13/12
  - p66 Yellowstone National Park recreation visits, May 2026 = **570,272** recreation visits (2026-05-01..2026-05-31) [keep: ] quote: "Yellowstone National Park hosted 570,272 recreation visits in May 2026, up 1% from May 2025 (566,363 recreation visits)."
  - p67 Yellowstone National Park recreation visits, May 2025 = **566,363** recreation visits (2025-05-01..2025-05-31) [keep: ] quote: "up 1% from May 2025 (566,363 recreation visits)."
  - p68 Yellowstone National Park recreation visits, May 2021 = **473,799** recreation visits (2021-05-01..2021-05-31) [keep: ] quote: "showed a 20% increase from May 2021 (473,799 recreation visits), which was Yellowstone's record-breaking year"
  - p69 Yellowstone National Park recreation visits, year-to-date through May 2026 = **773,653** recreation visits (2026-01-01..2026-05-31) [keep: ] quote: "So far in 2026, the park has hosted 773,653 recreation visits, up 1% from 2025 (762,672 recreation visits)"
  - p70 Yellowstone National Park recreation visits, year-to-date through May 2025 = **762,672** recreation visits (2025-01-01..2025-05-31) [keep: ] quote: "up 1% from 2025 (762,672 recreation visits), and up 19% from 2021 (649,153 recreation visits)."
  - p71 Yellowstone National Park recreation visits, year-to-date through May 2021 = **649,153** recreation visits (2021-01-01..2021-05-31) [keep: ] quote: "and up 19% from 2021 (649,153 recreation visits)."
  - p72 Yellowstone National Park recreation visits, year-to-date through May 2024 = **719,127** recreation visits (2024-01-01..2024-05-31) [keep: ] quote: "2024 - 719,127"
  - p73 Yellowstone National Park recreation visits, year-to-date through May 2023 = **644,979** recreation visits (2023-01-01..2023-05-31) [keep: ] quote: "2023 - 644,979"
  - p74 Yellowstone National Park recreation visits, year-to-date through May 2022 = **733,471** recreation visits (2022-01-01..2022-05-31) [keep: ] quote: "2022 - 733,471 (The park was closed June 13 through June 21 due to the historic flood event."
  - p75 Yellowstone National Park record-breaking year total recreation visits (2021) = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits."
  - p76 Yellowstone National Park closure period due to historic flood event, June 2022  = **13** date (2022-06-13..2022-06-13) [keep: ] quote: "The park was closed June 13 through June 21 due to the historic flood event."
  - p77 Yellowstone National Park closure period due to historic flood event, June 2022  = **21** date (2022-06-21..2022-06-21) [keep: ] quote: "The park was closed June 13 through June 21 due to the historic flood event."
- `https://www.nps.gov/yell/planyourvisit/operating-dates.htm` -> **snapshot** (snapshot 20260717083945); points raw/verified 15/0
- dropped by code checks: 16 (number: no number in value_as_written: 2; period_end missing or unparseable: 1; period_end 2026-09-13 after as_of: 1; period_end 2026-09-19 after as_of: 1; period_end 2026-09-26 after as_of: 1; period_end 2026-10-17 after as_of: 2; period_end 2026-09-27 after as_of: 1; period_end 2026-10-12 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-10-11 after as_of: 1; period_end 2026-10-18 after as_of: 1; period_end 2026-10-24 after as_of: 2; period_end 2026-10-10 after as_of: 1)

### d4 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from vehicle entries at park entrances multiplied by average occupancy. If entrance counts for August 2026 are available (or can be inferred from recent data), this provides an independent route.

Queries issued by the searcher: Yellowstone National Park August vehicle entries statistics entrance station counts; Yellowstone average visitors per vehicle occupancy study; NPS Visitor Use Statistics Yellowstone monthly recreation visits August 2025 871,000; Yellowstone persons per vehicle multiplier 2.58 table by month entrance station IRMA

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p78 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p79 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p80 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p81 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p82 Yellowstone National Park year-to-date recreation visits through August, 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p83 Yellowstone National Park year-to-date recreation visits through August, 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p84 Yellowstone National Park year-to-date recreation visits through August, 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p85 Yellowstone National Park year-to-date recreation visits through August, 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p86 Yellowstone National Park year-to-date recreation visits through August, 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p87 Yellowstone National Park year-to-date recreation visits through August, 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://ravallirepublic.com/outdoors/article_8902f5e0-bbea-5962-b86d-545832082acf.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] Accommodation and campground capacity

Hypothesis: Overnight stays in the park (lodges, campgrounds) plus day-use visits can be used to estimate total recreation visits. Occupancy rates and capacity constraints may limit the maximum possible visits.

Queries issued by the searcher: Yellowstone National Park overnight stays monthly statistics lodges campgrounds; Yellowstone lodging occupancy August statistics average length of stay; Yellowstone National Park number of lodging rooms campsites capacity total; Yellowstone visitation August 2025 report NPS recreation visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://omb.report/icr/200709-1024-001/doc/7367201.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://industry.visitjacksonhole.com/wp-content/uploads/2023/06/Situational-Analysis-Report.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `http://www.yellowstone-bearman.com/parkfacts.html` -> **snapshot** (snapshot 20260519035817); points raw/verified 15/1
  - p88 Yellowstone National Park record year visitation (visitors) = **3,144,405** visitors (1992-01-01..1992-12-31) [keep: ] quote: "Record year: 1992--3,144,405 visitors"
- dropped by code checks: 14 (period_end missing or unparseable: 14)

### d6 [base_rates] Seasonal patterns and year-over-year growth

Hypothesis: The ratio of August visits to annual visits is relatively stable. Applying this ratio to a forecast of 2026 annual visits (or using recent growth rates) can yield an estimate.

Queries issued by the searcher: Yellowstone annual visitation 2025 recreation visits record; Yellowstone August 2025 visitation monthly statistics NPS; Yellowstone annual recreation visits 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 table; Yellowstone visitation statistics July 2026 recreation visits down 1%

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 13/13
  - p89 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p90 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p91 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p92 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p93 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p94 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p95 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p96 Yellowstone National Park year-to-date recreation visits through August 2025 (tr = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "2025 - 3,547,967"
  - p97 Yellowstone National Park year-to-date recreation visits through August 2024 (tr = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "2024 - 3,494,350"
  - p98 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p99 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p100 Yellowstone National Park year-to-date recreation visits through August 2021 (tr = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "2021 - 3,590,609"
  - p101 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://oilcity.news/community/wyoming-community-2/2026/08/11/yellowstone-reports-958k-visitors-in-july-visits-down-2-from-2025/` -> **snapshot** (snapshot 20260812092842); points raw/verified 10/10
  - p102 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025, when 975,109 people visited the park."
  - p103 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025, when 975,109 people visited the park."
  - p104 Yellowstone National Park recreation visits, July 2021 = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "tation in July 2026 showed an 11% decrease from July 2021, when the park hosted 1,080,767 visits, both part of Yellowstone's record-breaking year with over 4.8 million recreation visits and the busies"
  - p105 Yellowstone National Park annual recreation visits, 2021 record-breaking year (o = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "both part of Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p106 Yellowstone National Park year-to-date recreation visits, 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025's 2,666,031 recreation visits and down 1% from 2021's 2,668,765 recreation visits."
  - p107 Yellowstone National Park year-to-date recreation visits, 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025's 2,666,031 recreation visits and down 1% from 2021's 2,668,765 recreation visits."
  - p108 Yellowstone National Park year-to-date recreation visits, 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025's 2,666,031 recreation visits and down 1% from 2021's 2,668,765 recreation visits."
  - p109 Yellowstone National Park year-to-date recreation visits, 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "- 2024 - 2,626,091"
  - p110 Yellowstone National Park year-to-date recreation visits, 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "- 2023 - 2,462,535"
  - p111 Yellowstone National Park year-to-date recreation visits, 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "- 2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"

### d7 [attention] Search and social media interest

Hypothesis: Online attention (Google Trends, social media mentions) for Yellowstone in summer 2026 may correlate with visitation. If attention is significantly higher or lower than previous years, it could signal a change in visits.

Queries issued by the searcher: Google Trends Yellowstone National Park 2026; Yellowstone National Park visitation July 2026 record; Yellowstone National Park visitation statistics August 2025 recreation visits; Yellowstone August 2024 visitation 900,000 recreation visits NPS

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p112 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p113 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p114 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p115 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p116 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p117 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p118 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p119 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p120 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p121 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p122 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p123 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p124 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p125 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p126 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p127 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p128 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p129 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p130 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p131 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p132 Yellowstone Google search lead over Grand Canyon National Park, July 2025 to Jun = **1,420,000** searches (2025-07-01..2026-06-30) [keep: ] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### d8 [forecasts_markets] Tourism forecasts and prediction markets

Hypothesis: Any published forecasts for Yellowstone visitation in 2026 or prediction markets on tourism numbers could provide a direct estimate or a range.

Queries issued by the searcher: Yellowstone visitation forecast 2026; Yellowstone National Park monthly visitation statistics August; Yellowstone July 2026 visitation statistics recreation visits; national park visitation forecast 2026 tourism outlook

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p133 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p134 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p135 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p136 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p137 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p138 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p139 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p140 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p141 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p142 Yellowstone National Park year-to-date recreation visits through July 2022 (floo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p143 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p144 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p145 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p146 Yellowstone National Park record-breaking year 2021 recreation visits (stated as = **4,800,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p147 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p148 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p149 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p150 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p151 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p152 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 15/15
  - p153 Yellowstone National Park average number of visits in August, 2014-2018 average = **839,787** visits (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p154 Yellowstone National Park August visits as share of average annual visits, 2014- = **20.89** % (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p155 Yellowstone National Park average number of visits in July, 2014-2018 average = **947,688** visits (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p156 Yellowstone National Park July visits as share of average annual visits, 2014-20 = **23.57** % (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p157 Yellowstone National Park average number of visits in September, 2014-2018 avera = **663,651** visits (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p158 Yellowstone National Park September visits as share of average annual visits, 20 = **16.51** % (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p159 Yellowstone National Park average number of visits in June, 2014-2018 average = **780,652** visits (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p160 Yellowstone National Park June visits as share of average annual visits, 2014-20 = **19.42** % (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p161 Yellowstone National Park average number of visits in May, 2014-2018 average = **401,449** visits (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p162 Yellowstone National Park May visits as share of average annual visits, 2014-201 = **9.99** % (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p163 Yellowstone National Park average number of visits in October, 2014-2018 average = **223,777** visits (2014-10-01..2018-10-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p164 Yellowstone National Park October visits as share of average annual visits, 2014 = **5.57** % (2014-10-01..2018-10-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p165 Yellowstone National Park average number of visits in April, 2014-2018 average = **44,027** visits (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p166 Yellowstone National Park average number of visits in January, 2014-2018 average = **28,837** visits (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p167 Yellowstone National Park average number of visits in February, 2014-2018 averag = **33,088** visits (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
- `https://doaj.org/article/a9a34a9eb7224f0a87d38d34da1d1b69` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visitation']: no matching market created on or before as_of markets=0


## Judge

### round 1

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

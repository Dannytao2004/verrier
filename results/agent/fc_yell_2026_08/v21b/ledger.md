# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions c | unit recreation visits | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [own_history] NPS historical monthly visitation statistics

Hypothesis: August recreation visits in recent years (2019, 2021, 2022, 2023, 2024, 2025) provide a baseline for the seasonal peak. The 2022 flood caused a sharp drop in June 2022 but August 2022 may have recovered. The 2025 value is the most recent August before the target. A simple projection using recent August levels and trend can estimate August 2026.

Queries issued by the searcher: Yellowstone National Park August 2025 visitation statistics recreation visits; NPS visitor use statistics Yellowstone monthly recreation visits 2024; Yellowstone visitation statistics August 2023 846,000 recreation visits; Yellowstone August 2022 visitation 838,000 recreation visits record

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p1 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024"
  - p2 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [keep: ] quote: "up 2% from August 2024 (868,259 recreation visits)"
  - p3 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p4 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of the 2021 annual record already carried by p40/p57/p134; adds no information.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p5 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [keep: ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024"
  - p6 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [keep: ] quote: "up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021"
  - p7 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [keep: ] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p8 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [keep: ] quote: "2023 - 3,308,924"
  - p9 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [keep: ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event."
  - p10 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [keep: ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/23037.htm` -> **snapshot** (snapshot 20260617061634); points raw/verified 15/15
  - p11 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [keep: ] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p12 Yellowstone National Park recreational visits, August 2022 = **582,211** recreational visits (2022-08-01..2022-08-31) [keep: ] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p13 Yellowstone National Park recreational visits, August 2019 = **820,006** recreational visits (2019-08-01..2019-08-31) [keep: ] quote: "and a 3% increase from August 2019* (820,006 recreational visits)."
  - p14 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Preliminary YTD-through-August 2023 vintage (3,313,244) superseded by the later NPS release (3,308,924, p8/p69).] quote: "So far in 2023, the park has hosted 3,313,244 recreation visits"
  - p15 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value.] quote: "up 36% from 2022 (2,437,607 recreation visits)"
  - p16 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [keep: ] quote: "and up 6% from 2019 (3,114,697 recreation visits)."
  - p17 Yellowstone National Park year-to-date recreation visits through August 2023 (li = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of the superseded 2023 YTD vintage p14.] quote: "2023 - 3,313,244"
  - p18 Yellowstone National Park year-to-date recreation visits through August 2022 (li = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21. Three entrances opened June 22.)"
  - p19 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of YTD-Aug 2021 value.] quote: "2021 - 3,590,609"
  - p20 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of YTD-Aug 2020 value.] quote: "2020 - 2,556,528 (The park was closed May 1 through May 17. Two entrances opened May 18 and the remaining three opened June 1.)"
  - p21 Yellowstone National Park year-to-date recreation visits through August 2019 (li = **3,114,697** recreation visits (2019-01-01..2019-08-31) [DISCARD: Duplicate of YTD-Aug 2019 value.] quote: "2019 - 3,114,697"
  - p22 Yellowstone National Park year-to-date recreation visits through August 2018 = **3,136,241** recreation visits (2018-01-01..2018-08-31) [keep: ] quote: "2018 - 3,136,241"
  - p23 Percent increase in Yellowstone August recreation visits, August 2023 vs August  = **45** % (2023-08-01..2023-08-31) [DISCARD: Derived percentage already implied by the level pair p11/p12; redundant.] quote: "This is a 45% increase from August 2022 (582,211 recreational visits)"
  - p24 Percent increase in Yellowstone August recreation visits, August 2023 vs August  = **3** % (2023-08-01..2023-08-31) [DISCARD: Derived percentage already implied by p11/p13; redundant.] quote: "and a 3% increase from August 2019* (820,006 recreational visits)."
  - p25 Percent increase in Yellowstone year-to-date recreation visits through August 20 = **36** % (2023-01-01..2023-08-31) [DISCARD: Derived percentage already implied by p14/p15; redundant.] quote: "the park has hosted 3,313,244 recreation visits, up 36% from 2022 (2,437,607 recreation visits)"
- `https://www.newsfromthestates.com/article/visits-yellowstone-national-park-tick-year-compared-last` -> **snapshot** (snapshot 20260707115703); points raw/verified 13/13
  - p26 Yellowstone National Park recreation visits, August 2024 = **871,163** recreation visits (2024-08-01..2024-08-31) [DISCARD: Preliminary August 2024 vintage (871,163) superseded by the later NPS release (868,259, p2/p63); mixing vintages would c] quote: "Yellowstone National Park hosted 871,163 recreation visits in August 2024, up 3% from August 2023 (846,389 recreation visits), the park said Wednesday in a news release."
  - p27 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [DISCARD: Duplicate of August 2023 value already carried by p11.] quote: "Yellowstone National Park hosted 871,163 recreation visits in August 2024, up 3% from August 2023 (846,389 recreation visits), the park said Wednesday in a news release."
  - p28 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "This August's visitation showed an 5% decrease from August 2021 (921,844 recreation visits)."
  - p29 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,497,254** recreation visits (2024-01-01..2024-08-31) [DISCARD: Preliminary YTD-through-August 2024 vintage (3,497,254) superseded by the later NPS release (3,494,350, p6/p67).] quote: "So far in 2024, the park has hosted 3,497,254 recreation visits, up 6% from 2023 (3,308,924 recreation visits), and down 3% from 2021 (3,590,609 recreation visits)."
  - p30 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of YTD-Aug 2023 value already carried by p8/p69/p89/p119.] quote: "So far in 2024, the park has hosted 3,497,254 recreation visits, up 6% from 2023 (3,308,924 recreation visits), and down 3% from 2021 (3,590,609 recreation visits)."
  - p31 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of YTD-Aug 2021 value already carried by p7/p19/p68/p88/p118.] quote: "So far in 2024, the park has hosted 3,497,254 recreation visits, up 6% from 2023 (3,308,924 recreation visits), and down 3% from 2021 (3,590,609 recreation visits)."
  - p32 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value already carried by p9/p15/p18/p70/p90/p120.] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p33 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of YTD-Aug 2020 value already carried by p10/p20/p71/p91/p121.] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
  - p34 Yellowstone National Park year-to-date recreation visits through August 2019 = **3,114,697** recreation visits (2019-01-01..2019-08-31) [DISCARD: Duplicate of YTD-Aug 2019 value already carried by p16/p21.] quote: "2019 - 3,114,697"
  - p35 Year-over-year change in Yellowstone August recreation visits, 2024 vs 2023 = **3** % (2024-08-01..2024-08-31) [DISCARD: Derived percentage already implied by p26/p27; redundant.] quote: "Yellowstone National Park hosted 871,163 recreation visits in August 2024, up 3% from August 2023 (846,389 recreation visits), the park said Wednesday in a news release."
  - p36 Change in Yellowstone August recreation visits, 2024 vs 2021 = **5** % (2024-08-01..2024-08-31) [DISCARD: Derived percentage already implied by p26/p28; redundant.] quote: "This August's visitation showed an 5% decrease from August 2021 (921,844 recreation visits)."
  - p37 Year-over-year change in Yellowstone year-to-date recreation visits through Augu = **6** % (2024-01-01..2024-08-31) [DISCARD: Derived percentage already implied by p29/p30; redundant.] quote: "So far in 2024, the park has hosted 3,497,254 recreation visits, up 6% from 2023 (3,308,924 recreation visits), and down 3% from 2021 (3,590,609 recreation visits)."
  - p38 Change in Yellowstone year-to-date recreation visits through August, 2024 vs 202 = **3** % (2024-01-01..2024-08-31) [DISCARD: Derived percentage already implied by p29/p31; redundant.] quote: "So far in 2024, the park has hosted 3,497,254 recreation visits, up 6% from 2023 (3,308,924 recreation visits), and down 3% from 2021 (3,590,609 recreation visits)."

### d2 [physical_flow] Entrance station counts and vehicle traffic

Hypothesis: Yellowstone has five entrances; total recreation visits can be approximated by summing vehicle entries and multiplying by average occupancy, plus pedestrian/bicycle entries. If monthly entrance counts or traffic volumes are available for August 2026 (even partial), they can be scaled to a full month.

Queries issued by the searcher: Yellowstone National Park vehicle entries August 2025 entrance counts; Yellowstone average vehicle occupancy summer visitors per vehicle; Yellowstone monthly visitation statistics August recreation visits 2025; Yellowstone traffic volume counts road counter report; Yellowstone visitation statistics July 2026 recreation visits NPS; Yellowstone "persons per vehicle" multiplier NPS visitor use reporting instructions

- `https://grizzlyrv.com/which-yellowstone-entrance-should-rvers-stay-near/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://powelltribune.com/stories/yellowstone-2025-attendance-is-second-highest,173812` -> **snapshot** (snapshot 20260321074542); points raw/verified 15/11
  - p39 Yellowstone National Park total recreation visits in 2025 = **4,762,988** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "Yellowstone National Park welcomed 4,762,988 recreation visits in 2025."
  - p40 Yellowstone National Park record recreation visits in 2021 = **4,860,242** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "The number is just shy of the 2021 record of 4,860,242"
  - p41 Yellowstone National Park total recreation visits in 2024 = **4,744,363** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "about 20,000 visits higher than last year's total of 4,744,363"
  - p42 Yellowstone National Park visitor hours spent in park in 2025 = **86,891,452** hours (2025-01-01..2025-12-31) [DISCARD: Visitor-hours total with no August or 2026 counterpart; no conversion to visits available.] quote: "The park also reported visitors spent 86,891,452 hours in the park"
  - p43 Yellowstone National Park overnight stays in 2025 = **1,238,983** overnight stays (2025-01-01..2025-12-31) [DISCARD: Overnight-stay total with no August or 2026 counterpart; day visits dominate and no bridge exists.] quote: "along with 1,238,983 overnight stays"
  - p44 Share of Yellowstone 2025 visits occurring between May and August = **75** percent of all visits (2025-05-01..2025-08-31) [keep: ] quote: "More than 75% of all visits in 2025 happened between May and August."
  - p45 Yellowstone East Entrance visits in 2025 = **167,500** visits (2025-01-01..2025-12-31) [DISCARD: Single-entrance annual count with no August-specific or 2026 counterpart; cannot be converted to the target.] quote: "Just under 167,500 came through the entrance last year."
  - p46 Yellowstone West Entrance visits in 2025 = **778,075** visits (2025-01-01..2025-12-31) [DISCARD: Single-entrance annual count; no August/2026 counterpart.] quote: "The West Entrance had the most visits, with 778,075."
  - p47 Yellowstone North Entrance visits in 2025 = **561,290** visits (2025-01-01..2025-12-31) [DISCARD: Single-entrance annual count; no August/2026 counterpart.] quote: "The North Entrance was the second busiest with 561,290"
  - p48 Yellowstone South Entrance visits in 2025 = **291,693** visits (2025-01-01..2025-12-31) [DISCARD: Single-entrance annual count; no August/2026 counterpart.] quote: "the South Entrance was third with 291,693"
  - p49 Yellowstone Northeast Entrance visits in 2025 = **136,768** visits (2025-01-01..2025-12-31) [DISCARD: Single-entrance annual count; no August/2026 counterpart.] quote: "The Northeast Entrance had the lowest attendance with 136,768."
- `https://NPS.gov:443/yell/getinvolved/upload/YELL_Phase-2-Traffic-Parking-Analysis_508-reduced.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- dropped by code checks: 4 (number: no number in value_as_written: 1; period_end missing or unparseable: 3)

### d3 [shocks] Closures, weather, and policy changes

Hypothesis: Any major closures (e.g., road construction, flood damage, government shutdown) or unusual weather in August 2026 could significantly alter visitation. The 2022 flood caused a temporary drop; similar events in 2026 would need to be accounted for.

Queries issued by the searcher: Yellowstone closure August 2026; Yellowstone road construction 2026 closures; Yellowstone visitation August 2026 record visitors NPS; Yellowstone National Park July 2026 closure road flooding

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 15/5
  - p50 Yellowstone road improvement project along road between Canyon Village and West  = **10** minutes (2026-07-01..2026-08-14) [keep: ] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p51 Yellowstone road improvement project along road between Canyon Village and West  = **7** a.m. (2026-07-01..2026-08-14) [keep: ] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p52 Yellowstone road improvement project along road between Canyon Village and West  = **6** p.m. (2026-07-01..2026-08-14) [keep: ] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p53 Yellowstone road improvement project along road between Canyon Village and West  = **10** minutes (2026-07-01..2026-08-14) [keep: ] quote: "One lane will be closed while crews work; traffic lights will operate in 10-minute increments."
  - p54 Yellowstone road improvement project in Old Faithful area: maximum traffic delay = **15** minutes (2026-07-15..2026-08-15) [keep: ] quote: "expect up to 15-minute delays from mid-July through mid-August."
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 15/7
  - p55 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p56 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p57 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p58 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Grand Teton annual total; regional analogue only, no August or 2026 signal to transfer.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p59 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Grand Teton annual total; no transferable August/2026 signal.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p60 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Grand Teton annual total; no transferable August/2026 signal.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p61 Year of historic flooding that devastated North Entrance Road, Yellowstone = **2,022** year (2022-01-01..2022-12-31) [DISCARD: Year-of-flood metadata (2022) is not a numeric visitation input.] quote: "The National Park Service is mulling new permanent routes to replace the North Entrance Road, which was devastated by 2022 historic flooding."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 18 (period_end 2026-10-31 after as_of: 3; number: no number in value_as_written: 3; period_end missing or unparseable: 6; number: more than one number in value_as_written: 1; period_end 2026-09-30 after as_of: 1; period_end 2026-09-15 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-09-07 after as_of: 1; value_as_written not in quote as a whole number: 1)

### d4 [base_rates] Seasonal share of annual visitation

Hypothesis: August typically accounts for a stable share of Yellowstone's annual recreation visits (e.g., around 20-25%). If a reliable estimate of total 2026 annual visits is available (or can be projected from year-to-date data), multiplying by the August share yields the target.

Queries issued by the searcher: Yellowstone annual visitation 2025 recreation visits record; Yellowstone year to date visitation 2026 through July; Yellowstone August 2025 recreation visits monthly statistics; Yellowstone National Park 2024 annual recreation visits 4,744,354

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p62 Yellowstone National Park recreation visits in August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of August 2025 value (p1).] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p63 Yellowstone National Park recreation visits in August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of August 2024 value (p2).] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p64 Yellowstone National Park recreation visits in August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of August 2021 value (p3).] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p65 Yellowstone National Park record-breaking annual recreation visits in 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record (p40/p57/p134).] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p66 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of YTD-Aug 2025 value (p5).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p67 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of YTD-Aug 2024 value (p6).] quote: "up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p68 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of YTD-Aug 2021 value (p7).] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p69 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of YTD-Aug 2023 value (p8).] quote: "2023 - 3,308,924"
  - p70 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value (p9).] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p71 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of YTD-Aug 2020 value (p10).] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p72 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p73 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [keep: ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p74 Yellowstone National Park recreation visits, July 2021 = **1,080,767** recreation visits (2021-07-01..2021-07-31) [keep: ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p75 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p76 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p77 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p78 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [keep: ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p79 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [keep: ] quote: "2024 - 2,626,091"
  - p80 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [keep: ] quote: "2023 - 2,462,535"
  - p81 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [keep: ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] NPS park-level monthly data for other large western parks

Hypothesis: Visitation trends at comparable parks (e.g., Grand Teton, Glacier, Zion, Yosemite) may correlate with Yellowstone's August visitation, especially if regional travel patterns are similar. A ratio of Yellowstone August visits to a composite of these parks in past years can be applied to their 2026 August data if available.

Queries issued by the searcher: Grand Teton National Park August 2025 visitation statistics; NPS Visitor Use Statistics monthly visitation 2026 July Yellowstone Grand Teton Glacier; Yellowstone August 2025 recreation visits record 2024; Yosemite National Park August 2025 visitation statistics

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p82 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of August 2025 value (p1).] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p83 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of August 2024 value (p2).] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p84 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of August 2021 value (p3).] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p85 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p86 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of YTD-Aug 2025 value (p5).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p87 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of YTD-Aug 2024 value (p6).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p88 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of YTD-Aug 2021 value (p7).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p89 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of YTD-Aug 2023 value (p8).] quote: "2023 - 3,308,924"
  - p90 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value (p9).] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p91 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of YTD-Aug 2020 value (p10).] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p92 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 value (p72).] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p93 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [DISCARD: Duplicate of July 2025 value (p73).] quote: "down 2% from July 2025 (975,109 recreation visits)."
  - p94 Yellowstone National Park recreation visits, July 2021 = **1,080,767** recreation visits (2021-07-01..2021-07-31) [DISCARD: Duplicate of July 2021 value (p74).] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p95 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [DISCARD: Duplicate of YTD-July 2026 value (p76).] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits)"
  - p96 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [DISCARD: Duplicate of YTD-July 2025 value (p77).] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p97 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Duplicate of YTD-July 2021 value (p78).] quote: "and down 1% from 2021 (2,668,765 recreation visits)."
  - p98 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [DISCARD: Duplicate of YTD-July 2024 value (p79).] quote: "2024 - 2,626,091"
  - p99 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [DISCARD: Duplicate of YTD-July 2023 value (p80).] quote: "2023 - 2,462,535"
  - p100 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Duplicate of YTD-July 2022 value (p81).] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
  - p101 Yellowstone National Park record-breaking year total recreation visits (2021) = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
- `https://buckrail.com/year-to-date-visitation-in-grand-teton-nearly-identical-to-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=2572a2e6-34ee-40e7-af08-a177fe35eebe&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [capacity_consumption] Lodging and campground occupancy

Hypothesis: Overnight stays in Yellowstone (lodges, campgrounds) are a component of visitation. Total recreation visits correlate with overnight stays, but day visits dominate. If occupancy rates and room/campsite counts are available for August 2026, they can help estimate overnight visitors, which can be combined with day-use estimates.

Queries issued by the searcher: Yellowstone lodging occupancy August 2025 Xanterra overnight stays; Yellowstone National Park monthly visitation statistics August 2025 overnight stays; Yellowstone visitation statistics July 2026 recreation visits; Xanterra Yellowstone National Park Lodges 2026 occupancy bookings summer

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p102 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 value (p72).] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025"
  - p103 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [DISCARD: Duplicate of July 2025 value (p73).] quote: "down 2% from July 2025 (975,109 recreation visits)"
  - p104 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [DISCARD: Duplicate of July 2021 value (p74).] quote: "an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year"
  - p105 Yellowstone National Park total recreation visits in record-breaking year 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "record-breaking year with over 4.8 million recreation visits and the busiest July on record"
  - p106 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [DISCARD: Duplicate of YTD-July 2026 value (p76).] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025"
  - p107 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [DISCARD: Duplicate of YTD-July 2025 value (p77).] quote: "down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021"
  - p108 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Duplicate of YTD-July 2021 value (p78).] quote: "down 1% from 2021 (2,668,765 recreation visits)"
  - p109 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [DISCARD: Duplicate of YTD-July 2024 value (p79).] quote: "2024 - 2,626,091"
  - p110 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [DISCARD: Duplicate of YTD-July 2023 value (p80).] quote: "2023 - 2,462,535"
  - p111 Yellowstone National Park year-to-date recreation visits through July 2022 (floo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Duplicate of YTD-July 2022 value (p81).] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p112 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [DISCARD: Duplicate of August 2025 value (p1).] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p113 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [DISCARD: Duplicate of August 2024 value (p2).] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p114 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [DISCARD: Duplicate of August 2021 value (p3).] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p115 Yellowstone National Park record-breaking year recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p116 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [DISCARD: Duplicate of YTD-Aug 2025 value (p5).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p117 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [DISCARD: Duplicate of YTD-Aug 2024 value (p6).] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p118 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of YTD-Aug 2021 value (p7).] quote: "and down 1% from 2021 (3,590,609 recreation visits)."
  - p119 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of YTD-Aug 2023 value (p8).] quote: "2023 - 3,308,924"
  - p120 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of YTD-Aug 2022 value (p9).] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p121 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of YTD-Aug 2020 value (p10).] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://powelltribune.com/stories/region-continues-to-buck-downward-trend-of-tourism,170327` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Tourism forecasts and industry outlook

Hypothesis: National or regional tourism forecasts for summer 2026 may indicate whether travel to national parks is up or down. If a forecast for Yellowstone specifically exists, it can be used directly.

Queries issued by the searcher: Yellowstone visitation forecast 2026; national park tourism forecast summer 2026; Yellowstone recreation visits June 2026 NPS visitation statistics; Yellowstone August 2026 visitation record

- `https://www.nps.gov/yell/learn/news/26016.htm` -> **snapshot** (snapshot 20260714213711); points raw/verified 10/10
  - p122 Yellowstone National Park recreation visits, June 2026 = **903,025** recreation visits (2026-06-01..2026-06-30) [keep: ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p123 Yellowstone National Park recreation visits, June 2025 = **928,250** recreation visits (2025-06-01..2025-06-30) [keep: ] quote: "down 3% from June 2025 (928,250 recreation visits)."
  - p124 Yellowstone National Park recreation visits, June 2021 = **938,845** recreation visits (2021-06-01..2021-06-30) [keep: ] quote: "Visitation in June 2026 showed a 4% decrease from June 2021 (938,845 recreation visits)."
  - p125 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Rounded duplicate of 2021 annual record.] quote: "The park's record-breaking year was 2021 with over 4.8 million recreation visits."
  - p126 Yellowstone National Park year-to-date recreation visits through June 2026 = **1,676,678** recreation visits (2026-01-01..2026-06-30) [keep: ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p127 Yellowstone National Park year-to-date recreation visits through June 2025 = **1,690,922** recreation visits (2025-01-01..2025-06-30) [keep: ] quote: "down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p128 Yellowstone National Park year-to-date recreation visits through June 2021 = **1,587,998** recreation visits (2021-01-01..2021-06-30) [keep: ] quote: "and up 6% from 2021 (1,587,998 recreation visits)."
  - p129 Yellowstone National Park year-to-date recreation visits through June 2024 = **1,633,739** recreation visits (2024-01-01..2024-06-30) [keep: ] quote: "2024 - 1,633,739"
  - p130 Yellowstone National Park year-to-date recreation visits through June 2023 = **1,492,843** recreation visits (2023-01-01..2023-06-30) [keep: ] quote: "2023 - 1,492,843"
  - p131 Yellowstone National Park year-to-date recreation visits through June 2022 = **1,258,834** recreation visits (2022-01-01..2022-06-30) [keep: ] quote: "2022 - 1,258,834 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 15/8
  - p132 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Duplicate of 2025 annual total (p39/p55).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p133 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Duplicate of 2024 annual total (p41/p56).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p134 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate of 2021 annual total (p40/p57).] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p135 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Duplicate Grand Teton 2025 total.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p136 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Duplicate Grand Teton 2024 total.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p137 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Duplicate Grand Teton 2021 total.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p138 Year of hydrothermal explosion at Biscuit Basin, Yellowstone = **2,024** year (2024-01-01..2024-12-31) [DISCARD: Year-of-hydrothermal-explosion metadata (2024) is not a numeric visitation input.] quote: "Biscuit Basin was the site of a 2024 hydrothermal explosion that tossed boiling water and rocks skyward"
  - p139 Year of historic flooding that devastated Yellowstone North Entrance Road = **2,022** year (2022-01-01..2022-12-31) [DISCARD: Duplicate year-of-flood metadata.] quote: "The National Park Service is mulling new permanent routes to replace the North Entrance Road, which was devastated by 2022 historic flooding."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (period_end missing or unparseable: 2; period_end 2026-09-07 after as_of: 1; number: no number in value_as_written: 2; number: more than one number in value_as_written: 1; period_end 2029-12-31 after as_of: 1)

### d8 [attention] Search and social media interest

Hypothesis: Google Trends or social media mentions for Yellowstone may correlate with visitation, but the relationship is noisy. If a strong correlation is established historically, current attention levels could indicate whether August 2026 is above or below trend.

Queries issued by the searcher: Google Trends Yellowstone National Park search interest visitation correlation; Yellowstone National Park monthly visitation statistics 2025 August recreation visits; Google Trends predicts national park visitation study search volume data monthly visitors; Yellowstone visitation statistics July 2026 recreation visits

- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p140 Yellowstone Google search margin over Grand Canyon National Park, July 2025 to J = **1,420,000** searches (2025-07-01..2026-06-30) [DISCARD: Google-search margin is a noisy attention proxy with no established park-specific conversion to August recreation visits] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sciencedirect.com/science/article/abs/pii/S0301479719306048` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://businessupturn.com/usa/lifestyle/travel/most-searched-national-park-every-state-2026-yellowstone/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [own_history] NPS monthly visitation release for August 2026 (or a partial-month/entrance-count release) published after the cutoff

Hypothesis: The single most valuable missing input: an actual August 2026 NPS figure or entrance-counter total would replace the projection entirely and resolve the ~2-3% YoY drift uncertainty. It would directly anchor m1/m2/m3.

Queries issued by the searcher: Yellowstone National Park August 2026 visitation statistics NPS; Yellowstone recreation visits August 2025 NPS visitor use statistics; Yellowstone visitation statistics July 2026 news release; Yellowstone National Park visitation July 2026 NPS recreation visits

- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.pl/aktualno%C5%9Bci/artyku%C5%82/63ykvnvt60ul/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-visitation-down-in-august` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] August share of annual visits and the July-to-August ratio in recent years

Hypothesis: A stable July/August ratio (e.g., August ~90-92% of July) would let the observed July 2026 value (p72) be converted directly into an August 2026 estimate, completing the d4 route with a park-specific coefficient rather than a generic assumption.

Queries issued by the searcher: Yellowstone monthly visitation July August ratio NPS Visitor Use Statistics 2018-2025; Yellowstone National Park monthly recreation visits August 2025 July 2025 NPS; Yellowstone visitation statistics July 2022 2020 2019 recreation visits August monthly; irma.nps.gov Yellowstone summary visitor use by month and year recreation visitors July August

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 14/14
  - p141 Yellowstone National Park average July visits, 2014-2018 = **947,688** visits (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p142 Yellowstone National Park average August visits, 2014-2018 = **839,787** visits (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
  - p143 Yellowstone National Park average June visits, 2014-2018 = **780,652** visits (2014-06-01..2018-06-30) [keep: ] quote: "\| June \| 780,652 \| 19.42% \|"
  - p144 Yellowstone National Park average September visits, 2014-2018 = **663,651** visits (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p145 Yellowstone National Park average May visits, 2014-2018 = **401,449** visits (2014-05-01..2018-05-31) [keep: ] quote: "\| May \| 401,449 \| 9.99% \|"
  - p146 Yellowstone National Park average October visits, 2014-2018 = **223,777** visits (2014-10-01..2018-10-31) [keep: ] quote: "\| October \| 223,777 \| 5.57% \|"
  - p147 Yellowstone National Park average April visits, 2014-2018 = **44,027** visits (2014-04-01..2018-04-30) [keep: ] quote: "\| April \| 44,027 \| 1.10% \|"
  - p148 Yellowstone National Park average February visits, 2014-2018 = **33,088** visits (2014-02-01..2018-02-28) [keep: ] quote: "\| February \| 33,088 \| 0.82% \|"
  - p149 Yellowstone National Park average January visits, 2014-2018 = **28,837** visits (2014-01-01..2018-01-31) [keep: ] quote: "\| January \| 28,837 \| 0.72% \|"
  - p150 Yellowstone National Park average March visits, 2014-2018 = **22,266** visits (2014-03-01..2018-03-31) [keep: ] quote: "\| March \| 22,266 \| 0.55% \|"
  - p151 Yellowstone National Park average December visits, 2014-2018 = **20,434** visits (2014-12-01..2018-12-31) [keep: ] quote: "\| December \| 20,434 \| 0.51% \|"
  - p152 Yellowstone National Park average November visits, 2014-2018 = **14,323** visits (2014-11-01..2018-11-30) [keep: ] quote: "\| November \| 14,323 \| 0.36% \|"
  - p153 Yellowstone National Park July share of average annual visits, 2014-2018 = **23.57** % (2014-07-01..2018-07-31) [keep: ] quote: "\| July \| 947,688 \| 23.57% \|"
  - p154 Yellowstone National Park August share of average annual visits, 2014-2018 = **20.89** % (2014-08-01..2018-08-31) [keep: ] quote: "\| August \| 839,787 \| 20.89% \|"
- `https://www.wyomingpublicmedia.org/news/2025-09-09/yellowstone-is-on-track-for-its-second-busiest-year` -> **snapshot** (snapshot 20251016213459); points raw/verified 6/0
- `https://yellowstonenotebooknews.blogspot.com/search/label/visitation%20statistics` -> **snapshot** (snapshot 20231224073643); points raw/verified 15/15
  - p155 Yellowstone National Park recreation visits, July 2023 = **969,692** recreation visits (2023-07-01..2023-07-31) [DISCARD: July 2023 value (969,692) is a different calendar month from the target and is not needed for the August projection.] quote: "Yellowstone National Park hosted 969,692 recreation visits in July 2023."
  - p156 Yellowstone National Park recreation visits, August 2023 = **846,389** recreation visits (2023-08-01..2023-08-31) [keep: ] quote: "Yellowstone National Park hosted 846,389 recreation visits in August 2023."
  - p157 Yellowstone National Park recreation visits, July 2022 = **596,562** recreation visits (2022-07-01..2022-07-31) [DISCARD: July 2022 value (596,562) is a different calendar month and is not needed.] quote: "a 63% increase from July 2022 (596,562 recreational visits)"
  - p158 Yellowstone National Park recreation visits, August 2022 = **582,211** recreation visits (2022-08-01..2022-08-31) [keep: ] quote: "Yellowstone National Park hosted 582,211 recreation visits in August 2022."
  - p159 Yellowstone National Park recreation visits, July 2019 = **936,062** recreation visits (2019-07-01..2019-07-31) [DISCARD: July 2019 value (936,062) is a different calendar month and is not needed.] quote: "a 4% increase from July 2019* (936,062 recreation visits)"
  - p160 Yellowstone National Park recreation visits, August 2019 = **820,006** recreation visits (2019-08-01..2019-08-31) [keep: ] quote: "a 3% increase from August 2019* (820,006 recreational visits)"
  - p161 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "a 37% decrease from August 2021 (921,844 recreational visits), the most-visited August on record"
  - p162 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [DISCARD: Duplicate of p78/p97/p108 (YTD-through-July 2021).] quote: "2021 - 2,668,765"
  - p163 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [DISCARD: Duplicate of p7/p19/p31/p68/p88/p118 (YTD-through-August 2021).] quote: "2021 - 3,590,609"
  - p164 Yellowstone National Park year-to-date recreation visits through July 2020 = **1,674,699** recreation visits (2020-01-01..2020-07-31) [DISCARD: YTD-through-July 2020 is a different period and is not needed for the August projection.] quote: "2020 - 1,674,699"
  - p165 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [DISCARD: Duplicate of p10/p20/p33/p71/p91/p121 (YTD-through-August 2020).] quote: "2020 - 2,556,528"
  - p166 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [DISCARD: Duplicate of p81/p100/p111 (YTD-through-July 2022).] quote: "2022 - 1,855,396"
  - p167 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [DISCARD: Duplicate of p9/p15/p18/p32/p70/p90/p120 (YTD-through-August 2022).] quote: "2022 - 2,437,607"
  - p168 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,463,202** recreation visits (2023-01-01..2023-07-31) [DISCARD: YTD-through-July 2023 (2,463,202) conflicts with the later NPS value (2,462,535, p80/p99/p110); superseded vintage.] quote: "2023 - 2,463,202"
  - p169 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,313,244** recreation visits (2023-01-01..2023-08-31) [DISCARD: Duplicate of the superseded 2023 YTD vintage p14.] quote: "2023 - 3,313,244"
- dropped by code checks: 6 (period_end missing or unparseable: 6)

### b3 [shocks] Any August 2026-specific disruption (fire, smoke, road closure, shutdown, reservation policy)

Hypothesis: The construction notices (p50-p54) end mid-August; a larger unobserved shock (wildfire smoke, full road closure, timed-entry policy) would invalidate the trend-based methods and is the largest single uncertainty in the projection.

Queries issued by the searcher: Yellowstone August 2026 road closure alert; Yellowstone wildfire smoke August 2026; Yellowstone timed entry 2026 reservation policy; Yellowstone National Park construction notices August 2026

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 16/7
  - p170 Yellowstone West Entrance to Madison road projected open period start date, 2026 = **17** date (day of month) (2026-04-17..2026-04-17) [keep: ] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris"
  - p171 Yellowstone East Entrance to Fishing Bridge (Sylvan Pass) projected open period  = **1** date (day of month) (2026-05-01..2026-05-01) [keep: ] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p172 Yellowstone South Entrance to West Thumb projected open period start date, 2026 = **8** date (day of month) (2026-05-08..2026-05-08) [keep: ] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass)"
  - p173 Yellowstone Canyon Village to Tower Fall (Dunraven Pass) projected open period s = **22** date (day of month) (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Canyon Village to Tower Fall (Dunraven Pass)."
  - p174 Beartooth Highway (US-212) and Chief Joseph Scenic Byway (WY-296) projected open = **22** date (day of month) (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Beartooth Highway (US-212), Chief Joseph Scenic Byway (WY-296)."
  - p175 Minimum traffic delay from fiber project along road between Canyon Village and W = **10** minutes (2026-07-01..2026-08-14) [keep: ] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p176 Maximum traffic delay from construction in Old Faithful area, mid-July through m = **15** minutes (2026-07-15..2026-08-15) [keep: ] quote: "expect up to 15-minute delays from mid-July through mid-August."
- `https://www.nps.gov/yell/learn/news/26009.htm` -> **snapshot** (snapshot 20260812105204); points raw/verified 6/0
- `https://tgftp.nws.noaa.gov/data/raw/ae/aeus75.kriw.aqa.riw.txt` -> **snapshot** (snapshot 20260124033813); points raw/verified 4/4
  - p177 Air Quality Alert for Wildfire Smoke in Yellowstone National Park and western Wy = **1** time of day (MDT) (2025-09-05..2025-09-05) [DISCARD: September 2025 wildfire-smoke air-quality alert is outside the target month and provides no quantitative August 2026 sig] quote: "* WHEN...1 PM Friday, September 5, until 1 PM Sunday, September 7."
  - p178 Air Quality Alert for Wildfire Smoke in Yellowstone National Park and western Wy = **1** time of day (MDT) (2025-09-07..2025-09-07) [DISCARD: Same September 2025 air-quality alert; outside target period.] quote: "* WHEN...1 PM Friday, September 5, until 1 PM Sunday, September 7."
  - p179 Air Quality Alert message issue time (MDT) for Yellowstone National Park and wes = **1,102** time of day (MDT) (2025-09-05..2025-09-05) [DISCARD: Issue time of the September 2025 alert; not a visitation input.] quote: "1102 AM MDT Fri Sep 5 2025"
  - p180 Air Quality Alert message issue time (UTC) for Yellowstone National Park and wes = **51,702** UTC timestamp (DDHHMM) (2025-09-05..2025-09-05) [DISCARD: UTC issue time of the September 2025 alert; not a visitation input.] quote: "AEUS75 KRIW 051702"
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end 2026-10-31 after as_of: 2; period_end 2026-10-12 after as_of: 2; number: no number in value_as_written: 2; period_end 2026-09-07 after as_of: 1; period_end 2026-09-15 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-08-31 after as_of: 1; period_end missing or unparseable: 5)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p62', 'p82', 'p112'] All four are the same NPS August 2025 figure (881,936) repeated across snapshots; they are one measurement, not four independent confirmations.
- corroborating: ['p2', 'p63', 'p83', 'p113'] Same NPS August 2024 value (868,259) repeated; single underlying measurement.
- corroborating: ['p3', 'p28', 'p64', 'p84', 'p114'] Same NPS August 2021 value (921,844) repeated across snapshots.
- corroborating: ['p11', 'p27'] August 2023 = 846,389 in both the NPS release and the news republication; same source figure.
- conflicting: ['p2', 'p26'] Two different August 2024 values: 868,259 (NPS release, later snapshot) vs 871,163 (news report). Likely a revision or transcription difference; the NPS-published 868,259 is the more authoritative vin
- corroborating: ['p5', 'p66', 'p86', 'p116'] Same YTD-through-August 2025 total (3,547,967) repeated.
- conflicting: ['p6', 'p67', 'p87', 'p117'] YTD-through-August 2024 appears as 3,494,350 (NPS) and 3,497,254 (news); a small revision/rounding difference, same underlying series.
- conflicting: ['p8', 'p14', 'p17', 'p30', 'p69', 'p89', 'p119'] YTD-through-August 2023 appears as 3,308,924 and 3,313,244; minor revision difference within the same NPS series.
- corroborating: ['p39', 'p55', 'p132'] 2025 annual total ~4.76 million reported consistently (4,762,988 exact vs 4.76M rounded).
- corroborating: ['p40', 'p57', 'p134'] 2021 annual record ~4.86 million reported consistently.
- corroborating: ['p41', 'p56', 'p133'] 2024 annual total ~4.74 million reported consistently.
- corroborating: ['p72', 'p92', 'p102'] Same July 2026 value (958,706) repeated; single NPS measurement.
- corroborating: ['p73', 'p93', 'p103'] Same July 2025 value (975,109) repeated.
- corroborating: ['p76', 'p95', 'p106'] Same YTD-through-July 2026 value (2,635,384) repeated.
- corroborating: ['p77', 'p96', 'p107'] Same YTD-through-July 2025 value (2,666,031) repeated.
- corroborating: ['p122', 'p123', 'p124'] June 2026/2025/2021 monthly values from one NPS release; internally consistent and show 2026 running ~1-3% below 2025.
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p54'] Construction-delay notices for summer 2026; together they indicate modest, localized delays ending mid-August, a mild negative or neutral factor on August 2026 visitation.
- corroborating: ['p44', 'p39'] May-August share (>75%) and 2025 annual total are from the same article and jointly bound the seasonal concentration of visits.
- corroborating: ['p58', 'p59', 'p60', 'p135', 'p136', 'p137'] Grand Teton annual series (2021/2024/2025) repeated; useful only as a regional analogue, not a direct input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p62', 'p82', 'p112'] All four are the same NPS August 2025 recreation-visit figure (881,936) repeated across snapshots; they are one underlying measurement, not independent confirmation.
- corroborating: ['p2', 'p63', 'p83', 'p113'] Same NPS August 2024 figure (868,259) repeated; one measurement.
- corroborating: ['p3', 'p28', 'p64', 'p84', 'p114', 'p161'] Same NPS August 2021 figure (921,844) repeated; one measurement.
- corroborating: ['p11', 'p27', 'p156'] Same NPS August 2023 figure (846,389) repeated.
- corroborating: ['p12', 'p158'] Same NPS August 2022 figure (582,211) repeated.
- corroborating: ['p13', 'p160'] Same NPS August 2019 figure (820,006) repeated.
- conflicting: ['p26', 'p2'] Two different August 2024 values: 871,163 (newsfromthestates, 2024-09-11) vs 868,259 (NPS, 2025-09-04). The later NPS release is the revised official figure; the earlier news value is a preliminary vi
- corroborating: ['p5', 'p66', 'p86', 'p116'] Same NPS YTD-through-August 2025 figure (3,547,967) repeated.
- corroborating: ['p6', 'p67', 'p87', 'p117'] Same NPS YTD-through-August 2024 figure (3,494,350) repeated.
- conflicting: ['p29', 'p6'] YTD-through-August 2024 is 3,497,254 in the 2024 news vintage vs 3,494,350 in the later NPS release; a revision, not two independent measurements.
- corroborating: ['p8', 'p30', 'p69', 'p89', 'p119'] Same NPS YTD-through-August 2023 figure (3,308,924) repeated.
- conflicting: ['p14', 'p17', 'p169'] YTD-through-August 2023 appears as 3,313,244 in the 2023 vintage and 3,308,924 in later vintages; a revision.
- corroborating: ['p39', 'p55', 'p132'] Annual 2025 recreation visits reported as 4,762,988 (precise) and 4.76 million (rounded); same underlying NPS total.
- corroborating: ['p41', 'p56', 'p133'] Annual 2024 recreation visits reported as 4,744,363 and 4.74 million; same underlying total.
- corroborating: ['p40', 'p57', 'p134'] Annual 2021 recreation visits reported as 4,860,242 and 4.86 million; same underlying total.
- corroborating: ['p72', 'p92', 'p102'] Same NPS July 2026 figure (958,706) repeated.
- corroborating: ['p73', 'p93', 'p103'] Same NPS July 2025 figure (975,109) repeated.
- corroborating: ['p76', 'p95', 'p106'] Same NPS YTD-through-July 2026 figure (2,635,384) repeated.
- corroborating: ['p77', 'p96', 'p107'] Same NPS YTD-through-July 2025 figure (2,666,031) repeated.
- corroborating: ['p141', 'p142', 'p153', 'p154'] 2014-2018 monthly averages and shares from the same NPS table; internally consistent and useful for the July-to-August ratio.
- corroborating: ['p50', 'p51', 'p52', 'p53', 'p175'] Same 2026 Canyon-to-West-Thumb construction delay notice repeated; describes a modest delay ending August 14, 2026.
- corroborating: ['p54', 'p176'] Same Old Faithful-area construction delay notice repeated; ends mid-August 2026.
- corroborating: ['p170', 'p171', 'p172', 'p173', 'p174'] 2026 road-opening schedule shows all main park roads open through August, so no access closure is indicated.
- corroborating: ['p122', 'p123', 'p124'] June 2026 NPS release: June 2026 (903,025) down 3% from June 2025 (928,250) and down 4% from June 2021 (938,845); consistent with a mild 2026 softness.
- corroborating: ['p72', 'p73', 'p74'] July 2026 NPS release: July 2026 (958,706) down 2% from July 2025 (975,109) and down 11% from July 2021 (1,080,767); consistent with a mild 2026 softness.
- corroborating: ['p76', 'p77', 'p78'] YTD-through-July 2026 (2,635,384) down 1% from 2025 (2,666,031) and down 1% from 2021 (2,668,765); consistent with a mild 2026 softness.
- corroborating: ['p140'] Google-search attention margin for Yellowstone over Grand Canyon is a weak contextual signal of continued high interest; not a visitation measurement.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 recreation visits as a fraction of July 2026 recreation visits | 0.886 | 0.82..0.95 | 0.6241..1.248 (widened) | ratio | m1 (m1) | Park-specific July-to-August ratio. From the 2014-2018 NPS monthly averages (p141, p142), August/July = 839,787/947,688 = 0.886. Recent years are consistent: 2025 881,936/975,109 = 0.904; 2024 868,259/975,109-like July 2024 is not directly available, but 2023 846,389/969,692 = 0.873; 2021 921,844/1, | August 2026 has no major access closure or demand shock relative to July 2026, and the park's seasonal July-to-August pattern remains similar to 2014-2025. | Evidence of a major August 2026 closure, wildfire smoke event, or policy change that materially shifts August relative to July; or an observed August 2026 value far outside the ratio range. |
| a2 | August 2026 recreation visits as a fraction of August 2025 recreation visits | 0.98 | 0.93..1.03 | 0.6921..1.384 (widened) | ratio | m2 (m2) | Recent 2026 monthly NPS releases show mild softness versus 2025: June 2026 down 3% (p122), July 2026 down 2% (p72), YTD through July 2026 down 1% (p76). A near-flat August 2026 versus August 2025 is the central case, with uncertainty spanning roughly -7% to +3%. | The mild 2026 softness seen in June and July continues into August, with no new shock. | A major August 2026 shock (closure, smoke, policy) or a sharp reversal in the 2026 trend. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 843,961 | ['p72'] / ['a1'] | [] |  | 0.33 | median_of_backtested |  |
| m2 | formula_mc | 865,116 | ['p1'] / ['a2'] | [] |  | 0.33 | median_of_backtested |  |
| m3 | series_naive | 875,098 |  | [2024, 2025] | 0.035 | 0.33 | backtest |  |

Result: central **861,293**, 80% interval [823,138, 901,217], basis historical_errors, weight rule inverse_backtest_error, weight on methods that use assumptions 0.67

## Final answer

The best estimate for recreation visits to Yellowstone National Park during August 2026, as reported in NPS monthly visitation statistics, is 861,293 visits, with an 80% interval of 823,138 to 901,217 (historical errors). The combination draws on 3 methods: a July-to-August ratio applied to observed July 2026 (843,961, weight 33%), a year-over-year change from observed August 2025 (865,116, weight 33%), and a naive recent-August average (875,098, weight 33%). Observed inputs are the July 2026 and August 2025 NPS figures; the ratio 0.886 (range 0.6241 to 1.248) and change factor 0.98 (range 0.6921 to 1.384) are analyst assumptions, not measurements. The interval is model-based and conditional on those assumptions, not a demonstrated accuracy guarantee. The main risk is an August-specific shock or a trend change not captured by June-July data. The most useful missing evidence would be partial August 2026 counts or park-level daily entry data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 recreation visits as a fraction of July 2026 recreation visits: 0.886 ratio, range 0.6241 to 1.248 (range widened by code); used by m1. Overturned by: Evidence of a major August 2026 closure, wildfire smoke event, or policy change that materially shifts August relative to July; or an observed August 2026 value far outside the ratio range.
- a2 August 2026 recreation visits as a fraction of August 2025 recreation visits: 0.98 ratio, range 0.6921 to 1.384 (range widened by code); used by m2. Overturned by: A major August 2026 shock (closure, smoke, policy) or a sharp reversal in the [n] trend.

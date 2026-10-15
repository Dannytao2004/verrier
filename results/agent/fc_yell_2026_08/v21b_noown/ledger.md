# Evidence ledger: fc_yell_2026_08

- Question: Assume today is 2026-08-15. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in August 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-08-15
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasions c | unit recreation visits | period 2026-08-01..2026-08-31 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 856,467

## Directions and pages

### d1 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from vehicle entries at park entrances multiplied by average occupancy. NPS may report vehicle counts or total entries. If August 2026 vehicle counts are available (e.g., from park traffic counters), they can be converted to visits using a historical occupancy rate. This route is independent of the reported visit total.

Queries issued by the searcher: Yellowstone vehicle entries August vehicle counts NPS traffic counters; Yellowstone National Park average persons per vehicle visitation survey; Yellowstone visitation August 2026 press release recreational vehicles entrances; NPS Visitor Use Statistics Yellowstone monthly recreational vehicles 2025 August

- `https://local.newsbreak.com/kifi-local-news-8-1276858/4891489150987-yellowstone-2026-summer-tourism-shows-decline-in-visitors` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://woodallscm.com/yellowstone-n-p-s-visitation-mixed-for-july/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstonegate.com/?p=7848` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [shocks] Park closures, weather, and policy changes

Hypothesis: Any major closures (e.g., road construction, wildfires, flooding) or policy changes (e.g., reservation requirements) in August 2026 could significantly alter visitation. Identifying such events and their duration/scope can adjust the baseline estimate. For example, the 2022 flood closed the park for a period; a similar event in 2026 would reduce visits.

Queries issued by the searcher: Yellowstone closure August 2026; Yellowstone road construction 2026 closures; Yellowstone reservation system 2026; Yellowstone National Park visitation 2026 news

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 15/3
  - p1 Yellowstone road improvement project delays along road between Canyon Village an = **10** minutes (2026-07-01..2026-08-14) [keep: ] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p2 Yellowstone road improvement project traffic light cycle increments along road b = **10** minutes (2026-07-01..2026-08-14) [keep: ] quote: "One lane will be closed while crews work; traffic lights will operate in 10-minute increments."
  - p3 Yellowstone road improvement project delays in Old Faithful area, up to 15-minut = **15** minutes (2026-07-15..2026-08-15) [keep: ] quote: "Location: Old Faithful area Access: expect up to 15-minute delays from mid-July through mid-August."
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 15/8
  - p4 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p5 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p6 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p7 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p8 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p9 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [keep: ] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p10 Year of hydrothermal explosion at Biscuit Basin, Yellowstone National Park = **2,024** year (2024-01-01..2024-12-31) [DISCARD: The 2024 Biscuit Basin hydrothermal explosion is a past event with no quantified effect on August 2026 visitation; it is] quote: "Biscuit Basin was the site of a 2024 hydrothermal explosion that tossed boiling water and rocks skyward and destroyed a section of boardwalk where tourists were sightseeing."
  - p11 Year of historic flooding that devastated North Entrance Road, Yellowstone Natio = **2,022** year (2022-01-01..2022-12-31) [DISCARD: The 2022 flood is a past event; it is not a quantitative input for August 2026 and its visitation effect is not given.] quote: "The National Park Service is mulling new permanent routes to replace the North Entrance Road, which was devastated by 2022 historic flooding."
- `https://www.yellowstonenationalparklodges.com/alerts/` -> **snapshot** (snapshot 20260703035945); points raw/verified 15/0
- `https://www.recreation.gov/sitepass/72451` -> **snapshot** (snapshot 20260628224112); points raw/verified 0/0
- dropped by code checks: 34 (period_end 2026-10-31 after as_of: 8; number: no number in value_as_written: 4; period_end 2026-09-07 after as_of: 2; period_end 2026-09-15 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-08-31 after as_of: 1; period_end 2026-12-31 after as_of: 1; period_end 2026-10-12 after as_of: 2; period_end missing or unparseable: 9; value_as_written not in quote as a whole number: 2; period_end 2026-09-30 after as_of: 1; number: more than one number in value_as_written: 2)

### d3 [related_series] NPS park-level monthly data for comparable parks

Hypothesis: Other large nature parks (e.g., Grand Teton, Glacier, Yosemite) may show similar seasonal patterns and year-over-year trends. If Yellowstone-specific August 2026 data are unavailable, the ratio of Yellowstone August visits to a broader total (e.g., all NPS visits or a group of parks) can be used to infer Yellowstone's share. The share is relatively stable but may shift with park-specific events.

Queries issued by the searcher: Grand Teton National Park August visitation 2025 NPS statistics; Glacier National Park August 2025 visitation statistics; NPS total recreation visits August 2025 national parks 2026 monthly visitation; Yellowstone National Park August 2025 visitation 2026 monthly report

- `https://tourism.az.gov/wp-content/uploads/2026/04/NPS-August-2025-Final.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://tourism.az.gov/wp-content/uploads/2025/10/NPS-August-2025-10-1-25.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jhnewsandguide.com/news/business/market_watch/market-watch-airport-sees-exponential-growth-in-fall-traffic-in-last-10-years/article_1a6d22` -> **snapshot** (snapshot 20260110180109); points raw/verified 14/14
  - p12 Yellowstone National Park recreational visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p13 Yellowstone National Park recreational visits, August 2024 (implied by year-over = **1.2** percent (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p14 Yellowstone National Park recreational visits, August 2021 (third-busiest August = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p15 Yellowstone National Park recreational visits, August 2017 (second-busiest Augus = **916,166** recreation visits (2017-08-01..2017-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p16 Yellowstone National Park recreational visits, fiscal year ending August 2025 = **4,797,970** recreation visits (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p17 Yellowstone National Park fiscal year ending August 2025 recreational visits, ye = **2.3** percent (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p18 Grand Teton National Park recreational visits, August 2025 = **735,593** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p19 Grand Teton National Park recreational visits, August 2025 vs August 2024 change = **2.6** percent (2025-08-01..2025-08-31) [keep: ] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p20 Grand Teton National Park recreational visits, fiscal year ending August 2025 = **3,730,599** recreation visits (2024-09-01..2025-08-31) [keep: ] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p21 Grand Teton National Park fiscal year ending August 2025 recreational visits, ye = **4.8** percent (2024-09-01..2025-08-31) [keep: ] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p22 Jackson Hole Airport enplanements, October 2025 = **41,622** passengers (2025-10-01..2025-10-31) [keep: ] quote: "In October, enplanements at Jackson Hole Airport totaled 41,622, 9.7% more than the number of passengers who enplaned a commercial airline flight in October 2024."
  - p23 Jackson Hole Airport enplanements, October 2025 vs October 2024 change = **9.7** percent (2025-10-01..2025-10-31) [keep: ] quote: "In October, enplanements at Jackson Hole Airport totaled 41,622, 9.7% more than the number of passengers who enplaned a commercial airline flight in October 2024."
  - p24 Jackson Hole Airport enplanements, fiscal year ending October 2025 = **578,130** passengers (2024-11-01..2025-10-31) [keep: ] quote: "During the fiscal year ending October 2025, enplanements totaled 578,130, a 9.7% increase over the previous 12 months."
  - p25 Jackson Hole Airport fiscal year ending October 2025 enplanements, year-over-yea = **9.7** percent (2024-11-01..2025-10-31) [keep: ] quote: "During the fiscal year ending October 2025, enplanements totaled 578,130, a 9.7% increase over the previous 12 months."
- `https://www.jhnewsandguide.com/news/business/market_watch/market-watch-airport-traffic-at-all-time-high-shutdown-nixes-park-visitation-data/article_1d` -> **snapshot** (snapshot 20251203013351); points raw/verified 15/15
  - p26 Yellowstone National Park August 2025 recreational visits = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p27 Yellowstone National Park August 2025 recreational visits year-over-year change  = **1.2** % (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p28 Yellowstone National Park August 2021 recreational visits (third-busiest August  = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)"
  - p29 Yellowstone National Park August 2017 recreational visits (second-busiest August = **916,166** recreation visits (2017-08-01..2017-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)"
  - p30 Yellowstone National Park fiscal year ending August 2025 recreational visits = **4,797,970** recreation visits (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p31 Yellowstone National Park fiscal year ending August 2025 recreational visits yea = **2.3** % (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p32 Grand Teton National Park August 2025 recreational visits = **735,593** recreation visits (2025-08-01..2025-08-31) [DISCARD: Redundant copy of p18/p97 (same Grand Teton August 2025 total from the same source).] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p33 Grand Teton National Park August 2025 recreational visits year-over-year change  = **2.6** % (2025-08-01..2025-08-31) [DISCARD: Redundant copy of p19/p102 (same 2.6% change).] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p34 Grand Teton National Park August 2025 vs August 2017 (previous busiest August) m = **2.6** % (2025-08-01..2025-08-31) [keep: ] quote: "Historically, August 2025 was the park's busiest-ever August, 2.6% ahead of the previous leader, August 2017."
  - p35 Grand Teton National Park fiscal year ending August 2025 recreational visits = **3,730,599** recreation visits (2024-09-01..2025-08-31) [DISCARD: Redundant copy of p20/p101 (same fiscal-year total).] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p36 Grand Teton National Park fiscal year ending August 2025 recreational visits yea = **4.8** % (2024-09-01..2025-08-31) [DISCARD: Redundant copy of p21/p105 (same 4.8% change).] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p37 Jackson Hole Airport September 2025 enplanements = **67,452** passengers enplaned (2025-09-01..2025-09-30) [keep: ] quote: "In September, enplanements at Jackson Hole Airport totaled 67,452, 21.2% more than the number of passengers who enplaned a commercial airline flight in September 2024."
  - p38 Jackson Hole Airport September 2025 enplanements year-over-year change vs Septem = **21.2** % (2025-09-01..2025-09-30) [keep: ] quote: "In September, enplanements at Jackson Hole Airport totaled 67,452, 21.2% more than the number of passengers who enplaned a commercial airline flight in September 2024."
  - p39 Jackson Hole Airport fiscal year ending September 2025 enplanements = **574,456** passengers enplaned (2024-10-01..2025-09-30) [keep: ] quote: "During the fiscal year ending September 2025, enplanements totaled 574,456, a 10.7% increase over the previous 12 months."
  - p40 Jackson Hole Airport fiscal year ending September 2025 enplanements year-over-ye = **10.7** % (2024-10-01..2025-09-30) [keep: ] quote: "During the fiscal year ending September 2025, enplanements totaled 574,456, a 10.7% increase over the previous 12 months."

### d4 [capacity_consumption] Lodging, campground, and gateway community occupancy

Hypothesis: Park lodging and campground occupancy, plus gateway community hotel occupancy, can proxy for visitation. If August 2026 occupancy rates and room/campsite capacities are known, total overnight stays can be estimated, then converted to visits using a multiplier (day visitors per overnight visitor). This route is indirect and requires assumptions about day-trip share.

Queries issued by the searcher: Yellowstone lodging occupancy August 2026 Xanterra; West Yellowstone hotel occupancy August 2026; Yellowstone National Park monthly visitation statistics August 2025 recreation visits NPS; Yellowstone lodging capacity Xanterra number of rooms campground sites overnight stays statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p41 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p42 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p43 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p44 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p45 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p46 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p47 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p48 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p49 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p50 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://yellowstonetrips.com/when-to-book-yellowstone-lodging/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wyomingpublicmedia.org/news/2025-09-09/yellowstone-is-on-track-for-its-second-busiest-year` -> **snapshot** (snapshot 20251016213459); points raw/verified 6/0
- dropped by code checks: 6 (period_end missing or unparseable: 6)

### d5 [base_rates] Seasonal share of annual visits

Hypothesis: August typically accounts for a stable share of annual recreation visits to Yellowstone (e.g., around 20-25%). If a reliable estimate or forecast of total 2026 annual visits exists, August can be derived by applying the historical August share. This route requires an annual total estimate, which may be available from NPS or tourism sources.

Queries issued by the searcher: Yellowstone annual visitation 2025 total recreation visits; Yellowstone August share of annual recreation visits NPS; Yellowstone recreation visits by month 2024 2023 August IRMA NPS statistics; Yellowstone 2026 visitation July year-to-date recreation visits NPS

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Published forecasts or tourism outlooks

Hypothesis: Tourism forecasts for Yellowstone or Wyoming/Montana may provide an expected range for summer 2026 visitation. These forecasts often incorporate economic conditions, gas prices, and travel trends. They can serve as a sanity check or an input to adjust historical baselines.

Queries issued by the searcher: Yellowstone visitation forecast 2026 summer; Wyoming tourism forecast summer 2026 visitation; Yellowstone National Park August 2026 recreation visits NPS monthly visitation; national park visitation forecast 2026 summer travel outlook

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 7/6
  - p51 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p52 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p53 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p54 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Redundant copy of p7/p116 (same Grand Teton 2025 annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p55 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Redundant copy of p8/p117 (same Grand Teton 2024 annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p56 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Redundant copy of p9/p118 (same Grand Teton 2021 peak annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sheridanwyoming.org/wp-content/uploads/2026/05/2026-Q2-Spring-Industry-Update-WEB.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d7 [attention] Search and social media interest

Hypothesis: Google Trends or social media mentions for Yellowstone may correlate with visitation, but the relationship is noisy and not a direct measure. If a strong correlation is established historically, current attention levels could indicate whether August 2026 is above or below trend. This route is weak and should be used only as a qualitative check.

Queries issued by the searcher: Google Trends Yellowstone National Park visitation correlation search interest; NPS Visitor Use Statistics Yellowstone recreation visits August; Google Trends predict national park visitation search volume correlation study; "Google Trends" Yellowstone search interest August 2026 visitation

- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p57 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p58 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "up 2% from August 2024 (868,259 recreation visits)."
  - p59 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p60 Yellowstone National Park record-breaking year 2021 recreation visits (over) = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p61 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p62 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p63 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p64 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p65 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p66 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://www.sciencedirect.com/science/article/abs/pii/S0301479719306048` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cowboystatedaily.com/2026/08/07/bison-tosses-or-cowboy-culture-why-yellowstone-is-no-1-parks-google-obsession/` -> **snapshot** (snapshot 20260813134538); points raw/verified 15/1
  - p67 Yellowstone Google search margin over Grand Canyon National Park, July 2025 to J = **1,420,000** searches (2025-07-01..2026-06-30) [keep: ] quote: "It's pulled ahead of other heavyweights such as the Grand Canyon by an eye-catching margin of roughly 1.42 million more searches over the most recent period from July 2025 to June 2026."
- `https://creators.yahoo.com/lifestyle/story/america-has-a-favorite-national-parkand-its-not-even-close-174747097.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 13)

### b1 [base_rates] Yellowstone-specific seasonal baseline

Hypothesis: A reliable Yellowstone August recreation-visit total for a recent year (e.g., August 2024 or August 2025) would anchor the level for August 2026 and allow a year-over-year change factor to be applied. Without it, the estimate must rely on Grand Teton analogues and regional growth, which introduces transfer error.

Queries issued by the searcher: Yellowstone National Park August 2024 recreation visits NPS visitor use statistics; Yellowstone August 2025 visitation record recreation visits; Yellowstone visitation statistics July 2026 recreation visits news release; "Yellowstone" 2026 visitation "June 2026" recreation visits NPS

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p68 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p69 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p70 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p71 Yellowstone National Park record-breaking year total recreation visits (2021) = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
  - p72 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p73 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p74 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p75 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p76 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p77 Yellowstone National Park year-to-date recreation visits through July 2022 = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
- `https://www.nps.gov/yell/learn/news/25019.htm` -> **snapshot** (snapshot 20260416044835); points raw/verified 10/10
  - p78 Yellowstone National Park recreation visits, August 2025 = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p79 Yellowstone National Park recreation visits, August 2024 = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 881,936 recreation visits in August 2025, up 2% from August 2024 (868,259 recreation visits)."
  - p80 Yellowstone National Park recreation visits, August 2021 = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "This August's visitation showed a 4% decrease from August 2021 (921,844 recreation visits)."
  - p81 Yellowstone National Park record-breaking annual recreation visits, 2021 = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021, with over 4.8 million recreation visits."
  - p82 Yellowstone National Park year-to-date recreation visits through August 2025 = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p83 Yellowstone National Park year-to-date recreation visits through August 2024 = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p84 Yellowstone National Park year-to-date recreation visits through August 2021 = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "So far in 2025, the park has hosted 3,547,967 recreation visits, up 2% from 2024 (3,494,350 recreation visits), and down 1% from 2021 (3,590,609 recreation visits)."
  - p85 Yellowstone National Park year-to-date recreation visits through August 2023 = **3,308,924** recreation visits (2023-01-01..2023-08-31) [EXCLUDED (ablation): ] quote: "2023 - 3,308,924"
  - p86 Yellowstone National Park year-to-date recreation visits through August 2022 = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "2022 - 2,437,607 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p87 Yellowstone National Park year-to-date recreation visits through August 2020 = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "2020 - 2,556,528 (The park was closed March 24 through May 17 due to COVID-19. Two entrances opened on May 18 and the remaining three opened on June 1.)"
- `https://home.nps.gov/yell/learn/news/24034.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Yellowstone-to-Grand Teton August ratio

Hypothesis: The ratio of Yellowstone August recreation visits to Grand Teton August recreation visits is relatively stable across years. If that ratio can be established from historical NPS data, the kept Grand Teton August 2025 total (p18) can be scaled to a Yellowstone August baseline, then adjusted for 2026. This would convert already-collected evidence into a direct Yellowstone estimate.

Queries issued by the searcher: Yellowstone August recreation visits NPS Visitor Use Statistics; Grand Teton August recreation visits 2024 2023 NPS statistics; Grand Teton National Park August 2025 recreation visits 735,593 news release; Grand Teton National Park August 2024 visitation 701,711 record

- `https://idahonews.com/news/local/park-population-peaks-yellowstone-sees-slight-rise-in-august-visitors` -> **snapshot** (snapshot 20250906003304); points raw/verified 8/8
  - p88 Yellowstone National Park August 2025 recreation visits = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park experienced a slight uptick in visitors this August, with 881,936 recreation visits recorded."
  - p89 Yellowstone National Park August 2024 recreation visits = **868,259** recreation visits (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "This marks a 2% increase from August 2024, which saw 868,259 visits."
  - p90 Yellowstone National Park August 2021 recreation visits (record-breaking August) = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "this year's August visitation was still 4% lower than the record-breaking August of 2021, when 921,844 visitors flocked to the park."
  - p91 Yellowstone National Park year-to-date through August 2025 recreation visits = **3,547,967** recreation visits (2025-01-01..2025-08-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone has welcomed 3,547,967 recreation visits so far, according to the National Park Service"
  - p92 Yellowstone National Park year-to-date through August 2024 recreation visits = **3,494,350** recreation visits (2024-01-01..2024-08-31) [EXCLUDED (ablation): ] quote: "reflecting a 2% rise from the same period in 2024, which had 3,494,350 visits."
  - p93 Yellowstone National Park year-to-date through August 2021 recreation visits = **3,590,609** recreation visits (2021-01-01..2021-08-31) [EXCLUDED (ablation): ] quote: "the current year's numbers are down 1% from 2021, when the park recorded 3,590,609 visits by the end of August."
  - p94 Yellowstone National Park year-to-date through August 2022 recreation visits (fl = **2,437,607** recreation visits (2022-01-01..2022-08-31) [EXCLUDED (ablation): ] quote: "In 2022, the park was closed for several days in June due to a historic flood event, resulting in 2,437,607 visits by August."
  - p95 Yellowstone National Park year-to-date through August 2020 recreation visits (CO = **2,556,528** recreation visits (2020-01-01..2020-08-31) [EXCLUDED (ablation): ] quote: "In 2020, the park faced closures from March to May due to the COVID-19 pandemic, leading to 2,556,528 visits by the end of August."
- `https://www.jhnewsandguide.com/news/business/market_watch/market-watch-airport-sees-exponential-growth-in-fall-traffic-in-last-10-years/article_1a6d22` -> **snapshot** (snapshot 20260110180109); points raw/verified 14/14
  - p96 Yellowstone National Park August 2025 recreation visits = **881,936** recreation visits (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p97 Grand Teton National Park August 2025 recreation visits = **735,593** recreation visits (2025-08-01..2025-08-31) [DISCARD: Redundant copy of p18/p32 (same Grand Teton August 2025 total).] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p98 Yellowstone National Park August 2021 recreation visits = **921,844** recreation visits (2021-08-01..2021-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p99 Yellowstone National Park August 2017 recreation visits = **916,166** recreation visits (2017-08-01..2017-08-31) [EXCLUDED (ablation): ] quote: "this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p100 Yellowstone National Park fiscal year ending August 2025 recreation visits = **4,797,970** recreation visits (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p101 Grand Teton National Park fiscal year ending August 2025 recreation visits = **3,730,599** recreation visits (2024-09-01..2025-08-31) [DISCARD: Redundant copy of p20/p35 (same fiscal-year total).] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p102 Grand Teton National Park August 2025 recreation visits year-over-year change = **2.6** percent (2025-08-01..2025-08-31) [DISCARD: Redundant copy of p19/p33 (same 2.6% change).] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p103 Yellowstone National Park August 2025 recreation visits year-over-year change = **1.2** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p104 Yellowstone National Park fiscal year ending August 2025 recreation visits year- = **2.3** percent (2024-09-01..2025-08-31) [EXCLUDED (ablation): ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p105 Grand Teton National Park fiscal year ending August 2025 recreation visits year- = **4.8** percent (2024-09-01..2025-08-31) [DISCARD: Redundant copy of p21/p36 (same 4.8% change).] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p106 Jackson Hole Airport October 2025 enplanements = **41,622** enplanements (2025-10-01..2025-10-31) [DISCARD: Redundant copy of p22/p108 (same October 2025 enplanements).] quote: "In October, enplanements at Jackson Hole Airport totaled 41,622, 9.7% more than the number of passengers who enplaned a commercial airline flight in October 2024."
  - p107 Jackson Hole Airport October 2025 enplanements year-over-year change = **9.7** percent (2025-10-01..2025-10-31) [DISCARD: Redundant copy of p23/p109 (same 9.7% change).] quote: "In October, enplanements at Jackson Hole Airport totaled 41,622, 9.7% more than the number of passengers who enplaned a commercial airline flight in October 2024."
  - p108 Jackson Hole Airport fiscal year ending October 2025 enplanements = **578,130** enplanements (2024-11-01..2025-10-31) [DISCARD: Redundant copy of p24/p106 (same fiscal-year enplanements).] quote: "During the fiscal year ending October 2025, enplanements totaled 578,130, a 9.7% increase over the previous 12 months."
  - p109 Jackson Hole Airport fiscal year ending October 2025 enplanements year-over-year = **9.7** percent (2024-11-01..2025-10-31) [DISCARD: Redundant copy of p25/p107 (same 9.7% change).] quote: "During the fiscal year ending October 2025, enplanements totaled 578,130, a 9.7% increase over the previous 12 months."
- `https://buckrail.com/year-to-date-visitation-in-grand-teton-nearly-identical-to-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] August 2026 Yellowstone access and policy conditions

Hypothesis: The kept road-project points (p1-p3) show only minor delays, but any additional August 2026 closure, reservation requirement, or wildfire smoke event could materially change visitation. Confirming the absence or presence of such events would resolve the largest uncertainty in the 2026 adjustment.

Queries issued by the searcher: Yellowstone National Park 2026 road construction closures summer; Yellowstone 2026 reservation timed entry policy; Yellowstone National Park August 2026 wildfire smoke closures; NPS Visitor Use Statistics Yellowstone recreation visits monthly 2026

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260814162057); points raw/verified 15/3
  - p110 Yellowstone fiber project between Canyon Village and West Thumb: minimum traffic = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Redundant copy of p1 (same Canyon–West Thumb delay).] quote: "expect delays of at least 10 minutes from 7 a.m. to 6 p.m. weekdays from early-July through August 14, 2026."
  - p111 Yellowstone fiber project between Canyon Village and West Thumb: traffic light c = **10** minutes (2026-07-01..2026-08-14) [DISCARD: Redundant copy of p2 (same traffic-light cycle).] quote: "One lane will be closed while crews work; traffic lights will operate in 10-minute increments."
  - p112 Yellowstone Old Faithful area road project: maximum traffic delay, mid-July thro = **15** minutes (2026-07-15..2026-08-15) [DISCARD: Redundant copy of p3 (same Old Faithful delay).] quote: "Location: Old Faithful area Access: expect up to 15-minute delays from mid-July through mid-August."
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 15/9
  - p113 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p114 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p115 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p116 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [DISCARD: Redundant copy of p7/p54 (same Grand Teton 2025 annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p117 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Redundant copy of p8/p55 (same Grand Teton 2024 annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p118 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Redundant copy of p9/p56 (same Grand Teton 2021 peak annual total).] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p119 Maximum intermittent traffic delay on Moose-Wilson Road corridor, Grand Teton Na = **45** minutes (2025-06-20..2025-09-07) [keep: ] quote: "Visitors can expect intermittent delays of up to 45 minutes through the corridor from June 20 to Sept. 7."
  - p120 Year of hydrothermal explosion at Biscuit Basin, Yellowstone National Park = **2,024** year (2024-01-01..2024-12-31) [DISCARD: Redundant copy of p10 (same 2024 Biscuit Basin explosion year).] quote: "Biscuit Basin was the site of a 2024 hydrothermal explosion that tossed boiling water and rocks skyward and destroyed a section of boardwalk where tourists were sightseeing."
  - p121 Year of historic flooding that devastated North Entrance Road, Yellowstone Natio = **2,022** year (2022-01-01..2022-12-31) [DISCARD: Redundant copy of p11 (same 2022 flood year).] quote: "The National Park Service is mulling new permanent routes to replace the North Entrance Road, which was devastated by 2022 historic flooding."
- `https://kamala.cod.edu/wy/latest.aeus75.KRIW.html` -> **snapshot** (snapshot 20211024114540); points raw/verified 2/1
  - p122 Air Quality Alert expiration time for Yellowstone National Park wildfire smoke = **1** time of day and date (2021-10-01..2021-10-01) [DISCARD: A 2021 air-quality alert expiration time is irrelevant to August 2026 visitation and provides no usable quantitative inp] quote: "..AIR QUALITY ALERT IN EFFECT UNTIL 1 PM MDT FRIDAY"
- `https://www.recreation.gov/sitepass/72451` -> **snapshot** (snapshot 20260628224112); points raw/verified 0/0
- dropped by code checks: 19 (period_end 2026-10-31 after as_of: 3; number: no number in value_as_written: 1; period_end missing or unparseable: 6; number: more than one number in value_as_written: 2; period_end 2026-09-07 after as_of: 1; period_end 2026-09-15 after as_of: 1; period_end 2026-11-30 after as_of: 1; period_end 2026-08-31 after as_of: 1; period_end 2026-12-31 after as_of: 1; value_as_written not in quote as a whole number: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'august', 'visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p18', 'p32'] Same Grand Teton August 2025 recreation-visit total (735,593) reported in two snapshots of the same underlying article; they are duplicate evidence, not independent confirmation.
- corroborating: ['p19', 'p33'] Same +2.6% August 2025 vs August 2024 change for Grand Teton, duplicated across snapshots.
- corroborating: ['p20', 'p35'] Same Grand Teton fiscal-year-ending-August-2025 total (3,730,599), duplicated.
- corroborating: ['p21', 'p36'] Same +4.8% fiscal-year change for Grand Teton, duplicated.
- corroborating: ['p7', 'p54'] Same Grand Teton 2025 annual recreation visits (3.8 million), duplicated across snapshots.
- corroborating: ['p8', 'p55'] Same Grand Teton 2024 annual recreation visits (3.6 million), duplicated.
- corroborating: ['p9', 'p56'] Same Grand Teton 2021 record annual recreation visits (3.88 million), duplicated.
- corroborating: ['p1', 'p2', 'p3'] All describe the same summer 2026 Yellowstone road-improvement project; they indicate modest, localized delay (10-15 minutes) rather than a closure, so they are contextual for a small downward adjustm
- corroborating: ['p10', 'p11'] Both are historical Yellowstone disruption events (2024 hydrothermal explosion, 2022 flood) cited in the same article; they establish that park-specific shocks occur but do not quantify August 2026.
- corroborating: ['p22', 'p23', 'p24', 'p25', 'p37', 'p38', 'p39', 'p40'] Jackson Hole Airport enplanement series all point to strong 2025 regional air-travel growth (roughly +10% fiscal-year), consistent with the Grand Teton visitation growth; they are regional demand indi
- corroborating: ['p18', 'p20', 'p7'] Grand Teton August 2025, fiscal-year 2025, and calendar-year 2025 totals are mutually consistent and show a strong 2025 season in the Yellowstone ecosystem.
- corroborating: ['p67'] Yellowstone search interest running well ahead of Grand Canyon in 2025-2026 is a weak qualitative signal of sustained or elevated attention; it cannot be converted to visits without a calibrated relat
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p18', 'p32', 'p97'] All three report the same Grand Teton August 2025 recreation-visit total (735,593) from the same underlying NPS figure, so they are redundant copies rather than independent measurements.
- corroborating: ['p19', 'p33', 'p102'] All three report the same 2.6% August 2025 vs August 2024 change for Grand Teton, again from the same underlying source.
- corroborating: ['p20', 'p35', 'p101'] All three report the same Grand Teton fiscal-year-ending-August-2025 total (3,730,599), a redundant copy of one NPS-derived figure.
- corroborating: ['p21', 'p36', 'p105'] All three report the same 4.8% fiscal-year change for Grand Teton, redundant copies of one figure.
- corroborating: ['p22', 'p106'] Both report Jackson Hole Airport October 2025 enplanements (41,622), redundant copies.
- corroborating: ['p23', 'p107'] Both report the same 9.7% October 2025 enplanement change, redundant copies.
- corroborating: ['p24', 'p108'] Both report Jackson Hole Airport fiscal-year-ending-October-2025 enplanements (578,130), redundant copies.
- corroborating: ['p25', 'p109'] Both report the same 9.7% fiscal-year enplanement change, redundant copies.
- corroborating: ['p7', 'p54', 'p116'] All three report Grand Teton 2025 annual recreation visits (3.8 million), redundant copies of one figure.
- corroborating: ['p8', 'p55', 'p117'] All three report Grand Teton 2024 annual recreation visits (3.6 million), redundant copies.
- corroborating: ['p9', 'p56', 'p118'] All three report Grand Teton's highest-ever annual visits (3.88 million in 2021), redundant copies.
- corroborating: ['p1', 'p110'] Both describe the same Canyon Village–West Thumb fiber-project delay of at least 10 minutes on weekdays through August 14, 2026.
- corroborating: ['p2', 'p111'] Both describe the same 10-minute traffic-light cycle for the Canyon Village–West Thumb project.
- corroborating: ['p3', 'p112'] Both describe the same Old Faithful area road project with up to 15-minute delays from mid-July through mid-August 2026.
- corroborating: ['p10', 'p120'] Both identify 2024 as the year of the Biscuit Basin hydrothermal explosion, redundant copies.
- corroborating: ['p11', 'p121'] Both identify 2022 as the year of the historic Yellowstone flood, redundant copies.
- corroborating: ['p37', 'p38', 'p39', 'p40'] Jackson Hole Airport September 2025 enplanements and fiscal-year-ending-September-2025 figures are internally consistent with the October 2025 figures and indicate strong regional air-travel growth in
- corroborating: ['p67'] Yellowstone's large Google-search margin over Grand Canyon in July 2025–June 2026 is consistent with sustained high interest, but it is only a qualitative attention signal, not a visitation measure.
- conflicting: ['p119'] The Moose-Wilson Road delay in Grand Teton is a different park and period; it does not directly conflict with Yellowstone's 2026 road projects but shows that regional construction can affect visitatio

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Yellowstone-to-Grand-Teton August recreation-visit ratio | 1.35 | 1.15..1.55 | 0.9441..1.888 (widened) | ratio | m1 (m1) | Historical NPS monthly data show Yellowstone August recreation visits typically exceed Grand Teton August visits by roughly 30–40%. The ratio is used to transfer the kept Grand Teton August 2025 level (p18) to a Yellowstone August baseline. The range reflects year-to-year variation in the ratio and  | The ratio is applied to Grand Teton August 2025 visits to estimate Yellowstone August 2025 visits, then adjusted to 2026. It assumes the two parks' August visitation relationship remains within its historical range. | A kept Yellowstone August 2025 or August 2026 total showing a ratio outside 1.15–1.55, or evidence of a park-specific shock that breaks the historical relationship. |
| a2 | Yellowstone August 2026 vs August 2025 change factor | 1 | 0.9..1.1 | 0.8899..1.112 (widened) | ratio | m1 (m1) | No kept point gives a Yellowstone-specific 2026 August change. Regional analogues are mixed: Grand Teton August 2025 was up 2.6% year-over-year (p19), Jackson Hole air traffic was up strongly in late 2025 (p37–p40), but the 2026 road projects (p1–p3) may modestly suppress visits. A central factor of | Applied to the Yellowstone August 2025 baseline to project August 2026. It assumes no major park-wide closure or reservation change beyond the known road projects. | Evidence of a major August 2026 closure, reservation requirement, wildfire, or a kept Yellowstone 2026 monthly total showing a change outside 0.9–1.1. |

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 75 of 122
- methods allowed: ['formula_mc']

  - p4 Yellowstone National Park annual recreation visits in 2025 = 4,760,000 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p5 Yellowstone National Park annual recreation visits in 2024 = 4,740,000 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p6 Yellowstone National Park annual recreation visits in 2021 = 4,860,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p12 Yellowstone National Park recreational visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p13 Yellowstone National Park recreational visits, August 2024 (implied by year-over-year comp = 1.2 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p14 Yellowstone National Park recreational visits, August 2021 (third-busiest August compariso = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p15 Yellowstone National Park recreational visits, August 2017 (second-busiest August comparis = 916,166 (2017-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p16 Yellowstone National Park recreational visits, fiscal year ending August 2025 = 4,797,970 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p17 Yellowstone National Park fiscal year ending August 2025 recreational visits, year-over-ye = 2.3 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p26 Yellowstone National Park August 2025 recreational visits = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p27 Yellowstone National Park August 2025 recreational visits year-over-year change vs August  = 1.2 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p28 Yellowstone National Park August 2021 recreational visits (third-busiest August comparison = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p29 Yellowstone National Park August 2017 recreational visits (second-busiest August compariso = 916,166 (2017-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p30 Yellowstone National Park fiscal year ending August 2025 recreational visits = 4,797,970 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p31 Yellowstone National Park fiscal year ending August 2025 recreational visits year-over-yea = 2.3 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p41 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p42 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p43 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p44 Yellowstone National Park record-breaking annual recreation visits, 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p45 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p46 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p47 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p48 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p49 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p50 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p51 Yellowstone National Park annual recreation visits in 2025 = 4,760,000 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p52 Yellowstone National Park annual recreation visits in 2024 = 4,740,000 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p53 Yellowstone National Park annual recreation visits in 2021 = 4,860,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p57 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p58 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p59 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p60 Yellowstone National Park record-breaking year 2021 recreation visits (over) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p61 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p62 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p63 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p64 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p65 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p66 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p68 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p69 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p70 Yellowstone National Park recreation visits, July 2021 (record July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p71 Yellowstone National Park record-breaking year total recreation visits (2021) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p72 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p73 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p74 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p75 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p76 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p77 Yellowstone National Park year-to-date recreation visits through July 2022 = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p78 Yellowstone National Park recreation visits, August 2025 = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p79 Yellowstone National Park recreation visits, August 2024 = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p80 Yellowstone National Park recreation visits, August 2021 = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p81 Yellowstone National Park record-breaking annual recreation visits, 2021 = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p82 Yellowstone National Park year-to-date recreation visits through August 2025 = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p83 Yellowstone National Park year-to-date recreation visits through August 2024 = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p84 Yellowstone National Park year-to-date recreation visits through August 2021 = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p85 Yellowstone National Park year-to-date recreation visits through August 2023 = 3,308,924 (2023-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p86 Yellowstone National Park year-to-date recreation visits through August 2022 = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p87 Yellowstone National Park year-to-date recreation visits through August 2020 = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p88 Yellowstone National Park August 2025 recreation visits = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p89 Yellowstone National Park August 2024 recreation visits = 868,259 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p90 Yellowstone National Park August 2021 recreation visits (record-breaking August) = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p91 Yellowstone National Park year-to-date through August 2025 recreation visits = 3,547,967 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p92 Yellowstone National Park year-to-date through August 2024 recreation visits = 3,494,350 (2024-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p93 Yellowstone National Park year-to-date through August 2021 recreation visits = 3,590,609 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p94 Yellowstone National Park year-to-date through August 2022 recreation visits (flood closur = 2,437,607 (2022-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p95 Yellowstone National Park year-to-date through August 2020 recreation visits (COVID-19 clo = 2,556,528 (2020-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p96 Yellowstone National Park August 2025 recreation visits = 881,936 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p98 Yellowstone National Park August 2021 recreation visits = 921,844 (2021-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p99 Yellowstone National Park August 2017 recreation visits = 916,166 (2017-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p100 Yellowstone National Park fiscal year ending August 2025 recreation visits = 4,797,970 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p103 Yellowstone National Park August 2025 recreation visits year-over-year change = 1.2 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p104 Yellowstone National Park fiscal year ending August 2025 recreation visits year-over-year  = 2.3 (2025-08-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p113 Yellowstone National Park annual recreation visits in 2025 = 4,760,000 (2025-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p114 Yellowstone National Park annual recreation visits in 2024 = 4,740,000 (2024-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p115 Yellowstone National Park annual recreation visits in 2021 = 4,860,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 978,047 | ['p18'] / ['a1', 'a2'] | [] |  | 1.00 | equal |  |

Result: central **978,047**, 80% interval [648,727, 1,474,544], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for recreation visits to Yellowstone National Park during August 2026, as reported in NPS monthly visitation statistics, is 978,047 visits. The supplied interval is 648,727 to 1,474,544, a model-based range conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate rests on one method (978,047, weight 100%). It transfers the kept Grand Teton August 2025 total using an assumed Yellowstone/Grand Teton August ratio of 1.35 (range 0.9441–1.888), then applies a [n] change factor of 1 (range 0.8899–1.112). Only the Grand Teton August 2025 point is observed; the ratio and change factor are analyst assumptions, so the result is indirect.

The main risk is a shift in the Yellowstone–Grand Teton ratio or an unobserved August 2026 shock, including road projects. The most useful missing evidence would be a kept Yellowstone August total or partial [n] Yellowstone data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Yellowstone-to-Grand-Teton August recreation-visit ratio: 1.35 ratio, range 0.9441 to 1.888 (range widened by code); used by m1. Overturned by: A kept Yellowstone August 2025 or August 2026 total showing a ratio outside [n]–[n], or evidence of a park-specific shock that breaks the historical relationship.
- a2 Yellowstone August 2026 vs August 2025 change factor: 1 ratio, range 0.8899 to 1.112 (range widened by code); used by m1. Overturned by: Evidence of a major August 2026 closure, reservation requirement, wildfire, or a kept Yellowstone [n] monthly total showing a change outside [n]–[n].

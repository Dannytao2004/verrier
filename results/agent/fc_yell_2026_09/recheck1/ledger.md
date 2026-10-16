# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Visitor Use Statistics / Monthly Public Use Report). Counts are recreation visits, not unique visitors; a visit is one person entering the park for recreational purpo | unit recreation visits | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), Visitor Use Statistics program

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [own_history] NPS historical monthly visitation reports

Hypothesis: September recreation visits in recent years provide a baseline; adjusting for year-over-year trends and known shocks yields an estimate for September 2026.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September recreation visits; NPS Visitor Use Statistics Yellowstone 2025 monthly public use report; Yellowstone September recreation visits 2018 2019 2020 2022 2023 monthly report; Yellowstone visitation statistics July 2026 recreation visits year-to-date

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/23038.htm` -> **snapshot** (snapshot 20260214203637); points raw/verified 13/13
  - p1 Yellowstone National Park recreation visits, September 2023 = **838,458** recreation visits (2023-09-01..2023-09-30) [keep: ] quote: "Yellowstone National Park hosted 838,458 recreation visits in September 2023."
  - p2 Yellowstone National Park recreation visits, September 2022 = **567,587** recreation visits (2022-09-01..2022-09-30) [keep: ] quote: "This is a 48% increase from September 2022 (567,587 recreational visits)"
  - p3 Yellowstone National Park recreation visits, September 2019 = **693,118** recreation visits (2019-09-01..2019-09-30) [keep: ] quote: "a 21% increase from September 2019* (693,118 recreational visits)."
  - p4 Yellowstone National Park year-to-date recreation visits through September 2023 = **4,161,602** recreation visits (2023-01-01..2023-09-30) [keep: ] quote: "So far in 2023, the park has hosted 4,161,602 recreation visits"
  - p5 Yellowstone National Park year-to-date recreation visits through September 2022 = **3,005,194** recreation visits (2022-01-01..2022-09-30) [keep: ] quote: "up 38% from 2022 (3,005,194 recreation visits)"
  - p6 Yellowstone National Park year-to-date recreation visits through September 2019 = **3,807,815** recreation visits (2019-01-01..2019-09-30) [keep: ] quote: "up 9% from 2019 (3,807,815 recreation visits)."
  - p7 Yellowstone National Park year-to-date recreation visits through September 2021 = **4,472,687** recreation visits (2021-01-01..2021-09-30) [keep: ] quote: "2021 - 4,472,687"
  - p8 Yellowstone National Park year-to-date recreation visits through September 2020 = **3,393,642** recreation visits (2020-01-01..2020-09-30) [keep: ] quote: "2020 - 3,393,642 (The park was closed March 24 through May 17."
  - p9 Yellowstone National Park year-to-date recreation visits through September 2018 = **3,860,695** recreation visits (2018-01-01..2018-09-30) [keep: ] quote: "2018 - 3,860,695"
  - p10 Year-over-year change in Yellowstone September recreation visits, 2023 vs 2022 = **48** % (2023-09-01..2023-09-30) [DISCARD: Redundant derived percentage change already implied by p1 and p2; adds no independent information.] quote: "This is a 48% increase from September 2022 (567,587 recreational visits)"
  - p11 Year-over-year change in Yellowstone September recreation visits, 2023 vs 2019 = **21** % (2023-09-01..2023-09-30) [DISCARD: Redundant derived percentage change already implied by p1 and p3; adds no independent information.] quote: "a 21% increase from September 2019* (693,118 recreational visits)."
  - p12 Year-over-year change in Yellowstone year-to-date recreation visits through Sept = **38** % (2023-01-01..2023-09-30) [DISCARD: Redundant derived percentage change already implied by p4 and p5; adds no independent information.] quote: "the park has hosted 4,161,602 recreation visits, up 38% from 2022"
  - p13 Year-over-year change in Yellowstone year-to-date recreation visits through Sept = **9** % (2023-01-01..2023-09-30) [DISCARD: Redundant derived percentage change already implied by p4 and p6; adds no independent information.] quote: "up 9% from 2019 (3,807,815 recreation visits)."
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] NPS park-level and national visitation trends

Hypothesis: Yellowstone's share of total NPS recreation visits or of a comparable set of large parks is relatively stable; applying that share to a broader total or using comparable parks' September trends can estimate Yellowstone's September 2026 visits.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September 2025; NPS national monthly visitation 2026 recreation visits; Grand Teton National Park September 2025 recreation visits monthly report; Yosemite National Park September 2025 visitation monthly statistics

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.miamiherald.com/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.ae/news/article/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-occupancy-amid-n` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aol.com/articles/data-shows-national-parks-could-194320000.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [shocks] Closures, weather, and policy changes

Hypothesis: Known shocks (e.g., road closures, wildfires, government shutdowns, reservation requirements) can significantly alter September visitation; identifying and quantifying their impact improves the estimate.

Queries issued by the searcher: Yellowstone closures September 2026; Yellowstone visitation impact wildfire September; Yellowstone National Park September 2026 visitation record; Yellowstone National Park 2026 fire restrictions wildfire closure; Yellowstone National Park reports August 2026 visitation statistics; Yellowstone September 2025 visitation statistics 839,579

- `https://home.nps.gov/yell/planyourvisit/operating-dates.htm` -> **snapshot** (snapshot 20260614230148); points raw/verified 15/1
  - p14 Pebble Creek Campground closure due to 2022 floods (closed until further notice) = **2,022** year (2022-01-01..2022-12-31) [DISCARD: Pebble Creek is a small campground; the closure is a minor capacity caveat but not a usable numeric input for a Septembe] quote: "Pebble Creek Campground was significantly impacted by the 2022 floods and will remain closed until further notice for flood recovery work."
- `https://fishbio.com/news/stream-in-yellowstone-national-park-closed-as-officials-poison-invasive-fish/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://k2radio.com/ixp/102/p/yellowstone-road-closures-winter-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (period_end 2026-09-13 after as_of: 3; period_end 2026-09-19 after as_of: 1; period_end 2026-09-26 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-09-27 after as_of: 1; period_end 2026-10-24 after as_of: 1; period_end 2026-10-18 after as_of: 1; period_end 2026-10-10 after as_of: 1; number: more than one number in value_as_written: 2; period_end 2026-09-07 after as_of: 2)

### d4 [base_rates] Seasonal share of annual visits

Hypothesis: September typically accounts for a stable share of Yellowstone's annual recreation visits; applying that share to a projected annual total for 2026 yields a September estimate.

Queries issued by the searcher: Yellowstone annual visitation September share monthly distribution; Yellowstone National Park year-to-date visitation 2026; Yellowstone annual recreation visits 2024 2025 total 4.7 million NPS; Yellowstone National Park visitation statistics monthly table September average percent annual visits nps.gov

- `https://irma.nps.gov/Stats/Reports/Park/YELL` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/planyourvisit/visitationstats.htm` -> **snapshot** (snapshot 20260422081553); points raw/verified 13/13
  - p15 Yellowstone National Park average September recreation visits, 2014-2018 average = **663,651** recreation visits (2014-09-01..2018-09-30) [keep: ] quote: "\| September \| 663,651 \| 16.51% \|"
  - p16 September share of average annual Yellowstone recreation visits, 2014-2018 avera = **16.51** % (2014-09-01..2018-09-30) [DISCARD: Redundant share derived from p15 and the other monthly averages; the level p15 is sufficient for the seasonal-share rout] quote: "\| September \| 663,651 \| 16.51% \|"
  - p17 Yellowstone average January recreation visits, 2014-2018 average = **28,837** recreation visits (2014-01-01..2018-01-31) [DISCARD: January average is not relevant to September estimation and is not needed for the seasonal-share route.] quote: "\| January \| 28,837 \| 0.72% \|"
  - p18 Yellowstone average February recreation visits, 2014-2018 average = **33,088** recreation visits (2014-02-01..2018-02-28) [DISCARD: February average is not relevant to September estimation.] quote: "\| February \| 33,088 \| 0.82% \|"
  - p19 Yellowstone average March recreation visits, 2014-2018 average = **22,266** recreation visits (2014-03-01..2018-03-31) [DISCARD: March average is not relevant to September estimation.] quote: "\| March \| 22,266 \| 0.55% \|"
  - p20 Yellowstone average April recreation visits, 2014-2018 average = **44,027** recreation visits (2014-04-01..2018-04-30) [DISCARD: April average is not relevant to September estimation.] quote: "\| April \| 44,027 \| 1.10% \|"
  - p21 Yellowstone average May recreation visits, 2014-2018 average = **401,449** recreation visits (2014-05-01..2018-05-31) [DISCARD: May average is not relevant to September estimation.] quote: "\| May \| 401,449 \| 9.99% \|"
  - p22 Yellowstone average June recreation visits, 2014-2018 average = **780,652** recreation visits (2014-06-01..2018-06-30) [DISCARD: June average is not relevant to September estimation.] quote: "\| June \| 780,652 \| 19.42% \|"
  - p23 Yellowstone average July recreation visits, 2014-2018 average = **947,688** recreation visits (2014-07-01..2018-07-31) [DISCARD: July average is not relevant to September estimation.] quote: "\| July \| 947,688 \| 23.57% \|"
  - p24 Yellowstone average August recreation visits, 2014-2018 average = **839,787** recreation visits (2014-08-01..2018-08-31) [DISCARD: August average is not relevant to September estimation.] quote: "\| August \| 839,787 \| 20.89% \|"
  - p25 Yellowstone average October recreation visits, 2014-2018 average = **223,777** recreation visits (2014-10-01..2018-10-31) [DISCARD: October average is not relevant to September estimation.] quote: "\| October \| 223,777 \| 5.57% \|"
  - p26 Yellowstone average November recreation visits, 2014-2018 average = **14,323** recreation visits (2014-11-01..2018-11-30) [DISCARD: November average is not relevant to September estimation.] quote: "\| November \| 14,323 \| 0.36% \|"
  - p27 Yellowstone average December recreation visits, 2014-2018 average = **20,434** recreation visits (2014-12-01..2018-12-31) [DISCARD: December average is not relevant to September estimation.] quote: "\| December \| 20,434 \| 0.51% \|"
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/yellowstone-reports-4-76-million-visitors-in-2025-second-busiest-year-on-record/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] Entrance station counts and vehicle occupancy

Hypothesis: Recreation visits can be estimated from vehicle entries at park entrances multiplied by average occupancy, adjusted for seasonality and non-recreation entries.

Queries issued by the searcher: Yellowstone entrance vehicle counts September 2025 visitation statistics; Yellowstone average vehicle occupancy visitation estimate; Yellowstone National Park September 2025 recreation visits monthly public use report; NPS Visitor Use Statistics Yellowstone monthly report 2025 recreation visits

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.miamiherald.com/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grizzlyrv.com/which-yellowstone-entrance-should-rvers-stay-near/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [capacity_consumption] Lodging, campground, and tour capacity

Hypothesis: September visitation is constrained by available lodging and campground capacity; occupancy rates and capacity can bound or estimate visits.

Queries issued by the searcher: Yellowstone lodging occupancy September Xanterra; Yellowstone campground capacity number of sites statistics; Yellowstone National Park lodging rooms capacity 2000 rooms Xanterra annual report; NPS Visitor Use Statistics Yellowstone monthly public use report September 2025 recreation visits

- `https://www.nps.gov/yell/planyourvisit/campgrounds.htm` -> **snapshot** (snapshot 20260821140207); points raw/verified 15/0
- `https://powelltribune.com/stories/region-continues-to-buck-downward-trend-of-tourism,170327` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yellowstone.co/camping.htm` -> **snapshot** (snapshot 20260615181604); points raw/verified 0/0
- `https://maintenancejobs.net/profile/yellowstone-national-park-lodges/1719388/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end missing or unparseable: 6; period_end 2026-09-13 after as_of: 1; period_end 2026-09-19 after as_of: 1; period_end 2026-10-17 after as_of: 2; period_end 2026-09-26 after as_of: 1; period_end 2026-09-14 after as_of: 1; period_end 2026-10-11 after as_of: 1; period_end 2026-10-12 after as_of: 1; period_end 2026-09-27 after as_of: 1)

### d7 [forecasts_markets] Published forecasts and tourism outlooks

Hypothesis: Tourism forecasts for Yellowstone or Wyoming/Montana may provide a directional signal for September 2026 visitation.

Queries issued by the searcher: Yellowstone visitation forecast 2026; Wyoming tourism forecast fall 2026; Montana tourism outlook 2026; Yellowstone September visitation statistics 2025

- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.com/news/article/0tf6wt7yoqpa/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://montanaeconomist.org/a-steady-year-amid-shifting-trends/` -> **snapshot** (snapshot 20260511092735); points raw/verified 15/8
  - p28 Canadian border crossings decline year-to-date as of November 2025 (Montana) = **17** percent (2025-01-01..2025-11-30) [keep: ] quote: "Canadian border crossings were down 17% year-to-date (as of November 2025)"
  - p29 Canadian border crossings decline in third quarter of 2025 (Montana) = **24** percent (2025-07-01..2025-09-30) [keep: ] quote: "nearly 24% in the third quarter of 2025"
  - p30 Share of surveyed Montana tourism businesses reporting increased visitor volume  = **31** percent of surveyed businesses (2025-01-01..2025-12-31) [keep: ] quote: "Only 31% of businesses reported increased visitor volume in 2025 compared to 43% in 2024"
  - p31 Share of surveyed Montana tourism businesses reporting increased visitor volume  = **43** percent of surveyed businesses (2024-01-01..2024-12-31) [keep: ] quote: "Only 31% of businesses reported increased visitor volume in 2025 compared to 43% in 2024"
  - p32 Share of surveyed Montana tourism businesses experiencing visitor volume decline = **44** percent of surveyed businesses (2025-01-01..2025-12-31) [keep: ] quote: "those experiencing declines rose sharply from 27% to 44%"
  - p33 Share of surveyed Montana tourism businesses experiencing visitor volume decline = **27** percent of surveyed businesses (2024-01-01..2024-12-31) [keep: ] quote: "those experiencing declines rose sharply from 27% to 44%"
  - p34 Share of surveyed Montana tourism businesses expecting customer volume to increa = **81** percent of surveyed businesses (2025-01-01..2025-12-31) [keep: ] quote: "although 81% expect customer volume to increase or remain steady in 2025, this marks a decline from 87% last year"
  - p35 Share of surveyed Montana tourism businesses anticipating no change in customer  = **44** percent of surveyed businesses (2025-01-01..2025-12-31) [keep: ] quote: "with 44% anticipating no change at all"
- `https://www.sheridanwyoming.org/wp-content/uploads/2026/08/2026-Q3-Summer-Industry-Update-WEB.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 7 (period_end missing or unparseable: 7)

### d8 [attention] Search and social media interest

Hypothesis: Online attention (search volume, social media mentions) for Yellowstone correlates with visitation; changes in attention from previous years can indicate direction of change.

Queries issued by the searcher: Google Trends Yellowstone National Park September search interest; NPS Visitor Use Statistics Monthly Public Use Report Yellowstone recreation visits; Google Trends search interest correlates national park visitation study; Yellowstone September 2026 visitation forecast park visits

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nypost.com/2026/09/05/us-news/10-best-national-parks-in-america-ranked-as-yellowstone-no-1/` -> **snapshot** (snapshot 20260906015105); points raw/verified 15/0
- `https://www.sciencedirect.com/science/article/abs/pii/S0301479719306048` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/DataStore/DownloadFile/759491` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end missing or unparseable: 15)

### b1 [own_history] NPS monthly visitation statistics

Hypothesis: Obtaining Yellowstone September recreation visits for 2024 and 2025 would extend the recent September series and materially reduce uncertainty in the 2026 anchor. The current series jumps from 2023 to the target year, so a 2024/2025 observation would reveal whether the post-2023 level persisted or reverted.

Queries issued by the searcher: Yellowstone National Park September 2025 recreation visits NPS visitor use statistics; Yellowstone September 2024 visitation 800,000 NPS monthly report; NPS Visitor Use Statistics Monthly Public Use Report Yellowstone 2024; Yellowstone visitation statistics September 2023 record

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://home.nps.gov/yell/learn/news/26004.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] NPS-wide or large-park monthly visitation

Hypothesis: A 2024-2025 September trend for total NPS recreation visits or for a comparable large western park (e.g., Grand Teton, Glacier) would provide a signal to scale the 2023 Yellowstone September level to 2026. This would unlock a yoy_scaling or ratio method that is currently impossible because no 2024/2025 signal is kept.

Queries issued by the searcher: Yellowstone National Park September 2024 visitation recreation visits; Grand Teton September 2025 visitation record NPS; Grand Teton National Park September 2025 visitation 617,970 recreation visits; Glacier National Park September 2025 visitation statistics recreation visits

- `https://home.nps.gov/yell/learn/news/24036.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://buckrail.com/grand-teton-national-park-visitation-slows-in-september/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jhnewsandguide.com/news/business/market_watch/market-watch-airport-traffic-at-all-time-high-shutdown-nixes-park-visitation-data/article_1d` -> **snapshot** (snapshot 20251203013351); points raw/verified 15/15
  - p36 Jackson Hole Airport September 2025 enplanements = **67,452** enplanements (passengers boarding commercial airline flights (2025-09-01..2025-09-30) [keep: ] quote: "In September, enplanements at Jackson Hole Airport totaled 67,452, 21.2% more than the number of passengers who enplaned a commercial airline flight in September 2024."
  - p37 Jackson Hole Airport September 2025 enplanements year-over-year increase vs Sept = **21.2** % (2025-09-01..2025-09-30) [keep: ] quote: "In September, enplanements at Jackson Hole Airport totaled 67,452, 21.2% more than the number of passengers who enplaned a commercial airline flight in September 2024."
  - p38 Jackson Hole Airport fiscal year ending September 2025 enplanements total = **574,456** enplanements (passengers boarding commercial airline flights (2024-10-01..2025-09-30) [keep: ] quote: "During the fiscal year ending September 2025, enplanements totaled 574,456, a 10.7% increase over the previous 12 months."
  - p39 Jackson Hole Airport fiscal year ending September 2025 enplanements increase ove = **10.7** % (2024-10-01..2025-09-30) [keep: ] quote: "During the fiscal year ending September 2025, enplanements totaled 574,456, a 10.7% increase over the previous 12 months."
  - p40 Grand Teton National Park August 2025 recreational visitation total = **735,593** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p41 Grand Teton National Park August 2025 recreational visitation increase vs August = **2.6** % (2025-08-01..2025-08-31) [keep: ] quote: "In August, Grand Teton's recreational visitation total was 735,593, 2.6% more than the number visiting in August 2024."
  - p42 Grand Teton National Park August 2025 visitation increase over previous busiest  = **2.6** % (2025-08-01..2025-08-31) [DISCARD: Redundant with p41; both describe the same August 2025 Grand Teton increase.] quote: "Historically, August 2025 was the park's busiest-ever August, 2.6% ahead of the previous leader, August 2017."
  - p43 Grand Teton National Park fiscal year ending August 2025 recreational visits tot = **3,730,599** recreation visits (2024-09-01..2025-08-31) [keep: ] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p44 Grand Teton National Park fiscal year ending August 2025 recreational visits inc = **4.8** % (2024-09-01..2025-08-31) [DISCARD: Redundant with p43; the percentage change is already implied by the level and prior-year comparison.] quote: "During the fiscal year ending in August 2025, 3,730,599 people paid a recreational visit to Grand Teton, 4.8% more than visited during the preceding 12 months."
  - p45 Yellowstone National Park August 2025 recreational visitation total = **881,936** recreation visits (2025-08-01..2025-08-31) [keep: ] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p46 Yellowstone National Park August 2025 recreational visitation increase vs August = **1.2** % (2025-08-01..2025-08-31) [DISCARD: Redundant with p45; the percentage change is already implied by the level and prior-year comparison.] quote: "The August visitation count for Yellowstone totaled 881,936, 1.2% more than visited in August 2024."
  - p47 Yellowstone National Park August 2021 recreational visitation (busiest August on = **921,844** recreation visits (2021-08-01..2021-08-31) [keep: ] quote: "Perhaps surprisingly, this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p48 Yellowstone National Park August 2017 recreational visitation (second-busiest Au = **916,166** recreation visits (2017-08-01..2017-08-31) [DISCARD: Historical August 2017 level is not needed for September 2026 estimation and is redundant context.] quote: "Perhaps surprisingly, this was only the third-busiest August, trailing only 2021 (921,844) and 2017 (916,166)."
  - p49 Yellowstone National Park fiscal year ending August 2025 recreational visits tot = **4,797,970** recreation visits (2024-09-01..2025-08-31) [keep: ] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
  - p50 Yellowstone National Park fiscal year ending August 2025 recreational visits inc = **2.3** % (2024-09-01..2025-08-31) [DISCARD: Redundant with p49; the percentage change is already implied by the level and prior-year comparison.] quote: "During the fiscal year ending in August 2025, 4,797,970 people paid a recreational visit to Yellowstone, 2.3% more than during the previous year."
- `https://www.outdoornews.com/2026/04/28/visitation-solid-at-national-parks-in-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] Yellowstone operations and access

Hypothesis: Identifying any 2026 road closures, reservation requirements, wildfire impacts, or construction in Yellowstone would resolve whether September 2026 should be adjusted up or down from the recent baseline. This is the largest single uncertainty in the estimate.

Queries issued by the searcher: Yellowstone National Park 2026 road construction closures September; Yellowstone 2026 reservation requirement entrance; Yellowstone September 2026 visitation statistics record; Yellowstone National Park wildfire September 2026 closure

- `https://www.tripadvisor.com/ShowTopic-g60999-i481-k15514679-Spring_Summer_2026_Temporary_YNP_Road_Closure_Alerts-Yellowstone_National_Park_Wyoming.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://roadconditions.com/Bozeman-to-Yellowstone-National-Park` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsfromthestates.com/article/what-expect-wyomings-grand-teton-yellowstone-parks-summer-kicks` -> **snapshot** (snapshot 20260708163950); points raw/verified 12/6
  - p51 Yellowstone National Park annual recreation visits in 2025 = **4,760,000** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p52 Yellowstone National Park annual recreation visits in 2024 = **4,740,000** recreation visits (2024-01-01..2024-12-31) [keep: ] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p53 Yellowstone National Park annual recreation visits in 2021 = **4,860,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: 2021 annual total is historical context but not needed for the 2026 September estimate; p51 and p52 provide the recent a] quote: "In 2025, Yellowstone tallied 4.76 million recreation visits, up slightly from 4.74 million in 2024 but still shy of 4.86 million in 2021."
  - p54 Grand Teton National Park annual recreation visits in 2025 = **3,800,000** recreation visits (2025-01-01..2025-12-31) [keep: ] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p55 Grand Teton National Park annual recreation visits in 2024 = **3,600,000** recreation visits (2024-01-01..2024-12-31) [DISCARD: Grand Teton 2024 annual total is not needed for the Yellowstone September estimate.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
  - p56 Grand Teton National Park highest-ever annual recreation visits in 2021 = **3,880,000** recreation visits (2021-01-01..2021-12-31) [DISCARD: Grand Teton 2021 peak annual total is not needed for the Yellowstone September estimate.] quote: "Grand Teton National Park, meanwhile, clocked 3.8 million recreation visits in 2025, up from 3.6 million in 2024 but down from its highest-ever annual visitation of 3.88 million in 2021."
- `https://www.codyenterprise.com/news/local/article_6fd5d467-1e38-4c12-b0c7-e384ed34d688.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period_end missing or unparseable: 2; period_end 2026-09-07 after as_of: 1; number: no number in value_as_written: 2; number: more than one number in value_as_written: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone september visits', 'yellowstone visitation 2026', 'nps monthly visits']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] These are the same quantity (Yellowstone September recreation visits) for three different years, all from the same NPS source and snapshot. They are not independent measurements of the same period, bu
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9'] These are year-to-date through September totals for different years from the same NPS source. They are not September-only values and cannot be substituted for the target, but they provide context on a
- corroborating: ['p10', 'p11', 'p12', 'p13'] These are year-over-year percentage changes derived from the same NPS September and year-to-date counts. They are redundant with p1-p6 for level estimation but useful as directional context. They are 
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] These are monthly averages and shares for 2014-2018 from the same NPS seasonal table. They are internally consistent and describe the pre-2020 seasonal shape. They are older than the recent September 
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35'] These are Montana tourism survey and border-crossing indicators for 2024-2025. They are not Yellowstone-specific and cover a different geography and period, but they consistently point to softer touri
- contextual: ['p14'] Pebble Creek Campground closure is a specific capacity constraint from the 2022 floods. It is a small campground and its effect on total September recreation visits is likely minor, but it is a real s
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] All are NPS-reported Yellowstone September recreation visits for 2019, 2022, and 2023. They are the same quantity and definition, but different years; they form the only direct September history and s
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9'] These are Yellowstone year-to-date recreation visits through September for 2018-2023. They are consistent with the September monthly values and provide context on annual level and trend, but they are 
- corroborating: ['p10', 'p11', 'p12', 'p13'] These are derived year-over-year percentage changes from the same NPS release. They corroborate the levels in p1-p6 but are redundant transformations, not independent measurements.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] These are NPS 2014-2018 average monthly visitation and shares for Yellowstone. They are internally consistent and provide a seasonal-share route, but the 2014-2018 base predates the 2021-2023 visitati
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50'] These are Yellowstone August 2025 and fiscal-year 2025 visitation figures from a Jackson Hole News & Guide article. They are consistent with the NPS annual totals in p51-p53 and indicate that 2025 vis
- corroborating: ['p51', 'p52', 'p53'] These are Yellowstone annual recreation visits for 2021, 2024, and 2025. They are rounded but consistent with the fiscal-year and monthly evidence, and they establish that 2024-2025 annual visitation 
- corroborating: ['p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] These are Grand Teton and Jackson Hole Airport indicators for 2025. They show strong regional tourism in September 2025, but they are for a different park and a different measurement (enplanements), s
- conflicting: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35'] These Montana tourism survey and border-crossing indicators point to weaker Canadian cross-border travel and softer business sentiment in 2025. They conflict directionally with the strong Jackson Hole
- contextual: ['p14'] Pebble Creek Campground closure is a specific capacity constraint from the 2022 flood. It is a real shock but affects a small share of total Yellowstone capacity and is not quantified in visits.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 Yellowstone visits relative to September 2023 | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m1 (m1) | September 2023 is the most recent observed September level (p1). Annual 2024 and 2025 visitation was roughly flat versus 2023 (p51, p52), and August 2025 was only 1.2% above August 2024 (p45, p46). Regional indicators are mixed: strong Jackson Hole/Grand Teton 2025 signals (p36-p44) versus weaker Mo | No major 2026 Yellowstone closure, wildfire, reservation change, or economic shock materially alters September visitation relative to the 2023-2025 regime. | Evidence of a large 2026 road closure, wildfire, reservation requirement, or a sharp national/regional travel recession that would move September 2026 well outside the 0.85-1.15 range. |
| a2 | September share of Yellowstone annual recreation visits in 2026 | 0.165 | 0.14..0.19 | 0.1153..0.2307 (widened) | fraction | unused | The NPS 2014-2018 average September share was 16.51% (p16). The 2021-2023 visitation regime may have shifted seasonality, so the share is uncertain. A central value of 16.5% with a 14-19% range is consistent with the historical share and allows for modest post-2020 seasonal change. | The seasonal distribution of Yellowstone visitation in 2026 is broadly similar to the 2014-2018 average, with no extreme September-specific disruption. | Evidence that September 2024 or 2025 accounted for a share far outside 14-19% of annual visits, or a major change in park operating season. |

Rejected by code:

- a3 Yellowstone 2026 annual recreation visits: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 831,377 | ['p1'] / ['a1'] | [] |  | 0.50 | median_of_backtested |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |
| m3 | series_naive | 838,458 |  | [2022, 2023] | 0.295 | 0.50 | backtest |  |

Result: central **834,910**, 80% interval [561,207, 1,242,100], basis historical_errors, weight rule inverse_backtest_error, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for recreation visits to Yellowstone National Park during September 2026, as reported in NPS monthly visitation statistics, is 834,910, with an interval of 561,207 to 1,242,100 (80%, historical errors). The combination averages 2 methods: a formula-based estimate of 831,377 at weight 50% and a naive September anchor of 838,458 at weight 50%. The naive method's backtest error was 34.3%. The formula method scales the most recent observed September level by an assumed change factor of 1 (range 0.6991 to 1.398). Observed inputs are limited to past September and annual totals; the [n] change factor is an assumption, not an observation. The interval is model-based and conditional on those assumptions, not a demonstrated accuracy guarantee. The main risk is a [n]-specific shock or a seasonal-share shift. Missing September 2024 and 2025 actuals would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 Yellowstone visits relative to September 2023: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m1. Overturned by: Evidence of a large [n] road closure, wildfire, reservation requirement, or a sharp national/regional travel recession that would move September 2026 well outside the [n]-[n] range.

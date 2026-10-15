# Evidence ledger: fc_yell_2026_09

- Question: Assume today is 2026-09-06. You know nothing published after this date. Estimate the number of recreation visits to Yellowstone National Park in September 2026, as it will be reported in the National Park Service's official monthly visitation statistics.
- as_of: 2026-09-06
- Pinned target: Recreation visits to Yellowstone National Park as reported in the National Park Service's official monthly visitation statistics (NPS Monthly Public Use Report). A recreation visit is one person entering the park for recreational purposes; the same person entering multiple times on separate occasion | unit recreation visits (count) | period 2026-09-01..2026-09-30 | publisher National Park Service (NPS), Public Use Statistics Office / Social Science Program

- Official value (scoring only, never shown to the agent): 868,450

## Directions and pages

### d1 [related_series] NPS year-to-date and recent monthly data for 2026

Hypothesis: Year-to-date 2026 visitation through July or August, combined with the historical share of September in the annual total, yields an estimate for September 2026. If 2026 YTD is above/below recent years, September may follow a similar deviation.

Queries issued by the searcher: Yellowstone National Park 2026 year to date visitation statistics; NPS Yellowstone monthly public use report 2026 recreation visits; Yellowstone September visitation 839,579 2025 monthly recreation visits history; Yellowstone National Park monthly visitation September share annual total statistics table

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/yellowstone-july-visits-fall-2-from-2025-down-11-from-record-2021` -> **snapshot** (snapshot 20260812104051); points raw/verified 10/10
  - p1 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "The park hosted 958,706 recreation visits in July 2026, down 2% from July 2025"
  - p2 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 2% from July 2025, when Yellowstone recorded 975,109 recreation visits"
  - p3 Yellowstone National Park recreation visits, July 2021 (record July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "down 11% from July 2021, when the park logged 1,080,767 recreation visits"
  - p4 Yellowstone National Park recreation visits, record-breaking year 2021 annual to = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "record-breaking year, with more than 4.8 million recreation visits and the busiest July on record"
  - p5 Yellowstone National Park year-to-date recreation visits through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, Yellowstone has hosted 2,635,384 recreation visits."
  - p6 Yellowstone National Park year-to-date recreation visits through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "down 1% from the same point in 2025, when the park recorded 2,666,031 recreation visits"
  - p7 Yellowstone National Park year-to-date recreation visits through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "down 1% from 2021, when it had 2,668,765 recreation visits"
  - p8 Yellowstone National Park year-to-date recreation visits through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p9 Yellowstone National Park year-to-date recreation visits through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p10 Yellowstone National Park year-to-date recreation visits through July 2022 (floo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event."
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [shocks] Park closures, weather, and access restrictions

Hypothesis: Any closures or access restrictions in September 2026 (e.g., road closures, wildfires, government shutdown, flood recovery) would reduce visitation relative to the historical pattern. Conversely, a major anniversary or promotion could increase it. The direction and magnitude of the shock must be estimated from news and official announcements.

Queries issued by the searcher: Yellowstone National Park September 2026 closures road conditions; Yellowstone visitation impact 2022 flood September monthly visitation NPS; Yellowstone National Park visitation 2026 record attendance news release; Yellowstone wildfire closure September 2026

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/0
- `https://www.nps.gov/yell/learn/news/26016.htm` -> **snapshot** (snapshot 20260714213711); points raw/verified 11/11
  - p11 Yellowstone National Park recreation visits, June 2026 = **903,025** recreation visits (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p12 Yellowstone National Park recreation visits, June 2025 = **928,250** recreation visits (2025-06-01..2025-06-30) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 903,025 recreation visits in June 2026, down 3% from June 2025 (928,250 recreation visits)."
  - p13 Yellowstone National Park recreation visits, June 2021 = **938,845** recreation visits (2021-06-01..2021-06-30) [EXCLUDED (ablation): ] quote: "Visitation in June 2026 showed a 4% decrease from June 2021 (938,845 recreation visits)."
  - p14 Yellowstone National Park record-breaking year 2021 recreation visits = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "The park's record-breaking year was 2021 with over 4.8 million recreation visits."
  - p15 Yellowstone National Park year-to-date recreation visits through June 2026 = **1,676,678** recreation visits (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p16 Yellowstone National Park year-to-date recreation visits through June 2025 = **1,690,922** recreation visits (2025-01-01..2025-06-30) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p17 Yellowstone National Park year-to-date recreation visits through June 2021 = **1,587,998** recreation visits (2021-01-01..2021-06-30) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 1,676,678 recreation visits, down 1% from 2025 (1,690,922 recreation visits), and up 6% from 2021 (1,587,998 recreation visits)."
  - p18 Yellowstone National Park year-to-date recreation visits through June 2024 = **1,633,739** recreation visits (2024-01-01..2024-06-30) [EXCLUDED (ablation): ] quote: "2024 - 1,633,739"
  - p19 Yellowstone National Park year-to-date recreation visits through June 2023 = **1,492,843** recreation visits (2023-01-01..2023-06-30) [EXCLUDED (ablation): ] quote: "2023 - 1,492,843"
  - p20 Yellowstone National Park year-to-date recreation visits through June 2022 = **1,258,834** recreation visits (2022-01-01..2022-06-30) [EXCLUDED (ablation): ] quote: "2022 - 1,258,834 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p21 Yellowstone National Park year-to-date recreation visits through June 2021 (list = **1,587,998** recreation visits (2021-01-01..2021-06-30) [EXCLUDED (ablation): ] quote: "2021 - 1,587,998"
- `https://trib.com/news/state-regional/yellowstone-visits-decline-in-september-park-headed-toward-lowest-visitation-in-9-years/article_14ddc944-e598-583` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 2; period_end 2026-10-31 after as_of: 4; number: no number in value_as_written: 4; number: more than one number in value_as_written: 1; period_end 2026-12-31 after as_of: 1; period_end 2026-10-12 after as_of: 1)

### d3 [base_rates] Seasonal share of September in annual visitation

Hypothesis: The share of annual recreation visits occurring in September is relatively stable across years (e.g., 10-12%). Multiplying a forecast of 2026 annual visitation by this share gives a September estimate. Annual visitation can be forecast from 2026 YTD and historical growth rates.

Queries issued by the searcher: Yellowstone National Park monthly visitation statistics September recreation visits; Yellowstone annual visitation 2024 record 4.7 million NPS; Yellowstone National Park August 2026 visitation statistics year-to-date; Yellowstone 2025 annual visitation total recreation visits 4.7 million

- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.miamiherald.com/living/article317328753.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nbcmontana.com/news/local/recreation-visits-up-3-from-2025-in-yellowstone` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] Park entrances and vehicle counts

Hypothesis: Recreation visits can be estimated from vehicle entries at park entrances multiplied by average occupancy, adjusted for non-recreation entries and seasonality. September vehicle counts and occupancy rates may be available from traffic counters or entrance station data.

Queries issued by the searcher: Yellowstone entrance vehicle counts September visitation statistics; Yellowstone average occupancy persons per vehicle visitation study; Yellowstone September 2025 recreation visits record NPS; Yellowstone persons per vehicle multiplier 2.58 table by month PPV

- `https://irma.nps.gov/Stats/FileDownload/43470` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.tripadvisor.com.au/ShowTopic-g60999-i481-k15386767-West_entrance_wait_times-Yellowstone_National_Park_Wyoming.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yellowstonegate.com/?p=7848` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] Lodging, campground, and gateway community occupancy

Hypothesis: September visitation is constrained by available lodging and campground capacity and their occupancy rates. Total overnight stays plus day-use visits can be estimated from accommodation capacity and utilization, then converted to recreation visits using average length of stay and day-trip ratios.

Queries issued by the searcher: Yellowstone lodging occupancy September statistics; Yellowstone National Park campground capacity number of sites lodges rooms; Yellowstone National Park September 2025 visitation 839,579 NPS release; Yellowstone lodges number of rooms Xanterra 2000 rooms nine lodges capacity

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cz/zpr%C3%A1vy/%C4%8Dl%C3%A1nek/yellowstone-tourism-surges-during-shoulder-season-as-hotels-and-lodges-maintain-strong-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nationalparkstraveler.org/parks/yellowstone-national-park/camping-yellowstone` -> **snapshot** (snapshot 20250327165432); points raw/verified 15/0
- dropped by code checks: 15 (period_end missing or unparseable: 15)

### d6 [forecasts_markets] Published tourism forecasts and prediction markets

Hypothesis: Any published forecast for Yellowstone 2026 visitation or prediction market on September 2026 visitation could provide a direct estimate or a range. These may incorporate expert judgment and current conditions.

Queries issued by the searcher: Yellowstone 2026 visitation forecast; prediction market Yellowstone visitation 2026; Yellowstone tourism outlook 2026; Yellowstone National Park September visitation statistics record

- `https://www.coinrithm.com/en/prediction-markets/kalshi/kxyellvisits-27mar31` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gtg.webhost.uoradea.ro/PDF/GTG-2-2026/gtg.65204-1709.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelandtourworld.pl/aktualno%C5%9Bci/artyku%C5%82/63ykvnvt60ul/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wyomingpublicmedia.org/natural-resources-energy/2026-07-14/yellowstone-visitation-went-down-in-june` -> **snapshot** (snapshot 20260725002223); points raw/verified 11/5
  - p22 Yellowstone National Park recreation visits in June (NPS reported) = **903,025** people (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "The National Park Service (NPS) says 903,025 people visited Yellowstone National Park in June."
  - p23 Yellowstone June visitation change vs June of 2025 = **3** % (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "That number is 3% lower than in June of 2025."
  - p24 Yellowstone record visitation in 2021 (busiest year on record) = **4,800,000** visitors (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was the busiest year on record with more than 4.8 million visitors."
  - p25 Grand Teton National Park visitors in June = **798,286** visitors (2026-06-01..2026-06-30) [DISCARD: Different park (Grand Teton) and different month (June 2026); no defensible conversion to Yellowstone September 2026 rec] quote: "Grand Teton National Park also saw a decrease this month at 798,286 visitors."
  - p26 U.S. inflation rate in May = **4.2** % (2026-05-01..2026-05-31) [DISCARD: Macroeconomic inflation rate for May 2026; no established quantitative bridge to Yellowstone September visitation and no] quote: "U.S. inflation hit 4.2% in May, the highest since April of 2023."
- dropped by code checks: 6 (period_end missing or unparseable: 6)

### d7 [attention] Search and social media interest in Yellowstone

Hypothesis: Google Trends or social media mentions for Yellowstone in September 2026 may correlate with visitation, but the relationship is noisy and not a direct conversion. Use only as a directional check if other routes are uncertain.

Queries issued by the searcher: Google Trends search interest Yellowstone National Park visitation correlation monthly; Yellowstone National Park September visitation statistics 2024 2025 NPS monthly public use report; Yellowstone National Park August 2026 visitation statistics NPS release; Google Trends Yellowstone National Park search interest September 2026

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26022.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://businessupturn.com/usa/lifestyle/travel/most-searched-national-park-every-state-2026-yellowstone/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.outsideonline.com/adventure-travel/national-parks/top-searched-national-parks/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] NPS monthly visitation statistics

Hypothesis: Yellowstone monthly recreation visits for January through August 2026, if published before the cutoff, would anchor a seasonal-share route (d1/d3) and allow a 2026 YTD level to be multiplied by the historical September share. Without these, the estimate must rely on older annual or monthly patterns.

Queries issued by the searcher: Yellowstone National Park monthly visitation 2026 recreation visits; NPS Monthly Public Use Report 2026 Yellowstone visitation statistics; nps.gov Yellowstone visitation statistics for July 2026 news release; Yellowstone September 2025 visitation statistics 839,579 recreation visits

- `https://www.nps.gov/yell/learn/news/26019.htm` -> **snapshot** (snapshot 20260814204347); points raw/verified 10/10
  - p27 Yellowstone National Park recreation visits, July 2026 = **958,706** recreation visits (2026-07-01..2026-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p28 Yellowstone National Park recreation visits, July 2025 = **975,109** recreation visits (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "Yellowstone National Park hosted 958,706 recreation visits in July 2026, down 2% from July 2025 (975,109 recreation visits)."
  - p29 Yellowstone National Park recreation visits, July 2021 (record busiest July) = **1,080,767** recreation visits (2021-07-01..2021-07-31) [EXCLUDED (ablation): ] quote: "Visitation in July 2026 showed an 11% decrease from July 2021 (1,080,767 recreation visits), which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July o"
  - p30 Yellowstone National Park recreation visits, year-to-date through July 2026 = **2,635,384** recreation visits (2026-01-01..2026-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p31 Yellowstone National Park recreation visits, year-to-date through July 2025 = **2,666,031** recreation visits (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p32 Yellowstone National Park recreation visits, year-to-date through July 2021 = **2,668,765** recreation visits (2021-01-01..2021-07-31) [EXCLUDED (ablation): ] quote: "So far in 2026, the park has hosted 2,635,384 recreation visits, down 1% from 2025 (2,666,031 recreation visits), and down 1% from 2021 (2,668,765 recreation visits)."
  - p33 Yellowstone National Park recreation visits, year-to-date through July 2024 = **2,626,091** recreation visits (2024-01-01..2024-07-31) [EXCLUDED (ablation): ] quote: "2024 - 2,626,091"
  - p34 Yellowstone National Park recreation visits, year-to-date through July 2023 = **2,462,535** recreation visits (2023-01-01..2023-07-31) [EXCLUDED (ablation): ] quote: "2023 - 2,462,535"
  - p35 Yellowstone National Park recreation visits, year-to-date through July 2022 (flo = **1,855,396** recreation visits (2022-01-01..2022-07-31) [EXCLUDED (ablation): ] quote: "2022 - 1,855,396 (The park was closed June 13 through June 21 due to the historic flood event. Three entrances opened on June 22.)"
  - p36 Yellowstone National Park annual recreation visits, 2021 record-breaking year = **4,800,000** recreation visits (2021-01-01..2021-12-31) [EXCLUDED (ablation): ] quote: "which was Yellowstone's record-breaking year with over 4.8 million recreation visits and the busiest July on record."
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsfromthestates.com/article/yellowstone-national-park-visitation-ticks-down-slightly-pace-third-busiest-year` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=403bc337-c90a-4e9e-95f6-09a36155174d&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fM` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [shocks] Park access and operations

Hypothesis: Any September 2026 road closures, wildfire impacts, government shutdown, or flood-recovery restrictions would materially change September visitation relative to the historical seasonal share. This would resolve the largest uncertainty in the seasonal-share route.

Queries issued by the searcher: Yellowstone National Park September 2026 road closures wildfire; Yellowstone road status 2026 construction closures; Yellowstone National Park visitation statistics September 2025 monthly public use report; Yellowstone National Park operating status 2026 flood recovery

- `https://www.nps.gov/yell/planyourvisit/parkroads.htm` -> **snapshot** (snapshot 20260906063912); points raw/verified 15/5
  - p37 Yellowstone West Entrance to Madison, Madison to Old Faithful, Madison to Norris = **17** date (2026-04-17..2026-04-17) [keep: ] quote: "Open April 17 - October 31, 2026: West Entrance to Madison, Madison to Old Faithful, Madison to Norris, Mammoth Hot Springs to Norris, Norris to Canyon Village"
  - p38 Yellowstone East Entrance to Fishing Bridge (Sylvan Pass) and Canyon Village to  = **1** date (2026-05-01..2026-05-01) [keep: ] quote: "Open May 1 - October 31, 2026: East Entrance to Fishing Bridge (Sylvan Pass), Canyon Village to Bridge Bay"
  - p39 Yellowstone South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass = **8** date (2026-05-08..2026-05-08) [keep: ] quote: "Open May 8 - October 31, 2026: South Entrance to West Thumb, West Thumb to Old Faithful (Craig Pass), West Thumb to Lake Village, Tower-Roosevelt to Tower Fall"
  - p40 Yellowstone Canyon Village to Tower Fall (Dunraven Pass) road opening date (proj = **22** date (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Canyon Village to Tower Fall (Dunraven Pass)."
  - p41 Beartooth Highway (US-212) and Chief Joseph Scenic Byway (WY-296) opening date ( = **22** date (2026-05-22..2026-05-22) [keep: ] quote: "Open May 22 - October 12, 2026: Beartooth Highway (US-212), Chief Joseph Scenic Byway (WY-296)."
- `https://www.nps.gov/yell/learn/management/current-fire-activity.htm` -> **snapshot** (snapshot 20260722025734); points raw/verified 6/1
  - p42 Yellowstone fire activity table last updated date = **21** day of month (July) (2026-07-21..2026-07-21) [DISCARD: A page-update date, not a fire-impact measurement; it carries no numeric information usable in a formula and is supersed] quote: "Last updated: July 21, 2026"
- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=67167d69-7e8e-4356-b91c-30e3e61ca29c&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fS` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://local.newsbreak.com/news/4863047323691-yellowstone-and-grand-teton-fall-guide-plan-around-fire-road-and-service-changes` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end 2026-10-31 after as_of: 4; period_end 2026-10-12 after as_of: 2; period_end 2026-11-30 after as_of: 2; period_end 2026-09-30 after as_of: 1; period_end 2026-12-31 after as_of: 1; missing quote or value_as_written: 1; period_end missing or unparseable: 4)

### b3 [base_rates] Historical seasonal share

Hypothesis: The historical share of annual Yellowstone recreation visits occurring in September is needed to convert a 2026 annual or YTD forecast into a September estimate. A stable multi-year share would make the seasonal-share route executable even without 2026 monthly data.

Queries issued by the searcher: Yellowstone National Park monthly recreation visits September annual totals NPS Public Use Statistics; NPS Public Use Statistics Yellowstone monthly visitation 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024

- `https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=c595a5c7-e6f0-43a6-8e87-68da4b5a880a&_m=Remote&_r=%2fIRMA+Prod%2fSTATS%2fPark+Specific+Reports%2fR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nps.gov/yell/learn/news/26024.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wyomingnews.com/news/local_news/yellowstone-national-park-reports-september-2026-visitation-statistics/article_3df9c932-70de-46b1-b898-372` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://powelltribune.com/stories/yellowstone-national-park-reports-increased-september-visits,178194` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['yellowstone', 'visitation', 'september']: no matching market created on or before as_of markets=0


## Judge

### round 1
- contextual: ['p25', 'p26'] Both come from the same Wyoming Public Media snapshot and concern regional tourism and macroeconomic conditions. p25 is a June 2026 Grand Teton visitor count, useful only as a directional analogue for
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41'] All are 2026 Yellowstone road-opening/closure schedule entries from the same NPS page (snapshot 2026-09-06). They jointly establish that the park's road network is open through September 2026: West En
- contextual: ['p42'] Fire-activity page last updated July 21, 2026, with no indication of a large active fire. Weak, dated signal; it does not establish September 2026 fire conditions, so it can only support the assumptio
- contextual: ['p25', 'p26'] Grand Teton June 2026 visitors (798,286) and May 2026 US inflation (4.2%) come from the same Wyoming Public Media snapshot. They are regional/economic context for the Greater Yellowstone area, not Yel

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 Yellowstone recreation visits as a multiple of the 2019-2025 September average | 1 | 0.85..1.18 | 0.7082..1.416 (widened) | ratio | unused | No 2026 monthly Yellowstone data are available at the cutoff, so the level must be transferred from the historical September base. The road schedule (p37-p41) shows the park fully open through September 2026, and no September 2026 closure, wildfire, or shutdown is documented as of 2026-09-06. The ra | The park remains open through September 2026 with no major new closure, wildfire, or government shutdown, and 2026 demand is broadly in line with the recent 2019-2025 September pattern. | A September 2026 road closure, wildfire evacuation, government shutdown, or credible 2026 YTD data showing a large deviation from the recent September base. |

Rejected by code:

- a2 Average September recreation visits to Yellowstone National Park, 2019-2025: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['yellowstone']; quantity stems: ['recre', 'visit']
- points excluded before the judge: 34 of 42
- methods allowed: ['formula_mc']

  - p1 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p2 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p3 Yellowstone National Park recreation visits, July 2021 (record July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p4 Yellowstone National Park recreation visits, record-breaking year 2021 annual total (more  = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p5 Yellowstone National Park year-to-date recreation visits through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p6 Yellowstone National Park year-to-date recreation visits through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p7 Yellowstone National Park year-to-date recreation visits through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p8 Yellowstone National Park year-to-date recreation visits through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p9 Yellowstone National Park year-to-date recreation visits through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p10 Yellowstone National Park year-to-date recreation visits through July 2022 (flood closures = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p11 Yellowstone National Park recreation visits, June 2026 = 903,025 (2026-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p12 Yellowstone National Park recreation visits, June 2025 = 928,250 (2025-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p13 Yellowstone National Park recreation visits, June 2021 = 938,845 (2021-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p14 Yellowstone National Park record-breaking year 2021 recreation visits = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p15 Yellowstone National Park year-to-date recreation visits through June 2026 = 1,676,678 (2026-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p16 Yellowstone National Park year-to-date recreation visits through June 2025 = 1,690,922 (2025-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p17 Yellowstone National Park year-to-date recreation visits through June 2021 = 1,587,998 (2021-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p18 Yellowstone National Park year-to-date recreation visits through June 2024 = 1,633,739 (2024-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p19 Yellowstone National Park year-to-date recreation visits through June 2023 = 1,492,843 (2023-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p20 Yellowstone National Park year-to-date recreation visits through June 2022 = 1,258,834 (2022-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p21 Yellowstone National Park year-to-date recreation visits through June 2021 (list entry) = 1,587,998 (2021-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p22 Yellowstone National Park recreation visits in June (NPS reported) = 903,025 (2026-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p23 Yellowstone June visitation change vs June of 2025 = 3 (2026-06-30): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p24 Yellowstone record visitation in 2021 (busiest year on record) = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p27 Yellowstone National Park recreation visits, July 2026 = 958,706 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p28 Yellowstone National Park recreation visits, July 2025 = 975,109 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p29 Yellowstone National Park recreation visits, July 2021 (record busiest July) = 1,080,767 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p30 Yellowstone National Park recreation visits, year-to-date through July 2026 = 2,635,384 (2026-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p31 Yellowstone National Park recreation visits, year-to-date through July 2025 = 2,666,031 (2025-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p32 Yellowstone National Park recreation visits, year-to-date through July 2021 = 2,668,765 (2021-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p33 Yellowstone National Park recreation visits, year-to-date through July 2024 = 2,626,091 (2024-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p34 Yellowstone National Park recreation visits, year-to-date through July 2023 = 2,462,535 (2023-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p35 Yellowstone National Park recreation visits, year-to-date through July 2022 (flood closure = 1,855,396 (2022-07-31): ablation: name refers to the target entity ['yellowstone'] and quantity
  - p36 Yellowstone National Park annual recreation visits, 2021 record-breaking year = 4,800,000 (2021-12-31): ablation: name refers to the target entity ['yellowstone'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a2: assumption a2 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

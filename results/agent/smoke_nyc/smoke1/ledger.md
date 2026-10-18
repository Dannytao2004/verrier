# Evidence ledger: smoke_nyc

- Question: What is the average number of taxi and ride-hail trips per day in New York City in October 2026 (yellow taxis, green taxis and high-volume for-hire vehicles combined, as counted by the NYC Taxi & Limousine Commission)?
- as_of: 2026-10-17
- Pinned target: Average daily count of trips by yellow taxis, green taxis (Boro Taxis), and high-volume for-hire vehicles (HVFHV: Uber, Lyft, and similar) in New York City, combined, as recorded in NYC Taxi & Limousine Commission trip-record data | unit trips per day | period 2026-10-01..2026-10-31 | publisher New York City Taxi and Limousine Commission (TLC)

## Directions and pages

### d1 [own_history] TLC data publisher / analyst tracking monthly trip totals

Hypothesis: October 2026 daily average will be close to recent monthly daily averages (e.g., 2024-2025 October and adjacent months) adjusted for trend and seasonality; October typically shows a modest seasonal dip versus summer peak and a rise versus winter trough. The most recent published months before cutoff anchor the level.

Queries issued by the searcher: NYC TLC monthly trip record data yellow taxi green taxi HVFHV totals 2025; TLC taxi and for-hire vehicle trip record data monthly summary dashboard; "TLC Industry Indicators" average daily trips yellow green FHV 2026; NYC TLC factbook monthly trips 2025 yellow taxi HVFHV "average daily trips"

- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://data.cityofnewyork.us/d/c5iv-bn4s` -> **live_dated** (page date 2026-09-25); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` -> **live_dated** (page date 2017-08-09); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d2 [related_series] Component decomposition across vehicle classes

Hypothesis: Combined total = yellow + green + HVFHV; each component has different trend (yellow/green roughly flat or declining, HVFHV growing then plateauing). Estimating each component separately and summing reduces aggregation error and lets us use class-specific recent data.

Queries issued by the searcher: NYC TLC HVFHV trips per month 2025 yellow taxi monthly trips report; TLC monthly trip record data yellow taxi green taxi HVFHV average daily trips; "TLC Industry Indicators" trips_per_day license_class yellow green FHV 2026 values; NYC TLC factbook yellow taxi trips per day 2025 HVFHV trips per day 2025 monthly

- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/aggregated-reports.page` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nyc.gov/assets/tlc/downloads/pdf/testimony_2_10_25.pdf` -> **live_dated** (page date 2025-02-07); points raw/verified 15/7
  - p1 Yellow taxi trips completed in October 2024 = **3,800,000** trips (2024-10-01..2024-10-31) [keep: ] quote: "the 3.8 million trips completed in October 2024 were the highest since early 2020"
  - p2 Taxi trips completed each month in 2015 (upper bound) = **13,000,000** trips per month (2015-01-01..2015-12-31) [DISCARD: 2015 taxi monthly trips are a pre-rideshare regime far from 2026; unusable for level or near-term trend and risks distor] quote: "with 11-13 million trips completed each month in 2015"
  - p3 Taxi trips completed each month in 2019 (upper bound) = **8,000,000** trips per month (2019-01-01..2019-12-31) [DISCARD: 2019 taxi monthly trips predate HVFHV dominance and congestion pricing; not a valid anchor for 2026 combined level.] quote: "and 6-8 million completed each month in 2019"
  - p4 Active taxis completing a trip in December 2024 = **9,768** taxis (2024-12-01..2024-12-31) [keep: ] quote: "9,768 taxis completed a trip in December of 2024"
  - p5 Active taxis completing a trip in March 2020 = **11,315** taxis (2020-03-01..2020-03-31) [DISCARD: March 2020 active-taxi count is a pandemic-onset artifact; not representative of 2026 capacity.] quote: "the 11,315 that completed a trip in March of 2020"
  - p6 Share of HVFHV trips dispatched to EVs or WAVs by end of 2024 (about) = **20** percent of trips (..2024-12-31) [DISCARD: EV/WAV dispatch share; irrelevant to trip counts.] quote: "by the end of 2024, about 20% of trips were dispatched to EVs or WAVs"
  - p7 Green Rides 2025 benchmark share of HVFHV trips to EVs or WAVs = **15** percent of trips (2025-01-01..2025-12-31) [DISCARD: Green Rides EV/WAV requirement; irrelevant to trip counts.] quote: "outpacing the 15% required in 2025"
- dropped by code checks: 8 (period_end missing or unparseable: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word 'million' not supported by quote or table header: 2; period_end 2030-12-31 after as_of: 1)

### d3 [related_series] Broader for-hire vehicle universe and share bridge

Hypothesis: Total FHV/taxi trips (all classes) times the share attributable to yellow+green+HVFHV gives the target; the excluded classes (black car, livery, luxury) are a small and slowly changing share, so a stable share can bridge.

Queries issued by the searcher: NYC TLC all for-hire vehicle trips by license class monthly; TLC active vehicles by category 2025 black car livery; "TLC Industry Indicators" trips_per_day license_class black car livery 2026; data.cityofnewyork.us TLC active vehicles by category dataset black car livery luxury

- `https://data.cityofnewyork.us/Transportation/TLC-Industry-Indicators/v6kb-cqej/data_preview` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` -> **live_dated** (page date 2017-08-09); points raw/verified 0/0
- `https://www.nyc.gov/assets/tlc/downloads/pdf/preliminary_budget_hearing_testimony_3_19_25.pdf` -> **live_dated** (page date 2025-03-14); points raw/verified 15/8
  - p8 Total trips completed across all TLC-regulated industries, calendar year 2024 = **300,000,000** trips (2024-01-01..2024-12-31) [keep: ] quote: "In calendar year 2024, across all industries, there were over 300 million trips completed."
  - p9 Year-over-year increase in overall trips across all TLC industries, calendar yea = **4.4** percent (2024-01-01..2024-12-31) [keep: ] quote: "In comparison to the previous year, overall trips have increased by 4.4%."
  - p10 High-volume for-hire vehicle (HVFHV) trips completed, calendar year 2024 = **239,000,000** trips (2024-01-01..2024-12-31) [keep: ] quote: "The high-volume for-hire vehicle sector, the largest segment of our regulated industries, completed over 239 million trips in calendar year 2024"
  - p11 High-volume for-hire vehicle (HVFHV) trips completed, calendar year 2023 = **232,000,000** trips (2023-01-01..2023-12-31) [keep: ] quote: "compared to about 232 million in calendar year 2023, representing a 3% increase"
  - p12 Year-over-year increase in HVFHV trips, calendar year 2024 vs 2023 = **3** percent (2024-01-01..2024-12-31) [keep: ] quote: "compared to about 232 million in calendar year 2023, representing a 3% increase"
  - p13 Non-high-volume for-hire vehicle trips completed, calendar year 2024 = **19,700,000** trips (2024-01-01..2024-12-31) [keep: ] quote: "non-high-volume for-hire vehicles continue to show signs of progress as well, completing 19.7 million trips in calendar year 2024"
  - p14 Year-over-year increase in non-high-volume for-hire vehicle trips, calendar year = **18** percent (2024-01-01..2024-12-31) [keep: ] quote: "This is an 18% increase compared to calendar year 2023."
  - p15 Year-over-year increase in taxi trips, calendar year 2024 vs 2023 = **7.5** percent (2024-01-01..2024-12-31) [keep: ] quote: "Taxi trips have increased by 7.5% from calendar year 2023 to calendar year 2024."
- `https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=sOzgSHMzBUKpp/GOQYUYJQ==` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 7 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3; period_end missing or unparseable: 4)

### d4 [capacity_consumption] Fleet capacity and utilisation

Hypothesis: Daily trips = active vehicles × trips per vehicle per day (utilisation). Active HVFHV and taxi counts are published; trips per vehicle per day can be derived from recent data and held roughly constant, giving an independent capacity-based estimate.

Queries issued by the searcher: NYC TLC active vehicles high volume for-hire 2025 monthly driver vehicle counts; NYC TLC trips per vehicle per day yellow taxi HVFHV 2024 report; "TLC Industry Indicators" trips_per_day vehicles_per_day FHV 2025 data.cityofnewyork.us; MTA Congestion Relief Zone first evaluation report active HVFHV vehicles Figure 3-1 yellow taxi active vehicles 2025

- `https://data.cityofnewyork.us/Transportation/TLC-Industry-Indicators/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nyc.gov/assets/tlc/downloads/pdf/testimony_2_10_25.pdf` -> **live_dated** (page date 2025-02-07); points raw/verified 15/7
  - p16 Yellow taxi trips completed in October 2024 = **3,800,000** trips (2024-10-01..2024-10-31) [DISCARD: Exact duplicate of p1 (same 3.8M Oct 2024 yellow trips); adds no information.] quote: "the 3.8 million trips completed in October 2024 were the highest since early 2020"
  - p17 Active taxis that completed a trip in December 2024 = **9,768** taxis (vehicles) (2024-12-01..2024-12-31) [DISCARD: Duplicate of p4 (9,768 active taxis Dec 2024).] quote: "9,768 taxis completed a trip in December of 2024, which is the highest number of active taxis since the 11,315 that completed a trip in March of 2020."
  - p18 Active taxis that completed a trip in March 2020 = **11,315** taxis (vehicles) (2020-03-01..2020-03-31) [DISCARD: Duplicate of p5 (11,315 active taxis Mar 2020).] quote: "the highest number of active taxis since the 11,315 that completed a trip in March of 2020"
  - p19 Monthly taxi trips completed in 2015 (upper bound) = **13,000,000** trips per month (2015-01-01..2015-12-31) [DISCARD: Duplicate of p2 (2015 monthly taxi trips upper bound).] quote: "with 11-13 million trips completed each month in 2015 and 6-8 million completed each month in 2019"
  - p20 Monthly taxi trips completed in 2019 (upper bound) = **8,000,000** trips per month (2019-01-01..2019-12-31) [DISCARD: Duplicate of p3 (2019 monthly taxi trips upper bound).] quote: "6-8 million completed each month in 2019"
  - p21 Share of HVFHV trips dispatched to EVs or WAVs by end of 2024 (about) = **20** % of dispatched trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p6 (EV/WAV share end-2024); not volume-relevant.] quote: "by the end of 2024, about 20% of trips were dispatched to EVs or WAVs, outpacing the 15% required in 2025"
  - p22 Green Rides Initiative required EV/WAV dispatch share for 2025 = **15** % of dispatched trips (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7 (15% Green Rides requirement); not volume-relevant.] quote: "outpacing the 15% required in 2025"
- `https://therideshareguy.com/rsg267/` -> **live_dated** (page date 2025-11-26); points raw/verified 15/4
  - p23 Ride-hail trips per day in NYC as of September 2025 = **647,819** ride-hail trips per day (2025-09-01..2025-09-30) [keep: ] quote: "~647,819 ride-hail trips per day and ~138,644 taxi trips per day as of September 2025"
  - p24 Taxi trips per day in NYC as of September 2025 = **138,644** taxi trips per day (2025-09-01..2025-09-30) [keep: ] quote: "~647,819 ride-hail trips per day and ~138,644 taxi trips per day as of September 2025"
  - p25 Average revenue per ride-hail trip in NYC (estimate) = **35** USD per ride-hail trip (2025-09-01..2025-09-30) [DISCARD: Revenue per ride-hail trip; not a volume input.] quote: "average revenue estimates of ~$35 per ride-hail trip and ~$25 per taxi trip"
  - p26 Average revenue per taxi trip in NYC (estimate) = **25** USD per taxi trip (2025-09-01..2025-09-30) [DISCARD: Revenue per taxi trip; not a volume input.] quote: "average revenue estimates of ~$35 per ride-hail trip and ~$25 per taxi trip"
- dropped by code checks: 19 (period_end missing or unparseable: 9; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word 'million' not supported by quote or table header: 2; scale word 'thousand' not supported by quote or table header: 6)

### d5 [shocks] Policy and calendar effects

Hypothesis: Congestion pricing (started 2025), FHV fee changes, and calendar effects (Halloween, holidays, weather) shift October 2026 volume relative to trend; quantifying the congestion-pricing effect on FHV/taxi trips adjusts the baseline.

Queries issued by the searcher: congestion pricing effect on yellow taxi HVFHV trips 2025 TLC trip data; NYC taxi FHV trip volumes declined after congestion pricing 2025 monthly; "Congestion Relief Zone" first evaluation report average daily trips citywide yellow taxi HVFHV October 2025; TLC 2026 rule for-hire vehicle per-trip fee increase HVFHV minimum pay standard 2026

- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://cdn.crainsnewyork.com/transportation/yellow-cabs-land-more-trips-new-yorks-congestion-pricing-zone` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://findingspress.org/article/155761.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` -> **live_dated** (page date 2017-08-09); points raw/verified 5/3
  - p27 Congestion pricing charge column added to Yellow, Green, and High Volume FHV tri = **2,025** year (2025-01-01..2025-12-31) [DISCARD: Congestion-fee column metadata; no numeric volume content.] quote: "For 2025 data onwards, a cbd_congestion_fee column has been added to the Yellow, Green, and High Volume FHV datasets to reflect new congestion pricing charges."
  - p28 Start date of the $0.30 improvement surcharge on all taxi and SHL trips = **1** day of month (January 1) (2015-01-01..2015-01-01) [DISCARD: 2015 surcharge start date; irrelevant to 2026 volume.] quote: "This is a $0.30 surcharge on all trips to help fund accessibility in taxis and SHLs, which began on January 1, 2015."
  - p29 Year from which high volume trip records (HVFHV) are reported in a separate data = **2,019** year (2019-01-01..2019-12-31) [DISCARD: Dataset-structure note (HVFHV separate since 2019); no numeric volume.] quote: "Since 2019 high volume trip records (HVFHV) are reported in a separate (and more detailed) dataset."
- dropped by code checks: 2 (period_end missing or unparseable: 1; number: no number in value_as_written: 1)

### d6 [base_rates] Seasonality and day-of-week structure

Hypothesis: October daily average = annual daily average × October seasonal index; also weekday/weekend mix affects the mean. Historical monthly seasonal factors for October (relative to annual mean) can transfer if stable.

Queries issued by the searcher: NYC TLC monthly trip totals 2024 full year taxi HVFHV; NYC taxi trips monthly seasonality 2024 2025 October; TLC monthly driver and vehicle numbers trip records December 2024 total trips; "TLC Industry Indicators" average daily trips yellow green FHV monthly 2024 values; NYC for-hire vehicle trips per day 2024 2025 average Uber Lyft yellow taxi combined statistics; TLC Factbook 2025 trips per day yellow taxi HVFHV green taxi annual

- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nyc.gov/site/tlc/about/aggregated-reports.page` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://citymeetings.nyc/meetings/new-york-city-council/2025-03-19-1015-am-committee-on-transportation-and-infrastructure/chapter/tlc-industry-overvie` -> **live_dated** (page date 2025-03-19); points raw/verified 12/9
  - p30 Year-over-year increase in total trips across all industries, 2024 vs 2023 = **4.4** percent (2024-01-01..2024-12-31) [DISCARD: Duplicate of p9 (4.4% all-industry YoY).] quote: "In comparison to the previous year, overall trips have increased by 4.4%."
  - p31 Increase in taxi trips, calendar year 2023 to calendar year 2024 = **7.5** percent (2024-01-01..2024-12-31) [DISCARD: Duplicate of p15 (7.5% taxi YoY).] quote: "Taxi trips have increased by 7.5% from calendar year twenty twenty three to calendar year twenty twenty four."
  - p32 Increase in high-volume for-hire vehicle trips, 2024 vs 2023 = **3** percent (2024-01-01..2024-12-31) [DISCARD: Duplicate of p12 (3% HVFHV YoY).] quote: "compared to about two thirty two million in calendar year 2023 representing a 3% increase."
  - p33 Non-high-volume for-hire vehicle trips completed, calendar year 2024 = **19,700,000** trips (2024-01-01..2024-12-31) [DISCARD: Duplicate of p13 (19.7M non-HVFHV FHV trips).] quote: "Moreover, non high volume for hire vehicles continue to show signs of progress as well, completing 19,700,000 trips in calendar year '24."
  - p34 Increase in non-high-volume for-hire vehicle trips, 2024 vs 2023 = **18** percent (2024-01-01..2024-12-31) [DISCARD: Duplicate of p14 (18% non-HVFHV FHV YoY).] quote: "This is an 18% increase to calendar year '23."
  - p35 Commuter vans in service (current, compared to 34 at beginning of 2024) = **43** vans (..) [DISCARD: Commuter vans in service; outside target scope (yellow+green+HVFHV).] quote: "The commuter van industry is beginning to show signs of recovery with 43 vans in service compared to 34 at the beginning of 2024."
  - p36 Commuter vans in service at beginning of 2024 = **34** vans (2024-01-01..2024-01-01) [DISCARD: Commuter vans baseline; outside target scope.] quote: "with 43 vans in service compared to 34 at the beginning of 2024."
  - p37 Share of yellow taxi drivers estimated to be full time (lower bound) = **70** percent (..) [DISCARD: Share of full-time yellow drivers; not a volume input.] quote: "The agency estimates that between 70 to 75% of yellow taxi drivers are full time drivers."
  - p38 Share of yellow taxi drivers estimated to be full time (upper bound) = **75** percent (..) [DISCARD: Share of full-time yellow drivers; not a volume input.] quote: "The agency estimates that between 70 to 75% of yellow taxi drivers are full time drivers."
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### d7 [forecasts_markets] Published forecasts and planning documents

Hypothesis: TLC, MTA, or NYC transportation reports may project for-hire trip volumes or congestion trends into 2026; these forecasts, if any, constrain the level and direction. Treat as forecast, not observation.

Queries issued by the searcher: NYC TLC forecast for-hire vehicle trips 2026; congestion pricing FHV trips report 2025 2026 MTA projection; TLC "For-Hire Vehicle License Review" 2026 report trips per day yellow taxi HVFHV; NYC TLC monthly trip data 2026 high-volume for-hire vehicle trips per day yellow taxi average

- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.newsbreak.com/the-city-1594241/4583132034003-up-against-uber-and-lyft-green-cabs-wither-to-lowest-ever-level-in-new-york` -> **live_dated** (page date 2026-04-09); points raw/verified 15/11
  - p39 Green cab average daily trips, February (TLC data) = **1,304** trips per day (2026-02-01..2026-02-28) [keep: ] quote: "Green cabs averaged 1,304 daily trips in February, according to TLC data"
  - p40 Green cab peak average daily trips, May 2015 = **57,637** trips per day (2015-05-01..2015-05-31) [DISCARD: 2015 green-cab peak; historical context only, superseded by p39 for current level.] quote: "down almost 98% from the peak of 57,637 trips per day in May 2015"
  - p41 Working green cab drivers, February = **539** drivers (2026-02-01..2026-02-28) [DISCARD: Green-cab driver count; not a trip-volume input.] quote: "TLC data shows there were just 539 working green cab drivers in February"
  - p42 Green cab operators, May 2015 = **7,521** operators (2015-05-01..2015-05-31) [DISCARD: 2015 green-cab operator count; historical context only.] quote: "a nearly 93% collapse from May 2015, when 7,521 operators were picking up street hails in the boroughs and Upper Manhattan"
  - p43 Green cabs on the road, February = **522** vehicles (2026-02-01..2026-02-28) [DISCARD: Green-cab vehicle count; not directly a trip count.] quote: "The number of those on the road fell to 522 in February"
  - p44 Green cabs in service, April 2020 = **671** vehicles (2020-04-01..2020-04-30) [DISCARD: 2020 green-cab vehicles; historical context only.] quote: "lower even than the 671 that remained in service during the early days of the pandemic in April 2020"
  - p45 Green cabs working at June 2015 peak = **6,500** vehicles (2015-06-01..2015-06-30) [DISCARD: 2015 green-cab vehicle peak; historical context only.] quote: "At their June 2015 peak, more than 6,500 green cabs were working in Brooklyn, The Bronx, Queens, Staten Island"
  - p46 High-volume FHV (Uber, Lyft) trips, February = **19,800,000** trips (2026-02-01..2026-02-28) [keep: ] quote: "high-volume for-hire vehicles, such as Uber and Lyft, had 19.8 million trips in February, almost 99% of pre-2020 levels"
  - p47 Green cab average daily driver earnings, February = **52** dollars per day (2026-02-01..2026-02-28) [DISCARD: Green-cab driver earnings; not a volume input.] quote: "In February, those earnings dropped to roughly $52 a day, according to an analysis of TLC data."
  - p48 Green cab average daily driver earnings, May 2015 peak = **114** dollars per day (2015-05-01..2015-05-31) [DISCARD: 2015 green-cab earnings; not a volume input.] quote: "At its peak in May 2015, green cab drivers averaged $114 a day from trips"
  - p49 Street-hail livery pilot permits actively in use as of last June = **563** permits (2025-06-01..2025-06-30) [DISCARD: Street-hail livery pilot permits; outside target scope.] quote: "only 563 permits from the test were actively in use as of last June after 3,509 were initially issued"
- `https://www.blackcarnews.com/article/tlc-review-concludes-no-new-fhv-plates-needed` -> **live_dated** (page date 2026-05-29); points raw/verified 4/3
  - p50 FHV License Review report coverage period start (February 2025) = **2,025** month (2025-02-01..2025-02-28) [DISCARD: Report coverage-period metadata; no volume content.] quote: "The February 2026 report covers the period of February 2025 through January 2026."
  - p51 FHV License Review report coverage period end (January 2026) = **2,026** month (2026-01-01..2026-01-31) [DISCARD: Report coverage-period metadata; no volume content.] quote: "The February 2026 report covers the period of February 2025 through January 2026."
  - p52 FHV License Review report publication month (February 2026) = **2,026** month (2026-02-01..2026-02-28) [DISCARD: Report publication-month metadata; no volume content.] quote: "The February 2026 report covers the period of February 2025 through January 2026."
- `https://data.ny.gov/api/views/2iid-6be2/files/69a060a3-e577-4165-8f93-b43239f561dc?download=true&filename=MTA_TaxiAndFHVMilesTraveledInTheCentralBusin` -> **live_dated** (page date 2026-04-08); points raw/verified 0/0
- dropped by code checks: 5 (period_end missing or unparseable: 4; period_end 2027-12-31 after as_of: 1)

### b1 [related_series] d2

Hypothesis: A monthly TLC summary or trip-record total for yellow+green+HVFHV in mid-2026 (e.g., June-August 2026) would anchor the level immediately before the target month, replacing the Sept-2025 secondary anchor (p23/p24) and the Feb-2026 HVFHV anchor (p46). This is the single most valuable missing input because the target is a near-term forecast and the most recent observed combined level is the dominant uncertainty.

Queries issued by the searcher: NYC TLC monthly summary report 2026 yellow taxi green HVFHV trips; TLC trip record data 2026 parquet yellow green HVFHV monthly totals; "TLC Industry Indicators" data.cityofnewyork.us average daily trips 2026 yellow green FHV HVFHV; TLC aggregated reports "average daily trips" June 2026 yellow taxi HVFHV

- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/aggregated-reports.page` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` -> **live_dated** (page date 2017-08-09); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b2 [related_series] d6

Hypothesis: A historical October seasonal index for combined yellow+green+HVFHV trips (October daily average relative to adjacent-month or annual daily average) would let us transfer a mid-2026 level to October 2026. Without it we must assume October is near the annual mean; a stable seasonal factor would materially tighten the estimate.

Queries issued by the searcher: TLC monthly trip totals 2023 2024 2025 by month yellow taxi HVFHV; NYC TLC trip record data monthly summary yellow green HVFHV trips October; "TLC Industry Indicators" monthly average daily trips yellow green FHVHV data.cityofnewyork.us v6kb-cqej; NYC taxi trips per day 2024 average 500,000 yellow taxi 700,000 Uber Lyft monthly trip totals

- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` -> **live_dated** (page date 2017-08-09); points raw/verified 0/0
- `https://data.cityofnewyork.us/d/c5iv-bn4s` -> **live_dated** (page date 2026-09-25); points raw/verified 0/0
- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b3 [shocks] d5

Hypothesis: Quantified effect of the 2025 congestion pricing charge on yellow/green/HVFHV trip volumes would adjust a pre-2025 baseline to 2026. If the effect is small (a few percent) it can be treated as absorbed in the recent anchor; if large, it changes the trend extrapolation.

Queries issued by the searcher: congestion pricing effect on for-hire vehicle trips NYC 2025 TLC data; MTA congestion pricing taxi FHV trip volume impact 2025 report; TLC data 2025 average daily trips citywide yellow taxi HVFHV total per day New York; "congestion pricing" NYC one year taxi FHV trips "1.4%" MTA evaluation report December 2025

- `https://www.mta.info/document/195631` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://findingspress.org/article/155761.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://ny1.com/nyc/all-boroughs/news/2025/03/01/taxi-rides-in-congestion-zone-up-in-january-compared-to-last-year` -> **live_dated** (page date 2025-03-01); points raw/verified 5/4
  - p53 Change in taxi trips to/from/within congestion relief zone since start of conges = **19** % change in taxi trips (2025-01-05..2025-01-31) [keep: ] quote: "Since the start of the program through the end of January, taxi trips were up nearly 19% for rides to, from and within the congestion relief zone, compared to the same time period in 2024"
  - p54 Change in for-hire vehicle (Uber/Lyft) rides to/from/within congestion relief zo = **3.4** % change in for-hire vehicle rides (2025-01-05..2025-01-31) [keep: ] quote: "for-hire vehicles rides - like Ubers and Lyfts - were down 3.4% during that same period"
  - p55 Change in citywide yellow taxi trips, all of January 2025 vs all of January 2024 = **17** % change in yellow taxi trips (2025-01-01..2025-01-31) [keep: ] quote: "Citywide, yellow taxi trips were up just over 17%, while for-hire rides were up 3.8% when comparing all of January."
  - p56 Change in citywide for-hire vehicle rides, all of January 2025 vs all of January = **3.8** % change in for-hire vehicle rides (2025-01-01..2025-01-31) [keep: ] quote: "Citywide, yellow taxi trips were up just over 17%, while for-hire rides were up 3.8% when comparing all of January."
- `https://data.cityofnewyork.us/d/v6kb-cqej` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['nyc taxi trips', 'tlc trips october', 'ride-hail volume']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p16'] Same underlying TLC statement (3.8M yellow-taxi trips in Oct 2024); p16 is a duplicate of p1, not independent confirmation.
- corroborating: ['p4', 'p17'] Duplicate of the same 9,768 active-taxis-in-Dec-2024 figure; one measurement, two URLs.
- corroborating: ['p5', 'p18'] Duplicate of the 11,315 active taxis in March 2020 benchmark.
- corroborating: ['p2', 'p19'] Duplicate of the 11-13M monthly taxi trips in 2015 upper bound.
- corroborating: ['p3', 'p20'] Duplicate of the 6-8M monthly taxi trips in 2019 upper bound.
- corroborating: ['p6', 'p21'] Duplicate of the ~20% EV/WAV dispatch share at end-2024; irrelevant to trip volume.
- corroborating: ['p7', 'p22'] Duplicate of the 15% Green Rides 2025 requirement; irrelevant to trip volume.
- corroborating: ['p8', 'p9', 'p30'] Same TLC testimony: 300M all-industry trips in 2024, +4.4% YoY; p30 is a duplicate transcript.
- corroborating: ['p10', 'p11', 'p12', 'p32'] Same TLC testimony: HVFHV 239M in 2024 vs 232M in 2023 (+3%); p32 duplicate.
- corroborating: ['p13', 'p14', 'p33', 'p34'] Same TLC testimony: non-HVFHV FHV 19.7M in 2024, +18%; p33/p34 duplicates.
- corroborating: ['p15', 'p31'] Same TLC testimony: taxi trips +7.5% 2023->2024; p31 duplicate.
- corroborating: ['p23', 'p24'] Same secondary source (therideshareguy) reporting Sept 2025 ride-hail ~647,819/day and taxi ~138,644/day; internally consistent but a single secondary measurement.
- corroborating: ['p25', 'p26'] Same secondary source revenue-per-trip estimates; not volume evidence.
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p47', 'p48', 'p49'] Single newsbreak article on green-cab decline; internally consistent, one underlying TLC-data analysis. p39 (1,304 green trips/day Feb 2026) is the only volume-relevant value.
- corroborating: ['p46'] Same newsbreak article: HVFHV 19.8M trips in Feb 2026, ~99% of pre-2020 levels; consistent with p10/p11 HVFHV scale.
- corroborating: ['p50', 'p51', 'p52'] Same blackcarnews article describing FHV License Review report coverage; contextual only.
- conflicting: ['p1', 'p23', 'p24', 'p39', 'p46'] Apparent tension: p1 (3.8M yellow trips Oct 2024 ~123k/day) vs p24 (138,644 taxi/day Sept 2025) vs p39 (green only 1,304/day Feb 2026). These are different scopes (yellow-only vs yellow+green) and per
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p15'] Both indicate yellow-taxi trips were rising into 2024 (October 2024 at 3.8M, +7.5% for CY2024); same TLC-derived source family, so not independent, but consistent in direction and level.
- corroborating: ['p10', 'p11', 'p12'] HVFHV 2023 ~232M, 2024 ~239M, +3% — internally consistent; same TLC release, so one underlying measurement.
- corroborating: ['p8', 'p9', 'p10', 'p13'] All-industry 2024 total >300M decomposes plausibly into HVFHV 239M + non-HVFHV FHV 19.7M + taxi (~40M implied); consistent accounting, same source.
- corroborating: ['p23', 'p24'] September 2025 ride-hail ~647,819/day and taxi ~138,644/day; combined ~786k/day. Third-party aggregation of TLC data; consistent with 2024 annual levels (~239M HVFHV ≈ 655k/day).
- corroborating: ['p46', 'p39'] February 2026 HVFHV 19.8M (~707k/day) and green cab 1,304/day; both from TLC data reported in same article. HVFHV Feb 2026 is above 2025 run-rate, suggesting continued modest growth.
- conflicting: ['p23', 'p46'] Apparent tension: Sep 2025 ride-hail ~648k/day vs Feb 2026 HVFHV ~707k/day. Resolvable by definition (ride-hail may exclude some HVFHV or be a different month/season) and by growth; treat as a level r
- corroborating: ['p53', 'p54', 'p55', 'p56'] Congestion-pricing period shows yellow taxi up sharply (~17% citywide Jan 2025) and FHV up modestly (~3.8%); same NY1 report, one measurement. Indicates taxi rebound and FHV near-flat, not a large FHV
- corroborating: ['p4', 'p5'] Active taxi counts (9,768 Dec 2024 vs 11,315 Mar 2020) show fleet shrinkage; contextual for capacity route, not a trip count.
- conflicting: ['p2', 'p3'] 2015 (11-13M/mo) vs 2019 (6-8M/mo) taxi trips show long-run decline; historical, not directly transferable to 2026 level but useful as trend context.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | October 2026 HVFHV level relative to February 2026 | 1 | 0.9..1.12 | 0.7099..1.42 (widened) | ratio | m1 (m2) | October is near or slightly below the annual mean for combined taxi/HVFHV trips; February 2026 is a winter month with a modest seasonal dip, so October 2026 should be roughly at or modestly above the February level, with trend growth offsetting seasonality. Range reflects uncertainty in seasonality  | Transferring the February 2026 HVFHV level (p46) to October 2026. | Evidence that October combined trips are materially below winter levels or that HVFHV volume has declined sharply since early 2026. |
| a2 | Yellow+green taxi daily trips in October 2026 | 140,000 | 115,000..165,000 | 97,404..194,808 (widened) | trips per day | m1 (m2) | September 2025 taxi ~138,644/day (p24) plus green ~1,304/day (p39); yellow taxi has been recovering (p1, p15, p55), so October 2026 likely near or slightly above the Sep 2025 level. Range spans flat-to-recovering. | Used as the taxi+green component in the combined sum for October 2026. | TLC data showing yellow/green taxi daily trips well outside 115k-165k in mid/late 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 787,959 | ['p46'] / ['a1', 'a2'] | [] |  | 1.00 | equal |  |

- m1 coverage: sum over channel of yellow+green taxi, HVFHV

Result: central **787,959** trip/day, 80% interval [567,456, 1,094,146] trip/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-10-31, after as_of: it cannot have been published yet


## Final answer

The best computed estimate for the average daily count of yellow taxi, green taxi (Boro Taxi), and high-volume for-hire vehicle trips combined in New York City for October 2026 is 787,959 trip/day (80% model-based interval 567,456 to 1,094,146 trip/day). This is a forecast; the target month lies after the information cutoff, so no observed value exists.

The estimate comes from a single method (1 method, weight 100%). It anchors the HVFHV component on the observed February 2026 monthly total of 19,800,000 trips trips, scaled to October 2026 by assumption 1 (range 0.7099 to 1.42), and adds a yellow-plus-green taxi daily component of 140,000 trip/day (range 97,404 to 194,808). Only the February HVFHV total is observed; the October scaling and the taxi level are analyst assumptions.

The main risk is that both components rest on TLC-derived third-party reporting and on unverified seasonal and recovery assumptions. Better evidence would be recent monthly TLC trip-record files and summary reports covering the months closest to the cutoff.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 October 2026 HVFHV level relative to February 2026: 1 ratio, range 0.7099 to 1.42 (range widened by code); used by m1. Overturned by: Evidence that October combined trips are materially below winter levels or that HVFHV volume has declined sharply since early 2026.
- a2 Yellow+green taxi daily trips in October 2026: 140,000 trips per day, range 97,404 to 194,808 (range widened by code); used by m1. Overturned by: TLC data showing yellow/green taxi daily trips well outside [n]k-[n]k in mid/late 2026.

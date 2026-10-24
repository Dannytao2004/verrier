# Evidence ledger: fc_us_retail_2026_06

- Question: Assume today is 2026-06-18. You know nothing published after this date. Estimate total U.S. retail and food services sales for June 2026 (seasonally adjusted and adjusted for holiday and trading-day differences, but not for price changes; a monthly amount, not an annual rate), in US dollars (the release states it in millions of dollars), as it will be first reported (advance estimate) in the U.S. Census Bureau's Advance Monthly Sales for Retail and Food Services release.
- as_of: 2026-06-18
- Pinned target: Total U.S. retail and food services sales for June 2026, seasonally adjusted and adjusted for holiday and trading-day differences but not for price changes, as it will be first reported in the U.S. Census Bureau's Advance Monthly Sales for Retail and Food Services release; monthly total in current U | unit millions of US dollars for the month | period 2026-06-01..2026-06-30 | publisher U.S. Census Bureau

- Official value (scoring only, never shown to the agent): 768,553,000,000

## Directions and pages

### d1 [own_history] Census advance report and historical seasonal-adjusted series

Hypothesis: The June 2026 advance total should be close to the most recent seasonally adjusted May 2026 level plus a typical June month-to-month change; recent 3-, 6-, and 12-month momentum constrains the plausible range. Because the series is already seasonally adjusted and holiday/trading-day adjusted, June calendar effects should be small but not zero.

Queries issued by the searcher: Advance Monthly Retail Trade Report May 2026 seasonally adjusted total retail and food services sales; Census retail sales May 2026 advance estimate; Census "adv2605" retail sales May 2026 pdf table 1 adjusted monthly sales; "June 2025" advance retail sales $ billion up from May 2025 seasonally adjusted Census

- `https://www2.census.gov/retail/releases/historical/marts/adv2605.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.census.gov/retail/releases/historical/marts/adv2604.pdf` -> **snapshot** (snapshot 20260519130340); points raw/verified 15/15
  - p1 Advance estimate of U.S. retail and food services sales, April 2026, seasonally  = **757,100,000,000** USD (2026-04-01..2026-04-30) [DISCARD: Rounded duplicate of p10 ($757.1B vs 757,085M); no extra information.] quote: "Advance estimates of U.S. retail and food services sales for April 2026, adjusted for seasonal variation and holiday and trading-day differences, but not for price changes, were $757.1 billion"
  - p2 Month-to-month percent change in total retail and food services sales, April 202 = **0.5** percent (2026-04-01..2026-04-30) [keep: ] quote: "were $757.1 billion, up 0.5 percent (±0.4 percent) from the previous month"
  - p3 Revised March 2026 total retail and food services sales, seasonally adjusted, cu = **753,400,000,000** USD (2026-03-01..2026-03-31) [DISCARD: Rounded duplicate of p11 ($753.4B vs 753,370M); no extra information.] quote: "March 2026 (revised) $753.4 billion 1.6%"
  - p4 Revised February 2026 to March 2026 percent change in total retail and food serv = **1.6** percent (2026-02-01..2026-03-31) [keep: ] quote: "The February 2026 to March 2026 percent change was revised from up 1.7 percent (±0.4 percent) to up 1.6 percent (±0.2 percent)."
  - p5 Table 1 seasonally adjusted total retail and food services sales, April 2026 adv = **755,713** USD millions (2026-04-01..2026-04-30) [DISCARD: Conflicts with p1/p2/p10/p11; 755,713M cannot be April 2026 total with +0.5% from p11. Likely misaligned column/vintage.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p6 Table 1 seasonally adjusted total retail and food services sales, March 2026 pre = **760,772** USD millions (2026-03-01..2026-03-31) [DISCARD: Conflicts with p2/p10/p11; 760,772M as March 2026 preliminary is inconsistent with revised March 753,370M and April +0.5] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p7 Table 1 seasonally adjusted total retail and food services sales, February 2026  = **656,082** USD millions (2026-02-01..2026-02-28) [DISCARD: Misaligned or typo February 2026 value (656,082) conflicts with p12's 741,278 and is implausible in the monthly sequence] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p8 Table 1 seasonally adjusted total retail and food services sales, April 2025 (mi = **722,319** USD millions (2025-04-01..2025-04-30) [DISCARD: Older April 2025 vintage superseded by revised p13; avoid duplicate incompatible 2025 base.] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p9 Table 1 seasonally adjusted total retail and food services sales, March 2025 (mi = **726,888** USD millions (2025-03-01..2025-03-31) [DISCARD: Older March 2025 vintage superseded by revised p14; avoid duplicate incompatible 2025 base.] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p10 Table 1 seasonally adjusted total retail and food services sales, April 2026 rev = **757,085** USD millions (2026-04-01..2026-04-30) [keep: ] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p11 Table 1 seasonally adjusted total retail and food services sales, March 2026 rev = **753,370** USD millions (2026-03-01..2026-03-31) [keep: ] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p12 Table 1 seasonally adjusted total retail and food services sales, February 2026  = **741,278** USD millions (2026-02-01..2026-02-28) [keep: ] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p13 Table 1 seasonally adjusted total retail and food services sales, April 2025 rev = **721,903** USD millions (2025-04-01..2025-04-30) [keep: ] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p14 Table 1 seasonally adjusted total retail and food services sales, March 2025 rev = **723,339** USD millions (2025-03-01..2025-03-31) [keep: ] quote: "total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p15 Table 2 percent change in total retail and food services sales, April 2026 advan = **4.9** percent (2026-04-01..2026-04-30) [keep: ] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
- `https://investinglive.com/news/us-may-advance-retail-sales-09-vs-05-expected-20260617/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Census component detail by NAICS category

Hypothesis: The total equals the sum of major retail and food services components. Forecasting the largest components from their latest May 2026 levels and category-specific trends should constrain the total and reveal whether a simple aggregate trend is plausible.

Queries issued by the searcher: May 2026 advance retail sales by NAICS Census Bureau; Advance Monthly Retail Trade Report May 2026 table 1 motor vehicle food services nonstore; census.gov retail marts adv2605.pdf May 2026 table 1 estimated monthly sales millions of dollars; JETRO 米国 小売売上高 業種別 2026年5月 季節調整済み 100万ドル 自動車 無店舗

- `https://www2.census.gov/retail/releases/historical/marts/adv2605.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/release/tables?rid=477` -> **snapshot** (snapshot 20241028102221); points raw/verified 0/0
- `http://hosting.briefing.com/cschwab/Calendars/EconomicReleases/retail.htm` -> **snapshot** (snapshot 20260209214615); points raw/verified 15/0
- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period year 2025 does not appear in the page text or URL (likely mis-dated): 15)

### d3 [related_series] Card-processor and bank spending indices

Hypothesis: High-frequency card spending growth in June versus May maps into Census nominal retail sales growth for card-heavy categories, especially nonstore, general merchandise, restaurants, and gasoline. A bridge based on historical correlation and category coverage can nowcast the aggregate.

Queries issued by the searcher: Bank of America card spending June 2026; JPMorgan Chase credit card spending June 2026; Affinity Solutions retail spending June 2026; Census advance monthly retail sales May 2026 total seasonally adjusted million; "Consumer Checkpoint" Bank of America June 2026 card spending week ending June 13; JPMorgan Chase card spending tracker mid-June 2026 year over year

- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-june-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.affinity.solutions/newsroom/cnbc-nrf-retail-monitor-shows-nineth-month-of-sales-growth-in-june/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-july-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sa.marketscreener.com/quote/stock/BANK-OF-AMERICA-CORPORATI-11751/news/Bank-of-America-spots-a-clear-pickup-in-US-consumer-spending-53752162/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] Motor vehicle dealers and auto market data

Hypothesis: Motor vehicle and parts dealers are one of the largest components. Their nominal sales can be approximated by light vehicle unit sales times average transaction price, with a small parts-and-service add-on. A May or partial-June vehicle-sales estimate plus pricing can anchor this component; the rest of retail can be extrapolated separately.

Queries issued by the searcher: May 2026 US light vehicle sales SAAR; average new vehicle transaction price May 2026; Census advance retail sales May 2026 motor vehicle and parts dealers millions seasonally adjusted; "retail sales" May 2026 advance estimate Census Bureau total retail and food services

- `https://fred.stlouisfed.org/data/RSMVPD` -> **snapshot** (snapshot 20241027094924); points raw/verified 15/15
  - p16 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **128,751** millions of US dollars (2024-06-01..2024-06-30) [keep: ] quote: "\| 2024-06-01 \| 128751 \|"
  - p17 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **133,545** millions of US dollars (2024-05-01..2024-05-31) [keep: ] quote: "\| 2024-05-01 \| 133545 \|"
  - p18 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **133,441** millions of US dollars (2023-06-01..2023-06-30) [keep: ] quote: "\| 2023-06-01 \| 133441 \|"
  - p19 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **131,953** millions of US dollars (2023-05-01..2023-05-31) [keep: ] quote: "\| 2023-05-01 \| 131953 \|"
  - p20 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **125,577** millions of US dollars (2022-06-01..2022-06-30) [keep: ] quote: "\| 2022-06-01 \| 125577 \|"
  - p21 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **125,373** millions of US dollars (2022-05-01..2022-05-31) [keep: ] quote: "\| 2022-05-01 \| 125373 \|"
  - p22 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **126,502** millions of US dollars (2021-06-01..2021-06-30) [keep: ] quote: "\| 2021-06-01 \| 126502 \|"
  - p23 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **130,237** millions of US dollars (2021-05-01..2021-05-31) [keep: ] quote: "\| 2021-05-01 \| 130237 \|"
  - p24 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **106,827** millions of US dollars (2020-06-01..2020-06-30) [keep: ] quote: "\| 2020-06-01 \| 106827 \|"
  - p25 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **98,394** millions of US dollars (2020-05-01..2020-05-31) [keep: ] quote: "\| 2020-05-01 \| 98394 \|"
  - p26 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, June = **102,707** millions of US dollars (2019-06-01..2019-06-30) [keep: ] quote: "\| 2019-06-01 \| 102707 \|"
  - p27 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, May  = **102,958** millions of US dollars (2019-05-01..2019-05-31) [keep: ] quote: "\| 2019-05-01 \| 102958 \|"
  - p28 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, late = **133,854** millions of US dollars (2024-09-01..2024-09-30) [keep: ] quote: "\| 2024-09-01 \| 133854 \|"
  - p29 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, July = **134,367** millions of US dollars (2024-07-01..2024-07-31) [keep: ] quote: "\| 2024-07-01 \| 134367 \|"
  - p30 Advance Retail Sales: Motor Vehicle and Parts Dealers, seasonally adjusted, Augu = **133,799** millions of US dollars (2024-08-01..2024-08-31) [keep: ] quote: "\| 2024-08-01 \| 133799 \|"
- `https://kpmg.com/us/en/articles/2026/may-2026-retail-sales.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.motor.com/2026/06/nada-market-beat-may-saar-reaches-16-1-million/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fi-magazine.com/news/auto-prices-ride-may-moderation` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] Gasoline stations and fuel market data

Hypothesis: Gasoline station sales are a volatile but meaningful share of retail. They can be estimated from motor gasoline consumed or supplied multiplied by retail gasoline prices. Weekly EIA data available before the cutoff can nowcast June gasoline station sales, which then feed the component sum.

Queries issued by the searcher: EIA weekly retail gasoline price June 2026; Census advance monthly retail sales May 2026 gasoline stations; EIA weekly petroleum status report motor gasoline product supplied June 2026 four week average; "gasoline stations" sales May 2026 millions of dollars Census advance retail trade table

- `https://www.eia.gov/dnav/pet/PET_PRI_GND_DCUS_R1Z_W.htm` -> **snapshot** (snapshot 20260607023819); points raw/verified 12/12
  - p31 U.S. weekly retail gasoline price, all grades, week of 06/01/26 (dollars per gal = **4.04** dollars per gallon (2026-06-01..2026-06-01) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p32 U.S. weekly retail gasoline price, all grades, week of 05/25/26 (dollars per gal = **4.257** dollars per gallon (2026-05-25..2026-05-25) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p33 U.S. weekly retail gasoline price, all grades, week of 05/18/26 (dollars per gal = **4.226** dollars per gallon (2026-05-18..2026-05-18) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p34 U.S. weekly retail gasoline price, all grades, week of 05/11/26 (dollars per gal = **4.282** dollars per gallon (2026-05-11..2026-05-11) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p35 U.S. weekly retail gasoline price, all grades, week of 05/04/26 (dollars per gal = **4.217** dollars per gallon (2026-05-04..2026-05-04) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p36 U.S. weekly retail gasoline price, all grades, week of 04/27/26 (dollars per gal = **3.924** dollars per gallon (2026-04-27..2026-04-27) [keep: ] quote: "\| \| 3.924 \| 4.217 \| 4.282 \| 4.226 \| 4.257 \| 4.040 \| 1993-2026 \|"
  - p37 U.S. weekly retail regular gasoline price, week of 06/01/26 (dollars per gallon  = **3.932** dollars per gallon (2026-06-01..2026-06-01) [DISCARD: Redundant gasoline sub-grade detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as] quote: "\| \| 3.817 \| 4.113 \| 4.176 \| 4.120 \| 4.151 \| 3.932 \| 1993-2026 \|"
  - p38 U.S. weekly retail regular gasoline price, week of 05/25/26 (dollars per gallon  = **4.151** dollars per gallon (2026-05-25..2026-05-25) [DISCARD: Redundant gasoline sub-grade detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as] quote: "\| \| 3.817 \| 4.113 \| 4.176 \| 4.120 \| 4.151 \| 3.932 \| 1993-2026 \|"
  - p39 U.S. weekly retail premium gasoline price, week of 06/01/26 (dollars per gallon  = **4.627** dollars per gallon (2026-06-01..2026-06-01) [DISCARD: Redundant gasoline sub-grade detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as] quote: "\| \| 4.385 \| 4.618 \| 4.731 \| 4.723 \| 4.796 \| 4.627 \| 1994-2026 \|"
  - p40 U.S. weekly retail midgrade gasoline price, week of 06/01/26 (dollars per gallon = **4.231** dollars per gallon (2026-06-01..2026-06-01) [DISCARD: Redundant gasoline sub-grade detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as] quote: "\| \| 3.967 \| 4.220 \| 4.339 \| 4.338 \| 4.413 \| 4.231 \| 1994-2026 \|"
  - p41 U.S. weekly retail all-grades conventional areas gasoline price, week of 06/01/2 = **4.011** dollars per gallon (2026-06-01..2026-06-01) [DISCARD: Redundant gasoline area detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as a to] quote: "\| \| 3.909 \| 4.207 \| 4.267 \| 4.205 \| 4.233 \| 4.011 \| 1994-2026 \|"
  - p42 U.S. weekly retail all-grades reformulated areas gasoline price, week of 06/01/2 = **4.345** dollars per gallon (2026-06-01..2026-06-01) [DISCARD: Redundant gasoline area detail; p31-p36 all-grade weekly prices already capture the early-June price move needed as a to] quote: "\| \| 4.077 \| 4.326 \| 4.446 \| 4.445 \| 4.518 \| 4.345 \| 1994-2026 \|"
- `https://cmegroup.econoday.com/byevent?fid=672407&year=2026&cty=US&ctyall=10738893&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://foodinstitute.com/focus/online-retail-gains-foodservice-slips-in-latest-census-data/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/news/economy-news/us-retail-sales-beat-expectations-in-may-4747321` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [related_series] Nonstore retailers and e-commerce

Hypothesis: Nonstore retailers are a large and growing share of retail. Their June sales can be projected from the latest Census nonstore level and e-commerce trend, with online spending indices or promotion timing as a June adjustment.

Queries issued by the searcher: Census advance monthly retail sales May 2026 nonstore retailers; Census e-commerce share of retail sales Q1 2026; "nonstore retailers" May 2026 "million" advance retail sales table 454; census.gov retail releases historical marts adv2605.pdf

- `https://primarynewssource.org/wp-content/uploads/marts_current-34.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.macroaxis.com/advance-retail-sales-nonstore-retailers` -> **snapshot** (snapshot 20230625103902); points raw/verified 15/0
- `https://eightx.co/blog/ecommerce-penetration-by-category-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (scale word 'million' not supported by quote or table header: 1; value_as_written not in quote as a whole number: 14)

### d7 [forecasts_markets] Macro forecasters and published consensus

Hypothesis: June nominal retail sales growth should be consistent with nominal income, goods consumption, employment, and inflation trends. Any published June 2026 retail sales forecast or Q2 tracking estimate available before the cutoff can serve as an anchor, provided its definition matches the Census total.

Queries issued by the searcher: May 2026 retail sales advance monthly Census Bureau; June 2026 retail sales forecast consensus; "June 2026" retail sales nowcast forecast published June 2026 Bank of America card spending; census.gov advance monthly retail trade May 2026 $763.7 billion release June 17 2026

- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/analysis/retail-sales-strength-looks-more-like-inflation-than-consumer-momentum-200682355` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-june-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fxverify.com/vi/news/bank-of-america-highlights-softer-card-spending-data-ahead-of-next-weeks-retail-sales-14864` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [related_series] Restaurants and food services

Hypothesis: Food services and drinking places sales can be projected from their May 2026 level and recent trend, with restaurant booking/activity data and food-away-from-home inflation providing a June adjustment. This is a smaller component but helps validate the aggregate.

Queries issued by the searcher: Census food services and drinking places sales May 2026 advance monthly retail; OpenTable seated diners June 2026; adv2605.pdf Census advance monthly retail May 2026 release table food services drinking places; CPI food away from home May 2026 BLS report June 10 2026

- `https://primarynewssource.org/wp-content/uploads/marts_current-34.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://foodinstitute.com/focus/online-retail-gains-foodservice-slips-in-latest-census-data/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/data/RSFSDP` -> **snapshot** (snapshot 20250722082233); points raw/verified 12/0
- `https://www.opentable.com/c/state-of-industry/` -> **snapshot** (snapshot 20260613164054); points raw/verified 0/0
- dropped by code checks: 12 (scale word 'million' not supported by quote or table header: 10; number: no number in value_as_written: 1; number: more than one number in value_as_written: 1)

### b1 [own_history] data_gap

Hypothesis: The missing May 2026 advance total is the highest-value input: it would let us project June from the latest level plus one month of recent momentum instead of extrapolating two months from April, and would show whether the April m/m gain persisted.

Queries issued by the searcher: Census "Advance Monthly Retail Trade" May 2026 retail sales; FRED RSAFS retail sales May 2026; "adv2605" OR "marts_current" census May 2026 advance monthly sales $763.7 billion table 1; census.gov "Advance Monthly Sales for Retail and Food Services" May 2026 released June 17 2026 seasonally adjusted total 763,7

- `https://www2.census.gov/retail/releases/historical/marts/adv2605.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://primarynewssource.org/wp-content/uploads/marts_current-34.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.furnituretoday.com/furniture-retailing/doc-furnitures-sales-gap-shrinks-in-may/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] seasonal_baseline

Hypothesis: June 2025 total retail and food services sales, and surrounding 2025 monthly totals, would enable a proper year-on-year or series-based forecast and reduce reliance on a two-month extrapolation from April 2026.

Queries issued by the searcher: FRED RSAFS advance retail and food services sales total seasonally adjusted June 2025; Census Monthly Retail Trade historical tables 2025 seasonally adjusted total retail and food services sales

- `https://fred.stlouisfed.org/data/MRTSSM44X72USS` -> **snapshot** (snapshot 20250210204818); points raw/verified 15/0
- `https://www2.census.gov/retail/releases/historical/marts/adv2506.pdf` -> **snapshot** (snapshot 20250801000552); points raw/verified 15/3
  - p43 U.S. retail and food services total sales, June 2025, headline advance estimate = **720,100,000,000** USD (2025-06-01..2025-06-30) [keep: ] quote: "holiday and trading-day differences, but not for price changes, were $720.1 billion, up 0.6 percent (±0.5 percent) from the previous month, and up 3.9 percent (±0.5 percent) from June 2024."
  - p44 U.S. retail and food services total sales, May 2025 (revised), headline = **715,500,000,000** USD (2025-05-01..2025-05-31) [keep: ] quote: "May 2025 (revised) $715.5 billion -0.9%"
  - p45 Percent change in U.S. retail and food services total sales, June 2025 vs June 2 = **3.9** percent (2025-06-01..2025-06-30) [keep: ] quote: "total .......................................................... 0.6 3.9 -0.9 3.3 0.5 4.1"
- `https://www.census.gov/econ/currentdata/?programCode=MRTS&startYear=1992&endYear=2023&categories[` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/data/RSAFS` -> **snapshot** (snapshot 20241105062726); points raw/verified 15/0
- dropped by code checks: 42 (scale word 'million' not supported by quote or table header: 42)

### b3 [physical_flow] nowcast_adjustment

Hypothesis: High-frequency June 2026 card spending, EIA gasoline volumes, or light-vehicle sales would quantify the early-June gasoline price drop and auto momentum, the main identifiable risks to a simple April-based extrapolation.

Queries issued by the searcher: June 2026 card spending retail sales nowcast; EIA weekly gasoline supplied June 2026; Cox Automotive June 2026 light vehicle sales forecast; Census advance retail sales May 2026 released June 16 2026 total sales billion; EIA retail gasoline price June 2026 national average drop per gallon

- `https://fxverify.com/en/news/bank-of-america-highlights-softer-card-spending-data-ahead-of-next-weeks-retail-sales-14864` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eia.gov/petroleum/supply/weekly/archive/2026/2026_06_10/wpsr_2026_06_10.php` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rosap.ntl.bts.gov/view/dot/91977` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ph.investing.com/news/assorted/crude-inventory-fell-72-million-barrels-last-week-says-eia-432SI-2444594` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['retail sales', 'june 2026', 'us consumer']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p10'] Both identify April 2026 total retail and food services sales at about $757.1B ($757,100M text vs $757,085M revised table). They come from the same Census release/definition, so this is vintage agreem
- corroborating: ['p5', 'p1', 'p10'] p5 is the April 2026 advance table level ($755,713M), slightly below the revised/text $757.1B. The gap is consistent with a routine advance-to-revised revision; use p10 for the base level and p5 mainl
- corroborating: ['p2', 'p4', 'p15'] Same Census release: April m/m +0.5%, revised Feb-Mar +1.6%, and April y/y +4.9% all describe positive nominal spring 2026 momentum. They are not independent measurements.
- conflicting: ['p7', 'p12', 'p5'] p7 labels 656,082 as February 2026 revised, but p12 gives February 2026 revised 741,278 and the table sequence around p5 makes 656,082 implausible for February 2026. Treat p7 as a misaligned or typo c
- corroborating: ['p8', 'p13'] Both are April 2025 total levels (722,319 and 721,903), differing only by revision/rounding. Useful as historical context, not as a direct June 2026 signal.
- corroborating: ['p9', 'p14'] March 2025 values 726,888 and 723,339 differ by a small revision-sized amount; keep as historical context, not as independent evidence on June 2026.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30'] Historical motor-vehicle and parts dealer levels show June/May ratios mostly near 1.0 except 2020. They are a seasonal analogue only, lack 2025-2026 levels, and cannot anchor the June 2026 total direc
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36'] EIA weekly all-grade gasoline prices show a sharp early-June drop from 4.257 on 2026-05-25 to 4.040 on 2026-06-01, a downside risk for June gasoline-station sales versus May. Only one June week is obs
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42'] Sub-grade and area gasoline prices corroborate the early-June price decline, but are redundant for a total-retail estimate once p31-p36 are kept.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p14', 'p2', 'p4', 'p15'] Same Census May 14 2026 release and internally consistent: p10 Apr 2026 757,085M, p11 Mar 2026 753,370M, p12 Feb 2026 741,278M; p2 Apr +0.5% matches p10/p11; p4 Feb-Mar +1.6% matches p12/p11; p15 Apr 
- duplicate: ['p1', 'p3', 'p10', 'p11'] p1 and p3 are rounded headline copies of p10/p11: p1 ~$757.1B vs p10 757,085M; p3 ~$753.4B vs p11 753,370M. They corroborate but add no independent information.
- conflicting: ['p5', 'p6', 'p1', 'p2', 'p10', 'p11'] p5 755,713M and p6 760,772M cannot be the same-vintage total row that matches p1 757.1B and p2 +0.5% from p11 753,370M; likely column/vintage misalignment. Do not use for levels.
- revision: ['p8', 'p9', 'p13', 'p14'] p8/p9 are older April/March 2025 vintages; p13/p14 are revised. Differences (Apr 722,319 vs 721,903; Mar 726,888 vs 723,339) are revision-scale. Use revised p13/p14 for a consistent 2025 base; not ind
- corroborating: ['p43', 'p44', 'p45'] Same 2025 Census release: p43 Jun 2025 $720.1B, p44 May 2025 revised $715.5B; p45 Jun m/m +0.6% matches p43/p44 ratio ~1.0064. Use p43/p44 for June/May momentum analog and p43 as last-year base.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36'] EIA weekly all-grades retail gasoline prices show May 2026 around $4.22-$4.28/gal and June 1 at $4.04, with late April $3.924. Independent of Census; only price, not volume. p31-p35 support a June gas
- contextual: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30'] FRED motor vehicle and parts dealers historical May/June levels 2019-2024. Shows a large but mixed June-vs-May component pattern; no 2026 level or trend, so cannot directly anchor June 2026 total. Use

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | effective share of total retail and food services sales moving with retail gasoline price | 0.075 | 0.05..0.1 | 0.05..0.1 | share | m1 (m1) | Gasoline stations are roughly 7-8% of total retail and food services sales in recent years. Using 7.5% with full pass-through of the EIA all-grades retail price change to gasoline-station receipts gives a modest aggregate adjustment. The range allows for definitional scope and volume-response uncert | Used only to adjust the aggregate momentum forecast for the June 2026 EIA gasoline price drop; assumes gasoline volume and other categories are unaffected over the month. | Evidence that gasoline-station sales are below 5% or above 10% of total retail sales, or that gasoline volume or pass-through offsets most of the price change. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 770,858,967,260 | ['p10', 'p2', 'p4', 'p31', 'p32', 'p33', 'p34', 'p35'] / ['a1'] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 756,235,665,560 | ['p43', 'p15'] / [] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | formula_mc | 763,645,844,012 | ['p10', 'p2', 'p43', 'p44'] / [] | [] |  | 1.00 | B3 of 3 blocks; median of blocks: this block is the median |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p10 * (1 + mean(p2, p4)) ** 2 * (1 + a1 * (p31 / mean(p32, p33, p34, p35) - 1)); Monte Carlo P10 to P90 642,376,210,939 to 924,803,664,165; result unit 1000000 USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p43 * (1 + p15); Monte Carlo P10 to P90 630,432,631,248 to 907,144,625,629; result unit USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p10 * (1 + p2) * (p43 / p44); Monte Carlo P10 to P90 556,782,330,876 to 1,049,720,783,031; result unit 1000000 USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 770,858,967,260 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 756,235,665,560 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 763,645,844,012 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.04 (not above one, so no widening); final width x/÷1.38.

Result: central **763,645,844,012** USD, 80% interval [554,305,642,205, 1,052,045,894,314] USD, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The estimate for total U.S. retail and food services sales for June 2026 (seasonally adjusted, holiday/trading-day adjusted, not price-adjusted, monthly total) is 763,645,844,012 USD (80% model-based interval 554,305,642,205 to 1,052,045,894,314 USD). This is a forecast: June 2026 is future relative to the cutoff, so it rests on data through May 2026.

Observed inputs include April 2026 sales of 757,085 USD millions, the April m/m change of 0.5 percent, the revised February–March change of 1.6 percent, June 2025 sales of 720,100,000,000 USD, May 2025 sales of 715,500,000,000 USD, and the April 2026 year-over-year change of 4.9 percent. Gasoline prices (4.04 dollars per gallon versus May weeks) feed the momentum route, which also uses the analyst assumption a1 of 0.075 (range 0.05 to 0.1).

The combination uses 3 routes; the code gave the momentum bridge full weight because its inputs overlap the others, so blocks were not treated as independent. The main risk is that May/June 2026 momentum diverges from the April and prior-year analogs. Better evidence would be actual May 2026 sales and early June indicators.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 effective share of total retail and food services sales moving with retail gasoline price: 0.075 share, range 0.05 to 0.1; used by m1. Overturned by: Evidence that gasoline-station sales are below [n] or above [n] of total retail sales, or that gasoline volume or pass-through offsets most of the price change.

Method details (computed by code):
- m1 formula_mc: p10 * (1 + mean(p2, p4)) ** 2 * (1 + a1 * (p31 / mean(p32, p33, p34, p35) - 1)); Monte Carlo P10 to P90 642,376,210,939 to 924,803,664,165; result unit 1000000 USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p43 * (1 + p15); Monte Carlo P10 to P90 630,432,631,248 to 907,144,625,629; result unit USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p10 * (1 + p2) * (p43 / p44); Monte Carlo P10 to P90 556,782,330,876 to 1,049,720,783,031; result unit 1000000 USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 770,858,967,260 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 756,235,665,560 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 763,645,844,012 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.04 (not above one, so no widening); final width x/÷1.38.

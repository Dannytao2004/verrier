# Evidence ledger: fc_us_retail_2026_06

- Question: Assume today is 2026-06-18. You know nothing published after this date. Estimate total U.S. retail and food services sales for June 2026 (seasonally adjusted and adjusted for holiday and trading-day differences, but not for price changes; a monthly amount, not an annual rate), in US dollars (the release states it in millions of dollars), as it will be first reported (advance estimate) in the U.S. Census Bureau's Advance Monthly Sales for Retail and Food Services release.
- as_of: 2026-06-18
- Pinned target: Total U.S. retail and food services sales (advance monthly estimate), seasonally adjusted and adjusted for holiday and trading-day differences but not for price changes, as first reported by the U.S. Census Bureau for the month of June 2026 | unit millions of US dollars (monthly total) | period 2026-06-01..2026-06-30 | publisher U.S. Census Bureau (Advance Monthly Retail Trade and Food Services Survey, MARTS)

- Official value (scoring only, never shown to the agent): 768,553,000,000

## Directions and pages

### d1 [own_history] Census Bureau MARTS time series

Hypothesis: The target is a continuation of the seasonally adjusted monthly retail and food services sales series; recent published levels (through the latest month before cutoff, e.g. April/May 2026) plus typical month-over-month growth and June seasonal factors anchor the June 2026 level.

Queries issued by the searcher: Census advance monthly retail trade report May 2026 seasonally adjusted retail and food services sales; MARTS historical table seasonally adjusted retail and food services sales monthly millions 2024 2025; "MRTSSM44X72USS" 2025 values retail trade and food services millions FRED table data; Census "advance monthly sales for retail and food services" May 2026 pdf table 1 total sales millions February March April May 2026

- `https://www.census.gov/retail/marts/www/marts_current.pdf` -> **snapshot** (snapshot 20260617144540); points raw/verified 15/15
  - p1 Advance estimate of U.S. retail and food services sales, seasonally adjusted, Ma = **763,700,000,000** USD (2026-05-01..2026-05-31) [keep: ] quote: "Advance estimates of U.S. retail and food services sales for May 2026, adjusted for seasonal variation and holiday and trading-day differences, but not for price changes, were $763.7 billion"
  - p2 Revised estimate of U.S. retail and food services sales, seasonally adjusted, Ap = **757,000,000,000** USD (2026-04-01..2026-04-30) [keep: ] quote: "April 2026 (revised) $757.0 billion 0.4%"
  - p3 Month-over-month percent change in total retail and food services sales, May 202 = **0.9** percent (2026-05-01..2026-05-31) [keep: ] quote: "were $763.7 billion, up 0.9 percent (±0.4 percent) from the previous month"
  - p4 Year-over-year percent change in total retail and food services sales, May 2026  = **6.9** percent (2026-05-01..2026-05-31) [keep: ] quote: "and up 6.9 percent (±0.5 percent) from May 2025"
  - p5 Revised month-over-month percent change in total retail and food services sales, = **0.4** percent (2026-04-01..2026-04-30) [keep: ] quote: "The March 2026 to April 2026 percent change was revised from up 0.5 percent (±0.4 percent) to up 0.4 percent (±0.2 percent)."
  - p6 Seasonally adjusted total retail and food services sales, May 2026 (Table 1) = **763,705** millions of USD (2026-05-01..2026-05-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p7 Seasonally adjusted total retail and food services sales, April 2026 preliminary = **757,036** millions of USD (2026-04-01..2026-04-30) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p8 Seasonally adjusted total retail and food services sales, March 2026 revised (Ta = **754,013** millions of USD (2026-03-01..2026-03-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p9 Seasonally adjusted total retail and food services sales, May 2025 revised (Tabl = **722,319** millions of USD (2025-05-01..2025-05-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p10 Seasonally adjusted total retail and food services sales, April 2025 revised (Ta = **714,568** millions of USD (2025-04-01..2025-04-30) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p11 Seasonally adjusted total retail and food services sales, March 2025 revised (Ta = **722,442** millions of USD (2025-03-01..2025-03-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p12 Not adjusted total retail and food services sales, May 2026 advance (Table 1) = **792,825** millions of USD (2026-05-01..2026-05-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p13 Not adjusted total retail and food services sales, April 2026 preliminary (Table = **754,755** millions of USD (2026-04-01..2026-04-30) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p14 Not adjusted total retail and food services sales, March 2026 revised (Table 1) = **761,135** millions of USD (2026-03-01..2026-03-31) [keep: ] quote: "total ......................................................... 3,639,171 4.3 792,825 754,755 761,135 753,313 722,319 763,705 757,036 754,013 714,568 722,442"
  - p15 Median average absolute revision to advance estimates, total retail and food ser = **0.1** percent (not stated (page dated 2026-06-16)) [keep: ] quote: "total ........................................................... 1.0 0.2 0.1 0.3 0.0 0.1"
- `https://fred.stlouisfed.org/data/MRTSSM44X72USS` -> **snapshot** (snapshot 20250210204818); points raw/verified 15/0
- `https://www2.census.gov/retail/releases/historical/marts/adv2604.pdf` -> **snapshot** (snapshot 20260519130340); points raw/verified 15/13
  - p16 Advance estimate of total U.S. retail and food services sales, seasonally adjust = **755,713** millions of US dollars (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; superseded April advance vintage, redundant with p64/p7.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p17 Preliminary estimate of total U.S. retail and food services sales, seasonally ad = **760,772** millions of US dollars (2026-03-01..2026-03-31) [DISCARD: Discarded earlier; superseded May preliminary vintage, redundant with p6.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p18 Revised estimate of total U.S. retail and food services sales, seasonally adjust = **656,082** millions of US dollars (2026-02-01..2026-02-28) [DISCARD: Discarded earlier; value (656,082) is implausible for a February total and conflicts with the series; unusable.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p19 Advance estimate of total U.S. retail and food services sales, seasonally adjust = **722,319** millions of US dollars (2025-04-01..2025-04-30) [DISCARD: Discarded earlier; mislabeled (April 2025 value presented as April 2026 advance), redundant with p9.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p20 Preliminary estimate of total U.S. retail and food services sales, seasonally ad = **726,888** millions of US dollars (2025-03-01..2025-03-31) [DISCARD: Discarded earlier; superseded May preliminary vintage, redundant with p6.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p21 Revised estimate of total U.S. retail and food services sales, seasonally adjust = **757,085** millions of US dollars (2025-04-01..2025-04-30) [DISCARD: Discarded earlier; near-duplicate of p7 with a different vintage label; redundant.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p22 Revised estimate of total U.S. retail and food services sales, seasonally adjust = **753,370** millions of US dollars (2025-03-01..2025-03-31) [DISCARD: Discarded earlier; near-duplicate of p8; redundant.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p23 Revised estimate of total U.S. retail and food services sales, seasonally adjust = **741,278** millions of US dollars (2025-02-01..2025-02-28) [DISCARD: Discarded earlier; February 2026 revised value, not needed and of uncertain vintage.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p24 Month-over-month percent change in total retail and food services sales, April 2 = **0.5** percent (2026-04-01..2026-04-30) [keep: ] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p25 Month-over-month percent change in total retail and food services sales, March 2 = **1.6** percent (2026-03-01..2026-03-31) [keep: ] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p26 Year-over-year percent change in total retail and food services sales, April 202 = **4.9** percent (2026-04-01..2026-04-30) [keep: ] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p27 Percent change in total retail and food services sales, February 2026 through Ap = **4.4** percent (2026-02-01..2026-04-30) [keep: ] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p28 Median average absolute revision to advance month-to-month change, total retail  = **0.1** percent (not stated (page dated 2026-05-13)) [keep: ] quote: "Retail & food services, total ........................................................... 1.0 0.2 0.1 0.3 0.0 0.1"
- `https://www.census.gov/retail/marts/historic_releases.html` -> **snapshot** (snapshot 20260416030202); points raw/verified 0/0
- dropped by code checks: 17 (scale word 'million' not supported by quote or table header: 15; period year 2024 does not appear in the page text or URL (likely mis-dated): 2)

### d2 [related_series] Component breakdown (NAICS categories)

Hypothesis: Total equals sum of published component series (motor vehicles, food services, general merchandise, nonstore retailers, gasoline stations, etc.); projecting each component and summing gives an independent route and reveals which components drive uncertainty.

Queries issued by the searcher: MARTS advance monthly retail trade sales by kind of business NAICS table April 2026; retail sales by NAICS category table monthly seasonally adjusted 2026 nonstore retailers gasoline stations; adv2605.pdf Census advance monthly retail trade May 2026 table 1 estimated monthly sales millions; FRED release tables "Advance Monthly Sales for Retail and Food Services" millions of dollars seasonally adjusted May 2026

- `https://primarynewssource.org/wp-content/uploads/marts_current-34.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.census.gov/retail/releases/historical/marts/adv2604.pdf` -> **snapshot** (snapshot 20260519130340); points raw/verified 15/15
  - p29 Total U.S. retail and food services sales, advance estimate, seasonally adjusted = **755,713** USD millions (monthly total) (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; duplicate of p16/p64 April advance.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p30 Total U.S. retail and food services sales, seasonally adjusted, March 2026 (prel = **760,772** USD millions (monthly total) (2026-03-01..2026-03-31) [DISCARD: Discarded earlier; duplicate of p17/p6 May preliminary.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p31 Total U.S. retail and food services sales, seasonally adjusted, February 2026 (r = **656,082** USD millions (monthly total) (2026-02-01..2026-02-28) [DISCARD: Discarded earlier; implausible February value, duplicate of p18.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p32 Total U.S. retail and food services sales, seasonally adjusted, April 2025 = **722,319** USD millions (monthly total) (2025-04-01..2025-04-30) [DISCARD: Discarded earlier; duplicate of p9 (April 2025).] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p33 Total U.S. retail and food services sales, seasonally adjusted, March 2025 = **726,888** USD millions (monthly total) (2025-03-01..2025-03-31) [DISCARD: Discarded earlier; duplicate of p11 (March 2025).] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p34 Total U.S. retail and food services sales, not adjusted, April 2026 (advance) = **757,085** USD millions (monthly total) (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; duplicate of p13/p16 April not-adjusted.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p35 Total U.S. retail and food services sales, not adjusted, March 2026 (preliminary = **753,370** USD millions (monthly total) (2026-03-01..2026-03-31) [DISCARD: Discarded earlier; duplicate of p14 March not-adjusted.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p36 Total U.S. retail and food services sales, not adjusted, February 2026 (revised) = **741,278** USD millions (monthly total) (2026-02-01..2026-02-28) [DISCARD: Discarded earlier; duplicate of p18 February not-adjusted.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p37 Total U.S. retail and food services sales, not adjusted, April 2025 = **721,903** USD millions (monthly total) (2025-04-01..2025-04-30) [DISCARD: Discarded earlier; duplicate of p10 April 2025.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p38 Total U.S. retail and food services sales, not adjusted, March 2025 = **723,339** USD millions (monthly total) (2025-03-01..2025-03-31) [DISCARD: Discarded earlier; duplicate of p11 March 2025.] quote: "Retail & food services, total ......................................................... 2,846,941 4.1 755,713 760,772 656,082 722,319 726,888 757,085 753,370 741,278 721,903 723,339"
  - p39 Total U.S. retail and food services sales, advance estimate, April 2026, in bill = **757,100,000,000** USD (monthly total) (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; duplicate of p64.] quote: "estimates of U.S. retail and food services sales for April 2026, adjusted for seasonal variation and holiday and trading-day differences, but not for price changes, were $757.1 billion, up 0.5 percent"
  - p40 Total U.S. retail and food services sales, March 2026 revised, in billions (head = **753,400,000,000** USD (monthly total) (2026-03-01..2026-03-31) [DISCARD: Discarded earlier; duplicate of p65.] quote: "March 2026 (revised) $753.4 billion 1.6%"
  - p41 Month-to-month percent change, total retail and food services, April 2026 vs Mar = **0.5** percent (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; duplicate of p66.] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p42 Year-over-year percent change, total retail and food services, April 2026 vs Apr = **4.9** percent (2026-04-01..2026-04-30) [DISCARD: Discarded earlier; duplicate of p67.] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
  - p43 Month-to-month percent change, total retail and food services, March 2026 vs Feb = **1.6** percent (2026-03-01..2026-03-31) [DISCARD: Discarded earlier; duplicate of p25.] quote: "Retail & food services, total .......................................................... 0.5 4.9 1.6 4.2 2.2 4.4"
- `https://www.census.gov/econ/currentdata/?programCode=MRTS&startYear=1992&endYear=2023&categories[` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/release/tables?eid=201281&rid=9&snid=201299` -> **snapshot** (snapshot 20190824123833); points raw/verified 15/15
  - p44 Percent change in Retail Trade and Food Services, seasonally adjusted, Jul 2019  = **0.7** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 total change, redundant with p45.] quote: "\| Retail Trade and Food Services \| 0.7 \| 0.3 \| 0.6 \|"
  - p45 Percent change in Retail Trade and Food Services, seasonally adjusted, Jun 2019  = **0.3** percent (2019-06-01..2019-06-30) [keep: ] quote: "\| Retail Trade and Food Services \| 0.7 \| 0.3 \| 0.6 \|"
  - p46 Percent change in Retail Trade and Food Services, seasonally adjusted, Jul 2018  = **0.6** percent (2018-07-01..2018-07-31) [DISCARD: Discarded earlier; July 2018 total change, not needed.] quote: "\| Retail Trade and Food Services \| 0.7 \| 0.3 \| 0.6 \|"
  - p47 Percent change in Retail Trade and Food Services ex Auto, seasonally adjusted, J = **1** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 ex-auto change, not needed.] quote: "\| Retail Trade and Food Services, ex Auto \| 1.0 \| 0.3 \| 0.6 \|"
  - p48 Percent change in Retail Trade, seasonally adjusted, Jul 2019 = **0.6** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 retail trade change, not needed.] quote: "\| Retail Trade \| 0.6 \| 0.3 \| 0.5 \|"
  - p49 Percent change in Motor Vehicle and Parts Dealers, seasonally adjusted, Jul 2019 = **-0.6** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 motor vehicle change, not needed.] quote: "\| Motor Vehicle and Parts Dealers \| -0.6 \| 0.3 \| 0.4 \|"
  - p50 Percent change in Food and Beverage Stores, seasonally adjusted, Jul 2019 = **0.6** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 food/beverage change, not needed.] quote: "\| Food and Beverage Stores \| 0.6 \| 0.8 \| 0.6 \|"
  - p51 Percent change in Gasoline Stations, seasonally adjusted, Jul 2019 = **1.8** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 gasoline change, redundant with p52.] quote: "\| Gasoline Stations \| 1.8 \| -2.3 \| 0.7 \|"
  - p52 Percent change in Gasoline Stations, seasonally adjusted, Jun 2019 = **-2.3** percent (2019-06-01..2019-06-30) [keep: ] quote: "\| Gasoline Stations \| 1.8 \| -2.3 \| 0.7 \|"
  - p53 Percent change in General Merchandise Stores, seasonally adjusted, Jul 2019 = **0.6** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 general merchandise change, not needed.] quote: "\| General Merchandise Stores \| 0.6 \| 0.1 \| 0.6 \|"
  - p54 Percent change in Nonstore Retailers, seasonally adjusted, Jul 2019 = **2.8** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 nonstore change, redundant with p55.] quote: "\| Nonstore Retailers \| 2.8 \| 1.9 \| 1.0 \|"
  - p55 Percent change in Nonstore Retailers, seasonally adjusted, Jun 2019 = **1.9** percent (2019-06-01..2019-06-30) [keep: ] quote: "\| Nonstore Retailers \| 2.8 \| 1.9 \| 1.0 \|"
  - p56 Percent change in Food Services and Drinking Places, seasonally adjusted, Jul 20 = **1.1** percent (2019-07-01..2019-07-31) [DISCARD: Discarded earlier; July 2019 food services change, redundant with p57.] quote: "\| Food Services and Drinking Places \| 1.1 \| 0.7 \| 1.0 \|"
  - p57 Percent change in Food Services and Drinking Places, seasonally adjusted, Jun 20 = **0.7** percent (2019-06-01..2019-06-30) [keep: ] quote: "\| Food Services and Drinking Places \| 1.1 \| 0.7 \| 1.0 \|"
  - p58 Percent change in Clothing and Clothing Access. Stores, seasonally adjusted, Jul = **1.9** percent (2018-07-01..2018-07-31) [DISCARD: Discarded earlier; July 2018 clothing change, not needed.] quote: "\| Clothing and Clothing Access. Stores \| 0.8 \| -0.1 \| 1.9 \|"

### d3 [forecasts_markets] Professional forecasters and nowcasts

Hypothesis: Published forecasts or nowcasts of June 2026 retail sales (e.g. from banks, forecasting firms, or the Philadelphia Fed survey) provide a direct anchor, though they may share underlying assumptions.

Queries issued by the searcher: June 2026 retail sales forecast advance retail sales; retail sales nowcast June 2026 economists forecast; "May 2026" advance estimates retail and food services sales $ billion Census June 17 2026; "June 2026" retail sales preview economists expect June retail sales released July 16

- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.census.gov/retail/releases/historical/marts/adv2605.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bankingjournal.aba.com/2026/06/aba-databank-retail-sales-surge-in-may/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=667191&year=2026&cty=US&ctyall=1073758175&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Nominal vs real bridge

Hypothesis: Nominal retail sales growth ≈ real sales growth plus retail price inflation; CPI (goods) and PCE goods data can constrain the nominal level if a real-activity indicator is available.

Queries issued by the searcher: CPI May 2026 release consumer price index BLS; advance monthly retail trade survey May 2026 retail sales Census Bureau; PCE price index April 2026 personal income outlays goods consumption BEA release May 2026; real retail sales index 2026 FRED inflation adjusted retail and food services

- `https://approd.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026?topic=smart-beta` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/analysis/retail-sales-strength-looks-more-like-inflation-than-consumer-momentum-200682355` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://investinglive.com/news/us-may-cpi-42-vs-42-yy-expected-20260610/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.indexbox.io/blog/us-personal-income-dips-slightly-in-april-2026-spending-rises-05/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] High-frequency card spending and transaction data

Hypothesis: Aggregate card-spending indices (e.g. Bank of America, Affinity, or Census/other transaction trackers) correlate with retail sales; a June 2026 partial-month reading can indicate direction and magnitude of change.

Queries issued by the searcher: card spending data June 2026 retail sales; consumer spending tracker June 2026 weekly card spending index; CNBC/NRF Retail Monitor May 2026 released June 2026 month over month; "June 2026" card spending data first two weeks consumers mid-June report

- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-june-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fdra.org/latest-news/cnbc-nrf-retail-monitor-shows-sales-grew-again-in-may/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.homepagenews.com/retail-articles/retail-monitor-sales-keep-gaining-despite-uncertain-economy/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nrf.com/research-insights/center-retail-consumer-insights/cnbc-nrf-retail-monitor` -> **snapshot** (snapshot 20260613062725); points raw/verified 2/2
  - p59 Core retail sales month-over-month change, U.S., May 2026 (CNBC/NRF Retail Monit = **0.39** % (2026-05-01..2026-05-31) [keep: ] quote: "The Retail Monitor calculation of core retail sales was up 0.39% month over month in May and up 6.98% year over year."
  - p60 Core retail sales year-over-year change, U.S., May 2026 (CNBC/NRF Retail Monitor = **6.98** % (2026-05-01..2026-05-31) [keep: ] quote: "The Retail Monitor calculation of core retail sales was up 0.39% month over month in May and up 6.98% year over year."

### d6 [shocks] Calendar and macro conditions

Hypothesis: June 2026 has specific calendar features (number of weekends, holidays such as Father's Day, Juneteenth) and macro conditions (inflation, tariffs, interest rates) that shift the seasonal adjustment and level; identifying them constrains deviations from trend.

Queries issued by the searcher: advance monthly retail trade and food services May 2026 Census Bureau; June 2026 calendar Father's Day Juneteenth retail sales calendar effects; June 2026 retail sales forecast economists expect Census advance estimate July 2026 release; national average gasoline price June 2026 Iran war crude oil gasoline prices record

- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/analysis/retail-sales-strength-looks-more-like-inflation-than-consumer-momentum-200682355` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.aastocks.com/sc/(Z(@@n7cjDGdCXMF=acx%7b%7b%7bthis%7d%7d%7dxfs.bxss.me` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jagranjosh.com/general-knowledge/us-federal-holidays-in-june-2026-1820009423-1` -> **snapshot** (snapshot 20260618115831); points raw/verified 7/3
  - p61 Year Juneteenth was enacted into law as a federal holiday (U.S.) = **2,021** year (2021-01-01..2021-12-31) [DISCARD: Discarded earlier; Juneteenth enactment year, not a usable numeric input.] quote: "This is the newest federal holiday in the country, enacted into law in 2021, and it commemorates the end of slavery in America."
  - p62 Flag Day date in 2026 (Sunday, state/local observance, no public sector closures = **14** day of month (June 2026) (2026-06-14..2026-06-14) [DISCARD: Discarded earlier; Flag Day date, not a usable numeric input.] quote: "\| Sunday, June 14 \| Flag Day \| State/Local Observance \| No \|"
  - p63 Author's stated years of journalism experience (Harshita Singh) = **5** years (not stated (page dated 2026-05-30)) [DISCARD: Discarded earlier; irrelevant author biography.] quote: "Harshita Singh is an education and general knowledge journalist with over 5 years of experience in educational writing."
- dropped by code checks: 4 (period_end 2026-06-30 after as_of: 1; period_end 2026-06-19 after as_of: 1; period_end 2026-06-21 after as_of: 2)

### b1 [forecasts_markets] Consensus nowcast

Hypothesis: A published June 2026 retail sales nowcast (bank/firm or Philadelphia Fed survey) would directly anchor the June level and resolve whether the recent +0.9% May pace continues; it would unlock a direct forecast route (d3) independent of the series extrapolation.

Queries issued by the searcher: Philadelphia Fed Survey of Professional Forecasters retail sales forecast 2026; retail sales June 2026 forecast consensus advance monthly retail trade; "retail sales" May 2026 advance estimate $ billion "June 16, 2026" Census; Econoday retail sales preview June 2026 "for Jun" consensus outlook released June 2026

- `https://bankingjournal.aba.com/2026/07/retail-sales-edged-up-0-2-in-june/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cmegroup.econoday.com/byevent?fid=667191&year=2026&cty=US&ctyall=1073758175&lid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.advisorperspectives.com/dshort/updates/2026/06/17/retail-sales-may-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.investing.com/analysis/retail-sales-strength-looks-more-like-inflation-than-consumer-momentum-200682355` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Card-spend partial month

Hypothesis: A June 2026 partial-month card-spend reading (CNBC/NRF Retail Monitor, BofA, Affinity) would provide a within-month directional signal for June, converting the May-only monitor (p59/p60) into a June nowcast and reducing uncertainty on the m/m change factor.

Queries issued by the searcher: CNBC NRF Retail Monitor June 2026; Bank of America card spending June 2026 retail; Bank of America Institute Consumer Checkpoint June 2026 card spending; CNBC/NRF Retail Monitor May 2026 retail sales report released June 2026

- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-june-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gurufocus.com/news/8911966/bank-of-america-reports-resilience-among-lowerincome-consumers-amid-inflation` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://convenience.org/stay-current/news/2026/july/21/nrf-retail-sales-rose-in-june` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-july-2026.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [own_history] Seasonal factor

Hypothesis: The June seasonal factor (SA/NSA ratio) from the Census MARTS seasonal adjustment files would let the not-adjusted June level be converted to the SA target, completing a partial_period/seasonal route and constraining the June level independently of trend extrapolation.

Queries issued by the searcher: Census MARTS seasonal adjustment factors table June total retail and food services; Advance Monthly Retail Trade Survey seasonal adjustment factors download; "Combined Seasonal, Trading-Day, and Holiday Adjustment Factors" retail food services sales kinds of business 2026; census.gov retail marts sa factor table "44X72" total retail and food services seasonal factor

- `https://www.census.gov/retail/marts/www/adfactor.html` -> **snapshot** (snapshot 20250421144420); points raw/verified 0/0
- `https://www2.census.gov/retail/releases/historical/marts/adv2604.pdf` -> **snapshot** (snapshot 20260519130340); points raw/verified 15/5
  - p64 Retail & food services total, seasonally adjusted, April 2026 advance estimate ( = **757,100,000,000** USD (2026-04-01..2026-04-30) [keep: ] quote: "Advance estimates of U.S. retail and food services sales for April 2026, adjusted for seasonal variation and holiday and trading-day differences, but not for price changes, were $757.1 billion"
  - p65 Retail & food services total, seasonally adjusted, March 2026 revised (headline) = **753,400,000,000** USD (2026-03-01..2026-03-31) [keep: ] quote: "March 2026 (revised) $753.4 billion 1.6%"
  - p66 Retail & food services total, month-to-month percent change, April 2026 vs March = **0.5** percent (2026-04-01..2026-04-30) [keep: ] quote: "were $757.1 billion, up 0.5 percent (±0.4 percent) from the previous month"
  - p67 Retail & food services total, year-over-year percent change, April 2026 vs April = **4.9** percent (2026-04-01..2026-04-30) [keep: ] quote: "and up 4.9 percent (±0.5 percent) from April 2025"
  - p68 Retail & food services total, median CV of current month (sampling variability) = **1** percent (2026-04-01..2026-04-30) [keep: ] quote: "Retail & food services, total ........................................................... 1.0 0.2 0.1 0.3 0.0 0.1"
- `https://www.census.gov/econ/currentdata/?programCode=MARTS&startYear=2014&endYear=2024&categories[` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fred.stlouisfed.org/release/tables?eid=201301&rid=9&snid=201312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (scale word 'million' not supported by quote or table header: 10)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['retail sales', 'us consumer', 'census retail']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p6', 'p3'] Same May 2026 advance total: headline $763.7B, Table 1 SA level 763,705 million, and +0.9% m/m are internally consistent (763,705/757,036 ≈ +0.9%).
- corroborating: ['p2', 'p7', 'p5'] April 2026 revised level 757,036 million matches headline $757.0B and the revised +0.4% m/m from March 754,013.
- conflicting: ['p8', 'p11'] March 2026 revised (754,013) vs March 2025 revised (722,442) are different years, not a conflict; but note p17/p30 give March 2026 preliminary 760,772, later revised down to 754,013 — a revision of ~0
- corroborating: ['p16', 'p29', 'p39'] Three copies of the April 2026 advance total (755,713 million; $757.1B headline rounds differently) — same underlying release, not independent.
- corroborating: ['p17', 'p30', 'p40'] March 2026 preliminary 760,772 million / $753.4B headline — same release vintage, redundant.
- corroborating: ['p18', 'p31'] February 2026 revised 656,082 million — identical duplicate; the low value looks anomalous relative to neighbors (possible transcription issue) and should not be used as a trend anchor.
- corroborating: ['p19', 'p32'] April 2025 722,319 million — duplicate.
- corroborating: ['p20', 'p33'] March 2025 726,888 million — duplicate.
- corroborating: ['p21', 'p22', 'p23'] April/March/February 2025 revised values from the May 2026 release; consistent with p9/p10 vintage.
- conflicting: ['p9', 'p10', 'p19', 'p32'] May 2025 revised 722,319 (p9) equals April 2025 (p10/p19/p32) — likely a column-alignment artifact in the quoted table; treat 2025 monthly levels with caution.
- corroborating: ['p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] 2018–2019 component m/m changes: useful only as a base-rate distribution of June/July monthly moves, not as current levels.
- corroborating: ['p59', 'p60'] CNBC/NRF card-spend monitor for May 2026: +0.39% m/m core, +6.98% y/y — directionally consistent with Census May +0.9% total and +6.9% y/y; different scope (core, card-based) so a directional check on
- corroborating: ['p61', 'p62', 'p63'] Calendar context: Juneteenth federal holiday since 2021, Flag Day 2026 on Sunday — minor seasonal-adjustment context; p63 (journalist experience) is irrelevant.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p6', 'p3'] Same May 2026 advance release: headline level ($763.7B), Table 1 SA level (763,705M) and +0.9% m/m are internally consistent (763,705/757,036 ≈ +0.88%). These are one measurement, not independent conf
- corroborating: ['p2', 'p7', 'p5'] April 2026 revised level ($757.0B headline; 757,036M Table 1) and the revised +0.4% m/m from March (754,013M) agree. Same release, same underlying survey.
- corroborating: ['p8', 'p11', 'p10', 'p9'] March 2026 (754,013M) vs March 2025 (722,442M) and April 2026 (757,036M) vs April 2025 (714,568M) give y/y growth of roughly 4.4% and 5.9%; May 2026 vs May 2025 (722,319M) gives 5.7% on Table 1 levels
- corroborating: ['p64', 'p65', 'p66', 'p67', 'p24', 'p25', 'p26', 'p27'] Prior-vintage (May 14, 2026) April advance release: $757.1B, +0.5% m/m, +4.9% y/y. The June 17 vintage revised April to 757,036M and +0.4% m/m — a small downward revision consistent with p15/p28 media
- corroborating: ['p15', 'p28', 'p68'] Revision and sampling-variability statistics: median absolute revision ~0.1% and CV ~1%. These bound how far the advance June figure can sit from the eventual revised value and set the plausible noise
- corroborating: ['p59', 'p60'] CNBC/NRF Retail Monitor (card-transaction based) May 2026: core retail +0.39% m/m, +6.98% y/y. Different scope (core, excludes autos/gasoline/food services) and different measurement (card panel), so 
- corroborating: ['p45', 'p52', 'p55', 'p57'] June 2019 component m/m changes (total +0.3%, gasoline -2.3%, nonstore +1.9%, food services +0.7%) are a historical analogue for June seasonal/component behavior; old and only weakly transferable to 2

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | June 2026 m/m change factor applied to May 2026 SA level | 1.004 | 0.985..1.023 | 0.8978..1.122 (widened) | ratio | m1 (m1) | Recent m/m changes: May +0.9% (p3), April +0.4% (p5), March +1.6% (p25). June typically shows modest positive growth; a central +0.4% with a range spanning roughly -1.5% to +2.3% reflects the ~1% CV (p68) and ~0.1% revision noise (p15) plus genuine month-to-month volatility. | June 2026 continues the recent trend without a major shock; May's +0.9% is not fully reversed. | A June card-spend or nowcast reading showing a sharp contraction or a >2.5% jump. |
| a2 | June 2026 y/y growth factor relative to May 2025 | 1.055 | 1.03..1.08 | 0.9434..1.179 (widened) | ratio | unused | Recent y/y growth: May +6.9% (p4), April +4.9% (p26), Table 1 levels imply ~5.7% May y/y. A central ~5.5% with a range 3%-8% reflects deceleration from the May headline and normal volatility. | Nominal growth continues near the recent 5-7% pace. | A June CPI or card-spend reading implying nominal growth outside 3-8%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 766,401 | ['p6'] / ['a1'] | [] |  | 1.00 | B1 (only block) |  |
| m2 | series_auto | n/a | ['p11', 'p10', 'p9', 'p8', 'p7', 'p6'] / [] | [] |  | 0.00 |  | series_auto: needs last year's value for the target month (2025-06) |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p6 * a1; Monte Carlo P10 to P90 618,051 to 947,681; result unit USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 1 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 766,401 (width x/÷1.38, no error evidence, code's default width). Estimate = the only block.
- Interval: one block, so the interval is that block's own width (x/÷1.38).

Result: central **766,401** USD, 80% interval [556,305, 1,055,841] USD, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule single_block, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total U.S. retail and food services sales for June 2026 (seasonally adjusted, holiday/trading-day adjusted, not price-adjusted, monthly total) is 766,401 USD (80% model-based interval 556,305 to 1,055,841 USD).

The estimate rests on the observed May 2026 level of 763,705 millions of USD, extrapolated by an assumed June m/m factor of 1.004 (range 0.8978 to 1.122). Only 1 method contributed, at weight 100%; the series route was unusable, so the combination is effectively a single block rather than independent corroboration. The interval is conditional on that assumption, not a demonstrated accuracy guarantee.

Observed inputs include 757,036 millions of USD, 754,013 millions of USD, 722,319 millions of USD, 714,568 millions of USD, and 722,442 millions of USD; the June factor is an analyst assumption, not observed.

The main risk is that the assumed June m/m factor is wrong, since the whole estimate hinges on it. Better evidence would be a longer run of consecutive monthly SA levels enabling a genuine seasonal/y-y extrapolation with backtest error.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 June 2026 m/m change factor applied to May 2026 SA level: 1.004 ratio, range 0.8978 to 1.122 (range widened by code); used by m1. Overturned by: A June card-spend or nowcast reading showing a sharp contraction or a >[n] jump.

Method details (computed by code):
- m1 formula_mc: p6 * a1; Monte Carlo P10 to P90 618,051 to 947,681; result unit USD converted to USD; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 1 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 766,401 (width x/÷1.38, no error evidence, code's default width). Estimate = the only block.
- Interval: one block, so the interval is that block's own width (x/÷1.38).

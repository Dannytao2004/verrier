# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births in Japan during July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which include foreign nationals residing in Japan). | unit births | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (MHLW), Japan

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW vital statistics time series

Hypothesis: July 2026 births can be estimated by applying the typical July seasonal factor and recent year-over-year trend to the most recent monthly or annual birth counts available before the cutoff.

Queries issued by the searcher: MHLW 人口動態統計 月報 出生数 2026; Japan monthly vital statistics births 2025 2026 preliminary; 人口動態統計速報 2025年 月別 出生数 1月 2月 3月 推移; 令和7年 2025年 出生数 月別 速報 累計 人口動態統計 6月 7月

- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/en/japan-data/h02872/japan-births-edge-up-in-first-half-of-2026-after-a-decade-of-decline.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e6%9c%88%e5%a0%b1%e8%aa%bf%e6%95%b4%e4%bf%82/page/3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/01.html` -> **snapshot** (snapshot 20260410161952); points raw/verified 0/0

### d2 [related_series] MHLW annual vital statistics and quarterly estimates

Hypothesis: The July 2026 monthly figure is a share of the annual total; if a reliable annual forecast or year-to-date total is available, the monthly value can be derived using historical monthly shares.

Queries issued by the searcher: MHLW 人口動態統計 月次 出生数 2026年6月 速報; Japan births 2025 annual total 人口動態統計 出生数 2025年; 人口動態統計速報 2026年5月分 出生数; 月別 出生数 2025年 7月 人口動態統計 月報 概数

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7houdou.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202512h.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [forecasts_markets] Demographic forecasts and expert projections

Hypothesis: Published forecasts for Japan's 2026 births or monthly estimates from research institutes can be used directly or as a sanity check for the July 2026 figure.

Queries issued by the searcher: Japan 2026 birth forecast IPSS 出生数 予測; IPSS 将来推計人口 2026年 出生数 予測; 2026年上半期 出生数 34万2068人 厚生労働省 速報; Japan births first half 2026 rose 11 years population estimates

- `https://www.ipss.go.jp/pp-zenkoku/e/zenkoku_e2023/pp2023e_Summary.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chiba-tv.com/plus/detail/202506339182` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Municipal or prefectural birth registrations

Hypothesis: Aggregating birth registrations from major municipalities or prefectures for July 2026 can provide a lower-bound or proxy for the national total, scaled by their historical share of national births.

Queries issued by the searcher: 東京都 出生数 2026年7月; 大阪市 出生届 2026年7月 出生数; 東京都 人口動態統計 月報 出生数 令和8年7月; 大阪市 出生数 2026年 月別 推計人口

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260829-GYT1T00068/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asahi.com/articles/ASV8X3GN7V8XUTFL015M.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businesstimes.com.sg/international/tokyo-reverses-baby-bust-ai-matchmaking-and-generous-subsidies` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [administrative] Birth registration and family register data

Hypothesis: Birth registrations filed in July 2026 (or the number of birth certificates issued) can serve as a proxy for births, though registration timing may lag actual birth by a few days.

Queries issued by the searcher: 出生届 件数 2026年7月; 人口動態統計 速報 2026年 出生数 月別; 人口動態統計速報 2026年6月分 出生数 5万9846人 前年同月比; 人口動態統計速報 令和7年7月分 出生数 前年同月比

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://research.nicoxz.com/articles/japan-births-post-covid-bottoming` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [base_rates] Demographic accounting

Hypothesis: July 2026 births can be estimated from the population of women of childbearing age and age-specific fertility rates, adjusted for seasonality.

Queries issued by the searcher: Japan female population 2026 age 15-49 人口推計 2026 女性 年齢別; Japan total fertility rate 2025 2026 age-specific fertility rates 合計特殊出生率; 人口動態統計 月別 出生数 2025年 7月 速報 厚生労働省; 日本 出生数 月別 季節性 7月 多い 月別出生数 2024

- `https://www.stat.go.jp/data/jinsui/pdf/202605.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/07.html` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.ipss.go.jp/syoushika/bunken/data/pdf/jinkokenshiryo353.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d7 [physical_flow] Hospital and maternity clinic discharge counts

Hypothesis: The number of births in July 2026 can be approximated by the number of maternity ward discharges or delivery admissions in a sample of hospitals, scaled to national coverage.

Queries issued by the searcher: Japan hospital deliveries July 2026 分娩数 病院; MHLW 人口動態統計速報 2026年7月 出生数; 分娩数 2026年7月 病院 産科 統計; 2025年7月 出生数 人口動態統計速報 前年同月

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/07.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://tsubaki-wc.com/obstetrics/medical_experience.html` -> **snapshot** (snapshot 20260414175600); points raw/verified 15/14
  - p1 Total deliveries at this clinic, July 2025 = **61** deliveries (2025-07-01..2025-07-31) [keep: ] quote: "\| 総分娩数 \| 58 \| 51 \| 50 \| 45 \| 74 \| 62 \| 61 \| 74 \| 51 \| 62 \| 55 \| 59 \| 702 \|"
  - p2 Total deliveries at this clinic, July 2024 = **49** deliveries (2024-07-01..2024-07-31) [keep: ] quote: "\| 総分娩数 \| 63 \| 52 \| 36 \| 47 \| 62 \| 45 \| 49 \| 47 \| 55 \| 63 \| 59 \| 53 \| 631 \|"
  - p3 Total deliveries at this clinic, July 2023 = **64** deliveries (2023-07-01..2023-07-31) [keep: ] quote: "\| 総分娩数 \| 46 \| 45 \| 55 \| 54 \| 42 \| 47 \| 64 \| 52 \| 49 \| 52 \| 60 \| 63 \| 629 \|"
  - p4 Total deliveries at this clinic, July 2022 = **64** deliveries (2022-07-01..2022-07-31) [keep: ] quote: "\| 総分娩数 \| 60 \| 56 \| 49 \| 40 \| 49 \| 52 \| 64 \| 61 \| 62 \| 66 \| 50 \| 41 \| 650 \|"
  - p5 Total deliveries at this clinic, July 2021 = **56** deliveries (2021-07-01..2021-07-31) [keep: ] quote: "\| 総分娩数 \| 40 \| 61 \| 61 \| 64 \| 57 \| 56 \| 56 \| 60 \| 58 \| 57 \| 57 \| 59 \| 686 \|"
  - p6 Total deliveries at this clinic, July 2020 = **52** deliveries (2020-07-01..2020-07-31) [keep: ] quote: "\| 総分娩数 \| 48 \| 42 \| 54 \| 45 \| 50 \| 49 \| 52 \| 84 \| 46 \| 55 \| 53 \| 56 \| 634 \|"
  - p7 Total deliveries at this clinic, July 2019 = **59** deliveries (2019-07-01..2019-07-31) [keep: ] quote: "\| 総分娩数 \| 50 \| 49 \| 50 \| 46 \| 55 \| 56 \| 59 \| 58 \| 47 \| 49 \| 51 \| 50 \| 620 \|"
  - p8 Total deliveries at this clinic, July 2018 = **43** deliveries (2018-07-01..2018-07-31) [keep: ] quote: "\| 総分娩数 \| 50 \| 34 \| 52 \| 54 \| 44 \| 41 \| 43 \| 59 \| 56 \| 43 \| 38 \| 59 \| 573 \|"
  - p9 Total deliveries at this clinic, July 2017 = **54** deliveries (2017-07-01..2017-07-31) [keep: ] quote: "\| 総分娩数 \| 47 \| 44 \| 39 \| 60 \| 34 \| 47 \| 54 \| 77 \| 56 \| 61 \| 44 \| 55 \| 618 \|"
  - p10 Total deliveries at this clinic, July 2016 = **48** deliveries (2016-07-01..2016-07-31) [keep: ] quote: "\| 総分娩数 \| 38 \| 31 \| 43 \| 43 \| 56 \| 47 \| 48 \| 51 \| 38 \| 43 \| 38 \| 51 \| 527 \|"
  - p11 Total deliveries at this clinic, January–April 2026 cumulative = **229** deliveries (2026-01-01..2026-04-30) [keep: ] quote: "\| 総分娩数 \| 62 \| 59 \| 54 \| 54 \| \| \| \| \| \| \| \| \| 229 \|"
  - p12 Total deliveries at this clinic, calendar year 2025 = **702** deliveries (2025-01-01..2025-12-31) [keep: ] quote: "\| 総分娩数 \| 58 \| 51 \| 50 \| 45 \| 74 \| 62 \| 61 \| 74 \| 51 \| 62 \| 55 \| 59 \| 702 \|"
  - p13 Normal vaginal deliveries at this clinic, July 2025 = **43** deliveries (2025-07-01..2025-07-31) [DISCARD: Sub-component of p1 (normal vaginal deliveries in July 2025); adds no independent information for a national July 2026 e] quote: "\| 正常経膣分娩 \| 44 \| 33 \| 35 \| 32 \| 58 \| 45 \| 43 \| 55 \| 39 \| 45 \| 39 \| 46 \| 514 \|"
  - p14 Cesarean deliveries at this clinic, July 2025 = **11** deliveries (2025-07-01..2025-07-31) [DISCARD: Sub-component of p1 (cesarean deliveries in July 2025); redundant with the total-delivery series and not usable as a sep] quote: "\| 帝王切開 \| 5 \| 5 \| 5 \| 4 \| 7 \| 8 \| 11 \| 5 \| 3 \| 5 \| 7 \| 3 \| 68 \|"
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### d8 [shocks] Calendar and policy effects

Hypothesis: July 2026 births may be affected by the number of days, weekends, holidays, and any major policy changes (e.g., fertility incentives) that alter conception timing or reporting. Adjusting a baseline for these factors improves the estimate.

Queries issued by the searcher: MHLW monthly vital statistics preliminary Japan births 2025 monthly; Japan births July 2026 monthly estimate 厚生労働省 人口動態統計 月報; 2026年7月 出生数 人口動態統計速報 令和8年7月分; Japan public holidays 2026 calendar Marine Day July 20

- `https://caixinboke1.blog.caixin.com/archives/288480` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.zhihu.com/column/c_1639320595354652672` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=447111&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] national administrative

Hypothesis: Monthly or year-to-date birth counts for 2026 from MHLW preliminary vital statistics (e.g., January–May 2026) would provide the most recent national level and trend. Applying the historical July share of the annual total or a July seasonal factor to a 2026 year-to-date total would unlock a direct national monthly estimate, replacing the clinic-only analogue.

Queries issued by the searcher: MHLW preliminary vital statistics 2026 births monthly January February March April May; 厚生労働省 人口動態統計速報 2026年 出生数; 人口動態統計速報 令和7年7月分 出生数 2025年7月; 日本の月別出生数 2024年 7月 年間出生数に占める割合 月別シェア

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [forecasts_markets] research institute

Hypothesis: Published 2026 annual birth forecasts from Japanese research institutes (e.g., IPSS, NIPSSR, or university demographers) would provide an independent annual anchor. Combined with the historical July share of annual births, this would yield a national July 2026 estimate and serve as a sanity check on any clinic-based scaling.

Queries issued by the searcher: IPSS Japan 2026 birth forecast annual live births estimate; Japan 2026年 出生数 予測 推計 国立社会保障・人口問題研究所; 厚生労働省 人口動態統計 月報 2026年7月 出生数; 日本 出生数 月別 構成比 7月 年間出生数 割合

- `https://www.ipss.go.jp/pp-zenkoku/e/zenkoku_e2023/pp2023e_Summary.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.shugiin.go.jp/Internet/itdb_shitsumon.nsf/html/shitsumon/b216033.htm` -> **snapshot** (snapshot 20260209055049); points raw/verified 4/0
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (number: no number in value_as_written: 4)

### b3 [related_series] subnational administrative

Hypothesis: Monthly birth counts for July 2026 from major municipalities or prefectures (e.g., Tokyo, Osaka, Aichi) would provide a broader geographic proxy than a single clinic. Scaling by those areas' historical share of national births would give a national estimate and help validate or correct the clinic-based trend.

Queries issued by the searcher: 厚生労働省 人口動態統計 2026年7月 出生数 速報; 東京都 2026年7月 出生数 月報 人口動態; 東京都 人口動態統計 2026年 月別 出生数 速報 都内; "2026年6月" 人口動態統計速報 出生数 都道府県別 東京都 愛知県 大阪府

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/07.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.straitstimes.com/asia/east-asia/tokyo-reverses-baby-bust-with-ai-matchmaking-and-generous-subsidies` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan births', 'july 2026 births', 'vital statistics']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'] These are July delivery counts from the same single clinic for 2016–2025. They form a consistent same-clinic July series, but they are one small clinic's experience, not a national sample. They can on
- corroborating: ['p1', 'p12'] p1 is the July 2025 component of the calendar-year 2025 total p12 from the same clinic. They are internally consistent but not independent; p12 adds annual context only.
- corroborating: ['p1', 'p13', 'p14'] p13 and p14 are subcategories of p1 (normal vaginal plus cesarean deliveries) for July 2025 at the same clinic. They confirm the clinic's July 2025 delivery count but are not independent observations 
- corroborating: ['p11', 'p12'] p11 is the January–April 2026 cumulative count at the same clinic; p12 is the 2025 annual total. They are from the same source and can be used only as a within-clinic trend signal, not as a national b
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'] All are the same clinic's July total-delivery counts across consecutive years, so they form one consistent series measuring the same quantity (deliveries at one facility in July). They corroborate eac
- corroborating: ['p1', 'p13', 'p14'] For July 2025 the clinic reports 61 total deliveries, split into 43 normal vaginal and 11 cesarean (43+11=54, leaving 7 other/unspecified modes). These are internally consistent components of the same
- corroborating: ['p11', 'p12'] January–April 2026 cumulative (229) and calendar-year 2025 (702) are the same clinic's counts on a different period basis. They are consistent with the monthly series (2025 monthly values sum to 702) 
- conflicting: ['p1', 'p11'] Apparent tension only: p1 is July 2025 (61) while p11 is Jan–Apr 2026 cumulative (229, i.e. ~57/month). Different periods and aggregation, so not a true contradiction; it does indicate the clinic's 20

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | National July 2026 live births per clinic July delivery (scaling factor) | 1,100 | 550..2,200 | 550..2,200 | births per clinic delivery | m1 (m1), m2 (m2) | The clinic records roughly 50-65 deliveries per July (p1-p3). Japan's national monthly live births in recent years are on the order of 60,000-80,000, so the national-to-clinic ratio is of order 1e3, not 1e5. This factor absorbs both the national/clinic size ratio and the delivery-to-live-birth defin | The clinic's July delivery count is assumed to move proportionally with national July live births, so that a fixed multiplicative scaling transfers the clinic analogue to the national level. | Evidence that the clinic's share of national births changed materially between 2025 and 2026, or a published national monthly birth figure that implies a ratio far outside this range. |
| a2 | Year-over-year change factor for national July 2026 live births relative to July 2025 | 0.96 | 0.9..1.02 | 0.857..1.071 (widened) | ratio | m2 (m2) | Japan's births have been declining gradually; a modest further decline in July 2026 versus July 2025 is the central expectation. The range spans a continued decline to near-stabilisation, consistent with the clinic's own 2026 run-rate being close to its 2025 level (p11 vs p12). This is a dimensionle | Used to carry a July 2025 national level forward to July 2026 when no 2026 national monthly data are available. | A published 2026 year-to-date national birth count showing growth or a much steeper decline than this range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 64,331 | ['p1', 'p2', 'p3'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 61,628 | ['p1', 'p2', 'p3'] / ['a1', 'a2'] | [] |  | 0.50 | equal |  |

Result: central **62,965**, 80% interval [30,888, 128,351], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births in Japan during July 2026, as first reported in MHLW's preliminary monthly vital statistics (including foreign nationals residing in Japan), is 62,965 births. The supplied interval is 30,888 to 128,351, a model-based range conditional on the stated assumptions rather than a demonstrated accuracy guarantee.

Two methods were combined with weights 50% and 50%: 64,331 and 61,628. Both scale a single clinic's recent July delivery level (observed points 12) to national births using assumption a1 = 1,100 (range 550–2,200); the second adds a year-over-year factor a2 = 0.96 (range 0.857–1.071). The clinic data are observed; the national scaling and trend are analyst assumptions, not measurements.

The main risk is that one clinic's deliveries poorly proxy national births, and the scaling factor is unverified. The most valuable missing evidence would be actual national July 2026 counts or a representative sample of clinics.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 National July 2026 live births per clinic July delivery (scaling factor): 1,100 births per clinic delivery, range 550 to 2,200; used by m1, m2. Overturned by: Evidence that the clinic's share of national births changed materially between 2025 and 2026, or a published national monthly birth figure that implies a ratio far outside this range.
- a2 Year-over-year change factor for national July 2026 live births relative to July 2025: 0.96 ratio, range 0.857 to 1.071 (range widened by code); used by m2. Overturned by: A published [n] year-to-date national birth count showing growth or a much steeper decline than this range.

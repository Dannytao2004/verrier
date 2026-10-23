# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of internal migration events (moves of individuals between municipalities within Japan) recorded in the Basic Resident Registration system and reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration, for moves occ | unit person (moves) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan (Ministry of Internal Affairs and Communications)

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau monthly report time series

Hypothesis: August 2026 internal migration events are close to August values in prior years (2019-2025), adjusted for trend and any structural break from COVID-era patterns; August is typically a high-move month due to summer relocations.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 移動者数 外国人含む; 統計局 住民基本台帳人口移動報告 2026年 月次 移動者数; Report on Internal Migration in Japan Derived from Basic Resident Registration August 2025 total; e-Stat 住民基本台帳人口移動報告 月報 表1 移動者数 時系列 2018年 2026年7月; stat.go.jp 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 時系列表 月別 市区町村間移動者数 2018 2019 2020 2021 2022 2023 2024 2025

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecitizen.jp/Statdb/StatsData/0003423613` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Annual internal migration totals and monthly shares

Hypothesis: Annual internal migration total multiplied by the historical August share of the annual total gives an August estimate; the August share is fairly stable across years.

Queries issued by the searcher: 人口移動報告 年次 総移動者数 月別内訳; Japan internal migration annual total 2024 Statistics Bureau Report on Internal Migration Basic Resident Registration; 統計局 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; stat.go.jp idou 2025np jissu 市区町村間移動者数 月別 8月 移動者

- `https://www.stat.go.jp/data/idou/2024np/jissu/pdf/all.pdf` -> **snapshot** (snapshot 20250516005632); points raw/verified 15/13
  - p1 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p2 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p3 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,310,972** persons (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p4 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,247,744** persons (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p5 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,255,721** persons (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p6 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,403,465** persons (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p7 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,359,174** persons (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p8 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,318,617** persons (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p9 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,251,717** persons (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p10 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,384,553** persons (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p11 Annual internal migration (inter-municipal movers, Japanese + foreign), Japan, 2 = **5,207,599** persons (moves) (2014-01-01..2014-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p12 Inter-municipal migration rate (movers as % of Basic Resident Register populatio = **4.17** % of registered population (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動率 4.05 4.20 4.10 4.16 4.20 4.24 4.13 4.14 4.22 4.20 4.17"
  - p13 Inter-municipal migration rate (movers as % of Basic Resident Register populatio = **4.2** % of registered population (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動率 4.05 4.20 4.10 4.16 4.20 4.24 4.13 4.14 4.22 4.20 4.17"
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsMeta/0003419960` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/en/stat-search/files?layout=normal&kikan=00200&toukei=00200523&tstat=000000070001` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 2)

### d3 [related_series] Foreign resident subset

Hypothesis: Foreign resident internal moves are a growing share of total moves; combining a Japanese-only August baseline with a foreign-resident August estimate (from foreign population and mobility rates) reconstructs the combined total.

Queries issued by the searcher: 人口移動報告 外国人 移動者数 月別; foreign residents internal migration Japan monthly statistics 住民基本台帳 移動者数 外国人; 住民基本台帳人口移動報告 2025年8月結果 外国人移動者 市区町村間移動者数; stat.go.jp idou rireki 2605 2026年5月結果 全国の移動者数 移動者 日本人移動者 外国人移動者

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/new.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 14/13
  - p14 Total population of Japan, August 1 2026 (provisional estimate) = **122,680,000** as written "1億2268万人", value check failed persons (2026-08-01..2026-08-01) [keep: ] quote: "【2026年(令和8年)8月1日現在(概算値)】 <総人口> 1億2268万人で、前年同月に比べ減少"
  - p15 Year-on-year change in total population, August 2026 (provisional estimate) = **590,000** persons (2026-08-01..2026-08-01) [keep: ] quote: "<総人口> 1億2268万人で、前年同月に比べ減少 ▲59万人 (▲0.48%)"
  - p16 Year-on-year percent change in total population, August 2026 (provisional estima = **0.48** % (2026-08-01..2026-08-01) [keep: ] quote: "▲59万人 (▲0.48%)"
  - p17 Total population of Japan, March 1 2026 (final value based on 2020 Census) = **122,811,000,000** as written "1億2281万1千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Value carries a spurious 1e3 multiplier (122,811,000,000) inconsistent with the quoted 1億2281万1千人; the correct figure is] quote: "【2026年(令和8年)3月1日現在(令和2年国勢調査を基準とする確定値)】 <総人口> 1億2281万1千人で、前年同月に比べ減少"
  - p18 Year-on-year change in total population, March 2026 (final value) = **610,000** persons (2026-03-01..2026-03-01) [keep: ] quote: "▲61万人 (▲0.49%)"
  - p19 Population aged under 15, March 2026 (final value) = **13,319,000,000** as written "1331万9千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (13,319,000,000) vs quoted 1331万9千人; age breakdown not needed for the estimate.] quote: "・15歳未満人口は 1331万9千人で、前年同月に比べ減少 ▲36万人 (▲2.63%)"
  - p20 Population aged 15-64, March 2026 (final value) = **73,290,000** persons (2026-03-01..2026-03-01) [keep: ] quote: "・15~64歳人口は 7329万人で、 前年同月に比べ減少 ▲26万5千人 (▲0.36%)"
  - p21 Population aged 75 and over, March 2026 (final value) = **21,488,000,000** as written "2148万8千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (21,488,000,000) vs quoted 2148万8千人; age breakdown not needed.] quote: "うち75歳以上人口は 2148万8千人で、前年同月に比べ増加 47万9千人 ( 2.28%)"
  - p22 Japanese population, March 2026 (final value) = **118,989,000,000** as written "1億1898万9千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (118,989,000,000) vs quoted 1億1898万9千人; Japanese population level not needed separately from tot] quote: "<日本人人口> 1億1898万9千人で、前年同月に比べ減少 ▲86万6千人 (▲0.72%)"
  - p23 Year-on-year change in Japanese population, March 2026 (final value) = **-866,000,000** as written "▲86万6千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (-866,000,000) vs quoted ▲86万6千人; redundant with p22.] quote: "<日本人人口> 1億1898万9千人で、前年同月に比べ減少 ▲86万6千人 (▲0.72%)"
  - p24 Foreign population, March 2026 (final value) = **3,821,000,000** as written "382万1千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (3,821,000,000) vs quoted 382万1千人; foreign population level is better taken from the quoted text] quote: "<外国人人口> 382万1千人で、前年同月に比べ増加 25万7千人 ( 7.20%)"
  - p25 Year-on-year change in foreign population, March 2026 (final value) = **257,000,000** as written "25万7千人", value check pending persons (2026-03-01..2026-03-01) [DISCARD: Spurious 1e3 multiplier (257,000,000) vs quoted 25万7千人; redundant with p26 growth rate.] quote: "<外国人人口> 382万1千人で、前年同月に比べ増加 25万7千人 ( 7.20%)"
  - p26 Year-on-year percent change in foreign population, March 2026 (final value) = **7.2** % (2026-03-01..2026-03-01) [keep: ] quote: "25万7千人 ( 7.20%)"
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d4 [administrative] Municipal resident registration offices

Hypothesis: The number of transfer-of-residence notifications (転入届/転出届) processed nationally in August approximates the reported migration events, since the report is derived from these registrations.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 転入者数 転出者数; 転入届 転出届 月別 全国 件数 統計; stat.go.jp 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数 月結果; 住民基本台帳人口移動報告 利用上の注意 移動者 定義 市区町村間移動者 転入 転出 同一市区町村内の移動

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p27 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2025 = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p28 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2025 (table 1) = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Redundant duplicate of p27 (same 2025 annual total, same source).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p29 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2024 = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p30 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2023 = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p31 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2022 = **5,310,972** persons (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p32 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2021 = **5,247,744** persons (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p33 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2020 = **5,255,721** persons (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p34 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2019 = **5,403,465** persons (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p35 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2018 = **5,359,174** persons (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p36 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2017 = **5,318,617** persons (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p37 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2016 = **5,251,717** persons (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p38 National inter-municipal movers (市区町村間移動者数), Japan, calendar year 2015 = **5,384,553** persons (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p39 National inter-prefectural movers (都道府県間移動者数), Japan, calendar year 2025 = **2,515,731** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p40 National intra-prefectural movers (都道府県内移動者数), Japan, calendar year 2025 = **2,674,817** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p41 Year-on-year change rate of national inter-municipal movers, Japan, 2025 vs 2024 = **-0.3** percent (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p42 National inter-municipal movers (市区町村間移動者数), all movers, October 2025 = **379,751** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p43 National inter-municipal movers (市区町村間移動者数), all movers, October 2024 = **378,202** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p44 National inter-municipal movers, Japanese movers only, October 2025 = **321,850** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p45 National inter-municipal movers, foreign movers only, October 2025 = **57,901** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p46 National inter-prefectural movers (都道府県間移動者数), all movers, October 2025 = **168,057** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p47 National intra-prefectural movers (都道府県内移動者数), all movers, October 2025 = **211,694** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p48 National in-migrants (転入者数), all movers, October 2025 = **168,057** persons (2025-10-01..2025-10-31) [DISCARD: National in-migrants equals inter-prefectural movers (168,057) and is a duplicate of p46; adds no independent informatio] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p49 National out-migrants (転出者数), all movers, October 2025 = **168,057** persons (2025-10-01..2025-10-31) [DISCARD: National out-migrants equals in-migrants by construction; duplicate of p48/p46.] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p50 National in-migrants (転入者数), all movers, October 2024 = **167,107** persons (2024-10-01..2024-10-31) [DISCARD: October 2024 in-migrants, duplicate of p46's prior-year value; not needed.] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p51 Year-on-year change in national inter-municipal movers, all movers, October 2025 = **1,549** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p52 Year-on-year percent change in national inter-municipal movers, all movers, Octo = **0.4** percent (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p53 National inter-municipal movers, Japanese movers only, October 2024 = **326,783** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p54 National inter-municipal movers, foreign movers only, October 2024 = **51,419** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p55 21 major cities total in-migrants (転入者数), all movers, October 2025 = **93,597** persons (2025-10-01..2025-10-31) [DISCARD: 21 major cities in-migrants; sub-geography not used in any route and not needed for a national total.] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
  - p56 21 major cities total out-migrants (転出者数), all movers, October 2025 = **93,543** persons (2025-10-01..2025-10-31) [DISCARD: 21 major cities out-migrants; sub-geography not used.] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"

### d5 [base_rates] Population-based mobility rate

Hypothesis: Internal migration events in a month equal population times a monthly mobility rate; August mobility rate can be taken from prior Augusts and applied to the 2026 population.

Queries issued by the searcher: Statistics Bureau 住民基本台帳人口移動報告 2025年8月 移動者数; Japan population 2026 total residents 人口推計 2026年; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; stat.go.jp idou rireki 2408 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 11/11
  - p57 Total internal migration events between municipalities (all movers, Japanese + f = **390,799** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p58 Year-on-year change in total inter-municipal movers, Japan, July 2026 = **7,618** persons (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p59 Year-on-year percent change in total inter-municipal movers, Japan, July 2026 = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p60 Total inter-prefectural movers (all movers), Japan, July 2026 = **181,604** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p61 Total intra-prefectural movers (all movers), Japan, July 2026 = **209,195** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p62 Japanese movers between municipalities, Japan, July 2026 = **335,854** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p63 Japanese movers between prefectures, Japan, July 2026 = **150,347** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p64 Japanese movers within prefectures, Japan, July 2026 = **185,507** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p65 Foreign movers between municipalities, Japan, July 2026 = **54,945** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p66 Foreign movers between prefectures, Japan, July 2026 = **31,257** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p67 Foreign movers within prefectures, Japan, July 2026 = **23,688** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://emb3.nhk.or.jp/nhkworld/en/news/20260730_01/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [physical_flow] Moving/relocation service activity

Hypothesis: August relocation activity (moving companies, utility transfers, address changes) tracks internal migration events; seasonal peaks in moving demand align with August migration counts.

Queries issued by the searcher: 引越し 需要 月別 季節性 8月; 住民基本台帳人口移動報告 月別 転入 転出 2025年; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 引越し 件数 月別 シェア 3月 4月 ピーク 何割

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p68 Annual internal migration between municipalities in Japan, 2025 (total moves) = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p27 (2025 annual total).] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p69 Annual internal migration between municipalities in Japan, 2024 (total moves) = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p1/p29 (2024 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p70 Annual internal migration between municipalities in Japan, 2023 (total moves) = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p2/p30 (2023 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p71 Annual internal migration between municipalities in Japan, 2022 (total moves) = **5,310,972** persons (moves) (2022-01-01..2022-12-31) [DISCARD: Duplicate of p3/p31 (2022 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p72 Annual internal migration between municipalities in Japan, 2021 (total moves) = **5,247,744** persons (moves) (2021-01-01..2021-12-31) [DISCARD: Duplicate of p4/p32 (2021 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p73 Annual internal migration between municipalities in Japan, 2020 (total moves) = **5,255,721** persons (moves) (2020-01-01..2020-12-31) [DISCARD: Duplicate of p5/p33 (2020 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p74 Annual internal migration between municipalities in Japan, 2019 (total moves) = **5,403,465** persons (moves) (2019-01-01..2019-12-31) [DISCARD: Duplicate of p6/p34 (2019 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p75 Annual internal migration between municipalities in Japan, 2018 (total moves) = **5,359,174** persons (moves) (2018-01-01..2018-12-31) [DISCARD: Duplicate of p7/p35 (2018 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p76 Annual internal migration between municipalities in Japan, 2017 (total moves) = **5,318,617** persons (moves) (2017-01-01..2017-12-31) [DISCARD: Duplicate of p8/p36 (2017 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p77 Annual internal migration between municipalities in Japan, 2016 (total moves) = **5,251,717** persons (moves) (2016-01-01..2016-12-31) [DISCARD: Duplicate of p9/p37 (2016 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p78 Annual internal migration between municipalities in Japan, 2015 (total moves) = **5,384,553** persons (moves) (2015-01-01..2015-12-31) [DISCARD: Duplicate of p10/p38 (2015 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p79 Year-on-year change rate of internal migration between municipalities, 2025 = **-0.3** percent (2025-01-01..2025-12-31) [DISCARD: Duplicate of p96/p41 (2025 annual y/y %).] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p80 Annual inter-prefectural migration in Japan, 2025 = **2,515,731** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p39 (2025 inter-prefectural).] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p81 Annual intra-prefectural migration in Japan, 2025 = **2,674,817** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p40 (2025 intra-prefectural).] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p82 Annual inflow from abroad to Japan, 2025 = **782,165** persons (2025-01-01..2025-12-31) [DISCARD: Inflow from abroad is an international move, explicitly excluded from the internal-migration target; unusable as a compo] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
- `https://www.starmoving.jp/blog/recommended-timetomove` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] Calendar and policy effects

Hypothesis: August 2026 move counts may deviate from trend due to calendar effects (weekday composition, Obon), housing market conditions, or policy changes affecting registration; these should be checked as modifiers.

Queries issued by the searcher: 住民基本台帳移動報告 2026年8月 都道府県間 転入超過; 総務省統計局 住民基本台帳人口移動報告 2026年 月次 移動者数; stat.go.jp 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳 制度変更 2026年 転入届 転出届 オンライン マイナンバー 改正

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kankeijinko.jp/2026/08/29/1292/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p83 Japan internal inter-municipal migration count (市区町村間移動者数), 2025 annual total = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p27 (2025 annual total).] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p84 Japan internal inter-municipal migration count (市区町村間移動者数), 2025 annual total (t = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p27 (2025 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p85 Japan internal inter-municipal migration count (市区町村間移動者数), 2024 annual total = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p1 (2024 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p86 Japan internal inter-municipal migration count (市区町村間移動者数), 2023 annual total = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p2 (2023 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p87 Japan internal inter-municipal migration count (市区町村間移動者数), 2022 annual total = **5,310,972** persons (moves) (2022-01-01..2022-12-31) [DISCARD: Duplicate of p3 (2022 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p88 Japan internal inter-municipal migration count (市区町村間移動者数), 2021 annual total = **5,247,744** persons (moves) (2021-01-01..2021-12-31) [DISCARD: Duplicate of p4 (2021 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p89 Japan internal inter-municipal migration count (市区町村間移動者数), 2020 annual total = **5,255,721** persons (moves) (2020-01-01..2020-12-31) [DISCARD: Duplicate of p5 (2020 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p90 Japan internal inter-municipal migration count (市区町村間移動者数), 2019 annual total = **5,403,465** persons (moves) (2019-01-01..2019-12-31) [DISCARD: Duplicate of p6 (2019 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p91 Japan internal inter-municipal migration count (市区町村間移動者数), 2018 annual total = **5,359,174** persons (moves) (2018-01-01..2018-12-31) [DISCARD: Duplicate of p7 (2018 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p92 Japan internal inter-municipal migration count (市区町村間移動者数), 2017 annual total = **5,318,617** persons (moves) (2017-01-01..2017-12-31) [DISCARD: Duplicate of p8 (2017 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p93 Japan internal inter-municipal migration count (市区町村間移動者数), 2016 annual total = **5,251,717** persons (moves) (2016-01-01..2016-12-31) [DISCARD: Duplicate of p9 (2016 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p94 Japan internal inter-municipal migration count (市区町村間移動者数), 2015 annual total = **5,384,553** persons (moves) (2015-01-01..2015-12-31) [DISCARD: Duplicate of p10 (2015 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p95 Japan inter-municipal migration year-on-year change (対前年増減数), 2025 = **-17,198** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p96 Japan inter-municipal migration year-on-year change rate (対前年増減率), 2025 = **-0.3** percent (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p97 Japan inter-prefectural migration count (都道府県間移動者数), 2025 annual total = **2,515,731** persons (moves) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p39 (2025 inter-prefectural).] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Statistics Bureau monthly report archive

Hypothesis: August values of 市区町村間移動者数 for 2021-2025 (and the August share of the annual total) would let a series_naive or yoy_scaling method run directly on the target month, replacing the July-anchored scaling route (m2) whose main uncertainty is the July-to-August seasonal step.

Queries issued by the searcher: 住民基本台帳人口移動報告 月報 8月 市区町村間移動者数 stat.go.jp; e-Stat 住民基本台帳人口移動報告 時系列データ 月次 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万; e-Stat 住民基本台帳人口移動報告 月，男女別市区町村間移動者数 全国 移動者 日本人移動者 外国人移動者 2020年～

- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20240927_no1695.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?page=1&iroha=29&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Seasonal shape of monthly moves

Hypothesis: A monthly seasonal index (August vs July ratio) from recent years would convert the observed July 2026 level (p57) into an August 2026 level with a defensible seasonal factor, tightening m2's assumption a1.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 月別 時系列 都道府県間移動者数 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 長期時系列表 市区町村間移動者数 月別 1954年〜; e-Stat 住民基本台帳人口移動報告 年報（実数）2020年～ 1 月，男女別移動者数，市区町村間移動者数 全国

- `https://www.e-stat.go.jp/stat-search/files?layout=datalist&cycle=0&toukei=00200523&tstat=000000070001&tclass1=000001051218` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p98 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **390,799** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p57 (July 2026 total).] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p99 Year-on-year change in total internal migration events between municipalities, a = **7,618** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p58 (July 2026 y/y change).] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p100 Year-on-year percent change in total internal migration events between municipal = **1.9** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p59 (July 2026 y/y %).] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p101 Japanese movers internal migration events between municipalities (日本人移動者の市区町村間移動 = **335,854** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p62 (July 2026 Japanese movers).] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p102 Year-on-year change in Japanese movers internal migration events between municip = **9,318** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p62's y/y change.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p103 Year-on-year percent change in Japanese movers internal migration events between = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p62's y/y %.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p104 Foreign movers internal migration events between municipalities (外国人移動者の市区町村間移動者 = **54,945** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p65 (July 2026 foreign movers).] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p105 Year-on-year change in foreign movers internal migration events between municipa = **1,700** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p65's y/y change.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p106 Year-on-year percent change in foreign movers internal migration events between  = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p65's y/y %.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p107 Total movers inter-prefectural migration events (都道府県間移動者数), July 2026 = **181,604** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p60 (July 2026 inter-prefectural).] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p108 Total movers intra-prefectural migration events (都道府県内移動者数), July 2026 = **209,195** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p61 (July 2026 intra-prefectural).] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p109 Japanese movers inter-prefectural migration events, July 2026 = **150,347** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p63 (July 2026 Japanese inter-prefectural).] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p110 Japanese movers intra-prefectural migration events, July 2026 = **185,507** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p64 (July 2026 Japanese intra-prefectural).] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p111 Foreign movers inter-prefectural migration events, July 2026 = **31,257** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p66 (July 2026 foreign inter-prefectural).] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p112 Foreign movers intra-prefectural migration events, July 2026 = **23,688** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p67 (July 2026 foreign intra-prefectural).] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"

### b3 [related_series] Foreign mover share trend

Hypothesis: Monthly foreign-mover counts for August in recent years would let the foreign component (growing ~3% y/y in July 2026, p65) be projected separately and summed with a Japanese-only August baseline, testing whether the combined total diverges from the July-anchored route.

Queries issued by the searcher: 住民基本台帳人口移動報告 外国人移動者 8月 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 2025年8月 外国人 移動者数; stat.go.jp 住民基本台帳人口移動報告 2023年8月結果 外国人移動者 市区町村間移動者数; 住民基本台帳人口移動報告 2024年8月 外国人移動者 市区町村間移動者数 4万2009人

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2308/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2408/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august migration japan', 'resident registration moves']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11'] Single Statistics Bureau annual series of inter-municipal movers (Japanese + foreign), 2014-2024, from one table; identical to p27-p38/p68-p78/p83-p94 (duplicate copies of the same underlying series).
- corroborating: ['p27', 'p28', 'p68', 'p83', 'p84'] 2025 annual total 5,190,548 from the 2026-02-03 release; same figure repeated across d4/d6/d7 copies. Extends the annual series one year and is the most recent full-year anchor.
- corroborating: ['p12', 'p13'] Annual inter-municipal migration rate ~4.1-4.2% of registered population, consistent with annual totals divided by ~123M population; supports a population x rate route but is annual, not August-specif
- corroborating: ['p14', 'p15', 'p16'] August 2026 provisional total population 122.68M, down 0.48% y/y; consistent with p17-p26 March 2026 final figures (population ~122.8M, Japanese declining, foreign rising). Provides the 2026 populatio
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26'] March 2026 final population breakdown; several values carry a spurious 1e3 multiplier in the table (e.g. p17, p19, p21, p22, p24, p25) but the quoted Japanese text confirms 122.811M total, 118.989M Ja
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56'] October 2025 monthly report: total 379,751, Japanese 321,850, foreign 57,901; inter-prefectural 168,057 + intra-prefectural 211,694 = total. Confirms monthly report structure and that foreign movers a
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67'] July 2026 monthly report: total 390,799 (down 1.9% y/y), Japanese 335,854 (down 2.7%), foreign 54,945 (up 3.2%). Most recent observed month and the key anchor for a y/y scaling route into August 2026;
- corroborating: ['p39', 'p40', 'p80', 'p81', 'p97'] 2025 inter-prefectural 2,515,731 + intra-prefectural 2,674,817 = 5,190,548 total; consistent decomposition of the annual total.
- corroborating: ['p41', 'p79', 'p95', 'p96'] Annual y/y change rates and change counts for the same series; 2025 -0.3% / -17,198 consistent with 5,207,746 -> 5,190,548.
- corroborating: ['p82'] 2025 inflow from abroad 782,165; context only — international moves are excluded from the target, so this is not a component of internal migration.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11'] Same annual series (市区町村間移動者数, all movers) from one Statistics Bureau table; p1-p11 are successive years of one measurement, not independent confirmations. p27/p29-p38 repeat the same series in a late
- corroborating: ['p27', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] Later-vintage (2026-02-03) copy of the annual series; adds 2025 = 5,190,548. Consistent with p1-p11 where they overlap; use one vintage per year, not both.
- corroborating: ['p12', 'p13'] Annual inter-municipal migration rate 4.17% (2024) and 4.20% (2023); same table, stable around 4.1-4.2%, consistent with annual totals divided by ~123M population.
- corroborating: ['p39', 'p40', 'p80', 'p81', 'p97'] Inter-prefectural (2,515,731) + intra-prefectural (2,674,817) = 5,190,548 = p27 for 2025; internal decomposition is consistent, not independent.
- corroborating: ['p57', 'p58', 'p59', 'p98', 'p99', 'p100'] Duplicate copies of the same July 2026 release (390,799; -7,618; -1.9%). One measurement, repeated ids.
- corroborating: ['p62', 'p65', 'p101', 'p104'] July 2026 Japanese (335,854) + foreign (54,945) = 390,799 = total; consistent split, same source.
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p51', 'p52', 'p53', 'p54'] October 2025/2024 monthly release: total 379,751 vs 378,202; Japanese 321,850 vs 326,783; foreign 57,901 vs 51,419. Internally consistent; shows foreign movers growing ~12.6% y/y while Japanese fall ~
- conflicting: ['p57', 'p42'] Not a true conflict: different months (July vs October). July 2026 (390,799) is higher than October 2025 (379,751), consistent with summer being a high-move season; used only as a seasonal anchor, not
- corroborating: ['p14', 'p15', 'p16', 'p18', 'p20', 'p26'] August 2026 provisional population 122.68M, -0.48% y/y; March 2026 final -0.49%; foreign population +7.2% y/y. Consistent demographic backdrop: shrinking Japanese base, growing foreign base, supportin
- corroborating: ['p95', 'p96', 'p41', 'p79'] 2025 annual change -17,198 / -0.3%; same figure repeated. Confirms near-flat annual trend, so August 2026 should be near recent August levels with small negative drift for Japanese and positive for fo

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August/July ratio of total inter-municipal movers | 1.05 | 0.95..1.18 | 0.7487..1.497 (widened) | ratio | m1 (m2) | August in Japan is a peak relocation month (Obon, end-of-summer job and school moves) and typically runs at or slightly above July. July 2026 (p57) is the observed anchor; this is a dimensionless seasonal step factor, not a level of the target. Range spans a mild decline to a strong August peak. | August seasonal pattern resembles recent pre-2026 years; no major registration-policy or calendar shock. | Evidence that August 2026 move counts fell below July 2026, or a documented shift in the seasonal profile. |
| a2 | August share of annual inter-municipal movers | 0.088 | 0.078..0.1 | 0.06245..0.1249 (widened) | share | m2 (m3) | August is a high-move month; with ~5.2M annual moves, a typical August of ~430-460k implies a share near 8.5-9%. Range covers a flat-month low to a strong summer peak. | Annual total near the recent 5.2M level and August retains its usual seasonal weight. | Evidence that August 2026 was unusually weak or strong relative to the annual total. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 414,096 | ['p57'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 38,136 | ['p27'] / ['a2'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **125,666** person, 80% interval [27,260, 579,310] person, basis method_spread (interval width set from the disagreement between the methods' estimates), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 125,666 person (80% model-based interval 27,260 to 579,310 person), covering internal migration events between municipalities within Japan (Japanese and foreign residents combined) for 2026-[n]-[n] to 2026-[n]-[n], as first reported in the Statistics Bureau's monthly Report on Internal Migration.

Two methods were combined with weights of 50% and 50%. Method [n] scales the observed July 2026 level (390,799 persons (moves)) by an August/July seasonal step of 1.05 (range 0.7487 to 1.497). Method [n] applies an August share of 0.088 (range 0.06245 to 0.1249) to the observed 2025 annual total (5,190,548 persons (moves)). Only the July and annual figures are observed; the seasonal step and share are analyst assumptions, and the annual total is transferred from 2025 to 2026.

The interval reflects disagreement between the two methods, not demonstrated accuracy. The biggest risk is the seasonal assumptions, especially the August/July step. Actual August 2026 data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August/July ratio of total inter-municipal movers: 1.05 ratio, range 0.7487 to 1.497 (range widened by code); used by m1. Overturned by: Evidence that August 2026 move counts fell below July 2026, or a documented shift in the seasonal profile.
- a2 August share of annual inter-municipal movers: 0.088 share, range 0.06245 to 0.1249 (range widened by code); used by m2. Overturned by: Evidence that August 2026 was unusually weak or strong relative to the annual total.

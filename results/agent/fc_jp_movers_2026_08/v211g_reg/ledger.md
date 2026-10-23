# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of persons who changed their municipality of residence within Japan (internal migration events, i.e., moves between municipalities, including moves between wards of designated cities and between municipalities within the same prefecture), as reported in the Statistics Bureau of Japan's monthl | unit person (moves between municipalities) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan (総務省統計局)

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau time series

Hypothesis: August internal-migration move counts follow a strong seasonal pattern (peak in spring around March–April, secondary peak in late summer/autumn); the August 2026 value should be close to August values in 2023–2025 adjusted for trend and population change. Role: provides the base level and seasonal shape.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 国内移動者数; Statistics Bureau Japan internal migration monthly report August 2025 total movers 住民基本台帳人口移動報告; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 統計メールニュース 2026年8月26日 住民基本台帳人口移動報告 2026年7月; 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万5918

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Annual/calendar-year totals

Hypothesis: Annual internal-migration move totals divided by 12 give a baseline monthly average; August's share of the annual total (seasonal index) can be applied to a projected 2026 annual total. Role: cross-check and smoothing of d1.

Queries issued by the searcher: 住民基本台帳人口移動報告 年次 国内移動者数 2024 2025; Japan internal migration annual total movers 2024 住民基本台帳人口移動報告 年間; 統計メールニュース 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2023年結果 市区町村間移動者数 526万

- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/7
  - p1 Annual total internal-migration moves between municipalities (all persons, Japan = **5,310,972** persons (moves between municipalities) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p2 Annual total internal-migration moves between municipalities (all persons, Japan = **5,263,249** persons (moves between municipalities) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p3 Annual total internal-migration moves between municipalities (all persons, Japan = **5,207,746** persons (moves between municipalities) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p4 Annual total internal-migration moves between municipalities (Japanese only, Jap = **4,603,155** persons (moves between municipalities) (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p5 Annual total internal-migration moves between municipalities (foreigners only, J = **604,591** persons (moves between municipalities) (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p6 Inter-prefecture moves (all persons, Japan), 2024 = **2,523,249** persons (moves between prefectures) (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p7 Intra-prefecture moves (all persons, Japan), 2024 = **2,684,497** persons (moves within prefecture between municipalities) (2024-01-01..2024-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2024np/jissu/pdf/all.pdf` -> **snapshot** (snapshot 20250516005632); points raw/verified 15/9
  - p8 Annual internal migration between municipalities (市区町村間移動者数), Japan, all nationa = **5,310,972** persons (moves between municipalities) (2022-01-01..2022-12-31) [DISCARD: Duplicate of p1 (2022 annual total, same value).] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p9 Annual internal migration between municipalities (市区町村間移動者数), Japan, all nationa = **5,263,249** persons (moves between municipalities) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p2 (2023 annual total).] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p10 Annual internal migration between municipalities, Japan, all nationalities, 2024 = **5,207,746** persons (moves between municipalities) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p3 (2024 annual total).] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p11 Year-on-year change in annual internal migration between municipalities, Japan,  = **-1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 - 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1"
  - p12 Annual internal migration between municipalities, Japan, Japanese only, 2023 = **4,696,572** persons (moves between municipalities) (2023-01-01..2023-12-31) [keep: ] quote: "総数 4,603,155 4,696,572 -93,417 -2.0 2,188,590 2,229,186 -40,596 -1.8 2,414,565 2,467,386 -52,821 -2.1"
  - p13 Annual internal migration between municipalities, Japan, foreigners only, 2023 = **566,677** persons (moves between municipalities) (2023-01-01..2023-12-31) [keep: ] quote: "総数 604,591 566,677 37,914 6.7 334,659 315,453 19,206 6.1 269,932 251,224 18,708 7.4"
  - p14 Municipality-to-municipality migration rate (市区町村間移動率) per registered population = **4.2** % (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動率 4.05 4.20 4.10 4.16 4.20 4.24 4.13 4.14 4.22 4.20 4.17"
  - p15 Annual internal migration between municipalities, Japan, all nationalities, 2021 = **5,247,744** persons (moves between municipalities) (2021-01-01..2021-12-31) [DISCARD: Duplicate of p22 (2021 annual total).] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p16 Annual internal migration between municipalities, Japan, all nationalities, 2020 = **5,255,721** persons (moves between municipalities) (2020-01-01..2020-12-31) [DISCARD: Duplicate of p23 (2020 annual total).] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (value_as_written not in quote as a whole number: 8; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 6)

### d3 [related_series] Population base and migration rate

Hypothesis: Internal-migration moves per 1,000 population (migration rate) is relatively stable; multiplying the August 2026 population (Japanese + foreign residents on Basic Resident Registration) by the August migration rate gives an estimate. Role: independent route using population stock and rate.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 移動者数 転入 転出; 住民基本台帳に基づく人口、人口動態及び世帯数 2026年1月1日 総人口; 住民基本台帳人口移動報告 時系列表 市区町村間移動者数 月別 2023 2024 2025; 住民基本台帳人口移動報告 2024年8月 市区町村間移動者数 35万5918人

- `https://www.soumu.go.jp/main_content/001083784.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p17 Japan total inter-municipal (city/ward/town/village) internal migrants, 2025 (an = **5,190,548** persons (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p18 Japan inter-municipal internal migrants, 2025 (table 1, persons) = **5,190,548** persons (moves between municipalities) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p17 (2025 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p19 Japan inter-municipal internal migrants, 2024 (table 1, persons) = **5,207,746** persons (moves between municipalities) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p3 (2024 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p20 Japan inter-municipal internal migrants, 2023 (table 1, persons) = **5,263,249** persons (moves between municipalities) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p2 (2023 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p21 Japan inter-municipal internal migrants, 2022 (table 1, persons) = **5,310,972** persons (moves between municipalities) (2022-01-01..2022-12-31) [DISCARD: Duplicate of p1 (2022 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p22 Japan inter-municipal internal migrants, 2021 (table 1, persons) = **5,247,744** persons (moves between municipalities) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p23 Japan inter-municipal internal migrants, 2020 (table 1, persons) = **5,255,721** persons (moves between municipalities) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p24 Japan inter-municipal internal migrants, 2019 (table 1, persons) = **5,403,465** persons (moves between municipalities) (2019-01-01..2019-12-31) [DISCARD: Duplicate of p82 (2019 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p25 Japan inter-municipal internal migrants, 2018 (table 1, persons) = **5,359,174** persons (moves between municipalities) (2018-01-01..2018-12-31) [DISCARD: Duplicate of p83 (2018 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p26 Japan inter-municipal internal migrants, 2017 (table 1, persons) = **5,318,617** persons (moves between municipalities) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p27 Japan inter-municipal internal migrants, 2016 (table 1, persons) = **5,251,717** persons (moves between municipalities) (2016-01-01..2016-12-31) [DISCARD: Duplicate of p85 (2016 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p28 Japan inter-municipal internal migrants, 2015 (table 1, persons) = **5,384,553** persons (moves between municipalities) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p29 Japan year-on-year change rate of inter-municipal internal migrants, 2025 (perce = **-0.3** percent (year-on-year change) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p30 Japan inter-prefectural internal migrants, 2025 (annual) = **2,515,731** persons (moves between prefectures) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p31 Japan intra-prefectural internal migrants, 2025 (table 1, persons) = **2,674,817** persons (moves between municipalities within same prefecture (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"

### d4 [related_series] Prefecture-level components

Hypothesis: Summing prefecture-level internal in-migration (or out-migration) counts for August 2026, if any preliminary prefecture data are available, gives the national total. Role: bottom-up cross-check.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 都道府県別 移動者数; 都道府県別 住民基本台帳 移動者数 2025年8月 転入 転出; 住民基本台帳人口移動報告 2026年 月結果 市区町村間移動者数 統計メールニュース; 統計局 住民基本台帳人口移動報告 2026年6月結果 都道府県別 転入者数

- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tokyo.vivinavi.com/mc/desc/_wid_551f4899ba914fb4b0d0f60089453e9e1cf3082626/-/-/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/10
  - p32 National total internal migration between municipalities (all persons, Japanese  = **5,190,548** persons (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p33 National total inter-prefectural migration (all persons), calendar year 2025 = **2,515,731** persons (moves between prefectures) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p30 (2025 inter-prefectural total).] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p34 National total internal migration between municipalities (all persons), calendar = **5,207,746** persons (moves between municipalities) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p3 (2024 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p35 National total inter-prefectural in-migrants (all persons) from prefecture table = **2,515,731** persons (in-migrants from other prefectures) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p30 (inter-prefectural in-migrants = out-migrants nationally).] quote: "全 国 2,515,731 2,515,731 782,165 409,592 82,854 118,193 337,234 331,686"
  - p36 National total inter-prefectural out-migrants (all persons) from prefecture tabl = **2,515,731** persons (out-migrants to other prefectures) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p30 (inter-prefectural out-migrants = in-migrants nationally).] quote: "全 国 2,515,731 2,515,731 782,165 409,592 82,854 118,193 337,234 331,686"
  - p37 National total internal migration between municipalities (Japanese only), calend = **4,528,254** persons (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p38 National total internal migration between municipalities (foreigners only), cale = **662,294** persons (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p39 National total inter-prefectural migration (foreigners only), calendar year 2025 = **367,402** persons (moves between prefectures) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は36万7402人(対前年比9.8%増)。2014年以降、過去最多"
  - p40 National total inter-prefectural migration (Japanese only), calendar year 2025 = **2,148,329** persons (moves between prefectures) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は214万8329人(対前年比1.8%減)"
  - p41 National total intra-prefectural migration (Japanese only), calendar year 2025 = **2,379,925** persons (moves between municipalities within same prefecture (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数は237万9925人で、前年に比べ3万4640人(1.4%)の減少となっている。"
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 5)

### d5 [base_rates] Foreign vs Japanese composition

Hypothesis: Foreign residents have higher mobility rates than Japanese; the foreign share of internal movers has been rising. Estimating the foreign and Japanese components separately (each = population × group-specific August rate) improves accuracy. Role: decomposition of d3.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 外国人 移動者数; 外国人 住民基本台帳 移動者数 2025年8月 国籍別; 2025年8月 市区町村間移動者数 日本人移動者 外国人移動者 4万6532人; 令和8年 住民基本台帳 外国人住民数 2026年 外国人人口 総務省 推計

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/9
  - p42 Foreign internal movers (municipality-to-municipality), Japan, calendar year 202 = **604,591** persons (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p43 Japanese internal movers (municipality-to-municipality), Japan, calendar year 20 = **4,603,155** persons (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p44 All internal movers (Japanese + foreign, municipality-to-municipality), Japan, c = **5,207,746** persons (2024-01-01..2024-12-31) [DISCARD: Duplicate of p3 (2024 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p45 All internal movers (Japanese + foreign, municipality-to-municipality), Japan, c = **5,263,249** persons (2023-01-01..2023-12-31) [DISCARD: Duplicate of p2 (2023 annual total).] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p46 Foreign internal movers (municipality-to-municipality), Japan, calendar year 202 = **566,677** persons (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p47 Japanese internal movers (municipality-to-municipality), Japan, calendar year 20 = **4,696,572** persons (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
  - p48 Foreign internal movers (municipality-to-municipality), Japan, calendar year 202 = **535,765** persons (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
  - p49 Japanese internal movers (municipality-to-municipality), Japan, calendar year 20 = **4,775,207** persons (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 4,775,207 2,525,114 2,250,093 -0.9 -1.2 -0.6 2,519,845 1,279,793"
  - p50 Foreign internal movers (municipality-to-municipality), Japan, calendar year 202 = **429,023** persons (2021-01-01..2021-12-31) [keep: ] quote: "3 2021 429,023 243,117 185,906 3.4 3.1 3.8 195,228 106,282"
- dropped by code checks: 6 (value_as_written not in quote as a whole number: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d6 [shocks] Calendar and policy effects

Hypothesis: August 2026 move counts may be affected by the timing of the Obon holiday, the number of business days, and any policy changes (e.g., foreign resident registration rules, My Number integration). Role: adjust the seasonal baseline for known calendar/policy shifts.

Queries issued by the searcher: 2026年8月 カレンダー 平日 数 祝日; 住民基本台帳 制度変更 2026; 住民基本台帳人口移動報告 2026年8月 転入 転出 総務省統計局; 2025年8月 住民基本台帳人口移動報告 日本人 移動者数 前年同月

- `https://www.benri.jp/calendar/month/?year=2026&month=8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bestcalendar.jp/2026/8` -> **snapshot** (snapshot 20260828231809); points raw/verified 12/7
  - p51 Obon date in August 2026 calendar (single day marked お盆) = **15** day of month (2026-08-15..2026-08-15) [keep: ] quote: "2026年8月15日(土) お盆"
  - p52 Mountain Day (山の日) date in August 2026 = **11** day of month (2026-08-11..2026-08-11) [keep: ] quote: "2026年8月11日(火) 山の日"
  - p53 New moon date in August 2026 = **13** day of month (2026-08-13..2026-08-13) [DISCARD: Astronomical calendar fact with no quantitative link to mover counts.] quote: "新月は13日、満月は28日です。"
  - p54 Full moon date in August 2026 = **28** day of month (2026-08-28..2026-08-28) [DISCARD: Astronomical calendar fact with no quantitative link to mover counts.] quote: "新月は13日、満月は28日です。"
  - p55 First day of August 2026 shown on calendar grid = **1** day of month (2026-08-01..2026-08-01) [DISCARD: Calendar grid fact, irrelevant to mover counts.] quote: "\| \| \| \| \| \| \| 1 赤口 神吉日 大明日 \|"
  - p56 New moon time in August 2026 (JST) = **2.36** as written "02:36", value check pending clock time (hours:minutes) (2026-08-13..2026-08-13) [DISCARD: Astronomical calendar fact, irrelevant.] quote: "13 先勝 新月 (02:36) 月齢:0.4"
  - p57 Full moon time in August 2026 (JST) = **13.18** as written "13:18", value check pending clock time (hours:minutes) (2026-08-28..2026-08-28) [DISCARD: Astronomical calendar fact, irrelevant.] quote: "28 仏滅 満月 (13:18) 月齢:15.4"
- `https://www.cao.go.jp/bunken-suishin/teianbosyu/doc/r08/ko_08_moj.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p58 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **379,751** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p59 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **378,202** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p60 Year-on-year change in total internal migration events between municipalities, a = **1,549** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p61 Japanese movers between municipalities (市区町村間移動者数, 日本人移動者), Japan, October 2025 = **321,850** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p62 Japanese movers between municipalities, Japan, October 2024 = **326,783** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p63 Foreign movers between municipalities (市区町村間移動者数, 外国人移動者), Japan, October 2025 = **57,901** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p64 Foreign movers between municipalities, Japan, October 2024 = **51,419** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p65 Inter-prefectural movers (都道府県間移動者数), all movers, Japan, October 2025 = **168,057** persons (moves between prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p66 Intra-prefectural movers (都道府県内移動者数), all movers, Japan, October 2025 = **211,694** persons (moves within prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p67 Inter-prefectural movers, all movers, Japan, October 2024 = **167,107** persons (moves between prefectures) (2024-10-01..2024-10-31) [keep: ] quote: "都道府県間移動者数 168,057 167,107 950 0.6 137,348 140,545 -3,197 -2.3 30,709 26,562 4,147 15.6"
  - p68 Intra-prefectural movers, all movers, Japan, October 2024 = **211,095** persons (moves within prefectures) (2024-10-01..2024-10-31) [keep: ] quote: "都道府県内移動者数 211,694 211,095 599 0.3 184,502 186,238 -1,736 -0.9 27,192 24,857 2,335 9.4"
  - p69 Japanese inter-prefectural movers, Japan, October 2025 = **137,348** persons (moves between prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 13万7348人。前年同月に比べ減少 ▲ 3197人( ▲ 2.3%)"
  - p70 Japanese intra-prefectural movers, Japan, October 2025 = **184,502** persons (moves within prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 18万4502人。前年同月に比べ減少 ▲ 1736人( ▲ 0.9%)"
  - p71 Foreign inter-prefectural movers, Japan, October 2025 = **30,709** as written "3万 709", value check pending persons (moves between prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 3万 709人。前年同月に比べ増加 4147人( 15.6%)"
  - p72 Foreign intra-prefectural movers, Japan, October 2025 = **27,192** persons (moves within prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 2万7192人。前年同月に比べ増加 2335人( 9.4%)"
- dropped by code checks: 5 (period_end 2026-08-31 after as_of: 5)

### b1 [own_history] seasonal index

Hypothesis: The August share of the annual municipality-to-municipality mover total is needed to convert the annual level (p17/p32) into an August 2026 figure. Monthly August totals for 2023-2025 would give the seasonal index and let a series_naive or ratio method replace the October-based scaling.

Queries issued by the searcher: stat.go.jp 住民基本台帳人口移動報告 月報 8月 市区町村間移動者数; e-Stat 人口移動 月次 2025年8月 市区町村間移動者数; 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万5918人; 住民基本台帳人口移動報告 2023年8月結果 市区町村間移動者数 37万9493

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20240927_no1695.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2024np/jissu/pdf/all.pdf` -> **snapshot** (snapshot 20250516005632); points raw/verified 15/15
  - p73 Annual municipality-to-municipality movers, all persons (Japan), 2024 = **5,207,746** persons (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p74 Annual municipality-to-municipality movers, all persons (Japan), 2023 = **5,263,249** persons (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p75 Annual municipality-to-municipality movers, all persons (Japan), 2022 = **5,310,972** persons (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p76 Annual municipality-to-municipality movers, all persons (Japan), 2021 = **5,247,744** persons (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p77 Annual municipality-to-municipality movers, all persons (Japan), 2020 = **5,255,721** persons (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p78 Annual municipality-to-municipality movers, Japanese only (Japan), 2024 = **4,603,155** persons (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,603,155 4,696,572 -93,417 -2.0 2,188,590 2,229,186 -40,596 -1.8 2,414,565 2,467,386 -52,821 -2.1"
  - p79 Annual municipality-to-municipality movers, Japanese only (Japan), 2023 = **4,696,572** persons (2023-01-01..2023-12-31) [keep: ] quote: "総数 4,603,155 4,696,572 -93,417 -2.0 2,188,590 2,229,186 -40,596 -1.8 2,414,565 2,467,386 -52,821 -2.1"
  - p80 Annual municipality-to-municipality movers, foreigners only (Japan), 2024 = **604,591** persons (2024-01-01..2024-12-31) [keep: ] quote: "総数 604,591 566,677 37,914 6.7 334,659 315,453 19,206 6.1 269,932 251,224 18,708 7.4"
  - p81 Annual municipality-to-municipality movers, foreigners only (Japan), 2023 = **566,677** persons (2023-01-01..2023-12-31) [keep: ] quote: "総数 604,591 566,677 37,914 6.7 334,659 315,453 19,206 6.1 269,932 251,224 18,708 7.4"
  - p82 Annual municipality-to-municipality movers, all persons (Japan), 2019 = **5,403,465** persons (2019-01-01..2019-12-31) [keep: ] quote: "令和 元 年 2019 5,403,465 2,882,778 2,520,687 0.8 0.9 0.8 2,835,379 1,455,862"
  - p83 Annual municipality-to-municipality movers, all persons (Japan), 2018 = **5,359,174** persons (2018-01-01..2018-12-31) [keep: ] quote: "30 2018 5,359,174 2,858,159 2,501,015 0.8 0.7 0.8 2,823,573 1,449,586"
  - p84 Annual municipality-to-municipality movers, all persons (Japan), 2017 = **5,318,617** persons (2017-01-01..2017-12-31) [keep: ] quote: "29 2017 5,318,617 2,837,193 2,481,424 1.3 1.2 1.3 2,813,553 1,444,220"
  - p85 Annual municipality-to-municipality movers, all persons (Japan), 2016 = **5,251,717** persons (2016-01-01..2016-12-31) [keep: ] quote: "28 2016 5,251,717 2,803,048 2,448,669 -2.5 -2.5 -2.4 2,791,371 1,431,940"
  - p86 Annual municipality-to-municipality movers, all persons (Japan), 2015 = **5,384,553** persons (2015-01-01..2015-12-31) [keep: ] quote: "27 2015 5,384,553 2,876,343 2,508,210 3.4 3.8 2.9 2,881,773 1,478,954"
  - p87 Annual municipality-to-municipality movers, all persons (Japan), 2014 = **5,207,599** persons (2014-01-01..2014-12-31) [keep: ] quote: "26 2014 5,207,599 2,771,245 2,436,354 ... ... ... 2,802,376 1,433,251"
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0

### b2 [related_series] monthly trend

Hypothesis: A recent monthly mover total (e.g., July 2026 or June 2026) would anchor the 2026 level and year-on-year change, reducing reliance on the October 2025 monthly point (p58) and the annual trend. It would let a yoy_scaling method use a same-year signal.

Queries issued by the searcher: stat.go.jp 人口移動報告 2026年7月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2026年6月 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 39万799人; "2026年7月" 人口移動報告 市区町村間移動者数 39万799人 前年同月

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p88 Total inter-municipal movers (市区町村間移動者数), all persons, Japan, October 2025 = **379,751** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p89 Year-on-year change in total inter-municipal movers, all persons, Japan, October = **1,549** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p90 Year-on-year rate of change in total inter-municipal movers, all persons, Japan, = **0.4** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p91 Total inter-municipal movers, all persons, Japan, October 2024 (prior-year compa = **378,202** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p92 Japanese inter-municipal movers (日本人移動者), Japan, October 2025 = **321,850** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p93 Year-on-year change in Japanese inter-municipal movers, Japan, October 2025 = **4,933** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p94 Year-on-year rate of change in Japanese inter-municipal movers, Japan, October 2 = **1.5** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p95 Japanese inter-municipal movers, Japan, October 2024 (prior-year comparison) = **326,783** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p96 Foreign inter-municipal movers (外国人移動者), Japan, October 2025 = **57,901** persons (moves between municipalities) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p97 Year-on-year change in foreign inter-municipal movers, Japan, October 2025 = **6,482** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p98 Year-on-year rate of change in foreign inter-municipal movers, Japan, October 20 = **12.6** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p99 Foreign inter-municipal movers, Japan, October 2024 (prior-year comparison) = **51,419** persons (moves between municipalities) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p100 Inter-prefectural movers (都道府県間移動者数), all persons, Japan, October 2025 = **168,057** persons (moves between prefectures) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p101 Intra-prefectural movers (都道府県内移動者数), all persons, Japan, October 2025 = **211,694** persons (moves within prefecture) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p102 Year-on-year rate of change in intra-prefectural movers, all persons, Japan, Oct = **0.3** % (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 13/13
  - p103 Total movers (all persons), inter-municipal moves, Japan, July 2026 = **390,799** persons (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p104 Year-on-year change in total movers, inter-municipal moves, Japan, July 2026 = **7,618** persons (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p105 Year-on-year percent change in total movers, inter-municipal moves, Japan, July  = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p106 Total movers (all persons), inter-prefectural moves, Japan, July 2026 = **181,604** persons (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p107 Total movers (all persons), intra-prefectural moves, Japan, July 2026 = **209,195** persons (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p108 Japanese movers, inter-municipal moves, Japan, July 2026 = **335,854** persons (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p109 Year-on-year change in Japanese movers, inter-municipal moves, Japan, July 2026 = **9,318** persons (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p110 Japanese movers, inter-prefectural moves, Japan, July 2026 = **150,347** persons (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p111 Japanese movers, intra-prefectural moves, Japan, July 2026 = **185,507** persons (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p112 Foreign movers, inter-municipal moves, Japan, July 2026 = **54,945** persons (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p113 Year-on-year change in foreign movers, inter-municipal moves, Japan, July 2026 = **1,700** persons (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p114 Foreign movers, inter-prefectural moves, Japan, July 2026 = **31,257** persons (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p115 Foreign movers, intra-prefectural moves, Japan, July 2026 = **23,688** persons (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?page=1&iroha=29&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] foreign share

Hypothesis: The foreign share of monthly movers is rising; a 2026 monthly foreign mover count or foreign registered population would refine the Japanese/foreign decomposition (d5) and the August foreign share, which is the largest source of uncertainty in the decomposition route.

Queries issued by the searcher: stat.go.jp 住民基本台帳 外国人 人口 2026; 出入国在留管理庁 在留外国人数 2026; 住民基本台帳人口移動報告 2026年 外国人 転入者数 総務省統計局; e-Stat 住民基本台帳人口移動報告 2026年6月 外国人 移動者数

- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040479057&iroha=26` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/new.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 14/14
  - p116 Total population of Japan, August 1 2026 (provisional estimate) = **122,680,000** persons (2026-08-01..2026-08-01) [keep: ] quote: "【2026年(令和8年)8月1日現在(概算値)】 <総人口> 1億2268万人で、前年同月に比べ減少"
  - p117 Year-on-year change in total population, August 2026 (provisional estimate) = **590,000** persons (2026-08-01..2026-08-01) [keep: ] quote: "<総人口> 1億2268万人で、前年同月に比べ減少 ▲59万人 (▲0.48%)"
  - p118 Year-on-year percentage change in total population, August 2026 (provisional est = **0.48** % (2026-08-01..2026-08-01) [keep: ] quote: "▲59万人 (▲0.48%)"
  - p119 Total population of Japan, March 1 2026 (final values based on 2020 Census) = **122,811,000,000** as written "1億2281万1千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "【2026年(令和8年)3月1日現在(令和2年国勢調査を基準とする確定値)】 <総人口> 1億2281万1千人で、前年同月に比べ減少"
  - p120 Year-on-year change in total population, March 2026 (final values) = **610,000** persons (2026-03-01..2026-03-01) [keep: ] quote: "<総人口> 1億2281万1千人で、前年同月に比べ減少 ▲61万人 (▲0.49%)"
  - p121 Population aged under 15, March 2026 (final values) = **13,319,000,000** as written "1331万9千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "・15歳未満人口は 1331万9千人で、前年同月に比べ減少 ▲36万人 (▲2.63%)"
  - p122 Population aged 15-64, March 2026 (final values) = **73,290,000** persons (2026-03-01..2026-03-01) [keep: ] quote: "・15~64歳人口は 7329万人で、 前年同月に比べ減少 ▲26万5千人 (▲0.36%)"
  - p123 Population aged 65 and over, March 2026 (final values) = **36,202,000,000** as written "3620万2千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "・65歳以上人口は 3620万2千人で、前年同月に比べ増加 1万5千人 ( 0.04%)"
  - p124 Population aged 75 and over, March 2026 (final values) = **21,488,000,000** as written "2148万8千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "うち75歳以上人口は 2148万8千人で、前年同月に比べ増加 47万9千人 ( 2.28%)"
  - p125 Japanese population, March 2026 (final values) = **118,989,000,000** as written "1億1898万9千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "<日本人人口> 1億1898万9千人で、前年同月に比べ減少 ▲86万6千人 (▲0.72%)"
  - p126 Year-on-year change in Japanese population, March 2026 (final values) = **-866,000,000** as written "▲86万6千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "<日本人人口> 1億1898万9千人で、前年同月に比べ減少 ▲86万6千人 (▲0.72%)"
  - p127 Foreign population, March 2026 (final values) = **3,821,000,000** as written "382万1千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "<外国人人口> 382万1千人で、前年同月に比べ増加 25万7千人 ( 7.20%)"
  - p128 Year-on-year change in foreign population, March 2026 (final values) = **257,000,000** as written "25万7千人", value check pending persons (2026-03-01..2026-03-01) [keep: ] quote: "<外国人人口> 382万1千人で、前年同月に比べ増加 25万7千人 ( 7.20%)"
  - p129 Year-on-year percentage change in foreign population, March 2026 (final values) = **7.2** % (2026-03-01..2026-03-01) [keep: ] quote: "25万7千人 ( 7.20%)"
- `https://www.stat.go.jp/info/mail/pdf/20260619_no1872.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august 2026 migration', 'jumin kihon daicho']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p8', 'p9', 'p10', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p32', 'p34', 'p44', 'p45'] All are the same annual municipality-to-municipality mover series (市区町村間移動者数) from the Statistics Bureau; p1/p2/p3, p8/p9/p10, p17-p28, p32, p34, p44, p45 are duplicate vintages of overlapping years a
- corroborating: ['p4', 'p12', 'p37', 'p43', 'p47', 'p49'] Japanese-only annual municipality-to-municipality movers; consistent across vintages (2022 4.78M, 2023 4.70M, 2024 4.60M, 2025 4.53M), showing a steady decline.
- corroborating: ['p5', 'p13', 'p38', 'p42', 'p46', 'p48', 'p50'] Foreign-only annual municipality-to-municipality movers; consistent rising series (2021 0.43M, 2022 0.54M, 2023 0.57M, 2024 0.60M, 2025 0.66M). Confirms rising foreign share of movers.
- corroborating: ['p4', 'p5', 'p44'] Japanese + foreign components sum to the all-persons total for 2024 (4,603,155 + 604,591 = 5,207,746), confirming the decomposition is exhaustive and non-overlapping.
- corroborating: ['p6', 'p7', 'p30', 'p31', 'p33', 'p35', 'p36'] Inter-prefecture and intra-prefecture components sum to the municipality total; p35 and p36 (in- and out-migrants) are equal by construction, confirming internal consistency of the prefecture table.
- corroborating: ['p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72'] October 2025 monthly report gives the only monthly-level data: total 379,751 (Japanese 321,850 + foreign 57,901), inter-prefecture 168,057 + intra-prefecture 211,694. Establishes the monthly magnitude
- corroborating: ['p14'] Annual municipality-to-municipality migration rate ~4.1-4.2% per registered population, consistent with annual totals divided by population (~124M).
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57'] Calendar facts for August 2026 (Obon Aug 15, Mountain Day Aug 11, moon phases). These are contextual only; they do not by themselves quantify a migration effect.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p17', 'p22', 'p23', 'p26', 'p28', 'p32', 'p73', 'p74', 'p75', 'p76', 'p77', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87'] All are the same annual all-person municipality-to-municipality mover series from the Statistics Bureau; p1/p2/p3/p17/p22/p23/p26/p28/p32 and p73-p87 are duplicate vintages of the same table. They agr
- corroborating: ['p4', 'p5', 'p12', 'p13', 'p37', 'p38', 'p42', 'p43', 'p46', 'p47', 'p48', 'p49', 'p50', 'p78', 'p79', 'p80', 'p81'] Japanese-only and foreign-only annual mover totals; they sum to the all-person totals (e.g. 2024: 4,603,155 + 604,591 = 5,207,746; 2025: 4,528,254 + 662,294 = 5,190,548). Confirms the decomposition ro
- corroborating: ['p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102'] October 2025 monthly report: total 379,751 = Japanese 321,850 + foreign 57,901; inter-prefectural 168,057 + intra-prefectural 211,694 = 379,751. Internally consistent; p58/p88 and p59/p91 are duplicat
- corroborating: ['p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115'] July 2026 monthly report: total 390,799 = Japanese 335,854 + foreign 54,945; inter-prefectural 181,604 + intra-prefectural 209,195 = 390,799. This is the most recent same-year signal: total movers dow
- corroborating: ['p116', 'p117', 'p118', 'p119', 'p120', 'p125', 'p126', 'p127', 'p128', 'p129'] Population estimates: total ~122.68M (Aug 2026 provisional), Japanese ~118.99M and foreign ~3.82M (Mar 2026 final). Note p119, p121, p123, p124, p125, p127, p128 carry a spurious 1e9 multiplier in the
- corroborating: ['p14', 'p29', 'p11'] Annual migration rate ~4.1-4.2% and yoy changes (-1.1% 2024, -0.3% 2025) are consistent with the annual totals; p14 is a rate, not a count, so it can only enter a rate-based route.
- corroborating: ['p51', 'p52'] Calendar facts for August 2026 (Obon 15 Aug, Mountain Day 11 Aug). They are contextual only; no quantitative bridge to mover counts is available, so they cannot enter a formula.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August-to-October monthly mover ratio | 1 | 0.85..1.2 | 0.7141..1.428 (widened) | ratio | m1 (m1) | August and October are both secondary-peak months in the Japanese mover calendar; without monthly August history the ratio is centred at 1 with a wide band reflecting seasonal spread. | Used to transfer the observed October 2025 monthly level to August 2026. | Monthly August totals showing August systematically far above or below October. |
| a2 | 2026-to-2025 annual trend factor for movers | 0.99 | 0.96..1.02 | 0.8851..1.106 (widened) | ratio | m1 (m1), m2 (m2) | Annual totals fell 0.3% in 2025 and July 2026 total movers were down 1.9% yoy (p103/p105); a modest further decline is the central case, with the range spanning flat to a slightly steeper fall. | Applied to a 2025-based level to project 2026. | A 2026 monthly report showing total movers up year-on-year. |
| a3 | August share of annual mover total | 0.085 | 0.075..0.095 | 0.05969..0.1194 (widened) | share | m2 (m2) | August is a secondary-peak month; a 1/12 uniform share is 0.083, and the seasonal peak in late summer/autumn justifies a value slightly above uniform with a band covering the plausible seasonal range. | Used to convert an annual total into an August monthly figure. | Monthly August totals implying a share outside 7.5-9.5% of the annual total. |
| a4 | August-to-July monthly mover ratio | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m3 (m3) | July and August are adjacent summer months with similar mover volumes; the ratio is centred at 1 with a band reflecting month-to-month variation. | Used to carry the observed July 2026 level forward to August 2026. | Monthly data showing August consistently far from July. |
| a5 | Japanese mover August-to-July ratio | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m4 (m4) | Same seasonal reasoning as a4 applied to the Japanese-only component. | Used to carry July 2026 Japanese movers to August 2026. | Japanese monthly data showing a strong August-July divergence. |
| a6 | Foreign mover August-to-July ratio | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | m4 (m4) | Same seasonal reasoning as a4 applied to the foreign-only component. | Used to carry July 2026 foreign movers to August 2026. | Foreign monthly data showing a strong August-July divergence. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 379,342 | ['p58'] / ['a1', 'a2'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 434,128 | ['p17'] / ['a2', 'a3'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 384,086 | ['p103'] / ['a4'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 388,658 | ['p108', 'p112'] / ['a5', 'a6'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: sum over channel of Japanese, foreign

Result: central **395,969** person, 80% interval [262,502, 597,296] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for the number of persons who changed municipality of residence within Japan (inter-municipal moves, Japanese and foreign residents combined) in August 2026 is 395,969 person (80% model-based interval 262,502 to 597,296 person). This is a forward estimate: the official August 2026 report is not yet published at the cutoff.

Evidence: the only observed monthly level is 379,751 persons (moves between municipalities) (October 2025); the annual total is 5,190,548 persons (moves between municipalities); and the July 2026 anchors are 390,799 persons, split into 335,854 persons and 54,945 persons. Four methods were combined with equal weights (25%, 25%, 25%, 25%); no backtest errors were available, so weighting reflects the code's design, not demonstrated accuracy. All seasonal ratios and trend factors (1 through 1) are assumptions, not observations.

Main risk: the August-to-July and August-to-October seasonal ratios are unobserved, so a mis-set seasonal factor could shift the result substantially. The most useful missing evidence would be historical monthly August mover counts to calibrate those ratios.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August-to-October monthly mover ratio: 1 ratio, range 0.7141 to 1.428 (range widened by code); used by m1. Overturned by: Monthly August totals showing August systematically far above or below October.
- a2 2026-to-2025 annual trend factor for movers: 0.99 ratio, range 0.8851 to 1.106 (range widened by code); used by m1, m2. Overturned by: A 2026 monthly report showing total movers up year-on-year.
- a3 August share of annual mover total: 0.085 share, range 0.05969 to 0.1194 (range widened by code); used by m2. Overturned by: Monthly August totals implying a share outside [n]-[n] of the annual total.
- a4 August-to-July monthly mover ratio: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m3. Overturned by: Monthly data showing August consistently far from July.
- a5 Japanese mover August-to-July ratio: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m4. Overturned by: Japanese monthly data showing a strong August-July divergence.
- a6 Foreign mover August-to-July ratio: 1 ratio, range 0.6991 to 1.398 (range widened by code); used by m4. Overturned by: Foreign monthly data showing a strong August-July divergence.

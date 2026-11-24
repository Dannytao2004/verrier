# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of internal migration events (moves between municipalities) within Japan recorded in the Basic Resident Registration system and first published in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration, for moves occurring i | unit persons (moves between municipalities) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan (Ministry of Internal Affairs and Communications)

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau time series

Hypothesis: August internal migration in Japan follows a stable seasonal pattern (August is typically a high-migration month due to summer job/relocation season and student moves). Prior-year August totals and the 2026 monthly year-to-date series (Jan-Jul 2026) anchor the level and trend; August 2026 ≈ August 2025 × (2026 YTD growth factor) × seasonal factor.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 転入者数 転出者数; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 統計メールニュース 2026 住民基本台帳人口移動報告 2026年7月 市区町村間移動者数 前年同月; 住民基本台帳人口移動報告 2025年8月 転入者数 転出者数; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 統計メールニュース 2026 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月 転入者数 転出者数; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 前年同月; 統計メールニュース 2026年 住民基本台帳人口移動報告 市区町村間移動者数 2026年6月結果

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/12
  - p1 Annual total internal migration between municipalities (Japanese + foreign), Jap = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p2 Annual total internal migration between municipalities (Japanese + foreign), Jap = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p3 Annual total internal migration between municipalities (Japanese + foreign), Jap = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p4 Year-on-year change in annual internal migration between municipalities (Japanes = **-17,198** person (2025-01-01..2025-12-31) [DISCARD: Redundant restatement of the change already implied by p1 and p2.] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p5 Year-on-year percent change in annual internal migration between municipalities  = **-0.3** % (2025-01-01..2025-12-31) [DISCARD: Redundant restatement of the percent change already implied by p1 and p2.] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p6 Annual inter-prefectural migration (Japanese + foreign), Japan, calendar year 20 = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p7 Annual internal migration between municipalities, Japanese movers only, Japan, c = **4,528,254** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p8 Annual internal migration between municipalities, Japanese movers only, Japan, c = **4,603,155** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p9 Annual internal migration between municipalities, foreign movers only, Japan, ca = **662,294** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p10 Annual internal migration between municipalities, foreign movers only, Japan, ca = **604,591** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p11 Annual internal migration between municipalities, foreign movers only, Japan, ca = **566,677** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p12 Annual internal migration between municipalities, Japanese movers only, Japan, c = **4,696,572** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 14/14
  - p13 Total internal migration between municipalities (市区町村間移動者数), all movers, Japan,  = **379,751** person (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p14 Total internal migration between municipalities (市区町村間移動者数), all movers, Japan,  = **378,202** person (2024-10-01..2024-10-31) [DISCARD: October 2024 total duplicated by p52/p66; adds no new information.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4"
  - p15 Inter-prefectural movers (都道府県間移動者数), all movers, Japan, October 2025 = **168,057** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p16 Intra-prefectural movers (都道府県内移動者数), all movers, Japan, October 2025 = **211,694** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p17 Japanese movers between municipalities (市区町村間移動者数, 日本人移動者), Japan, October 2025 = **321,850** person (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p18 Japanese movers between municipalities (市区町村間移動者数, 日本人移動者), Japan, October 2024 = **326,783** person (2024-10-01..2024-10-31) [DISCARD: October 2024 Japanese movers duplicated by p54/p67.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5"
  - p19 Foreign movers between municipalities (市区町村間移動者数, 外国人移動者), Japan, October 2025 = **57,901** person (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p20 Foreign movers between municipalities (市区町村間移動者数, 外国人移動者), Japan, October 2024 = **51,419** person (2024-10-01..2024-10-31) [DISCARD: October 2024 foreign movers duplicated by p56/p68.] quote: "321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p21 Year-on-year change in total municipal-to-municipal movers, Japan, October 2025  = **1,549** person (2025-10-01..2025-10-31) [DISCARD: Redundant change value already implied by p13 and p14.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4"
  - p22 Year-on-year percent change in total municipal-to-municipal movers, Japan, Octob = **0.4** % (2025-10-01..2025-10-31) [DISCARD: Redundant percent change already implied by p13 and p14.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4"
  - p23 Year-on-year percent change in foreign municipal-to-municipal movers, Japan, Oct = **12.6** % (2025-10-01..2025-10-31) [DISCARD: Redundant percent change already implied by p19 and p20.] quote: "57,901 51,419 6,482 12.6"
  - p24 Year-on-year percent change in Japanese municipal-to-municipal movers, Japan, Oc = **-1.5** % (2025-10-01..2025-10-31) [DISCARD: Redundant percent change already implied by p17 and p18.] quote: "321,850 326,783 -4,933 -1.5"
  - p25 Inter-prefectural movers (都道府県間移動者数), all movers, Japan, October 2024 = **167,107** person (2024-10-01..2024-10-31) [DISCARD: October 2024 inter-prefectural value duplicated by p15's comparison base.] quote: "都道府県間移動者数 168,057 167,107 950 0.6"
  - p26 Intra-prefectural movers (都道府県内移動者数), all movers, Japan, October 2024 = **211,095** person (2024-10-01..2024-10-31) [DISCARD: October 2024 intra-prefectural value duplicated by p16's comparison base.] quote: "都道府県内移動者数 211,694 211,095 599 0.3"
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?kana=11&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 13/13
  - p27 Total internal migration between municipalities (all movers), Japan, July 2026 = **390,799** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p28 Year-on-year change in total internal migration between municipalities (all move = **7,618** person (2026-07-01..2026-07-31) [DISCARD: Redundant change value already implied by p27 and p174.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p29 Year-on-year percent change in total internal migration between municipalities ( = **1.9** % (2026-07-01..2026-07-31) [DISCARD: Redundant percent change already implied by p27 and p174.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p30 Inter-prefectural movers (all movers), Japan, July 2026 = **181,604** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p31 Intra-prefectural movers (all movers), Japan, July 2026 = **209,195** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p32 Japanese movers between municipalities, Japan, July 2026 = **335,854** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p33 Year-on-year percent change in Japanese movers between municipalities, Japan, Ju = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Redundant percent change already implied by p32 and p177.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p34 Foreign movers between municipalities, Japan, July 2026 = **54,945** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p35 Year-on-year percent change in foreign movers between municipalities, Japan, Jul = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Redundant percent change already implied by p34 and p180.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p36 Japanese inter-prefectural movers, Japan, July 2026 = **150,347** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p37 Japanese intra-prefectural movers, Japan, July 2026 = **185,507** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p38 Foreign inter-prefectural movers, Japan, July 2026 = **31,257** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p39 Foreign intra-prefectural movers, Japan, July 2026 = **23,688** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `http://ecitizen.jp/Statdb/StatsData/0003420273` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2308/index.html` -> **snapshot** (snapshot 20251011123433); points raw/verified 11/11
  - p40 Total internal migration (moves between municipalities), all movers, Japan, Augu = **379,493** person (2023-08-01..2023-08-31) [keep: ] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p41 Change in total internal migration (moves between municipalities), all movers, J = **22,480** person (2023-08-01..2023-08-31) [DISCARD: Redundant change value already implied by p40 and its 2022 base.] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p42 Year-on-year change rate of total internal migration (moves between municipaliti = **5.6** % (2023-08-01..2023-08-31) [DISCARD: Redundant percent change already implied by p40 and its 2022 base.] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p43 Inter-prefectural movers, all movers, Japan, August 2023 = **173,963** person (2023-08-01..2023-08-31) [keep: ] quote: "移動者の都道府県間移動者数は17万3963人と、前年同月に比べ1万2369人(6.6%)減少。"
  - p44 Intra-prefectural movers, all movers, Japan, August 2023 = **205,530** person (2023-08-01..2023-08-31) [keep: ] quote: "移動者の都道府県内移動者数は20万5530人と、前年同月に比べ1万111人(4.7%)減少。"
  - p45 Total internal migration (moves between municipalities), Japanese movers only, J = **336,601** person (2023-08-01..2023-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万6601人と、前年同月に比べ2万1043人(5.9%)減少。"
  - p46 Inter-prefectural movers, Japanese movers only, Japan, August 2023 = **150,656** person (2023-08-01..2023-08-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万656人と、前年同月に比べ1万1591人(7.1%)減少。"
  - p47 Intra-prefectural movers, Japanese movers only, Japan, August 2023 = **185,945** person (2023-08-01..2023-08-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5945人と、前年同月に比べ9452人 (4.8%)減少。"
  - p48 Total internal migration (moves between municipalities), foreign movers only, Ja = **42,892** person (2023-08-01..2023-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2892人と、前年同月に比べ1437人(3.2%)減少。"
  - p49 Inter-prefectural movers, foreign movers only, Japan, August 2023 = **23,307** person (2023-08-01..2023-08-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万3307人と、前年同月に比べ778人(3.2%)減少。"
  - p50 Intra-prefectural movers, foreign movers only, Japan, August 2023 = **19,585** person (2023-08-01..2023-08-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は1万9585人と、前年同月に比べ659人(3.3%)減少。"
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d2 [related_series] Population register / demographic statistics

Hypothesis: Internal migration volume scales with the registered population base and with the foreign-resident share, which has been growing. Total moves ≈ registered population × monthly migration rate; the rate is fairly stable year to year, so population growth (including foreign residents) drives part of the change.

Queries issued by the searcher: 住民基本台帳 人口 2026年 外国人 総人口; Japan registered population 2026 foreign residents 住民基本台帳; 住民基本台帳人口移動報告 2026年7月 転入者数 転出者数 日本人; 住民基本台帳人口移動報告 2025年8月 転入超過 転入者数 総務省統計局; 住民基本台帳 人口 2026年 外国人 総人口; Statistics Bureau Japan Report on Internal Migration Basic Resident Registration monthly 2025; stat.go.jp 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; stat.go.jp data idou 2026年7月結果 住民基本台帳人口移動報告; 住民基本台帳人口移動報告 2025年8月 移動者数 転入 転出; 住民基本台帳に基づく人口 2026年1月1日 総人口 外国人; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2024年8月 市区町村間移動者数 35万

- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.nippon.com/ja/articles/-/54278` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/c32b4a72-aa04-485a-a2ac-5e26daca42e6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsData/0003420273` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/14
  - p51 Total inter-municipal movers (all nationalities), Japan, October 2025 = **379,751** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p13/p65.] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p52 Total inter-municipal movers (all nationalities), Japan, October 2024 = **378,202** person (2024-10-01..2024-10-31) [DISCARD: Duplicate of p14/p66.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p53 Japanese inter-municipal movers, Japan, October 2025 = **321,850** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p17/p67.] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p54 Japanese inter-municipal movers, Japan, October 2024 = **326,783** person (2024-10-01..2024-10-31) [DISCARD: Duplicate of p18/p67.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p55 Foreign inter-municipal movers, Japan, October 2025 = **57,901** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p19/p68.] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p56 Foreign inter-municipal movers, Japan, October 2024 = **51,419** person (2024-10-01..2024-10-31) [DISCARD: Duplicate of p20/p68.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p57 Year-on-year change in foreign inter-municipal movers, Japan, October 2025 vs Oc = **12.6** % (2025-10-01..2025-10-31) [DISCARD: Redundant percent change already implied by p19 and p20.] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p58 Year-on-year change in total inter-municipal movers, Japan, October 2025 vs Octo = **0.4** % (2025-10-01..2025-10-31) [DISCARD: Redundant change value already implied by p13 and p14.] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p59 Inter-prefectural movers (all nationalities), Japan, October 2025 = **168,057** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p60 Intra-prefectural movers (all nationalities), Japan, October 2025 = **211,694** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p61 Foreign inter-prefectural movers, Japan, October 2025 = **30,709** as written "3万 709", value check pending person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 3万 709人。前年同月に比べ増加 4147人( 15.6%)"
  - p62 Foreign intra-prefectural movers, Japan, October 2025 = **27,192** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 2万7192人。前年同月に比べ増加 2335人( 9.4%)"
  - p63 Japanese inter-prefectural movers, Japan, October 2025 = **137,348** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 13万7348人。前年同月に比べ減少 ▲ 3197人( ▲ 2.3%)"
  - p64 Japanese intra-prefectural movers, Japan, October 2025 = **184,502** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 18万4502人。前年同月に比べ減少 ▲ 1736人( ▲ 0.9%)"
- `https://emb3.nhk.or.jp/nhkworld/en/news/20260730_01/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&bunya_l=02&stat_infid=000040479057` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gaikokujin-press.com/archives/3245` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?page=1&iroha=29&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] Prefectural breakdown

Hypothesis: The national total equals the sum of prefectural in-migration (or out-migration) totals; prefectural August patterns (e.g., Tokyo, Osaka, Aichi) can be summed. If national August 2026 is unavailable, summing prefectural August 2025 values scaled by 2026 YTD prefectural trends gives the national figure.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 都道府県別; 総務省統計局 住民基本台帳人口移動報告 2026年 都道府県別 転入; 統計局 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; stat.go.jp 人口移動報告 2025年8月結果 市区町村間移動者数 34万8602人; 都道府県別 住民基本台帳人口移動報告 2025年8月; 住民基本台帳人口移動報告 2026年 都道府県別 転入超過; stat.go.jp 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; "住民基本台帳人口移動報告" 2025年8月結果 市区町村間移動者数 34万8602 都道府県別転入・転出者数; 住民基本台帳人口移動報告 2025年8月 都道府県別; 住民基本台帳人口移動報告 2026年 月次 statistics.go.jp; 統計局 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; stat.go.jp data idou rireki 2508 2025年8月結果 都道府県別転入・転出者数

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/info/mail/pdf/20260227_no1840.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p65 National total internal migration between municipalities (市区町村間移動者数), all movers = **379,751** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p13/p51.] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p66 National total internal migration between municipalities (市区町村間移動者数), all movers = **378,202** person (2024-10-01..2024-10-31) [DISCARD: Duplicate of p14/p52.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p67 National total internal migration between municipalities, Japanese movers (日本人移動 = **321,850** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p17/p53.] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p68 National total internal migration between municipalities, foreign movers (外国人移動者 = **57,901** person (2025-10-01..2025-10-31) [DISCARD: Duplicate of p19/p55.] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p69 National inter-prefectural movers (都道府県間移動者数), all movers, October 2025 = **168,057** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p70 National intra-prefectural movers (都道府県内移動者数), all movers, October 2025 = **211,694** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p71 Tokyo prefecture in-migrants (転入者数), all movers, October 2025 = **29,182** person (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p72 Osaka prefecture in-migrants (転入者数), all movers, October 2025 = **12,152** person (2025-10-01..2025-10-31) [keep: ] quote: "大 阪 府 12,152 12,202 -50 -0.4 11,543 11,301 242 2.1 609 901"
  - p73 Aichi prefecture in-migrants (転入者数), all movers, October 2025 = **8,056** person (2025-10-01..2025-10-31) [keep: ] quote: "愛 知 県 8,056 7,793 263 3.4 8,601 8,677 -76 -0.9 -545 -884"
  - p74 Tokyo metropolitan area (東京圏) in-migrants, all movers, October 2025 = **29,721** person (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p75 Nagoya metropolitan area (名古屋圏) in-migrants, all movers, October 2025 = **8,791** person (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p76 Osaka metropolitan area (大阪圏) in-migrants, all movers, October 2025 = **14,195** person (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p77 21 major cities total in-migrants (21大都市計 転入者数), all movers, October 2025 = **93,597** person (2025-10-01..2025-10-31) [keep: ] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
  - p78 National inter-prefectural movers, Japanese movers, October 2025 = **137,348** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数 168,057 167,107 950 0.6 137,348 140,545 -3,197 -2.3 30,709 26,562 4,147 15.6"
  - p79 National intra-prefectural movers, Japanese movers, October 2025 = **184,502** person (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数 211,694 211,095 599 0.3 184,502 186,238 -1,736 -0.9 27,192 24,857 2,335 9.4"
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kurashi-infra-hikaku.com/hikkoshi/ido/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsData/0003420273` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2601/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20260515082224); points raw/verified 15/12
  - p80 National total internal migration between municipalities (市区町村間移動者数), all movers = **328,136** person (2026-01-01..2026-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3"
  - p81 National total internal migration between municipalities (市区町村間移動者数), all movers = **327,312** person (2025-01-01..2025-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3"
  - p82 National total internal migration between municipalities, Japanese movers, Janua = **286,595** person (2025-01-01..2025-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3 280,982 286,595 -5,613 -2.0"
  - p83 National total internal migration between municipalities, foreign movers (外国人移動者 = **47,154** person (2026-01-01..2026-01-31) [keep: ] quote: "市区町村間移動者数は 4万7154人。前年同月に比べ増加 6437人( 15.8%)"
  - p84 National total internal migration between municipalities, foreign movers, Januar = **40,717** person (2025-01-01..2025-01-31) [keep: ] quote: "47,154 40,717 6,437 15.8"
  - p85 Tokyo prefecture in-migrants (転入者数), all movers, January 2026 = **27,465** person (2026-01-01..2026-01-31) [keep: ] quote: "東 京 都 27,465 27,193 272 1.0 25,038 24,966 72 0.3 2,427 2,227"
  - p86 Tokyo prefecture in-migrants (転入者数), all movers, January 2025 = **27,193** person (2025-01-01..2025-01-31) [keep: ] quote: "東 京 都 27,465 27,193 272 1.0 25,038 24,966 72 0.3 2,427 2,227"
  - p87 Osaka prefecture in-migrants (転入者数), all movers, January 2026 = **11,080** person (2026-01-01..2026-01-31) [keep: ] quote: "大 阪 府 11,080 10,971 109 1.0 10,543 10,190 353 3.5 537 781"
  - p88 Osaka prefecture in-migrants (転入者数), all movers, January 2025 = **10,971** person (2025-01-01..2025-01-31) [keep: ] quote: "大 阪 府 11,080 10,971 109 1.0 10,543 10,190 353 3.5 537 781"
  - p89 Aichi prefecture in-migrants (転入者数), all movers, January 2026 = **7,772** person (2026-01-01..2026-01-31) [keep: ] quote: "愛 知 県 7,772 7,455 317 4.3 7,819 7,867 -48 -0.6 -47 -412"
  - p90 Aichi prefecture in-migrants (転入者数), all movers, January 2025 = **7,455** person (2025-01-01..2025-01-31) [keep: ] quote: "愛 知 県 7,772 7,455 317 4.3 7,819 7,867 -48 -0.6 -47 -412"
  - p91 Tokyo metropolitan area (東京圏) in-migrants, all movers, January 2026 = **28,536** person (2026-01-01..2026-01-31) [keep: ] quote: "2026年1月 (令和8年1月) 28,536 23,805 4,731 8,320 8,812 -492 13,253 13,110 143"
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### d4 [base_rates] Seasonal decomposition

Hypothesis: August's share of annual internal migration is stable (roughly 8-9% of the year, elevated by summer relocations). Annual 2025 total × August share × 2026 growth adjustment yields August 2026.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年 年間 総数 移動者数; Japan internal migration annual total 2025 Basic Resident Registration report; 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数 前年同月; 住民基本台帳人口移動報告 2025年 年間 総数 移動者数; Japan internal migration annual total 2025 住民基本台帳 移動者数 統計; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月; 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年 年間 都道府県間移動 総数; Japan internal migration annual total 2024 Basic Resident Registration Report total moves; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数 前年同月

- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/9
  - p92 Annual total internal migration between municipalities (Japanese and foreign), 2 = **5,263,249** person (2023-01-01..2023-12-31) [DISCARD: Duplicate of p3/p191/p221/p256.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p93 Annual total internal migration between municipalities (Japanese and foreign), 2 = **5,207,746** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p2/p190/p220/p248.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p94 Annual total internal migration between municipalities (Japanese and foreign), 2 = **5,190,548** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p1/p189/p219/p247.] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p95 Annual internal migration between municipalities, Japanese movers only, 2024, Ja = **4,603,155** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p8/p225/p253.] quote: "総数 4,528,254 4,603,155 -74,901 -1.6"
  - p96 Annual internal migration between municipalities, foreign movers only, 2024, Jap = **604,591** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p10/p227/p255.] quote: "総数 662,294 604,591 57,703 9.5"
  - p97 Annual internal migration between municipalities, foreign movers only, 2025, Jap = **662,294** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p9/p226/p254.] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p98 Annual internal migration between municipalities, foreign movers only, 2023, Jap = **566,677** person (2023-01-01..2023-12-31) [DISCARD: Duplicate of p11/p228/p294.] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p99 Annual internal migration between municipalities, Japanese movers only, 2023, Ja = **4,696,572** person (2023-01-01..2023-12-31) [DISCARD: Duplicate of p12/p229/p296.] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
  - p100 Inter-prefectural migration (subset of municipal moves), 2025, Japan = **2,515,731** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p6/p172/p230/p251/p273/p301/p332.] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 15/15
  - p101 Annual internal migration between municipalities, Japan, 2025 (total moves) = **5,190,548** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p1.] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p102 Year-on-year change in annual internal migration between municipalities, Japan,  = **0.3** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p201/p223/p250/p272/p300/p331.] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p103 Annual inter-prefectural migration, Japan, 2025 = **2,515,731** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p6.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p104 Year-on-year change in inter-prefectural migration, Japan, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [DISCARD: Redundant restatement of the inter-prefectural annual change.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p105 In-migrants from abroad, Japan, 2025 = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p106 Year-on-year change in in-migrants from abroad, Japan, 2025 vs 2024 = **6.3** % (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p107 Out-migrants to abroad, Japan, 2025 = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p108 Year-on-year change in out-migrants to abroad, Japan, 2025 vs 2024 = **10.2** % (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p109 National net social increase (社会増減数), Japan, 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "全国の社会増減数は、国外からの転入者数(78万2165人)が国外への転出者数(40万9592人)を上回ったこと等により、33万7234人の社会増加、前年に比べ5548人の拡大"
  - p110 Year-on-year expansion of national net social increase, Japan, 2025 vs 2024 = **5,548** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p111 Net in-migration (転入超過) Tokyo metropolitan area, 2025 = **123,534** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p112 Year-on-year change in Tokyo area net in-migration, 2025 vs 2024 = **12,309** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p113 Net in-migration (転入超過) three major metropolitan areas combined, 2025 = **119,581** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p114 Year-on-year change in three major metropolitan areas net in-migration, 2025 vs  = **85** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p115 Net in-migration (転入超過) Tokyo prefecture, 2025 = **65,219** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数は東京都が6万5219人と最も多く、神奈川県が最も拡大(1089人)"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p116 Total internal migration between municipalities (all movers), July 2026, Japan = **390,799** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p27/p232.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p117 Year-on-year change in total internal migration between municipalities, July 202 = **7,618** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p233.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p118 Year-on-year percent change in total internal migration between municipalities,  = **1.9** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p234.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p119 Japanese movers internal migration between municipalities, July 2026, Japan = **335,854** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p32/p237.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p120 Year-on-year change in Japanese movers internal migration between municipalities = **9,318** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p238.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p121 Year-on-year percent change in Japanese movers internal migration between munici = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p239.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p122 Foreign movers internal migration between municipalities, July 2026, Japan = **54,945** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p34/p242.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p123 Year-on-year change in foreign movers internal migration between municipalities, = **1,700** person (moves between municipalities) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p243.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p124 Year-on-year percent change in foreign movers internal migration between municip = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p244.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p125 Total movers inter-prefectural migration, July 2026, Japan = **181,604** person (moves between prefectures) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p126 Total movers intra-prefectural migration, July 2026, Japan = **209,195** person (moves within prefecture) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p127 Japanese movers inter-prefectural migration, July 2026, Japan = **150,347** person (moves between prefectures) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p128 Japanese movers intra-prefectural migration, July 2026, Japan = **185,507** person (moves within prefecture) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p129 Foreign movers inter-prefectural migration, July 2026, Japan = **31,257** person (moves between prefectures) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p130 Foreign movers intra-prefectural migration, July 2026, Japan = **23,688** person (moves within prefecture) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `http://ecitizen.jp/Statdb/StatsData/0003420273` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsData/0003419960` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260528_no1867.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search/files?layout=dataset&cycle=1&toukei=00200523&tstat=000000070001&tclass1=000001008739&tclass2val=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsData/0003420482` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; value_as_written not in quote as a whole number: 2)

### d5 [shocks] Calendar and policy effects

Hypothesis: August 2026 calendar (weekday composition, Obon holiday timing) and any policy changes (e.g., foreign resident registration rules, moving-related administrative changes) could shift the count relative to August 2025. Quantify exposure: number of weekdays/weekends and any known registration-system changes.

Queries issued by the searcher: 2026年8月 カレンダー 平日 土日 祝日; 住民基本台帳人口移動報告 2025年8月 転入 転出 件数; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 在留カード マイナンバーカード 一体化 2026年 施行 外国人 住民基本台帳; 2026年8月 カレンダー 平日 土日 祝日; 住民基本台帳 制度変更 2025 2026 転入届 オンライン; 住民基本台帳人口移動報告 2026年6月 移動者数 前年同月比; 住民基本台帳人口移動報告 2025年8月 移動者数 転入 転出 総務省統計局; 住民基本台帳人口移動報告 2025年8月 転入 転出 移動者数; 2026年8月 カレンダー 平日 土日 祝日; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 2026年 転入届 住民基本台帳 制度変更 マイナンバー 引越し オンライン 手続き 変更

- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://kalatlas.com/ja/calendar/2026/august/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dayscalculator.site/calendar/2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://ecitizen.jp/Statdb/StatsData/0003420273` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp-newsfocus.com/foreign-resident-interprefectural-moves-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://benricalendar.com/august-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p131 Total internal migrants between municipalities (市区町村間移動者数), Japan, July 2026 = **390,799** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p27/p232.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p132 Year-on-year change in total internal migrants between municipalities, Japan, Ju = **7,618** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p233.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p133 Year-on-year percent change in total internal migrants between municipalities, J = **1.9** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p234.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p134 Japanese internal migrants between municipalities (日本人移動者の市区町村間移動者数), Japan, Jul = **335,854** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p32/p237.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p135 Year-on-year change in Japanese internal migrants between municipalities, Japan, = **9,318** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p238.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p136 Year-on-year percent change in Japanese internal migrants between municipalities = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p239.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p137 Foreign internal migrants between municipalities (外国人移動者の市区町村間移動者数), Japan, July = **54,945** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p34/p242.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p138 Year-on-year change in foreign internal migrants between municipalities, Japan,  = **1,700** person (2026-07-01..2026-07-31) [DISCARD: Duplicate of p243.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p139 Year-on-year percent change in foreign internal migrants between municipalities, = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p244.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p140 Total internal migrants between prefectures (都道府県間移動者数), Japan, July 2026 = **181,604** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p141 Total internal migrants within prefectures (都道府県内移動者数), Japan, July 2026 = **209,195** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p142 Japanese internal migrants between prefectures (日本人移動者の都道府県間移動者数), Japan, July 2 = **150,347** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p143 Japanese internal migrants within prefectures (日本人移動者の都道府県内移動者数), Japan, July 20 = **185,507** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p144 Foreign internal migrants between prefectures (外国人移動者の都道府県間移動者数), Japan, July 20 = **31,257** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p145 Foreign internal migrants within prefectures (外国人移動者の都道府県内移動者数), Japan, July 202 = **23,688** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/13
  - p146 Japan internal migration events between municipalities (all persons incl. foreig = **5,190,548** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p1.] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p147 Japan internal migration events between municipalities (all persons), annual tot = **5,207,746** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p2.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p148 Year-on-year change in Japan between-municipality migration events, 2025 vs 2024 = **-17,198** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p200/p222/p249/p271/p330.] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p149 Year-on-year rate of change in Japan between-municipality migration events, 2025 = **-0.3** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p201/p223/p250/p272/p300/p331.] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p150 Japanese nationals between-municipality migration events, annual total 2025 = **4,528,254** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7/p224/p252.] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p151 Japanese nationals between-municipality migration events, annual total 2024 = **4,603,155** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p8/p225/p253.] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p152 Foreign nationals between-municipality migration events, annual total 2025 = **662,294** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p9/p226/p254.] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p153 Foreign nationals between-municipality migration events, annual total 2024 = **604,591** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p10/p227/p255.] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p154 Japan between-municipality migration events, annual total 2023 = **5,263,249** person (2023-01-01..2023-12-31) [DISCARD: Duplicate of p3/p191/p221/p256.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p155 Japan between-municipality migration events, annual total 2022 = **5,310,972** person (2022-01-01..2022-12-31) [DISCARD: Duplicate of p162/p192/p231/p257/p263.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p156 Japan between-municipality migration events, annual total 2021 = **5,247,744** person (2021-01-01..2021-12-31) [DISCARD: Duplicate of p163/p193/p258/p264.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p157 Japan between-municipality migration events, annual total 2020 = **5,255,721** person (2020-01-01..2020-12-31) [DISCARD: Duplicate of p164/p194/p259/p265.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p158 Japan between-municipality migration events, annual total 2019 = **5,403,465** person (2019-01-01..2019-12-31) [DISCARD: Duplicate of p165/p195/p266.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- dropped by code checks: 2 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d6 [forecasts_markets] Official projections and research

Hypothesis: IPSS (National Institute of Population and Social Security Research) or MIC publications may project 2026 internal migration; these can constrain the annual level and thus August.

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年8月 転入転出 移動者数; 国立社会保障・人口問題研究所 人口移動 2026 推計; stat.go.jp 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 39万799人; 住民基本台帳人口移動報告 2025年 年結果 市区町村間移動者数 年間; 国立社会保障・人口問題研究所 人口移動 2026; Statistics Bureau Report on Internal Migration Japan Basic Resident Registration monthly 2025; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; stat.go.jp idou rireki 2608 2026年7月結果 住民基本台帳人口移動報告; 国立社会保障・人口問題研究所 人口移動 2026; 住民基本台帳人口移動報告 2025年 月別 移動者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://ipss.repo.nii.ac.jp/records/2000819` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/library/opac/Newly_arrived/detail?tmtl=1&idx=7&rgtn=WT2260036&hidx=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/library/opac/Newly_arrived?ppg=20&tmtl=3&idx=22&rfs=list&vw=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p159 Japan inter-municipal internal migration, annual total, 2025 (persons) = **5,190,548** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p1.] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p160 Japan inter-municipal internal migration, annual total, 2024 (persons) = **5,207,746** person (2024-01-01..2024-12-31) [DISCARD: Duplicate of p2.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p161 Japan inter-municipal internal migration, annual total, 2023 (persons) = **5,263,249** person (2023-01-01..2023-12-31) [DISCARD: Duplicate of p3.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p162 Japan inter-municipal internal migration, annual total, 2022 (persons) = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p163 Japan inter-municipal internal migration, annual total, 2021 (persons) = **5,247,744** person (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p164 Japan inter-municipal internal migration, annual total, 2020 (persons) = **5,255,721** person (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p165 Japan inter-municipal internal migration, annual total, 2019 (persons) = **5,403,465** person (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p166 Japan inter-municipal internal migration, annual total, 2018 (persons) = **5,359,174** person (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p167 Japan inter-municipal internal migration, annual total, 2017 (persons) = **5,318,617** person (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p168 Japan inter-municipal internal migration, annual total, 2016 (persons) = **5,251,717** person (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p169 Japan inter-municipal internal migration, annual total, 2015 (persons) = **5,384,553** person (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p170 Japan inter-municipal internal migration, year-on-year change, 2025 (persons) = **-17,198** person (2025-01-01..2025-12-31) [DISCARD: Duplicate of p200/p222/p249/p271/p330.] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p171 Japan inter-municipal internal migration, year-on-year change rate, 2025 (%) = **-0.3** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p201/p223/p250/p272/p300/p331.] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p172 Japan inter-prefectural internal migration, annual total, 2025 (persons) = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p173 Japan intra-prefectural internal migration, annual total, 2025 (persons) = **2,674,817** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2507/index.html` -> **snapshot** (snapshot 20260808220647); points raw/verified 15/15
  - p174 Total internal migration events between municipalities, nationwide, July 2025 (a = **398,417** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p175 Year-on-year change in total internal migration events between municipalities, J = **6,371** person (moves between municipalities) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p205.] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p176 Year-on-year percent change in total internal migration events between municipal = **1.6** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p206.] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p177 Japanese movers' internal migration events between municipalities, nationwide, J = **345,172** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p178 Year-on-year change in Japanese movers' internal migration events between munici = **10,632** person (moves between municipalities) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p208.] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p179 Year-on-year percent change in Japanese movers' internal migration events betwee = **3** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p209.] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p180 Foreign movers' internal migration events between municipalities, nationwide, Ju = **53,245** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p181 Year-on-year change in foreign movers' internal migration events between municip = **4,261** person (moves between municipalities) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p211.] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p182 Year-on-year percent change in foreign movers' internal migration events between = **8.7** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p212.] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p183 Total inter-prefectural migration events, nationwide, July 2025 (all movers) = **182,864** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p184 Total intra-prefectural migration events, nationwide, July 2025 (all movers) = **215,553** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
  - p185 Japanese movers' inter-prefectural migration events, nationwide, July 2025 = **154,148** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p186 Japanese movers' intra-prefectural migration events, nationwide, July 2025 = **191,024** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p187 Foreign movers' inter-prefectural migration events, nationwide, July 2025 = **28,716** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p188 Foreign movers' intra-prefectural migration events, nationwide, July 2025 = **24,529** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
- `https://www.e-stat.go.jp/stat-search/database?kana=11&toukei=00200523&result_page=1&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] seasonal pattern

Hypothesis: The August 2025 national total (all movers) is the single most valuable missing input: it would let the July 2026 YoY trend (-1.9%) be applied directly to last year's August level, completing the strongest series route. Without it we must bridge from August 2023 or from annual totals.

Queries issued by the searcher: stat.go.jp 人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; 令和7年8月 住民基本台帳人口移動報告 市区町村間移動者数 総数; 2025年8月 人口移動報告 市区町村間 移動者数 前年同月比; stat.go.jp 人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; 住民基本台帳人口移動報告 2025年（令和7年）8月結果 市区町村間移動者数 34万8602人 日本人移動者 外国人移動者; stat.go.jp 住民基本台帳人口移動報告 2026年（令和8年）7月結果 市区町村間移動者数; stat.go.jp 人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; stat.go.jp/data/idou/rireki/2508 住民基本台帳人口移動報告 2025年8月結果; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 前年同月に比べ 1.9%

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p189 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2025 = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p190 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2024 = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p191 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2023 = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p192 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2022 = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p193 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2021 = **5,247,744** person (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p194 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2020 = **5,255,721** person (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p195 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2019 = **5,403,465** person (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p196 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2018 = **5,359,174** person (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p197 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2017 = **5,318,617** person (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p198 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2016 = **5,251,717** person (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p199 Japan total inter-municipal movers (市区町村間移動者数), all movers, calendar year 2015 = **5,384,553** person (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p200 Year-on-year change in Japan total inter-municipal movers, all movers, 2025 vs 2 = **-17,198** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p201 Year-on-year percent change in Japan total inter-municipal movers, all movers, 2 = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p202 Year-on-year percent change in Japan total inter-municipal movers, all movers, 2 = **-1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p203 Japan inter-prefectural movers (都道府県間移動者数), all movers, calendar year 2025 = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
- `https://www.stat.go.jp/data/idou/rireki/2507/index.html` -> **snapshot** (snapshot 20260808220647); points raw/verified 15/15
  - p204 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **398,417** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p205 Year-on-year change in total internal migration events between municipalities, a = **6,371** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p206 Year-on-year percent change in total internal migration events between municipal = **1.6** % (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p207 Japanese movers internal migration events between municipalities (日本人移動者の市区町村間移動 = **345,172** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p208 Year-on-year change in Japanese movers internal migration events between municip = **10,632** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p209 Year-on-year percent change in Japanese movers internal migration events between = **3** % (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p210 Foreign movers internal migration events between municipalities (外国人移動者の市区町村間移動者 = **53,245** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p211 Year-on-year change in foreign movers internal migration events between municipa = **4,261** person (moves between municipalities) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p212 Year-on-year percent change in foreign movers internal migration events between  = **8.7** % (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p213 Total inter-prefectural migration events (都道府県間移動者数), all movers, Japan, July 20 = **182,864** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p214 Total intra-prefectural migration events (都道府県内移動者数), all movers, Japan, July 20 = **215,553** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
  - p215 Japanese movers inter-prefectural migration events, Japan, July 2025 = **154,148** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p216 Japanese movers intra-prefectural migration events, Japan, July 2025 = **191,024** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p217 Foreign movers inter-prefectural migration events, Japan, July 2025 = **28,716** person (moves between prefectures) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p218 Foreign movers intra-prefectural migration events, Japan, July 2025 = **24,529** person (moves within prefecture) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&bunya_l=02&tstat=000000070001&cycle=7&tclass1=000001128855&result_` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tokyo.vivinavi.com/mc/prt/_wid_fbe5824ea65900b790e962f5b390117f85b2092525` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?page=1&layout=dataset&iroha=12&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.com/real_estate_news/n/n25ec427671d5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/13
  - p219 National total inter-municipal movers (Japanese and foreign), calendar year 2025 = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p220 National total inter-municipal movers (Japanese and foreign), calendar year 2024 = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p221 National total inter-municipal movers (Japanese and foreign), calendar year 2023 = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p222 Year-on-year change in national total inter-municipal movers (Japanese and forei = **-17,198** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p223 Year-on-year percent change in national total inter-municipal movers (Japanese a = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p224 National inter-municipal movers, Japanese only, calendar year 2025 = **4,528,254** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p225 National inter-municipal movers, Japanese only, calendar year 2024 = **4,603,155** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p226 National inter-municipal movers, foreign only, calendar year 2025 = **662,294** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p227 National inter-municipal movers, foreign only, calendar year 2024 = **604,591** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p228 National inter-municipal movers, foreign only, calendar year 2023 = **566,677** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p229 National inter-municipal movers, Japanese only, calendar year 2023 = **4,696,572** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
  - p230 National inter-prefectural movers (Japanese and foreign), calendar year 2025 = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p231 National inter-municipal movers (Japanese and foreign), calendar year 2022 = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p232 National total inter-municipal movers (all movers), July 2026 = **390,799** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p233 Year-on-year change in national total inter-municipal movers (all movers), July  = **7,618** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p234 Year-on-year percent change in national total inter-municipal movers (all movers = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p235 National total inter-prefectural movers (all movers), July 2026 = **181,604** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p236 National total intra-prefectural movers (all movers), July 2026 = **209,195** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p237 Japanese movers inter-municipal movers, July 2026 = **335,854** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p238 Year-on-year change in Japanese inter-municipal movers, July 2026 = **9,318** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p239 Year-on-year percent change in Japanese inter-municipal movers, July 2026 = **2.7** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p240 Japanese movers inter-prefectural movers, July 2026 = **150,347** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p241 Japanese movers intra-prefectural movers, July 2026 = **185,507** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p242 Foreign movers inter-municipal movers, July 2026 = **54,945** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p243 Year-on-year change in foreign inter-municipal movers, July 2026 = **1,700** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p244 Year-on-year percent change in foreign inter-municipal movers, July 2026 = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p245 Foreign movers inter-prefectural movers, July 2026 = **31,257** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p246 Foreign movers intra-prefectural movers, July 2026 = **23,688** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b2 [own_history] monthly seasonality

Hypothesis: A full 2025 monthly series (Jan-Dec) would let us compute August's share of the annual total and the August/July ratio, converting the annual 2025 level (p1) into an August 2025 base and then applying the 2026 YoY trend. This unlocks the d4 annual-share route with a measured rather than assumed seasonal factor.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年 月別 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 時系列 月次 市区町村間移動者数 2024; stat.go.jp 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月; 住民基本台帳人口移動報告 長期時系列表 月別 移動者数 エクセル; "住民基本台帳人口移動報告" "2025年（令和7年）" 月結果 市区町村間移動者数 前年同月に比べ 2025年1月 3月 4月 5月 6月; 住民基本台帳人口移動報告 2025年 月別 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 時系列表 月次 都道府県; "市区町村間移動者数" 月別 2025年 表 全国 1月 2月 3月 統計局; stat.go.jp idou 2025np 表2 月 男女別移動者数 都道府県内移動者数 都道府県間移動者数; 住民基本台帳人口移動報告 2025年 月別 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 時系列 月次 市区町村間移動者数; stat.go.jp idou 2025年8月結果 市区町村間移動者数 前年同月; 統計局 月次レポート 主要統計時系列データ 住民基本台帳人口移動報告 市区町村間移動者数 2025年 月

- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/13
  - p247 Total internal migration events between municipalities (市区町村間移動者数), Japan, all p = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p248 Total internal migration events between municipalities (市区町村間移動者数), Japan, all p = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p249 Year-on-year change in total internal migration events between municipalities, J = **-17,198** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p250 Year-on-year percent change in total internal migration events between municipal = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p251 Inter-prefectural migration events (都道府県間移動者数), Japan, all persons, calendar yea = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p252 Inter-municipal migration events, Japan, Japanese movers only (日本人移動者), calendar = **4,528,254** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p253 Inter-municipal migration events, Japan, Japanese movers only, calendar year 202 = **4,603,155** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p254 Inter-municipal migration events, Japan, foreign movers only (外国人移動者), calendar  = **662,294** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p255 Inter-municipal migration events, Japan, foreign movers only, calendar year 2024 = **604,591** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p256 Inter-municipal migration events, Japan, all persons, calendar year 2023 = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p257 Inter-municipal migration events, Japan, all persons, calendar year 2022 = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p258 Inter-municipal migration events, Japan, all persons, calendar year 2021 = **5,247,744** person (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p259 Inter-municipal migration events, Japan, all persons, calendar year 2020 = **5,255,721** person (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p260 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2025 = **5,190,548** person (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p261 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2024 = **5,207,746** person (moves between municipalities) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p262 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2023 = **5,263,249** person (moves between municipalities) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p263 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2022 = **5,310,972** person (moves between municipalities) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p264 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2021 = **5,247,744** person (moves between municipalities) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p265 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2020 = **5,255,721** person (moves between municipalities) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p266 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2019 = **5,403,465** person (moves between municipalities) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p267 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2018 = **5,359,174** person (moves between municipalities) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p268 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2017 = **5,318,617** person (moves between municipalities) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p269 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2016 = **5,251,717** person (moves between municipalities) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p270 Japan internal migration between municipalities (市区町村間移動者数), annual total, 2015 = **5,384,553** person (moves between municipalities) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p271 Year-on-year change in Japan internal migration between municipalities (市区町村間移動者 = **-17,198** person (moves between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p272 Year-on-year percent change in Japan internal migration between municipalities ( = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p273 Japan inter-prefecture migration (都道府県間移動者数), annual total, 2025 = **2,515,731** person (moves between prefectures) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p274 Japan intra-prefecture migration (都道府県内移動者数), annual total, 2025 = **2,674,817** person (moves within prefecture between municipalities) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
- `https://www.e-stat.go.jp/stat-search/database?kana=11&toukei=00200523&result_page=1&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000560` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/headline/pdf/202506.pdf` -> **snapshot** (snapshot 20260419025306); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/rireki/2502/index.html` -> **snapshot** (snapshot 20251009235240); points raw/verified 15/15
  - p275 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **357,056** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万7056人と、前年同月に比べ7077人(1.9%)減少。"
  - p276 Year-on-year change in total internal migration events between municipalities, a = **7,077** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万7056人と、前年同月に比べ7077人(1.9%)減少。"
  - p277 Year-on-year percent change in total internal migration events between municipal = **1.9** % (2025-02-01..2025-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万7056人と、前年同月に比べ7077人(1.9%)減少。"
  - p278 Japanese movers internal migration events between municipalities (日本人移動者の市区町村間移動 = **314,397** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万4397人と、前年同月に比べ7586人(2.4%)減少。"
  - p279 Year-on-year change in Japanese movers internal migration events between municip = **7,586** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万4397人と、前年同月に比べ7586人(2.4%)減少。"
  - p280 Year-on-year percent change in Japanese movers internal migration events between = **2.4** % (2025-02-01..2025-02-28) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万4397人と、前年同月に比べ7586人(2.4%)減少。"
  - p281 Foreign movers internal migration events between municipalities (外国人移動者の市区町村間移動者 = **42,659** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2659人と、前年同月に比べ509人(1.2%)増加。"
  - p282 Year-on-year change in foreign movers internal migration events between municipa = **509** person (moves between municipalities) (2025-02-01..2025-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2659人と、前年同月に比べ509人(1.2%)増加。"
  - p283 Year-on-year percent change in foreign movers internal migration events between  = **1.2** % (2025-02-01..2025-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2659人と、前年同月に比べ509人(1.2%)増加。"
  - p284 Total movers inter-prefectural migration events (都道府県間移動者数), Japan, February 202 = **161,521** person (moves between prefectures) (2025-02-01..2025-02-28) [keep: ] quote: "移動者の都道府県間移動者数は16万1521人と、前年同月に比べ2909人(1.8%)減少。"
  - p285 Total movers intra-prefectural migration events (都道府県内移動者数), Japan, February 202 = **195,535** person (moves within prefecture) (2025-02-01..2025-02-28) [keep: ] quote: "移動者の都道府県内移動者数は19万5535人と、前年同月に比べ4168人(2.1%)減少。"
  - p286 Japanese movers inter-prefectural migration events, Japan, February 2025 = **138,817** person (moves between prefectures) (2025-02-01..2025-02-28) [keep: ] quote: "日本人移動者の都道府県間移動者数は13万8817人と、前年同月に比べ2751人(1.9%)減少。"
  - p287 Japanese movers intra-prefectural migration events, Japan, February 2025 = **175,580** person (moves within prefecture) (2025-02-01..2025-02-28) [keep: ] quote: "日本人移動者の都道府県内移動者数は17万5580人と、前年同月に比べ4835人 (2.7%)減少。"
  - p288 Foreign movers inter-prefectural migration events, Japan, February 2025 = **22,704** person (moves between prefectures) (2025-02-01..2025-02-28) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万2704人と、前年同月に比べ158人(0.7%)減少。"
  - p289 Foreign movers intra-prefectural migration events, Japan, February 2025 = **19,955** person (moves within prefecture) (2025-02-01..2025-02-28) [keep: ] quote: "外国人移動者の都道府県内移動者数は1万9955人と、前年同月に比べ667人(3.5%)増加。"
- `http://search.ckan.jp/datasets/catalog.data.metro.tokyo.lg.jp__dataset:t000003d0000000560` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&tstat=000000070001&cycle=7&tclass1=000001128355&tclass2val=0` -> **snapshot** (snapshot 20220525142014); points raw/verified 0/0
- `https://www-pref-yamaguchi-lg-jp.cache.yimg.jp/soshiki/22/225373.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&bunya_l=02&tstat=000000070001&cycle=7&tclass1=000001128855&result_` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search?iroha=1&layout=dataset&page=1&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b3 [related_series] foreign share trend

Hypothesis: The foreign-mover share has been rising (foreign +9.5% in 2025, +3.2% in July 2026) while Japanese movers fall; a 2026 YTD foreign/Japanese split would refine the August 2026 composition and reduce uncertainty in the total. Currently only July 2026 gives the split.

Queries issued by the searcher: 令和8年 人口移動報告 外国人移動者 市区町村間移動者数; stat.go.jp 2026年 住民基本台帳人口移動報告 外国人 日本人 移動者数; stat.go.jp 住民基本台帳人口移動報告 2026年1月結果 外国人移動者 市区町村間移動者数; stat.go.jp/data/idou/rireki/2508 2025年8月結果 市区町村間移動者数 日本人 外国人; 令和8年 人口移動報告 外国人移動者 累計 市区町村間移動者数; stat.go.jp 2026年 人口移動報告 日本人 外国人 市区町村間移動者数; stat.go.jp/data/idou/rireki/2607 2026年7月結果 外国人移動者 市区町村間移動者数; 住民基本台帳人口移動報告 2026年 上半期 外国人移動者 増加 日本人移動者 減少; 令和8年 人口移動報告 外国人移動者 市区町村間移動者数; stat.go.jp 2026年 上半期 市区町村間移動者数 日本人 外国人; stat.go.jp/data/idou/rireki/2607 2026年7月結果 外国人移動者 市区町村間移動者数; stat.go.jp/data/idou/rireki/2606 2026年6月結果 日本人移動者 外国人移動者 市区町村間

- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2602/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/9
  - p290 Total internal migration events between municipalities (Japanese + foreign), Jap = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p291 Japanese internal migration events between municipalities, Japan, calendar year  = **4,603,155** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p292 Foreign internal migration events between municipalities, Japan, calendar year 2 = **604,591** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p293 Year-on-year change rate in foreign internal migration events between municipali = **9.5** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p294 Foreign internal migration events between municipalities, Japan, calendar year 2 = **566,677** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p295 Foreign internal migration events between municipalities, Japan, calendar year 2 = **535,765** person (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
  - p296 Japanese internal migration events between municipalities, Japan, calendar year  = **4,696,572** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
  - p297 Japanese internal migration events between municipalities, Japan, calendar year  = **4,775,207** person (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 4,775,207 2,525,114 2,250,093 -0.9 -1.2 -0.6 2,519,845 1,279,793"
  - p298 Foreign internal migration events between municipalities, Japan, calendar year 2 = **429,023** person (2021-01-01..2021-12-31) [keep: ] quote: "3 2021 429,023 243,117 185,906 3.4 3.1 3.8 195,228 106,282"
- `https://jp-newsfocus.com/foreign-resident-interprefectural-moves-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 15/15
  - p299 Japan total internal migration between municipalities (市区町村間移動者数), all movers, 2 = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p300 Year-on-year change in Japan total internal migration between municipalities, al = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p301 Japan inter-prefectural migration (都道府県間移動者数), all movers, 2025 = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p302 In-migrants from abroad to Japan (国外からの転入者数), 2025 = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p303 Year-on-year change in in-migrants from abroad to Japan, 2025 = **6.3** % (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p304 Out-migrants from Japan to abroad (国外への転出者数), 2025 = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p305 Year-on-year change in out-migrants from Japan to abroad, 2025 = **10.2** % (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p306 Japan national net social change (社会増減数), 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "全国の社会増減数は、国外からの転入者数(78万2165人)が国外への転出者数(40万9592人)を上回ったこと等により、33万7234人の社会増加、前年に比べ5548人の拡大"
  - p307 Year-on-year expansion of Japan national net social change, 2025 = **5,548** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p308 Three major metropolitan areas net in-migration (転入超過), all movers, 2025 = **119,581** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p309 Three major metropolitan areas net in-migration (転入超過), Japanese movers only, 20 = **110,680** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p310 Three major metropolitan areas net in-migration (転入超過), foreign movers only, 202 = **8,901** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(外国人移動者)では8901人の転入超過、前年に比べ529人の拡大"
  - p311 Tokyo metropolitan area net in-migration (転入超過), foreign movers only, 2025 = **10,796** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は1万796人の転入超過、前年に比べ5710人の縮小"
  - p312 Tokyo metropolitan area net in-migration (転入超過), Japanese movers only, 2025 = **112,738** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は11万2738人の転入超過、前年に比べ6599人の縮小。30年連続の転入超過"
  - p313 Nagoya metropolitan area net out-migration (転出超過), foreign movers only, 2025 = **3,134** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は3134人の転出超過、前年に比べ4205人の縮小"
- `https://www.stat.go.jp/data/idou/rireki/2601/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20260515082224); points raw/verified 15/13
  - p314 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **328,136** person (2026-01-01..2026-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3 280,982 286,595 -5,613 -2.0 47,154 40,717 6,437 15.8"
  - p315 Foreign internal migration events between municipalities (外国人移動者 市区町村間移動者数), Jan = **47,154** person (2026-01-01..2026-01-31) [keep: ] quote: "・市区町村間移動者数は 4万7154人。前年同月に比べ増加 6437人( 15.8%)"
  - p316 Japanese internal migration events between municipalities, January 2025 (year-ea = **286,595** person (2025-01-01..2025-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3 280,982 286,595 -5,613 -2.0 47,154 40,717 6,437 15.8"
  - p317 Foreign internal migration events between municipalities, January 2025 (year-ear = **40,717** person (2025-01-01..2025-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3 280,982 286,595 -5,613 -2.0 47,154 40,717 6,437 15.8"
  - p318 Total internal migration events between municipalities, January 2025 (year-earli = **327,312** person (2025-01-01..2025-01-31) [keep: ] quote: "市区町村間移動者数 328,136 327,312 824 0.3 280,982 286,595 -5,613 -2.0 47,154 40,717 6,437 15.8"
  - p319 Year-on-year change rate in foreign internal migration events between municipali = **15.8** % (2026-01-01..2026-01-31) [keep: ] quote: "・市区町村間移動者数は 4万7154人。前年同月に比べ増加 6437人( 15.8%)"
  - p320 Year-on-year change in Japanese internal migration events between municipalities = **5,613** person (2026-01-01..2026-01-31) [keep: ] quote: "・市区町村間移動者数は 28万 982人。前年同月に比べ減少 ▲ 5613人( ▲ 2.0%)"
  - p321 Year-on-year change rate in Japanese internal migration events between municipal = **2** % (2026-01-01..2026-01-31) [keep: ] quote: "・市区町村間移動者数は 28万 982人。前年同月に比べ減少 ▲ 5613人( ▲ 2.0%)"
  - p322 Inter-prefectural migration events (都道府県間移動者数), all movers, January 2026 = **151,680** person (2026-01-01..2026-01-31) [keep: ] quote: "都道府県間移動者数 151,680 149,033 2,647 1.8 125,662 127,112 -1,450 -1.1 26,018 21,921 4,097 18.7"
  - p323 Intra-prefectural migration events (都道府県内移動者数), all movers, January 2026 = **176,456** person (2026-01-01..2026-01-31) [keep: ] quote: "都道府県内移動者数 176,456 178,279 -1,823 -1.0 155,320 159,483 -4,163 -2.6 21,136 18,796 2,340 12.4"
  - p324 Foreign inter-prefectural migration events (外国人移動者 都道府県間移動者数), January 2026 = **26,018** person (2026-01-01..2026-01-31) [keep: ] quote: "・都道府県間移動者数は 2万6018人。前年同月に比べ増加 4097人( 18.7%)"
  - p325 Foreign intra-prefectural migration events (外国人移動者 都道府県内移動者数), January 2026 = **21,136** person (2026-01-01..2026-01-31) [keep: ] quote: "・都道府県内移動者数は 2万1136人。前年同月に比べ増加 2340人( 12.4%)"
  - p326 Japanese inter-prefectural migration events (日本人移動者 都道府県間移動者数), January 2026 = **125,662** person (2026-01-01..2026-01-31) [keep: ] quote: "・都道府県間移動者数は 12万5662人。前年同月に比べ減少 ▲ 1450人( ▲ 1.1%)"
- `https://www.stat.go.jp/info/mail/pdf/20260227_no1840.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 14/14
  - p327 Japan total inter-municipal movers (市区町村間移動者数), calendar year 2025 = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p328 Japan total inter-municipal movers (市区町村間移動者数), calendar year 2025 (table 1) = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p329 Japan total inter-municipal movers (市区町村間移動者数), calendar year 2024 = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p330 Year-on-year change in Japan total inter-municipal movers, 2025 vs 2024 = **-17,198** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p331 Year-on-year percent change in Japan total inter-municipal movers, 2025 = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p332 Japan inter-prefectural movers (都道府県間移動者数), calendar year 2025 = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p333 Japan intra-prefectural movers (都道府県内移動者数), calendar year 2025 = **2,674,817** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p334 Inflow from abroad (国外からの転入者数), calendar year 2025 = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p335 Outflow abroad (国外への転出者数), calendar year 2025 = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p336 Year-on-year percent change in inflow from abroad, 2025 = **6.3** % (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p337 Year-on-year percent change in outflow abroad, 2025 = **10.2** % (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p338 Inflow from abroad (国外からの転入者数), calendar year 2024 = **735,883** person (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数 - - - - - 358,359 209,700 639,124 700,138 735,883 782,165"
  - p339 Outflow abroad (国外への転出者数), calendar year 2024 = **371,615** person (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数 - - - - - 226,845 224,077 312,484 346,690 371,615 409,592"
  - p340 National social increase (社会増加数), calendar year 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "を上回ったこと等により、33万7234人の社会増加、前年に比べ5548人の拡大"
- dropped by code checks: 8 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 5; value_as_written not in quote as a whole number: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august 2026 migration', 'juki-net moves']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p94', 'p101', 'p146', 'p159'] All state the same 2025 annual total of 5,190,548 municipal-to-municipal movers; they are duplicate vintages of one Statistics Bureau release, not independent confirmation.
- corroborating: ['p2', 'p93', 'p147', 'p160'] Same 2024 annual total 5,207,746; duplicate copies of one source.
- corroborating: ['p3', 'p92', 'p154', 'p161'] Same 2023 annual total 5,263,249; duplicate copies.
- corroborating: ['p1', 'p4', 'p5', 'p148', 'p149', 'p170', 'p171'] Level, absolute change and percent change for 2025 are internally consistent (5,207,746 - 17,198 = 5,190,548; -0.3%).
- corroborating: ['p7', 'p8', 'p95', 'p150', 'p151'] Japanese-only annual totals 2024/2025 consistent with the -1.6% change.
- corroborating: ['p9', 'p10', 'p11', 'p96', 'p97', 'p98', 'p152', 'p153'] Foreign-only annual totals 2023-2025 consistent with +9.5% in 2025; Japanese + foreign sums to the all-mover totals.
- corroborating: ['p13', 'p14', 'p21', 'p22', 'p51', 'p52', 'p58', 'p65', 'p66'] October 2025/2024 monthly totals and their +0.4% change agree across duplicate copies.
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p23', 'p24', 'p53', 'p54', 'p55', 'p56', 'p57', 'p67', 'p68'] October Japanese (-1.5%) and foreign (+12.6%) components sum to the all-mover total; duplicates of one release.
- corroborating: ['p27', 'p28', 'p29', 'p116', 'p117', 'p118', 'p131', 'p132', 'p133'] July 2026 total 390,799 with -7,618 (-1.9%) YoY; duplicate copies of the same July 2026 release.
- corroborating: ['p32', 'p33', 'p34', 'p35', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139'] July 2026 Japanese 335,854 (-2.7%) and foreign 54,945 (+3.2%) sum to 390,799; consistent.
- corroborating: ['p174', 'p175', 'p176', 'p177', 'p178', 'p179', 'p180', 'p181', 'p182'] July 2025 total 398,417 with Japanese 345,172 and foreign 53,245; consistent with the July 2026 YoY comparison (398,417 - 7,618 = 390,799).
- corroborating: ['p40', 'p41', 'p42', 'p45', 'p48'] August 2023 total 379,493 = Japanese 336,601 + foreign 42,892; internally consistent August benchmark.
- corroborating: ['p1', 'p27', 'p174'] Annual 2025 level and July 2025/2026 monthly levels are mutually consistent; July 2026 is running about 1.9% below July 2025.
- conflicting: ['p40', 'p27'] August 2023 (379,493) is lower than July 2026 (390,799) and July 2025 (398,417); August is not uniformly higher than July, so a simple 'August is a peak month' seasonal assumption is not safe. August 
- corroborating: ['p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77'] Prefectural/metropolitan in-migration figures for October 2025 are a partial (in-migration only) view; they cannot be summed to the national total without double counting inter-prefectural moves, so t
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p162', 'p163', 'p164', 'p165', 'p166', 'p167', 'p168', 'p169'] Same annual series (市区町村間移動者数, all movers) from the same Statistics Bureau table; p1/p2/p3 are duplicated by p189-p199, p219-p221, p247-p248, p256-p259, p260-p270, p290, p327-p329. One underlying meas
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p224', 'p225', 'p226', 'p227', 'p228', 'p229', 'p252', 'p253', 'p254', 'p255', 'p291', 'p292', 'p294', 'p296', 'p297', 'p298'] Japanese/foreign split of the same annual series; p7+p9 = p1 and p8+p10 = p2, so they are components of the total, not independent evidence.
- corroborating: ['p40', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50'] August 2023 monthly report; p43+p44 = p40 and p45+p48 = p40, so the split is internally consistent. Only one August observation exists, so it cannot by itself establish the August seasonal level.
- corroborating: ['p27', 'p30', 'p31', 'p32', 'p34', 'p36', 'p37', 'p38', 'p39', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p232', 'p235', 'p236', 'p237', 'p242', 'p245', 'p246'] July 2026 report; duplicated across ids. p30+p31 = p27 and p32+p34 = p27. This is the latest observed month and the key trend anchor.
- corroborating: ['p174', 'p177', 'p180', 'p183', 'p184', 'p185', 'p186', 'p187', 'p188', 'p204', 'p207', 'p210', 'p213', 'p214', 'p215', 'p216', 'p217', 'p218'] July 2025 report; duplicated. p174 is the year-earlier value for the July 2026 comparison and is consistent with p27 + p233.
- corroborating: ['p13', 'p15', 'p16', 'p17', 'p19', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p69', 'p70', 'p78', 'p79'] October 2025 report; p15+p16 = p13 and p17+p19 = p13. Useful only as a level check on monthly magnitude, not for August.
- corroborating: ['p80', 'p81', 'p82', 'p83', 'p84', 'p314', 'p315', 'p316', 'p317', 'p318', 'p319', 'p320', 'p321', 'p322', 'p323', 'p324', 'p325', 'p326'] January 2026 report; duplicated. Shows foreign movers growing (+15.8%) while Japanese movers fall (-2.0%), consistent with the July 2026 pattern.
- corroborating: ['p275', 'p276', 'p277', 'p278', 'p279', 'p280', 'p281', 'p282', 'p283', 'p284', 'p285', 'p286', 'p287', 'p288', 'p289'] February 2025 report; another monthly level point, not August.
- corroborating: ['p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91'] Prefectural in-migration for October 2025 and January 2026. These are in-migration (転入) counts, not the same as inter-municipal movers, and cannot be summed to the national total without double counti
- corroborating: ['p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p302', 'p303', 'p304', 'p305', 'p306', 'p307', 'p308', 'p309', 'p310', 'p311', 'p312', 'p313', 'p334', 'p335', 'p336', 'p337', 'p338', 'p339', 'p340'] Annual 2025 migration report (abroad flows, net social change, metropolitan net migration). Context for the foreign-mover growth driver; not a direct input to an August monthly level.
- corroborating: ['p200', 'p201', 'p202', 'p222', 'p223', 'p249', 'p250', 'p271', 'p272', 'p293', 'p300', 'p330', 'p331'] Year-on-year changes of the annual series; consistent with p1 vs p2 and p9 vs p10. Duplicated across ids.
- conflicting: ['p40', 'p27', 'p174'] Not a true conflict but a scope caution: August 2023 (p40 = 379,493) is below July 2025 (p174 = 398,417) and July 2026 (p27 = 390,799). August is not necessarily the peak month, so an August share nea

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 vs August 2025 YoY change factor for all inter-municipal movers | 0.981 | 0.94..1.02 | 0.8758..1.095 (widened) | ratio | m2 (m2), m4 (m4) | July 2026 was -1.9% YoY (p27 vs p174) with Japanese movers -2.7% (p32 vs p177) and foreign movers +3.2% (p34 vs p180); January 2026 showed the same pattern (p314 vs p318, p315 vs p317). A modest continued decline near -2% is the central value; the range allows for foreign-mover acceleration or a Jap | The July 2026 YoY trend carries into August 2026 without a large calendar or policy break. | A published August 2026 figure outside the range, or evidence of a registration-rule change or Obon-timing shift that moves August 2026 materially away from the July trend. |
| a2 | August share of the annual inter-municipal migration total | 0.083 | 0.075..0.092 | 0.05874..0.1175 (widened) | ratio | m2 (m2) | No kept point gives a measured August share of the annual total. August 2023 (p40 = 379,493) is about 7.2% of the 2023 annual total (p3 = 5,263,249), and July 2025 (p174 = 398,417) is about 7.7% of the 2025 annual total (p1 = 5,190,548); August is typically slightly above July because of late-summer | The 2026 seasonal shape resembles recent years and August is not an outlier month. | A published monthly series showing August shares consistently outside 7.5-9.2% of the annual total. |
| a3 | Two-year bridge factor from August 2023 to August 2026 | 0.965 | 0.9..1.03 | 0.6808..1.362 (widened) | ratio | m3 (m3) | The annual total fell from 5,263,249 in 2023 (p3) to 5,190,548 in 2025 (p1), a factor of about 0.986 over two years; the July 2026 YoY trend (p27 vs p174) adds a further small decline. A factor near 0.965 with a wide range reflects the uncertainty in extrapolating a single August observation three y | The August seasonal pattern and the national migration trend are stable between 2023 and 2026. | Evidence that August 2026 differs sharply from the 2023-2025 trend, for example a large policy or demographic shock. |
| a4 | August 2025 vs July 2025 level ratio for all inter-municipal movers | 0.97 | 0.9..1.05 | 0.6874..1.375 (widened) | ratio | m4 (m4) | Repairs m1: yoy_scaling needs a target value for August 2025, which no kept point supplies. The only observed August level is August 2023 (p40 = 379,493) and the only observed July 2025 level is p174 = 398,417; the August/July ratio in 2023 was 379,493 / (July 2023 implied by p174 and its -1.6% YoY, | The August-to-July seasonal ratio in 2025 resembles the 2023 ratio and the recent stable seasonal pattern. | A published August 2025 or August 2026 figure showing the August/July ratio far outside 0.90-1.05. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | n/a | ['p40', 'p174', 'p27'] / [] | [] |  | 0.00 |  | yoy_scaling needs target for 2025 |
| m2 | formula_mc | 421,767 | ['p1'] / ['a1', 'a2'] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | formula_mc | 365,498 | ['p40'] / ['a3'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m4 | formula_mc | 376,858 | ['p174'] / ['a1', 'a4'] | [] |  | 1.00 | B3 of 3 blocks; median of blocks: this block is the median |  |

- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Method details (computed by code):

- m2 formula_mc: p1 * a2 * a1; Monte Carlo P10 to P90 281,443 to 636,303; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.50 (Monte Carlo of the formula inputs)
- m3 formula_mc: p40 * a3; Monte Carlo P10 to P90 246,692 to 540,182; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m4 formula_mc: p174 * a4 * a1; Monte Carlo P10 to P90 252,159 to 567,572; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.50 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 421,767 (width x/÷1.50, Monte Carlo of the formula inputs); B2 = m3: 365,498 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m4: 376,858 (width x/÷1.50, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.49; Birge ratio 0.24 (not above one, so no widening); final width x/÷1.49.

Result: central **376,858** person, 80% interval [252,144, 563,256] person, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

Unit of the estimate: person (persons (moves between municipalities); total for 2026-08-01 to 2026-08-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for moves between municipalities within Japan (Japanese and foreign residents combined) occurring in August 2026, as first reported in the Statistics Bureau's monthly Report on Internal Migration, is 376,858 person (80% model-based interval 252,144 to 563,256 person).

Evidence: observed anchors include July 2025 (398,417 person (moves between municipalities)), July 2026 (390,799 person), August 2023 (379,493 person) and the 2025 annual total (5,190,548 person). The retained route builds an August 2025 level from July 2025 times an August/July ratio (0.97) and applies a YoY factor (0.981); alternative routes use the annual-share (0.083) and a two-year bridge (0.965). All three depend on analyst assumptions, not measured August shares or ratios. Code combined blocks by equal weight per input-overlap block, not by backtest accuracy (no backtest errors available).

Main risk: the assumed August seasonal share/ratio is unobserved. The most useful missing evidence is an actual August 2025 inter-municipal total.

Unit of the estimate: person (persons (moves between municipalities); total for 2026-08-01 to 2026-08-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 vs August 2025 YoY change factor for all inter-municipal movers: 0.981 ratio, range 0.8758 to 1.095 (range widened by code); used by m2, m4. Overturned by: A published August 2026 figure outside the range, or evidence of a registration-rule change or Obon-timing shift that moves August 2026 materially away from the July trend.
- a2 August share of the annual inter-municipal migration total: 0.083 ratio, range 0.05874 to 0.1175 (range widened by code); used by m2. Overturned by: A published monthly series showing August shares consistently outside [n]-[n] of the annual total.
- a3 Two-year bridge factor from August 2023 to August 2026: 0.965 ratio, range 0.6808 to 1.362 (range widened by code); used by m3. Overturned by: Evidence that August 2026 differs sharply from the 2023-2025 trend, for example a large policy or demographic shock.
- a4 August 2025 vs July 2025 level ratio for all inter-municipal movers: 0.97 ratio, range 0.6874 to 1.375 (range widened by code); used by m4. Overturned by: A published August 2025 or August 2026 figure showing the August/July ratio far outside [n]-[n].

Method details (computed by code):
- m2 formula_mc: p1 * a2 * a1; Monte Carlo P10 to P90 281,443 to 636,303; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.50 (Monte Carlo of the formula inputs)
- m3 formula_mc: p40 * a3; Monte Carlo P10 to P90 246,692 to 540,182; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m4 formula_mc: p174 * a4 * a1; Monte Carlo P10 to P90 252,159 to 567,572; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.50 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 421,767 (width x/÷1.50, Monte Carlo of the formula inputs); B2 = m3: 365,498 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m4: 376,858 (width x/÷1.50, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.49; Birge ratio 0.24 (not above one, so no widening); final width x/÷1.49.

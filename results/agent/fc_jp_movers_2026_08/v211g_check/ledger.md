# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of persons who changed their municipality of residence within Japan (inter-municipal/internal migration moves) during August 2026, as recorded in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration (住民基本台帳人口移動報告), countin | unit person (moves) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan (総務省統計局), Ministry of Internal Affairs and Communications

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau time series

Hypothesis: The August 2026 total is best anchored on the same month in prior years (August 2023, 2024, 2025) plus the most recent published months before the cutoff (e.g., Jan-Jul 2026), since internal migration has strong seasonality (August is a peak moving month) and a stable level with modest year-over-year drift. Target = prior August level × (1 + recent YoY growth).

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 転入 転出 総務省統計局; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 前年同月; stat.go.jp 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 34万

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/12
  - p1 Japanese-only inter-municipal movers, July 2026 = **335,854** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p2 Year-over-year change in Japanese-only inter-municipal movers, July 2026 = **9,318** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Redundant with p1; the level p1 is what the method needs, and the change is derivable from p1 and prior-year data not in] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p3 Year-over-year percent change in Japanese-only inter-municipal movers, July 2026 = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Redundant with p1; percent change adds no independent information for a level-based route.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p4 Foreign-only inter-municipal movers, July 2026 = **54,945** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p5 Year-over-year change in foreign-only inter-municipal movers, July 2026 = **1,700** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Redundant with p4; the level is the usable input.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p6 Year-over-year percent change in foreign-only inter-municipal movers, July 2026 = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Redundant with p4; percent change adds no independent information.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p7 Total inter-prefectural movers (all persons), July 2026 = **181,604** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p8 Total intra-prefectural movers (all persons), July 2026 = **209,195** persons (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p9 Japanese-only inter-prefectural movers, July 2026 = **150,347** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Sub-component of p1 (Japanese inter-prefectural); not needed separately and would double-count if combined with p1.] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p10 Japanese-only intra-prefectural movers, July 2026 = **185,507** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Sub-component of p1 (Japanese intra-prefectural); not needed separately.] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p11 Foreign-only inter-prefectural movers, July 2026 = **31,257** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Sub-component of p4 (foreign inter-prefectural); not needed separately.] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p12 Foreign-only intra-prefectural movers, July 2026 = **23,688** persons (moves) (2026-07-01..2026-07-31) [DISCARD: Sub-component of p4 (foreign intra-prefectural); not needed separately.] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/8
  - p13 Total inter-municipal internal migration moves, Japan, all persons (Japanese + f = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p14 Total inter-municipal internal migration moves, Japan, all persons (Japanese + f = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p82 (2023 annual total); redundant copy.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p15 Year-over-year change rate of total inter-municipal internal migration moves, Ja = **-1.1** percent (2024-01-01..2024-12-31) [DISCARD: Redundant with p92 (2024 YoY rate); duplicate representation.] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p16 Year-over-year change rate of total inter-municipal internal migration moves, Ja = **-0.9** percent (2023-01-01..2023-12-31) [DISCARD: Redundant with p93 (2023 YoY rate); duplicate representation.] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p17 Inter-municipal internal migration moves, Japan, Japanese movers only, calendar  = **4,603,155** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p18 Inter-municipal internal migration moves, Japan, foreign movers only, calendar y = **604,591** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p19 Inter-municipal internal migration moves, Japan, foreign movers only, calendar y = **566,677** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p20 Inter-municipal internal migration moves, Japan, Japanese movers only, calendar  = **4,696,572** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 5; value_as_written not in quote as a whole number: 5)

### d2 [related_series] Foreign vs Japanese split

Hypothesis: Foreign residents' internal migration has been rising and is a growing share of total moves; the combined total = Japanese-resident moves + foreign-resident moves. If the Japanese component is stable and the foreign component is trending up, the combined August 2026 total exceeds the Japanese-only August level by the foreign share.

Queries issued by the searcher: 住民基本台帳人口移動報告 外国人 転入 月別; 住民基本台帳人口移動報告 2025年8月 転入 転出 外国人 日本人; 統計局 住民基本台帳人口移動報告 2026年7月結果 外国人移動者; 住民基本台帳に基づく人口 外国人 2026年1月1日 総務省 過去最多

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gaikokujin-press.com/archives/3245` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/14
  - p21 Total inter-municipal internal migration moves (Japanese + foreign), nationwide, = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p22 Japanese-resident inter-municipal internal migration moves, nationwide, calendar = **4,528,254** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p23 Japanese-resident inter-municipal internal migration moves, nationwide, calendar = **4,603,155** persons (moves) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p17 (2024 Japanese-only annual total); redundant copy.] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p24 Foreign-resident inter-municipal internal migration moves, nationwide, calendar  = **662,294** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p25 Foreign-resident inter-municipal internal migration moves, nationwide, calendar  = **604,591** persons (moves) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p18 (2024 foreign-only annual total); redundant copy.] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p26 Year-on-year percent change in foreign-resident inter-municipal moves, 2025 vs 2 = **9.5** percent (2025-01-01..2025-12-31) [DISCARD: Redundant with p18/p24 levels; the 9.5% growth is derivable and adds no independent input.] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p27 Foreign-resident inter-municipal moves, 2023 = **566,677** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p28 Foreign-resident inter-municipal moves, 2022 = **535,765** persons (moves) (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
  - p29 Foreign-resident inter-municipal moves, 2021 = **429,023** persons (moves) (2021-01-01..2021-12-31) [keep: ] quote: "3 2021 429,023 243,117 185,906 3.4 3.1 3.8 195,228 106,282"
  - p30 Foreign-resident inter-municipal moves, 2020 = **414,869** persons (moves) (2020-01-01..2020-12-31) [keep: ] quote: "2 2020 414,869 235,799 179,070 -19.3 -19.1 -19.6 198,369 108,167"
  - p31 Foreign-resident inter-municipal moves, 2019 = **514,274** persons (moves) (2019-01-01..2019-12-31) [keep: ] quote: "令和 元 年 2019 514,274 291,524 222,750 9.5 10.5 8.3 243,193 133,156"
  - p32 Foreign-resident inter-municipal moves, 2018 = **469,461** persons (moves) (2018-01-01..2018-12-31) [keep: ] quote: "30 2018 469,461 263,823 205,638 10.5 12.0 8.5 227,353 123,424"
  - p33 Foreign-resident inter-municipal moves, 2017 = **425,036** persons (moves) (2017-01-01..2017-12-31) [keep: ] quote: "29 2017 425,036 235,498 189,538 14.6 16.2 12.8 207,282 111,105"
  - p34 Foreign-resident inter-municipal moves, 2016 = **370,750** persons (moves) (2016-01-01..2016-12-31) [keep: ] quote: "28 2016 370,750 202,678 168,072 8.1 8.9 7.1 185,735 98,497"
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d3 [base_rates] Population × migration rate

Hypothesis: Total moves in a month ≈ resident population × monthly inter-municipal migration rate. August rate is seasonally elevated. Target = (Japanese population + foreign population) × August monthly migration rate, where the rate is derived from prior-year August moves divided by prior-year population.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 移動者数; 住民基本台帳に基づく人口 2026年1月1日 総人口 外国人; 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数; 住民基本台帳人口移動報告 移動率 住民基本台帳人口に基づく移動率 2025年 年報

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/14
  - p35 Total inter-municipal (市区町村間) movers, all nationalities, Japan, October 2025 = **379,751** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p36 Total inter-municipal movers, all nationalities, Japan, October 2024 (prior-year = **378,202** persons (moves) (2024-10-01..2024-10-31) [DISCARD: Duplicate of p70 (October 2024 all-person total); redundant copy.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p37 Japanese inter-municipal movers, Japan, October 2025 = **321,850** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p38 Japanese inter-municipal movers, Japan, October 2024 = **326,783** persons (moves) (2024-10-01..2024-10-31) [DISCARD: Duplicate of p72 (October 2024 Japanese total); redundant copy.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p39 Foreign inter-municipal movers, Japan, October 2025 = **57,901** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p40 Foreign inter-municipal movers, Japan, October 2024 = **51,419** persons (moves) (2024-10-01..2024-10-31) [DISCARD: Duplicate of p66 (October 2024 foreign total); redundant copy.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p41 Inter-prefectural (都道府県間) movers, all nationalities, Japan, October 2025 = **168,057** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p42 Intra-prefectural (都道府県内) movers, all nationalities, Japan, October 2025 = **211,694** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p43 Year-on-year change in total inter-municipal movers, Japan, October 2025 vs Octo = **0.4** percent (2025-10-01..2025-10-31) [DISCARD: Redundant with p69/p70 levels; change is derivable.] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p44 Year-on-year change in foreign inter-municipal movers, Japan, October 2025 vs Oc = **12.6** percent (2025-10-01..2025-10-31) [DISCARD: Redundant with p65/p66 levels; change is derivable.] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p45 Total in-migrants (転入者数), all 47 prefectures, Japan, October 2025 = **168,057** persons (moves) (2025-10-01..2025-10-31) [DISCARD: Inter-prefectural in-migrant total, not the inter-municipal target; overlaps p41 and is not the target quantity.] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p46 Total out-migrants (転出者数), all 47 prefectures, Japan, October 2025 = **168,057** persons (moves) (2025-10-01..2025-10-31) [DISCARD: Out-migrant total, not the inter-municipal target; not usable for the target level.] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p47 Net in-migration (転入超過数), all 47 prefectures, Japan, October 2025 = **0** persons (2025-10-01..2025-10-31) [DISCARD: Net migration (zero by construction), not a gross move count; irrelevant to the target.] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p48 Total in-migrants, 21 major cities (21大都市計), October 2025 = **93,597** persons (moves) (2025-10-01..2025-10-31) [DISCARD: In-migrants to 21 major cities only; a partial geographic subset, not the national inter-municipal total.] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
- `https://www.sentankyo.jp/articles/c32b4a72-aa04-485a-a2ac-5e26daca42e6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d4 [shocks] Calendar and policy effects

Hypothesis: August 2026 move counts may deviate from trend due to calendar effects (number of weekends, Obon moving season), any policy changes affecting registration (e.g., My Number / residence certificate procedures), or economic conditions. Identifying measurable deviations constrains the adjustment from the prior-August anchor.

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年 月次 転入 転出; 住民基本台帳 制度 変更 2026 転入届 オンライン; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月; 2026年8月 引越し 繁忙期 お盆 転入 転出 日本 ニュース

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2602/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cas.go.jp/jp/seisaku/digital_gyozaikaikaku/kyotsuwt3/siryou9.pdf` -> **snapshot** (snapshot 20260208141523); points raw/verified 3/1
  - p49 Number of the 2025 Ministry of Internal Affairs and Communications ordinance ame = **22** ordinance number (2025-01-01..2025-12-31) [DISCARD: Count of ordinance amendments, not a migration quantity; irrelevant to the target.] quote: "(令和7年総務省令第22号。令和7年3月31日施行。)"
- dropped by code checks: 2 (number: more than one number in value_as_written: 2)

### d5 [related_series] Moving/relocation industry

Hypothesis: Aggregate moves correlate with moving-company transaction volumes and housing turnover; these can validate the level and direction of the August 2026 total if official statistics are unavailable. Target ≈ (moving-industry volume) × (share captured by inter-municipal registered moves).

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年 月別 転入 転出 件数; 引越し 件数 2026年8月 日本 引越しシーズン 需要; 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数 前年同月; 住民基本台帳人口移動報告 2026年7月結果 移動者 市区町村間 公表

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://datainsight.x.ezic.info/japan-residential-mobility-trend-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://home.osakagas.co.jp/column/moving/moving-costs/moving-cost-august/` -> **snapshot** (snapshot 20260107031259); points raw/verified 15/0
- dropped by code checks: 15 (period_end 2026-08-31 after as_of: 7; period year 2026 does not appear in the page text or URL (likely mis-dated): 8)

### b1 [own_history] d1

Hypothesis: August 2025 (and August 2024) all-person inter-municipal monthly totals from the same Statistics Bureau report would give the direct seasonal anchor for August 2026, replacing the need to infer August level from annual totals and October/July months. This is the single most valuable missing input.

Queries issued by the searcher: stat.go.jp 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 移動者数 前年同月; stat.go.jp idou rireki 2408 2024年8月結果 市区町村間移動者数 35万5918人; "住民基本台帳人口移動報告" 2026年7月結果 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2408/index.html` -> **snapshot** (snapshot 20251009225522); points raw/verified 15/15
  - p50 Total (all persons) inter-municipal movers, Japan, August 2024 = **355,918** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p51 Total (all persons) inter-municipal movers, year-on-year change, August 2024 vs  = **23,575** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p52 Total (all persons) inter-municipal movers, year-on-year percent change, August  = **6.2** % (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p53 Japanese movers inter-municipal movers, Japan, August 2024 = **313,909** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p54 Japanese movers inter-municipal movers, year-on-year change, August 2024 vs Augu = **22,692** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p55 Japanese movers inter-municipal movers, year-on-year percent change, August 2024 = **6.7** % (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p56 Foreign movers inter-municipal movers, Japan, August 2024 = **42,009** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p57 Foreign movers inter-municipal movers, year-on-year change, August 2024 vs Augus = **883** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p58 Foreign movers inter-municipal movers, year-on-year percent change, August 2024 = **2.1** % (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p59 Total (all persons) inter-prefectural movers, Japan, August 2024 = **161,982** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の都道府県間移動者数は16万1982人と、前年同月に比べ1万1981人(6.9%)減少。"
  - p60 Total (all persons) intra-prefectural movers, Japan, August 2024 = **193,936** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の都道府県内移動者数は19万3936人と、前年同月に比べ1万1594人(5.6%)減少。"
  - p61 Japanese movers inter-prefectural movers, Japan, August 2024 = **139,649** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は13万9649人と、前年同月に比べ1万1007人(7.3%)減少。"
  - p62 Japanese movers intra-prefectural movers, Japan, August 2024 = **174,260** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は17万4260人と、前年同月に比べ1万1685人 (6.3%)減少。"
  - p63 Foreign movers inter-prefectural movers, Japan, August 2024 = **22,333** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万2333人と、前年同月に比べ974人(4.2%)減少。"
  - p64 Foreign movers intra-prefectural movers, Japan, August 2024 = **19,676** persons (moves) (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は1万9676人と、前年同月に比べ91人(0.5%)増加。"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0

### b2 [related_series] d2

Hypothesis: Monthly foreign-resident inter-municipal mover counts for mid-2026 (June/July already partly known via p4) and the foreign share trend would let us scale the Japanese-only August anchor by the foreign share, which is rising ~3-13% YoY. Resolves the largest uncertainty in the combined total.

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年 外国人移動者 月次; stat.go.jp 人口移動報告 2026 6月 7月 外国人; 住民基本台帳人口移動報告 2026年7月結果 外国人移動者の市区町村間移動者数; 住民基本台帳人口移動報告 2026年1月結果 外国人移動者の市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2606/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p65 Foreign inter-municipal movers (市区町村間移動者数), Japan, October 2025 = **57,901** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "・市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p66 Foreign inter-municipal movers, Japan, October 2024 (same month prior year) = **51,419** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p67 Foreign inter-municipal movers year-on-year change, Japan, October 2025 vs Octob = **6,482** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p68 Foreign inter-municipal movers year-on-year rate of change, Japan, October 2025 = **12.6** percent (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p69 Total (all residents) inter-municipal movers, Japan, October 2025 = **379,751** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p70 Total (all residents) inter-municipal movers, Japan, October 2024 = **378,202** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p71 Japanese inter-municipal movers, Japan, October 2025 = **321,850** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p72 Japanese inter-municipal movers, Japan, October 2024 = **326,783** persons (moves) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p73 Japanese inter-municipal movers year-on-year rate of change, Japan, October 2025 = **-1.5** percent (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p74 Foreign inter-prefectural movers (都道府県間移動者数), Japan, October 2025 = **30,709** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数 168,057 167,107 950 0.6 137,348 140,545 -3,197 -2.3 30,709 26,562 4,147 15.6"
  - p75 Foreign intra-prefectural movers (都道府県内移動者数), Japan, October 2025 = **27,192** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数 211,694 211,095 599 0.3 184,502 186,238 -1,736 -0.9 27,192 24,857 2,335 9.4"
  - p76 Foreign intra-prefectural movers year-on-year rate of change, Japan, October 202 = **9.4** percent (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数 211,694 211,095 599 0.3 184,502 186,238 -1,736 -0.9 27,192 24,857 2,335 9.4"
  - p77 Foreign inter-prefectural movers year-on-year rate of change, Japan, October 202 = **15.6** percent (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数 168,057 167,107 950 0.6 137,348 140,545 -3,197 -2.3 30,709 26,562 4,147 15.6"
  - p78 Foreign inter-municipal movers, Tokyo metropolitan area (東京圏), October 2025 = **5,252** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 5,252 4,186 1,066 1,948 2,521 -573 2,468 2,216 252"
  - p79 Foreign inter-municipal movers, Nagoya metropolitan area (名古屋圏), October 2025 = **1,948** persons (moves) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 5,252 4,186 1,066 1,948 2,521 -573 2,468 2,216 252"
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2603/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] d3

Hypothesis: August monthly inter-municipal migration rate (moves per resident) from prior years, combined with 2026 population, would provide an independent structural check on the seasonal anchor and constrain the August seasonal multiplier.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 市区町村間移動 転入 転出; 人口移動報告 8月 移動率 都道府県間移動者数 2024年; 人口推計 2025年8月1日現在 総人口 概算値 1億2343万; 住民基本台帳人口移動報告 2023年8月 市区町村間移動者数 37万9493人

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/pdf/202508.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20240927_no1695.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p80 Japan annual inter-municipal (city/town/village-to-city/town/village) internal m = **5,190,548** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p81 Japan annual inter-municipal internal migration moves, 2024 (table 1) = **5,207,746** persons (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p82 Japan annual inter-municipal internal migration moves, 2023 (table 1) = **5,263,249** persons (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p83 Japan annual inter-municipal internal migration moves, 2022 (table 1) = **5,310,972** persons (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p84 Japan annual inter-municipal internal migration moves, 2021 (table 1) = **5,247,744** persons (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p85 Japan annual inter-municipal internal migration moves, 2020 (table 1) = **5,255,721** persons (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p86 Japan annual inter-municipal internal migration moves, 2019 (table 1) = **5,403,465** persons (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p87 Japan annual inter-municipal internal migration moves, 2018 (table 1) = **5,359,174** persons (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p88 Japan annual inter-municipal internal migration moves, 2017 (table 1) = **5,318,617** persons (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p89 Japan annual inter-municipal internal migration moves, 2016 (table 1) = **5,251,717** persons (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p90 Japan annual inter-municipal internal migration moves, 2015 (table 1) = **5,384,553** persons (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p91 Japan annual inter-municipal internal migration moves, year-on-year change rate, = **-0.3** percent (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p92 Japan annual inter-municipal internal migration moves, year-on-year change rate, = **-1.1** percent (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p93 Japan annual inter-municipal internal migration moves, year-on-year change rate, = **-0.9** percent (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p94 Japan annual inter-municipal internal migration moves, year-on-year change count = **-17,198** persons (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august migration japan', 'juumin kihon daicho']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] Same July 2026 Japanese-only release: level, absolute YoY change and percent change are internally consistent (335,854 down 9,318 = 2.7%). One measurement, not three independent ones.
- corroborating: ['p4', 'p5', 'p6'] Same July 2026 foreign-only release: 54,945 up 1,700 = 3.2%. One measurement.
- corroborating: ['p1', 'p4'] Japanese and foreign components of the same July 2026 report; sum to the all-person inter-municipal total for July 2026 (not directly given but implied by p7+p8).
- corroborating: ['p7', 'p8', 'p9', 'p10', 'p11', 'p12'] July 2026 breakdown by inter-/intra-prefectural and nationality; p9+p10=p1, p11+p12=p4, p7+p8 = all-person inter-municipal total. Consistent decomposition of the same release.
- corroborating: ['p13', 'p14', 'p15', 'p16'] Annual all-person inter-municipal series 2023-2024 with YoY rates; consistent with p21 (2025) and with p17+p18.
- corroborating: ['p17', 'p18', 'p23', 'p25'] p17/p23 and p18/p25 are duplicate copies of the same 2024 Japanese and foreign annual figures; keep one of each.
- corroborating: ['p21', 'p22', 'p24'] 2025 annual all-person total = Japanese + foreign (4,528,254 + 662,294 = 5,190,548). Consistent.
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p43', 'p44'] October 2025 monthly release: total 379,751 = Japanese 321,850 + foreign 57,901; YoY +0.4% total, +12.6% foreign. Internally consistent single release.
- corroborating: ['p41', 'p42', 'p45', 'p46', 'p47'] October 2025 inter-/intra-prefectural split and prefectural in/out totals; consistent with p35.
- corroborating: ['p13', 'p35'] Annual 2024 total (5,207,746) is consistent in magnitude with monthly October 2024 (378,202) times 12 plus seasonality; no conflict.
- corroborating: ['p1', 'p35'] July 2026 Japanese-only (335,854) vs October 2025 Japanese-only (321,850): July is a seasonal peak, consistent with modest YoY decline in Japanese movers.
- contextual: ['p49'] Ordinance amending Basic Resident Registration rules effective 2025-03-31; possible minor procedural effect on registration but no quantified migration impact. Context only.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p4'] Both are July 2026 preliminary figures from the same Statistics Bureau report and same release (2026-08-27); they are complementary components (Japanese + foreign) of the July 2026 all-person inter-mu
- corroborating: ['p7', 'p8'] July 2026 inter-prefectural and intra-prefectural totals are the two non-overlapping components of the all-person inter-municipal total; they should sum to the July 2026 all-person level. Same source/
- corroborating: ['p13', 'p17', 'p18'] 2024 annual all-person total equals Japanese-only plus foreign-only (p17 + p18). Same report, same vintage; internal consistency check, not independent evidence.
- corroborating: ['p21', 'p22', 'p24'] 2025 annual all-person total equals Japanese-only plus foreign-only. Same source and vintage as each other.
- corroborating: ['p13', 'p21', 'p80', 'p81'] p13 and p81 are the same 2024 annual total from different snapshots; p21 and p80 are the same 2025 annual total. Redundant copies, not independent measurements.
- corroborating: ['p50', 'p53', 'p56'] August 2024 all-person total equals Japanese-only plus foreign-only. This is the key seasonal anchor for August, from the same report but a different year than the July 2026 points.
- corroborating: ['p35', 'p37', 'p39'] October 2025 all-person total equals Japanese-only plus foreign-only; useful for the foreign share trend and for validating the Japanese/foreign decomposition, but October is not August.
- corroborating: ['p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73'] All from the same October 2025 release table; p65/p39 and p69/p35 are duplicate representations. They corroborate the foreign-share level (~15% of inter-municipal moves in October 2025) and the foreig
- corroborating: ['p18', 'p24', 'p19', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] Foreign-resident annual inter-municipal move series 2016-2025 shows a persistent upward trend with a dip in 2020-2021 (COVID) and strong growth since 2022. This supports a rising foreign component in 
- corroborating: ['p50', 'p51', 'p52'] August 2024 total and its YoY change/percent are internally consistent (355,918 vs prior August 379,493, -6.2%). Same release.
- corroborating: ['p53', 'p54', 'p55', 'p56', 'p57', 'p58'] August 2024 Japanese and foreign components with their YoY changes; internally consistent with p50.
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64'] August 2024 inter-/intra-prefectural breakdown by nationality; sums to p50 and p53/p56. Same release, not independent.
- conflicting: ['p1', 'p50'] Apparent tension: July 2026 combined level (~390,799) is above August 2024 (~355,918), but August is normally a peak moving month and 2024 August was unusually weak (-6.2% YoY). Not a true contradicti
- corroborating: ['p91', 'p92', 'p93', 'p94'] Annual YoY change rates and counts for 2023-2025 confirm a near-flat all-person total with modest decline (-0.3% in 2025), constraining the annual change factor a2.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 all-person inter-municipal moves relative to August 2024 | 1.03 | 0.97..1.1 | 0.7304..1.461 (widened) | ratio | m1 (m1), m2 (m2) | Annual all-person totals were near-flat (-1.1% 2024, -0.3% 2025) but the foreign component rose ~9.5% in 2025 and foreign movers are a growing share; combined with a modest Japanese decline this implies a small net upward drift of roughly 1-3% per year over two years. Range spans a flat-to-modestly- | Used to carry the August 2024 all-person level forward to August 2026. | Published 2026 monthly data showing a sharp (>5%) annual change in the all-person total. |
| a2 | August 2026 foreign share of all-person inter-municipal moves | 0.135 | 0.115..0.16 | 0.09592..0.1918 (widened) | ratio | unused | Foreign share was ~11.8% in August 2024 (42,009/355,918), ~15.2% in October 2025, and ~12.8% for 2025 annually; the share is trending up, so August 2026 should sit above the August 2024 value, near 13-14%. | Used to split the August 2026 all-person total into Japanese and foreign components for the sum method. | Published foreign share for mid-2026 outside 11.5-16%. |
| a3 | August 2026 combined total relative to July 2026 combined total | 1.02 | 0.9..1.15 | 0.7194..1.439 (widened) | ratio | unused | August 2024 (355,918) was below October 2025 (379,751) and the July 2026 combined level is ~390,799; August is not reliably a strong peak, so a near-unity ratio with wide range is appropriate rather than a large uplift. | Used to scale the July 2026 combined level to August 2026. | Published August/July ratios consistently outside 0.90-1.15 in prior years. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 367,713 | ['p50'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 367,713 | ['p50'] / ['a1'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of Japanese, foreign

Result: central **367,713** person, 80% interval [248,597, 543,903] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 367,713 person (80% model-based interval 248,597 to 543,903 person) for inter-municipal moves within Japan, Japanese and foreign residents combined, during August 2026, as would appear in the Statistics Bureau's Basic Resident Registration migration report.

The anchor is the observed August 2024 all-person total of 355,918 persons (moves). Both methods apply the same drift factor 1.03 (range 0.7304 to 1.461) to that anchor; the second expresses it as a Japanese-plus-foreign split as a structural cross-check. Because both share the same anchor and assumption, they are not independent, and the equal weights (50% and 50%) reflect that shared dependency rather than corroboration. No backtest error was available.

The main risk is the drift factor: if 2026 migration departs from the stable 2024-2025 trend, the estimate is off. The most useful missing evidence would be actual 2025 and early-2026 monthly totals, especially the foreign component, to calibrate the drift.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 all-person inter-municipal moves relative to August 2024: 1.03 ratio, range 0.7304 to 1.461 (range widened by code); used by m1, m2. Overturned by: Published 2026 monthly data showing a sharp (>[n]) annual change in the all-person total.

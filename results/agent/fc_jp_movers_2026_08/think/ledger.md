# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of persons recorded in the Basic Resident Registration as moving from one municipality to another within Japan during August 2026, Japanese and foreign residents combined, as the first preliminary monthly figure in the Statistics Bureau of Japan's Report on Internal Migration in Japan Derived | unit person | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan, Ministry of Internal Affairs and Communications

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau monthly-series analyst

Hypothesis: The August 2026 first-reported total is best anchored by earlier August totals and the 2026 January-July trajectory. If the level and seasonal pattern are stable, August 2026 can be expressed as August 2025 adjusted by recent year-over-year movement and known population or foreign-share changes. The role is to provide the base level and seasonal shape, not to assume exact repetition.

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年8月 移動者数; 住民基本台帳人口移動報告 2025年8月 移動者数 外国人; stat.go.jp 住民基本台帳人口移動報告 長期時系列 市区町村間移動者数 月次 表1; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 39万799人

- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/8
  - p1 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,207,746** persons (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p2 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,359,174** persons (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p3 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,403,465** persons (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p4 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,255,721** persons (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p5 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,247,744** persons (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p6 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,310,972** persons (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p7 Total internal migration (Japanese and foreign combined), inter-municipal movers = **5,263,249** persons (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p8 Foreign movers, inter-municipal movers, calendar year 2024, national = **604,591** persons (2024-01-01..2024-12-31) [DISCARD: The quoted table shows 662,294 as a total with 604,591 and 57,703 as its Japanese/foreign components, so 604,591 is not ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
- `https://tokyo.vivinavi.com/mc/desc/_wid_551f4899ba914fb4b0d0f60089453e9e1cf3082626/-/-/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (value_as_written not in quote as a whole number: 4; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d2 [related_series] Annual/monthly accounting analyst

Hypothesis: August 2026 can be derived from the 2026 year-to-date published total multiplied by a historical August-to-January-July seasonal ratio, or from the latest annual total multiplied by a historical August share. This provides an independent check on the direct history route and helps handle the fact that the monthly first report is preliminary.

Queries issued by the searcher: 住民基本台帳人口移動報告 2026年 1月 7月 累計 移動者数; 住民基本台帳人口移動報告 年間 移動者数 2025; 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数 39万; 住民基本台帳人口移動報告 2026年 1月～7月 累計 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/10
  - p9 Annual total internal migration between municipalities (Japanese and foreign com = **5,207,746** persons (2024-01-01..2024-12-31) [DISCARD: Duplicate of p1 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p10 Annual total internal migration between municipalities (Japanese and foreign com = **5,263,249** persons (2023-01-01..2023-12-31) [DISCARD: Duplicate of p7 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p11 Annual total internal migration between municipalities (Japanese and foreign com = **5,310,972** persons (2022-01-01..2022-12-31) [DISCARD: Duplicate of p6 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p12 Annual total internal migration between municipalities (Japanese and foreign com = **5,247,744** persons (2021-01-01..2021-12-31) [DISCARD: Duplicate of p5 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p13 Annual total internal migration between municipalities (Japanese and foreign com = **5,255,721** persons (2020-01-01..2020-12-31) [DISCARD: Duplicate of p4 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p14 Annual total internal migration between municipalities (Japanese and foreign com = **5,403,465** persons (2019-01-01..2019-12-31) [DISCARD: Duplicate of p3 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p15 Annual total internal migration between municipalities (Japanese and foreign com = **5,359,174** persons (2018-01-01..2018-12-31) [DISCARD: Duplicate of p2 annual total; no additional information.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p16 Annual total internal migration between municipalities (Japanese and foreign com = **5,318,617** persons (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p17 Annual total internal migration between municipalities (Japanese and foreign com = **5,251,717** persons (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p18 Annual total internal migration between municipalities (Japanese and foreign com = **5,384,553** persons (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 13/13
  - p19 Total internal migrants (all residents, Japanese and foreign) between municipali = **356,713** persons (2026-02-01..2026-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p20 Total internal migrants (all residents) between municipalities, February 2026, y = **343** persons (2026-02-01..2026-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p21 Total internal migrants (all residents) between municipalities, February 2026, y = **0.1** % (2026-02-01..2026-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p22 Japanese-resident migrants between municipalities, February 2026 = **309,774** persons (2026-02-01..2026-02-28) [keep: ] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p23 Foreign-resident migrants between municipalities, February 2026 = **46,939** persons (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p24 Foreign-resident migrants between municipalities, February 2026, year-on-year ch = **4,280** persons (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p25 Foreign-resident migrants between municipalities, February 2026, year-on-year pe = **10** % (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p26 Total internal migrants (all residents) between prefectures, February 2026 = **163,993** persons (2026-02-01..2026-02-28) [keep: ] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p27 Total internal migrants (all residents) within prefectures, February 2026 = **192,720** persons (2026-02-01..2026-02-28) [keep: ] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p28 Japanese-resident migrants between prefectures, February 2026 = **137,548** persons (2026-02-01..2026-02-28) [keep: ] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p29 Japanese-resident migrants within prefectures, February 2026 = **172,226** persons (2026-02-01..2026-02-28) [keep: ] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p30 Foreign-resident migrants between prefectures, February 2026 = **26,445** persons (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p31 Foreign-resident migrants within prefectures, February 2026 = **20,494** persons (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
- `https://www.stat.go.jp/info/mail/pdf/20260227_no1840.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d3 [base_rates] Demographer using population exposure

Hypothesis: The number of movers equals the resident population exposed to moving multiplied by an August monthly mover rate. Historical mover rates and foreign-resident shares can supply an independent baseline and constrain the plausible range, provided the population denominator and coverage are aligned with the migration series.

Queries issued by the searcher: 住民基本台帳 人口 2026年 総人口 外国人; 人口移動報告 2025年8月 移動者数 総務省統計局; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 人口推計 2026年8月1日現在 総人口 総務省統計局

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.soumu.go.jp/main_content/001083785.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/japan-data/h02859/` -> **snapshot** (snapshot 20260730040750); points raw/verified 15/13
  - p32 Total population in Basic Resident Registration, all residents, Japan, as of 202 = **123,767,642** persons (2026-01-01..2026-01-01) [keep: ] quote: "全国の人口は前年比0.45%減の1億2376万7642人だった。"
  - p33 Japanese resident population in Basic Resident Registration, Japan, as of 2026-0 = **119,736,483** persons (2026-01-01..2026-01-01) [keep: ] quote: "日本人は前年比91万6774人(0.76%)減少して1億1973万6483人。"
  - p34 Foreign resident population in Basic Resident Registration, Japan, as of 2026-01 = **4,031,159** persons (2026-01-01..2026-01-01) [keep: ] quote: "35万3696人(9.62%)増の403万1159人となった。"
  - p35 Year-on-year change in total population, Japan, 2026-01-01 vs 2025-01-01 = **0.45** % (2025-01-01..2026-01-01) [keep: ] quote: "全国の人口は前年比0.45%減の1億2376万7642人だった。"
  - p36 Year-on-year decrease in Japanese population, Japan, 2026-01-01 vs 2025-01-01 = **916,774** persons (2025-01-01..2026-01-01) [keep: ] quote: "日本人は前年比91万6774人(0.76%)減少して1億1973万6483人。"
  - p37 Year-on-year decrease rate of Japanese population, Japan, 2026-01-01 vs 2025-01- = **0.76** % (2025-01-01..2026-01-01) [keep: ] quote: "日本人は前年比91万6774人(0.76%)減少して1億1973万6483人。"
  - p38 Year-on-year increase in foreign resident population, Japan, 2026-01-01 vs 2025- = **353,696** persons (2025-01-01..2026-01-01) [keep: ] quote: "35万3696人(9.62%)増の403万1159人となった。"
  - p39 Year-on-year increase rate of foreign resident population, Japan, 2026-01-01 vs  = **9.62** % (2025-01-01..2026-01-01) [keep: ] quote: "35万3696人(9.62%)増の403万1159人となった。"
  - p40 Total population (including foreign residents) of Tokyo, as of 2026-01-01 = **14,077,553** persons (2026-01-01..2026-01-01) [DISCARD: Tokyo population is not needed for a national total and has no direct conversion to August movers.] quote: "最も人口(外国人も含めた総計)が多いのは、東京都の1407万7553人。"
  - p41 Total population (including foreign residents) of the three major metropolitan a = **65,979,272** persons (2026-01-01..2026-01-01) [DISCARD: Metropolitan-area population total is not needed for the national estimate.] quote: "東京、大阪、名古屋の三大都市圏全体の外国人も含めた人口は6597万9272人。"
  - p42 Share of national population living in the three major metropolitan areas, as of = **53.31** % (2026-01-01..2026-01-01) [DISCARD: Metropolitan population share is not a mover-count input.] quote: "なお全人口の53.31%が集中している。"
  - p43 Share of foreign residents living in the three major metropolitan areas, as of 2 = **68.65** % (2026-01-01..2026-01-01) [DISCARD: Foreign metropolitan concentration is not needed for the national mover total.] quote: "外国人住民は、大都市部への集中が一段と鮮明で、全体の68.65%が三大都市圏で暮らしている。"
  - p44 Foreign resident population of Tokyo, as of 2026-01-01 = **783,702** persons (2026-01-01..2026-01-01) [DISCARD: Tokyo foreign population is not needed for the national estimate.] quote: "\| 東京 \| 783,702 \|"
- dropped by code checks: 2 (period year 2024 does not appear in the page text or URL (likely mis-dated): 2)

### d4 [related_series] Foreign-resident mobility analyst

Hypothesis: The combined total equals Japanese movers plus foreign movers. Foreign residents have different age structure, mobility, and growth trends, so separating the two components reduces error versus applying one historical total trend. If no combined table exists, the components are the direct construction route.

Queries issued by the searcher: 住民基本台帳人口移動報告 外国人 移動者数 月別; 住民基本台帳人口移動報告 2026年 外国人 日本人 移動者数; stat.go.jp 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 外国人移動者; 住民基本台帳 人口 2026年1月1日 外国人 割合 総人口 統計局

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 15/12
  - p45 Japanese movers, inter-municipal moves within Japan, February 2026 = **309,774** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p46 Foreign movers, inter-municipal moves within Japan, February 2026 = **46,939** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p47 Total movers, inter-prefectural moves within Japan, February 2026 = **163,993** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p48 Japanese movers, inter-prefectural moves within Japan, February 2026 = **137,548** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p49 Foreign movers, inter-prefectural moves within Japan, February 2026 = **26,445** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p50 Total movers, intra-prefectural moves within Japan, February 2026 = **192,720** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p51 Japanese movers, intra-prefectural moves within Japan, February 2026 = **172,226** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p52 Foreign movers, intra-prefectural moves within Japan, February 2026 = **20,494** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
  - p53 Year-on-year change in Japanese inter-municipal movers, February 2026 = **4,623** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p54 Year-on-year change in foreign inter-municipal movers, February 2026 = **4,280** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p55 Year-on-year percent change in foreign inter-municipal movers, February 2026 = **10** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p56 Year-on-year percent change in Japanese inter-municipal movers, February 2026 = **1.5** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.e-stat.go.jp/index.php/stat-search/database?iroha=18&toukei=00200523&tstat=000000070001&cycle=1&tclass1=000001008739&layout=datalist&page=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search/files?layout=datalist&cycle=1&toukei=00200523&tstat=000000070001&tclass1=000001008739&tclass2val=0&year` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d5 [administrative] Municipal resident-registration operations

Hypothesis: National August movers can be scaled from move-in and move-out notification counts in large municipalities if those municipalities' share of national internal migration is stable. Administrative notification counts may differ in timing from the national report, but they provide a partial real-time signal for August 2026.

Queries issued by the searcher: 転入届 転出届 件数 2026年8月 区; 東京都 人口移動 2026年8月 転入 転出; 住民基本台帳人口移動報告 2026年7月結果 移動者数 市区町村間; 東京都 人口の動き 2026年7月 転入 転出 推計 総務局

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 13/13
  - p57 Total movers (all residents) between municipalities within Japan, February 2026 = **356,713** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p58 Total movers (all residents) between prefectures within Japan, February 2026 = **163,993** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p59 Total movers (all residents) within prefectures, February 2026 = **192,720** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p60 Japanese movers between municipalities, February 2026 = **309,774** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p61 Japanese movers between prefectures, February 2026 = **137,548** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p62 Japanese movers within prefectures, February 2026 = **172,226** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p63 Foreign movers between municipalities, February 2026 = **46,939** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p64 Foreign movers between prefectures, February 2026 = **26,445** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p65 Foreign movers within prefectures, February 2026 = **20,494** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
  - p66 Year-on-year change in total municipal-to-municipal movers, February 2026 = **343** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p67 Year-on-year percent change in total municipal-to-municipal movers, February 202 = **0.1** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p68 Year-on-year percent change in foreign municipal-to-municipal movers, February 2 = **10** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p69 Year-on-year percent change in Japanese municipal-to-municipal movers, February  = **1.5** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
- `https://kankeijinko.jp/data/prefecture/tokyo/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/en/stat-search/files?page=1&layout=dataset&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%20%E4%BA%BA%E5%8F%A3&stat_infid=000040476900` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/en/stat-search?layout=dataset&page=1&query=%E5%A4%96%E5%9B%BD` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [physical_flow] Moving-services and utility operations analyst

Hypothesis: Household moving activity, such as moving-company jobs, truck rentals, or utility transfer requests, correlates with resident-registration inter-municipal moves. A household-move count can be converted to persons using average household size, but the route is only a directional constraint because not all moves use commercial services and registration timing may lag.

Queries issued by the searcher: 引越し 件数 月別 2026年8月 引越し会社 需要; 電力 ガス 使用開始 停止 件数 8月 引越し 統計; 住民基本台帳人口移動報告 2026年8月 速報 転入 転出 件数; 引越し 市場規模 統計 月別 件数 全国 引越専門協同組合

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 14/14
  - p70 Total inter-municipal movers (Japanese and foreign combined), February 2026, nat = **356,713** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p71 Year-on-year change in total inter-municipal movers, February 2026, national = **343** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p72 Year-on-year percent change in total inter-municipal movers, February 2026, nati = **0.1** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p73 Japanese inter-municipal movers, February 2026, national = **309,774** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p74 Year-on-year change in Japanese inter-municipal movers, February 2026, national = **4,623** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p75 Foreign inter-municipal movers, February 2026, national = **46,939** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p76 Year-on-year change in foreign inter-municipal movers, February 2026, national = **4,280** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p77 Year-on-year percent change in foreign inter-municipal movers, February 2026, na = **10** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p78 Total inter-prefectural movers (Japanese and foreign combined), February 2026, n = **163,993** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p79 Total intra-prefectural movers (Japanese and foreign combined), February 2026, n = **192,720** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p80 Japanese inter-prefectural movers, February 2026, national = **137,548** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p81 Japanese intra-prefectural movers, February 2026, national = **172,226** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p82 Foreign inter-prefectural movers, February 2026, national = **26,445** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p83 Foreign intra-prefectural movers, February 2026, national = **20,494** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
- `https://kankeijinko.jp/2026/08/29/1292/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search?iroha=18&layout=dataset&page=1&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecitizen.jp/statdb/StatsData/0003420473` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] Calendar and disruption analyst

Hypothesis: August 2026 mover counts may deviate from the historical seasonal norm because of Obon timing, heat, typhoons, disasters, holidays, or policy changes affecting resident registration. Measurable exposure to these shocks can adjust the seasonal factor derived from own history.

Queries issued by the searcher: 2026年8月 台風 災害 住民票 転入 転出; 住民基本台帳移動報告 2026年8月 転入 転出 速報; 2026年 お盆 日程 8月13日 16日; 住民基本台帳 制度 変更 2026 転入届

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 15/15
  - p84 Total movers (all residents) inter-municipal within Japan, February 2026 = **356,713** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p85 Year-on-year change in total inter-municipal movers, February 2026 = **343** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p86 Year-on-year percent change in total inter-municipal movers, February 2026 = **0.1** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p87 Japanese movers inter-municipal within Japan, February 2026 = **309,774** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p88 Year-on-year change in Japanese inter-municipal movers, February 2026 = **4,623** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p89 Year-on-year percent change in Japanese inter-municipal movers, February 2026 = **1.5** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p90 Foreign movers inter-municipal within Japan, February 2026 = **46,939** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p91 Year-on-year change in foreign inter-municipal movers, February 2026 = **4,280** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p92 Year-on-year percent change in foreign inter-municipal movers, February 2026 = **10** % (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p93 Total movers inter-prefectural within Japan, February 2026 = **163,993** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p94 Total movers intra-prefectural within Japan, February 2026 = **192,720** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p95 Japanese movers inter-prefectural within Japan, February 2026 = **137,548** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p96 Japanese movers intra-prefectural within Japan, February 2026 = **172,226** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p97 Foreign movers inter-prefectural within Japan, February 2026 = **26,445** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p98 Foreign movers intra-prefectural within Japan, February 2026 = **20,494** persons (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 monthly figures already in p19-p31.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
- `https://www.c-nexco.co.jp/corporate/pressroom/news_release/6632.html` -> **snapshot** (snapshot 20260811150056); points raw/verified 12/12
  - p99 Obon period length in days (NEXCO forecast period, Kanto-Koshin/Shizuoka express = **10** days (2026-08-07..2026-08-16) [keep: ] quote: "お盆期間[令和8年8月7日(金)~8月16日(日)の10日間]"
  - p100 Obon period start date (Reiwa 8 / 2026) = **7** as written "8月7日", value check pending day of month (2026-08-07..2026-08-07) [DISCARD: Redundant start date already covered by p99.] quote: "令和8年8月7日(金)~8月16日(日)の10日間"
  - p101 Obon period end date (Reiwa 8 / 2026) = **16** as written "8月16日", value check pending day of month (2026-08-16..2026-08-16) [DISCARD: Redundant end date already covered by p99.] quote: "令和8年8月7日(金)~8月16日(日)の10日間"
  - p102 General Obon entry (盆入り) date in 2026 = **13** day of month (2026-08-13..2026-08-13) [DISCARD: Redundant Obon core date already covered by p111.] quote: "一般的な盆入りの13日が木曜、16日が日曜"
  - p103 Mountain Day (山の日) public holiday date in 2026 = **11** as written "8月11日", value check pending day of month (2026-08-11..2026-08-11) [keep: ] quote: "8月11日の山の日が飛び石の祝日であること"
  - p104 Maximum predicted traffic congestion length, Obon 2026, Kanto-Koshin/Shizuoka ex = **45** km (2026-08-07..2026-08-16) [DISCARD: Traffic congestion length is not convertible to resident-registration movers.] quote: "最大45kmの渋滞を予測しています"
  - p105 Threshold for counted long congestion (10km or more), Obon 2026 forecast = **10** km (2026-08-07..2026-08-16) [DISCARD: Congestion threshold is not a mover-count input.] quote: "10km以上の交通集中渋滞をお知らせします"
  - p106 Threshold for especially long congestion (35km or more), Obon 2026 forecast = **35** km (2026-08-07..2026-08-16) [DISCARD: Congestion threshold is not a mover-count input.] quote: "特に長い渋滞(35km以上)の予測"
  - p107 Increase in number of 10km+ congestion occurrences, Obon 2026 forecast vs prior- = **35** occurrences (2026-08-07..2026-08-16) [DISCARD: Congestion occurrence change is not convertible to mover counts.] quote: "今年の10km以上の渋滞回数は昨年実績と比較して35回増加する見込みです"
  - p108 Prior-year (Reiwa 7) Obon comparison period length in days = **10** days (2025-08-08..2025-08-17) [DISCARD: Prior-year comparison period length is not a mover-count input.] quote: "令和7年実績は、令和7年8月8日(金)~令和7年8月17日(日)の10日間を集計"
  - p109 Prior-year (Reiwa 7) Obon comparison period start date = **8** as written "8月8日", value check pending day of month (2025-08-08..2025-08-08) [DISCARD: Prior-year comparison start date is not a mover-count input.] quote: "令和7年8月8日(金)~令和7年8月17日(日)の10日間"
  - p110 Prior-year (Reiwa 7) Obon comparison period end date = **17** as written "8月17日", value check pending day of month (2025-08-17..2025-08-17) [DISCARD: Prior-year comparison end date is not a mover-count input.] quote: "令和7年8月8日(金)~令和7年8月17日(日)の10日間"
- `https://rurubu.jp/andmore/article/25189` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tripre.jp/archives/41619` -> **snapshot** (snapshot 20260809051102); points raw/verified 15/14
  - p111 Obon holiday period days in 2026 (conventional Obon, 4 days) = **4** days (2026-08-13..2026-08-16) [keep: ] quote: "一般的に「お盆」とされるのは、8月13日~8月16日の4日間。"
  - p112 Start date of 2026 Obon holiday travel activity (around Aug 7) = **7** as written "8月7日", value check pending day of month (2026-08-07..2026-08-07) [DISCARD: Redundant Obon activity start context already covered by p99.] quote: "2026年のお盆休みは8月7日(金)頃から、行楽地や帰省先との往来が活発化するとみられています。"
  - p113 NEXCO East forecast count of 10km+ traffic jams, 2026 Obon 10-day period = **133** occurrences (2026-08-07..2026-08-16) [DISCARD: Traffic jam forecast count is not convertible to resident-registration movers.] quote: "2026年8月7日(金)~8月16日(日)の10日間、管内の高速道路で10km以上の渋滞が133回発生すると予測しています。"
  - p114 Length of 2026 Obon forecast period (days) = **10** days (2026-08-07..2026-08-16) [DISCARD: Forecast period length is not a mover-count input.] quote: "2026年8月7日(金)~8月16日(日)の10日間、管内の高速道路で10km以上の渋滞が133回発生すると予測しています。"
  - p115 Maximum forecast traffic jam length, Tohoku Expressway downbound Nasushiobara-Sh = **35** km (2026-08-13..2026-08-13) [DISCARD: Specific traffic jam length is not convertible to mover counts.] quote: "下りでは8月13日(木)11:00をピークに東北自動車道の西那須野塩原IC(栃木県那須塩原市)-鹿沼IC(栃木県鹿沼市)間で最大35kmの渋滞が予測されています。"
  - p116 Maximum forecast traffic jam length, Kanetsu Expressway upbound Tsurugashima IC  = **40** km (2026-08-15..2026-08-15) [DISCARD: Specific traffic jam length is not convertible to mover counts.] quote: "上りでは、8月15日(土)18:00をピークに関越自動車道の鶴ヶ島IC(埼玉県鶴ヶ島市)-藤岡JCT(群馬県藤岡市)間で最大40km。"
  - p117 Maximum forecast traffic jam length, Tohoku Expressway upbound ending at Tochigi = **35** km (2026-08-15..2026-08-15) [DISCARD: Specific traffic jam length is not convertible to mover counts.] quote: "この日には東北自動車道の栃木IC(栃木県栃木市)を末尾とする最大35kmの渋滞も発生するとみられています。"
  - p118 Mountain Day public holiday date in 2026 = **11** as written "8月11日", value check pending day of month (2026-08-11..2026-08-11) [DISCARD: Duplicate Mountain Day date already captured by p103.] quote: "一方で、8月11日(火)に祝日の「山の日」があることで、8月8日(土)からお盆休みに入るという人も多そうです。"
  - p119 Maximum consecutive holiday days possible in 2026 Obon season if weekdays taken  = **9** consecutive days (2026-08-08..2026-08-16) [keep: ] quote: "間にある8月10日(月)、8月12日(水)の平日を休めば、9連休にまで拡大します。"
  - p120 Forecast peak downbound traffic jam length, Tohoku Expressway Kanuma IC to Nasus = **30** km (2026-08-12..2026-08-12) [DISCARD: Specific traffic jam forecast is not convertible to mover counts.] quote: "\| 下り \| 8/12(水) \| 鹿沼IC → 西那須野塩原IC \| 30km \| 9時~17時 \| 12時 \|"
  - p121 Forecast peak traffic jam length, Kanetsu Expressway downbound Oizumi JCT to Hig = **30** km (2026-08-13..2026-08-13) [DISCARD: Specific traffic jam forecast is not convertible to mover counts.] quote: "\| 下り \| 8/13(木) \| 大泉JCT → 東松山IC \| 30km \| 6時~14時 \| 9時 \|"
  - p122 Forecast peak traffic jam length, Kanetsu Expressway upbound Honjo-Kodama IC to  = **35** km (2026-08-14..2026-08-14) [DISCARD: Specific traffic jam forecast is not convertible to mover counts.] quote: "\| 上り \| 8/14(金) \| 本庄児玉IC → 鶴ヶ島IC \| 35km \| 14時~23時 \| 17時 \|"
  - p123 Forecast peak traffic jam length, Joban Expressway upbound Kita-Ibaraki IC to Hi = **25** km (2026-08-15..2026-08-15) [DISCARD: Specific traffic jam forecast is not convertible to mover counts.] quote: "\| 上り \| 8/15(土) \| 北茨城IC → 日立南太田IC \| 25km \| 14時~21時 \| 17時 \|"
  - p124 Forecast peak traffic jam length, Tohoku Expressway upbound Tochigi IC to Kazo I = **30** km (2026-08-14..2026-08-14) [DISCARD: Specific traffic jam forecast is not convertible to mover counts.] quote: "\| 上り \| 8/14(金) \| 栃木IC → 加須IC \| 30km \| 15時~22時 \| 18時 \|"
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b1 [own_history] d1

Hypothesis: Historical August first-reported monthly inter-municipal mover totals for 2019-2025 would replace the seasonal-share and August-to-February assumptions a1/a3 with observed August seasonality, directly anchoring m1 and m2 and reducing the largest uncertainty.

Queries issued by the searcher: 住民基本台帳人口移動報告 市区町村間移動者数 2025年8月; Statistics Bureau Report on Internal Migration in Japan August 2025 inter-municipal movers total; stat.go.jp 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2019年8月 市区町村間移動者数 日本人移動者

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **snapshot** (snapshot 20251118092550); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/rireki/2408/index.html` -> **snapshot** (snapshot 20251009225522); points raw/verified 15/15
  - p125 All residents (Japanese and foreign combined) inter-municipal movers, nationwide = **355,918** persons (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p126 All residents inter-municipal movers, year-on-year change, August 2024 = **23,575** persons (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p127 All residents inter-municipal movers, year-on-year percent change, August 2024 = **6.2** % (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p128 Japanese residents inter-municipal movers, nationwide, August 2024 = **313,909** persons (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p129 Japanese residents inter-municipal movers, year-on-year change, August 2024 = **22,692** persons (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p130 Japanese residents inter-municipal movers, year-on-year percent change, August 2 = **6.7** % (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p131 Foreign residents inter-municipal movers, nationwide, August 2024 = **42,009** persons (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p132 Foreign residents inter-municipal movers, year-on-year change, August 2024 = **883** persons (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p133 Foreign residents inter-municipal movers, year-on-year percent change, August 20 = **2.1** % (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p134 All residents inter-prefectural movers, nationwide, August 2024 = **161,982** persons (2024-08-01..2024-08-31) [keep: ] quote: "移動者の都道府県間移動者数は16万1982人と、前年同月に比べ1万1981人(6.9%)減少。"
  - p135 All residents intra-prefectural movers, nationwide, August 2024 = **193,936** persons (2024-08-01..2024-08-31) [keep: ] quote: "移動者の都道府県内移動者数は19万3936人と、前年同月に比べ1万1594人(5.6%)減少。"
  - p136 Japanese residents inter-prefectural movers, nationwide, August 2024 = **139,649** persons (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は13万9649人と、前年同月に比べ1万1007人(7.3%)減少。"
  - p137 Japanese residents intra-prefectural movers, nationwide, August 2024 = **174,260** persons (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は17万4260人と、前年同月に比べ1万1685人 (6.3%)減少。"
  - p138 Foreign residents inter-prefectural movers, nationwide, August 2024 = **22,333** persons (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万2333人と、前年同月に比べ974人(4.2%)減少。"
  - p139 Foreign residents intra-prefectural movers, nationwide, August 2024 = **19,676** persons (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は1万9676人と、前年同月に比べ91人(0.5%)増加。"
- `https://www.e-stat.go.jp/en/stat-search/files?iroha=26&layout=dataset&stat_infid=000040322123` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] d2

Hypothesis: 2026 January-July monthly first-reported totals would establish the 2026 level and the Japanese/foreign trend, allowing the 2024-to-2026 factor a2 and component rates to be updated from actual 2026 data rather than 2024 and February-only anchors.

Queries issued by the searcher: Statistics Bureau Report on Internal Migration in Japan Derived 2026 monthly; 住民基本台帳人口移動報告 2026年 1月 転入 転出; stat.go.jp/data/idou/rireki/2607 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数 日本人移動者 外国人移動者

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 15/15
  - p140 Total inter-municipal movers (all residents, Japanese and foreign combined), Feb = **356,713** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p19 from the same February 2026 release; same value and role.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p141 Year-on-year change in total inter-municipal movers, February 2026 = **343** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p20 from the same February 2026 release.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p142 Year-on-year percent change in total inter-municipal movers, February 2026 = **0.1** % (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p21 from the same February 2026 release.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p143 Japanese inter-municipal movers, February 2026 = **309,774** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p22 from the same February 2026 release.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p144 Year-on-year change in Japanese inter-municipal movers, February 2026 = **4,623** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p24 from the same February 2026 release.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p145 Year-on-year percent change in Japanese inter-municipal movers, February 2026 = **1.5** % (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p22/p25 wording from the same February 2026 release.] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p146 Foreign inter-municipal movers, February 2026 = **46,939** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p23 from the same February 2026 release.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p147 Year-on-year change in foreign inter-municipal movers, February 2026 = **4,280** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p24 from the same February 2026 release.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p148 Year-on-year percent change in foreign inter-municipal movers, February 2026 = **10** % (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p25 from the same February 2026 release.] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p149 Total inter-prefectural movers (all residents), February 2026 = **163,993** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p26 from the same February 2026 release.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p150 Total intra-prefectural movers (all residents), February 2026 = **192,720** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p27 from the same February 2026 release.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p151 Japanese inter-prefectural movers, February 2026 = **137,548** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p28 from the same February 2026 release.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p152 Japanese intra-prefectural movers, February 2026 = **172,226** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p29 from the same February 2026 release.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p153 Foreign inter-prefectural movers, February 2026 = **26,445** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p30 from the same February 2026 release.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p154 Foreign intra-prefectural movers, February 2026 = **20,494** persons (2026-02-01..2026-02-28) [DISCARD: Redundant duplicate of p31 from the same February 2026 release.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2604/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 14/14
  - p155 Inter-municipal movers, all residents combined, Japan, October 2025 (first-repor = **379,751** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p156 Inter-municipal movers, all residents combined, Japan, October 2024 (comparison  = **378,202** persons (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p157 Inter-municipal movers, Japanese residents, Japan, October 2025 = **321,850** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p158 Inter-municipal movers, Japanese residents, Japan, October 2024 = **326,783** persons (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p159 Inter-municipal movers, foreign residents, Japan, October 2025 = **57,901** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p160 Inter-municipal movers, foreign residents, Japan, October 2024 = **51,419** persons (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p161 Inter-municipal movers, all residents combined, Japan, October 2025 year-on-year = **1,549** persons (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p162 Inter-municipal movers, all residents combined, Japan, October 2025 year-on-year = **0.4** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p163 Inter-municipal movers, Japanese residents, Japan, October 2025 year-on-year cha = **1.5** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p164 Inter-municipal movers, foreign residents, Japan, October 2025 year-on-year chan = **12.6** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p165 Inter-prefectural movers, all residents combined, Japan, October 2025 = **168,057** persons (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p166 Intra-prefectural movers, all residents combined, Japan, October 2025 = **211,694** persons (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p167 Inter-prefectural movers, foreign residents, Japan, October 2025 = **307,090,000** as written "3万 709", value check pending persons (2025-10-01..2025-10-31) [DISCARD: Value is corrupted by a 10,000x multiplier/OCR error: 307,090,000 persons conflicts with the quoted 3万709人 and with p159] quote: "都道府県間移動者数は 3万 709人。前年同月に比べ増加 4147人( 15.6%)"
  - p168 Intra-prefectural movers, foreign residents, Japan, October 2025 = **27,192** persons (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 2万7192人。前年同月に比べ増加 2335人( 9.4%)"

### b3 [administrative] d5

Hypothesis: August 2026 move-in/move-out notification counts from large municipalities or a late-August real-time indicator would provide a partial signal for the August level/shock and help validate m2/m3, especially if Obon timing shifted moves.

Queries issued by the searcher: 東京都 人口の動き 2026年8月 住民基本台帳 転入 転出; 住民基本台帳人口移動報告 2026年8月 速報; 東京都の人口（推計） 令和8年8月1日現在 発表; 東京都 住民基本台帳人口移動報告 令和8年7月 転入超過

- `https://tokyo.vivinavi.com/mc/desc/_wid_551f4899ba914fb4b0d0f60089453e9e1cf3082626/-/-/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp-newsfocus.com/tag/%e4%ba%ba%e5%8f%a3%e7%a7%bb%e5%8b%95/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://catalog.data.metro.tokyo.lg.jp/organization/t000003?res_format=CSV&license_id=CC-BY-4.0&organization=t000003&_groups_limit=0&page=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.toukei.metro.tokyo.lg.jp/juukiy/jy-index.htm` -> **snapshot** (snapshot 20260727064559); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p16', 'p17', 'p18'] Same Statistics Bureau annual series for inter-municipal movers, Japanese and foreign combined, covering 2015-2024. These are a consistent historical level/trend but not independent yearly observation
- related: ['p1', 'p8'] p1 is the combined annual total and p8 is the foreign component from the same source/definition. p1-p8 implies the Japanese component, but this is an internal decomposition, not independent confirmati
- corroborating: ['p19', 'p22', 'p23', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31'] February 2026 monthly report: p19 equals p22+p23 and p26+p27; p22 equals p28+p29; p23 equals p30+p31. Exact internal arithmetic consistency, but all from one release, so not independent evidence. p20/
- corroborating: ['p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39'] Basic Resident Registration population as of 2026-01-01: p32=p33+p34; p35-p39 describe the same population change. Same administrative source, useful as denominator and foreign-share context.
- duplicate: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98'] These repeat the February 2026 monthly figures already captured by p19-p31. They come from parallel d4-d7 extracts and add no measurement information.
- context: ['p99', 'p103', 'p111', 'p119'] Obon/Mountain Day timing in 2026: a 10-day Obon traffic period Aug 7-16, Mountain Day Aug 11, conventional Obon Aug 13-16, and possibility of a 9-day holiday. This informs August seasonality but is no
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p16', 'p17', 'p18'] Annual inter-municipal totals from the same Statistics Bureau series; consistent level around 5.19–5.40 million and mild recent decline. Shared source/vintage, so not independent confirmation.
- corroborating: ['p125', 'p128', 'p131', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139'] August 2024 monthly release; internal arithmetic identities hold: p128+p131=p125, p134+p135=p125, p136+p137=p128, p138+p139=p131. Same underlying measurement, not independent.
- corroborating: ['p19', 'p22', 'p23', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31'] February 2026 monthly release; p22+p23=p19, p28+p30=p26, p29+p31=p27. Same source and release, so consistent but not independent.
- redundant: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154'] p140–p154 duplicate the February 2026 values already given by p19–p31; keeping both would double-count the same release.
- corroborating: ['p155', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166', 'p168'] October 2025/2024 release; p157+p159=p155, p158+p160=p156, and year-on-year changes match the levels. October is seasonally higher than August/February, so it informs trend but not direct August level
- conflicting: ['p167', 'p159', 'p168'] p167 carries 307,090,000 persons, a 10,000x multiplier/OCR corruption; the quote says 3万709人 (~30,709), and p159 minus p168 implies about that foreign inter-prefectural value. p167 is unusable as stat
- corroborating: ['p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39'] Population components sum correctly: p33+p34=p32; Japanese decline and foreign growth are internally consistent. Same Basic Resident Registration population source, useful for rates but a different co
- contextual: ['p99', 'p103', 'p111', 'p119'] Obon 2026 timing is consistent: extended holiday window around Aug 7–16, Mountain Day Aug 11, conventional Obon Aug 13–16, possible 9-day break. Provides shock context only, not a mover count.
- related: ['p125', 'p155', 'p19'] Monthly totals at different seasons: August 2024 355,918, February 2026 356,713, October 2025 379,751. Same scale, with October seasonally higher; not independent and not a direct seasonal match.
- related: ['p128', 'p131', 'p22', 'p23'] August 2024 and February 2026 components show Japanese movers roughly flat/slightly down and foreign movers rising. Different months/years, so usable only with trend and seasonal conversion assumption

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2024-to-August 2026 change factor for all-resident inter-municipal movers | 1 | 0.95..1.05 | 0.8933..1.117 (widened) | factor | m1 (m1) | Recent annual totals (p1–p7) show only mild decline, and February 2026 total movers were nearly flat year-on-year (p19 with p21). Foreign growth should offset Japanese decline, so a two-year August factor near 1.0 is defensible with a wide range for trend and shock uncertainty. | p125 August 2024 is a valid seasonal anchor and no large August 2026 registration/disaster shock occurs. | Published August 2025/2026 data showing a change materially outside ±5%, or evidence of a major registration-timing shift. |
| a2 | Japanese August 2024-to-August 2026 change factor | 0.97 | 0.93..1 | 0.8626..1.078 (widened) | factor | m2 (m2) | Japanese population fell 0.76% year-on-year (p37), Japanese February 2026 inter-municipal movers were down 1.5% (p22), and annual totals show mild decline. Two years of Japanese mobility decline point to a factor slightly below 1.0. | The recent Japanese mobility decline continues through August 2026. | Evidence that Japanese inter-municipal movers rebounded or fell much faster than the recent trend. |
| a3 | Foreign August 2024-to-August 2026 change factor | 1.18 | 1.1..1.28 | 1.061..1.327 (widened) | factor | m2 (m2) | Foreign movers were up 10.0% year-on-year in February 2026 (p23/p25) and 12.6% in October 2025 (p159/p164); foreign resident population rose 9.62% (p39). A two-year factor around 1.18 incorporates strong but possibly slowing foreign mobility growth. | Foreign resident mobility continues to grow at roughly the recent pace through August 2026. | A sharp slowdown or reversal in foreign mover counts or foreign resident growth. |
| a4 | Japanese August 2026-to-February 2026 ratio of monthly inter-municipal movers | 0.98 | 0.94..1.02 | 0.6924..1.385 (widened) | ratio | m3 (m3) | p128 August 2024 Japanese movers is close to p22 February 2026 Japanese movers after allowing for Japanese decline; this implies August is seasonally near or slightly below February for Japanese movers. The total August/February comparison from p125 and p19 is also near parity. | The Japanese monthly seasonal pattern in 2026 resembles the limited observed August/February evidence. | A large August 2026 Japanese seasonal deviation or a revised February 2026 base outside the range. |
| a5 | Foreign August 2026-to-February 2026 ratio of monthly inter-municipal movers | 1.08 | 1..1.16 | 0.7616..1.523 (widened) | ratio | m3 (m3) | p131 August 2024 foreign movers and p23 February 2026 foreign movers, adjusted for foreign growth, suggest August foreign movement is modestly above February. Foreign seasonality is less stable, so the range is wide. | Foreign movers show the usual August uplift relative to February in 2026. | Evidence of a flat or reversed foreign August/February seasonal pattern in 2026. |
| a6 | Total August 2026-to-February 2026 ratio of monthly inter-municipal movers | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m4 (m4) | p125 August 2024 total and p19 February 2026 total are nearly equal, and the recent total trend is near flat with foreign growth offsetting Japanese decline. This makes an August/February total ratio centered near 1.0 reasonable. | Total August/February seasonality is stable and February 2026 is a valid near-term base. | Published August or revised February data showing a large seasonal or level shift. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 355,293 | ['p125'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 353,599 | ['p128', 'p131'] / ['a2', 'a3'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 356,146 | ['p22', 'p23'] / ['a4', 'a5'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 358,300 | ['p19'] / ['a6'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over component of Japanese, Foreign
- m3 coverage: sum over component of Japanese, Foreign
- m4 coverage: the whole target

Result: central **355,831** person, 80% interval [240,336, 526,826] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate is 355,831 person (80% model-based interval 240,336 to 526,826 person) for persons recorded in the Basic Resident Registration as moving between municipalities within Japan during August 2026, Japanese and foreign residents combined, as the first preliminary monthly figure.

Four routes were averaged with equal weights of 25% each: 355,293, 353,599, 356,146, and 358,300 person. Observed anchors include August 2024 totals (355,918 persons), August 2024 Japanese and foreign components (313,909 persons; 42,009 persons), and February 2026 levels (309,774 persons; 46,939 persons; 356,713 persons). The transfers to August 2026 rest on assumptions a1–a6, including Japanese and foreign change factors and seasonal ratios.

The main risk is that these two-year factors and seasonal ratios are unobserved and could absorb trend or shocks poorly. The most useful missing evidence would be a published August 2025 figure to calibrate the August seasonal shape.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2024-to-August 2026 change factor for all-resident inter-municipal movers: 1 factor, range 0.8933 to 1.117 (range widened by code); used by m1. Overturned by: Published August 2025/2026 data showing a change materially outside ±[n], or evidence of a major registration-timing shift.
- a2 Japanese August 2024-to-August 2026 change factor: 0.97 factor, range 0.8626 to 1.078 (range widened by code); used by m2. Overturned by: Evidence that Japanese inter-municipal movers rebounded or fell much faster than the recent trend.
- a3 Foreign August 2024-to-August 2026 change factor: 1.18 factor, range 1.061 to 1.327 (range widened by code); used by m2. Overturned by: A sharp slowdown or reversal in foreign mover counts or foreign resident growth.
- a4 Japanese August 2026-to-February 2026 ratio of monthly inter-municipal movers: 0.98 ratio, range 0.6924 to 1.385 (range widened by code); used by m3. Overturned by: A large August 2026 Japanese seasonal deviation or a revised February 2026 base outside the range.
- a5 Foreign August 2026-to-February 2026 ratio of monthly inter-municipal movers: 1.08 ratio, range 0.7616 to 1.523 (range widened by code); used by m3. Overturned by: Evidence of a flat or reversed foreign August/February seasonal pattern in 2026.
- a6 Total August 2026-to-February 2026 ratio of monthly inter-municipal movers: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m4. Overturned by: Published August or revised February data showing a large seasonal or level shift.

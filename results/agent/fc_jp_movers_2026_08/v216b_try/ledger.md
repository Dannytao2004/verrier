# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of internal migration events (moves of individuals between municipalities) within Japan recorded in the Basic Resident Registration system and first published in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration, for th | unit person (moves) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan, Ministry of Internal Affairs and Communications

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau time series

Hypothesis: August internal migration counts follow a stable seasonal pattern; the August 2026 value can be projected from August values in 2023-2025 plus a trend adjustment. The relationship is direct: same definition, same month, same publisher.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 移動者数; Report on Internal Migration in Japan August 2025 total migrants Statistics Bureau; 住民基本台帳人口移動報告 2023年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月 移動者数; Report on Internal Migration in Japan August 2025 total migrants Statistics Bureau; 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万5918人; 統計メールニュース 2026年7月結果 住民基本台帳人口移動報告 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月 移動者数; Report on Internal Migration in Japan August 2025 total migrants Statistics Bureau; 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万5918人; 住民基本台帳人口移動報告 2023年8月結果 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/12
  - p1 Annual internal migration between municipalities, Japan, 2023 (persons) = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p2 Annual internal migration between municipalities, Japan, 2024 (persons) = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p3 Year-on-year change rate of internal migration between municipalities, Japan, 20 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p4 Annual internal migration between municipalities, Japan, 2022 (persons) = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p5 Annual internal migration between municipalities, Japan, 2021 (persons) = **5,247,744** person (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p6 Annual internal migration between municipalities, Japan, 2020 (persons) = **5,255,721** person (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p7 Annual internal migration between municipalities, Japan, 2019 (persons) = **5,403,465** person (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p8 Annual internal migration between municipalities, Japan, 2018 (persons) = **5,359,174** person (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p9 Annual internal migration between municipalities, Japan, 2017 (persons) = **5,318,617** person (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p10 Annual internal migration between municipalities, Japan, 2016 (persons) = **5,251,717** person (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p11 Annual internal migration between municipalities, Japan, 2015 (persons) = **5,384,553** person (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p12 Intra-prefectural migration, Japan, 2025 (persons) = **2,674,817** person (2025-01-01..2025-12-31) [DISCARD: Intra-prefectural 2025 total; redundant with p307/p391 and not needed for any route.] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kurashi-infra-hikaku.com/hikkoshi/ido/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/en/stat-search?page=1&iroha=30&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 15/15
  - p13 Japan total internal migration between municipalities (Japanese + foreign), 2025 = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p14 Japan total internal migration between municipalities, year-on-year change, 2025 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p15 Japan inter-prefectural migration count, 2025 annual = **2,515,731** person (moves) (2025-01-01..2025-12-31) [DISCARD: Inter-prefectural 2025; duplicate of p316/p390/p202.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p16 Japan inflows from abroad (transfers in from outside Japan), 2025 annual = **782,165** person (2025-01-01..2025-12-31) [DISCARD: Overseas inflow 2025; duplicate of p318/p151.] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p17 Japan outflows to abroad (transfers out of Japan), 2025 annual = **409,592** person (2025-01-01..2025-12-31) [DISCARD: Overseas outflow 2025; duplicate of p320/p152.] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p18 Japan national net social change (social increase), 2025 annual = **337,234** person (2025-01-01..2025-12-31) [DISCARD: Net social change 2025; duplicate of p313/p322.] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p19 Japan national net social change, year-on-year expansion, 2025 vs 2024 = **5,548** person (2025-01-01..2025-12-31) [DISCARD: Net social change yoy; duplicate of p323.] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p20 Tokyo metropolitan area net in-migration (all movers), 2025 annual = **123,534** person (2025-01-01..2025-12-31) [DISCARD: Tokyo-area net in-migration 2025; duplicate of p325.] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p21 Three major metropolitan areas combined net in-migration (all movers), 2025 annu = **119,581** person (2025-01-01..2025-12-31) [DISCARD: Three-metro net in-migration 2025; duplicate of p324.] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p22 Nagoya metropolitan area net out-migration (all movers), 2025 annual = **12,695** person (2025-01-01..2025-12-31) [DISCARD: Nagoya net out-migration 2025; not used in any route.] quote: "名古屋圏は1万2695人の転出超過、前年に比べ6161人の縮小"
  - p23 Osaka metropolitan area net in-migration (all movers), 2025 annual = **8,742** person (2025-01-01..2025-12-31) [DISCARD: Osaka net in-migration 2025; not used in any route.] quote: "大阪圏は8742人の転入超過、前年に比べ6063人の拡大"
  - p24 Three major metropolitan areas combined net in-migration (Japanese movers only), = **110,680** person (2025-01-01..2025-12-31) [DISCARD: Three-metro Japanese net in-migration 2025; duplicate of p326.] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p25 Tokyo metropolitan area net in-migration (Japanese movers only), 2025 annual = **112,738** person (2025-01-01..2025-12-31) [DISCARD: Tokyo-area Japanese net in-migration 2025; not used.] quote: "東京圏は11万2738人の転入超過、前年に比べ6599人の縮小。30年連続の転入超過"
  - p26 Three major metropolitan areas combined net in-migration (foreign movers only),  = **8,901** person (2025-01-01..2025-12-31) [DISCARD: Three-metro foreign net in-migration 2025; duplicate of p327.] quote: "3大都市圏全体(外国人移動者)では8901人の転入超過、前年に比べ529人の拡大"
  - p27 Tokyo metropolitan area net in-migration (foreign movers only), 2025 annual = **10,796** person (2025-01-01..2025-12-31) [DISCARD: Tokyo-area foreign net in-migration 2025; duplicate of p328.] quote: "東京圏は1万796人の転入超過、前年に比べ5710人の縮小"
- `https://tokyo.vivinavi.com/mc/prt/_wid_91687f5ce3056af43a43fba6f9ad8bd64ac4092426` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.toukei.metro.tokyo.lg.jp/jidou/2025/ji-point.pdf` -> **snapshot** (snapshot 20260718032106); points raw/verified 15/15
  - p28 Tokyo-to inter-municipal internal migration count, all persons (Japanese + forei = **1,317,064** person (2025-01-01..2025-12-31) [keep: ] quote: "令和7年における東京都の区市町村間移動者数は 1,317,064 人で、前年比 6,596 人(△0.5%)減"
  - p29 Tokyo-to inter-municipal internal migration count, Japanese persons, calendar ye = **1,116,080** person (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人の区市町村間移動者数は 1,116,080 人で、前年比 20,233 人(△1.8%)減"
  - p30 Tokyo-to inter-municipal internal migration count, foreign persons, calendar yea = **200,984** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人の区市町村間移動者数は 200,984 人で、前年比 13,637 人(7.3%)増"
  - p31 Year-on-year change in Tokyo-to inter-municipal internal migration count, all pe = **6,596** person (2025-01-01..2025-12-31) [DISCARD: Tokyo yoy change; duplicate of p187.] quote: "前年比 6,596 人(△0.5%)減"
  - p32 Year-on-year percent change in Tokyo-to inter-municipal internal migration count = **0.5** % (2025-01-01..2025-12-31) [DISCARD: Tokyo yoy percent; duplicate of p190.] quote: "前年比 6,596 人(△0.5%)減"
  - p33 Tokyo-to migration count between prefectures (other 道府県), all persons, calendar  = **838,467** person (2025-01-01..2025-12-31) [DISCARD: Tokyo inter-prefectural count; duplicate of p191.] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p34 Tokyo-to migration count within Tokyo (都内間), all persons, calendar year 2025 = **465,145** person (2025-01-01..2025-12-31) [DISCARD: Tokyo intra-Tokyo count; duplicate of p194.] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p35 Tokyo-to other migration count (previous address unknown), all persons, calendar = **13,452** person (2025-01-01..2025-12-31) [DISCARD: Tokyo other-migration count; duplicate of p197.] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p36 Tokyo-to in-migrants from other prefectures, all persons, calendar year 2025 = **451,843** person (2025-01-01..2025-12-31) [DISCARD: Tokyo in-migrants; not used.] quote: "転入者数は 451,843 人"
  - p37 Tokyo-to out-migrants to other prefectures, all persons, calendar year 2025 = **386,624** person (2025-01-01..2025-12-31) [DISCARD: Tokyo out-migrants; not used.] quote: "転出者数は 386,624 人"
  - p38 Tokyo-to net in-migration from other prefectures, all persons, calendar year 202 = **65,219** person (2025-01-01..2025-12-31) [DISCARD: Tokyo net in-migration; duplicate of p56.] quote: "転入超過数(転入者数-転出者数)は 65,219 人"
  - p39 Tokyo-to migration count between special wards (区相互間), all persons, calendar yea = **306,398** person (2025-01-01..2025-12-31) [DISCARD: Tokyo special-ward migration; not used.] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p40 Tokyo-to migration count between special wards and municipal areas (区部と市町村部間), a = **95,674** person (2025-01-01..2025-12-31) [DISCARD: Tokyo ward-municipal migration; not used.] quote: "区部と市町村部間: 95,674 人(日本人 83,834 人、外国人 11,840 人)"
  - p41 Tokyo-to migration count between municipalities (市町村相互間), all persons, calendar  = **63,073** person (2025-01-01..2025-12-31) [DISCARD: Tokyo municipality-municipality count; not used.] quote: "市町村相互間: 63,073 人(日本人 58,012 人、外国人 5,061 人)"
  - p42 Tokyo-to net in-migration from three adjacent prefectures (Saitama, Chiba, Kanag = **4,557** person (2025-01-01..2025-12-31) [DISCARD: Tokyo adjacent-prefecture net; not used.] quote: "3県合計で2年ぶりに転出超過となり、転出超過数は 4,557 人"
- `https://www.stat.go.jp/data/idou/rireki/2308/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (value_as_written not in quote as a whole number: 3)

### d2 [related_series] Statistics Bureau annual/calendar-year totals

Hypothesis: Annual internal migration totals divided by 12, adjusted for August seasonality share, give the monthly target. August typically has an above-average share due to summer/relocation season.

Queries issued by the searcher: 住民基本台帳人口移動報告 年間 移動者数 2025; Japan internal migration annual total 2024 statistics bureau 住民基本台帳 移動者数 年間; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2023年 結果 市区町村間移動者数 526万; 住民基本台帳人口移動報告 2025年 年間 移動者数; Japan internal migration annual total 2024 Statistics Bureau Basic Resident Registration moves; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2023年 年間 市区町村間移動者数 526万; 統計メールニュース 2024年1月31日 住民基本台帳人口移動報告 2023年結果 市区町村間移動者数 526万; 住民基本台帳人口移動報告 年間 移動者数 2024 総務省統計局; Japan internal migration annual total 2024 statistics bureau 住民基本台帳 移動者数; 住民基本台帳人口移動報告 2025年（令和7年）結果 市区町村間移動者数 年間; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 stat.go.jp

- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 15/15
  - p43 Japan internal migration: moves between municipalities (domestic movers), calend = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p44 Japan internal migration: year-on-year change in domestic municipality-to-munici = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p45 Japan internal migration: moves between prefectures (inter-prefectural movers),  = **2,515,731** person (moves) (2025-01-01..2025-12-31) [DISCARD: Inter-prefectural 2025; duplicate of p316.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p46 Japan internal migration: year-on-year change in inter-prefectural movers, 2025  = **0.3** % (2025-01-01..2025-12-31) [DISCARD: Inter-prefectural yoy; duplicate of p317.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p47 Japan: in-migrants from abroad (overseas transfers in), calendar year 2025 = **782,165** person (2025-01-01..2025-12-31) [DISCARD: Overseas inflow 2025; duplicate of p318.] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p48 Japan: year-on-year change in in-migrants from abroad, 2025 vs 2024 = **6.3** % (2025-01-01..2025-12-31) [DISCARD: Overseas inflow yoy; duplicate of p319.] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p49 Japan: out-migrants to abroad (overseas transfers out), calendar year 2025 = **409,592** person (2025-01-01..2025-12-31) [DISCARD: Overseas outflow 2025; duplicate of p320.] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p50 Japan: year-on-year change in out-migrants to abroad, 2025 vs 2024 = **10.2** % (2025-01-01..2025-12-31) [DISCARD: Overseas outflow yoy; duplicate of p321.] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p51 Japan: national net social increase (社会増減数), calendar year 2025 = **337,234** person (2025-01-01..2025-12-31) [DISCARD: Net social change 2025; duplicate of p313.] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p52 Japan: year-on-year expansion of national net social increase, 2025 vs 2024 = **5,548** person (2025-01-01..2025-12-31) [DISCARD: Net social change yoy; duplicate of p323.] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p53 Tokyo metropolitan area (東京圏): net in-migration (転入超過), calendar year 2025 = **123,534** person (2025-01-01..2025-12-31) [DISCARD: Tokyo-area net in-migration; duplicate of p325.] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p54 Tokyo metropolitan area (東京圏): year-on-year change in net in-migration, 2025 vs  = **12,309** person (2025-01-01..2025-12-31) [DISCARD: Tokyo-area net yoy; not used.] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p55 Three major metropolitan areas combined (３大都市圏): net in-migration, calendar year = **119,581** person (2025-01-01..2025-12-31) [DISCARD: Three-metro net; duplicate of p324.] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p56 Tokyo prefecture: net in-migration (転入超過), calendar year 2025 = **65,219** person (2025-01-01..2025-12-31) [DISCARD: Tokyo net in-migration; not used.] quote: "転入超過数は東京都が6万5219人と最も多く、神奈川県が最も拡大(1089人)"
  - p57 Tokyo prefecture: net social increase (社会増加), calendar year 2025 = **125,457** person (2025-01-01..2025-12-31) [DISCARD: Tokyo net social increase; not used.] quote: "社会増加となっているのは東京都(12万5457人)、大阪府(5万8524人)、千葉県(4万2629人)など23都道府県"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/9
  - p58 Annual internal migration (inter-municipal movers, Japanese and foreign) nationw = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p59 Annual internal migration (inter-municipal movers, Japanese and foreign) nationw = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p60 Annual internal migration (inter-municipal movers, Japanese and foreign) nationw = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p61 Annual inter-prefectural movers (Japanese and foreign) nationwide, 2023 calendar = **2,544,639** person (moves) (2023-01-01..2023-12-31) [DISCARD: Inter-prefectural 2023; duplicate of p409.] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p62 Annual inter-prefectural movers (Japanese and foreign) nationwide, 2024 calendar = **2,523,249** person (moves) (2024-01-01..2024-12-31) [DISCARD: Inter-prefectural 2024; duplicate of p394.] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p63 Annual inter-municipal movers, Japanese only, 2023 calendar year = **4,696,572** person (moves) (2023-01-01..2023-12-31) [DISCARD: Japanese-only 2023; not needed (annual split available for 2024/2025).] quote: "5 2023 4,696,572 2,490,712 2,205,860 -1.6 -1.4 -2.0 2,467,386 1,258,257"
  - p64 Annual inter-municipal movers, Japanese only, 2024 calendar year = **4,603,155** person (moves) (2024-01-01..2024-12-31) [DISCARD: Japanese-only 2024; duplicate of p331.] quote: "6 2024 4,603,155 2,443,456 2,159,699 -2.0 -1.9 -2.1 2,414,565 1,232,750"
  - p65 Annual inter-municipal movers, foreign residents only, 2023 calendar year = **566,677** person (moves) (2023-01-01..2023-12-31) [DISCARD: Foreign-only 2023; duplicate of p333.] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p66 Annual inter-municipal movers, foreign residents only, 2024 calendar year = **604,591** person (moves) (2024-01-01..2024-12-31) [DISCARD: Foreign-only 2024; duplicate of p329.] quote: "6 2024 604,591 348,385 256,206 6.7 7.8 5.2 269,932 149,331"
- `https://www.stat.go.jp/data/idou/2024np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260804104833); points raw/verified 15/15
  - p67 Japan internal migration between municipalities (persons), calendar year 2024 = **5,207,746** person (moves) (2024-01-01..2024-12-31) [DISCARD: Annual total 2024; duplicate of p2.] quote: "2024年の国内における市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p68 Year-on-year change in Japan internal migration between municipalities, 2024 vs  = **1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "2024年の国内における市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p69 Japan inter-prefecture migration (persons), calendar year 2024 = **2,523,249** person (moves) (2024-01-01..2024-12-31) [DISCARD: Inter-prefecture 2024; duplicate of p394.] quote: "都道府県間移動者数は252万3249人となり、前年に比べ0.8%の減少"
  - p70 Year-on-year change in Japan inter-prefecture migration, 2024 vs 2023 = **0.8** % (2024-01-01..2024-12-31) [DISCARD: Inter-prefecture yoy; duplicate of p425.] quote: "都道府県間移動者数は252万3249人となり、前年に比べ0.8%の減少"
  - p71 In-migrants from abroad to Japan (persons), calendar year 2024 = **735,883** person (2024-01-01..2024-12-31) [DISCARD: Overseas inflow 2024; duplicate of p311.] quote: "国外からの転入者数は73万5883人となり、前年に比べ5.1%の増加"
  - p72 Year-on-year change in in-migrants from abroad, 2024 vs 2023 = **5.1** % (2024-01-01..2024-12-31) [DISCARD: Overseas inflow yoy; duplicate of p427.] quote: "国外からの転入者数は73万5883人となり、前年に比べ5.1%の増加"
  - p73 Out-migrants to abroad from Japan (persons), calendar year 2024 = **371,615** person (2024-01-01..2024-12-31) [DISCARD: Overseas outflow 2024; duplicate of p312.] quote: "国外への転出者数は37万1615人となり、前年に比べ7.2%の増加"
  - p74 Year-on-year change in out-migrants to abroad, 2024 vs 2023 = **7.2** % (2024-01-01..2024-12-31) [DISCARD: Overseas outflow yoy; duplicate of p429.] quote: "国外への転出者数は37万1615人となり、前年に比べ7.2%の増加"
  - p75 National net social increase (persons), calendar year 2024 = **331,686** person (2024-01-01..2024-12-31) [DISCARD: Net social change 2024; duplicate of p397.] quote: "全国の社会増減数は、国外からの転入者数(73万5883人)が国外への転出者数(37万1615人)を上回ったこと等により、33万1686人の社会増加"
  - p76 Tokyo metropolitan area net in-migration (persons), calendar year 2024 = **135,843** person (2024-01-01..2024-12-31) [DISCARD: Tokyo-area net 2024; duplicate of p398.] quote: "東京圏は13万5843人の転入超過、前年に比べ9328人の拡大"
  - p77 Nagoya metropolitan area net out-migration (persons), calendar year 2024 = **18,856** person (2024-01-01..2024-12-31) [DISCARD: Nagoya net 2024; duplicate of p400.] quote: "名古屋圏は1万8856人の転出超過、前年に比べ535人の拡大"
  - p78 Osaka metropolitan area net in-migration (persons), calendar year 2024 = **2,679** person (2024-01-01..2024-12-31) [DISCARD: Osaka net 2024; duplicate of p401.] quote: "大阪圏は2679人の転入超過。外国人を含む集計を開始した2014年以降、初めて転出超過から転入超過に転じる"
  - p79 Three major metropolitan areas combined net in-migration (persons), calendar yea = **119,666** person (2024-01-01..2024-12-31) [DISCARD: Three-metro net 2024; duplicate of p399.] quote: "3大都市圏全体では11万9666人の転入超過、前年に比べ1万2031人の拡大"
  - p80 Tokyo net social increase (persons), calendar year 2024 = **140,548** person (2024-01-01..2024-12-31) [DISCARD: Tokyo net social 2024; duplicate of p402.] quote: "社会増加となっているのは東京都(14万548人)、大阪府(4万9767人)、神奈川県(4万1916人)など20都道府県"
  - p81 Tokyo net in-migration (persons), calendar year 2024 = **79,285** person (2024-01-01..2024-12-31) [DISCARD: Tokyo net in-migration 2024; duplicate of p405.] quote: "転入超過数は東京都が7万9285人と最も多く、最も拡大(1万1000人)"
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2024np/jissu/pdf/all.pdf` -> **snapshot** (snapshot 20250516005632); points raw/verified 15/13
  - p82 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p83 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p84 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,310,972** person (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p85 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,247,744** person (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p86 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,255,721** person (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p87 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,403,465** person (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p88 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,359,174** person (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p89 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,318,617** person (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p90 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,251,717** person (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p91 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,384,553** person (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p92 Japan internal migration between municipalities (市区町村間移動者数), all nationalities,  = **5,207,599** person (moves) (2014-01-01..2014-12-31) [keep: ] quote: "市区町村間移動者数 5,207,599 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746"
  - p93 Japan internal migration between municipalities (市区町村間移動者数), Japanese nationals  = **4,696,572** person (moves) (2023-01-01..2023-12-31) [DISCARD: Japanese-only 2023; duplicate of p63.] quote: "総数 4,603,155 4,696,572 -93,417 -2.0 2,188,590 2,229,186 -40,596 -1.8 2,414,565 2,467,386 -52,821 -2.1"
  - p94 Japan internal migration between municipalities (市区町村間移動者数), foreign nationals o = **566,677** person (moves) (2023-01-01..2023-12-31) [DISCARD: Foreign-only 2023; duplicate of p65.] quote: "総数 604,591 566,677 37,914 6.7 334,659 315,453 19,206 6.1 269,932 251,224 18,708 7.4"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2408/index.html` -> **snapshot** (snapshot 20251009225522); points raw/verified 11/11
  - p95 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **355,918** person (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p96 Year-on-year change in total internal migration events between municipalities, a = **23,575** person (moves) (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p97 Year-on-year percent change in total internal migration events between municipal = **6.2** % (2024-08-01..2024-08-31) [keep: ] quote: "移動者の市区町村間移動者数は35万5918人と、前年同月に比べ2万3575人(6.2%)減少。"
  - p98 Inter-prefectural migration events (都道府県間移動者数), all movers, Japan, August 2024 = **161,982** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 inter-prefectural; not needed for the inter-municipal total route.] quote: "移動者の都道府県間移動者数は16万1982人と、前年同月に比べ1万1981人(6.9%)減少。"
  - p99 Intra-prefectural migration events (都道府県内移動者数), all movers, Japan, August 2024 = **193,936** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 intra-prefectural; not needed.] quote: "移動者の都道府県内移動者数は19万3936人と、前年同月に比べ1万1594人(5.6%)減少。"
  - p100 Total internal migration events between municipalities (市区町村間移動者数), Japanese mov = **313,909** person (moves) (2024-08-01..2024-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は31万3909人と、前年同月に比べ2万2692人(6.7%)減少。"
  - p101 Inter-prefectural migration events, Japanese movers only, Japan, August 2024 = **139,649** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 Japanese inter-prefectural; not needed.] quote: "日本人移動者の都道府県間移動者数は13万9649人と、前年同月に比べ1万1007人(7.3%)減少。"
  - p102 Intra-prefectural migration events, Japanese movers only, Japan, August 2024 = **174,260** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 Japanese intra-prefectural; not needed.] quote: "日本人移動者の都道府県内移動者数は17万4260人と、前年同月に比べ1万1685人 (6.3%)減少。"
  - p103 Total internal migration events between municipalities (市区町村間移動者数), foreign move = **42,009** person (moves) (2024-08-01..2024-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2009人と、前年同月に比べ883人(2.1%)減少。"
  - p104 Inter-prefectural migration events, foreign movers only, Japan, August 2024 = **22,333** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 foreign inter-prefectural; not needed.] quote: "外国人移動者の都道府県間移動者数は2万2333人と、前年同月に比べ974人(4.2%)減少。"
  - p105 Intra-prefectural migration events, foreign movers only, Japan, August 2024 = **19,676** person (moves) (2024-08-01..2024-08-31) [DISCARD: Aug 2024 foreign intra-prefectural; not needed.] quote: "外国人移動者の都道府県内移動者数は1万9676人と、前年同月に比べ91人(0.5%)増加。"
- `https://www.stat.go.jp/data/idou/2023np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260726151457); points raw/verified 15/14
  - p106 Japan total inter-municipal internal migration (Japanese and foreign residents), = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "2023年の日本国内における市区町村間移動者数は526万3249人となり、前年に比べ0.9%の減少"
  - p107 Japan total inter-municipal internal migration (Japanese and foreign residents), = **0.9** % (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数は526万3249人。前年に比べ0.9%の減少"
  - p108 Japan inter-prefectural internal migration (Japanese and foreign residents), 202 = **2,544,639** person (moves) (2023-01-01..2023-12-31) [DISCARD: Inter-prefectural 2023; duplicate of p409.] quote: "都道府県間移動者数は254万4639人となり、前年に比べ0.3%の減少"
  - p109 Japan intra-prefectural internal migration (Japanese and foreign residents), 202 = **2,718,610** person (moves) (2023-01-01..2023-12-31) [DISCARD: Intra-prefectural 2023; duplicate of p410.] quote: "都道府県内移動者数は271万8610人となり、前年に比べ1.4%の減少"
  - p110 Japan foreign-resident inter-municipal internal migration, 2023 calendar year = **566,677** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "2023年の日本国内における外国人の市区町村間移動者数は56万6677人となり、前年に比べ5.8%の増加"
  - p111 Japan foreign-resident inter-prefectural internal migration, 2023 calendar year = **315,453** person (moves) (2023-01-01..2023-12-31) [DISCARD: Foreign inter-prefectural 2023; duplicate of p412.] quote: "都道府県間移動者数は31万5453人となり、前年に比べ5.8%の増加"
  - p112 Japan foreign-resident intra-prefectural internal migration, 2023 calendar year = **251,224** person (moves) (2023-01-01..2023-12-31) [DISCARD: Foreign intra-prefectural 2023; duplicate of p413.] quote: "都道府県内移動者数は25万1224人となり、前年に比べ5.7%の増加"
  - p113 Tokyo metropolitan area net in-migration (Japanese and foreign residents), 2023  = **126,515** person (net in-migrants) (2023-01-01..2023-12-31) [DISCARD: Tokyo-area net 2023; duplicate of p414.] quote: "東京圏は12万6515人の転入超過。前年に比べ2万6996人の拡大"
  - p114 Tokyo metropolitan area net in-migration (Japanese residents only), 2023 calenda = **114,802** person (net in-migrants) (2023-01-01..2023-12-31) [DISCARD: Tokyo-area Japanese net 2023; duplicate of p418.] quote: "東京圏は11万4802人の転入超過。前年に比べ2万391人の拡大。28年連続の転入超過"
  - p115 Three major metropolitan areas combined net in-migration (Japanese and foreign r = **107,635** person (net in-migrants) (2023-01-01..2023-12-31) [DISCARD: Three-metro net 2023; duplicate of p415.] quote: "3大都市圏全体では10万7635人の転入超過。前年に比べ2万6681人の拡大"
  - p116 Nagoya metropolitan area net out-migration (Japanese and foreign residents), 202 = **18,321** person (net out-migrants) (2023-01-01..2023-12-31) [DISCARD: Nagoya net 2023; duplicate of p416.] quote: "名古屋圏は1万8321人の転出超過。前年に比べ2103人の拡大"
  - p117 Osaka metropolitan area net out-migration (Japanese and foreign residents), 2023 = **559** person (net out-migrants) (2023-01-01..2023-12-31) [DISCARD: Osaka net 2023; duplicate of p417.] quote: "大阪圏は559人の転出超過。前年に比べ1788人の縮小"
  - p118 Municipalities with net in-migration as share of all municipalities, 2023 = **29.7** % (2023-01-01..2023-12-31) [DISCARD: Municipality share with net in-migration; not used.] quote: "全国1719市町村注1)のうち、転入超過注2)は511市町村で、全市町村の29.7%"
  - p119 Tokyo special wards net in-migration (largest among municipalities), 2023 calend = **53,899** person (net in-migrants) (2023-01-01..2023-12-31) [DISCARD: Tokyo special-ward net; not used.] quote: "転入超過数が最も多い市町村は東京都特別区部(5万3899人)、次いで大阪府大阪市(1万2966人)、神奈川県横浜市(9731人)など"
- `https://www.stat.go.jp/data/idou/rireki/2308/index.html` -> **snapshot** (snapshot 20251011123433); points raw/verified 11/11
  - p120 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **379,493** person (moves) (2023-08-01..2023-08-31) [keep: ] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p121 Year-on-year change in total internal migration events between municipalities, a = **22,480** person (moves) (2023-08-01..2023-08-31) [keep: ] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p122 Year-on-year percent change in total internal migration events between municipal = **5.6** % (2023-08-01..2023-08-31) [keep: ] quote: "移動者の市区町村間移動者数は37万9493人と、前年同月に比べ2万2480人(5.6%)減少。"
  - p123 Inter-prefectural migration events (都道府県間移動者数), all movers, Japan, August 2023 = **173,963** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 inter-prefectural; not needed.] quote: "移動者の都道府県間移動者数は17万3963人と、前年同月に比べ1万2369人(6.6%)減少。"
  - p124 Intra-prefectural migration events (都道府県内移動者数), all movers, Japan, August 2023 = **205,530** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 intra-prefectural; not needed.] quote: "移動者の都道府県内移動者数は20万5530人と、前年同月に比べ1万111人(4.7%)減少。"
  - p125 Internal migration events between municipalities (市区町村間移動者数), Japanese movers on = **336,601** person (moves) (2023-08-01..2023-08-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万6601人と、前年同月に比べ2万1043人(5.9%)減少。"
  - p126 Inter-prefectural migration events, Japanese movers only, Japan, August 2023 = **150,656** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 Japanese inter-prefectural; not needed.] quote: "日本人移動者の都道府県間移動者数は15万656人と、前年同月に比べ1万1591人(7.1%)減少。"
  - p127 Intra-prefectural migration events, Japanese movers only, Japan, August 2023 = **185,945** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 Japanese intra-prefectural; not needed.] quote: "日本人移動者の都道府県内移動者数は18万5945人と、前年同月に比べ9452人 (4.8%)減少。"
  - p128 Internal migration events between municipalities (市区町村間移動者数), foreign movers onl = **42,892** person (moves) (2023-08-01..2023-08-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万2892人と、前年同月に比べ1437人(3.2%)減少。"
  - p129 Inter-prefectural migration events, foreign movers only, Japan, August 2023 = **23,307** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 foreign inter-prefectural; not needed.] quote: "外国人移動者の都道府県間移動者数は2万3307人と、前年同月に比べ778人(3.2%)減少。"
  - p130 Intra-prefectural migration events, foreign movers only, Japan, August 2023 = **19,585** person (moves) (2023-08-01..2023-08-31) [DISCARD: Aug 2023 foreign intra-prefectural; not needed.] quote: "外国人移動者の都道府県内移動者数は1万9585人と、前年同月に比べ659人(3.3%)減少。"
- `https://www.stat.go.jp/data/idou/rireki/2507/index.html` -> **snapshot** (snapshot 20260808220647); points raw/verified 15/15
  - p131 Total internal migration between municipalities (市区町村間移動者数), all movers, Japan,  = **398,417** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p132 Year-on-year change in total internal migration between municipalities, all move = **6,371** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 yoy change; duplicate of p265.] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p133 Year-on-year percent change in total internal migration between municipalities,  = **1.6** % (2025-07-01..2025-07-31) [DISCARD: Jul 2025 yoy percent; duplicate of p266.] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p134 Total internal migration between municipalities (市区町村間移動者数), Japanese movers onl = **345,172** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p135 Year-on-year change in internal migration between municipalities, Japanese mover = **10,632** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 Japanese yoy change; duplicate of p268.] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p136 Year-on-year percent change in internal migration between municipalities, Japane = **3** % (2025-07-01..2025-07-31) [DISCARD: Jul 2025 Japanese yoy percent; duplicate of p269.] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p137 Total internal migration between municipalities (市区町村間移動者数), foreign movers only = **53,245** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p138 Year-on-year change in internal migration between municipalities, foreign movers = **4,261** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 foreign yoy change; duplicate of p271.] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p139 Year-on-year percent change in internal migration between municipalities, foreig = **8.7** % (2025-07-01..2025-07-31) [DISCARD: Jul 2025 foreign yoy percent; duplicate of p272.] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p140 Inter-prefectural migration (都道府県間移動者数), all movers, Japan, July 2025 = **182,864** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 inter-prefectural; duplicate of p273.] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p141 Intra-prefectural migration (都道府県内移動者数), all movers, Japan, July 2025 = **215,553** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 intra-prefectural; duplicate of p274.] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
  - p142 Inter-prefectural migration (都道府県間移動者数), Japanese movers only, Japan, July 2025 = **154,148** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 Japanese inter-prefectural; duplicate of p275.] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p143 Intra-prefectural migration (都道府県内移動者数), Japanese movers only, Japan, July 2025 = **191,024** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 Japanese intra-prefectural; duplicate of p276.] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p144 Inter-prefectural migration (都道府県間移動者数), foreign movers only, Japan, July 2025 = **28,716** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 foreign inter-prefectural; duplicate of p277.] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p145 Intra-prefectural migration (都道府県内移動者数), foreign movers only, Japan, July 2025 = **24,529** person (moves) (2025-07-01..2025-07-31) [DISCARD: Jul 2025 foreign intra-prefectural; duplicate of p278.] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
- dropped by code checks: 9 (value_as_written not in quote as a whole number: 7; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d3 [related_series] Foreign resident component

Hypothesis: Total = Japanese-resident moves + foreign-resident moves. Foreign moves can be estimated from foreign population stock and foreign mobility rates; Japanese moves from Japanese population and historical Japanese mobility. Summing components constrains the total.

Queries issued by the searcher: 住民基本台帳人口移動報告 外国人 移動者数 月次 国籍別; foreign residents Japan internal migration statistics 2025 住民基本台帳 移動者数 外国人; 住民基本台帳人口移動報告 2026年7月結果 外国人移動者 市区町村間移動者数; 在留外国人数 令和7年末 出入国在留管理庁 2025年 外国人住民 人口; 住民基本台帳人口移動報告 外国人 移動者数 月次 2025; 住民基本台帳人口移動報告 2025年 移動者数 国籍別; 住民基本台帳人口移動報告 2026年（令和8年）7月結果 外国人移動者 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月結果 外国人移動者 市区町村間移動者数 統計局; 住民基本台帳人口移動報告 外国人 移動者数 国籍別; foreign residents Japan internal migration statistics 2025 住民基本台帳 外国人の移動; 住民基本台帳人口移動報告 2026年6月結果 外国人移動者 市区町村間移動者数; 住民基本台帳人口移動報告 2025年結果 日本人移動者 市区町村間移動者数 外国人移動者; 在留外国人統計 2025年6月末 在留外国人数 約400万人 出入国在留管理庁

- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/12
  - p146 Japan internal migration between municipalities, total, 2025 (annual) = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p147 Japan internal migration between municipalities, total, 2025 (table, persons) = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p148 Japan internal migration between municipalities, total, 2024 (table, persons) = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p149 Japan inter-prefecture migration, 2025 (annual) = **2,515,731** person (moves) (2025-01-01..2025-12-31) [DISCARD: Inter-prefecture 2025; duplicate of p316.] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p150 Japan intra-prefecture migration, 2025 (table, persons) = **2,674,817** person (moves) (2025-01-01..2025-12-31) [DISCARD: Intra-prefecture 2025; duplicate of p307.] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p151 Inflow from abroad to Japan, 2025 (annual) = **782,165** person (moves) (2025-01-01..2025-12-31) [DISCARD: Overseas inflow 2025; duplicate of p318.] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p152 Outflow from Japan to abroad, 2025 (annual) = **409,592** person (moves) (2025-01-01..2025-12-31) [DISCARD: Overseas outflow 2025; duplicate of p320.] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p153 Inflow from abroad to Japan, 2024 (table, persons) = **735,883** person (moves) (2024-01-01..2024-12-31) [DISCARD: Overseas inflow 2024; duplicate of p311.] quote: "国外からの転入者数 - - - - - 358,359 209,700 639,124 700,138 735,883 782,165"
  - p154 Outflow from Japan to abroad, 2024 (table, persons) = **371,615** person (moves) (2024-01-01..2024-12-31) [DISCARD: Overseas outflow 2024; duplicate of p312.] quote: "国外への転出者数 - - - - - 226,845 224,077 312,484 346,690 371,615 409,592"
  - p155 Tokyo area net in-migration, foreign movers, 2025 = **10,796** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo-area foreign net 2025; duplicate of p328.] quote: "東京圏は1万796人の転入超過、前年に比べ5710人の縮小"
  - p156 Three major metropolitan areas net in-migration, Japanese movers, 2025 = **110,680** person (moves) (2025-01-01..2025-12-31) [DISCARD: Three-metro Japanese net 2025; duplicate of p326.] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p157 Three major metropolitan areas in-migrants, Japanese movers, 2025 (table, person = **754,602** person (moves) (2025-01-01..2025-12-31) [DISCARD: Three-metro Japanese in-migrants; not used.] quote: "転入者数 813,906 795,328 796,693 808,772 816,306 767,651 751,990 766,689 777,968 769,772 754,602"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/11
  - p158 Total internal migration events between municipalities, Japan, all nationalities = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p159 Japanese-only internal migration events between municipalities, Japan, 2025 cale = **4,528,254** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p160 Foreign-resident internal migration events between municipalities, Japan, 2025 c = **662,294** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p161 Foreign-resident internal migration events between municipalities, Japan, 2024 c = **604,591** person (moves) (2024-01-01..2024-12-31) [DISCARD: Foreign-only 2024; duplicate of p329.] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p162 Japanese-resident internal migration events between municipalities, Japan, 2024  = **4,603,155** person (moves) (2024-01-01..2024-12-31) [DISCARD: Japanese-only 2024; duplicate of p331.] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p163 Total internal migration events between municipalities, Japan, all nationalities = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 5,190,548 5,207,746 -17,198 -0.3 2,515,731 2,523,249 -7,518 -0.3 2,674,817 2,684,497 -9,680 -0.4"
  - p164 Foreign-resident inter-prefectural migration events, Japan, 2025 calendar year = **367,402** person (moves) (2025-01-01..2025-12-31) [DISCARD: Foreign inter-prefectural 2025; not used.] quote: "都道府県間移動者数は36万7402人(対前年比9.8%増)。2014年以降、過去最多"
  - p165 Japanese-resident inter-prefectural migration events, Japan, 2025 calendar year = **2,148,329** person (moves) (2025-01-01..2025-12-31) [DISCARD: Japanese inter-prefectural 2025; not used.] quote: "都道府県間移動者数は214万8329人(対前年比1.8%減)"
  - p166 Japanese-resident intra-prefectural migration events, Japan, 2025 calendar year = **2,379,925** person (moves) (2025-01-01..2025-12-31) [DISCARD: Japanese intra-prefectural 2025; not used.] quote: "都道府県内移動者数は237万9925人で、前年に比べ3万4640人(1.4%)の減少となっている。"
  - p167 Foreign-resident inter-municipal migration events, Japan, 2023 calendar year = **566,677** person (moves) (2023-01-01..2023-12-31) [DISCARD: Foreign-only 2023; duplicate of p333.] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p168 Foreign-resident inter-municipal migration events, Japan, 2022 calendar year = **535,765** person (moves) (2022-01-01..2022-12-31) [DISCARD: Foreign-only 2022; duplicate of p334.] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp-newsfocus.com/foreign-resident-interprefectural-moves-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 15/15
  - p169 Total internal migration between municipalities (市区町村間移動者数), all nationalities,  = **379,751** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 total; not needed.] quote: "・市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p170 Japanese-resident internal migration between municipalities (日本人移動者 市区町村間移動者数),  = **321,850** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 Japanese; not needed.] quote: "・市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p171 Foreign-resident internal migration between municipalities (外国人移動者 市区町村間移動者数), J = **57,901** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 foreign; not needed.] quote: "・市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p172 Total internal migration between municipalities, all nationalities, Japan, Octob = **378,202** person (moves) (2024-10-01..2024-10-31) [DISCARD: Oct 2024 total; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p173 Japanese-resident internal migration between municipalities, Japan, October 2024 = **326,783** person (moves) (2024-10-01..2024-10-31) [DISCARD: Oct 2024 Japanese; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p174 Foreign-resident internal migration between municipalities, Japan, October 2024  = **51,419** person (moves) (2024-10-01..2024-10-31) [DISCARD: Oct 2024 foreign; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p175 Year-on-year change in foreign-resident internal migration between municipalitie = **6,482** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2024 foreign yoy change; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p176 Year-on-year growth rate of foreign-resident internal migration between municipa = **12.6** % (2025-10-01..2025-10-31) [DISCARD: Oct 2024 foreign yoy percent; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p177 Year-on-year growth rate of Japanese-resident internal migration between municip = **-1.5** % (2025-10-01..2025-10-31) [DISCARD: Oct 2024 Japanese yoy percent; not needed.] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p178 Total inter-prefectural migration (都道府県間移動者数), all nationalities, Japan, October = **168,057** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 inter-prefectural; not needed.] quote: "・都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p179 Foreign-resident inter-prefectural migration (外国人移動者 都道府県間移動者数), Japan, October  = **30,709** as written "3万 709", value check pending person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 foreign inter-prefectural; not needed.] quote: "・都道府県間移動者数は 3万 709人。前年同月に比べ増加 4147人( 15.6%)"
  - p180 Japanese-resident inter-prefectural migration (日本人移動者 都道府県間移動者数), Japan, October = **137,348** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 Japanese inter-prefectural; not needed.] quote: "・都道府県間移動者数は 13万7348人。前年同月に比べ減少 ▲ 3197人( ▲ 2.3%)"
  - p181 Total intra-prefectural migration (都道府県内移動者数), all nationalities, Japan, October = **211,694** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 intra-prefectural; not needed.] quote: "・都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p182 Foreign-resident intra-prefectural migration (外国人移動者 都道府県内移動者数), Japan, October  = **27,192** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 foreign intra-prefectural; not needed.] quote: "・都道府県内移動者数は 2万7192人。前年同月に比べ増加 2335人( 9.4%)"
  - p183 Japanese-resident intra-prefectural migration (日本人移動者 都道府県内移動者数), Japan, October = **184,502** person (moves) (2025-10-01..2025-10-31) [DISCARD: Oct 2025 Japanese intra-prefectural; not needed.] quote: "・都道府県内移動者数は 18万4502人。前年同月に比べ減少 ▲ 1736人( ▲ 0.9%)"
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search?page=1&iroha=29&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.toukei.metro.tokyo.lg.jp/jidou/2025/ji-point.pdf` -> **snapshot** (snapshot 20260718032106); points raw/verified 15/15
  - p184 Tokyo inter-municipal internal migrants, total (Japanese + foreign), 2025 = **1,317,064** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "令和7年における東京都の区市町村間移動者数は 1,317,064 人で、前年比 6,596 人(△0.5%)減"
  - p185 Tokyo inter-municipal internal migrants, Japanese only, 2025 = **1,116,080** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人の区市町村間移動者数は 1,116,080 人で、前年比 20,233 人(△1.8%)減"
  - p186 Tokyo inter-municipal internal migrants, foreign only, 2025 = **200,984** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "外国人の区市町村間移動者数は 200,984 人で、前年比 13,637 人(7.3%)増"
  - p187 Tokyo year-on-year change in total inter-municipal migrants, 2025 = **6,596** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo yoy change; duplicate of p31.] quote: "前年比 6,596 人(△0.5%)減"
  - p188 Tokyo year-on-year change in Japanese inter-municipal migrants, 2025 = **20,233** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo Japanese yoy change; not used.] quote: "前年比 20,233 人(△1.8%)減"
  - p189 Tokyo year-on-year change in foreign inter-municipal migrants, 2025 = **13,637** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo foreign yoy change; not used.] quote: "前年比 13,637 人(7.3%)増"
  - p190 Tokyo year-on-year percent change in foreign inter-municipal migrants, 2025 = **7.3** % (2025-01-01..2025-12-31) [DISCARD: Tokyo foreign yoy percent; duplicate of p32.] quote: "前年比 13,637 人(7.3%)増"
  - p191 Tokyo inter-municipal migrants between other prefectures, total, 2025 = **838,467** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo inter-prefectural; duplicate of p33.] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p192 Tokyo inter-municipal migrants between other prefectures, Japanese only, 2025 = **730,373** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo Japanese inter-prefectural; not used.] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p193 Tokyo inter-municipal migrants between other prefectures, foreign only, 2025 = **108,094** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo foreign inter-prefectural; not used.] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p194 Tokyo intra-Tokyo inter-municipal migrants, total, 2025 = **465,145** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo intra-Tokyo; duplicate of p34.] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p195 Tokyo intra-Tokyo inter-municipal migrants, Japanese only, 2025 = **384,882** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo Japanese intra-Tokyo; not used.] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p196 Tokyo intra-Tokyo inter-municipal migrants, foreign only, 2025 = **80,263** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo foreign intra-Tokyo; not used.] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p197 Tokyo other migrants (previous address unknown), total, 2025 = **13,452** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo other-migration; duplicate of p35.] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p198 Tokyo other migrants (previous address unknown), foreign only, 2025 = **12,627** person (moves) (2025-01-01..2025-12-31) [DISCARD: Tokyo foreign other-migration; not used.] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202501007A-sonota1_0.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gaikokujin-press.com/archives/3245` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040380508` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7)

### d4 [base_rates] Demographic rate approach

Hypothesis: Internal migration events per 1000 population per month (mobility rate) is fairly stable; multiply August 2026 population by the August mobility rate. August rate is elevated by moving season.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 転入超過 移動者数; 人口移動率 8月 住民基本台帳 総務省 統計局; 住民基本台帳に基づく人口 2026年1月1日 総人口 日本人 外国人 総務省; 人口推計 2026年 総人口 1億2000万人 統計局 月報; 住民基本台帳人口移動報告 2026年8月 市区町村間 移動者数; 人口移動率 8月 住民基本台帳 過去; 総人口 2026年 住民基本台帳 日本人 外国人; 2025年8月 住民基本台帳人口移動報告 市区町村間移動者数 348602 移動率; 2024年8月 住民基本台帳人口移動報告 市区町村間移動者数; 人口推計 2026年8月 総人口 統計局; 2026年1月1日 住民基本台帳 総人口 123767642; 住民基本台帳人口移動報告 2025年8月 移動者数; internal migration rate per 1000 Japan monthly 住民基本台帳 人口移動率; stat.go.jp 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数; 人口推計 2026年 総人口 1億2000万人 統計局 月報

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/articles/-/54278` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/c32b4a72-aa04-485a-a2ac-5e26daca42e6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/8
  - p199 Japan annual internal migration rate (municipality-to-municipality movers / popu = **4.17** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動率は4.17%で前年と同率"
  - p200 Japan municipality-to-municipality movers (internal migration events), all perso = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p201 Japan municipality-to-municipality movers (internal migration events), all perso = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p202 Japan inter-prefectural movers, all persons, calendar year 2025 = **2,515,731** person (moves) (2025-01-01..2025-12-31) [DISCARD: Inter-prefectural 2025; duplicate of p316.] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p203 Japan municipality-to-municipality movers, Japanese nationals only, calendar yea = **4,528,254** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p204 Japan municipality-to-municipality movers, foreign nationals only, calendar year = **662,294** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p205 Japan municipality-to-municipality movers, foreign nationals only, calendar year = **604,591** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p206 Japan municipality-to-municipality movers, all persons, calendar year 2015 (earl = **5,384,553** person (moves) (2015-01-01..2015-12-31) [DISCARD: Annual total 2015; duplicate of p11.] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- `https://www.yomiuri.co.jp/politics/20260729-GYT1T00324` -> **snapshot** (snapshot 20260829171942); points raw/verified 13/8
  - p207 Japan total population (Japanese + foreign residents) as of January 1, 2026, per = **123,767,642** person (2026-01-01..2026-01-01) [keep: ] quote: "国内総人口は1億2376万7642人で前年から56万3048人減った。"
  - p208 Japanese national population as of January 1, 2026 = **119,736,483** person (2026-01-01..2026-01-01) [keep: ] quote: "日本人住民は、前年比91万6744人減の1億1973万6483人で42年ぶりに1億2000万人を割り込んだ。"
  - p209 Foreign resident population as of January 1, 2026 = **4,031,159** person (2026-01-01..2026-01-01) [keep: ] quote: "外国人住民は、同35万3696人増の403万1159人で過去最多だった。"
  - p210 Year-on-year change in Japanese national population (decrease) as of January 1,  = **916,744** person (2025-01-01..2026-01-01) [DISCARD: Japanese population yoy change; not used.] quote: "日本人住民は、前年比91万6744人減の1億1973万6483人で42年ぶりに1億2000万人を割り込んだ。"
  - p211 Year-on-year change in foreign resident population (increase) as of January 1, 2 = **353,696** person (2025-01-01..2026-01-01) [DISCARD: Foreign population yoy change; not used.] quote: "外国人住民は、同35万3696人増の403万1159人で過去最多だった。"
  - p212 Year-on-year change in Japan total population (decrease) as of January 1, 2026 = **563,048** person (2025-01-01..2026-01-01) [DISCARD: Total population yoy change; not used.] quote: "国内総人口は1億2376万7642人で前年から56万3048人減った。"
  - p213 Largest prefectural total population decline rate (Akita), year to January 1, 20 = **1.88** as written "1・88%", value check pending % (2025-01-01..2026-01-01) [DISCARD: Akita decline rate; not used.] quote: "総人口の減少率は秋田県の1・88%が最大で、山形、青森両県の1・62%などが続いた。"
  - p214 Prefectural total population decline rate (Yamagata and Aomori), year to January = **1.62** as written "1・62%", value check pending % (2025-01-01..2026-01-01) [DISCARD: Yamagata/Aomori decline rate; not used.] quote: "総人口の減少率は秋田県の1・88%が最大で、山形、青森両県の1・62%などが続いた。"
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040380881&iroha=42` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2019np/kihon/pdf/all.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://catalog.data.metro.tokyo.lg.jp/ja/dataset/t000003d0000000560/resource/644d9bab-78f9-4e86-af7e-eb3bd01b5807/view/99df9df3-5967-4ab7-90c3-e2f452` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7; period year 2025 does not appear in the page text or URL (likely mis-dated): 5)

### d5 [administrative] Municipal registration offices / e-Stat

Hypothesis: Preliminary monthly figures are released via e-Stat and the Statistics Bureau; checking release calendar and any advance tables confirms timing and whether a preliminary August 2026 figure could exist before cutoff (it should not). This constrains whether the target is a forecast.

Queries issued by the searcher: e-Stat 住民基本台帳人口移動報告 公表予定 2026; Statistics Bureau Japan Report on Internal Migration release schedule 2026; stat.go.jp 住民基本台帳人口移動報告 公表予定 令和8年 9月; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 公表予定 2026; Statistics Bureau Japan Report on Internal Migration release schedule 2026; stat.go.jp data idou 公表予定 令和8年 月次結果 公表日; "住民基本台帳人口移動報告" 2026年8月分 公表 9月; e-Stat 住民基本台帳人口移動報告 公表予定 2026; Statistics Bureau Japan Report on Internal Migration release schedule 2026; stat.go.jp 住民基本台帳人口移動報告 公表予定 令和8年 9月結果; "住民基本台帳人口移動報告" "2026年8月結果" 公表

- `https://www.stat.go.jp/data/idou/qa-1.html` -> **snapshot** (snapshot 20260419172017); points raw/verified 14/4
  - p215 Start year of publishing municipality-level out-migrants (転出者数) in annual result = **2,010** year (2010-01-01..2010-12-31) [DISCARD: Publication start year; not used.] quote: "2010年(平成22年)から年次結果で公表を開始しました。"
  - p216 Start year of publishing age-specific movers = **2,010** year (2010-01-01..2010-12-31) [DISCARD: Publication start year; not used.] quote: "2010年(平成22年)から公表を開始しました。"
  - p217 Start year of tabulating overseas migration (reference table 2020-2023) = **2,020** year (2020-01-01..2020-12-31) [DISCARD: Overseas table start year; not used.] quote: "2020年以降、集計を行っており、2020年から2023年までは参考表として、掲載しています。"
  - p218 End year of overseas migration reference table period = **2,023** year (2023-01-01..2023-12-31) [DISCARD: Overseas table end year; not used.] quote: "2020年から2023年までは参考表として、掲載しています。"
- `https://www.e-stat.go.jp/en/stat-search/database?page=1&bunya_l=02&layout=dataset&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2603/index.html` -> **snapshot** (snapshot 20260612111251); points raw/verified 14/14
  - p219 Total internal movers between municipalities (市区町村間移動者数), all nationalities, Mar = **916,197** person (moves) (2026-03-01..2026-03-31) [keep: ] quote: "移動者の市区町村間移動者数は91万6197人と、前年同月に比べ1万1018人(1.2%)増加。"
  - p220 Year-on-year change in total internal movers between municipalities, all nationa = **11,018** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 yoy change; duplicate of p229/p225 context.] quote: "移動者の市区町村間移動者数は91万6197人と、前年同月に比べ1万1018人(1.2%)増加。"
  - p221 Year-on-year percent change in total internal movers between municipalities, all = **1.2** % (2026-03-01..2026-03-31) [DISCARD: Mar 2026 yoy percent; not needed.] quote: "移動者の市区町村間移動者数は91万6197人と、前年同月に比べ1万1018人(1.2%)増加。"
  - p222 Total internal movers between prefectures (都道府県間移動者数), all nationalities, March  = **528,163** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 inter-prefectural; not needed.] quote: "移動者の都道府県間移動者数は52万8163人と、前年同月に比べ9631人(1.9%)増加。"
  - p223 Total internal movers within prefectures (都道府県内移動者数), all nationalities, March 2 = **388,034** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 intra-prefectural; not needed.] quote: "移動者の都道府県内移動者数は38万8034人と、前年同月に比べ1387人(0.4%)増加。"
  - p224 Japanese internal movers between municipalities (日本人移動者の市区町村間移動者数), March 2026 = **816,562** person (moves) (2026-03-01..2026-03-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は81万6562人と、前年同月に比べ4584人(0.6%)減少。"
  - p225 Year-on-year change in Japanese internal movers between municipalities, March 20 = **4,584** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 Japanese yoy change; not needed.] quote: "日本人移動者の市区町村間移動者数は81万6562人と、前年同月に比べ4584人(0.6%)減少。"
  - p226 Japanese internal movers between prefectures, March 2026 = **467,133** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 Japanese inter-prefectural; not needed.] quote: "日本人移動者の都道府県間移動者数は46万7133人と、前年同月に比べ1396人(0.3%)減少。"
  - p227 Japanese internal movers within prefectures, March 2026 = **349,429** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 Japanese intra-prefectural; not needed.] quote: "日本人移動者の都道府県内移動者数は34万9429人と、前年同月に比べ3188人 (0.9%)減少。"
  - p228 Foreign internal movers between municipalities (外国人移動者の市区町村間移動者数), March 2026 = **99,635** person (moves) (2026-03-01..2026-03-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は9万9635人と、前年同月に比べ1万5602人(18.6%)増加。"
  - p229 Year-on-year change in foreign internal movers between municipalities, March 202 = **15,602** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 foreign yoy change; duplicate of p228 context.] quote: "外国人移動者の市区町村間移動者数は9万9635人と、前年同月に比べ1万5602人(18.6%)増加。"
  - p230 Year-on-year percent change in foreign internal movers between municipalities, M = **18.6** % (2026-03-01..2026-03-31) [DISCARD: Mar 2026 foreign yoy percent; duplicate of p228 context.] quote: "外国人移動者の市区町村間移動者数は9万9635人と、前年同月に比べ1万5602人(18.6%)増加。"
  - p231 Foreign internal movers between prefectures, March 2026 = **61,030** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 foreign inter-prefectural; not needed.] quote: "外国人移動者の都道府県間移動者数は6万1030人と、前年同月に比べ1万1027人(22.1%)増加。"
  - p232 Foreign internal movers within prefectures, March 2026 = **38,605** person (moves) (2026-03-01..2026-03-31) [DISCARD: Mar 2026 foreign intra-prefectural; not needed.] quote: "外国人移動者の都道府県内移動者数は3万8605人と、前年同月に比べ4575人(13.4%)増加。"
- `https://www.stat.go.jp/info/mail/pdf/20260227_no1840.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search?iroha=1&layout=dataset&page=1&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **snapshot** (snapshot 20260419022039); points raw/verified 11/11
  - p233 Total internal migration events between municipalities (市区町村間移動者数), all movers,  = **356,713** person (moves) (2026-02-01..2026-02-28) [keep: ] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p234 Change in total inter-municipal movers vs same month previous year, February 202 = **343** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 yoy change; not needed.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p235 Year-on-year percent change in total inter-municipal movers, February 2026 = **0.1** % (2026-02-01..2026-02-28) [DISCARD: Feb 2026 yoy percent; not needed.] quote: "移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人(0.1%)減少。"
  - p236 Total inter-prefectural movers, all movers, February 2026 = **163,993** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 inter-prefectural; not needed.] quote: "移動者の都道府県間移動者数は16万3993人と、前年同月に比べ2472人(1.5%)増加。"
  - p237 Total intra-prefectural movers, all movers, February 2026 = **192,720** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 intra-prefectural; not needed.] quote: "移動者の都道府県内移動者数は19万2720人と、前年同月に比べ2815人(1.4%)減少。"
  - p238 Japanese movers, inter-municipal movers, February 2026 = **309,774** person (moves) (2026-02-01..2026-02-28) [keep: ] quote: "日本人移動者の市区町村間移動者数は30万9774人と、前年同月に比べ4623人(1.5%)減少。"
  - p239 Japanese movers, inter-prefectural movers, February 2026 = **137,548** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 Japanese inter-prefectural; not needed.] quote: "日本人移動者の都道府県間移動者数は13万7548人と、前年同月に比べ1269人(0.9%)減少。"
  - p240 Japanese movers, intra-prefectural movers, February 2026 = **172,226** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 Japanese intra-prefectural; not needed.] quote: "日本人移動者の都道府県内移動者数は17万2226人と、前年同月に比べ3354人 (1.9%)減少。"
  - p241 Foreign movers, inter-municipal movers, February 2026 = **46,939** person (moves) (2026-02-01..2026-02-28) [keep: ] quote: "外国人移動者の市区町村間移動者数は4万6939人と、前年同月に比べ4280人(10.0%)増加。"
  - p242 Foreign movers, inter-prefectural movers, February 2026 = **26,445** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 foreign inter-prefectural; not needed.] quote: "外国人移動者の都道府県間移動者数は2万6445人と、前年同月に比べ3741人(16.5%)増加。"
  - p243 Foreign movers, intra-prefectural movers, February 2026 = **20,494** person (moves) (2026-02-01..2026-02-28) [DISCARD: Feb 2026 foreign intra-prefectural; not needed.] quote: "外国人移動者の都道府県内移動者数は2万494人と、前年同月に比べ539人(2.7%)増加。"
- `https://www.stat.go.jp/info/t-news/pdf/2602.pdf` -> **snapshot** (snapshot 20260416170037); points raw/verified 8/2
  - p244 Latest month covered by the release schedule table (2026年3月) = **3** as written "2026年3月", value check pending month of year (2026-03-01..2026-03-31) [DISCARD: Release schedule month; not a quantity.] quote: "統計関係の主要日程(2026年2月~2026年3月)"
  - p245 Issue date of 統計調査ニュース No.471 = **2** as written "令和 8 年(2026 年)2月", value check pending month of year (2026-02-01..2026-02-28) [DISCARD: Newsletter issue date; not a quantity.] quote: "統計調査ニュース No.471 令和 8 年(2026 年)2月"
- `https://fermata-integrity.com/stats/estatList.php?limit=1100&statsDataId=0004044293&openYears=2026&statsCode=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search/database?layout=dataset&cycle=7&toukei=00200523&tstat=000000070001&tclass1=000001219441&tclass2val=0&pa` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fermata-integrity.com/smpl/php/estatList.php?limit=1000&statsDataId=0003419947&openYears=2026&statsCode=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&bunya_l=02` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (number: no number in value_as_written: 1; number: more than one number in value_as_written: 1; period_end missing or unparseable: 5; value_as_written not in quote as a whole number: 9)

### d6 [shocks] Calendar and policy effects

Hypothesis: August 2026 migration may deviate from trend due to calendar effects (Obon, moving season), policy changes (e.g. foreign resident registration rules), or economic conditions. Quantify deviation from the historical August pattern.

Queries issued by the searcher: 住民基本台帳 制度変更 2026 外国人; Statistics Bureau Japan Report on Internal Migration Basic Resident Registration August 2025; 特定在留カード 2026年6月14日 運用開始 在留カード 新様式 マイナンバーカード機能; 住民基本台帳法 改正 令和8年 施行 転入 転出 届出 変更; 住民基本台帳人口移動報告 2026年8月 公表; 住民基本台帳 制度変更 2026 外国人; 統計局 住民基本台帳人口移動報告 2026年7月結果 公表 8月27日 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 外国人移動者; 住民基本台帳 制度変更 2026 外国人; Japan resident registration policy change 2025 2026 foreign residents basic resident register; Statistics Bureau Report on Internal Migration in Japan Derived from Basic Resident Registration 2026 monthly; 住民基本台帳人口移動報告 2025年8月 転入 転出 移動者数

- `https://laws.e-gov.go.jp/law/342CO0000000292?occasion_date=20260301` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.city.yamato.lg.jp/gyosei/life_scene/hikkoshi/jusho/14367.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://210.173.40.80/kurashi/0000000438.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://city.numazu.shizuoka.jp/kurashi/todokede/gaikokujin.htm` -> **snapshot** (snapshot 20251111113046); points raw/verified 0/0
- `https://www.city.shunan.lg.jp/soshiki/20/2593.html` -> **snapshot** (snapshot 20250427171948); points raw/verified 10/0
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p246 Total internal migration events between municipalities (all movers), Japan, July = **390,799** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p247 Year-on-year change in total internal migration events between municipalities (a = **7,618** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 yoy change; duplicate of p280.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p248 Year-on-year percent change in total internal migration events between municipal = **1.9** % (2026-07-01..2026-07-31) [DISCARD: Jul 2026 yoy percent; duplicate of p281.] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p249 Japanese movers internal migration events between municipalities, Japan, July 20 = **335,854** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p250 Year-on-year change in Japanese movers internal migration events between municip = **9,318** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 Japanese yoy change; duplicate of p283.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p251 Year-on-year percent change in Japanese movers internal migration events between = **2.7** % (2026-07-01..2026-07-31) [DISCARD: Jul 2026 Japanese yoy percent; duplicate of p284.] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p252 Foreign movers internal migration events between municipalities, Japan, July 202 = **54,945** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p253 Year-on-year change in foreign movers internal migration events between municipa = **1,700** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 foreign yoy change; duplicate of p286.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p254 Year-on-year percent change in foreign movers internal migration events between  = **3.2** % (2026-07-01..2026-07-31) [DISCARD: Jul 2026 foreign yoy percent; duplicate of p287.] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p255 Total internal migration events between prefectures (all movers), Japan, July 20 = **181,604** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 inter-prefectural; duplicate of p288.] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p256 Total internal migration events within prefectures (all movers), Japan, July 202 = **209,195** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 intra-prefectural; duplicate of p289.] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p257 Foreign movers internal migration events between prefectures, Japan, July 2026 = **31,257** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 foreign inter-prefectural; duplicate of p292.] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p258 Year-on-year percent change in foreign movers internal migration events between  = **8.8** % (2026-07-01..2026-07-31) [DISCARD: Jul 2026 foreign inter-prefectural yoy; duplicate of p292 context.] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p259 Foreign movers internal migration events within prefectures, Japan, July 2026 = **23,688** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 foreign intra-prefectural; duplicate of p293.] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
  - p260 Japanese movers internal migration events between prefectures, Japan, July 2026 = **150,347** person (moves) (2026-07-01..2026-07-31) [DISCARD: Jul 2026 Japanese inter-prefectural; duplicate of p290.] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jimin.jp/news/information/213554.html` -> **snapshot** (snapshot 20260624192723); points raw/verified 5/3
  - p261 Number of foreign residents in Japan at end of June 2025 (Reiwa 7), stated as re = **4,000,000** person (2025-06-30..2025-06-30) [DISCARD: Foreign resident stock mid-2025; not used.] quote: "在留外国人数が令和7年6月末時点で過去最高の約400万人に達した中、マイナンバーカード保有率は約6割にとどまり"
  - p262 My Number card holding rate among foreign residents (share of foreign residents  = **6** % (foreign residents holding My Number card / foreign reside (2025-06-30..2025-06-30) [DISCARD: My Number holding rate; not used.] quote: "マイナンバーカード保有率は約6割にとどまり"
  - p263 Year the amended Immigration Control Act providing for card integration was enac = **6** year (Reiwa era) (2024-01-01..2024-12-31) [DISCARD: Legislation year; not used.] quote: "令和6年に成立した入管法等改正で、一体化が措置されました。"
- `https://www.city.mito.lg.jp/site/mito-mynumbercard/127442.html` -> **snapshot** (snapshot 20260810042739); points raw/verified 4/0
- `https://www.city.kuki.lg.jp/kurashi/koseki/koseki_oshirase/1013602.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (number: more than one number in value_as_written: 8; period_end missing or unparseable: 8)

### b1 [own_history] Statistics Bureau monthly report archive

Hypothesis: August 2025 monthly inter-municipal mover total (all nationalities) would anchor the yoy_scaling route: August 2026 = August 2025 x (July 2026 / July 2025). Currently only August 2023 and 2024 are kept; the 2025 August value is the single missing input that would let the strongest seasonal route run.

Queries issued by the searcher: stat.go.jp 人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; 令和7年8月 住民基本台帳人口移動報告 市区町村間移動者数 外国人 日本人; Report on Internal Migration in Japan August 2025 total inter-municipal movers; stat.go.jp 人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 市区町村間移動者数; stat.go.jp/data/idou/rireki/2508/index.html 2025年8月結果 市区町村間移動者数 日本人移動者 外国人移動者; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 前年同月; stat.go.jp 住民基本台帳人口移動報告 令和7年8月 市区町村間移動者数; e-Stat 住民基本台帳人口移動報告 2025年8月 移動者数; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 統計メールニュース 2026年8月27日 住民基本台帳人口移動報告 2026年7月 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2507/index.html` -> **snapshot** (snapshot 20260808220647); points raw/verified 15/15
  - p264 Total inter-municipal movers (市区町村間移動者数), all nationalities, Japan, July 2025 = **398,417** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p265 Year-on-year change in total inter-municipal movers, all nationalities, Japan, J = **6,371** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p266 Year-on-year percent change in total inter-municipal movers, all nationalities,  = **1.6** % (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p267 Japanese inter-municipal movers (日本人移動者の市区町村間移動者数), Japan, July 2025 = **345,172** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p268 Year-on-year change in Japanese inter-municipal movers, Japan, July 2025 vs July = **10,632** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p269 Year-on-year percent change in Japanese inter-municipal movers, Japan, July 2025 = **3** % (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p270 Foreign inter-municipal movers (外国人移動者の市区町村間移動者数), Japan, July 2025 = **53,245** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p271 Year-on-year change in foreign inter-municipal movers, Japan, July 2025 vs July  = **4,261** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p272 Year-on-year percent change in foreign inter-municipal movers, Japan, July 2025 = **8.7** % (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p273 Total inter-prefectural movers (都道府県間移動者数), all nationalities, Japan, July 2025 = **182,864** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p274 Total intra-prefectural movers (都道府県内移動者数), all nationalities, Japan, July 2025 = **215,553** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
  - p275 Japanese inter-prefectural movers (日本人移動者の都道府県間移動者数), Japan, July 2025 = **154,148** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p276 Japanese intra-prefectural movers (日本人移動者の都道府県内移動者数), Japan, July 2025 = **191,024** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p277 Foreign inter-prefectural movers (外国人移動者の都道府県間移動者数), Japan, July 2025 = **28,716** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p278 Foreign intra-prefectural movers (外国人移動者の都道府県内移動者数), Japan, July 2025 = **24,529** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 15/15
  - p279 Total inter-municipal movers (市区町村間移動者数), all nationalities, July 2026 = **390,799** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p280 Year-on-year change in total inter-municipal movers, all nationalities, July 202 = **7,618** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p281 Year-on-year percent change in total inter-municipal movers, all nationalities,  = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p282 Japanese inter-municipal movers (日本人移動者の市区町村間移動者数), July 2026 = **335,854** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p283 Year-on-year change in Japanese inter-municipal movers, July 2026 = **9,318** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p284 Year-on-year percent change in Japanese inter-municipal movers, July 2026 = **2.7** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p285 Foreign inter-municipal movers (外国人移動者の市区町村間移動者数), July 2026 = **54,945** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p286 Year-on-year change in foreign inter-municipal movers, July 2026 = **1,700** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p287 Year-on-year percent change in foreign inter-municipal movers, July 2026 = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p288 Total inter-prefectural movers (都道府県間移動者数), all nationalities, July 2026 = **181,604** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p289 Total intra-prefectural movers (都道府県内移動者数), all nationalities, July 2026 = **209,195** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p290 Japanese inter-prefectural movers, July 2026 = **150,347** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p291 Japanese intra-prefectural movers, July 2026 = **185,507** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p292 Foreign inter-prefectural movers, July 2026 = **31,257** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p293 Foreign intra-prefectural movers, July 2026 = **23,688** person (moves) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/10
  - p294 Total inter-municipal movers (all nationalities), Japan, calendar year 2025 = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p295 Total inter-municipal movers (all nationalities), Japan, calendar year 2024 = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p296 Total inter-municipal movers (all nationalities), Japan, calendar year 2023 = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p297 Japanese inter-municipal movers, Japan, calendar year 2025 = **4,528,254** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p298 Japanese inter-municipal movers, Japan, calendar year 2024 = **4,603,155** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p299 Foreign inter-municipal movers, Japan, calendar year 2025 = **662,294** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p300 Foreign inter-municipal movers, Japan, calendar year 2024 = **604,591** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p301 Inter-prefectural movers (all nationalities), Japan, calendar year 2025 = **2,515,731** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p302 Year-on-year change in total inter-municipal movers (all nationalities), Japan,  = **-17,198** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p303 Year-on-year change rate in total inter-municipal movers (all nationalities), Ja = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/10
  - p304 Japan annual total inter-municipal movers (市区町村間移動者数), all nationalities, 2025 = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p305 Japan annual total inter-municipal movers (市区町村間移動者数), all nationalities, 2024 = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p306 Japan annual total inter-municipal movers (市区町村間移動者数), all nationalities, 2023 = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p307 Japan annual intra-prefectural movers (都道府県内移動者数), all nationalities, 2025 = **2,674,817** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p308 Japan annual year-on-year change rate of inter-municipal movers, all nationaliti = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p309 Japan annual year-on-year change rate of inter-municipal movers, all nationaliti = **-1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p310 Japan annual year-on-year change rate of inter-municipal movers, all nationaliti = **-0.9** % (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p311 Japan annual in-migrants from abroad (国外からの転入者数), 2024 = **735,883** person (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数 - - - - - 358,359 209,700 639,124 700,138 735,883 782,165"
  - p312 Japan annual out-migrants to abroad (国外への転出者数), 2024 = **371,615** person (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数 - - - - - 226,845 224,077 312,484 346,690 371,615 409,592"
  - p313 Japan national net social increase (社会増加数), 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "を上回ったこと等により、33万7234人の社会増加、前年に比べ5548人の拡大"
- `https://www.e-stat.go.jp/stat-search?page=1&layout=dataset&iroha=12&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tokyo.vivinavi.com/mc/prt/_wid_fbe5824ea65900b790e962f5b390117f85b2092525` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 15/15
  - p314 Japan total inter-municipal movers (市区町村間移動者数), calendar year 2025 = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p315 Year-on-year change in Japan total inter-municipal movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p316 Japan inter-prefectural movers (都道府県間移動者数), calendar year 2025 = **2,515,731** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p317 Year-on-year change in Japan inter-prefectural movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p318 In-migrants from abroad (国外からの転入者数), Japan, calendar year 2025 = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p319 Year-on-year change in in-migrants from abroad, Japan, 2025 vs 2024 = **6.3** % (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p320 Out-migrants to abroad (国外への転出者数), Japan, calendar year 2025 = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p321 Year-on-year change in out-migrants to abroad, Japan, 2025 vs 2024 = **10.2** % (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p322 National net social change (社会増減数), Japan, calendar year 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p323 Year-on-year expansion of national net social change, 2025 vs 2024 = **5,548** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p324 Net in-migration (転入超過) of the three major metropolitan areas combined, all nati = **119,581** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p325 Net in-migration (転入超過) of Tokyo area (東京圏), all nationalities, calendar year 20 = **123,534** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p326 Net in-migration (転入超過) of the three major metropolitan areas combined, Japanese = **110,680** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p327 Net in-migration (転入超過) of the three major metropolitan areas combined, foreign  = **8,901** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(外国人移動者)では8901人の転入超過、前年に比べ529人の拡大"
  - p328 Net in-migration (転入超過) of Tokyo area (東京圏), foreign movers only, calendar year  = **10,796** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は1万796人の転入超過、前年に比べ5710人の縮小"
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7; value_as_written not in quote as a whole number: 3)

### b2 [related_series] Foreign mover trend

Hypothesis: Foreign inter-municipal movers are the fastest-growing component (July 2026 +3.2% yoy, March 2026 +18.6%). An August 2025 foreign-mover value would let the component-sum route (Japanese + foreign) be built with a proper yoy scaling for each part, reducing reliance on the aggregate trend.

Queries issued by the searcher: 外国人移動者 市区町村間移動者数 2025年8月 人口移動報告; stat.go.jp 人口移動報告 外国人 月次 2025年8月; "302,070" 日本人移動者 市区町村間 2025年8月; "46,532" "302,070" 人口移動 2025年8月; site:stat.go.jp/data/idou/rireki/2508 外国人移動者 市区町村間 46532; 外国人移動者 市区町村間移動者数 2025年8月 人口移動報告; stat.go.jp 人口移動報告 外国人 月次 2025 市区町村間移動者数; "2025年（令和7年）8月結果" 住民基本台帳人口移動報告 外国人移動者の市区町村間移動者数; stat.go.jp idou rireki 2508 index.html 人口移動報告 8月結果; 外国人移動者 市区町村間移動者数 2025年8月 人口移動報告; stat.go.jp 住民基本台帳人口移動報告 2025年8月 外国人 日本人 移動者数; 住民基本台帳人口移動報告 2026年7月結果 外国人移動者 市区町村間移動者数; stat.go.jp idou rireki 2508 gaikyou 外国人移動者 市区町村間 46532

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/7
  - p329 Foreign inter-municipal movers (市区町村間移動者数), Japan, calendar year 2024 = **604,591** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p330 Foreign inter-municipal movers, year-on-year growth rate, Japan, 2025 = **9.5** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p331 Japanese inter-municipal movers, Japan, calendar year 2024 = **4,603,155** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p332 All residents (Japanese + foreign) inter-municipal movers, Japan, calendar year  = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p333 Foreign inter-municipal movers, Japan, calendar year 2023 = **566,677** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p334 Foreign inter-municipal movers, Japan, calendar year 2022 = **535,765** person (moves) (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
  - p335 Foreign inter-municipal movers, year-on-year growth rate, Japan, 2024 = **6.7** % (2024-01-01..2024-12-31) [keep: ] quote: "6 2024 604,591 348,385 256,206 6.7 7.8 5.2 269,932 149,331"
- `https://www.stat.go.jp/data/idou/rireki/2507/index.html` -> **snapshot** (snapshot 20260808220647); points raw/verified 15/15
  - p336 Total internal inter-municipal movers (all residents), Japan, July 2025 = **398,417** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p337 Japanese-resident internal inter-municipal movers, Japan, July 2025 = **345,172** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p338 Foreign-resident internal inter-municipal movers, Japan, July 2025 = **53,245** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p339 Year-on-year change in total inter-municipal movers, Japan, July 2025 = **6,371** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p340 Year-on-year percent change in total inter-municipal movers, Japan, July 2025 = **1.6** % (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p341 Year-on-year change in Japanese-resident inter-municipal movers, Japan, July 202 = **10,632** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p342 Year-on-year percent change in Japanese-resident inter-municipal movers, Japan,  = **3** % (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p343 Year-on-year change in foreign-resident inter-municipal movers, Japan, July 2025 = **4,261** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p344 Year-on-year percent change in foreign-resident inter-municipal movers, Japan, J = **8.7** % (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p345 Total internal inter-prefectural movers (all residents), Japan, July 2025 = **182,864** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p346 Total internal intra-prefectural movers (all residents), Japan, July 2025 = **215,553** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
  - p347 Japanese-resident inter-prefectural movers, Japan, July 2025 = **154,148** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p348 Japanese-resident intra-prefectural movers, Japan, July 2025 = **191,024** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p349 Foreign-resident inter-prefectural movers, Japan, July 2025 = **28,716** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p350 Foreign-resident intra-prefectural movers, Japan, July 2025 = **24,529** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&bunya_l=02&tstat=000000070001&cycle=7&tclass1=000001128855&result_` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.com/real_estate_news/n/n25ec427671d5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecitizen.jp/statdb/StatsData/0003423633` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?layout=dataset&iroha=40&toukei=00200523&statdisp_id=0004044330` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.kateikessan.co.jp/geocities/column30-188.html` -> **snapshot** (snapshot 20260314202102); points raw/verified 15/15
  - p351 Total internal inter-municipal movers (市区町村間移動者数), all residents, Japan, July 20 = **398,417** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p352 Japanese-resident internal inter-municipal movers (日本人移動者の市区町村間移動者数), Japan, Jul = **345,172** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p353 Foreign-resident internal inter-municipal movers (外国人移動者の市区町村間移動者数), Japan, July = **53,245** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p354 Year-on-year change in foreign-resident inter-municipal movers, Japan, July 2025 = **4,261** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p355 Year-on-year growth rate of foreign-resident inter-municipal movers, Japan, July = **8.7** % (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万3245人と、前年同月に比べ4261人(8.7%)増加。"
  - p356 Year-on-year change in Japanese-resident inter-municipal movers, Japan, July 202 = **10,632** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p357 Year-on-year change rate of Japanese-resident inter-municipal movers, Japan, Jul = **3** % (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は34万5172人と、前年同月に比べ1万632人(3.0%)減少。"
  - p358 Year-on-year change in total inter-municipal movers, Japan, July 2025 = **6,371** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p359 Year-on-year change rate of total inter-municipal movers, Japan, July 2025 = **1.6** % (2025-07-01..2025-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万8417人と、前年同月に比べ6371人(1.6%)減少。"
  - p360 Foreign-resident inter-prefectural movers (外国人移動者の都道府県間移動者数), Japan, July 2025 = **28,716** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は2万8716人と、前年同月に比べ2706人(10.4%)増加。"
  - p361 Foreign-resident intra-prefectural movers (外国人移動者の都道府県内移動者数), Japan, July 2025 = **24,529** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万4529人と、前年同月に比べ1555人(6.8%)増加。"
  - p362 Japanese-resident inter-prefectural movers (日本人移動者の都道府県間移動者数), Japan, July 2025 = **154,148** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万4148人と、前年同月に比べ7014人(4.4%)減少。"
  - p363 Japanese-resident intra-prefectural movers (日本人移動者の都道府県内移動者数), Japan, July 2025 = **191,024** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は19万1024人と、前年同月に比べ3618人 (1.9%)減少。"
  - p364 Total inter-prefectural movers, all residents, Japan, July 2025 = **182,864** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万2864人と、前年同月に比べ4308人(2.3%)減少。"
  - p365 Total intra-prefectural movers, all residents, Japan, July 2025 = **215,553** person (moves) (2025-07-01..2025-07-31) [keep: ] quote: "移動者の都道府県内移動者数は21万5553人と、前年同月に比べ2063人(0.9%)減少。"
- `https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000560` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (value_as_written not in quote as a whole number: 5; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### b3 [base_rates] Seasonal share of August

Hypothesis: The August share of the annual inter-municipal mover total (August / annual) would let the annual 2025 total (p13) be converted to an August level and then trended to 2026. This is a coverage/conversion factor that would complete the d2 route without needing a full monthly series.

Queries issued by the searcher: 人口移動報告 2023年 年間 市区町村間移動者数 8月; Statistics Bureau Report on Internal Migration in Japan Derived from Basic Resident Registration annual total 2023 monthly August; 住民基本台帳人口移動報告 2024年（令和6年）8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2024年結果 市区町村間移動者数 526万; 人口移動報告 2023年 8月 市区町村間移動者数 年間; 統計局 住民基本台帳人口移動報告 2023年 8月 市区町村間 転入 転出; Report on Internal Migration in Japan 2023 annual total inter-municipal movers August; 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2024年結果 市区町村間移動者数 520万; site:stat.go.jp/data/idou 2024 8月 市区町村間移動者数; 住民基本台帳人口移動報告 2024年 月別 8月 市区町村間移動者数; 住民基本台帳人口移動報告 2024年 年間 市区町村間移動者数 総数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月; stat.go.jp idou rireki 2508 住民基本台帳人口移動報告 2025年8月結果

- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 15/11
  - p366 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p367 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p368 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p369 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,310,972** person (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p370 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,247,744** person (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p371 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,255,721** person (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p372 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,403,465** person (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p373 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,359,174** person (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p374 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,318,617** person (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p375 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,251,717** person (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p376 Annual total inter-municipal movers (Japanese and foreign), Japan, calendar year = **5,384,553** person (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 15/15
  - p377 Annual inter-municipal movers (市区町村間移動者数), Japan, 2025 = **5,190,548** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p378 Annual inter-municipal movers (市区町村間移動者数), Japan, 2024 = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p379 Annual inter-municipal movers (市区町村間移動者数), Japan, 2023 = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p380 Annual inter-municipal movers (市区町村間移動者数), Japan, 2022 = **5,310,972** person (moves) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p381 Annual inter-municipal movers (市区町村間移動者数), Japan, 2021 = **5,247,744** person (moves) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p382 Annual inter-municipal movers (市区町村間移動者数), Japan, 2020 = **5,255,721** person (moves) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p383 Annual inter-municipal movers (市区町村間移動者数), Japan, 2019 = **5,403,465** person (moves) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p384 Annual inter-municipal movers (市区町村間移動者数), Japan, 2018 = **5,359,174** person (moves) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p385 Annual inter-municipal movers (市区町村間移動者数), Japan, 2017 = **5,318,617** person (moves) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p386 Annual inter-municipal movers (市区町村間移動者数), Japan, 2016 = **5,251,717** person (moves) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p387 Annual inter-municipal movers (市区町村間移動者数), Japan, 2015 = **5,384,553** person (moves) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p388 Year-on-year change in annual inter-municipal movers, Japan, 2025 = **-17,198** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p389 Year-on-year percent change in annual inter-municipal movers, Japan, 2025 = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p390 Annual inter-prefectural movers (都道府県間移動者数), Japan, 2025 = **2,515,731** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p391 Annual intra-prefectural movers (都道府県内移動者数), Japan, 2025 = **2,674,817** person (moves) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
- `https://www.stat.go.jp/data/idou/rireki/2308/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2024np/jissu/youyaku/index.htm` -> **snapshot** (snapshot 20251014222744); points raw/verified 15/15
  - p392 Japan internal inter-municipal movers, annual total 2024 (all persons, Japanese  = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "2024年の国内における市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p393 Japan internal inter-municipal movers, year-on-year change 2024 vs 2023 = **1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "2024年の国内における市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p394 Japan inter-prefectural movers, annual total 2024 = **2,523,249** person (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数は252万3249人となり、前年に比べ0.8%の減少"
  - p395 Japan in-migrants from abroad, annual total 2024 = **735,883** person (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数は73万5883人となり、前年に比べ5.1%の増加"
  - p396 Japan out-migrants to abroad, annual total 2024 = **371,615** person (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数は37万1615人となり、前年に比べ7.2%の増加"
  - p397 Japan national net social change (social increase), annual 2024 = **331,686** person (2024-01-01..2024-12-31) [keep: ] quote: "全国の社会増減数は、国外からの転入者数(73万5883人)が国外への転出者数(37万1615人)を上回ったこと等により、33万1686人の社会増加"
  - p398 Tokyo metropolitan area net in-migration (all persons), annual 2024 = **135,843** person (2024-01-01..2024-12-31) [keep: ] quote: "東京圏は13万5843人の転入超過、前年に比べ9328人の拡大"
  - p399 Three major metropolitan areas combined net in-migration (all persons), annual 2 = **119,666** person (2024-01-01..2024-12-31) [keep: ] quote: "3大都市圏全体では11万9666人の転入超過、前年に比べ1万2031人の拡大"
  - p400 Nagoya metropolitan area net out-migration (all persons), annual 2024 = **18,856** person (2024-01-01..2024-12-31) [keep: ] quote: "名古屋圏は1万8856人の転出超過、前年に比べ535人の拡大"
  - p401 Osaka metropolitan area net in-migration (all persons), annual 2024 = **2,679** person (2024-01-01..2024-12-31) [keep: ] quote: "大阪圏は2679人の転入超過。外国人を含む集計を開始した2014年以降、初めて転出超過から転入超過に転じる"
  - p402 Tokyo prefecture net social increase, annual 2024 = **140,548** person (2024-01-01..2024-12-31) [keep: ] quote: "社会増加となっているのは東京都(14万548人)、大阪府(4万9767人)、神奈川県(4万1916人)など20都道府県"
  - p403 Osaka prefecture net social increase, annual 2024 = **49,767** person (2024-01-01..2024-12-31) [keep: ] quote: "社会増加となっているのは東京都(14万548人)、大阪府(4万9767人)、神奈川県(4万1916人)など20都道府県"
  - p404 Kanagawa prefecture net social increase, annual 2024 = **41,916** person (2024-01-01..2024-12-31) [keep: ] quote: "社会増加となっているのは東京都(14万548人)、大阪府(4万9767人)、神奈川県(4万1916人)など20都道府県"
  - p405 Tokyo prefecture net in-migration (all persons), annual 2024 = **79,285** person (2024-01-01..2024-12-31) [keep: ] quote: "転入超過数は東京都が7万9285人と最も多く、最も拡大(1万1000人)"
  - p406 Three major metropolitan areas combined net in-migration (Japanese only), annual = **111,294** person (2024-01-01..2024-12-31) [keep: ] quote: "3大都市圏全体(日本人のみ)では11万1294人の転入超過、前年に比べ9843人の拡大"
- `https://www.stat.go.jp/data/idou/2023np/jissu/youyaku/index.htm` -> **snapshot** (snapshot 20260224182928); points raw/verified 15/15
  - p407 Japan inter-municipal movers (Japanese and foreign), annual total 2023 = **5,263,249** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "2023年の日本国内における市区町村間移動者数は526万3249人となり、前年に比べ0.9%の減少"
  - p408 Japan inter-municipal movers (Japanese and foreign), annual total 2022 (implied  = **0.9** % (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数は526万3249人。前年に比べ0.9%の減少"
  - p409 Japan inter-prefectural movers (Japanese and foreign), annual total 2023 = **2,544,639** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "都道府県間移動者数は254万4639人となり、前年に比べ0.3%の減少"
  - p410 Japan intra-prefectural movers (Japanese and foreign), annual total 2023 = **2,718,610** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "都道府県内移動者数は271万8610人となり、前年に比べ1.4%の減少"
  - p411 Japan inter-municipal movers, foreign nationals only, annual total 2023 = **566,677** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "2023年の日本国内における外国人の市区町村間移動者数は56万6677人となり、前年に比べ5.8%の増加"
  - p412 Japan inter-prefectural movers, foreign nationals only, annual total 2023 = **315,453** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "都道府県間移動者数は31万5453人となり、前年に比べ5.8%の増加"
  - p413 Japan intra-prefectural movers, foreign nationals only, annual total 2023 = **251,224** person (moves) (2023-01-01..2023-12-31) [keep: ] quote: "都道府県内移動者数は25万1224人となり、前年に比べ5.7%の増加"
  - p414 Tokyo metropolitan area net in-migration (Japanese and foreign), annual 2023 = **126,515** person (net in-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "東京圏は12万6515人の転入超過。前年に比べ2万6996人の拡大"
  - p415 Three major metropolitan areas combined net in-migration (Japanese and foreign), = **107,635** person (net in-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "3大都市圏全体では10万7635人の転入超過。前年に比べ2万6681人の拡大"
  - p416 Nagoya metropolitan area net out-migration (Japanese and foreign), annual 2023 = **18,321** person (net out-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "名古屋圏は1万8321人の転出超過。前年に比べ2103人の拡大"
  - p417 Osaka metropolitan area net out-migration (Japanese and foreign), annual 2023 = **559** person (net out-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "大阪圏は559人の転出超過。前年に比べ1788人の縮小"
  - p418 Tokyo metropolitan area net in-migration, Japanese movers only, annual 2023 = **114,802** person (net in-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "東京圏は11万4802人の転入超過。前年に比べ2万391人の拡大。28年連続の転入超過"
  - p419 Three major metropolitan areas combined net in-migration, Japanese movers only,  = **101,451** person (net in-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "3大都市圏全体では10万1451人の転入超過。前年に比べ2万4382人の拡大"
  - p420 Nagoya metropolitan area net out-migration, Japanese movers only, annual 2023 = **13,586** person (net out-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "名古屋圏は1万3586人の転出超過。前年に比べ123人の縮小。11年連続の転出超過"
  - p421 Osaka metropolitan area net in-migration, Japanese movers only, annual 2023 = **235** person (net in-migrants) (2023-01-01..2023-12-31) [keep: ] quote: "大阪圏は235人の転入超過。11年ぶりに転出超過から転入超過へ転じる"
- `https://www.stat.go.jp/data/idou/rireki/2408/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.soumu.go.jp/menu_news/s-news/01toukei03_01000127.html` -> **snapshot** (snapshot 20260119053207); points raw/verified 0/0
- `https://toshi-fudousan.or.jp/news2/tfk/2024.html` -> **snapshot** (snapshot 20260720091925); points raw/verified 8/8
  - p422 Japan internal inter-municipal movers, annual total 2024 (Basic Resident Registr = **5,207,746** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "2024年の国内における市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p423 Japan internal inter-municipal movers, year-on-year change 2024 vs 2023 = **1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数は520万7746人となり、前年に比べ1.1%の減少"
  - p424 Japan inter-prefectural movers, annual total 2024 = **2,523,249** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数は252万3249人となり、前年に比べ0.8%の減少"
  - p425 Japan inter-prefectural movers, year-on-year change 2024 vs 2023 = **0.8** % (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数は252万3249人となり、前年に比べ0.8%の減少"
  - p426 In-migrants from outside Japan, annual total 2024 = **735,883** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数は73万5883人となり、前年に比べ5.1%の増加"
  - p427 In-migrants from outside Japan, year-on-year change 2024 vs 2023 = **5.1** % (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数は73万5883人となり、前年に比べ5.1%の増加"
  - p428 Out-migrants to outside Japan, annual total 2024 = **371,615** person (moves) (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数は37万1615人となり、前年に比べ7.2%の増加"
  - p429 Out-migrants to outside Japan, year-on-year change 2024 vs 2023 = **7.2** % (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数は37万1615人となり、前年に比べ7.2%の増加"
- `https://www.stat.go.jp/data/idou/rireki/2308/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20240505135217); points raw/verified 15/0
- `https://www.e-stat.go.jp/stat-search/files?tstat=000000070001` -> **snapshot** (snapshot 20260807120118); points raw/verified 0/0
- dropped by code checks: 19 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 19)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august 2026 migration', 'resident registration moves']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p58', 'p59', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p106'] Same annual inter-municipal mover series (all nationalities) from the Statistics Bureau, repeated across snapshots. Values are consistent across vintages; these are redundant copies of one underlying 
- corroborating: ['p13', 'p43', 'p60', 'p146', 'p147', 'p158', 'p163', 'p200', 'p201'] 2025 annual total 5,190,548 and 2024 total 5,207,746 repeated across pages; one source, redundant.
- corroborating: ['p3', 'p14', 'p44', 'p68', 'p107'] Year-on-year change rates for annual totals; consistent with the level series.
- corroborating: ['p95', 'p96', 'p97', 'p120', 'p121', 'p122'] August 2024 = 355,918 and August 2023 = 379,493; the 2024 yoy change (-23,575, -6.2%) is internally consistent with these two levels. These are the key August anchors.
- corroborating: ['p100', 'p103', 'p125', 'p128'] Japanese + foreign August components sum to the August totals (313,909+42,009=355,918; 336,601+42,892=379,493). Confirms the component decomposition.
- corroborating: ['p159', 'p160', 'p203', 'p204'] 2025 Japanese 4,528,254 + foreign 662,294 = 5,190,548 total; consistent decomposition.
- corroborating: ['p131', 'p134', 'p137', 'p246', 'p249', 'p252'] July 2025 and July 2026 monthly totals with Japanese/foreign split; July 2026 (390,799) is the latest observed month and the strongest recent trend signal.
- corroborating: ['p219', 'p224', 'p228', 'p233', 'p238', 'p241'] 2026 monthly releases (Feb, Mar) show foreign movers growing strongly (+10% to +19%) while Japanese movers decline slightly; consistent with the July 2026 pattern.
- conflicting: ['p95', 'p120', 'p246'] August 2023 (379,493) to August 2024 (355,918) fell 6.2%, but July 2026 is only 1.9% below July 2025. The August 2024 dip may be a one-off; the recent trend suggests August 2026 closer to the 2025 lev
- corroborating: ['p199', 'p207', 'p208', 'p209'] Annual migration rate 4.17% and 2026 population 123.77M give a base-rate cross-check; foreign population 4.03M supports the growing foreign-mover component.
- corroborating: ['p28', 'p29', 'p30', 'p184', 'p185', 'p186'] Tokyo inter-municipal movers with Japanese/foreign split; consistent with national foreign-mover growth, but Tokyo is only a fraction of the national total.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p13', 'p43', 'p58', 'p59', 'p60', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p106', 'p146', 'p147', 'p148', 'p158', 'p163', 'p200', 'p201', 'p294', 'p295', 'p296', 'p304', 'p305', 'p306', 'p314', 'p332', 'p366', 'p367', 'p368', 'p369', 'p370', 'p371', 'p372', 'p373', 'p374', 'p375', 'p376', 'p377', 'p378', 'p379', 'p380', 'p381', 'p382', 'p383', 'p384', 'p385', 'p386', 'p387', 'p392', 'p407', 'p422'] All are the same annual inter-municipal mover total (all nationalities) from the Statistics Bureau annual release, repeated across many snapshots and mirrors. They agree exactly; they are one measurem
- corroborating: ['p95', 'p120', 'p131', 'p246', 'p219', 'p233'] Monthly all-nationality inter-municipal mover counts from the same monthly report, different months/years. Same definition and publisher; they form the only genuine monthly series available. p95 (Aug 
- corroborating: ['p100', 'p103', 'p125', 'p128', 'p134', 'p137', 'p249', 'p252', 'p224', 'p228', 'p238', 'p241'] Japanese/foreign split of monthly inter-municipal movers. Within each month the two components sum to the total (e.g. p100+p103=p95; p249+p252=p246), so they are internally consistent but not independ
- corroborating: ['p159', 'p160', 'p203', 'p204', 'p297', 'p299', 'p331', 'p329', 'p298', 'p300', 'p205', 'p110', 'p333', 'p334'] Annual Japanese-only and foreign-only inter-municipal mover totals. Japanese component declining (~-1.6%/yr), foreign component growing fast (+9.5% in 2025, +6.7% in 2024, +5.8% in 2023). Consistent w
- corroborating: ['p199', 'p207', 'p208', 'p209'] Migration rate (4.17%/yr) and population stocks (total 123.77m, Japanese 119.74m, foreign 4.03m as of 2026-01-01). p207 = p208 + p209 exactly. These give a base-rate route; the annual rate must be con
- corroborating: ['p28', 'p29', 'p30', 'p184', 'p185', 'p186'] Tokyo-to inter-municipal movers, total/Japanese/foreign, 2025. Same definition family but a single prefecture; useful only as a cross-check on the national Japanese/foreign growth split, not as a nati
- corroborating: ['p3', 'p14', 'p44', 'p68', 'p107', 'p303', 'p308', 'p309', 'p310', 'p315', 'p388', 'p389', 'p393', 'p408', 'p423'] Year-on-year change rates for annual totals. Note sign convention: p3/p14/p44/p315 state '0.3% decrease' (i.e. -0.3%), while p303/p308/p389 give -0.3 directly. Same underlying figure; do not mix a 'de
- corroborating: ['p96', 'p97', 'p121', 'p122', 'p265', 'p266', 'p280', 'p281', 'p339', 'p340', 'p358', 'p359'] Yoy changes accompanying the monthly totals; redundant with the levels but confirm the direction (Aug 2023 -5.6%, Aug 2024 -6.2%, Jul 2025 -1.6%, Jul 2026 -1.9%).
- corroborating: ['p246', 'p279', 'p249', 'p282', 'p252', 'p285'] July 2026 monthly figures (total, Japanese, foreign) — the most recent observed month before cutoff, published 2026-08-27. This is the key yoy signal for August 2026.
- corroborating: ['p219', 'p224', 'p228', 'p233', 'p238', 'p241'] March and February 2026 monthly figures; show foreign movers growing strongly (+18.6% March, +10.0% February) while Japanese decline modestly. Supports the foreign growth assumption.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 yoy change factor for Japanese inter-municipal movers vs August 2025 | 0.975 | 0.93..1.02 | 0.8711..1.089 (widened) | 1 | m2 (m2) | Japanese movers have declined steadily: July 2026 -2.7% yoy (p284), July 2025 -3.0% (p269), March 2026 -0.6% (p224), February 2026 -1.5% (p238), annual 2025 -1.6% (p159). A factor near 0.975 (about -2.5%) with a wide band reflects this persistent mild decline. | Japanese-resident inter-municipal mover counts follow the same mild declining trend into August 2026 as in the preceding months. | A July/August 2026 Japanese mover figure showing growth or a much steeper decline than -3%. |
| a2 | August 2026 yoy change factor for foreign inter-municipal movers vs August 2025 | 1.05 | 0.98..1.15 | 0.9495..1.187 (widened) | 1 | m2 (m2) | Foreign movers grew +3.2% in July 2026 (p287), +18.6% in March 2026 (p228), +10.0% in February 2026 (p241), +9.5% annual 2025 (p160). Growth has decelerated recently, so a factor near 1.05 with a wide band is used rather than the higher annual rate. | Foreign-resident mover growth continues at a modest positive rate into August 2026. | A July/August 2026 foreign mover figure showing decline or renewed double-digit growth. |
| a3 | August seasonality factor: August monthly movers relative to the annual monthly average | 0.92 | 0.85..1 | 0.6519..1.304 (widened) | 1 | m3 (m3) | August is a low-migration month in Japan (Obon, school-year moves concentrated in March-April). August 2024 total was 355,918 (p95) vs annual 2024 5,207,746 (p2), i.e. about 0.82 of the monthly average; August 2023 379,493 (p120) vs 5,263,249 (p1) about 0.87. A factor near 0.92 with a band covers th | The August share of annual movers in 2026 is similar to 2023-2024. | Evidence that August 2026 has an unusually high or low share of annual moves. |
| a4 | August 2026 total inter-municipal movers as a factor of August 2024 level (two-year change) | 0.96 | 0.9..1.03 | 0.8612..1.076 (widened) | 1 | m1 (m1) | Replaces the rejected yoy_scaling route. The only observed August levels are 2023 (p120) and 2024 (p95); no August 2025 value is kept, so the target must be bridged from August 2024 across two years. Annual totals fell 0.3% in 2025 (p315) and July 2026 was -1.9% yoy (p281), July 2025 -1.6% (p340); c | The mild national decline in inter-municipal movers observed in 2025 and mid-2026 continues through August 2026. | Evidence of a sharp August 2026 deviation (e.g. a policy change in foreign registration or a large rebound) relative to the 2024-2026 trend. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 342,239 | ['p95'] / ['a4'] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 351,251 | ['p100', 'p103'] / ['a1', 'a2'] | [] |  | 1.00 | B2 of 3 blocks; median of blocks: this block is the median |  |
| m3 | formula_mc | 396,538 | ['p199', 'p207'] / ['a3'] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of Japanese, foreign
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p95 * a4; Monte Carlo P10 to P90 276,796 to 424,094; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p100 * a1 + p103 * a2; Monte Carlo P10 to P90 291,665 to 424,498; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p199 * p207 / k_months_per_year * a3; Monte Carlo P10 to P90 256,983 to 614,615; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.55 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 342,239 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 351,251 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 396,538 (width x/÷1.55, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.44; Birge ratio 0.25 (not above one, so no widening); final width x/÷1.44.

Result: central **351,251** person, 80% interval [244,316, 504,989] person, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

Unit of the estimate: person (person (moves); total for 2026-08-01 to 2026-08-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 351,251 person (80% model-based interval 244,316 to 504,989 person) for internal migration events between municipalities within Japan, all residents combined, for August 2026, as would first appear in the Statistics Bureau's monthly Report on Internal Migration. The central route sums observed August 2024 Japanese movers (313,909 person (moves)) and foreign movers (42,009 person (moves)), each scaled by an assumed two-year change factor (0.975 and 1.05). Alternative routes carry the observed August 2024 total (355,918 person (moves)) forward with 0.96, or apply the observed annual rate (4.17%) to population (123,767,642 person) with an August seasonality factor (0.92). Only the 2024 levels, rate and population are observed; every bridge to 2026 is an assumption. Code combined the three routes as equal-weight blocks and took the median, with no backtest evidence to set weights. The main risk is that the two-year factors must absorb both years of change, and August-specific shocks are unobserved. The most useful missing evidence is an actual August 2025 figure.

Unit of the estimate: person (person (moves); total for 2026-08-01 to 2026-08-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 yoy change factor for Japanese inter-municipal movers vs August 2025: 0.975 [n], range 0.8711 to 1.089 (range widened by code); used by m2. Overturned by: A July/August 2026 Japanese mover figure showing growth or a much steeper decline than -[n].
- a2 August 2026 yoy change factor for foreign inter-municipal movers vs August 2025: 1.05 [n], range 0.9495 to 1.187 (range widened by code); used by m2. Overturned by: A July/August 2026 foreign mover figure showing decline or renewed double-digit growth.
- a3 August seasonality factor: August monthly movers relative to the annual monthly average: 0.92 [n], range 0.6519 to 1.304 (range widened by code); used by m3. Overturned by: Evidence that August 2026 has an unusually high or low share of annual moves.
- a4 August 2026 total inter-municipal movers as a factor of August 2024 level (two-year change): 0.96 [n], range 0.8612 to 1.076 (range widened by code); used by m1. Overturned by: Evidence of a sharp August 2026 deviation (e.g. a policy change in foreign registration or a large rebound) relative to the 2024-2026 trend.

Method details (computed by code):
- m1 formula_mc: p95 * a4; Monte Carlo P10 to P90 276,796 to 424,094; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p100 * a1 + p103 * a2; Monte Carlo P10 to P90 291,665 to 424,498; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p199 * p207 / k_months_per_year * a3; Monte Carlo P10 to P90 256,983 to 614,615; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.55 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 342,239 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 351,251 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 396,538 (width x/÷1.55, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.44; Birge ratio 0.25 (not above one, so no widening); final width x/÷1.44.

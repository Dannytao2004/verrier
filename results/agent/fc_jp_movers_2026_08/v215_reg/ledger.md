# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of persons who changed their municipality of residence within Japan (domestic inter-municipal moves, Japanese and foreign residents combined), counted as migration events reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident | unit person (migration events, one per mover per move) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan, Ministry of Internal Affairs and Communications (総務省統計局)

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau time series

Hypothesis: August internal migration totals follow a stable seasonal pattern (August is typically a high-move month due to summer/relocation season). Prior August values (2019-2025) plus the recent monthly trend give the base level; the target equals last observed August level adjusted for trend growth.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 移動者数 総務省統計局; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 時系列表 市区町村間移動者数 月別 2018年 統計局; 統計メールニュース 2026年 住民基本台帳人口移動報告 6月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月 移動者数; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 統計局 人口移動報告 時系列表 市区町村間移動者数 月別 2018年 2019年 8月; 住民基本台帳人口移動報告 2025年8月 移動者数; Report on Internal Migration in Japan August 2025 total moves Statistics Bureau; 住民基本台帳人口移動報告 2026年（令和8年）7月結果 市区町村間移動者数; 統計メールニュース 2026.8 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 29/22
  - p1 Annual domestic inter-municipal movers, Japan, 2025 (all residents) = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p2 Annual domestic inter-municipal movers, Japan, 2024 (all residents) = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p3 Annual domestic inter-municipal movers, Japan, 2023 (all residents) = **5,263,249** person (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p4 Annual domestic inter-municipal movers, Japan, 2022 (all residents) = **5,310,972** person (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p5 Annual domestic inter-municipal movers, Japan, 2021 (all residents) = **5,247,744** person (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p6 Annual domestic inter-municipal movers, Japan, 2020 (all residents) = **5,255,721** person (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p7 Annual domestic inter-municipal movers, Japan, 2019 (all residents) = **5,403,465** person (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p8 Annual domestic inter-municipal movers, Japan, 2018 (all residents) = **5,359,174** person (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p9 Annual domestic inter-municipal movers, Japan, 2017 (all residents) = **5,318,617** person (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p10 Annual domestic inter-municipal movers, Japan, 2016 (all residents) = **5,251,717** person (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p11 Annual domestic inter-municipal movers, Japan, 2015 (all residents) = **5,384,553** person (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p12 Year-on-year change in annual domestic inter-municipal movers, Japan, 2025 = **-17,198** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 176,954 -132,836 66,900 40,557 44,291 -147,744 -7,977 63,228 -47,723 -55,503 -17,198"
  - p13 Year-on-year percent change in annual domestic inter-municipal movers, Japan, 20 = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p14 Year-on-year percent change in annual domestic inter-municipal movers, Japan, 20 = **-1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p15 Annual intra-prefectural inter-municipal movers, Japan, 2025 (all residents) = **2,674,817** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p16 Annual intra-prefectural inter-municipal movers, Japan, 2024 (all residents) = **2,684,497** person (2024-01-01..2024-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p17 Annual inter-prefectural movers, Japan, 2024 (all residents) = **2,523,249** person (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p18 Annual net social increase, Japan, 2025 = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p19 In-migrants, three major metropolitan areas, 2025 (Japanese movers) = **754,602** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数 813,906 795,328 796,693 808,772 816,306 767,651 751,990 766,689 777,968 769,772 754,602"
  - p20 Out-migrants, three major metropolitan areas, 2025 (Japanese movers) = **643,922** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数 704,993 689,158 690,718 688,519 686,102 683,039 688,293 689,620 676,517 658,478 643,922"
  - p21 In-migrants, three major metropolitan areas, 2024 (Japanese movers) = **769,772** person (2024-01-01..2024-12-31) [keep: ] quote: "転入者数 813,906 795,328 796,693 808,772 816,306 767,651 751,990 766,689 777,968 769,772 754,602"
  - p22 Out-migrants, three major metropolitan areas, 2024 (Japanese movers) = **658,478** person (2024-01-01..2024-12-31) [keep: ] quote: "転出者数 704,993 689,158 690,718 688,519 686,102 683,039 688,293 689,620 676,517 658,478 643,922"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://datainsight.x.ezic.info/japan-residential-mobility-trend-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html` -> **snapshot** (snapshot 20260510081517); points raw/verified 29/29
  - p23 Japan domestic inter-municipal movers (total internal migration), 2025 annual = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p24 Year-on-year change in Japan domestic inter-municipal movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p25 Japan inter-prefectural movers, 2025 annual = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p26 Year-on-year change in Japan inter-prefectural movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p27 In-migrants from abroad to Japan, 2025 annual = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p28 Year-on-year change in in-migrants from abroad, 2025 vs 2024 = **6.3** % (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p29 Out-migrants to abroad from Japan, 2025 annual = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p30 Year-on-year change in out-migrants to abroad, 2025 vs 2024 = **10.2** % (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
  - p31 Japan national net social change (social increase), 2025 annual = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p32 Year-on-year expansion of Japan national net social increase, 2025 vs 2024 = **5,548** person (2025-01-01..2025-12-31) [keep: ] quote: "33万7234人の社会増加、前年に比べ5548人の拡大"
  - p33 Tokyo metropolitan area net in-migration (all movers), 2025 annual = **123,534** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p34 Year-on-year change in Tokyo metropolitan area net in-migration (all movers), 20 = **12,309** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年に比べ1万2309人の縮小"
  - p35 Three major metropolitan areas combined net in-migration (all movers), 2025 annu = **119,581** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p36 Year-on-year change in three major metropolitan areas combined net in-migration  = **85** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体では11万9581人の転入超過、前年に比べ85人の縮小"
  - p37 Nagoya metropolitan area net out-migration (all movers), 2025 annual = **12,695** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は1万2695人の転出超過、前年に比べ6161人の縮小"
  - p38 Osaka metropolitan area net in-migration (all movers), 2025 annual = **8,742** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は8742人の転入超過、前年に比べ6063人の拡大"
  - p39 Three major metropolitan areas combined net in-migration (Japanese movers only), = **110,680** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p40 Tokyo metropolitan area net in-migration (Japanese movers only), 2025 annual = **112,738** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は11万2738人の転入超過、前年に比べ6599人の縮小。30年連続の転入超過"
  - p41 Nagoya metropolitan area net out-migration (Japanese movers only), 2025 annual = **9,561** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は9561人の転出超過、前年に比べ1956人の縮小。13年連続の転出超過"
  - p42 Osaka metropolitan area net in-migration (Japanese movers only), 2025 annual = **7,503** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は7503人の転入超過、前年に比べ4029人の拡大。3年連続の転入超過"
  - p43 Three major metropolitan areas combined net in-migration (foreign movers only),  = **8,901** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(外国人移動者)では8901人の転入超過、前年に比べ529人の拡大"
  - p44 Tokyo metropolitan area net in-migration (foreign movers only), 2025 annual = **10,796** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は1万796人の転入超過、前年に比べ5710人の縮小"
  - p45 Nagoya metropolitan area net out-migration (foreign movers only), 2025 annual = **3,134** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は3134人の転出超過、前年に比べ4205人の縮小"
  - p46 Osaka metropolitan area net in-migration (foreign movers only), 2025 annual = **1,239** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は1239人の転入超過、3年ぶりに転出超過から転入超過へ転じている"
  - p47 Tokyo prefecture net social increase, 2025 annual = **125,457** person (2025-01-01..2025-12-31) [keep: ] quote: "社会増加となっているのは東京都(12万5457人)、大阪府(5万8524人)、千葉県(4万2629人)など23都道府県"
  - p48 Osaka prefecture net social increase, 2025 annual = **58,524** person (2025-01-01..2025-12-31) [keep: ] quote: "社会増加となっているのは東京都(12万5457人)、大阪府(5万8524人)、千葉県(4万2629人)など23都道府県"
  - p49 Chiba prefecture net social increase, 2025 annual = **42,629** person (2025-01-01..2025-12-31) [keep: ] quote: "社会増加となっているのは東京都(12万5457人)、大阪府(5万8524人)、千葉県(4万2629人)など23都道府県"
  - p50 Tokyo prefecture net in-migration (all movers), 2025 annual = **65,219** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数は東京都が6万5219人と最も多く、神奈川県が最も拡大(1089人)"
  - p51 Aichi prefecture largest expansion of net social increase, 2025 annual = **9,298** person (2025-01-01..2025-12-31) [keep: ] quote: "社会増加数が最も拡大しているのは愛知県(9298人)"
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 27/27
  - p52 Total inter-municipal movers (Japanese and foreign combined), July 2026, Japan = **390,799** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p53 Year-on-year change in total inter-municipal movers, July 2026 vs July 2025, Jap = **7,618** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p54 Year-on-year percent change in total inter-municipal movers, July 2026 vs July 2 = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p55 Total inter-prefectural movers (Japanese and foreign combined), July 2026, Japan = **181,604** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p56 Year-on-year change in total inter-prefectural movers, July 2026 vs July 2025, J = **1,260** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p57 Year-on-year percent change in total inter-prefectural movers, July 2026 vs July = **0.7** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p58 Total intra-prefectural movers (Japanese and foreign combined), July 2026, Japan = **209,195** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p59 Year-on-year change in total intra-prefectural movers, July 2026 vs July 2025, J = **6,358** person (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p60 Year-on-year percent change in total intra-prefectural movers, July 2026 vs July = **2.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p61 Japanese inter-municipal movers, July 2026, Japan = **335,854** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p62 Year-on-year change in Japanese inter-municipal movers, July 2026 vs July 2025,  = **9,318** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p63 Year-on-year percent change in Japanese inter-municipal movers, July 2026 vs Jul = **2.7** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p64 Japanese inter-prefectural movers, July 2026, Japan = **150,347** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p65 Year-on-year change in Japanese inter-prefectural movers, July 2026 vs July 2025 = **3,801** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p66 Year-on-year percent change in Japanese inter-prefectural movers, July 2026 vs J = **2.5** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p67 Japanese intra-prefectural movers, July 2026, Japan = **185,507** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p68 Year-on-year change in Japanese intra-prefectural movers, July 2026 vs July 2025 = **5,517** person (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p69 Year-on-year percent change in Japanese intra-prefectural movers, July 2026 vs J = **2.9** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p70 Foreign inter-municipal movers, July 2026, Japan = **54,945** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p71 Year-on-year change in foreign inter-municipal movers, July 2026 vs July 2025, J = **1,700** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p72 Year-on-year percent change in foreign inter-municipal movers, July 2026 vs July = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p73 Foreign inter-prefectural movers, July 2026, Japan = **31,257** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p74 Year-on-year change in foreign inter-prefectural movers, July 2026 vs July 2025, = **2,541** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p75 Year-on-year percent change in foreign inter-prefectural movers, July 2026 vs Ju = **8.8** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p76 Foreign intra-prefectural movers, July 2026, Japan = **23,688** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
  - p77 Year-on-year change in foreign intra-prefectural movers, July 2026 vs July 2025, = **841** person (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
  - p78 Year-on-year percent change in foreign intra-prefectural movers, July 2026 vs Ju = **3.4** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.stat.go.jp/data/idou/sankouhyo.htm` -> **snapshot** (snapshot 20171120235944); points raw/verified 0/0
- dropped by code checks: 7 (value_as_written not in quote as a whole number: 4; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d2 [related_series] Population stock and migration rate

Hypothesis: Total moves = population × monthly gross migration rate. Japan's population (~123-124 million) times an August-specific gross move rate (~0.35-0.45% per month) yields the total; the rate can be derived from prior-year August moves divided by prior-year population.

Queries issued by the searcher: 住民基本台帳人口移動報告 2025年8月 転入 転出 移動者数; Report on Internal Migration in Japan Derived from the Basic Resident Registration August 2025 Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 人口推計 2026年 総務省統計局 総人口 2025年10月1日; 住民基本台帳人口移動報告 2025年8月 転入 転出 移動者数; Statistics Bureau Report on Internal Migration in Japan August 2025 total moves persons; 人口推計 2025年 総人口 1億2330万人 総務省統計局; 住民基本台帳人口 2026年1月1日 総人口 123 万人; 住民基本台帳 人口 2025年 総人口 1億2000万人 統計局; 住民基本台帳人口移動報告 2025年8月 転入 転出 移動者数; stat.go.jp 住民基本台帳人口移動報告 2024年8月結果 市区町村間移動者数 35万; nikkei 日本人の人口1億2000万人割れ 住民基本台帳 2026年1月1日 総人口 1億2376万7642人

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 29/28
  - p79 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2025 = **5,190,548** person (migration events) (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p80 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2024 = **5,207,746** person (migration events) (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p81 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2023 = **5,263,249** person (migration events) (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p82 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2022 = **5,310,972** person (migration events) (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p83 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2021 = **5,247,744** person (migration events) (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p84 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2020 = **5,255,721** person (migration events) (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p85 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2019 = **5,403,465** person (migration events) (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p86 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2018 = **5,359,174** person (migration events) (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p87 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2017 = **5,318,617** person (migration events) (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p88 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2016 = **5,251,717** person (migration events) (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p89 Japan domestic inter-municipal movers (市区町村間移動者数), annual total, 2015 = **5,384,553** person (migration events) (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p90 Japan inter-prefectural movers (都道府県間移動者数), annual total, 2025 = **2,515,731** person (migration events) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人となり、前年に比べ0.3%の減少"
  - p91 Japan intra-prefectural inter-municipal movers (都道府県内移動者数), annual total, 2025 = **2,674,817** person (migration events) (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p92 Japan inter-prefectural movers (都道府県間移動者数), annual total, 2024 = **2,523,249** person (migration events) (2024-01-01..2024-12-31) [keep: ] quote: "都道府県間移動者数 2,502,780 2,460,346 2,505,064 2,535,601 2,568,086 2,463,992 2,476,640 2,553,434 2,544,639 2,523,249 2,515,731"
  - p93 Japan intra-prefectural inter-municipal movers (都道府県内移動者数), annual total, 2024 = **2,684,497** person (migration events) (2024-01-01..2024-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p94 Year-on-year change rate of Japan domestic inter-municipal movers, 2025 vs 2024 = **-0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p95 Year-on-year change rate of Japan domestic inter-municipal movers, 2024 vs 2023 = **-1.1** % (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p96 Year-on-year change rate of Japan domestic inter-municipal movers, 2023 vs 2022 = **-0.9** % (2023-01-01..2023-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p97 Year-on-year change rate of Japan domestic inter-municipal movers, 2022 vs 2021 = **1.2** % (2022-01-01..2022-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p98 Year-on-year change rate of Japan domestic inter-municipal movers, 2021 vs 2020 = **-0.2** % (2021-01-01..2021-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p99 Year-on-year change rate of Japan domestic inter-municipal movers, 2020 vs 2019 = **-2.7** % (2020-01-01..2020-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p100 Year-on-year change rate of Japan domestic inter-municipal movers, 2019 vs 2018 = **0.8** % (2019-01-01..2019-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p101 Year-on-year change rate of Japan domestic inter-municipal movers, 2018 vs 2017 = **0.8** % (2018-01-01..2018-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p102 Year-on-year change rate of Japan domestic inter-municipal movers, 2017 vs 2016 = **1.3** % (2017-01-01..2017-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p103 Year-on-year change rate of Japan domestic inter-municipal movers, 2016 vs 2015 = **-2.5** % (2016-01-01..2016-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p104 Year-on-year change rate of Japan domestic inter-municipal movers, 2015 vs 2014 = **3.4** % (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 3.4 -2.5 1.3 0.8 0.8 -2.7 -0.2 1.2 -0.9 -1.1 -0.3"
  - p105 Japan in-migrants from abroad (国外からの転入者数), annual total, 2025 = **782,165** person (migration events) (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人となり、前年に比べ6.3%の増加"
  - p106 Japan out-migrants to abroad (国外への転出者数), annual total, 2025 = **409,592** person (migration events) (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人となり、前年に比べ10.2%の増加"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?kana=11&toukei=00200523&result_page=1&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.toukei.metro.tokyo.lg.jp/jidou/2025/ji-point.pdf` -> **snapshot** (snapshot 20260718032106); points raw/verified 30/30
  - p107 Tokyo inter-municipal movers (区市町村間移動者数), total Japanese and foreign, 2025 = **1,317,064** person (2025-01-01..2025-12-31) [keep: ] quote: "令和7年における東京都の区市町村間移動者数は 1,317,064 人で、前年比 6,596 人(△0.5%)減"
  - p108 Tokyo inter-municipal movers, Japanese only, 2025 = **1,116,080** person (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人の区市町村間移動者数は 1,116,080 人で、前年比 20,233 人(△1.8%)減"
  - p109 Tokyo inter-municipal movers, foreign residents only, 2025 = **200,984** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人の区市町村間移動者数は 200,984 人で、前年比 13,637 人(7.3%)増"
  - p110 Tokyo year-on-year change in total inter-municipal movers, 2025 vs 2024 = **6,596** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p111 Tokyo year-on-year percent change in total inter-municipal movers, 2025 vs 2024 = **0.5** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p112 Tokyo movers between prefectures (他道府県間), total, 2025 = **838,467** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p113 Tokyo movers between prefectures, Japanese only, 2025 = **730,373** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p114 Tokyo movers between prefectures, foreign residents only, 2025 = **108,094** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p115 Tokyo movers within Tokyo (都内間), total, 2025 = **465,145** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p116 Tokyo movers within Tokyo, Japanese only, 2025 = **384,882** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p117 Tokyo movers within Tokyo, foreign residents only, 2025 = **80,263** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p118 Tokyo other movers (previous address unknown), total, 2025 = **13,452** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p119 Tokyo other movers (previous address unknown), Japanese only, 2025 = **825** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p120 Tokyo other movers (previous address unknown), foreign residents only, 2025 = **12,627** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p121 Tokyo in-migrants from other prefectures (転入者数), total, 2025 = **451,843** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数は 451,843 人"
  - p122 Tokyo in-migrants from other prefectures, Japanese only, 2025 = **397,985** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 397,985 人、外国人 53,858 人)"
  - p123 Tokyo in-migrants from other prefectures, foreign residents only, 2025 = **53,858** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 397,985 人、外国人 53,858 人)"
  - p124 Tokyo out-migrants to other prefectures (転出者数), total, 2025 = **386,624** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数は 386,624 人"
  - p125 Tokyo out-migrants to other prefectures, Japanese only, 2025 = **332,388** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 332,388 人、外国人 54,236 人)"
  - p126 Tokyo out-migrants to other prefectures, foreign residents only, 2025 = **54,236** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 332,388 人、外国人 54,236 人)"
  - p127 Tokyo net in-migration from other prefectures (転入超過数), total, 2025 = **65,219** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数(転入者数-転出者数)は 65,219 人"
  - p128 Tokyo net in-migration from other prefectures, Japanese only, 2025 = **65,597** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p129 Tokyo net migration from other prefectures, foreign residents only, 2025 = **378** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p130 Tokyo net in-migration from other prefectures, year-on-year change, 2025 vs 2024 = **14,066** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 14,066 人減"
  - p131 Tokyo movers between wards (区相互間), total, 2025 = **306,398** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p132 Tokyo movers between wards, Japanese only, 2025 = **243,036** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p133 Tokyo movers between wards, foreign residents only, 2025 = **63,362** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p134 Tokyo movers between ward area and municipal area (区部と市町村部間), total, 2025 = **95,674** person (2025-01-01..2025-12-31) [keep: ] quote: "区部と市町村部間: 95,674 人(日本人 83,834 人、外国人 11,840 人)"
  - p135 Tokyo movers between municipalities (市町村相互間), total, 2025 = **63,073** person (2025-01-01..2025-12-31) [keep: ] quote: "市町村相互間: 63,073 人(日本人 58,012 人、外国人 5,061 人)"
  - p136 Tokyo net in-migration, age 20-24, 2025 = **57,263** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数の最も多い年齢階級は20~24歳の57,263人、次いで25~29歳の20,642人、15~19歳の12,944人"
- `https://www.e-stat.go.jp/en/stat-search?page=1&iroha=30&toukei=00200523&layout=dataset` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250826_no1788.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp-newsfocus.com/foreign-resident-interprefectural-moves-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&toukei=00200523&stat_infid=000040491278&iroha=12` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d3 [forecasts_markets] Official projections and demographic forecasts

Hypothesis: IPSS or Statistics Bureau population projections and any published 2026 monthly estimates before cutoff indicate the level and direction of internal migration; these anchor the trend adjustment applied to the prior August base.

Queries issued by the searcher: 人口移動報告 2026年 月次 公表 統計局; 統計局 住民基本台帳人口移動報告 2026年 速報; stat.go.jp/data/idou/rireki/2607 2026年7月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月; 人口移動報告 2026年 月次 公表 総務省統計局; 統計局 住民基本台帳人口移動報告 2025年 年間 転入 転出; "2025年（令和7年）8月結果" 市区町村間移動者数 住民基本台帳人口移動報告; 統計局ホームページ 住民基本台帳人口移動報告 2026年6月結果 市区町村間移動者数; 人口移動報告 2026年 月次 公表 総務省統計局; 住民基本台帳人口移動報告 2026年 1月 転入 転出 都道府県; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数 39万799人; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 前年同月

- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260227_no1840.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 29/29
  - p137 Inter-municipal movers (市区町村間移動者数), all residents, Japan, October 2025 = **379,751** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p138 Inter-municipal movers, all residents, Japan, October 2024 = **378,202** person (migration events) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p139 Year-on-year change in inter-municipal movers, all residents, Japan, October 202 = **1,549** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p140 Year-on-year rate of change in inter-municipal movers, all residents, Japan, Oct = **0.4** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p141 Inter-municipal movers, Japanese residents, Japan, October 2025 = **321,850** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 32万1850人。前年同月に比べ減少 ▲ 4933人( ▲ 1.5%)"
  - p142 Inter-municipal movers, Japanese residents, Japan, October 2024 = **326,783** person (migration events) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p143 Inter-municipal movers, foreign residents, Japan, October 2025 = **57,901** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数は 5万7901人。前年同月に比べ増加 6482人( 12.6%)"
  - p144 Inter-municipal movers, foreign residents, Japan, October 2024 = **51,419** person (migration events) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p145 Inter-prefectural movers, all residents, Japan, October 2025 = **168,057** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 16万8057人。前年同月に比べ増加 950人( 0.6%)"
  - p146 Intra-prefectural movers, all residents, Japan, October 2025 = **211,694** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 21万1694人。前年同月に比べ増加 599人( 0.3%)"
  - p147 Inter-prefectural movers, Japanese residents, Japan, October 2025 = **137,348** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 13万7348人。前年同月に比べ減少 ▲ 3197人( ▲ 2.3%)"
  - p148 Intra-prefectural movers, Japanese residents, Japan, October 2025 = **184,502** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 18万4502人。前年同月に比べ減少 ▲ 1736人( ▲ 0.9%)"
  - p149 Inter-prefectural movers, foreign residents, Japan, October 2025 = **307,090,000** as written "3万 709", value check pending person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数は 3万 709人。前年同月に比べ増加 4147人( 15.6%)"
  - p150 Intra-prefectural movers, foreign residents, Japan, October 2025 = **27,192** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数は 2万7192人。前年同月に比べ増加 2335人( 9.4%)"
  - p151 Inter-prefectural in-migrants, all Japan total (sum of prefectural in-migrants), = **168,057** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p152 Inter-prefectural in-migrants, all Japan total, October 2024 = **167,107** person (migration events) (2024-10-01..2024-10-31) [keep: ] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p153 Tokyo metropolitan area (東京圏) in-migrants, all movers, October 2025 = **29,721** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p154 Tokyo metropolitan area (東京圏) net in-migration (転入超過数), all movers, October 2025 = **2,885** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p155 Nagoya metropolitan area (名古屋圏) net in-migration (転入超過数), all movers, October 20 = **-735** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p156 Osaka metropolitan area (大阪圏) net in-migration (転入超過数), all movers, October 2025 = **778** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p157 21 major cities total in-migrants, all movers, October 2025 = **93,597** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
  - p158 21 major cities total out-migrants, all movers, October 2025 = **93,543** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
  - p159 21 major cities total net in-migration (転入超過数), all movers, October 2025 = **54** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
  - p160 Tokyo 23 special wards (東京都特別区部) in-migrants, all movers, October 2025 = **25,953** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東京都特別区部 25,953 26,558 -605 -2.3 27,055 25,862 1,193 4.6 -1,102 696"
  - p161 Tokyo 23 special wards (東京都特別区部) net in-migration (転入超過数), all movers, October 2 = **-1,102** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東京都特別区部 25,953 26,558 -605 -2.3 27,055 25,862 1,193 4.6 -1,102 696"
  - p162 Tokyo prefecture (東京都) in-migrants, all movers, October 2025 = **29,182** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p163 Tokyo prefecture (東京都) net in-migration (転入超過数), all movers, October 2025 = **227** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p164 Tokyo metropolitan area (東京圏) in-migrants, Japanese movers, October 2025 = **24,469** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 24,469 22,650 1,819 6,843 7,005 -162 11,727 11,201 526"
  - p165 Tokyo metropolitan area (東京圏) net in-migration (転入超過数), Japanese movers, October = **1,819** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 24,469 22,650 1,819 6,843 7,005 -162 11,727 11,201 526"
- `https://www.stat.go.jp/data/idou/rireki/2602/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?page=1&layout=dataset&toukei=00200523&iroha=24` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2603/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260528_no1867.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ipss.go.jp/syoushika/tohkei/Popular/Popular2026.asp?chap=9` -> **snapshot** (snapshot 20260510081302); points raw/verified 0/0

### d4 [related_series] Prefectural decomposition

Hypothesis: National total = sum over prefectures of in-migration (or out-migration) counts; large prefectures (Tokyo, Osaka, Aichi, Kanagawa) dominate. Summing prefectural August figures or scaling from a few large prefectures reconstructs the national total.

Queries issued by the searcher: 2025年8月 住民基本台帳人口移動報告 都道府県別 転入 転出 移動者数; 住民基本台帳人口移動報告 2025年8月 結果 総務省統計局; 住民基本台帳人口移動報告 2026年（令和8年）7月結果 市区町村間移動者数; 令和8年7月 人口移動の概況 都道府県別 転入者数 転出者数 2026; 東京都 住民基本台帳 移動者数 2025年8月 転入 転出; 都道府県別 人口移動 2025年8月 統計局 住民基本台帳移動報告; 住民基本台帳人口移動報告 2026年（令和8年）7月結果 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 2026年6月結果 移動者数; 東京都 住民基本台帳 移動者数 2025年8月 転入 転出; 住民基本台帳人口移動報告 2025年8月 都道府県別 転入超過 統計局; 住民基本台帳人口移動報告 2025年 年間 移動者数 総数; Japan internal migration report August 2025 statistics bureau prefectural in-migration

- `https://www.stat.go.jp/data/idou/rireki/2508/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 30/25
  - p166 National total inter-municipal movers (Japanese and foreign combined), calendar  = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p167 National inter-prefectural movers (Japanese and foreign combined), calendar year = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は251万5731人(対前年比0.3%減)"
  - p168 National total inter-municipal movers (Japanese and foreign combined), calendar  = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p169 National inter-prefectural in-migration total (sum of prefectural in-migrants, J = **2,515,731** person (2025-01-01..2025-12-31) [keep: ] quote: "全 国 2,515,731 2,515,731 782,165 409,592 82,854 118,193 337,234 331,686"
  - p170 Tokyo prefecture in-migrants from other prefectures (Japanese and foreign combin = **451,843** person (2025-01-01..2025-12-31) [keep: ] quote: "東 京 都 451,843 386,624 150,416 74,903 13,452 28,727 125,457 140,548"
  - p171 Tokyo prefecture out-migrants to other prefectures (Japanese and foreign combine = **386,624** person (2025-01-01..2025-12-31) [keep: ] quote: "東 京 都 451,843 386,624 150,416 74,903 13,452 28,727 125,457 140,548"
  - p172 Osaka prefecture in-migrants from other prefectures (Japanese and foreign combin = **184,232** person (2025-01-01..2025-12-31) [keep: ] quote: "大 阪 府 184,232 168,565 42,808 29,111 38,897 9,737 58,524 49,767"
  - p173 Osaka prefecture out-migrants to other prefectures (Japanese and foreign combine = **168,565** person (2025-01-01..2025-12-31) [keep: ] quote: "大 阪 府 184,232 168,565 42,808 29,111 38,897 9,737 58,524 49,767"
  - p174 Aichi prefecture in-migrants from other prefectures (Japanese and foreign combin = **124,856** person (2025-01-01..2025-12-31) [keep: ] quote: "愛 知 県 124,856 127,037 65,024 34,964 6,027 7,570 26,336 17,038"
  - p175 Aichi prefecture out-migrants to other prefectures (Japanese and foreign combine = **127,037** person (2025-01-01..2025-12-31) [keep: ] quote: "愛 知 県 124,856 127,037 65,024 34,964 6,027 7,570 26,336 17,038"
  - p176 Kanagawa prefecture in-migrants from other prefectures (Japanese and foreign com = **235,438** person (2025-01-01..2025-12-31) [keep: ] quote: "神 奈 川 県 235,438 207,386 51,913 30,150 421 8,344 41,892 41,916"
  - p177 Kanagawa prefecture out-migrants to other prefectures (Japanese and foreign comb = **207,386** person (2025-01-01..2025-12-31) [keep: ] quote: "神 奈 川 県 235,438 207,386 51,913 30,150 421 8,344 41,892 41,916"
  - p178 National inter-municipal movers, Japanese only, calendar year 2025 = **4,528,254** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p179 National inter-municipal movers, foreign residents only, calendar year 2025 = **662,294** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p180 National inter-prefectural movers, foreign residents only, calendar year 2025 = **367,402** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は36万7402人(対前年比9.8%増)。2014年以降、過去最多"
  - p181 National inter-prefectural in-migrants, Japanese only, calendar year 2025 = **2,148,329** person (2025-01-01..2025-12-31) [keep: ] quote: "全 国 2,148,329 2,188,590 -40,261 -1.8 2,148,329 2,188,590 -40,261 -1.8 0 0 0"
  - p182 National inter-prefectural in-migrants, foreign residents only, calendar year 20 = **367,402** person (2025-01-01..2025-12-31) [keep: ] quote: "全 国 367,402 334,659 32,743 9.8 367,402 334,659 32,743 9.8 0 0 0"
  - p183 Tokyo prefecture in-migrants from other prefectures, Japanese only, calendar yea = **397,985** person (2025-01-01..2025-12-31) [keep: ] quote: "東 京 都 397,985 407,610 -9,625 -2.4 332,388 337,047 -4,659 -1.4 65,597 70,563 -4,966"
  - p184 Tokyo prefecture out-migrants to other prefectures, Japanese only, calendar year = **332,388** person (2025-01-01..2025-12-31) [keep: ] quote: "東 京 都 397,985 407,610 -9,625 -2.4 332,388 337,047 -4,659 -1.4 65,597 70,563 -4,966"
  - p185 Osaka prefecture in-migrants from other prefectures, Japanese only, calendar yea = **160,358** person (2025-01-01..2025-12-31) [keep: ] quote: "大 阪 府 160,358 162,547 -2,189 -1.3 142,869 143,747 -878 -0.6 17,489 18,800 -1,311"
  - p186 Aichi prefecture in-migrants from other prefectures, Japanese only, calendar yea = **102,818** person (2025-01-01..2025-12-31) [keep: ] quote: "愛 知 県 102,818 103,003 -185 -0.2 101,012 103,611 -2,599 -2.5 1,806 -608 2,414"
  - p187 Tokyo prefecture in-migrants from other prefectures, foreign residents only, cal = **53,858** person (2025-01-01..2025-12-31) [keep: ] quote: "東 京 都 53,858 53,844 14 0.0 54,236 45,122 9,114 20.2 -378 8,722 -9,100"
  - p188 Osaka prefecture in-migrants from other prefectures, foreign residents only, cal = **23,874** person (2025-01-01..2025-12-31) [keep: ] quote: "大 阪 府 23,874 20,925 2,949 14.1 25,696 22,877 2,819 12.3 -1,822 -1,952 130"
  - p189 Aichi prefecture in-migrants from other prefectures, foreign residents only, cal = **22,038** person (2025-01-01..2025-12-31) [keep: ] quote: "愛 知 県 22,038 18,640 3,398 18.2 26,025 25,324 701 2.8 -3,987 -6,684 2,697"
  - p190 Share of total in-migrants captured by six prefectures (Tokyo, Kanagawa, Osaka,  = **53.8** % (2025-01-01..2025-12-31) [keep: ] quote: "これら6都府県への転入者数の合計は115万5560人となり、転入者総数の53.8%を占めている。"
- `https://www.stat.go.jp/data/idou/rireki/2508/pdf/gaikyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **snapshot** (snapshot 20251223084738); points raw/verified 30/30
  - p191 National total inter-municipal movers (市区町村間移動者数), all residents, October 2025 = **379,751** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "・市区町村間移動者数は 37万9751人。前年同月に比べ増加 1549人( 0.4%)"
  - p192 National inter-municipal movers, all residents, October 2024 (comparison month) = **378,202** person (migration events) (2024-10-01..2024-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p193 National inter-municipal movers, all residents, year-on-year change, October 202 = **1,549** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p194 National inter-municipal movers, all residents, year-on-year rate, October 2025 = **0.4** % (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p195 National inter-municipal movers, Japanese residents, October 2025 = **321,850** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p196 National inter-municipal movers, foreign residents, October 2025 = **57,901** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "市区町村間移動者数 379,751 378,202 1,549 0.4 321,850 326,783 -4,933 -1.5 57,901 51,419 6,482 12.6"
  - p197 National inter-prefectural movers, all residents, October 2025 = **168,057** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県間移動者数 168,057 167,107 950 0.6 137,348 140,545 -3,197 -2.3 30,709 26,562 4,147 15.6"
  - p198 National intra-prefectural movers, all residents, October 2025 = **211,694** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "都道府県内移動者数 211,694 211,095 599 0.3 184,502 186,238 -1,736 -0.9 27,192 24,857 2,335 9.4"
  - p199 National total in-migrants (転入者数) across prefectures, all residents, October 202 = **168,057** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "全 国 168,057 167,107 950 0.6 168,057 167,107 950 0.6 0 0"
  - p200 Tokyo prefecture in-migrants (転入者数), all residents, October 2025 = **29,182** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p201 Tokyo prefecture out-migrants (転出者数), all residents, October 2025 = **28,955** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p202 Tokyo prefecture net in-migration (転入超過数), all residents, October 2025 = **227** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "東 京 都 29,182 29,395 -213 -0.7 28,955 28,147 808 2.9 227 1,248"
  - p203 Kanagawa prefecture in-migrants (転入者数), all residents, October 2025 = **16,175** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "神 奈 川 県 16,175 15,984 191 1.2 15,187 14,976 211 1.4 988 1,008"
  - p204 Saitama prefecture in-migrants (転入者数), all residents, October 2025 = **14,018** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "埼 玉 県 14,018 13,475 543 4.0 12,558 12,125 433 3.6 1,460 1,350"
  - p205 Chiba prefecture in-migrants (転入者数), all residents, October 2025 = **11,480** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "千 葉 県 11,480 11,225 255 2.3 11,270 11,572 -302 -2.6 210 -347"
  - p206 Osaka prefecture in-migrants (転入者数), all residents, October 2025 = **12,152** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "大 阪 府 12,152 12,202 -50 -0.4 11,543 11,301 242 2.1 609 901"
  - p207 Osaka prefecture out-migrants (転出者数), all residents, October 2025 = **11,543** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "大 阪 府 12,152 12,202 -50 -0.4 11,543 11,301 242 2.1 609 901"
  - p208 Osaka prefecture net in-migration (転入超過数), all residents, October 2025 = **609** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "大 阪 府 12,152 12,202 -50 -0.4 11,543 11,301 242 2.1 609 901"
  - p209 Aichi prefecture in-migrants (転入者数), all residents, October 2025 = **8,056** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "愛 知 県 8,056 7,793 263 3.4 8,601 8,677 -76 -0.9 -545 -884"
  - p210 Aichi prefecture out-migrants (転出者数), all residents, October 2025 = **8,601** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "愛 知 県 8,056 7,793 263 3.4 8,601 8,677 -76 -0.9 -545 -884"
  - p211 Aichi prefecture net in-migration (転入超過数), all residents, October 2025 = **-545** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "愛 知 県 8,056 7,793 263 3.4 8,601 8,677 -76 -0.9 -545 -884"
  - p212 Hokkaido in-migrants (転入者数), all residents, October 2025 = **3,407** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "北 海 道 3,407 3,625 -218 -6.0 3,961 3,910 51 1.3 -554 -285"
  - p213 Fukuoka prefecture in-migrants (転入者数), all residents, October 2025 = **6,121** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "福 岡 県 6,121 6,328 -207 -3.3 6,116 6,259 -143 -2.3 5 69"
  - p214 Hyogo prefecture in-migrants (転入者数), all residents, October 2025 = **6,408** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "兵 庫 県 6,408 6,116 292 4.8 6,126 6,252 -126 -2.0 282 -136"
  - p215 Tokyo metropolitan area (東京圏) in-migrants, all residents, October 2025 = **29,721** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p216 Tokyo metropolitan area (東京圏) out-migrants, all residents, October 2025 = **26,836** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p217 Tokyo metropolitan area (東京圏) net in-migration, all residents, October 2025 = **2,885** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p218 Nagoya metropolitan area (名古屋圏) net in-migration, all residents, October 2025 = **-735** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p219 Osaka metropolitan area (大阪圏) net in-migration, all residents, October 2025 = **778** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "2025年10月 (令和7年10月) 29,721 26,836 2,885 8,791 9,526 -735 14,195 13,417 778"
  - p220 21 major cities total in-migrants (21大都市計), all residents, October 2025 = **93,597** person (migration events) (2025-10-01..2025-10-31) [keep: ] quote: "21 大 都 市 計 93,597 94,393 -796 -0.8 93,543 91,627 1,916 2.1 54 2,766"
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kankeijinko.jp/2026/08/29/1292/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000560` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.toukei.metro.tokyo.lg.jp/jidou/2025/ji-point.pdf` -> **snapshot** (snapshot 20260718032106); points raw/verified 28/28
  - p221 Tokyo total inter-municipal movers (all residents), calendar year 2025 = **1,317,064** person (2025-01-01..2025-12-31) [keep: ] quote: "令和7年における東京都の区市町村間移動者数は 1,317,064 人で、前年比 6,596 人(△0.5%)減"
  - p222 Tokyo Japanese-resident inter-municipal movers, calendar year 2025 = **1,116,080** person (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人の区市町村間移動者数は 1,116,080 人で、前年比 20,233 人(△1.8%)減"
  - p223 Tokyo foreign-resident inter-municipal movers, calendar year 2025 = **200,984** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人の区市町村間移動者数は 200,984 人で、前年比 13,637 人(7.3%)増"
  - p224 Tokyo movers between Tokyo and other prefectures (all residents), calendar year  = **838,467** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p225 Tokyo movers within Tokyo (between municipalities), all residents, calendar year = **465,145** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p226 Tokyo other movers (previous address unknown), all residents, calendar year 2025 = **13,452** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p227 Tokyo in-migrants from other prefectures (all residents), calendar year 2025 = **451,843** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数は 451,843 人"
  - p228 Tokyo out-migrants to other prefectures (all residents), calendar year 2025 = **386,624** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数は 386,624 人"
  - p229 Tokyo net in-migration from other prefectures (all residents), calendar year 202 = **65,219** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数(転入者数-転出者数)は 65,219 人"
  - p230 Tokyo net in-migration from other prefectures, Japanese residents, calendar year = **65,597** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p231 Tokyo net in-migration from other prefectures, foreign residents, calendar year  = **378** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p232 Tokyo movers within Tokyo between wards (ku), all residents, calendar year 2025 = **306,398** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p233 Tokyo movers between ku area and city/town/village area, all residents, calendar = **95,674** person (2025-01-01..2025-12-31) [keep: ] quote: "区部と市町村部間: 95,674 人(日本人 83,834 人、外国人 11,840 人)"
  - p234 Tokyo movers between municipalities outside ku area, all residents, calendar yea = **63,073** person (2025-01-01..2025-12-31) [keep: ] quote: "市町村相互間: 63,073 人(日本人 58,012 人、外国人 5,061 人)"
  - p235 Tokyo net in-migration, age 20-24, calendar year 2025 = **57,263** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数の最も多い年齢階級は20~24歳の57,263人、次いで25~29歳の20,642人、15~19歳の12,944人"
  - p236 Tokyo net in-migration, age 25-29, calendar year 2025 = **20,642** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数の最も多い年齢階級は20~24歳の57,263人、次いで25~29歳の20,642人、15~19歳の12,944人"
  - p237 Tokyo net in-migration, age 15-19, calendar year 2025 = **12,944** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数の最も多い年齢階級は20~24歳の57,263人、次いで25~29歳の20,642人、15~19歳の12,944人"
  - p238 Tokyo net out-migration, age 60-64, calendar year 2025 = **4,222** person (2025-01-01..2025-12-31) [keep: ] quote: "転出超過数の最も多い年齢階級は60~64歳の4,222人、次いで55~59歳の3,774人、65~69歳の2,562人"
  - p239 Tokyo net out-migration, age 55-59, calendar year 2025 = **3,774** person (2025-01-01..2025-12-31) [keep: ] quote: "転出超過数の最も多い年齢階級は60~64歳の4,222人、次いで55~59歳の3,774人、65~69歳の2,562人"
  - p240 Tokyo net out-migration, age 65-69, calendar year 2025 = **2,562** person (2025-01-01..2025-12-31) [keep: ] quote: "転出超過数の最も多い年齢階級は60~64歳の4,222人、次いで55~59歳の3,774人、65~69歳の2,562人"
  - p241 Tokyo net out-migration to three adjacent prefectures (Saitama, Chiba, Kanagawa) = **4,557** person (2025-01-01..2025-12-31) [keep: ] quote: "隣接3県(埼玉・千葉・神奈川県)との間では、3県合計で2年ぶりに転出超過となり、転出超過数は 4,557 人"
  - p242 Tokyo net in-migration from three adjacent prefectures, Japanese residents, cale = **967** person (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人は、前年に引き続き、3県合計で転入超過となり、転入超過数は 967 人"
  - p243 Tokyo net out-migration to three adjacent prefectures, foreign residents, calend = **5,524** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人は、3年ぶりに3県合計で転出超過となり、転出超過数は 5,524 人"
  - p244 Tokyo year-on-year change in total inter-municipal movers, calendar year 2025 = **6,596** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p245 Tokyo year-on-year percent change in total inter-municipal movers, calendar year = **0.5** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p246 Tokyo year-on-year percent change in foreign-resident inter-municipal movers, ca = **7.3** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 13,637 人(7.3%)増"
  - p247 Tokyo year-on-year change in net in-migration from other prefectures, calendar y = **14,066** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 14,066 人減"
  - p248 Tokyo net out-migration between ku area and city/town/village area, calendar yea = **6,968** person (2025-01-01..2025-12-31) [keep: ] quote: "区部と市町村部間では区部が 6,968 人の転出超過"
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://www.e-stat.go.jp/release-calendar/detail/00200523/202509261400` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 5)

### d5 [base_rates] Foreign vs Japanese resident split

Hypothesis: Foreign residents are a growing share of movers (roughly 5-10% of internal moves). Total = Japanese-resident moves + foreign-resident moves; foreign component can be estimated from foreign population and its higher mobility rate.

Queries issued by the searcher: 外国人 住民基本台帳 移動者数 割合 人口移動報告; foreign residents Japan internal migration share 2025 住民基本台帳移動報告; 2025年 外国人移動者 市区町村間移動者数 割合 住民基本台帳人口移動報告 外国人 11%; 住民基本台帳人口移動報告 2025年8月結果 外国人移動者 市区町村間; 住民基本台帳人口移動報告 2025年8月 移動者数 外国人 割合; 外国人 住民基本台帳 移動者数 割合 人口移動報告; 住民基本台帳人口移動報告 2026年7月結果 移動者数 外国人移動者; 住民基本台帳 人口動態調査 2026年1月1日 外国人住民 人数 総務省; 住民基本台帳人口移動報告 外国人 移動者数 割合; foreign residents Japan internal migration share 2025 住民基本台帳移動報告; 住民基本台帳人口移動報告 2025年8月結果 外国人移動者 市区町村間移動者数; stat.go.jp 住民基本台帳人口移動報告 令和8年 月次結果 2026年

- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **snapshot** (snapshot 20260513110926); points raw/verified 29/24
  - p249 Total inter-municipal movers (Japanese and foreign combined), Japan, calendar ye = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は519万548人(対前年比0.3%減)"
  - p250 Foreign-resident inter-municipal movers, Japan, calendar year 2025 = **662,294** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p251 Foreign-resident inter-municipal movers, Japan, calendar year 2024 = **604,591** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 662,294 604,591 57,703 9.5 367,402 334,659 32,743 9.8 294,892 269,932 24,960 9.2"
  - p252 Japanese-resident inter-municipal movers, Japan, calendar year 2025 = **4,528,254** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は452万8254人(対前年比1.6%減)"
  - p253 Japanese-resident inter-municipal movers, Japan, calendar year 2024 = **4,603,155** person (2024-01-01..2024-12-31) [keep: ] quote: "総数 4,528,254 4,603,155 -74,901 -1.6 2,148,329 2,188,590 -40,261 -1.8 2,379,925 2,414,565 -34,640 -1.4"
  - p254 Foreign-resident inter-municipal movers, Japan, calendar year 2014 (first year o = **299,590** person (2014-01-01..2014-12-31) [keep: ] quote: "26 2014 299,590 159,250 140,340 ... ... ... 154,055 79,452"
  - p255 Foreign-resident inter-municipal movers, Japan, calendar year 2015 = **343,070** person (2015-01-01..2015-12-31) [keep: ] quote: "27 2015 343,070 186,166 156,904 14.5 16.9 11.8 175,028 91,736"
  - p256 Foreign-resident inter-municipal movers, Japan, calendar year 2016 = **370,750** person (2016-01-01..2016-12-31) [keep: ] quote: "28 2016 370,750 202,678 168,072 8.1 8.9 7.1 185,735 98,497"
  - p257 Foreign-resident inter-municipal movers, Japan, calendar year 2017 = **425,036** person (2017-01-01..2017-12-31) [keep: ] quote: "29 2017 425,036 235,498 189,538 14.6 16.2 12.8 207,282 111,105"
  - p258 Foreign-resident inter-municipal movers, Japan, calendar year 2018 = **469,461** person (2018-01-01..2018-12-31) [keep: ] quote: "30 2018 469,461 263,823 205,638 10.5 12.0 8.5 227,353 123,424"
  - p259 Foreign-resident inter-municipal movers, Japan, calendar year 2019 = **514,274** person (2019-01-01..2019-12-31) [keep: ] quote: "令和 元 年 2019 514,274 291,524 222,750 9.5 10.5 8.3 243,193 133,156"
  - p260 Foreign-resident inter-municipal movers, Japan, calendar year 2020 = **414,869** person (2020-01-01..2020-12-31) [keep: ] quote: "2 2020 414,869 235,799 179,070 -19.3 -19.1 -19.6 198,369 108,167"
  - p261 Foreign-resident inter-municipal movers, Japan, calendar year 2021 = **429,023** person (2021-01-01..2021-12-31) [keep: ] quote: "3 2021 429,023 243,117 185,906 3.4 3.1 3.8 195,228 106,282"
  - p262 Foreign-resident inter-municipal movers, Japan, calendar year 2022 = **535,765** person (2022-01-01..2022-12-31) [keep: ] quote: "4 2022 535,765 302,829 232,936 24.9 24.6 25.3 237,693 130,016"
  - p263 Foreign-resident inter-municipal movers, Japan, calendar year 2023 = **566,677** person (2023-01-01..2023-12-31) [keep: ] quote: "5 2023 566,677 323,084 243,593 5.8 6.7 4.6 251,224 138,713"
  - p264 Foreign-resident inter-municipal movers, Japan, year-on-year growth rate 2025 = **9.5** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数は66万2294人(対前年比9.5%増)。2014年以降、過去最多"
  - p265 Foreign-resident inter-prefectural movers, Japan, calendar year 2025 = **367,402** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数は36万7402人(対前年比9.8%増)。2014年以降、過去最多"
  - p266 Total inter-municipal movers (Japanese and foreign), Japan, calendar year 2024 = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p267 Total inter-municipal movers (Japanese and foreign), Japan, calendar year 2015 = **5,384,553** person (2015-01-01..2015-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p268 Inflow from abroad (from outside Japan), Japanese and foreign combined, calendar = **782,165** person (2025-01-01..2025-12-31) [keep: ] quote: "国外からの転入者数は78万2165人(対前年比6.3%増)"
  - p269 Outflow to abroad, Japanese and foreign combined, calendar year 2025 = **409,592** person (2025-01-01..2025-12-31) [keep: ] quote: "国外への転出者数は40万9592人(対前年比10.2%増)"
  - p270 Foreign-resident inter-prefectural movers aged 25-29, Japan, calendar year 2025 = **102,912** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県間移動者数を年齢5歳階級別にみると、25~29歳が10万2912人と最も多く、次いで20"
  - p271 Foreign-resident inter-prefectural movers aged 20-24, Japan, calendar year 2025 = **101,074** person (2025-01-01..2025-12-31) [keep: ] quote: "~24歳(10万1074人)、30~34歳(6万1150人)などとなっている。(図22、表21、図23、表22)"
  - p272 Foreign-resident inter-prefectural movers aged 30-34, Japan, calendar year 2025 = **61,150** person (2025-01-01..2025-12-31) [keep: ] quote: "~24歳(10万1074人)、30~34歳(6万1150人)などとなっている。(図22、表21、図23、表22)"
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **snapshot** (snapshot 20260203011352); points raw/verified 30/27
  - p273 Japan domestic inter-municipal movers, 2025 (total, Japanese and foreign combine = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の国内における市区町村間移動者数は519万548人となり、前年に比べ0.3%の減少"
  - p274 Japan domestic inter-municipal movers, 2025 (table 1, persons) = **5,190,548** person (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p275 Japan domestic inter-municipal movers, 2024 (table 1, persons) = **5,207,746** person (2024-01-01..2024-12-31) [keep: ] quote: "市区町村間移動者数 5,384,553 5,251,717 5,318,617 5,359,174 5,403,465 5,255,721 5,247,744 5,310,972 5,263,249 5,207,746 5,190,548"
  - p276 Japan intra-prefectural inter-municipal movers, 2025 (persons) = **2,674,817** person (2025-01-01..2025-12-31) [keep: ] quote: "都道府県内移動者数 2,881,773 2,791,371 2,813,553 2,823,573 2,835,379 2,791,729 2,771,104 2,757,538 2,718,610 2,684,497 2,674,817"
  - p277 Japan inflows from abroad, 2024 (persons) = **735,883** person (2024-01-01..2024-12-31) [keep: ] quote: "国外からの転入者数 - - - - - 358,359 209,700 639,124 700,138 735,883 782,165"
  - p278 Japan outflows to abroad, 2024 (persons) = **371,615** person (2024-01-01..2024-12-31) [keep: ] quote: "国外への転出者数 - - - - - 226,845 224,077 312,484 346,690 371,615 409,592"
  - p279 Japan net social increase (national), 2025 (persons) = **337,234** person (2025-01-01..2025-12-31) [keep: ] quote: "を上回ったこと等により、33万7234人の社会増加、前年に比べ5548人の拡大"
  - p280 Three major metropolitan areas net in-migration, all movers, 2025 (persons) = **119,581** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体で は11万9581人の転入超過、前年に比べ 85人の縮小"
  - p281 Tokyo area net in-migration, all movers, 2025 (persons) = **123,534** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は12万3534人の転入超過、前年 に比べ1万2309人の縮小"
  - p282 Nagoya area net out-migration, all movers, 2025 (persons) = **12,695** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は1万2695人の転出超過、前年 に比べ6161人の縮小"
  - p283 Osaka area net in-migration, all movers, 2025 (persons) = **8,742** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は8742人の転入超過、前年に比べ 6063人の拡大"
  - p284 Three major metropolitan areas net in-migration, Japanese movers only, 2025 (per = **110,680** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(日本人移動者)では11万680人の転入超過、前年に比べ614人の縮小"
  - p285 Tokyo area net in-migration, Japanese movers only, 2025 (persons) = **112,738** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は11万2738人の転入超過、前年に比べ6599人の縮小。30年連続の転入超過"
  - p286 Nagoya area net out-migration, Japanese movers only, 2025 (persons) = **9,561** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は9561人の転出超過、前年に比べ1956人の縮小。13年連続の転出超過"
  - p287 Osaka area net in-migration, Japanese movers only, 2025 (persons) = **7,503** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は7503人の転入超過、前年に比べ4029人の拡大。3年連続の転入超過"
  - p288 Three major metropolitan areas in-movers, Japanese movers only, 2025 (persons) = **754,602** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数 813,906 795,328 796,693 808,772 816,306 767,651 751,990 766,689 777,968 769,772 754,602"
  - p289 Three major metropolitan areas out-movers, Japanese movers only, 2025 (persons) = **643,922** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数 704,993 689,158 690,718 688,519 686,102 683,039 688,293 689,620 676,517 658,478 643,922"
  - p290 Tokyo area in-movers, Japanese movers only, 2025 (persons) = **450,468** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数 487,251 477,790 481,289 491,003 497,660 459,096 446,808 459,077 468,064 462,388 450,468"
  - p291 Tokyo area out-movers, Japanese movers only, 2025 (persons) = **337,730** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数 367,894 359,922 361,510 355,403 352,084 361,091 366,367 364,666 353,262 343,051 337,730"
  - p292 Nagoya area in-movers, Japanese movers only, 2025 (persons) = **107,696** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数 122,609 119,006 117,509 118,026 116,168 111,015 110,481 110,642 110,286 108,929 107,696"
  - p293 Nagoya area out-movers, Japanese movers only, 2025 (persons) = **117,257** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数 123,699 121,369 122,488 125,466 127,683 123,290 121,718 124,351 123,872 120,446 117,257"
  - p294 Osaka area in-movers, Japanese movers only, 2025 (persons) = **196,438** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数 204,046 198,532 197,895 199,743 202,478 197,540 194,701 196,970 199,618 198,455 196,438"
  - p295 Osaka area out-movers, Japanese movers only, 2025 (persons) = **188,935** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数 213,400 207,867 206,720 207,650 206,335 198,658 200,208 200,603 199,383 194,981 188,935"
  - p296 Three major metropolitan areas net in-migration, foreign movers only, 2025 (pers = **8,901** person (2025-01-01..2025-12-31) [keep: ] quote: "3大都市圏全体(外国人移動者)では8901 人の転入超過、前年に比べ529人の拡大"
  - p297 Tokyo area net in-migration, foreign movers only, 2025 (persons) = **10,796** person (2025-01-01..2025-12-31) [keep: ] quote: "東京圏は1万796人の転入超過、前年に比べ 5710人の縮小"
  - p298 Nagoya area net out-migration, foreign movers only, 2025 (persons) = **3,134** person (2025-01-01..2025-12-31) [keep: ] quote: "名古屋圏は3134人の転出超過、前年に比べ 4205人の縮小"
  - p299 Osaka area net in-migration, foreign movers only, 2025 (persons) = **1,239** person (2025-01-01..2025-12-31) [keep: ] quote: "大阪圏は1239人の転入超過、3年ぶりに転 出超過から転入超過へ転じている"
- `https://www.toukei.metro.tokyo.lg.jp/jidou/2025/ji-point.pdf` -> **snapshot** (snapshot 20260718032106); points raw/verified 31/31
  - p300 Tokyo inter-municipal movers, total (Japanese + foreign), 2025 = **1,317,064** person (2025-01-01..2025-12-31) [keep: ] quote: "令和7年における東京都の区市町村間移動者数は 1,317,064 人で、前年比 6,596 人(△0.5%)減"
  - p301 Tokyo inter-municipal movers, Japanese residents, 2025 = **1,116,080** person (2025-01-01..2025-12-31) [keep: ] quote: "うち、日本人の区市町村間移動者数は 1,116,080 人で、前年比 20,233 人(△1.8%)減"
  - p302 Tokyo inter-municipal movers, foreign residents, 2025 = **200,984** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人の区市町村間移動者数は 200,984 人で、前年比 13,637 人(7.3%)増"
  - p303 Tokyo inter-municipal movers, year-on-year change, total, 2025 = **6,596** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p304 Tokyo inter-municipal movers, year-on-year change, Japanese, 2025 = **20,233** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 20,233 人(△1.8%)減"
  - p305 Tokyo inter-municipal movers, year-on-year change, foreign, 2025 = **13,637** person (2025-01-01..2025-12-31) [keep: ] quote: "前年比 13,637 人(7.3%)増"
  - p306 Tokyo inter-municipal movers, year-on-year percent change, total, 2025 = **0.5** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 6,596 人(△0.5%)減"
  - p307 Tokyo inter-municipal movers, year-on-year percent change, Japanese, 2025 = **1.8** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 20,233 人(△1.8%)減"
  - p308 Tokyo inter-municipal movers, year-on-year percent change, foreign, 2025 = **7.3** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比 13,637 人(7.3%)増"
  - p309 Tokyo movers between prefectures, total, 2025 = **838,467** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p310 Tokyo movers between prefectures, Japanese, 2025 = **730,373** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p311 Tokyo movers between prefectures, foreign, 2025 = **108,094** person (2025-01-01..2025-12-31) [keep: ] quote: "他道府県間: 838,467 人(日本人 730,373 人、外国人 108,094 人)"
  - p312 Tokyo movers within Tokyo (都内間), total, 2025 = **465,145** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p313 Tokyo movers within Tokyo (都内間), Japanese, 2025 = **384,882** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p314 Tokyo movers within Tokyo (都内間), foreign, 2025 = **80,263** person (2025-01-01..2025-12-31) [keep: ] quote: "都内間: 465,145 人(日本人 384,882 人、外国人 80,263 人)"
  - p315 Tokyo other movers (previous address unknown), total, 2025 = **13,452** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p316 Tokyo other movers (previous address unknown), Japanese, 2025 = **825** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p317 Tokyo other movers (previous address unknown), foreign, 2025 = **12,627** person (2025-01-01..2025-12-31) [keep: ] quote: "その他の移動者数:13,452 人(日本人 825 人、外国人 12,627 人)"
  - p318 Tokyo in-migrants from other prefectures, total, 2025 = **451,843** person (2025-01-01..2025-12-31) [keep: ] quote: "転入者数は 451,843 人"
  - p319 Tokyo in-migrants from other prefectures, Japanese, 2025 = **397,985** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 397,985 人、外国人 53,858 人)"
  - p320 Tokyo in-migrants from other prefectures, foreign, 2025 = **53,858** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 397,985 人、外国人 53,858 人)"
  - p321 Tokyo out-migrants to other prefectures, total, 2025 = **386,624** person (2025-01-01..2025-12-31) [keep: ] quote: "転出者数は 386,624 人"
  - p322 Tokyo out-migrants to other prefectures, Japanese, 2025 = **332,388** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 332,388 人、外国人 54,236 人)"
  - p323 Tokyo out-migrants to other prefectures, foreign, 2025 = **54,236** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 332,388 人、外国人 54,236 人)"
  - p324 Tokyo net in-migration from other prefectures, total, 2025 = **65,219** person (2025-01-01..2025-12-31) [keep: ] quote: "転入超過数(転入者数-転出者数)は 65,219 人"
  - p325 Tokyo net in-migration from other prefectures, Japanese, 2025 = **65,597** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p326 Tokyo net in-migration from other prefectures, foreign, 2025 = **378** person (2025-01-01..2025-12-31) [keep: ] quote: "(日本人 65,597 人、外国人△378 人)"
  - p327 Tokyo movers between wards (区相互間), total, 2025 = **306,398** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p328 Tokyo movers between wards (区相互間), foreign, 2025 = **63,362** person (2025-01-01..2025-12-31) [keep: ] quote: "区相互間: 306,398 人(日本人 243,036 人、外国人 63,362 人)"
  - p329 Tokyo movers between ward area and municipal area (区部と市町村部間), total, 2025 = **95,674** person (2025-01-01..2025-12-31) [keep: ] quote: "区部と市町村部間: 95,674 人(日本人 83,834 人、外国人 11,840 人)"
  - p330 Tokyo movers between municipalities (市町村相互間), total, 2025 = **63,073** person (2025-01-01..2025-12-31) [keep: ] quote: "市町村相互間: 63,073 人(日本人 58,012 人、外国人 5,061 人)"
- `https://www.sompo-ri.co.jp/2026/03/27/22713/` -> **snapshot** (snapshot 20260715103120); points raw/verified 26/26
  - p331 Foreign residents' share of Japan's total population (approximate, as stated) = **3** % (2025-01-01..2025-12-31) [keep: ] quote: "また、外国人の人口割合は日本全体では3%程度であるが"
  - p332 Tokyo area (Saitama, Chiba, Tokyo, Kanagawa) net in-migration, Japanese and fore = **123,534** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人と外国人を合計した、東京圏(埼玉県、千葉県、東京都、神奈川県)の2025年の転入超過数(転入数-転出数)は12万3,534人となり"
  - p333 Change in Tokyo area combined net in-migration, 2025 vs 2024 = **12,309** person (2025-01-01..2025-12-31) [keep: ] quote: "2024年に比べて1万2,309人縮小している。"
  - p334 Tokyo area combined net in-migration, 2024 = **135,843** person (2024-01-01..2024-12-31) [keep: ] quote: "2021年の8万441人を底に2024年の13万5,843人まで年々増加していた"
  - p335 Tokyo area combined net in-migration, 2021 (trough) = **80,441** person (2021-01-01..2021-12-31) [keep: ] quote: "2021年の8万441人を底に2024年の13万5,843人まで年々増加していた"
  - p336 Tokyo area net in-migration, foreign residents, 2025 = **10,796** person (2025-01-01..2025-12-31) [keep: ] quote: "しかし、2025年は1万796人と一転して大幅に減少している。"
  - p337 Tokyo area net in-migration, foreign residents, 2024 = **16,506** person (2024-01-01..2024-12-31) [keep: ] quote: "2023年は1万1,713 人、2024年は1万6,506人と大きく増加した。"
  - p338 Tokyo area net in-migration, foreign residents, 2023 = **11,713** person (2023-01-01..2023-12-31) [keep: ] quote: "2023年は1万1,713 人、2024年は1万6,506人と大きく増加した。"
  - p339 Change in Tokyo area net in-migration, foreign residents, 2025 vs 2024 = **5,710** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人は▲6,599人というやや減少、外国人は▲5,710人という大幅減少となっている。"
  - p340 Change in Tokyo area net in-migration, Japanese residents, 2025 vs 2024 = **6,599** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人は▲6,599人というやや減少、外国人は▲5,710人という大幅減少となっている。"
  - p341 Tokyo area net in-migration, Japanese residents, 2014 = **109,480** person (2014-01-01..2014-12-31) [keep: ] quote: "地方創生本格化前の2014年の10万9,480人をわずかながら上回っているだけだ。"
  - p342 Tokyo area net in-migration, Japanese residents, 2019 = **145,576** person (2019-01-01..2019-12-31) [keep: ] quote: "景気回復などを契機に2019年の14万5,576人まで大きく増加していた。"
  - p343 Tokyo area net in-migration, Japanese residents, 2011 = **62,809** person (2011-01-01..2011-12-31) [keep: ] quote: "リーマンショック後の2011年の6万2,809人にいったん落ち込んだものの"
  - p344 Nagoya area (Aichi, Gifu, Mie) combined net migration, 2025 (net out-migration) = **12,695** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の転入超過数を日本人と外国人を合わせると、名古屋圏は▲1万2,695人で"
  - p345 Osaka area (Osaka, Hyogo, Kyoto, Nara) combined net in-migration, 2025 = **8,742** person (2025-01-01..2025-12-31) [keep: ] quote: "同様に大阪圏は+8,742人で、2024年から6,063人増加している。"
  - p346 Nagoya area net migration, foreign residents, 2025 (net out-migration) = **3,134** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人を同様に見ると、2025年は▲3,134人で、2024年に比べて4,025人増加"
  - p347 Osaka area net migration, foreign residents, 2025 = **1,239** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年は2024年の▲795人の転出超過から一転して+1,239人の転入超過に転じ"
  - p348 Osaka area net migration, foreign residents, 2024 (net out-migration) = **795** person (2024-01-01..2024-12-31) [keep: ] quote: "2025年は2024年の▲795人の転出超過から一転して+1,239人の転入超過に転じ"
  - p349 Nagoya area net migration, Japanese residents, 2025 (net out-migration) = **9,561** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の名古屋圏の日本人の転入超過数は▲9,561人(転出超過)"
  - p350 Osaka area net migration, Japanese residents, 2025 = **7,503** person (2025-01-01..2025-12-31) [keep: ] quote: "2025年の大阪圏の日本人の転入超過数は+7,503人で、2024年に比べて4,029人増加している。"
  - p351 Combined change in Nagoya and Osaka areas' net in-migration, foreign residents,  = **6,059** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人は+5,985人、外国人は+6,059人となっている。"
  - p352 Combined change in Nagoya and Osaka areas' net in-migration, Japanese residents, = **5,985** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人は+5,985人、外国人は+6,059人となっている。"
  - p353 Decrease in Tokyo area net in-migration vs non-three-major-metro areas, foreign  = **2,694** person (2025-01-01..2025-12-31) [keep: ] quote: "外国人の転入超過数の減少については、対その他が▲2,694人とかなり大きく"
  - p354 Decrease in Tokyo area net in-migration vs non-three-major-metro areas, Japanese = **2,786** person (2025-01-01..2025-12-31) [keep: ] quote: "日本人の転入超過数の減少については、対その他が▲2,786人と最も大きい"
  - p355 Tokyo area net in-migration, Japanese residents, 1984 (historical comparison) = **112,610** person (1984-01-01..1984-12-31) [keep: ] quote: "1984年(11万2,610人)、2005年(11万4,688人)と、かなり昔まで遡る必要がある。"
  - p356 Tokyo area net in-migration, Japanese residents, 2005 (historical comparison) = **114,688** person (2005-01-01..2005-12-31) [keep: ] quote: "1984年(11万2,610人)、2005年(11万4,688人)と、かなり昔まで遡る必要がある。"
- `https://www.e-stat.go.jp/stat-search/database?layout=dataset&query=Foreigners%20in%20Japan&statdisp_id=0004035372` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202301021A-buntan6_0.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2511/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2406/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search?layout=dataset&page=1&query=Foreigners%20by%20nationality` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260203_no1834.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?page=1&layout=dataset&toukei=00200523&bunya_l=02&tstat=000000070001&cycle=7&tclass1=000001128855&result_` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kannaikaikei.jp/news/15723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 5; value_as_written not in quote as a whole number: 3)

### d6 [shocks] Calendar and policy effects

Hypothesis: August 2026 move volume may deviate from trend due to calendar effects (number of weekends, Obon timing), housing/relocation policy, or economic conditions; these shift the level modestly (±few %). Identifying measurable drivers constrains the adjustment.

Queries issued by the searcher: 引越し 件数 2026年 8月 需要; 人口移動 2026年 傾向 統計局; 住民基本台帳人口移動報告 2026年7月 速報 統計局; 住民基本台帳人口移動報告 2026年 転入超過 傾向; 統計局 住民基本台帳人口移動報告 2026年 6月 公表; Report on Internal Migration in Japan Derived from the Basic Resident Registration 2026 Statistics Bureau; 住民基本台帳人口移動報告 2026年7月結果 市区町村間移動者数; 引越し 件数 2026年 需要 引越しシーズン 2026年8月; 引越し 件数 2026年 8月 需要; 人口移動 2026年 傾向 統計局; moving company Japan 2026 relocation demand; 住民基本台帳人口移動報告 2026年7月 外国人 移動者数; 総務省統計局 人口移動報告 2026年 月次 公表; 2026年8月 お盆 日程 暦 土日 数 去年

- `https://www.stat.go.jp/data/idou/rireki/2607/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260827_no1893.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.html` -> **snapshot** (snapshot 20260618143342); points raw/verified 0/0
- `https://jp-newsfocus.com/foreign-resident-interprefectural-moves-july-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kurashi-start.com/hikkoshi-hanki-calendar-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hikkoshi-pedia.com/yen/2168/` -> **snapshot** (snapshot 20260518094719); points raw/verified 1/1
  - p357 Long-distance moves (over 100 km) advised against during Obon holiday, August 20 = **100** km (2025-08-01..2025-08-31) [keep: ] quote: "新居までの移動が100kmを超える長距離引越しについては、お盆休みに行うべきではありません。"
- `https://www.wa-f.com/blog/entry-797803/` -> **snapshot** (snapshot 20260722140934); points raw/verified 9/2
  - p358 Advance notice required to terminate a typical rental lease, Japan = **1** month (not stated (page dated 2026-06-02)) [keep: ] quote: "多くの賃貸借契約では、退去の1か月前までに解約の申し出を行うことが必要とされているため、夏に引っ越す場合は、この期限から逆算して時期を決めると良いでしょう。"
  - p359 Recommended overlap period of double rent when changing residence, Japan (lower  = **1** day (not stated (page dated 2026-06-02)) [keep: ] quote: "無理のない範囲で、数日から1週間程度の重複にとどめられるよう、契約条件をよく確認しながら引っ越し時期を調整することが大切です。"
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.html` -> **snapshot** (snapshot 20260827233628); points raw/verified 27/27
  - p360 Total inter-municipal movers (all residents, Japanese and foreign), Japan, July  = **390,799** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p361 Year-on-year change in total inter-municipal movers, Japan, July 2026 = **7,618** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p362 Year-on-year percent change in total inter-municipal movers, Japan, July 2026 = **1.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の市区町村間移動者数は39万799人と、前年同月に比べ7618人(1.9%)減少。"
  - p363 Total inter-prefectural movers (all residents), Japan, July 2026 = **181,604** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p364 Year-on-year change in total inter-prefectural movers, Japan, July 2026 = **1,260** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p365 Year-on-year percent change in total inter-prefectural movers, Japan, July 2026 = **0.7** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県間移動者数は18万1604人と、前年同月に比べ1260人(0.7%)減少。"
  - p366 Total intra-prefectural movers (all residents), Japan, July 2026 = **209,195** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p367 Year-on-year change in total intra-prefectural movers, Japan, July 2026 = **6,358** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p368 Year-on-year percent change in total intra-prefectural movers, Japan, July 2026 = **2.9** % (2026-07-01..2026-07-31) [keep: ] quote: "移動者の都道府県内移動者数は20万9195人と、前年同月に比べ6358人(2.9%)減少。"
  - p369 Japanese inter-municipal movers, Japan, July 2026 = **335,854** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p370 Year-on-year change in Japanese inter-municipal movers, Japan, July 2026 = **9,318** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p371 Year-on-year percent change in Japanese inter-municipal movers, Japan, July 2026 = **2.7** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の市区町村間移動者数は33万5854人と、前年同月に比べ9318人(2.7%)減少。"
  - p372 Japanese inter-prefectural movers, Japan, July 2026 = **150,347** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p373 Year-on-year change in Japanese inter-prefectural movers, Japan, July 2026 = **3,801** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p374 Year-on-year percent change in Japanese inter-prefectural movers, Japan, July 20 = **2.5** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県間移動者数は15万347人と、前年同月に比べ3801人(2.5%)減少。"
  - p375 Japanese intra-prefectural movers, Japan, July 2026 = **185,507** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p376 Year-on-year change in Japanese intra-prefectural movers, Japan, July 2026 = **5,517** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p377 Year-on-year percent change in Japanese intra-prefectural movers, Japan, July 20 = **2.9** % (2026-07-01..2026-07-31) [keep: ] quote: "日本人移動者の都道府県内移動者数は18万5507人と、前年同月に比べ5517人(2.9%)減少。"
  - p378 Foreign resident inter-municipal movers, Japan, July 2026 = **54,945** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p379 Year-on-year change in foreign resident inter-municipal movers, Japan, July 2026 = **1,700** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p380 Year-on-year percent change in foreign resident inter-municipal movers, Japan, J = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の市区町村間移動者数は5万4945人と、前年同月に比べ1700人(3.2%)増加。"
  - p381 Foreign resident inter-prefectural movers, Japan, July 2026 = **31,257** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p382 Year-on-year change in foreign resident inter-prefectural movers, Japan, July 20 = **2,541** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p383 Year-on-year percent change in foreign resident inter-prefectural movers, Japan, = **8.8** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県間移動者数は3万1257人と、前年同月に比べ2541人(8.8%)増加。"
  - p384 Foreign resident intra-prefectural movers, Japan, July 2026 = **23,688** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
  - p385 Year-on-year change in foreign resident intra-prefectural movers, Japan, July 20 = **841** person (migration events) (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
  - p386 Year-on-year percent change in foreign resident intra-prefectural movers, Japan, = **3.4** % (2026-07-01..2026-07-31) [keep: ] quote: "外国人移動者の都道府県内移動者数は2万3688人と、前年同月に比べ841人(3.4%)減少。"
- `https://www.e-stat.go.jp/index.php/stat-search/files?page=1&layout=dataset&iroha=18&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://shokicost.com/hikkoshi-hanbouki-sougaku-sagaku/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.com/dare_mo_iwanai/n/nf55eab7145bf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hellomove.com/news/%ef%bc%98%e6%9c%88%e3%81%af%e6%af%8e%e5%b9%b4%e7%a9%ba%e3%81%8d%e3%81%8c%e5%bc%b7%e3%81%84%e3%81%a7%e3%81%99%e3%80%82/` -> **snapshot** (snapshot 20260716140159); points raw/verified 1/1
  - p387 Months in the July–September period during which the moving company has reduced  = **8** (range 7..9) as written "7月~9月", value check pending month (2025-07-01..2025-09-30) [keep: ] quote: "ここ数年前からこの期間(7月~9月)につきましては、件数を減らしスタッフの休憩を多くしているため早めのご契約がおすすめです。"
- dropped by code checks: 7 (period year 2026 does not appear in the page text or URL (likely mis-dated): 3; number: low/high given but value_as_written is not a range: 4)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan migration', 'internal migration', 'population movement']: no matching market created on or before as_of markets=0


## Judge

### round 1

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a** person, 80% interval [n/a, n/a] person, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

Unit of the estimate: person (person (migration events, one per mover per move); total for 2026-08-01 to 2026-08-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

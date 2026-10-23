# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births occurring in Japan during July 2026, as counted in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (人口動態統計速報), which includes foreign nationals residing in Japan | unit births | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (MHLW), Japan

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW preliminary monthly vital statistics time series

Hypothesis: July 2026 births will follow the recent year-over-year trend and July seasonality seen in prior preliminary monthly releases; the same-month prior-year value plus recent YoY change gives a direct anchor.

Queries issued by the searcher: 人口動態統計速報 2025年 月別 出生数; Japan monthly vital statistics preliminary births July 2025 人口動態統計速報; 人口動態統計速報 令和8年6月分 出生数 2026; 人口動態統計速報 2026年5月分 出生数 前年同月比; 2024年7月分 人口動態統計速報 出生数 前年同月比 2024年9月; "2023年7月" 人口動態統計速報 出生数 6万人 前年同月比

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 15/15
  - p1 Preliminary births, Japan, March 2025 (令和7年3月, monthly) = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p2 Preliminary births, Japan, March 2024 (令和6年3月, monthly, prior-year preliminary) = **55,198** as written "55 198", value check pending births (2024-03-01..2024-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p3 Year-over-year change in monthly births, Japan, March 2025 vs March 2024 = **-1,579** as written "△ 1 579", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p4 Year-over-year percent change in monthly births, Japan, March 2025 = **2.9** % (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p5 Cumulative preliminary births, Japan, Jan-Mar 2025 (令和7年1月～3月) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p6 Cumulative preliminary births, Japan, Jan-Mar 2024 (prior-year preliminary) = **170,804** as written "170 804", value check pending births (2024-01-01..2024-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p7 Year-over-year percent change in cumulative births, Japan, Jan-Mar 2025 = **4.6** % (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p8 Trailing 12-month preliminary births, Japan, Apr 2024-Mar 2025 (当月を含む過去1年間) = **713,139** as written "713 139", value check pending births (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p9 Trailing 12-month preliminary births, Japan, Apr 2023-Mar 2024 (prior-year preli = **746,958** as written "746 958", value check pending births (2023-04-01..2024-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p10 Year-over-year percent change in trailing 12-month births, Japan, Apr 2024-Mar 2 = **4.5** % (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p11 National total births, Japan, March 2025 (都道府県別 table, 全国) = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [DISCARD: Duplicate of p1 (same national total, same release).] quote: "全 国 53 619 145 215 1 351 55 762 19 692"
  - p12 National total births, Japan, Jan-Mar 2025 (都道府県別 cumulative table, 全国) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [DISCARD: Duplicate of p5.] quote: "全 国 162 955 466 672 3 979 131 332 48 685"
  - p13 Year-over-year ratio of monthly births, Japan, March 2025 (対前年比, prior year = 10 = **97.3** index (prior year = 100) (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p14 Year-over-year ratio of trailing 12-month births, Japan, Apr 2024-Mar 2025 (対前年比 = **95.9** index (prior year = 100) (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p15 Year-over-year ratio of cumulative births, Japan, Jan-Mar 2025 (対前年比) = **96.6** index (prior year = 100) (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7.pdf` -> **snapshot** (snapshot 20260816002753); points raw/verified 15/10
  - p16 Japan total live births, calendar year 2023 (確定数) = **727,288** as written "727 288", value check pending births (2023-01-01..2023-12-31) [keep: ] quote: "総数 770 759 727 288 686 173 671 236 △43 471 △41 115 △14 937"
  - p17 Japan total live births, calendar year 2022 (確定数) = **770,759** as written "770 759", value check pending births (2022-01-01..2022-12-31) [keep: ] quote: "総数 770 759 727 288 686 173 671 236 △43 471 △41 115 △14 937"
  - p18 Year-over-year change in Japan total live births, 2024 vs 2023 = **-41,115** as written "△41 115", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "総数 770 759 727 288 686 173 671 236 △43 471 △41 115 △14 937"
  - p19 Year-over-year change in Japan total live births, 2023 vs 2022 = **-43,471** as written "△43 471", value check pending births (2023-01-01..2023-12-31) [keep: ] quote: "総数 770 759 727 288 686 173 671 236 △43 471 △41 115 △14 937"
  - p20 Year-over-year percent change in Japan total live births, 2025 vs 2024 (prelimin = **2.2** % (2025-01-01..2025-12-31) [keep: ] quote: "671 236 686 173 △ 14 937 △ 2.2 5.6 5.7 47 46"
  - p21 Japan total fertility rate, 2025 preliminary = **1.14** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "また、合計特殊出生率 は 1.14 で、前年の 1.15 より低下している。"
  - p22 Japan total fertility rate, 2024 = **1.15** children per woman (2024-01-01..2024-12-31) [keep: ] quote: "また、合計特殊出生率 は 1.14 で、前年の 1.15 より低下している。"
  - p23 Japan total live births, calendar year 2021 (確定数) = **811,622** as written "811 622", value check pending births (2021-01-01..2021-12-31) [keep: ] quote: "2021 3 811 622 1 439 856 1 399 658 △ 628 234 16 277 8 082 8 195 2 741 501 138 184 384 1 815"
  - p24 Japan total live births, calendar year 2020 (確定数) = **840,835** as written "840 835", value check pending births (2020-01-01..2020-12-31) [keep: ] quote: "2020 2 840 835 1 372 755 1 512 704 △ 531 920 17 278 8 188 9 090 2 664 525 507 193 253 1 805"
  - p25 Japan total live births, calendar year 2019 (確定数) = **865,239** as written "865 239", value check pending births (2019-01-01..2019-12-31) [keep: ] quote: "2019 令和 元 年 865 239 1 381 093 1 654 755 △ 515 854 19 454 8 997 10 457 2 955 599 007 208 496 1 953"
- `https://www.wic-net.com/search/by_freeword/page/2/?freeword=%E4%BA%BA%E5%8F%A3%E5%8B%95%E6%85%8B%E7%B5%B1%E8%A8%88&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e3%83%bb%e4%bf%9d%e5%81%a5%e7%a4%be%e4%bc%9a%e7%b5%b1%e8%a8%88%e5%ae%a4/page/3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d2 [related_series] Annual and year-to-date birth totals

Hypothesis: Annual births (confirmed 確定 or 概数) decomposed into monthly shares lets July 2026 be estimated as annual total × July share; year-to-date 2026 births scaled by historical July/YTD ratio provides a cross-check.

Queries issued by the searcher: Japan total births 2025 annual vital statistics 人口動態統計 確定値 出生数; 人口動態統計 月別 出生数 内訳 2024年 各月; 人口動態統計速報 令和8年6月分 出生数 2026年1月～6月 累計; e-Stat 出生月別にみた年次別出生数 2024年 7月 出生数

- `https://www.e-stat.go.jp/index.php/stat-search/files?cycle=7&layout=dataset&month=0&stat_infid=000040320377&tclass1=000001053058&tclass2=000001053061&` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202512h.pdf` -> **snapshot** (snapshot 20260712060226); points raw/verified 15/15
  - p26 Annual live births in Japan, 2025 preliminary (速報), including foreign nationals  = **705,809** births (2025-01-01..2025-12-31) [keep: ] quote: "・出生数は、705,809 人で 10 年連続減少 (対前年 15,179 人減少 △2.1%)"
  - p27 Annual live births in Japan, 2024 preliminary (速報), including foreign nationals  = **720,988** as written "720 988", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "令和6年 2024 720 988 1 618 684 △ 897 696 16 031 499 999 189 952"
  - p28 Annual live births in Japan, 2023 preliminary (速報), including foreign nationals  = **758,631** as written "758 631", value check pending births (2023-01-01..2023-12-31) [keep: ] quote: "令和5年 2023 758 631 1 590 503 △ 831 872 16 153 489 281 187 798"
  - p29 Annual live births in Japan, 2024 confirmed (確定数), Japanese nationals in Japan o = **686,173** as written "686 173", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "令和6年 2024 686 173 1 605 378 △ 919 205 15 323 485 092 185 904"
  - p30 Year-on-year change in annual live births, 2025 vs 2024 preliminary (速報) = **15,179** births (2025-01-01..2025-12-31) [keep: ] quote: "・出生数は、705,809 人で 10 年連続減少 (対前年 15,179 人減少 △2.1%)"
  - p31 Year-on-year percent change in annual live births, 2025 vs 2024 preliminary (速報) = **2.1** % (2025-01-01..2025-12-31) [keep: ] quote: "・出生数は、705,809 人で 10 年連続減少 (対前年 15,179 人減少 △2.1%)"
  - p32 Annual live births in Japan, 2022 preliminary (速報), including foreign nationals  = **799,728** as written "799 728", value check pending births (2022-01-01..2022-12-31) [keep: ] quote: "令和4年 2022 799 728 1 582 033 △ 782 305 15 714 519 823 183 103"
  - p33 Annual live births in Japan, 2021 preliminary (速報), including foreign nationals  = **842,897** as written "842 897", value check pending births (2021-01-01..2021-12-31) [keep: ] quote: "令和3年 2021 842 897 1 452 289 △ 609 392 16 854 514 242 187 854"
  - p34 Annual live births in Japan, 2020 preliminary (速報), including foreign nationals  = **872,683** as written "872 683", value check pending births (2020-01-01..2020-12-31) [keep: ] quote: "令和2年 2020 872 683 1 384 544 △ 511 861 17 894 537 583 196 641"
  - p35 Annual live births in Japan, 2019 preliminary (速報), including foreign nationals  = **898,600** as written "898 600", value check pending births (2019-01-01..2019-12-31) [keep: ] quote: "令和元年 2019 898 600 1 393 917 △ 495 317 20 001 615 652 212 955"
  - p36 Annual live births in Japan, 2018 preliminary (速報), including foreign nationals  = **950,832** as written "950 832", value check pending births (2018-01-01..2018-12-31) [keep: ] quote: "平成30年 2018 950 832 1 374 765 △ 423 933 20 140 602 735 212 393"
  - p37 Annual live births in Japan, 2017 preliminary (速報), including foreign nationals  = **978,167** as written "978 167", value check pending births (2017-01-01..2017-12-31) [keep: ] quote: "平成29年 2017 978 167 1 352 198 △ 374 031 20 873 623 010 216 354"
  - p38 Annual live births in Japan, 2016 preliminary (速報), including foreign nationals  = **1,010,944** as written "1 010 944", value check pending births (2016-01-01..2016-12-31) [keep: ] quote: "平成28年 2016 1 010 944 1 319 012 △ 308 068 21 386 636 522 221 029"
  - p39 Annual live births in Japan, 2015 preliminary (速報), including foreign nationals  = **1,037,064** as written "1 037 064", value check pending births (2015-01-01..2015-12-31) [keep: ] quote: "平成27年 2015 1 037 064 1 301 824 △ 264 760 23 085 650 519 230 580"
  - p40 Annual live births in Japan, 2014 preliminary (速報), including foreign nationals  = **1,035,667** as written "1 035 667", value check pending births (2014-01-01..2014-12-31) [keep: ] quote: "平成26年 2014 1 035 667 1 283 560 △ 247 893 23 973 658 579 226 334"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7houdou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Japanese-nationals-only monthly estimates (概数/月報)

Hypothesis: The 概数 series for Japanese nationals tracks the preliminary total closely; applying the historical foreign-national share bridges to the all-nationality preliminary figure.

Queries issued by the searcher: 人口動態統計月報 出生数 外国人 日本人 2025; 厚生労働省 人口動態統計速報 2025年 出生数 外国人 割合; 人口動態統計月報（概数） 令和8 2026年 出生数 mhlw.go.jp geppo m2026; "人口動態統計月報" 2025年7月分 概数 出生数 日本人

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/03.html` -> **snapshot** (snapshot 20260818065414); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p41 Preliminary (速報) births, all nationalities, Japan, May 2026 = **59,663** as written "59 663", value check ok births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p42 Preliminary (速報) births, all nationalities, Japan, May 2025 = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p43 Preliminary (速報) births, all nationalities, Japan, cumulative Jan–May 2026 = **282,222** as written "282 222", value check ok births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p44 Preliminary (速報) births, all nationalities, Japan, cumulative Jan–May 2025 = **280,979** as written "280 979", value check ok births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p45 Preliminary (速報) births, all nationalities, Japan, trailing 12 months Jun 2025–M = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p46 Preliminary (速報) births, all nationalities, Japan, trailing 12 months Jun 2024–M = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p47 Year-on-year change in preliminary births, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p48 Year-on-year percent change in preliminary births, May 2026 vs May 2025 = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p49 Year-on-year percent change in preliminary births, cumulative Jan–May 2026 vs 20 = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p50 Year-on-year percent change in preliminary births, trailing 12 months Jun 2025–M = **0.4** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p51 Ratio of May 2026 to May 2025 preliminary births (前年比) = **98.7** % (2026-05-01..2026-05-31) [keep: ] quote: "出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p52 Ratio of cumulative Jan–May 2026 to 2025 preliminary births (前年比) = **101** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p53 Ratio of trailing-12-month Jun 2025–May 2026 to prior year preliminary births (前 = **100** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p54 National total preliminary births, May 2026 (prefecture table) = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p41.] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p55 National total preliminary births, cumulative Jan–May 2026 (prefecture table) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [DISCARD: Duplicate of p43.] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://limo.media/articles/-/141476` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Official population projections and research institute forecasts

Hypothesis: IPSS (国立社会保障・人口問題研究所) and other published birth forecasts for 2026, plus any monthly projections, constrain the annual level from which July is a share.

Queries issued by the searcher: 国立社会保障・人口問題研究所 2026 出生数 推計; Japan 2026 births forecast IPSS projection annual; 日本総研 2026年 出生数 予測 何万人; 人口動態統計速報 2025年 月別 出生数 7月

- `https://www.ipss.go.jp/pp-zenkoku/e/zenkoku_e2023/pp2023e_Summary.pdf` -> **snapshot** (snapshot 20260621125821) **LEAK SENTINEL HIT ['(?<![\\d.,])62,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.sankei.com./article/20260510-BY3MFI6NIJD23KXYH6EKTMQC5A/` -> **snapshot** (snapshot 20260511154028); points raw/verified 7/7
  - p56 Japan total births, January 2026, preliminary vital statistics, year-on-year cha = **0.5** as written "0・5%増", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p57 Japan total births, January 2026, preliminary vital statistics = **58,694** births (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p58 Japan total births, February 2026, preliminary vital statistics, year-on-year ch = **0.4** as written "0・4%減", value check pending % (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だった"
  - p59 Japan total births, February 2026, preliminary vital statistics = **50,761** births (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だった"
  - p60 Japan cumulative total births, January-February 2026, preliminary vital statisti = **0.1** as written "0・1%増", value check pending % (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p61 Japan cumulative total births, January-February 2026, preliminary vital statisti = **109,455** births (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p62 Japan total births, 1966 (previous 丙午 year), year-on-year decline = **25** % (1966-01-01..1966-12-31) [DISCARD: 1966 丙午 superstition-year decline is a one-off historical anomaly with no transfer to 2026.] quote: "60年前の1966年は出生数が前年比25%も減少した"
- `https://www.163.com/dy/article/L6B3PO5F05561FYZ_pdya11y.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.47news.jp/13920092.html` -> **snapshot** (snapshot 20260404075650); points raw/verified 12/11
  - p63 Japan total live births including foreign nationals, 2025 preliminary (速報値) = **705,809** births (2025-01-01..2025-12-31) [DISCARD: Duplicate of p26.] quote: "2025年の外国人を含むわが国の出生数(速報値)は、70万5809人で過去最少となった。"
  - p64 Estimated Japanese-national births (日本人の出生数) for the year, year-on-year change = **2.2** as written "2・2%減", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "例年6月に公表される日本人の出生数を試算すると、前年比2・2%減の67万1千人となる。"
  - p65 Japan total fertility rate (合計特殊出生率), 2024 actual = **1.15** as written "1・15", value check pending children per woman (2024-01-01..2024-12-31) [keep: ] quote: "「合計特殊出生率」は、過去最低だった2024年の1・15を下回り、1・13程度となることが見込まれる。"
  - p66 Japan total fertility rate (合計特殊出生率), forecast for the year = **1.13** as written "1・13程度", value check pending children per woman (2025-01-01..2025-12-31) [keep: ] quote: "「合計特殊出生率」は、過去最低だった2024年の1・15を下回り、1・13程度となることが見込まれる。"
  - p67 Annual decline rate of births exceeded, 2022 onward (threshold) = **5** % (2022-01-01..2025-12-31) [DISCARD: A threshold statement, not a measurement of births.] quote: "ただし、出生数は2022年から5%を超えて減少し続けていたが、その状況からは脱する見通しである。"
  - p68 Birth decline rate, large cities (20 designated cities + Tokyo 23 wards), prelim = **0.7** as written "0・7%の減少", value check pending % (2025-01-01..2025-12-31) [DISCARD: Large-city decline rate for an unspecified period; no usable level or clean conversion to July 2026 national births.] quote: "全国20の政令指定都市と東京都区部(23区)を合わせた大都市では、出生数が0・7%の減少にとどまる一方、それらを除く地域ではマイナス2・8%と強めの減勢が続いている。"
  - p69 Birth decline rate, areas outside large cities, preliminary = **-2.8** as written "マイナス2・8%", value check pending % (2025-01-01..2025-12-31) [DISCARD: Non-large-city decline rate, unspecified period; unusable as a level.] quote: "全国20の政令指定都市と東京都区部(23区)を合わせた大都市では、出生数が0・7%の減少にとどまる一方、それらを除く地域ではマイナス2・8%と強めの減勢が続いている。"
  - p70 Birth change rate, Tokyo 23 wards (東京都区部), preliminary = **1.4** as written "1・4%の増加", value check pending % (2025-01-01..2025-12-31) [DISCARD: Tokyo 23-ward change rate, unspecified period; too local and undefined to convert.] quote: "東京都区部が1・4%の増加に転じ、大阪市はマイナス0・1%の微減にとどまった。"
  - p71 Birth change rate, Osaka City (大阪市), preliminary = **-0.1** as written "マイナス0・1%", value check pending % (2025-01-01..2025-12-31) [DISCARD: Osaka City change rate, unspecified period; too local.] quote: "東京都区部が1・4%の増加に転じ、大阪市はマイナス0・1%の微減にとどまった。"
  - p72 Birth decline rate, Sagamihara City (相模原市), preliminary = **7** as written "7・0%減", value check pending % (2025-01-01..2025-12-31) [DISCARD: Sagamihara change rate, unspecified period; too local.] quote: "一方で、相模原市(7・0%減)や神戸市(4・5%減)のように全国平均を大きく超える減少率となった都市もある。"
  - p73 Birth decline rate, Kobe City (神戸市), preliminary = **4.5** as written "4・5%減", value check pending % (2025-01-01..2025-12-31) [DISCARD: Kobe change rate, unspecified period; too local.] quote: "一方で、相模原市(7・0%減)や神戸市(4・5%減)のように全国平均を大きく超える減少率となった都市もある。"
- dropped by code checks: 1 (number: scale conflict: '千' in value vs '万': 1)

### d5 [shocks] Calendar and demographic drivers

Hypothesis: July births reflect conceptions ~9-10 months earlier (Sept-Oct 2025); marriage counts, COVID-era cohort effects, and any 2025 shocks (e.g., flu, heat) shift the level; number of reproductive-age women and recent marriage trends set the base.

Queries issued by the searcher: 人口動態統計速報 2025年 月別 出生数; 婚姻件数 月別 2025 厚生労働省 人口動態統計; 人口動態統計速報 2026年6月分 出生数; 2026年 出生数 月別 速報 5月 前年同月比; 人口動態統計速報 令和8年5月分 出生数 累計 2026

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 15/15
  - p74 Japan total live births, March 2025 (preliminary monthly vital statistics, inclu = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [DISCARD: Duplicate of p1.] quote: "3月 出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p75 Japan total live births, March 2024 (preliminary, prior-year comparison) = **55,198** as written "55 198", value check pending births (2024-03-01..2024-03-31) [DISCARD: Duplicate of p2.] quote: "3月 出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p76 Japan total live births, January-March 2025 cumulative (preliminary) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [DISCARD: Duplicate of p5.] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p77 Japan total live births, January-March 2024 cumulative (preliminary) = **170,804** as written "170 804", value check pending births (2024-01-01..2024-03-31) [DISCARD: Duplicate of p6.] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p78 Japan total live births, trailing 12 months April 2024-March 2025 (preliminary) = **713,139** as written "713 139", value check pending births (2024-04-01..2025-03-31) [DISCARD: Duplicate of p8.] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p79 Japan total live births, trailing 12 months April 2023-March 2024 (preliminary) = **746,958** as written "746 958", value check pending births (2023-04-01..2024-03-31) [DISCARD: Duplicate of p9.] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p80 Japan marriage registrations, March 2025 (preliminary, conception proxy) = **55,762** as written "55 762", value check pending marriages (2025-03-01..2025-03-31) [DISCARD: March 2025 marriage count; conception proxy for a birth month far from July 2026 and not usable as a level.] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p81 Japan marriage registrations, March 2024 (preliminary) = **56,864** as written "56 864", value check pending marriages (2024-03-01..2024-03-31) [DISCARD: March 2024 marriage count; same issue.] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p82 Japan marriage registrations, January-March 2025 cumulative (preliminary) = **131,332** as written "131 332", value check pending marriages (2025-01-01..2025-03-31) [DISCARD: Jan–Mar 2025 cumulative marriages; conception proxy with no calibrated birth conversion.] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p83 Japan marriage registrations, January-March 2024 cumulative (preliminary) = **136,653** as written "136 653", value check pending marriages (2024-01-01..2024-03-31) [DISCARD: Jan–Mar 2024 cumulative marriages; same issue.] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p84 Japan marriage registrations, trailing 12 months April 2024-March 2025 (prelimin = **494,678** as written "494 678", value check pending marriages (2024-04-01..2025-03-31) [DISCARD: Trailing-12-month marriages; no calibrated marriage-to-birth conversion available.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p85 Japan marriage registrations, trailing 12 months April 2023-March 2024 (prelimin = **491,082** as written "491 082", value check pending marriages (2023-04-01..2024-03-31) [DISCARD: Prior-year trailing marriages; same issue.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p86 Japan total live births, March 2025, national row of prefecture table (prelimina = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [DISCARD: Duplicate of p1.] quote: "全 国 53 619 145 215 1 351 55 762 19 692"
  - p87 Japan total live births, January-March 2025 cumulative, national row of prefectu = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [DISCARD: Duplicate of p5.] quote: "全 国 162 955 466 672 3 979 131 332 48 685"
  - p88 Japan total deaths, March 2025 (preliminary) = **145,215** as written "145 215", value check pending deaths (2025-03-01..2025-03-31) [DISCARD: Deaths, irrelevant to births.] quote: "死 亡 145 215 144 451 764 0.5 13.9 13.8 100.7"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/search/by_freeword/page/2/?freeword=%E4%BA%BA%E5%8F%A3%E5%8B%95%E6%85%8B%E7%B5%B1%E8%A8%88&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e3%83%bb%e4%bf%9d%e5%81%a5%e7%a4%be%e4%bc%9a%e7%b5%b1%e8%a8%88%e5%ae%a4/page/3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [administrative] Local government birth registrations and resident registry

Hypothesis: Municipal or prefectural birth registration counts and 住民基本台帳 population data for mid-2026 can proxy the national monthly flow if aggregated shares are known.

Queries issued by the searcher: 住民基本台帳 出生数 2026; 人口動態統計速報 2026年7月 出生数; 人口動態統計速報 令和8年6月分 出生数 2026年8月; 東京都 人口動態統計 月別 出生数 2026年 速報; 人口動態統計速報 令和8年5月分 出生数 5万9663人 都道府県別; 令和8年 月別 出生数 1月 5万8694人 2月 3月 4月 5月 2026

- `https://www.saitama-np.co.jp/articles/207978/postDetail` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nihonnews.jp.net/shakai/jinko/japan-population-drops-record-916744-births-at-record-low.html` -> **snapshot** (snapshot 20260729173505); points raw/verified 16/0
- `https://www.yomiuri.co.jp/politics/20260729-GYT1T00324/` -> **snapshot** (snapshot 20260730093620); points raw/verified 14/14
  - p89 Japanese resident population (住民基本台帳, Jan 1 2026), total = **119,736,483** people (2026-01-01..2026-01-01) [keep: ] quote: "日本人住民は、前年比91万6744人減の1億1973万6483人で42年ぶりに1億2000万人を割り込んだ。"
  - p90 Japanese resident population change vs prior year (住民基本台帳, Jan 1 2026) = **916,744** people (2026-01-01..2026-01-01) [DISCARD: Population change, not births; redundant with p89.] quote: "日本人住民は、前年比91万6744人減の1億1973万6483人で42年ぶりに1億2000万人を割り込んだ。"
  - p91 Foreign resident population (住民基本台帳, Jan 1 2026), total = **4,031,159** people (2026-01-01..2026-01-01) [keep: ] quote: "外国人住民は、同35万3696人増の403万1159人で過去最多だった。"
  - p92 Foreign resident population change vs prior year (住民基本台帳, Jan 1 2026) = **353,696** people (2026-01-01..2026-01-01) [DISCARD: Foreign population change, not births; redundant with p91.] quote: "外国人住民は、同35万3696人増の403万1159人で過去最多だった。"
  - p93 Total domestic population (住民基本台帳, Jan 1 2026) = **123,767,642** people (2026-01-01..2026-01-01) [DISCARD: Total population, irrelevant to monthly births.] quote: "国内総人口は1億2376万7642人で前年から56万3048人減った。"
  - p94 Total domestic population change vs prior year (住民基本台帳, Jan 1 2026) = **563,048** people (2026-01-01..2026-01-01) [DISCARD: Total population change, irrelevant.] quote: "国内総人口は1億2376万7642人で前年から56万3048人減った。"
  - p95 Natural decrease among Japanese residents (住民基本台帳, Jan 1 2026) = **923,008** people (2026-01-01..2026-01-01) [DISCARD: Natural decrease, irrelevant to births.] quote: "出生数が死亡数を下回る「自然減」は日本人で92万3008人に上り、18年連続で拡大した。"
  - p96 Japanese births (住民基本台帳, Jan 1 2026 reference year), record low = **670,467** births (2026-01-01..2026-01-01) [keep: ] quote: "日本人の出生数は67万467人で過去最少だった一方、外国人は2万2835人で過去最多を更新した。"
  - p97 Foreign resident births (住民基本台帳, Jan 1 2026 reference year), record high = **22,835** births (2026-01-01..2026-01-01) [keep: ] quote: "日本人の出生数は67万467人で過去最少だった一方、外国人は2万2835人で過去最多を更新した。"
  - p98 Japanese deaths (住民基本台帳, Jan 1 2026 reference year) = **1,593,475** people (2026-01-01..2026-01-01) [DISCARD: Deaths, irrelevant.] quote: "死亡者数は日本人で159万3475人、外国人で9109人だった。"
  - p99 Foreign resident deaths (住民基本台帳, Jan 1 2026 reference year) = **9,109** people (2026-01-01..2026-01-01) [DISCARD: Deaths, irrelevant.] quote: "死亡者数は日本人で159万3475人、外国人で9109人だった。"
  - p100 Largest prefectural total population decline rate (Akita, 住民基本台帳, Jan 1 2026) = **1.88** as written "1・88%", value check pending % (2026-01-01..2026-01-01) [DISCARD: Prefectural population decline rate, irrelevant to national monthly births.] quote: "総人口の減少率は秋田県の1・88%が最大で、山形、青森両県の1・62%などが続いた。"
  - p101 Prefectural total population decline rate (Yamagata and Aomori, 住民基本台帳, Jan 1 20 = **1.62** as written "1・62%", value check pending % (2026-01-01..2026-01-01) [DISCARD: Prefectural decline rates, irrelevant.] quote: "総人口の減少率は秋田県の1・88%が最大で、山形、青森両県の1・62%などが続いた。"
  - p102 Number of prefectures (excluding Tokyo) with Japanese population decline (住民基本台帳 = **46** prefectures (2026-01-01..2026-01-01) [DISCARD: Count of declining prefectures, irrelevant.] quote: "日本人住民は、東京以外の46道府県で減ったが、外国人は全都道府県で増えた。"
- `https://www.47news.jp/14705499.html` -> **snapshot** (snapshot 20260729192514); points raw/verified 14/12
  - p103 Japanese population as of Jan 1, 2026 (住民基本台帳-based 人口動態調査) = **119,736,483** people (2026-01-01..2026-01-01) [DISCARD: Duplicate of p89.] quote: "今年1月1日時点の日本人の人口は1億1973万6483人だった"
  - p104 Year-on-year rate of decrease in Japanese population = **0.76** % (2025-01-01..2026-01-01) [DISCARD: Population decrease rate, irrelevant.] quote: "前年比約91万7千人(0.76%)減で"
  - p105 Foreign national population as of Jan 1, 2026 = **4,031,159** people (2026-01-01..2026-01-01) [DISCARD: Duplicate of p91.] quote: "外国人は約35万4千人増の403万1159人"
  - p106 Deaths among Japanese (approx., year to Jan 1, 2026) = **1,590,000** people (2025-01-01..2026-01-01) [DISCARD: Deaths, irrelevant.] quote: "死亡者は約159万人だったのに対し"
  - p107 Births among Japanese (approx., minimum, year to Jan 1, 2026) = **670,000** births (2025-01-01..2026-01-01) [DISCARD: Approximate duplicate of p96.] quote: "出生者は最少の約67万人と大きく下回った"
  - p108 Tokyo metropolitan area (Saitama, Chiba, Tokyo, Kanagawa) population as of Jan 1 = **35,319,837** people (2026-01-01..2026-01-01) [DISCARD: Metro-area population, irrelevant.] quote: "東京圏(埼玉、千葉、東京、神奈川)は約8万人減の3531万9837人"
  - p109 Year-on-year decrease in Tokyo metropolitan area population (approx.) = **80,000** people (2025-01-01..2026-01-01) [DISCARD: Metro-area population change, irrelevant.] quote: "東京圏(埼玉、千葉、東京、神奈川)は約8万人減の3531万9837人"
  - p110 Tokyo metropolitan area share of total population = **29.5** % (2026-01-01..2026-01-01) [DISCARD: Population share, irrelevant.] quote: "全体の29.50%に上り、東京圏への人口集中が続いている"
  - p111 Tokyo prefecture Japanese population change rate (only positive prefecture) = **0.09** % (2025-01-01..2026-01-01) [DISCARD: Tokyo population change rate, irrelevant.] quote: "プラスは東京の0.09%"
  - p112 Akita prefecture Japanese population decline rate (highest) = **1.95** % (2025-01-01..2026-01-01) [DISCARD: Akita decline rate, irrelevant.] quote: "減少率は秋田の1.95%が最も高く"
  - p113 Aomori and Kochi prefecture Japanese population decline rate = **1.7** % (2025-01-01..2026-01-01) [DISCARD: Prefectural decline rates, irrelevant.] quote: "青森、高知がいずれも1.70%で続いた"
  - p114 Number of prefectures with declining Japanese population (excluding Tokyo) = **46** prefectures (2025-01-01..2026-01-01) [DISCARD: Count of declining prefectures, irrelevant.] quote: "都道府県別では、東京を除く46道府県が減少した"
- dropped by code checks: 18 (period year 2025 does not appear in the page text or URL (likely mis-dated): 5; period year 2026 does not appear in the page text or URL (likely mis-dated): 11; number: scale conflict: '千' in value vs '万': 2)

### b1 [own_history] MHLW preliminary monthly vital statistics

Hypothesis: The July 2025 preliminary all-nationality birth count (and July 2024) would give a direct same-month anchor for July 2026 via yoy_scaling against the Jan–May 2026 trend; this is the single most valuable missing input because it converts the observed 2026 flat trend into a July level.

Queries issued by the searcher: 人口動態統計速報 令和7年7月 出生数 外国人; MHLW monthly vital statistics July 2025 births; 2025年7月 人口動態統計速報 出生数 前年同月; site:mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html 出生数 63,415; 2024年7月 人口動態統計速報 出生数 65,231; 2026年1月 人口動態統計速報 出生数 1月 2026

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2024/07.html` -> **snapshot** (snapshot 20260317070535); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20250&month=23070907&tclass1=0000010` -> **snapshot** (snapshot 20251112234917); points raw/verified 0/0

### b2 [related_series] Seasonal decomposition of monthly births

Hypothesis: Historical monthly shares of annual births (July share) would let the 2026 annual level (≈705,000–710,000) be decomposed into a July figure; this unlocks a second independent route and cross-checks the yoy route.

Queries issued by the searcher: 人口動態統計速報 月次 出生数 2024年 各月; Japan monthly live births 2024 2025 by month statistics 出生数 月別; mhlw.go.jp 人口動態統計速報 令和7年7月分 出生数 63,415; 日本 出生数 月別 2023年 2024年 2025年 一覧 速報 1月 2月 3月 各月 推移

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&lid=000001450284` -> **snapshot** (snapshot 20260320013947); points raw/verified 0/0
- `https://www.wic-net.com/publisher/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e3%83%bb%e4%bf%9d%e5%81%a5%e7%a4%be%e4%bc%9a%e7%b5%b1%e8%a8%88%e5%ae%a4/page/4/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.namu.wiki/w/%ec%9d%bc%eb%b3%b8/%ec%b6%9c%ec%82%b0%ec%9c%a8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] Foreign-national share of births

Hypothesis: The foreign-national share of births (≈3% from p97/p96) applied to the Japanese-nationals 概数 series would bridge to the all-nationality preliminary figure; this resolves whether the 2026 flat trend is driven by foreign births and constrains the level.

Queries issued by the searcher: 人口動態統計速報 外国人 出生数 2025; 日本 出生数 外国人 割合 3% 2024 人口動態統計; 人口動態統計速報 2026年 月別 出生数 厚生労働省; 人口動態統計 概数 2025年 日本人 出生数 外国人 別

- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&bunya_l=02&stat_infid=000040483983` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/01.html` -> **snapshot** (snapshot 20260711103824); points raw/verified 0/0
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.jnocnews.co.jp/n144068.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan births', 'japan birth rate', 'japan population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p13', 'p74', 'p75'] Same March 2025 preliminary release; p1/p11/p74/p86 are the same 53,619 figure repeated across tables (not independent). p2/p75 same 55,198. p3/p4/p13 are the derived change/ratio of the same pair.
- corroborating: ['p5', 'p6', 'p7', 'p12', 'p15', 'p76', 'p77', 'p87'] Jan–Mar 2025 cumulative 162,955 vs 170,804; p5/p12/p76/p87 duplicate the same total; p7/p15 derived ratios.
- corroborating: ['p8', 'p9', 'p10', 'p14', 'p78', 'p79'] Trailing-12-month Apr2024–Mar2025 = 713,139 vs 746,958; duplicates of one release.
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55'] Single MHLW preliminary release (2026-07-24) covering May 2026 and Jan–May 2026 cumulative; p54/p55 duplicate national rows. This is the most recent and most relevant vintage for the 2026 level.
- corroborating: ['p56', 'p57', 'p58', 'p59', 'p60', 'p61'] Sankei reporting of Jan/Feb 2026 preliminary births; consistent with the Jan–May 2026 cumulative being roughly flat (+0.4%).
- corroborating: ['p26', 'p27', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p63'] Annual preliminary (速報) series including foreign nationals; p26 and p63 are the same 705,809 figure from two outlets (not independent).
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p23', 'p24', 'p25', 'p29'] Confirmed (確定) series for Japanese nationals; lower than preliminary all-nationality by the foreign-national share. p20's 2.2% decline is the Japanese-nationals preliminary, consistent with p64.
- corroborating: ['p21', 'p22', 'p65', 'p66'] TFR 1.15 (2024) → 1.14/1.13 (2025); consistent with continued decline.
- corroborating: ['p89', 'p90', 'p103', 'p104'] Same 住民基本台帳 Jan-1-2026 Japanese population 119,736,483 from two outlets.
- corroborating: ['p91', 'p92', 'p105'] Same foreign population 4,031,159.
- corroborating: ['p96', 'p97', 'p107'] 住民基本台帳 Japanese births ~670,467 and foreign births 22,835 for the year to Jan 1 2026; p107 is the rounded version. Different definition (registry, not vital statistics) but consistent in magnitude wit
- conflicting: ['p100', 'p101', 'p112', 'p113'] Two different decline-rate figures for Akita (1.88% vs 1.95%) and Yamagata/Aomori (1.62% vs 1.70%) — different reference definitions (total vs Japanese population). Not material to the birth estimate.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p41', 'p42', 'p47', 'p48', 'p51'] Same May 2026 preliminary release: level, prior-year level, change, percent change and ratio are internally consistent arithmetic from one measurement, not independent evidence.
- corroborating: ['p43', 'p44', 'p49', 'p52'] Jan–May 2026 cumulative and its prior-year comparison come from the same release; the +0.4% cumulative vs −1.7% May-only shows a mild recent softening within one source.
- corroborating: ['p45', 'p46', 'p50', 'p53'] Trailing-12-month figures are the same release's rolling sum; they overlap p41–p44 and are not independent.
- corroborating: ['p57', 'p56', 'p59', 'p58', 'p61', 'p60'] Sankei-reported Jan and Feb 2026 preliminary monthly births and cumulative; consistent with the MHLW Jan–May cumulative (p43) being roughly flat year-on-year. Same underlying MHLW preliminary series, 
- corroborating: ['p26', 'p27', 'p28', 'p30', 'p31'] Annual preliminary (速報) all-nationality series: 2025 = 705,809, down 15,179 (−2.1%) from 2024 = 720,988; internally consistent.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p29'] Confirmed (確定) Japanese-national annual births and changes; 2024 confirmed 686,173 is below the all-nationality preliminary 720,988, consistent with the foreign-national share and with preliminary-vs-
- corroborating: ['p96', 'p97', 'p29'] Resident-register (住民基本台帳) Japanese births 670,467 plus foreign 22,835 ≈ 693,302, close to but below the confirmed Japanese-national 686,173 plus foreign; different measurement system (register vs vit
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p13', 'p5', 'p6', 'p7', 'p15', 'p8', 'p9', 'p10', 'p14'] March 2025 release: monthly, cumulative and trailing-12-month levels and ratios are one measurement set; they establish the 2025 downtrend (~−4.5% trailing) but are a year stale for July 2026.
- corroborating: ['p21', 'p22', 'p65', 'p66', 'p64'] TFR 1.14 (2025 prelim) vs 1.15 (2024) and press forecast ~1.13 are consistent; they constrain the annual level only indirectly.
- conflicting: ['p41', 'p26'] Apparent conflict: 2025 annual preliminary was −2.1% but Jan–May 2026 is +0.4% year-on-year. Not a true contradiction — different periods; the 2026 flattening is a genuine change in trend that must be

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 level relative to May 2026 preliminary monthly births | 1 | 0.93..1.07 | 0.7054..1.411 (widened) | dimensionless | m1 (m1) | July and May monthly birth counts in Japan are typically within a few percent of each other; the Jan–May 2026 cumulative is +0.4% year-on-year (p43 vs p44) and the trailing 12 months are −0.4% (p45 vs p46), so the mid-2026 monthly flow is near-flat. A factor centred at 1.0 with a ±7% 10–90 range cov | The May 2026 preliminary level is a valid proxy for the July 2026 monthly flow, i.e. no large July-specific shock. | Evidence of a large July-specific birth surge or collapse, or a strong seasonal July-vs-May gap in preliminary monthly data. |
| a2 | July share of annual all-nationality births | 0.0833 | 0.078..0.089 | 0.05892..0.1178 (widened) | fraction | m2 (m2) | July is a near-average month; 1/12 ≈ 0.0833. Japanese monthly birth shares vary only modestly around the mean, so a share near 0.083 with a ±6% relative range is appropriate. | The 2026 annual level is close to the 2025 preliminary level and July's seasonal share is near average. | Historical monthly shares showing July systematically far from 1/12, or a 2026 annual level far from 705,809. |
| a3 | July 2026 vs July 2025 year-on-year change factor | 1 | 0.94..1.06 | 0.8928..1.116 (widened) | dimensionless | m3 (m3) | Jan–May 2026 cumulative is +0.4% (p43 vs p44) and trailing-12-month −0.4% (p45 vs p46), so the recent year-on-year change is essentially flat; a factor centred at 1.0 with a ±6% range reflects the observed flattening rather than the steeper 2025 decline. | The flat 2026 year-on-year trend continues into July. | Evidence that July 2026 diverges sharply from the Jan–May 2026 flat trend. |
| a4 | July 2025 preliminary all-nationality births as a fraction of the 2025 annual preliminary total | 0.0836 | 0.078..0.089 | 0.05892..0.1178 (widened) | fraction | m3 (m3) | July 2025 monthly births are not in the kept table, but the July share of the annual total is a dimensionless seasonal share near 1/12 (0.0833). May 2025 was 60,718 (p42) against a 2025 annual of 705,809 (p26), i.e. a May share of 0.0860, so a July share near 0.0836 is consistent with normal seasona | Used only as a share multiplied by the 2025 annual preliminary total to reconstruct a July 2025 base, then adjusted by a3. | Historical monthly shares showing July systematically far from 1/12. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 59,596 | ['p41'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 58,863 | ['p26'] / ['a2'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 58,691 | ['p26'] / ['a3', 'a4'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **59,049** person, 80% interval [39,331, 88,651] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for live births occurring in Japan during July 2026, as counted in MHLW's preliminary monthly vital statistics (all nationalities, including foreign residents), is 59,049 person (80% model-based interval 39,331 to 88,651 person).

Three routes were averaged with equal weights (33%, 33%, 33%): a direct carry-forward from the May 2026 preliminary count of 59,663 births (59,596 person); an annual-decomposition using 2025 preliminary births of 705,809 births times a July share near 0.0833 (58,863 person); and a same-month year-on-year route using a July 2025 share of 0.0836 and a near-flat change factor of 1 (58,691 person).

Only the May 2026 count and the 2025 annual total are observed; the July level factor (1), seasonal shares, and year-on-year factor are analyst assumptions. The interval reflects input uncertainty only, not demonstrated accuracy. The main risk is that July's seasonal share or level departs materially from these assumptions. Actual July 2026 monthly data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 level relative to May 2026 preliminary monthly births: 1 dimensionless, range 0.7054 to 1.411 (range widened by code); used by m1. Overturned by: Evidence of a large July-specific birth surge or collapse, or a strong seasonal July-vs-May gap in preliminary monthly data.
- a2 July share of annual all-nationality births: 0.0833 fraction, range 0.05892 to 0.1178 (range widened by code); used by m2. Overturned by: Historical monthly shares showing July systematically far from [n]/[n], or a 2026 annual level far from [n].
- a3 July 2026 vs July 2025 year-on-year change factor: 1 dimensionless, range 0.8928 to 1.116 (range widened by code); used by m3. Overturned by: Evidence that July 2026 diverges sharply from the Jan–May 2026 flat trend.
- a4 July 2025 preliminary all-nationality births as a fraction of the 2025 annual preliminary total: 0.0836 fraction, range 0.05892 to 0.1178 (range widened by code); used by m3. Overturned by: Historical monthly shares showing July systematically far from [n]/[n].

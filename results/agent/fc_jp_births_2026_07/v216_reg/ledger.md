# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births occurring in Japan during July 2026, as counted in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (人口動態統計速報), which includes foreign nationals residing in Japan | unit births | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (厚生労働省), preliminary monthly vital statistics (人口動態統計速報)

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW preliminary monthly vital statistics time series

Hypothesis: July births in recent years (2019-2025) show a declining trend with a seasonal July pattern; extrapolating the recent year-over-year decline rate to July 2025 gives a baseline for July 2026.

Queries issued by the searcher: 人口動態統計速報 令和7年7月 出生数; Japan monthly vital statistics preliminary births July 2025 人口動態統計速報; 人口動態統計速報 令和8年5月分 出生数 2026; "人口動態統計速報" 2026年1月分 出生数 前年同月比; 人口動態統計速報 令和7年7月 出生数; Japan monthly vital statistics births July 2025 preliminary MHLW; mhlw.go.jp 人口動態統計速報 令和8年 2026年6月分 出生数; 人口動態統計速報 2024年7月分 出生数 前年同月比; 人口動態統計速報 月別 出生数 2025年7月; Japan monthly vital statistics preliminary births July 2025 人口動態統計速報; 人口動態統計速報 令和8年5月分 出生数 厚生労働省; www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026 出生数

- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/07.html` -> **snapshot** (snapshot 20260317070800); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p1 Japan monthly births, May 2026 (preliminary vital statistics, current month) = **59,663** as written "59 663", value check ok births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p2 Japan monthly births, May 2025 (preliminary, prior year comparison) = **60,718** as written "60 718", value check ok births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p3 Japan births, May 2026 vs May 2025 year-over-year change (difference) = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p4 Japan births, May 2026 vs May 2025 year-over-year change rate = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p5 Japan births, cumulative January-May 2026 (preliminary) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p6 Japan births, cumulative January-May 2025 (preliminary) = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p7 Japan births, cumulative January-May 2026 vs 2025 change rate = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p8 Japan births, past 12 months June 2025-May 2026 (preliminary) = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p9 Japan births, past 12 months June 2024-May 2025 (preliminary) = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p10 Japan births, past 12 months June 2025-May 2026 vs prior 12 months change rate = **0.4** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p11 Japan national births, May 2026 (by prefecture of notification table) = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p12 Japan national births, cumulative January-May 2026 (by prefecture table) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
  - p13 Japan annualized birth rate, May 2026 (per 1,000 population, year-converted) = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p14 Japan annualized birth rate, May 2025 (per 1,000 population, year-converted) = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p15 Japan annualized birth rate, past 12 months June 2025-May 2026 (per 1,000 popula = **5.7** births per 1,000 population (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20250&month=23070907&tclass1=0000010` -> **snapshot** (snapshot 20251112234917); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/dl/toukeihyo_07.pdf` -> **snapshot** (snapshot 20260517093739); points raw/verified 15/15
  - p16 Japan total live births, July 2025 (preliminary monthly vital statistics, 実数) = **60,650** as written "60 650", value check ok births (2025-07-01..2025-07-31) [keep: ] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p17 Japan total live births, July 2024 (preliminary, 実数) = **62,306** as written "62 306", value check ok births (2024-07-01..2024-07-31) [keep: ] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p18 Year-over-year change in Japan total live births, July 2025 vs July 2024 (差引増減) = **-1,656** as written "△ 1 656", value check pending births (2025-07-01..2025-07-31) [keep: ] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p19 Year-over-year percent change in Japan total live births, July 2025 vs July 2024 = **2.7** % (2025-07-01..2025-07-31) [keep: ] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p20 Japan total live births, January-July 2025 cumulative (実数) = **379,729** as written "379 729", value check pending births (2025-01-01..2025-07-31) [keep: ] quote: "累 計 1月~7月 379 729 392 304 △ 12 575 △ 3.2 5.5 5.6"
  - p21 Japan total live births, January-July 2024 cumulative (実数) = **392,304** as written "392 304", value check pending births (2024-01-01..2024-07-31) [keep: ] quote: "累 計 1月~7月 379 729 392 304 △ 12 575 △ 3.2 5.5 5.6"
  - p22 Japan monthly live births, January 2024 (Table 2, 出生数) = **54,624** as written "54 624", value check pending births (2024-01-01..2024-01-31) [keep: ] quote: "令和6年1月 54 624 151 988 110 52 △ 97 364 575 689 199 39 572 14 602"
  - p23 Japan monthly live births, February 2024 (Table 2, 出生数) = **51,884** as written "51 884", value check pending births (2024-02-01..2024-02-29) [keep: ] quote: "2月 51 884 138 498 83 45 △ 86 614 544 710 163 37 388 14 875"
  - p24 Japan monthly live births, March 2024 (Table 2, 出生数) = **52,470** as written "52 470", value check pending births (2024-03-01..2024-03-31) [keep: ] quote: "3月 52 470 142 937 100 43 △ 90 467 599 790 194 55 496 19 871"
  - p25 Japan monthly live births, April 2024 (Table 2, 出生数) = **56,563** as written "56 563", value check pending births (2024-04-01..2024-04-30) [keep: ] quote: "4月 56 563 126 195 99 52 △ 69 632 557 732 181 30 158 16 580"
  - p26 Japan monthly live births, May 2024 (Table 2, 出生数) = **59,144** as written "59 144", value check pending births (2024-05-01..2024-05-31) [keep: ] quote: "5月 59 144 124 167 114 60 △ 65 023 553 717 179 45 949 15 454"
  - p27 Japan monthly live births, June 2024 (Table 2, 出生数) = **55,313** as written "55 313", value check pending births (2024-06-01..2024-06-30) [keep: ] quote: "6月 55 313 116 489 130 75 △ 61 176 534 698 209 32 030 14 025"
  - p28 Japan monthly live births, August 2024 (Table 2, 出生数) = **60,698** as written "60 698", value check ok births (2024-08-01..2024-08-31) [keep: ] quote: "8月 60 698 132 797 100 47 △ 72 099 621 639 187 39 619 14 341"
  - p29 Japan monthly live births, January 2025 (Table 2, 出生数) = **51,816** as written "51 816", value check pending births (2025-01-01..2025-01-31) [keep: ] quote: "令和7年1月 51 816 172 287 124 56 △120 471 570 682 186 32 401 14 045"
  - p30 Japan monthly live births, June 2025 (Table 2, 出生数) = **55,658** as written "55 658", value check pending births (2025-06-01..2025-06-30) [keep: ] quote: "6月 55 658 114 709 111 51 △ 59 051 607 706 185 31 156 14 564"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/nengai25/dl/gaikyouR7houdou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.crosshealthjp.org/articles/2026072705/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202507.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://d.hatena.ne.jp/keyword/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e7%b5%b1%e8%a8%88%e9%80%9f%e5%a0%b12025%e5%b9%b47%e6%9c%88%e5%88%86` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Annual and year-to-date birth totals from MHLW

Hypothesis: Annual births (2024, 2025) and year-to-date cumulative births through June 2026 (if published) constrain the July level via the historical July share of annual births.

Queries issued by the searcher: 厚生労働省 人口動態統計速報 2026年 出生数; Japan annual births 2025 厚生労働省 出生数 速報; 人口動態統計速報 令和7年7月 出生数 前年同月; 2026年1月 出生数 速報 厚生労働省 人口動態統計 月別; Japan annual births 2025 厚生労働省 出生数 人口動態統計; 2026年 上半期 出生数 速報 厚生労働省; 人口動態統計速報 2026年5月 出生数 厚生労働省; 人口動態統計速報 令和8年6月 出生数 外国人を含む; 人口動態統計速報 令和7年7月分 出生数 前年同月比; 2026年6月分 人口動態統計速報 出生数 7月24日 公表; 人口動態統計速報 2026年 出生数 厚生労働省; Japan births 2025 annual total 厚生労働省 出生数 速報 2025年; 人口動態統計速報 令和8年6月分 出生数 1月から当月までの累計; 2025年7月 出生数 速報 人口動態統計 6万人

- `https://www.nippon.com/ja/articles/-/55093` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p31 Japan total live births, May 2026 (preliminary monthly vital statistics, 出生) = **59,663** as written "59 663", value check ok births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p32 Japan total live births, May 2025 (preliminary, prior year comparison) = **60,718** as written "60 718", value check ok births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p33 Japan cumulative live births January-May 2026 (preliminary, １月から当月までの累計) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p34 Japan cumulative live births January-May 2025 (preliminary, prior year) = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p35 Japan live births in the 12 months June 2025-May 2026 (preliminary, 当月を含む過去１年間) = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p36 Japan live births in the 12 months June 2024-May 2025 (preliminary, prior year) = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p37 Japan national total live births, May 2026 (by prefecture table, 全国) = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p38 Japan national cumulative live births January-May 2026 (by prefecture table, 全国) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
  - p39 Japan annualized birth rate (年換算率) for May 2026, births per 1,000 population = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [keep: ] quote: "出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p40 Japan annualized birth rate (年換算率) for May 2025, births per 1,000 population = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [keep: ] quote: "出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p41 Japan annualized birth rate (年換算率) for cumulative January-May 2026, births per 1 = **5.6** births per 1,000 population (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p42 Japan annualized birth rate (年換算率) for cumulative January-May 2025, births per 1 = **5.5** births per 1,000 population (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p43 Japan annualized birth rate (年換算率) for 12 months June 2025-May 2026, births per  = **5.7** births per 1,000 population (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p44 Japan annualized birth rate (年換算率) for 12 months June 2024-May 2025, births per  = **5.7** births per 1,000 population (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p45 Japan year-on-year change in cumulative live births January-May 2026 vs 2025 (増減 = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/articles/print/54325` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nikkei.com/article/DGXZQOUA0197C0R00C26A6000000/` -> **snapshot** (snapshot 20260625233753); points raw/verified 15/12
  - p46 Japan total fertility rate (合計特殊出生率), 2025 preliminary (概数) = **1.14** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "厚生労働省が3日発表した2025年の人口動態統計(概数)によると、1人の女性が生涯で産む子どもの数を示す合計特殊出生率は1.14だった。"
  - p47 Japan total fertility rate, 2024 = **1.15** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "24年の1.15から0.01ポイント下がり、過去最低を更新した。"
  - p48 Japan births to Japanese nationals, 2025 preliminary (概数) = **671,236** births (2025-01-01..2025-12-31) [keep: ] quote: "25年に国内で生まれた日本人の子どもは67万1236人で、24年より1万4937人(2.2%)減った。"
  - p49 Year-on-year decrease in Japan births to Japanese nationals, 2025 vs 2024 = **14,937** births (2025-01-01..2025-12-31) [keep: ] quote: "25年に国内で生まれた日本人の子どもは67万1236人で、24年より1万4937人(2.2%)減った。"
  - p50 Year-on-year percentage decrease in Japan births to Japanese nationals, 2025 vs  = **2.2** % (2025-01-01..2025-12-31) [keep: ] quote: "25年に国内で生まれた日本人の子どもは67万1236人で、24年より1万4937人(2.2%)減った。"
  - p51 Japan marriages (婚姻件数), 2025 preliminary = **489,119** marriages (2025-01-01..2025-12-31) [keep: ] quote: "厚労省は婚姻件数が2年連続で増え、25年は0.8%増の48万9119組だったことなどを理由に挙げる。"
  - p52 Year-on-year percentage increase in Japan marriages, 2025 = **0.8** % (2025-01-01..2025-12-31) [keep: ] quote: "厚労省は婚姻件数が2年連続で増え、25年は0.8%増の48万9119組だったことなどを理由に挙げる。"
  - p53 Japan deaths, 2025 preliminary = **1,589,489** deaths (2025-01-01..2025-12-31) [keep: ] quote: "死亡数は158万9489人で5年ぶりに前年を下回った。"
  - p54 Japan natural change (births minus deaths), 2025 preliminary = **918,253** persons (2025-01-01..2025-12-31) [keep: ] quote: "出生と死亡の差である自然増減はマイナス91万8253人だった。"
  - p55 IPSS medium-variant projection of Japan total fertility rate for 2025 = **1.25** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "国立社会保障・人口問題研究所(社人研)が23年に公表した将来推計人口でメインシナリオとされる中位推計は25年の出生率を1.25と見積もっていた。"
  - p56 IPSS low-variant projection of Japan total fertility rate for 2025 = **1.1** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "現実は悲観シナリオの低位推計が見込んだ1.10に近づいた。"
  - p57 Number of years by which Japan's fertility decline is ahead of IPSS medium proje = **15** years (2025-01-01..2025-12-31) [DISCARD: Already discarded; a qualitative 'years ahead' statement, not a usable quantity.] quote: "想定より15年前倒しで少子化が進んでいる。"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://sp.m.jiji.com/article/show/3854705` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.swissinfo.ch/chi/%e6%97%a5%e6%9c%ac%e5%87%ba%e7%94%9f%e4%ba%ba%e6%95%b0%e8%bf%9e10%e5%b9%b4%e4%b8%8b%e6%bb%91%e3%80%80%e6%97%a5%e7%9b%b8%e` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e6%9c%88%e5%a0%b1%e8%aa%bf%e6%95%b4%e4%bf%82/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_05.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tokyo-np.co.jp/article/530333?rct=national` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period year 2018 does not appear in the page text or URL (likely mis-dated): 1; period year 2040 does not appear in the page text or URL (likely mis-dated): 2)

### d3 [related_series] Municipal and prefectural monthly birth notifications

Hypothesis: Some large cities/prefectures publish monthly birth counts earlier than national preliminary data; summing or scaling these to national coverage provides an independent July 2026 estimate.

Queries issued by the searcher: 東京都 出生数 月別 2026年7月; 人口動態統計速報 2026年7月 出生数; 東京都 子供政策連携室 出生数 2026年7月 増加; 大阪市 出生数 2026年7月 月別; 東京都 出生数 月別 2026年7月 人口動態統計; 人口動態統計速報 2026年7月 出生数; 東京都 2026年7月 出生数 8392人 人口動態統計 速報; 東京都 月別 出生数 2026年7月 子供政策連携室 発表; 東京都 出生数 月別 2026年7月; 人口動態統計速報 2026年7月 出生数; 横浜市 出生数 令和8年7月 人口動態 速報; 大阪市 出生数 2026年7月 月別

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.crosshealthjp.org/articles/2026092706/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e3%83%bb%e4%bf%9d%e5%81%a5%e7%a4%be%e4%bc%9a%e7%b5%b1%e8%a8%88%e5%ae%a4/` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040505435&iroha=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/07.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.am-consulting.co.jp/social-jpn-jinkou-doutai-toukei-sokuhou.html` -> **snapshot** (snapshot 20220715230052); points raw/verified 0/0
- `https://jp.asiadaily.org/news/17779/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://zhuanlan.zhihu.com/p/2086505697672441974` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sankei.com/article/20261124-KASSNYVECBMFPMOKZ3FUYANEMA/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://iza.ne.jp/article/20261105-2WPGL63WW5GYBFQAA7NAKBSJTU/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.metro.tokyo.lg.jp/ja/information/press/2026/07/2026073102` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Official population projections and research institute forecasts

Hypothesis: IPSS (国立社会保障・人口問題研究所) and private forecasts of 2026 monthly or annual births provide an independent anchor for the July 2026 level.

Queries issued by the searcher: 国立社会保障・人口問題研究所 2026 出生数 推計; Japan 2026 birth forecast monthly 出生数 予測 2026年; 2026年 出生数 予測 第一生命経済研究所 日本総研 2026年 65万人; 人口動態統計速報 令和8年5月 出生数 2026; 国立社会保障・人口問題研究所 2026 出生数 推計; Japan 2026 birth forecast 出生数 予測 2026年; 日本の将来推計人口 令和5年推計 参考推計表 出生数 2026年 日本人; 人口動態統計速報 2026年6月分 厚生労働省 出生数; 国立社会保障・人口問題研究所 2026 出生数 推計; Japan 2026 birth forecast monthly 出生数 予測; 2026年 出生数 予測 民間 研究機関; 人口動態統計速報 令和7年7月 出生数 速報値; 日本総合研究所 藤波匠 2026年 出生数 予測 横ばい; 出生数 月別 7月 年間 割合 人口動態統計 月次

- `https://kurashi-data.com/articles/shusseisu-yosoku/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://373news.com/news/national/detail/2026110401001093/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dlri.co.jp/report/macro/617726.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://research.nicoxz.com/articles/japan-fertility-rate-population-projection` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://iroiromirai.jp/wp-content/uploads/2026/03/20260331_WhitePaper2025.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://babiesmap.com/births/japan` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.com/zz08/n/n7fd22e86da6d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sankei.com./article/20260510-BY3MFI6NIJD23KXYH6EKTMQC5A/` -> **snapshot** (snapshot 20260511154028); points raw/verified 8/7
  - p58 Japan total live births, January 2026, preliminary (速報値), year-on-year compariso = **58,694** births (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p59 Japan total live births, February 2026, preliminary (速報値) = **50,761** births (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だったものの"
  - p60 Japan total live births, January-February 2026 cumulative, preliminary (速報値) = **109,455** births (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p61 Japan total live births, January-February 2026 cumulative, year-on-year change = **0.1** as written "0・1%", value check pending % (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p62 Japan total live births, January 2026, year-on-year change = **0.5** as written "0・5%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p63 Japan total live births, February 2026, year-on-year change = **0.4** as written "0・4%", value check pending % (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だったものの"
  - p64 Japan total live births, calendar year 1966 (previous 丙午 year), year-on-year dec = **25** % (1966-01-01..1966-12-31) [DISCARD: 1966 丙午 (fire-horse) year decline is a one-off cultural anomaly with no analogue to 2026; would distort any trend.] quote: "60年前の1966年は出生数が前年比25%も減少した"
- `https://www.47news.jp/13920092.html` -> **snapshot** (snapshot 20260404075650); points raw/verified 12/11
  - p65 Japan total live births including foreign nationals, 2025 preliminary (速報値) = **705,809** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年の外国人を含むわが国の出生数(速報値)は、70万5809人で過去最少となった。"
  - p66 Estimated Japanese-national live births for 2026 (forecast, year-on-year change) = **2.2** as written "2・2%減", value check pending % (2026-01-01..2026-12-31) [keep: ] quote: "例年6月に公表される日本人の出生数を試算すると、前年比2・2%減の67万1千人となる。"
  - p67 Japan total fertility rate, 2024 (actual, lowest on record) = **1.15** as written "1・15", value check pending births per woman (2024-01-01..2024-12-31) [keep: ] quote: "過去最低だった2024年の1・15を下回り、1・13程度となることが見込まれる。"
  - p68 Japan total fertility rate, 2025 (forecast) = **1.13** as written "1・13程度", value check pending births per woman (2025-01-01..2025-12-31) [keep: ] quote: "過去最低だった2024年の1・15を下回り、1・13程度となることが見込まれる。"
  - p69 Annual decline threshold exceeded by Japan births since 2022 = **5** % (2022-01-01..2025-12-31) [DISCARD: Threshold statement, not a measurement.] quote: "出生数は2022年から5%を超えて減少し続けていたが、その状況からは脱する見通しである。"
  - p70 Change in births, 20 designated major cities plus Tokyo 23 wards (preliminary) = **0.7** as written "0・7%の減少", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "全国20の政令指定都市と東京都区部(23区)を合わせた大都市では、出生数が0・7%の減少にとどまる一方"
  - p71 Change in births, areas outside major cities (preliminary) = **-2.8** as written "マイナス2・8%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "それらを除く地域ではマイナス2・8%と強めの減勢が続いている。"
  - p72 Change in births, Tokyo 23 wards (preliminary) = **1.4** as written "1・4%の増加", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "東京都区部が1・4%の増加に転じ、大阪市はマイナス0・1%の微減にとどまった。"
  - p73 Change in births, Osaka city (preliminary) = **-0.1** as written "マイナス0・1%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "東京都区部が1・4%の増加に転じ、大阪市はマイナス0・1%の微減にとどまった。"
  - p74 Change in births, Sagamihara city (preliminary) = **-7** as written "7・0%減", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "相模原市(7・0%減)や神戸市(4・5%減)のように全国平均を大きく超える減少率となった都市もある。"
  - p75 Change in births, Kobe city (preliminary) = **-4.5** as written "4・5%減", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "相模原市(7・0%減)や神戸市(4・5%減)のように全国平均を大きく超える減少率となった都市もある。"
- `https://community.jmp.com/t5/blogs/blogarticleprintpage/blog-id-nmasukawa-blog/article-id/94` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://caixinboke1.blog.caixin.com/archives/288480` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: no number in value_as_written: 1; number: scale conflict: '千' in value vs '万': 1)

### d5 [physical_flow] Pregnancy and conception timing / maternal health records

Hypothesis: Births in July 2026 correspond to conceptions around October 2025; maternal and child health handbook issuances or pregnancy notifications in late 2025 can proxy the birth cohort nine months later.

Queries issued by the searcher: 母子健康手帳 交付数 2025年 月別; 妊娠届 提出数 2025年 月別 統計; 厚生労働省 妊娠届出数の状況 2025年 月別 2025年10月; 人口動態統計速報 2026年 月別 出生数 厚生労働省; 母子健康手帳 交付数 2025年 月別 人口動態統計; 妊娠届 提出数 2025年 月別 厚生労働省; 人口動態統計速報 令和8年 2026年 出生数 月別 厚生労働省; 妊娠届出数 月別 2025年 厚生労働省 公表 令和7年; 母子健康手帳 交付数 2025年 月別; 妊娠届 提出数 2025 月別 統計; 厚生労働省 妊娠届出数の推移等 令和7年 月別 妊娠届出数; 人口動態統計速報 2026年 出生数 月別

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/stf/newpage_20613.html` -> **snapshot** (snapshot 20260317031935); points raw/verified 15/15
  - p76 Pregnancy reports (妊娠届出数) nationwide, February 2021 (Reiwa 3) = **70,747** pregnancy report (2021-02-01..2021-02-28) [DISCARD: Pregnancy-report series from 2020-21; too old and too far from the target period to bridge to July 2026 without a long, ] quote: "令和3年2月の妊娠届出数は70,747件であり、前年同月の71,478件と比較すると1.0%減。"
  - p77 Pregnancy reports (妊娠届出数) nationwide, February 2020 (previous year same month) = **71,478** pregnancy report (2020-02-01..2020-02-29) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年2月の妊娠届出数は70,747件であり、前年同月の71,478件と比較すると1.0%減。"
  - p78 Year-on-year change in pregnancy reports, February 2021 vs February 2020 = **1** % (2021-02-01..2021-02-28) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年2月の妊娠届出数は70,747件であり、前年同月の71,478件と比較すると1.0%減。"
  - p79 Pregnancy reports (妊娠届出数) nationwide, March 2021 (Reiwa 3) = **81,717** pregnancy report (2021-03-01..2021-03-31) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年3月の妊娠届出数は81,717件であり、前年同月の78,339件と比較すると4.3%増。"
  - p80 Pregnancy reports (妊娠届出数) nationwide, March 2020 (previous year same month) = **78,339** pregnancy report (2020-03-01..2020-03-31) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年3月の妊娠届出数は81,717件であり、前年同月の78,339件と比較すると4.3%増。"
  - p81 Year-on-year change in pregnancy reports, March 2021 vs March 2020 = **4.3** % (2021-03-01..2021-03-31) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年3月の妊娠届出数は81,717件であり、前年同月の78,339件と比較すると4.3%増。"
  - p82 Pregnancy reports (妊娠届出数) nationwide, April 2021 (Reiwa 3) = **73,908** pregnancy report (2021-04-01..2021-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年4月の妊娠届出数は73,908件であり、前年同月の75,541件と比較すると2.2%減。"
  - p83 Pregnancy reports (妊娠届出数) nationwide, April 2020 (previous year same month) = **75,541** pregnancy report (2020-04-01..2020-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年4月の妊娠届出数は73,908件であり、前年同月の75,541件と比較すると2.2%減。"
  - p84 Year-on-year change in pregnancy reports, April 2021 vs April 2020 = **2.2** % (2021-04-01..2021-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "令和3年4月の妊娠届出数は73,908件であり、前年同月の75,541件と比較すると2.2%減。"
  - p85 Cumulative pregnancy reports (妊娠届出数) nationwide, January-April 2021 (Reiwa 3) = **304,425** pregnancy report (2021-01-01..2021-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "また、令和3年1-4月の累計妊娠届出数は304,425件であり、前年同期間の308,178件と比較すると1.2%減でした。"
  - p86 Cumulative pregnancy reports (妊娠届出数) nationwide, January-April 2020 (previous ye = **308,178** pregnancy report (2020-01-01..2020-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "また、令和3年1-4月の累計妊娠届出数は304,425件であり、前年同期間の308,178件と比較すると1.2%減でした。"
  - p87 Year-on-year change in cumulative pregnancy reports, January-April 2021 vs Janua = **1.2** % (2021-01-01..2021-04-30) [DISCARD: Same 2020-21 pregnancy-report series; unusable for 2026.] quote: "また、令和3年1-4月の累計妊娠届出数は304,425件であり、前年同期間の308,178件と比較すると1.2%減でした。"
  - p88 Share of pregnant women filing pregnancy report by week 11 of pregnancy, FY2019  = **93.5** % (2019-04-01..2020-03-31) [DISCARD: Notification-timing share from FY2019; not needed and not transferable to 2026 without a bridge.] quote: "厚生労働省では、妊娠11週以下の時期の届出を勧奨しており、令和元年度には93.5%の妊婦が、妊娠11週までに届出を行っている。"
  - p89 Year-on-year change in pregnancy reports, FY2015 (Heisei 27) = **2.1** % (2015-04-01..2016-03-31) [DISCARD: FY2015 pregnancy-report change; too old and irrelevant to 2026.] quote: "平成27年度 2.1%減、平成28年度 4.2%減、平成29年度 2.3%減、"
  - p90 Year-on-year change in pregnancy reports, FY2018 (Heisei 30) = **5.3** % (2018-04-01..2019-03-31) [DISCARD: FY2018 pregnancy-report change; too old and irrelevant to 2026.] quote: "平成30年度 5.3%減、令和元年度 2.1%減"
- `https://warp.ndl.go.jp/info:ndljp/pid/11735397/www.mhlw.go.jp/content/11920000/000824098.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 15/15
  - p91 Japan total live births, March 2025 (preliminary monthly vital statistics, all p = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p92 Japan total live births, March 2024 (preliminary, prior year comparison) = **55,198** as written "55 198", value check pending births (2024-03-01..2024-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p93 Japan cumulative live births, January-March 2025 (preliminary) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p94 Japan cumulative live births, January-March 2024 (preliminary) = **170,804** as written "170 804", value check pending births (2024-01-01..2024-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p95 Japan live births, trailing 12 months April 2024-March 2025 (preliminary) = **713,139** as written "713 139", value check pending births (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p96 Japan live births, trailing 12 months April 2023-March 2024 (preliminary) = **746,958** as written "746 958", value check pending births (2023-04-01..2024-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p97 Japan year-on-year change in trailing-12-month live births (April 2024-March 202 = **4.5** % (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p98 Japan year-on-year change in March 2025 live births, percent = **2.9** % (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p99 Japan year-on-year change in January-March 2025 cumulative live births, percent = **4.6** % (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p100 Japan annualised birth rate per 1,000 population, March 2025 (year-converted rat = **5.1** births per 1,000 population (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p101 Japan annualised birth rate per 1,000 population, trailing 12 months April 2024- = **5.8** births per 1,000 population (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p102 Tokyo prefecture live births, March 2025 (by place of report) = **6,406** as written "6 406", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "13 東 京 6 406 12 592 180 8 843 2 104"
  - p103 Tokyo prefecture cumulative live births, January-March 2025 (by place of report) = **19,550** as written "19 550", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "13 東 京 19 550 40 339 516 21 520 5 375"
  - p104 Tokyo 23 wards (東京都区部) live births, March 2025 = **4,667** as written "4 667", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "東京都区部 4 667 8 231 144 7 190 1 499"
  - p105 Tokyo 23 wards (東京都区部) cumulative live births, January-March 2025 = **14,311** as written "14 311", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "東京都区部 14 311 26 550 394 17 502 3 876"
- `https://mhlw-grants.niph.go.jp/system/files/2012/121011/201201015B/201201015B0006.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://covid19outputjapan.github.io/JP/files/ChibaNakata_Birth_20220208.pdf` -> **snapshot** (snapshot 20250520084816); points raw/verified 15/12
  - p106 Average period from conception to pregnancy notification (Japan, general) = **7.5** week (not stated (page dated 2022-02-08)) [DISCARD: Generic conception-to-notification interval; no 2026 pregnancy-report data to apply it to.] quote: "妊娠から妊娠届出までの平均期間は約7.5週間(約2か月)※1であることを考慮して"
  - p107 Average period from conception to birth (Japan, general) = **38** week (not stated (page dated 2022-02-08)) [DISCARD: Generic conception-to-birth interval; no 2026 conception data to apply it to.] quote: "妊娠から出産までの平均期間は約38週間(約9か月)※1であることを考慮して"
  - p108 Pregnancy-to-notification interval, lower bound of range (timeline chart) = **7.5** (range 6..9) as written "6~9週間", value check pending week (not stated (page dated 2022-02-08)) [DISCARD: Timeline-chart interval bound; no 2026 data to apply it to.] quote: "6~9週間 (1.5~2か月)"
  - p109 Notification-to-birth interval, lower bound of range (timeline chart) = **30.5** (range 29..32) as written "29~32週間", value check pending week (not stated (page dated 2022-02-08)) [DISCARD: Timeline-chart interval bound; no 2026 data to apply it to.] quote: "29~32週間 (6.75~7.5か月)"
  - p110 Estimated 2021 annual births (confirmed-value basis, Japan) = **810,000** birth (2021-01-01..2021-12-31) [DISCARD: 2021 estimated births; superseded by actual 2025/2026 preliminary data.] quote: "2021年の出生数(確定値ベースの推計値)は約81万人程度となる可能性"
  - p111 Shortfall of 2021 estimated births below pre-COVID trend (Japan) = **50,000** birth (2021-01-01..2021-12-31) [DISCARD: 2021 COVID shortfall estimate; not applicable to 2026.] quote: "トレンドを約5万人(5.7%)下回る"
  - p112 Shortfall of 2021 estimated births below trend, share (Japan) = **5.7** % (2021-01-01..2021-12-31) [DISCARD: 2021 COVID shortfall share; not applicable to 2026.] quote: "トレンドを約5万人(5.7%)下回る"
  - p113 Shortfall of 2019 and 2020 births below trend (Japan) = **35,000** (range 30,000..40,000) as written "3-4万人", value check pending birth (2019-01-01..2020-12-31) [DISCARD: 2019-2020 shortfall; not applicable to 2026.] quote: "2019年、2020年もトレンドを3-4万人下回っていたため"
  - p114 Pre-COVID trend counterfactual births, January 2021 (Japan) = **72,000** birth (2021-01-01..2021-01-31) [DISCARD: 2021 counterfactual; not applicable to 2026.] quote: "ビフォー・コロナのトレンド(2010年1月~2020年10月)に従った場合、2021年1月の出生数は72,000人"
  - p115 Actual January 2021 births shortfall vs trend (Japan) = **11,000** birth (2021-01-01..2021-01-31) [DISCARD: 2021 shortfall; not applicable to 2026.] quote: "実際は、それより約11,000人(16%)少なかった"
  - p116 Actual Jan-Feb 2021 births shortfall vs trend (Japan) = **26,000** birth (2021-01-01..2021-02-28) [DISCARD: 2021 shortfall; not applicable to 2026.] quote: "実際は、それより約26,000人(18%)少なかった"
  - p117 Average years from marriage to first child birth (Japan) = **2.5** year (not stated (page dated 2022-02-08)) [DISCARD: Average marriage-to-first-birth interval; no usable 2026 marriage-cohort data to apply it to.] quote: "結婚してからの第1子出産までの平均年数は約2.5年"
- `http://search.ckan.jp/datasets/data.bodik.jp__dataset:232114_maternal_and_child_health_handbook` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/content/11920000000824098.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/10.html` -> **snapshot** (snapshot 20260317070608); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/dl/toukeihyo_10.pdf` -> **snapshot** (snapshot 20260521112927); points raw/verified 15/15
  - p118 Japan total live births, October 2025 (provisional monthly vital statistics, Jap = **59,979** as written "59 979", value check ok births (2025-10-01..2025-10-31) [keep: ] quote: "10 月 59 979 60 213 △ 234 △ 0.4 5.9 5.9"
  - p119 Japan total live births, October 2024 (comparison year, provisional) = **60,213** as written "60 213", value check ok births (2024-10-01..2024-10-31) [keep: ] quote: "10 月 59 979 60 213 △ 234 △ 0.4 5.9 5.9"
  - p120 Japan cumulative live births, January-October 2025 = **556,091** as written "556 091", value check pending births (2025-01-01..2025-10-31) [keep: ] quote: "累 計 1月~10月 556 091 571 274 △ 15 183 △ 2.7 5.6 5.7"
  - p121 Japan cumulative live births, January-October 2024 = **571,274** as written "571 274", value check pending births (2024-01-01..2024-10-31) [keep: ] quote: "累 計 1月~10月 556 091 571 274 △ 15 183 △ 2.7 5.6 5.7"
  - p122 Japan monthly live births, July 2025 (monthly table) = **60,650** as written "60 650", value check ok births (2025-07-01..2025-07-31) [keep: ] quote: "7月 60 650 118 288 92 42 △ 57 638 615 735 177 57 390 14 964"
  - p123 Japan monthly live births, July 2024 (monthly table) = **62,306** as written "62 306", value check ok births (2024-07-01..2024-07-31) [keep: ] quote: "7月 62 306 126 383 115 51 △ 64 077 567 680 204 46 747 15 630"
  - p124 Japan monthly live births, September 2025 (monthly table) = **57,407** as written "57 407", value check ok births (2025-09-01..2025-09-30) [keep: ] quote: "9月 57 407 119 256 84 35 △ 61 849 570 650 179 26 172 14 862"
  - p125 Japan monthly live births, August 2025 (monthly table) = **58,976** as written "58 976", value check ok births (2025-08-01..2025-08-31) [keep: ] quote: "8月 58 976 122 085 99 50 △ 63 109 615 639 219 41 518 13 518"
  - p126 Japan live birth rate per 1,000 population, October 2025 = **5.9** births per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "5.9 12.4 1.6 0.9 △ 6.5 9.7 11.4 3.4 4.0 1.51 10月"
  - p127 Japan live birth rate per 1,000 population, July 2025 = **6** births per 1,000 population (2025-07-01..2025-07-31) [keep: ] quote: "6.0 11.6 1.6 0.7 △ 5.7 9.9 11.9 2.9 5.6 1.47 7月"
  - p128 Japan live birth rate per 1,000 population, July 2024 = **6.1** births per 1,000 population (2024-07-01..2024-07-31) [keep: ] quote: "6.1 12.4 1.9 0.8 △ 6.3 8.9 10.7 3.3 4.6 1.53 7月"
  - p129 Japan total live births, October 2025, by prefecture table (national row) = **59,979** as written "59 979", value check pending births (2025-10-01..2025-10-31) [keep: ] quote: "全 国 59 979 30 736 29 243 125 507 63 850 61 657 94 44"
  - p130 Tokyo prefecture live births, October 2025 = **7,918** as written "7 918", value check pending births (2025-10-01..2025-10-31) [keep: ] quote: "13 東 京 7 918 4 030 3 888 11 102 5 648 5 454 9 4"
  - p131 Tokyo prefecture cumulative live births, January-October 2025 = **70,299** as written "70 299", value check pending births (2025-01-01..2025-10-31) [keep: ] quote: "13 東 京 70 299 36 222 34 077 113 451 58 264 55 187 97 47"
  - p132 Japan total live births, October 2025, foreign nationals (separate row) = **3** births (2025-10-01..2025-10-31) [DISCARD: Foreign-national October 2025 births = 3; implausibly small and unusable as a scope adjustment.] quote: "外 国 3 1 2 19 15 4 - -"
- `https://data.bodik.jp/dataset/472115_9-14_ninsinntodokedejoukyou_20200401` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://pulmo.jp/29361/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (number: more than one number in value_as_written: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d6 [shocks] Calendar and demographic shocks affecting July 2026 births

Hypothesis: July 2026 has no leap-day effect; any changes in marriage rates, COVID-era conception dips, or policy changes (e.g., childcare subsidies) around late 2025 could shift the level relative to trend.

Queries issued by the searcher: Japan monthly births 2025 人口動態統計速報 出生数 月別; Japan marriages 2025 monthly 婚姻数 人口動態統計; 人口動態統計速報 令和8年 2026年 出生数 月別 上半年; 2026年 出生数 上半期 前年比 厚労省 速報 2026年8月; 人口動態統計速報 令和7年7月分 出生数 前年同月比; 2026年1月 婚姻件数 速報 増加 2025年 婚姻数 月別; 人口動態統計速報 2026年 出生数; Japan monthly births 2026 preliminary vital statistics; 人口動態統計速報 令和8年6月分 出生数 厚生労働省; 2025年 出生数 70万5800 速報 婚姻数 増加; 人口動態統計速報 2026年 出生数; Japan monthly births 2025 preliminary vital statistics 出生数 月別; 2026年上半期 出生数 34万2068人 速報 厚労省 外国人含む; 2025年 婚姻数 増加 厚労省 人口動態統計 婚姻件数 48万組

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e4%ba%ba%e5%8f%a3%e5%8b%95%e6%85%8b%e3%83%bb%e4%bf%9d%e5%81%a5%e7%a4%be%e4%bc%9a%e7%b5%b1%e8%a8%88%e5%ae%a4/page/3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p133 Japan live births, May 2026 (preliminary monthly vital statistics, all persons i = **59,663** as written "59 663", value check ok births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p134 Japan live births, May 2025 (preliminary, prior year) = **60,718** as written "60 718", value check ok births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p135 Japan live births, year-on-year change, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p136 Japan live births, year-on-year change rate, May 2026 vs May 2025 = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p137 Japan marriages, May 2026 (preliminary) = **41,169** as written "41 169", value check pending marriages (2026-05-01..2026-05-31) [keep: ] quote: "婚 姻 41 169 43 257 △ 2 088 △ 4.8 3.9 4.1 95.6"
  - p138 Japan marriages, May 2025 (preliminary, prior year) = **43,257** as written "43 257", value check pending marriages (2025-05-01..2025-05-31) [keep: ] quote: "婚 姻 41 169 43 257 △ 2 088 △ 4.8 3.9 4.1 95.6"
  - p139 Japan marriages, year-on-year change rate, May 2026 vs May 2025 = **4.8** % (2026-05-01..2026-05-31) [keep: ] quote: "婚 姻 41 169 43 257 △ 2 088 △ 4.8 3.9 4.1 95.6"
  - p140 Japan live births, cumulative January-May 2026 (preliminary) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p141 Japan live births, cumulative January-May 2025 (preliminary, prior year) = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p142 Japan marriages, cumulative January-May 2026 (preliminary) = **206,971** as written "206 971", value check pending marriages (2026-01-01..2026-05-31) [keep: ] quote: "婚 姻 206 971 206 142 829 0.4 4.1 4.0 100.9"
  - p143 Japan marriages, cumulative January-May 2025 (preliminary, prior year) = **206,142** as written "206 142", value check pending marriages (2025-01-01..2025-05-31) [keep: ] quote: "婚 姻 206 971 206 142 829 0.4 4.1 4.0 100.9"
  - p144 Japan live births, trailing 12 months June 2025-May 2026 (preliminary) = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p145 Japan live births, trailing 12 months June 2024-May 2025 (preliminary, prior yea = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p146 Japan marriages, trailing 12 months June 2025-May 2026 (preliminary) = **506,485** as written "506 485", value check pending marriages (2025-06-01..2026-05-31) [keep: ] quote: "婚 姻 506 485 490 791 15 694 3.2 4.1 4.0 103.7"
  - p147 Japan marriages, trailing 12 months June 2024-May 2025 (preliminary, prior year) = **490,791** as written "490 791", value check pending marriages (2024-06-01..2025-05-31) [keep: ] quote: "婚 姻 506 485 490 791 15 694 3.2 4.1 4.0 103.7"
- `https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040527115&fileKind=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 15/15
  - p148 Japan monthly live births, March 2025 (preliminary vital statistics, all Japan i = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p149 Japan monthly live births, March 2024 (preliminary, prior year) = **55,198** as written "55 198", value check pending births (2024-03-01..2024-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p150 Japan monthly marriages, March 2025 (preliminary, all Japan) = **55,762** as written "55 762", value check pending marriages (2025-03-01..2025-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p151 Japan monthly marriages, March 2024 (preliminary, prior year) = **56,864** as written "56 864", value check pending marriages (2024-03-01..2024-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p152 Japan cumulative live births, Jan-Mar 2025 (preliminary) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p153 Japan cumulative live births, Jan-Mar 2024 (preliminary, prior year) = **170,804** as written "170 804", value check pending births (2024-01-01..2024-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p154 Japan cumulative marriages, Jan-Mar 2025 (preliminary) = **131,332** as written "131 332", value check pending marriages (2025-01-01..2025-03-31) [keep: ] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p155 Japan cumulative marriages, Jan-Mar 2024 (preliminary, prior year) = **136,653** as written "136 653", value check pending marriages (2024-01-01..2024-03-31) [keep: ] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p156 Japan live births, trailing 12 months Apr 2024-Mar 2025 (preliminary) = **713,139** as written "713 139", value check pending births (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p157 Japan live births, trailing 12 months Apr 2023-Mar 2024 (preliminary, prior year = **746,958** as written "746 958", value check pending births (2023-04-01..2024-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p158 Japan marriages, trailing 12 months Apr 2024-Mar 2025 (preliminary) = **494,678** as written "494 678", value check pending marriages (2024-04-01..2025-03-31) [keep: ] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p159 Japan marriages, trailing 12 months Apr 2023-Mar 2024 (preliminary, prior year) = **491,082** as written "491 082", value check pending marriages (2023-04-01..2024-03-31) [keep: ] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p160 Japan year-converted birth rate, March 2025 (per 1,000 population) = **5.1** births per 1,000 population (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p161 Japan year-converted marriage rate, March 2025 (per 1,000 population) = **5.3** marriages per 1,000 population (2025-03-01..2025-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p162 Japan year-converted marriage rate, trailing 12 months Apr 2024-Mar 2025 (per 1, = **4** marriages per 1,000 population (2024-04-01..2025-03-31) [keep: ] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
- `https://www.hoikusys.jp/post/%E5%8A%A0%E9%80%9F%E3%81%99%E3%82%8B%E5%B0%91%E5%AD%90%E5%8C%96%E3%81%8C%E9%88%8D%E5%8C%96%E3%81%99%E3%82%8B%E5%8F%AF%E8%` -> **snapshot** (snapshot 20260609083701); points raw/verified 15/5
  - p163 Japan live births, January–June 2025 (preliminary, same period prior year) = **350,074** births (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 prior-year value; superseded by the Jan-May 2026/2025 cumulative pair (p5/p6) and adds no new information.] quote: "今年1月から6月までに生まれた子どもは33万9280人で、昨年の35万74人に比べて1万794人の減少となっています。"
  - p164 Year-on-year decline in Japan live births, January–June 2025 vs 2024 = **20,978** births (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 decline; superseded by the Jan-May 2026/2025 cumulative pair.] quote: "これは、前年同期の2万978人に比べて半分程度となっています。"
  - p165 Japan live births, full year 2025 (preliminary, prior year) = **686,000** births (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 preliminary 686,000; conflicts with the more precise all-person 705,809 (p65) and is a different/rounded ] quote: "昨年1年間の出生数は、前年より4万人あまり少ない約68万6000人でした"
  - p166 Year-on-year decline in Japan live births, full year 2025 vs 2024 = **40,000** births (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 decline of 40,000; inconsistent with p65/p48 and superseded.] quote: "昨年1年間の出生数は、前年より4万人あまり少ない約68万6000人でした"
  - p167 Japan marriages, January–June 2025 (same period prior year) = **246,382** marriages (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 marriages prior-year; superseded by p142/p143.] quote: "婚姻件数が24万8513件となっていて、昨年の24万6382件を2131件とわずかに上回っていることです。"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_05.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sanyonews.jp/article/1821059?rct=global_syuyo` -> **snapshot** (snapshot 20251104110829); points raw/verified 11/9
  - p168 Live births in Japan, January-June 2025 (provisional, excluding foreign national = **319,079** births (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 Japanese-resident births; different scope and superseded by the all-person Jan-May pair.] quote: "2025年上半期(1~6月)に生まれた赤ちゃんの数は、前年同期比3・3%減の31万9079人となった。外国人は含まない。"
  - p169 Year-on-year change in Japan live births, January-June 2025 vs January-June 2024 = **3.3** as written "3・3%減", value check pending % (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 change; superseded.] quote: "2025年上半期(1~6月)に生まれた赤ちゃんの数は、前年同期比3・3%減の31万9079人となった。"
  - p170 Live births in Japan, June 2025 (monthly) = **55,658** births (2025-06-01..2025-06-30) [DISCARD: June 2025 monthly births; duplicate of p30.] quote: "出生数を月別でみると、6月は5万5658人で前年を345人上回ったものの、1~5月はいずれも前年を下回った。"
  - p171 Year-on-year change in Japan live births, June 2025 vs June 2024 = **345** births (2025-06-01..2025-06-30) [DISCARD: June 2025 change; superseded.] quote: "6月は5万5658人で前年を345人上回ったものの、1~5月はいずれも前年を下回った。"
  - p172 Marriages in Japan, January-June 2025 (provisional) = **230,166** marriages (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 marriages; superseded by p142/p143.] quote: "婚姻数は4・3%減の23万166組。"
  - p173 Year-on-year change in Japan marriages, January-June 2025 vs January-June 2024 = **4.3** as written "4・3%減", value check pending % (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 marriage change; superseded.] quote: "婚姻数は4・3%減の23万166組。"
  - p174 Deaths in Japan, January-June 2025 (provisional) = **823,343** deaths (2025-01-01..2025-06-30) [DISCARD: Deaths; irrelevant to births.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
  - p175 Year-on-year change in Japan deaths, January-June 2025 vs January-June 2024 = **2.9** as written "2・9%増", value check pending % (2025-01-01..2025-06-30) [DISCARD: Deaths change; irrelevant to births.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
  - p176 Natural decrease (births minus deaths) in Japan, January-June 2025 = **504,264** persons (2025-01-01..2025-06-30) [DISCARD: Natural decrease; irrelevant to births.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
- `https://www.saga-s.co.jp/articles/-/1586660` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.okinawatimes.co.jp/articles/-/1706167` -> **snapshot** (snapshot 20251104200329); points raw/verified 11/9
  - p177 Live births in Japan, January–June 2025 (provisional, excluding foreign national = **3.3** as written "3・3%減", value check pending % (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 Japanese-resident change; superseded.] quote: "2025年上半期(1~6月)に生まれた赤ちゃんの数は、前年同期比3・3%減の31万9079人となった。"
  - p178 Live births in Japan, January–June 2025 (provisional, excluding foreign national = **319,079** births (2025-01-01..2025-06-30) [DISCARD: Jan-Jun 2025 Japanese-resident births; superseded.] quote: "2025年上半期(1~6月)に生まれた赤ちゃんの数は、前年同期比3・3%減の31万9079人となった。外国人は含まない。"
  - p179 Deaths in Japan, January–June 2025 (provisional), year-on-year change = **2.9** as written "2・9%増", value check pending % (2025-01-01..2025-06-30) [DISCARD: Deaths change; irrelevant.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
  - p180 Deaths in Japan, January–June 2025 (provisional) = **823,343** deaths (2025-01-01..2025-06-30) [DISCARD: Deaths; irrelevant.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
  - p181 Natural decrease (deaths minus births) in Japan, January–June 2025 (provisional) = **504,264** persons (2025-01-01..2025-06-30) [DISCARD: Natural decrease; irrelevant.] quote: "上半期の死亡数は2・9%増の82万3343人で、出生数と差し引きした自然減は50万4264人だった。"
  - p182 Marriages in Japan, January–June 2025 (provisional), year-on-year change = **4.3** as written "4・3%減", value check pending % (2025-01-01..2025-06-30) [DISCARD: Marriage change; superseded.] quote: "婚姻数は4・3%減の23万166組。"
  - p183 Marriages in Japan, January–June 2025 (provisional) = **230,166** marriages (2025-01-01..2025-06-30) [DISCARD: Marriages; superseded.] quote: "婚姻数は4・3%減の23万166組。"
  - p184 Live births in Japan, June 2025 (provisional, monthly) = **55,658** births (2025-06-01..2025-06-30) [DISCARD: June 2025 monthly births; duplicate of p30.] quote: "出生数を月別でみると、6月は5万5658人で前年を345人上回ったものの、1~5月はいずれも前年を下回った。"
  - p185 Year-on-year increase in live births in Japan, June 2025 (provisional, monthly) = **345** births (2025-06-01..2025-06-30) [DISCARD: June 2025 change; superseded.] quote: "出生数を月別でみると、6月は5万5658人で前年を345人上回ったものの、1~5月はいずれも前年を下回った。"
- `https://www.at-s.com/wv/news/article/national/1841068.html?news=1779041` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/10.html` -> **snapshot** (snapshot 20260410162316); points raw/verified 0/0
- dropped by code checks: 14 (period year 2026 does not appear in the page text or URL (likely mis-dated): 10; period year 2024 does not appear in the page text or URL (likely mis-dated): 4)

### b1 [related_series] national monthly vital statistics

Hypothesis: June 2026 preliminary births (published ~late August 2026) would give the most recent month before July and let the year-on-year growth of the latest 1-3 months anchor the July 2026 estimate via series_auto; it is the single missing input that most tightens the forecast.

Queries issued by the searcher: 厚生労働省 人口動態統計速報 令和8年6月; www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo 2026年6月 速報; 人口動態統計速報 令和7年6月 出生数 速報 2025年6月; "202606.pdf" 人口動態統計速報 出生数 前年同月 増減; 厚生労働省 人口動態統計速報 令和8年6月; 人口動態統計速報 2026年6月 出生数; 人口動態統計速報 令和7年7月分 出生数 2025年7月; mhlw.go.jp toukei saikin hw jinkou geppo s2026 月別 出生数 2026年1月 2月 3月 4月 5月; 厚生労働省 人口動態統計速報 令和8年6月; www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo 2026年6月 速報; 人口動態統計速報 令和7年7月分 出生数 2025年7月; "202606.pdf" 人口動態統計速報 令和8年6月 出生数 前年同月

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/articles/print/54325` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://24h-care.com/statistics/20260828-2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20260&month=12040606&tclass1=0000010` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hoikusys.jp/post/この半年の出生数は増加に転じたが` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wic-net.com/publisher/%e6%9c%88%e5%a0%b1%e8%aa%bf%e6%95%b4%e4%bf%82/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 1/0
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/06.html` -> **snapshot** (snapshot 20260317070738); points raw/verified 2/1
  - p186 Reference month of the preliminary vital statistics report (Reiwa 7 June) = **6** month (2025-06-01..2025-06-30) [keep: ] quote: "人口動態統計速報(令和7年6月分)"
- dropped by code checks: 2 (number: more than one number in value_as_written: 2)

### b2 [related_series] sub-national monthly births

Hypothesis: Tokyo 23 wards or other large cities publish monthly birth counts earlier than the national preliminary; a July 2026 city-level count scaled by the city's historical share of national July births would provide an independent July 2026 anchor.

Queries issued by the searcher: 東京都 区部 出生数 2026年7月 人口動態; Tokyo metropolitan monthly population estimates births July 2026; 東京都 人口動態統計速報 令和8年 月別 出生数 2026; 東京都 月別 出生数 7月 区部 割合 全国 シェア; 東京都 区部 出生数 2026年7月 人口動態; Tokyo metropolitan monthly population estimates births July 2026; 東京都の人口推計 令和8年7月1日現在 自然増減 出生数; 人口動態統計速報 令和8年6月分 出生数 東京都; 東京都 人口の動き 詳細集計 令和8年 出生数 月別 総数 日本人 外国人; 人口動態統計速報 令和8年5月分 出生数 厚生労働省 2026; 東京都 人口動態統計速報 2026年 出生数 月別; 東京都 区部 出生数 2026年7月; 東京都 人口動態統計速報 令和8年 月報 出生数 保健医療局; 東京都の人口推計 令和8年 自然増減 出生数 区市町村別 2026

- `https://www.toukei.metro.tokyo.lg.jp/jsuikei/2026/js267f0000.pdf` -> **snapshot** (snapshot 20260807204246); points raw/verified 0/0
- `https://www.city.toshima.lg.jp/documents/56063/1-10-r7.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://zhuanlan.zhihu.com/p/2086505697672441974` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jtsutsui-lang.github.io/tokyo-fertility-notes/tokyo_factsheet_review.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jri.co.jp/file/report/research/pdf/16351.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.komei.or.jp/km/yachiyo-takahashi-hideyuki/2026/06/07/%e6%9d%b1%e4%ba%ac%e3%81%ae%e5%87%ba%e7%94%9f%e5%a2%97%e3%80%81%e6%94%af%e6%8f%b4%e7%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hokeniryo.metro.tokyo.lg.jp/documents/d/hokeniryo/p025-040-1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hokeniryo.metro.tokyo.lg.jp/documents/d/hokeniryo/r6kaku-3-pdf` -> **snapshot** (snapshot 20260122035514); points raw/verified 15/11
  - p187 Tokyo Metropolis total live births, calendar year 2024 (Japanese residents only, = **84,207** births (2024-01-01..2024-12-31) [keep: ] quote: "出生数は 84,207 人で、令和5年の 86,348 人より 2,141 人(2.5%)減少した。"
  - p188 Tokyo 23 wards (区部) live births, calendar year 2024 = **61,449** as written "61 449", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "区 部 61 449 92 337 89 1 42842 61 219 168 14 786"
  - p189 National (全国) live births, calendar year 2024, as cited in Tokyo report = **686,173** as written "686 173", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "( 全 国 ) 686 173 1 605 378 1 266 15 323 637 485 092 2 285 185 904"
  - p190 Tokyo Metropolis share of national live births, 2024 (index, national = 100) = **110** 1 (2024-01-01..2024-12-31) [keep: ] quote: "総 数 110.5 78.2 72.2 66.7 103.2 81.8 142.5 98.1"
  - p191 Tokyo 23 wards (区部) share of national live births, 2024 (index, national = 100) = **109** 1 (2024-01-01..2024-12-31) [keep: ] quote: "区 部 108.8 70.7 77.8 77.8 104.1 81.8 155.0 96.8"
  - p192 Tokyo Metropolis total live births, calendar year 2023 = **86,348** as written "86 348", value check pending births (2023-01-01..2023-12-31) [keep: ] quote: "23 5 86 348 137 241 135 60 △ 50 893 1 934 266 71 774 20 016"
  - p193 Tokyo Metropolis total live births, calendar year 2020 = **99,661** as written "99 661", value check pending births (2020-01-01..2020-12-31) [keep: ] quote: "2020 2 99 661 121 219 135 61 △ 21 558 2 076 296 73 931 20 783"
  - p194 Tokyo Metropolis total live births, calendar year 2019 (令和元年) = **101,818** as written "101 818", value check pending births (2019-01-01..2019-12-31) [keep: ] quote: "19 令和元年 101 818 120 870 146 59 △ 19 052 2 303 308 86 059 22 707"
  - p195 Tokyo Metropolis total live births, calendar year 2017 = **108,990** as written "108 990", value check pending births (2017-01-01..2017-12-31) [keep: ] quote: "17 29 108 990 116 453 169 86 △ 7 463 2 298 373 84 993 23 055"
  - p196 Tokyo Metropolis total live births, calendar year 2015 = **113,194** as written "113 194", value check pending births (2015-01-01..2015-12-31) [keep: ] quote: "15 27 113 194 111 673 189 89 1 521 2 406 368 87 169 24 135"
  - p197 Tokyo Metropolis total live births, calendar year 2014 = **110,629** as written "110 629", value check pending births (2014-01-01..2014-12-31) [keep: ] quote: "14 26 110 629 111 024 205 89 △ 395 2 460 388 87 000 23 653"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ntv.co.jp/englishnews/articles/20212pax880pomrz5klv.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://view.inews.qq.com/wxn/20261106A06CNO00?tbkt=F&openid=o04IBAEHI6F1RctG6h06ZN3WRgog&uid=&strategy=&refer=wx_hot&reJumped=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nli-research.co.jp/report/detail/id=86610` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period year 2022 does not appear in the page text or URL (likely mis-dated): 1; period year 2021 does not appear in the page text or URL (likely mis-dated): 1; period year 2018 does not appear in the page text or URL (likely mis-dated): 1; period year 2016 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [base_rates] seasonal pattern

Hypothesis: The July share of annual births and the month-to-month seasonal factor (July typically above the annual monthly average) would let the 2026 annual forecast (from p65/p66 trend) be converted to a July level; this resolves the largest uncertainty in the level route.

Queries issued by the searcher: 人口動態統計 月別 出生数 7月 年間 割合; 2026年 出生数 予測 年間; 人口動態統計速報 令和8年 2026年 出生数 6月; 2025年 出生数 月別 1月 2月 3月 4月 5月 6月 7月 日本人 人口動態統計; 人口動態統計 月別 出生数 7月 年間 割合; 2026年 出生数 予測 年間; 人口動態統計速報 令和8年 出生数 月別 外国人含む; 2025年 年間出生数 70万人 月別 出生数 1月 2月 12月 人口動態統計速報; 人口動態統計 月別 出生数 7月 年間 割合; 2026年 出生数 予測 年間; 人口動態統計速報 2026年 出生数 月別 厚生労働省; 2025年 人口動態統計 速報 年間 出生数 70万5800 外国人含む

- `https://warp.da.ndl.go.jp/info:ndljp/pid/11563916/www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2019/dl/all0112.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202401013A-sonota2_0.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www-pref-kochi-lg-jp.cache.yimg.jp/doc/2026010900176/file_contents/file_20263183141516_1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2024/dl/tyousanogaiyou.pdf` -> **snapshot** (snapshot 20260320011855); points raw/verified 0/0
- `https://warp.da.ndl.go.jp/info:ndljp/pid/3487545/www.city.hirosaki.aomori.jp/gaiyo/tokei/jinko/dotai/h20dotai.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2016/dl/all2812.pdf` -> **snapshot** (snapshot 20260324172851); points raw/verified 15/11
  - p198 Japan monthly live births, July 2015 (preliminary, Japanese residents) = **88,857** as written "88 857", value check pending births (2015-07-01..2015-07-31) [keep: ] quote: "7月 88 857 99 280 157 77 △10 423 984 926 305 58 685 19 015"
  - p199 Japan monthly live births, July 2016 (preliminary, Japanese residents) = **84,390** as written "84 390", value check pending births (2016-07-01..2016-07-31) [keep: ] quote: "7月 84 390 98 862 154 69 △14 472 772 856 294 60 201 17 036"
  - p200 Japan annual live births, 2015 (confirmed, Japanese residents) = **1,005,677** as written "1 005 677", value check pending births (2015-01-01..2015-12-31) [keep: ] quote: "27 1 005 677 1 290 444 1 916 902 △ 284 767 10 862 11 755 3 728 635 156 226 215"
  - p201 Japan annual live births, 2016 (preliminary, Japanese residents) = **976,979** as written "976 979", value check pending births (2016-01-01..2016-12-31) [keep: ] quote: "28* 976 979 1 307 765 1 928 874 △ 330 786 10 076 10 862 3 522 620 523 216 805"
  - p202 Japan annual live births, 2014 (Japanese residents) = **1,003,539** as written "1 003 539", value check pending births (2014-01-01..2014-12-31) [keep: ] quote: "26 1 003 539 1 273 004 2 080 952 △ 269 465 10 905 12 619 3 750 643 749 222 107"
  - p203 Japan annual live births, 2013 (Japanese residents) = **1,029,816** as written "1 029 816", value check pending births (2013-01-01..2013-12-31) [keep: ] quote: "25 1 029 816 1 268 436 2 185 1 026 △ 238 620 10 938 13 164 3 862 660 613 231 383"
  - p204 Japan annual live births, 2012 (Japanese residents) = **1,037,231** as written "1 037 231", value check pending births (2012-01-01..2012-12-31) [keep: ] quote: "24 1 037 231 1 256 359 2 299 1 065 △ 219 128 11 448 13 352 4 133 668 869 235 406"
  - p205 Japan annual live births, 2011 (Japanese residents) = **1,050,806** as written "1 050 806", value check pending births (2011-01-01..2011-12-31) [keep: ] quote: "23 1 050 806 1 253 066 2 463 1 147 △ 202 260 11 940 13 811 4 315 661 895 235 719"
  - p206 Japan annual live births, 2010 (Japanese residents) = **1,071,304** as written "1 071 304", value check pending births (2010-01-01..2010-12-31) [keep: ] quote: "22 1 071 304 1 197 012 2 450 1 167 △ 125 708 12 245 14 315 4 515 700 214 251 378"
  - p207 Japan annual live births, 2008 (Japanese residents) = **1,091,156** as written "1 091 156", value check pending births (2008-01-01..2008-12-31) [keep: ] quote: "20 1 091 156 1 142 407 2 798 1 331 △ 51 251 12 625 15 552 4 720 726 106 251 136"
  - p208 Japan annual live births, 2007 (Japanese residents) = **1,089,818** as written "1 089 818", value check pending births (2007-01-01..2007-12-31) [keep: ] quote: "19 1 089 818 1 108 334 2 828 1 434 △ 18 516 13 107 16 206 4 906 719 822 254 832"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2019/dl/all0108.pdf` -> **snapshot** (snapshot 20260324174007); points raw/verified 14/14
  - p209 Japan monthly live births, August 2019 (preliminary monthly vital statistics, Ja = **75,732** as written "75 732", value check pending births (2019-08-01..2019-08-31) [keep: ] quote: "8月 75 732 110 475 120 54 △34 743 793 808 274 41 658 15 963"
  - p210 Japan monthly live births, July 2019 (preliminary monthly vital statistics, Japa = **76,239** as written "76 239", value check pending births (2019-07-01..2019-07-31) [keep: ] quote: "7月 76 239 105 655 152 77 △29 416 803 893 261 42 463 17 810"
  - p211 Japan monthly live births, July 2018 (preliminary monthly vital statistics, Japa = **80,024** as written "80 024", value check pending births (2018-07-01..2018-07-31) [keep: ] quote: "7月 80 024 106 271 140 61 △26 247 743 811 261 50 412 16 963"
  - p212 Japan monthly live births, August 2018 (preliminary monthly vital statistics, Ja = **80,710** as written "80 710", value check pending births (2018-08-01..2018-08-31) [keep: ] quote: "8月 80 710 106 193 138 67 △25 483 826 874 283 45 329 17 083"
  - p213 Japan cumulative live births January-August 2019 (preliminary monthly vital stat = **571,087** as written "571 087", value check pending births (2019-01-01..2019-08-31) [keep: ] quote: "571 087 608 652 △ 37 565 △ 6.2 6.9 7.3"
  - p214 Japan cumulative live births January-August 2018 (preliminary monthly vital stat = **608,652** as written "608 652", value check pending births (2018-01-01..2018-08-31) [keep: ] quote: "571 087 608 652 △ 37 565 △ 6.2 6.9 7.3"
  - p215 Japan live births, July 2019, year-on-year change rate = **-4,978** as written "△ 4 978", value check pending births (2019-07-01..2019-07-31) [keep: ] quote: "75 732 80 710 △ 4 978 △ 6.2 7.2 7.6"
  - p216 Japan live births, August 2019, year-on-year change rate (%) = **6.2** % (2019-08-01..2019-08-31) [keep: ] quote: "75 732 80 710 △ 4 978 △ 6.2 7.2 7.6"
  - p217 Japan births rate per 1,000 population, August 2019 (annualised monthly rate) = **7.2** births per 1,000 population (2019-08-01..2019-08-31) [keep: ] quote: "7.2 10.5 1.6 0.7 △ 3.3 10.3 10.4 3.6 4.0 1.52 8月"
  - p218 Japan births rate per 1,000 population, July 2019 (annualised monthly rate) = **7.2** births per 1,000 population (2019-07-01..2019-07-31) [keep: ] quote: "7.2 10.0 2.0 1.0 △ 2.8 10.3 11.5 3.4 4.0 1.69 7月"
  - p219 Japan births rate per 1,000 population, July 2018 (annualised monthly rate) = **7.6** births per 1,000 population (2018-07-01..2018-07-31) [keep: ] quote: "7.6 10.1 1.8 0.8 △ 2.5 9.1 9.9 3.3 4.8 1.61 7月"
  - p220 Japan births rate per 1,000 population, August 2018 (annualised monthly rate) = **7.6** births per 1,000 population (2018-08-01..2018-08-31) [keep: ] quote: "7.6 10.1 1.7 0.8 △ 2.4 10.0 10.6 3.5 4.3 1.62 8月"
  - p221 Japan total population (Japanese), August 1 2019 provisional (denominator for ra = **123,882,000** as written "123 882 000", value check pending person (2019-08-01..2019-08-01) [keep: ] quote: "8月 * 123 882 000 * 60 269 000 * 63 613 000"
  - p222 Japan total population (Japanese), July 1 2019 (denominator for rates) = **123,881,000** as written "123 881 000", value check pending person (2019-07-01..2019-07-01) [keep: ] quote: "7月 123 881 000 60 270 000 63 611 000"
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=448084&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period year 2009 does not appear in the page text or URL (likely mis-dated): 1; period year 2006 does not appear in the page text or URL (likely mis-dated): 1; period year 2005 does not appear in the page text or URL (likely mis-dated): 1; period year 2004 does not appear in the page text or URL (likely mis-dated): 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan births', 'july 2026 births', 'vital statistics']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p31', 'p32', 'p133', 'p134', 'p135', 'p136'] Same May 2026 preliminary release: May 2026 births 59,663 vs May 2025 60,718, a 1.7% decline. These are duplicate renderings of one measurement, not independent confirmations.
- corroborating: ['p5', 'p6', 'p7', 'p33', 'p34', 'p45', 'p140', 'p141'] Same release: Jan-May 2026 cumulative 282,222 vs 280,979 in 2025, +0.4%. Duplicates of one figure.
- corroborating: ['p8', 'p9', 'p10', 'p35', 'p36', 'p144', 'p145'] Trailing 12 months Jun2025-May2026 = 707,052 vs 709,893 prior year, -0.4%. Same underlying release.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p122', 'p123'] July 2025 births 60,650 vs July 2024 62,306, -2.7%. Two vintages of the same July figures agree exactly, so the July 2025 level is well established.
- corroborating: ['p20', 'p21'] Jan-Jul 2025 cumulative 379,729 vs 392,304 in 2024, -3.2%; consistent with the monthly July figures and the Jan-May cumulative.
- corroborating: ['p58', 'p59', 'p60', 'p61', 'p62', 'p63'] Jan 2026 58,694 (+0.5%), Feb 2026 50,761 (-0.4%), Jan-Feb cumulative 109,455 (+0.1%). Consistent with the Jan-May cumulative being roughly flat versus 2025.
- corroborating: ['p1', 'p5', 'p58', 'p59'] Monthly 2026 values (Jan 58,694, Feb 50,761, May 59,663) are consistent with the Jan-May cumulative 282,222; the 2026 year is running close to 2025 levels, unlike the steep 2024-25 declines.
- corroborating: ['p48', 'p49', 'p50', 'p65', 'p66'] Japanese-national births 2025 = 671,236 (-2.2%); all-person 2025 preliminary = 705,809. The gap (~34,600) is the foreign-national contribution, consistent with the all-person scope of the target.
- corroborating: ['p46', 'p47', 'p55', 'p56', 'p57', 'p67', 'p68'] TFR 2025 = 1.14 vs 2024 = 1.15, well below IPSS medium (1.25) and near low variant (1.10); consistent with continued but slowing decline.
- corroborating: ['p70', 'p71', 'p72', 'p73', 'p74', 'p75'] 2025 births fell less in major cities (-0.7%) than elsewhere (-2.8%); urban/rural divergence, not a contradiction.
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p106', 'p107', 'p108', 'p109'] Pregnancy-notification data and conception-to-birth lag (~38 weeks) are internally consistent; but they are 2020-21 vintage and cannot be transferred to Oct 2025 conceptions without a large, unsupport
- corroborating: ['p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p148', 'p149', 'p152', 'p153', 'p156', 'p157'] March 2025 and Q1 2025 figures show the steep 2024-25 decline phase; consistent with the July 2025 -2.7% and Jan-Jul -3.2%.
- conflicting: ['p163', 'p164', 'p165', 'p166', 'p168', 'p169', 'p170', 'p171', 'p178', 'p184', 'p185'] These 2025 mid-year reports (Jan-Jun 2025 ~339,280 or 319,079 excluding foreigners; full-year 2025 ~686,000) are inconsistent with the later official preliminary figures (Jan-May 2026 cumulative 282,2
- corroborating: ['p118', 'p119', 'p120', 'p121', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132'] Oct 2025 59,979 vs Oct 2024 60,213 (-0.4%); Jan-Oct 2025 556,091 vs 571,274 (-2.7%). Consistent with the slowing decline in late 2025.
- corroborating: ['p137', 'p138', 'p139', 'p142', 'p143', 'p146', 'p147', 'p150', 'p151', 'p154', 'p155', 'p158', 'p159', 'p167', 'p172', 'p173', 'p182', 'p183'] Marriage counts: May 2026 41,169 (-4.8%), Jan-May 2026 206,971 (+0.4%), trailing 12m 506,485 (+3.2%). Mixed but broadly stable; marriages are a weak, lagged predictor of births and not directly usable
- corroborating: ['p11', 'p12', 'p37', 'p38'] Prefecture-table national totals equal the headline totals (59,663 May; 282,222 Jan-May), confirming internal consistency of the release.
- corroborating: ['p13', 'p14', 'p15', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p100', 'p101', 'p126', 'p127', 'p128', 'p160'] Annualized birth rates (5.7-5.8 per 1,000) are consistent with the monthly counts and population; useful only as a cross-check, not a separate route.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p31', 'p32', 'p133', 'p134', 'p135', 'p136'] All are the same May 2026/May 2025 preliminary vital-statistics figures (59,663 vs 60,718, -1,055, -1.7%) repeated across tables and directions. They are one measurement, not independent confirmation.
- corroborating: ['p5', 'p6', 'p7', 'p33', 'p34', 'p38', 'p45', 'p140', 'p141'] Same Jan-May cumulative pair (282,222 vs 280,979, +0.4%). One measurement repeated. This is the key evidence that 2026 has flattened relative to 2025's steep decline.
- corroborating: ['p8', 'p9', 'p10', 'p35', 'p36', 'p43', 'p44', 'p144', 'p145'] Same trailing-12-month pair (707,052 vs 709,893, -0.4%). One measurement repeated; shows the annual decline rate has shrunk to near zero.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p122', 'p123'] July 2025 = 60,650 and July 2024 = 62,306 appear in both the preliminary monthly report and the later monthly table; identical values, same underlying source. July 2025 YoY was -2.7%.
- corroborating: ['p20', 'p21'] Jan-Jul cumulative 2025 (379,729) vs 2024 (392,304), -3.2%. Consistent with the monthly July figures and with the Jan-May and trailing-12-month declines; same source family.
- corroborating: ['p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p91', 'p92', 'p93', 'p94', 'p148', 'p149', 'p152', 'p153'] 2024/2025 monthly and cumulative values from the monthly table; internally consistent with the preliminary series (e.g. March 2025 53,619, Jan-Mar 162,955). Same source, overlapping coverage.
- corroborating: ['p118', 'p119', 'p120', 'p121', 'p124', 'p125', 'p129'] Oct 2025 (59,979 vs 60,213, -0.4%), Aug/Sep 2025, and Jan-Oct cumulative (-2.7%). Same source; shows the decline rate easing through late 2025.
- corroborating: ['p58', 'p59', 'p60', 'p61', 'p62', 'p63'] Jan 2026 +0.5%, Feb 2026 -0.4%, Jan-Feb +0.1%. Consistent with the Jan-May +0.4% cumulative from MHLW; a secondary press report of the same preliminary statistics, so not independent of p5.
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p65', 'p66', 'p67', 'p68'] 2025 annual picture: TFR 1.14 (down from 1.15), Japanese-national births 671,236 (-2.2%), all-person 2025 preliminary 705,809, marriages up 0.8%. Consistent with the monthly series showing a ~2-3% ann
- corroborating: ['p70', 'p71', 'p72', 'p73', 'p74', 'p75'] 2025 geographic pattern: major cities -0.7% (Tokyo 23 wards +1.4%), rest of country -2.8%. Explains why national decline is milder than rural decline; useful context but not a direct July 2026 level.
- corroborating: ['p187', 'p188', 'p189', 'p190', 'p191', 'p192', 'p193', 'p194', 'p195', 'p196', 'p197'] Tokyo births series (Japanese residents only) and national 2024 = 686,173 as cited. Different population definition (Japanese residents, excludes foreign nationals) and different vintage from the all-
- corroborating: ['p198', 'p199', 'p200', 'p201', 'p202', 'p203', 'p204', 'p205', 'p206', 'p207', 'p208', 'p209', 'p210', 'p211', 'p212', 'p213', 'p214', 'p215', 'p216', 'p217', 'p218', 'p219', 'p220', 'p221', 'p222'] Older (2010s) Japanese-resident monthly/annual series. Different population scope (excludes foreign nationals) and much older level; useful only for the July seasonal share, not for the 2026 level.
- corroborating: ['p137', 'p138', 'p139', 'p142', 'p143', 'p146', 'p147', 'p150', 'p151', 'p154', 'p155', 'p158', 'p159', 'p161', 'p162'] Marriage series: May 2026 -4.8%, Jan-May +0.4%, trailing-12m +3.2%. Marriages lead births by roughly 1-2 years, so 2025's marriage rise is a mild positive for 2026-27 births; weak, indirect signal.
- corroborating: ['p13', 'p14', 'p15', 'p39', 'p40', 'p41', 'p42', 'p100', 'p101', 'p126', 'p127', 'p128', 'p160'] Annualised birth rates (5.7 vs 5.8 in May; 5.6 vs 5.5 cumulative; 6.0 July 2025). Consistent with the count series; redundant for level estimation since counts are directly available.
- conflicting: ['p55', 'p56'] IPSS medium-variant 2025 TFR projection of 1.25 vs actual 1.14 (p46) and low-variant 1.10. The official projection overstates fertility; do not use IPSS medium as a level anchor.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 vs July 2025 year-on-year change factor (all-person births) | 0.995 | 0.96..1.03 | 0.8894..1.112 (widened) | dimensionless | m1 (m1) | 2026 has flattened: Jan-May cumulative +0.4% (p5/p6), trailing-12m -0.4% (p8/p9), May -1.7% (p1/p2), Jan-Feb +0.1% (p60/p61). July 2025 itself was -2.7% (p19). A near-flat factor with a wide band centred slightly below 1 reflects the recent easing of decline and the risk of a renewed dip. | The recent flattening in the Jan-May and trailing-12m cumulative series persists into July 2026. | A June 2026 preliminary figure showing a renewed decline of 2%+ year-on-year. |
| a2 | July share of annual all-person births | 0.086 | 0.08..0.092 | 0.06066..0.1213 (widened) | dimensionless | m2 (m2) | July is a high-birth month. From the monthly table, July 2025 60,650 against a 2025 annual all-person total of ~705,809 (p65) gives ~8.6%; July 2024 62,306 against ~686,000 gives ~9.1%. The share is stable, so a band around 8.6% is justified. | The 2026 annual total is close to 2025's and the July seasonal share is stable. | A 2026 annual total far from 2025's, or evidence of a shifted seasonal pattern. |
| a3 | 2026 annual all-person births as a factor of 2025 | 0.99 | 0.95..1.02 | 0.6961..1.392 (widened) | dimensionless | m2 (m2) | 2025 all-person births were 705,809 (p65). The 2026 year-to-date series is roughly flat (Jan-May +0.4%, trailing-12m -0.4%), so a near-flat annual factor is appropriate, with a band allowing a modest renewed decline. | The 2026 annual total tracks the flat year-to-date trend. | A sharp acceleration of decline in mid-2026 monthly data. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 60,303 | ['p16'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 59,501 | ['p65'] / ['a2', 'a3'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p16 * a1; Monte Carlo P10 to P90 48,725 to 74,883; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p65 * a3 * a2; Monte Carlo P10 to P90 35,285 to 99,770; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.68 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 60,303 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 59,501 (width x/÷1.68, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.54; Birge ratio 0.03 (not above one, so no widening); final width x/÷1.54.

Result: central **59,901** person, 80% interval [38,899, 92,240] person, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

Unit of the estimate: person (births; total for 2026-07-01 to 2026-07-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in Japan during July 2026, as counted in the MHLW preliminary monthly vital statistics (including foreign nationals), is 59,901 person (80% model-based interval 38,899 to 92,240 person).

Two routes were combined with equal weight per block. m1 (60,303 person, weight 50%) scales the observed July 2025 preliminary figure of 60,650 births by an assumed near-flat year-on-year factor of 0.995 (range 0.8894 to 1.112). m2 (59,501 person, weight 50%) multiplies the observed 2025 all-person annual total of 705,809 births by an assumed 2026 annual factor of 0.99 and an assumed July share of 0.086. The observed points are historical; the factors and share are analyst assumptions, not observations.

The main risk is a renewed steep decline in mid-2026, which would push the true value below both routes. The most useful missing evidence would be actual July 2026 monthly counts or a longer, stable monthly series to pin down the July share and the year-on-year factor.

Unit of the estimate: person (births; total for 2026-07-01 to 2026-07-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 vs July 2025 year-on-year change factor (all-person births): 0.995 dimensionless, range 0.8894 to 1.112 (range widened by code); used by m1. Overturned by: A June 2026 preliminary figure showing a renewed decline of [n]+ year-on-year.
- a2 July share of annual all-person births: 0.086 dimensionless, range 0.06066 to 0.1213 (range widened by code); used by m2. Overturned by: A 2026 annual total far from 2025's, or evidence of a shifted seasonal pattern.
- a3 2026 annual all-person births as a factor of 2025: 0.99 dimensionless, range 0.6961 to 1.392 (range widened by code); used by m2. Overturned by: A sharp acceleration of decline in mid-2026 monthly data.

Method details (computed by code):
- m1 formula_mc: p16 * a1; Monte Carlo P10 to P90 48,725 to 74,883; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p65 * a3 * a2; Monte Carlo P10 to P90 35,285 to 99,770; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.68 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 60,303 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 59,501 (width x/÷1.68, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.54; Birge ratio 0.03 (not above one, so no widening); final width x/÷1.54.

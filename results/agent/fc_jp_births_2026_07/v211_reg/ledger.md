# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births occurring in Japan during July 2026, as counted in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (人口動態統計速報), which includes foreign nationals resident in Japan | unit births | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (厚生労働省), preliminary monthly vital statistics (人口動態統計速報)

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW preliminary monthly vital statistics time series

Hypothesis: July 2026 births will follow the level and seasonal pattern of July preliminary counts in recent years, adjusted for the ongoing downward trend; the same-month prior-year values and the most recent 2025-2026 monthly preliminary values anchor the level.

Queries issued by the searcher: 人口動態統計速報 月別 出生数 2025 2026 厚生労働省; Japan monthly vital statistics preliminary births July 2025 人口動態統計速報; 2024年7月 人口動態統計速報 出生数 前年同月比 7月 65231; 人口動態統計速報 出生数 月別推移 2019 2020 2021 2022 2023 2024 7月 一覧

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p1 Japan monthly preliminary births (速報), May 2026 = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p2 Japan monthly preliminary births (速報), May 2025 = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p3 Japan May 2026 births year-on-year change (difference) = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p4 Japan May 2026 births year-on-year change rate = **1.7** % (2026-05-01..2026-05-31) [DISCARD: Derived rate from p1/p2; redundant with the levels.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p5 Japan May 2026 births year-on-year ratio (対前年比) = **98.7** ratio (previous year = 100) (2026-05-01..2026-05-31) [DISCARD: Derived ratio from p1/p2; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p6 Japan cumulative preliminary births (速報), Jan-May 2026 = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p7 Japan cumulative preliminary births (速報), Jan-May 2025 = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p8 Japan Jan-May 2026 cumulative births year-on-year change rate = **0.4** % (2026-01-01..2026-05-31) [DISCARD: Derived rate from p6/p7; redundant.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p9 Japan Jan-May 2026 cumulative births year-on-year ratio (対前年比) = **101** ratio (previous year = 100) (2026-01-01..2026-05-31) [DISCARD: Derived ratio from p6/p7; redundant.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p10 Japan preliminary births (速報), trailing 12 months Jun 2025-May 2026 = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p11 Japan preliminary births (速報), trailing 12 months Jun 2024-May 2025 = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p12 Japan trailing 12 months births year-on-year change rate (Jun 2025-May 2026) = **0.4** % (2025-06-01..2026-05-31) [DISCARD: Derived rate from p10/p11; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p13 Japan trailing 12 months births year-on-year ratio (対前年比, Jun 2025-May 2026) = **100** ratio (previous year = 100) (2025-06-01..2026-05-31) [DISCARD: Derived ratio from p10/p11; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p14 Japan national preliminary births (速報), May 2026, prefecture table total = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p15 Japan national cumulative preliminary births (速報), Jan-May 2026, prefecture tabl = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.wic-net.com/report/4766/8.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Annual and year-to-date birth totals

Hypothesis: Annual births (確定値 or 概数) and year-to-date cumulative preliminary births can be decomposed into monthly shares; July's share of the annual total is stable, so annual or YTD totals times a July share give the target.

Queries issued by the searcher: 人口動態統計 2025年 出生数 速報 年間; 2026年 上半期 出生数 速報 累計 厚生労働省; 人口動態統計速報 2026年7月 出生数 厚生労働省; 人口動態統計 月別 出生数 2025年 7月 8月 各月 推移

- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/japan-data/h02802/` -> **snapshot** (snapshot 20260704025756); points raw/verified 15/15
  - p16 Japan annual births, 2025 (概数, preliminary) = **671,236** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に生まれた赤ちゃんの数(出生数)は、前年より1万4937人少ない67万1236人となり"
  - p17 Japan annual births, 2024 (確定値, confirmed) = **686,173** births (2024-01-01..2024-12-31) [keep: ] quote: "\| 出生数 \| 67万1236人 \| 68万6173人 \|"
  - p18 Year-on-year decline in Japan births, 2025 vs 2024 = **14,937** births (2025-01-01..2025-12-31) [keep: ] quote: "前年より1万4937人少ない67万1236人となり"
  - p19 Japan total fertility rate, 2025 (概数) = **1.14** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "合計特殊出生率(1人の女性が生涯に産む子どもの数)は前年比0.01ポイント減の1.14で過去最低を更新した。"
  - p20 Japan total fertility rate, 2024 (確定) = **1.15** children per woman (2024-01-01..2024-12-31) [keep: ] quote: "\| 合計特殊出生率 \| 1.14 \| 1.15 \|"
  - p21 Japan deaths, 2025 (概数) = **1,589,489** deaths (2025-01-01..2025-12-31) [keep: ] quote: "\| 死亡数 \| 158万9489人 \| 160万5378人 \|"
  - p22 Japan deaths, 2024 (確定) = **1,605,378** deaths (2024-01-01..2024-12-31) [keep: ] quote: "\| 死亡数 \| 158万9489人 \| 160万5378人 \|"
  - p23 Japan natural decrease (births minus deaths), 2025 (概数) = **918,253** persons (2025-01-01..2025-12-31) [DISCARD: Natural decrease; not needed for a birth-level estimate.] quote: "\| 自然増減 \| ▲91万8253人 \| ▲91万9205人 \|"
  - p24 Japan natural decrease (births minus deaths), 2024 (確定) = **919,205** persons (2024-01-01..2024-12-31) [DISCARD: Natural decrease; not needed.] quote: "\| 自然増減 \| ▲91万8253人 \| ▲91万9205人 \|"
  - p25 Japan marriages, 2025 (概数) = **489,119** couples (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数は前年よりも4027組増の48万9119組と2年連続の微増となったが、底ばいが続いている。"
  - p26 Japan marriages, 2024 (確定) = **485,092** couples (2024-01-01..2024-12-31) [keep: ] quote: "\| 婚姻数 \| 48万9119組 \| 48万5092組 \|"
  - p27 Japan divorces, 2025 (概数) = **179,068** divorces (2025-01-01..2025-12-31) [keep: ] quote: "\| 離婚数 \| 17万9068件 \| 18万5904件 \|"
  - p28 Japan divorces, 2024 (確定) = **185,904** divorces (2024-01-01..2024-12-31) [keep: ] quote: "\| 離婚数 \| 17万9068件 \| 18万5904件 \|"
  - p29 Tokyo total fertility rate, 2025 (below 1 for third consecutive year) = **0.96** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "東京は3年連続で「1」を割り込み0.96。"
  - p30 Okinawa total fertility rate, 2025 (highest prefecture) = **1.52** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "最も高かったのは沖縄1.52で、宮崎1.46、福井1.45、長崎1.42、島根1.41、香川と熊本の1.40が続いた。"
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nikkei.com/article/DGXZQOUA0197C0R00C26A6000000/?utm_source=newsshowcase&utm_medium=gnews&utm_campaign=CDAQvIb1ia2T3-FWGKzipr_l2-2NngEqKgg` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Japanese-national-only vs all-resident counts

Hypothesis: The preliminary series includes foreign residents; the foreign-national share of births is small but non-zero and may be growing, so a Japanese-national-only series (e.g., 人口動態統計 on Japanese nationals, or 国籍別 counts) plus a foreign-resident birth allowance bridges to the target.

Queries issued by the searcher: 人口動態統計 外国人 出生数 国籍別 2024; 日本 外国人 出生数 割合 人口動態統計 2023; 人口動態統計速報 令和8年 2026年 出生数 月別 厚生労働省; 2025年 出生数 外国人 割合 速報 日本人 減少

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/gaikoku26/dl/gaikyo_r08.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&toukei=00450013&stat_infid=000040484208` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/pdf/202601.pdf` -> **snapshot** (snapshot 20260306120943); points raw/verified 15/15
  - p31 Live births to foreign population in Japan, annual 2024 (final estimates) = **21,900** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 3,506,158 347,675 110.08 21,900 8,871 13,029 3,231,871 2,889,687 342,184 -7,538"
  - p32 Live births to foreign population in Japan, annual 2023 (final estimates) = **18,799** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 3,158,483 242,217 83.06 18,799 8,836 9,963 2,336,993 2,096,788 240,205 -7,951"
  - p33 Live births to foreign population in Japan, annual 2022 (final estimates) = **17,397** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 2,916,266 194,463 71.45 17,397 8,667 8,730 1,008,689 818,024 190,665 -4,932"
  - p34 Live births to foreign population in Japan, July 2025 (final estimates) = **1,874** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 3,747,640 -62,472 -16.67 1,874 706 1,168 276,416 338,912 -62,496 -1,144"
  - p35 Live births to foreign population in Japan, July 2024 (final estimates) = **1,979** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 3,418,173 -48,656 -14.23 1,979 714 1,265 227,845 276,693 -48,848 -1,073"
  - p36 Live births to foreign population in Japan, December 2024 (final estimates) = **2,284** births (2024-12-01..2024-12-31) [keep: ] quote: "12月 Dec. 3,589,470 -187,216 -52.16 2,284 890 1,394 204,545 392,248 -187,703 -907"
  - p37 Live births to foreign population in Japan, October 2024 (final estimates) = **2,210** births (2024-10-01..2024-10-31) [keep: ] quote: "10月 Oct. 3,506,158 50,602 14.43 2,210 742 1,468 263,505 213,526 49,979 -845"
  - p38 Live births to foreign population in Japan, September 2024 (final estimates) = **2,087** births (2024-09-01..2024-09-30) [keep: ] quote: "9月 Sept. 3,406,609 99,549 29.22 2,087 702 1,385 335,609 237,492 98,117 47"
  - p39 Live births to foreign population in Japan, August 2024 (final estimates) = **2,067** births (2024-08-01..2024-08-31) [keep: ] quote: "8月 Aug. 3,369,517 37,092 11.01 2,067 708 1,359 372,150 335,474 36,676 -943"
  - p40 Live births to foreign population in Japan, July 2023 (final estimates) = **1,771** births (2023-07-01..2023-07-31) [keep: ] quote: "8月 Aug. 3,029,205 48,358 15.96 1,771 764 1,007 332,875 284,721 48,154 -803"
  - p41 Total live births in Japan, annual 2024 (final estimates, all residents) = **717,291** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 123,801,750 -550,127 -4.42 717,291 1,607,261 -889,970 4,192,568 3,852,725 339,843"
  - p42 Total live births in Japan, annual 2023 (final estimates, all residents) = **757,939** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 124,351,877 -594,912 -4.76 757,939 1,594,982 -837,043 3,250,231 3,008,100 242,131"
  - p43 Total live births in Japan, July 2025 (final estimates, all residents) = **62,521** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 123,366,734 -98,784 -0.80 62,521 118,980 -56,459 394,642 436,967 -42,325"
  - p44 Total live births in Japan, July 2024 (final estimates, all residents) = **64,283** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 123,975,371 -87,882 -0.71 64,283 127,085 -62,802 350,001 375,081 -25,080"
  - p45 Live births to Japanese population in Japan, July 2025 (final estimates) = **60,647** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 119,619,094 -36,312 -0.30 60,647 118,274 -57,627 118,226 98,055 20,171 1,144"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Official and research forecasts of 2026 births

Hypothesis: IPSS (国立社会保障・人口問題研究所) and other published projections or nowcasts of 2026 annual births, combined with a July monthly share, constrain the plausible range; forecast revisions reflect recent trends.

Queries issued by the searcher: 国立社会保障・人口問題研究所 2026年 出生数 見通し; Japan 2026 births forecast projection IPSS; 人口動態統計速報 2026年 出生数 月別 外国人含む; Japan births first half 2026 rose 11 years monthly vital statistics preliminary

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 0/0
- `https://www.pacola.co.jp/n2026061408/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ipss.go.jp/pp-zenkoku/e/zenkoku_e2023/pp2023e_Summary.pdf` -> **snapshot** (snapshot 20260621125821) **LEAK SENTINEL HIT ['(?<![\\d.,])62,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.47news.jp/13919142.html` -> **snapshot** (snapshot 20260226204005); points raw/verified 8/5
  - p46 Japan births including foreign nationals, 2025 preliminary vital statistics (ann = **705,809** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に生まれた外国人を含む子どもの数は70万5809人となり、統計を始めた1899年以降で最少を更新した。"
  - p47 Year-on-year change in Japan births including foreign nationals, 2025 (percent) = **2.1** % (2025-01-01..2025-12-31) [keep: ] quote: "前年から2.1%(1万5179人)減った。"
  - p48 Year-on-year decrease in Japan births including foreign nationals, 2025 (persons = **15,179** births (2025-01-01..2025-12-31) [keep: ] quote: "前年から2.1%(1万5179人)減った。"
  - p49 Japan natural population decrease (deaths minus births), 2025 = **899,845** people (2025-01-01..2025-12-31) [DISCARD: Natural decrease; not needed.] quote: "死亡数から出生数を差し引いた人口の「自然減」は89万9845人で過去最大となり、人口減少にも歯止めがかからない。"
  - p50 Years by which Japan's low fertility has advanced ahead of government assumption = **17** years (not stated (page dated 2026-02-26)) [DISCARD: Contextual claim about fertility lag; not a numeric input.] quote: "少子化は政府想定より17年早く進んでいる。"
- dropped by code checks: 3 (period_end 2042-12-31 after as_of: 1; number: scale conflict: '千' in value vs '万': 2)

### d5 [related_series] Conception and pregnancy-related leading indicators

Hypothesis: Births in July 2026 reflect conceptions around October 2025; marriage registrations, pregnancy reports (妊娠届出数) and maternal health records lagged ~9 months can signal the level of births, with the caveat that conception-to-birth timing varies.

Queries issued by the searcher: 妊娠届出数 月別 2025 厚生労働省; 婚姻件数 月別 2025 人口動態統計速報; 人口動態統計速報 令和8年6月分 2026 出生数; 妊娠届出数 全国 月別 2026 厚生労働省 母子保健 集計

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 15/15
  - p51 National marriage registrations (婚姻件数), March 2025 (令和7年3月), preliminary vital s = **55,762** as written "55 762", value check pending marriages (2025-03-01..2025-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p52 National marriage registrations (婚姻件数), March 2024 (令和6年3月), preliminary = **56,864** as written "56 864", value check pending marriages (2024-03-01..2024-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p53 National marriage registrations (婚姻件数), cumulative Jan-Mar 2025 (令和7年1月～3月) = **131,332** as written "131 332", value check pending marriages (2025-01-01..2025-03-31) [keep: ] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p54 National marriage registrations (婚姻件数), cumulative Jan-Mar 2024 (令和6年1月～3月) = **136,653** as written "136 653", value check pending marriages (2024-01-01..2024-03-31) [keep: ] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p55 National marriage registrations (婚姻件数), trailing 12 months Apr 2024-Mar 2025 (令和 = **494,678** as written "494 678", value check pending marriages (2024-04-01..2025-03-31) [keep: ] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p56 National marriage registrations (婚姻件数), trailing 12 months Apr 2023-Mar 2024 (令和 = **491,082** as written "491 082", value check pending marriages (2023-04-01..2024-03-31) [keep: ] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p57 National live births (出生), March 2025 (令和7年3月), preliminary vital statistics = **53,619** as written "53 619", value check pending births (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p58 National live births (出生), March 2024 (令和6年3月), preliminary = **55,198** as written "55 198", value check pending births (2024-03-01..2024-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p59 National live births (出生), cumulative Jan-Mar 2025 (令和7年1月～3月) = **162,955** as written "162 955", value check pending births (2025-01-01..2025-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p60 National live births (出生), cumulative Jan-Mar 2024 (令和6年1月～3月) = **170,804** as written "170 804", value check pending births (2024-01-01..2024-03-31) [keep: ] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p61 National live births (出生), trailing 12 months Apr 2024-Mar 2025 (令和6年4月～令和7年3月) = **713,139** as written "713 139", value check pending births (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p62 National live births (出生), trailing 12 months Apr 2023-Mar 2024 (令和5年4月～令和6年3月) = **746,958** as written "746 958", value check pending births (2023-04-01..2024-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p63 Year-on-year change rate in national live births, March 2025 vs March 2024 (増減率) = **2.9** percent (2025-03-01..2025-03-31) [keep: ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p64 Year-on-year change rate in national marriage registrations, March 2025 vs March = **1.9** percent (2025-03-01..2025-03-31) [keep: ] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p65 Year-on-year change rate in national live births, trailing 12 months Apr 2024-Ma = **4.5** percent (2024-04-01..2025-03-31) [keep: ] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hoikusys.jp/post/この半年の出生数は増加に転じたが` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [shocks] Calendar and policy effects on July births

Hypothesis: July birth counts are affected by the number of days, holiday timing, and any policy or health shocks (e.g., pandemic-era conception dips, heat, infectious disease); comparing July 2026 to July 2025 requires adjusting for these and for the ongoing secular decline.

Queries issued by the searcher: 人口動態統計速報 2026年 月別 出生数; 2025年7月 出生数 速報 人口動態統計; 人口動態統計速報 令和8年6月分 厚生労働省 2026年8月 公表; mhlw.go.jp 人口動態統計速報 s2026 07.html 令和8年7月分

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p66 Japan total live births (速報, all residents incl. foreign nationals), May 2026 = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p1.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p67 Japan total live births (速報), May 2025 = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [DISCARD: Duplicate of p2.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p68 Year-on-year change in Japan monthly births, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p3.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p69 Year-on-year percent change in Japan monthly births, May 2026 vs May 2025 = **1.7** % (2026-05-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p70 Japan cumulative live births (速報), Jan–May 2026 = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [DISCARD: Duplicate of p6.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p71 Japan cumulative live births (速報), Jan–May 2025 = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [DISCARD: Duplicate of p7.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p72 Year-on-year percent change in Japan cumulative births, Jan–May 2026 vs Jan–May  = **0.4** % (2026-01-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p73 Japan live births (速報), trailing 12 months Jun 2025–May 2026 = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [DISCARD: Duplicate of p10.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p74 Japan live births (速報), trailing 12 months Jun 2024–May 2025 = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [DISCARD: Duplicate of p11.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p75 Year-on-year percent change in Japan trailing-12-month births, Jun 2025–May 2026 = **0.4** % (2025-06-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p76 Japan annualised birth rate per 1,000 population, May 2026 = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [DISCARD: Derived birth rate; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p77 Japan annualised birth rate per 1,000 population, May 2025 = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [DISCARD: Derived birth rate; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p78 Japan annualised birth rate per 1,000 population, trailing 12 months Jun 2025–Ma = **5.7** births per 1,000 population (2025-06-01..2026-05-31) [DISCARD: Derived birth rate; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p79 Japan annualised birth rate per 1,000 population, trailing 12 months Jun 2024–Ma = **5.7** births per 1,000 population (2024-06-01..2025-05-31) [DISCARD: Derived birth rate; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p80 Japan total live births (速報), May 2026, national row of prefecture table = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p1/p14.] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20250&month=23070907&tclass1=0000010` -> **snapshot** (snapshot 20251112234917); points raw/verified 0/0
- `https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html` -> **snapshot** (snapshot 20260730150924); points raw/verified 15/7
  - p81 Marine Day (海の日) date in 2026 (Japan national holiday) = **20** as written "7月20日", value check pending day of July (2026-07-20..2026-07-20) [keep: ] quote: "\| 海の日 \| 7月20日 \| \|"
  - p82 Marine Day date in 2020 (Tokyo Olympics special measure, Japan) = **23** as written "7月23日", value check pending day of July (2020-07-23..2020-07-23) [DISCARD: 2020 special holiday date; irrelevant to 2026.] quote: "海の日 7月23日"
  - p83 Sports Day date in 2020 (Tokyo Olympics special measure, Japan) = **24** as written "7月24日", value check pending day of July (2020-07-24..2020-07-24) [DISCARD: 2020 special holiday date; irrelevant.] quote: "スポーツの日 7月24日"
  - p84 Marine Day date in 2021 (Tokyo Olympics special measure, Japan) = **22** as written "7月22日", value check pending day of July (2021-07-22..2021-07-22) [DISCARD: 2021 special holiday date; irrelevant.] quote: "海の日 7月22日"
  - p85 Sports Day date in 2021 (Tokyo Olympics special measure, Japan) = **23** as written "7月23日", value check pending day of July (2021-07-23..2021-07-23) [DISCARD: 2021 special holiday date; irrelevant.] quote: "スポーツの日 7月23日"
  - p86 Vernal Equinox Day date in 2026 (Japan national holiday) = **20** as written "3月20日", value check pending day of March (2026-03-20..2026-03-20) [DISCARD: Vernal Equinox; not in July.] quote: "\| 春分の日 \| 3月20日 \| \|"
  - p87 Substitute holiday date in 2026 following Constitution Memorial Day (Japan) = **6** as written "5月6日", value check pending day of May (2026-05-06..2026-05-06) [DISCARD: May substitute holiday; not in July.] quote: "\| 休日 \| 5月6日 \| 祝日法第3条第2項による休日 \|"
- dropped by code checks: 8 (period_end missing or unparseable: 2; period_end 2027-07-19 after as_of: 1; period_end 2026-09-23 after as_of: 1; period_end 2026-09-22 after as_of: 1; period_end 2027-09-23 after as_of: 1; period_end 2027-03-22 after as_of: 1; number: low/high given but value_as_written is not a range: 1)

### d7 [base_rates] Fertility rate and population base

Hypothesis: Births = women of childbearing age × age-specific fertility rates; using the mid-2026 female population aged 15-49 and recent TFR/ASFR gives an independent level check on the monthly count.

Queries issued by the searcher: 総務省 人口推計 2026年 年齢別 女性人口 15-49歳; 合計特殊出生率 2025年 日本 1.20 人口動態統計; 人口動態統計速報 2026年 月別 出生数 厚生労働省; 人口推計 2026年5月1日現在 年齢別 女性人口 30代 人数 総務省 確定値

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p88 Japan total live births, May 2026 (preliminary monthly vital statistics, all eve = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p1.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p89 Japan total live births, May 2025 (preliminary, prior year) = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [DISCARD: Duplicate of p2.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p90 Japan cumulative live births, January-May 2026 = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [DISCARD: Duplicate of p6.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p91 Japan cumulative live births, January-May 2025 = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [DISCARD: Duplicate of p7.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p92 Japan live births, trailing 12 months June 2025-May 2026 = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [DISCARD: Duplicate of p10.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p93 Japan live births, trailing 12 months June 2024-May 2025 = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [DISCARD: Duplicate of p11.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p94 Japan annualised birth rate (per 1,000 population), May 2026 = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p95 Japan annualised birth rate (per 1,000 population), May 2025 = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [DISCARD: Derived rate; redundant.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p96 Japan annualised birth rate (per 1,000 population), trailing 12 months June 2025 = **5.7** births per 1,000 population (2025-06-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p97 Japan annualised birth rate (per 1,000 population), cumulative January-May 2026 = **5.6** births per 1,000 population (2026-01-01..2026-05-31) [DISCARD: Derived rate; redundant.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p98 Japan annualised birth rate (per 1,000 population), cumulative January-May 2025 = **5.5** births per 1,000 population (2025-01-01..2025-05-31) [DISCARD: Derived rate; redundant.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p99 Japan total live births, May 2026, by prefecture of notification (national row) = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p1/p14.] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p100 Japan cumulative live births January-May 2026, by prefecture of notification (na = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [DISCARD: Duplicate of p6/p15.] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
  - p101 Tokyo Metropolis live births, May 2026 = **8,240** as written "8 240", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "13 東 京 8 240 10 540 166 7 227 1 540"
  - p102 Tokyo Metropolis cumulative live births January-May 2026 = **36,470** as written "36 470", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "13 東 京 36 470 58 325 846 34 840 8 585"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.projectdesign.jp/articles/news/622644f6-9462-48a6-976b-b8dd511ec5e3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/pdf/202605.pdf` -> **snapshot** (snapshot 20260612120154); points raw/verified 15/6
  - p103 Total live births, Japan, calendar year 2024 (final estimates) = **717,291** births (2024-01-01..2024-12-31) [DISCARD: Duplicate of p17/p126.] quote: "2024年 123,801,750 -550,127 -4.42 717,291 1,607,261 -889,970 4,192,568 3,852,725 339,843"
  - p104 Total live births, Japan, calendar year 2025 (final estimates) = **694,162** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年 123,219,024 -582,726 -4.71 694,162 1,613,143 -918,981 4,732,271 4,396,016 336,255"
  - p105 Live births, Japan, July 2024 (final estimates) = **64,283** births (2024-07-01..2024-07-31) [DISCARD: Duplicate of p44/p110/p123.] quote: "7月 July 123,975,371 -87,882 -0.71 64,283 127,085 -62,802 350,001 375,081 -25,080"
  - p106 Live births, Japan, July 2025 (final estimates) = **62,521** births (2025-07-01..2025-07-31) [DISCARD: Duplicate of p43.] quote: "7月 July 123,366,734 -98,784 -0.80 62,521 118,980 -56,459 394,642 436,967 -42,325"
  - p107 Live births, Japanese population, July 2025 (final estimates) = **60,647** births (2025-07-01..2025-07-31) [DISCARD: Duplicate of p45.] quote: "7月 July 119,619,094 -36,312 -0.30 60,647 118,274 -57,627 118,226 98,055 20,171 1,144"
  - p108 Live births, foreign population, July 2025 (final estimates) = **1,874** births (2025-07-01..2025-07-31) [DISCARD: Duplicate of p34.] quote: "7月 July 3,747,640 -62,472 -16.67 1,874 706 1,168 276,416 338,912 -62,496 -1,144"
- dropped by code checks: 9 (scale word 'thousand' not supported by quote or table header: 9)

### b1 [own_history] MHLW preliminary monthly vital statistics

Hypothesis: The June 2026 preliminary release (published ~late August 2026) would give June 2026 births and a Jan-Jun cumulative, letting us anchor July 2026 with a one-month-lag YoY ratio rather than a May-based ratio. This is the single most valuable missing input because it directly extends the target's own series to the month immediately before the target.

Queries issued by the searcher: mhlw.go.jp 人口動態統計速報 令和8年6月; 人口動態統計速報 2026年6月 出生数; 人口動態統計速報 令和7年7月分 出生数 前年同月; 2025年7月 出生数 速報 人口動態 6万 人 外国人含む

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Statistics Bureau monthly final estimates

Hypothesis: Monthly all-resident births for July 2022 and July 2023 (and the foreign-population July series) would give a longer July seasonal-share and foreign-share history, improving the July-share and foreign-allowance routes. Currently only July 2024/2025 are available.

Queries issued by the searcher: stat.go.jp 人口推計 2022年7月 出生数 外国人; stat.go.jp 人口推計 2023年7月 出生数; 人口推計 月別 出生児数 死亡者数 日本人 外国人 e-stat 2022年7月; 厚生労働省 人口動態統計速報 2026年7月 出生数

- `https://www.stat.go.jp/data/jinsui/pdf/202508.pdf` -> **snapshot** (snapshot 20251116161556); points raw/verified 15/13
  - p109 Japan total population live births, July 2023 (final estimates, all residents) = **65,620** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 124,516,650 -77,499 -0.62 65,620 120,120 -54,500 314,845 337,844 -22,999"
  - p110 Japan total population live births, July 2024 (final estimates, all residents) = **64,283** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 123,975,371 -87,882 -0.71 64,283 127,085 -62,802 350,001 375,081 -25,080"
  - p111 Japan Japanese population live births, July 2023 (final estimates) = **64,034** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 121,441,187 -31,241 -0.26 64,034 119,399 -55,365 119,814 96,383 23,431 693"
  - p112 Japan Japanese population live births, July 2024 (final estimates) = **62,304** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 120,557,198 -39,226 -0.33 62,304 126,371 -64,067 122,156 98,388 23,768 1,073"
  - p113 Japan foreign population live births, July 2023 (final estimates) = **1,586** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 3,075,463 -46,258 -15.04 1,586 721 865 195,031 241,461 -46,430 -693"
  - p114 Japan foreign population live births, July 2024 (final estimates) = **1,979** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 3,418,173 -48,656 -14.23 1,979 714 1,265 227,845 276,693 -48,848 -1,073"
  - p115 Japan total population live births, calendar year 2022 (final estimates, all res = **799,486** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 124,946,789 -555,501 -4.43 799,486 1,530,102 -730,616 1,595,872 1,420,757 175,115"
  - p116 Japan total population live births, calendar year 2023 (final estimates, all res = **757,939** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 124,351,877 -594,912 -4.76 757,939 1,594,982 -837,043 3,250,231 3,008,100 242,131"
  - p117 Japan Japanese population live births, calendar year 2022 (final estimates) = **782,089** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 122,030,523 -749,964 -6.11 782,089 1,521,435 -739,346 587,183 602,733 -15,550 4,932"
  - p118 Japan Japanese population live births, calendar year 2023 (final estimates) = **739,140** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 121,193,394 -837,129 -6.86 739,140 1,586,146 -847,006 913,238 911,312 1,926 7,951"
  - p119 Japan foreign population live births, calendar year 2022 (final estimates) = **17,397** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 2,916,266 194,463 71.45 17,397 8,667 8,730 1,008,689 818,024 190,665 -4,932"
  - p120 Japan foreign population live births, calendar year 2023 (final estimates) = **18,799** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 3,158,483 242,217 83.06 18,799 8,836 9,963 2,336,993 2,096,788 240,205 -7,951"
  - p121 Japan foreign population live births, calendar year 2024 (final estimates) = **21,900** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 3,506,158 347,675 110.08 21,900 8,871 13,029 3,231,871 2,889,687 342,184 -7,538"
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&bunya_l=02&stat_infid=000040400643` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/1.html` -> **snapshot** (snapshot 20260726231402); points raw/verified 0/0
- `https://www.stat.go.jp/data/jinsui/pdf/202504.pdf` -> **snapshot** (snapshot 20260106064452); points raw/verified 14/13
  - p122 Japan total population live births, July 2023 (final estimates, all residents) = **65,620** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 124,516,650 -77,499 -0.62 65,620 120,120 -54,500 314,845 337,844 -22,999"
  - p123 Japan total population live births, July 2024 (final estimates, all residents) = **64,283** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 123,975,371 -87,882 -0.71 64,283 127,085 -62,802 350,001 375,081 -25,080"
  - p124 Japan total population live births, calendar year 2022 (final estimates, all res = **799,486** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 124,946,789 -555,501 -4.43 799,486 1,530,102 -730,616 1,595,872 1,420,757 175,115"
  - p125 Japan total population live births, calendar year 2023 (final estimates, all res = **757,939** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 124,351,877 -594,912 -4.76 757,939 1,594,982 -837,043 3,250,231 3,008,100 242,131"
  - p126 Japan total population live births, calendar year 2024 (final estimates, all res = **717,291** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 123,801,750 -550,127 -4.42 717,291 1,607,261 -889,970 4,192,568 3,852,725 339,843"
  - p127 Foreign population live births, July 2023 (final estimates) = **1,586** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 3,075,463 -46,258 -15.04 1,586 721 865 195,031 241,461 -46,430 -693"
  - p128 Foreign population live births, July 2024 (final estimates) = **1,979** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 3,418,173 -48,656 -14.23 1,979 714 1,265 227,845 276,693 -48,848 -1,073"
  - p129 Foreign population live births, calendar year 2022 (final estimates) = **17,397** births (2022-01-01..2022-12-31) [keep: ] quote: "2022年 2,916,266 194,463 71.45 17,397 8,667 8,730 1,008,689 818,024 190,665 -4,932"
  - p130 Foreign population live births, calendar year 2023 (final estimates) = **18,799** births (2023-01-01..2023-12-31) [keep: ] quote: "2023年 3,158,483 242,217 83.06 18,799 8,836 9,963 2,336,993 2,096,788 240,205 -7,951"
  - p131 Foreign population live births, calendar year 2024 (final estimates) = **21,900** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 3,506,158 347,675 110.08 21,900 8,871 13,029 3,231,871 2,889,687 342,184 -7,538"
  - p132 Japanese population live births, July 2023 (final estimates) = **64,034** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 121,441,187 -31,241 -0.26 64,034 119,399 -55,365 119,814 96,383 23,431 693"
  - p133 Japanese population live births, July 2024 (final estimates) = **62,304** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 120,557,198 -39,226 -0.33 62,304 126,371 -64,067 122,156 98,388 23,768 1,073"
  - p134 Foreign population total, November 1, 2024 (final estimate) = **3,556,760** persons (2024-11-01..2024-11-01) [keep: ] quote: "11月 Nov. 3,556,760"
- dropped by code checks: 3 (number: scale conflict: '千' in value vs '万': 2; scale word 'thousand' not supported by quote or table header: 1)

### b3 [forecasts_markets] IPSS / research institute nowcasts

Hypothesis: A published 2026 annual birth projection (IPSS or private nowcast) combined with a July monthly share would provide an independent level check and constrain the plausible range, resolving disagreement between the May-anchored and July-share routes.

Queries issued by the searcher: 国立社会保障・人口問題研究所 2026年 出生数 推計; 2026年 出生数 予測 民間 日本; 2026年 出生数 予測 日本総研 藤波匠 2026年 70万人; 人口動態統計 月別 出生数 2025年7月 速報 前年同月比

- `https://www.dlri.co.jp/files/macro/617726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sankei.com./article/20260510-BY3MFI6NIJD23KXYH6EKTMQC5A/` -> **snapshot** (snapshot 20260511154028); points raw/verified 7/7
  - p135 Japan total births, January 2026, preliminary vital statistics, year-on-year cha = **0.5** as written "0・5%増", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p136 Japan total births, January 2026, preliminary vital statistics = **58,694** births (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p137 Japan total births, February 2026, preliminary vital statistics, year-on-year ch = **0.4** as written "0・4%減", value check pending % (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だった"
  - p138 Japan total births, February 2026, preliminary vital statistics = **50,761** births (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だった"
  - p139 Japan cumulative total births, January-February 2026, preliminary vital statisti = **0.1** as written "0・1%増", value check pending % (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p140 Japan cumulative total births, January-February 2026, preliminary vital statisti = **109,455** births (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p141 Japan total births, 1966 (previous 丙午 year), year-on-year decline = **25** % (1966-01-01..1966-12-31) [keep: ] quote: "60年前の1966年は出生数が前年比25%も減少した"
- `https://www.ipss.go.jp/pp-zenkoku/e/zenkoku_e2023/pp2023e_Summary.pdf` -> **snapshot** (snapshot 20260621125821) **LEAK SENTINEL HIT ['(?<![\\d.,])62,000(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://community.jmp.com/t5/blogs/blogarticleprintpage/blog-id/nmasukawa-blog/article-id/94` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan births', 'japan birth rate', 'japan population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p66', 'p67', 'p68', 'p69', 'p88', 'p89'] All are the same May 2026 vs May 2025 preliminary birth comparison from one MHLW release; p1/p66/p88 and p2/p67/p89 are duplicate copies of the same two numbers, and p3/p4/p5/p68/p69 are derived diffe
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p70', 'p71', 'p72', 'p90', 'p91'] Same Jan-May cumulative preliminary births and YoY change from the same MHLW release; duplicates of one measurement.
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p73', 'p74', 'p75', 'p92', 'p93'] Same trailing-12-month Jun2025-May2026 vs Jun2024-May2025 comparison; duplicates of one release.
- corroborating: ['p14', 'p15', 'p80', 'p99', 'p100'] Prefecture-table national rows reproduce the headline May 2026 and Jan-May 2026 totals, confirming internal consistency of the release.
- conflicting: ['p16', 'p17', 'p18', 'p46', 'p47', 'p48', 'p104'] Two different 2025 annual birth concepts: p16 (671,236, Japanese-national 概数) vs p46 (705,809, preliminary vital statistics including foreign nationals) vs p104 (694,162, final estimates all residents
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p103', 'p105', 'p106', 'p107', 'p108', 'p34', 'p35'] Statistics Bureau final estimates: all-resident July totals equal Japanese + foreign components (p43=p45+p34; p44=p107-equivalent+p35), and p103/p105 duplicate p41/p44. Internally consistent decomposi
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40'] Foreign-population monthly births from the same Statistics Bureau series; annual totals consistent with monthly pattern. Useful for the foreign-resident allowance.
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p65'] March 2025 and trailing-12-month births from an earlier MHLW preliminary release; same series as p1 but older vintage, useful for seasonal shape and trend, not for direct substitution.
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p64'] Marriage registrations from the same earlier release; a lagged conception proxy (d5), weak but usable as a directional check.
- corroborating: ['p19', 'p20', 'p29', 'p30'] TFR values for 2024/2025 and prefecture extremes; contextual, not directly usable for a July monthly count.
- corroborating: ['p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87'] Holiday calendar dates; only p81 (Marine Day 2026 = July 20) is relevant to July 2026 timing; the 2020/2021 Olympic special measures are historical analogues of limited value.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p14'] Same May 2026 preliminary release: p1 and p14 are the same national May 2026 count (59,663) from the summary row and prefecture table; p2 is the May 2025 comparator and p3 the derived difference. One 
- corroborating: ['p6', 'p7', 'p15'] Jan-May 2026 cumulative 282,222 appears in both summary (p6) and prefecture table (p15); p7 is the 2025 comparator. Same release, same measurement.
- corroborating: ['p10', 'p11'] Trailing-12-month levels from the same May 2026 release; consistent with the small YoY decline implied by p1/p2 and p6/p7.
- conflicting: ['p16', 'p17', 'p18', 'p46', 'p47', 'p48', 'p104'] Two different definitions: p16/p17 are Japanese-national (人口動態統計) annual births (671,236 in 2025, 686,173 in 2024), while p46 (705,809) and p104 (694,162) are all-resident totals including foreign nat
- corroborating: ['p31', 'p32', 'p33', 'p119', 'p120', 'p121', 'p129', 'p130', 'p131'] Duplicate vintages of the same foreign-population annual birth series (2022-2024); identical values across snapshots, so redundant copies.
- corroborating: ['p34', 'p35', 'p40', 'p108', 'p113', 'p114', 'p127', 'p128'] Foreign-resident July births: 2023 ~1,586-1,771, 2024 1,979, 2025 1,874. Duplicated vintages agree; the 2023 discrepancy (1,586 vs 1,771) reflects revision/vintage differences, not a real conflict.
- corroborating: ['p43', 'p44', 'p106', 'p110', 'p123'] All-resident July totals: 2024 64,283, 2025 62,521; duplicated vintages agree exactly.
- corroborating: ['p45', 'p107', 'p111', 'p112', 'p132', 'p133'] Japanese-population July births: 2023 64,034, 2024 62,304, 2025 60,647; duplicated vintages agree.
- corroborating: ['p135', 'p136', 'p137', 'p138', 'p139', 'p140'] Jan-Feb 2026 preliminary monthly births from one press report; internally consistent (58,694 + 50,761 = 109,455).
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65'] One March 2025 preliminary release: marriages and births, monthly and cumulative, with derived rates. Single underlying measurement.
- corroborating: ['p81'] Marine Day 2026 date; contextual for day-count/holiday effects but not a birth count.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 vs July 2025 all-resident birth change factor | 0.985 | 0.94..1.03 | 0.8801..1.1 (widened) | ratio | m1 (m1) | Recent preliminary data show near-flat YoY: Jan-May 2026 cumulative +0.4% (p6/p7), trailing-12m -0.4% (p10/p11), May 2026 -1.7% (p1/p2), Jan-Feb 2026 +0.1% (p139/p140). July 2025 was already low; a small decline to flat is the central case, with wide tails for monthly noise. | July 2026 behaves like the recent Jan-May 2026 pattern of near-flat YoY change. | Evidence of a sharp July-specific drop or rebound (e.g., a June 2026 preliminary showing a large YoY swing). |
| a2 | July share of annual all-resident births | 0.088 | 0.082..0.094 | 0.06208..0.1242 (widened) | share | unused | July 2025 62,521 / 2025 all-resident 694,162 (p43/p104) is about 0.090; July 2024 64,283 / 2024 717,291 (p44/p41) is about 0.0896. July is a high-birth month; share is stable around 0.086-0.090. | July's seasonal share of annual births remains near its 2024-2025 level. | A marked shift in the July seasonal pattern. |
| a3 | 2026 annual all-resident births relative to 2025 all-resident births | 0.99 | 0.95..1.03 | 0.6995..1.399 (widened) | ratio | unused | 2025 all-resident births were 694,162 (p104). Recent YoY is near-flat (p6/p7, p10/p11), so 2026 is expected within a few percent of 2025; central case a small decline. | 2026 annual births continue the recent near-flat trend relative to 2025. | A published 2026 annual projection far outside this range. |
| a4 | July 2026 vs July 2025 change factor for Japanese-population births | 0.985 | 0.94..1.03 | 0.8801..1.1 (widened) | ratio | m2 (m3) | Japanese-population July births fell 64,034 (2023) to 62,304 (2024) to 60,647 (2025), about -2.7% then -2.7%; the recent national preliminary trend is near-flat, so a small decline is the central case. | Japanese-population July births continue their recent gentle decline. | Evidence of a sharp July-specific drop or rebound in Japanese-population births. |
| a5 | Foreign-resident share of July births | 0.03 | 0.024..0.037 | 0.02107..0.04214 (widened) | share | m2 (m3) | July 2025 foreign 1,874 / all-resident 62,521 (p34/p43) is about 0.030; July 2024 1,979/64,283 (p35/p44) is about 0.031; July 2023 1,586/65,620 (p127/p109) is about 0.024. Share is stable near 3%. | Foreign-resident share of July births stays near 3%. | Evidence of a sharp change in foreign-resident births. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 61,689 | ['p43'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 61,505 | ['p45'] / ['a4', 'a5'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **61,597** person, 80% interval [44,711, 84,860] person, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in Japan during July 2026, as counted in the MHLW preliminary monthly vital statistics (all residents, including foreign nationals), is 61,597 person (80% model-based interval 44,711 to 84,860 person).

Two methods were combined with weights 50% and 50%. The first anchors on the observed July 2025 all-resident count of 62,521 births and applies a near-flat year-on-year factor of 0.985 (range 0.8801 to 1.1). The second builds from the observed July 2025 Japanese-population count of 60,647 births, a factor of 0.985 (range 0.8801 to 1.1), and a foreign-resident share of 0.03 (range 0.02107 to 0.04214).

Only the July 2025 levels and the foreign share are observed; the change factors and share stability are assumptions. The main risk is that July 2026 deviates from the near-flat trend. The most useful missing evidence is the actual July 2026 preliminary count, unavailable at the cutoff.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 vs July 2025 all-resident birth change factor: 0.985 ratio, range 0.8801 to 1.1 (range widened by code); used by m1. Overturned by: Evidence of a sharp July-specific drop or rebound (e.g., a June 2026 preliminary showing a large YoY swing).
- a4 July 2026 vs July 2025 change factor for Japanese-population births: 0.985 ratio, range 0.8801 to 1.1 (range widened by code); used by m2. Overturned by: Evidence of a sharp July-specific drop or rebound in Japanese-population births.
- a5 Foreign-resident share of July births: 0.03 share, range 0.02107 to 0.04214 (range widened by code); used by m2. Overturned by: Evidence of a sharp change in foreign-resident births.

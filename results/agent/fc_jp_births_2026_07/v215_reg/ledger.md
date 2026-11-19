# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births in Japan during July 2026, as counted in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (including foreign nationals resident in Japan) | unit births | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (MHLW), Japan

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW preliminary monthly vital statistics time series

Hypothesis: July 2026 births will be close to July births in recent years, adjusted for the ongoing downward trend and any calendar effects (number of weekdays, Obon timing). The same-month prior-year values and the most recent months published before the cutoff anchor the level and trend.

Queries issued by the searcher: 厚生労働省 人口動態統計 速報 月次 出生数 2025; MHLW monthly vital statistics preliminary births July 2025 Japan; 人口動態統計速報 令和8年6月分 出生数 2026; 人口動態統計速報 2026年 上半期 出生数 外国人含む; 厚生労働省 人口動態統計 速報 月次 出生数 2025年7月; MHLW monthly vital statistics preliminary births July 2025 Japan; 人口動態統計速報 令和8年6月分 出生数 2026; 人口動態統計速報 2026年5月分 出生数 前年同月比; 厚生労働省 人口動態統計 速報 月次 出生数 2025; MHLW monthly vital statistics preliminary births July 2025; 人口動態統計速報 令和8年 出生数 2026年 月分; www.mhlw.go.jp 人口動態統計速報 令和8年6月分 2026

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/07.html` -> **snapshot** (snapshot 20260317070542); points raw/verified 0/0
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/07.html` -> **snapshot** (snapshot 20260317070800); points raw/verified 0/0
- `https://macrodatahub.com/data/japan-population-vital-statistics-2210` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.at-s.com/wv/news/article/national/1841068.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20260&month=12040606&tclass1=0000010` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.oshima-sr.com/2025/09/26/12137/` -> **snapshot** (snapshot 20260610062101); points raw/verified 0/0
- `https://www.hoikusys.jp/post/%E4%BB%8A%E5%B9%B4%E3%82%82%E5%B0%91%E5%AD%90%E5%8C%96%E3%81%AB%E6%AD%AF%E6%AD%A2%E3%82%81%E3%81%8C%E3%81%8B%E3%81%8B%E3%` -> **snapshot** (snapshot 20260217124037); points raw/verified 12/10
  - p1 Japan live births, January 2025 (preliminary monthly vital statistics) = **58,385** births (2025-01-01..2025-01-31) [DISCARD: Conflicts with MHLW-sourced p69 for the same month (58,385 vs 51,816); different definition/vintage, would corrupt a ser] quote: "今年1月は前年同月より2689人少ない5万8385人"
  - p2 Japan live births, February 2025 (preliminary monthly vital statistics) = **50,951** births (2025-02-01..2025-02-28) [DISCARD: Same secondary-source definitional conflict as p1 (50,951 vs MHLW p70 48,256).] quote: "2月は3581人少ない5万951人"
  - p3 Japan live births, March 2025 (preliminary monthly vital statistics) = **53,619** births (2025-03-01..2025-03-31) [DISCARD: Same secondary-source definitional conflict as p1 (53,619 vs MHLW p71 50,767).] quote: "3月は1579人少ない5万3619人"
  - p4 Japan live births, April 2025 (preliminary monthly vital statistics) = **57,306** births (2025-04-01..2025-04-30) [DISCARD: Same secondary-source definitional conflict as p1 (57,306 vs MHLW p72 54,686).] quote: "4月は1904人少ない5万7306人"
  - p5 Year-on-year decrease in Japan live births, January 2025 vs January 2024 = **2,689** births (2025-01-01..2025-01-31) [DISCARD: Year-on-year decrease tied to the conflicting p1 series; redundant with the MHLW series.] quote: "今年1月は前年同月より2689人少ない5万8385人"
  - p6 Year-on-year decrease in Japan live births, February 2025 vs February 2024 = **3,581** births (2025-02-01..2025-02-28) [DISCARD: Tied to conflicting p2 series; redundant.] quote: "2月は3581人少ない5万951人"
  - p7 Year-on-year decrease in Japan live births, March 2025 vs March 2024 = **1,579** births (2025-03-01..2025-03-31) [DISCARD: Tied to conflicting p3 series; redundant.] quote: "3月は1579人少ない5万3619人"
  - p8 Year-on-year decrease in Japan live births, April 2025 vs April 2024 = **1,904** births (2025-04-01..2025-04-30) [DISCARD: Tied to conflicting p4 series; redundant.] quote: "4月は1904人少ない5万7306人"
  - p9 Cumulative year-on-year decrease in Japan live births, January-April 2025 vs Jan = **9,573** births (2025-01-01..2025-04-30) [DISCARD: Cumulative decrease tied to the conflicting secondary series; redundant with MHLW p73/p74.] quote: "1~4月の累計では、今年が前年に比べて9573人の減少"
  - p10 Possible upper bound on Japan population decrease in 2025 (stated as possibility = **1,000,000** persons (2025-01-01..2025-12-31) [DISCARD: Speculative population-decrease bound, not a birth quantity; irrelevant to the target.] quote: "今年の人口減少数はひょっとすると100万人の大台に達する可能性もありそうです"
- dropped by code checks: 2 (period year 2024 does not appear in the page text or URL (likely mis-dated): 2)

### d2 [related_series] Annual and year-to-date birth totals

Hypothesis: Annual births (calendar year or fiscal year) can be decomposed into monthly shares; July's share of the annual total is fairly stable, so July 2026 ≈ (expected 2026 annual births) × (July share). Alternatively, year-to-date 2026 births × (July share of YTD) gives the monthly figure.

Queries issued by the searcher: Japan annual births 2025 total 出生数 年間 厚生労働省 人口動態統計; 月別 出生数 2024年 構成比 7月 人口動態統計; 人口動態統計速報 令和8年 出生数 月別 2026年 上半期; 人口動態統計 月報 概数 令和7年 月別 出生数 1月 2月 3月 2025; 人口動態統計速報 令和7年7月分 出生数 2025年7月 前年同月比; 2025年 出生数 月別 速報 1月 2月 3月 4月 5月 6月 7月 外国人含む 厚労省; Japan annual births 2025 total 出生数 年間 厚生労働省 人口動態統計; 月別 出生数 構成比 7月 日本 人口動態統計; 人口動態統計速報 令和8年 2026年 出生数 月別 外国人含む; 2026年 上半期 出生数 1～6月 前年比 人口動態統計速報; 人口動態統計速報 令和8年5月分 出生数 累計 1月～5月; 人口動態統計月報 令和8年3月分 出生数 累計 1月～3月 日本人; Japan annual births 2025 total 出生数 年間 厚生労働省; 月別 出生数 構成比 7月 人口動態統計; 2026年 出生数 上半期 速報; 人口動態統計速報 令和8年5月分 出生数 厚生労働省; 人口動態統計速報 2025年 年間 出生数 外国人含む 速報値 年計; mhlw.go.jp 人口動態統計速報 令和8年 2026年 月分 出生数

- `https://www.nikkei.com/article/DGXZQOUA0197C0R00C26A6000000/?utm_source=newsshowcase&utm_medium=gnews&utm_campaign=CDAQvIb1ia2T3-FWGKzipr_l2-2NngEqKgg` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/articles/-/55093` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fukushishimbun.com/fukushiippan/45515` -> **snapshot** (snapshot 20260717142127); points raw/verified 9/9
  - p11 Number of births to Japanese nationals in Japan, 2025 (provisional/rounded vital = **671,236** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に国内で生まれた日本人のこどもの数は前年より1万4937人減の67万1236人だった"
  - p12 Year-on-year decrease in births to Japanese nationals, 2025 vs 2024 = **14,937** births (2025-01-01..2025-12-31) [keep: ] quote: "前年より1万4937人減の67万1236人だった"
  - p13 Total fertility rate (children per woman over lifetime), Japan, 2025 = **1.14** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "合計特殊出生率も1.14で、過去最低となった"
  - p14 Year-on-year change in total fertility rate, Japan, 2025 = **0.01** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "前年より0.01ポイント低下した"
  - p15 Number of marriages, Japan, 2025 = **489,119** marriages (2025-01-01..2025-12-31) [keep: ] quote: "婚姻件数は48万9119組で、前年を4027組上回った"
  - p16 Year-on-year increase in marriages, Japan, 2025 = **4,027** marriages (2025-01-01..2025-12-31) [keep: ] quote: "前年を4027組上回った"
  - p17 Peak number of marriages, Japan, 1972 = **1,099,984** marriages (1972-01-01..1972-12-31) [keep: ] quote: "1972年の109万9984組をピークに減少傾向が続いていた"
  - p18 Number of deaths, Japan, 2025 = **1,589,489** deaths (2025-01-01..2025-12-31) [keep: ] quote: "死亡数は158万9489人で、前年より1万5889人減少した"
  - p19 Year-on-year decrease in deaths, Japan, 2025 = **15,889** deaths (2025-01-01..2025-12-31) [keep: ] quote: "前年より1万5889人減少した"
- `https://news.tv-asahi.co.jp/news_society/articles/000509666.html` -> **snapshot** (snapshot 20260623141240); points raw/verified 8/8
  - p20 Japanese births in Japan, 2025 (preliminary vital statistics, Japanese nationals = **671,236** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に国内で生まれた日本人は67万1236人で、前の年より1万5000人ほど減って過去最少となりました。"
  - p21 Japanese births in Japan, 2025, rounded (about 670,000) = **670,000** births (2025-01-01..2025-12-31) [DISCARD: Rounded duplicate of p11/p20/p28 (671,236); adds no information.] quote: "2025年の日本人の出生数は約67万人で前の年から約1万5000人減少し、10年連続で過去最少となりました。"
  - p22 Year-on-year decrease in Japanese births, 2025 vs 2024 (about) = **15,000** births (2025-01-01..2025-12-31) [DISCARD: Rounded duplicate of p12/p29 (~15,000 decline).] quote: "2025年の日本人の出生数は約67万人で前の年から約1万5000人減少し、10年連続で過去最少となりました。"
  - p23 Consecutive years of record-low Japanese births, 2025 = **10** years (2025-01-01..2025-12-31) [DISCARD: Count of consecutive record-low years; not a birth count, no role in the estimate.] quote: "2025年の日本人の出生数は約67万人で前の年から約1万5000人減少し、10年連続で過去最少となりました。"
  - p24 Total fertility rate, Japan, 2025 = **1.14** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "女性1人が一生のうちに産む子どもの数の指標「合計特殊出生率」は1.14で去年より0.01ポイント減り、こちらも過去最低となっています。"
  - p25 Year-on-year change in total fertility rate, 2025 vs 2024 = **0.01** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "「合計特殊出生率」は1.14で去年より0.01ポイント減り、こちらも過去最低となっています。"
  - p26 Natural population decrease (deaths minus births), Japan, 2025 (about) = **920,000** persons (2025-01-01..2025-12-31) [DISCARD: Rounded natural-decrease figure; redundant with p37 and not a birth count.] quote: "人口は死亡者の数が出生数を92万人ほど上回り、19年連続で「自然減」となっています。"
  - p27 Consecutive years of natural population decrease, Japan, 2025 = **19** years (2025-01-01..2025-12-31) [DISCARD: Count of consecutive natural-decrease years; irrelevant to the July 2026 level.] quote: "人口は死亡者の数が出生数を92万人ほど上回り、19年連続で「自然減」となっています。"
- `https://www.jiji.com/jc/article?g=soc&k=2026060300610&m=rss` -> **snapshot** (snapshot 20260604103732); points raw/verified 29/27
  - p28 Japan total live births (Japanese nationals), calendar year 2025, final vital st = **671,236** births (2025-01-01..2025-12-31) [keep: ] quote: "昨年国内で生まれた子ども(出生数)は67万1236人で、統計がある1899年以降の最少を10年連続で更新。"
  - p29 Year-on-year change in Japan total live births, 2025 vs 2024 (decrease) = **14,937** births (2025-01-01..2025-12-31) [keep: ] quote: "24年に初めて70万人を割り、25年は前年比1万4937人減。"
  - p30 Year-on-year rate of decline in Japan total live births, 2025 vs 2024 = **2.2** % (2025-01-01..2025-12-31) [keep: ] quote: "減少率では、22年以降は5%台で高止まりだったが、今回は2.2%と緩やかになった。"
  - p31 Japan total fertility rate (total special fertility rate), 2025 = **1.14** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "1人の女性が生涯に産む見込みの人数を示す合計特殊出生率も1.14と過去最低だった。"
  - p32 Change in Japan total fertility rate, 2025 vs prior year (points) = **0.01** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "出生率は前年から0.01ポイント下がり、10年連続で低下。"
  - p33 Japan marriages, calendar year 2025 = **489,119** marriages (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数は2年連続で増加し、48万9119組。"
  - p34 Year-on-year change in Japan marriages, 2025 vs 2024 (increase) = **4,027** marriages (2025-01-01..2025-12-31) [keep: ] quote: "前年から4027組増えたが、コロナ禍前の水準(19年は約59.9万組)には戻っていない。"
  - p35 Japan divorces, calendar year 2025 = **179,068** divorces (2025-01-01..2025-12-31) [DISCARD: Divorces; irrelevant to births.] quote: "離婚は17万9068組で減少した。"
  - p36 Japan deaths, calendar year 2025 = **1,589,489** deaths (2025-01-01..2025-12-31) [keep: ] quote: "死亡数は158万9489人で、5年ぶりに減少。"
  - p37 Japan natural decrease (deaths minus births), calendar year 2025 = **918,253** persons (2025-01-01..2025-12-31) [keep: ] quote: "19年連続で死亡数が出生数を上回る自然減となり、減少幅は91万8253人だった。"
  - p38 Average age at first marriage, husbands, Japan 2025 = **31** years (2025-01-01..2025-12-31) [DISCARD: Mean age at first marriage; no numerical role.] quote: "平均初婚年齢は夫31.0歳、妻29.7歳。"
  - p39 Average age at first marriage, wives, Japan 2025 = **29.7** years (2025-01-01..2025-12-31) [DISCARD: Mean age at first marriage; no numerical role.] quote: "平均初婚年齢は夫31.0歳、妻29.7歳。"
  - p40 Average age of mother at first child's birth, Japan 2025 = **31** years (2025-01-01..2025-12-31) [DISCARD: Mean age of mother at first birth; no numerical role.] quote: "第1子出生時の母の平均年齢は31.0歳だった。"
  - p41 Japan total fertility rate, Okinawa (highest prefecture), 2025 = **1.52** births per woman (2025-01-01..2025-12-31) [DISCARD: Prefectural TFR (Okinawa); irrelevant to national monthly level.] quote: "沖縄(1.52)が最高で、宮崎(1.46)、福井(1.45)が続いた。"
  - p42 Japan total fertility rate, Miyazaki, 2025 = **1.46** births per woman (2025-01-01..2025-12-31) [DISCARD: Prefectural TFR (Miyazaki); irrelevant.] quote: "沖縄(1.52)が最高で、宮崎(1.46)、福井(1.45)が続いた。"
  - p43 Japan total fertility rate, Fukui, 2025 = **1.45** births per woman (2025-01-01..2025-12-31) [DISCARD: Prefectural TFR (Fukui); irrelevant.] quote: "沖縄(1.52)が最高で、宮崎(1.46)、福井(1.45)が続いた。"
  - p44 Japan total fertility rate, Tokyo (lowest prefecture), 2025 = **0.96** births per woman (2025-01-01..2025-12-31) [DISCARD: Prefectural TFR (Tokyo); irrelevant to national monthly level.] quote: "東京(0.96)が最も低く、3年連続で「1」を切った。"
  - p45 Japan total fertility rate, Hokkaido and Miyagi, 2025 = **1** births per woman (2025-01-01..2025-12-31) [DISCARD: Prefectural TFR (Hokkaido/Miyagi); irrelevant.] quote: "次いで北海道と宮城が1.00だった。"
  - p46 Number of prefectures with rising total fertility rate, Japan 2025 = **13** prefectures (2025-01-01..2025-12-31) [DISCARD: Count of prefectures with rising TFR; irrelevant.] quote: "都道府県別では西高東低の傾向で、13県で上昇した。"
  - p47 Number of prefectures with rising births, Japan 2025 = **4** prefectures (2025-01-01..2025-12-31) [DISCARD: Count of prefectures with rising births; irrelevant.] quote: "東京、富山、石川、香川の4都県は増加した。"
  - p48 Year Japan total births first fell below 1 million = **2,016** year (2016-01-01..2016-12-31) [DISCARD: Year births fell below 1 million; historical context only, no numerical role.] quote: "出生数は1975年以降、減少傾向で、2016年に100万人を下回った。"
  - p49 Number of consecutive years of record-low births, Japan through 2025 = **10** years (2016-01-01..2025-12-31) [DISCARD: Consecutive record-low years; irrelevant.] quote: "統計がある1899年以降の最少を10年連続で更新。"
  - p50 Number of consecutive years of declining total fertility rate, Japan through 202 = **10** years (2016-01-01..2025-12-31) [DISCARD: Consecutive TFR-decline years; irrelevant.] quote: "出生率は前年から0.01ポイント下がり、10年連続で低下。"
  - p51 Number of consecutive years deaths exceeded births (natural decrease), Japan thr = **19** years (2007-01-01..2025-12-31) [DISCARD: Consecutive natural-decrease years; irrelevant.] quote: "19年連続で死亡数が出生数を上回る自然減となり、減少幅は91万8253人だった。"
  - p52 Number of consecutive years Tokyo total fertility rate below 1, through 2025 = **3** years (2023-01-01..2025-12-31) [DISCARD: Consecutive years Tokyo TFR below 1; irrelevant.] quote: "東京(0.96)が最も低く、3年連続で「1」を切った。"
  - p53 Number of consecutive years marriages increased, Japan through 2025 = **2** years (2024-01-01..2025-12-31) [DISCARD: Consecutive marriage-increase years; irrelevant.] quote: "婚姻数は2年連続で増加し、48万9119組。"
  - p54 Gap between actual timing of Japan's declining births and National Institute of  = **15** years (not stated (page dated 2026-06-03)) [DISCARD: Gap vs IPSS projection; qualitative, no numerical role.] quote: "しかし、国立社会保障・人口問題研究所の将来推計より15年ほど速く少子化が進んでいる。"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2024/07.html` -> **snapshot** (snapshot 20260320021543); points raw/verified 0/0
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202401013A-sonota2_0.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/pluralphoto/20260603-GYT1I00260/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/pluralphoto/20260603-GYT1I00207/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fukushishimbun.com/fukushiippan/44681` -> **snapshot** (snapshot 20260715221331); points raw/verified 9/9
  - p55 Live births in Japan in 2025, including foreign nationals, preliminary (速報値) = **705,809** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に生まれた外国人を含むこどもの数は70万5809人となり、10年連続で最少を更新した。"
  - p56 Year-on-year change in 2025 live births including foreign nationals, preliminary = **2.1** as written "2・1%", value check pending % (2025-01-01..2025-12-31) [DISCARD: Redundant with p318/p55 (2.1% decline).] quote: "前年から2・1%減った。"
  - p57 Natural decrease (deaths minus births) in Japan in 2025, preliminary = **899,845** persons (2025-01-01..2025-12-31) [DISCARD: Natural decrease; redundant with p320 and not a birth count.] quote: "死亡数から出生数を差し引いた人口の「自然減」は89万9845人で過去最大となり"
  - p58 Peak Japanese births in 1949 = **2,690,000** births (1949-01-01..1949-12-31) [DISCARD: 1949 peak births; historical context only.] quote: "日本人の出生数は1949年の約269万人をピークに75年ごろから減少傾向で、2016年に100万人を割った。"
  - p59 Year Japanese births fell below 1 million = **1,000,000** births (2016-01-01..2016-12-31) [DISCARD: Year births fell below 1 million; historical context only.] quote: "2016年に100万人を割った。"
  - p60 Increase in marriages in 2025 vs prior-year preliminary = **5,657** marriages (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数は前年速報値から5657組(1・1%)増加し"
  - p61 Percent increase in marriages in 2025 vs prior-year preliminary = **1.1** as written "1・1%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数は前年速報値から5657組(1・1%)増加し"
  - p62 Decrease in divorces in 2025 vs prior-year preliminary = **6,983** divorces (2025-01-01..2025-12-31) [DISCARD: Divorce change; irrelevant.] quote: "離婚数は同6983組(3・7%)減った。"
  - p63 Percent decrease in divorces in 2025 vs prior-year preliminary = **3.7** as written "3・7%", value check pending % (2025-01-01..2025-12-31) [DISCARD: Divorce percent change; irrelevant.] quote: "離婚数は同6983組(3・7%)減った。"
- `https://times.abema.tv/articles/-/10250160` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ubrand.udn.com/ubrand/story/123656/9545898?form=udn_ch2_common3_cate` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period year 2019 does not appear in the page text or URL (likely mis-dated): 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d3 [base_rates] Seasonal birth pattern and month-to-month ratios

Hypothesis: The ratio of July births to adjacent months (June, August) and to the same month prior year is stable; applying these ratios to known 2026 June or 2025 July values yields July 2026. This route needs the seasonal ratio and one anchor month.

Queries issued by the searcher: 月別 出生数 2024 2025 6月 7月 8月 人口動態統計; 人口動態統計 月次 出生数 推移 2025 7月; Japan monthly live births July 2024 June August statistics; 2026年6月 出生数 人口動態統計 速報; 月別 出生数 2024 2025 6月 7月 8月 人口動態統計; 人口動態統計 月次 出生数 推移 2025年; 人口動態統計速報 令和8年6月分 出生数; 2025年7月 出生数 速報 日本人 5万人 前年同月; 人口動態統計月報 概数 第2表 人口動態総覧 月別 2025年 出生数 7月 8月; 人口動態統計速報 令和8年5月分 出生数 1～5月; 人口動態統計 月次 出生数 2025年 6月 7月 8月; 月別 出生数 2024 2025 6月 7月 8月 日本; 人口動態統計月報（概数）（令和8年6月分） 出生数; 2025年 年間 出生数 月別 1月 2月 3月 4月 5月 6月 7月 8月 厚生労働省 概数

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/06.html` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202401013A-sonota2_0.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/dl/toukeihyo_04.pdf` -> **snapshot** (snapshot 20260320011915); points raw/verified 30/30
  - p64 Japan live births, July 2024 (provisional monthly vital statistics) = **62,306** as written "62 306", value check ok birth (2024-07-01..2024-07-31) [keep: ] quote: "7月 62 306 126 383 115 51 △ 64 077 567 680 204 46 747 15 630"
  - p65 Japan live births, June 2024 (provisional monthly vital statistics) = **55,313** as written "55 313", value check pending birth (2024-06-01..2024-06-30) [keep: ] quote: "6月 55 313 116 489 130 75 △ 61 176 534 698 209 32 030 14 025"
  - p66 Japan live births, August 2024 (provisional monthly vital statistics) = **60,698** as written "60 698", value check pending birth (2024-08-01..2024-08-31) [keep: ] quote: "8月 60 698 132 797 100 47 △ 72 099 621 639 187 39 619 14 341"
  - p67 Japan live births, May 2024 (provisional monthly vital statistics) = **59,144** as written "59 144", value check pending birth (2024-05-01..2024-05-31) [keep: ] quote: "5月 59 144 124 167 114 60 △ 65 023 553 717 179 45 949 15 454"
  - p68 Japan live births, April 2024 (provisional monthly vital statistics) = **56,563** as written "56 563", value check pending birth (2024-04-01..2024-04-30) [keep: ] quote: "4月 56 563 126 195 99 52 △ 69 632 557 732 181 30 158 16 580"
  - p69 Japan live births, January 2025 (provisional monthly vital statistics) = **51,816** as written "51 816", value check pending birth (2025-01-01..2025-01-31) [keep: ] quote: "令和7年1月 51 816 172 287 124 56 △120 471 570 682 186 32 401 14 045"
  - p70 Japan live births, February 2025 (provisional monthly vital statistics) = **48,256** as written "48 256", value check pending birth (2025-02-01..2025-02-28) [keep: ] quote: "2月 48 256 141 104 96 36 △ 92 848 550 690 157 40 110 13 883"
  - p71 Japan live births, March 2025 (provisional monthly vital statistics) = **50,767** as written "50 767", value check pending birth (2025-03-01..2025-03-31) [keep: ] quote: "3月 50 767 143 597 114 54 △ 92 830 555 730 186 54 342 19 365"
  - p72 Japan live births, April 2025 (provisional monthly vital statistics) = **54,686** as written "54 686", value check pending birth (2025-04-01..2025-04-30) [keep: ] quote: "4月 54 686 128 369 114 50 △ 73 683 551 759 190 30 287 15 436"
  - p73 Japan live births, cumulative January-April 2025 (provisional monthly vital stat = **205,525** as written "205 525", value check pending birth (2025-01-01..2025-04-30) [keep: ] quote: "205 525 215 541 △ 10 016 △ 4.6 5.2 5.4"
  - p74 Japan live births, cumulative January-April 2024 (provisional monthly vital stat = **215,541** as written "215 541", value check pending birth (2024-01-01..2024-04-30) [keep: ] quote: "205 525 215 541 △ 10 016 △ 4.6 5.2 5.4"
  - p75 Japan live births, July 2023 (trailing 12-month cumulative table, monthly increm = **703,307** as written "703 307", value check pending birth (2023-08-01..2024-07-31) [DISCARD: Trailing-12-month cumulative value mislabeled as a monthly increment; not a monthly birth count and not usable as a leve] quote: "7月 703 307 1 596 834 △ 893 527"
  - p76 Japan live births, June 2023 (trailing 12-month cumulative table, monthly increm = **705,035** as written "705 035", value check pending birth (2023-07-01..2024-06-30) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "6月 705 035 1 589 863 △ 884 828"
  - p77 Japan live births, August 2023 (trailing 12-month cumulative table, monthly incr = **698,641** as written "698 641", value check pending birth (2023-09-01..2024-08-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "8月 698 641 1 599 941 △ 901 300"
  - p78 Japan live births, April 2025 (trailing 12-month cumulative table, monthly incre = **676,045** as written "676 045", value check pending birth (2024-05-01..2025-04-30) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "4月 676 045 1 631 037 △ 954 992"
  - p79 Japan live births, March 2025 (trailing 12-month cumulative table, monthly incre = **677,922** as written "677 922", value check pending birth (2024-04-01..2025-03-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "3月 677 922 1 628 863 △ 950 941"
  - p80 Japan live births, February 2025 (trailing 12-month cumulative table, monthly in = **679,625** as written "679 625", value check pending birth (2024-03-01..2025-02-28) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "2月 679 625 1 628 203 △ 948 578"
  - p81 Japan live births, January 2025 (trailing 12-month cumulative table, monthly inc = **683,253** as written "683 253", value check pending birth (2024-02-01..2025-01-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "令和7年 1月 683 253 1 625 597 △ 942 344"
  - p82 Japan live births, December 2024 (trailing 12-month cumulative table, monthly in = **686,061** as written "686 061", value check pending birth (2024-01-01..2024-12-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "12月 686 061 1 605 298 △ 919 237"
  - p83 Japan live births, November 2024 (trailing 12-month cumulative table, monthly in = **688,945** as written "688 945", value check pending birth (2023-12-01..2024-11-30) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "11月 688 945 1 593 467 △ 904 522"
  - p84 Japan live births, October 2024 (trailing 12-month cumulative table, monthly inc = **693,699** as written "693 699", value check pending birth (2023-11-01..2024-10-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "10月 693 699 1 594 160 △ 900 461"
  - p85 Japan live births, September 2024 (trailing 12-month cumulative table, monthly i = **695,414** as written "695 414", value check pending birth (2023-10-01..2024-09-30) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "9月 695 414 1 598 526 △ 903 112"
  - p86 Japan live births, May 2024 (trailing 12-month cumulative table, monthly increme = **711,100** as written "711 100", value check pending birth (2023-06-01..2024-05-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "5月 711 100 1 585 763 △ 874 663"
  - p87 Japan live births, April 2024 (trailing 12-month cumulative table, monthly incre = **713,982** as written "713 982", value check pending birth (2023-05-01..2024-04-30) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "4月 713 982 1 582 619 △ 868 637"
  - p88 Japan live births, March 2024 (trailing 12-month cumulative table, monthly incre = **715,181** as written "715 181", value check pending birth (2023-04-01..2024-03-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "3月 715 181 1 578 265 △ 863 084"
  - p89 Japan live births, February 2024 (trailing 12-month cumulative table, monthly in = **721,552** as written "721 552", value check pending birth (2023-03-01..2024-02-29) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "2月 721 552 1 567 924 △ 846 372"
  - p90 Japan live births, January 2024 (trailing 12-month cumulative table, monthly inc = **724,172** as written "724 172", value check pending birth (2023-02-01..2024-01-31) [DISCARD: Trailing-12-month cumulative, not a monthly count.] quote: "令和6年 1月 724 172 1 563 660 △ 839 488"
  - p91 Japan live birth rate, July 2024 (per 1,000 population) = **6.1** birth per 1,000 population (2024-07-01..2024-07-31) [DISCARD: Birth rate per 1,000 population, not a count; redundant with p64.] quote: "6.1 12.4 1.9 0.8 △ 6.3 8.9 10.7 3.3 4.6 1.53 7月"
  - p92 Japan live birth rate, June 2024 (per 1,000 population) = **5.6** birth per 1,000 population (2024-06-01..2024-06-30) [DISCARD: Birth rate, not a count; redundant with p65.] quote: "5.6 11.8 2.2 1.4 △ 6.2 9.4 12.3 3.8 3.2 1.42 6月"
  - p93 Japan live birth rate, August 2024 (per 1,000 population) = **5.9** birth per 1,000 population (2024-08-01..2024-08-31) [DISCARD: Birth rate, not a count; redundant with p66.] quote: "5.9 13.0 1.7 0.8 △ 7.1 10.0 10.3 3.1 3.9 1.40 8月"
- `https://www-pref-saga-lg-jp.cache.yimg.jp/toukei/kiji003112552/3_112552_up_jgdkjq74.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search/database?page=1&layout=dataset&iroha=4&toukei=00450011&tstat=000001028897&statdisp_id=0003411630` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/sokuhou/2025/07/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/07.html` -> **snapshot** (snapshot 20260317070800); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/08.html` -> **snapshot** (snapshot 20260525075511); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2024/07.html` -> **snapshot** (snapshot 20260320021543); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2024/08.html` -> **snapshot** (snapshot 20260424064953); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2024/06.html` -> **snapshot** (snapshot 20260317070602); points raw/verified 0/0

### d4 [related_series] Population and birth-rate bridge

Hypothesis: Births ≈ population of women of childbearing age × age-specific fertility rates summed; or births ≈ mid-year population × crude birth rate / 12 with a July seasonal factor. A declining population and fertility rate imply July 2026 below July 2025.

Queries issued by the searcher: 人口推計 2026年 年齢別 女性 20代 30代 総務省; Japan crude birth rate 2025 population estimates; 人口動態統計 速報 令和8年 2026年 出生数 月別 7月; 令和7年 2025年 月別 出生数 1月 2月 3月 人口動態統計 月報; 人口推計 2025年 年齢別 女性 20代 30代 総務省; Japan crude birth rate 2025 vital statistics; 人口動態統計速報 2025年7月分 出生数 厚生労働省; 人口動態統計速報 2026年 月別 出生数 減少; 人口推計 2026 年齢別 女性 20代 30代 総務省; Japan crude birth rate 2025 合計特殊出生率 2025 人口動態統計; 人口動態統計速報 令和8年 2026年 出生数 月別 厚生労働省; 2025年7月 出生数 人口動態統計速報 月別 出生数 日本人

- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040455463&iroha=40` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gender.go.jp/about_danjo/whitepaper/r08/zentai/pdf/05.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_05.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/07.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei25/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cas.go.jp/jp/seisaku/jinko_senryaku/contents/20261028/01_ref01.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/stat-search/files?iroha=18&layout=dataset&page=1&toukei=00450011&tstat=000001028897` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://portal.ijamp.jiji.com/portal/news/detail/2026082800725` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tsuchihashi-siki.com/topics/9573/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.desh.tv/international/89150` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://historysaid.com/japan/population/2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [administrative] Resident registration and notification counts

Hypothesis: Birth notifications filed with municipalities (出生届) and resident-registration-based birth counts track MHLW preliminary births closely; a partial count of notifications for July 2026 from major municipalities or a national registry extract could proxy the target, with a coverage adjustment.

Queries issued by the searcher: 出生届 受理 2026年7月 自治体 出生数; 人口動態統計速報 2026年 出生数 月別; 住民基本台帳 月別 出生数 2026年7月 政令市 人口動態; 東京都 人口動態統計 速報 令和8年7月 出生数; 出生届 受理 件数 2026年7月 自治体; 人口動態統計 速報 2026年 出生数 月次; 東京都 出生数 2026年7月 速報 人口動態; 人口動態統計速報 令和8年6月分 公表 2026年8月 出生数; 人口動態統計速報 令和8年6月分 出生数 令和8年8月25日 公表; 2025年7月 出生数 速報 人口動態 前年同月比; 人口動態統計速報 2026年 出生数; 出生届 受理 2026年7月 自治体; 2025年7月 出生数 人口動態統計速報 前年同月; 東京都 出生数 2026年6月 速報 人口動態; 住民基本台帳 出生数 2026年 上半期 届出

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 29/29
  - p94 National births (出生数), May 2026, preliminary vital statistics = **59,663** as written "59 663", value check ok birth (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p95 National births (出生数), May 2025, preliminary = **60,718** as written "60 718", value check pending birth (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p96 Year-on-year change in national births, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending birth (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p97 Year-on-year percent change in national births, May 2026 = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p98 National cumulative births (出生数), Jan-May 2026 = **282,222** as written "282 222", value check ok birth (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p99 National cumulative births, Jan-May 2025 = **280,979** as written "280 979", value check ok birth (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p100 National cumulative births, Jan-May 2026, year-on-year percent change = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p101 National births, trailing 12 months Jun 2025-May 2026 = **707,052** as written "707 052", value check pending birth (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p102 National births, trailing 12 months Jun 2024-May 2025 = **709,893** as written "709 893", value check pending birth (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p103 National births, trailing 12 months Jun 2025-May 2026, year-on-year percent chan = **0.4** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p104 National births, May 2026, annualised rate per 1,000 population = **5.7** birth/(1000 person*year) (2026-05-01..2026-05-31) [DISCARD: Rate per 1,000, not a count; redundant with p94.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p105 National births, May 2025, annualised rate per 1,000 population = **5.8** birth/(1000 person*year) (2025-05-01..2025-05-31) [DISCARD: Rate per 1,000, not a count; redundant with p95.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p106 National births, Jan-May 2026 cumulative, annualised rate per 1,000 population = **5.6** birth/(1000 person*year) (2026-01-01..2026-05-31) [DISCARD: Rate per 1,000, not a count; redundant with p98.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p107 National births, trailing 12 months Jun 2025-May 2026, rate per 1,000 population = **5.7** birth/(1000 person*year) (2025-06-01..2026-05-31) [DISCARD: Rate per 1,000, not a count; redundant with p101.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p108 National births, May 2026, ratio to previous year (percent) = **98.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p109 National births, Jan-May 2026 cumulative, ratio to previous year (percent) = **101** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p110 National births, trailing 12 months Jun 2025-May 2026, ratio to previous year (p = **100** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p111 Tokyo prefecture births, May 2026 = **8,240** as written "8 240", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Tokyo May 2026 births; sub-national, no national scaling available.] quote: "13 東 京 8 240 10 540 166 7 227 1 540"
  - p112 Tokyo prefecture births, Jan-May 2026 cumulative = **36,470** as written "36 470", value check pending birth (2026-01-01..2026-05-31) [DISCARD: Tokyo cumulative births; sub-national.] quote: "13 東 京 36 470 58 325 846 34 840 8 585"
  - p113 Tokyo 23 wards (東京都区部) births, May 2026 = **6,075** as written "6 075", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Tokyo 23 wards births; sub-national.] quote: "東京都区部 6 075 6 929 127 5 937 1 141"
  - p114 Tokyo 23 wards births, Jan-May 2026 cumulative = **26,759** as written "26 759", value check pending birth (2026-01-01..2026-05-31) [DISCARD: Tokyo 23 wards cumulative; sub-national.] quote: "東京都区部 26 759 38 378 671 28 462 6 226"
  - p115 Osaka prefecture births, May 2026 = **4,733** as written "4 733", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Osaka births; sub-national.] quote: "27 大 阪 4 733 8 418 99 3 468 1 117"
  - p116 Osaka prefecture births, Jan-May 2026 cumulative = **22,215** as written "22 215", value check pending birth (2026-01-01..2026-05-31) [DISCARD: Osaka cumulative; sub-national.] quote: "27 大 阪 22 215 45 134 515 17 705 6 070"
  - p117 Aichi prefecture births, May 2026 = **3,987** as written "3 987", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Aichi births; sub-national.] quote: "23 愛 知 3 987 6 363 68 2 863 821"
  - p118 Kanagawa prefecture births, May 2026 = **4,536** as written "4 536", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Kanagawa births; sub-national.] quote: "14 神 奈 川 4 536 8 010 124 3 393 999"
  - p119 Saitama prefecture births, May 2026 = **3,579** as written "3 579", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Saitama births; sub-national.] quote: "11 埼 玉 3 579 6 667 91 2 220 752"
  - p120 Chiba prefecture births, May 2026 = **3,036** as written "3 036", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Chiba births; sub-national.] quote: "12 千 葉 3 036 5 817 73 1 971 664"
  - p121 Fukuoka prefecture births, May 2026 = **2,785** as written "2 785", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Fukuoka births; sub-national.] quote: "40 福 岡 2 785 4 839 76 1 713 653"
  - p122 Hokkaido births, May 2026 = **1,865** as written "1 865", value check pending birth (2026-05-01..2026-05-31) [DISCARD: Hokkaido births; sub-national.] quote: "01 北 海 道 1 865 6 104 48 1 421 633"
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20260&month=12040606&tclass1=0000010` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.city.inzai.lg.jp/0000001390.html` -> **snapshot** (snapshot 20260311072450); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.crosshealthjp.org/articles/2026072705/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.city.nanao.lg.jp/shimin/aramashi/profile/jinko/tsukibetsu.html` -> **snapshot** (snapshot 20260716082130); points raw/verified 28/28
  - p123 Nanao City monthly births, May 2026 (Reiwa 8) = **6** birth (2026-05-01..2026-05-31) [DISCARD: Single small municipality (Nanao, ~50k pop); too small and noisy to scale to national July births.] quote: "\| 令和8年 \| 5月 \| 6 \| 64 \| 4 \| 82 \| 101 \| 0 \|"
  - p124 Nanao City monthly births, April 2026 (Reiwa 8) = **9** birth (2026-04-01..2026-04-30) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 4月 \| 9 \| 69 \| 4 \| 187 \| 186 \| 0 \|"
  - p125 Nanao City monthly births, March 2026 (Reiwa 8) = **14** birth (2026-03-01..2026-03-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 3月 \| 14 \| 65 \| 11 \| 157 \| 404 \| 0 \|"
  - p126 Nanao City monthly births, February 2026 (Reiwa 8) = **6** birth (2026-02-01..2026-02-28) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 2月 \| 6 \| 51 \| 9 \| 67 \| 122 \| 1 \|"
  - p127 Nanao City monthly births, January 2026 (Reiwa 8) = **15** birth (2026-01-01..2026-01-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 1月 \| 15 \| 83 \| 6 \| 98 \| 113 \| 0 \|"
  - p128 Nanao City monthly births, July 2025 (Reiwa 7) = **15** birth (2025-07-01..2025-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 15 \| 65 \| 10 \| 82 \| 111 \| 0 \|"
  - p129 Nanao City monthly births, June 2025 (Reiwa 7) = **16** birth (2025-06-01..2025-06-30) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 6月 \| 16 \| 64 \| 11 \| 85 \| 101 \| 0 \|"
  - p130 Nanao City monthly births, July 2024 (Reiwa 6) = **24** birth (2024-07-01..2024-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 24 \| 71 \| 8 \| 103 \| 118 \| 0 \|"
  - p131 Nanao City monthly births, July 2023 (Reiwa 5) = **22** birth (2023-07-01..2023-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 22 \| 73 \| 7 \| 94 \| 90 \| 0 \|"
  - p132 Nanao City monthly births, July 2022 (Reiwa 4) = **19** birth (2022-07-01..2022-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 19 \| 60 \| 7 \| 114 \| 102 \| 1 \|"
  - p133 Nanao City monthly births, July 2021 (Reiwa 3) = **17** birth (2021-07-01..2021-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 17 \| 71 \| 8 \| 88 \| 88 \| 0 \|"
  - p134 Nanao City monthly births, July 2020 (Reiwa 2) = **22** birth (2020-07-01..2020-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 22 \| 52 \| 11 \| 50 \| 107 \| 2 \|"
  - p135 Nanao City monthly births, July 2019 (Reiwa 1) = **24** birth (2019-07-01..2019-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 24 \| 65 \| 17 \| 106 \| 111 \| 2 \|"
  - p136 Nanao City monthly births, July 2018 (Heisei 30) = **19** birth (2018-07-01..2018-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 19 \| 54 \| 20 \| 89 \| 96 \| 1 \|"
  - p137 Nanao City monthly births, July 2017 (Heisei 29) = **25** birth (2017-07-01..2017-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 25 \| 51 \| 15 \| 128 \| 90 \| 4 \|"
  - p138 Nanao City monthly births, July 2016 (Heisei 28) = **34** birth (2016-07-01..2016-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 34 \| 67 \| 18 \| 125 \| 88 \| 0 \|"
  - p139 Nanao City monthly births, July 2015 (Heisei 27) = **39** birth (2015-07-01..2015-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 39 \| 79 \| 17 \| 112 \| 106 \| 1 \|"
  - p140 Nanao City monthly births, July 2014 (Heisei 26) = **24** birth (2014-07-01..2014-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 24 \| 64 \| 15 \| 88 \| 114 \| 0 \|"
  - p141 Nanao City monthly births, July 2013 (Heisei 25) = **26** birth (2013-07-01..2013-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 26 \| 56 \| 21 \| 96 \| 116 \| 2 \|"
  - p142 Nanao City monthly births, July 2012 (Heisei 24) = **34** birth (2012-07-01..2012-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 34 \| 53 \| 22 \| 86 \| 101 \| 1 \|"
  - p143 Nanao City monthly births, July 2011 (Heisei 23) = **38** birth (2011-07-01..2011-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 38 \| 58 \| 23 \| 67 \| 71 \| 1 \|"
  - p144 Nanao City monthly births, July 2010 (Heisei 22) = **39** birth (2010-07-01..2010-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 39 \| 54 \| 9 \| 82 \| 118 \| 0 \|"
  - p145 Nanao City monthly births, July 2009 (Heisei 21) = **36** birth (2009-07-01..2009-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 36 \| 59 \| 16 \| 85 \| 114 \| 2 \|"
  - p146 Nanao City monthly births, July 2008 (Heisei 20) = **27** birth (2008-07-01..2008-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 27 \| 51 \| 26 \| 101 \| 92 \| 1 \|"
  - p147 Nanao City monthly births, July 2007 (Heisei 19) = **45** birth (2007-07-01..2007-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 45 \| 58 \| 29 \| 54 \| 100 \| 1 \|"
  - p148 Nanao City monthly births, July 2006 (Heisei 18) = **41** birth (2006-07-01..2006-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 41 \| 62 \| 18 \| 84 \| 107 \| -1 \|"
  - p149 Nanao City monthly births, July 2005 (Heisei 17) = **32** birth (2005-07-01..2005-07-31) [DISCARD: Nanao City — too small to scale.] quote: "\| \| 7月 \| 32 \| 45 \| 26 \| 81 \| 144 \| 1 \|"
  - p150 Nanao City monthly births, June 2026 (Reiwa 8) — not listed; latest month in tab = **5** month (2026-05-01..2026-05-31) [DISCARD: Not a birth count; a note that the table ends at May 2026.] quote: "平成17年4月~令和8年5月末まで"
- `https://www.city.ishikari.hokkaido.jp/shisei/gaiyo/1001900/1005671/1007053.html` -> **snapshot** (snapshot 20260412232558); points raw/verified 21/21
  - p151 Ishikari City natural-change births, January 2026 (of which foreign nationals) = **21** as written "21(1)", value check pending birth (2026-01-01..2026-01-31) [DISCARD: Ishikari City — single small municipality, not scalable.] quote: "- 自然動態(うち外国人)出生 - 21(1)"
  - p152 Ishikari City natural-change deaths, January 2026 = **95** death (2026-01-01..2026-01-31) [DISCARD: Ishikari City deaths — irrelevant.] quote: "- 自然動態(うち外国人)死亡 - 95"
  - p153 Ishikari City natural-change net change, January 2026 (of which foreign national = **-74** as written "-74(1)", value check pending person (2026-01-01..2026-01-31) [DISCARD: Ishikari City net change — irrelevant.] quote: "- 自然動態(うち外国人)増減 - -74(1)"
  - p154 Ishikari City social-change in-migrants, January 2026 (of which foreign national = **124** as written "124(21)", value check pending person (2026-01-01..2026-01-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転入 - 124(21)"
  - p155 Ishikari City social-change out-migrants, January 2026 (of which foreign nationa = **138** as written "138(20)", value check pending person (2026-01-01..2026-01-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転出 - 138(20)"
  - p156 Ishikari City social-change net change, January 2026 (of which foreign nationals = **-14** as written "-14(1)", value check pending person (2026-01-01..2026-01-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)増減 - -14(1)"
  - p157 Ishikari City month-end population, January 2026 (of which foreign nationals) = **56,757** as written "56,757(1,035)", value check pending person (2026-01-31..2026-01-31) [DISCARD: Ishikari City population — irrelevant.] quote: "- 末日人口(うち外国人) - 56,757(1,035)"
  - p158 Ishikari City natural-change births, February 2026 = **16** birth (2026-02-01..2026-02-28) [DISCARD: Ishikari City — single small municipality, not scalable.] quote: "- 自然動態(うち外国人)出生 - 16"
  - p159 Ishikari City natural-change deaths, February 2026 (of which foreign nationals) = **70** as written "70(1)", value check pending death (2026-02-01..2026-02-28) [DISCARD: Ishikari City deaths — irrelevant.] quote: "- 自然動態(うち外国人)死亡 - 70(1)"
  - p160 Ishikari City natural-change net change, February 2026 (of which foreign nationa = **-54** as written "-54(-1)", value check pending person (2026-02-01..2026-02-28) [DISCARD: Ishikari City net change — irrelevant.] quote: "- 自然動態(うち外国人)増減 - -54(-1)"
  - p161 Ishikari City social-change in-migrants, February 2026 (of which foreign nationa = **109** as written "109(29)", value check pending person (2026-02-01..2026-02-28) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転入 - 109(29)"
  - p162 Ishikari City social-change out-migrants, February 2026 (of which foreign nation = **119** as written "119(26)", value check pending person (2026-02-01..2026-02-28) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転出 - 119(26)"
  - p163 Ishikari City social-change net change, February 2026 (of which foreign national = **-10** as written "-10(3)", value check pending person (2026-02-01..2026-02-28) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)増減 - -10(3)"
  - p164 Ishikari City month-end population, February 2026 (of which foreign nationals) = **56,693** as written "56,693(1,037)", value check pending person (2026-02-28..2026-02-28) [DISCARD: Ishikari City population — irrelevant.] quote: "- 末日人口(うち外国人) - 56,693(1,037)"
  - p165 Ishikari City natural-change births, March 2026 = **21** birth (2026-03-01..2026-03-31) [DISCARD: Ishikari City — single small municipality, not scalable.] quote: "- 自然動態(うち外国人)出生 - 21"
  - p166 Ishikari City natural-change deaths, March 2026 = **64** death (2026-03-01..2026-03-31) [DISCARD: Ishikari City deaths — irrelevant.] quote: "- 自然動態(うち外国人)死亡 - 64"
  - p167 Ishikari City natural-change net change, March 2026 = **-43** person (2026-03-01..2026-03-31) [DISCARD: Ishikari City net change — irrelevant.] quote: "- 自然動態(うち外国人)増減 - -43"
  - p168 Ishikari City social-change in-migrants, March 2026 (of which foreign nationals) = **279** as written "279(47)", value check pending person (2026-03-01..2026-03-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転入 - 279(47)"
  - p169 Ishikari City social-change out-migrants, March 2026 (of which foreign nationals = **327** as written "327(21)", value check pending person (2026-03-01..2026-03-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)転出 - 327(21)"
  - p170 Ishikari City social-change net change, March 2026 (of which foreign nationals) = **-48** as written "-48(26)", value check pending person (2026-03-01..2026-03-31) [DISCARD: Ishikari City migration — irrelevant.] quote: "- 社会動態(うち外国人)増減 - -48(26)"
  - p171 Ishikari City month-end population, March 2026 (of which foreign nationals) = **56,601** as written "56,601(1,063)", value check pending person (2026-03-31..2026-03-31) [DISCARD: Ishikari City population — irrelevant.] quote: "- 末日人口(うち外国人) - 56,601(1,063)"
- `https://ckan.pf-sapporo.jp/dataset/8-2026` -> **snapshot** (snapshot 20260712152103); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&toukei=00200241&tstat=000001039591` -> **snapshot** (snapshot 20251005195444); points raw/verified 0/0
- `http://www.nul.nagoya-u.ac.jp/eco/support/stat/stat_3-1.pdf` -> **snapshot** (snapshot 20220430163821); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/01.html` -> **snapshot** (snapshot 20260410161952); points raw/verified 0/0

### d6 [forecasts_markets] Official projections and research institute forecasts

Hypothesis: IPSS (National Institute of Population and Social Security Research) projections and private forecasts of 2026 births, combined with a July seasonal share, constrain the plausible range. Forecasts share underlying demographic assumptions, so treat as a range not independent evidence.

Queries issued by the searcher: 国立社会保障・人口問題研究所 2026 出生数 推計; 2026年 出生数 予測 日本; 人口動態統計速報 2026年6月 出生数 厚生労働省; 2024年 月別 出生数 7月 人口動態統計 月報 日本人; 国立社会保障・人口問題研究所 2026 出生数 推計; 2026年 出生数 予測 日本; 2026年 出生数 予測 エコノミスト 第一生命 ニッセイ基礎研究所 2026年 年間 出生数 見通し; 人口動態統計速報 2026年6月分 出生数 月別; 国立社会保障・人口問題研究所 2026 出生数 推計; 2026年 出生数 予測 日本; 人口動態統計速報 2026年5月 出生数 前年同月比; 日本の将来推計人口 令和5年推計 2026年 出生数 出生中位 低位

- `https://www.dlri.co.jp/report/macro/617726.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.com/zz08/n/n7fd22e86da6d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp` -> **snapshot** (snapshot 20260807022957); points raw/verified 0/0
- `https://iroiromirai.jp/wp-content/uploads/2026/03/20260331_WhitePaper2025.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://www.shugiin.go.jp/Internet/itdb_shitsumon.nsf/html/shitsumon/b216033.htm` -> **snapshot** (snapshot 20260209055049); points raw/verified 1/0
- `https://www.sankei.com./article/20260510-BY3MFI6NIJD23KXYH6EKTMQC5A/` -> **snapshot** (snapshot 20260511154028); points raw/verified 8/7
  - p172 Japan total live births, January 2026, preliminary (Ministry of Health, Labour a = **58,694** births (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p173 Japan total live births, February 2026, preliminary (Ministry of Health, Labour  = **50,761** births (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だったものの"
  - p174 Japan total live births, January-February 2026 cumulative, preliminary (Ministry = **109,455** births (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p175 Year-on-year change in Japan total live births, January 2026 vs January 2025, pr = **0.5** as written "0・5%増", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "1月の出生数は前年同月比0・5%増の5万8694人"
  - p176 Year-on-year change in Japan total live births, February 2026 vs February 2025,  = **-0.4** as written "0・4%減", value check pending % (2026-02-01..2026-02-28) [keep: ] quote: "2月は0・4%減の5万761人だったものの"
  - p177 Year-on-year change in Japan total live births, January-February 2026 cumulative = **0.1** as written "0・1%増", value check pending % (2026-01-01..2026-02-28) [keep: ] quote: "1~2月累計では0・1%増の10万9455人と依然プラス圏を維持している"
  - p178 Japan total live births, calendar year 1966 (hinoeuma year), year-on-year declin = **25** % (1966-01-01..1966-12-31) [DISCARD: 1966 hinoeuma decline; historical curiosity, no role for 2026.] quote: "60年前の1966年は出生数が前年比25%も減少した。"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/07.html` -> **snapshot** (snapshot 20260317070800); points raw/verified 0/0
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/06.html` -> **snapshot** (snapshot 20260712063920); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20260&month=12040606&tclass1=0000010` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/english/data/nenkan/75nenkan/zenbun/en75/book/pageindices/index111.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://373news.com/news/national/detail/2026110401001093/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://153.125.172.172/shisei/04gyouseizaisei/sogokeikaku/6th_kihonkoso/seisaku01202005131.files/jinnkoubijonn.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period year 2026 does not appear in the page text or URL (likely mis-dated): 1; number: no number in value_as_written: 1)

### d7 [shocks] Calendar and policy effects on July births

Hypothesis: July births depend on conceptions ~9-10 months earlier (Sept-Oct 2025), so shocks such as influenza/COVID waves, heat, holidays, or policy changes in late 2025 affect July 2026 births. Also the number of weekdays and Obon timing shift the monthly count. Quantify exposure where possible.

Queries issued by the searcher: 2025年 妊娠届 件数 減少; 婚姻届 2025年 9月 10月 件数; July 2026 calendar Japan weekdays holidays; 人口動態統計 令和8年 6月 速報 出生数; 2026年 出生数 上半期 減少 速報; 2025年 インフルエンザ 流行 ピーク 12月 感染者数 過去最多; 2025年 妊娠届 件数 減少; 婚姻届 2025年 9月 10月 婚姻件数; 人口動態統計速報 2026年 月別 出生数 厚生労働省; 2025年 出生数 月別 減少 インフルエンザ 流行 妊娠; 2025年 妊娠届 件数 減少; 婚姻届 2025年 9月 10月 件数 厚生労働省; 人口動態統計速報 令和8年 2026年 出生数 月別; 2025年 インフルエンザ 流行 早い 11月 注意報 過去最速

- `http://www.jfpa.info/boshi/archives/28/pdf/04/shiryo03.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://babytech.jp/2026/10/lunaluna-niigata-d/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.infoseek.co.jp/article/prtimes_000001236_000002943/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jiji.com/jc/article?k=000001236.000002943&g=prt%c5%8d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gendai.media/articles/-/146631?imp=0` -> **snapshot** (snapshot 20250210124807); points raw/verified 8/8
  - p179 Share of postpartum mothers developing postpartum depression (general baseline,  = **10** % (not stated (page dated 2025-02-09)) [DISCARD: Postpartum depression share — no quantitative link to July 2026 births.] quote: "出産後の母親の10%程度が「産後うつ」を発症するとされるが"
  - p180 Share of mothers with possible postpartum depression during COVID-19, University = **24** % (2020-10-01..2020-10-31) [DISCARD: Postpartum depression share — no quantitative link.] quote: "筑波大学などの調査(2020年10月)によれば、コロナ禍によって発症の可能性のある人が24%に上った。"
  - p181 Share of mothers with possible postpartum depression, another research group's s = **30** % (not stated (page dated 2025-02-09)) [DISCARD: Postpartum depression share — no quantitative link.] quote: "別の研究グループの調査結果では、約30%というものもあった。"
  - p182 Year-on-year change in 'satogaeri' birth reservations, 6 prefectures with major  = **24** % (2020-10-01..2021-03-31) [DISCARD: Satogaeri reservation change — qualitative, no quantitative link.] quote: "東京、大阪、愛知など大都市を抱える6都府県で前年同期間比約24%減"
  - p183 Year-on-year change in 'satogaeri' birth reservations, other prefectures (Oct 20 = **37** % (2020-10-01..2021-03-31) [DISCARD: Satogaeri reservation change — qualitative, no quantitative link.] quote: "それ以外の道府県では約37%も減ったのである。"
  - p184 Number of prefectures with major cities in satogaeri survey (Tokyo, Osaka, Aichi = **6** prefecture (2020-10-01..2021-03-31) [DISCARD: Prefecture count for satogaeri survey — irrelevant.] quote: "東京、大阪、愛知など大都市を抱える6都府県で前年同期間比約24%減"
  - p185 Number of main factors cited for sharp decline in pregnancy notifications and ma = **3** factor (not stated (page dated 2025-02-09)) [DISCARD: Factor count — irrelevant.] quote: "出生数の動向を左右する妊娠届け出数や婚姻件数が激減した要因は、主に3つある。"
  - p186 Copies sold of 'Mirai no Nenpyo' series (cumulative) = **1,000,000** copy (not stated (page dated 2025-02-09)) [DISCARD: Book sales — irrelevant.] quote: "100万部突破の『未来の年表』シリーズの『未来のドリル』は"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://aqua.mtk.nao.ac.jp/koyomi/yoko/2026/rekiyou261.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.timeanddate.com/holidays/japan/2026?hol=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://momclock.com/de-de/calendar/country/japan/2026/july` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://blog.livedoor.jp/jyoushiki43/archives/52201680.html` -> **snapshot** (snapshot 20251127150809); points raw/verified 10/10
  - p187 Japan live births, January-September 2025, preliminary, including foreign nation = **525,064** births (2025-01-01..2025-09-30) [keep: ] quote: "1-9月の出生数(外国人を含む速報値)は52万5064人で、前年同期比2.8%減った。"
  - p188 Year-on-year change in Japan live births, January-September 2025 vs 2024 = **2.8** % (2025-01-01..2025-09-30) [keep: ] quote: "1-9月の出生数(外国人を含む速報値)は52万5064人で、前年同期比2.8%減った。"
  - p189 Japan marriages, January-September 2025, year-on-year change = **0.4** % (2025-01-01..2025-09-30) [DISCARD: Marriage yoy change; not a birth count.] quote: "1-9月の婚姻数は前年同期比0.4%増の36万7716組だった。"
  - p190 Japan marriages, January-September 2025 = **367,716** marriages (2025-01-01..2025-09-30) [DISCARD: Marriage count; not a birth count.] quote: "1-9月の婚姻数は前年同期比0.4%増の36万7716組だった。"
  - p191 Japan marriages, July 2025, year-on-year increase in count = **10,000** marriages (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages affect ~April 2026 births, not July 2026; not usable for the target month.] quote: "7月の婚姻数が前年同月から1万組以上増え、22.5%増だったことが寄与した。"
  - p192 Japan marriages, July 2025, year-on-year percent increase = **22.5** % (2025-07-01..2025-07-31) [DISCARD: Same as p191 — wrong lag for July 2026 births.] quote: "7月の婚姻数が前年同月から1万組以上増え、22.5%増だったことが寄与した。"
  - p193 Japan deaths, January-September 2025, year-on-year change = **0.1** % (2025-01-01..2025-09-30) [DISCARD: Deaths — irrelevant to births.] quote: "1-9月の死亡数は前年同期比0.1%増の119万9567人だった。"
  - p194 Japan deaths, January-September 2025 = **1,199,567** deaths (2025-01-01..2025-09-30) [DISCARD: Deaths — irrelevant.] quote: "1-9月の死亡数は前年同期比0.1%増の119万9567人だった。"
  - p195 Japan natural change (births minus deaths), January-September 2025 = **674,503** persons (2025-01-01..2025-09-30) [DISCARD: Natural change — irrelevant to the birth count.] quote: "出生数から死亡数を差し引いた自然増減はマイナス67万4503人だった。"
  - p196 Widening of Japan natural decrease, January-September 2025 vs prior year = **15,704** persons (2025-01-01..2025-09-30) [DISCARD: Natural decrease widening — irrelevant.] quote: "マイナス幅は前年同期より1万5704人広がった。"
- `https://catalog.data.metro.tokyo.lg.jp/dataset/t131105d0000000188` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [related_series] Foreign-national share adjustment

Hypothesis: MHLW preliminary births include foreign nationals; the foreign-national share of births has been rising. If a Japan-national-only series is available, add the foreign-national component (share × total) to bridge to the target definition.

Queries issued by the searcher: 外国人 出生数 割合 日本 2025 人口動態統計; vital statistics Japan births foreign nationals share 2024; 人口動態統計速報 令和8年 2026年 出生数 外国人を含む; 令和7年 2025年 人口動態統計 概数 出生数 外国人 2万3015; 外国人 出生数 割合 日本 2025 人口動態統計; vital statistics Japan births to foreign nationals share 2024; 令和7年 人口動態統計 概数 出生数 2026年6月 公表; 人口動態統計 速報 2026年 月別 出生数 外国人 母子保健; 外国人 出生数 割合 日本 2025 厚生労働省 人口動態統計; vital statistics Japan births foreign nationals share 2024; 人口動態統計速報 令和8年 2026年 出生数 月次 厚生労働省; 外国人 出生数 2023年 令和5年 人口動態統計 1万8千人

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/gaikoku26/dl/02_r08.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://asia.nikkei.com/spotlight/japan-immigration/in-japan-babies-born-to-foreign-parents-hit-3-easing-birth-decline` -> **snapshot** (snapshot 20260825173358); points raw/verified 2/2
  - p197 Births to foreign-national parents in Japan, 2024 (count, stated as more than) = **20,000** births (2024-01-01..2024-12-31) [keep: ] quote: "More than 20,000 babies were born to foreign-national parents in Japan in 2024"
  - p198 Share of all newborns in Japan born to foreign-national parents, 2024 (stated as = **3** % (2024-01-01..2024-12-31) [keep: ] quote: "accounting for more than 3% of all newborns"
- `https://www.theguardian.com/world/2025/oct/13/record-number-babies-born-foreign-parents-japan-political-row-migration` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/gaikoku26/dl/houdou_r08.pdf` -> **snapshot** (snapshot 20260818065224); points raw/verified 10/10
  - p199 Total live births in Japan including foreign nationals, 2024 = **709,051** as written "70 万 9051", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "・出生数は、70 万 9051 人"
  - p200 Live births to foreign nationals in Japan, 2024 = **22,878** as written "2 万 2878", value check pending births (2024-01-01..2024-12-31) [keep: ] quote: "うち日本における外国人は 2 万 2878 人で 3.2%"
  - p201 Share of live births to foreign nationals in Japan, 2024 = **3.2** % (2024-01-01..2024-12-31) [keep: ] quote: "うち日本における外国人は 2 万 2878 人で 3.2%"
  - p202 Increase in foreign-national birth share, 2024 vs 2014 = **1.8** percentage points (2024-01-01..2024-12-31) [DISCARD: Change in foreign share; redundant with p201.] quote: "3.2% (10 年前※と比べ 1.8 ポイント増)"
  - p203 Total deaths in Japan including foreign nationals, 2024 = **1,614,706** as written "161 万 4706", value check pending deaths (2024-01-01..2024-12-31) [DISCARD: Deaths — irrelevant.] quote: "・死亡数は、161 万 4706 人"
  - p204 Deaths of foreign nationals in Japan, 2024 = **9,328** deaths (2024-01-01..2024-12-31) [DISCARD: Foreign deaths — irrelevant.] quote: "うち日本における外国人は 9328 人で 0.6%"
  - p205 Share of deaths to foreign nationals in Japan, 2024 = **0.6** % (2024-01-01..2024-12-31) [DISCARD: Foreign death share — irrelevant.] quote: "うち日本における外国人は 9328 人で 0.6%"
  - p206 Total marriages in Japan including foreign nationals, 2024 = **490,171** as written "49 万 171", value check pending marriages (2024-01-01..2024-12-31) [DISCARD: Marriages — irrelevant to July 2026 births.] quote: "・婚姻件数は、49 万 171 組"
  - p207 Marriages involving foreign nationals in Japan, 2024 = **5,079** marriages (2024-01-01..2024-12-31) [DISCARD: Foreign marriages — irrelevant.] quote: "うち日本における外国人は 5079 組で 1.0%"
  - p208 Share of marriages involving foreign nationals in Japan, 2024 = **1** % (2024-01-01..2024-12-31) [DISCARD: Foreign marriage share — irrelevant.] quote: "うち日本における外国人は 5079 組で 1.0%"
- `https://www.e-stat.go.jp/stat-search/database?page=1&query=%E5%87%BA%E7%94%9F%E6%95%B0%20%E5%A4%96%E5%9B%BD%E4%BA%BA&layout=dataset&statdisp_id=000341` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www3.nhk.or.jp/nhkworld/zt/news/nd-20261026de66022/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nikkei.com/article/DGXZQOFM104SG0Q5A011C2000000/` -> **snapshot** (snapshot 20251010133634); points raw/verified 3/3
  - p209 Foreign-national births in Japan in 2024 (count, first time at this level) = **20,000** births (2024-01-01..2024-12-31) [keep: ] quote: "日本で2024年に生まれた外国人が2万人に達し、新生児に占める割合が3%を超えた。"
  - p210 Share of foreign-national births among newborns in Japan in 2024 (foreign-nation = **3** % (2024-01-01..2024-12-31) [keep: ] quote: "日本で2024年に生まれた外国人が2万人に達し、新生児に占める割合が3%を超えた。"
  - p211 Share of resident foreigners in Japan's total population (resident foreigners /  = **3** % (not stated (page dated 2025-10-10)) [DISCARD: Resident-foreigner population share — not a birth quantity; redundant with p201 for the birth bridge.] quote: "働き手世代を中心に在留外国人は総人口の約3%まで増えてきたが、出生段階でも日本の低出生数をある程度補う新たなステージに入った。"
- `https://www.jiji.com/jc/article?k=2026080700822&g=soc&m=rss` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040456883&fileKind=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/ja/articles/-/54325` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.psrn.jp/topics/detail.php?id=42487` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] MHLW preliminary monthly vital statistics

Hypothesis: A June 2026 preliminary birth count (published ~August 2026) would give the most recent month before July and let a June-to-July seasonal ratio (from p65/p64) anchor July 2026 directly, tightening the estimate materially.

Queries issued by the searcher: MHLW 人口動態統計速報 令和8年6月 出生数; www.mhlw.go.jp 人口動態統計 2026年6月 速報 出生数; 人口動態統計速報 令和8年5月分 出生数 厚生労働省 2026年7月公表; 人口動態統計速報 令和7年7月分 出生数 2025年 月別 出生数 6月 7月; MHLW 人口動態統計速報 令和8年6月 出生数; www.mhlw.go.jp 人口動態統計 2026年6月 速報 出生数; 人口動態統計速報 令和8年6月分 202606.pdf 出生数 速報; 人口動態統計速報 令和8年5月分 出生数 2026年5月; 人口動態統計速報 令和8年6月 出生数; www.mhlw.go.jp 人口動態統計 2026年6月 速報 出生数; 人口動態統計速報 令和7年7月分 出生数 速報値; 人口動態統計速報 令和8年6月分 出生数 6万 速報 202606.pdf

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nippon.com/en/articles/-/54326` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sp.m.jiji.com/article/show/3854705` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.psrn.jp/topics/detail.php?id=43415` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 29/29
  - p212 Japan total live births, May 2026 preliminary (monthly, all nationalities incl.  = **59,663** as written "59 663", value check pending birth (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p213 Japan total live births, May 2025 preliminary (monthly, comparison year) = **60,718** as written "60 718", value check pending birth (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p214 Year-on-year change in Japan total live births, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending birth (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p215 Year-on-year percent change in Japan total live births, May 2026 = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p216 Japan annualised birth rate (per 1,000 population), May 2026 = **5.7** birth/(1000 person*year) (2026-05-01..2026-05-31) [DISCARD: Birth rate per 1,000; redundant with p94/p212.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p217 Japan annualised birth rate (per 1,000 population), May 2025 = **5.8** birth/(1000 person*year) (2025-05-01..2025-05-31) [DISCARD: Birth rate per 1,000; redundant with p95/p213.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p218 Japan cumulative live births, January–May 2026 preliminary = **282,222** as written "282 222", value check pending birth (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p219 Japan cumulative live births, January–May 2025 preliminary = **280,979** as written "280 979", value check pending birth (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p220 Year-on-year change in Japan cumulative live births, Jan–May 2026 vs 2025 = **1,243** as written "1 243", value check pending birth (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p221 Year-on-year percent change in Japan cumulative live births, Jan–May 2026 = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p222 Japan cumulative annualised birth rate (per 1,000 population), Jan–May 2026 = **5.6** birth/(1000 person*year) (2026-01-01..2026-05-31) [DISCARD: Cumulative birth rate; redundant with p98/p218.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p223 Japan cumulative annualised birth rate (per 1,000 population), Jan–May 2025 = **5.5** birth/(1000 person*year) (2025-01-01..2025-05-31) [DISCARD: Cumulative birth rate; redundant with p99/p219.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p224 Japan live births, trailing 12 months June 2025–May 2026 preliminary = **707,052** as written "707 052", value check pending birth (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p225 Japan live births, trailing 12 months June 2024–May 2025 preliminary = **709,893** as written "709 893", value check pending birth (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p226 Year-on-year change in Japan trailing-12-month live births = **-2,841** as written "△ 2 841", value check pending birth (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p227 Japan trailing-12-month annualised birth rate (per 1,000 population), June 2025– = **5.7** birth/(1000 person*year) (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p228 Japan total deaths, May 2026 preliminary (monthly) = **122,385** as written "122 385", value check pending death (2026-05-01..2026-05-31) [DISCARD: Deaths; irrelevant to births.] quote: "死 亡 122 385 124 572 △ 2 187 △ 1.8 11.7 11.9 98.7"
  - p229 Japan natural decrease, May 2026 preliminary (births minus deaths) = **-62,722** as written "△ 62 722", value check pending person (2026-05-01..2026-05-31) [DISCARD: Natural decrease; irrelevant.] quote: "自 然 増 減 △ 62 722 △ 63 854 1 132 ... △ 6.0 △ 6.1 ..."
  - p230 Japan cumulative natural decrease, Jan–May 2026 preliminary = **-382,288** as written "△ 382 288", value check pending person (2026-01-01..2026-05-31) [DISCARD: Cumulative natural decrease; irrelevant.] quote: "自 然 増 減 △ 382 288 △ 440 059 57 771 ... △ 7.5 △ 8.6 ..."
  - p231 Japan cumulative deaths, Jan–May 2026 preliminary = **664,510** as written "664 510", value check pending death (2026-01-01..2026-05-31) [DISCARD: Cumulative deaths; irrelevant.] quote: "死 亡 664 510 721 038 △ 56 528 △ 7.8 13.1 14.1 92.6"
  - p232 Japan stillbirths, May 2026 preliminary (monthly) = **1,318** as written "1 318", value check pending stillbirth (2026-05-01..2026-05-31) [DISCARD: Stillbirths; not live births.] quote: "死 産 1 318 1 392 △ 74 △ 5.3 21.6 22.4 96.4"
  - p233 Japan stillbirth rate per 1,000 deliveries (births + stillbirths), May 2026 = **21.6** stillbirth/(1000 birth) (2026-05-01..2026-05-31) [DISCARD: Stillbirth rate; irrelevant.] quote: "死 産 1 318 1 392 △ 74 △ 5.3 21.6 22.4 96.4"
  - p234 Japan marriages, May 2026 preliminary (monthly) = **41,169** as written "41 169", value check pending marriage (2026-05-01..2026-05-31) [DISCARD: Marriages; not a birth count.] quote: "婚 姻 41 169 43 257 △ 2 088 △ 4.8 3.9 4.1 95.6"
  - p235 Japan cumulative marriages, Jan–May 2026 preliminary = **206,971** as written "206 971", value check pending marriage (2026-01-01..2026-05-31) [DISCARD: Cumulative marriages; not a birth count.] quote: "婚 姻 206 971 206 142 829 0.4 4.1 4.0 100.9"
  - p236 Japan trailing-12-month marriages, June 2025–May 2026 preliminary = **506,485** as written "506 485", value check pending marriage (2025-06-01..2026-05-31) [DISCARD: Trailing marriages; not a birth count.] quote: "婚 姻 506 485 490 791 15 694 3.2 4.1 4.0 103.7"
  - p237 Japan divorces, May 2026 preliminary (monthly) = **13,449** as written "13 449", value check pending divorce (2026-05-01..2026-05-31) [DISCARD: Divorces; irrelevant.] quote: "離 婚 13 449 14 407 △ 958 △ 6.6 1.29 1.38 93.8"
  - p238 Japan cumulative stillbirths, Jan–May 2026 preliminary = **6,700** as written "6 700", value check pending stillbirth (2026-01-01..2026-05-31) [DISCARD: Cumulative stillbirths; irrelevant.] quote: "死 産 6 700 6 763 △ 63 △ 0.9 23.2 23.5 98.7"
  - p239 Japan trailing-12-month stillbirths, June 2025–May 2026 preliminary = **16,038** as written "16 038", value check pending stillbirth (2025-06-01..2026-05-31) [DISCARD: Trailing stillbirths; irrelevant.] quote: "死 産 16 038 16 025 13 0.1 22.2 22.1 100.5"
  - p240 Japan cumulative divorces, Jan–May 2026 preliminary = **75,656** as written "75 656", value check pending divorce (2026-01-01..2026-05-31) [DISCARD: Cumulative divorces; irrelevant.] quote: "離 婚 75 656 78 870 △ 3 214 △ 4.1 1.49 1.54 96.4"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 2/2
  - p241 MHLW vital statistics preliminary report reference month (Reiwa 8 / 2026 May edi = **5** month (calendar month of reference, May 2026) (2026-05-01..2026-05-31) [DISCARD: Reference month of the report; metadata, no numerical role.] quote: "人口動態統計速報(令和8(2026)年5月分)"
  - p242 Publication date of MHLW preliminary vital statistics report for May 2026 = **24** day of month (publication date, 2026-07-24) (2026-07-24..2026-07-24) [DISCARD: Publication date; metadata, no numerical role.] quote: "令和8年7月24日"
- `https://www.e-stat.go.jp/index.php/stat-search/files?page=1&layout=dataset&iroha=46&toukei=00450011&stat_infid=000040477217` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] conception-side signal

Hypothesis: Pregnancy notifications (妊娠届) for Sep-Oct 2025, or 2025 monthly marriage counts, would constrain the conception cohort behind July 2026 births and resolve whether the recent flat/positive yoy trend (p100) persists into July.

Queries issued by the searcher: 妊娠届 2025年 月別 全国 集計 厚生労働省; 妊娠届出数 2025年9月 10月 集計; 厚生労働省 妊娠届出数の状況について 令和7年 月別 全国; 人口動態統計速報 令和8年 出生数 婚姻数 2026年; 妊娠届 2025年 集計 厚生労働省 妊娠届出数; 2025年 婚姻件数 月別 厚生労働省 人口動態統計; 妊娠届出数 2025年9月 東京都 月別; 人口動態統計速報 2026年 出生数 月別 前年比; 妊娠届 2025年9月 10月 全国 集計; 厚生労働省 妊娠届出数 2025; 妊娠届出数 令和7年 月別 厚生労働省 2025年 減少; 2026年 出生数 速報 6月 前年比 増加 人口動態統計

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2025/dl/202503.pdf` -> **snapshot** (snapshot 20260320012912); points raw/verified 29/29
  - p243 National live births, Japan, March 2025 (preliminary vital statistics, all event = **53,619** as written "53 619", value check pending birth (2025-03-01..2025-03-31) [DISCARD: March 2025 births from a different vintage (53,619) conflicting with p71 (50,767); using both would corrupt the monthly ] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p244 National live births, Japan, March 2024 (preliminary, prior year comparison) = **55,198** as written "55 198", value check pending birth (2024-03-01..2024-03-31) [DISCARD: March 2024 comparison value from the same conflicting vintage.] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p245 Year-on-year change in national live births, Japan, March 2025 vs March 2024 = **-1,579** as written "△ 1 579", value check pending birth (2025-03-01..2025-03-31) [DISCARD: March 2025 yoy change from the conflicting vintage.] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p246 Year-on-year percent change in national live births, Japan, March 2025 = **2.9** % (2025-03-01..2025-03-31) [DISCARD: March 2025 yoy percent from the conflicting vintage.] quote: "出 生 53 619 55 198 △ 1 579 △ 2.9 5.1 5.3 97.3"
  - p247 National marriage counts, Japan, March 2025 (preliminary) = **55,762** as written "55 762", value check pending marriage (2025-03-01..2025-03-31) [DISCARD: March 2025 marriages; not a birth count.] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p248 National marriage counts, Japan, March 2024 (preliminary, prior year comparison) = **56,864** as written "56 864", value check pending marriage (2024-03-01..2024-03-31) [DISCARD: March 2024 marriages; not a birth count.] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p249 Year-on-year change in national marriage counts, Japan, March 2025 = **-1,102** as written "△ 1 102", value check pending marriage (2025-03-01..2025-03-31) [DISCARD: Marriage change; irrelevant.] quote: "婚 姻 55 762 56 864 △ 1 102 △ 1.9 5.3 5.4 98.2"
  - p250 National live births, Japan, cumulative January-March 2025 (preliminary) = **162,955** as written "162 955", value check pending birth (2025-01-01..2025-03-31) [DISCARD: Jan-Mar 2025 cumulative from the conflicting vintage; redundant with p73/p99.] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p251 National live births, Japan, cumulative January-March 2024 (preliminary, prior y = **170,804** as written "170 804", value check pending birth (2024-01-01..2024-03-31) [DISCARD: Jan-Mar 2024 cumulative from the conflicting vintage.] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p252 Year-on-year percent change in national live births, Japan, cumulative January-M = **4.6** % (2025-01-01..2025-03-31) [DISCARD: Jan-Mar 2025 yoy percent; redundant.] quote: "出 生 162 955 170 804 △ 7 849 △ 4.6 5.4 5.5 96.6"
  - p253 National marriage counts, Japan, cumulative January-March 2025 (preliminary) = **131,332** as written "131 332", value check pending marriage (2025-01-01..2025-03-31) [DISCARD: Cumulative marriages; irrelevant.] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p254 National marriage counts, Japan, cumulative January-March 2024 (preliminary, pri = **136,653** as written "136 653", value check pending marriage (2024-01-01..2024-03-31) [DISCARD: Cumulative marriages; irrelevant.] quote: "婚 姻 131 332 136 653 △ 5 321 △ 3.9 4.3 4.4 97.3"
  - p255 National live births, Japan, trailing 12 months April 2024-March 2025 (prelimina = **713,139** as written "713 139", value check pending birth (2024-04-01..2025-03-31) [DISCARD: Trailing 12 months to March 2025 from the conflicting vintage; redundant with p102/p225.] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p256 National live births, Japan, trailing 12 months April 2023-March 2024 (prelimina = **746,958** as written "746 958", value check pending birth (2023-04-01..2024-03-31) [DISCARD: Trailing 12 months to March 2024 from the conflicting vintage.] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p257 Year-on-year percent change in national live births, Japan, trailing 12 months t = **4.5** % (2024-04-01..2025-03-31) [DISCARD: Trailing yoy percent; redundant.] quote: "出 生 713 139 746 958 △ 33 819 △ 4.5 5.8 6.0 95.9"
  - p258 National marriage counts, Japan, trailing 12 months April 2024-March 2025 (preli = **494,678** as written "494 678", value check pending marriage (2024-04-01..2025-03-31) [DISCARD: Trailing marriages; irrelevant.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p259 National marriage counts, Japan, trailing 12 months April 2023-March 2024 (preli = **491,082** as written "491 082", value check pending marriage (2023-04-01..2024-03-31) [DISCARD: Trailing marriages; irrelevant.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p260 Year-on-year change in national marriage counts, Japan, trailing 12 months to Ma = **3,596** as written "3 596", value check pending marriage (2024-04-01..2025-03-31) [DISCARD: Marriage change; irrelevant.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p261 Year-on-year percent change in national marriage counts, Japan, trailing 12 mont = **0.7** % (2024-04-01..2025-03-31) [DISCARD: Marriage percent change; irrelevant.] quote: "婚 姻 494 678 491 082 3 596 0.7 4.0 3.9 101.2"
  - p262 National live births, Japan, March 2025, by prefecture of notification (national = **53,619** as written "53 619", value check pending birth (2025-03-01..2025-03-31) [DISCARD: March 2025 national births from the conflicting vintage (53,619).] quote: "全 国 53 619 145 215 1 351 55 762 19 692"
  - p263 National marriage counts, Japan, March 2025, by prefecture of notification (nati = **55,762** as written "55 762", value check pending marriage (2025-03-01..2025-03-31) [DISCARD: March 2025 marriages; irrelevant.] quote: "全 国 53 619 145 215 1 351 55 762 19 692"
  - p264 Tokyo Metropolis live births, March 2025 (by notification place) = **6,406** as written "6 406", value check pending birth (2025-03-01..2025-03-31) [DISCARD: Tokyo March 2025 births; sub-national.] quote: "13 東 京 6 406 12 592 180 8 843 2 104"
  - p265 Tokyo Metropolis marriage counts, March 2025 (by notification place) = **8,843** as written "8 843", value check pending marriage (2025-03-01..2025-03-31) [DISCARD: Tokyo marriages; irrelevant.] quote: "13 東 京 6 406 12 592 180 8 843 2 104"
  - p266 National live births, Japan, cumulative January-March 2025, by prefecture of not = **162,955** as written "162 955", value check pending birth (2025-01-01..2025-03-31) [DISCARD: Jan-Mar 2025 national births from the conflicting vintage.] quote: "全 国 162 955 466 672 3 979 131 332 48 685"
  - p267 National marriage counts, Japan, cumulative January-March 2025, by prefecture of = **131,332** as written "131 332", value check pending marriage (2025-01-01..2025-03-31) [DISCARD: Cumulative marriages; irrelevant.] quote: "全 国 162 955 466 672 3 979 131 332 48 685"
  - p268 Tokyo Metropolis live births, cumulative January-March 2025 (by notification pla = **19,550** as written "19 550", value check pending birth (2025-01-01..2025-03-31) [DISCARD: Tokyo cumulative births; sub-national.] quote: "13 東 京 19 550 40 339 516 21 520 5 375"
  - p269 Tokyo Metropolis marriage counts, cumulative January-March 2025 (by notification = **21,520** as written "21 520", value check pending marriage (2025-01-01..2025-03-31) [DISCARD: Tokyo cumulative marriages; irrelevant.] quote: "13 東 京 19 550 40 339 516 21 520 5 375"
  - p270 National stillbirths (fetal deaths), Japan, March 2025 (preliminary) = **1,351** as written "1 351", value check pending stillbirth (2025-03-01..2025-03-31) [DISCARD: Stillbirths; irrelevant.] quote: "死 産 1 351 1 438 △ 87 △ 6.1 24.6 25.4 96.8"
  - p271 National stillbirth rate per 1,000 births plus stillbirths, Japan, March 2025 (a = **24.6** stillbirth per 1,000 (birth + stillbirth) (2025-03-01..2025-03-31) [DISCARD: Stillbirth rate; irrelevant.] quote: "死 産 1 351 1 438 △ 87 △ 6.1 24.6 25.4 96.8"
- `https://x.com/Ftf4gzRaQI8nOqj/status/2087470161150550328` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.jfpa.info/boshi/archives/28/pdf/04/shiryo03.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_06.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.pref.mie.lg.jp/common/content/000987076.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/dl/toukeihyo_05.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/2012/121011/201201015B/201201015B0006.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/stf/newpage_18837.html` -> **snapshot** (snapshot 20260317031932); points raw/verified 17/12
  - p272 Pregnancy notifications, Japan, November 2020 (Reiwa 2) = **69,804** pregnancy notification (2020-11-01..2020-11-30) [DISCARD: Pregnancy notifications from 2020; far too old to constrain the Sep-Oct 2025 conception cohort.] quote: "令和2年11 月の妊娠届け出数は69,804 件であり、前年同月の73,348 件と比較すると4.8%減。"
  - p273 Year-on-year change in pregnancy notifications, Japan, November 2020 = **4.8** % (2020-11-01..2020-11-30) [DISCARD: 2020 pregnancy-notification change; too old.] quote: "令和2年11 月の妊娠届け出数は69,804 件であり、前年同月の73,348 件と比較すると4.8%減。"
  - p274 Pregnancy notifications, Japan, December 2020 (Reiwa 2) = **75,755** pregnancy notification (2020-12-01..2020-12-31) [DISCARD: 2020 pregnancy notifications; too old.] quote: "令和2年12 月の妊娠届け出数は75,755 件であり、前年同月の77,165 件と比較すると1.8%減。"
  - p275 Year-on-year change in pregnancy notifications, Japan, December 2020 = **1.8** % (2020-12-01..2020-12-31) [DISCARD: 2020 pregnancy-notification change; too old.] quote: "令和2年12 月の妊娠届け出数は75,755 件であり、前年同月の77,165 件と比較すると1.8%減。"
  - p276 Pregnancy notifications, Japan, January 2021 (Reiwa 3) = **76,985** pregnancy notification (2021-01-01..2021-01-31) [DISCARD: 2021 pregnancy notifications; too old.] quote: "令和3年1月の妊娠届け出数は76,985 件であり、前年同月の82,835 件と比較すると7.1%減。"
  - p277 Pregnancy notifications, Japan, January 2020 (same month previous year) = **82,835** pregnancy notification (2020-01-01..2020-01-31) [DISCARD: 2020 pregnancy notifications; too old.] quote: "令和3年1月の妊娠届け出数は76,985 件であり、前年同月の82,835 件と比較すると7.1%減。"
  - p278 Year-on-year change in pregnancy notifications, Japan, January 2021 = **7.1** % (2021-01-01..2021-01-31) [DISCARD: 2021 pregnancy-notification change; too old.] quote: "令和3年1月の妊娠届け出数は76,985 件であり、前年同月の82,835 件と比較すると7.1%減。"
  - p279 Cumulative pregnancy notifications, Japan, January-December 2020 (Reiwa 2) = **872,227** pregnancy notification (2020-01-01..2020-12-31) [DISCARD: 2020 cumulative pregnancy notifications; too old.] quote: "また、令和2年1-12 月の累計妊娠届出数は872,227 件であり、前年同期間の916,590 件と比較すると4.8%減でした。"
  - p280 Year-on-year change in cumulative pregnancy notifications, Japan, January-Decemb = **4.8** % (2020-01-01..2020-12-31) [DISCARD: 2020 cumulative change; too old.] quote: "また、令和2年1-12 月の累計妊娠届出数は872,227 件であり、前年同期間の916,590 件と比較すると4.8%減でした。"
  - p281 Year-on-year change in pregnancy notifications, Japan, FY2015 = **2.1** % (2015-04-01..2016-03-31) [DISCARD: FY2015 pregnancy-notification change; too old.] quote: "平成27 年度 2.1%減、平成28 年度 4.2%減、平成29 年度 2.3%減、平成30 年度 5.3%減"
  - p282 Year-on-year change in pregnancy notifications, Japan, FY2016 = **4.2** % (2016-04-01..2017-03-31) [DISCARD: FY2016 pregnancy-notification change; too old.] quote: "平成27 年度 2.1%減、平成28 年度 4.2%減、平成29 年度 2.3%減、平成30 年度 5.3%減"
  - p283 Year-on-year change in pregnancy notifications, Japan, FY2017 = **2.3** % (2017-04-01..2018-03-31) [DISCARD: FY2017 pregnancy-notification change; too old.] quote: "平成27 年度 2.1%減、平成28 年度 4.2%減、平成29 年度 2.3%減、平成30 年度 5.3%減"
- `https://www.mhlw.go.jp/toukei/saikin/hw/c-hoken/22/index.html` -> **snapshot** (snapshot 20260416151825); points raw/verified 0/0
- `http://search.ckan.jp/datasets/data.bodik.jp__dataset:232114_maternal_and_child_health_handbook` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pref.saitama.lg.jp/documents/265654/shiryo1.pdf` -> **snapshot** (snapshot 20250913195709); points raw/verified 29/29
  - p284 Total pregnancy notifications (妊娠届出数), all municipalities in Saitama prefecture, = **44,414** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 3,574 815 259 63 7 35 27 1,275 61 68 24 44 21 875 0"
  - p285 Total pregnancy notifications, all municipalities excluding Saitama/Kawagoe/Kosh = **26,442** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "26,442 2,053 316 172 30 1 22 17 843 42 45 16 39 17 493 0"
  - p286 Pregnancy notifications reported within 11 weeks gestation (第3月以内), all municipa = **41,991** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p287 Pregnancy notifications reported at 12-19 weeks gestation (第4月～5月以内), all munici = **1,745** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p288 Pregnancy notifications reported at 20-27 weeks gestation (第6月～7月以内), all munici = **254** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p289 Pregnancy notifications reported at 28 weeks to delivery (第8月～分娩まで), all municip = **126** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p290 Pregnancy notifications reported post-delivery (分娩後), all municipalities total = **204** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p291 Pregnancy notifications with unknown reporting week (不詳), all municipalities tot = **94** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama pregnancy notifications; sub-national and undated.] quote: "44,414 41,991 1,745 254 126 204 94"
  - p292 Pregnancy notifications, Saitama city (さいたま市), cumulative total = **9,688** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Saitama city pregnancy notifications; sub-national and undated.] quote: "さいたま市 さいたま市 9,688 546 139 31 13 6 7 5 139 6 13 6 3 4 174 0"
  - p293 Pregnancy notifications, Kawaguchi city (川口市), cumulative total = **4,168** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kawaguchi pregnancy notifications; sub-national and undated.] quote: "川口市 川口市 4,168 710 313 32 15 0 5 3 182 12 1 0 1 0 146 0"
  - p294 Pregnancy notifications, Koshigaya city (越谷市), cumulative total = **2,127** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Koshigaya pregnancy notifications; sub-national and undated.] quote: "越谷市 越谷市 2,127 137 28 16 5 0 0 1 44 1 7 2 0 0 33 0"
  - p295 Pregnancy notifications, Kawagoe city (川越市), cumulative total = **1,989** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kawagoe pregnancy notifications; sub-national and undated.] quote: "川越市 川 越 市 1,989 128 19 8 0 0 1 1 67 0 2 0 1 0 29 0"
  - p296 Pregnancy notifications, Asaka city (朝霞市), cumulative total = **1,165** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Asaka pregnancy notifications; sub-national and undated.] quote: "朝 霞 市 1,165 88 14 4 2 0 1 0 40 1 0 0 1 0 25 0"
  - p297 Pregnancy notifications, Kasukabe city (春日部市), cumulative total = **1,165** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kasukabe pregnancy notifications; sub-national and undated.] quote: "春日部市 1,165 99 11 10 0 0 0 2 40 0 10 1 1 0 24 0"
  - p298 Pregnancy notifications, Kumagaya city (熊谷市), cumulative total = **1,043** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kumagaya pregnancy notifications; sub-national and undated.] quote: "熊 谷 市 1,043 50 4 2 2 0 1 0 22 0 0 0 1 1 17 0"
  - p299 Pregnancy notifications, Koshigaya health centre jurisdiction (南部), cumulative t = **4,899** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Koshigaya health-centre notifications; sub-national and undated.] quote: "4,899 345 70 21 6 0 8 5 123 8 6 4 1 0 93 0"
  - p300 Pregnancy notifications, Kawagoe health centre jurisdiction (坂戸), cumulative tot = **995** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kawagoe health-centre notifications; sub-national and undated.] quote: "995 87 4 5 0 0 1 0 54 0 1 1 2 0 19 0"
  - p301 Pregnancy notifications, Higashimatsuyama health centre jurisdiction (東松山), cumu = **966** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Higashimatsuyama notifications; sub-national and undated.] quote: "966 85 5 7 0 0 1 0 39 3 0 3 7 3 17 0"
  - p302 Pregnancy notifications, Chichibu health centre jurisdiction (秩父), cumulative to = **309** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Chichibu notifications; sub-national and undated.] quote: "309 10 0 2 0 0 0 1 7 0 0 0 0 0 0 0"
  - p303 Pregnancy notifications, Honjo health centre jurisdiction (本庄), cumulative total = **668** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Honjo notifications; sub-national and undated.] quote: "668 64 2 6 0 0 1 0 41 2 1 0 7 1 3 0"
  - p304 Pregnancy notifications, Kasukabe health centre jurisdiction (加須), cumulative to = **1,211** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kasukabe health-centre notifications; sub-national and undated.] quote: "1,211 141 5 15 0 0 0 2 50 2 7 0 10 5 45 0"
  - p305 Pregnancy notifications, Soka health centre jurisdiction (草加), cumulative total = **3,596** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Soka notifications; sub-national and undated.] quote: "3,596 348 55 33 10 0 5 2 133 6 14 0 0 1 89 0"
  - p306 Pregnancy notifications, Kuki health centre jurisdiction (幸手), cumulative total = **1,942** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Kuki notifications; sub-national and undated.] quote: "1,942 118 9 17 0 0 1 1 55 3 4 1 1 0 26 0"
  - p307 Pregnancy notifications, Wako city (和光市), cumulative total = **693** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Wako notifications; sub-national and undated.] quote: "和 光 市 693 39 7 0 1 0 4 0 6 3 1 0 0 0 17 0"
  - p308 Pregnancy notifications, Niiza city (新座市), cumulative total = **982** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Niiza notifications; sub-national and undated.] quote: "新 座 市 982 85 19 8 2 0 2 3 27 1 1 4 0 0 18 0"
  - p309 Pregnancy notifications, Fujimi city (富士見市), cumulative total = **786** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Fujimi notifications; sub-national and undated.] quote: "富士見市 786 53 10 6 0 0 1 0 17 1 1 0 0 0 17 0"
  - p310 Pregnancy notifications, Fujimino city (ふじみ野市), cumulative total = **631** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Fujimino notifications; sub-national and undated.] quote: "ふじみ野市 631 34 9 1 1 0 0 1 12 0 2 0 0 0 8 0"
  - p311 Pregnancy notifications, Warabi city (蕨市), cumulative total = **521** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Warabi notifications; sub-national and undated.] quote: "蕨 市 521 115 59 1 0 0 0 0 29 0 0 0 0 0 26 0"
  - p312 Pregnancy notifications, Toda city (戸田市), cumulative total = **1,170** pregnancy notification (not stated (page dated 2025-03-27)) [DISCARD: Toda notifications; sub-national and undated.] quote: "戸 田 市 1,170 120 39 3 3 1 2 1 43 1 0 0 0 0 27 0"
- `https://www.city.yokote.lg.jp/_res/projects/default_project/_page_/001/006/551/r8hokenjigyounogaiyou.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period year 2019 does not appear in the page text or URL (likely mis-dated): 5)

### b3 [related_series] foreign-national birth share

Hypothesis: A 2025 or early-2026 foreign-national birth share (updating p201's 3.2% for 2024) would refine the bridge from the Japanese-national series to the total-incl-foreigners target, which is the main definitional gap.

Queries issued by the searcher: 2025年 外国人 出生数 割合 厚生労働省; 日本 外国人 出生 2025 3.2% 割合; 人口動態統計速報 令和8年 2026年 出生数 月別 厚生労働省; 2025年 外国人出生数 2万3千人 割合 速報 2026年 厚生労働省 人口動態統計; 2025年 外国人 出生数 割合 厚生労働省; 日本 外国人 出生 2025 3.2% 割合; 2025年 人口動態統計速報 出生数 70万5809人 外国人 割合; 厚生労働省 人口動態統計速報 2026年6月 出生数 外国人; 2025年 外国人 出生数 割合 厚生労働省; 日本 外国人 出生 2025 3.2%; 厚生労働省 人口動態統計 2025年 外国人 出生数; 令和7年 人口動態統計 速報 2025 出生数 705809 外国人; 2025年 外国人 出生数 23015 厚生労働省 2026; site:mhlw.go.jp 人口動態統計速報 令和8年6月 出生数; 2026年6月 人口動態統計 速報 出生数 外国人

- `https://roushikyo-digital.com/news/20125/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.on.cc/hk/bkn/cnt/intnews/20251014/bkn-20251014141515336-1014_00992_001_cn.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sankei.com/article/20251019-6JEMISXGDZORBLWICIFFQ7YABU/` -> **snapshot** (snapshot 20251207144544); points raw/verified 4/4
  - p313 Foreign residents in Japan at end of June 2025 (Immigration Services Agency), ye = **5** as written "5・0%", value check pending % (2025-06-30..2025-06-30) [DISCARD: Foreign-resident growth rate; not a birth count.] quote: "6月末現在の在留外国人数が昨年末より5・0%増の395万6619人となり、過去最多を更新した。"
  - p314 Foreign residents in Japan at end of June 2025 (Immigration Services Agency), to = **3,956,619** person (2025-06-30..2025-06-30) [DISCARD: Foreign-resident stock; not a birth count.] quote: "6月末現在の在留外国人数が昨年末より5・0%増の395万6619人となり、過去最多を更新した。"
  - p315 Share of Japan's total population that is foreign residents, end of June 2025 = **3.2** as written "3・2%", value check pending % (2025-06-30..2025-06-30) [DISCARD: Foreign-resident share of population; not a birth share.] quote: "日本の総人口に占める割合は3・2%となった。"
  - p316 Projected foreign residents in Japan at end of 2025 (author's simple extrapolati = **4,150,000** person (2025-12-31..2025-12-31) [DISCARD: Author's extrapolation of foreign residents; not a birth count.] quote: "単純計算すれば、2025年末には415万人ほどとなる。"
- `https://www3.nhk.or.jp/nhkworld/zt/news/nd-20261026de66022/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asahi.com/articles/ASV2T4HGHV2TUTFL01ZM.html` -> **snapshot** (snapshot 20260723062755); points raw/verified 12/6
  - p317 Live births in Japan in 2025 including foreign nationals born in Japan and Japan = **705,809** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年に生まれた子どもの数は、日本で生まれた外国人や外国で生まれた日本人など含めて前年比2.1%減の70万5809人となり"
  - p318 Year-on-year decrease rate of total births (incl. foreigners) in 2025 = **2.1** % (2025-01-01..2025-12-31) [keep: ] quote: "前年比2.1%減の70万5809人となり、10年連続で過去最少を更新した"
  - p319 Consecutive years of declining births (incl. foreigners) through 2025 = **10** years (2016-01-01..2025-12-31) [DISCARD: Consecutive declining years; irrelevant.] quote: "10年連続で過去最少を更新した"
  - p320 Natural decrease (births minus deaths) in 2025, record high = **899,845** persons (2025-01-01..2025-12-31) [DISCARD: Natural decrease; not a birth count.] quote: "出生数から死亡数を引いた「自然減」は89万9845人で過去最多となった"
  - p321 Number of marriages in 2025, year-on-year change = **505,656** couples (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数が、前年より1.1%増えて50万5656組となり、2年連続の増加となった"
  - p322 Year-on-year increase rate of marriages in 2025 = **1.1** % (2025-01-01..2025-12-31) [keep: ] quote: "婚姻数が、前年より1.1%増えて50万5656組となり、2年連続の増加となった"
- `http://www.jnocnews.co.jp/n162902.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www3.nhk.or.jp/nhkworld/pt/news/20261027_RS13/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://russiajapansociety.ru/?p=86395` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202608.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.projectdesign.jp/articles/news/622644f6-9462-48a6-976b-b8dd511ec5e3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://blog.livedoor.jp/yumesakiannaininn/archives/51659418.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period year 2017 does not appear in the page text or URL (likely mis-dated): 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1; number: scale conflict: '千' in value vs '万': 3; period year 2042 does not appear in the page text or URL (likely mis-dated): 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan births', 'july 2026 births', 'vital statistics']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] Monthly 2025 preliminary births from one secondary summary (hoikusys) of MHLW data; internally consistent with the stated year-on-year decreases p5-p8 and cumulative p9. However these values (58,385 f
- corroborating: ['p69', 'p70', 'p71', 'p72', 'p73', 'p74'] MHLW preliminary monthly births Jan-Apr 2025 and cumulative Jan-Apr 2024/2025, internally consistent (sum of p69-p72 = p73). This is the authoritative definitional series for the target (total births 
- corroborating: ['p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p108', 'p109', 'p110'] MHLW preliminary vital statistics snapshot 2026-07-24: May 2026 births 59,663 vs May 2025 60,718; Jan-May 2026 cumulative 282,222 vs 280,979. Same publisher/definition as target; the most recent and m
- corroborating: ['p172', 'p173', 'p174', 'p175', 'p176', 'p177'] Sankei reporting of MHLW preliminary Jan/Feb 2026 births; consistent with the MHLW Jan-May cumulative p98 (Jan+Feb 2026 = 109,455). Same underlying source as p94-p110, so not independent confirmation,
- corroborating: ['p64', 'p65', 'p66', 'p67', 'p68'] MHLW preliminary monthly births 2024 (Apr-Aug), same definition as target. July 2024 = 62,306 is the key seasonal anchor for July.
- corroborating: ['p11', 'p20', 'p21', 'p28'] All report 2025 Japanese-national births = 671,236 (p21 rounded to ~670,000). Same figure, multiple outlets; not independent. Definition is Japanese nationals only, so must be bridged to the total-inc
- conflicting: ['p55', 'p199'] p55 gives 2025 total births incl. foreign nationals as 705,809 (preliminary, published 2026-03-08); p199 gives 2024 total incl. foreign nationals as 709,051 (final, published 2026-08-07). These are di
- corroborating: ['p197', 'p198', 'p209', 'p210'] Nikkei reports ~20,000+ foreign-national births in 2024, >3% share; consistent with MHLW p200 (22,878, 3.2%). Same underlying statistic, multiple vintages.
- corroborating: ['p200', 'p201', 'p202'] MHLW 2024: foreign-national births 22,878 = 3.2% of total, up 1.8pp in 10 years. This is the bridge factor to convert Japanese-national series to the total-incl-foreigners target.
- corroborating: ['p123', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139', 'p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150'] Nanao City monthly births — a single small municipality (~50k pop). Too small and noisy to inform the national July level; useful only as a qualitative check that July births are not anomalous. Not us
- corroborating: ['p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166', 'p167', 'p168', 'p169', 'p170', 'p171'] Ishikari City monthly natural-change data — single small municipality, not usable for national scaling; only contextual.
- corroborating: ['p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121', 'p122'] Prefecture-level May 2026 births from the same MHLW snapshot as p94-p110; consistent with national total (sum of listed prefectures is a fraction of 59,663). Useful only as a consistency check, not a 
- corroborating: ['p187', 'p188'] Jan-Sep 2025 births incl. foreign nationals = 525,064, -2.8% yoy. Consistent with the 2025 total level (p55) and the monthly MHLW series. Provides a 2025 partial-year anchor.
- corroborating: ['p191', 'p192'] July 2025 marriages +22.5% yoy — a conception-side signal for ~April 2026 births, not July 2026. Not directly relevant to July 2026 births (which depend on Sep-Oct 2025 conceptions).
- corroborating: ['p179', 'p180', 'p181', 'p182', 'p183', 'p184', 'p185', 'p186'] Postpartum depression and satogaeri context — qualitative only, no quantitative link to July 2026 births. Not usable numerically.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p11', 'p20', 'p28', 'p21'] All report 2025 Japanese-national births at 671,236 (or ~670,000 rounded); same underlying MHLW final/provisional vital statistics, so they are one measurement, not independent confirmations.
- corroborating: ['p12', 'p29', 'p22', 'p30'] Year-on-year decline of 14,937 (~15,000) and 2.2% decline in 2025 Japanese births; consistent arithmetic from the same source.
- corroborating: ['p13', 'p24', 'p31', 'p14', 'p25', 'p32'] TFR 1.14 in 2025, down 0.01 point; same statistic repeated across outlets.
- corroborating: ['p15', 'p33', 'p34', 'p16', 'p60', 'p61', 'p321', 'p322'] 2025 marriages ~489,000-506,000 depending on preliminary vs final and definition; all show a small increase (~1%). Different vintages, not contradictions.
- corroborating: ['p55', 'p317', 'p318', 'p199'] 2025 births including foreign nationals ~705,809 (preliminary) vs 709,051 (2024 final); consistent with a ~2.1% decline and with the 2024 total-incl-foreigners level.
- corroborating: ['p197', 'p198', 'p200', 'p201', 'p209', 'p210'] Foreign-national births ~20,000-22,878 in 2024, share ~3.0-3.2%; the MHLW 3.2% figure is the more precise version of the Nikkei '>3%' statement.
- corroborating: ['p64', 'p65', 'p66', 'p67', 'p68'] 2024 monthly MHLW preliminary births; July (62,306) is the seasonal peak, above June (55,313) and August (60,698).
- corroborating: ['p69', 'p70', 'p71', 'p72', 'p73', 'p74'] 2025 monthly and Jan-Apr cumulative MHLW preliminary births; consistent with the 2025 annual decline.
- corroborating: ['p94', 'p95', 'p96', 'p97', 'p108', 'p212', 'p213', 'p214', 'p215'] May 2026 births 59,663 vs 60,718 in May 2025 (-1.7%); duplicated across p94/p212 and p95/p213, so one measurement.
- corroborating: ['p98', 'p99', 'p100', 'p109', 'p218', 'p219', 'p220', 'p221'] Jan-May 2026 cumulative 282,222 vs 280,979 (+0.4%); duplicated copies of the same MHLW table.
- corroborating: ['p101', 'p102', 'p103', 'p110', 'p224', 'p225', 'p226', 'p227'] Trailing-12-month births 707,052 vs 709,893 (-0.4%); duplicated copies.
- corroborating: ['p172', 'p173', 'p174', 'p175', 'p176', 'p177'] Jan 2026 +0.5%, Feb 2026 -0.4%, Jan-Feb cumulative +0.1%; consistent with the Jan-May +0.4% figure.
- corroborating: ['p187', 'p188'] Jan-Sep 2025 births incl. foreigners 525,064, -2.8% yoy; consistent with the 2025 annual decline.
- conflicting: ['p94', 'p98', 'p172', 'p173'] May 2026 is -1.7% yoy while Jan-May cumulative is +0.4% and Jan/Feb were near flat; the recent month is weaker than the year-to-date, so the July 2026 yoy factor is genuinely uncertain between roughly
- conflicting: ['p11', 'p55'] Not a real conflict: 671,236 is Japanese nationals only, 705,809 includes foreign nationals; the ~34,000 gap is the foreign-national component plus definitional scope.
- conflicting: ['p243', 'p71', 'p262'] March 2025 births appear as 50,767 (p71) and 53,619 (p243/p262); different vintages/definitions of the preliminary table. Use p71 for the monthly series and treat p243 as a separate vintage, not a med
- corroborating: ['p272', 'p273', 'p274', 'p275', 'p276', 'p277', 'p278', 'p279', 'p280'] Pregnancy-notification series from 2020-21; internally consistent but far too old to constrain the Sep-Oct 2025 conception cohort for July 2026.
- corroborating: ['p284', 'p285', 'p286', 'p287', 'p288', 'p289', 'p290', 'p291', 'p292', 'p293', 'p294', 'p295', 'p296', 'p297', 'p298', 'p299', 'p300', 'p301', 'p302', 'p303', 'p304', 'p305', 'p306', 'p307', 'p308', 'p309', 'p310', 'p311', 'p312'] Saitama prefecture pregnancy-notification breakdown; internally consistent but sub-national and undated, unusable for a national July 2026 level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July-to-June seasonal ratio of monthly births | 1.126 | 1.05..1.2 | 0.7937..1.587 (widened) | ratio | unused | From p64/p65 (July 2024 62,306 / June 2024 55,313 = 1.126); July is consistently the seasonal peak in the 2024 monthly table. Range reflects year-to-year variation in the July/June ratio and the fact that the anchor month is May 2026, not June 2026. | The July/June seasonal pattern of 2024 carries over to 2026 and May-to-July is a reasonable stand-in for June-to-July. | A June 2026 preliminary figure showing the July/June ratio far outside 1.05-1.20, or evidence of a large shift in the seasonal birth pattern. |
| a2 | July 2026 to July 2025 year-on-year change factor | 1 | 0.94..1.06 | 0.8928..1.116 (widened) | ratio | m2 (m2) | Jan-May 2026 cumulative births are +0.4% yoy (p98/p99) but May 2026 alone is -1.7% (p94/p95); the recent month is weaker than the year-to-date, so the July yoy factor is centered near flat with a range spanning roughly -6% to +6%. | The July 2026 yoy change is similar to the recent Jan-May 2026 trend rather than reverting to the 2025 annual decline. | A June 2026 preliminary figure showing a yoy change well outside -6% to +6%. |
| a3 | July 2026 to July 2024 two-year change factor | 0.97 | 0.9..1.04 | 0.8653..1.082 (widened) | ratio | unused | Bridges the two-year gap from July 2024 (p64) to July 2026. 2025 annual births incl. foreigners fell 2.1% (p56/p318) and Jan-May 2026 is +0.4% (p98/p99), so the cumulative two-year change is roughly -1.7%; centered at 0.97 with a range spanning -10% to +4% to allow for July-specific deviation. | The July 2026 level is close to July 2024 adjusted by the cumulative national trend over 2025-2026. | A June 2026 preliminary figure implying a two-year change well outside 0.90-1.04. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | n/a | ['p64', 'p98', 'p99'] / [] | [] |  | 0.00 |  | yoy_scaling needs target for 2025 |
| m2 | formula_mc | 62,235 | ['p64'] / ['a2'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m3 | formula_mc | 62,754 | ['p64', 'p98', 'p99'] / [] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m2 formula_mc: p64 * a2; Monte Carlo P10 to P90 50,296 to 77,021; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p64 * (p98 / p99); Monte Carlo P10 to P90 45,820 to 85,799; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 62,235 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 62,754 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.38.

Result: central **62,494** birth, 80% interval [45,362, 86,096] birth, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 0.50

Unit of the estimate: birth (births; total for 2026-07-01 to 2026-07-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for the target — live births in Japan during July 2026, as counted in MHLW's preliminary monthly vital statistics (including foreign nationals resident in Japan) — is 62,494 birth (80% model-based interval 45,362 to 86,096 birth).

Main evidence: July 2024 provisional births were 62,306 birth; Jan–May 2026 cumulative births were 282,222 birth versus 280,979 birth in Jan–May 2025. One route scales the July 2024 level by the Jan–May cumulative ratio (62,754 birth, weight 50%); the other applies an explicit July year-on-year factor centered at 1 (range 0.8928 to 1.116) to the same July 2024 base (62,235 birth, weight 50%). The two blocks are combined by geometric mean with equal weight; the interval is conditional on the assumptions, not a demonstrated accuracy guarantee.

Observed: the July 2024 level and the two cumulative totals. Assumed/transferred: that July 2026's year-on-year change resembles the Jan–May ratio or the flat-centered factor. The biggest risk is that July reverts to the steeper 2025 decline, making the estimate too high. The most useful missing evidence would be July 2025 births and any early 2026 monthly birth counts.

Unit of the estimate: birth (births; total for 2026-07-01 to 2026-07-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 July 2026 to July 2025 year-on-year change factor: 1 ratio, range 0.8928 to 1.116 (range widened by code); used by m2. Overturned by: A June 2026 preliminary figure showing a yoy change well outside -[n] to +[n].

Method details (computed by code):
- m2 formula_mc: p64 * a2; Monte Carlo P10 to P90 50,296 to 77,021; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p64 * (p98 / p99); Monte Carlo P10 to P90 45,820 to 85,799; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 62,235 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 62,754 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.38.

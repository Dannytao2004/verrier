# Evidence ledger: fc_jp_births_2026_07

- Question: Assume today is 2026-08-25. You know nothing published after this date. Estimate the number of births in Japan in July 2026, as first reported in the Ministry of Health, Labour and Welfare's preliminary monthly vital statistics (which also count foreign nationals in Japan).
- as_of: 2026-08-25
- Pinned target: Number of live births occurring in Japan in July 2026 among all persons in Japan, including foreign nationals, as first published in the MHLW preliminary monthly vital statistics. | unit birth | period 2026-07-01..2026-07-31 | publisher Ministry of Health, Labour and Welfare (MHLW), Japan

- Official value (scoring only, never shown to the agent): 62,479

## Directions and pages

### d1 [own_history] MHLW monthly vital statistics time series

Hypothesis: July 2026 preliminary births should be near recent July preliminary levels adjusted for the declining trend and for 2026 Hinoeuma effects; prior July values and 2026 Jan-Jun values anchor the level, seasonality, and volatility.

Queries issued by the searcher: 人口動態統計速報 令和7年7月 出生数; monthly vital statistics Japan 2025 July births preliminary MHLW; 人口動態統計速報 令和8年 2026年 出生数 5月分 厚生労働省; 人口動態統計速報 令和8年6月分 出生数 2026; 人口動態統計速報 令和6年7月分 出生数 前年同月比

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2025/dl/toukeihyo_07.pdf` -> **snapshot** (snapshot 20260517093739); points raw/verified 15/15
  - p1 MHLW monthly report July 2025 births (Japanese nationals only, not including for = **60,650** as written "60 650", value check pending births (2025-07-01..2025-07-31) [keep: ] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p2 MHLW monthly report July 2024 births (previous year, approximate) = **62,306** as written "62 306", value check pending births (2024-07-01..2024-07-31) [DISCARD: Duplicate of p9: both report July 2024 Japanese-only births as 62,306.] quote: "7 月 60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p3 MHLW monthly report July 2025 births year-on-year change rate = **2.7** % (2025-07-01..2025-07-31) [DISCARD: Sign mismatch: the quoted table shows a decline (△2.7), while the data-point value is positive 2.7; using it as a positi] quote: "60 650 62 306 △ 1 656 △ 2.7 6.0 6.1"
  - p4 MHLW monthly report June 2025 births = **55,658** as written "55 658", value check pending births (2025-06-01..2025-06-30) [keep: ] quote: "6月 55 658 114 709 111 51 △ 59 051 607 706 185 31 156 14 564"
  - p5 MHLW monthly report January 2025 births = **51,816** as written "51 816", value check pending births (2025-01-01..2025-01-31) [keep: ] quote: "令和7年1月 51 816 172 287 124 56 △120 471 570 682 186 32 401 14 045"
  - p6 MHLW monthly report cumulative January-July 2025 births = **379,729** as written "379 729", value check pending births (2025-01-01..2025-07-31) [keep: ] quote: "累 計 1月~7月 379 729 392 304 △ 12 575 △ 3.2 5.5 5.6"
  - p7 MHLW monthly report cumulative January-July 2024 births = **392,304** as written "392 304", value check pending births (2024-01-01..2024-07-31) [keep: ] quote: "累 計 1月~7月 379 729 392 304 △ 12 575 △ 3.2 5.5 5.6"
  - p8 MHLW monthly report cumulative January-July 2025 births year-on-year change rate = **3.2** % (2025-01-01..2025-07-31) [DISCARD: Sign mismatch: the quoted table shows △3.2% while the data-point value is positive 3.2%.] quote: "379 729 392 304 △ 12 575 △ 3.2 5.5 5.6"
  - p9 MHLW monthly report July 2024 births (monthly table, previous year) = **62,306** as written "62 306", value check pending births (2024-07-01..2024-07-31) [keep: ] quote: "7月 62 306 126 383 115 51 △ 64 077 567 680 204 46 747 15 630"
  - p10 MHLW monthly report June 2024 births (monthly table, previous year) = **55,313** as written "55 313", value check pending births (2024-06-01..2024-06-30) [keep: ] quote: "6月 55 313 116 489 130 75 △ 61 176 534 698 209 32 030 14 025"
  - p11 MHLW monthly report January 2024 births (monthly table, previous year) = **54,624** as written "54 624", value check pending births (2024-01-01..2024-01-31) [keep: ] quote: "令和6年1月 54 624 151 988 110 52 △ 97 364 575 689 199 39 572 14 602"
  - p12 MHLW monthly report July 2025 births per 1,000 population (birth rate) = **6** births per 1,000 population (2025-07-01..2025-07-31) [DISCARD: Birth rate per 1,000 population; not needed for a birth-count estimate.] quote: "6.0 11.6 1.6 0.7 △ 5.7 9.9 11.9 2.9 5.6 1.47 7月"
  - p13 MHLW monthly report July 2025 births to foreign nationals (national total, 外国 ro = **3** births (2025-07-01..2025-07-31) [DISCARD: Mis-scoped foreign-birth figure; conflicts with the much larger stat.go.jp foreign series.] quote: "外 国 3 - 3 14 5 9 - -"
  - p14 MHLW monthly report cumulative January-July 2025 births to foreign nationals (外国 = **7** births (2025-01-01..2025-07-31) [DISCARD: Mis-scoped cumulative foreign-birth figure; conflicts with the stat.go.jp foreign series.] quote: "外 国 7 1 6 69 44 25 - -"
  - p15 MHLW monthly report July 2025 births with unknown prefecture (不詳 row) = **99** births (2025-07-01..2025-07-31) [DISCARD: Unknown-prefecture count is a small administrative detail not needed for the national total.] quote: "不 詳 ・ ・ ・ 99 79 20 - -"
- `https://www.wic-net.com/material/document/21937/2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yosshy0131.hatenablog.com/entry/2025/10/09/200257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450011&tstat=000001028897&cycle=1&year=20250&month=23070907&tclass1=0000010` -> **snapshot** (snapshot 20251112234917); points raw/verified 0/0

### d2 [shocks] zodiac-year behavior and conception timing

Hypothesis: 2026 is 丙午 (Hinoeuma), historically associated with reduced births; July 2026 may be depressed if conceptions were avoided in late 2025. Historical 1966 monthly patterns and current pregnancy/notification signals can size the effect.

Queries issued by the searcher: 丙午 2026 出生数 減少; 1966 丙午 出生数 月別 推移; hinoeuma 2026 Japan births decline; 2026年 出生数 見通し 丙午 影響

- `https://www.jri.co.jp/report/economistcolumn/detail/16632/` -> **snapshot** (snapshot 20260513004054); points raw/verified 6/3
  - p16 Year-on-year change in Japan's monthly live births, January 2026 preliminary (al = **0.5** % (2026-01-01..2026-01-31) [keep: ] quote: "3月末、2026年1月の出生数の速報値が出た。速報値では、前年同月比+0.5%でわずかながら増加となった。"
  - p17 Year-on-year decline in Japan's annual births in 1966 (Hinoeuma) versus prior ye = **25** % (1966-01-01..1966-12-31) [DISCARD: Redundant copy of the 1966 Hinoeuma decline already represented by p38.] quote: "前回の丙午だった1966年には、故事に倣って丙午の出産を意図的に避ける夫婦も多く、出生数が前年比▲25%の大幅な減少を記録した。"
  - p18 Average age at first childbirth in Japan 60 years ago (around 1966) = **25** years of age (1966-01-01..1966-12-31) [keep: ] quote: "60年前の女性の平均第一子出産年齢は25歳代であったが、現在は31歳と5歳も上がっており"
- `https://chinesezodiac.com/studies/fire-horse-birth-rates` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/report_pdf/202401013A-buntan1_1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://baby-calendar.jp/smilenews/detail/104224/` -> **snapshot** (snapshot 20260610051242); points raw/verified 15/14
  - p19 1966 Hinoeuma year-on-year decline in births (Japan, annual) = **25** % (1966-01-01..1966-12-31) [DISCARD: Redundant copy of the 1966 Hinoeuma decline already represented by p38.] quote: "前回の丙午である1966年(昭和41年)には、「この年に生まれた女性は気性が激しい」などの迷信が広まり、出生数が前年比で約25%も激減しました。"
  - p20 Estimated 2025 births in Japan (preliminary vital statistics basis incl. foreign = **667,542** births (2025-01-01..2025-12-31) [DISCARD: Ambiguous mixed-basis 2025 annual estimate; not directly usable for the July 2026 all-person preliminary target.] quote: "(※1)本文中の出生数(66万7542人程度)は、厚生労働省公表の人口動態統計速報値(在留外国人等を含む)をもとに、確定値(日本に住む日本人のみの出生数)ベースでの着地を想定した推計値です。"
  - p21 Average interval from marriage to first-child birth (Japan, 2024 data) = **2.8** years (2024-01-01..2024-12-31) [DISCARD: Marriage-to-first-birth interval is contextual but not used in any executable route.] quote: "注目すべきなのは、2024年時点のデータで見ると、結婚から第1子出産までの平均期間が約2.8年となっている点です。"
  - p22 Average age of current parent generation (Japan, around 2025) = **30** years old (2025-01-01..2025-12-31) [DISCARD: General parental-age context not used in the estimate.] quote: "しかし、現在の親世代は平均30歳前後。"
  - p23 Average age at first-child birth among survey respondents (pregnant/parenting wo = **30.7** years old (2025-12-08..2025-12-12) [DISCARD: Survey age context not used; p18 already covers the relevant age-shift point.] quote: "実際に今回のベビーカレンダーのアンケート調査では、第1子出産時の平均年齢は「30.7歳」となっており"
  - p24 Survey respondents who would not avoid 2026 birth due to superstition, prioritiz = **76.2** % (2025-12-08..2025-12-12) [keep: ] quote: "「迷信は気にせず、自分たちの計画やタイミングを優先したい(優先した)」と回答した人が76.2%(712人)で最多となりました。"
  - p25 Survey respondents who would deliberately choose a 2026 birth (share of 935) = **5.2** % (2025-12-08..2025-12-12) [keep: ] quote: "さらに、「メリットも考えられるので、あえて選びたい(選んだ)」は5.2%(49人)で"
  - p26 Survey respondents advised by family/acquaintances to avoid a 2026 birth (share  = **12.4** % (2025-12-08..2025-12-12) [keep: ] quote: "「2026年の出産は避けたほうがいい」「女の子だと大変」といった言葉をかけられた経験があるかを尋ねたところ、12.4%(116人)が「ある」と回答。"
  - p27 Survey respondents aware of Hinoeuma superstition (share of 935) = **8** tenths of respondents (80%) (2025-12-08..2025-12-12) [keep: ] quote: "「よく知っている」31.2%(292人)、「なんとなく聞いたことはある」49.0%(458人)を合わせて、約8割が認知していました。"
  - p28 Survey respondents citing money as top anxiety when deciding first pregnancy/bir = **32** % (2025-12-08..2025-12-12) [DISCARD: Money anxiety is not a Hinoeuma-avoidance signal and is not used.] quote: "「最初に妊娠・出産を決めるにあたり、最も不安に感じたこと」を尋ねたところ、「金銭面」が32.0%(299人)で最多となりました。"
  - p29 Survey respondents citing own age/physical strength as top anxiety (share of 935 = **24.8** % (2025-12-08..2025-12-12) [DISCARD: Age/physical-strength anxiety is not used.] quote: "次いで「自身の年齢や体力」24.8%(232人)、「仕事やキャリア」10.5%(98人)と続き"
  - p30 Survey respondents citing work/career as top anxiety (share of 935) = **10.5** % (2025-12-08..2025-12-12) [DISCARD: Work/career anxiety is not used.] quote: "次いで「自身の年齢や体力」24.8%(232人)、「仕事やキャリア」10.5%(98人)と続き"
  - p31 Survey sample size (pregnant/parenting women aged 20s-40s) = **935** respondents (2025-12-08..2025-12-12) [keep: ] quote: "妊娠中・育児中のママ(20〜40代)935人にアンケート調査を行い"
  - p32 Survey period (start date) = **20,251,208** as written "2025年12月8日", value check pending date (2025-12-08..2025-12-08) [DISCARD: Malformed date value; duplicates the survey period already implied by p24-p27.] quote: "調査期間:2025年12月8日(月)〜12月12日(金)"
- dropped by code checks: 4 (period_end missing or unparseable: 3; number: low/high given but value_as_written is not a range: 1)

### d3 [related_series] annual births and monthly allocation

Hypothesis: If a 2026 annual births forecast or a reliable Jan-Jun 2026 partial total is available, July 2026 can be estimated as annual births multiplied by the historical July share, adjusted for any Hinoeuma-related timing shift.

Queries issued by the searcher: 2025年 出生数 速報 厚生労働省 人口動態統計; 2026年 出生数 予測 丙午 減少; 2026年 人口動態統計速報 出生数 6月 前年同月比; 2026年 出生数 月別 速報 1月 2月 3月 4月 5月

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260828-GYT1T00289/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jri.co.jp/report/economistcolumn/detail/16632/` -> **snapshot** (snapshot 20260513004054); points raw/verified 7/2
  - p33 January 2026 preliminary live births year-on-year change (MHLW preliminary month = **0.5** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p16 (same January 2026 yoy signal).] quote: "3月末、2026年1月の出生数の速報値が出た。速報値では、前年同月比+0.5%でわずかながら増加となった。"
  - p34 1966 (previous Hinoeuma year) live births year-on-year change = **25** % (1966-01-01..1966-12-31) [DISCARD: Duplicate of the 1966 Hinoeuma decline already represented by p38.] quote: "前回の丙午だった1966年には、故事に倣って丙午の出産を意図的に避ける夫婦も多く、出生数が前年比▲25%の大幅な減少を記録した。"
- `https://www.nippon.com/ja/japan-data/h02872/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period_end missing or unparseable: 4; period_end 2026-12-31 after as_of: 1)

### d4 [administrative] municipal maternal health records

Hypothesis: Births in July 2026 correspond to pregnancies notified around late 2025 or early 2026; monthly pregnancy notification counts adjusted for notification-to-live-birth ratios and gestational timing can predict July births.

Queries issued by the searcher: 妊娠届出数 月別 2025 2026; 母子保健事業報告 妊娠届出数 2026; 人口動態統計速報 2026年6月 出生数; 妊娠届出数 全国 出生数 比率 厚生労働省 母子保健事業報告

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fukushi.metro.tokyo.lg.jp/documents/d/fukushi/r7boshi_annualreport-pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/index.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.bodik.jp/dataset/e49a588b-4bf7-487f-a51e-9c8ffb2a9918/resource/2ec2f3dd-a90b-4358-9efe-5ee75fc30643` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] large municipalities with earlier monthly birth counts

Hypothesis: Tokyo wards or other large cities may publish July 2026 birth counts before the national preliminary report; scaling by their historical share of national births gives an early estimate.

Queries issued by the searcher: 東京都 人口動態 月報 2026年7月 出生数; 東京23区 出生数 2026年7月; 横浜市 人口動態 2026年7月 出生数; 大阪市 毎月推計人口 2026年7月 出生数 死亡数

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.city.yokohama.lg.jp/city-info/yokohamashi/tokei-chosa/portal/opendata/jinko-dotai-tsuki.html` -> **snapshot** (snapshot 20260413181604); points raw/verified 0/0
- `https://www.jri.co.jp/file/report/research/pdf/16351.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yomiuri.co.jp/national/20260829-GYT1T00068/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] published forecasts

Hypothesis: Research institutes may publish 2026 annual or monthly birth forecasts incorporating Hinoeuma and recent trends; these provide independent anchors but must be reconciled with the preliminary-report definition.

Queries issued by the searcher: 2026年 出生数 予測 丙午 減少; Japan birth forecast 2026 hinoeuma fire horse births decline projection; 2026年1月 出生数 速報 厚生労働省 人口動態統計 前年同月比; 2026年 出生数 予測 68万人 丙午 影響 研究所 見通し

- `https://www.jri.co.jp/report/economistcolumn/detail/16632/` -> **snapshot** (snapshot 20260513004054); points raw/verified 7/3
  - p35 Year-on-year change in Japan monthly live births, January 2026 preliminary (all  = **0.5** % (2026-01-01..2026-01-31) [DISCARD: Duplicate of p16.] quote: "3月末、2026年1月の出生数の速報値が出た。速報値では、前年同月比+0.5%でわずかながら増加となった。"
  - p36 Year-on-year change in Japan live births in 1966 (Hinoeuma year) = **25** % (1966-01-01..1966-12-31) [DISCARD: Duplicate of the 1966 Hinoeuma decline.] quote: "前回の丙午だった1966年には、故事に倣って丙午の出産を意図的に避ける夫婦も多く、出生数が前年比▲25%の大幅な減少を記録した。"
  - p37 Average age of mother at first birth in Japan, 60 years ago (approx. 1966) = **25** years of age (1966-01-01..1966-12-31) [DISCARD: Duplicate of p18.] quote: "60年前の女性の平均第一子出産年齢は25歳代であったが、現在は31歳と5歳も上がっており"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/01.html` -> **snapshot** (snapshot 20260410161952); points raw/verified 0/0
- `https://www.shugiin.go.jp/Internet/itdb_shitsumon.nsf/html/shitsumon/b216033.htm` -> **snapshot** (snapshot 20260209055049); points raw/verified 4/0
- `https://www.sompo-ri.co.jp/topics_plus/20251203-20996/` -> **snapshot** (snapshot 20260411235758); points raw/verified 5/1
  - p38 Year-on-year change in Japan births in 1966 (Hinoeuma year) versus previous year = **25.4** % (1966-01-01..1966-12-31) [keep: ] quote: "前回の丙午の年である1966年の出生数は前年比で25.4%と大きく減少しており"
- dropped by code checks: 12 (period_end missing or unparseable: 8; period_end 2026-12-31 after as_of: 2; number: no number in value_as_written: 2)

### d7 [related_series] foreign residents in Japan

Hypothesis: Because the target includes foreign nationals, separately estimating foreign-national births and adding them to a Japanese-national series can improve coverage if a Japanese-only monthly series is more readily available.

Queries issued by the searcher: 外国人 出生数 日本 2024 月別 人口動態統計; 人口動態統計 外国人 出生数 2024 割合; 人口動態統計速報 令和8年6月分 出生数 2026; 2026年 上半期 出生数 速報 厚生労働省 外国人 含む

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/gaikoku26/dl/02_r08.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/pdf/202606.pdf` -> **snapshot** (snapshot 20260724135116); points raw/verified 15/13
  - p39 Foreign population live births, Japan, July 2024 (monthly) = **1,979** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 3,418,173 -48,656 -14.23 1,979 714 1,265 227,845 276,693 -48,848 -1,073"
  - p40 Foreign population live births, Japan, July 2025 (monthly) = **1,874** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 3,747,640 -62,472 -16.67 1,874 706 1,168 276,416 338,912 -62,496 -1,144"
  - p41 Foreign population live births, Japan, calendar year 2024 = **21,900** births (2024-01-01..2024-12-31) [keep: ] quote: "2024年 3,506,158 347,675 110.08 21,900 8,871 13,029 3,231,871 2,889,687 342,184 -7,538"
  - p42 Foreign population live births, Japan, calendar year 2025 = **23,068** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年 3,839,332 333,174 95.03 23,068 9,233 13,835 3,758,011 3,430,454 327,557 -8,218"
  - p43 Japanese population live births, Japan, July 2024 (monthly) = **62,304** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 120,557,198 -39,226 -0.33 62,304 126,371 -64,067 122,156 98,388 23,768 1,073"
  - p44 Japanese population live births, Japan, July 2025 (monthly) = **60,647** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 119,619,094 -36,312 -0.30 60,647 118,274 -57,627 118,226 98,055 20,171 1,144"
  - p45 Total population live births, Japan, July 2024 (monthly) = **64,283** births (2024-07-01..2024-07-31) [keep: ] quote: "7月 July 123,975,371 -87,882 -0.71 64,283 127,085 -62,802 350,001 375,081 -25,080"
  - p46 Total population live births, Japan, July 2025 (monthly) = **62,521** births (2025-07-01..2025-07-31) [keep: ] quote: "7月 July 123,366,734 -98,784 -0.80 62,521 118,980 -56,459 394,642 436,967 -42,325"
  - p47 Total population live births, Japan, calendar year 2024 = **717,291** births (2024-01-01..2024-12-31) [DISCARD: Annual total births are redundant with the monthly total series and foreign components already kept.] quote: "2024年 123,801,750 -550,127 -4.42 717,291 1,607,261 -889,970 4,192,568 3,852,725 339,843"
  - p48 Total population live births, Japan, calendar year 2025 = **694,162** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年 123,219,024 -582,726 -4.71 694,162 1,613,143 -918,981 4,732,271 4,396,016 336,255"
  - p49 Japanese population live births, Japan, calendar year 2024 = **695,391** births (2024-01-01..2024-12-31) [DISCARD: Japanese annual births are redundant with the Japanese monthly/component evidence.] quote: "2024年 120,295,592 -897,802 -7.41 695,391 1,598,390 -902,999 960,697 963,038 -2,341 7,538"
  - p50 Japanese population live births, Japan, calendar year 2025 = **671,094** births (2025-01-01..2025-12-31) [DISCARD: Japanese annual births are redundant with the Japanese monthly/component evidence.] quote: "2025年 119,379,692 -915,900 -7.61 671,094 1,603,910 -932,816 974,260 965,562 8,698 8,218"
  - p51 Foreign population, Japan, as of June 1, 2026 (provisional estimate) = **3,730,000** persons (2026-06-01..2026-06-01) [DISCARD: Foreign population level is not a birth count and has no matched prior level to form a growth factor.] quote: "<外国人人口> 373万人で、前年同月に比べ増加 32万8千人( 9.64%)"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/gaikoku26/index.html` -> **snapshot** (snapshot 20260818065537); points raw/verified 0/0
- dropped by code checks: 2 (scale word 'thousand' not supported by quote or table header: 2)

### d8 [base_rates] seasonal index

Hypothesis: July births have a stable seasonal ratio to adjacent months and to the annual total; recent monthly ratios and available 2026 June/May counts constrain July even without a direct July observation.

Queries issued by the searcher: 人口動態統計 月別 出生数 2025 速報; monthly births Japan seasonality July 出生数 月別 2024; 人口動態統計速報 2026年5月分 出生数 厚生労働省; mhlw 人口動態統計速報 令和8年 2026 月別 出生数

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p52 Japan total live births, May 2026 (preliminary monthly vital statistics, all per = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p53 Japan total live births, May 2025 (preliminary, prior year comparison) = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p54 Japan total live births, cumulative Jan-May 2026 (preliminary) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p55 Japan total live births, cumulative Jan-May 2025 (preliminary) = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p56 Japan total live births, trailing 12 months Jun 2025-May 2026 (preliminary) = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p57 Japan total live births, trailing 12 months Jun 2024-May 2025 (preliminary) = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p58 Japan annualised birth rate for May 2026 (per 1,000 population, year-converted) = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [DISCARD: Birth rate; not needed for a count estimate.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p59 Japan annualised birth rate for May 2025 (per 1,000 population, year-converted) = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [DISCARD: Birth rate; not needed for a count estimate.] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p60 Japan annualised birth rate, cumulative Jan-May 2026 (per 1,000 population) = **5.6** births per 1,000 population (2026-01-01..2026-05-31) [DISCARD: Birth rate; not needed for a count estimate.] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p61 Japan annualised birth rate, trailing 12 months Jun 2025-May 2026 (per 1,000 pop = **5.7** births per 1,000 population (2025-06-01..2026-05-31) [DISCARD: Birth rate; not needed for a count estimate.] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p62 Japan total live births, May 2026, by prefecture of notification (national row o = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [DISCARD: Duplicate of p52 at prefecture level.] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p63 Japan total live births, cumulative Jan-May 2026, by prefecture of notification  = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [DISCARD: Duplicate of p54 at prefecture level.] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
  - p64 Japan total deaths, May 2026 (preliminary) = **122,385** as written "122 385", value check pending deaths (2026-05-01..2026-05-31) [DISCARD: Deaths, not births.] quote: "死 亡 122 385 124 572 △ 2 187 △ 1.8 11.7 11.9 98.7"
  - p65 Japan natural decrease, May 2026 (births minus deaths, preliminary) = **-62,722** as written "△ 62 722", value check pending persons (2026-05-01..2026-05-31) [DISCARD: Natural decrease, not births.] quote: "自 然 増 減 △ 62 722 △ 63 854 1 132 ... △ 6.0 △ 6.1 ..."
  - p66 Japan total foetal deaths (stillbirths), May 2026 (preliminary) = **1,318** as written "1 318", value check pending stillbirths (2026-05-01..2026-05-31) [DISCARD: Stillbirths, not live births.] quote: "死 産 1 318 1 392 △ 74 △ 5.3 21.6 22.4 96.4"
- `https://www.e-stat.go.jp/index.php/stat-search/files?cycle=7&layout=dataset&month=0&stat_infid=000040320377&tclass1=000001053058&tclass2=000001053061&` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/05.html` -> **snapshot** (snapshot 20260804122455); points raw/verified 0/0
- `https://gadandan.co.jp/news/birthday-most-common-month/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [administrative] d8

Hypothesis: A June 2026 preliminary MHLW monthly report, due around late August 2026, would supply the missing month between the observed May 2026 level (p52) and the July target. A June-to-July seasonal ratio from prior years would then directly anchor July 2026 and also test whether the May -1.7% weakness persisted.

Queries issued by the searcher: site:mhlw.go.jp 人口動態統計速報 令和8年6月 出生数; 2026年6月 出生数 速報 人口動態; 人口動態統計速報 令和8年6月分 出生数 6万 人 前年同月比; 2025年7月 出生数 速報 人口動態 前年同月比 人

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202606.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pacola.co.jp/n2026091515/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 15/15
  - p67 Japan total live births, May 2026 (preliminary monthly vital statistics, all per = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p68 Japan total live births, May 2025 (preliminary, prior year comparison) = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p69 Year-on-year change in Japan total live births, May 2026 vs May 2025 = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p70 Year-on-year percent change in Japan total live births, May 2026 = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p71 Japan cumulative total live births, Jan-May 2026 (preliminary) = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p72 Japan cumulative total live births, Jan-May 2025 (preliminary) = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p73 Year-on-year change in Japan cumulative live births, Jan-May 2026 vs Jan-May 202 = **1,243** as written "1 243", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p74 Year-on-year percent change in Japan cumulative live births, Jan-May 2026 = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p75 Japan total live births, trailing 12 months Jun 2025-May 2026 (preliminary) = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p76 Japan total live births, trailing 12 months Jun 2024-May 2025 (preliminary) = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p77 Year-on-year percent change in Japan trailing-12-month live births, Jun 2025-May = **0.4** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p78 Japan annualized birth rate for May 2026 (per 1,000 population) = **5.7** births per 1,000 population (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p79 Japan annualized birth rate for May 2025 (per 1,000 population) = **5.8** births per 1,000 population (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p80 Japan cumulative annualized birth rate, Jan-May 2026 (per 1,000 population) = **5.6** births per 1,000 population (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p81 Japan cumulative annualized birth rate, Jan-May 2025 (per 1,000 population) = **5.5** births per 1,000 population (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] d5

Hypothesis: Tokyo wards or other large cities sometimes publish July 2026 birth notifications or provisional population-dynamics counts before the national preliminary report. Scaling their July count by the historical national share would give an early direct July signal and reduce reliance on May/June seasonal transfer.

Queries issued by the searcher: 東京都 特別区 2026年7月 出生数 人口動態; 2026年7月 出生届 速報 自治体 出生数; 東京都 人口動態統計 令和8年7月 出生数 速報; 大阪市 2026年7月 出生数 人口動態概況; 横浜市 人口ニュース 令和8年7月 出生数

- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.komei.or.jp/km/yachiyo-takahashi-hideyuki/2026/06/07/%e6%9d%b1%e4%ba%ac%e3%81%ae%e5%87%ba%e7%94%9f%e5%a2%97%e3%80%81%e6%94%af%e6%8f%b4%e7%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/content/10700000/000674996.pdf` -> **snapshot** (snapshot 20260322041455); points raw/verified 0/0
- `https://adeac.jp/viewitem/toshima-history/viewer/viewer/05_02_H271224_1/data/05_02_H271224_1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [administrative] d4

Hypothesis: July 2026 births correspond roughly to conceptions in October 2025. Pregnancy-notification counts for October 2025-January 2026, if published by prefectures or cities, would measure the Hinoeuma-avoidance channel for this birth cohort and help size the a1 July-specific adjustment.

Queries issued by the searcher: 妊娠届受理数 2025年10月 月別 自治体; 妊娠届出数 月別 2025 2026 市町村 公表; 東京都 妊娠届出数 月別 2025年 公表 福祉保健局; 2026年 丙午 妊娠届 減少 2025年10月 報道

- `https://data.bodik.jp/dataset/472115_ninshintodokedesu_20251201` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhlw-grants.niph.go.jp/system/files/2012/121011/201201015B/201201015B0006.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fukushi.metro.tokyo.lg.jp/documents/d/fukushi/r6boshi_annualreport-pdf` -> **snapshot** (snapshot 20251013033124); points raw/verified 0/0
- `https://www.pref.okinawa.jp/_res/projects/default_project/_page_/001/021/582/04h26boshihoken.pdf` -> **snapshot** (snapshot 20250807132152); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p39', 'p40', 'p43', 'p44', 'p45', 'p46'] The July total-population series cleanly decomposes into Japanese and foreign components: p45 is p43 plus p39 for July 2024, and p46 is p44 plus p40 for July 2025. p1 is the MHLW Japanese-only July 20
- conflicting: ['p13', 'p14', 'p39', 'p40', 'p41', 'p42'] p13 and p14 report only 3 foreign births in July 2025 and 7 cumulative Jan-Jul 2025, far below the stat.go.jp foreign live-birth series p39-p42. The p13/p14 rows are mis-scoped or otherwise unusable a
- overlapping: ['p16', 'p33', 'p35', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57'] The 2026 signals are not independent: p16, p33 and p35 are the same January 2026 +0.5% yoy signal; p54/p55 show Jan-May cumulative +0.4%; p52/p53 show May 2026 -1.7%; p56/p57 show trailing 12-month -0
- conflicting: ['p17', 'p19', 'p34', 'p36', 'p38', 'p24', 'p25', 'p26', 'p27', 'p31', 'p18'] The 1966 Hinoeuma decline is about -25% (p38 and duplicates), but modern survey evidence shows most respondents would not avoid a 2026 birth (p24), only a minority were advised to avoid (p26), and man
- corroborating: ['p45', 'p46', 'p52', 'p53'] These support a May-to-July seasonal bridge: p52 is May 2026 total births, p53 is May 2025 total births, and p46 is July 2025 total births. The same all-person definition is used, so the May/July rati
- overlapping: ['p46', 'p54', 'p55', 'p56', 'p57'] These provide alternative 2026 trend anchors for scaling July 2025 total births: Jan-May cumulative growth (p54/p55) and trailing 12-month growth (p56/p57). They overlap in time and source, so agreeme
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 1.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 Hinoeuma/timing deviation factor relative to Jan-May 2026 trend | 0.995 | 0.95..1.03 | 0.8848..1.106 (widened) | fraction | m5 (m5) | The Jan-May 2026 cumulative all-person series is already +0.4% yoy (p54/p55), so any Hinoeuma effect in early 2026 births is muted. Survey evidence shows 76.2% would not avoid a 2026 birth (p24), only 12.4% were advised to avoid (p26), and 5.2% deliberately chose a 2026 birth (p25); the historical 1 | July 2026 conceptions (roughly October 2025) faced similar Hinoeuma avoidance behavior to the January-May 2026 birth cohort. | Evidence of a sharp July-specific drop in pregnancy notifications or local July 2026 birth counts, or a renewed strong Hinoeuma avoidance signal beyond the survey evidence. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_naive | 62,521 |  | [2025] | 0.028 | 0.17 | backtest |  |
| m2 | yoy_scaling | 62,798 |  | [] |  | 0.17 | median_of_backtested |  |
| m3 | formula_mc | 61,604 | ['p52', 'p46', 'p53'] / [] | [] |  | 0.17 | median_of_backtested |  |
| m4 | formula_mc | 62,936 | ['p46', 'p16'] / [] | [] |  | 0.17 | median_of_backtested |  |
| m5 | formula_mc | 62,413 | ['p46', 'p54', 'p55'] / ['a1'] | [] |  | 0.17 | median_of_backtested |  |
| m6 | formula_mc | 62,433 | ['p46', 'p56', 'p57'] / [] | [] |  | 0.17 | median_of_backtested |  |

- m3 coverage: the whole target
- m4 coverage: the whole target
- m5 coverage: the whole target
- m6 coverage: the whole target

Result: central **62,449** birth, 80% interval [44,579, 87,483] birth, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule inverse_backtest_error, weight on methods that use assumptions 0.17

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for live births occurring in Japan in July 2026, all persons including foreign nationals, as first reported in MHLW preliminary monthly vital statistics, is 62,449 birth (80% model-based interval 44,579 to 87,483 birth). This combines 6 methods at roughly equal weights, anchored on the observed July 2025 total of 62,521 births and adjusted by recent trends: the Jan-May 2026 cumulative of 282,222 births versus 280,979 births, May 2026 of 59,663 births versus 60,718 births, the January 2026 yoy change of 0.5%, and trailing-[n]-month totals 707,052 births and 709,893 births. The July 2025 anchor and these comparisons are observed; the July-specific Hinoeuma/timing factor 0.995 (range 0.8848 to 1.106) is an assumption. The interval reflects input uncertainty only, not demonstrated accuracy. The main risk is that July-specific Hinoeuma or reporting-timing effects differ from the early-2026 pattern. Better evidence would be a July-specific Hinoeuma survey or preliminary July reporting completeness data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 Hinoeuma/timing deviation factor relative to Jan-May 2026 trend: 0.995 fraction, range 0.8848 to 1.106 (range widened by code); used by m5. Overturned by: Evidence of a sharp July-specific drop in pregnancy notifications or local July 2026 birth counts, or a renewed strong Hinoeuma avoidance signal beyond the survey evidence.

# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends (인구동향)

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly birth series

Hypothesis: The number of live births in July 2026 can be estimated by extrapolating the recent trend and seasonal pattern from the most recent monthly birth counts published before the cutoff. July typically has a seasonal factor relative to adjacent months.

Queries issued by the searcher: Statistics Korea monthly live births 2026 인구동향 출생아 수; South Korea monthly births 2025 2026 year-over-year increase statistics; 인구동향 월별 출생아 수 2025년 7월 20282명 2026년 1월 26916명 시계열; Statistics Korea monthly births series 2023 2024 2025 by month live births KOSTAT population trends

- `https://www.korea.net/NewsFocus/Society/view?articleId=297003&koreanId=296981` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.segye.com/view/20260729516289` -> **snapshot** (snapshot 20260730134609); points raw/verified 15/8
  - p1 Year-over-year increase in South Korea live births, May 2026 = **2,781** live births (persons) (2026-05-01..2026-05-31) [keep: ] quote: "올해 5월 출생아 수는 2만3160명으로 지난해와 비교해 2781명(13.6%) 증가했다."
  - p2 Year-over-year growth rate of South Korea live births, May 2026 = **13.6** percent (2026-05-01..2026-05-31) [DISCARD: Redundant restatement of p1's change in ratio form; p1 already carries the level and the change.] quote: "올해 5월 출생아 수는 2만3160명으로 지난해와 비교해 2781명(13.6%) 증가했다."
  - p3 Year-over-year growth rate of South Korea cumulative live births, January–May 20 = **15.2** percent (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 전년보다 1만6166명(15.2%) 늘어 2019년(13만4433명) 이후 가장 많았고"
  - p4 South Korea total fertility rate, May 2026 = **0.85** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "이에 따라 5월 합계출산율은 0.85로 전년보다 0.10명 증가했다."
  - p5 Year-over-year increase in South Korea total fertility rate, May 2026 = **0.1** children per woman (2026-05-01..2026-05-31) [DISCARD: Redundant restatement of p4 (the +0.10 YoY TFR change is fully implied by p4 and the prior-year level); no additional in] quote: "이에 따라 5월 합계출산율은 0.85로 전년보다 0.10명 증가했다."
  - p6 Year-over-year decrease in South Korea marriages, May 2026 = **1,392** marriages (cases) (2026-05-01..2026-05-31) [keep: ] quote: "출생 증가 가능성을 예상할 수 있는 혼인 건수는 2만368건으로 1년 전보다 1392건, 6.4% 감소했다."
  - p7 Year-over-year growth rate of South Korea marriages, May 2026 = **6.4** percent (2026-05-01..2026-05-31) [DISCARD: Redundant restatement of p6 (the -6.4% is the same May 2026 marriage change already given in absolute terms); no additio] quote: "출생 증가 가능성을 예상할 수 있는 혼인 건수는 2만368건으로 1년 전보다 1392건, 6.4% 감소했다."
  - p8 South Korea natural decrease (deaths minus births), May 2026 = **6,413** persons (2026-05-01..2026-05-31) [keep: ] quote: "5월 사망자 수는 2만9573명으로 1년 전보다 1091명(3.8%) 늘어 6413명이 자연감소했다."
- `https://news.tvchosun.com/site/data/html_dir/2026/06/24/2026062490133.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://chosun-chosun-prod.cdn.arcpublishing.com/economy/economy_general/2026/09/23/4336WE6G4BBALOXOVOQM7RBNKE/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (number: more than one number in value_as_written: 7)

### d2 [related_series] Resident registration births and administrative records

Hypothesis: Monthly counts of birth registrations from the resident registration system (주민등록) can serve as a leading or coincident indicator for the vital statistics live birth count, after adjusting for registration lag and coverage differences.

Queries issued by the searcher: 주민등록 출생아 수 월별 2026 행정안전부; resident registration births South Korea monthly 2026 주민등록인구통계 출생; 주민등록 출생 등록 2026년 6월 행정안전부 주민등록인구통계 출생자 수; 통계청 인구동향 출생아 수 행정안전부 주민등록 출생아 비율 차이

- `https://korea.nabo.go.kr/board/file/down.do?fid=33319503` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://event.kyeonggi.com/article/20260817580137` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://saif.or.kr/comm/getFile?srvcId=BBSTY1&upperNo=2620&fileTy=ATTACH&fileNo=2&board=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Hospital and health insurance birth claims

Hypothesis: National Health Insurance Service (NHIS) or Health Insurance Review & Assessment Service (HIRA) data on childbirth-related claims can provide a near-real-time proxy for monthly births, with a stable ratio to the vital statistics count.

Queries issued by the searcher: 건강보험심사평가원 분만 청구 월별 2026; NHIS childbirth claims monthly South Korea 분만실적 통계; 심평원 분만환자수 월별 2025 분만 청구 건수 통계; 인구동향 2026년 6월 출생아 수 월별 통계청

- `https://www.newsis.com/view/NISX20260804_0003736346` -> **snapshot** (snapshot 20260805121026); points raw/verified 15/7
  - p9 Year-on-year increase rate of South Korea total delivery cases, 2025 vs 2024 = **6.1** % (2025-01-01..2025-12-31) [keep: ] quote: "2025년 전국의 총 분만 건수는 25만2000건으로 2024년(23만7484건) 대비 6.1% 증가했다."
  - p10 Sejong delivery (분만) cases, 2025 = **3,299** delivery cases (2025-01-01..2025-12-31) [DISCARD: Sejong 2025 delivery count is a small regional component; without a regional-share model it cannot improve the national ] quote: "세종은 지난해 3299건으로 전년(2864건) 대비 435건이 증가했다."
  - p11 Sejong delivery (분만) cases, 2024 = **2,864** delivery cases (2024-01-01..2024-12-31) [DISCARD: Sejong 2024 delivery count is only a base for the 2025 Sejong figure; the regional pair adds no information about the na] quote: "세종은 지난해 3299건으로 전년(2864건) 대비 435건이 증가했다."
  - p12 Gyeongbuk delivery (분만) cases, 2025 = **5,890** delivery cases (2025-01-01..2025-12-31) [DISCARD: Gyeongbuk 2025 delivery count is a small regional component; same reasoning as p10.] quote: "지난해 5890건으로 전년(5811건) 대비 79건이 증가했다."
  - p13 Gyeongbuk delivery (분만) cases, 2024 = **5,811** delivery cases (2024-01-01..2024-12-31) [DISCARD: Gyeongbuk 2024 delivery count is only a base for the 2025 Gyeongbuk figure; redundant for the national target.] quote: "지난해 5890건으로 전년(5811건) 대비 79건이 증가했다."
  - p14 Gyeongbuk delivery (분만) cases, 2021 = **7,248** delivery cases (2021-01-01..2021-12-31) [DISCARD: Gyeongbuk 2021 delivery count is a historical regional level with no bearing on the July 2026 national monthly flow.] quote: "경북은 2021년 7248건에서 2025년 5890건으로 1358건이 줄었고"
  - p15 Jeju delivery (분만) cases, 2021 = **3,615** delivery cases (2021-01-01..2021-12-31) [DISCARD: Jeju 2021 delivery count is a historical regional level with no bearing on the July 2026 national monthly flow.] quote: "제주는 3615건에서 3122건으로 493건이 감소했다."
- `http://hirasabo.or.kr/240102/section1_4.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.mw.go.kr/boardDownload.es?bid=0020&list_no=264505&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.data.go.kr/data/15118813/fileData.do` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (number: more than one number in value_as_written: 8)

### d4 [base_rates] Demographic accounting from population and fertility rates

Hypothesis: Live births in July 2026 can be approximated by multiplying the estimated mid-2026 female population aged 20–39 by an age-specific fertility rate for July, adjusted for seasonality. This route requires population estimates and recent fertility rates.

Queries issued by the searcher: Statistics Korea population by age 2026 female 20-39; South Korea total fertility rate 2025 2026 monthly births; 2026년 6월 인구동향 출생아 수 23111명; 월별 출생아 수 2025년 7월 8월 9월 통계

- `https://www.ajupress.com/view/20260729142454222` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4840361?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.namu.wiki/w/%EC%84%B1%EB%B9%84/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.en.seoul.co.kr/news/society/2026/08/27/20260827010006?cp=en` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Policy and calendar effects on births

Hypothesis: Recent policy changes (e.g., parental benefits, housing support) or calendar effects (e.g., Lunar New Year timing, marriage trends) may have shifted the number of births in July 2026 relative to the historical trend. Quantifying these effects can adjust the extrapolation.

Queries issued by the searcher: South Korea monthly marriage registrations 2026 Statistics Korea; 혼인 건수 월별 2026 인구동향; South Korea birth policy 2026 parental benefits housing support; South Korea live births monthly 2026 Population Trends KOSTAT

- `https://mods.go.kr/board.es?mid=a20108090000&bid=11749&act=view&list_no=445396` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.gmw.cn/2026-06/27/content_1304511276.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://french.korea.net/NewsFocus/Society/view?articleId=289568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://japanese.korea.net/NewsFocus/Society/view?articleId=289564` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Official projections and analyst forecasts

Hypothesis: Statistics Korea or other institutions may have published monthly or quarterly birth projections for 2026 that can serve as a prior for July 2026, though these are forecasts rather than realized outcomes.

Queries issued by the searcher: Statistics Korea birth projection 2026 monthly live births; 2026년 출생아 수 전망 통계청; 장래인구추계 2022-2072 출생아 수 2026년 29만5000명 OECD 평균 시나리오; 2025년 7월 출생아 수 2만1844명 인구동향

- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/7
  - p16 South Korea cumulative live births growth rate, January–May of current year vs s = **15.2** percent (2026-01-01..2026-05-31) [DISCARD: Redundant duplicate of p3 (same 15.2% Jan-May 2026 cumulative growth from the same KOSTAT release, reported by a differe] quote: "올해 1~5월 누계 출생아 수는 전년 동기보다 15.2% 늘었다."
  - p17 South Korea total fertility rate, January = **0.99** children per woman (2026-01-01..2026-01-31) [keep: ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p18 South Korea total fertility rate, February = **0.93** children per woman (2026-02-01..2026-02-28) [keep: ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p19 South Korea total fertility rate, March = **0.93** children per woman (2026-03-01..2026-03-31) [keep: ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p20 South Korea total fertility rate, April = **0.93** children per woman (2026-04-01..2026-04-30) [keep: ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p21 South Korea total fertility rate, May = **0.85** children per woman (2026-05-01..2026-05-31) [DISCARD: Duplicate of p4 for May 2026 TFR; the eToday series p17–p20 already supplies the other months.] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p22 South Korea total fertility rate, previous year (2025) = **0.8** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "지난해 합계출산율(0.80명)은 데이터처의 '2022~2072년 장래인구추계'에 제시된 고위 가정(0.75명)을 넘어섰다."
- `https://www.newsworks.co.kr/news/articleView.html?idxno=848723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=AKR20251231132800002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020600&bid=207&tag=&act=view&list_no=428476&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (period_end 2026-12-31 after as_of: 2; number: unknown scale word '만': 1; period_end missing or unparseable: 1; number: more than one number in value_as_written: 3; period_end 2035-12-31 after as_of: 1)

### b1 [own_history] d1

Hypothesis: The single most valuable missing input is the KOSTAT monthly live-birth count for June 2026 (published around late August 2026) and, if available, the June 2025 comparison. June 2026 is the last month before the target and would let a YoY-scaling or naive-series route be anchored one month closer, sharply reducing the extrapolation error from May to July. It also tests whether the May 2026 TFR dip to 0.85 was seasonal or the start of a slowdown.

Queries issued by the searcher: KOSTAT 인구동향 2026년 6월 출생아 수; Statistics Korea monthly live births June 2026; 인구동향 2026년 5월 출생아 수 23,160명 발표; 2025년 7월 출생아 수 인구동향; 주민등록 출생신고 2026년 7월

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260826079400002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=297003` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] d2

Hypothesis: A monthly resident-registration (주민등록) birth-registration series for 2025–2026 would supply a coincident proxy for July 2026, since registrations for July births are largely filed by August. The needed conversion is the registration-to-vital-statistics ratio and the lag distribution; without that ratio the series cannot be used, so the search should target both the monthly registration counts and any published comparison of registration counts to KOSTAT live births.

Queries issued by the searcher: 행정안전부 주민등록 출생신고 월별 2026; 주민등록 인구통계 출생자 수 7월 2026; 출생신고 vs 출생아 수 차이 통계 주민등록 출생등록 통계청 인구동향 비교; 행안부 주민등록 출생등록 2026년 7월 전국 2만명

- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kosis.kr/civilComplaint/qnaDetail.do?boardIdx=23332` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10502020100&bid=3204&tag=&act=view&list_no=161932&ref_bid=` -> **snapshot** (snapshot 20260210112150); points raw/verified 0/0

### b3 [related_series] d3

Hypothesis: Monthly NHIS/HIRA delivery-claim counts for 2026 (or at least Q2 2026) would give a near-real-time check on the July 2026 birth level and let the annual delivery-case evidence (p9–p12) be converted into a monthly flow. The key missing coefficient is the stable ratio of delivery claims to KOSTAT live births; if that ratio is published or derivable, the July 2026 claim count becomes a direct proxy.

Queries issued by the searcher: 건강보험심사평가원 분만 청구 월별 2026; 국민건강보험 분만실적 2026년; 인구동향 2026년 7월 출생아 수 통계청; 분만 청구 건수 출생아 수 비율 건강보험; 2026년 5월 인구동향 출생아 수 전년동월대비; 건강보험 진료비통계지표 2026년 분만 자연분만 제왕절개 청구

- `https://medicalworldnews.co.kr/news/view.php?idx=1510977580&key_idx=5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://karm.or.kr/bbs/skin/notice_popup/download.php?code=notice&number=23845` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.doctorsnews.co.kr/news/articleView.html?idxno=166573` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.medipana.com/news/articleView.html?idxno=418629` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Same sentence, same measurement (May 2026 births level and its YoY change); p2 is the ratio form of p1. Not independent evidence, but jointly they pin the May 2026 level at 23,160 and the May 2025 bas
- corroborating: ['p3', 'p16'] Two outlets reporting the same KOSTAT January–May 2026 cumulative growth of 15.2%. Same underlying statistic, so this is one observation, not two.
- corroborating: ['p4', 'p5', 'p21'] May 2026 TFR of 0.85 and its +0.10 YoY change appear in both the Segye and eToday reports; same KOSTAT release, single underlying measurement.
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21'] Monthly TFR path for Jan–May 2026 from one article: 0.99, 0.93, 0.93, 0.93, 0.85. Internally consistent and consistent with p4/p5; useful for judging whether the May dip is seasonal or a break in tren
- corroborating: ['p6', 'p7'] May 2026 marriages down 1,392 (-6.4%) YoY; level and rate from the same sentence. Relevant as a leading indicator for births roughly 9–15 months later, i.e. mostly beyond July 2026, so it constrains t
- contextual: ['p8'] Natural decrease of 6,413 in May 2026 implies deaths of 29,573; consistent with the birth level in p1 and useful only as a coherence check on the same release.
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] NHIS/HIRA-type delivery-case counts for 2024–2025 (national total plus Sejong, Gyeongbuk, Jeju). They corroborate the direction of the 2025–2026 birth upturn and give a level anchor for 2025, but they
- contextual: ['p22'] 2025 annual TFR of 0.80 versus the 2026 monthly TFRs of 0.85–0.99 shows the 2026 upturn is real and large; it also warns that monthly TFRs are noisy and seasonally shaped, so the May 0.85 should not b
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] Same May 2026 KOSTAT release: p1 is the absolute YoY increase and p2 the implied growth rate; they are two expressions of one measurement, not independent evidence.
- corroborating: ['p3', 'p16'] Both report the same 15.2% cumulative Jan-May 2026 growth figure, evidently from the same KOSTAT release; p16 is a duplicate restatement, not an independent source.
- corroborating: ['p4', 'p5', 'p21'] All three give May 2026 TFR = 0.85 (p5 adds the +0.10 YoY change); p4 and p21 are the same KOSTAT value reported by two outlets.
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21'] Monthly TFR path Jan-May 2026 from one KOSTAT release: 0.99, 0.93, 0.93, 0.93, 0.85. The May drop is a within-year seasonal pattern (May TFR is typically the lowest month), not necessarily a break in 
- corroborating: ['p1', 'p4'] Birth count up 13.6% YoY and TFR up 0.10 YoY in the same month are mutually consistent; both come from the same release so they share a single underlying measurement.
- corroborating: ['p6', 'p7'] Same May 2026 marriage statistic (20,368 cases, -1,392, -6.4%); one measurement, two expressions. Marriages are a leading indicator for births roughly 9-15 months later, so May 2026 marriages bear mai
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] All from one NHIS/HIRA-based delivery-case article: national 2025 deliveries 252,000 (+6.1% vs 237,484 in 2024), with regional detail. They share one underlying measurement system and one publication,
- corroborating: ['p9', 'p3'] Delivery cases +6.1% in 2025 and live births +15.2% in Jan-May 2026 point the same way (a rebound), but they cover different periods and different measurement systems (claims vs vital statistics), so 
- contextual: ['p8'] Natural decrease of 6,413 in May 2026 implies deaths of 29,573; combined with p1's 23,160 births this is internally consistent with the same release and confirms the birth level, but adds no independe

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 live births relative to July 2025 live births | 1.13 | 1.04..1.23 | 0.7997..1.599 (widened) | ratio | m1 (m1) | The only pre-cutoff KOSTAT evidence on the 2026 birth level is the May 2026 YoY increase of 13.6% (p1/p2) and the Jan-May cumulative increase of 15.2% (p3). July 2026 is two months beyond the last observed month, so the YoY factor is centered slightly below the May figure to allow for mean reversion | The 2026 birth rebound observed through May continues into July at a somewhat attenuated pace, and no new shock (e.g., a policy change or a sharp marriage decline) intervenes between May and July 2026. | A June 2026 KOSTAT release showing YoY growth falling to near zero or turning negative, or a documented break in the registration/occurrence relationship for mid-2026. |
| a2 | July seasonal index relative to the annual average month | 0.97 | 0.93..1.01 | 0.6853..1.371 (widened) | ratio | unused | Korean monthly births show a mild seasonal pattern with July typically slightly below the annual average month (autumn and winter months are higher). The value is a dimensionless seasonal factor applied to an annualized level; it is not a level of the target and is not supplied by any kept point. | The historical July seasonal pattern of Korean live births remains broadly stable in 2026. | Evidence that the 2026 monthly seasonal profile has shifted materially (e.g., a documented change in conception timing or in the registration-to-occurrence lag). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,154 | ['p1'] / ['a1'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a | ['p3'] / ['a2'] | [] |  | 0.00 |  | formula names ['a2', 'k_months_per_year', 'p3'] != inputs ['a2', 'p3'] |

Result: central **3,154**, 80% interval [2,135, 4,660], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first reported by Statistics Korea's monthly Population Trends release, is 3,154 persons. The interval is 2,135 to 4,660, a model-based range conditional on the assumptions rather than a demonstrated accuracy guarantee.

The estimate rests on one method (1 method, weight 100%). It anchors on the observed May 2026 year-over-year increase and scales it by an assumed July 2026 year-over-year factor of 1.13 (range 0.7997 to 1.599). The May increment is observed; the July factor is an analyst assumption, centered below the May figure to allow mean reversion.

The main risk is that this assumed factor is wrong, since July 2026 lies beyond the last observed month. The most useful missing evidence would be June 2026 or early-July registration data, which could replace the assumption with observation.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 live births relative to July 2025 live births: 1.13 ratio, range 0.7997 to 1.599 (range widened by code); used by m1. Overturned by: A June 2026 KOSTAT release showing YoY growth falling to near zero or turning negative, or a documented break in the registration/occurrence relationship for mid-2026.

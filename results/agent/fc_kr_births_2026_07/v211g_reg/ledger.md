# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in Statistics Korea's monthly Population Trends (인구동향) release | unit live births | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), monthly Population Trends / 인구동향

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly series

Hypothesis: July 2026 births = July 2025 births adjusted by the recent year-on-year trend in monthly births; July has a distinct seasonal level relative to adjacent months.

Queries issued by the searcher: Statistics Korea monthly live births 2025 인구동향 출생아 수; South Korea monthly births July 2025 Statistics Korea population trends; 2026년 6월 인구동향 출생아 수 국가데이터처; "2026년 5월 인구동향" 출생아 수 전년 동월 대비

- `https://www.koreatimes.co.kr/southkorea/society/20250924/koreas-childbirths-rise-for-13th-consecutive-month-in-july-data` -> **snapshot** (snapshot 20250924045410); points raw/verified 15/14
  - p1 Live births in South Korea, July (latest year reported) = **21,803** live births (2025-07-01..2025-07-31) [keep: ] quote: "A total of 21,803 babies were born in July, up 5.9 percent from 20,580 babies born a year earlier"
  - p2 Year-on-year growth rate of July live births in South Korea = **5.9** % (2025-07-01..2025-07-31) [keep: ] quote: "A total of 21,803 babies were born in July, up 5.9 percent from 20,580 babies born a year earlier"
  - p3 Cumulative live births in South Korea, January-July = **147,804** live births (2025-01-01..2025-07-31) [keep: ] quote: "A total of 147,804 babies were born between January and July."
  - p4 Year-on-year growth rate of cumulative January-July live births in South Korea = **7.2** % (2025-01-01..2025-07-31) [keep: ] quote: "The figure represents a 7.2 percent increase from the same period last year, the highest growth rate since 1981."
  - p5 Total fertility rate in South Korea, July = **0.8** children per woman (2025-07-01..2025-07-31) [keep: ] quote: "rose 0.04 from a year earlier to 0.8 in July"
  - p6 Year-on-year change in total fertility rate in South Korea, July = **0.04** children per woman (change) (2025-07-01..2025-07-31) [DISCARD: Redundant with p5 (same July TFR change); adds no independent information.] quote: "rose 0.04 from a year earlier to 0.8 in July"
  - p7 Marriages in South Korea, July = **20,394** marriages (2025-07-01..2025-07-31) [keep: ] quote: "The number of marriages in July climbed 8.4 percent on-year to 20,394, marking the 16th consecutive month of growth."
  - p8 Year-on-year growth rate of marriages in South Korea, July = **8.4** % (2025-07-01..2025-07-31) [keep: ] quote: "The number of marriages in July climbed 8.4 percent on-year to 20,394"
  - p9 Marriages in South Korea, July 2016 (comparison year) = **21,154** marriages (2016-07-01..2016-07-31) [keep: ] quote: "the largest number for any July since 2016, when the figure came to 21,154"
  - p10 Deaths in South Korea, July = **27,979** deaths (2025-07-01..2025-07-31) [DISCARD: Deaths are irrelevant to the live-birth target.] quote: "the number of deaths in July dropped 0.7 percent from a year earlier to 27,979"
  - p11 Year-on-year change in deaths in South Korea, July = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Deaths change irrelevant to births.] quote: "the number of deaths in July dropped 0.7 percent from a year earlier to 27,979"
  - p12 Natural population decline in South Korea, July (deaths minus births) = **6,175** persons (2025-07-01..2025-07-31) [DISCARD: Natural decline is a derived deaths-minus-births figure, not a birth input.] quote: "resulting in a natural population decline of 6,175"
  - p13 Divorces in South Korea, July = **7,826** divorces (2025-07-01..2025-07-31) [DISCARD: Divorces irrelevant to births.] quote: "The number of divorces fell 1.4 percent on-year to 7,826 in July"
  - p14 Year-on-year change in divorces in South Korea, July = **1.4** % (2025-07-01..2025-07-31) [DISCARD: Divorce change irrelevant to births.] quote: "The number of divorces fell 1.4 percent on-year to 7,826 in July"
- `https://www.heraldk.com/article/2026082520003478163` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11749&list_no=437779&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] Administrative registration data

Hypothesis: Resident registration (주민등록) birth registrations and birth-related administrative counts track the statistics-agency birth series with a stable ratio and lag, allowing a bridge to the July 2026 occurrence count.

Queries issued by the searcher: 주민등록 출생자 수 월별 2026 행정안전부; resident registration births Korea monthly 2026 행정안전부 인구통계; 행안부 주민등록 출생자 수 2026년 7월 출생등록; 주민등록 출생등록 통계청 출생아 수 비율 비교 2025 2026

- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jumin.mois.go.kr/` -> **snapshot** (snapshot 20260717112850); points raw/verified 0/0
- `http://overtherainbow.korea.kr/docViewer/skin/doc.html?fn=48a08d32f0cc5e4d5ae53e1ef0f48d41&rs=/docViewer/result/2026.06/24/48a08d32f0cc5e4d5ae53e1ef0f` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Health insurance / birth-related claims

Hypothesis: National Health Insurance Service (NHIS) counts of births/deliveries (분만 건수) provide an independent monthly proxy for live births, bridged by the historical ratio of NHIS delivery claims to KOSTAT births.

Queries issued by the searcher: 건강보험 분만 건수 월별 2026 통계; NHIS 분만실적 월별 통계 출산 급여 건수; 공공데이터포털 건강보험심사평가원 분만 통계 월별 2025 다운로드; 2026년 7월 출생아 수 인구동향 통계청

- `https://opendata.hira.or.kr/op/opb/selectRfrmList.do?rfrmTpCd=&searchCnd=&searchWrd=&sno=0&pageIndex=2` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hirasabo.or.kr/240102/section1_4.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nabo.go.kr/system/common/JSPservlet/download.jsp?fCode=33318753&fSHC=&fName=NABO+%EC%9D%B8%EA%B5%AC%C2%B7%EA%B3%A0%EC%9A%A9%EB%8F%99%ED%96` -> **snapshot** (snapshot 20250824103837); points raw/verified 15/10
  - p15 NHIS delivery (분만자) count, South Korea, 2024 = **235,000** persons (분자) (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p16 KOSTAT live births, South Korea, 2024 = **238,000** live births (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p17 Ratio of NHIS delivery count to KOSTAT live births, 2024 = **98.6** % (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p18 KOSTAT live births, South Korea, 2023 = **230,000** live births (2023-01-01..2023-12-31) [keep: ] quote: "2023년 23.0만명이던 출생아 수는 2024년 23.8만명으로 증가"
  - p19 KOSTAT live births, South Korea, 2025 May = **20,309** live births (2025-05-01..2025-05-31) [keep: ] quote: "5월 출생아 수는 20,309명으로 전년동월대비 762명(3.9%) 증가"
  - p20 KOSTAT live births year-on-year change, South Korea, 2025 May = **762** live births (2025-05-01..2025-05-31) [DISCARD: Redundant with p19 (same May 2025 figure and its YoY change).] quote: "5월 출생아 수는 20,309명으로 전년동월대비 762명(3.9%) 증가"
  - p21 NHIS 임신 바우처 분만 예정자 수, South Korea, 2025 (forecast basis) = **304,000** persons (분 예정자) (2025-01-01..2025-12-31) [keep: ] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p22 NHIS 임신 바우처 분만 예정자 수, South Korea, 2024 = **283,000** persons (분 예정자) (2024-01-01..2024-12-31) [keep: ] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p23 Ratio of KOSTAT live births to 임신 바우처 분만 예정자 수, South Korea, 2024 = **82.4** % (출생아 / 분만 예정자) (2024-01-01..2024-12-31) [keep: ] quote: "28.9 82.4 23.8"
  - p24 NHIS 임신 바우처 분만 예정자 수 year-on-year increase, South Korea, 2025 = **7.2** % (2025-01-01..2025-12-31) [keep: ] quote: "2025년 분만 예정자 수는 2024년 대비 7.2% 증가하여 출산율 반등 추세를 이어갈 것으로 전망"
- `https://www.data.go.kr/data/15118813/fileData.do` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (scale word '만' not supported by quote or table header: 5)

### d4 [base_rates] Demographic accounting

Hypothesis: July 2026 births ≈ women of childbearing age × age-specific fertility rates for July, or annual births × July seasonal share; the seasonal share of July within the year is stable.

Queries issued by the searcher: Statistics Korea monthly live births July 2025 Population Trends 인구동향; 출생아 월별 구성비 7월 2024 통계청; 2026년 6월 인구동향 출생아 수 2026년 8월 발표; 2026년 출생아 수 전망 상반기 누계 출생아; KOSIS 월별 출생아 수 2020 2021 2022 2023 2024 2025; 2026년 5월 인구동향 출생아 수 2026년 7월 발표; 2026년 1~5월 누계 출생아 수; 2026년 출생아 수 전망 통계청 2026

- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000056178&listChk=list&backUrl=https%3A%2F%2Fnsp.nanet.go.kr%2Fsearch%2Flist` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m-jp.yna.co.kr/view/AJP20250924002800882?section=society-culture/index` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www6.seoul.co.kr/news/society/2025/09/25/20250925014008` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Official and analyst projections

Hypothesis: Published 2026 birth projections or year-to-date commentary (e.g., KOSTAT, Bank of Korea, research institutes) constrain the plausible July 2026 level and the direction of the 2026 trend.

Queries issued by the searcher: 2026년 출생아 수 전망 통계청; South Korea 2026 births forecast monthly; 2025년 7월 출생아 수 2만명 인구동향; 2026년 6월 인구동향 출생아 수 발표

- `https://www.donga.com/news/article/all/20250924/132453847/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260802035341); points raw/verified 15/1
  - p25 South Korea late-20s age-specific fertility rate relative to late-30s (share) = **0.3333** as written "3분의 1", value check pending ratio (not stated (page dated 2026-08-02)) [DISCARD: Age-specific fertility ratio is not usable without age-structure data and is not needed for the chosen routes.] quote: "20대 후반 출산율(해당연령 여자인구 1000명당 출생아 수)은 30대 후반의 3분의 1 수준에 정체돼 있고"
- `https://www.newsworks.co.kr/news/articleView.html?idxno=848723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (period_end 2026-12-31 after as_of: 4; period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period year 2025 does not appear in the page text or URL (likely mis-dated): 4)

### d6 [shocks] Policy and calendar effects

Hypothesis: Policy changes (e.g., expanded parental benefits, marriage/childbirth incentives) and calendar effects (lunar dates, holidays) shift monthly births; measurable exposure helps adjust the trend extrapolation.

Queries issued by the searcher: Korea monthly live births 2026 Statistics Korea 인구동향 월별 출생아 수; 혼인 건수 월별 2026 통계청; 2026년 5월 인구동향 출생아 수 혼인 건수 7월 29일 발표; 2025년 7월 출생아 수 21,854명 인구동향

- `https://m.yonhapnewstv.co.kr/news/AKR20260729110346y00` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://overtherainbow.korea.kr/docViewer/skin/doc.html?fn=48a08d32f0cc5e4d5ae53e1ef0f48d41&rs=/docViewer/result/2026.06/24/48a08d32f0cc5e4d5ae53e1ef0f` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chosun.com/economy/economy_general/2026/04/22/DMBJ2HALXRADPCZV3ZFUGFIKXQ/` -> **snapshot** (snapshot 20260422043002); points raw/verified 3/3
  - p26 Consecutive months of marriage growth (birth leading indicator) in South Korea,  = **22** months (2024-05-01..2026-01-31) [keep: ] quote: "출생 선행 지표 결혼 22개월 연속 늘다 올해 2월 꺾여"
  - p27 Live births in South Korea in February 2026, as reported = **22,898** live births (2026-02-01..2026-02-28) [keep: ] quote: "2월 출생아는 2만2898명으로 7년만 최대"
  - p28 Years since the last time February births in South Korea were this high (7-year  = **7** years (2026-02-01..2026-02-28) [DISCARD: A 'years since' descriptor, not a quantity usable in any method.] quote: "2월 출생아는 2만2898명으로 7년만 최대"
- `https://www.mk.co.kr/news/economy/12059075` -> **snapshot** (snapshot 20260528114426); points raw/verified 15/13
  - p29 South Korea Q1 2026 live births (quarterly total) = **75,013** live births (2026-01-01..2026-03-31) [keep: ] quote: "2026년 1분기 출생아는 7만 5013명으로, 전년 대비 14.8% 증가하며 통계 작성 이래 역대 최대 증가율과 증가폭을 기록했어요."
  - p30 South Korea Q1 2026 live births year-on-year increase (count) = **9,651** live births (2026-01-01..2026-03-31) [DISCARD: Redundant with p29/p31 (Q1 count and growth already captured).] quote: "올해 1분기 출생아는 7만 5013명으로 지난해 같은 기간보다 14.8%인 9651명 증가했습니다."
  - p31 South Korea Q1 2026 live births year-on-year growth rate = **14.8** % (2026-01-01..2026-03-31) [keep: ] quote: "2026년 1분기 출생아는 7만 5013명으로, 전년 대비 14.8% 증가하며 통계 작성 이래 역대 최대 증가율과 증가폭을 기록했어요."
  - p32 South Korea March 2026 live births (monthly) = **25,200** live births (2026-03-01..2026-03-31) [keep: ] quote: "특히 3월 출생아는 2만 5200명으로 1년 전보다 19.4%나 늘어, 3월 기준으로 역대 최대 증가율을 보였어요."
  - p33 South Korea March 2026 live births year-on-year growth rate = **19.4** % (2026-03-01..2026-03-31) [DISCARD: Redundant with p32 (March 2026 level and growth).] quote: "특히 3월 출생아는 2만 5200명으로 1년 전보다 19.4%나 늘어, 3월 기준으로 역대 최대 증가율을 보였어요."
  - p34 South Korea Q1 2026 marriage registrations (quarterly total) = **62,309** marriages (2026-01-01..2026-03-31) [keep: ] quote: "출생 증가의 선행 지표인 혼인 건수도 8년 만에 가장 많은 1분기 6만 2309건을 기록했으며"
  - p35 South Korea Q1 2026 marriage registrations year-on-year growth rate = **6.1** % (2026-01-01..2026-03-31) [DISCARD: Redundant with p34 (Q1 2026 marriage count).] quote: "2026년 1분기 혼인 건수는 전년 동기 대비 6.1% 증가하며 8년 만에 최고치를 기록했답니다."
  - p36 South Korea July 2024 live births (monthly) = **20,601** live births (2024-07-01..2024-07-31) [keep: ] quote: "7월 출생아 수도 2만 601명으로 1년 전보다 7.9% 증가하며, 2007년 7월 이후 최고 증가율을 보였어요."
  - p37 South Korea July 2024 live births year-on-year growth rate = **7.9** % (2024-07-01..2024-07-31) [DISCARD: Redundant with p36 (July 2024 level and growth).] quote: "7월 출생아 수도 2만 601명으로 1년 전보다 7.9% 증가하며, 2007년 7월 이후 최고 증가율을 보였어요."
  - p38 South Korea July 2024 marriage registrations (monthly) = **18,811** marriages (2024-07-01..2024-07-31) [keep: ] quote: "7월 혼인 건수는 1만 8811건으로 지난해 같은 기간보다 32.9% 늘며 1981년 월간 통계 작성 이후 7월 기준 최고 증가율을 기록했어요."
  - p39 South Korea July 2024 marriage registrations year-on-year growth rate = **32.9** % (2024-07-01..2024-07-31) [DISCARD: Redundant with p38 (July 2024 marriage level and growth).] quote: "7월 혼인 건수는 1만 8811건으로 지난해 같은 기간보다 32.9% 늘며 1981년 월간 통계 작성 이후 7월 기준 최고 증가율을 기록했어요."
  - p40 South Korea June 2024 live births (monthly) = **18,242** live births (2024-06-01..2024-06-30) [keep: ] quote: "6월 출생아 수는 1만 8242명으로 1년 전보다 1.8% 줄어, 관련 통계 작성 이래 6월 기준 역대 최소치를 기록했어요."
  - p41 South Korea Q2 2024 live births (quarterly total) = **56,838** live births (2024-04-01..2024-06-30) [DISCARD: Q2 2024 quarterly total is not needed and overlaps with monthly points already kept.] quote: "2024년 2분기 출생아 수는 1년 전보다 1.2% 증가한 5만 6838명으로 집계되었어요."
- dropped by code checks: 2 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b1 [related_series] administrative bridge

Hypothesis: Monthly NHIS 분만 (delivery) claim counts for Jan–Jun 2026, bridged by the 98.6% NHIS/KOSTAT ratio (p17), would give an independent July 2026 birth level and let us check whether the Q1 2026 surge (p29–p33) persisted into summer. This is the single most valuable missing input because it is the only route that does not rely on extrapolating the 2025 July level.

Queries issued by the searcher: 건강보험 분만자 수 2026년 월별; NHIS 분만 청구 건수 2026 출생아 수 비교; 2026년 5월 출생아 수 통계청 인구동향; 국민건강보험공단 분만 건수 2026년 상반기 증가

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260729067200002` -> **snapshot** (snapshot 20260730114307); points raw/verified 15/15
  - p42 South Korea monthly live births, May 2026 (first-reported KOSTAT Population Tren = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p43 South Korea cumulative live births, January–May 2026 = **122,694** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1∼5월까지는 12만2천694명이 태어났다."
  - p44 South Korea year-on-year increase in May 2026 live births (count) = **2,781** live births (2026-05-01..2026-05-31) [keep: ] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p45 South Korea year-on-year growth rate of May 2026 live births = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p46 South Korea year-on-year increase in cumulative Jan–May 2026 live births (count) = **16,166** live births (2026-01-01..2026-05-31) [keep: ] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p47 South Korea year-on-year growth rate of cumulative Jan–May 2026 live births = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p48 South Korea May live births, 2019 comparison year = **25,299** live births (2019-05-01..2019-05-31) [keep: ] quote: "출생아 규모는 5월 기준으로 2019년(2만5천299명) 이후 7년 만에 가장 많았다."
  - p49 South Korea cumulative Jan–May live births, 2019 comparison year = **134,433** live births (2019-01-01..2019-05-31) [keep: ] quote: "1∼5월 누적 규모는 2019년(13만4천433명) 이후 가장 많았고, 증가폭과 증가율 모두 통계 작성 시작 이래 가장 컸다."
  - p50 South Korea total fertility rate, May 2026 = **0.85** births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p51 South Korea year-on-year change in total fertility rate, May 2026 = **0.1** births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p52 South Korea share of May 2026 births that were first-order births = **63** % (2026-05-01..2026-05-31) [keep: ] quote: "출산 순위별 출생아 수 구성비는 첫째가 63.0%로 1.3%포인트(p) 늘었다."
  - p53 South Korea share of May 2026 births that were second-order births = **31.7** % (2026-05-01..2026-05-31) [keep: ] quote: "둘째는 31.7%로 0.2%p 감소했다."
  - p54 South Korea share of May 2026 births that were third-order or higher = **5.3** % (2026-05-01..2026-05-31) [keep: ] quote: "셋째 이상은 5.3%로 1.1%p 줄었다."
  - p55 South Korea monthly deaths, May 2026 = **29,573** deaths (2026-05-01..2026-05-31) [keep: ] quote: "5월 사망자 수는 2만9천573명으로 1년 전보다 1천91명(3.8%) 증가했다."
  - p56 South Korea natural decrease (deaths minus births), May 2026 = **6,413** persons (2026-05-01..2026-05-31) [keep: ] quote: "이에 따라 5월에는 6천413명이 자연감소했다."
- `https://data.edmgr.kr/dataView.do?id=www-data-go-kr-data-filedata-15118813` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://likms.assembly.go.kr/filegate/sender10?dummy=dummy&bookId=B5B54E74-DD6A-8603-D1E0-FFF7207496FB&type=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] monthly seasonality

Hypothesis: The July share of annual births and the July-vs-June and July-vs-August ratios in 2023–2025 would let us convert the strong Q1 2026 level into a July 2026 level without assuming the 2025 July YoY rate persists. July is typically a high-birth month (autumn conceptions), so a naive carry-forward of the Q1 growth rate may overstate July.

Queries issued by the searcher: 통계청 인구동향 2025년 7월 출생아 수 21,803; KOSTAT monthly live births July 2024 20,601 population trends; 인구동향조사 월별 출생아 수 2025년 8월 9월 10월 출생아 수 통계청; kostat.go.kr 인구동향 2025년 8월 출생아 수 2만 천명 전년동월대비

- `https://www.kostat.go.kr/boardDownload.es?bid=204&list_no=439018&seq=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jibs.co.kr/news/articles/articlesDetail/41409?feed=na` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/MYH20240925014900884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AFR20241023001600884?section=news` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] 2026 trend commentary

Hypothesis: Published 2026 birth projections or mid-2026 monthly commentary (e.g., KOSTAT Q2 2026 release, BOK, research institutes) would resolve whether the Q1 2026 +14.8% surge (p29–p31) moderated in Q2 — the key uncertainty in the trend-extrapolation route. If Q2 growth fell back toward single digits, July 2026 should be scaled down accordingly.

Queries issued by the searcher: 통계청 인구동향 2026년 6월 출생아 수; KOSTAT monthly population trends 2026 April June births year-on-year; "2026년 5월 인구동향" 출생아 수 23,160명 전년동월대비; 2025년 7월 출생아 수 명 통계청 인구동향

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6269788` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth rate', 'korea population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Same article: p1 is the July 2025 level and p2 its 5.9% YoY growth; internally consistent (21,803 vs 20,580). Both are KOSTAT provisional July figures reported by a news outlet, so they share one unde
- corroborating: ['p1', 'p3', 'p4'] Same release: July 2025 level (p1) and Jan–Jul 2025 cumulative (p3) with 7.2% growth (p4). Consistent in direction (strong 2025 rebound) and same source/vintage.
- corroborating: ['p5', 'p6'] July TFR 0.8 and +0.04 YoY are the same statistic; consistent with the birth growth in p1/p2.
- corroborating: ['p7', 'p8', 'p9'] July 2025 marriages 20,394 (+8.4%) and the 2016 comparison (21,154) are one series; marriage strength is a leading indicator for 2026 births.
- corroborating: ['p10', 'p11', 'p12'] Deaths 27,979, -0.7%, and natural decline 6,175 are arithmetically linked (27,979 - 21,803 ≈ 6,176). Not directly needed for births but confirms the release's internal consistency.
- corroborating: ['p15', 'p16', 'p17'] NHIS 2024 deliveries 235k vs KOSTAT 238k = 98.6%; same NABO document, so the ratio is a single measurement, not independent confirmation. Useful only as a bridge factor.
- corroborating: ['p21', 'p22', 'p24'] Voucher-based 분만 예정자 수 304k (2025) vs 283k (2024), +7.2%; same source. This is a pregnancy-intent/booking count, not a birth count, and its 2025 vintage is a forecast basis.
- corroborating: ['p23', 'p16', 'p22'] 82.4% = 23.8/28.9 in the same table; a conversion factor from voucher bookings to KOSTAT births, not an independent birth observation.
- corroborating: ['p27', 'p28'] February 2026 births 22,898, a 7-year high; same article. Shows the 2026 upswing continuing into Q1.
- corroborating: ['p29', 'p30', 'p31'] Q1 2026 = 75,013, +9,651, +14.8%; internally consistent and same release. Strong evidence of a 2026 level shift.
- corroborating: ['p32', 'p33'] March 2026 = 25,200, +19.4%; consistent with Q1 total (Jan+Feb+Mar ≈ 75,013 given p27).
- corroborating: ['p34', 'p35'] Q1 2026 marriages 62,309, +6.1%; supports continued birth momentum via the ~1-year marriage→birth lag.
- corroborating: ['p36', 'p37'] July 2024 = 20,601, +7.9%; consistent with p1's implied July 2024 base (20,580, small revision difference).
- corroborating: ['p38', 'p39'] July 2024 marriages 18,811, +32.9%; consistent with p7's July 2025 level (20,394) after another year of growth.
- corroborating: ['p40', 'p41'] June 2024 = 18,242 and Q2 2024 = 56,838; same release, consistent.
- conflicting: ['p1', 'p36'] Minor vintage conflict: p36 implies July 2024 ≈ 20,601 while p1's base is 20,580. Revisions of ~0.1% — immaterial, but shows the two articles use different vintages.
- conflicting: ['p26', 'p34'] p26 says the 22-month marriage growth streak broke in February 2026, while p34 reports Q1 2026 marriages +6.1% YoY. Not strictly contradictory (a single month can dip within a growing quarter), but it
- corroborating: ['p19', 'p20'] May 2025 = 20,309, +762 (+3.9%); same document, consistent. Provides a mid-2025 monthly anchor.
- corroborating: ['p18', 'p16'] 2023 = 230k, 2024 = 238k; same source, consistent annual series.
- corroborating: ['p25'] Age-specific fertility shape (late-20s ≈ 1/3 of late-30s) is context on the age structure of fertility; not a level input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p36'] All three describe July live births in South Korea on KOSTAT's occurrence basis: p1 gives July 2025 = 21,803, p2 its +5.9% YoY, and p36 gives July 2024 = 20,601. They are internally consistent (20,601
- corroborating: ['p3', 'p4', 'p43', 'p46', 'p47'] Cumulative Jan–Jul 2025 (p3, p4) and cumulative Jan–May 2026 (p43, p46, p47) are the same KOSTAT cumulative series in adjacent years; they establish the strong 2026 upswing and are consistent with the
- corroborating: ['p29', 'p31', 'p32', 'p42', 'p45', 'p47'] Q1 2026 +14.8% (p29/p31), March 2026 +19.4% (p32), May 2026 +13.6% (p42/p45) and cumulative Jan–May +15.2% (p47) all point to a sustained double-digit 2026 birth surge through spring. Same KOSTAT sour
- corroborating: ['p27', 'p29', 'p32', 'p42'] February 2026 (22,898), Q1 total (75,013), March (25,200) and May (23,160) are mutually consistent monthly/quarterly KOSTAT figures for 2026; they anchor the level of the 2026 surge.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p23'] NHIS delivery counts and KOSTAT annual births for 2023–2024 with the 98.6% NHIS/KOSTAT ratio and the 82.4% births/voucher ratio are internally consistent annual bridges. They are annual, not monthly, 
- corroborating: ['p21', 'p22', 'p24'] NHIS 임신 바우처 분만 예정자 counts for 2024 (283k) and 2025 forecast (304k, +7.2%) are a forward-looking administrative indicator consistent with the 2025 birth rebound; they are a forecast basis, not an outco
- corroborating: ['p7', 'p8', 'p9', 'p26', 'p34', 'p38'] Marriage registrations (July 2025 +8.4%, 22 consecutive growth months through Jan 2026, Q1 2026 62,309, July 2024 +32.9%) are a leading indicator consistent with the 2026 birth surge, with a typical ~
- corroborating: ['p19', 'p42'] May 2025 (20,309) and May 2026 (23,160) are the same monthly series one year apart; the implied +13.6% matches p45, confirming the 2026 acceleration.
- corroborating: ['p1', 'p36', 'p40'] June 2024 (18,242), July 2024 (20,601) and July 2025 (21,803) show July is seasonally a high-birth month relative to June, supporting a July seasonal uplift.
- corroborating: ['p5', 'p50', 'p51'] July 2025 TFR 0.8 and May 2026 TFR 0.85 (+0.10) are consistent with the birth surge; TFR is a rate, not a count, so it supports direction only.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 YoY birth growth factor relative to July 2025 | 1.08 | 0.98..1.2 | 0.9699..1.212 (widened) | ratio | m1 (m1) | 2026 monthly YoY growth has been double-digit (Q1 +14.8% p31, March +19.4% p32, May +13.6% p45, cumulative Jan–May +15.2% p47). July 2025 was already a strong base (+5.9%, p2), and July is seasonally high, so moderation from the spring peak is plausible; central 1.08 with a wide range spanning flat  | The 2026 surge persists into summer but moderates from the spring peak. | Q2 2026 monthly releases showing growth falling back to low single digits or turning negative. |
| a2 | July seasonal share of annual births | 0.086 | 0.08..0.092 | 0.06066..0.1213 (widened) | share | m2 (m2) | July is a seasonally high-birth month; roughly 1/12 of annual births with a modest uplift, consistent with July 2024 (20,601, p36) and July 2025 (21,803, p1) being above adjacent June (18,242, p40). Range reflects seasonal variation. | Annual births are distributed with a stable July seasonal share. | Evidence that July's share of annual births has shifted materially in 2025–2026. |
| a3 | 2026 annual live births relative to 2024 annual live births | 1.12 | 1.05..1.22 | 0.8003..1.601 (widened) | ratio | m2 (m2) | 2026 Jan–May births are +15.2% over 2025 (p47); 2025 was itself up ~7% over 2024 (p4, p18). A full-year 2026/2024 ratio of ~1.12 reflects the observed surge with some moderation in H2 as the 2025 base strengthens. | 2026 annual births run above 2024 by roughly the observed cumulative growth. | H2 2026 monthly releases showing growth collapsing toward zero. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 23,669 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 23,093 | ['p16'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **23,379** person, 80% interval [13,834, 39,510] person, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first provisionally reported in Statistics Korea's monthly Population Trends release, is 23,379 person (80% model-based interval 13,834 to 39,510 person; too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

Two methods were averaged with weights of 50% and 50%. Method [n] carries forward the observed July 2025 level of 21,803 live births adjusted by a July 2026 year-over-year growth factor of 1.08 (range 0.9699 to 1.212). Method [n] scales observed 2024 annual births of 238,000 live births by a 2026/2024 ratio of 1.12 (range 0.8003 to 1.601) and a July seasonal share of 0.086 (range 0.06066 to 0.1213). Only the two base levels are observed; the growth, ratio, and seasonal-share inputs are analyst assumptions, and the methods share the same 2026-surge premise, so they are not independent.

The main risk is that the double-digit 2026 surge moderates sharply before July, or that the seasonal share is off. Actual June and July 2026 monthly releases would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 YoY birth growth factor relative to July 2025: 1.08 ratio, range 0.9699 to 1.212 (range widened by code); used by m1. Overturned by: Q2 2026 monthly releases showing growth falling back to low single digits or turning negative.
- a2 July seasonal share of annual births: 0.086 share, range 0.06066 to 0.1213 (range widened by code); used by m2. Overturned by: Evidence that July's share of annual births has shifted materially in 2025–2026.
- a3 2026 annual live births relative to 2024 annual live births: 1.12 ratio, range 0.8003 to 1.601 (range widened by code); used by m2. Overturned by: H2 2026 monthly releases showing growth collapsing toward zero.

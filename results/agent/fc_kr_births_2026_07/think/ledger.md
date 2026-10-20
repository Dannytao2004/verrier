# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Provisional number of live births occurring in South Korea during July 2026, as first reported in Statistics Korea's monthly Population Trends release. | unit live births | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT)

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea historical vital-statistics series

Hypothesis: July live births follow a recurring seasonal slice of the recent monthly birth level; if provisional births in early 2026 are above or below their year-earlier counterparts, July 2026 should move in the same direction, subject to July-specific seasonality and reporting changes.

Queries issued by the searcher: 통계청 인구동향 월별 출생아 수 2025 2026; Statistics Korea monthly population trends live births 2026 June; 2025년 7월 인구동향 출생아 수 21,803명 통계청 보도자료; 7월 출생아 수 통계 2019 2020 2021 2022 2023 2024 명

- `https://mods.go.kr/board.es?act=view&bid=204&list_no=438748&mid=a10301020100` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.joongang.co.kr/article/25449289` -> **snapshot** (snapshot 20260814043421); points raw/verified 15/1
  - p1 South Korea cumulative live births, January-May 2019 = **134,433** live births (2019-01-01..2019-05-31) [keep: ] quote: "1~5월 누적 규모는 2019년(13만4433명) 이후 7년 만에 최대로, 증가폭과 증가율 모두 통계 작성 시작 이후 가장 컸다."
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20250924067700002` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (period year 2026 does not appear in the page text or URL (likely mis-dated): 11; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; value_as_written not in quote as a whole number: 1)

### d2 [administrative] Civil birth-registration office

Hypothesis: Monthly civil birth registrations track statistical live births with a registration lag; July 2026 registrations or partial registration counts can constrain the occurrence-based July estimate after adjusting for lag and completeness.

Queries issued by the searcher: 출생신고 현황 월별 2026; 가족관계등록 출생신고 통계 월별; 전자가족관계등록시스템 통계정보 지역별 출생신고 건수 월별; 아동수당 신청 현황 월별 2026 출생아

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.guri.go.kr/www/selectBbsNttList.do?key=351&bbsNo=21&searchCtgry=&searchCnd=SJ&searchKrwd=&integrDeptCode=&pageIndex=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bigdata.seoul.go.kr/data/selectSampleData.do?sample_data_seq=60` -> **snapshot** (snapshot 20251118110334); points raw/verified 0/0
- `https://www.gimhaeilbo.com/news/articleView.html?idxno=34519` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [forecasts_markets] Forecast publisher or research institute

Hypothesis: Published annual 2026 birth forecasts can be converted to a July estimate using historical July shares; the route constrains the annual level but depends on the forecast's definition and the stability of monthly seasonality.

Queries issued by the searcher: 2026년 출생아 수 전망; South Korea 2026 births forecast annual; 2025년 7월 출생아 수 명 인구동향 월별; 월별 출생아 수 2025 1월 2월 3월 4월 5월 6월 7월 8월 9월 10월 11월 12월 통계

- `https://en.wikipedia.org/wiki/Demographics_of_South_Korea` -> **snapshot** (snapshot 20260708133615); points raw/verified 15/14
  - p2 South Korea annual live births, 2025 (full-year actual) = **254,457** live births (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 \| 51,684,564 \| 254,457 \| 363,389 \| -108,931 \| 4.9 \| 7.0 \| -2.1 \| 0.800 \| 0.8 \|"
  - p3 South Korea annual live births, 2024 = **238,343** live births (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024[42] \| 51,751,065 \| 238,343 \| 358,356 \| -120,013 \| 4.7 \| 7.0 \| -2.3 \| 0.748 \| 3.1 \|"
  - p4 South Korea annual live births, 2023 = **230,028** live births (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023 \| 51,712,619 \| 230,028 \| 352,511 \| -122,483 \| 4.5 \| 6.9 \| -2.4 \| 0.721 \| 3.1 \|"
  - p5 South Korea annual live births, 2022 = **249,186** live births (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022 \| 51,672,569 \| 249,186 \| 372,939 \| -123,753 \| 4.9 \| 7.3 \| -2.4 \| 0.778 \| 0.5 \|"
  - p6 South Korea annual live births, 2021 = **260,562** live births (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021 \| 51,769,539 \| 260,562 \| 317,680 \| -57,118 \| 5.1 \| 6.2 \| -1.1 \| 0.808 \| -0.2 \|"
  - p7 South Korea annual live births, 2020 = **272,337** live births (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020 \| 51,836,239 \| 272,337 \| 304,948 \| -32,611 \| 5.3 \| 5.9 \| -0.6 \| 0.837 \| 2.0 \|"
  - p8 South Korea annual live births, 2019 = **302,676** live births (2019-01-01..2019-12-31) [keep: ] quote: "\| 2019 \| 51,764,822 \| 302,676 \| 295,132 \| 7,544 \| 5.9 \| 5.7 \| 0.2 \| 0.918 \| 3.3 \|"
  - p9 South Korea annual live births, 2018 = **326,822** live births (2018-01-01..2018-12-31) [keep: ] quote: "\| 2018 \| 51,585,058 \| 326,822 \| 298,820 \| 28,002 \| 6.4 \| 5.8 \| 0.6 \| 0.977 \| 3.8 \|"
  - p10 South Korea annual live births, 2017 = **357,771** live births (2017-01-01..2017-12-31) [keep: ] quote: "\| 2017 \| 51,361,911 \| 357,771 \| 285,534 \| 72,237 \| 7.0 \| 5.6 \| 1.4 \| 1.052 \| 1.4 \|"
  - p11 South Korea annual live births, 2016 = **406,243** live births (2016-01-01..2016-12-31) [keep: ] quote: "\| 2016 \| 51,217,803 \| 406,243 \| 280,827 \| 125,416 \| 7.9 \| 5.5 \| 2.5 \| 1.172 \| 1.3 \|"
  - p12 South Korea annual live births, 2015 = **438,420** live births (2015-01-01..2015-12-31) [keep: ] quote: "\| 2015 \| 51,024,947 \| 438,420 \| 275,895 \| 162,525 \| 8.6 \| 5.4 \| 3.2 \| 1.239 \| 1.1 \|"
  - p13 South Korea live births, January–June 2026 (partial-year cumulative) = **146,162** live births (2026-01-01..2026-06-30) [keep: ] quote: "\| January-June 2026 \| 146,162 \| \| \|"
  - p14 South Korea live births, January–June 2025 (partial-year cumulative) = **127,184** live births (2025-01-01..2025-06-30) [keep: ] quote: "\| January-June 2025 \| 127,184 \| \| = \|"
  - p15 South Korea year-on-year change in January–June live births, 2026 vs 2025 = **18,978** as written "+18,978 (+14.94%)", value check pending % (2026-01-01..2026-06-30) [keep: ] quote: "\| Difference \| +18,978 (+14.94%) \| \| \|"
- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/0
- `https://www.mt.co.kr/economy/2025/09/24/2025092408343697171` -> **snapshot** (snapshot 20250924034408); points raw/verified 15/14
  - p16 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 출생아는 2만1803명으로 전년 동월 대비 5.9%(1223명) 증가했다."
  - p17 South Korea live births, July 2025, year-on-year increase = **1,223** live births (2025-07-01..2025-07-31) [DISCARD: Derived July 2025 year-on-year increase from p16; redundant, adds no independent information.] quote: "지난 7월 출생아는 2만1803명으로 전년 동월 대비 5.9%(1223명) 증가했다."
  - p18 South Korea live births, July 2025, year-on-year growth rate = **5.9** % (2025-07-01..2025-07-31) [keep: July 2025 yoy growth (5.9%) is the measurable July-versus-cumulative growth gap that calibrates the damping assumption a] quote: "지난 7월 출생아는 2만1803명으로 전년 동월 대비 5.9%(1223명) 증가했다."
  - p19 South Korea live births, July 2021 (comparison year) = **22,364** live births (2021-07-01..2021-07-31) [keep: ] quote: "2021년 7월(2만2364명) 이후 4년 만에 7월 기준 가장 많은 아이가 태어났다."
  - p20 South Korea cumulative live births, January-July 2025 = **147,804** live births (2025-01-01..2025-07-31) [keep: ] quote: "1~7월 누적 출생아 수는 14만7804명으로 전년 동기(13만7860명)보다 7.2% 증가했다."
  - p21 South Korea cumulative live births Jan-Jul 2025, year-on-year growth rate = **7.2** % (2025-01-01..2025-07-31) [keep: Jan-Jul 2025 cumulative growth (7.2%) is the companion half of the July-vs-cumulative growth comparison that anchors a1 ] quote: "1~7월 누적 출생아 수는 14만7804명으로 전년 동기(13만7860명)보다 7.2% 증가했다."
  - p22 South Korea total fertility rate, July 2025 = **0.8** births per woman (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 합계출산율은 0.80명으로 전년 동월 대비 0.04명 증가했다."
  - p23 South Korea total fertility rate, January 2025 = **0.88** births per woman (2025-01-01..2025-01-31) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p24 South Korea total fertility rate, February 2025 = **0.82** births per woman (2025-02-01..2025-02-28) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p25 South Korea total fertility rate, March 2025 = **0.77** births per woman (2025-03-01..2025-03-31) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p26 South Korea total fertility rate, April 2025 = **0.79** births per woman (2025-04-01..2025-04-30) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p27 South Korea total fertility rate, May 2025 = **0.75** births per woman (2025-05-01..2025-05-31) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p28 South Korea total fertility rate, June 2025 = **0.76** births per woman (2025-06-01..2025-06-30) [keep: ] quote: "△1월 0.88명 △2월 0.82명 △3월 0.77명 △4월 0.79명 △5월 0.75명 △6월 0.76명 △7월 0.80명이다."
  - p29 South Korea crude birth rate, July 2025 = **5** births per 1,000 people (2025-07-01..2025-07-31) [keep: ] quote: "인구 1000명당 출생아수를 의미하는 조(粗)출생율은 5.0명을 기록하며 전년 대비 0.2명 늘었다."
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=AKR20251231132800002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 17 (period_end 2026-12-31 after as_of: 5; period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end 2035-12-31 after as_of: 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d4 [related_series] Marriage-registration and fertility demographer

Hypothesis: Marriages lead first births by roughly a gestation-plus-conception interval, so marriage registrations in late 2025 and early 2026 should provide a directional signal for July 2026 births; the transfer assumes Korea's birth-marriage linkage remains strong.

Queries issued by the searcher: 혼인건수 월별 2025 2026 통계청; Korea monthly marriage registrations 2025 2026 KOSTAT statistics; 2025년 10월 인구동향 혼인건수 전년동월대비 증가; 출생아 수 혼인 건수 상관관계 시차 9개월 회귀분석

- `https://m.korea.kr/briefing/pressReleaseView.do?newsId=156736731&pWise=mSub&pWiseSub=C8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/briefing/policyBriefingView.do?newsId=156749798&pWise=mSub&pWiseSub=C3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.khan.co.kr/en/article/202607291529057` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stock.mk.co.kr/news/view/1069388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] Health insurer and maternity-service provider

Hypothesis: Delivery-related medical claims or hospital delivery cases approximate the number of births, with coverage differences for foreign residents and timing lags between delivery and claim; recent claim volumes can indicate July 2026 delivery activity.

Queries issued by the searcher: 분만 청구 건강보험 월별 통계 2026; HIRA delivery claims monthly Korea childbirth statistics; 2026년 6월 출생아 수 통계청 월간 인구동향; 건강보험심사평가원 분만 건수 월별 2026년 상반기; 2026년 5월 인구동향 출생아 수 전년동월대비; 2025년 7월 출생아 수 명 통계청 인구동향

- `https://www.nabo.go.kr/system/common/JSPservlet/download.jsp?fCode=33318753&fSHC=&fName=NABO+%EC%9D%B8%EA%B5%AC%C2%B7%EA%B3%A0%EC%9A%A9%EB%8F%99%ED%96` -> **snapshot** (snapshot 20250824103837); points raw/verified 14/12
  - p30 National Health Insurance delivery claimants (분만자 수), South Korea, 2024 = **235,000** delivery claimants (persons) (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p31 Statistics Korea live births, South Korea, 2024 = **238,000** live births (2024-01-01..2024-12-31) [DISCARD: Rounded 2024 KOSTAT live-birth total already represented by p3; p32 supplies the useful coverage ratio.] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p32 Ratio of NHI delivery claimants to Statistics Korea live births, 2024 = **98.6** % (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p33 Statistics Korea live births, South Korea, 2023 = **230,000** live births (2023-01-01..2023-12-31) [DISCARD: Rounded 2023 KOSTAT live-birth total already represented by p4.] quote: "2023년 23.0만명이던 출생아 수는 2024년 23.8만명으로 증가"
  - p34 Total delivery rate (합계분만율), all NHI, 2024 = **0.7** deliveries per woman (2024-01-01..2024-12-31) [keep: ] quote: "2024년 합계분만율은 0.70명으로 2023년 대비 0.03명 증가했으며, 2024년 합계출산율은 0.75명으로 전년대비 0.03명 증가하여 동일한 추세를 보임"
  - p35 Total fertility rate (합계출산율), South Korea, 2024 = **0.75** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "2024년 합계출산율은 0.75명으로 전년대비 0.03명 증가하여 동일한 추세를 보임"
  - p36 Ratio of live births to pregnancy-voucher expected delivery persons, 2021-2024 = **82** % (2021-01-01..2024-12-31) [keep: ] quote: "2021~2024년간 분만 예정자 대비 출생아 수 비율은 82% 수준에서 차이를 보여주고 있음"
  - p37 Pregnancy-voucher expected delivery persons (분만 예정자), 2025 (Jan-May applications = **304,000** expected delivery persons (2025-01-01..2025-12-31) [keep: ] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p38 Pregnancy-voucher expected delivery persons (분만 예정자), 2024 (Jan-May applications = **283,000** expected delivery persons (2024-01-01..2024-12-31) [keep: ] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p39 Year-on-year increase in pregnancy-voucher expected delivery persons, 2025 vs 20 = **7.2** % (2025-01-01..2025-12-31) [keep: ] quote: "2025년 분만 예정자 수는 2024년 대비 7.2% 증가하여 출산율 반등 추세를 이어갈 것으로 전망"
  - p40 Year-on-year increase in pregnancy-voucher expected delivery persons, Jan-Apr 20 = **8.3** % (2025-01-01..2025-04-30) [keep: ] quote: "2025년 1~4월 분만 예정자 수는 2024년 같은 기간 대비 8.3% 증가"
  - p41 Year-on-year increase in live births, Jan-Apr 2025 vs Jan-Apr 2024 = **7.6** % (2025-01-01..2025-04-30) [keep: ] quote: "2025년 1~4월 출생아 수는 2024년 1~4월 출생아 수 대비 7.6% 증가하여 분만 예정자 수와 차이가 존재"
- `https://likms.assembly.go.kr/filegate/sender10?dummy=dummy&bookId=B5B54E74-DD6A-8603-D1E0-FFF7207496FB&type=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mw.go.kr/boardDownload.es?bid=0003&list_no=1490008&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://data.edmgr.kr/dataView.do?id=www-data-go-kr-data-filedata-15118813` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (scale word '만' not supported by quote or table header: 2)

### d6 [administrative] Child-benefit program administrator

Hypothesis: Applications for universal birth-related vouchers or child benefits are filed shortly after birth and can proxy live births, though eligibility and application timing introduce coverage and lag errors.

Queries issued by the searcher: 첫만남이용권 신청 월별 통계 2025; First Meeting Voucher applications monthly Korea birth statistics; 2026년 6월 출생아 수 인구동향 국가데이터처; 2026년 7월 출생아 수 증가; 2026년 5월 인구동향 출생아 수 전년동월대비 증가 국가데이터처; 2025년 7월 출생아 수 2만명 인구동향

- `http://www.joongboo.com/news/articleView.html?idxno=363704450` -> **snapshot** (snapshot 20251026074130); points raw/verified 16/2
  - p42 Incheon live births, full year 2024 = **15,242** as written "1만5천242명", value check pending live births (2024-01-01..2024-12-31) [DISCARD: Incheon regional births, not national monthly July 2026 target; limited transferability.] quote: "지난해 인천시 출생아 수는 1만5천242명으로, 1년 전인 2023년보다 11.6% 증가해 전국에서 가장 높은 상승률을 기록했다."
  - p43 Incheon live births year-on-year growth, 2024 vs 2023 = **11.6** % (2024-01-01..2024-12-31) [DISCARD: Incheon regional growth rate, same regional-scope limitation.] quote: "지난해 인천시 출생아 수는 1만5천242명으로, 1년 전인 2023년보다 11.6% 증가해 전국에서 가장 높은 상승률을 기록했다."
- `https://repo.kicce.re.kr:443/bitstream/2019.oak/5504/2/OR2308.pdf` -> **snapshot** (snapshot 20250803054147); points raw/verified 15/9
  - p44 Usable voucher amount (total) for First Meeting Voucher, 2022.4–2023.3, Korea = **607,200,000,000** KRW (2022-04-01..2023-03-31) [DISCARD: Voucher spending total, not a birth count; period and scope do not map to July 2026 live births.] quote: "사용 가능 바우처 6072억 원 중 약 5433억원이 실제 사용되었다고 발표하였다"
  - p45 Actually used voucher amount, 2022.4–2023.3, Korea = **543,300,000,000** KRW (2022-04-01..2023-03-31) [DISCARD: Voucher amount actually used, not a birth count; same scope/period mismatch.] quote: "사용 가능 바우처 6072억 원 중 약 5433억원이 실제 사용되었다고 발표하였다"
  - p46 Voucher amount per child under First Meeting Voucher = **2,000,000** KRW (2022-04-01..2023-12-31) [DISCARD: Per-child voucher amount, not a birth count; no usable bridge to July 2026 national births.] quote: "부모(보호자)가 출생신고하면 자녀 1명당 200만 원 바우처를 국민행복카드로 지급받는데"
  - p47 First Meeting Voucher full-spend population, 2022 (Jan–Dec), Korea = **194,553** people (2022-01-01..2022-12-31) [DISCARD: Full-spend voucher population, not total live births; different definition and 2022 period.] quote: "전체 194,553 69,322"
  - p48 First Meeting Voucher full-spend population, 2023 (Jan–Jun), Korea = **69,322** people (2023-01-01..2023-06-30) [DISCARD: Full-spend voucher population for Jan-Jun 2023, not a birth count; not applicable to July 2026.] quote: "전체 194,553 69,322"
  - p49 First Meeting Voucher full-spend population with contactable phone numbers, 2023 = **14,541** people (2023-01-01..2023-06-30) [DISCARD: Contactable survey subset of voucher users, not births; survey coverage issue.] quote: "2023년도 첫만남이용권 소진자 전체 모집단에서 연락처(핸드폰번호)가 있는 사례 14,541명을 추출하여"
  - p50 Pre-application submissions for First Meeting Voucher (as of 2022-03-31), Korea = **48,563** applications (2022-01-03..2022-03-31) [DISCARD: Voucher pre-applications as of 2022-03-31, not births; historical program administration.] quote: "사전신청 기간 동안 현장 및 온라인으로 접수된 총 48,563건(2022. 3. 31. 기준)에 대해 첫만남"
  - p51 Share of survey respondents who applied for voucher at birth registration (visit = **69.9** % (2023-01-01..2023-06-30) [DISCARD: Survey share applying at birth registration, not a birth count.] quote: "방문 신청이 69.9%로 높은 비율을 차지하였다"
  - p52 Share of survey respondents who applied online for voucher = **30.2** % (2023-01-01..2023-06-30) [DISCARD: Survey share applying online, not a birth count.] quote: "그러나 온라인 신청도 30.2%로 전체 신청의 1/3 정도를 차지하고 있음을 확인할 수 있었다"
- `https://neverolds.com/45` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.etoday.co.kr/news/view/2626148?trc=right_categori_news` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 20 (period year 2025 does not appear in the page text or URL (likely mis-dated): 10; number: scale conflict: '천만' in value vs '억': 4; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3; number: scale conflict: '천' in value vs '만': 1; period_end missing or unparseable: 2)

### d7 [base_rates] Population projection demographer

Hypothesis: Annual births can be decomposed into age-specific fertility rates times the female population of childbearing ages; this structural route constrains whether a monthly July figure is plausible relative to the 2025-2026 fertile population and fertility level.

Queries issued by the searcher: 2025 합계출산율 연령별 출산율 통계청; KOSTAT age-specific fertility rate 2025 total fertility rate 0.75; 2026년 6월 출생아 수 인구동향 월별 출생아; 2026년 가임여성 인구 20대 30대 여성 인구 추계; "2025년 7월" 출생아 수 인구동향 2만 명; 장래인구추계 2025 2026 여성 인구 30~34세 35~39세 명 통계청

- `https://www.korea.kr/common/download.do?fileId=198368726` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ibabynews.com/news/articleView.html?idxno=154827` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://central.childcare.go.kr/ccef/community/notice/NoticeSl.jsp?flag=Sl&BBSGB=48&BID=218969` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mk.co.kr/news/society/12136658` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [shocks] Policy and calendar-effects analyst

Hypothesis: New birth incentives, marriage tax or housing policies, and lingering COVID-era timing shifts can create level changes in monthly births; identifying measurable policy start dates and affected cohorts helps judge whether extrapolated 2025-2026 trends over- or under-state July 2026.

Queries issued by the searcher: 2025 2026 출산 장려 정책 출생아 수 월별; Korea monthly live births 2025 2026 Statistics Korea population trends; "2025년 7월" 출생아 수 인구동향 2만 명; Korea births July 2025 monthly population trend 21,000

- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=297003&koreanId=296981` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://47.newstomato.com/ReadNews.aspx?no=1308574` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://betterfuture.go.kr/cmm/fms/FileDown.do;jsessionid=1E368783215D0CC4BE8BC83AB721A0D4.node10?atchFileId=FILE_000000000013835&fileSn=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [base_rates] monthly seasonality and vintage reconciliation

Hypothesis: KOSTAT monthly live-birth levels for Jan-Jun 2026 and revised July 2025/Jan-Jun 2025 would let us replace the H1 scaling with a direct July seasonal-factor estimate and resolve the p14 vs p20-p16 discrepancy. This matters because the current estimate is driven by whether the H1 2025 baseline is 127.2k or 126.0k and whether July 2026 keeps the 2025 July seasonal uplift.

Queries issued by the searcher: Statistics Korea monthly live births 2026 Population Trends; KOSTAT 인구동향 2026년 6월 출생아 수; "2026년 5월 인구동향" 출생아 수 23,160 보도자료; 2025년 7월 출생아 수 2만1천명 인구동향 2025년 9월 발표

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6269788` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chosun.com/economy/economy_general/2026/09/24/VNCQZBDYEZDFZLQXJ7W5DVOK74/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=297003&koreanId=296981` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [base_rates] administrative early count

Hypothesis: July 2026 birth registrations from resident registration or Ministry of Interior and Safety monthly data, adjusted for registration lag, would provide an independent partial count for the target month and reduce reliance on H1 extrapolation. It matters because the target release is not yet available and civil registration is the closest administrative flow.

Queries issued by the searcher: 행정안전부 주민등록 인구통계 2026년 6월 출생자 수; 주민등록 출생등록 월별 2026년 7월 통계; 주민등록 인구통계 월별 출생자수 2026년 7월 전국 출생등록; 행정안전부 주민등록 통계 2026년 7월 출생자 수 자연증가

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] delivery-based proxy

Hypothesis: NHI delivery claims or pregnancy-voucher expected delivery persons for July 2026 would provide a delivery-flow proxy. With the 2024 NHI/KOSTAT ratio of 98.6% (p32) and the 2021-2024 voucher/live-birth ratio of 82% (p36), this could become a coverage-adjusted alternative to the H1 trend. It matters because it is an independent measurement channel rather than another KOSTAT series.

Queries issued by the searcher: 건강보험 분만 청구 건수 2026년 7월; 국민행복카드 임신·출산 진료비 지원 출산 예정자 수 2026; 2026년 6월 출생아 수 통계청 인구동향 월간; 국민건강보험공단 분만자 수 월별 2026 건강보험통계

- `https://www.nabo.go.kr/system/common/JSPservlet/download.jsp?fCode=33318753&fSHC=&fName=NABO+%EC%9D%B8%EA%B5%AC%C2%B7%EA%B3%A0%EC%9A%A9%EB%8F%99%ED%96` -> **snapshot** (snapshot 20250824103837); points raw/verified 15/13
  - p53 NHI delivery claimant (분만자) count, South Korea, 2024 = **235,000** persons (2024-01-01..2024-12-31) [DISCARD: Exact duplicate of p30 (same 235,000 NHI delivery claimants, 2024, same sentence and source).] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p54 KOSTAT live births, South Korea, 2024 = **238,000** live births (2024-01-01..2024-12-31) [keep: ] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p55 Ratio of NHI delivery claimants to KOSTAT live births, 2024 = **98.6** % (2024-01-01..2024-12-31) [DISCARD: Exact duplicate of p32 (98.6% NHI/KOSTAT ratio, 2024, same source sentence).] quote: "2024년 건강보험의 분만자 수는 23.5만명으로 통계청 출생아 수(23.8만명) 대비 98.6% 수준"
  - p56 Ratio of live births to pregnancy-voucher expected delivery persons, 2021-2024 = **82** % (2021-01-01..2024-12-31) [DISCARD: Exact duplicate of p36 (82% live-birth/voucher ratio, 2021-2024).] quote: "2021~2024년간 분만 예정자 대비 출생아 수 비율은 82% 수준에서 차이를 보여주고 있음"
  - p57 Pregnancy-voucher expected delivery persons, 2025 (as of May applications) = **304,000** persons (2025-01-01..2025-12-31) [DISCARD: Exact duplicate of p37 (304,000 voucher expected-delivery persons, 2025 basis).] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p58 Pregnancy-voucher expected delivery persons, 2024 (as of May applications) = **283,000** persons (2024-01-01..2024-12-31) [DISCARD: Exact duplicate of p38 (283,000 voucher expected-delivery persons, 2024).] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p59 Year-on-year increase in pregnancy-voucher expected delivery persons, 2025 vs 20 = **21,000** persons (2025-01-01..2025-12-31) [DISCARD: The +21,000 persons increase is p37 minus p38 and adds nothing beyond those two kept points plus the 7.2% growth already] quote: "2025년 분만 예정자 수는 30.4만명으로 2024년 분만 예정자 수 28.3만명 대비 2.1만명 증가"
  - p60 Pregnancy-voucher expected delivery persons, 2021 = **305,000** persons (2021-01-01..2021-12-31) [keep: ] quote: "2025년 분만 예정자 수는 '21년 분만 예정자 수(30.5만명)와 비슷한 수준"
  - p61 Live births to expected delivery persons ratio, 2021 = **83.6** % (live births / expected delivery persons) (2021-01-01..2021-12-31) [keep: ] quote: "31.2 83.6 26.1"
  - p62 Live births to expected delivery persons ratio, 2022 = **84.9** % (live births / expected delivery persons) (2022-01-01..2022-12-31) [keep: ] quote: "29.3 84.9 24.9"
  - p63 Live births to expected delivery persons ratio, 2023 = **81.9** % (live births / expected delivery persons) (2023-01-01..2023-12-31) [keep: ] quote: "28.1 81.9 23.0"
  - p64 Live births to expected delivery persons ratio, 2024 = **82.4** % (live births / expected delivery persons) (2024-01-01..2024-12-31) [keep: ] quote: "28.9 82.4 23.8"
  - p65 Year-on-year increase in pregnancy-voucher expected delivery persons, 2025 vs 20 = **7.2** % (2025-01-01..2025-12-31) [DISCARD: Exact duplicate of p39 (7.2% yoy increase in voucher expected-delivery persons, 2025 vs 2024).] quote: "2025년 분만 예정자 수는 2024년 대비 7.2% 증가하여 출산율 반등 추세를 이어갈 것으로 전망"
- `https://likms.assembly.go.kr/filegate/sender10?dummy=dummy&bookId=B5B54E74-DD6A-8603-D1E0-FFF7207496FB&type=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.data.go.kr/data/15118813/fileData.do` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mw.go.kr/boardDownload.es?bid=0003&list_no=1490008&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (scale word '만' not supported by quote or table header: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12'] Annual live-birth series from the same Wikipedia/KOSTAT table, same definition. They show the long decline to 2023 and rebound in 2024-2025 (p2 254,457 vs p3 238,343). Used for trend context, not dire
- corroborating: ['p13', 'p14', 'p15'] Jan-Jun cumulative 2026 and 2025 plus derived +14.94% growth. p15 is derived from p13/p14, so it is not independent. This is the main current-year signal for July 2026.
- corroborating: ['p16', 'p17', 'p18'] July 2025 monthly level and derived increase/growth from the same article. p17 and p18 are redundant with p16.
- conflicting: ['p14', 'p16', 'p20'] p20 minus p16 implies Jan-Jun 2025 = 126,001, while p14 reports 127,184, a 1,183 (0.9%) gap. Likely provisional-vs-revised vintage and/or rounding; this matters because it changes the H1 growth denomi
- corroborating: ['p16', 'p19', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] July 2025 level, July 2021 comparison, monthly TFR 2025 and crude birth rate. They are derived from the same KOSTAT birth/population data and corroborate the July 2025 level/seasonality but are not in
- corroborating: ['p30', 'p32', 'p34', 'p35'] NHI delivery claimants vs KOSTAT births in 2024 give 98.6% coverage; total delivery rate 0.70 vs TFR 0.75. Different definitions but a consistent administrative coverage check.
- corroborating: ['p36', 'p37', 'p38', 'p39', 'p40', 'p41'] Pregnancy-voucher expected delivery persons +7.2% in 2025 and Jan-Apr +8.3%, while Jan-Apr live births +7.6%; expected delivery persons 304k vs 254k births is consistent with the 82% ratio. Corroborat
- corroborating: ['p1', 'p13'] p1 gives a Jan-May 2019 benchmark of 134,433; the quoted context says the recent Jan-May cumulative is the largest since 2019. p13 Jan-Jun 2026 = 146,162 is consistent with a high 2026 level, but the 
- contextual: ['p42', 'p43'] Incheon 2024 births and +11.6% growth are regional data, not the national monthly target; only weak corroboration of the 2024 rebound.
- not usable: ['p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52'] Voucher spending, full-spend population, pre-applications and survey shares are program administration/survey data rather than live-birth counts, with 2022-2023 periods and no direct bridge to July 20
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p13', 'p14', 'p15'] p15 is just the arithmetic difference of p13 and p14 (H1 2026 up roughly 15% on H1 2025), so this is one measurement channel, not three confirmations. All three trace to a single Wikipedia table built
- conflicting: ['p14', 'p16', 'p20'] p20 minus p16 implies Jan-Jun 2025 = 126,001 (first-report vintage, Sept 2025 article), while p14 states 127,184 for the same period (2026-07-08 vintage): a ~0.9% revision/vintage gap, not a definitio
- corroborating: ['p16', 'p19', 'p20'] Same July 2025 KOSTAT release: July 2025 births 21,803, the highest July since 2021's 22,364 (p19), consistent with the 147,804 Jan-Jul cumulative (p20). Establishes that July 2025 was already a seaso
- corroborating: ['p16', 'p22', 'p29'] Within the same release, July 2025 TFR 0.80 (joint-highest month of 2025) and CBR 5.0 confirm July as a seasonally high month. Not independent of p16 but supports treating July 2025 as a valid carrier
- corroborating: ['p1', 'p13', 'p14'] p1 (independent news report on KOSTAT data) says the 2026 Jan-May cumulative is the largest Jan-May since 2019's 134,433, i.e. below 134,433 but well above 2020-2025. That is consistent with p13's Jan
- corroborating: ['p2', 'p3', 'p4', 'p5'] Annual KOSTAT series 2022-2025 (249,186 → 230,028 → 238,343 → 254,457) documents the 2024-2025 rebound (+6.8% in 2025) that makes a further 2026 increase directionally plausible. p2 also supplies the 
- corroborating: ['p30', 'p32', 'p34', 'p35'] NHI delivery claimants 235k vs KOSTAT 238k live births in 2024 (98.6%), and total delivery rate 0.70 vs TFR 0.75, move together. This sets a ~1.4% coverage gap so a claims-based count would need a sma
- corroborating: ['p36', 'p61', 'p62', 'p63', 'p64'] Live births / pregnancy-voucher expected-delivery persons is stable at 81.9-84.9% across 2021-2024 (82.4% in 2024). The gap is administrative composition (non-live-birth outcomes, coverage of foreign 
- context: ['p37', 'p38', 'p39', 'p40', 'p41'] Voucher expected-delivery persons rose 7.2% in 2025 (8.3% in Jan-Apr 2025) while Jan-Apr 2025 live births rose 7.6%, showing birth-adjacent administrative flows track statistical births within a few p
- context: ['p18', 'p21'] Restored from round 1: July 2025 yoy growth 5.9% (p18) versus Jan-Jul 2025 cumulative growth 7.2% (p21). In 2025 the July month-specific yoy ran at roughly 0.8x the year-to-date rate, which is the emp

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Damping factor: July 2026 yoy birth growth relative to H1 2026 yoy growth | 0.85 | 0.5..1.2 | 0.5..1.2 | ratio | m3 (m3) | Empirical analogue from the same series: in 2025 the July month-specific yoy birth growth was 5.9% (p18) while the Jan-Jul cumulative growth was 7.2% (p21), i.e. the July rate ran at about 0.8x the year-to-date rate. In addition, July 2025 was itself a strong month relative to its own H1 average (p1 | July 2026 month-specific yoy growth can reasonably differ from the H1 2026 yoy growth, and the difference is expected to resemble the 2025 pattern where the single-month yoy ran below the cumulative rate. | Evidence that July 2026 delivery activity grew at or above the H1 2026 pace (for example July 2026 voucher expected-delivery persons or NHI delivery claims well above the H1 rate), or evidence that the H1 2026 surge was concentrated in January-March and had already faded by June. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | 25,056 |  | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 25,196 | ['p16', 'p13', 'p20'] / [] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 24,400 | ['p16', 'p13', 'p14'] / ['a1'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **24,882** birth, 80% interval [17,406, 35,569] birth, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.33

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for provisional live births occurring in South Korea during July 2026, as first reported in Statistics Korea's monthly Population Trends release, is 24,882 birth (80% model-based interval 17,406 to 35,569 birth). This combines 3 methods at roughly equal weights (33%, 33%, 33%).

Observed anchors: July 2025 births 21,803 live births; H1 2025 cumulative 127,184 live births; H1 2026 cumulative 146,162 live births; Jan–Jul 2025 cumulative 147,804 live births. The methods carry July 2025 forward by the H1 2026 growth, with one method damping that growth by assumption a1 (0.85, range 0.5 to 1.2). The weighting reflects too few backtest years to favor any method.

Key risks: the H1 2026 surge may not persist into July, and the cumulative figures may be running aggregates. The interval is conditional on these assumptions, not a demonstrated accuracy guarantee. Monthly July 2026 data and revised cumulative vintages would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Damping factor: July 2026 yoy birth growth relative to H1 2026 yoy growth: 0.85 ratio, range 0.5 to 1.2; used by m3. Overturned by: Evidence that July 2026 delivery activity grew at or above the H1 2026 pace (for example July 2026 voucher expected-delivery persons or NHI delivery claims well above the H1 rate), or evidence that the H1 2026 surge was concentrated in January-March and had already faded by June.

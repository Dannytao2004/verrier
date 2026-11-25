# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first published in Statistics Korea's monthly Population Trends (인구동향) release | unit live births | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), monthly Population Trends / 인구동향

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly series

Hypothesis: July 2026 births follow the recent level and seasonal pattern of monthly births; July is typically a relatively high-birth month in Korea. Recent monthly values (2024-2026) plus year-over-year change give a baseline nowcast.

Queries issued by the searcher: Statistics Korea monthly live births 2026 인구동향 출생아 수; 출생아 수 월별 2026 통계청 인구동향 5월; 2025년 7월 인구동향 출생아 수 명 전년동월대비; 2025년 12월 인구동향 출생아 수 월별 2025년 연간 출생아 25만4341명; Statistics Korea monthly live births 2026 인구동향 출생아 수; KOSTAT population trends monthly births 2025 2026 statistics; 2026년 5월 인구동향 출생아 수 2만 명대 전년동월대비 13%; 2025년 7월 인구동향 출생아 수 2만1천명 2024년 7월 출생아; Statistics Korea monthly live births 2026 인구동향 출생아 수; 통계청 인구동향 2026년 5월 출생아 수 월별; 2025년 7월 인구동향 출생아 수 2만1천명 전년동월대비 통계청; 국가데이터처 인구동향 연간 월별 출생아 수 2023 2024 2025 표

- `http://47.newstomato.com/ReadNews.aspx?no=1308574` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020300&act=view&bid=204&list_no=445579` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4690717` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sedaily.com/article/20073452` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=294740&koreanId=294708` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446225&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260729067200002` -> **snapshot** (snapshot 20260730114307); points raw/verified 15/15
  - p1 South Korea monthly live births, May 2026 = **23,160** live births (2026-05-01..2026-05-31) [keep: May 2026 births 23,160 — latest observed month, anchors the YoY growth factor.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p2 South Korea monthly live births, May 2026 year-over-year increase = **2,781** live births (2026-05-01..2026-05-31) [keep: May 2026 YoY increase 2,781 — supports the growth factor.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p3 South Korea monthly live births, May 2026 year-over-year growth rate = **13.6** % (2026-05-01..2026-05-31) [keep: May 2026 YoY growth 13.6% — supports the growth factor.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p4 South Korea cumulative live births, January to May 2026 = **122,694** live births (2026-01-01..2026-05-31) [keep: Jan-May 2026 cumulative 122,694 — anchors the annual-level route.] quote: "올해 1∼5월까지는 12만2천694명이 태어났다."
  - p5 South Korea cumulative live births, January to May 2026 year-over-year increase = **16,166** live births (2026-01-01..2026-05-31) [keep: Jan-May 2026 YoY increase 16,166 — supports the annual-level route.] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p6 South Korea cumulative live births, January to May 2026 year-over-year growth ra = **15.2** % (2026-01-01..2026-05-31) [keep: Jan-May 2026 YoY growth 15.2% — supports the annual-level route.] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p7 South Korea cumulative live births, January to May 2019 (comparison year) = **134,433** live births (2019-01-01..2019-05-31) [DISCARD: 2019 Jan-May cumulative; comparison context only, not used in a route.] quote: "1∼5월 누적 규모는 2019년(13만4천433명) 이후 가장 많았고"
  - p8 South Korea monthly live births, May 2019 (comparison year) = **25,299** live births (2019-05-01..2019-05-31) [DISCARD: 2019 May births; comparison context only, not used.] quote: "출생아 규모는 5월 기준으로 2019년(2만5천299명) 이후 7년 만에 가장 많았다."
  - p9 South Korea total fertility rate, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [DISCARD: May 2026 TFR; rate, not used in a count route.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p10 South Korea total fertility rate, May 2026 year-over-year increase = **0.1** live births per woman (2026-05-01..2026-05-31) [DISCARD: May 2026 TFR YoY; not used.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p11 South Korea share of May 2026 births that were first births = **63** % (2026-05-01..2026-05-31) [DISCARD: May 2026 first-birth share; not used in a route.] quote: "출산 순위별 출생아 수 구성비는 첫째가 63.0%로 1.3%포인트(p) 늘었다."
  - p12 South Korea share of May 2026 births that were second births = **31.7** % (2026-05-01..2026-05-31) [DISCARD: May 2026 second-birth share; not used.] quote: "둘째는 31.7%로 0.2%p 감소했다."
  - p13 South Korea share of May 2026 births that were third or higher order = **5.3** % (2026-05-01..2026-05-31) [DISCARD: May 2026 third-birth share; not used.] quote: "셋째 이상은 5.3%로 1.1%p 줄었다."
  - p14 South Korea monthly deaths, May 2026 = **29,573** deaths (2026-05-01..2026-05-31) [DISCARD: Deaths; not used in any birth route.] quote: "5월 사망자 수는 2만9천573명으로 1년 전보다 1천91명(3.8%) 증가했다."
  - p15 South Korea monthly marriages, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [DISCARD: May 2026 marriages; not used in a route.] quote: "5월 혼인 건수는 2만368건으로 1년 전보다 1천392건(-6.4%) 줄었다."
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p16 Live births in South Korea, July 2025 (monthly total) = **21,803** live births (2025-07-01..2025-07-31) [keep: July 2025 births 21,803 — the base for the YoY-scaling route.] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p17 Year-over-year change in live births, South Korea, July 2025 vs July 2024 = **5.9** % (2025-07-01..2025-07-31) [DISCARD: July 2025 YoY %; the level p16 plus assumption a1 is the route, so the historical YoY is context only.] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p18 Deaths in South Korea, July 2025 (monthly total) = **27,979** deaths (2025-07-01..2025-07-31) [DISCARD: Deaths; irrelevant to births.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p19 Year-over-year change in deaths, South Korea, July 2025 vs July 2024 = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Deaths change; irrelevant.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p20 Marriages in South Korea, July 2025 (monthly count) = **20,394** marriages (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages; not used in a route (marriage lead is too long to pin July 2026).] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p21 Year-over-year change in marriages, South Korea, July 2025 vs July 2024 = **8.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 marriage YoY; not used.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p22 Divorces in South Korea, July 2025 (monthly count) = **7,826** divorces (2025-07-01..2025-07-31) [DISCARD: Divorces; irrelevant to births.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p23 Year-over-year change in divorces, South Korea, July 2025 vs July 2024 = **1.4** % (2025-07-01..2025-07-31) [DISCARD: Divorces change; irrelevant.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p24 Natural increase (live births minus deaths), South Korea, July 2025 = **-6,175** persons (2025-07-01..2025-07-31) [DISCARD: Natural increase; not a birth input.] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://newspim.com/news/view/20250924000454` -> **snapshot** (snapshot 20251126043735); points raw/verified 15/14
  - p25 South Korea monthly live births, July 2025 (latest July published) = **21,803** live births (2025-07-01..2025-07-31) [DISCARD: Duplicate of p16 (July 2025 births).] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월보다 1223명(5.9%) 증가했다."
  - p26 South Korea July live births year-over-year change, July 2025 vs July 2024 = **1,223** live births (2025-07-01..2025-07-31) [DISCARD: Duplicate of the July 2025 YoY change.] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월보다 1223명(5.9%) 증가했다."
  - p27 South Korea July live births year-over-year growth rate, July 2025 = **5.9** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p17 (July 2025 YoY %).] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월보다 1223명(5.9%) 증가했다."
  - p28 South Korea monthly live births, June 2025 (exception month below 20,000) = **19,953** live births (2025-06-01..2025-06-30) [DISCARD: June 2025 births; not used in a route.] quote: "해당 기간 동안 지난해 12월(1만8256명)과 올해 6월(1만9953명)을 제외하고는 줄곧 2만명대 규모를 유지했다."
  - p29 South Korea cumulative live births, January-July 2025 = **147,804** live births (2025-01-01..2025-07-31) [DISCARD: Jan-Jul 2025 cumulative; not used in a route.] quote: "올해 1~7월 누계 출생아 수는 14만7804명으로 전년 동기보다 9944명(7.2%) 늘었다."
  - p30 South Korea cumulative live births year-over-year change, January-July 2025 vs 2 = **9,944** live births (2025-01-01..2025-07-31) [DISCARD: Jan-Jul 2025 cumulative YoY; not used.] quote: "올해 1~7월 누계 출생아 수는 14만7804명으로 전년 동기보다 9944명(7.2%) 늘었다."
  - p31 South Korea cumulative live births year-over-year growth rate, January-July 2025 = **7.2** % (2025-01-01..2025-07-31) [DISCARD: Jan-Jul 2025 cumulative growth; not used.] quote: "올해 1~7월 누계 출생아 수는 14만7804명으로 전년 동기보다 9944명(7.2%) 늘었다."
  - p32 South Korea total fertility rate, July 2025 = **0.8** live births per woman (2025-07-01..2025-07-31) [DISCARD: July 2025 TFR; not used.] quote: "7월 합계출산율은 0.80명으로 전년 동월 대비 0.04명 증가했다."
  - p33 South Korea total fertility rate year-over-year change, July 2025 = **0.04** live births per woman (2025-07-01..2025-07-31) [DISCARD: July 2025 TFR YoY; not used.] quote: "7월 합계출산율은 0.80명으로 전년 동월 대비 0.04명 증가했다."
  - p34 Gyeonggi province live births, July 2025 = **6,539** live births (2025-07-01..2025-07-31) [DISCARD: Provincial July 2025 births; not used and not needed for a national total.] quote: "출생아가 가장 많이 태어난 지역은 ▲경기(6539명) ▲서울(3938명) ▲인천(1488명) ▲부산(1218명) ▲경남(1179명) 등으로 집계됐다."
  - p35 Seoul live births, July 2025 = **3,938** live births (2025-07-01..2025-07-31) [DISCARD: Seoul July 2025 births; not used.] quote: "출생아가 가장 많이 태어난 지역은 ▲경기(6539명) ▲서울(3938명) ▲인천(1488명) ▲부산(1218명) ▲경남(1179명) 등으로 집계됐다."
  - p36 Sejong live births, July 2025 (lowest region) = **240** live births (2025-07-01..2025-07-31) [DISCARD: Sejong July 2025 births; not used.] quote: "가장 적게 태어난 지역은 세종(240명)이었다."
  - p37 South Korea marriages, July 2025 = **20,394** marriages (2025-07-01..2025-07-31) [DISCARD: Duplicate of p20 (July 2025 marriages).] quote: "7월 혼인건수는 2만394건으로 전년 동월보다 1583건(8.4%) 증가했다."
  - p38 South Korea cumulative marriages, January-July 2025 = **138,267** marriages (2025-01-01..2025-07-31) [DISCARD: Jan-Jul 2025 cumulative marriages; not used in a route.] quote: "1~7월 누계 혼인건수는 13만8267건으로 전년 동기에 비해 7.3% 늘었다."
- `https://www.asiatoday.co.kr/kn/view.php?key=20260729010010766` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] Marriage registrations

Hypothesis: Korean births are strongly linked to marriages roughly 1-2 years earlier; marriage registrations rose in 2023-2024, which should support 2025-2026 births. Monthly marriage counts lead births and can adjust the own-history baseline.

Queries issued by the searcher: South Korea monthly marriage registrations 2025 2026 Statistics Korea; 혼인건수 월별 2026 통계청 인구동향; 2025년 혼인건수 월별 24만건 통계청 인구동향 연간; 혼인 출생 상관관계 시차 2년 출생아수 결혼 선행지표 분석; South Korea monthly marriage registrations 2025 2026 Statistics Korea; 혼인건수 월별 2026 통계청 인구동향; 2026년 5월 인구동향 보도자료 혼인 출생 2026-07-29 국가데이터처; 2025년 혼인·이혼 통계 2026년 3월 19일 월별 혼인건수 평균 초혼 연령; South Korea monthly marriage registrations 2025 2026 statistics Korea; 혼인건수 월별 2026 통계청 인구동향; Korea marriage births lag correlation months 2024 2025 혼인 출생 상관관계 시차; 2025년 혼인건수 24만건 월별 혼인 2024년 월별 혼인 건수 통계

- `https://www.khan.co.kr/article/202607291457001` -> **snapshot** (snapshot 20260730104343); points raw/verified 15/15
  - p39 South Korea marriage registrations, May (latest month, year-over-year change) = **20,368** marriage registration (2026-05-01..2026-05-31) [DISCARD: Duplicate of p15.] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p40 South Korea marriage registrations, May, year-over-year change (count) = **1,392** marriage registration (2026-05-01..2026-05-31) [DISCARD: May 2026 marriage YoY count; not used.] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p41 South Korea marriage registrations, May, year-over-year change (percent) = **6.4** % (2026-05-01..2026-05-31) [DISCARD: May 2026 marriage YoY %; not used.] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p42 South Korea live births, May = **23,160** live birth (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p1 (same KOSTAT May 2026 figure).] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p43 South Korea live births, May, year-over-year change (count) = **2,781** live birth (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p2.] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p44 South Korea live births, May, year-over-year change (percent) = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p3.] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p45 South Korea consecutive months of live-birth increase through May = **23** month (2024-07-01..2026-05-31) [DISCARD: Birth streak; context only, not used.] quote: "출생아 수는 2024년 7월 이후 23개월 연속 증가세를 이어갔다."
  - p46 South Korea live births, May 2019 (comparison year for 7-year high) = **25,299** live birth (2019-05-01..2019-05-31) [DISCARD: Duplicate of p8 (2019 May births).] quote: "5월 기준 출생아 수는 2019년(2만5299명) 이후 7년 만에 가장 많았다."
  - p47 South Korea cumulative live births, January-May = **122,694** live birth (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p4.] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p48 South Korea cumulative live births, January-May, year-over-year change (count) = **16,166** live birth (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p5.] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p49 South Korea cumulative live births, January-May, year-over-year change (percent) = **15.2** % (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p6.] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p50 South Korea cumulative live births, January-May 2019 (comparison year) = **134,433** live birth (2019-01-01..2019-05-31) [DISCARD: Redundant copy of p7.] quote: "누적 출생아 수는 2019년(13만4433명) 이후 가장 많았으며, 증가 폭과 증가율 모두 통계 작성 이래 최대를 기록했다."
  - p51 South Korea total fertility rate, May = **0.85** live birth per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p9.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 지난해 같은 달보다 0.10명 증가했다."
  - p52 South Korea total fertility rate, May, year-over-year change = **0.1** live birth per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p10.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 지난해 같은 달보다 0.10명 증가했다."
  - p53 South Korea natural population change, May (deaths minus births) = **6,413** person (2026-05-01..2026-05-31) [DISCARD: Natural decrease; not a birth input.] quote: "이에 따라 5월 인구는 6413명 자연 감소했다."
- `https://biz.chosun.com/en/en-policy/2026/07/29/BC2ERZDWNJEXJGVZAHECYJ6WAI/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?num=279886` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=204&list_no=444188&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chosun.com/economy/economy_general/2026/04/22/DMBJ2HALXRADPCZV3ZFUGFIKXQ/` -> **snapshot** (snapshot 20260422043002); points raw/verified 2/2
  - p54 Consecutive months of marriage registration increase in South Korea (streak leng = **22** month (not stated (page dated 2026-04-22)) [DISCARD: Marriage streak; context only, not used.] quote: "출생 선행 지표 결혼 22개월 연속 늘다 올해 2월 꺾여"
  - p55 Live births in South Korea, February (latest reported month), stated as 7-year m = **22,898** live births (not stated (page dated 2026-04-22)) [DISCARD: Duplicate of p58 (February 2026 births).] quote: "2월 출생아는 2만2898명으로 7년만 최대"
- `https://dl.nanet.go.kr/detail/NONB12026000010922` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mk.co.kr/news/economy/12023896` -> **snapshot** (snapshot 20260508043037); points raw/verified 12/10
  - p56 South Korea marriage registrations, February 2026 (monthly count) = **18,557** marriage registrations (2026-02-01..2026-02-28) [DISCARD: February 2026 marriages; not used in a route.] quote: "2월 혼인 건수는 1만 8557건으로 전년 동월 대비 4.2% 감소하며 23개월 만에 처음으로 줄어든 것으로 집계되었답니다."
  - p57 South Korea marriage registrations, February 2026, year-on-year change = **4.2** % (2026-02-01..2026-02-28) [DISCARD: February 2026 marriage YoY; not used.] quote: "2026년 2월 혼인 건수가 전년 동월 대비 4.2% 감소했다고 해요."
  - p58 South Korea live births, February 2026 (monthly count) = **22,898** live births (2026-02-01..2026-02-28) [DISCARD: February 2026 births; not used in a July route.] quote: "2026년 2월 출생아 수는 2만 2898명으로 전년 동월 대비 13.6% 증가하며"
  - p59 South Korea live births, February 2026, year-on-year change = **13.6** % (2026-02-01..2026-02-28) [DISCARD: February 2026 birth YoY; not used.] quote: "2월 출생아 수는 전년 동월 대비 13.6% 증가하며 20개월 연속 상승세를 이어가는"
  - p60 South Korea consecutive months of marriage registration increase ending January  = **22** months (2024-04-01..2026-01-31) [DISCARD: Marriage streak; context only.] quote: "2024년 4월부터 2026년 1월까지 22개월 연속 증가세를 기록하며 역대 최장 상승 흐름을 이어왔던"
  - p61 South Korea consecutive months of live birth increase through February 2026 = **20** months (2024-07-01..2026-02-28) [DISCARD: Birth streak; context only.] quote: "2024년 7월 이후 20개월 연속 증가세를 기록했어요."
  - p62 South Korea marriage registration reporting days, February 2025 = **20** days (2025-02-01..2025-02-28) [DISCARD: February 2025 reporting days; only relevant to the Feb marriage dip, not to July births.] quote: "지난해 2월에는 신고일수가 20일이었던 반면, 올해 2월은 설 연휴로 인해 신고일수가 17일로 줄었기 때문이에요."
  - p63 South Korea marriage registration reporting days, February 2026 = **17** days (2026-02-01..2026-02-28) [DISCARD: February 2026 reporting days; only relevant to the Feb marriage dip, not to July births.] quote: "올해 2월은 설 연휴로 인해 신고일수가 17일로 줄었기 때문이에요."
  - p64 South Korea deaths, February 2026, year-on-year change = **3.5** % (2026-02-01..2026-02-28) [DISCARD: Deaths change; irrelevant.] quote: "이와 반대로 사망자 수는 3.5% 감소했고"
  - p65 South Korea divorces, February 2026, year-on-year change = **15.6** % (2026-02-01..2026-02-28) [DISCARD: Divorces change; irrelevant.] quote: "이혼 건수도 15.6% 줄어든 것으로 나타났어요."
- `https://www.segye.com/newsView/20260325504288` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://view.asiae.co.kr/article/2026022509242475041` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sisajournal.com/news/articleView.html?idxno=366375` -> **dropped** (snapshot fetch failed (http 302); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.datasom.co.kr/news/articleView.html?idxno=208150` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: value_as_written is only part of a larger CJK number in the quote: 2)

### d3 [related_series] Births by birth order / maternal age

Hypothesis: Total births decompose into first births and higher-order births; first-birth trends track marriage cohorts while higher-order births track prior births. This constrains the level and direction of change.

Queries issued by the searcher: 출생아 수 출생순위 월별 2026 통계청 인구동향; Korea births by birth order 2025 statistics first child share; 2026년 5월 인구동향 출생아 수 첫째아 비중 국가데이터처; 2025년 7월 인구동향 출생아 수 2만1854명 첫째아 61.9%; 출생아 수 출생순위 월별 2026 통계청 인구동향; Korea births by birth order 2025 first birth share statistics; 2026년 5월 인구동향 출생아 수 5월 발표 국가데이터처; 2026년 6월 인구동향 출생아 수 2만3111명 첫째아; 출생아 수 출생순위 월별 2026 통계청 인구동향; Korea births by birth order 2025 statistics first child share; 2026년 5월 인구동향 출생아 수 첫째아 비중 둘째아; 2025년 출생통계 잠정 첫째아 15만8천700명 첫째아 비중 62.4% 2026년 2월 발표

- `https://www.ajunews.com/view/20260422105926408` -> **snapshot** (snapshot 20260423090949); points raw/verified 15/13
  - p66 South Korea live births, year-on-year change, February 2026 = **2,747** live births (2026-02-01..2026-02-28) [DISCARD: February 2026 birth YoY count; not used.] quote: "지난 2월 출생아 수는 2만2898명으로 전년 동월 대비 2747명(13.6%) 증가했다."
  - p67 South Korea live births, year-on-year growth rate, February 2026 = **13.6** % (2026-02-01..2026-02-28) [DISCARD: February 2026 birth YoY %; not used.] quote: "지난 2월 출생아 수는 2만2898명으로 전년 동월 대비 2747명(13.6%) 증가했다."
  - p68 South Korea live births, year-on-year growth rate, July 2024 = **7.8** % (2024-07-01..2024-07-31) [DISCARD: July 2024 YoY %; not used.] quote: "출생아 수는 2024년 7월(7.8%) 이후 20개월째 상승세를 보이고 있다."
  - p69 South Korea total fertility rate, February 2026 = **0.93** births per woman (2026-02-01..2026-02-28) [DISCARD: February 2026 TFR; not used.] quote: "합계출산율은 0.93명으로 1년 전보다 0.10명 늘었다."
  - p70 South Korea total fertility rate, year-on-year change, February 2026 = **0.1** births per woman (2026-02-01..2026-02-28) [DISCARD: February 2026 TFR YoY; not used.] quote: "합계출산율은 0.93명으로 1년 전보다 0.10명 늘었다."
  - p71 South Korea share of first births in total births, year-on-year change in percen = **1.2** % (2026-02-01..2026-02-28) [DISCARD: First-birth share change; not used.] quote: "출산 순위별 출생아 수 구성비는 전년 동월 대비 첫째아는 1.2%포인트 증가했으며"
  - p72 South Korea share of second births in total births, year-on-year change in perce = **0.5** % (2026-02-01..2026-02-28) [DISCARD: Second-birth share change; not used.] quote: "둘째아, 셋째아 이상은 각각 0.5%포인트, 0.6%포인트 줄었다."
  - p73 South Korea share of third-or-higher births in total births, year-on-year change = **0.6** % (2026-02-01..2026-02-28) [DISCARD: Third-birth share change; not used.] quote: "둘째아, 셋째아 이상은 각각 0.5%포인트, 0.6%포인트 줄었다."
  - p74 South Korea natural decrease (live births minus deaths), February 2026 = **-6,275** persons (2026-02-01..2026-02-28) [DISCARD: Natural decrease; not a birth input.] quote: "이에 출생아 수에서 사망자 수를 제외한 규모는 -6275명으로 자연감소했다."
  - p75 South Korea marriages, year-on-year change, February 2026 = **811** marriages (2026-02-01..2026-02-28) [DISCARD: February 2026 marriage YoY count; not used.] quote: "출생률의 선행지표로 불리는 혼인 건수는 1만8557건으로 1년 전보다 811건(-4.2%) 줄었다."
  - p76 South Korea marriages, year-on-year growth rate, February 2026 = **-4.2** % (2026-02-01..2026-02-28) [DISCARD: February 2026 marriage YoY %; not used.] quote: "출생률의 선행지표로 불리는 혼인 건수는 1만8557건으로 1년 전보다 811건(-4.2%) 줄었다."
  - p77 South Korea divorces, February 2026 = **6,197** divorces (2026-02-01..2026-02-28) [DISCARD: Divorces; irrelevant.] quote: "같은 달 이혼 건수는 6197건으로 전년 동월 대비 1149건(-15.6%) 감소했다."
  - p78 South Korea natural decrease, November 2019 (start of streak) = **-1,685** persons (2019-11-01..2019-11-30) [DISCARD: Natural-decrease streak; irrelevant.] quote: "자연감소는 2019년 11월(-1685명) 이후 76개월 연속 발생하고 있다."
- `https://www.korea.kr/briefing/policyBriefingView.do?newsId=156745912` -> **snapshot** (snapshot 20260225040619); points raw/verified 15/15
  - p79 South Korea total live births, 2025 provisional = **254,500** live births (2025-01-01..2025-12-31) [DISCARD: 2025 annual births; superseded by p133 for the annual level.] quote: "2025년 출생아 수는 25만 4,500명으로 전년보다 1만 6,100명이 늘어 6.8% 증가했습니다."
  - p80 South Korea first-order births (첫째아), 2025 provisional = **158,700** live births (2025-01-01..2025-12-31) [DISCARD: 2025 first-order births; not used in a route.] quote: "첫째아는 15만 8,700명으로 전년보다 1만 2,600명, 8.6% 증가했고"
  - p81 South Korea second-order births (둘째아), 2025 provisional = **79,300** live births (2025-01-01..2025-12-31) [DISCARD: 2025 second-order births; not used.] quote: "둘째아는 7만 9,300명으로 전년보다 3,400명, 4.5% 증가했습니다."
  - p82 South Korea third-or-higher-order births (셋째아 이상), 2025 provisional = **16,300** live births (2025-01-01..2025-12-31) [DISCARD: 2025 third-order births; not used.] quote: "셋째아 이상은 1만 6,300명으로 전년보다 100명, 0.5% 증가했습니다."
  - p83 Share of first-order births in total live births, 2025 provisional = **62.4** % (2025-01-01..2025-12-31) [DISCARD: 2025 first-birth share; not used.] quote: "첫째아가 출생아 수에서 차지하는 비중은 62.4%로 전년보다 1.1%p 증가했습니다."
  - p84 Year-on-year change in first-order births, 2025 provisional = **12,600** live births (2025-01-01..2025-12-31) [DISCARD: 2025 first-birth YoY; not used.] quote: "출산 순위별 출생을 보면 전년에 비해 첫째아는 1만 2,600명 증가하였고 둘째아는 3,400명 증가하였습니다."
  - p85 Year-on-year change in second-order births, 2025 provisional = **3,400** live births (2025-01-01..2025-12-31) [DISCARD: 2025 second-birth YoY; not used.] quote: "출산 순위별 출생을 보면 전년에 비해 첫째아는 1만 2,600명 증가하였고 둘째아는 3,400명 증가하였습니다."
  - p86 South Korea total fertility rate (합계출산율), 2025 provisional = **0.8** live births per woman (2025-01-01..2025-12-31) [DISCARD: 2025 TFR; redundant with p135.] quote: "2025년 합계출산율은 0.80명으로 2024년 0.75명보다 0.05명 증가했습니다."
  - p87 South Korea total fertility rate (합계출산율), 2024 = **0.75** live births per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; redundant with p136.] quote: "2025년 합계출산율은 0.80명으로 2024년 0.75명보다 0.05명 증가했습니다."
  - p88 South Korea crude birth rate (조출생률), 2025 provisional = **5** live births per 1,000 population (2025-01-01..2025-12-31) [DISCARD: 2025 crude birth rate; not used.] quote: "인구 1,000명당 출생아 수를 나타내는 조출생률은 5.0명으로 전년보다 0.3명 증가하였습니다."
  - p89 Share of January in annual live births (monthly birth share), 2025 = **9.5** % (2025-01-01..2025-12-31) [DISCARD: 2025 January share; not used (July share is the relevant one).] quote: "월별 출생아 수 비중은 1월이 9.5%로 연중 가장 높았고, 2월·6월·12월이 7.9%로 가장 낮았습니다."
  - p90 Share of February, June and December in annual live births (monthly birth share, = **7.9** % (2025-01-01..2025-12-31) [DISCARD: 2025 low-month share; not used.] quote: "월별 출생아 수 비중은 1월이 9.5%로 연중 가장 높았고, 2월·6월·12월이 7.9%로 가장 낮았습니다."
  - p91 Share of births within 2 years of marriage in total live births, 2025 provisiona = **36.1** % (2025-01-01..2025-12-31) [DISCARD: Share of births within 2 years of marriage; not used in a route.] quote: "결혼 후 2년 미만에 낳는 출생아 비중은 36.1%로 전년보다 1.1%p 증가했습니다."
  - p92 Live births within 2 years of marriage, 2025 provisional = **87,200** live births (2025-01-01..2025-12-31) [DISCARD: Births within 2 years of marriage; not used.] quote: "결혼 후 2년 만에 낳는 출생아 수는 8만 7,200명으로 전년에 비해 8,100명, 10.2% 증가했습니다."
  - p93 Share of births to mothers aged 35 and over, 2025 provisional = **37.3** % (2025-01-01..2025-12-31) [DISCARD: Share of births to mothers 35+; not used.] quote: "35세 이상 고령 산모가 낳은 출생아의 비중은 전체의 37.3%로 전년에 비해 1.4%p 증가했습니다."
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dl.nanet.go.kr/detail/NONB12026000010922` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thepowernews.co.kr/view.php?ud=202606241520061706de3f0aa1be_7&vct=g0104` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asiatoday.co.kr/kn/view.php?key=20260729010010766` -> **snapshot** (snapshot 20260730092319); points raw/verified 15/15
  - p94 Live births in South Korea, May 2026 (monthly) = **23,160** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p1.] quote: "올해 5월 출생아 수는 2만3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p95 Year-on-year increase in live births, South Korea, May 2026 = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p2.] quote: "올해 5월 출생아 수는 2만3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p96 Year-on-year growth rate of live births, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p3.] quote: "올해 5월 출생아 수는 2만3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p97 Live births in South Korea, May 2019 (comparison year) = **25,299** live births (2019-05-01..2019-05-31) [DISCARD: Redundant copy of p8.] quote: "5월 기준 출생아 수는 2019년(2만5299명) 이후 가장 많았다."
  - p98 Cumulative live births in South Korea, January-May 2026 = **122,694** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p4.] quote: "이에 올해 1~5월 누적 출생아 수도 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p99 Year-on-year increase in cumulative live births, South Korea, January-May 2026 = **16,166** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p5.] quote: "이에 올해 1~5월 누적 출생아 수도 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p100 Year-on-year growth rate of cumulative live births, South Korea, January-May 202 = **15.2** % (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p6.] quote: "이에 올해 1~5월 누적 출생아 수도 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p101 Total fertility rate, South Korea, May 2026 = **0.85** births per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p9.] quote: "5월 합계출산율은 0.85명으로 전년보다 0.10명 상승했다."
  - p102 Year-on-year change in total fertility rate, South Korea, May 2026 = **0.1** births per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p10.] quote: "5월 합계출산율은 0.85명으로 전년보다 0.10명 상승했다."
  - p103 Share of first births in total live births, South Korea, May 2026 = **63** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p11.] quote: "출산 순위별로는 첫째아 비중이 63.0%로 지난해보다 1.3%포인트(p) 증가했다."
  - p104 Year-on-year change in share of first births, South Korea, May 2026 = **1.3** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p11's change.] quote: "출산 순위별로는 첫째아 비중이 63.0%로 지난해보다 1.3%포인트(p) 증가했다."
  - p105 Share of second births in total live births, South Korea, May 2026 = **31.7** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p12.] quote: "반면 둘째아는 31.7%, 셋째 이상은 5.3%로 각각 0.2%p, 1.1%p 감소했다."
  - p106 Share of third-or-higher-order births in total live births, South Korea, May 202 = **5.3** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p13.] quote: "반면 둘째아는 31.7%, 셋째 이상은 5.3%로 각각 0.2%p, 1.1%p 감소했다."
  - p107 Marriages in South Korea, May 2026 (monthly) = **20,368** marriages (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p15.] quote: "5월 혼인 건수는 2만368건으로 작년보다 1392건(6.4%) 감소했다."
  - p108 Year-on-year change in marriages, South Korea, May 2026 = **1,392** marriages (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p15's change.] quote: "5월 혼인 건수는 2만368건으로 작년보다 1392건(6.4%) 감소했다."
- `https://www.thepowernews.co.kr/view.php?ud=202606241520061706de3f0aa1be_7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000056178` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/briefing/pressReleaseView.do?gubun=pressRelease&newsId=156775545` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yugacrew.com/crewletter/births-2026-08` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dailian.co.kr:3000/news/view/1636477/2%EC%9B%94-%EC%B6%9C%EC%83%9D%EC%95%84-%EC%A0%84%EB%85%84%EB%8F%99%EC%9B%94-%E6%AF%94-13620%EA%B0%9C-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (scale word '万' not supported by quote or table header: 2)

### d4 [administrative] Resident registration birth registrations

Hypothesis: Resident registration (주민등록) birth registrations and 'birth support' applications provide a near-real-time administrative trace that correlates with occurrence-based births with a short lag.

Queries issued by the searcher: 주민등록 출생자 수 2026 월별; 행정안전부 주민등록 인구통계 출생 2026; 2026년 5월 인구동향 출생아 수 23,160 보도자료; 주민등록 출생등록자수 2026년 7월 전국 출생등록; 주민등록 출생자 수 2026 월별; 첫만남이용권 신청 건수 2026; 행정안전부 주민등록 인구통계 2026년 7월 출생등록자 수; 2026년 5월 인구동향 출생아 수 23,160 통계청; 주민등록 출생자 수 2026 월별; 첫만남이용권 신청 건수 2025 월별; 행정안전부 주민등록 인구통계 2026년 7월 출생등록 자연증가; 주민등록기준 출생등록자수 KOSIS 월별 2026

- `https://www.data.go.kr/data/15099155/fileData.do` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://korea.nabo.go.kr/board/file/down.do?fid=33319286` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dl.nanet.go.kr/detail/NONB12026000010922` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1681&no=9918644` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gimjecity.tistory.com/entry/2026-7%EC%9B%94%EB%A7%90-%EC%A0%84%EA%B5%AD%EA%B4%91%EC%97%AD%EC%8B%9C%EB%8F%84%EB%B3%84-%EC%9D%B8%EA%B5%AC%ED%98%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260729067200002` -> **snapshot** (snapshot 20260730114307); points raw/verified 15/15
  - p109 South Korea monthly live births, May 2026 (KOSTAT monthly Population Trends) = **23,160** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p1.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p110 South Korea year-on-year increase in monthly live births, May 2026 = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p2.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p111 South Korea year-on-year growth rate of monthly live births, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p3.] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p112 South Korea cumulative live births, January-May 2026 = **122,694** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p4.] quote: "올해 1∼5월까지는 12만2천694명이 태어났다."
  - p113 South Korea year-on-year increase in cumulative live births, January-May 2026 = **16,166** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p5.] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p114 South Korea year-on-year growth rate of cumulative live births, January-May 2026 = **15.2** % (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p6.] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p115 South Korea cumulative live births, January-May 2019 (comparison year) = **134,433** live births (2019-01-01..2019-05-31) [DISCARD: Redundant copy of p7.] quote: "1∼5월 누적 규모는 2019년(13만4천433명) 이후 가장 많았고"
  - p116 South Korea monthly live births, May 2019 (comparison year) = **25,299** live births (2019-05-01..2019-05-31) [DISCARD: Redundant copy of p8.] quote: "출생아 규모는 5월 기준으로 2019년(2만5천299명) 이후 7년 만에 가장 많았다."
  - p117 South Korea total fertility rate, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p9.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p118 South Korea year-on-year change in total fertility rate, May 2026 = **0.1** live births per woman (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p10.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p119 Share of May 2026 live births that were first births = **63** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p11.] quote: "출산 순위별 출생아 수 구성비는 첫째가 63.0%로 1.3%포인트(p) 늘었다."
  - p120 Share of May 2026 live births that were second births = **31.7** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p12.] quote: "둘째는 31.7%로 0.2%p 감소했다."
  - p121 Share of May 2026 live births that were third or higher order = **5.3** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p13.] quote: "셋째 이상은 5.3%로 1.1%p 줄었다."
  - p122 South Korea monthly deaths, May 2026 = **29,573** deaths (2026-05-01..2026-05-31) [DISCARD: Deaths; irrelevant.] quote: "5월 사망자 수는 2만9천573명으로 1년 전보다 1천91명(3.8%) 증가했다."
  - p123 South Korea monthly marriages, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p15.] quote: "5월 혼인 건수는 2만368건으로 1년 전보다 1천392건(-6.4%) 줄었다."
- `https://mods.go.kr/board.es?bid=204&mid=a10301020000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jumin.mois.go.kr` -> **snapshot** (snapshot 20260717112850); points raw/verified 0/0

### d5 [forecasts_markets] Official and analyst projections

Hypothesis: KOSTAT and research institutes publish annual birth projections and sometimes monthly commentary; these constrain the plausible 2026 level and July share.

Queries issued by the searcher: 2026년 출생아 수 전망 통계청; South Korea 2026 birth forecast projection; 2025년 7월 출생아 수 2만명 인구동향; 2026년 6월 출생아 수 인구동향 국가데이터처; 2026년 출생아 수 전망 통계청; South Korea 2026 birth forecast projection; 2026년 6월 출생아 수 인구동향 상반기 누계; 2025년 7월 출생아 수 2만명 인구동향 통계청; 2026년 출생아 수 전망 통계청; South Korea 2026 birth forecast projection; 2025년 7월 출생아 수 명 인구동향; 통계청 장래인구추계 2022-2072 2026년 출생아 수 중위 고위 저위

- `https://v.daum.net/v/20260802121104585` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/society/2026/08/03/20260803010003` -> **snapshot** (snapshot 20260803052117); points raw/verified 15/15
  - p124 South Korea total fertility rate, Q1 2026 (annualised rate) = **0.95** children per woman (2026-01-01..2026-03-31) [DISCARD: Q1 2026 TFR; rate, not used in a count route.] quote: "올해 1분기 합계출산율은 0.95명으로 집계됐다."
  - p125 South Korea total fertility rate, April 2026 = **0.93** children per woman (2026-04-01..2026-04-30) [DISCARD: April 2026 TFR; not used.] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p126 South Korea total fertility rate, May 2026 = **0.85** children per woman (2026-05-01..2026-05-31) [DISCARD: May 2026 TFR; duplicate of p9, not used.] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p127 South Korea live births, January-May 2026 cumulative = **122,694** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p4.] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p128 South Korea live births, January-May 2026 increase vs same period prior year = **16,166** live births (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p5.] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p129 South Korea live births, January-May 2026 year-on-year growth rate = **15.2** % (2026-01-01..2026-05-31) [DISCARD: Redundant copy of p6.] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p130 South Korea live births, May 2026 = **23,160** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p1.] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p131 South Korea live births, May 2026 increase vs May prior year = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p2.] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p132 South Korea live births, May 2026 year-on-year growth rate = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p3.] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p133 South Korea annual live births, prior year (2025) reference level = **254,457** live births (2025-01-01..2025-12-31) [keep: 2025 annual births 254,457 — the base for the annual-level route.] quote: "지금과 같은 흐름이 이어지면 올해 연간 출생아 수는 지난해(25만 4457명)를 넘어 20만명대 후반까지 늘어날 것으로 예상된다."
  - p134 South Korea annual live births, 2026 forecast (upper end of 'late 200,000s') = **200,000** live births (2026-01-01..2026-12-31) [DISCARD: Journalistic 'late 200,000s' forecast; the coded 200,000 is the floor of a vague phrase, not a usable point estimate, an] quote: "지금과 같은 흐름이 이어지면 올해 연간 출생아 수는 지난해(25만 4457명)를 넘어 20만명대 후반까지 늘어날 것으로 예상된다."
  - p135 South Korea total fertility rate, 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [DISCARD: 2025 TFR; context only, not used in a count route.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p136 South Korea total fertility rate, 2024 = **0.75** children per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; context only.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p137 South Korea total fertility rate, 2023 = **0.72** children per woman (2023-01-01..2023-12-31) [DISCARD: 2023 TFR; context only.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p138 South Korea total fertility rate, 2019 (last year in 0.9 range) = **0.92** children per woman (2019-01-01..2019-12-31) [DISCARD: 2019 TFR context; not used in any route.] quote: "현실화하면 2019년 0.92명 이후 7년 만이다."
- `https://m.dailymagazine.co.kr/news/newsview.php?ncode=1065541823597083` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://re-www.yna.co.kr/view/AKR20251231132800002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mk.co.kr/news/economy/11491148` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://re-www.yna.co.kr/view/AKR20251231132800002?section=search` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03230806642303400&mediaCodeNo=257` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.wikipedia.org/wiki/Demographics_of_South_Korea` -> **snapshot** (snapshot 20260708133615); points raw/verified 15/15
  - p139 South Korea live births, January–June 2026 (partial-year total) = **146,162** live births (2026-01-01..2026-06-30) [DISCARD: Wikipedia secondary compilation of the same KOSTAT series already represented by p1/p4; redundant and lower-vintage, add] quote: "\| January-June 2026 \| 146,162 \| \| \|"
  - p140 South Korea live births, January–June 2025 (comparable prior-year total) = **127,184** live births (2025-01-01..2025-06-30) [DISCARD: Same Wikipedia compilation; redundant with the KOSTAT-sourced 2025 series.] quote: "\| January-June 2025 \| 127,184 \| \| = \|"
  - p141 South Korea year-on-year change in live births, January–June 2026 vs 2025 = **18,978** live births (2026-01-01..2026-06-30) [DISCARD: Derived difference from the redundant Wikipedia table.] quote: "\| Difference \| +18,978 (+14.94%) \| \| \|"
  - p142 South Korea year-on-year percent change in live births, January–June 2026 vs 202 = **14.94** % (2026-01-01..2026-06-30) [DISCARD: Derived percentage from the redundant Wikipedia table.] quote: "\| Difference \| +18,978 (+14.94%) \| \| \|"
  - p143 South Korea annual live births, 2025 = **254,457** live births (2025-01-01..2025-12-31) [DISCARD: Wikipedia annual 2025 births; redundant with p79/p133/p157 KOSTAT/NABO figures.] quote: "\| 2025 \| 51,684,564 \| 254,457 \| 363,389 \| -108,931 \| 4.9 \| 7.0 \| -2.1 \| 0.800 \| 0.8 \|"
  - p144 South Korea annual live births, 2024 = **238,343** live births (2024-01-01..2024-12-31) [DISCARD: Wikipedia 2024 annual births; not needed for a July 2026 nowcast and redundant with the KOSTAT annual series.] quote: "\| 2024[42] \| 51,751,065 \| 238,343 \| 358,356 \| -120,013 \| 4.7 \| 7.0 \| -2.3 \| 0.748 \| 3.1 \|"
  - p145 South Korea annual live births, 2023 = **230,028** live births (2023-01-01..2023-12-31) [DISCARD: Wikipedia 2023 annual births; not needed and redundant.] quote: "\| 2023 \| 51,712,619 \| 230,028 \| 352,511 \| -122,483 \| 4.5 \| 6.9 \| -2.4 \| 0.721 \| 3.1 \|"
  - p146 South Korea annual live births, 2022 = **249,186** live births (2022-01-01..2022-12-31) [DISCARD: Wikipedia 2022 annual births; not needed and redundant.] quote: "\| 2022 \| 51,672,569 \| 249,186 \| 372,939 \| -123,753 \| 4.9 \| 7.3 \| -2.4 \| 0.778 \| 0.5 \|"
  - p147 South Korea total fertility rate, 2026 estimate (data as of January–April 2026) = **0.945** children per woman (2026-01-01..2026-04-30) [DISCARD: Wikipedia 2026 TFR estimate 0.945; superseded by observed monthly TFRs and not a birth count.] quote: "\| 2026(e) \| 51,609,121 \| \| \| \| \| \| \| 0.945* \| \|"
  - p148 South Korea total fertility rate, 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [DISCARD: Wikipedia 2025 TFR; redundant with p86/p135.] quote: "\| 2025 \| 51,684,564 \| 254,457 \| 363,389 \| -108,931 \| 4.9 \| 7.0 \| -2.1 \| 0.800 \| 0.8 \|"
  - p149 South Korea total fertility rate, 2024 = **0.748** children per woman (2024-01-01..2024-12-31) [DISCARD: Wikipedia 2024 TFR; redundant with p87/p136.] quote: "\| 2024[42] \| 51,751,065 \| 238,343 \| 358,356 \| -120,013 \| 4.7 \| 7.0 \| -2.3 \| 0.748 \| 3.1 \|"
  - p150 South Korea crude birth rate, 2025 (births per 1,000 population) = **4.9** live births per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Wikipedia 2025 crude birth rate; not used in any route.] quote: "\| 2025 \| 51,684,564 \| 254,457 \| 363,389 \| -108,931 \| 4.9 \| 7.0 \| -2.1 \| 0.800 \| 0.8 \|"
  - p151 South Korea crude birth rate, 2024 (births per 1,000 population) = **4.7** live births per 1,000 population (2024-01-01..2024-12-31) [DISCARD: Wikipedia 2024 crude birth rate; not used in any route.] quote: "\| 2024[42] \| 51,751,065 \| 238,343 \| 358,356 \| -120,013 \| 4.7 \| 7.0 \| -2.3 \| 0.748 \| 3.1 \|"
  - p152 South Korea projected total population, 2026 estimate = **51,609,121** people (2026-01-01..2026-12-31) [DISCARD: Projected population; not needed for a birth-count route.] quote: "\| 2026(e) \| 51,609,121 \| \| \| \| \| \| \| 0.945* \| \|"
  - p153 South Korea live births in October 2018 (monthly observation) = **26,500** live births (2018-10-01..2018-10-31) [DISCARD: 2018 October monthly births; too old and not needed given the seasonal-share route.] quote: "In 2018, fertility in South Korea became a topic of international debate after only 26,500 babies were born in October and an estimated 325,000 babies for the year"
- `https://supple.kr/news/cmsb86z360000bp3h1pxipjj0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ppomppu.co.kr/zboard/view.php?id=freeboard&no=9921995` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n.news.naver.com/article/654/0000159368` -> **snapshot** (snapshot 20260101181723); points raw/verified 15/15
  - p154 KOSTAT future population projection, total fertility rate, middle scenario, 2026 = **0.68** births per woman (2026-01-01..2026-12-31) [DISCARD: KOSTAT middle-scenario TFR 0.68 for 2026 is far below realized 2026 monthly TFRs (0.85–0.95); misleading as a level inpu] quote: "중위 시나리오 기준 합계출산율은 지난해 0.65명으로 저점을 찍은 뒤 올해 0.68명, 2027년 0.71명, 2028년 0.75명으로 점진적인 회복세를 보일 것으로 예측됐다."
  - p155 KOSTAT future population projection, total fertility rate, high scenario, 2026 = **0.8** births per woman (2026-01-01..2026-12-31) [DISCARD: KOSTAT high-scenario 0.80 for 2026 also below realized monthly TFRs; not usable as a level.] quote: "낙관적인 고위 시나리오에서는 지난해 0.75명에서 올해 0.80명, 2027년에는 0.84명까지 상승할 것으로 전망된다."
  - p156 NABO estimate, total fertility rate, 2025 = **0.8** births per woman (2025-01-01..2025-12-31) [DISCARD: NABO 2025 TFR; redundant with p86/p135.] quote: "국회예산정책처는 지난해 합계출산율을 0.80명, 출생아 수를 25만4000명으로 추산했다."
  - p157 NABO estimate, number of live births, 2025 = **254,000** live births (2025-01-01..2025-12-31) [DISCARD: NABO 2025 births; redundant with p79/p133.] quote: "국회예산정책처는 지난해 합계출산율을 0.80명, 출생아 수를 25만4000명으로 추산했다."
  - p158 NABO forecast, total fertility rate, 2026 = **0.9** births per woman (2026-01-01..2026-12-31) [DISCARD: NABO 0.90 forecast is close to realized but is a forecast, not an outcome; superseded by observed monthly TFRs.] quote: "예정처는 합계출산율이 지난해 0.8명에서 올해 0.9명으로 단기 반등할 것으로 내다봤으며 장기적으로는 2045년까지 0.92명 수준으로 증가할 것으로 전망했다."
  - p159 NABO forecast, total fertility rate, long-term level by 2045 = **0.92** births per woman (2045-01-01..2045-12-31) [DISCARD: 2045 long-term TFR; irrelevant to July 2026.] quote: "예정처는 합계출산율이 지난해 0.8명에서 올해 0.9명으로 단기 반등할 것으로 내다봤으며 장기적으로는 2045년까지 0.92명 수준으로 증가할 것으로 전망했다."
  - p160 Total fertility rate, October 2025 (monthly) = **0.81** births per woman (2025-10-01..2025-10-31) [DISCARD: October 2025 monthly TFR; not relevant to July 2026 level and redundant with the 2026 monthly TFR points.] quote: "지난해 10월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.81명으로 전년 동월 대비 0.02명 증가했다."
  - p161 Year-on-year change in total fertility rate, October 2025 vs October 2024 = **0.02** births per woman (2025-10-01..2025-10-31) [DISCARD: YoY change of October 2025 TFR; not relevant.] quote: "지난해 10월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.81명으로 전년 동월 대비 0.02명 증가했다."
  - p162 Average total fertility rate, January-October 2025 = **0.8** births per woman (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 average TFR; superseded by full-year 2025 TFR points.] quote: "지난해 1∼10월 평균 합계출산율은 0.80명 수준으로 연말까지 안정적인 회복세가 이어질 경우 4년 만에 0.8명대를 기록할 것으로 전망된다."
  - p163 Total fertility rate, 2021 = **0.81** births per woman (2021-01-01..2021-12-31) [DISCARD: 2021 TFR; historical context only, not used.] quote: "합계출산율은 2021년 0.81명에서 2022년 0.78명, 2023년에는 0.72명으로 역대 최저 수준까지 떨어졌다가 2024년 0.75명으로 9년 만에 반등했다."
  - p164 Total fertility rate, 2022 = **0.78** births per woman (2022-01-01..2022-12-31) [DISCARD: 2022 TFR; historical context only, not used.] quote: "합계출산율은 2021년 0.81명에서 2022년 0.78명, 2023년에는 0.72명으로 역대 최저 수준까지 떨어졌다가 2024년 0.75명으로 9년 만에 반등했다."
  - p165 Total fertility rate, 2023 = **0.72** births per woman (2023-01-01..2023-12-31) [DISCARD: 2023 TFR; redundant with p137.] quote: "합계출산율은 2021년 0.81명에서 2022년 0.78명, 2023년에는 0.72명으로 역대 최저 수준까지 떨어졌다가 2024년 0.75명으로 9년 만에 반등했다."
  - p166 Total fertility rate, 2024 = **0.75** births per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; redundant with p87/p136.] quote: "합계출산율은 2021년 0.81명에서 2022년 0.78명, 2023년에는 0.72명으로 역대 최저 수준까지 떨어졌다가 2024년 0.75명으로 9년 만에 반등했다."
  - p167 OECD average total fertility rate, 2023 = **1.43** births per woman (2023-01-01..2023-12-31) [DISCARD: OECD average; irrelevant.] quote: "경제협력개발기구(OECD) 회원국 평균 합계출산율 1.43명(2023년 기준)과 비교하면 여전히 낮은 수준이다."
  - p168 Replacement-level total fertility rate = **2.1** births per woman (not stated (page dated 2026-01-01)) [DISCARD: Replacement-level TFR; irrelevant.] quote: "현재 인구 규모를 유지하는 데 필요한 대체출산율 2.1명에는 크게 못 미치는 상황으로 구조적인 저출산 문제 해결까지는 상당한 시간이 필요할 것으로 보인다."
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000056178&newReportChk=list&highNationalPlanSubjectSn=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [base_rates] Seasonal and calendar effects

Hypothesis: July births reflect conceptions around October of the prior year; the July share of annual births is stable and can convert an annual estimate into a July figure. Calendar (lunar, holidays) effects are modest.

Queries issued by the searcher: Korea monthly live births seasonality July share of annual births; 출생아 수 월별 계절성 7월 비중; 통계청 "2025년 7월 인구동향" 출생아 수 21,863; 2025년 출생·사망통계 월별 출생아 수 비중 8.6% 7월; Korea monthly births seasonality July share Statistics Korea; 출생아 수 월별 계절성 7월 비중; 2025년 출생아 수 연간 25만명 월별 출생아 7월 2만1천명; 통계청 월별 출생아 수 2015 2016 2017 2018 2019 표 kosis; Korea monthly births seasonality July share of annual births Statistics Korea; 출생아 수 월별 계절성 7월 비중 통계청 인구동향; "2026년 5월 인구동향" 출생아 수 통계청 발표; "2025년 12월 인구동향" 연간 출생아 수 2025년 합계출산율

- `https://www.yna.co.kr/view/AKR20260923077000002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.seoul.co.kr/news/economy/2025/01/27/20250127500008` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/news/read?newsId=04877366645519440&mediaCodeNo=257` -> **snapshot** (snapshot 20260809115653); points raw/verified 11/4
  - p169 South Korea February daily average live births deviation from annual average (Ki = **19.6** % (not stated (page dated 2026-07-29)) [DISCARD: February daily-average deviation; not used directly (July share route uses p173).] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p170 South Korea June daily average live births deviation from annual average (Kim Je = **-8.4** % (not stated (page dated 2026-07-29)) [DISCARD: June daily-average deviation; not used.] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p171 South Korea December daily average live births deviation from annual average (Ki = **-8.9** % (not stated (page dated 2026-07-29)) [DISCARD: December daily-average deviation; not used.] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p172 South Korea gap between highest and lowest month in daily average live births (K = **28.5** % (not stated (page dated 2026-07-29)) [DISCARD: Seasonal range; not used.] quote: "가장 많은 달과 적은 달의 격차는 28.5%에 달한다."
- `https://www.seoul.co.kr/news/economy/2025/01/27/20250127500008` -> **snapshot** (snapshot 20250128134604); points raw/verified 15/15
  - p173 July share of total live births, South Korea, Jan 1981–Dec 2023 (July births / t = **7.8** % (1981-01-01..2023-12-31) [keep: July share of annual births 7.8% (1981-2023) — the seasonal conversion factor for the annual-to-July route.] quote: "7월에는 183만 812명(7.8%), 12월에는 181만 4420명(7.8%), 6월에는 175만 237명(7.5%)이 태어났다."
  - p174 July live births, South Korea, cumulative Jan 1981–Dec 2023 = **1,830,812** live births (1981-01-01..2023-12-31) [DISCARD: Cumulative July births 1981-2023; the share p173 is the usable conversion factor.] quote: "7월에는 183만 812명(7.8%), 12월에는 181만 4420명(7.8%), 6월에는 175만 237명(7.5%)이 태어났다."
  - p175 Total live births, South Korea, Jan 1981–Dec 2023 (denominator of monthly shares = **23,327,013** live births (1981-01-01..2023-12-31) [DISCARD: Denominator of the share; not needed once p173 is used.] quote: "43년간 총 출생아 수 2332만 7013명 가운데 10.0%의 비중을 차지했다."
  - p176 June share of total live births, South Korea, Jan 1981–Dec 2023 (lowest month) = **7.5** % (1981-01-01..2023-12-31) [DISCARD: June share; not used.] quote: "7월에는 183만 812명(7.8%), 12월에는 181만 4420명(7.8%), 6월에는 175만 237명(7.5%)이 태어났다."
  - p177 December share of total live births, South Korea, Jan 1981–Dec 2023 = **7.8** % (1981-01-01..2023-12-31) [DISCARD: December share; not used.] quote: "7월에는 183만 812명(7.8%), 12월에는 181만 4420명(7.8%), 6월에는 175만 237명(7.5%)이 태어났다."
  - p178 January share of total live births, South Korea, Jan 1981–Dec 2023 (highest mont = **10** % (1981-01-01..2023-12-31) [DISCARD: January share; not used.] quote: "43년간 총 출생아 수 2332만 7013명 가운데 10.0%의 비중을 차지했다."
  - p179 January live births, South Korea, cumulative Jan 1981–Dec 2023 = **2,332,681** live births (1981-01-01..2023-12-31) [DISCARD: January cumulative births; not used.] quote: "1월생이 233만 2681명으로 가장 많았다."
  - p180 February share of total live births, South Korea, Jan 1981–Dec 2023 = **9.6** % (1981-01-01..2023-12-31) [DISCARD: February share; not used.] quote: "그다음은 2월로 224만 44명(9.6%)이 태어났다."
  - p181 March share of total live births, South Korea, Jan 1981–Dec 2023 = **8.6** % (1981-01-01..2023-12-31) [DISCARD: March share; not used.] quote: "세 번째는 3월로 200만 1716명(8.6%)이 출생했다."
  - p182 Q1 (Jan–Mar) share of total live births, South Korea, Jan 1981–Dec 2023 = **28.2** % (1981-01-01..2023-12-31) [DISCARD: Q1 share; not used.] quote: "전체 비중은 28.2%, 국민 10명 중 3명이 1분기에 태어난 셈이다."
  - p183 October share of total live births, South Korea, Jan 1981–Dec 2023 = **8.4** % (1981-01-01..2023-12-31) [DISCARD: October share; not used.] quote: "10월이 196만 1332명(8.4%)으로 네 번째, 9월이 192만 1065명(8.2%)으로 다섯번째였다."
  - p184 September share of total live births, South Korea, Jan 1981–Dec 2023 = **8.2** % (1981-01-01..2023-12-31) [DISCARD: September share; not used.] quote: "10월이 196만 1332명(8.4%)으로 네 번째, 9월이 192만 1065명(8.2%)으로 다섯번째였다."
  - p185 April share of total live births, South Korea, Jan 1981–Dec 2023 = **8.1** % (1981-01-01..2023-12-31) [DISCARD: April share; not used.] quote: "출생아 수가 여섯번째로 많은 달은 4월로 188만 795명(8.1%)이 태어났다."
  - p186 November share of total live births, South Korea, Jan 1981–Dec 2023 = **8** % (1981-01-01..2023-12-31) [DISCARD: November share; not used.] quote: "일곱번째는 한겨울로 진입하기 직전인 11월(187만 1314명)로, 비중은 8.0%였다."
  - p187 August share of total live births, South Korea, Jan 1981–Dec 2023 = **8** % (1981-01-01..2023-12-31) [DISCARD: August share; not used.] quote: "그다음은 한여름인 8월 186만 6496명(8.0%), 가정의 달인 5월 185만 6101명(7.9%) 순으로 집계됐다."
- `https://www.donga.com/news/article/all/20250924/132453847/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n.news.naver.com/article/016/0002436180` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://app.yonhapnewstv.co.kr/news/AKR20260923135712MsI` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.nate.com/view/20250303n02458` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532&listChk=list` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://marketinsight.hankyung.com/article/202509244939i` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://archives.kdischool.ac.kr/bitstream/11125/34103/1/WP%2019-19.pdf` -> **snapshot** (snapshot 20231119050826); points raw/verified 15/15
  - p188 South Korea January live births, 1997 (largest month of that year) = **60,734** live births (1997-01-01..1997-01-31) [DISCARD: 1997 monthly births; too old for level, superseded by recent seasonal shares.] quote: "In 1997, 60,734 was born in January which was the biggest in the year"
  - p189 South Korea June live births, 1997 (smallest month of that year) = **50,422** live births (1997-06-01..1997-06-30) [DISCARD: 1997 monthly births; too old.] quote: "whereas the smallest number, 50,422 was born in June"
  - p190 South Korea adjusted January live births, 2015 = **40,561** live births (2015-01-01..2015-01-31) [DISCARD: 2015 adjusted January births; not needed.] quote: "2015 31,636 40,561 38,259 39,028 0.78 2.38 0.85 0.79 0.90"
  - p191 South Korea adjusted January live births, 2016 = **38,133** live births (2016-01-01..2016-01-31) [DISCARD: 2016 adjusted January births; not needed.] quote: "2016 30,880 38,133 36,031 36,900 0.75 1.97 0.77 0.79 0.80"
  - p192 South Korea adjusted January live births, 2017 = **33,710** live births (2017-01-01..2017-01-31) [DISCARD: 2017 adjusted January births; not needed.] quote: "2017 26,506 33,710 32,677 32,125 0.59 0.71 0.51 0.42 0.48"
  - p193 South Korea adjusted January live births, 2018 = **31,159** live births (2018-01-01..2018-01-31) [DISCARD: 2018 adjusted January births; not needed.] quote: "2018 24,335 31,159 29,544 29,019 0.43 0.58 0.55 0.58 0.51"
  - p194 South Korea adjusted December live births, 2018 = **24,335** live births (2018-12-01..2018-12-31) [DISCARD: 2018 adjusted December births; not needed.] quote: "2018 24,335 31,159 29,544 29,019 0.43 0.58 0.55 0.58 0.51"
  - p195 South Korea adjusted February live births, 2018 = **29,544** live births (2018-02-01..2018-02-28) [DISCARD: 2018 adjusted February births; not needed.] quote: "2018 24,335 31,159 29,544 29,019 0.43 0.58 0.55 0.58 0.51"
  - p196 South Korea adjusted March live births, 2018 = **29,019** live births (2018-03-01..2018-03-31) [DISCARD: 2018 adjusted March births; not needed.] quote: "2018 24,335 31,159 29,544 29,019 0.43 0.58 0.55 0.58 0.51"
  - p197 South Korea share of 2018 births born at 37-41 weeks of pregnancy = **92** % (2018-01-01..2018-12-31) [DISCARD: Gestation length; irrelevant to monthly level.] quote: "In 2018, 92% of babies were born in 37-41 weeks of pregnancy"
  - p198 South Korea share of 2018 births born before 37 weeks of pregnancy = **7.6** % (2018-01-01..2018-12-31) [DISCARD: Preterm share; irrelevant.] quote: "whereas 7.6%of them were born before 37 weeks"
  - p199 Average years from marriage to first birth, South Korea (2018 birth statistics) = **2.16** years (2018-01-01..2018-12-31) [DISCARD: Marriage-to-first-birth lag; too coarse to convert monthly marriages to July 2026 births.] quote: "the average year from marriage to the first birth is 2.16 year and to the second birth is 4.61 year"
  - p200 Average years from marriage to second birth, South Korea (2018 birth statistics) = **4.61** years (2018-01-01..2018-12-31) [DISCARD: Marriage-to-second-birth lag; too coarse.] quote: "the average year from marriage to the first birth is 2.16 year and to the second birth is 4.61 year"
  - p201 Minimum waiting time from first try to pregnancy (months) = **3.5** (range 3..4) as written "3-4", value check pending months (not stated (page dated 2005-12-07)) [DISCARD: Conception waiting time; irrelevant.] quote: "it will take 3-4 months because of the risk of the failure at fertilization and implantation"
  - p202 South Korea January share of births at other than hospital, 2018 (yearly average = **0.58** % (live births outside hospital / live births) (2018-01-01..2018-01-31) [DISCARD: Out-of-hospital birth share; irrelevant.] quote: "2018 24,335 31,159 29,544 29,019 0.43 0.58 0.55 0.58 0.51"
- `https://namu.wiki/w/대한민국/출산율/상세_통계` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (period year 2025 does not appear in the page text or URL (likely mis-dated): 7)

### d7 [shocks] Policy and demographic shocks

Hypothesis: Pronatalist policies (2024-2026), immigration, and COVID-era conception dips affect the level; identifying measurable policy effects or cohort sizes helps adjust the baseline.

Queries issued by the searcher: Statistics Korea monthly birth statistics 2025 2026 live births July; South Korea births 2025 rebound increase monthly statistics; 2026년 6월 인구동향 출생아 수 국가데이터처; "2026년 5월 인구동향" 출생아 증가율; South Korea monthly live births 2026 Statistics Korea population trends; South Korea births 2025 annual increase first rise in nine years Statistics Korea; 2025년 7월 출생아 수 2만1854명 인구동향; 2026년 6월 출생아 수 인구동향 발표; Statistics Korea monthly population trends 2026 births January February increase; South Korea 2025 total births 250,000 first increase Statistics Korea annual; "2026년 5월 인구동향" 출생아 수 증가; "2025년 7월 인구동향" 출생아 수 2만명 증가율

- `https://spanish.korea.net/NewsFocus/Society/view?articleId=301909` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asiae.co.kr/en/article/2026012815260243400` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.yonhapnewstv.co.kr/news/AKR20260225102345k7S` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/docViewer/skin/doc.html?fn=fd3fb0160c7fe7dcf6d47daffb4299e1&rs=/docViewer/result/2025.12/01/fd3fb0160c7fe7dcf6d47daffb4299e1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fr.yna.co.kr/view/AFR20251126001700884?section=national/index` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aa.com.tr/en/asia-pacific/south-korea-sees-rise-in-childbirths-for-9th-straight-month-in-march/3581765` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8266449` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mk.co.kr/news/economy/12081926` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsappapi.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n.news.naver.com/article/029/0003049656?sid=102&type=journalists` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kukinews.com/article/view/kuk202609230114` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] KOSTAT monthly release timing

Hypothesis: If June 2026 births (published ~late August 2026) are available, they would extend the own-history series to the month immediately before July and sharpen the YoY-scaling route (m1).

Queries issued by the searcher: 통계청 인구동향 2026년 6월 출생아 수; KOSTAT monthly live births June 2026 South Korea; 2025년 7월 인구동향 출생아 수 2만명 전년동월대비 통계청; 2026년 5월 인구동향 출생아 수 23,160명 국가데이터처; 통계청 인구동향 2026년 5월 출생아 수; KOSTAT monthly population trends 2026 June live births; 2025년 7월 출생아 수 인구동향 통계청 2만명; 2026년 4월 인구동향 출생아 수 전년동월대비 18.0%; 통계청 인구동향 2026년 6월 출생아 수; KOSTAT 인구동향 2026년 5월 출생아; 2025년 7월 인구동향 출생아 수 통계청; 통계청 2026년 4월 인구동향 출생아 18.0% 증가

- `https://www.donga.com/news/article/all/20250924/132453847/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1274698.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.womennews.co.kr/news/articleView.html?idxno=267782` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03230806642303400&mediaCodeNo=257` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41845` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260826079400002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03552246645551256` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8366129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Marriage lead indicator

Hypothesis: Marriages in mid-2024 to mid-2025 feed first births in 2026; a monthly marriage series for 2024–2025 would let us test whether the 2026 birth surge is marriage-driven and whether it persists into July.

Queries issued by the searcher: 2025년 혼인건수 월별 통계청 인구동향; 2024 월별 혼인 통계청 혼인건수; KOSTAT monthly marriage registrations 2025 South Korea; KOSIS 월별 혼인건수 2024 2025 통계표; 2025년 혼인·이혼 통계 월별 혼인건수 2025년 12월 24만 370건; 2025년 12월 인구동향 혼인 건수 전년동월 2025년 연간 혼인; site:kostat.go.kr 2025년 혼인 이혼 통계 보도자료; 2025년 월별 혼인건수 통계청 인구동향; 2024 월별 혼인 통계 통계청 혼인건수; "2025년 12월 및 4분기 인구동향" 혼인 건수 보도자료; "2025년 혼인·이혼 통계" 통계청 월별 혼인건수 2025년 12월; 2025년 혼인건수 월별 통계청 인구동향; 2024 월별 혼인 통계 통계청 혼인건수; 2025년 12월 및 4분기 인구동향 혼인 건수 연간 2025 혼인 24만건; 2025년 혼인·이혼 통계 통계청 월별 혼인건수 2025년 12월

- `https://gonggam.korea.kr/newsContentView.es?mid=a12503000000&section_id=NCCD_POLICY&news_id=d5cde5ee-3c8c-412e-957d-fbfe571f4470` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://27.101.222.81/board.es?mid=a10301020300&bid=204` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://view.asiae.co.kr/article/2026022509242475041` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kostat.go.kr/board.es?mid=a10301020300&bid=204` -> **snapshot** (snapshot 20250620173512); points raw/verified 0/0
- `https://mhdata.or.kr/mailing/Numbers325_260303_B1_Part.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/briefing/policyBriefingView.do?newsId=156679907` -> **snapshot** (snapshot 20260117202213); points raw/verified 15/15
  - p203 Total marriage registrations, South Korea, 2024 (full year) = **222,000** marriage (2024-01-01..2024-12-31) [DISCARD: 2024 annual marriages; not used in a route.] quote: "2024년 혼인건수는 22만 2,000건으로 전년대비 2만 9,000건이 늘어 14.8% 증가했습니다."
  - p204 Year-on-year change in marriage registrations, South Korea, 2024 vs 2023 = **29,000** marriage (2024-01-01..2024-12-31) [DISCARD: 2024 marriage YoY; not used.] quote: "2024년 혼인건수는 22만 2,000건으로 전년대비 2만 9,000건이 늘어 14.8% 증가했습니다."
  - p205 Year-on-year growth rate of marriage registrations, South Korea, 2024 = **14.8** % (2024-01-01..2024-12-31) [DISCARD: 2024 marriage growth; not used.] quote: "2024년 혼인건수는 22만 2,000건으로 전년대비 2만 9,000건이 늘어 14.8% 증가했습니다."
  - p206 Crude marriage rate (marriages per 1,000 population), South Korea, 2024 = **4.4** marriage per 1,000 person (2024-01-01..2024-12-31) [DISCARD: Crude marriage rate; not used.] quote: "인구 1,000명당 혼인건수를 의미하는 조혼인율은 4.4건으로 전년보다 0.6건 증가했습니다."
  - p207 Change in crude marriage rate, South Korea, 2024 vs 2023 = **0.6** marriage per 1,000 person (2024-01-01..2024-12-31) [DISCARD: Crude marriage rate change; not used.] quote: "인구 1,000명당 혼인건수를 의미하는 조혼인율은 4.4건으로 전년보다 0.6건 증가했습니다."
  - p208 Marriage registrations, South Korea, 2023 (implied prior year level) = **222,000** marriage (2023-01-01..2023-12-31) [DISCARD: Quote mislabels 2023 as 222,000 (the 2024 figure); the 2023 level is not actually stated, so the point is internally inc] quote: "2023년 혼인건수는 22만 2,000건으로 전년보다 2만 9,000건 늘어 14.8% 증가했습니다."
  - p209 Share of marriages where both spouses are first-married, South Korea, 2024 = **80.4** % (2024-01-01..2024-12-31) [DISCARD: First-marriage share; not used in a route.] quote: "전체 혼인건수 중에 남녀 모두 초혼인 부부는 80.4%, 남녀 모두 재혼인 부부는 10.4%를 차지했습니다."
  - p210 Share of marriages where both spouses are remarried, South Korea, 2024 = **10.4** % (2024-01-01..2024-12-31) [DISCARD: Remarriage share; not used.] quote: "전체 혼인건수 중에 남녀 모두 초혼인 부부는 80.4%, 남녀 모두 재혼인 부부는 10.4%를 차지했습니다."
  - p211 Growth rate of marriages among both-first-married couples, South Korea, 2024 vs  = **19.4** % (2024-01-01..2024-12-31) [DISCARD: First-marriage growth; not used.] quote: "전년대비 남녀 모두 초혼은 증가, 재혼은 감소했고 초혼부부의 혼인이 19.4%로 가장 크게 증가하였습니다."
  - p212 Marriage registrations with foreign spouse, South Korea, 2024 = **21,000** marriage (2024-01-01..2024-12-31) [DISCARD: Foreign-spouse marriages; not used.] quote: "외국인과의 혼인은 2만 1,000건으로 전년보다 1,000건이 늘어나면서 5.3% 증가했습니다."
  - p213 Marriage registrations with foreign wife, South Korea, 2024 = **16,000** marriage (2024-01-01..2024-12-31) [DISCARD: Foreign-wife marriages; not used.] quote: "외국인 여자와의 혼인은 1만 6,000건이고, 외국인 남자와의 혼인은 5,000건이었습니다."
  - p214 Marriage registrations with foreign husband, South Korea, 2024 = **5,000** marriage (2024-01-01..2024-12-31) [DISCARD: Foreign-husband marriages; not used.] quote: "외국인 여자와의 혼인은 1만 6,000건이고, 외국인 남자와의 혼인은 5,000건이었습니다."
  - p215 Marriage registrations, men aged early 30s, South Korea, 2024 = **87,000** marriage (2024-01-01..2024-12-31) [DISCARD: Marriages by men's age; not used.] quote: "남자의 연령별 혼인건수는 30대 초반에서 8만 7,000건, 30대 후반에서 4만 3,000건, 20대 후반에서 4만 건 순으로 많았습니다."
  - p216 Marriage registrations, women aged early 30s, South Korea, 2024 = **84,000** marriage (2024-01-01..2024-12-31) [DISCARD: Marriages by women's age; not used.] quote: "여성의 혼인내용은 먼저 연령별 혼인건수가 30대 초반 8만 4,000건 그리고 20대 후반이 6만 4,000건, 30대 후반이 2만 9,000건 순이었습니다."
  - p217 Marriage registrations, women aged late 20s, South Korea, 2024 = **64,000** marriage (2024-01-01..2024-12-31) [DISCARD: Marriages by women's age; not used.] quote: "여성의 혼인내용은 먼저 연령별 혼인건수가 30대 초반 8만 4,000건 그리고 20대 후반이 6만 4,000건, 30대 후반이 2만 9,000건 순이었습니다."
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=437660&act=view&mainXml=Y` -> **snapshot** (snapshot 20260612120752); points raw/verified 8/8
  - p218 Marriage registrations, South Korea, May 2025 (monthly) = **21,761** marriage (2025-05-01..2025-05-31) [DISCARD: May 2025 marriages; not used in a route.] quote: "혼인 건수는 21,761건으로 전년동월대비 4.0% 증가"
  - p219 Marriage registrations, South Korea, May 2025 vs May 2024, year-on-year change = **4** % (2025-05-01..2025-05-31) [DISCARD: May 2025 marriage YoY; not used.] quote: "혼인 건수는 21,761건으로 전년동월대비 4.0% 증가"
  - p220 Live births, South Korea, May 2025 (monthly) = **20,309** live birth (2025-05-01..2025-05-31) [DISCARD: May 2025 births; superseded by the 2026 series and not needed.] quote: "출생아 수는 20,309명으로 전년동월대비 3.8% 증가"
  - p221 Live births, South Korea, May 2025 vs May 2024, year-on-year change = **3.8** % (2025-05-01..2025-05-31) [DISCARD: May 2025 birth YoY; not used.] quote: "출생아 수는 20,309명으로 전년동월대비 3.8% 증가"
  - p222 Deaths, South Korea, May 2025 (monthly) = **28,510** death (2025-05-01..2025-05-31) [DISCARD: Deaths; irrelevant to births.] quote: "사망자 수는 28,510명으로 전년동월대비 0.0% 감소"
  - p223 Natural increase (live births minus deaths), South Korea, May 2025 = **-8,202** person (2025-05-01..2025-05-31) [DISCARD: Natural increase; irrelevant to births.] quote: "자연증가(출생아 수 - 사망자 수)는 -8,202명"
  - p224 Divorces, South Korea, May 2025 (monthly) = **7,413** divorce (2025-05-01..2025-05-31) [DISCARD: Divorces; irrelevant.] quote: "이혼 건수는 7,413건으로 전년동월대비 6.4% 감소"
  - p225 Divorces, South Korea, May 2025 vs May 2024, year-on-year change = **6.4** % (2025-05-01..2025-05-31) [DISCARD: Divorce YoY; irrelevant.] quote: "이혼 건수는 7,413건으로 전년동월대비 6.4% 감소"
- `https://m.korea.kr/briefing/pressReleaseView.do?newsId=156736731&pWise=mSub&pWiseSub=C8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/docViewer/skin/doc.html?fn=198107214&rs=/docViewer/result/2025.03/26/198107214` -> **snapshot** (snapshot 20250518105248); points raw/verified 0/0
- `https://kostat.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=433942` -> **snapshot** (snapshot 20250710082547); points raw/verified 9/9
  - p226 Marriage registrations in South Korea, September 2024 (monthly) = **15,368** marriage (2024-09-01..2024-09-30) [DISCARD: September 2024 marriages; not used.] quote: "혼인 건수는 15,368건으로 전년동월대비 18.8% 증가"
  - p227 Year-on-year change in marriage registrations, South Korea, September 2024 = **18.8** % (2024-09-01..2024-09-30) [DISCARD: September 2024 marriage YoY; not used.] quote: "혼인 건수는 15,368건으로 전년동월대비 18.8% 증가"
  - p228 Live births in South Korea, September 2024 (monthly) = **20,590** live birth (2024-09-01..2024-09-30) [DISCARD: September 2024 births; not used.] quote: "출생아 수는 20,590명으로 전년동월대비 10.1% 증가"
  - p229 Year-on-year change in live births, South Korea, September 2024 = **10.1** % (2024-09-01..2024-09-30) [DISCARD: September 2024 birth YoY; not used.] quote: "출생아 수는 20,590명으로 전년동월대비 10.1% 증가"
  - p230 Deaths in South Korea, September 2024 (monthly) = **29,362** death (2024-09-01..2024-09-30) [DISCARD: Deaths; irrelevant.] quote: "사망자 수는 29,362명으로 전년동월대비 3.8% 증가"
  - p231 Year-on-year change in deaths, South Korea, September 2024 = **3.8** % (2024-09-01..2024-09-30) [DISCARD: Death YoY; irrelevant.] quote: "사망자 수는 29,362명으로 전년동월대비 3.8% 증가"
  - p232 Divorces in South Korea, September 2024 (monthly) = **7,531** divorce (2024-09-01..2024-09-30) [DISCARD: Divorces; irrelevant.] quote: "이혼 건수는 7,531건으로 전년동월대비 0.4% 증가"
  - p233 Year-on-year change in divorces, South Korea, September 2024 = **0.4** % (2024-09-01..2024-09-30) [DISCARD: Divorce YoY; irrelevant.] quote: "이혼 건수는 7,531건으로 전년동월대비 0.4% 증가"
  - p234 Natural increase (live births minus deaths) in South Korea, September 2024 = **-8,772** person (2024-09-01..2024-09-30) [DISCARD: Natural increase; irrelevant.] quote: "자연증가(출생아 수 - 사망자 수)는 -8,772명"
- `https://www.yna.co.kr/view/AKR20250423064400002` -> **snapshot** (snapshot 20250529111329); points raw/verified 15/15
  - p235 South Korea monthly marriage registrations, February 2025 = **19,370** marriage registration (2025-02-01..2025-02-28) [DISCARD: February 2025 marriages; not used.] quote: "2월 혼인 건수는 1년 전보다 2천422건(14.3%) 늘어난 1만9천370건이었다."
  - p236 South Korea year-on-year increase in monthly marriage registrations, February 20 = **2,422** marriage registration (2025-02-01..2025-02-28) [DISCARD: February 2025 marriage YoY; not used.] quote: "2월 혼인 건수는 1년 전보다 2천422건(14.3%) 늘어난 1만9천370건이었다."
  - p237 South Korea year-on-year percent change in monthly marriage registrations, Febru = **14.3** % (2025-02-01..2025-02-28) [DISCARD: February 2025 marriage YoY %; not used.] quote: "2월 혼인 건수는 1년 전보다 2천422건(14.3%) 늘어난 1만9천370건이었다."
  - p238 South Korea monthly marriage registrations, February 2017 (comparison year) = **21,501** marriage registration (2017-02-01..2017-02-28) [DISCARD: 2017 February marriages; not used.] quote: "2월 기준으로 2017년(2만1천501건) 이후 8년 만에 가장 많다."
  - p239 Consecutive months of year-on-year increase in South Korea monthly marriage regi = **11** month (2024-04-01..2025-02-28) [DISCARD: Marriage streak length; superseded by p54/p60.] quote: "혼인은 작년 4월 이후 11개월째 늘고 있다."
  - p240 South Korea monthly live births, February 2025 = **20,035** live birth (2025-02-01..2025-02-28) [DISCARD: February 2025 births; not used.] quote: "지난 2월 출생아는 2만35명으로 1년 전보다 622명(3.2%) 늘었다."
  - p241 South Korea year-on-year increase in monthly live births, February 2025 = **622** live birth (2025-02-01..2025-02-28) [DISCARD: February 2025 birth YoY; not used.] quote: "지난 2월 출생아는 2만35명으로 1년 전보다 622명(3.2%) 늘었다."
  - p242 South Korea year-on-year percent change in monthly live births, February 2025 = **3.2** % (2025-02-01..2025-02-28) [DISCARD: February 2025 birth YoY %; not used.] quote: "지난 2월 출생아는 2만35명으로 1년 전보다 622명(3.2%) 늘었다."
  - p243 Consecutive months of year-on-year increase in South Korea monthly live births,  = **8** month (2024-07-01..2025-02-28) [DISCARD: Birth streak through Feb 2025; superseded by p45/p61.] quote: "월별 출생아는 작년 7월부터 8개월째 증가세가 계속되고 있다."
  - p244 South Korea total fertility rate, February 2025 = **0.82** births per woman (2025-02-01..2025-02-28) [DISCARD: February 2025 TFR; not used.] quote: "2월 합계출산율은 1년 전보다 0.05명 증가했지만 0.82명에 그쳤다."
  - p245 South Korea year-on-year change in total fertility rate, February 2025 = **0.05** births per woman (2025-02-01..2025-02-28) [DISCARD: February 2025 TFR YoY; not used.] quote: "2월 합계출산율은 1년 전보다 0.05명 증가했지만 0.82명에 그쳤다."
  - p246 South Korea monthly deaths, February 2025 = **30,283** death (2025-02-01..2025-02-28) [DISCARD: Deaths; irrelevant.] quote: "2월 사망자는 3만283명으로 1년 전보다 401명(1.3%) 늘었다."
  - p247 South Korea monthly divorces, February 2025 = **7,347** divorce (2025-02-01..2025-02-28) [DISCARD: Divorces; irrelevant.] quote: "2월 이혼은 1년 전보다 7건(0.1%) 줄어든 7천347건으로 집계됐다."
  - p248 South Korea natural decrease of population (deaths minus births), February 2025 = **10,248** person (2025-02-01..2025-02-28) [DISCARD: Natural decrease; irrelevant.] quote: "사망자 수가 출생아 수를 웃돌면서 2월 인구는 1만248명 자연 감소했다."
  - p249 Consecutive months of natural population decline in South Korea, through Februar = **64** month (2019-11-01..2025-02-28) [DISCARD: Natural-decline streak; irrelevant.] quote: "인구는 2019년 11월 이후 64개월째 자연 감소하고 있다."

### b3 [administrative] Resident registration births

Hypothesis: 주민등록 birth registrations for July 2026 (available earlier than KOSTAT occurrence data) would provide a near-real-time check on the July level.

Queries issued by the searcher: 주민등록 출생자 수 2026년 7월 행정안전부; 행정안전부 주민등록 인구통계 월별 출생자 수 2026; "2026년 7월" 주민등록 출생등록 전국 명; 주민등록 인구통계 2026년 7월 출생자 수 증가 행안부 8월 1일 발표; 주민등록 출생자 수 2026년 7월; 행정안전부 주민등록 인구통계 출생 2026년 6월; 2026년 7월 주민등록 출생 24761; "7월" 출생신고 주민등록 2026년 8월 행안부 인구통계 발표; 주민등록 출생자 수 2026년 7월; 행정안전부 주민등록 인구통계 출생 2026년 6월; "출생등록" 2026년 7월 주민등록 출생 24761; 주민등록 인구통계 2026년 7월 출생아 수 전년동월대비 증가 행정안전부 발표

- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?bid=204&mid=a10301020000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy//materialView.do?num=287353&pg=&pp=&device=&search_txt=&topic=&type=J&depth1=A0000&depth2=A0400` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mlbpark.donga.com/mp/b.php?p=1&b=bullpen&id=202608030117768000&select=&query=%EC%A0%84%EC%9E%A5%EC%97%B0&shop=&subselect=&subquery=&user=&site` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nabo.go.kr/board/file/down.do?fid=33319503` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.data.go.kr/data/15099155/fileData.do` -> **snapshot** (snapshot 20260716110723); points raw/verified 0/0
- `https://stat.jeonbuk.go.kr/2011html/sub2/index.jsp?b_idx=8&bd_idx=1593&gubun=view&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jeongeup.go.kr/board/view.jeongeup?boardId=BBS_0000145&menuCd=DOM_000000105002000000&paging=ok&startPage=1&dataSid=1416956` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tongyeong.go.kr/00681/00827/00837.web?amode=view&idx=662037&gcode=1020&ccx=Y&cpage=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jumin.mois.go.kr/` -> **snapshot** (snapshot 20260717112850); points raw/verified 0/0
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth rate', 'korea population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p42', 'p94', 'p109', 'p130'] All report the same KOSTAT May 2026 figure of 23,160 births; they are copies of one underlying release, not independent confirmation.
- corroborating: ['p2', 'p43', 'p95', 'p110', 'p131'] Same +2,781 May 2026 YoY change repeated across outlets; single source.
- corroborating: ['p3', 'p44', 'p96', 'p111', 'p132'] Same +13.6% May 2026 growth rate; single source.
- corroborating: ['p4', 'p47', 'p98', 'p112', 'p127'] Same Jan–May 2026 cumulative 122,694; single KOSTAT release.
- corroborating: ['p5', 'p48', 'p99', 'p113', 'p128'] Same +16,166 Jan–May YoY change.
- corroborating: ['p6', 'p49', 'p100', 'p114', 'p129'] Same +15.2% Jan–May growth rate.
- corroborating: ['p7', 'p50', 'p115'] Same 2019 Jan–May comparison 134,433.
- corroborating: ['p8', 'p46', 'p97', 'p116'] Same May 2019 comparison 25,299.
- corroborating: ['p9', 'p51', 'p101', 'p117', 'p126'] Same May 2026 TFR 0.85.
- corroborating: ['p10', 'p52', 'p102', 'p118'] Same +0.10 TFR YoY change for May 2026.
- corroborating: ['p11', 'p103', 'p119'] Same 63.0% first-birth share May 2026.
- corroborating: ['p12', 'p105', 'p120'] Same 31.7% second-birth share May 2026.
- corroborating: ['p13', 'p106', 'p121'] Same 5.3% third-or-higher share May 2026.
- corroborating: ['p15', 'p39', 'p107', 'p123'] Same May 2026 marriages 20,368, -6.4% YoY.
- corroborating: ['p16', 'p25'] Same July 2025 births 21,803; two outlets of one KOSTAT release.
- corroborating: ['p17', 'p27'] Same +5.9% July 2025 growth rate.
- corroborating: ['p20', 'p37'] Same July 2025 marriages 20,394.
- corroborating: ['p55', 'p58'] Same Feb 2026 births 22,898.
- corroborating: ['p56', 'p75'] Same Feb 2026 marriages 18,557, -4.2%.
- corroborating: ['p79', 'p143'] 2025 annual births ~254,500 vs 254,457; consistent provisional figures.
- corroborating: ['p86', 'p135', 'p148'] 2025 TFR 0.80 consistent across sources.
- corroborating: ['p87', 'p136', 'p149', 'p166'] 2024 TFR 0.75 consistent.
- corroborating: ['p137', 'p165'] 2023 TFR 0.72 consistent.
- corroborating: ['p139', 'p140', 'p141', 'p142'] Wikipedia Jan–Jun 2026 vs 2025 totals; internally consistent but a secondary compilation, lower reliability than KOSTAT releases.
- corroborating: ['p124', 'p125', 'p147'] Q1 2026 TFR 0.95 and April 0.93 consistent with the 0.945 estimate; all point to a strong 2026 rebound.
- conflicting: ['p154', 'p155', 'p158'] KOSTAT projection (0.68–0.80) and NABO (0.90) bracket the observed 2026 monthly TFRs (0.85–0.95); the projections are pre-rebound and understate the realized level, so they are context only, not direc
- corroborating: ['p169', 'p170', 'p171', 'p172'] Seasonal daily-average deviations; February high, June/December low, consistent with the 1981–2023 monthly shares.
- corroborating: ['p173', 'p174', 'p175', 'p176', 'p177', 'p178', 'p179', 'p180', 'p181', 'p182', 'p183', 'p184', 'p185', 'p186', 'p187'] Long-run monthly birth shares; July 7.8% is a stable seasonal anchor for converting an annual level to July.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p45', 'p61'] All describe the same KOSTAT monthly Population Trends release (May 2026 and cumulative Jan-May 2026): May level 23,160, +2,781 (+13.6%), cumulative 122,694, +16,166 (+15.2%), and a 23-month (through 
- corroborating: ['p58', 'p59', 'p66', 'p67', 'p55', 'p61'] February 2026 births 22,898, +2,747 (+13.6%), 7-year maximum, 20-month streak — consistent with the May release's picture of a strong, broad-based 2026 upswing. Same KOSTAT source across different new
- corroborating: ['p16', 'p17', 'p25', 'p26', 'p27', 'p29', 'p30', 'p31'] July 2025 births 21,803, +1,223 (+5.9%); Jan-Jul 2025 cumulative 147,804 (+7.2%). Two outlets (mods.go.kr and newspim) report the same KOSTAT figures — one measurement, not two.
- corroborating: ['p139', 'p140', 'p141', 'p142', 'p4', 'p5'] Wikipedia Jan-Jun 2026 total 146,162 vs Jan-Jun 2025 127,184 (+14.94%) is consistent with the KOSTAT Jan-May figures (122,694, +15.2%): implied June 2026 ≈ 23,468, a plausible continuation. Wikipedia 
- corroborating: ['p15', 'p39', 'p40', 'p41', 'p56', 'p57', 'p75', 'p76', 'p54', 'p60'] Marriage registrations turned down in 2026: Feb 18,557 (-4.2%, first decline after 22-month streak), May 20,368 (-6.4%). This is a headwind for first births ~1-2 years later, i.e. it argues the 2026 b
- corroborating: ['p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p133', 'p143', 'p148', 'p135', 'p136', 'p137', 'p156', 'p157'] 2025 annual births ~254,000-254,500 and TFR 0.80 across KOSTAT, NABO and Wikipedia — same underlying annual release, mutually consistent. First-birth share rising (62.4%) confirms the marriage-cohort 
- corroborating: ['p89', 'p90', 'p173', 'p174', 'p175', 'p176', 'p177', 'p178', 'p179', 'p180', 'p181', 'p182', 'p183', 'p184', 'p185', 'p186', 'p187'] Two independent seasonal-share sources: 2025 monthly shares (Jan 9.5%, Feb/Jun/Dec 7.9%) and 1981-2023 cumulative shares (July 7.8%, June 7.5%, Jan 10.0%). Both show July as a mid-to-high month; the l
- corroborating: ['p169', 'p170', 'p171', 'p172'] Daily-average deviations (Feb +19.6%, Jun -8.4%, Dec -8.9%, range 28.5%) are consistent with the share-based seasonality: July sits between the June trough and the autumn peak, so a July share near 8.
- corroborating: ['p124', 'p125', 'p126', 'p9', 'p10', 'p69', 'p70'] Monthly TFR: Q1 2026 0.95, April 0.93, May 0.85, Feb 0.93 — all well above 2025 monthly levels, confirming the 2026 upswing is real and broad. TFR is a rate, not a count, so it constrains direction ra
- conflicting: ['p134', 'p133'] The Seoul Shinmun 'late 200,000s' 2026 forecast (p134 coded as 200,000 upper end) is a journalistic projection, not a KOSTAT figure, and its coded value is the lower bound of the phrase; it is directi

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 YoY growth factor applied to July 2025 births | 1.12 | 1.02..1.24 | 1.006..1.257 (widened) | ratio | m1 (m1) | 2026 monthly YoY growth has run +13.6% (Feb), +13.6% (May), +15.2% cumulative Jan–May, and Jan–Jun 2026 (+14.94%) implies June ≈ 23,468. July 2025 was itself +5.9% YoY, so a slightly moderated 2026 growth is plausible as the marriage-registration decline (Feb −4.2%, May −6.4%) starts to bite. Centra | July 2026 continues the 2026 upswing at a somewhat moderated pace relative to spring 2026. | June 2026 births (published late August) showing YoY growth below ~5% or above ~20%. |
| a2 | July share of 2026 annual live births | 0.083 | 0.076..0.09 | 0.05848..0.117 (widened) | ratio | unused | Long-run July share is 7.8% (p173); 2025 monthly shares show July between the June trough (7.9%) and the autumn peak, and daily-average deviations put July above the annual average. 8.3% is a modest upward adjustment for the recent shift toward higher summer shares, with a band spanning the long-run | The 2026 seasonal pattern resembles the recent (2020s) pattern rather than the 1981–2023 average. | KOSTAT monthly shares for 2026 showing July below 7.5% or above 9.5%. |
| a3 | 2026 annual live births level | 285,000 | 265,000..305,000 | 201,029..402,057 (widened) | live births/year | unused | Jan–May 2026 cumulative 122,694 (+15.2%) and Jan–Jun ~146,162 imply a full-year total well above 2025's 254,457; the Seoul Shinmun 'late 200,000s' projection and the sustained double-digit growth support ~285,000, with a band from 265,000 to 305,000. | The 2026 upswing persists through the second half of the year. | June–July 2026 monthly births falling back toward 2025 levels. |
| a4 | July 2026 YoY growth factor applied to July 2025 births (own-history route) | 1.13 | 1.03..1.25 | 1.015..1.269 (widened) | ratio | m3 (m3) | Same evidence base as a1 but anchored on the Jan–Jun 2026 YoY growth of +14.94% (p142) and the June 2026 implied level (~23,468 from p139 minus p4), which is a closer lead-in to July than the May figure. Central 1.13, band spanning near-flat to continued double-digit growth. | July 2026 continues the 2026 upswing at roughly the Jan–Jun pace. | June 2026 births (published late August) showing YoY growth below ~5% or above ~20%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 24,518 | ['p16'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | n/a | [] / ['a2', 'a3'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |
| m3 | formula_mc | 24,733 | ['p16'] / ['a4'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p16 * a1; Monte Carlo P10 to P90 19,811 to 30,446; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p16 * a4; Monte Carlo P10 to P90 19,953 to 30,727; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 24,518 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 24,733 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.38.

Result: central **24,625** person, 80% interval [17,875, 33,925] person, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

Unit of the estimate: person (live births; total for 2026-07-01 to 2026-07-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first published in Statistics Korea's monthly Population Trends release, is 24,625 person (80% model-based interval 17,875 to 33,925 person).

Evidence: the observed anchor is July 2025 births of 21,803 live births. Two YoY-scaling routes apply growth factors of 1.12 (range 1.006 to 1.257) and 1.13 (range 1.015 to 1.269), giving 24,518 person and 24,733 person. Both factors are analyst assumptions, not observations, and both routes share the same KOSTAT monthly source, so they are not independent. Code combined them as two equal-weight blocks via geometric mean; the interval is conditional on these assumptions, not a demonstrated accuracy guarantee.

Main risk: a sharp break in the 2026 upswing, e.g. the marriage-registration decline biting harder than assumed. Better evidence would be July 2026 birth-registration or preliminary monthly data, which is unavailable before the cutoff.

Unit of the estimate: person (live births; total for 2026-07-01 to 2026-07-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 YoY growth factor applied to July 2025 births: 1.12 ratio, range 1.006 to 1.257 (range widened by code); used by m1. Overturned by: June 2026 births (published late August) showing YoY growth below ~[n] or above ~[n].
- a4 July 2026 YoY growth factor applied to July 2025 births (own-history route): 1.13 ratio, range 1.015 to 1.269 (range widened by code); used by m3. Overturned by: June 2026 births (published late August) showing YoY growth below ~[n] or above ~[n].

Method details (computed by code):
- m1 formula_mc: p16 * a1; Monte Carlo P10 to P90 19,811 to 30,446; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p16 * a4; Monte Carlo P10 to P90 19,953 to 30,727; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 24,518 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 24,733 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.38.

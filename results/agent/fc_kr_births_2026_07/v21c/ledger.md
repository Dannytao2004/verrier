# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population movement statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends / population movement statistics

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly birth series

Hypothesis: July 2026 births can be projected from the most recent monthly birth counts and the seasonal pattern of July relative to adjacent months and prior years. The role is to anchor the level and seasonality; the transfer assumption is that recent trends and seasonal factors persist.

Queries issued by the searcher: Statistics Korea monthly live births 2025 2026 population trends; KOSTAT 출생아 수 월별 2025 2026 인구동향; 2025년 7월 인구동향 출생아 수 21,854명 통계청; 2024년 7월 출생아 수 인구동향 20,000명대

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://47.newstomato.com/ReadNews.aspx?no=1308574` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [administrative] Birth registration records and provisional monthly counts

Hypothesis: The number of birth registrations in July 2026, as recorded by local governments and compiled by KOSTAT, is the direct administrative trace of live births. The role is to provide a near-complete count; the transfer assumption is that registration timing closely matches occurrence month, with only minor lag.

Queries issued by the searcher: South Korea birth registration July 2026 KOSTAT monthly population trends; KOSTAT 출생아 수 2026년 7월 인구동향

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=447111` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://admin.korea.kr/briefing/pressReleaseView.do?newsId=156783095` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260923077000002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Marriage registrations as a leading indicator

Hypothesis: Marriage registrations in South Korea lead first births by roughly 1–2 years. A change in marriages around mid-2024 to mid-2025 should be associated with a proportional change in births in July 2026. The role is to adjust the recent birth trend for a marriage-driven shift; the transfer assumption is a stable marriage-to-first-birth lag and share.

Queries issued by the searcher: South Korea monthly marriage registrations 2025 KOSTAT statistics; KOSTAT 혼인 건수 월별 2025 통계; 2026년 6월 인구동향 출생 혼인 국가데이터처; "2026년 5월 인구동향" 혼인 건수 출생아 수; "2026년 5월 인구동향" 혼인 6.4% 감소 출생아; South Korea births July 2025 2024 monthly number KOSTAT 인구동향 7월 출생아 수

- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000062839&listChk=list&backUrl=https%3A%2F%2Fnsp.nanet.go.kr%2Fsearch%2Flist` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://woman.donga.com/issue/article/all/12/6178276/1` -> **snapshot** (snapshot 20260520100445); points raw/verified 15/6
  - p1 South Korea marriage registrations, year-on-year increase rate, 2024 = **14.8** % (2024-01-01..2024-12-31) [keep: ] quote: "2024년 22만2000건, 2025년에는 24만370건으로 각각 14.8%, 8.1% 증가한 것이다."
  - p2 South Korea marriage registrations, year-on-year increase rate, 2025 = **8.1** % (2025-01-01..2025-12-31) [keep: ] quote: "2024년 22만2000건, 2025년에는 24만370건으로 각각 14.8%, 8.1% 증가한 것이다."
  - p3 South Korea marriage registrations, December 2025 year-on-year increase rate = **13.4** % (2025-12-01..2025-12-31) [keep: ] quote: "특히 2025년 12월 한 달간 혼인 건수는 2만5527건으로 전년 동월 대비 13.4%나 급증하며 강한 상승세를 기록했다."
  - p4 South Korea live births, annual increase rate, 2025 vs 2024 = **6.8** % (2025-01-01..2025-12-31) [keep: ] quote: "국가데이터처가 발표한 2025년 인구동향조사에 따르면 지난해 출생아 수는 25만4500명으로 전년보다 1만6100명(6.8%) 증가했다."
  - p5 South Korea total fertility rate, 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "합계출산율은 0.8명을 기록해 2021년(0.81명) 이후 4년 만에 가장 높은 수준을 회복했다."
  - p6 South Korea total fertility rate, 2021 (comparison) = **0.81** children per woman (2021-01-01..2021-12-31) [DISCARD: 2021 TFR is a comparison value inside the same sentence as p5; it adds no independent information for a July 2026 level ] quote: "합계출산율은 0.8명을 기록해 2021년(0.81명) 이후 4년 만에 가장 높은 수준을 회복했다."
- `https://mhdata.or.kr/mailing/Numbers325_260303_B1_Part.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://m.sedaily.com/NewsView/2GY0Z41268/GC13` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (number: more than one number in value_as_written: 7; period_end missing or unparseable: 1; number: unknown scale word '만': 1)

### d4 [base_rates] Seasonal adjustment factors for July

Hypothesis: July births in South Korea have a consistent seasonal relationship to the annual total or to adjacent months. The role is to convert an annual or quarterly estimate into a July-specific figure; the transfer assumption is that the seasonal factor is stable across recent years.

Queries issued by the searcher: South Korea monthly births by month 2020 2021 2022 2023 2024 statistics; KOSTAT 월별 출생아 수 2025년 7월 인구동향; 월별 출생아 수 2025년 12월 인구동향 연간 출생아 2025년 25만명; namu wiki 대한민국 출산율 상세통계 월별 출생아 수 2020 2021 2022 2023 2024 2025 7월

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p7 South Korea live births, July 2025 (monthly Population Trends) = **21,803** persons (live births) (2025-07-01..2025-07-31) [keep: ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p8 South Korea live births year-on-year change rate, July 2025 vs July 2024 = **5.9** % (2025-07-01..2025-07-31) [keep: ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p9 South Korea deaths, July 2025 = **27,979** persons (deaths) (2025-07-01..2025-07-31) [DISCARD: July 2025 deaths are not an input to a birth estimate; retained only as context and not usable in any executable method.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p10 South Korea deaths year-on-year change rate, July 2025 vs July 2024 = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Deaths y/y rate is irrelevant to the birth target and redundant with p9.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p11 South Korea marriages, July 2025 = **20,394** cases (marriages) (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p12 South Korea marriages year-on-year change rate, July 2025 vs July 2024 = **8.4** % (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p13 South Korea divorces, July 2025 = **7,826** cases (divorces) (2025-07-01..2025-07-31) [DISCARD: Divorce count is not a birth input and has no established transfer to the target.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p14 South Korea divorces year-on-year change rate, July 2025 vs July 2024 = **1.4** % (2025-07-01..2025-07-31) [DISCARD: Divorce y/y rate is irrelevant and redundant with p13.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p15 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (natural increase) (2025-07-01..2025-07-31) [DISCARD: Natural increase is a derived identity from births and deaths; it cannot be used to estimate births without already know] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=443681&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www6.seoul.co.kr/news/economy/2025/01/27/20250127500008` -> **snapshot** (snapshot 20250128134604); points raw/verified 15/5
  - p16 South Korea January share of total births, 1981–2023 = **10** % (1981-01-01..2023-12-31) [keep: Kept as part of the long-run monthly-share set; only the July share (p20) is usable, but the set documents the seasonal ] quote: "43년간 총 출생아 수 2332만 7013명 가운데 10.0%의 비중을 차지했다."
  - p17 South Korea February share of total births, 1981–2023 = **9.6** % (1981-01-01..2023-12-31) [keep: Kept as part of the long-run monthly-share set; not a July input.] quote: "그다음은 2월로 224만 44명(9.6%)이 태어났다."
  - p18 South Korea March share of total births, 1981–2023 = **8.6** % (1981-01-01..2023-12-31) [keep: Kept as part of the long-run monthly-share set; not a July input.] quote: "세 번째는 3월로 200만 1716명(8.6%)이 출생했다."
  - p19 South Korea Q1 (Jan–Mar) share of total births, 1981–2023 = **28.2** % (1981-01-01..2023-12-31) [keep: Kept as the Q1 aggregate that validates the monthly shares; not a July input.] quote: "전체 비중은 28.2%, 국민 10명 중 3명이 1분기에 태어난 셈이다."
  - p20 South Korea July share of total births, 1981–2023 = **7.8** % (1981-01-01..2023-12-31) [keep: ] quote: "7월에는 183만 812명(7.8%), 12월에는 181만 4420명(7.8%), 6월에는 175만 237명(7.5%)이 태어났다."
- dropped by code checks: 10 (number: more than one number in value_as_written: 10)

### d5 [related_series] Population by age and sex, women of childbearing age

Hypothesis: Births in July 2026 are approximately the product of the number of women aged 20–39 in mid-2026 and an age-specific fertility rate. The role is to provide the denominator and check whether the population at risk changed materially; the transfer assumption is that fertility rates by age follow recent trends.

Queries issued by the searcher: South Korea population by age 2026 statistics women 20-39; KOSTAT 주민등록인구 연령별 2026 여성 인구; age specific fertility rate South Korea 2024 2025 per 1000 women 20-39; KOSTAT Monthly Population Trends live births July 2025 2026 인구동향 출생아수

- `https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=H000202&idx_cd=H0002&freq=Y&period=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EC%84%B1%EB%B9%84/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446625&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jumin.mois.go.kr/ageStatMonth.do` -> **snapshot** (snapshot 20260423104656); points raw/verified 15/14
  - p21 South Korea (전국) female population aged 20-29, March 2026 = **2,698,567** persons (2026-03-01..2026-03-31) [keep: ] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p22 South Korea (전국) female population aged 30-39, March 2026 = **3,184,332** persons (2026-03-01..2026-03-31) [keep: ] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p23 South Korea (전국) total population, March 2026 = **51,101,371** persons (2026-03-01..2026-03-31) [keep: Kept as the population total for context and cross-checking the MOIS table.] quote: "\| 전국 \| 51,101,371 \| 51,101,371 \| 2,920,250 \| 4,623,895 \| 5,609,816 \| 6,678,153 \| 7,534,672 \| 8,621,183 \| 7,962,748 \| 4,623,870 \| 2,139,068 \| 378,754 \| 8,962 \|"
  - p24 South Korea (전국) male population, March 2026 = **25,425,930** persons (2026-03-01..2026-03-31) [DISCARD: Male population total is not a denominator for births and is redundant with the female age bands for the fertility route] quote: "\| 7,534,672 \| 8,621,183 \| 7,962,748 \| 4,623,870 \| 2,139,068 \| 378,754 \| 8,962 \| 25,425,930 \| 25,425,930 \| 1,496,704 \| 2,372,897 \| 2,911,249 \| 3,493,821 \| 3,837,966 \| 4,346,162 \| 3,929,"
  - p25 South Korea (전국) female population aged 0-9, March 2026 = **1,423,546** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 0-9 is far below reproductive age and cannot enter an age-specific fertility decomposition.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p26 South Korea (전국) female population aged 10-19, March 2026 = **2,250,998** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 10-19 is largely below reproductive age and is not a usable fertility denominator for July 2026 b] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p27 South Korea (전국) female population aged 40-49, March 2026 = **3,696,706** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 40-49 contributes only a small share of births and is not needed once the 20-39 denominator is av] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p28 South Korea (전국) female population aged 50-59, March 2026 = **4,275,021** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 50-59 is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p29 South Korea (전국) female population aged 60-69, March 2026 = **4,032,868** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 60-69 is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p30 South Korea (전국) female population aged 70-79, March 2026 = **2,485,863** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 70-79 is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p31 South Korea (전국) female population aged 80-89, March 2026 = **1,333,754** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 80-89 is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p32 South Korea (전국) female population aged 90-99, March 2026 = **286,315** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 90-99 is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p33 South Korea (전국) female population aged 100 and over, March 2026 = **7,471** persons (2026-03-01..2026-03-31) [DISCARD: Female population aged 100+ is outside reproductive age and irrelevant.] quote: "25,675,441 \| 25,675,441 \| 1,423,546 \| 2,250,998 \| 2,698,567 \| 3,184,332 \| 3,696,706 \| 4,275,021 \| 4,032,868 \| 2,485,863 \| 1,333,754 \| 286,315 \| 7,471 \|"
  - p34 South Korea (전국) male population aged 20-29, March 2026 = **2,911,249** persons (2026-03-01..2026-03-31) [DISCARD: Male population aged 20-29 is not a fertility denominator and adds nothing to the target.] quote: "25,425,930 \| 25,425,930 \| 1,496,704 \| 2,372,897 \| 2,911,249 \| 3,493,821 \| 3,837,966 \| 4,346,162 \| 3,929,880 \| 2,138,007 \| 805,314 \| 92,439 \| 1,491 \|"
- dropped by code checks: 1 (quote longer than 400 chars: 1)

### d6 [forecasts_markets] Official projections and demographic forecasts

Hypothesis: Statistics Korea or other demographers may publish monthly or quarterly birth projections for 2026. These forecasts can serve as a prior for the July 2026 level, adjusted for any known deviations in recent months. The role is to provide an independent anchor; the transfer assumption is that the forecast methodology captures current trends.

Queries issued by the searcher: South Korea 2026 birth forecast KOSTAT births projection; 2026년 출생아 수 전망 통계청; 2025년 7월 출생아 수 인구동향 월별 출생아; 2026년 연간 출생아 수 전망 29만명 30만명 하반기

- `https://www.etoday.co.kr/news/view/2610060?trc=main_top_sub` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20250924067700002?input=1195m` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://koreabizwire.com/birth-rate-poised-to-return-to-0-9-after-seven-years?ckattempt=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] Policy and economic shocks affecting fertility

Hypothesis: Policies such as parental leave expansion, baby bonuses, or housing support introduced in 2024–2025 could have changed birth timing or number by July 2026. The role is to identify any measurable step-change in births; the transfer assumption is that the shock’s effect is quantifiable from pre/post comparisons.

Queries issued by the searcher: South Korea monthly births 2025 increase Statistics Korea population trends; South Korea pronatalist policy 2025 birth rate effect baby bonus parental leave; 7월 출생아 수 2025년 2만명 인구동향 통계청; 2026년 5월 출생아 수 인구동향 국가데이터처

- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8366129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hkcna.hk/hk/content/s6aa254bfe4b01e987f7c1964.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.seoul.co.kr/news/society/2026/08/27/20260827010006` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sacbee.com/news/nation-world/world/article313993900.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [attention] Online search and social media interest in pregnancy and childbirth

Hypothesis: Search volume for pregnancy-related terms or online birth announcements may correlate with birth counts with a lag. The role is to provide a high-frequency signal of birth trends; the transfer assumption is a stable relationship between attention and actual births, which is uncertain.

Queries issued by the searcher: 네이버 데이터랩 임신 출산 검색량 추이; Google Trends South Korea pregnancy childbirth search interest birth correlation; Statistics Korea monthly population trends live births 2026; South Korea monthly births 2026 KOSTAT population movement statistics

- `https://www.chosun.com/economy/economy_general/2026/09/23/4336WE6G4BBALOXOVOQM7RBNKE/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indonesian.korea.net/NewsFocus/Society/view?articleId=297012` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.sedaily.com/finance/2026/06/24/koreas-birth-rate-rises-to-093-but-population-shrinks-for` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://koreabizwire.com/gender-reveal-parties-maternity-photos-and-ai-baby-faces-how-koreas-millennials-and-gen-z-are-redefining-parenthood/330134` -> **snapshot** (snapshot 20260410161530); points raw/verified 0/0

### b1 [own_history] Monthly birth series continuity

Hypothesis: The July 2026 estimate is anchored on the July 2025 level (p7) plus the 2026 year-to-date monthly birth counts. If KOSTAT monthly Population Trends releases for January-June 2026 are available, they give the actual 2026 level and trend, replacing the assumption that the 2025 y/y growth rate persists. This is the single most valuable missing input because it converts a trend-extrapolation into a level-plus-recent-momentum estimate.

Queries issued by the searcher: KOSTAT Monthly Population Trends live births January 2026; Statistics Korea 인구동향 2026년 1월 출생아 수; 2026년 5월 인구동향 출생아 수 국가데이터처; 2026년 4월 인구동향 출생아 수 전년동월대비

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=297003&koreanId=296981` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=444188` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Marriage-to-birth bridge

Hypothesis: The 2024-2025 marriage surge (p1-p3, p11-p12) should raise first births in 2026. A quantified lag structure (share of first births occurring 12-24 months after marriage, and the marriage cohort sizes) would let the marriage signal adjust the birth trend rather than being used only qualitatively. This resolves whether the 2026 birth level should be above or below a simple extrapolation of the 2025 y/y rate.

Queries issued by the searcher: KOSTAT monthly marriage registrations 2024 2025 first birth interval after marriage distribution; South Korea first birth within 12-24 months after marriage share statistics; KOSTAT 인구동향 혼인건수 2025년 월별 2024년 결혼 증가 출생아수; South Korea marriages 2025 increase 20% births 2026 first birth lag statistics

- `https://mods.go.kr/boardDownload.es?bid=11815&list_no=365445&seq=15` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhdata.or.kr/mailing/Numbers325_260303_B1_Part.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `http://tv.edaily.co.kr/News/NewsRead?NewsId=04382086642337840&Kind=257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kihasa.re.kr/api/kihasa/file/download?seq=12297` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Official 2026 projection

Hypothesis: Statistics Korea's 2026 population projections or its 2026 birth forecast provide an independent anchor for the annual 2026 level, which can be combined with the July seasonal share. This would resolve the disagreement between a pure 2025-trend extrapolation and a marriage-driven rebound, and it is the most direct check on the central level.

Queries issued by the searcher: Statistics Korea 2026 birth projection 장래인구추계 2026년 출생아 수 전망; KOSTAT 2026 population projection annual births forecast 2026; 장래인구추계 2022-2072 출생아 수 2026년 중위 고위 시나리오 통계청; 2026년 7월 출생아 수 인구동향 발표

- `https://sri.kostat.go.kr/boardDownload.es?bid=207&list_no=428476&seq=6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/0
- `https://mods.go.kr/boardDownload.es?bid=0056&list_no=431838&seq=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://koreabizwire.com/birth-rate-poised-to-return-to-0-9-after-seven-years` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 2; number: unknown scale word '만': 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; number: more than one number in value_as_written: 3; period_end 2035-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] All three describe the same underlying administrative series (KOSTAT marriage registrations) and are consistent: a 2024 surge (+14.8%), continued growth in 2025 (+8.1%), and a strong December 2025 (+1
- corroborating: ['p4', 'p5', 'p6'] Same KOSTAT 2025 population-movement release: births 254,500 (+6.8% vs 2024) and TFR 0.80, the highest since 2021 (0.81). Internally consistent (rising births and a TFR rebound). Shared source, so tre
- corroborating: ['p7', 'p8'] Same July 2025 release: 21,803 births, +5.9% y/y. p8 is the change rate implied by p7 and its 2024 base; they are not independent, but p7 is the key level anchor for the July seasonal position.
- corroborating: ['p9', 'p10', 'p15'] Deaths 27,979 (-0.7%) and natural increase -6,175 are arithmetically consistent with p7 (21,803 - 27,979 = -6,176, rounding). Same release; useful only as a consistency check, not as a birth input.
- corroborating: ['p11', 'p12'] July 2025 marriages 20,394, +8.4% y/y. Same release as p7-p10 and consistent with the annual marriage growth in p1-p2. Provides the July-specific marriage level for a marriage-to-birth bridge.
- corroborating: ['p13', 'p14'] Divorces 7,826, -1.4%. Same release; no direct role in births, kept only as context.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20'] Long-run (1981-2023) monthly birth shares from one article: Jan 10.0%, Feb 9.6%, Mar 8.6%, Q1 28.2%, July 7.8%. Internally consistent (Jan+Feb+Mar = 28.2%). They describe a very different fertility re
- corroborating: ['p21', 'p22', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33'] Resident-registration female population by age, March 2026, from one MOIS table. The 20-29 (2,698,567) and 30-39 (3,184,332) groups are the reproductive-age denominator; the other age groups are conte
- corroborating: ['p23', 'p24', 'p34'] Same MOIS table: total population 51,101,371, males 25,425,930, males 20-29 2,911,249. Consistent with the female columns (total = male + female). Context only.
- conflicting: ['p7', 'p20'] Not a true contradiction but a scope/period mismatch: p20's 7.8% July share is a 1981-2023 average, while p7's 21,803 is the current-regime July 2025 level. Using the old share on a current annual tot
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] All three describe the same underlying administrative series (marriage registrations compiled by the national statistics agency) and are mutually consistent: a 2024 jump, continued 2025 growth, and a 
- corroborating: ['p4', 'p5', 'p6'] 2025 annual births up 6.8% and TFR back to 0.80 (highest since 2021's 0.81) come from the same 2025 population-movement release and are internally consistent; they establish that 2025 was a genuine tu
- corroborating: ['p7', 'p8'] July 2025 level (21,803) and its +5.9% y/y rate are the same release and arithmetically consistent; p7 is the direct anchor for the July seasonal level.
- corroborating: ['p4', 'p7', 'p8'] The annual 2025 increase (+6.8%) and the July 2025 monthly increase (+5.9%) are close, indicating July 2025 was near the 2025 trend rather than an outlier month.
- corroborating: ['p1', 'p2', 'p11', 'p12'] Annual 2024-2025 marriage growth and the July 2025 monthly marriage growth (+8.4%) point the same way; the marriage surge is broad-based, supporting a positive 2026 birth impulse via the 1-2 year lag.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20'] The monthly shares are internally consistent (Jan+Feb+Mar = 28.2% = Q1 share) and come from one long-run tabulation; they are a single seasonal source, not independent.
- corroborating: ['p21', 'p22', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33'] All female age bands come from one resident-registration snapshot and sum to the female total; they are one denominator source.
- corroborating: ['p23', 'p24', 'p21', 'p22'] Male plus female totals reconcile with the national total in the same March 2026 snapshot, confirming internal consistency of the population file.
- corroborating: ['p9', 'p10', 'p15'] Deaths and natural increase are from the same July 2025 release and reconcile arithmetically (21,803 - 27,979 = -6,175); they are context only, not inputs to a birth estimate.
- corroborating: ['p13', 'p14'] Divorce level and rate are the same release; they carry no direct information on births and are context only.
- conflicting: ['p20', 'p7'] The long-run July share (7.8% of annual births, 1981-2023) applied to a 2026 annual level would give a July figure that need not match a level-plus-momentum extrapolation from p7; the two routes can d
- corroborating: ['p1', 'p2', 'p4'] Marriage growth in 2024-2025 and the 2025 birth rebound are consistent with a lagged marriage-to-birth channel, but they are different series and the link is an assumption, not a measurement.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 live births relative to July 2025 | 1.03 | 0.95..1.12 | 0.7294..1.459 (widened) | ratio | m1 (m1) | July 2025 was 21,803 (p7), up 5.9% y/y (p8), and 2025 annual births rose 6.8% (p4). The 2024-2025 marriage surge (p1, p2, p3, p11, p12) should keep 2026 births at or above the 2025 level through the 1-2 year lag, but the pace of the rebound is likely to moderate and month-to-month noise is large. A  | The 2026 monthly birth trend continues the 2025 recovery at a moderating pace and no new shock (policy, epidemic, registration change) shifts July 2026 births. | Published January-June 2026 monthly births showing a y/y decline, or evidence that the 2024-2025 marriage surge did not translate into first births by mid-2026. |
| a2 | July share of 2026 annual live births | 0.078 | 0.07..0.086 | 0.05486..0.1097 (widened) | share | unused | The long-run July share of annual births is 7.8% (p20), from a 1981-2023 tabulation. The share is used to convert an annual 2026 level into a July figure; the range allows for drift in seasonality and for the fact that the 43-year average may not match the recent monthly pattern. | The seasonal distribution of births in 2026 is close to the historical average, so July's share of the annual total is near 7.8%. | Recent monthly releases showing July shares persistently above or below the historical 7.8% by more than the stated range. |
| a3 | 2026 annual live births relative to 2025 | 1.02 | 0.94..1.1 | 0.719..1.438 (widened) | ratio | unused | 2025 annual births were 254,500, up 6.8% (p4), and the marriage surge (p1, p2, p3) supports a further but smaller 2026 increase. A factor near 1.02 with a wide range is used to scale the 2025 annual level before applying the July share. | The 2026 annual birth total continues the 2025 recovery at a moderating pace, consistent with the lagged marriage signal. | A published 2026 annual or year-to-date birth total showing a decline versus 2025, or evidence that the marriage surge has already been fully absorbed. |
| a4 | July 2026 births per woman aged 20-39 | 0.00055 | 0.00045..0.00068 | 0.0003912..0.0007823 (widened) | births per woman per month | m3 (m3) | No kept point gives a monthly age-specific fertility rate for women 20-39. The value is a monthly rate consistent with a TFR near 0.8 (p5) concentrated in ages 20-39, spread over 12 months; the range is wide because the age distribution of births and the monthly rate are uncertain. | Fertility in July 2026 follows recent age-specific patterns and the 20-39 female population from the March 2026 snapshot is a valid mid-2026 denominator. | Published age-specific fertility rates for 2026 showing a monthly rate outside the stated range, or a large mid-2026 change in the 20-39 female population. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 22,494 | ['p7'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | n/a | ['p4'] / ['a2', 'a3'] | [] |  | 0.00 |  | formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of ratios cannot produce the target |
| m3 | formula_mc | 3,264 | ['p21', 'p22'] / ['a4'] | [] |  | 0.50 | equal |  |

Result: central **8,569**, 80% interval [2,487, 29,518], basis method_spread, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first reported by Statistics Korea's monthly Population Trends release, is 8,569 persons. The supplied interval is 2,487 to 29,518, at the 80% level, on a method spread basis; it is model-based and conditional on the assumptions, not a demonstrated accuracy guarantee.

Two methods were combined with weights: 22,494 (50%) anchors on July 2025 and a growth factor 1.03 (range 0.7294 to 1.459); 3,264 (50%) uses the female population aged [n]-[n] and a monthly fertility rate 0.00055 (range 0.0003912 to 0.0007823). Observed inputs are the [n] monthly and annual birth levels and population counts; the growth factor and fertility rate are analyst assumptions. The combination reflects method spread, not independent validation.

The main risk is that the [n] monthly trend diverges from the [n] rebound, or that the assumed fertility rate is wrong. The most useful missing evidence would be early [n] monthly birth counts.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 live births relative to July 2025: 1.03 ratio, range 0.7294 to 1.459 (range widened by code); used by m1. Overturned by: Published January-June 2026 monthly births showing a y/y decline, or evidence that the [n]-2025 marriage surge did not translate into first births by mid-2026.
- a4 July 2026 births per woman aged [n]-[n]: 0.00055 births per woman per month, range 0.0003912 to 0.0007823 (range widened by code); used by m3. Overturned by: Published age-specific fertility rates for 2026 showing a monthly rate outside the stated range, or a large mid-2026 change in the [n]-[n] female population.

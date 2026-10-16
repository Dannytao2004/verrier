# Evidence ledger: fc_kr_births_2026_08

- Question: Assume today is 2026-10-16. You know nothing published after this date. Estimate the number of live births in South Korea in August 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-10-16
- Pinned target: Number of live births in South Korea during August 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-08-01..2026-08-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends (인구동향)

## Directions and pages

### d1 [own_history] Statistics Korea monthly vital statistics time series

Hypothesis: August 2026 live births can be projected from the same month in prior years, adjusted for the recent trend and any known calendar effects. The target is a monthly flow with strong seasonality and a declining trend.

Queries issued by the searcher: Statistics Korea monthly live births 2025 2026 인구동향 출생아 수; KOSTAT population trends live births August 2025 monthly; 2026년 7월 인구동향 출생아 수; 2026년 6월 인구동향 출생아 수 2만3111명

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=439018&tag=&nPage=1&ref_bid=203,204,205,206,207,210,211,11109,11113,11814,213,21` -> **live_dated** (page date 2025-10-29); points raw/verified 9/9
  - p1 South Korea live births, August 2025 (monthly Population Trends) = **20,867** live births (persons) (2025-08-01..2025-08-31) [keep: ] quote: "출생아 수는 20,867명으로 전년동월대비 3.8% 증가"
  - p2 South Korea live births year-on-year change, August 2025 vs August 2024 = **3.8** % (2025-08-01..2025-08-31) [DISCARD: Redundant restatement of p1's YoY change; the level p1 is what the series route needs, and the percentage adds no indepe] quote: "출생아 수는 20,867명으로 전년동월대비 3.8% 증가"
  - p3 South Korea deaths, August 2025 = **28,971** deaths (persons) (2025-08-01..2025-08-31) [DISCARD: Deaths are not an input to the birth estimate; kept only as context and not used in any method.] quote: "사망자 수는 28,971명으로 전년동월대비 9.8% 감소"
  - p4 South Korea deaths year-on-year change, August 2025 vs August 2024 = **9.8** % (2025-08-01..2025-08-31) [DISCARD: Deaths change; not a birth input.] quote: "사망자 수는 28,971명으로 전년동월대비 9.8% 감소"
  - p5 South Korea marriages, August 2025 = **19,449** marriages (cases) (2025-08-01..2025-08-31) [DISCARD: August 2025 marriage level; the marriage route needs the 2026 marriage surge (p14/p15/p68/p32), not the 2025 level, and ] quote: "혼인 건수는 19,449건으로 전년동월대비 11.0% 증가"
  - p6 South Korea marriages year-on-year change, August 2025 vs August 2024 = **11** % (2025-08-01..2025-08-31) [DISCARD: August 2025 marriage YoY change — same reason as p5.] quote: "혼인 건수는 19,449건으로 전년동월대비 11.0% 증가"
  - p7 South Korea divorces, August 2025 = **7,196** divorces (cases) (2025-08-01..2025-08-31) [DISCARD: Divorces; not a birth input.] quote: "이혼 건수는 7,196건으로 전년동월대비 5.5% 감소"
  - p8 South Korea divorces year-on-year change, August 2025 vs August 2024 = **5.5** % (2025-08-01..2025-08-31) [DISCARD: Divorces change; not a birth input.] quote: "이혼 건수는 7,196건으로 전년동월대비 5.5% 감소"
  - p9 South Korea natural increase (live births minus deaths), August 2025 = **-8,105** persons (natural increase) (2025-08-01..2025-08-31) [DISCARD: Natural increase; not a birth input.] quote: "자연증가(출생아 수 - 사망자 수)는 -8,105명"
- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=447111` -> **live_dated** (page date 2026-09-23); points raw/verified 9/9
  - p10 South Korea live births, July 2026 (monthly Population Trends) = **24,275** live births (persons) (2026-07-01..2026-07-31) [keep: ] quote: "출생아 수는 24,275명으로 전년동월대비 11.1% 증가"
  - p11 South Korea live births, year-on-year change, July 2026 = **11.1** percent (2026-07-01..2026-07-31) [keep: ] quote: "출생아 수는 24,275명으로 전년동월대비 11.1% 증가"
  - p12 South Korea deaths, July 2026 = **28,921** deaths (persons) (2026-07-01..2026-07-31) [DISCARD: Deaths; not a birth input.] quote: "사망자 수는 28,921명으로 전년동월대비 3.0% 증가"
  - p13 South Korea deaths, year-on-year change, July 2026 = **3** percent (2026-07-01..2026-07-31) [DISCARD: Deaths change; not a birth input.] quote: "사망자 수는 28,921명으로 전년동월대비 3.0% 증가"
  - p14 South Korea marriages, July 2026 = **22,282** marriages (cases) (2026-07-01..2026-07-31) [keep: ] quote: "혼인 건수는 22,282건으로 전년동월대비 9.3% 증가"
  - p15 South Korea marriages, year-on-year change, July 2026 = **9.3** percent (2026-07-01..2026-07-31) [keep: ] quote: "혼인 건수는 22,282건으로 전년동월대비 9.3% 증가"
  - p16 South Korea divorces, July 2026 = **7,764** divorces (cases) (2026-07-01..2026-07-31) [DISCARD: Divorces; not a birth input.] quote: "이혼 건수는 7,764건으로 전년동월대비 0.8% 감소"
  - p17 South Korea divorces, year-on-year change, July 2026 = **0.8** percent (2026-07-01..2026-07-31) [DISCARD: Divorces change; not a birth input.] quote: "이혼 건수는 7,764건으로 전년동월대비 0.8% 감소"
  - p18 South Korea natural increase (live births minus deaths), July 2026 = **-4,647** persons (2026-07-01..2026-07-31) [DISCARD: Natural increase; not a birth input.] quote: "자연증가(출생아 수 - 사망자 수)는 -4,647명"
- `https://www.news1.kr/economy/trend/6300083` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://biz.sbs.co.kr/article/20000268394` -> **live_dated** (page date 2025-10-29); points raw/verified 0/0

### d2 [forecasts_markets] Official projections and nowcasts

Hypothesis: Statistics Korea or other institutions may publish monthly or quarterly birth projections or nowcasts that can serve as a direct estimate for August 2026.

Queries issued by the searcher: South Korea birth forecast 2026 monthly live births KOSTAT projection; 출생아 수 전망 2026 인구동향; 2026년 7월 인구동향 출생아 수 통계청; 2026년 8월 출생아 수 전망 2만명

- `https://www.gov.kr/portal/ntnadmNews/4866340?srchOrgCd=1241000&pageIndex=1&hideurl=N` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://namu.wiki/w/2024-2026%EB%85%84%20%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%B6%9C%EC%82%B0%EC%9C%A8%20%EB%B0%98%EB%93%B1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.etoday.co.kr/news/view/2610060?trc=main_top_sub` -> **live_dated** (page date 2026-08-02); points raw/verified 15/0
- `https://www.yna.co.kr/view/AKR20260923077000002?section=economy/all&site=topnews02` -> **live_dated** (page date 2026-09-23); points raw/verified 15/7
  - p19 South Korea year-on-year percentage increase in monthly live births, July = **11.1** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p11 (same July 2026 +11.1% from the same release).] quote: "지난 7월 출생아 수는 2만4천275명으로 작년 동월보다 2천421명(11.1%) 증가했다."
  - p20 South Korea year-on-year percentage increase in cumulative live births, January– = **14.7** % (2026-01-01..2026-07-31) [keep: ] quote: "1∼7월 누적 출생아는 작년 동기보다 14.7% 늘어나며 역대 가장 높은 증가율을 기록했다."
  - p21 South Korea total fertility rate, July = **0.89** children per woman (2026-07-01..2026-07-31) [DISCARD: July 2026 TFR; corroborating context, not a direct input to the August birth count.] quote: "7월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.89명으로 전년동월대비 0.08명 증가했다."
  - p22 South Korea year-on-year change in total fertility rate, July = **0.08** children per woman (2026-07-01..2026-07-31) [DISCARD: July 2026 TFR change; corroborating context.] quote: "7월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.89명으로 전년동월대비 0.08명 증가했다."
  - p23 South Korea age-specific fertility rate, mothers aged 30–34, July = **82.1** births per 1,000 women (2026-07-01..2026-07-31) [DISCARD: June 2026 ASFR 30–34; the July values p113/p158 are closer to the target and the June value is redundant.] quote: "엄마의 연령별로는 30∼34세에서 82.1명으로 작년 동월보다 7.9명 늘었고, 35∼39세는 61.1명으로 8.6명 증가했다."
  - p24 South Korea age-specific fertility rate, mothers aged 35–39, July = **61.1** births per 1,000 women (2026-07-01..2026-07-31) [DISCARD: June 2026 ASFR 35–39; redundant with p114/p158.] quote: "엄마의 연령별로는 30∼34세에서 82.1명으로 작년 동월보다 7.9명 늘었고, 35∼39세는 61.1명으로 8.6명 증가했다."
  - p25 South Korea age-specific fertility rate, mothers aged 25–29, July = **21** births per 1,000 women (2026-07-01..2026-07-31) [DISCARD: June 2026 ASFR 25–29; not needed.] quote: "25∼29세는 21.0명으로 0.4명 늘었다."
- dropped by code checks: 23 (period year 2025 does not appear in the page text or URL (likely mis-dated): 8; number: unknown scale word '만': 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 1; number: more than one number in value_as_written: 11; period_end 2035-12-31 after as_of: 1)

### d3 [administrative] Birth registration data from local governments

Hypothesis: Some local governments or the Ministry of the Interior and Safety may publish monthly birth registration counts earlier than KOSTAT. These can be used as a leading indicator for the national figure.

Queries issued by the searcher: 행정안전부 주민등록 출생아 수 2026; South Korea birth registration August 2026; 주민등록 출생자 수 2026년 8월 행정안전부; 행안부 주민등록 출생아 8월 2026 전년동월대비

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (live http 403); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=331026` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://kosis.kr/serviceInfo/newContrainDataDetail.do?boardIdx=2008001&boardOrgId=101` -> **live_dated** (page date 2014-10-26); points raw/verified 0/0

### d4 [related_series] Marriage and birth registration administrative data

Hypothesis: Live births are strongly linked to the number of marriages in prior periods, with a typical lag of 1–3 years. A change in marriages can signal a change in births, though the relationship is weakening.

Queries issued by the searcher: South Korea monthly marriage registrations 2025 2026 Statistics Korea; 혼인건수 월별 통계 2025 2026; Korea births per marriage ratio; Statistics Korea monthly live births August 2026 population trends

- `https://v.daum.net/v/20260422120605247` -> **live_dated** (page date 2026-04-22); points raw/verified 13/2
  - p26 Duration of consecutive monthly marriage registration increases in South Korea b = **22** months (2024-04-01..2026-01-31) [DISCARD: Marriage-streak context; the marriage levels p32/p33/p68/p157 carry the signal.] quote: "2024년 4월부터 올해 1월까지 22개월 연속 증가하며 역대 최장 상승 흐름을 이어왔다."
  - p27 Longest prior streak of consecutive monthly live birth increases in South Korea = **25** months (2006-02-01..2008-02-29) [DISCARD: Streak-length context; not a numerical input to the August level.] quote: "2006년 2월부터 2008년 2월까지 25개월 연속 증가 이후 약 18년 만에 가장 긴 흐름이다."
- `https://m.etoday.co.kr/news/view/2569148?trc=m_sub_list_news` -> **live_dated** (page date 2026-03-25); points raw/verified 15/14
  - p28 South Korea divorce case filings, January 2026 = **7,208** divorce case filings (2026-01-01..2026-01-31) [DISCARD: Divorce filings are not an input to births; the January 2026 divorce block is context only.] quote: "1월 한 달간 신고된 이혼 건수는 총 7208건으로 집계됐다."
  - p29 South Korea divorce case filings, January 2025 (year-earlier comparison) = **6,918** divorce case filings (2025-01-01..2025-01-31) [DISCARD: Divorce filings, not a birth input.] quote: "이는 지난해 같은 기간(6918건)보다 290건, 약 4.2% 증가한 수치다."
  - p30 Year-on-year increase in South Korea divorce case filings, January 2026 vs Janua = **290** divorce case filings (2026-01-01..2026-01-31) [DISCARD: Divorce filings, not a birth input.] quote: "이는 지난해 같은 기간(6918건)보다 290건, 약 4.2% 증가한 수치다."
  - p31 Year-on-year percentage increase in South Korea divorce case filings, January 20 = **4.2** % (2026-01-01..2026-01-31) [DISCARD: Divorce filings, not a birth input.] quote: "이는 지난해 같은 기간(6918건)보다 290건, 약 4.2% 증가한 수치다."
  - p32 Year-on-year percentage increase in South Korea marriage registrations, January  = **12.4** % (2026-01-01..2026-01-31) [keep: ] quote: "1월 혼인 건수는 2만2640건을 기록하며 전년 동월 대비 12.4%(2489건)라는 큰 폭의 증가율을 보였다."
  - p33 Year-on-year increase in South Korea marriage registrations, January 2026 vs Jan = **2,489** marriage registrations (2026-01-01..2026-01-31) [keep: ] quote: "1월 혼인 건수는 2만2640건을 기록하며 전년 동월 대비 12.4%(2489건)라는 큰 폭의 증가율을 보였다."
  - p34 South Korea crude divorce rate (divorces per 1,000 population), January 2026 = **1.7** divorces per 1,000 population (2026-01-01..2026-01-31) [DISCARD: Crude divorce rate, not a birth input.] quote: "인구 1000명당 이혼 건수를 나타내는 조이혼율은 1.7건으로, 전년 동월(1.6건) 대비 0.1건 상승했다."
  - p35 South Korea crude divorce rate (divorces per 1,000 population), January 2025 = **1.6** divorces per 1,000 population (2025-01-01..2025-01-31) [DISCARD: Crude divorce rate, not a birth input.] quote: "인구 1000명당 이혼 건수를 나타내는 조이혼율은 1.7건으로, 전년 동월(1.6건) 대비 0.1건 상승했다."
  - p36 Change in South Korea crude divorce rate, January 2026 vs January 2025 = **0.1** divorces per 1,000 population (2026-01-01..2026-01-31) [DISCARD: Crude divorce rate change, not a birth input.] quote: "인구 1000명당 이혼 건수를 나타내는 조이혼율은 1.7건으로, 전년 동월(1.6건) 대비 0.1건 상승했다."
  - p37 South Korea crude marriage rate (marriages per 1,000 population), January 2026 = **5.2** marriages per 1,000 population (2026-01-01..2026-01-31) [DISCARD: Crude marriage rate for January 2026; the marriage level is already available from p32/p33 and this rate is not needed.] quote: "1월의 조혼인율이 5.2건인 것과 비교하면 혼인 신고 3건당 약 1건 꼴로 이혼 신고가 이뤄지고 있는 셈이다."
  - p38 Ratio of divorce filings to marriage registrations, South Korea, January 2026 (a = **3** marriage registrations per divorce filing (2026-01-01..2026-01-31) [DISCARD: Divorce-to-marriage ratio; not a birth input.] quote: "1월의 조혼인율이 5.2건인 것과 비교하면 혼인 신고 3건당 약 1건 꼴로 이혼 신고가 이뤄지고 있는 셈이다."
  - p39 Number of South Korea provinces/metropolitan cities with year-on-year increase i = **9** provinces/metropolitan cities (2026-01-01..2026-01-31) [DISCARD: Provincial divorce counts; not a birth input.] quote: "전국 17개 시도 가운데 서울, 부산, 대구 등 9개 시도에서는 전년 동월 대비 이혼 건수가 증가한 반면, 인천, 광주 등 8개 시도에서는 감소세를 보였다."
  - p40 Number of South Korea provinces/metropolitan cities with year-on-year decrease i = **8** provinces/metropolitan cities (2026-01-01..2026-01-31) [DISCARD: Provincial divorce counts; not a birth input.] quote: "전국 17개 시도 가운데 서울, 부산, 대구 등 9개 시도에서는 전년 동월 대비 이혼 건수가 증가한 반면, 인천, 광주 등 8개 시도에서는 감소세를 보였다."
  - p41 Total number of South Korea provinces/metropolitan cities covered, January 2026 = **17** provinces/metropolitan cities (2026-01-01..2026-01-31) [DISCARD: Province count; not a birth input.] quote: "전국 17개 시도 가운데 서울, 부산, 대구 등 9개 시도에서는 전년 동월 대비 이혼 건수가 증가한 반면, 인천, 광주 등 8개 시도에서는 감소세를 보였다."
- `https://stock.mk.co.kr/news/view/1069388` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.khan.co.kr/en/article/202607291529057` -> **live_dated** (page date 2026-07-29); points raw/verified 15/2
  - p42 South Korea monthly births, May 2019 = **25,299** live births (2019-05-01..2019-05-31) [DISCARD: May 2019 level used only as a 'highest since' reference; not an August input and not needed for the target month.] quote: "As of May, the number of births was the highest in seven years since 2019 (25,299)."
  - p43 South Korea cumulative births, January through May 2019 = **134,433** live births (2019-01-01..2019-05-31) [DISCARD: Jan–May 2019 cumulative; same reason as p42.] quote: "The cumulative number of births was the highest since 2019 (134,433), and both the absolute increase and the growth rate were the largest on record."
- dropped by code checks: 25 (number: more than one number in value_as_written: 4; period_end missing or unparseable: 21)

### d5 [related_series] Population and women of childbearing age

Hypothesis: Births equal the number of women of childbearing age multiplied by the general fertility rate. Changes in the size and age structure of this population, combined with fertility intentions, drive the level of births.

Queries issued by the searcher: South Korea women aged 15-49 population 2025 statistics; 가임여성 인구 2025 통계; Statistics Korea monthly birth statistics 2026 live births August; 통계청 인구동향 2026년 8월 출생아 수

- `https://namu.wiki/w/대한민국/출산율/상세%20통계` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://biz.heraldcorp.com/article/10852661` -> **live_dated** (page date 2026-08-26); points raw/verified 15/11
  - p44 South Korea year-on-year increase in monthly live births, June 2026 = **3,115** live births (persons) (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 출생아 수는 2만3111명으로 지난해 같은 달보다 3115명(15.6%) 증가했다."
  - p45 South Korea year-on-year percentage increase in monthly live births, June 2026 = **15.6** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p64 (June 2026 +15.6%).] quote: "지난 6월 출생아 수는 2만3111명으로 지난해 같은 달보다 3115명(15.6%) 증가했다."
  - p46 South Korea total fertility rate, June 2026 = **0.88** children per woman (2026-06-01..2026-06-30) [DISCARD: June 2026 TFR; corroborating context.] quote: "6월 합계출산율은 0.88명으로 1년 전보다 0.11명 상승했다."
  - p47 South Korea year-on-year change in total fertility rate, June 2026 = **0.11** children per woman (2026-06-01..2026-06-30) [DISCARD: June 2026 TFR change; corroborating context.] quote: "6월 합계출산율은 0.88명으로 1년 전보다 0.11명 상승했다."
  - p48 South Korea age-specific fertility rate, women aged 30-34, June 2026 = **81.6** live births per 1,000 women aged 30-34 (2026-06-01..2026-06-30) [DISCARD: June 2026 ASFR 30–34; duplicate of p23.] quote: "30~34세 여성 인구 1000명당 출생아 수는 81.6명으로 전년 동월보다 12.4명 증가했다."
  - p49 South Korea year-on-year increase in age-specific fertility rate, women aged 30- = **12.4** live births per 1,000 women aged 30-34 (2026-06-01..2026-06-30) [DISCARD: June 2026 ASFR change; duplicate of p23.] quote: "30~34세 여성 인구 1000명당 출생아 수는 81.6명으로 전년 동월보다 12.4명 증가했다."
  - p50 South Korea age-specific fertility rate, women aged 35-39, June 2026 = **59.1** live births per 1,000 women aged 35-39 (2026-06-01..2026-06-30) [DISCARD: June 2026 ASFR 35–39; duplicate of p24.] quote: "35~39세 출산율도 50.0명에서 59.1명으로 9.1명 늘었다."
  - p51 South Korea year-on-year increase in age-specific fertility rate, women aged 35- = **9.1** live births per 1,000 women aged 35-39 (2026-06-01..2026-06-30) [DISCARD: June 2026 ASFR change; duplicate of p24.] quote: "35~39세 출산율도 50.0명에서 59.1명으로 9.1명 늘었다."
  - p52 South Korea year-on-year increase in quarterly live births, Q2 2026 = **9,675** live births (persons) (2026-04-01..2026-06-30) [keep: ] quote: "2분기 출생아 수도 7만791명으로 전년 동기보다 9675명(15.8%) 늘었다."
  - p53 South Korea share of first births among all live births, June 2026 = **63.8** % (2026-06-01..2026-06-30) [DISCARD: June 2026 first-birth share; the July value p115 is closer to the target month and the June value is not needed separate] quote: "전체 출생아 가운데 첫째아가 차지하는 비중은 63.8%로 1년 전보다 2.3%포인트 상승했다."
  - p54 South Korea quarterly total fertility rate, Sejong, Q2 2026 = **1.22** children per woman (2026-04-01..2026-06-30) [DISCARD: Sejong Q2 2026 TFR; regional detail not needed for the national August estimate.] quote: "2분기 합계출산율은 세종이 1.22명으로 가장 높았고 전남 1.20명, 울산 1.05명, 충북 1.03명, 충남 1.02명 순이었다."
- `https://www.cwoneconomy.com/news/articleView.html?idxno=13970` -> **live_dated** (page date 2026-06-15); points raw/verified 15/9
  - p55 South Korea year-on-year growth in live births, 2024 vs 2023 = **3.6** % (2024-01-01..2024-12-31) [DISCARD: 2024 annual births; the 2025 annual level p56 is the more recent base for the seasonal route.] quote: "2024년 23만8317명으로 전년보다 3.6% 증가했다."
  - p56 South Korea year-on-year growth in live births, 2025 vs 2024 = **6.8** % (2025-01-01..2025-12-31) [DISCARD: 2025 annual births 254,457 is used only as the base for the seasonal route; it is retained in the method inputs, not dis] quote: "2025년에는 25만4457명으로 다시 6.8% 늘었다."
  - p57 South Korea total fertility rate, 2023 = **0.72** children per woman (total fertility rate) (2023-01-01..2023-12-31) [DISCARD: 2023 TFR; historical context only.] quote: "합계출산율도 2023년 0.72명에서 2024년 0.75명, 2025년 0.80명으로 상승했다."
  - p58 South Korea total fertility rate, 2024 = **0.75** children per woman (total fertility rate) (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; historical context only.] quote: "합계출산율도 2023년 0.72명에서 2024년 0.75명, 2025년 0.80명으로 상승했다."
  - p59 South Korea total fertility rate, 2025 = **0.8** children per woman (total fertility rate) (2025-01-01..2025-12-31) [DISCARD: 2025 TFR; historical context only.] quote: "합계출산율도 2023년 0.72명에서 2024년 0.75명, 2025년 0.80명으로 상승했다."
  - p60 South Korea year-on-year growth in live births, January 2026 vs January 2025 = **11.7** % (2026-01-01..2026-01-31) [DISCARD: January 2026 growth; the cumulative and recent-month figures carry the trend.] quote: "2026년 들어서도 1월 출생아 수는 전년 동월보다 11.7%, 2월에는 13.6% 증가했다."
  - p61 South Korea year-on-year growth in live births, February 2026 vs February 2025 = **13.6** % (2026-02-01..2026-02-28) [DISCARD: February 2026 growth; the cumulative and recent-month figures carry the trend.] quote: "2026년 들어서도 1월 출생아 수는 전년 동월보다 11.7%, 2월에는 13.6% 증가했다."
  - p62 South Korea year-on-year growth in births to women aged 30-34, 2024 = **7.7** % (2024-01-01..2024-12-31) [DISCARD: 2024 growth in births to women 30–34; historical context only.] quote: "이 연령대 출생아 수도 2024년 7.7%, 2025년 6.1% 늘었다."
  - p63 South Korea year-on-year growth in births to women aged 30-34, 2025 = **6.1** % (2025-01-01..2025-12-31) [DISCARD: 2025 growth in births to women 30–34; historical context only.] quote: "이 연령대 출생아 수도 2024년 7.7%, 2025년 6.1% 늘었다."
- `https://m.sedaily.com/article/20083425` -> **live_dated** (page date 2026-08-26); points raw/verified 15/9
  - p64 South Korea year-on-year growth rate of live births, June 2026 = **15.6** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p45; one June 2026 growth figure suffices.] quote: "6월 출생아 수가 1년 전보다 15.6% 늘며 같은 달 기준 역대 최대 증가율을 기록했다."
  - p65 South Korea total fertility rate, June 2026 (monthly) = **0.88** children per woman (total fertility rate) (2026-06-01..2026-06-30) [DISCARD: Duplicate of p46 (June 2026 TFR 0.88).] quote: "합계출산율은 0.88명으로 전년 동월보다 0.11명 늘었다."
  - p66 South Korea year-on-year change in total fertility rate, June 2026 vs June 2025 = **0.11** children per woman (change in total fertility rate) (2026-06-01..2026-06-30) [DISCARD: Duplicate of p47.] quote: "합계출산율은 0.88명으로 전년 동월보다 0.11명 늘었다."
  - p67 South Korea year-on-year growth rate of cumulative live births, H1 2026 vs H1 20 = **15.4** % (2026-01-01..2026-06-30) [keep: ] quote: "올 상반기 누적 출생아는 14만 5804명으로 전년 동기 대비 1만 9430명(15.4%) 늘어 역시 2019년 이후 7년만에 최대치다."
  - p68 South Korea year-on-year growth rate of marriages, June 2026 = **14** % (2026-06-01..2026-06-30) [keep: ] quote: "6월 혼인 건수는 2만 1075건으로 전년 동월보다 14.0% 늘어 2017년 이후 가장 많았다."
  - p69 South Korea share of first births among the increase in births last year = **80** % (2025-01-01..2025-12-31) [DISCARD: 2025 first-birth share of the increase; qualitative support only, not a numerical input.] quote: "지난해 늘어난 출생아의 약 80%는 첫째아였고 이 가운데 53.6%가 결혼 후 2년 안에 태어났다."
  - p70 South Korea share of first births born within 2 years of marriage = **53.6** % (2025-01-01..2025-12-31) [DISCARD: Share of first births within 2 years of marriage; qualitative support only.] quote: "지난해 늘어난 출생아의 약 80%는 첫째아였고 이 가운데 53.6%가 결혼 후 2년 안에 태어났다."
  - p71 South Korea age-specific fertility rate, women aged 30–34, Q2 2026 (per 1,000 wo = **82.1** births per 1,000 women aged 30–34 (2026-04-01..2026-06-30) [DISCARD: Q2 2026 ASFR 30–34; redundant with the July monthly values.] quote: "올해 2분기 30대 초반 출산율은 여성 1000명당 82.1명으로 전년 동기보다 11.0명 상승했다."
  - p72 South Korea year-on-year change in age-specific fertility rate, women aged 30–34 = **11** births per 1,000 women aged 30–34 (change) (2026-04-01..2026-06-30) [DISCARD: Q2 2026 ASFR change; redundant.] quote: "올해 2분기 30대 초반 출산율은 여성 1000명당 82.1명으로 전년 동기보다 11.0명 상승했다."
- dropped by code checks: 16 (number: more than one number in value_as_written: 11; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; number: unknown scale word '만': 4)

### d6 [base_rates] Seasonal adjustment factors

Hypothesis: August births have a consistent seasonal pattern relative to the annual total or to adjacent months. A seasonal index can be applied to a known annual or year-to-date total to estimate August.

Queries issued by the searcher: South Korea monthly births August seasonal pattern Statistics Korea; 출생아 수 월별 계절성 8월 연간 출생아 비중; 2023년 출생아 수 월별 비중 1월 8월 통계청 출생통계; 2025년 출생아 수 월별 8월 비중 출생통계

- `https://www.korea.kr/common/download.do?fileId=198368729` -> **dropped** (unsupported content type application/x-download); points raw/verified -/-
- `https://www.heraldk.com/article/2025030214464224997` -> **live_dated** (page date 2025-03-02); points raw/verified 15/12
  - p73 South Korea August share of annual births, 2024 = **8.4** percent of annual live births (2024-08-01..2024-08-31) [keep: ] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p74 South Korea January share of annual births, 2024 = **9** percent of annual live births (2024-01-01..2024-01-31) [DISCARD: January 2024 share; not the target month.] quote: "지난해 월별 출생아 수가 가장 많은 달은 1월과 10월로 각각 2만1461명, 2만1404명이 태어났다. 비중은 9.0%로 똑같았다."
  - p75 South Korea October share of annual births, 2024 = **9** percent of annual live births (2024-10-01..2024-10-31) [DISCARD: October 2024 share; not the target month.] quote: "지난해 월별 출생아 수가 가장 많은 달은 1월과 10월로 각각 2만1461명, 2만1404명이 태어났다. 비중은 9.0%로 똑같았다."
  - p76 South Korea July share of annual births, 2024 = **8.6** percent of annual live births (2024-07-01..2024-07-31) [DISCARD: July 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p77 South Korea September share of annual births, 2024 = **8.6** percent of annual live births (2024-09-01..2024-09-30) [DISCARD: September 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p78 South Korea November share of annual births, 2024 = **8.4** percent of annual live births (2024-11-01..2024-11-30) [DISCARD: November 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p79 South Korea March share of annual births, 2024 = **8.3** percent of annual live births (2024-03-01..2024-03-31) [DISCARD: March 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p80 South Korea May share of annual births, 2024 = **8.2** percent of annual live births (2024-05-01..2024-05-31) [DISCARD: May 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p81 South Korea February share of annual births, 2024 = **8.1** percent of annual live births (2024-02-01..2024-02-29) [DISCARD: February 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p82 South Korea April share of annual births, 2024 = **8** percent of annual live births (2024-04-01..2024-04-30) [DISCARD: April 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p83 South Korea June share of annual births, 2024 = **7.7** percent of annual live births (2024-06-01..2024-06-30) [DISCARD: June 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
  - p84 South Korea December share of annual births, 2024 = **7.6** percent of annual live births (2024-12-01..2024-12-31) [DISCARD: December 2024 share; not the target month.] quote: "이어 7월·9월(8.6%), 8월·11월(8.4%), 3월(8.3%), 5월(8.2%), 2월(8.1%), 4월(8.0%), 6월(7.7%), 12월(7.6%) 순이었다."
- `https://m.seoul.co.kr/news/economy/2025/01/27/20250127500008` -> **live_dated** (page date 2025-01-27); points raw/verified 15/10
  - p85 August share of total live births in South Korea, 1981-2023 cumulative = **8** percent (1981-01-01..2023-12-31) [keep: ] quote: "그다음은 한여름인 8월 186만 6496명(8.0%), 가정의 달인 5월 185만 6101명(7.9%) 순으로 집계됐다."
  - p86 January share of total live births in South Korea, 1981-2023 cumulative = **10** percent (1981-01-01..2023-12-31) [DISCARD: January cumulative share; not the target month.] quote: "43년간 총 출생아 수 2332만 7013명 가운데 10.0%의 비중을 차지했다."
  - p87 February share of total live births in South Korea, 1981-2023 cumulative = **9.6** percent (1981-01-01..2023-12-31) [DISCARD: February cumulative share; not the target month.] quote: "그다음은 2월로 224만 44명(9.6%)이 태어났다."
  - p88 March share of total live births in South Korea, 1981-2023 cumulative = **8.6** percent (1981-01-01..2023-12-31) [DISCARD: March cumulative share; not the target month.] quote: "세 번째는 3월로 200만 1716명(8.6%)이 출생했다."
  - p89 First quarter share of total live births in South Korea, 1981-2023 cumulative = **28.2** percent (1981-01-01..2023-12-31) [DISCARD: Q1 cumulative share; not the target month.] quote: "전체 비중은 28.2%, 국민 10명 중 3명이 1분기에 태어난 셈이다."
  - p90 October share of total live births in South Korea, 1981-2023 cumulative = **8.4** percent (1981-01-01..2023-12-31) [DISCARD: October cumulative share; not the target month.] quote: "10월이 196만 1332명(8.4%)으로 네 번째, 9월이 192만 1065명(8.2%)으로 다섯번째였다."
  - p91 September share of total live births in South Korea, 1981-2023 cumulative = **8.2** percent (1981-01-01..2023-12-31) [DISCARD: September cumulative share; not the target month.] quote: "10월이 196만 1332명(8.4%)으로 네 번째, 9월이 192만 1065명(8.2%)으로 다섯번째였다."
  - p92 April share of total live births in South Korea, 1981-2023 cumulative = **8.1** percent (1981-01-01..2023-12-31) [DISCARD: April cumulative share; not the target month.] quote: "출생아 수가 여섯번째로 많은 달은 4월로 188만 795명(8.1%)이 태어났다."
  - p93 November share of total live births in South Korea, 1981-2023 cumulative = **8** percent (1981-01-01..2023-12-31) [DISCARD: November cumulative share; not the target month.] quote: "일곱번째는 한겨울로 진입하기 직전인 11월(187만 1314명)로, 비중은 8.0%였다."
  - p94 May share of total live births in South Korea, 1981-2023 cumulative = **7.9** percent (1981-01-01..2023-12-31) [DISCARD: May cumulative share; not the target month.] quote: "그다음은 한여름인 8월 186만 6496명(8.0%), 가정의 달인 5월 185만 6101명(7.9%) 순으로 집계됐다."
- `https://m2.edaily.co.kr/News/Read?newsId=04877366645519440&mediaCodeNo=0` -> **live_dated** (page date 2026-07-29); points raw/verified 13/12
  - p95 South Korea May live births year-on-year growth rate = **13.6** % (..) [DISCARD: May 2026 growth; the cumulative and recent-month figures carry the trend.] quote: "지난 5월 태어난 아기는 2만 3160명으로 전년 동기 대비 13.6% 증가했다."
  - p96 South Korea March live births year-on-year growth rate = **19.4** % (..) [DISCARD: March 2026 growth; the cumulative and recent-month figures carry the trend.] quote: "3월(19.4%)과 4월(18.0%)의 가파른 상승세와 비교하면 반등세가 소폭 누그러진 수치다."
  - p97 South Korea April live births year-on-year growth rate = **18** % (..) [DISCARD: April 2026 growth; the cumulative and recent-month figures carry the trend.] quote: "3월(19.4%)과 4월(18.0%)의 가파른 상승세와 비교하면 반등세가 소폭 누그러진 수치다."
  - p98 South Korea February daily average live births deviation from annual average (se = **19.6** % (..) [DISCARD: February seasonal index; the August share points p73/p85 are the relevant coefficients.] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p99 South Korea June daily average live births deviation from annual average (season = **-8.4** % (..) [DISCARD: June seasonal index; not the target month.] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p100 South Korea December daily average live births deviation from annual average (se = **-8.9** % (..) [DISCARD: December seasonal index; not the target month.] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p101 South Korea gap between highest and lowest birth months (daily average basis) = **28.5** % (..) [DISCARD: Max-min gap; context only.] quote: "가장 많은 달과 적은 달의 격차는 28.5%에 달한다."
  - p102 South Korea May daily average live births = **747** live births per day (persons) (..) [DISCARD: May 2026 daily average; not the target month.] quote: "올해 5월 하루 평균 출생아(747명) 역시 1월(868명)이나 4월(817명)에 비하면 크게 적다."
  - p103 South Korea January daily average live births = **868** live births per day (persons) (..) [DISCARD: January 2026 daily average; not the target month.] quote: "올해 5월 하루 평균 출생아(747명) 역시 1월(868명)이나 4월(817명)에 비하면 크게 적다."
  - p104 South Korea April daily average live births = **817** live births per day (persons) (..) [DISCARD: April 2026 daily average; not the target month.] quote: "올해 5월 하루 평균 출생아(747명) 역시 1월(868명)이나 4월(817명)에 비하면 크게 적다."
  - p105 South Korea historical maximum-minimum birth month gap (past) = **41.6** % (..) [DISCARD: Historical max-min gap; context only.] quote: "연중 최대·최소 출생아 격차는 과거 41.6%에서 최근 26.3%로 점차 줄어드는 추세다."
  - p106 South Korea recent maximum-minimum birth month gap = **26.3** % (..) [DISCARD: Recent max-min gap; context only.] quote: "연중 최대·최소 출생아 격차는 과거 41.6%에서 최근 26.3%로 점차 줄어드는 추세다."
- dropped by code checks: 9 (number: more than one number in value_as_written: 9)

### d7 [shocks] Policy and economic shocks affecting births

Hypothesis: Government pronatalist policies, housing costs, and economic conditions can shift birth timing and numbers. Any major policy introduced in 2025–2026 could affect August 2026 births.

Queries issued by the searcher: South Korea birth policy 2025 2026 pronatalist incentives; 저출산 대책 2025 2026 출산 장려금 신설; Statistics Korea monthly births 2026 live births increase percent 인구동향 2026년 8월 출생아; 통계청 인구동향 2026년 출생아 수 6월 7월 증가

- `https://busan.fnnews.com/news/202609231201183232` -> **live_dated** (page date 2026-09-23); points raw/verified 15/1
  - p107 South Korea total fertility rate, July 2026 = **0.89** children per woman (total fertility rate) (2026-07-01..2026-07-31) [DISCARD: Duplicate of p21/p111/p153 (July 2026 TFR 0.89).] quote: "7월 합계출산율은 0.89명으로 지난해 같은 달 0.81명보다 0.08명 증가했다."
- `https://h21.hani.co.kr/arti/society/society_general/60030.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://biz.heraldcorp.com/article/10883019` -> **live_dated** (page date 2026-09-23); points raw/verified 15/8
  - p108 Year-on-year increase in live births, South Korea, July 2026 = **2,421** live births (persons) (2026-07-01..2026-07-31) [DISCARD: Duplicate of the July 2026 YoY increase already captured by p10/p11.] quote: "7월 출생아 수는 지난해 같은 달보다 2421명(11.1%) 증가한 2만4275명이다."
  - p109 Year-on-year percentage increase in live births, South Korea, July 2026 = **11.1** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p11.] quote: "7월 출생아 수는 지난해 같은 달보다 2421명(11.1%) 증가한 2만4275명이다."
  - p110 Year-on-year percentage increase in cumulative live births, South Korea, January = **14.7** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p20/p154 (Jan–Jul cumulative +14.7%).] quote: "올해 1~7월 누적 출생아 수는 17만79명으로 지난해 같은 기간보다 2만1851명(14.7%) 증가했다."
  - p111 Total fertility rate, South Korea, July 2026 = **0.89** children per woman (2026-07-01..2026-07-31) [DISCARD: Duplicate of p21.] quote: "7월 합계출산율은 0.89명으로 전년 동월보다 0.08명 높아졌다."
  - p112 Year-on-year change in total fertility rate, South Korea, July 2026 = **0.08** children per woman (2026-07-01..2026-07-31) [DISCARD: Duplicate of p22.] quote: "7월 합계출산율은 0.89명으로 전년 동월보다 0.08명 높아졌다."
  - p113 Live births per 1,000 women aged 30–34, South Korea, July 2026 = **82.1** live births per 1,000 women aged 30–34 (2026-07-01..2026-07-31) [DISCARD: July 2026 ASFR 30–34; duplicate of p23/p158 family and not needed as a separate input.] quote: "30~34세 여성 인구 1000명당 출생아 수는 82.1명으로 1년 전보다 7.9명 늘었고"
  - p114 Live births per 1,000 women aged 35–39, South Korea, July 2026 = **61.1** live births per 1,000 women aged 35–39 (2026-07-01..2026-07-31) [DISCARD: July 2026 ASFR 35–39; duplicate of p158.] quote: "35~39세는 61.1명으로 8.6명 증가했다."
  - p115 Share of first births among live births, South Korea, July 2026 = **63.4** % (2026-07-01..2026-07-31) [DISCARD: July 2026 first-birth share — composition detail, not a level driver.] quote: "출생아 중 첫째아 비중은 63.4%로 1.7%포인트 높아졌다."
- `https://www.cbc.ca/news/world/south-korea-birthrate-turnaround-9.7238102` -> **live_dated** (page date 2026-06-17); points raw/verified 15/2
  - p116 South Korea total fertility rate in 2023 (children per woman) = **0.72** children per woman (2023-01-01..2023-12-31) [DISCARD: Duplicate of p57/p169 (TFR 2023 = 0.72).] quote: "In 2023, South Korea's birthrate was 0.72 per woman."
  - p117 South Korea total fertility rate as of January 2026 (children per woman) = **0.99** children per woman (2026-01-01..2026-01-31) [DISCARD: January 2026 TFR 0.99; already covered by p163 (Q1 0.95) and not needed separately.] quote: "As of January 2026, it's 0.99."
- dropped by code checks: 34 (number: more than one number in value_as_written: 20; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 12; value_as_written not in quote as a whole number: 1)

### d8 [related_series] Neighboring countries with similar demographic trends

Hypothesis: Countries like Japan or Taiwan may have already reported August 2026 births, and their year-on-year changes could provide a rough signal for South Korea, given shared regional trends.

Queries issued by the searcher: Japan monthly births August 2026 人口動態統計; Taiwan monthly births August 2026 內政部 出生數; 人口動態統計速報 令和8年8月分 出生数; 韓国 2026年8月 出生数 人口動向

- `https://gb.crntt.com/crn-webapp/doc/docDetailCreate.jsp?coluid=7&kindid=0&docid=160266835` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202607.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://portal.ijamp.jiji.com/portal/news/detail/2026082800725` -> **live_dated** (page date 2026-08-28); points raw/verified 8/2
  - p118 Japan live births, first half of 2026, year-on-year change (percent) = **0.8** % (2026-01-01..2026-06-30) [DISCARD: Japan H1 2026 +0.8% is a regional analogue but too weak and too different in level to enter a numerical method; retained] quote: "今年上半期(1~6月)の出生数は、前年同期比0.8%増の34万2068人だったことが28日、厚生労働省の人口動態統計(速報)で分かった。"
  - p119 Japan live births, first half of 2026, increase versus first half of 2025 = **2,788** live births (persons) (2026-01-01..2026-06-30) [DISCARD: Same Japan H1 2026 measurement as p118, expressed as a level difference.] quote: "今年上半期の出生数は、昨年同期の33万9280人から2788人増加。"
- `https://research.nicoxz.com/articles/japan-births-post-covid-bottoming` -> **live_dated** (page date 2026-08-28); points raw/verified 15/7
  - p120 Japan live births, January–June cumulative, 2026, year-on-year change = **0.8** percent (2026-01-01..2026-06-30) [DISCARD: Duplicate of p118 (Japan H1 2026 +0.8%).] quote: "1〜6月の出生数が34万2068人となり、前年同期を2788人、率にして0.8%上回りました。"
  - p121 Japan live births, January–May cumulative, 2026, year-on-year change = **0.4** percent (2026-01-01..2026-05-31) [DISCARD: Japan Jan–May 2026 +0.4%; same analogue, not a numerical input.] quote: "5月分速報での1〜5月累計(28万2222人、前年同期比+0.4%)でも11年ぶりの前年超えが確認されていました"
  - p122 Japan live births, May 2026 single month, year-on-year change = **1.7** percent (2026-05-01..2026-05-31) [DISCARD: Japan May 2026 −1.7%; same analogue, not a numerical input.] quote: "5月単月の出生数は5万9663人で、前年同月比1.7%減でした。"
  - p123 Japan live births, trailing 12-month cumulative as of May 2026, year-on-year cha = **0.4** percent (2025-06-01..2026-05-31) [DISCARD: Japan trailing-12-month −0.4%; same analogue, not a numerical input.] quote: "直近12カ月の累計でも70万7052人と、前年同期間を0.4%下回っています(2026年5月時点)。"
  - p124 Japan live births, calendar year 2025 confirmed figure = **671,236** persons (live births) (2025-01-01..2025-12-31) [DISCARD: Japan 2025 annual births; the H1 2026 analogue (p118) is the relevant transfer signal.] quote: "合計特殊出生率が1.14と過去最低を更新し、出生数は671,236人と10年連続で過去最少を記録しました。"
  - p125 Japan live births, calendar year 2025 flash figure cited in Diet = **705,809** persons (live births) (2025-01-01..2025-12-31) [DISCARD: Japan flash 2025 births; the confirmed figure p124 is the better vintage and the flash/confirmed gap is already noted.] quote: "2025年の出生数をめぐっては、国会で速報値705,809人が取り上げられ、10年連続の減少との政府認識が示されました。"
  - p126 Japan total fertility rate, calendar year 2025 confirmed figure = **1.14** children per woman (2025-01-01..2025-12-31) [DISCARD: Japan TFR; not needed for the Korea August estimate.] quote: "合計特殊出生率が1.14と過去最低を更新し、出生数は671,236人と10年連続で過去最少を記録しました。"
- dropped by code checks: 14 (number: more than one number in value_as_written: 11; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; number: unknown scale word '万': 1)

### b1 [administrative] Leading indicator from earlier-published registration counts

Hypothesis: The Ministry of the Interior and Safety (행정안전부) monthly resident-registration birth counts, or provincial tallies, are published weeks before KOSTAT's August 2026 Population Trends. If an August 2026 registration count exists by mid-October, it can be scaled by the historical KOSTAT/registration ratio to pin the target level directly, replacing the YoY-transfer route (m1) whose main uncertainty is the assumed August growth rate.

Queries issued by the searcher: 행정안전부 주민등록 인구통계 출생 2026년 8월; KOSTAT 출생아 수 주민등록 비교 2026; 주민등록 출생자 수 2026년 8월 행정안전부; 2026년 8월 출생아 수 인구동향 10월 23일

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://ww4.asiatoday.co.kr/kn/view.php?key=20260826010008557` -> **live_dated** (page date 2026-08-25); points raw/verified 0/0
- `https://kosis.kr/civilComplaint/qnaDetail.do?boardIdx=23332` -> **live_dated** (page date 2014-10-26); points raw/verified 0/0

### b2 [own_history] August-specific seasonal and calendar structure

Hypothesis: The August share of annual births (p73 = 8.4% for 2024, p85 = 8.0% for 1981–2023) is the key coefficient for the seasonal route (m2). A more recent August share (2025) and the number of weekend/holiday days in August 2026 would sharpen the seasonal index and reduce the largest uncertainty in the share-based method.

Queries issued by the searcher: 2025년 8월 출생아 수 인구동향 월별; 인구동향 2025년 8월 출생아 2만명; 2026년 8월 달력 공휴일 광복절 대체공휴일 주말; 2025년 연간 출생아 수 월별 비중 8월 인구동향

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=439018&tag=&nPage=1&ref_bid=203,204,205,206,207,210,211,11109,11113,11814,213,21` -> **live_dated** (page date 2025-10-29); points raw/verified 9/9
  - p127 South Korea live births, August 2025 (monthly Population Trends) = **20,867** persons (live births) (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p1 (same KOSTAT August 2025 level); adds no independent information.] quote: "출생아 수는 20,867명으로 전년동월대비 3.8% 증가"
  - p128 South Korea live births year-on-year change, August 2025 vs August 2024 = **3.8** percent (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p2.] quote: "출생아 수는 20,867명으로 전년동월대비 3.8% 증가"
  - p129 South Korea deaths, August 2025 = **28,971** persons (deaths) (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p3.] quote: "사망자 수는 28,971명으로 전년동월대비 9.8% 감소"
  - p130 South Korea deaths year-on-year change, August 2025 vs August 2024 = **9.8** percent (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p4.] quote: "사망자 수는 28,971명으로 전년동월대비 9.8% 감소"
  - p131 South Korea marriages, August 2025 = **19,449** cases (marriages) (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p5.] quote: "혼인 건수는 19,449건으로 전년동월대비 11.0% 증가"
  - p132 South Korea marriages year-on-year change, August 2025 vs August 2024 = **11** percent (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p6.] quote: "혼인 건수는 19,449건으로 전년동월대비 11.0% 증가"
  - p133 South Korea divorces, August 2025 = **7,196** cases (divorces) (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p7.] quote: "이혼 건수는 7,196건으로 전년동월대비 5.5% 감소"
  - p134 South Korea divorces year-on-year change, August 2025 vs August 2024 = **5.5** percent (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p8.] quote: "이혼 건수는 7,196건으로 전년동월대비 5.5% 감소"
  - p135 South Korea natural increase (live births minus deaths), August 2025 = **-8,105** persons (2025-08-01..2025-08-31) [DISCARD: Exact duplicate of p9.] quote: "자연증가(출생아 수 - 사망자 수)는 -8,105명"
- `https://www.kostat.go.kr/boardDownload.es?bid=204&list_no=439018&seq=3` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.ajunews.com/view/20260722094917670` -> **live_dated** (page date 2026-07-22); points raw/verified 14/2
  - p136 South Korea 2026 Liberation Day substitute holiday date (Aug 17, Monday) = **17** date (2026-08-17..2026-08-17) [DISCARD: Holiday date fact; the August 2026 calendar is already established and no working-day adjustment is applied in the chose] quote: "올해 광복절인 8월 15일은 토요일로, 17일 월요일이 대체공휴일로 지정됐다."
  - p137 South Korea 2026 National Foundation Day holiday period (Oct 3-5), length = **3** days (2026-10-03..2026-10-05) [DISCARD: October 2026 holiday; outside the target month.] quote: "개천절인 10월 3일이 토요일이어서 5일 월요일이 대체공휴일이다."
- `https://school.jbedu.kr/iri/M010305/list.do?y=2026&m=8` -> **live_dated** (page date 2026-08-17); points raw/verified 13/13
  - p138 Public holiday in August 2026: Liberation Day (광복절), South Korea = **2,026** date (2026-08-15..2026-08-15) [DISCARD: Date-valued cell (2026-08-15) mis-parsed as 2,026; the holiday fact is already carried by p136/p139.] quote: "2026.08.15 광복절"
  - p139 Substitute public holiday in August 2026 (대체공휴일), South Korea = **2,026** date (2026-08-17..2026-08-17) [DISCARD: Date-valued cell (2026-08-17) mis-parsed as 2,026; duplicate of p136.] quote: "2026.08.17 대체공휴일"
  - p140 Number of Saturdays in August 2026 calendar (South Korea) = **1** days (2026-08-01..2026-08-01) [DISCARD: Calendar cell for Aug 1, 2026; not a count of Saturdays. The month's weekend structure is already established by p142–p1] quote: "\| \| \| \| \| \| \| 1 \|"
  - p141 Number of Sundays in August 2026 calendar (South Korea) = **2** days (2026-08-02..2026-08-02) [DISCARD: Calendar cell for Aug 2, 2026; not a count of Sundays.] quote: "\| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \|"
  - p142 Number of Saturdays in August 2026 calendar (South Korea) = **8** days (2026-08-08..2026-08-08) [DISCARD: Calendar cell for Aug 8, 2026; not a count of Saturdays.] quote: "\| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \|"
  - p143 Number of Sundays in August 2026 calendar (South Korea) = **9** days (2026-08-09..2026-08-09) [DISCARD: Calendar cell for Aug 9, 2026; not a count of Sundays.] quote: "\| 9 \| 10 \| 11 \| 12 \| 13 \| 14 \| 15 \|"
  - p144 Number of Saturdays in August 2026 calendar (South Korea) = **15** days (2026-08-15..2026-08-15) [DISCARD: Calendar cell for Aug 15, 2026; not a count of Saturdays.] quote: "\| 9 \| 10 \| 11 \| 12 \| 13 \| 14 \| 15 \|"
  - p145 Number of Sundays in August 2026 calendar (South Korea) = **16** days (2026-08-16..2026-08-16) [DISCARD: Calendar cell for Aug 16, 2026; not a count of Sundays.] quote: "\| 16 \| 17 \| 18 \| 19 \| 20 \| 21 \| 22 \|"
  - p146 Number of Saturdays in August 2026 calendar (South Korea) = **22** days (2026-08-22..2026-08-22) [DISCARD: Calendar cell for Aug 22, 2026; not a count of Saturdays.] quote: "\| 16 \| 17 \| 18 \| 19 \| 20 \| 21 \| 22 \|"
  - p147 Number of Sundays in August 2026 calendar (South Korea) = **23** days (2026-08-23..2026-08-23) [DISCARD: Calendar cell for Aug 23, 2026; not a count of Sundays.] quote: "\| 23 \| 24 \| 25 \| 26 \| 27 \| 28 \| 29 \|"
  - p148 Number of Saturdays in August 2026 calendar (South Korea) = **29** days (2026-08-29..2026-08-29) [DISCARD: Calendar cell for Aug 29, 2026; not a count of Saturdays.] quote: "\| 23 \| 24 \| 25 \| 26 \| 27 \| 28 \| 29 \|"
  - p149 Number of Sundays in August 2026 calendar (South Korea) = **30** days (2026-08-30..2026-08-30) [DISCARD: Calendar cell for Aug 30, 2026; not a count of Sundays.] quote: "\| 30 \| 31 \| \| \| \| \| \|"
  - p150 Last day of August 2026 calendar (South Korea) = **31** days (2026-08-31..2026-08-31) [DISCARD: Calendar cell for Aug 31, 2026; not a count of days in the month.] quote: "\| 30 \| 31 \| \| \| \| \| \|"
- dropped by code checks: 12 (period_end 2026-12-31 after as_of: 3; value_as_written not in quote as a whole number: 5; number: more than one number in value_as_written: 1; number: no number in value_as_written: 3)

### b3 [forecasts_markets] Institutional nowcast for August 2026

Hypothesis: Statistics Korea, the Bank of Korea, or research institutes may publish a monthly or quarterly birth nowcast covering August 2026. A published nowcast would provide an independent central estimate and help resolve whether the 2026 YoY growth is decelerating toward the single digits (as the Jan–Jul path suggests) or holding near +11–15%.

Queries issued by the searcher: 한국은행 출생아 수 전망 2026; 통계청 출생아 수 전망 2026년 8월; KOSTAT birth nowcast 2026 monthly live births projection; 통계청 인구동향 2026년 8월 출생아 수 발표; 한국은행 출생아 수 nowcast 2026 하반기 전망 인구

- `https://www.edaily.co.kr/News/Read?newsId=03312806645583072` -> **live_dated** (page date 2026-09-23); points raw/verified 15/8
  - p151 South Korea live births year-on-year growth rate, July 2026 = **11.1** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p11.] quote: "7월 출생아는 2만 4275명으로 1년 전보다 11.1% 늘었다."
  - p152 South Korea crude birth rate, July 2026 = **5.6** births per 1,000 population (2026-07-01..2026-07-31) [DISCARD: July 2026 crude birth rate; the level p10 is the direct input.] quote: "조출생률은 5.6명으로 0.6명 상승했고"
  - p153 South Korea total fertility rate, July 2026 = **0.89** children per woman (2026-07-01..2026-07-31) [DISCARD: Duplicate of p21.] quote: "합계출산율은 0.89명으로 0.08명 높아졌다."
  - p154 South Korea cumulative live births year-on-year growth rate, January–July 2026 = **14.7** % (2026-01-01..2026-07-31) [DISCARD: Duplicate of p20.] quote: "1~7월 출생아는 17만 79명으로 14.7% 늘었다."
  - p155 South Korea cumulative live births, January–July 2015 (comparison) = **26** live births (persons) (2015-01-01..2015-07-31) [DISCARD: Value parsed as 26 (truncated '260,000+'); unusable as a number and not needed for the August estimate.] quote: "2015년 1~7월에는 26만 명 넘게 태어났다."
  - p156 South Korea marriages year-on-year growth rate, 2024 = **14.8** % (2024-01-01..2024-12-31) [keep: ] quote: "혼인 건수는 2024년 14.8%, 지난해 8.1% 늘며 2년 연속 증가했다."
  - p157 South Korea marriages year-on-year growth rate, July 2026 = **9.3** % (2026-07-01..2026-07-31) [keep: ] quote: "7월 혼인도 2만 2282건으로 9.3% 늘었다."
  - p158 South Korea age-specific fertility rate, women aged 35–39, July 2026 = **61.1** births per 1,000 women aged 35–39 (2026-07-01..2026-07-31) [DISCARD: July 2026 ASFR 35–39; the ASFR block is corroborating context, not a direct input to the August level.] quote: "35~39세 출산율은 가임여성 1000명당 61.1명으로 8.6명 높아져 상승 폭이 가장 컸고"
- `https://www.donga.com/news/article/all/20260826/134546009/1` -> **live_dated** (page date 2026-08-26); points raw/verified 12/4
  - p159 South Korea Q2 2026 live births year-on-year increase = **9,675** live births (persons) (2026-04-01..2026-06-30) [DISCARD: Duplicate of p52 (Q2 2026 +9,675).] quote: "올 2분기 출생아 수는 7만791명으로 1년 전보다 9675명(15.8%) 늘었다."
  - p160 South Korea Q2 2026 live births year-on-year growth rate = **15.8** % (2026-04-01..2026-06-30) [DISCARD: Duplicate of p52.] quote: "올 2분기 출생아 수는 7만791명으로 1년 전보다 9675명(15.8%) 늘었다."
  - p161 South Korea H1 2026 cumulative live births year-on-year growth rate = **15.4** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of p67 (H1 2026 +15.4%).] quote: "올 상반기 누적 출생아 수(14만5804명)도 전년 대비 증가 규모(1만9430명)와 증가율(15.4%) 모두 역대 최대였다."
  - p162 Consecutive quarters of increase in South Korea live births since Q2 2024 = **9** quarters (2024-04-01..2026-06-30) [DISCARD: Quarter-streak context; not a numerical input.] quote: "출생아 수는 2024년 2분기부터 9개 분기 연속 증가세를 보이고 있다."
- `https://www.etoday.co.kr/news/view/2610060?trc=main_top_sub` -> **live_dated** (page date 2026-08-02); points raw/verified 15/0
- `https://www.yna.co.kr/view/AKR20260801045700002` -> **live_dated** (page date 2026-08-02); points raw/verified 15/11
  - p163 South Korea Q1 2026 total fertility rate = **0.95** persons per woman (total fertility rate) (2026-01-01..2026-03-31) [DISCARD: Q1 2026 TFR; corroborating context.] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p164 South Korea April 2026 total fertility rate = **0.93** persons per woman (total fertility rate) (2026-04-01..2026-04-30) [DISCARD: April 2026 TFR; corroborating context.] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p165 South Korea May 2026 total fertility rate = **0.85** persons per woman (total fertility rate) (2026-05-01..2026-05-31) [DISCARD: May 2026 TFR; corroborating context.] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p166 South Korea year-on-year growth rate of cumulative live births January–May 2026 = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1∼5월까지 누적 출생아는 12만2천694명으로 집계됐다. 1년 전과 비교하면 15.2% 늘었다."
  - p167 South Korea annual total fertility rate 2025 = **0.8** persons per woman (total fertility rate) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p59 (2025 TFR 0.80).] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p168 South Korea annual total fertility rate 2024 = **0.75** persons per woman (total fertility rate) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p58 (2024 TFR 0.75).] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p169 South Korea annual total fertility rate 2023 = **0.72** persons per woman (total fertility rate) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p57 (2023 TFR 0.72).] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p170 South Korea annual total fertility rate 2019 = **0.92** persons per woman (total fertility rate) (2019-01-01..2019-12-31) [DISCARD: 2019 TFR; historical context only, not an August input.] quote: "올해 합계출산율이 0.9명대를 기록한다면 이는 2019년(0.92명) 이후 7년 만에 처음이다."
  - p171 South Korea annual total fertility rate 2000 = **1.48** persons per woman (total fertility rate) (2000-01-01..2000-12-31) [DISCARD: 2000 TFR; historical context only.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p172 South Korea annual total fertility rate 2017 = **1.05** persons per woman (total fertility rate) (2017-01-01..2017-12-31) [DISCARD: 2017 TFR; historical context only.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p173 South Korea annual total fertility rate 2018 = **0.98** persons per woman (total fertility rate) (2018-01-01..2018-12-31) [DISCARD: 2018 TFR; historical context only.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
- dropped by code checks: 34 (number: more than one number in value_as_written: 17; period year 2025 does not appear in the page text or URL (likely mis-dated): 3; period_end 2026-12-31 after as_of: 3; period_end missing or unparseable: 2; period year 2026 does not appear in the page text or URL (likely mis-dated): 6; number: unknown scale word '만': 2; period_end 2035-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth august', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Same KOSTAT August 2025 release: level 20,867 and +3.8% YoY are internally consistent (implies Aug 2024 ≈ 20,103). p1 is the anchor level for the August seasonal route.
- corroborating: ['p10', 'p11', 'p19', 'p108', 'p109'] All describe the same July 2026 KOSTAT release (24,275; +11.1%; +2,421). Multiple URLs, one underlying measurement — counts as one observation, not five.
- corroborating: ['p20', 'p110'] Same Jan–Jul 2026 cumulative +14.7% (17만79명, +21,851). One measurement, two outlets.
- corroborating: ['p21', 'p22', 'p107', 'p111', 'p112'] July 2026 TFR 0.89, +0.08 — same KOSTAT release repeated. Useful as a level check on the birth surge, not as an independent estimate.
- corroborating: ['p44', 'p45', 'p64'] June 2026: 23,111, +3,115, +15.6% — same release, three outlets. June is the last month with a confirmed level before the target.
- corroborating: ['p46', 'p47', 'p65', 'p66'] June 2026 TFR 0.88, +0.11 — same release.
- corroborating: ['p60', 'p61', 'p95', 'p96', 'p97'] Monthly YoY growth path in 2026: Jan +11.7, Feb +13.6, Mar +19.4, Apr +18.0, May +13.6, Jun +15.6, Jul +11.1. Consistent decelerating-but-still-double-digit regime; these are the key inputs for a YoY-
- corroborating: ['p52', 'p67'] Q2 2026 +15.8% and H1 2026 +15.4% — same underlying registration data, consistent with the monthly path.
- corroborating: ['p73', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p74', 'p75'] 2024 monthly shares of annual births sum to ~100% and give August = 8.4%. Internally consistent seasonal profile for a recent year.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94'] 1981–2023 cumulative shares give August = 8.0%. Older but long-run; the two seasonal vintages (8.0% vs 8.4%) bracket the August share and are not contradictory.
- corroborating: ['p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106'] Daily-average seasonal indices: Feb +19.6%, Jun −8.4%, Dec −8.9%, max-min gap 28.5% (recent) vs 41.6% (past). Consistent with the share-based seasonality and useful for a daily-rate cross-check.
- corroborating: ['p26', 'p27', 'p32', 'p33', 'p68', 'p14', 'p15'] Marriage surge: 22-month streak to Jan 2026, Jan 2026 +12.4%, Jun 2026 +14.0%, Jul 2026 +9.3%. Supports the d4 mechanism behind the 2026 birth increase (first births within ~2 years of marriage, p69/p
- corroborating: ['p55', 'p56', 'p57', 'p58', 'p59', 'p116', 'p117'] Annual TFR path 0.72 (2023) → 0.75 (2024) → 0.80 (2025) and monthly TFR 0.99 in Jan 2026 — consistent with the 2026 monthly surge; p117 is a monthly TFR, not an annual level, so it must not be read as
- corroborating: ['p118', 'p119', 'p120', 'p121', 'p122', 'p123'] Japan H1 2026 +0.8% (34.2万), May 2026 single month −1.7%, trailing-12m −0.4%. Japan's rebound is far weaker than Korea's; useful only as a weak regional sanity check, not a transferable growth rate.
- conflicting: ['p124', 'p125', 'p126'] Japan 2025 births: 671,236 confirmed vs 705,809 flash — a ~5% revision gap. Not about Korea, but a warning that provisional monthly figures (including Korea's) can be revised; supports keeping uncerta
- corroborating: ['p3', 'p4', 'p12', 'p13', 'p9', 'p18'] Deaths and natural increase are internally consistent (Aug 2025: 20,867 − 28,971 = −8,105; Jul 2026: 24,275 − 28,921 = −4,647). Not needed for the birth target but confirms the release's internal arit
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p7', 'p8', 'p16', 'p17'] Divorce statistics cluster — internally consistent but essentially irrelevant to the birth level; kept only as context.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p127'] Identical KOSTAT August 2025 live-birth level (20,867) from the same release; p127 is a duplicate copy, not independent evidence.
- corroborating: ['p2', 'p128'] Same +3.8% August 2025 YoY change; duplicate of the same KOSTAT measurement.
- corroborating: ['p10', 'p11', 'p19', 'p108', 'p109', 'p151'] All report July 2026 live births = 24,275 and +11.1% YoY from the same KOSTAT release; multiple outlets, one underlying measurement.
- corroborating: ['p20', 'p110', 'p154'] Jan–Jul 2026 cumulative births +14.7% (170,079) from the same release; consistent with p10/p11.
- corroborating: ['p44', 'p45', 'p64'] June 2026 births 23,111, +15.6% YoY; same KOSTAT measurement reported by multiple outlets.
- corroborating: ['p52', 'p159', 'p160'] Q2 2026 births 70,791, +9,675 (+15.8%); same release.
- corroborating: ['p67', 'p161'] H1 2026 cumulative births 145,804, +15.4%; same release.
- corroborating: ['p60', 'p61', 'p95', 'p96', 'p97'] Monthly 2026 YoY growth path (Jan +11.7%, Feb +13.6%, Mar +19.4%, Apr +18.0%, May +13.6%) is internally consistent with the cumulative +14.7% through July and shows deceleration from spring peaks.
- corroborating: ['p21', 'p22', 'p107', 'p111', 'p112', 'p153'] July 2026 TFR 0.89, +0.08 YoY; same release, consistent with the birth-count increase.
- corroborating: ['p46', 'p47', 'p65', 'p66'] June 2026 TFR 0.88, +0.11 YoY; same release.
- corroborating: ['p163', 'p164', 'p165'] Q1 0.95, April 0.93, May 0.85 TFR path is consistent with the monthly birth growth deceleration.
- corroborating: ['p73', 'p85'] August share of annual births: 8.4% (2024) vs 8.0% (1981–2023 cumulative). Both indicate August is a mid-to-upper month; the 2024 value is the more relevant recent coefficient.
- corroborating: ['p98', 'p99', 'p100', 'p101', 'p105', 'p106'] Daily-average seasonal indices (Feb +19.6%, Jun −8.4%, Dec −8.9%, max-min gap narrowing 41.6%→26.3%) describe the same seasonality as the monthly-share points; useful for calendar-day adjustment.
- corroborating: ['p102', 'p103', 'p104'] 2026 daily averages (Jan 868, Apr 817, May 747) are consistent with the monthly levels and the seasonal shape.
- corroborating: ['p118', 'p119', 'p120', 'p121', 'p122', 'p123'] Japan H1 2026 births +0.8% YoY, May single month −1.7%; a regional analogue showing only a weak positive trend, far below Korea's double-digit growth — a caution against extrapolating Korea's spring s
- corroborating: ['p55', 'p56', 'p57', 'p58', 'p59', 'p167', 'p168', 'p169'] Annual births 238,317 (2024, +3.6%) and 254,457 (2025, +6.8%); TFR 0.72→0.75→0.80. Consistent multi-year recovery baseline.
- corroborating: ['p26', 'p32', 'p33', 'p68', 'p156', 'p157'] Marriage registrations rising strongly (2024 +14.8%, 2025 +8.1%, Jan 2026 +12.4%, Jun 2026 +14.0%, Jul 2026 +9.3%) support the births upturn via the 1–2 year marriage-to-first-birth lag.
- corroborating: ['p69', 'p70', 'p53', 'p115'] First-birth share ~63–64% and 80% of the 2025 increase being first births, with 53.6% within 2 years of marriage, explains why the marriage surge is transmitting into 2026 births.
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41'] Divorce filings/rates for January 2026 form one internally consistent block; they are not inputs to the birth estimate but confirm the administrative reporting cadence.
- corroborating: ['p136', 'p138', 'p139'] August 2026 has Liberation Day (Sat Aug 15) plus a substitute holiday on Mon Aug 17; two public holidays in the month, relevant to any working-day adjustment.
- corroborating: ['p140', 'p142', 'p144', 'p146', 'p148', 'p141', 'p143', 'p145', 'p147', 'p149', 'p150'] Calendar rows confirm August 2026 has 31 days with five Saturdays and five Sundays; these are calendar facts, not independent birth measurements.
- corroborating: ['p42', 'p43'] 2019 monthly/cumulative births provide a historical reference level for the 'highest since 2019' comparisons used in 2026 reporting.
- corroborating: ['p3', 'p4', 'p129', 'p130', 'p12', 'p13'] Deaths series (Aug 2025 28,971, −9.8%; Jul 2026 28,921, +3.0%) is internally consistent but is not a birth input; kept only as context.
- corroborating: ['p5', 'p6', 'p131', 'p132'] August 2025 marriages 19,449, +11.0%; duplicate copies of the same KOSTAT measurement.
- corroborating: ['p7', 'p8', 'p133', 'p134'] August 2025 divorces 7,196, −5.5%; duplicate copies.
- corroborating: ['p9', 'p135'] August 2025 natural increase −8,105; duplicate copies, consistent with p1 and p3.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p18'] July 2026 marriages/divorces/natural increase from the same release as p10–p13.
- corroborating: ['p23', 'p24', 'p25', 'p48', 'p49', 'p50', 'p51', 'p71', 'p72', 'p113', 'p114', 'p158'] Age-specific fertility rates for 30–34 and 35–39 in June/July/Q2 2026 all show large increases, consistent with the birth-count surge being concentrated at older maternal ages.
- corroborating: ['p116', 'p117'] TFR 0.72 (2023) and 0.99 (Jan 2026) bracket the recovery; consistent with p57–p59 and p163.
- corroborating: ['p124', 'p125', 'p126'] Japan 2025 births 671,236 (confirmed) vs 705,809 (flash) illustrates the revision risk between flash and confirmed vital statistics — a caution for treating any single vintage as final.
- corroborating: ['p27', 'p162'] Longest prior birth-increase streak (25 months, 2006–2008) and the current 9-quarter streak frame the current upturn as historically unusual but not unprecedented.
- corroborating: ['p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84'] 2024 monthly shares sum to ~100% and are mutually consistent; August 8.4% is the coefficient of interest.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94'] 1981–2023 cumulative monthly shares are mutually consistent; August 8.0% is the long-run coefficient.
- corroborating: ['p155'] 2015 Jan–Jul births >260,000 gives the historical high-water mark against which 2026's 170,079 is still far below.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY growth factor for Korean live births | 1.1 | 1.04..1.16 | 0.9824..1.228 (widened) | ratio (this year / last year) | m1 (m1) | The 2026 monthly YoY growth path decelerated from +19.4% (March) and +18.0% (April) to +13.6% (May), +15.6% (June) and +11.1% (July), while the Jan–Jul cumulative was +14.7%. August 2025 was itself a strong base (+3.8%), so a further step down toward the low double digits is plausible; the range spa | The August 2026 KOSTAT provisional release follows the same month-of-occurrence definition and the recent deceleration continues; it transfers to the target month because August 2026 is the next month after the observed July 2026 figure. | A published August 2026 nowcast or registration count implying YoY growth outside roughly +4% to +16%, or evidence that the spring surge was a one-off timing shift that reverses in August. |
| a2 | August share of 2026 annual live births | 8.4 | 8..8.8 | 5.933..11.87 (widened) | % of annual live births | unused | August accounted for 8.4% of 2024 annual births (p73) and 8.0% over 1981–2023 (p85). The recent value is the better coefficient for 2026; the range brackets the long-run and recent estimates and allows for the narrowing seasonal amplitude noted in p105/p106. | The 2026 annual birth total is known or can be projected, and the August seasonal share remains near its recent level; it transfers to August 2026 because the seasonal pattern is stable across recent years. | A 2025 or 2026 August share materially outside 8.0–8.8%, or evidence that the 2026 monthly distribution has shifted (for example a policy-driven timing change). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 22,944 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input p56: id p56 unknown or discarded |
| m3 | yoy_scaling | n/a |  | [] |  | 0.00 |  | yoy_scaling needs signal for 2025 |
| m4 | series_naive | 20,867 |  | [] |  | 0.50 | equal |  |

Result: central **21,881**, 80% interval [15,883, 30,144], basis no_basis, weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['korea', 'sk', 'south korea']; measure stems ['birth', 'durin', 'korea', 'live', 'perso']


## Final answer

The best computed estimate for the number of live births in South Korea during August 2026, as first reported by Statistics Korea's monthly Population Trends release, is 21,881, with an interval of 15,883 to 30,144 (80%; no basis). The combination rests on 2 methods, but only two carried weight: a YoY-transfer estimate of 22,944 (weight 50%) and a naive seasonal benchmark of 20,867 (weight 50%). The YoY route applies an assumed August 2026 growth factor of 1.1 (range 0.9824 to 1.228) to the observed August 2025 level, anchored on the [n] monthly upturn. The benchmark simply repeats the last observed August. Both depend on the same KOSTAT vital-statistics system, so they are not independent. The interval is model-based and conditional on the growth assumption, not a demonstrated accuracy guarantee. The main risk is that the assumed growth factor is wrong, especially given August 2025's strong base. The most useful missing evidence would be an actual August 2026 signal or registration-based data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 YoY growth factor for Korean live births: 1.1 ratio (this year / last year), range 0.9824 to 1.228 (range widened by code); used by m1. Overturned by: A published August 2026 nowcast or registration count implying YoY growth outside roughly +[n] to +[n], or evidence that the spring surge was a one-off timing shift that reverses in August.

# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), via the monthly Population Trends (인구동향) release

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly vital statistics time series

Hypothesis: The number of live births in July 2026 can be estimated by applying the recent year-over-year change and seasonal factor to the July 2025 (or most recent July) reported value. The role is to anchor the level and trend; the assumption is that the recent trend and seasonal pattern continue.

Queries issued by the searcher: Statistics Korea monthly live births 2026 population trends; KOSTAT population trends live births July 2025 인구동향 출생아 수; 국가데이터처 2026년 5월 인구동향 보도자료 출생아 23,160명; "2026년 6월 인구동향" 출생아 수

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p1 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (persons) (2025-07-01..2025-07-31) [keep: ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p2 South Korea live births, July 2025, year-over-year change = **5.9** % (2025-07-01..2025-07-31) [keep: ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p3 South Korea deaths, July 2025 = **27,979** deaths (persons) (2025-07-01..2025-07-31) [keep: Deaths, not births; kept only as context for the release structure and natural-increase checks, not for the target.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p4 South Korea deaths, July 2025, year-over-year change = **0.7** % (2025-07-01..2025-07-31) [keep: Deaths YoY change; contextual only.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p5 South Korea marriages, July 2025 = **20,394** marriages (cases) (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p6 South Korea marriages, July 2025, year-over-year change = **8.4** % (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p7 South Korea divorces, July 2025 = **7,826** divorces (cases) (2025-07-01..2025-07-31) [keep: Divorces; contextual, not a birth input.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p8 South Korea divorces, July 2025, year-over-year change = **1.4** % (2025-07-01..2025-07-31) [keep: Divorces YoY; contextual.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p9 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (natural increase) (2025-07-01..2025-07-31) [keep: Natural increase; consistency check only.] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://www.yna.co.kr/view/AKR20260729067200002` -> **snapshot** (snapshot 20260730114307); points raw/verified 15/7
  - p10 South Korea live births, May 2026 year-over-year increase rate = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "올해 5월 출생아 수는 2만3천160명으로 1년 전에 비해 2천781명(13.6%) 늘었다."
  - p11 South Korea cumulative live births, January–May 2026 year-over-year increase rat = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "1년 전과 비교하면 1만6천166명(15.2%) 늘었다."
  - p12 South Korea total fertility rate, May 2026 = **0.85** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p13 South Korea total fertility rate, May 2026 year-over-year change = **0.1** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 증가했다."
  - p14 South Korea share of first-order births among live births, May 2026 = **63** % (2026-05-01..2026-05-31) [keep: Birth-order shares for May 2026; contextual for composition, not a level input.] quote: "출산 순위별 출생아 수 구성비는 첫째가 63.0%로 1.3%포인트(p) 늘었다."
  - p15 South Korea share of second-order births among live births, May 2026 = **31.7** % (2026-05-01..2026-05-31) [keep: Birth-order share; contextual.] quote: "둘째는 31.7%로 0.2%p 감소했다."
  - p16 South Korea share of third-or-higher-order births among live births, May 2026 = **5.3** % (2026-05-01..2026-05-31) [keep: Birth-order share; contextual.] quote: "셋째 이상은 5.3%로 1.1%p 줄었다."
- `https://www.joongang.co.kr/article/25449112` -> **snapshot** (snapshot 20260807174612); points raw/verified 15/0
- dropped by code checks: 23 (number: more than one number in value_as_written: 15; period year 2026 does not appear in the page text or URL (likely mis-dated): 7; value_as_written not in quote as a whole number: 1)

### d2 [related_series] Resident registration-based birth registrations

Hypothesis: Monthly birth registrations from the Ministry of the Interior and Safety (resident registration) are highly correlated with KOSTAT live births but may differ in timing and coverage. The ratio of KOSTAT live births to registration counts can be used to convert registration data into an estimate for July 2026.

Queries issued by the searcher: 주민등록 출생아 수 2026 행정안전부 주민등록 인구통계; resident registration births South Korea monthly 2025 statistics; 주민등록 출생등록 2026년 7월 전국 출생아 수 행안부; 2026년 6월 인구동향 출생아 수 발표

- `https://www.kostat.go.kr/boardDownload.es?bid=204&list_no=439018&seq=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?tblKey=GMN&fileId=198318441` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/callDownload.do?num=278446&filenum=1&dtime=20260326042846` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1466&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Marriage and fertility timing

Hypothesis: Births in a given month are strongly linked to marriages approximately 9–12 months earlier and to the number of women of childbearing age. A shift in marriages or in the age structure can adjust the expected birth level. The role is to provide a leading indicator or structural adjustment.

Queries issued by the searcher: Statistics Korea monthly marriage registrations 2025 혼인건수 월별; South Korea live births monthly 2025 2026 Statistics Korea Population Trends; 2025년 10월 인구동향 혼인건수 출생아 수 통계청; 2025년 9월 혼인건수 2만 통계청 인구동향 최다

- `https://www.gov.kr/portal/ntnadmNews/4591737?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20251224053700002?section=society/all` -> **snapshot** (snapshot 20251224031240); points raw/verified 13/1
  - p17 South Korea total fertility rate, October 2025 = **0.81** children per woman (2025-10-01..2025-10-31) [keep: ] quote: "합계출산율은 올해 10월 기준 0.81명으로 1년 전보다 0.02명 증가했다."
- `https://www.joongang.co.kr/article/25449289` -> **snapshot** (snapshot 20260814043421); points raw/verified 15/1
  - p18 South Korea monthly natural population decrease, May prior year = **8,103** persons (2024-05-01..2024-05-31) [keep: May 2024 natural decrease; contextual, different period and quantity.] quote: "5월 한 달 자연감소한 인구도 6413명으로 지난해 5월(8103명)보다 20.9% 줄었다."
- `https://v.daum.net/v/20250924121739428` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 26 (number: more than one number in value_as_written: 21; value_as_written not in quote as a whole number: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 4)

### d4 [base_rates] Total fertility rate and population denominators

Hypothesis: The expected number of births in July 2026 can be approximated by the product of the number of women aged 15–49, the general fertility rate (or age-specific fertility rates), and the fraction of annual births occurring in July. The role is to provide a structural cross-check independent of recent monthly fluctuations.

Queries issued by the searcher: South Korea age-specific fertility rates 2025 KOSTAT; KOSTAT birth seasonality monthly share of annual births South Korea July; 2026년 6월 인구동향 출생아 수 국가데이터처 발표; 월별 출생아 수 2025년 7월 21,854 명 통계청 인구동향

- `https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=H000202&idx_cd=H0002&freq=Y&period=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mbiz.heraldcorp.com/article/10432049` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/news/policyNewsView.do?newsId=148970652` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Official projections and nowcasts

Hypothesis: Statistics Korea or other institutions may publish monthly or quarterly birth projections or nowcasts that can serve as a direct estimate for July 2026. The role is to provide an independent forecast to compare with other routes.

Queries issued by the searcher: South Korea birth forecast 2026 monthly live births KOSTAT projection; KOSTAT 출생아 수 전망 2026 월별; 행정안전부 주민등록 출생등록 2026년 7월 출생등록자; 한국은행 출생아 수 전망 2026 인구동향 nowcast

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsworks.co.kr/news/articleView.html?idxno=848723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.ppomppu.co.kr/new/bbs_view.php?id=news_society&no=513655` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [shocks] Policy and economic shocks affecting births

Hypothesis: Government policies (e.g., baby bonuses, parental leave expansions) or economic shocks (housing costs, employment) may have changed the birth rate in 2025–2026. The role is to adjust the trend if a measurable policy change occurred. The assumption is that any effect is gradual and can be bounded.

Queries issued by the searcher: South Korea birth incentive policy 2025 impact on births number of additional births; 저출산 대책 2025 출생아 수 효과 정부 예산; 2026년 5월 출생아 수 인구동향 전년동월비 증가; 2025년 7월 출생아 수 2만명 인구동향 통계청

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.betterfuture.go.kr/cmm/fms/FileDown.do;jsessionid=00374253B59EEE01607C7C0F37599F38.node10?atchFileId=FILE_000000000013288&fileSn=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businesstimes.com.sg/international/south-koreas-baby-bump-extends-second-year-offering-hope` -> **snapshot** (snapshot 20260713065320); points raw/verified 13/9
  - p19 South Korea total fertility rate, 2025 preliminary = **0.8** children per woman (lifetime expected births) (2025-01-01..2025-12-31) [keep: ] quote: "The number of babies a woman is expected to have over her lifetime increased to 0.8 last year from 0.75 in 2024, preliminary data released on Wednesday (Feb 25)"
  - p20 South Korea total fertility rate, 2024 = **0.75** children per woman (lifetime expected births) (2024-01-01..2024-12-31) [keep: ] quote: "increased to 0.8 last year from 0.75 in 2024, preliminary data released on Wednesday (Feb 25) by the Ministry of Data and Statistics showed."
  - p21 South Korea live births, 2025 (preliminary annual total) = **254,500** live births (persons) (2025-01-01..2025-12-31) [keep: ] quote: "Births in 2025 climbed 6.8 per cent from the previous year to 254,500, the highest total since 2021"
  - p22 South Korea year-on-year change in births, 2025 vs 2024 = **6.8** per cent change in live births (2025-01-01..2025-12-31) [keep: ] quote: "Births in 2025 climbed 6.8 per cent from the previous year to 254,500, the highest total since 2021"
  - p23 South Korea live births, 2021 (comparison year) = **260,600** live births (persons) (2021-01-01..2021-12-31) [keep: 2021 births comparison; contextual only.] quote: "the highest total since 2021, when about 260,600 babies were born."
  - p24 South Korea cumulative spending on fertility incentives and family support progr = **380,000,000,000,000** won (South Korean currency) (2006-01-01..2023-12-31) [keep: Cumulative fertility spending; contextual for policy direction, not a numeric input.] quote: "spending an estimated 380 trillion won (S$335 billion) on fertility incentives and family support programmes between 2006 and 2023."
  - p25 South Korea cumulative fertility/family support spending converted to Singapore  = **335,000,000,000** Singapore dollars (2006-01-01..2023-12-31) [keep: Same spending in SGD; redundant copy of p24, no additional information.] quote: "spending an estimated 380 trillion won (S$335 billion) on fertility incentives and family support programmes between 2006 and 2023."
  - p26 South Korea budget allocated in 2025 for programmes directly aimed at low birth  = **28,600,000,000,000** won (South Korean currency) (2025-01-01..2025-12-31) [keep: 2025 low-birth-rate budget; contextual for policy shock direction.] quote: "The country allocated 28.6 trillion won in 2025 for programmes directly aimed at addressing its low birth rate, a 13 per cent increase from a year earlier"
  - p27 South Korea year-on-year increase in 2025 low-birth-rate programme budget = **13** per cent increase in budget (2025-01-01..2025-12-31) [keep: Budget growth rate; contextual.] quote: "The country allocated 28.6 trillion won in 2025 for programmes directly aimed at addressing its low birth rate, a 13 per cent increase from a year earlier"
- `https://www.mk.co.kr/en/economy/11342193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### b1 [own_history] KOSTAT monthly birth series completeness

Hypothesis: The July 2026 estimate via yoy_scaling needs the July 2024 and July 2025 KOSTAT live-birth levels and the 2024-2025 monthly YoY path. p1 gives July 2025 but July 2024 is missing, so the July 2025 YoY (+5.9%) cannot be chained into a 2026 factor without the 2024 base. Finding the July 2024 KOSTAT figure (and ideally the full 2024 monthly series) would let us build a proper July-specific YoY signal and backtest the seasonal factor.

Queries issued by the searcher: KOSTAT Population Trends July 2024 live births monthly; Statistics Korea 인구동향 2024년 7월 출생아 수; 2025년 7월 인구동향 출생아 수 통계청; 2024년 월별 출생아 수 1월 2월 3월 4월 5월 6월 7월 8월 9월 10월 11월 12월 통계청

- `https://www.kostat.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=432861` -> **snapshot** (snapshot 20250421234650); points raw/verified 9/9
  - p28 South Korea live births, July 2024 (KOSTAT Population Trends monthly release) = **20,601** live births (persons) (2024-07-01..2024-07-31) [keep: ] quote: "출생아 수는 20,601명으로 전년동월대비 7.9% 증가"
  - p29 South Korea live births year-on-year change, July 2024 vs July 2023 = **7.9** % (2024-07-01..2024-07-31) [keep: ] quote: "출생아 수는 20,601명으로 전년동월대비 7.9% 증가"
  - p30 South Korea deaths, July 2024 = **28,240** deaths (persons) (2024-07-01..2024-07-31) [keep: July 2024 deaths; contextual.] quote: "사망자 수는 28,240명으로 전년동월대비 0.4% 증가"
  - p31 South Korea deaths year-on-year change, July 2024 vs July 2023 = **0.4** % (2024-07-01..2024-07-31) [keep: July 2024 deaths YoY; contextual.] quote: "사망자 수는 28,240명으로 전년동월대비 0.4% 증가"
  - p32 South Korea marriages, July 2024 = **18,811** marriages (cases) (2024-07-01..2024-07-31) [keep: ] quote: "혼인 건수는 18,811건으로 전년동월대비 32.9% 증가"
  - p33 South Korea marriages year-on-year change, July 2024 vs July 2023 = **32.9** % (2024-07-01..2024-07-31) [keep: ] quote: "혼인 건수는 18,811건으로 전년동월대비 32.9% 증가"
  - p34 South Korea divorces, July 2024 = **7,939** divorces (cases) (2024-07-01..2024-07-31) [keep: July 2024 divorces; contextual.] quote: "이혼 건수는 7,939건으로 전년동월대비 5.9% 증가"
  - p35 South Korea divorces year-on-year change, July 2024 vs July 2023 = **5.9** % (2024-07-01..2024-07-31) [keep: July 2024 divorces YoY; contextual.] quote: "이혼 건수는 7,939건으로 전년동월대비 5.9% 증가"
  - p36 South Korea natural increase (live births minus deaths), July 2024 = **-7,639** persons (natural increase) (2024-07-01..2024-07-31) [keep: July 2024 natural increase; consistency check.] quote: "자연증가(출생아 수 - 사망자 수)는 -7,639명"
- `https://sri.kostat.go.kr/boardDownload.es?bid=204&list_no=435204&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4026259` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Resident-registration monthly births

Hypothesis: Ministry of the Interior and Safety resident-registration birth counts are published with a shorter lag than KOSTAT and are highly correlated with KOSTAT live births. A registration count for July 2026 (or June 2026 as a nowcast input) plus a KOSTAT/registration ratio would provide an independent, more timely route to the July 2026 target and help validate the YoY-scaling result.

Queries issued by the searcher: 주민등록 인구통계 월별 출생자 수 2026; KOSTAT 인구동향 2026년 7월 출생아 수; 주민등록 기준 출생아 수 2026년 6월 행정안전부; 행안부 주민등록 출생아 등록 2026년 7월

- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/locgovNews/4699076` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Official or institutional 2026 birth projection

Hypothesis: Statistics Korea or research institutes may publish 2026 monthly or quarterly birth nowcasts/projections. A published July 2026 or Q3 2026 projection would directly constrain the target and help resolve the uncertainty between the +6.8% annual 2025 trend and the +13.6% May 2026 monthly signal.

Queries issued by the searcher: 통계청 인구동향 2026년 출생아 수 전망; Statistics Korea 2026 birth projection monthly nowcast population trends; 2025년 7월 출생아 수 인구동향 2만명; 국회예산정책처 인구전망 2025~2045 출생아 수 전망 연도별; 국회예산정책처 "인구전망" 2026년 출생아 수 30만명 전망 보고서; 2026년 출생아 수 전망 30만명 하반기 출산 통계청 장래인구추계

- `https://www.yna.co.kr/view/AKR20260801045700002` -> **snapshot** (snapshot 20260803065725); points raw/verified 15/11
  - p37 South Korea total fertility rate, Q1 2026 = **0.95** persons per woman (total fertility rate) (2026-01-01..2026-03-31) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p38 South Korea total fertility rate, April 2026 = **0.93** persons per woman (total fertility rate) (2026-04-01..2026-04-30) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p39 South Korea total fertility rate, May 2026 = **0.85** persons per woman (total fertility rate) (2026-05-01..2026-05-31) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p40 Year-on-year growth rate of cumulative live births, January–May 2026 vs 2025 = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1∼5월까지 누적 출생아는 12만2천694명으로 집계됐다. 1년 전과 비교하면 15.2% 늘었다."
  - p41 South Korea annual total fertility rate, 2025 = **0.8** persons per woman (total fertility rate) (2025-01-01..2025-12-31) [keep: ] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p42 South Korea annual total fertility rate, 2024 = **0.75** persons per woman (total fertility rate) (2024-01-01..2024-12-31) [keep: ] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p43 South Korea annual total fertility rate, 2023 = **0.72** persons per woman (total fertility rate) (2023-01-01..2023-12-31) [keep: ] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p44 South Korea annual total fertility rate, 2019 = **0.92** persons per woman (total fertility rate) (2019-01-01..2019-12-31) [keep: 2019 TFR; long-run context.] quote: "올해 합계출산율이 0.9명대를 기록한다면 이는 2019년(0.92명) 이후 7년 만에 처음이다."
  - p45 South Korea annual total fertility rate, 2018 = **0.98** persons per woman (total fertility rate) (2018-01-01..2018-12-31) [keep: 2018 TFR; long-run context.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p46 South Korea annual total fertility rate, 2017 = **1.05** persons per woman (total fertility rate) (2017-01-01..2017-12-31) [keep: 2017 TFR; long-run context.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p47 South Korea annual total fertility rate, 2000 = **1.48** persons per woman (total fertility rate) (2000-01-01..2000-12-31) [keep: 2000 TFR; long-run context.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
- `https://gji.re.kr/diam/web/base/board/file_download_new.php?dm_table=infographic&wr_id=103&no=1&nonce=5c648ac4d3c6d51346bf%7C1784931246%7C8b310a70c1a7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/society/2026/08/03/20260803010003` -> **snapshot** (snapshot 20260803052117); points raw/verified 15/11
  - p48 South Korea Q1 2026 total fertility rate = **0.95** children per woman (2026-01-01..2026-03-31) [keep: ] quote: "올해 1분기 합계출산율은 0.95명으로 집계됐다."
  - p49 South Korea April 2026 total fertility rate = **0.93** children per woman (2026-04-01..2026-04-30) [keep: ] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p50 South Korea May 2026 total fertility rate = **0.85** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p51 South Korea April 2026 total fertility rate year-on-year increase = **0.13** children per woman (2026-04-01..2026-04-30) [keep: April 2026 TFR YoY change; corroborates the 2026 acceleration.] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p52 South Korea May 2026 total fertility rate year-on-year increase = **0.1** children per woman (2026-05-01..2026-05-31) [keep: May 2026 TFR YoY change; corroborates the 2026 acceleration.] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p53 South Korea live births January-May 2026 year-on-year increase rate = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p54 South Korea May 2026 live births year-on-year increase = **2,781** live births (persons) (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p55 South Korea May 2026 live births year-on-year increase rate = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p56 South Korea 2025 total fertility rate = **0.8** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p57 South Korea 2024 total fertility rate = **0.75** children per woman (2024-01-01..2024-12-31) [keep: ] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p58 South Korea 2023 total fertility rate (record low) = **0.72** children per woman (2023-01-01..2023-12-31) [keep: 2023 TFR; redundant with p43 but harmless context.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
- dropped by code checks: 8 (number: more than one number in value_as_written: 7; number: unknown scale word '만': 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Same KOSTAT July 2025 release: level 21,803 and YoY +5.9% are internally consistent and define the July 2025 anchor for the target's own series.
- corroborating: ['p10', 'p11', 'p12', 'p13'] Same May 2026 KOSTAT release: May births +13.6% YoY, Jan-May cumulative +15.2%, and TFR 0.85 (+0.10) all point to a strong 2026 birth rebound. They share one underlying measurement, so they are one si
- corroborating: ['p19', 'p20', 'p21', 'p22'] Same Feb 2026 preliminary annual release: 2025 TFR 0.8 vs 0.75 in 2024 and 2025 births 254,500 (+6.8%) are mutually consistent and establish the 2025 level and upward trend.
- corroborating: ['p1', 'p21'] July 2025 births (21,803) and the 2025 annual total (254,500) are from the same statistical system and are consistent with a rising 2025 path; the annual figure is a useful level check but not a July 
- corroborating: ['p10', 'p21'] The 2025 annual increase (+6.8%) and the May 2026 monthly increase (+13.6%) both indicate acceleration into 2026, supporting a positive YoY factor for July 2026.
- corroborating: ['p17', 'p19'] October 2025 TFR 0.81 and 2025 preliminary TFR 0.8 are consistent; both are from KOSTAT and describe the same 2025 fertility level.
- corroborating: ['p3', 'p4', 'p9'] July 2025 deaths 27,979, deaths -0.7%, and natural decrease -6,175 are internally consistent (21,803 - 27,979 = -6,176, rounding). They are context only for the birth target.
- corroborating: ['p5', 'p6'] July 2025 marriages 20,394 and +8.4% YoY are one measurement; marriages are a leading indicator for births roughly 9-12 months later, so mid-2025 marriage strength supports elevated births in mid-2026
- corroborating: ['p7', 'p8'] July 2025 divorces 7,826 and -1.4% are one measurement and are not directly informative for the birth level.
- corroborating: ['p24', 'p25', 'p26', 'p27'] Same article: cumulative 2006-2023 fertility spending (380 trillion won / S$335bn) and the 2025 low-birth-rate budget (28.6 trillion won, +13%) describe policy scale. They are contextual for the persi
- corroborating: ['p18'] May 2024 natural decrease 8,103 is a prior-year context point; it is consistent with the improving natural-decrease trend but is not a birth count.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] Same KOSTAT July 2025 release: level 21,803 and +5.9% YoY are internally consistent (implies July 2024 ≈ 20,588, close to the separately reported p28 = 20,601; the small gap is consistent with revisio
- corroborating: ['p28', 'p29'] Same KOSTAT July 2024 release: 20,601 and +7.9% YoY. This is the missing 2024 base needed to chain the July YoY path; it is a different vintage from p1/p2, so the implied 2024 level differs slightly f
- corroborating: ['p1', 'p28'] Together they give the July 2024→2025 level path (20,601 → 21,803, +5.8%), the anchor for a July-specific YoY extrapolation into 2026.
- corroborating: ['p10', 'p54', 'p55'] Same May 2026 KOSTAT release reported by two outlets: 23,160 births, +2,781 (+13.6%) YoY. Identical underlying measurement, so not independent confirmation.
- corroborating: ['p11', 'p40', 'p53'] Same Jan–May 2026 cumulative figure (122,694 births, +16,166, +15.2%) from three outlets; one underlying statistic.
- corroborating: ['p12', 'p13', 'p39', 'p50', 'p52'] May 2026 TFR 0.85, +0.10 YoY, repeated across releases; same KOSTAT measurement.
- corroborating: ['p37', 'p38', 'p48', 'p49'] Q1 2026 TFR 0.95 and April 2026 TFR 0.93, repeated across outlets; same source.
- corroborating: ['p19', 'p21', 'p22', 'p41', 'p56'] 2025 annual TFR 0.80 and 2025 births 254,500 (+6.8%) agree across the February preliminary release and later Korean-language reporting.
- corroborating: ['p20', 'p42', 'p57'] 2024 TFR 0.75 repeated across sources; same annual statistic.
- corroborating: ['p43', 'p58'] 2023 TFR 0.72 (record low) repeated; same statistic.
- corroborating: ['p10', 'p11', 'p12'] May 2026 monthly and Jan–May cumulative growth are mutually consistent with a strong 2026 rebound; the monthly +13.6% is above the cumulative +15.2% only in the sense that both are large positive, no 
- conflicting: ['p1', 'p10'] July 2025 was +5.9% YoY while May 2026 was +13.6% YoY and Jan–May 2026 +15.2%. These are different periods, not a contradiction, but they imply the 2026 monthly YoY path is much steeper than the 2025 
- conflicting: ['p21', 'p10'] 2025 full-year growth was +6.8% while early-2026 monthly growth is ~14–15%; the acceleration is real in the data but its persistence into July 2026 is the key uncertainty.
- corroborating: ['p5', 'p6', 'p32', 'p33'] July marriages rose sharply in both 2024 (+32.9%) and 2025 (+8.4%), a leading indicator for births roughly 9–12 months later, i.e. into 2026.
- corroborating: ['p3', 'p4', 'p30', 'p31'] July deaths are stable (28,240 in 2024, 27,979 in 2025); they are not needed for the birth target but confirm the release structure and that p9/p36 natural-increase figures are consistent.
- corroborating: ['p9', 'p36'] Natural increase = births − deaths checks out for both Julys (21,803−27,979=−6,176≈−6,175; 20,601−28,240=−7,639).
- corroborating: ['p24', 'p25', 'p26', 'p27'] Fertility-policy spending figures (380tn won 2006–2023; 28.6tn won in 2025, +13%) are contextual for the policy-shock direction only; they are not birth counts.
- corroborating: ['p17', 'p19', 'p41'] October 2025 TFR 0.81 and 2025 annual 0.80 are consistent with a mild upward trend through 2025.
- corroborating: ['p44', 'p45', 'p46', 'p47'] Long-run TFR history (1.48 in 2000 down to 0.72 in 2023) provides the structural backdrop; not directly usable for a July 2026 level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 YoY change factor in KOSTAT live births relative to July 2025 | 1.11 | 1.04..1.19 | 0.995..1.244 (widened) | ratio | unused | July 2025 was +5.9% YoY (p1/p2) and July 2024 +7.9% (p28/p29), but 2026 monthly growth has accelerated: May 2026 +13.6% (p10/p54/p55) and Jan–May 2026 +15.2% (p11/p40/p53). A July 2026 factor near +11% sits between the 2025 July rate and the early-2026 monthly rates, allowing for some fade of the 20 | The 2026 birth rebound observed through May persists at a somewhat reduced pace into July 2026, and no major revision or definitional break occurs between the May and July releases. | A June or July 2026 KOSTAT release showing YoY growth below ~4% or above ~20%, or evidence that the early-2026 surge was a timing/registration artifact rather than a real birth increase. |
| a2 | July share of annual live births in South Korea | 0.083 | 0.078..0.088 | 0.05858..0.1172 (widened) | share | m2 (m2) | July is a mid-year month; with roughly uniform monthly distribution the share would be about 1/12 ≈ 0.083. Korean birth seasonality is mild, so a range of 0.078–0.088 covers plausible seasonal variation. Used only to convert an annual 2026 birth level into a July level. | The seasonal distribution of births in 2026 resembles the recent historical pattern and no unusual event shifts July births. | Evidence of a strong July-specific seasonal spike or trough in recent Korean monthly birth data, or a known 2026 event (e.g., a policy deadline) that concentrates births in July. |
| a4 | 2026 annual live births relative to 2025 annual live births (change factor) | 1.08 | 1.02..1.15 | 0.9687..1.211 (widened) | ratio | m2 (m2) | 2025 annual births were 254,500 (p21) with +6.8% growth (p22). The 2026 monthly evidence shows a stronger start — Jan–May +15.2% (p11/p40/p53) and May +13.6% (p10/p54/p55) — but some fade is likely over the remaining months, so a full-year factor of about +8% is used, with a range from +2% to +15%.  | The 2026 monthly birth growth observed through May continues for the rest of 2026 at a moderated pace, and the 2025 annual total is not substantially revised. | A mid-2026 KOSTAT release showing cumulative 2026 births far outside the implied range, or a sharp reversal in monthly YoY growth. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | n/a |  | [] |  | 0.00 |  | yoy_scaling needs signal for 2026 |
| m2 | formula_mc | 22,785 | ['p21'] / ['a2', 'a4'] | [] |  | 1.00 | equal |  |

Result: central **22,785**, 80% interval [15,190, 34,179], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for live births occurring in South Korea during July 2026, as first reported by Statistics Korea's monthly Population Trends release, is 22,785. This is a model-based interval of 15,190 to 34,179 at the 80% level, conditional on the stated assumptions rather than a demonstrated accuracy guarantee.

The estimate rests on 1 method(s); the retained route uses observed [n] annual births (58 observed point) combined with two analyst assumptions: July's share of annual births (0.083, range 0.05858–0.1172) and the [n] annual change factor (1.08, range 0.9687–1.211). The July-specific year-over-year route was unavailable, so the result depends on transfers and assumptions, not direct July 2026 observation.

The main risk is that the assumed [n] annual growth factor is wrong, since recent monthly gains may fade. The most valuable missing evidence would be the actual July 2026 monthly birth count or a reliable July-specific year-over-year signal.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 July share of annual live births in South Korea: 0.083 share, range 0.05858 to 0.1172 (range widened by code); used by m2. Overturned by: Evidence of a strong July-specific seasonal spike or trough in recent Korean monthly birth data, or a known [n] event (e.g., a policy deadline) that concentrates births in July.
- a4 [n] annual live births relative to 2025 annual live births (change factor): 1.08 ratio, range 0.9687 to 1.211 (range widened by code); used by m2. Overturned by: A mid-2026 KOSTAT release showing cumulative [n] births far outside the implied range, or a sharp reversal in monthly YoY growth.

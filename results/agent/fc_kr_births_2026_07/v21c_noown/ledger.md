# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends (인구동향)

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [related_series] Administrative registration data

Hypothesis: Births are registered with local governments, and the number of birth registrations in a month is closely related to the number of live births occurring in that month, though with a lag. If registration data for July 2026 are available before the KOSTAT release, they can provide an early indicator.

Queries issued by the searcher: 행정안전부 주민등록 출생아 수 2026년 7월; South Korea birth registration July 2026 resident registration; 주민등록 인구통계 2026년 7월 출생자 수 행정안전부; 행정안전부 주민등록 출생아 2026년 7월 발표

- `https://www.gov.kr/portal/ntnadmNews/4866340?srchOrgCd=1241000&pageIndex=1&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41885&pageIndex=&group=S&srchCode=&startDate=&endDate=&srchKeyword=&groupId=&codeLevel1=&codeLevel2=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=447111` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=447111&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [base_rates] Demographic accounting

Hypothesis: Live births in a month can be estimated from the number of women of childbearing age and the general fertility rate, or from the number of marriages in prior months (since first births often follow marriage). If marriage counts for late 2025 and early 2026 are available, they can inform births in July 2026.

Queries issued by the searcher: South Korea monthly marriage statistics 2026 혼인 건수 월별; 통계청 인구동향 2026년 6월 혼인 건수 출생아 수; 2026년 5월 인구동향 출생아 수 혼인 건수 국가데이터처; 결혼 후 첫째아 출산 시차 평균 개월 혼인 출산 시차

- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4793427` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a20108090000&bid=11749&act=view&list_no=445396` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4690717` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Hospital and health insurance claims

Hypothesis: Most births occur in hospitals, and health insurance claims for delivery-related care can serve as a proxy for live births. The number of claims for normal delivery or cesarean section in July 2026, if available, can be scaled to national births.

Queries issued by the searcher: 건강보험심사평가원 분만 청구 2026년 7월; Statistics Korea monthly population trends live births 2026; 2026년 6월 인구동향 출생아 수 국가데이터처 발표; 국민건강보험공단 분만 진료비 청구 통계 출생아 수 비교

- `https://news.tvchosun.com/site/data/html_dir/2026/07/29/2026072990177.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [shocks] Calendar and policy effects

Hypothesis: Births in July 2026 may be affected by the timing of holidays, government incentives, or changes in parental leave policies. For example, if a new birth incentive was introduced in 2025 or 2026, it could have shifted birth timing. Also, the Lunar calendar and school entry cutoff can influence seasonality.

Queries issued by the searcher: Statistics Korea Monthly Population Trends live births 2026 July; South Korea birth incentive 2026 policy parental leave baby bonus; 2026년 7월 공휴일 평일 수 주말 2025년 7월 비교; 2026년 6월 인구동향 출생아 수 발표

- `https://www.gov.kr/portal/ntnadmNews/4866340` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4742596` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nongmin.com/article/20260709500316` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Official projections and nowcasts

Hypothesis: Statistics Korea or other institutions may publish monthly or quarterly birth projections that include July 2026. These can serve as a prior, though they may be model-based rather than observed.

Queries issued by the searcher: Statistics Korea birth forecast 2026 monthly live births projection; 2026년 출생아 수 전망 월별; 2025년 7월 출생아 수 인구동향 2만명; 2026년 6월 인구동향 출생아 수 23,111명 국가데이터처

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260802035341); points raw/verified 15/0
- `https://www.edaily.co.kr/News/Read?newsId=04877366645519440` -> **snapshot** (snapshot 20260809115657); points raw/verified 11/0
- dropped by code checks: 26 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 2; number: unknown scale word '만': 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 11; number: more than one number in value_as_written: 4; period_end 2035-12-31 after as_of: 1)

### d6 [physical_flow] Obstetric care capacity and utilisation

Hypothesis: The number of live births is constrained by the number of obstetric beds, delivery rooms, and obstetricians, and their utilisation. If capacity and utilisation data for July 2026 are available, they can bound the plausible number of births.

Queries issued by the searcher: 산부인과 병상 수 2026 분만실; obstetric beds South Korea 2026 delivery rooms number; 2026년 6월 출생아 수 인구동향 통계청; 산부인과 전문의 수 2026 분만 담당 전문의 통계

- `https://it.chosun.com/news/articleView.html?idxno=2023092165941` -> **snapshot** (snapshot 20260718211432); points raw/verified 15/15
  - p1 Number of obstetric and gynecology clinics/hospitals nationwide in South Korea ( = **1,571** facilities (2025-01-01..2025-12-31) [keep: ] quote: "2025년 기준 전국 산부인과 병·의원은 총 1571곳으로 집계됐다."
  - p2 Number of obstetric and gynecology clinics/hospitals nationwide in South Korea ( = **1,573** facilities (2021-01-01..2021-12-31) [DISCARD: Redundant with p1: same universe, same source, and the 2021 value adds nothing beyond confirming that the ob/gyn facilit] quote: "4년 동안 전체 산부인과 병·의원 수는 1573곳에서 1571곳으로 거의 변하지 않았지만"
  - p3 Number of facilities actually providing delivery care nationwide in South Korea  = **260** facilities (2025-01-01..2025-12-31) [keep: ] quote: "실제 분만 진료를 시행한 기관은 260곳으로 전체의 16.5%에 그쳤다."
  - p4 Share of obstetric/gynecology clinics/hospitals providing delivery care nationwi = **16.5** % (2025-01-01..2025-12-31) [DISCARD: Arithmetic restatement of p3/p1 (260/1,571 = 16.5%); carries no information beyond p3 and p1.] quote: "실제 분만 진료를 시행한 기관은 260곳으로 전체의 16.5%에 그쳤다."
  - p5 Number of medical institutions providing delivery care nationwide including tert = **436** facilities (2025-01-01..2025-12-31) [keep: ] quote: "상급종합병원과 종합병원, 조산원 등을 모두 포함해도 전국에서 분만 진료를 시행한 의료기관은 436곳에 불과했다."
  - p6 Number of medical institutions providing delivery care nationwide including tert = **620** facilities (2015-01-01..2015-12-31) [keep: ] quote: "2015년 620곳과 비교하면 10년 사이 184곳, 29.7% 감소한 수치다."
  - p7 Decrease in number of delivery-providing medical institutions nationwide over 10 = **184** facilities (2015-01-01..2025-12-31) [DISCARD: Arithmetic restatement of p5 and p6 (620-436 = 184); not an independent observation.] quote: "2015년 620곳과 비교하면 10년 사이 184곳, 29.7% 감소한 수치다."
  - p8 Percentage decrease in delivery-providing medical institutions nationwide over 1 = **29.7** % (2015-01-01..2025-12-31) [DISCARD: Arithmetic restatement of p5 and p6 (184/620 = 29.7%); not an independent observation.] quote: "2015년 620곳과 비교하면 10년 사이 184곳, 29.7% 감소한 수치다."
  - p9 Number of clinic/hospital-level obstetric-gynecology facilities providing delive = **313** facilities (2021-01-01..2021-12-31) [keep: ] quote: "분만을 시행하는 병·의원급 산부인과는 2021년 313곳에서 2022년 300곳, 2023년 282곳, 2024년 269곳, 2025년 260곳으로 감소했다."
  - p10 Number of clinic/hospital-level obstetric-gynecology facilities providing delive = **300** facilities (2022-01-01..2022-12-31) [DISCARD: Redundant intermediate year of the p9-p12 delivery-provider series; the 2021 and 2025 endpoints (p9, p12/p3) carry the t] quote: "분만을 시행하는 병·의원급 산부인과는 2021년 313곳에서 2022년 300곳, 2023년 282곳, 2024년 269곳, 2025년 260곳으로 감소했다."
  - p11 Number of clinic/hospital-level obstetric-gynecology facilities providing delive = **282** facilities (2023-01-01..2023-12-31) [DISCARD: Redundant intermediate year of the p9-p12 delivery-provider series.] quote: "분만을 시행하는 병·의원급 산부인과는 2021년 313곳에서 2022년 300곳, 2023년 282곳, 2024년 269곳, 2025년 260곳으로 감소했다."
  - p12 Number of clinic/hospital-level obstetric-gynecology facilities providing delive = **269** facilities (2024-01-01..2024-12-31) [keep: ] quote: "분만을 시행하는 병·의원급 산부인과는 2021년 313곳에서 2022년 300곳, 2023년 282곳, 2024년 269곳, 2025년 260곳으로 감소했다."
  - p13 Share of obstetric/gynecology clinics/hospitals providing delivery care nationwi = **19.9** % (2021-01-01..2021-12-31) [DISCARD: Share series that duplicates the level series p9-p12 divided by p1/p2; adds no independent information.] quote: "분만 시행 비율도 2021년 19.9%에서 2022년 18.9%, 2023년 18.0%, 2024년 17.1%, 지난해 16.5%까지 낮아졌다."
  - p14 Number of obstetric-gynecology clinics/hospitals in Seoul (2025) = **437** facilities (2025-01-01..2025-12-31) [keep: ] quote: "서울은 전국에서 산부인과 병·의원이 가장 많은 지역이지만, 전체 437곳 가운데 실제 분만을 시행한 병·의원은 41곳에 그쳤다."
  - p15 Number of obstetric-gynecology clinics/hospitals actually providing delivery car = **41** facilities (2025-01-01..2025-12-31) [keep: ] quote: "서울은 전국에서 산부인과 병·의원이 가장 많은 지역이지만, 전체 437곳 가운데 실제 분만을 시행한 병·의원은 41곳에 그쳤다."
- `https://www.medicaltimes.com/Main/News/NewsView.html?ID=1155719` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://v.daum.net/v/20260713120404202` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kmdarchitects.com/cha-kangnam-1` -> **snapshot** (snapshot 20250218051741); points raw/verified 11/0
- dropped by code checks: 11 (period_end missing or unparseable: 8; number: no number in value_as_written: 3)

### d7 [attention] Search and media interest

Hypothesis: Public interest in pregnancy and childbirth, as measured by search volume or media coverage, may correlate with birth numbers, but the link is weak and lagged. This can provide a qualitative check on whether July 2026 births are likely above or below trend.

Queries issued by the searcher: Naver DataLab 임신 출산 검색량 2026; Google Trends South Korea births 2026; 2026년 출산율 뉴스 출생아 수 증가 베이비붐; 출산 임신 검색어 트렌드 2026 구글 트렌드; 네이버 데이터랩 검색어 트렌드 출산 2026년 7월; Korea births July 2026 monthly population trends 24,275

- `http://files.speakerdeck.com/presentations/7f3eaa3f42f04952a681effbd75a2fae/11_%EC%A0%95%ED%98%B8%EC%8B%9D_LODAC2016_%EB%84%A4%EC%9D%B4%EB%B2%84_%EB%8` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.badak.biz/wiki/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=133986979&t=board` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://zhuanlan.zhihu.com/p/2030243292919673943` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chosun.com/english/market-money-en/2026/05/27/WL5TMGQHRFGGJJPNVF4GL2WXZU/?outputType=native` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] administrative registration flow

Hypothesis: Monthly resident-registration birth counts (주민등록 인구통계) for July 2026 are published by the Ministry of the Interior and Safety with a much shorter lag than KOSTAT's vital statistics. If available, they give a near-contemporaneous level for July 2026 that can be scaled to the KOSTAT live-birth definition, unlocking a direct level route instead of relying only on capacity or prior-year analogues.

Queries issued by the searcher: 행정안전부 주민등록 인구통계 2026년 7월 출생; 주민등록 출생자 수 월별 2026; 주민등록 출생등록 2026년 7월 전국 명 행정안전부; 행안부 주민등록 출생아 등록 7월 2026 증가

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mois.go.kr/pdf/03statistics-description.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### b2 [base_rates] historical monthly seasonality and level

Hypothesis: KOSTAT's monthly Population Trends releases for 2024 and 2025 give the actual July live-birth counts and the recent year-over-year trend. These are the correct analogue levels for a July 2026 estimate and would replace the facility-capacity proxy with an observed birth series, sharply reducing uncertainty.

Queries issued by the searcher: 통계청 인구동향 2025년 7월 출생아 수; KOSTAT monthly live births July 2025 Population Trends; 2026년 5월 인구동향 출생아 수 통계청; 통계청 인구동향 2026년 출생아 수 월별 증가

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kostat.go.kr/boardDownload.es?bid=204&list_no=439018&seq=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p16 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p17 South Korea live births year-over-year change, July 2025 vs July 2024 = **5.9** percent (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p18 South Korea deaths, July 2025 (monthly Population Trends) = **27,979** deaths (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p19 South Korea deaths year-over-year change, July 2025 vs July 2024 = **0.7** percent (2025-07-01..2025-07-31) [keep: ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p20 South Korea marriages, July 2025 (monthly Population Trends) = **20,394** marriages (cases) (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p21 South Korea marriages year-over-year change, July 2025 vs July 2024 = **8.4** percent (2025-07-01..2025-07-31) [DISCARD: Year-over-year change restating p20's level; the level is the usable quantity.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p22 South Korea divorces, July 2025 (monthly Population Trends) = **7,826** divorces (cases) (2025-07-01..2025-07-31) [keep: ] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p23 South Korea divorces year-over-year change, July 2025 vs July 2024 = **1.4** percent (2025-07-01..2025-07-31) [DISCARD: Year-over-year change restating p22's level; divorces are in any case only a weak, indirect birth indicator.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p24 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://m-fr.yna.co.kr/view/AFR20250924002400884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] marriage-to-birth lag

Hypothesis: Marriage counts in late 2025 and early 2026 are a leading indicator of first births roughly 9-15 months later, so they can anchor a July 2026 level and help resolve whether the recent uptick in marriages is translating into births. This would provide an independent check on the capacity-based route.

Queries issued by the searcher: 통계청 혼인건수 월별 2025 2026 인구동향; KOSTAT monthly marriages 2026 South Korea statistics; 혼인 후 첫 출산 간격 평균 통계 첫째아 출산까지 기간; 2025년 혼인 이혼 통계 혼인건수 2025년 연간 26만건 통계청

- `https://www.yna.co.kr/view/AKR20220110132800002` -> **snapshot** (snapshot 20240715094702); points raw/verified 15/14
  - p25 Average time from first marriage to first child birth for newlywed couples with  = **16.7** months (2020-01-01..2020-12-31) [keep: ] quote: "2020년 기준 초혼 신혼부부 중 아이가 있는 부부 52만321쌍의 첫째 자녀 출산 소요기간은 평균 16.7개월이었다."
  - p26 Average time from marriage to first child birth, 2015 cohort = **15** months (2015-01-01..2015-12-31) [DISCARD: Redundant early cohort of the p25-p30 interval series; the 2020 endpoint (p25) is the relevant vintage for extrapolation] quote: "첫 아이 출산 평균 소요기간은 2015년 15개월, 2016년 15.2개월, 2017년 15.5개월, 2018년 15.7개월, 2019년 16.1개월, 2020년 16.7개월로 점점 길어지고 있다."
  - p27 Average time from marriage to first child birth, 2016 cohort = **15.2** months (2016-01-01..2016-12-31) [DISCARD: Redundant intermediate cohort of the p25-p30 interval series.] quote: "첫 아이 출산 평균 소요기간은 2015년 15개월, 2016년 15.2개월, 2017년 15.5개월, 2018년 15.7개월, 2019년 16.1개월, 2020년 16.7개월로 점점 길어지고 있다."
  - p28 Average time from marriage to first child birth, 2017 cohort = **15.5** months (2017-01-01..2017-12-31) [DISCARD: Redundant intermediate cohort of the p25-p30 interval series.] quote: "첫 아이 출산 평균 소요기간은 2015년 15개월, 2016년 15.2개월, 2017년 15.5개월, 2018년 15.7개월, 2019년 16.1개월, 2020년 16.7개월로 점점 길어지고 있다."
  - p29 Average time from marriage to first child birth, 2018 cohort = **15.7** months (2018-01-01..2018-12-31) [DISCARD: Redundant intermediate cohort of the p25-p30 interval series.] quote: "첫 아이 출산 평균 소요기간은 2015년 15개월, 2016년 15.2개월, 2017년 15.5개월, 2018년 15.7개월, 2019년 16.1개월, 2020년 16.7개월로 점점 길어지고 있다."
  - p30 Average time from marriage to first child birth, 2019 cohort = **16.1** months (2019-01-01..2019-12-31) [DISCARD: Redundant intermediate cohort of the p25-p30 interval series.] quote: "첫 아이 출산 평균 소요기간은 2015년 15개월, 2016년 15.2개월, 2017년 15.5개월, 2018년 15.7개월, 2019년 16.1개월, 2020년 16.7개월로 점점 길어지고 있다."
  - p31 Average time from first to second child birth for newlywed couples with two or m = **23.8** months (2020-01-01..2020-12-31) [keep: ] quote: "2020년 기준 아이가 둘 이상인 초혼 신혼부부 11만637쌍이 첫째 자녀를 낳은 뒤 둘째 자녀를 낳기까지 걸린 기간은 평균 23.8개월이었다."
  - p32 Average time from first to second child birth, 2015 cohort = **24.8** months (2015-01-01..2015-12-31) [DISCARD: Redundant early cohort of the p31-p35 second-birth interval series.] quote: "첫째 출산 후 둘째 출산까지의 평균 소요기간은 2015년 24.8개월, 2016년 24.5개월, 2017년 24.1개월, 2018·2019년 24.0개월, 2020년 23.8개월로 점차 짧아지고 있다."
  - p33 Average time from first to second child birth, 2016 cohort = **24.5** months (2016-01-01..2016-12-31) [DISCARD: Redundant intermediate cohort of the p31-p35 second-birth interval series.] quote: "첫째 출산 후 둘째 출산까지의 평균 소요기간은 2015년 24.8개월, 2016년 24.5개월, 2017년 24.1개월, 2018·2019년 24.0개월, 2020년 23.8개월로 점차 짧아지고 있다."
  - p34 Average time from first to second child birth, 2017 cohort = **24.1** months (2017-01-01..2017-12-31) [DISCARD: Redundant intermediate cohort of the p31-p35 second-birth interval series.] quote: "첫째 출산 후 둘째 출산까지의 평균 소요기간은 2015년 24.8개월, 2016년 24.5개월, 2017년 24.1개월, 2018·2019년 24.0개월, 2020년 23.8개월로 점차 짧아지고 있다."
  - p35 Average time from first to second child birth, 2018 and 2019 cohorts = **24** months (2018-01-01..2019-12-31) [DISCARD: Redundant intermediate cohort of the p31-p35 second-birth interval series.] quote: "첫째 출산 후 둘째 출산까지의 평균 소요기간은 2015년 24.8개월, 2016년 24.5개월, 2017년 24.1개월, 2018·2019년 24.0개월, 2020년 23.8개월로 점차 짧아지고 있다."
  - p36 Average time from marriage to first child birth, dual-income couples, 2020 cohor = **17.2** months (2020-01-01..2020-12-31) [DISCARD: Dual-income variant of the 2020-cohort first-birth interval; the income split is not resolvable for the 2025-2026 marria] quote: "2020년 기준으로 보면 맞벌이 부부가 첫 아이를 낳는 데 걸리는 평균 기간은 17.2개월로 외벌이 부부의 16.3개월보다 길었다."
  - p37 Average time from marriage to first child birth, single-income couples, 2020 coh = **16.3** months (2020-01-01..2020-12-31) [DISCARD: Single-income variant of the same 2020-cohort interval; redundant with p25 for the purpose of a single lag parameter.] quote: "2020년 기준으로 보면 맞벌이 부부가 첫 아이를 낳는 데 걸리는 평균 기간은 17.2개월로 외벌이 부부의 16.3개월보다 길었다."
  - p38 Share of newlywed couples who had a child within 5 years of marriage among all n = **55.5** % of newlywed couples (2020-01-01..2020-12-31) [keep: ] quote: "2020년 기준 출산 소요기간 집계 대상은 결혼 5년 내 아이를 낳은 부부로, 전체 신혼부부 93만8천쌍 중 55.5%다."
- `https://zhuanlan.zhihu.com/p/2052934842367599352` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4690717` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?bid=204&mid=a10301010000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: more than one number in value_as_written: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Both count the same entity (nationwide obstetric/gynecology clinics and hospitals) in 2021 and 2025, from the same article and likely the same underlying registry; they show near-stability of the faci
- corroborating: ['p3', 'p4', 'p9', 'p10', 'p11', 'p12'] p3/p4 give the 2025 level and share of clinic/hospital-level facilities actually doing deliveries; p9-p12 give the same series for 2021-2024. They are internally consistent (260/1571 = 16.5%) and shar
- corroborating: ['p5', 'p6', 'p7', 'p8'] Broader-scope counts of all institutions providing delivery care (including tertiary/general hospitals and midwifery clinics) for 2015 and 2025, plus the implied 10-year decline. Consistent with the n
- corroborating: ['p14', 'p15'] Seoul-level counts of all ob/gyn clinics/hospitals and those actually doing deliveries; consistent with the national pattern of a small delivery-capable share, but a regional subset, not a national to
- contextual: ['p3', 'p5'] Different scopes: p3 is clinic/hospital-level delivery providers only (260), p5 adds tertiary/general hospitals and midwifery clinics (436). They are not contradictory; the gap is the hospital-tier de
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] Both count the same universe (all ob/gyn clinics and hospitals nationwide) in 2021 and 2025; the near-identical totals (1,573 vs 1,571) show the stock of ob/gyn facilities is essentially flat, so faci
- corroborating: ['p3', 'p4', 'p9', 'p10', 'p11', 'p12'] p3/p4 (260 facilities, 16.5% of 1,571) and the p9-p12 series (313→300→282→269→260) are the same measurement of clinic/hospital-level delivery providers from the same article; p3 is the 2025 endpoint o
- corroborating: ['p5', 'p6', 'p7', 'p8'] All four describe the same broader delivery-provider universe (436 in 2025 vs 620 in 2015, a 184-facility / 29.7% decline); p7 and p8 are arithmetic restatements of p5 and p6, not separate evidence.
- corroborating: ['p3', 'p5'] Different but nested scopes: 260 clinic/hospital-level providers (p3) versus 436 including tertiary and general hospitals and midwifery clinics (p5). They are consistent (p3 < p5) and together define 
- corroborating: ['p14', 'p15'] Seoul-specific pair from the same article: 437 ob/gyn facilities, only 41 doing deliveries. Consistent with the national pattern of a small delivery-active share; useful only as a geographic concentra
- corroborating: ['p20', 'p21'] Same July 2025 marriage release: 20,394 marriages and +8.4% year-over-year. The level and the change are one measurement, not two.
- corroborating: ['p22', 'p23'] Same July 2025 divorce release: 7,826 divorces and -1.4% year-over-year; one measurement.
- corroborating: ['p19', 'p20', 'p22'] All three come from the same KOSTAT July 2025 Population Trends release (published 2025-09-24), so they share a source and vintage; they establish the release cadence and the July-2025 marriage level 
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p30'] One consistent cohort series of mean marriage-to-first-birth intervals (15.0→16.7 months, 2015→2020 cohorts) from a single 2022 release; the trend is monotone and slow, so extrapolation to 2025-2026 m
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35'] One consistent cohort series of first-to-second-birth intervals (24.8→23.8 months); same source and vintage as p25-p30.
- corroborating: ['p36', 'p37'] Dual-income (17.2 months) vs single-income (16.3 months) first-birth intervals for the 2020 cohort; same release, and the gap is small relative to the overall spread.
- corroborating: ['p25', 'p38'] Both from the same 2020-cohort newlywed analysis: p25 gives the mean interval for couples with children, p38 shows only 55.5% of newlywed couples had a child within 5 years. Together they warn that ma
- contextual: ['p25', 'p31'] First-birth lag (~16.7 months) and second-birth lag (~23.8 months) are different parity transitions; they cannot be averaged into a single marriage-to-birth lag without a parity mix, which no kept poi

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Live births per delivery-active clinic/hospital-level ob/gyn facility per month, South Korea, July 2026 | 55 | 30..100 | 30..100 | live births per facility per month | m1 (m1) | No kept point gives a births-per-facility throughput. The value is anchored on the scale implied by the capacity envelope: 260 clinic/hospital-level delivery providers (p3) and 436 total delivery institutions (p5) must jointly accommodate a national monthly birth flow that has been in the low tens o | The 2025 facility stock (p3, p5) is still representative of July 2026 capacity and utilisation, and the delivery-active facility mix has not shifted materially in the intervening year. | Evidence that the number of delivery-active facilities changed sharply in 2026, or any observed monthly birth count for 2025-2026 that implies a births-per-facility throughput far outside 30-100. |
| a2 | Ratio of July 2026 live births to July 2025 live births, South Korea | 1.03 | 0.95..1.12 | 0.7294..1.459 (widened) | ratio | unused | The only kept evidence on the recent direction of births is indirect: marriages in July 2025 were 20,394, up 8.4% year-over-year (p20), and the marriage-to-first-birth lag is about 16-17 months (p25), so the late-2024/2025 marriage recovery should begin feeding into births around mid-2026. However,  | The July 2025 KOSTAT live-birth level is available as the base period and the marriage-to-birth transmission observed in p20/p25/p38 is the dominant driver of the 2025-to-2026 change. | A published July 2026 birth count, or 2026 monthly birth data, showing a change outside the 0.95-1.12 band, or evidence that the 2025 marriage increase did not translate into first births. |

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['korea']; quantity stems: ['birth', 'live', 'perso']
- points excluded before the judge: 4 of 38
- methods allowed: ['formula_mc']

  - p16 South Korea live births, July 2025 (monthly Population Trends) = 21,803 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p17 South Korea live births year-over-year change, July 2025 vs July 2024 = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p18 South Korea deaths, July 2025 (monthly Population Trends) = 27,979 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p24 South Korea natural increase (live births minus deaths), July 2025 = -6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 14,229 | ['p3'] / ['a1'] | [] |  | 1.00 | equal |  |

Result: central **14,229**, 80% interval [7,568, 26,756], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first reported by Statistics Korea's Monthly Population Trends, is 14,229 (80% interval 7,568 to 26,756, monte carlo). The estimate rests on 14 observed point and 1 method, weighted 100%. The only observed input is the stock of delivery-active clinic/hospital-level ob/gyn facilities; the births-per-facility throughput of 55 (range 30 to 100) is an analyst assumption, not observed. This route deliberately excludes tertiary and midwifery institutions, so it is a lower-tier capacity estimate rather than a full national count. The interval is model-based and conditional on that assumption, not a demonstrated accuracy guarantee. The result could be wrong mainly because the throughput assumption is unanchored and facility counts may not map cleanly to monthly birth flow. The missing evidence that would most improve it is an observed births-per-facility throughput series or a directly reported monthly birth count.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Live births per delivery-active clinic/hospital-level ob/gyn facility per month, South Korea, July 2026: 55 live births per facility per month, range 30 to 100; used by m1. Overturned by: Evidence that the number of delivery-active facilities changed sharply in 2026, or any observed monthly birth count for 2025-2026 that implies a births-per-facility throughput far outside [n]-[n].

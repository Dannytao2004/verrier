# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first published in Statistics Korea's monthly Population Trends (인구동향) release | unit live births | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), monthly Population Trends / 인구동향

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly series

Hypothesis: July 2026 births follow the recent level and seasonal pattern of monthly births; July is typically a high-birth month relative to June. Recent monthly values (2024-2026) plus a July seasonal factor give a baseline.

Queries issued by the searcher: 통계청 인구동향 2026년 6월 출생아 수; Statistics Korea monthly live births 2026 population trends June; 2026년 5월 인구동향 출생아 수 전년동월대비 증가; 2025년 7월 출생아 수 인구동향 2만명; "7월" 출생아 수 2025년 7월 인구동향 2만2천명 전년동월대비 증가

- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446612&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4840361?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646700` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Resident registration births

Hypothesis: Administrative resident-registration birth counts (주민등록 출생) track statistical live births closely and are published with a shorter lag, providing a near-contemporaneous proxy for July 2026.

Queries issued by the searcher: 주민등록 출생자 수 2026년 7월; 행정안전부 주민등록 인구통계 월별 출생자 수 2026; 2026년 7월 주민등록 인구통계 출생자 24761 증가; 주민등록 출생자 수 통계청 출생아 수 차이 비율 발생일 신고일

- `https://mlbpark.donga.com/mp/b.php?p=1&b=bullpen&id=202608030117768000&select=&query=%EC%A0%84%EC%9E%A5%EC%97%B0&shop=&subselect=&subquery=&user=&site` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Year-to-date and annual totals

Hypothesis: YTD births through mid-2026 plus a July share of the annual total (from prior years) yields July 2026; annual total times July share is an alternative route.

Queries issued by the searcher: 2026년 상반기 출생아 수 통계청 인구동향; 2025년 연간 출생아 수 통계청 인구동향; 2025년 7월 출생아 수 명 통계청 인구동향 7월; 월별 출생아 수 2015 2016 2017 7월 비중 연간 출생아 수 표

- `https://www.yna.co.kr/view/AKR20260826079400002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ajunews.com/view/20260225104108429` -> **snapshot** (snapshot 20260411112229); points raw/verified 15/15
  - p1 South Korea total live births, 2025 (annual) = **254,500** live births (2025-01-01..2025-12-31) [keep: ] quote: "지난해 출생아 수는 25만4500명으로 전년보다 1만6100명(6.8%) 증가했다."
  - p2 South Korea year-on-year change in live births, 2025 vs 2024 = **16,100** live births (2025-01-01..2025-12-31) [keep: ] quote: "지난해 출생아 수는 25만4500명으로 전년보다 1만6100명(6.8%) 증가했다."
  - p3 South Korea year-on-year growth rate of live births, 2025 vs 2024 = **6.8** % (2025-01-01..2025-12-31) [keep: ] quote: "지난해 출생아 수는 25만4500명으로 전년보다 1만6100명(6.8%) 증가했다."
  - p4 South Korea total fertility rate, 2025 = **0.8** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "합계출산율은 지난해 0.80명으로 전년 대비 0.05명 증가했다."
  - p5 South Korea total fertility rate, 2024 = **0.75** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "2024년(0.75명) 반등에 성공한 이후 지난해 상승 폭을 키웠다."
  - p6 South Korea share of annual live births occurring in July, 2025 = **8.6** % (2025-07-01..2025-07-31) [keep: ] quote: "지난해 월별 출생아 수 비중은 1월 (9.5%), 9월(8.8%), 7월·10월(8.6%) 등이 높았고"
  - p7 South Korea share of annual live births occurring in October, 2025 = **8.6** % (2025-10-01..2025-10-31) [keep: ] quote: "지난해 월별 출생아 수 비중은 1월 (9.5%), 9월(8.8%), 7월·10월(8.6%) 등이 높았고"
  - p8 South Korea share of annual live births occurring in January, 2025 = **9.5** % (2025-01-01..2025-01-31) [keep: ] quote: "지난해 월별 출생아 수 비중은 1월 (9.5%), 9월(8.8%), 7월·10월(8.6%) 등이 높았고"
  - p9 South Korea share of annual live births occurring in September, 2025 = **8.8** % (2025-09-01..2025-09-30) [keep: ] quote: "지난해 월별 출생아 수 비중은 1월 (9.5%), 9월(8.8%), 7월·10월(8.6%) 등이 높았고"
  - p10 South Korea share of annual live births occurring in February, June and December = **7.9** % (2025-01-01..2025-12-31) [keep: ] quote: "2월·6월·12월(7.9%) 등이 낮았다."
  - p11 South Korea first-child live births, 2025 = **158,700** live births (2025-01-01..2025-12-31) [keep: Kept as context on birth-order mix; not used numerically because it does not reconcile exactly with p1.] quote: "지난해 첫째 아이는 15만8700명으로 전년보다 1만2600명 증가했고"
  - p12 South Korea second-child live births, 2025 = **79,300** live births (2025-01-01..2025-12-31) [keep: Kept as context; same caveat as p11.] quote: "둘째 아이는 7만9300명으로 전년 대비 3400명 늘었다."
  - p13 South Korea share of first-child births among live births, 2025 = **62.4** % (2025-01-01..2025-12-31) [keep: Kept as context on parity mix.] quote: "첫째 아이와 둘째 아이의 비중은 각각 62.4%, 31.2%를 기록했다."
  - p14 South Korea share of second-child births among live births, 2025 = **31.2** % (2025-01-01..2025-12-31) [keep: Kept as context on parity mix.] quote: "첫째 아이와 둘째 아이의 비중은 각각 62.4%, 31.2%를 기록했다."
  - p15 South Korea year-on-year increase in January live births, 2025 = **12.5** % (2025-01-01..2025-01-31) [keep: ] quote: "전년 동월 대비 출생아수는 1월(12.5%), 6월(9.7%) 순으로 많이 증가했다."
- `https://www.edaily.co.kr/News/Read?newsId=04818326645551256` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8366129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [base_rates] Demographic accounting

Hypothesis: Births = women of childbearing age × age-specific fertility rates; monthly births can be built from the female population by age and recent TFR/ASFR, adjusted for seasonality.

Queries issued by the searcher: 통계청 인구동향 2026년 6월 출생아 수; South Korea monthly live births 2025 Statistics Korea population trends; 2026년 5월 인구동향 출생아 수 국가데이터처 발표; 2026년 4월 인구동향 출생아 수 전년동월대비 증가; 통계청 장래인구추계 2026년 여자 인구 30-34세 명; 월별 출생아 수 2023 2024 2025 통계청 1월 2월 3월 4월 5월 6월 7월 8월 9월 10월 11월 12월

- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446612&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4840361?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646700` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Policy and calendar effects

Hypothesis: Recent policy expansions (parental leave, birth grants, marriage incentives) and calendar effects (Lunar New Year timing, marriage cohort shifts) alter the level and month-to-month path of births in 2026.

Queries issued by the searcher: Korea monthly live births 2026 Statistics Korea population trends; 혼인건수 2025 통계청 출생아 수 증가; 2026년 6월 인구동향 출생아 수; "2026년 6월 인구동향" 출생아 혼인

- `https://amp.seoul.co.kr/news/economy/2026/07/29/20260729500210` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=297012` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bizn.donga.com/news/article/all/20260128/133251886/3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.koreaherald.com/article/10703360` -> **snapshot** (snapshot 20260327055001); points raw/verified 15/9
  - p16 Total fertility rate in South Korea, 2023 (record low) = **0.72** births per woman (2023-01-01..2023-12-31) [keep: ] quote: "the figure has been gradually recovering from a record low of 0.72 in 2023 to 0.75 in 2024, with a provisional estimate of 0.8 for 2025."
  - p17 Total fertility rate in South Korea, 2024 = **0.75** births per woman (2024-01-01..2024-12-31) [DISCARD: Duplicate of p5 (2024 TFR 0.75); same figure from a second outlet.] quote: "the figure has been gradually recovering from a record low of 0.72 in 2023 to 0.75 in 2024, with a provisional estimate of 0.8 for 2025."
  - p18 Total fertility rate in South Korea, 2025 (provisional estimate) = **0.8** births per woman (2025-01-01..2025-12-31) [DISCARD: Duplicate of p4 (2025 TFR 0.80 provisional); same figure from a second outlet.] quote: "the figure has been gradually recovering from a record low of 0.72 in 2023 to 0.75 in 2024, with a provisional estimate of 0.8 for 2025."
  - p19 Annual marriages in South Korea, 2019 = **239,000** marriages (2019-01-01..2019-12-31) [keep: ] quote: "Annual marriages fell from 239,000 in 2019 to 191,000 in 2022, before recovering to around 240,000 last year."
  - p20 Annual marriages in South Korea, 2022 = **191,000** marriages (2022-01-01..2022-12-31) [keep: ] quote: "Annual marriages fell from 239,000 in 2019 to 191,000 in 2022, before recovering to around 240,000 last year."
  - p21 Annual marriages in South Korea, last year (2025) = **240,000** marriages (2025-01-01..2025-12-31) [keep: ] quote: "Annual marriages fell from 239,000 in 2019 to 191,000 in 2022, before recovering to around 240,000 last year."
  - p22 Population of South Korea at peak, 2019 = **51,840,000** persons (2019-01-01..2019-12-31) [keep: Context only; population level is not a birth-count input.] quote: "Korea's population has been shrinking since peaking at 51.84 million in 2019, with monthly decreases continuing since November that year."
  - p23 Population decline in South Korea, January last year (2025) = **15,306** persons (2025-01-01..2025-01-31) [keep: Context only; monthly population decline is not a birth-count input.] quote: "including 12,533 in December, 9,998 in November and 7,848 in October, as well as 15,306 in January last year."
  - p24 Share of population aged 65 or older in South Korea, 2025 = **21.2** % (2025-01-01..2025-12-31) [keep: Context only; ageing share does not enter a monthly birth estimate.] quote: "Korea is also rapidly aging, with 21.2 percent of its population aged 65 or older in 2025, officially classifying it as a super-aged society under United Nations standards."
- dropped by code checks: 6 (period year 2026 does not appear in the page text or URL (likely mis-dated): 5; period_end 2026-12-31 after as_of: 1)

### d6 [forecasts_markets] Official and analyst projections

Hypothesis: KOSTAT or research institutes may publish 2026 monthly or quarterly birth projections or nowcasts that constrain July 2026.

Queries issued by the searcher: 2026년 출생아 수 전망 통계청; Korea 2026 birth forecast monthly projections; 2025년 7월 출생아 수 인구동향 통계청; 2026년 5월 인구동향 출생아 수 발표 국가데이터처

- `https://m.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260802035341); points raw/verified 15/0
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.sedaily.com/article/20035151` -> **snapshot** (snapshot 20260521080409); points raw/verified 14/9
  - p25 Pregnant women registered at public health centers, April 2025–March 2026 (leadi = **351,000** pregnant women (2025-04-01..2026-03-31) [keep: ] quote: "지난해 4월부터 올해 3월까지 보건소에 임신 신고를 한 임산부 수가 35만 1000명으로 집계됐다."
  - p26 Year-on-year increase in registered pregnant women (April–March) = **16** % (2025-04-01..2026-03-31) [keep: ] quote: "이 기간 임산부 수는 전년 30만 명 대비 16%가량 증가해"
  - p27 Share of pregnancies not resulting in live birth (conversion loss rate) = **12.5** (range 10..15) as written "10~15%", value check pending % (not stated (page dated 2026-04-21)) [keep: ] quote: "통상 임신 이후 출산까지 이어지지 못하는 비율이 10~15% 수준이라는 점을 고려하면"
  - p28 Q1 2026 birth registrations (Ministry of the Interior and Safety) = **73,742** birth registrations (2026-01-01..2026-03-31) [keep: ] quote: "올해 1분기 행정안전부의 출생 등록 건수는 7만 3742건으로 전년 동기 대비 약 15% 증가하며"
  - p29 Year-on-year increase in Q1 2026 birth registrations = **15** % (2026-01-01..2026-03-31) [keep: ] quote: "출생 등록 건수는 7만 3742건으로 전년 동기 대비 약 15% 증가하며 역대 최대 증가 폭을 기록했다."
  - p30 Typical discrepancy between birth registrations and official live births = **2** % (not stated (page dated 2026-04-21)) [keep: ] quote: "출생 등록 건수는 국가데이터처가 집계하는 공식 출생아 수와 완전히 일치하지는 않지만 통상 2% 내외 오차 범위에서 비슷한 흐름을 보인다."
  - p31 January 2026 live births (official, National Data Office) = **26,916** live births (2026-01-01..2026-01-31) [keep: ] quote: "데이터처가 집계한 올해 1월 출생아 수 역시 2만 6916명으로 전년 동월 대비 11.7% 증가하는 등"
  - p32 Year-on-year increase in January 2026 live births = **11.7** % (2026-01-01..2026-01-31) [keep: ] quote: "올해 1월 출생아 수 역시 2만 6916명으로 전년 동월 대비 11.7% 증가하는 등 유사한 흐름이 이어지고 있다."
  - p33 Total fertility rate recovery target level mentioned = **1** births per woman (not stated (page dated 2026-04-21)) [DISCARD: A policy target (TFR 1.0 recovery timing), not an observation of 2026 births; unusable as a numeric input.] quote: "새로운 추계에서는 합계출산율 1.0 회복 시점 역시 기존 예상보다 빨라질 가능성이 제기된다."
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=AKR20251231132800002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 20 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 7; period year 2025 does not appear in the page text or URL (likely mis-dated): 6; period_end 2035-12-31 after as_of: 1)

### b1 [related_series] administrative near-contemporaneous proxy

Hypothesis: Monthly resident-registration birth counts (행정안전부 주민등록 출생) for April–June 2026 would extend the p28/p29 Q1 signal to the months immediately preceding July, letting us scale July 2025 births by an observed 2026 yoy factor rather than an assumed one. This is the single largest uncertainty in the estimate.

Queries issued by the searcher: 행정안전부 주민등록 인구통계 월별 출생 2026; 통계청 인구동향 2026년 5월 출생아 수; 주민등록 출생자 수 2026년 5월 행안부 출생등록 전년동월 대비; 2025년 7월 출생아 수 21,854명 인구동향

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://korea.nabo.go.kr/board/file/down.do?fid=33319286` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mlbpark.donga.com/mp/b.php?p=1&b=bullpen&id=202605010114652335&select=&query=%EB%B0%95%EB%AC%B8%EC%84%B1&subselect=&subquery=&user=&site=donga` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1472&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] seasonality

Hypothesis: July shares of annual births for 2022–2024 would test whether the 8.6% July share (p6) is stable or a 2025 idiosyncrasy; a stable share supports the annual-total × share route (m2) and narrows its uncertainty.

Queries issued by the searcher: 통계청 인구동향 월별 출생아 수 2022 2023 2024 7월; Statistics Korea monthly live births 2024 July births monthly trend; 2025년 12월 인구동향 출생아 수 연간 2025년 출생아 25만명 통계청; KOSIS 월별 출생아 수 2022년 1월부터 12월 2023년 월별 출생아수 표

- `https://sri.kostat.go.kr/boardDownload.es?bid=204&list_no=435204&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n.news.naver.com/article/008/0005093449?type=journalists` -> **snapshot** (snapshot 20240927025747); points raw/verified 15/13
  - p34 Live births in South Korea, July 2024 = **20,601** live births (2024-07-01..2024-07-31) [keep: ] quote: "7월 출생아 수는 2만601명으로 전년 동월 대비 7.9%(1516명) 증가했다."
  - p35 Live births in South Korea, July 2022 = **20,475** live births (2022-07-01..2022-07-31) [keep: ] quote: "특히 2022년 2만475명에서 지난해 1만9085명까지 떨어졌던 7월 출생아 수는 올해 다시 2만명대를 회복했다."
  - p36 Year-on-year change in July 2024 live births (percent) = **7.9** % (2024-07-01..2024-07-31) [keep: ] quote: "7월 출생아 수는 2만601명으로 전년 동월 대비 7.9%(1516명) 증가했다."
  - p37 Year-on-year change in July 2024 live births (count) = **1,516** live births (2024-07-01..2024-07-31) [keep: ] quote: "7월 출생아 수는 2만601명으로 전년 동월 대비 7.9%(1516명) 증가했다."
  - p38 Cumulative live births January–July 2024, South Korea = **137,913** live births (2024-01-01..2024-07-31) [keep: ] quote: "올해 7월 누적 출생아 수는 13만7913명으로 1년 전(13만9635명)보다 1.2% 감소한 수준이다."
  - p39 Year-on-year change in cumulative January–July 2024 live births (percent) = **1.2** % (2024-01-01..2024-07-31) [keep: ] quote: "올해 7월 누적 출생아 수는 13만7913명으로 1년 전(13만9635명)보다 1.2% 감소한 수준이다."
  - p40 Crude birth rate (births per 1,000 population), July 2024, South Korea = **4.8** births per 1,000 population (2024-07-01..2024-07-31) [keep: ] quote: "'조(粗) 출생률'도 4.8명으로 전년 동월 대비 0.4명 늘었다."
  - p41 Year-on-year change in crude birth rate, July 2024 (births per 1,000 population) = **0.4** births per 1,000 population (2024-07-01..2024-07-31) [keep: ] quote: "'조(粗) 출생률'도 4.8명으로 전년 동월 대비 0.4명 늘었다."
  - p42 Deaths in South Korea, July 2024 = **28,240** deaths (2024-07-01..2024-07-31) [keep: ] quote: "7월 사망자 수는 2만8240명으로 전년 동월 대비 0.4%(99명) 늘었다."
  - p43 Natural population change (births minus deaths), July 2024, South Korea = **7,639** persons (decrease) (2024-07-01..2024-07-31) [keep: ] quote: "7월 인구 자연증가(출생아 수 - 사망자 수)는 7639명 감소했다."
  - p44 Cumulative natural population decrease January–July 2024, South Korea = **68,100** persons (2024-01-01..2024-07-31) [keep: ] quote: "올해 들어 7월까지 누적 6만8100명의 인구가 줄었다."
  - p45 Marriages in South Korea, July 2024 = **18,811** marriages (2024-07-01..2024-07-31) [keep: ] quote: "7월 혼인 건수는 1만8811건으로 전년 동월 대비 32.9%(4658건) 증가했다."
  - p46 Divorces in South Korea, July 2024 = **7,939** divorces (2024-07-01..2024-07-31) [keep: ] quote: "7월 이혼 건수는 7939건으로 1년 전보다 5.9%(442건) 증가했다."
- `https://www.joongang.co.kr/article/25280007` -> **snapshot** (snapshot 20260714191100); points raw/verified 15/13
  - p47 Live births in South Korea, July 2024 (monthly) = **20,601** live births (2024-07-01..2024-07-31) [DISCARD: Duplicate of p34 (same July 2024 value 20,601 from the same KOSTAT release, different URL/vintage); adds no information.] quote: "지난 7월 출생아 수가 2만601명으로 전년 동월 대비 7.9% 증가했다."
  - p48 Year-on-year change in July live births, South Korea, July 2024 = **7.9** % (2024-07-01..2024-07-31) [DISCARD: Duplicate of p36 (July 2024 +7.9% yoy, same release).] quote: "지난 7월 출생아 수가 2만601명으로 전년 동월 대비 7.9% 증가했다."
  - p49 Live births in South Korea, April 2024 (monthly) = **19,049** live births (2024-04-01..2024-04-30) [keep: ] quote: "월간 출생아 수는 4월(1만9049명) 전년 동월 대비 2.8% 증가하고"
  - p50 Live births in South Korea, May 2024 (monthly) = **19,547** live births (2024-05-01..2024-05-31) [keep: ] quote: "5월(1만9547명) 2.7% 늘며"
  - p51 Live births in South Korea, June 2024 (monthly) = **18,242** live births (2024-06-01..2024-06-30) [keep: ] quote: "6월(1만8242명)엔 1.8% 감소하며"
  - p52 Live births in South Korea, Q2 2024 (quarterly) = **56,838** live births (2024-04-01..2024-06-30) [keep: ] quote: "지난 2분기 출생아 수(5만6838명)가 전년 동기보다 1.2% 증가하며"
  - p53 Year-on-year change in Q2 live births, South Korea, Q2 2024 = **1.2** % (2024-04-01..2024-06-30) [keep: ] quote: "지난 2분기 출생아 수(5만6838명)가 전년 동기보다 1.2% 증가하며 34개 분기 만에 플러스로 전환한 바 있다."
  - p54 Number of mothers applying for pregnancy voucher with expected delivery in 2024  = **287,000** mothers (2024-01-01..2024-12-31) [keep: ] quote: "올해 1~12월 분만 예정인 것으로 표시하며 임신 바우처사업을 신청한 산모 수는 28만7000명으로"
  - p55 Year-on-year change in pregnancy voucher applicants, 2024 vs 2023 = **3** % (2024-01-01..2024-12-31) [keep: ] quote: "전년(27만9000명)보다 3%가량 늘었다."
  - p56 Total fertility rate, South Korea, 2024 (Statistics Korea projection, upper end) = **0.7** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "올해 합계출산율(한 여자가 가임기간에 낳을 것으로 기대되는 평균 출생아 수)은 당초 예상했던 0.68명에서 0.70명 선까지 올라갈 수도 있다고 통계청은 관측한다."
  - p57 Total fertility rate, South Korea, 2024 (initial expectation, lower end) = **0.68** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "올해 합계출산율(한 여자가 가임기간에 낳을 것으로 기대되는 평균 출생아 수)은 당초 예상했던 0.68명에서 0.70명 선까지 올라갈 수도 있다고 통계청은 관측한다."
  - p58 Marriages in South Korea, July 2024 (monthly) = **18,811** marriages (2024-07-01..2024-07-31) [DISCARD: Duplicate of p45 (July 2024 marriages 18,811, same release).] quote: "지난 7월 혼인 건수는 1만8811명으로 전년 동월 대비 32.9% 늘어났다."
  - p59 Year-on-year change in July marriages, South Korea, July 2024 = **32.9** % (2024-07-01..2024-07-31) [DISCARD: Duplicate of p45's implied +32.9% (same release).] quote: "지난 7월 혼인 건수는 1만8811명으로 전년 동월 대비 32.9% 늘어났다."
- `https://slv.news.einfomax.co.kr/news/articleView.html?idxno=4400319` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period year 2023 does not appear in the page text or URL (likely mis-dated): 4)

### b3 [forecasts_markets] official nowcast

Hypothesis: KOSTAT or research institutes may have published a 2026 monthly/quarterly birth nowcast or projection that directly constrains July 2026, resolving the level disagreement between a +10% and a +15% yoy assumption.

Queries issued by the searcher: 2026년 출생아 수 전망 월별; KOSTAT 2026 birth nowcast monthly population trends; 2025년 7월 출생아 수 인구동향 전년동월; 주민등록 출생아 수 2026년 7월 행정안전부; 한국보건사회연구원 2026년 출생아 수 전망 하반기

- `https://www.betterfuture.go.kr/cmm/fms/FileDown.do;jsessionid=FDF2D324337E2F462BA7E3A402BC7AC8.node10?atchFileId=FILE_000000000013658&fileSn=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2610060?trc=m_main_top_sub` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=04877366645519440` -> **snapshot** (snapshot 20260809115657); points raw/verified 11/4
  - p60 February daily average live births deviation from annual average (seasonality, K = **19.6** % (not stated (page dated 2026-07-29)) [keep: ] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p61 June daily average live births deviation from annual average (seasonality) = **-8.4** % (not stated (page dated 2026-07-29)) [keep: ] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p62 December daily average live births deviation from annual average (seasonality) = **-8.9** % (not stated (page dated 2026-07-29)) [keep: ] quote: "하루 평균 출생아 수 기준으로 2월은 연평균보다 19.6% 많은 반면, 6월(-8.4%)과 12월(-8.9%)은 최저점을 찍는다."
  - p63 Gap between highest and lowest month in daily average live births (seasonality) = **28.5** % (not stated (page dated 2026-07-29)) [keep: ] quote: "가장 많은 달과 적은 달의 격차는 28.5%에 달한다."
- `https://v.daum.net/v/20260802121104585` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (period year 2026 does not appear in the page text or URL (likely mis-dated): 7)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth rate', 'korea population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] Same article, same underlying KOSTAT annual release: 2025 births 254,500, +16,100 (+6.8%) vs 2024. Internally consistent (254,500 - 16,100 = 238,400 for 2024). One measurement, not three independent c
- corroborating: ['p4', 'p5', 'p16', 'p17', 'p18'] TFR path 0.72 (2023) -> 0.75 (2024) -> 0.80 (2025 provisional) is reported identically by two outlets drawing on the same KOSTAT figures; corroboration of the fertility-recovery narrative, not indepen
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10'] Monthly shares of 2025 births from one article: Jan 9.5%, Sep 8.8%, Jul/Oct 8.6%, Feb/Jun/Dec 7.9%. These are shares of the same annual total, so they are mutually consistent by construction and must 
- corroborating: ['p11', 'p12', 'p13', 'p14'] Birth-order split: 158,700 first + 79,300 second = 238,000, i.e. 62.4% + 31.2% = 93.6% with 6.4% third-or-later. Consistent with p1's 254,500 total only approximately (238,000/254,500 = 93.5%), so the
- corroborating: ['p28', 'p29', 'p31', 'p32'] Q1 2026 resident-registration births 73,742 (+15% yoy) and January 2026 official births 26,916 (+11.7% yoy) point the same way: a strong early-2026 upswing. Different definitions (registration vs occu
- corroborating: ['p25', 'p26', 'p27'] Registered pregnancies Apr 2025–Mar 2026 = 351,000, +16% yoy, with a 10–15% non-live-birth loss rate. This is a leading indicator for births roughly Jul 2025–Jun 2026, i.e. it covers the target month 
- corroborating: ['p19', 'p20', 'p21'] Marriages 239,000 (2019) -> 191,000 (2022) -> ~240,000 (2025). The 2023–2025 marriage rebound is the demographic driver behind the 2025–2026 birth increase; consistent with p1/p2 and p25/p26.
- corroborating: ['p22', 'p23', 'p24'] Population decline and ageing context; consistent with low but rising fertility. Not numerically usable for a monthly birth count.
- corroborating: ['p1', 'p6'] p1 (annual 2025 total) and p6 (July share of 2025) combine to give July 2025 births ≈ 254,500 × 8.6% ≈ 21,900; this is the natural base for a yoy-scaled July 2026 estimate.
- needs reconciliation: ['p31', 'p1'] January 2026 = 26,916 (+11.7%) implies January 2025 ≈ 24,100, which is 9.5% of 254,500 ≈ 24,180 — consistent. So the 2026 uplift is real and roughly +10–15% yoy in the months observed; July 2026 shoul
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] Same article: 2025 annual births 254,500, +16,100 (+6.8%) vs 2024. Internally consistent; single source (ajunews), so not independent confirmation.
- corroborating: ['p4', 'p5', 'p16', 'p17', 'p18'] TFR path 0.72 (2023) → 0.75 (2024) → 0.80 (2025 provisional) appears in both Korea Herald and ajunews; same underlying KOSTAT figures, so agreement is not independent.
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10'] Monthly shares of 2025 births from one article: Jan 9.5%, Sep 8.8%, Jul/Oct 8.6%, Feb/Jun/Dec 7.9%. Consistent set; July share is the key input for the annual-total × share route.
- corroborating: ['p34', 'p36', 'p37', 'p47', 'p48'] July 2024 = 20,601 births, +7.9% (+1,516) reported identically by Naver/2024 snapshot and JoongAng/2026 snapshot; same KOSTAT release, duplicate vintage.
- corroborating: ['p35', 'p34'] July 2022 = 20,475; July 2023 = 19,085 implied by p35; July 2024 = 20,601. Consistent July history showing a dip then recovery.
- corroborating: ['p38', 'p39', 'p34'] Jan–Jul 2024 cumulative 137,913 (−1.2% yoy) is consistent with July 2024 20,601 and the monthly path; same release.
- corroborating: ['p28', 'p29', 'p31', 'p32'] Q1 2026 registration +15% and January 2026 official births 26,916 (+11.7%) point to a strong early-2026 upturn; different measures (registration vs occurrence) but same direction.
- corroborating: ['p25', 'p26', 'p27'] Registered pregnancies Apr 2025–Mar 2026 = 351,000, +16% yoy, with 10–15% non-live-birth loss; a leading indicator consistent with a 2026 birth increase, but registration coverage is partial.
- corroborating: ['p28', 'p30', 'p31'] Registration counts and official births differ by ~2% typically; supports using registration as a proxy with a small conversion allowance, not as an exact substitute.
- corroborating: ['p60', 'p61', 'p62', 'p63'] Seasonality: Feb +19.6%, Jun −8.4%, Dec −8.9% vs annual daily average, range 28.5%. July is not given directly but is known to be a high month (p6); usable only as a qualitative/seasonal cross-check.
- corroborating: ['p19', 'p20', 'p21'] Marriages fell 239k (2019) → 191k (2022) → ~240k (2025); the 2023–2025 marriage recovery supports the 2026 birth upturn with a lag.
- corroborating: ['p49', 'p50', 'p51', 'p52', 'p53'] 2024 monthly Apr–Jun and Q2 56,838 (+1.2%) are internally consistent with the July 2024 figure and the 2024 recovery.
- corroborating: ['p54', 'p55'] Pregnancy-voucher applicants for 2024 deliveries 287,000 (+3%) is a partial-coverage leading indicator; consistent with modest 2024 growth.
- corroborating: ['p56', 'p57'] KOSTAT 2024 TFR expectation 0.68–0.70 vs realised 0.75 shows forecasts understated the recovery; cautions against anchoring on conservative projections.
- corroborating: ['p11', 'p12', 'p13', 'p14'] 2025 first-child 158,700 (62.4%) and second-child 79,300 (31.2%) are consistent with the 254,500 total; composition context only.
- corroborating: ['p22', 'p23', 'p24'] Population peak 51.84M (2019), ongoing monthly decline, 21.2% aged 65+ in 2025; context for the shrinking reproductive-age base, not a direct birth input.
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p58', 'p59'] July 2024 crude birth rate 4.8, deaths 28,240, natural decrease 7,639, marriages 18,811 (+32.9%), divorces 7,939 — all from the same July 2024 release; consistent but not independent of p34.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 yoy change factor in live births relative to July 2025 | 1.1 | 1.02..1.2 | 0.9895..1.237 (widened) | ratio | unused | 2026 opened strong: January 2026 official births +11.7% yoy (p32) and Q1 2026 registrations +15% (p29); 2025 as a whole was +6.8% (p3). July 2025 is not directly observed, so a yoy factor is required. Centred near +10%, below the January surge because January benefited from Lunar New Year timing and | July 2026 births track the early-2026 upturn with some moderation; used to scale the July 2025 level. | Evidence that the 2026 upturn faded by mid-year (e.g. Q2 2026 registrations near flat) or that July 2025 was an unusually high base. |
| a2 | 2026 annual live births as a multiple of 2025 annual live births | 1.05 | 1.01..1.1 | 0.7453..1.491 (widened) | ratio | unused | 2025 was 254,500 (p1); early-2026 growth of ~+11.7% (p32) suggests a further rise, tempered because January is seasonally strong and the upturn may fade. Centred ~+5% over 2025, range +1% to +10%. | 2026 annual births continue the 2025 recovery at a moderate pace. | Mid-2026 monthly data showing births flat or declining versus 2025. |
| a3 | Two-year yoy change factor from July 2024 to July 2026 | 1.12 | 1..1.28 | 1..1.28 | ratio | m1 (m3) | July 2025 is not directly observed; July 2024 = 20,601 (p34). 2025 annual births rose +6.8% (p3) and 2026 early months rose ~+11.7% (p32), so cumulative two-year growth from July 2024 to July 2026 is plausibly ~+12%, with a wide range. | July births grew roughly in line with the annual 2025 and early-2026 trends. | Evidence that July 2025 was unusually high or low relative to the 2025 annual trend. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 23,306 | ['p34'] / ['a3'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **23,306** person, 80% interval [16,917, 32,108] person, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first reported in Statistics Korea's monthly Population Trends release, is 23,306 person (80% model-based interval 16,917 to 32,108 person).

The estimate rests on one observed anchor: July 2024 live births of 20,601 live births. That level is bridged to July 2026 using an assumed two-year growth factor of 1.12 (range 1 to 1.28), which is an analyst assumption, not an observation. The rationale is that 2025 annual births and early-2026 months showed gains, so cumulative two-year growth is plausibly around that factor. The single method (1 method, weight 100%) carries the full estimate; no backtest error was available, so the interval is conditional on the assumption rather than empirically calibrated.

The main risk is the bridge factor: July 2025 is unobserved, and if the recent growth trend decelerates or reverses, the true count could fall well outside the range. The most useful missing evidence would be the actual July 2025 monthly figure, which would replace the assumed two-year factor with a directly observed one-year change.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a3 Two-year yoy change factor from July 2024 to July 2026: 1.12 ratio, range 1 to 1.28; used by m1. Overturned by: Evidence that July 2025 was unusually high or low relative to the 2025 annual trend.

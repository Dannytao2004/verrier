# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first published in Statistics Korea's monthly Population Trends (인구동향) release | unit live births | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), monthly Population Trends / 인구동향

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly series

Hypothesis: July 2026 births follow the recent monthly level and seasonal pattern of July births; the most recent published months (through ~May/June 2026) anchor the level and July seasonal factor adjusts it.

Queries issued by the searcher: Statistics Korea monthly live births 2026 인구동향 출생아 수; 출생아 수 2026년 6월 인구동향 통계청; 2025년 7월 인구동향 출생아 수 2만1천명 전년동월대비 증가; 2026년 3월 인구동향 출생아 수 증가률 19.5% 통계청; Statistics Korea monthly live births 2026 인구동향 출생아 수; 출생아 수 2026년 5월 인구동향 통계청; 2025년 7월 인구동향 출생아 수 2만 명 전년동월대비 증가 통계청; 2024년 7월 인구동향 출생아 수 2만명 통계청 발표; Statistics Korea monthly live births 2026 인구동향 출생아 수; 출생아 수 2026년 6월 인구동향 통계청; 2025년 7월 인구동향 출생아 수 2만1844명 전년동월대비; "2026년 3월 인구동향" 출생아 수 19.5% 증가 통계청

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4721687` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=294740&koreanId=294708` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532&listChk=list` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tvchosun.com/site/data/html_dir/2026/06/24/2026062490133.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.donga.com/news/article/all/20250924/132453847/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03230806642303400&mediaCodeNo=257` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.shinailbo.co.kr/news/articleView.html?idxno=2122107` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tvchosun.com/site/data/html_dir/2026/03/25/2026032590189.html` -> **snapshot** (snapshot 20260409031543); points raw/verified 8/7
  - p1 South Korea live births, January 2026 = **26,916** live births (2026-01-01..2026-01-31) [keep: ] quote: "지난 1월 출생아 수는 2만 6,916명으로 전년 동월 대비 11.7%(2,817명) 증가했다."
  - p2 South Korea live births, January 2026, year-on-year change percent = **11.7** % (2026-01-01..2026-01-31) [DISCARD: Redundant percent duplicate of p1/p3/p176; the level and absolute change carry the information.] quote: "지난 1월 출생아 수는 2만 6,916명으로 전년 동월 대비 11.7%(2,817명) 증가했다."
  - p3 South Korea live births, January 2026, year-on-year change in births = **2,817** live births (2026-01-01..2026-01-31) [keep: ] quote: "지난 1월 출생아 수는 2만 6,916명으로 전년 동월 대비 11.7%(2,817명) 증가했다."
  - p4 South Korea live births, January 2019 (prior January maximum) = **30,271** live births (2019-01-01..2019-01-31) [DISCARD: January 2019 level is a historical comparison for a January record, not informative for July 2026 level.] quote: "이는 1월 기준으로 지난 2019년(3만 271명) 이후 7년 만에 가장 많은 수치다."
  - p5 South Korea January live births change, 2016 (start of 9-year decline) = **-6** % (2016-01-01..2016-01-31) [DISCARD: Historical January percent change from 2016; no role in a July 2026 level estimate.] quote: "1월 출생아 수는 2016년(-6.0%)부터 9년 연속 감소세를 보이다가 지난해 12.5% 늘어난 데 이어 올해도 2년 연속 10%대의 높은 증가율을 기록했다."
  - p6 South Korea total fertility rate, January 2026 = **0.99** live births per woman (2026-01-01..2026-01-31) [DISCARD: January 2026 TFR; a derived rate not needed once the January level is kept.] quote: "1월 합계출산율은 0.99명으로 집계돼 전년 동월 대비 0.10명 상승했다."
  - p7 South Korea total fertility rate, January 2026, year-on-year change = **0.1** live births per woman (2026-01-01..2026-01-31) [DISCARD: January TFR change; redundant with p6.] quote: "1월 합계출산율은 0.99명으로 집계돼 전년 동월 대비 0.10명 상승했다."
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=446612&tag=&nPage=1&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] Resident registration / administrative births

Hypothesis: Monthly resident-registration birth counts (행정안전부 주민등록 인구통계) track KOSTAT occurrence-based births closely and can proxy July 2026 before the official release.

Queries issued by the searcher: 주민등록 인구통계 출생 2026년 7월; 행정안전부 월별 출생자 수 주민등록 출생 2026; 주민등록 인구통계 출생자 수 전국 2026년 6월 행안부 월별; "주민등록" 출생아 수 2025년 월별 전국 통계청 인구동향 차이 비교; 주민등록 인구통계 출생 2026년 7월; 행정안전부 월별 출생자 수 주민등록 출생 2025; 주민등록 출생등록자 수 2026년 7월 행정안전부 발표; KOSIS 주민등록인구통계 월별 출생등록자 수 2024 2025 2026; 주민등록 인구통계 출생 2026년 7월; 행정안전부 월별 출생자 수 주민등록; 주민등록 기준 출생등록 2026년 7월 전국 명; 행안부 주민등록 출생등록 2026년 6월 증가

- `https://www.jeongeup.go.kr/board/view.jeongeup?boardId=BBS_0000145&menuCd=DOM_000000105002000000&paging=ok&startPage=1&dataSid=1416956` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yeosu.go.kr/www/govt/stats/stats_popul?idx=581028&mode=view` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1466&no=9919988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mois.go.kr/pdf/03statistics-description.pdf` -> **snapshot** (snapshot 20251124074411); points raw/verified 0/0
- `https://www.tongyeong.go.kr/00681/00827/00837.web?amode=view&idx=662037&gcode=1020&ccx=Y&cpage=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://app.jindo.go.kr/main/article/B0003/download/tp0?atchFile=RklMRV8wMDAwMDAwMDA0OTQ0ODM6MS4w` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://korea.nabo.go.kr/board/file/down.do?fid=33319286` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bigdata.gyeongnam.go.kr/user/provincialGovStatus/govStatusList.gn?menuCd=DOM_000000117007000000&contentsSid=189&category=PUBAD&cate2Cd=BRTPLN` -> **snapshot** (snapshot 20220731063450); points raw/verified 9/9
  - p8 Monthly resident-registration births (출생인구), administrative (Haenganbu) count, J = **1,092** births (2022-06-01..2022-06-30) [DISCARD: Gyeongnam-province administrative birth count, not a national figure; wrong scope.] quote: "출생인구 1,092 명 월 2022-06 행안부"
  - p9 Monthly resident-registration deaths (사망인구), administrative (Haenganbu) count, J = **1,929** deaths (2022-06-01..2022-06-30) [DISCARD: Gyeongnam-province deaths; wrong scope and irrelevant to births.] quote: "사망인구 1,929 명 월 2022-06 행안부"
  - p10 Resident-registration population (인구현황), administrative (Haenganbu), June 2022 = **3,295,615** people (2022-06-01..2022-06-30) [DISCARD: Gyeongnam-province population; wrong scope.] quote: "인구현황 3,295,615 명 월 2022-06 행안부"
  - p11 Population growth rate (인구증가율), administrative (Haenganbu), 2022 = **-0.91** % (2022-01-01..2022-12-31) [DISCARD: Gyeongnam-province growth rate; wrong scope.] quote: "인구증가율 -0.91 % 년 2022 행안부"
  - p12 In-migration population (전입인구), KOSTAT, 2021 = **374,782** people (2021-01-01..2021-12-31) [DISCARD: Gyeongnam-province in-migration; wrong scope.] quote: "전입인구 374,782 명 년 2021 통계청"
  - p13 Out-migration population (전출인구), KOSTAT, 2021 = **388,485** people (2021-01-01..2021-12-31) [DISCARD: Gyeongnam-province out-migration; wrong scope.] quote: "전출인구 388,485 명 년 2021 통계청"
  - p14 Projected population (추계인구), KOSTAT, 2031 = **3,314,828** people (2031-01-01..2031-12-31) [DISCARD: Gyeongnam-province population projection; wrong scope.] quote: "추계인구 3,314,828 명 년 2031 통계청"
  - p15 Future household projection (장래가구추계), KOSTAT, 2032 = **1,442,293** households (2032-01-01..2032-12-31) [DISCARD: Gyeongnam-province household projection; wrong scope.] quote: "장래가구추계 1,442,293 년 2032 통계청"
  - p16 Basic livelihood security recipients (기초생활보장수급자수), KOSTAT, 2020 = **137,605** people (2020-01-01..2020-12-31) [DISCARD: Gyeongnam-province welfare recipients; wrong scope.] quote: "기초생활보장수급자수 137,605 명 년 2020 통계청"
- `http://apt-micro.tistory.com/tag/%EA%B2%BD%EA%B8%B0%EB%8F%84%EC%98%81%EC%95%84%EC%B6%9C%EC%83%9D?page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bigdata.gyeongnam.go.kr/bigdata/collect/list.gn?cds=OC0002&menuCd=DOM_000000103002000000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Births by province / city

Hypothesis: Sum of regional monthly birth counts (시도별 출생) equals the national total; regional releases may appear earlier or provide partial July 2026 coverage.

Queries issued by the searcher: 시도별 출생아 수 2026년 6월 인구동향; KOSTAT monthly population trends June 2026 live births; 2026년 5월 인구동향 출생아 수 시도별 표; KOSIS 시도별 출생아 수 월별 통계표 인구동향; 시도별 출생아 수 2026년 7월; 지역별 출생 통계 2026 시도별 출생아 수; 2026년 5월 인구동향 국가데이터처 보도자료 시도별 출생아 수 표; 2025년 7월 인구동향 시도별 출생아 수 경기 서울 인천; 시도별 출생아 수 2026년 7월; provincial births Korea July 2026 statistics; 2026년 5월 인구동향 시도별 출생아 수 발표; 2026년 6월 인구동향 출생아 수 국가데이터처 발표

- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thepowernews.co.kr/view.php?ud=202607291307464277de3f0aa1be_7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.daejonilbo.com/news/articleView.html?idxno=2291311` -> **snapshot** (snapshot 20260809223302); points raw/verified 29/24
  - p17 National live births, South Korea, May 2026 = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 전국 출생아 수는 2만 3160명으로"
  - p18 Year-on-year growth rate of national live births, May 2026 vs May 2025 = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "지난해 같은 달(2만 379명)보다 13.6% 증가했다"
  - p19 National live births, South Korea, May 2019 (prior May peak) = **25,299** live births (2019-05-01..2019-05-31) [DISCARD: May 2019 comparison level; historical context only, not a July input.] quote: "5월 기준 2019년(2만 5299명) 이후 7년 만에 가장 많았다"
  - p20 Daejeon live births, May 2026 = **671** live births (2026-05-01..2026-05-31) [DISCARD: Daejeon May 2026 births; sub-national, not needed for national estimate.] quote: "대전 출생아 수는 671명으로 1년 전(600명) 대비 11.8% 늘었다"
  - p21 Year-on-year growth rate of Daejeon live births, May 2026 vs May 2025 = **11.8** % (2026-05-01..2026-05-31) [DISCARD: Daejeon May growth rate; sub-national.] quote: "1년 전(600명) 대비 11.8% 늘었다"
  - p22 Daejeon cumulative live births, January-May 2026 = **3,619** live births (2026-01-01..2026-05-31) [DISCARD: Daejeon cumulative births; sub-national.] quote: "1-5월 누적출생아도 3619명으로"
  - p23 Year-on-year growth rate of Daejeon cumulative live births, Jan-May 2026 vs Jan- = **14.1** % (2026-01-01..2026-05-31) [DISCARD: Daejeon cumulative growth; sub-national.] quote: "지난해 같은 기간(3173명)과 비교해 14.1% 올랐다"
  - p24 Sejong live births, May 2026 = **286** live births (2026-05-01..2026-05-31) [DISCARD: Sejong May births; sub-national.] quote: "세종은 286명으로 전년 동월(235명) 대비 21.7% 증가해"
  - p25 Year-on-year growth rate of Sejong live births, May 2026 vs May 2025 = **21.7** % (2026-05-01..2026-05-31) [DISCARD: Sejong May growth; sub-national.] quote: "전년 동월(235명) 대비 21.7% 증가해 전국에서 가장 높은 증가율을 기록했다"
  - p26 Sejong crude birth rate, May 2026 (live births per 1,000 population) = **8.6** live births per 1,000 population (2026-05-01..2026-05-31) [DISCARD: Sejong crude birth rate; sub-national.] quote: "조출생률도 인구 1000명당 8.6명으로 전국에서 가장 높았다"
  - p27 South Chungcheong live births, May 2026 = **875** live births (2026-05-01..2026-05-31) [DISCARD: South Chungcheong May births; sub-national.] quote: "충남의 출생아 수는 1년 전(827명)보다 5.8% 높은 총 875명이었으며"
  - p28 Year-on-year growth rate of South Chungcheong live births, May 2026 vs May 2025 = **5.8** % (2026-05-01..2026-05-31) [DISCARD: South Chungcheong growth; sub-national.] quote: "1년 전(827명)보다 5.8% 높은 총 875명"
  - p29 North Chungcheong live births, May 2026 = **700** live births (2026-05-01..2026-05-31) [DISCARD: North Chungcheong May births; sub-national.] quote: "충북에선 같은 기간 1% 늘어난 700명이 태어났다"
  - p30 Year-on-year growth rate of North Chungcheong live births, May 2026 vs May 2025 = **1** % (2026-05-01..2026-05-31) [DISCARD: North Chungcheong growth; sub-national.] quote: "충북에선 같은 기간 1% 늘어난 700명이 태어났다"
  - p31 National marriages, South Korea, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 전국 혼인 건수는 2만 368건으로 지난해보다 6.4% 감소했다"
  - p32 Year-on-year change in national marriages, May 2026 vs May 2025 = **6.4** % (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 전국 혼인 건수는 2만 368건으로 지난해보다 6.4% 감소했다"
  - p33 Daejeon marriages, May 2026 = **644** marriages (2026-05-01..2026-05-31) [DISCARD: Daejeon marriages; sub-national and not a birth input.] quote: "대전 644건, 세종 141건, 충남 738건, 충북 567건으로"
  - p34 Sejong marriages, May 2026 = **141** marriages (2026-05-01..2026-05-31) [DISCARD: Sejong marriages; sub-national.] quote: "대전 644건, 세종 141건, 충남 738건, 충북 567건으로"
  - p35 South Chungcheong marriages, May 2026 = **738** marriages (2026-05-01..2026-05-31) [DISCARD: South Chungcheong marriages; sub-national.] quote: "대전 644건, 세종 141건, 충남 738건, 충북 567건으로"
  - p36 North Chungcheong marriages, May 2026 = **567** marriages (2026-05-01..2026-05-31) [DISCARD: North Chungcheong marriages; sub-national.] quote: "대전 644건, 세종 141건, 충남 738건, 충북 567건으로"
  - p37 Sejong natural increase (births minus deaths), May 2026 = **142** persons (2026-05-01..2026-05-31) [DISCARD: Sejong natural increase; sub-national.] quote: "5월 세종에선 142명(4.3%↑)이 늘어"
  - p38 Daejeon natural decrease (deaths minus births), May 2026 = **92** persons (2026-05-01..2026-05-31) [DISCARD: Daejeon natural decrease; sub-national.] quote: "대전은 92명(0.8%↓)"
  - p39 South Chungcheong natural decrease (deaths minus births), May 2026 = **711** persons (2026-05-01..2026-05-31) [DISCARD: South Chungcheong natural decrease; sub-national.] quote: "충남 711명(3.9%↓)"
  - p40 North Chungcheong natural decrease (deaths minus births), May 2026 = **353** persons (2026-05-01..2026-05-31) [DISCARD: North Chungcheong natural decrease; sub-national.] quote: "충북은 353명(2.6%↓)의 자연감소를 기록했다"
- `https://www.ajunews.com/view/20260729091618236?l=T` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jibs.co.kr/news/articles/articlesDetail/63991?feed=na` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n.news.naver.com/mnews/article/016/0002676816?sid=101` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dailian.co.kr:3000/news/view/1672164/5%EC%9B%94-%EC%B6%9C%EC%83%9D%EC%95%84-136-%EB%8A%98%EC%97%88%EC%A7%80-%ED%98%BC%EC%9D%B8-64-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ghdx.healthdata.org/organizations/ministry-data-and-statistics-kostat-south-korea?qt-organization_records=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.einfomax.co.kr/news/articleView.html?idxno=4431869` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://rkfka24.tistory.com/324` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period year 2025 does not appear in the page text or URL (likely mis-dated): 5)

### d4 [base_rates] Demographic accounting

Hypothesis: Births in a month ≈ women of childbearing age × age-specific fertility rates × days; or births ≈ births 9 months earlier conception proxies. Use annual births and monthly seasonal shares to derive July.

Queries issued by the searcher: Statistics Korea monthly Population Trends live births June 2026; 합계출산율 2026년 출생아 수 월별 인구동향; 2025년 7월 출생아 수 명 인구동향 2025년 7월; 2025년 연간 출생아 수 25만4341명 합계출산율 0.80 통계청; Statistics Korea monthly population trends 2026 출생아 수 6월; South Korea births 2025 annual total 240,000 Statistics Korea; 2026년 5월 인구동향 출생아 수 발표; 2025년 7월 출생아 수 명 인구동향; Statistics Korea monthly Population Trends 2026 births 인구동향 출생아 수; South Korea annual births 2025 total fertility rate 0.75 Statistics Korea; 2026년 5월 인구동향 출생아 수 2만 명 전년동월대비 증가; 2025년 월별 출생아 수 7월 2만1854명 인구동향

- `https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000067380` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=446612&seq=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=288047` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20260729_0003727581` -> **snapshot** (snapshot 20260730190231); points raw/verified 29/22
  - p41 Year-on-year increase in live births, May 2026 vs May 2025 = **2,781** live births (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 출생아 수는 2만3160명으로 전년 같은 달보다 2781명(13.6%) 증가했다."
  - p42 Year-on-year growth rate of live births, May 2026 = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 출생아 수는 2만3160명으로 전년 같은 달보다 2781명(13.6%) 증가했다."
  - p43 Year-on-year growth rate of cumulative live births, January-May 2026 = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 전년 같은 기간보다 15.2% 늘었다."
  - p44 Total fertility rate, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율은 0.85명으로 전년 같은 달(0.75명)보다 0.10명 상승했다."
  - p45 Change in total fertility rate, May 2026 vs May 2025 = **0.1** live births per woman (2026-05-01..2026-05-31) [DISCARD: Redundant TFR change duplicate of p44/p74.] quote: "5월 합계출산율은 0.85명으로 전년 같은 달(0.75명)보다 0.10명 상승했다."
  - p46 Age-specific fertility rate, women aged 30-34, May 2026 = **78** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: Age-specific fertility rate 30-34; no population denominator kept to convert to births.] quote: "30~34세의 출산율은 78.0명으로 전년보다 8.3명 증가했고, 35~39세는 58.0명으로 9.9명 늘었다."
  - p47 Year-on-year change in age-specific fertility rate, women aged 30-34, May 2026 = **8.3** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR change 30-34; no usable denominator.] quote: "30~34세의 출산율은 78.0명으로 전년보다 8.3명 증가했고, 35~39세는 58.0명으로 9.9명 늘었다."
  - p48 Age-specific fertility rate, women aged 35-39, May 2026 = **58** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR 35-39; no usable denominator.] quote: "30~34세의 출산율은 78.0명으로 전년보다 8.3명 증가했고, 35~39세는 58.0명으로 9.9명 늘었다."
  - p49 Year-on-year change in age-specific fertility rate, women aged 35-39, May 2026 = **9.9** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR change 35-39; no usable denominator.] quote: "30~34세의 출산율은 78.0명으로 전년보다 8.3명 증가했고, 35~39세는 58.0명으로 9.9명 늘었다."
  - p50 Age-specific fertility rate, women aged 25-29, May 2026 = **20.6** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR 25-29; no usable denominator.] quote: "25~29세와 40세 이상은 각각 20.6명과 4.7명으로 1년 전보다 0.5명씩 증가했다."
  - p51 Age-specific fertility rate, women aged 40 and over, May 2026 = **4.7** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR 40+; no usable denominator.] quote: "25~29세와 40세 이상은 각각 20.6명과 4.7명으로 1년 전보다 0.5명씩 증가했다."
  - p52 Year-on-year change in age-specific fertility rate, women aged 25-29 and 40+, Ma = **0.5** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR change 25-29/40+; no usable denominator.] quote: "25~29세와 40세 이상은 각각 20.6명과 4.7명으로 1년 전보다 0.5명씩 증가했다."
  - p53 Age-specific fertility rate, women aged 24 and under, May 2026 = **1.9** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR 24 and under; no usable denominator.] quote: "24세 이하는 1.9명으로 0.4명 감소했다."
  - p54 Year-on-year change in age-specific fertility rate, women aged 24 and under, May = **0.4** live births per 1,000 women (2026-05-01..2026-05-31) [DISCARD: ASFR change 24 and under; no usable denominator.] quote: "24세 이하는 1.9명으로 0.4명 감소했다."
  - p55 Share of first births among all live births, May 2026 = **63** % (2026-05-01..2026-05-31) [DISCARD: Birth-order share; not needed for a level estimate.] quote: "전체 출생아 가운데 첫째아가 차지하는 비중은 63.0%로 전년보다 1.3%포인트(p) 상승했다."
  - p56 Share of second births among all live births, May 2026 = **31.7** % (2026-05-01..2026-05-31) [DISCARD: Birth-order share; not needed.] quote: "둘째아의 비중은 31.7%로 0.2%p, 셋째아 이상은 5.3%로 1.1%p 각각 하락했다."
  - p57 Share of third-or-higher births among all live births, May 2026 = **5.3** % (2026-05-01..2026-05-31) [DISCARD: Birth-order share; not needed.] quote: "둘째아의 비중은 31.7%로 0.2%p, 셋째아 이상은 5.3%로 1.1%p 각각 하락했다."
  - p58 Live births in Seoul, May 2026 = **4,227** live births (2026-05-01..2026-05-31) [DISCARD: Seoul May births; sub-national.] quote: "서울은 4227명으로 전년보다 17.7%, 경기는 7075명으로 13.8% 늘었다."
  - p59 Live births in Gyeonggi, May 2026 = **7,075** live births (2026-05-01..2026-05-31) [DISCARD: Gyeonggi May births; sub-national.] quote: "서울은 4227명으로 전년보다 17.7%, 경기는 7075명으로 13.8% 늘었다."
  - p60 Live births in Jeju, May 2026 = **252** live births (2026-05-01..2026-05-31) [DISCARD: Jeju May births; sub-national.] quote: "제주는 252명으로 3.1% 감소했다."
  - p61 Crude marriage rate, May 2026 = **4.7** marriages per 1,000 people (2026-05-01..2026-05-31) [DISCARD: Crude marriage rate; not a birth input.] quote: "5월 조혼인율은 4.7건으로 전년보다 0.3건 감소했다."
  - p62 Natural increase (live births minus deaths), May 2026 = **-6,413** persons (2026-05-01..2026-05-31) [DISCARD: May natural increase; not a birth input.] quote: "출생아 수에서 사망자 수를 뺀 '자연증가'는 -6413명으로, 출생과 사망만 놓고 보면 인구가 그만큼 줄었다는 의미다."
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p63 Live births in South Korea, July 2025 = **21,803** live births (2025-07-01..2025-07-31) [keep: ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p64 Year-on-year change in live births, July 2025 vs July 2024 = **5.9** % (2025-07-01..2025-07-31) [DISCARD: July 2025 percent change duplicate of p109.] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p65 Deaths in South Korea, July 2025 = **27,979** deaths (2025-07-01..2025-07-31) [DISCARD: July 2025 deaths; not a birth input.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p66 Year-on-year change in deaths, July 2025 vs July 2024 = **0.7** % (2025-07-01..2025-07-31) [DISCARD: July 2025 deaths change; not a birth input.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p67 Marriages in South Korea, July 2025 = **20,394** marriages (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages; not a birth input.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p68 Year-on-year change in marriages, July 2025 vs July 2024 = **8.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 marriage change; not a birth input.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p69 Divorces in South Korea, July 2025 = **7,826** divorces (2025-07-01..2025-07-31) [DISCARD: July 2025 divorces; not a birth input.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p70 Year-on-year change in divorces, July 2025 vs July 2024 = **1.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 divorce change; not a birth input.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p71 Natural increase (live births minus deaths) in South Korea, July 2025 = **-6,175** persons (2025-07-01..2025-07-31) [DISCARD: July 2025 natural increase; not a birth input.] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `http://47.newstomato.com/ReadNews.aspx?no=1308574` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8366129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03230806642303400&mediaCodeNo=257` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://vop.co.kr/A00001695396.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://biz.sbs.co.kr/article/20000312840` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.163.com/dy/article/L5EHO86K0519DDQ2.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cb.yna.co.kr/gate/big5/m-cn.yna.co.kr/view/ACK20260826002100881?section=news` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 7 (scale word '万' not supported by quote or table header: 6; period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d5 [forecasts_markets] Statistical agency and media forecasts

Hypothesis: KOSTAT or media may publish projections or nowcasts of 2026 monthly births; these constrain the plausible range.

Queries issued by the searcher: KOSTAT monthly live births 2026 South Korea 인구동향 출생아 수; 2026년 출생아 수 전망 통계청; "2025년 7월" 출생아 수 2만1천명 인구동향; 2026년 6월 인구동향 출생아 수 발표 8월; KOSTAT monthly live births 2026 인구동향 출생아 수; 2026년 5월 출생아 수 인구동향 통계청; 2025년 7월 출생아 수 2만 21,854 통계청 인구동향; 2026년 출생아 수 전망 30만명 반등 장래인구추계; KOSTAT monthly live births 2026 인구동향 출생아 수; 2026년 출생아 수 전망 통계청; "2026년 5월 인구동향" 국가데이터처 보도자료 출생아 23,160명; 2025년 7월 출생아 수 21,854명 인구동향

- `https://v.daum.net/v/20260802121104585` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/society/2026/08/03/20260803010003` -> **snapshot** (snapshot 20260803052117); points raw/verified 25/23
  - p72 South Korea total fertility rate, Q1 2026 = **0.95** children per woman (2026-01-01..2026-03-31) [DISCARD: Q1 2026 TFR; derived rate, no denominator kept.] quote: "올해 1분기 합계출산율은 0.95명으로 집계됐다."
  - p73 South Korea total fertility rate, April 2026 = **0.93** children per woman (2026-04-01..2026-04-30) [DISCARD: April 2026 TFR; derived rate, no denominator kept.] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p74 South Korea total fertility rate, May 2026 = **0.85** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "4월은 0.93명, 5월은 0.85명으로 지난해 같은 달보다 각각 0.13명, 0.10명 높았다."
  - p75 South Korea live births, January-May 2026 cumulative = **122,694** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p76 South Korea live births, January-May 2026 increase over same period prior year = **16,166** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p77 South Korea live births, January-May 2026 year-on-year growth rate = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 태어난 아이는 12만 2694명으로 지난해 같은 기간보다 1만 6166명(15.2%) 늘었다."
  - p78 South Korea live births, May 2026 = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p79 South Korea live births, May 2026 increase over May prior year = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 absolute change p41.] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p80 South Korea live births, May 2026 year-on-year growth rate = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 growth rate p42.] quote: "5월 출생아는 2만 3160명으로 1년 전보다 2781명(13.6%) 증가했다."
  - p81 South Korea annual live births, prior year (2025) = **254,457** live births (2025-01-01..2025-12-31) [keep: ] quote: "지금과 같은 흐름이 이어지면 올해 연간 출생아 수는 지난해(25만 4457명)를 넘어 20만명대 후반까지 늘어날 것으로 예상된다."
  - p82 South Korea annual live births, 2026 expected range lower bound (forecast) = **200,000** live births (2026-01-01..2026-12-31) [keep: ] quote: "지금과 같은 흐름이 이어지면 올해 연간 출생아 수는 지난해(25만 4457명)를 넘어 20만명대 후반까지 늘어날 것으로 예상된다."
  - p83 South Korea total fertility rate, 2018 = **0.98** children per woman (2018-01-01..2018-12-31) [DISCARD: 2018 TFR; historical context only.] quote: "합계출산율은 2018년 0.98명으로 처음 1.0명 아래로 떨어졌다."
  - p84 South Korea total fertility rate, 2023 (record low) = **0.72** children per woman (2023-01-01..2023-12-31) [DISCARD: 2023 TFR; historical context only.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p85 South Korea total fertility rate, 2024 = **0.75** children per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; historical context only.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p86 South Korea total fertility rate, 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [DISCARD: 2025 TFR; historical context only.] quote: "2023년에는 역대 최저인 0.72명까지 내려갔다가 2024년 0.75명, 지난해 0.80명으로 2년 연속 반등했다."
  - p87 South Korea total fertility rate, 2019 = **0.92** children per woman (2019-01-01..2019-12-31) [DISCARD: 2019 TFR; historical context only.] quote: "현실화하면 2019년 0.92명 이후 7년 만이다."
  - p88 South Korea population aged 0-14, 2025 census = **5,225,000** person (2025-01-01..2025-12-31) [DISCARD: Child population; not a birth input.] quote: "2025년 인구주택총조사에 따르면 0~14세 유소년 인구는 522만 5000명으로 10년 전보다 24.9% 감소했다."
  - p89 South Korea population aged 0-14, 10-year decline rate = **24.9** % (2025-01-01..2025-12-31) [DISCARD: Child population decline; not a birth input.] quote: "2025년 인구주택총조사에 따르면 0~14세 유소년 인구는 522만 5000명으로 10년 전보다 24.9% 감소했다."
  - p90 South Korea population aged 65+, 2025 census = **10,723,000** person (2025-01-01..2025-12-31) [DISCARD: Elderly population; not a birth input.] quote: "반면 65세 이상 고령 인구는 같은 기간 661만 7000명에서 1072만 3000명으로 62.0% 늘었다."
  - p91 South Korea population aged 65+, 10-year growth rate = **62** % (2025-01-01..2025-12-31) [DISCARD: Elderly growth; not a birth input.] quote: "반면 65세 이상 고령 인구는 같은 기간 661만 7000명에서 1072만 3000명으로 62.0% 늘었다."
  - p92 South Korea share of population aged 0-14, 2025 census = **10.1** % (2025-01-01..2025-12-31) [DISCARD: Child share; not a birth input.] quote: "전체 인구에서 유소년이 차지하는 비중은 10.1%에 그쳤지만 고령층은 20.7%까지 높아졌다."
  - p93 South Korea share of population aged 65+, 2025 census = **20.7** % (2025-01-01..2025-12-31) [DISCARD: Elderly share; not a birth input.] quote: "전체 인구에서 유소년이 차지하는 비중은 10.1%에 그쳤지만 고령층은 20.7%까지 높아졌다."
  - p94 South Korea population aged 85+, 2025 census = **1,148,525** person (2025-01-01..2025-12-31) [DISCARD: 85+ population; not a birth input.] quote: "특히 85세 이상 초고령 인구는 최근 10년간 52만 5723명에서 114만 8525명으로 두 배 넘게 불었다."
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532&listChk=list` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20251231132800002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.joongang.co.kr/sum-article/25422477?type=short` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/economy/2026/07/29/20260729500210` -> **snapshot** (snapshot 20260730174904); points raw/verified 14/13
  - p95 Live births in South Korea, May 2026 (monthly) = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p96 Year-on-year increase in live births, South Korea, May 2026 = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 absolute change p41.] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p97 Year-on-year growth rate of live births, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 growth rate p42.] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p98 Cumulative live births, South Korea, January-May 2026 = **122,694** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아는 12만 2694명으로 1~5월 기준 7년 만에 가장 많았다."
  - p99 Total fertility rate, South Korea, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p100 Year-on-year change in total fertility rate, South Korea, May 2026 = **0.1** live births per woman (2026-05-01..2026-05-31) [DISCARD: Duplicate TFR change.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p101 Marriages, South Korea, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [keep: ] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p102 Year-on-year change in marriages, South Korea, May 2026 = **1,392** marriages (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 marriage change p137.] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p103 Year-on-year growth rate of marriages, South Korea, May 2026 = **-6.4** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 marriage growth p138.] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p104 Natural population decrease, South Korea, May 2026 = **6,413** person (2026-05-01..2026-05-31) [DISCARD: May natural decrease; not a birth input.] quote: "출생아 증가에도 사망자가 더 많아 인구는 6413명 자연 감소했다."
  - p105 Deaths, South Korea, May 2026 = **29,573** person (2026-05-01..2026-05-31) [DISCARD: Deaths May 2026; irrelevant to births.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p106 Year-on-year increase in deaths, South Korea, May 2026 = **1,091** person (2026-05-01..2026-05-31) [DISCARD: Deaths change; not a birth input.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p107 Year-on-year growth rate of deaths, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Deaths +13.6% is a copy error (1,091/28,482 ≈ 3.8%); misleading duplicate of p155.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
- `https://dailymagazine.co.kr/news/newsview.php?ncode=1065541823597083&dt=m` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=445260&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asiae.co.kr/article/2025092410582510794` -> **snapshot** (snapshot 20250924133737); points raw/verified 29/28
  - p108 Live births in South Korea, July 2025 (monthly Population Trends) = **21,803** live births (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 출생아 수가 2만1803명으로 4년 만에 최대 규모를 기록했다."
  - p109 Year-on-year change in South Korea live births, July 2025 = **5.9** % (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월 대비 5.9%(1223명) 늘었다."
  - p110 Year-on-year increase in South Korea live births, July 2025 (persons) = **1,223** live births (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월 대비 5.9%(1223명) 늘었다."
  - p111 Live births in South Korea, July 2021 (prior July maximum) = **22,364** live births (2021-07-01..2021-07-31) [DISCARD: July 2021 comparison level; historical context only.] quote: "이는 역대 7월 기준으로 2021년(2만2364명) 이후 최대 규모다."
  - p112 Consecutive months of increase in South Korea live births (through July 2025) = **13** month (2024-07-01..2025-07-31) [DISCARD: Consecutive-month streak through July 2025; context only.] quote: "출생아 수는 13개월 연속 늘고 있다."
  - p113 Consecutive months of increase in South Korea marriages (through July 2025) = **16** month (2024-04-01..2025-07-31) [DISCARD: Marriage streak; context only.] quote: "통계청 관계자는 "혼인이 16개월째 늘고 있는 데다 주요 출산 연령대인 30대 초반 여성 인구가 늘면서 출생아 수도 증가하고 있다"고 설명했다."
  - p114 Live births in Seoul, July 2025 = **3,938** live births (2025-07-01..2025-07-31) [DISCARD: Seoul July 2025 births; sub-national.] quote: "시도별 출생아 수를 보면 서울(3938명)과 인천(188명), 부산(1218명) 등 13개 시도에서 늘어난 것으로 나타났다."
  - p115 Live births in Incheon, July 2025 = **188** live births (2025-07-01..2025-07-31) [DISCARD: Incheon July 2025 births; sub-national.] quote: "시도별 출생아 수를 보면 서울(3938명)과 인천(188명), 부산(1218명) 등 13개 시도에서 늘어난 것으로 나타났다."
  - p116 Live births in Busan, July 2025 = **1,218** live births (2025-07-01..2025-07-31) [DISCARD: Busan July 2025 births; sub-national.] quote: "시도별 출생아 수를 보면 서울(3938명)과 인천(188명), 부산(1218명) 등 13개 시도에서 늘어난 것으로 나타났다."
  - p117 Live births in Gwangju, July 2025 = **560** live births (2025-07-01..2025-07-31) [DISCARD: Gwangju July 2025 births; sub-national.] quote: "광주(560명)와 세종(240명) 등 4개 시도는 줄었다."
  - p118 Live births in Sejong, July 2025 = **240** live births (2025-07-01..2025-07-31) [DISCARD: Sejong July 2025 births; sub-national.] quote: "광주(560명)와 세종(240명) 등 4개 시도는 줄었다."
  - p119 Total fertility rate in South Korea, July 2025 = **0.8** live births per woman (2025-07-01..2025-07-31) [keep: ] quote: "합계출산율(여자 1명이 평생 낳을 것으로 예상하는 평균 출생아 수)은 0.80명으로 0.04명 증가했다."
  - p120 Change in South Korea total fertility rate, July 2025 vs year earlier = **0.04** live births per woman (2025-07-01..2025-07-31) [DISCARD: July 2025 TFR change; context only.] quote: "합계출산율(여자 1명이 평생 낳을 것으로 예상하는 평균 출생아 수)은 0.80명으로 0.04명 증가했다."
  - p121 Total fertility rate in South Korea, May 2025 = **0.75** live births per woman (2025-05-01..2025-05-31) [DISCARD: May 2025 TFR; context only.] quote: "지난 5월(0.75명)과 6월(0.76명)에 0.7명대를 기록한 데 이어 0.8명대로 늘어난 것이다."
  - p122 Total fertility rate in South Korea, June 2025 = **0.76** live births per woman (2025-06-01..2025-06-30) [DISCARD: June 2025 TFR; context only.] quote: "지난 5월(0.75명)과 6월(0.76명)에 0.7명대를 기록한 데 이어 0.8명대로 늘어난 것이다."
  - p123 Deaths in South Korea, July 2025 = **27,979** deaths (2025-07-01..2025-07-31) [DISCARD: July 2025 deaths; not a birth input.] quote: "지난 7월 사망자 수는 2만7979명으로 0.7% 감소했다."
  - p124 Natural decrease (births minus deaths) in South Korea, July 2025 = **6,175** persons (2025-07-01..2025-07-31) [DISCARD: July 2025 natural decrease; not a birth input.] quote: "이로써 자연감소(출생아 수-사망자 수)는 6175명이다."
  - p125 Natural decrease in South Korea, May 2025 = **-8,202** persons (2025-05-01..2025-05-31) [DISCARD: May 2025 natural decrease; not a birth input.] quote: "지난 5월(-8202명)과 6월(-7317명)에 비해 자연감소 규모가 줄어든 모습이다."
  - p126 Natural decrease in South Korea, June 2025 = **-7,317** persons (2025-06-01..2025-06-30) [DISCARD: June 2025 natural decrease; not a birth input.] quote: "지난 5월(-8202명)과 6월(-7317명)에 비해 자연감소 규모가 줄어든 모습이다."
  - p127 Marriages in South Korea, July 2025 = **20,394** marriages (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages; not a birth input.] quote: "지난 7월 혼인 건수는 2만394건으로 전년 동월보다 8.4%(1583건) 증가했다."
  - p128 Year-on-year change in South Korea marriages, July 2025 = **8.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 marriage change; not a birth input.] quote: "지난 7월 혼인 건수는 2만394건으로 전년 동월보다 8.4%(1583건) 증가했다."
  - p129 Year-on-year increase in South Korea marriages, July 2025 (count) = **1,583** marriages (2025-07-01..2025-07-31) [DISCARD: July 2025 marriage change count; not a birth input.] quote: "지난 7월 혼인 건수는 2만394건으로 전년 동월보다 8.4%(1583건) 증가했다."
  - p130 Marriages in South Korea, July 2016 (prior July maximum) = **21,154** marriages (2016-07-01..2016-07-31) [DISCARD: July 2016 marriages; not a birth input.] quote: "역대 7월 기준으로 2016년(2만1154건) 이후 9년 만에 최대 혼인 건수를 기록했다."
  - p131 Marriages in Seoul, July 2025 = **4,068** marriages (2025-07-01..2025-07-31) [DISCARD: Seoul July 2025 marriages; sub-national.] quote: "시도별로 보면 서울(4068건)과 인천(1234건), 부산(1092건) 등 11개 시도에서 혼인 건수가 늘었다."
  - p132 Marriages in Incheon, July 2025 = **1,234** marriages (2025-07-01..2025-07-31) [DISCARD: Incheon July 2025 marriages; sub-national.] quote: "시도별로 보면 서울(4068건)과 인천(1234건), 부산(1092건) 등 11개 시도에서 혼인 건수가 늘었다."
  - p133 Marriages in Busan, July 2025 = **1,092** marriages (2025-07-01..2025-07-31) [DISCARD: Busan July 2025 marriages; sub-national.] quote: "시도별로 보면 서울(4068건)과 인천(1234건), 부산(1092건) 등 11개 시도에서 혼인 건수가 늘었다."
  - p134 Divorces in South Korea, July 2025 = **7,826** divorces (2025-07-01..2025-07-31) [DISCARD: July 2025 divorces; not a birth input.] quote: "이혼 건수는 7826건으로 1.4% 감소했다."
  - p135 Divorces in South Korea, January-July 2025 cumulative = **50,794** divorces (2025-01-01..2025-07-31) [DISCARD: Jan-Jul 2025 divorces; not a birth input.] quote: "올해 1~7월 이혼 건수는 5만794건으로 5.1% 줄었다."
- `https://www.yna.co.kr/view/AKR20260527081300002?input=1195z` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period year 2015 does not appear in the page text or URL (likely mis-dated): 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d6 [shocks] Calendar and policy effects

Hypothesis: Policy incentives (baby bonuses), marriage trends, and calendar effects (lunar holidays, weekends) shift monthly births; identify measurable exposure for July 2026.

Queries issued by the searcher: Korea marriage registrations monthly 2025 statistics Korea 혼인건수; Statistics Korea monthly live births 2026 인구동향 출생아 수; 2026년 5월 인구동향 혼인 건수 20,368건 출생아 23,160명; 2025년 월별 혼인건수 10월 11월 12월 2025 혼인 통계 월별; Korea monthly live births 2026 인구동향 출생아 수; 혼인건수 2026 통계 월별; 2025년 7월 출생아 수 인구동향 2025년 8월 발표; 출생 장려금 2026 부모급여 첫만남이용권 확대 지원금; Korea monthly live births 2026 Statistics Korea 인구동향 월별 출생아 수; 혼인건수 2026년 통계청 월별; 2026년 5월 인구동향 출생아 수 혼인 건수 7월 29일 발표; 2025년 혼인 이혼 통계 월별 혼인건수 2025년 10월 11월 12월

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.khan.co.kr/article/202607291457001` -> **snapshot** (snapshot 20260730104343); points raw/verified 22/22
  - p136 Marriage registrations, South Korea, May 2026 = **20,368** marriage registration (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p137 Year-on-year change in marriage registrations, South Korea, May 2026 = **1,392** marriage registration (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p138 Year-on-year percent change in marriage registrations, South Korea, May 2026 = **6.4** % (2026-05-01..2026-05-31) [keep: ] quote: "지난 5월 혼인 건수는 2만368건으로 지난해 같은 달보다 1392건(6.4%) 감소했다."
  - p139 Divorce registrations, South Korea, May 2026 = **7,122** divorce registration (2026-05-01..2026-05-31) [DISCARD: May 2026 divorces; not a birth input.] quote: "5월 이혼 건수는 7122건으로 지난해 같은 달보다 290건(3.9%) 감소했다."
  - p140 Year-on-year change in divorce registrations, South Korea, May 2026 = **290** divorce registration (2026-05-01..2026-05-31) [DISCARD: May 2026 divorce change; not a birth input.] quote: "5월 이혼 건수는 7122건으로 지난해 같은 달보다 290건(3.9%) 감소했다."
  - p141 Year-on-year percent change in divorce registrations, South Korea, May 2026 = **3.9** % (2026-05-01..2026-05-31) [DISCARD: May 2026 divorce growth; not a birth input.] quote: "5월 이혼 건수는 7122건으로 지난해 같은 달보다 290건(3.9%) 감소했다."
  - p142 Live births, South Korea, May 2026 = **23,160** live birth (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p143 Year-on-year change in live births, South Korea, May 2026 = **2,781** live birth (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 absolute change p41.] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p144 Year-on-year percent change in live births, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 growth rate p42.] quote: "5월 출생아 수는 2만3160명으로 지난해 같은 달보다 2781명(13.6%) 증가했다."
  - p145 Consecutive months of increase in live births, South Korea, through May 2026 = **23** month (2024-07-01..2026-05-31) [DISCARD: Streak count; context only.] quote: "출생아 수는 2024년 7월 이후 23개월 연속 증가세를 이어갔다."
  - p146 Live births, South Korea, May 2019 (comparison for 7-year high) = **25,299** live birth (2019-05-01..2019-05-31) [DISCARD: May 2019 comparison level; context only.] quote: "5월 기준 출생아 수는 2019년(2만5299명) 이후 7년 만에 가장 많았다."
  - p147 Cumulative live births, South Korea, January-May 2026 = **122,694** live birth (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p148 Year-on-year change in cumulative live births, South Korea, January-May 2026 = **16,166** live birth (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p149 Year-on-year percent change in cumulative live births, South Korea, January-May  = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아 수는 12만2694명으로 지난해 같은 기간보다 1만6166명(15.2%) 늘었다."
  - p150 Cumulative live births, South Korea, January-May 2019 (comparison) = **134,433** live birth (2019-01-01..2019-05-31) [DISCARD: Jan-May 2019 cumulative; context only.] quote: "누적 출생아 수는 2019년(13만4433명) 이후 가장 많았으며, 증가 폭과 증가율 모두 통계 작성 이래 최대를 기록했다."
  - p151 Total fertility rate, South Korea, May 2026 = **0.85** live birth/woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 지난해 같은 달보다 0.10명 증가했다."
  - p152 Year-on-year change in total fertility rate, South Korea, May 2026 = **0.1** live birth/woman (2026-05-01..2026-05-31) [DISCARD: Duplicate TFR change.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 지난해 같은 달보다 0.10명 증가했다."
  - p153 Deaths, South Korea, May 2026 = **29,573** death (2026-05-01..2026-05-31) [DISCARD: Deaths May 2026; irrelevant.] quote: "5월 사망자 수는 2만9573명으로 1년 전보다 1091명(3.8%) 증가했다."
  - p154 Year-on-year change in deaths, South Korea, May 2026 = **1,091** death (2026-05-01..2026-05-31) [DISCARD: Deaths change; not a birth input.] quote: "5월 사망자 수는 2만9573명으로 1년 전보다 1091명(3.8%) 증가했다."
  - p155 Year-on-year percent change in deaths, South Korea, May 2026 = **3.8** % (2026-05-01..2026-05-31) [DISCARD: Deaths growth rate; irrelevant.] quote: "5월 사망자 수는 2만9573명으로 1년 전보다 1091명(3.8%) 증가했다."
  - p156 Natural decrease in population, South Korea, May 2026 = **6,413** person (2026-05-01..2026-05-31) [DISCARD: May natural decrease; not a birth input.] quote: "이에 따라 5월 인구는 6413명 자연 감소했다."
  - p157 Excess days with diurnal temperature range over 10 degrees, May 2026 vs prior ye = **3** as written "사흘", value check pending day (2026-05-01..2026-05-31) [DISCARD: Diurnal temperature-range days; speculative weather channel, not usable.] quote: "올해 5월에는 일교차가 10도 이상인 날이 지난해보다 사흘가량 많았고"
- `https://www.gov.kr/portal/ntnadmNews/4721687` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=294740&koreanId=294708` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/economy/2026/07/29/20260729500210` -> **snapshot** (snapshot 20260730174904); points raw/verified 19/17
  - p158 Live births in South Korea, May 2026 (monthly total) = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p159 Year-on-year increase in live births, South Korea, May 2026 = **2,781** live births (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 absolute change p41.] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p160 Year-on-year growth rate of live births, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 growth rate p42.] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p161 Cumulative live births, South Korea, January-May 2026 = **122,694** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아는 12만 2694명으로 1~5월 기준 7년 만에 가장 많았다."
  - p162 Cumulative live births, South Korea, January-May 2026 (headline rounded) = **120,000** live births (2026-01-01..2026-05-31) [DISCARD: Rounded '120,000' headline duplicate of the precise 122,694 cumulative figure; adds no information.] quote: "올해 5월까지 출생아 수가 12만명을 넘어서며 회복세를 이어갔다."
  - p163 Total fertility rate, South Korea, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p164 Year-on-year change in total fertility rate, South Korea, May 2026 = **0.1** live births per woman (2026-05-01..2026-05-31) [DISCARD: Duplicate TFR change.] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p165 Marriage registrations, South Korea, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [keep: ] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p166 Year-on-year change in marriage registrations, South Korea, May 2026 = **1,392** marriages (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 marriage change p137.] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p167 Year-on-year growth rate of marriage registrations, South Korea, May 2026 = **-6.4** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 marriage growth p138.] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p168 Reduction in reporting days in May 2026 due to Labour Day becoming a statutory h = **2** as written "이틀", value check pending days (2026-05-01..2026-05-31) [DISCARD: Reporting-day reduction for marriages; not a birth input.] quote: "데이터처는 지난 5월 1일 노동절이 법정공휴일로 지정되면서 신고 일수가 이틀 줄어든 영향이라고 분석했다."
  - p169 Consecutive months of marriage registration increase (adjusted), South Korea, th = **26** months (2024-03-01..2026-05-31) [DISCARD: Adjusted marriage streak; context only.] quote: "이를 고려하면 혼인 건수는 2024년 3월 이후 26개월 연속 증가세를 이어갔다."
  - p170 Natural population decrease, South Korea, May 2026 = **6,413** persons (2026-05-01..2026-05-31) [DISCARD: May natural decrease; not a birth input.] quote: "출생아 증가에도 사망자가 더 많아 인구는 6413명 자연 감소했다."
  - p171 Deaths, South Korea, May 2026 = **29,573** deaths (2026-05-01..2026-05-31) [DISCARD: Deaths May 2026; irrelevant.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p172 Year-on-year increase in deaths, South Korea, May 2026 = **1,091** deaths (2026-05-01..2026-05-31) [DISCARD: Deaths change; not a birth input.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p173 Year-on-year growth rate of deaths, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Same erroneous +13.6% deaths figure as p107; misleading duplicate.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p174 Consecutive months of live birth increase, South Korea, through May 2026 = **23** months (2024-07-01..2026-05-31) [DISCARD: Streak count; context only.] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
- `http://rkfka24.tistory.com/300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.datafocus.co.kr/news/articleView.html?idxno=1337` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy//materialView.do?num=284832&pg=&pp=&device=&search_txt=&topic=&type=J&depth1=A0000&depth2=A0600` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://studio.donga.com/NEWS/Society/article/all/20260729/134387353/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://47.newstomato.com/ReadNews.aspx?no=1308574` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.segye.com/view/20260325504288` -> **snapshot** (snapshot 20260326032017); points raw/verified 18/8
  - p175 Year-on-year increase in live births, South Korea, January 2026 = **2,817** live births (2026-01-01..2026-01-31) [keep: ] quote: "지난 1월 출생아 수는 2만6916명으로 전년 동월 대비 2817명(11.7%) 증가했다."
  - p176 Year-on-year growth rate of live births, South Korea, January 2026 = **11.7** % (2026-01-01..2026-01-31) [keep: ] quote: "이는 1년 전보다 11.7%(2817명) 늘어난 것으로, 1981년 관련 통계 작성 이래 지난해 1월(12.5%)에 이어 두 번째로 높은 수치다."
  - p177 Year-on-year increase in live births, South Korea, January 2011 (prior record) = **4,641** live births (2011-01-01..2011-01-31) [DISCARD: January 2011 comparison; context only.] quote: "1월 기준 전년 대비 증가 폭도 2011년(4641명) 이후 최대였다."
  - p178 Total fertility rate, South Korea, January 2026 = **0.99** live births per woman (2026-01-01..2026-01-31) [DISCARD: January 2026 TFR; derived rate, redundant with p1.] quote: "월별 합계출산율도 전년 대비 0.10명 늘어난 0.99명으로 집계돼 처음으로 0.9명을 넘겼다."
  - p179 Year-on-year change in total fertility rate, South Korea, January 2026 = **0.1** live births per woman (2026-01-01..2026-01-31) [DISCARD: January TFR change; redundant.] quote: "월별 합계출산율도 전년 대비 0.10명 늘어난 0.99명으로 집계돼 처음으로 0.9명을 넘겼다."
  - p180 Year-on-year increase in marriage registrations, South Korea, January 2026 = **2,489** marriages (2026-01-01..2026-01-31) [DISCARD: January 2026 marriages; not a July birth input.] quote: "1월 혼인 건수는 2만2640건으로 작년 동월보다 2489건(12.4%) 증가했다."
  - p181 Year-on-year growth rate of marriage registrations, South Korea, January 2026 = **12.4** % (2026-01-01..2026-01-31) [DISCARD: January 2026 marriage growth; not a July birth input.] quote: "1월 혼인 건수는 2만2640건으로 작년 동월보다 2489건(12.4%) 증가했다."
  - p182 Natural decrease (deaths minus births), South Korea, January 2026 = **5,539** person (2026-01-01..2026-01-31) [DISCARD: January natural decrease; not a birth input.] quote: "한편 올 1월 출생아 수보다 사망자 수(3만2454명)가 많아 5539명이 자연 감소했다."
- `https://re-www.yna.co.kr/view/AKR20260319092200002?section=economy/all&site=editors_picks_news_view` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (period year 2025 does not appear in the page text or URL (likely mis-dated): 4; number: more than one number in value_as_written: 1; scale word '万' not supported by quote or table header: 7)

### b1 [related_series] d2

Hypothesis: Resident-registration monthly births (행정안전부 주민등록 인구통계) for June and July 2026 would give a near-contemporaneous proxy for the KOSTAT occurrence-based July count, unlocking a yoy_scaling route (July 2026 registration births vs July 2025 registration births applied to p63).

Queries issued by the searcher: 행정안전부 주민등록 인구통계 월별 출생자 수 2026년; 주민등록 출생자 수 2026년 7월; 2026년 6월 주민등록 출생등록 24,000 출생신고 증가 행정안전부; 2025년 7월 주민등록 출생등록자 수 22,104; 행정안전부 주민등록 인구통계 월별 출생자 수; 주민등록 출생자 수 2026년 7월; 주민등록 출생등록 2026년 7월 2만4761명; 행정안전부 주민등록 인구통계 출생등록자 수 2026년 6월 전년동월대비; 행정안전부 주민등록 인구통계 월별 출생자 수; 주민등록 출생자 수 2026년 7월; 주민등록 출생등록 2026년 6월 행안부 출생자 수; jumin.mois.go.kr 주민등록 인구통계 월별 출생등록자수 2026

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])24,000(?!\\d|[.,]\\d)']; no pages fetched**


### b2 [own_history] d1

Hypothesis: KOSTAT June 2026 monthly births (released ~late July 2026) would extend the target's own monthly series to two months before July, tightening the series_auto YoY-growth anchor and revealing whether the double-digit growth is persisting into mid-2026.

Queries issued by the searcher: 2026년 6월 출생아 수 통계청 인구동향; 6월 출생아 수 2026 통계청 인구동향; 2026년 5월 인구동향 출생아 수 전년동월대비; 2025년 7월 출생아 수 2만 통계청 인구동향; 6월 출생아 수 2026 통계청 인구동향; 2026년 6월 출생아 수 2만명 인구동향; 2026년 5월 인구동향 출생아 수 전년동월대비 증가; 2025년 7월 출생아 수 2만명 인구동향 통계청; 6월 출생아 수 2026 통계청 인구동향; 2026년 6월 출생아 2만명 인구동향; 2026년 5월 인구동향 출생아 수 전년동월대비; 2025년 6월 출생아 수 1만9천명 인구동향 통계청

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.seoul.co.kr/news/economy/2026/07/29/20260729500210` -> **snapshot** (snapshot 20260730174904); points raw/verified 14/13
  - p183 National live births, South Korea, May 2026 = **23,160** live births (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p184 Year-on-year increase in national live births, South Korea, May 2026 vs May 2025 = **2,781** live births (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p185 Year-on-year growth rate of national live births, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [keep: ] quote: "5월 출생아 수는 2만 3160명으로 지난해 같은 달보다 2781명(13.6%) 증가해 23개월 연속 증가세를 이어갔다."
  - p186 Cumulative national live births, South Korea, January-May 2026 = **122,694** live births (2026-01-01..2026-05-31) [keep: ] quote: "올해 1~5월 누적 출생아는 12만 2694명으로 1~5월 기준 7년 만에 가장 많았다."
  - p187 Total fertility rate, South Korea, May 2026 = **0.85** live births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p188 Year-on-year change in total fertility rate, South Korea, May 2026 = **0.1** live births per woman (2026-05-01..2026-05-31) [keep: ] quote: "5월 합계출산율(여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수)은 0.85명으로 1년 전보다 0.10명 높아졌다."
  - p189 Marriage registrations, South Korea, May 2026 = **20,368** marriages (2026-05-01..2026-05-31) [keep: ] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p190 Year-on-year change in marriage registrations, South Korea, May 2026 = **1,392** marriages (2026-05-01..2026-05-31) [keep: ] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p191 Year-on-year growth rate of marriage registrations, South Korea, May 2026 = **-6.4** % (2026-05-01..2026-05-31) [keep: ] quote: "혼인 건수는 2만 368건으로 지난해 같은 달보다 1392건(-6.4%) 감소했다."
  - p192 Natural population decrease, South Korea, May 2026 = **6,413** persons (2026-05-01..2026-05-31) [DISCARD: Natural decrease May 2026; irrelevant to births level.] quote: "출생아 증가에도 사망자가 더 많아 인구는 6413명 자연 감소했다."
  - p193 Deaths, South Korea, May 2026 = **29,573** persons (2026-05-01..2026-05-31) [DISCARD: Deaths May 2026; irrelevant.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p194 Year-on-year increase in deaths, South Korea, May 2026 = **1,091** persons (2026-05-01..2026-05-31) [DISCARD: Deaths change May 2026; irrelevant.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
  - p195 Year-on-year growth rate of deaths, South Korea, May 2026 = **13.6** % (2026-05-01..2026-05-31) [DISCARD: Deaths growth May 2026; irrelevant.] quote: "5월 사망자 수는 2만 9573명으로 지난해 같은 달보다 1091명(13.6%) 증가해 통계 작성 이후 5월 기준 가장 많았다."
- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446612&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260826079400002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8646518` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4840361?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41845` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.yonhapnewstv.co.kr/news/AKR20260826105234xQm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20260826_0003762994` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1274698.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.sedaily.com/article/20083425` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [base_rates] d4

Hypothesis: A July seasonal factor (July births relative to the Jan-May monthly average) from 2023-2025 KOSTAT data would let the strong Jan-May 2026 cumulative (p75) be projected to July, providing an independent route that does not rely on the single July 2025 base.

Queries issued by the searcher: 월별 출생아 수 2023 2024 2025 통계청 인구동향; KOSTAT monthly live births 2025 July South Korea statistics; 2026년 6월 인구동향 출생아 수 통계청 발표; 2026년 1~5월 누계 출생아 수 전년동기대비 증가 통계청 인구동향; 월별 출생아 수 2023 2024 2025 통계청 인구동향; KOSTAT monthly births July 2025 live births statistics Korea; 2026년 5월 인구동향 출생아 수 누계 1~5월; KOSIS 월별 출생아 수 2023년 7월 19,085 2024년 7월 20,580; 월별 출생아 수 2023 2024 2025 통계청 인구동향; KOSTAT monthly live births July 2025 Korea statistics; 2026년 5월 인구동향 출생아 수 1~5월 누계; 2025년 12월 인구동향 월별 출생아 수 표 2023 2024 2025

- `https://www.korea.kr/common/download.do?fileId=198368729` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.joongang.co.kr/article/25369558` -> **snapshot** (snapshot 20260717192255); points raw/verified 27/3
  - p196 South Korea live births, July 2021 (comparison year for July high) = **22,364** live births (2021-07-01..2021-07-31) [keep: ] quote: "7월 기준으로는 2021년(2만2364명) 이후 가장 많은 수치다."
  - p197 South Korea live births, July 2023 (fourth-lowest July on record) = **19,085** live births (2023-07-01..2023-07-31) [keep: ] quote: "다만 1981년 통계 작성 이래로는 2023년(1만9085명)에 이어 역대 네 번째로 적은 기록이다."
  - p198 South Korea marriages, July 2016 (comparison year for July high) = **21,154** marriages (2016-07-01..2016-07-31) [DISCARD: July 2016 marriages; irrelevant to July 2026 births.] quote: "같은 달 기준으로는 2016년 7월(2만1154건) 이후 9년 만의 최고치다."
- `https://sri.kostat.go.kr/boardDownload.es?bid=204&list_no=435204&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.korea.kr/common/download.do?fileId=198066115` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.segye.com/newsView/20251029509310` -> **snapshot** (snapshot 20251109105652); points raw/verified 29/8
  - p199 South Korea cumulative live births, January to August 2025 = **10,708** live births (2025-01-01..2025-08-31) [DISCARD: Value 10,708 is internally inconsistent with a Jan-Aug cumulative (it is the YoY increase, not the level); unusable as a] quote: "작년 같은 기간보다 1만708명(6.8%) 증가했다."
  - p200 South Korea live births, August 2022 = **21,782** live births (2022-08-01..2022-08-31) [DISCARD: August 2022 level, not July; no role in a July 2026 estimate.] quote: "8월 출생아 수는 2022년(2만1천782명) 이후 3년 만에 가장 많았지만"
  - p201 South Korea live births, August 2023 = **18,974** live births (2023-08-01..2023-08-31) [DISCARD: August 2023 level, not July; no role.] quote: "2023년(1만8천974명), 2024년(2만103명)에 이어 세 번째로 낮은 수준이다."
  - p202 South Korea live births, August 2024 = **20,103** live births (2024-08-01..2024-08-31) [DISCARD: August 2024 level, not July; no role.] quote: "2023년(1만8천974명), 2024년(2만103명)에 이어 세 번째로 낮은 수준이다."
  - p203 South Korea marriages, August 2017 = **20,068** marriages (2017-08-01..2017-08-31) [DISCARD: August 2017 marriages; irrelevant.] quote: "같은 달 기준 2017년(2만68건) 이후 8년 만에 가장 많았다."
  - p204 South Korea divorces, August 2008 = **6,364** divorces (2008-08-01..2008-08-31) [DISCARD: 2008 divorces; irrelevant.] quote: "같은 달 기준 2008년(6천364건) 이후 17년 만에 최소치를 기록했다."
  - p205 Year-on-year percent change in South Korea cumulative live births, January to Au = **1.3** % (2015-01-01..2015-08-31) [DISCARD: 2015 cumulative growth rate; too old and not a July input.] quote: "1∼8월 출생아 수가 증가한 것은 2015년(1.3%) 이후 10년 만이며"
  - p206 Year-on-year percent change in South Korea cumulative live births, January to Au = **8.2** % (2007-01-01..2007-08-31) [DISCARD: 2007 cumulative growth rate; too old and not a July input.] quote: "'황금 돼지띠'였던 2007년(8.2%) 이후 가장 높은 증가율이다."
- `https://eiec.kdi.re.kr/policy/callDownload.do?num=278446&filenum=1&dtime=20260326042846` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1270472.html` -> **snapshot** (snapshot 20260808164127); points raw/verified 17/0
- `https://m-fr.yna.co.kr/view/AFR20250924002400884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532&listChk=list` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=F000801&idx_cd=F0008&freq=Y&period=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446612&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 62 (period year 2026 does not appear in the page text or URL (likely mis-dated): 60; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p17', 'p41', 'p78', 'p95', 'p142', 'p158'] All report the same KOSTAT May 2026 national live-birth count (23,160) and the same +2,781/+13.6% YoY change; they are repeated press renderings of one KOSTAT release, not independent measurements.
- corroborating: ['p43', 'p75', 'p76', 'p77', 'p98', 'p147', 'p148', 'p149', 'p161'] Same KOSTAT Jan-May 2026 cumulative figure (122,694; +16,166; +15.2%) repeated across outlets. One underlying source.
- corroborating: ['p44', 'p74', 'p99', 'p151', 'p163'] May 2026 TFR 0.85, +0.10 YoY, repeated; single KOSTAT origin.
- corroborating: ['p63', 'p108'] July 2025 national live births 21,803 from two outlets citing the same KOSTAT release; identical value confirms shared source.
- corroborating: ['p63', 'p109', 'p110'] July 2025 level, percent change and absolute change are internally consistent (21,803; +5.9%; +1,223).
- corroborating: ['p1', 'p2', 'p3', 'p175', 'p176'] January 2026 level 26,916 and +2,817/+11.7% repeated; same KOSTAT January release.
- corroborating: ['p31', 'p101', 'p136', 'p165'] May 2026 marriages 20,368, -1,392/-6.4%, repeated from one release.
- conflicting: ['p105', 'p107', 'p153', 'p155', 'p171', 'p173'] Deaths May 2026: +1,091 is quoted as both +13.6% (p107, p173) and +3.8% (p155); 1,091/28,482 ≈ 3.8%, so the 13.6% figures are a copy error. Deaths are not used in the birth estimate.
- conflicting: ['p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16'] These are Gyeongnam-province administrative figures (population ~3.3M), not national totals; they cannot be read as national births/deaths/migration and are irrelevant to a national July 2026 birth co
- corroborating: ['p63', 'p119'] July 2025 TFR 0.80 and level 21,803 come from the same release; TFR is a derived rate, useful only as context.
- corroborating: ['p81', 'p82'] 2025 annual births 254,457 and a 2026 forecast of 'high 200,000s' are consistent with the strong Jan-May 2026 pace; forecast is context, not a direct July input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p3', 'p175', 'p176'] Same January 2026 KOSTAT release reported by multiple outlets; one underlying measurement, not independent confirmation.
- corroborating: ['p17', 'p18', 'p41', 'p42', 'p78', 'p95', 'p142', 'p158', 'p183', 'p184', 'p185'] May 2026 national births 23,160 and +13.6% YoY, all from the same KOSTAT May release; redundant copies.
- corroborating: ['p43', 'p75', 'p76', 'p77', 'p98', 'p147', 'p148', 'p149', 'p161', 'p186'] Jan-May 2026 cumulative 122,694, +15.2% YoY; same release, redundant copies.
- corroborating: ['p63', 'p108', 'p109', 'p110'] July 2025 births 21,803, +5.9% (+1,223); same KOSTAT July 2025 release.
- contextual: ['p196', 'p197'] July 2021 (22,364) and July 2023 (19,085) July levels bracket recent July history; useful for seasonal/level context, not direct substitution.
- corroborating: ['p31', 'p32', 'p101', 'p136', 'p137', 'p138', 'p165', 'p189', 'p190', 'p191'] May 2026 marriages 20,368, -6.4% YoY; same release. Marriage decline is a mild headwind for births ~9-12 months later, not a July 2026 driver.
- corroborating: ['p44', 'p74', 'p99', 'p151', 'p163', 'p187', 'p188'] May 2026 TFR 0.85, +0.10 YoY; consistent with the birth surge but a rate, not a count.
- contextual: ['p81', 'p82'] 2025 annual 254,457 and a loose 2026 forecast of 'high 200,000s'; weak constraint, not a monthly input.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 YoY growth factor vs July 2025 | 1.12 | 1.02..1.24 | 1.006..1.257 (widened) | dimensionless | m1 (m1) | Jan-May 2026 cumulative births are +15.2% YoY (p75/p77) and May alone +13.6% (p17/p18); July 2025 was already a strong month (+5.9%, p109), so the July 2026 YoY factor should sit somewhat below the recent run-rate. Centered near 1.12 with a wide band reflecting possible fading of the surge. | The recent double-digit YoY birth growth persists into July 2026, possibly moderating because July 2025 was a high base. | Evidence that June/July 2026 YoY growth collapsed toward zero or turned negative, or that the July 2025 base was revised materially. |
| a2 | July seasonal factor relative to Jan-May 2026 monthly average | 0.95 | 0.88..1.03 | 0.6732..1.346 (widened) | dimensionless | unused | July births in Korea are typically slightly below the Jan-May average (July 2025 21,803 vs a 2025 monthly average near 21,200; July 2021 22,364 and July 2023 19,085 bracket the seasonal position). A factor just under 1 with a modest band is consistent with recent July shares. | The 2026 monthly pattern retains the usual Korean seasonal shape with July modestly below the Jan-May average. | Evidence that 2026 July births were unusually high or low relative to the Jan-May run-rate (e.g., a strong July registration surge). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 24,515 | ['p63'] / ['a1'] | [] |  | 1.00 | B1 (only block) |  |
| m2 | formula_mc | n/a | ['p75'] / ['a2'] | [] |  | 0.00 |  | formula: numeric constant 5 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the unit |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p63 * a1; Monte Carlo P10 to P90 19,826 to 30,407; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 1 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 24,515 (width x/÷1.38, no error evidence, code's default width). Estimate = the only block.
- Interval: one block, so the interval is that block's own width (x/÷1.38).

Result: central **24,515** person, 80% interval [17,794, 33,773] person, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule single_block, weight on methods that use assumptions 1.00

Unit of the estimate: person (live births; total for 2026-07-01 to 2026-07-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as first published in Statistics Korea's monthly Population Trends release, is 24,515 person (80% model-based interval 17,794 to 33,773 person).

Main evidence: the estimate anchors on the observed July 2025 level of 21,803 live births and applies an assumed July 2026 year-over-year factor of 1.12 (range 1.006 to 1.257). That factor is grounded in the observed January–May 2026 cumulative of 122,694 live births, which implies a recent run-rate above the assumed July factor because July 2025 was itself a strong base.

Observed: the July 2025 level and the 2026 cumulative. Assumed: the YoY factor, including its wide band. Only one method block was usable (1 method), so the estimate is that block's value; the interval is conditional on the assumption, not a demonstrated accuracy guarantee.

Key risk: if the 2026 surge fades by July, the estimate is too high. Better evidence would be June 2026 monthly births and any July registration data.

Unit of the estimate: person (live births; total for 2026-07-01 to 2026-07-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 YoY growth factor vs July 2025: 1.12 dimensionless, range 1.006 to 1.257 (range widened by code); used by m1. Overturned by: Evidence that June/July 2026 YoY growth collapsed toward zero or turned negative, or that the July 2025 base was revised materially.

Method details (computed by code):
- m1 formula_mc: p63 * a1; Monte Carlo P10 to P90 19,826 to 30,407; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 1 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 24,515 (width x/÷1.38, no error evidence, code's default width). Estimate = the only block.
- Interval: one block, so the interval is that block's own width (x/÷1.38).

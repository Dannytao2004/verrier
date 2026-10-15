# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), via the monthly Population Trends / Vital Statistics release

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [own_history] Statistics Korea monthly vital statistics time series

Hypothesis: July 2026 births can be projected from the same month in prior years plus recent monthly momentum. July is typically a high-birth month in Korea; the year-over-year change in recent months constrains the level.

Queries issued by the searcher: Statistics Korea monthly live births July 2025 population trends; South Korea monthly births 2025 statistics KOSTAT; 2026년 5월 인구동향 출생아 수 국가데이터처; 2023년 7월 출생아 수 1만8904명 인구동향

- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.koreatimes.co.kr/southkorea/society/20250924/koreas-childbirths-rise-for-13th-consecutive-month-in-july-data` -> **snapshot** (snapshot 20250924045410); points raw/verified 15/15
  - p1 Live births in South Korea, July (current year of report) = **21,803** live births (persons) (2026-07-01..2026-07-31) [keep: ] quote: "A total of 21,803 babies were born in July, up 5.9 percent from 20,580 babies born a year earlier, according to the data compiled by Statistics Korea."
  - p2 Live births in South Korea, July of prior year = **20,580** live births (persons) (2025-07-01..2025-07-31) [keep: ] quote: "A total of 21,803 babies were born in July, up 5.9 percent from 20,580 babies born a year earlier, according to the data compiled by Statistics Korea."
  - p3 Year-over-year change in July live births, South Korea = **5.9** percent (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of the +5.9% already carried by p1/p2; adds no independent information.] quote: "A total of 21,803 babies were born in July, up 5.9 percent from 20,580 babies born a year earlier, according to the data compiled by Statistics Korea."
  - p4 Cumulative live births, South Korea, January–July = **147,804** live births (persons) (2026-01-01..2026-07-31) [keep: ] quote: "A total of 147,804 babies were born between January and July. The figure represents a 7.2 percent increase from the same period last year, the highest growth rate since 1981."
  - p5 Year-over-year change in cumulative January–July live births, South Korea = **7.2** percent (2026-01-01..2026-07-31) [DISCARD: Redundant restatement of the +7.2% cumulative change already in p4/p28.] quote: "A total of 147,804 babies were born between January and July. The figure represents a 7.2 percent increase from the same period last year, the highest growth rate since 1981."
  - p6 Total fertility rate, South Korea, July = **0.8** children per woman (2026-07-01..2026-07-31) [DISCARD: July 2025 TFR is a rate, not a count; it cannot enter a count formula without a female-population denominator that no ke] quote: "The country's total fertility rate, the average number of children a woman is expected to have in her lifetime, rose 0.04 from a year earlier to 0.8 in July."
  - p7 Year-over-year change in total fertility rate, South Korea, July = **0.04** children per woman (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of the TFR change in p6/p31; no independent information.] quote: "The country's total fertility rate, the average number of children a woman is expected to have in her lifetime, rose 0.04 from a year earlier to 0.8 in July."
  - p8 Marriages in South Korea, July = **20,394** marriages (2026-07-01..2026-07-31) [keep: ] quote: "The number of marriages in July climbed 8.4 percent on-year to 20,394, marking the 16th consecutive month of growth."
  - p9 Year-over-year change in July marriages, South Korea = **8.4** percent (2026-07-01..2026-07-31) [DISCARD: Redundant restatement of the +8.4% July marriage change in p8.] quote: "The number of marriages in July climbed 8.4 percent on-year to 20,394, marking the 16th consecutive month of growth."
  - p10 Marriages in South Korea, July 2016 = **21,154** marriages (2016-07-01..2016-07-31) [keep: ] quote: "It also marked the largest number for any July since 2016, when the figure came to 21,154."
  - p11 Deaths in South Korea, July = **27,979** deaths (persons) (2026-07-01..2026-07-31) [DISCARD: July 2025 deaths; not an input to a birth estimate and its only role (arithmetic consistency with p1) is already noted i] quote: "Meanwhile, the number of deaths in July dropped 0.7 percent from a year earlier to 27,979, resulting in a natural population decline of 6,175."
  - p12 Year-over-year change in July deaths, South Korea = **0.7** percent (2026-07-01..2026-07-31) [DISCARD: Redundant y/y restatement of p11.] quote: "Meanwhile, the number of deaths in July dropped 0.7 percent from a year earlier to 27,979, resulting in a natural population decline of 6,175."
  - p13 Natural population decline, South Korea, July = **6,175** persons (2026-07-01..2026-07-31) [DISCARD: Natural decline is a derived difference of births and deaths; adds no independent information about births.] quote: "Meanwhile, the number of deaths in July dropped 0.7 percent from a year earlier to 27,979, resulting in a natural population decline of 6,175."
  - p14 Divorces in South Korea, July = **7,826** divorces (2026-07-01..2026-07-31) [DISCARD: Divorces have no established quantitative link to same-month births at the precision needed here.] quote: "The number of divorces fell 1.4 percent on-year to 7,826 in July, the data also showed."
  - p15 Year-over-year change in July divorces, South Korea = **1.4** percent (2026-07-01..2026-07-31) [DISCARD: Redundant y/y restatement of p14.] quote: "The number of divorces fell 1.4 percent on-year to 7,826 in July, the data also showed."
- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4657824` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Year-to-date births and recent monthly changes

Hypothesis: If year-to-date births for 2026 (January–June) are available, July can be estimated by applying the historical July-to-June ratio or the recent month-over-month growth rate.

Queries issued by the searcher: South Korea births January-June 2026 cumulative live births KOSTAT; 2026년 6월 출생아 수 통계청 인구동향; 2026년 5월 인구동향 출생아 수 누적 1~5월; "5월" 출생아 수 2026 국가데이터처 인구동향 발표 7월; 2025년 7월 출생아 수 2만명 인구동향 통계청; 2026년 5월 인구동향 보도자료 국가데이터처 출생아 2만3160명 누적 12만2694명

- `https://www.yna.co.kr/view/PYH20260826116500013?site=yna_usernews_news_view` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/PYH20260826116200013?input=1196m` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cb.yna.co.kr/gate/big5/cn.yna.co.kr/view/ACK20260826002100881?section=society/index` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tvchosun.com/site/data/html_dir/2026/08/26/2026082690132.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Marriage registrations as a leading indicator of births

Hypothesis: In South Korea, first births are strongly associated with marriage, typically 1–2 years earlier. Marriage registrations in mid-2024 to mid-2025 can help predict July 2026 births, especially if recent marriage trends have shifted.

Queries issued by the searcher: South Korea monthly marriage registrations 2024 2025 statistics; 혼인 건수 월별 2025 통계; 2026년 인구동향 출생아 수 혼인건수 6월; "2026년" 인구동향 5월 출생아 수 증가 혼인

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.newstomato.com/ReadNews.aspx?no=72160` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.newstomato.com/ReadNews.aspx?no=90816` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cj.sina.com.cn/articles/view/1649173367/624c637704001fyhc?froms=ggmp&` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [administrative] Birth registration records and resident registration

Hypothesis: Births are registered with local governments; the number of birth registrations in July 2026 (or around that month) may be available from administrative sources before the official vital statistics release, though registration timing can lag occurrence.

Queries issued by the searcher: 행정안전부 주민등록 출생아 수 2026년 7월; South Korea birth registration July 2026 monthly births; 행정안전부 주민등록 인구통계 2026년 7월 출생자 수; 주민등록 출생아 수 7월 2026 증가 주민등록통계

- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=447111` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260923077000002?section=economy/all&site=topnews02` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.afpbb.com/articles/-/3654683?cx_amp=all&act=all` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [base_rates] Seasonal adjustment factors for monthly births

Hypothesis: The ratio of July births to the annual total or to adjacent months is stable enough to use as a seasonal factor. This allows converting an annual estimate or a year-to-date total into a July figure.

Queries issued by the searcher: South Korea monthly live births 2024 2025 Statistics Korea monthly birth data; 월별 출생아 수 2024 2025 통계청; South Korea monthly births July 2025 7월 출생아 수 2만 2025년 인구동향; 통계청 인구동향 월별 출생아 수 2023 2024 표 1월 2월 3월 7월; 출생아 수 월별 2019 2020 2021 2022 2023 2024 2025 7월 비중 연간; namu.wiki 대한민국 출산율 상세통계 7월 출생아 수 비중

- `https://mods.go.kr/boardDownload.es?bid=11749&list_no=437460&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jinwanbaoepaper.enorth.com.cn/jwb/html/2025-12/26/content_87652_2976405.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://worldnews.net.ph/post/207182` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tvchosun.com/site/data/html_dir/2025/12/24/2025122490228.html` -> **snapshot** (snapshot 20251229141803); points raw/verified 15/10
  - p16 South Korea year-on-year increase in monthly live births, October 2025 = **2.1** % (2025-10-01..2025-10-31) [keep: ] quote: "지난 10월 출생아 수는 2만 646명으로 1년 전보다 2.1%(426명) 증가한 것으로 나타났다."
  - p17 South Korea year-on-year increase in monthly live births, October 2025 (persons) = **426** live births (persons) (2025-10-01..2025-10-31) [DISCARD: Redundant restatement of the +426 person change already in p16.] quote: "지난 10월 출생아 수는 2만 646명으로 1년 전보다 2.1%(426명) 증가한 것으로 나타났다."
  - p18 South Korea year-on-year change in cumulative live births, January–October 2025 = **6.1** % (2025-01-01..2025-10-31) [keep: ] quote: "1월부터 10월까지의 누적 출생아 수는 20만 5,257명으로, 지난해 같은 기간보다 6.1% 늘었다."
  - p19 South Korea year-on-year increase rate in monthly live births, September 2025 = **9.9** % (2025-09-01..2025-09-30) [keep: ] quote: "지난 9월 9.9%에 달했던 출생아 수 증가율은 10월 들어 2%대로 내려앉으며 지난 3월(0.8%) 이후 가장 낮은 수준을 보였다."
  - p20 South Korea year-on-year increase rate in monthly live births, March 2025 = **0.8** % (2025-03-01..2025-03-31) [keep: ] quote: "지난 9월 9.9%에 달했던 출생아 수 증가율은 10월 들어 2%대로 내려앉으며 지난 3월(0.8%) 이후 가장 낮은 수준을 보였다."
  - p21 South Korea year-on-year increase rate in monthly live births, October 2024 = **8.2** % (2024-10-01..2024-10-31) [keep: ] quote: "이는 지난해 10월 출생아 수가 전년 동월 대비 8.2% 급증했던 데 따른 기저효과가 작용한 결과로 풀이된다."
  - p22 South Korea year-on-year increase in monthly marriages, October 2025 = **18.2** % (2025-10-01..2025-10-31) [keep: ] quote: "10월 혼인 건수는 1만 6,923건으로 전년 동월 대비 18.2%(2,600건) 급증했다."
  - p23 South Korea year-on-year increase in monthly marriages, October 2025 (cases) = **2,600** marriages (cases) (2025-10-01..2025-10-31) [DISCARD: Redundant restatement of the +2,600 marriage change already in p22.] quote: "10월 혼인 건수는 1만 6,923건으로 전년 동월 대비 18.2%(2,600건) 급증했다."
  - p24 South Korea year-on-year increase rate in monthly marriages, April 2025 (peak) = **24.6** % (2025-04-01..2025-04-30) [keep: ] quote: "혼인 건수는 올해 4월(24.6%) 정점을 찍은 뒤 등락을 거듭하다 10월 들어 다시 증가 폭을 키웠다."
  - p25 South Korea year-on-year increase in monthly deaths, October 2025 = **4.2** % (2025-10-01..2025-10-31) [DISCARD: October 2025 deaths; irrelevant to the July 2026 birth count.] quote: "10월 사망자 수는 3만 1,586명으로 1년 전보다 4.2%(1,273명) 증가했다."
- dropped by code checks: 5 (number: more than one number in value_as_written: 4; value_as_written not in quote as a whole number: 1)

### d6 [related_series] Population and women of childbearing age

Hypothesis: Births equal the number of women of childbearing age multiplied by age-specific fertility rates. Changes in the size and age structure of the female population aged 15–49, especially 25–39, constrain the expected number of births.

Queries issued by the searcher: Statistics Korea female population by age 2025 가임여성 인구; South Korea age-specific fertility rate 2024 2025 KOSTAT; 2026년 5월 출생아 수 인구동향 통계청 월간; 2026년 6월 출생아 수 전년동월대비 인구동향

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=H000202&idx_cd=H0002&freq=Y&period=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=298549&koreanId=298547` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6245639` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Official and private forecasts for 2026 births

Hypothesis: Statistics Korea or research institutes may publish monthly or annual birth projections for 2026. These forecasts can anchor the July 2026 estimate, though they may be based on models rather than observed data.

Queries issued by the searcher: South Korea 2026 birth forecast Statistics Korea; 2026년 출생아 수 전망 통계청; 2025년 7월 출생아 수 인구동향 2만명; 2026년 6월 인구동향 출생아 2만3111명 상반기 14만5804명

- `https://newspim.com/news/view/20250924000454` -> **snapshot** (snapshot 20251126043735); points raw/verified 15/9
  - p26 South Korea live births, July 2025, year-on-year increase = **1,223** live births (persons) (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월보다 1223명(5.9%) 증가했다."
  - p27 South Korea live births, July 2025, year-on-year growth rate = **5.9** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p3/p26; same underlying KOSTAT measurement.] quote: "지난 7월 출생아 수는 2만1803명으로 전년 동월보다 1223명(5.9%) 증가했다."
  - p28 South Korea live births, January–July 2025 cumulative, year-on-year increase = **9,944** live births (persons) (2025-01-01..2025-07-31) [keep: ] quote: "올해 1~7월 누계 출생아 수는 14만7804명으로 전년 동기보다 9944명(7.2%) 늘었다."
  - p29 South Korea live births, January–July 2025 cumulative, year-on-year growth rate = **7.2** % (2025-01-01..2025-07-31) [DISCARD: Duplicate of p5/p28; same underlying KOSTAT measurement.] quote: "올해 1~7월 누계 출생아 수는 14만7804명으로 전년 동기보다 9944명(7.2%) 늘었다."
  - p30 South Korea total fertility rate, July 2025 = **0.8** children per woman (2025-07-01..2025-07-31) [keep: ] quote: "7월 합계출산율은 0.80명으로 전년 동월 대비 0.04명 증가했다."
  - p31 South Korea total fertility rate, July 2025, year-on-year change = **0.04** children per woman (2025-07-01..2025-07-31) [DISCARD: Duplicate of p7/p30; same underlying KOSTAT measurement.] quote: "7월 합계출산율은 0.80명으로 전년 동월 대비 0.04명 증가했다."
  - p32 South Korea live births, Gyeonggi province, July 2025 = **6,539** live births (persons) (2025-07-01..2025-07-31) [DISCARD: Provincial July 2025 births; sub-national components are not needed once the national total p1 is kept, and summing them] quote: "출생아가 가장 많이 태어난 지역은 ▲경기(6539명) ▲서울(3938명) ▲인천(1488명) ▲부산(1218명) ▲경남(1179명) 등으로 집계됐다."
  - p33 South Korea live births, Seoul, July 2025 = **3,938** live births (persons) (2025-07-01..2025-07-31) [DISCARD: Seoul July 2025 births; sub-national component, redundant with p1.] quote: "출생아가 가장 많이 태어난 지역은 ▲경기(6539명) ▲서울(3938명) ▲인천(1488명) ▲부산(1218명) ▲경남(1179명) 등으로 집계됐다."
  - p34 South Korea live births, Sejong, July 2025 (lowest) = **240** live births (persons) (2025-07-01..2025-07-31) [DISCARD: Sejong July 2025 births; sub-national component, redundant with p1.] quote: "가장 적게 태어난 지역은 세종(240명)이었다."
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.etoday.co.kr/news/view/2610060?trc=main_top_sub` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://koreabizwire.com/birth-rate-poised-to-return-to-0-9-after-seven-years?ckattempt=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (number: more than one number in value_as_written: 6)

### d8 [shocks] Policy and calendar effects on births

Hypothesis: Government pronatalist policies, changes in parental leave, or one-off events (e.g., a temporary baby bonus) could shift births in 2026. Also, the timing of the 2026 Lunar New Year and other holidays may affect birth seasonality.

Queries issued by the searcher: South Korea birth incentive policy 2025 2026 pronatalist effect births; 저출산 대책 2026 출생아 월별 통계; 2026년 6월 인구동향 출생아 수 국가데이터처 발표; 월별 출생아 수 2025년 7월 출생아 통계청 인구동향

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4840361?srchOrgCd` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indonesian.korea.net/NewsFocus/policies/view?articleId=291475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.swnews.kr/news/articleView.html?idxno=90937` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] KOSTAT monthly birth series, 2015–2025

Hypothesis: A complete monthly July birth series (2015–2025) would let series_naive and yoy_scaling be backtested on the actual July seasonal level, anchoring the 2026 July estimate rather than relying on a single 2025 July value. This is the missing input that completes the primary d1 route.

Queries issued by the searcher: Statistics Korea monthly live births July 2023 2024 인구동향 출생아 수; KOSTAT 국가통계포털 월별 출생아 수 2015 2016 2017 2018 2019; 2025년 7월 인구동향 출생아 수 통계청; kosis.kr DT_1B8000G 월별 출생아 수 인구동향

- `https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B8000G&conn_path=I2` -> **snapshot** (snapshot 20240722121002); points raw/verified 0/0
- `https://sri.kostat.go.kr/boardDownload.es?bid=204&list_no=435204&seq=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jibs.co.kr/news/articles/articlesDetail/41409` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Marriage-to-birth lag structure

Hypothesis: If the July 2026 birth level is driven by marriages 1–2 years earlier, a quantified lag distribution (share of births occurring 12–24 months after marriage) would convert the strong 2024–2025 marriage surge (p8, p22, p24) into a July 2026 birth increment. This unlocks the d3 route and would resolve whether the 2025 birth recovery continues into mid-2026.

Queries issued by the searcher: KOSTAT 혼인 후 첫 출생까지 기간 통계; marriage to first birth interval Korea statistics months; 출생아 수 혼인 건수 상관관계 시차 1년 2년; Statistics Korea birth by duration of marriage first birth table

- `https://www.kostat.go.kr/boardDownload.es?bid=11815&list_no=442387&seq=3` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://researcher.hf.go.kr/researcher/sub04/sub05_3.do?mode=download&articleNo=592769&attachNo=91412` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://repository.kihasa.re.kr/en/bitstream/201002/34284/1/%ec%97%b0%ea%b5%ac%eb%b3%b4%ea%b3%a0%ec%84%9c%202019-21.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.joongang.co.kr/article/25323712` -> **snapshot** (snapshot 20260717193935); points raw/verified 15/10
  - p35 Year-on-year increase in South Korea live births, January 2026 vs January 2025 = **2,486** live births (persons) (2026-01-01..2026-01-31) [keep: ] quote: "올 1월 출생아 수는 2만3947명으로 전년 같은 달보다 2486명(11.6%) 많았다."
  - p36 Year-on-year percent increase in South Korea live births, January 2026 vs Januar = **11.6** % (2026-01-01..2026-01-31) [keep: ] quote: "올 1월 출생아 수는 2만3947명으로 전년 같은 달보다 2486명(11.6%) 많았다."
  - p37 Year-on-year percent change in South Korea annual live births, 2025 vs 2023 = **3.6** % (2025-01-01..2025-12-31) [DISCARD: 2025 annual total vs 2023 is a different comparison base and period; the 2025 level is already available through the mon] quote: "덕분에 지난해 출생아 수는 23만8343명으로 2023년보다 3.6% 늘었다."
  - p38 Year-on-year percent increase in South Korea marriages, January 2026 vs January  = **0.7** % (2026-01-01..2026-01-31) [keep: ] quote: "출생아 수에 직접적인 영향을 주는 혼인 건수는 1월 2만153건으로 1년 전보다 0.7% 증가했다."
  - p39 South Korea total fertility rate, January 2026 = **0.88** children per woman (2026-01-01..2026-01-31) [DISCARD: January 2026 TFR is a rate, not a count, and no female-population denominator is available to convert it.] quote: "여성 1명이 평생 낳을 아이 수를 뜻하는 합계출산율은 0.88명으로 전년 동월 대비 0.08명 증가했다."
  - p40 Year-on-year change in South Korea total fertility rate, January 2026 vs January = **0.08** children per woman (2026-01-01..2026-01-31) [DISCARD: Redundant y/y restatement of p39.] quote: "여성 1명이 평생 낳을 아이 수를 뜻하는 합계출산율은 0.88명으로 전년 동월 대비 0.08명 증가했다."
  - p41 South Korea age-specific fertility rate, women aged 30-34, January 2026 (births  = **81.1** births per 1,000 women aged 30-34 (2026-01-01..2026-01-31) [DISCARD: January 2026 ASFR for ages 30-34 is a rate; without the corresponding female population it cannot produce a count.] quote: "특히 30~34세와 35~39세 출산율(해당 연령대 여자 인구 1000명당 태어난 아이 수)은 각각 81.1명, 56.6명으로 전년 동월 대비 8.0명, 9.3명씩 급증했다."
  - p42 South Korea age-specific fertility rate, women aged 35-39, January 2026 (births  = **56.6** births per 1,000 women aged 35-39 (2026-01-01..2026-01-31) [DISCARD: January 2026 ASFR for ages 35-39; same limitation as p41.] quote: "특히 30~34세와 35~39세 출산율(해당 연령대 여자 인구 1000명당 태어난 아이 수)은 각각 81.1명, 56.6명으로 전년 동월 대비 8.0명, 9.3명씩 급증했다."
  - p43 Year-on-year increase in South Korea age-specific fertility rate, women aged 30- = **8** births per 1,000 women aged 30-34 (2026-01-01..2026-01-31) [DISCARD: Redundant y/y restatement of p41.] quote: "특히 30~34세와 35~39세 출산율(해당 연령대 여자 인구 1000명당 태어난 아이 수)은 각각 81.1명, 56.6명으로 전년 동월 대비 8.0명, 9.3명씩 급증했다."
  - p44 Year-on-year increase in South Korea age-specific fertility rate, women aged 35- = **9.3** births per 1,000 women aged 35-39 (2026-01-01..2026-01-31) [DISCARD: Redundant y/y restatement of p42.] quote: "특히 30~34세와 35~39세 출산율(해당 연령대 여자 인구 1000명당 태어난 아이 수)은 각각 81.1명, 56.6명으로 전년 동월 대비 8.0명, 9.3명씩 급증했다."
- dropped by code checks: 5 (number: more than one number in value_as_written: 4; period_end missing or unparseable: 1)

### b3 [administrative] Provisional registration counts

Hypothesis: Resident registration or 주민등록 birth registration counts for July 2026 (available before the official vital-statistics release) would provide a near-contemporaneous level check on the target, resolving the largest uncertainty — whether the 2025 momentum (p16–p21) persisted into mid-2026.

Queries issued by the searcher: 주민등록 출생신고 2026년 7월; KOSTAT 잠정 출생아 수 2026년 7월 인구동향; 행정안전부 주민등록 인구통계 2026년 7월 출생자 수; "2026년 7월" 주민등록人口 출생신고 증가

- `https://mods.go.kr/board.es?mid=a10301020300&bid=204&act=view&list_no=447111` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260923077000002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p26', 'p27'] All describe the same July 2025 KOSTAT release: 21,803 July-2025 births, 20,580 July-2024 births, +1,223 (+5.9%). p1/p2/p3 and p26/p27 are duplicate reports of one underlying measurement, not independ
- corroborating: ['p4', 'p5', 'p28', 'p29'] Same KOSTAT release: Jan–Jul 2025 cumulative 147,804 births, +9,944 (+7.2%) vs Jan–Jul 2024. Again a 2025 vintage, duplicated across two outlets.
- corroborating: ['p6', 'p7', 'p30', 'p31'] July 2025 period TFR 0.80, +0.04 y/y — same release, duplicate reporting. TFR is a rate, not a count, so it cannot substitute for the birth level.
- corroborating: ['p8', 'p9', 'p10'] July 2025 marriages 20,394, +8.4% y/y, largest July since 2016 (21,154). Same release; p10 supplies the historical July marriage benchmark.
- corroborating: ['p11', 'p12', 'p13'] July 2025 deaths 27,979, −0.7% y/y, natural decline 6,175. Internally consistent (27,979 − 21,803 = 6,176 ≈ 6,175) and confirms the 21,803 birth figure.
- corroborating: ['p14', 'p15'] July 2025 divorces 7,826, −1.4% y/y. Same release; weak relevance to births.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21'] 2025 monthly birth momentum from KOSTAT releases: Oct-2025 +2.1% (+426), Sep-2025 +9.9%, Mar-2025 +0.8%, Oct-2024 +8.2% base effect, Jan–Oct 2025 cumulative +6.1%. Together they show a decelerating bu
- corroborating: ['p22', 'p23', 'p24'] 2025 marriage momentum: Oct-2025 +18.2% (+2,600), Apr-2025 peak +24.6%. Supports the marriage-led birth recovery channel (d3).
- corroborating: ['p25'] Oct-2025 deaths +4.2% (+1,273); consistent with the mortality series used in the same releases.
- corroborating: ['p32', 'p33', 'p34'] July 2025 regional breakdown (Gyeonggi 6,539; Seoul 3,938; Sejong 240) — same release, sums toward the national total; useful only as a coverage check.
- conflicting: ['p1', 'p4'] Apparent conflict is only a labeling artifact: p1–p15 carry 2026 period labels but 2025 snapshot dates and 2025 values. The true July 2026 figure is unpublished at the 2026-08-23 cutoff, so no kept po
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p26', 'p27'] All describe the same July 2025 KOSTAT vital-statistics release: 21,803 July 2025 births, +1,223 (+5.9%) vs July 2024's 20,580. p1/p2/p3 and p26/p27 are two outlets reporting one underlying measuremen
- corroborating: ['p4', 'p5', 'p28', 'p29'] Same release: Jan-Jul 2025 cumulative births 147,804, +9,944 (+7.2%) vs Jan-Jul 2024. Again a 2025 vintage, not 2026. Useful as the denominator base for a July-share-of-year or July-to-June ratio rout
- corroborating: ['p6', 'p7', 'p30', 'p31'] July 2025 TFR 0.80, +0.04 y/y. Same release and same vintage as p1-p5; a level indicator, not a count, so it cannot substitute for the birth count.
- corroborating: ['p8', 'p9', 'p10'] July 2025 marriages 20,394, +8.4% y/y, largest July since 2016 (21,154). Same release vintage. Relevant only through the marriage-to-birth lag route.
- corroborating: ['p11', 'p12', 'p13', 'p14', 'p15'] July 2025 deaths 27,979 (-0.7%), natural decline 6,175, divorces 7,826 (-1.4%). Internally consistent (27,979 - 21,803 = 6,176, rounding), which confirms the 21,803 birth figure is the same release's 
- corroborating: ['p16', 'p17', 'p19', 'p20', 'p21'] Monthly y/y birth growth rates through 2025: Oct 2025 +2.1% (+426), Sep 2025 +9.9%, Mar 2025 +0.8%, with Oct 2024 +8.2% as the base effect. Together they show a decelerating but still positive 2025 mo
- corroborating: ['p18'] Jan-Oct 2025 cumulative 205,257, +6.1% y/y — consistent with the +7.2% Jan-Jul figure (p4/p28) and the monthly deceleration in p16/p19.
- corroborating: ['p22', 'p23', 'p24'] Marriage surge: Oct 2025 +18.2% (+2,600), April 2025 peak +24.6%. Same underlying KOSTAT marriage series as p8/p9 but different months; supports the d3 lag route.
- corroborating: ['p35', 'p36', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] January 2026 release (snapshot 2026-07-17): births 23,947, +2,486 (+11.6%); marriages +0.7%; TFR 0.88 (+0.08); ASFR 30-34 = 81.1 (+8.0) and 35-39 = 56.6 (+9.3). This is the only genuinely 2026-vintage
- corroborating: ['p37'] 2025 annual births 238,343, +3.6% vs 2023 — a different comparison base (2023, not 2024) and a different period (annual), so it is context for the level, not a direct y/y signal.
- corroborating: ['p32', 'p33', 'p34'] July 2025 regional breakdown (Gyeonggi 6,539; Seoul 3,938; Sejong 240). Same release; useful only as a scope check that the national total is domestic and regionally complete.
- conflicting: ['p1', 'p4', 'p8', 'p11'] The period labels say 2026-07/2026-01..07, but the snapshot dates (2025-09-24) and the corroborating Korean-language articles (p26-p31, snapshot 2025-11-26) establish these as July 2025 / Jan-Jul 2025

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Ratio of July 2026 live births to July 2025 live births in South Korea | 1.05 | 0.98..1.13 | 0.7441..1.488 (widened) | ratio | unused | Anchored on kept evidence: January 2026 births were +11.6% y/y (p35/p36), but the 2025 monthly y/y rate decelerated from +9.9% in September to +2.1% in October (p19, p16) and the marriage y/y rate fell from +24.6% in April 2025 (p24) to +0.7% in January 2026 (p38), so the mid-2026 increment should b | July 2026 births are driven by the same marriage-cohort and policy momentum observed through January 2026, with no new shock between February and July 2026. | A published 2026 monthly birth figure for February-June 2026 showing y/y growth outside roughly -2% to +13%, or a collapse in 2026 marriage registrations. |
| a2 | Ratio of July 2026 live births to January-July 2026 cumulative live births in South Korea | 0.1475 | 0.135..0.16 | 0.1039..0.2078 (widened) | ratio | unused | From kept evidence, July 2025 births (21,803, p1) divided by Jan-Jul 2025 cumulative births (147,804, p4) is about 0.1475. This within-year seasonal ratio converts a 2026 cumulative total into a July figure; the band reflects year-to-year variation in the seasonal profile. | The 2026 within-year birth profile through July resembles 2025's, so July's share of the cumulative total is stable. | A 2026 monthly pattern showing a materially different July concentration, e.g. a large one-off shift in spring or summer births. |
| a3 | Ratio of January-July 2026 cumulative live births to January-July 2025 cumulative live births in South Korea | 1.07 | 1..1.14 | 0.755..1.51 (widened) | ratio | unused | Anchored on kept evidence: January 2026 births were +11.6% y/y (p35/p36), while the 2025 monthly y/y rate decelerated to +2.1% by October (p16, p19) and the marriage y/y rate fell to +0.7% in January 2026 (p38). A central +7% for the seven-month cumulative, with a 10-90 band of 0% to +14%, reflects  | The 2026 y/y birth growth through July averages near the January 2026 rate but decays toward the late-2025 pace, with no new shock. | Published 2026 monthly birth figures for February-June 2026 implying cumulative y/y growth outside roughly 0% to +14%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

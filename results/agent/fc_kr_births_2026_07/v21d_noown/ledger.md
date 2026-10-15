# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), via the monthly Population Trends / 인구동향 release

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [related_series] Administrative birth registration data from the Ministry of the Interior and Safety (resident registration)

Hypothesis: Monthly birth registrations reported by the Ministry of the Interior and Safety (MOIS) are highly correlated with KOSTAT live births, though they may differ in timing and coverage. The MOIS monthly resident registration data for July 2026 may be published earlier than KOSTAT's release and can serve as a leading indicator or proxy.

Queries issued by the searcher: 행정안전부 주민등록 출생신고 2026년 7월; MOIS birth registration statistics July 2026 South Korea 주민등록 인구통계 출생; 행정안전부 2026년 7월 주민등록 인구통계 출생자 수 발표; 주민등록 인구통계 출생등록자 수 2026년 6월 7월

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260923077000002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gunbo.pc.go.kr/portal/part/info-statistics/info-statistics-list/info-statistics-list-population?articleSeq=330193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yonginilbo.com/news/article.html?no=110895` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [base_rates] Demographic accounting: births = women of childbearing age × age-specific fertility rates

Hypothesis: The number of live births in July 2026 can be estimated by multiplying the female population aged 15–49 in mid-2026 by the expected general fertility rate or age-specific fertility rates for 2026, then applying a July seasonal factor. This route requires population estimates and fertility assumptions.

Queries issued by the searcher: KOSTAT monthly Population Trends 2026 July live births; South Korea female population 15-49 2026 KOSTAT; 2026년 6월 인구동향 출생아 수 국가데이터처; South Korea July 2025 monthly births 21,854 population trends; 2026년 5월 인구동향 출생아 수 2만명 국가데이터처 7월 발표

- `https://m-cn.yna.co.kr/view/ACK20260923002500881?section=society/index` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://admin.korea.kr/briefing/pressReleaseView.do?newsId=156783095&pWise=mSub&pWiseSub=C3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.ktv.go.kr/news/sphere/T000021/view?content_id=761507` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8670581` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National Health Insurance Service (NHIS) birth-related claims or health insurance qualification data

Hypothesis: The number of births can be approximated from the number of newborns registered for health insurance or the number of delivery-related medical claims. These administrative data may be available with a shorter lag than KOSTAT and can provide an independent check on the level of births in July 2026.

Queries issued by the searcher: 국민건강보험공단 신생아 건강보험 가입 2026; NHIS newborn health insurance registration monthly 2026 South Korea births; 2026년 6월 출생아 수 인구동향 통계청; 통계청 인구동향 2026년 5월 출생아 수 발표; "2026년 5월" 인구동향 출생아 수 전년동월대비 증가; 2025년 7월 출생아 수 인구동향

- `https://www.law.go.kr/lsLinkCommonInfo.do?lsJoLnkSeq=1032724207&utm_source=chatgpt.com` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.law.go.kr/LSW/lumLsLinkPop.do?lspttninfSeq=69276` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000921498&chrClsCd=010202` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://xn--939a1gynmpm0ukuoxtbq59g.kr/lm/lmxsrv/law/joHistoryContent.do?SEQ=29&SEQ_CONTENTS=3153792&DATE_START=20260325&DATE_END=20260325` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [shocks] Policy and social shocks affecting births in 2026

Hypothesis: Government policies (e.g., expanded parental leave, baby bonuses), economic conditions, or demographic shocks (e.g., COVID-19 delayed births) may have altered the recent birth trend. Identifying measurable impacts can adjust the projection from historical patterns.

Queries issued by the searcher: South Korea monthly births 2026 Statistics Korea population trends; 저출산 대책 2026 출생아 수 월별 인구동향; 2026년 6월 인구동향 출생아 수 6월 출생아; 2025년 7월 출생아 수 인구동향 2만명; 2025년 7월 출생아 수 2만명 인구동향 통계청

- `https://indonesian.korea.net/NewsFocus/Society/view?articleId=294749` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.gmw.cn/2026-06/27/content_1304511276.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=289563&koreanId=289562` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://society.sohu.com/a/1041138135_313745?scm=10008.1476_13-1476_13-88_88.0-0.0-1-0-0-0.0&spm=smpc.content.fspic.3.1782322394078bKwFqyq` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Published forecasts or projections for South Korea's 2026 births

Hypothesis: Official or private forecasts for 2026 annual births can be combined with the historical July share of annual births to estimate July 2026. Forecasts may incorporate recent trends and policy effects.

Queries issued by the searcher: South Korea 2026 birth forecast KOSTAT births 2026; 2026년 출생아 수 전망 통계청; 2025년 7월 출생아 수 인구동향 명; 월별 출생아 수 2024 2025 7월 8월 9월 통계

- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/0
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p1 South Korea live births, July 2025 (monthly Population Trends) = **21,803** persons (live births) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p2 South Korea live births year-on-year change, July 2025 vs July 2024 = **5.9** percent (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p3 South Korea deaths, July 2025 = **27,979** persons (deaths) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p4 South Korea deaths year-on-year change, July 2025 vs July 2024 = **0.7** percent (2025-07-01..2025-07-31) [keep: ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p5 South Korea marriages, July 2025 = **20,394** cases (marriages) (2025-07-01..2025-07-31) [keep: ] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p6 South Korea marriages year-on-year change, July 2025 vs July 2024 = **8.4** percent (2025-07-01..2025-07-31) [DISCARD: Redundant duplicate of p5/p14: same July 2025 marriage count and same +8.4% change from the same MOIS release; adds no i] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p7 South Korea divorces, July 2025 = **7,826** cases (divorces) (2025-07-01..2025-07-31) [keep: ] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p8 South Korea divorces year-on-year change, July 2025 vs July 2024 = **1.4** percent (2025-07-01..2025-07-31) [DISCARD: Redundant duplicate of p7/p18/p19: same July 2025 divorce count and same -1.4% change from the same MOIS release; adds n] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p9 South Korea natural increase (births minus deaths), July 2025 = **-6,175** persons (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://www.khan.co.kr/article/202509241503001` -> **snapshot** (snapshot 20251003060236); points raw/verified 15/10
  - p10 South Korea year-on-year change in July live births, 2025 vs 2024 = **5.9** percent (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "7월 출생아 수는 2만1803명으로 전년 대비 5.9% 증가했다."
  - p11 South Korea year-on-year change in cumulative live births, January–July 2025 vs  = **7.2** percent (2025-01-01..2025-07-31) [EXCLUDED (ablation): ] quote: "올해 들어 7월까지 누적 출생아 수 14만7804명으로 1년 전보다 7.2% 많다."
  - p12 South Korea total fertility rate, July 2025 (year-on-year increase) = **0.04** persons (children per woman) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "7월 합계출산율도 전년 대비 0.04명 늘어 0.8명대를 회복했다."
  - p13 South Korea total fertility rate level, July 2025 = **0.8** persons (children per woman) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "7월 합계출산율도 전년 대비 0.04명 늘어 0.8명대를 회복했다."
  - p14 South Korea year-on-year change in marriages, July 2025 vs 2024 = **8.4** percent (2025-07-01..2025-07-31) [DISCARD: Redundant secondary retelling of the same July 2025 marriage statistic already carried by p5/p6/p24/p25; adds no indepen] quote: "7월 혼인 건수는 2만394건으로 1년 전보다 8.4% 증가했다."
  - p15 South Korea year-on-year change in cumulative marriages, January–July 2025 vs 20 = **7.3** percent (2025-01-01..2025-07-31) [keep: ] quote: "1월~7월 누계 혼인 건수는 13만8267건으로 지난해 같은 기간보다 7.3% 증가했다."
  - p16 South Korea year-on-year change in deaths, July 2025 vs 2024 = **0.7** percent (2025-07-01..2025-07-31) [DISCARD: Redundant secondary retelling of the same July 2025 death statistic already carried by p4/p23.] quote: "7월 사망자 수는 2만7979명으로 전년 대비 0.7% 감소했다."
  - p17 South Korea natural population decrease, July 2025 = **6,175** persons (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "인구는 6175명 자연 감소했다."
  - p18 South Korea divorces, July 2025 = **7,826** divorces (cases) (2025-07-01..2025-07-31) [DISCARD: Redundant secondary retelling of the same July 2025 divorce statistic already carried by p7/p26.] quote: "7월 이혼 건수는 7826건으로 1년 전보다 1.4% 줄었다."
  - p19 South Korea year-on-year change in divorces, July 2025 vs 2024 = **1.4** percent (2025-07-01..2025-07-31) [DISCARD: Redundant secondary retelling of the same July 2025 divorce change already carried by p8/p27.] quote: "7월 이혼 건수는 7826건으로 1년 전보다 1.4% 줄었다."
- `https://en.namu.wiki/w/2024-2026%EB%85%84%20%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%B6%9C%EC%82%B0%EC%9C%A8%20%EB%B0%98%EB%93%B1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 20 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 2; number: unknown scale word '만': 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 1; number: more than one number in value_as_written: 8; period_end 2035-12-31 after as_of: 1)

### b1 [related_series] Administrative leading indicator

Hypothesis: MOIS monthly resident-registration birth counts for July 2026 (or the latest available month in 2026) would provide a near-contemporaneous level for July 2026 births. Combined with the historical ratio of KOSTAT live births to MOIS registrations, this would unlock a direct level estimate for the target and materially reduce reliance on stale 2025 marriage/death data.

Queries issued by the searcher: 주민등록 인구통계 월별 출생자 수 2026년 7월; 행정안전부 주민등록 신생아 수 2026년 6월 출생등록; 행정안전부 주민등록 인구통계 2026년 7월 출생등록 사망말소; "2026년 7월" 주민등록 통계 출생등록 인구 자연증가

- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4866340?srchOrgCd=1241000&pageIndex=1&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.news.nate.com/view/20260923n16214` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [base_rates] Demographic decomposition

Hypothesis: A July 2026 birth estimate can be built from the mid-2026 female population aged 15-49 and an assumed 2026 general fertility rate or age-specific fertility rates, then adjusted by the July seasonal factor. This route would provide an independent structural estimate and a check on any administrative-proxy route.

Queries issued by the searcher: KOSTAT 인구동향 2025년 7월 출생아 수; South Korea 2025 total fertility rate 0.75 Statistics Korea births; 2026년 5월 인구동향 출생아 수; 통계청 장래인구추계 2026년 가임여성 인구 15-49세

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p20 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p21 South Korea live births year-on-year change, July 2025 vs July 2024 = **5.9** % (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p22 South Korea deaths, July 2025 (monthly Population Trends) = **27,979** deaths (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p23 South Korea deaths year-on-year change, July 2025 vs July 2024 = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p4 (same death count and change, same release); no additional information.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p24 South Korea marriages, July 2025 (monthly Population Trends) = **20,394** marriages (cases) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p5 (same July 2025 marriage count); no additional information.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p25 South Korea marriages year-on-year change, July 2025 vs July 2024 = **8.4** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p6 (same July 2025 marriage change); no additional information.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p26 South Korea divorces, July 2025 (monthly Population Trends) = **7,826** divorces (cases) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p7 (same July 2025 divorce count); no additional information.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p27 South Korea divorces year-on-year change, July 2025 vs July 2024 = **1.4** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p8 (same July 2025 divorce change); no additional information.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p28 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=288047` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Annual forecast plus seasonal share

Hypothesis: An official or credible private forecast for 2026 annual births, combined with the historical July share of annual births, would yield a July 2026 estimate. This would directly address the target period and provide a cross-check against administrative and demographic routes.

Queries issued by the searcher: KOSTAT 2026 annual birth forecast South Korea births projection; 한국 2026년 출생아 수 전망 통계청; 인구동향 월별 출생아 수 2025년 7월 출생아 2만명; KOSTAT monthly live births by month 2024 2025 July share of annual births Korea

- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/0
- `https://www.yna.co.kr/view/AKR20250924067700002` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.sedaily.com/finance/2026/04/22/koreas-births-poised-to-rebound-to-300000-after-7-years` -> **snapshot** (snapshot 20260422132545); points raw/verified 15/2
  - p29 Births in January this year tallied by the National Data Agency = **26,916** persons (2026-01-01..2026-01-31) [keep: ] quote: "Births in January this year, as tallied by the National Data Agency, also totaled 26,916"
  - p30 Year-on-year increase in January births = **11.7** percent (2026-01-01..2026-01-31) [keep: ] quote: "also totaled 26,916, up 11.7 percent from a year earlier"
- `https://en.namu.wiki/w/2024-2026%EB%85%84%20%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%B6%9C%EC%82%B0%EC%9C%A8%20%EB%B0%98%EB%93%B1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 28 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 2; number: unknown scale word '만': 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 10; number: more than one number in value_as_written: 3; period_end 2035-12-31 after as_of: 1; scale word 'thousand' not supported by quote or table header: 3; value_as_written not in quote as a whole number: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p5', 'p6', 'p14'] All three report the same July 2025 marriage count (20,394) and the same +8.4% year-on-year change, from the same underlying MOIS release. They are redundant copies, not independent confirmations.
- corroborating: ['p7', 'p8', 'p18', 'p19'] All four report the same July 2025 divorce count (7,826) and the same -1.4% year-on-year change, from the same underlying MOIS release. Redundant copies.
- corroborating: ['p4', 'p16'] Both report the same July 2025 death count (27,979) and the same -0.7% year-on-year change, from the same underlying MOIS release. Redundant copies.
- contextual: ['p15'] Cumulative January-July 2025 marriages (+7.3%) is a different period and a different vital event from the target; it is contextual only and cannot directly estimate July 2026 births.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p5', 'p6', 'p14', 'p24', 'p25'] All report the same July 2025 marriage count (20,394) and the same +8.4% YoY change, from the same KOSTAT/MOIS monthly Population Trends release; the news article (p14) is a secondary retelling of the
- corroborating: ['p7', 'p8', 'p18', 'p19', 'p26', 'p27'] All report the same July 2025 divorce count (7,826) and -1.4% YoY change from the same release; p18/p19 are secondary retellings.
- corroborating: ['p4', 'p16', 'p23'] Same July 2025 death count (27,979) and -0.7% YoY change from the same KOSTAT release; p16 is a secondary retelling.
- corroborating: ['p29', 'p30'] Both come from the same Sedaily article: January 2026 births 26,916, +11.7% YoY. Same underlying statistic, so they are one observation, not two.
- contextual: ['p5', 'p29'] Marriages and births are different vital events; the July 2025 marriage surge is only a weak, lagged signal for 2026 births and cannot be substituted for a birth level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 births relative to July 2025 births | 1.06 | 0.98..1.16 | 0.7539..1.508 (widened) | ratio | m1 (m1) | January 2026 births were +11.7% YoY (p29/p30), and the 2025 marriage surge (p5/p6) plus policy support point to continued positive momentum, but monthly birth changes are volatile and the January jump may partly reflect timing; a modest positive factor with wide uncertainty is appropriate. | Transfers if the early-2026 birth upturn persists through July 2026 and no major shock intervenes between January and July 2026. | Evidence that 2026 monthly births turned negative YoY (e.g., a reported decline in spring/summer 2026) or that the January 2026 increase was a one-off registration artifact. |
| a2 | July share of annual live births in South Korea | 0.083 | 0.078..0.089 | 0.05892..0.1178 (widened) | share | unused | July is a near-average month for Korean births; the July share of the annual total has historically been close to 1/12 with mild seasonality. Used only to convert an annual forecast into a July level. | Transfers if the seasonal distribution of births in 2026 resembles recent years and the annual forecast is for calendar-year 2026 live births. | Evidence of a large change in the seasonal birth pattern (e.g., a documented shift in conception timing) or a mismatch between the forecast's definition and KOSTAT live births. |

Rejected by code:

- a3 2026 annual live births in South Korea: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['korea']; quantity stems: ['birth', 'live', 'perso']
- points excluded before the judge: 13 of 30
- methods allowed: ['formula_mc']

  - p1 South Korea live births, July 2025 (monthly Population Trends) = 21,803 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p2 South Korea live births year-on-year change, July 2025 vs July 2024 = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p3 South Korea deaths, July 2025 = 27,979 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p9 South Korea natural increase (births minus deaths), July 2025 = -6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p10 South Korea year-on-year change in July live births, 2025 vs 2024 = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p11 South Korea year-on-year change in cumulative live births, January–July 2025 vs 2024 = 7.2 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p12 South Korea total fertility rate, July 2025 (year-on-year increase) = 0.04 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p13 South Korea total fertility rate level, July 2025 = 0.8 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p17 South Korea natural population decrease, July 2025 = 6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p20 South Korea live births, July 2025 (monthly Population Trends) = 21,803 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p21 South Korea live births year-on-year change, July 2025 vs July 2024 = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p22 South Korea deaths, July 2025 (monthly Population Trends) = 27,979 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p28 South Korea natural increase (live births minus deaths), July 2025 = -6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 28,725 | ['p29'] / ['a1'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **28,725**, 80% interval [19,476, 42,367], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as it will first be reported by Statistics Korea's monthly Population Trends release, is 28,725 persons. The interval is 19,476 to 42,367, a model-based 80% range conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate rests on one observed anchor: January 2026 births (6 observed point kept). A single assumption, a July 2026-to-July 2025 ratio of 1.06 (range 0.7539 to 1.508), transfers that level forward, informed by the January year-over-year jump and the [n] marriage rebound. The structural cross-check was rejected, so 1 method carries 100% weight.

Main risk: the January level may not represent July, and the ratio is assumed, not measured. The July 2026 figure itself, once published, would most improve this.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 July 2026 births relative to July 2025 births: 1.06 ratio, range 0.7539 to 1.508 (range widened by code); used by m1. Overturned by: Evidence that [n] monthly births turned negative YoY (e.g., a reported decline in spring/summer [n]) or that the January 2026 increase was a one-off registration artifact.

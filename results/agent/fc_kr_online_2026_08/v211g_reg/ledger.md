# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Total value of online shopping transactions (거래액) in South Korea during August 2026, as reported in the National Data Office (formerly Statistics Korea) monthly Online Shopping Trends (온라인쇼핑동향) release — the aggregate online shopping transaction value across all commodity groups and both mobile and  | unit KRW (current prices, total for the month) | period 2026-08-01..2026-08-31 | publisher National Data Office (국가데이터처, formerly Statistics Korea / 통계청) — Online Shopping Trends (온라인쇼핑동향)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] Statistical agency time series

Hypothesis: The target is a continuation of a monthly series; August 2026 value ≈ August 2025 value grown by the recent year-over-year trend, adjusted for August-specific seasonality (summer holiday, Chuseok timing — Chuseok falls in September/October, not August 2026). Own history gives the level and seasonal shape directly.

Queries issued by the searcher: 온라인쇼핑동향 거래액 2025년 8월 통계청; Statistics Korea online shopping trends monthly transaction value 2026; 2026년 7월 온라인쇼핑동향 국가데이터처 보도자료; 2026년 5월 온라인쇼핑동향 거래액 전년동월대비

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20260901_0003770725` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newscj.com/news/articleView.html?idxno=3324134` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/briefing/pressReleaseView.do?newsId=156773173` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Retail sales statistics

Hypothesis: Online shopping is a large share of total retail sales; the target ≈ total retail sales value × online share. Retail sales index/value and the online share of retail (온라인 매출 비중) are published separately and can bridge to the target.

Queries issued by the searcher: 소매판매액 월별 2026 온라인 비중 온라인쇼핑동향; 통계청 온라인쇼핑동향 2026년 7월 거래액; retail sales index Korea 2026 online share; 2026년 7월 소매판매액 56조1852억원 국가데이터처; 2026년 7월 산업활동동향 소매판매 국가데이터처 8월 31일; site:kosis.kr 2026 7월 소매판매액

- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/Government/Briefing-Room/Press-Releases/view?articleId=2018417&type=N&insttCode=A260129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Payment/card and platform data

Hypothesis: Online transaction value can be cross-checked against card/electronic payment statistics and major platform GMV (Coupang, Naver Shopping, etc.). Platform GMV summed plus long-tail estimate approximates the total; payment statistics give an independent level check.

Queries issued by the searcher: 온라인쇼핑동향 2026년 6월 거래액; 지급결제통계 온라인 거래액 2026 한국은행; Coupang Q2 2026 results revenue Korea product commerce; 네이버 2분기 2026 실적 커머스 거래액

- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www1.edaily.co.kr/News/Read?newsId=03191446645543712&mediaCodeNo=257` -> **snapshot** (snapshot 20260803080838); points raw/verified 15/14
  - p1 South Korea total online shopping transaction value, June 2026 = **24,606,700,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p2 South Korea mobile shopping transaction value, June 2026 = **18,927,000,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "6월 모바일쇼핑 거래액은 18조9270억원으로 전년 동월보다 9.8% 증가했다."
  - p3 Mobile share of total online shopping transaction value, June 2026 = **76.9** % (2026-06-01..2026-06-30) [keep: ] quote: "전체 온라인쇼핑 거래액에서 모바일이 차지하는 비중은 76.9%로 지난해 같은 달보다 0.7%포인트 낮아졌다."
  - p4 South Korea H1 2026 total online shopping transaction value (cumulative) = **145,737,100,000,000** KRW (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 온라인쇼핑 거래액은 145조7371억원으로 집계됐다."
  - p5 South Korea Q1 2026 total online shopping transaction value = **72,128,600,000,000** KRW (2026-01-01..2026-03-31) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p6 South Korea Q2 2026 total online shopping transaction value = **73,608,500,000,000** KRW (2026-04-01..2026-06-30) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p7 South Korea H1 2026 online product transaction value excluding travel and food s = **100,308,000,000,000** KRW (2026-01-01..2026-06-30) [keep: ] quote: "여행과 음식서비스 등을 제외한 온라인 상품 거래액은 상반기 100조3080억원을 기록하며 100조원을 넘어섰다."
  - p8 Online product transaction share of total retail sales, Q1 2026 = **29.4** % (2026-01-01..2026-03-31) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p9 Online product transaction share of total retail sales, Q2 2026 = **30** % (2026-04-01..2026-06-30) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p10 South Korea Q2 2026 online overseas direct sales value = **1,203,200,000,000** KRW (2026-04-01..2026-06-30) [keep: ] quote: "2분기 온라인 해외 직접 판매액은 1조2032억원으로 전년 동기보다 38.7% 증가했다."
  - p11 South Korea Q2 2026 online overseas direct purchase value = **2,116,600,000,000** KRW (2026-04-01..2026-06-30) [keep: ] quote: "반면 2분기 해외 직접 구매액은 2조1166억원으로 전년 동기보다 2.7% 감소했다."
  - p12 South Korea June 2026 food and beverage online transaction value = **3,353,900,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "음·식료품 거래액은 3조3539억원으로 전년 동월보다 10.4%, 농축수산물은 1조2564억원으로 12.7% 증가했다."
  - p13 South Korea June 2026 cosmetics online transaction value = **1,264,200,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "화장품 거래액도 1조2642억원으로 9.9% 늘었다."
  - p14 South Korea June 2026 automobiles and auto supplies online transaction value = **1,194,600,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "자동차 및 자동차용품 거래액도 1조1946억원으로 지난해 같은 달보다 56.8% 늘었다."
- `https://content-archive.fast-edgar.com/20260804/AMB2822CZ222T2Z2222M22ZGBFKGA422A282/cpng-06302026ex991.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nasdaq.com/articles/coupang-q2-earnings-call-highlights` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d4 [forecasts_markets] Industry forecasts and market research

Hypothesis: Published e-commerce market forecasts for Korea 2026 (e.g., from research firms, government plans) give an annual total that can be split by month using historical monthly shares, providing an independent level estimate.

Queries issued by the searcher: Korea online shopping market size 2026 forecast annual KRW; 국내 온라인쇼핑 시장 규모 2026 전망; 2025년 8월 온라인쇼핑 거래액 조원 국가데이터처 온라인쇼핑동향; "온라인쇼핑" 월별 거래액 2025년 8월 24조 전년동월대비

- `https://www.edaily.co.kr/News/Read?newsId=03043846642370312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fiscal.ai/company/KOSE-A035420/investor-relations/552809/?_x_output_type_b6db407c4_=embedded_pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?depth1=D0000&num=271836` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kbv.kr/markets/korea-e-commerce-market-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] Logistics/parcel volumes

Hypothesis: Online shopping value ≈ parcel/online shipment volume × average order value. Parcel volume (택배 물동량) is a physical proxy; dividing by average transaction value per parcel gives the transaction value.

Queries issued by the searcher: 택배 물동량 2026 월별; 온라인쇼핑동향 2026년 6월 거래액; 온라인쇼핑 객단가 2026 평균 구매액; 택배 물동량 2025년 8월 개 국가물류통합정보센터 월별

- `https://www.etnews.com/20260810000249` -> **snapshot** (snapshot 20260810062515); points raw/verified 15/11
  - p15 South Korea parcel volume, H1 2026 cumulative (Jan-Jun) = **3,314,553,267** parcels (2026-01-01..2026-06-30) [keep: ] quote: "올해 1~6월 국내 택배 물동량은 33억1455만3267개로 집계됐다."
  - p16 South Korea parcel volume, H1 2025 cumulative (Jan-Jun) = **3,107,317,049** parcels (2025-01-01..2025-06-30) [keep: ] quote: "지난해 상반기 31억731만7049개보다 2억723만6218개(6.67%) 증가했다."
  - p17 South Korea parcel volume, H1 2024 cumulative (Jan-Jun) = **2,883,456,869** parcels (2024-01-01..2024-06-30) [keep: ] quote: "2024년 상반기 물동량은 28억8345만6869개에서 2025년 상반기 31억731만7049개로 7.76% 증가했다."
  - p18 South Korea parcel volume, January 2026 = **539,740,000** parcels (2026-01-01..2026-01-31) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p19 South Korea parcel volume, February 2026 = **497,110,000** parcels (2026-02-01..2026-02-28) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p20 South Korea parcel volume, March 2026 = **575,590,000** parcels (2026-03-01..2026-03-31) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p21 South Korea parcel volume, April 2026 = **567,330,000** parcels (2026-04-01..2026-04-30) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p22 South Korea annual parcel volume, 2025 (first year above 6 billion) = **6,000,000,000** parcels (2025-01-01..2025-12-31) [keep: ] quote: "지난해 처음으로 연간 물동량이 60억개를 돌파한 데 이어 올해도 상반기부터 가파른 성장세를 이어가고 있다."
  - p23 South Korea population aged 15+, June 2026 (denominator for per-capita parcel us = **45,997,000** people (2026-06-01..2026-06-30) [keep: ] quote: "올해 6월 기준 15세 이상 전체 인구 4599만7000명을 기준으로 상반기 물동량을 단순 환산하면 1인당 72.1회에 달한다."
  - p24 South Korea per-capita parcel use, H1 2026 (per person aged 15+) = **72.1** parcels per person (2026-01-01..2026-06-30) [keep: ] quote: "올해 6월 기준 15세 이상 전체 인구 4599만7000명을 기준으로 상반기 물동량을 단순 환산하면 1인당 72.1회에 달한다."
  - p25 South Korea per-capita parcel use, full-year 2025 (per person aged 15+) = **126** parcels per person (2025-01-01..2025-12-31) [keep: ] quote: "지난해 연간 기준 국민 1인당 125.5회, 경제활동인구 1인당 218.1회였던 것을 고려하면, 올해 상반기에만 연간 택배 이용량의 상당 부분을 채운 셈이다."
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www1.edaily.co.kr/News/Read?newsId=03191446645543712&mediaCodeNo=257` -> **snapshot** (snapshot 20260803080838); points raw/verified 15/14
  - p26 South Korea total online shopping transaction value, June 2026 = **24,606,700,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p1 (same June 2026 total).] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p27 South Korea total online shopping transaction value, H1 2026 (cumulative) = **145,737,100,000,000** KRW (2026-01-01..2026-06-30) [DISCARD: Duplicate of p4 (H1 2026 cumulative).] quote: "올해 상반기 온라인쇼핑 거래액은 145조7371억원으로 집계됐다."
  - p28 South Korea total online shopping transaction value, Q1 2026 = **72,128,600,000,000** KRW (2026-01-01..2026-03-31) [DISCARD: Duplicate of p5 (Q1 2026).] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p29 South Korea total online shopping transaction value, Q2 2026 = **73,608,500,000,000** KRW (2026-04-01..2026-06-30) [DISCARD: Duplicate of p6 (Q2 2026).] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p30 South Korea mobile shopping transaction value, June 2026 = **18,927,000,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p2 (June 2026 mobile value).] quote: "6월 모바일쇼핑 거래액은 18조9270억원으로 전년 동월보다 9.8% 증가했다."
  - p31 Mobile share of total online shopping transaction value, June 2026 = **76.9** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p3 (June 2026 mobile share).] quote: "전체 온라인쇼핑 거래액에서 모바일이 차지하는 비중은 76.9%로 지난해 같은 달보다 0.7%포인트 낮아졌다."
  - p32 South Korea online product transaction value excluding travel and food services, = **100,308,000,000,000** KRW (2026-01-01..2026-06-30) [DISCARD: Duplicate of p7 (product-only H1 2026).] quote: "여행과 음식서비스 등을 제외한 온라인 상품 거래액은 상반기 100조3080억원을 기록하며 100조원을 넘어섰다."
  - p33 Online product share of total retail sales, Q1 2026 = **29.4** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of p8 (Q1 2026 online retail share).] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p34 Online product share of total retail sales, Q2 2026 = **30** % (2026-04-01..2026-06-30) [DISCARD: Duplicate of p9 (Q2 2026 online retail share).] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p35 South Korea food and beverage online transaction value, June 2026 = **3,353,900,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p12 (June 2026 food & beverage).] quote: "음·식료품 거래액은 3조3539억원으로 전년 동월보다 10.4%, 농축수산물은 1조2564억원으로 12.7% 증가했다."
  - p36 South Korea agricultural, livestock and fishery online transaction value, June 2 = **1,256,400,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of the agricultural/livestock/fishery figure quoted within p12's article; no separate kept id needed.] quote: "음·식료품 거래액은 3조3539억원으로 전년 동월보다 10.4%, 농축수산물은 1조2564억원으로 12.7% 증가했다."
  - p37 South Korea cosmetics online transaction value, June 2026 = **1,264,200,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p13 (June 2026 cosmetics).] quote: "화장품 거래액도 1조2642억원으로 9.9% 늘었다."
  - p38 South Korea automobile and auto parts online transaction value, June 2026 = **1,194,600,000,000** KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p14 (June 2026 autos).] quote: "자동차 및 자동차용품 거래액도 1조1946억원으로 지난해 같은 달보다 56.8% 늘었다."
  - p39 South Korea mobile telecommunication device online transaction value, June 2026 = **892,400,000,000** KRW (2026-06-01..2026-06-30) [keep: ] quote: "6월 통신기기 온라인 거래액은 8924억원으로 전년 동월보다 144.4% 급증했다."
- `https://www.sedaily.com/article/20065986` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d6 [shocks] Calendar and macro effects

Hypothesis: August 2026 has no Chuseok (falls later), but summer promotions, heat waves, and macro consumption trends (consumer sentiment, inflation) shift the level. Identifying measurable August-specific effects constrains the YoY adjustment in d1.

Queries issued by the searcher: 소비자심리지수 2026년 8월; Korea consumer price index August 2026 year-on-year; 2026년 8월 온라인쇼핑 프로모션 매출 8.8 세일; 온라인쇼핑동향 2026년 7월 거래액

- `https://mods.go.kr/board.es?mid=a20109020000&bid=11751&list_no=446747&act=view` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/amp/view/AKR20260824149100002` -> **snapshot** (snapshot 20260825050624); points raw/verified 15/15
  - p40 South Korea Consumer Sentiment Index (CCSI), August 2026 = **104** index points (2026-08-01..2026-08-31) [keep: ] quote: "8월 소비자심리지수(CCSI)는 104.5로 전월보다 2.3포인트(p) 하락했다."
  - p41 Month-on-month change in South Korea CCSI, August 2026 = **2.3** index points (2026-08-01..2026-08-31) [keep: ] quote: "8월 소비자심리지수(CCSI)는 104.5로 전월보다 2.3포인트(p) 하락했다."
  - p42 South Korea expected inflation rate (consumer price inflation expectation over n = **2.7** % (2026-08-01..2026-08-31) [keep: ] quote: "기대인플레이션율 가운데 향후 1년의 소비자물가 상승률 전망치(2.7%)는 전월과 같은 수준을 유지했다."
  - p43 South Korea current economic judgment sub-index (현재경기판단), August 2026 = **79** index points (2026-08-01..2026-08-31) [keep: ] quote: "CCSI를 구성하는 6개 지수 중 현재경기판단(79·-5p)이 가장 큰 폭으로 내렸다."
  - p44 South Korea future economic outlook sub-index (향후경기전망), August 2026 = **89** index points (2026-08-01..2026-08-31) [keep: ] quote: "향후경기전망(89·-3p)과 취업기회전망(86·-3p)도 4월(-10p·-7p) 이후 가장 큰 폭으로 하락했으며"
  - p45 South Korea household income outlook sub-index (가계수입전망), August 2026 = **100** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p46 South Korea consumption expenditure outlook sub-index (소비지출전망), August 2026 = **109** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p47 South Korea current living standards sub-index (현재생활형편), August 2026 = **92** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p48 South Korea living standards outlook sub-index (생활형편전망), August 2026 = **97** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p49 South Korea employment opportunity outlook sub-index (취업기회전망), August 2026 = **86** index points (2026-08-01..2026-08-31) [keep: ] quote: "향후경기전망(89·-3p)과 취업기회전망(86·-3p)도 4월(-10p·-7p) 이후 가장 큰 폭으로 하락했으며"
  - p50 South Korea current household savings index (현재가계저축지수), August 2026 = **94** index points (2026-08-01..2026-08-31) [keep: ] quote: "현재가계저축지수(94)는 전월보다 3p 하락해 작년 5월(93) 이후 1년 3개월 만에 가장 낮았다."
  - p51 South Korea current household debt index (현재가계부채지수), August 2026 = **100** index points (2026-08-01..2026-08-31) [keep: ] quote: "현재 가계부채 수준에 대한 인식을 나타내는 현재가계부채지수는 100으로 전월과 같은 수준을 유지했다."
  - p52 South Korea housing price outlook index (주택가격전망지수), August 2026 = **125** index points (2026-08-01..2026-08-31) [keep: ] quote: "주택가격전망지수(125)는 전월보다 2p 하락했다."
  - p53 South Korea interest rate level outlook index (금리수준전망지수), August 2026 = **125** index points (2026-08-01..2026-08-31) [keep: ] quote: "6개월 후 금리 수준을 예상한 금리수준전망지수(125)는 1p 하락했다."
  - p54 South Korea CCSI month-on-month decline in April 2026 (comparison) = **-7.8** index points (2026-04-01..2026-04-30) [keep: ] quote: "다만 하락 폭은 중동 전쟁 영향으로 크게 내렸던 지난 4월(-7.8p)보다는 작았다."
- `https://www.etnews.com/20260825000046` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://incomglobal.co.kr/2026-liberation-day-retail-discount-strategy/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Time series

Hypothesis: Obtaining the full monthly Online Shopping Trends series for 2024-2025 (and August 2025 specifically) would let a direct YoY-scaling or seasonal-naive method replace the June-anchored extrapolation, which is currently the dominant uncertainty.

Queries issued by the searcher: 온라인쇼핑동향 2025년 8월 온라인쇼핑 거래액 통계청; Statistics Korea online shopping trends August 2025 monthly transaction value trillion won; 2026년 6월 온라인쇼핑동향 국가데이터처 온라인쇼핑 거래액; mods.go.kr 온라인쇼핑동향 2026년 5월 거래액 조 원 증가

- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=438862&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Seasonality

Hypothesis: The July-to-August seasonal ratio of online transaction value (summer holiday, no Chuseok) is needed to move from the June 2026 anchor to August 2026; historical monthly shares would supply this conversion factor.

Queries issued by the searcher: 온라인쇼핑동향 2023년 8월 온라인쇼핑 거래액 통계청; 온라인쇼핑동향 2025년 8월 거래액 조사 결과; 2024년 7월 온라인쇼핑동향 거래액 국가데이터처 보도자료; 2025년 7월 온라인쇼핑동향 거래액 역대 최고 전월대비

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4004097?Mcode=4100&pageIndex=198&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kostat.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=427377` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mt.co.kr/economy/2025/10/01/2025100110540095667` -> **snapshot** (snapshot 20251004015023); points raw/verified 15/15
  - p55 South Korea total online shopping transaction value, August 2025 = **22,480,200,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p56 South Korea total online shopping transaction value, year-on-year increase, Augu = **1,392,700,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p57 South Korea online shopping transaction value year-on-year growth rate, August 2 = **6.6** % (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액이 1년 전보다 6.6% 늘었다."
  - p58 South Korea online shopping transaction value year-on-year growth rate, July 202 = **7.8** % (2025-07-01..2025-07-31) [keep: ] quote: "증가율은 7월(7.8%)보다는 다소 둔화했지만"
  - p59 South Korea online shopping transaction value year-on-year growth rate, January  = **1.6** % (2025-01-01..2025-01-31) [keep: ] quote: "올해 온라인쇼핑 거래액 증가율은 △1월 1.6% △2월 3.7% △3월 2.5% △4월 2.8% △5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p60 South Korea online shopping transaction value year-on-year growth rate, February = **3.7** % (2025-02-01..2025-02-28) [keep: ] quote: "△1월 1.6% △2월 3.7% △3월 2.5% △4월 2.8% △5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p61 South Korea online shopping transaction value year-on-year growth rate, March 20 = **2.5** % (2025-03-01..2025-03-31) [keep: ] quote: "△2월 3.7% △3월 2.5% △4월 2.8% △5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p62 South Korea online shopping transaction value year-on-year growth rate, April 20 = **2.8** % (2025-04-01..2025-04-30) [keep: ] quote: "△3월 2.5% △4월 2.8% △5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p63 South Korea online shopping transaction value year-on-year growth rate, May 2025 = **0.6** % (2025-05-01..2025-05-31) [keep: ] quote: "△4월 2.8% △5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p64 South Korea online shopping transaction value year-on-year growth rate, June 202 = **2.2** % (2025-06-01..2025-06-30) [keep: ] quote: "△5월 0.6% △6월 2.2% △7월 7.8%에 이어 8월 6.6%를 기록하며"
  - p65 South Korea mobile shopping transaction value, August 2025 = **17,848,900,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p66 South Korea mobile shopping share of total online transaction value, August 2025 = **79.4** % (2025-08-01..2025-08-31) [keep: ] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p67 South Korea food services online transaction value, August 2025 = **3,736,600,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "상품군별로는 음식서비스(3조7366억원)가 전년 동월 대비 9.0% 늘며 거래액 1위를 차지했다."
  - p68 South Korea comprehensive mall online transaction value, August 2025 = **11,950,000,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "취급 상품 범위별로는 종합몰이 11조9500억원으로 4.1% 증가했고, 전문몰은 10조5302억원으로 9.6% 늘었다."
  - p69 South Korea specialized mall online transaction value, August 2025 = **10,530,200,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "종합몰이 11조9500억원으로 4.1% 증가했고, 전문몰은 10조5302억원으로 9.6% 늘었다."

### b3 [related_series] Level cross-check

Hypothesis: Card/electronic payment statistics or major platform GMV for mid-2026 would provide an independent level check on the June 2026 anchor and the growth trend, resolving whether the ~10.7% YoY growth is representative for August.

Queries issued by the searcher: 한국은행 지급결제동향 2026년 2분기 카드 이용액; Coupang Q2 2026 net revenues product commerce; 한국은행 지급결제동향 2026년 2분기 일평균 카드 결제금액 증가; 온라인쇼핑동향 2026년 6월 거래액 국가데이터처

- `https://content-archive.fast-edgar.com/20260804/AMB2822CZ222T2Z2222M22ZGBFKGA422A282/cpng-06302026ex991.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nasdaq.com/articles/coupang-q2-earnings-call-highlights` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260929073300002?section=economy/all` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1275844.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea online shopping', 'korea retail sales', 'korea e-commerce gmv']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p26'] Identical June 2026 total online shopping transaction value (24,606.7 bn KRW) reported in the same article; p26 is a duplicate of p1, not independent evidence.
- corroborating: ['p4', 'p27'] Identical H1 2026 cumulative total (145,737.1 bn KRW); p27 duplicates p4.
- corroborating: ['p5', 'p6', 'p4'] Q1 + Q2 = H1 by construction (72,128.6 + 73,608.5 = 145,737.1 bn KRW); internal consistency check, not independent.
- corroborating: ['p1', 'p2', 'p3'] Mobile value and mobile share are consistent with the total (18,927 / 24,606.7 ≈ 76.9%); same source, same release.
- corroborating: ['p1', 'p12', 'p13', 'p14', 'p39'] Commodity-group June 2026 values are components of the June total; they sum to a small fraction of the total, consistent with many other groups not listed.
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21'] Monthly 2026 parcel volumes sum to the H1 2026 cumulative; H1 growth rates (6.67%, 7.76%) are consistent across years. Same underlying parcel-volume measurement.
- corroborating: ['p22', 'p25', 'p23', 'p24'] Annual 2025 volume, per-capita rates and 15+ population are mutually consistent (6bn / ~46m ≈ 126).
- corroborating: ['p40', 'p41', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54'] All from the same August 2026 CCSI release; sub-indices and MoM changes are internally consistent. Note p40 value 104 vs quote 104.5 — minor transcription discrepancy; treat as ~104.5.
- corroborating: ['p1', 'p15'] Online transaction value and parcel volume both grew in H1 2026; used together in the parcel-based route (d5) as a level cross-check, though they measure different things (value vs. shipment count).
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] Same June 2026 release: mobile value p2 and mobile share p3 are internally consistent with total p1 (p2/p1 ≈ 76.9%). One underlying source (National Data Office release reported by edaily), so not ind
- corroborating: ['p1', 'p4', 'p5', 'p6'] Quarterly and half-year totals are the same series aggregated; p5+p6 should equal p4 and p1 is the June component of p6. Same source, so this is internal consistency, not independent evidence.
- corroborating: ['p55', 'p56', 'p57'] August 2025 level, YoY increment and YoY rate are three renderings of one statistic (22.48tn = prior year + 1.39tn at 6.6%).
- corroborating: ['p55', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64'] Monthly 2025 YoY growth rates from one article; they establish that 2025 growth accelerated in H2 (July 7.8%, Aug 6.6%) versus ~2% in H1, useful for judging whether the 2026 H1 ~10.7% rate is represen
- corroborating: ['p1', 'p55'] June 2026 (24.61tn, +10.7% YoY) versus August 2025 (22.48tn, +6.6% YoY): consistent with an accelerating 2026 trend; the June 2026 level implies June 2025 ≈ 22.23tn, close to the August 2025 level, so
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22'] Parcel volumes: monthly 2026 values sum to the H1 2026 cumulative; H1 growth 6.67% (2026) and 7.76% (2025) are consistent with the >6bn 2025 annual figure. Parcel volume grows slower than online trans
- corroborating: ['p15', 'p23', 'p24', 'p25'] Per-capita figures are derived from the same parcel totals and population; they add no independent level information.
- corroborating: ['p40', 'p41', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54'] August 2026 CCSI 104.5, down 2.3p m/m but still above 100 and a smaller drop than April's -7.8p; sub-indices mostly fell 1-5p. Signals mildly softer August consumption but not a collapse — supports a 
- corroborating: ['p12', 'p13', 'p14', 'p39'] June 2026 commodity-group values (food 3.35tn, cosmetics 1.26tn, autos 1.19tn, telecom devices 0.89tn with +144% YoY) are components of the June total p1; they explain part of the elevated 10.7% growt
- corroborating: ['p8', 'p9', 'p7'] Online product share of retail rose 29.4%→30.0% Q1→Q2 2026; p7 (product-only H1) is a narrower scope than the target and cannot be substituted directly.
- corroborating: ['p10', 'p11'] Cross-border flows are small relative to the total and are separate concepts (overseas direct sales/purchases), not components of domestic online shopping transaction value.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 / August 2025 growth factor for total online shopping transaction value | 1.09 | 1.02..1.16 | 0.9729..1.216 (widened) | ratio | m1 (m1) | June 2026 grew 10.7% YoY (p1) and H1 2026 averaged roughly 10%; 2025 growth accelerated into H2 (p58, p57: 7.8% July, 6.6% August 2025), so a base effect makes a repeat of ~9-10% plausible. August 2026 has no Chuseok (falls in September/October), same as August 2025, so no calendar distortion. The A | The 2026 YoY growth trend of roughly 8-12% observed through June continues into August, and August 2026 has no major one-off demand shock. | Evidence of a sharp break in online growth (e.g., a July/August 2026 YoY rate below 5% or above 15%), or a major August 2026 platform event or regulatory shock. |
| a2 | Average online transaction value per parcel (KRW/parcel) | 44,000 | 34,000..57,000 | 31,129..62,258 (widened) | KRW/parcel | unused | H1 2026 online value (p4, 145.7tn) divided by H1 2026 parcels (p15, 3.31bn) gives about 44,000 KRW per parcel. Because online value includes food services and travel that generate few parcels, the parcel-linked goods portion is somewhat lower per parcel, but high-ticket electronics and groceries pus | Parcel volume is a stable proxy for the goods portion of online transactions and value-per-parcel is stable between H1 and August 2026. | Evidence that value per parcel shifted sharply (e.g., a surge in high-ticket electronics or a collapse in low-value orders). |
| a3 | August 2026 / H1 2026 average monthly parcel-volume ratio | 1 | 0.9..1.1 | 0.7036..1.407 (widened) | ratio | unused | Monthly 2026 parcel volumes (p18-p21) vary within roughly ±8% around the H1 mean with no strong seasonal spike; August is a normal non-holiday month, so the August monthly volume should be close to the H1 average. Centered at 1.0. | August parcel volume behaves like other non-holiday months in 2026. | Data showing August parcel volume systematically 10%+ above or below the H1 average. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 24,473,747,015,246 | ['p55'] / ['a1'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **24,473,747,015,246** KRW, 80% interval [17,764,695,719,650, 33,716,552,336,087] KRW, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total online shopping transaction value (거래액) in South Korea for August 2026, across all commodity groups and both mobile and other channels, is 24,473,747,015,246 KRW (80% model-based interval 17,764,695,719,650 to 33,716,552,336,087 KRW).

The estimate rests on a single method (1 method, weight 100%): the observed August 2025 level of 22,480,200,000,000 KRW grown by an assumed August 2026/August 2025 growth factor of 1.09 (range 0.9729 to 1.216). The August 2025 figure is observed; the growth factor is an analyst assumption, not observed. It is motivated by roughly [n] YoY growth through mid-2026 and a favorable base effect, with no Chuseok distortion in August. Using the same calendar month avoids seasonal conversion.

The main risk is that 2026 YoY growth diverges from the assumed ~[n]-[n], for example from a telecom-device or demand shift. The most useful missing evidence would be actual July-August 2026 monthly figures to pin down the current growth rate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 / August 2025 growth factor for total online shopping transaction value: 1.09 ratio, range 0.9729 to 1.216 (range widened by code); used by m1. Overturned by: Evidence of a sharp break in online growth (e.g., a July/August 2026 YoY rate below [n] or above [n]), or a major August 2026 platform event or regulatory shock.

# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Nominal total value of online shopping transactions (online shopping transaction amount, 온라인쇼핑 거래액) in South Korea for calendar August 2026, covering all product and service categories in the monthly Online Shopping Trends survey, online and mobile combined, as it would first be reported by the Nati | unit KRW, nominal total for the month, not seasonally adjusted | period 2026-08-01..2026-08-31 | publisher National Data Office (국가데이터처, formerly Statistics Korea)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] official statistics publisher

Hypothesis: August 2026 online shopping transaction value can be projected from the most recent official monthly values before the cutoff, updated by recent year-on-year growth and the historical August seasonal factor. The relationship is V_2026_08 = V_latest_2026 * (1+g_recent)^months * seasonal_Aug, with seasonal factors estimated from 2023-2025 August-to-neighbouring-month ratios.

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 온라인쇼핑 거래액; 국가데이터처 온라인쇼핑동향 2026년 6월 거래액; 2025년 8월 온라인쇼핑동향 온라인쇼핑 거래액 8월 모바일쇼핑 거래액; 2024년 8월 온라인쇼핑 거래액 21조 온라인쇼핑동향; 2023년 8월 온라인쇼핑 거래액 19조 온라인쇼핑동향 통계청

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853&pageIndex=&group=S&srchCode=&startDate=&endDate=&srchKeyword=&groupId=&codeLevel1=&codeLevel2=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] retail statistics compiler

Hypothesis: Online shopping transaction value is a large share of total retail sales plus selected services. If monthly retail sales value and the online share are available, the target can be cross-checked or bounded as V_online = retail_sales_value * online_share / coverage_adjustment, with an explicit adjustment for service categories included in Online Shopping Trends but not in retail sales.

Queries issued by the searcher: 통계청 온라인쇼핑 동향 2026년 7월 온라인쇼핑 거래액; 소매판매액 지수 2026년 7월 통계청; 2025년 8월 온라인쇼핑 거래액 25조 통계청; 소매판매액 2026년 7월 56조1852억원 온라인쇼핑 상품 거래액 비중 30.3%

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ytn.co.kr/_ln/0102_202510011350546155` -> **snapshot** (snapshot 20251001062529); points raw/verified 8/8
  - p1 South Korea total online shopping transaction amount, August (all categories, on = **22,480,200,000,000** as written "22조 4천802억", value check ok KRW (2025-08-01..2025-08-31) [keep: ] quote: "지난 8월 온라인으로 물건을 구매한 총액이 22조 4천802억 원으로 1년 전보다 6.6% 늘었다고 밝혔습니다."
  - p2 South Korea total online shopping transaction amount, August, year-on-year growt = **6.6** % (2025-08-01..2025-08-31) [keep: ] quote: "지난 8월 온라인으로 물건을 구매한 총액이 22조 4천802억 원으로 1년 전보다 6.6% 늘었다고 밝혔습니다."
  - p3 South Korea mobile shopping transaction amount, August (share of online shopping = **17,848,900,000,000** as written "17조 8천489억", value check ok KRW (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 중 모바일 쇼핑액은 17조 8천489억 원으로 1년 전보다 8.9% 늘면서 8월 기준 역대 최고치를 기록했습니다."
  - p4 South Korea mobile shopping transaction amount, August, year-on-year growth rate = **8.9** % (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 중 모바일 쇼핑액은 17조 8천489억 원으로 1년 전보다 8.9% 늘면서 8월 기준 역대 최고치를 기록했습니다."
  - p5 South Korea mobile share of online shopping transaction amount, August = **79.4** % (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 가운데 모바일 거래액 비중은 79.4%로, 지난해 같은 달보다 1.7%p 늘었습니다."
  - p6 South Korea mobile share of online shopping transaction amount, August, year-on- = **1.7** % (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 가운데 모바일 거래액 비중은 79.4%로, 지난해 같은 달보다 1.7%p 늘었습니다."
  - p7 Tesla vehicles sold in South Korea, August = **7,974** as written "7천974", value check pending vehicles (2025-08-01..2025-08-31) [DISCARD: Tesla vehicle sales in August 2025, unrelated to online shopping transaction value.] quote: "테슬라는 지난 8월 7천974대를 판매하며 한 달 전 7천357대에 이어 두 달 연속 수입차 판매 1위를 기록했습니다."
  - p8 Tesla vehicles sold in South Korea, prior month (July) = **7,357** as written "7천357", value check pending vehicles (2025-07-01..2025-07-31) [DISCARD: Tesla July vehicle sales, unrelated to online shopping transaction value.] quote: "테슬라는 지난 8월 7천974대를 판매하며 한 달 전 7천357대에 이어 두 달 연속 수입차 판매 1위를 기록했습니다."
- `https://bbs2.shinhansec.com/board/message/file.do?attachmentId=341272` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] payments system observer

Hypothesis: Card, bank-transfer, and easy-payment online/remote spending is correlated with the official online shopping total. The target can be estimated as V_online = online_card_payment_amount / payment_coverage_share, where the coverage share captures non-card payments and categories not captured by card data.

Queries issued by the searcher: 신용카드 온라인 결제액 2026년 온라인쇼핑 거래액; 온라인쇼핑 거래액 2026년 6월 통계청; 2026년 7월 온라인쇼핑동향 국가데이터처 거래액; 한국은행 지급결제통계 2025년 연간 비대면 모바일 카드 결제 비중

- `https://www.gov.kr/portal/ntnadmNews/4844676` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.joseilbo.com/news/htmls/2026/07/20260730572916.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.tf.co.kr/read/economy/2318830.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] parcel delivery operator

Hypothesis: For goods purchased online, parcel volume times e-commerce parcel share times average order value can approximate the goods component of online shopping. The target then equals that goods component plus an allowance for services (travel, culture, food delivery, etc.). Symbolically V_online = parcels * ecommerce_share * AOV / parcels_per_order + service_allowance.

Queries issued by the searcher: 택배 물동량 2026년 8월; 온라인쇼핑 거래액 2026년 7월 국가데이터처; 국가물류통합정보센터 택배 물동량 2026년 7월 월별; 택배 물량 중 이커머스 비중 90% 온라인 쇼핑 택배

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.etnews.com/20260810000249` -> **snapshot** (snapshot 20260810062515); points raw/verified 15/12
  - p9 South Korea domestic parcel volume, H1 2026 cumulative (Jan-Jun) = **3,314,553,267** parcels (2026-01-01..2026-06-30) [keep: ] quote: "올해 1~6월 국내 택배 물동량은 33억1455만3267개로 집계됐다."
  - p10 South Korea domestic parcel volume, H1 2025 cumulative (Jan-Jun) = **3,107,317,049** parcels (2025-01-01..2025-06-30) [keep: ] quote: "지난해 상반기 31억731만7049개보다 2억723만6218개(6.67%) 증가했다."
  - p11 South Korea domestic parcel volume, H1 2024 cumulative (Jan-Jun) = **2,883,456,869** parcels (2024-01-01..2024-06-30) [keep: ] quote: "2024년 상반기 물동량은 28억8345만6869개에서 2025년 상반기 31억731만7049개로 7.76% 증가했다."
  - p12 South Korea domestic parcel volume, January 2026 = **539,740,000** parcels (2026-01-01..2026-01-31) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p13 South Korea domestic parcel volume, February 2026 = **497,110,000** parcels (2026-02-01..2026-02-28) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p14 South Korea domestic parcel volume, March 2026 = **575,590,000** parcels (2026-03-01..2026-03-31) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p15 South Korea domestic parcel volume, April 2026 = **567,330,000** parcels (2026-04-01..2026-04-30) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p16 South Korea domestic parcel volume, May 2026 = **554,040,000** parcels (2026-05-01..2026-05-31) [keep: ] quote: "월별로는 올해 1월 5억3974만개, 2월 4억9711만개, 3월 5억7559만개, 4월 5억6733만개, 5월 5억5404만개, 6월 5억8075만개를 각각 기록했다."
  - p17 South Korea annual parcel volume, 2025 (first year to exceed 6 billion) = **6,000,000,000** parcels (2025-01-01..2025-12-31) [keep: ] quote: "지난해 처음으로 연간 물동량이 60억개를 돌파한 데 이어 올해도 상반기부터 가파른 성장세를 이어가고 있다."
  - p18 South Korea H1 2026 parcel volume growth rate year-on-year = **6.67** % (2026-01-01..2026-06-30) [keep: ] quote: "지난해 상반기 31억731만7049개보다 2억723만6218개(6.67%) 증가했다."
  - p19 South Korea H1 2025 parcel volume growth rate year-on-year = **7.76** % (2025-01-01..2025-06-30) [keep: ] quote: "2024년 상반기 물동량은 28억8345만6869개에서 2025년 상반기 31억731만7049개로 7.76% 증가했다."
  - p20 South Korea per-capita parcel usage, H1 2026, population aged 15+ basis = **72.1** parcels per person (2026-01-01..2026-06-30) [keep: ] quote: "올해 6월 기준 15세 이상 전체 인구 4599만7000명을 기준으로 상반기 물동량을 단순 환산하면 1인당 72.1회에 달한다."
- `https://v.daum.net/v/20260813062127475` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20260901_0003770725` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; period_end 2026-12-31 after as_of: 2)

### d5 [persona] major online platform operator

Hypothesis: Summing GMV or transaction value of major Korean online platforms and dividing by their estimated share of the official online shopping market gives a top-down estimate. This route tests the target from operator-level disclosures and market-share estimates, with transfer assumptions about platform coverage and double counting.

Queries issued by the searcher: 쿠팡 GMV 2026 2분기 실적; 네이버 커머스 거래액 2026; 온라인쇼핑 거래액 2026년 7월 통계청 발표; 쿠팡 네이버 이커머스 점유율 2026 시장 규모 조원

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wiseapp.co.kr/insight/detail/1050` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.thebell.co.kr/m/newsview.asp?svccode=15&newskey=202608050728023360104986` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.nate.com/view/20260727n03136` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [base_rates] payment transaction processor

Hypothesis: Total online shopping value equals online transaction count times average transaction value, adjusted for services and non-card payments. This route is useful if a monthly count of online payment transactions and average online basket are available; it is weaker if transaction counts combine in-store and online.

Queries issued by the searcher: 온라인쇼핑 거래액 2026년 6월 통계청; 온라인 결제 건수 2025 전자상거래 결제건수 통계; 2026년 7월 온라인쇼핑동향 거래액; 2025년 온라인쇼핑 거래액 연간 250조 통계청 온라인쇼핑동향 12월

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.koreaherald.com/article/10699005` -> **snapshot** (snapshot 20260320125411); points raw/verified 15/14
  - p21 Daily average value of payment gateway (PG) services in South Korea, 2025 = **1,550,000,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "The daily average value of payment gateway services reached 1.55 trillion won ($1.04 billion) last year, up 9.2 percent from a year earlier"
  - p22 Year-on-year growth rate of daily average PG service value, South Korea, 2025 = **9.2** % (2025-01-01..2025-12-31) [keep: ] quote: "reached 1.55 trillion won ($1.04 billion) last year, up 9.2 percent from a year earlier"
  - p23 Daily average number of PG service transactions in South Korea, 2025 = **33,640,000** transactions (2025-01-01..2025-12-31) [keep: ] quote: "The daily average number of transactions also rose 11.8 percent on-year to 33.64 million."
  - p24 Year-on-year growth rate of daily average PG transaction count, South Korea, 202 = **11.8** % (2025-01-01..2025-12-31) [keep: ] quote: "The daily average number of transactions also rose 11.8 percent on-year to 33.64 million."
  - p25 Share of PG service value accounted for by credit card payment processing, South = **75** % (2025-01-01..2025-12-31) [keep: ] quote: "Growth in PG services was led by credit card payment processing, which accounts for about 75 percent of the total by value."
  - p26 Daily average number of prepaid electronic payment service transactions in South = **36,540,000** transactions (2025-01-01..2025-12-31) [keep: ] quote: "The daily average usage of prepaid electronic payment services also gained 8.0 percent from a year earlier to 36.54 million transactions"
  - p27 Year-on-year growth rate of daily average prepaid electronic payment transaction = **8** % (2025-01-01..2025-12-31) [keep: ] quote: "The daily average usage of prepaid electronic payment services also gained 8.0 percent from a year earlier to 36.54 million transactions"
  - p28 Daily average value of prepaid electronic payment services in South Korea, 2025 = **1,310,000,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "while their value increased 11.0 percent to 1.31 trillion won in 2025"
  - p29 Year-on-year growth rate of daily average prepaid electronic payment value, Sout = **11** % (2025-01-01..2025-12-31) [keep: ] quote: "while their value increased 11.0 percent to 1.31 trillion won in 2025"
  - p30 Daily average number of simple payment transactions in South Korea, 2025 = **35,570,000** transactions (2025-01-01..2025-12-31) [keep: ] quote: "The daily average number of simple payment transactions reached 35.57 million last year, up 14.9 percent from a year earlier"
  - p31 Year-on-year growth rate of daily average simple payment transaction count, Sout = **14.9** % (2025-01-01..2025-12-31) [keep: ] quote: "The daily average number of simple payment transactions reached 35.57 million last year, up 14.9 percent from a year earlier"
  - p32 Daily average value of simple payment services in South Korea, 2025 = **1,110,000,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "while their value rose 14.6 percent to 1.11 trillion won"
  - p33 Year-on-year growth rate of daily average simple payment value, South Korea, 202 = **14.6** % (2025-01-01..2025-12-31) [keep: ] quote: "while their value rose 14.6 percent to 1.11 trillion won"
  - p34 Share of electronic financial service companies (Naver Pay, Kakao Pay) in simple = **54.9** % (2025-01-01..2025-12-31) [keep: ] quote: "electronic financial service companies, such as Naver Pay and Kakao Pay, increased their share to 54.9 percent last year from the previous year's 50.5 percent"
- `https://en.infomaxai.com/news/articleView.html?idxno=102959` -> **snapshot** (snapshot 20260130131823); points raw/verified 15/0
- dropped by code checks: 16 (period year 2024 does not appear in the page text or URL (likely mis-dated): 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 14)

### d7 [forecasts_markets] industry forecaster

Hypothesis: A published 2026 annual Korean e-commerce or online shopping forecast can be multiplied by the historical August share of annual transactions. The route is a sanity check rather than a primary estimate because forecast scope often differs from the official series.

Queries issued by the searcher: 한국 이커머스 시장 규모 2026 전망; 온라인쇼핑 거래액 2026 전망; 2025년 8월 온라인쇼핑 거래액 조 원 국가데이터처 온라인쇼핑동향; 2024년 연간 온라인쇼핑 거래액 242조 통계청

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thebell.co.kr/front/newsview.asp?click=F&key=202602040907568360101882` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.theguru.co.kr/news/article_print.html?no=97988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dnews.co.kr/uhtml/view.jsp?idxno=202605171039185880976` -> **snapshot** (snapshot 20260519075430); points raw/verified 14/12
  - p35 South Korea total online shopping transaction amount (all categories, online+mob = **72,164,300,000,000** as written "72조1643억원", value check pending KRW (2026-01-01..2026-03-31) [keep: ] quote: "전체 쇼핑 거래액은 72조1643억원으로 전년 동기 대비 9.2% 늘었지만"
  - p36 Year-on-year growth rate of total online shopping transaction amount, Q1 = **9.2** % (2026-01-01..2026-03-31) [keep: ] quote: "전체 쇼핑 거래액은 72조1643억원으로 전년 동기 대비 9.2% 늘었지만"
  - p37 Year-on-year growth rate of online shopping transaction amount excluding cars an = **7.7** % (2026-01-01..2026-03-31) [keep: ] quote: "이를 제외한 거래액 신장률은 7.7%에 그쳤다."
  - p38 Quarter-on-quarter change in online shopping product transaction amount, Q1 = **51,000,000,000** KRW (2026-01-01..2026-03-31) [DISCARD: The table value is positive but the quoted text says product transaction amount decreased by 510억원 (-0.1%); sign is ambi] quote: "전분기 대비 상품 거래액은 오히려 510억원 줄었고(-0.1%)"
  - p39 Share of online products in retail sales, Q1 = **29.4** % (2026-01-01..2026-03-31) [keep: ] quote: "소매판매액 중 온라인 상품 비중도 28.2%에서 29.4%로 1.2%포인트 오르는 데 그쳤다."
  - p40 Coupang Product Commerce revenue, Q1 = **10,513,900,000,000** as written "10조5139억원", value check pending KRW (2026-01-01..2026-03-31) [keep: ] quote: "쿠팡의 프로덕트커머스 매출은 10조5139억원으로 지난해 같은 기간보다 5.4% 늘어나는 데 그쳤지만"
  - p41 Naver commerce segment revenue, Q1 = **1,839,800,000,000** as written "1조8398억원", value check pending KRW (2026-01-01..2026-03-31) [keep: ] quote: "네이버 커머스는 광고ᆞ서비스 분리 공시 첫 분기에 부문 매출 1조8398억원(+14.7%)을 기록하며"
  - p42 Kurly Q1 transaction amount (GMV) = **1,089,100,000,000** as written "1조891억원", value check pending KRW (2026-01-01..2026-03-31) [keep: ] quote: "컬리의 1분기 거래액은 1조891억원으로 29% 늘며 분기 첫 1조원을 돌파했다."
  - p43 11st Q1 revenue = **93,100,000,000** KRW (2026-01-01..2026-03-31) [keep: ] quote: "1분기 매출 931억원으로 17.6% 감소했다."
  - p44 SSG.com Q1 revenue = **322,600,000,000** KRW (2026-01-01..2026-03-31) [keep: ] quote: "SSG닷컴은 매출 3226억원으로 9.6% 줄었고 영업손실은 219억원으로 전년 동기보다 38억원 늘었다."
  - p45 Lotte On Q1 revenue change (year-on-year) = **3.8** % (2026-01-01..2026-03-31) [DISCARD: The table describes a positive 3.8% revenue change, but the quote says revenue decreased 3.8%; sign is ambiguous and the] quote: "롯데온도 매출은 3.8% 감소했지만 영업손실을 27억원 축소했다."
  - p46 E-Mart equity-method loss related to Gmarket, Q1 (estimated) = **50,000,000,000** KRW (2026-01-01..2026-03-31) [DISCARD: E-Mart equity-method loss estimate related to Gmarket is not an online shopping transaction value and cannot be converte] quote: "1분기 이마트 지분법 손실 약 500억원에 G마켓 적자 확대가 일부 반영된 것으로 추산된다."
- dropped by code checks: 2 (period_end missing or unparseable: 1; number: low/high given but value_as_written is not a range: 1)

### d8 [shocks] macro and calendar analyst

Hypothesis: August 2026 calendar and weather effects (weekday count, heatwave, summer vacation, back-to-school, Liberation Day, Chuseok timing outside August) may shift online shopping relative to a simple seasonal factor. The route adjusts the historical August seasonal factor using measurable anomalies in temperature, consumer sentiment, and weekly card spending.

Queries issued by the searcher: 2026년 8월 폭염 특보; 소비자심리지수 2026년 8월 한국은행; 2026년 8월 카드사용액 증가율 주간 신한카드; 온라인쇼핑 거래액 2026년 7월 통계청

- `https://www.yna.co.kr/amp/view/AKR20260824149100002` -> **snapshot** (snapshot 20260825050624); points raw/verified 12/12
  - p47 South Korea Consumer Sentiment Index (CCSI), August 2026 = **104** index points (2026-08-01..2026-08-31) [keep: ] quote: "8월 소비자심리지수(CCSI)는 104.5로 전월보다 2.3포인트(p) 하락했다."
  - p48 CCSI month-on-month change, August 2026 = **2.3** index points (2026-08-01..2026-08-31) [keep: ] quote: "8월 소비자심리지수(CCSI)는 104.5로 전월보다 2.3포인트(p) 하락했다."
  - p49 Current economic judgment sub-index, August 2026 = **79** index points (2026-08-01..2026-08-31) [keep: ] quote: "CCSI를 구성하는 6개 지수 중 현재경기판단(79·-5p)이 가장 큰 폭으로 내렸다."
  - p50 Future economic outlook sub-index, August 2026 = **89** index points (2026-08-01..2026-08-31) [keep: ] quote: "향후경기전망(89·-3p)과 취업기회전망(86·-3p)도 4월(-10p·-7p) 이후 가장 큰 폭으로 하락했으며"
  - p51 Household income outlook sub-index, August 2026 = **100** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p52 Consumption expenditure outlook sub-index, August 2026 = **109** index points (2026-08-01..2026-08-31) [keep: ] quote: "생활형편전망(97·-1p) , 현재생활형편(92·-1p), 가계수입전망(100·-1p), 소비지출전망(109·-1p) 등도 일제히 내렸다."
  - p53 Current household savings index, August 2026 = **94** index points (2026-08-01..2026-08-31) [keep: ] quote: "현재가계저축지수(94)는 전월보다 3p 하락해 작년 5월(93) 이후 1년 3개월 만에 가장 낮았다."
  - p54 Current household debt index, August 2026 = **100** index points (2026-08-01..2026-08-31) [keep: ] quote: "현재 가계부채 수준에 대한 인식을 나타내는 현재가계부채지수는 100으로 전월과 같은 수준을 유지했다."
  - p55 Housing price outlook index, August 2026 = **125** index points (2026-08-01..2026-08-31) [keep: ] quote: "주택가격전망지수(125)는 전월보다 2p 하락했다."
  - p56 Interest rate level outlook index, August 2026 = **125** index points (2026-08-01..2026-08-31) [keep: ] quote: "금리수준전망지수(125)는 1p 하락했다."
  - p57 Expected inflation rate, next 12 months, August 2026 = **2.7** % (2026-08-01..2026-08-31) [keep: ] quote: "향후 1년의 소비자물가 상승률 전망치(2.7%)는 전월과 같은 수준을 유지했다."
  - p58 CCSI April 2026 month-on-month change (comparison) = **-7.8** index points (2026-04-01..2026-04-30) [keep: ] quote: "다만 하락 폭은 중동 전쟁 영향으로 크게 내렸던 지난 4월(-7.8p)보다는 작았다."
- `https://www.khan.co.kr/article/202608031718001/amp` -> **snapshot** (snapshot 20260805073353); points raw/verified 15/11
  - p59 Daily maximum temperature recorded in Goryeong, Gyeongbuk (heatwave peak) = **41.2** degrees Celsius (2026-08-03..2026-08-03) [keep: ] quote: "기상청에 따르면 3일 고령의 일 최고 기온이 41.2도를 기록했다."
  - p60 Daily maximum temperature in Gwangyang and Daegu = **41.1** degrees Celsius (2026-08-03..2026-08-03) [keep: ] quote: "광양과 대구(이상 41.1도), 경남 합천(41도) 등 영남권 곳곳에서도 40도를 웃도는 폭염이 이어졌다."
  - p61 Daily maximum temperature in Hapcheon, Gyeongnam = **41** degrees Celsius (2026-08-03..2026-08-03) [keep: ] quote: "광양과 대구(이상 41.1도), 경남 합천(41도) 등 영남권 곳곳에서도 40도를 웃도는 폭염이 이어졌다."
  - p62 Perceived temperature (heat index) in Hanam, Gyeonggi = **39.1** degrees Celsius (2026-08-03..2026-08-03) [keep: ] quote: "경기 하남의 체감온도는 39.1도까지 올랐고 서울 강남의 체감 온도가 38도를 넘어서는 등"
  - p63 Perceived temperature (heat index) in Gangnam, Seoul = **38** degrees Celsius (2026-08-03..2026-08-03) [keep: ] quote: "서울 강남의 체감 온도가 38도를 넘어서는 등 도심 곳곳에서 사람 체온을 웃도는 수준의 무더위가 이어졌다."
  - p64 Average number of tropical nights nationwide (62 stations), Jun 1 to Aug 2, reco = **10.6** days (2026-06-01..2026-08-02) [keep: ] quote: "지난 6월1일부터 이달 2일까지 전국 62개 지점에서 발생한 열대야 일수는 평균 10.6일로, 1973년 관측 이래 가장 많았다."
  - p65 Previous record average tropical nights nationwide (2024) = **9.7** days (2024-01-01..2024-12-31) [keep: ] quote: "종전 최다 기록은 2024년의 9.7일이었다."
  - p66 Cumulative heat-related illness patients nationwide as of Aug 2 = **2,025** people (2026-05-15..2026-08-02) [keep: ] quote: "2일 기준 누적 온열질환자 수는 전날 대비 108명 증가한 2025명으로 집계됐다."
  - p67 Daily increase in heat-related illness patients (Aug 1 to Aug 2) = **108** people (2026-08-02..2026-08-02) [keep: ] quote: "2일 기준 누적 온열질환자 수는 전날 대비 108명 증가한 2025명으로 집계됐다."
  - p68 Cumulative estimated heat-related deaths nationwide as of Aug 2 = **16** people (2026-05-15..2026-08-02) [keep: ] quote: "추정 사망자는 전날보다 1명 늘어 누적 16명이 됐다."
  - p69 Forecast daily maximum temperature range nationwide on Aug 4 = **34** (range 30..38) as written "30~38", value check pending degrees Celsius (2026-08-04..2026-08-04) [keep: ] quote: "낮 최고기온은 30~38도까지 오르며 무더위가 이어질 것으로 예보됐다."
- `https://www.yna.co.kr/view/MYH20260805015400038?section=safe/video` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://app1.ytn.co.kr/app_news_view.php?key=202608231909530431&s_mcd=0108` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### b1 [own_history] official monthly series

Hypothesis: Finding Q2 2026 and June 2026 Online Shopping Trends totals, plus earlier August monthly values, would replace the Q1-only growth proxy with a closer, August-relevant trend and seasonal factor, directly reducing uncertainty in m1/m2.

Queries issued by the searcher: 온라인쇼핑동향 2026년 6월 거래액; Online Shopping Trends June 2026 Statistics Korea transaction amount; 온라인쇼핑 거래액 2023년 8월 2024년 8월 2025년 8월; 2025년 8월 온라인쇼핑동향 거래액 조원 전년동월대비; "2025년 8월" 온라인쇼핑 거래액 "21조" 국가데이터처 통계청

- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kostat.go.kr/board.es?mid=a20101000000&bid=11722&list_no=433060&act=view&mainXml=Y` -> **snapshot** (snapshot 20250811121545); points raw/verified 4/4
  - p70 South Korea total online shopping transaction value, August 2024 = **19,558,000,000,000** KRW (2024-08-01..2024-08-31) [keep: ] quote: "The online shopping transaction value marked 19.5580 trillion won in August 2024, rising 1.9% from August 2023."
  - p71 South Korea total online shopping transaction value, year-on-year growth August  = **1.9** % (2024-08-01..2024-08-31) [keep: ] quote: "The online shopping transaction value marked 19.5580 trillion won in August 2024, rising 1.9% from August 2023."
  - p72 South Korea mobile shopping transaction value, August 2024 = **14,981,700,000,000** KRW (2024-08-01..2024-08-31) [keep: ] quote: "The mobile shopping transaction value marked 14.9817 trillion won in August 2024, rising 5.4% from August 2023."
  - p73 South Korea mobile shopping transaction value, year-on-year growth August 2024 v = **5.4** % (2024-08-01..2024-08-31) [keep: ] quote: "The mobile shopping transaction value marked 14.9817 trillion won in August 2024, rising 5.4% from August 2023."
- `https://www1.edaily.co.kr/News/Read?newsId=03191446645543712&mediaCodeNo=257` -> **snapshot** (snapshot 20260803080838); points raw/verified 15/14
  - p74 South Korea online shopping transaction amount, June 2026, all categories, onlin = **24,606,700,000,000** as written "24조6067억원", value check pending KRW (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p75 South Korea online shopping transaction amount, Q2 2026, all categories = **73,608,500,000,000** as written "73조6085억원", value check pending KRW (2026-04-01..2026-06-30) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p76 South Korea online shopping transaction amount, Q1 2026, all categories = **72,128,600,000,000** as written "72조1286억원", value check pending KRW (2026-01-01..2026-03-31) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p77 South Korea online shopping transaction amount, H1 2026, all categories = **145,737,100,000,000** as written "145조7371억원", value check pending KRW (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 온라인쇼핑 거래액은 145조7371억원으로 집계됐다."
  - p78 South Korea mobile shopping transaction amount, June 2026 = **18,927,000,000,000** as written "18조9270억원", value check failed KRW (2026-06-01..2026-06-30) [keep: ] quote: "6월 모바일쇼핑 거래액은 18조9270억원으로 전년 동월보다 9.8% 증가했다."
  - p79 Mobile share of total online shopping transaction amount, June 2026 = **76.9** % (2026-06-01..2026-06-30) [keep: ] quote: "전체 온라인쇼핑 거래액에서 모바일이 차지하는 비중은 76.9%로 지난해 같은 달보다 0.7%포인트 낮아졌다."
  - p80 Year-on-year change in South Korea online shopping transaction amount, June 2026 = **10.7** % (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p81 Month-on-month change in South Korea online shopping transaction amount, June 20 = **1.7** % (2026-06-01..2026-06-30) [keep: ] quote: "다만 역대 2위 수준이었던 전월과 비교하면 1.7% 감소했다."
  - p82 Year-on-year change in South Korea online shopping transaction amount, Q2 2026 = **10.1** % (2026-04-01..2026-06-30) [keep: ] quote: "2분기 거래액은 전년 동기보다 10.1%, 전분기보다 2.1% 늘었다."
  - p83 Quarter-on-quarter change in South Korea online shopping transaction amount, Q2  = **2.1** % (2026-04-01..2026-06-30) [keep: ] quote: "2분기 거래액은 전년 동기보다 10.1%, 전분기보다 2.1% 늘었다."
  - p84 Year-on-year change in South Korea online shopping transaction amount, H1 2026 = **9.6** % (2026-01-01..2026-06-30) [keep: ] quote: "지난해 상반기 132조9541억원보다 9.6% 증가한 규모다."
  - p85 South Korea online product transaction amount excluding travel and food services = **100,308,000,000,000** as written "100조3080억원", value check pending KRW (2026-01-01..2026-06-30) [keep: ] quote: "여행과 음식서비스 등을 제외한 온라인 상품 거래액은 상반기 100조3080억원을 기록하며 100조원을 넘어섰다."
  - p86 Online product share of total retail sales, Q2 2026 = **30** % (2026-04-01..2026-06-30) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p87 Online product share of total retail sales, Q1 2026 = **29.4** % (2026-01-01..2026-03-31) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b2 [related_series] high-frequency payment indicator

Hypothesis: August 2026 card/remote online spending or PG data published before the September release would provide an independent August growth signal and help calibrate the PG coverage share used in m3.

Queries issued by the searcher: 2026년 8월 카드 온라인 매출; 온라인쇼핑 거래액 2026년 7월 통계청; 2026년 8월 카드 승인액 여신금융협회 8월 카드사용액; 2026년 8월 온라인 결제 금액 카드 매출 증가율 주간

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newspub.kr/content?nid=6a8261f47d49575a759a58fa&rss=1&aid=6863d4e8ce080a6be2a8b0e9&mid=6863d50be0fc5b5c40aaee65&utm_source=6863d50be0fc5b5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kbthink.com/securities-view.html?docId=20260812134944083K` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.financialpost.co.kr/news/articleView.html?idxno=268381` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] scope and category composition

Hypothesis: A service/category breakdown (travel, culture, food delivery, e-coupons vs physical goods) would let the parcel-volume route be corrected for non-parceled services and would also test whether Q1 headline growth is representative of August.

Queries issued by the searcher: 온라인쇼핑동향 월별 서비스 거래액 비중 여행 문화; online shopping Korea 2025 transaction amount by category travel culture services share KOSIS; 2026년 7월 온라인쇼핑동향 국가데이터처; 2025년 8월 온라인쇼핑동향 상품군별 거래액 여행 및 교통서비스 음식서비스

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=446725` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=439110&tag=&nPage=1&ref_bid=203,204,205,206,207,210,211,11109,11113,11814,213,21` -> **snapshot** (snapshot 20251116035540); points raw/verified 15/14
  - p88 South Korea total online shopping transaction amount, September 2025 = **23,795,600,000,000** as written "23조 7,956억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "2025년 9월 온라인쇼핑 거래액은 23조 7,956억원으로 전년동월대비 13.3% 증가했으며"
  - p89 South Korea mobile shopping transaction amount, September 2025 = **18,055,200,000,000** as written "18조 552억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 중 모바일쇼핑 거래액은 18조 552억원으로 11.0% 증가"
  - p90 Mobile share of total online shopping transaction amount, September 2025 = **75.9** % (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액 비중은 75.9%로 전년동월(77.5%)에 비해 1.6%p 감소"
  - p91 YoY growth of culture and leisure services online shopping transaction amount, S = **-8.2** % (2025-09-01..2025-09-30) [keep: ] quote: "문화 및 레저서비스(-8.2%) 등에서 감소했으나"
  - p92 YoY growth of automobiles and automobile parts online shopping transaction amoun = **136** % (2025-09-01..2025-09-30) [keep: ] quote: "자동차 및 자동차용품(136.4%), 음‧식료품(17.7%), 여행 및 교통서비스(12.0%) 등에서 증가"
  - p93 YoY growth of food and beverages online shopping transaction amount, September 2 = **17.7** % (2025-09-01..2025-09-30) [keep: ] quote: "자동차 및 자동차용품(136.4%), 음‧식료품(17.7%), 여행 및 교통서비스(12.0%) 등에서 증가"
  - p94 YoY growth of travel and transport services online shopping transaction amount,  = **12** % (2025-09-01..2025-09-30) [keep: ] quote: "자동차 및 자동차용품(136.4%), 음‧식료품(17.7%), 여행 및 교통서비스(12.0%) 등에서 증가"
  - p95 MoM growth of food services online shopping transaction amount, September 2025 = **-9.7** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비로는 음식서비스(-9.7%) 등에서 감소했으나"
  - p96 MoM growth of food and beverages online shopping transaction amount, September 2 = **11.8** % (2025-09-01..2025-09-30) [keep: ] quote: "음·식료품(11.8%), 의복(24.2%) 등에서 증가"
  - p97 MoM growth of clothing online shopping transaction amount, September 2025 = **24.2** % (2025-09-01..2025-09-30) [keep: ] quote: "음·식료품(11.8%), 의복(24.2%) 등에서 증가"
  - p98 General mall (comprehensive mall) online shopping transaction amount, September  = **13,099,800,000,000** as written "13조 998억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "종합몰은 12.0% 증가한 13조 998억원을"
  - p99 Specialty mall online shopping transaction amount, September 2025 = **10,695,800,000,000** as written "10조 6,958억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "전문몰은 15.0% 증가한 10조 6,958억원을 기록"
  - p100 Online mall online shopping transaction amount, September 2025 = **18,285,700,000,000** as written "18조 2,857억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인몰은 12.3% 증가한 18조 2,857억원을"
  - p101 Online/offline combined mall online shopping transaction amount, September 2025 = **5,509,900,000,000** as written "5조 5,099억원", value check pending KRW (2025-09-01..2025-09-30) [keep: ] quote: "온·오프라인병행몰은 16.9% 증가한 5조 5,099억원을 기록"
- `https://sri.kostat.go.kr/boardDownload.es?bid=241&list_no=443337&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=444909&mid=a10301120300&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] Same YTN article on August 2025 online shopping. p1/p2 give the total and its YoY growth; p3-p6 give mobile amount, growth, and share. They are internally consistent but share one source and one surve
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20'] Same etnews article on domestic parcel volume. Monthly 2026 volumes are consistent with H1 2026 cumulative volume; H1 growth rates are derived from cumulative volumes. p17 is a rounded 'first year to 
- corroborating: ['p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] Same Korea Herald article on payment-gateway, prepaid, and simple-payment statistics. The measures overlap: simple payments and PG payments can process the same transaction, and PG includes non-shoppi
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p39'] Same dnews article on Q1 2026 online shopping. p35 is the total and p36 its YoY growth; p37 is a narrower ex-cars/telecom growth rate, so it is not a contradiction. p38 has a sign conflict between the
- contextual: ['p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46'] Same dnews article, platform company results. These are operator revenue/GMV/loss figures with different scopes from the official online shopping transaction total; they are useful context but not dir
- corroborating: ['p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] Same YNA CCSI article for August 2026. The subindices and expectations describe consumer sentiment, not transaction values. They can inform a downward or upward adjustment to growth but do not measure
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] Same Khan weather article. These document an extreme August 2026 heatwave and its health effects. They are contextual for possible online shopping shifts, but do not give a transaction amount.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] Same YTN article for August 2025. p1 and p3 imply p5's mobile share, and p2/p4/p6 give the corresponding growth rates. They are internally consistent but are one source, not independent confirmation.
- conflicting: ['p70', 'p71', 'p72', 'p73'] Older-vintage Statistics Korea August 2024 total and mobile values. At the same stated scope they do not reconcile with p1/p2 and p3/p4, indicating a methodology/revision break between the 2024 and 20
- corroborating: ['p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87'] Edaily 2026 monthly/quarterly snapshot. p76 plus p75 equals p77; p74 has June YoY p80 and MoM p81; p78/p79 describe mobile June; p75 has Q2 YoY p82 and QoQ p83; p77 has H1 YoY p84; p85-p87 provide pro
- corroborating: ['p35', 'p36', 'p37', 'p39'] Older Q1 2026 snapshot. p35 differs only slightly from later p76, while p39 matches later p87; p36 and p37 provide Q1 growth and scope context. Use the later p76/p87 for Q1 levels if needed.
- corroborating: ['p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101'] September 2025 release. Mall and category subtotals reconcile with p88, and mobile p89/p90 is consistent. Different month, so useful for structure and seasonality context rather than direct August 202
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20'] Parcel-volume data are internally consistent: monthly 2026 values sum to p9, and p10/p9 and p11/p10 match p18/p19. This is a physical-flow cross-check, but there is no August 2026 parcel volume or ave
- corroborating: ['p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] 2025 PG and electronic-payment article. PG daily value/growth p21/p22 are usable for a payment-system route; prepaid and simple-payment series overlap with PG and are not additive. Use p25 only as con
- corroborating: ['p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] August 2026 CCSI and subindices. They show softer consumer sentiment than mid-2026, supporting a modest downward adjustment to recent online-shopping growth, but they do not directly measure transacti
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] Early-August 2026 heatwave evidence. Extreme heat can shift spending between online and offline, but the net effect on total online shopping is ambiguous; use as context for uncertainty, not as a dire

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY growth multiplier on June 2026 online shopping growth | 0.9 | 0.7..1.1 | 0.7..1.1 | ratio | m1 (m1) | June 2026 total online shopping YoY growth is p80. August 2026 CCSI fell 2.3 points (p48) and most subindices weakened (p49-p52), while heatwave effects on online spending are ambiguous (p59-p69). A multiplier slightly below 1 puts August growth near the H1/Q2 range rather than the June monthly rate | June 2026 growth is a relevant proxy for August 2026 and there is no major methodology or category break. | A direct August 2026 card, PG, or online-shopping indicator showing growth clearly outside the implied range, or evidence of a large methodology/category change. |
| a2 | August 2026 YoY growth multiplier on Q2 2026 online shopping growth | 0.95 | 0.75..1.15 | 0.75..1.15 | ratio | m2 (m2) | Q2 2026 total online shopping YoY growth is p82; H1 growth p84 is lower than June p80. August sentiment softened (p47/p48), so a multiplier near 1 keeps August near the broader H1/Q2 trend rather than assuming acceleration. | Q2 2026 growth is a relevant proxy for August 2026 and seasonality is not strongly different. | A direct August 2026 indicator outside the implied range, or evidence that Q2 growth was driven by transient categories absent in August. |
| a3 | August online shopping transaction amount as a share of August PG service value | 0.47 | 0.4..0.55 | 0.3317..0.6633 (widened) | fraction | m3 (m3) | 2025 PG daily average value p21 scaled to 31 days is about 48.05 trillion won. Current-vintage August 2025 online shopping reconstructed from p3/p5 is about 22.48 trillion, implying a ratio near 0.47. The range covers payment-mix, seasonality, and scope differences between PG services and the offici | PG coverage and online-shopping scope in August 2026 remain broadly similar to 2025, with no major payment-mix shift. | A PG-online reconciliation showing a materially different coverage share, or a large shift between card, account-transfer, and simple-payment channels. |
| a4 | 2026 PG growth multiplier on 2025 PG growth | 1 | 0.7..1.3 | 0.7..1.3 | ratio | m3 (m3) | 2025 PG daily average value grew 9.2% (p22). 2026 online-shopping growth signals p80 (10.7%) and p82 (10.1%) are similar, so 2026 PG growth is centered at the 2025 rate with wide uncertainty for payment-mix and macro shifts. | PG growth in 2026 is broadly similar to 2025 and there is no major regulatory or payment-method shock. | 2026 PG growth clearly outside the implied range, or evidence that PG and online-shopping growth diverged sharply. |
| a5 | August 2026 mobile share of total online shopping | 0.78 | 0.75..0.81 | 0.5511..1.102 (widened) | fraction | m4 (m4) | August 2025 mobile share was 79.4% (p5), but June 2026 mobile share was 76.9% (p79) and down year-on-year. August 2026 is centered at 78% with a range covering continued mild decline or stabilization. | Mobile share continues its recent mild decline and is not disrupted by a new platform shift. | Preliminary August 2026 mobile/total data showing a share outside the stated range, or evidence of a mobile-specific channel shock. |
| a6 | August 2026 mobile growth multiplier on August 2025 mobile YoY growth | 1 | 0.7..1.3 | 0.7..1.3 | ratio | m4 (m4) | August 2025 mobile shopping YoY growth was 8.9% (p4), used as the base trend for August 2026 mobile growth. A multiplier near 1 with a wide range reflects August 2026 sentiment softening (p48) and possible mobile-specific promotions or platform shifts. | August 2025 mobile growth is a relevant proxy for August 2026 mobile growth and there is no mobile-specific shock. | A direct August 2026 mobile indicator outside the implied range, or evidence of a mobile-specific promotion or platform disruption. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 24,542,254,096,365 | ['p3', 'p5', 'p80'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 24,568,803,626,314 | ['p3', 'p5', 'p82'] / ['a2'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 24,532,438,317,859 | ['p21', 'p22'] / ['a3', 'a4'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 24,830,636,543,792 | ['p3', 'p4'] / ['a5', 'a6'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **24,618,226,124,940** KRW, 80% interval [16,620,771,673,384, 36,463,833,897,025] KRW, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for the nominal total value of online shopping transactions in South Korea for August 2026 (all categories, online plus mobile, current prices, seasonally unadjusted) is 24,618,226,124,940 KRW (80% model-based interval 16,620,771,673,384 to 36,463,833,897,025 KRW).

Four methods were averaged with equal weights (25% each). All anchor on the current-vintage August 2025 level reconstructed from 17,848,900,000,000 KRW and 79.4%. m1 and m2 update it using 10.7% and 10.1% adjusted by 0.9 and 0.95. m3 uses the payment-gateway route (1,550,000,000,000 KRW, 9.2%) with coverage share 0.47 and growth multiplier 1. m4 uses mobile growth 8.9% with share 0.78 and multiplier 1.

Observed inputs are the 2025 levels and 2026 growth rates; the multipliers, coverage share, and mobile share are analyst assumptions, so the methods share the same underlying series and are not independent. The interval reflects input uncertainty only, not demonstrated accuracy. The main risk is that June/Q2 growth and the assumed multipliers misstate August. Better evidence would be July 2026 online-shopping data and August card or PG spending.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 YoY growth multiplier on June 2026 online shopping growth: 0.9 ratio, range 0.7 to 1.1; used by m1. Overturned by: A direct August 2026 card, PG, or online-shopping indicator showing growth clearly outside the implied range, or evidence of a large methodology/category change.
- a2 August 2026 YoY growth multiplier on Q2 2026 online shopping growth: 0.95 ratio, range 0.75 to 1.15; used by m2. Overturned by: A direct August 2026 indicator outside the implied range, or evidence that Q2 growth was driven by transient categories absent in August.
- a3 August online shopping transaction amount as a share of August PG service value: 0.47 fraction, range 0.3317 to 0.6633 (range widened by code); used by m3. Overturned by: A PG-online reconciliation showing a materially different coverage share, or a large shift between card, account-transfer, and simple-payment channels.
- a4 2026 PG growth multiplier on 2025 PG growth: 1 ratio, range 0.7 to 1.3; used by m3. Overturned by: 2026 PG growth clearly outside the implied range, or evidence that PG and online-shopping growth diverged sharply.
- a5 August 2026 mobile share of total online shopping: 0.78 fraction, range 0.5511 to 1.102 (range widened by code); used by m4. Overturned by: Preliminary August 2026 mobile/total data showing a share outside the stated range, or evidence of a mobile-specific channel shock.
- a6 August 2026 mobile growth multiplier on August 2025 mobile YoY growth: 1 ratio, range 0.7 to 1.3; used by m4. Overturned by: A direct August 2026 mobile indicator outside the implied range, or evidence of a mobile-specific promotion or platform disruption.

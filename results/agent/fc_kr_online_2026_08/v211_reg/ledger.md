# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Total value of online shopping transactions in South Korea during August 2026, as reported in the National Data Office (formerly Statistics Korea) monthly Online Shopping Trends (온라인쇼핑동향) release — i.e., the aggregate online shopping transaction amount (거래액) for the reference month, all commodities, | unit KRW | period 2026-08-01..2026-08-31 | publisher National Data Office (국가데이터처, formerly Statistics Korea / 통계청)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] National statistics publisher time series

Hypothesis: The target is a continuation of a monthly series; recent published months (through ~July 2026) plus the same-month prior years (Aug 2023, Aug 2024, Aug 2025) give level, trend, and August seasonal factor. Target ≈ latest level × trend growth × August seasonal index.

Queries issued by the searcher: 온라인쇼핑동향 거래액 월별 2026 통계청; Statistics Korea online shopping trends monthly transaction value 2025 2026; 2025년 8월 온라인쇼핑동향 거래액 조원; 온라인쇼핑 거래액 월별 시계열 2024년 8월 2023년 8월 통계표

- `https://www.speconomy.com/news/articleView.html?idxno=418479` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=438862&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.heraldk.com/article/2026083121430422094` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Retail sales / consumption aggregate

Hypothesis: Online shopping is a large share of total retail sales; total retail sales value (or household consumption) × online share gives an independent level estimate. Target ≈ monthly retail sales × online-penetration share, adjusted for scope differences.

Queries issued by the searcher: 온라인쇼핑 거래액 소매판매 비중 통계청; 소매판매액 월별 2026 통계청 온라인쇼핑동향; 2025년 8월 온라인쇼핑동향 거래액 25조 전년동월대비; 2026년 6월 온라인쇼핑동향 소매판매액 비중 국가데이터처

- `https://www.gov.kr/portal/ntnadmNews/4844676` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=241&list_no=444909&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Mobile vs total split and category composition

Hypothesis: Total online = mobile + PC (non-mobile). If mobile transaction value and mobile share are available, total can be reconstructed; category-level series (food, cosmetics, electronics, travel) can be summed as a cross-check.

Queries issued by the searcher: 온라인쇼핑동향 모바일 거래액 비중 2026년 6월; 온라인쇼핑 거래액 2026년 7월 통계청; 2025년 8월 온라인쇼핑동향 거래액 모바일 비중; 국가데이터처 온라인쇼핑동향 2026년 8월 거래액

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260901057900002?input=1195m` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsprime.co.kr/news/article/?no=745935` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] Payment/card transaction throughput

Hypothesis: Online purchases are settled through card/electronic payment rails; aggregate e-commerce card payment value (전자상거래 결제액 or 신용카드 온라인 결제) tracks the target closely. Target ≈ online card payment value × coverage adjustment.

Queries issued by the searcher: 전자상거래 결제액 월별 한국은행 2026; 온라인쇼핑동향 거래액 2026년 6월 통계청; 한국은행 전자상거래 결제액 신용카드 온라인 결제 통계 2026; 2026년 7월 온라인쇼핑동향 거래액 국가데이터처; 한국은행 2025년 중 전자지급서비스 이용 현황 전자지급결제대행 PG 신용카드 지급대행 일평균

- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://biz.heraldcorp.com/article/10828802` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.einfomax.co.kr/news/articleView.html?idxno=4428301` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Calendar and event effects

Hypothesis: August 2026 has no major Korean gift-giving holiday, but summer vacation/travel, heat waves, and any major platform promotions (e.g., 8.8/8.15 sales) shift the level. Quantify deviation of Aug 2026 from the seasonal norm using event/promotion signals.

Queries issued by the searcher: 온라인쇼핑동향 2026년 8월 거래액; August 2026 Korea e-commerce sales event 8.8 promotion; 2025년 8월 온라인쇼핑동향 거래액 전년동월대비 증가; 2026년 8월 폭염 여행 예약 급증 항공권 온라인 판매

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=447300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260807092100030` -> **snapshot** (snapshot 20260809042615); points raw/verified 14/14
  - p1 Lotte Department Store Nowon food hall promotion maximum discount rate for food  = **7** % (2026-08-04..2026-08-08) [DISCARD: Offline department-store food-hall discount rate; no route to the online-shopping transaction total.] quote: "식품 상품군 구매 고객을 대상으로 최대 7% 혜택을 제공하고"
  - p2 Lotte Department Store Nowon food club first-come members receiving 5,000 won Le = **2,000** people (2026-08-04..2026-08-08) [DISCARD: Offline department-store membership count; irrelevant to online transaction value.] quote: "노원점 식품 클럽(노원 미식회) 가입 고객 선착순 2천명에게는 프리미엄 식료품점 '레피세리' 5천원 할인권을 증정한다."
  - p3 Le Picerie discount voucher value for Lotte Nowon food club members = **5,000** KRW (2026-08-04..2026-08-08) [DISCARD: Offline voucher value; irrelevant to online transaction value.] quote: "프리미엄 식료품점 '레피세리' 5천원 할인권을 증정한다."
  - p4 Shinsegae Department Store Gangnam popup discount rate on all products = **10** % (2026-08-08..2026-08-12) [DISCARD: Offline popup discount rate; no usable conversion to online transaction total.] quote: "팝업스토어에서는 모든 상품을 10% 할인하고, 30만원 이상 구매 시 사은품을 증정한다."
  - p5 Shinsegae popup minimum purchase threshold for gift = **300,000** KRW (2026-08-08..2026-08-12) [DISCARD: Offline popup gift threshold; irrelevant.] quote: "팝업스토어에서는 모든 상품을 10% 할인하고, 30만원 이상 구매 시 사은품을 증정한다."
  - p6 E-Mart T-Cafe Americano price = **1,000** KRW (2026-08-08..2026-08-08) [DISCARD: Single coffee price at E-Mart T-Cafe; irrelevant to online transaction total.] quote: "T-카페에서는 대형 피자부터 닭 반 마리 쌀국수, 1천원 아메리카노 등 고객 선호도가 높은 상품을 선보이며"
  - p7 Lotte Mart 'Mat-kangs' promotion discount rate on Australian beef = **50** % (2026-08-08..2026-08-12) [DISCARD: Offline grocery beef discount rate; irrelevant.] quote: "호주산 소고기를 50% 할인하고, 1+등급 한우 제품도 30% 할인하는 행사다."
  - p8 Lotte Mart 'Mat-kangs' promotion discount rate on 1+ grade Hanwoo beef = **30** % (2026-08-08..2026-08-12) [DISCARD: Offline grocery Hanwoo discount rate; irrelevant.] quote: "호주산 소고기를 50% 할인하고, 1+등급 한우 제품도 30% 할인하는 행사다."
  - p9 Starfield new goods count sold at Hachuping movie-themed store = **8** types of goods (2026-08-08..2026-08-30) [DISCARD: Product-type count at an offline store; irrelevant.] quote: "또 신규 굿즈 8종 등 490종의 상품을 판매한다."
  - p10 Starfield total product types sold at Hachuping movie-themed store = **490** types of products (2026-08-08..2026-08-30) [DISCARD: Product-type count at an offline store; irrelevant.] quote: "또 신규 굿즈 8종 등 490종의 상품을 판매한다."
  - p11 Coupang Travel Mega Week Sale number of travel/leisure products offered at speci = **200** products (2026-08-08..2026-08-09) [DISCARD: Count of travel products on promotion; no transaction-value magnitude, cannot anchor the total.] quote: "호텔, 리조트, 펜션, 풀빌라 등 200여개 상품을 특가에 판매한다."
  - p12 SSG.com Shopping Express coupon discount rate range (lower bound) = **8** % (2026-08-08..2026-08-09) [DISCARD: Coupon discount rate only; no level information.] quote: "8∼10% 할인 쿠폰이 지급되며 행사 카드로 결제하면 추가 청구 할인도 받을 수 있다."
  - p13 SSG.com Shopping Express coupon discount rate range (upper bound) = **10** % (2026-08-08..2026-08-09) [DISCARD: Coupon discount rate only; no level information.] quote: "8∼10% 할인 쿠폰이 지급되며 행사 카드로 결제하면 추가 청구 할인도 받을 수 있다."
  - p14 11st summer appliance promotion maximum discount rate = **15** % (2026-08-08..2026-08-09) [DISCARD: Appliance discount rate only; no level information.] quote: "위닉스, 캐리어, 쿠쿠 등 인기 브랜드들이 참여해 다양한 상품을 최대 15% 할인해준다."
- `https://www.fnnews.com/news/202610011202444153` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Industry/market forecasts

Hypothesis: Published e-commerce market forecasts or monthly trackers (e.g., from research firms, ministry reports) provide an independent level or growth rate for 2026 that can anchor the estimate.

Queries issued by the searcher: Korea online shopping market forecast 2026; 국내 온라인쇼핑 시장 규모 전망 2026; 2025년 8월 온라인쇼핑동향 거래액 조 원 통계청; 2026년 6월 온라인쇼핑 동향 거래액 국가데이터처

- `https://fiscal.ai/company/KOSE-A035420/investor-relations/552809/?_x_output_type_b6db407c4_=embedded_pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ytn.co.kr/_ln/0102_202510011350546155` -> **snapshot** (snapshot 20251001062529); points raw/verified 8/0
- `https://www.edaily.co.kr/News/Read?newsId=03043846642370312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.hansbiz.co.kr/news/articleView.html?idxno=841041` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (period year 2026 does not appear in the page text or URL (likely mis-dated): 8)

### b1 [own_history] official series

Hypothesis: The National Data Office Online Shopping Trends monthly transaction-value series (all commodities, total online) through mid-2026 is the single most important missing input; it would enable series_naive/yoy_scaling and give the level, trend and August seasonal factor directly. Without it no credible numeric route exists.

Queries issued by the searcher: 온라인쇼핑동향 거래액 2025년 8월 통계청; KOSIS 온라인쇼핑동향 월별 거래액 총계; 2026년 6월 온라인쇼핑동향 국가데이터처 거래액; "온라인쇼핑동향" 2026년 7월 거래액 조 원

- `https://mods.go.kr/boardDownload.es?bid=241&list_no=444909&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.heraldk.com/article/2025093022032722828` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] retail decomposition

Hypothesis: Monthly total retail sales value combined with the online-shopping share of retail sales would give an independent level estimate (d2); the share is published in the same Online Shopping Trends / retail sales releases.

Queries issued by the searcher: 온라인쇼핑동향 거래액 2025년 소매판매액 비중; 소매판매액 월별 통계 2025 온라인 쇼핑 비중; 2026년 7월 온라인쇼핑동향 거래액 소매판매 비중; 2026년 6월 소매판매액 온라인쇼핑 거래액 비중 국가데이터처

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] payment rails

Hypothesis: Aggregate e-commerce card/electronic payment value (전자상거래 결제액) tracks the target closely and could serve as a cross-check via a coverage adjustment (d4).

Queries issued by the searcher: 전자상거래 결제액 월별 한국은행 지급결제통계; 신용카드 온라인 결제 통계 전자상거래 결제액 2025; 전자상거래 통신판매 신용카드 결제액 2025년 월별 한국은행; 온라인쇼핑 거래액 2026년 7월 통계청 20조

- `https://www.etoday.co.kr/news/view/2570614` -> **snapshot** (snapshot 20260330061609); points raw/verified 15/15
  - p15 Daily average payment card usage amount, South Korea, 2025 (all payment cards, d = **3,596,000,000,000** as written "3조5960억", value check pending KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p16 Daily average payment card usage amount, South Korea, 2024 (all payment cards, d = **3,436,000,000,000** as written "3조4360억", value check pending KRW per day (2024-01-01..2024-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p17 Year-on-year growth rate of payment card usage amount, South Korea, 2025 = **4.7** % (2025-01-01..2025-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p18 Year-on-year growth rate of payment card usage amount, South Korea, 2023 = **6.2** % (2023-01-01..2023-12-31) [keep: ] quote: "2022년 12.7%까지 뛰었던 카드 이용액 증가율은 2023년(6.2%)과 2024년(4.1%) 둔화 흐름을 보이다 지난해 다시 반등했다."
  - p19 Year-on-year growth rate of payment card usage amount, South Korea, 2024 = **4.1** % (2024-01-01..2024-12-31) [keep: ] quote: "2022년 12.7%까지 뛰었던 카드 이용액 증가율은 2023년(6.2%)과 2024년(4.1%) 둔화 흐름을 보이다 지난해 다시 반등했다."
  - p20 Year-on-year growth rate of payment card usage amount, South Korea, 2022 = **12.7** % (2022-01-01..2022-12-31) [keep: ] quote: "2022년 12.7%까지 뛰었던 카드 이용액 증가율은 2023년(6.2%)과 2024년(4.1%) 둔화 흐름을 보이다 지난해 다시 반등했다."
  - p21 Daily average usage amount of credit and other deferred-payment cards, South Kor = **2,860,000,000,000** as written "2조8600억", value check pending KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "지난해 신용카드와 같은 후불형카드의 하루 평균 이용금액은 2조8600억 원으로 1년 새 4.6% 늘었다."
  - p22 Daily average usage amount of debit cards (check cards etc.), South Korea, 2025 = **725,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "체크카드 등 직불형 카드 규모는 7250억 원으로 4.3% 증가했고 소액이긴 하나 선불카드(120억원)도 1년 전과 비교해 77.7% 증가했다."
  - p23 Daily average usage amount of prepaid cards, South Korea, 2025 = **12,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "체크카드 등 직불형 카드 규모는 7250억 원으로 4.3% 증가했고 소액이긴 하나 선불카드(120억원)도 1년 전과 비교해 77.7% 증가했다."
  - p24 Daily average card usage amount, South Korea, 2025 (separate BOK tally of 9 dedi = **3,100,000,000,000** as written "3조1000억", value check pending KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "한은이 전업카드사(9곳)을 대상으로 별도 집계한 지난해 국내 카드 이용 규모 3조1000억 원(일평균, 잠정치) 중 실물카드를 활용한 대면결제 규모는 하루 평균 1조4050억원(45.7%)으로 전년 대비 0.4% 감소했다."
  - p25 Daily average face-to-face (physical card) payment amount, South Korea, 2025 (9  = **1,405,000,000,000** as written "1조4050억", value check pending KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "실물카드를 활용한 대면결제 규모는 하루 평균 1조4050억원(45.7%)으로 전년 대비 0.4% 감소했다."
  - p26 Share of face-to-face (physical card) payments in card usage, South Korea, 2025  = **45.7** % (2025-01-01..2025-12-31) [keep: ] quote: "실물카드를 활용한 대면결제 규모는 하루 평균 1조4050억원(45.7%)으로 전년 대비 0.4% 감소했다."
  - p27 Daily average non-face-to-face (mobile/online, no physical card) payment amount, = **1,668,000,000,000** as written "1조6680억", value check ok KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
  - p28 Share of non-face-to-face (mobile/online, no physical card) payments in card usa = **54.3** % (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
  - p29 Year-on-year growth rate of non-face-to-face (mobile/online) card payment amount = **7.3** % (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
- `https://view.asiae.co.kr/article/2021031708060897058` -> **snapshot** (snapshot 20220426083529); points raw/verified 15/15
  - p30 Annual nationwide e-commerce/telecommunications sales personal credit card payme = **116,325,100,000,000** as written "116조3251억원", value check pending KRW (2020-01-01..2020-12-31) [keep: ] quote: "작년 전국 전자상거래·통신판매 개인 신용카드 결제액은 116조3251억원이었다."
  - p31 Annual e-commerce/telecommunications sales credit card payment value, South Kore = **51,670,000,000,000** as written "51조6천700억원", value check pending KRW (2016-01-01..2016-12-31) [keep: ] quote: "특히 2016년(+25.01%, 51조6천700억원), 2017년(+25.02%, 64조5천959억원)에는 연간 10조원 넘게 급증하기도 했다."
  - p32 Annual e-commerce/telecommunications sales credit card payment value, South Kore = **64,595,900,000,000** as written "64조5천959억원", value check pending KRW (2017-01-01..2017-12-31) [keep: ] quote: "특히 2016년(+25.01%, 51조6천700억원), 2017년(+25.02%, 64조5천959억원)에는 연간 10조원 넘게 급증하기도 했다."
  - p33 Year-on-year growth rate of annual e-commerce/telecommunications credit card pay = **25.01** % (2016-01-01..2016-12-31) [keep: ] quote: "특히 2016년(+25.01%, 51조6천700억원), 2017년(+25.02%, 64조5천959억원)에는 연간 10조원 넘게 급증하기도 했다."
  - p34 Year-on-year growth rate of annual e-commerce/telecommunications credit card pay = **25.02** % (2017-01-01..2017-12-31) [keep: ] quote: "특히 2016년(+25.01%, 51조6천700억원), 2017년(+25.02%, 64조5천959억원)에는 연간 10조원 넘게 급증하기도 했다."
  - p35 Monthly e-commerce/telecommunications credit card payment value, South Korea, Se = **10,294,300,000,000** as written "10조2943억원", value check failed KRW (2020-09-01..2020-09-30) [keep: ] quote: "월별로 봤을 때 지난해 9월(10조2943억원)에 처음으로 월간 기준 10조원을 넘었고, 작년 12월(11조4122억원)에는 11조원을 웃돌았다."
  - p36 Monthly e-commerce/telecommunications credit card payment value, South Korea, De = **11,412,200,000,000** as written "11조4122억원", value check failed KRW (2020-12-01..2020-12-31) [keep: ] quote: "월별로 봤을 때 지난해 9월(10조2943억원)에 처음으로 월간 기준 10조원을 넘었고, 작년 12월(11조4122억원)에는 11조원을 웃돌았다."
  - p37 Annual nationwide duty-free shop personal credit card payment value, South Korea = **555,400,000,000** KRW (2020-01-01..2020-12-31) [DISCARD: Duty-free shop card payments are a tiny, unrelated retail segment; no bearing on total online shopping.] quote: "지난해 연간 전국 면세점 개인 신용카드 결제액은 5554억원으로, 1년 전(2조1947억원)의 4분의 1 토막이 됐다."
  - p38 Annual nationwide duty-free shop personal credit card payment value, South Korea = **2,194,700,000,000** as written "2조1947억원", value check pending KRW (2019-01-01..2019-12-31) [DISCARD: Same duty-free series as p37; irrelevant to the target.] quote: "지난해 연간 전국 면세점 개인 신용카드 결제액은 5554억원으로, 1년 전(2조1947억원)의 4분의 1 토막이 됐다."
  - p39 Year-on-year change in annual nationwide duty-free shop personal credit card pay = **-74.7** % (2020-01-01..2020-12-31) [DISCARD: Duty-free YoY change; irrelevant to online shopping total.] quote: "역대 가장 큰 감소율(-74.7%)이었다."
  - p40 Daily average card usage amount, South Korea, 2020 = **2,521,000,000,000** as written "2조5210억원", value check pending KRW per day (2020-01-01..2020-12-31) [keep: ] quote: "지난해 카드 이용규모는 일평균 2조5210억원으로 전년대비 0.6% 늘었다."
  - p41 Year-on-year growth of daily average card usage amount, South Korea, 2020 = **0.6** % (2020-01-01..2020-12-31) [keep: ] quote: "지난해 카드 이용규모는 일평균 2조5210억원으로 전년대비 0.6% 늘었다."
  - p42 Daily average credit card payment amount, South Korea, 2020 = **1,961,000,000,000** as written "1조9610억원", value check pending KRW per day (2020-01-01..2020-12-31) [DISCARD: Credit-card-only daily average for 2020 is redundant with p40/p15 card totals and adds no distinct route.] quote: "신용카드 결제액은 하루 평균 1조9610억원으로 0.3% 감소전환했다."
  - p43 Share of non-face-to-face payments in total payments, South Korea, Q4 2020 = **39.6** % (2020-10-01..2020-12-31) [DISCARD: Q4 2020 non-face-to-face share is superseded by the 2025 p28 share for the same concept; keeping both risks double-count] quote: "전체 결제 중 비대면 결제 비중은 지속적으로 확대돼 작년 4분기 중 39.6%를 기록해 40%에 육박했다."
  - p44 Share of non-face-to-face payments in total payments, South Korea, Q1 2019 = **32.2** % (2019-01-01..2019-03-31) [DISCARD: Q1 2019 non-face-to-face share is an older duplicate of the same concept as p28; redundant.] quote: "2019년 1분기에만 해도 비대면 결제가 32.2% 수준이었지만 2020년 1분기 36.4%, 지난해 말 39.6%로 빠르게 늘어난 것이다."
- `http://www.financialpost.co.kr/news/articleView.html?idxno=257493` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.enewstoday.co.kr/news/articleView.html?idxno=2408777` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea online shopping', 'korea e-commerce sales', 'online shopping korea']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] All three describe the same Lotte Department Store Nowon food-hall promotion (Aug 4–8, 2026); they are one underlying source, not independent evidence. They are micro-level retail promotions, not onli
- corroborating: ['p4', 'p5'] Same Shinsegae Gangnam popup promotion; one source. Offline department-store promotion, not online transaction value.
- corroborating: ['p7', 'p8'] Same Lotte Mart 'Mat-kangs' beef promotion; one source. Offline grocery discount, not online shopping.
- corroborating: ['p9', 'p10'] Same Starfield Hachuping store description; product-count figures, not transaction values.
- corroborating: ['p12', 'p13'] Same SSG.com coupon range (8–10%); one source. Indicates an online promotion exists but gives no transaction level.
- corroborating: ['p11', 'p14'] Both are online-platform August 2026 promotions (Coupang Travel, 11st appliances); they signal promotional activity but provide no transaction-value magnitude.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p15', 'p16', 'p17', 'p19'] Same source (etoday, citing card-industry/BOK data): p15 and p16 are daily-average card usage levels for 2025 and 2024; p17 (4.7%) and p19 (4.1%) are the corresponding YoY growth rates. p15/p16 imply 
- corroborating: ['p21', 'p22', 'p23', 'p15'] Decomposition of the 2025 daily card total: credit/deferred p21 (2.86tn) + debit p22 (0.725tn) + prepaid p23 (0.012tn) ≈ 3.597tn, matching p15 (3.596tn). Internally consistent; same underlying measure
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29'] BOK separate tally of 9 dedicated card firms: p24 total 3.10tn/day; p25 face-to-face 1.405tn (p26 45.7%); p27 non-face-to-face 1.668tn (p28 54.3%); p29 7.3% growth. p25+p27 ≈ p24 and p26+p28 ≈ 100%. T
- conflicting: ['p15', 'p24'] Two different daily card totals for 2025 (3.596tn vs 3.10tn) because of different populations (all card issuers/merchants vs 9 dedicated card firms, provisional). Not a true contradiction; must not be
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Older (2016-2020) e-commerce/telecom-sales personal credit-card payment series from a 2022 snapshot. Internally consistent growth story (p33/p34 ~25%/yr; p35/p36 monthly milestones). Definition (perso
- corroborating: ['p37', 'p38', 'p39'] Duty-free personal credit-card payments 2019-2020 with -74.7% change; internally consistent but irrelevant to online shopping totals.
- corroborating: ['p40', 'p41', 'p42', 'p43', 'p44'] 2020 card-usage levels and non-face-to-face share trend (32.2% Q1 2019 → 39.6% Q4 2020). Consistent with p27/p28 direction (54.3% by 2025), showing a rising non-face-to-face share over time; useful on

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Online-shopping share of non-face-to-face card payments | 0.75 | 0.55..0.95 | 0.5111..1.022 (widened) | ratio | m1 (m1) | Non-face-to-face card payments (p27) include mobile in-store wallets, subscriptions, utility/bill payments and business purchases that are not 'online shopping' as defined by the Online Shopping Trends release, while some online shopping is settled by account transfer or cash and excluded. Net, onli | Using the 2025 non-face-to-face card payment level (p27) as a base for online shopping transaction value. | Evidence that mobile in-store payments are a large fraction of non-face-to-face card volume, or that online shopping is mostly paid outside cards. |
| a2 | Growth factor from 2025 average to August 2026 for online shopping | 1.07 | 1..1.16 | 0.9633..1.204 (widened) | ratio | m1 (m1) | Online shopping has grown high-single-digit annually in recent years; non-face-to-face card payments grew 7.3% in 2025 (p29) and total card usage 4.7% (p17). Applying roughly 7% for the ~20 months from the 2025 average to August 2026, with uncertainty. | Scaling a 2025-average-based level forward to August 2026. | Published 2026 online-shopping growth far outside 0-16%, or a sharp contraction in e-commerce. |
| a3 | August seasonal index vs annual daily average | 1 | 0.93..1.08 | 0.7087..1.417 (widened) | ratio | m1 (m1) | August has no major gift-giving holiday but includes summer travel/leisure online bookings and vacation effects; online shopping monthly values are fairly flat with mild summer elevation. Centered at 1.0 with modest spread. | Converting an annual daily-average-based level to an August monthly total. | Strong documented August seasonal swing in Online Shopping Trends (e.g., >10% above/below annual average). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 40,379,441,630,573 | ['p27'] / ['a1', 'a2', 'a3'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **40,379,441,630,573** KRW, 80% interval [23,588,813,318,522, 69,121,718,179,718] KRW, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total online shopping transaction value in South Korea for August 2026 (all commodities, aggregate 거래액) is 40,379,441,630,573 KRW (80% model-based interval 23,588,813,318,522 to 69,121,718,179,718 KRW).

The estimate scales the observed daily non-face-to-face card payment level (1,668,000,000,000 KRW per day) to the month, then applies the online-shopping share of such payments (0.75, range 0.5111 to 1.022), a growth factor to 2026 (1.07, range 0.9633 to 1.204), and an August seasonal index (1, range 0.7087 to 1.417). Only the payment level is observed; the share, growth, and seasonality are analyst assumptions, not measured.

A single method (1 method, weight 100%) was used, so no combination evidence exists. The interval is too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only.

The biggest risk is that non-face-to-face card payments are a poor proxy for the release's online-shopping definition, especially the assumed share. Better evidence would be recent actual online-shopping monthly totals and a measured share of card payments within them.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Online-shopping share of non-face-to-face card payments: 0.75 ratio, range 0.5111 to 1.022 (range widened by code); used by m1. Overturned by: Evidence that mobile in-store payments are a large fraction of non-face-to-face card volume, or that online shopping is mostly paid outside cards.
- a2 Growth factor from 2025 average to August 2026 for online shopping: 1.07 ratio, range 0.9633 to 1.204 (range widened by code); used by m1. Overturned by: Published 2026 online-shopping growth far outside [n]-[n], or a sharp contraction in e-commerce.
- a3 August seasonal index vs annual daily average: 1 ratio, range 0.7087 to 1.417 (range widened by code); used by m1. Overturned by: Strong documented August seasonal swing in Online Shopping Trends (e.g., >[n] above/below annual average).

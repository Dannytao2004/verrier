# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Total value of online shopping transactions (거래액) in South Korea during August 2026, as reported in the National Data Office (formerly Statistics Korea) monthly Online Shopping Trends (온라인쇼핑동향) release — the headline 'online shopping transaction value' aggregate covering all online shopping channels | unit KRW (current prices, total for the month) | period 2026-08-01..2026-08-31 | publisher 국가데이터처 (National Data Office, formerly 통계청/Statistics Korea) — Online Shopping Trends (온라인쇼핑동향조사)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] Statistical agency time series

Hypothesis: August 2026 total = most recent published monthly level (e.g., mid-2026) grown by trend monthly growth and adjusted by the historical August seasonal factor (August vs adjacent months). Own history gives both the level anchor and the seasonal shape.

Queries issued by the searcher: 온라인쇼핑동향 거래액 월별 2026; Statistics Korea online shopping trends monthly transaction value 2026; 2025년 8월 온라인쇼핑동향 거래액 전년동월대비; "온라인쇼핑" 거래액 2024년 8월 20조 통계청

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=444356&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Retail sales / consumption aggregate

Hypothesis: Online shopping is a large, slowly drifting share of total retail sales (소매판매액). Target = total retail sales in August 2026 × online share. Retail sales index/level and the online share provide an independent cross-check on the level.

Queries issued by the searcher: 소매판매액지수 2026년 6월 명목 소매판매액; 온라인쇼핑 거래액 소매판매 비중 2025 통계청; 2026년 6월 온라인쇼핑동향 거래액 국가데이터처; 2025년 8월 온라인쇼핑 거래액 24조 소매판매 비중

- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www1.edaily.co.kr/News/Read?newsId=03191446645543712&mediaCodeNo=257` -> **snapshot** (snapshot 20260803080838); points raw/verified 15/14
  - p1 South Korea online shopping transaction value, June 2026 (headline aggregate, al = **24,606,700,000,000** as written "24조6067억원", value check failed KRW (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p2 South Korea online shopping transaction value, H1 2026 (cumulative Jan-Jun) = **145,737,100,000,000** as written "145조7371억원", value check ok KRW (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 온라인쇼핑 거래액은 145조7371억원으로 집계됐다."
  - p3 South Korea online shopping transaction value, Q1 2026 = **72,128,600,000,000** as written "72조1286억원", value check failed KRW (2026-01-01..2026-03-31) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p4 South Korea online shopping transaction value, Q2 2026 = **73,608,500,000,000** as written "73조6085억원", value check failed KRW (2026-04-01..2026-06-30) [keep: ] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p5 South Korea online shopping transaction value, May 2026 (implied prior month, st = **1.7** % (2026-06-01..2026-06-30) [keep: Kept as corroborating context (implies May level) but not used as a direct series input since it is a change, not a leve] quote: "다만 역대 2위 수준이었던 전월과 비교하면 1.7% 감소했다."
  - p6 South Korea online shopping share of total retail sales, Q1 2026 (online product = **29.4** % (2026-01-01..2026-03-31) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p7 South Korea online shopping share of total retail sales, Q2 2026 (online product = **30** % (2026-04-01..2026-06-30) [keep: ] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p8 South Korea online product transaction value (excl. travel and food services), H = **100,308,000,000,000** as written "100조3080억원", value check pending KRW (2026-01-01..2026-06-30) [keep: ] quote: "여행과 음식서비스 등을 제외한 온라인 상품 거래액은 상반기 100조3080억원을 기록하며 100조원을 넘어섰다."
  - p9 South Korea mobile shopping transaction value, June 2026 = **18,927,000,000,000** as written "18조9270억원", value check failed KRW (2026-06-01..2026-06-30) [keep: ] quote: "6월 모바일쇼핑 거래액은 18조9270억원으로 전년 동월보다 9.8% 증가했다."
  - p10 South Korea mobile share of total online shopping transaction value, June 2026 = **76.9** % (2026-06-01..2026-06-30) [keep: ] quote: "전체 온라인쇼핑 거래액에서 모바일이 차지하는 비중은 76.9%로 지난해 같은 달보다 0.7%포인트 낮아졌다."
  - p11 South Korea online shopping transaction value, June 2026 year-on-year increase ( = **2,384,600,000,000** as written "2조3846억원", value check pending KRW (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p12 South Korea online shopping transaction value, June 2026 year-on-year growth rat = **10.7** % (2026-06-01..2026-06-30) [keep: ] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p13 South Korea online shopping transaction value, H1 2026 year-on-year growth rate = **9.6** % (2026-01-01..2026-06-30) [keep: ] quote: "지난해 상반기 132조9541억원보다 9.6% 증가한 규모다."
  - p14 South Korea online shopping transaction value, Q2 2026 year-on-year growth rate = **10.1** % (2026-04-01..2026-06-30) [keep: ] quote: "2분기 거래액은 전년 동기보다 10.1%, 전분기보다 2.1% 늘었다."
- `https://www.womennews.co.kr/news/articleView.html?idxno=273137` -> **snapshot** (snapshot 20260202073346); points raw/verified 15/15
  - p15 South Korea total online shopping transaction value, full year 2025 (annual) = **272,039,800,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "지난해 온라인쇼핑 거래액은 전년 대비 4.9% 증가한 272조398억원으로 집계됐다."
  - p16 South Korea total retail sales value (소매판매액), full year 2025 (denominator of onl = **654,883,300,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p17 Online shopping share of total retail sales, full year 2025 (online transactions = **28.2** % (2025-01-01..2025-12-31) [keep: ] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p18 Year-on-year change in online shopping share of retail sales, 2025 vs 2024 (perc = **0.8** % (2025-01-01..2025-12-31) [keep: ] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p19 Year-on-year growth rate of total online shopping transaction value, full year 2 = **4.9** % (2025-01-01..2025-12-31) [keep: ] quote: "지난해 온라인쇼핑 거래액은 전년 대비 4.9% 증가한 272조398억원으로 집계됐다."
  - p20 Year-on-year growth rate of total online shopping transaction value, full year 2 = **7.1** % (2024-01-01..2024-12-31) [keep: ] quote: "온라인쇼핑 거래 증가율은 2017년부터 2023년까지 두자릿수 증가율을 기록하다 2024년 7.1%, 2025년 4.9%로 떨어졌다."
  - p21 South Korea mobile shopping transaction value, full year 2025 = **211,144,800,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액은 211조 1448억원으로 6.5% 증가했다."
  - p22 South Korea online shopping transaction value, December 2025 (monthly) = **24,290,400,000,000** KRW (2025-12-01..2025-12-31) [keep: ] quote: "작년 12월 온라인쇼핑 거래액은 전년 동월 대비 6.2% 증가한 24조2904억원으로 나타났다."
  - p23 Year-on-year growth rate of online shopping transaction value, December 2025 = **6.2** % (2025-12-01..2025-12-31) [keep: ] quote: "작년 12월 온라인쇼핑 거래액은 전년 동월 대비 6.2% 증가한 24조2904억원으로 나타났다."
  - p24 South Korea mobile shopping transaction value, December 2025 (monthly) = **18,799,100,000,000** KRW (2025-12-01..2025-12-31) [keep: ] quote: "같은 기간 모바일 쇼핑 거래액은 6.2% 증가한 18조7991억원으로 집계됐다."
  - p25 South Korea online shopping transaction value, food & beverages category, full y = **47,356,300,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "작년온라인 거래액 중 품목별로 식품이 47조3563억원으로 가장 많았다."
  - p26 South Korea online shopping transaction value, food services (음식서비스) category, f = **36,989,100,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "음식서비스 36조9891억원 등 음식료품 거래가 84조3454억원을 기록했다."
  - p27 South Korea online shopping transaction value, travel & transportation services  = **32,464,700,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "여행 및 교통서비스(32조4647억원), 컴퓨터, 통신기기 등 가전 판매(30조8537), 의복 (21조9961억원), 생활용품(18조9996억원) 등이 뒤를 이었다."
  - p28 South Korea online shopping transaction value, clothing (의복) category, full year = **21,996,100,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "여행 및 교통서비스(32조4647억원), 컴퓨터, 통신기기 등 가전 판매(30조8537), 의복 (21조9961억원), 생활용품(18조9996억원) 등이 뒤를 이었다."
  - p29 South Korea online shopping transaction value, household goods (생활용품) category,  = **18,999,600,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "여행 및 교통서비스(32조4647억원), 컴퓨터, 통신기기 등 가전 판매(30조8537), 의복 (21조9961억원), 생활용품(18조9996억원) 등이 뒤를 이었다."
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d3 [related_series] Mobile vs internet split

Hypothesis: Total = mobile (모바일) + PC/internet (인터넷) transaction values. Mobile is the dominant and faster-growing component; estimating mobile level and its share, then adding the smaller internet component, gives an alternative decomposition and a consistency check.

Queries issued by the searcher: 모바일쇼핑 거래액 월별 2026 온라인쇼핑동향; 온라인쇼핑 거래액 2026년 6월 모바일 비중 통계청; 국가데이터처 2026년 7월 온라인쇼핑동향 보도자료 mods.go.kr; "PC기반" 인터넷쇼핑 거래액 2026년 7월 5조 모바일 19조5716억

- `https://kociscenter.kr/kor/file/Common_FileDownLoad.do?fileSeq=47812` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=444356&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Category composition

Hypothesis: Total = sum over covered industries (e.g., food & beverages, household goods, fashion, electronics, cosmetics, travel/intermediary services, e-coupons). Summing category-level August 2026 estimates (each grown from its own history) constrains the total and reveals which categories drive August seasonality.

Queries issued by the searcher: 온라인쇼핑동향 상품군별 거래액 2026년 6월; 온라인쇼핑 상품군별 거래액 2025 통계청; mods.go.kr boardDownload 2026년 7월 온라인쇼핑동향 상품군별 온라인쇼핑 거래액 통계표; 2026년 5월 온라인쇼핑동향 상품군별 거래액 여행 및 교통서비스 음식서비스 조원

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bbs2.shinhansec.com/board/message/file.do?attachmentId=341268` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20260901_0003770725` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Macro and calendar effects

Hypothesis: August 2026 level is affected by nominal consumption growth, inflation in goods, consumer sentiment, and calendar (number of weekend days, Chuseok timing — Chuseok 2026 falls in late September, so August is not boosted by it). Quantify trend growth and any known disruption (e.g., heat waves, policy stimulus, platform changes) to adjust the extrapolation.

Queries issued by the searcher: 소비자물가지수 2026년 8월 통계청; 온라인쇼핑동향 2026년 7월 거래액; 소비자심리지수 2026년 8월 한국은행; 2026년 7월 산업활동동향 소매판매 증가율

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/amp/view/AKR20260824149100002` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/cpidtval.es?mid=b70201010000` -> **snapshot** (snapshot 20260701075931); points raw/verified 15/9
  - p30 South Korea consumer price index (total), May 2026, 2020=100 = **120** index (2020=100) (2026-05-01..2026-05-31) [keep: ] quote: "\| 지수 \| 116.27 \| 116.31 \| 116.52 \| 116.45 \| 117.06 \| 117.42 \| 117.20 \| 117.57 \| 118.03 \| 118.40 \| 118.80 \| 119.37 \| 119.92 \|"
  - p31 South Korea consumer price index (total), April 2026, 2020=100 = **119** index (2020=100) (2026-04-01..2026-04-30) [keep: ] quote: "\| 지수 \| 116.27 \| 116.31 \| 116.52 \| 116.45 \| 117.06 \| 117.42 \| 117.20 \| 117.57 \| 118.03 \| 118.40 \| 118.80 \| 119.37 \| 119.92 \|"
  - p32 South Korea consumer price index (total), March 2026, 2020=100 = **119** index (2020=100) (2026-03-01..2026-03-31) [keep: ] quote: "\| 지수 \| 116.27 \| 116.31 \| 116.52 \| 116.45 \| 117.06 \| 117.42 \| 117.20 \| 117.57 \| 118.03 \| 118.40 \| 118.80 \| 119.37 \| 119.92 \|"
  - p33 South Korea CPI (total) month-on-month change, April 2026 = **0.5** percent (2026-04-01..2026-04-30) [keep: ] quote: "\| 전월비 \| -0.1 \| 0.0 \| 0.2 \| -0.1 \| 0.5 \| 0.3 \| -0.2 \| 0.3 \| 0.4 \| 0.3 \| 0.3 \| 0.5 \| 0.5 \|"
  - p34 South Korea CPI (total) month-on-month change, March 2026 = **0.3** percent (2026-03-01..2026-03-31) [keep: ] quote: "\| 전월비 \| -0.1 \| 0.0 \| 0.2 \| -0.1 \| 0.5 \| 0.3 \| -0.2 \| 0.3 \| 0.4 \| 0.3 \| 0.3 \| 0.5 \| 0.5 \|"
  - p35 South Korea CPI (total) year-on-year change, May 2026 = **3.1** % (2026-05-01..2026-05-31) [keep: ] quote: "전년동월대비 3.1% 상승"
  - p36 South Korea CPI (total) year-on-year change, April 2026 = **2.6** percent (2026-04-01..2026-04-30) [keep: ] quote: "\| 전년동월비 \| 1.9 \| 2.2 \| 2.1 \| 1.7 \| 2.1 \| 2.4 \| 2.4 \| 2.3 \| 2.0 \| 2.0 \| 2.2 \| 2.6 \| 3.1 \|"
  - p37 South Korea CPI (total) year-on-year change, March 2026 = **2.2** percent (2026-03-01..2026-03-31) [keep: ] quote: "\| 전년동월비 \| 1.9 \| 2.2 \| 2.1 \| 1.7 \| 2.1 \| 2.4 \| 2.4 \| 2.3 \| 2.0 \| 2.0 \| 2.2 \| 2.6 \| 3.1 \|"
  - p38 South Korea CPI (total) month-on-month change, May 2026 (headline text) = **0.5** % (2026-05-01..2026-05-31) [keep: ] quote: "2026년 05월 소비자물가지수는 전월 대비 0.5% 상승,"
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period year 2025 does not appear in the page text or URL (likely mis-dated): 5; value_as_written not in quote as a whole number: 1)

### d6 [forecasts_markets] Published forecasts and nowcasts

Hypothesis: Analyst or agency forecasts/nowcasts of 2026 online shopping or retail sales growth provide an external anchor for the trend growth rate applied to the last observed level.

Queries issued by the searcher: 2026 온라인쇼핑 시장 전망 성장률; Korea e-commerce market forecast 2026 growth; 2025년 온라인쇼핑 거래액 연간 250조 통계청 온라인쇼핑동향; JPMorgan 국내 온라인쇼핑 거래액 300조원 2026 전망

- `https://www.edaily.co.kr/News/Read?newsId=03043846642370312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.digitaltoday.co.kr/en/view/845/why-founders-are-turning-to-d2c-instead-of-platforms-in-a-300-trillion-won-ecommerce-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6058575` -> **snapshot** (snapshot 20260215164837); points raw/verified 0/0
- `https://m-i.kr/news/articleView.html?idxno=1332504` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [physical_flow] Payment/transaction throughput

Hypothesis: Online transaction value ≈ number of online card/payment transactions × average transaction value, or total card spending × online share. Card/payment network aggregates give an independent magnitude check.

Queries issued by the searcher: 신용카드 온라인 결제액 2025 온라인쇼핑 비중; 온라인쇼핑동향조사 2026년 6월 거래액; 2026년 7월 온라인쇼핑동향 거래액 국가데이터처; 여신금융협회 2026년 2분기 카드 승인 실적 온라인쇼핑

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2570614` -> **snapshot** (snapshot 20260710083501); points raw/verified 15/15
  - p39 Daily average payment card usage amount, South Korea, all payment cards (2025) = **3,596,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p40 Daily average payment card usage amount, South Korea, all payment cards (2024) = **3,436,000,000,000** KRW per day (2024-01-01..2024-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p41 Year-on-year growth rate of payment card usage amount, South Korea (2025) = **4.7** % (2025-01-01..2025-12-31) [keep: ] quote: "지난해 지급카드 이용규모(전업카드사·국내 가맹점 대상)는 하루 평균 3조5960억 원으로 전년(3조4360억원) 대비 4.7% 증가했다."
  - p42 Daily average credit (postpaid) card usage amount, South Korea (2025) = **2,860,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "지난해 신용카드와 같은 후불형카드의 하루 평균 이용금액은 2조8600억 원으로 1년 새 4.6% 늘었다."
  - p43 Credit card share of total payment card usage amount, South Korea (2025) = **80** % (2025-01-01..2025-12-31) [keep: ] quote: "신용카드가 전체 지급카드 이용 규모에서 차지하는 비중은 80%에 육박한다."
  - p44 Daily average debit card usage amount, South Korea (2025) = **725,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "체크카드 등 직불형 카드 규모는 7250억 원으로 4.3% 증가했고"
  - p45 Daily average prepaid card usage amount, South Korea (2025) = **12,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "소액이긴 하나 선불카드(120억원)도 1년 전과 비교해 77.7% 증가했다."
  - p46 Daily average card usage amount, South Korea, card issuers only (2025, provision = **3,100,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: Kept as a scope-narrower card aggregate (issuers only) useful only as a consistency check; not a direct target input.] quote: "지난해 국내 카드 이용 규모 3조1000억 원(일평균, 잠정치) 중 실물카드를 활용한 대면결제 규모는"
  - p47 Daily average face-to-face (physical card) payment amount, South Korea, card iss = **1,405,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: Kept as face-to-face card context; not a direct target input.] quote: "실물카드를 활용한 대면결제 규모는 하루 평균 1조4050억원(45.7%)으로 전년 대비 0.4% 감소했다."
  - p48 Face-to-face (physical card) share of card usage amount, South Korea, card issue = **45.7** % (2025-01-01..2025-12-31) [keep: Kept as share context; not a direct target input.] quote: "실물카드를 활용한 대면결제 규모는 하루 평균 1조4050억원(45.7%)으로 전년 대비 0.4% 감소했다."
  - p49 Daily average non-face-to-face (mobile/online, no physical card) payment amount, = **1,668,000,000,000** KRW per day (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
  - p50 Non-face-to-face (mobile/online, no physical card) share of card usage amount, S = **54.3** % (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
  - p51 Year-on-year growth rate of non-face-to-face card payment amount, South Korea, c = **7.3** % (2025-01-01..2025-12-31) [keep: ] quote: "결제 시 모바일을 활용하거나 온라인을 통해 결제한(실물카드 미제시) 규모는 7.3% 확대된 하루 평균 1조6680억원(54.3%)으로 집계됐다."
  - p52 Fintech simple-payment service share of simple-payment usage, South Korea (2025) = **72.5** % (2025-01-01..2025-12-31) [DISCARD: Fintech vs card-company simple-payment share split is irrelevant to the total online transaction value; no conversion ro] quote: "실제 핀테크 간편결제 서비스 이용비중(23년 67.7→24년 70.3→25년 72.5%)은 매년 우상향 중이다."
  - p53 Card company simple-payment service share of simple-payment usage, South Korea ( = **27.5** % (2025-01-01..2025-12-31) [DISCARD: Complement of p52; same irrelevance to the target level.] quote: "2023년 33%를 웃돌던 카드사 간편결제 서비스 이용 비중은 지난해 기준 27.5%로 해마다 하락하고 있는 것으로 나타났다."
- `http://www.enewstoday.co.kr/news/articleView.html?idxno=2408777` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Statistics Korea / National Data Office monthly release

Hypothesis: The July 2026 online shopping transaction value (published ~early September 2026) would give the most recent level anchor, reducing extrapolation distance from June to August. This is the single most valuable missing input for the own-history route (m1).

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 거래액; 통계청 온라인쇼핑동향 2026년 6월 거래액 모바일

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Seasonal pattern of online shopping

Hypothesis: Historical monthly August-vs-June ratios (2023-2025) would let us convert the June 2026 anchor to an August 2026 level with a proper seasonal factor rather than assuming flat months. This directly reduces the largest uncertainty in m1.

Queries issued by the searcher: 온라인쇼핑동향조사 2025년 8월 온라인쇼핑 거래액; Statistics Korea online shopping trends August 2025 transaction value trillion won; 2025년 6월 온라인쇼핑동향 온라인쇼핑 거래액 조원 전월대비; 2024년 6월 온라인쇼핑동향 거래액 20조 통계청

- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=438838` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=438862&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=437829` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20250801_0003275300` -> **snapshot** (snapshot 20250812112141); points raw/verified 15/15
  - p54 South Korea total online shopping transaction value, June 2025 (monthly) = **21,897,700,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "6월 온라인쇼핑 거래액은 21조8977억원으로 전년 같은달(21조5186억원)보다 1.8%(3790억원) 증가했다."
  - p55 South Korea total online shopping transaction value, June 2024 (monthly) = **21,518,600,000,000** KRW (2024-06-01..2024-06-30) [keep: ] quote: "6월 온라인쇼핑 거래액은 21조8977억원으로 전년 같은달(21조5186억원)보다 1.8%(3790억원) 증가했다."
  - p56 South Korea total online shopping transaction value, Q2 2025 (Apr-Jun cumulative = **66,077,200,000,000** KRW (2025-04-01..2025-06-30) [keep: ] quote: "올해 2분기(4~6월) 전체 온라인쇼핑 거래액은 66조772억원으로 전년 동기 대비 1.7% 증가했다."
  - p57 South Korea total online shopping transaction value, Q2 2024 (Apr-Jun cumulative = **66,000,000,000,000** KRW (2024-04-01..2024-06-30) [keep: ] quote: "올해 2분기 온라인쇼핑 거래액이 66조원을 넘어서면서 역대 최대를 기록했다."
  - p58 South Korea mobile shopping transaction value, June 2025 (monthly) = **17,033,900,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "전체 거래액 중 모바일쇼핑은 17조339억원으로 4.6%(7530억원) 늘었다."
  - p59 Mobile share of total online shopping transaction value, June 2025 = **77.8** % (2025-06-01..2025-06-30) [keep: ] quote: "전체 온라인쇼핑 중 모바일의 비중은 77.8%로, 전년(75.7%)보다 2.1%포인트(p) 늘었다."
  - p60 Mobile share of total online shopping transaction value, June 2024 = **75.7** % (2024-06-01..2024-06-30) [keep: ] quote: "전체 온라인쇼핑 중 모바일의 비중은 77.8%로, 전년(75.7%)보다 2.1%포인트(p) 늘었다."
  - p61 South Korea food services online transaction value, June 2025 (monthly) = **3,422,800,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "상품군별로는 음식서비스가 3조4228억원으로 전년보다 12.9% 증가했다."
  - p62 Food services share of total online shopping, June 2025 = **15.6** % (2025-06-01..2025-06-30) [keep: ] quote: "음식서비스는 전체 온라인쇼핑의 15.6%를 차지한다."
  - p63 South Korea food and beverages online transaction value, June 2025 (monthly) = **3,018,200,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "음·식료품은 11.0% 증가한 3조182억원, 농축수산물은 13.5% 늘어난 1조1097억원으로 집계됐다."
  - p64 South Korea agricultural, livestock and fishery products online transaction valu = **1,109,700,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "음·식료품은 11.0% 증가한 3조182억원, 농축수산물은 13.5% 늘어난 1조1097억원으로 집계됐다."
  - p65 South Korea e-coupon service online transaction value, June 2025 (monthly) = **458,200,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "이쿠폰서비스는 4582억원으로 1년 전보다 52.2% 쪼그라들었다."
  - p66 South Korea travel and transport services online transaction value, June 2025 (m = **2,645,300,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "여행 및 교통서비스는 2조6453억원으로 1.2% 증가에 그쳤고, 문화·레저서비스는 2490억원으로 24.8% 감소했다."
  - p67 South Korea online mall (online-only) transaction value, June 2025 (monthly) = **16,872,300,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "운영형태별로는 온라인몰이 16조8723억원으로 0.6% 증가했다."
  - p68 South Korea online-offline combined mall transaction value, June 2025 (monthly) = **5,025,400,000,000** KRW (2025-06-01..2025-06-30) [keep: ] quote: "온·오프라인 병행몰은 5조254억원으로 5.8% 늘었다."

### b3 [related_series] Retail sales level

Hypothesis: Monthly total retail sales value (소매판매액) for mid-2026 would let us apply the ~30% online share (p7) to get an independent cross-check on the target level (d2 route).

Queries issued by the searcher: 소매판매액 2026년 6월 통계청; 소매판매액지수 2026년 7월 산업활동동향; 2026년 6월 온라인쇼핑동향 거래액 국가데이터처; "소매판매액" 2026년 6월 금액 백만원 산업활동동향 통계표

- `https://mods.go.kr/board.es?act=view&bid=216&list_no=446690&mid=a10301010000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www1.edaily.co.kr/News/Read?newsId=03191446645543712&mediaCodeNo=257` -> **snapshot** (snapshot 20260803080838); points raw/verified 15/14
  - p69 Online shopping transaction value, South Korea, June 2026 (monthly total) = **24,606,700,000,000** as written "24조6067억원", value check failed KRW (2026-06-01..2026-06-30) [DISCARD: Exact duplicate of p1 (same June 2026 headline figure, same source); adds no information.] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p70 Share of online product transactions in total retail sales, Q2 2026 (numerator:  = **30** % (2026-04-01..2026-06-30) [DISCARD: Duplicate of p7 (Q2 2026 30.0% online share).] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p71 Share of online product transactions in total retail sales, Q1 2026 (numerator:  = **29.4** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of p6 (Q1 2026 29.4% online share).] quote: "전체 소매판매액에서 온라인 상품 거래가 차지하는 비중은 1분기 29.4%에서 2분기 30.0%로 높아졌다."
  - p72 Online product transaction value excluding travel and food services, H1 2026 (cu = **100,308,000,000,000** as written "100조3080억원", value check pending KRW (2026-01-01..2026-06-30) [DISCARD: Duplicate of p8 (H1 2026 online product transactions excl. travel/food).] quote: "여행과 음식서비스 등을 제외한 온라인 상품 거래액은 상반기 100조3080억원을 기록하며 100조원을 넘어섰다."
  - p73 Online shopping transaction value, H1 2026 (cumulative) = **145,737,100,000,000** as written "145조7371억원", value check pending KRW (2026-01-01..2026-06-30) [DISCARD: Duplicate of p2 (H1 2026 total).] quote: "올해 상반기 온라인쇼핑 거래액은 145조7371억원으로 집계됐다."
  - p74 Online shopping transaction value, Q1 2026 = **72,128,600,000,000** as written "72조1286억원", value check pending KRW (2026-01-01..2026-03-31) [DISCARD: Duplicate of p3 (Q1 2026 total).] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p75 Online shopping transaction value, Q2 2026 = **73,608,500,000,000** as written "73조6085억원", value check pending KRW (2026-04-01..2026-06-30) [DISCARD: Duplicate of p4 (Q2 2026 total).] quote: "분기별로는 1분기 72조1286억원, 2분기 73조6085억원을 기록했다."
  - p76 Mobile shopping transaction value, June 2026 = **18,927,000,000,000** as written "18조9270억원", value check failed KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p9 (June 2026 mobile).] quote: "6월 모바일쇼핑 거래액은 18조9270억원으로 전년 동월보다 9.8% 증가했다."
  - p77 Mobile share of total online shopping transaction value, June 2026 (numerator: m = **76.9** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p10 (June 2026 mobile share).] quote: "전체 온라인쇼핑 거래액에서 모바일이 차지하는 비중은 76.9%로 지난해 같은 달보다 0.7%포인트 낮아졌다."
  - p78 Online shopping transaction value, June 2026, month-on-month change = **1.7** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p5 (June 2026 -1.7% MoM).] quote: "다만 역대 2위 수준이었던 전월과 비교하면 1.7% 감소했다."
  - p79 Online shopping transaction value, June 2026, year-on-year increase (KRW) = **2,384,600,000,000** as written "2조3846억원", value check pending KRW (2026-06-01..2026-06-30) [DISCARD: Duplicate of p11 (June 2026 YoY increase).] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p80 Online shopping transaction value, June 2026, year-on-year growth rate = **10.7** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p12 (June 2026 YoY growth).] quote: "지난 6월 온라인쇼핑 거래액은 24조6067억원으로, 전년 동월보다 2조3846억원(10.7%) 증가했다."
  - p81 Online shopping transaction value, H1 2026, year-on-year growth rate = **9.6** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of p13 (H1 2026 YoY).] quote: "지난해 상반기 132조9541억원보다 9.6% 증가한 규모다."
  - p82 Online shopping transaction value, Q2 2026, year-on-year growth rate = **10.1** % (2026-04-01..2026-06-30) [DISCARD: Duplicate of p14 (Q2 2026 YoY).] quote: "2분기 거래액은 전년 동기보다 10.1%, 전분기보다 2.1% 늘었다."
- `https://mods.go.kr/board.es?mid=a10301010000&bid=216&act=view&list_no=446305&tag=&nPage=1&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['korea online shopping', 'korea retail sales', 'korea e-commerce']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] All from the same edaily article (snapshot 2026-08-03), same underlying Statistics Korea Online Shopping Trends release. They are internally consistent (Q1+Q2=H1; June is the largest month of Q2). Not
- corroborating: ['p1', 'p5'] p5 states June fell 1.7% vs May, implying May ≈ June/0.983 ≈ 25.03tn; consistent with June being a high month and with Q2 total. Same source.
- corroborating: ['p1', 'p9', 'p10'] Mobile 18.927tn / total 24.607tn = 76.9%, matching p10 exactly. Internally consistent decomposition of the same release.
- corroborating: ['p6', 'p7', 'p8'] Online share of retail rising 29.4%→30.0% Q1→Q2 2026; product-only H1 100.3tn is a subset of the 145.7tn headline (difference = travel/food services/e-coupons). Consistent scope hierarchy.
- corroborating: ['p15', 'p16', 'p17', 'p19', 'p21'] 2025 annual figures from womennews (snapshot 2026-02-02): 272.04tn total, 654.88tn retail, 28.2% share, mobile 211.14tn. 272.04/654.88 = 41.5% — note this is a different share definition (all online i
- conflicting: ['p17', 'p6', 'p7'] Apparent conflict (28.2% for 2025 vs 29.4-30.0% for 2026 quarters) is a definitional difference: p17 uses total online transactions over retail sales; p6/p7 use 'online product transactions' (excludin
- corroborating: ['p22', 'p23', 'p24'] Dec 2025 monthly 24.29tn (+6.2% YoY), mobile 18.80tn (+6.2%). Same release, consistent.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29'] 2025 category breakdown from same womennews article; sums to a plausible fraction of the 272tn total. Useful for category structure but only annual.
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] CPI series from mods.go.kr; the index levels and MoM/YoY changes are mutually consistent (May 2026 YoY 3.1%, MoM 0.5%). Provides inflation context for nominal growth.
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51'] Card usage aggregates from etoday (snapshot 2026-07-10). p39 = p42+p44+p45 approximately; p46 (issuers only) is a narrower scope than p39 (all cards incl. domestic merchants). p47+p49 ≈ p46. Non-face-
- corroborating: ['p52', 'p53'] Simple-payment shares sum to 100%; contextual only, not directly usable for the target level.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p69'] p1 and p69 are the same June 2026 headline figure (24,6067억원) from the same edaily article; identical, not independent.
- corroborating: ['p2', 'p3', 'p4'] H1 2026 = Q1 + Q2 (72.1286 + 73.6085 = 145.7371조) internally consistent; same source, so one measurement.
- corroborating: ['p1', 'p5', 'p11', 'p12'] June 2026 level, its -1.7% MoM vs May, and +2.3846조 (+10.7%) YoY are mutually consistent (24.6067 - 2.3846 = 22.2221조 June 2025 base).
- corroborating: ['p9', 'p10', 'p76', 'p77'] Mobile June 2026 (18.9270조) and 76.9% share are the same figures duplicated across snapshots; 18.9270/24.6067 ≈ 76.9% checks out.
- corroborating: ['p1', 'p54', 'p55'] June 2025 = 21.8977조 (p54) and June 2024 = 21.5186조 (p55); p1's implied June 2025 base (22.2221조) differs modestly, consistent with revisions between vintages.
- corroborating: ['p15', 'p16', 'p17', 'p19'] 2025 annual: 272.0398조 / 654.8833조 = 28.2% share, +4.9% YoY — internally consistent single source.
- corroborating: ['p6', 'p7', 'p70', 'p71'] Q1 29.4% → Q2 30.0% online share of retail; duplicated across snapshots, same source.
- corroborating: ['p8', 'p72'] H1 2026 online product transactions excl. travel/food services = 100.3080조; duplicate.
- corroborating: ['p13', 'p14', 'p81', 'p82'] H1 +9.6%, Q2 +10.1% YoY; consistent with June +10.7% (p12) — acceleration through H1.
- corroborating: ['p39', 'p42', 'p44', 'p45', 'p46', 'p47', 'p49'] Card-network aggregates: 3.596조/day total; credit 2.86 + debit 0.725 + prepaid 0.012 ≈ 3.597조; card-issuer subset 3.10조 with 45.7% face-to-face / 54.3% non-face-to-face. Different scope (all card spen
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29'] 2025 category breakdown sums plausibly toward the 272조 total; useful for category-share context but no monthly August seasonality.
- corroborating: ['p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] CPI path: ~2.2% (Mar) → 2.6% (Apr) → 3.1% (May) YoY, MoM ~0.3-0.5%; indicates nominal deflator drift for mid-2026, relevant to nominal growth but not a direct level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 vs June 2026 online shopping level ratio | 1 | 0.93..1.08 | 0.7087..1.417 (widened) | ratio | m1 (m1) | No August-vs-June seasonal factor is in kept evidence. June 2026 was near-record (p5: May was 2nd-highest ever, June -1.7% MoM), so June is a slightly elevated base; two months of trend growth (~+1.5%/mo, from p13/p14) roughly offsets that. August 2026 has no Chuseok boost (Chuseok falls late Septem | Used to bridge the June 2026 anchor to August 2026 when no August-specific seasonal factor is available. | Historical August-vs-June ratios (2023-2025) showing a systematic deviation from 1.0 beyond the stated band. |
| a2 | August 2026 year-on-year growth rate of online shopping | 9 | 5..13 | 5..13 | % | unused | H1 2026 +9.6% (p13), Q2 +10.1% (p14), June +10.7% (p12) show acceleration from 2025's +4.9% (p19). August 2026 likely continues the ~9-10% nominal pace, tempered by base effects and CPI running ~3% (p35). Centered at 9% with a wide band. | Used to project August 2026 from the June 2025 base implied by the June 2026 level and p12. | Evidence of a sharp deceleration (e.g., July 2026 YoY below 5%) or acceleration above 13%. |
| a3 | August 2026 vs June 2026 ratio for the mobile-shopping component | 1 | 0.92..1.09 | 0.7081..1.416 (widened) | ratio | unused | Same seasonal bridge as a1 but applied to the mobile component, which has a slightly different seasonal profile (mobile skews to food/delivery, which is less August-sensitive than travel). Slightly wider band than a1. | Used to bridge the June 2026 mobile anchor to August 2026. | Historical August-vs-June mobile ratios deviating systematically from 1.0. |
| a4 | Q1 2026 share of H1 2026 online shopping transaction value | 0.495 | 0.48..0.51 | 0.3499..0.6997 (widened) | ratio | m1 (m1) | p3/p4 are removed, so the Q1/Q2 split must be assumed. The removed (unconfirmed) figures implied Q1/H1 = 72.13/145.74 = 0.495; the 2025 pattern (Q2 2025 66.08tn vs H1 2025 132.95tn, p56/p13) gives Q1/H1 = 0.503. Both bracket 0.495-0.503, so 0.495 with a ±1.5pp band is a defensible central value; it  | Used to recover the Q2 2026 total (and hence the June monthly level) from the H1 2026 cumulative p2. | Publication of the actual Q1 2026 total showing a share outside 0.48-0.51. |
| a5 | months per quarter (unit conversion) | 3 | 3..3 | 2.121..4.243 (widened) | months | m1 (m1) | A quarter contains three months; used only to convert the Q2 2026 quarterly total to a monthly average. Not a data claim. | Used in m1 to divide the Q2 2026 total by three. | Nothing; it is a calendar identity. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 23,443,324,428,993 | ['p2'] / ['a1', 'a4', 'a5'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input p69: id p69 unknown or discarded |
| m3 | formula_mc | n/a |  | [] |  | 0.00 |  | input p69: id p69 unknown or discarded |
| m4 | formula_mc | n/a |  | [] |  | 0.00 |  | input p76: id p76 unknown or discarded |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **23,443,324,428,993** KRW, 80% interval [11,973,328,928,897, 45,901,141,073,358] KRW, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total online shopping transaction value (거래액) in South Korea for August 2026, all online shopping channels, is 23,443,324,428,993 KRW (80% model-based interval 11,973,328,928,897 to 45,901,141,073,358 KRW).

Main evidence: the observed H1 2026 cumulative total 145,737,100,000,000 KRW anchors the level. The estimate divides H1 into quarters using the assumed Q1 share 0.495, converts Q2 to a monthly June level via 3 months per quarter, then applies the assumed August-to-June ratio 1. Only 66 observed point was kept; the other methods failed on missing inputs, so the combination rests on one route (100% weight) and is not independent.

Key risks: the August seasonal factor is assumed, not observed, and June was an elevated base. The interval reflects input uncertainty only, conditional on assumptions, not demonstrated accuracy. The most useful missing evidence would be prior-year monthly August/June seasonality and confirmed Q1/Q2 splits.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 vs June 2026 online shopping level ratio: 1 ratio, range 0.7087 to 1.417 (range widened by code); used by m1. Overturned by: Historical August-vs-June ratios (2023-2025) showing a systematic deviation from [n] beyond the stated band.
- a4 Q1 2026 share of H1 2026 online shopping transaction value: 0.495 ratio, range 0.3499 to 0.6997 (range widened by code); used by m1. Overturned by: Publication of the actual Q1 2026 total showing a share outside [n]-[n].
- a5 months per quarter (unit conversion): 3 months, range 2.121 to 4.243 (range widened by code); used by m1. Overturned by: Nothing; it is a calendar identity.

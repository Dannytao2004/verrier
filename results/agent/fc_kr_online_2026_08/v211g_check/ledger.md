# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Total value of online shopping transactions (거래액) in South Korea during August 2026, as reported in the National Data Office (formerly Statistics Korea) monthly Online Shopping Trends (온라인쇼핑동향) release — the headline aggregate transaction value across online shopping channels (online shopping malls, | unit KRW (current prices, total for the month) | period 2026-08-01..2026-08-31 | publisher National Data Office (국가데이터처, formerly Statistics Korea / 통계청) — Online Shopping Trends (온라인쇼핑동향)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] Statistical agency time series

Hypothesis: The target is a continuation of a monthly series; recent published months (through ~June/July 2026) plus prior-year August values and month-over-month/YoY growth give the primary anchor. August 2026 ≈ latest published month × seasonal factor × trend growth.

Queries issued by the searcher: 온라인쇼핑동향 거래액 2026년 6월; 통계청 온라인쇼핑동향 월별 거래액 추이 2025년 8월; 2026년 7월 온라인쇼핑동향 거래액 국가데이터처; 국가데이터처 온라인쇼핑동향 월별 거래액 2024년 8월 21조

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ytn.co.kr/_ln/0102_202510011350546155` -> **snapshot** (snapshot 20251001062529); points raw/verified 8/0
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asiatoday.co.kr/kn/view.php?key=20251103010000860` -> **snapshot** (snapshot 20251115153555); points raw/verified 15/14
  - p1 South Korea total online shopping transaction value, September 2025 (headline ag = **23,795,600,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "지난달 온라인쇼핑 거래액은 23조7956억원으로 전년 동월보다 13.3% 늘었다."
  - p2 South Korea total online shopping transaction value, September 2025, YoY growth  = **13.3** % (2025-09-01..2025-09-30) [keep: ] quote: "지난달 온라인쇼핑 거래액은 23조7956억원으로 전년 동월보다 13.3% 늘었다."
  - p3 South Korea total online shopping transaction value, July 2025 (prior month exce = **23,142,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "월간 거래액이 23조원을 넘어선 것도 지난 7월(23조1427억원)에 이어 두번째다."
  - p4 South Korea mobile shopping transaction value, September 2025 = **18,055,200,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 거래액 중 모바일 쇼핑액은 18조552억원으로 전년대비 11.0%(1조7839억원) 증가했다."
  - p5 South Korea mobile shopping transaction value, September 2025, YoY growth rate = **11** % (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 거래액 중 모바일 쇼핑액은 18조552억원으로 전년대비 11.0%(1조7839억원) 증가했다."
  - p6 South Korea mobile shopping transaction value, September 2025, YoY increase amou = **1,783,900,000,000** KRW (2025-09-01..2025-09-30) [DISCARD: Redundant with p4/p5: the YoY increase amount is derivable from the level and growth rate and adds no independent inform] quote: "온라인쇼핑 거래액 중 모바일 쇼핑액은 18조552억원으로 전년대비 11.0%(1조7839억원) 증가했다."
  - p7 South Korea mobile share of online shopping transaction value, September 2025 = **75.9** % (2025-09-01..2025-09-30) [keep: ] quote: "모바일 거래액 비중은 75.9%로 지난해 같은 달보다 1.6%포인트 하락했다."
  - p8 South Korea comprehensive mall (종합몰) online shopping transaction value, Septembe = **13,099,800,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "종합몰 거래액(13조998억원)과 전문몰 거래액(10조6958억원)이 각각 12.0%, 15.0% 증가했다."
  - p9 South Korea specialized mall (전문몰) online shopping transaction value, September  = **10,695,800,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "종합몰 거래액(13조998억원)과 전문몰 거래액(10조6958억원)이 각각 12.0%, 15.0% 증가했다."
  - p10 South Korea comprehensive mall transaction value, September 2025, YoY growth rat = **12** % (2025-09-01..2025-09-30) [keep: ] quote: "종합몰 거래액(13조998억원)과 전문몰 거래액(10조6958억원)이 각각 12.0%, 15.0% 증가했다."
  - p11 South Korea specialized mall transaction value, September 2025, YoY growth rate = **15** % (2025-09-01..2025-09-30) [keep: ] quote: "종합몰 거래액(13조998억원)과 전문몰 거래액(10조6958억원)이 각각 12.0%, 15.0% 증가했다."
  - p12 South Korea online-only mall (온라인 전용몰) transaction value, September 2025 = **18,285,700,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인 전용몰(18조2857억원·12.3%), 온·오프라인 병행몰(5조5099억원·16.9%) 모두 증가세를 보였다."
  - p13 South Korea online-only mall transaction value, September 2025, YoY growth rate = **12.3** % (2025-09-01..2025-09-30) [keep: ] quote: "온라인 전용몰(18조2857억원·12.3%), 온·오프라인 병행몰(5조5099억원·16.9%) 모두 증가세를 보였다."
  - p14 South Korea online/offline combined mall (온·오프라인 병행몰) transaction value, Septemb = **5,509,900,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인 전용몰(18조2857억원·12.3%), 온·오프라인 병행몰(5조5099억원·16.9%) 모두 증가세를 보였다."
- dropped by code checks: 9 (period year 2026 does not appear in the page text or URL (likely mis-dated): 8; value_as_written not in quote as a whole number: 1)

### d2 [related_series] Retail sales statistics

Hypothesis: Online shopping is a large share of total retail sales; the agency's Retail Sales Index / monthly retail sales value provides a broader total from which online share can be applied. Target ≈ total retail sales value × online share.

Queries issued by the searcher: 소매판매액 온라인쇼핑 비중 2025 통계청; 온라인쇼핑동향 2025년 6월 거래액 소매판매 비중; 2026년 6월 온라인쇼핑동향 소매판매액 비중 국가데이터처; 2026년 5월 소매판매액 온라인쇼핑 거래액 비중; "2025년 8월 온라인쇼핑동향" 거래액 소매판매액 비중

- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsprime.co.kr/news/article/?no=718542&sec_no=76` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.womennews.co.kr/news/articleView.html?idxno=273137` -> **snapshot** (snapshot 20260202073346); points raw/verified 15/15
  - p15 South Korea total retail sales value (소매판매액), full year 2025 = **654,883,300,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p16 Online shopping share of total retail sales (온라인쇼핑 비중), full year 2025 = **28.2** % (2025-01-01..2025-12-31) [keep: ] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p17 Year-on-year change in online shopping share of retail sales, 2025 vs 2024 = **0.8** % (2025-01-01..2025-12-31) [DISCARD: The 0.8pp change in online share is a derived difference already implied by p16 and the prior-year share; redundant.] quote: "전체 소매판매액(654조8833억원)에서 온라인쇼핑 거래가 차지하는 비중은 전년보다 0.8%포인트(p) 상승한 28.2%로 역대 최고치를 나타냈다."
  - p18 South Korea online shopping transaction value (온라인쇼핑 거래액), full year 2025 = **272,039,800,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "지난해 온라인쇼핑 거래액은 전년 대비 4.9% 증가한 272조398억원으로 집계됐다."
  - p19 Year-on-year growth rate of online shopping transaction value, full year 2025 = **4.9** % (2025-01-01..2025-12-31) [keep: ] quote: "지난해 온라인쇼핑 거래액은 전년 대비 4.9% 증가한 272조398억원으로 집계됐다."
  - p20 Year-on-year growth rate of online shopping transaction value, full year 2024 = **7.1** % (2024-01-01..2024-12-31) [keep: ] quote: "온라인쇼핑 거래 증가율은 2017년부터 2023년까지 두자릿수 증가율을 기록하다 2024년 7.1%, 2025년 4.9%로 떨어졌다."
  - p21 South Korea online shopping transaction value, December 2025 = **24,290,400,000,000** KRW (2025-12-01..2025-12-31) [keep: ] quote: "작년 12월 온라인쇼핑 거래액은 전년 동월 대비 6.2% 증가한 24조2904억원으로 나타났다."
  - p22 Year-on-year growth rate of online shopping transaction value, December 2025 = **6.2** % (2025-12-01..2025-12-31) [keep: ] quote: "작년 12월 온라인쇼핑 거래액은 전년 동월 대비 6.2% 증가한 24조2904억원으로 나타났다."
  - p23 South Korea mobile shopping transaction value, December 2025 = **18,799,100,000,000** KRW (2025-12-01..2025-12-31) [keep: ] quote: "같은 기간 모바일 쇼핑 거래액은 6.2% 증가한 18조7991억원으로 집계됐다."
  - p24 South Korea mobile shopping transaction value, full year 2025 = **211,144,800,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액은 211조 1448억원으로 6.5% 증가했다."
  - p25 Year-on-year growth rate of mobile shopping transaction value, full year 2025 = **6.5** % (2025-01-01..2025-12-31) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액은 211조 1448억원으로 6.5% 증가했다."
  - p26 Online shopping transaction value for food (식품), full year 2025 = **47,356,300,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "작년온라인 거래액 중 품목별로 식품이 47조3563억원으로 가장 많았다."
  - p27 Online shopping transaction value for food services (음식서비스), full year 2025 = **36,989,100,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "음식서비스 36조9891억원 등 음식료품 거래가 84조3454억원을 기록했다."
  - p28 Online shopping transaction value for travel and transport services (여행 및 교통서비스) = **32,464,700,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "여행 및 교통서비스(32조4647억원), 컴퓨터, 통신기기 등 가전 판매(30조8537), 의복 (21조9961억원), 생활용품(18조9996억원) 등이 뒤를 이었다."
  - p29 Online shopping transaction value for clothing (의복), full year 2025 = **21,996,100,000,000** KRW (2025-01-01..2025-12-31) [keep: ] quote: "여행 및 교통서비스(32조4647억원), 컴퓨터, 통신기기 등 가전 판매(30조8537), 의복 (21조9961억원), 생활용품(18조9996억원) 등이 뒤를 이었다."
- `https://m2.edaily.co.kr/News/Read?newsId=03867126642230256&mediaCodeNo=257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Mobile vs PC split

Hypothesis: Total online = mobile transactions + PC/other transactions; mobile share is stable and published. If total is hard to get, mobile value / mobile share reconstructs the total.

Queries issued by the searcher: 온라인쇼핑동향 모바일 거래액 비중 2026; Korea online shopping transaction value mobile share 2026 Statistics Korea; 2026년 7월 온라인쇼핑동향 모바일쇼핑 거래액 비중; mods.go.kr 2026년 8월 온라인쇼핑동향

- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?num=286115&pg=&pp=&topic=O` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Commodity-group decomposition

Hypothesis: Total = sum over commodity groups (food/beverage, household goods, fashion, electronics, cosmetics, travel/services, e-coupons, etc.). Summing recent group-level values with trend growth gives the total and cross-checks the headline.

Queries issued by the searcher: 온라인쇼핑동향 상품군별 거래액 2026; 온라인쇼핑 취급상품범위별 거래액 2025 통계청; "2026년 7월 온라인쇼핑동향" 거래액; 2026년 6월 온라인쇼핑동향 거래액 25조 상품군별

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bbs2.shinhansec.com/board/message/file.do?attachmentId=341268` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Calendar and event effects

Hypothesis: August 2026 promotional events (e.g., Korea Sale Festa timing, major platform discount events, summer holiday travel bookings) and Chuseok timing shift the level vs. a naive trend. Identify measurable event effects to adjust the seasonal factor.

Queries issued by the searcher: 코리아세일페스타 2026 일정; 2026 추석 날짜; 2025년 8월 온라인쇼핑동향 거래액 조원 통계청; 2026년 8월 온라인쇼핑 거래액 증가율

- `https://www.yna.co.kr/view/AKR20251001059200002` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://influk.bwell.jp/media/archives/941` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ajunews.com/view/20260722094917670` -> **snapshot** (snapshot 20260730222347); points raw/verified 15/3
  - p30 Liberation Day 2026 date (South Korea) = **15** as written "8월 15일", value check pending day of month (August) (2026-08-15..2026-08-15) [keep: ] quote: "올해 광복절인 8월 15일은 토요일로, 17일 월요일이 대체공휴일로 지정됐다."
  - p31 Liberation Day 2026 substitute holiday date (South Korea) = **17** day of month (August) (2026-08-17..2026-08-17) [keep: ] quote: "올해 광복절인 8월 15일은 토요일로, 17일 월요일이 대체공휴일로 지정됐다."
  - p32 Liberation Day 2026 holiday length (South Korea) = **3** as written "사흘", value check pending days (2026-08-15..2026-08-17) [DISCARD: Holiday length is fully implied by p30/p31 (Sat 15, substitute Mon 17); redundant restatement.] quote: "토요일부터 월요일까지 사흘을 쉴 수 있다."
- `https://bbs2.shinhansec.com/board/message/file.do?attachmentId=341268` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (period_end 2026-12-31 after as_of: 5; period_end 2026-09-27 after as_of: 2; period_end 2026-09-24 after as_of: 1; period_end 2026-09-26 after as_of: 1; period_end 2026-10-05 after as_of: 1; period_end 2026-10-09 after as_of: 1; period_end 2026-12-27 after as_of: 1)

### d6 [forecasts_markets] Industry and agency forecasts

Hypothesis: Published e-commerce market forecasts or agency projections for 2026 give an annual total; monthly August ≈ annual × August seasonal share. Provides an independent level check.

Queries issued by the searcher: 한국 온라인쇼핑 시장 규모 2026 전망; Korea e-commerce market size forecast 2026; 2025년 8월 온라인쇼핑 거래액 통계청; 온라인쇼핑동향 월별 거래액 2026년 6월 증가율

- `https://www.edaily.co.kr/News/Read?newsId=03043846642370312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ytn.co.kr/_ln/0102_202510011350546155` -> **snapshot** (snapshot 20251001062529); points raw/verified 8/0
- `https://www.digitaltoday.co.kr/en/view/845/why-founders-are-turning-to-d2c-instead-of-platforms-in-a-300-trillion-won-ecommerce-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (period year 2026 does not appear in the page text or URL (likely mis-dated): 8)

### d7 [physical_flow] Payment and card transaction data

Hypothesis: Card/electronic payment transaction values for online merchants approximate online shopping value; target ≈ online card payment value × coverage adjustment. Cross-checks the survey-based total.

Queries issued by the searcher: 한국은행 전자지급결제 통계 온라인 카드결제액 월별; 온라인쇼핑동향 거래액 2026년 6월 통계청; 여신금융협회 온라인 가맹점 카드 승인액 전자상거래 월별 통계; 온라인쇼핑 거래액 카드 결제 비중 결제수단 비율 한국은행 보도자료

- `https://www.financialpost.co.kr/news/articleView.html?idxno=277719` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.edaily.co.kr/News/Read?newsId=03676886645519768&mediaCodeNo=257` -> **snapshot** (snapshot 20260801020942); points raw/verified 14/0
- `https://slv.news.einfomax.co.kr/news/articleView.html?idxno=4406663` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (period year 2026 does not appear in the page text or URL (likely mis-dated): 14)

### b1 [own_history] agency monthly series

Hypothesis: Obtain the actual published monthly online shopping transaction values for Jan–Jul 2026 (and the August 2025 value) from the National Data Office / KOSIS Online Shopping Trends. This would replace the Dec-2025-anchored extrapolation with a genuine 2026 trend and a true prior-year August base, sharply reducing the dominant uncertainty in the level and growth factor.

Queries issued by the searcher: KOSIS 온라인쇼핑동향 2026년 6월 거래액; 통계청 온라인쇼핑동향 2025년 8월 거래액; "2026년 7월 온라인쇼핑동향" 국가데이터처 거래액; 2026년 5월 온라인쇼핑동향 거래액 25조 332억; "2026년 4월 온라인쇼핑동향" 거래액 전년동월대비; "온라인쇼핑동향" 2026년 1월 2월 거래액 조 원 국가데이터처 발표

- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6247101` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://vop.co.kr/A00001696062.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] seasonality

Hypothesis: Find the historical August-to-December and August-to-September seasonal ratios of the online shopping series (e.g., Aug 2024 vs Dec 2024, Aug 2025 vs Sep 2025). This supplies the seasonal factor needed to convert the December 2025 anchor into an August 2026 level, which is currently an assumption.

Queries issued by the searcher: 온라인쇼핑동향 2025년 8월 거래액 통계청; online shopping transaction August 2024 Korea monthly KOSIS 거래액; 2025년 9월 온라인쇼핑동향 거래액 국가데이터처; 2025년 12월 온라인쇼핑동향 온라인쇼핑 거래액 조원; "2025년 12월" 온라인쇼핑동향 거래액 국가데이터처

- `http://www.paxnet.co.kr/news/allView?currentPageNo=1&vNewsSetId=4667&articleId=2025100112010600257&isNowNews=1&objId=A2025100112010600257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ytn.co.kr/_ln/0102_202510011350546155` -> **snapshot** (snapshot 20251001062529); points raw/verified 8/0
- `https://www.newscj.com/news/articleView.html?idxno=3324134` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www4.newstomato.com/ReadNews.aspx?no=1150963` -> **snapshot** (snapshot 20260312045129); points raw/verified 15/0
- dropped by code checks: 23 (period year 2026 does not appear in the page text or URL (likely mis-dated): 8; period year 2022 does not appear in the page text or URL (likely mis-dated): 14; period year 2021 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [shocks] event effect

Hypothesis: Quantify the effect of the 2026 Liberation Day 3-day weekend and any August 2026 platform promotion (e.g., summer travel/leisure booking surge) on online transaction value, to adjust the seasonal factor. Without a measured effect the holiday context cannot be used numerically.

Queries issued by the searcher: 2026년 8월 온라인쇼핑 여행 예약 증가; 온라인쇼핑동향 2026년 6월 거래액 통계청; 2026년 7월 온라인쇼핑동향 거래액 국가데이터처 발표; 광복절 연휴 여행 예약 증가 2026년 8월 숙박 예약

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ttlnews.com/news/articleView.html?idxno=3136481` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://uk.advfn.com/stock-market/share-news/Growing-Sportcation-Travel-Trend-Trip-com-Group-R/99214517` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446320&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['korea online shopping', 'korea retail sales', 'korea e-commerce']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] All from the same September 2025 Online Shopping Trends release (single article, single underlying survey). They are internally consistent (p1 ≈ p8+p9 ≈ p12+p14; p4/p1 ≈ p7) but are NOT independent me
- corroborating: ['p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29'] All from one 2025 annual-summary article citing the same agency survey. p18/p15 ≈ p16 confirms the retail-share identity. p21/p22 (Dec 2025) and p23 (Dec mobile) are the most recent monthly levels ava
- corroborating: ['p3', 'p1'] July 2025 (23.14 tn) and September 2025 (23.80 tn) bracket a plausible seasonal path; consistent with the same series.
- corroborating: ['p30', 'p31', 'p32'] Calendar facts about August 2026 (Liberation Day Sat 15th, substitute holiday Mon 17th, 3-day weekend). Contextual only — no quantified transaction effect is supplied, so they cannot be converted into
- corroborating: ['p18', 'p19', 'p20'] Growth deceleration 7.1% (2024) → 4.9% (2025) is the trend basis for projecting 2026 growth; consistent with Dec 2025 YoY of 6.2%.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] Same source (Asiatoday, snapshot 2025-11-15) reporting the same Online Shopping Trends series: p1 is the September 2025 headline level, p2 its YoY growth, p3 the July 2025 level. They are internally c
- corroborating: ['p1', 'p4', 'p7'] p4 (mobile 18.0552 tn) / p1 (total 23.7956 tn) = 75.9%, exactly p7's stated mobile share. This is an arithmetic identity within one release, not independent evidence, but it confirms the mobile/total 
- corroborating: ['p8', 'p9', 'p12', 'p14'] Two alternative partitions of the same September 2025 total: comprehensive+specialized malls (p8+p9 = 23.7956 tn) and online-only+combined malls (p12+p14 = 23.7956 tn). Both sum to p1, confirming inte
- corroborating: ['p15', 'p16', 'p18'] Same source (womennews, 2026-02-02): p18/p15 = 41.5%? No — p16 states 28.2% online share of retail. Note p18 (272.04 tn) / p15 (654.88 tn) = 41.5%, which does NOT equal 28.2%; the 28.2% share is defin
- corroborating: ['p18', 'p19', 'p20', 'p21', 'p22'] Same release: 2025 annual total 272.04 tn (+4.9%), December 2025 24.29 tn (+6.2%), and the growth deceleration narrative (7.1% in 2024, 4.9% in 2025). Consistent internally; single source.
- corroborating: ['p21', 'p23'] December 2025 total 24.2904 tn and mobile 18.7991 tn imply mobile share 77.4%, consistent with the ~76% September 2025 share (p7). Same release.
- corroborating: ['p26', 'p27', 'p28', 'p29'] Commodity-group annual 2025 values from the same release; they are components of the 272.04 tn total (food 47.36 + food services 36.99 + travel/transport 32.46 + electronics 30.85 + clothing 22.00 + h
- corroborating: ['p30', 'p31'] Calendar facts for August 2026: Liberation Day Saturday 15 Aug with substitute holiday Monday 17 Aug, giving a 3-day weekend. Relevant to a possible August demand bump but no measured transaction effe
- conflicting: ['p1', 'p21'] Not a true conflict: September 2025 (23.80 tn) vs December 2025 (24.29 tn) differ by season and by ~3 months of trend. They establish that December is a seasonal peak and August is typically below it,

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August-to-December seasonal ratio of online shopping value | 0.93 | 0.85..1.02 | 0.6584..1.317 (widened) | ratio | m1 (m1) | December is the seasonal peak (year-end/holiday shopping); August is a normal-to-soft summer month. Historical Korean online-shopping monthly patterns put August roughly 5-10% below December. Range spans a flat-to-strong-December case. | Used to convert a December-anchored level to an August level for the same series definition. | Published monthly data showing August 2025 at or above December 2025, or an August/December ratio outside 0.85-1.02. |
| a2 | YoY growth factor for online shopping, Aug 2026 vs Aug 2025 | 1.05 | 1..1.11 | 0.9423..1.178 (widened) | ratio | m1 (m1), m2 (m3) | Annual growth decelerated from 7.1% (2024) to 4.9% (2025); December 2025 ran +6.2% and September 2025 +13.3% (a high base effect month). A ~5% YoY factor for mid-2026 is consistent with the decelerating trend, with a range from flat to ~11%. | Applied to a 2025 base (August or September 2025) to project August 2026. | Published 2026 monthly YoY growth outside 0-11%, or a clear re-acceleration/contraction in online shopping. |
| a3 | August-to-average-month seasonal ratio of online shopping value | 0.97 | 0.9..1.04 | 0.6841..1.368 (widened) | ratio | m2 (m3) | August is a slightly below-average month for online shopping (no major gifting holiday; Chuseok falls in autumn). Applied to the 2025 annual monthly average to place August 2026. | Used to convert an annual-average monthly level to an August level. | Monthly data showing August consistently above the annual monthly average by more than 4%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 23,781,515,418,678 | ['p21'] / ['a1', 'a2'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 23,024,447,692,969 | ['p18'] / ['a2', 'a3'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **23,399,920,038,686** KRW, 80% interval [15,548,354,590,014, 35,216,347,469,241] KRW, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total online shopping transaction value (거래액) in South Korea for August 2026, as would be reported in the National Data Office's Online Shopping Trends release, is 23,399,920,038,686 KRW (80% model-based interval 15,548,354,590,014 to 35,216,347,469,241 KRW).

Two routes were averaged: m1 anchors on the observed December 2025 level (24,290,400,000,000 KRW) and applies an August-to-December seasonal ratio (0.93) plus one year of growth (1.05), giving 23,781,515,418,678 KRW at weight 50%. m2 divides the observed 2025 annual total (272,039,800,000,000 KRW) into a monthly average, applies an August seasonal ratio (0.97) and the same growth factor, giving 23,024,447,692,969 KRW at weight 50%.

Only the two anchor points are observed; the seasonal ratios and growth factor are analyst assumptions, so the interval reflects input uncertainty, not demonstrated accuracy. The main risk is a structural break in 2026 online shopping. Timelier 2026 monthly data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August-to-December seasonal ratio of online shopping value: 0.93 ratio, range 0.6584 to 1.317 (range widened by code); used by m1. Overturned by: Published monthly data showing August 2025 at or above December 2025, or an August/December ratio outside [n]-[n].
- a2 YoY growth factor for online shopping, Aug 2026 vs Aug 2025: 1.05 ratio, range 0.9423 to 1.178 (range widened by code); used by m1, m2. Overturned by: Published 2026 monthly YoY growth outside [n]-[n], or a clear re-acceleration/contraction in online shopping.
- a3 August-to-average-month seasonal ratio of online shopping value: 0.97 ratio, range 0.6841 to 1.368 (range widened by code); used by m2. Overturned by: Monthly data showing August consistently above the annual monthly average by more than [n].

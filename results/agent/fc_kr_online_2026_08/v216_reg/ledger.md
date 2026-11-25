# Evidence ledger: fc_kr_online_2026_08

- Question: Assume today is 2026-09-01. You know nothing published after this date. Estimate the total value of online shopping transactions in South Korea in August 2026, in Korean won (KRW), as it will be first reported in the national statistics agency's monthly Online Shopping Trends release (온라인쇼핑동향, National Data Office, formerly Statistics Korea).
- as_of: 2026-09-01
- Pinned target: Total value (in KRW) of online shopping transactions in South Korea during August 2026, as reported in the National Data Office (formerly Statistics Korea) monthly Online Shopping Trends (온라인쇼핑동향) release — i.e., the aggregate 'online shopping transaction value' (온라인쇼핑 거래액) covering online/mobile re | unit KRW | period 2026-08-01..2026-08-31 | publisher National Data Office (국가데이터처, formerly Statistics Korea) — Online Shopping Trends (온라인쇼핑동향)

- Official value (scoring only, never shown to the agent): 24,211,800,000,000

## Directions and pages

### d1 [own_history] National statistics publisher time series

Hypothesis: August 2026 total online shopping transaction value ≈ recent monthly level (e.g., mid-2026 months) adjusted for August seasonal factor and YoY growth trend. Own history gives level, seasonality (August vs July), and growth rate.

Queries issued by the searcher: 온라인쇼핑동향 거래액 2026년 7월; Statistics Korea online shopping trends monthly transaction value 2025 2026; 2025년 8월 온라인쇼핑동향 거래액 조원 전년동월대비; 2024년 8월 온라인쇼핑 거래액 통계청 온라인쇼핑동향; 온라인쇼핑동향 거래액 2026년 7월; Statistics Korea online shopping trends monthly transaction value 2025 2026; 2025년 8월 온라인쇼핑동향 거래액 조원 전년동월대비; "온라인쇼핑" 거래액 2024년 8월 통계청 20조; 온라인쇼핑동향 거래액 2026년 7월; 통계청 온라인쇼핑동향 월별 거래액 2025 2026; 2025년 8월 온라인쇼핑동향 거래액 통계청; 2024년 8월 온라인쇼핑 거래액 전년동월대비 통계청 온라인쇼핑동향

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://macrodatahub.com/data/south-korea-retail-sales-online-shopping-2714` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=11722&list_no=444356&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?depth1=D0000&num=271836` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://overtherainbow.korea.kr/archive/expDocView.do?docId=41385` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://biz.newdaily.co.kr/site/data/html/2026/05/04/2026050400159.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a20101000000&bid=11722&tag=&act=view&list_no=443836&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://slv.news.einfomax.co.kr/news/articleView.html?idxno=4377195` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kif.re.kr/kif2/publication/maildetview.aspx?nodeid=402&controlno=364737&ismail=1&email=%5B%24email%24%5D&SL=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Retail sales / consumption aggregates

Hypothesis: Online shopping transaction value is a share of total retail sales (소매판매액) plus services; using the retail sales index or 소매판매액 total times the online penetration share gives an independent level estimate. Direction: online share has been rising, so apply a trended share.

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 온라인쇼핑 거래액; 소매판매액 2026년 7월 통계청; 2025년 8월 온라인쇼핑동향 온라인쇼핑 거래액 조원; 2025년 8월 소매판매액 조원 온라인쇼핑 상품 거래액 비중; 소매판매액 2026년 7월 온라인쇼핑 거래액; 온라인쇼핑동향 2026년 6월 거래액 조달청 통계청; 2026년 7월 산업활동동향 소매판매액 지수 전년동월비; 2026년 8월 신용카드 승인실적 온라인 결제 증가; 온라인쇼핑동향 2026년 7월 거래액; 소매판매액 2026년 6월 통계청; 2025년 8월 온라인쇼핑동향 거래액 조원; 2026년 7월 소매판매액 56조 1852억 온라인쇼핑 비중 30.3%

- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mt.co.kr/economy/2025/10/01/2025100110540095667` -> **snapshot** (snapshot 20251004015023); points raw/verified 15/15
  - p1 South Korea online shopping transaction value, August 2025 (total) = **22,480,200,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p2 South Korea online shopping transaction value, year-on-year increase, August 202 = **1,392,700,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p3 South Korea online shopping transaction value, year-on-year growth rate, August  = **6.6** % (2025-08-01..2025-08-31) [keep: ] quote: "8월 온라인쇼핑 거래액이 1년 전보다 6.6% 늘었다."
  - p4 South Korea online shopping transaction value, year-on-year growth rate, July 20 = **7.8** % (2025-07-01..2025-07-31) [keep: ] quote: "증가율은 7월(7.8%)보다는 다소 둔화했지만"
  - p5 South Korea online shopping transaction value, year-on-year growth rate, January = **1.6** % (2025-01-01..2025-01-31) [keep: ] quote: "올해 온라인쇼핑 거래액 증가율은 △1월 1.6%"
  - p6 South Korea online shopping transaction value, year-on-year growth rate, Februar = **3.7** % (2025-02-01..2025-02-28) [keep: ] quote: "△2월 3.7%"
  - p7 South Korea online shopping transaction value, year-on-year growth rate, March 2 = **2.5** % (2025-03-01..2025-03-31) [keep: ] quote: "△3월 2.5%"
  - p8 South Korea online shopping transaction value, year-on-year growth rate, April 2 = **2.8** % (2025-04-01..2025-04-30) [keep: ] quote: "△4월 2.8%"
  - p9 South Korea online shopping transaction value, year-on-year growth rate, May 202 = **0.6** % (2025-05-01..2025-05-31) [keep: ] quote: "△5월 0.6%"
  - p10 South Korea online shopping transaction value, year-on-year growth rate, June 20 = **2.2** % (2025-06-01..2025-06-30) [keep: ] quote: "△6월 2.2%"
  - p11 South Korea mobile shopping transaction value, August 2025 = **17,848,900,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p12 Mobile share of total online shopping transaction value, August 2025 = **79.4** % (2025-08-01..2025-08-31) [keep: ] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p13 South Korea food services (음식서비스) online transaction value, August 2025 = **3,736,600,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "상품군별로는 음식서비스(3조7366억원)가 전년 동월 대비 9.0% 늘며 거래액 1위를 차지했다."
  - p14 South Korea food and beverages (음·식료품) online transaction value, August 2025 = **3,205,100,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품(3조2051억원, +5.8%), 농축수산물(+8.7%)도 증가세가 이어졌다."
  - p15 South Korea comprehensive malls (종합몰) online transaction value, August 2025 = **11,950,000,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "취급 상품 범위별로는 종합몰이 11조9500억원으로 4.1% 증가했고, 전문몰은 10조5302억원으로 9.6% 늘었다."
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8651451` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/5931568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1275407.html` -> **snapshot** (snapshot 20260831003917); points raw/verified 15/0
- `https://news.sbs.co.kr/news/endPage.do?news_id=N1008729447` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period year 2026 does not appear in the page text or URL (likely mis-dated): 14; number: value_as_written is only part of a larger CJK number in the quote: 1)

### d3 [related_series] Component decomposition by commodity group

Hypothesis: Total = sum over commodity groups (food, household goods, apparel, electronics, cosmetics, services, travel, etc.) of group transaction values; summing latest group levels with August seasonality gives the total and reveals which groups drive August.

Queries issued by the searcher: 온라인쇼핑동향 상품군별 거래액 2026년 6월; Statistics Korea online shopping trends 2026 commodity group transaction value; 2025년 8월 온라인쇼핑동향 거래액 상품군별; 온라인쇼핑 거래액 2025년 8월 26조 상품군별 음식서비스 여행 및 교통서비스; 온라인쇼핑동향 상품군별 거래액 2026년 7월; 온라인쇼핑동향 2026년 6월 거래액 상품군별; 2025년 8월 온라인쇼핑동향 상품군별 거래액 국가데이터처; "온라인쇼핑동향" 2026년 7월 상품군별 거래액 표 음식서비스 3조8945 여행 및 교통서비스 의복; 온라인쇼핑동향 상품군별 거래액 2026년 7월; 온라인쇼핑동향 2026년 6월 거래액 상품군별; 2025년 8월 온라인쇼핑동향 거래액 상품군별; 온라인쇼핑동향 상품군별 온라인쇼핑 거래액 통계표 2026년 7월 korea.kr

- `https://www.news1.kr/economy/trend/5931568` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=446320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&act=view&list_no=438838` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www5.ajunews.com/view/20251001094913913` -> **snapshot** (snapshot 20251001044516); points raw/verified 15/15
  - p16 Total online shopping transaction value, South Korea, August 2025 = **22,480,200,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1 (same August 2025 total).] quote: "지난 8월 온라인쇼핑 거래액은 22조4802억원으로 전년 동월 대비 1조3927억원(6.6%) 증가했다."
  - p17 Total online shopping transaction value YoY increase, South Korea, August 2025 = **1,392,700,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2.] quote: "지난 8월 온라인쇼핑 거래액은 22조4802억원으로 전년 동월 대비 1조3927억원(6.6%) 증가했다."
  - p18 Total online shopping transaction value YoY growth rate, South Korea, August 202 = **6.6** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3.] quote: "올해 8월 온라인 쇼핑 거래액이 1년 전보다 6.6% 증가했다."
  - p19 Automobiles and automobile parts online shopping transaction value, South Korea, = **782,100,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "자동차 및 자동차용품 거래액이 7821억원으로 전년 동월 대비 2779억원(55.1%) 증가했다."
  - p20 Automobiles and automobile parts online shopping transaction value YoY increase, = **277,900,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "자동차 및 자동차용품 거래액이 7821억원으로 전년 동월 대비 2779억원(55.1%) 증가했다."
  - p21 Automobiles and automobile parts online shopping transaction value YoY growth ra = **55.1** % (2025-08-01..2025-08-31) [keep: ] quote: "자동차 및 자동차용품 거래액이 7821억원으로 전년 동월 대비 2779억원(55.1%) 증가했다."
  - p22 Telecommunication devices online shopping transaction value, South Korea, August = **543,300,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "통신기기 거래액은 5433억원으로 전년 동월 대비 1078억원(24.8%) 증가했다."
  - p23 Telecommunication devices online shopping transaction value YoY increase, South  = **107,800,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "통신기기 거래액은 5433억원으로 전년 동월 대비 1078억원(24.8%) 증가했다."
  - p24 Telecommunication devices online shopping transaction value YoY growth rate, Sou = **24.8** % (2025-08-01..2025-08-31) [keep: ] quote: "통신기기 거래액은 5433억원으로 전년 동월 대비 1078억원(24.8%) 증가했다."
  - p25 Food and beverages online shopping transaction value, South Korea, August 2025 = **3,205,100,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
  - p26 Food and beverages online shopping transaction value YoY increase, South Korea,  = **176,300,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
  - p27 Food and beverages online shopping transaction value YoY growth rate, South Kore = **5.8** % (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
  - p28 Food services online shopping transaction value, South Korea, August 2025 = **3,736,600,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
  - p29 Food services online shopping transaction value YoY increase, South Korea, Augus = **307,000,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
  - p30 Food services online shopping transaction value YoY growth rate, South Korea, Au = **9** % (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품과 음식 서비스 거래액은 각각 3조2051억원과 3조7366억원으로 전년 동월 대비 1763억원(5.8%), 3070억원(9.0%) 증가했다."
- `https://www.mt.co.kr/economy/2025/10/01/2025100110540095667` -> **snapshot** (snapshot 20251004015023); points raw/verified 15/15
  - p31 Total online shopping transaction value, South Korea, August 2025 = **22,480,200,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1.] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p32 Year-on-year increase in total online shopping transaction value, South Korea, A = **1,392,700,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2.] quote: "8월 온라인쇼핑 거래액은 전년 동월보다 1조3927억원(6.6%) 증가한 22조4802억원으로 집계됐다."
  - p33 Year-on-year growth rate of total online shopping transaction value, South Korea = **6.6** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3.] quote: "8월 온라인쇼핑 거래액이 1년 전보다 6.6% 늘었다."
  - p34 Food services (음식서비스) online shopping transaction value, South Korea, August 202 = **3,736,600,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p13/p28.] quote: "상품군별로는 음식서비스(3조7366억원)가 전년 동월 대비 9.0% 늘며 거래액 1위를 차지했다."
  - p35 Year-on-year growth rate of food services online shopping transaction value, Sou = **9** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p30.] quote: "상품군별로는 음식서비스(3조7366억원)가 전년 동월 대비 9.0% 늘며 거래액 1위를 차지했다."
  - p36 Food and beverages (음·식료품) online shopping transaction value, South Korea, Augus = **3,205,100,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p14/p25.] quote: "음·식료품(3조2051억원, +5.8%), 농축수산물(+8.7%)도 증가세가 이어졌다."
  - p37 Year-on-year growth rate of food and beverages online shopping transaction value = **5.8** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p27.] quote: "음·식료품(3조2051억원, +5.8%), 농축수산물(+8.7%)도 증가세가 이어졌다."
  - p38 Year-on-year growth rate of agricultural, livestock and fishery products online  = **8.7** % (2025-08-01..2025-08-31) [keep: ] quote: "음·식료품(3조2051억원, +5.8%), 농축수산물(+8.7%)도 증가세가 이어졌다."
  - p39 Automobiles and automobile supplies online shopping transaction value, South Kor = **782,100,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p19.] quote: "특히 자동차 및 자동차용품 거래액은 7821억원으로 55.1% 급증했다."
  - p40 Year-on-year growth rate of automobiles and automobile supplies online shopping  = **55.1** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p21.] quote: "특히 자동차 및 자동차용품 거래액은 7821억원으로 55.1% 급증했다."
  - p41 Year-on-year growth rate of bags online shopping transaction value, South Korea, = **-7** % (2025-08-01..2025-08-31) [keep: ] quote: "반면 가방(-7.0%) 등 일부 패션 품목은 부진했다."
  - p42 Mobile shopping transaction value, South Korea, August 2025 = **17,848,900,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p43 Mobile share of total online shopping transaction value, South Korea, August 202 = **79.4** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p12.] quote: "모바일쇼핑 거래액은 17조8489억원으로 전년 동월보다 8.9% 증가해 전체 온라인 거래의 79.4%를 차지했다."
  - p44 E-coupon service (이쿠폰서비스) online shopping transaction value, South Korea, August = **476,000,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "이쿠폰서비스 거래액은 전년 동월 대비 8.6% 늘어난 4760억원을 기록했지만 전월 대비로는 7.1% 감소했다."
  - p45 Comprehensive mall (종합몰) online shopping transaction value, South Korea, August  = **11,950,000,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p15.] quote: "취급 상품 범위별로는 종합몰이 11조9500억원으로 4.1% 증가했고, 전문몰은 10조5302억원으로 9.6% 늘었다."
- `http://overtherainbow.korea.kr/archive/expDocView.do?docId=41385` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsprime.co.kr/news/article/?no=745935` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fntimes.com/html/view.php?ud=2026090115232667459bdb80fab5_18` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?depth1=D0000&num=271836` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.infomaxai.com/news/articleView.html?idxno=137497` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Mobile vs PC and domestic vs overseas split

Hypothesis: Total = mobile + PC (or domestic + overseas); mobile share is high and stable, so a mobile transaction value estimate times 1/mobile-share gives the total. Overseas direct purchase/sale components add a small increment.

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 거래액 모바일; 온라인쇼핑 거래액 2026년 6월 통계청 모바일 비중; 2025년 8월 온라인쇼핑동향 거래액 모바일 비중 통계청; 2026년 5월 온라인쇼핑동향 거래액 모바일; 온라인쇼핑동향 모바일 거래액 2026년 6월; 온라인쇼핑 거래액 2026년 5월 통계청; 2026년 2분기 온라인 해외 직접 판매 및 구매 동향 해외직구 거래액; 2025년 8월 온라인쇼핑동향 온라인쇼핑 거래액 모바일 비중; 온라인쇼핑동향 모바일 거래액 2026년 6월; 온라인쇼핑 거래액 모바일 비중 2025 통계청; 2025년 8월 온라인쇼핑동향 거래액 모바일 비중; 2026년 5월 온라인쇼핑동향 거래액 25조 모바일

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&tag=&act=view&list_no=438838&ref_bid=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198519390&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6247101` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?Mcode=4100&pageIndex=349&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://overtherainbow.korea.kr/archive/expDocView.do?docId=41385` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://go.seoul.co.kr/news/prnewsView.php?id=440439` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fntimes.com/html/view.php?ud=2026090115232667459bdb80fab5_18` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ajunews.com/view/20260901111640655` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fnnews.com/news/202609011106044113` -> **snapshot** (snapshot 20260901035653); points raw/verified 15/15
  - p46 Total online shopping transaction value, South Korea, July 2026 = **25,095,400,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "지난 7월 온라인쇼핑 거래액은 25조954억원으로 전년 동월 대비 7.3% 증가했다."
  - p47 Total online shopping transaction value, South Korea, March 2026 (prior record) = **25,543,400,000,000** KRW (2026-03-01..2026-03-31) [keep: ] quote: "거래액 기준으로는 2017년 시계열 개편 이후 지난 3월(25조5434억원)에 이어 역대 두번째 규모다."
  - p48 Mobile shopping transaction value, South Korea, July 2026 = **19,571,600,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "모바일 쇼핑 거래액은 19조5716억원으로 전년 동월 대비 6.4% 증가했다."
  - p49 Mobile share of online shopping transaction value, South Korea, July 2026 = **78** % (2026-07-01..2026-07-31) [keep: ] quote: "온라인 쇼핑 거래액 중 모바일 쇼핑 거래액 비중은 78.0%로 전년 동월 대비 0.6%p 감소했다."
  - p50 Year-on-year change in mobile share of online shopping, South Korea, July 2026 v = **0.6** % (2026-07-01..2026-07-31) [keep: ] quote: "온라인 쇼핑 거래액 중 모바일 쇼핑 거래액 비중은 78.0%로 전년 동월 대비 0.6%p 감소했다."
  - p51 Year-on-year growth of total online shopping transaction value, South Korea, Jul = **7.3** % (2026-07-01..2026-07-31) [keep: ] quote: "지난 7월 온라인쇼핑 거래액은 25조954억원으로 전년 동월 대비 7.3% 증가했다."
  - p52 Year-on-year growth of mobile shopping transaction value, South Korea, July 2026 = **6.4** % (2026-07-01..2026-07-31) [keep: ] quote: "모바일 쇼핑 거래액은 19조5716억원으로 전년 동월 대비 6.4% 증가했다."
  - p53 Food services transaction value, South Korea, July 2026 = **3,894,500,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "음식서비스 거래액이 3조8945억원을 기록하며 전체의 15.5%를 차지했다."
  - p54 Food services share of total online shopping transaction value, South Korea, Jul = **15.5** % (2026-07-01..2026-07-31) [keep: ] quote: "음식서비스 거래액이 3조8945억원을 기록하며 전체의 15.5%를 차지했다."
  - p55 Food and beverages transaction value, South Korea, July 2026 = **3,500,800,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "이어 음식료품이 3조5008억원(13.9%), 여행 및 교통서비스가 3조1695억원(12.6%)을 기록하며 뒤를 이었다."
  - p56 Travel and transport services transaction value, South Korea, July 2026 = **3,169,500,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "이어 음식료품이 3조5008억원(13.9%), 여행 및 교통서비스가 3조1695억원(12.6%)을 기록하며 뒤를 이었다."
  - p57 Comprehensive mall (종합몰) online shopping transaction value, South Korea, July 20 = **13,542,800,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "온라인쇼핑 취급상품범위별 거래액은 종합몰이 13조5428억원을 기록하며 전년 동월 대비 6.8% 증가했다."
  - p58 Specialized mall (전문몰) online shopping transaction value, South Korea, July 2026 = **11,552,700,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "전문몰은 7.9% 증가한 11조5527억원을 기록했다."
  - p59 Mobile share of food services transaction value, South Korea, July 2026 = **99.1** % (2026-07-01..2026-07-31) [keep: ] quote: "상품군별 모바일 비중은 음식서비스가 99.1%로 가장 높았다."
  - p60 Telecommunication devices transaction value, South Korea, July 2026 = **741,400,000,000** KRW (2026-07-01..2026-07-31) [keep: ] quote: "상품군 별로 보면 통신기기 거래액이 7414억원을 기록하며 전년 동월 대비 37.5% 급증했다."

### d5 [forecasts_markets] Industry and analyst forecasts

Hypothesis: Published forecasts of Korea e-commerce/online retail market size for 2026 (annual) can be divided by 12 and adjusted for August share to cross-check the monthly total. Direction: forecasts give an annual anchor.

Queries issued by the searcher: Korea e-commerce market size 2026 forecast KRW; 국내 온라인쇼핑 시장 규모 2026 전망; online retail Korea 2026 forecast billion won; 대한상공회의소 2026년 온라인쇼핑 시장 290조 6.4%; 2026년 온라인쇼핑 거래액 280.7조 전망; 통계청 2025년 8월 온라인쇼핑 거래액 조원; 2026년 6월 온라인쇼핑 거래액 통계청; Korea e-commerce market size 2026 forecast KRW; 국내 온라인쇼핑 시장 규모 2026 전망; 2026년 7월 온라인쇼핑동향 온라인쇼핑 거래액 통계청; 한국온라인쇼핑협회 2026년 온라인쇼핑 시장 규모 전망; Korea e-commerce market size 2026 forecast KRW; 국내 온라인쇼핑 시장 규모 2026 전망; 2026년 7월 온라인쇼핑동향 거래액 통계청; 2025년 8월 온라인쇼핑 거래액 21조 통계청

- `https://www.edaily.co.kr/News/Read?newsId=03043846642370312` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kbv.kr/markets/korea-e-commerce-market-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fiscal.ai/company/KOSE-A035420/investor-relations/552809/?_x_output_type_b6db407c4_=embedded_pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kci.go.kr/kciportal/mobile/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003171409` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hankyung.com/koreamarket/consensus/pdf/2025-11-234c01c39c71baa6cb54b59031e14720` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.marqvision.com/es/blog/2026-ecommerce-market-share-fmcg-trends-korea` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.retailing.co.kr/article/a_view.php?art_idx=5653` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kita.net/board/totalTradeNews/totalTradeNewsDetail.do?no=82491&siteId=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.m-i.kr/news/articleView.html?idxno=1209196` -> **snapshot** (snapshot 20250219085327); points raw/verified 15/9
  - p61 JP Morgan forecast of Korea e-commerce market size in 2026 = **300,000,000,000,000** KRW (2026-01-01..2026-12-31) [keep: ] quote: "한국 이커머스 시장 규모는 오는 2026년 300조원까지 불어날 것으로 전망된다."
  - p62 Annual online shopping transaction value growth rate, 2022 = **11** % (2022-01-01..2022-12-31) [keep: ] quote: "연간 온라인 쇼핑 거래액 증가율 자체는 2022년 11%, 2023년 8.4% 등으로 하락세를 보이고 있지만"
  - p63 Annual online shopping transaction value growth rate, 2023 = **8.4** % (2023-01-01..2023-12-31) [keep: ] quote: "연간 온라인 쇼핑 거래액 증가율 자체는 2022년 11%, 2023년 8.4% 등으로 하락세를 보이고 있지만"
  - p64 Coupang planned investment through 2026 for logistics centers and hiring = **3,000,000,000,000** KRW (2026-01-01..2026-12-31) [DISCARD: Coupang capex/hiring plan; not a transaction-value input.] quote: "오는 2026년까지 3조원을 쏟아부어 부산·광주·대전·경북 지역 등에 9개 물류센터를 확충하고 1만명(청년 포함)을 직고용할 계획이다."
  - p65 Coupang planned new logistics centers by 2026 = **9** logistics center (2026-01-01..2026-12-31) [DISCARD: Coupang logistics-center count; irrelevant to monthly transaction value.] quote: "오는 2026년까지 3조원을 쏟아부어 부산·광주·대전·경북 지역 등에 9개 물류센터를 확충하고 1만명(청년 포함)을 직고용할 계획이다."
  - p66 Coupang planned direct hires by 2026 = **10,000** person (2026-01-01..2026-12-31) [DISCARD: Coupang hiring plan; irrelevant.] quote: "9개 물류센터를 확충하고 1만명(청년 포함)을 직고용할 계획이다."
  - p67 Coupang acquisition price of Farfetch = **650,000,000,000** KRW (2023-01-01..2023-12-31) [DISCARD: Farfetch acquisition price; irrelevant to Korean online shopping flow.] quote: "2023년말 영국의 최대 명품 플랫폼 '파페치'를 6500억원에 인수하기도 했다."
  - p68 Coupang app monthly users, last month (Wise App·Retail) = **33,020,000** person (not stated (page dated 2025-02-19)) [DISCARD: App MAU; no bridge to transaction value.] quote: "쿠팡 3302만여명, 알리 912만여명, 테무 823만여명, 11번가 780만여명, G마켓 542만여명, GS샵 345만여명, 옥션 247만여명, CJ온스타일 239만여명 등이다."
  - p69 Ali app monthly users, last month (Wise App·Retail) = **9,120,000** person (not stated (page dated 2025-02-19)) [DISCARD: App MAU; no bridge to transaction value.] quote: "쿠팡 3302만여명, 알리 912만여명, 테무 823만여명, 11번가 780만여명, G마켓 542만여명, GS샵 345만여명, 옥션 247만여명, CJ온스타일 239만여명 등이다."
- `https://www.retailing.co.kr/article/a_view.php?art_idx=5653?sword=%B7%CE%BA%BF&page=5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.theguru.co.kr/news/article_print.html?no=97988` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period year 2024 does not appear in the page text or URL (likely mis-dated): 6)

### d6 [physical_flow] Payment and transaction infrastructure

Hypothesis: Total transaction value ≈ number of online card/e-payment transactions × average transaction value; card/payment network aggregates (e.g., BC, Shinhan, Bank of Korea payment statistics) provide an independent flow measure that can be scaled to the survey coverage.

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 온라인쇼핑 거래액; 지급결제동향 2026 온라인 카드 결제액; 2025년 8월 온라인쇼핑동향 온라인쇼핑 거래액 24조; 한국은행 2025년 하반기중 국내 지급결제동향 실물카드 미제시 결제 일평균; 지급결제동향 온라인 카드 결제 2026; 온라인쇼핑동향 2026년 6월 거래액; 2026년 7월 온라인쇼핑동향 국가데이터처 거래액; 한국은행 2026년 1분기중 국내 지급결제동향 카드 이용액; 지급결제동향 온라인 카드 결제 2026; 온라인쇼핑동향 2026년 7월 거래액; 한국은행 2026년 1분기 국내 지급결제동향 일평균 카드 이용액; 온라인쇼핑 거래액 2026년 8월 전망 추정

- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.einfomax.co.kr/news/articleView.html?idxno=4432866` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://overtherainbow.korea.kr/archive/expDocView.do?docId=41853` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8651451` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.joseilbo.com/news/htmls/2026/09/20260929576499.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1279938.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ajunews.com/view/20260929105151146` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120100&bid=241&act=view&list_no=438838&tag=&nPage=1&ref_bid=240,241` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20251001059200002?input=1195m` -> **snapshot** (snapshot 20251019081913); points raw/verified 15/15
  - p70 Total online (PC+mobile) shopping transaction value, South Korea, August 2025 (r = **22,480,200,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1.] quote: "지난 8월 온라인(PC+모바일)으로 물건을 구매한 총액은 22조4천802억원으로 1년 전보다 6.6%(1조3천927억원) 증가했다."
  - p71 Year-on-year increase in total online shopping transaction value, South Korea, A = **6.6** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3.] quote: "지난 8월 온라인(PC+모바일)으로 물건을 구매한 총액은 22조4천802억원으로 1년 전보다 6.6%(1조3천927억원) 증가했다."
  - p72 Year-on-year increase amount in total online shopping transaction value, South K = **1,392,700,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2.] quote: "지난 8월 온라인(PC+모바일)으로 물건을 구매한 총액은 22조4천802억원으로 1년 전보다 6.6%(1조3천927억원) 증가했다."
  - p73 Mobile shopping transaction value, South Korea, August 2025 (record high for Aug = **17,848,900,000,000** KRW (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11.] quote: "온라인 쇼핑액 중 모바일 쇼핑액은 17조8천489억원으로 1년 전보다 8.9%(1조4천617억원) 증가했다."
  - p74 Year-on-year increase in mobile shopping transaction value, South Korea, August  = **8.9** % (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 중 모바일 쇼핑액은 17조8천489억원으로 1년 전보다 8.9%(1조4천617억원) 증가했다."
  - p75 Year-on-year increase amount in mobile shopping transaction value, South Korea,  = **1,461,700,000,000** KRW (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 중 모바일 쇼핑액은 17조8천489억원으로 1년 전보다 8.9%(1조4천617억원) 증가했다."
  - p76 Mobile share of online shopping transaction value, South Korea, August 2025 = **79.4** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p12.] quote: "온라인 쇼핑액 중 모바일 거래액 비중은 79.4%로, 작년 같은 달보다 1.7%포인트(p) 증가했다."
  - p77 Year-on-year change in mobile share of online shopping transaction value, South  = **1.7** % (2025-08-01..2025-08-31) [keep: ] quote: "온라인 쇼핑액 중 모바일 거래액 비중은 79.4%로, 작년 같은 달보다 1.7%포인트(p) 증가했다."
  - p78 Share of food services in online shopping transaction value, South Korea, August = **16.6** % (2025-08-01..2025-08-31) [keep: ] quote: "쇼핑 거래액 구성비를 보면 음식 서비스(16.6%), 음·식료품(14.3%), 여행 및 교통서비스(13.1%) 순으로 높았다."
  - p79 Share of food and beverages in online shopping transaction value, South Korea, A = **14.3** % (2025-08-01..2025-08-31) [keep: ] quote: "쇼핑 거래액 구성비를 보면 음식 서비스(16.6%), 음·식료품(14.3%), 여행 및 교통서비스(13.1%) 순으로 높았다."
  - p80 Share of travel and transport services in online shopping transaction value, Sou = **13.1** % (2025-08-01..2025-08-31) [keep: ] quote: "쇼핑 거래액 구성비를 보면 음식 서비스(16.6%), 음·식료품(14.3%), 여행 및 교통서비스(13.1%) 순으로 높았다."
  - p81 Year-on-year growth of online transaction value for cars and car accessories, So = **55.1** % (2025-08-01..2025-08-31) [keep: ] quote: "가장 두드러진 증가세를 보인 상품군은 자동차 및 자동차용품(55.1%)이었다."
  - p82 Year-on-year growth of online transaction value for food services, South Korea,  = **9** % (2025-08-01..2025-08-31) [keep: ] quote: "음식서비스(9.0%), 음·식료품(5.8%) 등도 배달 플랫폼 경쟁 심화와 온라인 장보기 확산의 영향으로 거래액 증가세를 이어갔다."
  - p83 Year-on-year growth of online transaction value for food and beverages, South Ko = **5.8** % (2025-08-01..2025-08-31) [keep: ] quote: "음식서비스(9.0%), 음·식료품(5.8%) 등도 배달 플랫폼 경쟁 심화와 온라인 장보기 확산의 영향으로 거래액 증가세를 이어갔다."
  - p84 Year-on-year growth of e-coupon service transaction value, South Korea, August 2 = **8.6** % (2025-08-01..2025-08-31) [keep: ] quote: "작년 7월 '티몬·위메프 미정산 사태' 이후 감소세를 이어오던 이(e)쿠폰 서비스는 기저효과가 해소되면서 8.6% 증가해 14개월 만에 반등했다."

### d7 [shocks] Calendar and event effects

Hypothesis: August 2026 has no major Korean gift-giving holiday, but summer vacation/travel, heat waves, and any major platform promotions or regulatory changes (e.g., e-commerce platform fee/payment rules, Coupang/Naver events) shift the level. Quantify deviation from trend.

Queries issued by the searcher: 온라인쇼핑동향 2026년 7월 온라인쇼핑 거래액; 통계청 온라인쇼핑동향 2026년 6월 거래액; 2026년 8월 폭염 온라인쇼핑 매출 증가; 2025년 8월 온라인쇼핑 거래액 통계청 전년동월대비; 온라인쇼핑동향 2026년 6월 거래액; 국가데이터처 온라인쇼핑동향 2026년 7월 온라인쇼핑 거래액; 2025년 8월 온라인쇼핑동향 거래액 전년동월대비; 2026년 8월 폭염 온라인쇼핑 매출 증가; 2026년 8월 온라인쇼핑동향 거래액; 온라인쇼핑 거래액 2026년 6월 통계청; 2025년 8월 온라인쇼핑동향 거래액 22조 전년동월대비; 2026년 7월 온라인쇼핑동향 발표 9월

- `https://www.yna.co.kr/view/AKR20260901057900002?input=1195m` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dealsite.co.kr/articles/168236/068000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20251001_0003352021` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=446725&mid=a10301120300&nPage=1&ref_bid=&tag=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6275716` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4823564?Mcode=10300&pageIndex=253&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsappapi.kbs.co.kr/news/pc/view/view.do?ncd=8626893` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sedaily.com/article/20075271` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.khan.co.kr/article/202608261424001` -> **snapshot** (snapshot 20260827085107); points raw/verified 15/15
  - p85 Online retail sales growth, South Korea, month-on-month comparison with same mon = **8.5** % (2026-07-01..2026-07-31) [keep: ] quote: "지난달 오프라인 매출은 전년 동월보다 3.2%, 온라인 매출은 8.5% 늘어 전체 매출이 6.4% 증가했다."
  - p86 Total retail sales growth (offline + online), South Korea, July 2026 vs same mon = **6.4** % (2026-07-01..2026-07-31) [keep: ] quote: "지난달 오프라인 매출은 전년 동월보다 3.2%, 온라인 매출은 8.5% 늘어 전체 매출이 6.4% 증가했다."
  - p87 Offline retail sales growth, South Korea, July 2026 vs same month previous year = **3.2** % (2026-07-01..2026-07-31) [keep: ] quote: "지난달 오프라인 매출은 전년 동월보다 3.2%, 온라인 매출은 8.5% 늘어 전체 매출이 6.4% 증가했다."
  - p88 Online services & other category sales growth (delivery, travel, culture), South = **17.5** % (2026-07-01..2026-07-31) [keep: ] quote: "온라인에서는 배달 서비스와 여행·문화상품 등이 포함된 서비스·기타 부문 매출이 17.5% 증가했다."
  - p89 Online food category sales growth, South Korea, July 2026 vs same month previous = **10.4** % (2026-07-01..2026-07-31) [keep: ] quote: "식품(10.4%)과 가전(11.4%) 부문도 두 자릿수 증가율을 기록했다."
  - p90 Online home appliance category sales growth, South Korea, July 2026 vs same mont = **11.4** % (2026-07-01..2026-07-31) [keep: ] quote: "식품(10.4%)과 가전(11.4%) 부문도 두 자릿수 증가율을 기록했다."
  - p91 Online share of total retail sales by business type, South Korea, July 2026 = **60.8** % (2026-07-01..2026-07-31) [keep: ] quote: "유통업체의 업태별 매출 비중은 온라인이 60.8%로 가장 높았고, 편의점(15.0%), 백화점(14.1%), 대형마트(8.1%), 준대규모점포(2.1%) 순이었다."
  - p92 Convenience store share of total retail sales, South Korea, July 2026 = **15** % (2026-07-01..2026-07-31) [keep: ] quote: "유통업체의 업태별 매출 비중은 온라인이 60.8%로 가장 높았고, 편의점(15.0%), 백화점(14.1%), 대형마트(8.1%), 준대규모점포(2.1%) 순이었다."
  - p93 Department store share of total retail sales, South Korea, July 2026 = **14.1** % (2026-07-01..2026-07-31) [keep: ] quote: "유통업체의 업태별 매출 비중은 온라인이 60.8%로 가장 높았고, 편의점(15.0%), 백화점(14.1%), 대형마트(8.1%), 준대규모점포(2.1%) 순이었다."
  - p94 Hypermarket (large discount store) share of total retail sales, South Korea, Jul = **8.1** % (2026-07-01..2026-07-31) [keep: ] quote: "유통업체의 업태별 매출 비중은 온라인이 60.8%로 가장 높았고, 편의점(15.0%), 백화점(14.1%), 대형마트(8.1%), 준대규모점포(2.1%) 순이었다."
  - p95 SSM (super supermarket) share of total retail sales, South Korea, July 2026 = **2.1** % (2026-07-01..2026-07-31) [keep: ] quote: "유통업체의 업태별 매출 비중은 온라인이 60.8%로 가장 높았고, 편의점(15.0%), 백화점(14.1%), 대형마트(8.1%), 준대규모점포(2.1%) 순이었다."
  - p96 Department store sales growth, South Korea, July 2026 vs same month previous yea = **17.9** % (2026-07-01..2026-07-31) [keep: ] quote: "오프라인에서는 백화점(17.9%)과 편의점(1.1%) 매출이 증가한 반면 대형마트(-11.2%)와 준대규모점포(-2.9%)는 감소했다."
  - p97 Hypermarket (large discount store) sales growth, South Korea, July 2026 vs same  = **-11.2** % (2026-07-01..2026-07-31) [keep: ] quote: "오프라인에서는 백화점(17.9%)과 편의점(1.1%) 매출이 증가한 반면 대형마트(-11.2%)와 준대규모점포(-2.9%)는 감소했다."
  - p98 Hypermarket food category sales decline, June 2026 vs same month previous year = **10.6** % (2026-06-01..2026-06-30) [keep: ] quote: "다만 주력 상품군인 식품의 매출 감소폭은 지난 6월 10.6%에서 지난달 2.5%로 다소 줄었다."
  - p99 Hypermarket food category sales decline, July 2026 vs same month previous year = **2.5** % (2026-07-01..2026-07-31) [keep: ] quote: "다만 주력 상품군인 식품의 매출 감소폭은 지난 6월 10.6%에서 지난달 2.5%로 다소 줄었다."
- `https://www.newsway.co.kr/news/view?ud=2026073113563890799` -> **snapshot** (snapshot 20260801005639); points raw/verified 13/12
  - p100 Lotte Home Shopping seasonal appliance order volume growth, year-on-year (last m = **30** % (not stated (page dated 2026-08-01)) [keep: ] quote: "롯데홈쇼핑 지난달 계절가전 주문량이 전년 동기 대비 30% 올랐다."
  - p101 Lotte Home Shopping fan and air cooler order growth, year-on-year (last month) = **60** % (not stated (page dated 2026-08-01)) [keep: ] quote: "이 중 선풍기와 냉풍기 주문은 60% 증가해 가장 높은 증가율을 보였다."
  - p102 Lotte Home Shopping portable handheld fan order volume, multiple of prior year ( = **4** 1 (multiple of prior-year level) (not stated (page dated 2026-08-01)) [keep: ] quote: "휴대용 핸디 선풍기 주문량은 전년 대비 4배 수준으로 확대됐다."
  - p103 Morancano premium wireless handheld fan sets sold in one hour of broadcast (21st = **1,200** set (not stated (page dated 2026-08-01)) [DISCARD: Single-broadcast unit sales; no usable level.] quote: "특히 지난달 21일 방송한 '모란카노 프리미엄 무선 핸디 선풍기'는 방송 한 시간만에 1200세트가 판매됐다."
  - p104 Lotte Home Shopping stand air conditioner order growth, year-on-year (last month = **40** % (not stated (page dated 2026-08-01)) [keep: ] quote: "스탠드형 에어컨 주문은 40% 증가했으며 제습기 주문도 30% 늘었다."
  - p105 Lotte Home Shopping dehumidifier order growth, year-on-year (last month) = **30** % (not stated (page dated 2026-08-01)) [keep: ] quote: "스탠드형 에어컨 주문은 40% 증가했으며 제습기 주문도 30% 늘었다."
  - p106 Hyundai Home Shopping seasonal appliance revenue growth, year-on-year (last mont = **20** % (not stated (page dated 2026-08-01)) [keep: ] quote: "지난달 계절가전 매출은 지난해 동기 대비 20% 증가했다."
  - p107 SSG.com wall-mounted fan revenue growth, year-on-year (same period) = **75** % (not stated (page dated 2026-08-01)) [keep: ] quote: "동기간 벽걸이 선풍기 매출은 75% 늘었으며 일반형과 소형 선풍기 매출도 각각 13%, 10% 올랐다."
  - p108 SSG.com standard fan revenue growth, year-on-year (same period) = **13** % (not stated (page dated 2026-08-01)) [keep: ] quote: "동기간 벽걸이 선풍기 매출은 75% 늘었으며 일반형과 소형 선풍기 매출도 각각 13%, 10% 올랐다."
  - p109 SSG.com small fan revenue growth, year-on-year (same period) = **10** % (not stated (page dated 2026-08-01)) [keep: ] quote: "동기간 벽걸이 선풍기 매출은 75% 늘었으며 일반형과 소형 선풍기 매출도 각각 13%, 10% 올랐다."
  - p110 11st dehumidifier buyer count growth, year-on-year (1st to 26th of last month) = **154** % (not stated (page dated 2026-08-01)) [keep: ] quote: "지난달 1일부터 26일까지 제습기 구매 고객은 전년 동기 대비 154%, 거래액은 157% 증가했다."
  - p111 11st dehumidifier transaction value growth, year-on-year (1st to 26th of last mo = **157** % (not stated (page dated 2026-08-01)) [keep: ] quote: "지난달 1일부터 26일까지 제습기 구매 고객은 전년 동기 대비 154%, 거래액은 157% 증가했다."
- `https://www.ulsanilbo.co.kr/news/articleView.html?idxno=117169` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.etoday.co.kr/news/view/2614626?trc=right_categori_news` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### b1 [own_history] Complete the monthly total series for 2025-09 through 2026-06

Hypothesis: The series_auto route needs a continuous monthly total from mid-2025 to July 2026 to fit trend/seasonality and to compute the August-vs-July seasonal factor. Currently only August 2025 and July 2026 totals are pinned; filling the intervening months (Sep 2025–Jun 2026) would let a proper seasonal-plus-trend forecast replace the crude YoY-scaling route and materially tighten the estimate.

Queries issued by the searcher: Statistics Korea 온라인쇼핑동향 월별 거래액 2025년 9월 온라인쇼핑 거래액; kostat.go.kr 온라인쇼핑동향 2026년 1월 거래액 발표; "2025년 10월 온라인쇼핑동향" 온라인쇼핑 거래액 전년동월대비; "2025년 11월 온라인쇼핑동향" 온라인쇼핑 거래액 24조; Statistics Korea online shopping trends monthly transaction value 2026년 6월 온라인쇼핑 거래액; 온라인쇼핑동향 2026년 5월 온라인쇼핑 거래액 조사 결과; 2026년 4월 온라인쇼핑동향 거래액 국가데이터처; 2026년 3월 온라인쇼핑동향 온라인쇼핑 거래액 25조 5434억; Statistics Korea online shopping trends monthly transaction value 2025 September October November December; 온라인쇼핑동향 2025년 12월 온라인쇼핑 거래액 통계청; "2026년 1월 온라인쇼핑동향" 온라인쇼핑 거래액; "2026년 3월 온라인쇼핑동향" 거래액 국가데이터처

- `https://www.korea.kr/common/download.do?fileId=198377506&tblKey=GMN` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41587` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=439110&act=view&mainXml=Y` -> **snapshot** (snapshot 20251117035224); points raw/verified 15/14
  - p112 South Korea total online shopping transaction value, September 2025 = **23,795,600,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "2025년 9월 온라인쇼핑 거래액은 23조 7,956억원으로 전년동월대비 13.3% 증가했으며"
  - p113 South Korea mobile shopping transaction value, September 2025 = **18,055,200,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 중 모바일쇼핑 거래액은 18조 552억원으로 11.0% 증가"
  - p114 South Korea total online shopping transaction value, month-on-month change, Sept = **6.5** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 온라인쇼핑 거래액은 6.5%, 모바일쇼핑 거래액은 1.7% 각각 증가"
  - p115 South Korea mobile shopping transaction value, month-on-month change, September  = **1.7** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 온라인쇼핑 거래액은 6.5%, 모바일쇼핑 거래액은 1.7% 각각 증가"
  - p116 South Korea total online shopping transaction value, year-on-year change, Septem = **13.3** % (2025-09-01..2025-09-30) [keep: ] quote: "2025년 9월 온라인쇼핑 거래액은 23조 7,956억원으로 전년동월대비 13.3% 증가했으며"
  - p117 Mobile shopping share of total online shopping transaction value, September 2025 = **75.9** % (2025-09-01..2025-09-30) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액 비중은 75.9%로 전년동월(77.5%)에 비해 1.6%p 감소"
  - p118 South Korea online shopping transaction value, comprehensive malls (종합몰), Septem = **13,099,800,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "종합몰은 12.0% 증가한 13조 998억원을, 전문몰은 15.0% 증가한 10조 6,958억원을 기록"
  - p119 South Korea online shopping transaction value, specialized malls (전문몰), Septembe = **10,695,800,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "종합몰은 12.0% 증가한 13조 998억원을, 전문몰은 15.0% 증가한 10조 6,958억원을 기록"
  - p120 South Korea online shopping transaction value, online malls (온라인몰), September 20 = **18,285,700,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인몰은 12.3% 증가한 18조 2,857억원을, 온·오프라인병행몰은 16.9% 증가한 5조 5,099억원을 기록"
  - p121 South Korea online shopping transaction value, online/offline combined malls (온· = **5,509,900,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "온라인몰은 12.3% 증가한 18조 2,857억원을, 온·오프라인병행몰은 16.9% 증가한 5조 5,099억원을 기록"
  - p122 South Korea online shopping transaction value, comprehensive malls (종합몰), month- = **9.6** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 종합몰은 9.6%, 전문몰은 2.9% 각각 증가"
  - p123 South Korea online shopping transaction value, specialized malls (전문몰), month-on = **2.9** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 종합몰은 9.6%, 전문몰은 2.9% 각각 증가"
  - p124 South Korea online shopping transaction value, online malls (온라인몰), month-on-mon = **5.1** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 온라인몰은 5.1%, 온·오프라인병행몰은 11.4% 각각 증가"
  - p125 South Korea online shopping transaction value, online/offline combined malls (온· = **11.4** % (2025-09-01..2025-09-30) [keep: ] quote: "전월대비 온라인몰은 5.1%, 온·오프라인병행몰은 11.4% 각각 증가"
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=439502&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4668394` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=443817&mid=a10301010000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2562236` -> **snapshot** (snapshot 20260412223138); points raw/verified 15/0
- `https://news.einfomax.co.kr/news/articleView.html?idxno=4417758` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mt.co.kr/economy/2025/12/01/2025120111291837410` -> **snapshot** (snapshot 20260317151945); points raw/verified 15/15
  - p126 South Korea total online shopping transaction value, October 2025 = **22,710,300,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "10월 온라인쇼핑 거래액은 전년 동월 대비 1조519억원(4.9%) 증가한 22조7103억원으로 집계됐다."
  - p127 South Korea total online shopping transaction value, year-on-year increase, Octo = **1,051,900,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "10월 온라인쇼핑 거래액은 전년 동월 대비 1조519억원(4.9%) 증가한 22조7103억원으로 집계됐다."
  - p128 South Korea total online shopping transaction value, year-on-year growth rate, O = **4.9** % (2025-10-01..2025-10-31) [keep: ] quote: "10월 온라인쇼핑 거래액이 1년 전보다 4.9% 늘었다."
  - p129 South Korea total online shopping transaction value, year-on-year growth rate, S = **12.9** % (2025-09-01..2025-09-30) [keep: ] quote: "전체 증가율은 9월(12.9%)보다 둔화했다."
  - p130 South Korea total online shopping transaction value, year-on-year growth rate, J = **1.6** % (2025-01-01..2025-01-31) [keep: ] quote: "△1월 1.6%"
  - p131 South Korea total online shopping transaction value, year-on-year growth rate, F = **3.7** % (2025-02-01..2025-02-28) [keep: ] quote: "△2월 3.7%"
  - p132 South Korea total online shopping transaction value, year-on-year growth rate, M = **2.5** % (2025-03-01..2025-03-31) [keep: ] quote: "△3월 2.5%"
  - p133 South Korea total online shopping transaction value, year-on-year growth rate, A = **2.8** % (2025-04-01..2025-04-30) [keep: ] quote: "△4월 2.8%"
  - p134 South Korea total online shopping transaction value, year-on-year growth rate, M = **0.6** % (2025-05-01..2025-05-31) [keep: ] quote: "△5월 0.6%"
  - p135 South Korea total online shopping transaction value, year-on-year growth rate, J = **2.2** % (2025-06-01..2025-06-30) [keep: ] quote: "△6월 2.2%"
  - p136 South Korea total online shopping transaction value, year-on-year growth rate, J = **7.8** % (2025-07-01..2025-07-31) [keep: ] quote: "△7월 7.8%"
  - p137 South Korea total online shopping transaction value, year-on-year growth rate, A = **6** % (2025-08-01..2025-08-31) [keep: ] quote: "△8월 6.0%"
  - p138 South Korea mobile shopping transaction value, October 2025 = **17,714,300,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "모바일쇼핑 거래액은 17조7143억원으로 5.9% 늘었다."
  - p139 Mobile share of total online shopping transactions, October 2025 = **78** % (2025-10-01..2025-10-31) [keep: ] quote: "전체 거래 중 모바일 비중은 전년 동기 대비 0.8%p(포인트) 증가한 78.0%였다."
  - p140 South Korea online shopping transaction value, comprehensive malls (종합몰), Octobe = **12,329,800,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "취급상품범위별 거래액은 종합몰 12조3298억원(+2.2%), 전문몰 10조3805억원(+8.2%)로"
- `https://www.news1.kr/economy/trend/6090851` -> **snapshot** (snapshot 20260305031902); points raw/verified 8/8
  - p141 Online shopping transaction value, South Korea, November (monthly total, first t = **24,000,000,000,000** KRW (not stated (page dated 2026-03-05)) [keep: ] quote: "작년 11월 온라인쇼핑 거래액 24조원 첫 돌파...배달·음식료품이 견인"
  - p142 Online shopping transaction value, South Korea, October (monthly total, record h = **22,700,000,000,000** KRW (not stated (page dated 2026-03-05)) [keep: ] quote: "10월 온라인쇼핑 거래액 22.7조 '역대 최대'...소비쿠폰에 배달 '껑충'"
  - p143 Online shopping transaction value, South Korea, August (monthly total, record hi = **22,500,000,000,000** KRW (not stated (page dated 2026-03-05)) [keep: ] quote: "8월 온라인쇼핑 6.6% 늘어 22.5조 '역대 최대'...車·배달음식 '껑충'"
  - p144 Online shopping transaction value, South Korea, August, year-on-year growth rate = **6.6** % (not stated (page dated 2026-03-05)) [keep: ] quote: "8월 온라인쇼핑 6.6% 늘어 22.5조 '역대 최대'...車·배달음식 '껑충'"
  - p145 Online shopping transaction value, South Korea, annual total (record high, above = **272,000,000,000,000** KRW (not stated (page dated 2026-03-05)) [keep: ] quote: "'테슬라·무료배달'이 끌었다...온라인 쇼핑 272조 돌파 '역대 최대'"
  - p146 Food service online transaction growth rate (monthly, year-on-year) = **10.9** % (not stated (page dated 2026-03-05)) [keep: ] quote: "3개월 연속 24조원 넘어...음식서비스 10.9%·여행서비스 8.9%↑"
  - p147 Travel service online transaction growth rate (monthly, year-on-year) = **8.9** % (not stated (page dated 2026-03-05)) [keep: ] quote: "3개월 연속 24조원 넘어...음식서비스 10.9%·여행서비스 8.9%↑"
  - p148 Online shopping transaction value, South Korea, monthly total threshold exceeded = **24,000,000,000,000** KRW (not stated (page dated 2026-03-05)) [keep: ] quote: "3개월 연속 24조원 넘어...음식서비스 10.9%·여행서비스 8.9%↑"
- `https://www.kif.re.kr/kif/Publication/OthersDetail.aspx?NodeID=402&ControlNo=355059&ParentNodeID=0&PageNo=1&volumeID=0&SearchIndex=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120300&bid=241&nPage=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (period year 2024 does not appear in the page text or URL (likely mis-dated): 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 14; period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b2 [related_series] August seasonal factor from prior years

Hypothesis: The August-vs-July ratio (or August-vs-annual-average) of the total transaction value is the key seasonal input for converting the July 2026 level to August 2026. Historical August/July pairs (e.g., 2024, 2025) would quantify whether August runs above or below July, resolving the largest uncertainty in the YoY-scaling route.

Queries issued by the searcher: 온라인쇼핑 거래액 8월 2025 통계청 온라인쇼핑동향; 온라인쇼핑 거래액 7월 2024 통계청 월별; 2025년 7월 온라인쇼핑 동향 거래액 조원 국가데이터처; 2024년 8월 온라인쇼핑 거래액 20조 통계청 전년동월대비; 온라인쇼핑 거래액 2025년 7월 8월 통계; Statistics Korea online shopping transaction value July August 2024 2025; 온라인쇼핑동향 2024년 8월 거래액 7월; 2024년 7월 온라인쇼핑동향 거래액 20조; 2023년 8월 온라인쇼핑동향 거래액 19조; 2023년 7월 온라인쇼핑동향 거래액; site:kostat.go.kr "Online Shopping in August 2025"; 온라인쇼핑 거래액 2024년 8월 7월 통계청 온라인쇼핑동향; Statistics Korea online shopping transaction value August 2025 July 2025 trillion won; 2023년 8월 온라인쇼핑 거래액 19조 7월 18조 통계청; 2026년 7월 온라인쇼핑 동향 국가데이터처 거래액

- `https://www.stat.or.kr/lib/download.php?file_name=%ED%95%9C%EA%B5%AD%ED%86%B5%EA%B3%84%EC%9B%94%EB%B3%B4%288%EC%9B%94%29.pdf&save_file=a_2025092608291` -> **snapshot** (snapshot 20251128200456); points raw/verified 0/0
- `https://www.newsworks.co.kr/news/articleView.html?idxno=783040` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8072222&req_by=aipick` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=241&list_no=438323&mid=a10301010000` -> **snapshot** (snapshot 20260809040121); points raw/verified 14/13
  - p149 Total online shopping transaction value, South Korea, July 2025 = **23,033,500,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "2025년 7월 온라인쇼핑 거래액은 23조 335억원으로 전년동월대비 7.3% 증가했으며"
  - p150 Total online shopping transaction value, South Korea, July 2025, year-on-year gr = **7.3** % (2025-07-01..2025-07-31) [keep: ] quote: "2025년 7월 온라인쇼핑 거래액은 23조 335억원으로 전년동월대비 7.3% 증가했으며"
  - p151 Mobile shopping transaction value, South Korea, July 2025 = **18,156,800,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "온라인쇼핑 중 모바일쇼핑 거래액은 18조 1,568억원으로 10.0% 증가"
  - p152 Mobile shopping transaction value, South Korea, July 2025, year-on-year growth r = **10** % (2025-07-01..2025-07-31) [keep: ] quote: "온라인쇼핑 중 모바일쇼핑 거래액은 18조 1,568억원으로 10.0% 증가"
  - p153 Total online shopping transaction value, South Korea, July 2025, month-on-month  = **5** % (2025-07-01..2025-07-31) [keep: ] quote: "전월대비 온라인쇼핑 거래액은 5.0%, 모바일쇼핑 거래액은 6.4% 각각 증가"
  - p154 Mobile shopping transaction value, South Korea, July 2025, month-on-month growth = **6.4** % (2025-07-01..2025-07-31) [keep: ] quote: "전월대비 온라인쇼핑 거래액은 5.0%, 모바일쇼핑 거래액은 6.4% 각각 증가"
  - p155 Mobile share of total online shopping transaction value, South Korea, July 2025 = **78.8** % (2025-07-01..2025-07-31) [keep: ] quote: "온라인쇼핑 거래액 중 모바일쇼핑 거래액 비중은 78.8%로 전년동월(76.9%)에 비해 1.9%p 증가"
  - p156 Comprehensive mall online shopping transaction value, South Korea, July 2025 = **12,648,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "종합몰은 6.2% 증가한 12조 6,487억원을, 전문몰은 8.7% 증가한 10조 3,847억원을 기록"
  - p157 Specialty mall online shopping transaction value, South Korea, July 2025 = **10,384,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "종합몰은 6.2% 증가한 12조 6,487억원을, 전문몰은 8.7% 증가한 10조 3,847억원을 기록"
  - p158 Online mall transaction value, South Korea, July 2025 = **17,869,600,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "온라인몰은 7.1% 증가한 17조 8,696억원을, 온·오프라인병행몰은 8.2% 증가한 5조 1,639억원을 기록"
  - p159 Online/offline combined mall transaction value, South Korea, July 2025 = **5,163,900,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "온라인몰은 7.1% 증가한 17조 8,696억원을, 온·오프라인병행몰은 8.2% 증가한 5조 1,639억원을 기록"
  - p160 Travel and transport services transaction value, South Korea, July 2025, month-o = **11.4** % (2025-07-01..2025-07-31) [keep: ] quote: "전월대비로는 의복(-10.1%) 등에서 감소했으나, 여행 및 교통서비스(11.4%), 음·식료품(6.7%) 등에서 증가"
  - p161 Food and beverages transaction value, South Korea, July 2025, year-on-year growt = **12.6** % (2025-07-01..2025-07-31) [keep: ] quote: "음 식료품(12.6%), 음식서비스(11.0%), 자동차 및 자동차용품(54.8%) 등에서 증가"
- `https://news.nate.com/view/20251001n18532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mods.go.kr/boardDownload.es?bid=241&list_no=437829&seq=4` -> **snapshot** (snapshot 20251124053657); points raw/verified 15/15
  - p162 Total online shopping transaction value, South Korea, July 2023 = **201,296** KRW (2023-07-01..2023-07-31) [keep: ] quote: "7 201,296 25,314 6,758 14,722 3,834 3,506 2,136 1,370 44,197 16,395"
  - p163 Total online shopping transaction value, South Korea, August 2023 = **203,591** KRW (2023-08-01..2023-08-31) [keep: ] quote: "8 203,591 25,737 6,775 13,108 5,853 3,531 2,088 1,443 41,299 13,982"
  - p164 Total online shopping transaction value, South Korea, July 2024 = **214,622** KRW (2024-07-01..2024-07-31) [keep: ] quote: "7 214,622 27,021 6,353 15,235 5,432 3,816 2,296 1,520 44,386 16,606"
  - p165 Total online shopping transaction value, South Korea, August 2024 = **210,875** KRW (2024-08-01..2024-08-31) [keep: ] quote: "8 210,875 23,395 5,961 13,079 4,355 3,652 2,136 1,516 40,308 13,721"
  - p166 Total online shopping transaction value, South Korea, July 2025 (not in document = **224,300** KRW (2025-05-01..2025-05-31) [keep: ] quote: "5p 224,300 25,276 6,276 14,479 4,521 3,460 1,904 1,556 48,402 18,439"
  - p167 Total online shopping transaction value, South Korea, June 2025 (provisional) = **218,977** KRW (2025-06-01..2025-06-30) [keep: ] quote: "6p 218,977 24,551 5,946 14,956 3,648 3,220 1,742 1,478 47,056 18,292"
  - p168 Total online shopping transaction value, South Korea, annual 2024 = **2,594,319** KRW (2024-01-01..2024-12-31) [keep: ] quote: "2024 2,594,319 308,537 85,108 163,010 60,418 46,267 25,940 20,327 562,775 219,961"
  - p169 Total online shopping transaction value, South Korea, annual 2023 = **2,422,068** KRW (2023-01-01..2023-12-31) [keep: ] quote: "2023 2,422,068 304,044 87,078 156,036 60,931 44,075 24,678 19,397 557,385 217,087"
  - p170 Total online shopping transaction value, South Korea, Q2 2025 (provisional) = **660,772** KRW (2025-04-01..2025-06-30) [keep: ] quote: "2/4p 660,772 73,594 18,874 42,042 12,678 10,425 5,579 4,846 145,404 56,489"
  - p171 Total online shopping transaction value, South Korea, Q3 2024 = **635,460** KRW (2024-07-01..2024-09-30) [keep: ] quote: "3/4 635,460 75,697 18,154 40,366 17,178 11,036 6,498 4,538 126,398 45,295"
  - p172 Total online shopping transaction value, South Korea, Q3 2023 = **607,976** KRW (2023-07-01..2023-09-30) [keep: ] quote: "3/4 607,976 72,886 19,994 39,421 13,471 10,375 6,129 4,246 128,693 46,441"
  - p173 Total online shopping transaction value, South Korea, September 2024 = **209,964** KRW (2024-09-01..2024-09-30) [keep: ] quote: "9 209,964 25,281 5,839 12,051 7,390 3,568 2,066 1,502 41,703 14,968"
  - p174 Total online shopping transaction value, South Korea, September 2023 = **203,089** KRW (2023-09-01..2023-09-30) [keep: ] quote: "9 203,089 21,835 6,461 11,591 3,784 3,338 1,905 1,433 43,197 16,064"
  - p175 Total online shopping transaction value, South Korea, June 2024 = **215,186** KRW (2024-06-01..2024-06-30) [keep: ] quote: "6 215,186 25,807 6,805 15,197 3,805 3,170 1,760 1,410 45,931 17,930"
  - p176 Total online shopping transaction value, South Korea, June 2023 = **196,988** KRW (2023-06-01..2023-06-30) [keep: ] quote: "2023. 6 196,988 23,963 6,387 14,075 3,500 3,133 1,725 1,409 45,330 17,334"
- `https://bbs2.shinhansec.com/board/message/file.do?attachmentId=341272` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eiec.kdi.re.kr/policy/materialView.do?num=270389` -> **snapshot** (snapshot 20251013183813); points raw/verified 11/11
  - p177 Total online shopping transaction value, South Korea, July 2025 = **23,033,500,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "총 거래액은 23조 335억원으로 전년동월대비 7.3%(1조 5,713억원) 증가함."
  - p178 Total online shopping transaction value, South Korea, July 2025, year-on-year in = **1,571,300,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "총 거래액은 23조 335억원으로 전년동월대비 7.3%(1조 5,713억원) 증가함."
  - p179 Total online shopping transaction value, South Korea, July 2025, year-on-year gr = **7.3** % (2025-07-01..2025-07-31) [keep: ] quote: "총 거래액은 23조 335억원으로 전년동월대비 7.3%(1조 5,713억원) 증가함."
  - p180 Comprehensive mall (종합몰) online transaction value, South Korea, July 2025 = **12,648,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "취급상품범위별로 종합몰의 거래액은 12조 6,487억원으로 전년동월대비 6.2% 증가하고"
  - p181 Specialized mall (전문몰) online transaction value, South Korea, July 2025 = **10,384,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "전문몰의 거래액은 10조 3,847억원으로 전년동월대비 8.7% 증가함."
  - p182 Online-only mall (온라인몰) transaction value, South Korea, July 2025 = **17,869,600,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "운영형태별 온라인몰의 거래액은 17조 8,696억원으로 전년동월대비 7.1% 증가하고"
  - p183 Online/offline combined mall (온·오프라인병행몰) transaction value, South Korea, July 20 = **5,163,900,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "온·오프라인병행몰의 거래액은 5조 1,639억원으로 전년동월대비 8.2% 증가함."
  - p184 Mobile online shopping transaction value, South Korea, July 2025 = **18,156,800,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "모바일 거래액은 18조 1,568억원으로 전년동월대비 10.0%(1조 6,477억원) 증가했으며"
  - p185 Mobile transaction value, South Korea, July 2025, year-on-year increase = **1,647,700,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "모바일 거래액은 18조 1,568억원으로 전년동월대비 10.0%(1조 6,477억원) 증가했으며"
  - p186 Mobile share of total online shopping transaction value, South Korea, July 2025 = **78.8** % (2025-07-01..2025-07-31) [keep: ] quote: "총 거래액 중 모바일 거래액 비중은 78.8%로 전년동월대비 1.9%p 증가함."
  - p187 Mobile share of total online shopping transaction value, South Korea, July 2025, = **1.9** % (2025-07-01..2025-07-31) [keep: ] quote: "총 거래액 중 모바일 거래액 비중은 78.8%로 전년동월대비 1.9%p 증가함."
- `https://www.ytn.co.kr/_ln/0102_202509011418108696` -> **snapshot** (snapshot 20250901070751); points raw/verified 12/12
  - p188 Total online shopping transaction value, South Korea, July (record high, first m = **23,033,500,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 온라인으로 물건을 구매한 총액은 23조 335억 원으로 1년 전과 비교해 7.3% 늘었습니다."
  - p189 Year-on-year growth rate of total online shopping transaction value, South Korea = **7.3** % (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 온라인으로 물건을 구매한 총액은 23조 335억 원으로 1년 전과 비교해 7.3% 늘었습니다."
  - p190 Year-on-year growth rate of automobiles and automobile parts online shopping tra = **54.8** % (2025-07-01..2025-07-31) [keep: ] quote: "자동차 및 자동차용품이 54.8% 증가해 전체 상승세를 이끌었습니다."
  - p191 Year-on-year growth rate of food and beverages online shopping transaction value = **12.6** % (2025-07-01..2025-07-31) [keep: ] quote: "음·식료품은 12.6%, 음식서비스는 11% 증가세를 나타냈지만"
  - p192 Year-on-year growth rate of food services online shopping transaction value, Sou = **11** % (2025-07-01..2025-07-31) [keep: ] quote: "음·식료품은 12.6%, 음식서비스는 11% 증가세를 나타냈지만"
  - p193 Year-on-year change rate of bags online shopping transaction value, South Korea, = **13.8** % (2025-07-01..2025-07-31) [keep: ] quote: "가방은 13.8% 줄었습니다."
  - p194 Mobile shopping transaction value, South Korea, July (first month above 18 trill = **18,156,800,000,000** KRW (2025-07-01..2025-07-31) [keep: ] quote: "모바일 쇼핑액은 18조1천568억 원으로 1년 전보다 10% 늘었는데"
  - p195 Year-on-year growth rate of mobile shopping transaction value, South Korea, July = **10** % (2025-07-01..2025-07-31) [keep: ] quote: "모바일 쇼핑액은 18조1천568억 원으로 1년 전보다 10% 늘었는데"
  - p196 Mobile share of online shopping transaction value, South Korea, July = **78.8** % (2025-07-01..2025-07-31) [keep: ] quote: "모바일 거래액 비중도 78.8%로 1년 전보다 1.9%p 늘었습니다."
  - p197 Year-on-year change in mobile share of online shopping transaction value, South  = **1.9** % (2025-07-01..2025-07-31) [keep: ] quote: "모바일 거래액 비중도 78.8%로 1년 전보다 1.9%p 늘었습니다."
  - p198 Tesla vehicles sold in South Korea, July (imported car market sales rank 1) = **7,357** vehicle (2025-07-01..2025-07-31) [keep: ] quote: "지난 7월 테슬라는 7천357대를 팔아 국내 수입차 시장 판매 1위를 기록했는데"
  - p199 Tesla Model Y units sold in South Korea, July = **6,559** vehicle (2025-07-01..2025-07-31) [keep: ] quote: "이 가운데 신형인 모델Y가 6천559대 팔렸습니다."
- `https://www.fnnews.com/news/202409021034316402` -> **snapshot** (snapshot 20240910152516); points raw/verified 15/14
  - p200 Total online shopping transaction value, South Korea, July 2024 = **19,962,600,000,000** KRW (2024-07-01..2024-07-31) [keep: ] quote: "7월 기준 온라인쇼핑 거래액은 19조9626억원으로 전년동월대비 5.4% 증가했다."
  - p201 Total online shopping transaction value, South Korea, July 2024, year-on-year gr = **5.4** % (2024-07-01..2024-07-31) [keep: ] quote: "7월 기준 온라인쇼핑 거래액은 19조9626억원으로 전년동월대비 5.4% 증가했다."
  - p202 Mobile shopping transaction value, South Korea, July 2024 = **15,117,300,000,000** KRW (2024-07-01..2024-07-31) [keep: ] quote: "이 가운데 모바일쇼핑 거래액은 15조 1173억원으로 6.9% 늘며"
  - p203 Mobile shopping transaction value, South Korea, July 2024, year-on-year growth r = **6.9** % (2024-07-01..2024-07-31) [keep: ] quote: "모바일쇼핑 거래액은 15조 1173억원으로 6.9% 늘며"
  - p204 Online shopping share of total retail sales, South Korea, 2024 (July) = **27** % (2024-07-01..2024-07-31) [keep: ] quote: "전체 소매판매 가운데 비중은 지난해 25% 수준에서 올해 27%로 4분의 1을 훌쩍 넘어섰다."
  - p205 General mall (종합몰) online shopping transaction value, South Korea, July 2024 = **11,826,400,000,000** KRW (2024-07-01..2024-07-31) [keep: ] quote: "종합몰은 3.0% 증가한 11조8264억원을, 전문몰은 9.1% 증가한 8조1361억원을 기록했다."
  - p206 Specialty mall (전문몰) online shopping transaction value, South Korea, July 2024 = **8,136,100,000,000** KRW (2024-07-01..2024-07-31) [keep: ] quote: "종합몰은 3.0% 증가한 11조8264억원을, 전문몰은 9.1% 증가한 8조1361억원을 기록했다."
  - p207 General mall share of total online shopping transaction value, South Korea, July = **59.2** % (2024-07-01..2024-07-31) [keep: ] quote: "7월 기준 총 거래액의 59.2%가 종합몰, 나머지 40.8%가 한 가지의 상품을 집중 판매하는 '전문몰'을 통하고 있다."
  - p208 Specialty mall share of total online shopping transaction value, South Korea, Ju = **40.8** % (2024-07-01..2024-07-31) [keep: ] quote: "7월 기준 총 거래액의 59.2%가 종합몰, 나머지 40.8%가 한 가지의 상품을 집중 판매하는 '전문몰'을 통하고 있다."
  - p209 General mall transaction value year-on-year growth rate, South Korea, July 2024 = **3** % (2024-07-01..2024-07-31) [keep: ] quote: "종합몰은 3.0% 증가한 11조8264억원을, 전문몰은 9.1% 증가한 8조1361억원을 기록했다."
  - p210 Specialty mall transaction value year-on-year growth rate, South Korea, July 202 = **9.1** % (2024-07-01..2024-07-31) [keep: ] quote: "종합몰은 3.0% 증가한 11조8264억원을, 전문몰은 9.1% 증가한 8조1361억원을 기록했다."
  - p211 Food and beverages share of total online shopping transaction value, South Korea = **14.2** % (2024-07-01..2024-07-31) [keep: ] quote: "상품군별 거래액 구성비는 음·식료품(14.2%), 음식서비스(12.8%), 여행 및 교통서비스(11.5%) 순으로 높았다."
  - p212 Food services share of total online shopping transaction value, South Korea, Jul = **12.8** % (2024-07-01..2024-07-31) [keep: ] quote: "상품군별 거래액 구성비는 음·식료품(14.2%), 음식서비스(12.8%), 여행 및 교통서비스(11.5%) 순으로 높았다."
  - p213 Travel and transport services share of total online shopping transaction value,  = **11.5** % (2024-07-01..2024-07-31) [keep: ] quote: "상품군별 거래액 구성비는 음·식료품(14.2%), 음식서비스(12.8%), 여행 및 교통서비스(11.5%) 순으로 높았다."
- `https://sns.korea.kr/common/download.do?tblKey=EDN&fileId=197883101` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.ekn.kr/view.php?key=20251201028393281` -> **snapshot** (snapshot 20251201060217); points raw/verified 15/13
  - p214 Total online shopping transaction value, South Korea, October 2025 = **22,710,300,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "이달 동안 온라인 쇼핑 거래액은 22조7103억원으로 작년 동월보다 4.9% 증가했다."
  - p215 Total online shopping transaction value, South Korea, September 2025 = **23,795,600,000,000** KRW (2025-09-01..2025-09-30) [keep: ] quote: "특히 9월에는 증가율 13.3%, 거래액 23조7956억원으로 통계 작성 이후 최고치를 기록했다."
  - p216 YoY growth rate of total online shopping transaction value, South Korea, July 20 = **7.8** % (2025-07-01..2025-07-31) [keep: ] quote: "그러나 7월 증가율이 7.8%로 반등한 데 이어 8월에도 6.6% 증가하며 회복세를 나타냈다."
  - p217 YoY growth rate of total online shopping transaction value, South Korea, August  = **6.6** % (2025-08-01..2025-08-31) [keep: ] quote: "그러나 7월 증가율이 7.8%로 반등한 데 이어 8월에도 6.6% 증가하며 회복세를 나타냈다."
  - p218 YoY growth rate of total online shopping transaction value, South Korea, Septemb = **13.3** % (2025-09-01..2025-09-30) [keep: ] quote: "특히 9월에는 증가율 13.3%, 거래액 23조7956억원으로 통계 작성 이후 최고치를 기록했다."
  - p219 YoY growth rate of total online shopping transaction value, South Korea, October = **4.9** % (2025-10-01..2025-10-31) [keep: ] quote: "이달 동안 온라인 쇼핑 거래액은 22조7103억원으로 작년 동월보다 4.9% 증가했다."
  - p220 YoY growth rate of total online shopping transaction value, South Korea, January = **1.6** % (2025-01-01..2025-01-31) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p221 YoY growth rate of total online shopping transaction value, South Korea, Februar = **3.7** % (2025-02-01..2025-02-28) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p222 YoY growth rate of total online shopping transaction value, South Korea, March 2 = **2.5** % (2025-03-01..2025-03-31) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p223 YoY growth rate of total online shopping transaction value, South Korea, April 2 = **2.8** % (2025-04-01..2025-04-30) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p224 YoY growth rate of total online shopping transaction value, South Korea, May 202 = **0.6** % (2025-05-01..2025-05-31) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p225 YoY growth rate of total online shopping transaction value, South Korea, June 20 = **2.2** % (2025-06-01..2025-06-30) [keep: ] quote: "올해 들어서도 1월 1.6%, 2월 3.7%, 3월 2.5%, 4월 2.8%, 5월 0.6%, 6월 2.2% 등 부진이 이어졌다."
  - p226 Mobile shopping transaction value, South Korea, October 2025 = **17,714,300,000,000** KRW (2025-10-01..2025-10-31) [keep: ] quote: "온라인쇼핑 중 모바일쇼핑 거래액은 17조7143억원으로 5.9% 증가했다."
- dropped by code checks: 4 (period year 2024 does not appear in the page text or URL (likely mis-dated): 3; period year 2023 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [related_series] August 2026 early/partial indicators

Hypothesis: Any August 2026 partial data (e.g., card-network online spend, platform GMV, or a first-20-day figure) would anchor the level directly and resolve whether the July 2026 momentum (7.3% YoY) held, accelerated, or faded in August. This is the single most valuable missing input for the target month.

Queries issued by the searcher: 2026년 8월 온라인쇼핑 거래액 통계; 온라인쇼핑동향 2026년 7월 거래액 7.3%; 2026년 8월 카드 결제액 BC카드 신한카드 온라인 결제 증가; 2026년 8월 1~20일 수출 소매 판매 동향; 2025년 8월 온라인쇼핑 거래액 22조 전년동월대비; 2026년 8월 온라인쇼핑동향 거래액; 2026년 8월 온라인 카드 결제액 증가율; 2026년 7월 온라인쇼핑동향 거래액 25조 1074억; 여신금융협회 2026년 8월 카드승인실적 온라인; 2026년 8월 온라인쇼핑 거래액 동향; 2026년 8월 온라인 카드 결제액 증가율; 2026년 7월 온라인쇼핑동향 거래액 25조1074억원; 2025년 8월 온라인쇼핑 거래액 22조 전년동월비

- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&act=view&list_no=447300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fnnews.com/news/202610011202444153` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=241&list_no=446725&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4871104?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20261001_0003809970` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/archive/expDocView.do?docId=41897&group=S` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4844676?srchOrgCd=1241000&pageIndex=2&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.nocutnews.co.kr/news/noad6575182` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://slv.news.einfomax.co.kr/news/articleView.html?idxno=4442133` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.gov.kr/portal/ntnadmNews/4871104?&pageIndex=134&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301120200&bid=241&act=view&list_no=447300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsws.kbs.co.kr/news/pc/view/view.do?ncd=8675566` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['korea online shopping', 'korea retail sales', 'korea e-commerce']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p16', 'p31', 'p70'] Same August 2025 total (22.4802조원) reported by four outlets; all trace to the same Statistics Korea Online Shopping Trends release, so this is one measurement, not four independent confirmations.
- corroborating: ['p2', 'p17', 'p32', 'p72'] Same YoY increase (1조3927억원) for August 2025; same underlying release.
- corroborating: ['p3', 'p18', 'p33', 'p71'] Same 6.6% YoY growth for August 2025; single source measurement.
- corroborating: ['p11', 'p42', 'p73'] Same mobile value 17.8489조원 for August 2025; one measurement.
- corroborating: ['p12', 'p43', 'p76'] Same 79.4% mobile share for August 2025; one measurement.
- corroborating: ['p13', 'p28', 'p34'] Same food services value 3.7366조원 for August 2025.
- corroborating: ['p14', 'p25', 'p36'] Same food & beverages value 3.2051조원 for August 2025.
- corroborating: ['p15', 'p45'] Same comprehensive mall value 11.95조원 for August 2025.
- corroborating: ['p19', 'p39'] Same automobiles value 7821억원 for August 2025.
- corroborating: ['p20', 'p23', 'p26', 'p29'] Group-level YoY increases consistent with the reported group levels and growth rates.
- corroborating: ['p46', 'p48', 'p49', 'p51', 'p52', 'p53', 'p55', 'p56', 'p57', 'p58', 'p60'] All from the same July 2026 Online Shopping Trends release (fnnews snapshot 2026-09-01); internally consistent (mobile/total ≈ 78%, group shares sum plausibly). This is the most recent observed month 
- corroborating: ['p47'] March 2026 record 25.5434조원 is consistent with July 2026 being second-largest at 25.0954조원; same series.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91'] July 2026 retail sales trend report (khan) — different survey (retail sales index / distribution sales) but directionally consistent with strong online growth (~8.5%) in July 2026. Different scope (re
- corroborating: ['p61', 'p62', 'p63'] JP Morgan 2026 e-commerce forecast of 300조원/year and historical annual growth rates (11% 2022, 8.4% 2023) are consistent with a monthly level around 25조원 in mid-2026 (300/12 = 25조). Forecast, not an a
- corroborating: ['p100', 'p101', 'p102', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111'] Home-shopping/SSG/11st seasonal-appliance growth anecdotes for summer 2026 (heat-wave driven). Directionally supportive of elevated summer appliance demand but tiny scope relative to total; not usable
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'] Monthly YoY growth rates through 2025 show a decelerating trend (1.6% Jan → 7.8% Jul → 6.6% Aug 2025), useful for the growth-trend component of the forecast.
- corroborating: ['p46', 'p51'] July 2026 total and its 7.3% YoY growth are internally consistent with the July 2025 base implied by the 2025 series.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p137', 'p143', 'p144', 'p217'] All describe the same August 2025 total (22.48tn KRW, +6.6% YoY); p2/p3/p137/p144/p217 are restatements of the same underlying Statistics Korea release, not independent measurements.
- corroborating: ['p46', 'p47', 'p51', 'p48', 'p49', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60'] All from the same July 2026 Online Shopping Trends release (fnnews snapshot 2026-09-01); internally consistent (mobile 19.5716/25.0954 = 78.0%; food services 3.8945/25.0954 = 15.5%). Single underlying
- corroborating: ['p46', 'p47'] July 2026 (25.0954tn) is described as second-largest after March 2026 (25.5434tn); consistent ordering, same release.
- corroborating: ['p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p215', 'p218'] September 2025 release (mods.go.kr) and later press restatements agree on 23.7956tn and +13.3%; same underlying release.
- corroborating: ['p126', 'p127', 'p128', 'p138', 'p139', 'p140', 'p142', 'p214', 'p219', 'p226'] October 2025 total 22.7103tn, +4.9%, mobile 17.7143tn (78.0%); multiple press copies of one release.
- corroborating: ['p141', 'p145', 'p146', 'p147', 'p148'] November 2025 above 24tn and 2025 annual above 272tn; consistent with the monthly path (Sep 23.8, Oct 22.7, Nov >24).
- corroborating: ['p149', 'p150', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159', 'p177', 'p178', 'p179', 'p180', 'p181', 'p182', 'p183', 'p184', 'p185', 'p186', 'p187', 'p188', 'p189', 'p194', 'p195', 'p196', 'p197'] July 2025 total 23.0335tn, +7.3%, mobile 18.1568tn (78.8%); multiple press copies of one release.
- corroborating: ['p162', 'p163', 'p164', 'p165', 'p166', 'p167', 'p168', 'p169', 'p170', 'p171', 'p172', 'p173', 'p174', 'p175', 'p176'] KOSIS table extract in billions KRW (units mislabeled in table as KRW); internally consistent with press totals (e.g. Jul 2024 214.6tn vs p200 199.6tn differ by revision/definition — see conflict note
- conflicting: ['p200', 'p201', 'p202', 'p203', 'p204', 'p205', 'p206', 'p207', 'p208', 'p209', 'p210', 'p211', 'p212', 'p213'] July 2024 total 19.9626tn (p200) vs KOSIS table 214.622tn (p164) — a large gap reflecting series revision/definition change (2017 rebasing and later revisions); do not median across vintages. Use one 
- corroborating: ['p61', 'p62', 'p63'] JP Morgan 2026 e-commerce forecast of 300tn KRW and historical annual growth rates; forecast is a market-size projection, not the official transaction-value series, so only a loose cross-check.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99'] July 2026 retail sales trend release (khan.co.kr): online +8.5%, total +6.4%, online share 60.8% by business type — different scope (retail sales survey, business-type shares) from Online Shopping Tre
- corroborating: ['p100', 'p101', 'p102', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111'] Home-shopping/SSG/11st seasonal-appliance growth anecdotes for late July 2026; directionally consistent with a hot summer boosting appliance/fan/dehumidifier online sales, but tiny scope and no level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY growth of total online shopping value | 7 | 4..10 | 4..10 | % | m3 (m3) | July 2026 ran +7.3% (p51); 2025 monthly YoY ranged 0.6–13.3% with a mid-year dip then rebound. August has no gift holiday; summer travel/appliance demand supports a similar pace. Range spans a slowdown to ~4% and a re-acceleration to ~10%. | August 2026 momentum resembles July 2026 rather than a sharp break. | Card-network or platform data showing August 2026 YoY well below 4% or above 10%. |
| a2 | August-to-July seasonal ratio of total online shopping value | 1 | 0.93..1.07 | 0.7054..1.411 (widened) | 1 | m2 (m2) | Historical Aug/Jul ratios: 2023 203.591/201.296=1.011; 2024 210.875/214.622=0.983; 2025 22.4802/23.0335=0.976. Ratios cluster near 0.98–1.01; range allows for summer-vacation uplift or post-July cooling. | August 2026 seasonal pattern resembles 2023–2025. | Evidence of an unusual August 2026 promotion or heatwave shifting the ratio outside 0.93–1.07. |
| a3 | August 2026 YoY growth of total online shopping value (yoy_scaling signal) | 7 | 4..10 | 4..10 | % | unused | Same basis as a1: July 2026 +7.3% (p51) is the latest observed momentum; August 2025 grew 6.6% (p3) and 2025 monthly growth ranged 0.6–13.3%. Used as the signal for the yoy_scaling route because no kept point gives August 2026 growth directly. | August 2026 growth is close to July 2026's pace. | Any August 2026 partial data showing growth outside 4–10%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | n/a | ['p1', 'p46'] / [] | [] |  | 0.00 |  | yoy_scaling needs signal for 2025 |
| m2 | formula_mc | 25,096,331,327,528 | ['p46'] / ['a2'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m3 | formula_mc | 23,995,535,780,802 | ['p1'] / ['a1'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m2 formula_mc: p46 * a2; Monte Carlo P10 to P90 16,992,541,776,027 to 37,226,819,635,774; result unit (KRW/month) * 1 month converted to KRW; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 formula_mc: p1 * (1 + a1); Monte Carlo P10 to P90 19,983,833,502,366 to 28,906,527,099,859; result unit (KRW/month) * 1 month converted to KRW; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 25,096,331,327,528 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m3: 23,995,535,780,802 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.43; Birge ratio 0.11 (not above one, so no widening); final width x/÷1.43.
- Seasonal naive baseline (not combined): 22,480,200,000,000 (2025, from m1); the estimate is +9.2% against it.

Result: central **24,539,761,945,393** KRW, 80% interval [17,154,076,458,568, 35,105,353,400,462] KRW, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

Unit of the estimate: KRW (total for 2026-08-01 to 2026-08-31)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

Best estimate for total online shopping transaction value in South Korea for August 2026: 24,539,761,945,393 KRW (80% model-based interval 17,154,076,458,568 to 35,105,353,400,462 KRW). Scope is the headline total online shopping transaction value (온라인쇼핑 거래액) for the full month, as would be first reported in the National Data Office's Online Shopping Trends release.

Evidence: one route scales the observed July 2026 level (25,095,400,000,000 KRW) by an August/July seasonal ratio (1, range 0.7054 to 1.411); the other grows the observed August 2025 total (22,480,200,000,000 KRW) by an assumed August 2026 YoY rate (7%, range 4% to 10%). Both observed points are actual published figures; the seasonal ratio and growth rate are analyst assumptions, not observations. Code combined the two blocks by geometric mean with equal block weights because their inputs overlap by less than half; the interval reflects the blocks' own widths (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number).

Main risk: August 2026 growth or seasonality diverging from the July momentum and historical Aug/Jul pattern. The most useful missing evidence would be an early August 2026 partial-month indicator or a published August figure.

Unit of the estimate: KRW (total for 2026-08-01 to 2026-08-31).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 YoY growth of total online shopping value: 7%, range 4% to 10%; used by m3. Overturned by: Card-network or platform data showing August 2026 YoY well below [n] or above [n].
- a2 August-to-July seasonal ratio of total online shopping value: 1 [n], range 0.7054 to 1.411 (range widened by code); used by m2. Overturned by: Evidence of an unusual August 2026 promotion or heatwave shifting the ratio outside [n]–[n].

Method details (computed by code):
- m2 formula_mc: p46 * a2; Monte Carlo P10 to P90 16,992,541,776,027 to 37,226,819,635,774; result unit (KRW/month) * 1 month converted to KRW; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 formula_mc: p1 * (1 + a1); Monte Carlo P10 to P90 19,983,833,502,366 to 28,906,527,099,859; result unit (KRW/month) * 1 month converted to KRW; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m2: 25,096,331,327,528 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m3: 23,995,535,780,802 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.43; Birge ratio 0.11 (not above one, so no widening); final width x/÷1.43.
- Seasonal naive baseline (not combined): 22,480,200,000,000 (2025, from m1); the estimate is +9.2% against it.

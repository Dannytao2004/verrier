# Evidence ledger: fc_tw_restaurants_2026_09

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate the turnover of Taiwan's food and beverage services industry (餐飲業營業額, current prices) in September 2026, in New Taiwan dollars (TWD), as it will be first reported in the Ministry of Economic Affairs Department of Statistics' monthly release on wholesale, retail and food services turnover (批發、零售及餐飲業營業額統計).
- as_of: 2026-10-19
- Pinned target: Monthly turnover (revenue, current prices) of Taiwan's food and beverage services industry (餐飲業營業額), as reported in the MOEA Department of Statistics monthly release on wholesale, retail and food services turnover; total industry, domestic activity, all enterprise sizes covered by the survey | unit TWD | period 2026-09-01..2026-09-30 | publisher Ministry of Economic Affairs, Department of Statistics (經濟部統計處)

## Directions and pages

### d1 [own_history] MOEA statistical releases

Hypothesis: September 2026 turnover = September 2025 turnover grown by the recent year-on-year growth rate, adjusted for calendar (Mid-Autumn Festival timing, number of weekend days) and price effects; the target's own recent monthly series and prior-year September value anchor the level.

Queries issued by the searcher: 經濟部統計處 餐飲業營業額 2026年8月; 批發零售及餐飲業營業額 2026 統計 餐飲業 年增率; 2025年9月 餐飲業營業額 億元 年增率 經濟部統計處; 7月 餐飲業營業額 2026 年增 經濟部統計處 公布

- `https://iknow.stpi.niar.org.tw/Post/Read.aspx?PostID=22446` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.yesfund.com.tw/w/wp/wp05A.djhtm?a=%7BC1BFF93C-B69F-4ADD-8BD0-2721931BC455%7D&c=3` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://210.66.210.14/KMDJ/News/NewsViewer.aspx?a=5c2f82fc-b818-4399-b4d4-6f22d73cf56f` -> **live_dated** (page date 2026-09-23); points raw/verified 9/8
  - p1 Taiwan food and beverage services industry (餐飲業) monthly turnover, August 2026 = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of the August 2026 level (p13/p45/p52/p81/p114).] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%,為連續7個月正成長,並為同期新高"
  - p2 Taiwan food and beverage services industry (餐飲業) August 2026 month-on-month turn = **7** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August MoM growth.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p3 Taiwan food and beverage services industry (餐飲業) August 2026 year-on-year turnov = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August YoY growth (p17/p46/p53/p82/p116).] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%,為連續7個月正成長,並為同期新高"
  - p4 Taiwan food and beverage services industry (餐飲業) cumulative January-August 2026  = **737,200,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative (p14/p50/p86/p120).] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高。"
  - p5 Taiwan food and beverage services industry (餐飲業) cumulative January-August 2026  = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative growth.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高。"
  - p6 Taiwan retail trade (零售業) monthly turnover, August 2026 = **416,800,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail level (p11/p54/p88).] quote: "零售業8月營業額為4,168億元,月減0.5%、年增6.5%"
  - p7 Taiwan retail trade (零售業) August 2026 year-on-year turnover growth rate = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail growth (p16/p55/p89).] quote: "零售業8月營業額為4,168億元,月減0.5%、年增6.5%,連續7個月正成長"
  - p8 Taiwan wholesale trade (批發業) August 2026 year-on-year turnover growth rate = **65.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale growth (p15/p57/p92).] quote: "批發業8月營業額為1兆8,501億元,月增5.2%、年增65.4%,創下歷史新高"
- `https://www.chinatimes.com/newspapers/20250925000136-260202?chdtv` -> **live_dated** (page date 2025-09-25); points raw/verified 13/0
- dropped by code checks: 14 (number: compound CJK number (519万548): leave scale_word empty and give the whole number: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 11; number: value_as_written is only part of a larger CJK number in the quote: 1; value_as_written not in quote as a whole number: 1)

### d2 [related_series] MOEA retail/wholesale release

Hypothesis: Food service turnover moves with retail trade and overall private consumption; the food-service share of total retail+food-service turnover is fairly stable, so a broader total times share gives a cross-check.

Queries issued by the searcher: 經濟部統計處 批發業 零售業 餐飲業 營業額 2026年9月; 零售業營業額 餐飲業 占比 2025 經濟部; 經濟部統計處 新聞稿 115年8月 批發零售及餐飲業營業額 統計處 網址; "餐飲業" 9月 營業額 854 879 億元 預估 零售業 4104 4223

- `https://pchome.megatime.com.tw/news/cat8/20260923/17901614405403618003.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://mnscdn.moea.gov.tw/MNS/dos/bulletin/Bulletin.aspx?kind=8&html=1&menu_id=6727&bull_id=16913` -> **live_dated** (page date 2012-12-14); points raw/verified 15/15
  - p9 Taiwan wholesale trade turnover, August 2026 (monthly) = **1,850,100,000,000** as written "1兆8,501億元", value check pending TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale level (p56/p91).] quote: "8月批發業營業額為1兆8,501億元,年增65.4%"
  - p10 Taiwan wholesale trade turnover, January-August 2026 cumulative = **12,642,400,000,000** as written "12兆6,424億元", value check pending TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug wholesale cumulative (p94).] quote: "綜計1至8月營業額為12兆6,424億元,年增39.8%"
  - p11 Taiwan retail trade turnover, August 2026 (monthly) = **416,800,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail level.] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p12 Taiwan retail trade turnover, January-August 2026 cumulative = **3,298,300,000,000** as written "3兆2,983億元", value check pending TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug retail cumulative (p93).] quote: "綜計1至8月營業額為3兆2,983億元,年增4.9%"
  - p13 Taiwan food and beverage services turnover, August 2026 (monthly) = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service level (p45/p52/p81/p114).] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p14 Taiwan food and beverage services turnover, January-August 2026 cumulative = **737,200,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug food-service cumulative.] quote: "綜計1至8月營業額為7,372億元,年增3.7%"
  - p15 Taiwan wholesale trade turnover year-on-year growth, August 2026 = **65.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale growth.] quote: "8月批發業營業額為1兆8,501億元,年增65.4%"
  - p16 Taiwan retail trade turnover year-on-year growth, August 2026 = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail growth.] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p17 Taiwan food and beverage services turnover year-on-year growth, August 2026 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service growth.] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p18 Taiwan food, beverage and tobacco retail turnover year-on-year growth, August 20 = **13.1** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food/beverage/tobacco retail growth (p90).] quote: "食品、飲料及菸草零售業年增13.1%"
  - p19 Taiwan supermarket turnover year-on-year growth, August 2026 = **8.7** % (2026-08-01..2026-08-31) [DISCARD: Supermarket growth is retail, not food service; redundant with p90 context.] quote: "超級市場年增8.7%"
  - p20 Taiwan hypermarket turnover year-on-year growth, August 2026 = **9** % (2026-08-01..2026-08-31) [DISCARD: Hypermarket growth is retail, not food service.] quote: "量販店年增9.0%"
  - p21 Taiwan department store turnover year-on-year growth, August 2026 = **8.4** % (2026-08-01..2026-08-31) [DISCARD: Department store growth is retail, not food service.] quote: "百貨公司年增8.4%"
  - p22 Taiwan restaurants turnover year-on-year growth, August 2026 = **0.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August restaurant growth (p47/p83/p117).] quote: "餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
  - p23 Taiwan beverage shops turnover year-on-year growth, August 2026 = **7.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August beverage-shop growth (p48/p84/p118).] quote: "餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
- `https://ocacnews.net/article/413979?cid=13` -> **dropped** (live page has no readable date); points raw/verified -/-
- `http://www.tcfa.org.tw/announce_detail.asp?id=9212579` -> **live_dated** (page date 2026-01-23); points raw/verified 15/15
  - p24 Taiwan retail trade turnover, full year 2025 = **4,844,800,000,000** as written "4兆8448億元", value check pending TWD (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 retail level is not needed for a September food-service estimate.] quote: "經濟部1月23日公布2025年零售業營業額為4兆8448億元,年減0.2%翻黑"
  - p25 Taiwan food and beverage services turnover, full year 2025 = **1,067,400,000,000** TWD (2025-01-01..2025-12-31) [keep: ] quote: "餐飲業營業額1兆674億元,年增2.9%"
  - p26 Taiwan wholesale trade turnover, full year 2025 = **14,071,800,000,000** TWD (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 wholesale level is not needed.] quote: "批發業為14兆718億元,年增8.7%"
  - p27 Taiwan wholesale trade turnover, December 2025 = **1,251,400,000,000** TWD (2025-12-01..2025-12-31) [DISCARD: December 2025 wholesale level is not needed.] quote: "批發業營業額1兆2514億元,年增6.6%,連11紅"
  - p28 Taiwan retail trade turnover, December 2025 = **437,900,000,000** TWD (2025-12-01..2025-12-31) [DISCARD: December 2025 retail level is not needed.] quote: "零售業為4379億元,年增0.9%,連3紅"
  - p29 Taiwan food and beverage services turnover, December 2025 = **95,000,000,000** TWD (2025-12-01..2025-12-31) [DISCARD: December 2025 food-service level is not needed for September.] quote: "餐飲業為950億元,年減1.1%翻黑"
  - p30 Taiwan motor vehicle and parts retail turnover, December 2025 = **83,500,000,000** TWD (2025-12-01..2025-12-31) [DISCARD: Motor-vehicle retail turnover is unrelated to food service.] quote: "汽機車零售業12月單月營業額達835億元,年增約1成"
  - p31 Taiwan wholesale trade turnover forecast, January 2026, lower bound = **1,212,800,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 wholesale forecast is irrelevant to September food service.] quote: "統計處預估,2026年1月批發業營業額1兆2128億元至1兆2456億元"
  - p32 Taiwan wholesale trade turnover forecast, January 2026, upper bound = **1,245,600,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 wholesale forecast is irrelevant to September food service.] quote: "統計處預估,2026年1月批發業營業額1兆2128億元至1兆2456億元"
  - p33 Taiwan retail trade turnover forecast, January 2026, lower bound = **424,600,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 retail forecast is irrelevant to September food service.] quote: "零售業營業額4246億元至4380億元,年減4.8%至1.8%"
  - p34 Taiwan retail trade turnover forecast, January 2026, upper bound = **438,000,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 retail forecast is irrelevant to September food service.] quote: "零售業營業額4246億元至4380億元,年減4.8%至1.8%"
  - p35 Taiwan food and beverage services turnover forecast, January 2026, lower bound = **96,000,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 food-service forecast is too distant to inform September and is superseded by the September forecast.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p36 Taiwan food and beverage services turnover forecast, January 2026, upper bound = **99,200,000,000** TWD (2026-01-01..2026-01-31) [DISCARD: January 2026 food-service forecast is too distant to inform September and is superseded by the September forecast.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p37 Taiwan retail trade turnover year-on-year change, full year 2025 = **0.2** % (2025-01-01..2025-12-31) [DISCARD: Full-year 2025 retail change is unrelated context for food service.] quote: "2025年零售業營業額年減0.2%,主因是受到汽機車等耐久財與高單價商品銷售疲弱的拖累"
  - p38 Taiwan retail trade turnover year-on-year change excluding motor vehicles, full  = **1.5** % (2025-01-01..2025-12-31) [DISCARD: Retail ex-vehicles change is unrelated context for food service.] quote: "若排除汽機車零售業,整體營業額將轉為年增1.5%"

### d3 [physical_flow] restaurant operators / POS and card data

Hypothesis: Aggregate card-spending and POS transaction data for dining track food-service turnover; growth in restaurant card spend YoY approximates nominal turnover growth.

Queries issued by the searcher: 台灣 餐飲業營業額 2026年9月 經濟部統計處; 台灣 餐飲 信用卡 刷卡金額 統計 2026; 聯合信用卡中心 食品餐飲類 簽帳金額 年增率 2026年; food delivery Taiwan GMV growth 2026 Uber Eats foodpanda 市場規模

- `http://210.17.21.214/KMDJ/News/NewsViewer.aspx?a=790fb33a-3adb-4281-93cd-b724e02de46b` -> **live_dated** (page date 2026-09-23); points raw/verified 15/13
  - p39 Forecast September 2026 food and beverage services industry turnover (MOEA), upp = **87,900,000,000** TWD (2026-09-01..2026-09-30) [DISCARD: Duplicate of p110 (September 2026 forecast upper bound).] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p40 Forecast September 2026 food and beverage services industry turnover YoY growth, = **3** % (2026-09-01..2026-09-30) [DISCARD: Duplicate of the September 2026 forecast lower growth bound.] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p41 Forecast September 2026 food and beverage services industry turnover YoY growth, = **6** % (2026-09-01..2026-09-30) [DISCARD: Duplicate of the September 2026 forecast upper growth bound.] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p42 Forecast Q3 2026 food and beverage services industry turnover, upper bound = **271,600,000,000** TWD (2026-07-01..2026-09-30) [DISCARD: Duplicate of p112 (Q3 2026 forecast upper bound).] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p43 Forecast Q3 2026 food and beverage services industry turnover YoY growth, lower  = **2.4** % (2026-07-01..2026-09-30) [DISCARD: Duplicate of the Q3 2026 forecast lower growth bound.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p44 Forecast Q3 2026 food and beverage services industry turnover YoY growth, upper  = **3.4** % (2026-07-01..2026-09-30) [DISCARD: Duplicate of the Q3 2026 forecast upper growth bound.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p45 August 2026 food and beverage services industry turnover = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service level.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p46 August 2026 food and beverage services industry turnover YoY growth = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service growth.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p47 August 2026 restaurants turnover YoY growth = **0.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August restaurant growth.] quote: "餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,8月營業額分別年增0.3%及7.4%"
  - p48 August 2026 beverage shops turnover YoY growth = **7.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August beverage-shop growth.] quote: "餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,8月營業額分別年增0.3%及7.4%"
  - p49 August 2026 catering and contract food service turnover YoY growth = **11** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August catering/contract growth (p85/p119).] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11%"
  - p50 January-August 2026 food and beverage services industry cumulative turnover = **737,200,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p51 January-August 2026 food and beverage services industry cumulative turnover YoY  = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative growth.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
- `https://www.moea.gov.tw/Mns/dos/home/Home.aspx` -> **live_dated** (page date 2012-12-14); points raw/verified 15/15
  - p52 Taiwan food and beverage services industry turnover (餐飲業營業額), August 2026 (ROC 1 = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service level.] quote: "115年8月 餐飲業營業額 9/23/2026發布 950億元"
  - p53 Taiwan food and beverage services industry turnover YoY growth rate, August 2026 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service growth.] quote: "115年8月 餐飲業營業額 9/23/2026發布 950億元 1.8%"
  - p54 Taiwan retail trade turnover (零售業營業額), August 2026 = **416,800,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail level.] quote: "115年8月 零售業營業額 9/23/2026發布 4,168億元"
  - p55 Taiwan retail trade turnover YoY growth rate, August 2026 = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail growth.] quote: "115年8月 零售業營業額 9/23/2026發布 4,168億元 6.5%"
  - p56 Taiwan wholesale trade turnover (批發業營業額), August 2026 = **1,850,100,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale level.] quote: "115年8月 批發業營業額 9/23/2026發布 18,501億元"
  - p57 Taiwan wholesale trade turnover YoY growth rate, August 2026 = **65.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale growth.] quote: "115年8月 批發業營業額 9/23/2026發布 18,501億元 65.4 %"
  - p58 Taiwan consumer price index, September 2026 (index level) = **113** index (2026-09-01..2026-09-30) [DISCARD: Redundant copy of September CPI level (p68 context).] quote: "115年9月 消費者物價指數 10/7/2026發布 112.82"
  - p59 Taiwan consumer price index YoY growth rate, September 2026 = **2.73** % (2026-09-01..2026-09-30) [DISCARD: Redundant copy of September CPI growth (p68).] quote: "115年9月 消費者物價指數 10/7/2026發布 112.82 2.73%"
  - p60 Taiwan producer price index, September 2026 (index level) = **127** index (2026-09-01..2026-09-30) [DISCARD: PPI level is not a deflator for consumer food-service turnover.] quote: "115年9月 生產者物價指數 10/7/2026發布 127.03"
  - p61 Taiwan producer price index YoY growth rate, September 2026 = **18.12** % (2026-09-01..2026-09-30) [DISCARD: PPI growth is not a deflator for consumer food-service turnover.] quote: "115年9月 生產者物價指數 10/7/2026發布 127.03 18.12 %"
  - p62 Taiwan economic growth rate, Q2 2026 (preliminary) = **12.93** % (2026-04-01..2026-06-30) [DISCARD: Q2 GDP growth is background only and not usable in a turnover formula.] quote: "115年第2季(p) 經濟成長率 8/14/2026發布 12.93%"
  - p63 Taiwan economic growth rate, Q1 2026 (revised) = **15.43** % (2026-01-01..2026-03-31) [DISCARD: Q1 GDP growth is background only.] quote: "115年第1季(r) 經濟成長率 8/14/2026發布 15.43%"
  - p64 Taiwan economic growth rate, Q4 2025 = **12.95** % (2025-10-01..2025-12-31) [DISCARD: Q4 2025 GDP growth is background only.] quote: "114年第4季 經濟成長率 8/14/2026發布 12.95%"
  - p65 Taiwan unemployment rate, August 2026 = **3.41** % (2026-08-01..2026-08-31) [DISCARD: Unemployment rate is background only.] quote: "115年8月 失業率 9/22/2026發布 3.41%"
  - p66 Taiwan total monthly salary per employee, August 2026 = **65,826** TWD per person per month (2026-08-01..2026-08-31) [DISCARD: Monthly salary is background only.] quote: "115年8月 每人每月總薪資 10/15/2026發布 65,826元"
- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/CreditCardData/Jobsconsumption?WCM_PI=1&WCM_Page.aa5a95cd-0b6b-403f-bb0c-ee319cf16024=` -> **live_dated** (page date 2026-10-01); points raw/verified 6/1
  - p67 Update date of NCCC credit-card food & dining spending by occupation CSV = **2,026** date (2026-09-30..2026-09-30) [DISCARD: The NCCC CSV update date carries no spending value; the underlying dining card-spend numbers are not in the table.] quote: "\| 各職業類別持卡人以信用卡支付食品餐飲類消費之總簽帳金額及筆數 \| CSV \| 49 KB \| 2026.09.30 \| 844 \| 下載 \|"
- `https://www.merit-times.com/news/529639` -> **live_dated** (page date 2026-09-23); points raw/verified 15/0
- dropped by code checks: 22 (scale word '億' not supported by quote or table header: 2; period_end missing or unparseable: 5; period year 2025 does not appear in the page text or URL (likely mis-dated): 15)

### d4 [base_rates] price and volume decomposition

Hypothesis: Nominal turnover growth = real volume growth + menu price inflation; CPI for restaurant meals (外食費) gives the price component, so a CPI-based deflator plus a modest real-volume assumption constrains nominal growth.

Queries issued by the searcher: 主計總處 外食費 物價指數 2026年9月 年增率; Taiwan CPI food away from home September 2026 year-on-year; 經濟部統計處 餐飲業營業額 2026年9月 年增率; 餐飲業營業額 2026年8月 批發零售餐飲 統計 經濟部

- `http://dev.taisounds.news/news/content/76/292728` -> **live_dated** (page date 2026-10-07); points raw/verified 14/13
  - p68 Taiwan CPI year-on-year growth rate, September 2026 = **2.73** % (2026-09-01..2026-09-30) [keep: ] quote: "主計總處今(10/7)日公布9月消費者物價指數(CPI)年增率為2.73%"
  - p69 Taiwan CPI month-on-month growth rate, September 2026 = **0.68** % (2026-09-01..2026-09-30) [DISCARD: September CPI MoM is not needed for a YoY nominal-growth route.] quote: "9月CPI月增0.68%,年增率則升至2.73%"
  - p70 Consecutive months Taiwan CPI YoY above 2% threshold, as of September 2026 = **5** months (2026-09-01..2026-09-30) [DISCARD: CPI streak count is background only.] quote: "不僅連續5個月高於2%的通膨警戒線"
  - p71 Consecutive months food-away-from-home (外食費) YoY growth above 3%, as of Septembe = **4** months (2026-09-01..2026-09-30) [keep: ] quote: "外食費年增率已連續4個月超過3%"
  - p72 Food-away-from-home (外食費) YoY growth threshold exceeded for 4 consecutive months = **3** % (2026-09-01..2026-09-30) [keep: ] quote: "外食費年增率已連續4個月超過3%"
  - p73 Vegetable price change, September 2026 (month-on-month) = **4.93** % (2026-09-01..2026-09-30) [DISCARD: Vegetable price MoM change is a CPI detail, not a food-service turnover input.] quote: "蔬菜價格由8月下跌逾2成,轉為9月上漲4.93%"
  - p74 Contribution of vegetable price rise to September 2026 CPI YoY, percentage point = **0.53** percentage points (2026-09-01..2026-09-30) [DISCARD: Vegetable contribution to CPI is a CPI detail.] quote: "單項就推升CPI年增率約0.53個百分點"
  - p75 Vegetable price decline, August 2026 (month-on-month, stated as over 20%) = **2** percent (2026-08-01..2026-08-31) [DISCARD: August vegetable price decline is a CPI detail.] quote: "蔬菜價格由8月下跌逾2成"
  - p76 Average vegetable wholesale price, first 7 trading days of October 2026 = **34.7** TWD per kg (2026-10-01..2026-10-07) [DISCARD: October vegetable wholesale price is a CPI detail.] quote: "10月前7個交易日平均價格為每公斤34.7元"
  - p77 Education equipment and supplies price YoY growth, September 2026 = **9.75** % (2026-09-01..2026-09-30) [DISCARD: Education equipment price growth is irrelevant to food service.] quote: "教養設備及用具價格也明顯上漲,9月年增9.75%"
  - p78 Consecutive months education equipment and supplies prices rising, as of Septemb = **10** months (2026-09-01..2026-09-30) [DISCARD: Education equipment price streak is irrelevant to food service.] quote: "已連續10個月走揚"
  - p79 Years since statistics began for education equipment price series (record high), = **44** years (2026-09-01..2026-09-30) [DISCARD: Education equipment record is irrelevant to food service.] quote: "年增率更創下有統計以來44年新高"
  - p80 CPI weight of computers, other computer equipment and software items = **1.6** % (..) [DISCARD: CPI weight of computer items is irrelevant to food service.] quote: "相關項目占CPI權重約1.6%"
- `https://www.merit-times.com/news/529639` -> **live_dated** (page date 2026-09-23); points raw/verified 15/0
- `https://www.ceicdata.com/en/taiwan/consumer-price-index-2021100` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=28868bf8b0af484fa396b27f4cae772f` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 16 (period_end 2026-10-31 after as_of: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 15)

### d5 [forecasts_markets] official forecasts and nowcasts

Hypothesis: MOEA or research institutes publish nowcasts/forecasts of retail and food-service turnover growth; these can anchor the September 2026 YoY growth assumption.

Queries issued by the searcher: 經濟部 餐飲業 營業額 預測 2026 第三季; 餐飲業 營業額 年增率 預估 2026 經濟部統計處; 經濟部統計處 115年8月 批發零售餐飲 營業額 9月 854 879億元 年增 第三季 2,691; 中華經濟研究院 2026 第三季 預測 餐飲 零售 年增率 內需

- `https://mnscdn.moea.gov.tw/MNS/dos/bulletin/Bulletin.aspx?kind=8&html=1&menu_id=6727&bull_id=16913` -> **live_dated** (page date 2012-12-14); points raw/verified 14/14
  - p81 Taiwan food and beverage services industry (餐飲業) monthly turnover, August 2026 = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service level.] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p82 Taiwan food and beverage services industry (餐飲業) turnover year-on-year growth, A = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service growth.] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p83 Taiwan restaurants (餐館) turnover year-on-year growth, August 2026 = **0.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August restaurant growth.] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
  - p84 Taiwan beverage shops (飲料店) turnover year-on-year growth, August 2026 = **7.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August beverage-shop growth.] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
  - p85 Taiwan catering and group meal contractors (外燴及團膳承包業) turnover year-on-year grow = **11** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August catering/contract growth.] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11.0%"
  - p86 Taiwan food and beverage services industry (餐飲業) cumulative turnover, January-Au = **737,200,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative.] quote: "綜計1至8月營業額為7,372億元,年增3.7%"
  - p87 Taiwan food and beverage services industry (餐飲業) cumulative turnover year-on-yea = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative growth.] quote: "綜計1至8月營業額為7,372億元,年增3.7%"
  - p88 Taiwan retail trade (零售業) monthly turnover, August 2026 = **416,800,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail level.] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p89 Taiwan retail trade (零售業) turnover year-on-year growth, August 2026 = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August retail growth.] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p90 Taiwan food, beverage and tobacco retail (食品、飲料及菸草零售業) turnover year-on-year gro = **13.1** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food/beverage/tobacco retail growth.] quote: "食品、飲料及菸草零售業年增13.1%"
  - p91 Taiwan wholesale trade (批發業) monthly turnover, August 2026 = **1,850,100,000,000** as written "1兆8,501億元", value check pending TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale level.] quote: "8月批發業營業額為1兆8,501億元,年增65.4%"
  - p92 Taiwan wholesale trade (批發業) turnover year-on-year growth, August 2026 = **65.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August wholesale growth.] quote: "8月批發業營業額為1兆8,501億元,年增65.4%"
  - p93 Taiwan retail trade (零售業) cumulative turnover, January-August 2026 = **3,298,300,000,000** as written "3兆2,983億元", value check pending TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug retail cumulative.] quote: "綜計1至8月營業額為3兆2,983億元,年增4.9%"
  - p94 Taiwan wholesale trade (批發業) cumulative turnover, January-August 2026 = **12,642,400,000,000** as written "12兆6,424億元", value check pending TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug wholesale cumulative.] quote: "綜計1至8月營業額為12兆6,424億元,年增39.8%"
- `https://pchome.megatime.com.tw/news/cat8/20260923/17901614405403618003.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://www.tcfa.org.tw/announce_detail.asp?id=9213972` -> **live_dated** (page date 2026-08-25); points raw/verified 15/15
  - p95 MOEA forecast range for August 2026 food and beverage services industry turnover = **94,200,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: August 2026 food-service forecast is superseded by the actual (p1); only its error pattern matters, which is captured qu] quote: "餐飲業營業額則可望落在942億元至970億元之間,年增1%至4%。"
  - p96 MOEA forecast range for August 2026 food and beverage services industry turnover = **97,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: August 2026 food-service forecast is superseded by the actual (p1).] quote: "餐飲業營業額則可望落在942億元至970億元之間,年增1%至4%。"
  - p97 MOEA forecast range for August 2026 food and beverage services industry turnover = **1** % (2026-08-01..2026-08-31) [DISCARD: August 2026 food-service forecast growth is superseded by the actual (p3).] quote: "餐飲業營業額則可望落在942億元至970億元之間,年增1%至4%。"
  - p98 MOEA forecast range for August 2026 food and beverage services industry turnover = **4** % (2026-08-01..2026-08-31) [DISCARD: August 2026 food-service forecast growth is superseded by the actual (p3).] quote: "餐飲業營業額則可望落在942億元至970億元之間,年增1%至4%。"
  - p99 July 2026 food and beverage services industry turnover (餐飲業營業額) = **88,700,000,000** TWD (2026-07-01..2026-07-31) [DISCARD: July 2026 level is superseded by the August actual for a September estimate.] quote: "餐飲業7月營業額887億元,年增2.5%,累計前7月營業額6422億元、年增3.9%。"
  - p100 July 2026 food and beverage services industry turnover YoY growth = **2.5** % (2026-07-01..2026-07-31) [DISCARD: July 2026 growth is superseded by August.] quote: "餐飲業7月營業額887億元,年增2.5%,累計前7月營業額6422億元、年增3.9%。"
  - p101 Cumulative Jan-Jul 2026 food and beverage services industry turnover = **642,200,000,000** TWD (2026-01-01..2026-07-31) [DISCARD: Jan–Jul cumulative is superseded by Jan–Aug.] quote: "餐飲業7月營業額887億元,年增2.5%,累計前7月營業額6422億元、年增3.9%。"
  - p102 Cumulative Jan-Jul 2026 food and beverage services industry turnover YoY growth = **3.9** % (2026-01-01..2026-07-31) [DISCARD: Jan–Jul cumulative growth is superseded by Jan–Aug.] quote: "餐飲業7月營業額887億元,年增2.5%,累計前7月營業額6422億元、年增3.9%。"
  - p103 July 2026 restaurants (餐館) turnover YoY growth = **0.8** % (2026-07-01..2026-07-31) [DISCARD: July restaurant growth is superseded by August.] quote: "其中,餐館及飲料店受暑假外食及聚餐需求帶動,分別年增0.8%及9.7%;"
  - p104 July 2026 beverage shops (飲料店) turnover YoY growth = **9.7** % (2026-07-01..2026-07-31) [DISCARD: July beverage-shop growth is superseded by August.] quote: "其中,餐館及飲料店受暑假外食及聚餐需求帶動,分別年增0.8%及9.7%;"
  - p105 July 2026 catering and contract food service (外燴及團膳承包業) turnover YoY growth = **7.7** % (2026-07-01..2026-07-31) [DISCARD: July catering/contract growth is superseded by August.] quote: "外燴及團膳承包業則因跨境旅遊市場需求活絡,帶動空廚餐點銷售成長,年增7.7%。"
  - p106 MOEA forecast range for August 2026 retail trade turnover, lower bound = **411,100,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: August 2026 retail forecast is superseded by the actual (p6).] quote: "零售業營業額預估介於4111億元至4229億元,年增5%至8%;"
  - p107 MOEA forecast range for August 2026 retail trade turnover, upper bound = **422,900,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: August 2026 retail forecast is superseded by the actual (p6).] quote: "零售業營業額預估介於4111億元至4229億元,年增5%至8%;"
  - p108 July 2026 retail trade turnover = **418,300,000,000** TWD (2026-07-01..2026-07-31) [DISCARD: July retail level is superseded by August.] quote: "零售業方面,7月營業額4183億元,年增7.7%,累計前7月達2兆8810億元、年增4.6%。"
  - p109 July 2026 retail trade turnover YoY growth = **7.7** % (2026-07-01..2026-07-31) [DISCARD: July retail growth is superseded by August.] quote: "零售業方面,7月營業額4183億元,年增7.7%,累計前7月達2兆8810億元、年增4.6%。"
- `http://210.17.21.214/KMDJ/News/NewsViewer.aspx?a=790fb33a-3adb-4281-93cd-b724e02de46b` -> **live_dated** (page date 2026-09-23); points raw/verified 14/12
  - p110 MOEA forecast: food and beverage services industry (餐飲業) turnover, September 202 = **87,900,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p111 MOEA forecast: food and beverage services industry (餐飲業) turnover YoY growth, Se = **4.5** (range 3..6) as written "3%~6%", value check pending % (2026-09-01..2026-09-30) [keep: ] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p112 MOEA forecast: food and beverage services industry (餐飲業) turnover, 2026 Q3, uppe = **271,600,000,000** TWD (2026-07-01..2026-09-30) [DISCARD: Q3 forecast upper bound is redundant with the September forecast range.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p113 MOEA forecast: food and beverage services industry (餐飲業) turnover YoY growth, 20 = **2.9** (range 2.4..3.4) as written "2.4%~3.4%", value check pending % (2026-07-01..2026-09-30) [DISCARD: Q3 forecast growth range is redundant with the September forecast range.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p114 Food and beverage services industry (餐飲業) turnover, August 2026 = **95,000,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service level.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p115 Food and beverage services industry (餐飲業) turnover MoM growth, August 2026 = **7** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August MoM growth.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p116 Food and beverage services industry (餐飲業) turnover YoY growth, August 2026 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August food-service growth.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p117 Restaurants (餐館) turnover YoY growth, August 2026 = **0.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August restaurant growth.] quote: "8月營業額分別年增0.3%及7.4%"
  - p118 Beverage shops (飲料店) turnover YoY growth, August 2026 = **7.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August beverage-shop growth.] quote: "8月營業額分別年增0.3%及7.4%"
  - p119 Catering and contract food service (外燴及團膳承包業) turnover YoY growth, August 2026 = **11** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of August catering/contract growth.] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11%"
  - p120 Food and beverage services industry (餐飲業) cumulative turnover, January-August 20 = **737,200,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p121 Food and beverage services industry (餐飲業) cumulative turnover YoY growth, Januar = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of Jan–Aug cumulative growth.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
- dropped by code checks: 2 (scale word '億' not supported by quote or table header: 2)

### d6 [capacity_consumption] chain restaurant operators

Hypothesis: Listed restaurant chains' monthly revenue (公開資訊觀測站) aggregated and scaled to the industry total tracks the official series; chain revenue growth in September 2026 proxies industry growth.

Queries issued by the searcher: 王品 瓦城 2026年9月 營收; 經濟部統計處 餐飲業營業額 2025年9月; 王品 9月營收 2026 年增 前三季; 餐飲股 9月營收 2026年10月 瓦城 八方雲集 漢來美食

- `https://pchome.megatime.com.tw/news/cat8/20261008/17914609711671622009.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20261012000958-260410?chdtv` -> **live_dated** (page date 2026-10-12); points raw/verified 15/15
  - p122 王品 (Wowprime) September 2026 consolidated revenue (self-reported, TWD) = **2,090,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "王品(2727)公布2026年9月自結合併營收20.9億元"
  - p123 王品 September 2026 consolidated revenue month-on-month change = **17.19** % (2026-09-01..2026-09-30) [DISCARD: Wowprime September MoM change is redundant with its level and YoY growth.] quote: "雖月減17.19%、仍年增19.73%"
  - p124 王品 September 2026 consolidated revenue year-on-year growth = **19.73** % (2026-09-01..2026-09-30) [keep: ] quote: "雖月減17.19%、仍年增19.73%,改寫同期新高"
  - p125 王品 Q3 2026 consolidated revenue (TWD) = **6,717,000,000** TWD (2026-07-01..2026-09-30) [DISCARD: Wowprime Q3 revenue is redundant with its September and cumulative figures.] quote: "使第三季合併營收67.17億元,季增6%、年增15.04%"
  - p126 王品 Q3 2026 consolidated revenue year-on-year growth = **15.04** % (2026-07-01..2026-09-30) [DISCARD: Wowprime Q3 growth is redundant.] quote: "季增6%、年增15.04%,改寫歷史新高"
  - p127 王品 first three quarters 2026 cumulative consolidated revenue (TWD) = **19,533,000,000** TWD (2026-01-01..2026-09-30) [DISCARD: Wowprime cumulative revenue is redundant with its September figure for a September estimate.] quote: "前三季合併營收195.33億元、年增13.08%,改寫同期新高"
  - p128 王品 first three quarters 2026 cumulative revenue year-on-year growth = **13.08** % (2026-01-01..2026-09-30) [DISCARD: Wowprime cumulative growth is redundant.] quote: "前三季合併營收195.33億元、年增13.08%"
  - p129 王品 Taiwan business group September 2026 revenue (TWD) = **1,720,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "台灣事業群營收17.2億元,月減14.43%、年增19.85%"
  - p130 王品 Taiwan business group September 2026 revenue year-on-year growth = **19.85** % (2026-09-01..2026-09-30) [keep: ] quote: "月減14.43%、年增19.85%,改寫同期新高"
  - p131 王品 China mainland business group September 2026 revenue (TWD) = **369,000,000** TWD (2026-09-01..2026-09-30) [DISCARD: Wowprime China business group revenue is outside the Taiwan industry scope.] quote: "中國大陸事業群營收3.69億元,月減27.97%、年增19.17%"
  - p132 王品 China mainland business group September 2026 revenue year-on-year growth = **19.17** % (2026-09-01..2026-09-30) [DISCARD: Wowprime China business group growth is outside the Taiwan industry scope.] quote: "月減27.97%、年增19.17%"
  - p133 王品 Mid-Autumn single-day revenue year-on-year growth = **20** % (2026-09-01..2026-09-30) [DISCARD: Wowprime Mid-Autumn single-day growth is a single-chain anecdote; the holiday effect is better handled by the calendar a] quote: "中秋單日營收年增逾20%"
  - p134 王品 revenue over 4-day Mid-Autumn holiday (TWD) = **359,000,000** TWD (2026-09-01..2026-09-30) [DISCARD: Wowprime 4-day holiday revenue is a single-chain anecdote.] quote: "4天連假達3.59億元,總計13家門市營收突破千萬元"
  - p135 王品 total stores across Taiwan and China mainland as of end-September 2026 = **481** stores (2026-09-30..2026-09-30) [DISCARD: Wowprime total store count is not needed.] quote: "截至9月底,兩岸門市總數481家,包括台灣增至373家、中國大陸增至108家"
  - p136 王品 Taiwan store count as of end-September 2026 = **373** stores (2026-09-30..2026-09-30) [DISCARD: Wowprime Taiwan store count is not needed.] quote: "包括台灣增至373家、中國大陸增至108家"
- `http://investtaiwan.org.tw/indNewsPage666cht?lang=cht&search=666` -> **live_dated** (page date 2025-10-23); points raw/verified 15/15
  - p137 Taiwan food and beverage services industry monthly turnover, September 2025 (bas = **83,500,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "餐飲業:9月餐飲業營業額835億元,年減0.9%"
  - p138 Taiwan food and beverage services industry year-on-year change, September 2025 = **0.9** % (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p139 Taiwan restaurants (餐館) segment year-on-year change, September 2025 = **3.3** % (2025-09-01..2025-09-30) [keep: ] quote: "其中餐館因逢民俗月及假日天數少於上年同月,婚禮宴席及聚餐需求減緩,年減3.3%"
  - p140 Taiwan beverage shops (飲料店) segment year-on-year change, September 2025 = **10.5** % (2025-09-01..2025-09-30) [keep: ] quote: "飲料店因天熱帶動冰飲品銷售,加以中秋禮盒商機挹注,年增10.5%"
  - p141 Taiwan catering and contract food service (外燴及團膳承包業) segment year-on-year change = **6.7** % (2025-09-01..2025-09-30) [keep: ] quote: "外燴及團膳承包業因航空旅運市場穩定成長,推升機上餐飲需求,年增6.7%"
  - p142 Taiwan food and beverage services industry cumulative turnover, January-Septembe = **794,800,000,000** TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p143 Taiwan food and beverage services industry cumulative year-on-year change, Janua = **2.7** % (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p144 Taiwan wholesale industry monthly turnover, September 2025 = **1,284,200,000,000** as written "1兆2,842億元", value check pending TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月批發業營業額為1兆2,842億元,年增13.9%"
  - p145 Taiwan retail industry monthly turnover, September 2025 = **393,800,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月零售業營業額為3,938億元,年減2.2%"
  - p146 Taiwan retail industry year-on-year change, September 2025 = **2.2** % (2025-09-01..2025-09-30) [keep: ] quote: "9月零售業營業額為3,938億元,年減2.2%"
  - p147 Taiwan food, beverage and tobacco retail (食品、飲料及菸草零售業) year-on-year change, Sept = **3.9** % (2025-09-01..2025-09-30) [keep: ] quote: "食品、飲料及菸草零售業年增3.9%"
  - p148 Taiwan retail industry cumulative turnover, January-September 2025 = **3,539,300,000,000** as written "3兆5,393億元", value check pending TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為3兆5,393億元,年減0.9%"
  - p149 Taiwan wholesale industry cumulative turnover, January-September 2025 = **10,327,500,000,000** as written "10兆3,275億元", value check pending TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為10兆3,275億元,年增7.8%"
  - p150 Taiwan retail industry online sales share of total retail turnover, Q3 2025 = **14.1** % (2025-07-01..2025-09-30) [DISCARD: Online retail share is unrelated to food-service turnover.] quote: "網路銷售額占整體零售業營業額14.1%,較上年同季增加1.2個百分點"
  - p151 Taiwan retail industry online sales, Q3 2025 = **165,400,000,000** TWD (2025-07-01..2025-09-30) [DISCARD: Online retail sales value is unrelated to food-service turnover.] quote: "第3季零售業網路銷售額為1,654億元,年增7.3%"
- `http://210.66.210.14/KMDJ/News/NewsViewer.aspx?a=2a6b3e6d-cb9a-46c5-828a-5999e6cefd94` -> **live_dated** (page date 2026-09-14); points raw/verified 15/15
  - p152 王品 (Wowprime) August 2026 consolidated revenue, cross-strait combined = **2,520,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Wowprime August revenue is superseded by its September figure for a September estimate.] quote: "王品8月表現亮眼,兩岸合併營收25.2億元、年增11.31%"
  - p153 王品 (Wowprime) August 2026 Taiwan business group revenue = **2,010,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Wowprime August Taiwan revenue is superseded.] quote: "其中台灣事業群營收首度突破20億元、達20.1億元,年增8.99%"
  - p154 王品 (Wowprime) August 2026 China business group revenue = **510,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Wowprime China business group August revenue is outside the Taiwan industry scope.] quote: "中國事業群則達5.1億元、年增21.42%"
  - p155 王品 (Wowprime) cumulative Jan-Aug 2026 consolidated revenue = **17,440,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Wowprime Jan–Aug cumulative is superseded.] quote: "累計前8月合併營收174.4億元、年增12.33%"
  - p156 八方雲集 (Bafang Yunji) August 2026 revenue = **820,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Bafang August revenue is superseded by its September figure (not in table) and is only a chain signal.] quote: "八方雲集8月營收8.20億元,月增1.75%、年增9.29%"
  - p157 八方雲集 (Bafang Yunji) cumulative Jan-Aug 2026 revenue = **6,223,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Bafang Jan–Aug cumulative is superseded.] quote: "累計前8月營收62.23億元、年增7.92%"
  - p158 漢來美食 (Hi-Lai Foods) August 2026 revenue = **593,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Hi-Lai August revenue is superseded.] quote: "漢來美食今年展店效益突出,8月營收5.93億元,月增7.62%、年增19.99%"
  - p159 漢來美食 (Hi-Lai Foods) cumulative Jan-Aug 2026 revenue = **4,820,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Hi-Lai Jan–Aug cumulative is superseded.] quote: "累計前8月營收48.20億元、年增17.43%,雙雙刷新歷年同期紀錄"
  - p160 瓦城 (TTFB) August 2026 revenue = **612,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: TTFB August revenue is superseded.] quote: "瓦城8月營收6.12億元、年增2.44%"
  - p161 瓦城 (TTFB) cumulative Jan-Aug 2026 revenue = **4,408,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: TTFB Jan–Aug cumulative is superseded.] quote: "累計前8月營收44.08億元、年增5.96%"
  - p162 乾杯 (Kanpai) August 2026 revenue = **441,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Kanpai August revenue is superseded.] quote: "乾杯8月營收4.41億元、年增6.98%,創今年單月新高"
  - p163 乾杯 (Kanpai) cumulative Jan-Aug 2026 revenue = **3,195,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Kanpai Jan–Aug cumulative is superseded.] quote: "累計前8月營收31.95億元、年增6.36%"
  - p164 亞洲藏壽司 (Kura Sushi Asia) August 2026 revenue = **579,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Kura Sushi August revenue is superseded.] quote: "亞洲藏壽司8月營收5.79億元、年增6.98%,創單月歷史新高"
  - p165 亞洲藏壽司 (Kura Sushi Asia) cumulative Jan-Aug 2026 revenue = **4,075,000,000** TWD (2026-01-01..2026-08-31) [DISCARD: Kura Sushi Jan–Aug cumulative is superseded.] quote: "累計前8月營收40.75億元、年增6.34%"
  - p166 揚秦 (Young Qin) August 2026 revenue = **310,000,000** TWD (2026-08-01..2026-08-31) [DISCARD: Young Qin August revenue is superseded.] quote: "揚秦8月營收3.10億元、年增15.22%"

### d7 [shocks] calendar and event effects

Hypothesis: September 2026 calendar (Mid-Autumn Festival date, typhoon days, number of weekends) shifts dining turnover relative to September 2025; quantify the day-count and holiday effect.

Queries issued by the searcher: 2026 中秋節 日期 9月25日 放假; 2026年 政府行政機關辦公日曆表 中秋節 教師節 連假; 經濟部統計處 餐飲業營業額 114年9月 年增率 中秋節; 2026年9月 颱風 停班停課 台灣 颱風假

- `https://www.yesfund.com.tw/z/zf/zfz/zfzNStk_4F887E2F-15FB-4669-B7CE-922158750C52.djhtm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.sme.gov.tw/volunteer/article-vol-2694-19223` -> **live_dated** (page date 2025-10-27); points raw/verified 11/10
  - p167 Taiwan food and beverage services industry (餐飲業) monthly turnover, September 202 = **83,500,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p168 Taiwan food and beverage services industry turnover year-on-year change, Septemb = **0.9** % (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p169 Taiwan restaurants (餐館) turnover year-on-year change, September 2025, attributed = **3.3** % (2025-09-01..2025-09-30) [keep: ] quote: "其中餐館因逢民俗月及假日天數少於上年同月,婚禮宴席及聚餐需求減緩,年減3.3%"
  - p170 Taiwan beverage shops (飲料店) turnover year-on-year change, September 2025, aided  = **10.5** % (2025-09-01..2025-09-30) [keep: ] quote: "飲料店因天熱帶動冰飲品銷售,加以中秋禮盒商機挹注,年增10.5%"
  - p171 Taiwan catering and group meal contracting (外燴及團膳承包業) turnover year-on-year chan = **6.7** % (2025-09-01..2025-09-30) [keep: ] quote: "外燴及團膳承包業因航空旅運市場穩定成長,推升機上餐飲需求,年增6.7%"
  - p172 Taiwan food and beverage services industry cumulative turnover, January-Septembe = **794,800,000,000** TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p173 Taiwan food and beverage services industry cumulative turnover year-on-year chan = **2.7** % (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p174 Taiwan food, beverage and tobacco retail (食品、飲料及菸草零售業) turnover year-on-year cha = **3.9** % (2025-09-01..2025-09-30) [keep: ] quote: "食品、飲料及菸草零售業年增3.9%"
  - p175 Taiwan wholesale industry turnover, September 2025 = **1,284,200,000,000** as written "1兆2,842億元", value check pending TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月批發業營業額為1兆2,842億元,年增13.9%"
  - p176 Taiwan retail industry turnover, September 2025 = **393,800,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月零售業營業額為3,938億元,年減2.2%"
- `https://wces.chc.edu.tw/index.php/posts/123` -> **live_dated** (page date 2026-09-22); points raw/verified 6/3
  - p177 Mid-Autumn Festival date in 2026 (ROC year 115), day of month = **25** as written "9月25日", value check pending day of month (2026-09-25..2026-09-25) [keep: ] quote: "中秋節(9月25日,星期五)與孔子誕辰紀念日/教師節(9月28日,星期一),併同例假日形成4日連假。"
  - p178 Consecutive holiday length formed by Mid-Autumn Festival and Teachers' Day with  = **4** days (2026-09-25..2026-09-28) [keep: ] quote: "中秋節(9月25日,星期五)與孔子誕辰紀念日/教師節(9月28日,星期一),併同例假日形成4日連假。"
  - p179 Confucius' Birthday/Teachers' Day date in 2026 (ROC year 115), day of month = **28** as written "9月28日", value check pending day of month (2026-09-28..2026-09-28) [keep: ] quote: "中秋節(9月25日,星期五)與孔子誕辰紀念日/教師節(9月28日,星期一),併同例假日形成4日連假。"
- `https://mnscdn.moea.gov.tw/Mns/DOS/Publish/wHandPublish_File.ashx?pub_id=3273` -> **live_dated** (page date 2025-09-23); points raw/verified 15/15
  - p180 Taiwan food and beverage services industry monthly turnover, August 2025 (民國114年 = **93,300,000,000** TWD (2025-08-01..2025-08-31) [DISCARD: August 2025 level is superseded by the August 2026 actual for a September estimate.] quote: "8月餐飲業營業額933億元,較上月增加7.8%"
  - p181 Taiwan food and beverage services industry turnover, September 2024 (民國113年9月),  = **52,700,000,000** TWD (2024-09-01..2024-09-30) [DISCARD: September 2024 food-service turnover of 52.7bn TWD is inconsistent with adjacent September levels (84.3bn in 2023, 83.5b] quote: "9 月 11,271 4.5 5,411 7.5 527 12.9 1,323 -0.1"
  - p182 Taiwan food and beverage services industry turnover, September 2024 year-on-year = **12.9** % (2024-09-01..2024-09-30) [DISCARD: The +12.9% growth attached to the same mis-parsed row cannot be trusted as the food-service total growth.] quote: "9 月 11,271 4.5 5,411 7.5 527 12.9 1,323 -0.1"
  - p183 Taiwan food and beverage services industry turnover, August 2025 year-on-year gr = **4.8** % (2025-08-01..2025-08-31) [DISCARD: August 2025 growth is superseded by August 2026.] quote: "餐飲業營業額年增4.8%"
  - p184 Taiwan food and beverage services industry cumulative turnover January-August 20 = **711,200,000,000** TWD (2025-01-01..2025-08-31) [DISCARD: Jan–Aug 2025 cumulative is superseded by Jan–Aug 2026.] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%"
  - p185 Taiwan food and beverage services industry cumulative January-August 2025 year-o = **3.1** % (2025-01-01..2025-08-31) [DISCARD: Jan–Aug 2025 growth is superseded.] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%"
  - p186 Taiwan food and beverage services industry turnover, full year 2024 (民國113年) = **1,037,800,000,000** TWD (2024-01-01..2024-12-31) [DISCARD: Full-year 2024 level is not needed.] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p187 Taiwan food and beverage services industry turnover, full year 2024 year-on-year = **3.6** % (2024-01-01..2024-12-31) [DISCARD: Full-year 2024 growth is not needed.] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p188 Taiwan food and beverage services industry turnover, September 2023 (民國112年9月) = **84,300,000,000** TWD (2023-09-01..2023-09-30) [keep: ] quote: "9 月 843 3.8 677 3.6 111 0.7 54 13.0"
  - p189 Taiwan food and beverage services industry turnover, September 2023 year-on-year = **3.8** % (2023-09-01..2023-09-30) [keep: ] quote: "9 月 843 3.8 677 3.6 111 0.7 54 13.0"
  - p190 Taiwan food and beverage services industry turnover, August 2024 (民國113年8月) = **89,000,000,000** TWD (2024-08-01..2024-08-31) [DISCARD: August 2024 level is not needed.] quote: "8 月 890 1.8 729 1.6 115 1.6 47 6.5"
  - p191 Taiwan food and beverage services industry turnover, August 2024 year-on-year gr = **1.8** % (2024-08-01..2024-08-31) [DISCARD: August 2024 growth is not needed.] quote: "8 月 890 1.8 729 1.6 115 1.6 47 6.5"
  - p192 Taiwan food and beverage services industry turnover, July 2025 (民國114年7月, revise = **86,600,000,000** TWD (2025-07-01..2025-07-31) [DISCARD: July 2025 level is not needed.] quote: "7 月 r 866 2.1 693 0.5 119 7.4 54 12.9"
  - p193 Taiwan food and beverage services industry turnover, July 2025 year-on-year grow = **2.1** % (2025-07-01..2025-07-31) [DISCARD: July 2025 growth is not needed.] quote: "7 月 r 866 2.1 693 0.5 119 7.4 54 12.9"
  - p194 Taiwan food and beverage services industry turnover, September 2022 (民國111年9月) = **82,700,000,000** TWD (2022-09-01..2022-09-30) [keep: ] quote: "9 月 885 3.3 304 -5.6 250 -2.2 827 0.3"
- dropped by code checks: 4 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; value_as_written not in quote as a whole number: 1; period_end 2026-12-31 after as_of: 2)

### b1 [related_series] card-spend nowcast

Hypothesis: NCCC credit-card food & dining spending for September 2026 (the CSV updated 2026-09-30) would give a high-frequency YoY growth signal for dining; scaled by the historical ratio of MOEA food-service turnover to card dining spend, it would provide an independent check on the MOEA forecast range and on the Wowprime chain signal.

Queries issued by the searcher: NCCC 各職業類別持卡人以信用卡支付食品餐飲類消費之總簽帳金額; 聯合信用卡處理中心 信用卡 簽帳金額 食品餐飲類 統計; nccc.com.tw dataDownload NCCC_TWN_FD.CSV 食品餐飲類 金額 筆數 年月; 經濟部統計處 餐飲業營業額 115年8月 批發零售餐飲 2026

- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/CreditCardData/Jobsconsumption?WCM_PI=1&WCM_Page.aa5a95cd-0b6b-403f-bb0c-ee319cf16024=` -> **live_dated** (page date 2026-10-01); points raw/verified 7/2
  - p195 NCCC food & dining spending CSV update date (all occupations) = **2,026** date (2026-09-30..2026-09-30) [DISCARD: Only a CSV update date; no spending value, so it cannot enter any numeric route.] quote: "\| 各職業類別持卡人以信用卡支付食品餐飲類消費之總簽帳金額及筆數 \| CSV \| 49 KB \| 2026.09.30 \| 844 \| 下載 \|"
  - p196 NCCC Taipei City food & dining spending CSV update date = **2,026** date (2026-09-30..2026-09-30) [DISCARD: Only a CSV update date; no spending value.] quote: "\| 各職業類別持卡人於臺北市以信用卡支付食品餐飲類消費之金額及筆數 \| CSV \| 49 KB \| 2026.09.30 \| 173 \| 下載 \|"
- `https://www.nccc.com.tw/dataDownload/NCCC%20Open%20Data/Industry/NCCC_TWN_FD.CSV` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/NCCCData/Industryconsumption` -> **live_dated** (page date 2026-10-01); points raw/verified 3/0
- `https://open2.idataiwan.com/7015/` -> **live_dated** (page date 2025-12-12); points raw/verified 0/0
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b2 [forecasts_markets] listed-chain September roundup

Hypothesis: A September 2026 listed-restaurant revenue roundup (analogous to the 2026-09-14 August roundup) covering Bafang, Hi-Lai, TTFB, Kanpai, Kura Sushi and Young Qin would let the chain aggregate growth be computed and compared with Wowprime's +19.85%; if the aggregate is much lower, the Wowprime signal overstates industry growth and the MOEA forecast range should be weighted more heavily.

Queries issued by the searcher: 八方雲集 漢來美食 瓦城 乾杯 9月營收 2026; 餐飲股 9月營收 2026 王品 八方雲集 漢來美食 瓦城 乾杯 亞洲藏壽司 揚秦; 揚秦 9月營收 2026 年增 麥味登 第三季 新高; 亞洲藏壽司 9月營收 2026 年增

- `https://pchome.megatime.com.tw/news/cat8/20261008/17914609711671622009.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://tw.stock.yahoo.com/news/%E9%A4%90%E9%A3%B2%E5%86%B7%E7%86%B1%E5%85%A9%E6%A8%A3%E6%83%851-%E7%8E%8B%E5%93%81-%E6%BC%A2%E4%BE%86%E7%87%9F%E6%94%` -> **live_dated** (page date 2026-10-17); points raw/verified 15/15
  - p197 Bafang (八方雲集) September 2026 monthly revenue = **782,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "八方雲集9月營收7.82億元,年增8.36%"
  - p198 Bafang (八方雲集) September 2026 YoY revenue growth = **8.36** % (2026-09-01..2026-09-30) [keep: ] quote: "八方雲集9月營收7.82億元,年增8.36%"
  - p199 Hi-Lai Foods (漢來美食) September 2026 monthly revenue = **644,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "9月營收6.44億元,年增25.77%"
  - p200 Hi-Lai Foods (漢來美食) September 2026 YoY revenue growth = **25.77** % (2026-09-01..2026-09-30) [keep: ] quote: "9月營收6.44億元,年增25.77%"
  - p201 TTFB (瓦城) September 2026 monthly revenue = **497,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "瓦城9月營收4.97億元,年增8.86%"
  - p202 TTFB (瓦城) September 2026 YoY revenue growth = **8.86** % (2026-09-01..2026-09-30) [keep: ] quote: "瓦城9月營收4.97億元,年增8.86%"
  - p203 Kanpai (乾杯) September 2026 monthly revenue = **435,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "乾杯9月營收4.35億元,年增20.97%"
  - p204 Kanpai (乾杯) September 2026 YoY revenue growth = **20.97** % (2026-09-01..2026-09-30) [keep: ] quote: "乾杯9月營收4.35億元,年增20.97%"
  - p205 Wowprime (王品) September 2026 consolidated monthly revenue = **2,090,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "今年9月,王品合併營收20.9億元,年增19.73%"
  - p206 Wowprime (王品) September 2026 consolidated YoY revenue growth = **19.73** % (2026-09-01..2026-09-30) [keep: ] quote: "今年9月,王品合併營收20.9億元,年增19.73%"
  - p207 Wowprime (王品) Taiwan business group September 2026 YoY revenue growth = **19.85** % (2026-09-01..2026-09-30) [keep: ] quote: "其中台灣與中國事業群分別成長19.85%及19.17%"
  - p208 Wowprime (王品) China business group September 2026 YoY revenue growth = **19.17** % (2026-09-01..2026-09-30) [keep: ] quote: "其中台灣與中國事業群分別成長19.85%及19.17%"
  - p209 Jhujian (築間) September 2026 monthly revenue = **305,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "築間9月營收僅3.05億元,年減16.23%"
  - p210 Jhujian (築間) September 2026 YoY revenue growth = **16.23** % (2026-09-01..2026-09-30) [keep: ] quote: "築間9月營收僅3.05億元,年減16.23%"
  - p211 Gourmet-KY (美食-KY) September 2026 monthly revenue = **1,399,000,000** TWD (2026-09-01..2026-09-30) [DISCARD: Gourmet-KY is predominantly China/US bakery-cafe revenue, not a Taiwan food-service proxy; misleading for this target.] quote: "9月營收13.99億元,年減3.49%"
- `https://www.nstock.tw/news/article_c?id=20261009-081708170000` -> **live_dated** (page date 2026-10-09); points raw/verified 15/14
  - p212 Hi-Lai Foods (漢來美食) September revenue = **644,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "漢來美食9月營收6.44億元,月增8.58%、年增25.77%"
  - p213 Hi-Lai Foods (漢來美食) September revenue YoY growth = **25.77** % (2026-09-01..2026-09-30) [keep: ] quote: "漢來美食9月營收6.44億元,月增8.58%、年增25.77%"
  - p214 Hi-Lai Foods (漢來美食) September revenue MoM growth = **8.58** % (2026-09-01..2026-09-30) [keep: ] quote: "漢來美食9月營收6.44億元,月增8.58%、年增25.77%"
  - p215 Hi-Lai Foods (漢來美食) Q3 revenue = **1,789,000,000** TWD (2026-07-01..2026-09-30) [keep: ] quote: "第三季營收17.89億元,季增6.04%、年增22%"
  - p216 Hi-Lai Foods (漢來美食) Q3 revenue YoY growth = **22** % (2026-07-01..2026-09-30) [keep: ] quote: "第三季營收17.89億元,季增6.04%、年增22%"
  - p217 Hi-Lai Foods (漢來美食) first-nine-months revenue = **5,465,000,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "前九月營收54.65億元,年增18.36%"
  - p218 Wowprime (王品) September revenue = **2,090,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "王品9月淡季不淡,單月營收20.9億元,年增19.73%"
  - p219 Wowprime (王品) September revenue YoY growth = **19.73** % (2026-09-01..2026-09-30) [keep: ] quote: "王品9月淡季不淡,單月營收20.9億元,年增19.73%"
  - p220 Wowprime (王品) Q3 revenue = **6,717,000,000** TWD (2026-07-01..2026-09-30) [keep: ] quote: "第三季營收67.17億元,季增6%、年增15.04%"
  - p221 Wowprime (王品) first-nine-months consolidated revenue = **19,534,000,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "前九月合併營收195.34億元、年增13.08%"
  - p222 Bafang Yunji (八方雲集) September revenue = **782,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "八方雲集受惠二大品牌展店效應,9月營收7.82億元、年增8.36%"
  - p223 Bafang Yunji (八方雲集) September revenue YoY growth = **8.36** % (2026-09-01..2026-09-30) [keep: ] quote: "八方雲集受惠二大品牌展店效應,9月營收7.82億元、年增8.36%"
  - p224 Bafang Yunji (八方雲集) Q3 revenue = **2,408,000,000** TWD (2026-07-01..2026-09-30) [keep: ] quote: "第三季營收24.08億元、季增3.21%、年增9.35%"
  - p225 Bafang Yunji (八方雲集) first-nine-months revenue = **7,005,000,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "前九月營收70.05億元、年增7.97%"
- `https://tw.stock.yahoo.com/news/%E5%85%AC%E5%91%8A-%E6%8F%9A%E7%A7%A6-2026%E5%B9%B49%E6%9C%88%E5%90%88%E4%BD%B5%E7%87%9F%E6%94%B63-05%E5%84%84%E5%85%8` -> **live_dated** (page date 2026-10-08); points raw/verified 8/6
  - p226 Young Qin (揚秦) September 2026 consolidated net revenue = **304,645,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "\| 本月 \| 304,645 \|"
  - p227 Young Qin (揚秦) September 2026 YoY revenue growth = **17.26** percent (2026-09-01..2026-09-30) [keep: ] quote: "【公告】揚秦 2026年9月合併營收3.05億元 年增17.26%"
  - p228 Young Qin (揚秦) September 2026 consolidated revenue headline (in 億元) = **305,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "【公告】揚秦 2026年9月合併營收3.05億元 年增17.26%"
  - p229 Young Qin (揚秦) September 2026 YoY revenue change amount = **44,831,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "\| 增減金額 \| 44,831 \|"
  - p230 Young Qin (揚秦) year-to-date 2026 consolidated revenue (Jan-Sep) = **2,632,803,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "\| 本年累計 \| 2,632,803 \|"
  - p231 Young Qin (揚秦) year-to-date 2026 YoY revenue growth = **18.53** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 增減百分比 \| 18.53 \|"
- dropped by code checks: 3 (period_end missing or unparseable: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### b3 [base_rates] calendar/holiday effect

Hypothesis: The 2026 Mid-Autumn + Teachers' Day 4-day holiday (25–28 Sep) versus September 2025's calendar is the main reason MOEA forecasts +3–6% YoY against August's +1.8%; quantifying the historical September holiday effect (e.g. from 2023/2024 when Mid-Autumn fell in September) would tighten the growth assumption and resolve whether the forecast midpoint or the low end is more likely.

Queries issued by the searcher: 經濟部統計處 餐飲業營業額 114年9月 年增率 中秋節; MOEA Department of Statistics September 2025 food and beverage services turnover annual growth; 經濟部統計處 115年8月 批發零售餐飲業營業額 餐飲業 950億元 年增1.8% 9月 預測; 餐飲業營業額 歷年 9月 統計表 億元 107年 108年 110年 111年 112年 113年

- `https://mnscdn.moea.gov.tw/MNS/dos/bulletin/Bulletin.aspx?kind=8&html=1&menu_id=6727&bull_id=16913` -> **live_dated** (page date 2012-12-14); points raw/verified 15/13
  - p232 August 2026 food and beverage services industry turnover (餐飲業營業額), total industr = **95,000,000,000** TWD (2026-08-01..2026-08-31) [keep: ] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p233 August 2026 food and beverage services industry turnover YoY growth rate = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "8月餐飲業營業額950億元,年增1.8%"
  - p234 August 2026 restaurants (餐館) turnover YoY growth rate = **0.3** % (2026-08-01..2026-08-31) [keep: ] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
  - p235 August 2026 beverage stores (飲料店) turnover YoY growth rate = **7.4** % (2026-08-01..2026-08-31) [keep: ] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,分別年增0.3%及7.4%"
  - p236 August 2026 catering and contract food service (外燴及團膳承包業) turnover YoY growth ra = **11** % (2026-08-01..2026-08-31) [keep: ] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11.0%"
  - p237 Cumulative Jan–Aug 2026 food and beverage services industry turnover = **737,200,000,000** TWD (2026-01-01..2026-08-31) [keep: ] quote: "綜計1至8月營業額為7,372億元,年增3.7%"
  - p238 Cumulative Jan–Aug 2026 food and beverage services industry turnover YoY growth  = **3.7** % (2026-01-01..2026-08-31) [keep: ] quote: "綜計1至8月營業額為7,372億元,年增3.7%"
  - p239 August 2026 retail trade turnover, total = **416,800,000,000** TWD (2026-08-01..2026-08-31) [keep: ] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p240 August 2026 retail trade turnover YoY growth rate = **6.5** % (2026-08-01..2026-08-31) [keep: ] quote: "8月零售業營業額為4,168億元,年增6.5%"
  - p241 August 2026 food, beverage and tobacco retail (食品、飲料及菸草零售業) turnover YoY growth  = **13.1** % (2026-08-01..2026-08-31) [keep: ] quote: "致電子購物及郵購業年增8.5%、食品、飲料及菸草零售業年增13.1%"
  - p242 August 2026 supermarkets (超級市場) turnover YoY growth rate = **8.7** % (2026-08-01..2026-08-31) [keep: ] quote: "超級市場年增8.7%、量販店年增9.0%"
  - p243 August 2026 hypermarkets (量販店) turnover YoY growth rate = **9** % (2026-08-01..2026-08-31) [keep: ] quote: "超級市場年增8.7%、量販店年增9.0%"
  - p244 August 2026 department stores (百貨公司) turnover YoY growth rate = **8.4** % (2026-08-01..2026-08-31) [keep: ] quote: "百貨公司年增8.4%、資通訊及家電設備零售業年增10.9%"
- `https://www.sme.gov.tw/volunteer/article-vol-2694-19223` -> **live_dated** (page date 2025-10-27); points raw/verified 7/7
  - p245 Taiwan food and beverage services industry (餐飲業) monthly turnover, September 202 = **83,500,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p246 Taiwan food and beverage services industry turnover YoY change, September 2025 = **0.9** % (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p247 Taiwan restaurants (餐館) turnover YoY change, September 2025 = **3.3** % (2025-09-01..2025-09-30) [keep: ] quote: "其中餐館因逢民俗月及假日天數少於上年同月,婚禮宴席及聚餐需求減緩,年減3.3%"
  - p248 Taiwan beverage shops (飲料店) turnover YoY change, September 2025 = **10.5** % (2025-09-01..2025-09-30) [keep: ] quote: "飲料店因天熱帶動冰飲品銷售,加以中秋禮盒商機挹注,年增10.5%"
  - p249 Taiwan catering and contract food service (外燴及團膳承包業) turnover YoY change, Septem = **6.7** % (2025-09-01..2025-09-30) [keep: ] quote: "外燴及團膳承包業因航空旅運市場穩定成長,推升機上餐飲需求,年增6.7%"
  - p250 Taiwan food and beverage services industry cumulative Jan–Sep 2025 turnover = **794,800,000,000** TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p251 Taiwan food and beverage services industry cumulative Jan–Sep 2025 turnover YoY  = **2.7** % (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
- `https://www.fintechgo.com.tw/Article/59399999709315904` -> **dropped** (live http 404); points raw/verified -/-
- `https://mnscdn.moea.gov.tw/Mns/DOS/Publish/wHandPublish_File.ashx?pub_id=3273` -> **live_dated** (page date 2025-09-23); points raw/verified 15/13
  - p252 Taiwan food and beverage services industry turnover, September 2024 (民國113年9月) = **52,700,000,000** TWD (2024-09-01..2024-09-30) [DISCARD: September 2024 figure of 527億元 is a segment/sub-aggregate, not the total (total Sept 2024 ≈843億元); using it as total his] quote: "9 月 11,271 4.5 5,411 7.5 527 12.9 1,323 -0.1"
  - p253 Taiwan food and beverage services industry YoY growth, September 2024 (民國113年9月) = **12.9** % (2024-09-01..2024-09-30) [DISCARD: Paired with the mis-scoped p252 level; the +12.9% is not the total-industry growth.] quote: "9 月 11,271 4.5 5,411 7.5 527 12.9 1,323 -0.1"
  - p254 Taiwan food and beverage services industry turnover, September 2023 (民國112年9月) = **76,400,000,000** TWD (2023-09-01..2023-09-30) [DISCARD: September 2023 764億元 conflicts with the total 843億元 in p188; segment-level, not total.] quote: "9 月 4,026 3.4 3,262 2.0 1,298 5.6 764 9.7"
  - p255 Taiwan food and beverage services industry YoY growth, September 2023 (民國112年9月) = **9.7** % (2023-09-01..2023-09-30) [DISCARD: Paired with the mis-scoped p254; +9.7% is not the total-industry growth.] quote: "9 月 4,026 3.4 3,262 2.0 1,298 5.6 764 9.7"
  - p256 Taiwan food and beverage services industry annual turnover, 2024 (民國113年) = **1,037,800,000,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p257 Taiwan food and beverage services industry annual turnover, 2023 (民國112年) = **1,001,900,000,000** TWD (2023-01-01..2023-12-31) [keep: ] quote: "112年 10,019 20.4 8,152 21.2 1,286 7.7 582 45.7"
  - p258 Taiwan food and beverage services industry cumulative turnover Jan–Aug 2025 (民國1 = **711,200,000,000** TWD (2025-01-01..2025-08-31) [keep: ] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%。"
  - p259 Taiwan food and beverage services industry cumulative YoY growth Jan–Aug 2025 (民 = **3.1** % (2025-01-01..2025-08-31) [keep: ] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%。"
  - p260 Taiwan food and beverage services industry YoY growth, August 2025 (民國114年8月) = **4.8** % (2025-08-01..2025-08-31) [keep: ] quote: "與上年同月比較:餐飲業營業額年增4.8%"
  - p261 Taiwan food and beverage services industry month-on-month growth, August 2025 (民 = **7.8** % (2025-08-01..2025-08-31) [keep: ] quote: "8月餐飲業營業額933億元,較上月增加7.8%"
  - p262 Restaurant sub-sector turnover, September 2024 (民國113年9月) = **44,300,000,000** TWD (2024-09-01..2024-09-30) [DISCARD: Restaurant sub-sector level, not the total industry; redundant with the total series.] quote: "9 月 262 -0.1 203 2.4 443 -0.6 350 -0.2 148 5.7"
  - p263 Beverage shop sub-sector turnover, September 2024 (民國113年9月) = **14,800,000,000** TWD (2024-09-01..2024-09-30) [DISCARD: Beverage-shop sub-sector level, not the total industry.] quote: "9 月 262 -0.1 203 2.4 443 -0.6 350 -0.2 148 5.7"
  - p264 Catering and contract food service sub-sector turnover, September 2024 (民國113年9月 = **5,400,000,000** TWD (2024-09-01..2024-09-30) [DISCARD: Catering sub-sector level, not the total industry.] quote: "9 月 843 3.8 677 3.6 111 0.7 54 13.0"
- dropped by code checks: 4 (number: value_as_written is only part of a larger CJK number in the quote: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan restaurant revenue', 'taiwan food service turnover', 'moea retail sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p13', 'p45', 'p52', 'p81', 'p114'] All report the same August 2026 MOEA figure (950億元, +1.8% YoY) from the same 2026-09-23 release; they are one measurement, not independent confirmations.
- corroborating: ['p3', 'p17', 'p46', 'p53', 'p82', 'p116'] Same August 2026 YoY growth (+1.8%) repeated across mirrors of the same MOEA release.
- corroborating: ['p4', 'p14', 'p50', 'p86', 'p120'] Same Jan–Aug 2026 cumulative 7,372億元 / +3.7% from one release.
- corroborating: ['p39', 'p40', 'p41', 'p110', 'p111'] MOEA's own September 2026 forecast range 854–879億元, +3% to +6% YoY; a forecast, not an outcome, and shares the MOEA's model with the target series.
- corroborating: ['p42', 'p43', 'p44', 'p112', 'p113'] Q3 2026 forecast 2,691–2,716億元, +2.4% to +3.4%; consistent with the September range and with July (p99) and August (p1) actuals.
- corroborating: ['p137', 'p167'] September 2025 base 835億元, −0.9% YoY, reported identically by two mirrors; this is the denominator for any YoY route.
- corroborating: ['p139', 'p169'] Same September 2025 restaurant segment commentary (ghost-month and fewer holidays) from two mirrors.
- corroborating: ['p140', 'p170'] Same September 2025 beverage-shop commentary (heat, Mid-Autumn gift boxes).
- corroborating: ['p141', 'p171'] Same September 2025 catering/contract commentary (aviation meals).
- corroborating: ['p142', 'p172'] Same Jan–Sep 2025 cumulative 7,948億元 / +2.7%.
- corroborating: ['p145', 'p176'] Same September 2025 retail 3,938億元, −2.2%.
- corroborating: ['p144', 'p175'] Same September 2025 wholesale 1兆2,842億元, +13.9%.
- corroborating: ['p147', 'p174'] Same September 2025 food/beverage/tobacco retail +3.9%.
- corroborating: ['p122', 'p123', 'p124', 'p129', 'p130'] Wowprime September 2026 self-reported revenue and growth; Taiwan business group +19.85% is a single-company signal, not the industry.
- corroborating: ['p152', 'p153', 'p154', 'p155'] Wowprime August 2026 revenue from an earlier release; consistent with the September release's implied August base.
- corroborating: ['p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166'] Listed-chain August 2026 revenues from one 2026-09-14 roundup; a single news source covering several firms, useful as a growth cross-check only.
- corroborating: ['p58', 'p59', 'p68', 'p69'] September 2026 CPI 112.82, +2.73% YoY, +0.68% MoM; two sources but the same DGBAS release.
- corroborating: ['p71', 'p72'] Food-away-from-home inflation above 3% for four consecutive months; gives the price component for a nominal-growth decomposition.
- corroborating: ['p177', 'p178', 'p179'] 2026 Mid-Autumn on 25 Sep (Friday) plus Teachers' Day 28 Sep (Monday) forming a 4-day holiday; the key calendar difference versus September 2025.
- conflicting: ['p181', 'p182'] p181 gives September 2024 food-service turnover as 52,700,000,000 TWD, which is inconsistent with the 2023 value (p188, 84,300,000,000) and the 2025 value (p137, 83,500,000,000); the quoted table row 
- corroborating: ['p180', 'p183'] August 2025 933億元, +4.8% YoY; consistent with the August 2026 base implied by p1/p3.
- corroborating: ['p188', 'p189'] September 2023 843億元, +3.8%; a usable earlier September level for a naive series.
- corroborating: ['p190', 'p191'] August 2024 890億元, +1.8%; context for the August base.
- corroborating: ['p192', 'p193'] July 2025 revised 866億元, +2.1%; context.
- corroborating: ['p186', 'p187'] Full-year 2024 1,037.8億元? (1兆378億元), +3.6%; annual context.
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p37', 'p38'] Full-year 2025 and December 2025 figures from one trade-press summary; consistent with the monthly series but not independent.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36'] January 2026 MOEA forecast ranges; historical forecast-accuracy evidence only, not inputs to September.
- corroborating: ['p95', 'p96', 'p97', 'p98'] MOEA's August 2026 forecast range 942–970億元 (+1% to +4%) versus actual 950億元 (+1.8%); shows the forecaster's typical error and that the actual landed near the low end.
- corroborating: ['p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105'] July 2026 actuals and segment growth from the 2026-08-25 release; establishes the recent run-rate (Jul +2.5%, Aug +1.8%).
- corroborating: ['p106', 'p107', 'p108', 'p109'] July/August 2026 retail figures and forecasts; retail is a related but distinct series.
- corroborating: ['p6', 'p7', 'p11', 'p16', 'p54', 'p55', 'p88', 'p89'] August 2026 retail 4,168億元, +6.5%; one measurement repeated.
- corroborating: ['p8', 'p9', 'p15', 'p56', 'p57', 'p91', 'p92'] August 2026 wholesale 1兆8,501億元, +65.4%; one measurement repeated. The extreme growth reflects an AI/semiconductor base effect and is not transferable to food service.
- corroborating: ['p10', 'p94'] Jan–Aug 2026 wholesale cumulative 12兆6,424億元, +39.8%.
- corroborating: ['p12', 'p93'] Jan–Aug 2026 retail cumulative 3兆2,983億元, +4.9%.
- corroborating: ['p18', 'p19', 'p20', 'p21', 'p90'] August 2026 retail sub-segment growth (food/beverage/tobacco +13.1%, supermarkets +8.7%, hypermarkets +9.0%, department stores +8.4%); retail food sales, not food service.
- corroborating: ['p22', 'p23', 'p47', 'p48', 'p83', 'p84', 'p117', 'p118'] August 2026 segment growth: restaurants +0.3%, beverage shops +7.4%; one release.
- corroborating: ['p49', 'p85', 'p119'] August 2026 catering/contract +11.0%; one release.
- corroborating: ['p58', 'p60', 'p62', 'p63', 'p64', 'p65', 'p66'] Macro context (CPI, PPI, GDP, unemployment, wages) from MOEA/DGBAS pages; background only.
- corroborating: ['p67'] NCCC card CSV updated through 2026-09-30; indicates dining card-spend data exist but the values are not in the table.
- corroborating: ['p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80'] September 2026 CPI detail (vegetables, education equipment, weights); explains CPI but not food-service turnover.
- corroborating: ['p133', 'p134', 'p135', 'p136'] Wowprime Mid-Autumn performance and store count; supports a positive holiday effect but is one chain.
- corroborating: ['p125', 'p126', 'p127', 'p128', 'p131', 'p132'] Wowprime Q3 and cumulative 2026 revenue; context for chain growth.
- corroborating: ['p150', 'p151'] Q3 2025 online retail share and value; retail context, not food service.
- corroborating: ['p184', 'p185'] Jan–Aug 2025 cumulative 7,112億元, +3.1%; base for the 2026 cumulative.
- corroborating: ['p194'] September 2022 82,700,000,000 TWD; earlier September level for a naive series.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p137', 'p167', 'p245'] Three copies of the same MOEA September 2025 figure (835億元, -0.9% YoY) republished by different portals; one underlying measurement, not independent confirmation. Use as the base level.
- corroborating: ['p138', 'p168', 'p246'] Same -0.9% September 2025 YoY change, duplicated across portals; single source.
- corroborating: ['p139', 'p169', 'p247'] Restaurants -3.3% Sept 2025, same MOEA text; explains why Sept 2025 base is soft (ghost month, fewer holidays).
- corroborating: ['p140', 'p170', 'p248'] Beverage shops +10.5% Sept 2025, same source.
- corroborating: ['p141', 'p171', 'p249'] Catering/contract +6.7% Sept 2025, same source.
- corroborating: ['p142', 'p172', 'p250'] Jan-Sep 2025 cumulative 7,948億元 +2.7%, duplicated.
- corroborating: ['p143', 'p173', 'p251'] Same cumulative growth rate, duplicated.
- corroborating: ['p144', 'p175'] Wholesale Sept 2025 1兆2,842億元 +13.9%, duplicated; context only.
- corroborating: ['p145', 'p176'] Retail Sept 2025 3,938億元 -2.2%, duplicated; context only.
- corroborating: ['p146'] Retail -2.2% Sept 2025, consistent with p145/p176.
- corroborating: ['p147', 'p174'] Food/beverage/tobacco retail +3.9% Sept 2025, duplicated; different scope from food service.
- corroborating: ['p110', 'p111'] MOEA September 2026 forecast 854-879億元, +3-6% YoY; the two points are the same forecast (level and growth).
- corroborating: ['p232', 'p233'] August 2026 actual 950億元 +1.8%; the level and growth are the same release.
- corroborating: ['p234', 'p235', 'p236'] August 2026 sub-sector growths from the same release; restaurants only +0.3% while beverage +7.4% and catering +11%.
- corroborating: ['p237', 'p238'] Jan-Aug 2026 cumulative 7,372億元 +3.7%; same release.
- corroborating: ['p239', 'p240', 'p241', 'p242', 'p243', 'p244'] August 2026 retail detail from the same release; retail +6.5% is much stronger than food service +1.8%, so retail is a weak proxy for food service.
- corroborating: ['p122', 'p124', 'p205', 'p206', 'p218', 'p219'] Wowprime September 2026 consolidated 20.9億元 +19.73%, duplicated across outlets; one company's self-reported figure.
- corroborating: ['p129', 'p130', 'p207'] Wowprime Taiwan business group +19.85% (17.2億元); the Taiwan-only growth is the relevant one for the Taiwan industry, but still one chain.
- corroborating: ['p197', 'p198', 'p222', 'p223'] Bafang September 2026 7.82億元 +8.36%, duplicated.
- corroborating: ['p199', 'p200', 'p212', 'p213'] Hi-Lai September 2026 6.44億元 +25.77%, duplicated.
- corroborating: ['p201', 'p202'] TTFB September 2026 4.97億元 +8.86%.
- corroborating: ['p203', 'p204'] Kanpai September 2026 4.35億元 +20.97%.
- corroborating: ['p209', 'p210'] Jhujian September 2026 3.05億元 -16.23%; a decliner, showing chain dispersion.
- corroborating: ['p211'] Gourmet-KY September 2026 13.99億元 -3.49%; largely China/US bakery-cafe exposure, weak Taiwan proxy.
- corroborating: ['p226', 'p227', 'p228', 'p229'] Young Qin September 2026 3.05億元 +17.26%, with change amount 44.831M consistent with the level and rate.
- corroborating: ['p215', 'p216', 'p217'] Hi-Lai Q3 +22% and 9M +18.36%; consistent with its September +25.77%.
- corroborating: ['p220', 'p221'] Wowprime Q3 +15.04% and 9M +13.08%; September +19.73% is above its own trend, so the chain signal is not a clean industry proxy.
- corroborating: ['p224', 'p225'] Bafang Q3 +9.35%, 9M +7.97%; consistent with September +8.36%.
- corroborating: ['p230', 'p231'] Young Qin 9M +18.53%; consistent with September +17.26%.
- corroborating: ['p177', 'p178', 'p179'] Mid-Autumn 25 Sep 2026 (Friday) plus Teachers' Day 28 Sep (Monday) form a 4-day holiday 25-28 Sep; the calendar driver behind the MOEA +3-6% forecast.
- corroborating: ['p188', 'p189'] September 2023 843億元 +3.8% (a year when Mid-Autumn fell in September); analogue for the holiday effect.
- corroborating: ['p194', 'p195'] September 2022 827億元 +0.3%; another September analogue.
- corroborating: ['p252', 'p253'] September 2024 527億元 +12.9% — this is a sub-aggregate/segment figure, not the total (total Sept 2024 was ~843億元), so it must not be used as the total's history.
- corroborating: ['p254', 'p255'] September 2023 764億元 +9.7% — again a segment-level figure inconsistent with the total 843億元 in p188; do not mix with p188.
- corroborating: ['p256', 'p257'] Annual totals 2024 1兆378億元 and 2023 1兆19億元; consistent with p25's 2025 1兆674億元 +2.9%.
- corroborating: ['p258', 'p259'] Jan-Aug 2025 7,112億元 +3.1%; consistent with Jan-Sep 2025 7,948億元.
- corroborating: ['p260', 'p261'] August 2025 933億元 +4.8% MoM +7.8%; consistent with the 2025 base.
- corroborating: ['p262', 'p263', 'p264'] September 2024 sub-sector levels (restaurants 443, beverage 148, catering 54億元) — segment detail, not the total.
- corroborating: ['p68', 'p71', 'p72'] September 2026 CPI +2.73% and food-away-from-home above 3% for 4 consecutive months; the price component of nominal food-service growth.
- corroborating: ['p25'] 2025 full-year 1兆674億元 +2.9%; consistent with the monthly series and useful as a scale check.
- corroborating: ['p195', 'p196'] NCCC card CSV update dates only; no spending values, so they cannot enter a numeric route.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth factor for food-service turnover | 1.045 | 1.02..1.07 | 0.9344..1.168 (widened) | dimensionless | m1 (m1) | Anchored on MOEA's own September 2026 forecast of +3% to +6% (p111), midpoint 4.5%; the 4-day Mid-Autumn/Teachers' Day holiday (p177-p179) and food-away-from-home inflation above 3% (p71, p72) support the midpoint rather than the low end, while August's weak +1.8% (p233) and the soft restaurant sub- | The MOEA forecast is a genuine nowcast of the same total-industry, current-price series and the September calendar effect is as described. | A September 2026 print outside 854-879億元, or evidence that the holiday boost was much weaker than in prior Mid-Autumn-in-September years. |
| a2 | September 2026 food-away-from-home price growth | 3.2 | 2.8..3.8 | 2.8..3.8 | % | unused | Food-away-from-home inflation has exceeded 3% for four consecutive months as of September 2026 (p71, p72); general CPI is +2.73% (p68), so menu prices sit modestly above headline CPI. | Menu-price inflation in September 2026 is close to the recent 3%+ run rate. | A reported 外食費 YoY below 2.5% or above 4% for September 2026. |
| a4 | Chain-to-industry growth transfer factor (chain YoY growth relative to industry YoY growth) | 0.55 | 0.3..0.9 | 0.3..0.9 | dimensionless | m3 (m4), m4 (m5) | Listed chains grew far faster than the industry in September 2026 (Wowprime +19.85% Taiwan, Hi-Lai +25.77%, Kanpai +20.97%, Bafang +8.36%, TTFB +8.86%, Young Qin +17.26%, but Jhujian -16.23%), while the industry grew only ~1.8% in August and is forecast +3-6% in September; chains are expanding store | The listed-chain aggregate is used as a growth proxy and must be damped to the industry's broader, slower-growing base. | Evidence that chain and industry growth moved one-for-one in prior Septembers, or a September 2026 industry print near the chain aggregate. |

Rejected by code:

- a3 September 2026 real volume growth of food service: need 0 < low <= value <= high

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 87,295,084,182 | ['p137'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (need 0 < low <= value <= high) |
| m3 | formula_mc | 92,798,917,819 | ['p137', 'p207'] / ['a4'] | [] |  | 0.33 | equal |  |
| m4 | formula_mc | 88,581,719,436 | ['p137', 'p198', 'p202', 'p223', 'p227'] / ['a4'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **89,528,010,831** TWD, 80% interval [64,985,466,664, 123,339,342,392] TWD, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['moea']; measure stems ['turno', 'twd']; 1 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

Best estimate for Taiwan's food and beverage services industry (餐飲業營業額) turnover in September 2026 is 89,528,010,831 TWD (80% model-based interval 64,985,466,664 to 123,339,342,392 TWD).

Main evidence: the September 2025 base of 83,500,000,000 TWD is scaled by a YoY growth factor anchored on MOEA's own September 2026 forecast (1.045, range 0.9344 to 1.168). Chain data support this: Wowprime Taiwan grew 19.85%, Bafang 8.36%, TTFB 8.86%, Young Qin 17.26 percent, damped by a chain-to-industry transfer factor of 0.55 (0.3 to 0.9).

Observed: the base month and chain growth rates. Assumed: the industry growth factor and the transfer factor. Code weighted the usable methods roughly equally (33%, 33%, 33%); one deflator route was rejected.

Key risk: the MOEA forecast missing the holiday effect, and chain growth not representing the whole industry. Better evidence would be actual September 2026 industry data or a broader chain sample.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth factor for food-service turnover: 1.045 dimensionless, range 0.9344 to 1.168 (range widened by code); used by m1. Overturned by: A September 2026 print outside [n]-[n]億元, or evidence that the holiday boost was much weaker than in prior Mid-Autumn-in-September years.
- a4 Chain-to-industry growth transfer factor (chain YoY growth relative to industry YoY growth): 0.55 dimensionless, range 0.3 to 0.9; used by m3, m4. Overturned by: Evidence that chain and industry growth moved one-for-one in prior Septembers, or a September 2026 industry print near the chain aggregate.

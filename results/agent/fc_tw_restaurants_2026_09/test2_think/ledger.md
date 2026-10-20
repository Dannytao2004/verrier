# Evidence ledger: fc_tw_restaurants_2026_09

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate the turnover of Taiwan's food and beverage services industry (餐飲業營業額, current prices) in September 2026, in New Taiwan dollars (TWD), as it will be first reported in the Ministry of Economic Affairs Department of Statistics' monthly release on wholesale, retail and food services turnover (批發、零售及餐飲業營業額統計).
- as_of: 2026-10-19
- Pinned target: Monthly total turnover (營業額) of Taiwan's food and beverage services industry (餐飲業), current prices, in New Taiwan dollars, for September 2026, as first reported by the Ministry of Economic Affairs Department of Statistics in the monthly wholesale, retail and food services turnover release. Working i | unit New Taiwan dollars (current prices), monthly total | period 2026-09-01..2026-09-30 | publisher Ministry of Economic Affairs, Department of Statistics (經濟部統計處), Taiwan

## Directions and pages

### d1 [own_history] statistical compiler / historical series

Hypothesis: September food-service turnover has a recurring seasonal level and recent year-on-year momentum; prior September values and the latest published 2026 monthly values can anchor the target, with adjustment for calendar and shocks. Assumes no major break in survey coverage or industry classification.

Queries issued by the searcher: 餐飲業營業額 2025年9月 經濟部統計處; 批發零售及餐飲業營業額 2026年8月 餐飲業; 113年9月 餐飲業營業額 年增 統計處 億元; 112年9月 餐飲業營業額 億元 年增率 統計處

- `https://www.moea.gov.tw/MNS/Populace/news/News.aspx?kind=1&news_id=117733` -> **live_dated** (page date 2024-10-23); points raw/verified 10/0
- `https://tw.stock.yahoo.com/news/8%E6%9C%88%E6%89%B9%E7%99%BC%E6%A5%AD%E7%87%9F%E6%A5%AD%E9%A1%8D%E5%89%B5%E9%AB%98-%E9%9B%B6%E5%94%AE-%E9%A4%90%E9%A3%` -> **live_dated** (page date 2026-09-23); points raw/verified 5/5
  - p1 Taiwan food and beverage services industry (餐飲業) monthly turnover, August 2026 = **95,000,000,000** TWD (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%,為連續7個月正成長,並為同期新高"
  - p2 Taiwan food and beverage services industry (餐飲業) month-on-month growth, August 2 = **7** % (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%,為連續7個月正成長,並為同期新高"
  - p3 Taiwan food and beverage services industry (餐飲業) year-on-year growth, August 202 = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%,為連續7個月正成長,並為同期新高"
  - p4 Taiwan food and beverage services industry (餐飲業) cumulative turnover, January-Au = **737,200,000,000** TWD (2026-01-01..2026-08-31) [keep: ] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高。"
  - p5 Taiwan food and beverage services industry (餐飲業) cumulative year-on-year growth, = **3.7** % (2026-01-01..2026-08-31) [keep: ] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高。"
- `https://www.sme.gov.tw/volunteer/article-vol-2694-19223` -> **live_dated** (page date 2025-10-27); points raw/verified 7/7
  - p6 Taiwan food and beverage services industry (餐飲業) monthly turnover, September 202 = **83,500,000,000** TWD (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p7 Taiwan food and beverage services industry turnover year-on-year change, Septemb = **0.9** % (2025-09-01..2025-09-30) [keep: ] quote: "9月餐飲業營業額835億元,年減0.9%"
  - p8 Taiwan food and beverage services industry cumulative turnover, January-Septembe = **794,800,000,000** TWD (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p9 Taiwan food and beverage services industry cumulative turnover year-on-year chan = **2.7** % (2025-01-01..2025-09-30) [keep: ] quote: "綜計1至9月營業額為7,948億元,年增2.7%"
  - p10 Taiwan restaurants (餐館) turnover year-on-year change, September 2025 = **3.3** % (2025-09-01..2025-09-30) [keep: ] quote: "其中餐館因逢民俗月及假日天數少於上年同月,婚禮宴席及聚餐需求減緩,年減3.3%"
  - p11 Taiwan beverage shops (飲料店) turnover year-on-year change, September 2025 = **10.5** % (2025-09-01..2025-09-30) [keep: ] quote: "飲料店因天熱帶動冰飲品銷售,加以中秋禮盒商機挹注,年增10.5%"
  - p12 Taiwan catering and contract food services (外燴及團膳承包業) turnover year-on-year chan = **6.7** % (2025-09-01..2025-09-30) [keep: ] quote: "外燴及團膳承包業因航空旅運市場穩定成長,推升機上餐飲需求,年增6.7%"
- `https://www.moea.gov.tw/mns/populace/news/wHandNews_File.ashx?file_id=126799` -> **live_dated** (page date 2026-07-23); points raw/verified 15/15
  - p13 Taiwan food and beverage services industry (餐飲業) total turnover, annual 2021 (民國 = **6,988** 億元 TWD (2021-01-01..2021-12-31) [keep: ] quote: "110年 6,988 -6.8 5,584 -7.8 1,067 -0.6 337 -8.2"
  - p14 Taiwan food and beverage services industry (餐飲業) total turnover, annual 2022 (民國 = **8,322** 億元 TWD (2022-01-01..2022-12-31) [keep: ] quote: "111年 8,322 19.1 6,729 20.5 1,194 11.9 399 18.4"
  - p15 Taiwan food and beverage services industry (餐飲業) total turnover, annual 2023 (民國 = **10,019** 億元 TWD (2023-01-01..2023-12-31) [keep: ] quote: "112年 10,019 20.4 8,152 21.2 1,286 7.7 582 45.7"
  - p16 Taiwan food and beverage services industry (餐飲業) total turnover, annual 2024 (民國 = **10,378** 億元 TWD (2024-01-01..2024-12-31) [keep: ] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p17 Taiwan food and beverage services industry (餐飲業) total turnover, annual 2025 (民國 = **10,674** 億元 TWD (2025-01-01..2025-12-31) [keep: ] quote: "114年 10,674 2.9 8,533 1.7 1,426 7.1 716 8.6"
  - p18 Taiwan food and beverage services industry (餐飲業) total turnover, September 2025  = **829** 億元 TWD (2025-09-01..2025-09-30) [keep: ] quote: "9 月 829 -1.6 647 -4.4 123 11.2 59 8.1"
  - p19 Taiwan food and beverage services industry (餐飲業) total turnover, September 2025  = **-1.6** % (2025-09-01..2025-09-30) [keep: ] quote: "9 月 829 -1.6 647 -4.4 123 11.2 59 8.1"
  - p20 Taiwan food and beverage services industry (餐飲業) total turnover, January 2026 (民 = **967** 億元 TWD (2026-01-01..2026-01-31) [keep: ] quote: "1 月 967 -8.4 775 -11.4 125 0.1 67 17.6"
  - p21 Taiwan food and beverage services industry (餐飲業) total turnover, February 2026 ( = **1,003** 億元 TWD (2026-02-01..2026-02-28) [keep: ] quote: "2 月 1,003 21.1 835 23.8 120 15.4 48 -3.3"
  - p22 Taiwan food and beverage services industry (餐飲業) total turnover, March 2026 (民國1 = **872** 億元 TWD (2026-03-01..2026-03-31) [keep: ] quote: "3 月 872 1.8 690 0.9 119 4.3 63 7.0"
  - p23 Taiwan food and beverage services industry (餐飲業) total turnover, April 2026 (民國1 = **852** 億元 TWD (2026-04-01..2026-04-30) [keep: ] quote: "4 月 852 4.5 663 4.0 121 5.2 68 8.5"
  - p24 Taiwan food and beverage services industry (餐飲業) total turnover, May 2026 revise = **949** 億元 TWD (2026-05-01..2026-05-31) [keep: ] quote: "5 月 r 949 5.0 752 4.2 131 8.5 67 7.2"
  - p25 Taiwan food and beverage services industry (餐飲業) total turnover, June 2026 preli = **892** 億元 TWD (2026-06-01..2026-06-30) [keep: ] quote: "6 月 p 892 4.6 698 3.4 124 7.7 69 11.7"
  - p26 Taiwan food and beverage services industry (餐飲業) cumulative turnover, January-Ju = **5,535** 億元 TWD (2026-01-01..2026-06-30) [keep: ] quote: "115年 1~6月 5,535 4.2 4,413 3.4 740 6.7 383 8.4"
  - p27 Taiwan food and beverage services industry (餐飲業) cumulative January-June 2026 ye = **4.2** % (2026-01-01..2026-06-30) [keep: ] quote: "115年 1~6月 5,535 4.2 4,413 3.4 740 6.7 383 8.4"
- dropped by code checks: 10 (period year 2026 does not appear in the page text or URL (likely mis-dated): 10)

### d2 [related_series] listed-company operator

Hypothesis: Monthly revenue growth of Taiwan-listed restaurant chains is a timely indicator of the industry's September 2026 year-on-year direction; aggregate chain revenue growth can be transferred to the industry with a coverage/mix adjustment. Assumes chain mix and geographic exposure are representative and that acquisitions/store openings are handled.

Queries issued by the searcher: 王品 2026年9月 營收 年增; 餐飲股 2026年9月 營收 年增; 瓦城 2026年9月 營收 年增 八方雲集 亞洲藏壽司; 美食-KY 2026年9月 營收 年減

- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=70338b70709d4bcca67ec141f2781654` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://tcfa.org.tw/announce_detail.asp?id=9214306` -> **live_dated** (page date 2026-10-12); points raw/verified 6/6
  - p28 瓦城 September 2026 consolidated revenue (TWD) = **497,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "瓦城10月12日公布9月合併營收4.97億元,年增8.86%"
  - p29 瓦城 September 2026 year-on-year revenue growth = **8.86** % (2026-09-01..2026-09-30) [keep: ] quote: "瓦城10月12日公布9月合併營收4.97億元,年增8.86%"
  - p30 瓦城 Q3 2026 consolidated revenue (TWD) = **1,615,000,000** TWD (2026-07-01..2026-09-30) [keep: ] quote: "第3季營收16.15億元,年增約3.22%,創歷年同期新高"
  - p31 瓦城 Q3 2026 year-on-year revenue growth = **3.22** % (2026-07-01..2026-09-30) [keep: ] quote: "第3季營收16.15億元,年增約3.22%,創歷年同期新高"
  - p32 瓦城 cumulative first-nine-months 2026 consolidated revenue (TWD) = **4,905,000,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "累計前九月營收49.05億元,年增6.24%,亦創同期新高"
  - p33 瓦城 cumulative first-nine-months 2026 year-on-year revenue growth = **6.24** % (2026-01-01..2026-09-30) [keep: ] quote: "累計前九月營收49.05億元,年增6.24%,亦創同期新高"
- `https://rwdnews.sanlih.com.tw/news/1921337` -> **live_dated** (page date 2026-10-13); points raw/verified 14/8
  - p34 乾杯 (1269) September 2026 consolidated revenue (self-reported) = **435,000,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "乾杯公告2026年9月自結合併營收達4.35億元,較去年同期大增20.97%"
  - p35 乾杯 September 2026 consolidated revenue year-on-year growth = **20.97** % (2026-09-01..2026-09-30) [keep: ] quote: "較去年同期大增20.97%,刷新歷年同期新高紀錄"
  - p36 乾杯 cumulative January-September 2026 revenue = **3,630,000,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "累計今年1至9月營收達36.3億元,年增7.92%"
  - p37 乾杯 cumulative January-September 2026 revenue year-on-year growth = **7.92** % (2026-01-01..2026-09-30) [keep: ] quote: "累計今年1至9月營收達36.3億元,年增7.92%,也寫下同期次高紀錄"
  - p38 乾杯 Mid-Autumn Festival day 2026 revenue year-on-year growth = **8** % (2026-09-01..2026-09-30) [keep: ] quote: "中秋節當日營收較去年中秋節成長8%"
  - p39 乾杯 Taiwan restaurant business September 2026 revenue year-on-year growth (over) = **3** 成 (tenths, i.e. 30 percent) (2026-09-01..2026-09-30) [keep: ] quote: "推升台灣餐飲9月整體營收年增超過3成"
  - p40 乾杯 external sales (外販) business September 2026 revenue year-on-year growth (over = **2** 成 (tenths, i.e. 20 percent) (2026-09-01..2026-09-30) [keep: ] quote: "推動9月外販營收年增逾2成"
  - p41 乾杯 Mid-Autumn barbecue gift box sales (over) = **1,000** as written "破千盒", value check pending boxes (2026-09-01..2026-09-30) [keep: ] quote: "加上中秋燒肉禮盒熱銷破千盒"
- `https://tw.stock.yahoo.com/news/%E5%85%AC%E5%91%8A-%E7%8E%8B%E5%93%81-2026%E5%B9%B49%E6%9C%88%E5%90%88%E4%BD%B5%E7%87%9F%E6%94%B620-9%E5%84%84%E5%85%8` -> **live_dated** (page date 2026-10-08); points raw/verified 10/5
  - p42 王品 (2727) September 2026 consolidated net revenue = **2,090,458,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "\| 本月 \| 2,090,458 \|"
  - p43 王品 (2727) September 2026 year-on-year revenue change amount = **344,445,000** TWD (2026-09-01..2026-09-30) [keep: ] quote: "\| 增減金額 \| 344,445 \|"
  - p44 王品 (2727) September 2026 year-on-year revenue growth percent = **19.73** percent (2026-09-01..2026-09-30) [keep: ] quote: "\| 增減百分比 \| 19.73 \|"
  - p45 王品 (2727) year-to-date 2026 cumulative consolidated net revenue = **19,533,750,000** TWD (2026-01-01..2026-09-30) [keep: ] quote: "\| 本年累計 \| 19,533,750 \|"
  - p46 王品 (2727) year-to-date 2026 cumulative revenue growth percent = **13.08** percent (2026-01-01..2026-09-30) [keep: ] quote: "\| 增減百分比 \| 13.08 \|"
- dropped by code checks: 11 (period_end missing or unparseable: 4; period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; period_end 2026-10-20 after as_of: 3)

### d3 [related_series] annual accounting / seasonal share

Hypothesis: Annual food-service turnover multiplied by the historical September share gives an independent level estimate; if a 2026 annual total or forecast is available, combine it with stable September seasonal shares and adjust for calendar differences. Assumes September share is reasonably stable and any forecast is not simply derived from the same monthly source.

Queries issued by the searcher: 2025 餐飲業營業額 全年 經濟部統計處; 餐飲業營業額 9月 占全年 比重 統計; 2026年 餐飲業 營業額 預測 全年 兆元 成長; 113年9月 餐飲業營業額 843億 經濟部

- `http://www.tcfa.org.tw/announce_detail.asp?id=9212579` -> **live_dated** (page date 2026-01-23); points raw/verified 14/14
  - p47 Taiwan food and beverage services industry (餐飲業) annual turnover, 2025 = **1,067,400,000,000** NTD (2025-01-01..2025-12-31) [keep: ] quote: "餐飲業營業額1兆674億元,年增2.9%"
  - p48 Taiwan food and beverage services industry annual turnover year-on-year growth,  = **2.9** % (2025-01-01..2025-12-31) [keep: ] quote: "餐飲業營業額1兆674億元,年增2.9%"
  - p49 Taiwan food and beverage services industry monthly turnover, December 2025 = **95,000,000,000** NTD (2025-12-01..2025-12-31) [keep: ] quote: "餐飲業為950億元,年減1.1%翻黑"
  - p50 Taiwan food and beverage services industry monthly turnover year-on-year growth, = **1.1** % (2025-12-01..2025-12-31) [keep: ] quote: "餐飲業為950億元,年減1.1%翻黑"
  - p51 Taiwan restaurants (餐館) sub-sector monthly turnover year-on-year growth, Decembe = **2.5** % (2025-12-01..2025-12-31) [keep: ] quote: "其中餐館受農曆年節落點不同影響,企業尾牙及年菜採購商機延後,年減2.5%"
  - p52 Taiwan food and beverage services industry monthly turnover forecast, January 20 = **96,000,000,000** NTD (2026-01-01..2026-01-31) [DISCARD: January 2026 forecast range, superseded by the actual January 2026 value and not informative for September 2026.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p53 Taiwan food and beverage services industry monthly turnover forecast, January 20 = **99,200,000,000** NTD (2026-01-01..2026-01-31) [DISCARD: January 2026 forecast upper bound, superseded by actual data.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p54 Taiwan food and beverage services industry monthly turnover year-on-year growth  = **9.1** % (2026-01-01..2026-01-31) [DISCARD: January 2026 forecast growth lower bound, superseded by actual data.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p55 Taiwan food and beverage services industry monthly turnover year-on-year growth  = **6.1** % (2026-01-01..2026-01-31) [DISCARD: January 2026 forecast growth upper bound, superseded by actual data.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
  - p56 Taiwan retail trade annual turnover, 2025 = **4,844,800,000,000** NTD (2025-01-01..2025-12-31) [DISCARD: Annual retail turnover for 2025, outside the food-service target and not needed for any route.] quote: "2025年零售業營業額為4兆8448億元,年減0.2%翻黑"
  - p57 Taiwan wholesale trade annual turnover, 2025 = **14,071,800,000,000** NTD (2025-01-01..2025-12-31) [DISCARD: Annual wholesale turnover for 2025, outside the food-service target.] quote: "批發業為14兆718億元,年增8.7%"
  - p58 Taiwan wholesale trade monthly turnover, December 2025 = **1,251,400,000,000** NTD (2025-12-01..2025-12-31) [DISCARD: December 2025 wholesale turnover, outside the food-service target.] quote: "批發業營業額1兆2514億元,年增6.6%,連11紅"
  - p59 Taiwan retail trade monthly turnover, December 2025 = **437,900,000,000** NTD (2025-12-01..2025-12-31) [DISCARD: December 2025 retail turnover, outside the food-service target.] quote: "零售業為4379億元,年增0.9%,連3紅"
  - p60 Taiwan food and beverage services industry monthly turnover forecast, January 20 = **97,600,000,000** (range 96,000,000,000..99,200,000,000) as written "960億元至992億元", value check pending NTD (2026-01-01..2026-01-31) [DISCARD: January 2026 forecast midpoint, superseded by actual January 2026 data.] quote: "餐飲業營業額960億元至992億元,年減9.1%至6.1%"
- `https://wantrich.chinatimes.com/news/20251023900503-420501` -> **live_dated** (page date 2025-10-23); points raw/verified 12/9
  - p61 Taiwan food and beverage services industry (餐飲業) monthly turnover, September 202 = **83,500,000,000** New Taiwan dollars (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p6.] quote: "9月餐飲業營業額835億元,年減0.9%。"
  - p62 Taiwan food and beverage services industry (餐飲業) year-on-year change, September  = **0.9** % (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p7.] quote: "9月餐飲業營業額835億元,年減0.9%。"
  - p63 Taiwan food and beverage services industry (餐飲業) quarterly turnover, Q3 2025 (民國 = **263,400,000,000** New Taiwan dollars (2025-07-01..2025-09-30) [keep: ] quote: "第3季餐飲業營業額為2,634億元,季增2.4%,年增2.1%。"
  - p64 Taiwan food and beverage services industry (餐飲業) cumulative Jan-Sep 2025 (前9月) t = **794,800,000,000** New Taiwan dollars (2025-01-01..2025-09-30) [DISCARD: Redundant copy of p8.] quote: "前9月餐飲業營業額為7,948億元,年增2.7%。"
  - p65 Taiwan food and beverage services industry (餐飲業) cumulative Jan-Sep 2025 year-on = **2.7** % (2025-01-01..2025-09-30) [DISCARD: Redundant copy of p9.] quote: "前9月餐飲業營業額為7,948億元,年增2.7%。"
  - p66 Taiwan restaurants (餐館) year-on-year change, September 2025 = **3.3** % (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p10.] quote: "年減3.3%。"
  - p67 Taiwan beverage shops (飲料店) year-on-year change, September 2025 = **10.5** % (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p11.] quote: "年增10.5%。"
  - p68 Number of holiday days in September 2025 (this year), used in restaurant compari = **9** days (2025-09-01..2025-09-30) [keep: ] quote: "假日少於上年同月(今年9天,上年10天)"
  - p69 Taiwan retail industry (零售業) monthly turnover, September 2025, current prices = **393,800,000,000** New Taiwan dollars (2025-09-01..2025-09-30) [DISCARD: September 2025 retail turnover, not the food-service industry.] quote: "9月零售業營業額3,938億元,年減2.2%"
- `https://investtaiwan.nat.gov.tw/getFileWithCount?file=d894d838-e571-4174-9962-01a584f0292a.pdf&Fun=IndNewsAction&lang=cht` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.moea.gov.tw/mns/DOS/bulletin/wHandBulletin_File.ashx?file_id=39102` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 3 (period year 2024 does not appear in the page text or URL (likely mis-dated): 1; number: value_as_written is only part of a larger CJK number in the quote: 2)

### d4 [related_series] payment network / consumer spending

Hypothesis: Credit-card and mobile-payment spending at restaurants tracks food-service turnover; September 2026 card-spending growth can proxy the target's growth after adjusting for card share and cash transactions. Assumes card share is stable and merchant-category coverage is consistent.

Queries issued by the searcher: 聯合信用卡中心 餐飲 簽帳金額 2026年9月; 信用卡 餐飲消費 2026年9月 台灣 簽帳金額; 聯合信用卡中心 食品餐飲類 簽帳金額 億元 2026 統計; 經濟部統計處 2026年8月 餐飲業 營業額 批發零售 餐飲 統計

- `https://pchome.megatime.com.tw/news/cat8/20261015/17920618650124322003.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/CreditCardData/Gender%20X%20Age%20Group/` -> **live_dated** (page date 2026-10-01); points raw/verified 0/0
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=51684fa3bcbd43ec8effdf4f207d0803` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/CreditCardData/Educationconsumption/?WCM_PI=1&WCM_Page.bde3b591-d396-4179-9156-bc84ba6` -> **live_dated** (page date 2026-10-01); points raw/verified 3/0
- dropped by code checks: 3 (period_end missing or unparseable: 3)

### d5 [shocks] calendar and disruption analyst

Hypothesis: Mid-Autumn Festival timing, long weekends, typhoon closures, earthquakes, and weather in September 2026 shift restaurant demand away from or toward a seasonal baseline. A baseline forecast should be adjusted for event exposure; holiday dining can raise turnover while typhoon closures reduce it.

Queries issued by the searcher: 2026年9月 台灣 颱風 停班停課; 2026 中秋節 日期 9月25日 連假; 經濟部統計處 115年8月 批發零售及餐飲業 營業額 餐飲業 年增; 2026年9月 舒力基颱風 台灣 影響 停班停課 9月28日 9月29日

- `https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=127733` -> **live_dated** (page date 2026-09-23); points raw/verified 15/7
  - p70 Taiwan food and beverage services industry (餐飲業) monthly turnover, August 2026 ( = **95,000,000,000** NTD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1/p136.] quote: "8月餐飲業營業額950億元,較上月增加7.0%"
  - p71 Taiwan catering and contract food service (外燴及團膳承包業) year-on-year turnover chang = **11** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p90/p141.] quote: "帶動空廚餐點銷售擴增,年增11.0%"
  - p72 Taiwan food and beverage services industry (餐飲業) cumulative turnover, January-Au = **737,200,000,000** NTD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p4.] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,372億元,年增3.7%"
  - p73 Taiwan food and beverage services industry (餐飲業) cumulative year-on-year turnove = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p5.] quote: "餐飲業營業額為7,372億元,年增3.7%"
  - p74 Taiwan restaurants (餐館) monthly turnover, August 2026 = **76,100,000,000** NTD (2026-08-01..2026-08-31) [keep: ] quote: "餐館 761 9.1 0.3 5 871 2.7 79.6"
  - p75 Taiwan beverage shops (飲料店) monthly turnover, August 2026 = **13,300,000,000** NTD (2026-08-01..2026-08-31) [keep: ] quote: "飲料店 133 1.6 7.4 1 004 7.2 13.6"
  - p76 Taiwan catering and contract food service (外燴及團膳承包業) monthly turnover, August 20 = **5,600,000,000** NTD (2026-08-01..2026-08-31) [keep: ] quote: "外燴及團膳承包業 56 -5.0 11.0 497 8.7 6.7"
- `https://www.mnews.tw/story/mm-20260925edi009` -> **live_dated** (page date 2026-09-25); points raw/verified 4/0
- `https://www.mnews.tw/story/amp/mm-20260923edi001` -> **live_dated** (page date 2026-09-24); points raw/verified 7/5
  - p77 Mid-Autumn and Teachers' Day combined long weekend length (days) starting Friday = **4** days (2026-09-25..2026-09-28) [keep: ] quote: "週五起迎接中秋教師節4天連假"
  - p78 Tropical depression TD29 forecast movement speed toward west-northwest = **20** km per hour (2026-09-23..2026-09-23) [DISCARD: Tropical-depression movement speed is not a quantified food-service demand input.] quote: "熱帶性低氣壓TD29預測今日14時以時速20公里向西北西移動"
  - p79 Forecast time of TD29 position update (local hour) = **14** hour of day (2026-09-23..2026-09-23) [DISCARD: Forecast update hour is not a food-service turnover input.] quote: "熱帶性低氣壓TD29預測今日14時以時速20公里向西北西移動"
  - p80 Friday (25th) date of mostly cloudy to sunny weather and good moon-viewing condi = **25** day of month (2026-09-25..2026-09-25) [DISCARD: One-day weather outlook is not quantified for restaurant demand and is not used numerically.] quote: "週五(25日)地大多為多雲到晴"
  - p81 Article publication date (2026-09-23) = **2,026** date (2026-09-23..2026-09-23) [DISCARD: Article publication date is metadata, not an observed food-service quantity.] quote: "鏡週刊2026.09.23 08:00 臺北時間"
- `https://www.dgpa.gov.tw/typh/daily/nds.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 14 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7; period_end 2026-10-23 after as_of: 1; period_end missing or unparseable: 4; number: more than one number in value_as_written: 2)

### d6 [physical_flow] restaurant operator / POS and reservations

Hypothesis: Restaurant transaction counts, average ticket, and reservation occupancy from POS or booking platforms can approximate September activity; use year-on-year changes in transactions and average check, or level × ticket to build a turnover estimate. Assumes the sample is representative of the broader industry and that reporting coverage is stable.

Queries issued by the searcher: iCHEF 餐飲 景氣 報告 2026年9月; 經濟部統計處 餐飲業 營業額 2026年8月; 2026年9月 餐飲業 營業額 年增 中秋 連假 經濟部 統計; iCHEF 台灣餐飲景氣 白皮書 2026 營業額 年增

- `http://210.17.21.214/KMDJ/News/NewsViewer.aspx?a=790fb33a-3adb-4281-93cd-b724e02de46b` -> **live_dated** (page date 2026-09-23); points raw/verified 15/13
  - p82 Forecast September 2026 Taiwan food and beverage services industry turnover, upp = **87,900,000,000** NTD (2026-09-01..2026-09-30) [keep: ] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p83 Forecast September 2026 Taiwan food and beverage services industry turnover year = **3** % (2026-09-01..2026-09-30) [keep: ] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p84 Forecast September 2026 Taiwan food and beverage services industry turnover year = **6** % (2026-09-01..2026-09-30) [keep: ] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p85 August 2026 Taiwan food and beverage services industry turnover = **95,000,000,000** NTD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p86 August 2026 Taiwan food and beverage services industry turnover month-on-month g = **7** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p2.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p87 August 2026 Taiwan food and beverage services industry turnover year-on-year gro = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p3.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p88 August 2026 Taiwan restaurants turnover year-on-year growth = **0.3** % (2026-08-01..2026-08-31) [keep: ] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,8月營業額分別年增0.3%及7.4%"
  - p89 August 2026 Taiwan beverage shops turnover year-on-year growth = **7.4** % (2026-08-01..2026-08-31) [keep: ] quote: "其中餐館及飲料店受惠暑假及節慶聚餐需求,以及營運規模擴展,8月營業額分別年增0.3%及7.4%"
  - p90 August 2026 Taiwan catering and food service contracting turnover year-on-year g = **11** % (2026-08-01..2026-08-31) [keep: ] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11%"
  - p91 Cumulative January-August 2026 Taiwan food and beverage services industry turnov = **737,200,000,000** NTD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p4.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p92 Cumulative January-August 2026 Taiwan food and beverage services industry turnov = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p5.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p93 Forecast Q3 2026 Taiwan food and beverage services industry turnover, upper boun = **271,600,000,000** NTD (2026-07-01..2026-09-30) [keep: ] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p94 Forecast Q3 2026 Taiwan food and beverage services industry turnover year-on-yea = **2.4** % (2026-07-01..2026-09-30) [keep: ] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
- `https://pchome.megatime.com.tw/news/cat8/20261008/17914609711671622009.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20261014002447-260410?chdtv` -> **live_dated** (page date 2026-10-14); points raw/verified 7/4
  - p95 91APP September consolidated revenue (monthly, NT dollars) = **194,000,000** NT dollars (2026-09-01..2026-09-30) [DISCARD: E-commerce/service revenue unrelated to food-service turnover.] quote: "91APP今年9月合併營收1.94億元,年增30.80%"
  - p96 91APP September consolidated revenue year-on-year growth rate = **30.8** % (2026-09-01..2026-09-30) [DISCARD: E-commerce/service revenue growth unrelated to food-service turnover.] quote: "91APP今年9月合併營收1.94億元,年增30.80%"
  - p97 91APP cumulative first three quarters consolidated revenue (NT dollars) = **1,658,000,000** NT dollars (2026-01-01..2026-09-30) [DISCARD: E-commerce/service cumulative revenue unrelated to food-service turnover.] quote: "累計前三季合併營收16.58億元,年增31.98%"
  - p98 91APP cumulative first three quarters consolidated revenue year-on-year growth r = **31.98** % (2026-01-01..2026-09-30) [DISCARD: E-commerce/service cumulative growth unrelated to food-service turnover.] quote: "累計前三季合併營收16.58億元,年增31.98%"
- `https://www.tcscre.org/post/2026-09-%E4%B8%8A%E5%B8%82%E6%AB%83%E7%87%9F%E6%94%B6-%E9%9B%B6%E5%94%AE%E6%A5%AD-%E9%A4%90%E9%A3%B2%E6%A5%AD-%E7%87%9F%E6` -> **live_dated** (page date 2026-10-14); points raw/verified 3/3
  - p99 Wangpin (王品) cumulative revenue growth for first three quarters, year-on-year = **13.08** % (2026-01-01..2026-09-30) [DISCARD: Redundant copy of p156.] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
  - p100 Hi-Lai Foods (漢來美食) cumulative revenue growth for first three quarters, year-on- = **18.36** % (2026-01-01..2026-09-30) [DISCARD: Redundant copy of p157.] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
  - p101 Xiangbin (饗賓) cumulative revenue growth for first three quarters, year-on-year = **22.63** % (2026-01-01..2026-09-30) [DISCARD: Redundant copy of p158.] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
- dropped by code checks: 5 (scale word '億' not supported by quote or table header: 2; period_end missing or unparseable: 3)

### d7 [administrative] tax administrator / filings

Hypothesis: Business tax receipts or sales-value filings for food-service businesses provide an administrative cross-check on turnover levels and growth, though timing and tax-base differences require bridging. Useful mainly to validate or constrain the historical/listed-company routes.

Queries issued by the searcher: 營業稅 餐飲業 銷售額 2026 財政部; 餐飲業 營業人銷售額 2026 統計; 財政部 統計 營業人銷售額 與稅額 申報 統計 餐飲業 行業別; 營業稅 稅收 2026年8月 財政部 統計 餐飲 住宿

- `https://segis.moi.gov.tw/STATCloud/QueryInterfaceView?COL=lQWaUUlT617sHGrqYev02w%253d%253d&MCOL=1NChUL%252b5tC%252bsRYr%252fngjk%252bg%253d%253d` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.mof.gov.tw/download/pub78972` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.mof.gov.tw/download/8b31494a57964a9484c6e2a7ee550d05` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://service.mof.gov.tw/public/Data/statistic/Year_Fin/110%E9%9B%BB%E5%AD%90%E6%9B%B8/htm/33180.pdf` -> **live_dated** (page date 2022-05-20); points raw/verified 15/15
  - p102 Taiwan accommodation and food service activities business sales, 2021 (year-end/ = **1,514,262,982** NT$ thousand (2021-01-01..2021-12-31) [keep: ] quote: "1,232,398,172 1,284,148,472 1,342,336,598 1,514,262,982"
  - p103 Taiwan accommodation and food service activities business sales, 2020, NT$ thous = **1,342,336,598** NT$ thousand (2020-01-01..2020-12-31) [keep: ] quote: "1,232,398,172 1,284,148,472 1,342,336,598 1,514,262,982"
  - p104 Taiwan accommodation and food service activities business sales, 2019, NT$ thous = **1,284,148,472** NT$ thousand (2019-01-01..2019-12-31) [keep: ] quote: "1,232,398,172 1,284,148,472 1,342,336,598 1,514,262,982"
  - p105 Taiwan accommodation and food service activities business sales, 2018, NT$ thous = **1,232,398,172** NT$ thousand (2018-01-01..2018-12-31) [keep: ] quote: "1,232,398,172 1,284,148,472 1,342,336,598 1,514,262,982"
  - p106 Taiwan accommodation and food service activities business sales, 2017, NT$ thous = **1,122,341,123** NT$ thousand (2017-01-01..2017-12-31) [keep: ] quote: "1,017,032,841 1,026,613,567 1,062,448,097 1,122,341,123"
  - p107 Taiwan accommodation and food service activities business sales, 2016, NT$ thous = **1,062,448,097** NT$ thousand (2016-01-01..2016-12-31) [keep: ] quote: "1,017,032,841 1,026,613,567 1,062,448,097 1,122,341,123"
  - p108 Taiwan accommodation and food service activities business sales, 2015, NT$ thous = **1,026,613,567** NT$ thousand (2015-01-01..2015-12-31) [keep: ] quote: "1,017,032,841 1,026,613,567 1,062,448,097 1,122,341,123"
  - p109 Taiwan accommodation and food service activities business sales, 2014, NT$ thous = **1,017,032,841** NT$ thousand (2014-01-01..2014-12-31) [keep: ] quote: "1,017,032,841 1,026,613,567 1,062,448,097 1,122,341,123"
  - p110 Taiwan accommodation and food service activities number of business units, end o = **57,209** business units (2021-12-31..2021-12-31) [keep: ] quote: "48,331 50,758 53,885 57,209"
  - p111 Taiwan accommodation and food service activities number of business units, end o = **53,885** business units (2020-12-31..2020-12-31) [keep: ] quote: "48,331 50,758 53,885 57,209"
  - p112 Taiwan accommodation and food service activities number of business units, end o = **50,758** business units (2019-12-31..2019-12-31) [keep: ] quote: "48,331 50,758 53,885 57,209"
  - p113 Taiwan accommodation and food service activities number of business units, end o = **48,331** business units (2018-12-31..2018-12-31) [keep: ] quote: "48,331 50,758 53,885 57,209"
  - p114 Taiwan accommodation and food service activities number of business units, end o = **44,811** business units (2017-12-31..2017-12-31) [keep: ] quote: "36,726 39,028 42,288 44,811"
  - p115 Taiwan accommodation and food service activities number of business units, end o = **42,288** business units (2016-12-31..2016-12-31) [keep: ] quote: "36,726 39,028 42,288 44,811"
  - p116 Taiwan accommodation and food service activities number of business units, end o = **39,028** business units (2015-12-31..2015-12-31) [keep: ] quote: "36,726 39,028 42,288 44,811"

### d8 [forecasts_markets] forecaster / official outlook

Hypothesis: Published 2026 forecasts for Taiwan food-service turnover, private consumption, or retail sales can anchor annual growth and, combined with seasonal shares, constrain the September estimate. Distinguish forecasts from realised monthly outcomes and avoid circular sources based only on the same MOEA release.

Queries issued by the searcher: 2026 台灣 餐飲業 營業額 預測 經濟部統計處; 2026 餐飲業 景氣 展望 台灣 全年 預測 成長; 2025年9月 餐飲業營業額 億元 年增 經濟部統計處; 8月餐飲業營業額 年增1.8% 預估9月 餐飲業 營業額 區間 年增 2026

- `https://www.anntw.com/articles/20260616-0LTS` -> **live_dated** (page date 2026-06-16); points raw/verified 11/1
  - p117 Taiwan private consumption share of GDP, 2025 (TIER/台綜院 statement) = **43.3** % (2025-01-01..2025-12-31) [keep: ] quote: "民間消費從2000年代的55.6%高點下降到2025年的43.3%"
- `https://www.moea.gov.tw/MNS/POPULACE/news/News.aspx?kind=1&menu_id=40&news_id=124073` -> **live_dated** (page date 2009-09-09); points raw/verified 8/4
  - p118 Taiwan export orders year-on-year growth in August (percent) = **71.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p154; export orders are outside the food-service target.] quote: "帶動我國8月外銷訂單、製造業生產分別年增71.4%及24.6%"
  - p119 Taiwan manufacturing production year-on-year growth in August (percent) = **24.6** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p155; manufacturing production is outside the food-service target.] quote: "帶動我國8月外銷訂單、製造業生產分別年增71.4%及24.6%"
  - p120 Taiwan retail trade turnover year-on-year growth in August (percent) = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p153; retail trade is outside the food-service target.] quote: "民間消費方面,零售業8月營業額年增6.5%"
  - p121 Taiwan food and beverage services turnover year-on-year growth in August (percen = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p152/p3.] quote: "餐飲業8月營業額年增1.8%"
- `https://ocacnews.net/article/411423?cid=13` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://mnscdn.moea.gov.tw/Mns/DOS/Publish/wHandPublish_File.ashx?pub_id=3273` -> **live_dated** (page date 2025-09-23); points raw/verified 15/11
  - p122 Taiwan food and beverage services industry turnover, August 2025, year-on-year g = **4.8** % (2025-08-01..2025-08-31) [keep: ] quote: "與上年同月比較:餐飲業營業額年增4.8%"
  - p123 Taiwan food and beverage services industry turnover, August 2025, month-on-month = **7.8** % (2025-08-01..2025-08-31) [keep: ] quote: "8月餐飲業營業額933億元,較上月增加7.8%"
  - p124 Taiwan food and beverage services industry cumulative turnover, January-August 2 = **711,200,000,000** NTD (2025-01-01..2025-08-31) [keep: ] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%。"
  - p125 Taiwan food and beverage services industry cumulative turnover, January-August 2 = **3.1** % (2025-01-01..2025-08-31) [keep: ] quote: "累計1至8月與上年同期比較:餐飲業營業額為7,112億元,年增3.1%。"
  - p126 Taiwan food and beverage services industry turnover, September 2024 (prior-year  = **84,300,000,000** NTD (2024-09-01..2024-09-30) [keep: ] quote: "9 月 843 3.8 677 3.6 111 0.7 54 13.0"
  - p127 Taiwan food and beverage services industry turnover, September 2024, year-on-yea = **3.8** % (2024-09-01..2024-09-30) [keep: ] quote: "9 月 843 3.8 677 3.6 111 0.7 54 13.0"
  - p128 Taiwan food and beverage services industry turnover, full year 2024 (民國113年), an = **1,037,800,000,000** NTD (2024-01-01..2024-12-31) [keep: ] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p129 Taiwan food and beverage services industry turnover, full year 2024, year-on-yea = **3.6** % (2024-01-01..2024-12-31) [keep: ] quote: "113年 10,378 3.6 8,387 2.9 1,331 3.5 659 13.3"
  - p130 Restaurant sub-sector turnover, August 2025, monthly total = **75,900,000,000** NTD (2025-08-01..2025-08-31) [keep: ] quote: "餐館 759 9.5 4.1 5 718 2.2 80.4"
  - p131 Beverage shop sub-sector turnover, August 2025, monthly total = **12,400,000,000** NTD (2025-08-01..2025-08-31) [keep: ] quote: "飲料店 124 4.1 8.0 936 5.8 13.2"
  - p132 Catering and contract food service sub-sector turnover, August 2025, monthly tot = **5,000,000,000** NTD (2025-08-01..2025-08-31) [keep: ] quote: "外燴及團膳承包業 50 -6.9 7.3 458 9.7 6.4"
- dropped by code checks: 18 (period_end 2026-12-31 after as_of: 13; period year 2009 does not appear in the page text or URL (likely mis-dated): 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4)

### b1 [related_series] High-frequency card spending and POS data can discriminate between the low and high ends of the September 2026 growth forecast.

Hypothesis: If September 2026 credit-card restaurant spending grows near the upper single digits, it would support the higher end of the p82-p84 forecast range and raise the a1/a2 growth factors; weak card growth would pull the estimate toward the 3% end.

Queries issued by the searcher: 聯合信用卡中心 2026年9月 餐飲 刷卡; 2026年9月 餐飲業 營業額 年增 經濟部統計處; 聯合信用卡處理中心 2026 餐飲 刷卡金額 年增; 國泰世華 2026年9月 餐飲 簽帳金額

- `https://www.merit-times.com/news/529639` -> **live_dated** (page date 2026-09-23); points raw/verified 15/0
- `http://210.66.210.14/KMDJ/News/NewsViewer.aspx?a=790fb33a-3adb-4281-93cd-b724e02de46b` -> **live_dated** (page date 2026-09-23); points raw/verified 15/13
  - p133 Forecast September 2026 Taiwan food and beverage services industry (餐飲業) turnove = **87,900,000,000** NTD (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p82.] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p134 Forecast September 2026 Taiwan food and beverage services industry (餐飲業) turnove = **3** % (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p83.] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p135 Forecast September 2026 Taiwan food and beverage services industry (餐飲業) turnove = **6** % (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p84.] quote: "餐飲業9月營業額為854~879億元,年增3%~6%"
  - p136 August 2026 Taiwan food and beverage services industry (餐飲業) turnover = **95,000,000,000** NTD (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p137 August 2026 Taiwan food and beverage services industry (餐飲業) turnover year-on-ye = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p3.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p138 August 2026 Taiwan food and beverage services industry (餐飲業) turnover month-on-m = **7** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p2.] quote: "餐飲業8月營業額為950億元,月增7%、年增1.8%"
  - p139 August 2026 Taiwan restaurants (餐館) turnover year-on-year growth = **0.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p88.] quote: "8月營業額分別年增0.3%及7.4%"
  - p140 August 2026 Taiwan beverage shops (飲料店) turnover year-on-year growth = **7.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p89.] quote: "8月營業額分別年增0.3%及7.4%"
  - p141 August 2026 Taiwan catering and group meal contracting (外燴及團膳承包業) turnover year- = **11** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p90.] quote: "外燴及團膳承包業因暑期跨境旅遊人次攀升,挹注航餐銷售,年增11%"
  - p142 Cumulative January-August 2026 Taiwan food and beverage services industry (餐飲業)  = **737,200,000,000** NTD (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p4.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p143 Cumulative January-August 2026 Taiwan food and beverage services industry (餐飲業)  = **3.7** % (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p5.] quote: "綜計1至8月餐飲業營業額為7,372億元,年增3.7%,創同期新高"
  - p144 Forecast Q3 2026 Taiwan food and beverage services industry (餐飲業) turnover, uppe = **271,600,000,000** NTD (2026-07-01..2026-09-30) [DISCARD: Redundant copy of p93.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
  - p145 Forecast Q3 2026 Taiwan food and beverage services industry (餐飲業) turnover year- = **3.4** % (2026-07-01..2026-09-30) [DISCARD: Redundant copy of p94.] quote: "第三季營業額為2,691~2,716億元,年增2.4%~3.4%"
- `https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzEwL3JlbGZpbGUvNTYyMi80MDUwOS9iNjU1Y2U4OS1hMzUyLTRmMTctYWM2Mi1hYjdkOTk3MzU0MzkucGRm&n=M` -> **live_dated** (page date 2026-10-02); points raw/verified 15/5
  - p146 Taiwan non-manufacturing NMI, September 2026 (diffusion index) = **56.9** % (2026-09-01..2026-09-30) [keep: ] quote: "2026 年 9 月台灣非製造業經理人指數為 56.9%"
  - p147 Accommodation & food services supplier deliveries diffusion index, September 202 = **57.7** % (2026-09-01..2026-09-30) [keep: ] quote: "住 宿 餐 飲 業 ( 57.7% ) 、 運 輸 倉 儲 業"
  - p148 Accommodation & food services purchase prices (operating costs) diffusion index, = **73.1** % (2026-09-01..2026-09-30) [keep: ] quote: "住 宿 餐 飲 業 ( 73.1% ) 、 批 發 業 ( 72.1% )"
  - p149 Accommodation & food services inventory sentiment diffusion index, September 202 = **57.7** % (2026-09-01..2026-09-30) [keep: ] quote: "各產業依指數高低排序為住宿餐飲業( 57.7%)、批發業"
  - p150 Non-manufacturing NMI survey valid sample size (over) = **250** respondent firms (2026-09-01..2026-09-30) [keep: ] quote: "本報告主要根據超過 250 份(有效樣本)非製造業受訪企業之問卷回答內容作計"
- `https://www.nccc.com.tw/wps/wcm/connect/zh/home/openinformation/NCCCData/Foreigncardconsumption/` -> **live_dated** (page date 2026-10-01); points raw/verified 8/1
  - p151 Update date of the CSV on foreign cardholders' credit-card spending on food and  = **2,026** date (2026-09-30..2026-09-30) [DISCARD: Only an update-date/size line for a foreign-card spending CSV; no spending value or growth is supplied.] quote: "外國持卡人以信用卡支付食品餐飲類消費之金額及筆數 \| CSV \| 4 KB \| 2026.09.30"
- dropped by code checks: 34 (period year 2026 does not appear in the page text or URL (likely mis-dated): 15; scale word '億' not supported by quote or table header: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 10; period_end missing or unparseable: 7)

### b2 [own_history] Stable historical September-to-August sub-sector seasonal factors are the main missing coefficient in the sub-sector build.

Hypothesis: Monthly sub-sector turnover tables for 2023-2025 would let us calibrate restaurant, beverage-shop, and catering September/August ratios directly, improving m4 and resolving whether the 2026 long weekend raises the restaurant factor above its 2025 analogue.

Queries issued by the searcher: 經濟部統計處 餐飲業 餐館 飲料店 外燴 9月 8月 營業額; 批發零售及餐飲業 統計 月報 113年9月 餐館 飲料店 外燴及團膳承包業; "餐飲業營業額變動" 表3 餐館 飲料店 外燴 113年9月 營業額 月增率 年增率; 114年9月 餐飲業 835億元 餐館 飲料店 外燴 營業額 表3 月增率

- `https://service.moea.gov.tw/EE521/visualize/VisDashboard.aspx?d=21` -> **live_dated** (page date 2021-01-01); points raw/verified 8/0
- `https://mnscdn.moea.gov.tw/MNS/dos/content/ContentLink.aspx?menu_id=9425` -> **live_dated** (page date 2026-05-26); points raw/verified 0/0
- `https://accounts.cmoney.tw/forum/article/184920139` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://ocacnews.net/article/382274` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b3 [shocks] Event exposure in September 2026 could shift restaurant demand away from the seasonal baseline and is not yet quantified.

Hypothesis: Evidence on typhoon closures, earthquake disruptions, and Mid-Autumn long-weekend restaurant bookings would quantify the net event adjustment to the seasonal build, especially for the restaurant sub-sector factor a3.

Queries issued by the searcher: 2026年9月 颱風 餐飲 停業 營業額; 2026 中秋 連假 餐廳 訂位 成長; 經濟部統計處 餐飲業 營業額 2026年9月; 2026年9月 颱風 台灣 停班停課 餐飲 業績

- `https://lanpost.net/?p=32723` -> **live_dated** (page date 2026-10-05); points raw/verified 8/4
  - p152 Taiwan food and beverage services (餐飲業) August 2026 turnover year-on-year growth = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p3.] quote: "餐飲業8月營業額年增1.8%,其中餐館及飲料店受惠暑假及節慶聚餐需求"
  - p153 Taiwan retail trade August 2026 turnover year-on-year growth rate = **6.5** % (2026-08-01..2026-08-31) [DISCARD: Retail-trade growth, not food-service turnover; no direct numerical role.] quote: "零售業8月營業額年增6.5%,主因受惠車市逐步回溫、中元普渡及中秋禮盒採買商機"
  - p154 Taiwan export orders August 2026 year-on-year growth rate = **71.4** % (2026-08-01..2026-08-31) [DISCARD: Export orders are outside the food-service target.] quote: "帶動我國8月外銷訂單、製造業生產分別年增71.4%及24.6%"
  - p155 Taiwan manufacturing production August 2026 year-on-year growth rate = **24.6** % (2026-08-01..2026-08-31) [DISCARD: Manufacturing production is outside the food-service target.] quote: "帶動我國8月外銷訂單、製造業生產分別年增71.4%及24.6%"
- `https://www.uanfu.com/news/article/F3D43EF81DBCEFD7FEF627A3427A90F3` -> **live_dated** (page date 2026-09-24); points raw/verified 14/0
- `https://www.tcscre.org/post/2026-09-%E4%B8%8A%E5%B8%82%E6%AB%83%E7%87%9F%E6%94%B6-%E9%9B%B6%E5%94%AE%E6%A5%AD-%E9%A4%90%E9%A3%B2%E6%A5%AD-%E7%87%9F%E6` -> **live_dated** (page date 2026-10-14); points raw/verified 3/3
  - p156 Wangpin (王品) cumulative revenue growth, first three quarters of 2026, year-on-ye = **13.08** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
  - p157 Hilai Food (漢來美食) cumulative revenue growth, first three quarters of 2026, year- = **18.36** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
  - p158 Xiangbin (饗賓) cumulative revenue growth, first three quarters of 2026, year-on-y = **22.63** % (2026-01-01..2026-09-30) [keep: ] quote: "前三季累計分別成長13.08%、18.36%、22.63%"
- `http://210.66.210.14/kmdj/news/newsviewer.aspx?a=5817a151-71a0-42bc-971a-b21b7c391b7c` -> **live_dated** (page date 2026-08-25); points raw/verified 15/14
  - p159 Taiwan food and beverage services industry (餐飲業) monthly turnover, July 2026 = **88,700,000,000** NTD (2026-07-01..2026-07-31) [keep: ] quote: "餐飲業7月營業額887億元,月減0.5%、年增2.5%,亦為同月新高"
  - p160 Taiwan food and beverage services industry (餐飲業) monthly turnover, month-on-mont = **0.5** % (2026-07-01..2026-07-31) [keep: ] quote: "餐飲業7月營業額887億元,月減0.5%、年增2.5%"
  - p161 Taiwan food and beverage services industry (餐飲業) monthly turnover, year-on-year  = **2.5** % (2026-07-01..2026-07-31) [keep: ] quote: "餐飲業7月營業額887億元,月減0.5%、年增2.5%"
  - p162 Taiwan restaurants (餐館) monthly turnover, year-on-year change, July 2026 = **0.8** % (2026-07-01..2026-07-31) [keep: ] quote: "其中餐館及飲料店因受惠暑假外食及聚餐需求擴增,7月營業額分別年增0.8%及9.7%"
  - p163 Taiwan beverage shops (飲料店) monthly turnover, year-on-year change, July 2026 = **9.7** % (2026-07-01..2026-07-31) [keep: ] quote: "其中餐館及飲料店因受惠暑假外食及聚餐需求擴增,7月營業額分別年增0.8%及9.7%"
  - p164 Taiwan catering and contract food service (外燴及團膳承包業) monthly turnover, year-on-y = **7.7** % (2026-07-01..2026-07-31) [keep: ] quote: "外燴及團膳承包業因跨境旅運市場續呈活絡,帶動空廚餐點銷售成長,年增7.7%"
  - p165 Taiwan food and beverage services industry (餐飲業) cumulative turnover, January-Ju = **642,200,000,000** NTD (2026-01-01..2026-07-31) [keep: ] quote: "綜計1至7月餐飲業營業額為6,422億元,年增3.9%,也創同期新高"
  - p166 Taiwan food and beverage services industry (餐飲業) cumulative turnover, year-on-ye = **3.9** % (2026-01-01..2026-07-31) [keep: ] quote: "綜計1至7月餐飲業營業額為6,422億元,年增3.9%,也創同期新高"
  - p167 Taiwan food and beverage services industry (餐飲業) forecast monthly turnover, Augu = **97,000,000,000** NTD (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為942~970億元,年增1%~4%"
  - p168 Taiwan food and beverage services industry (餐飲業) forecast monthly turnover, year = **1** % (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為942~970億元,年增1%~4%"
  - p169 Taiwan food and beverage services industry (餐飲業) forecast monthly turnover, year = **4** % (2026-08-01..2026-08-31) [keep: ] quote: "餐飲業8月營業額為942~970億元,年增1%~4%"
  - p170 Taiwan retail trade (零售業) monthly turnover, July 2026 = **418,300,000,000** NTD (2026-07-01..2026-07-31) [DISCARD: Retail-trade level outside the food-service target.] quote: "零售業7月營業額為4,183億元,月減0.7%、年增7.7%"
  - p171 Taiwan department stores (百貨公司) monthly turnover, year-on-year change, July 2026 = **9.6** % (2026-07-01..2026-07-31) [DISCARD: Department-store growth outside the food-service target.] quote: "致汽機車零售業7月營業額年增12.6%、百貨公司年增9.6%"
  - p172 Taiwan wholesale trade (批發業) monthly turnover, July 2026 = **1,757,300,000,000** NTD (2026-07-01..2026-07-31) [DISCARD: Wholesale-trade level outside the food-service target.] quote: "批發業7月營業額為1兆7,573億元,月增3.1%、年增56.4%"
- dropped by code checks: 19 (period_end 2026-12-31 after as_of: 4; period year 2026 does not appear in the page text or URL (likely mis-dated): 11; number: value_as_written is only part of a larger CJK number in the quote: 3; scale word '億' not supported by quote or table header: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p70', 'p85', 'p2', 'p86', 'p3', 'p87', 'p121'] These are repeated copies of the August 2026 MOEA food-service release: 950億元, +7.0% m/m, +1.8% y/y. Multiple URLs and forecast copies are not independent measurements. p121 is also misdated/duplicati
- corroborating: ['p4', 'p72', 'p91', 'p5', 'p73', 'p92'] Same January-August 2026 cumulative food-service total and growth: 7,372億元, +3.7% y/y. These are redundant vintages/copies of one MOEA release.
- conflicting: ['p6', 'p61', 'p7', 'p62', 'p18', 'p19'] This is a revision/vintage conflict, not independent contradiction: the first September 2025 release reports 835億元 and -0.9% y/y, while the later annual table shows 829億元 and -1.6%. p6 is retained as 
- corroborating: ['p8', 'p64', 'p9', 'p65', 'p124', 'p125'] Initial-vintage January-August/January-September 2025 cumulative values are coherent with p6 and with the MOEA monthly release. p124 is useful for applying the 2025 September-to-January-August ratio t
- corroborating: ['p10', 'p66', 'p11', 'p67', 'p12'] September 2025 initial-release sub-sector growth details: restaurants weak, beverage shops strong, catering/contract food strong. They explain composition behind the total and are not independent of t
- context: ['p126', 'p127', 'p18', 'p19', 'p6', 'p7'] September 2024 and September 2025 show a slowing annual base and a downward revision in the 2025 level. This supports using both first-reported and revised September 2025 bases rather than mixing them
- corroborating: ['p82', 'p83', 'p84', 'p93', 'p94'] MOEA-style published forecasts for September 2026 (854-879億元, +3% to +6%) and Q3 2026 (2,691-2,716億元, +2.4% to +3.4%) are internally consistent. They share one forecasting source, so they are not inde
- corroborating: ['p28', 'p29', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p99', 'p100', 'p101'] Listed restaurant-chain September 2026 revenue growth is positive: 瓦城 +8.86%, 乾杯 +20.97%, 王品 +19.73%, and three chain groups show positive cumulative growth. This supports upside momentum for Septembe
- corroborating: ['p74', 'p75', 'p76', 'p88', 'p89', 'p90'] August 2026 sub-sector levels sum to the August 2026 total, and August sub-sector growth differs by segment: restaurants +0.3%, beverage shops +7.4%, catering/contract food +11%. These are useful for 
- context: ['p77', 'p38', 'p80'] The 2026 Mid-Autumn/Teachers' Day long weekend is a plausible positive restaurant-demand event, and 乾杯 reports Mid-Autumn day revenue up 8%. Weather on one day is not quantified and is not used numeri
- conflicting: ['p118', 'p119', 'p120', 'p121'] These rows carry a 2026-08 period label but a 2009-dated source page and macro growth values that look like the 2009 recovery. They are misdated or unusable as 2026 evidence; p121 also duplicates p3.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p70', 'p136'] Same August 2026 food-service turnover total reported by multiple pages; p70 and p136 are redundant copies of the same MOEA release.
- corroborating: ['p2', 'p138'] Same August 2026 month-on-month growth; p138 is a redundant copy.
- corroborating: ['p3', 'p137', 'p152'] Same August 2026 year-on-year growth; p137 and p152 are redundant copies.
- corroborating: ['p4', 'p72', 'p91', 'p142'] Same January-August 2026 cumulative turnover; multiple copies from the same MOEA release.
- corroborating: ['p5', 'p73', 'p92', 'p143'] Same January-August 2026 cumulative year-on-year growth; redundant copies.
- corroborating: ['p6', 'p61'] Same first-reported September 2025 food-service turnover and growth from the initial release.
- revision: ['p6', 'p7', 'p18', 'p19', 'p61', 'p62'] The initial September 2025 release reported 83.5bn and -0.9% y/y, while the later annual table reports 82.9bn and -1.6%. This is a vintage/revision difference, not an independent contradiction. The fi
- corroborating: ['p8', 'p64'] Same January-September 2025 cumulative turnover and growth.
- corroborating: ['p10', 'p66', 'p11', 'p67', 'p12'] Initial-release September 2025 sub-sector growth rates: restaurant, beverage-shop and catering/contract segments. The later p18 quote shows revised sub-sector growth, again a revision rather than a ne
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33'] Wacheng September/Q3/YTD 2026 revenue and growth are internally consistent company disclosures; they cover only one listed chain and must not be treated as the industry total.
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41'] KANPAI September 2026 revenue, growth and Mid-Autumn details are internally consistent company disclosures; they are chain-specific and require a coverage/mix transfer before any industry use.
- corroborating: ['p42', 'p43', 'p44', 'p45', 'p46'] Wangpin September 2026 revenue, change amount, growth and YTD figures are internally consistent company disclosures; chain-specific, not the industry total.
- context: ['p47', 'p48', 'p49', 'p50', 'p51'] 2025 annual and December 2025 MOEA figures establish the recent annual level and monthly momentum; they are not September 2026 observations.
- corroborating: ['p82', 'p83', 'p84', 'p133', 'p134', 'p135'] Same MOEA-based September 2026 forecast range repeated across pages; p133-p135 are redundant copies. The range is a forecast, not an actual outcome.
- corroborating: ['p88', 'p89', 'p90', 'p139', 'p140', 'p141'] Same August 2026 sub-sector growth rates repeated; p139-p141 are redundant copies.
- corroborating: ['p93', 'p94', 'p144', 'p145'] Same Q3 2026 forecast range and growth; p144-p145 are redundant copies.
- corroborating: ['p99', 'p100', 'p101', 'p156', 'p157', 'p158'] Same listed-chain cumulative growth figures repeated across pages; p99-p101 are redundant copies.
- context: ['p122', 'p123', 'p124', 'p125'] August 2025 food-service level, growth and January-August 2025 cumulative level are useful historical bases; they are not September 2026 observations.
- context: ['p126', 'p127'] September 2024 food-service turnover and growth provide an earlier same-month anchor for a naive series method.
- context: ['p128', 'p129'] 2024 annual food-service turnover and growth are historical context, not a September 2026 outcome.
- context: ['p130', 'p131', 'p132'] August 2025 sub-sector levels provide the denominator for September-to-August seasonal factors, but they are not September 2026 levels.
- corroborating: ['p74', 'p75', 'p76'] August 2026 sub-sector levels sum to the August 2026 total in p1 and provide the current-year base for a September seasonal decomposition.
- context: ['p77', 'p68'] The 2026 Mid-Autumn/Teachers' Day long weekend and the 2025 September holiday-day count are calendar/shock context; they shift restaurant demand relative to a plain seasonal baseline.
- context: ['p146', 'p147', 'p148', 'p149', 'p150'] September 2026 NMI diffusion indices for accommodation and food services indicate operating conditions but are diffusion indices, not turnover levels; use only as qualitative support.
- context: ['p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117'] Business-tax/sales-value administrative data cover accommodation plus food services and end in 2021; they are a different scope and vintage and cannot directly substitute for the MOEA food-service mon

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 year-on-year growth factor applied to first-reported September 2025 food-service turnover | 1.04 | 1.02..1.07 | 0.9344..1.168 (widened) | ratio | m1 (m1) | Uses the MOEA September 2026 forecast range of 3%-6% y/y (p82-p84), recent realized food-service momentum (p3, p5, p159-p161), and stronger listed-chain September growth (p29, p35, p44) as evidence that industry growth is positive but well below the largest chain gains. The 2026 Mid-Autumn/Teachers' | The target is the first-published MOEA September 2026 food-service turnover and p6 is the first-published September 2025 base; no major survey coverage break or severe nationwide typhoon closure occurs. | A MOEA release or credible pre-release nowcast showing September 2026 y/y growth outside roughly 2%-7%, or evidence of a major survey/classification break or severe weather closure. |
| a2 | September 2026 year-on-year growth and vintage-bridge factor applied to revised September 2025 food-service turnover | 1.05 | 1.025..1.078 | 0.9402..1.175 (widened) | ratio | m2 (m2) | p18 is the revised September 2025 level (82.9bn), lower than the first-reported p6 base. To compare with a first-published September 2026 figure, the factor must include both expected 2026 growth and the revision bridge. Evidence for growth is the MOEA forecast range (p82-p84), recent monthly moment | The revised September 2025 level in p18 is the base and the target is the first-published September 2026 total; the revision bridge is stable. | Evidence that the revised September 2025 benchmark is not comparable to the first-release September 2026 benchmark, or actual September 2026 growth far outside the assumed range. |
| a3 | September-to-August seasonal factor for restaurant sub-sector turnover, 2026 | 0.88 | 0.84..0.93 | 0.625..1.25 (widened) | ratio | m4 (m4) | The 2025 revised September and August restaurant sub-sector values (p18 and p130) imply a September level below August. For 2026, the late-September four-day Mid-Autumn/Teachers' Day weekend (p77) supports a modestly higher September-to-August factor than the 2025 analogue, but typhoon/weather risk  | Restaurant sub-sector seasonality in 2026 resembles 2025 and the long weekend provides only a modest lift rather than a major demand shift. | Actual September 2026 restaurant turnover or booking/POS evidence showing a much stronger or weaker September relative to August, or a severe typhoon/earthquake disruption. |
| a4 | September-to-August seasonal factor for beverage-shop turnover, 2026 | 1 | 0.92..1.08 | 0.7048..1.41 (widened) | ratio | m4 (m4) | The 2025 revised September and August beverage-shop values (p18 and p131) imply a September level close to August. September 2026 remains warm and includes Mid-Autumn gift demand, but summer peak demand fades; the factor is centered near one with a wide range. | Beverage-shop demand in September 2026 is broadly similar to the 2025 September-to-August pattern, with no extreme heat or typhoon closure. | Actual September 2026 beverage-shop data or weather/closure evidence showing a materially different September-to-August ratio. |
| a5 | September-to-August seasonal factor for catering and contract food-service turnover, 2026 | 1.18 | 1.08..1.3 | 0.8379..1.676 (widened) | ratio | m4 (m4) | The 2025 revised September and August catering/contract values (p18 and p132) imply September above August, partly reflecting airline catering and contract demand. August 2026 catering/contract turnover was strong (p76, p90), and continued cross-border travel demand supports carrying the 2025 season | Catering/contract food-service demand in September 2026 follows the 2025 September-to-August pattern and airline/cross-border catering remains stable. | A sharp change in airline catering, contract-food demand, or reported September 2026 sub-sector data outside the assumed range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 87,207,296,686 | ['p6'] / ['a1'] | [] |  | 0.20 | median_of_backtested |  |
| m2 | formula_mc | 87,216,244,934 | ['p18'] / ['a2'] | [] |  | 0.20 | median_of_backtested |  |
| m3 | formula_mc | 86,450,958,384 | ['p4', 'p6', 'p124'] / [] | [] |  | 0.20 | median_of_backtested |  |
| m4 | formula_mc | 87,932,050,971 | ['p74', 'p75', 'p76'] / ['a3', 'a4', 'a5'] | [] |  | 0.20 | median_of_backtested |  |
| m5 | series_naive | 83,500,000,000 |  | [2025] | 0.010 | 0.20 | backtest |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: sum over subsector of restaurants, beverage_shops, catering_contract

Result: central **86,447,161,912** TWD, 80% interval [62,749,178,793, 119,094,973,774] TWD, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule inverse_backtest_error, weight on methods that use assumptions 0.60

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms none (no entity constraint); measure stems ['curre', 'dolla', 'price', 'taiwa', 'turno']; 3 point(s) for the target period excluded as dated before the period end or quoted as a forecast
Early checks while the sub-agents were running: 1 (not_confirmed); details in state.json -> published_early.


## Final answer

The best estimate for Taiwan's food and beverage services industry (餐飲業) monthly turnover for September 2026 is 86,447,161,912 TWD (80% model-based interval 62,749,178,793 to 119,094,973,774 TWD).

Evidence: the estimate combines 5 routes. Observed anchors include first-reported September 2025 turnover of 83,500,000,000 TWD, revised September 2025 of 829 億元 TWD, January–August cumulative totals of 737,200,000,000 TWD and 711,200,000,000 NTD, August 2026 sub-sector levels (76,100,000,000 NTD, 13,300,000,000 NTD, 5,600,000,000 NTD), and September 2024 of 84,300,000,000 NTD. Growth and seasonal factors are assumptions: a1=1.04, a2=1.05, a3=0.88, a4=1, a5=1.18.

Weights were set by code (20% each) because backtest years were too few to calibrate; the interval is conditional on these assumptions, not a demonstrated accuracy guarantee.

Main risk: the revision bridge and seasonal factors may not hold. Better evidence would be the actual September 2026 MOEA release and more backtest years.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 year-on-year growth factor applied to first-reported September 2025 food-service turnover: 1.04 ratio, range 0.9344 to 1.168 (range widened by code); used by m1. Overturned by: A MOEA release or credible pre-release nowcast showing September 2026 y/y growth outside roughly [n]-[n], or evidence of a major survey/classification break or severe weather closure.
- a2 September 2026 year-on-year growth and vintage-bridge factor applied to revised September 2025 food-service turnover: 1.05 ratio, range 0.9402 to 1.175 (range widened by code); used by m2. Overturned by: Evidence that the revised September 2025 benchmark is not comparable to the first-release September 2026 benchmark, or actual September 2026 growth far outside the assumed range.
- a3 September-to-August seasonal factor for restaurant sub-sector turnover, 2026: 0.88 ratio, range 0.625 to 1.25 (range widened by code); used by m4. Overturned by: Actual September 2026 restaurant turnover or booking/POS evidence showing a much stronger or weaker September relative to August, or a severe typhoon/earthquake disruption.
- a4 September-to-August seasonal factor for beverage-shop turnover, 2026: 1 ratio, range 0.7048 to 1.41 (range widened by code); used by m4. Overturned by: Actual September 2026 beverage-shop data or weather/closure evidence showing a materially different September-to-August ratio.
- a5 September-to-August seasonal factor for catering and contract food-service turnover, 2026: 1.18 ratio, range 0.8379 to 1.676 (range widened by code); used by m4. Overturned by: A sharp change in airline catering, contract-food demand, or reported September 2026 sub-sector data outside the assumed range.

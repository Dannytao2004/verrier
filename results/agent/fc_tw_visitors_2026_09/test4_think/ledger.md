# Evidence ledger: fc_tw_visitors_2026_09

- Question: Assume today is 2026-10-24. You know nothing published after this date. Estimate the number of visitor arrivals to Taiwan (來臺旅客人次) in September 2026, as it will be first reported in the Ministry of Transportation and Communications' (Tourism Administration) monthly statistics on visitor arrivals and outbound departures (來臺旅客及國人出國人數).
- as_of: 2026-10-24
- Pinned target: Number of visitor arrivals (來臺旅客人次) to Taiwan during September 2026, counted as person-trips in the Tourism Administration, MOTC monthly release 'Visitor Arrivals and Outbound Departures'; the official series counts non-resident visitor border entries under its published definition, not unique indiv | unit visitor arrivals (person-trips) | period 2026-09-01..2026-09-30 | publisher Ministry of Transportation and Communications, Tourism Administration (Taiwan)

## Directions and pages

### d1 [own_history] statistical compiler

Hypothesis: September visitor arrivals follow a seasonal pattern and a recovery/trend level; the official monthly series through August 2026, plus September values in earlier years, gives a direct baseline. Symbolically, September 2026 arrivals ≈ September 2025 × recent year-on-year run-rate × calendar/seasonal adjustment.

Queries issued by the searcher: 來臺旅客人次 2025年9月 觀光署 統計; Tourism Administration Taiwan visitor arrivals September 2025 statistics; 2026年8月 來臺旅客 統計 觀光署 人次; "2026" 來台旅客 1至8月 累計 人次 年增 觀光署

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?pi=30&p=1&q&edate&sdate&c&a=1329` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/11
  - p1 Visitor arrivals to Taiwan, August 2026 (monthly, Tourism Administration) = **662,735** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p2 Year-on-year change in visitor arrivals, August 2026 vs August 2025 = **1.54** % (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p3 Cumulative visitor arrivals to Taiwan, January-August 2026 = **5,564,858** visitor arrivals (person-trips) (2026-01-01..2026-08-31) [keep: ] quote: "1至7月累計來台旅客為4,902,123人次,加上8月月報數字後,1至8月累計為5,564,858人次"
  - p4 Cumulative visitor arrivals to Taiwan, January-July 2026 = **4,902,123** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [keep: ] quote: "1至7月累計來台旅客為4,902,123人次"
  - p5 Cumulative visitor arrivals to Taiwan, January-June 2026 = **4,294,589** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p6 Year-on-year growth in cumulative visitor arrivals, January-June 2026 vs same pe = **2.3** % (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p7 Visitor arrivals to Taiwan, full year 2025 = **8,574,547** visitor arrivals (person-trips) (2025-01-01..2025-12-31) [keep: ] quote: "2019年全年來臺旅客達11,864,105人次;2025年則是8,574,547人次,年增9.12%"
  - p8 Year-on-year growth in visitor arrivals, full year 2025 = **9.12** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年則是8,574,547人次,年增9.12%"
  - p9 Visitor arrivals to Taiwan, full year 2019 (pre-pandemic baseline) = **11,864,105** visitor arrivals (person-trips) (2019-01-01..2019-12-31) [keep: ] quote: "2019年全年來臺旅客達11,864,105人次"
  - p10 2025 visitor arrivals as share of 2019 level (recovery ratio) = **72.3** % (2025-01-01..2025-12-31) [keep: ] quote: "以全年總量換算,2025年約恢復到2019年的72.3%,仍有27.7%的差距"
  - p11 Visitor arrivals to Taiwan, August 2026, by air (share of total) = **93.46** % (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月入境旅客中,空運有619,389人次,占93.46%"
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 4)

### d2 [administrative] border-control agency

Hypothesis: National Immigration Agency entry records for foreign nationals in September 2026 are a timely proxy for Tourism Administration visitor arrivals; after excluding resident entries and transit and adjusting for purpose/visa categories, they should closely track the target.

Queries issued by the searcher: 移民署 2026年9月 入境 外籍旅客 統計; Taiwan immigration statistics September 2026 foreign nationals entries; 觀光署 來臺旅客人次 2026年9月 統計; Tourism Administration Taiwan visitor arrivals September 2025 statistics monthly; 觀光署 2025年9月 來臺旅客 人數 統計 47萬; "來臺旅客" 統計 2026年8月 觀光署 每月 人數

- `https://www.toutiao.com/article/7699024202002596352/?wid=1792579503004` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.tkww.hk/a/202609/28/AP6aba16fce4b0e1e2ee72163e.html` -> **live_dated** (page date 2026-09-28); points raw/verified 0/0
- `https://www.immigration.gov.tw/media/67188/%E5%85%A7%E6%94%BF%E9%83%A8%E7%A7%BB%E6%B0%91%E7%BD%B2107%E5%B9%B4%E5%B9%B4%E5%A0%B1.pdf` -> **live_dated** (page date 2019-09-11); points raw/verified 15/12
  - p12 Total entries and exits at all Taiwan airports and seaports, September 2018 (mon = **4,233,427** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p13 Taoyuan International Airport entries and exits, September 2018 = **3,168,888** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p14 Kaohsiung Airport entries and exits, September 2018 = **416,297** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p15 Songshan Airport entries and exits, September 2018 = **264,350** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p16 Taichung Airport entries and exits, September 2018 = **131,298** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p17 Keelung Seaport entries and exits, September 2018 = **70,085** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p18 Kinmen entries and exits, September 2018 = **143,977** passengers (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 4,233,427 3,168,888 416,297 264,350 131,298 5,294 64 70,085 5,634 2,815 45 239 143,977 4,060 20,381"
  - p19 Mainland Chinese tourist entries to Taiwan (Type I, II, III and independent), Se = **145,090** visitor entries (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 172,237 68,734 103,503 168,308 67,798 100,510 145,090 58,162 86,928 116,502 46,928 69,574"
  - p20 Mainland Chinese independent-traveler entries to Taiwan, September 2018 = **90,400** visitor entries (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 108,283 44,791 63,492 108,399 44,940 63,459 90,400 37,060 53,340 65,601 27,343 38,258"
  - p21 Mainland Chinese professional/business exchange entries to Taiwan, September 201 = **24,415** visitor entries (person-trips) (2018-09-01..2018-09-30) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "9月Sep 13,023 9,087 3,936 12,551 8,679 3,872 24,415 14,181 10,234 15,569 11,000 4,569"
  - p22 Cruise passengers entering Taiwan, full year 2018 = **143,255** passenger entries (person-trips) (2018-01-01..2018-12-31) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "107年搭乘郵輪旅客入境我國者高達 14萬3,255人次"
  - p23 Mainland Chinese Mini Three Links visitors, full year 2018 = **310,676** visitor entries (person-trips) (2018-01-01..2018-12-31) [DISCARD: Outdated 2018 immigration entry/exit data; different scope (all passengers, not visitor arrivals) and not useful for Sep] quote: "Another 310,676 visits were from passengers arriving via the Mini Three Links"
- `https://ua.news/pl/world/na-taivani-kilkist-inozemtsiv-perevishchila-milion-taipei-times` -> **live_dated** (page date 2026-09-21); points raw/verified 0/0
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; value_as_written not in quote as a whole number: 1)

### d3 [physical_flow] airport operator

Hypothesis: International arrival passenger volumes and flight movements at Taiwan's main airports in September 2026 constrain visitor arrivals. After subtracting the resident share and adding sea arrivals, airport international arrivals approximate the official visitor total.

Queries issued by the searcher: 桃園機場 2026年9月 客運量 入境; Taoyuan Airport September 2026 passenger volume international arrivals; 桃園機場 2026年9月 旅運量 統計 萬人次 入境 出境; 2025年9月 來臺旅客 人數 觀光署 統計 入境

- `https://www.taoyuan-airport.com/news/C1CB08AC-9AAA-F111-BC31-0050569094FE?p=1&k=&s=&e=` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- `https://tw.news.yahoo.com/%E6%A1%83%E6%A9%9F%E6%9A%91%E6%9C%9F%E9%81%8B%E9%87%8F%E5%89%B5%E6%96%B0%E9%AB%98-%E4%B8%AD%E7%A7%8B-%E6%95%99%E5%B8%AB%E7%A` -> **live_dated** (page date 2026-09-08); points raw/verified 15/14
  - p24 Taoyuan Airport summer (Jul-Aug) 2026 total passenger volume, cumulative = **8,600,000** passenger trips (2026-07-01..2026-08-31) [keep: ] quote: "桃園國際機場公司今天(8日)發布今年7-8月暑期旅運量達860萬人次"
  - p25 Taoyuan Airport summer (Jul-Aug) 2026 average daily passenger volume = **138,000** passenger trips per day (2026-07-01..2026-08-31) [keep: ] quote: "日均運量達13.8萬人次,創下歷年暑期新高"
  - p26 Taoyuan Airport summer (Jul-Aug) 2025 average daily passenger volume (prior year = **132,000** passenger trips per day (2025-07-01..2025-08-31) [keep: ] quote: "不僅超越去年同期13.2萬人次"
  - p27 Taoyuan Airport summer (Jul-Aug) 2019 pre-pandemic average daily passenger volum = **137,000** passenger trips per day (2019-07-01..2019-08-31) [keep: ] quote: "也超過2019年疫情前的13.7萬人次"
  - p28 Taoyuan Airport Jan-Jul 2026 cumulative passenger volume = **30,000,000** passenger trips (2026-01-01..2026-07-31) [keep: ] quote: "繼桃園機場今年1-7月的旅運量突破3,000萬人次後"
  - p29 Taoyuan Airport full-year 2019 passenger volume peak = **48,000,000** passenger trips (2019-01-01..2019-12-31) [keep: ] quote: "超越2019年的4,800萬高峰"
  - p30 Taoyuan Airport forecast single-day peak passenger volume during Mid-Autumn/Teac = **160,000** passenger trips per day (2026-09-24..2026-09-29) [keep: ] quote: "桃機預估單日旅運高峰將達16萬人次"
  - p31 Taoyuan Airport total forecast passenger volume over 6-day Mid-Autumn/Teachers'  = **930,000** passenger trips (2026-09-24..2026-09-29) [keep: ] quote: "我們抓了6天的疏運,那這6天期間呢,我們預估桃機的總運量應該會突破93萬人次"
  - p32 Taoyuan Airport forecast average daily passenger volume over 6-day holiday trans = **155,000** passenger trips per day (2026-09-24..2026-09-29) [keep: ] quote: "平均每天是15.5萬"
  - p33 Taoyuan Airport forecast daily outbound peak on Sep 24-25 (holiday first two day = **160,000** passenger trips per day (2026-09-24..2026-09-25) [keep: ] quote: "出境的高峰會落在9月24、25,也就是連假的前2天,每天大概平均會有16萬人次"
  - p34 Taoyuan Airport forecast daily inbound peak on Sep 28 (last day of holiday) = **158,000** passenger trips per day (2026-09-28..2026-09-28) [keep: ] quote: "入境的高峰則是會落在連假的最後一天9月28日,大概會到15.8萬人次"
  - p35 Taoyuan Airport single-day peak passenger volume during 2026 Qingming holiday = **157,000** passenger trips per day (2026-04-01..2026-04-30) [keep: ] quote: "超越今年清明節單日旅運高峰15.7萬人次"
  - p36 Taoyuan Airport single-day peak passenger volume during 2026 Lunar New Year holi = **169,000** passenger trips per day (2026-02-01..2026-02-28) [keep: ] quote: "僅次於今年春節假期單日旅運高峰16.9萬人次"
  - p37 Mid-Autumn/Teachers' Day holiday length (consecutive days off) = **4** days (2026-09-25..2026-09-28) [keep: ] quote: "首度與周一的9月28日教師節形成一個4天連假"
- `https://www.mnews.tw/story/amp/20260924sot1347001` -> **live_dated** (page date 2026-09-24); points raw/verified 1/1
  - p38 Taoyuan Airport highest single-day passenger volume during Mid-Autumn holiday pe = **160,000** passengers (人次) (2026-09-25..2026-09-28) [keep: ] quote: "連假期間單日載客量超過16萬人次"
- `https://www.cardu.com.tw/news/detail.php?65326` -> **live_dated** (page date 2026-09-09); points raw/verified 15/14
  - p39 Taoyuan Airport cumulative passenger volume July-August 2026 = **8,600,000** passengers (person-trips) (2026-07-01..2026-08-31) [DISCARD: Redundant duplicate of the Taoyuan July-August 2026 total in p24.] quote: "今(2026)年7、8月累計旅客衝上860萬人次"
  - p40 Taoyuan Airport average daily passenger volume July-August 2026 = **138,000** passengers per day (2026-07-01..2026-08-31) [DISCARD: Redundant duplicate of the Taoyuan July-August daily average in p25.] quote: "平均每日超過13.8萬人次"
  - p41 Taoyuan Airport forecast passenger volume during 6-day Mid-Autumn/Teachers' Day  = **930,000** passengers (person-trips) (2026-09-24..2026-09-29) [DISCARD: Redundant duplicate of the Taoyuan six-day holiday forecast total in p31.] quote: "桃機預測9月24日至9月29日6天疏運期間,旅運量可望達93萬人次"
  - p42 Taoyuan Airport forecast average daily passenger volume during Sep 24-29, 2026 h = **155,000** passengers per day (2026-09-24..2026-09-29) [DISCARD: Redundant duplicate of the Taoyuan holiday daily average in p32.] quote: "平均每天約15.5萬人次"
  - p43 Taoyuan Airport cumulative passenger volume through end of July 2026 = **30,000,000** passengers (person-trips) (2026-01-01..2026-07-31) [DISCARD: Redundant duplicate of the Taoyuan Jan-Jul 2026 cumulative volume in p28.] quote: "截至7月底旅運量已突破3,000萬人次"
  - p44 Taoyuan Airport average daily passenger volume summer 2025 = **132,000** passengers per day (2025-07-01..2025-08-31) [DISCARD: Redundant duplicate of the Taoyuan summer 2025 daily average in p26.] quote: "相較去年暑假平均每日13.2萬人次"
  - p45 Taoyuan Airport average daily passenger volume summer 2019 = **137,000** passengers per day (2019-07-01..2019-08-31) [DISCARD: Redundant duplicate of the Taoyuan summer 2019 daily average in p27.] quote: "也略高於2019年同期約13.7萬人次"
  - p46 Taoyuan Airport forecast single-day total passenger volume Sep 24 or Sep 25, 202 = **160,000** passengers (person-trips) (2026-09-24..2026-09-25) [DISCARD: Redundant duplicate of the Taoyuan single-day holiday peak forecast in p30/p38.] quote: "兩天單日整體旅運量都上看16萬人次"
  - p47 Taoyuan Airport forecast flight movements per day Sep 24-25, 2026 = **780** flights per day (2026-09-24..2026-09-25) [keep: ] quote: "航班數約780架次"
  - p48 Taoyuan Airport forecast daily outbound passengers Sep 24-25, 2026 = **84,000** outbound passengers per day (2026-09-24..2026-09-25) [keep: ] quote: "每日出境遊客約8.4萬人"
  - p49 Taoyuan Airport forecast single-day total passenger volume Sep 28, 2026 (inbound = **158,000** passengers (person-trips) (2026-09-28..2026-09-28) [DISCARD: Redundant duplicate of the Taoyuan Sep 28 inbound peak forecast in p34.] quote: "入境高峰則落在9月28日,預期當天旅運量有15.8萬人次"
  - p50 Taoyuan Airport forecast flight movements Sep 28, 2026 = **736** flights (2026-09-28..2026-09-28) [keep: ] quote: "航班736架次"
  - p51 Taoyuan Airport forecast inbound passengers Sep 28, 2026 = **85,000** inbound passengers (2026-09-28..2026-09-28) [keep: ] quote: "入境旅客約8.5萬人次"
  - p52 Taoyuan Airport record single-day passenger volume Feb 14, 2026 = **169,000** passengers (person-trips) (2026-02-14..2026-02-14) [DISCARD: Redundant duplicate of the Feb 14 2026 Taoyuan peak in p36.] quote: "今年2月14日單日旅客曾高達16.9萬人次,創下歷史新高"
- dropped by code checks: 2 (period_end 2026-12-31 after as_of: 2)

### d4 [base_rates] source-market mix analyst

Hypothesis: September's share of annual or quarterly arrivals and source-market seasonality can translate available 2026 year-to-date or partial source-market data into a September total. Symbolically, total September arrivals = sum over source markets of (market YTD arrivals × September seasonal share), benchmarked to historical September shares.

Queries issued by the searcher: 來臺旅客 按國籍 2026 8月 觀光署; Taiwan visitor arrivals by country September 2025 Tourism Administration; 觀光署 來臺 主要客源市場 2026; "September 2026" visitor arrivals Taiwan 601,339 OR 662,735 Tourism Administration; site:admin.taiwan.net.tw "September 2026" Visitor Statistical Analysis; 2026年9月 來臺旅客 統計 觀光署

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260729002123-260405?chdtv` -> **live_dated** (page date 2026-07-29); points raw/verified 15/15
  - p53 Total visitor arrivals to Taiwan, January-June 2026 (cumulative) = **4,294,589** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p5 (Jan-Jun 2026 cumulative visitor arrivals).] quote: "今年 1至6月来台旅客429万4589人次"
  - p54 Outbound departures from Taiwan, January-June 2026 (cumulative) = **10,654,670** outbound departures (person-trips) (2026-01-01..2026-06-30) [DISCARD: Outbound departures, not visitor arrivals; irrelevant to target.] quote: "出国旅客1065万4670人次,首度上半年出国人数突破千万大关"
  - p55 Japan visitor arrivals to Taiwan, January-June 2026 (cumulative) = **680,499** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "来台旅客以日本68万499人、占15.8%,占比最高"
  - p56 Japan share of total visitor arrivals to Taiwan, January-June 2026 = **15.8** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "来台旅客以日本68万499人、占15.8%,占比最高"
  - p57 Hong Kong visitor arrivals to Taiwan, January-June 2026 (cumulative) = **527,879** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "其次为香港52万7879人,占12.3%"
  - p58 Hong Kong share of total visitor arrivals to Taiwan, January-June 2026 = **12.3** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "其次为香港52万7879人,占12.3%"
  - p59 Korea visitor arrivals to Taiwan, January-June 2026 (cumulative) = **525,775** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "韩国52万5775人、占12.2%"
  - p60 Korea share of total visitor arrivals to Taiwan, January-June 2026 = **12.2** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "韩国52万5775人、占12.2%"
  - p61 Philippines visitor arrivals to Taiwan, January-June 2026 (cumulative) = **400,827** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "菲律宾40万827人次、占9.3%"
  - p62 Philippines share of total visitor arrivals to Taiwan, January-June 2026 = **9.3** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "菲律宾40万827人次、占9.3%"
  - p63 United States visitor arrivals to Taiwan, January-June 2026 (cumulative) = **394,130** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "美国39万4130人、占9.2%"
  - p64 United States share of total visitor arrivals to Taiwan, January-June 2026 = **9.2** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "美国39万4130人、占9.2%"
  - p65 Mainland China visitor arrivals to Taiwan, January-June 2026 (cumulative) = **310,179** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "中国大陆31万179人,占7.2%"
  - p66 Mainland China share of total visitor arrivals to Taiwan, January-June 2026 = **7.2** % (2026-01-01..2026-06-30) [DISCARD: Jan-Jun 2026 source market data; not for September and less timely than August 2026 source market data (p175-p179).] quote: "中国大陆31万179人,占7.2%"
  - p67 Year-on-year growth of visitor arrivals to Taiwan, January-June 2026 = **2.3** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of the Jan-Jun 2026 YoY growth in p6.] quote: "今年上半年来台国际旅客429万4589人次,较去年成长2.3%"
- `https://www.bella.tw/articles/travel&foodies/55531/taiwan-top10-2025` -> **live_dated** (page date 2026-01-04); points raw/verified 15/15
  - p68 Taiwan international visitor arrivals, cumulative January-October 2025 = **6,815,767** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 cumulative; not needed for September 2025 base, which is better derived from p70/p71.] quote: "根據交通部觀光署分析2025年1至10月入境旅客數據,台灣共迎來6,815,767名國際旅客,較去年同期成長9.8%"
  - p69 Year-on-year growth rate of Taiwan international visitor arrivals, January-Octob = **9.8** % (2025-01-01..2025-10-31) [DISCARD: YoY growth Jan-Oct 2025; not needed.] quote: "台灣共迎來6,815,767名國際旅客,較去年同期成長9.8%,顯示觀光動能持續回溫"
  - p70 Taiwan international visitor arrivals, single month October 2025 = **757,860** visitor arrivals (person-trips) (2025-10-01..2025-10-31) [keep: ] quote: "其中10月表現尤為亮眼,單月入境人次達757,860人,較9月大幅成長26%"
  - p71 Month-on-month growth of Taiwan international visitor arrivals, October 2025 vs  = **26** % (2025-10-01..2025-10-31) [keep: ] quote: "單月入境人次達757,860人,較9月大幅成長26%"
  - p72 Japan visitor arrivals to Taiwan, January-October 2025 = **1,146,820** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "1.日本 1,146,820(16.83%)"
  - p73 Japan share of Taiwan international visitor arrivals, January-October 2025 = **16.83** % (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "1.日本 1,146,820(16.83%)"
  - p74 Hong Kong visitor arrivals to Taiwan, January-October 2025 = **974,492** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "2.香港 974,492(14.30%)"
  - p75 Hong Kong share of Taiwan international visitor arrivals, January-October 2025 = **14.3** % (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "2.香港 974,492(14.30%)"
  - p76 Korea visitor arrivals to Taiwan, January-October 2025 = **803,792** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "3.韓國 803,792(11.79%)"
  - p77 Korea share of Taiwan international visitor arrivals, January-October 2025 = **11.79** % (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "3.韓國 803,792(11.79%)"
  - p78 United States visitor arrivals to Taiwan, January-October 2025 = **560,078** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "4.美國 560,078(8.22%)"
  - p79 Mainland China visitor arrivals to Taiwan, January-October 2025 = **533,296** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "5.中國 533,296(7.82%)"
  - p80 Philippines visitor arrivals to Taiwan, January-October 2025 = **501,035** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "6.菲律賓 501,035(7.35%)"
  - p81 Vietnam visitor arrivals to Taiwan, January-October 2025 = **363,525** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "7.越南 363,525(5.33%)"
  - p82 Thailand visitor arrivals to Taiwan, January-October 2025 = **327,203** visitor arrivals (person-trips) (2025-01-01..2025-10-31) [DISCARD: Jan-Oct 2025 source market data; not needed for September 2026 estimate.] quote: "8.泰國 327,203(4.80%)"

### d5 [capacity_consumption] airline scheduler

Hypothesis: Inbound visitor arrivals are bounded by international seat capacity into Taiwan times realised load factor times the non-resident visitor share. Schedule capacity and load-factor data provide an independent upper bound and cross-check.

Queries issued by the searcher: Taiwan international seat capacity 2026 forecast OAG; 桃園機場 2026年 客運量 載客率 國際航線; 2026年9月 來台旅客 觀光署 統計 人次; routes.skyfaring.net 桃園 2026年9月 座位供給 載客率

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/7
  - p83 Cumulative visitor arrivals to Taiwan through end of September (year not stated  = **6,175,000** visitor arrivals (person-trips) (2026-01-01..2026-09-30) [keep: ] quote: "截至9月来台旅客约617.5万人次,与去年同期相比微幅成长"
  - p84 Year-on-year growth rate of cumulative visitor arrivals through end of September = **1.93** % (2026-01-01..2026-09-30) [keep: ] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p85 Share of domestic-travel weekday accommodation subsidy budget already used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Domestic-travel accommodation subsidy budget usage, not inbound visitor arrivals.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p86 Approximate fraction of domestic-travel weekday accommodation subsidy budget use = **0.25** as written "4分之1", value check pending fraction of budget (not stated (page dated 2026-10-07)) [DISCARD: Same domestic subsidy budget fraction as p85, irrelevant to the target.] quote: "目前该经费已使用约4分之1"
  - p87 Number of independent repeat-visitor applicants under international visitor ince = **49,000** applicants (people) (not stated (page dated 2026-10-07)) [DISCARD: Repeat-visitor applicant count lacks September arrival timing and is not a September arrivals level.] quote: "自由行重游客现在约4.9万人申请"
  - p88 Number of corporate group tour registrations under domestic-travel scheme = **371** groups (not stated (page dated 2026-10-07)) [DISCARD: Domestic corporate tour registrations are irrelevant to inbound visitor arrivals.] quote: "像企业团报名已达371团"
  - p89 Approximate number of repeat-visitor group tours (stated as '200-plus') = **200** groups (not stated (page dated 2026-10-07)) [DISCARD: Repeat-visitor group-tour count is not a September arrivals level and is not used.] quote: "重游团体也有约200多团"
- `https://routes.skyfaring.net/airport/tpe/` -> **live_dated** (page date 2009-09-01); points raw/verified 15/15
  - p90 Taoyuan Airport total scheduled seat supply, August 2026 (monthly) = **5,218,808** seats (2026-08-01..2026-08-31) [keep: ] quote: "座位供給 5,218,808 4,365,882 人次"
  - p91 Taoyuan Airport total scheduled seat supply, prior-year comparison (monthly) = **4,365,882** seats (2026-08-01..2026-08-31) [keep: ] quote: "座位供給 5,218,808 4,365,882 人次"
  - p92 Taoyuan Airport average passenger load factor, August 2026 = **83.7** % (2026-08-01..2026-08-31) [keep: ] quote: "平均載客率 83.7% 架次年增率 +1.2%"
  - p93 Taoyuan Airport weekly flights, August 2026 = **4,558** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "每週班次 4,558 20,186 架次/月"
  - p94 Taoyuan Airport monthly flight movements, August 2026 = **20,186** aircraft movements per month (2026-08-01..2026-08-31) [keep: ] quote: "每週班次 4,558 20,186 架次/月"
  - p95 Taoyuan Airport direct destinations count, August 2026 = **101** destinations (2026-08-01..2026-08-31) [keep: ] quote: "101 個航點 · 56 家航空 · 每週 4,558 班 · 2026 年 8 月"
  - p96 Airlines serving Taoyuan Airport, August 2026 = **56** airlines (2026-08-01..2026-08-31) [keep: ] quote: "101 個航點 · 56 家航空 · 每週 4,558 班 · 2026 年 8 月"
  - p97 Northeast Asia share of Taoyuan weekly flights, August 2026 = **39** % (2026-08-01..2026-08-31) [keep: ] quote: "班次最多的是東北亞,佔 39%,最滿的一條是雪梨 96.7%,最空的是亞庇 53.7%。"
  - p98 Taipei-Northeast Asia routes: weekly flights, August 2026 = **1,766** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東北亞 35 航點23 家航空每週 1,766.5 班載客率 90.6%"
  - p99 Taipei-Northeast Asia routes: passenger load factor, August 2026 = **90.6** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東北亞 35 航點23 家航空每週 1,766.5 班載客率 90.6%"
  - p100 Taipei-Southeast Asia routes: weekly flights, August 2026 = **1,150** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東南亞 20 航點22 家航空每週 1,149.5 班載客率 79.4%"
  - p101 Taipei-Southeast Asia routes: passenger load factor, August 2026 = **79.4** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東南亞 20 航點22 家航空每週 1,149.5 班載客率 79.4%"
  - p102 Taipei-Hong Kong/Macau routes: weekly flights, August 2026 = **628** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛港澳 2 航點8 家航空每週 627.5 班載客率 78.6%"
  - p103 Taipei-Hong Kong/Macau routes: passenger load factor, August 2026 = **78.6** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛港澳 2 航點8 家航空每週 627.5 班載客率 78.6%"
  - p104 Taipei-North America routes: weekly flights, August 2026 = **377** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛北美 12 航點5 家航空每週 377 班載客率 79.7%"
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 11/10
  - p105 August 2026 visitor arrivals to Taiwan (monthly total, person-trips) = **660,000** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 monthly arrivals in p1.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p106 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 YoY change in p2.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p107 Cumulative January-August 2026 visitor arrivals to Taiwan = **5,560,000** visitor arrivals (person-trips) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of the Jan-Aug 2026 cumulative arrivals in p3.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p108 Cumulative January-August 2026 visitor arrivals year-on-year increase = **2** % (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate growth of the Jan-Aug cumulative in p3.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p109 May 2026 inbound visitor arrivals to Taiwan (monthly total) = **692,000** visitor arrivals (person-trips) (2026-05-01..2026-05-31) [DISCARD: Approximate May 2026 data; exact May 2026 is p186, and cumulative p3/p4/p5 are exact. Redundant and less precise.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p110 May 2026 inbound visitor arrivals year-on-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Approximate May 2026 data; exact May 2026 is p186, and cumulative p3/p4/p5 are exact. Redundant and less precise.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p111 Cumulative January-May 2026 inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (person-trips) (2026-01-01..2026-05-31) [DISCARD: Approximate May 2026 data; exact May 2026 is p186, and cumulative p3/p4/p5 are exact. Redundant and less precise.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p112 Cumulative January-May 2026 inbound visitor arrivals year-on-year increase = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Approximate May 2026 data; exact May 2026 is p186, and cumulative p3/p4/p5 are exact. Redundant and less precise.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p113 Full-year 2025 visitor arrivals to Taiwan (prior-year actual) = **8,574,547** visitor arrivals (person-trips) (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 arrivals in p7.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p114 Full-year 2025 visitor arrivals year-on-year increase = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 YoY growth in p8.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
- `https://www.taoyuan-airport.com/news/194E8EB8-ED1D-F111-BC22-0050569094FE` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- dropped by code checks: 2 (period_end 2026-12-31 after as_of: 1; number: scale conflict: '萬' in value vs '百萬': 1)

### d6 [related_series] accommodation-sector analyst

Hypothesis: Hotel room-nights sold to inbound visitors in September 2026 relate to visitor arrivals through average length of stay and the share of visitors staying in hotels. This is noisy but can validate or adjust the arrival estimate.

Queries issued by the searcher: 觀光旅館 2026年 住客 統計 外籍 住用率; 來臺旅客 平均停留夜數 2025 觀光旅館 住宿; 觀光旅館營運月報 2026年7月 外國住客 住用率 觀光署; 來臺旅客 2026年 8月 統計 旅客人次 觀光署 每月

- `https://www.fintechgo.com.tw/FinDiary/Article/7952770668275405` -> **live_dated** (page date 2026-08-31); points raw/verified 15/12
  - p115 Taiwan tourist hotels (觀光旅館) total available room-nights, January-June 2026 cumu = **4,814,629** room-nights (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "全台觀光旅館上半年可供住用數4,814,629,客房住用數3,071,941,住用率63.80%"
  - p116 Taiwan tourist hotels (觀光旅館) occupied room-nights, January-June 2026 cumulative = **3,071,941** room-nights (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "全台觀光旅館上半年可供住用數4,814,629,客房住用數3,071,941,住用率63.80%"
  - p117 Taiwan tourist hotels (觀光旅館) occupancy rate (occupied room-nights / available ro = **63.8** % (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "2026年1至6月全台觀光旅館住用率63.80%,平均房價4,694元"
  - p118 Taiwan tourist hotels (觀光旅館) average room rate, January-June 2026 = **4,694** TWD per room (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "全台觀光旅館上半年可供住用數4,814,629,客房住用數3,071,941,住用率63.80%,平均房價4,694元"
  - p119 Taiwan tourist hotels (觀光旅館) total operating revenue, January-June 2026 cumulati = **32,377,121,375** TWD (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "總營業收入323億7,712萬1,375元"
  - p120 International tourist hotels (國際觀光旅館) occupied room-nights, January-June 2026 cu = **2,308,179** room-nights (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "2026年1至6月國際觀光旅館可供住用數3,527,036,客房住用數2,308,179,住用率65.44%"
  - p121 International tourist hotels (國際觀光旅館) occupancy rate, January-June 2026 = **65.44** % (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "國際觀光旅館總營業收入25,834,324,032元,住用率65.44%;外國住客2,325,691人次,日本居首"
  - p122 Foreign guests (外國住客) at Taiwan tourist hotels, January-June 2026 cumulative per = **2,325,691** guest person-count (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "上半年觀光旅館總住客人次570.9483萬人次,其中本國住客338.3792萬人次,外國住客232.5691萬人次"
  - p123 Total guests (總住客) at Taiwan tourist hotels, January-June 2026 cumulative person = **5,709,483** guest person-count (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "上半年觀光旅館總住客人次570.9483萬人次,其中本國住客338.3792萬人次,外國住客232.5691萬人次"
  - p124 Domestic guests (本國住客) at Taiwan tourist hotels, January-June 2026 cumulative pe = **3,383,792** guest person-count (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "其中本國住客338.3792萬人次,外國住客232.5691萬人次"
  - p125 Japan-source foreign guests at Taiwan tourist hotels, January-June 2026 cumulati = **482,660** guest person-count (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "外國住客來源中,日本48.266萬人次最多,韓國27.9161萬人次居次"
  - p126 Taipei City tourist hotels occupied room-nights, January-June 2026 cumulative = **1,236,407** room-nights (2026-01-01..2026-06-30) [DISCARD: Hotel room-nights and guests for Jan-Jun 2026; period mismatch (not September) and not needed for visitor arrival estima] quote: "上半年台北市可供住用數1,719,121,客房住用數1,236,407,住用率71.92%"
- `https://www.tad.gov.tw/m1.aspx?sNo=0044520` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.motc.gov.tw/ch/app/data/doc?id=14&module=news&detailNo=1533752680906756096&serno=ef5248d5-3f89-4c88-8f26-b55e99614693&type=s&preview=&apli` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://taipeitourguide.com/hotel/hoteloperation` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- dropped by code checks: 3 (period year 2025 does not appear in the page text or URL (likely mis-dated): 2; period_end 2026-11-30 after as_of: 1)

### d7 [forecasts_markets] policy-target analyst

Hypothesis: Official 2026 visitor-arrival targets and quarterly tourism plans imply an expected monthly path; if the year-to-date actual is close to the target path, the implied September value constrains the estimate. Treat targets as intentions, not realised data.

Queries issued by the searcher: 觀光署 2026 來台旅客 目標 千萬; Taiwan 2026 visitor arrivals target Tourism Administration; 2026年7月 來台旅客 統計 觀光署 人次 8月; 2026年9月 來台旅客 人次 觀光署 統計

- `https://admin.taiwan.net.tw/english/info/News?pi=30&p=1&q&edate&sdate&c&a=1329` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/11
  - p127 2026 January–August cumulative visitor arrivals to Taiwan = **5,564,858** visitor arrivals (person-trips) (2026-01-01..2026-08-31) [DISCARD: Exact duplicate of Jan-Aug 2026 cumulative arrivals in p3.] quote: "1至8月累計為5,564,858人次"
  - p128 2026 January–July cumulative visitor arrivals to Taiwan = **4,902,123** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [DISCARD: Exact duplicate of Jan-Jul 2026 cumulative arrivals in p4.] quote: "1至7月累計來台旅客為4,902,123人次"
  - p129 2026 August monthly visitor arrivals to Taiwan = **662,735** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Exact duplicate of August 2026 monthly arrivals in p1.] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p130 2026 August visitor arrivals year-on-year change rate = **1.54** % (2026-08-01..2026-08-31) [DISCARD: Exact duplicate of August 2026 YoY change in p2.] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p131 2026 January–June cumulative visitor arrivals to Taiwan = **4,294,589** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Exact duplicate of Jan-Jun 2026 cumulative arrivals in p5.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p132 2026 January–June visitor arrivals year-on-year growth rate = **2.3** % (2026-01-01..2026-06-30) [DISCARD: Exact duplicate of Jan-Jun 2026 YoY growth in p6.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p133 2025 full-year visitor arrivals to Taiwan = **8,574,547** visitor arrivals (person-trips) (2025-01-01..2025-12-31) [DISCARD: Exact duplicate of full-year 2025 arrivals in p7.] quote: "2025年則是8,574,547人次,年增9.12%"
  - p134 2019 full-year visitor arrivals to Taiwan (pre-pandemic baseline) = **11,864,105** visitor arrivals (person-trips) (2019-01-01..2019-12-31) [DISCARD: Exact duplicate of full-year 2019 arrivals in p9.] quote: "2019年全年來臺旅客達11,864,105人次"
  - p135 2026 August visitor arrivals by air transport = **619,389** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月入境旅客中,空運有619,389人次,占93.46%"
  - p136 2026 August visitor arrivals by sea transport = **43,346** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "海運入境43,346人次,占6.54%"
  - p137 2026 August visitor arrivals with tourism as purpose = **422,590** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "來臺目的以觀光422,590人次最多,占63.76%"
- `https://www.chinatimes.com/newspapers/20260211000301-260210` -> **live_dated** (page date 2026-02-11); points raw/verified 8/0
- `https://www.chinatimes.com/cn/realtimenews/20260820004113-260405?chdtv` -> **live_dated** (page date 2026-08-20); points raw/verified 15/10
  - p138 Taiwan visitor arrivals, first half (Jan-Jun) 2026 cumulative = **4,294,589** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Duplicate of Jan-Jun 2026 cumulative arrivals in p5/p53.] quote: "今年上半年(1至6月)来台旅客429万4,589人次"
  - p139 Taiwan outbound departures, first half (Jan-Jun) 2026 cumulative = **10,654,670** outbound departures (person-trips) (2026-01-01..2026-06-30) [DISCARD: Duplicate of Jan-Jun 2026 outbound departures in p54; outbound is not the target.] quote: "出国旅客1065万4,670人次"
  - p140 Taiwan inbound-outbound tourism deficit, first half 2026 = **6,360,000** person-trips (net deficit) (2026-01-01..2026-06-30) [DISCARD: Inbound-outbound tourism deficit, not a visitor-arrivals measure.] quote: "出入境观光逆差达636万人次"
  - p141 Taiwan visitor arrivals, January 2026 monthly = **1,200,000** visitor arrivals (person-trips) (2026-01-01..2026-01-31) [DISCARD: January 2026 visitor arrivals stated as ~1.2 million, inconsistent with official monthly series (p182 = 723,375); mislea] quote: "像今年1月成长率达到快12%,有120万人次"
  - p142 Taiwan visitor arrivals year-on-year growth rate, January 2026 = **12** % (2026-01-01..2026-01-31) [DISCARD: January 2026 visitor arrivals stated as ~1.2 million, inconsistent with official monthly series (p182 = 723,375); mislea] quote: "像今年1月成长率达到快12%"
  - p143 Domestic tourism share of same-day round trips (survey) = **79** % (not stated (page dated 2026-08-20)) [DISCARD: Domestic same-day-trip survey share, irrelevant to inbound visitor arrivals.] quote: "国内旅游「当日来回」约占79%"
  - p144 Estimated domestic travellers benefiting from stimulus plan = **4,000,000** travellers (not stated (page dated 2026-08-20)) [DISCARD: Domestic stimulus beneficiary estimate, irrelevant to the target.] quote: "预估可让国内400万名旅客、国外40万名旅客受益"
  - p145 Estimated foreign travellers benefiting from stimulus plan = **400,000** travellers (not stated (page dated 2026-08-20)) [DISCARD: Stimulus-plan foreign traveller estimate is not a September 2026 arrivals level.] quote: "预估可让国内400万名旅客、国外40万名旅客受益"
  - p146 Estimated output value driven by international visitors under stimulus plan = **19,400,000,000** NTD (not stated (page dated 2026-08-20)) [DISCARD: Stimulus output value, irrelevant to visitor arrivals.] quote: "国内旅客可带动产值约达180亿元、国际客约194亿元"
  - p147 Estimated total output value under stimulus plan = **37,400,000,000** NTD (not stated (page dated 2026-08-20)) [DISCARD: Stimulus total output value, irrelevant to visitor arrivals.] quote: "总计约374亿元"
- dropped by code checks: 17 (period_end 2026-12-31 after as_of: 11; period year 2025 does not appear in the page text or URL (likely mis-dated): 5; value_as_written not in quote as a whole number: 1)

### d8 [shocks] risk and calendar analyst

Hypothesis: Typhoons, earthquakes, travel advisories, cross-strait group-tour policy, visa changes, and calendar effects in September 2026 shift arrivals relative to the seasonal baseline. Measurable exposure such as flight cancellations, closure days, and advisory duration can adjust the estimate.

Queries issued by the searcher: 2026年9月 颱風 台灣 航班取消; 中國 團客 台灣 2026 政策 開放; 2026年8月 來台旅客人次 觀光署 統計; 2026年9月 颱風 侵台 停班停課 天數 9月

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tigerairtw.com/zh-TW/news/260920` -> **live_dated** (page date 2026-09-21); points raw/verified 0/0
- `https://www.matsu-news.gov.tw/news/article/244106` -> **live_dated** (page date 2026-09-03); points raw/verified 5/5
  - p148 Lienchiang (Matsu) Nangan flights cancelled morning of 3 Sep 2026 due to Typhoon = **4** flights (2026-09-03..2026-09-03) [keep: ] quote: "立榮航空上午南竿4班、北竿1班全部取消"
  - p149 Lienchiang (Matsu) Beigan flights cancelled morning of 3 Sep 2026 due to Typhoon = **1** flights (2026-09-03..2026-09-03) [keep: ] quote: "立榮航空上午南竿4班、北竿1班全部取消"
  - p150 Typhoon number affecting Matsu on 3 Sep 2026 = **18** typhoon number (2026-09-03..2026-09-03) [keep: ] quote: "受到第18號颱風外圍環流影響"
  - p151 Afternoon wind gust forecast lower bound, Matsu, 3 Sep 2026 = **30** knots (2026-09-03..2026-09-03) [keep: ] quote: "下午陣風仍可達30-35節"
  - p152 Afternoon wind gust forecast upper bound, Matsu, 3 Sep 2026 = **35** knots (2026-09-03..2026-09-03) [keep: ] quote: "下午陣風仍可達30-35節"
- `https://bj.crntt.com/crn-webapp/touch/detail.jsp?coluid=92&kindid=0&docid=160261906` -> **live_dated** (page date 2026-08-27); points raw/verified 8/8
  - p153 Shanghai residents' applications for group/individual travel to Kinmen, cumulati = **7,252** person-trips (applications) (2026-04-29..2026-08-26) [keep: ] quote: "从今年4月29日到8月26日止,上海居民申请到金门旅游有7252人次"
  - p154 Shanghai residents' approved travel to Kinmen, cumulative 2026-04-29 to 2026-08- = **6,777** person-trips (approved) (2026-04-29..2026-08-26) [keep: ] quote: "核准有6777人次、上海居民申请到马祖旅游有125人次,核准95人次"
  - p155 Shanghai residents' applications for travel to Matsu, cumulative 2026-04-29 to 2 = **125** person-trips (applications) (2026-04-29..2026-08-26) [keep: ] quote: "上海居民申请到马祖旅游有125人次,核准95人次"
  - p156 Shanghai residents' approved travel to Matsu, cumulative 2026-04-29 to 2026-08-2 = **95** person-trips (approved) (2026-04-29..2026-08-26) [keep: ] quote: "上海居民申请到马祖旅游有125人次,核准95人次"
  - p157 Fujian residents' applications for travel to Kinmen and Matsu, cumulative 2026-0 = **73,103** person-trips (applications) (2026-04-29..2026-08-24) [keep: ] quote: "自2026年4月29日至8月24日,福建居民申请赴金马旅游共计7万3103人次"
  - p158 Fujian residents' applications for travel to Kinmen, cumulative 2026-04-29 to 20 = **72,258** person-trips (applications) (2026-04-29..2026-08-24) [keep: ] quote: "其中申请赴金门为7万2258人次、申请赴马祖845人次"
  - p159 Fujian residents' applications for travel to Matsu, cumulative 2026-04-29 to 202 = **845** person-trips (applications) (2026-04-29..2026-08-24) [keep: ] quote: "其中申请赴金门为7万2258人次、申请赴马祖845人次"
  - p160 Shanghai Guolv travel agency years of history (founded 1954) = **72** years (2026-08-27..2026-08-27) [DISCARD: Travel-agency history, irrelevant to September 2026 arrivals.] quote: "上海国旅成立于1954年,至今已有72年历史"

### b1 [administrative] official_release

Hypothesis: The Tourism Administration's first September 2026 monthly table or press release would directly supply the target and remove the need to difference an approximate Jan-Sep cumulative p83 against Jan-Aug p3. This is the main route, so resolving whether p83 is preliminary, revised, or a different-year cumulative would materially tighten the estimate.

Queries issued by the searcher: 觀光署 來臺旅客 統計 2026年9月; Tourism Administration Taiwan visitor arrivals September 2026 monthly statistics; 114年8月 來臺旅客 統計 2026年1-8月 來台旅客 累計 人次 觀光署; "2026" 觀光署 統計 1至8月 來台旅客 萬人次

- `https://admin.taiwan.net.tw/english/info/News?pi=30&p=1&q&edate&sdate&c&a=1329` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/7
  - p161 Cumulative visitor arrivals to Taiwan, January through September (as of end-Sept = **6,175,000** visitor arrivals (person-trips) (2026-01-01..2026-09-30) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "截至9月来台旅客约617.5万人次,与去年同期相比微幅成长"
  - p162 Year-on-year growth rate of cumulative visitor arrivals to Taiwan, January throu = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p163 Share of domestic-travel weekday accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p164 Share of domestic-travel weekday accommodation subsidy budget used, stated as fr = **0.25** as written "4分之1", value check pending % (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "目前该经费已使用约4分之1"
  - p165 Number of enterprise group tour registrations under the subsidy scheme = **371** groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "像企业团报名已达371团"
  - p166 Number of repeat-visit independent traveler applicants (international visitors) = **49,000** people (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "自由行重游客现在约4.9万人申请"
  - p167 Number of repeat-visit group tour registrations (international visitors), approx = **200** groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p83, p84, or irrelevant subsidy information.] quote: "重游团体也有约200多团"
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/11
  - p168 August 2026 visitor arrivals to Taiwan, monthly total (person-trips) = **662,735** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p169 August 2026 visitor arrivals year-on-year change vs August 2025 = **1.54** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p170 January-August 2026 cumulative visitor arrivals to Taiwan = **5,564,858** visitor arrivals (person-trips) (2026-01-01..2026-08-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "1至7月累計來台旅客為4,902,123人次,加上8月月報數字後,1至8月累計為5,564,858人次"
  - p171 January-July 2026 cumulative visitor arrivals to Taiwan = **4,902,123** visitor arrivals (person-trips) (2026-01-01..2026-07-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "1至7月累計來台旅客為4,902,123人次"
  - p172 January-June 2026 cumulative visitor arrivals to Taiwan (CNA report) = **4,294,589** visitor arrivals (person-trips) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p173 August 2026 visitor arrivals by air transport = **619,389** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "2026年8月入境旅客中,空運有619,389人次,占93.46%"
  - p174 August 2026 visitor arrivals by sea transport = **43,346** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1, p2, p3, p4, p5, p11, p135, p136.] quote: "海運入境43,346人次,占6.54%,金門港占總量4.45%"
  - p175 August 2026 visitor arrivals from Hong Kong and Macau = **137,560** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p176 August 2026 visitor arrivals from Japan = **116,582** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p177 August 2026 visitor arrivals from mainland China = **67,303** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p178 August 2026 visitor arrivals from South Korea = **50,973** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
- `https://indiaoutbound.info/trade-news/tourist-arrivals-in-taiwan-drop-2pc-in-august-to-about-663000/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/15
  - p179 Taiwan visitor arrivals, August 2026 (monthly total) = **662,735** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "Taiwan recorded 662,735 visitor arrivals in August 2026, down 2 pc year-on-year"
  - p180 Taiwan visitor arrivals, January to August 2026 cumulative = **5,560,000** visitor arrivals (person-trips) (2026-01-01..2026-08-31) [DISCARD: Rounded cumulative Jan-Aug 2026 and 2025; exact values in p3 and p206. Less precise.] quote: "From January to August 2026, Taiwan recorded 5.56 million visitor arrivals, up 2 pc from 5.46 million during the same period in 2025."
  - p181 Taiwan visitor arrivals, January to August 2025 cumulative (comparison) = **5,460,000** visitor arrivals (person-trips) (2025-01-01..2025-08-31) [DISCARD: Rounded cumulative Jan-Aug 2026 and 2025; exact values in p3 and p206. Less precise.] quote: "up 2 pc from 5.46 million during the same period in 2025"
  - p182 Taiwan visitor arrivals, January 2026 monthly = **723,375** visitor arrivals (person-trips) (2026-01-01..2026-01-31) [keep: ] quote: "Monthly arrivals stood at 723,375 in January, up 11.1 pc from 651,078 in January 2025"
  - p183 Taiwan visitor arrivals, February 2026 monthly = **625,608** visitor arrivals (person-trips) (2026-02-01..2026-02-28) [keep: ] quote: "625,608 in February, down 10.52 pc from 699,158 in February 2025"
  - p184 Taiwan visitor arrivals, March 2026 monthly = **883,061** visitor arrivals (person-trips) (2026-03-01..2026-03-31) [keep: ] quote: "883,061 in March 2026, up 13.42 pc from 778,576 in March 2025"
  - p185 Taiwan visitor arrivals, April 2026 monthly = **758,613** visitor arrivals (person-trips) (2026-04-01..2026-04-30) [keep: ] quote: "758,613 in April, up 0.99 pc from 751,149 in April 2025"
  - p186 Taiwan visitor arrivals, May 2026 monthly = **692,784** visitor arrivals (person-trips) (2026-05-01..2026-05-31) [keep: ] quote: "692,784 in May, down 2.55 pc from 710,933 in May 2025"
  - p187 Taiwan visitor arrivals, June 2026 monthly = **611,148** visitor arrivals (person-trips) (2026-06-01..2026-06-30) [keep: ] quote: "611,148 in June, up 0.79 pc from 606,346 in June 2025"
  - p188 Taiwan visitor arrivals, July 2026 monthly = **607,534** visitor arrivals (person-trips) (2026-07-01..2026-07-31) [keep: ] quote: "607,534 in July 2026, up 3.63 pc from 586,226 in July."
  - p189 Taiwan visitor arrivals, August 2025 monthly (comparison) = **673,102** visitor arrivals (person-trips) (2025-08-01..2025-08-31) [DISCARD: Duplicate of p203 (Aug 2025).] quote: "down from 673,102 in the same month last year"
  - p190 Foreign visitors (non-Overseas-Chinese) arrivals, August 2026 = **466,729** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "The arrivals included 466,729 foreign visitors, down 0.27 pc"
  - p191 Overseas Chinese visitor arrivals, August 2026 = **196,006** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [keep: ] quote: "196,006 Overseas Chinese visitors, down 4.43 pc"
  - p192 Air-travel visitor arrivals, August 2026 = **619,389** visitor arrivals (person-trips) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p11/p135 (air arrivals Aug 2026).] quote: "Air travel accounted for 93.46 pc of total arrivals, with 619,389 visitors entering by air."
  - p193 Average length of stay of visitors leaving Taiwan, August 2026 = **7.68** nights (2026-08-01..2026-08-31) [keep: ] quote: "The average length of stay of visitors leaving Taiwan in August was 7.68 nights."
- dropped by code checks: 5 (period_end 2026-12-31 after as_of: 5)

### b2 [administrative] immigration_proxy

Hypothesis: National Immigration Agency September 2026 foreign-national entry records or airport arrival passenger totals would provide an independent check on the p83-minus-p3 route and help test whether the derived September level is consistent with actual border entries after excluding resident and transit categories.

Queries issued by the searcher: 移民署 2026年9月 外籍旅客 入境 統計; 觀光署 來臺旅客人次 2026年9月; 觀光署 統計 2026年9月 來臺旅客 人次 月報 居住地; 桃園機場 2026年9月 旅運量 入境 旅客人次

- `https://www.motc.gov.tw/uploaddowndoc?file=month/27010.pdf&filedisplay=27010.pdf&flag=doc` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 9/8
  - p194 Cumulative visitor arrivals to Taiwan, January through September (as of end-Sept = **6,175,000** visitor arrivals (person-trips) (2026-01-01..2026-09-30) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p195 Year-on-year growth rate of cumulative visitor arrivals to Taiwan through end-Se = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p196 Cumulative visitor arrivals to Taiwan through September (earlier mention in arti = **6,175,000** visitor arrivals (person-trips) (2026-01-01..2026-09-30) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "截至9月来台旅客约617.5万人次,与去年同期相比微幅成长"
  - p197 Share of domestic-travel weekday accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p198 Share of domestic-travel weekday accommodation subsidy budget used (stated as fr = **0.25** as written "4分之1", value check pending % (not stated (page dated 2026-10-07)) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p199 Number of corporate group tour registrations under the scheme = **371** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "像企业团报名已达371团,正由旅行社安排中"
  - p200 Number of repeat-visit independent travellers (FIT) who have applied for the int = **49,000** applicants (persons) (not stated (page dated 2026-10-07)) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "自由行重游客现在约4.9万人申请"
  - p201 Number of repeat-visit tour groups applying for the international repeat-visitor = **200** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicates of p83, p84, or irrelevant subsidy information.] quote: "重游团体也有约200多团"
- `https://admin.taiwan.net.tw/fapi/AttFile?type=AttFile&id=42113` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://stat.moc.gov.tw/UploadFile/CulturalStatist/46%E4%BE%86%E8%87%BA%E6%97%85%E5%AE%A2%E6%A6%82%E6%B3%81.pdf` -> **dropped** (live http 404); points raw/verified -/-
- dropped by code checks: 1 (period_end 2026-12-31 after as_of: 1)

### b3 [base_rates] seasonal_ratio

Hypothesis: Exact September 2025 and August 2025 monthly arrivals would strengthen the seasonal-ratio check: apply the Sep/Aug 2025 ratio to p1 and compare with the p83-minus-p3 route. This would directly test the September-specific growth proxy p84 and the a1 adjustment used in m2.

Queries issued by the searcher: September 2025 visitor arrivals Taiwan 來臺旅客 人次 August 2025 觀光署; 觀光署 來臺旅客 統計 2025年9月 8月 人次; Tourism Administration Taiwan monthly visitor arrivals September 2025 statistics; "September 2025" "visitors" Taiwan "601" OR "602" OR "600" visitor arrivals; "August 2025" Taiwan visitor arrivals "673" OR "674" OR "675"; site:stat.taiwan.net.tw 來臺旅客 統計 月 114年9月; 觀光署 114年9月 來臺旅客人次 605萬 9月 單月

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34782` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://datalab.visitkorea.or.kr/common/board/Download.do?bcIdx=309960&cbIdx=1132&streFileNm=b934fac3-629c-449b-b011-f3e20b8ac97c.pdf` -> **live_dated** (page date 2025-11-28); points raw/verified 15/15
  - p202 Taiwan inbound visitor arrivals, September 2024 (monthly) = **575,455** visitor arrivals (person-trips) (2024-09-01..2024-09-30) [keep: ] quote: "9월 575,455 794,415"
  - p203 Taiwan inbound visitor arrivals, August 2025 (monthly) = **673,102** visitor arrivals (person-trips) (2025-08-01..2025-08-31) [keep: ] quote: "8월 673,102 616,922 1,030,937 109.1% 65.3%"
  - p204 Taiwan inbound visitor arrivals, August 2024 (monthly) = **616,922** visitor arrivals (person-trips) (2024-08-01..2024-08-31) [keep: ] quote: "8월 673,102 616,922 1,030,937 109.1% 65.3%"
  - p205 Taiwan inbound visitor arrivals, July 2025 (monthly) = **586,226** visitor arrivals (person-trips) (2025-07-01..2025-07-31) [keep: ] quote: "7월 586,226 539,454 988,765 108.7% 59.3%"
  - p206 Taiwan inbound visitor arrivals, cumulative January-August 2025 = **5,456,568** visitor arrivals (person-trips) (2025-01-01..2025-08-31) [keep: ] quote: "1~8월 5,456,568 4,969,697 7,996,961 109.8% 68.2%"
  - p207 Taiwan inbound visitor arrivals, cumulative January-August 2024 = **4,969,697** visitor arrivals (person-trips) (2024-01-01..2024-08-31) [keep: ] quote: "1~8월 5,456,568 4,969,697 7,996,961 109.8% 68.2%"
  - p208 Taiwan inbound visitor arrivals, cumulative January-September 2025 (stated as 60 = **6,050,000** visitor arrivals (person-trips) (2025-01-01..2025-09-30) [keep: ] quote: "1~3분기 인바운드 관광객 605만명, 인/아웃바운드 격차 805만명"
  - p209 Taiwan inbound visitor arrivals, September 2024 (monthly, from 2019 comparison c = **794,415** visitor arrivals (person-trips) (2019-09-01..2019-09-30) [keep: ] quote: "9월 575,455 794,415"
  - p210 Taiwan inbound visitor arrivals, August 2019 (monthly) = **1,030,937** visitor arrivals (person-trips) (2019-08-01..2019-08-31) [keep: ] quote: "8월 673,102 616,922 1,030,937 109.1% 65.3%"
  - p211 Taiwan inbound visitor arrivals, full-year 2024 total = **7,857,686** visitor arrivals (person-trips) (2024-01-01..2024-12-31) [keep: ] quote: "계 7,857,686 11,864,105"
  - p212 Taiwan inbound visitor arrivals, October 2024 (monthly) = **661,115** visitor arrivals (person-trips) (2024-10-01..2024-10-31) [keep: ] quote: "10월 661,115 939,131"
  - p213 Taiwan inbound visitor arrivals, November 2024 (monthly) = **747,800** visitor arrivals (person-trips) (2024-11-01..2024-11-30) [keep: ] quote: "11월 747,800 990,397"
  - p214 Taiwan inbound visitor arrivals, December 2024 (monthly) = **903,619** visitor arrivals (person-trips) (2024-12-01..2024-12-31) [keep: ] quote: "12월 903,619 1,143,201"
  - p215 Taiwan inbound visitor arrivals, January 2025 (monthly) = **651,078** visitor arrivals (person-trips) (2025-01-01..2025-01-31) [keep: ] quote: "1월 651,078 589,961 867,711 110.4% 75.0%"
  - p216 Taiwan inbound visitor arrivals, June 2025 (monthly) = **606,346** visitor arrivals (person-trips) (2025-06-01..2025-06-30) [keep: ] quote: "6월 606,346 571,510 932,697 106.1% 65.0%"
- `https://stat.taiwan.net.tw/` -> **live_dated** (page date 2017-12-01); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5'] Exact Tourism Administration monthly-series values: August 2026 monthly arrivals, its YoY change, and Jan-Jun/Jul/Aug cumulative totals. The cumulative progression and monthly August value are interna
- corroborating: ['p83', 'p84'] Early-October 2026 report gives an approximate Jan-Sep 2026 cumulative level and its YoY growth. This is the strongest direct route: p83 minus p3 isolates September 2026. Caveats: p83 is rounded and s
- corroborating: ['p70', 'p71', 'p84'] p70 and p71 back out September 2025 from the October 2025 level and October-vs-September growth; applying the Jan-Sep 2026 YoY growth p84 gives a September 2026 check close to the p83-minus-p3 route. 
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p47', 'p48', 'p50', 'p51'] Taoyuan Airport summer and Mid-Autumn holiday volume evidence: summer daily average, holiday-period forecasts, and an actual peak-day report. These are passenger flows including residents and both dir
- corroborating: ['p11', 'p135', 'p136', 'p137'] August 2026 transport and purpose composition: air dominates, sea is small, and tourism is the largest purpose category. Useful for converting airport evidence into total-visitor terms, but compositio
- corroborating: ['p115', 'p116', 'p117', 'p122', 'p123', 'p124', 'p125'] H1 2026 tourist-hotel occupancy and foreign-guest counts are broadly plausible against H1 visitor arrivals after allowing for non-hotel stays and same-day visitors. They are not monthly September meas
- uncertain: ['p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104'] Capacity and load-factor values are internally plausible for August 2026, but the listed via/snapshot date 2009-09-01 cannot be a valid archive date for 2026 content. Treat as unverified provenance an
- corroborating: ['p148', 'p149', 'p150', 'p151', 'p152'] Typhoon-related cancellations were local to Matsu morning flights; they are far too small to materially move national monthly visitor arrivals and do not conflict with a roughly normal September total
- corroborating: ['p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159'] Cross-Strait Kinmen/Matsu applications and approvals are small relative to total monthly visitor arrivals and cover multi-month application flows, not September arrivals. They are a minor upside facto
- corroborating: ['p105', 'p106', 'p107', 'p108', 'p113', 'p114', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p138', 'p139'] Rounded or exact media duplicates of p1-p9, p5, p7, and p54. They share the same Tourism Administration or reported source and add no independent measurement; they are discarded as redundant copies.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p203'] August 2026 total (p1) and YoY change (p2) are consistent with August 2025 level (p203).
- corroborating: ['p3', 'p4', 'p5', 'p182', 'p183', 'p184', 'p185', 'p186', 'p187', 'p188'] Cumulative 2026 totals (p3, p4, p5) are consistent with the sum of monthly values (p182-p188); differences reflect month boundaries and rounding.
- corroborating: ['p83', 'p84', 'p3'] Jan-Sep 2026 cumulative (p83) and YoY growth (p84) are consistent with Jan-Aug cumulative (p3) and derived September 2025 level; p83 is rounded but internally coherent.
- conflicting: ['p70', 'p71', 'p206', 'p208'] p70 and p71 imply September 2025 ≈601k, while p208 minus p206 implies ≈593k; p208 is rounded to nearest 50k ('605만명'), so p70/p71 is more precise. Both are broadly consistent within rounding.
- contextual: ['p202', 'p209'] September 2024 (p202) and September 2019 (p209) show historical September levels and the pre-pandemic peak, useful for seasonal scale but not direct projection.
- corroborating: ['p24', 'p25', 'p38', 'p32'] Taoyuan Airport summer and Mid-Autumn holiday passenger volumes (p24, p25, p38, p32) indicate strong September travel, supporting a September total near or above August levels.
- contextual: ['p148', 'p149', 'p150'] Typhoon No. 18 caused minor flight cancellations in Matsu on 3 Sep 2026 (p148-p150), a small negative risk to early September arrivals.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY growth relative to Jan-Sep cumulative growth | 0.75 | 0.5..1.1 | 0.5..1.1 | fraction of cumulative growth rate | m2 (m2) | August 2026 YoY was -1.54% (p2) while Jan-Aug 2026 cumulative growth was about 1.98% (from p3 and p206); to reconcile with Jan-Sep cumulative growth of 1.93% (p84), September-specific growth must be slightly below the cumulative rate, roughly 1.5%, so a1 ≈ 1.5/1.93 ≈ 0.78. We use 0.75. | The cumulative Jan-Sep growth rate is a reasonable proxy for September growth, adjusted for the observed August YoY divergence. | September 2026 YoY growth is far outside 0.5 to 1.1 times the cumulative Jan-Sep growth rate. |
| a2 | Year-over-year change in September/August arrival ratio, 2026 vs 2025 | 1.03 | 0.9..1.15 | 0.9..1.15 | ratio | m3 (m3) | The 2025 September/August ratio is a baseline; a2 captures the change in that ratio due to different YoY growth in August (p2 = -1.54%) and September (derived from p84 and p3 to be about +1.5%). The ratio of (1.015 / 0.9846) ≈ 1.03. | The seasonal pattern is stable and the differential growth is captured by August YoY and cumulative growth. | The September/August ratio changes dramatically (e.g., by more than 15%). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 628,595 | ['p83', 'p3'] / [] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 610,381 | ['p70', 'p71', 'p84'] / ['a1'] | [] |  | 1.00 | B2 of 3 blocks; median of blocks: this block is the median |  |
| m3 | formula_mc | 603,355 | ['p1', 'p70', 'p71', 'p203'] / ['a2'] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p83 - p3; Monte Carlo P10 to P90 -859,889 to 2,154,472; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: (p70 / (1 + p71)) * (1 + p84 * a1); Monte Carlo P10 to P90 507,328 to 734,377; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p1 * (p70 / (1 + p71)) / p203 * a2; Monte Carlo P10 to P90 429,337 to 847,997; result unit visitor converted to visitor; own 80% width x/÷1.41 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 628,595 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 610,381 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 603,355 (width x/÷1.41, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.39; Birge ratio 0.08 (not above one, so no widening); final width x/÷1.39.

Result: central **610,381** visitor, 80% interval [440,063, 846,618] visitor, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['motc']; measure stems ['arriv', 'perso', 'trip', 'visit']


## Final answer

The best computed estimate for visitor arrivals (person-trips) to Taiwan during September 2026, as first reported in the Tourism Administration's monthly series, is 610,381 visitor (80% model-based interval 440,063 to 846,618 visitor).

Main evidence: the direct route differences cumulative arrivals through September (6,175,000 visitor arrivals (person-trips)) against January–August (5,564,858 visitor arrivals (person-trips)). Two independent routes use October 2025 arrivals (757,860 visitor arrivals (person-trips)) with October-vs-September growth (26%) to back out September 2025, then apply growth from cumulative year-on-year (1.93%) scaled by assumption a1 (0.75, range 0.5 to 1.1), or apply the 2025 September/August ratio from August levels (662,735 visitor arrivals (person-trips), 673,102 visitor arrivals (person-trips)) adjusted by a2 (1.03, range 0.9 to 1.15).

Observed inputs are the monthly and cumulative figures; the September-specific growth and seasonal-ratio adjustments are assumptions. Code combined the three routes as equal-weight blocks and took the median; no backtest errors were available, so widths are default or Monte Carlo.

Biggest risk: the rounded cumulative figure and unstable seasonal ratios. Better evidence would be a published September 2025 monthly level and confirmed 2026 vintage consistency.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY growth relative to Jan-Sep cumulative growth: 0.75 fraction of cumulative growth rate, range 0.5 to 1.1; used by m2. Overturned by: September 2026 YoY growth is far outside [n] to [n] times the cumulative Jan-Sep growth rate.
- a2 Year-over-year change in September/August arrival ratio, 2026 vs 2025: 1.03 ratio, range 0.9 to 1.15; used by m3. Overturned by: The September/August ratio changes dramatically (e.g., by more than [n]).

Method details (computed by code):
- m1 formula_mc: p83 - p3; Monte Carlo P10 to P90 -859,889 to 2,154,472; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: (p70 / (1 + p71)) * (1 + p84 * a1); Monte Carlo P10 to P90 507,328 to 734,377; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p1 * (p70 / (1 + p71)) / p203 * a2; Monte Carlo P10 to P90 429,337 to 847,997; result unit visitor converted to visitor; own 80% width x/÷1.41 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 628,595 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 610,381 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 603,355 (width x/÷1.41, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.39; Birge ratio 0.08 (not above one, so no widening); final width x/÷1.39.

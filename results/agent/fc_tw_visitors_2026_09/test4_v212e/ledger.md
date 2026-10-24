# Evidence ledger: fc_tw_visitors_2026_09

- Question: Assume today is 2026-10-24. You know nothing published after this date. Estimate the number of visitor arrivals to Taiwan (來臺旅客人次) in September 2026, as it will be first reported in the Ministry of Transportation and Communications' (Tourism Administration) monthly statistics on visitor arrivals and outbound departures (來臺旅客及國人出國人數).
- as_of: 2026-10-24
- Pinned target: Total visitor arrivals to Taiwan (來臺旅客人次) during September 2026, as reported in the Tourism Administration (MOTC) monthly statistics of visitor arrivals and outbound departures; counted as arrival events (visits) of foreign/non-resident visitors entering Taiwan, not unique persons, and excluding out | unit visitor arrivals (visits) in September 2026 | period 2026-09-01..2026-09-30 | publisher Tourism Administration, Ministry of Transportation and Communications (Taiwan)

## Directions and pages

### d1 [own_history] Tourism Administration statistical publisher

Hypothesis: September 2026 arrivals can be anchored on the same month in prior years (September 2023, 2024, 2025) and on the most recent months published before cutoff (e.g., July/August 2026), applying the historical September-to-adjacent-month seasonal ratio and the year-over-year growth trend. Target = recent monthly level × seasonal factor × trend adjustment.

Queries issued by the searcher: 來臺旅客人次 統計 2025年9月 觀光署; Taiwan visitor arrivals monthly statistics 2025 September total; 觀光署 來臺旅客 統計 2026年7月 8月 人次; Taiwan visitor arrivals 2026 monthly statistics July August 2026

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/13
  - p1 Total visitor arrivals to Taiwan, August 2026 (monthly) = **662,735** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p2 Year-over-year change in total visitor arrivals to Taiwan, August 2026 vs August = **1.54** % (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p3 Cumulative visitor arrivals to Taiwan, January-July 2026 = **4,902,123** visitor arrivals (visits) (2026-01-01..2026-07-31) [keep: ] quote: "1至7月累計來台旅客為4,902,123人次"
  - p4 Cumulative visitor arrivals to Taiwan, January-August 2026 = **5,564,858** visitor arrivals (visits) (2026-01-01..2026-08-31) [keep: ] quote: "1至8月累計為5,564,858人次"
  - p5 Cumulative visitor arrivals to Taiwan, January-June 2026 = **4,294,589** visitor arrivals (visits) (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p6 Year-over-year growth in cumulative visitor arrivals to Taiwan, January-June 202 = **2.3** % (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p7 Total visitor arrivals to Taiwan, full year 2025 = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [keep: ] quote: "2025年則是8,574,547人次,年增9.12%"
  - p8 Year-over-year growth in total visitor arrivals to Taiwan, full year 2025 = **9.12** % (2025-01-01..2025-12-31) [keep: ] quote: "2025年則是8,574,547人次,年增9.12%"
  - p9 Total visitor arrivals to Taiwan, full year 2019 (pre-pandemic baseline) = **11,864,105** visitor arrivals (visits) (2019-01-01..2019-12-31) [DISCARD: 2019 pre-pandemic baseline — too distant and structurally different (Mainland share, capacity) to transfer to 2026 witho] quote: "2019年全年來臺旅客達11,864,105人次"
  - p10 Air arrivals to Taiwan, August 2026 = **619,389** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: August 2026 air-arrival split — no September air/sea split available; not usable for a September decomposition.] quote: "2026年8月入境旅客中,空運有619,389人次,占93.46%"
  - p11 Sea arrivals to Taiwan, August 2026 = **43,346** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: August 2026 sea-arrival split — no September split available.] quote: "海運入境43,346人次,占6.54%"
  - p12 Hong Kong/Macau visitor arrivals to Taiwan, August 2026 = **137,560** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: August 2026 HK/Macau market level — no September market data to carry it forward.] quote: "主要客源包括港澳137,560人次、日本116,582人次"
  - p13 Japan visitor arrivals to Taiwan, August 2026 = **116,582** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: August 2026 Japan market level — no September market data to carry it forward.] quote: "日本116,582人次、中國大陸67,303人次"
- `https://admin.taiwan.net.tw/english/info/News?pi=30&p=1&q&edate&sdate&c&a=1329` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 11/10
  - p14 August 2026 total visitor arrivals to Taiwan (monthly) = **660,000** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p1/p45/p70/p90 (660,000 vs 662,735); adds no information beyond the precise figure.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p15 August 2026 total visitor arrivals to Taiwan, year-over-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p2/p46/p93 (-1.5% vs -1.54%).] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p16 Cumulative January-August 2026 visitor arrivals to Taiwan = **5,560,000** visitor arrivals (visits) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of p4/p47/p71/p91 (5.56M).] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p17 Cumulative January-August 2026 visitor arrivals to Taiwan, year-over-year change = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p48/p92 (+2%).] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p18 May 2026 inbound visitor arrivals to Taiwan (monthly) = **692,000** visitor arrivals (visits) (2026-05-01..2026-05-31) [DISCARD: Rounded duplicate of p122 (692,000 vs 692,784).] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p19 May 2026 inbound visitor arrivals to Taiwan, year-over-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of p50/p97.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p20 Cumulative January-May 2026 inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (visits) (2026-01-01..2026-05-31) [keep: ] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p21 Cumulative January-May 2026 inbound visitor arrivals to Taiwan, year-over-year c = **2.6** % (2026-01-01..2026-05-31) [keep: ] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p22 Full-year 2025 visitor arrivals to Taiwan (prior year total) = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7/p53/p74/p98.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p23 Full-year 2025 visitor arrivals to Taiwan, year-over-year change = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p8/p54/p99.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 2; number: scale conflict: '萬' in value vs '百萬': 1)

### d2 [related_series] Source-market composition (Japan, Korea, Southeast Asia, Americas, Europe, China)

Hypothesis: Total arrivals = sum over source markets of market-specific arrivals. If recent market-level monthly data or year-over-year growth by market is available, aggregate to a September 2026 total. Direction depends on market mix; China/Mainland policy and Japan/Korea trends dominate.

Queries issued by the searcher: 觀光署 來臺旅客 按國別 統計 2026; Taiwan visitor arrivals by country Japan Korea 2025 monthly statistics; "Visitor Statistical Analysis for September 2025" Tourism Administration; 2026年8月 來臺旅客 統計 觀光署 8月 來台人次

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=35715` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20260729002123-260405?chdtv` -> **live_dated** (page date 2026-07-29); points raw/verified 15/15
  - p24 Total visitor arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **4,294,589** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p5/p101 (Jan–Jun cumulative).] quote: "今年 1至6月來台旅客429萬4589人次"
  - p25 Total outbound departures from Taiwan, first half of year (Jan-Jun), cumulative = **10,654,670** outbound departures (visits) (2026-01-01..2026-06-30) [DISCARD: Outbound departures — different flow (residents leaving), not inbound arrivals.] quote: "出國旅客1065萬4670人次,首度上半年出國人數突破千萬大關"
  - p26 YoY growth of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **2.3** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of p6.] quote: "今年上半年來台國際旅客429萬4589人次,較去年成長2.3%"
  - p27 Japan arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **680,499** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 2026 Japan cumulative — no September market-level data to combine.] quote: "來台旅客以日本68萬499人、占15.8%,占比最高"
  - p28 Japan share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **15.8** % (2026-01-01..2026-06-30) [DISCARD: H1 Japan share — no September market data.] quote: "來台旅客以日本68萬499人、占15.8%,占比最高"
  - p29 Hong Kong arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **527,879** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 HK cumulative — no September market data.] quote: "其次為香港52萬7879人,占12.3%"
  - p30 Hong Kong share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **12.3** % (2026-01-01..2026-06-30) [DISCARD: H1 HK share — no September market data.] quote: "其次為香港52萬7879人,占12.3%"
  - p31 Korea arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **525,775** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 Korea cumulative — no September market data.] quote: "韓國52萬5775人、占12.2%"
  - p32 Korea share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **12.2** % (2026-01-01..2026-06-30) [DISCARD: H1 Korea share — no September market data.] quote: "韓國52萬5775人、占12.2%"
  - p33 Philippines arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **400,827** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 Philippines cumulative — no September market data.] quote: "菲律賓40萬827人次、占9.3%"
  - p34 Philippines share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **9.3** % (2026-01-01..2026-06-30) [DISCARD: H1 Philippines share — no September market data.] quote: "菲律賓40萬827人次、占9.3%"
  - p35 USA arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **394,130** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 USA cumulative — no September market data.] quote: "美國39萬4130人、占9.2%"
  - p36 USA share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **9.2** % (2026-01-01..2026-06-30) [DISCARD: H1 USA share — no September market data.] quote: "美國39萬4130人、占9.2%"
  - p37 Mainland China arrivals to Taiwan, first half of year (Jan-Jun), cumulative = **310,179** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: H1 Mainland China cumulative — no September market data.] quote: "中國大陸31萬179人,占7.2%"
  - p38 Mainland China share of visitor arrivals to Taiwan, first half of year (Jan-Jun) = **7.2** % (2026-01-01..2026-06-30) [DISCARD: H1 Mainland China share — no September market data.] quote: "中國大陸31萬179人,占7.2%"
- `https://admin.taiwan.net.tw/english/info/News?pi=30&p=1&q&edate&sdate&c&a=1329` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d3 [physical_flow] Airport/port immigration and flight capacity

Hypothesis: Air arrivals dominate Taiwan inbound tourism. Total arrivals ≈ international passenger arrivals at Taoyuan/Songshan/Kaohsiung airports × share that are foreign visitors (vs. residents/transit), plus sea arrivals. Flight seat capacity and load factors constrain the ceiling.

Queries issued by the searcher: 桃園機場 國際線 入境 旅客 2026年9月 統計; Taiwan Tourism Administration visitor arrivals September 2026 statistics; 觀光署 來臺旅客 9月 統計 人次 2026年 單月; "來臺旅客" 114年9月 統計 人次 觀光署

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 7/6
  - p39 Cumulative visitor arrivals to Taiwan through end of September (year-to-date, as = **6,175,000** visitor arrivals (person-times) (2026-01-01..2026-09-30) [DISCARD: Duplicate of p111 (end-September YTD 6,175,000); keep one copy.] quote: "截至9月来台旅客约617.5万人次"
  - p40 Year-on-year growth rate of cumulative visitor arrivals through end of September = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of p112.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p41 Independent-travel repeat visitors (international) applications received = **49,000** applicants (persons) (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p116 (49,000 repeat independent-travel applicants).] quote: "自由行重游客现在约4.9万人申请"
  - p42 Repeat-visit group tours (international) applications received = **200** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p117 (~200 repeat group tours).] quote: "重游团体也有约200多团"
  - p43 Domestic weekday accommodation subsidy budget used (share of allocated funds) = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p113 (24.95% subsidy used).] quote: "平日住宿经费已使用约24.95%"
  - p44 Corporate group tour registrations under the scheme = **371** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of p115 (371 corporate groups).] quote: "企业团报名已达371团"
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 13/11
  - p45 August 2026 visitor arrivals to Taiwan (monthly total, Tourism Administration) = **660,000** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1 (August 2026 total).] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p46 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p2.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p47 Cumulative January-August 2026 visitor arrivals to Taiwan = **5,560,000** visitor arrivals (visits) (2026-01-01..2026-08-31) [DISCARD: Duplicate of p4.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p48 Cumulative January-August 2026 visitor arrivals year-on-year growth = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p92.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p49 May 2026 inbound visitor arrivals to Taiwan (monthly total) = **692,000** visitor arrivals (visits) (2026-05-01..2026-05-31) [DISCARD: Duplicate of p122.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p50 May 2026 inbound visitor arrivals year-on-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of p97.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p51 Cumulative January-May 2026 inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (visits) (2026-01-01..2026-05-31) [DISCARD: Duplicate of Jan–May cumulative p20.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p52 Cumulative January-May 2026 inbound visitor arrivals year-on-year growth = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Duplicate of Jan–May growth p21.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p53 Full-year 2025 visitor arrivals to Taiwan (annual total) = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p54 Full-year 2025 visitor arrivals year-on-year growth = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p8.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p55 Domestic hotel guest nights January-September 2025 growth vs pre-pandemic same p = **2** 成 (tenths, growth in domestic guest nights) (2025-01-01..2025-09-30) [DISCARD: Domestic hotel guest-night growth vs pre-pandemic — different population (domestic) and period; not usable for inbound a] quote: "本國住客更覺疫情前同期大增2成"
- `https://www.cardu.com.tw/news/detail.php?65326` -> **live_dated** (page date 2026-09-09); points raw/verified 15/14
  - p56 Taoyuan Airport cumulative passenger volume July-August 2026 = **8,600,000** passengers (2026-07-01..2026-08-31) [DISCARD: Taoyuan Jul–Aug cumulative — both directions, no September foreign-share conversion available.] quote: "今(2026)年7、8月累計旅客衝上860萬人次"
  - p57 Taoyuan Airport average daily passenger volume July-August 2026 = **138,000** passengers per day (2026-07-01..2026-08-31) [DISCARD: Taoyuan summer daily average — both directions, no conversion to inbound foreign visits.] quote: "平均每日超過13.8萬人次"
  - p58 Taoyuan Airport forecast passenger volume during Mid-Autumn/Teachers' Day holida = **930,000** passengers (2026-09-24..2026-09-29) [DISCARD: Taoyuan holiday-period forecast — both directions, forecast not actual, no conversion.] quote: "桃機預測9月24日至9月29日6天疏運期間,旅運量可望達93萬人次"
  - p59 Taoyuan Airport forecast average daily passenger volume during Sep 24-29, 2026 h = **155,000** passengers per day (2026-09-24..2026-09-29) [DISCARD: Taoyuan holiday daily forecast — both directions, forecast.] quote: "平均每天約15.5萬人次"
  - p60 Taoyuan Airport cumulative passenger volume through end of July 2026 = **30,000,000** passengers (2026-01-01..2026-07-31) [DISCARD: Taoyuan YTD through July — both directions, no conversion.] quote: "截至7月底旅運量已突破3,000萬人次"
  - p61 Taoyuan Airport average daily passenger volume summer 2025 = **132,000** passengers per day (2025-07-01..2025-08-31) [DISCARD: Taoyuan 2025 summer daily average — both directions, no conversion.] quote: "相較去年暑假平均每日13.2萬人次"
  - p62 Taoyuan Airport average daily passenger volume summer 2019 (pre-pandemic) = **137,000** passengers per day (2019-07-01..2019-08-31) [DISCARD: Taoyuan 2019 summer daily average — both directions, no conversion.] quote: "也略高於2019年同期約13.7萬人次"
  - p63 Taoyuan Airport forecast single-day total passenger volume on Sep 24 and Sep 25, = **160,000** passengers per day (2026-09-24..2026-09-25) [DISCARD: Taoyuan peak-day forecast — both directions, forecast.] quote: "兩天單日整體旅運量都上看16萬人次"
  - p64 Taoyuan Airport forecast flight movements on Sep 24-25, 2026 peak days = **780** flights per day (2026-09-24..2026-09-25) [DISCARD: Taoyuan flight movements — capacity, not realized arrivals.] quote: "航班數約780架次"
  - p65 Taoyuan Airport forecast daily outbound passengers on Sep 24-25, 2026 peak days = **84,000** passengers per day (2026-09-24..2026-09-25) [DISCARD: Taoyuan outbound forecast — outbound, not inbound.] quote: "每日出境遊客約8.4萬人"
  - p66 Taoyuan Airport forecast total passenger volume on Sep 28, 2026 (inbound peak) = **158,000** passengers (2026-09-28..2026-09-28) [DISCARD: Taoyuan Sep 28 total forecast — both directions, forecast.] quote: "入境高峰則落在9月28日,預期當天旅運量有15.8萬人次"
  - p67 Taoyuan Airport forecast flight movements on Sep 28, 2026 = **736** flights (2026-09-28..2026-09-28) [DISCARD: Taoyuan flight movements — capacity.] quote: "航班736架次"
  - p68 Taoyuan Airport forecast inbound passengers on Sep 28, 2026 = **85,000** passengers (2026-09-28..2026-09-28) [DISCARD: Taoyuan Sep 28 inbound forecast — includes residents and transit, single day, forecast; no conversion to monthly foreign] quote: "入境旅客約8.5萬人次"
  - p69 Taoyuan Airport record single-day passenger volume on Feb 14, 2026 = **169,000** passengers (2026-02-14..2026-02-14) [DISCARD: Taoyuan record single day — both directions, context only.] quote: "今年2月14日單日旅客曾高達16.9萬人次,創下歷史新高"
- `https://www.taoyuan-airport.com/news/C1CB08AC-9AAA-F111-BC31-0050569094FE?p=1&k=&s=&e=` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 2; number: scale conflict: '萬' in value vs 'million': 1; number: scale conflict: '百萬' in value vs '萬': 1)

### d4 [capacity_consumption] Hotel occupancy and accommodation demand

Hypothesis: Visitor arrivals correlate with international hotel guest-nights and occupancy in Taiwan. If international guest-nights or occupancy for September 2026 are reported, divide by average length of stay to approximate arrivals. Direction: higher occupancy/guest-nights implies higher arrivals.

Queries issued by the searcher: 觀光旅館 住客 統計 外籍 客房住用率 2025; 來臺旅客 平均停留天數 2025 觀光局 統計; 2026年9月 來臺旅客 人次 觀光署 統計 2026; 觀光旅館 住客 統計 2026 外籍住客 客房住用率 月

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/0
- `https://www.tad.gov.tw/m1.aspx?sNo=0044520` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://jinninghc.kinmen.gov.tw/News_Content.aspx?n=3C6678B762C21300&sms=A2C62D68901B977C&s=4EFB13E264ECEE51` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 6/5
  - p70 August 2026 visitor arrivals to Taiwan (monthly) = **660,000** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p71 January–August 2026 cumulative visitor arrivals to Taiwan = **5,560,000** visitor arrivals (visits) (2026-01-01..2026-08-31) [DISCARD: Duplicate of p4.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p72 May 2026 inbound visitor arrivals to Taiwan (monthly) = **692,000** visitor arrivals (visits) (2026-05-01..2026-05-31) [DISCARD: Duplicate of p122.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p73 January–May 2026 cumulative inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (visits) (2026-01-01..2026-05-31) [DISCARD: Duplicate of Jan–May cumulative p20.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p74 2025 (114年) total visitor arrivals to Taiwan = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
- dropped by code checks: 9 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 8; number: scale conflict: '百萬' in value vs '萬': 1)

### d5 [shocks] Policy, calendar, and disruption effects

Hypothesis: September 2026 arrivals may deviate from trend due to typhoons, cross-strait policy changes, visa/travel programs, major events, or airline capacity changes. Quantify exposure (e.g., typhoon days closing airports, new visa-free programs, China group-tour policy) to adjust the baseline.

Queries issued by the searcher: 颱風 機場 關閉 2026年9月 台灣 航班取消; 中國 團客 來台 政策 2026 開放; Taiwan visa-free 2026 new countries extension; 來臺旅客人次 2026年9月 觀光署 統計

- `https://travel.kompas.com/read/2026/07/22/140015927/taiwan-perpanjang-bebas-visa-3-negara-asean-indonesia-termasuk` -> **live_dated** (page date 2026-07-22); points raw/verified 10/3
  - p75 Year-on-year growth in international visitor arrivals to Taiwan, 2025 vs 2024 = **9** % (international visitor arrivals, 2025 vs 2024) (2025-01-01..2025-12-31) [DISCARD: Rounded duplicate of p8/p99 (2025 +9%).] quote: "Jumlah tersebut meningkat sekitar 9 persen dibandingkan dengan 2024."
  - p76 Start date of extended Taiwan visa-free program (Thailand, Philippines, Brunei) = **1** as written "1 Agustus 2026", value check pending day of month (August 2026) (2026-08-01..2026-08-01) [DISCARD: Visa-free start date — context only, no numeric role.] quote: "Kebijakan bebas visa ini berlaku mulai 1 Agustus 2026 hingga 31 Juli 2027."
  - p77 Year Taiwan first introduced visa-free policy for Thailand, Philippines, Brunei = **2,016** year (2016-01-01..2016-12-31) [DISCARD: Year of first visa-free introduction — historical context, no numeric role.] quote: "Taiwan pertama kali memberlakukan kebijakan bebas visa bagi warga negara Thailand, Filipina, dan Brunei pada 2016."
- `https://www.boca.gov.tw/cp-220-8253-ff790-2.html` -> **live_dated** (page date 2017-07-31); points raw/verified 9/4
  - p78 Start date of extended trial visa-free entry for Thailand, Brunei, Philippines n = **1** as written "August 1, 2026", value check pending date (day of month) (2026-08-01..2026-08-01) [DISCARD: Duplicate of p76.] quote: "from August 1, 2026, to July 31, 2027."
  - p79 Additional extension duration of Project for Simplifying Visa Regulations for Hi = **1** as written "a further year", value check pending years (not stated (page dated 2017-07-31)) [DISCARD: High-end group visa program extension — no quantifiable September flow effect.] quote: "will be extended for a further year through December 31, 2027"
  - p80 Effective date Cambodia nationals lose eligibility for high-end group tourist an = **1** as written "August 1, 2026", value check pending date (day of month) (2026-08-01..2026-08-01) [DISCARD: Cambodia eligibility removal — small market, no quantifiable September effect.] quote: "Nationals of Cambodia will no longer be eligible for these two initiatives from August 1, 2026."
  - p81 Date of interagency meeting reviewing visa and entry measures = **21** date (day of month) (2026-04-21..2026-04-21) [DISCARD: Meeting date — no numeric role.] quote: "convened a meeting on April 21 with relevant government agencies"
- `https://metroradio.com.hk/News/details.aspx?NewsId=20260709194601&page=0` -> **live_dated** (page date 2026-07-09); points raw/verified 4/3
  - p82 Hong Kong Airlines round-trip Taipei flights cancelled on Saturday (at least, pa = **4** as written "至少四對", value check pending pairs of round-trip flights (2026-09-12..2026-09-12) [DISCARD: HK–Taipei cancellations — small magnitude, no reliable conversion to arrivals; context only.] quote: "其網站顯示周六至少四對往返台北的航班已經取消。"
  - p83 Greater Bay Airlines flights between Taipei and Zhoushan cancelled Friday and Sa = **6** flights (2026-09-11..2026-09-12) [DISCARD: HK–Zhoushan cancellations — small magnitude, context only.] quote: "大灣區航空亦宣布,取消周五及周六共6班來往台北及浙江舟山的航班。"
  - p84 HK Express flights between Hong Kong and Okinawa cancelled on Friday = **4** as written "四班", value check pending flights (2026-09-11..2026-09-11) [DISCARD: HK–Okinawa cancellations — not a Taiwan arrival route.] quote: "香港快運宣布,周五往返香港及沖繩的四班航班經已取消"
- `https://www.matsu-news.gov.tw/news/article/244106` -> **live_dated** (page date 2026-09-03); points raw/verified 5/5
  - p85 Cancelled Uni Air flights at Nangan (南竿) on morning of 3 September 2026 due to T = **4** flights (2026-09-03..2026-09-03) [DISCARD: Matsu domestic flight cancellations — domestic, not inbound visitor arrivals.] quote: "立榮航空上午南竿4班、北竿1班全部取消"
  - p86 Cancelled Uni Air flights at Beigan (北竿) on morning of 3 September 2026 due to T = **1** flights (2026-09-03..2026-09-03) [DISCARD: Matsu domestic flight cancellations — domestic.] quote: "立榮航空上午南竿4班、北竿1班全部取消"
  - p87 Typhoon number affecting Matsu flights on 3 September 2026 = **18** typhoon number (2026-09-03..2026-09-03) [DISCARD: Typhoon number — context only.] quote: "受到第18號颱風外圍環流影響"
  - p88 Forecast afternoon wind gusts (lower bound) in knots, Matsu, 3 September 2026 = **30** knots (2026-09-03..2026-09-03) [DISCARD: Wind gust forecast — context only.] quote: "下午陣風仍可達30-35節"
  - p89 Forecast afternoon wind gusts (upper bound) in knots, Matsu, 3 September 2026 = **35** knots (2026-09-03..2026-09-03) [DISCARD: Wind gust forecast — context only.] quote: "下午陣風仍可達30-35節"
- dropped by code checks: 13 (scale word 'million' not supported by quote or table header: 3; period_end 2027-07-31 after as_of: 6; period_end 2027-12-31 after as_of: 1; value_as_written not in quote as a whole number: 2; number: no number in value_as_written: 1)

### d6 [forecasts_markets] Official targets and industry forecasts

Hypothesis: Tourism Administration annual arrival targets and industry forecasts for 2026 can be decomposed into monthly paths; September share of annual total from history gives a September estimate. Direction: target-implied level vs. recent run-rate.

Queries issued by the searcher: 2026 來臺旅客 目標 觀光署; Taiwan 2026 tourist arrival target Tourism Administration; 觀光署 2026年9月 來臺旅客 統計 人次; 2025年9月 來台旅客 人次 觀光署 統計 單月

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/0
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 12/11
  - p90 August 2026 visitor arrivals to Taiwan (monthly, reported by Tourism Administrat = **660,000** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p1.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p91 January–August 2026 cumulative visitor arrivals to Taiwan = **5,560,000** visitor arrivals (visits) (2026-01-01..2026-08-31) [DISCARD: Duplicate of p4.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p92 January–August 2026 cumulative visitor arrivals year-on-year growth rate = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p48.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p93 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p2.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p94 May 2026 visitor arrivals to Taiwan (monthly) = **692,000** visitor arrivals (visits) (2026-05-01..2026-05-31) [DISCARD: Duplicate of p122.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p95 January–May 2026 cumulative visitor arrivals to Taiwan = **3,680,000** visitor arrivals (visits) (2026-01-01..2026-05-31) [DISCARD: Duplicate of Jan–May cumulative p20.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p96 January–May 2026 cumulative visitor arrivals year-on-year growth rate = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Duplicate of Jan–May growth p21.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p97 May 2026 visitor arrivals year-on-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of p19/p50.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p98 2025 full-year visitor arrivals to Taiwan (actual, from 114年 survey) = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p99 2025 full-year visitor arrivals year-on-year growth rate = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p8.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p100 Japanese visitor arrivals to Taiwan in 2025 through September 25 (cumulative) = **1,000,000** as written "百萬", value check pending visitor arrivals (visits) (2025-01-01..2025-09-25) [DISCARD: 2025 Japanese cumulative through Sep 25 — different year, no direct September 2026 role.] quote: "今年日本旅客來臺人次至9月25日已經突破百萬"
- `https://www.chinatimes.com/cn/realtimenews/20260820004113-260405?chdtv` -> **live_dated** (page date 2026-08-20); points raw/verified 15/10
  - p101 Visitor arrivals to Taiwan, January-June 2026 (cumulative) = **4,294,589** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p5.] quote: "今年上半年(1至6月)来台旅客429万4,589人次"
  - p102 Outbound departures from Taiwan, January-June 2026 (cumulative) = **10,654,670** outbound departures (visits) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p25.] quote: "出国旅客1065万4,670人次"
  - p103 Inbound-outbound tourism deficit, January-June 2026 = **6,360,000** visits (outbound minus inbound) (2026-01-01..2026-06-30) [DISCARD: Inbound-outbound deficit is a derived quantity from p25/p5; adds no independent information.] quote: "出入境观光逆差达636万人次"
  - p104 January 2026 visitor arrivals to Taiwan (monthly) = **1,200,000** visitor arrivals (visits) (2026-01-01..2026-01-31) [DISCARD: January 2026 level of ~1.2M is inconsistent with the Jan–Jun cumulative and with p126 (723,375); misleading as a level.] quote: "像今年1月成长率达到快12%,有120万人次"
  - p105 January 2026 visitor arrival growth rate (year-on-year) = **12** % (2026-01-01..2026-01-31) [DISCARD: Growth rate tied to the erroneous p104 level; superseded by p126's +11.1%.] quote: "像今年1月成长率达到快12%"
  - p106 Domestic same-day round-trip share of domestic travel (latest survey) = **79** % (not stated (page dated 2026-08-20)) [DISCARD: Domestic same-day travel share — irrelevant to inbound visitor arrivals.] quote: "最新调查报告显示,国内旅游「当日来回」约占79%"
  - p107 Estimated domestic travelers benefiting from stimulus plan = **4,000,000** travelers (persons) (not stated (page dated 2026-08-20)) [DISCARD: Domestic traveler count under stimulus — irrelevant to inbound arrivals.] quote: "预估可让国内400万名旅客、国外40万名旅客受益"
  - p108 Estimated foreign travelers benefiting from stimulus plan = **400,000** travelers (persons) (not stated (page dated 2026-08-20)) [DISCARD: Stimulus foreign-traveler estimate is a program target, not an observed September flow; not usable as a level.] quote: "预估可让国内400万名旅客、国外40万名旅客受益"
  - p109 Estimated output value driven by domestic travelers under stimulus plan = **18,000,000,000** NTD (not stated (page dated 2026-08-20)) [DISCARD: Domestic output value under stimulus — irrelevant to inbound arrivals.] quote: "国内旅客可带动产值约达180亿元"
  - p110 Estimated output value driven by international travelers under stimulus plan = **19,400,000,000** NTD (not stated (page dated 2026-08-20)) [DISCARD: International output value under stimulus — a value measure, not a visit count; not convertible without an unstated spen] quote: "国际客约194亿元,总计约374亿元"
- `https://www.chinatimes.com/newspapers/20260211000301-260210` -> **live_dated** (page date 2026-02-11); points raw/verified 11/0
- dropped by code checks: 25 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 8; number: scale conflict: '百萬' in value vs '萬': 1; period_end 2026-12-31 after as_of: 9; period year 2025 does not appear in the page text or URL (likely mis-dated): 5; value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 1)

### d7 [base_rates] Seasonal and day-count structure

Hypothesis: September is a low-to-mid season month; arrivals scale with number of weekend days, school calendar, and holiday timing (Mid-Autumn Festival, National Day). Adjust a baseline monthly rate by day-count and holiday effects. Target = daily arrival rate × 30 days × holiday/seasonal multiplier.

Queries issued by the searcher: 來臺旅客 統計 2026 每月 觀光署; 2026 中秋節 日期 台灣 放假; 2025年9月 來臺旅客 人次 觀光署 統計 九月; "Visitor Statistical Analysis for August 2026" Tourism Administration 662,735

- `https://turnnewsapp.com/livenews/life/20261007004019-260405` -> **live_dated** (page date 2026-10-24); points raw/verified 9/8
  - p111 Cumulative visitor arrivals to Taiwan through September (year-to-date, as of end = **6,175,000** visitor arrivals (visits) (2026-01-01..2026-09-30) [keep: ] quote: "截至9月來台旅客約617.5萬人次,與去年同期相比微幅成長"
  - p112 Year-on-year growth rate of cumulative visitor arrivals to Taiwan through Septem = **1.93** % (2026-01-01..2026-09-30) [keep: ] quote: "截至9月底,來台旅客約617.5萬人次,與去年同期相比成長1.93%"
  - p113 Share of weekday domestic-travel accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-24)) [DISCARD: Domestic accommodation subsidy usage — irrelevant to inbound arrivals.] quote: "平日住宿經費已使用約24.95%,已用掉約4分之1經費"
  - p114 Share of weekday domestic-travel accommodation subsidy budget used (stated as fr = **0.25** as written "4分之1", value check pending % (subsidy budget used / total budget) (not stated (page dated 2026-10-24)) [DISCARD: Duplicate of p113.] quote: "目前該經費已使用約4分之1"
  - p115 Number of corporate group tour applications registered = **371** group tour applications (not stated (page dated 2026-10-24)) [DISCARD: Corporate group tour registrations — domestic scheme, irrelevant to inbound arrivals.] quote: "像企業團報名已達371團,正由旅行社安排中"
  - p116 Number of repeat independent-travel international visitor applicants = **49,000** applicants (repeat independent travelers) (not stated (page dated 2026-10-24)) [DISCARD: Repeat-visitor applications are program sign-ups, not September arrivals; program started October.] quote: "自由行重遊客現在約4.9萬人申請"
  - p117 Number of repeat group-tour international visitor groups (approximately) = **200** group tours (not stated (page dated 2026-10-24)) [DISCARD: Repeat group-tour applications — program sign-ups, not September arrivals.] quote: "重遊團體也有約200多團"
  - p118 Start date of international visitor incentive program = **10** as written "10月10日", value check pending day of month (October 10) (2026-10-10..2026-10-10) [DISCARD: Program start date is context only; no numeric role in a September estimate.] quote: "國際客獎勵10月10日才上路,現在還在申請初期"
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://indiaoutbound.info/trade-news/tourist-arrivals-in-taiwan-drop-2pc-in-august-to-about-663000/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/15
  - p119 Total visitor arrivals to Taiwan, August 2026 = **662,735** visitor arrivals (2026-08-01..2026-08-31) [DISCARD: Duplicate of August 2026 total p1.] quote: "Taiwan recorded 662,735 visitor arrivals in August 2026, down 2 pc year-on-year"
  - p120 Total visitor arrivals to Taiwan, July 2026 = **607,534** visitor arrivals (2026-07-01..2026-07-31) [keep: ] quote: "607,534 in July 2026, up 3.63 pc from 586,226 in July."
  - p121 Total visitor arrivals to Taiwan, June 2026 = **611,148** visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "611,148 in June, up 0.79 pc from 606,346 in June 2025"
  - p122 Total visitor arrivals to Taiwan, May 2026 = **692,784** visitor arrivals (2026-05-01..2026-05-31) [keep: ] quote: "692,784 in May, down 2.55 pc from 710,933 in May 2025"
  - p123 Total visitor arrivals to Taiwan, April 2026 = **758,613** visitor arrivals (2026-04-01..2026-04-30) [keep: ] quote: "758,613 in April, up 0.99 pc from 751,149 in April 2025"
  - p124 Total visitor arrivals to Taiwan, March 2026 = **883,061** visitor arrivals (2026-03-01..2026-03-31) [keep: ] quote: "883,061 in March 2026, up 13.42 pc from 778,576 in March 2025"
  - p125 Total visitor arrivals to Taiwan, February 2026 = **625,608** visitor arrivals (2026-02-01..2026-02-28) [keep: ] quote: "625,608 in February, down 10.52 pc from 699,158 in February 2025"
  - p126 Total visitor arrivals to Taiwan, January 2026 = **723,375** visitor arrivals (2026-01-01..2026-01-31) [keep: ] quote: "Monthly arrivals stood at 723,375 in January, up 11.1 pc from 651,078 in January 2025"
  - p127 Cumulative visitor arrivals to Taiwan, January to August 2026 = **5,560,000** visitor arrivals (2026-01-01..2026-08-31) [keep: ] quote: "From January to August 2026, Taiwan recorded 5.56 million visitor arrivals, up 2 pc from 5.46 million during the same period in 2025."
  - p128 Cumulative visitor arrivals to Taiwan, January to August 2025 = **5,460,000** visitor arrivals (2025-01-01..2025-08-31) [keep: ] quote: "From January to August 2026, Taiwan recorded 5.56 million visitor arrivals, up 2 pc from 5.46 million during the same period in 2025."
  - p129 Total visitor arrivals to Taiwan, August 2025 = **673,102** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "Visitor arrivals to Taiwan declined 1.54 pc year-on-year to 662,735 in August this year, down from 673,102 in the same month last year."
  - p130 Total visitor arrivals to Taiwan, July 2025 = **586,226** visitor arrivals (2025-07-01..2025-07-31) [keep: ] quote: "607,534 in July 2026, up 3.63 pc from 586,226 in July."
  - p131 Foreign visitors (excluding Overseas Chinese) arrivals to Taiwan, August 2026 = **466,729** visitor arrivals (2026-08-01..2026-08-31) [DISCARD: August 2026 foreign vs overseas-Chinese split — no September split available; not usable for a September decomposition.] quote: "The arrivals included 466,729 foreign visitors, down 0.27 pc, and 196,006 Overseas Chinese visitors, down 4.43 pc."
  - p132 Overseas Chinese visitor arrivals to Taiwan, August 2026 = **196,006** visitor arrivals (2026-08-01..2026-08-31) [DISCARD: August 2026 overseas-Chinese split — no September split available.] quote: "The arrivals included 466,729 foreign visitors, down 0.27 pc, and 196,006 Overseas Chinese visitors, down 4.43 pc."
  - p133 Average length of stay of visitors leaving Taiwan, August 2026 = **7.68** nights (2026-08-01..2026-08-31) [DISCARD: Average length of stay — would only matter for a hotel-guest-night route, which lacks September 2026 guest-night data.] quote: "The average length of stay of visitors leaving Taiwan in August was 7.68 nights."
- `https://www.ntcunion.org/page/news/show.aspx?num=4536&root=2&page=5&kind=2&lang=TW` -> **live_dated** (page date 2025-06-16); points raw/verified 12/8
  - p134 Mid-Autumn Festival and Teachers' Day consecutive holiday length, 2026 = **4** days (2026-09-25..2026-09-28) [DISCARD: Holiday calendar — context only, no numeric role.] quote: "中秋節及孔子誕辰紀念日/教師節,9月25日至9月28日,連休4天。"
  - p135 Mid-Autumn Festival and Teachers' Day consecutive holiday end date, 2026 = **28** as written "9月28日", value check pending day of month (September) (2026-09-28..2026-09-28) [DISCARD: Holiday calendar — context only.] quote: "中秋節及孔子誕辰紀念日/教師節,9月25日至9月28日,連休4天。"
  - p136 National Day consecutive holiday length, 2026 = **3** days (2026-10-09..2026-10-11) [DISCARD: Holiday calendar — context only.] quote: "國慶日,10月9日至10月11日,連休3天。"
  - p137 National Day consecutive holiday end date, 2026 = **11** as written "10月11日", value check pending day of month (October) (2026-10-11..2026-10-11) [DISCARD: Holiday calendar — context only.] quote: "國慶日,10月9日至10月11日,連休3天。"
  - p138 New national holidays added in second half of 2025 (Teachers' Day, Taiwan Retroc = **3** national holidays (2025-07-01..2025-12-31) [DISCARD: Holiday calendar — context only.] quote: "114年下半年新增9月28日孔子誕辰紀念日/教師節、10月25日臺灣光復暨金門古寧頭大捷紀念日和12月25日行憲紀念日等3個國定假日"
  - p139 Additional 3-day consecutive holiday periods added in second half of 2025 = **2** consecutive holiday periods (2025-07-01..2025-12-31) [DISCARD: Holiday calendar — context only.] quote: "增加2個3天連續假期(併同例假日),教師節於次日9月29日補假"
  - p140 Teachers' Day makeup holiday date, 2025 = **29** as written "9月29日", value check pending day of month (September) (2025-09-29..2025-09-29) [DISCARD: Holiday calendar — context only.] quote: "教師節於次日9月29日補假,臺灣光復暨金門古寧頭大捷紀念日則於前一天10月24日補假。"
  - p141 Lunar New Year consecutive holiday length, 2026 = **9** days (2026-02-14..2026-02-22) [DISCARD: Holiday calendar — context only.] quote: "農曆春節假期,2月14日至2月22日,連休9天。"
- dropped by code checks: 5 (period_end 2026-12-31 after as_of: 3; value_as_written not in quote as a whole number: 2)

### b1 [own_history] September seasonal ratio

Hypothesis: The end-September YTD anchor (p111) gives September 2026 ≈ 610k only up to the ±5k rounding of the YTD. A published September 2025 monthly figure (and Sep 2023/2024) would let a September-to-August seasonal ratio route run independently and tighten the estimate.

Queries issued by the searcher: 觀光統計 來臺旅客 114年9月 觀光署; Tourism Administration Taiwan monthly statistics visitor arrivals September 2025; 113年9月觀光市場概況摘要 來臺旅客 人次; stat.taiwan.net.tw 來臺旅客人數 統計資料庫 中華民國統計 月別

- `https://admin.taiwan.net.tw/BusinessInfo/News?a=119&id=34979` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/BusinessInfo/News?a=119&id=32878` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://service.moea.gov.tw/EE521/common/Common.aspx?code=O&no=2` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b2 [related_series] September 2026 market-level data

Hypothesis: A September 2026 market breakdown (Japan, HK/Macau, Korea, Philippines, USA, Mainland) would let a sum-of-markets route run and reveal whether the September dip is broad or market-specific (e.g., typhoon-hit Japan/HK).

Queries issued by the searcher: 9月來臺旅客 主要客源 2026 觀光署; September 2026 Taiwan visitor arrivals by market Japan Hong Kong; 觀光署 115年9月 來臺旅客 統計 月報 居住地 日本 港澳; "9月" 來台旅客 2026 較去年同期 減少 颱風 日本 港澳 人次

- `https://www.motc.gov.tw/uploaddowndoc?file=month/27010.pdf&filedisplay=27010.pdf&flag=doc` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/11
  - p142 Total visitor arrivals to Taiwan, August 2026 (monthly) = **662,735** visitor arrivals (visits) (2026-08-01..2026-08-31) [DISCARD: Duplicate of August 2026 total p1.] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p143 Hong Kong/Macau arrivals to Taiwan, August 2026 = **137,560** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p144 Japan arrivals to Taiwan, August 2026 = **116,582** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p145 Mainland China arrivals to Taiwan, August 2026 = **67,303** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p146 Korea arrivals to Taiwan, August 2026 = **50,973** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p147 USA arrivals to Taiwan, August 2026 = **49,678** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p148 Europe arrivals to Taiwan, August 2026 = **32,613** visitor arrivals (visits) (2026-08-01..2026-08-31) [keep: ] quote: "歐洲旅客則有32,613人次"
  - p149 Cumulative visitor arrivals to Taiwan, January-July 2026 = **4,902,123** visitor arrivals (visits) (2026-01-01..2026-07-31) [DISCARD: Duplicate of Jan–Jul cumulative p3.] quote: "1至7月累計來台旅客為4,902,123人次"
  - p150 Cumulative visitor arrivals to Taiwan, January-August 2026 = **5,564,858** visitor arrivals (visits) (2026-01-01..2026-08-31) [DISCARD: Duplicate of Jan–Aug cumulative p4.] quote: "1至8月累計為5,564,858人次"
  - p151 Cumulative visitor arrivals to Taiwan, January-June 2026 = **4,294,589** visitor arrivals (visits) (2026-01-01..2026-06-30) [DISCARD: Duplicate of Jan–Jun cumulative p5.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p152 Total visitor arrivals to Taiwan, full year 2025 = **8,574,547** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Duplicate of 2025 full-year total p7.] quote: "2025年則是8,574,547人次,年增9.12%"
- `https://turnnewsapp.com/livenews/life/20261007004019-260405` -> **live_dated** (page date 2026-10-24); points raw/verified 9/8
  - p153 Cumulative visitor arrivals to Taiwan, January to end-September (current year),  = **6,175,000** visitor arrivals (visits) (2026-01-01..2026-09-30) [DISCARD: Duplicate of the end-September YTD anchor p111/p161; keep one.] quote: "截至9月來台旅客約617.5萬人次,與去年同期相比微幅成長"
  - p154 Cumulative visitor arrivals to Taiwan, January to end-September (current year),  = **6,175,000** visitor arrivals (visits) (2026-01-01..2026-09-30) [DISCARD: Duplicate of the end-September YTD anchor; keep one.] quote: "截至9月底,來台旅客約617.5萬人次,與去年同期相比成長1.93%"
  - p155 Year-on-year growth rate of cumulative visitor arrivals to Taiwan, January to en = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of the +1.93% YTD growth; keep p112/p162.] quote: "截至9月底,來台旅客約617.5萬人次,與去年同期相比成長1.93%"
  - p156 Share of weekday domestic-travel accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-24)) [DISCARD: Domestic accommodation subsidy budget usage; irrelevant to inbound visitor arrivals.] quote: "平日住宿經費已使用約24.95%,已用掉約4分之1經費"
  - p157 Fraction of weekday domestic-travel accommodation subsidy budget used (approx.) = **0.25** as written "4分之1", value check pending fraction of subsidy budget used (not stated (page dated 2026-10-24)) [DISCARD: Redundant restatement of p156 as a fraction; domestic subsidy, irrelevant.] quote: "平日住宿經費已使用約24.95%,已用掉約4分之1經費"
  - p158 Enterprise group tour registrations under subsidy scheme (count of groups) = **371** tour groups (not stated (page dated 2026-10-24)) [DISCARD: Enterprise domestic group-tour registrations; not inbound visitor arrivals.] quote: "像企業團報名已達371團,正由旅行社安排中"
  - p159 Repeat independent-travel international visitor applicants (count of people) = **49,000** applicants (people) (not stated (page dated 2026-10-24)) [DISCARD: Repeat-visitor program applications; program sign-ups, not September arrival events, and mostly post-September.] quote: "自由行重遊客現在約4.9萬人申請"
  - p160 Repeat group-tour international visitor groups (approx., count of groups) = **200** tour groups (not stated (page dated 2026-10-24)) [DISCARD: Repeat group-tour registrations; program sign-ups, not September arrivals.] quote: "重遊團體也有約200多團,國際客獎勵10月10日才上路"
- `https://tw.news.yahoo.com/%E5%A4%96%E7%B1%8D%E6%97%85%E5%AE%A2%E4%BE%86%E5%8F%B0%E9%87%8D%E9%81%8A%E5%AE%A2%E5%A2%9E-%E6%97%A5%E6%9C%AC%E6%B8%AF%E6%BE` -> **live_dated** (page date 2026-10-08); points raw/verified 14/11
  - p161 Total visitor arrivals to Taiwan, January-September cumulative (year of article, = **6,175,000** visitor arrivals (visits) (2026-01-01..2026-09-30) [DISCARD: Duplicate of the end-September YTD anchor p111; keep one.] quote: "根據交通部觀光署統計,今年1-9月來台旅客為617.5萬人次,與去年同期相比有1.93%的微幅成長。"
  - p162 Year-on-year growth rate of visitor arrivals to Taiwan, January-September cumula = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of the +1.93% YTD growth p112; keep one.] quote: "今年1-9月來台旅客為617.5萬人次,與去年同期相比有1.93%的微幅成長。"
  - p163 Total visitor arrivals to Taiwan, prior year (2025) full year = **8,570,000** visitor arrivals (visits) (2025-01-01..2025-12-31) [DISCARD: Rounded 2025 full-year total; redundant with the exact p7/p152.] quote: "交通部觀光署長陳玉秀說,去年來台旅客達857萬人次,其中重遊旅客比例達42%"
  - p164 Share of repeat visitors among visitor arrivals to Taiwan, prior year (2025) = **42** % (2025-01-01..2025-12-31) [DISCARD: Repeat-visitor share of 2025 arrivals; contextual only, not usable in a September 2026 level estimate.] quote: "去年來台旅客達857萬人次,其中重遊旅客比例達42%,已恢復至COVID-19(2019冠狀病毒疾病)疫情前重遊客水準"
  - p165 Registered repeat independent-travel visitors under reward program, cumulative a = **53,304** registered repeat visitors (persons) (..2026-10-07) [DISCARD: Cumulative reward registrations as of Oct 7; not September arrivals.] quote: "截至7日已有5萬3304名重遊旅客完成登記,並帶動1萬17名同行親友"
  - p166 Accompanying companions brought in by registered repeat visitors, cumulative as  = **10,017** accompanying companions (persons) (..2026-10-07) [DISCARD: Companions of registered repeat visitors; not September arrivals.] quote: "截至7日已有5萬3304名重遊旅客完成登記,並帶動1萬17名同行親友"
  - p167 Repeat independent-travel visitors registered, single day (the day before public = **4,652** registered repeat visitors (persons) (..2026-10-07) [DISCARD: Single-day registration count; program administration, not arrivals.] quote: "昨日單日就有4652名重遊旅客及896名同行親友完成登記,單日攜伴率達19.26%。"
  - p168 Accompanying companions registered, single day (the day before publication) = **896** accompanying companions (persons) (..2026-10-07) [DISCARD: Single-day companion registrations; not arrivals.] quote: "昨日單日就有4652名重遊旅客及896名同行親友完成登記,單日攜伴率達19.26%。"
  - p169 Single-day companion ratio (companions / repeat visitors registered that day) = **19.26** % (..2026-10-07) [DISCARD: Companion ratio; program metric, not arrivals.] quote: "昨日單日就有4652名重遊旅客及896名同行親友完成登記,單日攜伴率達19.26%。"
  - p170 Registered repeat visitors under reward program, cumulative as of the 7th (round = **53,000** registered repeat visitors (persons) (..2026-10-07) [DISCARD: Rounded repeat-visitor registrations; program metric, not arrivals.] quote: "截至7日已吸引5.3萬名旅客申請,帶動萬名親友來台,前5大市場為日本、港澳、韓國、新加坡及菲律賓。"
  - p171 Number of 7-ELEVEN stores offering reward redemption = **7,300** stores (not stated (page dated 2026-10-08)) [DISCARD: 7-ELEVEN store count for redemption; irrelevant to arrivals.] quote: "即可於期限內前往全台超過7300家7-ELEVEN門市"
- dropped by code checks: 8 (period_end 2026-12-31 after as_of: 5; scale word '萬' not supported by quote or table header: 1; period_end 2027-03-31 after as_of: 2)

### b3 [physical_flow] Taoyuan September actuals

Hypothesis: Actual (not forecast) Taoyuan September 2026 passenger and inbound-foreign counts, with a foreign-share factor, would provide an independent physical-flow cross-check on the ~610k figure.

Queries issued by the searcher: 桃園機場 2026年9月 旅運量 統計; Taoyuan airport September 2026 passenger statistics; 桃機 9月 旅運量 2026 統計 公布 旅客 萬人次; 觀光署 2026年9月 來台旅客 統計 桃園機場 入境

- `https://www.taoyuan-airport.com/news/C1CB08AC-9AAA-F111-BC31-0050569094FE?p=1&k=&s=&e=` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- `http://dev.taisounds.news/news/content/90/290835` -> **live_dated** (page date 2026-09-26); points raw/verified 15/15
  - p172 Taoyuan Airport passenger volume, cumulative first 2 days of Mid-Autumn holiday  = **288,000** passenger trips (2026-09-24..2026-09-25) [keep: ] quote: "桃園機場連假前2日累計疏運旅客達28.8萬人次,較去年同期成長6.0%。"
  - p173 Taoyuan Airport passenger volume year-on-year growth, first 2 days of Mid-Autumn = **6** % (2026-09-24..2026-09-25) [keep: ] quote: "桃園機場連假前2日累計疏運旅客達28.8萬人次,較去年同期成長6.0%。"
  - p174 Taoyuan Airport passenger volume, first 2 days of Mid-Autumn holiday (as listed  = **288,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Duplicate of Taoyuan holiday first-2-days volume p172.] quote: "桃園機場28.8萬人次(增6.0%)"
  - p175 Total main public transport system passenger volume, first 2 days of Mid-Autumn  = **2,836,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Total public transport passenger volume over holiday; domestic transport, not inbound visitors.] quote: "今年連假前2日主要公共運輸系統共疏運約283.6萬人次,較去年增加33.9萬人次"
  - p176 Increase in total main public transport passenger volume vs last year, first 2 d = **339,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Increase in public transport volume; domestic, not inbound.] quote: "今年連假前2日主要公共運輸系統共疏運約283.6萬人次,較去年增加33.9萬人次"
  - p177 Overall transport passenger volume increase vs last year, first 2 days of Mid-Au = **550,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Overall transport increase; domestic, not inbound.] quote: "整體疏運人次較去年同期大幅增加約55萬人次"
  - p178 Highway traffic volume estimate, first 2 days of Mid-Autumn holiday 2026 = **11,602,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Highway traffic volume; domestic, not inbound.] quote: "約有1160.2萬人次透過高速公路移動,增加21萬人次"
  - p179 Highway traffic volume increase vs last year, first 2 days of Mid-Autumn holiday = **210,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Highway traffic increase; domestic, not inbound.] quote: "約有1160.2萬人次透過高速公路移動,增加21萬人次"
  - p180 High-speed rail passenger volume, first 2 days of Mid-Autumn holiday 2026 = **664,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: High-speed rail passengers; domestic, not inbound.] quote: "高鐵疏運66.4萬人次(增23.5%)"
  - p181 High-speed rail passenger volume year-on-year growth, first 2 days of Mid-Autumn = **23.5** % (2026-09-24..2026-09-25) [DISCARD: HSR growth; domestic, not inbound.] quote: "高鐵疏運66.4萬人次(增23.5%)"
  - p182 Taiwan Railways passenger volume, first 2 days of Mid-Autumn holiday 2026 = **1,574,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Taiwan Railways passengers; domestic, not inbound.] quote: "臺鐵157.4萬人次(增10.9%)"
  - p183 Domestic air passenger volume, first 2 days of Mid-Autumn holiday 2026 = **40,000** passenger trips (2026-09-24..2026-09-25) [DISCARD: Domestic air passengers; not inbound international visitors.] quote: "國內航空4.0萬人次(增23.2%)"
  - p184 Domestic tourism trips on 2026-09-25 = **339,022** trips (2026-09-25..2026-09-25) [DISCARD: Domestic tourism trips on one day; not inbound arrivals.] quote: "9月25日國內旅遊人次達到33萬9022人次"
  - p185 High-speed rail trains operated on 2026-09-25 = **200** trains (2026-09-25..2026-09-25) [DISCARD: HSR train count; domestic, not inbound.] quote: "交通部9月25日協調高鐵開行200班列車(疏運31.6萬人次)"
  - p186 High-speed rail passengers carried on 2026-09-25 = **316,000** passenger trips (2026-09-25..2026-09-25) [DISCARD: HSR passengers on one day; domestic, not inbound.] quote: "高鐵開行200班列車(疏運31.6萬人次)"
- `https://tw.news.yahoo.com/%E6%A1%83%E6%A9%9F%E6%9A%91%E6%9C%9F%E9%81%8B%E9%87%8F%E5%89%B5%E6%96%B0%E9%AB%98-%E4%B8%AD%E7%A7%8B-%E6%95%99%E5%B8%AB%E7%A` -> **live_dated** (page date 2026-09-08); points raw/verified 14/11
  - p187 Taoyuan Airport summer (Jul-Aug) 2026 total passenger volume, cumulative = **8,600,000** passenger trips (2026-07-01..2026-08-31) [keep: ] quote: "桃園國際機場公司今天(8日)發布今年7-8月暑期旅運量達860萬人次"
  - p188 Taoyuan Airport summer (Jul-Aug) 2026 average daily passenger volume = **138,000** passenger trips per day (2026-07-01..2026-08-31) [keep: ] quote: "日均運量達13.8萬人次,創下歷年暑期新高"
  - p189 Taoyuan Airport summer (Jul-Aug) 2025 average daily passenger volume (prior year = **132,000** passenger trips per day (2025-07-01..2025-08-31) [keep: ] quote: "不僅超越去年同期13.2萬人次"
  - p190 Taoyuan Airport summer (Jul-Aug) 2019 pre-pandemic average daily passenger volum = **137,000** passenger trips per day (2019-07-01..2019-08-31) [keep: ] quote: "也超過2019年疫情前的13.7萬人次,刷新歷年暑假紀錄"
  - p191 Taoyuan Airport Jan-Jul 2026 cumulative passenger volume = **30,000,000** passenger trips (2026-01-01..2026-07-31) [keep: ] quote: "桃園機場今年1-7月的旅運量突破3,000萬人次後"
  - p192 Taoyuan Airport full-year 2019 passenger volume peak (comparison) = **48,000,000** passenger trips (2019-01-01..2019-12-31) [keep: ] quote: "超越2019年的4,800萬高峰"
  - p193 Taoyuan Airport Mid-Autumn/Teachers' Day holiday 6-day transport period total vo = **930,000** passenger trips (2026-09-23..2026-09-28) [keep: ] quote: "我們抓了6天的疏運,那這6天期間呢,我們預估桃機的總運量應該會突破93萬人次"
  - p194 Taoyuan Airport Mid-Autumn/Teachers' Day holiday 6-day transport period average  = **155,000** passenger trips per day (2026-09-23..2026-09-28) [keep: ] quote: "平均每天是15.5萬"
  - p195 Taoyuan Airport single-day peak passenger volume forecast during Mid-Autumn/Teac = **160,000** passenger trips per day (2026-09-23..2026-09-28) [keep: ] quote: "桃機預估單日旅運高峰將達16萬人次"
  - p196 Taoyuan Airport outbound daily peak forecast on Sep 24-25 (holiday first two day = **160,000** passenger trips per day (2026-09-24..2026-09-25) [keep: ] quote: "出境的高峰會落在9月24、25,也就是連假的前2天,每天大概平均會有16萬人次"
  - p197 Taoyuan Airport inbound daily peak forecast on Sep 28 (last day of holiday) = **158,000** passenger trips per day (2026-09-28..2026-09-28) [keep: ] quote: "入境的高峰則是會落在連假的最後一天9月28日,大概會到15.8萬人次"
- `https://www.mnews.tw/story/amp/20260924sot1347001` -> **live_dated** (page date 2026-09-24); points raw/verified 1/1
  - p198 Taoyuan Airport single-day maximum passenger volume during Mid-Autumn holiday pe = **160,000** passengers (人次) (2026-09-24..2026-09-28) [DISCARD: Duplicate of Taoyuan single-day peak forecast p195.] quote: "連假期間單日載客量超過16萬人次"
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan tourism', 'visitor arrivals', 'september arrivals']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p14', 'p15', 'p45', 'p46', 'p70', 'p90', 'p93', 'p119'] All report August 2026 total arrivals ≈660–663k with YoY ≈ -1.5%. p1/p119 (662,735) and p14/p45/p70/p90 (660,000 rounded) are the same Tourism Administration release; not independent measurements, jus
- corroborating: ['p4', 'p16', 'p47', 'p71', 'p91', 'p127'] Jan–Aug 2026 cumulative ≈5.56M, +2% YoY. Same MOTC release, rounded differently; p127 adds the 2025 comparator 5.46M.
- corroborating: ['p5', 'p6', 'p24', 'p26', 'p101'] Jan–Jun 2026 cumulative 4,294,589, +2.3% YoY — identical figure across outlets, one underlying release.
- corroborating: ['p18', 'p19', 'p49', 'p50', 'p72', 'p94', 'p97', 'p122'] May 2026 ≈692k, -2.6% YoY; p122 gives the precise 692,784 and the 2025 comparator 710,933.
- corroborating: ['p7', 'p8', 'p22', 'p23', 'p53', 'p54', 'p74', 'p98', 'p99'] Full-year 2025 = 8,574,547, +9.12%. Same annual release repeated; single underlying measurement.
- corroborating: ['p39', 'p40', 'p111', 'p112'] End-September 2026 YTD ≈6,175,000, +1.93% YoY. Two outlets, same Tourism Administration statement. This is the key anchor: it implies September 2026 ≈ 6,175,000 − 5,564,858 ≈ 610k, but the YTD is roun
- corroborating: ['p120', 'p121', 'p123', 'p124', 'p125', 'p126', 'p129', 'p130'] Monthly 2026 series Jan–Aug with 2025 comparators from one secondary aggregator (indiaoutbound). Internally consistent with the MOTC cumulative figures (sum of Jan–Aug months ≈5.56M) and with the repo
- conflicting: ['p1', 'p120'] p119 states August down 2% YoY while p1/p2 state -1.54%; minor rounding/transcription discrepancy in the same secondary article, not a real conflict.
- conflicting: ['p104', 'p105', 'p126'] p104 says January 2026 ≈1.2M with ~12% growth; p126 says 723,375 with +11.1%. The 1.2M figure is inconsistent with the Jan–Jun cumulative of 4.29M and with p126; p104 is a mis-stated/rounded level and
- corroborating: ['p56', 'p57', 'p60', 'p61', 'p62', 'p58', 'p59', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] Taoyuan Airport passenger volumes (both directions, residents + foreigners + transit). Useful as a capacity/seasonality cross-check for September (holiday-period daily volumes ~155–160k vs summer ~138
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89'] Typhoon-related flight cancellations in early/mid September 2026 (Matsu domestic, HK–Taipei, HK–Zhoushan). Small absolute magnitude relative to ~600k monthly arrivals; supports a small downward adjust
- corroborating: ['p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Visa-free extension for Thailand/Philippines/Brunei from 2026-08-01 and Cambodia removal — policy context affecting Southeast Asia source markets; direction mildly positive for Sep vs prior months.
- corroborating: ['p118', 'p116', 'p117', 'p115', 'p113', 'p114', 'p107', 'p108'] International visitor incentive program only started 2026-10-10, so it cannot affect September 2026 arrivals; useful mainly to rule out an upside driver for September.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p119', 'p142'] Same August 2026 total (662,735) reported by multiple outlets; identical figure, so one underlying Tourism Administration release, not independent confirmation.
- corroborating: ['p4', 'p150', 'p127'] Jan–Aug 2026 cumulative: 5,564,858 exact (p4, p150) vs 5.56 million rounded (p127); consistent, same source lineage.
- corroborating: ['p3', 'p149'] Jan–Jul 2026 cumulative 4,902,123 identical in both; same release.
- corroborating: ['p5', 'p151', 'p20', 'p51', 'p73', 'p95'] Jan–Jun 2026 cumulative 4,294,589 and Jan–May 3.68M with +2.6%/+2.3% growth; consistent overlapping YTD figures from the same Tourism Administration statistics.
- corroborating: ['p111', 'p112', 'p153', 'p154', 'p155', 'p161', 'p162'] End-September 2026 YTD ≈6,175,000 with +1.93% YoY, repeated across outlets; same underlying release, so a single anchor rather than multiple independent measurements.
- corroborating: ['p111', 'p4'] YTD Sep 6,175,000 minus YTD Aug 5,564,858 implies September ≈610k, consistent with a normal September level; the YTD anchor is the strongest single constraint on the target.
- corroborating: ['p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p1'] Monthly 2026 series Jan–Aug from one outlet; internally consistent with the YTD totals (sum matches p4/p150), so usable as the target's own monthly history.
- corroborating: ['p129', 'p130'] July/August 2025 monthly values used as prior-year comparators; consistent with the stated YoY percentages in p120 and p1.
- corroborating: ['p143', 'p144', 'p145', 'p146', 'p147', 'p148'] August 2026 market breakdown; sums to a large share of the 662,735 total, internally consistent, but only August — no September market split available.
- corroborating: ['p172', 'p173', 'p174', 'p193', 'p194', 'p195', 'p196', 'p197', 'p198'] Taoyuan Airport holiday-period volumes and forecasts; consistent with strong summer traffic (p187, p188) but these are total passengers (in+out, residents+transit), not visitor arrivals — usable only 
- corroborating: ['p187', 'p188', 'p189', 'p190', 'p191', 'p192'] Taoyuan summer 2026 daily average 138k vs 132k in 2025 and 137k in 2019; indicates inbound capacity at/above pre-pandemic, supporting a September near or slightly above 2025.
- corroborating: ['p7', 'p8', 'p152', 'p163'] 2025 full-year 8,574,547 (+9.12%) vs rounded 857万; consistent, provides prior-year scale.
- corroborating: ['p159', 'p160', 'p165', 'p166', 'p167', 'p168', 'p169', 'p170'] Repeat-visitor reward program registrations; these are program sign-ups (mostly October), not September arrivals, so only contextual for late-2026 demand.
- corroborating: ['p156', 'p157', 'p158'] Domestic subsidy and enterprise-tour program figures; domestic-side context, not directly the inbound target.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September share of the Jan–Sep cumulative arrivals | 0.0988 | 0.093..0.105 | 0.06987..0.1397 (widened) | fraction | m1 (m1) | September is a low-to-mid season month. With September 2026 implied near 610k against a ~6.175M Jan–Sep YTD, the share is close to 9.9%; the range covers month-to-month variation and the ±5k rounding of the YTD anchor. | The end-September YTD anchor (p111) is the correct cumulative and September 2026 is a normal-share month. | Evidence that September 2026 was unusually weak or strong relative to the Jan–Sep total (e.g. a market-specific collapse or surge). |
| a2 | September-to-August seasonal ratio for total visitor arrivals | 0.92 | 0.86..0.98 | 0.6492..1.298 (widened) | ratio | m2 (m2) | September typically runs below August in Taiwan inbound data (school term starts, fewer summer-family trips, typhoon exposure), while Mid-Autumn/Teachers' Day holidays add some inbound traffic. A ratio near 0.92 with a wide band reflects that September is a shoulder month. | August 2026 (p1) is a valid base and September 2026 follows a normal seasonal pattern. | A September 2026 level at or above August (e.g. a large holiday-driven surge or an August typhoon that depressed the base). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 614,333 | ['p111'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 609,788 | ['p1'] / ['a2'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p111 * a1; Monte Carlo P10 to P90 413,279 to 903,214; result unit visitor converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m2 formula_mc: p1 * a2; Monte Carlo P10 to P90 412,485 to 900,983; result unit visitor converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 614,333 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m2: 609,788 (width x/÷1.48, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.48; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.48.

Result: central **612,057** visitor, 80% interval [414,074, 904,702] visitor, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['motc', 'taiwan']; measure stems ['arriv', 'taiwa', 'visit']


## Final answer

The best estimate for total visitor arrivals to Taiwan during September 2026 is 612,057 visitor (80% model-based interval 414,074 to 904,702 visitor).

Two routes were combined with equal weight per block. The first decomposes the end-September year-to-date anchor of 6,175,000 visitor arrivals (visits) using an assumed September share of 0.0988 (range 0.06987 to 0.1397), giving 614,333 visitor. The second applies an assumed September-to-August ratio of 0.92 (range 0.6492 to 1.298) to the observed August level of 662,735 visitor arrivals (visits), giving 609,788 visitor. The two blocks share lineage, so they are not independent; equal weighting reflects that overlap rather than demonstrated accuracy.

Only the YTD anchor and August figure are observed; the September share and seasonal ratio are analyst assumptions. The main risk is an unusual September shock (typhoon, cross-strait policy) or a distorted August base. The most useful missing evidence would be early September daily arrival counts or airline load data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September share of the Jan–Sep cumulative arrivals: 0.0988 fraction, range 0.06987 to 0.1397 (range widened by code); used by m1. Overturned by: Evidence that September 2026 was unusually weak or strong relative to the Jan–Sep total (e.g. a market-specific collapse or surge).
- a2 September-to-August seasonal ratio for total visitor arrivals: 0.92 ratio, range 0.6492 to 1.298 (range widened by code); used by m2. Overturned by: A September 2026 level at or above August (e.g. a large holiday-driven surge or an August typhoon that depressed the base).

Method details (computed by code):
- m1 formula_mc: p111 * a1; Monte Carlo P10 to P90 413,279 to 903,214; result unit visitor converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m2 formula_mc: p1 * a2; Monte Carlo P10 to P90 412,485 to 900,983; result unit visitor converted to visitor; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 614,333 (width x/÷1.48, Monte Carlo of the formula inputs); B2 = m2: 609,788 (width x/÷1.48, Monte Carlo of the formula inputs). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.48; Birge ratio 0.02 (not above one, so no widening); final width x/÷1.48.

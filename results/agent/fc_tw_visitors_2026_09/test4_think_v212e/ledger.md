# Evidence ledger: fc_tw_visitors_2026_09

- Question: Assume today is 2026-10-24. You know nothing published after this date. Estimate the number of visitor arrivals to Taiwan (來臺旅客人次) in September 2026, as it will be first reported in the Ministry of Transportation and Communications' (Tourism Administration) monthly statistics on visitor arrivals and outbound departures (來臺旅客及國人出國人數).
- as_of: 2026-10-24
- Pinned target: Number of visitor arrivals to Taiwan (來臺旅客人次) during September 2026, as first reported in the Tourism Administration, MOTC monthly statistics on visitor arrivals and outbound departures; counted as arrival events (人次) of visitors entering Taiwan, not unique persons. | unit visitor arrivals (人次) in the month | period 2026-09-01..2026-09-30 | publisher Tourism Administration, Ministry of Transportation and Communications (MOTC), Taiwan

## Directions and pages

### d1 [own_history] Tourism Administration monthly statistical series

Hypothesis: September 2026 arrivals are anchored by recent 2026 monthly levels and prior September seasonal patterns. A usable relation is: target = recent monthly run-rate × September seasonal index × trend/recovery adjustment, with adjustments for calendar shifts and policy changes.

Queries issued by the searcher: site:admin.taiwan.net.tw 來臺旅客人次 2026; Taiwan Tourism Administration visitor arrivals September 2025 monthly statistics; admin.taiwan.net.tw Visitor Statistical Analysis for August 2026; 來臺旅客 2026年 7月 旅客人次 觀光署 統計

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://datalab.visitkorea.or.kr/common/board/Download.do?bcIdx=310092&cbIdx=1132&streFileNm=6ae48423-8669-433d-b730-e49d7c71e2c6.pdf` -> **live_dated** (page date 2025-12-31); points raw/verified 15/14
  - p1 Taiwan inbound visitor arrivals, September 2025 (monthly) = **601,339** visitor arrivals (人次) (2025-09-01..2025-09-30) [keep: ] quote: "9월 601,339 575,455 794,415 104.5% 75.7%"
  - p2 Taiwan inbound visitor arrivals, September 2024 (monthly) = **575,455** visitor arrivals (人次) (2024-09-01..2024-09-30) [keep: ] quote: "9월 601,339 575,455 794,415 104.5% 75.7%"
  - p3 Taiwan inbound visitor arrivals, September 2019 (monthly) = **794,415** visitor arrivals (人次) (2019-09-01..2019-09-30) [keep: ] quote: "9월 601,339 575,455 794,415 104.5% 75.7%"
  - p4 Taiwan inbound visitor arrivals, October 2025 (monthly) = **757,860** visitor arrivals (人次) (2025-10-01..2025-10-31) [keep: ] quote: "10월 757,860 661,115 939,131 114.6% 80.7%"
  - p5 Taiwan inbound visitor arrivals, January-October 2025 cumulative = **6,815,767** visitor arrivals (人次) (2025-01-01..2025-10-31) [keep: ] quote: "1~10월 6,815,767 6,206,267 9,730,507 109.8% 70.0%"
  - p6 Taiwan inbound visitor arrivals, January-October 2024 cumulative = **6,206,267** visitor arrivals (人次) (2024-01-01..2024-10-31) [keep: ] quote: "1~10월 6,815,767 6,206,267 9,730,507 109.8% 70.0%"
  - p7 Taiwan inbound visitor arrivals, January-October 2019 cumulative = **9,730,507** visitor arrivals (人次) (2019-01-01..2019-10-31) [keep: ] quote: "1~10월 6,815,767 6,206,267 9,730,507 109.8% 70.0%"
  - p8 Taiwan inbound visitor arrivals, full-year 2024 = **7,857,686** visitor arrivals (人次) (2024-01-01..2024-12-31) [keep: ] quote: "계 7,857,686 11,864,105"
  - p9 Taiwan inbound visitor arrivals, full-year 2019 = **11,864,105** visitor arrivals (人次) (2019-01-01..2019-12-31) [keep: ] quote: "계 7,857,686 11,864,105"
  - p10 Taiwan inbound visitor arrivals, November 2024 (monthly) = **747,800** visitor arrivals (人次) (2024-11-01..2024-11-30) [keep: ] quote: "11월 747,800 990,397"
  - p11 Taiwan inbound visitor arrivals, December 2024 (monthly) = **903,619** visitor arrivals (人次) (2024-12-01..2024-12-31) [keep: ] quote: "12월 903,619 1,143,201"
  - p12 Taiwan inbound visitor arrivals, January 2025 (monthly) = **651,078** visitor arrivals (人次) (2025-01-01..2025-01-31) [keep: ] quote: "1월 651,078 589,961 867,711 110.4% 75.0%"
  - p13 Taiwan inbound visitor arrivals, August 2025 (monthly) = **673,102** visitor arrivals (人次) (2025-08-01..2025-08-31) [keep: ] quote: "8월 673,102 616,922 1,030,937 109.1% 65.3%"
  - p14 Forecast Taiwan full-year 2025 inbound visitor arrivals (annual estimate) = **8,400,000** visitor arrivals (人次) (2025-01-01..2025-12-31) [keep: ] quote: "이에 따라 올해 전망치는 840만명에 불과할 것으로 예측되고 있는데"
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=35715` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d2 [related_series] Source-market decomposition

Hypothesis: Total visitor arrivals equal the sum of arrivals by source market. Major markets—Japan, Korea, Mainland China, Hong Kong/Macao, Southeast Asia, USA/Canada, Europe—have distinct recovery trends and flight links; recent market-level shares can transfer to September 2026.

Queries issued by the searcher: 臺灣 來臺旅客 按居住地 統計 2026 月別; Tourism Administration Taiwan visitor arrivals by country 2025 monthly statistics; 2026年8月 來臺旅客 統計 累計 1-8月 人次 觀光署; "9月" 來臺旅客 人次 2025年 觀光署 統計 月報 日本 港澳 韓國

- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/14
  - p15 Total visitor arrivals to Taiwan, August 2026 (monthly) = **662,735** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p16 Year-on-year change in total visitor arrivals, August 2026 vs August 2025 = **1.54** % (2026-08-01..2026-08-31) [keep: ] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p17 Cumulative visitor arrivals to Taiwan, January-August 2026 = **5,564,858** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Duplicate of the precise January-August 2026 cumulative p34.] quote: "1至7月累計來台旅客為4,902,123人次,加上8月月報數字後,1至8月累計為5,564,858人次"
  - p18 Cumulative visitor arrivals to Taiwan, January-July 2026 = **4,902,123** visitor arrivals (人次) (2026-01-01..2026-07-31) [keep: ] quote: "1至7月累計來台旅客為4,902,123人次"
  - p19 Cumulative visitor arrivals to Taiwan, January-June 2026 = **4,294,589** visitor arrivals (人次) (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p20 Year-on-year growth in cumulative visitor arrivals, January-June 2026 vs same pe = **2.3** % (2026-01-01..2026-06-30) [keep: ] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p21 Visitor arrivals from Hong Kong/Macao, August 2026 = **137,560** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p22 Visitor arrivals from Japan, August 2026 = **116,582** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p23 Visitor arrivals from Mainland China, August 2026 = **67,303** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p24 Visitor arrivals from Korea, August 2026 = **50,973** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p25 Visitor arrivals from USA, August 2026 = **49,678** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p26 Visitor arrivals from Europe, August 2026 = **32,613** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "歐洲旅客則有32,613人次"
  - p27 Total visitor arrivals to Taiwan, full year 2025 = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [keep: ] quote: "2025年則是8,574,547人次,年增9.12%"
  - p28 Total visitor arrivals to Taiwan, full year 2019 (pre-pandemic baseline) = **11,864,105** visitor arrivals (人次) (2019-01-01..2019-12-31) [keep: ] quote: "2019年全年來臺旅客達11,864,105人次"
- `https://www.cdnspg.com/articles/75718` -> **live_dated** (page date 2026-08-28); points raw/verified 15/0
- `https://unipro.tw/%e5%89%8d8%e5%80%8b%e6%9c%88556%e8%90%ac%e6%97%85%e5%ae%a2%e4%be%86%e8%87%ba-%e8%8f%b2%e3%80%81%e5%8d%b0%e6%97%85%e5%ae%a2%e5%a4%a7%` -> **live_dated** (page date 2026-10-02); points raw/verified 15/14
  - p29 August 2026 visitor arrivals to Taiwan (monthly total) = **660,000** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 total p15.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p30 August 2026 visitor arrivals to Taiwan (precise monthly total) = **662,735** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate precise August 2026 total; p15 already carries the same value.] quote: "8月國際旅客來臺達66萬2,735人次,較去年同期減少1.5%,較疫情前同期少35.7%"
  - p31 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p16's August 2026 year-on-year change.] quote: "8月國際旅客來臺達66萬2,735人次,較去年同期減少1.5%,較疫情前同期少35.7%"
  - p32 August 2026 visitor arrivals gap vs pre-pandemic same month = **35.7** % (2026-08-01..2026-08-31) [keep: ] quote: "8月國際旅客來臺達66萬2,735人次,較去年同期減少1.5%,較疫情前同期少35.7%"
  - p33 Jan-Aug 2026 cumulative visitor arrivals to Taiwan = **5,560,000** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of the precise January-August 2026 cumulative p34.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p34 Jan-Aug 2026 cumulative visitor arrivals to Taiwan (precise) = **5,564,858** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "1至8月來臺旅客達556萬4,858人次,比去年同期略增2%,較疫情前同期仍有30.4%的差距。"
  - p35 Jan-Aug 2026 cumulative visitor arrivals year-on-year growth = **2** % (2026-01-01..2026-08-31) [keep: ] quote: "1至8月來臺旅客達556萬4,858人次,比去年同期略增2%,較疫情前同期仍有30.4%的差距。"
  - p36 Jan-Aug 2026 cumulative visitor arrivals gap vs pre-pandemic = **30.4** % (2026-01-01..2026-08-31) [keep: ] quote: "1至8月來臺旅客達556萬4,858人次,比去年同期略增2%,較疫情前同期仍有30.4%的差距。"
  - p37 Jan-Aug 2026 Japan visitor arrivals (largest market) = **877,638** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "仍以日籍旅客87萬7,638人次最多,較去年略減1.5%,較疫情前少3成4"
  - p38 Jan-Aug 2026 Korea visitor arrivals = **623,070** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "韓國旅客達62萬3,070人次第二,年減2.2%,較疫情前少13.7%"
  - p39 Jan-Aug 2026 USA visitor arrivals = **504,907** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "美國50萬4,907人次第三,年增9.6%,較疫情前大增2成"
  - p40 Jan-Aug 2026 Philippines visitor arrivals = **495,920** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "1至8月菲律賓來臺旅客僅略低於美國,達49萬5,920人次,較去年同期增加22.7%、較2019年同期更是大幅增加5成"
  - p41 Jan-Aug 2026 Indonesia visitor arrivals = **173,803** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "印尼1至8月來臺旅客人次達到17萬3,803人次,較去年同期增加12.9%,較疫情前大增19.8%"
  - p42 Jan-Aug 2026 Vietnam visitor arrivals = **325,985** visitor arrivals (人次) (2026-01-01..2026-08-31) [keep: ] quote: "越南前8個月來臺旅客為32萬5,985人次,年增11.8%,較疫情前增加18%"
- dropped by code checks: 17 (period_end 2026-12-31 after as_of: 2; period year 2026 does not appear in the page text or URL (likely mis-dated): 15)

### d3 [physical_flow] Airport and immigration throughput

Hypothesis: International air arrivals at Taiwan airports are a physical flow closely related to visitor arrivals: visitor arrivals ≈ air visitor arrivals + sea visitor arrivals − resident returns − transit/transfer and crew/non-visitor entries. Air is dominant, so airport arrival counts constrain the target.

Queries issued by the searcher: 桃園機場 2026年9月 旅客運量 入境; Taiwan airport international arrivals September 2026 statistics Taoyuan; 觀光署 2026年9月 來臺旅客 統計 人次; 桃園機場 2026年9月 旅運量 統計 萬人次 公布

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/7
  - p43 Cumulative visitor arrivals to Taiwan, January to end of September (current year = **6,175,000** visitor arrivals (人次) (2026-01-01..2026-09-30) [keep: ] quote: "截至9月来台旅客约617.5万人次,与去年同期相比微幅成长"
  - p44 Year-on-year growth rate of cumulative visitor arrivals to Taiwan, January to en = **1.93** % (2026-01-01..2026-09-30) [keep: ] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p45 Share of domestic-travel weekday accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Domestic weekday-accommodation subsidy share; irrelevant to inbound visitor arrivals.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p46 Share of domestic-travel weekday accommodation subsidy budget used (stated as fr = **0.25** as written "4分之1", value check pending % (budget used / total subsidy budget) (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the domestic subsidy share p45.] quote: "目前该经费已使用约4分之1"
  - p47 Number of independent-travel repeat visitors who have applied for the internatio = **49,000** applicants (people) (not stated (page dated 2026-10-07)) [DISCARD: Repeat-visitor applicant count; not a September 2026 inbound visitor-arrival measure.] quote: "自由行重游客现在约4.9万人申请"
  - p48 Number of repeat-visitor group tours (stated as 200-plus) = **200** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Repeat group-tour count; irrelevant to the monthly inbound total.] quote: "重游团体也有约200多团"
  - p49 Number of corporate group tour registrations = **371** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Corporate group-tour registration count; irrelevant to the monthly inbound total.] quote: "像企业团报名已达371团"
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 12/11
  - p50 August 2026 visitor arrivals to Taiwan (monthly total, as reported by Tourism Ad = **660,000** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 total p15.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p51 Year-on-year change in August 2026 visitor arrivals to Taiwan = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 year-on-year change p16.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p52 Cumulative January-August 2026 visitor arrivals to Taiwan = **5,560,000** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of the January-August 2026 cumulative p34.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p53 Year-on-year growth in cumulative January-August 2026 visitor arrivals to Taiwan = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of the January-August 2026 growth statement p35.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p54 May 2026 inbound visitor arrivals to Taiwan (monthly total) = **692,000** visitor arrivals (人次) (2026-05-01..2026-05-31) [DISCARD: Rounded duplicate of the precise May 2026 total p123.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p55 Year-on-year change in May 2026 inbound visitor arrivals to Taiwan = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of the May 2026 year-on-year change p103.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p56 Cumulative January-May 2026 inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (人次) (2026-01-01..2026-05-31) [DISCARD: Rounded intermediate January-May 2026 cumulative; superseded by precise later cumulative and monthly points.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p57 Year-on-year growth in cumulative January-May 2026 inbound visitor arrivals to T = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Duplicate of the January-May 2026 growth statement.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p58 Full-year 2025 visitor arrivals to Taiwan (from 114-year survey) = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 total p27.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p59 Year-on-year growth in full-year 2025 visitor arrivals to Taiwan = **9.12** % (2025-01-01..2025-12-31) [keep: ] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p60 Japanese visitor arrivals to Taiwan through September 25, 2025 (cumulative) = **1,000,000** as written "百萬", value check pending visitor arrivals (人次) (2025-01-01..2025-09-25) [DISCARD: Mis-dated or duplicate Japan milestone evidence: it conflicts with p207 and duplicates the 2026 event in p206.] quote: "今年日本旅客來臺人次至9月25日已經突破百萬"
- `https://www.taoyuan-airport.com/news/C1CB08AC-9AAA-F111-BC31-0050569094FE?p=1&k=&s=&e=` -> **live_dated** (page date 2020-01-01); points raw/verified 0/0
- `https://www.sjtv.com.tw/articles/104691?lang=zh_TW` -> **dropped** (live fetch error URLError); points raw/verified -/-
- dropped by code checks: 2 (period_end 2026-12-31 after as_of: 1; number: scale conflict: '百萬' in value vs '萬': 1)

### d4 [capacity_consumption] Airline capacity and utilisation

Hypothesis: Scheduled international seat capacity to Taiwan multiplied by realised load factor and the share of arriving passengers who are visitors gives a capacity-based estimate: arrivals ≈ seats × load factor × visitor share. Route launches, cuts, and aircraft upgauges affect September 2026 capacity.

Queries issued by the searcher: Taiwan international seat capacity September 2026; 桃園機場 載客率 國際航線 座位數 2025; 2026年9月 台灣 國際航線 載客率 座位總數; 來臺旅客人次 2026年9月 觀光署 統計

- `https://www.aeroroutes.com/cht/260901-sep26tpehkg` -> **live_dated** (page date 2026-09-01); points raw/verified 12/0
- `https://routes.skyfaring.net/stats/quarterly/` -> **live_dated** (page date 2026-10-20); points raw/verified 15/15
  - p61 Taiwan international and cross-strait scheduled routes total seats, 2026 Q3 (thr = **12,783,747** seats (2026-07-01..2026-08-31) [keep: ] quote: "座位供給 12,783,747 年增 +3.3%"
  - p62 Taiwan international and cross-strait scheduled routes total passengers carried, = **10,814,373** passengers (2026-07-01..2026-08-31) [keep: ] quote: "載客人數 10,814,373 年增 +7.8%"
  - p63 Taiwan international and cross-strait scheduled routes average load factor, 2026 = **84.6** % (2026-07-01..2026-08-31) [keep: ] quote: "平均載客率 84.6% 年增 +3.5 個百分點"
  - p64 Taiwan international and cross-strait scheduled routes total flights, 2026 Q3 (t = **51,890** flights (2026-07-01..2026-08-31) [keep: ] quote: "飛行架次 51,890 年增 +3.2% · 比 2025 年 Q3同期"
  - p65 Taoyuan Airport (TPE) scheduled seats, 2026 Q3 (through August) = **10,208,384** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 102 \| 39,466 \| 10,208,384 \| 84.4% \| -0.6% \| +0.2% \|"
  - p66 Taoyuan Airport (TPE) load factor, 2026 Q3 (through August) = **84.4** % (2026-07-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 102 \| 39,466 \| 10,208,384 \| 84.4% \| -0.6% \| +0.2% \|"
  - p67 Kaohsiung Airport (KHH) scheduled seats, 2026 Q3 (through August) = **1,440,498** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 高雄機場KHH \| 31 \| 7,164 \| 1,440,498 \| 83.6% \| +13.0% \| +15.8% \|"
  - p68 Songshan Airport (TSA) load factor, 2026 Q3 (through August) = **91.8** % (2026-07-01..2026-08-31) [keep: ] quote: "\| 松山機場TSA \| 10 \| 2,357 \| 568,271 \| 91.8% \| -2.6% \| -2.3% \|"
  - p69 Taichung Airport (RMQ) scheduled seats, 2026 Q3 (through August) = **554,534** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 台中機場RMQ \| 19 \| 2,836 \| 554,534 \| 83.9% \| +62.1% \| +62.1% \|"
  - p70 Tainan Airport (TNN) scheduled seats, 2026 Q3 (through August) = **12,060** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 台南機場TNN \| 2 \| 67 \| 12,060 \| 88.6% \| - \| - \|"
  - p71 Japan routes scheduled seats, 2026 Q3 (through August) = **3,560,994** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 日本 \| 30 \| 15,545 \| 3,560,994 \| 90.4% \| +4.5% \|"
  - p72 Hong Kong routes load factor, 2026 Q3 (through August) = **76** % (2026-07-01..2026-08-31) [keep: ] quote: "\| 香港 \| 1 \| 6,132 \| 1,553,831 \| 76.0% \| +0.9% \|"
  - p73 South Korea routes scheduled seats, 2026 Q3 (through August) = **1,283,441** seats (2026-07-01..2026-08-31) [keep: ] quote: "\| 南韓 \| 6 \| 5,988 \| 1,283,441 \| 90.9% \| +17.3% \|"
  - p74 All Taiwan international and cross-strait scheduled routes total seats, 2026 Q2 = **18,800,828** seats (2026-04-01..2026-06-30) [keep: ] quote: "\| 2026 年 Q2 \| 76,387 \| 18,800,828 \| 15,687,649 \| 83.4% \| +4.8% \|"
  - p75 All Taiwan international and cross-strait scheduled routes load factor, 2025 Q3 = **78.9** % (2025-07-01..2025-09-30) [keep: ] quote: "\| 2025 年 Q3 \| 74,155 \| 18,241,978 \| 14,385,161 \| 78.9% \| +7.2% \|"
- `https://jazztalk.tw/taiwan-airport-passenger-load-factor-in-september-2025/` -> **live_dated** (page date 2025-11-04); points raw/verified 14/14
  - p76 Total scheduled seats, all Taiwan international and cross-strait airports, Septe = **5,869,746** seats (2025-09-01..2025-09-30) [keep: ] quote: "- 座位總數: 5,869,746 個"
  - p77 Total passengers, all Taiwan international and cross-strait airports, September  = **4,348,747** passenger trips (人次) (2025-09-01..2025-09-30) [keep: ] quote: "- 旅客總數: 4,348,747 人次"
  - p78 National average load factor, all Taiwan international and cross-strait airports = **74.1** % (2025-09-01..2025-09-30) [keep: ] quote: "- 全國平均載客率: 74.1%"
  - p79 International routes (incl. Hong Kong/Macau) average load factor, September 2025 = **73.7** % (2025-09-01..2025-09-30) [keep: ] quote: "- 國際航線(含港澳)平均載客率: 73.7%"
  - p80 Cross-strait routes average load factor, September 2025 = **77.7** % (2025-09-01..2025-09-30) [keep: ] quote: "- 兩岸航線平均載客率: 77.7%"
  - p81 Total international and cross-strait flights, all Taiwan airports, September 202 = **23,865** flights (架次) (2025-09-01..2025-09-30) [keep: ] quote: "- 航班架次總數: 23,865 架次"
  - p82 Taoyuan International Airport (TPE) scheduled seats, international and cross-str = **4,818,531** seats (2025-09-01..2025-09-30) [keep: ] quote: "提供了 4,818,531 個座位,總載客數為 3,537,571 人次,平均載客率為 73.4 %"
  - p83 Taoyuan International Airport (TPE) passengers, international and cross-strait,  = **3,537,571** passenger trips (人次) (2025-09-01..2025-09-30) [keep: ] quote: "提供了 4,818,531 個座位,總載客數為 3,537,571 人次,平均載客率為 73.4 %"
  - p84 Taoyuan International Airport (TPE) average load factor, September 2025 = **73.4** % (2025-09-01..2025-09-30) [keep: ] quote: "提供了 4,818,531 個座位,總載客數為 3,537,571 人次,平均載客率為 73.4 %"
  - p85 Kaohsiung International Airport (KHH) scheduled seats, international and cross-s = **594,949** seats (2025-09-01..2025-09-30) [keep: ] quote: "提供了 594,949 個座位,總載客數為 437,251 人次,平均載客率為 73.5 %"
  - p86 Kaohsiung International Airport (KHH) passengers, international and cross-strait = **437,251** passenger trips (人次) (2025-09-01..2025-09-30) [keep: ] quote: "提供了 594,949 個座位,總載客數為 437,251 人次,平均載客率為 73.5 %"
  - p87 Taipei Songshan Airport (TSA) scheduled seats, international and cross-strait, S = **286,134** seats (2025-09-01..2025-09-30) [keep: ] quote: "提供了 286,134 個座位,總載客數為 242,255 人次,平均載客率為 84.7 %"
  - p88 Taichung International Airport (RMQ) scheduled seats, international and cross-st = **164,372** seats (2025-09-01..2025-09-30) [keep: ] quote: "提供了 164,372 個座位,總載客數為 129,881 人次,平均載客率為 79.0 %"
  - p89 Hualien Airport (HUN) scheduled seats, international flights, September 2025 = **5,760** seats (2025-09-01..2025-09-30) [keep: ] quote: "提供了 5,760 個座位,總載客數為 1,789 人次,平均載客率為 31.1%"
- `https://www.motc.gov.tw/en/app/data/doc?id=2392&module=mebook&detailNo=1&serno=202411060001&type=s` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 12 (period year 2026 does not appear in the page text or URL (likely mis-dated): 12)

### d5 [administrative] National Immigration Agency entry records

Hypothesis: Immigration inbound entry counts by nationality and purpose are administrative traces that closely track visitor arrivals. A stable calibration ratio can be estimated from overlapping historical months: visitor arrivals ≈ foreign visitor entries × coverage adjustment.

Queries issued by the searcher: 內政部移民署 2026年9月 入境 人數 統計 外籍; National Immigration Agency Taiwan inbound arrivals statistics monthly 2026; 觀光統計月報 2026年9月 來臺旅客 人次 觀光署; 移民署 入出境統計 月報 2026 9月 入境人數

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 9/8
  - p90 Cumulative visitor arrivals to Taiwan, January to September (as of end-September = **6,175,000** visitor arrivals (人次) (2026-01-01..2026-09-30) [DISCARD: Duplicate of the January-September 2026 cumulative p43.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p91 Year-on-year growth rate of cumulative visitor arrivals to Taiwan, January to Se = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of the January-September 2026 growth statement p44.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p92 Cumulative visitor arrivals to Taiwan, January to September (as of September), s = **6,175,000** visitor arrivals (人次) (2026-01-01..2026-09-30) [DISCARD: Duplicate of the January-September 2026 cumulative p43.] quote: "截至9月来台旅客约617.5万人次,与去年同期相比微幅成长"
  - p93 Share of domestic weekday accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the domestic subsidy share p45.] quote: "平日住宿经费已使用约24.95%,已用掉约4分之1经费"
  - p94 Share of domestic weekday accommodation subsidy budget used, stated as fraction = **0.25** as written "4分之1", value check pending share of subsidy budget (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the domestic subsidy share p46.] quote: "目前该经费已使用约4分之1"
  - p95 Number of corporate group tour registrations under the scheme = **371** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the corporate group-tour count p49.] quote: "像企业团报名已达371团,正由旅行社安排中"
  - p96 Number of repeat independent-travel visitors who applied for the international r = **49,000** applicants (persons) (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the repeat-visitor applicant count p47.] quote: "自由行重游客现在约4.9万人申请"
  - p97 Number of repeat group tours under the international repeat-visitor incentive = **200** tour groups (not stated (page dated 2026-10-07)) [DISCARD: Duplicate of the repeat group-tour count p48.] quote: "重游团体也有约200多团"
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 14/10
  - p98 August 2026 visitor arrivals to Taiwan (monthly, Tourism Administration) = **660,000** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 total p15.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p99 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of the August 2026 year-on-year change p16.] quote: "8月來臺旅客為66萬人次,年減1.5%"
  - p100 January-August 2026 cumulative visitor arrivals to Taiwan = **5,560,000** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of the January-August 2026 cumulative p34.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p101 January-August 2026 cumulative visitor arrivals year-on-year change = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of the January-August 2026 growth statement p35.] quote: "1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p102 May 2026 inbound visitor arrivals to Taiwan (monthly) = **692,000** visitor arrivals (人次) (2026-05-01..2026-05-31) [DISCARD: Rounded duplicate of the May 2026 total p123.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p103 May 2026 inbound visitor arrivals year-on-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of the May 2026 year-on-year change p55.] quote: "5月入境旅客約69.2萬人次,年減2.6%"
  - p104 January-May 2026 cumulative inbound visitor arrivals = **3,680,000** visitor arrivals (人次) (2026-01-01..2026-05-31) [DISCARD: Rounded duplicate of the January-May 2026 cumulative p56.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p105 January-May 2026 cumulative inbound visitor arrivals year-on-year change = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Duplicate of the January-May 2026 growth statement p57.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p106 2025 (114年) full-year visitor arrivals to Taiwan = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 total p27.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p107 2025 full-year visitor arrivals year-on-year change = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 growth statement p59.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
- `https://statis.motc.gov.tw/MAIN/ForeignService/ProgSource/TSDSFS01_01v2.jsp?type=13&rptid=702&lang=en` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.immigration.gov.tw/media/67188/%E5%85%A7%E6%94%BF%E9%83%A8%E7%A7%BB%E6%B0%91%E7%BD%B2107%E5%B9%B4%E5%A0%B1.pdf` -> **dropped** (live fetch error URLError); points raw/verified -/-
- dropped by code checks: 5 (period_end 2026-12-31 after as_of: 2; number: scale conflict: '百萬' in value vs '萬': 1; number: unknown scale word '成': 1; number: scale conflict: '萬' in value vs '百萬': 1)

### d6 [forecasts_markets] Official targets and plans

Hypothesis: Tourism Administration annual 2026 visitor-arrival targets or forecasts, combined with year-to-date actuals, imply a required or planned September-December run-rate. Targets may be aspirational, so use them as bounds or context rather than direct observations.

Queries issued by the searcher: 觀光署 2026年 來臺旅客 目標 千萬人次; Taiwan 2026 visitor arrivals target Tourism Administration; 觀光署 2026年 1至8月 來台旅客 累計 人次 統計; 2025年9月 來台旅客 人次 觀光署 統計 月報

- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/8
  - p108 2026 Jan-Aug cumulative visitor arrivals = **5,564,858** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Duplicate of the precise January-August 2026 cumulative p34.] quote: "1至7月累計來台旅客為4,902,123人次,加上8月月報數字後,1至8月累計為5,564,858人次。"
  - p109 2026 August monthly visitor arrivals = **662,735** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of the August 2026 total p15.] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p110 2026 Jan-Jul cumulative visitor arrivals = **4,902,123** visitor arrivals (人次) (2026-01-01..2026-07-31) [DISCARD: Duplicate of the January-July 2026 cumulative p18.] quote: "1至7月累計來台旅客為4,902,123人次"
  - p111 2026 Jan-Jun cumulative visitor arrivals = **4,294,589** visitor arrivals (人次) (2026-01-01..2026-06-30) [DISCARD: Duplicate of the January-June 2026 cumulative p19.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p112 2025 full-year visitor arrivals = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [DISCARD: Duplicate of full-year 2025 total p27.] quote: "2025年則是8,574,547人次,年增9.12%"
  - p113 2019 full-year visitor arrivals (pre-pandemic baseline) = **11,864,105** visitor arrivals (人次) (2019-01-01..2019-12-31) [DISCARD: Duplicate of full-year 2019 total p28.] quote: "2019年全年來臺旅客達11,864,105人次"
  - p114 2026 August visitor arrivals year-on-year change rate = **1.54** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of the August 2026 year-on-year change p16.] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p115 2026 Jan-Jun visitor-arrival growth rate (year-on-year) = **2.3** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of the January-June 2026 growth statement p20.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
- `https://www.chinatimes.com/cn/realtimenews/20260820004113-260405?chdtv` -> **dropped** (live fetch error URLError); points raw/verified -/-
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=36381` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://indiaoutbound.info/trade-news/tourist-arrivals-in-taiwan-drop-2pc-in-august-to-about-663000/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/15
  - p116 Taiwan visitor arrivals, August 2026 (monthly total) = **662,735** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of the August 2026 total p15.] quote: "Taiwan recorded 662,735 visitor arrivals in August 2026, down 2 pc year-on-year"
  - p117 Taiwan visitor arrivals, January to August 2026 (cumulative YTD) = **5,560,000** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of the January-August 2026 cumulative p34.] quote: "From January to August 2026, Taiwan recorded 5.56 million visitor arrivals, up 2 pc from 5.46 million during the same period in 2025."
  - p118 Taiwan visitor arrivals, January to August 2025 (cumulative YTD, comparison) = **5,460,000** visitor arrivals (人次) (2025-01-01..2025-08-31) [keep: ] quote: "up 2 pc from 5.46 million during the same period in 2025"
  - p119 Taiwan visitor arrivals, January 2026 (monthly) = **723,375** visitor arrivals (人次) (2026-01-01..2026-01-31) [keep: ] quote: "Monthly arrivals stood at 723,375 in January, up 11.1 pc from 651,078 in January 2025"
  - p120 Taiwan visitor arrivals, February 2026 (monthly) = **625,608** visitor arrivals (人次) (2026-02-01..2026-02-28) [keep: ] quote: "625,608 in February, down 10.52 pc from 699,158 in February 2025"
  - p121 Taiwan visitor arrivals, March 2026 (monthly) = **883,061** visitor arrivals (人次) (2026-03-01..2026-03-31) [keep: ] quote: "883,061 in March 2026, up 13.42 pc from 778,576 in March 2025"
  - p122 Taiwan visitor arrivals, April 2026 (monthly) = **758,613** visitor arrivals (人次) (2026-04-01..2026-04-30) [keep: ] quote: "758,613 in April, up 0.99 pc from 751,149 in April 2025"
  - p123 Taiwan visitor arrivals, May 2026 (monthly) = **692,784** visitor arrivals (人次) (2026-05-01..2026-05-31) [keep: ] quote: "692,784 in May, down 2.55 pc from 710,933 in May 2025"
  - p124 Taiwan visitor arrivals, June 2026 (monthly) = **611,148** visitor arrivals (人次) (2026-06-01..2026-06-30) [keep: ] quote: "611,148 in June, up 0.79 pc from 606,346 in June 2025"
  - p125 Taiwan visitor arrivals, July 2026 (monthly) = **607,534** visitor arrivals (人次) (2026-07-01..2026-07-31) [keep: ] quote: "607,534 in July 2026, up 3.63 pc from 586,226 in July."
  - p126 Taiwan visitor arrivals, August 2025 (same month prior year) = **673,102** visitor arrivals (人次) (2025-08-01..2025-08-31) [DISCARD: Duplicate of August 2025 total p13.] quote: "down from 673,102 in the same month last year"
  - p127 Foreign visitors to Taiwan, August 2026 (monthly component) = **466,729** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "The arrivals included 466,729 foreign visitors, down 0.27 pc"
  - p128 Overseas Chinese visitors to Taiwan, August 2026 (monthly component) = **196,006** visitor arrivals (人次) (2026-08-01..2026-08-31) [keep: ] quote: "196,006 Overseas Chinese visitors, down 4.43 pc"
  - p129 Air-travel share of Taiwan total arrivals, August 2026 (visitors entering by air = **93.46** % (visitors entering by air / total arrivals) (2026-08-01..2026-08-31) [keep: ] quote: "Air travel accounted for 93.46 pc of total arrivals, with 619,389 visitors entering by air."
  - p130 Average length of stay of visitors leaving Taiwan, August 2026 = **7.68** nights (2026-08-01..2026-08-31) [keep: ] quote: "The average length of stay of visitors leaving Taiwan in August was 7.68 nights."
- dropped by code checks: 7 (period_end 2026-12-31 after as_of: 4; number: scale conflict: '千' in value vs '萬': 2; value_as_written not in quote as a whole number: 1)

### d7 [shocks] Policy, weather and calendar effects

Hypothesis: September 2026 arrivals may be shifted by typhoon/earthquake airport closures, mainland China group-tour or visa policy, visa-free programme changes, major events, and airline route changes. These should adjust the run-rate or widen uncertainty; measurable exposure (closure days, cancelled seats, policy start dates) matters more than headlines.

Queries issued by the searcher: 2026年9月 來臺旅客 人次 觀光署 統計; Taiwan typhoon September 2026 airport closures tourism arrivals; 2026年9月 來台旅客 人數 觀光署 統計 9月 單月 人次 2026; 中國 團客 來台 2026 政策 開放 陸客

- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **dropped** (live fetch error URLError); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **dropped** (live fetch error URLError); points raw/verified -/-
- `https://alvin.travel/en/article/safety/taiwan-typhoon-season-2026` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://arabic.euronews.com/video/2026/10/23/taiwan-deadly-typhoon-champi-causes-travel-chaos-and-school-closures` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### d8 [base_rates] Seasonality and calendar adjustment

Hypothesis: September has a recurring seasonal position relative to adjacent months and the annual total. A seasonal index from pre-COVID and recent years can convert a 2026 run-rate into a September estimate, adjusted for lunar-calendar shifts such as Mid-Autumn Festival timing.

Queries issued by the searcher: Taiwan monthly visitor arrivals seasonality 2019 2024 觀光署 來臺旅客 月別統計; 觀光署 來臺旅客 2025 月別 統計 人次; 觀光署 2026年 來臺旅客 月別 統計 1月至8月 人次; "Visitor Statistical Analysis" September 2025 Tourism Administration visitors Taiwan 601

- `https://www.motc.gov.tw/uploaddowndoc?file=month/27010.pdf&filedisplay=27010.pdf&flag=doc` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://indiaoutbound.info/trade-news/tourist-arrivals-in-taiwan-drop-2pc-in-august-to-about-663000/` -> **dropped** (live fetch error URLError); points raw/verified -/-
- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **dropped** (live fetch error URLError); points raw/verified -/-
- `https://www.bella.tw/articles/travel&foodies/55531/taiwan-top10-2025` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b1 [base_rates] administrative

Hypothesis: The exact first-release September 2026 monthly visitor-arrival count from the Tourism Administration would eliminate the rounding in the January-September cumulative p43 and directly replace the m1 difference with an observed monthly value.

Queries issued by the searcher: site:admin.taiwan.net.tw 2026年9月 來臺旅客; "2026年9月" "來臺旅客" "人次"; 2026年9月 來台旅客 單月 萬人次 觀光署 統計; 觀光署 統計資料 來臺旅客 2026年9月 人數 統計表; "來臺旅客" "9月" 2026 "61" 萬人次 觀光署 公布; admin.taiwan.net.tw 來臺旅客人數 統計 月 2026 9月 xlsx 中華民國115年

- `https://admin.taiwan.net.tw/News/News?a=35&id=35939&p=5` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/News/News?a=35&id=36193&p=3` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/News/News?a=35&id=35916&p=5` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://admin.taiwan.net.tw/siraya-nsa/NewsSiraya/NewsTravel?a=822&id=35939` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b2 [base_rates] physical_flow

Hypothesis: September 2026 scheduled seats, passengers, and load factor at Taiwan airports would test whether the August year-on-year change used in m2 transfers to September and would provide a capacity-based cross-check.

Queries issued by the searcher: routes.skyfaring.net Taiwan September 2026 seats; 桃園機場 2026年9月 座位數 載客率; routes.skyfaring.net 2026年8月 民航局月報 座位天; 民航局 民航統計月報 2026年8月 國際航線 客運 載客率

- `https://routes.skyfaring.net/airport/tpe/` -> **live_dated** (page date 2009-09-01); points raw/verified 15/15
  - p131 Taoyuan Airport total weekly scheduled seats, August 2026 = **5,218,808** seats (2026-08-01..2026-08-31) [DISCARD: Mislabeled duplicate of p146: same seat value but described as weekly; p146 gives the clear August monthly seat total.] quote: "座位供給 5,218,808 4,365,882 人次"
  - p132 Taoyuan Airport total monthly scheduled seats (20,186 flights/month), August 202 = **4,365,882** seats (2026-08-01..2026-08-31) [DISCARD: Mislabeled capacity/passenger field; the quote's second value is not a clean scheduled-seat measure and is derivable fro] quote: "座位供給 5,218,808 4,365,882 人次"
  - p133 Taoyuan Airport average load factor, August 2026 = **83.7** % (2026-08-01..2026-08-31) [keep: ] quote: "平均載客率 83.7% 架次年增率 +1.2%"
  - p134 Taoyuan Airport weekly flight count, August 2026 = **4,558** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "每週班次 4,558 20,186 架次/月"
  - p135 Taoyuan Airport monthly flight count, August 2026 = **20,186** flights per month (2026-08-01..2026-08-31) [keep: ] quote: "每週班次 4,558 20,186 架次/月"
  - p136 Taoyuan Airport flight count year-on-year change, August 2026 = **1.2** % (2026-08-01..2026-08-31) [keep: ] quote: "平均載客率 83.7% 架次年增率 +1.2%"
  - p137 Taoyuan direct-flight destinations count, August 2026 = **101** destinations (2026-08-01..2026-08-31) [keep: ] quote: "101 個航點 · 56 家航空 · 每週 4,558 班 · 2026 年 8 月"
  - p138 Airlines serving Taoyuan direct destinations, August 2026 = **56** airlines (2026-08-01..2026-08-31) [keep: ] quote: "101 個航點 · 56 家航空 · 每週 4,558 班 · 2026 年 8 月"
  - p139 Northeast Asia share of Taoyuan weekly flights, August 2026 = **39** % (2026-08-01..2026-08-31) [keep: ] quote: "班次最多的是東北亞,佔 39%,最滿的一條是雪梨 96.7%,最空的是亞庇 53.7%。"
  - p140 Taipei–Northeast Asia weekly flights, August 2026 = **1,766** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東北亞 35 航點23 家航空每週 1,766.5 班載客率 90.6%"
  - p141 Taipei–Northeast Asia load factor, August 2026 = **90.6** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛東北亞 35 航點23 家航空每週 1,766.5 班載客率 90.6%"
  - p142 Taipei–Hong Kong/Macau weekly flights, August 2026 = **628** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛港澳 2 航點8 家航空每週 627.5 班載客率 78.6%"
  - p143 Taipei–Hong Kong/Macau load factor, August 2026 = **78.6** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛港澳 2 航點8 家航空每週 627.5 班載客率 78.6%"
  - p144 Taipei–China mainland weekly flights, August 2026 = **418** flights per week (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛中國大陸 14 航點13 家航空每週 418 班載客率 83.1%"
  - p145 Taipei–China mainland load factor, August 2026 = **83.1** % (2026-08-01..2026-08-31) [keep: ] quote: "台北直飛中國大陸 14 航點13 家航空每週 418 班載客率 83.1%"
- `https://routes.skyfaring.net/for/agency/tpe/` -> **live_dated** (page date 2026-10-20); points raw/verified 15/15
  - p146 Taoyuan Airport total scheduled seats, August 2026 = **5,218,808** seats (2026-08-01..2026-08-31) [keep: ] quote: "5,218,808 個座位 · 28 個國家與地區 · 本月新開 1 條 · 停飛 1 條"
  - p147 Number of countries/regions served from Taoyuan, August 2026 = **28** countries/regions (2026-08-01..2026-08-31) [keep: ] quote: "5,218,808 個座位 · 28 個國家與地區 · 本月新開 1 條 · 停飛 1 條"
  - p148 Taoyuan–Japan scheduled seats, August 2026 = **1,359,351** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 日本 \| 30 \| 15 \| 1,293 \| 1,359,351 \| +1.0% \|"
  - p149 Taoyuan–Japan seats year-on-year change, August 2026 = **1** % (2026-08-01..2026-08-31) [keep: ] quote: "\| 日本 \| 30 \| 15 \| 1,293 \| 1,359,351 \| +1.0% \|"
  - p150 Taoyuan–Hong Kong scheduled seats, August 2026 = **579,230** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 香港 \| 1 \| 7 \| 511 \| 579,230 \| -0.0% \|"
  - p151 Taoyuan–USA scheduled seats, August 2026 = **473,830** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 美國 \| 10 \| 5 \| 335 \| 473,830 \| +4.7% \|"
  - p152 Taoyuan–South Korea scheduled seats, August 2026 = **471,356** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 南韓 \| 5 \| 13 \| 473 \| 471,356 \| +13.9% \|"
  - p153 Taoyuan–China mainland scheduled seats, August 2026 = **465,487** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 中國大陸 \| 14 \| 13 \| 418 \| 465,487 \| +2.9% \|"
  - p154 Taoyuan–Thailand scheduled seats, August 2026 = **346,703** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 泰國 \| 4 \| 8 \| 295 \| 346,703 \| -0.4% \|"
  - p155 Taoyuan–Vietnam scheduled seats, August 2026 = **337,729** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 越南 \| 5 \| 7 \| 299 \| 337,729 \| -0.5% \|"
  - p156 Taoyuan–Philippines scheduled seats, August 2026 = **265,927** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 菲律賓 \| 3 \| 7 \| 223.5 \| 265,927 \| -10.2% \|"
  - p157 Taoyuan–Singapore scheduled seats, August 2026 = **192,634** seats (2026-08-01..2026-08-31) [keep: ] quote: "\| 新加坡 \| 1 \| 5 \| 134 \| 192,634 \| -6.6% \|"
  - p158 Taoyuan–Busan load factor, August 2026 = **93.4** % (2026-08-01..2026-08-31) [keep: ] quote: "\| 桃園-釜山 \| 南韓 \| 107,969 \| 172,784 \| +60.0% \| 93.4% \|"
  - p159 Taoyuan–Fukuoka load factor, August 2026 = **94.1** % (2026-08-01..2026-08-31) [keep: ] quote: "\| 桃園-福岡 \| 日本 \| 108,564 \| 131,152 \| +20.8% \| 94.1% \|"
  - p160 Taoyuan–Sapporo scheduled seats, August 2026 (shrinking route) = **93,458** seats (2026-08-01..2026-08-31) [keep: ] quote: "-桃園-札幌 座位 113,866 → 93,458.載客率 94.7%"
- `https://routes.skyfaring.net/stats/yearly/` -> **live_dated** (page date 2026-10-20); points raw/verified 15/15
  - p161 Taiwan international and cross-strait scheduled flights, cumulative Jan-Aug 2026 = **205,753** flights (2026-01-01..2026-08-31) [keep: ] quote: "2026 年至 8 月 \| 205,753 \| 50,594,916 \| 42,767,426 \| 84.5% \| +5.2%"
  - p162 Taiwan international and cross-strait scheduled seats, cumulative Jan-Aug 2026 = **50,594,916** seats (2026-01-01..2026-08-31) [keep: ] quote: "2026 年至 8 月 \| 205,753 \| 50,594,916 \| 42,767,426 \| 84.5% \| +5.2%"
  - p163 Taiwan international and cross-strait passengers carried, cumulative Jan-Aug 202 = **42,767,426** passengers (2026-01-01..2026-08-31) [keep: ] quote: "2026 年至 8 月 \| 205,753 \| 50,594,916 \| 42,767,426 \| 84.5% \| +5.2%"
  - p164 Taiwan international and cross-strait average load factor, cumulative Jan-Aug 20 = **84.5** % (2026-01-01..2026-08-31) [keep: ] quote: "2026 年至 8 月 \| 205,753 \| 50,594,916 \| 42,767,426 \| 84.5% \| +5.2%"
  - p165 Taiwan international and cross-strait flights YoY change, cumulative Jan-Aug 202 = **5.2** % (2026-01-01..2026-08-31) [keep: ] quote: "2026 年至 8 月 \| 205,753 \| 50,594,916 \| 42,767,426 \| 84.5% \| +5.2%"
  - p166 Taiwan international and cross-strait seats YoY change, cumulative Jan-Aug 2026  = **5.1** % (2026-01-01..2026-08-31) [keep: ] quote: "座位供給 50,594,916 年增 +5.1%"
  - p167 Taiwan international and cross-strait passengers YoY change, cumulative Jan-Aug  = **11.1** % (2026-01-01..2026-08-31) [keep: ] quote: "載客人數 42,767,426 年增 +11.1%"
  - p168 Taiwan international and cross-strait average load factor YoY change, cumulative = **4.5** percentage points (2026-01-01..2026-08-31) [keep: ] quote: "平均載客率 84.5% 年增 +4.5 個百分點"
  - p169 Taoyuan Airport (TPE) scheduled seats, cumulative Jan-Aug 2026 = **40,793,842** seats (2026-01-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 107 \| 158,022 \| 40,793,842 \| 84.5% \| +2.4% \| +2.9% \|"
  - p170 Taoyuan Airport (TPE) flights, cumulative Jan-Aug 2026 = **158,022** flights (2026-01-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 107 \| 158,022 \| 40,793,842 \| 84.5% \| +2.4% \| +2.9% \|"
  - p171 Taoyuan Airport (TPE) load factor, cumulative Jan-Aug 2026 (passengers / seats) = **84.5** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 107 \| 158,022 \| 40,793,842 \| 84.5% \| +2.4% \| +2.9% \|"
  - p172 Taoyuan Airport (TPE) seats YoY change, cumulative Jan-Aug 2026 vs 2025 same mon = **2.9** % (2026-01-01..2026-08-31) [keep: ] quote: "\| 桃園機場TPE \| 107 \| 158,022 \| 40,793,842 \| 84.5% \| +2.4% \| +2.9% \|"
  - p173 Kaohsiung Airport (KHH) scheduled seats, cumulative Jan-Aug 2026 = **5,543,239** seats (2026-01-01..2026-08-31) [keep: ] quote: "\| 高雄機場KHH \| 34 \| 28,059 \| 5,543,239 \| 82.5% \| +14.1% \| +16.2% \|"
  - p174 Taiwan international and cross-strait scheduled seats, full year 2025 = **72,664,367** seats (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 年 \| 295,787 \| 72,664,367 \| 58,335,936 \| 80.3% \| +8.8% \|"
  - p175 Taiwan international and cross-strait passengers carried, full year 2025 = **58,335,936** passengers (2025-01-01..2025-12-31) [keep: ] quote: "\| 2025 年 \| 295,787 \| 72,664,367 \| 58,335,936 \| 80.3% \| +8.8% \|"
- `https://skyfaring.net/projects/` -> **live_dated** (page date 2026-01-01); points raw/verified 0/0

### b3 [base_rates] related_series

Hypothesis: September 2026 source-market arrivals would show whether the August market mix and the year-to-date growth carried into September, reducing uncertainty in the yoy_scaling routes that transfer August or January-August growth.

Queries issued by the searcher: 2026年9月 來臺旅客 人次 觀光署; 2025年9月 來臺旅客 統計 日本 港澳 人次; "Visitor Statistical Analysis for September 2026" Taiwan Tourism Administration; 2026年8月 來台旅客 人次 統計 觀光署 日本 港澳 韓國

- `https://appi.news/articles/taiwan-inbound-tourism-recovery-2026/` -> **live_dated** (page date 2026-10-04); points raw/verified 15/13
  - p176 August 2026 visitor arrivals to Taiwan, total = **662,735** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p15 with no additional precision.] quote: "2026年8月來台旅客為662,735人次,較2025年同月減少1.54%"
  - p177 August 2026 visitor arrivals, Hong Kong/Macao source market = **137,560** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p21.] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p178 August 2026 visitor arrivals, Japan source market = **116,582** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p22.] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p179 August 2026 visitor arrivals, Mainland China source market = **67,303** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p23.] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p180 August 2026 visitor arrivals, Korea source market = **50,973** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p24.] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p181 August 2026 visitor arrivals, USA source market = **49,678** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p25.] quote: "主要客源包括港澳137,560人次、日本116,582人次、中國大陸67,303人次、韓國50,973人次、美國49,678人次"
  - p182 August 2026 visitor arrivals, Europe source market = **32,613** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Duplicate of p26.] quote: "歐洲旅客則有32,613人次"
  - p183 January-August 2026 cumulative visitor arrivals = **5,564,858** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Duplicate of p34.] quote: "1至8月累計為5,564,858人次"
  - p184 January-July 2026 cumulative visitor arrivals = **4,902,123** visitor arrivals (人次) (2026-01-01..2026-07-31) [DISCARD: Duplicate of p18.] quote: "1至7月累計來台旅客為4,902,123人次"
  - p185 January-June 2026 cumulative visitor arrivals = **4,294,589** visitor arrivals (人次) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p19.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p186 January-June 2026 cumulative visitor arrivals year-on-year growth rate = **2.3** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of p20.] quote: "2026年1至6月累計來台旅客為4,294,589人次,較2025年同期成長2.3%"
  - p187 August 2026 visitor arrivals year-on-year change rate = **1.54** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p16.] quote: "2026年8月共有662,735名旅客入境,較2025年8月少1.54%"
  - p188 2025 full-year visitor arrivals to Taiwan = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p27.] quote: "2025年則是8,574,547人次,年增9.12%"
- `https://www.chinatimes.com/cn/realtimenews/20261007004019-260405?chdtv` -> **live_dated** (page date 2026-10-07); points raw/verified 8/7
  - p189 Cumulative visitor arrivals to Taiwan, January to September (as of end-September = **6,175,000** visitor arrivals (人次) (2026-01-01..2026-09-30) [DISCARD: Duplicate of p43.] quote: "截至9月底,来台旅客约617.5万人次"
  - p190 Year-on-year growth of cumulative visitor arrivals to Taiwan, January to Septemb = **1.93** % (2026-01-01..2026-09-30) [DISCARD: Duplicate of p44.] quote: "截至9月底,来台旅客约617.5万人次,与去年同期相比成长1.93%"
  - p191 Share of weekday accommodation subsidy budget used = **24.95** % (not stated (page dated 2026-10-07)) [DISCARD: Domestic-travel subsidy budget share; irrelevant to inbound visitor arrivals.] quote: "平日住宿经费已使用约24.95%"
  - p192 Share of weekday accommodation subsidy budget used, stated as fraction = **0.25** as written "4分之1", value check pending % (not stated (page dated 2026-10-07)) [DISCARD: Alternative expression of p191; irrelevant to inbound visitor arrivals.] quote: "目前该经费已使用约4分之1"
  - p193 Number of corporate group tour registrations under subsidy scheme = **371** 团 (groups) (not stated (page dated 2026-10-07)) [DISCARD: Corporate tour registration count under a subsidy scheme; not an arrival count and not convertible.] quote: "像企业团报名已达371团"
  - p194 Number of repeat-visit independent traveller applications (approx.) = **49,000** people (not stated (page dated 2026-10-07)) [DISCARD: Repeat-visitor application count; not an arrival count and not safely convertible.] quote: "自由行重游客现在约4.9万人申请"
  - p195 Number of repeat-visit group tour applications (approx., stated as 200-plus) = **200** 团 (groups) (not stated (page dated 2026-10-07)) [DISCARD: Repeat group-tour application count; not an arrival count and not safely convertible.] quote: "重游团体也有约200多团"
- `https://admin.taiwan.net.tw/english/info/News?a=1329&id=34978` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e4%ba%a4%e9%80%9a%e9%83%a8%e8%a7%80%e5%85%89%e7%bd%b2/` -> **live_dated** (page date 2026-10-05); points raw/verified 14/13
  - p196 August 2026 visitor arrivals to Taiwan (monthly total) = **660,000** visitor arrivals (人次) (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p15 with less precision.] quote: "觀光署29日公布8月來臺旅客為66萬人次,年減1.5%"
  - p197 August 2026 visitor arrivals year-on-year change = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p16 with less precision.] quote: "8月來臺旅客為66萬人次,年減1.5%"
  - p198 January-August 2026 cumulative visitor arrivals to Taiwan = **5,560,000** visitor arrivals (人次) (2026-01-01..2026-08-31) [DISCARD: Rounded duplicate of p34 with less precision.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p199 January-August 2026 cumulative visitor arrivals year-on-year change = **2** % (2026-01-01..2026-08-31) [DISCARD: Duplicate of p35.] quote: "今年1至8月來臺旅客達556萬人次,較去年同期增加2%"
  - p200 May 2026 inbound visitor arrivals to Taiwan = **692,000** visitor arrivals (人次) (2026-05-01..2026-05-31) [DISCARD: Rounded duplicate of p123.] quote: "觀光署日前公布5月入境旅客約69.2萬人次,年減2.6%"
  - p201 May 2026 inbound visitor arrivals year-on-year change = **2.6** % (2026-05-01..2026-05-31) [DISCARD: Duplicate of the May 2026 yoy change already implied by p123.] quote: "5月入境旅客約69.2萬人次,年減2.6%"
  - p202 January-May 2026 cumulative inbound visitor arrivals to Taiwan = **3,680,000** visitor arrivals (人次) (2026-01-01..2026-05-31) [DISCARD: Rounded cumulative value derivable from p119-p123; p18/p19 provide cleaner cumulative checks.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p203 January-May 2026 cumulative inbound visitor arrivals year-on-year change = **2.6** % (2026-01-01..2026-05-31) [DISCARD: Duplicate growth rate for p202.] quote: "1至5月累計入境旅客達368萬人次,較去年同期增加2.6%"
  - p204 2025 full-year visitor arrivals to Taiwan = **8,574,547** visitor arrivals (人次) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p27.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p205 2025 full-year visitor arrivals year-on-year change = **9.12** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p59.] quote: "去年來臺旅客為857萬4,547人次,年增9.12%"
  - p206 Japan visitor arrivals to Taiwan through September 25, 2026 (cumulative) = **1,000,000** as written "百萬", value check pending visitor arrivals (人次) (2026-01-01..2026-09-25) [keep: ] quote: "今年日本旅客來臺人次至9月25日已經突破百萬,相較於去年在10月下旬達成,時間提早一個月"
  - p207 Japan visitor arrivals to Taiwan reaching one million in 2025 (date) = **10** month (late October) (2025-10-21..2025-10-31) [keep: ] quote: "相較於去年在10月下旬達成,時間提早一個月"
  - p208 January-September 2025 domestic hotel guests year-on-year increase = **2** % (year-on-year increase) (2025-01-01..2025-09-30) [DISCARD: Domestic hotel guest growth; irrelevant to inbound visitor arrivals.] quote: "本國住客更覺疫情前同期大增2成"
- dropped by code checks: 4 (period_end 2026-12-31 after as_of: 3; number: scale conflict: '百萬' in value vs '萬': 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan tourism', 'visitor arrivals', 'tourism statistics']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p27', 'p28'] Historical Taiwan monthly and annual visitor arrivals from one external compilation of official Taiwan statistics. They establish the pre-2026 level and the August-to-September seasonal drop (p1 vs p1
- corroborating: ['p15', 'p30', 'p109', 'p116'] August 2026 total 662,735 appears in several news copies; exact agreement is expected because they trace the same Tourism Administration release. Treat as one measurement, not four independent observa
- duplicate: ['p29', 'p50', 'p98'] Rounded '66萬' versions of the August 2026 total; less precise than p15/p30 and redundant.
- corroborating: ['p16', 'p31', 'p51', 'p99', 'p114'] August 2026 year-on-year change around -1.5%; p16 gives the precise -1.54%, while the others are rounded duplicates. Consistent with p15 vs p13, but not an independent measurement.
- corroborating: ['p17', 'p34', 'p108'] January-August 2026 cumulative 5,564,858 appears in multiple articles from the same official figure. p17 and p108 are duplicate copies of p34.
- duplicate: ['p33', 'p52', 'p100', 'p117'] Rounded 5.56 million versions of the January-August 2026 cumulative; redundant with p34.
- corroborating: ['p35', 'p53', 'p101'] January-August 2026 cumulative growth about +2%; consistent with p34 and p118. p53/p101 are duplicate statements.
- corroborating: ['p43', 'p90', 'p92'] January-September 2026 cumulative about 6.175 million repeated in the same article; p90/p92 are duplicates. The 'about' wording implies rounding and is the main uncertainty in the direct subtraction r
- corroborating: ['p44', 'p91'] January-September 2026 cumulative year-on-year growth +1.93%; duplicate statements. Consistent with p43 and the 2025 baseline, but not independent.
- corroborating: ['p127', 'p128', 'p129'] August 2026 foreign and overseas-Chinese components sum to the total, and air share/air visitors are internally consistent with p15. Same release, so this is within-measurement corroboration.
- contextual: ['p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42'] August 2026 major-market breakdown and January-August 2026 market-level YTD totals. Different periods and partial market coverage; useful for market mix but not a direct September total.
- contextual: ['p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73'] 2026 Q3-through-August capacity and load-factor data. Same source and period July-August 2026, not September. Useful for capacity trend but not a direct visitor count.
- contextual: ['p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89'] Capacity and passenger statistics for 2025 Q3, September 2025, and 2026 Q2. Period and scope differ from the target and from p61-p73; load-factor differences are partly seasonal and partly vintage, no
- contextual: ['p14', 'p27', 'p59'] 2025 forecast was 8.4 million while actual full-year 2025 was 8,574,547 (+9.12%). The forecast understated actual, so Tourism Administration forecasts should be treated as context or bounds, not reali
- contextual: ['p45', 'p46', 'p47', 'p48', 'p49', 'p93', 'p94', 'p95', 'p96', 'p97'] Domestic-travel subsidy and repeat-visitor incentive program counts. Unrelated to the September 2026 inbound monthly total and not convertible without additional take-up/arrival data.
- contextual: ['p60'] Japan cumulative through 25 September 2025 milestone. Different year and partial period from 2026; market context only, not a total visitor-arrival measure.
- contextual: ['p18', 'p19', 'p20', 'p32', 'p36'] Intermediate 2026 cumulative totals and pre-pandemic gap measures. They are consistent with later cumulative points but cover different periods and do not directly identify September 2026.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p43', 'p44', 'p34', 'p35', 'p5', 'p4', 'p1', 'p118'] These are the strongest reconciliation points. p43 gives an approximate Jan-Sep 2026 cumulative, p44 gives its reported yoy growth, p34 gives a precise Jan-Aug 2026 cumulative, and p5 minus p4 reconst
- corroborating: ['p15', 'p16', 'p13', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p127', 'p128', 'p129'] August 2026 total arrivals, August yoy change, August 2025 comparison, source-market levels, foreign/overseas-Chinese components, and air share are mutually consistent. The foreign and overseas-Chines
- corroborating: ['p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p18', 'p19', 'p34', 'p15', 'p43'] The 2026 monthly path and cumulative totals are internally consistent: the monthly values reconcile with p18 and p19, p34 extends through August, and p43 is the only point that extends into September.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p10', 'p11', 'p12', 'p13', 'p8', 'p27', 'p28', 'p9'] Historical September, adjacent-month, and annual totals from the same Taiwan inbound visitor series are consistent across vintages. September 2025 p1 is below August 2025 p13 and well below October 20
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p34', 'p35', 'p32', 'p36'] January-August 2026 source-market data show a mixed but plausible composition: Japan and Korea slightly down, USA and several Southeast Asian markets up. This is consistent with the roughly 2% cumulat
- corroborating: ['p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p146', 'p133', 'p135', 'p166', 'p167', 'p168'] Capacity and passenger-flow points are internally consistent for September 2025 and for 2026 Q3/Jan-Aug growth. However, they measure scheduled seats, total passengers, and load factors, not visitor a
- corroborating: ['p206', 'p207'] Japanese arrivals through September 25, 2026 reached one million, earlier than the late-October timing in 2025. This supports the view that September 2026 was not weaker than the August yoy signal alo
- conflicting: ['p60'] p60 states Japanese arrivals through September 25, 2025 reached one million, but p207 says the 2025 one-million milestone occurred in late October. p60 is probably a mis-dated duplicate of p206 rather
- contextual: ['p14', 'p27', 'p59'] The 2025 forecast of 8.4 million was below the actual 8.574 million, so annual forecast/target figures should be treated as context or bounds, not as direct September substitutes.
- conflicting: ['p131', 'p132'] These Taoyuan entries are mislabeled or ambiguous: p131 duplicates the August 2026 seat total but is called weekly, while p132 appears to place a passenger count in a seats field. They should not be u
- irrelevant: ['p191', 'p192', 'p193', 'p194', 'p195', 'p208'] These are domestic-travel subsidy budget shares, repeat-visitor application counts, corporate tour registrations, or domestic hotel guests. They do not directly measure inbound visitor arrivals and ca

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 611,006 | ['p43', 'p34'] / [] | [] |  | 0.50 | B1 of 4 blocks; median of blocks: this block is the median |  |
| m2 | yoy_scaling | 592,077 | ['p1', 'p15', 'p13'] / [] | [] |  | 0.00 | B2 of 4 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | yoy_scaling | 612,888 | ['p1', 'p34', 'p118'] / [] | [] |  | 0.00 | B3 of 4 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m4 | formula_mc | 606,312 | ['p5', 'p4', 'p44', 'p34'] / [] | [] |  | 0.50 | B4 of 4 blocks; median of blocks: this block is the median |  |

- m1 coverage: the whole target
- m4 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: a - b; Monte Carlo P10 to P90 -909,830 to 2,150,675; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 yoy_scaling: target 2025 601,339 x signal 662,735 / 673,102 (growth 0.9846); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 yoy_scaling: target 2025 601,339 x signal 5,564,858 / 5,460,000 (growth 1.0192); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m4 formula_mc: (a - b) * (1 + c) - d; Monte Carlo P10 to P90 -1,012,222 to 2,305,158; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 4 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 611,006 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 592,077 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 612,888 (width x/÷1.38, no error evidence, code's default width); B4 = m4: 606,312 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.06 (not above one, so no widening); final width x/÷1.38.
- Seasonal naive baseline (not combined): 601,339 (2025, from m2); the estimate is +1.2% against it.

Result: central **608,655** visitor, 80% interval [441,803, 838,520] visitor, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['taiwan']; measure stems ['arriv', 'taiwa', 'visit']


## Final answer

The best estimate for visitor arrivals to Taiwan (人次, arrival events, not unique persons) during September 2026, as first reported by the Tourism Administration, MOTC, is 608,655 visitor (80% model-based interval 441,803 to 838,520 visitor).

Main evidence: the precise January–August 2026 cumulative 5,564,858 visitor arrivals (人次) is subtracted from the rounded January–September cumulative 6,175,000 visitor arrivals (人次) to isolate September (m1, 611,006 visitor, weight 50%); a growth-based reconciliation using 6,815,767 visitor arrivals (人次), 757,860 visitor arrivals (人次), 1.93% and 5,564,858 visitor arrivals (人次) gives m4 (606,312 visitor, weight 50%). Two yoy transfers from the September 2025 base 601,339 visitor arrivals (人次) use August momentum (m2, 592,077 visitor) and YTD growth (m3, 612,888 visitor).

The combination is the median of four equal-weight blocks, with overlapping inputs grouped; no backtest errors were available, so widths are default. The key risk is that 6,175,000 visitor arrivals (人次) is rounded and preliminary, and that August momentum was negative while YTD growth was positive. A precise first-release September figure or historical backtests would most improve the estimate.

Key assumptions: none (every formula input is an observed data point).

Method details (computed by code):
- m1 formula_mc: a - b; Monte Carlo P10 to P90 -909,830 to 2,150,675; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 yoy_scaling: target 2025 601,339 x signal 662,735 / 673,102 (growth 0.9846); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 yoy_scaling: target 2025 601,339 x signal 5,564,858 / 5,460,000 (growth 1.0192); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m4 formula_mc: (a - b) * (1 + c) - d; Monte Carlo P10 to P90 -1,012,222 to 2,305,158; result unit visitor converted to visitor; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 4 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 611,006 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 592,077 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 612,888 (width x/÷1.38, no error evidence, code's default width); B4 = m4: 606,312 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.06 (not above one, so no widening); final width x/÷1.38.
- Seasonal naive baseline (not combined): 601,339 (2025, from m2); the estimate is +1.2% against it.

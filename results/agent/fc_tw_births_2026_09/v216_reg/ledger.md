# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan (Republic of China) during September 2026, as counted in the Ministry of the Interior's monthly household registration statistics (births registered in the month, by date of registration) | unit births registered in September 2026 | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior, Republic of China (Taiwan) — Department of Household Registration, monthly bulletin of interior statistics

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household registration statistics time series

Hypothesis: September births registered in recent years (2019-2025) plus the 2026 year-to-date monthly pattern establish the level and the September seasonal factor; September typically shows a modest seasonal bump relative to August. Target = recent monthly level × September seasonal index, adjusted for the 2026 trend.

Queries issued by the searcher: 內政部 戶政司 出生 登記 統計 月 114年; Taiwan monthly births registered 2025 2026 MOI statistics; 內政部統計月報 1.2 現住人口出生、死亡、結婚、離婚登記 114年7月; 台灣 出生數 歷年 每月 2019 2020 2021 2022 2023 2024 統計 各月 出生人數; 內政部 戶政司 出生 登記 統計 月 中華民國 統計月報; Taiwan monthly births registered 2026 MOI household registration statistics; 台灣 2025年 每月 出生數 內政部 1月 2月 3月 4月 5月 6月 7月 8月 9月 新生兒 統計; 中華民國統計資訊網 統計月報 出生數 自然增加 月 113年 114年; 內政部 戶政司 出生登記 統計 月 2026; Taiwan monthly births registered 2026 MOI household registration statistics; 2025年9月 新生兒 出生數 內政部 戶口統計 9月; ris.gov.tw 出生死亡及結離婚月表 按登記日期 統計

- `https://focustaiwan.tw/society/202606100011` -> **snapshot** (snapshot 20260721035109); points raw/verified 15/14
  - p1 Taiwan births registered in May (monthly total) = **6,832** births (2026-05-01..2026-05-31) [keep: ] quote: "Taiwan recorded 6,832 births in May, the second-lowest monthly total on record after February's all-time low of 6,523"
  - p2 Taiwan births registered in February (all-time monthly low) = **6,523** births (2026-02-01..2026-02-28) [keep: ] quote: "the second-lowest monthly total on record after February's all-time low of 6,523"
  - p3 Taiwan births registered in April = **8,144** births (2026-04-01..2026-04-30) [keep: ] quote: "MOI data showed Taiwan had 6,832 births in May, compared with 8,144 in April and 8,433 a year earlier"
  - p4 Consecutive months of year-on-year decline in Taiwan births (streak length) = **29** months (not stated (page dated 2026-06-10)) [DISCARD: Streak length, not a birth count; no numerical role.] quote: "extending a 29-month streak of year-on-year declines in births"
  - p5 Taiwan crude birth rate in May (births per 1,000 people) = **3.64** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: Crude birth rate for May, redundant with monthly count and not needed.] quote: "The crude birth rate in May was 3.64 per 1,000 people, led by Taitung County at 5.09"
  - p6 Taitung County crude birth rate in May (highest) = **5.09** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant to national monthly total.] quote: "led by Taitung County at 5.09, followed by Penghu County at 4.64 and Hsinchu City at 4.37"
  - p7 Penghu County crude birth rate in May = **4.64** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant.] quote: "followed by Penghu County at 4.64 and Hsinchu City at 4.37"
  - p8 Hsinchu City crude birth rate in May = **4.37** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant.] quote: "followed by Penghu County at 4.64 and Hsinchu City at 4.37, while Keelung recorded the lowest at 1.90"
  - p9 Keelung crude birth rate in May (lowest) = **1.9** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant.] quote: "while Keelung recorded the lowest at 1.90, followed by Miaoli at 2.69 and Chiayi County at 2.75"
  - p10 Miaoli crude birth rate in May = **2.69** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant.] quote: "followed by Miaoli at 2.69 and Chiayi County at 2.75"
  - p11 Chiayi County crude birth rate in May = **2.75** births per 1,000 people (2026-05-01..2026-05-31) [DISCARD: County-level rate, irrelevant.] quote: "followed by Miaoli at 2.69 and Chiayi County at 2.75"
  - p12 Taiwan total population at end of May = **23,252,641** people (2026-05-31..2026-05-31) [keep: ] quote: "Taiwan's population stood at 23,252,641 at the end of last month, down 102,829 from a year earlier and 9,903 fewer than the previous month"
  - p13 Taiwan population aged 0-14 at end of May = **2,642,980** people (2026-05-31..2026-05-31) [DISCARD: Age-structure population, not needed for monthly birth forecast.] quote: "the population aged 0-14 stood at 2,642,980, accounting for 11.37 percent of the total"
  - p14 Taiwan population aged 15-64 at end of May = **15,859,310** people (2026-05-31..2026-05-31) [DISCARD: Age-structure population, not needed.] quote: "those aged 15-64 totaled 15,859,310, or 68.20 percent"
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taipeitimes.com/News/taiwan/archives/2026/03/10/2003853589` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6398792` -> **snapshot** (snapshot 20260830205515); points raw/verified 12/10
  - p15 Taiwan births registered, January-June 2026 cumulative = **46,344** births registered (2026-01-01..2026-06-30) [keep: ] quote: "Taiwan recorded 46,344 births from January through June, down 9,031 from 55,375 during the same period last year."
  - p16 Taiwan births registered, June 2026 = **7,324** births registered (2026-06-01..2026-06-30) [keep: ] quote: "June saw 7,324 births, 1,644 fewer than a year earlier but 492 more than in May."
  - p17 Taiwan births registered, May 2026 = **492** births registered (2026-05-01..2026-05-31) [DISCARD: Mislabeled value (492 is the month-on-month change, not May births); misleading.] quote: "June saw 7,324 births, 1,644 fewer than a year earlier but 492 more than in May."
  - p18 Taiwan population at end of June 2026 = **23,243,565** people (2026-06-30..2026-06-30) [keep: ] quote: "Household registration data showed a population of 23,243,565 at the end of June, down 103,176 from a year earlier, per Mirror Media."
  - p19 Taiwan annual crude birth rate, June 2026 = **3.83** births per 1,000 people (2026-06-01..2026-06-30) [DISCARD: Crude birth rate, redundant.] quote: "The annual crude birth rate was 3.83 per 1,000 people in June, while the annual crude death rate was 8.55 per 1,000."
  - p20 Taiwan annual crude death rate, June 2026 = **8.55** deaths per 1,000 people (2026-06-01..2026-06-30) [DISCARD: Crude death rate, irrelevant.] quote: "The annual crude birth rate was 3.83 per 1,000 people in June, while the annual crude death rate was 8.55 per 1,000."
  - p21 Taiwan deaths registered, June 2026 = **16,340** deaths registered (2026-06-01..2026-06-30) [DISCARD: Deaths, irrelevant to births.] quote: "There were 16,340 deaths, down 214 from a year earlier but up 1,182 from May, Mirror Media reported."
  - p22 Taiwan population share aged 65 and older, June 2026 = **20.49** % (2026-06-30..2026-06-30) [DISCARD: Age share, irrelevant.] quote: "People aged 65 and older now account for 20.49% of the population, per CNA."
  - p23 Taiwan population share aged 0 to 14, June 2026 = **11.34** % (2026-06-30..2026-06-30) [DISCARD: Age share, irrelevant.] quote: "Residents aged 0 to 14 made up 11.34% of the population, while those aged 15 to 64 accounted for 68.18%."
  - p24 Taiwan population share aged 15 to 64, June 2026 = **68.18** % (2026-06-30..2026-06-30) [DISCARD: Age share, irrelevant.] quote: "Residents aged 0 to 14 made up 11.34% of the population, while those aged 15 to 64 accounted for 68.18%."
- `https://www.taiwannews.com.tw/news/6338119` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6317474` -> **snapshot** (snapshot 20260830205515); points raw/verified 15/0
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/14
  - p25 Taiwan registered births, September 2025 (monthly total) = **8,603** births registered (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p26 Taiwan registered births, August 2025 (monthly total) = **8,464** births registered (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p27 Taiwan registered births, July 2025 (monthly total) = **8,939** births registered (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p28 Taiwan registered births, June 2025 (monthly total) = **8,968** births registered (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p29 Taiwan registered births, May 2025 (monthly total) = **8,433** births registered (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p30 Taiwan registered births, October 2025 (monthly total) = **9,458** births registered (2025-10-01..2025-10-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p31 Taiwan registered births, November 2025 (monthly total) = **7,946** births registered (2025-11-01..2025-11-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p32 Taiwan registered births, December 2025 (monthly total) = **9,027** births registered (2025-12-01..2025-12-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p33 Taiwan registered births, January 2025 (monthly total) = **9,495** births registered (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p34 Taiwan registered births, February 2025 (monthly total) = **10,407** births registered (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p35 Taiwan registered births, March 2025 (monthly total) = **9,388** births registered (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p36 Taiwan registered births, April 2025 (monthly total) = **8,684** births registered (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p37 Taiwan total registered births, full year 2024 = **134,856** births registered (2024-01-01..2024-12-31) [keep: ] quote: "113 年(1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p38 Taiwan year-on-year change in registered births, 2025 vs 2024 (percent) = **-20.05** % (2025-01-01..2025-12-31) [keep: ] quote: "[(2)-(1)]/(1)×100 -20.05 -0.91 -- -- -- --"
- `https://www.ris.gov.tw/documents/html/5/2/popudata-quart-pub.html` -> **snapshot** (snapshot 20260902055958); points raw/verified 0/0
- `https://statis.moi.gov.tw/micst/webMain.aspx?k=menum` -> **snapshot** (snapshot 20260814004253); points raw/verified 0/0
- `https://ghdx.healthdata.org/print/486571` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.moi.gov.tw/files/site_stuff/321/1/month/month.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://focustaiwan.tw/society/202602100026` -> **snapshot** (snapshot 20260307145952); points raw/verified 11/11
  - p39 Live births registered in Taiwan, January 2026 = **8,723** births registered (2026-01-01..2026-01-31) [keep: ] quote: "A total of 8,723 babies were born in January, 304 fewer than in December and 772 fewer than a year earlier."
  - p40 Change in live births, January 2026 vs December 2025 (Taiwan) = **304** births registered (2026-01-01..2026-01-31) [keep: ] quote: "with the number of live births falling by 304 from December 2025"
  - p41 Change in live births, January 2026 vs January 2025 (Taiwan) = **772** births registered (2026-01-01..2026-01-31) [keep: ] quote: "8,723 babies were born in January, 304 fewer than in December and 772 fewer than a year earlier."
  - p42 Crude birth rate, Taiwan, January 2026 (annualized) = **4.41** births per 1,000 people (2026-01-01..2026-01-31) [DISCARD: Crude birth rate, redundant.] quote: "That translates to roughly one birth every 5.1 minutes and an annual crude birth rate of 4.41 per 1,000 people, MOI data showed."
  - p43 Minutes per birth, Taiwan, January 2026 = **5.1** minutes per birth (2026-01-01..2026-01-31) [DISCARD: Minutes per birth, redundant.] quote: "That translates to roughly one birth every 5.1 minutes and an annual crude birth rate of 4.41 per 1,000 people, MOI data showed."
  - p44 Total population of Taiwan, end of January 2026 = **23,289,045** people (2026-01-31..2026-01-31) [keep: ] quote: "As of the end of January, Taiwan's population totaled 23,289,045, down 10,087 from December 2025, the data showed."
  - p45 Deaths registered in Taiwan, January 2026 = **17,529** deaths registered (2026-01-01..2026-01-31) [DISCARD: Deaths, irrelevant.] quote: "Deaths totaled 17,529 for the month, or about one every 2.5 minutes, up 79 from December and 2,511 more than in January 2024."
  - p46 Natural population decrease, Taiwan, January 2026 = **8,806** people (2026-01-01..2026-01-31) [DISCARD: Natural decrease, irrelevant.] quote: "The natural population decrease, the difference between births and deaths, was 8,806 in January, MOI data showed."
  - p47 Net migration decrease, Taiwan, January 2026 = **1,281** people (2026-01-01..2026-01-31) [DISCARD: Migration, irrelevant.] quote: "In addition, the country recorded a net migration decrease of 1,281 people in January, with 71,042 people immigrating and 72,323 emigrating, according to the data."
  - p48 Population aged 0-14, Taiwan, end of January 2026 = **2,675,210** people (2026-01-31..2026-01-31) [DISCARD: Age-structure population, irrelevant.] quote: "Demographic data showed that people ages 0 to 14 accounted for 11.49 percent of the population (2,675,210), while those ages 15 to 64 made up 68.36 percent (15,921,351)."
  - p49 Share of population aged 0-14, Taiwan, end of January 2026 = **11.49** % (2026-01-31..2026-01-31) [DISCARD: Age share, irrelevant.] quote: "Demographic data showed that people ages 0 to 14 accounted for 11.49 percent of the population (2,675,210), while those ages 15 to 64 made up 68.36 percent (15,921,351)."
- dropped by code checks: 19 (period year 2025 does not appear in the page text or URL (likely mis-dated): 3; period year 2026 does not appear in the page text or URL (likely mis-dated): 15; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d2 [related_series] National statistics / DGBAS population and birth statistics

Hypothesis: DGBAS and National Development Council publish monthly/quarterly birth counts and population projections that track MOI registration counts closely; these can cross-check the level and trend and provide a September 2026 forecast or year-to-date anchor.

Queries issued by the searcher: 行政院主計總處 出生數 2026 統計; 國發會 人口推估 2026 出生數 預估; 2026年7月 出生數 內政部 戶籍統計 新生兒; 2025年9月 出生數 內政部 新生兒 統計; 行政院主計總處 出生數 2026; 國發會 人口推估 2026 出生數; Taiwan births 2026 monthly statistics; 2025年9月 出生數 內政部 戶口統計; 2025年 每月出生數 台灣 1月 2月 3月 4月 5月 6月 7月 8月 9月 10月 11月 12月; 內政部 戶口統計速報 出生 2026年7月 統計表; 行政院主計總處 出生數 2026; Taiwan births 2026 monthly statistics; 國發會 人口推估 2026 出生數 推估 每年出生; 2025年9月 新生兒 出生數 內政部 113 114年 每月出生

- `https://www.businesstoday.com.tw/group_search/article?keywords=%E5%BE%88%E7%A9%8D%E6%A5%B5%E5%9C%B0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://dev.taisounds.news/news/content/76/285689` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ndc.gov.tw/News_Content.aspx?n=114AAE178CD95D4C&s=6F7655EDC5AAD458` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.setn.com/news/1897905` -> **snapshot** (snapshot 20260828104329); points raw/verified 15/15
  - p50 NDC 2026 forecast of Taiwan live births (mid-range estimate) = **94,000** births (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒出生數將跌破10萬人大關、中推估值為9.4萬人。"
  - p51 NDC 2026 forecast range of Taiwan live births (low end) = **92,000** births (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒數將跌破10萬人大關,估計落在9.2萬至9.7萬人,中推估值為9.4萬人。"
  - p52 NDC 2026 forecast range of Taiwan live births (high end) = **97,000** births (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒數將跌破10萬人大關,估計落在9.2萬至9.7萬人,中推估值為9.4萬人。"
  - p53 MOI 2025 Taiwan newborn count (full year) = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "根據內政部資訊,2025年台灣新生兒數為10萬7812人,連10年下降,再創新低。"
  - p54 Taiwan total fertility rate 2025 = **0.7** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p55 Japan total fertility rate (comparison) = **1.14** births per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p56 Singapore total fertility rate (comparison) = **0.87** births per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p57 South Korea total fertility rate (comparison) = **0.8** births per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p58 Threshold total fertility rate defining ultra-low fertility = **1.3** births per woman (not stated (page dated 2026-08-28)) [DISCARD: Definitional threshold, no numerical role.] quote: "亞洲主要鄰國多已落入超低生育率1.3人以下"
  - p59 Working-age population share threshold defining demographic dividend = **66.7** % (not stated (page dated 2026-08-28)) [DISCARD: Definitional threshold, no numerical role.] quote: "人口紅利是指青壯年人口(15至64歲人口、又稱工作年齡人口)占總人口比重達66.7%以上"
  - p60 Year demographic dividend ends (revised NDC estimate) = **2,030** year (2030-01-01..2030-12-31) [DISCARD: Projection horizon, irrelevant.] quote: "人口紅利結束時間點反而延後2年、為2030年。"
  - p61 Delay in demographic dividend end versus earlier NDC estimate = **2** years (not stated (page dated 2026-08-28)) [DISCARD: Projection horizon, irrelevant.] quote: "人口紅利結束時間點反而延後2年、為2030年。"
  - p62 NDC population projection horizon (start year) = **2,026** year (2026-01-01..2026-12-31) [DISCARD: Projection horizon, irrelevant.] quote: "國發會今天公布最新「中華民國人口推估(2026年至2075年)」"
  - p63 NDC population projection horizon (end year) = **2,075** year (2075-01-01..2075-12-31) [DISCARD: Projection horizon, irrelevant.] quote: "國發會今天公布最新「中華民國人口推估(2026年至2075年)」"
  - p64 Frequency of NDC population projection updates = **2** years (not stated (page dated 2026-08-28)) [DISCARD: Projection frequency, irrelevant.] quote: "國發會每2年依據最新戶籍人口資料,更新出生、死亡及遷徙等人口變動要素的假設情境"
- `https://www.ptt.cc/bbs/home-sale/M.1778309941.A.A4C.html` -> **snapshot** (snapshot 20260514084730); points raw/verified 10/10
  - p65 Taiwan (ROC) live births registered in April 2026, monthly household registratio = **8,144** births registered (2026-04-01..2026-04-30) [keep: ] quote: "出生:8,144"
  - p66 Taiwan (ROC) total population at April 2026 statistics = **23,262,544** person (2026-04-30..2026-04-30) [DISCARD: Population total, irrelevant.] quote: "人口:23,262,544 (-8,024 / -0.034%)"
  - p67 Taiwan (ROC) monthly population change in April 2026 = **-8,024** person (2026-04-01..2026-04-30) [DISCARD: Population change, irrelevant.] quote: "人口:23,262,544 (-8,024 / -0.034%)"
  - p68 Taiwan (ROC) deaths in April 2026 = **-15,994** death (2026-04-01..2026-04-30) [DISCARD: Deaths, irrelevant.] quote: "死亡:-15,994"
  - p69 Taiwan (ROC) natural decrease in April 2026 = **-7,850** person (2026-04-01..2026-04-30) [DISCARD: Natural decrease, irrelevant.] quote: "自然減少:-7,850"
  - p70 Taiwan (ROC) social decrease in April 2026 = **-174** person (2026-04-01..2026-04-30) [DISCARD: Social decrease, irrelevant.] quote: "社會減少:-174 (人口)"
  - p71 Taiwan (ROC) total households at April 2026 statistics = **9,895,639** household (2026-04-30..2026-04-30) [DISCARD: Households, irrelevant.] quote: "戶數:9,895,639 (+3,541 / +0.036%)"
  - p72 Taiwan (ROC) average household size (persons per household) at April 2026 = **2.351** person/household (2026-04-30..2026-04-30) [DISCARD: Household size, irrelevant.] quote: "戶量:2.351 (-0.070%)"
  - p73 Taiwan (ROC) in-migration from abroad in April 2026 = **4,289** person (2026-04-01..2026-04-30) [DISCARD: Migration, irrelevant.] quote: "遷入 - 自外國:4,289"
  - p74 Taiwan (ROC) out-migration abroad in April 2026 = **-5,556** person (2026-04-01..2026-04-30) [DISCARD: Migration, irrelevant.] quote: "遷出 - 往外國:-5,556"
- `https://www.taiwannews.com.tw/news/6418283` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6398792` -> **snapshot** (snapshot 20260830205515); points raw/verified 15/14
  - p75 Taiwan births registered, January-June 2026 cumulative = **46,344** births (2026-01-01..2026-06-30) [keep: ] quote: "Taiwan recorded 46,344 births from January through June, down 9,031 from 55,375 during the same period last year."
  - p76 Year-on-year change in Taiwan births, January-June 2026 vs 2025 = **9,031** births (2026-01-01..2026-06-30) [DISCARD: Redundant with p15/p75 cumulative and p91/p106.] quote: "down 9,031 from 55,375 during the same period last year"
  - p77 Year-on-year percentage change in Taiwan births, first half 2026 = **16.3** % (2026-01-01..2026-06-30) [DISCARD: Redundant percentage of p76.] quote: "births in the first half of 2026 fell 16.3% from a year earlier"
  - p78 Taiwan births registered, June 2026 = **7,324** births (2026-06-01..2026-06-30) [keep: ] quote: "June saw 7,324 births, 1,644 fewer than a year earlier but 492 more than in May."
  - p79 Year-on-year change in Taiwan births, June 2026 vs June 2025 = **1,644** births (2026-06-01..2026-06-30) [DISCARD: Redundant with p16/p78.] quote: "June saw 7,324 births, 1,644 fewer than a year earlier but 492 more than in May."
  - p80 Month-on-month change in Taiwan births, June 2026 vs May 2026 = **492** births (2026-06-01..2026-06-30) [DISCARD: Redundant with p16/p78.] quote: "June saw 7,324 births, 1,644 fewer than a year earlier but 492 more than in May."
  - p81 Taiwan population at end of June 2026 = **23,243,565** people (2026-06-30..2026-06-30) [DISCARD: Population total, irrelevant.] quote: "Household registration data showed a population of 23,243,565 at the end of June"
  - p82 Year-on-year change in Taiwan population, end June 2026 = **103,176** people (2026-06-30..2026-06-30) [DISCARD: Population change, irrelevant.] quote: "down 103,176 from a year earlier"
  - p83 Month-on-month change in Taiwan population, June 2026 vs May 2026 = **9,076** people (2026-06-01..2026-06-30) [DISCARD: Population change, irrelevant.] quote: "Compared with May, the population decreased by 9,076."
  - p84 Taiwan deaths registered, June 2026 = **16,340** deaths (2026-06-01..2026-06-30) [DISCARD: Deaths, irrelevant.] quote: "There were 16,340 deaths, down 214 from a year earlier but up 1,182 from May"
  - p85 Taiwan annual crude birth rate, June 2026 = **3.83** births per 1,000 people (2026-06-01..2026-06-30) [DISCARD: Crude birth rate, redundant.] quote: "The annual crude birth rate was 3.83 per 1,000 people in June"
  - p86 Taiwan annual crude death rate, June 2026 = **8.55** deaths per 1,000 people (2026-06-01..2026-06-30) [DISCARD: Crude death rate, irrelevant.] quote: "while the annual crude death rate was 8.55 per 1,000"
  - p87 Taiwan net out-migration, June 2026 = **60** people (2026-06-01..2026-06-30) [DISCARD: Migration, irrelevant.] quote: "resulting in a net out-migration of 60 people"
  - p88 Taiwan population aged 65 and older share, June 2026 = **20.49** % (2026-06-30..2026-06-30) [DISCARD: Age share, irrelevant.] quote: "People aged 65 and older now account for 20.49% of the population"
- `https://www.taipeitimes.com/News/taiwan/archives/2026/06/10/2003858871` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/aipl/202608100072.aspx` -> **snapshot** (snapshot 20260903232636); points raw/verified 14/13
  - p89 Taiwan July 2026 (ROC year 115) live births registered in the month = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人。"
  - p90 Taiwan January-July 2026 (ROC year 115) cumulative live births = **54,250** births registered (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p91 Year-on-year change in Taiwan January-July cumulative live births (2026 vs 2025) = **10,064** births registered (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人。"
  - p92 Change in Taiwan monthly live births, July 2026 vs June 2026 = **582** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒,折合年粗出生率為千分之4.01,較去年同期減少1033人,相比今年6月增加582人。"
  - p93 Change in Taiwan monthly live births, July 2026 vs July 2025 = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人。"
  - p94 Taiwan July 2026 crude birth rate (annualised) = **4.01** births per 1,000 population (2026-07-01..2026-07-31) [DISCARD: Crude birth rate, redundant.] quote: "折合年粗出生率為千分之4.01"
  - p95 Minutes per birth in Taiwan, July 2026 = **5.6** minutes per birth (2026-07-01..2026-07-31) [DISCARD: Minutes per birth, redundant.] quote: "約每5.6分鐘出生一個嬰兒"
  - p96 Taiwan total population at end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p97 Consecutive months of Taiwan population decline through July 2026 = **31** months (2026-07-31..2026-07-31) [DISCARD: Streak length, irrelevant.] quote: "台灣人口數2323萬5002人,連續31個月負成長"
  - p98 Taiwan July 2026 deaths registered in the month = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人,平均約每2.6分鐘1人死亡"
  - p99 Taiwan January-July 2026 cumulative deaths = **115,628** deaths registered (2026-01-01..2026-07-31) [DISCARD: Deaths, irrelevant.] quote: "以今年前7月累計數據來看,死亡數共11萬5628人,新生兒共5萬4250人"
  - p100 Taiwan July 2026 natural increase (births minus deaths) = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p101 Taiwan July 2026 net migration (in-migrants minus out-migrants) = **650** person (2026-07-01..2026-07-31) [DISCARD: Migration, irrelevant.] quote: "淨遷入人口數為650人。"
- `https://www.rti.org.tw/news?uid=3&pid=225273` -> **snapshot** (snapshot 20260815163625); points raw/verified 15/14
  - p102 Taiwan (ROC) population at end of July 2026, MOI household registration statisti = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年(2026年)7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p103 Live births registered in Taiwan in July 2026 (monthly count) = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p104 Change in Taiwan monthly live births, July 2026 vs June 2026 = **582** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p105 Cumulative live births registered in Taiwan, January-July 2026 = **54,250** births registered (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p106 Year-on-year change in cumulative live births, January-July 2026 vs January-July = **10,064** births registered (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人"
  - p107 Year-on-year change in Taiwan monthly live births, July 2026 vs July 2025 = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人"
  - p108 Annual crude birth rate implied for July 2026 (births per 1,000 population) = **4.01** births per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Crude birth rate, redundant.] quote: "約每5.6分鐘出生一個嬰兒,折合年粗出生率為千分之4.01"
  - p109 Average interval between births in Taiwan, July 2026 = **5.6** minutes per birth (2026-07-01..2026-07-31) [DISCARD: Minutes per birth, redundant.] quote: "約每5.6分鐘出生一個嬰兒"
  - p110 Deaths registered in Taiwan in July 2026 = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人"
  - p111 Cumulative deaths registered in Taiwan, January-July 2026 = **115,628** deaths registered (2026-01-01..2026-07-31) [DISCARD: Deaths, irrelevant.] quote: "死亡數共11萬5628人,新生兒共5萬4250人"
  - p112 Taiwan natural population increase in July 2026 (births minus deaths) = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p113 Taiwan total population change, July 2026 vs June 2026 = **8,563** person (2026-07-01..2026-07-31) [DISCARD: Population change, irrelevant.] quote: "7月總人口較6月減少8563人"
  - p114 Taiwan population aged 0-14 at end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p115 Share of Taiwan population aged 0-14 at end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "0至14歲人口數262萬5992人,占總人口比率11.30%"
- `https://udn.com/news/amp/story/7238/9681382` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/amp/story/7314/9720922` -> **snapshot** (snapshot 20260908021017); points raw/verified 15/15
  - p116 Taiwan total population, 2026, NDC medium-variant projection (start of projectio = **23,190,000** person (2026-01-01..2026-12-31) [DISCARD: Population projection, irrelevant.] quote: "台灣總人口將從今年2,319萬人一路下滑"
  - p117 Taiwan total population, 2035, NDC medium-variant projection = **21,970,000** person (2035-01-01..2035-12-31) [DISCARD: Population projection, irrelevant.] quote: "全台總人口2035年將降至2,197萬人"
  - p118 Taiwan total population, 2045, NDC medium-variant projection = **19,980,000** person (2045-01-01..2045-12-31) [DISCARD: Population projection, irrelevant.] quote: "2045年正式跌破2,000萬人,降至1,998萬人"
  - p119 Taiwan total population, 2075, NDC medium-variant projection = **12,150,000** person (2075-01-01..2075-12-31) [DISCARD: Population projection, irrelevant.] quote: "到了2075年,則僅剩1,215萬人"
  - p120 Taiwan live births (newborns), 2026, NDC low-variant projection = **92,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p121 Taiwan live births (newborns), 2026, NDC medium-variant projection = **94,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p122 Taiwan live births (newborns), 2026, NDC high-variant projection = **97,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p123 Taiwan live births (newborns), 2075, NDC medium-variant projection = **27,000** birth (2075-01-01..2075-12-31) [DISCARD: 2075 projection, irrelevant.] quote: "到2075年新生兒更只剩2.7萬人,不到今年的三成"
  - p124 Taiwan deaths, 2026, NDC projection = **199,000** death (2026-01-01..2026-12-31) [DISCARD: Deaths projection, irrelevant.] quote: "死亡人數將從今年19.9萬人增至2075年的30.5萬人"
  - p125 Taiwan deaths, 2075, NDC projection = **305,000** death (2075-01-01..2075-12-31) [DISCARD: Deaths projection, irrelevant.] quote: "死亡人數將從今年19.9萬人增至2075年的30.5萬人"
  - p126 Taiwan natural population increase, 2026, NDC projection = **105,000** person (2026-01-01..2026-12-31) [DISCARD: Natural increase projection, irrelevant.] quote: "人口自然增加由今年負10.5萬人,進一步擴大至負27.8萬人"
  - p127 Taiwan natural population increase, 2075, NDC projection = **278,000** person (2075-01-01..2075-12-31) [DISCARD: Natural increase projection, irrelevant.] quote: "人口自然增加由今年負10.5萬人,進一步擴大至負27.8萬人"
  - p128 Taiwan total fertility rate, 2025 (prior year, MOI data cited by NDC) = **0.695** birth/(woman*year) (2025-01-01..2025-12-31) [keep: ] quote: "台灣去年總生育率降至0.695人"
  - p129 Taiwan total fertility rate, 2075, NDC medium-variant projection = **0.8** birth/(woman*year) (2075-01-01..2075-12-31) [DISCARD: 2075 TFR projection, irrelevant.] quote: "預估到2075年,高、中、低情境下的生育率分別為1.1人、0.8人及0.6人"
  - p130 Share of women aged 20-49 ever married, 2025, Taiwan = **43.5** % (2025-01-01..2025-12-31) [DISCARD: Marriage share, not needed.] quote: "20至49歲女性有偶率已由2005年的55.3%,降至2025年的43.5%"
- dropped by code checks: 3 (period year 2025 does not appear in the page text or URL (likely mis-dated): 3)

### d3 [related_series] Comparable East Asian low-fertility jurisdictions

Hypothesis: Taiwan's birth trajectory resembles South Korea and Japan in direction; if Korea/Japan September 2026 or recent monthly data show a trend change (e.g., rebound or continued decline), it constrains whether Taiwan's 2026 level is above or below the 2025 extrapolation.

Queries issued by the searcher: South Korea monthly births 2026 statistics year-over-year; Japan births 2026 monthly statistics 厚生労働省 人口動態; Korea "June 2026" population trends births 15.6% August 26 2026 국가데이터처; 人口動態統計速報 令和8年6月分 出生数 前年同月比; South Korea monthly births 2026 statistics Korea; Japan births 2026 monthly statistics 人口動態統計; 국가데이터처 2026년 7월 인구동향 출생아 수; Taiwan births July 2026 household registration monthly statistics; South Korea monthly births 2026 statistics year-on-year change; Japan births 2026 monthly statistics 人口動態統計 2026; 人口動態統計速報 令和8年6月分 厚生労働省 発表 2026年8月; Korea July 2026 population trends births up 11.1% August 26 2026

- `https://spanish.korea.net/NewsFocus/Society/view?articleId=301909` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=294740&koreanId=294708` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/m2026/06.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://chosun-chosun-prod.cdn.arcpublishing.com/english/market-money-en/2026/07/30/Q32WPE2TNJHKXNO52CAVZMNRYA/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kurashi-data.com/shussei/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.yna.co.kr/view/AEN20260826004100320` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.infomaxai.com/news/articleView.html?idxno=136685` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yna.co.kr/view/AKR20260826079400002` -> **snapshot** (snapshot 20260906113400); points raw/verified 15/15
  - p131 South Korea live births, June 2026 (monthly) = **23,111** births registered (2026-06-01..2026-06-30) [keep: ] quote: "6월 출생아 수는 2만3천111명으로 작년 동월 대비 3천115명(15.6%) 증가했다."
  - p132 South Korea June 2026 live births year-over-year change (absolute) = **3,115** births registered (2026-06-01..2026-06-30) [keep: ] quote: "6월 출생아 수는 2만3천111명으로 작년 동월 대비 3천115명(15.6%) 증가했다."
  - p133 South Korea June 2026 live births year-over-year change (percent) = **15.6** % (2026-06-01..2026-06-30) [keep: ] quote: "6월 출생아 수는 2만3천111명으로 작년 동월 대비 3천115명(15.6%) 증가했다."
  - p134 South Korea consecutive months of year-over-year increase in monthly live births = **24** month (2024-07-01..2026-06-30) [keep: ] quote: "24개월 연속 동월대비 증가했다."
  - p135 South Korea total fertility rate, June 2026 = **0.88** births per woman (2026-06-01..2026-06-30) [keep: ] quote: "6월 합계출산율은 0.88명으로 0.11명 늘었다."
  - p136 South Korea live births, Q2 2026 (quarterly) = **70,791** births registered (2026-04-01..2026-06-30) [keep: ] quote: "올해 2분기 출생아는 7만791명으로 1년 전보다 9천675명(15.8%) 증가했다."
  - p137 South Korea Q2 2026 live births year-over-year change (absolute) = **9,675** births registered (2026-04-01..2026-06-30) [keep: ] quote: "올해 2분기 출생아는 7만791명으로 1년 전보다 9천675명(15.8%) 증가했다."
  - p138 South Korea Q2 2026 live births year-over-year change (percent) = **15.8** % (2026-04-01..2026-06-30) [keep: ] quote: "올해 2분기 출생아는 7만791명으로 1년 전보다 9천675명(15.8%) 증가했다."
  - p139 South Korea live births, H1 2026 cumulative (January-June) = **145,804** births registered (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 누적 출생아는 14만5천804명으로 1만9천430명(15.4%) 증가했다."
  - p140 South Korea H1 2026 live births year-over-year change (absolute) = **19,430** births registered (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 누적 출생아는 14만5천804명으로 1만9천430명(15.4%) 증가했다."
  - p141 South Korea H1 2026 live births year-over-year change (percent) = **15.4** % (2026-01-01..2026-06-30) [keep: ] quote: "올해 상반기 누적 출생아는 14만5천804명으로 1만9천430명(15.4%) 증가했다."
  - p142 South Korea marriages, June 2026 (leading indicator of births) = **21,075** marriages registered (2026-06-01..2026-06-30) [DISCARD: Korea marriages, not transferable to Taiwan level.] quote: "출생의 선행지표인 혼인 건수는 6월 2만1천75건으로 2천593건(14.0%) 증가했다."
  - p143 South Korea marriages, Q2 2026 = **62,065** marriages registered (2026-04-01..2026-06-30) [DISCARD: Korea marriages, not transferable.] quote: "2분기는 6만2천65건으로 2천904건(4.9%) 증가했다."
  - p144 South Korea age-specific fertility rate, women aged 30-34, Q2 2026 = **82.1** births per 1,000 women (2026-04-01..2026-06-30) [DISCARD: Korea ASFR, not transferable.] quote: "연령별 출산율은 30∼34세가 82.1명으로 1년 전 같은 분기보다 11.0명 증가했다."
  - p145 South Korea age-specific fertility rate, women aged 35-39, Q2 2026 = **60.2** births per 1,000 women (2026-04-01..2026-06-30) [DISCARD: Korea ASFR, not transferable.] quote: "35∼39세는 60.2명으로 10.7명 늘었다."
- `https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/geppo/s2026/dl/202605.pdf` -> **snapshot** (snapshot 20260724075506); points raw/verified 14/14
  - p146 Japan monthly live births, May 2026 (provisional, all events incl. foreigners an = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p147 Japan monthly live births, May 2025 (provisional) = **60,718** as written "60 718", value check pending births (2025-05-01..2025-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p148 Japan monthly live births, May 2026 vs May 2025, year-over-year change (count) = **-1,055** as written "△ 1 055", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p149 Japan monthly live births, May 2026 vs May 2025, year-over-year change rate = **1.7** % (2026-05-01..2026-05-31) [keep: ] quote: "5月 出 生 59 663 60 718 △ 1 055 △ 1.7 5.7 5.8 98.7"
  - p150 Japan cumulative live births, January-May 2026 = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p151 Japan cumulative live births, January-May 2025 = **280,979** as written "280 979", value check pending births (2025-01-01..2025-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p152 Japan cumulative live births, January-May 2026 vs 2025, year-over-year change (c = **1,243** as written "1 243", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p153 Japan cumulative live births, January-May 2026 vs 2025, year-over-year change ra = **0.4** % (2026-01-01..2026-05-31) [keep: ] quote: "出 生 282 222 280 979 1 243 0.4 5.6 5.5 100.9"
  - p154 Japan live births, trailing 12 months June 2025-May 2026 = **707,052** as written "707 052", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p155 Japan live births, trailing 12 months June 2024-May 2025 = **709,893** as written "709 893", value check pending births (2024-06-01..2025-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p156 Japan live births, trailing 12 months June 2025-May 2026 vs prior 12 months, yea = **-2,841** as written "△ 2 841", value check pending births (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p157 Japan live births, trailing 12 months June 2025-May 2026 vs prior 12 months, yea = **0.4** % (2025-06-01..2026-05-31) [keep: ] quote: "出 生 707 052 709 893 △ 2 841 △ 0.4 5.7 5.7 100.1"
  - p158 Japan national live births, May 2026 (by place of notification, prefecture table = **59,663** as written "59 663", value check pending births (2026-05-01..2026-05-31) [keep: ] quote: "全 国 59 663 122 385 1 318 41 169 13 449"
  - p159 Japan national live births, January-May 2026 cumulative (by place of notificatio = **282,222** as written "282 222", value check pending births (2026-01-01..2026-05-31) [keep: ] quote: "全 国 282 222 664 510 6 700 206 971 75 656"
- `https://www.sentankyo.jp/articles/3b848bca-e88c-45ce-96cf-1278fb20c1a0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.projectdesign.jp/articles/news/622644f6-9462-48a6-976b-b8dd511ec5e3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.nocutnews.co.kr/news/6568298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [base_rates] Demographic accounting: women of childbearing age × age-specific fertility

Hypothesis: September 2026 births ≈ sum over maternal age groups of (women aged a in 2026) × (age-specific fertility rate a) × (September seasonal factor). Population by age and recent ASFRs give an independent structural estimate.

Queries issued by the searcher: Taiwan age-specific fertility rate 2025 內政部 年齡別生育率; Taiwan female population by single year of age 2025 內政部 戶籍人口統計 年齡別; 內政部 戶政司 出生數 按月 統計 2026年 8月 出生 登記; 中華民國人口統計年刊 113年 年齡別生育率 表 育齡婦女; Taiwan age-specific fertility rate 2025 內政部 年齡別生育率; Taiwan births September 2025 monthly household registration statistics; 內政部戶政司 人口統計 年齡別生育率 育齡婦女 2024 各年齡組; 2026年8月 出生數 內政部 人口統計 新生兒; Taiwan age-specific fertility rate 2025 內政部 年齡別生育率; Taiwan female population by single year of age 2025 內政部 戶籍人口統計; 內政部 統計月報 出生數 按月 2026年 新生兒 8月; Taiwan monthly births 2025 September births by month statistics 內政部 出生數 每月; 2025年9月 出生數 內政部 新生兒 較去年同期 統計; 內政部 戶政司 年齡別生育率 2025 育齡婦女 25-29 30-34 每千婦女

- `http://mp.weixin.qq.com/s?__biz=MzYzODg1NjE3Mg==&mid=2247484485&idx=1&sn=6abc718b35aa41ed808248bc69afc5be` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cdj.sfaa.gov.tw/HTML/Refer_HtmlNewsReport_Menu?no=301&t=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://asianews.network/chips-powerhouse-hsinchu-a-bright-spot-amid-taiwans-birth-rate-crisis/` -> **snapshot** (snapshot 20260127034108); points raw/verified 15/15
  - p160 Taiwan crude birth rate, 2025 (births per 1,000 people) = **4.62** births per 1,000 people (2025-01-01..2025-12-31) [keep: ] quote: "its crude birth rate plummeting to 4.62 per 1,000 people in 2025, down from 5.76 a year earlier"
  - p161 Taiwan crude birth rate, 2024 (births per 1,000 people) = **5.76** births per 1,000 people (2024-01-01..2024-12-31) [keep: ] quote: "down from 5.76 a year earlier"
  - p162 Taiwan total newborns, 2025 (record low) = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, the total number of newborns hit a record low of 107,812."
  - p163 Taiwan total fertility rate, 2025 (projected, upper bound of 'below 0.8') = **0.8** children per woman (2025-01-01..2025-12-31) [DISCARD: Redundant TFR bound.] quote: "the 2025 figure is projected to have fallen below 0.8, based on monthly government data"
  - p164 Hsinchu city total fertility rate (several years, around) = **1** as written "one", value check pending children per woman (not stated (page dated 2026-01-27)) [DISCARD: Local TFR, irrelevant.] quote: "For several years, Hsinchu's total fertility rate has hovered around one child per woman."
  - p165 Hsinchu city population (roughly) = **450,500** people (not stated (page dated 2026-01-27)) [DISCARD: Local population, irrelevant.] quote: "with 15.7 per cent of the roughly 450,500 people in the city aged below 14"
  - p166 Hsinchu city share of residents aged below 14 = **15.7** % (residents aged below 14 / total residents) (not stated (page dated 2026-01-27)) [DISCARD: Local age share, irrelevant.] quote: "with 15.7 per cent of the roughly 450,500 people in the city aged below 14"
  - p167 Taiwan island-wide share of residents aged below 14 = **11** % (residents aged below 14 / total residents) (not stated (page dated 2026-01-27)) [DISCARD: Age share, irrelevant.] quote: "This is well above the island's average of 11 per cent."
  - p168 TSMC employees' share of Taiwan population = **0.3** % (TSMC employees / Taiwan population) (not stated (page dated 2026-01-27)) [DISCARD: Employment share, irrelevant.] quote: "its employees make up only 0.3 per cent of the island's population"
  - p169 TSMC employees' share of all Taiwan newborns, 2023 = **1.8** % (newborns to TSMC employees / all newborns) (2023-01-01..2023-12-31) [DISCARD: Employment share, irrelevant.] quote: "but were responsible for 1.8 per cent of all newborns in 2023"
  - p170 Taiwan housing price-to-annual-income ratio, 2024 (record high) = **10.76** years of income per home (2024-01-01..2024-12-31) [DISCARD: Housing ratio, irrelevant.] quote: "In 2024, Taiwan's housing price-to-annual-income ratio hit a record high of 10.76"
  - p171 Taipei housing price-to-annual-income ratio, 2024 = **16.6** years of income per home (2024-01-01..2024-12-31) [DISCARD: Housing ratio, irrelevant.] quote: "with the ratio in Taipei reaching 16.6, meaning that it would take a person more than 16 years to afford a home in the capital"
  - p172 Taiwan real wage annual average growth over past decade = **1** % per year (not stated (page dated 2026-01-27)) [DISCARD: Wage growth, irrelevant.] quote: "with real wages growing by an annual average of just around 1 per cent over the past decade"
  - p173 Share of 1111 survey respondents unwilling to have children due to economic conc = **70** % (respondents unwilling / respondents polled) (2025-11-01..2025-11-30) [DISCARD: Survey share, irrelevant.] quote: "According to a November 2025 survey by popular job portal 1111, close to 70 per cent of respondents polled said they were unwilling to have children due to economic concerns."
  - p174 Taiwan electronics sector wage premium over economy-wide average = **70** % (electronics wages above economy-wide average) (not stated (page dated 2026-01-27)) [DISCARD: Wage premium, irrelevant.] quote: "wages in Taiwan's electronics sector are around 70 per cent higher than the economy-wide average"
- `https://www.sunnyswa.org.tw/category/%e7%b2%97%e7%94%9f%e8%82%b2%e7%8e%87%e7%af%87` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gelonghui.com/live/2640723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rti.org.tw/news?uid=3&pid=231114` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/amp/story/7314/9745834` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/info-liferay/app/channel/newsEnglishDetail/26245250` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzExL3JlbGZpbGUvNTgxOS83MTM4LzAwMTIyMjQucGRm&n=MjAwOTA4LWFsbC5wZGY%3d&icon=.pdf` -> **snapshot** (snapshot 20260106043040); points raw/verified 15/10
  - p175 Taiwan total fertility rate (TFR), 2008 estimate, per woman = **1.1** births per woman (2008-01-01..2008-12-31) [DISCARD: Old TFR, irrelevant.] quote: "台 灣 23 9 6 3 1 8.4 1.1 -6"
  - p176 Taiwan TFR, 2009 (民國97年) projection starting year, per woman = **1.1** births per woman (2008-01-01..2008-12-31) [DISCARD: Old TFR, irrelevant.] quote: "一、總生育率-替代水準 人 1.1 104年1.60 2.10"
  - p177 Taiwan TFR, recent 3 years (民國94-96年), per woman = **1.1** births per woman (2005-01-01..2007-12-31) [DISCARD: Old TFR, irrelevant.] quote: "快速降至近 3 年(94 至 96 年)為 1.1 人"
  - p178 Taiwan births, 1986 (民國75年), persons = **308,000** births (1986-01-01..1986-12-31) [DISCARD: Old birth count, irrelevant.] quote: "75至86年間,我國出生數維持在30.8萬人至34.1萬人之間"
  - p179 Taiwan births, 1997 (民國86年), persons = **341,000** births (1997-01-01..1997-12-31) [DISCARD: Old birth count, irrelevant.] quote: "75至86年間,我國出生數維持在30.8萬人至34.1萬人之間"
  - p180 Taiwan births, 2056 (民國145年) medium projection, persons = **132,000** births (2056-01-01..2056-12-31) [DISCARD: Old projection, irrelevant.] quote: "110年 13.2萬人(中推計)"
  - p181 Taiwan births, 2056 (民國145年) low projection, persons = **94,000** births (2056-01-01..2056-12-31) [DISCARD: Old projection, irrelevant.] quote: "9.4萬人 (低推計)"
  - p182 Taiwan births, 2056 (民國145年) high projection, persons = **162,000** births (2056-01-01..2056-12-31) [DISCARD: Old projection, irrelevant.] quote: "16.2萬人(高推計)"
  - p183 Taiwan births, 2056 (民國145年) replacement-level projection, persons = **277,000** births (2056-01-01..2056-12-31) [DISCARD: Old projection, irrelevant.] quote: "27.7萬人(替代水準)"
  - p184 Taiwan crude birth rate, 2008 (民國97年), per 1,000 population = **8.9** births per 1,000 persons (2008-01-01..2008-12-31) [DISCARD: Old crude rate, irrelevant.] quote: "粗出生率 8.9‰ 粗死亡率16.8‰"
- `https://www.ris.gov.tw/documents/data/5/2/Demographic_Fact_Book_110.pdf?lottery=dFJSdCt5bUZMbzdrSEVtM25YTzJBQT09&name=NDMyMjM5SXB5V3lhYlJWdlBUY1hMUT09` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.dgbas.gov.tw/001/Upload/463/relfile/11053/87854/e716ed45-5e3a-48e0-90e6-d3796b4339c5.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word '千' not supported by quote or table header: 2; scale word '百萬' not supported by quote or table header: 1)

### d5 [administrative] Birth registration and prenatal care records

Hypothesis: Births registered in September 2026 largely correspond to conceptions around December 2025 and to births occurring in August-September 2026; prenatal care visits, hospital delivery counts, and birth certificate issuances in August-September 2026 provide a leading/coincident indicator of the September registration count.

Queries issued by the searcher: 台灣 出生 統計 2026 內政部 戶政司 每月 出生登記; 內政部 戶政司 出生登記 按月 統計 2025; 健保 產檢 人次 2026 統計 孕婦 產前檢查 申報; 國民健康署 出生通報 統計 2026 出生數 醫療院所 出生證明; 台灣 出生登記 統計 2026年 每月 出生人數 內政部; 台灣 2026年 上半年 出生人數 新生兒 統計; 2025年9月 新生兒 出生數 內政部 戶口統計 113年 vs 114年 9月; 健保 產檢 人次 統計 2026 孕婦 產前檢查 申報; 台灣 出生證明 統計 2026; 內政部 戶政司 出生登記 統計 2026年 每月; 2026年7月 新生兒 內政部 戶口統計 出生數 7月; 健保 產檢 人次 2026 統計 孕婦產檢

- `https://www.ris.gov.tw/info-liferay/app/channel/newsEnglishDetail/26245259` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://v3.mirrormedia.mg/story/20260508edi017` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rti.org.tw/news?pid=196249&uid=3` -> **snapshot** (snapshot 20260414160447); points raw/verified 15/12
  - p185 Live births registered in Taiwan, February 2026 (monthly births registered) = **6,523** births registered (2026-02-01..2026-02-28) [keep: ] quote: "今年2月出生數為6523人,約每6.2分鐘出生一個嬰兒"
  - p186 Live births registered in Taiwan, January 2026 (implied from February level and  = **2,200** births registered (2026-01-01..2026-01-31) [DISCARD: Implied/derived value, misleading.] quote: "2月新生兒共6523人,較1月少了2200人、大減25.2%"
  - p187 Month-on-month change in Taiwan live births, February 2026 vs January 2026 (perc = **25.2** % (2026-02-01..2026-02-28) [DISCARD: Derived percentage, misleading.] quote: "較1月少了2200人、大減25.2%"
  - p188 Year-on-year change in Taiwan live births, February 2026 vs February 2025 (birth = **3,884** births registered (2026-02-01..2026-02-28) [DISCARD: Derived change, redundant.] quote: "較1月減少2200人,也較去年同期減少3884人"
  - p189 Annualised crude birth rate, Taiwan, February 2026 = **3.65** births per 1,000 population (2026-02-01..2026-02-28) [DISCARD: Crude rate, redundant.] quote: "折合年粗出生率為千分之3.65"
  - p190 Average interval between births, Taiwan, February 2026 = **6.2** minutes per birth (2026-02-01..2026-02-28) [DISCARD: Minutes per birth, redundant.] quote: "約每6.2分鐘出生一個嬰兒"
  - p191 Deaths registered in Taiwan, February 2026 = **14,881** deaths registered (2026-02-01..2026-02-28) [DISCARD: Deaths, irrelevant.] quote: "2月死亡1萬4881人,平均約每2.7分鐘1人死亡"
  - p192 Natural population increase, Taiwan, February 2026 (births minus deaths) = **8,358** person (2026-02-01..2026-02-28) [DISCARD: Natural increase, irrelevant.] quote: "台灣2月人口自然增加為負8358人"
  - p193 Total population of Taiwan, end of February 2026 = **23,280,273** person (2026-02-28..2026-02-28) [DISCARD: Population, irrelevant.] quote: "截至2026年2月底,台灣人口數為2328萬273人,已連續26個月負成長"
  - p194 Population aged 15-64 in Taiwan, end of February 2026 = **15,905,248** person (2026-02-28..2026-02-28) [DISCARD: Population, irrelevant.] quote: "15至64歲人口數為1590萬5248人,占68.32%"
  - p195 Population aged 0-14 in Taiwan, end of February 2026 = **2,667,349** person (2026-02-28..2026-02-28) [DISCARD: Population, irrelevant.] quote: "台灣0至14歲人口數為266萬7349人,占總人口比率11.46%"
  - p196 Marriages in Taiwan, February 2026 (couples) = **6,733** couple (2026-02-01..2026-02-28) [DISCARD: February marriages, not the relevant conception month.] quote: "2月結婚共6733對,其中不同性別6534對、相同性別199對"
- `https://news.ltn.com.tw/news/life/breakingnews/5365298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mohw.gov.tw/dl-99969-c1f6ae78-5f82-4c52-bfeb-15581648da80.html` -> **snapshot** (snapshot 20260801141123); points raw/verified 15/6
  - p197 Prenatal care utilisation (at least 8 visits) rate, Taiwan, 2025 target = **95** % (2025-01-01..2025-12-31) [DISCARD: Prenatal target rate, no numerical role.] quote: "孕婦產檢率 111年:94% 112年:95% 113年:95% 114年:95%"
  - p198 Ultrasound examinations in pregnancy, Taiwan, 2025 estimate (visits) = **295,000** ultrasound examination (2025-01-01..2025-12-31) [DISCARD: Prenatal visit estimate, not a birth count.] quote: "超音波檢查利用人次約 29.5 萬人次"
  - p199 Anaemia testing in pregnancy, Taiwan, 2025 estimate (persons) = **99,000** person (2025-01-01..2025-12-31) [DISCARD: Prenatal test estimate, not a birth count.] quote: "貧血檢驗約服務 9.9 萬人次"
  - p200 Prenatal health education guidance, Taiwan, 2025 estimate (visits) = **175,000** visit (2025-01-01..2025-12-31) [DISCARD: Prenatal guidance estimate, not a birth count.] quote: "孕婦產前衛教指導約服務 17.5 萬人次"
  - p201 Newborn congenital metabolic disease screening, Taiwan, 2025 (persons) = **100,000** newborn (2025-01-01..2025-12-31) [DISCARD: Screening count, not a birth count.] quote: "新生兒先天性代謝異常疾病 114 年共篩檢 10 萬 7,142 人,篩檢率為 99.5%以上。"
  - p202 Newborn hearing screening, Taiwan, 2024 (persons) = **130,000** newborn (2024-01-01..2024-12-31) [DISCARD: Screening count, not a birth count.] quote: "新生兒聽力篩檢率 113 年篩檢 13 萬 5,386 人,篩檢率達 98.9%。"
- `https://health99.hpa.gov.tw/storage/pdf/materials/21770.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://opendatatw.org/dataset/8411` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.163.com/dy/article/KV36R0PT055080L4.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://vakiodaily.com/news/view/id/701101` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/story/7266/8729989` -> **snapshot** (snapshot 20250720183520); points raw/verified 15/0
- dropped by code checks: 27 (period year 2025 does not appear in the page text or URL (likely mis-dated): 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 9; period year 2026 does not appear in the page text or URL (likely mis-dated): 15)

### d6 [shocks] Calendar, policy, and Dragon-year effects

Hypothesis: 2024 was a Dragon year with elevated births; 2025-2026 likely revert downward. Policy changes (childbirth subsidies, marriage incentives) and any 2026 calendar effects (Lunar New Year timing affecting conception months) shift the September level. Quantify the post-Dragon reversion and any 2026 policy effect.

Queries issued by the searcher: Taiwan births after Dragon year decline 2012 2013 year-over-year; 台灣 2026 生育補助 新制 少子化 對策; 內政部 戶政司 2026年 7月 出生數 統計 新生兒; 台灣 2025年 出生數 總計 創新低 11萬; Taiwan births after Dragon year decline 2012 2013 龍年 出生數 下降; 內政部 戶政司 出生人數 統計 2025 每月; 2026年 出生數 內政部 戶口統計 新生兒 月; 好孕三方案 生育補助 每胎10萬元 2026年上路; Taiwan births September 2025 monthly household registration statistics; Taiwan births after Dragon year 2013 decline 2012; Taiwan 2026 childbirth subsidy policy announcement; Lunar New Year 2026 date Taiwan; site:moi.gov.tw 115年7月 戶口統計 出生數 2026; Taiwan August 2026 births monthly statistics 2026 年 8 月 出生數; Taiwan births 2026 first half year down percent January July; 2026 Lunar New Year February 17 2026 Taiwan conception September births

- `https://www.taipeitimes.com/News/taiwan/archives/2025/01/02/2003829530` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwanwomencenter.org.tw/upload/website/twc_75ac0add-5cd1-4125-8cc3-80c5570c0bc4.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p203 Taiwan total population, July 2026 (month-end) = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長"
  - p204 Live births registered in Taiwan, July 2026 = **7,906** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p205 Live births registered in Taiwan, May 2026 = **6,832** birth (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p206 Live births registered in Taiwan, June 2026 = **7,324** birth (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p207 Year-over-year change in July live births, Taiwan, 2026 vs 2025 = **1,033** birth (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p208 Year-over-year percent change in July live births, Taiwan, 2026 vs 2025 = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p209 Crude birth rate (annualised), Taiwan, July 2026 = **4.01** births per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p210 Deaths registered in Taiwan, July 2026 = **17,119** death (2026-07-01..2026-07-31) [keep: ] quote: "至於7月死亡人數則為1萬7119人,平均約每2.6分鐘有一人死亡"
  - p211 Crude death rate (annualised), Taiwan, July 2026 = **8.67** deaths per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Crude death rate, irrelevant.] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%"
  - p212 Year-over-year change in Taiwan total population, July 2026 vs 2025 = **0.44** % (2026-07-31..2026-07-31) [DISCARD: Population change, irrelevant.] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p213 Consecutive months of population decline, Taiwan, through July 2026 = **31** month (2026-07-31..2026-07-31) [DISCARD: Streak length, irrelevant.] quote: "是連續31個月出現人口負成長"
  - p214 Share of population aged 65+, Taiwan, end-July 2026 = **20.54** % (2026-07-31..2026-07-31) [DISCARD: Age share, irrelevant.] quote: "截自7月底,台灣年齡分布持續呈現超高齡化,65歲以上人口占20.54%"
  - p215 Share of population aged 0-14, Taiwan, end-July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p216 Marriages registered in Taiwan, July 2026 = **7,150** couple (2026-07-01..2026-07-31) [DISCARD: July marriages, not the relevant conception month.] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%"
  - p217 Divorces registered in Taiwan, July 2026 = **4,450** couple (2026-07-01..2026-07-31) [DISCARD: Divorces, irrelevant.] quote: "離婚對數為4450對,同婚占1.7%"
- `https://zhonghao.com.tw/tw/html/news/show.php?kid=116&kid2=&nid=309` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://macaubusiness.com/dragon-baby-boom-no-more/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ndc.gov.tw/News_Content7.aspx?n=3E6699ADB0BE3855&s=9D19CF32A86D2914` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/aipl/202605270141.aspx` -> **snapshot** (snapshot 20260830122645); points raw/verified 15/15
  - p218 Monthly growth allowance per person aged 0-18 under new population strategy (NTD = **5,000** NTD/(person*month) (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "0至18歲每人每月領新台幣5000元,0至6歲全額直接領"
  - p219 Birth grant top-up per birth under new strategy (NTD) = **100,000** NTD/birth (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "不論勞保、國保、農保、軍保或軍公教補助,每胎生育給付都補足至10萬元"
  - p220 Home childcare allowance per month for ages 0-2 (NTD, lower bound) = **5,000** NTD/(person*month) (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "0至2歲依胎次提高補助,在家帶每月5000至7000元"
  - p221 Home childcare allowance per month for ages 0-2 (NTD, upper bound) = **7,000** NTD/(person*month) (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "0至2歲依胎次提高補助,在家帶每月5000至7000元"
  - p222 Quasi-public childcare subsidy per month for ages 0-2 (NTD, lower bound) = **13,000** NTD/(person*month) (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "公托7000至9000元,準公共托育1.3萬至1.5萬元"
  - p223 Quasi-public childcare subsidy per month for ages 0-2 (NTD, upper bound) = **15,000** NTD/(person*month) (2026-05-27..2026-05-27) [DISCARD: Policy amount, no numerical role.] quote: "公托7000至9000元,準公共托育1.3萬至1.5萬元"
  - p224 Marriage leave extended to (days) = **14** day (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "婚假擴至14天、產假擴至12週、陪產假擴至14天"
  - p225 Maternity leave extended to (weeks) = **12** week (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "婚假擴至14天、產假擴至12週、陪產假擴至14天"
  - p226 Paternity leave extended to (days) = **14** day (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "婚假擴至14天、產假擴至12週、陪產假擴至14天"
  - p227 Parental leave allowance combined maximum per couple (months) = **18** month (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "雙親各領滿6個月育嬰留停津貼後,可各再多領3個月,合計最高18個月"
  - p228 Parental leave allowance per parent after 6 months (additional months) = **3** month (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "雙親各領滿6個月育嬰留停津貼後,可各再多領3個月,合計最高18個月"
  - p229 Childcare leave days per parent (increased from 30) = **60** day (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "並且從30日增加到60日,兩人合計120日"
  - p230 Reduced working hour per day without pay cut (hours) = **1** hour/(person*day) (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "勞工每日可減少1小時工時且不減薪"
  - p231 Housing subsidy multiplier for newlyweds within 2 years (times base rent subsidy = **1.5** 1 (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "新婚2年內者可加碼至1.5倍(例如租補4000元,則加碼至6000元)"
  - p232 Housing subsidy multiplier for households with newborn (times base rent subsidy) = **2** 1 (2026-05-27..2026-05-27) [DISCARD: Policy parameter, no numerical role.] quote: "育新生兒者加碼至2倍(例如租補4000元,則加碼至8000元)"
- `https://www.ey.gov.tw/File/628036A254DC11B2?A=C` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.ltn.com.tw/news/life/paper/1685195` -> **snapshot** (snapshot 20260101071826); points raw/verified 5/0
- `https://repository.kihasa.re.kr/en/bitstream/201002/35812/1/%ec%97%b0%ea%b5%ac%eb%b3%b4%ea%b3%a0%ec%84%9c%202014-22-3%28EWC%29.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://paternet.fr/wp-content/uploads/pdf/2018/02/20180201-institute-for-family-studies.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.xiaohongshu.com/discovery/item/69d5c4a8000000001a02151e` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (scale word '万' not supported by quote or table header: 2; period year 2012 does not appear in the page text or URL (likely mis-dated): 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 2)

### d7 [forecasts_markets] Official projections and demographic forecasts

Hypothesis: NDC population projections and any 2026 monthly birth forecasts give a baseline level for 2026; comparing projected annual births to the year-to-date actuals constrains the implied September value.

Queries issued by the searcher: 國發會 人口推估 2026 出生數 推估; Taiwan population projection 2026 births NDC; 內政部 戶政司 114年9月 出生數 統計 2025年9月 出生; Taiwan births July 2026 54,250 January through July interior ministry; 國發會 2026 出生數 推估 人口推估; 2026年 台灣 出生數 預估 上半年 出生; 內政部 2026年7月 戶口統計 出生數 7月新生兒 累計 1至7月; 2025年9月 出生數 台灣 新生兒 內政部 統計; 國發會 2026 出生數 推估 人口推估; Taiwan population projection 2026 births NDC; 內政部 戶政司 人口統計 出生數 2026年8月 統計; 2025年9月 出生數 內政部 台灣 新生兒 9月

- `https://www.ndc.gov.tw/News_Content.aspx?n=114AAE178CD95D4C&s=6F7655EDC5AAD458` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://focustaiwan.tw/society/202608290010` -> **snapshot** (snapshot 20260830111536); points raw/verified 4/4
  - p233 NDC projected Taiwan population decline from 2026 level to 2075 = **48** % (2026-01-01..2075-12-31) [DISCARD: Projection, irrelevant.] quote: "Taiwan's population is projected to fall 48 percent from 2026 levels to 12.15 million by 2075"
  - p234 NDC projected Taiwan population in 2075 = **12,150,000** person (2075-01-01..2075-12-31) [DISCARD: Projection, irrelevant.] quote: "to 12.15 million by 2075 because of a declining birth rate and a rapidly aging population"
  - p235 Taiwan newborns (live births) in 2025, record low, 10th consecutive annual decli = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "With the number of newborns in Taiwan falling for the 10th consecutive year to a record low of 107,812 in 2025"
  - p236 NDC forecast: Taiwan newborns in 2026 likely below 100,000 (upper bound) = **100,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "the figure is likely to decline further to below 100,000 this year, the NDC said"
- `http://dev.taisounds.news/news/content/76/285689` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.setn.com/news/1897905` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/amp/story/7314/9720922` -> **snapshot** (snapshot 20260908021017); points raw/verified 15/15
  - p237 NDC 2026 annual births projection, low scenario = **92,000** births (2026-01-01..2026-12-31) [keep: ] quote: "國發會指出,今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p238 NDC 2026 annual births projection, medium scenario = **94,000** births (2026-01-01..2026-12-31) [keep: ] quote: "國發會指出,今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p239 NDC 2026 annual births projection, high scenario = **97,000** births (2026-01-01..2026-12-31) [keep: ] quote: "國發會指出,今年新生兒人數低、中、高推估分別約9.2萬、9.4萬及9.7萬人"
  - p240 NDC 2075 births projection, medium scenario = **27,000** births (2075-01-01..2075-12-31) [DISCARD: 2075 projection, irrelevant.] quote: "若以中推估觀察,到2075年新生兒更只剩2.7萬人,不到今年的三成。"
  - p241 NDC 2026 deaths projection = **199,000** deaths (2026-01-01..2026-12-31) [DISCARD: Deaths projection, irrelevant.] quote: "反觀死亡人數將從今年19.9萬人增至2075年的30.5萬人"
  - p242 NDC 2075 deaths projection = **305,000** deaths (2075-01-01..2075-12-31) [DISCARD: Deaths projection, irrelevant.] quote: "反觀死亡人數將從今年19.9萬人增至2075年的30.5萬人"
  - p243 NDC 2026 natural increase projection = **105,000** persons (2026-01-01..2026-12-31) [DISCARD: Natural increase projection, irrelevant.] quote: "使人口自然增加由今年負10.5萬人,進一步擴大至負27.8萬人。"
  - p244 NDC 2075 natural increase projection = **278,000** persons (2075-01-01..2075-12-31) [DISCARD: Natural increase projection, irrelevant.] quote: "使人口自然增加由今年負10.5萬人,進一步擴大至負27.8萬人。"
  - p245 Taiwan total fertility rate, 2025 (prior year) = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "國發會引用內政部數據指出,台灣去年總生育率降至0.695人"
  - p246 Japan total fertility rate (comparison) = **1.14** births per woman (not stated (page dated 2026-08-29)) [keep: ] quote: "低於日本1.14人、新加坡0.87人、韓國0.8人"
  - p247 Singapore total fertility rate (comparison) = **0.87** births per woman (not stated (page dated 2026-08-29)) [keep: ] quote: "低於日本1.14人、新加坡0.87人、韓國0.8人"
  - p248 South Korea total fertility rate (comparison) = **0.8** births per woman (not stated (page dated 2026-08-29)) [keep: ] quote: "低於日本1.14人、新加坡0.87人、韓國0.8人"
  - p249 NDC 2075 total fertility rate projection, high scenario = **1.1** births per woman (2075-01-01..2075-12-31) [DISCARD: 2075 TFR projection, irrelevant.] quote: "預估到2075年,高、中、低情境下的生育率分別為1.1人、0.8人及0.6人。"
  - p250 NDC 2075 total fertility rate projection, medium scenario = **0.8** births per woman (2075-01-01..2075-12-31) [DISCARD: 2075 TFR projection, irrelevant.] quote: "預估到2075年,高、中、低情境下的生育率分別為1.1人、0.8人及0.6人。"
  - p251 NDC 2075 total fertility rate projection, low scenario = **0.6** births per woman (2075-01-01..2075-12-31) [DISCARD: 2075 TFR projection, irrelevant.] quote: "預估到2075年,高、中、低情境下的生育率分別為1.1人、0.8人及0.6人。"
- `https://www.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://indonesia.focustaiwan.tw/business/202608280011` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/aipl/202608280311.aspx` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bwplus.com.tw/Newsparse/article/1112460836.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/story/7241/9059548` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/campus/20251010000241-261509` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://world.storm.mg/articles/1160154` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] Taiwan MOI monthly births

Hypothesis: August 2026 registered births (published ~2026-09-10, just after cutoff) would anchor the latest level and the August-to-September seasonal ratio; without it the series_auto route relies on July and a 2025 seasonal factor.

Queries issued by the searcher: 內政部 戶政司 出生數 2026年7月 統計; Taiwan births August 2025 monthly statistics Ministry of Interior 11,000; 內政部 2025年9月 出生數 新生兒 9月出生 戶口統計; 內政部戶政司 人口統計資料 出生數按登記日期 月 統計表; 內政部 戶政司 出生數 2026年8月; MOI Taiwan births August 2026 monthly statistics household registration; 2025年9月 出生數 內政部 戶口統計 1萬 人 較上月; 內政部 2026年7月 出生數 7906 戶口統計; 內政部 戶政司 出生數 2026年8月; MOI Taiwan births August 2026 monthly statistics; 內政部 2026年7月 出生數 7,906 戶口統計; 內政部戶政司 統計速報 出生數 按月 2025年 各月出生數表

- `https://udn.com/news/story/7314/9745834` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ettoday.net/news/20260910/3234910.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.storm.mg/article/11163388` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6437303` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rti.org.tw/news?uid=3&pid=231114` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://open2.idataiwan.com/5320/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rti.org.tw/news?uid=3&pid=225273` -> **snapshot** (snapshot 20260815163625); points raw/verified 15/14
  - p252 Taiwan population at end of July 2026 (MOI household registration) = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年(2026年)7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p253 Live births registered in Taiwan, July 2026 = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p254 Change in monthly live births, June 2026 to July 2026 = **582** births registered (2026-06-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p255 Cumulative live births registered in Taiwan, January-July 2026 = **54,250** births registered (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p256 Year-on-year decrease in cumulative live births, January-July 2025 to January-Ju = **10,064** births registered (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人"
  - p257 Year-on-year change in live births, July 2025 to July 2026 = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人"
  - p258 Crude birth rate, July 2026 (annualised) = **4.01** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "約每5.6分鐘出生一個嬰兒,折合年粗出生率為千分之4.01"
  - p259 Average minutes between births, July 2026 = **5.6** minutes per birth (2026-07-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒"
  - p260 Deaths registered in Taiwan, July 2026 = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人,平均約每2.6分鐘1人死亡"
  - p261 Cumulative deaths registered in Taiwan, January-July 2026 = **115,628** deaths registered (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月累計數據來看,死亡數共11萬5628人"
  - p262 Natural increase (births minus deaths), Taiwan, July 2026 = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p263 Net in-migration (moves in minus moves out), Taiwan, July 2026 = **650** person (2026-07-01..2026-07-31) [keep: ] quote: "淨遷入人口數為650人"
  - p264 Total population change, June 2026 to July 2026 = **8,563** person (2026-06-01..2026-07-31) [keep: ] quote: "7月總人口較6月減少8563人"
  - p265 Population aged 0-14, Taiwan, end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=a993b8150b6c4f59b5ce02b47e347ed0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/story/7238/9681382` -> **snapshot** (snapshot 20260816173325); points raw/verified 15/0
- `https://www.taiwannews.com.tw/news/6197660` -> **snapshot** (snapshot 20260711082533); points raw/verified 15/0
- `https://merit-times.com.tw/NewsPage.aspx?unid=918288` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mdnkids.com/content.asp?Link_String_=23AB00000HSYFWF` -> **snapshot** (snapshot 20251010211725); points raw/verified 5/0
- dropped by code checks: 36 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 33; number: compound CJK number (519万548): leave scale_word empty and give the whole number: 2)

### b2 [related_series] Taiwan conception timing

Hypothesis: September births correspond to conceptions around December 2025; December 2025 marriage counts and any 2026 prenatal first-visit counts would constrain the September level independently of the registration trend.

Queries issued by the searcher: 台灣 2025年12月 結婚對數 內政部 統計; 台灣 出生數 2026年 月別 內政部 統計; 孕婦 初次產檢 人數 2026 月別 統計; ris.gov.tw 戶口統計速報 結婚對數 出生數 按月 115年; 台灣 2025年12月 結婚對數 統計; 內政部 戶政司 結婚對數 按月 2025年12月; 2026年 新生兒 出生數 內政部 每月 統計 6月 7月; 孕婦 初次產檢 人數 統計 月別 國健署; 台灣 2025年12月 結婚對數 內政部; 孕婦 初次產檢 人數 2026 月別 統計; 2026年7月 出生數 內政部 戶口統計 新生兒; 2025年9月 出生數 台灣 內政部 戶口統計; 2025年9月 出生數 9027 新生兒 內政部 9月戶口統計; 2026年1月 2月 3月 4月 出生數 新生兒 內政部 戶口統計

- `https://www.ris.gov.tw/info-liferay/app/channel/newsEnglishDetail/26245250` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/15
  - p266 Taiwan registered marriages (couples), December 2025 = **10,816** couple (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p267 Taiwan registered marriages, opposite-sex couples, December 2025 = **10,456** couple (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p268 Taiwan registered same-sex marriages (couples), December 2025 = **360** couple (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p269 Taiwan registered marriages (couples), November 2025 = **8,586** couple (2025-11-01..2025-11-30) [keep: ] quote: "8,586 8,327 259 4.48 1.52 - 4.03 1.23 - 4.38 0.81 -"
  - p270 Taiwan registered marriages (couples), October 2025 = **10,735** couple (2025-10-01..2025-10-31) [keep: ] quote: "10,735 10,428 307 5.42 0.58 4.78 0.48 - 4.37 0.74 -"
  - p271 Taiwan registered marriages (couples), full year 2025 = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "there were 104,376 marriages registered in 2025, including 3,305 same-sex marriages"
  - p272 Taiwan registered marriages (couples), full year 2024 = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "2024(1) 123,061 53,469 5.26 2.28"
  - p273 Taiwan registered births, September 2025 = **8,603** birth (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p274 Taiwan registered births, December 2025 = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p275 Taiwan registered births, November 2025 = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p276 Taiwan registered births, October 2025 = **9,458** birth (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p277 Taiwan registered births, full year 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p278 Taiwan registered births, full year 2024 = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p279 Taiwan crude marriage rate, December 2025 (per 1,000 population, annual basis) = **5.47** marriage per 1,000 person (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p280 Taiwan crude birth rate, September 2025 (per 1,000 population, annual basis) = **4.49** birth per 1,000 person (2025-09-01..2025-09-30) [keep: ] quote: "4.78 5.80 4.73 4.52 4.25 4.67 4.51 4.27 4.49 4.78"
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/aipl/202601090067.aspx` -> **snapshot** (snapshot 20260207175022); points raw/verified 15/15
  - p281 Taiwan marriages (couples) registered, full year 2025 = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "婚姻部分,去年結婚對數10萬4376對,折合年粗結婚率為千分之4.47"
  - p282 Taiwan marriages (couples) registered, full year 2024 = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "相比2024年的12萬3061對,減少1萬8685對"
  - p283 Change in Taiwan marriages (couples), 2025 vs 2024 = **18,685** couple (2025-01-01..2025-12-31) [keep: ] quote: "相比2024年的12萬3061對,減少1萬8685對"
  - p284 Taiwan crude marriage rate, full year 2025 (marriages per 1,000 population) = **4.47** couple per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "去年結婚對數10萬4376對,折合年粗結婚率為千分之4.47"
  - p285 Taiwan live births registered, December 2025 (single month) = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月單月新生兒出生數為9027人"
  - p286 Change in Taiwan monthly live births, December 2025 vs November 2025 = **1,081** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月單月新生兒出生數為9027人,比11月增加1081人"
  - p287 Change in Taiwan monthly live births, December 2025 vs December 2024 = **3,469** birth (2025-12-01..2025-12-31) [keep: ] quote: "但相較前年同期減少3469人"
  - p288 Taiwan live births registered, full year 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "2025年新生兒數為10萬7812人,連10年下降,再創新低"
  - p289 Taiwan live births registered, full year 2024 = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024年13萬4856人,加上去年僅有10萬餘人,已連續10年下降"
  - p290 Taiwan live births registered, full year 2023 = **135,571** birth (2023-01-01..2023-12-31) [keep: ] quote: "2023年13萬5571人"
  - p291 Taiwan live births registered, full year 2022 = **138,986** birth (2022-01-01..2022-12-31) [keep: ] quote: "2022年13萬8986人"
  - p292 Taiwan live births registered, full year 2021 = **153,820** birth (2021-01-01..2021-12-31) [keep: ] quote: "2021年15萬3820人"
  - p293 Taiwan live births registered, full year 2020 = **165,249** birth (2020-01-01..2020-12-31) [keep: ] quote: "2020年16萬5249人"
  - p294 Taiwan live births registered, full year 2019 = **177,767** birth (2019-01-01..2019-12-31) [keep: ] quote: "2019年17萬7767人"
  - p295 Taiwan live births registered, full year 2018 = **181,601** birth (2018-01-01..2018-12-31) [keep: ] quote: "2018年18萬1601人"
- `https://verybaby.tw/wiki/39832` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ctwant.com/article/465457/` -> **snapshot** (snapshot 20260811144346); points raw/verified 15/15
  - p296 Taiwan total marriages (couple pairs) registered, full year 2025 = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "全年結婚對數為10萬4376對,年粗結婚率為每千人4.47對,較前一年減少1萬8635對"
  - p297 Taiwan marriages change vs prior year, full year 2025 (decrease) = **18,635** couple (2025-01-01..2025-12-31) [keep: ] quote: "全年結婚對數為10萬4376對,年粗結婚率為每千人4.47對,較前一年減少1萬8635對"
  - p298 Taiwan crude marriage rate, full year 2025 (couples per 1,000 population) = **4.47** couple per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "年粗結婚率為每千人4.47對"
  - p299 Taiwan total live births, full year 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "2025年全年新生兒人數僅10萬7812人"
  - p300 Taiwan total live births, full year 2024 = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "較2024年的13萬4856人驟減2萬7044人"
  - p301 Taiwan live births change 2025 vs 2024 (decrease) = **27,044** birth (2025-01-01..2025-12-31) [keep: ] quote: "較2024年的13萬4856人驟減2萬7044人"
  - p302 Taiwan crude birth rate, full year 2025 (births per 1,000 population) = **4.62** birth per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "折合年粗出生率僅為每千人4.62人"
  - p303 Taiwan total live births, full year 2016 = **208,440** birth (2016-01-01..2016-12-31) [keep: ] quote: "從2016年20萬8440人逐年遞減至2025年僅剩10萬餘人"
  - p304 Taiwan total deaths, full year 2025 = **200,268** death (2025-01-01..2025-12-31) [keep: ] quote: "2025年全年共計20萬268人死亡"
  - p305 Taiwan crude death rate, full year 2025 (deaths per 1,000 population) = **8.58** death per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "年粗死亡率為每千人8.58人"
  - p306 Taiwan total population, end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "全年度總人口為2329萬9132人"
  - p307 Taiwan population change 2025 vs 2024 (decrease) = **101,088** person (2025-01-01..2025-12-31) [keep: ] quote: "較2024年同期減少10萬1088人"
  - p308 Taiwan average daily net population decrease, 2025 = **277** person per day (2025-01-01..2025-12-31) [keep: ] quote: "平均每日淨減少約277人"
  - p309 Taiwan in-migrants, December 2025 = **74,682** person (2025-12-01..2025-12-31) [keep: ] quote: "2025年12月遷入人口為7萬4682人,較2024年同月減少1萬1838人"
  - p310 Taiwan divorces (couple pairs), full year 2025 = **52,101** couple (2025-01-01..2025-12-31) [keep: ] quote: "離婚對數為5萬2101對,年粗離婚率為每千人2.23對"
- `https://www.cna.com.tw/news/aipl/202601090067.aspx?utm_source=LINE&utm_medium=linetoday&utm_campaign=lineback` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%8F%B0%E7%81%A3%E9%80%B2%E5%85%A5-%E8%80%81%E4%BA%BA%E5%9C%8B-%E6%99%82%E4%BB%A3-%E9%AB%98%E9%BD%A1%E4%BA%BA%E5%8F%A3%E5%` -> **snapshot** (snapshot 20260109123517); points raw/verified 15/15
  - p311 Taiwan total marriages (couples) in 2025 full year = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "全年結婚對數為10萬4376對,年粗結婚率為每千人4.47對,較前一年減少1萬8635對"
  - p312 Taiwan marriages change in 2025 vs prior year (couples) = **18,635** couple (2025-01-01..2025-12-31) [keep: ] quote: "全年結婚對數為10萬4376對,年粗結婚率為每千人4.47對,較前一年減少1萬8635對"
  - p313 Taiwan crude marriage rate 2025 (couples per 1,000 population) = **4.47** couple per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "年粗結婚率為每千人4.47對"
  - p314 Taiwan births registered in December 2025 = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月出生數為9027人,較去年11月增加1081人"
  - p315 Taiwan births registered in December 2025, month-on-month change = **1,081** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月出生數為9027人,較去年11月增加1081人"
  - p316 Taiwan births registered in December 2025, year-on-year change = **3,469** birth (2025-12-01..2025-12-31) [keep: ] quote: "114年12月出生數為9027人,約每4.9分鐘出生一個嬰兒,折合年粗出生率為4.56?,較上年同月減少3469人,較上月增加1081人"
  - p317 Taiwan births registered in December 2024 (prior-year same month) = **12,496** birth (2024-12-01..2024-12-31) [keep: ] quote: "去年12月新生兒為9027人,前年同期的1萬2496人相比少了3469人"
  - p318 Taiwan births registered in December 2025, year-on-year decline rate = **27.76** % (2025-12-01..2025-12-31) [keep: ] quote: "去年12月出生僅9,027人、年減逾27.76%"
  - p319 Taiwan total live births in 2025 full year = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "2025年全年新生兒人數僅10萬7812人,較2024年的13萬4856人驟減2萬7044人"
  - p320 Taiwan total live births in 2024 full year = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2025年全年新生兒人數僅10萬7812人,較2024年的13萬4856人驟減2萬7044人"
  - p321 Taiwan births decline 2025 vs 2024 (births) = **27,044** birth (2025-01-01..2025-12-31) [keep: ] quote: "較2024年的13萬4856人驟減2萬7044人,折合年粗出生率僅為每千人4.62人"
  - p322 Taiwan crude birth rate 2025 (births per 1,000 population) = **4.62** birth per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "折合年粗出生率僅為每千人4.62人,創下內政部統計以來最低紀錄"
  - p323 Taiwan total live births in 2016 full year = **208,440** birth (2016-01-01..2016-12-31) [keep: ] quote: "從2016年20萬8440人逐年遞減至2025年僅剩10萬餘人"
  - p324 Taiwan total live births in 2023 full year = **135,571** birth (2023-01-01..2023-12-31) [keep: ] quote: "112年13萬5571人、113年13萬4856人,114年更僅有10萬7812人,創下新低"
  - p325 Taiwan total population at end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "全年度總人口為2329萬9132人,較2024年同期減少10萬1088人"
- `https://www.rti.org.tw/news?uid=3&pid=225273` -> **snapshot** (snapshot 20260815163625); points raw/verified 15/14
  - p326 Taiwan live births registered in July 2026 (monthly births) = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p327 Taiwan live births registered January-July 2026 (cumulative) = **54,250** births registered (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p328 Change in Taiwan January-July live births, 2026 vs 2025 = **10,064** births registered (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人"
  - p329 Change in Taiwan July live births, 2026 vs June 2026 = **582** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒,折合年粗出生率為千分之4.01,較去年同期減少1033人,相比今年6月增加582人"
  - p330 Change in Taiwan July live births, 2026 vs July 2025 = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人"
  - p331 Taiwan July 2026 crude birth rate (annualised) = **4.01** births per 1,000 population (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為千分之4.01"
  - p332 Minutes per birth implied in July 2026 = **5.6** minutes per birth (2026-07-01..2026-07-31) [keep: ] quote: "約每5.6分鐘出生一個嬰兒"
  - p333 Taiwan population at end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年(2026年)7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p334 Taiwan deaths registered in July 2026 = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人,平均約每2.6分鐘1人死亡"
  - p335 Taiwan deaths registered January-July 2026 (cumulative) = **115,628** deaths registered (2026-01-01..2026-07-31) [keep: ] quote: "死亡數共11萬5628人,新生兒共5萬4250人"
  - p336 Taiwan natural increase (births minus deaths) July 2026 = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p337 Taiwan population aged 0-14 at end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p338 Taiwan population aged 15-64 at end of July 2026 = **15,835,491** person (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口數1583萬5491人,占68.15%"
  - p339 Taiwan population aged 65+ at end of July 2026 = **4,773,519** person (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
- `https://www.zhihu.com/pin/2059021650029457413` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://crc.sfaa.gov.tw/Uploadfile/Statiscs/80_20250217083057_1506107.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tpta.org.tw/images/forwarded/20190717105842-AFB4809C-3AC9-4A/2030%E5%85%92%E7%AB%A5%E9%86%AB%E7%99%82%E8%88%87%E5%81%A5%E5%BA%B7%E6%94%BF%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [forecasts_markets] NDC monthly path

Hypothesis: If NDC or MOI publishes a monthly 2026 birth path (not just annual), it would resolve whether the 92-97k annual forecast implies a September above or below the simple seasonal extrapolation.

Queries issued by the searcher: 國發會 2026 每月 出生數 推估; 內政部 2026年8月 出生數; 內政部戶政司 戶口統計 2026年8月 出生 7492 統計表; 國發會 2026 人口推估 新聞稿 出生數 9.4萬 產檢 結婚對數; 國發會 2026 每月 出生數 推估; 內政部 2026年8月 出生數; 國發會 人口推估 2026 短期 每月 出生數 推估 產檢件數 月別; 內政部戶政司 戶口統計 2025年 每月 出生數 1月 2月 3月 4月 5月 6月 7月 8月 9月; 國發會 2026 出生數 推估 每月; 內政部 2026年8月 出生數 統計; 內政部 2026年7月 出生數 7906 人口統計; 國發會 中華民國人口推估 2026 9.4萬 出生 報告 8月28日

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])7492(?!\\d|[.,]\\d)']; no pages fetched**


### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'taiwan birth rate', 'taiwan population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p17', 'p205'] All three give May 2026 registered births = 6,832; p17's value field is mislabeled (it is the June-vs-May change, 492) but the quote confirms 6,832. Same MOI source, so not independent.
- corroborating: ['p16', 'p78', 'p206'] June 2026 = 7,324 births across three outlets; same MOI release.
- corroborating: ['p15', 'p75'] Identical H1 2026 cumulative 46,344; duplicate of same source.
- corroborating: ['p89', 'p103', 'p204'] July 2026 = 7,906 births; same MOI release via CNA/RTI/PTS.
- corroborating: ['p90', 'p105'] Jan-Jul 2026 cumulative 54,250; duplicate.
- corroborating: ['p91', 'p106'] Jan-Jul YoY decline 10,064; duplicate.
- corroborating: ['p92', 'p93', 'p104', 'p107', 'p207', 'p208'] July 2026 vs June +582 and vs July 2025 -1,033 (-11.56%); consistent across outlets.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p53', 'p162', 'p235'] 2025 monthly series sums to 107,812, matching the stated 2025 annual total; internally consistent MOI series.
- corroborating: ['p37', 'p38', 'p161', 'p160'] 2024 births 134,856 and crude rate 5.76; 2025 rate 4.62 implies ~107.8k, consistent with -20% YoY.
- corroborating: ['p50', 'p51', 'p52', 'p120', 'p121', 'p122', 'p237', 'p238', 'p239', 'p236'] NDC 2026 forecast 92k/94k/97k repeated across sources; one underlying projection, not independent.
- conflicting: ['p39', 'p41', 'p186', 'p187'] January 2026: p39 gives 8,723 directly; p186's 'implied' 2,200 is a mislabeled change, and 6,523+2,200=8,723 confirms p39. p186 value is unusable as a level.
- corroborating: ['p2', 'p185'] February 2026 = 6,523 all-time low; duplicate.
- corroborating: ['p3', 'p65'] April 2026 = 8,144; duplicate.
- corroborating: ['p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139', 'p140', 'p141'] South Korea 2026 births rising ~15% YoY — a regional analogue that conflicts in direction with Taiwan's continued decline; different entity, so contextual only.
- corroborating: ['p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159'] Japan births roughly flat/slightly up in 2026 — another analogue showing no rebound in Taiwan is plausible but not guaranteed.
- corroborating: ['p96', 'p102', 'p203'] July 2026 population 23,235,002; duplicate.
- corroborating: ['p98', 'p110', 'p210'] July 2026 deaths 17,119; duplicate.
- corroborating: ['p100', 'p112'] July natural decrease 9,213; duplicate.
- corroborating: ['p114', 'p115', 'p215'] 0-14 share 11.30% end-July; duplicate.
- corroborating: ['p128', 'p245'] 2025 TFR 0.695; duplicate.
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p246', 'p247', 'p248'] TFR comparisons across countries; same source, contextual.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Single MOI/RIS monthly table for 2025; internally consistent and the authoritative 2025 monthly baseline. p53/p162/p235/p277/p288/p299/p319 repeat the same 107,812 annual total from the same MOI sourc
- corroborating: ['p1', 'p3', 'p65', 'p2', 'p185', 'p16', 'p78', 'p205', 'p206', 'p89', 'p103', 'p204', 'p253', 'p326'] 2026 monthly MOI registration counts from multiple outlets; May 6,832, June 7,324, July 7,906, April 8,144, February 6,523 all agree across sources. Same underlying MOI measurement, so agreement is no
- corroborating: ['p15', 'p75', 'p90', 'p105', 'p255', 'p327'] Jan-Jun 46,344 and Jan-Jul 54,250 cumulative totals agree across outlets; consistent with monthly sums (46,344 + 7,906 = 54,250).
- corroborating: ['p91', 'p106', 'p256', 'p328'] Jan-Jul 2026 down 10,064 vs 2025's 64,314; implies 2025 Jan-Jul = 64,314, consistent with 2025 monthly table.
- corroborating: ['p50', 'p51', 'p52', 'p120', 'p121', 'p122', 'p237', 'p238', 'p239', 'p236'] NDC 2026 annual projection 92k/94k/97k repeated across sources; same NDC projection, not independent. p236 (<100k) is a looser bound consistent with the range.
- corroborating: ['p131', 'p132', 'p133', 'p134', 'p136', 'p137', 'p138', 'p139', 'p140', 'p141'] South Korea 2026 births rising ~15% YoY — a regional analogue that conflicts in direction with Taiwan's continued decline; useful only as a directional cross-check, not a transferable level.
- corroborating: ['p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159'] Japan births roughly flat/slightly up in 2026 — another analogue showing no regional rebound strong enough to overturn Taiwan's own declining registration trend.
- corroborating: ['p266', 'p267', 'p268', 'p269', 'p270', 'p271', 'p272', 'p281', 'p282', 'p283', 'p284', 'p296', 'p297', 'p298', 'p311', 'p312', 'p313'] Marriage counts for late 2025 / full 2025; December 2025 marriages (10,816) are the conception-month proxy for September 2026 births. Same MOI source.
- corroborating: ['p37', 'p38', 'p278', 'p289', 'p290', 'p291', 'p292', 'p293', 'p294', 'p295', 'p300', 'p301', 'p303', 'p320', 'p321', 'p323', 'p324'] Historical annual birth series 2016-2025 from MOI; establishes the long declining trend and the 2024→2025 drop of ~20%.
- corroborating: ['p160', 'p161', 'p302', 'p322'] Crude birth rate 2025 = 4.62, 2024 = 5.76; consistent with annual totals and population.
- corroborating: ['p54', 'p128', 'p245'] TFR 2025 ≈ 0.695-0.7 from MOI/NDC; consistent across sources.
- corroborating: ['p12', 'p18', 'p44', 'p96', 'p102', 'p203', 'p252', 'p333'] Population totals by month; consistent declining series, not directly used for births.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY change factor vs September 2025 | 0.88 | 0.8..0.96 | 0.7838..0.9798 (widened) | 1 | unused | 2026 monthly YoY declines: Jan -772/9,495≈-8%, Jul -1,033/8,939≈-11.6%, H1 -9,031/55,375≈-16.3%. September 2025 was 8,603; a factor near 0.88 (≈-12%) sits between the July and H1 declines, reflecting continued but not accelerating decline. | September 2026 registration follows the 2026 YoY decline pattern seen in H1 and July. | August 2026 births (published ~Sep 10) showing a sharp rebound or a much steeper fall than -12% YoY. |
| a2 | September share of annual births | 0.083 | 0.078..0.088 | 0.05858..0.1172 (widened) | 1 | m2 (m2) | From 2025 monthly table, September 8,603 / 107,812 ≈ 0.0798; September is typically near the annual average (1/12≈0.083) with a modest seasonal bump. Range spans 0.078-0.088. | 2026 monthly seasonal distribution resembles 2025. | Evidence of a large shift in the 2026 seasonal birth pattern. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | 7,609 | ['p25', 'p27', 'p89'] / [] | [] |  | 1.00 | B1 of 3 blocks; median of blocks: this block is the median | p25: period 2025-09-01..2025-09-30 is not the same calendar period as 2026-07-01..2026-07-31; p26: period 2025-08-01..2025-08-31 is not the same calendar period as 2026-07-01..2026-07-31; p28: period  |
| m2 | formula_mc | 7,796 | ['p121'] / ['a2'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | series_auto | 7,206 | ['p29', 'p28', 'p27', 'p25', 'p1', 'p16', 'p89'] / [] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m2 coverage: the whole target

Method details (computed by code):

- m1 yoy_scaling: target 2025 8,603 x signal 7,906 / 8,939 (growth 0.8844); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p121 * a2; Monte Carlo P10 to P90 5,274 to 11,528; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p29), 2025-06 (p28), 2025-07 (p27), 2025-09 (p25), 2026-05 (p1), 2026-06 (p16), 2026-07 (p89) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 4 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy\|pairs3\|h2 of table bench-d12f86e0-1013c974)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,609 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,796 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 7,206 (width x/÷1.23, benchmark calibration). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.37; Birge ratio 0.19 (not above one, so no widening); final width x/÷1.37.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p25, from m3); the estimate is -11.6% against it.

Result: central **7,609** birth, 80% interval [5,552, 10,428] birth, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 0.00

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 7,609 birth (80% model-based interval 5,552 to 10,428 birth), covering live births registered in Taiwan during September 2026 as counted by the Ministry of the Interior's monthly household registration statistics (by date of registration).

Main evidence: the estimate is anchored on last year's same month, 8,603 births registered, scaled by recent year-on-year growth. July 2026 registrations were 7,906 births registered versus 8,939 births registered in July 2025, and the three-month YoY route uses 6,832 births, 7,324 births registered, 8,433 births registered and 8,968 births registered. A cross-check multiplies the NDC annual projection 94,000 birth by an assumed September share 0.083 (range 0.05858 to 0.1172).

Observed: the monthly registration counts and the annual projection. Assumed/transferred: the September share and the carry-forward of recent YoY decline.

Code combined three blocks with equal weight per block because methods sharing inputs were grouped, not treated as independent; widths came from benchmark calibration and Monte Carlo, not demonstrated accuracy.

Main risk: September 2026 is unobserved, and late registration or a shift in the recent decline could move the count. Better evidence would be August 2026 registrations and any early September figures.

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 September share of annual births: 0.083 [n], range 0.05858 to 0.1172 (range widened by code); used by m2. Overturned by: Evidence of a large shift in the 2026 seasonal birth pattern.

Method details (computed by code):
- m1 yoy_scaling: target 2025 8,603 x signal 7,906 / 8,939 (growth 0.8844); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p121 * a2; Monte Carlo P10 to P90 5,274 to 11,528; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p29), 2025-06 (p28), 2025-07 (p27), 2025-09 (p25), 2026-05 (p1), 2026-06 (p16), 2026-07 (p89) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 4 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy|pairs3|h2 of table bench-d12f86e0-1013c974)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,609 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,796 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 7,206 (width x/÷1.23, benchmark calibration). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.37; Birge ratio 0.19 (not above one, so no widening); final width x/÷1.37.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p25, from m3); the estimate is -11.6% against it.

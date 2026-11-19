# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan (Republic of China) during September 2026, as counted in the Ministry of the Interior's monthly household registration statistics (births registered in the month, by month of registration/occurrence as published in the MOI 'Household Registration Statistics | unit births registered in September 2026 | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior (內政部), Department of Household Registration (戶政司), Taiwan

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household registration series

Hypothesis: September registered births in recent years, plus the most recent months published before the cutoff (e.g., Jan–Jul 2026), anchor a trend-plus-seasonality forecast; September typically shows a modest seasonal pattern relative to adjacent months. Target = recent monthly level × September seasonal factor × trend adjustment.

Queries issued by the searcher: 內政部 戶籍人口統計 出生 按月 統計表; Taiwan Ministry of Interior births by month statistics 2025 monthly; 台灣 2026年 出生數 每月 內政部 戶口統計 新生兒; 內政部 戶政司 戶籍人口統計 月報 出生數 統計下載 ris.gov.tw; 內政部 戶籍人口統計 出生 按月 統計; Taiwan births by month 2025 monthly statistics Ministry of Interior; 台灣 2026 出生數 月別 統計; 內政部戶政司 出生數及粗出生率 按登記 統計表 2025 每月; 2024年9月 出生數 內政部 戶口統計 新生兒; 2023年9月 新生兒 出生數 內政部 戶口統計; 內政部 戶籍人口統計 出生 按月 統計表; Taiwan births by month 2025 2026 Ministry of Interior monthly statistics; 內政部 2025年9月 新生兒 出生數 公布 9月出生; ris.gov.tw 戶籍人口統計 月報 出生人數 統計表 中華民國114年9月

- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6153827` -> **snapshot** (snapshot 20260710132942); points raw/verified 30/30
  - p1 Taiwan population at end of June 2025 = **23,346,741** person (2025-06-30..2025-06-30) [keep: ] quote: "As of the end of June, the population stood at 23,346,741, a decrease of 8,729 from May, per CNA."
  - p2 Taiwan population decrease from May to June 2025 = **8,729** person (2025-06-01..2025-06-30) [keep: ] quote: "As of the end of June, the population stood at 23,346,741, a decrease of 8,729 from May, per CNA."
  - p3 Taiwan population annual decrease (June 2025 vs June 2024) = **66,158** person (2024-07-01..2025-06-30) [keep: ] quote: "Compared to the same time last year, the population dropped by 66,158, averaging a daily decline of 181.25 people."
  - p4 Average daily population decline in Taiwan (year to June 2025) = **181** person/day (2024-07-01..2025-06-30) [keep: ] quote: "Compared to the same time last year, the population dropped by 66,158, averaging a daily decline of 181.25 people."
  - p5 Newborns registered in Taiwan, June 2025 = **8,968** birth (2025-06-01..2025-06-30) [keep: ] quote: "Following record lows in April and May, the number of newborns in June rose to 8,968, ending a three-month slump."
  - p6 Births registered in Taiwan, first half 2025 (cumulative) = **55,375** birth (2025-01-01..2025-06-30) [keep: ] quote: "For the first half of 2025, births totaled 55,375, down 8,499 from the same period last year."
  - p7 Change in Taiwan first-half births, 2025 vs 2024 = **8,499** birth (2025-01-01..2025-06-30) [keep: ] quote: "For the first half of 2025, births totaled 55,375, down 8,499 from the same period last year."
  - p8 Average interval between births in Taiwan, June 2025 = **4.8** minute/birth (2025-06-01..2025-06-30) [keep: ] quote: "In June, a baby was born roughly every 4.8 minutes, with a crude birth rate of 4.67 per 1,000 people."
  - p9 Crude birth rate in Taiwan, June 2025 = **4.67** birth/(1000 person) (2025-06-01..2025-06-30) [keep: ] quote: "In June, a baby was born roughly every 4.8 minutes, with a crude birth rate of 4.67 per 1,000 people."
  - p10 June 2025 births increase over May 2025 = **535** birth (2025-06-01..2025-06-30) [keep: ] quote: "The figure was up 535 from May but still 1,472 fewer than June 2024."
  - p11 June 2025 births shortfall vs June 2024 = **1,472** birth (2025-06-01..2025-06-30) [keep: ] quote: "The figure was up 535 from May but still 1,472 fewer than June 2024."
  - p12 Births registered in Taiwan, January 2025 = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "Monthly birth figures this year were 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April, 8,433 in May, and 8,968 in June."
  - p13 Births registered in Taiwan, February 2025 = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "Monthly birth figures this year were 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April, 8,433 in May, and 8,968 in June."
  - p14 Births registered in Taiwan, March 2025 = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "Monthly birth figures this year were 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April, 8,433 in May, and 8,968 in June."
  - p15 Births registered in Taiwan, April 2025 = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "Monthly birth figures this year were 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April, 8,433 in May, and 8,968 in June."
  - p16 Births registered in Taiwan, May 2025 = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "Monthly birth figures this year were 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April, 8,433 in May, and 8,968 in June."
  - p17 Deaths in Taiwan, June 2025 = **16,554** death (2025-06-01..2025-06-30) [keep: ] quote: "There were 16,554 deaths in June, or about one every 2.6 minutes."
  - p18 Average interval between deaths in Taiwan, June 2025 = **2.6** minute/death (2025-06-01..2025-06-30) [keep: ] quote: "There were 16,554 deaths in June, or about one every 2.6 minutes."
  - p19 Crude death rate in Taiwan, June 2025 = **8.63** death/(1000 person) (2025-06-01..2025-06-30) [keep: ] quote: "This translated to a crude death rate of 8.63 per 1,000 people, up 1,632 from a year earlier and 1,172 more than in May."
  - p20 June 2025 deaths increase vs June 2024 = **1,632** death (2025-06-01..2025-06-30) [keep: ] quote: "This translated to a crude death rate of 8.63 per 1,000 people, up 1,632 from a year earlier and 1,172 more than in May."
  - p21 June 2025 deaths increase vs May 2025 = **1,172** death (2025-06-01..2025-06-30) [keep: ] quote: "This translated to a crude death rate of 8.63 per 1,000 people, up 1,632 from a year earlier and 1,172 more than in May."
  - p22 Natural population change in Taiwan, June 2025 (births minus deaths) = **7,586** person (2025-06-01..2025-06-30) [keep: ] quote: "In terms of natural population change, which is the difference between the number of births and deaths, in June was 7,586."
  - p23 Inbound migration to Taiwan, June 2025 = **71,834** person (2025-06-01..2025-06-30) [keep: ] quote: "In June, 71,834 people moved into Taiwan, down 49,180 from the previous month."
  - p24 Outbound migration from Taiwan, June 2025 = **72,977** person (2025-06-01..2025-06-30) [keep: ] quote: "Outbound migration totaled 72,977, a drop of 50,892, resulting in a net loss of 1,143 people."
  - p25 Net migration loss in Taiwan, June 2025 = **1,143** person (2025-06-01..2025-06-30) [keep: ] quote: "Outbound migration totaled 72,977, a drop of 50,892, resulting in a net loss of 1,143 people."
  - p26 Share of Taiwan population aged 0-14, June 2025 = **11.63** % (2025-06-30..2025-06-30) [keep: ] quote: "By age group, those 0-14 made up 11.63% of the population (2,716,281) and those 15-64 accounted for 68.78% (16,057,007)."
  - p27 Taiwan population aged 0-14, June 2025 = **2,716,281** person (2025-06-30..2025-06-30) [keep: ] quote: "By age group, those 0-14 made up 11.63% of the population (2,716,281) and those 15-64 accounted for 68.78% (16,057,007)."
  - p28 Share of Taiwan population aged 15-64, June 2025 = **68.78** % (2025-06-30..2025-06-30) [keep: ] quote: "By age group, those 0-14 made up 11.63% of the population (2,716,281) and those 15-64 accounted for 68.78% (16,057,007)."
  - p29 Share of Taiwan population aged 65 and older, June 2025 = **19.59** % (2025-06-30..2025-06-30) [keep: ] quote: "People aged 65 and older comprised 19.59% (4,573,453)."
  - p30 Taiwan population aged 65 and older, June 2025 = **4,573,453** person (2025-06-30..2025-06-30) [keep: ] quote: "People aged 65 and older comprised 19.59% (4,573,453)."
- `https://www.163.com/dy/article/KV36R0PT055080L4.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.setn.com/news/1805152` -> **snapshot** (snapshot 20260717005339); points raw/verified 15/15
  - p31 Taiwan total population at end of February 2026 (MOI household registration) = **23,280,273** person (2026-02-01..2026-02-28) [keep: ] quote: "截至2026年2月,台灣總人口是2328萬273人"
  - p32 Month-on-month change in Taiwan total population, February 2026 vs January 2026 = **8,772** person (2026-02-01..2026-02-28) [keep: ] quote: "比1月減少8772人"
  - p33 Consecutive months of Taiwan population decline through February 2026 = **26** month (2026-02-01..2026-02-28) [keep: ] quote: "同時也是連續26個月人口負成長"
  - p34 Live births registered in Taiwan, February 2026 = **6,523** birth (2026-02-01..2026-02-28) [keep: ] quote: "2026年2月新生兒數為6523人,是有紀錄以來首次單月跌破7000人"
  - p35 Deaths in Taiwan, February 2026 = **14,881** person (2026-02-01..2026-02-28) [keep: ] quote: "2026年2月死亡數為1萬4881人"
  - p36 Deaths in Taiwan, January 2026 (implied by February level and month-on-month cha = **2,648** person (2026-01-01..2026-01-31) [DISCARD: Already discarded; implied January 2026 deaths derived by subtraction, not a published figure.] quote: "較2026年1月減少2648人"
  - p37 Annual crude death rate, Taiwan, February 2026 = **8.33** death per 1,000 person (2026-02-01..2026-02-28) [keep: ] quote: "折合年粗死亡率為千分之8.33"
  - p38 Excess of deaths over births in Taiwan, February 2026 = **8,358** person (2026-02-01..2026-02-28) [keep: ] quote: "2月死亡比出生多8358人"
  - p39 Consecutive months of deaths exceeding births in Taiwan through February 2026 = **62** month (2026-02-01..2026-02-28) [keep: ] quote: "台灣連續62個月「生不如死」"
  - p40 Annual crude birth rate, Taiwan, February 2026 = **3.65** birth per 1,000 person (2026-02-01..2026-02-28) [keep: ] quote: "折合年粗出生率為千分之3.65"
  - p41 Month-on-month decrease in Taiwan live births, February 2026 vs January 2026 = **2,200** birth (2026-02-01..2026-02-28) [keep: ] quote: "新生兒數比2026年1月少2200人"
  - p42 Year-on-year decrease in Taiwan live births, February 2026 vs February 2025 = **3,884** birth (2026-02-01..2026-02-28) [keep: ] quote: "也比2025年同期減少3884人"
  - p43 Live births registered in Taiwan, November 2025 = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "比2025年11月的7946人低出許多"
  - p44 Year-on-year decrease in Taiwan total population, February 2026 vs February 2025 = **104,341** person (2026-02-01..2026-02-28) [keep: ] quote: "與2025年同期相比減少10萬4341人"
  - p45 Year-on-year decrease in Taiwan deaths, February 2026 vs February 2025 = **7,007** person (2026-02-01..2026-02-28) [keep: ] quote: "較2025年同期減少7007人"
- `https://www.bigmedia.com.tw/article/1773546826373` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 29/27
  - p46 Taiwan registered births, September 2025 (monthly total) = **8,603** birth (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p47 Taiwan registered births, October 2025 (monthly total) = **9,458** birth (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p48 Taiwan registered births, November 2025 (monthly total) = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p49 Taiwan registered births, December 2025 (monthly total) = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p50 Taiwan registered births, January 2025 (monthly total) = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p51 Taiwan registered births, February 2025 (monthly total) = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p52 Taiwan registered births, March 2025 (monthly total) = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p53 Taiwan registered births, April 2025 (monthly total) = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p54 Taiwan registered births, May 2025 (monthly total) = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p55 Taiwan registered births, June 2025 (monthly total) = **8,968** birth (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p56 Taiwan registered births, July 2025 (monthly total) = **8,939** birth (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p57 Taiwan registered births, August 2025 (monthly total) = **8,464** birth (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p58 Taiwan total registered births, full year 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p59 Taiwan total registered births, full year 2024 = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p60 Taiwan crude birth rate, full year 2025 = **4.62** birth per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "resulting in a crude birth rate of 4.62 per 1,000 population"
  - p61 Taiwan crude birth rate, full year 2024 = **5.76** birth per 1,000 population (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p62 Taiwan crude birth rate, September 2025 (unadjusted, annual basis) = **4.49** birth per 1,000 population (2025-09-01..2025-09-30) [keep: ] quote: "4.78 5.80 4.73 4.52 4.25 4.67 4.51 4.27 4.49 4.78"
  - p63 Taiwan seasonally adjusted birth rate, September 2025 = **4.42** birth per 1,000 population (2025-09-01..2025-09-30) [keep: ] quote: "4.85 6.28 4.50 4.97 4.40 4.91 4.71 4.42 4.55 4.36"
  - p64 Taiwan seasonally adjusted birth rate, October 2025 = **4.36** birth per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "4.85 6.28 4.50 4.97 4.40 4.91 4.71 4.42 4.55 4.36"
  - p65 Taiwan seasonally adjusted birth rate, November 2025 = **3.89** birth per 1,000 population (2025-11-01..2025-11-30) [keep: ] quote: "3.89 4.01 - 0.91 0.52 - 1.26 - 0.79 - 1.36 - 0.85 - 1.05 - 1.34"
  - p66 Taiwan seasonally adjusted birth rate, December 2025 = **4.01** birth per 1,000 population (2025-12-01..2025-12-31) [keep: ] quote: "3.89 4.01 - 0.91 0.52 - 1.26 - 0.79 - 1.36 - 0.85 - 1.05 - 1.34"
  - p67 Coefficient for adjusting October 2025 crude birth rate (seasonal adjustment div = **1.097** 1 (2025-10-01..2025-10-31) [keep: ] quote: "本月份粗出生率調整係數△為1.097"
  - p68 Coefficient for adjusting November 2025 crude birth rate (seasonal adjustment di = **1.066** 1 (2025-11-01..2025-11-30) [keep: ] quote: "本月份粗出生率調整係數△為1.066"
  - p69 Coefficient for adjusting December 2025 crude birth rate (seasonal adjustment di = **1.137** 1 (2025-12-01..2025-12-31) [keep: ] quote: "本月份粗出生率調整係數△為1.137"
  - p70 Taiwan population at end of September 2025 = **23,317,031** person (2025-09-30..2025-09-30) [keep: ] quote: "23,346,741 23,337,936 23,328,343 23,317,031 23,310,853 23,306,085 23,299,132"
  - p71 Taiwan population at end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "there were 9,851,532 households with a total population of 23,299,132"
  - p72 Taiwan registered deaths, September 2025 (monthly total) = **15,387** death (2025-09-01..2025-09-30) [keep: ] quote: "15,382 16,554 16,846 15,226 15,387 15,908 14,771 17,450"
- `https://j-media.tw/Article/Detail/37299` -> **snapshot** (snapshot 20260417185829); points raw/verified 26/26
  - p73 Taiwan annual live births, 2016 = **208,440** birth (2016-01-01..2016-12-31) [keep: ] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p74 Taiwan annual live births, 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p75 OLS annual decline in Taiwan births, 2016-2025 (lower bound) = **10,000** birth (2016-01-01..2025-12-31) [keep: ] quote: "年均減少量約在10,000至11,000人之間,判定係數(R2)高達0.96以上"
  - p76 OLS annual decline in Taiwan births, 2016-2025 (upper bound) = **11,000** birth (2016-01-01..2025-12-31) [keep: ] quote: "年均減少量約在10,000至11,000人之間,判定係數(R2)高達0.96以上"
  - p77 Taiwan annual live births, 2024 (Dragon year) = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024年受到「龍年效應」支撐,全年出生134,856人,年減僅0.5%"
  - p78 Taiwan 2025 annual births year-over-year change = **20.1** % (2025-01-01..2025-12-31) [keep: ] quote: "卻在2025年出生跌至107,812人,年減幅達20.1%,創下史上最大單年跌幅"
  - p79 Taiwan live births, January 2025 = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "2025年1月出生9,495人,2月受農曆年效應拉抬至10,407人"
  - p80 Taiwan live births, February 2025 = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "2025年1月出生9,495人,2月受農曆年效應拉抬至10,407人"
  - p81 Taiwan live births, March 2025 = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p82 Taiwan live births, April 2025 = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p83 Taiwan live births, May 2025 = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p84 Taiwan live births, November 2025 = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "進入下半年,11月更跌至7,946人,12月雖小幅回升至9,027人"
  - p85 Taiwan live births, December 2025 = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "11月更跌至7,946人,12月雖小幅回升至9,027人,全年月均出生人數約為8,984人"
  - p86 Taiwan 2025 average monthly live births = **8,984** birth (2025-01-01..2025-12-31) [keep: ] quote: "12月雖小幅回升至9,027人,全年月均出生人數約為8,984人"
  - p87 Taiwan live births, January 2026 = **8,723** birth (2026-01-01..2026-01-31) [keep: ] quote: "1月出生8,723人,與2025年同月相比年減8.1%"
  - p88 Taiwan January 2026 births year-over-year change = **8.1** % (2026-01-01..2026-01-31) [keep: ] quote: "1月出生8,723人,與2025年同月相比年減8.1%"
  - p89 Taiwan live births, February 2026 (record monthly low) = **6,523** birth (2026-02-01..2026-02-28) [keep: ] quote: "2月份全國新生兒僅6,523人,首度跌破7,000人大關,創下台灣有史以來單月出生人數的最低紀錄"
  - p90 Taiwan February 2026 births year-over-year change = **37.3** % (2026-02-01..2026-02-28) [keep: ] quote: "2月的6,523人讓外界瞠目--單月年減幅高達37.3%"
  - p91 Taiwan live births, January-February 2026 cumulative = **15,246** birth (2026-01-01..2026-02-28) [keep: ] quote: "2026年前兩月合計僅15,246人,與2025年同期的19,902人相比"
  - p92 Taiwan live births, January-February 2025 cumulative = **19,902** birth (2025-01-01..2025-02-28) [keep: ] quote: "2026年前兩月合計僅15,246人,與2025年同期的19,902人相比,實質年減幅仍達23.4%"
  - p93 Taiwan Jan-Feb 2026 births year-over-year change = **23.4** % (2026-01-01..2026-02-28) [keep: ] quote: "與2025年同期的19,902人相比,實質年減幅仍達23.4%"
  - p94 Forecast Taiwan 2026 annual births, conservative scenario (Mar-Dec -10% YoY) = **94,362** birth (2026-01-01..2026-12-31) [keep: ] quote: "在保守情境中,假設3至12月各月年減10%,全年合計約94,362人,勉強守住"
  - p95 Forecast Taiwan 2026 annual births, neutral scenario (Mar-Dec -15% YoY) = **89,967** birth (2026-01-01..2026-12-31) [keep: ] quote: "在中性情境中,以15%年減幅推算,全年約89,967人,正好跌破9萬"
  - p96 Forecast Taiwan 2026 annual births, pessimistic scenario (Mar-Dec -20% YoY) = **85,571** birth (2026-01-01..2026-12-31) [keep: ] quote: "在悲觀情境中,以20%年減幅推估,全年約85,571人,幾近再度腰斬一成"
  - p97 Taiwan total fertility rate, 2024 = **0.87** birth/(woman*year) (2024-01-01..2024-12-31) [keep: ] quote: "台灣2024年的總生育率約為0.87,遠低於替代水準"
  - p98 Replacement-level total fertility rate = **2.1** birth/(woman*year) (not stated (page dated 2026-03-15)) [keep: ] quote: "即便總生育率(TFR)立刻回升至替代水準(2.1)"
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gb.crntt.com/doc/1601/5/3/6/160153686.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rti.org.tw/news?uid=3&pid=196249` -> **snapshot** (snapshot 20260414160447); points raw/verified 18/15
  - p99 Taiwan total population at end of February 2026 (MOI household registration) = **23,280,273** person (2026-02-28..2026-02-28) [keep: ] quote: "截至2026年2月底,台灣人口數為2328萬273人"
  - p100 Taiwan live births registered in February 2026 (monthly births) = **6,523** birth (2026-02-01..2026-02-28) [keep: ] quote: "2月新生兒共6523人"
  - p101 Change in Taiwan monthly births, February 2026 vs January 2026 (persons) = **2,200** birth (2026-02-01..2026-02-28) [keep: ] quote: "較1月少了2200人"
  - p102 Change in Taiwan monthly births, February 2026 vs January 2026 (percent) = **25.2** % (2026-02-01..2026-02-28) [keep: ] quote: "大減25.2%"
  - p103 Taiwan crude birth rate, February 2026, annualised = **3.65** birth/(1000 person*year) (2026-02-01..2026-02-28) [keep: ] quote: "折合年粗出生率為千分之3.65"
  - p104 Change in Taiwan monthly births, February 2026 vs February 2025 (persons) = **3,884** birth (2026-02-01..2026-02-28) [keep: ] quote: "也較去年同期減少3884人"
  - p105 Taiwan deaths registered in February 2026 = **14,881** death (2026-02-01..2026-02-28) [keep: ] quote: "2月死亡1萬4881人"
  - p106 Taiwan natural increase (births minus deaths), February 2026 = **8,358** person (2026-02-01..2026-02-28) [keep: ] quote: "台灣2月人口自然增加為負8358人"
  - p107 Taiwan total population change, February 2026 vs January 2026 = **8,772** person (2026-02-01..2026-02-28) [keep: ] quote: "2月總人口較1月減少8772人"
  - p108 Taiwan population aged 0-14 at end of February 2026 = **2,667,349** person (2026-02-28..2026-02-28) [keep: ] quote: "台灣0至14歲人口數為266萬7349人"
  - p109 Taiwan population aged 15-64 at end of February 2026 = **15,905,248** person (2026-02-28..2026-02-28) [keep: ] quote: "15至64歲人口數為1590萬5248人"
  - p110 Taiwan population aged 65+ at end of February 2026 = **4,707,676** person (2026-02-28..2026-02-28) [keep: ] quote: "65歲以上人口數為470萬7676人"
  - p111 Taiwan marriages in February 2026 (couples) = **6,733** couple (2026-02-01..2026-02-28) [keep: ] quote: "2月結婚共6733對"
  - p112 Taiwan divorces/terminated marriages in February 2026 (couples) = **2,995** couple (2026-02-01..2026-02-28) [keep: ] quote: "離婚/終止結婚共2995對"
  - p113 Taiwan net migration (in minus out), February 2026 = **414** person (2026-02-01..2026-02-28) [keep: ] quote: "淨遷入人口數為負414人"
- `https://www.taiwannews.com.tw/news/6262219` -> **snapshot** (snapshot 20260830205514); points raw/verified 28/3
  - p114 Consecutive months of Taiwan population decline = **23** month (not stated (page dated 2025-09-19)) [keep: ] quote: "Taiwan's population has shrunk for the 23rd consecutive month, with November births hitting a new low"
  - p115 Consecutive years of negative newborn growth in Taiwan = **9** as written "nine", value check pending year (not stated (page dated 2025-09-19)) [keep: ] quote: "Taiwan has experienced nine consecutive years of negative newborn growth."
  - p116 WHO threshold share of population aged 65+ for super-aged society = **20** % (not stated (page dated 2025-09-19)) [keep: ] quote: "a population with 7% aged 65+ is considered an "aging society," 14% is an "aged society," and 20% is a super-aged society."
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- dropped by code checks: 30 (value_as_written not in quote as a whole number: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 27; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] National vital statistics / DGBAS

Hypothesis: Births registered in a month track births occurring in that month plus a lagged registration component; DGBAS/內政部 vital-statistics births by occurrence month can cross-check and adjust the registration-timing lag. Target ≈ births occurring in Sep 2026 × registration-completeness factor for that month.

Queries issued by the searcher: 內政部 戶政司 出生 登記 月別 統計 2025; Taiwan monthly live births 2025 statistics department of household registration; 2026年 7月 出生數 內政部 戶口統計 新生兒; 內政部 出生 按發生日期 統計 出生數 發生數 登記數 差距; 內政部 戶政司 出生 登記數 月別 統計; Taiwan monthly live births 2026 household registration statistics; 2026年7月 出生數 內政部 戶口統計 新生兒; 內政部 統計 出生數 按發生日期 月別 發生數 登記數 差異; 內政部 出生 發生數 登記數 月別 統計; Taiwan monthly live births 2024 2025 statistics by month; 2026年 出生數 內政部 戶口統計 6月 新生兒; 台灣 2026年 1月 2月 出生人數 創新低 內政部; 內政部 2026年7月 戶口統計 出生數 7月 新生兒; 出生數 按發生日期 統計 與 出生登記數 差異 內政部 113年

- `https://www.rti.org.tw/news?uid=3&pid=225273` -> **snapshot** (snapshot 20260815163625); points raw/verified 26/25
  - p117 Taiwan population at end of July 2026 (MOI household registration) = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年(2026年)7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p118 Live births registered in Taiwan in July 2026 = **7,906** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p119 Change in monthly live births, July 2026 vs June 2026 = **582** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p120 Cumulative live births registered in Taiwan, January-July 2026 = **54,250** birth (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p121 Year-on-year decline in cumulative live births, Jan-Jul 2026 vs Jan-Jul 2025 = **10,064** birth (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人"
  - p122 Year-on-year change in Taiwan population, July 2026 vs July 2025 = **102,934** person (2026-07-31..2026-07-31) [keep: ] quote: "較去年同期減少10萬2934人,平均每天減少282.01人"
  - p123 Average daily population decrease, July 2026 = **282** person/day (2026-07-01..2026-07-31) [keep: ] quote: "平均每天減少282.01人,相比今年6月則減少8563人"
  - p124 Change in Taiwan population, July 2026 vs June 2026 = **8,563** person (2026-07-01..2026-07-31) [keep: ] quote: "相比今年6月則減少8563人"
  - p125 Birth interval implied by July 2026 births (one birth every N minutes) = **5.6** minute/birth (2026-07-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒"
  - p126 Annualised crude birth rate, July 2026 = **4.01** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為千分之4.01,較去年同期減少1033人"
  - p127 Year-on-year change in July live births, 2026 vs 2025 = **1,033** birth (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人"
  - p128 Deaths registered in Taiwan in July 2026 = **17,119** death (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人,平均約每2.6分鐘1人死亡"
  - p129 Annualised crude death rate, July 2026 = **8.67** death per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為千分之8.67,較去年同期增加273人"
  - p130 Cumulative deaths registered in Taiwan, January-July 2026 = **115,628** death (2026-01-01..2026-07-31) [keep: ] quote: "死亡數共11萬5628人,新生兒共5萬4250人,死亡人數超過出生數的2倍"
  - p131 Natural increase (births minus deaths), Taiwan July 2026 = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p132 In-migrants registered in Taiwan in July 2026 = **74,647** person (2026-07-01..2026-07-31) [keep: ] quote: "7月遷入人口數7萬4647人,較6月增加9546人"
  - p133 Out-migrants registered in Taiwan in July 2026 = **73,997** person (2026-07-01..2026-07-31) [keep: ] quote: "遷出共7萬3997人,較6月增加8836人"
  - p134 Net migration (social increase), Taiwan July 2026 = **650** person (2026-07-01..2026-07-31) [keep: ] quote: "淨遷入人口數為650人"
  - p135 Population aged 0-14 at end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p136 Share of population aged 0-14, end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p137 Population aged 15-64 at end of July 2026 = **15,835,491** person (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口數1583萬5491人,占68.15%"
  - p138 Population aged 65+ at end of July 2026 = **4,773,519** person (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p139 Share of population aged 65+, end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p140 Highest county/city crude birth rate, Taitung County, July 2026 = **6.06** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "粗出生率最高為台東縣千分之6.06,其次為雲林縣千分之5.29、連江縣千分之5.18"
  - p141 Lowest county/city crude birth rate, Keelung City, July 2026 = **2.1** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "最低為基隆市千分之2.10,其次為台南市千分之3.14、嘉義縣千分之3.36"
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 29/29
  - p142 Taiwan total population, end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人"
  - p143 Live births registered in Taiwan, July 2026 (single month) = **7,906** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人"
  - p144 Live births registered in Taiwan, May 2026 (single month) = **6,832** birth (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p145 Live births registered in Taiwan, June 2026 (single month) = **7,324** birth (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p146 Year-on-year change in July 2026 live births, Taiwan (absolute) = **1,033** birth (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p147 Year-on-year change in July 2026 live births, Taiwan (percent) = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p148 Crude birth rate, July 2026, Taiwan (annualised) = **4.01** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為4.01‰"
  - p149 Deaths registered in Taiwan, July 2026 (single month) = **17,119** death (2026-07-01..2026-07-31) [keep: ] quote: "7月死亡人數則為1萬7119人"
  - p150 Crude death rate, July 2026, Taiwan (annualised) = **8.67** death per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰"
  - p151 Year-on-year change in July 2026 deaths, Taiwan (percent) = **1.62** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p152 Month-on-month change in July 2026 deaths, Taiwan (percent) = **4.77** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p153 Year-on-year change in Taiwan total population, July 2026 (percent) = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%"
  - p154 Month-on-month change in Taiwan total population, July 2026 (percent) = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "與6月相比則減少0.04%"
  - p155 Consecutive months of population decline, Taiwan, through July 2026 = **31** month (2024-01-01..2026-07-31) [keep: ] quote: "是連續31個月出現人口負成長"
  - p156 Share of population aged 65+, Taiwan, end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口占20.54%"
  - p157 Share of population aged 15-64, Taiwan, end of July 2026 = **68.15** % (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%"
  - p158 Share of population aged 0-14, Taiwan, end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "0至14歲占11.30%"
  - p159 Marriages registered in Taiwan, July 2026 = **7,150** couple (2026-07-01..2026-07-31) [keep: ] quote: "7月全台共有7150對"
  - p160 Share of July 2026 marriages that were same-sex, Taiwan = **3.5** % (2026-07-01..2026-07-31) [keep: ] quote: "同婚占3.5%"
  - p161 Divorces registered in Taiwan, July 2026 = **4,450** couple (2026-07-01..2026-07-31) [keep: ] quote: "離婚對數為4450對"
  - p162 Share of July 2026 divorces that were same-sex, Taiwan = **1.7** % (2026-07-01..2026-07-31) [keep: ] quote: "同婚占1.7%"
  - p163 Average interval between deaths, Taiwan, July 2026 = **2.6** minute per death (2026-07-01..2026-07-31) [keep: ] quote: "平均約每2.6分鐘有一人死亡"
  - p164 Highest county/city crude birth rate, Taitung County, July 2026 (annualised) = **6.06** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "粗出生率最高為台東縣6.06‰"
  - p165 Crude birth rate, Yunlin County, July 2026 (annualised) = **5.29** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "其次分別為雲林縣5.29‰、連江縣5.18‰"
  - p166 Crude birth rate, Lienchiang County, July 2026 (annualised) = **5.18** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "其次分別為雲林縣5.29‰、連江縣5.18‰"
  - p167 Lowest county/city crude birth rate, Keelung City, July 2026 (annualised) = **2.1** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p168 Crude birth rate, Tainan City, July 2026 (annualised) = **3.14** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p169 Crude birth rate, Chiayi County, July 2026 (annualised) = **3.36** birth per 1,000 person (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p170 Number of counties/cities below 20% aged 65+, Taiwan, end of July 2026 = **5** county/city (2026-07-31..2026-07-31) [keep: ] quote: "全台僅有5縣市尚未達標"
- `https://www.cna.com.tw/news/aipl/202608100072.aspx` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 29/29
  - p171 Registered live births in Taiwan (ROC), full year 2025 (household registration,  = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year, resulting in a crude birth rate of 4.62 per 1,000 population."
  - p172 Registered live births in Taiwan (ROC), full year 2024 (household registration) = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p173 Year-on-year percent change in registered births, 2025 vs 2024 = **-20.05** % (2025-01-01..2025-12-31) [keep: ] quote: "[(2)-(1)]/(1)×100 -20.05 -0.91 -- -- -- --"
  - p174 Registered births in Taiwan (ROC), September 2025 (month of registration) = **8,603** birth (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p175 Registered births in Taiwan (ROC), October 2025 (month of registration) = **9,458** birth (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p176 Registered births in Taiwan (ROC), November 2025 (month of registration) = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p177 Registered births in Taiwan (ROC), December 2025 (month of registration) = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p178 Registered births in Taiwan (ROC), January 2025 = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p179 Registered births in Taiwan (ROC), February 2025 = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p180 Registered births in Taiwan (ROC), March 2025 = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p181 Registered births in Taiwan (ROC), April 2025 = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p182 Registered births in Taiwan (ROC), May 2025 = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p183 Registered births in Taiwan (ROC), June 2025 = **8,968** birth (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p184 Registered births in Taiwan (ROC), July 2025 = **8,939** birth (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p185 Registered births in Taiwan (ROC), August 2025 = **8,464** birth (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p186 Crude birth rate, Taiwan (ROC), full year 2025 (births per 1,000 population, ann = **4.62** birth/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year, resulting in a crude birth rate of 4.62 per 1,000 population."
  - p187 Crude birth rate, Taiwan (ROC), full year 2024 (births per 1,000 population, ann = **5.76** birth/(1000 person) (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p188 Unadjusted crude birth rate, Taiwan (ROC), September 2025 (annual basis) = **4.49** birth/(1000 person) (2025-09-01..2025-09-30) [keep: ] quote: "4.78 5.80 4.73 4.52 4.25 4.67 4.51 4.27 4.49 4.78"
  - p189 Unadjusted crude birth rate, Taiwan (ROC), October 2025 (annual basis) = **4.78** birth/(1000 person) (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p190 Unadjusted crude birth rate, Taiwan (ROC), November 2025 (annual basis) = **4.15** birth/(1000 person) (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p191 Unadjusted crude birth rate, Taiwan (ROC), December 2025 (annual basis) = **4.56** birth/(1000 person) (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p192 Seasonally adjusted crude birth rate, Taiwan (ROC), September 2025 (annual basis = **4.42** birth/(1000 person) (2025-09-01..2025-09-30) [keep: ] quote: "4.85 6.28 4.50 4.97 4.40 4.91 4.71 4.42 4.55 4.36"
  - p193 Seasonally adjusted crude birth rate, Taiwan (ROC), October 2025 (annual basis) = **4.36** birth/(1000 person) (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p194 Seasonally adjusted crude birth rate, Taiwan (ROC), November 2025 (annual basis) = **3.89** birth/(1000 person) (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p195 Seasonally adjusted crude birth rate, Taiwan (ROC), December 2025 (annual basis) = **4.01** birth/(1000 person) (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p196 Cumulative crude birth rate, Taiwan (ROC), January-September 2025 (annual basis) = **4.66** birth/(1000 person) (2025-01-01..2025-09-30) [keep: ] quote: "4.78 5.26 5.08 4.94 4.80 4.78 4.74 4.68 4.66 4.67"
  - p197 Cumulative crude birth rate, Taiwan (ROC), January-December 2025 (annual basis) = **4.67** birth/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "4.78 5.26 5.08 4.94 4.80 4.78 4.74 4.68 4.66 4.67"
  - p198 Total population of Taiwan (ROC) at end of September 2025 = **23,317,031** person (2025-09-30..2025-09-30) [keep: ] quote: "23,346,741 23,337,936 23,328,343 23,317,031 23,310,853 23,306,085 23,299,132"
  - p199 Total population of Taiwan (ROC) at end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "at the end of December 2025, there were 9,851,532 households with a total population of 23,299,132"
- `https://www.golden-brother.com/index.php?action=news-detail&cid=2&id=4659&lang=TW` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/info-liferay/app/channel/newsEnglishDetail/26245250` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taipeitimes.com/News/taiwan/archives/2025/06/11/2003838416` -> **snapshot** (snapshot 20250817163931); points raw/verified 23/23
  - p200 Newborn babies registered in Taiwan in May (historic single-month low) = **8,433** births (2025-05-01..2025-05-31) [keep: ] quote: "The number of newborn babies was 8,433 last month, which was also a historic single-month low, ministry data showed."
  - p201 Cumulative births registered in Taiwan January to May = **46,407** births (2025-01-01..2025-05-31) [keep: ] quote: "From January to last month, 46,407 babies were born: 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April and 8,433 last month, the data showed."
  - p202 Births registered in Taiwan in January = **9,495** births (2025-01-01..2025-01-31) [keep: ] quote: "From January to last month, 46,407 babies were born: 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April and 8,433 last month, the data showed."
  - p203 Births registered in Taiwan in February = **10,407** births (2025-02-01..2025-02-28) [keep: ] quote: "From January to last month, 46,407 babies were born: 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April and 8,433 last month, the data showed."
  - p204 Births registered in Taiwan in March = **9,388** births (2025-03-01..2025-03-31) [keep: ] quote: "From January to last month, 46,407 babies were born: 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April and 8,433 last month, the data showed."
  - p205 Births registered in Taiwan in April = **8,684** births (2025-04-01..2025-04-30) [keep: ] quote: "From January to last month, 46,407 babies were born: 9,495 in January, 10,407 in February, 9,388 in March, 8,684 in April and 8,433 last month, the data showed."
  - p206 Change in monthly births, May 2025 vs May 2024 = **2,735** births (2025-05-01..2025-05-31) [keep: ] quote: "The number of births decreased by 2,735 compared with May last year and dropped by 251 compared with April."
  - p207 Change in monthly births, May 2025 vs April 2025 = **251** births (2025-05-01..2025-05-31) [keep: ] quote: "The number of births decreased by 2,735 compared with May last year and dropped by 251 compared with April."
  - p208 Average interval between births, January to May 2025 = **5.3** minutes per birth (2025-01-01..2025-05-31) [keep: ] quote: "From January to last month, one baby was born approximately every 5.3 minutes"
  - p209 Crude birth rate, annualised, May 2025 = **4.25** births per 1,000 people per year (2025-05-01..2025-05-31) [keep: ] quote: "One baby was born approximately every 5.3 minutes, corresponding to a crude birthrate of 4.25 per 1,000 annually."
  - p210 Taiwan population at end of May 2025 = **23,355,470** people (2025-05-31..2025-05-31) [keep: ] quote: "The nation's population declined last month to 23,355,470 from 23,365,274 in April"
  - p211 Taiwan population at end of April 2025 = **23,365,274** people (2025-04-30..2025-04-30) [keep: ] quote: "The nation's population declined last month to 23,355,470 from 23,365,274 in April"
  - p212 Year-on-year population change, May 2025 = **58,138** people (2025-05-01..2025-05-31) [keep: ] quote: "The population was down 58,138 compared with the same month last year, with an average daily decrease of 159.28 people."
  - p213 Average daily population decrease, May 2025 = **159** people per day (2025-05-01..2025-05-31) [keep: ] quote: "The population was down 58,138 compared with the same month last year, with an average daily decrease of 159.28 people."
  - p214 Deaths registered in Taiwan in May 2025 = **15,382** deaths (2025-05-01..2025-05-31) [keep: ] quote: "The government recorded 15,382 deaths last month, with one person dying every 2.9 minutes on average"
  - p215 Crude death rate, annualised, May 2025 = **7.75** deaths per 1,000 people per year (2025-05-01..2025-05-31) [keep: ] quote: "corresponding to a crude death rate of 7.75 per 1,000 annually"
  - p216 Couples married in Taiwan in May 2025 = **12,791** couples (2025-05-01..2025-05-31) [keep: ] quote: "A total of 12,791 couples married last month - 12,359 heterosexual couples and 432 same-sex couples."
  - p217 Heterosexual couples married in Taiwan in May 2025 = **12,359** couples (2025-05-01..2025-05-31) [keep: ] quote: "A total of 12,791 couples married last month - 12,359 heterosexual couples and 432 same-sex couples."
  - p218 Same-sex couples married in Taiwan in May 2025 = **432** couples (2025-05-01..2025-05-31) [keep: ] quote: "A total of 12,791 couples married last month - 12,359 heterosexual couples and 432 same-sex couples."
  - p219 Crude marriage rate, May 2025 = **6.45** marriages per 1,000 people (2025-05-01..2025-05-31) [keep: ] quote: "The crude marriage rate was approximately 6.45 per 1,000."
  - p220 Couples divorced in Taiwan in May 2025 = **4,532** couples (2025-05-01..2025-05-31) [keep: ] quote: "Meanwhile, 4,532 couples filed for divorce: 4,456 heterosexual couples and 76 same-sex couples."
  - p221 Crude divorce rate, May 2025 = **2.28** divorces per 1,000 people (2025-05-01..2025-05-31) [keep: ] quote: "The crude divorce rate was 2.28 per 1,000."
  - p222 Consecutive months of population decline through May 2025 = **17** months (2025-05-01..2025-05-31) [keep: ] quote: "the 17th consecutive month the population has shrunk"
- `https://www.cna.com.tw/news/aipl/202507100198.aspx` -> **snapshot** (snapshot 20250727051205); points raw/verified 29/28
  - p223 Taiwan total population at end of June 2025 = **23,346,741** person (2025-06-30..2025-06-30) [keep: ] quote: "截至今年6月底人口數為2334萬6741人"
  - p224 Taiwan population decrease from May 2025 to June 2025 = **8,729** person (2025-06-01..2025-06-30) [keep: ] quote: "較5月減少8729人,人口已連續18個月負成長"
  - p225 Consecutive months of Taiwan population decline through June 2025 = **18** month (2024-01-01..2025-06-30) [keep: ] quote: "人口已連續18個月負成長"
  - p226 Live births registered in Taiwan in June 2025 = **8,968** birth (2025-06-01..2025-06-30) [keep: ] quote: "6月出生數8968人,終止連3個月跌勢"
  - p227 Live births registered in Taiwan in June 2025 (minutes per birth) = **4.8** minute/birth (2025-06-01..2025-06-30) [keep: ] quote: "今年6月出生數為8968人,約每4.8分鐘出生一個嬰兒"
  - p228 Taiwan crude birth rate in June 2025 (annualised) = **4.67** birth/(1000 person*year) (2025-06-01..2025-06-30) [keep: ] quote: "年粗出生率為千分之4.67,較去年同期減少1472人"
  - p229 Change in June live births vs June 2024 (Taiwan) = **1,472** birth (2025-06-01..2025-06-30) [keep: ] quote: "較去年同期減少1472人,較5月增加535人"
  - p230 Change in June live births vs May 2025 (Taiwan) = **535** birth (2025-06-01..2025-06-30) [keep: ] quote: "較5月增加535人"
  - p231 Live births registered in Taiwan in January 2025 = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "1月為9495人、2月1萬407人、3月共9388人"
  - p232 Live births registered in Taiwan in February 2025 = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "2月1萬407人"
  - p233 Live births registered in Taiwan in March 2025 = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "3月共9388人"
  - p234 Live births registered in Taiwan in April 2025 (record low) = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "4月8684人創史上最低紀錄"
  - p235 Live births registered in Taiwan in May 2025 (record low) = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "5月8433人再探底"
  - p236 Live births registered in Taiwan in first half of 2025 = **55,375** birth (2025-01-01..2025-06-30) [keep: ] quote: "今年上半年新生兒共5萬5375人"
  - p237 Change in first-half live births 2025 vs 2024 (Taiwan) = **8,499** birth (2025-01-01..2025-06-30) [keep: ] quote: "今年上半年新生兒較去年同期減少8499人"
  - p238 Deaths registered in Taiwan in June 2025 = **16,554** death (2025-06-01..2025-06-30) [keep: ] quote: "今年6月死亡數為1萬6554人"
  - p239 Taiwan crude death rate in June 2025 (annualised) = **8.63** death/(1000 person*year) (2025-06-01..2025-06-30) [keep: ] quote: "折合年粗死亡率為千分之8.63"
  - p240 Taiwan natural population increase in June 2025 (births minus deaths) = **7,586** person (2025-06-01..2025-06-30) [keep: ] quote: "台灣6月人口自然增加為負7586人"
  - p241 Taiwan net migration in June 2025 = **1,143** person (2025-06-01..2025-06-30) [keep: ] quote: "淨遷入人口數為負1143人"
  - p242 Taiwan in-migrants in June 2025 = **71,834** person (2025-06-01..2025-06-30) [keep: ] quote: "6月遷入人口數為7萬1834人"
  - p243 Taiwan out-migrants in June 2025 = **72,977** person (2025-06-01..2025-06-30) [keep: ] quote: "遷出人口數為7萬2977人"
  - p244 Taiwan population aged 0-14 at end of June 2025 = **2,716,281** person (2025-06-30..2025-06-30) [keep: ] quote: "0至14歲人口數為271萬6281人,占總人口比率11.63%"
  - p245 Share of Taiwan population aged 0-14 at end of June 2025 = **11.63** % (2025-06-30..2025-06-30) [keep: ] quote: "占總人口比率11.63%"
  - p246 Taiwan population aged 15-64 at end of June 2025 = **16,057,007** person (2025-06-30..2025-06-30) [keep: ] quote: "15至64歲人口數為1605萬7007人,占68.78%"
  - p247 Taiwan population aged 65+ at end of June 2025 = **4,573,453** person (2025-06-30..2025-06-30) [keep: ] quote: "65歲以上人口數為457萬3453人,占19.59%"
  - p248 Share of Taiwan population aged 65+ at end of June 2025 = **19.59** % (2025-06-30..2025-06-30) [keep: ] quote: "占19.59%,距離邁入超高齡社會、65歲以上老年人口數突破20%僅一步之遙"
  - p249 Taiwan year-on-year population change at end of June 2025 = **66,158** person (2025-06-30..2025-06-30) [keep: ] quote: "比去年同期減少6萬6158人,平均每天減少181.25人"
  - p250 Average daily Taiwan population decline (June 2025 vs June 2024) = **181** person/day (2025-06-30..2025-06-30) [keep: ] quote: "平均每天減少181.25人"
- `https://www.moi.gov.tw/english//News_Content.aspx?n=7627&s=328628` -> **snapshot** (snapshot 20250627180351); points raw/verified 30/30
  - p251 Live births registered in Taiwan in May 2025 (monthly births registered) = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "There were 8,433 babies born in May 2025 which decreased 24.49% compared with the same month last year."
  - p252 Year-on-year change in May 2025 registered births vs May 2024 = **24.49** % (2025-05-01..2025-05-31) [keep: ] quote: "which decreased 24.49% compared with the same month last year"
  - p253 Average interval between births implied by May 2025 registered births = **5.3** minute/birth (2025-05-01..2025-05-31) [keep: ] quote: "The average showed that a baby was born about every 5.3 minutes."
  - p254 Annual crude birth rate, Taiwan, May 2025 report = **4.25** birth/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "The annual crude birth rate was 4.25‰."
  - p255 Total population of Taiwan at end of May 2025 = **23,355,470** person (2025-05-31..2025-05-31) [keep: ] quote: "By the end of May 2025, the total population was 23,355,470 with a decrease of 58,138 compared with the same month last year."
  - p256 Year-on-year change in total population, May 2025 = **58,138** person (2025-05-01..2025-05-31) [keep: ] quote: "the total population was 23,355,470 with a decrease of 58,138 compared with the same month last year"
  - p257 Population growth rate, Taiwan, May 2025 year-on-year = **-0.25** % (2025-05-01..2025-05-31) [keep: ] quote: "The population growth rate was -0.25% which meant that the average daily decreased was 159.28."
  - p258 Average daily population decrease, Taiwan, May 2025 = **159** person/day (2025-05-01..2025-05-31) [keep: ] quote: "the average daily decreased was 159.28"
  - p259 Households registered in Taiwan at end of May 2025 = **9,800,648** household (2025-05-31..2025-05-31) [keep: ] quote: "According to the household registration data, there were 9,800,648 households at the end of May 2025."
  - p260 Year-on-year increase in households, May 2025 = **504,868** household (2025-05-01..2025-05-31) [keep: ] quote: "there increased 504,868 households with an increase rate of 5.43%"
  - p261 Household increase rate, May 2025 year-on-year = **5.43** % (2025-05-01..2025-05-31) [keep: ] quote: "with an increase rate of 5.43%"
  - p262 Male population of Taiwan at end of May 2025 = **11,498,215** person (2025-05-31..2025-05-31) [keep: ] quote: "By the end of May 2025, the male population was 11,498,215 and female population was 11,857,255."
  - p263 Female population of Taiwan at end of May 2025 = **11,857,255** person (2025-05-31..2025-05-31) [keep: ] quote: "the male population was 11,498,215 and female population was 11,857,255"
  - p264 Sex ratio (male per 100 female), Taiwan, end of May 2025 = **96.97** male/(100 female) (2025-05-31..2025-05-31) [keep: ] quote: "The sex ratio was 96.97 compared with male to female."
  - p265 Deaths registered in Taiwan in May 2025 = **15,382** death (2025-05-01..2025-05-31) [keep: ] quote: "There were 15,382 deaths in May 2025 which decreased 6.30% compared with the same month last year."
  - p266 Year-on-year change in May 2025 deaths = **6.3** % (2025-05-01..2025-05-31) [keep: ] quote: "which decreased 6.30% compared with the same month last year"
  - p267 Annual crude death rate, Taiwan, May 2025 report = **7.75** death/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "The annual crude death rate was 7.75‰."
  - p268 Marriages registered in Taiwan in May 2025 = **12,791** couple (2025-05-01..2025-05-31) [keep: ] quote: "The couples of marriage were 12,791 in May 2025."
  - p269 Different-gender marriages registered in Taiwan in May 2025 = **12,359** couple (2025-05-01..2025-05-31) [keep: ] quote: "Including 12,359 couples of different gender and 432 couples of the same gender."
  - p270 Same-gender marriages registered in Taiwan in May 2025 = **432** couple (2025-05-01..2025-05-31) [keep: ] quote: "Including 12,359 couples of different gender and 432 couples of the same gender."
  - p271 Annual crude marriage rate, Taiwan, May 2025 report = **6.45** couple/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "The annual crude marriage rate was 6.45‰."
  - p272 Divorces registered in Taiwan in May 2025 = **4,532** couple (2025-05-01..2025-05-31) [keep: ] quote: "The couples of divorce were 4,532 in May 2025."
  - p273 Annual crude divorce rate, Taiwan, May 2025 report = **2.28** couple/(1000 person) (2025-01-01..2025-12-31) [keep: ] quote: "The annual crude divorce rate was 2.28‰."
  - p274 In-migrants to Taiwan in May 2025 = **121,014** person (2025-05-01..2025-05-31) [keep: ] quote: "There were 121,014 in-migrants in May 2025 which increased 29.23% compared with the same month last year."
  - p275 Out-migrants from Taiwan in May 2025 = **123,869** person (2025-05-01..2025-05-31) [keep: ] quote: "there were 123,869 out-migrants which increased 37.81% compared with the same month last year"
  - p276 Indigenous people registered in Taiwan at end of May 2025 = **617,824** person (2025-05-31..2025-05-31) [keep: ] quote: "At the end of May 2025, the indigenous people was 617,824 with an increase of 17,521 compared with the same month last year (2.65% of the total population)."
  - p277 Population aged 0 to 14 in Taiwan at end of May 2025 = **2,719,872** person (2025-05-31..2025-05-31) [keep: ] quote: "At the end of May 2025, the population aged 0 to 14 was 2,719,872 (11.65% of the total population)."
  - p278 Share of population aged 0 to 14 in Taiwan, end of May 2025 = **11.65** % (2025-05-31..2025-05-31) [keep: ] quote: "the population aged 0 to 14 was 2,719,872 (11.65% of the total population)"
  - p279 Population aged 15 to 64 in Taiwan at end of May 2025 = **16,071,285** person (2025-05-31..2025-05-31) [keep: ] quote: "The population aged 15 to 64 was 16,071,285 (68.81%)."
  - p280 Population aged over 65 in Taiwan at end of May 2025 = **4,564,313** person (2025-05-31..2025-05-31) [keep: ] quote: "The population aged over 65 was 4,564,313 (19.54%)."
- `https://gb.crntt.com/crn-webapp/touch/detail.jsp?coluid=7&kindid=0&docid=160153686` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.setn.com/news/1763612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://udn.com/news/story/7266/8729989` -> **snapshot** (snapshot 20250720183520); points raw/verified 29/0
- dropped by code checks: 31 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 29)

### d3 [base_rates] Demographic trend and seasonality

Hypothesis: Monthly births = annualised recent birth rate × population × (1/12) × seasonal factor. A declining annual trend (Taiwan's TFR ~0.8–0.9) plus September seasonal index gives a level estimate; useful to constrain the plausible range and detect trend breaks.

Queries issued by the searcher: 台灣 2025 出生數 總計 內政部; Taiwan births 2025 annual total household registration statistics; 2026年 7月 出生數 內政部 戶口統計 新生兒; Taiwan births July 2026 monthly household registration lowest; 台灣 2025 出生數 總計 內政部; Taiwan monthly births 2024 2025 statistics 內政部 戶政司 出生 按月; 2026年6月 新生兒 出生數 內政部 人口統計; 2026年7月 出生數 內政部 戶口統計 新生兒; 台灣 2025 出生數 總計 內政部 戶政司; Taiwan births 2025 annual total monthly statistics declining; 2026年7月 出生數 內政部 人口統計 新生兒; 內政部 戶政司 出生數 按月 統計 113年 各月出生人數 表

- `https://www.cna.com.tw/news/aipl/202601090067.aspx` -> **snapshot** (snapshot 20260207175022); points raw/verified 31/31
  - p281 Taiwan total population at end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "台灣2025年總人口2329萬9132人,持續負成長"
  - p282 Taiwan population aged 65 and over at end of December 2025 = **4,673,155** person (2025-12-31..2025-12-31) [keep: ] quote: "65歲以上人口達467萬3155人,占整體20.06%"
  - p283 Share of population aged 65 and over at end of December 2025 = **20.06** % (2025-12-31..2025-12-31) [keep: ] quote: "65歲以上人口達467萬3155人,占整體20.06%"
  - p284 Live births registered in Taiwan, full year 2025 = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "2025年新生兒數為10萬7812人,連10年下降,再創新低"
  - p285 Live births registered in Taiwan, December 2025 (single month) = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月單月新生兒出生數為9027人,比11月增加1081人"
  - p286 Month-on-month change in December 2025 births vs November 2025 = **1,081** birth (2025-12-01..2025-12-31) [keep: ] quote: "去年12月單月新生兒出生數為9027人,比11月增加1081人"
  - p287 Year-on-year change in December 2025 births vs December 2024 = **3,469** birth (2025-12-01..2025-12-31) [keep: ] quote: "但相較前年同期減少3469人"
  - p288 Live births registered in Taiwan, full year 2024 = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2023年13萬5571人、2024年13萬4856人"
  - p289 Live births registered in Taiwan, full year 2023 = **135,571** birth (2023-01-01..2023-12-31) [keep: ] quote: "2022年13萬8986人、2023年13萬5571人"
  - p290 Live births registered in Taiwan, full year 2022 = **138,986** birth (2022-01-01..2022-12-31) [keep: ] quote: "2021年15萬3820人、2022年13萬8986人"
  - p291 Live births registered in Taiwan, full year 2021 = **153,820** birth (2021-01-01..2021-12-31) [keep: ] quote: "2020年16萬5249人、2021年15萬3820人"
  - p292 Live births registered in Taiwan, full year 2020 = **165,249** birth (2020-01-01..2020-12-31) [keep: ] quote: "2019年17萬7767人、2020年16萬5249人"
  - p293 Live births registered in Taiwan, full year 2019 = **177,767** birth (2019-01-01..2019-12-31) [keep: ] quote: "2018年18萬1601人、2019年17萬7767人"
  - p294 Live births registered in Taiwan, full year 2018 = **181,601** birth (2018-01-01..2018-12-31) [keep: ] quote: "2017年19萬3844人、2018年18萬1601人"
  - p295 Live births registered in Taiwan, full year 2017 = **193,844** birth (2017-01-01..2017-12-31) [keep: ] quote: "2016年20萬8440人、2017年19萬3844人"
  - p296 Live births registered in Taiwan, full year 2016 = **208,440** birth (2016-01-01..2016-12-31) [keep: ] quote: "台灣新生兒數自2016年起逐年下降,2016年20萬8440人"
  - p297 Deaths in Taiwan, full year 2025 = **200,268** death (2025-01-01..2025-12-31) [keep: ] quote: "去年整體死亡人數為20萬268人,折合年粗死亡率為千分之8.58"
  - p298 Crude death rate in Taiwan, 2025 (per 1,000 population) = **8.58** death per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "折合年粗死亡率為千分之8.58,相比2024年減少了1839人"
  - p299 Year-on-year change in deaths, 2025 vs 2024 = **1,839** death (2025-01-01..2025-12-31) [keep: ] quote: "折合年粗死亡率為千分之8.58,相比2024年減少了1839人"
  - p300 Population aged 0-14 at end of December 2025 = **2,681,890** person (2025-12-31..2025-12-31) [keep: ] quote: "0歲至14歲人口數為268萬1890人,占總人口比率11.51%"
  - p301 Share of population aged 0-14 at end of December 2025 = **11.51** % (2025-12-31..2025-12-31) [keep: ] quote: "0歲至14歲人口數為268萬1890人,占總人口比率11.51%"
  - p302 Population aged 15-64 at end of December 2025 = **15,944,087** person (2025-12-31..2025-12-31) [keep: ] quote: "15歲至64歲人口數為1594萬4087人,占68.43%"
  - p303 Share of population aged 15-64 at end of December 2025 = **68.43** % (2025-12-31..2025-12-31) [keep: ] quote: "15歲至64歲人口數為1594萬4087人,占68.43%"
  - p304 Population aged 20 and over at end of December 2025 = **19,644,140** person (2025-12-31..2025-12-31) [keep: ] quote: "若看整體20歲以上人口數為1964萬4140人,占84.31%"
  - p305 Share of population aged 20 and over at end of December 2025 = **84.31** % (2025-12-31..2025-12-31) [keep: ] quote: "20歲以上人口數為1964萬4140人,占84.31%"
  - p306 Year-on-year change in total population, end-2025 vs end-2024 = **101,088** person (2025-12-31..2025-12-31) [keep: ] quote: "相比2024年同期減少了10萬1088人,人口負成長趨勢持續2年"
  - p307 Marriages in Taiwan, full year 2025 (couples) = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "去年結婚對數10萬4376對,折合年粗結婚率為千分之4.47"
  - p308 Crude marriage rate in Taiwan, 2025 (per 1,000 population) = **4.47** couple per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "折合年粗結婚率為千分之4.47,相比2024年的12萬3061對"
  - p309 Marriages in Taiwan, full year 2024 (couples) = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "相比2024年的12萬3061對,減少1萬8685對"
  - p310 Year-on-year change in marriages, 2025 vs 2024 (couples) = **18,685** couple (2025-01-01..2025-12-31) [keep: ] quote: "相比2024年的12萬3061對,減少1萬8685對"
  - p311 Divorces in Taiwan, full year 2025 (couples) = **52,101** couple (2025-01-01..2025-12-31) [keep: ] quote: "去年離婚對數5萬2101對,折合年粗離婚率為千分之2.23"
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 28/28
  - p312 Taiwan total population, end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長。"
  - p313 Taiwan total population change vs same month prior year, July 2026 = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%"
  - p314 Taiwan total population change vs previous month, July 2026 = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "與6月相比則減少0.04%,是連續31個月出現人口負成長。"
  - p315 Consecutive months of population decline through July 2026 = **31** month (2026-07-31..2026-07-31) [keep: ] quote: "是連續31個月出現人口負成長"
  - p316 Live births registered in Taiwan, July 2026 = **7,906** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人"
  - p317 Crude birth rate annualised, July 2026 = **4.01** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為4.01‰"
  - p318 Live births registered in Taiwan, May 2026 = **6,832** birth (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p319 Live births registered in Taiwan, June 2026 = **7,324** birth (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p320 Year-on-year change in July births, 2026 vs 2025 = **1,033** birth (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p321 Year-on-year percent decline in July births, 2026 vs 2025 = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p322 Deaths registered in Taiwan, July 2026 = **17,119** death (2026-07-01..2026-07-31) [keep: ] quote: "7月死亡人數則為1萬7119人"
  - p323 Average interval between deaths, July 2026 = **2.6** minute per death (2026-07-01..2026-07-31) [keep: ] quote: "平均約每2.6分鐘有一人死亡"
  - p324 Crude death rate annualised, July 2026 = **8.67** deaths per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰"
  - p325 Year-on-year change in July deaths, 2026 vs 2025 = **1.62** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p326 Month-on-month change in July deaths, 2026 vs June 2026 = **4.77** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p327 Share of population aged 65+, Taiwan, end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口占20.54%"
  - p328 Share of population aged 15-64, Taiwan, end of July 2026 = **68.15** % (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p329 Share of population aged 0-14, Taiwan, end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p330 Highest county/city crude birth rate, Taitung County, July 2026 = **6.06** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "粗出生率最高為台東縣6.06‰"
  - p331 Crude birth rate, Yunlin County, July 2026 = **5.29** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "其次分別為雲林縣5.29‰、連江縣5.18‰"
  - p332 Crude birth rate, Lienchiang County, July 2026 = **5.18** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "其次分別為雲林縣5.29‰、連江縣5.18‰"
  - p333 Lowest county/city crude birth rate, Keelung City, July 2026 = **2.1** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p334 Crude birth rate, Tainan City, July 2026 = **3.14** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p335 Crude birth rate, Chiayi County, July 2026 = **3.36** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "最低則依序為基隆市2.10‰、台南市3.14‰與嘉義縣3.36‰"
  - p336 Marriages registered in Taiwan, July 2026 = **7,150** couple (2026-07-01..2026-07-31) [keep: ] quote: "7月全台共有7150對,同婚占3.5%"
  - p337 Share of July 2026 marriages that were same-sex = **3.5** % (2026-07-01..2026-07-31) [keep: ] quote: "7月全台共有7150對,同婚占3.5%"
  - p338 Divorces registered in Taiwan, July 2026 = **4,450** couple (2026-07-01..2026-07-31) [keep: ] quote: "離婚對數為4450對,同婚占1.7%"
  - p339 Share of July 2026 divorces that were same-sex = **1.7** % (2026-07-01..2026-07-31) [keep: ] quote: "離婚對數為4450對,同婚占1.7%"
- `https://www.taiwannews.com.tw/news/6262219` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.ltn.com.tw/news/life/breakingnews/5304341` -> **snapshot** (snapshot 20260218031045); points raw/verified 26/26
  - p340 Taiwan total population at end of December 2025 (2025 year-end household registr = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "內政部今天公布2025年人口統計數據,整體人口數為2329萬9132人,較前年減少10萬1088人"
  - p341 Taiwan population decrease in 2025 vs 2024 = **101,088** person (2025-01-01..2025-12-31) [keep: ] quote: "整體人口數為2329萬9132人,較前年減少10萬1088人,跌幅僅次於2020年、2021年"
  - p342 Taiwan average daily population decrease in 2025 = **277** person (2025-01-01..2025-12-31) [keep: ] quote: "較2024年減少10萬1088人,平均每天減少276.95人"
  - p343 Taiwan live births registered in 2025 (full year) = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "台灣2025年全年僅10萬7812名新生兒出生,較2024年大幅減少2萬7044人,是台灣近10年跌幅最多"
  - p344 Taiwan live births registered in 2024 (full year) = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "相較於2024年新生兒數13萬4856人、年粗出生率千分之5.76,大幅減少2萬7044人"
  - p345 Change in Taiwan live births 2025 vs 2024 = **27,044** birth (2025-01-01..2025-12-31) [keep: ] quote: "去年全年僅10萬7812名新生兒出生,較2024年大幅減少2萬7044人,是台灣近10年跌幅最多"
  - p346 Taiwan crude birth rate 2025 (births per 1,000 population) = **4.62** birth per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "2025年全年新生兒數10萬7812人,折合年粗出生率為千分之4.62"
  - p347 Taiwan crude birth rate 2024 (births per 1,000 population) = **5.76** birth per 1,000 person (2024-01-01..2024-12-31) [keep: ] quote: "相較於2024年新生兒數13萬4856人、年粗出生率千分之5.76"
  - p348 Taiwan live births registered in 2023 (full year) = **135,571** birth (2023-01-01..2023-12-31) [keep: ] quote: "2022年13萬8986人、2023年13萬5571人、2024年13萬4856人、2025年10萬7812人"
  - p349 Taiwan live births registered in 2022 (full year) = **138,986** birth (2022-01-01..2022-12-31) [keep: ] quote: "2021年15萬3820人、2022年13萬8986人、2023年13萬5571人"
  - p350 Taiwan live births registered in 2021 (full year) = **153,820** birth (2021-01-01..2021-12-31) [keep: ] quote: "2020年16萬5249人、2021年15萬3820人、2022年13萬8986人"
  - p351 Taiwan live births registered in 2020 (full year) = **165,249** birth (2020-01-01..2020-12-31) [keep: ] quote: "2019年17萬7767人、2020年16萬5249人、2021年15萬3820人"
  - p352 Taiwan live births registered in 2019 (full year) = **177,767** birth (2019-01-01..2019-12-31) [keep: ] quote: "2018年18萬1601人、2019年17萬7767人、2020年16萬5249人"
  - p353 Taiwan live births registered in 2018 (full year) = **181,601** birth (2018-01-01..2018-12-31) [keep: ] quote: "2017年19萬3844人、2018年18萬1601人、2019年17萬7767人"
  - p354 Taiwan live births registered in 2017 (full year) = **193,844** birth (2017-01-01..2017-12-31) [keep: ] quote: "分別為2016年20萬8440人、2017年19萬3844人、2018年18萬1601人"
  - p355 Taiwan live births registered in 2016 (full year) = **208,440** birth (2016-01-01..2016-12-31) [keep: ] quote: "分別為2016年20萬8440人、2017年19萬3844人、2018年18萬1601人"
  - p356 Taiwan deaths registered in 2025 (full year) = **200,268** death (2025-01-01..2025-12-31) [keep: ] quote: "2025全年死亡數為20萬268人,折合年粗死亡率為千分之8.58"
  - p357 Taiwan crude death rate 2025 (deaths per 1,000 population) = **8.58** death per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "2025全年死亡數為20萬268人,折合年粗死亡率為千分之8.58"
  - p358 Taiwan deaths registered in 2024 (full year) = **202,107** death (2024-01-01..2024-12-31) [keep: ] quote: "相較2024年全年死亡數為20萬2107人,減少1839人"
  - p359 Taiwan in-migrants (moves in) in December 2025 = **74,682** person (2025-12-01..2025-12-31) [keep: ] quote: "2025年12月遷入人口數為7萬4682人,較2024年同月減少1萬1838人"
  - p360 Taiwan marriages in 2025 (couples) = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "2025年結婚對數為10萬4376對,折合年粗結婚率為千分之4.47"
  - p361 Taiwan marriages in 2024 (couples) = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "較2024年結婚對數為12萬3061對,減少1萬8635對"
  - p362 Taiwan population aged 0-14 at end of December 2025 = **2,681,890** person (2025-12-31..2025-12-31) [keep: ] quote: "2025年12月底,0歲至14歲人口數為268萬1890人,占總人口比率11.51%"
  - p363 Taiwan population aged 15-64 at end of December 2025 = **15,944,087** person (2025-12-31..2025-12-31) [keep: ] quote: "15歲至64歲人口數為1594萬4087人,占68.43%"
  - p364 Taiwan population aged 65+ at end of December 2025 = **4,673,155** person (2025-12-31..2025-12-31) [keep: ] quote: "65歲以上人口數為467萬3155人,占20.06%;台灣正式邁入超高齡社會"
  - p365 Share of Taiwan population aged 65+ at end of December 2025 = **20.06** % (2025-12-31..2025-12-31) [keep: ] quote: "65歲以上人口數為467萬3155人,占20.06%"
- `https://www.gvm.com.tw/article/127667` -> **snapshot** (snapshot 20260611063150); points raw/verified 22/21
  - p366 Taiwan live births, 2025 (annual total) = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年的新生兒共有10萬7812人、死亡人數為20萬0268人"
  - p367 Taiwan deaths, 2025 (annual total) = **200,268** deaths (2025-01-01..2025-12-31) [keep: ] quote: "2025年的新生兒共有10萬7812人、死亡人數為20萬0268人"
  - p368 Taiwan live births, 2024 (annual total) = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "回顧2024年,台灣的新生兒人數為13萬4856人,當時已創下史上最低紀錄"
  - p369 Taiwan live births, 1976 Dragon Year (historical peak, annual total) = **425,125** births (1976-01-01..1976-12-31) [keep: ] quote: "無論是1976年龍年創下42萬5125名新生兒的歷史高峰"
  - p370 Dragon-year excess births over prior year (1988/2000/2012 Dragon Years) = **250,000,000** (range 200,000,000..300,000,000) as written "2至3萬", value check pending births (not stated (page dated 2026-01-29)) [DISCARD: Already discarded; value is nonsensical (250 million) and unusable.] quote: "還是1988年、2000年、2012年龍年,都能比前一年多出2至3萬名新生兒"
  - p371 Taiwan forecast: 2026 live births likely to fall below 100,000 (stated bound) = **100,000** births (2026-01-01..2026-12-31) [keep: ] quote: "2026年的新生兒很可能跌破10萬"
  - p372 Taiwan consecutive years of population decline (through 2025) = **6** years (2020-01-01..2025-12-31) [keep: ] quote: "這已經是台灣人口持續6年負成長"
  - p373 Taiwan median annual salary, all workers, 2024 = **546,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "以2024年為例,全台灣勞工的年薪中位數為54.6萬元"
  - p374 Taiwan median annual salary, all workers, 2023 = **525,000** TWD (2023-01-01..2023-12-31) [keep: ] quote: "比2023年的52.5萬、2022年的51.8萬和2021年的50.8萬高"
  - p375 Taiwan median annual salary, all workers, 2022 = **518,000** TWD (2022-01-01..2022-12-31) [keep: ] quote: "比2023年的52.5萬、2022年的51.8萬和2021年的50.8萬高"
  - p376 Taiwan median annual salary, all workers, 2021 = **508,000** TWD (2021-01-01..2021-12-31) [keep: ] quote: "比2023年的52.5萬、2022年的51.8萬和2021年的50.8萬高"
  - p377 Hsinchu City median annual salary, 2024 (highest county/city) = **902,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "新竹市的年薪中位數最高,達90.2萬元"
  - p378 Hsinchu County median annual salary, 2024 = **736,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "新竹縣其次,為73.6萬元"
  - p379 Taipei City median annual salary, 2024 = **735,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "再來是台北市的73.5萬元"
  - p380 Changhua County median annual salary, 2024 (lower-wage county) = **468,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "就包含年薪中位數46.8萬的彰化縣"
  - p381 Pingtung County median annual salary, 2024 = **479,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "47.9萬的屏東縣"
  - p382 Taitung County median annual salary, 2024 = **483,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "與48.3萬的台東縣"
  - p383 Parental leave: maximum unpaid parental leave duration = **2** as written "兩年", value check pending years (not stated (page dated 2026-01-29)) [keep: ] quote: "最長可請兩年的育嬰留職停薪"
  - p384 Parental leave allowance: share of insured salary paid for first 6 months = **80** % (not stated (page dated 2026-01-29)) [keep: ] quote: "前6個月可領取投保薪資80%的育嬰留職津貼"
  - p385 Paid prenatal checkup leave days (Taiwan) = **7** days (not stated (page dated 2026-01-29)) [keep: ] quote: "有薪產檢假增至7日"
  - p386 Paid paternity/prenatal-companion leave days combined (Taiwan) = **7** days (not stated (page dated 2026-01-29)) [keep: ] quote: "配偶的有薪陪產檢與陪產假合計7日"
- `https://www.rti.org.tw/news?uid=3&pid=225273` -> **snapshot** (snapshot 20260815163625); points raw/verified 26/25
  - p387 Taiwan population at end of July 2026 (mid-2026 proxy) = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年(2026年)7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p388 Live births registered in Taiwan, July 2026 = **7,906** births (2026-07-01..2026-07-31) [keep: ] quote: "7月新生兒7906人,較6月增加582人"
  - p389 Change in monthly live births, June to July 2026 = **582** births (2026-06-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒,折合年粗出生率為千分之4.01,較去年同期減少1033人,相比今年6月增加582人。"
  - p390 Cumulative live births registered in Taiwan, January-July 2026 = **54,250** births (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看,較去年同期的6萬4314人,減少1萬64人。"
  - p391 Year-on-year decline in January-July live births, 2026 vs 2025 = **10,064** births (2026-01-01..2026-07-31) [keep: ] quote: "較去年同期的6萬4314人,減少1萬64人。"
  - p392 Year-on-year change in July live births, 2026 vs 2025 = **1,033** births (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人,相比今年6月增加582人。"
  - p393 Annual crude birth rate implied for July 2026 = **4.01** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為千分之4.01"
  - p394 Average interval between births, July 2026 = **5.6** minutes per birth (2026-07-01..2026-07-31) [keep: ] quote: "約每5.6分鐘出生一個嬰兒"
  - p395 Deaths registered in Taiwan, July 2026 = **17,119** deaths (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人,平均約每2.6分鐘1人死亡"
  - p396 Cumulative deaths registered in Taiwan, January-July 2026 = **115,628** deaths (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月累計數據來看,死亡數共11萬5628人,新生兒共5萬4250人"
  - p397 Taiwan population at end of July 2026, year-on-year decrease = **102,934** person (2025-07-31..2026-07-31) [keep: ] quote: "較去年同期減少10萬2934人,平均每天減少282.01人"
  - p398 Average daily population decrease, July 2026 vs July 2025 = **282** person per day (2025-07-31..2026-07-31) [keep: ] quote: "平均每天減少282.01人"
  - p399 Taiwan population change, June to July 2026 = **8,563** person (2026-06-30..2026-07-31) [keep: ] quote: "相比今年6月則減少8563人"
  - p400 Natural population increase, Taiwan, July 2026 = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p401 Population aged 0-14, Taiwan, end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p402 Share of population aged 0-14, Taiwan, end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p403 Population aged 15-64, Taiwan, end of July 2026 = **15,835,491** person (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口數1583萬5491人,占68.15%"
  - p404 Population aged 65 and over, Taiwan, end of July 2026 = **4,773,519** person (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p405 Share of population aged 65 and over, Taiwan, end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p406 In-migrants to Taiwan, July 2026 = **74,647** person (2026-07-01..2026-07-31) [keep: ] quote: "7月遷入人口數7萬4647人,較6月增加9546人"
  - p407 Out-migrants from Taiwan, July 2026 = **73,997** person (2026-07-01..2026-07-31) [keep: ] quote: "遷出共7萬3997人,較6月增加8836人"
  - p408 Net migration, Taiwan, July 2026 = **650** person (2026-07-01..2026-07-31) [keep: ] quote: "淨遷入人口數為650人"
  - p409 Consecutive months of population decline, Taiwan, through July 2026 = **31** months (2024-01-01..2026-07-31) [keep: ] quote: "連續31個月負成長"
  - p410 Highest county/city crude birth rate, Taitung County, July 2026 = **6.06** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "粗出生率最高為台東縣千分之6.06"
  - p411 Lowest county/city crude birth rate, Keelung City, July 2026 = **2.1** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "最低為基隆市千分之2.10"
- `https://www.bigmedia.com.tw/article/1773546826373` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/aipl/202608100072.aspx` -> **snapshot** (snapshot 20260903232636); points raw/verified 27/26
  - p412 Taiwan total population at end of July 2026 (ROC year 115, month 7) = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "截至今年7月底,台灣人口數2323萬5002人,連續31個月負成長"
  - p413 Taiwan population decrease versus same month previous year, July 2026 = **102,934** person (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少10萬2934人"
  - p414 Taiwan average daily population decrease, July 2026 = **282** person/day (2026-07-01..2026-07-31) [keep: ] quote: "平均每天減少282.01人"
  - p415 Taiwan population decrease versus June 2026, July 2026 = **8,563** person (2026-07-01..2026-07-31) [keep: ] quote: "相比今年6月則減少8563人"
  - p416 Live births registered in Taiwan, July 2026 = **7,906** birth (2026-07-01..2026-07-31) [keep: ] quote: "7月出生數7906人,約每5.6分鐘出生一個嬰兒"
  - p417 Minutes per birth, Taiwan July 2026 = **5.6** minute/birth (2026-07-01..2026-07-31) [keep: ] quote: "約每5.6分鐘出生一個嬰兒"
  - p418 Annual crude birth rate, Taiwan July 2026 = **4.01** birth/(1000 person*year) (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為千分之4.01"
  - p419 Live births registered in Taiwan, July 2026 decrease versus July 2025 = **1,033** birth (2026-07-01..2026-07-31) [keep: ] quote: "較去年同期減少1033人"
  - p420 Live births registered in Taiwan, July 2026 increase versus June 2026 = **582** birth (2026-07-01..2026-07-31) [keep: ] quote: "相比今年6月增加582人"
  - p421 Live births registered in Taiwan, January to July 2026 cumulative = **54,250** birth (2026-01-01..2026-07-31) [keep: ] quote: "以今年前7月新生兒共5萬4250人來看"
  - p422 Year-on-year decrease in live births, Taiwan January-July 2026 versus January-Ju = **10,064** birth (2026-01-01..2026-07-31) [keep: ] quote: "減少1萬64人"
  - p423 Deaths registered in Taiwan, July 2026 = **17,119** death (2026-07-01..2026-07-31) [keep: ] quote: "7月人口死亡數1萬7119人"
  - p424 Minutes per death, Taiwan July 2026 = **2.6** minute/death (2026-07-01..2026-07-31) [keep: ] quote: "平均約每2.6分鐘1人死亡"
  - p425 Annual crude death rate, Taiwan July 2026 = **8.67** death/(1000 person*year) (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為千分之8.67"
  - p426 Deaths registered in Taiwan, January to July 2026 cumulative = **115,628** death (2026-01-01..2026-07-31) [keep: ] quote: "死亡數共11萬5628人,新生兒共5萬4250人"
  - p427 Natural increase (births minus deaths), Taiwan July 2026 = **9,213** person (2026-07-01..2026-07-31) [keep: ] quote: "台灣7月人口自然增加為負9213人"
  - p428 Population aged 0-14, Taiwan end of July 2026 = **2,625,992** person (2026-07-31..2026-07-31) [keep: ] quote: "今年7月底0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p429 Share of population aged 0-14, Taiwan end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [keep: ] quote: "0至14歲人口數262萬5992人,占總人口比率11.30%"
  - p430 Population aged 15-64, Taiwan end of July 2026 = **15,835,491** person (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口數1583萬5491人,占68.15%"
  - p431 Share of population aged 15-64, Taiwan end of July 2026 = **68.15** % (2026-07-31..2026-07-31) [keep: ] quote: "15至64歲人口數1583萬5491人,占68.15%"
  - p432 Population aged 65 and over, Taiwan end of July 2026 = **4,773,519** person (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p433 Share of population aged 65 and over, Taiwan end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [keep: ] quote: "65歲以上人口數為477萬3519人,占20.54%"
  - p434 Consecutive months of negative population growth, Taiwan through July 2026 = **31** month (2024-01-01..2026-07-31) [keep: ] quote: "台灣人口數2323萬5002人,連續31個月負成長"
  - p435 In-migrants to Taiwan, July 2026 = **74,647** person (2026-07-01..2026-07-31) [keep: ] quote: "7月遷入人口數7萬4647人,較6月增加9546人"
  - p436 Out-migrants from Taiwan, July 2026 = **73,997** person (2026-07-01..2026-07-31) [keep: ] quote: "遷出共7萬3997人,較6月增加8836人"
  - p437 Net social increase (in-migrants minus out-migrants), Taiwan July 2026 = **650** person (2026-07-01..2026-07-31) [keep: ] quote: "淨遷入人口數為650人"
- `https://www.ris.gov.tw/info-liferay/app/channel/newsEnglishDetail/26245250` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2025.pdf` -> **snapshot** (snapshot 20260219170633) **LEAK SENTINEL HIT ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)', '(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://210.241.78.32/EngPages/Detail.aspx?nodeid=4524&pid=20269` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.setn.com/news/1778835` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (scale word '萬' not supported by quote or table header: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d4 [forecasts_markets] Official projections and nowcasts

Hypothesis: National Development Council (國發會) population projections and any 2026 monthly nowcasts/forecasts give an independent level estimate for 2026 births; compare with route d1 to bracket the September value.

Queries issued by the searcher: 國發會 人口推估 2026 出生數; Taiwan population projection 2026 births National Development Council; 內政部 2026年7月 出生數 統計 戶政 每月; 2026 台灣 出生數 前7月 5.4萬 內政部 統計; 國發會 人口推估 2026 出生數 推估; Taiwan population projection 2026 births National Development Council; 內政部 戶政司 2026年7月 出生數 統計 1至7月 新生兒; 2025年9月 出生數 台灣 內政部 新生兒 月; 國發會 人口推估 2026 出生數; Taiwan population projection 2026 births National Development Council; 內政部 2026年7月 出生數 統計 戶政; 台灣 2026年 前7月 出生人數 5.4萬 內政部 統計

- `https://www.ndc.gov.tw/News_Content.aspx?n=114AAE178CD95D4C&s=6F7655EDC5AAD458` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cna.com.tw/news/afe/202608280213.aspx` -> **snapshot** (snapshot 20260829104307); points raw/verified 21/21
  - p438 NDC 2026 annual projected live births, central estimate (Taiwan) = **94,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒出生數將跌破10萬人大關、中推估值為9.4萬人。"
  - p439 NDC 2026 annual projected live births, range (Taiwan) = **94,500** (range 92,000..97,000) as written "9.2萬至9.7萬", value check pending birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒數將跌破10萬人大關,估計落在9.2萬至9.7萬人,中推估值為9.4萬人。"
  - p440 2025 registered live births (Taiwan, MOI) = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "根據內政部資訊,2025年台灣新生兒數為10萬7812人,連10年下降,再創新低。"
  - p441 Taiwan total fertility rate 2025 = **0.7** birth per woman (2025-01-01..2025-12-31) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p442 Japan total fertility rate (comparison) = **1.14** birth per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p443 Singapore total fertility rate (comparison) = **0.87** birth per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p444 South Korea total fertility rate (comparison) = **0.8** birth per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣2025年生育率則是0.7人,低於日本1.14人、新加坡0.87人、韓國0.8人。"
  - p445 Threshold defining 'ultra-low' fertility rate in Asia (births per woman) = **1.3** birth per woman (not stated (page dated 2026-08-28)) [keep: ] quote: "亞洲主要鄰國多已落入超低生育率1.3人以下"
  - p446 Working-age (15-64) share of total population threshold defining demographic div = **66.7** % (not stated (page dated 2026-08-28)) [keep: ] quote: "人口紅利是指青壯年人口(15至64歲人口、又稱工作年齡人口)占總人口比重達66.7%以上"
  - p447 Year demographic dividend was previously projected to end (Taiwan) = **2,028** year (2028-01-01..2028-12-31) [keep: ] quote: "國發會原先推估台灣的「人口紅利」將於2028年結束"
  - p448 Year demographic dividend now projected to end (Taiwan), delayed by 2 years = **2,030** year (2030-01-01..2030-12-31) [keep: ] quote: "人口紅利結束時間點反而延後2年、為2030年"
  - p449 Delay in demographic dividend end year (years) = **2** year (not stated (page dated 2026-08-28)) [keep: ] quote: "人口紅利結束時間點反而延後2年、為2030年"
  - p450 Consecutive years of declining newborn count (Taiwan, through 2025) = **10** year (not stated (page dated 2026-08-28)) [keep: ] quote: "2025年台灣新生兒數為10萬7812人,連10年下降,再創新低"
  - p451 Frequency of NDC population projection updates (years) = **2** year (not stated (page dated 2026-08-28)) [keep: ] quote: "國發會每2年依據最新戶籍人口資料,更新出生、死亡及遷徙等人口變動要素的假設情境"
  - p452 Lower bound of 2026 newborn count estimate (Taiwan) = **92,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "估計落在9.2萬至9.7萬人,中推估值為9.4萬人"
  - p453 Upper bound of 2026 newborn count estimate (Taiwan) = **97,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "估計落在9.2萬至9.7萬人,中推估值為9.4萬人"
  - p454 2026 newborn count threshold not to be exceeded (Taiwan, 100,000) = **100,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "今年新生兒出生數將跌破10萬人大關、中推估值為9.4萬人。"
  - p455 Age range of women/men whose marriage rate is cited (lower bound) = **20** year of age (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣20至49歲男、女性有偶率持續下滑"
  - p456 Age range of women/men whose marriage rate is cited (upper bound) = **49** year of age (not stated (page dated 2026-08-28)) [keep: ] quote: "台灣20至49歲男、女性有偶率持續下滑"
  - p457 Lower bound of working-age definition (years of age) = **15** year of age (not stated (page dated 2026-08-28)) [keep: ] quote: "人口紅利是指青壯年人口(15至64歲人口、又稱工作年齡人口)"
  - p458 Upper bound of working-age definition (years of age) = **64** year of age (not stated (page dated 2026-08-28)) [keep: ] quote: "人口紅利是指青壯年人口(15至64歲人口、又稱工作年齡人口)"
- `https://focustaiwan.tw/society/202608290010` -> **snapshot** (snapshot 20260830111536); points raw/verified 14/14
  - p459 NDC projected Taiwan population decline from 2026 levels to 2075 (percent) = **48** % (2026-01-01..2075-12-31) [keep: ] quote: "Taiwan's population is projected to fall 48 percent from 2026 levels to 12.15 million by 2075"
  - p460 NDC projected Taiwan population in 2075 = **12,150,000** person (2075-01-01..2075-12-31) [keep: ] quote: "to 12.15 million by 2075 because of a declining birth rate and a rapidly aging population"
  - p461 Taiwan newborns in 2025 (record low, 10th consecutive annual decline) = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "With the number of newborns in Taiwan falling for the 10th consecutive year to a record low of 107,812 in 2025"
  - p462 NDC stated upper bound for Taiwan newborns in 2026 (below 100,000) = **100,000** birth (2026-01-01..2026-12-31) [keep: ] quote: "the figure is likely to decline further to below 100,000 this year, the NDC said"
  - p463 Monthly child growth subsidy per child from birth to age 18 (NTD) = **5,000** NTD (not stated (page dated 2026-08-29)) [keep: ] quote: "the government will provide a monthly NT$5,000 (US$158) child growth subsidy for every child from birth until age 18"
  - p464 Monthly child growth subsidy per child (USD equivalent) = **158** USD (not stated (page dated 2026-08-29)) [keep: ] quote: "monthly NT$5,000 (US$158) child growth subsidy for every child from birth until age 18"
  - p465 Annual matched deposit cap for low-income parents (NTD) = **15,000** NTD (not stated (page dated 2026-08-29)) [keep: ] quote: "match deposits made by low-income parents, up to NT$15,000 per year"
  - p466 Additional childcare leave per parent under proposed changes (months) = **3** as written "three months", value check pending month (not stated (page dated 2026-08-29)) [keep: ] quote: "each parent would be entitled to an additional three months of childcare leave on top of the current six months"
  - p467 Current childcare leave per parent (months) = **6** as written "six months", value check pending month (not stated (page dated 2026-08-29)) [keep: ] quote: "an additional three months of childcare leave on top of the current six months"
  - p468 Proposed marriage leave (weeks) = **2** as written "two weeks", value check pending week (not stated (page dated 2026-08-29)) [keep: ] quote: "while marriage leave would be extended to two weeks"
  - p469 Current maternity leave (weeks) = **8** as written "eight weeks", value check pending week (not stated (page dated 2026-08-29)) [keep: ] quote: "Maternity leave would increase from eight weeks to 12 weeks"
  - p470 Proposed maternity leave (weeks) = **12** week (not stated (page dated 2026-08-29)) [keep: ] quote: "Maternity leave would increase from eight weeks to 12 weeks"
  - p471 Current paid prenatal checkup leave (week) = **1** as written "one week", value check pending week (not stated (page dated 2026-08-29)) [keep: ] quote: "paid leave for prenatal checkups and paternity leave would both double from one week to two weeks"
  - p472 Proposed paid prenatal checkup and paternity leave (weeks) = **2** as written "two weeks", value check pending week (not stated (page dated 2026-08-29)) [keep: ] quote: "paid leave for prenatal checkups and paternity leave would both double from one week to two weeks"
- `https://udn.com/news/story/7314/9720922?list_ch2_index` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businesstoday.com.tw/group_search/article?keywords=%E9%9D%A0%E7%A7%BB%E6%B0%91` -> **snapshot** (snapshot 20200803232235); points raw/verified 0/0
- `https://gpi.culture.tw/books/1011500947` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pchome.com.tw/search.php?k=3.36&p=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www3.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gvm.com.tw/article/132702` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://pttweb.tw/Gossiping/M.1786330590.A.DBA` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dev.taisounds.news/news/content/76/285689` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kanglin.com.tw/news/%e5%89%8d7%e5%80%8b%e6%9c%88%e6%96%b0%e7%94%9f%e5%85%925-7%e8%90%ac-%e5%83%85%e5%8e%bb%e5%b9%b4%e5%90%8c%e6%9c%9f84-3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Calendar and policy effects

Hypothesis: September 2026 has 30 days; registration-office closures (typhoons, Mid-Autumn Festival around late September) and any birth-incentive policy changes (e.g., expanded childcare allowances) can shift registered counts. Quantify exposure: number of working days and any known policy effective dates before cutoff.

Queries issued by the searcher: 台灣 2026 9月 連假 中秋節 放假 行事曆; 內政部 出生登記 統計 2026 每月 出生數; 育兒津貼 2026 新制 加碼 行政院 少子化 上路 日期; 2026年9月 颱風 停班停課 登陸 台灣; 台灣 2026 9月 連假 中秋節 放假 行事曆; 2026年 政府行政機關辦公日曆表 中秋節 9月; 育兒津貼 2026 新制 出生登記 內政部; 2026年9月 颱風 停班停課 颱風假 台灣; 內政部 戶政司 出生登記 統計 2026年 出生數 每月; 2026年1月1日 生育補助 10萬元 上路 行政院 少子女化; 台灣 2026 9月 連假 颱風 停班 中秋節; Taiwan birth incentive policy 2026 育兒津貼 生育補助; 內政部 戶政司 出生登記 統計 2026年8月 出生數; 2026 政府行政機關辦公日曆表 中秋節 教師節 放假 人事行政總處

- `https://www.chinatimes.com/realtimenews/20260903004037-260405` -> **snapshot** (snapshot 20260908020057); points raw/verified 11/11
  - p473 Length of Mid-Autumn Festival and Teachers' Day combined holiday in Taiwan, 2026 = **4** day (2026-09-25..2026-09-28) [keep: ] quote: "●中秋節、教師節連假4天: 9月25日(五)~9月28日(一)"
  - p474 Start date of Mid-Autumn Festival and Teachers' Day combined holiday in Taiwan,  = **25** as written "9月25日", value check pending day of month (2026-09-25..2026-09-25) [keep: ] quote: "●中秋節、教師節連假4天: 9月25日(五)~9月28日(一)"
  - p475 End date of Mid-Autumn Festival and Teachers' Day combined holiday in Taiwan, 20 = **28** as written "9月28日", value check pending day of month (2026-09-28..2026-09-28) [keep: ] quote: "●中秋節、教師節連假4天: 9月25日(五)~9月28日(一)"
  - p476 Number of consecutive holidays in Taiwan from September to end of 2026 = **4** holiday period (2026-09-01..2026-12-31) [keep: ] quote: "2026年9月起至年底有4個連假"
  - p477 Number of consecutive holidays in Taiwan from late September to late October 202 = **3** holiday period (2026-09-25..2026-10-31) [keep: ] quote: "9月底到10月底就有3個連假"
  - p478 Length of National Day holiday in Taiwan, 2026 = **3** day (2026-10-09..2026-10-11) [keep: ] quote: "●國慶日連假3天: 10月9日(五)~10月11日(日)"
  - p479 Length of Retrocession Day holiday in Taiwan, 2026 = **3** day (2026-10-24..2026-10-26) [keep: ] quote: "●光復節連假3天: 10月24日(六)~10月26日(一)"
  - p480 Length of Constitution Day holiday in Taiwan, 2026 = **3** day (2026-12-25..2026-12-27) [keep: ] quote: "●行憲紀念日連假3天: 12月25日(五)~12月27日(日)"
  - p481 Length of New Year 2027 holiday in Taiwan = **3** day (2027-01-01..2027-01-03) [keep: ] quote: "2027年元旦連假(1月1日(五)~1月3日(日),共3天)"
  - p482 Annual leave days needed to bridge Constitution Day and New Year 2027 holidays i = **4** day (2026-12-28..2026-12-31) [keep: ] quote: "只要請12月28日至12月31日共4天特休"
  - p483 Total consecutive days off from 2026-12-25 to 2027-01-03 using 4 annual leave da = **10** day (2026-12-25..2027-01-03) [keep: ] quote: "從12月25日一路休到隔年1月3日,爽放10天"
- `https://futureparenting.cwgv.com.tw/family/content/index/36367` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.gov.tw/News_NoticeCalendar_Content_temp.aspx?MetaI_D=874&n=3717` -> **snapshot** (snapshot 20250830051409); points raw/verified 0/0
- `https://www.ntcunion.org/page/news/show.aspx?num=4536&root=2&page=5&kind=2&lang=TW` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://verybaby.tw/wiki/39832` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mnews.tw/external/mirrordaily66129` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://newdoc.nccu.edu.tw/acadbonus/04/10300039/10300039.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ettoday.net/news/20260527/3172896.htm` -> **snapshot** (snapshot 20260625103144); points raw/verified 30/29
  - p484 Policy package announcement date (18 childcare measures, announced at national s = **27** day of month (2026-08-27..2026-08-27) [keep: ] quote: "總統賴清德27日召開國安高層會議"
  - p485 Earliest stated effective year for the 18 childcare measures (Executive Yuan mee = **2,027** year (2027-01-01..2027-12-31) [keep: ] quote: "最快拚明年(2027年)上路"
  - p486 Number of policy measures in the childcare package = **18** measure (not stated (page dated 2026-05-27)) [keep: ] quote: "逐一提出18項政策大禮包"
  - p487 Number of policy themes/areas in the package = **5** theme (not stated (page dated 2026-05-27)) [keep: ] quote: "《ETtoday新聞雲》彙整成5張圖表"
  - p488 Growth allowance for ages 0-18 per person per month (TWD) = **5,000** TWD per person per month (not stated (page dated 2026-05-27)) [keep: ] quote: "0至18歲每人每月領5,000元"
  - p489 Birth insurance top-up: each birth benefit topped up to (TWD) = **100,000** TWD per birth (not stated (page dated 2026-05-27)) [keep: ] quote: "每胎生育給付都補足至10萬元"
  - p490 Assisted reproduction subsidy, under age 45, attempts 1-3, per attempt (TWD, ran = **140,000** (range 130,000..150,000) as written "13至15萬元", value check pending TWD per attempt (not stated (page dated 2026-05-27)) [keep: ] quote: "未滿45歲第1至3次補助13至15萬元"
  - p491 Assisted reproduction subsidy, under age 40, attempts 4-6, per attempt (TWD) = **60,000** TWD per attempt (not stated (page dated 2026-05-27)) [keep: ] quote: "未滿40歲第4至6次每次補助6萬元"
  - p492 Childcare subsidy ages 0-2, at-home care, per month (TWD, range) = **6,000** (range 5,000..7,000) as written "5,000至7,000元", value check pending TWD per person per month (not stated (page dated 2026-05-27)) [keep: ] quote: "在家帶每月5,000至7,000元"
  - p493 Childcare subsidy ages 0-2, public childcare, per month (TWD, range) = **8,000** (range 7,000..9,000) as written "7,000至9,000元", value check pending TWD per person per month (not stated (page dated 2026-05-27)) [keep: ] quote: "公托7,000至9,000元"
  - p494 Childcare subsidy ages 0-2, quasi-public childcare, per month (TWD, range) = **14,000** (range 13,000..15,000) as written "1.3萬至1.5萬元", value check pending TWD per person per month (not stated (page dated 2026-05-27)) [keep: ] quote: "準公共托育1.3萬至1.5萬元"
  - p495 Parental leave allowance: months each parent receives after 6-month leave (addit = **3** month (not stated (page dated 2026-05-27)) [keep: ] quote: "可各再多領3個月,合計最高18個月"
  - p496 Parental leave allowance: maximum combined months for both parents = **18** month (not stated (page dated 2026-05-27)) [keep: ] quote: "合計最高18個月"
  - p497 Parental leave allowance: monthly allowance can exceed (TWD) = **40,000** TWD per month (not stated (page dated 2026-05-27)) [keep: ] quote: "使津貼補助可超過4萬元"
  - p498 Parental leave days per parent increased to (days) = **60** day (not stated (page dated 2026-05-27)) [keep: ] quote: "從30增加到60日,兩人合計120日"
  - p499 Parental leave days combined for both parents (days) = **120** day (not stated (page dated 2026-05-27)) [keep: ] quote: "兩人合計120日"
  - p500 Reduction in daily working hours for flexible parental work (hours) = **1** hour per day (not stated (page dated 2026-05-27)) [keep: ] quote: "勞工每日可減少1小時工時且不減薪"
  - p501 Tax-free allowance per minor child raised to (TWD) = **151,500** TWD per child (not stated (page dated 2026-05-27)) [keep: ] quote: "未成年子女免稅額提高至每名15.15萬元"
  - p502 Increase in tax exemption for minors and seniors (percent) = **50** % (not stated (page dated 2026-05-27)) [keep: ] quote: "再額外加碼未成年子女免稅額增加50%"
  - p503 Corporate childcare tax deduction cap (percent of expense) = **200** % (not stated (page dated 2026-05-27)) [keep: ] quote: "加倍減除至200%"
  - p504 Maximum subsidy for corporate childcare facilities (TWD) = **5,000,000** TWD (not stated (page dated 2026-05-27)) [keep: ] quote: "最高500萬元"
  - p505 Student loan interest rate cut (percentage points) = **1** % (not stated (page dated 2026-05-27)) [keep: ] quote: "學貸利息再降1%"
  - p506 Private college annual subsidy cap per student (TWD) = **35,000** TWD per student per year (not stated (page dated 2026-05-27)) [keep: ] quote: "私立大專校院每學年最高補助3.5萬元"
  - p507 Dormitory subsidy per semester (TWD, range) = **6,000** (range 5,000..7,000) as written "5,000至7,000元", value check pending TWD per student per semester (not stated (page dated 2026-05-27)) [keep: ] quote: "大專校院住宿補貼每學期5,000至7,000元"
  - p508 Subsidy for temporary worker replacement per person per day (TWD) = **800** TWD per person per day (not stated (page dated 2026-05-27)) [keep: ] quote: "每人每日800元"
  - p509 Subsidy for long-term replacement hire at firms under 200 employees, per person  = **20,000** TWD per person (not stated (page dated 2026-05-27)) [keep: ] quote: "200人以下企業聘長期替代人力,每名補助2萬元"
  - p510 Public kindergarten maximum fee (TWD) = **1,000** TWD (not stated (page dated 2026-05-27)) [keep: ] quote: "公幼最多繳1,000元"
  - p511 Childcare allowance for self-care or private kindergarten, per month (TWD, range = **6,000** (range 5,000..7,000) as written "5,000至7,000元", value check pending TWD per person per month (not stated (page dated 2026-05-27)) [keep: ] quote: "育兒津貼每月5,000至7,000元"
  - p512 Number of newborn disease screenings made free = **22** screening item (not stated (page dated 2026-05-27)) [keep: ] quote: "新生兒22項疾病篩檢全免費"
- `https://www.upmedia.mg/tw/focus/politics/259868` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.moi.gov.tw/cl.aspx?n=4412` -> **snapshot** (snapshot 20260814004304); points raw/verified 0/0
- `https://tw.trip.com/blog/2026action-tw` -> **snapshot** (snapshot 20260813003331); points raw/verified 26/26
  - p513 Taiwan 2026 Mid-Autumn Festival + Teachers' Day consecutive holiday length (days = **4** day (2026-09-25..2026-09-28) [keep: ] quote: "中秋節+教師節連假 \| 9月25日(星期五)至9月28日(星期一) \| 4 天"
  - p514 Taiwan 2026 Mid-Autumn Festival holiday length (days) = **3** day (2026-09-25..2026-09-27) [keep: ] quote: "2026年中秋節放假日期為9月25日(星期五)至9月27日(星期日),共3天。"
  - p515 Taiwan 2026 Teachers' Day (9/28) national holiday days off = **1** day (2026-09-28..2026-09-28) [keep: ] quote: "教師節(9/28 週一):紀念孔子誕辰,全國放假 1 天,搭配中秋節假期形成4 天連假"
  - p516 Taiwan 2026 total national holidays (days) in the year = **11** holiday (2026-01-01..2026-12-31) [keep: ] quote: "2026行事曆迎來重大調整!全年共有11個國定假期、9個連假!"
  - p517 Taiwan 2026 total consecutive holiday blocks (count) in the year = **9** consecutive holiday block (2026-01-01..2026-12-31) [keep: ] quote: "全年共有11個國定假期、9個連假!"
  - p518 Taiwan 2026 Armed Forces Day (9/3) — not a national holiday, listed as commemora = **3** as written "9月3日", value check pending day of month (2026-09-03..2026-09-03) [keep: ] quote: "⭐ 軍人節:9月3日(星期四)"
  - p519 Taiwan 2026 new holiday-system ('4+1') additional national holidays count = **4** new national holiday (2026-01-01..2026-12-31) [keep: ] quote: "2026行事曆 \| 4大新增國定假"
  - p520 Taiwan 2026 Labor Day holiday length (days) under new nationwide rule = **3** day (2026-05-01..2026-05-03) [keep: ] quote: "連假為 5/1(週五)~5/3(週日),共 3 天,無需額外請假"
  - p521 Taiwan 2026 Lunar New Year holiday length (days) = **9** day (2026-02-14..2026-02-22) [keep: ] quote: "春節連假 \| 2月14日(星期六)至2月22日(星期四) \| 9 天"
  - p522 Taiwan 2026 Qingming holiday length (days) = **4** day (2026-04-03..2026-04-06) [keep: ] quote: "清明連假 \| 4月3日(星期五)至4月6日(星期一) \| 4天"
  - p523 Taiwan 2026 Dragon Boat holiday length (days) = **3** day (2026-06-19..2026-06-21) [keep: ] quote: "端午連假 \| 6月19日(星期五)至6月21日(星期日) \| 3 天"
  - p524 Taiwan 2026 National Day holiday length (days) = **3** day (2026-10-09..2026-10-11) [keep: ] quote: "國慶連假 \| 10月9日(星期五)至10月11日(星期日) \| 3 天"
  - p525 Taiwan 2026 Retrocession Day holiday length (days) = **3** day (2026-10-24..2026-10-26) [keep: ] quote: "光復節連假 \| 10月24日(星期六)至10月26日(星期一) \| 3 天"
  - p526 Taiwan 2026 Constitution Day/Christmas holiday length (days) = **3** day (2026-12-25..2026-12-27) [keep: ] quote: "行憲紀念日連假(聖誕節) \| 12月25日(星期五)至12月27日(星期日) \| 3 天"
  - p527 Taiwan 2026 New Year's Day holiday length (days) = **1** day (2026-01-01..2026-01-01) [keep: ] quote: "元旦 \| 1 月 1 日(星期四) \| 1 天"
  - p528 Taiwan 2026 228 holiday length (days) = **3** day (2026-02-27..2026-03-01) [keep: ] quote: "228連假 \| 2月27日(星期五)至3月1日(星期日) \| 3 天"
  - p529 Taiwan 2026 winter vacation length (days) = **30** day (2026-01-24..2026-02-22) [keep: ] quote: "寒假:2026年1月24日至2月22日(2月11日開學),共計30天"
  - p530 Taiwan 2026 summer vacation length (days) = **61** day (2026-07-01..2026-08-30) [keep: ] quote: "暑假:2026年7月1日至8月30日(預計8月31日開學),共計61天"
  - p531 Taiwan 2026 Indigenous ceremonial holiday days (increased from 1) = **3** day (2026-01-01..2026-12-31) [keep: ] quote: "原住民族歲時祭儀:從 1 天增至 3 天"
  - p532 Taiwan 2026 Indigenous ceremonial holiday days before increase = **1** day (2026-01-01..2026-12-31) [keep: ] quote: "原住民族歲時祭儀:從 1 天增至 3 天"
  - p533 Taiwan annual leave minimum for 1-year tenure (days) = **7** day (2026-01-01..2026-12-31) [keep: ] quote: "年假下限調高:受僱滿 1 年者年假從 7 天起算"
  - p534 Taiwan annual leave maximum (days) under new rule = **10** day (2026-01-01..2026-12-31) [keep: ] quote: "年資越長休假越多(最多 10 天)"
  - p535 Years labor groups had sought statutory national holidays (per legislator statem = **8** year (not stated (page dated 2025-05-09)) [keep: ] quote: "勞動團體為國定假日法制化爭取長達 8 年"
  - p536 Taiwan 2026 Teachers' Day Confucius ceremony ritual steps (Taipei Confucius Temp = **37** ritual step (2026-09-28..2026-09-28) [keep: ] quote: "包含啟扉、迎神、進饌、上香、行獻禮、恭讀祝文、飲福受胙、撤饌、送神等 37 道儀程"
  - p537 Mid-Autumn + Teachers' Day leave strategy: days of leave requested = **4** day (2026-09-21..2026-09-24) [keep: ] quote: "請4天(9月21日至9月24日),可休10天:9月19日至9月28日"
  - p538 Mid-Autumn + Teachers' Day leave strategy: total consecutive days off = **10** day (2026-09-19..2026-09-28) [keep: ] quote: "請4天(9月21日至9月24日),可休10天:9月19日至9月28日"
- `https://tw.trip.com/blog/2026action-tw?locale=zh-TW&curr=MYR` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: low/high given but value_as_written is not a range: 1)

### d6 [related_series] Marriage and conception timing

Hypothesis: Births in September largely reflect conceptions around December of the prior year; December marriage counts and seasonal conception patterns (Lunar New Year timing) can explain September deviations from trend. Target = trend level × conception-season factor derived from prior-December conditions.

Queries issued by the searcher: 台灣 結婚登記 月別統計 2025年12月 內政部; Taiwan births nine months lag marriage December seasonality; 內政部 114年12月 結婚登記 對數 出生數 統計 月報; 台灣 2026年 出生數 月別 統計 內政部 115年; 台灣 結婚登記 月別統計 2025年12月 內政部; Taiwan births September 2025 monthly statistics Ministry of Interior; 2026年6月 出生數 內政部 戶口統計 新生兒; 2025年12月 結婚對數 內政部 統計 較上年; 台灣 結婚登記 月別統計 2025年12月 內政部; Taiwan monthly births 2025 2026 statistics Department of Household Registration; 內政部 2026年7月 出生數 新生兒 戶口統計; 2025年12月 結婚登記 對數 內政部 戶口統計 新生兒 12月

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 30/30
  - p539 Taiwan registered marriages, December 2025 (total couples) = **10,816** couple (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p540 Taiwan registered marriages, November 2025 (total couples) = **8,586** couple (2025-11-01..2025-11-30) [keep: ] quote: "8,586 8,327 259 4.48 1.52 - 4.03 1.23 - 4.38 0.81 -"
  - p541 Taiwan registered marriages, October 2025 (total couples) = **10,735** couple (2025-10-01..2025-10-31) [keep: ] quote: "10,735 10,428 307 5.42 0.58 4.78 0.48 - 4.37 0.74 -"
  - p542 Taiwan registered marriages, September 2025 (total couples) = **5,844** couple (2025-09-01..2025-09-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p543 Taiwan registered marriages, August 2025 (total couples) = **5,916** couple (2025-08-01..2025-08-31) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p544 Taiwan registered marriages, July 2025 (total couples) = **7,418** couple (2025-07-01..2025-07-31) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p545 Taiwan registered marriages, June 2025 (total couples) = **7,655** couple (2025-06-01..2025-06-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p546 Taiwan registered marriages, May 2025 (total couples) = **12,791** couple (2025-05-01..2025-05-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p547 Taiwan registered marriages, April 2025 (total couples) = **6,520** couple (2025-04-01..2025-04-30) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p548 Taiwan registered marriages, March 2025 (total couples) = **10,675** couple (2025-03-01..2025-03-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p549 Taiwan registered marriages, February 2025 (total couples) = **8,221** couple (2025-02-01..2025-02-28) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p550 Taiwan registered marriages, January 2025 (total couples) = **9,199** couple (2025-01-01..2025-01-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p551 Taiwan registered marriages, full year 2025 (total couples) = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "there were 104,376 marriages registered in 2025, including 3,305 same-sex marriages"
  - p552 Taiwan registered marriages, full year 2024 (total couples) = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "2024(1) 123,061 53,469 5.26 2.28"
  - p553 Taiwan registered births, September 2025 (total births) = **8,603** birth (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p554 Taiwan registered births, October 2025 (total births) = **9,458** birth (2025-10-01..2025-10-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p555 Taiwan registered births, November 2025 (total births) = **7,946** birth (2025-11-01..2025-11-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p556 Taiwan registered births, December 2025 (total births) = **9,027** birth (2025-12-01..2025-12-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p557 Taiwan registered births, August 2025 (total births) = **8,464** birth (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p558 Taiwan registered births, July 2025 (total births) = **8,939** birth (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p559 Taiwan registered births, June 2025 (total births) = **8,968** birth (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p560 Taiwan registered births, May 2025 (total births) = **8,433** birth (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p561 Taiwan registered births, April 2025 (total births) = **8,684** birth (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p562 Taiwan registered births, March 2025 (total births) = **9,388** birth (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p563 Taiwan registered births, February 2025 (total births) = **10,407** birth (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p564 Taiwan registered births, January 2025 (total births) = **9,495** birth (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p565 Taiwan registered births, full year 2025 (total births) = **107,812** birth (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p566 Taiwan registered births, full year 2024 (total births) = **134,856** birth (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p567 Taiwan December 2025 crude marriage rate (annual basis) = **5.47** marriages per 1,000 population (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p568 Taiwan December 2025 seasonally adjusted marriage rate (annual basis) = **4.18** marriages per 1,000 population (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
- `https://stats.tw/society/marriage-divorce` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.taiwannews.com.tw/news/6395437` -> **snapshot** (snapshot 20260825233038); points raw/verified 32/32
  - p569 Taiwan total marriage registrations, 2025 (annual) = **104,376** marriage (2025-01-01..2025-12-31) [keep: ] quote: "Taiwan recorded 104,376 marriage registrations in 2025, a 15.2% decrease from the previous year"
  - p570 Year-on-year change in Taiwan marriage registrations, 2025 vs 2024 = **15.2** % (2025-01-01..2025-12-31) [keep: ] quote: "a 15.2% decrease from the previous year"
  - p571 Taiwan marriage registrations peak, 2016 (annual, approximate) = **148,000** marriage (2016-01-01..2016-12-31) [keep: ] quote: "falling from a peak of about 148,000 couples in 2016"
  - p572 Taiwan opposite-sex couple marriages registered, 2025 = **101,071** marriage (2025-01-01..2025-12-31) [keep: ] quote: "101,071 were between opposite-sex couples"
  - p573 Taiwan same-sex marriages registered, 2025 = **3,305** marriage (2025-01-01..2025-12-31) [keep: ] quote: "while 3,305 were same-sex marriages"
  - p574 Taiwan marriages between two Taiwanese citizens, 2025 = **85,042** marriage (2025-01-01..2025-12-31) [keep: ] quote: "85,042 couples, or 81.5%, consisted of two Taiwanese citizens"
  - p575 Share of Taiwan marriages between two Taiwanese citizens, 2025 = **81.5** % (2025-01-01..2025-12-31) [keep: ] quote: "85,042 couples, or 81.5%, consisted of two Taiwanese citizens"
  - p576 Taiwan marriages involving one foreign-national spouse, 2025 = **19,334** marriage (2025-01-01..2025-12-31) [keep: ] quote: "The remaining 19,334 marriages, or 18.5%, involved one spouse who was a foreign national"
  - p577 Share of Taiwan marriages involving a foreign spouse, 2025 = **18.5** % (2025-01-01..2025-12-31) [keep: ] quote: "Marriages involving a foreign spouse accounted for 18.5% of all registered marriages in 2025"
  - p578 Change in foreign-spouse share of Taiwan marriages, 2025 vs 2024 = **0.7** % (2025-01-01..2025-12-31) [keep: ] quote: "up 0.7% from the previous year"
  - p579 Taiwan same-sex marriages between men, 2025 = **1,043** marriage (2025-01-01..2025-12-31) [keep: ] quote: "1,043 were between men, and 2,262 were between women"
  - p580 Taiwan same-sex marriages between women, 2025 = **2,262** marriage (2025-01-01..2025-12-31) [keep: ] quote: "1,043 were between men, and 2,262 were between women"
  - p581 New Taipei same-sex marriages registered, 2025 = **651** marriage (2025-01-01..2025-12-31) [keep: ] quote: "New Taipei recorded the highest number, with 651 same-sex marriages"
  - p582 Taoyuan same-sex marriages registered, 2025 = **416** marriage (2025-01-01..2025-12-31) [keep: ] quote: "followed by Taoyuan and Taichung, each registering 416"
  - p583 Taichung same-sex marriages registered, 2025 = **416** marriage (2025-01-01..2025-12-31) [keep: ] quote: "followed by Taoyuan and Taichung, each registering 416"
  - p584 Taiwan crude marriage rate, 2025 = **4.5** marriage per 1,000 person (2025-01-01..2025-12-31) [keep: ] quote: "Taiwan's crude marriage rate, the number of marriages per 1,000 people, fell to 4.5 in 2025"
  - p585 Taiwan crude marriage rate, 2024 = **5.3** marriage per 1,000 person (2024-01-01..2024-12-31) [keep: ] quote: "fell to 4.5 in 2025, down from 5.3 in 2024"
  - p586 Taiwan marriages to Southeast Asian spouses, 2025 = **9,596** marriage (2025-01-01..2025-12-31) [keep: ] quote: "Spouses from Southeast Asia made up the largest group, with 9,596 marriages"
  - p587 Southeast Asian spouses' share of Taiwan foreign-spouse marriages, 2025 = **49.6** % (2025-01-01..2025-12-31) [keep: ] quote: "representing 49.6% of all marriages to a foreign spouse"
  - p588 Southeast Asian spouses' share of all Taiwan marriages, 2025 = **9.2** % (2025-01-01..2025-12-31) [keep: ] quote: "and 9.2% of all marriages registered in 2025"
  - p589 Taiwan marriages to Chinese spouses, 2025 = **5,170** marriage (2025-01-01..2025-12-31) [keep: ] quote: "Spouses from China totaled 5,170"
  - p590 Chinese spouses' share of Taiwan foreign-spouse marriages, 2025 = **26.7** % (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 26.7% of marriages to a foreign spouse"
  - p591 Chinese spouses' share of all Taiwan marriages, 2025 = **5** % (2025-01-01..2025-12-31) [keep: ] quote: "and 5% of all marriages, per the press release"
  - p592 Taiwan marriages to Vietnamese spouses (excluding China), 2025 = **6,427** marriage (2025-01-01..2025-12-31) [keep: ] quote: "Vietnamese nationals were the largest group, with 6,427 foreign spouse marriages"
  - p593 Taiwan marriages to US-national spouses, 2025 = **880** marriage (2025-01-01..2025-12-31) [keep: ] quote: "They were followed by US nationals, with 880 marriages"
  - p594 Taiwan marriages to Indonesian-national spouses, 2025 = **821** marriage (2025-01-01..2025-12-31) [keep: ] quote: "and Indonesian nationals, with 821"
  - p595 Female non-Taiwanese spouses marrying Taiwanese citizens, 2025 = **13,471** marriage (2025-01-01..2025-12-31) [keep: ] quote: "13,471, or 69.7%, were women"
  - p596 Share of non-Taiwanese spouses who were women, 2025 = **69.7** % (2025-01-01..2025-12-31) [keep: ] quote: "13,471, or 69.7%, were women"
  - p597 Male non-Taiwanese spouses marrying Taiwanese citizens, 2025 = **5,863** marriage (2025-01-01..2025-12-31) [keep: ] quote: "while 5,863, or 30.3%, were men"
  - p598 Share of non-Taiwanese spouses who were men, 2025 = **30.3** % (2025-01-01..2025-12-31) [keep: ] quote: "while 5,863, or 30.3%, were men"
  - p599 Gender ratio of non-Taiwanese spouses, 2025 = **43.5** 1 (male per 100 female non-Taiwanese spouses) (2025-01-01..2025-12-31) [keep: ] quote: "with the gender ratio rising from 31.8 in 2016 to 43.5 in 2025"
  - p600 Gender ratio of non-Taiwanese spouses, 2016 = **31.8** 1 (male per 100 female non-Taiwanese spouses) (2016-01-01..2016-12-31) [keep: ] quote: "with the gender ratio rising from 31.8 in 2016 to 43.5 in 2025"
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMzMzOC9hNmM4ZmJlOS1iOTc4LTQ1OGYtOGM0MS1kZTk5ZmZiMmIxNTYucGRm&n=MTE1MDQucGRm&` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.tycg.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMTUyL3JlbGZpbGUvMTg1NDQvMTYxNzU4NC84MDc2Yzg0My1kNTQ3LTRhYzUtODIwOC05ZmIzMTg1MzJmNjIucGRm&n=MTE1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bas.ntpc.gov.tw/uploaddowndoc?dis=bas21&file=bas21/202505061003410.pdf&filedisplay=%E6%96%B0%E5%8C%97%E5%B8%82%E9%87%8D%E8%A6%81%E7%B5%B1%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvNDIwL3JlbGZpbGUvMjA4MDQvOTM0ODY3MS85NWVlMzk3MS0yNjM5LTRiZDItYWJjZS1lYjhlYmUxY2ZjZGEucGRm&n=N` -> **snapshot** (snapshot 20260712030706); points raw/verified 29/29
  - p601 Monthly marriage registrations (different-sex couples), December, Taiwan (ROC ye = **94** couple (2025-12-01..2025-12-31) [DISCARD: Already discarded; marriage-table fragments with implausible magnitudes, superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p602 Monthly marriage registrations (same-sex couples), December, Taiwan (ROC year 11 = **4** couple (2025-12-01..2025-12-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(相同性別) 0 5 3 1 4 3 2 1 5 5 2 4"
  - p603 Total marriage registrations, December, Taiwan (ROC year 114 table) = **98** couple (2025-12-01..2025-12-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p604 Monthly marriage registrations (different-sex couples), November, Taiwan (ROC ye = **78** couple (2025-11-01..2025-11-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p605 Monthly marriage registrations (different-sex couples), October, Taiwan (ROC yea = **92** couple (2025-10-01..2025-10-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p606 Monthly marriage registrations (different-sex couples), January, Taiwan (ROC yea = **77** couple (2025-01-01..2025-01-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p607 Monthly marriage registrations (different-sex couples), February, Taiwan (ROC ye = **81** couple (2025-02-01..2025-02-28) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p608 Monthly marriage registrations (different-sex couples), March, Taiwan (ROC year  = **96** couple (2025-03-01..2025-03-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p609 Monthly marriage registrations (different-sex couples), April, Taiwan (ROC year  = **64** couple (2025-04-01..2025-04-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p610 Monthly marriage registrations (different-sex couples), May, Taiwan (ROC year 11 = **113** couple (2025-05-01..2025-05-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p611 Monthly marriage registrations (different-sex couples), June, Taiwan (ROC year 1 = **68** couple (2025-06-01..2025-06-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p612 Monthly marriage registrations (different-sex couples), July, Taiwan (ROC year 1 = **81** couple (2025-07-01..2025-07-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p613 Monthly marriage registrations (different-sex couples), August, Taiwan (ROC year = **57** couple (2025-08-01..2025-08-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p614 Monthly marriage registrations (different-sex couples), September, Taiwan (ROC y = **63** couple (2025-09-01..2025-09-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "結婚對數(不同性別) 77 81 96 64 113 68 81 57 63 92 78 94"
  - p615 Total marriage registrations, January, Taiwan (ROC year 114 table) = **77** couple (2025-01-01..2025-01-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p616 Total marriage registrations, February, Taiwan (ROC year 114 table) = **86** couple (2025-02-01..2025-02-28) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p617 Total marriage registrations, March, Taiwan (ROC year 114 table) = **99** couple (2025-03-01..2025-03-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p618 Total marriage registrations, April, Taiwan (ROC year 114 table) = **65** couple (2025-04-01..2025-04-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p619 Total marriage registrations, May, Taiwan (ROC year 114 table) = **117** couple (2025-05-01..2025-05-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p620 Total marriage registrations, June, Taiwan (ROC year 114 table) = **71** couple (2025-06-01..2025-06-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p621 Total marriage registrations, July, Taiwan (ROC year 114 table) = **83** couple (2025-07-01..2025-07-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p622 Total marriage registrations, August, Taiwan (ROC year 114 table) = **58** couple (2025-08-01..2025-08-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p623 Total marriage registrations, September, Taiwan (ROC year 114 table) = **68** couple (2025-09-01..2025-09-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p624 Total marriage registrations, October, Taiwan (ROC year 114 table) = **97** couple (2025-10-01..2025-10-31) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p625 Total marriage registrations, November, Taiwan (ROC year 114 table) = **80** couple (2025-11-01..2025-11-30) [DISCARD: Already discarded; superseded by p539–p550.] quote: "合計 77 86 99 65 117 71 83 58 68 97 80 98"
  - p626 Crude marriage rate, Taiwan (ROC year 114 table) = **4.67** marriages per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Already discarded; marriage-rate fragment inconsistent with p584/p308.] quote: "114年 999 4.67"
  - p627 Crude divorce rate (incl. terminated marriages), Taiwan (ROC year 114 table) = **2.1** divorces per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Already discarded; divorce-rate fragment inconsistent with p311/p273.] quote: "粗離婚率(含終止結婚)(‰) 2.10"
  - p628 Crude birth rate, Taiwan (ROC year 114 table) = **5.25** births per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Already discarded; crude birth rate 5.25 conflicts with the 2025 MOI value 4.62 (p60/p186).] quote: "出生人數 男 女 總計 583 539 1122 5.25"
  - p629 Crude death rate, Taiwan (ROC year 114 table) = **7.76** deaths per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Already discarded; crude death rate 7.76 conflicts with the 2025 MOI value 8.58 (p298/p357).] quote: "死亡人數 男 女 總計 897 761 1658 7.76"
- `https://www.moi.gov.tw./News_Content.aspx?n=9&sms=9009&s=339254` -> **snapshot** (snapshot 20260817180449); points raw/verified 0/0
- `https://ah.lib.nccu.edu.tw/item?item_id=35927&locale=en` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thesis.lib.nccu.edu.tw/thesis/detail/d6c6f7c6f609254a8c81514e8968a941/?seq=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://online.senao.com.tw/Article/detail/1745?content=4067` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yunlin.join.gov.tw/attachments/60732306-93d5-4dad-9561-d07297e338c8/download/%e8%bf%9110%e5%b9%b4%e5%87%ba%e7%94%9f%e6%95%b8%e5%8f%8a%e7%b5%90` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] MOI monthly registered births, August 2026

Hypothesis: The August 2026 monthly birth figure (published ~early September 2026) is the single most valuable missing input: it would extend the 2026 monthly series to 8 months and let series_auto / partial_period use a much more recent level, materially tightening the September 2026 forecast. Currently the latest observed month is July 2026 (p118/p143/p316).

Queries issued by the searcher: site:ris.gov.tw 115年8月 出生 戶籍統計; 內政部 戶政司 115年8月 出生人數; 內政部 115年7月 戶口統計 出生數 新生兒 7月2026; 114年9月 出生數 內政部 戶口統計 新生兒 2025年9月; 內政部 戶政司 115年8月 出生人數 統計; site:ris.gov.tw 115年8月 出生 戶籍統計; ris.gov.tw 戶口統計資料分析 115年8月 出生數 7492; 114年9月 出生數 內政部 戶口統計 新生兒; 內政部 戶政司 115年8月 出生人數 戶籍統計; site:ris.gov.tw 115年8月 出生 統計; ris.gov.tw 戶口統計資料分析 115年8月 新聞稿; 114年9月 出生數 內政部 戶口統計 新生兒 2025年9月

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])7492(?!\\d|[.,]\\d)']; no pages fetched**


### b2 [own_history] September seasonal factor for registered births

Hypothesis: The September seasonal adjustment divisor (analogous to p67–p69 for Oct/Nov/Dec) is not directly published in the kept data; only the September 2025 unadjusted and seasonally adjusted rates (p62/p63) allow an inference. A direct September divisor or a multi-year September/adjacent-month ratio would let the seasonal factor be applied with less uncertainty, which is the largest single modelling assumption in the trend-plus-seasonality route.

Queries issued by the searcher: 內政部 戶政司 粗出生率 季節調整 調整係數 9月; Taiwan registered births September 2023 2024 monthly household registration statistics; "人口統計季刊" 出生 "季節調整" 調整係數 表; ris.gov.tw 出生 月 統計 9月 113年9月 出生數; 內政部 戶政司 戶籍統計 粗出生率 季節調整 調整係數; Taiwan registered births September 2023 2024 monthly household registration statistics; 中華民國人口統計季刊 季節調整 調整係數 出生率 表 ris.gov.tw DemographicQuarterly Autumn 2025; ris.gov.tw DemographicQuarterly_Autumn2024.pdf seasonally adjusted birth rate September; 內政部 戶政司 粗出生率 季節調整 調整係數 9月; Taiwan registered births September 2023 2024 monthly statistics; ris.gov.tw 人口統計季刊 113年 第3季 出生 季節調整 表10; "Sep 2025" OR "September 2025" Taiwan births 8,603 MOI household registration

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2023.pdf` -> **snapshot** (snapshot 20251104063418); points raw/verified 28/28
  - p630 Registered births, Taiwan area, September 2023 (Table 11) = **10,717** births (2023-09-01..2023-09-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p631 Registered births, Taiwan area, August 2023 (Table 11) = **12,016** births (2023-08-01..2023-08-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p632 Registered births, Taiwan area, October 2023 (Table 11) = **13,068** births (2023-10-01..2023-10-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p633 Registered births, Taiwan area, November 2023 (Table 11) = **11,272** births (2023-11-01..2023-11-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p634 Registered births, Taiwan area, December 2023 (Table 11) = **11,579** births (2023-12-01..2023-12-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p635 Registered births, Taiwan area, July 2023 (Table 11) = **10,891** births (2023-07-01..2023-07-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p636 Registered births, Taiwan area, June 2023 (Table 11) = **11,009** births (2023-06-01..2023-06-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p637 Registered births, Taiwan area, May 2023 (Table 11) = **11,809** births (2023-05-01..2023-05-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p638 Registered births, Taiwan area, January 2023 (Table 11) = **10,948** births (2023-01-01..2023-01-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p639 Registered births, Taiwan area, February 2023 (Table 11) = **10,113** births (2023-02-01..2023-02-28) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p640 Registered births, Taiwan area, March 2023 (Table 11) = **12,506** births (2023-03-01..2023-03-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p641 Registered births, Taiwan area, April 2023 (Table 11) = **9,643** births (2023-04-01..2023-04-30) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p642 Total registered births, Taiwan area, 2023 (Table 11 total) = **135,571** births (2023-01-01..2023-12-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p643 Total registered births, Taiwan area, 2022 (Table 1) = **138,986** births (2022-01-01..2022-12-31) [keep: ] quote: "2022 (1) 138,986 207,230 -68,244 5.96 8.89 -2.93"
  - p644 Unadjusted crude birth rate, Taiwan area, September 2023 (Table 12) = **5.57** births per 1,000 population (2023-09-01..2023-09-30) [keep: ] quote: "5.54 5.66 6.31 5.03 5.95 5.73 5.48 6.05 5.57 6.57"
  - p645 Seasonally adjusted crude birth rate, Taiwan area, September 2023 (Table 13) = **5.64** births per 1,000 population (2023-09-01..2023-09-30) [keep: ] quote: "5.62 6.13 6.00 5.53 6.15 6.02 5.73 6.26 5.64 5.99"
  - p646 Seasonally adjusted crude birth rate, Taiwan area, October 2023 (Table 13) = **5.99** births per 1,000 population (2023-10-01..2023-10-31) [keep: ] quote: "5.62 6.13 6.00 5.53 6.15 6.02 5.73 6.26 5.64 5.99"
  - p647 Seasonally adjusted crude birth rate, Taiwan area, November 2023 (Table 13) = **5.5** births per 1,000 population (2023-11-01..2023-11-30) [keep: ] quote: "5.50 5.12 - 0.34 0.17 0.04 - 0.43 0.19 0.06 - 0.23 0.30 - 0.32 0.03 - 0.46 - 0.84"
  - p648 Seasonally adjusted crude birth rate, Taiwan area, December 2023 (Table 13) = **5.12** births per 1,000 population (2023-12-01..2023-12-31) [keep: ] quote: "5.50 5.12 - 0.34 0.17 0.04 - 0.43 0.19 0.06 - 0.23 0.30 - 0.32 0.03 - 0.46 - 0.84"
  - p649 Seasonal adjustment coefficient △ for crude birth rate, October 2023 (Table 3 no = **1.097** 1 (2023-10-01..2023-10-31) [keep: ] quote: "本月份粗出生率調整係數△為1.097"
  - p650 Seasonal adjustment coefficient △ for crude birth rate, November 2023 (Table 3 n = **1.066** 1 (2023-11-01..2023-11-30) [keep: ] quote: "本月份粗出生率調整係數△為1.066"
  - p651 Seasonal adjustment coefficient △ for crude birth rate, December 2023 (Table 3 n = **1.137** 1 (2023-12-01..2023-12-31) [keep: ] quote: "本月份粗出生率調整係數△為1.137"
  - p652 Seasonal adjustment coefficient △ for crude death rate, October 2023 (Table 4 no = **0.963** 1 (2023-10-01..2023-10-31) [keep: ] quote: "本月份粗死亡率調整係數△為0.963"
  - p653 Seasonal adjustment coefficient △ for crude death rate, November 2023 (Table 4 n = **0.942** 1 (2023-11-01..2023-11-30) [keep: ] quote: "本月份粗死亡率調整係數△為0.942"
  - p654 Seasonal adjustment coefficient △ for crude death rate, December 2023 (Table 4 n = **0.994** 1 (2023-12-01..2023-12-31) [keep: ] quote: "本月份粗死亡率調整係數△為0.994"
  - p655 Seasonal adjustment coefficient △ for crude marriage rate, October 2023 (Table 5 = **1.133** 1 (2023-10-01..2023-10-31) [keep: ] quote: "本月份粗結婚率調整係數△為1.133"
  - p656 Seasonal adjustment coefficient △ for crude marriage rate, November 2023 (Table  = **1.113** 1 (2023-11-01..2023-11-30) [keep: ] quote: "本月份粗結婚率調整係數△為1.113"
  - p657 Seasonal adjustment coefficient △ for crude marriage rate, December 2023 (Table  = **1.308** 1 (2023-12-01..2023-12-31) [keep: ] quote: "本月份粗結婚率調整係數△為1.308"
- `https://stats.tw/population/births-deaths` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Autumn2023.pdf` -> **snapshot** (snapshot 20240720141408); points raw/verified 29/29
  - p658 September 2023 seasonal adjustment coefficient (△) for crude birth rate, Taiwan = **0.987** 1 (2023-09-01..2023-09-30) [keep: ] quote: "本月份粗出生率調整係數△為0.987"
  - p659 July 2023 seasonal adjustment coefficient (△) for crude birth rate, Taiwan = **0.957** 1 (2023-07-01..2023-07-31) [keep: ] quote: "本月份粗出生率調整係數△為0.957"
  - p660 August 2023 seasonal adjustment coefficient (△) for crude birth rate, Taiwan = **0.967** 1 (2023-08-01..2023-08-31) [keep: ] quote: "本月份粗出生率調整係數△為0.967"
  - p661 Registered births, Taiwan total, September 2023 = **10,717** birth (2023-09-01..2023-09-30) [keep: ] quote: "10,717 5.57 0.84 - 5.64 0.32 - 5.71 0.16 -"
  - p662 Registered births, Taiwan total, August 2023 = **12,016** birth (2023-08-01..2023-08-31) [keep: ] quote: "12,016 6.05 0.01 6.26 0.30 5.73 0.08 -"
  - p663 Registered births, Taiwan total, July 2023 = **10,891** birth (2023-07-01..2023-07-31) [keep: ] quote: "23,392,423 11,548,206 11,844,217 10,891 17,992 - 7,101 - 3.58"
  - p664 Cumulative registered births, Taiwan total, July-September 2023 = **33,624** birth (2023-07-01..2023-09-30) [keep: ] quote: "計 33,624 32,220 556 847 1 49,741 27,191 26,414 777 13,789 13,578 211"
  - p665 Unadjusted birth rate, Taiwan total, September 2023 = **5.57** birth/(1000 person*year) (2023-09-01..2023-09-30) [keep: ] quote: "10,717 5.57 0.84 - 5.64 0.32 - 5.71 0.16 -"
  - p666 Seasonally adjusted birth rate, Taiwan total, September 2023 = **5.64** birth/(1000 person*year) (2023-09-01..2023-09-30) [keep: ] quote: "10,717 5.57 0.84 - 5.64 0.32 - 5.71 0.16 -"
  - p667 Unadjusted birth rate, Taiwan total, August 2023 = **6.05** birth/(1000 person*year) (2023-08-01..2023-08-31) [keep: ] quote: "12,016 6.05 0.01 6.26 0.30 5.73 0.08 -"
  - p668 Seasonally adjusted birth rate, Taiwan total, August 2023 = **6.26** birth/(1000 person*year) (2023-08-01..2023-08-31) [keep: ] quote: "12,016 6.05 0.01 6.26 0.30 5.73 0.08 -"
  - p669 Unadjusted birth rate, Taiwan total, July 2023 = **5.48** birth/(1000 person*year) (2023-07-01..2023-07-31) [keep: ] quote: "10,891 5.48 0.08 - 5.73 0.23 - 5.68 0.10 -"
  - p670 Seasonally adjusted birth rate, Taiwan total, July 2023 = **5.73** birth/(1000 person*year) (2023-07-01..2023-07-31) [keep: ] quote: "10,891 5.48 0.08 - 5.73 0.23 - 5.68 0.10 -"
  - p671 Cumulative birth rate Jan-Sep 2023, Taiwan total = **5.71** birth/(1000 person*year) (2023-01-01..2023-09-30) [keep: ] quote: "10,717 5.57 0.84 - 5.64 0.32 - 5.71 0.16 -"
  - p672 Live births, Taiwan total, 2022 (by date of occurrence) = **137,413** birth (2022-01-01..2022-12-31) [keep: ] quote: "總計 Grand Total 137,413 301 5,815 23,469 44,368 39,273 18,306 4,465 1,030 386"
  - p673 Live births, Taiwan total, 2022, registered within 15 days of birth = **76,556** birth (2022-01-01..2022-12-31) [keep: ] quote: "137,413 76,556 34,168 26,084 565 7 2"
  - p674 Live births, Taiwan total, 2022, registered 15 days to under 1 month after birth = **34,168** birth (2022-01-01..2022-12-31) [keep: ] quote: "137,413 76,556 34,168 26,084 565 7 2"
  - p675 Live births, Taiwan total, 2022, registered 1 to under 2 months after birth = **26,084** birth (2022-01-01..2022-12-31) [keep: ] quote: "137,413 76,556 34,168 26,084 565 7 2"
  - p676 Share of 2022 live births registered within 15 days of birth, Taiwan total = **55.71** % (2022-01-01..2022-12-31) [keep: ] quote: "5 26 100.00 55.71 24.87 18.98 0.41 0.01 0.00 0.00 0.02"
  - p677 Share of 2022 live births registered 15 days to under 1 month after birth, Taiwa = **24.87** % (2022-01-01..2022-12-31) [keep: ] quote: "5 26 100.00 55.71 24.87 18.98 0.41 0.01 0.00 0.00 0.02"
  - p678 Share of 2022 live births registered 1 to under 2 months after birth, Taiwan tot = **18.98** % (2022-01-01..2022-12-31) [keep: ] quote: "5 26 100.00 55.71 24.87 18.98 0.41 0.01 0.00 0.00 0.02"
  - p679 Registered deaths, Taiwan total, September 2023 = **14,610** death (2023-09-01..2023-09-30) [keep: ] quote: "14,610 7.60 1.06 - 8.14 0.75 - 9.00 0.12"
  - p680 September 2023 seasonal adjustment coefficient (△) for crude death rate, Taiwan = **0.934** 1 (2023-09-01..2023-09-30) [keep: ] quote: "本月份粗死亡率調整係數△為0.934"
  - p681 Total population, Taiwan, end of September 2023 = **23,404,300** person (2023-09-30..2023-09-30) [keep: ] quote: "23,404,300 11,550,801 11,853,499 10,717 14,610 - 3,893 - 2.02"
  - p682 Total population, Taiwan, end of August 2023 = **23,399,654** person (2023-08-31..2023-08-31) [keep: ] quote: "23,399,654 11,550,127 11,849,527 12,016 17,139 5,123 - - 2.58"
  - p683 Total population, Taiwan, end of July 2023 = **23,392,423** person (2023-07-31..2023-07-31) [keep: ] quote: "23,392,423 11,548,206 11,844,217 10,891 17,992 - 7,101 - 3.58"
  - p684 Registered births, New Taipei City, September 2023 = **1,397** birth (2023-09-01..2023-09-30) [keep: ] quote: "1,397 4.21 1.50 - 4.27 1.12 - 4.64 0.67 -"
  - p685 Registered births, Taipei City, September 2023 = **1,305** birth (2023-09-01..2023-09-30) [keep: ] quote: "1,305 6.33 0.13 6.41 0.60 6.15 0.35"
  - p686 Registered births, Kaohsiung City, September 2023 = **1,276** birth (2023-09-01..2023-09-30) [keep: ] quote: "1,276 5.67 1.00 - 5.74 0.16 - 5.60 0.20 -"
- `https://tools.vege.club/population/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2024.pdf` -> **snapshot** (snapshot 20251104072937) **LEAK SENTINEL HIT ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)', '(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMTQ3OC9lMzI2MmFmNS0zNjM4LTRiNmYtYjA0MS1lZjYzMDA0YThkZGQucGRm&n=MTEzMTIucGRm&` -> **snapshot** (snapshot 20250424204054); points raw/verified 25/23
  - p687 Registered live births in Taiwan, September 2024 (monthly, all births) = **11,169** births (2024-09-01..2024-09-30) [keep: ] quote: "11,169"
  - p688 Registered live births in Taiwan, September 2023 (monthly, all births) = **11,322** births (2023-09-01..2023-09-30) [DISCARD: September 2023 = 11,322 conflicts with the Table 11 / monthly-bulletin value 10,717 (p630/p661); mixing vintages would c] quote: "11,322"
  - p689 Registered live births in Taiwan, September 2022 (monthly, all births) = **11,596** births (2022-09-01..2022-09-30) [keep: ] quote: "11,596"
  - p690 Registered live births in Taiwan, September 2021 (monthly, all births) = **12,077** births (2021-09-01..2021-09-30) [keep: ] quote: "12,077"
  - p691 Registered live births in Taiwan, September 2020 (monthly, all births) = **11,957** births (2020-09-01..2020-09-30) [keep: ] quote: "11,957"
  - p692 Registered live births in Taiwan, August 2024 (monthly, all births) = **11,792** births (2024-08-01..2024-08-31) [keep: ] quote: "11,792"
  - p693 Registered live births in Taiwan, October 2024 (monthly, all births) = **12,070** births (2024-10-01..2024-10-31) [keep: ] quote: "12,070"
  - p694 Registered live births in Taiwan, November 2024 (monthly, all births) = **12,557** births (2024-11-01..2024-11-30) [keep: ] quote: "12,557"
  - p695 Registered live births in Taiwan, January 2024 (monthly, all births) = **11,023** births (2024-01-01..2024-01-31) [keep: ] quote: "11,023"
  - p696 Registered live births in Taiwan, February 2024 (monthly, all births) = **9,663** births (2024-02-01..2024-02-29) [keep: ] quote: "9,663"
  - p697 Registered live births in Taiwan, March 2024 (monthly, all births) = **10,827** births (2024-03-01..2024-03-31) [keep: ] quote: "10,827"
  - p698 Registered live births in Taiwan, April 2024 (monthly, all births) = **10,753** births (2024-04-01..2024-04-30) [keep: ] quote: "10,753"
  - p699 Registered live births in Taiwan, May 2024 (monthly, all births) = **11,168** births (2024-05-01..2024-05-31) [keep: ] quote: "11,168"
  - p700 Registered live births in Taiwan, June 2024 (monthly, all births) = **10,440** births (2024-06-01..2024-06-30) [keep: ] quote: "10,440"
  - p701 Registered live births in Taiwan, July 2024 (monthly, all births) = **10,424** births (2024-07-01..2024-07-31) [keep: ] quote: "10,424"
  - p702 Registered live births in Taiwan, full year 2024 (annual total) = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "134,856"
  - p703 Registered live births in Taiwan, full year 2023 (annual total) = **135,571** births (2023-01-01..2023-12-31) [keep: ] quote: "135,571"
  - p704 Registered live births in Taiwan, full year 2022 (annual total) = **138,986** births (2022-01-01..2022-12-31) [keep: ] quote: "138,986"
  - p705 Registered live births in Taiwan, full year 2021 (annual total) = **153,820** births (2021-01-01..2021-12-31) [keep: ] quote: "153,820"
  - p706 Crude birth rate, Taiwan, September 2024 (births per 1,000 population) = **0.5** births per 1,000 population (2024-09-01..2024-09-30) [keep: ] quote: "0.50"
  - p707 Crude birth rate, Taiwan, September 2023 (births per 1,000 population) = **0.5** births per 1,000 population (2023-09-01..2023-09-30) [keep: ] quote: "0.50"
  - p708 Crude birth rate, Taiwan, December 2024 (births per 1,000 population) = **0.53** births per 1,000 population (2024-12-01..2024-12-31) [keep: ] quote: "月粗出生率為0.53‰"
  - p709 Resident population of Taiwan, end of September 2024 = **23,404,138** persons (2024-09-30..2024-09-30) [keep: ] quote: "23,404,138"
- `https://data.nat.gov.tw/dataset/32970` -> **snapshot** (snapshot 20240303100625); points raw/verified 0/0
- `https://ghdx.healthdata.org/print/486571` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/html/5/2/popudata-quart-pub.html` -> **snapshot** (snapshot 20260902055958); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/data/5/2/150fd4cd-a2d2-4495-9ccf-a8b07e87df2f.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2025.pdf` -> **snapshot** (snapshot 20260219170633) **LEAK SENTINEL HIT ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)', '(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMTM3Ny80NDM5MzZkMS02NzczLTQ1YjktOGNmZC0zNjA2ZjJmNzI3ZDMucGRm&n=MTEzMTEucGRm&` -> **snapshot** (snapshot 20250413112354) **LEAK SENTINEL HIT ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 2)

### b3 [related_series] Registration-timing lag between occurrence and registration

Hypothesis: The target counts births by registration date, not occurrence date. A measured distribution of registration lag (share of births registered in the same month vs later months) would let the occurrence-based conception route (d2/d6) be converted to a registration-month forecast, resolving whether September 2026 registered births should be shifted relative to September 2026 occurrences.

Queries issued by the searcher: 內政部 出生登記 落後 申報 統計 出生發生 月 差異; DGBAS births by occurrence month Taiwan 2025 出生發生數 內政部 出生登記數; 台灣 出生登記 與 出生發生 月 差異 統計; "出生登記" "發生日期" "登記日期" 統計 台灣 表; "逾期申報出生登記" 人數 112年 113年 內政部; site:ris.gov.tw 出生登記 發生 登記 月 統計; "出生發生數" "出生登記數" 2024 台灣; 內政部 出生登記 落後 申報 統計; DGBAS births by occurrence month Taiwan 2025 出生發生數; "按登記日期" "按發生日期" 出生 統計 台灣 比較; 內政部 統計通報 出生登記 與 發生 差異 月份 落後; 內政部 出生登記 落後 申報 統計; DGBAS births by occurrence month Taiwan 2025 出生發生數 內政部 出生登記數 差異; 出生發生數 出生登記數 差異 內政部 統計 2024 2025 比較; "逾期申報" 出生登記 人數 比率 內政部 統計通報

- `https://w3fs.tainan.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMTYvY2tmaWxlL2U5YWIzMzgxLTQxYTktNGUyOS04YTE4LTBiNDI5YzM2YTJmMC5wZGY%3d&n=5oi25pS%2f5rOV6KaP` -> **snapshot** (snapshot 20250414143708); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 29/28
  - p710 Taiwan registered births, September 2025 (month of registration) = **8,603** births (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p711 Taiwan registered births, October 2025 (month of registration) = **9,458** births (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p712 Taiwan registered births, November 2025 (month of registration) = **7,946** births (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p713 Taiwan registered births, December 2025 (month of registration) = **9,027** births (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p714 Taiwan registered births, full year 2025 (month of registration) = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p715 Taiwan registered births, full year 2024 (month of registration) = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p716 Taiwan crude birth rate, 2025 (annual basis) = **4.62** births per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "resulting in a crude birth rate of 4.62 per 1,000 population"
  - p717 Taiwan crude birth rate, 2024 (annual basis) = **5.76** births per 1,000 population (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p718 Taiwan unadjusted crude birth rate, September 2025 (annual basis) = **4.49** births per 1,000 population (2025-09-01..2025-09-30) [keep: ] quote: "4.78 5.80 4.73 4.52 4.25 4.67 4.51 4.27 4.49 4.78"
  - p719 Taiwan unadjusted crude birth rate, October 2025 (annual basis) = **4.78** births per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p720 Taiwan unadjusted crude birth rate, November 2025 (annual basis) = **4.15** births per 1,000 population (2025-11-01..2025-11-30) [keep: ] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p721 Taiwan unadjusted crude birth rate, December 2025 (annual basis) = **4.56** births per 1,000 population (2025-12-01..2025-12-31) [keep: ] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p722 Seasonal adjustment coefficient for crude birth rate, October 2025 = **1.097** 1 (2025-10-01..2025-10-31) [keep: ] quote: "The coefficient △ for this month is 1.097"
  - p723 Seasonal adjustment coefficient for crude birth rate, November 2025 = **1.066** 1 (2025-11-01..2025-11-30) [keep: ] quote: "The coefficient △ for adjusting the CBR for this month is 1.066"
  - p724 Seasonal adjustment coefficient for crude birth rate, December 2025 = **1.137** 1 (2025-12-01..2025-12-31) [keep: ] quote: "The coefficient △ for adjusting the CBR for this month is 1.137"
  - p725 Taiwan seasonally adjusted crude birth rate, September 2025 (annual basis) = **4.55** births per 1,000 population (2025-09-01..2025-09-30) [keep: ] quote: "4.85 6.28 4.50 4.97 4.40 4.91 4.71 4.42 4.55 4.36"
  - p726 Taiwan cumulative crude birth rate January-September 2025 (annual basis) = **4.66** births per 1,000 population (2025-01-01..2025-09-30) [keep: ] quote: "4.78 5.26 5.08 4.94 4.80 4.78 4.74 4.68 4.66 4.67"
  - p727 Taiwan cumulative crude birth rate January-December 2025 (annual basis) = **4.67** births per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "4.78 5.26 5.08 4.94 4.80 4.78 4.74 4.68 4.66 4.67"
  - p728 Taiwan total population at end of September 2025 = **23,317,031** person (2025-09-30..2025-09-30) [keep: ] quote: "23,346,741 23,337,936 23,328,343 23,317,031 23,310,853 23,306,085 23,299,132"
  - p729 Taiwan total population at end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "there were 9,851,532 households with a total population of 23,299,132"
  - p730 Taiwan registered deaths, September 2025 = **15,387** deaths (2025-09-01..2025-09-30) [keep: ] quote: "15,382 16,554 16,846 15,226 15,387 15,908 14,771 17,450"
  - p731 Taiwan registered deaths, October 2025 = **15,908** deaths (2025-10-01..2025-10-31) [keep: ] quote: "15,382 16,554 16,846 15,226 15,387 15,908 14,771 17,450"
  - p732 Taiwan registered deaths, November 2025 = **14,771** deaths (2025-11-01..2025-11-30) [keep: ] quote: "15,382 16,554 16,846 15,226 15,387 15,908 14,771 17,450"
  - p733 Taiwan registered deaths, December 2025 = **17,450** deaths (2025-12-01..2025-12-31) [keep: ] quote: "15,382 16,554 16,846 15,226 15,387 15,908 14,771 17,450"
  - p734 Taiwan registered deaths, full year 2025 = **200,268** deaths (2025-01-01..2025-12-31) [keep: ] quote: "A total of 200,268 deaths were registered during the same period"
  - p735 Taiwan registered deaths, full year 2024 = **202,107** deaths (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p736 Taiwan registered births, January 2025 = **9,495** births (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p737 Taiwan registered births, February 2025 = **10,407** births (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
- `https://twinfo.ncl.edu.tw/tiqry/hypage.cgi?HYPAGE=search/search_res.hpg&dtd_id=1&sysid=00001451` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://twinfo.ncl.edu.tw/tiqry/hypage.cgi?HYPAGE=search/search_res.hpg&dtd_id=1&sysid=00002415` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.dgbas.gov.tw/public/Data/736143147ECWGCXEJ.pdf` -> **snapshot** (snapshot 20220711054708); points raw/verified 28/14
  - p738 Expansion factor for births occurring June 2013 (1 / same-month registration sha = **2.899** 1 (multiplier) (2013-06-01..2013-06-30) [keep: ] quote: "擴大因子註2 1.00190 1.00715 1.11520 2.89855"
  - p739 Expansion factor for births occurring May 2013 (1 / 1-month registration share) = **1.115** 1 (multiplier) (2013-05-01..2013-05-31) [keep: ] quote: "擴大因子註2 1.00190 1.00715 1.11520 2.89855"
  - p740 Births registered in June 2013 (registration-month count) = **13,975** birth (2013-06-01..2013-06-30) [keep: ] quote: "當月登記數 16,888 15,514 16,233 13,975"
  - p741 Births registered in May 2013 (registration-month count) = **16,233** birth (2013-05-01..2013-05-31) [keep: ] quote: "當月登記數 16,888 15,514 16,233 13,975"
  - p742 Births registered in April 2013 (registration-month count) = **15,514** birth (2013-04-01..2013-04-30) [keep: ] quote: "當月登記數 16,888 15,514 16,233 13,975"
  - p743 Births registered in March 2013 (registration-month count) = **16,888** birth (2013-03-01..2013-03-31) [keep: ] quote: "當月登記數 16,888 15,514 16,233 13,975"
  - p744 Estimated actual births occurring June 2013 (expanded estimate) = **13,975** birth (2013-06-01..2013-06-30) [keep: ] quote: "實際出生推估數註3 16,122 15,168 15,302 13,975 註 1"
  - p745 Estimated actual births occurring May 2013 (expanded estimate) = **15,302** birth (2013-05-01..2013-05-31) [keep: ] quote: "實際出生推估數註3 16,122 15,168 15,302 13,975 註 1"
  - p746 Estimated actual births occurring April 2013 (expanded estimate) = **15,168** birth (2013-04-01..2013-04-30) [keep: ] quote: "實際出生推估數註3 16,122 15,168 15,302 13,975 註 1"
  - p747 Estimated actual births occurring March 2013 (expanded estimate) = **16,122** birth (2013-03-01..2013-03-31) [keep: ] quote: "實際出生推估數註3 16,122 15,168 15,302 13,975 註 1"
  - p748 Estimated births occurring June 2013 not yet registered as of end-June 2013 = **9,153** birth (2013-06-01..2013-06-30) [keep: ] quote: "102 年 6 月實際出生、死亡數已登記比率估計僅 34.5%及 69.5%,估計約有 9,153 人及 3,487 人尚未登記"
  - p749 Estimated share of June 2013 births already registered by end-June 2013 = **34.5** % (registered births / births occurring) (2013-06-01..2013-06-30) [keep: ] quote: "102 年 6 月實際出生、死亡數已登記比率估計僅 34.5%及 69.5%"
  - p750 MAPE of birth estimate using same-month plus 1-month delayed registration, Taiwa = **1.74** % (MAPE) (2011-01-01..2013-02-28) [keep: ] quote: "納入當月及延遲登記一個月資料之出生、死亡人數推估之 MAPE 分別為 1.74%、0.40%"
  - p751 Share of population not registered at usual residence, 2010 Census Taiwan = **21** % (persons not registered at usual residence / population) (2010-01-01..2010-12-31) [keep: ] quote: "依據「99 年人口及住宅普查報告」,未設戶籍於常住地者占 21%"
- `https://www.ey.gov.tw/File/AC31F9B96D44C356?A=C` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://twinfo.ncl.edu.tw/tiqry/hypage.cgi?HYPAGE=search/merge_pdf.hpg&sysid=T0834228&jid=00238889&dtd_id=11&type=s&vol=60100000&page=%e6%8f%90%e8%a6%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.chcg.gov.tw/UserFiles/1010096221.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://midwife.org.tw/upfiles/newsfiles/112年出生通報統計年報.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hpa.gov.tw/File/Attach/16584/File_20499.pdf` -> **snapshot** (snapshot 20250901030622); points raw/verified 0/0
- `http://newdoc.nccu.edu.tw/acadbonus/04/10300039/10300039.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www2.census.gov/programs-surveys/decennial/2020/program-management/final-analysis-reports/2020-report-2010-undercount-children-net_census_cove` -> **snapshot** (snapshot 20260820155557); points raw/verified 30/29
  - p752 Ratio of 2010 Census counts to vital statistics births, September 2009 births (U = **95** % (census count / vital statistics births) (2009-09-01..2009-09-30) [keep: ] quote: "2009 Sep 344,000 362,000 18,000 95.0"
  - p753 Vital statistics registered births, September 2009 (US) = **362,000** birth (2009-09-01..2009-09-30) [keep: ] quote: "2009 Sep 344,000 362,000 18,000 95.0"
  - p754 2010 Census count of children by September 2009 month of birth (US) = **344,000** person (2009-09-01..2009-09-30) [keep: ] quote: "2009 Sep 344,000 362,000 18,000 95.0"
  - p755 Ratio of 2010 Census counts to vital statistics births, January 2010 births (US) = **103** % (census count / vital statistics births) (2010-01-01..2010-01-31) [keep: ] quote: "2010 Jan 334,000 323,000 -11,000 103.4"
  - p756 Ratio of 2010 Census counts to vital statistics births, February 2010 births (US = **103** % (census count / vital statistics births) (2010-02-01..2010-02-28) [keep: ] quote: "2010 Feb 310,000 302,000 -8,000 102.6"
  - p757 Ratio of 2010 Census counts to vital statistics births, March 2010 births (US) = **95.3** % (census count / vital statistics births) (2010-03-01..2010-03-31) [keep: ] quote: "2010 Mar 323,000 339,000 16,000 95.3"
  - p758 Ratio of 2010 Census counts to vital statistics births, April 1 2010 births (US) = **96** % (census count / vital statistics births) (2010-04-01..2010-04-01) [keep: ] quote: "2010 Apr1 12,000 12,500 500 96.0"
  - p759 Ratio of 2010 Census counts to vital statistics births, subtotal 2009 births (US = **95** % (census count / vital statistics births) (2009-01-01..2009-12-31) [keep: ] quote: "Subtotal 2009 3,925,000 4,131,000 206,000 95.0"
  - p760 Vital statistics registered births, subtotal 2009 (US) = **4,131,000** birth (2009-01-01..2009-12-31) [keep: ] quote: "Subtotal 2009 3,925,000 4,131,000 206,000 95.0"
  - p761 Ratio of 2010 Census counts to vital statistics births, subtotal 2010 births thr = **100** % (census count / vital statistics births) (2010-01-01..2010-04-01) [keep: ] quote: "Subtotal 2010 979,000 977,000 -2,000 100.2"
  - p762 Ratio of 2010 Census counts to vital statistics births, subtotal age 0 (US) = **96.4** % (census count / vital statistics births) (2009-01-01..2010-04-01) [keep: ] quote: "Subtotal Age 0 3,956,000 4,105,000 149,000 96.4"
  - p763 Vital statistics births, subtotal age 0, January 2009 - April 1 2010 (US) = **4,105,000** birth (2009-01-01..2010-04-01) [keep: ] quote: "Subtotal Age 0 3,956,000 4,105,000 149,000 96.4"
  - p764 Share of 2010 Census records with full age and DoB reported, January 2010 births = **82.9** % (records with full age and DoB reported / census records) (2010-01-01..2010-01-31) [keep: ] quote: "Full age and DoB reported (%) 91.7 92.0 82.9 83.4 82.2"
  - p765 Share of 2010 Census records with full age and DoB reported, November 2009 birth = **91.7** % (records with full age and DoB reported / census records) (2009-11-01..2009-11-30) [keep: ] quote: "Full age and DoB reported (%) 91.7 92.0 82.9 83.4 82.2"
  - p766 Share of 2010 Census records with DoB imputed, January 2010 births (US) = **14.9** % (records with DoB imputed / census records) (2010-01-01..2010-01-31) [keep: ] quote: "DoB imputed (%) 6.1 5.8 14.9 14.5 15.5"
  - p767 Share of 2010 Census records with DoB imputed, November 2009 births (US) = **6.1** % (records with DoB imputed / census records) (2009-11-01..2009-11-30) [keep: ] quote: "DoB imputed (%) 6.1 5.8 14.9 14.5 15.5"
  - p768 Share of 2010 Census records with reported age and year of birth but month and d = **9.6** % (records with month and day imputed / census records) (2010-01-01..2010-01-31) [keep: ] quote: "Reported age and year of birth; month and day of month imputed (%) 0.4 0.4 9.6 9.2 9.8"
  - p769 Share of 2010 Census records with reported age and year of birth but month and d = **0.4** % (records with month and day imputed / census records) (2009-11-01..2009-11-30) [keep: ] quote: "Reported age and year of birth; month and day of month imputed (%) 0.4 0.4 9.6 9.2 9.8"
  - p770 Share of self-response 2010 Census records with reported age and year of birth b = **7.2** % (records with month and day imputed / self-response census (2010-01-01..2010-01-31) [keep: ] quote: "Reported age and year of birth; month and day of month imputed (%) 0.2 0.2 7.2 6.9 7.6"
  - p771 Share of NRFU 2010 Census records with reported age and year of birth but month  = **14.7** % (records with month and day imputed / NRFU census records) (2010-01-01..2010-01-31) [keep: ] quote: "Reported age and year of birth; month and day of month imputed (%) 0.7 0.6 14.7 14.3 14.0"
  - p772 Share of NRFU 2010 Census records with full age and DoB reported, January 2010 b = **67.6** % (records with full age and DoB reported / NRFU census reco (2010-01-01..2010-01-31) [keep: ] quote: "Full age and DoB reported 80.2 80.8 67.6 68.0 68.7"
  - p773 Infant mortality rate around 2010 (US) = **6** infant deaths per 1,000 live births (2010-01-01..2010-12-31) [keep: ] quote: "The infant mortality rate for the years around 2010 was approximately 6 per 1,000 live births (National Center for Health Statistics 2014)."
  - p774 Demographic Analysis estimate of difference between zero-year-old resident popul = **0.3** % (difference / registered births) (2010-01-01..2010-12-31) [keep: ] quote: "differ from the registered births by less than 3 per thousand (0.3 percent)"
  - p775 2010 Census unedited cases with a date of birth after Census Day (US) = **133,543** case (2010-01-01..2010-12-31) [keep: ] quote: "there were 133,543 cases found in the unedited data from the 2010 Census where a date of birth after Census Day was listed"
  - p776 Cases with post-Census-Day DoB ultimately dropped from final 2010 Census count ( = **8,327** case (2010-01-01..2010-12-31) [keep: ] quote: "Of these 133,543 cases, only 8,327 were ultimately dropped from the final Census count"
  - p777 Cases with post-Census-Day DoB edited to a DoB prior to Census Day and kept in f = **125,216** case (2010-01-01..2010-12-31) [keep: ] quote: "the remaining 125,216 were included in the final Census count of the total population and edited to reflect a date of birth prior to Census Day"
  - p778 Share of April vital statistics births used for April 1 2010 estimate (US) = **0.039** % (April 1 share of April births) (2010-04-01..2010-04-01) [keep: ] quote: "Vital Statistics reduced to 0.039 percent of April estimate to account for April 1 only"
  - p779 Ratio of reported to imputed DoB records, 2009 birth year (US, 2010 Census) = **10** reported records per imputed record (2009-01-01..2009-12-31) [keep: ] quote: "For the 2009 birth year, the ratio is over 10 reported records for every imputed record."
  - p780 Ratio of reported to imputed DoB records, 2010 birth year (US, 2010 Census) = **5** reported records per imputed record (2010-01-01..2010-04-01) [keep: ] quote: "For 2010, the ratio falls dramatically to 5 or fewer reported records for every imputed record."
- dropped by code checks: 16 (value_as_written not in quote as a whole number: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 15)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'taiwan birth rate', 'taiwan population']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p5', 'p55', 'p183', 'p226', 'p559'] June 2025 registered births = 8,968 across MOI, CNA, Taiwan News, and RIS; same underlying MOI household-registration measurement, so these are one source, not independent confirmations.
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p50', 'p51', 'p52', 'p53', 'p54', 'p79', 'p80', 'p81', 'p82', 'p83', 'p178', 'p179', 'p180', 'p181', 'p182', 'p201', 'p202', 'p203', 'p204', 'p205', 'p231', 'p232', 'p233', 'p234', 'p235', 'p561', 'p562', 'p563', 'p564'] Jan–Jun 2025 monthly registered births repeated identically across many outlets; all trace to the same MOI release. Use one consistent vintage (RIS p50–p57) for the 2025 monthly series.
- corroborating: ['p46', 'p47', 'p48', 'p49', 'p54', 'p55', 'p56', 'p57', 'p174', 'p175', 'p176', 'p177', 'p182', 'p183', 'p184', 'p185', 'p553', 'p554', 'p555', 'p556', 'p557', 'p558'] May–Dec 2025 monthly registered births from the RIS table; the same numbers appear in multiple rows of the same table. This is the cleanest 2025 monthly series and includes September 2025 = 8,603.
- corroborating: ['p34', 'p89', 'p100'] February 2026 births = 6,523 (record low) from SETN, j-media, RTI; same MOI figure.
- corroborating: ['p87', 'p91', 'p92', 'p93', 'p101', 'p102', 'p41'] January 2026 = 8,723 and Jan–Feb 2026 = 15,246 are internally consistent (8,723 + 6,523 = 15,246); the 2,200 month-on-month drop and 25.2% decline agree with 6,523/8,723.
- corroborating: ['p118', 'p143', 'p316', 'p388', 'p416'] July 2026 births = 7,906 from RTI, PTS, CNA; same MOI release.
- corroborating: ['p144', 'p145', 'p318', 'p319'] May 2026 = 6,832 and June 2026 = 7,324 from PTS; consistent with July 2026 = 7,906 being +582 over June.
- corroborating: ['p120', 'p121', 'p390', 'p391', 'p421', 'p422'] Jan–Jul 2026 cumulative = 54,250, down 10,064 from 64,314 in Jan–Jul 2025; consistent with the monthly figures (sum of Jan–Jul 2026 months ≈ 54,250).
- corroborating: ['p438', 'p439', 'p452', 'p453', 'p454', 'p462'] NDC 2026 annual projection: central 94,000, range 92,000–97,000, below 100,000. This is a forecast, not an observed outcome; useful as an independent level check on the annual total, not as a Septembe
- corroborating: ['p94', 'p95', 'p96'] j-media scenario forecasts for 2026 annual births (94,362 / 89,967 / 85,571) bracket the NDC central estimate; these are scenarios, not observations.
- corroborating: ['p62', 'p63', 'p188', 'p192'] September 2025 unadjusted crude birth rate 4.49 and seasonally adjusted 4.42; the seasonal adjustment factor for September is therefore about 4.49/4.42 ≈ 1.016, i.e. September is slightly above the se
- corroborating: ['p67', 'p68', 'p69'] Published seasonal adjustment divisors for Oct/Nov/Dec 2025 (1.097, 1.066, 1.137) confirm that MOI publishes month-specific seasonal factors; September's factor is not directly given but can be inferr
- corroborating: ['p473', 'p474', 'p475', 'p513', 'p514', 'p515'] Mid-Autumn + Teachers' Day 4-day holiday 25–28 September 2026; two independent calendar sources agree. Relevant to registration-office working days in late September.
- corroborating: ['p484', 'p485', 'p486', 'p488', 'p489', 'p495', 'p496'] Childcare policy package announced 2026-08-27, earliest effective 2027; therefore no material effect on September 2026 births. Useful as a negative control on policy shocks.
- corroborating: ['p539', 'p542', 'p543', 'p544', 'p545', 'p546', 'p547', 'p548', 'p549', 'p550'] 2025 monthly marriage registrations from RIS; December 2025 = 10,816 is the conception-relevant month for September 2026 births (about 9 months earlier).
- conflicting: ['p601', 'p602', 'p603', 'p604', 'p605', 'p606', 'p607', 'p608', 'p609', 'p610', 'p611', 'p612', 'p613', 'p614', 'p615', 'p616', 'p617', 'p618', 'p619', 'p620', 'p621', 'p622', 'p623', 'p624', 'p625'] The Taipei City table (p601–p625) gives marriage counts of order 60–120 per month, which are Taipei City-level, not national; they conflict in magnitude with the national RIS series (p539–p550, thousa
- conflicting: ['p36'] p36 labels 2,648 as 'Deaths in Taiwan, January 2026' but the quote says deaths decreased by 2,648 versus January; it is a change, not a level. Mislabeled.
- conflicting: ['p370'] p370 gives 250,000,000 births as a 'Dragon-year excess' — clearly a unit/parse error (the quote says 2–3萬, i.e. 20,000–30,000). Unusable as stated.
- conflicting: ['p628', 'p629'] The Taipei City table's crude birth rate 5.25 and death rate 7.76 for ROC year 114 are local (Taipei City) figures, not national; they conflict with national 2025 crude birth rate 4.62 (p60/p186).
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p223', 'p224', 'p249', 'p250'] June 2025 population 23,346,741 and month-on-month decline 8,729 appear in both Taiwan News and CNA; same MOI release.
- corroborating: ['p31', 'p99', 'p107', 'p32'] February 2026 population 23,280,273 and month-on-month decline 8,772 from SETN and RTI; same MOI release.
- corroborating: ['p117', 'p142', 'p312', 'p387', 'p412'] July 2026 population 23,235,002 from RTI, PTS, CNA; same MOI release.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p46', 'p174', 'p553', 'p710'] Four independent-looking records of the same MOI/ris.gov.tw September 2025 registered-birth total (8,603); they are the same underlying measurement, so they confirm the value but add no independent in
- corroborating: ['p118', 'p143', 'p316', 'p388', 'p416'] All report July 2026 registered births = 7,906 from the same MOI release; single measurement, multiple outlets.
- corroborating: ['p144', 'p318'] May 2026 = 6,832 in two outlets; same MOI release.
- corroborating: ['p145', 'p319'] June 2026 = 7,324 in two outlets; same MOI release.
- corroborating: ['p120', 'p390', 'p421'] Jan–Jul 2026 cumulative = 54,250; same release, consistent with monthly values (8,723+6,523+...).
- corroborating: ['p34', 'p89', 'p100'] February 2026 = 6,523 record low, three outlets, same MOI release.
- corroborating: ['p87', 'p91', 'p120'] January 2026 = 8,723 and Jan–Feb = 15,246 are internally consistent with Feb = 6,523 and with the Jan–Jul cumulative.
- corroborating: ['p58', 'p74', 'p171', 'p284', 'p343', 'p366', 'p440', 'p461', 'p565', 'p714'] 2025 annual registered births = 107,812 across many outlets; one MOI measurement.
- corroborating: ['p46', 'p57', 'p56', 'p55', 'p54'] The 2025 monthly string (May–Sep) is internally consistent with the 2025 annual total and with the 2025 monthly figures reported elsewhere.
- conflicting: ['p630', 'p661', 'p688'] September 2023 registered births appear as 10,717 (Table 11), 10,717 (monthly bulletin) and 11,322 (ws.moi.gov.tw) — a definitional/vintage discrepancy (Taiwan-area vs total, or revision). Use only on
- conflicting: ['p62', 'p63', 'p188', 'p192', 'p718', 'p725'] September 2025 seasonally adjusted crude birth rate is 4.42 in one table and 4.55 in another; the unadjusted 4.49 is consistent. The implied September seasonal divisor is therefore ~1.016 or ~0.987 — 
- corroborating: ['p658', 'p659', 'p660'] 2023 monthly seasonal divisors (Jul 0.957, Aug 0.967, Sep 0.987) show September is close to neutral-to-slightly-negative seasonally, supporting a September factor near 1.0 rather than a large uplift.
- corroborating: ['p438', 'p439', 'p452', 'p453', 'p454', 'p462'] NDC 2026 central projection 94,000 (range 92,000–97,000) is an independent official forecast consistent with the observed Jan–Jul run-rate; it constrains the annual level, not the September month dire
- corroborating: ['p94', 'p95', 'p96'] Media scenario forecasts (85,571–94,362) bracket the NDC range; they are scenarios, not observations, and should not be used as central estimates.
- corroborating: ['p687', 'p688', 'p689', 'p690', 'p691'] September registered births 2020–2024 (11,957; 12,077; 11,596; 11,322; 11,169) form a declining September series; combined with 2025 = 8,603 they show a steep recent drop, so a simple multi-year Septe
- corroborating: ['p673', 'p676', 'p677', 'p678', 'p749'] Registration-lag evidence: ~56% of 2022 births registered within 15 days, ~25% at 15 days–1 month, ~19% at 1–2 months; June 2013 same-month registration share only 34.5%. This means a September regist
- corroborating: ['p473', 'p474', 'p475', 'p513', 'p514', 'p515'] Mid-Autumn/Teachers' Day 4-day holiday 25–28 September 2026 confirmed by two sources; registration offices closed on those days, a minor downward shift in registrations within the month (mostly recove
- corroborating: ['p484', 'p485', 'p486', 'p488', 'p489'] Childcare package announced 2026-08-27 but earliest effective 2027, so no September 2026 birth effect; relevant only as a reason not to expect an uptick.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 seasonal factor relative to the 2026 May–July average monthly level | 1 | 0.93..1.08 | 0.7087..1.417 (widened) | 1 | m1 (m1) | 2023 divisors put September near neutral (0.987) and the 2025 unadjusted/SA September rates imply a divisor of roughly 0.99–1.02; September is not a strong seasonal month in Taiwan. A factor centred at 1.0 with a ±7–8% band reflects the small and uncertain seasonal signal plus the 4-day late-Septemb | The May–July 2026 average is a fair proxy for the underlying late-2026 monthly level and no large registration-timing shift occurs. | A published September seasonal divisor far from 1.0, or evidence that the 2026 holiday closure shifted a large share of registrations into October. |
| a2 | Year-on-year change factor for September 2026 vs September 2025 registered births | 0.88 | 0.78..0.98 | 0.78..0.98 | 1 | m2 (m2) | Jan–Jul 2026 births are 54,250 vs 64,314 a year earlier (−15.6%, p121/p422); July alone was −11.6% (p147/p321). The decline has been moderating through spring–summer (May 6,832, June 7,324, July 7,906), so a September YoY factor somewhat milder than the year-to-date −15.6% but still clearly negative | The moderating month-on-month recovery seen in May–July 2026 continues into September rather than reversing. | An August 2026 figure showing a renewed steep drop (e.g. below ~7,000) or a sharp rebound above ~8,500. |
| a3 | Ratio of September 2026 registered births to the 2026 Jan–Jul monthly average | 1.02 | 0.92..1.12 | 0.7178..1.436 (widened) | 1 | unused | In 2025 September (8,603) was 0.96 of the Jan–Jul 2025 monthly average (9,188); in 2024 September (11,169) was about 1.0 of the Jan–Jul average. September is close to the annual mean, so a ratio near 1 with a modest band is justified; the slight upward tilt reflects the May–July 2026 recovery. | The within-year seasonal shape of 2026 resembles 2024–2025 and the Jan–Jul average is a valid base level. | Evidence of a strong September-specific registration surge or slump in 2026. |
| a4 | Number of months in the January–July 2026 cumulative window | 7 | 7..7 | 4.95..9.899 (widened) | month | unused | Calendar constant: the Jan–Jul cumulative (p421) spans exactly seven months, so dividing by it gives the monthly average. Fixed, not uncertain. | Used only to convert the Jan–Jul cumulative to a monthly average. | Nothing; it is a calendar fact. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,428 | ['p144', 'p145', 'p118'] / ['a1'] | [] |  | 0.50 | B1 of 2 blocks; geometric mean of blocks |  |
| m2 | formula_mc | 7,536 | ['p46'] / ['a2'] | [] |  | 0.50 | B2 of 2 blocks; geometric mean of blocks |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: mean(p144, p145, p118) * a1; Monte Carlo P10 to P90 5,170 to 10,686; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.44 (Monte Carlo of the formula inputs)
- m2 formula_mc: p46 * a2; Monte Carlo P10 to P90 6,097 to 9,359; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,428 (width x/÷1.44, Monte Carlo of the formula inputs); B2 = m2: 7,536 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.41; Birge ratio 0.04 (not above one, so no widening); final width x/÷1.41.

Result: central **7,482** birth, 80% interval [5,313, 10,537] birth, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_geometric_mean, weight on methods that use assumptions 1.00

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for live births registered in Taiwan during September 2026 (MOI monthly household registration statistics) is 7,482 birth (80% model-based interval 5,313 to 10,537 birth).

Two routes were combined with equal weight. The level-plus-seasonality route (7,428 birth, weight 50%) averages the observed May–July 2026 months (6,832 birth, 7,324 birth, 7,906 birth) and applies a near-neutral September seasonal factor (1, range 0.7087 to 1.417). The year-on-year route (7,536 birth, weight 50%) scales observed September 2025 births (8,603 birth) by a decline factor (0.88, range 0.78 to 0.98).

Observed: the four monthly points. Assumed: both factors, which carry the main uncertainty. The interval is conditional on these assumptions, not a demonstrated accuracy guarantee.

Main risk: the 2026 decline could re-steepen, or the 2025 September base could be distorted by registration timing. Better evidence would be August 2026 registrations and any partial September data.

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 seasonal factor relative to the 2026 May–July average monthly level: 1 [n], range 0.7087 to 1.417 (range widened by code); used by m1. Overturned by: A published September seasonal divisor far from [n], or evidence that the 2026 holiday closure shifted a large share of registrations into October.
- a2 Year-on-year change factor for September 2026 vs September 2025 registered births: 0.88 [n], range 0.78 to 0.98; used by m2. Overturned by: An August 2026 figure showing a renewed steep drop (e.g. below ~[n]) or a sharp rebound above ~[n].

Method details (computed by code):
- m1 formula_mc: mean(p144, p145, p118) * a1; Monte Carlo P10 to P90 5,170 to 10,686; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.44 (Monte Carlo of the formula inputs)
- m2 formula_mc: p46 * a2; Monte Carlo P10 to P90 6,097 to 9,359; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 2 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,428 (width x/÷1.44, Monte Carlo of the formula inputs); B2 = m2: 7,536 (width x/÷1.38, no error evidence, code's default width). Estimate = the geometric mean of the two blocks.
- Interval: root mean square of the block widths x/÷1.41; Birge ratio 0.04 (not above one, so no widening); final width x/÷1.41.

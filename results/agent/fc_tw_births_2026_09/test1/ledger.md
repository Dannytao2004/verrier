# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan during September 2026, as reported in the Ministry of the Interior's monthly household registration statistics (戶籍登記出生人數). This counts birth events registered with household registration offices, not all births occurring in the month; registration timing ma | unit births (persons) | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior, Department of Household Registration, Taiwan (內政部戶政司)

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] Historical monthly birth registration data from Taiwan's Ministry of the Interior.

Hypothesis: September 2026 births can be estimated by applying seasonal factors and recent trends to the same month in previous years. The target is a monthly flow, so year-over-year and month-over-month patterns are informative.

Queries issued by the searcher: Taiwan Ministry of Interior monthly birth statistics 2026 出生人數 統計; 內政部戶政司 戶籍登記出生人數 月報 統計; 內政部戶政司 人口統計資料 出生數 按年月 民國115年 ris.gov.tw; 台灣 2025年9月 出生數 8603 新生兒 內政部

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2026.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://news.pts.org.tw/tag/13920?page=1&type=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20260610002909-260407` -> **snapshot** (snapshot 20260622115614); points raw/verified 15/9
  - p1 Taiwan registered live births in May 2026 (民國115年5月) = **6,832** births (persons) (2026-05-01..2026-05-31) [keep: ] quote: "5月新生兒數為6832人,比4月新生兒8144人少了1312人"
  - p2 Taiwan registered live births in April 2026 = **8,144** births (persons) (2026-04-01..2026-04-30) [keep: ] quote: "5月新生兒數為6832人,比4月新生兒8144人少了1312人"
  - p3 Taiwan registered live births in February 2026 (lowest single month of the year) = **6,523** births (persons) (2026-02-01..2026-02-28) [keep: ] quote: "僅次於今年2月單月新生兒最低數6523人,創歷年次低"
  - p4 Year-over-year change in Taiwan registered live births, May 2026 vs May 2025 = **1,601** births (persons) decrease (2026-05-01..2026-05-31) [DISCARD: May 2026 y/y decline 1,601; derived from p1 and p18, not an independent input.] quote: "較上年同月減少1,601人,較上月減少1312人"
  - p5 Month-over-month change in Taiwan registered live births, May 2026 vs April 2026 = **1,312** births (persons) decrease (2026-05-01..2026-05-31) [DISCARD: May 2026 m/m decline 1,312; derived from p1 and p2, not an independent input.] quote: "較上年同月減少1,601人,較上月減少1312人"
  - p6 Annual crude birth rate for Taiwan, May 2026 (annualised) = **3.46** per thousand (crude birth rate) (2026-05-01..2026-05-31) [DISCARD: Derived presentation of p1 (May 2026 crude birth rate); adds no independent information.] quote: "115年5月出生數為6832人,約每6.5分鐘出生一個嬰兒,折合年粗出生率為千分之3.46"
  - p7 Average interval between births in Taiwan, May 2026 = **6.5** minutes per birth (2026-05-01..2026-05-31) [DISCARD: Derived presentation of p1 (minutes per birth); adds no independent information.] quote: "115年5月出生數為6832人,約每6.5分鐘出生一個嬰兒"
  - p8 Average daily population decrease in Taiwan, May 2026 = **282** persons per day (2026-05-01..2026-05-31) [DISCARD: Population-change context, not a birth input; redundant with p9.] quote: "與上年同月比較減少10萬2829人,平均每天減少281.72人"
  - p9 Month-over-month change in Taiwan total population, May 2026 vs April 2026 = **9,903** persons decrease (2026-05-01..2026-05-31) [DISCARD: Population-change context, not a birth input.] quote: "與上月比較則減少9903人"
- dropped by code checks: 6 (number: more than one number in value_as_written: 6)

### d2 [related_series] Marriage registrations and first-birth order statistics as leading indicators.

Hypothesis: Births are strongly linked to marriage registrations, especially first births, with a lag of roughly 9–12 months. September 2026 births may be partially predicted by marriage registrations in late 2025 and early 2026, and by the share of first births.

Queries issued by the searcher: Taiwan marriage registrations monthly statistics 2025 內政部 結婚登記 統計; 內政部戶政司 統計通報 出生人數 結婚對數 月; 台灣 2026年 1月 2月 3月 4月 5月 結婚對數 出生人數 戶口統計; 內政部 出生 第一胎 第二胎 胎次統計 生母平均年齡 第一胎

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMjY3OC9mYjFhNDNlNC0yNTQ0LTQ0NjctYWRjYi1iNDhlYWQ2ZGRkNDAucGRm&n=MTE0MDgucGRm&` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://life.tw/article/%e5%8f%b0%e7%81%a3%e4%ba%ba%e5%8f%a3-%e6%ba%9c%e6%bb%91%e6%a2%af-%e9%80%a329%e5%80%8b%e6%9c%88%e8%b2%a0%e6%88%90%e9%95%b7-5%e6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yunlin.join.gov.tw/attachments/60732306-93d5-4dad-9561-d07297e338c8/download/%e8%bf%9110%e5%b9%b4%e5%87%ba%e7%94%9f%e6%95%b8%e5%8f%8a%e7%b5%90` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d3 [base_rates] Seasonal patterns of births in Taiwan by month.

Hypothesis: Births exhibit seasonality; September may have a typical share of annual births. Using the average September share from recent years and an estimate of 2026 annual births can yield a monthly estimate.

Queries issued by the searcher: Taiwan monthly births by month 2020 2021 2022 2023 2024 2025 statistics 出生人數 月別; 內政部戶政司 戶籍登記出生人數 統計 月別 2025; 內政部戶政司 現住人口動態登記 按月別分 出生數 表4; 台灣 2026年 6月 出生人數 新生兒 內政部 戶口統計; 台灣 歷年 各月 出生人數 統計表 2020 2021 2022 2023 2024 每月; Taiwan 2026 births projection 90,000 國發會 人口推估 2026

- `https://j-media.tw/Article/Detail/37299` -> **snapshot** (snapshot 20260417185829); points raw/verified 15/15
  - p10 Taiwan annual live births in 2016 = **208,440** births (persons) (2016-01-01..2016-12-31) [DISCARD: 2016 annual births; too distant to inform a 2026 monthly level beyond the trend already captured by 2024–2026 data.] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p11 Taiwan annual live births in 2025 = **107,812** births (persons) (2025-01-01..2025-12-31) [keep: ] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p12 Taiwan annual live births in 2024 (Dragon Year) = **134,856** births (persons) (2024-01-01..2024-12-31) [keep: ] quote: "2024年受到「龍年效應」支撐,全年出生134,856人,年減僅0.5%,讓人誤以為少子化已觸底。"
  - p13 Taiwan year-on-year change in annual births, 2025 = **20.1** percent (2025-01-01..2025-12-31) [DISCARD: 2025 y/y decline 20.1%; derived from p11 and p12, not an independent input.] quote: "卻在2025年出生跌至107,812人,年減幅達20.1%,創下史上最大單年跌幅。"
  - p14 Taiwan live births, January 2025 = **9,495** births (persons) (2025-01-01..2025-01-31) [keep: ] quote: "2025年1月出生9,495人,2月受農曆年效應拉抬至10,407人,形成全年唯一高點"
  - p15 Taiwan live births, February 2025 = **10,407** births (persons) (2025-02-01..2025-02-28) [keep: ] quote: "2025年1月出生9,495人,2月受農曆年效應拉抬至10,407人,形成全年唯一高點"
  - p16 Taiwan live births, March 2025 = **9,388** births (persons) (2025-03-01..2025-03-31) [keep: ] quote: "但隨後便一路走低:3月9,388人、4月8,684人、5月8,433人。"
  - p17 Taiwan live births, April 2025 = **8,684** births (persons) (2025-04-01..2025-04-30) [keep: ] quote: "但隨後便一路走低:3月9,388人、4月8,684人、5月8,433人。"
  - p18 Taiwan live births, May 2025 = **8,433** births (persons) (2025-05-01..2025-05-31) [keep: ] quote: "但隨後便一路走低:3月9,388人、4月8,684人、5月8,433人。"
  - p19 Taiwan live births, November 2025 = **7,946** births (persons) (2025-11-01..2025-11-30) [keep: ] quote: "進入下半年,11月更跌至7,946人,12月雖小幅回升至9,027人,全年月均出生人數約為8,984人。"
  - p20 Taiwan live births, December 2025 = **9,027** births (persons) (2025-12-01..2025-12-31) [DISCARD: December 2025 births; not needed for the September seasonal ratio.] quote: "進入下半年,11月更跌至7,946人,12月雖小幅回升至9,027人,全年月均出生人數約為8,984人。"
  - p21 Taiwan average monthly live births, 2025 = **8,984** births (persons) per month (2025-01-01..2025-12-31) [DISCARD: 2025 monthly average; derived from the annual total and not an independent input.] quote: "12月雖小幅回升至9,027人,全年月均出生人數約為8,984人。"
  - p22 Taiwan live births, January 2026 = **8,723** births (persons) (2026-01-01..2026-01-31) [keep: ] quote: "進入2026年,趨勢沒有絲毫喘息。1月出生8,723人,與2025年同月相比年減8.1%"
  - p23 Taiwan live births, February 2026 (record monthly low) = **6,523** births (persons) (2026-02-01..2026-02-28) [DISCARD: Duplicate of p3 (same February 2026 record-low 6,523 births from the same MOI release).] quote: "2026年3月,內政部公布了一組震驚輿論的數字:2月份全國新生兒僅6,523人,首度跌破7,000人大關,創下台灣有史以來單月出生人數的最低紀錄。"
  - p24 Taiwan cumulative live births, January–February 2026 = **15,246** births (persons) (2026-01-01..2026-02-28) [DISCARD: Jan-Feb 2026 cumulative 15,246; derived from p22 and p3, not an independent input.] quote: "即便如此,2026年前兩月合計僅15,246人,與2025年同期的19,902人相比,實質年減幅仍達23.4%"
- `https://www.bigmedia.com.tw/article/1773546826373` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.baitimes.com/2026/03/16/%e5%8f%b0%e7%81%a3%e6%ad%a3%e5%9c%a8%e6%b6%88%e5%a4%b1-%e5%87%ba%e7%94%9f%e5%b4%a9%e8%b7%8c%e8%83%8c%e5%be%8c%e7%9` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.vocofm.com/taiwan-news/141558/` -> **snapshot** (snapshot 20250624134835); points raw/verified 0/0

### d4 [related_series] Population and demographic trends, including women of childbearing age and fertility rates.

Hypothesis: The number of births is a function of the number of women of childbearing age and the age-specific fertility rates. Changes in these factors can adjust historical birth counts to the current period.

Queries issued by the searcher: Taiwan total fertility rate 2025 2026 內政部; 內政部 育齡婦女 人口 統計 2026; Taiwan women aged 15-49 population 2026 育齡婦女 人數; 內政部戶政司 戶籍登記出生人數 2026年8月 統計

- `https://news.pts.org.tw/tag/1542?type=new&page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://open2.idataiwan.com/3334/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/%E6%AF%94%E6%83%B3%E5%83%8F%E6%9B%B4%E5%BF%AB-%E5%87%BA%E7%94%9F%E4%BA%BA%E5%8F%A3%E5%8F%AA%E5%89%A92-7%E8%90%AC-%E5%8F%B0%E` -> **snapshot** (snapshot 20260829011913); points raw/verified 15/2
  - p25 Taiwan total fertility rate, 2025 = **0.7** births per woman (2025-01-01..2025-12-31) [DISCARD: Rounded 2025 TFR 0.7; duplicate of the precise p26.] quote: "而台灣2025年總生育率更只有0.7。"
  - p26 Taiwan total fertility rate, 2025 (precise figure) = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "由於2025 年我國總生育率已跌至 0.695 人的低水準,降幅遠超預期"
- `https://asianews.network/chips-powerhouse-hsinchu-a-bright-spot-amid-taiwans-birth-rate-crisis/` -> **snapshot** (snapshot 20260127034108); points raw/verified 15/9
  - p27 Taiwan crude birth rate, 2025 = **4.62** births per 1,000 people (2025-01-01..2025-12-31) [DISCARD: 2025 crude birth rate; derived from annual births and population, not an independent input.] quote: "its crude birth rate plummeting to 4.62 per 1,000 people in 2025, down from 5.76 a year earlier"
  - p28 Taiwan crude birth rate, 2024 = **5.76** births per 1,000 people (2024-01-01..2024-12-31) [DISCARD: 2024 crude birth rate; derived from annual births and population, not an independent input.] quote: "its crude birth rate plummeting to 4.62 per 1,000 people in 2025, down from 5.76 a year earlier"
  - p29 Taiwan total number of newborns, 2025 (record low) = **107,812** newborns (persons) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p11 (same 2025 annual births 107,812).] quote: "In 2025, the total number of newborns hit a record low of 107,812."
  - p30 Taiwan projected total fertility rate (TFR), 2025 (projection, below 0.8) = **0.8** children per woman (TFR) (2025-01-01..2025-12-31) [DISCARD: Projected 2025 TFR below 0.8; superseded by actual 0.695 (p26).] quote: "the 2025 figure is projected to have fallen below 0.8, based on monthly government data"
  - p31 South Korea expected total fertility rate (TFR), 2025 (expected to surpass 0.8) = **0.8** children per woman (TFR) (2025-01-01..2025-12-31) [DISCARD: South Korea TFR context; not a Taiwan birth input.] quote: "the TFR for the previous record holder, South Korea, is expected to surpass 0.8 in 2025"
  - p32 TSMC employees' share of all newborns in Taiwan, 2023 = **1.8** per cent of all newborns (2023-01-01..2023-12-31) [DISCARD: TSMC newborn share; contextual, not a monthly birth input.] quote: "its employees make up only 0.3 per cent of the island's population, but were responsible for 1.8 per cent of all newborns in 2023"
  - p33 Taiwan housing price-to-annual-income ratio, 2024 (record high) = **10.76** ratio (years of annual income) (2024-01-01..2024-12-31) [DISCARD: Housing affordability ratio; contextual, not a monthly birth input.] quote: "In 2024, Taiwan's housing price-to-annual-income ratio hit a record high of 10.76"
  - p34 Taipei housing price-to-annual-income ratio, 2024 = **16.6** ratio (years of annual income) (2024-01-01..2024-12-31) [DISCARD: Taipei housing affordability ratio; contextual, not a monthly birth input.] quote: "with the ratio in Taipei reaching 16.6, meaning that it would take a person more than 16 years to afford a home in the capital"
  - p35 Share of survey respondents unwilling to have children due to economic concerns  = **70** per cent of respondents (2025-11-01..2025-11-30) [DISCARD: Survey on unwillingness to have children; contextual, not a monthly birth input.] quote: "According to a November 2025 survey by popular job portal 1111, close to 70 per cent of respondents polled said they were unwilling to have children due to economic concerns."
- dropped by code checks: 19 (number: unknown scale word '萬': 10; period_end 2026-12-31 after as_of: 1; period_end 2075-12-31 after as_of: 1; value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 1; period_end missing or unparseable: 5)

### d5 [administrative] Household registration offices and health authority birth reporting.

Hypothesis: Births are registered at household registration offices, but hospitals report births to health authorities. The number of birth notifications or health insurance birth records may be a leading indicator or a check on registration counts.

Queries issued by the searcher: Taiwan 出生通報 統計 國民健康署 月; 台灣 戶籍登記出生人數 2026 9月 統計; Taiwan monthly live births 2026 household registration statistics; 內政部戶政司 出生人數 統計 2025 每月

- `https://www.economy.com/taiwan-china/births` -> **snapshot** (snapshot 20230126211113); points raw/verified 15/13
  - p36 Taiwan monthly registered births, October 2022 (household registration, NSA) = **12,242** births (persons) (2022-10-01..2022-10-31) [DISCARD: October 2022 registered births; too old and not the target month.] quote: "\| Births \| Oct 2022 \| 12,242 \| 12,217 \| #, NSA \| Monthly \|"
  - p37 Taiwan monthly registered births, September 2022 (household registration, NSA) = **12,217** births (persons) (2022-09-01..2022-09-30) [DISCARD: September 2022 registered births; too old to anchor September 2026 without a large trend adjustment, and the 2022-2025 d] quote: "\| \| Sep 2022 \| 12,217 \|"
  - p38 Taiwan monthly registered births, October 2022 (top data block, NSA) = **12,242** births (persons) (2022-10-01..2022-10-31) [DISCARD: Duplicate of p36 (same October 2022 registered births value from the same economy.com page block).] quote: "\| Data \| Oct 2022 \| 12,242 \|"
  - p39 Taiwan monthly registered births, September 2022 (top data block, NSA) = **12,217** births (persons) (2022-09-01..2022-09-30) [DISCARD: Duplicate of p37 (same September 2022 registered births value from the same economy.com page block).] quote: "\| \| Sep 2022 \| 12,217 \|"
  - p40 Taiwan monthly birth rate, October 2022 (per thousand population, NSA) = **0.53** births per thousand population (2022-10-01..2022-10-31) [DISCARD: 2022 monthly birth rate; redundant with p41 and too old to inform September 2026.] quote: "\| Birth Rate \| Oct 2022 \| 0.53 \| 0.53 \| # per Ths. pop., NSA \| Monthly \|"
  - p41 Taiwan monthly birth rate, September 2022 (per thousand population, NSA) = **0.53** births per thousand population (2022-09-01..2022-09-30) [DISCARD: 2022 monthly birth rate; redundant with p40 and too old to inform September 2026.] quote: "\| Birth Rate \| Oct 2022 \| 0.53 \| 0.53 \| # per Ths. pop., NSA \| Monthly \|"
  - p42 Taiwan monthly registered deaths, October 2022 (NSA) = **17,099** deaths (persons) (2022-10-01..2022-10-31) [DISCARD: 2022 deaths; not a birth input.] quote: "\| Deaths \| Oct 2022 \| 17,099 \| 16,505 \| #, NSA \| Monthly \|"
  - p43 Taiwan monthly registered deaths, September 2022 (NSA) = **16,505** deaths (persons) (2022-09-01..2022-09-30) [DISCARD: 2022 deaths; not a birth input.] quote: "\| Deaths \| Oct 2022 \| 17,099 \| 16,505 \| #, NSA \| Monthly \|"
  - p44 Taiwan monthly death rate, October 2022 (per thousand population, NSA) = **0.74** deaths per thousand population (2022-10-01..2022-10-31) [DISCARD: 2022 death rate; not a birth input.] quote: "\| Death Rate \| Oct 2022 \| 0.74 \| 0.71 \| # per Ths. pop., NSA \| Monthly \|"
  - p45 Taiwan monthly death rate, September 2022 (per thousand population, NSA) = **0.71** deaths per thousand population (2022-09-01..2022-09-30) [DISCARD: 2022 death rate; not a birth input.] quote: "\| Death Rate \| Oct 2022 \| 0.74 \| 0.71 \| # per Ths. pop., NSA \| Monthly \|"
  - p46 Taiwan end-of-month population, October 2022 (NSA) = **23,212,056** persons (2022-10-31..2022-10-31) [DISCARD: 2022 population; not a birth input.] quote: "\| Population \| Oct 2022 \| 23,212,056 \| 23,198,133 \| # EOM, NSA \| Monthly \|"
  - p47 Taiwan end-of-month population, September 2022 (NSA) = **23,198,133** persons (2022-09-30..2022-09-30) [DISCARD: 2022 population; not a birth input.] quote: "\| Population \| Oct 2022 \| 23,212,056 \| 23,198,133 \| # EOM, NSA \| Monthly \|"
  - p48 Taiwan annual net migration, 2021 (NSA) = **-156,010** persons (2021-01-01..2021-12-31) [DISCARD: 2021 net migration; not a birth input.] quote: "\| Net Migration \| 2021 \| -156,010 \| -33,978 \| #, NSA \| Annual \|"
- `https://www.mlshb.gov.tw/nc/api/v3/storage/files/a98fa5fbeb25ae5ce476b22251a06ce43d5c43fb297ac5a8caa4e8c9ab04d28b.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.hpa.gov.tw/File/Attach/16584/File_20499.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160218724` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period year 2020 does not appear in the page text or URL (likely mis-dated): 1; number: more than one number in value_as_written: 1)

### d6 [forecasts_markets] Official population projections and demographic forecasts.

Hypothesis: National Development Council (NDC) population projections include monthly or annual birth estimates. These can provide a baseline for 2026, though they may be outdated.

Queries issued by the searcher: Taiwan population projections 2026 births 國發會 人口推估 出生數; Taiwan birth forecast 2026 內政部 戶籍登記出生人數 統計; 內政部 2025年9月 出生數 新生兒 戶口統計; 國發會 人口推估 2026 出生數 9.4萬 中推估 報告 下載

- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 11/0
- `https://www.chinatimes.com/realtimenews/20251009002298-260410` -> **snapshot** (snapshot 20251110062352); points raw/verified 15/11
  - p49 Taiwan live births registered in September 2025 (monthly household registration  = **8,603** births (persons) (2025-09-01..2025-09-30) [keep: ] quote: "今年9月出生數8,603人,約每5.1分鐘出生一個嬰兒"
  - p50 Year-on-year change in Taiwan September births, 2025 vs 2024 (percent) = **27.04** percent (2025-09-01..2025-09-30) [DISCARD: September 2025 y/y decline 27.04%; derived from p49 and the September 2024 level, not an independent input.] quote: "相比去年9月的出生人數大幅減少27.04%、少了3,189個新生娃"
  - p51 Absolute year-on-year decline in Taiwan September births, 2025 vs 2024 (persons) = **3,189** births (persons) (2025-09-01..2025-09-30) [DISCARD: September 2025 absolute y/y decline 3,189; derived from p49 and the September 2024 level, not an independent input.] quote: "相比去年9月的出生人數大幅減少27.04%、少了3,189個新生娃"
  - p52 Taiwan annualised crude birth rate for September 2025 (per thousand) = **4.49** per thousand (annualised crude birth rate) (2025-09-01..2025-09-30) [DISCARD: September 2025 annualised crude birth rate; derived from p49 and not an independent input.] quote: "折合年粗出生率為千分之4.49"
  - p53 Taiwan deaths in May 2025 (monthly household registration statistics) = **15,387** deaths (persons) (2025-05-01..2025-05-31) [DISCARD: May 2025 deaths; not a birth input.] quote: "而5月死亡數為15,387人,平均約每2.8分鐘死亡一個人"
  - p54 Taiwan annualised crude death rate for May 2025 (per thousand) = **8.03** per thousand (annualised crude death rate) (2025-05-01..2025-05-31) [DISCARD: May 2025 crude death rate; not a birth input.] quote: "折合年粗死亡率為千分之8.03,單月死亡比出生多了6,784人"
  - p55 Excess of deaths over births in Taiwan, May 2025 (persons) = **6,784** persons (deaths minus births) (2025-05-01..2025-05-31) [DISCARD: Deaths-minus-births; not a birth input.] quote: "單月死亡比出生多了6,784人,全台已連續57個月「生不如死」"
  - p56 Taiwan annualised natural increase rate, September 2025 (per thousand) = **-3.54** per thousand (annualised natural increase rate) (2025-09-01..2025-09-30) [DISCARD: Natural increase rate; not a birth input.] quote: "全國已連續57個月「生不如死」,折合年自然增加率為千分之-3.54"
  - p57 Taiwan in-migrants in September 2025 (monthly household registration statistics) = **79,080** persons (in-migrants) (2025-09-01..2025-09-30) [DISCARD: September 2025 in-migrants; not a birth input.] quote: "今年全國9月遷入人口僅79,080人,低於遷出人數83,608人"
  - p58 Taiwan out-migrants in September 2025 (monthly household registration statistics = **83,608** persons (out-migrants) (2025-09-01..2025-09-30) [DISCARD: September 2025 out-migrants; not a birth input.] quote: "今年全國9月遷入人口僅79,080人,低於遷出人數83,608人"
  - p59 Taiwan population aged 0-14 as share of total, end-September 2025 = **11.58** percent (share of total population) (2025-09-30..2025-09-30) [DISCARD: 0-14 population share; not a birth input.] quote: "截至今年9月底,全國幼年(0~14歲)人口佔比為11.58%"
- `https://s8088.com/article/date=today&id=3223066` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mdnkids.com/content.asp?Link_String_=248T00000GDYIDY` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (number: unknown scale word '萬': 9; value_as_written not in quote as a whole number: 1; period_end missing or unparseable: 2; number: unknown scale word '成': 1; number: no number in value_as_written: 1; period_end 2037-12-31 after as_of: 1)

### d7 [shocks] Calendar effects, holidays, and policy changes affecting birth timing.

Hypothesis: September births may be influenced by conception around December–January, including holiday effects and any policy changes (e.g., birth subsidies) that could affect timing. Dragon year effects (2024) may have shifted births, but 2026 is a Horse year.

Queries issued by the searcher: 台灣 生育補助 2026 內政部戶政司 出生人數 統計; Taiwan birth subsidy policy 2025 2026 monthly birth statistics; 內政部 戶政司 出生人數 統計 2025 每月 1月 2月 9月 表; 2025年 台灣 每月 出生人數 新生兒 統計 月別 內政部

- `https://fwnews.com.tw/tag/%E6%96%B0%E7%94%9F%E5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://dr131.com/snakeyearbabies/` -> **snapshot** (snapshot 20260512163234); points raw/verified 15/12
  - p60 Taiwan live births in January 2025 (start of Snake year), monthly registered bir = **9,495** births (persons) (2025-01-01..2025-01-31) [DISCARD: Duplicate of p14 (same January 2025 births 9,495).] quote: "2025年1月底是蛇年開頭,出生人數是9495人,是歷年單月分的次低。"
  - p61 Taiwan live births in February 2025, monthly registered births = **10,407** births (persons) (2025-02-01..2025-02-28) [DISCARD: Duplicate of p15 (same February 2025 births 10,407).] quote: "到了 2月,略為回升到萬人,為 10407人。"
  - p62 Taiwan live births in March 2025, monthly registered births = **9,388** births (persons) (2025-03-01..2025-03-31) [DISCARD: Duplicate of p16 (same March 2025 births 9,388).] quote: "可是,到了 3月,出生人數只有 9388人"
  - p63 Taiwan live births in April 2025, monthly registered births (record low) = **8,684** births (persons) (2025-04-01..2025-04-30) [DISCARD: Duplicate of p17 (same April 2025 births 8,684).] quote: "4月更掉到8684人,少了7.5%,創下歷年單月最低的出生記錄"
  - p64 Taiwan live births in May 2025, monthly registered births = **8,433** births (persons) (2025-05-01..2025-05-31) [DISCARD: Duplicate of p18 (same May 2025 births 8,433).] quote: "內政部統計5月出生數為8433人,比去年同期少了2735人"
  - p65 Taiwan live births in July 2025, monthly registered births = **8,939** births (persons) (2025-07-01..2025-07-31) [DISCARD: July 2025 births; not needed for the September seasonal ratio and redundant with the 2025 monthly path.] quote: "即使到了下半年,2025年7月的出生人數為8939人"
  - p66 Taiwan live births in September 2025, monthly registered births = **8,603** births (persons) (2025-09-01..2025-09-30) [DISCARD: Duplicate of p49 (same September 2025 births 8,603).] quote: "9月份的新生兒出生數僅8603人,相當5.1分鐘出生一名嬰兒,為歷年單月第三低的出生人數"
  - p67 Year-on-year decline in Taiwan September 2025 births versus September 2024 = **27.04** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p50 (same September 2025 y/y decline 27.04%).] quote: "比2024年9月的出生人數大幅減少27.04%,等於少了3189個新生兒。"
  - p68 Taiwan live births in November 2025, monthly registered births = **7,946** births (persons) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p19 (same November 2025 births 7,946).] quote: "及至11月,出生人數不到8000人,只有7946人"
  - p69 Taiwan full-year 2024 live births = **13.4** births (persons) (2024-01-01..2024-12-31) [DISCARD: Rounded duplicate of p12 (2024 annual births 13.4万 vs precise 134,856).] quote: "2024年全年有13.4萬人出生"
  - p70 Taiwan 2024 Dragon year newborn count (record low) = **13.48** births (persons) (2024-01-01..2024-12-31) [DISCARD: Rounded duplicate of p12 (2024 annual births 13.48万 vs precise 134,856).] quote: "2024年龍年新生兒只有13.48萬人,創下新低,比2023年兔寶寶還要少。"
  - p71 Projected Taiwan 2025 Snake year births if 13%–14% below Dragon year (upper boun = **11.72** births (persons) (2025-01-01..2025-12-31) [DISCARD: Projected 2025 births 11.59-11.72万; falsified by actual 107,812, so it is a misleading extrapolation.] quote: "如果2025年蛇寶寶比龍寶寶減少13%~14%,新生兒人數可能只有11.59萬~11.72萬人"
- `https://www.ocac.gov.tw/OCAC/Eng/Pages/Detail.aspx?nodeid=329&pid=86692946` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gb.crntt.com/crn-webapp/touch/detail.jsp?coluid=93&kindid=13830&docid=160230405` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (number: more than one number in value_as_written: 3)

### d8 [related_series] Comparable East Asian countries with similar demographic trends.

Hypothesis: Taiwan's birth trends are similar to South Korea and Japan, though levels differ. Recent monthly birth data from these countries can provide a directional signal for Taiwan's September 2026, after adjusting for differences in level and timing.

Queries issued by the searcher: South Korea monthly births 2026 statistics; Japan monthly births 2026 preliminary; Taiwan monthly births 2026 戶籍登記出生人數 內政部; 台灣 出生人數 2026年 每月 統計

- `https://french.korea.net/NewsFocus/Society/view?articleId=294745` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/ntnadmNews/4793427` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://chinese.korea.net/NewsFocus/Society/view?articleId=289565` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.net/NewsFocus/Society/view?articleId=294740&koreanId=294708` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] MOI monthly household-registration release

Hypothesis: The single most valuable missing input is the actual registered birth count for June, July and August 2026. These three months are the most recent observed levels and would let us anchor the September 2026 estimate on a within-year trajectory rather than on a 2025 seasonal shape. Without them, the September estimate rests on a May 2026 level and a 2025 September/May ratio, which is a long extrapolation.

Queries issued by the searcher: 內政部戶政司 115年6月 出生數 戶籍登記; 內政部 統計通報 115年7月 出生數; Taiwan registered births July 2026 MOI household registration; 戶籍登記出生人數 115年8月 內政部

- `https://www.economy.com/taiwan-china/population/not-seasonally-adjusted` -> **snapshot** (snapshot 20230402031716); points raw/verified 15/12
  - p72 Taiwan registered births, January 2023 (monthly, NSA) = **10,948** births (persons) (2023-01-01..2023-01-31) [DISCARD: January 2023 births; too old and redundant with the 2025-2026 monthly series.] quote: "\| Births \| Jan 2023 \| 10,948 \| 12,178 \| #, NSA \| Monthly \|"
  - p73 Taiwan registered births, previous month (December 2022) (monthly, NSA) = **12,178** births (persons) (2022-12-01..2022-12-31) [DISCARD: December 2022 births; too old and redundant.] quote: "\| Births \| Jan 2023 \| 10,948 \| 12,178 \| #, NSA \| Monthly \|"
  - p74 Taiwan birth rate, January 2023 (per thousand population, NSA) = **0.47** births per thousand population (2023-01-01..2023-01-31) [DISCARD: January 2023 birth rate; too old and redundant.] quote: "\| Birth Rate \| Jan 2023 \| 0.47 \| 0.52 \| # per Ths. pop., NSA \| Monthly \|"
  - p75 Taiwan birth rate, previous month (December 2022) (per thousand population, NSA) = **0.52** births per thousand population (2022-12-01..2022-12-31) [DISCARD: December 2022 birth rate; too old and redundant.] quote: "\| Birth Rate \| Jan 2023 \| 0.47 \| 0.52 \| # per Ths. pop., NSA \| Monthly \|"
  - p76 Taiwan registered deaths, January 2023 (monthly, NSA) = **17,770** deaths (persons) (2023-01-01..2023-01-31) [DISCARD: January 2023 deaths; not a birth input.] quote: "\| Deaths \| Jan 2023 \| 17,770 \| 17,685 \| #, NSA \| Monthly \|"
  - p77 Taiwan registered deaths, previous month (December 2022) (monthly, NSA) = **17,685** deaths (persons) (2022-12-01..2022-12-31) [DISCARD: December 2022 deaths; not a birth input.] quote: "\| Deaths \| Jan 2023 \| 17,770 \| 17,685 \| #, NSA \| Monthly \|"
  - p78 Taiwan death rate, January 2023 (per thousand population, NSA) = **0.76** deaths per thousand population (2023-01-01..2023-01-31) [DISCARD: January 2023 death rate; not a birth input.] quote: "\| Death Rate \| Jan 2023 \| 0.76 \| 0.76 \| # per Ths. pop., NSA \| Monthly \|"
  - p79 Taiwan death rate, previous month (December 2022) (per thousand population, NSA) = **0.76** deaths per thousand population (2022-12-01..2022-12-31) [DISCARD: December 2022 death rate; not a birth input.] quote: "\| Death Rate \| Jan 2023 \| 0.76 \| 0.76 \| # per Ths. pop., NSA \| Monthly \|"
  - p80 Taiwan total population, end of January 2023 (monthly, NSA) = **23,301,968** persons (2023-01-31..2023-01-31) [DISCARD: January 2023 population; not a birth input.] quote: "\| Population \| Jan 2023 \| 23,301,968 \| 23,264,640 \| # EOM, NSA \| Monthly \|"
  - p81 Taiwan total population, end of December 2022 (monthly, NSA) = **23,264,640** persons (2022-12-31..2022-12-31) [DISCARD: December 2022 population; not a birth input.] quote: "\| Population \| Jan 2023 \| 23,301,968 \| 23,264,640 \| # EOM, NSA \| Monthly \|"
  - p82 Taiwan net migration, 2021 (annual, NSA) = **-156,010** persons (2021-01-01..2021-12-31) [DISCARD: Duplicate of p48 (same 2021 net migration value from a second economy.com snapshot).] quote: "\| Net Migration \| 2021 \| -156,010 \| -33,978 \| #, NSA \| Annual \|"
  - p83 Taiwan population monthly change, January 2023 (NSA) = **0.16** percent (2023-01-01..2023-01-31) [DISCARD: January 2023 monthly population change; not a birth input.] quote: "\| \| Monthly \| 0.16 % \|"
- `https://www.chinatimes.com/realtimenews/20260710001780-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%E6%96%B0%E7%94%9F%E5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (period year 2020 does not appear in the page text or URL (likely mis-dated): 1; number: more than one number in value_as_written: 2)

### b2 [related_series] Marriage registrations as a leading indicator

Hypothesis: September 2026 births are largely conceptions from roughly December 2025–January 2026. Marriage registrations in that window, and the share of first births, would provide an independent leading signal to cross-check the seasonal-ratio route. If late-2025/early-2026 marriages fell sharply, the September 2026 estimate should be pulled below the pure seasonal extrapolation.

Queries issued by the searcher: 內政部 結婚登記 對數 114年12月; Taiwan marriage registrations December 2025 statistics; 戶政司 結婚 出生 月統計 114年; 台灣 第一胎 占比 出生 統計

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.moi.gov.tw./News_Content.aspx?n=9&sms=9009&s=339254` -> **snapshot** (snapshot 20260817180449); points raw/verified 15/0
- `https://tw.forumosa.com/t/taiwan-population-decline/259408` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvNDIwL3JlbGZpbGUvMjA4MDQvOTM0ODY3MS85NWVlMzk3MS0yNjM5LTRiZDItYWJjZS1lYjhlYmUxY2ZjZGEucGRm&n=N` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- dropped by code checks: 15 (number: more than one number in value_as_written: 6; period year 2025 does not appear in the page text or URL (likely mis-dated): 8; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [forecasts_markets] Official population projection / monthly birth forecast

Hypothesis: The National Development Council (國發會) population projection and any 2026 monthly birth forecast would give an independent baseline for the 2026 level and a check on whether the 2025→2026 decline is expected to continue at the same rate. This is the assumption contributing the largest uncertainty: the size of the 2026 y/y decline relative to 2025.

Queries issued by the searcher: 國發會 人口推估 115年 出生數; Taiwan population projection 2026 births NDC; 國發會 中華民國人口推估 2026 2150 出生數 9.4萬; 內政部 戶籍登記 出生 115年9月 統計

- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 11/0
- `https://www.chinatimes.com/newspapers/20260829000365-260120?chdtv` -> **snapshot** (snapshot 20260829080326); points raw/verified 15/1
  - p84 NDC 2022 projection: year births begin below 100,000 (Taiwan) = **2,022** year (2022-01-01..2022-12-31) [DISCARD: NDC projection vintage information; not a birth input.] quote: "上次推估已較2022年推估提前14年了"
- `https://ocacnews.net/article/422295` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%8F%B0%E7%81%A3%E4%BA%BA%E5%8F%A3%E6%95%B820%E5%B9%B4%E5%BE%8C%E4%B8%8D%E5%88%B02%E5%8D%83%E8%90%AC-%E9%80%99%E5%B9%B4-%E` -> **snapshot** (snapshot 20260901044610); points raw/verified 15/6
  - p85 Taiwan total fertility rate 2024 (總生育率) = **0.885** children per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR 0.885; contextual, not a monthly birth input.] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人,遠低於人口推估預期。"
  - p86 Taiwan total fertility rate 2025 (總生育率) = **0.695** children per woman (2025-01-01..2025-12-31) [DISCARD: Duplicate of p26 (same 2025 TFR 0.695).] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人,遠低於人口推估預期。"
  - p87 NDC previous (2024) total fertility rate assumptions, high/medium/low (高中低) = **1.3** children per woman (2024-01-01..2024-12-31) [DISCARD: NDC high TFR assumption 1.3; not a birth input.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p88 NDC previous (2024) total fertility rate assumptions, medium (中推估) = **1** children per woman (2024-01-01..2024-12-31) [DISCARD: NDC medium TFR assumption 1.0; not a birth input.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p89 NDC previous (2024) total fertility rate assumptions, low (低推估) = **0.8** children per woman (2024-01-01..2024-12-31) [DISCARD: NDC low TFR assumption 0.8; not a birth input.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p90 Share of women aged 20–49 currently married, 2025 (20歲至49歲婦女有偶率) = **43.5** percent (2025-01-01..2025-12-31) [keep: ] quote: "台灣20歲至49歲婦女有偶率,從2005年的55.3%,下降至2025年的43.5%"
- dropped by code checks: 34 (number: unknown scale word '萬': 18; number: unknown scale word '成': 1; period_end missing or unparseable: 6; number: no number in value_as_written: 1; period_end 2037-12-31 after as_of: 1; value_as_written not in quote as a whole number: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end 2075-12-31 after as_of: 1; period_end 2045-12-31 after as_of: 1; period_end 2026-12-31 after as_of: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'september 2026 births', 'taiwan birth rate']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p5'] Same source (Chinatimes report of MOI May 2026 release): p1 level, p2 April level, p5 the MoM change; p1 = p2 - p5 is internally consistent, so these are one measurement, not three.
- corroborating: ['p3', 'p23'] Two independent write-ups (Chinatimes snapshot 2026-06-22 and j-media snapshot 2026-04-17) both give February 2026 = 6,523, the record monthly low. Same underlying MOI release, so it is one measuremen
- corroborating: ['p4', 'p18'] p4 (May 2026 down 1,601 y/y) implies May 2025 ≈ 8,433, matching p18/p64 exactly. Confirms the May 2025 level and the y/y decline magnitude.
- corroborating: ['p14', 'p60'] January 2025 = 9,495 in both j-media and dr131; same MOI figure, duplicate vintage.
- corroborating: ['p15', 'p61'] February 2025 = 10,407 in both sources; duplicate.
- corroborating: ['p16', 'p62'] March 2025 = 9,388 in both sources; duplicate.
- corroborating: ['p17', 'p63'] April 2025 = 8,684 in both sources; duplicate.
- corroborating: ['p18', 'p64'] May 2025 = 8,433 in both sources; duplicate.
- corroborating: ['p19', 'p68'] November 2025 = 7,946 in both sources; duplicate.
- corroborating: ['p49', 'p66'] September 2025 = 8,603 in both Chinatimes and dr131; same MOI monthly release, duplicate vintage.
- corroborating: ['p50', 'p51', 'p67'] September 2025 y/y decline of 27.04% / 3,189 persons reported identically by two sources; implies September 2024 ≈ 11,792, consistent with p37/p39 (Sept 2022 = 12,217) and the 2024 Dragon-year level.
- corroborating: ['p11', 'p29'] 2025 annual births = 107,812 in both j-media and asianews; same MOI annual total.
- corroborating: ['p12', 'p69', 'p70'] 2024 annual births ≈ 134,856 (p12) vs 13.4萬 (p69) and 13.48萬 (p70); p69/p70 are rounded versions of the same MOI total, so p12 is the precise vintage.
- corroborating: ['p25', 'p26'] 2025 TFR 0.7 (rounded) and 0.695 (precise) from the same Yahoo article; p26 is the usable vintage.
- corroborating: ['p36', 'p38'] October 2022 registered births 12,242 appears twice in the same economy.com table (row and top block); duplicate.
- corroborating: ['p37', 'p39'] September 2022 registered births 12,217 appears twice in the same table; duplicate.
- corroborating: ['p40', 'p41'] Both monthly birth rates 0.53 per thousand for Sep/Oct 2022; same table, duplicate.
- corroborating: ['p42', 'p43'] Deaths Oct 2022 17,099 and Sep 2022 16,505; same table, consistent with p44/p45 rates.
- corroborating: ['p46', 'p47'] End-Sep 2022 population 23,198,133 and end-Oct 2022 23,212,056; same table, consistent with p40/p41 rates.
- corroborating: ['p1', 'p22', 'p24'] 2026 monthly levels (Jan 8,723; Feb 6,523; Apr 8,144; May 6,832) and the Jan–Feb cumulative 15,246 are mutually consistent (8,723 + 6,523 = 15,246), confirming the 2026 series is on the same definitio
- corroborating: ['p10', 'p11', 'p13'] 2016 = 208,440, 2025 = 107,812, 2025 y/y -20.1%: the 2025 decline is consistent with the 2024 base of 134,856 (p12).
- corroborating: ['p6', 'p7'] May 2026 crude birth rate 3.46 per thousand and 6.5 minutes per birth are two renderings of the same 6,832 count; internal consistency check only.
- corroborating: ['p8', 'p9'] May 2026 population decline figures; same release, not directly informative for births.
- corroborating: ['p53', 'p54', 'p55'] May 2025 deaths 15,387, crude death rate 8.03, excess deaths 6,784; same release, consistent with May 2025 births 8,433 (p18).
- corroborating: ['p56', 'p57', 'p58', 'p59'] September 2025 natural increase rate, in/out migration, and 0–14 share; same release, contextual only.
- corroborating: ['p27', 'p28'] 2025 crude birth rate 4.62 vs 2024 5.76; same article, consistent with the annual birth totals.
- corroborating: ['p30', 'p31'] Projected 2025 TFRs for Taiwan (<0.8) and South Korea (>0.8); same article, directional context.
- corroborating: ['p32', 'p33', 'p34', 'p35'] TSMC share of newborns, housing price-to-income ratios, and survey on unwillingness to have children; same article, structural context for the downward trend.
- conflicting: ['p36', 'p49'] Not a true conflict: September 2022 registered births 12,217 vs September 2025 8,603 reflects a genuine 30% decline over three years, not a definitional disagreement. Both are MOI household-registrati
- corroborating: ['p20', 'p21'] December 2025 = 9,027 and 2025 monthly average 8,984; consistent with the 2025 annual total 107,812.
- corroborating: ['p71', 'p11'] The dr131 projection of 11.59–11.72萬 for 2025 (13–14% below the Dragon year) brackets the actual 107,812; useful as a check on the size of the Snake-year drop.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p5'] May 2026 level (p1), April 2026 level (p2), and the May-over-April decline (p5) are internally consistent: 8,144 - 6,832 = 1,312. Same source (Chinatimes snapshot 2026-06-22), so they are one measurem
- corroborating: ['p1', 'p4', 'p18'] May 2026 births (p1) and the May 2026 y/y decline of 1,601 (p4) imply May 2025 = 8,433, which matches the independently reported May 2025 level (p18). This cross-checks the 2025 monthly series against
- corroborating: ['p3', 'p23'] Both report February 2026 registered births at 6,523, the record monthly low. Same underlying MOI release, so this is a duplicate measurement, not independent confirmation.
- corroborating: ['p14', 'p60'] January 2025 births = 9,495 in both the j-media annual review and the dr131 article. Same MOI source, duplicate reporting.
- corroborating: ['p15', 'p61'] February 2025 births = 10,407 in both sources; duplicate reporting of the same MOI figure.
- corroborating: ['p16', 'p62'] March 2025 births = 9,388 in both sources; duplicate reporting.
- corroborating: ['p17', 'p63'] April 2025 births = 8,684 in both sources; duplicate reporting.
- corroborating: ['p18', 'p64'] May 2025 births = 8,433 in both sources; duplicate reporting.
- corroborating: ['p19', 'p68'] November 2025 births = 7,946 in both sources; duplicate reporting.
- corroborating: ['p49', 'p66'] September 2025 registered births = 8,603 in both the Chinatimes snapshot and the dr131 article; duplicate reporting of the same MOI monthly figure.
- corroborating: ['p50', 'p67'] Both report the September 2025 y/y decline as 27.04%; duplicate reporting.
- corroborating: ['p11', 'p29'] 2025 annual births = 107,812 in both j-media and asianews; duplicate reporting of the same MOI annual total.
- corroborating: ['p25', 'p26', 'p86'] 2025 TFR reported as 0.7 (rounded), 0.695 (precise), and 0.695 again; the precise figure is the same measurement, the rounded one is a presentation variant.
- corroborating: ['p12', 'p69', 'p70'] 2024 annual births reported as 134,856 (precise), 13.4万 (rounded), and 13.48万 (rounded); all the same MOI annual total at different rounding.
- corroborating: ['p36', 'p38'] October 2022 registered births = 12,242 in two blocks of the same economy.com page; duplicate extraction.
- corroborating: ['p37', 'p39'] September 2022 registered births = 12,217 in two blocks of the same economy.com page; duplicate extraction.
- corroborating: ['p48', 'p82'] 2021 net migration = -156,010 in two economy.com snapshots; duplicate extraction.
- corroborating: ['p10', 'p11', 'p12', 'p13'] The 2016, 2024, and 2025 annual totals and the 2025 y/y decline of 20.1% are mutually consistent (134,856 x 0.799 ≈ 107,812) and come from the same j-media article.
- corroborating: ['p22', 'p24'] January 2026 = 8,723 and Jan-Feb 2026 cumulative = 15,246 imply February 2026 = 6,523, matching p3/p23. Same source chain.
- corroborating: ['p6', 'p7'] May 2026 crude birth rate 3.46 per thousand and 6.5 minutes per birth are two presentations of the same 6,832 May 2026 count; not independent.
- corroborating: ['p1', 'p22', 'p23'] The 2026 monthly path (Jan 8,723; Feb 6,523; Apr 8,144; May 6,832) is internally consistent with the reported y/y declines and the record-low February. All trace to MOI monthly releases.
- corroborating: ['p49', 'p50', 'p51'] September 2025 = 8,603, y/y decline 27.04%, and absolute decline 3,189 are mutually consistent (8,603 / (1 - 0.2704) ≈ 11,792; 11,792 - 8,603 ≈ 3,189). Same source.
- conflicting: ['p36', 'p37', 'p49'] September 2022 registered births were 12,217 versus 8,603 in September 2025, a 30% decline over three years. This is a genuine level shift, not a contradiction; it shows the 2022 economy.com series is
- corroborating: ['p25', 'p26', 'p85', 'p86'] 2025 TFR 0.695 and 2024 TFR 0.885 are consistent across the Yahoo and asianews sources; the 2025 collapse is the dominant demographic signal.
- conflicting: ['p84', 'p87', 'p88', 'p89'] NDC's 2024 projection assumed TFR of 0.8-1.3, but actual 2025 TFR was 0.695, far below even the low assumption. NDC projections are therefore biased upward and cannot be used as a central baseline wit
- corroborating: ['p30', 'p31'] Taiwan 2025 TFR projected below 0.8 and South Korea expected to surpass 0.8; both are directional context, not direct inputs to a September 2026 Taiwan count.
- corroborating: ['p32', 'p33', 'p34', 'p35'] TSMC share of newborns, housing affordability ratios, and the 70% unwilling-to-have-children survey all describe the same structural fertility constraint; they are contextual, not monthly inputs.
- corroborating: ['p53', 'p54', 'p55', 'p56'] May 2025 deaths 15,387, crude death rate 8.03, deaths-minus-births 6,784, and natural increase -3.54 are mutually consistent with May 2025 births 8,433. Same MOI release.
- corroborating: ['p57', 'p58'] September 2025 in-migrants 79,080 and out-migrants 83,608 are from the same MOI release; they describe migration, not births, and are contextual only.
- corroborating: ['p59'] 0-14 population share 11.58% at end-September 2025 is consistent with the low birth regime; contextual only.
- corroborating: ['p40', 'p41', 'p44', 'p45', 'p46', 'p47'] 2022 monthly birth/death rates and end-of-month populations are internally consistent with the 2022 birth and death counts; they are old but coherent.
- corroborating: ['p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p83'] January 2023 births 10,948, December 2022 births 12,178, and the associated rates and populations are internally consistent; they are old but coherent.
- corroborating: ['p8', 'p9'] May 2026 daily population decrease 282 and monthly decrease 9,903 are consistent (9,903 / 31 ≈ 319, close to 282 given rounding and migration); same source.
- corroborating: ['p27', 'p28'] 2025 crude birth rate 4.62 and 2024 5.76 are consistent with the annual birth totals and population; same asianews source.
- corroborating: ['p20', 'p21'] December 2025 births 9,027 and 2025 monthly average 8,984 are consistent with the 2025 annual total 107,812 / 12 ≈ 8,984; same j-media source.
- corroborating: ['p65'] July 2025 births 8,939 fits the 2025 monthly path between May 8,433 and September 8,603; same dr131 source.
- conflicting: ['p71'] The dr131 projection of 2025 births at 11.59-11.72万 was far above the actual 107,812 (10.78万), showing that simple y/y percentage extrapolations from the Dragon year were too optimistic. This is a war

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 / May 2026 registered-births ratio | 1.02 | 0.85..1.22 | 0.7201..1.44 (widened) | ratio | m1 (m1) | In 2025, September births (8,603, p49) were 1.020 times May births (8,433, p18). The 2026 monthly path is running below 2025 (Jan 8,723 vs 9,495; Feb 6,523 vs 10,407; May 6,832 vs 8,433), so the September/May ratio may differ from 2025. The range spans a continued decline (0.85) to a modest seasonal | September 2026 registration patterns follow the same seasonal shape as 2025 relative to May, with no major registration-timing shock. | Evidence that September 2026 births are far below or above the May 2026 level by more than the stated range, e.g., a new record low or a policy-driven registration surge. |
| a2 | September 2026 / September 2025 registered-births ratio | 0.92 | 0.78..1.08 | 0.649..1.298 (widened) | ratio | m2 (m2) | The 2026 y/y decline has been running around 8-23% in Jan-Feb and about 19% in May (p1 vs p18). September 2025 was already a low base (8,603, p49). A ratio of 0.92 implies a further ~8% decline, consistent with the recent y/y pace but allowing for stabilization or a sharper drop. | The 2026 y/y decline in September is similar to the recent monthly y/y declines, with no major change in registration behavior. | A September 2026 y/y decline outside the 0.78-1.08 range, e.g., a decline steeper than 22% or an outright increase. |
| a3 | September share of 2026 annual registered births | 0.079 | 0.07..0.09 | 0.05612..0.1122 (widened) | share | m3 (m3) | In 2025, September births (8,603, p49) were 7.98% of the annual total (107,812, p11). September is typically a mid-to-low month. The range allows for modest seasonal variation and for the 2026 annual total being uncertain. | The within-year seasonal distribution of births in 2026 is similar to 2025, and the 2026 annual total is near the central estimate. | Evidence that September 2026 is a much larger or smaller share of the year than 7-9%, e.g., a policy-driven September surge or a data-reporting anomaly. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 6,977 | ['p1'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 7,903 | ['p49'] / ['a2'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 8,565 | ['p11'] / ['a3'] | [] |  | 0.33 | equal |  |

Result: central **7,788**, 80% interval [5,268, 11,513], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for live births registered in Taiwan during September 2026, as reported in the Ministry of the Interior's monthly household registration statistics, is 7,788 births. A model-based 80% interval spans 5,268 to 11,513, conditional on the stated assumptions rather than a demonstrated accuracy guarantee.

Three routes were averaged with roughly equal weight: 6,977 (latest observed level times a September/May ratio), 7,903 (September 2025 level times a year-over-year factor), and 8,565 (2025 annual total times a September share). Only the anchor levels are observed; the ratios and shares are analyst assumptions, so the methods share MOI data dependencies and are not independent.

The main risk is that [n]'s year-over-year decline could accelerate or reverse, since September 2025 was already a low base. The most useful missing evidence would be complete [n] monthly registration data through August, which would sharpen the seasonal and trend factors.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 / May 2026 registered-births ratio: 1.02 ratio, range 0.7201 to 1.44 (range widened by code); used by m1. Overturned by: Evidence that September 2026 births are far below or above the May 2026 level by more than the stated range, e.g., a new record low or a policy-driven registration surge.
- a2 September 2026 / September 2025 registered-births ratio: 0.92 ratio, range 0.649 to 1.298 (range widened by code); used by m2. Overturned by: A September 2026 y/y decline outside the [n]-[n] range, e.g., a decline steeper than [n] or an outright increase.
- a3 September share of 2026 annual registered births: 0.079 share, range 0.05612 to 0.1122 (range widened by code); used by m3. Overturned by: Evidence that September 2026 is a much larger or smaller share of the year than [n]-[n], e.g., a policy-driven September surge or a data-reporting anomaly.

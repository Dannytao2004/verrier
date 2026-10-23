# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan (Republic of China) during September 2026, as counted in the Ministry of the Interior's monthly household registration statistics (births registered in the month, by date of registration) | unit births | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior (MOI), Department of Household Registration, Taiwan

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household registration series

Hypothesis: September 2026 registered births will follow the recent level and seasonal pattern of monthly registered births; the most recent months before the cutoff (e.g., Jan-Jul 2026) anchor the level, and prior Septembers give the September seasonal factor relative to adjacent months.

Queries issued by the searcher: 內政部 戶政司 出生 統計 月 2026 出生人數; 台灣 2025 每月 出生人數 統計 內政部; 2025年9月 出生數 內政部 戶口統計 新生兒; 2024年9月 出生數 新生兒 內政部 戶口統計

- `https://www.chinatimes.com/realtimenews/20251009002298-260410` -> **snapshot** (snapshot 20251110062352); points raw/verified 15/15
  - p1 Taiwan September 2025 registered live births (monthly household registration sta = **8,603** births (2025-09-01..2025-09-30) [keep: ] quote: "9月出生僅8,603人、年減逾27%,為歷年單月第三低的出生人數"
  - p2 Taiwan September 2025 registered births, year-on-year change (percent) = **27.04** % (2025-09-01..2025-09-30) [keep: ] quote: "相比去年9月的出生人數大幅減少27.04%、少了3,189個新生娃"
  - p3 Taiwan September 2025 births, year-on-year decrease in number of births = **3,189** births (2025-09-01..2025-09-30) [keep: ] quote: "相比去年9月的出生人數大幅減少27.04%、少了3,189個新生娃"
  - p4 Taiwan September 2025 crude birth rate (annualized, per 1,000 population) = **4.49** births per 1,000 population (2025-09-01..2025-09-30) [DISCARD: Annualized crude birth rate for September 2025; redundant with the count and requires a population denominator not neede] quote: "今年9月出生數8,603人,約每5.1分鐘出生一個嬰兒,折合年粗出生率為千分之4.49"
  - p5 Taiwan September 2025 births, minutes per birth = **5.1** minutes per birth (2025-09-01..2025-09-30) [DISCARD: Minutes-per-birth restatement of the September 2025 count; adds no information.] quote: "今年9月出生數8,603人,約每5.1分鐘出生一個嬰兒"
  - p6 Taiwan September 2025 deaths (monthly) = **15,000** deaths (2025-09-01..2025-09-30) [DISCARD: Deaths, not births; irrelevant to the target.] quote: "而9月死亡人數約1.5萬人,全國已連續57個月「生不如死」"
  - p7 Taiwan May 2025 deaths (monthly) = **15,387** deaths (2025-05-01..2025-05-31) [DISCARD: Deaths, not births; irrelevant.] quote: "而5月死亡數為15,387人,平均約每2.8分鐘死亡一個人"
  - p8 Taiwan May 2025 crude death rate (annualized, per 1,000 population) = **8.03** deaths per 1,000 population (2025-05-01..2025-05-31) [DISCARD: Crude death rate; irrelevant.] quote: "折合年粗死亡率為千分之8.03,單月死亡比出生多了6,784人"
  - p9 Taiwan May 2025 excess of deaths over births (monthly) = **6,784** persons (2025-05-01..2025-05-31) [DISCARD: Deaths-minus-births excess; not a birth count.] quote: "單月死亡比出生多了6,784人,全台已連續57個月「生不如死」"
  - p10 Taiwan September 2025 in-migrants (monthly) = **79,080** persons (2025-09-01..2025-09-30) [DISCARD: In-migration; irrelevant to births.] quote: "今年全國9月遷入人口僅79,080人,低於遷出人數83,608人"
  - p11 Taiwan September 2025 out-migrants (monthly) = **83,608** persons (2025-09-01..2025-09-30) [DISCARD: Out-migration; irrelevant.] quote: "今年全國9月遷入人口僅79,080人,低於遷出人數83,608人"
  - p12 Taiwan total population at end-September 2025 = **23,317,000** persons (2025-09-30..2025-09-30) [DISCARD: Population level; not needed for a count projection.] quote: "致全國總人口已連21月下跌至2,331.7萬人"
  - p13 Taiwan population at end-2023 (start of 21-month decline) = **23,420,000** persons (2023-12-31..2023-12-31) [DISCARD: Population level; irrelevant.] quote: "使全國總人口自2023年底以來連21月下滑,從2,342萬人一路降至2,331.7萬人"
  - p14 Taiwan working-age population (15-64) at end-September 2025 = **16,000,000** persons (2025-09-30..2025-09-30) [DISCARD: Working-age population; irrelevant.] quote: "「工作年齡人口(15~64歲)」也不及7成,約1,600萬人、占68.6%"
  - p15 Taiwan population aged 65+ at end-September 2025 = **4,616,000** persons (2025-09-30..2025-09-30) [DISCARD: Elderly population; irrelevant.] quote: "65歲以上老年人口數則續增至461.6萬人,佔比19.8%"
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/tag/13920?page=1&type=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/14
  - p16 Taiwan total registered births, September 2025 = **8,603** births (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p17 Taiwan total registered births, August 2025 = **8,464** births (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p18 Taiwan total registered births, July 2025 = **8,939** births (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p19 Taiwan total registered births, October 2025 = **9,458** births (2025-10-01..2025-10-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p20 Taiwan total registered births, November 2025 = **7,946** births (2025-11-01..2025-11-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p21 Taiwan total registered births, December 2025 = **9,027** births (2025-12-01..2025-12-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p22 Taiwan total registered births, January 2025 = **9,495** births (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p23 Taiwan total registered births, February 2025 = **10,407** births (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p24 Taiwan total registered births, March 2025 = **9,388** births (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p25 Taiwan total registered births, April 2025 = **8,684** births (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p26 Taiwan total registered births, May 2025 = **8,433** births (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p27 Taiwan total registered births, June 2025 = **8,968** births (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p28 Taiwan total registered births, full year 2024 = **134,856** births (2024-01-01..2024-12-31) [DISCARD: Duplicate of p44 (2024 total births).] quote: "113 年(1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p29 Taiwan year-on-year percent change in births, 2025 vs 2024 = **-20.05** percent (2025-01-01..2025-12-31) [keep: ] quote: "[(2)-(1)]/(1)×100 -20.05 -0.91 -- -- -- --"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d2 [base_rates] Annual total times September share

Hypothesis: September 2026 births = projected 2026 annual births x September's historical share of annual births (roughly 1/12 adjusted for seasonality); annual projection can come from year-to-date 2026 births annualized.

Queries issued by the searcher: 台灣 2026 出生數 累計 內政部; Taiwan births year to date 2026 monthly statistics; 內政部 2025年9月 出生數 新生兒 統計 去年同月; 2023年 出生數 13萬5571 2024年 13萬4856 內政部 全年新生兒

- `https://www.cardu.com.tw/news/detail.php?64681` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://www.chinatimes.com/cn/realtimenews/20251009002298-260410?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.anntw.com/articles/20261018-Du3C` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National statistics / DGBAS population and birth series

Hypothesis: Alternative official series (DGBAS, National Development Council population projections, Directorate-General of Budget) report monthly or annual births that track MOI registered births with a stable ratio; these can cross-check and fill the level.

Queries issued by the searcher: 行政院主計總處 出生 統計 2026 出生數; 國發會 人口推估 出生數 2026; 內政部 戶政司 出生人數 2026年 每月 統計 7月 8月; 台灣 2026年 1-7月 出生人數 5.4萬 內政部

- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/1
  - p30 Taiwan total fertility rate (TFR) in 2025, per MOI latest statistics = **0.695** births per woman (2025-01-01..2025-12-31) [DISCARD: Duplicate of p33 (2025 TFR 0.695).] quote: "我國總生育率於去(2025)年降至0.695人"
- `https://tw.news.yahoo.com/%E5%8F%B0%E7%81%A3%E4%BA%BA%E5%8F%A3%E6%95%B820%E5%B9%B4%E5%BE%8C%E4%B8%8D%E5%88%B02%E5%8D%83%E8%90%AC-%E9%80%99%E5%B9%B4-%E` -> **snapshot** (snapshot 20260901044610); points raw/verified 15/7
  - p31 Taiwan births, first 7 months of 2026 (cumulative, MOI-based statistic cited by  = **54,000** births (2026-01-01..2026-07-31) [keep: ] quote: "根據目前統計,台灣2026年前7月出生人數僅5.4萬人"
  - p32 Taiwan total fertility rate, 2024 = **0.885** births per woman (2024-01-01..2024-12-31) [DISCARD: 2024 TFR; redundant with the 2025 TFR and annual totals already kept.] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人"
  - p33 Taiwan total fertility rate, 2025 = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人"
  - p34 NDC 2024 projection model: high-case total fertility rate assumption = **1.3** births per woman (2024-01-01..2024-12-31) [DISCARD: NDC high-case TFR assumption; a scenario parameter, not an observation.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p35 NDC 2024 projection model: medium-case total fertility rate assumption = **1** births per woman (2024-01-01..2024-12-31) [DISCARD: NDC medium-case TFR assumption; scenario parameter.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p36 NDC 2024 projection model: low-case total fertility rate assumption = **0.8** births per woman (2024-01-01..2024-12-31) [DISCARD: NDC low-case TFR assumption; scenario parameter.] quote: "原先,國發會2024年提出的人推估模型,高中低分別是將總生育率設定為1.3、1、0.8人"
  - p37 Share of women aged 20-49 currently married, 2025 = **43.5** % (2025-01-01..2025-12-31) [DISCARD: Married-share of women; not usable without age-specific fertility detail.] quote: "台灣20歲至49歲婦女有偶率,從2005年的55.3%,下降至2025年的43.5%"
- `https://fwnews.com.tw/tag/%E6%96%B0%E7%94%9F%E5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mdnkids.com/content.asp?Link_String_=248T00000GDYIDY` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 22 (period_end 2075-12-31 after as_of: 3; scale word 'thousand' not supported by quote or table header: 4; period_end 2026-12-31 after as_of: 14; period_end 2070-12-31 after as_of: 1)

### d4 [forecasts_markets] Official population projections and demographic forecasts

Hypothesis: NDC/DGBAS population projections and any published 2026 birth forecasts give an independent annual anchor; September 2026 can be derived by applying the seasonal share.

Queries issued by the searcher: 國發會 人口推估 2026 出生數; Taiwan population projection 2026 births NDC; 內政部 戶籍統計 2026年 每月 出生數 6月 7月 8月; 2025年 台灣 每月出生數 9月 出生 內政部 統計

- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/1
  - p38 Taiwan total fertility rate (TFR) in 2025, per Ministry of Interior statistics c = **0.695** births per woman (2025-01-01..2025-12-31) [DISCARD: Duplicate of p33 (2025 TFR 0.695).] quote: "依據內政部最新統計,我國總生育率於去(2025)年降至0.695人"
- `https://www3.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.womengroups.org.tw/OnePage.aspx?tid=1&id=5213` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- dropped by code checks: 14 (period_end 2075-12-31 after as_of: 3; period_end 2070-12-31 after as_of: 3; scale word 'thousand' not supported by quote or table header: 4; period_end 2026-12-31 after as_of: 4)

### d5 [related_series] Conception/birth lead-time decomposition

Hypothesis: Births in September 2026 correspond approximately to conceptions around December 2025 (about 38-40 weeks earlier); monthly marriage registrations, contraceptive/abortion proxies, and prior-year birth levels can constrain the expected level via a lagged relationship.

Queries issued by the searcher: 台灣 結婚登記 每月 統計 2025 2026 內政部; Taiwan monthly births 2025 2026 household registration statistics; 114年12月 出生數 結婚對數 戶口統計 內政部; 115年7月 戶口統計 出生數 結婚 內政部 公布

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/15
  - p39 Taiwan registered births, December 2025 (monthly total) = **9,027** births (2025-12-01..2025-12-31) [DISCARD: Duplicate of p21 (December 2025 births).] quote: "23,299,132 11,462,401 11,836,731 9,027 17,450 8,423"
  - p40 Taiwan registered births, November 2025 (monthly total) = **7,946** births (2025-11-01..2025-11-30) [DISCARD: Duplicate of p20 (November 2025 births).] quote: "23,306,085 11,467,137 11,838,948 7,946 14,771 6,825"
  - p41 Taiwan registered births, October 2025 (monthly total) = **9,458** births (2025-10-01..2025-10-31) [DISCARD: Duplicate of p19 (October 2025 births).] quote: "23,310,853 11,470,704 11,840,149 9,458 15,908 6,450"
  - p42 Taiwan registered births, September 2025 (monthly total) = **8,603** births (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p43 Taiwan registered births, full year 2025 = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p44 Taiwan registered births, full year 2024 = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p45 Taiwan registered marriages (couples), December 2025 (monthly total) = **10,816** couples (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p46 Taiwan registered marriages (couples), November 2025 (monthly total) = **8,586** couples (2025-11-01..2025-11-30) [keep: ] quote: "8,586 8,327 259 4.48 1.52 - 4.03 1.23 - 4.38 0.81 -"
  - p47 Taiwan registered marriages (couples), October 2025 (monthly total) = **10,735** couples (2025-10-01..2025-10-31) [keep: ] quote: "10,735 10,428 307 5.42 0.58 4.78 0.48 - 4.37 0.74 -"
  - p48 Taiwan registered marriages (couples), September 2025 (monthly total) = **5,844** couples (2025-09-01..2025-09-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p49 Taiwan registered marriages (couples), full year 2025 = **104,376** couples (2025-01-01..2025-12-31) [keep: ] quote: "there were 104,376 marriages registered in 2025, including 3,305 same-sex marriages"
  - p50 Taiwan registered marriages (couples), full year 2024 = **123,061** couples (2024-01-01..2024-12-31) [keep: ] quote: "2024(1) 123,061 53,469 5.26 2.28"
  - p51 Taiwan registered divorces/terminated marriages (couples), December 2025 (monthl = **4,674** couples (2025-12-01..2025-12-31) [DISCARD: Divorces; irrelevant to the birth count.] quote: "4,674 4,576 98 2.36 0.06 2.39 0.11 2.23 0.05 -"
  - p52 Taiwan registered divorces/terminated marriages (couples), full year 2025 = **52,101** couples (2025-01-01..2025-12-31) [DISCARD: Divorces; irrelevant.] quote: "there were 52,101 divorces or terminated marriages, including 898 same-sex cases"
  - p53 Taiwan crude birth rate, full year 2025 = **4.62** births per 1,000 population (2025-01-01..2025-12-31) [DISCARD: Crude birth rate; redundant with the annual count and needs a population denominator.] quote: "resulting in a crude birth rate of 4.62 per 1,000 population"
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://joelin.cc/p/4372` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [shocks] Policy and calendar effects

Hypothesis: Taiwan's 2025-2026 birth-subsidy expansions (e.g., increased monthly child allowances) and 2026 holiday/registration timing (Mid-Autumn Festival, typhoon closures) may shift the level or registration timing of September 2026 births relative to history.

Queries issued by the searcher: 台灣 育兒津貼 2025 2026 出生 影響; 2026 中秋節 日期 台灣 放假; 2026年 出生人數 內政部 統計 月 出生 增加 生育給付10萬; 內政部 戶政司 出生 統計 2026年7月 新生兒 人數

- `https://fwnews.com.tw/tag/%E6%96%B0%E7%94%9F%E5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ntcunion.org/page/news/show.aspx?num=4536&root=2&page=5&kind=2&lang=TW` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gb.crntt.com/crn-webapp/touch/detail.jsp?coluid=93&kindid=13830&docid=160230405` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.parenting.com.tw/article/5090559` -> **snapshot** (snapshot 20230319085207); points raw/verified 0/0

### b1 [own_history] MOI monthly series

Hypothesis: Obtaining the actual MOI monthly registered-birth counts for January-July 2026 (not just the rounded 54,000 cumulative) would let us fit the 2026 level and month-to-month seasonality directly, replacing the rounded p31 anchor and the 2025-based seasonal factor. This is the single most important missing input.

Queries issued by the searcher: 內政部戶政司 出生數 2026年 月別 統計; ris.gov.tw 戶口統計 出生數 2026 月; ris.gov.tw 人口統計資料 出生數 按月 115年7月 戶口統計; "7月" 新生兒 7906人 內政部 2026 人口連31個月負成長

- `https://statis.moi.gov.tw/micst/webMain.aspx?k=menum` -> **snapshot** (snapshot 20260814004253); points raw/verified 0/0
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160245185` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] seasonality

Hypothesis: A multi-year September seasonal factor (September births relative to adjacent months) from 2019-2024 MOI data would sharpen the seasonal adjustment applied to the 2026 level; currently only 2025 monthly data are available, so the September factor rests on one year.

Queries issued by the searcher: 內政部 歷年 出生數 月別 統計; Taiwan monthly births 2019 2020 2021 2022 2023 2024 by month statistics; ris.gov.tw 歷年全國人口統計資料 出生 按月別 2019 2020 2021 2022 2023 2024 出生數; "現住人口動態登記" "按月別分" 出生數 表4 內政部 統計月報

- `https://www.ris.gov.tw/documents/html/5/2/popudata-quart-pub.html` -> **snapshot** (snapshot 20260902055958); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2023.pdf` -> **snapshot** (snapshot 20251104063418); points raw/verified 15/14
  - p54 Taiwan registered births, September 2023 (monthly total) = **10,717** births (2023-09-01..2023-09-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p55 Taiwan registered births, August 2023 (monthly total) = **12,016** births (2023-08-01..2023-08-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p56 Taiwan registered births, October 2023 (monthly total) = **13,068** births (2023-10-01..2023-10-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p57 Taiwan registered births, July 2023 (monthly total) = **10,891** births (2023-07-01..2023-07-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p58 Taiwan registered births, January 2023 (monthly total) = **10,948** births (2023-01-01..2023-01-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p59 Taiwan registered births, February 2023 (monthly total) = **10,113** births (2023-02-01..2023-02-28) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p60 Taiwan registered births, March 2023 (monthly total) = **12,506** births (2023-03-01..2023-03-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p61 Taiwan registered births, April 2023 (monthly total) = **9,643** births (2023-04-01..2023-04-30) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p62 Taiwan registered births, May 2023 (monthly total) = **11,809** births (2023-05-01..2023-05-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p63 Taiwan registered births, June 2023 (monthly total) = **11,009** births (2023-06-01..2023-06-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p64 Taiwan registered births, November 2023 (monthly total) = **11,272** births (2023-11-01..2023-11-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p65 Taiwan registered births, December 2023 (monthly total) = **11,579** births (2023-12-01..2023-12-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p66 Taiwan total registered births, full year 2022 = **138,986** births (2022-01-01..2022-12-31) [keep: ] quote: "111 年(1) 138,986 207,230 -68,244 5.96 8.89 -2.93"
  - p67 Taiwan September 2023 seasonally adjusted crude birth rate (annual basis) = **5.64** births per 1,000 population (2023-09-01..2023-09-30) [keep: ] quote: "5.62 6.13 6.00 5.53 6.15 6.02 5.73 6.26 5.64 5.99"
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMTQ3OC9lMzI2MmFmNS0zNjM4LTRiNmYtYjA0MS1lZjYzMDA0YThkZGQucGRm&n=MTEzMTIucGRm&` -> **snapshot** (snapshot 20250424204054); points raw/verified 15/8
  - p68 Taiwan (ROC) registered live births, September 2024 (monthly) = **11,792** births (2024-09-01..2024-09-30) [keep: ] quote: "11,643 11,792 12,070 12,557 12,496"
  - p69 Taiwan (ROC) registered live births, August 2024 (monthly) = **11,643** births (2024-08-01..2024-08-31) [keep: ] quote: "11,643 11,792 12,070 12,557 12,496"
  - p70 Taiwan (ROC) registered live births, October 2024 (monthly) = **12,070** births (2024-10-01..2024-10-31) [keep: ] quote: "11,643 11,792 12,070 12,557 12,496"
  - p71 Taiwan (ROC) registered live births, November 2024 (monthly) = **12,557** births (2024-11-01..2024-11-30) [keep: ] quote: "11,643 11,792 12,070 12,557 12,496"
  - p72 Taiwan (ROC) registered live births, January 2024 (monthly) = **11,023** births (2024-01-01..2024-01-31) [keep: ] quote: "134,856 11,023 9,663 10,827 10,753 11,168 10,440 10,424 11,643 11,792 12,070 12,557 12,496"
  - p73 Taiwan (ROC) registered live births, February 2024 (monthly) = **9,663** births (2024-02-01..2024-02-29) [keep: ] quote: "134,856 11,023 9,663 10,827 10,753 11,168 10,440 10,424 11,643 11,792 12,070 12,557 12,496"
  - p74 Taiwan (ROC) registered live births, March 2024 (monthly) = **10,827** births (2024-03-01..2024-03-31) [keep: ] quote: "134,856 11,023 9,663 10,827 10,753 11,168 10,440 10,424 11,643 11,792 12,070 12,557 12,496"
  - p75 Taiwan (ROC) registered live births, April 2024 (monthly) = **10,753** births (2024-04-01..2024-04-30) [keep: ] quote: "134,856 11,023 9,663 10,827 10,753 11,168 10,440 10,424 11,643 11,792 12,070 12,557 12,496"
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMzMzOC9hNmM4ZmJlOS1iOTc4LTQ1OGYtOGM0MS1kZTk5ZmZiMmIxNTYucGRm&n=MTE1MDQucGRm&` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (value_as_written not in quote as a whole number: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7)

### b3 [shocks] policy/timing

Hypothesis: Evidence on the 2025-2026 birth-subsidy expansion's effect on registration timing and on any September 2026 holiday/typhoon registration disruptions would bound the deviation of September 2026 from the trend projection.

Queries issued by the searcher: Taiwan birth subsidy 2026 effect births 育兒津貼 2026 出生數 影響; 台灣 2026 育兒津貼 擴大 出生登記 時程; Taiwan monthly births September 2025 Ministry of Interior household registration; 2026年1月1日 每胎10萬 生育補助 出生登記 影響 2025年12月 出生數; "10萬元" 生育補助 2026 上路 新生兒 登記 2025 12月; Taiwan births July 2026 7906 MOI August 10 2026; 台灣 2026年7月 出生數 7906 內政部 戶籍統計

- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=f5b0d41d65534ee4858fb5c2ce865845` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=d2c128aba0fb4645bdaeb00f57a34c48` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/campus/20251010000241-261509?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gb.crntt.com/crn-webapp/touch/detail.jsp?coluid=93&kindid=13830&docid=160230405` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'taiwan birth rate', 'september births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p16', 'p42'] All three give September 2025 registered births = 8,603; p1 is a news report, p16/p42 are MOI/RIS monthly-statistics extracts. Same underlying MOI measurement, so this is one source, not three indepen
- corroborating: ['p2', 'p3'] Both describe the same September 2025 year-on-year decline (-27.04%, -3,189 births); internally consistent with 8,603 vs ~11,792 in September 2024. Same article, same source.
- corroborating: ['p4', 'p5', 'p53'] Crude birth rate and minutes-per-birth are arithmetic restatements of the 8,603 monthly count and population; they add no independent information about the level.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p43'] Monthly 2025 values from the same MOI/RIS table; they sum consistently to the 107,812 annual total (p43). This is the primary series for level and seasonality.
- corroborating: ['p28', 'p44'] Duplicate statements of 2024 annual births = 134,856; same source, one data point.
- corroborating: ['p29', 'p43', 'p44'] The -20.05% change is consistent with 107,812 vs 134,856; same MOI table.
- corroborating: ['p30', 'p33', 'p38'] All three report 2025 TFR = 0.695 from MOI statistics; p30/p38 are NDC restatements of the same MOI figure, not independent measurements.
- corroborating: ['p31'] 2026 first-7-month births ~54,000 is consistent with a continuation of the 2025 monthly level (~9,000/month) and with the steep 2025-2026 decline; it is the key 2026 anchor but is a rounded news citat
- conflicting: ['p34', 'p35', 'p36'] NDC 2024 projection TFR assumptions (0.8-1.3) are far above realised 0.695; they are scenario parameters, not forecasts of the actual level, and should not be used as central anchors.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50'] Marriage series is internally consistent (monthly sums to annual). It is a lagged conception proxy only; the December 2025 conception window maps to September 2026 births, but the marriage-to-birth li
- corroborating: ['p39', 'p40', 'p41', 'p42'] Oct-Dec 2025 monthly births duplicate p19-p21; same source.
- corroborating: ['p6', 'p7', 'p8', 'p9'] Death statistics are internally consistent but irrelevant to the birth target except as demographic context.
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Migration and population-structure figures are consistent with each other but only contextual; they do not directly determine September 2026 births.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p16', 'p42'] Same MOI September 2025 registered-birth count (8,603) reported by a news outlet and by the official household-registration table; they share one underlying measurement, so this is one fact, not three
- corroborating: ['p2', 'p3', 'p68'] September 2025 was 27.04% / 3,189 births below September 2024; 8,603 + 3,189 = 11,792 matches p68, so the YoY figures and the 2024 level are internally consistent.
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] One continuous official 2025 monthly series from the same MOI table; mutually consistent and summing to the 107,812 annual total in p43.
- corroborating: ['p43', 'p44', 'p29'] 2025 total 107,812 vs 2024 total 134,856 implies about -20.05%, matching the stated YoY change; consistent annual anchors.
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65'] Complete 2023 monthly MOI series; used only for the September seasonal shape, not for the 2026 level.
- corroborating: ['p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75'] Complete 2024 monthly MOI series; September 2024 (11,792) is the base for the 2025 YoY drop and gives a second year of September seasonality.
- conflicting: ['p31', 'p43'] 2026 first-7-month cumulative of about 54,000 implies a monthly pace near 7,700, well below the 2025 monthly average of about 8,984; this is a genuine level decline, not a definitional conflict, and p
- corroborating: ['p33', 'p29'] TFR falling from 0.885 (2024) to 0.695 (2025) is consistent with the ~20% annual birth decline; both point to a continuing low 2026 level.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50'] Marriage registrations fell ~15% in 2025 vs 2024; December 2025 marriages (p45) are the conception-window proxy for September 2026 births, but the marriage-to-birth link is weak and lagged, so this is

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September seasonal factor relative to the 2026 monthly mean | 0.97 | 0.88..1.07 | 0.6861..1.372 (widened) | ratio | unused | September is typically slightly below the annual monthly mean in Taiwan's registration series: 2025 September (8,603) ≈ 0.96 of the 2025 monthly mean (8,984); 2024 September (11,792) ≈ 1.05 of the 2024 mean (11,238); 2023 September (10,717) ≈ 0.95 of the 2023 mean. Average ≈ 0.97, range spans observ | The 2026 monthly level is roughly flat across the year and September follows the historical seasonal shape. | Evidence that 2026 registration timing was shifted by holiday/typhoon closures or subsidy-driven registration bunching. |
| a2 | 2026 vs 2025 year-over-year birth change factor | 0.86 | 0.78..0.94 | 0.7659..0.9573 (widened) | ratio | m2 (m2) | 2026 first-7-month cumulative (~54,000, p31) implies a monthly pace near 7,700 versus 2025's ~8,984 monthly average, a ratio near 0.86; the 2025 TFR drop (p33) and falling marriages (p49 vs p50) support a continued decline rather than a rebound. Range reflects the rounding of p31 and uncertainty in  | The 2026 level decline relative to 2025 persists through September. | Monthly 2026 MOI data showing a level near or above 2025's monthly average. |
| a3 | Months in the first-7-month cumulative window | 7 | 7..7 | 4.95..9.899 (widened) | months | unused | p31 covers January through July 2026, exactly seven calendar months; this is a calendar constant needed to convert the cumulative to a monthly mean. | p31 is the cumulative over January-July 2026. | Evidence that p31 covers a different number of months. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_naive | 8,603 |  | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 7,369 | ['p16'] / ['a2'] | [] |  | 0.50 | equal |  |
| m3 | formula_mc | n/a | ['p31'] / ['a1', 'a3'] | [] |  | 0.00 |  | formula: numeric constant 12 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the uni |

Result: central **7,962** birth, 80% interval [5,779, 10,969] birth, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for registered live births in Taiwan during September 2026 (registration-date basis, MOI monthly household registration statistics) is 7,962 birth (80% model-based interval 5,779 to 10,969 birth).

Two methods were combined at 50% and 50%: a naive seasonal anchor using September 2025 births of 8,603 births, and a seasonal-anchor route scaling that anchor by an assumed 2026-vs-2025 change factor of 0.86 (range 0.7659 to 0.9573). The third method was unusable. The only observed inputs are 8,603 births and the first-[n]-month cumulative 54,000 births; the year-over-year factor is an assumption, not an observation. The weighting reflects the code's fixed scheme, not demonstrated backtest accuracy.

The main risk is a shift in registration timing or a change in the 2026 decline pace, which would move the scaled anchor. Better evidence would be actual monthly 2026 birth counts through August and any partial September registration data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a2 2026 vs 2025 year-over-year birth change factor: 0.86 ratio, range 0.7659 to 0.9573 (range widened by code); used by m2. Overturned by: Monthly 2026 MOI data showing a level near or above 2025's monthly average.

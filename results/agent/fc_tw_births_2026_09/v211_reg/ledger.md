# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan (Republic of China) during September 2026, as counted in the Ministry of the Interior's monthly household registration statistics (births registered in the month, by date of registration) | unit births registered in September 2026 | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior, Republic of China (Taiwan) — Department of Household Registration, monthly statistics on household registration (人口統計/出生登記)

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household registration series

Hypothesis: September 2026 births ≈ recent monthly level adjusted for the September seasonal factor and the ongoing downward trend. September typically shows a modest seasonal pattern relative to August; the dominant driver is the multi-year decline in Taiwan births.

Queries issued by the searcher: 內政部 戶政司 出生登記 統計 月別 2026; Taiwan monthly births household registration statistics 2025 2026 內政部 出生數; ris.gov.tw 戶政司 人口統計 出生 歷年 月別 統計表 下載; 2025年9月 出生數 8603 內政部 戶口統計 新生兒

- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/html/5/2/1/674.html` -> **snapshot** (snapshot 20260801140833); points raw/verified 0/0
- `https://www.chinatimes.com/cn/search/%e7%b2%97%e5%87%ba%e7%94%9f%e7%8e%87?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [base_rates] Seasonality and month-to-month ratios

Hypothesis: September births = August births × (September/August ratio). The ratio is fairly stable historically (often slightly below or near 1.0); applying a historical average ratio to the latest observed August 2026 value gives a direct estimate.

Queries issued by the searcher: 台灣 出生數 8月 2026 內政部 戶政統計; Taiwan births August 2026 monthly household registration statistics; 內政部戶政司 歷年 每月 出生數 統計 月別 2015 2025 表; 台灣 歷年 各月 出生人數 統計表 1月 2月 3月 4月 5月 6月 7月 8月 9月 10月 11月 12月

- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS84NDkyLzEwODA2LnBkZg%3d%3d&n=MTA4MDYucGRm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1904770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pttweb.cc/bbs/home-sale/M.1789960451.A.3ED` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] National statistics agency / DGBAS population and birth data

Hypothesis: DGBAS and National Development Council publish monthly/quarterly birth counts and population projections that can cross-check and extend the MOI series; the September 2026 value should be consistent with the same underlying registration flow.

Queries issued by the searcher: 行政院主計總處 出生數 月 2026; Taiwan monthly births 2026 Ministry of Interior household registration statistics; 內政部戶政司 人口統計 出生登記 每月 出生數 統計表 115年; 國發會 中華民國人口推估 2026 出生數 推估 每年

- `https://statis.moi.gov.tw/micst/webMain.aspx?k=menum` -> **snapshot** (snapshot 20260814004253); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/14
  - p1 Taiwan (ROC) total registered births, full year 2024 = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "113 年(1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p2 Year-on-year percent change in Taiwan registered births, 2025 vs 2024 = **-20.05** percent (2025-01-01..2025-12-31) [keep: ] quote: "[(2)-(1)]/(1)×100 -20.05 -0.91 -- -- -- --"
  - p3 Taiwan crude birth rate, full year 2025 = **4.62** births per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "2025 (2) 107,812 200,268 -92,456 4.62 8.58 -3.96"
  - p4 Taiwan total registered births, September 2025 = **8,603** births (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p5 Taiwan total registered births, October 2025 = **9,458** births (2025-10-01..2025-10-31) [keep: ] quote: "23,310,853 11,470,704 11,840,149 9,458 15,908 6,450 - - 3.26"
  - p6 Taiwan total registered births, November 2025 = **7,946** births (2025-11-01..2025-11-30) [keep: ] quote: "23,306,085 11,467,137 11,838,948 7,946 14,771 6,825 - - 3.56"
  - p7 Taiwan total registered births, December 2025 = **9,027** births (2025-12-01..2025-12-31) [keep: ] quote: "23,299,132 11,462,401 11,836,731 9,027 17,450 8,423 - - 4.26"
  - p8 Taiwan total registered births, January 2025 = **9,495** births (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p9 Taiwan total registered births, February 2025 = **10,407** births (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p10 Taiwan total registered births, March 2025 = **9,388** births (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p11 Taiwan total registered births, April 2025 = **8,684** births (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p12 Taiwan total registered births, May 2025 = **8,433** births (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p13 Taiwan total registered births, June 2025 = **8,968** births (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p14 Taiwan total registered births, July 2025 = **8,939** births (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
- `https://news.pts.org.tw/tag/13920?page=1&type=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260610002909-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d4 [related_series] Upstream: births by date of occurrence and maternal age/parity

Hypothesis: Births occurring in September 2026 were largely conceived around December 2025–January 2026; conception proxies (marriages, first-birth timing) and the number of women of childbearing age constrain the level. Occurrence-based counts approximate registration-based counts with a small lag.

Queries issued by the searcher: 台灣 出生登記 月別 統計 2026 內政部 戶政司; 台灣 結婚登記 月別 統計 2025 2026 內政部; 內政部 戶政司 7月新生兒 7,906 2026 人口統計; 台灣 25-39歲 女性 人口數 2026 統計 年齡別

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p15 Taiwan total population, July 2026 = **23,235,002** people (2026-07-01..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人"
  - p16 Taiwan births registered in July 2026 (monthly count) = **7,906** births (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人"
  - p17 Taiwan crude birth rate, annualized, July 2026 = **4.01** births per 1,000 people (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為4.01‰"
  - p18 Taiwan births registered in May 2026 (monthly count) = **6,832** births (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p19 Taiwan births registered in June 2026 (monthly count) = **7,324** births (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p20 Year-on-year change in Taiwan July births, 2026 vs 2025 = **1,033** births (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p21 Year-on-year percent decline in Taiwan July births, 2026 vs 2025 = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p22 Taiwan deaths in July 2026 (monthly count) = **17,119** deaths (2026-07-01..2026-07-31) [DISCARD: Deaths are irrelevant to the births target; no conversion to births exists.] quote: "7月死亡人數則為1萬7119人"
  - p23 Taiwan marriage registrations in July 2026 (couples) = **7,150** couples (2026-07-01..2026-07-31) [keep: ] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%"
  - p24 Share of July 2026 Taiwan marriages that were same-sex = **3.5** % (2026-07-01..2026-07-31) [DISCARD: Same-sex share of marriages is not a births input and adds no information beyond p23.] quote: "7月全台共有7150對,同婚占3.5%"
  - p25 Taiwan divorces in July 2026 (couples) = **4,450** couples (2026-07-01..2026-07-31) [DISCARD: Divorces are not a births input.] quote: "離婚對數為4450對,同婚占1.7%"
  - p26 Share of Taiwan population aged 65+ at end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [DISCARD: 65+ share is contextual aging stock, not a births driver usable in any executable route.] quote: "65歲以上人口占20.54%"
  - p27 Share of Taiwan population aged 15-64 at end of July 2026 = **68.15** % (2026-07-31..2026-07-31) [DISCARD: 15-64 share is too broad to constrain births; redundant with p15/p28.] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p28 Share of Taiwan population aged 0-14 at end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [DISCARD: 0-14 share is a stock of children, not a flow input.] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p29 Consecutive months of Taiwan population decline through July 2026 = **31** months (2026-07-31..2026-07-31) [DISCARD: Months of population decline is descriptive context, not a births input.] quote: "是連續31個月出現人口負成長"
- `https://www.chinatimes.com/newspapers/20260811000189-260210` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1887028` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [forecasts_markets] Official projections and demographic forecasts

Hypothesis: NDC/DGBAS 2026 annual birth projections divided by 12, adjusted for September share, provide an independent anchor; forecast error is mainly trend, not seasonality.

Queries issued by the searcher: 國發會 人口推估 2026 出生數 2024-2070; Taiwan 2026 births forecast annual projection NDC; 2026年 出生數 預估 台灣 國發會; 內政部 2026 1-7月 出生數 新生兒 統計; 2026年7月 出生人數 內政部 統計 累計; site:ris.gov.tw 2026 出生 統計 月; 2026 前7月 新生兒 出生數 台灣

- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/1
  - p30 Taiwan total fertility rate (TFR) in 2025, per Ministry of Interior statistics c = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "依據內政部最新統計,我國總生育率於去(2025)年降至0.695人"
- `https://pop-proj.ndc.gov.tw/Custom_Fast_Statistics_Search.aspx?d=H08&m=81&n=7&sms=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 11/3
  - p31 Average age of first-time birth mothers in Taiwan (latest) = **31.8** years of age (not stated (page dated 2026-08-28)) [DISCARD: First-birth mother age is descriptive; no executable conversion to a monthly count.] quote: "首胎生母平均年齡31.8歲"
  - p32 Increase in average age of first-time birth mothers since 2005 = **4.1** years of age (not stated (page dated 2026-08-28)) [DISCARD: Change in first-birth age is descriptive; no executable conversion.] quote: "相較2005年增加4.1歲"
  - p33 Projected decline in Taiwan working-age population over the next 50 years (share = **0.6667** as written "三分之二", value check pending share of working-age population (not stated (page dated 2026-08-28)) [DISCARD: 50-year working-age projection is far outside the target horizon and not a births input.] quote: "未來50年,工作年齡人口總量將減少近三分之二"
- `https://rwdnews.sanlih.com.tw/news/1897905` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 22 (period_end 2075-12-31 after as_of: 5; scale word 'thousand' not supported by quote or table header: 4; period_end 2026-12-31 after as_of: 10; period_end 2045-12-31 after as_of: 1; period_end 2055-12-31 after as_of: 1; period_end 2037-12-31 after as_of: 1)

### d6 [shocks] Calendar and policy effects

Hypothesis: 2026 is the Year of the Horse (lunar), which in Taiwan has historically been associated with slightly higher birth numbers than adjacent zodiac years; also check for any 2026 policy (childcare subsidies, marriage incentives) that could shift registrations.

Queries issued by the searcher: 台灣 龍年 2024 出生數 效應 內政部; Taiwan birth zodiac year effect dragon year 2024 births; 好孕三方案 2026年1月1日 生育補助 每胎10萬元 行政院; 2025年 台灣 出生數 內政部 每月 統計 1月 2月 3月

- `https://ocacnews.net/article/388559` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20250110003323-260407` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.post.gov.tw/post/FileCenter/post_ww2/ad/ad_linkpage/1141003.htm` -> **snapshot** (snapshot 20260824074947); points raw/verified 15/14
  - p34 Birth allowance plus subsidy per birth under expanded fertility subsidy (effecti = **100,000** TWD per birth (2026-01-01..2026-01-01) [keep: ] quote: "115年1月1日起 每胎生育給付加補助至10萬元"
  - p35 IVF subsidy for first application per parity, age under 39 (effective 2025-11-01 = **150,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: IVF subsidy amount; no quantified births effect and redundant with the policy cluster.] quote: "各胎首次申請10萬元→15萬元"
  - p36 IVF subsidy for first application per parity, age under 39, previous amount = **100,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: Previous IVF amount; redundant with p35.] quote: "各胎首次申請10萬元→15萬元"
  - p37 IVF subsidy for 2nd-3rd application per parity, age under 39, new amount = **100,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: IVF subsidy amount; no quantified births effect.] quote: "各胎第2-3次申請6萬元→10萬元"
  - p38 IVF subsidy for 2nd-3rd application per parity, age under 39, previous amount = **60,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: Previous IVF amount; redundant with p37.] quote: "各胎第2-3次申請6萬元→10萬元"
  - p39 IVF subsidy for 4th-6th application per parity, age under 40 = **60,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: IVF subsidy amount; no quantified births effect.] quote: "各胎第4-6次申請6萬元(未滿40歲)"
  - p40 IVF subsidy for first application per parity, age 39 to under 45, new amount = **130,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: IVF subsidy amount; no quantified births effect.] quote: "各胎首次申請10萬元→13萬元"
  - p41 IVF subsidy for first application per parity, age 39 to under 45, previous amoun = **100,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: Previous IVF amount; redundant with p40.] quote: "各胎首次申請10萬元→13萬元"
  - p42 IVF subsidy for 2nd-3rd application per parity, age 39 to under 45, new amount = **80,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: IVF subsidy amount; no quantified births effect.] quote: "各胎第2-3次申請6萬元→8萬元"
  - p43 IVF subsidy for 2nd-3rd application per parity, age 39 to under 45, previous amo = **60,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: Previous IVF amount; redundant with p42.] quote: "各胎第2-3次申請6萬元→8萬元"
  - p44 Maximum IVF subsidy for low- and middle-low-income households, any age or parity = **150,000** TWD per application (2025-11-01..2025-11-01) [DISCARD: Low-income IVF cap; no quantified births effect.] quote: "低收及中低收入戶,不分年齡、胎次,最高補助15萬元"
  - p45 Maximum medical fertility preservation subsidy per egg retrieval (effective 2025 = **70,000** TWD per retrieval (2025-09-01..2025-09-01) [DISCARD: Fertility-preservation subsidy; no quantified births effect.] quote: "114年9月1日起 取卵最高補助7萬元/次"
  - p46 Number of embryos implanted per cycle, age under 39 = **1** embryos per implantation (2025-11-01..2025-11-01) [DISCARD: Embryo implantation protocol; not a births input.] quote: "胚胎植入數1個"
  - p47 Number of embryos implanted per cycle, age 39 to under 45 = **2** embryos per implantation (2025-11-01..2025-11-01) [DISCARD: Embryo implantation protocol; not a births input.] quote: "胚胎植入數2個"
- `https://www.pan-asia.com.tw/News.aspx?nID=139706&page=10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (scale word '千' not supported by quote or table header: 1)

### b1 [own_history] MOI monthly registration series

Hypothesis: Obtaining the actual August 2026 monthly birth count (published early September 2026) would let the September/August ratio route (d2) run on the latest adjacent month rather than extrapolating from July; this is the single most valuable missing input because the level is dominated by the recent trend.

Queries issued by the searcher: 內政部 戶政司 出生登記 115年8月 出生人數; ris.gov.tw 人口統計 出生登記 115年8月; "115年8月" 戶口統計資料分析 內政部 9月8日 公布; Taiwan August 2026 births 7,492 monthly household registration September 2026 preliminary

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)']; no pages fetched**


### b2 [base_rates] Seasonal ratio history

Hypothesis: A multi-year table of September/August registration ratios (2015-2025) would quantify the seasonal factor and its stability, converting the latest observed level into a September estimate with a defensible ratio rather than an assumed one.

Queries issued by the searcher: 內政部 出生人數 月別 統計 歷年 台灣 每月出生數; Taiwan monthly births by month 2015 2025 statistics Department of Household Registration; 內政部統計月報 現住人口動態登記 按月別分 出生人數 統計表 歷年; "出生登記" 月份 統計 台灣 2024年9月 出生人數 1萬 內政部 每月; ris.gov.tw 人口統計資料 表 出生 按月別 歷年 中華民國人口統計年刊 表4

- `https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=53338829-db38-4ddb-9089-755e9f0c1c10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stats.moe.gov.tw/files/analysis/115_st_report.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS83MTg0LzEwNDEwLnBkZg%3D%3D&n=MTA0MTAucGRm&icon=..pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stats.moe.gov.tw/files/analysis/113_st_report.pdf` -> **snapshot** (snapshot 20250903191215); points raw/verified 15/15
  - p48 Taiwan (Republic of China) live births registered in September 2023 (monthly cou = **10,717** births (2023-09-01..2023-09-30) [keep: ] quote: "9月 Sept. 10,717 0.46 5,658 5,059 14,610 0.62 8,480 6,130"
  - p49 Taiwan (Republic of China) live births registered in August 2023 (monthly count, = **12,016** births (2023-08-01..2023-08-31) [keep: ] quote: "8月 Aug. 12,016 0.51 6,267 5,749 17,139 0.73 9,983 7,156"
  - p50 Taiwan (Republic of China) live births registered in January 2023 (monthly count = **10,948** births (2023-01-01..2023-01-31) [keep: ] quote: "1月 Jan. 10,948 0.47 5,639 5,309 17,770 0.76 10,267 7,503"
  - p51 Taiwan (Republic of China) live births registered in February 2023 (monthly coun = **10,113** births (2023-02-01..2023-02-28) [keep: ] quote: "2月 Feb. 10,113 0.43 5,203 4,910 18,506 0.79 10,749 7,757"
  - p52 Taiwan (Republic of China) live births registered in March 2023 (monthly count,  = **12,506** births (2023-03-01..2023-03-31) [keep: ] quote: "3月 Mar. 12,506 0.54 6,481 6,025 20,572 0.88 12,001 8,571"
  - p53 Taiwan (Republic of China) live births registered in April 2023 (monthly count,  = **9,643** births (2023-04-01..2023-04-30) [keep: ] quote: "4月 Apr. 9,643 0.41 4,989 4,654 15,572 0.67 8,963 6,609"
  - p54 Taiwan (Republic of China) live births registered in May 2023 (monthly count, 11 = **11,809** births (2023-05-01..2023-05-31) [keep: ] quote: "5月 May 11,809 0.51 6,055 5,754 17,530 0.75 10,114 7,416"
  - p55 Taiwan (Republic of China) live births registered in June 2023 (monthly count, 1 = **11,009** births (2023-06-01..2023-06-30) [keep: ] quote: "6月 June 11,009 0.47 5,793 5,216 17,415 0.75 10,056 7,359"
  - p56 Taiwan (Republic of China) live births registered in July 2023 (monthly count, 1 = **10,891** births (2023-07-01..2023-07-31) [keep: ] quote: "7月 July 10,891 0.47 5,632 5,259 17,992 0.77 10,352 7,640"
  - p57 Taiwan (Republic of China) live births registered in October 2023 (monthly count = **13,068** births (2023-10-01..2023-10-31) [keep: ] quote: "10月 Oct. 13,068 0.56 6,755 6,313 16,594 0.71 9,615 6,979"
  - p58 Taiwan (Republic of China) live births registered in November 2023 (monthly coun = **11,272** births (2023-11-01..2023-11-30) [keep: ] quote: "11月 Nov. 11,272 0.48 5,838 5,434 15,965 0.68 9,100 6,865"
  - p59 Taiwan (Republic of China) live births registered in December 2023 (monthly coun = **11,579** births (2023-12-01..2023-12-31) [keep: ] quote: "12月 Dec. 11,579 0.49 5,917 5,662 15,703 0.67 9,174 6,529"
  - p60 Taiwan (Republic of China) total live births in calendar year 2023 (112年) = **135,571** births (2023-01-01..2023-12-31) [keep: ] quote: "112年 2023 135,571 5.81 70,227 65,344 205,368 8.80 118,854 86,514"
  - p61 Taiwan (Republic of China) total live births in calendar year 2022 (111年) = **138,986** births (2022-01-01..2022-12-31) [keep: ] quote: "111年 2022 138,986 5.96 72,097 66,889 207,230 8.89 119,920 87,310"
  - p62 Taiwan (Republic of China) total live births in calendar year 2021 (110年) = **153,820** births (2021-01-01..2021-12-31) [keep: ] quote: "110年 2021 153,820 6.55 79,513 74,307 183,732 7.83 106,877 76,855"

### b3 [forecasts_markets] NDC/DGBAS 2026 projection

Hypothesis: The NDC/DGBAS 2026 annual births projection (or a 2026 monthly path) would provide an independent anchor for the annual level, letting the September share of the year be applied; this resolves whether the recent 6,800-7,900 monthly range is the true 2026 level.

Queries issued by the searcher: 國發會 2026 出生數 推估; 國發會 人口推估 2026 出生數 預估 台灣; 國發會 中華民國人口推估（2026年至2075年） 新聞稿 出生數 9.4萬; 內政部 戶政司 出生登記 2026年 每月 出生數 統計

- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/1
  - p63 Taiwan total fertility rate (TFR) in 2025, per Ministry of Interior statistics c = **0.695** births per woman (total fertility rate) (2025-01-01..2025-12-31) [DISCARD: Exact duplicate of p30 (same TFR 0.695 from the same NDC/MOI citation); redundant copy.] quote: "我國總生育率於去(2025)年降至0.695人"
- `https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzEwL3JlbGZpbGUvNjIwMi80MDQwNy8xMzRmMDVhZS1lMDA4LTQ5YTMtYjlmMS03OTJiNTRiMzIzOWUucGRm&n=5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1897905` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 11/2
  - p64 Average age of first-time mothers in Taiwan (latest) = **31.8** years of age (not stated (page dated 2026-08-28)) [keep: ] quote: "首胎生母平均年齡31.8歲"
  - p65 Increase in average age of first-time mothers since 2005 = **4.1** years of age (not stated (page dated 2026-08-28)) [keep: ] quote: "相較2005年增加4.1歲"
- dropped by code checks: 23 (period_end 2075-12-31 after as_of: 5; period_end 2070-12-31 after as_of: 3; scale word 'thousand' not supported by quote or table header: 4; period_end 2026-12-31 after as_of: 7; period_end 2045-12-31 after as_of: 1; period_end 2055-12-31 after as_of: 1; number: no number in value_as_written: 1; period_end 2037-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'taiwan birth rate', 'september 2026 births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3'] All from the same MOI/ris.gov.tw annual household-registration table (2024 births 134,856; 2025 births 107,812 implied by -20.05% and stated directly; 2025 CBR 4.62). They are one measurement system, 
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] Monthly 2025 registration counts from the same MOI table; sum to the 2025 annual total (107,812). Provide the September seasonal shape and the 2025 monthly baseline. Same source as p1-p3, so not indep
- corroborating: ['p16', 'p17', 'p18', 'p19', 'p20', 'p21'] News report of MOI monthly figures for May-July 2026; internally consistent (7,906 July births, 4.01‰ annualized CBR, -1,033 / -11.56% YoY vs July 2025's 8,939). Same underlying MOI registration flow 
- corroborating: ['p15', 'p26', 'p27', 'p28', 'p29'] Population stock and age structure from the same July 2026 MOI release; consistent with a shrinking, aging population. Contextual only.
- corroborating: ['p23', 'p24', 'p25'] July 2026 marriage/divorce counts from the same release; marriage is a weak leading indicator of births ~9-12 months later, not a direct input.
- corroborating: ['p30', 'p31', 'p32', 'p33'] NDC/新闻 commentary on TFR 0.695 (2025) and rising first-birth age; consistent with the steep decline but not a monthly level.
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47'] Policy parameters (birth allowance, IVF subsidies) effective 2025-2026. Directionally pro-natalist but no quantified monthly effect; usable only as a qualitative upside consideration.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3'] All from the same MOI/ris.gov.tw annual household-registration table: 2024 births 134,856, 2025 down 20.05% to 107,812 (crude rate 4.62). Internally consistent (134,856 × 0.7995 ≈ 107,812) but a singl
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] Same MOI monthly registration table for 2025; the twelve monthly values sum to the 107,812 annual total in p3, confirming they are the same registration-flow definition as the target. p4 (Sept 2025 = 
- corroborating: ['p16', 'p18', 'p19', 'p20', 'p21'] News report of MOI monthly counts: May 6,832, June 7,324, July 7,906. July YoY decline of 1,033 (11.56%) is consistent with July 2025 = 8,939 (p14): 8,939 − 1,033 = 7,906. Same registration definition
- corroborating: ['p16', 'p17', 'p15'] July 2026 births 7,906 with annualized crude rate 4.01‰ and population 23,235,002 are mutually consistent (7,906×12/23.235M ≈ 4.08‰, close to 4.01‰). Confirms the 2026 level is well below 2025.
- corroborating: ['p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60'] MOE statistics monthly live-birth registrations for 2023, summing to the 2023 annual total 135,571 (p60). Same registration concept, different vintage/source table; usable for the September/August sea
- corroborating: ['p60', 'p61', 'p62'] MOE annual live births 2021-2023 (153,820; 138,986; 135,571) show the multi-year decline; consistent in direction with the MOI 2024-2025 series (p1, p3) though from a different table.
- redundant: ['p30', 'p63'] p30 and p63 are the same TFR 0.695 figure from the same NDC citation of MOI statistics; p63 is a duplicate and adds no information.
- corroborating: ['p64', 'p65'] Average age of first-time mothers 31.8 and +4.1 years since 2005 are internally consistent context; they constrain the tempo effect but do not give a monthly level.
- contextual: ['p34'] Expanded fertility subsidy (NT$100,000 per birth from 2026-01) is a policy shock that could support registrations; direction is upward but magnitude unquantified, so it is context for the trend assump

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September/August registration ratio | 0.98 | 0.9..1.06 | 0.6907..1.381 (widened) | ratio | m1 (m1), m3 (m3) | Historical September/August registration ratios are near or slightly below 1.0 (2023: 10,717/12,016 = 0.89; 2025: 8,603/8,939 = 0.96). Central value 0.98 with a wide range spanning the observed 0.89-0.96 and modest upside. | The August 2026 level is known or proxied and the September seasonal pattern resembles recent years. | Evidence that September 2026 registrations were unusually boosted (e.g., a registration-deadline or subsidy effect) or that the seasonal ratio shifted well outside 0.90-1.06. |
| a2 | August 2026 level relative to July 2026 | 1 | 0.9..1.1 | 0.7036..1.407 (widened) | ratio | m1 (m1) | Month-to-month registration moves are modest; 2025 July→August was 8,939→8,464 (0.95) and 2023 July→August was 10,891→12,016 (1.10). Central 1.0 with ±10% range. | August 2026 is not yet observed and July 2026 is the latest available month. | Publication of an August 2026 count far outside 0.90-1.10 of July's 7,906. |
| a3 | September 2026 YoY change factor vs September 2025 | 0.9 | 0.8..1 | 0.8..1 | ratio | m2 (m2) | July 2026 was down 11.56% YoY (p21) and the 2025 annual decline was 20% (p2); recent months show a steepening decline. Central 0.90 (10% decline) with range 0.80-1.00 reflecting the ongoing downward trend and possible subsidy cushioning. | September 2026 continues the 2026 downward trend observed through July. | Evidence that the 2026 decline flattened or reversed (e.g., August 2026 YoY near zero or positive). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,648 | ['p16'] / ['a1', 'a2'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 7,682 | ['p4'] / ['a3'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 7,246 | ['p18', 'p19', 'p16'] / ['a1'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **7,522** birth, 80% interval [4,441, 12,742] birth, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 7,522 birth (80% model-based interval 4,441 to 12,742 birth), covering births registered in Taiwan during September 2026 under the MOI monthly household registration statistics. Three methods were averaged with equal weights (33%, 33%, 33%): 7,648, 7,682, and 7,246 birth. Observed anchors include July 2026 at 7,906 births, September 2025 at 8,603 births, and May–June 2026 at 6,832 births and 7,324 births. The methods carry these forward using assumptions: a September/August ratio of 0.98 (range 0.6907 to 1.381), an August/July level of 1 (0.7036 to 1.407), and a September year-over-year factor of 0.9 (0.8 to 1). The combination reflects too few backtest years to weight methods by demonstrated accuracy, so the interval reflects input uncertainty only. The main risk is that the 2026 decline steepens or flattens beyond these assumed ranges. Actual August 2026 registrations and early September data would most improve the forecast.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September/August registration ratio: 0.98 ratio, range 0.6907 to 1.381 (range widened by code); used by m1, m3. Overturned by: Evidence that September 2026 registrations were unusually boosted (e.g., a registration-deadline or subsidy effect) or that the seasonal ratio shifted well outside [n]-[n].
- a2 August 2026 level relative to July 2026: 1 ratio, range 0.7036 to 1.407 (range widened by code); used by m1. Overturned by: Publication of an August 2026 count far outside [n]-[n] of July's [n].
- a3 September 2026 YoY change factor vs September 2025: 0.9 ratio, range 0.8 to 1; used by m2. Overturned by: Evidence that the 2026 decline flattened or reversed (e.g., August 2026 YoY near zero or positive).

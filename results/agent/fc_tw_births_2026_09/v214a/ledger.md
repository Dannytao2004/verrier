# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered in Taiwan (Republic of China) during September 2026, as counted in the Ministry of the Interior's monthly household registration statistics (births registered in the month, by date of registration) | unit births registered in September 2026 | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior (MOI), Republic of China (Taiwan) — Department of Household Registration monthly statistics

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household registration statistics

Hypothesis: September 2026 births registered will follow the recent monthly level and September seasonal pattern; the most recent published months (through ~July/August 2026) anchor the level, and prior Septembers give the seasonal factor.

Queries issued by the searcher: 內政部 戶政司 出生 登記 統計 月 2026; Taiwan monthly registered births 2026 statistics Ministry of Interior; 2026年7月 出生數 內政部 戶口統計 新生兒; 2026年6月 出生數 新生兒 內政部 戶政司 公布; 內政部 戶政司 出生 登記 統計 月 2026; Taiwan monthly births registered statistics 2026 Ministry of Interior; 2025年9月 出生數 8603 內政部 戶口統計 新生兒; 2024年9月 出生數 內政部 戶口統計 新生兒 較上年; 內政部 戶政司 出生 登記 統計 月 各月出生數; Taiwan monthly births registered statistics 2025 2026 Ministry of Interior; ris.gov.tw 出生死亡及結離婚月表 按登記日期 115年7月 出生數; 112年9月 出生數 內政部 戶口統計 1萬 新生兒 2023年9月

- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://hk.crntt.com/doc/1602/1/8/7/160218724.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20260610002909-260407` -> **snapshot** (snapshot 20260622115614); points raw/verified 15/15
  - p1 Taiwan total population at end of May 2026 (ROC year 115) = **23,252,641** person (2026-05-01..2026-05-31) [keep: ] quote: "截至今年5月底為止,台灣總人口數為2325萬2641人"
  - p2 Taiwan live births registered in May 2026 (ROC year 115) = **6,832** births registered (2026-05-01..2026-05-31) [keep: ] quote: "5月新生兒數為6832人"
  - p3 Taiwan live births registered in April 2026 (ROC year 115) = **8,144** births registered (2026-04-01..2026-04-30) [keep: ] quote: "比4月新生兒8144人少了1312人"
  - p4 Taiwan live births registered in February 2026 (ROC year 115), lowest single mon = **6,523** births registered (2026-02-01..2026-02-28) [keep: ] quote: "僅次於今年2月單月新生兒最低數6523人"
  - p5 Change in Taiwan live births registered, May 2026 vs April 2026 = **1,312** births registered (2026-04-01..2026-05-31) [keep: ] quote: "較上月減少1312人"
  - p6 Change in Taiwan live births registered, May 2026 vs May 2025 = **1,601** births registered (2025-05-01..2026-05-31) [keep: ] quote: "較上年同月減少1,601人"
  - p7 Taiwan crude birth rate, annualised, May 2026 (ROC year 115) = **3.46** births per 1,000 person (2026-05-01..2026-05-31) [keep: ] quote: "折合年粗出生率為千分之3.46"
  - p8 Minutes per birth implied for May 2026 = **6.5** minutes per birth (2026-05-01..2026-05-31) [keep: ] quote: "約每6.5分鐘出生一個嬰兒"
  - p9 Taiwan deaths registered in May 2026 (ROC year 115) = **15,158** deaths registered (2026-05-01..2026-05-31) [keep: ] quote: "5月死亡數為1萬5158人"
  - p10 Taiwan population aged 0-14 at end of May 2026 = **2,642,980** person (2026-05-01..2026-05-31) [keep: ] quote: "0至14歲人口數為264萬2980人"
  - p11 Share of Taiwan population aged 0-14 at end of May 2026 = **11.37** % (2026-05-01..2026-05-31) [keep: ] quote: "0至14歲人口數為264萬2980人,占總人口比率11.37%"
  - p12 Taiwan population aged 15-64 at end of May 2026 = **15,859,310** person (2026-05-01..2026-05-31) [keep: ] quote: "15至64歲人口數為1585萬9310人"
  - p13 Taiwan population aged 65 and over at end of May 2026 = **4,750,351** as written "4,75萬351人", value check pending person (2026-05-01..2026-05-31) [keep: ] quote: "65歲以上人口數為4,75萬351人"
  - p14 Taiwan population aged 20 and over at end of May 2026 = **19,641,337** person (2026-05-01..2026-05-31) [keep: ] quote: "20歲以上人口數則為1964萬1337人"
  - p15 Change in Taiwan total population, May 2026 vs May 2025 = **102,829** person (2025-05-01..2026-05-31) [keep: ] quote: "與上年同月比較減少10萬2829人"
- `https://i-media.tw/Article/Detail/47445` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p16 Taiwan total population, July 2026 = **23,235,002** person (2026-07-01..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人"
  - p17 Taiwan births registered, July 2026 = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人"
  - p18 Taiwan births registered, May 2026 = **6,832** births registered (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p19 Taiwan births registered, June 2026 = **7,324** births registered (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p20 Taiwan year-on-year change in July births, 2026 vs 2025 = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少11.56%"
  - p21 Taiwan year-on-year decrease in July births, 2026 vs 2025 (count) = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p22 Taiwan crude birth rate, July 2026 (annualised) = **4.01** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗出生率為4.01‰"
  - p23 Taiwan deaths registered, July 2026 = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "7月死亡人數則為1萬7119人"
  - p24 Taiwan crude death rate, July 2026 (annualised) = **8.67** deaths per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰"
  - p25 Taiwan year-on-year change in July deaths, 2026 vs 2025 = **1.62** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%"
  - p26 Taiwan month-on-month change in July deaths, 2026 vs June 2026 = **4.77** % (2026-07-01..2026-07-31) [keep: ] quote: "較上月增加4.77%"
  - p27 Taiwan total population year-on-year change, July 2026 vs 2025 = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%"
  - p28 Taiwan total population month-on-month change, July 2026 vs June 2026 = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "與6月相比則減少0.04%"
  - p29 Taiwan marriages registered, July 2026 = **7,150** marriages registered (2026-07-01..2026-07-31) [keep: ] quote: "7月全台共有7150對"
  - p30 Taiwan divorces registered, July 2026 = **4,450** divorces registered (2026-07-01..2026-07-31) [keep: ] quote: "離婚對數為4450對"
- `https://news.pts.org.tw/article/821731` -> **snapshot** (snapshot 20260811182642); points raw/verified 15/1
  - p31 Average age of Taiwanese women at first birth = **32** years (not stated (page dated 2026-08-10)) [keep: ] quote: "台灣女性生育第一胎的平均年齡大約落在32歲"
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160255313` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=a993b8150b6c4f59b5ce02b47e347ed0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/421847` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ocac.gov.tw/OCAC/Eng/Pages/Detail.aspx?nodeid=329&pid=83728160` -> **snapshot** (snapshot 20260410211556); points raw/verified 15/0
- `https://www.taiwanplus.com/news/taiwan-news/public-policy/260508018/april-marks-28th-straight-month-of-population-decline-in-taiwan` -> **snapshot** (snapshot 20260610150351); points raw/verified 3/3
  - p32 Taiwan births registered in April 2026 (interior ministry monthly figures, 'just = **8,000** births registered (2026-04-01..2026-04-30) [DISCARD: Rounded approximation superseded by exact April 2026 figure p3.] quote: "New figures from the interior ministry showed just over 8,000 births during the month, compared with nearly 16,000 deaths."
  - p33 Taiwan deaths registered in April 2026 (interior ministry monthly figures, 'near = **16,000** deaths registered (2026-04-01..2026-04-30) [DISCARD: Rounded approximation, not needed.] quote: "New figures from the interior ministry showed just over 8,000 births during the month, compared with nearly 16,000 deaths."
  - p34 Consecutive months of Taiwan population decline through April 2026 = **28** consecutive months (2026-04-01..2026-04-30) [keep: ] quote: "Taiwan's population declined again in April, marking the 28th consecutive month of population decrease."
- `https://rwdnews.sanlih.com.tw/news/1887028` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 29 (period year 2026 does not appear in the page text or URL (likely mis-dated): 28; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d2 [related_series] National statistics / DGBAS population and birth series

Hypothesis: Alternative official birth series (DGBAS, National Development Council population projections, or annual birth totals) can cross-check and bridge to the MOI monthly registration count; annual 2026 births projected from trend times September share gives an independent route.

Queries issued by the searcher: Taiwan annual births 2024 2023 statistics Ministry of Interior 出生數; 國發會 人口推估 出生數 2026 台灣; 內政部 戶政司 統計 2026年 出生人數 月 統計 6月 7月; 台灣 每月出生人數 分布 9月 占全年 比例 出生 月別; Taiwan annual births 2025 statistics Department of Household Registration; 國發會 人口推估 出生數 2026; 內政部 戶口統計 2025年9月 出生數 新生兒; Taiwan monthly births 2024 by month September birth count MOI statistics; Taiwan annual births 2025 statistics 內政部 出生數; 國發會 人口推估 2026 出生數; Taiwan births September share of annual births monthly pattern; 2025年9月 出生數 內政部 戶口統計 新生兒 8,603; 內政部 戶政統計 每月出生人數 統計表 113年 114年 出生數 按月; 2026年 前7月 出生人數 5.4萬 內政部 統計

- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 10/6
  - p35 Taiwan total population in 2045 (NDC projection) = **20,000,000** person (2045-01-01..2045-12-31) [keep: ] quote: "2045年首度跌破2000萬人"
  - p36 Taiwan total population in 2055 (NDC projection) = **17,510,000** person (2055-01-01..2055-12-31) [keep: ] quote: "2055年只剩1751萬人"
  - p37 Share of women aged 15-49 in total female population in 2075 (NDC projection, up = **2** % (2075-01-01..2075-12-31) [keep: ] quote: "2075年15到49歲的育齡婦女,占全體女性比率將不到2成"
  - p38 Average age of mother at first birth in Taiwan (latest) = **31.8** year (not stated (page dated 2026-08-28)) [keep: ] quote: "首胎生母平均年齡31.8歲,相較2005年增加4.1歲"
  - p39 Increase in average age of mother at first birth since 2005 (Taiwan) = **4.1** year (not stated (page dated 2026-08-28)) [keep: ] quote: "首胎生母平均年齡31.8歲,相較2005年增加4.1歲"
  - p40 Decline in working-age population over next 50 years (Taiwan, NDC projection) = **0.6667** as written "近三分之二", value check pending 1 (2026-01-01..2075-12-31) [keep: ] quote: "未來50年,工作年齡人口總量將減少近三分之二"
- `http://dev.taisounds.news/news/content/76/285689` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/11
  - p41 Taiwan total fertility rate (TFR) in 2025, per MOI latest statistics = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "我國總生育率於去(2025)年降至0.695人"
  - p42 NDC projection high scenario: long-term TFR reached by 2075 = **1.1** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "高、中及低情境由前次假設2070年達1.3人、1.0人及0.8人,微調為2075年達1.1人、0.8人及0.6人"
  - p43 NDC projection medium scenario: long-term TFR reached by 2075 = **0.8** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "微調為2075年達1.1人、0.8人及0.6人"
  - p44 NDC projection low scenario: long-term TFR reached by 2075 = **0.6** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "微調為2075年達1.1人、0.8人及0.6人"
  - p45 NDC projection: share of population aged 0-14 in 2026 (Table 1) = **11.1** % (2026-01-01..2026-12-31) [keep: ] quote: "2026 23,191 2,577 15,756 4,858 11.1 67.9 20.9"
  - p46 NDC projection: share of population aged 15-64 in 2026 (Table 1) = **67.9** % (2026-01-01..2026-12-31) [keep: ] quote: "2026 23,191 2,577 15,756 4,858 11.1 67.9 20.9"
  - p47 NDC projection: share of population aged 65+ in 2026 (Table 1) = **20.9** % (2026-01-01..2026-12-31) [keep: ] quote: "2026 23,191 2,577 15,756 4,858 11.1 67.9 20.9"
  - p48 NDC projection: median age in 2026 (Table 2) = **46.4** years (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p49 NDC projection: potential support ratio in 2026 (Table 2) = **3.2** working-age persons per elderly person (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p50 NDC projection: total dependency ratio (per 100 working-age) in 2026 (Table 2) = **47.2** dependents per 100 working-age persons (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p51 NDC projection: old-age dependency ratio (per 100 working-age) in 2026 (Table 2) = **30.8** elderly per 100 working-age persons (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
- `https://tw.news.yahoo.com/%E5%8F%B0%E7%81%A3%E4%BA%BA%E5%8F%A3%E6%95%B820%E5%B9%B4%E5%BE%8C%E4%B8%8D%E5%88%B02%E5%8D%83%E8%90%AC-%E9%80%99%E5%B9%B4-%E` -> **snapshot** (snapshot 20260901044610); points raw/verified 15/15
  - p52 Taiwan total live births, first 7 months of 2026 (Jan–Jul), as counted in curren = **54,000** births (2026-01-01..2026-07-31) [keep: ] quote: "根據目前統計,台灣2026年前7月出生人數僅5.4萬人"
  - p53 NDC forecast of Taiwan total live births for full-year 2026 (projection, below 1 = **94,000** births (2026-01-01..2026-12-31) [keep: ] quote: "國發會預計,2026年全年總出生人數將會跌破10萬,預計為9.4萬人。"
  - p54 Taiwan total fertility rate, 2024 (observed) = **0.885** births per woman (2024-01-01..2024-12-31) [keep: ] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人"
  - p55 Taiwan total fertility rate, 2025 (observed) = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "主要是國內總生育率由2024年0.885,驟降至2025年0.695人"
  - p56 NDC 2024 projection model: high-case total fertility rate assumption for 2026 = **1.1** births per woman (2026-01-01..2026-12-31) [keep: ] quote: "2026的總生育,則全面下調至1.1、0.8、0.6。"
  - p57 NDC 2024 projection model: mid-case total fertility rate assumption for 2026 = **0.8** births per woman (2026-01-01..2026-12-31) [keep: ] quote: "2026的總生育,則全面下調至1.1、0.8、0.6。"
  - p58 NDC 2024 projection model: low-case total fertility rate assumption for 2026 = **0.6** births per woman (2026-01-01..2026-12-31) [keep: ] quote: "2026的總生育,則全面下調至1.1、0.8、0.6。"
  - p59 Taiwan total population, 2026 (NDC projection) = **23,191,000** persons (2026-01-01..2026-12-31) [keep: ] quote: "2026年 總人口 2,319.1 萬人"
  - p60 Taiwan total population, 2035 (NDC projection) = **21,972,000** persons (2035-01-01..2035-12-31) [keep: ] quote: "2035年 總人口 2,197.2 萬人"
  - p61 Taiwan total population, 2045 (NDC projection) = **19,976,000** persons (2045-01-01..2045-12-31) [keep: ] quote: "2045年 總人口 1,997.6 萬人"
  - p62 Taiwan total population, 2075 (NDC projection) = **12,149,000** persons (2075-01-01..2075-12-31) [keep: ] quote: "2075年 總人口 1,214.9 萬人"
  - p63 Share of population aged 0–14 (young children), 2026 (NDC projection) = **11.1** % (2026-01-01..2026-12-31) [keep: ] quote: "2026年 總人口 2,319.1 萬人 11.1% 67.9% 20.9%"
  - p64 Share of population aged 15–64 (working age), 2026 (NDC projection) = **67.9** % (2026-01-01..2026-12-31) [keep: ] quote: "2026年 總人口 2,319.1 萬人 11.1% 67.9% 20.9%"
  - p65 Share of population aged 65+ (elderly), 2026 (NDC projection) = **20.9** % (2026-01-01..2026-12-31) [keep: ] quote: "2026年 總人口 2,319.1 萬人 11.1% 67.9% 20.9%"
  - p66 Married share (有偶率) of women aged 20–49, 2025 = **43.5** % (2025-01-01..2025-12-31) [keep: ] quote: "台灣20歲至49歲婦女有偶率,從2005年的55.3%,下降至2025年的43.5%"
- `https://www.mdnkids.com/content.asp?Link_String_=248T00000GDYIDY` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www3.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sinchew.com.my/news/20260109/international/7174252` -> **snapshot** (snapshot 20260110002511); points raw/verified 15/15
  - p67 Taiwan annual live births, 2023 = **135,571** births (2023-01-01..2023-12-31) [keep: ] quote: "2022年13万8986人、2023年13万5571人、2024年13万4856人"
  - p68 Taiwan annual live births, 2024 = **134,856** births (2024-01-01..2024-12-31) [keep: ] quote: "2023年13万5571人、2024年13万4856人,加上去年仅有10万余人"
  - p69 Taiwan annual live births, 2025 = **107,812** births (2025-01-01..2025-12-31) [keep: ] quote: "2025年新生儿数有10万7812人,连续10年下降,再创新低。"
  - p70 Taiwan annual live births, 2022 = **138,986** births (2022-01-01..2022-12-31) [keep: ] quote: "2021年15万3820人、2022年13万8986人、2023年13万5571人"
  - p71 Taiwan annual live births, 2021 = **153,820** births (2021-01-01..2021-12-31) [keep: ] quote: "2020年16万5249人、2021年15万3820人、2022年13万8986人"
  - p72 Taiwan annual live births, 2020 = **165,249** births (2020-01-01..2020-12-31) [keep: ] quote: "2019年17万7767人、2020年16万5249人、2021年15万3820人"
  - p73 Taiwan annual live births, 2019 = **177,767** births (2019-01-01..2019-12-31) [keep: ] quote: "2018年18万1601人、2019年17万7767人、2020年16万5249人"
  - p74 Taiwan annual live births, 2018 = **181,601** births (2018-01-01..2018-12-31) [keep: ] quote: "2017年19万3844人、2018年18万1601人、2019年17万7767人"
  - p75 Taiwan annual live births, 2017 = **193,844** births (2017-01-01..2017-12-31) [keep: ] quote: "2016年20万8440人、2017年19万3844人、2018年18万1601人"
  - p76 Taiwan annual live births, 2016 = **208,440** births (2016-01-01..2016-12-31) [keep: ] quote: "台湾新生儿数自2016年起逐年下降,2016年20万8440人、2017年19万3844人"
  - p77 Taiwan single-month live births, December 2025 = **9,027** births (2025-12-01..2025-12-31) [keep: ] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p78 Change in Taiwan monthly live births, December 2025 vs November 2025 = **1,081** births (2025-12-01..2025-12-31) [keep: ] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p79 Change in Taiwan monthly live births, December 2025 vs December 2024 = **3,469** births (2025-12-01..2025-12-31) [keep: ] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p80 Taiwan total population, end of December 2025 = **23,299,132** person (2025-12-31..2025-12-31) [keep: ] quote: "去年12月底,全台人口数2329万9132人,比2024年同期减少了10万1088人"
  - p81 Taiwan annual deaths, 2025 = **200,268** deaths (2025-01-01..2025-12-31) [keep: ] quote: "去年整体死亡人数为20万268人,折合年粗死亡率为千分之8.58"
- `https://rwdnews.sanlih.com.tw/news/1897905` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://worldnews.net.ph/post/217743` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821731` -> **snapshot** (snapshot 20260811182642); points raw/verified 15/10
  - p82 Average age of Taiwanese women at first birth = **32** years (not stated (page dated 2026-08-10)) [DISCARD: Duplicate of p31 (average age at first birth); no added information.] quote: "台灣女性生育第一胎的平均年齡大約落在32歲"
  - p83 Share of obstetric medical institutions closed in Taiwan over the past 5 years = **3** % (obstetric institutions closed / obstetric institutions) (not stated (page dated 2026-08-10)) [keep: ] quote: "這5年來差不多關了3成的產科醫療機構"
  - p84 Decline in births at large hospitals in Taiwan over the past 5 years (lower boun = **2** % (decline in births / births) (not stated (page dated 2026-08-10)) [keep: ] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p85 Decline in births at large hospitals in Taiwan over the past 5 years (upper boun = **3** % (decline in births / births) (not stated (page dated 2026-08-10)) [keep: ] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p86 Decline in births at primary/clinic level in Taiwan over the past 5 years (lower = **6** % (decline in births / births) (not stated (page dated 2026-08-10)) [keep: ] quote: "可是在基層來講大概掉6、7成"
  - p87 Decline in births at primary/clinic level in Taiwan over the past 5 years (upper = **7** % (decline in births / births) (not stated (page dated 2026-08-10)) [keep: ] quote: "可是在基層來講大概掉6、7成"
  - p88 Highest county/city crude birth rate in Taiwan (Taitung County) = **6.06** births per 1,000 population (not stated (page dated 2026-08-10)) [keep: ] quote: "粗出生率最高為台東縣千分之6.06"
  - p89 Second-highest county/city crude birth rate in Taiwan (Yunlin County) = **5.29** births per 1,000 population (not stated (page dated 2026-08-10)) [keep: ] quote: "其次為雲林縣千分之5.29"
  - p90 Lowest county/city crude birth rate in Taiwan (Keelung City) = **2.1** births per 1,000 population (not stated (page dated 2026-08-10)) [keep: ] quote: "最低為基隆市千分之2.10"
  - p91 Second-lowest county/city crude birth rate in Taiwan (Tainan City) = **3.14** births per 1,000 population (not stated (page dated 2026-08-10)) [keep: ] quote: "其次為台南市千分之3.14"
- `https://health.businessweekly.com.tw/article/ARTL003018867` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 13 (period year 2026 does not appear in the page text or URL (likely mis-dated): 8; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 4)

### d3 [physical_flow] Birth occurrence vs registration timing

Hypothesis: Registered births in a month ≈ births occurring in the month plus net registration lag adjustment; occurrence-based monthly births (from health/statistics sources) can be shifted by the typical registration lag distribution to estimate registrations.

Queries issued by the searcher: 台灣 出生登記 期限 60日 統計 出生登記 時效; Taiwan birth registration within 60 days law 戶籍法 出生登記; 內政部戶政司 出生登記 按月 統計 114年 各月 出生數 表; 出生通報 統計 月報 活產 114年 各月 出生通報數; 台灣 出生登記 期限 60日 統計 出生發生數 登記數 差異; Taiwan birth registration lag distribution births registered within 30 days; 內政部 戶政司 統計 115年7月 出生數 出生登記 月報; 出生通報統計 每月 出生通報數 2026 國民健康署 統計; 台灣 出生登記 期限 60日 統計; Taiwan birth registration lag distribution 出生登記 發生數 登記數 差異; 內政部 戶政司 114年7月 出生數 統計 每月 出生 登記; 台灣 2025年 出生數 創新低 每月 出生 統計 114年; 人口統計季刊 113年 嬰兒出生數按出生日期及登記日期相差日數分 百分比分配

- `https://www.hpa.gov.tw/Pages/ashx/File.ashx?FilePath=~/File/Attach/1247/File_1104.pdf` -> **snapshot** (snapshot 20240714080211); points raw/verified 8/3
  - p92 Deadline for birth registration before reminder/registration-by-office (days aft = **60** day (2008-05-01..2008-05-31) [keep: ] quote: "If birth registration procedures are not completed within 30 days (amended to 60 days in May 2008), this copy will be used to send a reminder"
  - p93 Minimum birth weight for stillbirth reporting threshold (grams) = **500** g (not stated (page dated 2019-03-19)) [keep: ] quote: "including live births and stillbirths (weighing 500 grams or more and carried for 20 weeks or more)"
  - p94 Minimum gestation for stillbirth reporting threshold (weeks) = **20** week (not stated (page dated 2019-03-19)) [keep: ] quote: "including live births and stillbirths (weighing 500 grams or more and carried for 20 weeks or more)"
- `https://www.mlshb.gov.tw/nc/api/v3/storage/files/a98fa5fbeb25ae5ce476b22251a06ce43d5c43fb297ac5a8caa4e8c9ab04d28b.pdf?displayName=113%E5%B9%B4%E5%87%B` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.chcg.gov.tw/UserFiles/1010096221.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS82NjEzLzEwMjEyLnBkZg%3D%3D&n=MTAyMTIucGRm&icon=..pdf` -> **snapshot** (snapshot 20250502234415) **LEAK SENTINEL HIT ['(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.hpa.gov.tw/File/Attach/14717/File_17496.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `http://newdoc.nccu.edu.tw/acadbonus/04/10300039/10300039.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://twinfo.ncl.edu.tw/tiqry/hypage.cgi?HYPAGE=search/merge_pdf.hpg&sysid=T0834228&jid=00238889&dtd_id=11&type=s&vol=60100000&page=%e6%8f%90%e8%a6%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS82NTI0Lzk5MDEucGRm&n=OTkwMS5wZGY%3d&icon=..pdf` -> **snapshot** (snapshot 20260109040211) **LEAK SENTINEL HIT ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)', '(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS82NTMzLzk5MTAucGRm&n=OTkxMC5wZGY%3D&icon=.pdf` -> **snapshot** (snapshot 20250803164030) **LEAK SENTINEL HIT ['(?<![\\d.,])7,704(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.ey.gov.tw/File/AC31F9B96D44C356?A=C` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/15
  - p95 Registered births in Taiwan, September 2025 (month of registration) = **8,603** births registered (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p96 Registered births in Taiwan, October 2025 (month of registration) = **9,458** births registered (2025-10-01..2025-10-31) [keep: ] quote: "23,310,853 11,470,704 11,840,149 9,458 15,908 6,450"
  - p97 Registered births in Taiwan, November 2025 (month of registration) = **7,946** births registered (2025-11-01..2025-11-30) [keep: ] quote: "23,306,085 11,467,137 11,838,948 7,946 14,771 6,825"
  - p98 Registered births in Taiwan, December 2025 (month of registration) = **9,027** births registered (2025-12-01..2025-12-31) [keep: ] quote: "23,299,132 11,462,401 11,836,731 9,027 17,450 8,423"
  - p99 Registered births in Taiwan, full year 2025 = **107,812** births registered (2025-01-01..2025-12-31) [keep: ] quote: "According to the household registration data, there were 107,812 births in 2025,"
  - p100 Registered births in Taiwan, January 2025 = **9,495** births registered (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p101 Registered births in Taiwan, February 2025 = **10,407** births registered (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p102 Registered births in Taiwan, March 2025 = **9,388** births registered (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p103 Registered births in Taiwan, April 2025 = **8,684** births registered (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p104 Registered births in Taiwan, May 2025 = **8,433** births registered (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p105 Registered births in Taiwan, June 2025 = **8,968** births registered (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p106 Registered births in Taiwan, July 2025 = **8,939** births registered (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p107 Registered births in Taiwan, August 2025 = **8,464** births registered (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p108 Registered births in Taiwan, October-December 2025 cumulative = **26,431** births registered (2025-10-01..2025-12-31) [keep: ] quote: "26,431 13,591 12,840 25,162 12,932 12,230"
  - p109 Registered births in Taiwan, 2024 (previous year) = **134,856** births registered (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
- `https://210.241.78.32/Pages/Detail.aspx?nodeid=647&pid=1248` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3; value_as_written not in quote as a whole number: 2)

### d4 [base_rates] Demographic base rate

Hypothesis: Monthly births ≈ women of childbearing age × age-specific fertility rate / 12, adjusted for seasonality; a fertility-rate-based decomposition constrains the level independently of recent registration noise.

Queries issued by the searcher: Taiwan age-specific fertility rate 2024 內政部 統計; 台灣 育齡婦女 人數 2025 15-49歲 統計; 內政部 戶政司 出生數 按月 統計 2026年 1月 2月 3月 新生兒; Taiwan births monthly 2026 January February March year-on-year decline 內政部 出生人數; Taiwan age-specific fertility rate 2024 內政部 統計; 台灣 育齡婦女 人數 2025 15-49歲 統計; 內政部 戶政司 出生數 按登記日期 2026年7月 出生人數; 台灣 2026年 上半年 新生兒 出生數 統計 內政部 創新低; Taiwan age-specific fertility rate 2024 Department of Household Registration; 台灣 育齡婦女人數 2025 內政部 統計; 內政部 戶政司 統計 出生數 按月 2026年 每月 出生 人數; Taiwan monthly births 2026 January February March year-on-year decline

- `http://mp.weixin.qq.com/s?__biz=MzYzODg1NjE3Mg==&mid=2247484485&idx=1&sn=6abc718b35aa41ed808248bc69afc5be` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/3%e6%9c%88%e5%87%ba%e7%94%9f%e6%95%b8%e5%9b%9e%e5%8d%87-%e7%b8%bd%e4%ba%ba%e5%8f%a3%e4%bb%8d%e9%80%a327%e5%80%8b%e6%9c%88%e8%b2%` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://124.217.235.41/news/business/2026/01/09/789231` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://open2.idataiwan.com/3334/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://georank.org/birth-rate/taiwan` -> **snapshot** (snapshot 20260107111018); points raw/verified 15/15
  - p110 Taiwan total fertility rate, 2026 (children per woman) = **0.88** children per woman (2026-01-01..2026-12-31) [DISCARD: TFR 0.88 conflicts with official 0.695/0.885; unreliable.] quote: "\| 2026 \| 0.88 \| 2.18 \|"
  - p111 Taiwan total fertility rate, 2025 (children per woman) = **0.88** children per woman (2025-01-01..2025-12-31) [DISCARD: TFR 0.88 conflicts with official 0.695; unreliable.] quote: "\| 2025 \| 0.88 \| 2.18 \|"
  - p112 Taiwan total fertility rate, 2024 (children per woman) = **0.89** children per woman (2024-01-01..2024-12-31) [DISCARD: TFR 0.89 conflicts with official 0.885; unreliable.] quote: "According to the latest birth rate data available, the fertility rate in Taiwan was 0.89 in 2024"
  - p113 Taiwan female reproductive age (15-49) share of population, 2024 = **22.9** % (2024-01-01..2024-12-31) [DISCARD: Reproductive-age share not needed and not used in any executable route.] quote: "22.9% of the population in 2024 is composed of women of reproductive age (15-49)"
  - p114 Taiwan annual births per 1,000 women ages 15-19, 2026 = **2.85** births per 1,000 women (2026-01-01..2026-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2026 \| 10.4 \| 2.85 \| 26.8 \| 10.2 \|"
  - p115 Taiwan annual births per 1,000 women ages 20-29, 2026 = **26.8** births per 1,000 women (2026-01-01..2026-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2026 \| 10.4 \| 2.85 \| 26.8 \| 10.2 \|"
  - p116 Taiwan annual births per 1,000 women ages 30+, 2026 = **10.2** births per 1,000 women (2026-01-01..2026-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2026 \| 10.4 \| 2.85 \| 26.8 \| 10.2 \|"
  - p117 Taiwan annual births per 1,000 women, total, 2026 = **10.4** births per 1,000 women (2026-01-01..2026-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2026 \| 10.4 \| 2.85 \| 26.8 \| 10.2 \|"
  - p118 Taiwan annual births per 1,000 women ages 15-19, 2025 = **2.87** births per 1,000 women (2025-01-01..2025-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2025 \| 10.6 \| 2.87 \| 27.7 \| 10.3 \|"
  - p119 Taiwan annual births per 1,000 women ages 20-29, 2025 = **27.7** births per 1,000 women (2025-01-01..2025-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2025 \| 10.6 \| 2.87 \| 27.7 \| 10.3 \|"
  - p120 Taiwan annual births per 1,000 women ages 30+, 2025 = **10.3** births per 1,000 women (2025-01-01..2025-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2025 \| 10.6 \| 2.87 \| 27.7 \| 10.3 \|"
  - p121 Taiwan annual births per 1,000 women, total, 2025 = **10.6** births per 1,000 women (2025-01-01..2025-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2025 \| 10.6 \| 2.87 \| 27.7 \| 10.3 \|"
  - p122 Taiwan annual births per 1,000 women, total, 2024 = **11.4** births per 1,000 women (2024-01-01..2024-12-31) [DISCARD: Age-specific fertility rates not used; no executable route.] quote: "\| 2024 \| 11.4 \| 2.89 \| 28.7 \| 10.4 \|"
  - p123 Taiwan share of live births to women under 20, 2026 = **1.08** % (2026-01-01..2026-12-31) [DISCARD: Birth share by age not used; no executable route.] quote: "In 2026, of all live births 1.08% were to women under 20 years old, 26.1% to women ages 20-29, and 72.8% to women ages 30 and above."
  - p124 Taiwan share of live births to women ages 20-29, 2026 = **26.1** % (2026-01-01..2026-12-31) [DISCARD: Birth share by age not used; no executable route.] quote: "In 2026, of all live births 1.08% were to women under 20 years old, 26.1% to women ages 20-29, and 72.8% to women ages 30 and above."
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://living.taronews.tw/2026/03/10/1155443/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/798480` -> **snapshot** (snapshot 20260415075135); points raw/verified 15/15
  - p125 Taiwan total population at end of February 2026 = **23,280,273** person (2026-02-28..2026-02-28) [keep: ] quote: "截至今年2月底台灣總人口數為2328萬273人"
  - p126 Live births registered in Taiwan in February 2026 = **6,523** birth (2026-02-01..2026-02-28) [keep: ] quote: "今年2月新生兒數共6523人"
  - p127 Month-on-month change in Taiwan live births, February 2026 vs January 2026 = **2,200** birth (2026-02-01..2026-02-28) [keep: ] quote: "今年2月新生兒數共6523人,較1月減少2200人"
  - p128 Month-on-month percentage change in Taiwan live births, February 2026 vs January = **25.2** % (2026-02-01..2026-02-28) [keep: ] quote: "較1月減少2200人、減幅約25.2%"
  - p129 Taiwan overall annualised crude birth rate, February 2026 = **3.65** births per 1,000 people (2026-02-01..2026-02-28) [keep: ] quote: "整體折合年粗出生率為3.65‰"
  - p130 Taiwan population aged 15-64 at end of February 2026 = **15,905,248** person (2026-02-28..2026-02-28) [keep: ] quote: "15至64歲人口數為1590萬5248人,占68.32%"
  - p131 Share of Taiwan population aged 15-64, end of February 2026 = **68.32** % (2026-02-28..2026-02-28) [keep: ] quote: "15至64歲人口數為1590萬5248人,占68.32%"
  - p132 Taiwan population aged 0-14 at end of February 2026 = **2,667,349** person (2026-02-28..2026-02-28) [keep: ] quote: "台灣0至14歲人口數為266萬7349人,占總人口比率11.46%"
  - p133 Taiwan population aged 65 and over at end of February 2026 = **4,707,676** person (2026-02-28..2026-02-28) [keep: ] quote: "65歲以上人口數共470萬7676人,占20.22%"
  - p134 Year-on-year decrease in Taiwan total population, February 2026 vs February 2025 = **104,000** person (2026-02-01..2026-02-28) [keep: ] quote: "今年2月台灣總人口數較去年同期已減少10.4萬人、減幅約0.45%"
  - p135 Average daily decrease in Taiwan total population, February 2026 = **286** person per day (2026-02-01..2026-02-28) [keep: ] quote: "平均每天減少285.87人"
  - p136 Deaths in Taiwan in February 2026 = **14,881** death (2026-02-01..2026-02-28) [keep: ] quote: "共有1萬4881人死亡"
  - p137 Taiwan overall annualised crude death rate, February 2026 = **8.33** deaths per 1,000 people (2026-02-01..2026-02-28) [keep: ] quote: "今年2月折合年粗死亡率為8.33‰"
  - p138 Highest county/city crude birth rate in Taiwan, February 2026 (Penghu County) = **5.62** births per 1,000 people (2026-02-01..2026-02-28) [keep: ] quote: "今年2月粗出生率最高縣市為澎湖縣5.62‰"
  - p139 Lowest county/city crude birth rate in Taiwan, February 2026 (Keelung City) = **2.54** births per 1,000 people (2026-02-01..2026-02-28) [keep: ] quote: "最低縣市則為基隆市2.54‰"
- `https://www.pttweb.tw/HatePolitics/M.1781106883.A.829` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/newspapers/20250611000175-260210` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pttweb.cc/bbs/Gossiping/M.1757517417.A.E21` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [shocks] Calendar and policy effects

Hypothesis: 2026 lunar calendar (Year of the Horse), holiday timing, marriage cohort shifts, and any new birth-incentive policy could shift September 2026 registrations relative to trend; quantify exposure where measurable.

Queries issued by the searcher: 台灣 2026 出生 生肖 效應 馬年; 台灣 2025 出生人數 內政部 統計 月; 2026年6月 出生數 內政部 戶口統計 新生兒; 台灣 2026 生育補助 每胎10萬 上路 政策; 台灣 2026 出生 生肖 效應 馬年; 內政部 戶政司 出生 登記 統計 2025 月; 2025年9月 出生數 8603 內政部 戶口統計 9月; 2026 新生兒 預估 出生數 龍年 蛇年 馬年 生肖 台灣 少子化; 台灣 2026 出生 生肖 效應 馬年; 台灣 2025 出生人數 內政部 戶籍統計 月; 2026年 7月 出生數 內政部 戶口統計 新生兒; 好孕三方案 生育補助 10萬元 2026年上路

- `https://rwdnews.sanlih.com.tw/news/1763612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.4gtv.tv/article/2026013001000007` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.masterkl.com/78/hkej-give-birth-a-year-of-horse-baby-in-2026/` -> **snapshot** (snapshot 20260417120628); points raw/verified 15/14
  - p140 Start of 2026 Year of the Horse (立春) local time, date = **4** as written "2月4日", value check pending day of month (February) (2026-02-04..2026-02-04) [DISCARD: Lunar calendar date, not usable as a numeric input.] quote: "2026年立春(新曆2月4日)本地時間04:01起出生的嬰兒便屬馬"
  - p141 Start time of 2026 Year of the Horse (立春) local time = **401** as written "04:01", value check pending time of day (HH:MM) (2026-02-04..2026-02-04) [DISCARD: Lunar calendar time, not usable.] quote: "2026年立春(新曆2月4日)本地時間04:01起出生的嬰兒便屬馬"
  - p142 Frequency of 犯太歲 for people born in Horse year (every N years) = **6** year (not stated (page dated 2025-05-03)) [DISCARD: Zodiac superstition frequency, no measurable effect.] quote: "屬馬者每逢馬年與鼠年才會遇上犯太歲年,即每6年才犯一次太歲"
  - p143 Frequency of 犯太歲 for people born in Dog year (every N years) = **3** year (not stated (page dated 2025-05-03)) [DISCARD: Zodiac superstition frequency, no measurable effect.] quote: "相比肖狗者每隔3年便犯一次太歲的,少得多了"
  - p144 Start date of 庚子 month (子午相沖 period) in 2026 = **7** as written "2026年12月7日", value check pending day of month (December 2026) (2026-12-07..2026-12-07) [DISCARD: Lunar month date, not usable.] quote: "庚子月即新曆2026年12月7日至2027年1月5日"
  - p145 End date of 庚子 month (子午相沖 period) = **5** as written "2027年1月5日", value check pending day of month (January 2027) (2027-01-05..2027-01-05) [DISCARD: Lunar month date, not usable.] quote: "庚子月即新曆2026年12月7日至2027年1月5日"
  - p146 寅 month start (2026) date and time = **401** as written "2026年2月4日04:01", value check pending time of day (HH:MM) (2026-02-04..2026-02-04) [DISCARD: Lunar month date, not usable.] quote: "寅月(2026年2月4日04:01至3月5日21:57)"
  - p147 寅 month end (2026) date and time = **2,157** as written "3月5日21:57", value check pending time of day (HH:MM) (2026-03-05..2026-03-05) [DISCARD: Lunar month date, not usable.] quote: "寅月(2026年2月4日04:01至3月5日21:57)"
  - p148 卯 month start (2026) date and time = **2,158** as written "3月5日21:58", value check pending time of day (HH:MM) (2026-03-05..2026-03-05) [DISCARD: Lunar month date, not usable.] quote: "卯月(3月5日21:58至4月5日02:38)"
  - p149 卯 month end (2026) date and time = **238** as written "4月5日02:38", value check pending time of day (HH:MM) (2026-04-05..2026-04-05) [DISCARD: Lunar month date, not usable.] quote: "卯月(3月5日21:58至4月5日02:38)"
  - p150 申 month start (2026) date and time = **1,942** as written "8月7日19:42", value check pending time of day (HH:MM) (2026-08-07..2026-08-07) [DISCARD: Lunar month date, not usable.] quote: "申月(8月7日19:42至9月7日22:40)"
  - p151 申 month end (2026) date and time = **2,240** as written "9月7日22:40", value check pending time of day (HH:MM) (2026-09-07..2026-09-07) [DISCARD: Lunar month date, not usable.] quote: "申月(8月7日19:42至9月7日22:40)"
  - p152 酉 month start (2026) date and time = **2,241** as written "9月7日22:41", value check pending time of day (HH:MM) (2026-09-07..2026-09-07) [DISCARD: Lunar month date, not usable.] quote: "酉月(9月7日22:41至10月8日14:28)"
  - p153 酉 month end (2026) date and time = **1,428** as written "10月8日14:28", value check pending time of day (HH:MM) (2026-10-08..2026-10-08) [DISCARD: Lunar month date, not usable.] quote: "酉月(9月7日22:41至10月8日14:28)"
- `https://www.mnews.tw/external/mirrordaily72257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.parenting.com.tw/article/6002405` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160245185` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/11
  - p154 Taiwan registered births, September 2025 (monthly total) = **8,603** births registered (2025-09-01..2025-09-30) [DISCARD: Duplicate of p95 (September 2025 = 8,603).] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p155 Taiwan registered births, full year 2024 = **134,856** births registered (2024-01-01..2024-12-31) [keep: ] quote: "113 年(1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p156 Year-on-year change in Taiwan registered births, 2025 vs 2024 (percent) = **-20.05** % (2025-01-01..2025-12-31) [keep: ] quote: "[(2)-(1)]/(1)×100 -20.05 -0.91 -- -- -- --"
  - p157 Taiwan crude birth rate, full year 2025 (per 1,000 population) = **4.62** births per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "114 年(2) 107,812 200,268 -92,456 4.62 8.58 -3.96"
  - p158 Taiwan registered marriages (couples), full year 2024 = **123,061** couples married (2024-01-01..2024-12-31) [keep: ] quote: "113 年(1) 123,061 53,469 5.26 2.28"
  - p159 Taiwan registered marriages (couples), September 2025 = **5,844** couples married (2025-09-01..2025-09-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p160 Taiwan registered marriages (couples), October 2025 = **10,735** couples married (2025-10-01..2025-10-31) [keep: ] quote: "10,735 10,428 307 5.42 0.58 4.78 0.48 - 4.37 0.74 -"
  - p161 Taiwan registered births, October 2025 = **9,458** births registered (2025-10-01..2025-10-31) [DISCARD: Duplicate of p96.] quote: "9,458 4.78 1.31 - 4.36 1.40 - 4.67 0.96 -"
  - p162 Taiwan registered births, November 2025 = **7,946** births registered (2025-11-01..2025-11-30) [DISCARD: Duplicate of p97.] quote: "7,946 4.15 2.40 - 3.89 1.87 - 4.62 1.09 -"
  - p163 Taiwan registered births, December 2025 = **9,027** births registered (2025-12-01..2025-12-31) [DISCARD: Duplicate of p98.] quote: "9,027 4.56 1.74 - 4.01 1.75 - 4.62 1.14 -"
  - p164 Taiwan registered births, January-December 2025 cumulative (Table 29) = **107,812** births registered (2025-01-01..2025-12-31) [DISCARD: Duplicate of p99.] quote: "107,812 55,797 52,015 102,968 53,285 49,683"
- `https://www.sinchew.com.my/news/20260109/international/7174252` -> **snapshot** (snapshot 20260110002511); points raw/verified 15/15
  - p165 Taiwan total live births registered, full year 2025 = **107,812** births registered (2025-01-01..2025-12-31) [DISCARD: Duplicate of p99.] quote: "整体来看,去年1月至12月新生儿数仅有10万7812人。"
  - p166 Taiwan live births registered, single month December 2025 = **9,027** births registered (2025-12-01..2025-12-31) [DISCARD: Duplicate of p98.] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p167 Change in Taiwan monthly live births, December 2025 vs November 2025 = **1,081** births registered (2025-12-01..2025-12-31) [DISCARD: Duplicate of p78.] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p168 Change in Taiwan monthly live births, December 2025 vs December 2024 = **3,469** births registered (2025-12-01..2025-12-31) [DISCARD: Duplicate of p79.] quote: "去年12月单月新生儿出生数是9027人,比11月增加1081人,相比前年同期减少3469人。"
  - p169 Taiwan live births registered, full year 2024 = **134,856** births registered (2024-01-01..2024-12-31) [DISCARD: Duplicate of p68/p155.] quote: "2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p170 Taiwan live births registered, full year 2023 = **135,571** births registered (2023-01-01..2023-12-31) [DISCARD: Duplicate of p67.] quote: "2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p171 Taiwan live births registered, full year 2022 = **138,986** births registered (2022-01-01..2022-12-31) [DISCARD: Duplicate of p70.] quote: "2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p172 Taiwan live births registered, full year 2021 = **153,820** births registered (2021-01-01..2021-12-31) [DISCARD: Duplicate of p71.] quote: "2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p173 Taiwan live births registered, full year 2020 = **165,249** births registered (2020-01-01..2020-12-31) [DISCARD: Duplicate of p72.] quote: "2019年17万7767人、2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p174 Taiwan live births registered, full year 2019 = **177,767** births registered (2019-01-01..2019-12-31) [DISCARD: Duplicate of p73.] quote: "2018年18万1601人、2019年17万7767人、2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p175 Taiwan live births registered, full year 2018 = **181,601** births registered (2018-01-01..2018-12-31) [DISCARD: Duplicate of p74.] quote: "2017年19万3844人、2018年18万1601人、2019年17万7767人、2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p176 Taiwan live births registered, full year 2017 = **193,844** births registered (2017-01-01..2017-12-31) [DISCARD: Duplicate of p75.] quote: "台湾新生儿数自2016年起逐年下降,2016年20万8440人、2017年19万3844人、2018年18万1601人、2019年17万7767人、2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p177 Taiwan live births registered, full year 2016 = **208,440** births registered (2016-01-01..2016-12-31) [DISCARD: Duplicate of p76.] quote: "台湾新生儿数自2016年起逐年下降,2016年20万8440人、2017年19万3844人、2018年18万1601人、2019年17万7767人、2020年16万5249人、2021年15万3820人、2022年13万8986人、2023年13万5571人、2024年13万4856人,加上去年仅有10万余人,已连续10年下降。"
  - p178 Taiwan marriages registered (couples), full year 2025 = **104,376** couples married (2025-01-01..2025-12-31) [keep: ] quote: "在婚姻部分,去年结婚对数10万4376对,折合年粗结婚率为千分之4.47,相比2024年的12万3061对,减少1万8685对"
  - p179 Taiwan marriages registered (couples), full year 2024 = **123,061** couples married (2024-01-01..2024-12-31) [DISCARD: Duplicate of p158.] quote: "在婚姻部分,去年结婚对数10万4376对,折合年粗结婚率为千分之4.47,相比2024年的12万3061对,减少1万8685对"
- `http://hkcna.hk/docDetail.jsp?id=101105647&channel=2805` -> **snapshot** (snapshot 20250910213321); points raw/verified 15/14
  - p180 Taiwan live births registered in August 2025 (monthly total) = **8,464** births (2025-08-01..2025-08-31) [keep: ] quote: "今年8月,全台僅有8464名新生兒,較去年同期大減2成7"
  - p181 Taiwan live births registered in July 2025 (monthly total) = **8,939** births (2025-07-01..2025-07-31) [DISCARD: Duplicate of p106.] quote: "也比7月的8939人減少475人"
  - p182 Taiwan live births registered in May 2025 (record monthly low) = **8,433** births (2025-05-01..2025-05-31) [DISCARD: Duplicate of p104.] quote: "僅比今年5月8433人的最低紀錄略高"
  - p183 Taiwan live births registered January-August 2025 (cumulative) = **72,778** births (2025-01-01..2025-08-31) [keep: ] quote: "今年前8個月,台灣新生兒總數72778人"
  - p184 Year-on-year decline in Taiwan January-August births, 2025 vs 2024 = **13,000** births (2025-01-01..2025-08-31) [keep: ] quote: "比去年同期的85941人大減1.3萬餘人"
  - p185 Year-on-year decline in Taiwan August births, 2025 vs 2024 = **3,179** births (2025-08-01..2025-08-31) [keep: ] quote: "比去年同期少3179人"
  - p186 Year-on-year percentage decline in Taiwan August births, 2025 vs 2024 = **27** as written "2成7", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "較去年同期大減2成7"
  - p187 Taiwan crude birth rate for August 2025 (annualised) = **4.27** births per 1,000 people (2025-08-01..2025-08-31) [keep: ] quote: "折合年粗出生率千分之4.27"
  - p188 Taiwan marriages registered in August 2025 (monthly total) = **5,916** marriages (2025-08-01..2025-08-31) [keep: ] quote: "8月,台灣僅有5916對新人結婚"
  - p189 Taiwan divorces registered in August 2025 (monthly total) = **4,486** divorces (2025-08-01..2025-08-31) [keep: ] quote: "離婚卻錄得4486對"
  - p190 Taiwan deaths in August 2025 (monthly total) = **15,226** deaths (2025-08-01..2025-08-31) [keep: ] quote: "同期死亡人數15226人,出生人數不及死亡人數一半"
  - p191 Taiwan total population at end of August 2025 = **23,328,343** people (2025-08-31..2025-08-31) [keep: ] quote: "截至今年8月底,全台人口總數為2332萬8343人"
  - p192 Taiwan total households at end of August 2025 = **9,820,000** households (2025-08-31..2025-08-31) [keep: ] quote: "全台總戶數於8月底突破982萬戶,創歷史新高"
  - p193 Taiwan average household size at end of August 2025 = **2.37** people per household (2025-08-31..2025-08-31) [keep: ] quote: "但平均每戶僅2.37人,家庭規模持續縮小"
- `https://www.chinatimes.com/realtimenews/20251110002033-260410` -> **snapshot** (snapshot 20251114075436); points raw/verified 15/15
  - p194 Taiwan births registered in October (monthly count) = **9,458** births registered (2025-10-01..2025-10-31) [DISCARD: Duplicate of p96.] quote: "內政部指出,今年10月出生數9,458人,約每4.7分鐘出生一個嬰兒"
  - p195 Taiwan cumulative births registered January–October 2025 = **90,839** births registered (2025-01-01..2025-10-31) [keep: ] quote: "累計今年1至10月出生人數僅90,839人,全年恐難保12萬"
  - p196 Taiwan full-year 2025 births registered (stated bound: may not hold 120,000) = **120,000** births registered (2025-01-01..2025-12-31) [DISCARD: Stated bound, not a value; superseded by p99.] quote: "累計今年1至10月出生人數僅90,839人,全年恐難保12萬"
  - p197 Year-on-year change in Taiwan October births (percent) = **21.6** % (2025-10-01..2025-10-31) [keep: ] quote: "相比去年10月的出生人數大幅減少21.6%、少了2,612個新生娃"
  - p198 Year-on-year decrease in Taiwan October births (count) = **2,612** births registered (2025-10-01..2025-10-31) [DISCARD: Duplicate of p197 count.] quote: "相比去年10月的出生人數大幅減少21.6%、少了2,612個新生娃"
  - p199 Taiwan October deaths (monthly count) = **15,908** deaths (2025-10-01..2025-10-31) [keep: ] quote: "而10月死亡數為15,908人,平均約每2.8分鐘死亡一個人"
  - p200 Taiwan October net natural decrease (deaths minus births) = **6,450** persons (2025-10-01..2025-10-31) [keep: ] quote: "單月死亡比出生多了6,450人,全台已連續58個月「生不如死」"
  - p201 Taiwan annualised crude birth rate, October (per 1,000 population) = **4.78** births per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "折合年粗出生率為千分之4.78"
  - p202 Taiwan annualised crude death rate, October (per 1,000 population) = **8.03** deaths per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "折合年粗死亡率為千分之8.03"
  - p203 Taiwan annualised natural increase rate (per 1,000 population) = **-3.26** persons per 1,000 population (2025-10-01..2025-10-31) [keep: ] quote: "全國已連續58個月「生不如死」,折合年自然增加率為千分之-3.26"
  - p204 Taiwan total population at end of October (level) = **23,310,000** persons (2025-10-31..2025-10-31) [keep: ] quote: "全國總人口已連22月下跌至2,331萬人"
  - p205 Taiwan total population at end of 2023 (level) = **23,420,000** persons (2023-12-31..2023-12-31) [keep: ] quote: "從自2023年底的2,342萬人一路降至2,331萬人"
  - p206 Taiwan population aged 65+ at end of October (level) = **4,637,000** persons (2025-10-31..2025-10-31) [keep: ] quote: "截至10月底,全國65歲以上老年人口數續增至463.7萬人,佔比已達19.9%"
  - p207 Taiwan working-age population 15–64 at end of October (level) = **15,970,000** persons (2025-10-31..2025-10-31) [keep: ] quote: "「工作年齡人口(15~64歲)」也不及7成,約1,597萬人、占68.55%"
  - p208 Taiwan share of population aged 0–14 at end of October = **11.55** % (2025-10-31..2025-10-31) [keep: ] quote: "而幼年(0~14歲)人口佔比僅11.55%"
- `https://health.businessweekly.com.tw/article/ARTL003018867` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/newspapers/20260711000303-260120` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (number: more than one number in value_as_written: 1; value_as_written not in quote as a whole number: 4; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### d6 [forecasts_markets] Official projections and analyst forecasts

Hypothesis: Published 2026 birth projections or monthly forecasts (government, academia, media) provide an external anchor for the September 2026 level.

Queries issued by the searcher: Taiwan 2026 births forecast projection 出生數 預估; 2026 台灣 出生數 預估 少子化; 國發會 2026 人口推估 新生兒 9.4萬 八月二十八日 報告; 內政部 2026年8月 新生兒 7492 出生 統計 戶政司; Taiwan 2026 births forecast projection; 2026 台灣 出生數 預估 國發會 人口推估; 內政部 2026年8月 新生兒 7492 戶口統計 出生數; 2025年9月 台灣 出生數 新生兒 內政部 統計; 2026年7月 新生兒 7906 內政部 戶口統計 出生數; 2025年9月 新生兒出生數 內政部 戶口統計 9月出生; Taiwan 2026 births forecast projection; 2026 台灣 出生數 預估; 內政部 2026年8月 戶口統計 新生兒 7492 出生數; 國發會 2026年8月28日 人口推估 新聞稿 新生兒 9.4萬

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])7492(?!\\d|[.,]\\d)']; no pages fetched**


### b1 [own_history] d1

Hypothesis: August 2026 MOI monthly births (published ~early September 2026) would anchor the level one month closer to the target and materially tighten the series_auto/partial_period route.

Queries issued by the searcher: 內政部戶政司 出生登記 統計 2026年8月; Taiwan monthly births 2026 household registration August 2026 births registered; 內政部戶政司 115年7月 戶口統計 出生數 7906 公布; 台灣 2025年 9月 出生數 新生兒 內政部 戶政司 統計; 內政部 戶政司 出生數 統計 115年8月 出生登記; Taiwan monthly births registered August 2026 MOI Department of Household Registration; 內政部 115年7月 戶口統計 出生數 7月新生兒 7906; 2026年7月 台湾 出生数 内政部 戸口統計 新生児 8月10日発表; 內政部 戶政司 出生 統計 114年8月 出生登記; Taiwan August 2026 births registered monthly household registration statistics; 內政部 115年7月 戶口統計 出生數 7906 新生兒; 內政部戶政司 人口統計資料 歷月 出生數 115年 6月 7月 統計表

- `https://news.pts.org.tw/article/826497` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://turnnewsapp.com/livenews/politicsv3/20260810002102-260407` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1904770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/newspapers/20260811000520-260114?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160255313` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%8F%B0%E7%81%A3%E7%B8%BD%E4%BA%BA%E5%8F%A3%E9%80%A331%E5%80%8B%E6%9C%88%E8%B2%A0%E6%88%90%E9%95%B7-%E5%89%8D7%E6%9C%88%E6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/tag/3471?page=1&type=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.crntt.com/doc/1602/6/6/8/160266835.html?coluid=93&kindid=13830&docid=160266835` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/8%E6%9C%88%E6%96%B0%E7%94%9F%E5%85%92%E5%83%85%E5%89%A97492%E4%BA%BA-%E4%BA%BA%E5%8F%A3%E9%80%A332%E5%80%8B%E6%9C%88%E8%B2%A` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://pttweb.tw/Gossiping/M.1789013237.A.790` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] d2

Hypothesis: A monthly 2026 births series (Jan-Aug) from MOI would let a partial_period nowcast use the observed Jan-Aug share of the annual total, replacing the annual-projection route with a within-year coverage ratio.

Queries issued by the searcher: 內政部 戶政司 戶籍統計 出生 2026年 各月 出生登記; Taiwan Ministry of Interior monthly household registration births 2026; 內政部戶政司 戶籍人口統計速報 115年7月 出生數 統計表; ris.gov.tw 出生數 按月 統計 2026年 1月至7月 新生兒 累計; 內政部 戶政司 出生 統計 114年8月 出生數; Taiwan monthly registered births 2026 statistics Department of Household Registration; 2026年6月 出生數 戶口統計 新生兒 內政部; ris.gov.tw 戶籍人口統計速報 115年7月 出生數; 內政部 戶籍人口統計 出生人數 2026年 每月; Taiwan monthly registered births 2026 Ministry of Interior household registration statistics; 內政部戶政司 人口統計資料 出生數 按月 統計表 中華民國115年 ris.gov.tw; 2026年6月新生兒 7324人 內政部 上半年 4萬6344

- `https://www.economy.com/taiwan-china/births/not-seasonally-adjusted` -> **snapshot** (snapshot 20230327075810); points raw/verified 14/10
  - p209 Registered births in Taiwan, January 2023 (monthly, NSA) = **10,948** births (2023-01-01..2023-01-31) [keep: ] quote: "\| Births \| Jan 2023 \| 10,948 \| 12,178 \| #, NSA \| Monthly \|"
  - p210 Registered births in Taiwan, December 2022 (monthly, NSA, previous value) = **12,178** births (2022-12-01..2022-12-31) [keep: ] quote: "\| Births \| Jan 2023 \| 10,948 \| 12,178 \| #, NSA \| Monthly \|"
  - p211 Birth rate in Taiwan, January 2023 (per thousand population, NSA) = **0.47** births per 1,000 population (2023-01-01..2023-01-31) [keep: ] quote: "\| Birth Rate \| Jan 2023 \| 0.47 \| 0.52 \| # per Ths. pop., NSA \| Monthly \|"
  - p212 Birth rate in Taiwan, December 2022 (per thousand population, NSA, previous valu = **0.52** births per 1,000 population (2022-12-01..2022-12-31) [keep: ] quote: "\| Birth Rate \| Jan 2023 \| 0.47 \| 0.52 \| # per Ths. pop., NSA \| Monthly \|"
  - p213 Registered population in Taiwan, end of January 2023 (EOM stock, NSA) = **23,301,968** person (2023-01-31..2023-01-31) [keep: ] quote: "\| Population \| Jan 2023 \| 23,301,968 \| 23,264,640 \| # EOM, NSA \| Monthly \|"
  - p214 Registered population in Taiwan, end of December 2022 (EOM stock, NSA, previous  = **23,264,640** person (2022-12-31..2022-12-31) [keep: ] quote: "\| Population \| Jan 2023 \| 23,301,968 \| 23,264,640 \| # EOM, NSA \| Monthly \|"
  - p215 Registered deaths in Taiwan, January 2023 (monthly, NSA) = **17,770** deaths (2023-01-01..2023-01-31) [keep: ] quote: "\| Deaths \| Jan 2023 \| 17,770 \| 17,685 \| #, NSA \| Monthly \|"
  - p216 Registered deaths in Taiwan, December 2022 (monthly, NSA, previous value) = **17,685** deaths (2022-12-01..2022-12-31) [keep: ] quote: "\| Deaths \| Jan 2023 \| 17,770 \| 17,685 \| #, NSA \| Monthly \|"
  - p217 Death rate in Taiwan, January 2023 (per thousand population, NSA) = **0.76** deaths per 1,000 population (2023-01-01..2023-01-31) [keep: ] quote: "\| Death Rate \| Jan 2023 \| 0.76 \| 0.76 \| # per Ths. pop., NSA \| Monthly \|"
  - p218 Net migration in Taiwan, 2021 (annual, NSA) = **-156,010** person (2021-01-01..2021-12-31) [keep: ] quote: "\| Net Migration \| 2021 \| -156,010 \| -33,978 \| #, NSA \| Annual \|"
- `https://www.moi.gov.tw/News_Content.aspx?n=2&s=340017` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/info-liferay/app/channel/newsDetail/26218233?p=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mombaby.com.tw/articles/9937899` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cenantc.pckids.com.tw/board/title_show.asp?titleid=56426&kind=B3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p219 Taiwan total population, July 2026 (month-end) = **23,235,002** person (2026-07-01..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長"
  - p220 Live births registered in Taiwan, July 2026 = **7,906** births registered (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p221 Live births registered in Taiwan, May 2026 = **6,832** births registered (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p222 Live births registered in Taiwan, June 2026 = **7,324** births registered (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p223 Year-on-year change in July 2026 live births, Taiwan = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p224 Year-on-year decrease in July 2026 live births, Taiwan (count) = **1,033** births registered (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p225 Crude birth rate, Taiwan, July 2026 (annualised) = **4.01** births per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p226 Deaths registered in Taiwan, July 2026 = **17,119** deaths registered (2026-07-01..2026-07-31) [keep: ] quote: "至於7月死亡人數則為1萬7119人,平均約每2.6分鐘有一人死亡"
  - p227 Crude death rate, Taiwan, July 2026 (annualised) = **8.67** deaths per 1,000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%"
  - p228 Year-on-year change in Taiwan total population, July 2026 vs July 2025 = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p229 Month-on-month change in Taiwan total population, July 2026 vs June 2026 = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "與6月相比則減少0.04%,是連續31個月出現人口負成長"
  - p230 Consecutive months of population decline, Taiwan, through July 2026 = **31** month (2026-07-01..2026-07-31) [keep: ] quote: "是連續31個月出現人口負成長"
  - p231 Share of population aged 65+, Taiwan, end of July 2026 = **20.54** % (2026-07-01..2026-07-31) [keep: ] quote: "截自7月底,台灣年齡分布持續呈現超高齡化,65歲以上人口占20.54%"
  - p232 Share of population aged 15-64, Taiwan, end of July 2026 = **68.15** % (2026-07-01..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
  - p233 Share of population aged 0-14, Taiwan, end of July 2026 = **11.3** % (2026-07-01..2026-07-31) [keep: ] quote: "15至64歲人口占68.15%、0至14歲占11.30%"
- `https://hk.crntt.com/doc/1602/1/8/7/160218724.html?coluid=46&docid=160218724&kindid=21997` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.icrt.com.tw/info_details.php?mlevel1=6&mlevel2=13&news_id=301625` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.qq.com/rain/a/20260610A092PB00` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=c30c5419d024492296728a1b4c373516` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/421847` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end missing or unparseable: 2; number: more than one number in value_as_written: 2)

### b3 [shocks] d5

Hypothesis: Any 2026 birth-incentive policy (e.g. new subsidy effective mid-2026) or registration-lag change could shift September registrations; quantifying exposure would resolve whether the recent uptick (May->July) is policy-driven or noise.

Queries issued by the searcher: 台灣 2026 生育補助 新制 上路 日期; 行政院 少子女化 對策 2.0 生育給付 2026 每胎 十萬; 內政部 戶政司 統計 115年7月 出生數 出生登記; 2026年 7月 出生數 台灣 內政部 統計 較上月 增加; 行政院 2026 生育補助 新制 上路; Taiwan 2026 birth subsidy policy change effective date 生育補助; 內政部 戶籍統計 2026年7月 出生數 新生兒 統計; 台灣 2026年 上半年 出生人數 內政部 統計 較去年同期; 台灣 2026 生育補助 新制 行政院 上路 日期; Taiwan 2026 birth subsidy new policy effective date Executive Yuan; 內政部 戶政司 出生數 統計 115年 每月 出生登記; 2026年 各縣市 生育津貼 加碼 上路 7月 8月 9月 生效

- `https://www.hl.gov.tw/News_Content.aspx?n=32725&s=233070` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bwplus.com.tw/wpstudy/article/1129580567.html` -> **snapshot** (snapshot 20260516171452); points raw/verified 15/15
  - p234 Taiwan expanded birth subsidy scheme (擴大生育補助方案) effective date, year = **2,026** year (2026-01-01..2026-12-31) [keep: ] quote: "勞動部於2026年(民國115年)1月1日起推動「擴大生育補助方案」"
  - p235 Total central birth benefit per single birth under 2026 scheme (original insuran = **100,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "只要生一胎就加發補助至10萬元"
  - p236 Total central birth benefit for twins under 2026 scheme (2x single-birth amount) = **200,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "雙胞胎合計可領20萬元"
  - p237 Total central birth benefit for triplets under 2026 scheme (3x single-birth amou = **300,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "3胞胎(3倍)則為30萬元"
  - p238 Estimated number of people to receive retroactive top-up payment (back pay recip = **18,000** person (2026-01-01..2026-05-11) [keep: ] quote: "預計補發對象約1.8萬人"
  - p239 Announcement date of retroactive top-up execution (Executive Yuan approval), dat = **20,260,506** as written "2026年5月6日", value check pending date (2026-05-06..2026-05-06) [keep: ] quote: "勞動部於2026年5月6日宣布,行政院已同意執行新興計畫動支案"
  - p240 Deadline for retroactive top-up payments to be credited (before Mother's Day), d = **511** as written "5月11日", value check pending date (2026-05-11..2026-05-11) [keep: ] quote: "生育給付加發至10萬元的差額將於母親節(5月11日)前陸續入帳"
  - p241 National pension (國保) monthly insured amount from 2026-01-01, TWD = **21,103** TWD (2026-01-01..2026-12-31) [keep: ] quote: "國保月投保金額自115年1月1日起調高至2萬1103元"
  - p242 National pension (國保) birth benefit: 2 months of insured amount, TWD = **42,206** TWD (2026-01-01..2026-12-31) [keep: ] quote: "按月投保金額一次發給2個月,合計可領4萬2206元"
  - p243 Government top-up difference for national pension birth benefit to reach 100,000 = **57,794** TWD (2026-01-01..2026-12-31) [keep: ] quote: "政府將自動補足差額5萬7794元"
  - p244 Labor insurance (勞保) birth benefit: months of average monthly insured salary pai = **2** month (2026-01-01..2026-12-31) [keep: ] quote: "按前6個月平均月投保薪資發給2個月"
  - p245 Labor insurance (勞保) minimum insured days required for birth benefit at full-ter = **280** day (2026-01-01..2026-12-31) [keep: ] quote: "加保滿280日分娩(早產181日)"
  - p246 Labor insurance (勞保) minimum insured days required for birth benefit at prematur = **181** day (2026-01-01..2026-12-31) [keep: ] quote: "加保滿280日分娩(早產181日)"
  - p247 Labor insurance (勞保) birth benefit example: original benefit for average monthly = **70,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "若產婦前6個月平均月投保薪資為3萬5000元,原勞保生育給付可領7萬元"
  - p248 Labor insurance (勞保) birth benefit example: government top-up difference to reac = **30,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "2026年起,政府將自動補足3萬元差額,產婦最終實領總額為10萬元"
- `https://www.parenting.com.tw/article/5091069` -> **snapshot** (snapshot 20230415061610); points raw/verified 0/0
- `https://ocacnews.net/article/408541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://futureparenting.cwgv.com.tw/family/content/index/36367` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cenantc.pckids.com.tw/board/title_show.asp?titleid=56160&kind=B3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mammyvillage.com/blogs/mammyvillageblog/182850` -> **snapshot** (snapshot 20260520035106); points raw/verified 15/15
  - p249 Central government birth subsidy per live birth, effective 2026-01-01 (Taiwan) = **100,000** TWD per live birth (2026-01-01..2026-12-31) [keep: ] quote: "自2026年1月1日起,每生一胎中央補助10萬元"
  - p250 Public childcare subsidy monthly amount from January 2024 (Taiwan) = **7,000** TWD per child per month (2024-01-01..2024-01-31) [keep: ] quote: "公共化托育補助:113年1月起每月7,000元起"
  - p251 Quasi-public childcare subsidy monthly amount from January 2024 (Taiwan) = **13,000** TWD per child per month (2024-01-01..2024-01-31) [keep: ] quote: "準公共托育補助:113年1月起每月13,000元起"
  - p252 Additional childcare subsidy for second child (Taiwan) = **1,000** TWD per child (not stated (page dated 2025-02-24)) [keep: ] quote: "第2名子女加發1,000元"
  - p253 Additional childcare subsidy for third or later child (Taiwan) = **2,000** TWD per child (not stated (page dated 2025-02-24)) [keep: ] quote: "第3名以上子女加發2,000元(胎次計算)"
  - p254 Total parental leave allowance entitlement period (Taiwan) = **2** year (not stated (page dated 2025-02-24)) [keep: ] quote: "總額度共2年,父母在其中各有30 天可按「單日」申請,合計60天。"
  - p255 Flexible parental leave days per parent (Taiwan) = **30** day per parent (not stated (page dated 2025-02-24)) [keep: ] quote: "父母在其中各有30 天可按「單日」申請,合計60天。"
  - p256 Combined flexible parental leave days for both parents (Taiwan) = **60** day (not stated (page dated 2025-02-24)) [keep: ] quote: "父母在其中各有30 天可按「單日」申請,合計60天。"
  - p257 Parental leave allowance wage replacement rate (Taiwan) = **8** % of salary (not stated (page dated 2025-02-24)) [keep: ] quote: "按日申請期間,一樣可請領8成薪的育嬰留停津貼!"
  - p258 Standard advance notice days for flexible parental leave application (Taiwan) = **5** day (not stated (page dated 2025-02-24)) [keep: ] quote: "一般情況5日前提出;緊急狀況(如子女停課)可於1日前提出!"
  - p259 Emergency advance notice days for flexible parental leave application (Taiwan) = **1** day (not stated (page dated 2025-02-24)) [keep: ] quote: "一般情況5日前提出;緊急狀況(如子女停課)可於1日前提出!"
  - p260 Original parental leave allowance entitlement period included in flexible leave  = **6** month (not stated (page dated 2025-02-24)) [keep: ] quote: "這30天的「彈性育嬰假」津貼,是包含在原本6個月的津貼總額度內的唷!"
  - p261 Age threshold for childcare allowance eligibility (Taiwan) = **2** year of age (not stated (page dated 2025-02-24)) [keep: ] quote: "補助資格:未滿2歲之幼兒,完成出生登記或初設戶籍登記"
  - p262 Lower age bound of education subsidy stage (Taiwan) = **2** year of age (not stated (page dated 2025-02-24)) [keep: ] quote: "細分為「2至未滿5歲」與「滿5歲至入國民小學前」兩個階段"
  - p263 Upper age bound of first education subsidy stage (Taiwan) = **5** year of age (not stated (page dated 2025-02-24)) [keep: ] quote: "細分為「2至未滿5歲」與「滿5歲至入國民小學前」兩個階段"
- `https://www.sjtv.com.tw/articles/96120` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/%e8%b3%b4%e6%b8%85%e5%be%b7%e6%8e%a818%e9%a0%85%e5%ae%b6%e5%ba%ad%e6%94%af%e6%8c%81%e6%96%b0%e5%88%b6-%e6%9c%80%e5%bf%ab%e6%98%8` -> **snapshot** (snapshot 20260611202753); points raw/verified 15/4
  - p264 Current maternity leave duration (weeks) before planned extension = **8** week/maternity leave (not stated (page dated 2026-05-27)) [keep: ] quote: "新制規劃將現行8週產假延長為12週"
  - p265 Current paternity/prenatal-check leave days before planned increase = **7** day/paternity leave (not stated (page dated 2026-05-27)) [keep: ] quote: "另陪產檢及陪產假則由7日提高至14日"
  - p266 Current marriage leave days before planned increase = **8** day/marriage leave (not stated (page dated 2026-05-27)) [keep: ] quote: "婚假也將比照軍公教,由8日增加至14日"
  - p267 Current annual days of parental leave claimable by day before upgrade = **30** day/parent/year (not stated (page dated 2026-05-27)) [keep: ] quote: "目前以日申請的30日育嬰留停,也將升級改為60日「育兒假」"
- `https://turnnewsapp.com/livenews/politicsv3/20260528002583-260407` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mnews.tw/external/mirrordaily63444` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (period year 2027 does not appear in the page text or URL (likely mis-dated): 11)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'taiwan birth rate', 'september 2026 births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p2', 'p18'] Same May 2026 MOI registration count (6,832) reported by two outlets; one underlying measurement, not independent confirmation.
- corroborating: ['p3', 'p32'] April 2026 births ~8,000-8,144; p32 is a rounded press paraphrase of the same MOI release, so p3 is the precise version.
- corroborating: ['p4', 'p126'] February 2026 births 6,523 in two outlets; same MOI figure.
- corroborating: ['p17', 'p20', 'p21'] July 2026 births 7,906 with -11.56% YoY and -1,033 count are internally consistent (7,906+1,033=8,939 = July 2025).
- corroborating: ['p17', 'p106'] July 2026 (7,906) vs July 2025 (8,939) matches the stated -1,033 YoY change.
- corroborating: ['p18', 'p19', 'p17'] May 6,832, June 7,324, July 7,906 form a consistent recent monthly sequence from the same MOI series.
- corroborating: ['p95', 'p154'] Duplicate of September 2025 registered births (8,603) from the same RIS table.
- corroborating: ['p96', 'p161'] Duplicate October 2025 births (9,458).
- corroborating: ['p97', 'p162'] Duplicate November 2025 births (7,946).
- corroborating: ['p98', 'p163', 'p77', 'p166'] December 2025 births 9,027 across RIS table and press; same MOI source.
- corroborating: ['p99', 'p164', 'p165', 'p69'] Full-year 2025 births 107,812 consistent across RIS table and press.
- corroborating: ['p52', 'p53'] Jan-Jul 2026 ~54,000 and NDC full-year 2026 projection 94,000 are from the same article; the annual projection is a forecast, not an observation.
- corroborating: ['p41', 'p55'] TFR 2025 = 0.695 in both NDC and press; same underlying statistic.
- conflicting: ['p110', 'p111', 'p112', 'p117', 'p121', 'p122'] georank.org TFR (~0.88-0.89) and births-per-1000-women figures conflict with official MOI/NDC TFR (0.695 in 2025); georank appears to use stale or different-vintage data and is not reliable for 2026 l
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p169', 'p170', 'p171', 'p172', 'p173', 'p174', 'p175', 'p176', 'p177'] Annual birth series 2016-2025 consistent across press and RIS; shows steep decline, especially 2024->2025 (-20%).
- corroborating: ['p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153'] Lunar/astrological calendar dates; internally consistent but of dubious causal relevance to birth registration.
- corroborating: ['p31', 'p38', 'p39', 'p82'] Average age at first birth ~31.8-32 years, consistent across sources.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p2', 'p18', 'p221'] Same May 2026 MOI registration count (6,832) reported by two outlets; identical underlying MOI release, so one measurement, not independent confirmation.
- corroborating: ['p17', 'p220'] Same July 2026 MOI count (7,906) from the same release; duplicate reporting.
- corroborating: ['p19', 'p222'] Same June 2026 count (7,324); duplicate.
- corroborating: ['p20', 'p21', 'p223', 'p224'] July 2026 YoY decline of 1,033 births / 11.56% is internally consistent with p17 and p106 (8,939 - 1,033 = 7,906); same release.
- corroborating: ['p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107'] Official RIS/MOI monthly registration series for 2025; internally consistent (months sum to the 107,812 annual total p99). This is the authoritative vintage for the September seasonal anchor.
- corroborating: ['p69', 'p99', 'p155', 'p156'] 2025 annual births 107,812 and 2024 134,856 agree across the news and RIS sources; the -20.05% YoY is consistent with those two levels.
- corroborating: ['p52', 'p53'] Jan-Jul 2026 cumulative ~54,000 and NDC full-year projection 94,000 are mutually consistent (54,000/94,000 ≈ 0.57, close to the historical 7/12 share), so the NDC projection embeds the observed 2026 l
- corroborating: ['p52', 'p17', 'p18', 'p19'] Sum of May+June+July 2026 (6,832+7,324+7,906=22,062) is compatible with a Jan-Jul total of ~54,000 given the low Feb-Apr months (p4, p3).
- corroborating: ['p41', 'p55'] 2025 TFR 0.695 reported identically by NDC and news; same MOI-derived statistic.
- corroborating: ['p54', 'p55'] TFR fell from 0.885 (2024) to 0.695 (2025), consistent with the -20% birth drop; same source family.
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76'] Consistent annual birth series 2016-2025 showing steady decline; useful for trend context but not for a monthly September level.
- corroborating: ['p77', 'p98'] December 2025 = 9,027 in both news and RIS; duplicate.
- corroborating: ['p1', 'p16', 'p219'] Population levels May/July 2026 consistent with ongoing decline; context only.
- corroborating: ['p4', 'p126'] February 2026 = 6,523 in two outlets; duplicate.
- conflicting: ['p3', 'p32'] April 2026 exact 8,144 vs discarded 'just over 8,000' approximation; the exact figure supersedes the rounded one.
- corroborating: ['p95', 'p154'] September 2025 = 8,603 in both RIS and news; duplicate.
- conflicting: ['p110', 'p111', 'p112', 'p41', 'p54', 'p55'] Discarded TFR points (0.88/0.89) conflict with the official 0.695/0.885; the discarded ones are unreliable and excluded.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY change factor vs September 2025 | 0.9 | 0.78..1.02 | 0.78..1.02 | 1 | m1 (m1) | Recent 2026 months run below 2025: July 2026 was -11.56% YoY (p20/p223), and the 2026 level (Jan-Jul ~54,000, p52) is well below 2025. September 2025 was 8,603 (p95). A factor near 0.90 with wide range reflects the observed ~10-12% decline plus uncertainty. | September 2026 continues the 2026 YoY decline seen in July. | Evidence that 2026 births have stabilized or rebounded to 2025 levels. |
| a2 | September share of annual births | 0.083 | 0.075..0.092 | 0.05874..0.1175 (widened) | 1 | m2 (m2) | September 2025 was 8,603 of 107,812 annual (p95/p99) ≈ 0.0798; typical September share is near 1/12 ≈ 0.083. Range covers seasonal variation. | September 2026 has a similar seasonal share as prior years. | A large shift in the seasonal birth pattern. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 7,665 | ['p95'] / ['a1'] | [] |  | 1.00 | B1 of 3 blocks; median of blocks: this block is the median |  |
| m2 | formula_mc | 7,806 | ['p53'] / ['a2'] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m3 | series_auto | 7,206 | ['p104', 'p105', 'p106', 'p95', 'p18', 'p19', 'p17'] / [] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Method details (computed by code):

- m1 formula_mc: p95 * a1; Monte Carlo P10 to P90 6,105 to 9,633; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p53 * a2; Monte Carlo P10 to P90 5,273 to 11,580; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p104), 2025-06 (p105), 2025-07 (p106), 2025-09 (p95), 2026-05 (p18), 2026-06 (p19), 2026-07 (p17) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 3 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy\|pairs3\|h2 of table bench-d12f86e0-1013c974)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,665 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,806 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 7,206 (width x/÷1.23, benchmark calibration). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.37; Birge ratio 0.20 (not above one, so no widening); final width x/÷1.37.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p95, from m3); the estimate is -10.9% against it.

Result: central **7,665** birth, 80% interval [5,587, 10,514] birth, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for births registered in Taiwan during September 2026 (MOI monthly household registration statistics, by date of registration) is 7,665 birth (80% model-based interval 5,587 to 10,514 birth).

Main evidence: September 2025 registered 8,603 births registered; the NDC full-year 2026 projection is 94,000 births; recent 2026 months (6,832 births registered, 7,324 births registered, 7,906 births registered) show a decline. Method m1 scales the September 2025 anchor by an assumed YoY factor 0.9 (range 0.78 to 1.02); m2 applies an assumed September share 0.083 (range 0.05874 to 0.1175) to the annual projection; m3 extrapolates the registration series. Only the observed points are data; the factors and shares are analyst assumptions, and the series forecast is a transfer.

Code combined three non-overlapping blocks with equal weight per block, taking the median; widths came from default, Monte Carlo, and benchmark calibration, not backtest errors.

Biggest risk: a policy-driven rebound from the 2026 birth subsidy, or registration timing shifts. Better evidence would be August 2026 registrations and any subsidy take-up data.

Unit of the estimate: birth (births registered in September 2026; total for 2026-09-01 to 2026-09-30).

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY change factor vs September 2025: 0.9 [n], range 0.78 to 1.02; used by m1. Overturned by: Evidence that 2026 births have stabilized or rebounded to 2025 levels.
- a2 September share of annual births: 0.083 [n], range 0.05874 to 0.1175 (range widened by code); used by m2. Overturned by: A large shift in the seasonal birth pattern.

Method details (computed by code):
- m1 formula_mc: p95 * a1; Monte Carlo P10 to P90 6,105 to 9,633; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p53 * a2; Monte Carlo P10 to P90 5,273 to 11,580; result unit (birth/month) * 1 month converted to birth; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p104), 2025-06 (p105), 2025-07 (p106), 2025-09 (p95), 2026-05 (p18), 2026-06 (p19), 2026-07 (p17) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 3 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy|pairs3|h2 of table bench-d12f86e0-1013c974)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 7,665 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 7,806 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 7,206 (width x/÷1.23, benchmark calibration). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.37; Birge ratio 0.20 (not above one, so no widening); final width x/÷1.37.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p95, from m3); the estimate is -10.9% against it.

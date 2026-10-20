# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of live births registered (出生登記) in Taiwan during September 2026, as published in the Ministry of the Interior's monthly household registration statistics (戶口統計 / 人口統計月報), national total (all counties/cities), counted by registration date (登記日期) rather than by date of occurrence | unit births registered in September 2026 (persons) | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior, Department of Household Registration (內政部戶政司) — monthly household registration / population statistics bulletin, typically released around the 8th–10th of the following month

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] vital-statistics compiler (MOI household registration)

Hypothesis: Monthly registered births have a fairly stable within-year seasonal shape plus a declining trend, so September 2026 can be anchored either by September 2025 scaled by the recent year-on-year ratio, or by the 2026 year-to-date monthly average scaled by the historical September seasonal index. The relationship is direct (same definition, same publisher) and needs only a stable-shape assumption.

Queries issued by the searcher: 內政部 戶口統計 出生人數 114年9月; 台灣 每月 出生人數 統計 2025 2026 戶政司; 內政部 戶口統計 109年9月 出生數 1萬6千 出生人數 各月; 2026年6月 出生數 內政部 戶口統計 新生兒 7月7906人

- `https://www.moi.gov.tw/News_Content.aspx?n=2&s=332339` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/tag/13920` -> **snapshot** (snapshot 20260416072218); points raw/verified 15/13
  - p1 Taiwan national registered births, March 2026 (monthly count) = **8,798** persons (2026-03-01..2026-03-31) [keep: ] quote: "3月出生數為8798人,比上個月增加2275人,增加幅度為34.88%。"
  - p2 Taiwan national registered births, February 2026 (monthly count) = **6,523** persons (2026-02-01..2026-02-28) [keep: ] quote: "今(2026)年2月新生兒數共6523人,較1月大減25%,創單月史上新低"
  - p3 Month-on-month change in Taiwan registered births, March 2026 vs February 2026 = **2,275** persons (2026-03-01..2026-03-31) [keep: ] quote: "3月出生數為8798人,比上個月增加2275人,增加幅度為34.88%。"
  - p4 Month-on-month percent change in Taiwan registered births, February 2026 vs Janu = **25** % (2026-02-01..2026-02-28) [keep: ] quote: "今(2026)年2月新生兒數共6523人,較1月大減25%,創單月史上新低"
  - p5 Month-on-month percent increase in Taiwan registered births, March 2026 vs Febru = **34.88** % (2026-03-01..2026-03-31) [keep: ] quote: "3月出生數為8798人,比上個月增加2275人,增加幅度為34.88%。"
  - p6 Taiwan national registered births, March 2026 (rounded, as stated in second arti = **8,000** persons (2026-03-01..2026-03-31) [keep: ] quote: "不過3月新生兒有8000多人,比2月增加2000多人,止跌回升。"
  - p7 Taiwan total population, end of March 2026 = **23,270,568** persons (2026-03-31..2026-03-31) [keep: ] quote: "截至3月底,台灣人口數為2327萬568人,已連續27個月負成長。"
  - p8 Taiwan total population, end of February 2026 = **23,280,273** persons (2026-02-28..2026-02-28) [keep: ] quote: "截至今年2月底台灣總人口數為2328萬273人,已連續26個月負成長"
  - p9 Year-on-year decrease in Taiwan total population, February 2026 vs February 2025 = **104,000** persons (2026-02-01..2026-02-28) [keep: ] quote: "與去(2025)年同期相比減少10.4萬人。"
  - p10 Year-on-year decrease in Taiwan total population, March 2026 vs March 2025 = **104,000** persons (2026-03-01..2026-03-31) [keep: ] quote: "比去(2025)年同期減少10萬4000多人,連續27個月負成長"
  - p11 Taiwan total population, end of July 2025 = **23,330,000** persons (2025-07-31..2025-07-31) [keep: ] quote: "截至今(2025)年7月底,人口總數為2333萬多人,人口連續19個月負成長"
  - p12 Taiwan women's mean age at first birth, 2024 = **31.7** years (2024-01-01..2024-12-31) [keep: ] quote: "去(2024)年台灣婦女第1胎生育年齡為31.7歲,比20年前增加5歲"
  - p13 Taiwan national residential price index, 2025 Q3 = **145** index (2025-07-01..2025-09-30) [keep: ] quote: "2025年第三季全國指數為145.46,已連續3季下跌"
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/d3f3447c-5be7-4398-8d3e-da1867d3bc9c.pdf` -> **snapshot** (snapshot 20240221224234); points raw/verified 15/14
  - p14 Taiwan national registered births, September 2019 (monthly, by registration date = **14,533** persons (2019-09-01..2019-09-30) [keep: ] quote: "總 計 Grand Total 11,704,227 23,593,783 11,889,556 14,533 13,866 667 0.34"
  - p15 Taiwan national registered births, August 2019 (monthly, by registration date) = **14,330** persons (2019-08-01..2019-08-31) [keep: ] quote: "總 計 Grand Total 11,705,234 23,593,794 11,888,560 14,330 13,983 347 0.17"
  - p16 Taiwan national registered births, July 2019 (monthly, by registration date) = **15,104** persons (2019-07-01..2019-07-31) [keep: ] quote: "總 計 Grand Total 11,705,811 23,592,598 11,886,787 15,104 15,854 750 - 0.37 -"
  - p17 Taiwan national cumulative registered births, July–September 2019 (Table 7 total = **43,967** persons (2019-07-01..2019-09-30) [keep: ] quote: "計 Total 43,967 42,239 612 1,115 1 43,703"
  - p18 Taiwan national registered births, September 2019, male = **7,515** persons (2019-09-01..2019-09-30) [keep: ] quote: "總 計 Grand Total 男 Male 7,515 7,232 106 177 - 8,148"
  - p19 Taiwan national registered births, September 2019, female = **7,018** persons (2019-09-01..2019-09-30) [keep: ] quote: "女 Female 7,018 6,722 92 203 1 5,718"
  - p20 Taiwan national registered births, August 2019, male = **7,427** persons (2019-08-01..2019-08-31) [keep: ] quote: "總 計 Grand Total 男 Male 7,427 7,142 89 196 - 8,190"
  - p21 Taiwan national registered births, August 2019, female = **6,903** persons (2019-08-01..2019-08-31) [keep: ] quote: "女 Female 6,903 6,614 122 167 - 5,793"
  - p22 Taiwan national registered births, July 2019, male = **7,803** persons (2019-07-01..2019-07-31) [keep: ] quote: "總 計 Grand Total 男 Male 7,803 7,503 101 199 - 9,248"
  - p23 Taiwan national registered births, July 2019, female = **7,301** persons (2019-07-01..2019-07-31) [keep: ] quote: "女 Female 7,301 7,026 102 173 - 6,606"
  - p24 Taiwan national registered births, September 2019, legitimate = **13,954** persons (2019-09-01..2019-09-30) [keep: ] quote: "計 Total 14,533 13,954 198 380 1 13,866"
  - p25 Taiwan national registered births, August 2019, legitimate = **13,756** persons (2019-08-01..2019-08-31) [keep: ] quote: "計 Total 14,330 13,756 211 363 - 13,983"
  - p26 Taiwan national registered births, July 2019, legitimate = **14,529** persons (2019-07-01..2019-07-31) [keep: ] quote: "計 Total 15,104 14,529 203 372 - 15,854"
  - p27 Taiwan national live births, calendar year 2018 (by date of occurrence) = **180,656** persons (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 1; value_as_written not in quote as a whole number: 2)

### d2 [forecasts_markets] official projections and full-year forecasts

Hypothesis: September births equal the 2026 annual birth total multiplied by September's share of annual births (historically a fairly narrow band). Full-year 2026 forecasts or targets from 國發會/內政部 projections and mid-year media or expert forecasts therefore give an independent level anchor, cross-checking d1.

Queries issued by the searcher: 2026年 出生數 預估 台灣 全年 國發會 人口推估; 台灣 2026 上半年 出生人數 全年 預測 新生兒; 內政部 戶口統計 2025年9月 出生數 歷年 各月 出生人數 統計表; 台灣 每年9月 出生數 占全年 比例 歷年 月別 出生人數 2015 2016 2017

- `https://pchome.megatime.com.tw/news/cat8/20260828/17879076111121718003.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://futureparenting.cwgv.com.tw/family/content/index/36251` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/410298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [administrative] household registration office processing birth registrations

Hypothesis: Registered births in month m = births occurring in m that are registered within m + late registrations of births from m-1 and earlier. The lag distribution is administratively determined (60-day legal window), so a stable same-month registration share lets us convert an occurrence-based forecast into a registration-based one, or calibrate a registration-only trend.

Queries issued by the searcher: 出生登記 發生日期 登記日期 統計 內政部; 台灣 出生 至 登記 間隔 天數 統計 戶政; 人口統計季刊 出生 按登記日期 按發生日期 比較 表 內政部; 內政部 戶政司 2026年 出生登記數 每月 統計 新生兒

- `https://www.ris.gov.tw/documents/data/5/2/d3f3447c-5be7-4398-8d3e-da1867d3bc9c.pdf` -> **snapshot** (snapshot 20240221224234); points raw/verified 15/15
  - p28 Taiwan national total live births 2018 by date of occurrence (Table 8 Grand Tota = **180,656** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p29 Taiwan national total live births 2018 registered within 15 days of occurrence ( = **76,414** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p30 Taiwan national total live births 2018 registered 15 days to under 1 month after = **51,299** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p31 Taiwan national total live births 2018 registered 1 to under 2 months after occu = **51,579** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p32 Taiwan national total live births 2018 registered 2 to under 3 months after occu = **1,271** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p33 Taiwan national total live births 2018 registered 3 to under 4 months after occu = **38** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p34 Taiwan national total live births 2018 registered 4 to under 5 months after occu = **8** live births (2018-01-01..2018-12-31) [keep: ] quote: "總 計 Grand Total 180,656 76,414 51,299 51,579 1,271 38 8"
  - p35 Taiwan national total live births 2018 registered 5 to under 6 months after occu = **2** live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p36 Taiwan national total live births 2018 registered 6 months or more after occurre = **45** live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p37 Taiwan national share of 2018 live births registered within 15 days of occurrenc = **42.3** percent of live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p38 Taiwan national share of 2018 live births registered 15 days to under 1 month af = **28.4** percent of live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p39 Taiwan national share of 2018 live births registered 1 to under 2 months after o = **28.55** percent of live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p40 Taiwan national share of 2018 live births registered 2 to under 3 months after o = **0.7** percent of live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p41 Taiwan national share of 2018 live births registered 6 months or more after occu = **0.02** percent of live births (2018-01-01..2018-12-31) [keep: ] quote: "2 45 100.00 42.30 28.40 28.55 0.70 0.02 0.00 0.00 0.02"
  - p42 Taiwan registered births September 2019 (national total, by registration date) = **14,533** births (2019-09-01..2019-09-30) [keep: ] quote: "總 計 Grand Total 11,704,227 23,593,783 11,889,556 14,533 13,866 667 0.34"
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2023.pdf` -> **snapshot** (snapshot 20251104063418); points raw/verified 15/15
  - p43 Taiwan national registered births, September 2023 (monthly total, by registratio = **10,717** births registered (2023-09-01..2023-09-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p44 Taiwan national registered births, October 2023 (monthly total, by registration  = **13,068** births registered (2023-10-01..2023-10-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p45 Taiwan national registered births, November 2023 (monthly total, by registration = **11,272** births registered (2023-11-01..2023-11-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p46 Taiwan national registered births, December 2023 (monthly total, by registration = **11,579** births registered (2023-12-01..2023-12-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p47 Taiwan national registered births, full year 2023 (annual total, by registration = **135,571** births registered (2023-01-01..2023-12-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p48 Taiwan national registered births, January 2023 (monthly total, by registration  = **10,948** births registered (2023-01-01..2023-01-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p49 Taiwan national registered births, February 2023 (monthly total, by registration = **10,113** births registered (2023-02-01..2023-02-28) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p50 Taiwan national registered births, March 2023 (monthly total, by registration da = **12,506** births registered (2023-03-01..2023-03-31) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p51 Taiwan national registered births, April 2023 (monthly total, by registration da = **9,643** births registered (2023-04-01..2023-04-30) [keep: ] quote: "135,571 10,948 10,113 12,506 9,643"
  - p52 Taiwan national registered births, May 2023 (monthly total, by registration date = **11,809** births registered (2023-05-01..2023-05-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p53 Taiwan national registered births, June 2023 (monthly total, by registration dat = **11,009** births registered (2023-06-01..2023-06-30) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p54 Taiwan national registered births, July 2023 (monthly total, by registration dat = **10,891** births registered (2023-07-01..2023-07-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p55 Taiwan national registered births, August 2023 (monthly total, by registration d = **12,016** births registered (2023-08-01..2023-08-31) [keep: ] quote: "11,809 11,009 10,891 12,016 10,717 13,068 11,272 11,579"
  - p56 Taiwan national registered births, 2022 (annual total, by registration date) = **138,986** births registered (2022-01-01..2022-12-31) [keep: ] quote: "2022 (1) 138,986 207,230 -68,244 5.96 8.89 -2.93"
  - p57 Taiwan national registered births, Q4 2023 (October-December cumulative, by regi = **35,919** births registered (2023-10-01..2023-12-31) [keep: ] quote: "35,919 18,510 17,409 34,502 17,768 16,734 593 311 282 824 431 393"
- `http://midwife.org.tw/upfiles/newsfiles/112%E5%B9%B4%E5%87%BA%E7%94%9F%E9%80%9A%E5%A0%B1%E7%B5%B1%E8%A8%88%E5%B9%B4%E5%A0%B1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2020.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-

### d4 [related_series] health ministry birth-notification system and hospitals

Hypothesis: Births notified by hospitals (出生通報) approximate all live births by occurrence date with near-complete coverage, so the ratio 出生登記/出生通報 is a stable bridge factor; the notification series also gives a faster, higher-frequency read on recent birth levels (through mid-2026) that feeds the September forecast via trend and seasonality.

Queries issued by the searcher: 出生通報 統計 國民健康署 按月; 衛生福利部 出生通報 件數 月 統計; 113年出生通報統計年報 國民健康署 活產 按出生月份分 2024; 內政部 戶口統計 2026年 出生數 月 統計 人口統計資料

- `https://www.mlshb.gov.tw/nc/api/v3/storage/files/a98fa5fbeb25ae5ce476b22251a06ce43d5c43fb297ac5a8caa4e8c9ab04d28b.pdf?displayName=113%E5%B9%B4%E5%87%B` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://midwife.org.tw/upfiles/newsfiles/112%E5%B9%B4%E5%87%BA%E7%94%9F%E9%80%9A%E5%A0%B1%E7%B5%B1%E8%A8%88%E5%B9%B4%E5%A0%B1.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://210.241.78.32/Pages/List.aspx?nodeid=55` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://newdoc.nccu.edu.tw/acadbonus/04/10300039/10300039.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [physical_flow] National Health Insurance prenatal-care system

Hypothesis: Births in month m correspond to first-trimester prenatal visits roughly 7–9 months earlier; NHI-reimbursed prenatal checkup volumes (or first-visit counts) for late 2025 and early 2026 therefore constrain September–October 2026 births. The bridge is a lead-time/coverage factor, assuming prenatal-care uptake and visit schedules stay stable.

Queries issued by the searcher: 產前檢查 申報 件數 每月 健保署 統計; 國民健康署 孕婦產檢 利用率 統計 月別; 健保署 統計 產前檢查 件數 月 113年 114年 預防保健 申報; 內政部 戶政司 出生登記 2025年 每月 統計 人口統計月報

- `https://www.mohw.gov.tw/dl-99969-c1f6ae78-5f82-4c52-bfeb-15581648da80.html` -> **snapshot** (snapshot 20260801141123); points raw/verified 15/8
  - p58 Number of prenatal checkups before the July 2021 increase (prior entitlement) = **10** prenatal checkups per pregnancy (2021-07-01..2021-07-01) [keep: ] quote: "自 110 年 7 月 1 日起將產前檢查次數從 10 次增加至 14 次"
  - p59 Estimated ultrasound utilisation visits, Taiwan, 2025 (estimate) = **295,000** ultrasound visits (人次) (2025-01-01..2025-12-31) [keep: ] quote: "超音波檢查利用人次約 29.5 萬人次"
  - p60 Estimated prenatal health education guidance services, Taiwan, 2025 (estimate) = **175,000** health education guidance visits (人次) (2025-01-01..2025-12-31) [keep: ] quote: "孕婦產前衛教指導約服務 17.5 萬人次"
  - p61 Estimated anaemia testing services, Taiwan, 2025 (estimate) = **99,000** anaemia tests (人次) (2025-01-01..2025-12-31) [keep: ] quote: "貧血檢驗約服務 9.9 萬人次"
  - p62 Pregnant women receiving at least 8 prenatal checkups (孕婦產檢率), Taiwan, 2024 targ = **95** % (2024-01-01..2024-12-31) [keep: ] quote: "孕婦產檢率 111年:94% 112年:95% 113年:95% 114年:95%"
  - p63 Pregnant women receiving at least 8 prenatal checkups (孕婦產檢率), Taiwan, 2023 = **95** % (2023-01-01..2023-12-31) [keep: ] quote: "孕婦產檢率 111年:94% 112年:95% 113年:95% 114年:95%"
  - p64 Pregnant women receiving at least 8 prenatal checkups (孕婦產檢率), Taiwan, 2022 = **95** % (2022-01-01..2022-12-31) [keep: ] quote: "孕婦產檢率 111年:94% 112年:95% 113年:95% 114年:95%"
  - p65 Pregnant women receiving at least 8 prenatal checkups (孕婦產檢率), Taiwan, 2021 = **94** % (2021-01-01..2021-12-31) [keep: ] quote: "孕婦產檢率 111年:94% 112年:95% 113年:95% 114年:95%"
- `https://www.mohw.gov.tw/dl-92627-7da472aa-ed34-432e-ac06-735144701448.html` -> **snapshot** (snapshot 20260801154659); points raw/verified 15/6
  - p66 General ultrasound exams (一般超音波檢查), Taiwan, Jan–Jun 2024, estimated from 2024 NH = **193,000** visits (人次) (2024-01-01..2024-06-30) [keep: ] quote: "一般超音波檢查約為 19.3 萬人次"
  - p67 General ultrasound exams covered per pregnancy, Taiwan, from 2021-07-01 (raised  = **3** ultrasound exams per pregnancy (2021-07-01..2021-07-01) [keep: ] quote: "一般超音波檢查由 1 次增加至 3 次"
  - p68 Prior general ultrasound exams covered per pregnancy, Taiwan, before 2021-07-01 = **1** ultrasound exams per pregnancy (..2021-06-30) [keep: ] quote: "一般超音波檢查由 1 次增加至 3 次"
  - p69 Children under 2 receiving childcare allowance (育兒津貼), Taiwan, cumulative Jan–Au = **302,721** as written "30 萬 2,721", value check pending children (2024-01-01..2024-08-31) [keep: ] quote: "113 年截至 8 月底累計 30 萬 2,721 名未滿 2 歲兒童受惠"
  - p70 Monthly average number of children under 2 benefiting from childcare subsidy, Ta = **55,688** as written "5 萬 5,688", value check pending children per month (2023-01-01..2023-12-31) [keep: ] quote: "112 年補助 57 億 3,789 萬 3,483 元,每月平均 5 萬 5,688 名未滿 2 歲兒童受益"
  - p71 Public childcare slots (公共托育名額), Taiwan, as of end-Aug 2024 = **15,427** as written "1 萬 5,427", value check pending slots (2024-08-31..2024-08-31) [keep: ] quote: "提供 1 萬 5,427 個公共托育名額"
- `https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvMzY3L3JlbGZpbGUvMC84MTQzMC8wZDlkYjA3Yi03MWMxLTQwNDEtODkyZi1kOTQ3YmExNjMxNjMucGRm&n=5bCR5a2Q5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.hsinchu.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMS9yZWxmaWxlLzg3MzUvMjY1NTU0L2M5YmZlNDU0LTNhMjItNDI3MS04NWI3LTBjZTRhZTIzZjhkZS5wZGY%3D&n=5Li` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 16 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 16)

### d6 [related_series] demographers linking marriage and first births

Hypothesis: In Taiwan a large share of births occur within roughly 1–2 years of marriage registration, and monthly marriages lead monthly births by about 10–15 months; marriage registrations in mid-2025 therefore carry information about September 2026 births, and the marriage series helps explain deviations from the pure seasonal extrapolation.

Queries issued by the searcher: 內政部 結婚對數 按月 統計 2025 戶政司; 台灣 婚後第一胎 間隔 研究 結婚 生育 間隔 月; 內政部戶政司 人口統計資料 結婚對數 月別 統計表 下載 xls 114年; "結婚對數" 114年9月 戶口統計 內政部 公布

- `https://ws.moi.gov.tw/001/Upload/OldFile/site_stuff/321/1/month/month.html` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/15
  - p72 Taiwan national total registered marriages (couples), September 2025 = **5,844** couples (2025-09-01..2025-09-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p73 Taiwan national total registered marriages (couples), August 2025 = **5,916** couples (2025-08-01..2025-08-31) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p74 Taiwan national total registered marriages (couples), July 2025 = **7,418** couples (2025-07-01..2025-07-31) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p75 Taiwan national total registered marriages (couples), June 2025 = **7,655** couples (2025-06-01..2025-06-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p76 Taiwan national total registered marriages (couples), May 2025 = **12,791** couples (2025-05-01..2025-05-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p77 Taiwan national total registered marriages (couples), April 2025 = **6,520** couples (2025-04-01..2025-04-30) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p78 Taiwan national total registered marriages (couples), March 2025 = **10,675** couples (2025-03-01..2025-03-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p79 Taiwan national total registered marriages (couples), February 2025 = **8,221** couples (2025-02-01..2025-02-28) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p80 Taiwan national total registered marriages (couples), January 2025 = **9,199** couples (2025-01-01..2025-01-31) [keep: ] quote: "9,199 217 8,221 253 10,675 307 6,520 167 12,791 432"
  - p81 Taiwan national total registered marriages (couples), full year 2025 = **104,376** couples (2025-01-01..2025-12-31) [keep: ] quote: "there were 104,376 marriages registered in 2025, including 3,305 same-sex marriages"
  - p82 Taiwan national total registered marriages (couples), full year 2024 = **123,061** couples (2024-01-01..2024-12-31) [keep: ] quote: "2024(1) 123,061 53,469 5.26 2.28"
  - p83 Taiwan national total registered births (persons), September 2025 = **8,603** persons (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p84 Taiwan national total registered births (persons), full year 2025 = **107,812** persons (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p85 Taiwan national total registered births (persons), full year 2024 = **134,856** persons (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p86 Taiwan national total registered births (persons), October 2025 = **9,458** persons (2025-10-01..2025-10-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
- `https://e-asianwomen.org/xml/04993/04993.pdf` -> **snapshot** (snapshot 20241023013145); points raw/verified 15/11
  - p87 Taiwan birth spacing from marriage to first child, 2010 = **18.82** months (2010-01-01..2010-12-31) [keep: ] quote: "In 2010, Taiwan had the lowest global fertility rate (i.e., 0.97) and the birth spacing between marriage age and the birth of the first child was approximately 18.82 months."
  - p88 Taiwan birth spacing from first to second child, 2010 = **31.96** months (2010-01-01..2010-12-31) [keep: ] quote: "The spacing between the birth of the first and second child was approximately 31.96 months."
  - p89 Taiwan fertility rate, 2010 (lowest globally) = **0.97** births per woman (2010-01-01..2010-12-31) [keep: ] quote: "In 2010, Taiwan had the lowest global fertility rate (i.e., 0.97)"
  - p90 US average age of married woman at first child, 2013 = **27** years (2013-01-01..2013-12-31) [keep: ] quote: "In the United States, in 2013 the average age for a married woman to give birth to her first child was 27 years"
  - p91 US gap in age at first child vs 20 years earlier = **4** years (2013-01-01..2013-12-31) [keep: ] quote: "which is 4 years older than the age of married women who had their first child 20 years earlier."
  - p92 Taiwan marriage-to-first-birth spacing, full sample mean 1983-2010 (Spacing 1, c = **22.35** months (1983-01-01..2010-12-31) [keep: ] quote: "Spacing 1 22.35 25.07 22.87 23.66 22.35 21.73"
  - p93 Taiwan marriage-to-first-birth spacing, full sample mean, 2000s (Spacing 1, chil = **26.65** months (2000-01-01..2009-12-31) [keep: ] quote: "The 2000s =1 Spacing 1 26.65 30.53 26.73 32.72 23.28 25.64"
  - p94 Taiwan marriage-to-first-birth spacing, full sample mean, 1990s (Spacing 1, chil = **23.3** months (1990-01-01..1999-12-31) [keep: ] quote: "The 1990s =1 Spacing 1 23.30 25.06 23.21 24.43 25.11 22.34"
  - p95 Taiwan marriage-to-first-birth spacing, full sample mean, 1980s (Spacing 1, chil = **21.4** months (1980-01-01..1989-12-31) [keep: ] quote: "The 1980s =1 Spacing 1 21.40 23.57 20.30 16.43 21.04 20.30"
  - p96 Taiwan marriage-to-first-birth spacing, full-time employees, 2000s (Spacing 1, c = **30.53** months (2000-01-01..2009-12-31) [keep: ] quote: "The 2000s =1 Spacing 1 26.65 30.53 26.73 32.72 23.28 25.64"
  - p97 Taiwan WMFE married sample total observations = **119,402** observations (1983-01-01..2010-12-31) [keep: ] quote: "The total number of observations recorded was 119,402."
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMzM4Mi9hOGRjNGFmNC00ODI0LTQwMzItODA1NC1jMmM3OWY4OGEwYWYucGRm&n=MTE15bm056ysM` -> **snapshot** (snapshot 20260814040643); points raw/verified 15/11
  - p98 Taiwan total marriage registration pairs (總結婚登記對數), year 2024 (民國113年) = **123,061** marriage pairs (2024-01-01..2024-12-31) [keep: ] quote: "113年 123,061 5.3 21,888 17.8 7,660 6,330 1,330 14,228 10,459 3,769 6,496 15,392 42.2"
  - p99 Taiwan total marriage registration pairs (總結婚登記對數), year 2023 (民國112年) = **125,192** marriage pairs (2023-01-01..2023-12-31) [keep: ] quote: "112年 125,192 5.4 22,469 17.9 9,284 7,530 1,754 13,185 8,797 4,388 7,341 15,128 48.5"
  - p100 Taiwan total marriage registration pairs (總結婚登記對數), year 2022 (民國111年) = **124,997** marriage pairs (2022-01-01..2022-12-31) [keep: ] quote: "111年 124,997 5.4 12,650 10.1 4,070 2,935 1,135 8,580 5,317 3,263 4,754 7,896 60.2"
  - p101 Taiwan total marriage registration pairs (總結婚登記對數), year 2021 (民國110年) = **114,606** marriage pairs (2021-01-01..2021-12-31) [keep: ] quote: "110年 114,606 4.9 8,167 7.1 2,906 2,067 839 5,261 2,703 2,558 3,115 5,052 61.7"
  - p102 Taiwan total marriage registration pairs (總結婚登記對數), year 2020 (民國109年) = **121,702** marriage pairs (2020-01-01..2020-12-31) [keep: ] quote: "109年 121,702 5.2 10,581 8.7 3,203 2,363 840 7,378 4,395 2,983 3,709 6,872 54.0"
  - p103 Taiwan total marriage registration pairs (總結婚登記對數), year 2019 (民國108年) = **134,524** marriage pairs (2019-01-01..2019-12-31) [keep: ] quote: "108年 134,524 5.7 21,216 15.8 8,329 6,698 1,631 12,887 9,007 3,880 5,948 15,268 39.0"
  - p104 Taiwan total marriage registration pairs (總結婚登記對數), year 2018 (民國107年) = **135,403** marriage pairs (2018-01-01..2018-12-31) [keep: ] quote: "107年 135,403 5.7 20,608 15.2 8,216 6,944 1,272 12,392 8,749 3,643 5,385 15,223 35.4"
  - p105 Taiwan total marriage registration pairs (總結婚登記對數), year 2017 (民國106年) = **138,034** marriage pairs (2017-01-01..2017-12-31) [keep: ] quote: "106年 138,034 5.9 21,097 15.3 8,950 7,634 1,316 12,147 8,569 3,578 5,304 15,793 33.6"
  - p106 Taiwan total marriage registration pairs (總結婚登記對數), year 2016 (民國105年), stated a = **147,861** marriage pairs (2016-01-01..2016-12-31) [keep: ] quote: "105年 147,861 6.3 20,359 13.8 9,813 8,673 1,140 10,546 7,111 3,435 4,917 15,442 31.8"
  - p107 Share of 2025 Taiwan marriage pairs where both spouses are Taiwan nationals (num = **81.5** percent (2025-01-01..2025-12-31) [keep: ] quote: "其中雙方均為我國籍者有8萬5,042對,占81.5%,一方為"
  - p108 Same-sex marriage registration pairs in Taiwan, year 2025 (male 1,043 + female 2 = **3,305** marriage pairs (2025-01-01..2025-12-31) [keep: ] quote: "另相同性別結婚登記3,305對中,男性1,043對、女性2,262對,以新"
- dropped by code checks: 8 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3; period_end missing or unparseable: 3; value_as_written not in quote as a whole number: 2)

### d7 [administrative] social insurance and municipal birth-bonus administrators

Hypothesis: Maternity benefit claims (勞保/國保/農保 生育給付) and municipal birth-bonus applications are filed shortly after birth and cover a large, stable share of all births, so their monthly counts act as an early proxy with a short lag and can validate the level implied by registration-based routes.

Queries issued by the searcher: 勞保局 生育給付 件數 統計 月報; 勞動部勞工保險局 統計 勞保生育給付 核付件數 月; 勞動統計月報 勞工保險 生育給付 核付件數 年月別 表; 內政部 戶口統計 出生登記 2026年 月 出生數

- `https://statdb.mol.gov.tw/html/mon/4%E5%85%A8%E6%96%87%E4%B8%8B%E8%BC%89.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://statdb.mol.gov.tw/html/mon/26040.htm` -> **snapshot** (snapshot 20260611065619); points raw/verified 0/0
- `https://www.bli.gov.tw/0109813.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://events.bli.gov.tw/report/reportY.aspx?y=113&f=h10150` -> **snapshot** (snapshot 20251214225419); points raw/verified 0/0

### d8 [shocks] calendar and policy effects analyst

Hypothesis: Zodiac-year effects (2024 dragon peak, 2025 snake trough, 2026 horse year), the timing of Lunar New Year (2026-02-17) shifting conceptions, and any 2025–2026 birth-incentive policy changes can shift the September 2026 level and the year-on-year ratio relative to a naive seasonal extrapolation; quantifying the zodiac and LNY effects from history converts them into an adjustment multiplier.

Queries issued by the searcher: 台灣 生肖 出生數 龍年 蛇年 馬年 比較 統計; 內政部 人口統計月報 出生登記 2026年 月別 出生數; 2025年9月 出生數 內政部 戶口統計 新生兒 月; 2026年 生育補助 加碼 每胎 10萬 行政院 上路 婚育政策

- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p109 Taiwan total population, July 2026 (month-end) = **23,235,002** persons (2026-07-01..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長"
  - p110 Taiwan births registered, July 2026 (single month) = **7,906** births (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p111 Taiwan births registered, May 2026 (single month) = **6,832** births (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p112 Taiwan births registered, June 2026 (single month) = **7,324** births (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p113 Year-on-year change in Taiwan July births, 2026 vs 2025 = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p114 Year-on-year decrease in Taiwan July births, 2026 vs 2025 (persons) = **1,033** births (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p115 Taiwan crude birth rate, July 2026 (annualised) = **4.01** births per 1,000 population (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p116 Taiwan deaths, July 2026 (single month) = **17,119** deaths (2026-07-01..2026-07-31) [keep: ] quote: "至於7月死亡人數則為1萬7119人,平均約每2.6分鐘有一人死亡"
  - p117 Taiwan crude death rate, July 2026 (annualised) = **8.67** deaths per 1,000 population (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%"
  - p118 Year-on-year change in Taiwan July deaths, 2026 vs 2025 = **1.62** % (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%"
  - p119 Month-on-month change in Taiwan July deaths, 2026 vs June 2026 = **4.77** % (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%"
  - p120 Year-on-year change in Taiwan total population, July 2026 vs July 2025 = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p121 Month-on-month change in Taiwan total population, July 2026 vs June 2026 = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p122 Taiwan marriages, July 2026 (couples) = **7,150** couples (2026-07-01..2026-07-31) [keep: ] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%"
  - p123 Taiwan divorces, July 2026 (couples) = **4,450** couples (2026-07-01..2026-07-31) [keep: ] quote: "離婚對數為4450對,同婚占1.7%"
- `https://ocacnews.net/article/410298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ccswf.org.tw/upload/chcf/topic/20210429180708217229.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/388559` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['taiwan births', 'monthly births', 'birth registration']: no matching market created on or before as_of markets=0


## Judge

### round 1

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|

Result: central **n/a** person, 80% interval [n/a, n/a] person, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

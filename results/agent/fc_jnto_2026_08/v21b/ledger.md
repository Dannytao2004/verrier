# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) for the calendar month of August 2026. This is the headline monthly estimate of visitor arrivals, counting foreign nationals entering Japan for tourism, busines | unit visits (arrivals) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [own_history] JNTO monthly estimates provide the target's own history, including seasonal patterns and recent trends. The most recent months before the cutoff (e.g., June 2026, July 2026 if available) and the same 

Hypothesis: August is typically a peak month for foreign visitor arrivals to Japan due to summer holidays. The target value for August 2026 can be estimated by applying the historical August-to-annual ratio or the year-over-year growth rate observed in recent months to the known August 2025 value. If recent monthly growth rates are stable, the August 2026 estimate can be projected from the most recent actual data.

Queries issued by the searcher: JNTO monthly visitor arrivals August 2025 foreign visitors Japan; Japan foreign visitor arrivals 2026 monthly JNTO estimate; JNTO 訪日外客数 2026年6月推計値 3,148,600 発表; JNTO 月別推計値 訪日外客数 2023年8月 2,181,700 2024年8月 2,933,381

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p1 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [keep: ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p2 Year-over-year change in foreign visitor arrivals to Japan, June 2026 vs June 20 = **6.8** % (2026-06-01..2026-06-30) [keep: ] quote: "6月:前年同月比6.8%減の315万人"
  - p3 Cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [keep: ] quote: "また、上半期の累計で21,084,800人となった。"
  - p4 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.scgr.co.jp/report/daily/2026072182279/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-statistics/inbound-travel-statistics/` -> **snapshot** (snapshot 20260731002019); points raw/verified 5/5
  - p5 Foreign visitors to Japan, April 2026 (JNTO estimate) = **3,692,200** visits (arrivals) (2026-04-01..2026-04-30) [keep: ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p6 Year-over-year change in foreign visitors to Japan, April 2026 = **5.5** % (2026-04-01..2026-04-30) [keep: ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p7 Foreign visitors to Japan from South Korea, May 2026 = **951,300** visits (arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p8 Foreign visitors to Japan from Taiwan, May 2026 = **616,800** visits (arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p9 Foreign visitors to Japan from the United States, May 2026 = **333,700** visits (arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
- dropped by code checks: 1 (number: unknown scale word '万人': 1)

### d2 [related_series] Japan's immigration records (e.g., from the Ministry of Justice) or other border control data may provide a broader total of foreign entries that can be adjusted to match JNTO's definition. Alternativ

Hypothesis: The number of foreign visitor arrivals is closely related to the number of foreign nationals entering Japan through major airports and seaports. If total foreign entries are known, subtracting foreign residents re-entering and other non-visitor categories yields the visitor estimate. Air passenger arrivals from international flights, multiplied by the share of foreign visitors, can also approximate the target.

Queries issued by the searcher: Japan international passenger arrivals August 2026 airports statistics; JNTO foreign visitor arrivals monthly 2026 estimate; JNTO 訪日外客数 2026年6月推計値 発表 7月15日; 出入国管理統計 2026年 外国人入国者数 法務省 月別

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.travelvoice.jp/20260805-160287/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p10 JNTO estimated foreign visitor arrivals to Japan, June 2026 (detailed figure) = **3,148,600** people (visits/arrivals) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1 (same JNTO June 2026 estimate).] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p11 Year-on-year change in foreign visitor arrivals to Japan, June 2026 = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 year-on-year change).] quote: "6月:前年同月比6.8%減の315万人"
  - p12 Cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = **21,084,800** people (visits/arrivals) (2026-01-01..2026-06-30) [DISCARD: Redundant duplicate of p3 (same first-half 2026 cumulative).] quote: "また、上半期の累計で21,084,800人となった。"
  - p13 Number of markets recording record-high June foreign visitor arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 (same 15-market record statement).] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.aviationwire.jp/archives/tag/inbound` -> **snapshot** (snapshot 20260719142722); points raw/verified 13/6
  - p14 Year-on-year change in JNTO estimated foreign visitor arrivals to Japan, June 20 = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 year-on-year change).] quote: "2026年6月の訪日客数は前年同月比6.8%減の314万8600人で、3カ月連続で前年同月を下回った。"
  - p15 Year-on-year change in visitor arrivals from China, June 2026 = **57.3** % (2026-06-01..2026-06-30) [keep: ] quote: "6月訪日客、前年割れ続く 中国57.3%減"
  - p16 Year-on-year change in Haneda Airport total passenger count (domestic + internat = **4.5** % (2026-04-01..2026-04-30) [DISCARD: Haneda total passenger count (domestic + international) is a different population from foreign visitor arrivals and cann] quote: "2026年4月の国内線と国際線を合わせた総旅客数は、前年同月比4.5%増の727万4516人だった。"
  - p17 Year-on-year change in Narita International Airport total passenger count, May 2 = **2** % (2026-05-01..2026-05-31) [DISCARD: Narita total passenger count (domestic + international) is a different population from foreign visitor arrivals; no conv] quote: "国際線と国内線を合わせた総旅客数は前年同月比2%増の354万7995人で、10カ月連続で前年同月を上回った。"
  - p18 Year-on-year change in Kansai International Airport total passenger count, May 2 = **12** % (2026-05-01..2026-05-31) [DISCARD: Kansai total passenger count (domestic + international) is a different population from foreign visitor arrivals; no conv] quote: "関空の国際線と国内線を合わせた総旅客数は、前年同月比12%減の254万761人だった。"
  - p19 Year-on-year change in Chubu Centrair International Airport total passenger coun = **1** % (2026-05-01..2026-05-31) [DISCARD: Centrair total passenger count (domestic + international) is a different population from foreign visitor arrivals; no co] quote: "国際線と国内線を合わせた総旅客数は前年同月比1%減の95万1381人で、2カ月連続で前年同月を下回った。"
- dropped by code checks: 8 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 5; period_end 2026-10-23 after as_of: 2)

### d3 [forecasts_markets] Published forecasts from tourism agencies, airlines, or research firms may provide a direct estimate or a growth rate for August 2026 foreign visitor arrivals.

Hypothesis: If a reputable source (e.g., Japan Tourism Agency, JNTO, or a travel research firm) has published a forecast for August 2026 or for full-year 2026, that forecast can be used directly or adjusted for seasonality. Forecasts may incorporate known events (e.g., Expo 2025 aftermath, new routes) that affect arrivals.

Queries issued by the searcher: Japan inbound tourism forecast 2026 foreign visitor arrivals; JNTO 2026 forecast foreign visitors Japan full-year; JNTO 訪日外客数 2026年7月 推計値 3,442,100; 訪日外客数 2025年8月 月別 推計値 JNTO 日本人出国者数; 森トラスト 2026年 訪日外国人 予測 4050万人 4200万人 7月; 訪日外客数 2026年6月 推計値 JNTO 315万人 発表

- `https://www.toutiao.com/article/7664460194746729001/?wid=1786954752411` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dir.co.jp/english/research/report/analysis/20260413_025695.html` -> **snapshot** (snapshot 20260520165358); points raw/verified 0/0
- `https://m.sohu.com/a/1065415167_115479?scm=10008.1475_13-1475_13-11_11.0-0.0-1-0-0-0.0&spm=smwp.content.fd-d.37.1787535187988hSMiDOT&_trans_=000019_wz` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [base_rates] The share of foreign visitor arrivals by month relative to the annual total, and the average year-over-year growth rate, are stable base rates that can be used to project August 2026 from known annual

Hypothesis: Historically, August accounts for approximately 9-10% of annual foreign visitor arrivals to Japan. If a reliable estimate for full-year 2026 is available (e.g., from a forecast), multiplying by the August share yields the target. Alternatively, if the year-to-date total through July 2026 is known, the August value can be estimated using the historical August-to-YTD ratio.

Queries issued by the searcher: JNTO foreign visitor arrivals monthly August share annual total Japan; Japan inbound tourism year-to-date 2026 foreign visitor arrivals JNTO; JNTO 訪日外客数 2026年6月推計値 発表 7月15日 上半年 2108万人; Japan 2026 full year inbound visitor forecast 40 million foreign visitors annual projection

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p20 June 2026 estimated foreign visitor arrivals to Japan (JNTO monthly estimate) = **3,148,600** people (visits/arrivals) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1 (same June 2026 estimate).] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p21 Year-on-year change in June 2026 foreign visitor arrivals to Japan = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 year-on-year change).] quote: "6月:前年同月比6.8%減の315万人"
  - p22 Cumulative first-half 2026 (January-June) foreign visitor arrivals to Japan = **21,084,800** people (visits/arrivals) (2026-01-01..2026-06-30) [DISCARD: Redundant duplicate of p3 (same first-half 2026 cumulative).] quote: "また、上半期の累計で21,084,800人となった。"
  - p23 Number of markets recording their highest-ever June foreign visitor arrivals in  = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 (same 15-market record statement).] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.japantimes.co.jp/news/2026/07/16/japan/society/japan-visitor-number-down/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-database/stats/inbound/` -> **snapshot** (snapshot 20260626140236); points raw/verified 15/15
  - p24 Estimated international traveler arrivals to Japan, April 2026 = **3,692,200** visits (2026-04-01..2026-04-30) [DISCARD: Redundant duplicate of p5 (same April 2026 estimate).] quote: "the estimated number of international travelers to Japan in April 2026 was 3,692,200 (-5.5% compared to 2025)."
  - p25 Year-on-year change in international traveler arrivals to Japan, April 2026 = **-5.5** % (2026-04-01..2026-04-30) [DISCARD: Redundant duplicate of p6 (same April 2026 year-on-year change).] quote: "Overseas Residents' Visits to Japan (Estimated figures) 3,692,200 Visits YOY -5.5%"
  - p26 Cumulative international traveler arrivals to Japan, January to April 2026 YTD = **14,375,829** visits (2026-01-01..2026-04-30) [keep: ] quote: "January to April 14,375,829 Visits"
  - p27 Foreign visitor arrivals to Japan from South Korea, April 2026 = **878,600** visits (2026-04-01..2026-04-30) [keep: ] quote: "South Korea ranked first with 878,600 visitors"
  - p28 Foreign visitor arrivals to Japan from Taiwan, April 2026 = **643,500** visits (2026-04-01..2026-04-30) [keep: ] quote: "followed by Taiwan with 643,500 visitors"
  - p29 Foreign visitor arrivals to Japan from China, April 2026 = **330,700** visits (2026-04-01..2026-04-30) [keep: ] quote: "and China with 330,700 visitors."
  - p30 Foreign visitor arrivals to Japan from Hong Kong, April 2026 = **226,000** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Hong Kong \| \| 226,000 Visits \| \|"
  - p31 Foreign visitor arrivals to Japan from USA, April 2026 = **330,000** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| USA \| \| 330,000 Visits \| \|"
  - p32 Foreign visitor arrivals to Japan from Australia, April 2026 = **102,500** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Australia \| \| 102,500 Visits \| \|"
  - p33 Foreign visitor arrivals to Japan from Thailand, April 2026 = **164,800** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Thailand \| \| 164,800 Visits \| \|"
  - p34 Foreign visitor arrivals to Japan from Philippines, April 2026 = **88,400** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Philippinnes \| \| 88,400 Visits \| \|"
  - p35 Foreign visitor arrivals to Japan from Vietnam, April 2026 = **76,000** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Vietnam \| \| 76,000 Visits \| \|"
  - p36 Foreign visitor arrivals to Japan from Canada, April 2026 = **70,300** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Canada \| \| 70,300 Visits \| \|"
  - p37 Foreign visitor arrivals to Japan from Singapore, April 2026 = **62,900** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Singapore \| \| 62,900 Visits \| \|"
  - p38 Foreign visitor arrivals to Japan from Indonesia, April 2026 = **62,200** visits (2026-04-01..2026-04-30) [keep: ] quote: "\| Indonesia \| \| 62,200 Visits \| \|"
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### d5 [capacity_consumption] International flight seat capacity to Japan and hotel occupancy rates by foreign guests can constrain the maximum possible visitor arrivals and provide a cross-check.

Hypothesis: The number of foreign visitor arrivals is bounded by the available international seat capacity to Japan and the willingness of airlines to fill those seats with foreign visitors. If seat capacity for August 2026 is known (from airline schedules or OAG data), and the historical utilisation rate by foreign visitors is known, the target can be estimated. Similarly, hotel guest nights by foreign visitors can be converted to arrivals using average length of stay.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2025 monthly estimate; Japan international flight seat capacity August 2026 OAG; 訪日外客数 2026年6月 推計値 JNTO; Japan visitor arrivals 2026 record monthly JNTO estimate June 2026

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p39 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** people (visits/arrivals) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1 (same June 2026 estimate).] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p40 Year-on-year change in foreign visitor arrivals to Japan, June 2026 vs June 2025 = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 year-on-year change).] quote: "6月:前年同月比6.8%減の315万人"
  - p41 Cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = **21,084,800** people (visits/arrivals) (2026-01-01..2026-06-30) [DISCARD: Redundant duplicate of p3 (same first-half 2026 cumulative).] quote: "また、上半期の累計で21,084,800人となった。"
  - p42 Number of markets recording record-high June foreign visitor arrivals to Japan,  = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 (same 15-market record statement).] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/8
  - p43 Japan inbound foreign visitor arrivals, June 2026 estimate (JNTO), year-on-year  = **6.8** percent (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 year-on-year change).] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p44 Japan inbound foreign visitor arrivals, cumulative January-June 2026, year-on-ye = **2** percent (2026-01-01..2026-06-30) [DISCARD: Duplicate of the first-half 2026 YoY change already implied by p3 and p2; adds no new information.] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p45 Japan inbound visitor arrivals from South Korea, June 2026, year-on-year change = **7.8** percent (2026-06-01..2026-06-30) [keep: ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p46 Japan inbound visitor arrivals from Taiwan, June 2026, year-on-year change = **14.6** percent (2026-06-01..2026-06-30) [keep: ] quote: "台湾が67万400人(同14.6%増)"
  - p47 Japan inbound visitor arrivals from United States, June 2026, year-on-year chang = **2.7** percent (2026-06-01..2026-06-30) [keep: ] quote: "米国が35万4500人(同2.7%増)"
  - p48 Japan inbound visitor arrivals from China, June 2026, year-on-year change = **57.3** percent (2026-06-01..2026-06-30) [keep: ] quote: "中国が34万700人(同57.3%減)"
  - p49 Japan inbound visitor arrivals from Hong Kong, June 2026, year-on-year change = **28.5** percent (2026-06-01..2026-06-30) [keep: ] quote: "香港が21万4300人(同28.5%増)"
  - p50 Number of markets setting record-high June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 (same 15-market record statement).] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- dropped by code checks: 8 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 7)

### d6 [shocks] Events such as natural disasters, political tensions, pandemics, or major sporting/cultural events can significantly alter visitor flows. The cutoff is 2026-08-16, so any shocks occurring before or du

Hypothesis: If a major shock (e.g., earthquake, typhoon, travel advisory, or geopolitical conflict) occurred in or affected Japan in August 2026, it would likely reduce visitor arrivals relative to the baseline. Conversely, a major event like the Osaka Expo (if ongoing) could boost arrivals. The impact can be estimated by comparing with similar past shocks.

Queries issued by the searcher: JNTO foreign visitor arrivals July 2026; Japan inbound tourism August 2026 visitor arrivals forecast; Osaka Expo 2026 visitor numbers; Japan travel advisory August 2026

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.micetraveladvisor.com/news/article/japan-faces-a-tourism-shock-as-chinese-visitors-fall-while-global-travel-demand-holds-strong/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.explera.jp/blog/2026-09-28-japan-arrivals-august-2026-market-mix/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [administrative] Visa issuance statistics, Advance Passenger Information (API) data, or other administrative records can provide early signals of visitor volumes.

Hypothesis: The number of visas issued to foreign nationals for travel to Japan in the months leading up to August 2026 is correlated with actual arrivals, especially for nationalities requiring visas. If visa issuance data for June-July 2026 is available, it can indicate the trend for August. Similarly, API data collected by airlines might be accessible.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2026; Japan visa issuance statistics 2026 Ministry of Foreign Affairs; 訪日外客数 2026年7月 推計値 JNTO 344万人; 査証（ビザ）発給統計 2026年 外務省 月別

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260916_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-in-august-2026-were-down-9-6-to-3-1-million-despite-record-high-in-14-source-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d8 [attention] Online search interest, social media mentions, and travel booking platform data can serve as leading indicators of tourism demand, though they require a bridge to actual arrivals.

Hypothesis: Google Trends for queries like 'Japan travel' from major source countries, or booking data from platforms like Booking.com or Expedia, can indicate the relative change in travel interest for August 2026 compared to previous periods. If a stable relationship between search interest and arrivals exists, it can be used to adjust a baseline estimate.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan August 2026; Japan National Tourism Organization monthly visitor arrivals 2026; Google Trends "Japan travel" search interest 2026 summer surge; JNTO 訪日外客数 2025年8月 推計値 過去最高

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wimmeramalleenews.com.au/bali-overtakes-japan-in-travel-searches-2026-09-08` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-in-august-2026-were-down-9-6-to-3-1-million-despite-record-high-in-14-source-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] d1

Hypothesis: The August 2025 JNTO monthly estimate is the single most important missing input: it is the base level for any year-over-year projection to August 2026. Without it, the yoy_scaling route cannot be executed and the estimate must rely on weaker seasonal-share or cumulative-ratio routes.

Queries issued by the searcher: JNTO estimated foreign visitor arrivals August 2025; Japan National Tourism Organization August 2025 visitor arrivals estimate monthly

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-reached-3-4-million-in-august-2025-the-first-over-3-million-for-august/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jen-k.jiji.com/jc/eng?g=eco&k=2025091700902` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [own_history] d1

Hypothesis: July 2026 JNTO monthly estimate (published mid-August 2026) would provide the most recent actual level and YoY change, materially reducing uncertainty about the August 2026 trend. It is the last observed month before the target.

Queries issued by the searcher: JNTO July 2026 foreign visitor arrivals estimate; Japan National Tourism Organization 訪日外国人 2026年7月 推計値; JNTO 訪日外客数 2025年8月 推計値 前年同月比; JNTO visitor arrivals statistics monthly estimate Excel 2026

- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/_files/20260819_1615.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-statistics/inbound-travel-statistics/` -> **snapshot** (snapshot 20260731002019); points raw/verified 5/5
  - p51 Foreign visitors to Japan, April 2026 (JNTO estimate) = **3,692,200** visits (2026-04-01..2026-04-30) [DISCARD: Redundant duplicate of p5 (same April 2026 estimate).] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p52 Year-on-year change in foreign visitors to Japan, April 2026 = **5.5** % (2026-04-01..2026-04-30) [DISCARD: Redundant duplicate of p6 (same April 2026 year-on-year change).] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p53 Foreign visitors to Japan from South Korea, May 2026 = **951,300** visits (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p7 (same May 2026 South Korea arrivals).] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p54 Foreign visitors to Japan from Taiwan, May 2026 = **616,800** visits (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p8 (same May 2026 Taiwan arrivals).] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p55 Foreign visitors to Japan from the United States, May 2026 = **333,700** visits (2026-05-01..2026-05-31) [DISCARD: Redundant duplicate of p9 (same May 2026 US arrivals).] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
- `https://yamatogokoro.jp/inbound_data/58034/` -> **snapshot** (snapshot 20260515113739); points raw/verified 15/4
  - p56 Year-on-year change in JNTO estimated foreign visitor arrivals, August 2025 vs A = **16.9** percent (2025-08-01..2025-08-31) [keep: ] quote: "293万3381人を49万人上回り、16.9%増となった"
  - p57 Year-on-year change in JNTO estimated foreign visitor arrivals, July 2025 (menti = **10** percent (2025-07-01..2025-07-31) [keep: ] quote: "7月は前年比約10%減だった韓国も"
  - p58 Year-on-year change in JNTO estimated foreign visitor arrivals from China, Augus = **36.5** percent (2025-08-01..2025-08-31) [keep: ] quote: "中国が最多の101万8600人(前年同月比36.5%増)となり"
  - p59 Year-on-year change in cumulative JNTO estimated foreign visitor arrivals, Janua = **18.2** percent (2025-01-01..2025-08-31) [keep: ] quote: "2025年1月〜8月の累計訪日客数は2838万3600人で、前年同期比18.2%増となった"
- dropped by code checks: 11 (number: more than one number in value_as_written: 11)

### b3 [base_rates] d4

Hypothesis: The historical August share of annual foreign visitor arrivals (or the August-to-first-half ratio) is needed to convert the known first-half 2026 cumulative (p3) into an August 2026 estimate. A stable seasonal ratio would unlock a second independent route.

Queries issued by the searcher: JNTO annual monthly foreign visitor arrivals August 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025; JNTO 訪日外客数 月別 年別 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 8月 年間; Japan inbound visitor arrivals August 2024 JNTO 2,933,000 monthly annual total; JNTO 訪日外客数 2015年 2016年 2017年 2018年 2019年 2020年 2021年 2022年 2023年 2024年 月別 8月 数値; 訪日外客数 2025年8月 JNTO 推計値 年間 2025

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://statistics.jnto.go.jp/en/graph/` -> **snapshot** (snapshot 20260808171734); points raw/verified 0/0
- `https://setouchitourism.or.jp/ja/wp-content/uploads/2025/03/%E8%A6%B3%E5%85%89%E6%8C%87%E6%A8%99R%EF%BC%882024%E5%B9%B4%E6%AC%A1%EF%BC%89%E5%A0%B1%E5%` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.swissinfo.ch/spa/jap%c3%b3n-recibi%c3%b3-cerca-de-3-millones-de-turistas-en-agosto,-otra-cifra-r%c3%a9cord/87570125` -> **snapshot** (snapshot 20260313150639); points raw/verified 15/9
  - p60 Year-on-year growth rate of foreign visitor arrivals to Japan in August 2024 = **36** percent (2024-08-01..2024-08-31) [keep: ] quote: "Japón recibió en agosto 2,93 millones de turistas, lo que supone un incremento interanual del 36 %"
  - p61 Foreign visitor arrivals to Japan from China in August 2024 = **746** visits (tourists) (2024-08-01..2024-08-31) [keep: ] quote: "China aportó en agosto el mayor influjo de turistas a Japón con un total de 745.800"
  - p62 Foreign visitor arrivals to Japan from South Korea in August 2024 = **612** visits (tourists) (2024-08-01..2024-08-31) [keep: ] quote: "seguido de Corea del Sur (612.100)"
  - p63 Foreign visitor arrivals to Japan from Taiwan in August 2024 = **564** visits (tourists) (2024-08-01..2024-08-31) [keep: ] quote: "Taiwán (564.300)"
  - p64 Foreign visitor arrivals to Japan from Hong Kong in August 2024 = **247** visits (tourists) (2024-08-01..2024-08-31) [keep: ] quote: "Hong Kong (246.600)"
  - p65 Foreign visitor arrivals to Japan from the United States in August 2024 = **174** visits (tourists) (2024-08-01..2024-08-31) [keep: ] quote: "Estados Unidos (174.000)"
  - p66 Foreign visitor arrivals to Japan from Italy in August 2024 = **34.7** visits (tourists) (2024-08-01..2024-08-31) [DISCARD: Italy August 2024 arrivals figure is malformed in the source (34.7000) and is not needed for the aggregate estimate.] quote: "Las nacionalidades italiana (34.7000) y española (25.900) lideraron el grupo"
  - p67 Foreign visitor arrivals to Japan from Spain in August 2024 = **25.9** visits (tourists) (2024-08-01..2024-08-31) [DISCARD: Spain August 2024 arrivals figure is malformed in the source (25.900) and is not needed for the aggregate estimate.] quote: "y española (25.900) lideraron el grupo formado por turistas procedentes de Europa"
  - p68 Foreign visitor arrivals to Japan from Middle East region in August 2024 = **11.4** visits (tourists) (2024-08-01..2024-08-31) [DISCARD: Middle East August 2024 arrivals figure is malformed in the source (11.400) and is not needed for the aggregate estimate] quote: "Los visitantes de las regiones de Oriente Medio y los países nórdicos ascendieron a 11.400 y 6.900, respectivamente"
- dropped by code checks: 6 (number: more than one number in value_as_written: 2; number: ambiguous separators: '.' used as a thousands separator: 2; scale word 'million' not supported by quote or table header: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'visitor arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p10', 'p20', 'p39'] All four report the same JNTO June 2026 monthly estimate of 3,148,600 arrivals; they are duplicate copies of one underlying JNTO measurement, not independent confirmations.
- corroborating: ['p2', 'p11', 'p14', 'p21', 'p40', 'p43'] All report the same June 2026 year-on-year change of -6.8%, derived from the same JNTO estimate; duplicate reporting, not independent evidence.
- corroborating: ['p3', 'p12', 'p22', 'p41'] All report the same JNTO first-half 2026 cumulative total of 21,084,800 arrivals; duplicate copies of one JNTO figure.
- corroborating: ['p4', 'p13', 'p23', 'p42', 'p50'] All report 15 markets setting June records; same JNTO release, duplicate copies.
- corroborating: ['p5', 'p24'] Both report the April 2026 JNTO estimate of 3,692,200 arrivals; same underlying JNTO measurement.
- corroborating: ['p6', 'p25'] Both report the April 2026 year-on-year change of -5.5%; same underlying JNTO measurement.
- corroborating: ['p15', 'p48'] Both report the June 2026 China year-on-year change of -57.3%; same JNTO source.
- corroborating: ['p1', 'p5'] June 2026 (-6.8% YoY) and April 2026 (-5.5% YoY) both show a recent negative trend in total arrivals, consistent with a slowdown in 2026.
- corroborating: ['p15', 'p48', 'p45', 'p46', 'p47', 'p49'] June 2026 market-level changes show a sharp China decline (-57.3%) offset by growth from Korea (+7.8%), Taiwan (+14.6%), US (+2.7%), and Hong Kong (+28.5%), explaining the modest overall decline.
- corroborating: ['p16', 'p17', 'p18', 'p19'] Airport passenger trends for April-May 2026 are mixed (Haneda +4.5%, Narita +2%, Kansai -12%, Centrair -1%), broadly consistent with a flat-to-slightly-negative overall arrivals trend.
- corroborating: ['p26', 'p3'] January-April 2026 cumulative 14,375,829 (p26) and January-June 2026 cumulative 21,084,800 (p3) are consistent with each other and with the reported monthly figures.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p10', 'p20', 'p39'] All four are the same JNTO June 2026 monthly estimate (3,148,600) repeated across snapshots; they are one underlying measurement, not independent confirmations.
- corroborating: ['p2', 'p11', 'p14', 'p21', 'p40', 'p43'] All report the same JNTO June 2026 year-on-year change of -6.8%; shared JNTO origin, so they add no independent information.
- corroborating: ['p3', 'p12', 'p22', 'p41'] Same JNTO first-half 2026 cumulative (21,084,800) repeated; one measurement.
- corroborating: ['p4', 'p13', 'p23', 'p42', 'p50'] Same JNTO statement that 15 markets set June records; repeated copies of one fact.
- corroborating: ['p5', 'p24', 'p51'] Same April 2026 JNTO estimate (3,692,200) from tourism.jp; one measurement.
- corroborating: ['p6', 'p25', 'p52'] Same April 2026 year-on-year change (-5.5%); one measurement.
- corroborating: ['p7', 'p53'] Same May 2026 South Korea arrivals (951,300); duplicate.
- corroborating: ['p8', 'p54'] Same May 2026 Taiwan arrivals (616,800); duplicate.
- corroborating: ['p9', 'p55'] Same May 2026 US arrivals (333,700); duplicate.
- corroborating: ['p15', 'p48'] Both report China June 2026 arrivals down 57.3% year on year; same JNTO-derived figure.
- corroborating: ['p44'] First-half 2026 cumulative down 2.0% year on year is consistent with the reported monthly declines and the 21,084,800 level.
- corroborating: ['p56', 'p59'] August 2025 up 16.9% and January-August 2025 cumulative up 18.2% are mutually consistent JNTO figures for the same 2025 period.
- contextual: ['p57'] July 2025 South Korea down about 10% is a market-level detail; it does not conflict with the aggregate August 2025 growth figure.
- contextual: ['p58'] China August 2025 up 36.5% is a market-level detail consistent with strong August 2025 aggregate growth.
- corroborating: ['p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68'] August 2024 aggregate growth of 36% and the market breakdown are from the same JNTO release; the market figures sum consistently with the aggregate.
- contextual: ['p16', 'p17', 'p18', 'p19'] Airport passenger counts for April-May 2026 show mixed trends (Haneda +4.5%, Narita +2%, Kansai -12%, Centrair -1%); they are related but not the same as foreign visitor arrivals and are not directly 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 year-on-year change factor for foreign visitor arrivals to Japan | 0.95 | 0.88..1.02 | 0.8474..1.059 (widened) | ratio | unused | Recent JNTO data show year-on-year declines: April 2026 -5.5% (p6), June 2026 -6.8% (p2), first-half 2026 -2.0% (p44). The decline is driven mainly by China (-57.3% in June, p15/p48), while Korea, Taiwan and the US are still growing. August 2025 was exceptionally strong (+16.9%, p56), making a furth | The recent negative year-on-year trend continues into August 2026 and no major new shock or policy change alters the trajectory. | Evidence that July 2026 arrivals returned to strong year-on-year growth, or that China arrivals rebounded sharply, would push the factor above 1.0. |
| a2 | August share of annual foreign visitor arrivals to Japan | 0.095 | 0.085..0.105 | 0.0668..0.1336 (widened) | share | unused | August is a peak summer month; historically it accounts for roughly 9-10% of annual arrivals. This is a standard seasonal share used to convert a full-year total into an August estimate. | The seasonal pattern of arrivals in 2026 is broadly similar to historical years, with August remaining a peak month. | Evidence that August 2026 is unusually weak or strong relative to the rest of the year, e.g., a major event or shock concentrated in August. |
| a3 | Ratio of August arrivals to January-June cumulative arrivals | 0.42 | 0.38..0.46 | 0.2956..0.5913 (widened) | ratio | m2 (m3) | Historically, August arrivals are roughly 40-45% of the first-half cumulative, reflecting the summer peak. This ratio allows converting the known first-half 2026 cumulative (p3) into an August 2026 estimate. | The seasonal relationship between August and the first half remains stable in 2026. | Evidence that the 2026 seasonal pattern differs materially, e.g., a shift in holiday timing or a major event changing the summer peak. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p1', 'p2'] / ['a1'] | [] |  | 0.00 |  | formula: numeric constant 100 not allowed (only 1 and exponents); make it a named input |
| m2 | formula_mc | 8,770,962 | ['p3'] / ['a3'] | [] |  | 1.00 | equal |  |

Result: central **8,770,962**, 80% interval [5,936,768, 12,958,193], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for foreign visitor arrivals to Japan in August 2026, as first reported by JNTO's monthly estimate, is 8,770,962 visits. This covers the calendar month [n]-[n]-[n] to 2026-[n]-[n] and counts entries of foreign nationals, not unique persons. The supplied interval is 5,936,768 to 12,958,193, at level 80%, basis monte carlo; it is model-based and conditional on the stated assumptions, not a demonstrated accuracy guarantee.

The estimate rests on 1 method(s), with the final weight concentrated on m2 (100%). m2 transfers a historical August-to-first-half ratio, 0.42 (range 0.2956 to 0.5913), to the observed first-half [n] cumulative ([unknown placeholder]). The observed input is the first-half cumulative; the ratio is an analyst assumption, not observed. The main risk is that the [n] seasonal pattern differs from history, so the ratio does not transfer. Better evidence would be actual July 2026 arrivals or an August 2026 booking/forward-looking indicator.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a3 Ratio of August arrivals to January-June cumulative arrivals: 0.42 ratio, range 0.2956 to 0.5913 (range widened by code); used by m2. Overturned by: Evidence that the [n] seasonal pattern differs materially, e.g., a shift in holiday timing or a major event changing the summer peak.

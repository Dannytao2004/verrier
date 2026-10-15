# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) for the calendar month of August 2026. This is the headline monthly estimate of visitor arrivals, counting foreign nationals entering Japan for tourism, busines | unit visits (arrivals) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [related_series] Immigration and border control statistics

Hypothesis: JNTO's estimates are based on immigration records. The number of foreign nationals entering Japan in August 2026 can be approximated by the number of foreign entries recorded by immigration, possibly adjusted for coverage (e.g., excluding crew, diplomats, etc.). This route uses a broader administrative total multiplied by a coverage share to match JNTO's definition.

Queries issued by the searcher: 出入国在留管理庁 外国人入国者数 月別 2025; JNTO 訪日外国人 2025年8月 推計値; 出入国在留管理庁 2025年8月 外国人入国者数 新規入国者 月別 速報; JNTO 訪日外客数 2026年 月別 推計値

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&bunya_l=02&stat_infid=000040362034` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.moj.go.jp/isa/publications/press/13_00056.html` -> **snapshot** (snapshot 20260416063424); points raw/verified 15/3
  - p1 Year-on-year percentage increase in foreign national entries, first half of 2025 = **20** percent (2025-01-01..2025-06-30) [keep: ] quote: "2,137万6,170人で、前年同期に比べ355万5,541人(20.0%)増加"
  - p2 Year-on-year percentage increase in foreign national new entries, first half of  = **20.2** percent (2025-01-01..2025-06-30) [keep: ] quote: "1,972万8,405人で、前年同期に比べ331万4,380人(20.2%)増加しました"
  - p3 Share of 'short-term stay' among new foreign entries, first half of 2025 = **98.1** percent (share of new foreign entries) (2025-01-01..2025-06-30) [keep: ] quote: "「短期滞在」(1,935万8,017人、対前年同期20.3%増)が最も多く、全体の98.1%を占め"
- `https://www.ntv.co.jp/englishnews/articles/20213sqoivhayoczritt.html` -> **snapshot** (snapshot 20260308231405); points raw/verified 9/8
  - p4 Foreign nationals entering Japan in 2025 (Immigration Services Agency total, all = **42,430,000** foreign nationals entering Japan (2025-01-01..2025-12-31) [keep: ] quote: "the number of foreign nationals who entered Japan in 2025 totaled an all-time high of about 42.43 million."
  - p5 Year-on-year increase in foreign nationals entering Japan in 2025 = **5,650,000** foreign nationals entering Japan (increase) (2025-01-01..2025-12-31) [DISCARD: Redundant restatement of the same 2025 annual increase already captured more precisely by p51/p52; adds no independent i] quote: "The figure that includes permanent residents and other long-term stayers increased by about 5.65 million from the year before, surpassing 40 million for the first time."
  - p6 Share of first-time arrivals in Japan in 2025 who were short-term visitors = **98.1** percent (short-term visitors / first-time arrivals) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "Among those arriving in Japan for the first time, 98.1 percent were short-term visitors, indicating an increase in tourists driven by factors such as the weak yen and the rising number of internationa"
  - p7 Foreigners entering Japan with a student visa in 2025 (record high) = **180,000** foreigners entering with a student visa (2025-01-01..2025-12-31) [DISCARD: Student-visa entries are long-term stayers outside JNTO's visitor definition; not usable as a direct input.] quote: "The number of foreigners entering with a student visa totaled about 180,000, also a record high."
  - p8 New entrants from China in 2025 = **7,220,000** new entrants from China (2025-01-01..2025-12-31) [keep: ] quote: "Last year, the number of new entrants from China came to about 7.22 million, up 1.74 million from 2024."
  - p9 Year-on-year increase in new entrants from China in 2025 = **1,740,000** new entrants from China (increase) (2025-01-01..2025-12-31) [DISCARD: Redundant duplicate of p8 (same China 2025 figure and same source); keeping both would double-count one observation.] quote: "Last year, the number of new entrants from China came to about 7.22 million, up 1.74 million from 2024."
  - p10 Monthly arrivals in December 2025 (after Chinese travel advisory) = **280,000** arrivals (2025-12-01..2025-12-31) [keep: ] quote: "ged its citizens to refrain from traveling to Japan following Prime Minister Takaichi Sanae's remarks concerning a potential Taiwan contingency nearly halved from the previous year to roughly 280,000."
  - p11 Foreign workers in Japan as of end of October 2025 (record high) = **2,571,037** foreign workers (2025-10-31..2025-10-31) [DISCARD: Foreign-worker stock is a long-term-stay population measure, not a short-term visitor flow; unusable for the target and ] quote: "the number of foreign workers in Japan as of the end of October 2025 reached a record-high 2,571,037."
- dropped by code checks: 13 (number: more than one number in value_as_written: 12; number: no number in value_as_written: 1)

### d2 [forecasts_markets] Government and industry forecasts

Hypothesis: Official or industry forecasts for inbound tourism in 2026, particularly for the summer months, can provide a direct estimate or a range. The Japan Tourism Agency, JNTO, or private research institutes may publish forecasts. These forecasts often incorporate current trends and policy changes.

Queries issued by the searcher: Japan inbound tourism forecast 2026 visitor arrivals; 訪日外国人 2026年 予測 8月; JNTO 訪日外客数 2026年6月 推計値 前年同月比; 訪日外国人 2026年夏 8月 予測 インバウンド 減少

- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p12 Japan inbound foreign visitor arrivals, June 2026 monthly estimate (JNTO) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p13 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p14 Cumulative Japan inbound foreign visitor arrivals, first half (January-June) 202 = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p15 Number of markets recording record-high June inbound arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.dir.co.jp/english/research/report/analysis/20260413_025695.html` -> **snapshot** (snapshot 20260520165358); points raw/verified 0/0
- `https://www.toutiao.com/article/7664460194746729001/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### d3 [base_rates] Seasonal and trend decomposition

Hypothesis: The ratio of August arrivals to the annual total or to adjacent months is stable. Using a recent year's seasonal pattern and the year-to-date total for 2026, we can estimate August 2026. This route requires the seasonal factor (August share of annual total) and the 2026 YTD total.

Queries issued by the searcher: JNTO monthly foreign visitor arrivals 2025 monthly breakdown August; 訪日外客数 2025年 月別 推計値 JNTO; 訪日外客数 2026年6月 推計値 JNTO 累計; Japan visitor arrivals 2026 first half year-to-date JNTO record

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 4/3
  - p16 June 2026 estimated foreign visitor arrivals to Japan (JNTO monthly estimate) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p17 Year-on-year change in June 2026 foreign visitor arrivals to Japan = **6.8** % (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p18 Cumulative first-half 2026 foreign visitor arrivals to Japan (JNTO estimate) = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
- `https://www.travelvision.jp/news/detail/news-120617?comment_pg=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/8
  - p19 JNTO estimated foreign visitor arrivals to Japan, June 2026 (provisional), year- = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p20 JNTO cumulative foreign visitor arrivals to Japan, January–June 2026, year-on-ye = **2** percent (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p21 Foreign visitor arrivals to Japan from South Korea, June 2026, year-on-year chan = **7.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p22 Foreign visitor arrivals to Japan from Taiwan, June 2026, year-on-year change = **14.6** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾が67万400人(同14.6%増)"
  - p23 Foreign visitor arrivals to Japan from the United States, June 2026, year-on-yea = **2.7** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "米国が35万4500人(同2.7%増)"
  - p24 Foreign visitor arrivals to Japan from China, June 2026, year-on-year change = **57.3** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "中国が34万700人(同57.3%減)"
  - p25 Foreign visitor arrivals to Japan from Hong Kong, June 2026, year-on-year change = **28.5** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "香港が21万4300人(同28.5%増)"
  - p26 Number of markets setting a record high for June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Duplicate of p15/p34 (same 15-market June 2026 record via a secondary outlet); no additional information.] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- dropped by code checks: 8 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 7)

### d4 [physical_flow] Airport and seaport passenger traffic

Hypothesis: Foreign visitor arrivals are a subset of international passenger arrivals at Japanese airports and seaports. Total international arrivals (including Japanese nationals) multiplied by the foreign share gives an estimate. The foreign share can be derived from historical data or from immigration statistics. This route uses physical throughput data from airports and ports.

Queries issued by the searcher: JNTO 訪日外国人客数 2026年8月 推計; Narita airport international passenger arrivals August 2025 monthly statistics; 出入国管理統計月報 2025年8月 外国人入国者数 日本人帰国者数 総数; 関西国際空港 2025年8月 国際線旅客数 外国人

- `https://www.narita-airport.jp/files/b2e22b1f56ede88eda96151d616c3d8893efaeaa57658001834df6fb32d70835` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.moj.go.jp/isa/content/001459115.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d5 [capacity_consumption] Airlines and travel agencies

Hypothesis: Available seat capacity on international flights to Japan multiplied by expected load factor and the share of foreign visitors yields an estimate. This route uses airline schedules and booking data. It is forward-looking and can incorporate announced capacity changes for August 2026.

Queries issued by the searcher: Japan international flight seat capacity August 2026 OAG; JNTO 訪日外国人 2026年8月 推計; OAG 国際線 座席数 日本 2026年夏ダイヤ 増便; 訪日外客数 2026年6月 推計値 JNTO

- `https://press.jal.co.jp/en/items/uploads/JAL%20Traffic%20Data%20AUG%202026.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-in-august-2026-were-down-9-6-to-3-1-million-despite-record-high-in-14-source-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ttnmedia.com/?p=142962` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [related_series] Source market trends

Hypothesis: Arrivals from major source countries (e.g., South Korea, China, Taiwan, USA) can be summed to approximate the total. Trends in these markets, such as recovery rates compared to 2019, can be used to project August 2026. This route uses country-level data and assumes stable shares.

Queries issued by the searcher: JNTO 訪日外客数 国別 2026年6月; JNTO foreign visitor arrivals by country August 2025; JNTO 2025年8月 国別 訪日外客数 推計値 pdf 20250917; 訪日外客数 2026年7月 推計値 JNTO

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260715_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://wwwtb.mlit.go.jp/kyushu/content/000378221.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/8
  - p27 Year-on-year change in total foreign visitor arrivals to Japan, June 2026 vs Jun = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p28 Year-on-year change in cumulative foreign visitor arrivals to Japan, January–Jun = **2** percent (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p29 Year-on-year change in foreign visitor arrivals to Japan from South Korea, June  = **7.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p30 Year-on-year change in foreign visitor arrivals to Japan from Taiwan, June 2026  = **14.6** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾が67万400人(同14.6%増)"
  - p31 Year-on-year change in foreign visitor arrivals to Japan from the United States, = **2.7** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "米国が35万4500人(同2.7%増)"
  - p32 Year-on-year change in foreign visitor arrivals to Japan from China, June 2026 v = **57.3** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "中国が34万700人(同57.3%減)"
  - p33 Year-on-year change in foreign visitor arrivals to Japan from Hong Kong, June 20 = **28.5** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "香港が21万4300人(同28.5%増)"
  - p34 Number of markets setting record-high June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Duplicate of p15/p26 (same 15-market June 2026 record); redundant copy.] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- dropped by code checks: 7 (number: more than one number in value_as_written: 7)

### d7 [shocks] Event and policy calendar

Hypothesis: Major events, policy changes (e.g., visa liberalization, travel advisories), or disruptions (e.g., natural disasters, pandemics, geopolitical tensions) in August 2026 could significantly affect arrivals. Identifying such shocks and their expected impact helps adjust the baseline estimate.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan monthly 2026; Japan major events August 2026 Expo inbound tourism; 訪日外客数 2025年8月 推計値 342万人 JNTO; Japan visa policy change 2026 visa-free travel advisory China

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://micetimes.jp/2026-8-picks/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-were-down-5-5-to-3-7-million-in-april-2026/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [base_rates] JNTO monthly seasonality

Hypothesis: A stable August share of annual JNTO foreign visitor arrivals would unlock a seasonal-share route (d3) using a 2026 year-to-date total or a 2025 annual total. Without this share, the August level cannot be anchored to the annual scale.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2024 monthly estimate annual total; JNTO 訪日外客数 2024年 年間 推計値 月別 8月; JNTO 訪日外客数 2026年6月 推計値 発表; JNTO 2025年 年間訪日外客数 42,687,000 確定値

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvision.jp/news/detail/news-114693` -> **snapshot** (snapshot 20250810214908); points raw/verified 14/13
  - p35 JNTO foreign visitor arrivals to Japan, August 2019 = **2,520,134** visits (arrivals) (2019-08-01..2019-08-31) [EXCLUDED (ablation): ] quote: "\| 8月 \| 2,520,134 \| 2,933,381 \| 116.4% \| 2,109,568 \| 1,437,126 \| 68.1% \|"
  - p36 JNTO foreign visitor arrivals to Japan, August 2024 = **2,933,381** visits (arrivals) (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "\| 8月 \| 2,520,134 \| 2,933,381 \| 116.4% \| 2,109,568 \| 1,437,126 \| 68.1% \|"
  - p37 JNTO foreign visitor arrivals to Japan, annual total 2019 = **31,882,049** visits (arrivals) (2019-01-01..2019-12-31) [EXCLUDED (ablation): ] quote: "\| 1~12月 \| 31,882,049 \| 36,869,900 \| 115.6% \| 20,080,669 \| 13,007,300 \| 64.8% \|"
  - p38 JNTO foreign visitor arrivals to Japan, annual total 2024 = **36,869,900** visits (arrivals) (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "\| 1~12月 \| 31,882,049 \| 36,869,900 \| 115.6% \| 20,080,669 \| 13,007,300 \| 64.8% \|"
  - p39 JNTO foreign visitor arrivals to Japan, January 2024 = **2,688,478** visits (arrivals) (2024-01-01..2024-01-31) [EXCLUDED (ablation): ] quote: "\| 1月 \| 2,689,339 \| 2,688,478 \| 100.0% \| 1,452,157 \| 838,581 \| 57.7% \|"
  - p40 JNTO foreign visitor arrivals to Japan, February 2024 = **2,788,224** visits (arrivals) (2024-02-01..2024-02-29) [EXCLUDED (ablation): ] quote: "\| 2月 \| 2,604,322 \| 2,788,224 \| 107.1% \| 1,534,792 \| 978,884 \| 63.8% \|"
  - p41 JNTO foreign visitor arrivals to Japan, March 2024 = **3,081,781** visits (arrivals) (2024-03-01..2024-03-31) [EXCLUDED (ablation): ] quote: "\| 3月 \| 2,760,136 \| 3,081,781 \| 111.7% \| 1,929,915 \| 1,219,789 \| 63.2% \|"
  - p42 JNTO foreign visitor arrivals to Japan, April 2024 = **3,043,003** visits (arrivals) (2024-04-01..2024-04-30) [EXCLUDED (ablation): ] quote: "\| 4月 \| 2,926,685 \| 3,043,003 \| 104.0% \| 1,666,546 \| 888,767 \| 53.3% \|"
  - p43 JNTO foreign visitor arrivals to Japan, May 2024 = **3,040,294** visits (arrivals) (2024-05-01..2024-05-31) [EXCLUDED (ablation): ] quote: "\| 5月 \| 2,773,091 \| 3,040,294 \| 109.6% \| 1,437,929 \| 941,709 \| 65.5% \|"
  - p44 JNTO foreign visitor arrivals to Japan, June 2024 = **3,140,642** visits (arrivals) (2024-06-01..2024-06-30) [EXCLUDED (ablation): ] quote: "\| 6月 \| 2,880,041 \| 3,140,642 \| 109.0% \| 1,520,993 \| 930,229 \| 61.2% \|"
  - p45 JNTO foreign visitor arrivals to Japan, July 2024 = **3,292,602** visits (arrivals) (2024-07-01..2024-07-31) [EXCLUDED (ablation): ] quote: "\| 7月 \| 2,991,189 \| 3,292,602 \| 110.1% \| 1,659,166 \| 1,048,823 \| 63.2% \|"
  - p46 JNTO foreign visitor arrivals to Japan, September 2024 = **2,872,487** visits (arrivals) (2024-09-01..2024-09-30) [EXCLUDED (ablation): ] quote: "\| 9月 \| 2,272,883 \| 2,872,487 \| 126.4% \| 1,751,477 \| 1,212,545 \| 69.2% \|"
  - p47 JNTO foreign visitor arrivals to Japan, October 2024 = **3,312,193** visits (arrivals) (2024-10-01..2024-10-31) [EXCLUDED (ablation): ] quote: "\| 10月 \| 2,496,568 \| 3,312,193 \| 132.7% \| 1,663,474 \| 1,148,502 \| 69.0% \|"
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 4/3
  - p48 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p49 JNTO estimated foreign visitor arrivals to Japan, June 2026, year-on-year change = **6.8** % (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p50 JNTO cumulative foreign visitor arrivals to Japan, first half (January-June) 202 = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 1; number: unknown scale word '万人': 1)

### b2 [related_series] Immigration coverage bridge

Hypothesis: A conversion factor from total foreign national entries (Immigration Services Agency) to JNTO visitor arrivals would let the 2025 immigration total (p4) and short-term share (p3) be used to scale a 2026 August estimate. This is the key missing bridge for d1.

Queries issued by the searcher: JNTO foreign visitor arrivals vs Immigration Services Agency foreign entries total comparison; 出入国在留管理庁 外国人入国者数 統計 2025年 JNTO 訪日外客数 比較; 出入国在留管理庁 出入国管理統計 月別 2025年8月 外国人入国者数 速報; JNTO 訪日外客数 2025年8月 推計値 342万人 過去最高

- `https://www.jef.or.jp/journal/pdf/250th_Economic_Indicators.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.moj.go.jp/isa/publications/press/13_00063.html` -> **snapshot** (snapshot 20260418165023); points raw/verified 15/3
  - p51 Year-on-year percentage increase in total foreign national entries, calendar yea = **15.4** percent (year-on-year change in foreign national entries) (2025-01-01..2025-12-31) [keep: ] quote: "4,243万930人で、前年に比べ565万966人(15.4%)増加、新規入国者数は、3,918万4,525人で、前年に比べ516万8,759人(15.2%)増加"
  - p52 Year-on-year percentage increase in new foreign national entries, calendar year  = **15.2** percent (year-on-year change in new foreign national entries (2025-01-01..2025-12-31) [keep: ] quote: "新規入国者数は、3,918万4,525人で、前年に比べ516万8,759人(15.2%)増加し、いずれも過去最高となりました"
  - p53 Share of 'short-term stay' among new foreign national entries, calendar year 202 = **98.1** percent (short-term stay new entries / total new foreign nat (2025-01-01..2025-12-31) [keep: ] quote: "「短期滞在」(3,845万8,105人、対前年15.3%増)が最も多く、全体の98.1%を占め"
- `https://www.mlit.go.jp/pri/houkoku/gaiyou/pdf/kkk38.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 12 (number: more than one number in value_as_written: 12)

### b3 [forecasts_markets] Summer 2026 capacity and demand

Hypothesis: Announced international seat capacity to Japan for August 2026 and any airline/industry summer outlook would provide a forward-looking anchor for d5 and help bound the August 2026 level, especially given the post-2025 Chinese advisory shock.

Queries issued by the searcher: OAG international seat capacity Japan August 2026; JNTO foreign visitor arrivals August 2026 forecast; South China Morning Post OAG China-Japan flights August 2026 down 57% capacity; international seat capacity Japan summer 2026 airline schedule OAG seats million

- `https://www.scmp.com/economy/global-economy/article/3358296/china-japan-flights-drop-57-summer-travel-peak-amid-geopolitical-tensions?module=inline&pg` -> **snapshot** (snapshot 20260719234847); points raw/verified 12/4
  - p54 China-Japan round-trip flights scheduled for July 2026 (summer travel period) = **2,629** round-trip flights (2026-07-01..2026-07-31) [keep: ] quote: "A total of 2,629 round-trip flights were expected next month between the two Asian countries, down from 6,317 in July last year."
  - p55 China-Japan round-trip flights flown in July 2025 = **6,317** round-trip flights (2025-07-01..2025-07-31) [keep: ] quote: "A total of 2,629 round-trip flights were expected next month between the two Asian countries, down from 6,317 in July last year."
  - p56 China-Japan round-trip flights flown in August 2025 = **6,127** round-trip flights (2025-08-01..2025-08-31) [keep: ] quote: "In August, 2,641 were scheduled, a drop from the 6,127 flown in August 2025, data compiled by British aviation intelligence firm OAG showed."
  - p57 China-Japan flights scrapped by China as of June 23 (current year) = **9,000** flights (..2026-06-23) [keep: ] quote: "As of June 23, China had scrapped nearly 9,000 flights to Japan this year."
- `https://www.travelandtourworld.com/news/article/0czr1h4z6n4n/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/en/news/result/?page=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (period_end 2026-08-31 after as_of: 2; period_end missing or unparseable: 6)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'visitor arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Both are first-half 2025 year-on-year growth rates for foreign entries from the same Immigration Services Agency release; p1 covers all foreign entries while p2 covers new entries, so they are closely
- contextual: ['p3'] Short-term stay share of new foreign entries in H1 2025 is a definitional/coverage factor, not a level estimate; it helps bridge broader immigration totals to JNTO's visitor definition.
- corroborating: ['p4', 'p5'] Both come from the same 2025 immigration total report; p5 is the year-on-year increment consistent with p4, so they are not independent.
- corroborating: ['p8', 'p9'] Both describe 2025 new entrants from China and its increase from 2024; same underlying source and same measurement.
- corroborating: ['p15', 'p26', 'p34'] All three report the same June 2026 JNTO-related fact that 15 markets set June records; they are redundant copies of the same underlying statistic.
- contextual: ['p10'] December 2025 arrivals after a Chinese travel advisory is a shock-related observation; it is useful for scenario adjustment but not a direct August 2026 level.
- contextual: ['p7', 'p11'] Student visa entries and foreign workers are different populations from short-term visitors; they help characterize total foreign entries but are not direct JNTO visitor arrivals.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] Both from the same Immigration Services Agency release (MOJ), measuring the same first-half 2025 foreign-entry surge: total foreign national entries +20.0% and new entries +20.2%. They are not indepen
- corroborating: ['p4', 'p5', 'p51', 'p52'] All describe the same 2025 Immigration Services Agency annual total: p4 gives ~42.43m foreign nationals entering, p5 the +5.65m increase, p51 the precise 42,430,930 (+15.4%), p52 new entries 39,184,52
- corroborating: ['p3', 'p53'] Both report the 'short-term stay' share of new foreign entries at 98.1%, one for H1-2025 and one for CY2025. Same source and definition; the stability across periods supports using ~98% as the short-t
- corroborating: ['p8', 'p9'] Same NTV report: China new entrants ~7.22m in 2025, up 1.74m from 2024. Identical underlying figure, so they are one observation, not two.
- corroborating: ['p15', 'p26', 'p34'] All three report the same JNTO June 2026 result: 15 markets set June record highs. p15 is the JNTO primary source; p26/p34 are the same figure via TravelVoice. One underlying measurement, useful as a 
- corroborating: ['p54', 'p55', 'p56', 'p57'] All from the same SCMP/OAG aviation dataset on the China-Japan flight collapse: July 2026 scheduled 2,629 vs 6,317 flown July 2025; August 2026 scheduled 2,641 vs 6,127 flown August 2025; ~9,000 fligh
- corroborating: ['p10', 'p54', 'p56'] p10 (December 2025 arrivals ~280,000 after the Chinese travel advisory) and the OAG flight cuts (p54/p56) are consistent evidence of a China-driven demand shock persisting into 2026; they describe dif
- contextual: ['p7', 'p11'] Student-visa entries (p7) and foreign workers (p11) are stock/flow measures of long-term stayers, not short-term visitors. They are consistent with a large foreign-entry total but are not direct input

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 foreign visitor arrivals as a multiple of August 2025 JNTO arrivals | 0.95 | 0.8..1.15 | 0.6782..1.356 (widened) | ratio (dimensionless) | m1 (m1) | No kept point gives the August 2026 level directly. June 2026 set records in 15 markets (p15), indicating broad-based strength, but the China-Japan flight collapse (p54/p56: August 2026 scheduled 2,641 vs 6,127 flown August 2025) removes a large share of Chinese arrivals, and the December 2025 advis | Used to scale a known August 2025 JNTO arrival level to August 2026; valid only if the China shock is not fully offset by growth in Korea, Taiwan, US and other markets. | Evidence that China-Japan capacity has been restored toward 2025 levels, or that total 2026 summer arrivals are running clearly above 2025. |
| a2 | August share of annual JNTO foreign visitor arrivals | 0.095 | 0.085..0.105 | 0.0668..0.1336 (widened) | share (dimensionless) | unused | August is a peak summer month; historically it accounts for roughly 9-10% of annual JNTO arrivals. No kept point supplies this share, so it is assumed with a wide range to allow the seasonal-share route. | Used with a 2026 annual arrivals total to derive the August 2026 level; valid if 2026 seasonality resembles recent years. | A published 2026 monthly distribution showing August materially outside 8.5-10.5% of the annual total. |

Rejected by code:

- a3 2026 full-year JNTO foreign visitor arrivals: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['japan']; quantity stems: ['arriv', 'visit']
- points excluded before the judge: 37 of 57
- methods allowed: ['formula_mc']

  - p6 Share of first-time arrivals in Japan in 2025 who were short-term visitors = 98.1 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p12 Japan inbound foreign visitor arrivals, June 2026 monthly estimate (JNTO) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p13 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p14 Cumulative Japan inbound foreign visitor arrivals, first half (January-June) 2026 = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p16 June 2026 estimated foreign visitor arrivals to Japan (JNTO monthly estimate) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p17 Year-on-year change in June 2026 foreign visitor arrivals to Japan = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p18 Cumulative first-half 2026 foreign visitor arrivals to Japan (JNTO estimate) = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p19 JNTO estimated foreign visitor arrivals to Japan, June 2026 (provisional), year-on-year ch = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p20 JNTO cumulative foreign visitor arrivals to Japan, January–June 2026, year-on-year change = 2 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p21 Foreign visitor arrivals to Japan from South Korea, June 2026, year-on-year change = 7.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p22 Foreign visitor arrivals to Japan from Taiwan, June 2026, year-on-year change = 14.6 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p23 Foreign visitor arrivals to Japan from the United States, June 2026, year-on-year change = 2.7 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p24 Foreign visitor arrivals to Japan from China, June 2026, year-on-year change = 57.3 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p25 Foreign visitor arrivals to Japan from Hong Kong, June 2026, year-on-year change = 28.5 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p27 Year-on-year change in total foreign visitor arrivals to Japan, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p28 Year-on-year change in cumulative foreign visitor arrivals to Japan, January–June 2026 vs  = 2 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p29 Year-on-year change in foreign visitor arrivals to Japan from South Korea, June 2026 vs 20 = 7.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p30 Year-on-year change in foreign visitor arrivals to Japan from Taiwan, June 2026 vs 2025 = 14.6 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p31 Year-on-year change in foreign visitor arrivals to Japan from the United States, June 2026 = 2.7 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p32 Year-on-year change in foreign visitor arrivals to Japan from China, June 2026 vs 2025 = 57.3 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p33 Year-on-year change in foreign visitor arrivals to Japan from Hong Kong, June 2026 vs 2025 = 28.5 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p35 JNTO foreign visitor arrivals to Japan, August 2019 = 2,520,134 (2019-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p36 JNTO foreign visitor arrivals to Japan, August 2024 = 2,933,381 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p37 JNTO foreign visitor arrivals to Japan, annual total 2019 = 31,882,049 (2019-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p38 JNTO foreign visitor arrivals to Japan, annual total 2024 = 36,869,900 (2024-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p39 JNTO foreign visitor arrivals to Japan, January 2024 = 2,688,478 (2024-01-31): ablation: name refers to the target entity ['japan'] and quantity
  - p40 JNTO foreign visitor arrivals to Japan, February 2024 = 2,788,224 (2024-02-29): ablation: name refers to the target entity ['japan'] and quantity
  - p41 JNTO foreign visitor arrivals to Japan, March 2024 = 3,081,781 (2024-03-31): ablation: name refers to the target entity ['japan'] and quantity
  - p42 JNTO foreign visitor arrivals to Japan, April 2024 = 3,043,003 (2024-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p43 JNTO foreign visitor arrivals to Japan, May 2024 = 3,040,294 (2024-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p44 JNTO foreign visitor arrivals to Japan, June 2024 = 3,140,642 (2024-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p45 JNTO foreign visitor arrivals to Japan, July 2024 = 3,292,602 (2024-07-31): ablation: name refers to the target entity ['japan'] and quantity
  - p46 JNTO foreign visitor arrivals to Japan, September 2024 = 2,872,487 (2024-09-30): ablation: name refers to the target entity ['japan'] and quantity
  - p47 JNTO foreign visitor arrivals to Japan, October 2024 = 3,312,193 (2024-10-31): ablation: name refers to the target entity ['japan'] and quantity
  - p48 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p49 JNTO estimated foreign visitor arrivals to Japan, June 2026, year-on-year change = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p50 JNTO cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 5,880 | ['p56'] / ['a1'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **5,880**, 80% interval [3,977, 8,696], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for foreign visitor arrivals to Japan in August 2026, as JNTO would first report it, is 5,880 visits. The code supplies a model-based interval of 3,977 to 8,696 at the 80% level, conditional on the assumptions rather than a demonstrated accuracy guarantee.

The estimate rests mainly on one route: scaling August 2025 China-Japan flight volume into a change factor for arrivals, using observed point 3,977 and assumption 0.95 (range 0.6782 to 1.356). A second seasonal-share route was rejected because its input was target-like, so it received weight 0%. The combination therefore reflects the single retained method, not independent confirmation.

The key risk is that the flight-shock transfer may misstate how Chinese demand and other markets offset each other. Better evidence would be actual August 2026 immigration or arrival counts.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 foreign visitor arrivals as a multiple of August 2025 JNTO arrivals: 0.95 ratio (dimensionless), range 0.6782 to 1.356 (range widened by code); used by m1. Overturned by: Evidence that China-Japan capacity has been restored toward [n] levels, or that total [n] summer arrivals are running clearly above [n].

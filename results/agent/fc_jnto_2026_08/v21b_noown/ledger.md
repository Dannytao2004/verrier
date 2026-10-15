# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) for the calendar month of August 2026. This is a count of visits (arrivals), not unique individuals, based on immigration records and JNTO's estimation methodol | unit arrivals (visits) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [physical_flow] Immigration and border control

Hypothesis: Immigration entry records for August 2026 (if available in real-time or preliminary) can directly provide the count. Even partial data for early August can be extrapolated.

Queries issued by the searcher: Japan immigration foreign arrivals August 2026; JNTO inbound visitors July 2026 statistics; 訪日外客数 2026年6月 推計値 JNTO プレスリリース; e-Stat 出入国管理統計 速報値 2026年7月 外国人入国者数

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p1 June 2026 foreign visitor arrivals to Japan, detailed count = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p2 June 2026 foreign visitor arrivals year-on-year change = **6.8** % (year-on-year change) (2026-06-01..2026-06-30) [keep: ] quote: "6月:前年同月比6.8%減の315万人"
  - p3 Cumulative first-half 2026 foreign visitor arrivals to Japan = **21,084,800** arrivals (visits) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p4 Number of markets recording record-high June foreign visitor arrivals = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p13/p27/p52; same JNTO June 2026 release and same 15-market record count, adds no independent inf] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040502458&iroha=19` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-statistics/inbound-travel-statistics/` -> **snapshot** (snapshot 20260731002019); points raw/verified 5/5
  - p5 Foreign visitors to Japan, April 2026 (JNTO estimate) = **3,692,200** visitors (2026-04-01..2026-04-30) [EXCLUDED (ablation): ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p6 Year-on-year change in foreign visitors to Japan, April 2026 = **5.5** % (2026-04-01..2026-04-30) [EXCLUDED (ablation): ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p7 Foreign visitors to Japan from South Korea, May 2026 = **951,300** visitors (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p8 Foreign visitors to Japan from Taiwan, May 2026 = **616,800** visitors (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p9 Foreign visitors to Japan from the United States, May 2026 = **333,700** visitors (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### d2 [related_series] Air travel and aviation statistics

Hypothesis: Foreign visitor arrivals are strongly correlated with international passenger arrivals at Japanese airports. If international passenger arrival data for August 2026 (or partial data) is available, it can be used to estimate the share of foreign visitors among all international arrivals, then scaled to the full month.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan August 2026; Japan international passenger arrivals July 2026 airport statistics; 訪日外客数 2026年6月推計値 JNTO 発表 7月; 成田空港 2026年6月 空港運用状況 国際線外国人旅客数

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sky-budget.com/2026/08/27/narita-airport-news-aug2026-3/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p10 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p11 Year-on-year change in foreign visitor arrivals to Japan, June 2026 vs June 2025 = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p12 Cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = **21,084,800** arrivals (visits) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p13 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4; same JNTO June 2026 record-market statement, adds no new information.] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### d3 [forecasts_markets] Government and industry forecasts

Hypothesis: Official forecasts or targets for Japan's inbound tourism in 2026, such as from the Japan Tourism Agency or JNTO, can provide a baseline. If a full-year target exists, monthly seasonality can allocate it to August.

Queries issued by the searcher: Japan inbound tourism forecast 2026 JNTO visitor target; Japan Tourism Agency 2026 inbound visitor forecast forecast; JNTO foreign visitor arrivals August 2025 record; Japan 2026 tourism target 40 million visitors forecast

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://tradingeconomics.com/japan/tourist-arrivals` -> **snapshot** (snapshot 20260816071036); points raw/verified 14/10
  - p14 Japan tourist arrivals, actual, June 2026 = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "Tourist Arrivals in Japan decreased to 3148600 in June from 3559900 in May of 2026."
  - p15 Japan tourist arrivals, previous month, May 2026 = **3,559,900** arrivals (visits) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "Tourist Arrivals in Japan decreased to 3148600 in June from 3559900 in May of 2026."
  - p16 Japan tourist arrivals, long-run average, 1991 to 2026 = **971,885** arrivals (visits) (1991-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "Tourist Arrivals in Japan averaged 971884.88 from 1991 until 2026, reaching an all time high of 3908900.00 in April of 2025 and a record low of 1700.00 in May of 2020."
  - p17 Japan tourist arrivals, all-time high, April 2025 = **3,908,900** arrivals (visits) (2025-04-01..2025-04-30) [EXCLUDED (ablation): ] quote: "reaching an all time high of 3908900.00 in April of 2025 and a record low of 1700.00 in May of 2020."
  - p18 Japan tourist arrivals, record low, May 2020 = **1,700** arrivals (visits) (2020-05-01..2020-05-31) [EXCLUDED (ablation): ] quote: "reaching an all time high of 3908900.00 in April of 2025 and a record low of 1700.00 in May of 2020."
  - p19 Japan tourist arrivals, forecast for end of current quarter (Q2 2026), Trading E = **3,150,000** arrivals (visits) (2026-04-01..2026-06-30) [EXCLUDED (ablation): ] quote: "Tourist Arrivals in Japan is expected to be 3150000.00 by the end of this quarter, according to Trading Economics global macro models and analysts expectations."
  - p20 Japan tourist arrivals, actual, June 2026 (related table row) = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "\| Tourist Arrivals \| 3148600.00 \| 3559900.00 \| \| Jun 2026 \|"
  - p21 Japan tourist arrivals, previous month, May 2026 (related table row) = **3,559,900** arrivals (visits) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "\| Tourist Arrivals \| 3148600.00 \| 3559900.00 \| \| Jun 2026 \|"
  - p22 Japan tourist arrivals, highest value, 1991-2026 series = **3,908,900** arrivals (visits) (1991-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "\| \| 3148600.00 \| 3559900.00 \| 3908900.00 \| 1700.00 \| 1991 - 2026 \| \| Monthly \| \|"
  - p23 Japan tourist arrivals, lowest value, 1991-2026 series = **1,700** arrivals (visits) (1991-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "\| \| 3148600.00 \| 3559900.00 \| 3908900.00 \| 1700.00 \| 1991 - 2026 \| \| Monthly \| \|"
- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.japantimes.co.jp/news/2026/07/16/japan/society/japan-visitor-number-down/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (period_end 2027-12-31 after as_of: 1; period_end 2028-12-31 after as_of: 1; scale word 'thousand' not supported by quote or table header: 2)

### d4 [base_rates] Seasonality and source markets

Hypothesis: August is typically a peak month for Japanese outbound and inbound tourism due to summer holidays. The share of August arrivals in the annual total can be used with a full-year estimate. Also, major source markets (e.g., South Korea, China, Taiwan, USA) have distinct patterns that can be summed.

Queries issued by the searcher: JNTO inbound visitor arrivals August 2025 monthly statistics; Japan inbound tourism seasonality August share of annual arrivals monthly distribution; 訪日外客数 2026年6月 推計値 JNTO; JNTO 2025年 年間 訪日外客数 月別 8月 構成比

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p24 Japan inbound foreign visitor arrivals, June 2026 (JNTO estimate, detailed) = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p25 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 = **6.8** % (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p26 Cumulative Japan inbound foreign visitor arrivals, first half of 2026 = **21,084,800** arrivals (visits) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p27 Number of markets recording record-high June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4; same JNTO June 2026 record-market statement.] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/news/press/20250917_monthly.html` -> **snapshot** (snapshot 20260211174533); points raw/verified 4/4
  - p28 JNTO estimated foreign visitor arrivals to Japan, August 2025 (provisional estim = **3,428,000** arrivals (visits) (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "8月の訪日外客数は3,428,000人で、前年同月比では16.9%増となった。"
  - p29 Year-on-year change in foreign visitor arrivals to Japan, August 2025 = **16.9** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "8月の訪日外客数は3,428,000人で、前年同月比では16.9%増となった。"
  - p30 Foreign visitor arrivals to Japan, August 2024 (previous August record) = **2,933,381** arrivals (visits) (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "8月として過去最高であった2024年の2,933,381人を49万人以上上回り、同月過去最高を更新するとともに、同月として初めて300万人を超えた。"
  - p31 Number of markets recording their highest-ever August for foreign visitor arriva = **18** markets (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "韓国や中国、米国など18市場で8月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://yamatogokoro.jp/print/?post_id=60728&_type=inbound_data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### d5 [capacity_consumption] Airlines and travel agencies

Hypothesis: Seat capacity on international flights to Japan, multiplied by an estimated load factor and the share of foreign visitors, provides an upper bound or estimate. Booking data and forward-looking schedules can indicate demand.

Queries issued by the searcher: Japan international flight seat capacity August 2026; JNTO foreign visitor arrivals August 2026 forecast; Japan hotel bookings August 2026 foreign tourists OTA reservation; 訪日外客数 2026年8月 推計値 見通し 夏 予測; JNTO 訪日外客数 2026年7月 推計値 前年同月比

- `https://www.anahd.co.jp/group/ari/news/20260508.html` -> **snapshot** (snapshot 20260512070453); points raw/verified 15/0
- `http://tcfa.org.tw/announce_detail.asp?id=9213324` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp.trip.com/flights/status-cx5629/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aviationwire.jp/archives/343264/print/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (number: unknown scale word '万': 11; period_end 2026-10-24 after as_of: 4)

### d6 [shocks] Policy and external events

Hypothesis: Any major events (e.g., visa policy changes, natural disasters, pandemics, economic shocks, currency fluctuations) between the cutoff and August 2026 could affect arrivals. The impact can be estimated by comparing to similar past events.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2026 estimate; Japan National Tourism Organization monthly inbound visitors 2025 statistics; JNTO 訪日外客数 2026年6月推計値; China travel advisory Japan tourists decline 2026 monthly arrivals

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p32 Japan inbound foreign visitor arrivals, June 2026 estimate (JNTO) = **3,148,600** arrivals (visits) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p33 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p34 Japan inbound foreign visitor arrivals, cumulative first half (January-June) 202 = **21,084,800** arrivals (visits) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p35 Number of markets recording record-high June inbound arrivals to Japan, June 202 = **15** markets (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/news/press/20260121_monthly.html` -> **snapshot** (snapshot 20260801173314); points raw/verified 12/9
  - p36 JNTO estimated monthly foreign visitor arrivals to Japan, December 2025 (provisi = **3,617,700** arrivals (visits) (2025-12-01..2025-12-31) [EXCLUDED (ablation): ] quote: "訪日外客数(2025年12月推計値)12月:3,617,700人、12月過去最高を更新"
  - p37 Year-on-year change in December 2025 foreign visitor arrivals to Japan = **3.7** percent (2025-12-01..2025-12-31) [EXCLUDED (ablation): ] quote: "12月の訪日外客数は3,617,700人で、前年同月比では3.7%増となり、12月として過去最高を記録した。"
  - p38 JNTO estimated annual foreign visitor arrivals to Japan, calendar year 2025 = **42,683,600** arrivals (visits) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "2025年計:42,683,600人、年間で4,200万人を突破し過去最多"
  - p39 Year-on-year change in annual foreign visitor arrivals to Japan, calendar year 2 = **15.8** percent (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "2025年の年間訪日外客数は42,683,600人で、前年比では15.8%増と、過去最高であった2024年の36,870,148人を580万人以上上回り、年間過去最高を更新した。"
  - p40 Annual foreign visitor arrivals to Japan, calendar year 2024 (previous record) = **36,870,148** arrivals (visits) (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "過去最高であった2024年の36,870,148人を580万人以上上回り、年間過去最高を更新した。"
  - p41 Number of markets recording their highest-ever single month in December 2025 = **7** markets (2025-12-01..2025-12-31) [keep: ] quote: "韓国、タイなど7市場で単月過去最高を更新したほか"
  - p42 Number of markets recording their highest-ever December in 2025 = **14** markets (2025-12-01..2025-12-31) [keep: ] quote: "台湾や米国、カナダなど14市場で12月として過去最高を記録した。"
  - p43 Number of markets exceeding 1 million annual arrivals in 2025 (Australia being t = **7** markets (2025-01-01..2025-12-31) [keep: ] quote: "中国、韓国、台湾、米国、香港、タイに次ぎ7市場目となる年間で100万人を超えた市場となった。"
  - p44 Number of markets recording their highest-ever annual cumulative arrivals in 202 = **20** markets (2025-01-01..2025-12-31) [keep: ] quote: "なお、20市場が年間累計で過去最高を記録した。"
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/8
  - p45 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p46 Year-on-year change in Japan inbound foreign visitor arrivals, cumulative Januar = **2** percent (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p47 Year-on-year change in Japan inbound visitor arrivals from South Korea, June 202 = **7.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p48 Year-on-year change in Japan inbound visitor arrivals from Taiwan, June 2026 vs  = **14.6** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾が67万400人(同14.6%増)"
  - p49 Year-on-year change in Japan inbound visitor arrivals from United States, June 2 = **2.7** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "米国が35万4500人(同2.7%増)"
  - p50 Year-on-year change in Japan inbound visitor arrivals from China, June 2026 vs J = **57.3** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "中国が34万700人(同57.3%減)"
  - p51 Year-on-year change in Japan inbound visitor arrivals from Hong Kong, June 2026  = **28.5** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "香港が21万4300人(同28.5%増)"
  - p52 Number of markets setting record-high June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 from a secondary source; same underlying JNTO June 2026 record-market statement.] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- `https://www.scgr.co.jp/report/daily/2026072182279/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (number: unknown scale word '万': 4; number: more than one number in value_as_written: 7)

### d7 [attention] Search and social media trends

Hypothesis: Online search interest for Japan travel (e.g., Google Trends) correlates with actual arrivals with a lead time. If search interest for August 2026 travel is known, it can indicate demand strength relative to previous years.

Queries issued by the searcher: Google Trends Japan travel 2026 search interest; JNTO foreign visitor arrivals August 2026 forecast; "Japan travel" Google search interest 2026 increase year over year summer; 訪日旅行 検索ボリューム 2026年夏 Googleトレンド 旅行アプリ ダウンロード数

- `https://news1.kr/articles/?6240877` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnt` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/zh-hans/japan/google-search-trends-by-categories` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.itij.com/latest/news/adventure-travel-boom-puts-india-japan-and-jordan-top-2026-bookings` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [base_rates] seasonality

Hypothesis: The August share of annual foreign visitor arrivals in recent normal years (e.g., 2023-2025) would allow converting a full-year 2026 level or a recent monthly level into an August 2026 estimate. This is the missing input for a seasonality route and would materially reduce uncertainty around the summer peak.

Queries issued by the searcher: JNTO monthly foreign visitor arrivals August 2025 record full year 2024; Japan National Tourism Organization monthly arrivals August 2024 statistics visitors; JNTO 2025年 年間 訪日外客数 過去最高 4700万人 2025年12月推計値; 訪日外客数 2023年8月 215万人 2023年 年間 2506万人 JNTO

- `https://www.jnto.go.jp/news/press/20260121_monthly.html` -> **snapshot** (snapshot 20260801173314); points raw/verified 12/9
  - p53 JNTO estimated foreign visitor arrivals to Japan, December 2025 (monthly estimat = **3,617,700** arrivals (visits) (2025-12-01..2025-12-31) [EXCLUDED (ablation): ] quote: "訪日外客数(2025年12月推計値)12月:3,617,700人、12月過去最高を更新"
  - p54 JNTO estimated foreign visitor arrivals to Japan, full-year 2025 total = **42,683,600** arrivals (visits) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "2025年計:42,683,600人、年間で4,200万人を突破し過去最多"
  - p55 Year-on-year change in December 2025 foreign visitor arrivals to Japan = **3.7** percent (2025-12-01..2025-12-31) [EXCLUDED (ablation): ] quote: "12月の訪日外客数は3,617,700人で、前年同月比では3.7%増となり、12月として過去最高を記録した。"
  - p56 Year-on-year change in full-year 2025 foreign visitor arrivals to Japan = **15.8** percent (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "2025年の年間訪日外客数は42,683,600人で、前年比では15.8%増と、過去最高であった2024年の36,870,148人を580万人以上上回り"
  - p57 JNTO foreign visitor arrivals to Japan, full-year 2024 total (previous record) = **36,870,148** arrivals (visits) (2024-01-01..2024-12-31) [EXCLUDED (ablation): ] quote: "過去最高であった2024年の36,870,148人を580万人以上上回り、年間過去最高を更新した。"
  - p58 Number of markets recording a single-month record high in December 2025 = **7** markets (2025-12-01..2025-12-31) [DISCARD: Redundant duplicate of p41; same JNTO December 2025 single-month record statement.] quote: "韓国、タイなど7市場で単月過去最高を更新したほか"
  - p59 Number of markets recording a December record high in December 2025 = **14** markets (2025-12-01..2025-12-31) [DISCARD: Redundant duplicate of p42; same JNTO December 2025 record statement.] quote: "台湾や米国、カナダなど14市場で12月として過去最高を記録した。"
  - p60 Number of markets recording an annual cumulative record high in 2025 = **20** markets (2025-01-01..2025-12-31) [DISCARD: Redundant duplicate of p44; same JNTO 2025 annual record statement.] quote: "なお、20市場が年間累計で過去最高を記録した。"
  - p61 Number of markets (including Australia) exceeding 1 million annual arrivals in 2 = **7** markets (2025-01-01..2025-12-31) [DISCARD: Redundant duplicate of p43; same JNTO 2025 annual 1-million-market statement.] quote: "中国、韓国、台湾、米国、香港、タイに次ぎ7市場目となる年間で100万人を超えた市場となった。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/press/20240918_monthly.html` -> **snapshot** (snapshot 20250219093350); points raw/verified 5/5
  - p62 JNTO estimated foreign visitor arrivals to Japan, August 2024 (monthly estimate) = **2,933,000** arrivals (visits) (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "8月の訪日外客数は、2,933,000人で、前年同月比では36.0%増、2019年同月比では16.4%増となり、7か月連続で同月過去最高を記録した。"
  - p63 Year-on-year change in foreign visitor arrivals to Japan, August 2024 vs August  = **36** percent (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "8月の訪日外客数は、2,933,000人で、前年同月比では36.0%増、2019年同月比では16.4%増となり、7か月連続で同月過去最高を記録した。"
  - p64 Change in foreign visitor arrivals to Japan, August 2024 vs August 2019 = **16.4** percent (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "8月の訪日外客数は、2,933,000人で、前年同月比では36.0%増、2019年同月比では16.4%増となり、7か月連続で同月過去最高を記録した。"
  - p65 Number of markets recording record-high August foreign visitor arrivals to Japan = **17** markets (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "23市場のうち17市場(台湾、香港、シンガポール、インドネシア、フィリピン、ベトナム、インド、豪州、米国、カナダ、メキシコ、英国、フランス、ドイツ、イタリア、スペイン、中東地域)において8月として過去最高を記録した"
  - p66 Total number of markets tracked for foreign visitor arrivals to Japan, August 20 = **23** markets (2024-08-01..2024-08-31) [EXCLUDED (ablation): ] quote: "23市場のうち17市場(台湾、香港、シンガポール、インドネシア、フィリピン、ベトナム、インド、豪州、米国、カナダ、メキシコ、英国、フランス、ドイツ、イタリア、スペイン、中東地域)において8月として過去最高を記録した"
- `https://www.travelvoice.jp/20260121-159116/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (number: unknown scale word '万': 3)

### b2 [related_series] leading indicator

Hypothesis: International passenger arrival data at Narita, Haneda, Kansai, and other airports for July and early August 2026 would provide a near-real-time proxy for August foreign visitor arrivals. This would unlock a capacity/flow-based estimate and help resolve whether the June 2026 year-on-year decline persisted into the summer peak.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2026 estimate; Narita Haneda Kansai international passenger arrivals July 2026; JNTO 訪日外客数 2026年7月 344万2100人 速報; 成田空港 2026年7月 国際線旅客 速報 訪日客

- `https://www.aviationwire.jp/archives/tag/inbound/page/2` -> **snapshot** (snapshot 20260614042726); points raw/verified 13/6
  - p67 羽田空港 2026年2月 総旅客数の前年同月比 = **1.6** % (year-on-year change) (2026-02-01..2026-02-28) [keep: ] quote: "2026年2月の国内線と国際線を合わせた総旅客数は、前年同月比1.6%増の718万9654人だった。"
  - p68 成田国際空港 2026年3月 総旅客数の前年同月比 = **5** % (year-on-year change) (2026-03-01..2026-03-31) [keep: ] quote: "国際線と国内線を合わせた総旅客数は前年同月比5%増の385万9350人で、8カ月連続で前年同月を上回った。"
  - p69 成田国際空港 2026年3月 国際線・国内線合計総発着回数の前年同月比 = **1** % (year-on-year change) (2026-03-01..2026-03-31) [keep: ] quote: "国際線と国内線を合わせた総発着回数は1%減の2"
  - p70 成田国際空港 2025年度 総旅客数の前年度比 = **4** % (year-on-year change) (2025-04-01..2026-03-31) [keep: ] quote: "国際線と国内線を合わせた旅客数は前年度比4%増の4258万9518人で、2018年度に次ぎ歴代2位を記録した。"
  - p71 関西国際空港 2026年3月 総旅客数の前年同月比 = **4** % (year-on-year change) (2026-03-01..2026-03-31) [keep: ] quote: "関空の国際線と国内線を合わせた総旅客数は、前年同月比4%減の273万799人だった。"
  - p72 中部国際空港 2026年3月 総旅客数の前年同月比 = **2** % (year-on-year change) (2026-03-01..2026-03-31) [keep: ] quote: "国際線と国内線を合わせた総旅客数は前年同月比2%増の106万1463人で、3カ月ぶりに前年同月を上回った。"
- `https://www.aviationwire.jp/archives/tag/%e7%99%ba%e7%9d%80%e5%9b%9e%e6%95%b0/page/2` -> **snapshot** (snapshot 20260418235452); points raw/verified 15/8
  - p73 Kansai International Airport total passengers (international + domestic), Januar = **9** percent (2026-01-01..2026-01-31) [keep: ] quote: "関空の国際線と国内線を合わせた総旅客数は、前年同月比9%減の256万8089人だった。"
  - p74 Haneda Airport total passengers (domestic + international), November 2025, year- = **2.4** percent (2025-11-01..2025-11-30) [keep: ] quote: "2025年11月の国内線と国際線を合わせた総旅客数は、前年同月比2.4%増の796万3876人だった。"
  - p75 Narita Airport total passengers (international + domestic), December 2025 prelim = **4** percent (2025-12-01..2025-12-31) [keep: ] quote: "国際線と国内線を合わせた総旅客数は前年同月比4%増の364万9542人で、5カ月連続で前年同月を上回り、12月としては2019年に次ぐ2番目の記録とな"
  - p76 Narita Airport total passengers (international + domestic), calendar year 2025,  = **6** percent (2025-01-01..2025-12-31) [keep: ] quote: "国際線と国内線を合わせた総旅客数は前年比6%増の4225万5291人で、2019年以来6年ぶりに4000万人を超えた。"
  - p77 Narita Airport foreign visitor arrivals (訪日客), calendar year 2025 = **2,300** people (2025-01-01..2025-12-31) [keep: ] quote: "このうち訪日客は2300"
  - p78 Kansai International Airport total passengers (international + domestic), Decemb = **3** percent (2025-12-01..2025-12-31) [keep: ] quote: "関空の国際線と国内線を合わせた総旅客数は、前年同月比3%減の271万7182人だった。"
  - p79 Kansai International Airport total passengers including transit (international + = **3,409** people (2025-01-01..2025-12-31) [keep: ] quote: "関空の通過旅客を含む国際線と国内線の総旅客数は前年比11%増の3409万"
  - p80 Kansai International Airport total passengers including transit (international + = **11** percent (2025-01-01..2025-12-31) [keep: ] quote: "関空の通過旅客を含む国際線と国内線の総旅客数は前年比11%増の3409万"
- `https://www.jnto.go.jp/news/press/20260819_montly` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (number: more than one number in value_as_written: 12; period_end missing or unparseable: 2)

### b3 [forecasts_markets] official target

Hypothesis: A Japan Tourism Agency or JNTO full-year 2026 inbound target or forecast, combined with August seasonality, would provide a baseline for August 2026. This is the most direct missing input for a top-down forecast route and would anchor the estimate against the June 2026 decline.

Queries issued by the searcher: Japan Tourism Agency 2026 inbound tourism forecast target visitors; JNTO 2026 foreign visitor arrivals forecast; 訪日外客数 2025年8月 過去最高 JNTO 推計値; JNTO 訪日外客数 2026年6月 推計値 前年同月比

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yamatogokoro.jp/inbound_data/58034/` -> **snapshot** (snapshot 20260515113739); points raw/verified 15/1
  - p81 Year-on-year growth rate of foreign visitor arrivals to Japan, August 2025 vs Au = **16.9** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "前年同月(2024年8月)の293万3381人を49万人上回り、16.9%増となった"
- `https://www.kankokeizai.com/2603121130kks/` -> **snapshot** (snapshot 20260411120026); points raw/verified 7/0
- dropped by code checks: 21 (number: more than one number in value_as_written: 16; number: unknown scale word '万人': 1; number: unknown scale word '兆円': 2; number: unknown scale word '万人泊': 1; period_end 2030-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'visitor arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p2', 'p4', 'p13', 'p27', 'p52'] All five points describe the same JNTO June 2026 release: foreign visitor arrivals fell 6.8% year-on-year to 3.15 million, while 15 markets set June records. p4, p13, p27 and p52 are redundant restate
- corroborating: ['p41', 'p42', 'p43', 'p44'] These are all from the JNTO January 2026 annual/December release and describe the strength of 2025 inbound tourism: 7 markets set single-month records in December 2025, 14 set December records, 7 mark
- contextual: ['p2', 'p41', 'p42', 'p43', 'p44'] June 2026 arrivals were down 6.8% year-on-year despite many market records, implying the 2025 base was exceptionally strong and/or some large source markets (notably China) weakened. This is a materia
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p2', 'p4', 'p13', 'p27', 'p52'] All describe June 2026 JNTO foreign visitor arrivals: p2 gives the level change (-6.8% YoY to 3.15 million) while p4/p13/p27/p52 report the same JNTO release that 15 markets set June records. They sha
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p58', 'p59', 'p60', 'p61'] These are duplicate or near-duplicate JNTO statements about 2025 records: December 2025 single-month records (7 markets), December records (14 markets), 2025 annual records (20 markets), and 7 markets
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80'] Airport passenger statistics for Haneda, Narita, Kansai, and Chubu show mixed but generally positive passenger trends through early 2026. They are related to foreign visitor arrivals but cover total p

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 foreign visitor arrivals relative to June 2026 arrivals | 1.15 | 1..1.35 | 0.8216..1.643 (widened) | ratio | unused | August is typically a summer peak month for Japan inbound tourism, with arrivals often 10-20% above June. June 2026 was 3.15 million (p2). A ratio of 1.15 is a central summer uplift, with wide uncertainty reflecting possible continuation of the June YoY decline and unknown policy or demand shocks. | The seasonal pattern from recent normal years (2023-2025) holds and no major new shock occurs between June and August 2026. | Evidence that August 2026 arrivals were below June 2026 levels, or that a major shock (e.g., new travel restrictions, natural disaster) suppressed summer travel. |
| a2 | August 2026 foreign visitor arrivals relative to August 2025 arrivals | 0.95 | 0.8..1.1 | 0.6633..1.327 (widened) | ratio | unused | June 2026 was down 6.8% YoY (p2), suggesting a possible slowdown. August 2026 may be slightly below August 2025, but summer peak demand and record market strength (p4) could offset. A ratio of 0.95 with wide uncertainty reflects this tension. | The YoY decline observed in June 2026 persists into August 2026, but no severe deterioration occurs. | Evidence that August 2026 arrivals exceeded August 2025, or that the decline deepened substantially. |

Rejected by code:

- a3 June 2026 foreign visitor arrivals level: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['japan']; quantity stems: ['arriv', 'visit']
- points excluded before the judge: 54 of 81
- methods allowed: ['formula_mc']

  - p1 June 2026 foreign visitor arrivals to Japan, detailed count = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p3 Cumulative first-half 2026 foreign visitor arrivals to Japan = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p5 Foreign visitors to Japan, April 2026 (JNTO estimate) = 3,692,200 (2026-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p6 Year-on-year change in foreign visitors to Japan, April 2026 = 5.5 (2026-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p7 Foreign visitors to Japan from South Korea, May 2026 = 951,300 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p8 Foreign visitors to Japan from Taiwan, May 2026 = 616,800 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p9 Foreign visitors to Japan from the United States, May 2026 = 333,700 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p10 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p11 Year-on-year change in foreign visitor arrivals to Japan, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p12 Cumulative foreign visitor arrivals to Japan, first half (January-June) 2026 = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p14 Japan tourist arrivals, actual, June 2026 = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p15 Japan tourist arrivals, previous month, May 2026 = 3,559,900 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p16 Japan tourist arrivals, long-run average, 1991 to 2026 = 971,885 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p17 Japan tourist arrivals, all-time high, April 2025 = 3,908,900 (2025-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p18 Japan tourist arrivals, record low, May 2020 = 1,700 (2020-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p19 Japan tourist arrivals, forecast for end of current quarter (Q2 2026), Trading Economics a = 3,150,000 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p20 Japan tourist arrivals, actual, June 2026 (related table row) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p21 Japan tourist arrivals, previous month, May 2026 (related table row) = 3,559,900 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p22 Japan tourist arrivals, highest value, 1991-2026 series = 3,908,900 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p23 Japan tourist arrivals, lowest value, 1991-2026 series = 1,700 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p24 Japan inbound foreign visitor arrivals, June 2026 (JNTO estimate, detailed) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p25 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p26 Cumulative Japan inbound foreign visitor arrivals, first half of 2026 = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p28 JNTO estimated foreign visitor arrivals to Japan, August 2025 (provisional estimate) = 3,428,000 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p29 Year-on-year change in foreign visitor arrivals to Japan, August 2025 = 16.9 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p30 Foreign visitor arrivals to Japan, August 2024 (previous August record) = 2,933,381 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p31 Number of markets recording their highest-ever August for foreign visitor arrivals to Japa = 18 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p32 Japan inbound foreign visitor arrivals, June 2026 estimate (JNTO) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p33 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p34 Japan inbound foreign visitor arrivals, cumulative first half (January-June) 2026 (JNTO) = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p35 Number of markets recording record-high June inbound arrivals to Japan, June 2026 = 15 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p36 JNTO estimated monthly foreign visitor arrivals to Japan, December 2025 (provisional estim = 3,617,700 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p37 Year-on-year change in December 2025 foreign visitor arrivals to Japan = 3.7 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p38 JNTO estimated annual foreign visitor arrivals to Japan, calendar year 2025 = 42,683,600 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p39 Year-on-year change in annual foreign visitor arrivals to Japan, calendar year 2025 = 15.8 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p40 Annual foreign visitor arrivals to Japan, calendar year 2024 (previous record) = 36,870,148 (2024-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p45 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p46 Year-on-year change in Japan inbound foreign visitor arrivals, cumulative January-June 202 = 2 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p47 Year-on-year change in Japan inbound visitor arrivals from South Korea, June 2026 vs June  = 7.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p48 Year-on-year change in Japan inbound visitor arrivals from Taiwan, June 2026 vs June 2025 = 14.6 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p49 Year-on-year change in Japan inbound visitor arrivals from United States, June 2026 vs Jun = 2.7 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p50 Year-on-year change in Japan inbound visitor arrivals from China, June 2026 vs June 2025 = 57.3 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p51 Year-on-year change in Japan inbound visitor arrivals from Hong Kong, June 2026 vs June 20 = 28.5 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p53 JNTO estimated foreign visitor arrivals to Japan, December 2025 (monthly estimate) = 3,617,700 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p54 JNTO estimated foreign visitor arrivals to Japan, full-year 2025 total = 42,683,600 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p55 Year-on-year change in December 2025 foreign visitor arrivals to Japan = 3.7 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p56 Year-on-year change in full-year 2025 foreign visitor arrivals to Japan = 15.8 (2025-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p57 JNTO foreign visitor arrivals to Japan, full-year 2024 total (previous record) = 36,870,148 (2024-12-31): ablation: name refers to the target entity ['japan'] and quantity
  - p62 JNTO estimated foreign visitor arrivals to Japan, August 2024 (monthly estimate) = 2,933,000 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p63 Year-on-year change in foreign visitor arrivals to Japan, August 2024 vs August 2023 = 36 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p64 Change in foreign visitor arrivals to Japan, August 2024 vs August 2019 = 16.4 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p65 Number of markets recording record-high August foreign visitor arrivals to Japan, August 2 = 17 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p66 Total number of markets tracked for foreign visitor arrivals to Japan, August 2024 = 23 (2024-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p81 Year-on-year growth rate of foreign visitor arrivals to Japan, August 2025 vs August 2024 = 16.9 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) in its monthly press release. The JNTO estimate counts foreign nationals entering Japan for any purpose (tourism, business, visiting friends/relatives, etc.) ba | unit persons (arrivals, not unique individuals) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [own_history] JNTO monthly estimates

Hypothesis: August 2026 foreign visitor arrivals can be projected from the same month in previous years, adjusted for recent year-on-year growth trends. August is a peak month due to summer holidays. The relationship is: target = August 2025 value × (1 + recent YoY growth rate).

Queries issued by the searcher: JNTO monthly foreign visitor arrivals August 2025; JNTO 訪日外客数 2026年6月; Japan inbound tourism statistics 2026 monthly visitors year-on-year; 訪日外客数 2025年8月 推計値 JNTO

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p1 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** persons (foreign visitor arrivals) (2026-06-01..2026-06-30) [keep: ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p2 Year-on-year change in foreign visitor arrivals to Japan, June 2026 = **6.8** % (2026-06-01..2026-06-30) [keep: ] quote: "6月:前年同月比6.8%減の315万人"
  - p3 Cumulative foreign visitor arrivals to Japan, first half of 2026 (January–June) = **21,084,800** persons (foreign visitor arrivals, cumulative) (2026-01-01..2026-06-30) [keep: ] quote: "また、上半期の累計で21,084,800人となった。"
  - p4 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.jnto.go.jp/statistics/data/_files/20260715_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20250917-158383` -> **snapshot** (snapshot 20260608084226); points raw/verified 15/7
  - p5 August 2025 YoY growth rate of foreign visitor arrivals to Japan = **16.9** percent (year-on-year change) (2025-08-01..2025-08-31) [keep: ] quote: "2025年8月の訪日外国人旅行者数(推計値)は前年比16.9%増の342万8000人となり、8月として初めて300万人を超えた。"
  - p6 August 2025 vs August 2023 increase rate of foreign visitor arrivals to Japan = **58.9** percent (increase) (2025-08-01..2025-08-31) [keep: ] quote: "2023年8月(実数:215万7190人)比では、58.9%増。"
  - p7 August 2025 YoY growth rate of foreign visitor arrivals to Japan from China = **36.5** percent (year-on-year change) (2025-08-01..2025-08-31) [keep: ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)"
  - p8 August 2025 YoY growth rate of foreign visitor arrivals to Japan from South Kore = **8** percent (year-on-year change) (2025-08-01..2025-08-31) [keep: ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)"
  - p9 August 2025 YoY growth rate of foreign visitor arrivals to Japan from Taiwan = **10** percent (year-on-year change) (2025-08-01..2025-08-31) [keep: ] quote: "台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)"
  - p10 August 2025 YoY growth rate of foreign visitor arrivals to Japan from Hong Kong = **8.3** percent (year-on-year change, decrease) (2025-08-01..2025-08-31) [keep: ] quote: "台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)"
  - p11 August 2025 YoY growth rate of foreign visitor arrivals to Japan from United Sta = **11.7** percent (year-on-year change) (2025-08-01..2025-08-31) [keep: ] quote: "米国が19万4500人(同11.7%増)の順。"
- dropped by code checks: 9 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 8)

### d2 [related_series] Ministry of Justice (MOJ) immigration statistics

Hypothesis: JNTO estimates are derived from MOJ immigration records. The number of foreign nationals entering Japan in August 2026 can be approximated by MOJ monthly entry data, which may be published with a similar lag. The relationship is: JNTO estimate ≈ MOJ foreign entries minus certain categories (e.g., re-entries of foreign residents).

Queries issued by the searcher: 出入国在留管理庁 外国人入国者数 月別 2026; JNTO 訪日外客数 2026年7月 推計; JNTO 訪日外客数 2026年6月推計値 前年同月比6.8%減 314万人; 出入国在留管理庁 2026年6月 外国人入国者数 速報 出入国管理統計

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p12 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** persons (foreign visitor arrivals) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1 (same JNTO June 2026 estimate).] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p13 Year-on-year change in JNTO estimated foreign visitor arrivals, June 2026 vs Jun = **6.8** percent (year-on-year change) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2 (same June 2026 YoY).] quote: "6月:前年同月比6.8%減の315万人"
  - p14 JNTO cumulative foreign visitor arrivals to Japan, first half (January–June) 202 = **21,084,800** persons (foreign visitor arrivals, cumulative) (2026-01-01..2026-06-30) [DISCARD: Redundant duplicate of p3 (same H1 2026 cumulative).] quote: "また、上半期の累計で21,084,800人となった。"
  - p15 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4 (same 15 markets).] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/_files/20260617_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040455745&iroha=18` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://mediachina.jp/info/6762696` -> **snapshot** (snapshot 20260618075922); points raw/verified 14/2
  - p16 Year-on-year change in new entrants from China (mainland) in April = **57** percent (year-on-year decrease) (2026-04-01..2026-04-30) [keep: ] quote: "前年の4月は61万1千人余りで、57%のマイナスとなっている。"
  - p17 New entrants from China (mainland) for study purposes, January to February = **390** persons (new entries for study) (2026-01-01..2026-02-28) [DISCARD: Study entrants are a tiny, non-representative subset; adds little to the total estimate.] quote: "これに先立って判明した1-2月における中国からの「留学」新規来日者数は390人で、前年比では2か月連続で3割程度のマイナスとなっている。"
- dropped by code checks: 13 (number: unknown scale word '万': 2; number: more than one number in value_as_written: 11)

### d3 [base_rates] Seasonal patterns and source market mix

Hypothesis: August has a consistent seasonal pattern in Japan's inbound tourism, with a peak due to summer holidays from East Asia. The share of August in annual arrivals is stable. The relationship is: target = annual arrivals × August share. Also, source market mix (South Korea, China, Taiwan, etc.) affects total.

Queries issued by the searcher: JNTO 訪日外国人 月別 2025年8月 推計値; Japan inbound tourism August arrivals share of annual total seasonal; JNTO 2026年7月 訪日外客数 推計値 1月～7月累計 2,453万人; 訪日外客数 月別推移 2025年 8月 3,428,000人 年間 4,268万人 割合

- `https://www.jnto.go.jp/news/press/20250917_monthly.html` -> **snapshot** (snapshot 20260211174533); points raw/verified 5/5
  - p18 JNTO estimated foreign visitor arrivals to Japan, August 2025 (provisional estim = **3,428,000** persons (2025-08-01..2025-08-31) [keep: ] quote: "8月の訪日外客数は3,428,000人で、前年同月比では16.9%増となった。"
  - p19 Year-on-year change in foreign visitor arrivals to Japan, August 2025 = **16.9** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p18/p5 (August 2025 +16.9%).] quote: "8月の訪日外客数は3,428,000人で、前年同月比では16.9%増となった。"
  - p20 Foreign visitor arrivals to Japan, August 2024 (previous August record) = **2,933,381** persons (2024-08-01..2024-08-31) [keep: ] quote: "8月として過去最高であった2024年の2,933,381人を49万人以上上回り"
  - p21 Number of markets recording their highest-ever August foreign visitor arrivals,  = **18** markets (2025-08-01..2025-08-31) [keep: ] quote: "韓国や中国、米国など18市場で8月として過去最高を記録した。"
  - p22 Number of markets recording their highest-ever August foreign visitor arrivals,  = **18** markets (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p21 (same 18 markets); market list adds no numeric input.] quote: "*8月過去最高の18市場は韓国、中国、マレーシア、インドネシア、フィリピン、ベトナム、インド、豪州、米国、カナダ、メキシコ、英国、フランス、ドイツ、イタリア、ロシア、北欧地域、中東地域。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/_files/20260819_1615.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://yamatogokoro.jp/inbound_data/58034/` -> **snapshot** (snapshot 20260515113739); points raw/verified 15/1
  - p23 Year-on-year growth rate of foreign visitor arrivals, August 2025 vs August 2024 = **16.9** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p18/p5.] quote: "前年同月(2024年8月)の293万3381人を49万人上回り、16.9%増となった"
- dropped by code checks: 14 (number: more than one number in value_as_written: 14)

### d4 [physical_flow] Airport and seaport passenger traffic

Hypothesis: Foreign visitor arrivals are a subset of total international passenger arrivals at Japanese airports and seaports. If total international arrivals and the foreign visitor share are known, the target can be estimated. The relationship is: target = total international arrivals × foreign visitor share. August is peak season, so capacity and load factors are high.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan monthly 2026; Japan international passenger arrivals August 2025 Narita Haneda statistics; JNTO 訪日外客数 2025年8月 推計値 342万人; 成田空港 2025年8月 空港運用状況 国際線 旅客数 到着

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.narita-airport.jp/files/b2e22b1f56ede88eda96151d616c3d8893efaeaa57658001834df6fb32d70835` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260617_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.47news.jp/13060940.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] International flight seat capacity and hotel bookings

Hypothesis: Foreign visitor arrivals are constrained by available international flight seats and accommodation capacity. If seat capacity and load factors are known, arrivals can be estimated. The relationship is: target ≈ international seat capacity × load factor × foreign visitor share. August is peak, so load factors are high.

Queries issued by the searcher: Japan international flight seat capacity August 2026; OAG Japan inbound international seats 2026 forecast; JNTO 2026年7月 訪日外客数 推計値; 訪日外国人 2026年8月 宿泊者数 ホテル稼働率 外国人比率

- `https://www.anahd.co.jp/group/ari/news/20260508.html` -> **snapshot** (snapshot 20260512070453); points raw/verified 15/0
- `http://tcfa.org.tw/announce_detail.asp?id=9213324` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://jp.trip.com/flights/status-cx5629/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aviationwire.jp/archives/343264/print/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (number: unknown scale word '万': 13; period_end 2026-10-24 after as_of: 2)

### d6 [forecasts_markets] Government targets and industry forecasts

Hypothesis: The Japanese government has set targets for inbound tourism (e.g., 60 million visitors by 2030). Industry forecasts for 2026 may provide a baseline. The relationship is: target = annual forecast × August seasonal share.

Queries issued by the searcher: Japan inbound tourism forecast 2026 foreign visitors; 訪日外国人 2026年 予測 JNTO; JNTO 訪日外客数 2025年8月 月別 推計値; 訪日外客数 月別 2024年 8月 279万人 季節性

- `https://www.jtbcorp.jp/jp/newsroom/2026/01/08_jtb_inbound_outlook.html` -> **snapshot** (snapshot 20260510055357); points raw/verified 15/3
  - p24 JAPANiCAN.com booking count growth, Taiwan, Jan-Apr 2026 vs same period prior ye = **161** percent (year-on-year index, prior year = 100) (2026-01-01..2026-04-30) [keep: ] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p25 JAPANiCAN.com booking count growth, South Korea, Jan-Apr 2026 vs same period pri = **138** percent (year-on-year index, prior year = 100) (2026-01-01..2026-04-30) [keep: ] quote: "前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p26 JAPANiCAN.com booking count growth, China, Jan-Apr 2026 vs same period prior yea = **50** percent (year-on-year index, prior year = 100) (2026-01-01..2026-04-30) [keep: ] quote: "日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://yamatogokoro.jp/inbound_data/58034/` -> **snapshot** (snapshot 20260515113739); points raw/verified 15/2
  - p27 Year-on-year growth rate of foreign visitor arrivals to Japan, August 2025 vs Au = **16.9** % (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p18/p5.] quote: "前年同月(2024年8月)の293万3381人を49万人上回り、16.9%増となった"
  - p28 Year-on-year growth rate of cumulative foreign visitor arrivals to Japan, Januar = **18.2** % (2025-01-01..2025-08-31) [DISCARD: Jan-Aug 2025 cumulative is not needed once August 2025 level and 2026 H1 are known.] quote: "2025年1月〜8月の累計訪日客数は2838万3600人で、前年同期比18.2%増となった"
- `https://www.kankokeizai.com/2607290745kks/` -> **snapshot** (snapshot 20260730032651); points raw/verified 15/8
  - p29 Japan inbound foreign visitor arrivals, 2026 January–May year-on-year change = **1.1** percent (year-on-year change) (2026-01-01..2026-05-31) [keep: ] quote: "2026年1月から5月の訪日外国人客数は前年比1.1%減で推移。"
  - p30 Japan inbound visitors from China, monthly year-on-year decline range, 2026 Janu = **45.2** percent (year-on-year decline) (2026-01-01..2026-05-31) [keep: ] quote: "中国からの訪客は各月で前年同月比45.2〜60.7%減と大幅に落ち込んでいる。"
  - p31 Japan inbound visitors from China, monthly year-on-year decline range, 2026 Janu = **60.7** percent (year-on-year decline) (2026-01-01..2026-05-31) [DISCARD: Upper end of the same China decline range already captured by p30; redundant for a central estimate.] quote: "中国からの訪客は各月で前年同月比45.2〜60.7%減と大幅に落ち込んでいる。"
  - p32 Japan inbound visitors from countries/regions excluding China, 2026 January–May  = **14.1** percent (year-on-year growth) (2026-01-01..2026-05-31) [keep: ] quote: "中国以外の国・地域からの訪客は1〜5月平均で前年比14.1%増。"
  - p33 Japan inbound visitors from countries/regions excluding China, February 2026 yea = **21.1** percent (year-on-year growth) (2026-02-01..2026-02-28) [keep: ] quote: "月によっては21.1%増(2月)・17.3%増(3月)を記録するなど堅調な伸びが続き"
  - p34 Japan inbound visitors from countries/regions excluding China, March 2026 year-o = **17.3** percent (year-on-year growth) (2026-03-01..2026-03-31) [keep: ] quote: "月によっては21.1%増(2月)・17.3%増(3月)を記録するなど堅調な伸びが続き"
  - p35 China share of Japan inbound visitors, 2019 = **30** percent (share of total inbound visitors) (2019-01-01..2019-12-31) [keep: ] quote: "2019年時点で約30%を占めた中国の比率は、2026年1〜5月には約9.6%まで低下した。"
  - p36 China share of Japan inbound visitors, 2026 January–May = **9.6** percent (share of total inbound visitors) (2026-01-01..2026-05-31) [keep: ] quote: "2019年時点で約30%を占めた中国の比率は、2026年1〜5月には約9.6%まで低下した。"
- dropped by code checks: 32 (number: unknown scale word '万人': 7; period_end 2026-12-31 after as_of: 6; number: unknown scale word '兆円': 2; number: unknown scale word '万人泊': 3; period_end missing or unparseable: 1; number: more than one number in value_as_written: 13)

### d7 [shocks] Travel advisories, visa policies, and economic conditions

Hypothesis: Shocks such as currency fluctuations (weak yen), visa liberalization, travel advisories, or geopolitical events can significantly affect inbound tourism. A weaker yen boosts arrivals; travel restrictions reduce them. The relationship is: target = baseline × shock multiplier.

Queries issued by the searcher: JNTO monthly press release inbound visitors August 2026; yen exchange rate August 2026 JPY USD level; Japan travel advisory China citizens avoid Japan November 2025 arrivals decline flight cuts; JNTO 訪日外客数 2026年6月推計値 中国 減少

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-in-august-2026-were-down-9-6-to-3-1-million-despite-record-high-in-14-source-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fr.theglobaleconomy.com/Japan/Dollar_exchange_rate/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinadaily.com.cn/a/202601/28/WS69796092a310d6866eb361c3.html` -> **snapshot** (snapshot 20260208082302); points raw/verified 8/5
  - p37 Cancellation rate for flights from the Chinese mainland to Japan in January 2026 = **47.2** percent (2026-01-01..2026-01-31) [keep: ] quote: "in January 2026, the cancellation rate for flights from the Chinese mainland to Japan reached 47.2 percent"
  - p38 Increase in cancellation rate for flights from the Chinese mainland to Japan in  = **7.8** percentage points (2026-01-01..2026-01-31) [DISCARD: Month-on-month change in cancellation rate; not needed for the level estimate.] quote: "up 7.8 percentage points from the previous month"
  - p39 Chinese nationals (excluding Hong Kong, Macao and Taiwan) traveling to Japan in  = **348,700** persons (2025-12-01..2025-12-31) [keep: ] quote: "about 348,700 Chinese nationals, excluding those from Hong Kong, Macao and Taiwan, traveled to Japan in December 2025"
  - p40 Year-on-year decline in Chinese nationals traveling to Japan in December 2025 = **40** percent (2025-12-01..2025-12-31) [keep: ] quote: "down about 40 percent from the previous year"
  - p41 Month-on-month decline in Chinese nationals traveling to Japan in December 2025  = **35** percent (2025-12-01..2025-12-31) [DISCARD: Month-on-month decline; redundant with p40 for the level estimate.] quote: "about 35 percent from November 2025"
- dropped by code checks: 3 (period_end missing or unparseable: 3)

### d8 [attention] Search and social media interest

Hypothesis: Online search interest for Japan travel (e.g., Google Trends) correlates with actual arrivals, especially for leisure travelers. A spike in search interest in the months before August 2026 could indicate higher arrivals. The relationship is: target = baseline × (search index / baseline search index).

Queries issued by the searcher: Google Trends Japan travel 2026 search interest; JNTO 訪日外国人 2026年 推計 月別; 2025年8月 訪日外客数 342万人 JNTO 前年同月比; 訪日旅行 検索 トレンド 2026年夏 Google Trends 韓国 台湾 米国

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.travelvoice.jp/20250917-158383` -> **snapshot** (snapshot 20260608084226); points raw/verified 15/7
  - p42 Year-on-year change in JNTO estimated foreign visitor arrivals to Japan, August  = **16.9** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p18/p5.] quote: "2025年8月の訪日外国人旅行者数(推計値)は前年比16.9%増の342万8000人となり、8月として初めて300万人を超えた。"
  - p43 Increase in August 2025 foreign visitor arrivals to Japan versus August 2023 = **58.9** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p6.] quote: "2023年8月(実数:215万7190人)比では、58.9%増。"
  - p44 Year-on-year change in foreign visitor arrivals to Japan from China, August 2025 = **36.5** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p7.] quote: "中国が101万8600人(前年比36.5%増)"
  - p45 Year-on-year change in foreign visitor arrivals to Japan from South Korea, Augus = **8** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p8.] quote: "韓国が66万900人(同8%増)"
  - p46 Year-on-year change in foreign visitor arrivals to Japan from Taiwan, August 202 = **10** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p9.] quote: "台湾が62万700人(同10%増)"
  - p47 Year-on-year change in foreign visitor arrivals to Japan from Hong Kong, August  = **8.3** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p10.] quote: "香港が22万6100人(同8.3%減)"
  - p48 Year-on-year change in foreign visitor arrivals to Japan from the United States, = **11.7** percent (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p11.] quote: "米国が19万4500人(同11.7%増)"
- `https://www.itij.com/latest/news/adventure-travel-boom-puts-india-japan-and-jordan-top-2026-bookings` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ceicdata.com/en/japan/google-search-trends-by-categories` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (number: more than one number in value_as_written: 8)

### b1 [own_history] JNTO monthly estimates

Hypothesis: The July 2026 JNTO estimate (released mid-August 2026) would provide the most recent monthly level and YoY growth, allowing a direct carry-forward into August 2026. This is the single most important missing input for the own-history route.

Queries issued by the searcher: JNTO July 2026 foreign visitor arrivals estimate; Japan National Tourism Organization 訪日外客数 2026年7月; JNTO 訪日外客数 2026年6月推計値 314万8600人 前年同月比; 訪日外客数 2025年8月 推計値 JNTO 前年同月比

- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p49 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** persons (foreign visitor arrivals) (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p1.] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p50 JNTO estimated foreign visitor arrivals to Japan, June 2026, year-on-year change = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p2.] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p51 JNTO estimated cumulative foreign visitor arrivals to Japan, first half of 2026  = **21,084,800** persons (foreign visitor arrivals, cumulative) (2026-01-01..2026-06-30) [DISCARD: Redundant duplicate of p3.] quote: "また、上半期の累計で21,084,800人となった。"
  - p52 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [DISCARD: Redundant duplicate of p4.] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://yamatogokoro.jp/print/?post_id=61032&_type=inbound_data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-statistics/inbound-travel-statistics/` -> **snapshot** (snapshot 20260731002019); points raw/verified 5/5
  - p53 Foreign visitors to Japan, April 2026, JNTO estimate = **3,692,200** persons (foreign visitor arrivals) (2026-04-01..2026-04-30) [keep: ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p54 Year-on-year change in foreign visitors to Japan, April 2026, JNTO estimate = **5.5** % (2026-04-01..2026-04-30) [keep: ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p55 Foreign visitors to Japan from South Korea, May 2026 = **951,300** persons (foreign visitor arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p56 Foreign visitors to Japan from Taiwan, May 2026 = **616,800** persons (foreign visitor arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p57 Foreign visitors to Japan from the United States, May 2026 = **333,700** persons (foreign visitor arrivals) (2026-05-01..2026-05-31) [keep: ] quote: "r of foreign visitors to Japan in May 2026 by country and region, South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### b2 [related_series] China market recovery

Hypothesis: The China collapse is the dominant driver of the 2026 slowdown. Evidence on whether China arrivals were still falling, stabilizing, or recovering by July–August 2026 would materially narrow the uncertainty in the total August estimate.

Queries issued by the searcher: JNTO 訪日外国人旅行者数 2026年7月 中国; 訪日中国人客 2026年6月 減少 訪日外客数; 中国 訪日 団体旅行 再開 2026年7月 訪日中国人 回復の兆し; 访日中国游客 2026年7月 机票 预订 日本 暑期 恢复

- `https://news.infoseek.co.jp/article/prtimes_000000055_000060253/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://china.kyodonews.net/articles/-/12958` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://japannews.yomiuri.co.jp/world/asia-pacific/20260620-333862/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://finance.sina.com.cn/jjxw/2026-07-27/doc-inikfnph9950485.shtml` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [capacity_consumption] Air capacity

Hypothesis: International seat capacity and load factors to Japan in August 2026 would provide an independent physical-flow check on the demand-based projection, especially given the China route cancellations.

Queries issued by the searcher: JNTO 訪日外客数 2026年8月 推計; international seat capacity to Japan summer 2026 airline schedule; OAG seat capacity Japan international flights summer 2026 schedule seats; 中国 日本 航空便 減便 2026年8月 訪日 注意喚起

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260916_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20260916-160529` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://honichi.com/news/2026/09/16/inbound202608/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'inbound arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p12'] Identical JNTO June 2026 estimate reported by the same publisher; p12 is a duplicate of p1 and adds no independent information.
- corroborating: ['p2', 'p13'] Identical June 2026 YoY decline from the same JNTO release; p13 duplicates p2.
- corroborating: ['p3', 'p14'] Identical JNTO first-half 2026 cumulative arrivals; p14 duplicates p3.
- corroborating: ['p4', 'p15'] Identical count of markets with record June arrivals; p15 duplicates p4.
- corroborating: ['p5', 'p18', 'p19', 'p23', 'p27', 'p42'] All report the same August 2025 JNTO estimate and 16.9% YoY growth, mostly from the same JNTO release or secondary summaries of it. They are not independent measurements.
- corroborating: ['p6', 'p43'] Same August 2025 vs August 2023 increase rate from the same underlying JNTO data.
- corroborating: ['p7', 'p44'] Same August 2025 China YoY growth from the same source.
- corroborating: ['p8', 'p45'] Same August 2025 South Korea YoY growth from the same source.
- corroborating: ['p9', 'p46'] Same August 2025 Taiwan YoY growth from the same source.
- corroborating: ['p10', 'p47'] Same August 2025 Hong Kong YoY growth from the same source.
- corroborating: ['p11', 'p48'] Same August 2025 US YoY growth from the same source.
- corroborating: ['p20', 'p23'] August 2024 level and the implied August 2025 level are consistent with the reported 16.9% growth.
- corroborating: ['p21', 'p22'] Same count of markets with record August 2025 arrivals, one with the market list.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] All from the same kankokeizai.com article describing 2026 January–May inbound trends: weak China, strong non-China, China share collapse. They share one underlying analysis.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41'] All from the same China Daily article on the China–Japan travel slump in late 2025/early 2026.
- corroborating: ['p24', 'p25', 'p26'] Same JTB booking-platform release for Jan–Apr 2026; Taiwan and Korea strong, China weak.
- conflicting: ['p1', 'p29'] June 2026 JNTO estimate shows a 6.8% YoY decline, while the January–May 2026 average was only 1.1% below 2025. This suggests a deteriorating trend into mid-2026, likely driven by the China collapse.
- conflicting: ['p5', 'p29'] August 2025 grew 16.9% YoY, but 2026 has shifted to flat-to-negative overall growth because of the China market slump. A simple carry-forward of August 2025 growth would be misleading.
- corroborating: ['p30', 'p31', 'p32'] China down 45–61% while non-China up 14.1% on average; together they explain the near-flat overall 2026 trend.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p12', 'p49'] Identical JNTO June 2026 estimate (3,148,600) repeated across snapshots; one underlying measurement, not independent confirmation.
- corroborating: ['p2', 'p13', 'p50'] Same June 2026 YoY decline (-6.8%) from the same JNTO release; redundant copies.
- corroborating: ['p3', 'p14', 'p51'] Same H1 2026 cumulative (21,084,800) from the same JNTO release; redundant copies.
- corroborating: ['p4', 'p15', 'p52'] Same count of 15 markets at June record; same JNTO release, redundant copies.
- corroborating: ['p5', 'p18', 'p19', 'p23', 'p27', 'p42'] All report August 2025 arrivals 3,428,000 and +16.9% YoY; same JNTO estimate via different outlets, not independent.
- corroborating: ['p6', 'p43'] Same +58.9% vs August 2023; redundant.
- corroborating: ['p7', 'p44'] Same China August 2025 +36.5%; redundant.
- corroborating: ['p8', 'p45'] Same South Korea August 2025 +8%; redundant.
- corroborating: ['p9', 'p46'] Same Taiwan August 2025 +10%; redundant.
- corroborating: ['p10', 'p47'] Same Hong Kong August 2025 -8.3%; redundant.
- corroborating: ['p11', 'p48'] Same US August 2025 +11.7%; redundant.
- corroborating: ['p21', 'p22'] Same 18 markets at August record; p22 adds the market list, same JNTO release.
- corroborating: ['p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] Same kankokeizai analysis of JNTO data: Jan-May 2026 total -1.1%, China -45.2% to -60.7%, ex-China +14.1%, China share 9.6% vs 30% in 2019. Internally consistent decomposition.
- corroborating: ['p16', 'p17', 'p37', 'p38', 'p39', 'p40', 'p41'] Independent Chinese-side evidence of the China collapse: April new entrants -57%, Jan-Feb study entrants -30%, January flight cancellations 47.2%, December 2025 Chinese travelers -40% YoY. Different m
- corroborating: ['p24', 'p25', 'p26'] JTB booking indices show Taiwan +161%, Korea +138%, China 50% of prior year, Hong Kong 90% — consistent with JNTO market mix (ex-China strong, China weak).
- corroborating: ['p53', 'p54'] April 2026 JNTO estimate 3,692,200, -5.5% YoY; consistent with the June decline and the H1 total.
- corroborating: ['p55', 'p56', 'p57'] May 2026 market breakdown (Korea 951,300; Taiwan 616,800; US 333,700) consistent with ex-China strength and China weakness.
- corroborating: ['p20', 'p18'] August 2024 2,933,381 and August 2025 3,428,000 imply +16.9%, matching p19/p23.
- corroborating: ['p28'] Jan-Aug 2025 cumulative 28,383,600, +18.2% — consistent with the 2025 monthly levels.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY change factor vs August 2025 | 0.95 | 0.88..1.02 | 0.8474..1.059 (widened) | ratio | m1 (m1) | June 2026 was -6.8% YoY (p2) and April -5.5% (p54), while ex-China markets grew +14.1% (p32) and China fell 45-61% (p30). August 2025 was an exceptionally strong base (+16.9%, p18). A modest further decline is the central case, with wide uncertainty because July 2026 JNTO data are not yet available. | The recent negative YoY trend persists into August 2026 and no major new shock or recovery occurs. | July 2026 JNTO data showing a return to positive YoY growth, or evidence of a sharp China recovery or new travel restriction. |
| a2 | August share of annual foreign visitor arrivals | 0.095 | 0.085..0.105 | 0.0668..0.1336 (widened) | share | unused | August is a peak summer month; in recent years August has accounted for roughly 9-10% of annual arrivals. Used to convert an annual 2026 level into an August level. | The seasonal pattern of 2026 resembles recent years and no unusual event shifts summer travel. | Evidence that August 2026 seasonality is materially different, e.g., a major holiday shift or capacity constraint. |
| a4 | August 2026 YoY change factor vs August 2025 (ex-China route) | 0.95 | 0.88..1.02 | 0.8474..1.059 (widened) | ratio | unused | Same as a1 but used in the ex-China decomposition; ex-China markets grew +14.1% in Jan-May 2026 (p32) but the August 2025 base was very strong. | Ex-China growth remains positive but moderates, and China remains weak. | Evidence of a sharp change in ex-China demand or a China recovery. |
| a5 | China share of August 2026 arrivals | 0.1 | 0.07..0.13 | 0.06745..0.1349 (widened) | share | unused | China share fell to 9.6% in Jan-May 2026 (p36) from 30% in 2019 (p35); August 2025 China share was about 30% of the total, so a continued low share is assumed. | The China travel slump persists through August 2026. | Evidence of a significant recovery in Chinese travel to Japan. |

Rejected by code:

- a3 2026 full-year foreign visitor arrivals: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,246,694 | ['p18'] / ['a1'] | [] |  | 1.00 | equal |  |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a3: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |
| m3 | formula_mc | n/a | ['p18', 'p36'] / ['a4', 'a5'] | [] |  | 0.00 |  | formula median is not positive |

Result: central **3,246,694**, 80% interval [2,356,670, 4,472,848], basis no_basis, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for foreign visitor arrivals to Japan in August 2026, as JNTO would first report it, is 3,246,694 persons. This counts foreign-national arrivals for any purpose during 2026-[n]-[n] to 2026-[n]-[n], not unique visitors. The supplied interval is 2,356,670 to 4,472,848 at the 80% level, no basis; it is model-based and conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate rests on one method (100% weight) that scales the observed August 2025 JNTO figure by an assumed year-over-year factor of 0.95 (range 0.8474 to 1.059). That factor is an assumption, not observed: it reflects the recent negative trend and the strong [n] base. Other routes were rejected or unusable.

The main risk is that July 2026 JNTO data are unavailable, so the China drag's persistence is unverified. The most valuable missing evidence would be the July 2026 JNTO release.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 YoY change factor vs August 2025: 0.95 ratio, range 0.8474 to 1.059 (range widened by code); used by m1. Overturned by: July 2026 JNTO data showing a return to positive YoY growth, or evidence of a sharp China recovery or new travel restriction.

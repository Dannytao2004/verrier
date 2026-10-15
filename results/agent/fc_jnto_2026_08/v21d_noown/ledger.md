# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) for the calendar month of August 2026. This is a count of visits (arrivals), not unique individuals, based on JNTO's monthly estimates derived from Ministry of  | unit visits (arrivals) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [related_series] Ministry of Justice (MOJ) immigration statistics

Hypothesis: JNTO estimates are based on MOJ immigration data. The number of foreign nationals entering Japan in August 2026 can be approximated from MOJ's monthly immigration statistics, which may be published with a similar lag. The ratio of JNTO arrivals to MOJ entries is typically close to 1, but adjustments may exist.

Queries issued by the searcher: Ministry of Justice Japan immigration statistics monthly 2026 出入国在留管理庁 月別 外国人入国者数; JNTO 訪日外国人旅行者数 2025年8月 推計値; Japan visitor arrivals August 2025 JNTO record foreign visitors; 出入国在留管理庁 外国人入国者数 月別 2025 統計

- `https://www.jnto.go.jp/statistics/data/_files/20260916_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `http://mediachina.jp/info/6762696` -> **snapshot** (snapshot 20260618075922); points raw/verified 15/4
  - p1 Year-on-year change in new entrants from China (mainland), April 2026 vs April 2 = **57** percent (decline) (2026-04-01..2026-04-30) [keep: ] quote: "前年の4月は61万1千人余りで、57%のマイナスとなっている。"
  - p2 Year-on-year change in cumulative new entrants from China (mainland), Jan–Apr 20 = **57** percent (decline) (2026-01-01..2026-04-30) [keep: ] quote: "昨年同時期(約247万6千人)との比較では、同様に57%(約141万6千人)減で推移する。"
  - p3 New entrants to Japan from China (mainland) for study (ryugaku), January–Februar = **390** people (new entrants for study) (2026-01-01..2026-02-28) [keep: ] quote: "これに先立って判明した1-2月における中国からの「留学」新規来日者数は390人で、前年比では2か月連続で3割程度のマイナスとなっている。"
  - p4 Year-on-year change in new entrants from China (mainland) for study, Jan–Feb 202 = **3** percent (decline, approximate) (2026-01-01..2026-02-28) [keep: ] quote: "前年比では2か月連続で3割程度のマイナスとなっている。"
- `https://www.e-stat.go.jp/index.php/stat-search/files?cycle=1&layout=dataset&month=12040604&tclass1=000001012482&toukei=00250011&tstat=000001012480&yea` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (number: more than one number in value_as_written: 10; number: unknown scale word '万': 1)

### d2 [forecasts_markets] Industry forecasts and government targets

Hypothesis: Published forecasts for Japan's inbound tourism in 2026, such as from the Japan Tourism Agency, travel agencies, or economic research institutes, may provide a projected annual figure or monthly growth rates. These can be used to infer August 2026 arrivals if monthly seasonality is known.

Queries issued by the searcher: Japan inbound tourism forecast 2026 visitor arrivals projection; 訪日外国人旅行者数 予測 2026; JNTO 訪日外客数 2026年7月 月別 推計値; 訪日外客数 2025年8月 342万人 JNTO 月別

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jtbcorp.jp/jp/newsroom/2026/01/08_jtb_inbound_outlook.html` -> **snapshot** (snapshot 20260510055357); points raw/verified 15/4
  - p5 JAPANiCAN.com booking count growth for Taiwan, Jan-Apr 2026 vs prior year = **161** % (2026-01-01..2026-04-30) [keep: ] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p6 JAPANiCAN.com booking count growth for South Korea, Jan-Apr 2026 vs prior year = **138** % (2026-01-01..2026-04-30) [keep: ] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p7 JAPANiCAN.com booking count growth for China, Jan-Apr 2026 vs prior year = **50** % (2026-01-01..2026-04-30) [keep: ] quote: "一方、日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています"
  - p8 JAPANiCAN.com booking count growth for Hong Kong, Jan-Apr 2026 vs prior year = **90** % (2026-01-01..2026-04-30) [keep: ] quote: "一方、日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています"
- `https://www.dir.co.jp/english/research/report/analysis/20260413_025695.html` -> **snapshot** (snapshot 20260520165358); points raw/verified 0/0
- dropped by code checks: 11 (number: unknown scale word '万人': 1; period_end 2026-12-31 after as_of: 6; number: unknown scale word '兆円': 1; number: unknown scale word '万人泊': 3)

### d3 [base_rates] Seasonality and source market mix

Hypothesis: August is typically a peak month for inbound tourism in Japan due to summer holidays. The seasonal factor (August arrivals relative to annual average) can be applied to an annual estimate. Additionally, the mix of source countries (e.g., South Korea, China, Taiwan) affects growth rates; using recent growth by market can refine the estimate.

Queries issued by the searcher: Japan inbound tourism seasonality August monthly arrivals JNTO; 訪日外国人 月別 2025年 8月 JNTO 推計値; JNTO 訪日外客数 2026年7月推計値 344万人 年間; JNTO 訪日外客統計 月別推計値 2025年 月別 一覧 8月 3,428,000

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://yamatogokoro.jp/inbound_data/58034/` -> **snapshot** (snapshot 20260515113739); points raw/verified 15/5
  - p9 Year-on-year growth rate of total foreign visitor arrivals to Japan, August 2025 = **16.9** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "前年同月(2024年8月)の293万3381人を49万人上回り、16.9%増となった。"
  - p10 Year-on-year growth rate of foreign visitor arrivals to Japan from China, August = **36.5** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "東アジア市場では中国が最多の101万8600人(前年同月比36.5%増)となり、大きく増加した。"
  - p11 Year-on-year growth rate of foreign visitor arrivals to Japan from South Korea,  = **8** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "7月は前年比約10%減だった韓国も、66万900人(同8.0%増)と回復し、8月として過去最高を更新。"
  - p12 Year-on-year growth rate of foreign visitor arrivals to Japan from Taiwan, Augus = **10** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "台湾は62万700人(同10.0%増)で、単月として過去最高となった。"
  - p13 Year-on-year growth rate of foreign visitor arrivals to Japan from USA, August 2 = **11.7** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "アメリカは19万4500人(前年同月比11.7%増)で引き続き堅調に推移。"
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (number: more than one number in value_as_written: 10)

### d4 [physical_flow] Airport and seaport passenger traffic

Hypothesis: Foreign visitor arrivals are a subset of total international passenger arrivals at Japanese airports and seaports. By estimating total international arrivals in August 2026 and applying the historical share of foreign visitors, we can derive the target. This route requires data on flight schedules, seat capacity, and load factors.

Queries issued by the searcher: Narita airport international passenger traffic 2026; JNTO foreign visitor arrivals Japan monthly 2026 August; 訪日外客数 2026年7月推計値 JNTO 8月発表; 関西空港 国際線 外国人旅客数 2026年; 羽田空港 国際線 旅客数 2026年 速報

- `https://www.narita-airport.jp/files/2d726be7151e64dc9242dd4ca604eccc2fb5067335bacbf53e2f33e8b97b3c76` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://travelmole.com/news/tokyo-narita-returns-in-favor` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aci-asiapac.aero/media-centre/news/narita-airport-passenger-estimates-for-the-2026-summer-peak-period` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aviationwire.jp/archives/349551` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [capacity_consumption] Hotel occupancy and accommodation statistics

Hypothesis: Foreign visitor arrivals correlate with hotel stays by inbound tourists. The number of foreign guests staying in Japanese hotels in August 2026 can be estimated from occupancy rates and room supply, then converted to arrivals using average length of stay and party size. This route provides an independent check.

Queries issued by the searcher: 宿泊旅行統計調査 外国人延べ宿泊者数 2026年; Japan hotel occupancy rate foreign guests 2026 Japan Tourism Agency accommodation statistics; JNTO 訪日外国人旅行者数 2026年6月 推計 発表; 訪日外国人 平均泊数 2026 消費動向調査 平均滞在日数

- `https://www.mlit.go.jp/kankocho/news02_00098.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mlit.go.jp/kankocho/news02_00084.html` -> **snapshot** (snapshot 20260514130124); points raw/verified 8/2
  - p14 Room occupancy rate (all), February 2026 = **59.6** % (2026-02-01..2026-02-28) [keep: ] quote: "2026年2月の客室稼働率は全体で59.6%であった。"
  - p15 Room occupancy rate (all), March 2026 = **60.3** % (2026-03-01..2026-03-31) [keep: ] quote: "また、2026年3月は全体で60.3%であった。"
- `https://www.mlit.go.jp/kankocho/content/002010558.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://wwwtb.mlit.go.jp/shikoku/content/000377115.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 6 (number: unknown scale word '万人泊': 6)

### d6 [shocks] Event and policy calendar

Hypothesis: Major events, holidays, or policy changes in August 2026 could affect visitor arrivals. For example, the Obon holiday, international sporting events, visa policy changes, or travel advisories. Identifying such factors helps adjust the estimate from historical patterns.

Queries issued by the searcher: JNTO foreign visitor arrivals August 2025 monthly estimate; Japan visa policy changes 2026 China South Korea Taiwan travel; JNTO 訪日外客数 2026年6月 推計値 前年同月比; 訪日外客数 2026年7月 推計値 JNTO

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 6/5
  - p16 Japan inbound foreign visitor arrivals, June 2026 monthly estimate (JNTO) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p17 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p18 Japan inbound foreign visitor arrivals, first-half 2026 cumulative total (JNTO) = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p19 Number of markets recording record-high June inbound foreign visitor arrivals to = **15** markets (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
  - p20 Date of formulation of the 5th Tourism Nation Promotion Basic Plan = **2,026** year (2026-03-01..2026-03-31) [DISCARD: Date of formulation of a tourism plan (2026) is not a quantity relevant to estimating August 2026 arrivals; no usable nu] quote: "2026年3月に策定された第5次観光立国推進基本計画では"
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.asiae.co.kr/lang/print.htm?idxno=2026062508475936012&lang=en` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/8
  - p21 Japan inbound foreign visitor arrivals, June 2026 vs June 2025, year-on-year cha = **6.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p22 Japan inbound foreign visitor arrivals, cumulative January-June 2026 vs same per = **2** percent (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p23 Japan inbound visitor arrivals from South Korea, June 2026 vs 2025, year-on-year = **7.8** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p24 Japan inbound visitor arrivals from Taiwan, June 2026 vs 2025, year-on-year chan = **14.6** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "台湾が67万400人(同14.6%増)"
  - p25 Japan inbound visitor arrivals from United States, June 2026 vs 2025, year-on-ye = **2.7** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "米国が35万4500人(同2.7%増)"
  - p26 Japan inbound visitor arrivals from China, June 2026 vs 2025, year-on-year chang = **57.3** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "中国が34万700人(同57.3%減)"
  - p27 Japan inbound visitor arrivals from Hong Kong, June 2026 vs 2025, year-on-year c = **28.5** percent (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "香港が21万4300人(同28.5%増)"
  - p28 Number of markets setting record-high June arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- dropped by code checks: 8 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 7)

### d7 [administrative] Visa issuance and travel agency bookings

Hypothesis: The number of visas issued to foreign nationals in the months leading up to August 2026 can indicate travel intentions. Similarly, forward bookings from major travel agencies or online travel platforms can provide a leading indicator of arrivals.

Queries issued by the searcher: JNTO 訪日外客数 2026年 月別 推計; Japan inbound visitor arrivals 2026 monthly JNTO estimate; Japan visa issuance statistics 2026 monthly 外務省 査証発給統計; 訪日旅行 予約動向 2026年夏 旅行社 予約状況

- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jwing.net/news/111949` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/tourism-statistics/inbound-travel-statistics/` -> **snapshot** (snapshot 20260731002019); points raw/verified 5/5
  - p29 Foreign visitors to Japan, total, April 2026 (JNTO estimate) = **3,692,200** visits (arrivals) (2026-04-01..2026-04-30) [EXCLUDED (ablation): ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p30 Year-on-year change in foreign visitors to Japan, April 2026 = **5.5** % (2026-04-01..2026-04-30) [EXCLUDED (ablation): ] quote: "Foreign visitors to Japan totaled 3,692,200 in April 2026, down 5.5% year on year (JNTO estimate)."
  - p31 Foreign visitors to Japan from South Korea, May 2026 = **951,300** visits (arrivals) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p32 Foreign visitors to Japan from Taiwan, May 2026 = **616,800** visits (arrivals) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
  - p33 Foreign visitors to Japan from the United States, May 2026 = **333,700** visits (arrivals) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "South Korea ranked first with 951,300 visitors, followed by Taiwan with 616,800 visitors, and the United States with 333,700 visitors."
- `https://www.mofa.go.jp/mofaj/toko/tokei/hakkyu/index.html` -> **snapshot** (snapshot 20260115113717); points raw/verified 0/0

### b1 [related_series] administrative

Hypothesis: JNTO's monthly estimate for August 2026 will be published in mid-September 2026. If a preliminary or leaked figure, or a closely related MOJ immigration count for August 2026, becomes available before the cutoff, it would directly anchor the target and eliminate the need for a forecast. This is the single most valuable missing input.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan August 2026; Japan National Tourism Organization monthly inbound visitors 2026 estimate; 訪日外客数 2026年7月推計値 344万人 8月19日発表; 出入国管理統計 2026年 外国人入国者数 月別 法務省

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p34 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** visits (arrivals) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p35 Year-on-year change in foreign visitor arrivals to Japan, June 2026 = **6.8** percent (year-on-year change) (2026-06-01..2026-06-30) [EXCLUDED (ablation): ] quote: "6月:前年同月比6.8%減の315万人"
  - p36 Cumulative foreign visitor arrivals to Japan, first half of 2026 (January-June) = **21,084,800** visits (arrivals) (2026-01-01..2026-06-30) [EXCLUDED (ablation): ] quote: "また、上半期の累計で21,084,800人となった。"
  - p37 Number of markets recording their highest-ever June foreign visitor arrivals, Ju = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.travelvoice.jp/english/international-arrivals-in-japan-in-august-2026-were-down-9-6-to-3-1-million-despite-record-high-in-14-source-market` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: unknown scale word '万': 1)

### b2 [base_rates] historical

Hypothesis: A reliable August seasonal factor (August arrivals divided by the annual monthly average) for recent years would allow an annual 2026 forecast to be converted into an August 2026 level. Without this factor, any annual forecast cannot be transferred to the target month.

Queries issued by the searcher: JNTO monthly foreign visitor arrivals August 2025 annual total; Japan inbound tourism monthly arrivals 2024 August record JNTO statistics; JNTO 訪日外客数 月別推計値 2023年 年間 2506万人 2024年 3687万人; 訪日外客数 2025年 年間 推移 月別 1月 2月 3月 4月 5月 6月 7月 8月 9月

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/news/_files/20250115_1615.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://travelvision.jp/news/detail/news-109256` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] industry

Hypothesis: Published 2026 inbound tourism forecasts (annual or monthly) from the Japan Tourism Agency, JTB, or economic research institutes would provide a growth-rate anchor. Combined with a seasonal factor, this would yield a credible August 2026 estimate. The current evidence lacks any explicit 2026 annual or monthly forecast level.

Queries issued by the searcher: JNTO 2026 inbound tourism forecast Japan visitor arrivals; JTB 2026年 訪日外国人旅行者数 予測 見通し; JNTO 2025年8月 訪日外客数 推計値 前年同月比; JNTO 2026年6月 訪日外客数 推計値 統計

- `https://www.jtbcorp.jp/jp/newsroom/2026/01/08_jtb_inbound_outlook.html` -> **snapshot** (snapshot 20260510055357); points raw/verified 15/4
  - p38 JAPANiCAN.com booking count change for Taiwan visitors, Jan-Apr 2026 vs same per = **161** % (2026-01-01..2026-04-30) [DISCARD: Redundant duplicate of p5; same Taiwan booking growth figure from the same source and period.] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p39 JAPANiCAN.com booking count change for South Korea visitors, Jan-Apr 2026 vs sam = **138** % (2026-01-01..2026-04-30) [DISCARD: Redundant duplicate of p6; same South Korea booking growth figure.] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています"
  - p40 JAPANiCAN.com booking count change for China visitors, Jan-Apr 2026 vs same peri = **50** % (2026-01-01..2026-04-30) [DISCARD: Redundant duplicate of p7; same China booking growth figure.] quote: "一方、日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています"
  - p41 JAPANiCAN.com booking count change for Hong Kong visitors, Jan-Apr 2026 vs same  = **90** % (2026-01-01..2026-04-30) [DISCARD: Redundant duplicate of p8; same Hong Kong booking growth figure.] quote: "一方、日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています"
- `https://www.tourism.jp/en/tourism-statistics/` -> **snapshot** (snapshot 20260815090947); points raw/verified 6/4
  - p42 Foreign visitors to Japan, May 2026 estimated figures (JTB Tourism Research & Co = **3,559,900** visits (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "May 2026: Estimated figures3,559,900 visits"
  - p43 Foreign visitors to Japan, May 2026 year-on-year change = **-3.6** percent (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "May 2026: Estimated figures3,559,900 visitsYOY-3.6%"
  - p44 Japanese travelers abroad, May 2026 estimated figures = **1,127,432** visits (2026-05-01..2026-05-31) [DISCARD: Japanese travelers abroad is outbound tourism, not foreign visitor arrivals to Japan; different population and direction] quote: "May 2026: Estimated figures1,127,432 visits"
  - p45 Japanese travelers abroad, May 2026 year-on-year change = **4.7** percent (2026-05-01..2026-05-31) [DISCARD: Year-on-year change for Japanese outbound travel; not applicable to inbound foreign visitor arrivals.] quote: "May 2026: Estimated figures1,127,432 visitsYOY+4.7%"
- `https://www.travelvoice.jp/20250917-158383` -> **snapshot** (snapshot 20260608084226); points raw/verified 16/8
  - p46 Japan inbound foreign visitor arrivals, August 2025 vs August 2024, year-on-year = **16.9** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2025年8月の訪日外国人旅行者数(推計値)は前年比16.9%増の342万8000人となり、8月として初めて300万人を超えた。"
  - p47 Japan inbound foreign visitor arrivals, August 2025 vs August 2023, growth rate = **58.9** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "2023年8月(実数:215万7190人)比では、58.9%増。"
  - p48 Japan inbound visitor arrivals from China, August 2025 vs August 2024, year-on-y = **36.5** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p49 Japan inbound visitor arrivals from South Korea, August 2025 vs August 2024, yea = **8** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p50 Japan inbound visitor arrivals from Taiwan, August 2025 vs August 2024, year-on- = **10** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p51 Japan inbound visitor arrivals from Hong Kong, August 2025 vs August 2024, year- = **8.3** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p52 Japan inbound visitor arrivals from United States, August 2025 vs August 2024, y = **11.7** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)、香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p53 Japan inbound visitor arrivals from Singapore, August 2025 vs August 2024, year- = **17.3** percent (2025-08-01..2025-08-31) [EXCLUDED (ablation): ] quote: "一方、シンガポールは2万500人(同17.3%減)で唯一、前年比2ケタ減となった。"
- `https://www.apir.or.jp/uploads/research/【26年6月】観光レポート_2026-08-18.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 21 (number: unknown scale word '万人': 1; period_end 2026-12-31 after as_of: 6; number: unknown scale word '兆円': 1; number: unknown scale word '万人泊': 3; value_as_written not in quote as a whole number: 2; number: more than one number in value_as_written: 8)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'inbound arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Both describe the same underlying phenomenon: a severe (~57%) year-on-year decline in new entrants from mainland China in early 2026. p1 is the April monthly figure; p2 is the Jan–Apr cumulative figur
- corroborating: ['p3', 'p4'] p3 gives the level of study-related new entrants from China in Jan–Feb 2026 (390 people); p4 gives the approximate year-on-year decline (~30%). They are consistent with each other and with the broader
- corroborating: ['p5', 'p6', 'p7', 'p8'] These are four market-level booking growth rates from the same JAPANiCAN.com source for Jan–Apr 2026. They are not independent of each other (same platform, same period), but together they show a clea
- corroborating: ['p14', 'p15'] Both are monthly all-room occupancy rates from the same MLIT source (Feb 2026: 59.6%; Mar 2026: 60.3%). They are not independent observations of the target, but they establish a recent, modestly risin
- contextual: ['p28'] p28 reports that 15 markets set record-high June 2026 arrivals. This is a broad, positive signal for inbound tourism in mid-2026, but it does not directly quantify August 2026 arrivals and is not a su
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2'] Both report the same ~57% year-on-year decline in new entrants from mainland China in early 2026 (April and Jan–Apr cumulative), consistent with a sustained China-market contraction.
- corroborating: ['p3', 'p4'] Both describe a sharp drop in Chinese student new entrants in Jan–Feb 2026; p3 gives the level (390) and p4 the approximate ~30% decline, same underlying phenomenon.
- corroborating: ['p5', 'p6', 'p7', 'p8'] JTB JAPANiCAN booking growth for Taiwan, South Korea, China, and Hong Kong in Jan–Apr 2026; same source and period, showing strong Taiwan/Korea and weak China/Hong Kong demand.
- redundant: ['p5', 'p38'] p38 is a duplicate of p5 (same Taiwan booking growth figure, same source and period).
- redundant: ['p6', 'p39'] p39 duplicates p6 (South Korea booking growth).
- redundant: ['p7', 'p40'] p40 duplicates p7 (China booking growth).
- redundant: ['p8', 'p41'] p41 duplicates p8 (Hong Kong booking growth).
- corroborating: ['p28', 'p37'] Both report 15 markets setting record-high June 2026 arrivals; same JNTO-based statistic from different outlets.
- corroborating: ['p14', 'p15'] Hotel room occupancy rates for Feb and Mar 2026 (59.6% and 60.3%) from the same MLIT series, showing stable but not exceptional occupancy.
- corroborating: ['p1', 'p7'] Independent sources (mediachina.jp immigration data and JTB booking data) both indicate a severe contraction in Chinese travel to Japan in early 2026.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a2 | August 2026 foreign visitor arrivals relative to August 2025 | 1 | 0.85..1.15 | 0.6991..1.398 (widened) | ratio | unused | Early-2026 evidence shows strong Taiwan/Korea booking growth (p5, p6) but a severe China contraction (p1, p2, p7). China is a large source market, so the net effect on total arrivals is highly uncertain. A central ratio of 1.0 with a wide range reflects offsetting market trends and the absence of a  | Used to scale August 2025 JNTO arrivals to August 2026; assumes the market mix and policy environment in August 2026 are broadly similar to early 2026 with no major new shocks. | Evidence of a large new visa policy, travel advisory, or economic shock affecting Japan inbound travel in mid-2026, or a published JNTO/MOJ figure for August 2026 showing a change outside the range. |

Rejected by code:

- a1 August 2025 JNTO foreign visitor arrivals: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['japan']; quantity stems: ['arriv', 'visit']
- points excluded before the judge: 34 of 53
- methods allowed: ['formula_mc']

  - p9 Year-on-year growth rate of total foreign visitor arrivals to Japan, August 2025 vs August = 16.9 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p10 Year-on-year growth rate of foreign visitor arrivals to Japan from China, August 2025 = 36.5 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p11 Year-on-year growth rate of foreign visitor arrivals to Japan from South Korea, August 202 = 8 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p12 Year-on-year growth rate of foreign visitor arrivals to Japan from Taiwan, August 2025 = 10 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p13 Year-on-year growth rate of foreign visitor arrivals to Japan from USA, August 2025 = 11.7 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p16 Japan inbound foreign visitor arrivals, June 2026 monthly estimate (JNTO) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p17 Year-on-year change in Japan inbound foreign visitor arrivals, June 2026 vs June 2025 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p18 Japan inbound foreign visitor arrivals, first-half 2026 cumulative total (JNTO) = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p19 Number of markets recording record-high June inbound foreign visitor arrivals to Japan, Ju = 15 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p21 Japan inbound foreign visitor arrivals, June 2026 vs June 2025, year-on-year change = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p22 Japan inbound foreign visitor arrivals, cumulative January-June 2026 vs same period 2025,  = 2 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p23 Japan inbound visitor arrivals from South Korea, June 2026 vs 2025, year-on-year change = 7.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p24 Japan inbound visitor arrivals from Taiwan, June 2026 vs 2025, year-on-year change = 14.6 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p25 Japan inbound visitor arrivals from United States, June 2026 vs 2025, year-on-year change = 2.7 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p26 Japan inbound visitor arrivals from China, June 2026 vs 2025, year-on-year change = 57.3 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p27 Japan inbound visitor arrivals from Hong Kong, June 2026 vs 2025, year-on-year change = 28.5 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p29 Foreign visitors to Japan, total, April 2026 (JNTO estimate) = 3,692,200 (2026-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p30 Year-on-year change in foreign visitors to Japan, April 2026 = 5.5 (2026-04-30): ablation: name refers to the target entity ['japan'] and quantity
  - p31 Foreign visitors to Japan from South Korea, May 2026 = 951,300 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p32 Foreign visitors to Japan from Taiwan, May 2026 = 616,800 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p33 Foreign visitors to Japan from the United States, May 2026 = 333,700 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p34 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = 3,148,600 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p35 Year-on-year change in foreign visitor arrivals to Japan, June 2026 = 6.8 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p36 Cumulative foreign visitor arrivals to Japan, first half of 2026 (January-June) = 21,084,800 (2026-06-30): ablation: name refers to the target entity ['japan'] and quantity
  - p42 Foreign visitors to Japan, May 2026 estimated figures (JTB Tourism Research & Consulting) = 3,559,900 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p43 Foreign visitors to Japan, May 2026 year-on-year change = -3.6 (2026-05-31): ablation: name refers to the target entity ['japan'] and quantity
  - p46 Japan inbound foreign visitor arrivals, August 2025 vs August 2024, year-on-year growth ra = 16.9 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p47 Japan inbound foreign visitor arrivals, August 2025 vs August 2023, growth rate = 58.9 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p48 Japan inbound visitor arrivals from China, August 2025 vs August 2024, year-on-year growth = 36.5 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p49 Japan inbound visitor arrivals from South Korea, August 2025 vs August 2024, year-on-year  = 8 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p50 Japan inbound visitor arrivals from Taiwan, August 2025 vs August 2024, year-on-year growt = 10 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p51 Japan inbound visitor arrivals from Hong Kong, August 2025 vs August 2024, year-on-year gr = 8.3 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p52 Japan inbound visitor arrivals from United States, August 2025 vs August 2024, year-on-yea = 11.7 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity
  - p53 Japan inbound visitor arrivals from Singapore, August 2025 vs August 2024, year-on-year gr = 17.3 (2025-08-31): ablation: name refers to the target entity ['japan'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a1: assumption a1 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

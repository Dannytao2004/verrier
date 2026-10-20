# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Preliminary JNTO monthly estimate of foreign visitor arrivals to Japan for August 2026: foreign nationals entering Japan during 1–31 August 2026, counted as visitor arrivals/entries in the headline JNTO series, not unique persons and not Japanese nationals. | unit foreign visitor arrivals | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [own_history] JNTO monthly statistics analyst

Hypothesis: August 2026 can be projected from JNTO's own history: August 2025 level multiplied by recent year-on-year growth in Jan–Jul 2026, adjusted for calendar/Obon timing and market mix. Role: central baseline and seasonal shape. Expected direction: if 2026 YTD growth remains positive, August 2026 exceeds August 2025.

Queries issued by the searcher: JNTO foreign visitors monthly August 2025 record 3.4 million; JNTO 2026年6月 訪日外国人 推計 月別; 訪日外客数 月別 推移 2019年8月 2,520,100 2023年8月 2024年8月 2,933,381; 2026年7月 訪日外国人 予測 夏休み 中国 減少 8月 見通し

- `https://www.travelvision.jp/news/detail/news-123348` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://n-seikei.jp/2025/09/post-113165.html` -> **snapshot** (snapshot 20260114185540); points raw/verified 14/14
  - p1 JNTO total foreign visitor arrivals, August 2025 (headline) = **3,428,000** foreign visitor arrivals (2025-08-01..2025-08-31) [DISCARD: Duplicate of p33: same August 2025 JNTO headline total of 3,428,000.] quote: "\| 総数 \| 3,428,000 \| 16.9% \| 100.0% \| 28,383,600 \| 18.2% \| 100.0% \|"
  - p2 JNTO total foreign visitor arrivals, August 2025 YoY change = **16.9** % (2025-08-01..2025-08-31) [DISCARD: Duplicate YoY for the same August 2025 headline already captured by p33; adds no separate information.] quote: "8月の訪日外客数は前年同月比では16.9%増の3,428,000人となった。"
  - p3 JNTO total foreign visitor arrivals, August 2024 = **2,933,381** foreign visitor arrivals (2024-08-01..2024-08-31) [keep: ] quote: "\| 8月 \| 2,520,134 \| 2,157,190 \| 2,933,381 \| 3,428,000 \| 16.9% \|"
  - p4 JNTO total foreign visitor arrivals, August 2023 = **2,157,190** foreign visitor arrivals (2023-08-01..2023-08-31) [keep: ] quote: "\| 8月 \| 2,520,134 \| 2,157,190 \| 2,933,381 \| 3,428,000 \| 16.9% \|"
  - p5 JNTO total foreign visitor arrivals, August 2019 = **2,520,134** foreign visitor arrivals (2019-08-01..2019-08-31) [keep: ] quote: "\| 8月 \| 2,520,134 \| 2,157,190 \| 2,933,381 \| 3,428,000 \| 16.9% \|"
  - p6 JNTO total foreign visitor arrivals, January 2025 = **3,781,629** foreign visitor arrivals (2025-01-01..2025-01-31) [DISCARD: n-seikei duplicate of JNTO January 2025 p27; prefer the JNTO preliminary series.] quote: "\| 1月 \| 2,689,339 \| 1,497,472 \| 2,688,478 \| 3,781,629 \| 40.7% \|"
  - p7 JNTO total foreign visitor arrivals, February 2025 = **3,258,491** foreign visitor arrivals (2025-02-01..2025-02-28) [DISCARD: n-seikei duplicate of JNTO February 2025 p28; prefer the JNTO preliminary series.] quote: "\| 2月 \| 2,604,322 \| 1,475,455 \| 2,788,224 \| 3,258,491 \| 16.9% \|"
  - p8 JNTO total foreign visitor arrivals, March 2025 = **3,497,755** foreign visitor arrivals (2025-03-01..2025-03-31) [DISCARD: n-seikei duplicate of JNTO March 2025 p29; prefer the JNTO preliminary series.] quote: "\| 3月 \| 2,760,136 \| 1,817,616 \| 3,081,781 \| 3,497,755 \| 13.5% \|"
  - p9 JNTO total foreign visitor arrivals, April 2025 = **3,909,128** foreign visitor arrivals (2025-04-01..2025-04-30) [DISCARD: n-seikei duplicate of JNTO April 2025 p30; prefer the JNTO preliminary series.] quote: "\| 4月 \| 2,926,685 \| 1,949,236 \| 3,043,003 \| 3,909,128 \| 28.5% \|"
  - p10 JNTO total foreign visitor arrivals, May 2025 = **3,693,300** foreign visitor arrivals (2025-05-01..2025-05-31) [DISCARD: n-seikei duplicate of JNTO May 2025 p31, with minor rounding/vintage differences.] quote: "\| 5月 \| 2,773,091 \| 1,899,176 \| 3,040,294 \| 3,693,300 \| 21.5% \|"
  - p11 JNTO total foreign visitor arrivals, June 2025 = **3,377,800** foreign visitor arrivals (2025-06-01..2025-06-30) [DISCARD: n-seikei duplicate of JNTO June 2025 p26, with minor rounding/vintage differences.] quote: "\| 6月 \| 2,880,041 \| 2,073,441 \| 3,140,642 \| 3,377,800 \| 7.6% \|"
  - p12 JNTO total foreign visitor arrivals, July 2025 = **3,437,000** foreign visitor arrivals (2025-07-01..2025-07-31) [DISCARD: n-seikei duplicate of JNTO July 2025 p24.] quote: "\| 7月 \| 2,991,189 \| 2,320,694 \| 3,292,602 \| 3,437,000 \| 4.4% \|"
  - p13 JNTO total foreign visitor arrivals, January–August 2025 cumulative = **28,383,600** foreign visitor arrivals (2025-01-01..2025-08-31) [DISCARD: Duplicate of p21: same Jan-Aug 2025 cumulative 28,383,600.] quote: "\| 総数 \| 3,428,000 \| 16.9% \| 100.0% \| 28,383,600 \| 18.2% \| 100.0% \|"
  - p14 JNTO total foreign visitor arrivals, January–August 2025 cumulative YoY change = **18.2** % (2025-01-01..2025-08-31) [DISCARD: Duplicate of p23: same Jan-Aug 2025 cumulative YoY change of +18.2%.] quote: "\| 総数 \| 3,428,000 \| 16.9% \| 100.0% \| 28,383,600 \| 18.2% \| 100.0% \|"
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/5
  - p15 JNTO estimated foreign visitor arrivals to Japan, June 2026 (provisional monthly = **3,150,000** foreign visitor arrivals (2026-06-01..2026-06-30) [DISCARD: Rounded duplicate of p62 for June 2026 total; p62 gives the exact 3,148,600 value and is preferred.] quote: "訪日外客数(2026年6月推計値)6月:前年同月比6.8%減の315万人"
  - p16 JNTO foreign visitor arrivals to Japan, June 2026 (detailed count) = **3,148,600** foreign visitor arrivals (2026-06-01..2026-06-30) [DISCARD: Detailed June 2026 count is redundant with p15 preliminary estimate and p17 YoY change for the same month.] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p17 Year-on-year change in foreign visitor arrivals to Japan, June 2026 vs June 2025 = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p63 for June 2026 total YoY change; same JNTO release.] quote: "6月:前年同月比6.8%減の315万人"
  - p18 Cumulative first-half (Jan–Jun) 2026 foreign visitor arrivals to Japan = **21,084,800** foreign visitor arrivals (2026-01-01..2026-06-30) [DISCARD: Duplicate of p64 for H1 2026 cumulative arrivals; same value 21,084,800.] quote: "また、上半期の累計で21,084,800人となった。"
  - p19 Number of markets recording record-high June foreign visitor arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [DISCARD: Duplicate of p76 for the count of June 2026 record-high markets; same JNTO release.] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **snapshot** (snapshot 20260323162238); points raw/verified 15/13
  - p20 JNTO preliminary estimate of total foreign visitor arrivals to Japan, August 202 = **3,428,000** visitor arrivals (persons) (2025-08-01..2025-08-31) [DISCARD: Duplicate of p33: same August 2025 JNTO preliminary estimate of 3,428,000.] quote: "8 月:3,428,000 人、8 月として初の 300 万人超え"
  - p21 Cumulative total foreign visitor arrivals to Japan, January–August 2025 (prelimi = **28,383,600** visitor arrivals (persons) (2025-01-01..2025-08-31) [keep: ] quote: "1~8 24,008,405 28,383,600* 18.2*"
  - p22 Cumulative total foreign visitor arrivals to Japan, January–August 2024 (definit = **24,008,405** visitor arrivals (persons) (2024-01-01..2024-08-31) [DISCARD: Jan-Aug 2024 cumulative is historical context not needed for the August 2026 estimate; p23 already gives the relevant 20] quote: "1~8 24,008,405 28,383,600* 18.2*"
  - p23 Year-on-year change in cumulative total foreign visitor arrivals, January–August = **18.2** % change (2025-01-01..2025-08-31) [keep: ] quote: "1~8 24,008,405 28,383,600* 18.2*"
  - p24 Total foreign visitor arrivals to Japan, July 2025 (preliminary) = **3,437,000** visitor arrivals (persons) (2025-07-01..2025-07-31) [keep: ] quote: "7 3,292,602 3,437,000* 4.4*"
  - p25 Total foreign visitor arrivals to Japan, July 2024 (definitive) = **3,292,602** visitor arrivals (persons) (2024-07-01..2024-07-31) [DISCARD: July 2024 level is not needed for August 2026; July 2025 p24 is the relevant recent July context.] quote: "7 3,292,602 3,437,000* 4.4*"
  - p26 Total foreign visitor arrivals to Japan, June 2025 (preliminary) = **3,377,985** visitor arrivals (persons) (2025-06-01..2025-06-30) [keep: ] quote: "6 3,140,642 3,377,985 7.6"
  - p27 Total foreign visitor arrivals to Japan, January 2025 (preliminary) = **3,781,629** visitor arrivals (persons) (2025-01-01..2025-01-31) [keep: ] quote: "1 2,688,478 3,781,629 40.7"
  - p28 Total foreign visitor arrivals to Japan, February 2025 (preliminary) = **3,258,491** visitor arrivals (persons) (2025-02-01..2025-02-28) [keep: ] quote: "2 2,788,224 3,258,491 16.9"
  - p29 Total foreign visitor arrivals to Japan, March 2025 (preliminary) = **3,497,755** visitor arrivals (persons) (2025-03-01..2025-03-31) [keep: ] quote: "3 3,081,781 3,497,755 13.5"
  - p30 Total foreign visitor arrivals to Japan, April 2025 (preliminary) = **3,909,128** visitor arrivals (persons) (2025-04-01..2025-04-30) [keep: ] quote: "4 3,043,003 3,909,128 28.5"
  - p31 Total foreign visitor arrivals to Japan, May 2025 (preliminary) = **3,693,587** visitor arrivals (persons) (2025-05-01..2025-05-31) [keep: ] quote: "5 3,040,294 3,693,587 21.5"
  - p32 Total foreign visitor arrivals to Japan, full year 2024 (definitive) = **36,870,148** visitor arrivals (persons) (2024-01-01..2024-12-31) [DISCARD: Full-year 2024 total is not needed for an August 2026 monthly estimate.] quote: "1~12 36,870,148 13,007,282"
- dropped by code checks: 2 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### d2 [related_series] JNTO country-market analyst

Hypothesis: Total August 2026 arrivals equal the sum of major source-market arrivals. Use August 2025 market levels/shares and Jan–Jul 2026 market-specific YoY trends, then adjust for market-specific shocks. Role: reduces aggregate growth uncertainty and exposes composition effects among Korea, China, Taiwan, Hong Kong, US and others.

Queries issued by the searcher: JNTO 訪日外国人 国籍別 2025年8月 韓国 中国 台湾; Japan inbound arrivals by country July 2026 JNTO; 訪日外客数 2026年6月 国籍別 韓国 台湾 中国 前年同月比; 中国 訪日 渡航自粛 2026年8月 回復 中国政府 観光 渡航注意

- `https://www.jnto.go.jp/news/_files/20260819_1615.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **snapshot** (snapshot 20260323162238); points raw/verified 15/15
  - p33 Total foreign visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **3,428,000** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "8 月の訪日外客数は 3,428,000 人で、前年同月比では 16.9%増となった。"
  - p34 South Korea visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **660,900** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "韓国 South Korea 612,172 660,900 8.0 5,811,962 6,123,100 5.4"
  - p35 China visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **1,018,600** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "中国 China 746,010 1,018,600 36.5 4,595,386 6,711,600 46.1"
  - p36 Taiwan visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **620,700** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "台湾 Taiwan 564,360 620,700 10.0 4,115,255 4,509,700 9.6"
  - p37 Hong Kong visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **226,100** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "香港 Hong Kong 246,557 226,100 -8.3 1,801,733 1,673,200 -7.1"
  - p38 United States visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **194,500** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "米国 U.S.A. 174,051 194,500 11.7 1,768,204 2,173,000 22.9"
  - p39 Thailand visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **35,500** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "タイ Thailand 34,667 35,500 2.4 706,471 764,600 8.2"
  - p40 Australia visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **41,200** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "豪州 Australia 40,999 41,200 0.5 551,606 658,600 19.4"
  - p41 Singapore visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **20,500** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "シンガポール Singapore 24,781 20,500 -17.3 352,923 390,000 10.5"
  - p42 Philippines visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **44,200** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "フィリピン Philippines 38,971 44,200 13.4 496,204 539,700 8.8"
  - p43 Vietnam visitor arrivals to Japan, August 2025 (JNTO preliminary estimate) = **61,200** visitor arrivals (2025-08-01..2025-08-31) [keep: ] quote: "ベトナム Vietnam 52,430 61,200 16.7 434,061 479,300 10.4"
  - p44 South Korea visitor arrivals to Japan, January–August 2025 cumulative (JNTO prel = **6,123,100** visitor arrivals (2025-01-01..2025-08-31) [DISCARD: Cumulative Jan-Aug 2025 Korea total is redundant for the August 2026 target because the August 2025 Korea level p34 is d] quote: "韓国 South Korea 612,172 660,900 8.0 5,811,962 6,123,100 5.4"
  - p45 China visitor arrivals to Japan, January–August 2025 cumulative (JNTO preliminar = **6,711,600** visitor arrivals (2025-01-01..2025-08-31) [DISCARD: Cumulative Jan-Aug 2025 China total is redundant for the August 2026 target because the August 2025 China level p35 is d] quote: "中国 China 746,010 1,018,600 36.5 4,595,386 6,711,600 46.1"
  - p46 Taiwan visitor arrivals to Japan, January–August 2025 cumulative (JNTO prelimina = **4,509,700** visitor arrivals (2025-01-01..2025-08-31) [DISCARD: Cumulative Jan-Aug 2025 Taiwan total is redundant for the August 2026 target because the August 2025 Taiwan level p36 is] quote: "台湾 Taiwan 564,360 620,700 10.0 4,115,255 4,509,700 9.6"
  - p47 Hong Kong visitor arrivals to Japan, January–August 2025 cumulative (JNTO prelim = **1,673,200** visitor arrivals (2025-01-01..2025-08-31) [DISCARD: Cumulative Jan-Aug 2025 Hong Kong total is redundant for the August 2026 target because the August 2025 Hong Kong level ] quote: "香港 Hong Kong 246,557 226,100 -8.3 1,801,733 1,673,200 -7.1"
- `https://www.fnn.jp/articles/FujiTV/932783` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://yamatogokoro.jp/print/?post_id=60728&_type=inbound_data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [capacity_consumption] airport and airline capacity planner

Hypothesis: Air arrivals ≈ scheduled international seat capacity to Japan × passenger load factor × foreign visitor share of arriving passengers; add sea/cruise arrivals. August 2026 capacity from published schedules and load-factor evidence constrains the total. Expected direction: capacity growth vs 2025 maps to arrival growth unless load factor or foreign share changes.

Queries issued by the searcher: Japan international airline seat capacity August 2026 OAG; 国際線 座席数 2026年8月 日本 増便; ANA総合研究所 日本着国際線 提供座席数 月別 2026年8月; JNTO 訪日外国人 2026年7月 推計値 前年比

- `https://www.anahd.co.jp/group/ari/news/20260508.html` -> **snapshot** (snapshot 20260512070453); points raw/verified 15/0
- `https://www.anahd.co.jp/group/ari/news/pdf/20260508-1.pdf` -> **snapshot** (snapshot 20260512104120); points raw/verified 15/0
- `https://www.aviationwire.jp/archives/343264/print/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ana.co.jp/group/investors/irdata/annual/pdf/26/26_00_2.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 30 (period_end 2026-10-24 after as_of: 25; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; scale word '万' not supported by quote or table header: 3)

### d4 [physical_flow] immigration and airport statistician

Hypothesis: JNTO arrivals should approximately equal foreign-national entries through airports and seaports. Partial August 2026 international arrival counts and foreign share can be scaled to the full month; role: independent physical-flow check and within-month nowcast.

Queries issued by the searcher: Narita airport international arrivals August 2026 passenger statistics; 関西空港 国際線 旅客数 2026年8月; JNTO 2026年7月 訪日外国人旅行者数 推計 前年同月比; 出入国在留管理庁 2026年 外国人 入国者数 統計 月別

- `https://www.travelvoice.jp/20260805-160287/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kansai-airports.co.jp/news/j-260731-pressrelease-forecast_flight/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aviationwire.jp/archives/348216/print/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://topics.smt.docomo.ne.jp/article/mbs_news/region/mbs_news-2873612?redirect=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] tourism statistics analyst

Hypothesis: Foreign hotel guest nights correlate with arrivals; latest monthly accommodation survey and August occupancy evidence can validate the trend, but need a bridge from guest nights to arrivals and a lag adjustment. Role: secondary validation rather than a primary route for August.

Queries issued by the searcher: 宿泊旅行統計 外国人延べ宿泊者数 2026年6月; Japan hotel foreign guest nights June 2026 accommodation survey; 外国人延べ宿泊者数 2025年8月 前年同月比 宿泊旅行統計 訪日外国人 比率; Japan hotel occupancy August 2026 forecast inbound demand

- `https://www.mlit.go.jp/kankocho/news02_00095.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.hotelbank.jp/inbound/inbound-consumption-2026-q2-lodging-share-vs-settled-adr/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mlit.go.jp/kankocho/content/002014389.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mlit.go.jp/kankocho/news02_00098.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [shocks] risk and policy analyst

Hypothesis: August 2026 arrivals are affected by calendar effects (Obon, weekends), yen level, typhoons/weather, travel advisories, visa/entry policies and source-market disruptions. Quantify exposure and adjust baseline routes. Role: modify d1/d2/d3 rather than stand alone.

Queries issued by the searcher: Japan inbound tourism August 2026 typhoon flight cancellations; 訪日外国人 2026年8月 影響; JNTO 2026年7月 訪日外客数 推計値 344万人 発表 8月; 中国 日本 渡航自粛 2026 航空便 減便 日本路線 6割減

- `https://www.traveldailynews.asia/destinations/typhoon-dolphin-disrupts-okinawa-tourism-with-flight-cancellations-and-safety-measures/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.fnn.jp/articles/-/1090042` -> **snapshot** (snapshot 20260807141506); points raw/verified 5/0
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/3qjg3k0endv6/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.traveldailynews.asia/asia-pacific/typhoon-dolphin-continues-to-disrupt-tourism-across-east-asia/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period year 2026 does not appear in the page text or URL (likely mis-dated): 4; period_end 2026-08-31 after as_of: 1)

### d7 [attention] online travel agency and search analyst

Hypothesis: Flight/hotel search and forward-booking momentum by source market for August 2026 travel indicates the direction of arrivals relative to 2025, but only after calibrating search/booking growth to arrival growth. Role: fill within-month signal, especially for late-August bookings.

Queries issued by the searcher: Japan travel forward bookings summer 2026 OTA search interest; 訪日旅行 予約 2026年8月 検索数; 中国 訪日 2026年8月 予約 前年比 旅行サイト 検索; Japan international flight seat capacity August 2026 OAG schedule increase inbound

- `https://news.nate.com/view/20260802n00814` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.nate.com/view/20260728n21306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://v.daum.net/v/20260728103527462` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ryoko-net.co.jp/?p=170901` -> **snapshot** (snapshot 20260807015544); points raw/verified 6/1
  - p48 Year-on-year growth in Agoda accommodation searches from Turkey to Japan, summer = **52** % (2026-04-01..2026-06-30) [DISCARD: Turkey is a tiny source market and Agoda search growth there is not material to total August 2026 foreign arrivals.] quote: "トルコから日本への宿泊施設検索数も前年比52%増となり、欧州市場で最も高い伸びを記録したと明らかにした。"
- dropped by code checks: 5 (period_end 2026-08-31 after as_of: 5)

### d8 [forecasts_markets] tourism forecaster

Hypothesis: Published 2026 Japan inbound forecasts, government targets, airline/OTA summer outlooks and any prediction market can provide an external range for sanity-checking. Forecasts are not realized outcomes but useful for scenario weights. Role: anchor and validation.

Queries issued by the searcher: Japan inbound tourism forecast 2026 visitor arrivals forecast; 訪日外国人 2026年 予測 旅行者数; Japan visitor arrivals August 2026 summer outlook forecast JNTO monthly; prediction market Japan inbound tourists 2026 contract

- `https://www.jtbcorp.jp/jp/newsroom/2026/01/08_jtb_inbound_outlook.html` -> **snapshot** (snapshot 20260510055357); points raw/verified 15/6
  - p49 Europe/US/Australia visitor total nights in Japan, Jan-Sep 2025 (cumulative) = **29,950,000** person-nights (2025-01-01..2025-09-30) [DISCARD: 2025 Jan-Sep Europe/US/Australia hotel-night total has no 2026 August bridge and is not directly comparable to arrival c] quote: "2025年1月~9月における欧米豪からの延べ宿泊者数は2,995万人泊(前年同期比+609万人泊)と"
  - p50 Europe/US/Australia visitor total nights year-on-year increase, Jan-Sep 2025 = **6,090,000** person-nights (2025-01-01..2025-09-30) [DISCARD: 2025 Jan-Sep hotel-night increase is not a 2026 August arrival indicator without a bridge.] quote: "2025年1月~9月における欧米豪からの延べ宿泊者数は2,995万人泊(前年同期比+609万人泊)と"
  - p51 Korea/Taiwan/Hong Kong visitor total nights in Japan, Jan-Sep 2025 (comparison b = **31,860,000** person-nights (2025-01-01..2025-09-30) [DISCARD: 2025 Jan-Sep Korea/Taiwan/Hong Kong hotel-night comparison is not directly usable for August 2026 arrivals.] quote: "従来ボリュームの大きかった韓国・台湾・香港(3,186万人泊)に匹敵する規模にまで拡大してきました。"
  - p52 JAPANiCAN.com 2026 Jan-Apr bookings from Taiwan (year-on-year) = **161** % (2026-01-01..2026-04-30) [keep: ] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています。"
  - p53 JAPANiCAN.com 2026 Jan-Apr bookings from South Korea (year-on-year) = **138** % (2026-01-01..2026-04-30) [keep: ] quote: "2026年1月~4月の予約件数は、前年同期比で台湾161%、韓国138%、米国はほぼ横ばいと堅調に推移しています。"
  - p54 JAPANiCAN.com 2026 Jan-Apr bookings from China (year-on-year) = **50** % (2026-01-01..2026-04-30) [keep: ] quote: "一方、日中関係の影響を受け、中国からの旅行者は同50%、香港は同90%にとどまっています。"
- `https://www.toyokeizai.net/articles/-/951773?display=b` -> **snapshot** (snapshot 20260807133633); points raw/verified 15/7
  - p55 Japan inbound foreign visitor arrivals, first half (Jan-Jun) 2026, cumulative to = **21,080,000** foreign visitor arrivals (2026-01-01..2026-06-30) [DISCARD: Rounded media restatement of H1 2026 total already given exactly by p18; not independent.] quote: "2026年の半年間(1~6月)のインバウンド実績が揃いました。2108万人となったので 、25年の同期間と比較して2.0%の減少となりました。"
  - p56 Change in Japan inbound arrivals, first half 2026 vs first half 2025 = **2** % (2026-01-01..2026-06-30) [DISCARD: Duplicate of p65 for H1 2026 total YoY change; same -2.0% result from another media report.] quote: "2108万人となったので 、25年の同期間と比較して2.0%の減少となりました。"
  - p57 China inbound visitors to Japan, first half 2026, cumulative total = **2,060,000** visitor arrivals from China (2026-01-01..2026-06-30) [keep: ] quote: "中国からのインバウンドは、半年で206万人、前年対比で56.4%の減少です。"
  - p58 Change in China inbound visitors to Japan, first half 2026 vs prior year = **56.4** % (2026-01-01..2026-06-30) [keep: ] quote: "中国からのインバウンドは、半年で206万人、前年対比で56.4%の減少です。"
  - p59 China share of Japan inbound visitors, first half 2026 (numerator China arrivals = **9.8** % (2026-01-01..2026-06-30) [keep: ] quote: "インバウンドに占める中国人観光客は9.8%と、03年以来の低水準です。"
  - p60 Growth in Japan inbound visitors from regions other than China, first half 2026 = **13.3** % (2026-01-01..2026-06-30) [keep: ] quote: "中国以外の地域は13.3%も伸びています。"
  - p61 Growth in Japan inbound visitors from Asia excluding China, first half 2026 = **14.9** % (2026-01-01..2026-06-30) [keep: ] quote: "中国を除くアジアからのインバウンド伸び率は14.9%と大幅に増えています。"
- `https://news.ifeng.com/c/8uucLmSOfvx` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dir.co.jp/english/research/report/analysis/20260413_025695.html` -> **snapshot** (snapshot 20260520165358); points raw/verified 0/0
- dropped by code checks: 17 (period_end 2026-12-31 after as_of: 13; period_end missing or unparseable: 1; period year 2019 does not appear in the page text or URL (likely mis-dated): 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### b1 [physical_flow] d4

Hypothesis: If preliminary August 1-15 2026 foreign-national entry counts at major Japanese airports/seaports are available, they can be scaled to a full-August nowcast and used to validate the market-decomposition estimate, especially for late-August travel.

Queries issued by the searcher: JNTO 2026年8月 訪日外客数 速報; 出入国在留管理庁 2026年8月 外国人入国者数; JNTO 2026年7月 訪日外客数 推計値 344万2100人 8月19日; 成田空港 2026年8月 外国人旅客数 速報

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])344万2100(?!\\d|[.,]\\d)']; no pages fetched**


### b2 [base_rates] d2/d6

Hypothesis: China is the largest uncertainty: it was about 30% of August 2025 arrivals but H1 2026 arrivals were down 56.4%. August 2026 China-Japan flight capacity, visa/travel advisory status, or Chinese OTA booking data would resolve whether that decline persists in the target month.

Queries issued by the searcher: 中国 日本 2026年8月 航空便 座席数; 訪日外国人 2026年 中国 減少 予約; JNTO 2026年6月 訪日外国人 中国 前年比 推計値 7月15日発表; OAG China Japan seat capacity August 2026 schedule 日中線 8月 減便 欠航率

- `https://jsto.or.jp/wp-content/uploads/jsto_bj20260831.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://honichi.com/news/2026/08/19/china202607/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/20260715-160182` -> **snapshot** (snapshot 20260716034720); points raw/verified 15/15
  - p62 JNTO June 2026 preliminary estimate of foreign visitor arrivals to Japan, total = **3,148,600** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p63 Year-on-year change in JNTO June 2026 total foreign visitor arrivals = **6.8** % (2026-06-01..2026-06-30) [keep: ] quote: "2026年6月の訪日外国人旅行者数(推計値)は、2025年同月比6.8%減の314万8600人となった。"
  - p64 JNTO cumulative January-June 2026 foreign visitor arrivals to Japan = **21,084,800** foreign visitor arrivals (2026-01-01..2026-06-30) [keep: ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p65 Year-on-year change in JNTO cumulative January-June 2026 foreign visitor arrival = **2** % (2026-01-01..2026-06-30) [keep: ] quote: "1~6月の累計でも、前年同期比2.0%減の2108万4800人と前年割れとなった。"
  - p66 JNTO June 2026 foreign visitor arrivals from China = **340,700** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "中国が34万700人(同57.3%減)"
  - p67 Year-on-year change in JNTO June 2026 foreign visitor arrivals from China = **57.3** % (2026-06-01..2026-06-30) [keep: ] quote: "中国が34万700人(同57.3%減)"
  - p68 JNTO June 2026 foreign visitor arrivals from South Korea = **787,100** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p69 Year-on-year change in JNTO June 2026 foreign visitor arrivals from South Korea = **7.8** % (2026-06-01..2026-06-30) [keep: ] quote: "韓国が78万7100人(2025年比7.8%増)"
  - p70 JNTO June 2026 foreign visitor arrivals from Taiwan = **670,400** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "台湾が67万400人(同14.6%増)"
  - p71 Year-on-year change in JNTO June 2026 foreign visitor arrivals from Taiwan = **14.6** % (2026-06-01..2026-06-30) [keep: ] quote: "台湾が67万400人(同14.6%増)"
  - p72 JNTO June 2026 foreign visitor arrivals from United States = **354,500** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "米国が35万4500人(同2.7%増)"
  - p73 Year-on-year change in JNTO June 2026 foreign visitor arrivals from United State = **2.7** % (2026-06-01..2026-06-30) [keep: ] quote: "米国が35万4500人(同2.7%増)"
  - p74 JNTO June 2026 foreign visitor arrivals from Hong Kong = **214,300** foreign visitor arrivals (2026-06-01..2026-06-30) [keep: ] quote: "香港が21万4300人(同28.5%増)"
  - p75 Year-on-year change in JNTO June 2026 foreign visitor arrivals from Hong Kong = **28.5** % (2026-06-01..2026-06-30) [keep: ] quote: "香港が21万4300人(同28.5%増)"
  - p76 Number of markets setting record June highs for foreign visitor arrivals in June = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "韓国や台湾、米国、インドなど15市場で、6月の過去最多を更新した。"
- `http://tcfa.org.tw/announce_detail.asp?id=9213324` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [capacity_consumption] d3

Hypothesis: Scheduled international seat capacity to Japan for August 2026 by source market, with load-factor evidence, would independently constrain non-China arrival growth and test whether the +13.3% H1 non-China trend is sustained in August.

Queries issued by the searcher: Japan international seat capacity August 2026 OAG; 2026年8月 日本 国際線 座席数; Japan inbound flight capacity August 2026 seats; 訪日 航空 座席 2026年8月

- `https://www.jnto.go.jp/statistics/` -> **snapshot** (snapshot 20260726110513); points raw/verified 0/0
- `https://www.mlit.go.jp/koku/koku_fr10_000036.html` -> **snapshot** (snapshot 20260112025328); points raw/verified 0/0
- `https://www.oag.com/` -> **snapshot** (snapshot 20260807174435); points raw/verified 0/0
- `https://forwardkeys.com/` -> **snapshot** (snapshot 20260602041213); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan visitor arrivals', 'japan inbound tourism', 'jnto august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p33', 'p20', 'p1', 'p2'] All report the same August 2025 JNTO headline total of 3,428,000 and the associated +16.9% YoY change. They are not independent: p1, p20 and p33 are duplicate/vintage copies of the same JNTO estimate;
- corroborating: ['p3', 'p4', 'p5'] Historical August totals for 2024, 2023 and 2019 show the seasonal August scale and post-COVID recovery path. They are different years and are context, not direct 2026 evidence.
- corroborating: ['p27', 'p28', 'p29', 'p30', 'p31', 'p26', 'p24', 'p33'] JNTO monthly 2025 levels sum consistently with the Jan-Aug 2025 cumulative p21, allowing for rounding. These are the preferred JNTO preliminary vintage; the n-seikei monthly copies p6-p12 differ only 
- corroborating: ['p21', 'p23'] p21 gives Jan-Aug 2025 cumulative 28,383,600 and p23 gives +18.2% YoY. They are the same JNTO cumulative series.
- corroborating: ['p15', 'p26', 'p17'] June 2026 and June 2025 JNTO preliminary levels: p15 is 3.15m in June 2026, p26 is 3,377,985 in June 2025, and p17 is the -6.8% YoY decline. They are internally consistent and from the same monthly se
- corroborating: ['p18', 'p56'] H1 2026 cumulative arrivals are 21,084,800 and down 2.0% vs H1 2025. p18 is the exact JNTO figure; p56 is the associated decline magnitude.
- corroborating: ['p57', 'p58', 'p59'] China H1 2026 arrivals 2.06m, down 56.4%, and 9.8% share are internally consistent and come from the same JNTO H1 data; p59 is derived from p57 and p18.
- corroborating: ['p60', 'p61'] Non-China H1 2026 growth +13.3% and Asia-ex-China growth +14.9% are derived from the same JNTO H1 data. p61 is a subset of p60; the difference implies other non-China regions grew more slowly. They ar
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43'] August 2025 market levels sum to about 2.923m for these listed markets; the remainder to p33 is about 0.505m 'other'. They are consistent components of the August 2025 total.
- corroborating: ['p44', 'p45', 'p46', 'p47'] Jan-Aug 2025 cumulative market levels are consistent with the August 2025 market levels and the JNTO January-August cumulative total, but they cover a different period and are context rather than dire
- corroborating: ['p52', 'p53', 'p54'] JAPANiCAN Jan-Apr 2026 booking indices show Taiwan/Korea strength and China/Hong Kong weakness, broadly in the same direction as p60/p58. They are bookings, not arrivals, and cover a different period,
- corroborating: ['p19'] Fifteen markets set June records despite the total June decline, qualitatively supporting the strong non-China growth in p60/p61.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p24', 'p21', 'p23'] JNTO 2025 monthly and August 2025 market breakdown. p33 total 3,428,000 and the listed August markets sum to about 2.923m, leaving roughly 0.505m other; p26 June 2025 3,377,985 and p24 July 2025 3,437
- corroborating: ['p15', 'p17', 'p18', 'p19', 'p62', 'p63', 'p64', 'p65', 'p76'] June 2026 JNTO release reported by official and media sources. p15 about 3.15m and p62 3,148,600 describe the same June total; p17/p63 both report -6.8%; p18/p64 both report 21,084,800 H1 total; p19/p
- corroborating: ['p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p64', 'p65'] China and non-China H1 2026 composition. p57 2.06m China, p58 -56.4%, and p59 9.8% share imply a total near 21.0m, matching p64 21,084,800; p60 non-China +13.3 and p61 Asia ex China +14.9 are consiste
- corroborating: ['p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p62', 'p63', 'p64', 'p65'] June 2026 market details: China 340,700/-57.3%, Korea 787,100/+7.8%, Taiwan 670,400/+14.6%, US 354,500/+2.7%, Hong Kong 214,300/+28.5%; these plus other markets reconcile to p62 3,148,600 and p63 -6.8
- related: ['p52', 'p53', 'p54', 'p66', 'p67', 'p70', 'p71', 'p74', 'p75'] JAPANiCAN Jan-Apr 2026 booking signals (Taiwan 161%, Korea 138%, China 50%, Hong Kong 90% of prior-year levels, likely index values rather than growth rates) directionally match June arrivals: Taiwan/
- related: ['p3', 'p4', 'p5', 'p33'] Historical August totals: 2019 2,520,134; 2023 2,157,190; 2024 2,933,381; 2025 3,428,000. Different years and recovery stages, not contradictions. They show seasonality and the strong 2025 level, but 
- related: ['p44', 'p45', 'p46', 'p47', 'p34', 'p35', 'p36', 'p37'] Cumulative Jan-Aug 2025 market totals and August 2025 monthly market levels come from the same JNTO series but cover different periods. They are not conflicting; the cumulative values are redundant fo

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,165,926 | ['p33', 'p35', 'p60', 'p58'] / [] | [] |  | 0.33 | equal |  |
| m2 | yoy_scaling | 3,195,219 |  | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 3,087,343 | ['p33', 'p35', 'p62', 'p66', 'p26', 'p67'] / [] | [] |  | 0.33 | equal |  |
| m4 | formula_mc | n/a | ['p35', 'p67', 'p34', 'p69', 'p36', 'p71', 'p37', 'p75', 'p38', 'p73', 'p33', 'p62', 'p66', 'p68', 'p70', 'p72', 'p74', 'p26'] / [] | [] |  | 0.00 |  | formula has more than 60 nodes |

- m1 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: sum over market of China, South Korea, Taiwan, Hong Kong, United States, other

Result: central **3,149,165** visitor, 80% interval [2,174,346, 4,561,021] visitor, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for preliminary JNTO foreign visitor arrivals to Japan for [n]–[n] August 2026 is 3,149,165 visitor (80% model-based interval 2,174,346 to 4,561,021 visitor). This is a model-based range conditional on the assumptions, not a demonstrated accuracy guarantee.

Evidence: August 2025 totals were 3,428,000 visitor arrivals, with China 1,018,600 visitor arrivals and other markets such as Korea 660,900 visitor arrivals, Taiwan 620,700 visitor arrivals, Hong Kong 226,100 visitor arrivals and the US 194,500 visitor arrivals. H1 2026 non-China growth was 13.3% while China fell 56.4%. June 2026 total was 3,148,600 foreign visitor arrivals versus 3,377,985 visitor arrivals (persons) in June 2025, with China 340,700 foreign visitor arrivals (57.3%).

The three weighted routes (33%, 33%, 33%) transfer H1 or June growth/decline onto August 2025 bases; the market-decomposition route was dropped. All August 2026 figures are transfers, not observations. The main risk is that June's non-China slowdown or China's decline does not persist through August. First-half August 2026 JNTO data would most improve this.

Key assumptions: none (every formula input is an observed data point).

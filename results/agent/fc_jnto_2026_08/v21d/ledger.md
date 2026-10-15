# Evidence ledger: fc_jnto_2026_08

- Question: Assume today is 2026-08-16. You know nothing published after this date. Estimate the number of foreign visitor arrivals to Japan in August 2026, as it will be first reported in the Japan National Tourism Organization's (JNTO) monthly estimate.
- as_of: 2026-08-16
- Pinned target: Number of foreign visitor arrivals to Japan (inbound international visitors) as estimated by the Japan National Tourism Organization (JNTO) for the calendar month of August 2026. This is the headline monthly estimate of visitor arrivals, counting foreign nationals entering Japan for tourism, busines | unit visits (arrivals) | period 2026-08-01..2026-08-31 | publisher Japan National Tourism Organization (JNTO)

- Official value (scoring only, never shown to the agent): 3,098,900

## Directions and pages

### d1 [own_history] JNTO monthly estimates and seasonal patterns

Hypothesis: August is typically a peak month for foreign visitor arrivals to Japan due to summer holidays. The target value can be estimated by applying the historical August-to-annual ratio or by extrapolating from recent monthly trends. The most recent JNTO data before the cutoff (e.g., June or July 2026) and the same month in previous years (August 2023, 2024, 2025) provide a baseline. If arrivals have been growing year-over-year, August 2026 may be higher than August 2025.

Queries issued by the searcher: JNTO monthly visitor arrivals August 2025; Japan foreign visitor arrivals June 2026 JNTO; JNTO 訪日外客数 月別推計値 2026年 5月 4月 前年同月比; 訪日外客数 2023年8月 215万7190人 2024年8月 293万3381人

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p1 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** people (visits/arrivals) (2026-06-01..2026-06-30) [keep: ] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p2 JNTO estimated foreign visitor arrivals to Japan, June 2026, year-on-year change = **6.8** % (2026-06-01..2026-06-30) [keep: ] quote: "6月:前年同月比6.8%減の315万人"
  - p3 JNTO cumulative foreign visitor arrivals to Japan, first half (January–June) 202 = **21,084,800** people (visits/arrivals) (2026-01-01..2026-06-30) [keep: ] quote: "また、上半期の累計で21,084,800人となった。"
  - p4 Number of markets recording record-high June foreign visitor arrivals, June 2026 = **15** markets (2026-06-01..2026-06-30) [keep: ] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://aviationwire.jp/archives/tag/jnto` -> **snapshot** (snapshot 20260618042453); points raw/verified 9/0
- dropped by code checks: 10 (number: unknown scale word '万': 1; number: more than one number in value_as_written: 9)

### d2 [base_rates] Seasonality and year-over-year growth rates

Hypothesis: The ratio of August arrivals to the preceding month (July) or to the annual total is relatively stable. By applying the historical August/July ratio to the known July 2026 figure (if available), or by applying the August share of annual arrivals to a year-to-date total, we can estimate August 2026. Also, the year-over-year growth rate in recent months can be extrapolated. The relationship: August 2026 ≈ July 2026 × (August/July ratio from 2023-2025) or August 2026 ≈ (2026 YTD through July) × (August share of annual from 2023-2025) / (YTD share through July).

Queries issued by the searcher: JNTO July 2026 visitor arrivals monthly estimate; Japan foreign visitor arrivals August 2025 JNTO record 3.4 million; JNTO 訪日外客数 2025年8月 342万人 前年同月比 7月 3,437,118; 訪日外客数 2024年8月 293万人 2023年8月 215万人 JNTO 月別

- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/` -> **snapshot** (snapshot 20260228082412); points raw/verified 0/0
- `https://www.travelvoice.jp/20250917-158383` -> **snapshot** (snapshot 20260608084226); points raw/verified 15/7
  - p5 Year-over-year growth rate of foreign visitor arrivals to Japan, August 2025 vs  = **16.9** percent (2025-08-01..2025-08-31) [keep: ] quote: "2025年8月の訪日外国人旅行者数(推計値)は前年比16.9%増の342万8000人となり、8月として初めて300万人を超えた。"
  - p6 Increase in August 2025 foreign visitor arrivals vs August 2023 = **58.9** percent (2025-08-01..2025-08-31) [keep: ] quote: "2023年8月(実数:215万7190人)比では、58.9%増。"
  - p7 Year-over-year growth rate of foreign visitor arrivals to Japan from China, Augu = **36.5** percent (2025-08-01..2025-08-31) [keep: ] quote: "中国が101万8600人(前年比36.5%増)"
  - p8 Year-over-year growth rate of foreign visitor arrivals to Japan from South Korea = **8** percent (2025-08-01..2025-08-31) [keep: ] quote: "韓国が66万900人(同8%増)"
  - p9 Year-over-year growth rate of foreign visitor arrivals to Japan from Taiwan, Aug = **10** percent (2025-08-01..2025-08-31) [keep: ] quote: "台湾が62万700人(同10%増)"
  - p10 Year-over-year change rate of foreign visitor arrivals to Japan from Hong Kong,  = **8.3** percent (2025-08-01..2025-08-31) [keep: ] quote: "香港が22万6100人(同8.3%減)"
  - p11 Year-over-year growth rate of foreign visitor arrivals to Japan from the United  = **11.7** percent (2025-08-01..2025-08-31) [keep: ] quote: "米国が19万4500人(同11.7%増)の順。"
- `https://honichi.com/news/2026/08/19/inbound202607/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (number: more than one number in value_as_written: 8)

### d3 [related_series] Immigration statistics and air travel data

Hypothesis: JNTO's estimate is based on Ministry of Justice immigration records. Related series such as the number of foreign nationals entering Japan through major airports (Narita, Haneda, Kansai, etc.) or the number of international flight passengers can serve as a proxy. If air passenger data for August 2026 is partially available (e.g., first half), it can be scaled to the full month using historical intra-month patterns. The relationship: foreign visitor arrivals ≈ (international air passenger arrivals) × (share of foreign visitors among passengers) × (adjustment for land/sea entries).

Queries issued by the searcher: JNTO foreign visitor arrivals August 2025 monthly estimate; Japan international passenger arrivals August 2025 Narita Haneda Kansai foreign arrivals; JNTO 訪日外客数 2026年6月 推計値; 訪日外客数 2026年 月別 推移 JNTO

- `https://www.jnto.go.jp/news/press/20260715_monthly.html` -> **snapshot** (snapshot 20260716193946); points raw/verified 5/4
  - p12 JNTO estimated foreign visitor arrivals to Japan, June 2026 (monthly estimate) = **3,148,600** people (visits/arrivals) (2026-06-01..2026-06-30) [DISCARD: Duplicate of p1: same JNTO June 2026 estimate, same value, same source. Adds no independent information.] quote: "6月の訪日外客数は3,148,600人で、前年同月比6.8%減となったものの"
  - p13 Year-on-year change in JNTO foreign visitor arrivals to Japan, June 2026 = **6.8** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p2: same June 2026 YoY change, same source.] quote: "6月:前年同月比6.8%減の315万人"
  - p14 Cumulative JNTO foreign visitor arrivals to Japan, first half (January-June) 202 = **21,084,800** people (visits/arrivals) (2026-01-01..2026-06-30) [DISCARD: Duplicate of p3: same H1 2026 cumulative total, same source.] quote: "また、上半期の累計で21,084,800人となった。"
  - p15 Number of markets recording their highest-ever June foreign visitor arrivals to  = **15** markets (2026-06-01..2026-06-30) [DISCARD: Duplicate of p4: same count of record June markets, same source.] quote: "台湾、韓国、米国、インドなど15市場で6月として過去最高を記録した。"
- `https://www.jnto.go.jp/statistics/data/visitors-statistics/?tab=block10` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.narita-airport.jp/files/b2e22b1f56ede88eda96151d616c3d8893efaeaa57658001834df6fb32d70835` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.47news.jp/13060940.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (number: unknown scale word '万人': 1)

### d4 [forecasts_markets] Official forecasts and industry projections

Hypothesis: Government or industry forecasts for Japan's inbound tourism in 2026, such as targets from the Japan Tourism Agency or projections from travel associations, can provide a top-down estimate. If a full-year 2026 forecast exists, August can be derived using the historical share of August in annual arrivals. The relationship: August 2026 arrivals ≈ (annual 2026 forecast) × (historical August share).

Queries issued by the searcher: Japan inbound tourism forecast 2026 JNTO visitor arrivals; Japan Tourism Agency 2026 target visitors forecast; JNTO 訪日外客数 2025年8月 推計値 単月; 訪日外客数 月別 2024年8月 2023年8月 推計値 JNTO

- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260520_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20250917-158383` -> **snapshot** (snapshot 20260608084226); points raw/verified 15/7
  - p16 Year-on-year growth rate of foreign visitor arrivals to Japan, August 2025 = **16.9** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p5: same August 2025 YoY growth rate, same source.] quote: "2025年8月の訪日外国人旅行者数(推計値)は前年比16.9%増の342万8000人となり、8月として初めて300万人を超えた。"
  - p17 Increase in August 2025 foreign visitor arrivals versus August 2023 = **58.9** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p6: same August 2025 vs August 2023 comparison, same source.] quote: "2023年8月(実数:215万7190人)比では、58.9%増。"
  - p18 Year-on-year growth rate of foreign visitor arrivals to Japan from China, August = **36.5** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p7: same China August 2025 growth rate, same source.] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)"
  - p19 Year-on-year growth rate of foreign visitor arrivals to Japan from South Korea,  = **8** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p8: same South Korea August 2025 growth rate, same source.] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)"
  - p20 Year-on-year growth rate of foreign visitor arrivals to Japan from Taiwan, Augus = **10** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p9: same Taiwan August 2025 growth rate, same source.] quote: "中国が101万8600人(前年比36.5%増)、韓国が66万900人(同8%増)、台湾が62万700人(同10%増)"
  - p21 Year-on-year growth rate of foreign visitor arrivals to Japan from Hong Kong, Au = **8.3** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p10: same Hong Kong August 2025 growth rate, same source.] quote: "香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
  - p22 Year-on-year growth rate of foreign visitor arrivals to Japan from the United St = **11.7** percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p11: same United States August 2025 growth rate, same source.] quote: "香港が22万6100人(同8.3%減)、米国が19万4500人(同11.7%増)の順。"
- `https://www.japantimes.co.jp/news/2026/07/16/japan/society/japan-visitor-number-down/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (number: more than one number in value_as_written: 8)

### d5 [physical_flow] Port and airport entry counts

Hypothesis: The number of foreign visitor arrivals can be approximated by summing entries through major ports and airports. If partial data for August 2026 (e.g., first two weeks) is available from immigration or airport authorities, it can be scaled to the full month using the historical intra-month distribution (e.g., first half typically accounts for about 50% of monthly total). The relationship: August 2026 total ≈ (first-half August 2026 entries) / (historical share of first half in August).

Queries issued by the searcher: Japan immigration foreign entries August 2026; JNTO foreign visitor arrivals August 2026 monthly estimate; Narita airport foreign arrivals daily August 2026; Japan visitor arrivals August 2025 JNTO record

- `https://www.narita-airport.jp/files/a7a1e0a6db19049d5e39d3cd849bb7d07e4d4c74d50c426be7f15e3ffeb116f0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.saga-s.co.jp/articles/-/1777098` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/20260805-160287/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [capacity_consumption] Flight capacity and hotel bookings

Hypothesis: Available seat capacity on international flights to Japan multiplied by an estimated load factor and the share of seats occupied by foreign visitors gives an upper bound or estimate of arrivals. Alternatively, hotel occupancy by foreign guests in August 2026 (if partially reported) can be scaled to national arrivals using the historical ratio of hotel guests to total arrivals. The relationship: foreign visitor arrivals ≈ (international seat capacity to Japan) × (load factor) × (share of foreign visitors) + other modes.

Queries issued by the searcher: Japan international flight seat capacity August 2026 OAG; JNTO foreign visitor arrivals August 2025 record; JNTO 訪日外客数 2026年7月 推計値; Japan international airline seat capacity summer 2026 increase forecast

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/news/_files/20260819_1615.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.travelvoice.jp/20260819-160365/print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://press.jal.co.jp/en/items/uploads/JAL%20Traffic%20Data%20AUG%202026.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d7 [shocks] Events, policies, and disruptions affecting travel

Hypothesis: Shocks such as visa policy changes, currency fluctuations (weak yen boosting inbound tourism), natural disasters, pandemics, or geopolitical events can significantly alter arrival numbers. For August 2026, any known events before the cutoff (e.g., new visa-free arrangements, major sporting events, or travel advisories) could shift the estimate. The direction and magnitude of impact should be assessed relative to the baseline from own history.

Queries issued by the searcher: JNTO foreign visitor arrivals Japan monthly 2026 record; Japan visa policy 2026 foreign tourists visa-free changes; Japan China travel advisory Chinese visitors decline 2026 airline capacity cuts; yen exchange rate August 2026 USD JPY weak

- `https://www.travelvoice.jp/english/tags/ForeignVisitorArrivalResult` -> **snapshot** (snapshot 20260308161724); points raw/verified 15/15
  - p23 International visitor arrivals to Japan, August 2025 (monthly estimate) = **3,428,000** visits (arrivals) (2025-08-01..2025-08-31) [keep: ] quote: "The number of international arrivals in Japan in August 2025 was up 16.9% year on year to 3,428,000."
  - p24 Year-on-year growth rate of international arrivals to Japan, August 2025 = **16.9** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p5/p23: same August 2025 YoY growth rate, same source.] quote: "The number of international arrivals in Japan in August 2025 was up 16.9% year on year to 3,428,000."
  - p25 International visitor arrivals to Japan, August 2024 (monthly estimate) = **2,933,000** visits (arrivals) (2024-08-01..2024-08-31) [keep: ] quote: "The number of international visitors to Japan in August 2024 reached 2,933,000, 16.4% more than the same month in 2019 and 35% more than a year ago"
  - p26 International arrivals to Japan, January 2026 (monthly estimate) = **3,597,500** visits (arrivals) (2026-01-01..2026-01-31) [keep: ] quote: "The number of international arrivals in Japan in January 2026 was down 4.9% year on year to 3,597,500, declining for the first time in four years since January 2022."
  - p27 Year-on-year change in international arrivals to Japan, January 2026 = **4.9** % (2026-01-01..2026-01-31) [keep: ] quote: "The number of international arrivals in Japan in January 2026 was down 4.9% year on year to 3,597,500, declining for the first time in four years since January 2022."
  - p28 International arrivals to Japan, November 2025 (monthly estimate) = **3,518,000** visits (arrivals) (2025-11-01..2025-11-30) [keep: ] quote: "The number of international arrivals in Japan in November 2025 was up 10.4% year on year to 3,518,000."
  - p29 International arrivals to Japan, October 2025 (monthly estimate) = **3,896,300** visits (arrivals) (2025-10-01..2025-10-31) [keep: ] quote: "The number of international arrivals in Japan in October 2025 was up 17.6% year on year to 3,896,300, record-braking for October with 580,000 more arrivals than a year ago."
  - p30 International arrivals to Japan, September 2025 (monthly estimate) = **3,266,800** visits (arrivals) (2025-09-01..2025-09-30) [keep: ] quote: "The number of international arrivals in Japan in September 2025 was up 13.7% year on year to 3,266,800, totaling 31.7 million arrivals for the first nine months."
  - p31 International arrivals to Japan, July 2025 (monthly estimate) = **3,437,000** visits (arrivals) (2025-07-01..2025-07-31) [keep: ] quote: "The number of international arrivals in Japan in July 2025 was up 4.4% year on year to record-high 3,437,000 for July"
  - p32 International arrivals to Japan, June 2025 (monthly estimate) = **3,377,800** visits (arrivals) (2025-06-01..2025-06-30) [keep: ] quote: "The number of international arrivals in Japan in June 2025 was up 7.6% year on year to record-high 3,377,800 for June totaling 21,518,100 for the first half of 2025."
  - p33 International arrivals to Japan, May 2025 (monthly estimate) = **3,693,300** visits (arrivals) (2025-05-01..2025-05-31) [keep: ] quote: "The number of international arrivals in Japan in May 2025 was up 21.5% year on year to record-high 3,693,300 for May."
  - p34 International arrivals to Japan, April 2025 (monthly estimate) = **3,908,900** visits (arrivals) (2025-04-01..2025-04-30) [keep: ] quote: "The number of international arrivals in Japan in April 2025 was up 28.5% year on year to record-high 3,908,900 on a single month basis."
  - p35 International arrivals to Japan, calendar year 2025 (annual total) = **42,683,600** visits (arrivals) (2025-01-01..2025-12-31) [keep: ] quote: "The number of international arrivals in Japan in 2025 was up 15.8% year on year to 42,683,600 in total, about 17 million more than 2023 or about 10 million more than 2019."
  - p36 International visitors to Japan, calendar year 2024 (annual total) = **36,900,000** visits (arrivals) (2024-01-01..2024-12-31) [keep: ] quote: "The number of international visitors to Japan in 2024 reached record-high 36.9 million, 15.6% more visitors than the previous record of 31.9 million in 2019"
  - p37 International cruise travelers to Japan, calendar year 2025 (annual total) = **1,767,000** travelers (2025-01-01..2025-12-31) [keep: ] quote: "the number of international cruise travelers to Japan increased by 1.2 times year on year to 1,767,000, and port calls were up 1.3 times to 3,117, 6% more than the peak level in 2018."
- `https://www.ccaonline.cn/yunshu/ystop/1231733.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelandtourworld.cn/%E6%B6%88%E6%81%AF/%E5%88%8A%E6%96%87/0czr1h4z6n4n/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20260617_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d8 [persona] Travel agencies and tour operators

Hypothesis: Major travel agencies and online travel platforms (e.g., JTB, Booking.com, Expedia) may report booking volumes or forward-looking travel demand for Japan in August 2026. If booking data shows a certain percentage change versus August 2025, it can be applied to the August 2025 actual to estimate August 2026. The relationship: August 2026 ≈ August 2025 × (1 + booking growth rate).

Queries issued by the searcher: Japan travel bookings summer 2026 inbound demand forecast; JNTO foreign visitor arrivals August 2025 record; JNTO July 2026 visitor arrivals estimate 3.44 million; Expedia "Unpack '26" summer report Japan searches bookings 2026

- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rakuten.today/blog/rakuten-travel-xchange-ceo-why-japan-is-maturing-as-a-global-travel-destination.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] JNTO monthly release

Hypothesis: The July 2026 JNTO monthly estimate (normally released mid-August 2026) would provide the most recent level and YoY change immediately preceding the target month. This unlocks the August/July ratio route (m2) and a direct YoY extrapolation, and would materially narrow the estimate because June 2026 was already -6.8% YoY.

Queries issued by the searcher: JNTO 訪日外国人旅行者数 2026年7月 推計値; Japan National Tourism Organization July 2026 visitor arrivals estimate; JNTO 訪日外客数 2025年8月 推計値 前年同月比 342万人; 訪日外客数 月別推移 8月 7月 2024 2025 推計値 JNTO 統計

- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/_files/20260819_1615.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.jnto.go.jp/statistics/data/_files/20250917_1615-1.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://yamatogokoro.jp/print/?post_id=61032&_type=inbound_data` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] Immigration / airport authority

Hypothesis: Partial August 2026 entry counts (first half of August) from immigration or major airport operators would allow scaling to the full month using the historical intra-month distribution, directly anchoring the target rather than relying on a YoY growth assumption.

Queries issued by the searcher: 出入国在留管理庁 2026年8月 外国人入国者数 速報; JNTO 訪日外客数 2026年8月 推計値; 訪日外客数 2026年7月推計値 JNTO 344万人 8月15日発表; 出入国在留管理庁 2026年7月 出入国管理統計速報 外国人入国者数

- `https://www.jnto.go.jp/news/press/20260916_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/files?page=1&layout=dataset&stat_infid=000040502458&iroha=19` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.jp/i/1472471563275551505` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Industry / government forecast

Hypothesis: A 2026 full-year inbound forecast or a summer-2026 demand outlook from JTB, the Japan Tourism Agency, or an airline would provide a top-down anchor and help resolve whether the 2026 downturn (January -4.9%, June -6.8%) persists into August or reverses.

Queries issued by the searcher: JTB 2026 inbound visitor arrivals forecast Japan foreign tourists; Japan National Tourism Organization 2026 inbound forecast summer 2026 demand

- `https://www.tourism.jp/en/research-reports/2026-inbound-outlook/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.travelvoice.jp/english/the-number-of-international-travelers-to-japan-may-reach-a-plateau-in-2026-affected-by-a-decrease-in-travelers-from` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://newsdig.tbs.co.jp/articles/withbloomberg/2804762?display=1` -> **snapshot** (snapshot 20260715131057); points raw/verified 13/3
  - p38 Japan foreign visitor arrivals, January–June cumulative, year-on-year change = **2** percent (2026-01-01..2026-06-30) [keep: ] quote: "日本政府観光局(JNTO)が15日発表した1-6月の訪日客数は、前年同期比2%減の2108万人だった。"
  - p39 Japan foreign visitor arrivals, June 2026, year-on-year change = **6.8** percent (2026-06-01..2026-06-30) [keep: ] quote: "対象期間の最終月となる6月は、前年同月比6.8%減の314万8600人となり、中国からの訪日客が同57%減の34万人と全体を押し下げた。"
  - p40 Chinese visitor arrivals to Japan, June 2026, year-on-year change = **57** percent (2026-06-01..2026-06-30) [keep: ] quote: "対象期間の最終月となる6月は、前年同月比6.8%減の314万8600人となり、中国からの訪日客が同57%減の34万人と全体を押し下げた。"
- `https://www.jnto.go.jp/news/press/20260819_montly.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 10 (number: unknown scale word '万人': 2; number: more than one number in value_as_written: 1; period_end 2026-12-31 after as_of: 2; period_end 2026-09-30 after as_of: 4; period_end missing or unparseable: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan tourism', 'visitor arrivals', 'august 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p12'] Same JNTO June 2026 monthly estimate (3,148,600) reported via two different snapshots; identical underlying measurement, so they are redundant copies rather than independent confirmation.
- corroborating: ['p2', 'p13'] Same JNTO June 2026 year-on-year change (-6.8%) from the same release; redundant copies.
- corroborating: ['p3', 'p14'] Same JNTO first-half 2026 cumulative total (21,084,800); redundant copies of one release.
- corroborating: ['p4', 'p15'] Same JNTO statement that 15 markets set June records; redundant copies.
- corroborating: ['p5', 'p16', 'p23', 'p24'] All describe August 2025 arrivals of 3,428,000 and +16.9% YoY from the same travelvoice/JNTO-derived report; one underlying measurement, not four independent confirmations.
- corroborating: ['p6', 'p17'] Same +58.9% comparison of August 2025 vs August 2023; redundant copies.
- corroborating: ['p7', 'p18'] Same China August 2025 +36.5% figure; redundant copies.
- corroborating: ['p8', 'p19'] Same South Korea August 2025 +8% figure; redundant copies.
- corroborating: ['p9', 'p20'] Same Taiwan August 2025 +10% figure; redundant copies.
- corroborating: ['p10', 'p21'] Same Hong Kong August 2025 -8.3% figure; redundant copies.
- corroborating: ['p11', 'p22'] Same US August 2025 +11.7% figure; redundant copies.
- corroborating: ['p25', 'p23'] August 2024 (2,933,000) and August 2025 (3,428,000) are consistent with the reported +16.9% YoY for August 2025, forming a coherent own-history series for the same calendar month.
- corroborating: ['p26', 'p27'] January 2026 level (3,597,500) and -4.9% YoY are internally consistent and indicate a slowdown/decline phase entering 2026.
- conflicting: ['p1', 'p26'] January 2026 was down 4.9% YoY while June 2026 was down 6.8% YoY, but these are different months; together they suggest a broad 2026 downturn rather than a contradiction. The June 2026 decline is the 
- corroborating: ['p35', 'p36'] 2024 annual 36.9m and 2025 annual 42.68m are consistent with the reported +15.8% for 2025; useful for computing August shares of annual totals.
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34'] Monthly 2025 levels form a coherent within-year seasonal profile (April peak, summer plateau, autumn rebound) usable for August/July and August-share ratios.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p12'] p1 and p12 are duplicate records of the same JNTO June 2026 monthly estimate (3,148,600 arrivals). They share the same underlying measurement and source, so they corroborate only as a consistency chec
- corroborating: ['p2', 'p13', 'p39'] p2, p13, and p39 all report the same June 2026 year-on-year decline of 6.8%. p2/p13 are JNTO-sourced; p39 is a news report of the same JNTO release. They are not independent measurements.
- corroborating: ['p3', 'p14'] p3 and p14 are duplicate records of the JNTO first-half 2026 cumulative total (21,084,800 arrivals). Same source and measurement.
- corroborating: ['p4', 'p15'] p4 and p15 both report 15 markets setting June records. Same JNTO release; duplicate evidence.
- corroborating: ['p5', 'p16', 'p23', 'p24'] p5, p16, p23, and p24 all report August 2025 arrivals of 3,428,000 and/or +16.9% YoY. They trace to the same JNTO estimate and travelvoice reporting, so they are mutually reinforcing but not independe
- corroborating: ['p6', 'p17'] p6 and p17 both report August 2025 was +58.9% versus August 2023. Same underlying comparison.
- corroborating: ['p7', 'p18'] p7 and p18 both report China August 2025 arrivals of 1,018,600, +36.5% YoY. Same source.
- corroborating: ['p8', 'p19'] p8 and p19 both report South Korea August 2025 arrivals of 660,900, +8% YoY. Same source.
- corroborating: ['p9', 'p20'] p9 and p20 both report Taiwan August 2025 arrivals of 620,700, +10% YoY. Same source.
- corroborating: ['p10', 'p21'] p10 and p21 both report Hong Kong August 2025 arrivals of 226,100, -8.3% YoY. Same source.
- corroborating: ['p11', 'p22'] p11 and p22 both report United States August 2025 arrivals of 194,500, +11.7% YoY. Same source.
- corroborating: ['p1', 'p3', 'p38'] p1/p3 (JNTO June and H1 2026) and p38 (news report of H1 2026 -2% YoY) are consistent: H1 2026 cumulative 21,084,800 versus H1 2025 21,518,100 implies about -2.0% YoY. p38 is a secondary report of the
- corroborating: ['p1', 'p26', 'p27', 'p39', 'p40'] These points together describe the 2026 slowdown: January 2026 -4.9% YoY, June 2026 -6.8% YoY, with Chinese arrivals down 57% in June 2026. They are consistent with a weakening trend rather than a con
- corroborating: ['p23', 'p25', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] These JNTO monthly and annual totals form a coherent 2024-2025 history: August 2024 2,933,000; July 2025 3,437,000; August 2025 3,428,000; 2025 annual 42,683,600; 2024 annual 36,900,000. They are the 
- corroborating: ['p28', 'p29', 'p30'] September, October, and November 2025 monthly estimates are consistent with the 2025 annual total and the broader series.
- contextual: ['p37'] International cruise travelers (1,767,000 in 2025) are a small subset of total arrivals and are already included in JNTO's headline count. Useful only as a scope note, not as an independent level.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY change factor relative to August 2025 | 0.95 | 0.85..1.05 | 0.845..1.056 (widened) | ratio | m1 (m1) | June 2026 was -6.8% YoY and H1 2026 was about -2.0% YoY, with Chinese arrivals down 57% in June. The 2026 slowdown is likely to persist into August, but August is a peak summer month and the decline may moderate. A central factor of 0.95 (i.e., -5% YoY) with a wide 10th-90th percentile range of 0.85 | The 2026 slowdown observed in January and June continues into August 2026 without a major new shock or a sharp policy-driven reversal. | Evidence that July 2026 arrivals returned to positive YoY growth, or a major new visa-free arrangement or travel disruption that clearly shifts August demand. |
| a2 | August 2026 YoY change factor relative to August 2025 (alternative) | 0.93 | 0.82..1.04 | 0.82..1.04 | ratio | m2 (m2) | A slightly more pessimistic central factor reflecting the possibility that the June -6.8% YoY decline and the 57% drop in Chinese arrivals persist or worsen through the summer. The range is wide to cover both stabilization and further deterioration. | The Chinese market weakness and broader 2026 slowdown continue at or near June 2026 rates through August 2026. | A July 2026 JNTO release showing a clear improvement in YoY growth, or evidence of a sharp rebound in Chinese arrivals. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 3,237,188 | ['p23'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 3,165,102 | ['p23'] / ['a2'] | [] |  | 0.50 | equal |  |

Result: central **3,200,942**, 80% interval [2,323,460, 4,409,816], basis no_basis, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best estimate for foreign visitor arrivals to Japan in August 2026, as JNTO's headline monthly estimate, is 3,200,942 visits. This covers the calendar month [n]-[n]-[n] to 2026-[n]-[n] and counts entries, not unique visitors. The supplied interval is 2,323,460 to 4,409,816, at the 80% level, and is no basis — model-based and conditional on the assumptions, not a demonstrated accuracy guarantee.

The estimate combines 2 methods: 3,237,188 (weight 50%) and 3,165,102 (weight 50%). Both anchor on the observed August 2025 level and apply a YoY factor: 0.95 (range 0.845–1.056) and 0.93 (range 0.82–1.04). Only the anchor is observed; the factors are analyst assumptions, so the methods are not independent.

The main risk is that the [n] slowdown, including weak Chinese arrivals, reverses or worsens. Partial August data and clearer Chinese demand figures would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 YoY change factor relative to August 2025: 0.95 ratio, range 0.845 to 1.056 (range widened by code); used by m1. Overturned by: Evidence that July 2026 arrivals returned to positive YoY growth, or a major new visa-free arrangement or travel disruption that clearly shifts August demand.
- a2 August 2026 YoY change factor relative to August 2025 (alternative): 0.93 ratio, range 0.82 to 1.04; used by m2. Overturned by: A July 2026 JNTO release showing a clear improvement in YoY growth, or evidence of a sharp rebound in Chinese arrivals.

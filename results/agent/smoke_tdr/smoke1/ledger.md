# Evidence ledger: smoke_tdr

- Question: What was the average daily number of visitors to Tokyo Disney Resort (Tokyo Disneyland and Tokyo DisneySea combined) in September 2026?
- as_of: 2026-10-17
- Pinned target: Average daily number of visitors (park admissions/visits, not unique people) to Tokyo Disney Resort, i.e. Tokyo Disneyland and Tokyo DisneySea combined, during September 2026, expressed as total monthly admissions divided by the number of days in September 2026 (30). | unit visitors per day | period 2026-09-01..2026-09-30 | publisher No official daily/monthly visitor series is published by Oriental Land Co. (operator); attendance is disclosed only in aggregate annual/fiscal figures and occasional press reports. Any monthly figure would be an estimate or third-party (e.g. TEA/AECOM Themed Entertainment Association) reconstruction

## Directions and pages

### d1 [own_history] Oriental Land investor relations / annual reports

Hypothesis: Annual (fiscal-year) attendance for Tokyo Disneyland and Tokyo DisneySea combined, multiplied by a September share of annual attendance, gives the monthly total; dividing by 30 gives the daily average. Historical monthly or seasonal shares (if any press disclosures exist) constrain the September share.

Queries issued by the searcher: Oriental Land fiscal 2025 attendance Tokyo Disneyland Tokyo DisneySea combined annual report; 東京ディズニーリゾート 入園者数 月別 9月; Tokyo Disney Resort annual attendance fiscal 2024 Oriental Land 30 million; Oriental Land FY2026 attendance forecast Tokyo Disneyland DisneySea

- `https://www.olc.co.jp/en/ir/library/annual/main/01111111112/teaserItems2/010/linkList/0/link/integrated_2025_en_07.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.yomiuri.co.jp/economy/20251030-OYT1T50171/` -> **live_dated** (page date 2025-10-30); points raw/verified 14/1
  - p1 Tokyo Disney Resort theme park admissions (visitors), Apr-Sep 2025 = **12,250,000** visitors (万人 = ten thousand people) (2025-04-01..2025-09-30) [keep: ] quote: "4~9月のテーマパーク入園者数は0・4%増の1225万人でほぼ横ばいだった"
- `https://news.qq.com/rain/a/20260510A001KA00` -> **live_dated** (page date 2026-05-10); points raw/verified 15/15
  - p2 Tokyo Disney Resort (Tokyo Disneyland + Tokyo DisneySea) total visitor attendanc = **27,530,000** visitors (person-times) (2025-04-01..2026-03-31) [keep: ] quote: "2025年,东迪(含东京迪士尼乐园和海洋迪士尼乐园两座园区)共接待游客数量2753万人次,同比下滑了0.1%。"
  - p3 Tokyo Disney Resort total visitor attendance year-on-year change, FY2026 = **0.1** % (year-on-year decline) (2025-04-01..2026-03-31) [keep: Kept as the y/y change accompanying p2; not used as a level.] quote: "共接待游客数量2753万人次,同比下滑了0.1%"
  - p4 Oriental Land FY2026 revenue = **704,500,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "东迪2025年营收7045亿日元,约合305亿人民币,同比增长了3.7%"
  - p5 Oriental Land FY2026 revenue year-on-year growth = **3.7** % (year-on-year growth) (2025-04-01..2026-03-31) [keep: Kept as revenue growth context; not a direct input.] quote: "营收7045亿日元,约合305亿人民币,同比增长了3.7%"
  - p6 Oriental Land FY2026 net profit attributable to parent owners = **121,800,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "归属母公司所有者的净利润1218亿日元,约合53亿人民币,同比下滑了1.8%"
  - p7 Oriental Land FY2026 net profit year-on-year change = **1.8** % (year-on-year decline) (2025-04-01..2026-03-31) [keep: Kept as profit-change context; not a direct input.] quote: "净利润1218亿日元,约合53亿人民币,同比下滑了1.8%"
  - p8 Ticket revenue share of total revenue, Tokyo Disney Resort FY2026 = **41.1** % (ticket revenue / total revenue) (2025-04-01..2026-03-31) [keep: ] quote: "这四块占总营收的比例分别是41.1%、23.7%、16.9%、14%"
  - p9 Merchandise sales share of total revenue, Tokyo Disney Resort FY2026 = **23.7** % (merchandise revenue / total revenue) (2025-04-01..2026-03-31) [keep: ] quote: "这四块占总营收的比例分别是41.1%、23.7%、16.9%、14%"
  - p10 Hotel revenue share of total revenue, Tokyo Disney Resort FY2026 = **16.9** % (hotel revenue / total revenue) (2025-04-01..2026-03-31) [keep: ] quote: "这四块占总营收的比例分别是41.1%、23.7%、16.9%、14%"
  - p11 Food & beverage revenue share of total revenue, Tokyo Disney Resort FY2026 = **14** % (F&B revenue / total revenue) (2025-04-01..2026-03-31) [keep: ] quote: "这四块占总营收的比例分别是41.1%、23.7%、16.9%、14%"
  - p12 Ticket revenue amount, Tokyo Disney Resort FY2026 = **289,500,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "对应营收金额分别为2895亿日元、1673亿日元、1190亿日元、983亿日元"
  - p13 Merchandise sales revenue amount, Tokyo Disney Resort FY2026 = **167,300,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "对应营收金额分别为2895亿日元、1673亿日元、1190亿日元、983亿日元"
  - p14 Hotel revenue amount, Tokyo Disney Resort FY2026 = **119,000,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "对应营收金额分别为2895亿日元、1673亿日元、1190亿日元、983亿日元"
  - p15 Food & beverage revenue amount, Tokyo Disney Resort FY2026 = **98,300,000,000** Japanese yen (2025-04-01..2026-03-31) [keep: ] quote: "对应营收金额分别为2895亿日元、1673亿日元、1190亿日元、983亿日元"
  - p16 Secondary spending (hotel + F&B + merchandise) share of total revenue, Tokyo Dis = **54.6** % (non-ticket revenue / total revenue) (2025-04-01..2026-03-31) [keep: Kept as a derived share consistent with p8–p11; not used directly.] quote: "酒店、餐饮、购物等二消合计占54.6%"
- `https://castel.jp/p/5870` -> **live_dated** (page date 2026-10-02); points raw/verified 15/1
  - p17 Actual annual attendance FY2025 (2025/4-2026/3), both parks combined = **27,530,000** visitors (annual admissions) (2025-04-01..2026-03-31) [keep: ] quote: "実際、2025年4月〜2026年3月の1年間の入園者数は2,753万人で、1日1パークあたり平均3万7千人でした。"
- dropped by code checks: 27 (value_as_written not in quote as a whole number: 8; number: value_as_written is only part of a larger CJK number in the quote: 5; period_end 2027-03-31 after as_of: 1; number: CJK numerals (e.g. 三百, 1千) are not supported: 3; period_end 2026-12-31 after as_of: 4; period_end 2026-10-31 after as_of: 2; period_end 2026-11-30 after as_of: 2; period_end missing or unparseable: 2)

### d2 [related_series] TEA/AECOM Theme Index and industry trackers

Hypothesis: Third-party annual attendance estimates for Tokyo Disneyland and Tokyo DisneySea provide a cross-check on Oriental Land figures and a base for applying a September seasonal share.

Queries issued by the searcher: TEA AECOM Theme Index Tokyo Disneyland attendance 2024; Tokyo DisneySea attendance 2023 2024 theme index; 東京ディズニーリゾート 月別 入園者数 9月 季節変動; Oriental Land attendance fiscal 2024 27.5 million Tokyo Disneyland DisneySea theme index 2025

- `https://diservations.com/magic-kingdom-tops-2024-tea-global-experience-index/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://dpost.jp/2025/10/24/wp-127792/` -> **live_dated** (page date 2025-10-24); points raw/verified 0/0
- `https://castel.jp/p/5870` -> **live_dated** (page date 2026-10-02); points raw/verified 16/1
  - p18 Actual total park admissions, Apr 2025-Mar 2026, both parks = **27,530,000** visitors (annual admissions, both parks) (2025-04-01..2026-03-31) [DISCARD: Duplicate of p2/p17 (27.53M FY2025 admissions).] quote: "実際、2025年4月〜2026年3月の1年間の入園者数は2,753万人で、1日1パークあたり平均3万7千人でした。"
- `https://www.theparkdb.com/blog/peaking-theme-park/` -> **live_dated** (page date 2023-12-08); points raw/verified 15/0
- dropped by code checks: 30 (period_end 2026-10-31 after as_of: 2; period_end 2026-12-31 after as_of: 4; period_end 2026-11-30 after as_of: 2; period_end 2027-03-31 after as_of: 1; number: CJK numerals (e.g. 三百, 1千) are not supported: 3; period_end missing or unparseable: 18)

### d3 [base_rates] Seasonality analyst

Hypothesis: September attendance share of annual total can be estimated from Japanese school-holiday calendar, event calendar (Halloween events starting mid-September), and comparable seasonal patterns at Japanese leisure venues; September is typically a low month, so share is below 1/12 of annual.

Queries issued by the searcher: ディズニー 混雑 月別 入園者数 9月; Tokyo Disney Resort monthly attendance seasonality crowd calendar September; 東京ディズニーリゾート 月別 入園者数 推移 9月 年間; 舞浜ラボ 9月 入園者数 月別 指数 ディズニー

- `https://maihama-lab.com/column/tdr-crowd-forecast-september/` -> **live_dated** (page date 2026-10-05); points raw/verified 15/14
  - p19 Tokyo Disneyland monthly congestion index for September (baseline from past actu = **39** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 9月 \| 39 \| 47 \| 年間2番目に短い。ハロウィーンは月後半だけ \|"
  - p20 Tokyo DisneySea monthly congestion index for September (baseline from past actua = **47** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 9月 \| 39 \| 47 \| 年間2番目に短い。ハロウィーンは月後半だけ \|"
  - p21 Tokyo Disneyland monthly congestion index for October (baseline) = **63** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 10月 \| 63 \| 61 \| ハロウィーン本番。指数が一気に上がる \|"
  - p22 Tokyo DisneySea monthly congestion index for October (baseline) = **61** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 10月 \| 63 \| 61 \| ハロウィーン本番。指数が一気に上がる \|"
  - p23 Tokyo Disneyland monthly congestion index for July (baseline, lowest month) = **26** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 7月 \| 26 \| 35 \| 年間で最も待ち時間が短い \|"
  - p24 Tokyo DisneySea monthly congestion index for July (baseline) = **35** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 7月 \| 26 \| 35 \| 年間で最も待ち時間が短い \|"
  - p25 Tokyo Disneyland monthly congestion index for November (baseline, highest month) = **75** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 11月 \| 75 \| 79 \| 年間1位。クリスマス開幕で急上昇 \|"
  - p26 Tokyo DisneySea monthly congestion index for November (baseline, highest month) = **79** congestion index (0–100, wait-time based) (2020-01-01..2026-07-31) [keep: ] quote: "\| 11月 \| 75 \| 79 \| 年間1位。クリスマス開幕で急上昇 \|"
  - p27 Tokyo Disneyland September congestion index, 2025 actual = **40** congestion index (0–100, wait-time based) (2025-09-01..2025-09-30) [keep: ] quote: "2025年実績ではランドが9月「40」から10月「68」へ70%上昇しました。"
  - p28 Tokyo DisneySea September congestion index, 2025 actual = **51** congestion index (0–100, wait-time based) (2025-09-01..2025-09-30) [keep: ] quote: "この伸び率を2025年9月の実績(ランド「40」/シー「51」)に掛けると、ランド約「49」・シー約「61」という数字が出ます。"
  - p29 Tokyo Disneyland September congestion index, 2026 reference estimate (2025 Septe = **49** congestion index (0–100, wait-time based) (2026-09-01..2026-09-30) [keep: ] quote: "この伸び率を2025年9月の実績(ランド「40」/シー「51」)に掛けると、ランド約「49」・シー約「61」という数字が出ます。"
  - p30 Tokyo DisneySea September congestion index, 2026 reference estimate (2025 Septem = **61** congestion index (0–100, wait-time based) (2026-09-01..2026-09-30) [keep: ] quote: "この伸び率を2025年9月の実績(ランド「40」/シー「51」)に掛けると、ランド約「49」・シー約「61」という数字が出ます。"
  - p31 Tokyo Disneyland Jan–Jun 2026 vs 2025 growth multiplier = **1.21** ratio (multiple) (2026-01-01..2026-06-30) [keep: ] quote: "2026年1〜6月と、2025年の同じ1〜6月を突き合わせて伸び率を出すと、ランド約1.21倍・シー約1.20倍でした。"
  - p32 Tokyo DisneySea Jan–Jun 2026 vs 2025 growth multiplier = **1.2** ratio (multiple) (2026-01-01..2026-06-30) [keep: ] quote: "2026年1〜6月と、2025年の同じ1〜6月を突き合わせて伸び率を出すと、ランド約1.21倍・シー約1.20倍でした。"
- `https://castel.jp/p/5870` -> **live_dated** (page date 2026-10-02); points raw/verified 15/5
  - p33 Actual annual admissions Apr 2025–Mar 2026, both parks = **27,530,000** people per year (2025-04-01..2026-03-31) [DISCARD: Duplicate of p2/p17 (27.53M FY2025 admissions).] quote: "実際、2025年4月〜2026年3月の1年間の入園者数は2,753万人で、1日1パークあたり平均3万7千人でした。"
  - p34 Pre-COVID normal daily admissions per park (over) = **40,000** people per park per day (..) [keep: ] quote: "コロナ前(通常時)は、1日あたり40,000人超が入園していたことになります。"
  - p35 Pre-COVID Tokyo Disneyland admission-restriction threshold (lower bound) = **60,000** people per day (..) [keep: ] quote: "・ディズニーランド:60,000人~70,000人"
  - p36 Pre-COVID Tokyo Disneyland admission-restriction threshold (upper bound) = **70,000** people per day (..) [keep: ] quote: "・ディズニーランド:60,000人~70,000人"
  - p37 Pre-COVID Tokyo DisneySea admission-restriction threshold (lower bound) = **40,000** people per day (..) [keep: ] quote: "・ディズニーシー:40,000人~50,000人"
- `https://www.olc.co.jp/ja/ir/library/annual/main/018/teaserItems1/0/file/integrated_2025_ja.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://disneyblog.com/calendar/tokyo-disney-resort/september/` -> **live_dated** (page date 2026-10-17); points raw/verified 2/0
- dropped by code checks: 13 (period_end 2026-10-31 after as_of: 3; period_end 2026-11-30 after as_of: 2; period_end 2026-12-31 after as_of: 4; period_end 2027-03-31 after as_of: 1; number: CJK numerals (e.g. 三百, 1千) are not supported: 3)

### d4 [forecasts_markets] Equity analyst / Oriental Land guidance

Hypothesis: Oriental Land FY2026 guidance and analyst forecasts for attendance and park revenue, combined with a September revenue or attendance share, constrain the monthly figure.

Queries issued by the searcher: Oriental Land FY2026 guidance attendance operating revenue forecast; オリエンタルランド 2026年3月期 入園者数 見通し; 東京ディズニーリゾート 入園者数 月別 9月 過去 データ; オリエンタルランド 四半期 入園者数 第2四半期 7-9月 2025年 何万人

- `https://stockanalysis.com/quote/tyo/4661/transcripts/406226-q4-2026/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/10
  - p38 Oriental Land theme park segment net sales, FY ended March 2026 (actual) = **568,300,000,000** JPY (2025-04-01..2026-03-31) [keep: ] quote: "net sales for the theme park segment increased by JPY 16.2 billion to JPY 568.3 billion"
  - p39 Oriental Land theme park segment net sales increase, FY ended March 2026 = **16,200,000,000** JPY (2025-04-01..2026-03-31) [keep: ] quote: "net sales for the theme park segment increased by JPY 16.2 billion to JPY 568.3 billion"
  - p40 Oriental Land net sales per guest, FY ended March 2026 (actual, record high) = **18,403** JPY per guest (2025-04-01..2026-03-31) [keep: ] quote: "Net sales per guest reached a record high of JPY 18,403, driven by factors such as increased revenue from attractions and shows."
  - p41 Oriental Land theme park segment operating profit, FY ended March 2026 (actual) = **130,400,000,000** JPY (2025-04-01..2026-03-31) [keep: ] quote: "Operating profit for the theme park segment decreased by JPY 9.9 billion to JPY 130.4 billion"
  - p42 Oriental Land theme park segment operating profit decrease, FY ended March 2026 = **9,900,000,000** JPY (2025-04-01..2026-03-31) [keep: ] quote: "Operating profit for the theme park segment decreased by JPY 9.9 billion to JPY 130.4 billion"
  - p43 Oriental Land full-year attendance forecast used as comparison base (FY ended Ma = **28,000,000** visitors (attendance) (2025-04-01..2026-03-31) [keep: ] quote: "the trend in attendance compared to the full year forecast of 28 million"
  - p44 Oriental Land Q4 FY ended March 2026 attendance change vs prior year same quarte = **1** % lower (attendance) (2026-01-01..2026-03-31) [keep: ] quote: "For the three-month period of this quarter, the attendance numbers were approximately 1% lower."
  - p45 Oriental Land January attendance change vs prior year (FY ended March 2026) = **5** % lower (attendance) (2026-01-01..2026-01-31) [keep: ] quote: "By month, January was approximately 5% lower."
  - p46 Oriental Land Q4 FY ended March 2026 attendance change vs full-year forecast of  = **5** % lower (attendance) (2026-01-01..2026-03-31) [keep: ] quote: "For the three-month period of this quarter, the attendance numbers were approximately 5% lower."
  - p47 Oriental Land March attendance change vs full-year forecast of 28 million = **6** % lower (attendance) (2026-03-01..2026-03-31) [keep: ] quote: "February was approximately 5% lower, and March was approximately 6% lower."
- `https://finance.biggo.com/quote/4661.T/earnings-call/JP_4661.T_2026-07-31` -> **live_dated** (page date 2026-07-31); points raw/verified 15/15
  - p48 Theme park segment revenue, Oriental Land FY2026 Q1 (Apr-Jun 2026) = **147,400,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Revenue: ¥147.4 billion (up ¥16.1 billion year-on-year)"
  - p49 Theme park segment revenue increase year-on-year, Oriental Land FY2026 Q1 = **16,100,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Revenue: ¥147.4 billion (up ¥16.1 billion year-on-year)"
  - p50 Theme park segment operating profit, Oriental Land FY2026 Q1 = **37,800,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Operating Profit: ¥37.8 billion (up ¥8.5 billion year-on-year)"
  - p51 Theme park attendance growth year-on-year, Oriental Land FY2026 Q1 = **7** percent (2026-04-01..2026-06-30) [keep: ] quote: "Attendance: Up approximately 7% year-on-year. By month: April +4%, May +13%, June +3%."
  - p52 Theme park attendance growth year-on-year, April 2026 = **4** percent (2026-04-01..2026-04-30) [keep: ] quote: "Attendance: Up approximately 7% year-on-year. By month: April +4%, May +13%, June +3%."
  - p53 Theme park attendance growth year-on-year, May 2026 = **13** percent (2026-05-01..2026-05-31) [keep: ] quote: "Attendance: Up approximately 7% year-on-year. By month: April +4%, May +13%, June +3%."
  - p54 Theme park attendance growth year-on-year, June 2026 = **3** percent (2026-06-01..2026-06-30) [keep: ] quote: "Attendance: Up approximately 7% year-on-year. By month: April +4%, May +13%, June +3%."
  - p55 Per-guest spending growth year-on-year, Oriental Land FY2026 Q1 = **5** percent (2026-04-01..2026-06-30) [keep: ] quote: "Per-Guest Spending: Up approximately 5% year-on-year."
  - p56 Hotel segment revenue, Oriental Land FY2026 Q1 = **29,200,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Revenue: ¥29.2 billion (up ¥0.7 billion year-on-year), a record high."
  - p57 Hotel segment operating profit, Oriental Land FY2026 Q1 = **9,200,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Operating Profit: ¥9.2 billion, a record high."
  - p58 Hotel occupancy rate, Oriental Land FY2026 Q1 = **95.2** percent (2026-04-01..2026-06-30) [keep: ] quote: "Occupancy Rate: 95.2% (up 1.2 percentage points year-on-year)"
  - p59 Hotel average daily rate, Oriental Land FY2026 Q1 = **67,036** yen (2026-04-01..2026-06-30) [keep: ] quote: "Average Daily Rate: ¥67,036 (up ¥502 year-on-year)"
  - p60 Other businesses operating profit, Oriental Land FY2026 Q1 = **500,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "Operating profit was ¥0.5 billion (up ¥0.3 billion year-on-year)."
  - p61 Attendance excess over guidance, Oriental Land FY2026 Q1 = **3** percent (2026-04-01..2026-06-30) [keep: ] quote: "Attendance exceeded guidance by approximately 3% (April roughly flat, May +5%, June +4%)."
  - p62 Per-guest spending excess over guidance, Oriental Land FY2026 Q1 = **4** percent (2026-04-01..2026-06-30) [keep: ] quote: "Per-guest spending exceeded guidance by approximately 4%."
- `https://www2.jpx.co.jp/disc/46610/140120191001403629.pdf` -> **live_dated** (page date 2019-10-01); points raw/verified 8/1
  - p63 Year-on-year ratio of combined first-half FY2019 attendance to prior-year same p = **101** percent (2019-04-01..2019-09-30) [keep: ] quote: "15,735 千人(前年同期比 101.4% 218 千人増)"
- `https://dotcom-edge-prod.ind7f52b.eas.morningstar.com/company-reports/1477626-oriental-land-earnings-cut-fair-value-25-on-slower-margin-recovery-share` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 12 (period_end 2027-03-31 after as_of: 5; scale word 'thousand' not supported by quote or table header: 7)

### d5 [capacity_consumption] Operations / capacity analyst

Hypothesis: Daily attendance is bounded by park capacity and realised utilisation; September low-season utilisation times combined capacity of both parks times 30 days gives a constraint and a route to the daily average.

Queries issued by the searcher: Tokyo Disneyland capacity daily visitors 65,000; Tokyo DisneySea maximum capacity daily admissions; Oriental Land FY2024 attendance 30 million two parks results briefing; TEA AECOM 2024 theme index Tokyo Disneyland Tokyo DisneySea attendance 2024

- `https://www.olc.co.jp/en/ir/library/annual/main/01111111112/teaserItems2/010/linkList/0/link/integrated_2025_en_07.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://castel.jp/p/6076` -> **live_dated** (page date 2022-06-29); points raw/verified 15/3
  - p64 Daily admission cap per park during emergency declaration (Jan–Mar 21, 2021) = **5,000** visitors per day per park (2021-01-01..2021-03-21) [keep: Kept only as a COVID-era capacity bound; not usable as a September 2026 level.] quote: "1パークにつき、1日5,000人に絞って営業を予定しているそうです。"
  - p65 Both parks combined average daily admissions, FY2018 = **89,200** visitors per day (both parks combined) (2018-04-01..2019-03-31) [keep: ] quote: "2018年度:1日平均89,200人"
  - p66 Both parks combined average daily admissions, FY2019 = **87,111** visitors per day (both parks combined) (2019-04-01..2020-03-31) [keep: ] quote: "2019年度:1日平均87,111人"
- `https://baotintuc.vn/the-gioi/cong-vien-chu-de-noi-tieng-tokyo-disney-gap-kho-khan-trong-viec-thu-hut-khach-20250822110041492.htm` -> **live_dated** (page date 2025-08-22); points raw/verified 15/0
- `https://wdwnt.com/2022/02/tokyo-disney-resort-increases-capacity-to-50-as-japan-eyes-quasi-emergency-extension/` -> **live_dated** (page date 2022-02-28); points raw/verified 5/0
- dropped by code checks: 32 (number: more than one number in value_as_written: 10; period_end missing or unparseable: 18; scale word 'billion' not supported by quote or table header: 2; scale word 'million' not supported by quote or table header: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 1)

### d6 [physical_flow] Transport and access data

Hypothesis: Rail and bus passenger flows to Maihama Station (Keiyo Line, Disney Resort Line) in September 2026, converted via the share of park visitors arriving by each mode, provide an independent physical-flow estimate of daily admissions.

Queries issued by the searcher: 舞浜駅 乗降客数 月別; Maihama Station passenger numbers monthly JR East Keiyo Line; 舞浜駅 乗車人員 月別 浦安市 統計 9月; 東京ディズニーリゾート 来園者 交通手段 割合 電車 舞浜駅 何%

- `https://www.pref.chiba.lg.jp/koukei/tetsudou/documents/h30jr.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.weblio.jp/content/%E8%88%9E%E6%B5%9C%E9%A7%85` -> **live_dated** (page date 2026-08-08); points raw/verified 13/10
  - p67 JR East Maihama Station FY2024 daily average passengers (boarding only, excludin = **79,403** people per day (2024-04-01..2025-03-31) [keep: ] quote: "乗車人員 -統計年度- \| 79,403人/日(降車客含まず) -2024年-"
  - p68 JR East Maihama Station FY2024 daily average passengers (boarding only) in usage = **79,403** people per day (2024-04-01..2025-03-31) [DISCARD: Duplicate of p67/p155 (same FY2024 Maihama boarding figure).] quote: "2024年度(令和6年度)の1日平均乗車人員は79,403人で"
  - p69 JR East Maihama Station FY2024 non-commuter (定期外) daily average passengers = **49,553** people per day (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
  - p70 JR East Maihama Station FY2024 commuter (定期) daily average passengers = **29,849** people per day (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
  - p71 JR East Maihama Station FY2023 daily average passengers (total) = **76,156** people per day (2023-04-01..2024-03-31) [keep: ] quote: "\| 2023年(令和5年) \| 48,331 \| 27,825 \| 76,156 \| 19.2% \| 50位 \| [JR 26] \| [県 33] \| [市 5] \|"
  - p72 JR East Maihama Station FY2022 daily average passengers (total) = **63,906** people per day (2022-04-01..2023-03-31) [keep: ] quote: "\| 2022年(令和4年) \| 38,976 \| 24,930 \| 63,906 \| 36.5% \| 58位 \| [JR 25] \| [県 32] \| [市 4] \|"
  - p73 JR East Maihama Station FY2019 (pre-COVID) daily average passengers (total) = **78,811** people per day (2019-04-01..2020-03-31) [keep: ] quote: "\| 2019年(令和元年) \| 48,858 \| 29,953 \| 78,811 \| -5.2% \| 58位 \| [JR 22] \| [県 29] \| \|"
  - p74 JR East Maihama Station FY2018 daily average passengers (total) = **83,157** people per day (2018-04-01..2019-03-31) [keep: ] quote: "\| 2018年(平成30年) \| 53,364 \| 29,793 \| 83,157 \| 5.2% \| 55位 \| [JR 21] \| [県 28] \| \|"
  - p75 JR East Maihama Station FY2020 daily average passengers (total, COVID trough) = **38,395** people per day (2020-04-01..2021-03-31) [keep: Kept as a COVID-trough reference for the Maihama flow series; not used in the estimate.] quote: "\| 2020年(令和2年) \| 17,610 \| 20,785 \| 38,395 \| -51.3% \| 93位 \| [JR 23] \| [県 30] \| [市 2] \|"
  - p76 JR East Maihama Station FY2024 year-on-year change in daily average passengers = **4.3** percent (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
- `https://www.gleasin.jp/station/station-d75d5f70af-004055-jr-east/` -> **live_dated** (page date 2026-10-01); points raw/verified 4/0
- `https://nlab.itmedia.co.jp/research/articles/2942389/4/` -> **live_dated** (page date 2024-08-30); points raw/verified 7/7
  - p77 JR Keiyo Line Maihama Station average daily boarding passengers, FY2023 = **76,156** people per day (2023-04-01..2024-03-31) [keep: ] quote: "第2位は千葉県浦安市にある「舞浜」駅で、1日平均の乗車人員は7万6156人でした。"
  - p78 JR Keiyo Line Maihama Station average daily boarding passengers, FY2023 (ranking = **76,156** people per day (2023-04-01..2024-03-31) [DISCARD: Duplicate of p71/p159 (FY2023 Maihama boarding 76,156).] quote: "第2位:舞浜(7万6156人)"
  - p79 JR Keiyo Line Tokyo Station average daily boarding passengers, FY2023 = **403,831** people per day (2023-04-01..2024-03-31) [keep: Kept as a Keiyo Line comparison station; not used directly.] quote: "第1位:東京(40万3831人)"
  - p80 JR Keiyo Line Shinkiba Station average daily boarding passengers, FY2023 = **67,206** people per day (2023-04-01..2024-03-31) [keep: Kept as a Keiyo Line comparison station; not used directly.] quote: "第3位:新木場(6万7206人)"
  - p81 JR Keiyo Line Kaihin-Makuhari Station average daily boarding passengers, FY2023 = **55,196** people per day (2023-04-01..2024-03-31) [keep: Kept as a Keiyo Line comparison station; not used directly.] quote: "第4位:海浜幕張(5万5196人)"
  - p82 JR Keiyo Line Shin-Urayasu Station average daily boarding passengers, FY2023 = **50,380** people per day (2023-04-01..2024-03-31) [keep: Kept as a Keiyo Line comparison station; not used directly.] quote: "第5位:新浦安(5万380人)"
  - p83 JR Keiyo Line Soga Station average daily boarding passengers, FY2023 = **31,328** people per day (2023-04-01..2024-03-31) [keep: Kept as a Keiyo Line comparison station; not used directly.] quote: "第6位:蘇我(3万1328人)"
- dropped by code checks: 7 (value_as_written not in quote as a whole number: 1; period_end missing or unparseable: 6)

### d7 [shocks] Event and calendar analyst

Hypothesis: September 2026 attendance is affected by specific events (Halloween event start, typhoon closures, new attraction openings, price changes) that shift the seasonal share; identifying these adjusts the base-rate route.

Queries issued by the searcher: Tokyo Disney Halloween 2026 dates; ディズニー ハロウィン 2026 期間; Oriental Land attendance fiscal 2025 Tokyo Disneyland DisneySea annual visitors million; 東京ディズニーリゾート 入園者数 2025年度 延べ オリエンタルランド

- `https://www.olc.co.jp/ja/ir/olc/group04.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.jiji.com/jc/article?k=2025103001018` -> **live_dated** (page date 2025-10-30); points raw/verified 6/3
  - p84 Oriental Land interim consolidated revenue, FY2025 first half (Apr-Sep 2025), ye = **6.4** percent (2025-04-01..2025-09-30) [keep: ] quote: "売上高が前年同期比6.4%増の3161億円と、中間決算として過去最高を更新した。"
  - p85 Tokyo Disney Resort first-half park admissions (visitors), FY2025 (Apr-Sep 2025) = **0.4** percent (2025-04-01..2025-09-30) [keep: ] quote: "上半期の入園者数は0.4%増の1225万人"
  - p86 Tokyo Disney Resort revenue per visitor, FY2025 first half (Apr-Sep 2025), year- = **5.2** percent (2025-04-01..2025-09-30) [keep: ] quote: "1人当たり売上高は5.2%増の1万8196円だった。"
- `https://www.tokyodisneyresort.jp/en/topics/event/halloween2026/tdl.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://finance.biggo.com/news/89e0ec45-0d6f-4894-9ba9-4dfa60852250` -> **live_dated** (page date 2026-07-09); points raw/verified 15/8
  - p87 Combined annual attendance at Tokyo Disneyland and Tokyo DisneySea, fiscal 2018  = **32,560,000** visitors (2017-04-01..2018-03-31) [keep: ] quote: "Combined annual attendance at Tokyo Disneyland and Tokyo DisneySea peaked at 32.56 million in fiscal 2018, the park's 35th anniversary year"
  - p88 TDR per-guest spending, fiscal 2018 = **11,815** yen per guest (2017-04-01..2018-03-31) [keep: Kept as per-guest spending history; not used directly.] quote: "TDR's per-guest spending from ¥11,815 in fiscal 2018 to ¥18,403 in fiscal 2025"
  - p89 TDR per-guest spending, fiscal 2025 = **18,403** yen per guest (2025-04-01..2026-03-31) [DISCARD: Duplicate of p40 (FY2025 per-guest spending ¥18,403).] quote: "TDR's per-guest spending from ¥11,815 in fiscal 2018 to ¥18,403 in fiscal 2025"
  - p90 Adult one-day passport price, 2019 = **7,500** yen (2019-01-01..2019-12-31) [keep: Kept as price-history context; not used directly.] quote: "An adult one-day passport, priced at ¥7,500 in 2019, now reaches a ceiling of ¥10,900."
  - p91 Junior (ages 12-17) one-day passport price, 2019 = **6,400** yen (2019-01-01..2019-12-31) [keep: Kept as price-history context; not used directly.] quote: "A one-day passport for junior visitors (ages 12-17), priced at ¥6,400 in 2019, now carries a minimum price of ¥6,600"
  - p92 Visitors under 18 at TDR, fiscal 2018 = **9,000,000** visitors (2017-04-01..2018-03-31) [keep: Kept as demographic context; not used directly.] quote: "After exceeding 9 million in fiscal 2018, the figure dropped to 7.72 million in fiscal 2019"
  - p93 Visitors under 18 at TDR, fiscal 2019 = **7,720,000** visitors (2018-04-01..2019-03-31) [keep: Kept as demographic context; not used directly.] quote: "After exceeding 9 million in fiscal 2018, the figure dropped to 7.72 million in fiscal 2019"
  - p94 Visitors under 18 at TDR, fiscal 2025 = **6,720,000** visitors (2025-04-01..2026-03-31) [keep: Kept as demographic context; not used directly.] quote: "reaching just 6.72 million in fiscal 2025"
- dropped by code checks: 10 (number: value_as_written is only part of a larger CJK number in the quote: 1; number: unknown scale word 'ten thousand': 1; value_as_written not in quote as a whole number: 1; period_end missing or unparseable: 6; period_end 2028-12-31 after as_of: 1)

### d8 [attention] Digital attention analyst

Hypothesis: Search interest, app downloads, and wait-time aggregator data for September 2026 relative to annual baseline can proxy relative attendance and help calibrate the September share, though without a bridge it is only contextual.

Queries issued by the searcher: Tokyo Disney wait times September 2026 crowd level; 東京ディズニー 待ち時間 9月 2026 混雑; thrill-data Tokyo DisneySea September 2026 average wait by month; Tokyo Disney Resort September 2026 attendance visitors decline news Oriental Land

- `https://www.thrill-data.com/trip-planning/crowd-calendar/tokyo-disneysea/calendar/2026/1547` -> **live_dated** (page date 2026-08-14); points raw/verified 0/0
- `https://www.thrill-data.com/waits/park/dis/tokyo-disneyland/2026/09/10` -> **live_dated** (page date 2026-09-10); points raw/verified 0/0
- `https://magic-tips.app/ja/konzatsu-calendar/tokyo-disney-resort/2026/09` -> **live_dated** (page date 2026-10-12); points raw/verified 15/7
  - p95 September 2026 average observed congestion score for Tokyo Disney Resort (both p = **75** percent congestion score (wait-time based, not visitors) (2026-09-01..2026-09-30) [keep: ] quote: "9月の平均混雑度(実測)は75%でした。その月に実際に表示された待ち時間から算出しています。"
  - p96 Number of days in September 2026 with congestion below 50% at Tokyo Disney Resor = **3** days (2026-09-01..2026-09-30) [keep: ] quote: "月間30日中、3日が50%未満です。"
  - p97 Total days in September 2026 covered by the Tokyo Disney Resort congestion calen = **30** days (2026-09-01..2026-09-30) [DISCARD: Trivial calendar constant (30 days in September) already supplied by code as k_days_target.] quote: "月間30日中、3日が50%未満です。"
  - p98 Least crowded day in September 2026 at Tokyo Disney Resort (Sept 6) congestion s = **35** percent capacity (congestion score) (2026-09-06..2026-09-06) [keep: ] quote: "具体的には、9月2026の最良の日は9月6日(35%容量)と9月7日(37%)で、最も混雑しているのは9月22日(96%)と9月23日(94%)です。"
  - p99 Second least crowded day in September 2026 at Tokyo Disney Resort (Sept 7) conge = **37** percent capacity (congestion score) (2026-09-07..2026-09-07) [keep: ] quote: "具体的には、9月2026の最良の日は9月6日(35%容量)と9月7日(37%)で、最も混雑しているのは9月22日(96%)と9月23日(94%)です。"
  - p100 Most crowded day in September 2026 at Tokyo Disney Resort (Sept 22) congestion s = **96** percent capacity (congestion score) (2026-09-22..2026-09-22) [keep: ] quote: "具体的には、9月2026の最良の日は9月6日(35%容量)と9月7日(37%)で、最も混雑しているのは9月22日(96%)と9月23日(94%)です。"
  - p101 Second most crowded day in September 2026 at Tokyo Disney Resort (Sept 23) conge = **94** percent capacity (congestion score) (2026-09-23..2026-09-23) [keep: ] quote: "具体的には、9月2026の最良の日は9月6日(35%容量)と9月7日(37%)で、最も混雑しているのは9月22日(96%)と9月23日(94%)です。"
- `https://disneyreal.asumirai.info/monthly/disneyland-forecast-2026-9.html` -> **dropped** (live page dated 2026-10-18 > as_of); points raw/verified -/-
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b1 [related_series] Oriental Land monthly or quarterly attendance disclosure for Jul–Sep 2026

Hypothesis: If Oriental Land's Q2 FY2026 (Jul–Sep 2026) results or a press report give attendance growth for the quarter or for September specifically, it would replace the Q1 +7% y/y anchor (p51) with a same-quarter signal, which is the single largest uncertainty in the y/y-scaling route.

Queries issued by the searcher: オリエンタルランド 2026年 第2四半期 入園者数; Tokyo Disney Resort attendance September 2026; TEA AECOM 2025 theme index Tokyo Disneyland Tokyo DisneySea attendance 2025; オリエンタルランド 2026年3月期 通期決算 入園者数 3,000万人

- `https://stockanalysis.com/quote/tyo/4661/transcripts/357162-q2-2026/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p102 Tokyo Disney Resort attendance change y/y, September (Theme Park segment, month  = **2** % (y/y change in attendance) (2025-09-01..2025-09-30) [keep: ] quote: "Month by month, July was approximately 9% lower, August was approximately 15% higher, and September was approximately 2% lower."
  - p103 Tokyo Disney Resort attendance change y/y, Q2 three-month period (Jul–Sep) = **1** % (y/y change in attendance) (2025-07-01..2025-09-30) [keep: ] quote: "Over the three-month period, it was approximately 1% higher."
  - p104 Tokyo Disney Resort attendance change y/y, July = **9** % (y/y change in attendance) (2025-07-01..2025-07-31) [keep: ] quote: "Month by month, July was approximately 9% lower, August was approximately 15% higher, and September was approximately 2% lower."
  - p105 Tokyo Disney Resort attendance change y/y, August = **15** % (y/y change in attendance) (2025-08-01..2025-08-31) [keep: ] quote: "Month by month, July was approximately 9% lower, August was approximately 15% higher, and September was approximately 2% lower."
  - p106 Tokyo Disney Resort attendance vs forecast, September (month) = **4** % (below forecast, attendance) (2025-09-01..2025-09-30) [keep: ] quote: "By month, July was about 11% below. August was about 10% above. September was about 4% below."
  - p107 Tokyo Disney Resort attendance vs forecast, Q2 three-month period = **2** % (below forecast, attendance) (2025-07-01..2025-09-30) [keep: ] quote: "Over the three-month second quarter period, attendance was approximately 2% below our forecast."
  - p108 Tokyo Disney Resort attendance vs forecast, July = **11** % (below forecast, attendance) (2025-07-01..2025-07-31) [keep: ] quote: "By month, July was about 11% below. August was about 10% above. September was about 4% below."
  - p109 Tokyo Disney Resort attendance vs forecast, August = **10** % (above forecast, attendance) (2025-08-01..2025-08-31) [keep: ] quote: "By month, July was about 11% below. August was about 10% above. September was about 4% below."
  - p110 Theme Park segment net sales, first half FY ending March 2026 = **251,700,000,000** JPY (2025-04-01..2025-09-30) [keep: ] quote: "Net sales for the Theme Park segment increased by JPY 12.9 billion to JPY 251.7 billion."
  - p111 Theme Park segment net sales increase y/y, first half FY ending March 2026 = **12,900,000,000** JPY (2025-04-01..2025-09-30) [keep: ] quote: "Net sales for the Theme Park segment increased by JPY 12.9 billion to JPY 251.7 billion."
  - p112 Theme Park segment operating profit, first half FY ending March 2026 = **49,700,000,000** JPY (2025-04-01..2025-09-30) [keep: ] quote: "Operating profit of the Theme Park segment decreased by JPY 0.2 billion to JPY 49.7 billion."
  - p113 Disney Hotels occupancy rate, first half FY ending March 2026 = **92.3** % (occupancy rate) (2025-04-01..2025-09-30) [keep: ] quote: "the occupancy rate at Disney Hotels decreased by 1% to 92.3% due to a decline in reservations made through Vacation Packages"
  - p114 Disney Hotels average charge per room, first half FY ending March 2026 = **66,806** JPY per room (2025-04-01..2025-09-30) [keep: ] quote: "the average charge per room increased by JPY 5,350 to JPY 66,806"
  - p115 Hotel business segment net sales, first half FY ending March 2026 = **56,100,000,000** JPY (2025-04-01..2025-09-30) [keep: ] quote: "The hotel business segment saw net sales increase by JPY 5.8 billion to JPY 56.1 billion"
  - p116 Theme Park segment net sales vs forecast, first half FY ending March 2026 = **900,000,000** JPY (above projection) (2025-04-01..2025-09-30) [keep: ] quote: "Net sales for the Theme Park segment exceeded projections by JPY 0.9 billion."
- `https://finance.logmi.jp/articles/382975` -> **live_dated** (page date 2025-11-06); points raw/verified 15/4
  - p117 Oriental Land H1 FY2026 Disney hotel occupancy rate = **92.3** percent (2025-04-01..2025-09-30) [keep: ] quote: "上半期のディズニーホテルにおける客室稼働率は、東京ディズニーリゾート・バケーションパッケージ経由の予約減少により前年同期比1ポイント減の92.3パーセント"
  - p118 Oriental Land H1 FY2026 Disney hotel occupancy rate change y/y = **1** percentage points (2025-04-01..2025-09-30) [keep: ] quote: "前年同期比1ポイント減の92.3パーセント"
  - p119 Oriental Land H1 FY2026 Disney hotel average room rate = **66,806** 円 (yen) (2025-04-01..2025-09-30) [keep: ] quote: "平均客室単価は前年同期比5,350円増の6万6,806円でした。"
  - p120 Oriental Land H1 FY2026 Disney hotel average room rate increase y/y = **5,350** 円 (yen) (2025-04-01..2025-09-30) [keep: ] quote: "平均客室単価は前年同期比5,350円増の6万6,806円でした。"
- `https://www.jiji.com/jc/article?k=2026073001010&g=eco` -> **live_dated** (page date 2026-07-30); points raw/verified 5/4
  - p121 Oriental Land consolidated sales, Apr–Jun 2026 quarter, y/y change = **10.4** % (2026-04-01..2026-06-30) [keep: ] quote: "2026年4~6月期連結決算は、売上高が前年同期比10.4%増の1807億円"
  - p122 Oriental Land consolidated net profit, Apr–Jun 2026 quarter, y/y change = **50.3** % (2026-04-01..2026-06-30) [keep: ] quote: "純利益が50.3%増の412億9700万円となり"
  - p123 Oriental Land consolidated net profit, Apr–Jun 2026 quarter = **41,297,000,000** yen (2026-04-01..2026-06-30) [keep: ] quote: "純利益が50.3%増の412億9700万円となり、いずれも4~6月期として過去最高を更新した。"
  - p124 Tokyo DisneySea 25th anniversary event start month = **4** month (April) (2026-04-01..2026-04-30) [keep: ] quote: "4月に始まった東京ディズニーシーの開園25周年イベントの効果で入園者数が増加。"
- `https://www.okasan.co.jp/market/report/20240509_4661.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 12 (number: value_as_written is only part of a larger CJK number in the quote: 12)

### b2 [base_rates] September share of annual attendance at Tokyo Disney Resort

Hypothesis: A published monthly or seasonal attendance split (even for a prior year) would convert the FY2025 annual total (p17) directly into a September monthly total, removing the need to infer the September share from congestion indices alone.

Queries issued by the searcher: 東京ディズニーリゾート 月別 入園者数; TDR monthly attendance share September Tokyo Disneyland attendance by month; ディズニーランド入場者数の推移を年別で読むコツ 月別 aruru; オリエンタルランド 月別 入園者数 9月 割合 年間

- `https://queue-times.com/en-US/parks/16/stats` -> **live_dated** (page date 2026-01-01); points raw/verified 15/15
  - p125 Disneyland average crowd level in September (monthly share proxy, not Tokyo) = **35** percent crowd level (..) [keep: ] quote: "\| Sep \| 35 \|"
  - p126 Disneyland average crowd level in August = **39** percent crowd level (..) [keep: ] quote: "\| Aug \| 39 \|"
  - p127 Disneyland average crowd level in April (busiest month) = **60** percent crowd level (..) [keep: ] quote: "\| Apr \| 60 \|"
  - p128 Disneyland average crowd level in January = **46** percent crowd level (..) [keep: ] quote: "\| Jan \| 46 \|"
  - p129 Disneyland average crowd level in February = **52** percent crowd level (..) [keep: ] quote: "\| Feb \| 52 \|"
  - p130 Disneyland average crowd level in March = **59** percent crowd level (..) [keep: ] quote: "\| Mar \| 59 \|"
  - p131 Disneyland average crowd level in May = **59** percent crowd level (..) [keep: ] quote: "\| May \| 59 \|"
  - p132 Disneyland average crowd level in June = **50** percent crowd level (..) [keep: ] quote: "\| Jun \| 50 \|"
  - p133 Disneyland average crowd level in July = **48** percent crowd level (..) [keep: ] quote: "\| Jul \| 48 \|"
  - p134 Disneyland average crowd level in October = **58** percent crowd level (..) [keep: ] quote: "\| Oct \| 58 \|"
  - p135 Disneyland average crowd level in November = **50** percent crowd level (..) [keep: ] quote: "\| Nov \| 50 \|"
  - p136 Disneyland average crowd level in December = **53** percent crowd level (..) [keep: ] quote: "\| Dec \| 53 \|"
  - p137 Disneyland 2026 year-to-date average crowd level = **34** percent crowd level (2026-01-01..) [keep: ] quote: "So far in 2026, Disneyland is running 7 percentage points quieter than at the same point in 2025 (34% compared with 41%)."
  - p138 Disneyland 2025 same-point average crowd level = **41** percent crowd level (2025-01-01..) [keep: ] quote: "So far in 2026, Disneyland is running 7 percentage points quieter than at the same point in 2025 (34% compared with 41%)."
  - p139 Disneyland busiest full year on record average crowd level (2022) = **74** percent crowd level (2022-01-01..2022-12-31) [keep: ] quote: "Of the full years on record, 2022 was the busiest, averaging 74%."
- `https://aruru.co.jp/trip/2025/10/page/20/` -> **live_dated** (page date 2025-10-01); points raw/verified 0/0
- `https://ryderush.com/parks/tokyo-disneyland/crowd-calendar/2026/` -> **live_dated** (page date 2010-08-02); points raw/verified 0/0
- `https://castel.jp/p/5169` -> **live_dated** (page date 2020-03-23); points raw/verified 15/15
  - p140 Tokyo Disney Resort annual admissions, FY2019 (calendar year 2019) = **29,008,000** people (admissions) (2019-01-01..2019-12-31) [keep: ] quote: "\| 2019年 \| 29,008,000人 \| 7,500円 \| 消費税10% \|"
  - p141 Tokyo Disney Resort annual admissions, calendar year 2018 (record high) = **32,558,000** people (admissions) (2018-01-01..2018-12-31) [keep: ] quote: "\| 2018年 \| 32,558,000人 \| 7,400円 \| 年パス使用不可日導入/TDL35周年 \|"
  - p142 Tokyo Disney Resort annual admissions, calendar year 2020 (COVID closures) = **7,560,000** people (admissions) (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 \| 7,560,000人 \| 8,200円 \| コロナ休園/TDL新エリア開業 \|"
  - p143 Tokyo Disney Resort annual admissions, calendar year 2017 = **30,100,000** people (admissions) (2017-01-01..2017-12-31) [keep: ] quote: "\| 2017年 \| 30,100,000人 \| 7,400円 \| - \|"
  - p144 Tokyo Disney Resort annual admissions, calendar year 2016 = **30,004,000** people (admissions) (2016-01-01..2016-12-31) [keep: ] quote: "\| 2016年 \| 30,004,000人 \| 7,400円 \| - \|"
  - p145 Tokyo Disney Resort annual admissions, calendar year 2015 = **30,191,000** people (admissions) (2015-01-01..2015-12-31) [keep: ] quote: "\| 2015年 \| 30,191,000人 \| 6,900円 \| - \|"
  - p146 Tokyo Disney Resort annual admissions, calendar year 2014 = **31,377,000** people (admissions) (2014-01-01..2014-12-31) [keep: ] quote: "\| 2014年 \| 31,377,000人 \| 6,400円 \| 消費税8% \|"
  - p147 Tokyo Disney Resort annual admissions, calendar year 2013 = **31,298,000** people (admissions) (2013-01-01..2013-12-31) [keep: ] quote: "\| 2013年 \| 31,298,000人 \| 6,200円 \| - \|"
  - p148 Tokyo Disney Resort annual admissions, calendar year 2012 = **27,503,000** people (admissions) (2012-01-01..2012-12-31) [keep: ] quote: "\| 2012年 \| 27,503,000人 \| 6,200円 \| - \|"
  - p149 Tokyo Disney Resort annual admissions, calendar year 2011 (Great East Japan Eart = **25,347,000** people (admissions) (2011-01-01..2011-12-31) [keep: ] quote: "\| 2011年 \| 25,347,000人 \| 6,200円 \| 東日本大震災 \|"
  - p150 Tokyo Disney Resort annual admissions, calendar year 2001 (Tokyo DisneySea opene = **22,047,000** people (admissions) (2001-01-01..2001-12-31) [keep: ] quote: "\| 2001年 \| 22,047,000人 \| 5,500円 \| TDSオープン \|"
  - p151 Tokyo Disneyland annual admissions, opening year 1983 = **9,933,000** people (admissions) (1983-01-01..1983-12-31) [keep: ] quote: "\| 1983年 \| 9,933,000人 \| 3,900円 \| TDLオープン \|"
  - p152 Tokyo Disney Resort temporary closure duration due to COVID-19 (months) = **4** months (2020-02-29..2020-06-30) [keep: ] quote: "2020年、新型コロナウイルスの感染拡大により、東京ディズニーリゾートは約4ヶ月の間臨時休園していました。"
  - p153 Oriental Land plan target: annual admissions by 2023 = **30,000,000** people (admissions) (2023-01-01..2023-12-31) [keep: ] quote: "オリエンタルランドの計画は、2023年までに来場者3,000万人達成が目標でしたが、すでに達成し、2018年度は過去最高来場者数を記録しました。"
  - p154 Oriental Land plan: maximum part-time staff to be converted to regular employmen = **4,000** people (staff) (..2023-12-31) [keep: ] quote: "加えて、2023年までに最大4,000人のアルバイトを正規雇用すると発表しました。"

### b3 [physical_flow] Maihama Station September 2026 passenger counts and park-arrival share

Hypothesis: A September 2026 Maihama Station boarding count, combined with the share of park visitors arriving by JR, would give an independent physical-flow estimate to cross-check the attendance-based route and resolve the conflict between the congestion-index sources (p95 vs p29/p30).

Queries issued by the searcher: 舞浜駅 乗車人員 2025年度 1日平均; Tokyo Disney Resort visitor transportation mode share JR train percentage; 舞浜駅 乗車人員 2025年度 1日平均 79,000 JR東日本; 東京ディズニーリゾート 来園者 交通手段 割合 鉄道 舞浜駅 調査

- `https://www.weblio.jp/content/%E8%88%9E%E6%B5%9C%E9%A7%85` -> **live_dated** (page date 2026-08-08); points raw/verified 15/12
  - p155 Maihama Station FY2024 daily average passengers (boarding only, excluding alight = **79,403** people per day (2024-04-01..2025-03-31) [keep: ] quote: "乗車人員 -統計年度- \| 79,403人/日(降車客含まず) -2024年-"
  - p156 Maihama Station FY2024 daily average passengers (JR East ranking statement) = **79,403** people per day (2024-04-01..2025-03-31) [keep: ] quote: "2024年度(令和6年度)の1日平均乗車人員は79,403人で、JR東日本管内では荻窪駅に次いで第50位である"
  - p157 Maihama Station FY2024 non-commuter (定期外) daily average passengers = **49,553** people per day (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
  - p158 Maihama Station FY2024 commuter-pass (定期) daily average passengers = **29,849** people per day (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
  - p159 Maihama Station FY2023 daily average passengers (total) = **76,156** people per day (2023-04-01..2024-03-31) [keep: ] quote: "\| 2023年(令和5年) \| 48,331 \| 27,825 \| 76,156 \| 19.2% \| 50位 \| [JR 26] \| [県 33] \| [市 5] \|"
  - p160 Maihama Station FY2023 non-commuter (定期外) daily average passengers = **48,331** people per day (2023-04-01..2024-03-31) [keep: ] quote: "\| 2023年(令和5年) \| 48,331 \| 27,825 \| 76,156 \| 19.2% \| 50位 \| [JR 26] \| [県 33] \| [市 5] \|"
  - p161 Maihama Station FY2018 daily average passengers (total, peak year) = **83,157** people per day (2018-04-01..2019-03-31) [keep: ] quote: "\| 2018年(平成30年) \| 53,364 \| 29,793 \| 83,157 \| 5.2% \| 55位 \| [JR 21] \| [県 28] \| \|"
  - p162 Maihama Station FY2018 non-commuter (定期外) daily average passengers = **53,364** people per day (2018-04-01..2019-03-31) [keep: ] quote: "\| 2018年(平成30年) \| 53,364 \| 29,793 \| 83,157 \| 5.2% \| 55位 \| [JR 21] \| [県 28] \| \|"
  - p163 Maihama Station FY2019 daily average passengers (total, pre-COVID) = **78,811** people per day (2019-04-01..2020-03-31) [keep: ] quote: "\| 2019年(令和元年) \| 48,858 \| 29,953 \| 78,811 \| -5.2% \| 58位 \| [JR 22] \| [県 29] \| \|"
  - p164 Maihama Station FY2020 daily average passengers (total, COVID trough) = **38,395** people per day (2020-04-01..2021-03-31) [keep: ] quote: "\| 2020年(令和2年) \| 17,610 \| 20,785 \| 38,395 \| -51.3% \| 93位 \| [JR 23] \| [県 30] \| [市 2] \|"
  - p165 Maihama Station FY2022 daily average passengers (total) = **63,906** people per day (2022-04-01..2023-03-31) [keep: ] quote: "\| 2022年(令和4年) \| 38,976 \| 24,930 \| 63,906 \| 36.5% \| 58位 \| [JR 25] \| [県 32] \| [市 4] \|"
  - p166 Maihama Station FY2024 year-on-year change in daily average passengers = **4.3** percent (2024-04-01..2025-03-31) [keep: ] quote: "\| 2024年(令和6年) \| 49,553 \| 29,849 \| 79,403 \| 4.3% \| 50位 \| [JR 1] \| \| [市 6] \|"
- `https://www.pref.chiba.lg.jp/koukei/tetsudou/documents/h30jr.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://news.goo.ne.jp/article/chibatv/region/chibatv-202505180815.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.gleasin.jp/station/station-d75d5f70af-004055-jr-east/` -> **live_dated** (page date 2026-10-01); points raw/verified 10/0
- dropped by code checks: 13 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period_end missing or unparseable: 10; number: value_as_written is only part of a larger CJK number in the quote: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['tokyo disney attendance', 'disneysea visitors', 'theme park attendance']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p2', 'p17', 'p18', 'p33'] All four report the same FY2025 (Apr 2025–Mar 2026) combined annual attendance of 27.53 million; p2/p3 are a Chinese-language news summary, p17/p18/p33 are a Japanese blog citing the same Oriental Lan
- corroborating: ['p2', 'p3'] Level and year-on-year change from the same article; internally consistent (27.53M ≈ 0.1% below prior year).
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16'] Revenue, profit and segment-share figures from one Chinese-language summary of Oriental Land FY2026 results; internally consistent (shares sum to ~95.7% for the four listed segments, amounts match sha
- corroborating: ['p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47'] English-language earnings summary of the same FY2026 results; theme-park segment sales ¥568.3bn and net sales per guest ¥18,403 are consistent with p4/p12 (ticket revenue ¥289.5bn is a subset of segme
- corroborating: ['p48', 'p49', 'p50', '51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62'] Q1 FY2026 (Apr–Jun 2026) results: attendance +7% y/y with monthly detail (+4/+13/+3). This is the most recent hard attendance signal and is the natural anchor for a September 2026 y/y growth factor.
- corroborating: ['p51', 'p61'] Both describe Q1 attendance vs prior year and vs guidance; the +7% y/y and +3% vs guidance are different comparisons, not contradictions.
- corroborating: ['p19', 'p20', 'p27', 'p28', 'p29', 'p30'] Congestion-index baselines and 2025 actuals for September; the 2026 reference estimates (p29/p30) are derived from the 2025 actuals times the Oct uplift, so they are not independent of p27/p28.
- corroborating: ['p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26'] Monthly congestion-index table from one source; September is the second-lowest month, consistent with the qualitative claim in p19/p20.
- corroborating: ['p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101'] September 2026 observed congestion from one aggregator: mean 75%, 3 of 30 days below 50%, extremes 35% (Sep 6) and 96% (Sep 22). Internally consistent; single source.
- conflicting: ['p95', 'p29', 'p30'] The aggregator's observed September 2026 mean congestion (75%) is far above the maihama-lab reference estimate (land 49, sea 61). Different index definitions (percent-of-capacity vs 0–100 relative ind
- corroborating: ['p65', 'p66', 'p34'] Pre-COVID combined daily averages (~87–89k) and per-park >40k are consistent with each other and with the pre-COVID admission-restriction thresholds (p35–p37).
- corroborating: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78'] Maihama Station boarding statistics from JR East-derived tables; p67/p68 are the same FY2024 total, p77/p78 the same FY2023 total. These are boarding-only counts, not park admissions, and include non-
- corroborating: ['p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94'] Historical context on attendance peak, per-guest spending and under-18 visitors; consistent with the FY2025 per-guest figure in p40/p89.
- corroborating: ['p1', 'p85'] First-half FY2025 admissions 12.25 million, +0.4% y/y, reported by two outlets from the same interim disclosure.
- corroborating: ['p63'] FY2019 first-half attendance 15,735 thousand, +1.4% y/y — a pre-COVID seasonal-share reference for the Apr–Sep half.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p2', 'p17', 'p3'] Same FY2025 (Apr 2025–Mar 2026) combined attendance of 27.53M from two independent write-ups; p3 gives the -0.1% y/y change consistent with that level. These are the best annual anchor.
- corroborating: ['p1', 'p85'] Both report Apr–Sep 2025 admissions of 12.25M (+0.4% y/y) — same underlying Oriental Land H1 disclosure, not independent.
- corroborating: ['p2', 'p43'] Actual FY2025 attendance 27.53M vs the 28M full-year forecast base; the ~1.7% shortfall is consistent with p44–p47 monthly misses. p43 is a forecast, usable only as a comparison base, not as actual.
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p61'] Q1 FY2026 monthly y/y growth (+4/+13/+3, ~+7% quarter) from one Oriental Land disclosure; p61 is the same quarter vs guidance, a different comparison, not a contradiction.
- corroborating: ['p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109'] Q2 FY2025 (Jul–Sep 2025) monthly y/y and vs-forecast figures from one analyst call; September 2025 was ~2% lower y/y and ~4% below forecast. This is the same-quarter signal that replaces the Q1 anchor
- corroborating: ['p19', 'p20', 'p27', 'p28', 'p29', 'p30'] Maihama-lab congestion indices: September baseline (39/47), 2025 actual (40/51), and 2026 reference estimate (49/61) derived by applying the Sep→Oct uplift. Internally consistent but all from one mode
- conflicting: ['p95', 'p96', 'p98', 'p99', 'p100', 'p101'] magic-tips reports September 2026 average congestion 75% with only 3 days below 50% and peaks of 96/94% on Sep 22–23 — far above the maihama-lab 2026 reference (49/61). Different congestion scales/def
- corroborating: ['p67', 'p69', 'p70', 'p155', 'p156', 'p157', 'p158'] Duplicate copies of the same JR East FY2024 Maihama Station boarding figure (79,403/day; 49,553 non-commuter + 29,849 commuter). One underlying measurement.
- corroborating: ['p71', 'p72', 'p73', 'p74', 'p75', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165'] Maihama Station annual boarding series FY2018–FY2024; duplicates across two URLs. Shows station flow tracks park attendance but is boarding-only and includes commuters, so needs a conversion to admiss
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p65', 'p66'] Pre-COVID per-park daily admissions (~40k/park normal; caps 60–70k TDL, 40–50k TDS) and FY2018/FY2019 combined daily averages (89,200 / 87,111) are mutually consistent capacity/utilisation context.
- corroborating: ['p140', 'p141', 'p142', 'p143', 'p144', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150', 'p151'] Calendar-year admissions history from one source; useful for scale and seasonality context but not the target period.
- corroborating: ['p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139'] Anaheim Disneyland crowd-level seasonality (Sep lowest at 35, Apr peak 60) — an analogue only, different park and scale; supports September being a low month but cannot be numerically transferred.
- corroborating: ['p48', 'p49', 'p50', 'p121', 'p122', 'p123'] Q1 FY2026 revenue/profit growth (theme park +¥16.1bn; consolidated +10.4% sales, +50.3% net profit) from two write-ups of the same results; consistent with the +7% attendance and +5% per-guest spendin
- corroborating: ['p38', 'p39', 'p40', 'p41', 'p42'] FY2025 theme park segment sales ¥568.3bn (+¥16.2bn) and net sales per guest ¥18,403 imply ~30.9M guest-equivalents, above the 27.53M admissions — a scope difference (per-guest includes hotel/F&B/other

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September share of annual admissions | 0.072 | 0.06..0.086 | 0.05079..0.1016 (widened) | fraction of annual admissions | m1 (m1), m3 (m3) | September is a low month (Halloween only in the second half; school term). Congestion indices (p19/p20, p27/p28) put September near the annual low, well below 1/12=0.083. A share around 0.07 of annual admissions is consistent with a low-month position; range spans 0.06–0.086. | Annual admissions are roughly evenly distributed with September as a below-average month, as the congestion indices indicate. | A published monthly split showing September materially above ~8.6% or below ~6% of annual admissions. |
| a2 | September 2026 y/y attendance change factor | 1.02 | 0.95..1.1 | 0.9143..1.143 (widened) | ratio (2026 vs 2025) | unused | Q1 FY2026 attendance was +7% y/y (p51) but Q2 FY2025 September was -2% y/y (p102); the 25th-anniversary event (p124) and strong Q1 momentum suggest modest positive growth, tempered by the September 2025 base and the conflicting congestion signals (p29/p30 vs p95). Centered near +2% with wide range. | September 2026 attendance grows modestly relative to September 2025, consistent with Q1 momentum but not extrapolating the +7% quarter. | Oriental Land Q2 FY2026 disclosure showing September 2026 attendance flat or declining, or a major closure/typhoon. |
| a3 | September 2025 daily average admissions (both parks) | 66,000 | 55,000..78,000 | 46,314..92,628 (widened) | visitors per day | unused | FY2025 annual 27.53M (p17) over 365 days ≈ 75,400/day average; September is a low month, so daily average is below the annual mean. ~66,000/day is a plausible low-month level, bracketed by pre-COVID ~87–89k (p65/p66) and current lower attendance. | September 2025 daily average sits below the FY2025 annual daily mean, consistent with September being a low month. | A published September 2025 monthly total or daily average outside the 55k–78k range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 66,082 | ['p17'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | n/a | [] / ['a2', 'a3'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |
| m3 | formula_mc | 66,082 | ['p17'] / ['a1'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **66,082** visitor/day, 80% interval [44,630, 97,846] visitor/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms none (no entity constraint); measure stems ['avera', 'visit']


## Final answer

The best estimate for the average daily number of visitors (park admissions, both gates combined) to Tokyo Disney Resort during September 2026 is 66,082 visitor/day (80% model-based interval 44,630 to 97,846 visitor/day).

The estimate rests mainly on observed annual attendance for FY[n] of 27,530,000 visitors (annual admissions) admissions, multiplied by an assumed September share of annual admissions of 0.072 (range 0.05079 to 0.1016) and divided by [n] days. The September share is the dominant uncertainty: it is an analyst assumption informed by congestion indices showing September as a low month, not an observed figure. The two retained methods are algebraically equivalent reformulations sharing the same inputs, so they are not independent confirmation; the weighting reflects that shared basis rather than demonstrated accuracy.

The main risk is that the September share is wrong, since no official monthly or daily visitor series exists. The most useful missing evidence would be any third-party monthly attendance reconstruction or park-level monthly disclosure that could calibrate the September seasonal share directly.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September share of annual admissions: 0.072 fraction of annual admissions, range 0.05079 to 0.1016 (range widened by code); used by m1, m3. Overturned by: A published monthly split showing September materially above ~[n] or below ~[n] of annual admissions.

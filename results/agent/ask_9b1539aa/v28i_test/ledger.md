# Evidence ledger: ask_9b1539aa

- Question: 镇江恒顺集团每年卖出多少瓶香醋（所有的瓶装醋，不区分类型）到美国
- as_of: 2026-10-18
- Pinned target: Number of bottles of Zhenjiang Hengshun (恒顺) vinegar (all bottled vinegar types, including aromatic/sharp vinegar 香醋 and other bottled vinegar products) sold by Hengshun Group into the United States market, counted as bottles (physical units) over a full year | unit bottle | period 2024-01-01..2024-12-31 | publisher None identified; Hengshun (Jiangsu Hengshun Vinegar-Industry Co., Ltd., 恒顺醋业, SSE: 600305) discloses revenue and export/overseas sales in annual reports but not US bottle counts

## Directions and pages

### d1 [related_series] Hengshun corporate disclosure (annual report / investor relations)

Hypothesis: Hengshun's annual report discloses overseas/export revenue (境外收入 or 出口收入) and total vinegar sales volume; overseas revenue × US share of overseas sales ÷ average export bottle price gives US bottle count. Direction: higher overseas revenue implies more bottles.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外收入 出口; 恒顺醋业 2023 年报 境外收入 营业收入 醋 销量; 恒顺醋业 2024年年度与行业相关的定期经营数据公告 外贸模式 产销量 吨; 恒顺醋业 出口 美国 海外市场 占比 外贸 亿美元 香醋 出口量

- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://data.eastmoney.com/notices/detail/600305/AN202404291631610629.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-

### d2 [physical_flow] China customs / trade statistics

Hypothesis: China customs export data for HS code 2209 (vinegar and substitutes) to the US, combined with Hengshun's share of China's vinegar exports to the US, gives US-bound tonnage; tonnage ÷ average bottle fill weight gives bottles. Direction: higher US-bound tonnage implies more bottles.

Queries issued by the searcher: China customs HS 2209 vinegar exports United States 2024 kg; UN Comtrade 220900 vinegar exports China USA; 恒顺醋业 2024年年度报告 境外 营业收入 出口; 中国 食醋 出口 美国 海关 数据 吨 2023

- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p1 China HS22090000 vinegar exports to United States, quantity (2020-2022 cumulativ = **6,597,078** liters (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p2 China HS22090000 vinegar exports to United States, value (2020-2022 cumulative) = **8,459,027** USD (2020-01-01..2022-12-31) [DISCARD: Duplicate of p1 (same US export value measurement); p101 also carries it.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p3 United States share of China HS22090000 vinegar export quantity (2020-2022 cumul = **11.35** % (2020-01-01..2022-12-31) [DISCARD: Duplicate of p102 (same US share); keep p102.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p4 China HS22090000 vinegar total exports to all countries, quantity (2020-2022 cum = **58,119,878** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p99 (same all-country total).] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p5 Number of destination countries for China HS22090000 vinegar exports (2020-2022  = **129** countries (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家"
  - p6 China HS22090000 vinegar exports to Hong Kong, quantity (2020-2022 cumulative, l = **13,624,552** liters (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p7 China HS22090000 vinegar exports to Hong Kong, value (2020-2022 cumulative) = **15,656,412** USD (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p8 China HS22090000 vinegar exports to Singapore, quantity (2020-2022 cumulative) = **4,057,620** liters (2020-01-01..2022-12-31) [keep: ] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p9 China HS22090000 vinegar exports to Australia, quantity (2020-2022 cumulative) = **3,691,524** liters (2020-01-01..2022-12-31) [keep: ] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p10 China HS22090000 vinegar exports to Netherlands, quantity (2020-2022 cumulative) = **3,519,273** liters (2020-01-01..2022-12-31) [keep: ] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p11 China HS22090000 vinegar exports to Malaysia, quantity (2020-2022 cumulative) = **3,160,711** liters (2020-01-01..2022-12-31) [keep: ] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p12 China HS22090000 vinegar exports to Canada, quantity (2020-2022 cumulative) = **2,537,372** liters (2020-01-01..2022-12-31) [keep: ] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p13 China HS22090000 vinegar exports to Japan, quantity (2020-2022 cumulative) = **2,404,533** liters (2020-01-01..2022-12-31) [keep: ] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p14 China HS22090000 vinegar exports to France, quantity (2020-2022 cumulative) = **1,754,906** liters (2020-01-01..2022-12-31) [keep: ] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `https://chinadata.live/china-trade/hs/220900/united-states/` -> **dropped** (live http 403); points raw/verified -/-
- `https://irm.cninfo.com.cn/ircs/question/questionDetail?questionId=2231512647605473280` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://chinadata.live/china-trade/hs/220900/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] US import statistics (USITC/Census)

Hypothesis: US import records for vinegar from China (HS 2209) give total US-bound volume; Hengshun's share of Chinese vinegar imports into the US × total volume ÷ bottle size gives bottles. Direction: larger US imports from China imply more Hengshun bottles if share is stable.

Queries issued by the searcher: USITC imports HS 2209 vinegar China 2024 quantity kg; 恒顺醋业 2024年年报 境外收入 出口 营收; US imports vinegar from China 2024 value HS 220900 Census Bureau trade data; "2209" vinegar United States imports China 2023 2024 million dollars quantity liters

- `https://cfi.cn/p20260415001052.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://oec.world/en/profile/bilateral-product/vinegar/reporter/usa` -> **live_dated** (page date 2024-11-01); points raw/verified 0/0
- `https://boatdb.net/hs/220900` -> **dropped** (live http 429); points raw/verified -/-
- `http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-22/600305_20250422_2SFY.pdf` -> **live_dated** (page date 2025-04-22); points raw/verified 0/0

### d4 [base_rates] Industry / market research on Chinese vinegar exports and US Asian condiment market

Hypothesis: Industry reports give China's vinegar export volume and the share going to North America; Hengshun as the largest producer holds a known export share. Bottles = export volume × North America share × Hengshun share ÷ average bottle size.

Queries issued by the searcher: 中国调味品协会 食醋 出口 北美 占比; Hengshun vinegar largest vinegar exporter China export share; 中国食醋出口量 2024 万吨 海关 出口额; 恒顺醋业 出口 占全国食醋出口 65% 海外收入 年报

- `https://www.sohu.com/a/821678279_121823071` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://www.ourjiangsu.com/a/20211013/1634093003829.shtml` -> **live_dated** (page date 2021-10-13); points raw/verified 11/10
  - p15 Hengshun share of China's total vinegar exports (stated as more than) = **65** % of China's total vinegar exports (..) [keep: ] quote: "accounting for more than 65% of China's total vinegar exports."
  - p16 Number of countries where Hengshun products are sold (stated as more than) = **100** countries (..) [keep: ] quote: "its products are widely sold in more than 100 countries around the world"
  - p17 Years of Hengshun brand inheritance and innovation = **181** years (..) [DISCARD: Brand heritage years — irrelevant to bottle volume.] quote: "after 181 years of inheritance and innovation of excellence"
  - p18 Number of processes to make a drop of vinegar = **40** processes (..) [DISCARD: Number of production processes — irrelevant.] quote: "A grain of rice can be turned into a drop of vinegar after more than 40 processes in 70 days."
  - p19 Days to make a drop of vinegar = **70** days (..) [DISCARD: Days to make vinegar — irrelevant.] quote: "after more than 40 processes in 70 days"
  - p20 Oil vinegar juice sales (stated as nearly) = **10,000,000** yuan (..) [DISCARD: Oil/vinegar/juice sales figure, ambiguous scope and tiny — not usable for US bottle count.] quote: "oil vinegar juice has generated nearly 10 million yuan in sales."
  - p21 Annual increase in Hengshun e-commerce sales (stated as more than) = **100** % per year (..) [DISCARD: E-commerce growth rate — no bridge to US bottles.] quote: "Hengshun has increased its e-commerce sales by more than 100% every year"
  - p22 Jiangsu time-honored brand enterprises identified and awarded = **271** enterprises (..) [DISCARD: Jiangsu time-honored brand count — irrelevant.] quote: "Jiangsu has made headway in the identification and awarding of time-honored brand titles to 271 venerable enterprises."
  - p23 Jiangsu enterprises awarded national time-honored titles by Ministry of Commerce = **96** enterprises (..) [DISCARD: Jiangsu national time-honored count — irrelevant.] quote: "96 of them are awarded national titles by the Ministry of Commerce"
  - p24 Share of national total held by Jiangsu's nationally titled time-honored enterpr = **8.5** % of national total (..) [DISCARD: Jiangsu share of national time-honored brands — irrelevant.] quote: "accounting for 8.5% of the national total."
- `https://finance.sina.com.cn/stock/relnews/cn/2026-06-10/doc-iniawpnc1440816.shtml` -> **live_dated** (page date 2026-06-10); points raw/verified 15/15
  - p25 China vinegar (食醋) total production volume, 2024 = **4,800,000** 万吨 (10,000 tonnes) (2024-01-01..2024-12-31) [keep: ] quote: "2024年全国食醋产量达480万吨,产值突破300亿元"
  - p26 China vinegar industry output value, 2024 = **30,000,000,000** 亿元 (100 million yuan) (2024-01-01..2024-12-31) [keep: ] quote: "2024年全国食醋产量达480万吨,产值突破300亿元"
  - p27 China vinegar industry compound annual growth rate = **6.5** % per year (..) [keep: ] quote: "年均复合增长率保持在6.5%以上"
  - p28 Share of China vinegar production from top five provinces (combined) = **75** % of national output (..) [keep: ] quote: "其中前五省合计产量占比超75%"
  - p29 Jiangsu province share of national vinegar production (Zhenjiang aromatic vinega = **19** % of national output (..) [keep: ] quote: "\| 江苏省 \| 19% \| 镇江香醋 \| 恒顺醋业 \|"
  - p30 Shanxi province share of national vinegar production = **29** % of national output (..) [DISCARD: Shanxi province share — not Hengshun; context only, no route.] quote: "\| 山西省 \| 29% \| 山西老陈醋 \|"
  - p31 Sichuan province share of national vinegar production = **12** % of national output (..) [DISCARD: Sichuan province share — not Hengshun.] quote: "\| 四川省 \| 12% \| 保宁麸醋 \|"
  - p32 Shandong province share of national vinegar production = **9** % of national output (..) [DISCARD: Shandong province share — not Hengshun.] quote: "\| 山东省 \| 9% \| 山东米醋、特色香醋 \|"
  - p33 Fujian province share of national vinegar production = **6** % of national output (..) [DISCARD: Fujian province share — not Hengshun.] quote: "\| 福建省 \| 6% \| 永春老醋 \|"
  - p34 Combined market share of top five vinegar enterprises = **42.3** % of market (..) [keep: ] quote: "食醋行业前五企业合计占比约42.3%"
  - p35 Number of above-scale (规上) vinegar enterprises in China, as of 2025 = **1,200** enterprises (2025-01-01..2025-12-31) [DISCARD: Count of above-scale vinegar enterprises — irrelevant to volume.] quote: "截至 2025 年,全国规上食醋企业约 1200 家"
  - p36 Number of small and medium vinegar workshops in China, as of 2025 = **2,800** workshops (2025-01-01..2025-12-31) [DISCARD: Count of small workshops — irrelevant.] quote: "中小作坊超 2800 家"
  - p37 United States share of China's total vinegar export volume (largest export desti = **40** % of total export volume (..) [keep: ] quote: "其中美国为第一大出口市场,占中国食醋总出口量约40%"
  - p38 Hengshun (恒顺醋业) 2025 R&D expenditure = **93,920,000** 万元 (10,000 yuan) (2025-01-01..2025-12-31) [DISCARD: R&D expenditure — irrelevant to US bottle count.] quote: "2025 年研发费9392 万元 (+4.67%)"
  - p39 Share of brewed vinegar (酿造食醋) in China vinegar product mix = **80** % of market (..) [keep: ] quote: "其中酿造食醋占据市场主流,占比超 80%"
- `http://m.3news.cn/exist/ylbg/2023/0908/1044946.html` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d5 [capacity_consumption] Hengshun production and export capacity

Hypothesis: Hengshun's total vinegar production capacity × export share × US share of exports ÷ bottle size gives an upper-bound-constrained estimate. Direction: capacity and utilisation bound the maximum possible US bottles.

Queries issued by the searcher: 恒顺醋业 产能 万吨 食醋 产量; 恒顺醋业 年报 食醋 产能 产量 销量 万吨; 恒顺醋业 境外收入 出口 占比 年报 分地区; 恒顺 出口 美国 海外 占比 食醋 出口量

- `https://www.9fzt.com/detail/sh_600305_9_be7632f9eac0dfcaba1f793b32797faa.html` -> **live_dated** (page date 1995-10-17); points raw/verified 11/0
- `https://www.zjhengshun.com/cn_wap/list/12/284.htm` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=12089193` -> **live_dated** (page date 2026-04-15); points raw/verified 15/11
  - p40 Hengshun vinegar-series (醋系列) production volume, 2025 = **235,643** tons (2025-01-01..2025-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22 \|"
  - p41 Hengshun vinegar-series (醋系列) sales volume, 2025 = **228,113** tons (2025-01-01..2025-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22 \|"
  - p42 Hengshun vinegar-series inventory volume at year-end 2025 = **18,409** tons (2025-12-31..2025-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22 \|"
  - p43 Hengshun foreign-trade (外贸模式) revenue, 2025 = **39,171,647** CNY (2025-01-01..2025-12-31) [keep: ] quote: "\| 外贸模式 \| 39,171,647.23 \| 29,715,440.56 \| 24.14 \| -17.95 \| -14.38 \| 减少3.16个百分点 \|"
  - p44 Hengshun foreign-trade (外贸模式) revenue year-on-year change, 2025 = **-17.95** % (2025-01-01..2025-12-31) [keep: ] quote: "\| 外贸模式 \| 39,171,647.23 \| 29,715,440.56 \| 24.14 \| -17.95 \| -14.38 \| 减少3.16个百分点 \|"
  - p45 Hengshun total condiment (调味品) revenue, 2025 = **2,266,466,159** CNY (2025-01-01..2025-12-31) [keep: ] quote: "\| 调味品 \| 2,266,466,159.39 \| 1,537,411,067.26 \| 32.17 \| 8.29 \| 13.18 \| 减少2.93个百分点 \|"
  - p46 Hengshun vinegar-series (醋系列) revenue, 2025 = **1,321,092,496** CNY (2025-01-01..2025-12-31) [keep: ] quote: "\| 醋系列 \| 1,321,092,495.56 \| 709,855,429.02 \| 46.27 \| 4.38 \| 2.57 \| 增加0.95个百分点 \|"
  - p47 Hengshun total revenue, 2025 = **2,286,538,594** CNY (2025-01-01..2025-12-31) [keep: ] quote: "\| 营业收入 \| 2,286,538,593.94 \| 2,195,870,508.45 \| 4.13 \| 2,106,410,685.37 \|"
  - p48 Hengshun total revenue, 2024 = **2,195,870,508** CNY (2024-01-01..2024-12-31) [keep: ] quote: "\| 营业收入 \| 2,286,538,593.94 \| 2,195,870,508.45 \| 4.13 \| 2,106,410,685.37 \|"
  - p49 Hengshun planned capacity of 3万吨/year brewed vinegar expansion project (complete = **3** 万吨 (10,000 tons) per year (2025-01-01..2025-12-31) [keep: ] quote: "\| 向特定对象发行股票 \| 年产3万吨酿造食醋扩产项目[注1][注3] \| 生产建设 \| 是 \| 否 \| 12,000.00 \| 5,804.60 \| 12,049.74 \| 100.41 \| 2025年12月 \| 是 \| 是 \|"
  - p50 Hengshun vinegar-series production volume year-on-year change, 2025 = **11.87** % (2025-01-01..2025-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 235,643.35 \| 228,113.05 \| 18,409.49 \| 11.87 \| 7.22 \| 69.22 \|"
- `http://www.canyin88.com:8080/zixun/2025/12/02/110232.html` -> **live_dated** (page date 2025-12-02); points raw/verified 15/12
  - p51 Hengshun vinegar series production volume 2024 = **210,600** 万吨 (10,000 tons) of vinegar series production (2024-01-01..2024-12-31) [DISCARD: Unit label is wrong (万吨 vs tonnes) and it duplicates the 2024 vinegar production scale already given by p40/p50; keep p5] quote: "2024年,恒顺醋业的醋系列产量已经达到21.06万吨"
  - p52 Hengshun vinegar series sales volume 2024 = **212,700** 万吨 (10,000 tons) of vinegar series sales (2024-01-01..2024-12-31) [keep: ] quote: "销量也超过21.27万吨"
  - p53 Hengshun total revenue 2024 = **2,196,000,000** 亿元 (100 million yuan) total revenue (2024-01-01..2024-12-31) [DISCARD: Rounded duplicate of p48 (Hengshun total revenue 2024).] quote: "去年,其总营收为21.96亿元"
  - p54 Hengshun vinegar series revenue 2024 = **1,266,000,000** 亿元 (100 million yuan) vinegar series revenue (2024-01-01..2024-12-31) [keep: ] quote: "醋系列就实现12.66亿元,占据过半营收"
  - p55 Hengshun vinegar series revenue H1 2025 = **739,000,000** 亿元 (100 million yuan) vinegar series revenue (2025-01-01..2025-06-30) [DISCARD: H1 2025 vinegar revenue — sub-period, redundant with annual p46.] quote: "醋系列仍是恒顺醋业的营收主力,贡献了7.39亿元收入"
  - p56 Hengshun wine and sauce series combined revenue H1 2025 = **231,000,000** 亿元 (100 million yuan) combined revenue (2025-01-01..2025-06-30) [DISCARD: Wine/sauce H1 revenue — not vinegar, irrelevant.] quote: "酒系列、酱系列的销售收入合计仅2.31亿元左右"
  - p57 Hengshun wine series revenue year-on-year change H1 2025 = **5.42** % decrease (2025-01-01..2025-06-30) [DISCARD: Wine series change — not vinegar.] quote: "分别同比减少了5.42%、3.53%"
  - p58 Hengshun sauce series revenue year-on-year change H1 2025 = **3.53** % decrease (2025-01-01..2025-06-30) [DISCARD: Sauce series change — not vinegar.] quote: "分别同比减少了5.42%、3.53%"
  - p59 Hengshun offline distributors covered (as of end of last year) = **1,700** distributors (2024-12-31..2024-12-31) [DISCARD: Domestic distributor count — domestic, not US.] quote: "恒顺醋业已经覆盖全国超1700家经销商"
  - p60 Hengshun terminal outlets (as of end of last year) = **350,000** 万家 (10,000 outlets) (2024-12-31..2024-12-31) [DISCARD: Domestic terminal outlets — domestic, not US.] quote: "终端网点突破35万家"
  - p61 Hengshun self-media cumulative followers (as of end of last year) = **280,000** 万 (10,000) followers (2024-12-31..2024-12-31) [DISCARD: Social media followers — irrelevant.] quote: "截止去年底累计粉丝超28万"
  - p62 Hengshun R&D and pilot base area (as of end of last year) = **6,000** square meters (2024-12-31..2024-12-31) [DISCARD: R&D base area — irrelevant.] quote: "研究实验场所和中试基地占地 6000多平方米"
- dropped by code checks: 18 (value_as_written not in quote as a whole number: 11; number: value_as_written is only part of a larger CJK number in the quote: 3; period_end missing or unparseable: 3; number: no number in value_as_written: 1)

### d6 [own_history] Hengshun historical export disclosures and news

Hypothesis: Past years' disclosed export volumes or overseas revenue growth rates can anchor the 2024 level and reveal trend; if US exports grew at a known rate, prior estimates can be updated. Direction: stable or growing trend implies 2024 near recent levels.

Queries issued by the searcher: 恒顺醋业 出口 销量 海外收入 2019 2020 2021 年报; Hengshun vinegar US market Walmart Asian supermarket sales; 恒顺醋业 分销售模式 经销 直销 外贸 营业收入 万元 2023年报; 恒顺醋业 海外 收入 占比 出口 美国 日本 东南亚 新闻 2023

- `https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2024-04-30/600305_20240430_ANJE.pdf` -> **live_dated** (page date 2024-04-30); points raw/verified 0/0
- `https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600305&id=8852755` -> **live_dated** (page date 2023-02-28); points raw/verified 15/12
  - p63 Hengshun foreign trade (export) segment revenue, 2022 = **43,692,699** RMB yuan (2022-01-01..2022-12-31) [keep: ] quote: "\| 外贸模式 \| 43,692,698.82 \| \| 34,617,335.02 \| 20.77 \| 12.41 \| 15.07 \| 减少1.83个百分点 \|"
  - p64 Hengshun foreign trade (export) segment revenue year-on-year change, 2022 = **12.41** % (2022-01-01..2022-12-31) [keep: ] quote: "\| 外贸模式 \| 43,692,698.82 \| \| 34,617,335.02 \| 20.77 \| 12.41 \| 15.07 \| 减少1.83个百分点 \|"
  - p65 Hengshun foreign trade (export) segment gross margin, 2022 = **20.77** % (2022-01-01..2022-12-31) [DISCARD: Export gross margin — not a volume input.] quote: "\| 外贸模式 \| 43,692,698.82 \| \| 34,617,335.02 \| 20.77 \| 12.41 \| 15.07 \| 减少1.83个百分点 \|"
  - p66 Hengshun vinegar series (醋系列) sales volume, 2022 = **206,704** tonnes (2022-01-01..2022-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 209,390.61 \| 206,704.04 \| 15,295.55 \| 14.74 \| 17.77 \| 21.31 \|"
  - p67 Hengshun vinegar series (醋系列) sales volume year-on-year change, 2022 = **17.77** % (2022-01-01..2022-12-31) [DISCARD: 2022 sales volume YoY change — redundant with p66 level.] quote: "\| 醋系列 \| 吨 \| 209,390.61 \| 206,704.04 \| 15,295.55 \| 14.74 \| 17.77 \| 21.31 \|"
  - p68 Hengshun vinegar series (醋系列) production volume, 2022 = **209,391** tonnes (2022-01-01..2022-12-31) [keep: ] quote: "\| 醋系列 \| 吨 \| 209,390.61 \| 206,704.04 \| 15,295.55 \| 14.74 \| 17.77 \| 21.31 \|"
  - p69 Hengshun vinegar series (醋系列) revenue, 2022 = **1,283,931,266** RMB yuan (2022-01-01..2022-12-31) [keep: ] quote: "\| 醋系列 \| 1,283,931,265.81 \| 750,550,024.91 \| 41.54 \| 6.03 \| 10.63 \| 减少2.43 \|"
  - p70 Hengshun vinegar series (醋系列) revenue year-on-year change, 2022 = **6.03** % (2022-01-01..2022-12-31) [DISCARD: 2022 vinegar revenue YoY change — redundant with p69 level.] quote: "\| 醋系列 \| 1,283,931,265.81 \| 750,550,024.91 \| 41.54 \| 6.03 \| 10.63 \| 减少2.43 \|"
  - p71 Hengshun total operating revenue, 2022 = **2,139,020,033** RMB yuan (2022-01-01..2022-12-31) [DISCARD: 2022 total revenue — redundant with p48/p53 for 2024 target.] quote: "\| 营业收入 \| 2,139,020,033.23 \| 1,893,347,829.74 \| 12.98 \| 2,023,826,420.92 \|"
  - p72 Hengshun total operating revenue, 2021 = **1,893,347,830** RMB yuan (2021-01-01..2021-12-31) [DISCARD: 2021 total revenue — not needed.] quote: "\| 营业收入 \| 2,139,020,033.23 \| 1,893,347,829.74 \| 12.98 \| 2,023,826,420.92 \|"
  - p73 Hengshun total operating revenue, 2020 = **2,023,826,421** RMB yuan (2020-01-01..2020-12-31) [DISCARD: 2020 total revenue — not needed.] quote: "\| 营业收入 \| 2,139,020,033.23 \| 1,893,347,829.74 \| 12.98 \| 2,023,826,420.92 \|"
  - p74 Hengshun condiment main business revenue, 2022 = **2,031,615,553** RMB yuan (2022-01-01..2022-12-31) [DISCARD: 2022 condiment revenue — redundant context.] quote: "\| 调味品 \| 2,031,615,552.76 \| 1,340,053,782.89 \| 34.04 \| 10.05 \| 15.15 \| 减少2.92个百分点 \|"
- `https://basic.10jqka.com.cn/600305/` -> **live_dated** (page date 2026-10-16); points raw/verified 0/0
- `https://www.inst.cr/products/17891985-heng-shun-zhenjiang-vinegar-580-ml?retailerSlug=hmart` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 3 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; number: value_as_written is only part of a larger CJK number in the quote: 1)

### d7 [persona] US distributors, importers, and Asian supermarket buyers

Hypothesis: US importers/distributors of Hengshun (e.g., Asian food wholesalers) may disclose shipment volumes or container counts; containers × bottles per container gives bottles. Direction: more containers implies more bottles.

Queries issued by the searcher: Hengshun vinegar US distributor importer Chinkiang; 恒顺香醋 美国 进口商 经销商; Well Luck Co Inc Hengshun US agent vinegar distributor Jersey City; 20ft container loading quantity 550ml glass bottles 24 per carton vinegar

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://tw.news.yahoo.com/%E5%90%84%E4%BA%9E%E6%B4%B2%E8%B6%85%E5%B8%82%E6%8E%A8%E5%87%BA%E6%81%86%E9%A0%86%E7%B3%BB%E5%88%97%E7%94%A2%E5%93%81%E9%BB%` -> **live_dated** (page date 2024-11-29); points raw/verified 0/0
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p75 Total US customs shipments recorded for Jiangsu Hengshun Group (2006-11-01 to 20 = **44** shipments (2006-11-01..2022-08-14) [DISCARD: Duplicate of p113 (same ImportGenius shipment count).] quote: "Total Shipments 44"
  - p76 Number of trading partners recorded for Jiangsu Hengshun Group = **6** trading partners (2006-11-01..2022-08-14) [DISCARD: Duplicate of p114.] quote: "Trading Partners 6"
  - p77 Number of ports recorded for Jiangsu Hengshun Group shipments = **5** ports (2006-11-01..2022-08-14) [DISCARD: Duplicate of p115.] quote: "Ports 5"
  - p78 Piece count on bill of lading EGLV142252207486 for Chinkiang vinegar 550ML@24 = **700** pieces (2022-08-13..2022-08-13) [DISCARD: Duplicate of p116.] quote: "Piece Count 700"
  - p79 Bottle size in vinegar shipment description (Chinkiang vinegar 550ML@24) = **550** millilitres per bottle (2022-08-13..2022-08-13) [DISCARD: Duplicate of p117.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p80 Bottles per case in vinegar shipment description (550ML@24) = **24** bottles per case (2022-08-13..2022-08-13) [DISCARD: Duplicate of p118.] quote: "VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p81 Container length in centimetres on bill of lading EGLV142252207486 = **240** centimetres (2022-08-13..2022-08-13) [DISCARD: Duplicate of p119.] quote: "Length 240"
  - p82 Container height in centimetres on bill of lading EGLV142252207486 = **102** centimetres (2022-08-13..2022-08-13) [DISCARD: Duplicate of p120.] quote: "Height 102"
  - p83 Container width in centimetres on bill of lading EGLV142252207486 = **96** centimetres (2022-08-13..2022-08-13) [DISCARD: Duplicate of p121.] quote: "Width 96"

### d8 [attention] US retail and e-commerce presence

Hypothesis: Hengshun product listings and review counts on Amazon/Walmart/Asian grocers, combined with typical sales-per-review or per-listing ratios, can proxy US retail bottle volume. Direction: more reviews/listings imply more retail sales, but the bridge to bottles is weak.

Queries issued by the searcher: Hengshun vinegar Amazon US reviews Chinkiang; 恒顺香醋 美国 亚马逊 销量; 恒顺 镇江香醋 weee 周销量 1K+ 18.6 液盎司; Amazon "bought in past month" Chinkiang vinegar Hengshun 550ml ratings count

- `https://www.sayweee.com/zht/mkpl/category/seasoning10/Vinegar?filters=%7B%22catalogue_num%22%3A%22seasoning10%22%7D` -> **live_dated** (page date 2015-01-01); points raw/verified 15/0
- `https://www.weee.com/en/product/Heng-Shun-Zhenjiang-Vinegar/64693` -> **live_dated** (page date 2026-10-18); points raw/verified 0/0
- `https://www.freshgogo.com/pc/goodsDescribe?id=10004&language=zh` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.amazon.com/Chinkiang-Zhenjiang-Vinegar-Yr-Aged/dp/B00VPL24NE/r` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- dropped by code checks: 15 (period year 2024 does not appear in the page text or URL (likely mis-dated): 15)

### b1 [related_series] customs

Hypothesis: A 2024 China customs HS22090000 export-to-US quantity (liters) would replace the stale 2020-2022 p1 and resolve the p3-vs-p37 US-share conflict, directly anchoring the physical-flow route (m2).

Queries issued by the searcher: UN Comtrade China exports USA HS 220900 vinegar 2024 quantity; 中国海关 醋 出口 美国 2024 数量 HS220900; 2024年 中国 醋 出口 美国 升 数量 金额 海关 22090000 国别; comtradeapi.un.org HS 220900 China United States 2022 netweight

- `https://hs.bianmachaxun.com/sec_report/by_hscode/22090000` -> **live_dated** (page date 2026-01-01); points raw/verified 15/15
  - p84 China HS 22090000 vinegar exports, total quantity, 2024 Jan-Dec = **25,760,168** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p85 China HS 22090000 vinegar exports, total value, 2024 Jan-Dec = **29,648,742** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p86 China HS 22090000 vinegar exports, average price per liter, 2024 Jan-Dec = **1.15** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 25760168 \| $29648742 \| $1.15 \| 导出 \|"
  - p87 China HS 22090000 vinegar exports, total quantity, 2023 Jan-Dec = **21,832,831** liters (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p88 China HS 22090000 vinegar exports, total value, 2023 Jan-Dec = **25,717,401** USD (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p89 China HS 22090000 vinegar exports, average price per liter, 2023 Jan-Dec = **1.18** USD per liter (2023-01-01..2023-12-31) [keep: ] quote: "\| 2023年 1月-12月份 \| 21832831 \| $25717401 \| $1.18 \| 导出 \|"
  - p90 China HS 22090000 vinegar imports, total quantity, 2024 Jan-Dec = **6,382,197** liters (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p91 China HS 22090000 vinegar imports, total value, 2024 Jan-Dec = **11,585,503** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p92 China HS 22090000 vinegar imports, average price per liter, 2024 Jan-Dec = **1.82** USD per liter (2024-01-01..2024-12-31) [keep: ] quote: "\| 2024年 1月-12月份 \| 6382197 \| $11585503 \| $1.82 \| 导出 \|"
  - p93 China HS 22090000 vinegar exports, total quantity, 2022 Jan-Dec = **19,604,254** liters (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p94 China HS 22090000 vinegar exports, total value, 2022 Jan-Dec = **24,461,049** USD (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p95 China HS 22090000 vinegar exports, average price per liter, 2022 Jan-Dec = **1.25** USD per liter (2022-01-01..2022-12-31) [keep: ] quote: "\| 2022年 1月-12月份 \| 19604254 \| $24461049 \| $1.25 \| 导出 \|"
  - p96 China HS 22090000 vinegar exports, total quantity, 2021 Jan-Dec = **20,249,374** liters (2021-01-01..2021-12-31) [keep: ] quote: "\| 2021年 1月-12月份 \| 20249374 \| $25590784 \| $1.26 \| 导出 \|"
  - p97 China HS 22090000 vinegar exports, total quantity, 2020 Jan-Dec = **17,414,624** liters (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
  - p98 China HS 22090000 vinegar exports, average price per liter, 2020 Jan-Dec = **1.34** USD per liter (2020-01-01..2020-12-31) [keep: ] quote: "\| 2020年 1月-12月份 \| 17414624 \| $23362688 \| $1.34 \| 导出 \|"
- `https://www.sohu.com/a/821678279_121823071` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://m.x315.cn/doc/oCdbqO` -> **live_dated** (page date 2025-02-23); points raw/verified 15/14
  - p99 China HS22090000 total vinegar exports to all 129 countries, quantity, 2020-01 t = **58,119,878** liters (2020-01-01..2022-12-31) [keep: ] quote: "近三年来,HS22090000共销往海外129个国家,总计58,119,878升,7,245万美元"
  - p100 China HS22090000 vinegar exports to United States, quantity, 2020-01 to 2022-12 = **6,597,078** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p1.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p101 China HS22090000 vinegar exports to United States, value, 2020-01 to 2022-12 = **8,459,027** USD (2020-01-01..2022-12-31) [DISCARD: Duplicate of p1/p2.] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p102 United States share of China HS22090000 vinegar export quantity, 2020-01 to 2022 = **11.35** % (2020-01-01..2022-12-31) [keep: ] quote: "第二美国:总数量为6,597,078升;金额8,459,027美元;总占比11.35%。"
  - p103 Hong Kong share of China HS22090000 vinegar export quantity, 2020-01 to 2022-12 = **23.44** % (2020-01-01..2022-12-31) [keep: ] quote: "第一中国香港:总数量为13,624,552升;金额15,656,412美元;总占比23.44%。"
  - p104 China HS22090000 vinegar exports to Hong Kong, quantity, 2020-01 to 2022-12 = **13,624,552** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p6 (Hong Kong quantity).] quote: "其中出口中国香港数量最多,总计13,624,552升"
  - p105 China HS22090000 vinegar exports to Singapore, quantity, 2020-01 to 2022-12 = **4,057,620** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p8 (Singapore quantity).] quote: "第三新加坡:总数量为4,057,620升;金额4,497,131美元;总占比6.98%。"
  - p106 China HS22090000 vinegar exports to Australia, quantity, 2020-01 to 2022-12 = **3,691,524** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p9 (Australia quantity).] quote: "第四澳大利亚:总数量为3,691,524升;金额5,888,882美元;总占比6.35%。"
  - p107 China HS22090000 vinegar exports to Netherlands, quantity, 2020-01 to 2022-12 = **3,519,273** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p10 (Netherlands quantity).] quote: "第五荷兰:总数量为3,519,273升;金额5,331,215美元;总占比6.06%。"
  - p108 China HS22090000 vinegar exports to Malaysia, quantity, 2020-01 to 2022-12 = **3,160,711** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p11 (Malaysia quantity).] quote: "第六马来西亚:总数量为3,160,711升;金额3,749,966美元;总占比5.44%。"
  - p109 China HS22090000 vinegar exports to Canada, quantity, 2020-01 to 2022-12 = **2,537,372** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p12 (Canada quantity).] quote: "第七加拿大:总数量为2,537,372升;金额3,265,483美元;总占比4.37%。"
  - p110 China HS22090000 vinegar exports to Japan, quantity, 2020-01 to 2022-12 = **2,404,533** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p13 (Japan quantity).] quote: "第八日本:总数量为2,404,533升;金额3,219,722美元;总占比4.14%。"
  - p111 China HS22090000 vinegar exports to Macau, quantity, 2020-01 to 2022-12 = **2,087,101** liters (2020-01-01..2022-12-31) [keep: ] quote: "第九中国澳门:总数量为2,087,101升;金额2,294,008美元;总占比3.59%。"
  - p112 China HS22090000 vinegar exports to France, quantity, 2020-01 to 2022-12 = **1,754,906** liters (2020-01-01..2022-12-31) [DISCARD: Duplicate of p14 (France quantity).] quote: "第十法国:总数量为1,754,906升;金额2,049,887美元;总占比3.02%。"
- `https://chinadata.live/china-trade/hs8/22090000/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b2 [related_series] company disclosure

Hypothesis: Hengshun annual report 2024 overseas/境外 revenue (or export share of vinegar sales) would let us convert total vinegar volume (p52) into export volume and then US bottles, unlocking a company-level route independent of customs.

Queries issued by the searcher: 恒顺醋业 2024 年报 境外收入; 恒顺醋业 出口 占比 2024 海外收入; 恒顺醋业 2024 年报 境外 收入 主营业务分地区 出口 美国; 恒顺醋业 2024 食醋 产量 销量 吨 年报 产销量

- `https://data.eastmoney.com/notices/detail/600305/AN202504211660034972.html` -> **live_dated** (page date 2007-02-17); points raw/verified 0/0
- `https://www.aijingu.com/notices/600305/AN202504211660034968.html` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://q.stock.sohu.com/cn/news.html?textId=100018443238&tab=100&type=100&code=cn_600305&date=2026/0415` -> **live_dated** (page date 2026-05-23); points raw/verified 0/0
- `https://basic.10jqka.com.cn/astockpc/astockmain/index.html` -> **dropped** (live page has no readable date); points raw/verified -/-

### b3 [related_series] trade_records

Hypothesis: Recent (2023-2024) US import bill-of-lading records for Hengshun would give container/shipment counts and bottle sizes, converting the sparse 2022 p78 evidence into an annual US bottle flow.

Queries issued by the searcher: ImportYeti Jiangsu Hengshun vinegar shipments; Panjiva Hengshun Chinkiang vinegar US imports; importyeti.com "Jiangsu Hengshun" supplier vinegar; 52wmb jiangsu hengshun international trad 提单记录 2024 香醋 美国

- `https://www.importgenius.cn/suppliers/jiangsu-hengshun-international-trad` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.52wmb.com/buyer/4134495` -> **dropped** (live http 502); points raw/verified -/-
- `https://www.importgenius.com/suppliers/jiangsu-hengshun-group` -> **live_dated** (page date 2022-08-13); points raw/verified 9/9
  - p113 Total US customs shipments recorded for Jiangsu Hengshun Group, cumulative 2006- = **44** shipments (2006-11-01..2022-08-14) [keep: ] quote: "Total Shipments 44"
  - p114 Trading partners count for Jiangsu Hengshun Group in US customs records = **6** trading partners (2006-11-01..2022-08-14) [keep: ] quote: "Trading Partners 6"
  - p115 Ports count for Jiangsu Hengshun Group in US customs records = **5** ports (2006-11-01..2022-08-14) [keep: ] quote: "Ports 5"
  - p116 Piece count on bill of lading EGLV142252207486 for CHINKIANG VINEGAR 550ML@24, a = **700** pieces (2022-08-13..2022-08-13) [keep: ] quote: "Piece Count 700"
  - p117 Bottle size in cargo description for CHINKIANG VINEGAR on bill of lading EGLV142 = **550** millilitres per bottle (2022-08-13..2022-08-13) [keep: ] quote: "Description VINEGAR ASIAN TASTE BRAND CHINKIANG VINEGAR 550ML@24"
  - p118 Bottles per case in cargo description for CHINKIANG VINEGAR 550ML@24 on bill of  = **24** bottles per case (2022-08-13..2022-08-13) [keep: ] quote: "VINEGAR 550ML@24"
  - p119 Container length in cm for shipment on bill of lading EGLV142252207486 = **240** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Length 240"
  - p120 Container height in cm for shipment on bill of lading EGLV142252207486 = **102** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Height 102"
  - p121 Container width in cm for shipment on bill of lading EGLV142252207486 = **96** centimetres (2022-08-13..2022-08-13) [keep: ] quote: "Width 96"
- `https://www.volza.com/p/chinkiang-vinegar/` -> **dropped** (live http 403); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['hengshun vinegar exports', 'china vinegar us imports', 'zhenjiang vinegar sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] Same source (m.x315.cn) reporting China HS22090000 export totals; p1/p2/p3/p4 are internally consistent (US 6.60M L of 58.12M L ≈ 11.35%). Single underlying measurement, not independent confirmation.
- conflicting: ['p1', 'p37'] p3 says US is 11.35% of China vinegar export quantity (2020-2022); p37 says US is ~40% of China vinegar export volume (largest destination). Material disagreement on the key US share; p37 is a later i
- corroborating: ['p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14'] Same source, destination breakdown of the same HS22090000 export total; consistent with p4 and useful for context but not independent of p1-p4.
- corroborating: ['p40', 'p41', 'p42', 'p46', 'p50'] Same 2025 annual report table: production 235,643 t, sales 228,113 t, inventory 18,409 t, revenue 1.321bn CNY, production +11.87%. Internally consistent.
- corroborating: ['p51', 'p52', 'p54'] 2024 vinegar series production 21.06万吨, sales 21.27万吨, revenue 12.66亿元 — consistent with p40/p41/p46 trend (2025 slightly higher).
- corroborating: ['p43', 'p44', 'p63', 'p64'] Foreign-trade segment revenue series: 2022 43.69M CNY (+12.41%), 2025 39.17M CNY (-17.95%). Same disclosure lineage; gives export revenue scale and trend.
- corroborating: ['p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83'] ImportGenius US customs records for Hengshun: 44 shipments 2006-2022, one 2022 BOL with 700 pieces of 550mL@24 Chinkiang vinegar. Direct physical evidence of US-bound bottles but sparse and old.
- corroborating: ['p15', 'p16'] 2021 Jiangsu article: Hengshun >65% of China's vinegar exports, sold in >100 countries. Supports high export share but is a promotional claim, not audited.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p34', 'p37', 'p39'] Same 2026 Sina industry article on China vinegar industry; internally consistent context. p37 (US 40% share) conflicts with p3 as noted.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p99', 'p100', 'p101', 'p102'] Same underlying m.x315.cn customs dataset (2020-2022 cumulative HS22090000). p1/p100 and p2/p101 and p3/p102 are duplicate copies of the same measurement; p4/p99 duplicate the all-country total. They 
- conflicting: ['p1', 'p37'] p1/p3 imply the US took ~11.35% of China's vinegar export quantity in 2020-2022, while p37 (industry article) says the US is the largest destination at ~40%. Different periods and possibly different d
- corroborating: ['p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98'] Consistent annual HS22090000 total-export series from one customs aggregator (bianmachaxun): 2020 17.4M L, 2021 20.2M L, 2022 19.6M L, 2023 21.8M L, 2024 25.8M L. These are all-destination totals, not
- conflicting: ['p84', 'p99'] p99's 2020-2022 cumulative all-country total (58.1M L) is close to but not equal to the sum of the annual p97+p96+p93 (57.3M L); minor vintage/definition differences, not a real contradiction.
- corroborating: ['p40', 'p41', 'p42', 'p50', 'p51', 'p52', 'p66', 'p68'] Hengshun vinegar-series production/sales volumes across 2022, 2024, 2025 are mutually consistent in magnitude (~206k-236k t) and growth. These establish the company's total vinegar scale, which bounds
- corroborating: ['p43', 'p44', 'p63', 'p64'] Hengshun foreign-trade (export) segment revenue: 2022 ~43.7M CNY, 2025 ~39.2M CNY (-17.95% yoy). This is the company's total export revenue across all products and destinations, not US vinegar bottles
- corroborating: ['p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121'] ImportGenius bill-of-lading evidence: 44 cumulative US shipments 2006-2022, one 2022 shipment of 700 pieces of 550mL@24 Chinkiang vinegar. p75-p83 and p113-p121 are duplicate copies of the same record
- corroborating: ['p15', 'p16'] 2021 media claim that Hengshun accounts for >65% of China's vinegar exports and sells to >100 countries. Plausible for the leading producer but a promotional figure; treat as an upper-ish share anchor
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p34', 'p37', 'p39'] One industry article (finance.sina) giving China vinegar production 4.8M t, top-5 share 42.3%, Jiangsu 19%, US ~40% of exports. Internally consistent as a single source; the US-share figure conflicts 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | US share of China HS22090000 vinegar export quantity, 2024 | 20 | 8..40 | 8..40 | % | m1 (m1) | Customs p102 implies ~11.35% (2020-2022) while industry p37 claims ~40%. Truth likely between; midpoint ~20% with wide range spanning both. Share, not target level. | 2024 US share of Chinese vinegar export volume lies within the 2020-2022 customs and industry-article range. | A 2024 customs US-specific HS22090000 quantity showing a share well outside 8-40%. |
| a2 | Hengshun share of China's vinegar exports to the US | 40 | 15..65 | 15..65 | % | m1 (m1) | p15 claims >65% of all China vinegar exports (all-destination promotional). For the US specifically Hengshun is the leading brand but faces other exporters, so ~40% with wide range. | Hengshun's US-bound share of Chinese vinegar exports is below its all-destination share. | Bill-of-lading or customs data showing Hengshun's US share near/above 65% or below 15%. |
| a3 | Average bottle fill volume for Hengshun bottled vinegar sold in the US | 500 | 350..750 | 350..750 | millilitres per bottle | m1 (m1), m2 (m2) | Only observed bottle size is 550mL (p117); typical Chinese vinegar retail bottles range 350-750mL. 500mL central with range spanning common sizes. | US-sold Hengshun bottled vinegar averages near 500mL per bottle. | Evidence that US Hengshun sales are dominated by much smaller or larger pack sizes. |
| a4 | Hengshun export share of its total vinegar sales volume, 2024 | 3 | 1..8 | 1..8 | % | m2 (m2) | Hengshun foreign-trade revenue (~39-44M CNY) is ~2-3% of total revenue (~2.2bn CNY) and vinegar is the bulk of exports; export volume share therefore ~1-8%. | Export volume share tracks export revenue share for Hengshun. | Disclosure that Hengshun exports a much larger or smaller fraction of vinegar volume. |
| a5 | US share of Hengshun's vinegar export volume | 30 | 10..55 | 10..55 | % | m2 (m2) | The US is a major but not dominant destination for Chinese vinegar; Hengshun sells to >100 countries (p16). US likely a large minority of its exports. | US is a large minority destination for Hengshun exports. | Evidence that the US is a small (<10%) or dominant (>55%) share of Hengshun exports. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2,787 | ['p84'] / ['a1', 'a2', 'a3'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 2.756 | ['p52'] / ['a3', 'a4', 'a5'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **87.65** bottle, 80% interval [1.041, 7,383] bottle, basis method_spread (interval width set from the disagreement between the methods' estimates), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_confirmed**. 3 candidate(s); entity terms ['hengshun', 'zh', 'zhenjiang', 'zhenjiang hengshun']; measure stems ['bottl', 'hengs', 'zhenj']
Early checks while the sub-agents were running: 2 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p48 | Hengshun total revenue, 2024 | 2,195,870,508 | CNY | 2024-01-01..2024-12-31 | vip.stock.finance.sina.com.cn | different | This is total company revenue in CNY, not a count of bottles of vinegar sold into the US; measure, unit, and scope all differ. |
| p52 | Hengshun vinegar series sales volume 2024 | 212,700 | 万吨 (10,000 tons) of vinegar se | 2024-01-01..2024-12-31 | www.canyin88.com:8080 | different | This is vinegar series sales volume in 10,000 tons (all types, not US-specific, not bottles), so measure, unit, and geographic scope differ. |
| p54 | Hengshun vinegar series revenue 2024 | 1,266,000,000 | 亿元 (100 million yuan) vinegar  | 2024-01-01..2024-12-31 | www.canyin88.com:8080 | different | This is vinegar series revenue in CNY, not a bottle count and not US-specific; measure, unit, and scope differ. |


## Final answer

The best computed estimate is 87.65 bottle (80% model-based interval 1.041 to 7,383 bottle), for Hengshun Group bottled vinegar of all types sold into the US over calendar year 2024. Two routes were averaged with weights of 50% (physical-flow) and 50% (company-level). The physical-flow route multiplies observed China vinegar export quantity 25,760,168 liters by the US share 20% (range 8%–40%), Hengshun's share of US-bound exports 40% (15%–65%), and divides by bottle size 500 mL (350–750). The company route starts from observed Hengshun sales volume 212,700 万吨 (10,000 tons) of vinegar series sales, then applies export share 3% (1%–8%) and US share of exports 30% (10%–55%). Only the two observed points are measured; every share and the bottle size are analyst assumptions, so the interval is conditional on them. The largest risk is that Hengshun's actual US mix and bottle sizes differ from these national-average transfers. The most useful missing evidence would be Hengshun's US export volume or customs data by destination.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 US share of China HS[n] vinegar export quantity, 2024: 20%, range 8% to 40%; used by m1. Overturned by: A 2024 customs US-specific HS[n] quantity showing a share well outside [n]-[n].
- a2 Hengshun share of China's vinegar exports to the US: 40%, range 15% to 65%; used by m1. Overturned by: Bill-of-lading or customs data showing Hengshun's US share near/above [n] or below [n].
- a3 Average bottle fill volume for Hengshun bottled vinegar sold in the US: 500 millilitres per bottle, range 350 to 750; used by m1, m2. Overturned by: Evidence that US Hengshun sales are dominated by much smaller or larger pack sizes.
- a4 Hengshun export share of its total vinegar sales volume, 2024: 3%, range 1% to 8%; used by m2. Overturned by: Disclosure that Hengshun exports a much larger or smaller fraction of vinegar volume.
- a5 US share of Hengshun's vinegar export volume: 30%, range 10% to 55%; used by m2. Overturned by: Evidence that the US is a small (<[n]) or dominant (>[n]) share of Hengshun exports.

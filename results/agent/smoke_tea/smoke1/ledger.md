# Evidence ledger: smoke_tea

- Question: How many cups of tea do people in the United Kingdom drink per day?
- as_of: 2026-10-17
- Pinned target: Total number of cups of tea consumed by people in the United Kingdom per day, averaged over a recent representative day (working interpretation: all tea beverages, hot and iced, consumed by UK residents and visitors within the UK, including tea made at home and out-of-home; excludes herbal/fruit inf | unit cups per day | period 2025-01-01..2025-12-31 | publisher No single official publisher; UK Tea & Infusions Association (UKTIA) and ONS family food/retail data are the closest reference sources

## Directions and pages

### d1 [related_series] Trade association / industry body

Hypothesis: UKTIA and similar bodies publish per-person daily cup counts and total daily cups; target = published cups/person/day × UK population, or directly the published total. Direction: higher population and stable per-capita habit imply total near published figure.

Queries issued by the searcher: UK Tea and Infusions Association cups of tea per day UK; how many cups of tea drunk daily Britain UKTIA average per person; tea.co.uk "100 million cups" tea drunk every day UKTIA fact sheet; UKTIA "Tea Census" 2025 press release cups of tea a day average UK adults

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day?trk=article-ssr-frontend-pulse_little-text` -> **live_dated** (page date 2026-01-01); points raw/verified 13/2
  - p1 Sample size of UK adults survey (Omnibus) = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [keep: ] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p2 Sample size of second UK adults poll (Perspectus Global) = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [keep: ] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `https://myteaplanner.com/tea-statistics` -> **live_dated** (page date 2026-09-30); points raw/verified 12/4
  - p3 US total tea (85 billion, reported as more than 3.9 billion gallons for the year = **85,000,000,000** unspecified (US total tea) (2021-01-01..2021-12-31) [DISCARD: US total tea count in unspecified units; superseded by p4 (gallons) and irrelevant to UK target.] quote: "85 billion The U.S. Census Bureau reported that total as more than 3.9 billion gallons for the year, citing the Tea Association of the U.S.A."
  - p4 US total tea volume in gallons for the year (more than 3.9 billion gallons) = **3,900,000,000** gallons (2021-01-01..2021-12-31) [DISCARD: US total tea volume; different country, irrelevant to UK target.] quote: "The U.S. Census Bureau reported that total as more than 3.9 billion gallons for the year, citing the Tea Association of the U.S.A."
  - p5 US share (84%, Census Bureau tea feature) = **84** % (US tea share) (2021-01-01..2021-12-31) [DISCARD: US tea-type share; no role in UK cups estimate.] quote: "84% The Census Bureau reports green tea at 15%, with oolong, white, and dark teas making up the remaining share cited from the association."
  - p6 US green tea share (15%) = **15** % (US green tea share) (2021-01-01..2021-12-31) [DISCARD: US green-tea share; no role in UK cups estimate.] quote: "The Census Bureau reports green tea at 15%, with oolong, white, and dark teas making up the remaining share cited from the association."
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/2
  - p7 Share of tea drinkers in 2023 Product of the Year survey drinking three or more  = **35** % (2023-01-01..2023-12-31) [DISCARD: Redundant duplicate of p11/p63/p84 (same 35% Product of the Year statistic).] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
  - p8 Annual cups implied for those drinking three or more cups a day = **1,000** cups of tea per person per year (2023-01-01..2023-12-31) [DISCARD: Derived '1,000 cups/year' for heavy drinkers is a rough illustrative figure, not a measured quantity; adds no independen] quote: "This puts them at roughly 1,000 cups each a year"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/2
  - p9 Global tea market estimated value by 2025 (forecast) = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of p31 (same global market forecast, same source).] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p10 UK tea exports value in 2023 = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: Duplicate of p32 (same UK export value, same source).] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
- dropped by code checks: 45 (period_end missing or unparseable: 44; value_as_written not in quote as a whole number: 1)

### d2 [physical_flow] Tea supply chain / trade statistics

Hypothesis: Total cups = tea available for UK consumption (imports + stocks change − exports, in tonnes) × cups per tonne (from average tea bag/leaf weight per cup). Direction: higher net supply implies more cups; conversion factor ~200-250 cups per kg dry tea.

Queries issued by the searcher: UK tea imports tonnes HMRC statistics; United Kingdom tea imports exports tonnes UN Comtrade FAO; grams of tea per tea bag average UK; HMRC UK trade info tea 0902 imports exports tonnes 2024; UK tea imports 2024 117,300 tonnes exports; site:gov.uk tea imports quantity tonnes 2023 2024

- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p11 Share of surveyed tea drinkers drinking three or more cups a day (2023 Product o = **35** % of tea drinkers (2023-01-01..2023-12-31) [DISCARD: Duplicate of p63/p84; keep one copy only.] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- `https://www.thegrocer.co.uk/consumer-trends/cuppa-in-decline-as-brits-drink-870-million-fewer-cups-of-tea/571087.article` -> **live_dated** (page date 2018-08-31); points raw/verified 11/5
  - p12 Decline in UK tea volume purchased (Kantar Worldpanel, 52 w/e 20 May 2018) = **2,600,000** kilograms of tea (2017-05-21..2018-05-20) [keep: ] quote: "The nation bought 2.6 million fewer kilograms of tea, shows Kantar Worldpanel data [52 w/e 20 May 2018], the steepest volume decline in four years."
  - p13 Estimated reduction in cups of tea drunk (derived from 2.6m kg at 3g/teabag) = **866,700,000** cups of tea (2017-05-21..2018-05-20) [keep: ] quote: "As the average teabag contains 3g of leaves, this equates to roughly 866.7 million fewer cups of tea over that period."
  - p14 Growth in value of UK tea market (Kantar Worldpanel, 52 w/e 20 May 2018) = **0.6** percent (2017-05-21..2018-05-20) [DISCARD: Value growth of tea market in 2018; not a volume or cup measure, no role in the estimate.] quote: "Kantar Worldpanel data shows the value of tea has risen by 0.6% to £669.2m over the past year."
  - p15 Value growth of free-from market (Kantar Worldpanel, 52 w/e 26 March 2018) = **37.5** percent (2017-03-27..2018-03-26) [DISCARD: Free-from market value growth; unrelated to tea volume.] quote: "PG Tips launched a brew designed especially for drinking with non-dairy milk in a bid to grab a slice of the growing free-from market, whose value is up 37.5% [Kantar Worldpanel 52 w/e 26 March 2018]."
  - p16 Yorkshire Tea brand value growth (Nielsen, 52 w/e 30 December 2017) = **7.9** percent (2016-12-31..2017-12-30) [DISCARD: Single-brand value growth; not a UK total or conversion factor.] quote: "Yorkshire Tea, which secured the highest value growth of any tea brand in The Grocer's Britain's Biggest Brands (up 7.9% to £88m, Nielsen 52 w/e 30 December 2017)"
- `https://wits.worldbank.org/trade/comtrade/en/country/All/year/2023/tradeflow/Exports/partner/GBR/product/090240` -> **live_dated** (page date 2023-01-01); points raw/verified 15/14
  - p17 Kenya exports of black tea to United Kingdom, quantity = **42,329,900** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Kenya \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 90,657.15 \| 42,329,900 \| Kg \|"
  - p18 India exports of black tea to United Kingdom, quantity = **9,722,010** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| India \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 38,296.47 \| 9,722,010 \| Kg \|"
  - p19 Malawi exports of black tea to United Kingdom, quantity = **21,289,000** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Malawi \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 35,017.18 \| 21,289,000 \| Kg \|"
  - p20 Switzerland exports of black tea to United Kingdom, quantity = **5,219,380** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Switzerland \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 19,043.05 \| 5,219,380 \| Kg \|"
  - p21 Rwanda exports of black tea to United Kingdom, quantity = **5,971,550** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Rwanda \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 15,608.14 \| 5,971,550 \| Kg \|"
  - p22 Tanzania exports of black tea to United Kingdom, quantity = **2,767,650** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Tanzania \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 4,896.63 \| 2,767,650 \| Kg \|"
  - p23 European Union exports of black tea to United Kingdom, quantity = **340,499** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| European Union \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 2,945.22 \| 340,499 \| Kg \|"
  - p24 China exports of black tea to United Kingdom, quantity = **669,591** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| China \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 2,831.30 \| 669,591 \| Kg \|"
  - p25 Sri Lanka exports of black tea to United Kingdom, quantity = **463,014** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Sri Lanka \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 2,614.35 \| 463,014 \| Kg \|"
  - p26 Ethiopia exports of black tea to United Kingdom, quantity = **1,077,100** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Ethiopia(excludes Eritrea) \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 2,260.84 \| 1,077,100 \| Kg \|"
  - p27 United Arab Emirates exports of black tea to United Kingdom, quantity = **986,560** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| United Arab Emirates \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 2,226.13 \| 986,560 \| Kg \|"
  - p28 Argentina exports of black tea to United Kingdom, quantity = **1,001,500** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Argentina \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 1,134.64 \| 1,001,500 \| Kg \|"
  - p29 Burundi exports of black tea to United Kingdom, quantity = **1,081,280** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Burundi \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 933.95 \| 1,081,280 \| Kg \|"
  - p30 Indonesia exports of black tea to United Kingdom, quantity = **439,800** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| Indonesia \| Export \| 090240 \| Black tea (fermented) and partly fermented tea, \| 2023 \| United Kingdom \| 598.01 \| 439,800 \| Kg \|"
- `https://gtaic.ai/files/reports/United_Kingdom_090240_d8bb37d4-0597-484f-aeb9-4ed5f91849a7.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 21 (period_end missing or unparseable: 18; scale word 'million' not supported by quote or table header: 2; scale word 'thousand' not supported by quote or table header: 1)

### d3 [capacity_consumption] Household consumption survey

Hypothesis: Cups/day = UK population × share who drink tea × average cups per tea drinker per day. Direction: survey-based drinking prevalence and frequency constrain the total independently of supply data.

Queries issued by the searcher: percentage of UK adults who drink tea survey average cups per day tea drinkers; UK Tea & Infusions Association tea consumption statistics cups per day; UK Tea & Infusions Association 2026 survey average 4.8 cups tea per day adults; ONS Family Food survey tea consumption UK grams per person per week 2024

- `https://www.comunicaffe.com/tea-brings-brits-together-says-the-uk-tea-and-infusions-association-uktia/` -> **live_dated** (page date 2026-05-20); points raw/verified 15/0
- `https://cravemag.co.uk/6-in-10-brits-still-rely-on-tea-to-stay-calm-new-study-finds/` -> **live_dated** (page date 2025-12-11); points raw/verified 11/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/2
  - p31 Global tea market value forecast for 2025 = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global market value forecast; no UK cups conversion and not a quantity of tea.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025"
  - p32 UK tea export value, 2023 (ranked 7th) = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: UK tea export value; exports are not domestic consumption and value is not volume.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea"
- `https://www.gbnews.com/news/national-tea-day-britons-celebrate-60billion-cups-drunk-per-year-uk` -> **live_dated** (page date 2025-04-21); points raw/verified 3/0
- dropped by code checks: 42 (number: no number in value_as_written: 3; period_end missing or unparseable: 39)

### d4 [related_series] Retail / household food data

Hypothesis: Cups/day = UK household tea purchases (kg/year) × cups per kg / 365, adjusted for out-of-home consumption. Direction: retail purchase volumes give a lower bound on domestic consumption; hospitality adds a share.

Queries issued by the searcher: ONS Family Food tea purchases grams per person per week; UK household tea purchases kg per person per year statistics; Defra Family Food 2023 tea consumption UK; "tea" "grams per person per week" Family Food 2022 UK; site:gov.uk family food tea purchases 2023; UKTIA tea consumption cups per day statistics

- `https://www.gov.uk/government/statistical-data-sets/family-food-datasets` -> **live_dated** (page date 2026-09-17); points raw/verified 0/0
- `https://www.riunit.com/wp-content/uploads/2018/06/Content-Page-for-Tea-Report-Final-2.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.statista.com/topics/8613/tea-market-in-the-united-kingdom/` -> **live_dated** (page date 2025-12-17); points raw/verified 3/0
- `https://farming.co.uk/news/defra-how-british-family-eating-habits-have-changed-since-ww2-` -> **live_dated** (page date 2025-11-13); points raw/verified 14/1
  - p33 Number of UK vineyards, 2015 = **502** vineyards (2015-01-01..2015-12-31) [DISCARD: UK vineyard count; irrelevant.] quote: "The number of vineyards in the UK has increased too, with 502 in 2015 compared to 400 vineyards in the 1980s."
- dropped by code checks: 16 (scale word 'million' not supported by quote or table header: 1; scale word 'billion' not supported by quote or table header: 1; period_end missing or unparseable: 6; period year 1949 does not appear in the page text or URL (likely mis-dated): 1; period_end 2029-12-31 after as_of: 2; number: no number in value_as_written: 1; period year 1989 does not appear in the page text or URL (likely mis-dated): 2; period year 1959 does not appear in the page text or URL (likely mis-dated): 1; period year 1979 does not appear in the page text or URL (likely mis-dated): 1)

### d5 [base_rates] Beverage market / servings

Hypothesis: Cups/day = total UK tea market volume (litres or servings) / average cup volume. Direction: market-size reports in servings or litres convert to cups via standard cup size (~200-250 ml).

Queries issued by the searcher: UK tea market volume litres per year billion cups consumed; UK Tea & Infusions Association tea consumption 100 million cups a day; standard UK mug capacity ml average cup of tea 250ml volume research; Statista tea market United Kingdom volume kg per capita 2025

- `https://www-euromonitor-com.ezproxy.haaga-helia.fi/globalassets/samples/pdf/hot-drinks/coffee/coffee-in-the-uk-sample.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 14/14
  - p34 UK cups of tea drunk per day (UKTIA stated figure) = **100,000,000** cups of tea per day (..) [keep: ] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p35 Global cups of tea drunk per day (UKTIA stated figure) = **5,000,000,000** cups of tea per day (..) [DISCARD: Global cups/day; duplicate of p36 and not the UK target.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p36 Global cups of tea drunk per day (headline statement) = **5,000,000,000** cups of tea per day (..) [DISCARD: Duplicate global headline of p35.] quote: "Tea is loved by Brits whatever their age and 5 billion cups of tea are drunk globally each day versus 2 billion cups of coffee."
  - p37 Global cups of coffee drunk per day = **2,000,000,000** cups of coffee per day (..) [DISCARD: Global coffee cups; irrelevant.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p38 UK cups of coffee drunk per day = **98,000,000** cups of coffee per day (..) [DISCARD: UK coffee cups; not tea, only contextual.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p39 Estimated total global tea consumption (International Tea Committee) = **6,209,000,000** kg of tea (..) [DISCARD: Global tea consumption; wrong scope for UK target.] quote: "Estimated Total Global Consumption 6,209 Million Kg of Tea (Data Source: International Tea Committee)."
  - p40 Assumed average tea quantity per cup used for global conversion = **3** g of tea per cup (..) [keep: ] quote: "Using an average of 3g (per cup), this would equate to over 5 billion cups consumed worldwide every day."
  - p41 Share of 18–24-year-olds having a daily cuppa (UK survey) = **83** % of 18–24-year-olds surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1 (83% of 18–24s daily cuppa); keep p1.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p42 UK adults surveyed in omnibus research = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1 sample size.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p43 UK adults polled in second survey = **1,000** UK adults polled (2023-03-01..2023-05-31) [DISCARD: Duplicate of p2 sample size.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration and boosting mood"
  - p44 Share of younger adults citing great taste as main reason for tea = **80** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Taste-attitude share; no volume role.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p45 Share of over-25s citing great taste as main reason for tea = **85** % of over-25s surveyed (2022-12-01..2022-12-31) [DISCARD: Taste-attitude share; no volume role.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p46 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; no volume role.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p47 Share of young adults brewing a cuppa immediately on waking = **10** proportion of young adults surveyed (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; no volume role.] quote: "Seven out of 10 young adults brew up a cuppa as soon as they get out of bed."
- `https://www.statista.com/topics/8613/tea-market-in-the-united-kingdom/` -> **live_dated** (page date 2025-12-17); points raw/verified 3/1
  - p48 Number of tea processing enterprises in the UK = **133** enterprises (..) [DISCARD: Count of tea processing enterprises; not a consumption quantity.] quote: "- Number of tea processing enterprises in the UK - 133"
- `https://teas.co.uk/wiki/tea-in-a-big-mug/` -> **live_dated** (page date 2026-10-03); points raw/verified 14/14
  - p49 Standard tea bag designed cup volume lower bound = **200** ml (..) [DISCARD: Cup-volume range; retained via p50/p53 etc. but this lower bound duplicates p50's range; keep p50 and p53–p54 as the usa] quote: "Most are made for a cup of about 200 to 250ml."
  - p50 Standard tea bag designed cup volume upper bound = **250** ml (..) [keep: ] quote: "Most are made for a cup of about 200 to 250ml."
  - p51 Small china cup typical fill lower bound = **150** ml (..) [DISCARD: Small china cup fill; not representative of typical UK mug; redundant with standard mug range.] quote: "\| Small china cup \| 150 to 200ml \|"
  - p52 Small china cup typical fill upper bound = **200** ml (..) [DISCARD: Small china cup fill upper bound; redundant.] quote: "\| Small china cup \| 150 to 200ml \|"
  - p53 Standard mug typical fill lower bound = **250** ml (..) [keep: ] quote: "\| Standard mug \| 250 to 300ml \|"
  - p54 Standard mug typical fill upper bound = **300** ml (..) [keep: ] quote: "\| Standard mug \| 250 to 300ml \|"
  - p55 Large builder's mug typical fill lower bound = **350** ml (..) [DISCARD: Large builder's mug; atypical, not the representative cup.] quote: "\| Large "builder's" mug \| 350 to 450ml \|"
  - p56 Large builder's mug typical fill upper bound = **450** ml (..) [DISCARD: Large builder's mug upper bound; redundant.] quote: "\| Large "builder's" mug \| 350 to 450ml \|"
  - p57 Travel flask typical fill lower bound = **450** ml (..) [DISCARD: Travel flask; atypical vessel, not representative.] quote: "\| Travel flask \| 450 to 500ml \|"
  - p58 Travel flask typical fill upper bound = **500** ml (..) [DISCARD: Travel flask upper bound; redundant.] quote: "\| Travel flask \| 450 to 500ml \|"
  - p59 Tetley One Cup tea per bag = **2** g per bag (..) [keep: ] quote: "\| Tetley One Cup \| 72 bags / 144g \| 2g \|"
  - p60 Tetley Original tea per bag = **3.1** g per bag (..) [keep: ] quote: "\| Tetley Original \| 80 bags / 250g \| 3.1g \|"
  - p61 Yorkshire Tea Original tea per bag = **3.1** g per bag (..) [keep: ] quote: "\| Yorkshire Tea Original \| 80 bags / 250g \| 3.1g \|"
  - p62 Example milk volume in finished 400ml tea = **50** ml (..) [DISCARD: Milk-volume example for a 400ml brew; not needed for cups conversion.] quote: "400ml of finished tea with 50ml of milk in it means you are brewing 350ml of tea, not 400ml."
- dropped by code checks: 2 (scale word 'million' not supported by quote or table header: 1; scale word 'billion' not supported by quote or table header: 1)

### d6 [own_history] Historical trend

Hypothesis: Past published estimates of UK daily cups (e.g., '165 million cups a day') can be updated for population and per-capita decline in tea drinking. Direction: older totals adjusted downward for falling consumption give a plausible current range.

Queries issued by the searcher: 165 million cups of tea a day UK UKTIA; UK tea consumption decline per capita trend cups per day; how many cups of tea Britain history million a day 100 million; BBC tea bags per person per week 1974 30 teabags 2023 10 National Food Survey; UKTIA "165 million" cups tea day "100 million" cups infusions difference

- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p63 Share of surveyed tea drinkers drinking three or more cups a day (2023 Product o = **35** % of surveyed tea drinkers (2023-01-01..2023-12-31) [keep: ] quote: "the just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- `https://fortune.com/europe/2024/07/03/how-young-brits-are-reigniting-love-for-the-classic-cuppa-amidst-a-crisis-of-relevance/` -> **live_dated** (page date 2024-07-03); points raw/verified 15/6
  - p64 Yorkshire Tea revenue growth 2023 = **21** % growth in value (revenue) (2023-01-01..2023-12-31) [DISCARD: Single-brand revenue growth; not a UK total.] quote: "Yorkshire Tea is certainly unusual in having enjoyed recent growth in both value (revenue) and volume (the number of tea bags sold), at 21% and 12%, respectively, in 2023."
  - p65 Yorkshire Tea volume growth 2023 = **12** % growth in volume (tea bags sold) (2023-01-01..2023-12-31) [DISCARD: Single-brand volume growth; not a UK total.] quote: "Yorkshire Tea is certainly unusual in having enjoyed recent growth in both value (revenue) and volume (the number of tea bags sold), at 21% and 12%, respectively, in 2023."
  - p66 Bettys & Taylors turnover 2023 = **295,700,000** GBP (£) (2023-01-01..2023-12-31) [DISCARD: Single-company turnover; not a UK consumption quantity.] quote: "Bettys & Taylors, which owns domestic market leader Yorkshire Tea, grew turnover 14% to £295.7 million ($375.5 million)."
  - p67 Bettys & Taylors turnover growth 2023 = **14** % growth in turnover (2023-01-01..2023-12-31) [DISCARD: Single-company turnover growth; not a UK total.] quote: "grew turnover 14% to £295.7 million ($375.5 million)."
  - p68 Kallo Foods (Clipper Teas) sales 2023 = **121,700,000** GBP (£) (2023-01-01..2023-12-31) [DISCARD: Single-company sales; not a UK total.] quote: "Kallo Foods, which owns Clipper Teas, jumped 8% to £121.7 million ($155.5 million) in 2023"
  - p69 Global at-home tea market value 2024 (Statista) = **127,000,000,000** USD ($) (2024-01-01..2024-12-31) [DISCARD: Global at-home market value; no UK cups conversion.] quote: "the global at-home tea market-worth $127 billion in 2024, according to Statista-is growing, at a compound annual growth rate of 6%."
- `https://www.publicsectorcatering.co.uk/news/research-finds-brits-drink-165-million-cups-tea-every-day` -> **live_dated** (page date 2019-09-26); points raw/verified 5/0
- `http://downloads.bbc.co.uk/worldservice/learningenglish/6minute/101209_6min_tea.pdf` -> **live_dated** (page date 2010-12-20); points raw/verified 4/0
- dropped by code checks: 32 (period_end missing or unparseable: 30; number: no number in value_as_written: 2)

### d7 [shocks] Recent disruptions and price effects

Hypothesis: Tea prices, cost-of-living pressure, and changing work patterns (home vs office) shift where and how much tea is drunk; measurable price/volume changes constrain whether historical per-capita rates still apply.

Queries issued by the searcher: ONS CPI tea price index UK tea prices 2024 2025; UK tea sales volume change cost of living 2023 2024 UKTIA; tea consumption UK pandemic change out of home sales; UKTIA how many cups of tea drunk in UK per day 2024 2025; ONS CPI tea index 01.2.1.2 tea price annual 2025; UK tea market volume sales 2024 decline 1.6% 2025; out of home tea sales UK 2023 2024 foodservice tea volume

- `https://www.just-drinks.com/newsletters/in-data-global-tea-coffee-value-sales-to-slow-until-2027/` -> **live_dated** (page date 2024-06-05); points raw/verified 15/8
  - p70 Global tea value sales CAGR 2021-2024 (13 key markets) = **7.8** % compound annual growth rate (2021-01-01..2024-12-31) [DISCARD: Global value CAGR; not a UK volume signal.] quote: "the compound annual growth rate (CAGR) of overall value sales for tea will fall from 7.8% between 2021 and 2024 to 4.8% between 2024 and 2027"
  - p71 Global coffee value sales CAGR 2021-2024 (13 key markets) = **5.9** % compound annual growth rate (2021-01-01..2024-12-31) [DISCARD: Global coffee CAGR; irrelevant.] quote: "For coffee, the CAGR will fall from 5.9% to 5% during the same periods"
  - p72 UK tea sales value growth 2023-2024 = **12.3** % change in value sales (2023-01-01..2024-12-31) [keep: ] quote: "In the UK specifically, tea's sales value jumped 12.3% between 2023 and 2024, despite volume sales declining 1.6%."
  - p73 UK tea volume sales change 2023-2024 = **1.6** % decline in volume sales (2023-01-01..2024-12-31) [keep: ] quote: "In the UK specifically, tea's sales value jumped 12.3% between 2023 and 2024, despite volume sales declining 1.6%."
  - p74 US tea value growth 2023-2024 = **7.4** % change in value sales (2023-01-01..2024-12-31) [DISCARD: US tea value growth; not UK.] quote: "The US is similar, with value growth across tea and coffee (7.4% and 2.9% respectively), but lagging volume growth of 3.8% and 0.4% respectively."
  - p75 US coffee value growth 2023-2024 = **2.9** % change in value sales (2023-01-01..2024-12-31) [DISCARD: US coffee value growth; irrelevant.] quote: "The US is similar, with value growth across tea and coffee (7.4% and 2.9% respectively), but lagging volume growth of 3.8% and 0.4% respectively."
  - p76 US tea volume growth 2023-2024 = **3.8** % change in volume sales (2023-01-01..2024-12-31) [DISCARD: US tea volume growth; not UK.] quote: "but lagging volume growth of 3.8% and 0.4% respectively"
  - p77 US coffee volume growth 2023-2024 = **0.4** % change in volume sales (2023-01-01..2024-12-31) [DISCARD: US coffee volume growth; irrelevant.] quote: "but lagging volume growth of 3.8% and 0.4% respectively"
- `https://www.standard.co.uk/business/business-news/inflation-office-for-national-statistics-ons-energy-bills-tea-b1243721.html` -> **live_dated** (page date 2025-08-20); points raw/verified 15/0
- `https://www.thecaterer.com/products--equipment/trends-in-tea-targeting-a-smaller-market` -> **live_dated** (page date 2024-10-28); points raw/verified 8/1
  - p78 Chai latte growth in 2023 (Mintel) = **94** % growth (2023-01-01..2023-12-31) [DISCARD: Chai latte growth; niche segment, no total-cups role.] quote: "Mintel figures show chai latte saw 94% growth in 2023"
- `https://www.foodmanufacture.co.uk/Article/2020/08/03/Coronavirus-lockdown-boosted-retail-dairy-sales-of-milk-cheese-butter/` -> **live_dated** (page date 2020-08-03); points raw/verified 11/3
  - p79 Increase in cups of tea drunk over the peak lockdown period versus prior period = **21** percent (2020-05-17..2020-07-12) [DISCARD: Lockdown-period change in cups; a shock, not a level, and period is 2020.] quote: "an increase of 21% and 19% respectively"
  - p80 Increase in cups of coffee drunk over the peak lockdown period versus prior peri = **19** percent (2020-05-17..2020-07-12) [DISCARD: Lockdown coffee change; irrelevant.] quote: "an increase of 21% and 19% respectively"
  - p81 Year-on-year increase in weekly butter sales in week commencing 22 March (Kantar = **69** percent (2020-03-22..2020-03-28) [DISCARD: Butter sales spike; irrelevant.] quote: "with a year-on-year increase of 69% in weekly sales, Kantar reported"
- dropped by code checks: 37 (period_end 2027-12-31 after as_of: 2; scale word 'billion' not supported by quote or table header: 6; period_end missing or unparseable: 12; period year 2025 does not appear in the page text or URL (likely mis-dated): 15; period_end 2028-12-31 after as_of: 1; number: no number in value_as_written: 1)

### b1 [related_series] trade association / market research

Hypothesis: A current (2024-2025) UKTIA or Kantar/Nielsen figure for UK tea volume (kg) or cups/day would replace the undated p34 headline and let d2/d4 be anchored to a recent year, resolving the p34-vs-retail-volume conflict.

Queries issued by the searcher: UKTIA cups of tea per day 2024 statistics UK tea consumption; Kantar Worldpanel UK tea volume kg 2024; Defra Family Food 2024 tea purchases grams per person per week; "tea" UK household consumption "grams per person per week" 2023 2024 Family Food

- `https://www.gov.uk/government/statistics/family-food-fye-2024` -> **live_dated** (page date 2025-11-06); points raw/verified 0/0
- `https://www.tea.co.uk/assets/uploads/files/news/4ea32-uk-tea-report-2023-3149-for-web-spreads.pdf` -> **live_dated** (page date 2023-05-05); points raw/verified 15/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/2
  - p82 Global tea market value forecast for 2025 (USD) = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global market value forecast; wrong scope and a forecast, not an outcome.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p83 UK tea export value in 2023 (USD) = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: UK tea export value; exports are not consumption.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p84 Share of tea drinkers in 2023 Product of the Year survey drinking three or more  = **35** % of surveyed tea drinkers (2023-01-01..2023-12-31) [keep: ] quote: "the just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- dropped by code checks: 42 (period_end missing or unparseable: 40; number: no number in value_as_written: 2)

### b2 [physical_flow] customs / trade statistics

Hypothesis: Complete UK tea import volume (all HS 0902 lines, all reporters, plus re-exports and stock change) would let d2 produce a full supply-based cups/day estimate rather than the partial black-tea floor from p17-p30.

Queries issued by the searcher: HMRC UK trade info tea imports 0902 tonnes 2024; UN Comtrade United Kingdom tea imports 2023 quantity tonnes HS 0902; wits.worldbank.org United Kingdom imports 2024 product 0902 tea world quantity Kg; UK tea imports tonnes per year UKTIA "tea imports" 2024 statistics

- `https://www.vietnam.vn/hu/viet-nam-la-thi-truong-cung-cap-che-thu-14-cho-anh` -> **live_dated** (page date 2025-03-15); points raw/verified 15/2
  - p85 UK black tea imports 2024 vs 2023, value growth = **20** % (2024-01-01..2024-12-31) [DISCARD: Value growth percentage of imports; not a quantity and not needed.] quote: "mennyiségben 17,6%-os, értékben pedig 20%-os növekedést jelent 2023-hoz képest"
  - p86 Vietnam tea exports to UK 2024, quantity (14th largest supplier) = **994** tonnes (2024-01-01..2024-12-31) [keep: ] quote: "2024-ben Vietnam volt az Egyesült Királyság 14. legnagyobb teaszállítója, elérve a 994 tonnát, 2,01 millió USD értékben"
- `https://gtaic.ai/files/reports/United_Kingdom_090240_d8bb37d4-0597-484f-aeb9-4ed5f91849a7.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://wits.worldbank.org/trade/comtrade/en/country/GBR/year/2024/tradeflow/Imports/partner/ALL/product/090230` -> **live_dated** (page date 2024-01-01); points raw/verified 15/14
  - p87 UK total world imports of black tea (HS 090230), quantity, 2024 = **11,182,300** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| World \| 73,469.38 \| 11,182,300 \| Kg \|"
  - p88 UK imports of black tea (HS 090230) from Kenya, quantity, 2024 = **6,317,170** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Kenya \| 26,944.27 \| 6,317,170 \| Kg \|"
  - p89 UK imports of black tea (HS 090230) from Poland, quantity, 2024 = **1,368,030** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Poland \| 10,859.35 \| 1,368,030 \| Kg \|"
  - p90 UK imports of black tea (HS 090230) from Sri Lanka, quantity, 2024 = **584,772** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Sri Lanka \| 7,783.22 \| 584,772 \| Kg \|"
  - p91 UK imports of black tea (HS 090230) from Germany, quantity, 2024 = **314,550** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Germany \| 6,353.32 \| 314,550 \| Kg \|"
  - p92 UK imports of black tea (HS 090230) from Turkey, quantity, 2024 = **619,486** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Turkey \| 6,318.66 \| 619,486 \| Kg \|"
  - p93 UK imports of black tea (HS 090230) from India, quantity, 2024 = **897,676** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| India \| 5,233.29 \| 897,676 \| Kg \|"
  - p94 UK imports of black tea (HS 090230) from Ireland, quantity, 2024 = **475,425** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Ireland \| 2,742.49 \| 475,425 \| Kg \|"
  - p95 UK imports of black tea (HS 090230) from United Arab Emirates, quantity, 2024 = **192,185** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| United Arab Emirates \| 2,004.20 \| 192,185 \| Kg \|"
  - p96 UK imports of black tea (HS 090230) from China, quantity, 2024 = **52,737** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| China \| 656.54 \| 52,737 \| Kg \|"
  - p97 UK imports of black tea (HS 090230) from Pakistan, quantity, 2024 = **88,351** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Pakistan \| 529.55 \| 88,351 \| Kg \|"
  - p98 UK imports of black tea (HS 090230) from Indonesia, quantity, 2024 = **11,259** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Indonesia \| 423.17 \| 11,259 \| Kg \|"
  - p99 UK imports of black tea (HS 090230) from France, quantity, 2024 = **12,067** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| France \| 274.73 \| 12,067 \| Kg \|"
  - p100 UK imports of black tea (HS 090230) from United States, quantity, 2024 = **7,944** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| United States \| 238.24 \| 7,944 \| Kg \|"
- `https://wits.worldbank.org/trade/comtrade/en/country/GBR/year/2023/tradeflow/Imports/partner/ALL/product/090220` -> **live_dated** (page date 2023-01-01); points raw/verified 12/0
- dropped by code checks: 26 (number: more than one number in value_as_written: 13; scale word 'thousand' not supported by quote or table header: 7; period_end missing or unparseable: 6)

### b3 [base_rates] survey prevalence and frequency

Hypothesis: A representative UK survey giving share of adults drinking tea and mean cups per drinker per day would let d3 produce an independent total, cross-checking p34 and constraining the largest uncertainty (per-capita frequency).

Queries issued by the searcher: UK tea drinking prevalence survey 2024 cups per day adults; YouGov tea drinking habits UK 2024 cups per day; Statista UK tea consumption frequency adults 2024; UK adults drink tea daily 48% Mintel 2024 average cups per day; "cups of tea" "a day" survey UK adults average 2025; UKTIA survey 2025 cups tea day 44% 1-2 35% 3-4 20% 5-6

- `https://cravemag.co.uk/6-in-10-brits-still-rely-on-tea-to-stay-calm-new-study-finds/` -> **live_dated** (page date 2025-12-11); points raw/verified 11/11
  - p101 UK adults surveyed who drink tea to calm down (share of over 1,000 adults polled = **60** % of adults surveyed (..) [DISCARD: Share drinking tea to calm down; attitudinal, not a consumption quantity.] quote: "nearly two thirds (60%) polled in our real-world study of over 1,000 adults1 saying they drink tea to get them to calm down"
  - p102 UK adults aged 25-34 who agree they drink tea to calm down (share of that age gr = **83** % of adults aged 25-34 surveyed (..) [DISCARD: Attitudinal share by age; not a consumption quantity.] quote: "twice as many younger adults (25-34 years category; 83%) agreed with this statement"
  - p103 UK adults aged 65+ who agree they drink tea to calm down (share of that age grou = **38** % of adults aged 65+ surveyed (..) [DISCARD: Attitudinal share by age; not a consumption quantity.] quote: "compared with the older generation (65+ years category; 38%)"
  - p104 UK people drinking at least one cup of tea a day (share of surveyed people) = **10** share of people surveyed (..) [keep: ] quote: "which shows that more than nine in 10 people drink at least one cup of tea a day"
  - p105 UK people drinking the recommended three to four cups of tea a day (share of sur = **35** % of people surveyed (..) [keep: ] quote: "Over a third (35%) drink the recommended three to four cups"
  - p106 UK people drinking one or two cups of tea a day (share of surveyed people) = **44** % of people surveyed (..) [keep: ] quote: "while four in 10 (44%) drink one or two a day"
  - p107 UK people drinking five to six cups of tea a day (share of surveyed people) = **20** % of people surveyed (..) [keep: ] quote: "and a thirsty one in five (20%) drink five to six cups a day"
  - p108 UK adults surveyed who brew tea for thinking time (share of Brits surveyed) = **64** % of Brits surveyed (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "nearly two thirds (64%) of Brits like to brew a tea to give them some thinking time"
  - p109 UK adults surveyed who would pick regular tea as their only hot drink (share of  = **66** % of adults surveyed (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "the top answer (66%) was a regular cup of tea, whatever their age"
  - p110 UK adults surveyed who agree a cuppa gives comfort (share of Brits surveyed) = **59** % of Brits surveyed (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "nearly six in 10 (59%) agreed that having a cuppa gives people comfort"
  - p111 UK survey sample size of adults polled = **1,000** adults surveyed (..) [DISCARD: Sample size only; no usable quantity.] quote: "polled in our real-world study of over 1,000 adults1"
- `https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation` -> **live_dated** (page date 2025-06-30); points raw/verified 15/15
  - p112 Share of British adults drinking tea at home or at work at least twice a day = **41** % of British adults (..) [keep: ] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p113 Share of British adults drinking coffee at home or at work at least twice a day = **40** % of British adults (..) [DISCARD: Coffee share; not tea.] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p114 Share of tea drinkers buying tea out-of-home (takeaway/café) at least once a wee = **16** % of tea drinkers (..) [keep: ] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p115 Share of coffee drinkers buying coffee out-of-home (takeaway/café) at least once = **12** % of coffee drinkers (..) [DISCARD: Coffee out-of-home share; not tea.] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p116 Share of Gen Z drinking tea daily = **11** % of Gen Z (..) [keep: ] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p117 Share of Gen Z drinking coffee daily = **8** % of Gen Z (..) [DISCARD: Coffee daily share; not tea.] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p118 Share of Millennials drinking tea daily = **23** % of Millennials (..) [keep: ] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p119 Share of Millennials drinking coffee daily = **24** % of Millennials (..) [DISCARD: Coffee daily share; not tea.] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p120 Share of Gen X drinking tea daily = **31** % of Gen X (..) [keep: ] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p121 Share of Gen X drinking coffee daily = **33** % of Gen X (..) [DISCARD: Coffee daily share; not tea.] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p122 Share of Baby Boomers drinking tea daily = **32** % of Baby Boomers (..) [keep: ] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p123 Share of Baby Boomers drinking coffee daily = **32** % of Baby Boomers (..) [DISCARD: Coffee daily share; not tea.] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p124 Share of daily tea drinkers nationally choosing green tea = **20** % of daily tea drinkers (..) [DISCARD: Green-tea share among daily drinkers; not a total consumption quantity.] quote: "32% of Gen Z daily tea drinkers opt for green tea (vs. 20% nationally)"
  - p125 Share of daily tea drinkers nationally choosing fruit tea = **13** % of daily tea drinkers (..) [DISCARD: Fruit-tea share; excluded from target scope and not a total.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)"
  - p126 Share of daily tea drinkers nationally choosing herbal tea = **16** % of daily tea drinkers (..) [DISCARD: Herbal-tea share; excluded from target scope.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/14
  - p127 Share of UK residents who drink tea daily (UKTIA, May) = **98** % of UK residents (..) [keep: ] quote: "In May, the UK Tea & Infusions Association (UKTIA) revealed that 98% of UK residents drink tea daily."
  - p128 Cups of tea drunk every day in the UK (ITC estimate, cited by UKTIA) = **100,000,000** cups per day (..) [keep: ] quote: ""More than 100 million cups of tea are drunk every day here in the UK," she said, citing the International Tea Committee (ITC)"
  - p129 ITC estimate of UK tea consumption per year = **36,000,000,000** cups per year (..) [keep: ] quote: "which estimates consumption at 36 billion cups per year."
  - p130 Number of adults surveyed in March (UKTIA survey) = **1,010** adults surveyed (..) [DISCARD: Sample size only.] quote: "Hall explains that nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
  - p131 Share of surveyed adults choosing tea bags to make black tea = **84** % of surveyed adults (..) [DISCARD: Tea-bag vs loose-leaf share; not a consumption quantity.] quote: ""It's no surprise that 84% pick the option of a tea bag to make their black tea, with 16% opting for loose leaf,""
  - p132 Share of surveyed adults choosing loose leaf to make black tea = **16** % of surveyed adults (..) [DISCARD: Loose-leaf share; not a consumption quantity.] quote: "with 16% opting for loose leaf," said Hall."
  - p133 Share of surveyed adults drinking black tea without milk = **24** % of surveyed adults (..) [DISCARD: Milk/no-milk share; not a consumption quantity.] quote: "nearly a quarter (24%) said they drink their black tea as it comes, without any milk"
  - p134 Share of UK fluid intake that is tea (Tea Advisory Panel) = **40** % of nation's fluid intake (..) [DISCARD: Share of fluid intake; not a cup count.] quote: "even today, 40% of the nation's fluid intake will be tea, according to the Tea Advisory Panel (TAP)."
  - p135 Statista estimate of UK tea consumption annually (excludes herbal, RTD, instant) = **72,000,000** kilos per year (..) [keep: ] quote: "Statista Market Insights estimates UK consumption at 72 million kilos annually, excluding herbal infusions, ready-to-drink, and instant tea."
  - p136 UK tea market value (Statista) = **1,700,000,000** GBP (£) (..) [DISCARD: Market value; not a volume or cup count.] quote: "According to Statista market research, the UK market is valued at £1.7 billion ($2.2 billion)."
  - p137 Average UK tea spend per person per week (Statista) = **15** pence per person per week (..) [DISCARD: Spend per person; not a volume or cup count.] quote: "According to Statista, UK residents spend an average of 15 pence per person per week on tea."
  - p138 Global tea market forecast value by 2025 = **134,400,000,000** USD ($) (2025-01-01..2025-12-31) [DISCARD: Global market forecast; wrong scope.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p139 FAO estimate of global tea production = **6,700,000** tons (..) [DISCARD: Global production; wrong scope.] quote: "According to the UN Food and Agriculture Organization (FAO), tea production is nearing 6.7 million tons."
  - p140 Number of tea enterprises located in the UK = **122** enterprises (..) [DISCARD: Enterprise count; irrelevant.] quote: "Several of the 122 enterprises located there have been in operation for centuries."
- `https://www.gloucestershirelive.co.uk/news/uk-world-news/cuppa-tea-time-out-ashley-9270017` -> **live_dated** (page date 2024-05-08); points raw/verified 15/14
  - p141 Share of tea drinkers who believe a brew can be a mindful moment = **64** % of tea drinkers (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "64 per cent of tea drinkers believe sipping on a brew can be a mindful moment."
  - p142 Share of tea drinkers citing positivity boost as reason for a cuppa = **32** % of tea drinkers (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "And getting a boost of positivity (32 per cent), clearing their mind (31 per cent) and a burst of motivation (21 per cent) are among the reasons for enjoying a cuppa."
  - p143 Share of tea drinkers citing clearing their mind as reason for a cuppa = **31** % of tea drinkers (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "And getting a boost of positivity (32 per cent), clearing their mind (31 per cent) and a burst of motivation (21 per cent) are among the reasons for enjoying a cuppa."
  - p144 Share of tea drinkers citing burst of motivation as reason for a cuppa = **21** % of tea drinkers (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "And getting a boost of positivity (32 per cent), clearing their mind (31 per cent) and a burst of motivation (21 per cent) are among the reasons for enjoying a cuppa."
  - p145 Share of people needing breaks to clear their heads = **42** % of people (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "Research has shown that 42 per cent of people need to take breaks to clear their heads, with 32 per cent stating that an overactive mind makes it difficult for them to sort out their problems."
  - p146 Share stating an overactive mind makes sorting problems difficult = **32** % of people (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "Research has shown that 42 per cent of people need to take breaks to clear their heads, with 32 per cent stating that an overactive mind makes it difficult for them to sort out their problems."
  - p147 Share of tea drinkers finding a cup of tea is what they need when solving a prob = **69** % of tea drinkers (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "Consequently, 69 per cent of tea drinkers find that a cup of tea is exactly what they need when they have a problem to solve."
  - p148 Share of those individuals saying a brew allows them to come up with solutions = **22** % of individuals (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "22 per cent of these individuals say that having a brew allows them to come up with solutions because it gives them the ability to think - a crucial element in daily progress."
  - p149 Share choosing tea to help organise thoughts = **38** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "The survey, conducted by OnePoll, also revealed that 38 per cent choose a cup of tea to help them organise their thoughts, more than those who would opt for a coffee (32 per cent), turn to a friend (2"
  - p150 Share opting for coffee to organise thoughts = **32** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "e a cup of tea to help them organise their thoughts, more than those who would opt for a coffee (32 per cent), turn to a friend (25 per cent) or write in a journal (11 per cent) in the same situation."
  - p151 Share turning to a friend to organise thoughts = **25** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "e a cup of tea to help them organise their thoughts, more than those who would opt for a coffee (32 per cent), turn to a friend (25 per cent) or write in a journal (11 per cent) in the same situation."
  - p152 Share writing in a journal to organise thoughts = **11** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "e a cup of tea to help them organise their thoughts, more than those who would opt for a coffee (32 per cent), turn to a friend (25 per cent) or write in a journal (11 per cent) in the same situation."
  - p153 Share feeling refreshed after a tea break = **48** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "It was also found that 48 per cent feel refreshed after a tea break, with 26 per cent feeling happy and 23 per cent uplifted."
  - p154 Share feeling happy after a tea break = **26** % of respondents (..) [DISCARD: Attitudinal share; not a consumption quantity.] quote: "It was also found that 48 per cent feel refreshed after a tea break, with 26 per cent feeling happy and 23 per cent uplifted."
- dropped by code checks: 2 (number: no number in value_as_written: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['tea consumption', 'uk tea', 'cups per day']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p34', 'p38'] Same UKTIA page, same statement: UK tea ~100m cups/day vs coffee 98m cups/day. Shared source, so not independent; p34 is the only direct UK total-cups figure and is the anchor for d1/d6.
- corroborating: ['p35', 'p36', 'p37', 'p39', 'p40'] Same UKTIA page: global 5bn cups/day derived from 6,209m kg global consumption at 3g/cup. Internally consistent but a single source; p40 (3g/cup) is the useful conversion factor, p39 is the global sup
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30'] WITS bilateral black-tea export quantities to the UK for 2023; each is a distinct reporter so they are independent of each other, but they cover only HS 090240 black tea and only these reporters, so t
- corroborating: ['p59', 'p60', 'p61', 'p40', 'p13'] Tea mass per cup/bag: 2g (one-cup bag), 3.1g (standard bags), 3g (UKTIA global conversion), and 3g/teabag used in p13. Consistent 2-3.1 g/cup band; supports a cups-per-kg conversion of roughly 320-500
- corroborating: ['p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58'] Cup/mug fill volumes 150-500ml; supports a ~200-300ml typical serving for any litres-to-cups conversion (d5).
- corroborating: ['p7', 'p11', 'p63', 'p8'] Same Product of the Year 2023 survey reported three times (35% of tea drinkers have 3+ cups/day; ~1000 cups/yr for that group). Redundant copies of one survey; usable as a frequency distribution input
- corroborating: ['p1', 'p2', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47'] UKTIA-cited omnibus/Perspectus surveys: sample sizes and attitudinal shares. They establish prevalence/attitudes but give no total-cups figure; p41 (83% of 18-24s daily) is a prevalence input for d3.
- corroborating: ['p12', 'p13', 'p14'] Kantar 2018: 2.6m kg volume decline equated to 866.7m fewer cups at 3g/bag, and £669.2m market value. Confirms the 3g/cup conversion and gives a historical market-size anchor; period is 2018 so only u
- corroborating: ['p72', 'p73'] Just-drinks: UK tea value +12.3% but volume -1.6% 2023-2024. Supports a modest downward drift in per-capita volume, relevant to updating p34.
- corroborating: ['p3', 'p4', 'p5', 'p6'] US tea totals and shares from one myteaplanner/Census/Tea Association chain; internally consistent but about the US, not the UK.
- corroborating: ['p9', 'p31'] Identical global market value forecast ($134.4bn by 2025) from the same stir-tea-coffee page; duplicate.
- corroborating: ['p10', 'p32'] Identical UK tea export value 2023 ($121.4m) from the same page; duplicate.
- conflicting: ['p34', 'p12', 'p13'] p34's 100m cups/day implies ~36.5bn cups/yr; at 3g/cup that is ~110m kg dry tea, far above the ~2.6m kg annual decline and the ~£669m 2018 market. The gap is explained by p34 being a trade-association
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p34', 'p128', 'p129'] All three trace to the same UKTIA/International Tea Committee headline of ~100 million cups/day (36 billion cups/year ÷ 365 ≈ 98.6 million). They are not independent measurements; they are one trade-a
- corroborating: ['p135', 'p40', 'p59', 'p60', 'p61'] Statista's 72 million kg/year (p135) and the 3 g/cup conversion (p40) plus tea-bag weights of 2–3.1 g (p59–p61) are mutually consistent: 72e6 kg × ~333 cups/kg ≈ 24 billion cups/year ≈ 66 million cups
- corroborating: ['p87', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p86'] WITS bilateral black-tea import records (2023 HS 090240 and 2024 HS 090230) are the same underlying customs measurement from different reporters/years. They give a partial black-tea import floor (~90–
- conflicting: ['p104', 'p105', 'p106', 'p107', 'p127'] p104 states 'more than nine in 10' drink at least one cup daily (value parsed as 10, likely a mis-parse of 90%), while p127 claims 98% drink tea daily. Both are implausibly high versus YouGov generati
- corroborating: ['p116', 'p118', 'p120', 'p122', 'p112'] YouGov generational daily-tea shares (11–32%) and the 41% 'at least twice a day' figure are consistent with a moderate daily-drinking prevalence, far below the 90–98% claims. These are the more credib
- corroborating: ['p72', 'p73'] Value up 12.3% while volume down 1.6% (2023–2024) is a coherent price-inflation/volume-decline signal; supports a mild downward drift in per-capita volume, not a level.
- corroborating: ['p12', 'p13'] Kantar 2.6m kg decline and the derived 866.7m cups (at 3 g/bag) are the same measurement; the 3 g/cup conversion corroborates p40 and the tea-bag weights.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a2 | Cups per kg of dry tea (inverse of grams per cup) | 333 | 250..500 | 250..500 | cups/kg | unused | Derived from 2-3.1 g per bag (p59-p61) and the 3 g/cup convention (p40); 333 cups/kg corresponds to 3 g/cup, with range spanning 2-4 g/cup. | Converting UK tea mass (kg) to cups for a recent year. | Evidence that typical UK cups use materially more or less than 2-4 g of dry tea. |
| a3 | Share of UK adults drinking tea on a given day | 0.45 | 0.3..0.6 | 0.3..0.6 | fraction | unused | YouGov generational daily shares (p116-p122, 11-32%) and the 41% 'twice a day' figure (p112) imply a moderate daily prevalence; the 90-98% claims (p104, p127) are implausibly high. Assumed central 45% with wide range. | Capacity x frequency decomposition of daily cups for UK adults. | A representative survey showing daily tea-drinking prevalence well outside 30-60%. |
| a4 | Mean cups per tea drinker per day | 2.5 | 1.5..4 | 1.5..4 | cups/day | unused | Distributional survey (p105-p107: 44% one-two, 35% three-four, 20% five-six) implies a mean around 2.5-3 cups among drinkers; assumed 2.5 with wide range. | Capacity x frequency decomposition of daily cups for UK adults. | A representative survey showing mean cups per drinker outside 1.5-4. |
| a5 | Share of UK population who are adults | 0.78 | 0.75..0.81 | 0.5511..1.102 (widened) | fraction | unused | ONS: adults (~18+) are roughly 78% of the UK population; used to apply adult-based prevalence to the national total. | Scaling adult survey prevalence to the whole UK population. | ONS age structure showing adult share outside 75-81%. |
| a6 | UK resident population 2025 | 69,000,000 | 68,000,000..70,000,000 | 48,785,244..97,570,487 (widened) | people | unused | ONS mid-year UK population is ~68-69 million in the mid-2020s; used to convert per-capita prevalence into a national daily total. No kept point supplies population, so it is assumed. | Converting adult prevalence and frequency into a national daily cup total for 2025. | An ONS 2025 population estimate outside 68-70 million. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p135'] / ['a2'] | [] |  | 0.00 |  | formula names ['a2', 'k_days_per_year', 'p135'] != inputs ['a2', 'p135'] |
| m2 | formula_mc | 100,143,953 | ['p34'] / [] | [] |  | 1.00 | equal |  |
| m3 | formula_mc | n/a | ['p87'] / ['a2'] | [] |  | 0.00 |  | formula names ['a2', 'k_days_per_year', 'p87'] != inputs ['a2', 'p87'] |
| m4 | formula_mc | n/a | [] / ['a3', 'a4', 'a5', 'a6'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: only black tea imports of channel (siblings green/other tea, stock change and re-exports)
- m4 coverage: the whole target

Result: central **100,143,953** cup/day, 80% interval [72,691,233, 137,964,523] cup/day, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['uk', 'united kingdom']; measure stems ['consu', 'cup', 'peopl', 'tea']


## Final answer

The best computed estimate is 100,143,953 cup/day (80% model-based interval 72,691,233 to 137,964,523 cup/day), for UK-wide tea consumption averaged over a recent representative day in 2025, covering hot and iced tea drunk at home and out of home, excluding herbal/fruit infusions. The combination rests almost entirely on the trade-association headline of 100,000,000 cups of tea per day cups per day (method m2, weight 100%); the supply route using 72,000,000 kilos per year kg/year and the import floor from 11,182,300 Kg kg were not combined. Observed anchors are the headline, the Statista volume and the black-tea import quantity; the cups-per-kg conversion and prevalence/frequency inputs are assumptions, so the capacity decomposition (m4) is assumption-driven. The headline is a single, possibly dated source, so the main risk is that it overstates current consumption after years of decline. The interval is conditional on these assumptions, not a demonstrated accuracy guarantee. Better evidence would be a recent, independently conducted consumption survey with clear cup definitions.

Key assumptions: none (every formula input is an observed data point).

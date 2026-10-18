# Evidence ledger: smoke_tea

- Question: How many cups of tea do people in the United Kingdom drink per day?
- as_of: 2026-10-18
- Pinned target: Total number of cups of tea consumed by people in the United Kingdom (UK) on an average day, counting all tea types (black, green, herbal, fruit, decaffeinated) prepared as cups/mugs, including tea drunk at home and out of home, by residents and visitors present in the UK | unit cups per day | period 2026-01-01..2026-12-31 | publisher No single official publisher; UK Tea & Infusions Association (UKTIA) is the commonly cited industry source, with ONS/Nielsen/Defra data as supporting inputs

## Directions and pages

### d1 [own_history] Industry association / trade body

Hypothesis: UKTIA and predecessors have periodically published headline estimates of daily cups of tea drunk in the UK (e.g. ~100 million cups/day figures widely cited). These give a direct anchor for the target and its trend; the role is to provide a base level and recent direction.

Queries issued by the searcher: UK Tea and Infusions Association cups of tea per day; how many cups of tea drunk in UK each day 100 million UKTIA; tea.co.uk UKTIA 2026 cups of tea a day press release; UK Tea Council "165 million cups" tea drunk each day

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 15/12
  - p1 UK daily cups of tea consumed (UKTIA headline, all tea, cups) = **100,000,000** cups of tea per day (2023-08-22..2023-08-22) [keep: ] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p2 UK daily cups of coffee consumed (comparison, cups) = **98,000,000** cups of coffee per day (2023-08-22..2023-08-22) [DISCARD: Coffee cups/day comparison; irrelevant to tea target.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p3 Global daily cups of tea consumed (UKTIA estimate) = **5,000,000,000** cups of tea per day (2023-08-22..2023-08-22) [DISCARD: Global tea figure; wrong entity (world, not UK).] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p4 Global daily cups of coffee consumed (comparison) = **2,000,000,000** cups of coffee per day (2023-08-22..2023-08-22) [DISCARD: Global coffee figure; irrelevant.] quote: "way more than the 2 billion cups of coffee drunk daily."
  - p5 Global daily cups of tea consumed (intro statement) = **5,000,000,000** cups of tea per day (2023-08-22..2023-08-22) [DISCARD: Duplicate of p3 (global tea); wrong entity.] quote: "5 billion cups of tea are drunk globally each day versus 2 billion cups of coffee."
  - p6 Global daily cups of coffee consumed (intro statement) = **2,000,000,000** cups of coffee per day (2023-08-22..2023-08-22) [DISCARD: Duplicate of p4 (global coffee); irrelevant.] quote: "5 billion cups of tea are drunk globally each day versus 2 billion cups of coffee."
  - p7 Share of UK 18–24-year-olds having a daily cuppa = **83** % of 18–24-year-olds (2022-12-01..2022-12-31) [DISCARD: Share of 18–24s having a daily cuppa; a prevalence fragment for one narrow cohort, not usable to build the total without] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p8 Share of younger adults citing great taste as main reason = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Taste-reason share; irrelevant to volume.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p9 Share of over-25s citing great taste as main reason = **85** % of over 25s (2022-12-01..2022-12-31) [DISCARD: Taste-reason share; irrelevant to volume.] quote: "cited by 80% of younger adult and 85% of the over 25s."
  - p10 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; irrelevant to volume.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p11 Sample size of UK adults in Omnibus survey = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Survey sample size; not a quantity for estimation.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p12 Sample size of UK adults in Perspectus Global poll = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [DISCARD: Survey sample size; not a quantity for estimation.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published"
- `https://www.tea.co.uk/news/article/first-sips-how-tea-becomes-a-lifelong-habit-for-brits` -> **live_dated** (page date 2026-05-18); points raw/verified 0/0
- `https://www.climateactionforassociations.org/post/uk-tea-infusions-association-joins-cafa` -> **live_dated** (page date 2026-03-18); points raw/verified 1/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/0
- dropped by code checks: 19 (period_end missing or unparseable: 15; value_as_written not in quote as a whole number: 1; period_end 2026-12-31 after as_of: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 1; number: no number in value_as_written: 1)

### d2 [related_series] Retail and household consumption statistics

Hypothesis: Total tea consumed = tea retail sales volume (household) + out-of-home tea volume. Retail tea sales volumes (tonnes or kg) from ONS/Nielsen/Defra family food data, converted via grams per cup, give the at-home component; the target equals (retail volume / g-per-cup) plus an out-of-home allowance.

Queries issued by the searcher: UK tea retail sales volume tonnes per year UK Tea & Infusions Association; Defra Family Food tea purchases UK kg per person per week; Family Food 2023 tea purchases grams per person per week UK "tea" 2022; "average tea bag" weight grams UK 3.1g 2.5g teabag study

- `https://www.cbi.eu/sites/default/files/market-information/cbi_2016_-_tea_-_pfs_uk_-_final_draft_-_adjusted.pdf` -> **live_dated** (page date 2016-12-12); points raw/verified 15/9
  - p13 UK total tea consumption (apparent, all tea) in 2015 = **113,000** tonnes (2015-01-01..2015-12-31) [keep: ] quote: "total tea consumption amounting to about 113 thousand tonnes in 2015"
  - p14 UK per capita tea consumption per year (Quartz 2014) = **1,941** grams per year (2014-01-01..2014-12-31) [keep: ] quote: "as compared to 1941 grams in the UK (Quartz, 2014)"
  - p15 Ireland per capita tea consumption per year (Quartz 2014) = **2,191** grams per year (2014-01-01..2014-12-31) [DISCARD: Ireland per-capita; wrong entity.] quote: "higher per capita tea consumption of 2191 grams per year"
  - p16 Tea share of all away-from-home hot beverage servings in 2010 = **31.5** % of away-from-home hot beverage servings (2010-01-01..2010-12-31) [keep: ] quote: "tea accounts for 27% of all away-from-home hot beverage servings, compared to 31.5% in 2010"
  - p17 UK tea imports volume in 2015 = **133,000** tonnes (2015-01-01..2015-12-31) [keep: ] quote: "tea imports amounting to some 133 thousand tonnes with a value of about €354 million in 2015"
  - p18 UK tea exports volume in 2015 = **20,000** tonnes (2015-01-01..2015-12-31) [keep: ] quote: "tea exports from the United Kingdom amounted to a total volume of 20 thousand tonnes"
  - p19 Share of UK tea imports that was black tea in 2015 = **97** % of tea imports (2015-01-01..2015-12-31) [DISCARD: Black-tea import share; not needed for total-cup conversion.] quote: "Of all of the tea imported in the United Kingdom in 2015, about 97% was black tea (about 150 thousand tonnes)"
  - p20 Share of UK tea imports that was green tea in 2015 = **3** % of tea imports (2015-01-01..2015-12-31) [DISCARD: Green-tea import share; not needed.] quote: "and only about 3% was green tea (about four thousand tonnes)"
  - p21 Share of UK tea imports that was bulk tea in 2015 = **92** % of tea imports (2015-01-01..2015-12-31) [DISCARD: Bulk-tea import share; not needed.] quote: "the United Kingdom predominantly imports bulk tea (92% in 2015)"
- `https://www.gov.uk/government/statistical-data-sets/family-food-datasets` -> **live_dated** (page date 2026-09-17); points raw/verified 0/0
- `https://www.tea.co.uk/news/article/know-the-nation-to-a-tea-uk-tea-census-2022-launched-to-provide-the-answers-on-international-tea-day-21st-may-2022` -> **live_dated** (page date 2026-01-01); points raw/verified 15/1
  - p22 UK daily tea consumption (cups per day, all tea, UK) = **100,000,000** cups of tea per day (2022-05-21..2022-05-21) [keep: ] quote: "consume more than 100 million cups of tea every day in the UK"
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p23 Share of surveyed tea drinkers drinking three or more cups a day (2023 Product o = **35** % (2023-01-01..2023-12-31) [keep: ] quote: "the just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- dropped by code checks: 34 (period_end missing or unparseable: 31; number: no number in value_as_written: 2; value_as_written not in quote as a whole number: 1)

### d3 [base_rates] Consumer survey / persona

Hypothesis: Cups/day = UK population × share who drink tea × average cups per tea drinker per day. Survey data on tea-drinking prevalence and daily cup frequency (e.g. YouGov, Mintel, Statista, NHS) supply the base rates; the role is to cross-check the volume-based route.

Queries issued by the searcher: YouGov tea drinking habits UK cups per day survey; percentage of Brits who drink tea daily survey cups per day; UK per capita tea consumption kg per year Defra; UKTIA survey 1000 adults 98% drink tea daily 100 million cups a day 2024; site:tea.co.uk cups of tea day survey 98% adults; UK tea consumption 100 million cups a day UKTIA 2025

- `https://www.aldipresscentre.co.uk/product-news/tea-loving-brits-slurp-a-staggering-127-million-cuppas-a-day-but-nearly-a-quarter-are-making-it-all-wro` -> **live_dated** (page date 2025-07-03); points raw/verified 15/14
  - p24 UK total cups of tea consumed per day (Aldi headline estimate) = **127,000,000** cups per day (2025-01-01..2025-12-31) [keep: ] quote: "TEA-LOVING BRITS SLURP A STAGGERING 127 MILLION CUPPAS A DAY"
  - p25 Share of Brits drinking an average of four cups a day (Aldi survey) = **72** % (2025-06-01..2025-06-30) [keep: ] quote: "nearly three quarters (72%) drink an average of four cups a day"
  - p26 Share of Brits preferring tea to coffee (Aldi survey) = **55** % (2025-06-01..2025-06-30) [DISCARD: Tea-vs-coffee preference share; attitudinal, not a volume input.] quote: "over half of the nation (55%) saying coffee just isn't their cup of tea"
  - p27 UK adult population used in Aldi calculation = **31,758,667** people (UK adults) (2025-01-01..2025-12-31) [keep: ] quote: "55% of the UK adult population = 31,758,667"
  - p28 Calculated UK daily cups from Aldi methodology = **127,034,668** cups per day (2025-01-01..2025-12-31) [DISCARD: Pure arithmetic output of the Aldi methodology already captured by p24; adds no independent information.] quote: "Multiply by average number of cups a day (4) = 127,034,668"
  - p29 Average cups of tea per Brit per year (quoted by etiquette consultant) = **1,460** cups per person per year (2025-01-01..2025-12-31) [DISCARD: 1,460 cups/person/yr quoted by an etiquette consultant; unsourced and inconsistent with YouGov 884 (p63); misleading.] quote: "the average Brit consuming a staggering 1,460 cups a year"
  - p30 Aldi survey sample size (Brits polled) = **2,000** respondents (2025-06-01..2025-06-30) [DISCARD: Survey sample size; not a quantity.] quote: "This research of 2,000 Brits was commissioned by Aldi and conducted by Perspectus Global in June 2025."
  - p31 Share of Brits who put milk in first (making tea wrong) = **22** % (2025-06-01..2025-06-30) [DISCARD: Milk-first share; irrelevant.] quote: "almost a quarter (22%) are making their tea wrong by putting the milk in first"
  - p32 Share choosing English Breakfast as go-to brew = **67** % (2025-06-01..2025-06-30) [DISCARD: English Breakfast share; irrelevant to total volume.] quote: "English Breakfast (67%) is the go-to brew"
  - p33 Share who add water first before letting bag stew = **78** % (2025-06-01..2025-06-30) [DISCARD: Brewing-method share; irrelevant.] quote: "(78%) add the water first before letting the bag stew for TWO minutes"
  - p34 Share who give specific instructions when someone offers a tea run = **78** % (2025-06-01..2025-06-30) [DISCARD: Instruction-giving share; irrelevant.] quote: "78% so passionate about a good brew that they give exact instructions when someone offers to make them a cup"
  - p35 Share preferring no sugar in tea = **38** % (2025-06-01..2025-06-30) [DISCARD: Sugar-preference share; irrelevant.] quote: "two in five (38%) preferring no sugar at all"
  - p36 Share taking two sugars in tea = **22** % (2025-06-01..2025-06-30) [DISCARD: Sugar-preference share; irrelevant.] quote: "almost a quarter (22%) take two"
  - p37 Share who re-boil kettle because distracted = **48** % (2025-06-01..2025-06-30) [DISCARD: Kettle re-boil share; irrelevant.] quote: "48% say they often have to re-boil their kettle because they get distracted"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/10
  - p38 Cups of tea drunk every day in the UK (ITC estimate, cited by UKTIA) = **100,000,000** cups per day (..) [keep: ] quote: ""More than 100 million cups of tea are drunk every day here in the UK," she said, citing the International Tea Committee (ITC)"
  - p39 Annual UK tea consumption in cups (ITC estimate) = **36,000,000,000** cups per year (..) [DISCARD: Annualised duplicate of the 100m cups/day ITC headline (p38/p102); redundant.] quote: "which estimates consumption at 36 billion cups per year."
  - p40 Share of 30-44-year-olds preferring loose-leaf black tea (2024 Tea Census) = **27** % of 30-44-year-olds (2024-01-01..2024-12-31) [DISCARD: Loose-leaf preference share by age; irrelevant to total cups.] quote: "the age cohort most likely to prefer loose-leaf black tea was the 30-44-year-olds (27%)"
  - p41 Share of 18-29-year-olds preferring loose-leaf black tea (2024 Tea Census) = **16** % of 18-29-year-olds (2024-01-01..2024-12-31) [DISCARD: Loose-leaf preference share; irrelevant.] quote: "compared with 16% of 18-29-year-olds"
  - p42 Share of 45-59-year-olds preferring loose-leaf black tea (2024 Tea Census) = **12** % of 45-59-year-olds (2024-01-01..2024-12-31) [DISCARD: Loose-leaf preference share; irrelevant.] quote: "12% of 45-59-year-olds"
  - p43 Share of adults aged 60+ preferring loose-leaf black tea (2024 Tea Census) = **10** % of adults aged 60+ (2024-01-01..2024-12-31) [DISCARD: Loose-leaf preference share; irrelevant.] quote: "only one in 10 (10%) of those aged 60+"
  - p44 Share of 18-29-year-olds choosing loose leaf for herbal/green tea (2024 Tea Cens = **28** % of 18-29-year-olds (2024-01-01..2024-12-31) [DISCARD: Loose-leaf preference share; irrelevant.] quote: "more than a quarter (28%) of this age group said they predominantly chose loose leaf over tea bags"
  - p45 UK annual tea consumption in kilos (Statista Market Insights, excluding herbal,  = **72,000,000** kilos per year (..) [keep: ] quote: "Statista Market Insights estimates UK consumption at 72 million kilos annually, excluding herbal infusions, ready-to-drink, and instant tea."
  - p46 UK tea market value (Statista) = **1,700,000,000** GBP (£) (..) [DISCARD: Market value in GBP; not a volume input.] quote: "According to Statista market research, the UK market is valued at £1.7 billion ($2.2 billion)."
  - p47 Share of UK fluid intake that is tea (Tea Advisory Panel) = **40** % of fluid intake (..) [DISCARD: Share of fluid intake; not convertible to cups without total fluid intake data; low value.] quote: "even today, 40% of the nation's fluid intake will be tea, according to the Tea Advisory Panel (TAP)."
- `https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation` -> **live_dated** (page date 2025-06-30); points raw/verified 15/15
  - p48 Share of British adults who drink tea at home or at work at least twice a day = **41** % of British adults (..) [keep: ] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p49 Share of British adults who drink coffee at home or at work at least twice a day = **40** % of British adults (..) [DISCARD: Coffee daily-drinking share; irrelevant.] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p50 Share of tea drinkers buying tea out of home (takeaway/café) at least once a wee = **16** % of tea drinkers (..) [keep: ] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p51 Share of coffee drinkers buying coffee out of home (takeaway/café) at least once = **12** % of coffee drinkers (..) [DISCARD: Coffee out-of-home share; irrelevant.] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p52 Share of Gen Z who drink tea daily = **11** % of Gen Z (..) [keep: ] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p53 Share of Gen Z who drink coffee daily = **8** % of Gen Z (..) [DISCARD: Coffee daily-drinking share; irrelevant.] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p54 Share of Millennials who drink tea daily = **23** % of Millennials (..) [keep: ] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p55 Share of Millennials who drink coffee daily = **24** % of Millennials (..) [DISCARD: Coffee daily-drinking share; irrelevant.] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p56 Share of Gen X who drink tea daily = **31** % of Gen X (..) [keep: ] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p57 Share of Gen X who drink coffee daily = **33** % of Gen X (..) [DISCARD: Coffee daily-drinking share; irrelevant.] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p58 Share of Baby Boomers who drink tea daily = **32** % of Baby Boomers (..) [keep: ] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p59 Share of Baby Boomers who drink coffee daily = **32** % of Baby Boomers (..) [DISCARD: Coffee daily-drinking share; irrelevant.] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p60 Share of daily tea drinkers nationally who opt for green tea = **20** % of daily tea drinkers (..) [DISCARD: Green-tea share among daily drinkers; not needed for total cups.] quote: "32% of Gen Z daily tea drinkers opt for green tea (vs. 20% nationally)"
  - p61 Share of daily tea drinkers nationally who drink fruit tea = **13** % of daily tea drinkers (..) [DISCARD: Fruit-tea share; not needed.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)."
  - p62 Share of daily tea drinkers nationally who enjoy herbal tea = **16** % of daily tea drinkers (..) [DISCARD: Herbal-tea share; not needed.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)."
- `https://www.cosmopolitan.com/uk/reports/news/a35052/british-people-cups-tea-year/` -> **live_dated** (page date 2015-04-18); points raw/verified 8/7
  - p63 Average cups of tea per year per British person (YouGov survey, over 2,000 Briti = **884** cups of tea per person per year (..) [keep: ] quote: "a YouGov survey studying over 2,000 British people revealed that an average British person enjoys 884 cups of tea per year"
  - p64 Cups of tea per week among over 55s (YouGov survey) = **21** cups of tea per person per week (..) [keep: ] quote: "Over 55s are on a bit of a mad one, tea-wise, making their way through 21 cups a week."
  - p65 Cups of tea per week among 18 to 24s (YouGov survey) = **8** cups of tea per person per week (..) [keep: ] quote: "18 to 24s average out at only 8 cups per week in comparison."
  - p66 Share of 18 to 25 year olds who make tea when feeling down (YouGov survey) = **24** % (..) [DISCARD: Attitudinal share; irrelevant.] quote: "with 24% of 18 to 25 year olds saying they make a cup when they're feeling a bit down in the dumps"
  - p67 Share of people over age 55 who make tea when feeling down (YouGov survey) = **11** % (..) [DISCARD: Attitudinal share; irrelevant.] quote: "versus only 11% of people over age 55"
  - p68 Share of men who make tea when feeling unwell (YouGov survey) = **16** % (..) [DISCARD: Attitudinal share; irrelevant.] quote: "compared to 16% of men"
  - p69 YouGov survey sample size of British people = **2,000** British people surveyed (..) [DISCARD: Survey sample size; not a quantity.] quote: "a YouGov survey studying over 2,000 British people"
- dropped by code checks: 7 (number: no number in value_as_written: 3; period_end 2026-12-31 after as_of: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 3)

### d4 [physical_flow] Upstream trade / supply

Hypothesis: UK tea imports (or tea available for consumption = imports + production - exports - stock change) bound total consumption; converting net supply in tonnes to cups via grams-per-cup gives an upper-bound/independent estimate of daily cups.

Queries issued by the searcher: UK tea imports tonnes HMRC 2023 2024; FAO tea imports United Kingdom tonnes; UK tea market size tonnes consumption UKTIA; HMRC UK trade data tea imports exports 2024 tonnes commodity 0902; OEC United Kingdom tea imports exports 2023 tonnes; UKTIA tea facts 100 million cups 100,000 tonnes grams per cup; UK tea exports tonnes 2024 HMRC

- `https://asemconnectvietnam.gov.vn/default.aspx?ID1=2&ZID1=8&ID8=142023` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tea.co.uk/news/article/know-the-nation-to-a-tea-uk-tea-census-2022-launched-to-provide-the-answers-on-international-tea-day-21st-may-2022` -> **live_dated** (page date 2026-01-01); points raw/verified 15/1
  - p70 Highest tea party altitude (Mount Everest Camp 2) = **6,496** metres (2021-05-05..2021-05-05) [DISCARD: Highest tea-party altitude; irrelevant.] quote: "on Mount Everest Camp 2, Nepal, on May 5, 2021, at a height of 6,496 metres"
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p71 Share of tea drinkers drinking three or more cups a day (2023 Product of the Yea = **35** % of surveyed tea drinkers (2023-01-01..2023-12-31) [DISCARD: Duplicate of p23.] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- `https://www.indexbox.io/store/united-kingdom-kw-fair-trade-green-tea-840-market-analysis-forecast-size-trends-and-insights/` -> **live_dated** (page date 2026-05-24); points raw/verified 15/0
- dropped by code checks: 43 (period_end missing or unparseable: 39; number: no number in value_as_written: 2; period_end 2026-12-31 after as_of: 2)

### d5 [capacity_consumption] Out-of-home operator

Hypothesis: Out-of-home tea cups/day = number of hot drinks served in UK foodservice × tea share of hot drinks. Foodservice hot beverage servings (cafes, pubs, workplaces, hotels) and tea's share of those servings give the away-from-home component missing from retail data.

Queries issued by the searcher: UK foodservice hot drinks servings per year tea share Allegra; UK coffee shop tea sales share hot beverages out of home; Tetley Tea Report four billion cups tea out-of-home 2016 £3.4bn; UK out of home tea cups per year billion foodservice 2023 2024 Kantar hot drinks

- `https://www.beveragestandardsassociation.co.uk/wp-content/uploads/2020/01/Tetley_Tea_Report2018.pdf` -> **live_dated** (page date 2020-01-01); points raw/verified 15/4
  - p72 Average tea cost per cup out of home, UK, 2017 = **1.77** pounds sterling per cup (2017-01-01..2017-12-31) [DISCARD: Out-of-home tea price per cup; not a volume input.] quote: "£1.77 2017 AVERAGE Tea cost per cup"
  - p73 Average tea cost per cup out of home, UK, 2016 = **1.73** pounds sterling per cup (2016-01-01..2016-12-31) [DISCARD: Out-of-home tea price; not a volume input.] quote: "£1.73 2016"
  - p74 Average tea cost per cup out of home, UK, 2015 = **1.69** pounds sterling per cup (2015-01-01..2015-12-31) [DISCARD: Out-of-home tea price; not a volume input.] quote: "£1.69 2015"
  - p75 Average coffee cost per cup out of home, UK, 2017 = **2.1** pounds sterling per cup (2017-01-01..2017-12-31) [DISCARD: Coffee price; irrelevant.] quote: "£2.10 2017 AVERAGE COFFEE cost per cup"
- `https://www.publicsectorcatering.co.uk/news/ooh-tea-occasions-grow-while-coffee-slows-down-report-finds` -> **live_dated** (page date 2016-12-08); points raw/verified 15/0
- `https://www.thecaterer.com/products--equipment/trends-in-tea-targeting-a-smaller-market` -> **live_dated** (page date 2024-10-28); points raw/verified 9/2
  - p76 Chai latte growth in 2023 (Mintel) = **94** % growth (2023-01-01..2023-12-31) [DISCARD: Chai-latte growth; irrelevant to total cups.] quote: "Mintel figures show chai latte saw 94% growth in 2023"
  - p77 Consecutive Great Taste awards for Birchall Great Rift blend (2024) = **14** awards (consecutive) (2024-01-01..2024-12-31) [DISCARD: Awards count; irrelevant.] quote: "Our flagship Great Rift blend was awarded its 14th consecutive Great Taste award in 2024."
- `https://www.restaurantonline.co.uk/Article/2017/04/05/Tea-sales-drop-compared-to-coffee-says-report/` -> **live_dated** (page date 2017-04-05); points raw/verified 10/6
  - p78 Out-of-home tea share of UK out-of-home hot drinks sales, 2015 = **4.1** % share (2015-01-01..2015-12-31) [keep: ] quote: "'Out of home' tea sales have declined in the past year from 4.1% in 2015 to 3.8% in the latest report"
  - p79 Out-of-home tea share of UK out-of-home hot drinks sales, latest report (2016) = **3.8** % share (2016-01-01..2016-12-31) [keep: ] quote: "'Out of home' tea sales have declined in the past year from 4.1% in 2015 to 3.8% in the latest report"
  - p80 Average cups of tea drunk in coffee shops per week per consumer, UK = **0.65** cups per week (2016-01-01..2016-12-31) [DISCARD: Coffee-shop cups/week per consumer; too narrow and old to build out-of-home component reliably.] quote: "and three per day at work, but just 0.65 cups per week in coffee shops."
  - p81 UK coffee shop sector turnover growth last year (2016) = **12** % growth (2016-01-01..2016-12-31) [DISCARD: Coffee-shop turnover growth; irrelevant.] quote: "And while the UK coffee shop sector increased by 12% in turnover last year"
  - p82 Forecast UK out-of-home tea turnover by year-end 2017 = **341** GBP million (turnover) (2017-01-01..2017-12-31) [DISCARD: Out-of-home tea turnover; value not volume.] quote: "Allegra World Coffee Portal anticipates the category to continue similar growth in 2017 and reach £341 turnover by year-end."
  - p83 Share of consumers saying coffee shops do not make a cup of tea to their taste = **22** % of consumers (2016-01-01..2016-12-31) [DISCARD: Value-for-money share; irrelevant.] quote: "and 22% saying that tea available out-of-home was 'not good value for money'."
- dropped by code checks: 37 (scale word 'billion' not supported by quote or table header: 4; period_end missing or unparseable: 21; scale word 'million' not supported by quote or table header: 8; number: more than one number in value_as_written: 1; period_end 2028-12-31 after as_of: 1; number: no number in value_as_written: 2)

### d6 [shocks] Market analyst

Hypothesis: Tea consumption is slowly declining in the UK as coffee and other drinks substitute; recent price inflation and cost-of-living pressures may accelerate decline. Adjusting older headline estimates (e.g. 100 million cups/day) by observed trend in retail volumes or per-capita consumption gives a current figure.

Queries issued by the searcher: UK tea market decline volume Kantar; UKTIA tea consumption 100 million cups a day decline; tea sales volume UK 2024 2025 fall Kantar The Grocer tea category report; UK tea volumes decline percent 2023 2024 NielsenIQ tea market value volume

- `https://www.thegrocer.co.uk/consumer-trends/cuppa-in-decline-as-brits-drink-870-million-fewer-cups-of-tea/571087.article` -> **live_dated** (page date 2018-08-31); points raw/verified 10/5
  - p84 UK tea volume decline in kilograms, Kantar Worldpanel 52 weeks ending 20 May 201 = **2,600,000** kilograms of tea (2017-05-21..2018-05-20) [keep: ] quote: "The nation bought 2.6 million fewer kilograms of tea, shows Kantar Worldpanel data [52 w/e 20 May 2018], the steepest volume decline in four years."
  - p85 Equivalent fewer cups of tea implied by 2.6 million kg decline at 3g per teabag, = **866,700,000** cups of tea (2017-05-21..2018-05-20) [keep: ] quote: "As the average teabag contains 3g of leaves, this equates to roughly 866.7 million fewer cups of tea over that period."
  - p86 UK tea market value growth rate, Kantar Worldpanel 52 weeks ending 20 May 2018 = **0.6** % (2017-05-21..2018-05-20) [DISCARD: Tea market value growth; not a volume trend.] quote: "Kantar Worldpanel data shows the value of tea has risen by 0.6% to £669.2m over the past year."
  - p87 Yorkshire Tea brand value growth, Nielsen 52 weeks ending 30 December 2017 = **7.9** % (2016-12-31..2017-12-30) [DISCARD: Brand value growth; irrelevant.] quote: "Yorkshire Tea, which secured the highest value growth of any tea brand in The Grocer's Britain's Biggest Brands (up 7.9% to £88m, Nielsen 52 w/e 30 December 2017)"
  - p88 Free-from market value growth, Kantar Worldpanel 52 weeks ending 26 March 2018 = **37.5** % (2017-03-27..2018-03-26) [DISCARD: Free-from market growth; irrelevant.] quote: "in a bid to grab a slice of the growing free-from market, whose value is up 37.5% [Kantar Worldpanel 52 w/e 26 March 2018]."
- `https://www.kantar.com/uki/inspiration/consumer/our-feelings-about-tea-in-the-uk` -> **live_dated** (page date 2019-04-17); points raw/verified 15/11
  - p89 Total UK tea-drinking occasions as a nation, year to February 2019 = **18,300,000,000** tea-drinking occasions (2018-03-01..2019-02-28) [keep: ] quote: "we still enjoyed a cuppa on 18.3 billion occasions as a nation"
  - p90 Total UK spend on tea, year to 52 w/e 24 March 2019 = **663,327,000** GBP (2018-03-25..2019-03-24) [DISCARD: Tea spend in GBP; not a volume input.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p91 Year-on-year change in total UK tea spend = **1** percent (2018-03-25..2019-03-24) [DISCARD: Spend change; not a volume trend.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p92 Year-on-year increase in average tea price per kilogram = **7** pence per kilogram (2018-03-25..2019-03-24) [DISCARD: Price change; not a volume input.] quote: "that decline is despite prices rising by 7p a kilogram (+3.1% year on year) this year"
  - p93 Year-on-year percentage increase in average tea price per kilogram = **3.1** percent (2018-03-25..2019-03-24) [DISCARD: Price change; not a volume input.] quote: "prices rising by 7p a kilogram (+3.1% year on year) this year"
  - p94 Year-on-year growth in spend on Speciality Tea, 52 w/e March 2019 vs 2018 = **4.2** percent (2018-03-25..2019-03-24) [DISCARD: Speciality-tea spend growth; irrelevant.] quote: "Spending on Speciality Tea is up 4.2% (52 w/e March 2019 vs. 2018)"
  - p95 Year-on-year increase in average price of Speciality Tea = **2.7** percent (2018-03-25..2019-03-24) [DISCARD: Speciality-tea price change; irrelevant.] quote: "partly due to pricing (the average price has gone up 2.7%)"
  - p96 Increase in speciality tea occasions, 52 w/e March 2019 vs 2018 = **10** percent (2018-03-25..2019-03-24) [DISCARD: Speciality-tea occasion growth; irrelevant.] quote: "Occasions involving speciality tea were up 10% in the time period, or 100m."
  - p97 Year-on-year growth in spend on Everyday Decaf tea = **5.5** percent (2018-03-25..2019-03-24) [DISCARD: Decaf spend growth; irrelevant.] quote: ""Everyday Decaf" spend is also up, 5.5%, thanks to more shoppers making that choice in the supermarket."
  - p98 Yorkshire Tea spend growth over the past year = **28** percent (2018-03-25..2019-03-24) [DISCARD: Brand spend growth; irrelevant.] quote: "Yorkshire Tea has been the biggest winner (+28% spend growth) over the past year."
  - p99 Share of Everyday Decaf consumption occasions occurring at breakfast = **4** in 10 consumption occasions (2018-03-25..2019-03-24) [DISCARD: Decaf breakfast share; irrelevant.] quote: "4 in 10 consumption occasions (of Everyday Decaf tea) come at breakfast"
- `https://www.thecaterer.com/products--equipment/trends-in-tea-targeting-a-smaller-market` -> **live_dated** (page date 2024-10-28); points raw/verified 8/2
  - p100 Mintel: chai latte growth in 2023 = **94** % growth (2023-01-01..2023-12-31) [DISCARD: Duplicate of p76.] quote: "Mintel figures show chai latte saw 94% growth in 2023"
  - p101 Birchall Great Rift consecutive Great Taste awards as of 2024 = **14** consecutive awards (2024-01-01..2024-12-31) [DISCARD: Duplicate of p77.] quote: "Our flagship Great Rift blend was awarded its 14th consecutive Great Taste award in 2024."
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 14/7
  - p102 UK daily tea consumption, cups per day (ITC estimate cited by UKTIA) = **100,000,000** cups per day (2024-05-01..2024-05-31) [keep: ] quote: ""More than 100 million cups of tea are drunk every day here in the UK," she said, citing the International Tea Committee (ITC)"
  - p103 UK annual tea consumption, cups per year (ITC estimate cited by UKTIA) = **36,000,000,000** cups per year (2024-01-01..2024-12-31) [DISCARD: Duplicate of p39/p133 (36bn cups/year); redundant with the daily headline.] quote: "which estimates consumption at 36 billion cups per year."
  - p104 Share of UK residents who drink tea daily (UKTIA survey) = **98** % of UK residents (2024-05-01..2024-05-31) [keep: ] quote: "the UK Tea & Infusions Association (UKTIA) revealed that 98% of UK residents drink tea daily."
  - p105 Global tea market value forecast for 2025 = **134,400,000,000** USD ($) (2025-01-01..2025-12-31) [DISCARD: Global market value forecast; irrelevant.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p106 UK tea export value, 2023 (ranked 7th by value) = **121,400,000** USD ($) (2023-01-01..2023-12-31) [DISCARD: UK tea export value; not a consumption input.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
  - p107 Japan green tea export value, 2023 (ranked 6th) = **210,100,000** USD ($) (2023-01-01..2023-12-31) [DISCARD: Japan green-tea export value; irrelevant.] quote: "Green tea exporter Japan ranked 6th that year with $210.1 million in exports."
  - p108 Adults surveyed in UKTIA March survey = **1,010** adults (2024-03-01..2024-03-31) [DISCARD: Survey sample size; not a quantity.] quote: "nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
- dropped by code checks: 22 (period_end missing or unparseable: 15; scale word 'million' not supported by quote or table header: 6; period_end 2028-12-31 after as_of: 1)

### d7 [related_series] Cross-country comparable

Hypothesis: UK per-capita tea consumption (kg/person/year) from FAO/ITC can be compared with known cup-frequency surveys to calibrate grams-per-cup and prevalence, then applied to UK population. The role is to validate the conversion factor and per-capita level.

Queries issued by the searcher: FAO per capita tea consumption United Kingdom kg per year; ITC tea consumption per capita UK kg Ireland Turkey; "per capita" tea consumption "United Kingdom" kg 2023 ITC Annual Bulletin apparent consumption table; FAO tea market review per capita consumption Europe United Kingdom kilograms 2022

- `https://logos-pres.md/en/news/tea-versus-coffee-why-tea-has-become-the-worlds-most-popular-drink/` -> **live_dated** (page date 2026-09-13); points raw/verified 15/3
  - p109 International tea trade volume in 2025 = **2,000,000** tonnes (2025-01-01..2025-12-31) [DISCARD: Global trade volume; irrelevant.] quote: "International trade in 2025 amounted to around 2 million tonnes."
  - p110 China green tea production in 2025 = **2,000,000** tonnes (2025-01-01..2025-12-31) [DISCARD: China green-tea production; irrelevant.] quote: "In 2025, the country produced over 2 million tonnes of green tea, compared with 0.51 million tonnes of black tea."
  - p111 China black tea production in 2025 = **510,000** tonnes (2025-01-01..2025-12-31) [DISCARD: China black-tea production; irrelevant.] quote: "In 2025, the country produced over 2 million tonnes of green tea, compared with 0.51 million tonnes of black tea."
- `https://inttea.com/wp-content/uploads/IndexABS24.pdf` -> **live_dated** (page date 2024-11-15); points raw/verified 0/0
- `https://inttea.com/wp-content/uploads/Index2022.pdf` -> **live_dated** (page date 2022-07-26); points raw/verified 0/0
- `https://openknowledge.fao.org/server/api/core/bitstreams/2cbea209-a1f4-4f37-af40-e54d8b6cadbc/content` -> **live_dated** (page date 2022-02-18); points raw/verified 15/0
- dropped by code checks: 27 (period_end missing or unparseable: 10; number: no number in value_as_written: 2; number: more than one number in value_as_written: 12; value_as_written not in quote as a whole number: 3)

### b1 [related_series] physical_flow

Hypothesis: A recent (2023–2025) UK apparent tea consumption figure (imports + production − exports − stock change, in tonnes) would let the physical-flow route (p13/p17/p18) be updated to the target year and converted to cups via a grams-per-cup factor, giving an independent check on the 100m vs 127m disagreement.

Queries issued by the searcher: UK tea imports exports tonnes 2023 HMRC trade statistics; Defra family food tea supply UK consumption tonnes; FAOSTAT United Kingdom tea imports quantity tonnes 2023 food balance sheet; UKTIA "100 million cups" tea UK daily 2024

- `https://gtaic.ai/files/reports/United_Kingdom_090240_d8bb37d4-0597-484f-aeb9-4ed5f91849a7.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://wits.worldbank.org/trade/comtrade/en/country/GBR/year/2023/tradeflow/Imports/partner/ALL/product/090230` -> **live_dated** (page date 2023-01-01); points raw/verified 15/14
  - p112 UK imports of black tea (HS 090230) from World, quantity, 2023 = **7,769,920** Kg (2023-01-01..2023-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| World \| 53,559.06 \| 7,769,920 \| Kg \|"
  - p113 UK imports of black tea (HS 090230) from Kenya, quantity, 2023 = **3,412,680** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row of the 2023 black-tea import table; subsumed by the World total p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Kenya \| 13,062.05 \| 3,412,680 \| Kg \|"
  - p114 UK imports of black tea (HS 090230) from Poland, quantity, 2023 = **1,239,360** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Poland \| 9,413.62 \| 1,239,360 \| Kg \|"
  - p115 UK imports of black tea (HS 090230) from Sri Lanka, quantity, 2023 = **672,620** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Sri Lanka \| 8,140.54 \| 672,620 \| Kg \|"
  - p116 UK imports of black tea (HS 090230) from India, quantity, 2023 = **581,842** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| India \| 4,789.29 \| 581,842 \| Kg \|"
  - p117 UK imports of black tea (HS 090230) from Germany, quantity, 2023 = **524,346** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Germany \| 4,297.24 \| 524,346 \| Kg \|"
  - p118 UK imports of black tea (HS 090230) from Turkey, quantity, 2023 = **414,603** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Turkey \| 3,798.28 \| 414,603 \| Kg \|"
  - p119 UK imports of black tea (HS 090230) from Ireland, quantity, 2023 = **310,436** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Ireland \| 2,780.94 \| 310,436 \| Kg \|"
  - p120 UK imports of black tea (HS 090230) from United Arab Emirates, quantity, 2023 = **163,030** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| United Arab Emirates \| 1,837.30 \| 163,030 \| Kg \|"
  - p121 UK imports of black tea (HS 090230) from China, quantity, 2023 = **48,554** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| China \| 685.48 \| 48,554 \| Kg \|"
  - p122 UK imports of black tea (HS 090230) from United Kingdom (re-imports), quantity,  = **17,252** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| United Kingdom \| 81.44 \| 17,252 \| Kg \|"
  - p123 UK imports of black tea (HS 090230) from Indonesia, quantity, 2023 = **12,716** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Indonesia \| 390.77 \| 12,716 \| Kg \|"
  - p124 UK imports of black tea (HS 090230) from Netherlands, quantity, 2023 = **15,430** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Netherlands \| 167.61 \| 15,430 \| Kg \|"
  - p125 UK imports of black tea (HS 090230) from Uganda, quantity, 2023 = **47,240** Kg (2023-01-01..2023-12-31) [DISCARD: Partner-level row subsumed by p112.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2023 \| Uganda \| 80.13 \| 47,240 \| Kg \|"
- `https://inttea.com/wp-content/uploads/IndexABS24.pdf` -> **live_dated** (page date 2024-11-15); points raw/verified 0/0
- `https://assets.publishing.service.gov.uk/media/6a69b3eb4dda8076771a42a7/agriculture-in-the-uk-2025.pdf` -> **dropped** (live http 301); points raw/verified -/-
- dropped by code checks: 1 (scale word 'thousand' not supported by quote or table header: 1)

### b2 [base_rates] survey

Hypothesis: A recent nationally representative survey giving both tea-drinking prevalence and average cups per drinker per day (not just '3+ cups' or '4 cups' among a self-selected subgroup) would let the base-rate route (p48/p52–p58) be built without the Aldi 4-cups-for-55% assumption, resolving the largest uncertainty in the survey route.

Queries issued by the searcher: UK Tea & Infusions Association cups of tea per day UK statistics; YouGov tea drinking survey UK cups per day 2024; Statista average cups of tea consumed per day per person UK; Mintel tea UK report cups per day consumption

- `https://myteaplanner.com/tea-statistics` -> **live_dated** (page date 2026-09-30); points raw/verified 12/5
  - p126 U.S. Census Bureau January 2024 tea feature estimate of Americans drinking tea ( = **159,000,000** people (U.S.) (2024-01-01..2024-01-31) [DISCARD: US population drinking tea; different country, not transferable to UK target.] quote: "159 million+ The U.S. Census Bureau's January 2024 tea feature cites this estimate from the Tea Association of the U.S.A."
  - p127 U.S. total tea (gallons) reported by U.S. Census Bureau citing Tea Association o = **85,000,000,000** gallons (U.S., year) (2021-01-01..2021-12-31) [DISCARD: US total tea gallons; different country and scope (includes RTD/iced), not transferable.] quote: "85 billion The U.S. Census Bureau reported that total as more than 3.9 billion gallons for the year, citing the Tea Association of the U.S.A."
  - p128 U.S. total tea volume in gallons for the year (U.S. Census Bureau citing Tea Ass = **3,900,000,000** gallons (U.S., year) (2021-01-01..2021-12-31) [DISCARD: US total tea gallons; different country and scope, not transferable.] quote: "The U.S. Census Bureau reported that total as more than 3.9 billion gallons for the year, citing the Tea Association of the U.S.A."
  - p129 Share of U.S. tea consumption attributed to a tea type (84%) in U.S. Census Bure = **84** % of U.S. tea consumption (2021-01-01..2021-12-31) [DISCARD: US tea-type share; irrelevant to UK level.] quote: "84% The Census Bureau reports green tea at 15%, with oolong, white, and dark teas making up the remaining share cited from the association."
  - p130 Share of U.S. tea consumption attributed to green tea (U.S. Census Bureau Januar = **15** % of U.S. tea consumption (2021-01-01..2021-12-31) [DISCARD: US green-tea share; irrelevant to UK level.] quote: "The Census Bureau reports green tea at 15%, with oolong, white, and dark teas making up the remaining share cited from the association."
- `https://cravemag.co.uk/6-in-10-brits-still-rely-on-tea-to-stay-calm-new-study-finds/` -> **live_dated** (page date 2025-12-11); points raw/verified 11/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/14
  - p131 UK residents who drink tea daily, share of UK residents (UKTIA) = **98** % of UK residents (2024-05-01..2024-05-31) [DISCARD: Duplicate of p104 (98% drink tea daily); also implausible as a prevalence.] quote: "In May, the UK Tea & Infusions Association (UKTIA) revealed that 98% of UK residents drink tea daily."
  - p132 Cups of tea drunk every day in the UK (ITC estimate, cited by UKTIA) = **100,000,000** cups per day (2024-05-01..2024-05-31) [DISCARD: Duplicate of the 100m cups/day ITC headline already represented by p1/p22/p38/p102.] quote: ""More than 100 million cups of tea are drunk every day here in the UK," she said, citing the International Tea Committee (ITC)"
  - p133 Annual UK tea consumption in cups (ITC estimate) = **36,000,000,000** cups per year (2024-05-01..2024-05-31) [DISCARD: Duplicate of p39/p103; redundant.] quote: "which estimates consumption at 36 billion cups per year."
  - p134 Adults surveyed in March UKTIA survey = **1,010** adults surveyed (2024-03-01..2024-03-31) [keep: ] quote: "nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
  - p135 Share of surveyed black-tea drinkers using tea bags = **84** % of surveyed adults (2024-03-01..2024-03-31) [keep: ] quote: ""It's no surprise that 84% pick the option of a tea bag to make their black tea, with 16% opting for loose leaf,""
  - p136 Share of surveyed black-tea drinkers using loose leaf = **16** % of surveyed adults (2024-03-01..2024-03-31) [keep: ] quote: "with 16% opting for loose leaf," said Hall."
  - p137 Share of surveyed adults drinking black tea without milk = **24** % of surveyed adults (2024-03-01..2024-03-31) [keep: ] quote: "nearly a quarter (24%) said they drink their black tea as it comes, without any milk"
  - p138 UK tea market value (Statista) = **1,700,000,000** GBP (£) (..) [keep: ] quote: "According to Statista market research, the UK market is valued at £1.7 billion ($2.2 billion)."
  - p139 UK tea consumption in kilos annually, excluding herbal infusions, RTD and instan = **72,000,000** kilos per year (..) [DISCARD: Duplicate of p45 (72 million kg/year Statista); same source and value.] quote: "Statista Market Insights estimates UK consumption at 72 million kilos annually, excluding herbal infusions, ready-to-drink, and instant tea."
  - p140 UK tea export value, 2023 (ranked 7th by value) = **121,400,000** USD ($) export value (2023-01-01..2023-12-31) [keep: ] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
  - p141 Average weekly tea spend per person in the UK (Statista) = **15** pence per person per week (..) [keep: ] quote: "According to Statista, UK residents spend an average of 15 pence per person per week on tea."
  - p142 Share of UK fluid intake that is tea (Tea Advisory Panel) = **40** % of fluid intake (..) [keep: ] quote: "even today, 40% of the nation's fluid intake will be tea, according to the Tea Advisory Panel (TAP)."
  - p143 Global tea market estimated value by 2025 (forecast) = **134,400,000,000** USD ($) (2025-01-01..2025-12-31) [keep: ] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p144 Global tea production nearing (FAO) = **6,700,000** tons (..) [keep: ] quote: "According to the UN Food and Agriculture Organization (FAO), tea production is nearing 6.7 million tons."
- `https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation` -> **live_dated** (page date 2025-06-30); points raw/verified 15/15
  - p145 Share of British adults who drink tea at home or at work at least twice a day = **41** % of British adults (..) [DISCARD: Duplicate of p48 (41% YouGov); same statistic.] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p146 Share of British adults who drink coffee at home or at work at least twice a day = **40** % of British adults (..) [keep: ] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p147 Share of tea drinkers buying tea out of home (takeaway/café) at least once a wee = **16** % of tea drinkers (..) [keep: ] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p148 Share of Gen Z drinking tea daily = **11** % of Gen Z adults (..) [DISCARD: Duplicate of p52 (11% Gen Z daily tea).] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p149 Share of Millennials drinking tea daily = **23** % of Millennials (..) [DISCARD: Duplicate of p54 (23% Millennials daily tea).] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p150 Share of Gen X drinking tea daily = **31** % of Gen X adults (..) [DISCARD: Duplicate of p56 (31% Gen X daily tea).] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p151 Share of Baby Boomers drinking tea daily = **32** % of Baby Boomers (..) [DISCARD: Duplicate of p58 (32% Baby Boomers daily tea).] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p152 Share of daily tea drinkers nationally choosing green tea = **20** % of daily tea drinkers (..) [keep: ] quote: "32% of Gen Z daily tea drinkers opt for green tea (vs. 20% nationally)"
  - p153 Share of daily tea drinkers nationally choosing fruit tea = **13** % of daily tea drinkers (..) [keep: ] quote: "27% drink fruit tea (vs. 13%)"
  - p154 Share of daily tea drinkers nationally choosing herbal tea = **16** % of daily tea drinkers (..) [keep: ] quote: "28% enjoy herbal tea (vs. 16%)"
  - p155 Share of daily tea drinkers nationally choosing matcha = **4** % of daily tea drinkers (..) [keep: ] quote: "Matcha, though still a niche option overall (4%), finds greater traction among Gen Z (7%) and Millennials (9%)."
  - p156 Share of Millennials daily tea drinkers choosing traditional English breakfast t = **77** % of Millennial daily tea drinkers (..) [keep: ] quote: "traditional English breakfast (e.g., black tea blend) remains dominant across all age groups, especially Millennials (77%) and Gen Z (74%)"
  - p157 Share of Gen Z daily tea drinkers choosing traditional English breakfast tea = **74** % of Gen Z daily tea drinkers (..) [keep: ] quote: "traditional English breakfast (e.g., black tea blend) remains dominant across all age groups, especially Millennials (77%) and Gen Z (74%)"
  - p158 Share of Gen Z daily tea drinkers choosing iced tea = **22** % of Gen Z daily tea drinkers (..) [keep: ] quote: "Iced tea is another youthful favourite, consumed by 22% of Gen Z compared to just 2% of Baby Boomers."
  - p159 Share of Baby Boomers daily tea drinkers choosing iced tea = **2** % of Baby Boomer daily tea drinkers (..) [keep: ] quote: "Iced tea is another youthful favourite, consumed by 22% of Gen Z compared to just 2% of Baby Boomers."
- dropped by code checks: 19 (period_end 2026-12-31 after as_of: 7; period year 2025 does not appear in the page text or URL (likely mis-dated): 11; number: no number in value_as_written: 1)

### b3 [related_series] conversion

Hypothesis: A current grams-per-cup (or grams-per-teabag) figure and the split between at-home and out-of-home tea volume would let retail volume (p45, p13) be converted to cups and the out-of-home component (p16/p78) be added, completing the volume-based route (d2) that currently lacks a current conversion factor.

Queries issued by the searcher: UK average teabag weight grams 2024; UKTIA tea consumption per cup grams tea bag; tea out of home share UK volume Kantar; "tea bag" weight "2.5g" UK average grams per cup UKTIA; UK tea consumption out of home "per cent" of tea volume foodservice UKTIA market report; tea and infusions association UK market report tea bags per kg 2024 out of home

- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/2
  - p160 Share of surveyed tea drinkers drinking three or more cups a day (Product of the = **35** % (2023-01-01..2023-12-31) [DISCARD: Duplicate of p23 (35% drink 3+ cups/day).] quote: "the just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day."
  - p161 Share of Britons drinking five-10 cups a day (2023 survey context) = **20** % (2023-01-01..2023-12-31) [keep: ] quote: "while 20% of Britons do their part by drinking five-10 cups a day."
- `https://menafn.com/1104246395/KNOW-THE-NATION-TO-A-TEA-TEA-CENSUS-REPORT-2022-LAUNCHED-TO-PROVIDE-THE-ANSWERS-ON-INTERNATIONAL-TEA-DAY-21St-MAY-2022?s` -> **live_dated** (page date 2022-05-20); points raw/verified 15/11
  - p162 UK daily tea consumption (cups per day, all tea, UK) = **100,000,000** cups of tea per day (2022-01-01..2022-12-31) [keep: ] quote: "We import around 100,000 metric tons of tea every year and consume more than 100 million cups of tea every day in the UK."
  - p163 UK annual tea imports (metric tons per year) = **100,000** metric tons of tea per year (2022-01-01..2022-12-31) [keep: ] quote: "We import around 100,000 metric tons of tea every year and consume more than 100 million cups of tea every day in the UK."
  - p164 Share of respondents adding milk or sugar before teabag and water = **22** % (2022-01-01..2022-12-31) [keep: ] quote: "almost one in four people (22%) adds milk or sugar BEFORE adding the teabag and hot water."
  - p165 Share of respondents adding plant-based milk = **10** % (2022-01-01..2022-12-31) [keep: ] quote: "only marginally fewer than the percentage who add a plant-based milk (10%)."
  - p166 Share of respondents adding cream to tea = **7** % (2022-01-01..2022-12-31) [keep: ] quote: "seven times that number (7%) add CREAM to their tea"
  - p167 Share of respondents drinking peppermint infusion at least twice a week = **24** % (2022-01-01..2022-12-31) [keep: ] quote: "Peppermint and chamomile are the most popular infusions with 24% and 21% of respondents drinking them at least twice a week."
  - p168 Share of respondents drinking chamomile infusion at least twice a week = **21** % (2022-01-01..2022-12-31) [keep: ] quote: "Peppermint and chamomile are the most popular infusions with 24% and 21% of respondents drinking them at least twice a week."
  - p169 Number of countries growing true tea (Camellia sinensis) = **60** countries (2022-01-01..2022-12-31) [keep: ] quote: "True tea from the Camellia sinensis plant is grown in more than 60 countries"
  - p170 Number of different plants used in herbal and fruit infusions = **300** plants (2022-01-01..2022-12-31) [keep: ] quote: "Around 300 different plants and over 400 plant parts including leaves roots, bark, seeds, flowers, or fruits are used in herbal and fruit infusions."
  - p171 Number of plant parts used in herbal and fruit infusions = **400** plant parts (2022-01-01..2022-12-31) [keep: ] quote: "Around 300 different plants and over 400 plant parts including leaves roots, bark, seeds, flowers, or fruits are used in herbal and fruit infusions."
  - p172 Highest tea party altitude (Mount Everest Camp 2, Nepal) = **6,496** metres (2021-05-05..2021-05-05) [keep: ] quote: "on Mount Everest Camp 2, Nepal, on May 5, 2021, at a height of 6,496 metres."
- `https://www.thecaterer.com/products--equipment/trends-in-tea-targeting-a-smaller-market` -> **live_dated** (page date 2024-10-28); points raw/verified 8/2
  - p173 Mintel growth of chai latte in 2023 = **94** % growth (2023-01-01..2023-12-31) [keep: ] quote: "Mintel figures show chai latte saw 94% growth in 2023"
  - p174 Birchall Great Rift consecutive Great Taste awards as of 2024 = **14** consecutive awards (2024-01-01..2024-12-31) [keep: ] quote: "Our flagship Great Rift blend was awarded its 14th consecutive Great Taste award in 2024."
- `https://businesswales.gov.wales/foodanddrink/sites/foodanddrink/files/documents/Food%20-%20Research%20-%20Kantar%20-%20Taste%20Wales%20-%20Chris%20Hay` -> **live_dated** (page date 2017-04-19); points raw/verified 15/9
  - p175 GB out-of-home hot beverage spend share on tea (numerator: tea spend; denominato = **17** % of out-of-home hot beverage spend (2016-01-03..2017-01-01) [keep: ] quote: "In GB 72% out of home hot beverage spend is on coffee (only 17% on tea), Wales shows a similar dynamic"
  - p176 GB out-of-home hot beverage spend share on coffee (numerator: coffee spend; deno = **72** % of out-of-home hot beverage spend (2016-01-03..2017-01-01) [keep: ] quote: "In GB 72% out of home hot beverage spend is on coffee (only 17% on tea), Wales shows a similar dynamic"
  - p177 Average price of an out-of-home coffee in GB = **1.68** GBP per coffee (2016-01-03..2017-01-01) [keep: ] quote: "The average out of home coffee costs £1.68"
  - p178 GB out-of-home spend per person per year (Kantar OOH, 52 w/e 01 Jan 2017) = **968** GBP per person per year (2016-01-03..2017-01-01) [keep: ] quote: "£968 per person in OOH GB £846 in Wales"
  - p179 GB out-of-home trips per person per year (Kantar OOH, 52 w/e 01 Jan 2017) = **250** trips per person per year (2016-01-03..2017-01-01) [keep: ] quote: "240 In Wales 250 GB Trips per person"
  - p180 GB average out-of-home spend per trip (Kantar OOH, 52 w/e 01 Jan 2017) = **3.86** GBP per trip (2016-01-03..2017-01-01) [keep: ] quote: "£3.86 Our average GB spend per trip"
  - p181 GB out-of-home purchase frequency per week (Kantar OOH, 52 w/e 01 Jan 2017) = **4.8** times per week (2016-01-03..2017-01-01) [keep: ] quote: "4.8 times a week in GB, 4.6 in Wales"
  - p182 GB population share buying out of home (Kantar OOH, 52 w/e 01 Jan 2017) = **97** % of population (2016-01-03..2017-01-01) [keep: ] quote: "97% buy Out of Home in GB 98% in Wales"
  - p183 GB population share buying coffee out of home over a year (Kantar OOH, 52 w/e 01 = **69.9** % of population (2016-01-03..2017-01-01) [keep: ] quote: "69.9% Population buy Coffee out of home over a year"
- dropped by code checks: 29 (period_end missing or unparseable: 18; number: no number in value_as_written: 4; period_end 2028-12-31 after as_of: 1; scale word 'billion' not supported by quote or table header: 6)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['tea consumption', 'uk tea', 'cups per day']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p22', 'p38', 'p102'] All four are the same ~100 million cups/day UK headline, ultimately traceable to UKTIA/ITC industry estimates. They are not independent measurements; they corroborate a stable industry anchor but shar
- corroborating: ['p39', 'p103'] Both give 36 billion cups/year, the annualised form of the ~100 million/day figure (36bn/365 ≈ 98.6m). Same ITC/UKTIA lineage, so redundant with p1/p22/p38/p102.
- corroborating: ['p24', 'p28'] p28 is the arithmetic result of the Aldi methodology (31,758,667 adults × 55% × 4 cups). p24 is the rounded headline. They are the same calculation, not independent evidence.
- corroborating: ['p24', 'p25', 'p27', 'p28'] Internally consistent Aldi survey chain: adult population × tea-preferring share × 4 cups/day. The 127m figure is a survey-based estimate that conflicts in level with the ~100m industry anchor, but us
- conflicting: ['p1', 'p24'] Industry anchor ~100m/day vs Aldi survey-derived 127m/day. The gap likely reflects methodology: Aldi applies 4 cups/day to 55% of adults (a high per-drinker rate and a broad prevalence), while the ind
- corroborating: ['p13', 'p17', 'p18'] Apparent consumption 113kt ≈ imports 133kt − exports 20kt = 113kt. Internally consistent physical-flow identity for 2015.
- corroborating: ['p14', 'p13'] Per-capita 1,941 g/yr × ~65m population ≈ 126kt, roughly consistent with the 113kt apparent consumption (order-of-magnitude agreement, different years/sources).
- conflicting: ['p45', 'p13'] Statista 72m kg/yr (excluding herbal/RTD/instant) is well below the 113kt apparent consumption; scope differences (exclusions, retail vs total) explain much of the gap. Use with caution as a lower-bou
- corroborating: ['p48', 'p52', 'p54', 'p56', 'p58'] YouGov age-cohort daily tea-drinking shares (11–32%) are mutually consistent and show a clear age gradient; they are one survey family, not independent of each other.
- corroborating: ['p63', 'p64', 'p65'] YouGov 2015 per-capita 884 cups/yr and age-band weekly rates are internally consistent (over-55s 21/wk, 18–24s 8/wk). Older vintage; useful for calibrating grams-per-cup and prevalence, not for direct
- corroborating: ['p84', 'p85'] p85 is the arithmetic conversion of p84 at 3g/teabag; same source (Kantar). Confirms a ~3g-per-cup conversion factor and a declining-volume trend signal.
- corroborating: ['p89', 'p90'] Kantar 18.3bn tea occasions/yr and £663m spend are from the same Kantar dataset; occasions (~50m/day) are far below cups because occasions ≠ cups. Useful as a lower bound on drinking events, not cups.
- conflicting: ['p16', 'p78', 'p79'] p16 gives tea at 31.5% of away-from-home hot beverage servings (2010); p78/p79 give tea at only 3.8–4.1% of out-of-home hot drinks sales (2015–16). Different metrics (servings vs sales value) and peri
- corroborating: ['p3', 'p5'] Duplicate global 5bn cups/day statements from the same UKTIA page; redundant.
- corroborating: ['p4', 'p6'] Duplicate global 2bn coffee cups/day statements; redundant.
- corroborating: ['p23', 'p71'] Same 35% 'three or more cups a day' statistic from the same 2023 Product of the Year survey; duplicate.
- corroborating: ['p76', 'p100'] Same Mintel chai-latte 94% growth figure; duplicate.
- corroborating: ['p77', 'p101'] Same Birchall 14-award figure; duplicate.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p22', 'p38', 'p102', 'p132', 'p162'] All are the same ~100 million cups/day UKTIA/ITC headline, repeated across years and URLs. They are not independent measurements; they share one underlying industry estimate. Useful as a stable anchor
- corroborating: ['p24', 'p28'] p28 is the arithmetic result of the Aldi methodology (adults × 55% × 4 cups) that produces p24. Same source, same inputs; p28 adds no independent information beyond p24.
- conflicting: ['p24', 'p25', 'p27', 'p28'] The Aldi 127m figure conflicts with the ~100m UKTIA/ITC anchor. The conflict is largely methodological: Aldi applies 4 cups/day to 55% of adults, an implausibly high per-drinker rate, and excludes chi
- corroborating: ['p39', 'p103', 'p133'] 36 billion cups/year is the annualised form of ~100m cups/day (36bn/365 ≈ 98.6m). Same ITC source; redundant with the daily headline.
- corroborating: ['p13', 'p17', 'p18'] 2015 apparent consumption (113kt) is consistent with imports 133kt minus exports 20kt. Internally coherent physical-flow set for 2015, but old and pre-dating the target year.
- corroborating: ['p45', 'p139'] Both give 72 million kg/year UK tea consumption (Statista, excluding herbal/RTD/instant). Same source, duplicate. Useful as a volume anchor for black/leaf tea only.
- corroborating: ['p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125'] These are partner-level rows of the same 2023 HS090230 black-tea import table; they sum to the World total p112. Not independent; p112 is the usable aggregate. Note HS090230 covers only packaged black
- corroborating: ['p48', 'p145'] Same YouGov statistic (41% drink tea at home/work at least twice a day), duplicated. Measures a frequency threshold, not prevalence or cups/day.
- corroborating: ['p52', 'p54', 'p56', 'p58', 'p148', 'p149', 'p150', 'p151'] Age-band daily tea-drinking shares from one YouGov survey, duplicated across ids. Internally consistent (rising with age); usable to build a weighted prevalence but not cups per drinker.
- corroborating: ['p23', 'p160'] Same 2023 Product of the Year statistic (35% of tea drinkers drink 3+ cups/day), duplicated. A threshold share, not a mean.
- corroborating: ['p63', 'p64', 'p65'] YouGov 2015 survey: 884 cups/person/year overall, with 21 cups/week for over-55s and 8 for 18-24s. Internally consistent age gradient; old but a usable per-capita anchor needing trend adjustment.
- conflicting: ['p78', 'p79', 'p175'] Out-of-home tea share differs by metric: 4.1%/3.8% of servings (p78/p79) versus 17% of spend (p175). Different denominators (servings vs spend, and tea cheaper than coffee), so not a true contradictio
- corroborating: ['p104', 'p131'] Same UKTIA claim that 98% of UK residents drink tea daily, duplicated. Implausibly high versus YouGov age-band shares; treat as marketing hyperbole, not a usable prevalence.
- corroborating: ['p84', 'p85'] p85 is the cup-equivalent of p84 at 3g/teabag. Same Kantar data; p85 supplies a grams-per-cup conversion (3g) rather than an independent level.
- conflicting: ['p89'] 18.3bn tea-drinking occasions (Kantar, year to Feb 2019) is far below 36bn cups/year. Occasions ≠ cups (multiple cups per occasion, and occasion definition differs), so it is a lower-bound context, no
- corroborating: ['p126', 'p127', 'p128', 'p129', 'p130'] US tea statistics. Different country and mostly different scope (includes RTD/iced); not transferable to the UK target except as loose context.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Grams of tea per cup (dry leaf, all tea types) | 2.5 | 1.8..3.5 | 1.775..3.55 (widened) | g per cup | unused | p85 uses 3g per teabag as the industry convention; herbal/fruit and green teas use less leaf per cup and loose-leaf varies, so a central 2.5g with a wide range brackets the 3g teabag convention. | Converting dry tea mass to cups for all tea types averaged over the year. | A current UK survey or industry statement giving grams per cup materially outside 1.8–3.5g. |
| a2 | Out-of-home share of total UK tea cups | 0.15 | 0.08..0.25 | 0.08..0.25 | fraction | unused | p50/p147 show only 16% of tea drinkers buy tea out of home weekly, and p78/p79 show tea is a small share of out-of-home hot drinks; most tea is drunk at home. A modest out-of-home fraction is consistent with these. | Grossing at-home retail tea volume up to total consumption including foodservice. | Evidence that out-of-home tea is a much larger share of total cups (e.g. >30%). |
| a3 | Trend factor: 2026 vs 2015 per-capita tea consumption | 0.85 | 0.7..1 | 0.7..1 | fraction | m4 (m4) | UK tea consumption has been slowly declining (p84/p85 show a steep 2018 volume fall; coffee substitution noted in d6). Applying a modest decline factor to the 2015 YouGov per-capita figure (p63) brings it toward the target year. | Adjusting the 2015 per-capita cups figure to 2026. | Evidence that UK per-capita tea consumption has been flat or rising since 2015. |
| a4 | UK population 2026 | 69,000,000 | 67,000,000..71,000,000 | 48,769,868..97,539,735 (widened) | people | m4 (m4) | No kept point gives current UK population; ONS mid-year estimates put the UK around 68–69 million in the mid-2020s. Used to scale per-capita cups to a national total. | Scaling a per-person cups figure to the whole UK population. | An ONS population estimate for 2026 outside 67–71 million. |
| a5 | Mean cups per day among daily tea drinkers | 2.5 | 1.8..3.5 | 1.775..3.55 (widened) | cups per drinker per day | unused | p23/p160 show 35% of tea drinkers have 3+ cups/day and p161 shows 20% have 5–10; a mean around 2.5 cups/day among daily drinkers is consistent with that right-skewed distribution. | Combining a daily-drinker prevalence with a per-drinker cup rate. | A representative survey giving a mean cups/day among daily drinkers outside 1.8–3.5. |
| a6 | Share of UK adults who drink tea daily (age-weighted) | 0.25 | 0.18..0.33 | 0.1723..0.3447 (widened) | fraction | unused | YouGov age-band daily shares (p52/p54/p56/p58) range 11–32%; weighting by UK age structure gives roughly a quarter of adults drinking tea daily. The 98% UKTIA claim (p104) is implausible and not used. | Building a base-rate estimate of daily tea drinkers. | A representative survey showing daily tea-drinking prevalence well outside 18–33% of adults. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_naive | n/a |  | [] |  | 0.00 |  | series_naive needs 1 earlier years, has 0 |
| m2 | formula_mc | 127,075,234 | ['p24'] / [] | [] |  | 0.50 | equal |  |
| m3 | formula_mc | n/a | ['p45'] / ['a1', 'a2'] | [] |  | 0.00 |  | formula: numeric constant 1000 not allowed (only 1 and exponents); make it a named input. If the number only converts units (1000 g per kg, days per year), drop it and set the method's "unit" to the u |
| m4 | formula_mc | 139,162,770 | ['p63'] / ['a3', 'a4'] | [] |  | 0.50 | equal |  |
| m5 | formula_mc | n/a | [] / ['a4', 'a5', 'a6'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |

- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target
- m5 coverage: the whole target

Result: central **132,981,734** cup/day, 80% interval [86,684,636, 204,005,491] cup/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-12-31, after as_of: it cannot have been published yet


## Final answer

The best computed estimate is 132,981,734 cup/day (80% model-based interval 86,684,636 to 204,005,491 cup/day) for total cups of tea consumed in the UK on an average day in 2026, counting all tea types, at home and out of home. Two routes were kept and weighted equally: a survey-based upper scenario anchored on 127,000,000 cups per day and a per-capita route using 884 cups of tea per person per year scaled by trend factor 0.85 (range 0.7 to 1) and population 69,000,000 (range 48,769,868 to 97,539,735). The volume route and base-rate route were rejected by code, so the combination rests on limited evidence. Observed inputs are the survey and headline figures; the trend factor and population are analyst assumptions, not observations. The result could be wrong mainly because the per-capita base is dated and the trend adjustment is uncertain. Better evidence would be a current, all-tea consumption survey with a clear cups-versus-mugs definition.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a3 Trend factor: 2026 vs [n] per-capita tea consumption: 0.85 fraction, range 0.7 to 1; used by m4. Overturned by: Evidence that UK per-capita tea consumption has been flat or rising since [n].
- a4 UK population 2026: 69,000,000 people, range 48,769,868 to 97,539,735 (range widened by code); used by m4. Overturned by: An ONS population estimate for 2026 outside [n]–[n] million.

# Evidence ledger: smoke_tea

- Question: How many cups of tea do people in the United Kingdom drink per day?
- as_of: 2026-10-17
- Pinned target: Total number of cups of tea consumed by people in the United Kingdom per day, counting all tea-drinking occasions (cups/mugs of tea, including from tea bags, loose leaf, and prepared tea), averaged over a representative day in the most recent period before the cutoff | unit cups per day | period 2025-01-01..2026-10-17 | publisher No single official publisher; constructed from industry (UK Tea & Infusions Association), survey (Defra/NatCen), and retail data

## Directions and pages

### d1 [related_series] Industry association / trade body

Hypothesis: UK Tea & Infusions Association and trade press publish estimates of daily cups of tea consumed in the UK (commonly cited as ~100 million cups/day). This directly gives the target or a close proxy; role is to anchor the central estimate. Transfer assumption: figure refers to hot tea, all locations, whole population.

Queries issued by the searcher: UK Tea and Infusions Association cups of tea per day; how many cups of tea drunk in UK daily million; tea.co.uk UKTIA "100 million cups" statistics tea consumption UK 2026; UK tea consumption tonnes per year statistic retail tea volume "tonnes" Defra

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 13/6
  - p1 Share of 18–24-year-olds having a daily cuppa = **83** % of 18–24-year-olds (2022-12-01..2022-12-31) [DISCARD: 83% 18-24 daily-cuppa share; not a population-level input.] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p2 Share of younger adults citing great taste as reason = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Taste-reason share; no bearing on cup volume.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p3 Share of over-25s citing great taste as reason = **85** % of over 25s (2022-12-01..2022-12-31) [DISCARD: Taste-reason share; no bearing on cup volume.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p4 Share of younger adults saying they drink more tea than parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Share drinking more tea than parents; not a volume input.] quote: "31% of younger adults polled saying they drink more tea than their parents"
  - p5 UK adults surveyed in omnibus research = **4,000** UK adults (2022-12-01..2022-12-31) [DISCARD: Sample size only; no volume information.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p6 UK adults surveyed in second poll = **1,000** UK adults (2023-03-01..2023-05-31) [DISCARD: Sample size only; no volume information.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 14/3
  - p7 Global tea market value forecast for 2025 = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Global tea market value forecast; irrelevant to UK cup count.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p8 Number of adults surveyed (March, UKTIA Tea Census) = **1,010** adults surveyed (2024-03-01..2024-03-31) [DISCARD: Sample size only; no volume information.] quote: "nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
  - p9 UK tea exports value 2023 = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: UK tea export value; exports are not consumption and value units don't convert to cups.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/0
- `https://www.gbnews.com/news/national-tea-day-britons-celebrate-60billion-cups-drunk-per-year-uk` -> **live_dated** (page date 2025-04-21); points raw/verified 3/0
- dropped by code checks: 36 (period_end missing or unparseable: 35; value_as_written not in quote as a whole number: 1)

### d2 [physical_flow] Retail and wholesale tea supply

Hypothesis: National tea supply (production + imports - exports +/- stocks) or retail tea sales volume in tonnes, divided by average grams of tea per cup, yields cups per day. Role: independent physical-flow route. Transfer assumption: grams per cup (~2-3 g for tea bags) and that supply approximates consumption.

Queries issued by the searcher: UK tea imports tonnes per year Defra tea consumption tonnes; grams of tea per cup tea bag weight UK; UK Tea & Infusions Association tea consumption cups per day tonnes; Defra tea imports UK 2023 tonnes; FAO tea consumption United Kingdom tonnes 2022; UK tea market volume tonnes 2024 retail sales

- `https://menafn.com/1104246395/KNOW-THE-NATION-TO-A-TEA-TEA-CENSUS-REPORT-2022-LAUNCHED-ON-INTERNATIONAL-TEA-DAY-21St-MAY-2022?source=294` -> **live_dated** (page date 2024-01-02); points raw/verified 0/0
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day?trk=article-ssr-frontend-pulse_little-text` -> **live_dated** (page date 2026-01-01); points raw/verified 14/6
  - p10 Share of 18–24-year-olds having a daily cuppa (survey) = **83** % of 18–24-year-olds surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1 (same 83% 18-24 daily-cuppa figure, same source).] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p11 Share of 18–24-year-olds citing great taste as reason (survey) = **80** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p12 Share of over-25s citing great taste as reason (survey) = **85** % of over-25s surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p13 Share of younger adults drinking more tea than parents (survey) = **31** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4; irrelevant.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p14 UK adults surveyed in real-world research (sample size) = **4,000** UK adults (2022-12-01..2022-12-31) [DISCARD: Duplicate sample size; no volume information.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p15 UK adults polled in second survey (sample size) = **1,000** UK adults (2023-03-01..2023-05-31) [DISCARD: Duplicate sample size; no volume information.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `https://www.cbi.eu/sites/default/files/pdf/research/666.pdf` -> **live_dated** (page date 2023-07-10); points raw/verified 15/14
  - p16 UK tea consumption volume, 2015 (largest European consumer) = **113,000** tonnes (2015-01-01..2015-12-31) [keep: ] quote: "the United Kingdom is the largest consumer by far, with consumption amounting to 113 thousand tonnes in 2015."
  - p17 UK tea imports volume, 2015 = **133,000** tonnes (2015-01-01..2015-12-31) [keep: ] quote: "The United Kingdom is by far the largest importer of tea in Europe, with imports amounting to about 133 thousand tonnes in 2015."
  - p18 UK share of all European tea imports, 2015 = **39** percent (2015-01-01..2015-12-31) [keep: ] quote: "The country accounts for 39% of all European imports, which is the result of an annual decrease of 3.6% since 2011."
  - p19 UK per capita tea consumption, 2015 = **1.9** kilograms per capita (2015-01-01..2015-12-31) [keep: ] quote: "The United Kingdom (1.9 kg per capita);"
  - p20 Ireland per capita tea consumption, 2015 (highest in Europe) = **2.2** kilograms per capita (2015-01-01..2015-12-31) [DISCARD: Ireland per-capita consumption; different country, not a UK input.] quote: "Ireland with 2.2 kilograms (kg);"
  - p21 Apparent tea consumption in Europe, 2015 = **229,000** tonnes (2015-01-01..2015-12-31) [DISCARD: Europe apparent consumption; not UK.] quote: "The apparent tea consumption in Europe amounted to 229 thousand tonnes in 2015 (based on import and export data)."
  - p22 Global tea consumption, 2015 = **5,000,000** tonnes (2015-01-01..2015-12-31) [DISCARD: Global consumption; not UK.] quote: "This represents about 4.6% of the global tea consumption of 5 million tonnes."
  - p23 European Union tea imports, 2015 = **342,000** tonnes (2015-01-01..2015-12-31) [DISCARD: EU imports; not UK consumption.] quote: "In 2015, tea imports in the European Union amounted to 342 thousand tonnes, showing an average annual decrease of 2% since 2011."
  - p24 European tea exports volume, 2015 = **113,000** tonnes (2015-01-01..2015-12-31) [DISCARD: European exports; not UK consumption.] quote: "Between 2011 and 2015, the volume of European tea exports increased slightly (0.4% annually), amounting to about 113 thousand tonnes in 2015."
  - p25 Portugal tea production, 2013 = **140** tonnes (2013-01-01..2013-12-31) [DISCARD: Portugal tea production; irrelevant.] quote: "For example, Portugal produced 140 tonnes in 2013 (FAOSTAT, 2016)."
  - p26 China orthodox tea production, 2013 = **1,924,000** tonnes (2013-01-01..2013-12-31) [DISCARD: China tea production; irrelevant.] quote: "In 2013, Chinese production of orthodox tea reached 1,924 thousand tonnes."
  - p27 Germany tea supplied to European market, 2015 = **20,000** tonnes (2015-01-01..2015-12-31) [DISCARD: Germany tea supply to Europe; irrelevant to UK.] quote: "In 2015, they supplied 20 thousand tonnes and 19 thousand tonnes, respectively."
  - p28 Poland tea supplied to European market, 2015 = **19,000** tonnes (2015-01-01..2015-12-31) [DISCARD: Poland tea supply to Europe; irrelevant to UK.] quote: "In 2015, they supplied 20 thousand tonnes and 19 thousand tonnes, respectively."
  - p29 UK black tea share of market, 2015 = **97** percent (2015-01-01..2015-12-31) [keep: ] quote: "Market shares of black tea range from about 53% (in the Netherlands) to 97% in the United Kingdom."
- `https://teas.co.uk/product/twinings-assam-80-tea-bags-200g/` -> **live_dated** (page date 2026-09-13); points raw/verified 5/0
- dropped by code checks: 14 (period_end missing or unparseable: 12; value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 1)

### d3 [base_rates] Population survey / consumer panel

Hypothesis: Population (or adults) multiplied by share who drink tea multiplied by average cups per tea drinker per day gives total cups/day. Role: decomposition route using survey base rates. Transfer assumption: survey shares representative of whole population and all days.

Queries issued by the searcher: percentage of UK adults who drink tea survey cups per day; UK Tea & Infusions Association 100 million cups tea per day statistics; tea.co.uk UKTIA survey 2025 "nine in 10" cups of tea a day press release; YouGov UK tea drinking habits survey how many cups a day

- `https://www.cravemag.co.uk/6-in-10-brits-still-rely-on-tea-to-stay-calm-new-study-finds/` -> **live_dated** (page date 2025-12-11); points raw/verified 11/11
  - p30 Share of UK adults surveyed who drink tea to calm down (UKTIA survey of over 1,0 = **60** % (..) [DISCARD: Share drinking tea to calm down; not a volume input.] quote: "nearly two thirds (60%) polled in our real-world study of over 1,000 adults1 saying they drink tea to get them to calm down"
  - p31 Share of UK adults aged 25-34 surveyed who agree they drink tea to calm down = **83** % (..) [DISCARD: Calm-down share by age; not a volume input.] quote: "twice as many younger adults (25-34 years category; 83%) agreed with this statement"
  - p32 Share of UK adults aged 65+ surveyed who agree they drink tea to calm down = **38** % (..) [DISCARD: Calm-down share by age; not a volume input.] quote: "compared with the older generation (65+ years category; 38%)"
  - p33 Share of UK people surveyed who drink at least one cup of tea a day = **10** share of people surveyed (proportion) (..) [DISCARD: Malformed value (10 for 'more than nine in 10'); unusable as parsed.] quote: "which shows that more than nine in 10 people drink at least one cup of tea a day"
  - p34 Share of UK people surveyed who drink the recommended three to four cups of tea  = **35** % (..) [DISCARD: Bin share from an undated small survey; not used numerically.] quote: "Over a third (35%) drink the recommended three to four cups"
  - p35 Share of UK people surveyed who drink one or two cups of tea a day = **44** % (..) [DISCARD: Bin share; not used numerically.] quote: "while four in 10 (44%) drink one or two a day"
  - p36 Share of UK people surveyed who drink five to six cups of tea a day = **20** % (..) [DISCARD: Bin share; not used numerically.] quote: "and a thirsty one in five (20%) drink five to six cups a day"
  - p37 Share of UK people surveyed who like to brew a tea for thinking time = **64** % (..) [DISCARD: Attitude share; not a volume input.] quote: "nearly two thirds (64%) of Brits like to brew a tea to give them some thinking time"
  - p38 Share of UK people surveyed who would pick a regular cup of tea as their only ho = **66** % (..) [DISCARD: Preference share; not a volume input.] quote: "the top answer (66%) was a regular cup of tea, whatever their age"
  - p39 Share of UK people surveyed who agree a cuppa gives people comfort = **59** % (..) [DISCARD: Comfort attitude share; not a volume input.] quote: "nearly six in 10 (59%) agreed that having a cuppa gives people comfort"
  - p40 Number of adults in UKTIA real-world study sample = **1,000** adults surveyed (..) [DISCARD: Duplicate sample size; no volume information.] quote: "polled in our real-world study of over 1,000 adults1"
- `https://www.tea.co.uk/assets/uploads/files/news/4ea32-uk-tea-report-2023-3149-for-web-spreads.pdf` -> **live_dated** (page date 2023-05-05); points raw/verified 15/12
  - p41 Share of UK survey respondents who drink 1 to 2 cups of tea per day = **38** % (..) [DISCARD: Bin share; not used numerically.] quote: "38% of people drink 1 to 2 cups of tea per day"
  - p42 Share of UK survey respondents who drink 3 to 4 cups of tea per day = **36** % (..) [DISCARD: Bin share; not used numerically.] quote: "36% drink 3 to 4 cups"
  - p43 Share of UK survey respondents who drink 5 to 6 cups of tea per day = **15** % (..) [DISCARD: Bin share; not used numerically.] quote: "15% drink 5 to 6 cups"
  - p44 Share of UK survey respondents who drink more than 11 cups of tea per day = **2** % (..) [DISCARD: Bin share; not used numerically.] quote: "A tiny 2% drink more than 11 cups"
  - p45 Share of 18-24-year-olds in UK who have developed a taste for tea = **83** % (..) [DISCARD: Restatement of the same 83% 18-24 figure with looser wording; adds no information beyond p1.] quote: "Over eight in 10 (83%) 18 to 24-year-olds have developed a taste for tea."
  - p46 Share of UK survey respondents who drink more tea during autumn = **32** % (..) [DISCARD: Seasonal attitude share; not a volume input.] quote: "This was followed by 32% who drink more tea during the autumn."
  - p47 Share of UK survey respondents who have not changed tea consumption due to energ = **50** % (..) [DISCARD: Energy-price response share; not a volume input.] quote: "Around half (50%) of people have not changed their tea consumption because of energy price rises."
  - p48 Share of UK survey respondents who make more tea due to energy price rises = **25** % (..) [DISCARD: Energy-price response share; not a volume input.] quote: "Only 25% have less tea than before and the same number, 25%, actually make more tea."
  - p49 Share of UK survey respondents who boil one cup of water to make one cup of tea = **23** % (..) [DISCARD: Water-boiling behaviour; not a cup-count input.] quote: "Only 23% boil one cup (to make one cup) according to our poll"
  - p50 Share of UK survey respondents who drink black tea at home = **71** % (..) [DISCARD: At-home share of black tea; could inform a home/out-of-home split but no out-of-home volume to combine with; kept only a] quote: "71% of black tea is drunk at home."
  - p51 Share of UK survey respondents who would feel something missing without a mornin = **72** % (..) [DISCARD: Attitude share; not a volume input.] quote: "72% of respondents said that they would feel there was something missing if they didn't have a cup of tea in the morning."
  - p52 Share of UK survey respondents who use tea bags for black tea = **77** % (..) [DISCARD: Tea-bag use share; not needed for cup count.] quote: "77% of people use tea bags"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 12/11
  - p53 Share of UK residents who drink tea daily (UKTIA survey) = **98** % of UK residents (..) [DISCARD: 98% daily-drinker share is implausibly high and sample-skewed; not usable as a population share.] quote: "In May, the UK Tea & Infusions Association (UKTIA) revealed that 98% of UK residents drink tea daily."
  - p54 Cups of tea drunk every day in the UK (ITC estimate, cited by UKTIA) = **100,000,000** cups per day (..) [keep: ] quote: ""More than 100 million cups of tea are drunk every day here in the UK," she said, citing the International Tea Committee (ITC)"
  - p55 UK annual tea consumption in cups (ITC estimate) = **36,000,000,000** cups per year (..) [keep: ] quote: "which estimates consumption at 36 billion cups per year."
  - p56 Adults surveyed in UKTIA March survey = **1,010** adults (2024-03-01..2024-03-31) [DISCARD: Sample size only; no volume information.] quote: "nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
  - p57 Share of surveyed adults using tea bags to make black tea = **84** % of surveyed adults (2024-03-01..2024-03-31) [DISCARD: Tea-bag share; not a volume input.] quote: ""It's no surprise that 84% pick the option of a tea bag to make their black tea, with 16% opting for loose leaf," said Hall."
  - p58 Share of surveyed adults using loose leaf to make black tea = **16** % of surveyed adults (2024-03-01..2024-03-31) [DISCARD: Loose-leaf share; not a volume input.] quote: "with 16% opting for loose leaf," said Hall."
  - p59 Share of surveyed adults drinking black tea without milk = **24** % of surveyed adults (2024-03-01..2024-03-31) [DISCARD: Milk/no-milk share; not a volume input.] quote: "nearly a quarter (24%) said they drink their black tea as it comes, without any milk,"
  - p60 Share of UK fluid intake that is tea (Tea Advisory Panel) = **40** % of nation's fluid intake (..) [DISCARD: Share of fluid intake; not directly convertible to cups without total fluid intake.] quote: "even today, 40% of the nation's fluid intake will be tea, according to the Tea Advisory Panel (TAP)."
  - p61 UK tea market value (Statista) = **1,700,000,000** GBP (£) (..) [DISCARD: Market value; no volume conversion available.] quote: "According to Statista market research, the UK market is valued at £1.7 billion ($2.2 billion)."
  - p62 UK annual tea consumption in kilos, excluding herbal infusions, RTD and instant  = **72,000,000** kilos per year (..) [keep: ] quote: "Statista Market Insights estimates UK consumption at 72 million kilos annually, excluding herbal infusions, ready-to-drink, and instant tea."
  - p63 Average UK tea spend per person per week (Statista) = **15** pence per person per week (..) [DISCARD: Spend per person; no price-per-cup bridge available.] quote: "According to Statista, UK residents spend an average of 15 pence per person per week on tea."
- `https://www.nationwide.co.uk/media/news/nationwide-spills-the-tea-on-britains-longest-standing-love-affair` -> **live_dated** (page date 2025-04-21); points raw/verified 15/13
  - p64 Share of people choosing tea as their first drink of the day = **31** percent of people (..) [DISCARD: First-drink-of-day share; not a daily cup count.] quote: "31 per cent of people choose to drink tea as their first drink of the day"
  - p65 Share of people choosing coffee as their first drink of the day = **26** percent of people (..) [DISCARD: First-drink share; not a volume input.] quote: "ahead of coffee (26%), water (22%) and juice (5%)"
  - p66 Share of people choosing water as their first drink of the day = **22** percent of people (..) [DISCARD: First-drink share; not a volume input.] quote: "ahead of coffee (26%), water (22%) and juice (5%)"
  - p67 Share of people choosing juice as their first drink of the day = **5** percent of people (..) [DISCARD: First-drink share; not a volume input.] quote: "ahead of coffee (26%), water (22%) and juice (5%)"
  - p68 Share of people saying a cup of tea provides comfort and routine = **71** percent of people (..) [DISCARD: Attitude share; not a volume input.] quote: "just over seven in ten (71%) say a cup of tea provides comfort and routine"
  - p69 Share of people saying tea makes them feel relaxed = **49** percent of people (..) [DISCARD: Attitude share; not a volume input.] quote: "almost half (49%) say it makes them feel relaxed"
  - p70 Share of Brits using tea to check in on an older relative = **56** percent of Brits (..) [DISCARD: Attitude share; not a volume input.] quote: "56 per cent of Brits using it to check in on an older relative"
  - p71 Share of people who drink tea naming breakfast tea as favourite blend = **53** percent of tea drinkers (..) [DISCARD: Blend preference; not a volume input.] quote: "more than half of people who drink tea (53%) named breakfast tea as their favourite blend"
  - p72 Share of people who drink tea who used a teapot in the last week = **43** percent of tea drinkers (..) [DISCARD: Teapot use; not a volume input.] quote: "43 per cent of people who drink tea used a teapot to make a cuppa in the last week"
  - p73 Share of 16 to 24-year-olds who drink tea and used a teapot in the last week = **56** percent of 16-24 year old tea drinkers (..) [DISCARD: Teapot use by age; not a volume input.] quote: "rising to a remarkable 56 per cent among 16 to 24-year-olds"
  - p74 Share of people preferring golden brown shade of tea = **53** percent of people (..) [DISCARD: Colour preference; not a volume input.] quote: "golden brown is the most popular shade of tea (53%)"
  - p75 Share of people preferring stronger darker 'builder's tea' = **18** percent of people (..) [DISCARD: Strength preference; not a volume input.] quote: "close to a fifth (18%) prefer a stronger, darker 'builder's tea'"
  - p76 Share of people preferring sugar in their tea = **53** percent of people (..) [DISCARD: Sugar preference; not a volume input.] quote: "slightly more people prefer having sugar in their tea than not, at 53 per cent versus 47 per cent"
- dropped by code checks: 6 (number: no number in value_as_written: 5; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d4 [capacity_consumption] Household penetration and frequency

Hypothesis: Households buying tea (penetration) times purchase frequency times cups per pack, or per-capita cups from household panel. Role: cross-check via household consumption. Transfer assumption: household purchases map to individual consumption without large waste.

Queries issued by the searcher: Kantar UK tea household penetration purchase frequency; Defra family food tea consumption per person UK; Defra Family Food 2023 tea purchases grams per person per week UK; UK Tea and Infusions Association 100 million cups of tea a day statistics

- `https://www.kantar.com/uki/inspiration/consumer/our-feelings-about-tea-in-the-uk` -> **live_dated** (page date 2019-04-17); points raw/verified 15/8
  - p77 UK tea-drinking occasions per year (national total), year to February 2019 = **18,300,000,000** tea-drinking occasions per year (2018-02-01..2019-02-28) [DISCARD: Kantar 18.3bn occasions is in-home and one-cup-per-occasion; too narrow and dated to serve as a full total, and no relia] quote: "That said, we still enjoyed a cuppa on 18.3 billion occasions as a nation."
  - p78 Total UK spend on tea, 52 weeks ending March 2019 = **663,327,000** GBP (2018-03-25..2019-03-24) [DISCARD: Tea spend; no price-per-cup bridge.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p79 Year-on-year change in UK tea spend = **1** percent (2018-03-25..2019-03-24) [DISCARD: Spend change; not a volume input.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p80 Year-on-year increase in average tea price per kilogram = **7** pence per kilogram (2018-03-25..2019-03-24) [DISCARD: Price change; not a volume input.] quote: "that decline is despite prices rising by 7p a kilogram (+3.1% year on year) this year."
  - p81 Year-on-year percentage increase in average tea price per kilogram = **3.1** percent (2018-03-25..2019-03-24) [DISCARD: Price change; not a volume input.] quote: "prices rising by 7p a kilogram (+3.1% year on year) this year."
  - p82 Year-on-year increase in spend on Speciality Tea, 52 weeks ending March 2019 = **4.2** percent (2018-03-25..2019-03-24) [DISCARD: Speciality tea spend change; not a volume input.] quote: "Spending on Speciality Tea is up 4.2% (52 w/e March 2019 vs. 2018)"
  - p83 Year-on-year increase in average price of Speciality Tea = **2.7** percent (2018-03-25..2019-03-24) [DISCARD: Speciality tea price change; not a volume input.] quote: "the average price has gone up 2.7%"
  - p84 Year-on-year increase in Speciality Tea occasions = **10** percent (2018-03-25..2019-03-24) [DISCARD: Speciality tea occasion change; not a total volume input.] quote: "Occasions involving speciality tea were up 10% in the time period, or 100m."
- `https://www.gov.uk/government/statistical-data-sets/family-food-datasets` -> **live_dated** (page date 2026-09-17); points raw/verified 0/0
- `https://www.gov.uk/government/statistics/family-food-fye-2023/family-food-fye-2023` -> **live_dated** (page date 2024-10-17); points raw/verified 15/12
  - p85 UK household purchases of beverages (tea/coffee etc.) per person per week, FYE 2 = **49** grams per person per week (2022-04-01..2023-03-31) [DISCARD: All-beverage purchases, not tea-specific; unusable as tea mass.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p86 UK household purchases of beverages per person per week, FYE 2022 = **57** grams per person per week (2021-04-01..2022-03-31) [DISCARD: All-beverage purchases; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p87 UK household purchases of beverages per person per week, FYE 2021 = **60** grams per person per week (2020-04-01..2021-03-31) [DISCARD: All-beverage purchases; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p88 UK household purchases of beverages per person per week, FYE 2020 = **56** grams per person per week (2019-04-01..2020-03-31) [DISCARD: All-beverage purchases; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p89 UK household purchases of beverages per person per week, FYE 2019 = **52** grams per person per week (2018-04-01..2019-03-31) [DISCARD: All-beverage purchases; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p90 Percentage change in UK household beverage purchases FYE 2022 to FYE 2023 = **-13.5** % (2022-04-01..2023-03-31) [DISCARD: Beverage purchase change; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p91 Percentage change in UK household beverage purchases FYE 2020 to FYE 2023 = **-11.4** % (2019-04-01..2023-03-31) [DISCARD: Beverage purchase change; not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p92 UK average household expenditure on household food and non-alcoholic drink, per  = **29.66** pounds per person per week (2022-04-01..2023-03-31) [DISCARD: Food expenditure; not a volume input.] quote: "\| Expenditure on household food and non-alcoholic drink \| £32.74 \| £32.78 \| £35.58 \| £30.71 \| £29.66 \| -3.4% \| -9.5% \|"
  - p93 UK average household expenditure on all food and drink, per person per week, FYE = **43.33** pounds per person per week (2022-04-01..2023-03-31) [DISCARD: Food expenditure; not a volume input.] quote: "\| Total expenditure on all food and drink \| £53.85 \| £54.58 \| £44.76 \| £44.72 \| £43.33 \| -3.1% \| -20.6% \|"
  - p94 Share of UK household expenditure on food and non-alcoholic drinks, all househol = **11.2** percent of total household expenditure (2022-04-01..2023-03-31) [DISCARD: Expenditure share; not a volume input.] quote: "\| Food & non-alcoholic drinks \| 11.2 \|"
  - p95 Share of UK household expenditure on food and non-alcoholic drinks, lowest 20% o = **14.4** % (2022-04-01..2023-03-31) [DISCARD: Expenditure share; not a volume input.] quote: "while for the lowest 20% of households by equivalised disposable income it was higher at 14.4%"
  - p96 UK household purchases of soft drinks per person per week, FYE 2023 = **1,500** millilitres per person per week (2022-04-01..2023-03-31) [DISCARD: Soft drinks volume; not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
- `https://www.heraldscotland.com/life_style/14286142.food-thought-tea-toast-decline-survey-shows-consumers-adopting-healthier-diets/` -> **live_dated** (page date 2016-02-18); points raw/verified 11/5
  - p97 Average cups of tea per person per week in 1974 = **23** cups per person per week (1974-01-01..1974-12-31) [DISCARD: 1974 cups/person/week; historical baseline only, superseded by p113 mass series for trend.] quote: "that means Britons are drinking on average just eight cups of tea a week today, down from 23 in 1974."
  - p98 Number of households in National Food Survey sample (1974-2000) = **150,000** households (1974-01-01..2000-12-31) [DISCARD: Survey sample size; not a volume input.] quote: "The new data from 150,000 households who took part in the National Food Survey between 1974 and 2000"
  - p99 Reduction in bread eaten per person since 1974 (share) = **40** percent (1974-01-01..2014-12-31) [DISCARD: Bread consumption change; irrelevant.] quote: "But Britons have also reduced the amount of bread they eat by 40% since 1974."
  - p100 Bread slices per person per week in 1974 (40g slice basis) = **25** slices per person per week (1974-01-01..1974-12-31) [DISCARD: Bread slices; irrelevant.] quote: "the amount people are eating has fallen from 25 to 15 slices a week in the last four decades"
  - p101 Share of pay spent on food in 1974 = **24** percent of pay (1974-01-01..1974-12-31) [DISCARD: Food spend share; irrelevant.] quote: "when almost a quarter (24%) of the pay packet went on food"
- dropped by code checks: 16 (scale word 'million' not supported by quote or table header: 4; period_end missing or unparseable: 11; number: no number in value_as_written: 1)

### d5 [own_history] Historical trend of UK tea consumption

Hypothesis: Earlier estimates of UK daily cups (e.g., 165 million in 1970s declining to ~100 million) show a trend that can be extrapolated or used to sanity-check current figure. Role: constrain plausible range and direction. Transfer assumption: decline continues at historical rate.

Queries issued by the searcher: UK tea consumption decline history million cups per day 165 million 1970s; UK Tea and Infusions Association 100 million cups tea per day statistics; Defra Family Food tea purchases per person per week grams decline 1974 2022 UK; "million cups of tea" UK per day 2010 2015 UKTIA estimate decline from 165 million

- `https://www.theguardian.com/business/2005/sep/27/food.foodanddrink` -> **live_dated** (page date 2018-08-18); points raw/verified 15/4
  - p102 Annual retail sales decline of standard tea = **5.1** % decline (2004-07-01..2005-06-30) [DISCARD: Standard tea sales decline; no volume bridge.] quote: "annual retail sales of standard tea (that is, non-premium teas) dropped 5.1% to £439.8m"
  - p103 Annual retail sales growth of standard instant coffee = **4.1** % growth (2004-07-01..2005-06-30) [DISCARD: Instant coffee growth; irrelevant.] quote: "standard instant coffee, up 4.1% at £439.9m"
  - p104 Standard tea share of hot drinks market by value, year to June 2005 = **33.5** % of hot drinks market value (2004-07-01..2005-06-30) [DISCARD: Market value share; no volume bridge.] quote: "Standard tea £439.84m 33.5%"
  - p105 Fruit and herbal tea share of hot drinks market by value, year to June 2005 = **3.1** % of hot drinks market value (2004-07-01..2005-06-30) [DISCARD: Market value share; no volume bridge.] quote: "Fruit and herbal tea £40.4m 3.1%"
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 15/7
  - p106 Share of 18-24-year-olds having a daily cuppa = **83** % of 18-24-year-olds (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1.] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p107 Share of 18-24-year-olds citing great taste as reason = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p108 Share of over-25s citing great taste as reason = **85** % of over 25s (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p109 Share of younger adults saying they drink more tea than parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4; irrelevant.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p110 Share of young adults brewing a cuppa on waking = **10** proportion of young adults (2022-12-01..2022-12-31) [DISCARD: Morning-brew share; not a volume input.] quote: "Seven out of 10 young adults brew up a cuppa as soon as they get out of bed."
  - p111 Sample size of UK adults in real-world research poll = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate sample size; not a volume input.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p112 Sample size of second UK adults poll = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [DISCARD: Duplicate sample size; not a volume input.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `https://uk.news.yahoo.com/why-have-brits-stopped-drinking-so-much-tea-193658616.html` -> **live_dated** (page date 2022-01-27); points raw/verified 15/11
  - p113 UK per-capita tea purchases, grams per week, 1974 = **68** grams of tea per person per week (1974-01-01..1974-12-31) [DISCARD: 1974 mass baseline; too old to extrapolate to 2025-26 without a reliable decline rate.] quote: "In 1974, a typical person bought 68g of tea a week each, now it's 22g."
  - p114 Year coffee purchases overtook tea in the UK = **2,015** year (2015-01-01..2015-12-31) [DISCARD: Coffee-overtook-tea year; contextual only, no volume.] quote: "Coffee overtook tea in 2015 and has kept its lead ever since."
  - p115 Share of Germans who said they drank tea (2020 YouGov survey) = **87** % of surveyed Germans (2020-01-01..2020-12-31) [DISCARD: German tea-drinking share; not UK.] quote: "87% of Germans and 81% of Swedes said they drank tea in a 2020 YouGov survey, compared to 78% of Brits."
  - p116 Share of Swedes who said they drank tea (2020 YouGov survey) = **81** % of surveyed Swedes (2020-01-01..2020-12-31) [DISCARD: Swedish tea-drinking share; not UK.] quote: "87% of Germans and 81% of Swedes said they drank tea in a 2020 YouGov survey, compared to 78% of Brits."
  - p117 Share of Brits who said they drank tea (2020 YouGov survey) = **78** % of surveyed Brits (2020-01-01..2020-12-31) [DISCARD: 78% drinker share from a 2020 YouGov survey; usable only as a wide-range assumption, not a precise input.] quote: "87% of Germans and 81% of Swedes said they drank tea in a 2020 YouGov survey, compared to 78% of Brits."
  - p118 UK per-capita whole milk purchases, ml per week, 1974 = **2,655** ml of whole milk per person per week (1974-01-01..1974-12-31) [DISCARD: Milk purchases; not tea volume.] quote: "In 1974 Brits bought on average 2,655ml of whole milk a week, compared to just 302ml in 2020."
  - p119 UK per-capita whole milk purchases, ml per week, 2020 = **302** ml of whole milk per person per week (2020-01-01..2020-12-31) [DISCARD: Milk purchases; not tea volume.] quote: "In 1974 Brits bought on average 2,655ml of whole milk a week, compared to just 302ml in 2020."
  - p120 UK per-capita skimmed milk purchases, ml per week, 1974 = **5** ml of skimmed milk per person per week (1974-01-01..1974-12-31) [DISCARD: Milk purchases; not tea volume.] quote: "with just 5ml bought on average in 1974 compared to 1,024ml in 2020."
  - p121 UK per-capita skimmed milk purchases, ml per week, 2020 = **1,024** ml of skimmed milk per person per week (2020-01-01..2020-12-31) [DISCARD: Milk purchases; not tea volume.] quote: "with just 5ml bought on average in 1974 compared to 1,024ml in 2020."
  - p122 UK per-capita potatoes purchases, grams per week, 1974 = **1,318** grams of potatoes per person per week (1974-01-01..1974-12-31) [DISCARD: Potato purchases; irrelevant.] quote: "with on average 1,318g purchased a week in 1974 compared to 355g in 2020."
  - p123 UK per-capita potatoes purchases, grams per week, 2020 = **355** grams of potatoes per person per week (2020-01-01..2020-12-31) [DISCARD: Potato purchases; irrelevant.] quote: "with on average 1,318g purchased a week in 1974 compared to 355g in 2020."
- `https://www.gov.uk/government/statistical-data-sets/family-food-datasets` -> **live_dated** (page date 2026-09-17); points raw/verified 0/0
- dropped by code checks: 23 (scale word 'million' not supported by quote or table header: 3; period_end missing or unparseable: 16; number: no number in value_as_written: 3; scale word 'billion' not supported by quote or table header: 1)

### d6 [related_series] Out-of-home / foodservice

Hypothesis: Out-of-home tea servings (cafes, restaurants, workplaces) plus home consumption equals total. Role: component split to check whether industry totals include foodservice. Transfer assumption: foodservice servings counted as cups.

Queries issued by the searcher: UK out of home tea servings per year foodservice cups; Allegra tea out of home UK market; UK Tea and Infusions Association 100 million cups tea per day 2024 statistics; "tea out of home" UK 2023 2024 million cups per day Allegra Project Tea

- `https://www.beveragestandardsassociation.co.uk/wp-content/uploads/2020/01/Tetley_Tea_Report2018.pdf` -> **live_dated** (page date 2020-01-01); points raw/verified 15/0
- `https://www.comunicaffe.com/tea-out-of-home-underperforms-as-brits-love-of-coffee-takes-over/` -> **live_dated** (page date 2022-01-05); points raw/verified 10/5
  - p124 UK coffee shop sector turnover 2016 = **8,900,000,000** pounds sterling turnover (2016-01-01..2016-12-31) [DISCARD: Coffee-shop turnover; no cup conversion.] quote: "The UK coffee shop sector increased by 12% in turnover to reach £8.9 billion in 2016"
  - p125 UK tea out-of-home category sales contribution to coffee shop market 2016 = **308,000,000** pounds sterling sales (2016-01-01..2016-12-31) [DISCARD: Tea OOH sales value; no price-per-cup input to convert.] quote: "the low performing tea out-of-home category contributing £308 million to the total sales"
  - p126 Tea share of total UK coffee shop market turnover 2016 = **3.8** percent of coffee shop market turnover (2016-01-01..2016-12-31) [DISCARD: Tea share of coffee-shop turnover; not a cup count.] quote: "The tea category currently accounts for 3.8% of the total coffee shop market turnover"
  - p127 Tea share of total UK coffee shop market turnover 2015 = **4.1** percent of coffee shop market turnover (2015-01-01..2015-12-31) [DISCARD: Duplicate of p126 (prior-year share); no added volume information.] quote: "declining in sales share from 4.1% in 2015"
  - p128 Forecast UK tea out-of-home category turnover year-end 2017 = **341** pounds sterling turnover (forecast) (2017-01-01..2017-12-31) [DISCARD: Forecast out-of-home turnover; forecast, not realised, and no cup bridge.] quote: "Allegra World Coffee Portal anticipates the category to continue similar growth in 2017 and reach £341 turnover by year-end"
- `https://www.publicsectorcatering.co.uk/news/ooh-tea-occasions-grow-while-coffee-slows-down-report-finds` -> **live_dated** (page date 2016-12-08); points raw/verified 15/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/3
  - p129 Global tea market value forecast for 2025 (estimated) = **134,400,000,000** USD ($) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p7 (global market value forecast); irrelevant.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p130 UK tea export value (2023, ranked 7th by value) = **121,400,000** USD ($) (2023-01-01..2023-12-31) [DISCARD: Duplicate of p9; irrelevant to consumption.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
  - p131 Japan green tea export value (2023, ranked 6th) = **210,100,000** USD ($) (2023-01-01..2023-12-31) [DISCARD: Japan green tea exports; irrelevant to UK consumption.] quote: "Green tea exporter Japan ranked 6th that year with $210.1 million in exports."
- dropped by code checks: 47 (scale word 'billion' not supported by quote or table header: 3; value_as_written not in quote as a whole number: 1; scale word 'million' not supported by quote or table header: 6; period_end missing or unparseable: 35; number: more than one number in value_as_written: 1; number: no number in value_as_written: 1)

### b1 [related_series] Reconcile the ITC/UKTIA ~100m cups/day with Kantar's 18.3bn occasions/year

Hypothesis: If Kantar occasions are ~1 cup each and exclude out-of-home, the gap (~50m/day) is the out-of-home + multi-cup-per-occasion component; resolving it would let us choose between the industry anchor and the panel figure and set the central estimate.

Queries issued by the searcher: Kantar Worldpanel tea occasions cups per occasion UK 18.3 billion; UKTIA 100 million cups tea foodservice out of home; Defra Family Food tea purchases cups per week; "100 million" cups tea UK "out of home" UKTIA; "tea" "occasions" Kantar UK "cups" per occasion; UKTIA tea consumption 36 billion cups International Tea Committee 100 million; Family Food 2022 tea purchases grams per person per week UK

- `https://www.kantar.com/uki/inspiration/consumer/our-feelings-about-tea-in-the-uk` -> **live_dated** (page date 2019-04-17); points raw/verified 15/8
  - p132 UK tea-drinking occasions, year to February 2019 (Kantar) = **18,300,000,000** tea-drinking occasions (2018-02-01..2019-02-28) [DISCARD: Duplicate of p77 (same Kantar 18.3bn occasions).] quote: "we still enjoyed a cuppa on 18.3 billion occasions as a nation."
  - p133 Total UK spend on tea, 52 weeks ending March 2019 (Kantar) = **663,327,000** pounds sterling (2018-03-25..2019-03-24) [DISCARD: Spend total; no cup conversion.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p134 Year-on-year change in total UK tea spend (Kantar) = **1** percent (2018-03-25..2019-03-24) [DISCARD: Spend change; irrelevant.] quote: "Spend on tea overall is £663,327,000 - down 1%."
  - p135 Year-on-year increase in tea price per kilogram (Kantar) = **7** pence per kilogram (2018-03-25..2019-03-24) [DISCARD: Price change; irrelevant.] quote: "prices rising by 7p a kilogram (+3.1% year on year) this year."
  - p136 Year-on-year percentage increase in tea price per kilogram (Kantar) = **3.1** percent (2018-03-25..2019-03-24) [DISCARD: Price change; irrelevant.] quote: "prices rising by 7p a kilogram (+3.1% year on year) this year."
  - p137 Year-on-year increase in speciality tea spend, 52 weeks ending March 2019 vs 201 = **4.2** percent (2018-03-25..2019-03-24) [DISCARD: Speciality spend change; irrelevant.] quote: "Spending on Speciality Tea is up 4.2% (52 w/e March 2019 vs. 2018)"
  - p138 Year-on-year increase in average price of speciality tea (Kantar) = **2.7** percent (2018-03-25..2019-03-24) [DISCARD: Speciality price change; irrelevant.] quote: "the average price has gone up 2.7%"
  - p139 Year-on-year percentage increase in speciality tea occasions (Kantar) = **10** percent (2018-03-25..2019-03-24) [DISCARD: Speciality occasion change; irrelevant.] quote: "Occasions involving speciality tea were up 10% in the time period, or 100m."
- `https://www.tea.co.uk/assets/uploads/files/news/39ef5-uk-tea-census-report-2022-web.pdf` -> **live_dated** (page date 2022-05-13); points raw/verified 15/11
  - p140 Tea Census poll sample size (UK employed tea drinkers) = **1,000** people polled (2022-03-01..2022-08-31) [DISCARD: Sample size; not a numeric input.] quote: "Independent poll of 1000 UK employed tea drinkers conducted by Perspectus Global; Spring/Summer 2022"
  - p141 Share of respondents drinking most tea at home = **54** % of respondents (2022-03-01..2022-08-31) [DISCARD: Home-drinking share; not convertible to cups.] quote: "Despite tea seemingly being an ideal accompaniment to a day's work, the majority of people (54%) drink most of their tea at home."
  - p142 Share of office workers drinking two cups during working hours = **29** % of office-working respondents (2022-03-01..2022-08-31) [DISCARD: Office cups bin; too narrow and not population-representative.] quote: "Just under a third (29%) drink two cups of tea during their working hours"
  - p143 Share of office workers drinking three cups during working hours = **24** % of office-working respondents (2022-03-01..2022-08-31) [DISCARD: Office cups bin; too narrow.] quote: "24% drink three cups of tea and 6% told us they drink more that five cups a day."
  - p144 Share of office workers drinking more than five cups a day = **6** % of office-working respondents (2022-03-01..2022-08-31) [DISCARD: Office cups bin; too narrow.] quote: "24% drink three cups of tea and 6% told us they drink more that five cups a day."
  - p145 Share of home workers drinking more than five cups during working hours = **14** % of home-working respondents (2022-03-01..2022-08-31) [DISCARD: Home-worker cups bin; too narrow.] quote: "Working from home does seem to lead to more tea drinking as 14% drink more than five cups, and 36% drink three to four cups during the working hours."
  - p146 Share of home workers drinking three to four cups during working hours = **36** % of home-working respondents (2022-03-01..2022-08-31) [DISCARD: Home-worker cups bin; too narrow.] quote: "Working from home does seem to lead to more tea drinking as 14% drink more than five cups, and 36% drink three to four cups during the working hours."
  - p147 Share of respondents drinking black tea several times a day = **40** % of respondents (2022-03-01..2022-08-31) [DISCARD: Frequency descriptor; not a numeric level.] quote: "40% drink black tea with or without milk, several times a day"
  - p148 Share of respondents drinking several cups of green tea a day = **10** % of respondents (2022-03-01..2022-08-31) [DISCARD: Green-tea frequency; not a numeric level.] quote: "10% drink several cups of green tea a day"
  - p149 Share of respondents working in an office (vs home or mix) = **56** % of respondents (2022-03-01..2022-08-31) [DISCARD: Work-location share; irrelevant.] quote: "Just over 56% of those questioned in the Tea Census Poll now work in an office, with the other 44% working from home or a mix of office and home."
  - p150 Share of respondents working from home or a mix = **44** % of respondents (2022-03-01..2022-08-31) [DISCARD: Work-location share; irrelevant.] quote: "Just over 56% of those questioned in the Tea Census Poll now work in an office, with the other 44% working from home or a mix of office and home."
- `https://www.tea.co.uk/assets/uploads/files/news/4ea32-uk-tea-report-2023-3149-for-web-spreads.pdf` -> **live_dated** (page date 2023-05-05); points raw/verified 15/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 14/2
  - p151 Global tea market forecast value by 2025 = **134,400,000,000** USD ($) (2025-01-01..2025-12-31) [DISCARD: Global market forecast; irrelevant to UK cup count.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p152 UK tea export value in 2023 = **121,400,000** USD ($) (2023-01-01..2023-12-31) [DISCARD: Export value; not consumption.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
- dropped by code checks: 38 (scale word 'million' not supported by quote or table header: 4; period_end missing or unparseable: 29; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; number: no number in value_as_written: 3)

### b2 [physical_flow] Grams of tea per cup for UK tea bags

Hypothesis: The physical-flow route (72m kg/year ÷ grams per cup) is the most independent check on the 100m anchor; a defensible 2–3 g/cup range would convert p62/p16 into cups/day and materially narrow the estimate.

Queries issued by the searcher: UK tea bag weight grams per bag PG Tips Tetley; grams of tea per cup UK average tea bag fill weight; UK Tea & Infusions Association 100 million cups a day 2 grams per cup; "tea bag" "2.5g" OR "3g" fill weight UK standard black tea market data

- `https://teas.co.uk/wiki/tea-in-a-big-mug/` -> **live_dated** (page date 2026-10-03); points raw/verified 15/0
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 14/2
  - p153 Global tea market forecast value by 2025 = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of p151.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p154 UK tea export value, 2023 = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: Duplicate of p152.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
- `https://teas.co.uk/wiki/best-400-tea-bags-uk/` -> **live_dated** (page date 2026-10-06); points raw/verified 12/2
  - p155 PG Tips 400-bag box price at 8 August 2026 shop snapshot = **8** GBP per 400-bag box (2026-08-08..2026-08-08) [DISCARD: Retail price snapshot; no cup conversion and not a consumption measure.] quote: "When we checked on 8 August 2026: £8.00, in stock"
  - p156 Tetley 400-bag box price at 8 August 2026 shop snapshot = **11** GBP per 400-bag box (2026-08-08..2026-08-08) [DISCARD: Retail price snapshot; no cup conversion.] quote: "When we checked on 8 August 2026: £11.00, in stock"
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p157 Share of tea drinkers drinking three or more cups a day (2023 Product of the Yea = **35** % of tea drinkers surveyed (2023-01-01..2023-12-31) [DISCARD: Duplicate of p196 (35% three-or-more cups).] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- dropped by code checks: 51 (period_end missing or unparseable: 47; number: unknown scale word 'kg': 2; value_as_written not in quote as a whole number: 2)

### b3 [base_rates] Representative per-drinker cup frequency and drinker share

Hypothesis: The decomposition route (population × drinker share × cups/drinker/day) is sensitive to the drinker share (78% vs 98%) and mean cups; a representative survey with a full frequency distribution would pin both and cross-check the 100m anchor.

Queries issued by the searcher: UK Tea & Infusions Association 100 million cups tea per day statistics; NatCen tea consumption survey UK share of adults drinking tea cups per day; National Diet and Nutrition Survey tea consumption ml per day adults mean percentage consumers; Defra Family Food tea purchases grams per person per week UK

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 15/11
  - p158 UK cups of tea drunk each day (stated by UKTIA CEO) = **100,000,000** cups of tea per day (..) [DISCARD: Duplicate of p54.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p159 UK cups of coffee drunk each day (comparison) = **98,000,000** cups of coffee per day (..) [DISCARD: Coffee comparison; irrelevant to tea cups.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p160 Global cups of tea drunk each day = **5,000,000,000** cups of tea per day (..) [DISCARD: Global tea cups; not UK.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p161 Global cups of coffee drunk each day = **2,000,000,000** cups of coffee per day (..) [DISCARD: Global coffee cups; irrelevant.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p162 Estimated total global tea consumption (International Tea Committee) = **6,209,000,000** kg of tea (..) [DISCARD: Global consumption; not UK.] quote: "Estimated Total Global Consumption 6,209 Million Kg of Tea (Data Source: International Tea Committee)."
  - p163 Assumed average tea per cup used for global conversion = **3** g per cup (..) [keep: ] quote: "Using an average of 3g (per cup), this would equate to over 5 billion cups consumed worldwide every day."
  - p164 Share of 18–24-year-olds having a daily cuppa (UK survey) = **83** % of 18–24-year-olds (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p165 UK adults surveyed in Omnibus survey (Obsurvant) = **4,000** UK adults (2022-12-01..2022-12-31) [DISCARD: Sample size; not a numeric input.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p166 Share of younger adults citing great taste as reason for tea = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Taste reason; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p167 Share of over-25s citing great taste as reason for tea = **85** % of over-25s (2022-12-01..2022-12-31) [DISCARD: Taste reason; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p168 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Relative-drinking claim; not a level.] quote: "31% of younger adults polled saying they drink more tea than their parents"
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/14
  - p169 Share of UK residents who drink tea daily (UKTIA, May) = **98** % of UK residents (..) [DISCARD: Duplicate of p53 (98% daily drinkers).] quote: "the UK Tea & Infusions Association (UKTIA) revealed that 98% of UK residents drink tea daily."
  - p170 Cups of tea drunk every day in the UK (UKTIA/ITC estimate) = **100,000,000** cups per day (..) [DISCARD: Duplicate of p54 (100m cups/day).] quote: ""More than 100 million cups of tea are drunk every day here in the UK,""
  - p171 Annual UK tea consumption in cups (ITC estimate) = **36,000,000,000** cups per year (..) [DISCARD: Duplicate of p55 (36bn cups/year).] quote: "which estimates consumption at 36 billion cups per year."
  - p172 Adults surveyed in March UKTIA survey = **1,010** adults surveyed (..) [DISCARD: Sample size; not a numeric input.] quote: "nearly two-thirds of the 1010 adults surveyed in March start their day with tea."
  - p173 Share of black tea drinkers using tea bags = **84** % of surveyed adults (..) [DISCARD: Duplicate of p52 (tea-bag use share).] quote: ""It's no surprise that 84% pick the option of a tea bag to make their black tea, with 16% opting for loose leaf,""
  - p174 Share of black tea drinkers using loose leaf = **16** % of surveyed adults (..) [DISCARD: Complement of p173/p52; redundant.] quote: "with 16% opting for loose leaf," said Hall."
  - p175 Share of UK residents drinking black tea without milk = **24** % of surveyed adults (..) [DISCARD: Milk preference; irrelevant to cup counts.] quote: "nearly a quarter (24%) said they drink their black tea as it comes, without any milk,"
  - p176 UK tea market value (Statista) = **1,700,000,000** GBP (..) [DISCARD: Market value in GBP; no cup conversion available.] quote: "According to Statista market research, the UK market is valued at £1.7 billion ($2.2 billion)."
  - p177 UK annual tea consumption in kilos (Statista, excl. herbal/RTD/instant) = **72,000,000** kilos per year (..) [DISCARD: Duplicate of p62 (72m kg/year).] quote: "Statista Market Insights estimates UK consumption at 72 million kilos annually, excluding herbal infusions, ready-to-drink, and instant tea."
  - p178 Average UK tea spend per person per week (Statista) = **15** pence per person per week (..) [DISCARD: Spend per person; no cup conversion available.] quote: "According to Statista, UK residents spend an average of 15 pence per person per week on tea."
  - p179 Share of UK fluid intake that is tea (Tea Advisory Panel) = **40** % of fluid intake (..) [DISCARD: Share of fluid intake; not convertible to cups without total fluid volume.] quote: "even today, 40% of the nation's fluid intake will be tea, according to the Tea Advisory Panel (TAP)."
  - p180 UK tea export value, 2023 (ranked 7th) = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: Duplicate of p152 (UK tea export value 2023).] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea."
  - p181 Global tea market estimated value by 2025 (forecast) = **134,400,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of p151 (global market forecast).] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025."
  - p182 Global tea production (FAO, nearing) = **6,700,000** tons (..) [DISCARD: Global production; not UK consumption.] quote: "According to the UN Food and Agriculture Organization (FAO), tea production is nearing 6.7 million tons."
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/15
  - p183 UKTIA estimate of cups of tea consumed daily in the UK = **100,000,000** cups of tea per day (..) [DISCARD: Duplicate of p54.] quote: "The UKTIA estimates over 100 million cups of tea are consumed daily, or 36 billion cups annually."
  - p184 UKTIA estimate of cups of tea consumed annually in the UK = **36,000,000,000** cups of tea per year (..) [DISCARD: Duplicate of p55.] quote: "The UKTIA estimates over 100 million cups of tea are consumed daily, or 36 billion cups annually."
  - p185 Last official UK population estimate = **67,600,000** people (..) [DISCARD: Population figure embedded in a derived per-capita calculation; not needed as a separate input.] quote: "The last official population estimate for the U.K. was 67.6 million, meaning the average Briton drinks 532.5 cups of tea each year."
  - p186 Average cups of tea per Briton per year (derived from UKTIA figures) = **532** cups of tea per person per year (..) [DISCARD: Derived from the 100m/day anchor; circular.] quote: "The last official population estimate for the U.K. was 67.6 million, meaning the average Briton drinks 532.5 cups of tea each year."
  - p187 UK annual tea consumption (World Population Review, UN data) = **100,000** tons of tea per year (..) [keep: ] quote: "The review, which uses data from the United Nations., tells us the U.K. consumes 100,000 tons of tea annually."
  - p188 Lower bound of tea bag weight range = **1.5** grams per tea bag (..) [keep: ] quote: "Tea bags range in weight from around 1.5g to 3g, so this shakes out to somewhere between 33 billion and 66 billion cups of tea."
  - p189 Upper bound of tea bag weight range = **3** grams per tea bag (..) [keep: ] quote: "Tea bags range in weight from around 1.5g to 3g, so this shakes out to somewhere between 33 billion and 66 billion cups of tea."
  - p190 Lower bound of implied cups of tea per year from 100,000 tons = **33,000,000,000** cups of tea per year (..) [DISCARD: Derived bound from p187 and p188; redundant with the mass-flow formula.] quote: "Tea bags range in weight from around 1.5g to 3g, so this shakes out to somewhere between 33 billion and 66 billion cups of tea."
  - p191 Upper bound of implied cups of tea per year from 100,000 tons = **66,000,000,000** cups of tea per year (..) [DISCARD: Derived bound from p187 and p189; redundant with the mass-flow formula.] quote: "Tea bags range in weight from around 1.5g to 3g, so this shakes out to somewhere between 33 billion and 66 billion cups of tea."
  - p192 Popular brand tea bag weight range lower bound = **2** grams per tea bag (..) [keep: ] quote: "Popular brands like Barry's, Yorkshire, and PG Tips weigh-in at 2-3g, while most guides to brewing loose leaf tea advise using a rounded teaspoon (2-3g) of tea leaves per cup."
  - p193 Popular brand tea bag weight range upper bound = **3** grams per tea bag (..) [keep: ] quote: "Popular brands like Barry's, Yorkshire, and PG Tips weigh-in at 2-3g, while most guides to brewing loose leaf tea advise using a rounded teaspoon (2-3g) of tea leaves per cup."
  - p194 Average cups of tea per Briton per year (rounded conclusion) = **500** cups of tea per person per year (..) [DISCARD: Rounded restatement of p186; circular.] quote: "it seems like British people really do drink an average of about 500 cups of tea every year."
  - p195 UK population under 16 = **13,000,000** people (..) [DISCARD: Under-16 population; not used in any executable route.] quote: "There are also roughly 13 million people under 16 in the U.K."
  - p196 Share of tea drinkers drinking three or more cups a day (2023 Product of the Yea = **35** % (2023-01-01..2023-12-31) [DISCARD: Same 35% figure as p157; retained only as shape context, not a numeric input.] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day."
  - p197 Share of Britons drinking five-10 cups a day (2023 Product of the Year survey) = **20** % (2023-01-01..2023-12-31) [DISCARD: Bin share from a small survey; not used numerically.] quote: "while 20% of Britons do their part by drinking five-10 cups a day."
- `https://www.stage.bbc.co.uk/bitesize/articles/zm2txyc` -> **live_dated** (page date 2026-05-21); points raw/verified 0/0
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 2; number: no number in value_as_written: 3)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['tea consumption uk', 'cups of tea', 'uk tea drinking']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p54', 'p55'] Both are the same ITC/UKTIA-derived figure (100m cups/day and 36bn cups/year); 36bn/365 ≈ 98.6m, so they are internally consistent but not independent — one underlying source.
- conflicting: ['p54', 'p77'] ITC/UKTIA ~100m cups/day vs Kantar 18.3bn tea-drinking occasions/year (~50m/day). Different definitions (cups vs occasions; Kantar household panel may exclude out-of-home and multiple cups per occasio
- corroborating: ['p16', 'p19', 'p62'] Physical-flow anchors: 113kt consumption (2015), 1.9 kg/capita (2015), and 72m kg/year (Statista, excl. herbal/RTD/instant). The 72m kg figure is lower than 113kt, consistent with decline and narrower
- corroborating: ['p41', 'p42', 'p43', 'p44'] UKTIA cup-frequency distribution (38% 1–2, 36% 3–4, 15% 5–6, 2% >11) sums to 91%, leaving ~9% for 7–11 and non-drinkers; internally coherent and supports a per-drinker mean of roughly 3–4 cups/day.
- corroborating: ['p34', 'p35', 'p36'] Crave/UKTIA distribution (35% 3–4, 44% 1–2, 20% 5–6) is a similar shape to p41–p44 but with different shares; same underlying survey family, so corroboration is weak (shared source).
- conflicting: ['p33', 'p53'] p33 says >9 in 10 drink at least one cup/day; p53 says 98% drink tea daily. Both are implausibly high vs p117 (78% drink tea) and p41–p44 (9% non-drinkers); likely survey framing/definition difference
- corroborating: ['p97', 'p113'] Historical decline: 23 cups/person/week in 1974 and 68g/person/week in 1974 vs 22g now — consistent with a long-run fall in per-capita tea consumption; supports using a declining trend rather than a f
- corroborating: ['p1', 'p10', 'p45', 'p106'] Duplicate copies of the same 83% 18–24 daily-cuppa statistic across directions; one underlying poll, not independent confirmation.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89'] Defra household beverage purchases series (grams/person/week) — a consistent time series but 'beverages' includes coffee etc., so it is a weak, non-tea-specific proxy.
- corroborating: ['p124', 'p125', 'p126', 'p127', 'p128'] Coffee-shop tea category (£308m, 3.8% of turnover) — out-of-home tea channel evidence; useful only as a component check, not a direct cup count.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p54', 'p158', 'p170', 'p183'] All four are the same UKTIA/ITC 'over 100 million cups/day' claim repeated across outlets; they are one underlying estimate, not independent confirmations.
- corroborating: ['p55', 'p171', 'p184'] Same 36 billion cups/year ITC figure restated; consistent with 100m/day only if a year is treated as 360 days, so it is a rounded restatement rather than an independent measurement.
- corroborating: ['p62', 'p177'] Identical Statista 72 million kg/year figure (excl. herbal, RTD, instant) repeated; one source, not two.
- corroborating: ['p16', 'p19', 'p187'] Physical-volume estimates of UK tea consumption (113k t 2015; 1.9 kg/capita 2015; 100k t UN-based) are broadly consistent and give an independent mass-flow route, though at different vintages and scop
- corroborating: ['p188', 'p189', 'p192', 'p193', 'p163'] Tea-bag/loose-leaf mass per cup ranges (1.5-3 g, popular brands 2-3 g, UKTIA's 3 g conversion) agree on a 2-3 g central band for converting mass to cups.
- conflicting: ['p33', 'p53', 'p169', 'p117'] Drinker-share estimates range from 78% (YouGov 2020) to 98% (UKTIA) to 'more than nine in 10'; the 98% figure is implausibly high for a whole-population share and likely reflects a tea-drinker-skewed 
- conflicting: ['p41', 'p42', 'p43', 'p44', 'p34', 'p35', 'p36'] Two frequency distributions (tea.co.uk and cravemag) differ in bin shares and neither closes to 100% cleanly; both are usable only as rough shape constraints on cups per drinker, not as precise levels
- corroborating: ['p77', 'p132'] Duplicate Kantar 18.3 billion tea-drinking occasions (year to Feb 2019); one panel measurement, likely in-home and one-cup-per-occasion, so it is a lower-bound cross-check rather than a full total.
- corroborating: ['p97', 'p113'] 1974 baseline (23 cups/person/week; 68 g/person/week) is internally consistent at ~3 g/cup and shows the historical high from which consumption has declined.
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89'] Defra household beverage purchase series (grams/person/week) is a consistent time series but covers all beverages, not tea alone, so it cannot be used directly as tea mass.
- corroborating: ['p124', 'p125', 'p126'] Coffee-shop turnover and tea's 3.8% share give an out-of-home tea sales value; converting to cups requires an unobserved price per cup, so this is contextual only.
- corroborating: ['p1', 'p10', 'p45', 'p106', 'p164'] Repeated 83% daily-cuppa figure for 18-24s from the same UKTIA/Omnibus research; one survey, not independent.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Grams of tea per cup (hot brewed tea) | 2.5 | 2..3 | 1.732..3.464 (widened) | g per cup | unused | Tea-bag and loose-leaf mass ranges (p188, p189, p192, p193) and UKTIA's 3 g conversion (p163) bracket 2-3 g; 2.5 g is the central value. | Converting UK tea mass (kg/year) to cups, assuming negligible waste and that bag mass approximates brewed leaf mass. | Evidence that typical UK cups use substantially more or less leaf (e.g., large-scale bag-weight audit outside 2-3 g). |
| a2 | Share of UK population drinking tea on a given day | 0.75 | 0.55..0.9 | 0.4975..0.995 (widened) | fraction | unused | Drinker-share estimates range from 78% (p117) to 98% (p53); the lower end is more plausible for a whole-population daily share, so 0.75 with a wide band. | Decomposing total cups as population x drinker share x cups per drinker. | A representative all-ages survey showing daily drinker share outside 55-90%. |
| a3 | Mean cups per tea drinker per day | 2.2 | 1.5..3.2 | 1.5..3.2 | cups per drinker per day | unused | Frequency distributions (p41-p44, p34-p36) and the 35% three-or-more figure (p157/p196) imply a mean of roughly 2-3 cups among drinkers. | Decomposing total cups as population x drinker share x cups per drinker. | A representative survey giving a mean cups-per-drinker clearly outside 1.5-3.2. |
| a4 | UK population (mid-2025) | 69,000,000 | 68,000,000..70,000,000 | 48,785,244..97,570,487 (widened) | people | unused | No kept point supplies a current population; p185's 67.6m is dated and embedded in a derived calculation. A 68-70m band reflects recent UK growth. | Multiplying by per-person cup rates to get a national total. | An official ONS mid-2025 population estimate outside 68-70m. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p62'] / ['a1'] | [] |  | 0.00 |  | unit of the formula's result: 'kg/cup/day' (kg / cp / d) cannot be converted to 'cup/day' (cp / d). Write the unit the formula actually produces (an annual total gives a per-year result); code convert |
| m2 | formula_mc | n/a | [] / ['a2', 'a3', 'a4'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **n/a** cup/day, 80% interval [n/a, n/a] cup/day, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['uk', 'united kingdom']; measure stems ['consu', 'cup', 'peopl', 'tea']


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

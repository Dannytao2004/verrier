# Evidence ledger: smoke_tea

- Question: How many cups of tea do people in the United Kingdom drink per day?
- as_of: 2026-10-18
- Pinned target: Total number of cups of tea consumed by people in the United Kingdom (England, Scotland, Wales, Northern Ireland) in a single day, counting each cup/teacup/mug serving of tea (hot brewed tea, including herbal/fruit and green tea, but excluding iced tea and ready-to-drink bottled tea unless explicitl | unit cups per day | period 2026-10-18..2026-10-18 | publisher No single official publisher; candidate sources include the UK Tea & Infusions Association (UKTIA), Defra Family Food survey, ONS, Kantar/Nielsen retail data, and trade bodies

## Directions and pages

### d1 [related_series] Trade body / industry analyst

Hypothesis: UKTIA and press frequently cite a headline 'X million cups of tea a day' figure for the UK. If such a published estimate exists, it directly anchors the target (possibly the single best evidence). Direction: target ≈ published daily cups figure, adjusted for definitional scope (herbal inclusion, out-of-home).

Queries issued by the searcher: UK Tea and Infusions Association cups of tea per day UK; how many cups of tea drunk daily Britain million; tea consumption UK per day statistic UKTIA 100 million cups; site:tea.co.uk 2026 survey cups tea day UK adults 4.8; UKTIA 2026 tea survey average cups per day August 2026; "4.8 cups" tea UK 2026 UKTIA

- `https://www.tea.co.uk/assets/uploads/files/news/39ef5-uk-tea-census-report-2022-web.pdf` -> **live_dated** (page date 2022-05-13); points raw/verified 15/0
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 13/6
  - p1 Share of 18–24-year-olds having a daily cuppa (UK survey) = **83** % of 18–24-year-olds (2022-12-01..2022-12-31) [DISCARD: Duplicate of p7, p42, p53, p97, p131; same underlying survey statistic.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p2 UK adults surveyed in Omnibus survey (sample size) = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p8, p43, p54, p102, p136; sample size only, not a consumption rate.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p3 Share of younger adults citing great taste as reason for drinking tea = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p9, p44, p55, p98, p132; reason for drinking tea, not a consumption quantity.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p4 Share of over-25s citing great taste as reason for drinking tea = **85** % of over-25s (2022-12-01..2022-12-31) [DISCARD: Duplicate of p10, p45, p56, p99, p133; reason for drinking tea, not a consumption quantity.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p5 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Duplicate of p11, p46, p57, p100, p134; attitudinal, not a consumption quantity.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p6 UK adults polled in Perspectus Global survey (sample size) = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [DISCARD: Duplicate of p12, p48, p58, p103, p137; sample size only.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/0
- `https://www.manchestereveningnews.co.uk/news/cost-of-living/tea-experts-guide-making-perfect-29738364` -> **live_dated** (page date 2024-08-14); points raw/verified 10/0
- dropped by code checks: 47 (period_end missing or unparseable: 42; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 3)

### d2 [related_series] National statistics / household survey analyst

Hypothesis: Total cups/day = UK population × average cups per person per day. Per-capita tea consumption can be derived from Defra Family Food / ONS household consumption data (tea purchases or intake) converted to cups via average cup size. Direction: target scales linearly with population and per-capita rate.

Queries issued by the searcher: UK Tea & Infusions Association cups of tea per day UK 100 million; Defra Family Food tea consumption per person kg per year UK; Family Food tea purchases grams per person per week UK 2023 2024 "tea"; ONS UK population mid-2026 projection 69 million

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day?trk=article-ssr-frontend-pulse_little-text` -> **live_dated** (page date 2026-01-01); points raw/verified 14/6
  - p7 Share of 18–24-year-olds having a daily cuppa (UK survey) = **83** % of 18–24-year-olds surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1, p42, p53, p97, p131; same survey statistic.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p8 UK adults surveyed in omnibus research = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2, p43, p54, p102, p136.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p9 Share of younger adults citing great taste as reason for drinking tea = **80** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3, p44, p55, p98, p132.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p10 Share of over-25s citing great taste as reason for drinking tea = **85** % of over-25s surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4, p45, p56, p99, p133.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p11 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Duplicate of p5, p46, p57, p100, p134.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p12 UK adults polled in second survey (Perspectus Global) = **1,000** UK adults polled (2023-03-01..2023-05-31) [DISCARD: Duplicate of p6, p48, p58, p103, p137.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration and boosting mood"
- `https://www.gov.uk/government/statistical-data-sets/family-food-datasets` -> **live_dated** (page date 2026-09-17); points raw/verified 0/0
- `https://diamondgeezer.blogspot.com/2024/12/were-drinking-less-tea.html` -> **live_dated** (page date 2024-12-01); points raw/verified 15/9
  - p13 UK household average tea quantity purchased per person per week (2023) = **19** grams per person per week (2023-01-01..2023-12-31) [keep: ] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p14 UK household average tea consumed outside home per person per week (2023) = **12** millilitres per person per week (2023-01-01..2023-12-31) [DISCARD: Out-of-home tea in millilitres per week is a tiny, ambiguous quantity (12 ml) that cannot be reliably converted to cups;] quote: "Tea (out of home) n/a n/a n/a 44ml 30ml 12ml"
  - p15 UK household average tea quantity purchased per person per week (2014) = **25** grams per person per week (2014-01-01..2014-12-31) [DISCARD: Historical tea purchase data (2014) superseded by more recent p13/p127; not needed for current estimate.] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p16 UK household average tea quantity purchased per person per week (2004) = **31** grams per person per week (2004-01-01..2004-12-31) [DISCARD: Historical tea purchase data (2004) superseded by more recent p13/p127.] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p17 UK household average tea quantity purchased per person per week (1994) = **41** grams per person per week (1994-01-01..1994-12-31) [DISCARD: Historical tea purchase data (1994) superseded by more recent p13/p127.] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p18 UK household average tea quantity purchased per person per week (1984) = **55** grams per person per week (1984-01-01..1984-12-31) [DISCARD: Historical tea purchase data (1984) superseded by more recent p13/p127.] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p19 UK household average tea quantity purchased per person per week (1974) = **68** grams per person per week (1974-01-01..1974-12-31) [DISCARD: Historical tea purchase data (1974) superseded by more recent p13/p127.] quote: "Tea (at home) 68g 55g 41g 31g 25g 19g"
  - p20 UK household average tea consumed outside home per person per week (2014) = **30** millilitres per person per week (2014-01-01..2014-12-31) [DISCARD: Historical out-of-home tea consumption (2014) superseded by more recent p14.] quote: "Tea (out of home) n/a n/a n/a 44ml 30ml 12ml"
  - p21 UK household average tea consumed outside home per person per week (2004) = **44** millilitres per person per week (2004-01-01..2004-12-31) [DISCARD: Historical out-of-home tea consumption (2004) superseded by more recent p14.] quote: "Tea (out of home) n/a n/a n/a 44ml 30ml 12ml"
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p22 Share of surveyed tea drinkers drinking three or more cups a day (2023 Product o = **35** % of tea drinkers surveyed (2023-01-01..2023-12-31) [keep: ] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day."
- dropped by code checks: 28 (period_end missing or unparseable: 23; value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 1; number: more than one number in value_as_written: 1; scale word 'billion' not supported by quote or table header: 2)

### d3 [physical_flow] Supply-chain / import analyst

Hypothesis: Cups/day ≈ (UK tea supply available for domestic consumption per day) ÷ (grams of tea per cup). Supply = imports + domestic production − exports ± stock change, from HMRC trade data and FAO/ITC. Direction: target proportional to net tea availability and inversely proportional to tea-per-cup.

Queries issued by the searcher: UK tea imports tonnes per year HMRC tea available for consumption; grams of tea per cup tea bag weight 2-3 grams UKTIA; UK tea imports 2023 tonnes HMRC trade data tea exports volume; UN Comtrade United Kingdom tea 0902 imports tonnes 2023 2024

- `https://vietnamnews.vn/economy/1594804/plenty-of-room-for-vietnamese-tea-exports-to-the-uk.html` -> **live_dated** (page date 2023-10-06); points raw/verified 15/10
  - p23 UK total tea imports, volume, first half 2023 = **53,000** tonnes (2023-01-01..2023-06-30) [keep: ] quote: "the UK spent $160 million on importing 53,000 tonnes of tea, marking a 9.7 per cent reduction in volume"
  - p24 UK total tea imports, value, first half 2023 = **160,000,000** US dollars (2023-01-01..2023-06-30) [DISCARD: Import value, not volume; not needed for physical-flow estimate.] quote: "the UK spent $160 million on importing 53,000 tonnes of tea"
  - p25 UK tea import volume change year-on-year, first half 2023 = **9.7** per cent (2023-01-01..2023-06-30) [DISCARD: Year-on-year change in imports, not a level; not needed.] quote: "marking a 9.7 per cent reduction in volume and a 9.4 per cent drop in value from the corresponding period the previous year"
  - p26 UK tea import value change year-on-year, first half 2023 = **9.4** per cent (2023-01-01..2023-06-30) [DISCARD: Year-on-year change in import value, not a level; not needed.] quote: "a 9.4 per cent drop in value from the corresponding period the previous year"
  - p27 Kenya share of UK total tea imports, first half 2023 = **56.8** per cent (2023-01-01..2023-06-30) [DISCARD: Kenya share of imports, not needed for total volume estimate.] quote: "Kenya emerged as the predominant tea provider to the UK, representing 56.8 per cent of the market's total imports."
  - p28 Kenya tea exports to UK, volume, first half 2023 = **30,100** tonnes (2023-01-01..2023-06-30) [DISCARD: Kenya-to-UK bilateral export line; subsumed in total imports p208/p23 and not needed separately.] quote: "Kenya dispatched 30,100 tonnes to the market, garnering $70.9 million"
  - p29 Kenya tea exports to UK, value, first half 2023 = **70,900,000** US dollars (2023-01-01..2023-06-30) [DISCARD: Kenya export value, not needed.] quote: "Kenya dispatched 30,100 tonnes to the market, garnering $70.9 million"
  - p30 Kenya tea export volume change year-on-year to UK, first half 2023 = **3.2** per cent (2023-01-01..2023-06-30) [DISCARD: Year-on-year change, not a level.] quote: "an increase of 3.2 per cent in volume and 1.6 per cent in value year-on-year"
  - p31 Kenya tea export value change year-on-year to UK, first half 2023 = **1.6** per cent (2023-01-01..2023-06-30) [DISCARD: Year-on-year change, not a level.] quote: "an increase of 3.2 per cent in volume and 1.6 per cent in value year-on-year"
  - p32 Average price of tea imported from Vietnam to UK, first half 2023 = **4.928** US dollars per tonne (2023-01-01..2023-06-30) [DISCARD: Implausible unit (US$ per tonne) and not needed.] quote: "The average price of tea imported from Việt Nam stood at US$4.928 per tonne, a decrease of 0.4 per cent"
- `https://wits.worldbank.org/trade/comtrade/en/country/GBR/year/2023/tradeflow/Imports/partner/ALL/product/090220` -> **live_dated** (page date 2023-01-01); points raw/verified 12/0
- `https://www.riunit.com/wp-content/uploads/2018/06/Content-Page-for-Tea-Report-Final-2.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/1
  - p33 Share of surveyed tea drinkers drinking three or more cups a day (2023 Product o = **35** percent of tea drinkers (2023-01-01..2023-12-31) [DISCARD: Duplicate of p22; same survey statistic.] quote: "just over a third (35%) of tea drinkers who responded to a 2023 survey from Product of the Year drink three or more cups a day"
- dropped by code checks: 31 (period_end missing or unparseable: 25; scale word 'thousand' not supported by quote or table header: 6)

### d4 [capacity_consumption] Retail / FMCG analyst

Hypothesis: Cups/day ≈ (retail tea sales volume, kg/year ÷ 365) ÷ g-per-cup, plus out-of-home servings. Retail sales volume (Kantar, Nielsen, IRI) times share consumed at home vs out-of-home gives a bottom-up flow. Direction: target proportional to retail volume and inversely to g/cup.

Queries issued by the searcher: UK tea market volume tonnes Kantar retail tea sales; UK Tea & Infusions Association tea consumption cups per day statistics; out of home tea consumption share UK percent foodservice hot drinks Kantar tea 15%; UK retail tea market volume million kg 2024 Kantar tea category report

- `https://www-euromonitor-com.ezproxy.haaga-helia.fi/globalassets/samples/pdf/hot-drinks/coffee/coffee-in-the-uk-sample.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.beveragestandardsassociation.co.uk/wp-content/uploads/2020/01/Tetley_Tea_Report2018.pdf` -> **live_dated** (page date 2020-01-01); points raw/verified 15/3
  - p34 Average cups of tea per day drunk out of home by average tea drinker on a weekda = **2** cups per day (out of home, weekday) (2017-01-01..2017-12-31) [keep: ] quote: "Weekday 2 Cups a day OOH"
  - p35 Average cups of tea per day drunk out of home by average tea drinker on a weeken = **1** cups per day (out of home, weekend) (2017-01-01..2017-12-31) [keep: ] quote: "Weekend 1 Cup a day OOH"
  - p36 Average tea cost per cup out of home, 2017 = **1.77** GBP per cup (2017-01-01..2017-12-31) [DISCARD: Cost per cup, not a consumption quantity.] quote: "£1.77 2017 AVERAGE Tea cost per cup"
- `https://www.thegrocer.co.uk/consumer-trends/cuppa-in-decline-as-brits-drink-870-million-fewer-cups-of-tea/571087.article` -> **live_dated** (page date 2018-08-31); points raw/verified 10/5
  - p37 UK retail tea volume decline, Kantar Worldpanel 52 weeks ending 20 May 2018 = **2,600,000** kilograms of tea (2017-05-21..2018-05-20) [DISCARD: Volume decline, not a level; not needed.] quote: "The nation bought 2.6 million fewer kilograms of tea, shows Kantar Worldpanel data [52 w/e 20 May 2018]"
  - p38 Implied fewer cups of tea from volume decline, 52 weeks ending 20 May 2018 = **866,700,000** cups of tea (2017-05-21..2018-05-20) [DISCARD: Implied fewer cups from decline, not a level; not needed.] quote: "this equates to roughly 866.7 million fewer cups of tea over that period."
  - p39 UK tea market value growth rate, 52 weeks ending 20 May 2018 = **0.6** percent (2017-05-21..2018-05-20) [DISCARD: Market value growth, not a consumption quantity.] quote: "Kantar Worldpanel data shows the value of tea has risen by 0.6% to £669.2m over the past year."
  - p40 Yorkshire Tea brand value growth, Nielsen 52 weeks ending 30 December 2017 = **7.9** percent (2016-12-31..2017-12-30) [DISCARD: Brand value growth, not a consumption quantity.] quote: "Yorkshire Tea, which secured the highest value growth of any tea brand in The Grocer's Britain's Biggest Brands (up 7.9% to £88m, Nielsen 52 w/e 30 December 2017)"
  - p41 Free-from market value growth, Kantar Worldpanel 52 weeks ending 26 March 2018 = **37.5** percent (2017-03-27..2018-03-26) [DISCARD: Free-from market growth, irrelevant.] quote: "in a bid to grab a slice of the growing free-from market, whose value is up 37.5% [Kantar Worldpanel 52 w/e 26 March 2018]."
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 14/7
  - p42 Share of UK 18–24-year-olds having a daily cuppa (survey) = **83** % of surveyed UK adults aged 18–24 (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1, p7, p53, p97, p131.] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p43 UK adults surveyed in omnibus survey (sample size) = **4,000** UK adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2, p8, p54, p102, p136.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p44 Share of 18–24-year-olds citing great taste as reason for drinking tea = **80** % of surveyed younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3, p9, p55, p98, p132.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p45 Share of over-25s citing great taste as reason for drinking tea = **85** % of surveyed over-25s (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4, p10, p56, p99, p133.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p46 Share of younger adults saying they drink more tea than their parents = **31** % of surveyed younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p5, p11, p57, p100, p134.] quote: "31% of younger adults polled saying they drink more tea than their parents"
  - p47 Share of young adults brewing a cuppa immediately on waking = **10** proportion of surveyed young adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p101, p135; attitudinal, not a consumption quantity.] quote: "Seven out of 10 young adults brew up a cuppa as soon as they get out of bed."
  - p48 UK adults polled in second survey (sample size) = **1,000** UK adults (2023-03-01..2023-05-31) [DISCARD: Duplicate of p6, p12, p58, p103, p137.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published"
- dropped by code checks: 24 (period_end missing or unparseable: 16; value_as_written not in quote as a whole number: 1; scale word 'million' not supported by quote or table header: 4; scale word 'billion' not supported by quote or table header: 2; number: no number in value_as_written: 1)

### d5 [base_rates] Survey / behavioural analyst

Hypothesis: Cups/day = population × share who drink tea × average cups per drinker per day. Base rates: share of UK adults who drink tea regularly (~70-80% commonly cited) and cups per drinker per day (~2-4). Direction: target is product of these base rates and population.

Queries issued by the searcher: percentage of Britons who drink tea survey cups per day UK; YouGov tea drinking habits UK survey how many cups a day; UK Tea & Infusions Association "100 million cups" tea a day UK statistics cups per day; UKTIA Tea Census 2025 survey percentage drink tea daily cups per day

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day?trk=article-ssr-frontend-pulse_little-text` -> **live_dated** (page date 2026-01-01); points raw/verified 14/13
  - p49 UK cups of tea drunk each day (UKTIA stated figure) = **100,000,000** cups of tea per day (..) [keep: ] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p50 Global cups of tea drunk each day (UKTIA stated figure) = **5,000,000,000** cups of tea per day (..) [DISCARD: Global cups, not UK-specific.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p51 Global cups of coffee drunk each day (comparison) = **2,000,000,000** cups of coffee per day (..) [DISCARD: Global coffee cups, not UK tea.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p52 UK cups of coffee drunk each day (comparison) = **98,000,000** cups of coffee per day (..) [DISCARD: UK coffee cups, not tea.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p53 Share of UK 18-24-year-olds having a daily cuppa (survey, Dec 2022) = **83** % of surveyed UK adults aged 18-24 (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1, p7, p42, p97, p131.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p54 Sample size of UK adult survey on daily tea drinking = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2, p8, p43, p102, p136.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p55 Share of younger adults citing great taste as main reason for tea = **80** % of surveyed younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3, p9, p44, p98, p132.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p56 Share of over-25s citing great taste as main reason for tea = **85** % of surveyed over-25s (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4, p10, p45, p99, p133.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p57 Share of younger adults saying they drink more tea than their parents = **31** % of surveyed younger adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p5, p11, p46, p100, p134.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p58 Sample size of second UK adult poll (Perspectus Global, Spring 2023) = **1,000** UK adults surveyed (2023-03-20..2023-06-20) [DISCARD: Duplicate of p6, p12, p48, p103, p137.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
  - p59 Estimated total global tea consumption = **6,209,000,000** kg of tea (..) [DISCARD: Global tea consumption, not UK-specific.] quote: "Estimated Total Global Consumption 6,209 Million Kg of Tea (Data Source: International Tea Committee)."
  - p60 Assumed average tea weight per cup used for global cup conversion = **3** grams per cup (..) [keep: ] quote: "Using an average of 3g (per cup), this would equate to over 5 billion cups consumed worldwide every day."
  - p61 Global cups of tea drunk each day (footnote restatement) = **5,000,000,000** cups of tea per day (..) [DISCARD: Duplicate of p50; global cups.] quote: "Using an average of 3g (per cup), this would equate to over 5 billion cups consumed worldwide every day."
- `https://yougov.com/en-gb/articles/41661-part-five-drinking-habits-and-preferences` -> **live_dated** (page date 2022-04-20); points raw/verified 10/10
  - p62 Share of Britons who drink a cup of tea at least once a week = **74** % of Britons (..) [keep: ] quote: "Three quarters of Britons (74%) drink a cup of tea at least once a week, the study finds."
  - p63 Share of Britons who have more than 20 cups of tea over the course of the week = **17** % of Britons (..) [DISCARD: Share drinking >20 cups/week, not a mean; not directly usable.] quote: "This includes 17% who say they have more than 20 cups over the course of the week."
  - p64 Share of Britons who don't drink tea at all = **25** % of Britons (..) [keep: ] quote: "A quarter of Britons (25%) don't drink tea at all."
  - p65 Share of 16-24-year-olds who don't drink tea at all = **39** % of 16-24-year-olds (..) [DISCARD: Share of 16-24 non-drinkers, not a mean; not directly usable.] quote: "This goes up to one in four (39%) among 16-24-year-olds."
  - p66 Share of those aged 60+ who drink 20 cups or more of tea a week = **24** % of those aged 60+ (..) [DISCARD: Share of 60+ drinking 20+ cups/week, not a mean.] quote: "20 cups or more - a week (24% of those aged 60+ vs 6% of those aged 16-24)."
  - p67 Share of those aged 16-24 who drink 20 cups or more of tea a week = **6** % of those aged 16-24 (..) [DISCARD: Share of 16-24 drinking 20+ cups/week, not a mean.] quote: "20 cups or more - a week (24% of those aged 60+ vs 6% of those aged 16-24)."
  - p68 Share of tea-drinking Britons who don't take any sugar with tea = **74** % of tea-drinking Britons (..) [DISCARD: Sugar preference, not a consumption quantity.] quote: "Three-quarters of tea-drinking Britons (74%) don't take any sugar with it, with this applying more to women (78%) than men (69%)."
  - p69 Share of Britons who drink coffee at least once a week = **70** % of Britons (..) [DISCARD: Coffee consumption, not tea.] quote: "Seven in ten Britons (70%) drink coffee at least once a week, with one in eight (12%) having more than 20 cups a week."
  - p70 Share of Britons who don't drink coffee = **29** % of Britons (..) [DISCARD: Coffee non-drinkers, not tea.] quote: "One in three Britons (29%) don't drink coffee."
  - p71 Share of Britons who don't drink milk = **50** % of Britons (..) [DISCARD: Milk/fizzy drinks, irrelevant.] quote: "Results also show that half of Britons don't drink milk (50%) and 44% don't typically drink fizzy drinks or fruit juice."
- `https://cravemag.co.uk/6-in-10-brits-still-rely-on-tea-to-stay-calm-new-study-finds/` -> **live_dated** (page date 2025-12-11); points raw/verified 11/11
  - p72 Share of UK adults polled who drink tea to calm down (UKTIA survey of over 1,000 = **60** % of adults surveyed (..) [DISCARD: Reason for drinking tea, not a consumption quantity.] quote: "nearly two thirds (60%) polled in our real-world study of over 1,000 adults1 saying they drink tea to get them to calm down"
  - p73 Share of UK adults aged 25-34 who agree they drink tea to calm down = **83** % of adults aged 25-34 surveyed (..) [DISCARD: Reason for drinking tea, not a consumption quantity.] quote: "twice as many younger adults (25-34 years category; 83%) agreed with this statement"
  - p74 Share of UK adults aged 65+ who agree they drink tea to calm down = **38** % of adults aged 65+ surveyed (..) [DISCARD: Reason for drinking tea, not a consumption quantity.] quote: "compared with the older generation (65+ years category; 38%)"
  - p75 Share of UK adults who drink at least one cup of tea a day (UKTIA survey) = **10** % of adults surveyed (stated as more than nine in 10) (..) [DISCARD: Parsed value (10%) contradicts its own quote ('more than nine in 10'); unusable as a share.] quote: "which shows that more than nine in 10 people drink at least one cup of tea a day"
  - p76 Share of UK adults drinking the recommended three to four cups of tea a day = **35** % of adults surveyed (..) [keep: ] quote: "Over a third (35%) drink the recommended three to four cups"
  - p77 Share of UK adults drinking one or two cups of tea a day = **44** % of adults surveyed (..) [keep: ] quote: "while four in 10 (44%) drink one or two a day"
  - p78 Share of UK adults drinking five to six cups of tea a day = **20** % of adults surveyed (..) [keep: ] quote: "and a thirsty one in five (20%) drink five to six cups a day"
  - p79 Share of Brits who brew tea for thinking time (UKTIA survey) = **64** % of Brits surveyed (..) [DISCARD: Attitudinal, not a consumption quantity.] quote: "nearly two thirds (64%) of Brits like to brew a tea to give them some thinking time"
  - p80 Share of Brits surveyed choosing regular tea as their only hot drink = **66** % of Brits surveyed (..) [DISCARD: Preference, not a consumption quantity.] quote: "the top answer (66%) was a regular cup of tea, whatever their age"
  - p81 Share of Brits surveyed agreeing a cuppa gives comfort = **59** % of Brits surveyed (..) [DISCARD: Attitudinal, not a consumption quantity.] quote: "nearly six in 10 (59%) agreed that having a cuppa gives people comfort"
  - p82 Number of adults polled in UKTIA real-world study = **1,000** adults surveyed (..) [DISCARD: Sample size only.] quote: "our real-world study of over 1,000 adults1"
- `https://www.aldipresscentre.co.uk/product-news/tea-loving-brits-slurp-a-staggering-127-million-cuppas-a-day-but-nearly-a-quarter-are-making-it-all-wro` -> **live_dated** (page date 2025-07-03); points raw/verified 15/14
  - p83 UK adults preferring tea to coffee (share of UK adult population) = **55** % of UK adults (..) [DISCARD: Preference share, not a consumption quantity.] quote: "55% people reported preferring tea to coffee"
  - p84 UK adult population used in Aldi calculation = **31,758,667** people (UK adults) (2025-01-01..2025-12-31) [DISCARD: Adult population used in Aldi calculation; p111/p119 provide total population, and adult share is not needed.] quote: "55% of the UK adult population = 31,758,667"
  - p85 Average cups of tea per day per person (UK, Aldi calculation input) = **4** cups per day (..) [keep: ] quote: "Multiply by average number of cups a day (4) = 127,034,668"
  - p86 Total cups of tea consumed per day in UK (Aldi calculated estimate) = **127,000,000** cups per day (..) [keep: ] quote: "TEA-LOVING BRITS SLURP A STAGGERING 127 MILLION CUPPAS A DAY"
  - p87 Share of nation preferring a brew over coffee = **55** % of respondents (..) [DISCARD: Preference share, not a consumption quantity.] quote: "over half of the nation (55%) saying coffee just isn't their cup of tea"
  - p88 Share drinking an average of four cups a day = **72** % of respondents (..) [keep: ] quote: "nearly three quarters (72%) drink an average of four cups a day"
  - p89 Average cups per Brit per year = **1,460** cups per year (..) [keep: ] quote: "the average Brit consuming a staggering 1,460 cups a year"
  - p90 Share giving exact instructions when someone makes them tea = **78** % of respondents (..) [DISCARD: Attitudinal, not a consumption quantity.] quote: "78% so passionate about a good brew that they give exact instructions"
  - p91 Share making tea wrong by putting milk in first = **22** % of respondents (..) [DISCARD: Attitudinal, not a consumption quantity.] quote: "almost a quarter (22%) are making their tea wrong by putting the milk in first"
  - p92 Share choosing English Breakfast as go-to brew = **67** % of respondents (..) [DISCARD: Preference share, not a consumption quantity.] quote: "English Breakfast (67%) is the go-to brew"
  - p93 Survey sample size (Brits polled) = **2,000** respondents (2025-06-01..2025-06-30) [DISCARD: Sample size only.] quote: "This research of 2,000 Brits was commissioned by Aldi and conducted by Perspectus Global in June 2025."
  - p94 Share preferring no sugar in tea = **38** % of tea drinkers (..) [DISCARD: Sugar preference, not a consumption quantity.] quote: "two in five (38%) preferring no sugar at all"
  - p95 Share taking two sugars in tea = **22** % of tea drinkers (..) [DISCARD: Sugar preference, not a consumption quantity.] quote: "almost a quarter (22%) take two"
  - p96 Share having a specific mug they always use = **40** % of respondents (..) [DISCARD: Mug preference, not a consumption quantity.] quote: "(40%) having a specific mug that they always use"
- dropped by code checks: 2 (value_as_written not in quote as a whole number: 1; number: no number in value_as_written: 1)

### d6 [own_history] Time-series analyst

Hypothesis: If earlier published estimates of UK cups/day exist (e.g., '165 million cups a day' widely cited), the target for 2026 can be updated by trend in per-capita consumption (declining) and population growth. Direction: target ≈ historical daily figure × (per-capita trend) × (population growth).

Queries issued by the searcher: 165 million cups of tea a day UK Tea and Infusions Association; UK tea consumption decline per capita trend cups per day; "100 million cups" tea day UK 2023 UKTIA decline from 165 million; Defra Family Food tea consumption grams per person per week 2022 UK

- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 15/7
  - p97 Share of UK 18-24-year-olds having a daily cuppa = **83** % of UK adults aged 18-24 (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1, p7, p42, p53, p131.] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p98 Share of UK 18-24-year-olds citing great taste as main reason = **80** % of UK adults aged 18-24 (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3, p9, p44, p55, p132.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p99 Share of UK over-25s citing great taste as main reason = **85** % of UK adults aged over 25 (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4, p10, p45, p56, p133.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p100 Share of UK younger adults saying they drink more tea than their parents = **31** % of UK younger adults polled (2022-12-01..2022-12-31) [DISCARD: Duplicate of p5, p11, p46, p57, p134.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p101 Share of UK young adults brewing a cuppa immediately on waking = **10** proportion of UK young adults (2022-12-01..2022-12-31) [DISCARD: Duplicate of p47, p135; attitudinal.] quote: "Seven out of 10 young adults brew up a cuppa as soon as they get out of bed."
  - p102 Sample size of UK omnibus survey on tea habits = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2, p8, p43, p54, p136.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p103 Sample size of second UK poll on tea attitudes = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [DISCARD: Duplicate of p6, p12, p48, p58, p137.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `http://www.tea.co.uk/tea-faqs` -> **live_dated** (page date 2026-01-01); points raw/verified 15/3
  - p104 China tea production (2015) = **2,230,000** tonnes (2015-01-01..2015-12-31) [DISCARD: Global tea production, not UK consumption.] quote: "A: China with 2,230,000 tonnes, India is second with 1,191,100 tonnes, Kenya third with 399,210 tonnes (2015 production)."
  - p105 India tea production (2015) = **1,191,100** tonnes (2015-01-01..2015-12-31) [DISCARD: Global tea production, not UK consumption.] quote: "A: China with 2,230,000 tonnes, India is second with 1,191,100 tonnes, Kenya third with 399,210 tonnes (2015 production)."
  - p106 Kenya tea production (2015) = **399,210** tonnes (2015-01-01..2015-12-31) [DISCARD: Global tea production, not UK consumption.] quote: "A: China with 2,230,000 tonnes, India is second with 1,191,100 tonnes, Kenya third with 399,210 tonnes (2015 production)."
- `https://fortune.com/europe/2024/07/03/how-young-brits-are-reigniting-love-for-the-classic-cuppa-amidst-a-crisis-of-relevance/` -> **live_dated** (page date 2024-07-03); points raw/verified 15/4
  - p107 Yorkshire Tea 2023 volume growth (tea bags sold) = **12** % (2023-01-01..2023-12-31) [DISCARD: Brand volume growth, not a level.] quote: "Yorkshire Tea is certainly unusual in having enjoyed recent growth in both value (revenue) and volume (the number of tea bags sold), at 21% and 12%, respectively, in 2023."
  - p108 Yorkshire Tea 2023 value (revenue) growth = **21** % (2023-01-01..2023-12-31) [DISCARD: Brand value growth, not a level.] quote: "Yorkshire Tea is certainly unusual in having enjoyed recent growth in both value (revenue) and volume (the number of tea bags sold), at 21% and 12%, respectively, in 2023."
  - p109 Global at-home tea market value 2024 (Statista) = **127,000,000,000** US dollars (2024-01-01..2024-12-31) [DISCARD: Global market value, not UK consumption.] quote: "the global at-home tea market-worth $127 billion in 2024, according to Statista-is growing, at a compound annual growth rate of 6%."
  - p110 Kallo Foods (Clipper Teas) turnover growth 2023 = **8** % (2023-01-01..2023-12-31) [DISCARD: Company turnover growth, not a consumption quantity.] quote: "Kallo Foods, which owns Clipper Teas, jumped 8% to £121.7 million ($155.5 million) in 2023"
- `https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates` -> **live_dated** (page date 2024-04-09); points raw/verified 14/14
  - p111 Estimated total UK population, mid-2025 = **69,500,000** people (2025-01-01..2025-06-30) [keep: ] quote: "The population of the UK continued to grow in the year to mid-2025, reaching an estimated 69.5 million people."
  - p112 Annual increase in UK population, year to mid-2025 = **228,000** people (2024-07-01..2025-06-30) [DISCARD: Population change, not a level.] quote: "The size of the population is estimated to have increased by 228,000 (0.3%) from mid-2024, the lowest rate of increase since mid-2020."
  - p113 Annual UK population growth rate, year to mid-2025 = **0.3** % (2024-07-01..2025-06-30) [DISCARD: Population growth rate, not a level.] quote: "The size of the population is estimated to have increased by 228,000 (0.3%) from mid-2024, the lowest rate of increase since mid-2020."
  - p114 Annual population growth rate for England, year to mid-2025 = **0.4** % (2024-07-01..2025-06-30) [DISCARD: Regional growth rate, not a level.] quote: "There was an increase in population for England of 0.4%, with Scotland and Northern Ireland having very small population growth (less than 0.1%)."
  - p115 Annual population growth rate for Wales, year to mid-2025 (decrease) = **0.1** % (2024-07-01..2025-06-30) [DISCARD: Regional growth rate, not a level.] quote: "Wales had a small decrease in population (negative 0.1%)."
  - p116 Estimated total population of England and Wales, mid-2025 = **62,000,000** people (2025-01-01..2025-06-30) [DISCARD: England and Wales population, not UK total; p111/p119 provide UK total.] quote: "The population of England and Wales continued to grow in the year to mid-2025, reaching an estimated 62.0 million people."
  - p117 Annual increase in population of England and Wales, year to mid-2025 = **224,900** people (2024-07-01..2025-06-30) [DISCARD: Population change, not a level.] quote: "The size of the population is estimated to have increased by 224,900 (0.4%) from mid-2024, the lowest rate of increase since mid-2020."
  - p118 Annual population growth rate for England and Wales, year to mid-2025 = **0.4** % (2024-07-01..2025-06-30) [DISCARD: Population growth rate, not a level.] quote: "The size of the population is estimated to have increased by 224,900 (0.4%) from mid-2024, the lowest rate of increase since mid-2020."
  - p119 UK population time series value, 2025 = **69,483,900** people (2025-01-01..2025-12-31) [keep: ] quote: "69,483,900 2025"
  - p120 England population time series value, 2025 = **67,555,500** people (2025-01-01..2025-12-31) [DISCARD: England population only, not UK total.] quote: "67,555,500 2025"
  - p121 England and Wales population time series value, 2025 = **58,834,800** people (2025-01-01..2025-12-31) [DISCARD: England and Wales population only, not UK total.] quote: "58,834,800 2025"
  - p122 Scotland population time series value, 2025 = **3,175,200** people (2025-01-01..2025-12-31) [DISCARD: Scotland population only, not UK total.] quote: "3,175,200 2025"
  - p123 Wales population time series value, 2025 = **5,545,500** people (2025-01-01..2025-12-31) [DISCARD: Wales population only, not UK total.] quote: "5,545,500 2025"
  - p124 Northern Ireland population time series value, 2025 = **1,928,400** people (2025-01-01..2025-12-31) [DISCARD: Northern Ireland population only, not UK total.] quote: "1,928,400 2025"
- dropped by code checks: 31 (period_end missing or unparseable: 28; number: more than one number in value_as_written: 1; number: no number in value_as_written: 2)

### d7 [shocks] Market/behaviour analyst

Hypothesis: Recent price inflation, cost-of-living pressure, and shifts to coffee/other drinks may have reduced tea frequency; conversely, at-home consumption may rise. Direction: adjust base per-capita rate for recent consumption trend and any documented change in tea drinking frequency.

Queries issued by the searcher: UK tea consumption trend 2024 2025 decline cups per day; UK Tea and Infusions Association tea consumption statistics cups per day; Defra Family Food 2023 tea purchases grams per person per week; UKTIA survey 2026 average cups of tea per day UK adults

- `https://www.bbc.com/news/articles/c4gpll9l535o` -> **live_dated** (page date 2024-12-08); points raw/verified 10/4
  - p125 Average weekly tea purchased per person in 1974 (government figures) = **68** grams per person per week (1974-01-01..1974-12-31) [DISCARD: Historical tea purchase (1974), superseded by p13/p127.] quote: "In 1974, the average family purchased 68g - about 30 tea bags - of tea per person, per week."
  - p126 Average weekly tea purchased per person in 1974 in tea bags = **30** tea bags per person per week (1974-01-01..1974-12-31) [DISCARD: Historical tea bags (1974), superseded by p128.] quote: "In 1974, the average family purchased 68g - about 30 tea bags - of tea per person, per week."
  - p127 Average weekly tea purchased per person in 2023 (government figures) = **19** grams per person per week (2023-01-01..2023-12-31) [keep: ] quote: "By 2023, that had gone down to 19g - about 10 tea bags - per person, according to government figures."
  - p128 Average weekly tea purchased per person in 2023 in tea bags = **10** tea bags per person per week (2023-01-01..2023-12-31) [keep: ] quote: "By 2023, that had gone down to 19g - about 10 tea bags - per person, according to government figures."
- `https://stir-tea-coffee.com/tea-coffee-news/nearly-everyone-in-the-uk-still-drinks-tea/` -> **live_dated** (page date 2024-06-18); points raw/verified 15/2
  - p129 Global tea market value forecast for 2025 = **134,400,000,000** USD (forecast) (2025-01-01..2025-12-31) [DISCARD: Global market forecast, not UK consumption.] quote: "The global market is expanding and will be worth an estimated $134.4 billion by 2025"
  - p130 UK tea export value in 2023 (7th by value globally) = **121,400,000** USD (2023-01-01..2023-12-31) [DISCARD: UK tea export value, not domestic consumption.] quote: "In 2023, the UK ranked 7th by value in tea exports, shipping $121.4 million worth of mainly black tea"
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 13/7
  - p131 Share of UK 18-24-year-olds having a daily cuppa = **83** % of 18-24-year-olds surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p1, p7, p42, p53, p97.] quote: "over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p132 Share of 18-24-year-olds citing great taste as main reason for tea = **80** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p3, p9, p44, p55, p98.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p133 Share of over-25s citing great taste as main reason for tea = **85** % of over-25s surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p4, p10, p45, p56, p99.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p134 Share of younger adults saying they drink more tea than their parents = **31** % of younger adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p5, p11, p46, p57, p100.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p135 Share of young adults brewing a cuppa on waking = **10** share of young adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p47, p101; attitudinal.] quote: "Seven out of 10 young adults brew up a cuppa as soon as they get out of bed."
  - p136 Sample size of UK adults in Omnibus survey on tea habits = **4,000** UK adults surveyed (2022-12-01..2022-12-31) [DISCARD: Duplicate of p2, p8, p43, p54, p102.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p137 Sample size of second UK adults poll on tea attitudes = **1,000** UK adults surveyed (2023-03-01..2023-05-31) [DISCARD: Duplicate of p6, p12, p48, p58, p103.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- `https://www.gov.uk/government/statistics/family-food-fye-2023/family-food-fye-2023` -> **live_dated** (page date 2024-10-17); points raw/verified 15/14
  - p138 UK household purchases of beverages (tea/coffee etc.) per person per week, FYE 2 = **49** grams per person per week (2022-04-01..2023-03-31) [DISCARD: Beverages total (tea/coffee etc.), not tea-specific; misleading if used as tea quantity.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p139 UK household purchases of beverages per person per week, FYE 2022 = **57** grams per person per week (2021-04-01..2022-03-31) [DISCARD: Historical beverage purchases (FYE 2022), not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p140 UK household purchases of beverages per person per week, FYE 2021 = **60** grams per person per week (2020-04-01..2021-03-31) [DISCARD: Historical beverage purchases (FYE 2021), not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p141 UK household purchases of beverages per person per week, FYE 2020 = **56** grams per person per week (2019-04-01..2020-03-31) [DISCARD: Historical beverage purchases (FYE 2020), not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p142 UK household purchases of beverages per person per week, FYE 2019 = **52** grams per person per week (2018-04-01..2019-03-31) [DISCARD: Historical beverage purchases (FYE 2019), not tea-specific.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p143 Percentage change in UK household beverage purchases FYE 2020 to FYE 2023 = **-11.4** % (2019-04-01..2023-03-31) [DISCARD: Percentage change, not a level.] quote: "\| Beverages \| \| 52 \| 56 \| 60 \| 57 \| 49 \| -13.5% \| -11.4% \|"
  - p144 UK household purchases of soft drinks per person per week, FYE 2023 = **1,500** millilitres per person per week (2022-04-01..2023-03-31) [DISCARD: Soft drinks, not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
  - p145 UK household purchases of soft drinks per person per week, FYE 2022 = **1,670** millilitres per person per week (2021-04-01..2022-03-31) [DISCARD: Soft drinks, not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
  - p146 UK household purchases of soft drinks per person per week, FYE 2021 = **1,812** millilitres per person per week (2020-04-01..2021-03-31) [DISCARD: Soft drinks, not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
  - p147 UK household purchases of soft drinks per person per week, FYE 2020 = **1,658** millilitres per person per week (2019-04-01..2020-03-31) [DISCARD: Soft drinks, not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
  - p148 UK household purchases of soft drinks per person per week, FYE 2019 = **1,642** millilitres per person per week (2018-04-01..2019-03-31) [DISCARD: Soft drinks, not tea.] quote: "\| Soft drinks (b) \| (ml) \| 1642 \| 1658 \| 1812 \| 1670 \| 1500 \| -10.2% \| -9.5% \|"
  - p149 Share of UK food and drink expenditure consumed outside the home, FYE 2023 = **23** % (2022-04-01..2023-03-31) [DISCARD: Share of food expenditure out-of-home, not tea-specific.] quote: "23% of expenditure on food and drink was spent on eating out in FYE 2023, up from 22% in FYE 2022 and the low of 8% in FYE 2021 due partly to COVID-19 restrictions."
  - p150 Share of UK food and drink expenditure consumed outside the home, FYE 2021 (COVI = **8** % (2020-04-01..2021-03-31) [DISCARD: Share of food expenditure out-of-home, not tea-specific.] quote: "23% of expenditure on food and drink was spent on eating out in FYE 2023, up from 22% in FYE 2022 and the low of 8% in FYE 2021 due partly to COVID-19 restrictions."
  - p151 Annual CPIH food and non-alcoholic beverage price inflation, March 2023 = **19.2** % (2023-03-01..2023-03-31) [DISCARD: Food price inflation, not a consumption quantity.] quote: "In March 2023, the annual CPIH food and non alcoholic beverage prices rose by 19.2%, which was much higher than the CPIH all items rate of 8.9% in the same period."
- dropped by code checks: 26 (period_end missing or unparseable: 21; scale word 'million' not supported by quote or table header: 1; scale word 'billion' not supported by quote or table header: 1; number: no number in value_as_written: 2; value_as_written not in quote as a whole number: 1)

### d8 [persona] Catering / workplace / hospitality operator

Hypothesis: Out-of-home tea servings/day can be estimated from hospitality footfall (cafés, pubs, workplaces) × share ordering tea × servings per visit, added to at-home estimate. Direction: provides the out-of-home component often missing from retail-volume routes.

Queries issued by the searcher: UK coffee shop transactions per day footfall statistics; share of hot drinks ordered tea UK hospitality statistics; cafe visits per day UK statistics; UK Tea & Infusions Association 100 million cups tea day out of home; "tea" "out of home" million cups UK foodservice; Kantar tea 15% hot drinks foodservice coffee 75%; UK foodservice hot drinks servings per day tea coffee

- `https://www.foodstandards.gov.scot/downloads/Monitoring_out_of_home_food_and_drink_purchases_in_Scotland_and_Great_Britain_%282022_and_2023%29.pdf` -> **live_dated** (page date 2023-11-10); points raw/verified 0/0
- `https://www.npdgroup.co.uk/wps/wcm/connect/npd/b081c711-03ce-40fc-be10-9d614ed5081d/UK+Food+SME+Aug+2019.pdf?MOD=AJPERES&CONVERT_TO=url&CACHEID=ROOTWO` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.thecaterer.com/products--equipment/trends-in-tea-targeting-a-smaller-market` -> **live_dated** (page date 2024-10-28); points raw/verified 8/2
  - p152 Number of consecutive Great Taste awards for Birchall Great Rift blend as of 202 = **14** awards (consecutive) (2024-01-01..2024-12-31) [DISCARD: Awards, irrelevant.] quote: "Our flagship Great Rift blend was awarded its 14th consecutive Great Taste award in 2024."
  - p153 Mintel growth of chai latte in 2023 = **94** % growth (2023-01-01..2023-12-31) [DISCARD: Chai latte growth, irrelevant.] quote: "Mintel figures show chai latte saw 94% growth in 2023"
- `https://www.publicsectorcatering.co.uk/news/new-delifrance-research-showcases-brits-love-coffee-shops` -> **live_dated** (page date 2025-06-05); points raw/verified 5/0
- dropped by code checks: 11 (period_end missing or unparseable: 10; period_end 2028-12-31 after as_of: 1)

### b1 [related_series] UK tea market volume

Hypothesis: If we can obtain total UK retail tea volume (kg/year) from Kantar/Nielsen/IRI, we can convert to cups using a grams-per-cup factor and add out-of-home. This would provide a bottom-up flow estimate independent of survey-based per-capita rates.

Queries issued by the searcher: UK retail tea sales volume tonnes kg 2024 Kantar; UK tea market value volume 2024 UKTIA tonnes consumed; "UK Tea and Infusions Association" "100 million cups" tea drunk every day UKTIA facts; The Grocer tea volume sales decline Kantar black tea kg 2024

- `https://www.tastingtable.com/1872396/how-much-tea-british-people-drink/` -> **live_dated** (page date 2025-06-01); points raw/verified 15/0
- `https://www.indexbox.io/store/united-kingdom-kw-fair-trade-green-tea-840-market-analysis-forecast-size-trends-and-insights/` -> **live_dated** (page date 2026-05-24); points raw/verified 15/0
- `https://asemconnectvietnam.gov.vn/default.aspx?ID1=2&ZID1=8&ID8=142023` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tea.co.uk/assets/uploads/files/news/39ef5-uk-tea-census-report-2022-web.pdf` -> **live_dated** (page date 2022-05-13); points raw/verified 15/6
  - p154 Tea Census poll sample size (UK employed tea drinkers) = **1,000** people polled (2022-03-01..2022-08-31) [DISCARD: Sample size only; no estimand.] quote: "Independent poll of 1000 UK employed tea drinkers conducted by Perspectus Global; Spring/Summer 2022"
  - p155 Share of respondents drinking black tea with or without milk = **74** % of respondents (2022-03-01..2022-08-31) [DISCARD: Share drinking black tea (type preference), not cups; not a rate.] quote: "nearly three quarters of those questioned (74%) drink black tea with or without milk, whilst 55% drink green tea and just under half (47%) also enjoy herbal infusions."
  - p156 Share of respondents drinking green tea = **55** % of respondents (2022-03-01..2022-08-31) [DISCARD: Share drinking green tea (type preference), not cups.] quote: "nearly three quarters of those questioned (74%) drink black tea with or without milk, whilst 55% drink green tea and just under half (47%) also enjoy herbal infusions."
  - p157 Share of respondents enjoying herbal infusions = **47** % of respondents (2022-03-01..2022-08-31) [DISCARD: Share enjoying herbal infusions, not cups.] quote: "nearly three quarters of those questioned (74%) drink black tea with or without milk, whilst 55% drink green tea and just under half (47%) also enjoy herbal infusions."
  - p158 Share of respondents drinking black tea several times a day = **40** % of respondents (2022-03-01..2022-08-31) [DISCARD: Share drinking black tea several times a day; qualitative, not a mean rate.] quote: "40% drink black tea with or without milk, several times a day"
  - p159 Share of respondents drinking several cups of green tea a day = **10** % of respondents (2022-03-01..2022-08-31) [DISCARD: Share drinking several cups of green tea; qualitative, not a mean rate.] quote: "10% drink several cups of green tea a day"
- dropped by code checks: 39 (period_end missing or unparseable: 35; scale word 'million' not supported by quote or table header: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2)

### b2 [base_rates] Per-capita tea consumption

Hypothesis: A representative survey of UK adults reporting average cups per day (not just categories) would directly give a per-capita rate. Existing surveys give conflicting categorical data; a mean would resolve the disagreement.

Queries issued by the searcher: YouGov survey average cups of tea per day UK adults; UK Tea and Infusions Association tea consumption 100 million cups per day statistics; Mintel UK tea consumption average cups per day per person survey; "cups of tea" per day survey UK "1-2 cups" "3-4 cups" percentage adults 2024

- `https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation` -> **live_dated** (page date 2025-06-30); points raw/verified 15/15
  - p160 Share of British adults drinking tea at home or work at least twice a day = **41** % of British adults (..) [DISCARD: Share drinking tea at least twice a day; a threshold share, not a mean cups rate.] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p161 Share of British adults drinking coffee at home or work at least twice a day = **40** % of British adults (..) [DISCARD: Coffee comparison share; irrelevant to tea cups.] quote: "Among British adults, 41% drink tea and 40% drink coffee at home or at work at least twice a day."
  - p162 Share of tea drinkers buying tea out of home at least once a week = **16** % of tea drinkers (..) [keep: ] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p163 Share of coffee drinkers buying coffee out of home at least once a week = **12** % of coffee drinkers (..) [DISCARD: Coffee out-of-home share; irrelevant to tea cups.] quote: "Just 16% of tea drinkers and 12% of coffee drinkers buy their drinks at a takeaway, café, or similar venue at least once a week."
  - p164 Share of Gen Z drinking tea daily = **11** % of Gen Z (..) [keep: ] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p165 Share of Gen Z drinking coffee daily = **8** % of Gen Z (..) [DISCARD: Coffee daily share; irrelevant.] quote: "Just 11% of Gen Z drink tea daily, compared to 8% who drink coffee every day."
  - p166 Share of Millennials drinking tea daily = **23** % of Millennials (..) [keep: ] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p167 Share of Millennials drinking coffee daily = **24** % of Millennials (..) [DISCARD: Coffee daily share; irrelevant.] quote: "Among Millennials, 23% drink tea daily and 24% drink coffee."
  - p168 Share of Gen X drinking tea daily = **31** % of Gen X (..) [keep: ] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p169 Share of Gen X drinking coffee daily = **33** % of Gen X (..) [DISCARD: Coffee daily share; irrelevant.] quote: "Gen Xers show a similar balance, with 31% consuming tea and 33% coffee daily."
  - p170 Share of Baby Boomers drinking tea daily = **32** % of Baby Boomers (..) [keep: ] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p171 Share of Baby Boomers drinking coffee daily = **32** % of Baby Boomers (..) [DISCARD: Coffee daily share; irrelevant.] quote: "Baby Boomers are nearly split as well, with 32% drinking tea and 32% drinking coffee each day."
  - p172 Share of daily tea drinkers nationally choosing green tea = **20** % of daily tea drinkers (..) [DISCARD: Share choosing green tea among daily drinkers; type mix, not cups.] quote: "32% of Gen Z daily tea drinkers opt for green tea (vs. 20% nationally)"
  - p173 Share of daily tea drinkers nationally choosing fruit tea = **13** % of daily tea drinkers (..) [DISCARD: Share choosing fruit tea; type mix, not cups.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)."
  - p174 Share of daily tea drinkers nationally choosing herbal tea = **16** % of daily tea drinkers (..) [DISCARD: Share choosing herbal tea; type mix, not cups.] quote: "27% drink fruit tea (vs. 13%), and 28% enjoy herbal tea (vs. 16%)."
- `https://www.dailymail.co.uk/news/article-3044382/Average-Briton-enjoys-884-cups-tea-year-two-BATHS.html` -> **live_dated** (page date 2015-04-18); points raw/verified 10/6
  - p175 Average cups of tea consumed per Briton per year (YouGov poll) = **884** cups per year (..) [keep: ] quote: "The average Briton enjoys 884 cups of tea each year - or enough to fill two bathtubs, a survey has found."
  - p176 Average cups of tea consumed per Briton per week (YouGov poll) = **17** cups per week (..) [keep: ] quote: "The YouGov poll of more than 2,000 Britons revealed that we consume an average of 17 cups of tea each week."
  - p177 Average cups of tea per week among those aged 55 and over = **21** cups per week (..) [DISCARD: Age-band cups/week (2015) is a subgroup rate; superseded by overall p176 for a national mean.] quote: "those aged 55 and over typically enjoying 21 cups of tea a week compared with 18 to 24-year-olds, who only drink eight cups a week."
  - p178 Number of Britons surveyed in YouGov poll = **2,000** people (..) [DISCARD: Sample size only.] quote: "The YouGov poll of more than 2,000 Britons revealed that we consume an average of 17 cups of tea each week."
  - p179 Share of men who turn to tea when unwell = **16** percentage of men (..) [DISCARD: Attitudinal share; irrelevant to cups.] quote: "almost a third of women turn to a cuppa to make them feel better when they are unwell - in comparison with only 16 per cent of men."
  - p180 Share of 55 and overs who drink tea when sad = **11** percentage of 55 and overs (..) [DISCARD: Attitudinal share; irrelevant to cups.] quote: "nearly a quarter of 18 to 25s saying they put the kettle on when they are feeling down, compared with just 11 per cent of 55 and overs."
- `https://yougov.com/en-gb/articles/41661-part-five-drinking-habits-and-preferences` -> **live_dated** (page date 2022-04-20); points raw/verified 15/15
  - p181 Share of Britons who drink a cup of tea at least once a week = **74** % of Britons (..) [keep: ] quote: "Three quarters of Britons (74%) drink a cup of tea at least once a week, the study finds."
  - p182 Share of Britons who have more than 20 cups of tea over the course of the week = **17** % of Britons (..) [DISCARD: Threshold share (>20 cups/week); not a mean rate.] quote: "This includes 17% who say they have more than 20 cups over the course of the week."
  - p183 Share of Britons who don't drink tea at all = **25** % of Britons (..) [keep: ] quote: "A quarter of Britons (25%) don't drink tea at all."
  - p184 Share of 16-24-year-olds who don't drink tea at all = **39** % of 16-24-year-olds (..) [DISCARD: Subgroup non-drinker share; not needed for national mean.] quote: "This goes up to one in four (39%) among 16-24-year-olds."
  - p185 Share of those aged 60+ who drink 20 cups or more of tea a week = **24** % of those aged 60+ (..) [DISCARD: Subgroup threshold share; not a mean rate.] quote: "20 cups or more - a week (24% of those aged 60+ vs 6% of those aged 16-24)."
  - p186 Share of those aged 16-24 who drink 20 cups or more of tea a week = **6** % of those aged 16-24 (..) [DISCARD: Subgroup threshold share; not a mean rate.] quote: "20 cups or more - a week (24% of those aged 60+ vs 6% of those aged 16-24)."
  - p187 Share of tea-drinking Britons who take no sugar with tea = **74** % of tea-drinking Britons (..) [DISCARD: Sugar preference; irrelevant.] quote: "Three-quarters of tea-drinking Britons (74%) don't take any sugar with it"
  - p188 Share of Britons who drink coffee at least once a week = **70** % of Britons (..) [DISCARD: Coffee share; irrelevant.] quote: "Seven in ten Britons (70%) drink coffee at least once a week"
  - p189 Share of Britons who have more than 20 cups of coffee a week = **12** % of Britons (..) [DISCARD: Coffee share; irrelevant.] quote: "with one in eight (12%) having more than 20 cups a week."
  - p190 Share of Britons who don't drink coffee = **29** % of Britons (..) [DISCARD: Coffee share; irrelevant.] quote: "One in three Britons (29%) don't drink coffee."
  - p191 Share of Britons who do not drink tap water = **15** % of Britons (..) [DISCARD: Water share; irrelevant.] quote: "One in six Britons (15%) do not drink tap water"
  - p192 Share of Britons who don't drink bottled water = **66** % of Britons (..) [DISCARD: Water share; irrelevant.] quote: "Two-thirds (66%) don't drink bottled water."
  - p193 Share of Britons who don't drink milk = **50** % of Britons (..) [DISCARD: Milk share; irrelevant.] quote: "half of Britons don't drink milk (50%)"
  - p194 Share of Britons who don't typically drink fizzy drinks or fruit juice = **44** % of Britons (..) [DISCARD: Fizzy/juice share; irrelevant.] quote: "44% don't typically drink fizzy drinks or fruit juice."
  - p195 Share of 16-24-year-olds with at least one smoothie a week = **25** % of 16-24-year-olds (..) [DISCARD: Smoothie share; irrelevant.] quote: "a quarter (25%) of those aged 16-24 have at least one smoothie a week"
- `https://www.tea.co.uk/news/article/tea-loved-by-brits-and-5-billion-cups-of-tea-are-drunk-globally-each-day` -> **live_dated** (page date 2026-01-01); points raw/verified 13/12
  - p196 UK cups of tea drunk each day (UKTIA stated figure) = **100,000,000** cups of tea per day (..) [keep: ] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p197 UK cups of coffee drunk each day (comparison) = **98,000,000** cups of coffee per day (..) [DISCARD: Coffee comparison; irrelevant to tea cups.] quote: "Brits are drinking over 100 million cups of tea each day versus 98 million cups of coffee."
  - p198 Global cups of tea drunk each day = **5,000,000,000** cups of tea per day (..) [DISCARD: Global tea cups; not UK target.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p199 Global cups of coffee drunk each day = **2,000,000,000** cups of coffee per day (..) [DISCARD: Global coffee cups; irrelevant.] quote: "And across the globe we drink over 5 billion cups of tea each day[1] - way more than the 2 billion cups of coffee drunk daily."
  - p200 Estimated total global tea consumption (International Tea Committee) = **6,209,000,000** kg of tea (..) [DISCARD: Global tea consumption; not UK.] quote: "Estimated Total Global Consumption 6,209 Million Kg of Tea (Data Source: International Tea Committee)."
  - p201 Assumed average tea per cup used for conversion = **3** grams per cup (..) [keep: ] quote: "Using an average of 3g (per cup), this would equate to over 5 billion cups consumed worldwide every day."
  - p202 Share of 18–24-year-olds having a daily cuppa (UK survey) = **83** % of 18–24-year-olds (2022-12-01..2022-12-31) [DISCARD: Share of 18-24s having a daily cuppa; subgroup threshold, not a mean rate.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p203 UK adults surveyed in omnibus research = **4,000** UK adults (2022-12-01..2022-12-31) [DISCARD: Sample size only.] quote: "Real-world research[2] among 4,000 UK adults found that over eight in 10 (83%) 18-24-year-olds are having a daily cuppa."
  - p204 Share of younger adults citing great taste as main reason = **80** % of younger adults (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p205 Share of over-25s citing great taste as main reason = **85** % of over 25s (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; irrelevant.] quote: "The main reason given is the great taste - cited by 80% of younger adult and 85% of the over 25s."
  - p206 Share of younger adults drinking more tea than their parents = **31** % of younger adults polled (2022-12-01..2022-12-31) [DISCARD: Attitudinal share; irrelevant.] quote: "with 31% of younger adults polled saying they drink more tea than their parents"
  - p207 UK adults polled in Perspectus Global survey = **1,000** UK adults (2023-03-01..2023-05-31) [DISCARD: Sample size only.] quote: "Another real-world research poll[3] of more than 1000 UK adults also just published found that middle-aged and older adults think tea is great for hydration"
- dropped by code checks: 5 (number: no number in value_as_written: 4; value_as_written not in quote as a whole number: 1)

### b3 [physical_flow] Tea available for domestic consumption

Hypothesis: Net tea availability (imports minus exports plus stock change) from HMRC trade data, divided by grams per cup, gives a physical upper bound. This would validate or refute the headline 100-127 million cups/day figures.

Queries issued by the searcher: UK tea imports tonnes 2024 HMRC trade data; FAO tea imports United Kingdom tonnes 2023; UK tea exports tonnes 2024 HS 0902 re-exports HMRC; UKTIA "million cups" tea day grams per cup 2.5g tea bag

- `https://wits.worldbank.org/trade/comtrade/en/country/GBR/year/2024/tradeflow/Imports/partner/ALL/product/090230` -> **live_dated** (page date 2024-01-01); points raw/verified 15/15
  - p208 UK imports of black tea (HS 090230) from World, 2024, quantity = **11,182,300** Kg (2024-01-01..2024-12-31) [keep: ] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| World \| 73,469.38 \| 11,182,300 \| Kg \|"
  - p209 UK imports of black tea (HS 090230) from World, 2024, trade value = **73,469** 1000USD (2024-01-01..2024-12-31) [DISCARD: Trade value in USD for black tea; value not needed since quantity p208 is available.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| World \| 73,469.38 \| 11,182,300 \| Kg \|"
  - p210 UK imports of black tea (HS 090230) from Kenya, 2024, quantity = **6,317,170** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Kenya \| 26,944.27 \| 6,317,170 \| Kg \|"
  - p211 UK imports of black tea (HS 090230) from Poland, 2024, quantity = **1,368,030** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Poland \| 10,859.35 \| 1,368,030 \| Kg \|"
  - p212 UK imports of black tea (HS 090230) from Sri Lanka, 2024, quantity = **584,772** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Sri Lanka \| 7,783.22 \| 584,772 \| Kg \|"
  - p213 UK imports of black tea (HS 090230) from Germany, 2024, quantity = **314,550** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Germany \| 6,353.32 \| 314,550 \| Kg \|"
  - p214 UK imports of black tea (HS 090230) from Turkey, 2024, quantity = **619,486** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Turkey \| 6,318.66 \| 619,486 \| Kg \|"
  - p215 UK imports of black tea (HS 090230) from India, 2024, quantity = **897,676** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| India \| 5,233.29 \| 897,676 \| Kg \|"
  - p216 UK imports of black tea (HS 090230) from Ireland, 2024, quantity = **475,425** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Ireland \| 2,742.49 \| 475,425 \| Kg \|"
  - p217 UK imports of black tea (HS 090230) from United Arab Emirates, 2024, quantity = **192,185** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| United Arab Emirates \| 2,004.20 \| 192,185 \| Kg \|"
  - p218 UK imports of black tea (HS 090230) from China, 2024, quantity = **52,737** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| China \| 656.54 \| 52,737 \| Kg \|"
  - p219 UK imports of black tea (HS 090230) from Pakistan, 2024, quantity = **88,351** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Pakistan \| 529.55 \| 88,351 \| Kg \|"
  - p220 UK imports of black tea (HS 090230) from Indonesia, 2024, quantity = **11,259** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Indonesia \| 423.17 \| 11,259 \| Kg \|"
  - p221 UK imports of black tea (HS 090230) from France, 2024, quantity = **12,067** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| France \| 274.73 \| 12,067 \| Kg \|"
  - p222 UK imports of black tea (HS 090230) from Italy, 2024, quantity = **36,860** Kg (2024-01-01..2024-12-31) [DISCARD: Bilateral component of p208; redundant.] quote: "\| United Kingdom \| Import \| 090230 \| Black tea (fermented) and partly fermented tea \| 2024 \| Italy \| 200.97 \| 36,860 \| Kg \|"
- `https://asemconnectvietnam.gov.vn/default.aspx?ID1=2&ZID1=8&ID8=142023` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://gtaic.ai/market-reports?page=354` -> **live_dated** (page date 2025-07-22); points raw/verified 0/0
- `https://assets.publishing.service.gov.uk/media/6881de3ff47abf78ca1d35b0/agriculture-in-the-uk-2024.pdf` -> **live_dated** (page date 2025-07-24); points raw/verified 15/15
  - p223 UK imports of coffee, tea, etc. (SITC 07) value at 2024 prices = **6,005** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 value covers coffee, tea, cocoa, spices combined; not a tea quantity.] quote: "07 Coffee, Tea, Etc. 5,805 5,298 6,005"
  - p224 UK exports of coffee, tea, etc. (SITC 07) value at 2024 prices = **1,805** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 export value, combined category; not tea-specific.] quote: "07 Coffee, Tea, Etc. 1,854 1,701 1,805"
  - p225 UK imports of coffee, tea, etc. (SITC 07) from EU value at 2024 prices = **4,197** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 EU import value, combined category; not tea-specific.] quote: "07 Coffee, Tea, Etc. 3,847 3,722 4,197"
  - p226 UK imports of coffee, tea, etc. (SITC 07) from non-EU value at 2024 prices = **1,808** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 non-EU import value, combined category; not tea-specific.] quote: "07 Coffee, Tea, Etc. 1,958 1,576 1,808"
  - p227 UK exports of coffee, tea, etc. (SITC 07) to EU value at 2024 prices = **1,319** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 EU export value, combined category; not tea-specific.] quote: "07 Coffee, Tea, Etc. 1,176 1,180 1,319"
  - p228 UK exports of coffee, tea, etc. (SITC 07) to non-EU value at 2024 prices = **485** £ million (2024-01-01..2024-12-31) [DISCARD: SITC 07 non-EU export value, combined category; not tea-specific.] quote: "07 Coffee, Tea, Etc. 679 521 485"
  - p229 UK total food, feed and drink import volume 2024 (peak) = **43,200,000** tonnes (2024-01-01..2024-12-31) [DISCARD: Total food/feed/drink import volume; irrelevant to tea cups.] quote: "Import volumes have fluctuated over the past decade, reaching a peak in 2024 at 43.2 million tonnes."
  - p230 UK total food, feed and drink export volume 2024 = **10,800,000** tonnes (2024-01-01..2024-12-31) [DISCARD: Total food/feed/drink export volume; irrelevant to tea cups.] quote: "The overall volume of exports of food, feed and drink decreased by 9.5% from 2024 to 10.8 million tonnes in 2024."
  - p231 UK food, feed and drink imports value 2024 at 2024 prices = **64,053** £ million (2024-01-01..2024-12-31) [DISCARD: Total food import value; irrelevant to tea cups.] quote: "Imports of food, feed and drink 65,769 60,059 64,053"
  - p232 UK food, feed and drink exports value 2024 at 2024 prices = **24,552** £ million (2024-01-01..2024-12-31) [DISCARD: Total food export value; irrelevant to tea cups.] quote: "Exports of food, feed and drink 28,234 25,130 24,552"
  - p233 UK imports of coffee, tea, etc. (SITC 07) value at 2024 prices, 2023 = **5,298** £ million (2023-01-01..2023-12-31) [DISCARD: SITC 07 combined-category value, 2023; not tea-specific.] quote: "07 Coffee, Tea, Etc. 5,805 5,298 6,005"
  - p234 UK imports of coffee, tea, etc. (SITC 07) value at 2024 prices, 2022 = **5,805** £ million (2022-01-01..2022-12-31) [DISCARD: SITC 07 combined-category value, 2022; not tea-specific.] quote: "07 Coffee, Tea, Etc. 5,805 5,298 6,005"
  - p235 UK exports of coffee, tea, etc. (SITC 07) value at 2024 prices, 2023 = **1,701** £ million (2023-01-01..2023-12-31) [DISCARD: SITC 07 combined-category export value, 2023; not tea-specific.] quote: "07 Coffee, Tea, Etc. 1,854 1,701 1,805"
  - p236 UK exports of coffee, tea, etc. (SITC 07) value at 2024 prices, 2022 = **1,854** £ million (2022-01-01..2022-12-31) [DISCARD: SITC 07 combined-category export value, 2022; not tea-specific.] quote: "07 Coffee, Tea, Etc. 1,854 1,701 1,805"
  - p237 UK imports of coffee, tea, etc. (SITC 07) real-terms increase 2023 to 2024 = **13** % (2023-01-01..2024-12-31) [DISCARD: SITC 07 real-terms growth; combined category, not tea-specific.] quote: "imports of coffee, tea, cocoa, spices, etc. which increased by 13% to £6.0 billion"

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['tea consumption', 'uk tea', 'cups per day']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p49', 'p86'] Two independent headline estimates of UK daily tea cups: UKTIA 'over 100 million' (p49) and Aldi/Perspectus '127 million' (p86). Both are trade/press figures with unclear methodology, but they bracket
- corroborating: ['p62', 'p64', 'p75'] YouGov (p62, p64) and UKTIA/Crave (p75) both indicate high tea participation: 74% drink weekly, 25% never, and >90% drink at least one cup a day (p75). The p75 figure is likely overstated due to surve
- corroborating: ['p13', 'p127', 'p138'] Defra Family Food data: 19 g/person/week tea purchased at home in 2023 (p13, p127) and total beverages 49 g/person/week (p138). These are consistent with declining tea purchases and provide a physical
- corroborating: ['p14', 'p20', 'p21'] Out-of-home tea consumption series from Defra: 12 ml/person/week in 2023 (p14), 30 ml in 2014 (p20), 44 ml in 2004 (p21). Shows a declining trend but provides a small out-of-home volume component.
- corroborating: ['p34', 'p35'] Beverage Standards Association: average tea drinker has 2 cups out-of-home on a weekday (p34) and 1 on a weekend (p35). These are per-drinker, not per-capita, and from 2017, but useful for out-of-home
- conflicting: ['p22', 'p33', 'p76', 'p77', 'p78'] Surveys on cups per drinker per day conflict: p22/p33 say 35% drink 3+ cups/day; p76 says 35% drink 3-4 cups; p77 says 44% drink 1-2 cups; p78 says 20% drink 5-6 cups. These are from different surveys
- corroborating: ['p85', 'p88', 'p89'] Aldi/Perspectus survey: average 4 cups/day per person (p85), 72% drink average 4 cups/day (p88), 1,460 cups/year per Brit (p89). These are internally consistent but likely overstate per-capita consump
- corroborating: ['p111', 'p119'] ONS population estimates: 69.5 million mid-2025 (p111) and 69,483,900 for 2025 (p119). These are consistent and provide the population denominator.
- corroborating: ['p23', 'p28'] UK tea imports: 53,000 tonnes in H1 2023 (p23) and Kenya alone 30,100 tonnes (p28). These are consistent with import volumes and can be used for a physical-flow estimate, though they include re-export
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p49', 'p196'] Same UKTIA headline ('over 100 million cups a day') captured twice from the same publisher; not independent, and it is a rounded trade-body claim of unknown derivation.
- corroborating: ['p86', 'p85', 'p89', 'p88'] Aldi's 127 million figure is internally built from its own 4-cups-per-person and 1,460-cups-per-year inputs; these are one source, not independent confirmation of the UKTIA figure.
- conflicting: ['p49', 'p86'] Two headline totals differ by ~27%; both are commercial/trade claims with unclear scope (herbal inclusion, out-of-home, cup size).
- corroborating: ['p62', 'p64', 'p181', 'p183'] YouGov 2022: 74% drink tea weekly and 25% never — consistent complements from the same survey.
- corroborating: ['p75', 'p76', 'p77', 'p78'] Same UKTIA/Crave survey distribution; note p75's parsed value (10) contradicts its quote ('more than nine in 10'), so it is unreliable as a share.
- corroborating: ['p22', 'p76'] Both report ~35% drinking three or more cups a day, but likely share a common survey lineage; treat as one signal.
- corroborating: ['p175', 'p176'] 884 cups/year and 17 cups/week are the same YouGov 2015 statistic restated; one underlying measurement.
- corroborating: ['p13', 'p127', 'p128'] Defra-derived 19 g/person/week in 2023, restated by BBC as ~10 tea bags; same underlying government series.
- conflicting: ['p13', 'p175'] Household purchase data (~19 g/week ≈ 6 cups/week at 3 g) is far below survey-based 17 cups/week; purchase data excludes out-of-home and may under-record, while surveys over-report.
- corroborating: ['p208', 'p210', 'p211', 'p212', 'p213', 'p214', 'p215', 'p216', 'p217', 'p218', 'p219', 'p220', 'p221', 'p222'] WITS bilateral black-tea import lines sum to the World total p208; they are components, not independent estimates.
- conflicting: ['p23', 'p208'] H1-2023 total tea imports 53 kt vs 2024 black-tea-only imports 11.2 kt; different periods and HS coverage (all tea vs HS 090230), so not directly comparable.
- corroborating: ['p111', 'p119'] Two ONS mid-2025 population estimates (69.5m and 69.48m); effectively the same source.
- corroborating: ['p34', 'p35', 'p162'] Out-of-home tea is a modest channel: ~1-2 cups/day among drinkers on weekdays/weekends (2017) and only 16% buying out-of-home weekly (YouGov).
- corroborating: ['p164', 'p166', 'p168', 'p170'] YouGov generational daily-tea shares rise with age (11% Gen Z to ~32% Boomers), consistent with declining per-capita trend.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Share of UK black-tea imports actually brewed into domestic cups (net of re-export, waste, non-beverage use) | 0.85 | 0.7..0.95 | 0.5766..1.153 (widened) | fraction | unused | Imports include re-exports and some industrial/non-beverage use; most imported black tea is brewed in UK homes and cafés. Wide range reflects stock changes and re-export uncertainty. | Used to convert black-tea import mass into cups drunk in the UK. | Evidence of a large re-export share or substantial non-beverage tea use in the UK. |
| a2 | Average grams of tea per cup (UK domestic brewing) | 2.5 | 1.8..3.5 | 1.775..3.55 (widened) | grams per cup | unused | UKTIA uses 3 g/cup globally; UK tea bags are typically ~2-2.5 g and mugs are larger, so a slightly lower per-cup mass is plausible. Range spans tea-bag to loose-leaf/mug practice. | Converting tea mass to cup servings for UK domestic consumption. | Documented UK average tea-bag mass or brewing strength materially outside this range. |
| a3 | Out-of-home tea cups per person per day (all UK population) | 0.15 | 0.05..0.4 | 0.05..0.4 | cups per person per day | m2 (m4) | p34/p35 give 1-2 cups/day among out-of-home tea drinkers, but only ~16% of tea drinkers buy out-of-home weekly (p162); averaging over the whole population yields a small per-capita out-of-home rate. | Added to at-home per-capita rate to cover the out-of-home channel. | Survey showing a much larger share of the population regularly drinking tea out of home. |
| a4 | Average at-home cups per person per day implied by household purchase data | 0.9 | 0.6..1.4 | 0.6..1.4 | cups per person per day | m2 (m4) | p13/p127 give 19 g/person/week; at ~2.5 g/cup this is ~7.6 cups/week ≈ 1.1 cups/day, but household purchase data under-record some consumption; range reflects cup-mass and under-recording uncertainty. | Used as the at-home component of a bottom-up per-capita estimate. | Evidence that household purchase data substantially under- or over-state actual brewed cups. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 169,252,661 | ['p119', 'p176'] / [] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 76,678,232 | ['p119'] / ['a3', 'a4'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 100,021,162 | ['p49'] / [] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: sum over channel of at-home, out-of-home
- m3 coverage: the whole target

Result: central **109,085,367** cup/day, 80% interval [70,415,744, 168,990,864] cup/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.33

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['uk', 'united kingdom']; measure stems ['consu', 'cup', 'peopl', 'tea']


## Final answer

The best computed estimate is 109,085,367 cup/day (80% model-based interval 70,415,744 to 168,990,864 cup/day), for total cups of hot brewed tea consumed by all people in the UK on a single day in 2026. Three routes were combined with equal weights: a survey-based route using population 69,483,900 people times 17 cups per week converted to daily (169,252,661 cup/day, weight 33%); a bottom-up at-home plus out-of-home decomposition (76,678,232 cup/day, weight 33%); and the trade-body headline 100,000,000 cups of tea per day (100,021,162 cup/day, weight 33%). Observed inputs are population, the YouGov weekly figure, and the UKTIA claim; the at-home rate 0.9 (range 0.6 to 1.4) and out-of-home rate 0.15 (range 0.05 to 0.4) are analyst assumptions. No backtest error was available, so the interval reflects input uncertainty only. The biggest risk is that the survey mean overstates current consumption and the trade figure is rounded and undated. Better evidence would be recent measured per-capita intake and out-of-home consumption data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a3 Out-of-home tea cups per person per day (all UK population): 0.15 cups per person per day, range 0.05 to 0.4; used by m2. Overturned by: Survey showing a much larger share of the population regularly drinking tea out of home.
- a4 Average at-home cups per person per day implied by household purchase data: 0.9 cups per person per day, range 0.6 to 1.4; used by m2. Overturned by: Evidence that household purchase data substantially under- or over-state actual brewed cups.

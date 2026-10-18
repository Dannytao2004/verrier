# Evidence ledger: smoke_pizza

- Question: How many tonnes of pizza do people in Chicago eat on an average day in 2026?
- as_of: 2026-10-18
- Pinned target: Total mass of pizza consumed by people in Chicago (city of Chicago, all pizza types, all consumption occasions: restaurant, takeout, delivery, and home-prepared from purchased/frozen pizza) on an average day in calendar year 2026 | unit metric tonnes per day | period 2026-01-01..2026-12-31 | publisher No official publisher; analyst-constructed estimate

## Directions and pages

### d1 [related_series] National/industry pizza market data provider or trade association

Hypothesis: US per-capita pizza consumption (kg/person/year) multiplied by Chicago population gives a first-order total; Chicago's pizza culture and dense restaurant supply likely push it above the national average, so a Chicago adjustment factor (restaurant density or sales-per-capita ratio) is needed. Target = per_capita_pizza_kg * population / 365.

Queries issued by the searcher: how much pizza does the average American eat per year statistics; US pizza industry sales 2024 billions Pizza Restaurant Association; USDA ERS per capita pizza consumption pounds per person 2023 pizza servings day; Census Bureau Chicago city population estimate 2025

- `https://www.hindustantimes.com/lifestyle/america-is-falling-out-of-love-with-pizza-101767590184330.html` -> **live_dated** (page date 2026-01-05); points raw/verified 14/4
  - p1 US pizza chain restaurant sales, 2024 (Technomic) = **31,000,000,000** USD (2024-01-01..2024-12-31) [keep: Kept as national pizza-chain sales context for a spend-based route; requires Chicago allocation and price/mass conversio] quote: "Pizza chains generated around $31 billion in sales from their restaurants in 2024, the market-research firm Technomic said."
  - p2 California Pizza Kitchen sale price, December (investor group) = **300,000,000** USD (2024-12-01..2024-12-31) [DISCARD: California Pizza Kitchen sale price is a corporate M&A valuation, irrelevant to pizza mass consumed in Chicago.] quote: "California Pizza Kitchen was sold in December to an investor group for under $300 million, according to people familiar with the matter."
  - p3 California Pizza Kitchen prior sale price, 2011 = **470,000,000** USD (2011-01-01..2011-12-31) [DISCARD: 2011 CPK sale price; same irrelevance as p2.] quote: "That is less than the $470 million it sold for in 2011, when the chain went private."
  - p4 Year US pizza restaurant count hit record high (Datassential) = **2,019** year (2019-01-01..2019-12-31) [DISCARD: Year the US pizza-restaurant count peaked (2019) is a bare year label, not a quantity usable in any route.] quote: "The number of pizza restaurants in the U.S. hit a record high in 2019 and has declined since then, figures from the market-research firm Datassential show."
- `https://www.tastingtable.com/1854781/where-pizza-most-popular/` -> **live_dated** (page date 2025-05-15); points raw/verified 8/0
- `https://www.ibisworld.org/united-states/industry/pizza-restaurants/4320/` -> **live_dated** (page date 2026-01-01); points raw/verified 0/0
- `https://www.census.gov/quickfacts/fact/table/chicagocityillinois/PST045224` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 18 (period_end missing or unparseable: 14; number: no number in value_as_written: 3; value_as_written not in quote as a whole number: 1)

### d2 [related_series] Restaurant/food-service sales and expenditure statistics

Hypothesis: Chicago food-away-from-home and pizza-restaurant sales (USD) divided by average price per pizza and average pizza mass yields pizza mass sold; pizza's share of Chicago restaurant sales times total Chicago restaurant sales gives pizza sales. Target = (Chicago restaurant sales * pizza share) / price_per_pizza * mass_per_pizza / 365.

Queries issued by the searcher: Chicago restaurant industry sales 2024 total Illinois Restaurant Association; pizza share of restaurant sales United States percent limited service; "Chicago-Naperville-Elgin" eating and drinking places sales 2025 restaurant economic impact study; average price of a large pizza United States 2024 dollars average pizza weight grams

- `https://restaurant.org/getmedia/3ea909b6-a3c2-4178-bf6e-5d4a567b4f0f/il_econ_impact_study_fs-3.pdf` -> **live_dated** (page date 2025-07-29); points raw/verified 15/5
  - p5 Chicago-Naperville-Elgin MSA eating and drinking places direct employment, 2025 = **424,662** jobs (2025-01-01..2025-12-31) [keep: Kept as MSA restaurant-employment context; not city-scope, so not a direct input.] quote: "CHICAGO￾NAPERVILLE, ELGIN, IL-IN Direct Total $46.99B $86.32B 424,662 588,064"
  - p6 Chicago-Naperville-Elgin MSA eating and drinking places total employment (direct = **588,064** jobs (2025-01-01..2025-12-31) [keep: Kept as MSA restaurant-employment context; indirect/induced, not a direct input.] quote: "424,662 588,064 $16.35B $30.13B"
  - p7 Illinois eating and drinking places projected direct employment, 2025 = **552,014** jobs (2025-01-01..2025-12-31) [keep: Kept as Illinois restaurant-employment context; state scope, not a direct input.] quote: "support 552,014 jobs, and deliver $19.57B in total labor income"
  - p8 Illinois limited-service restaurants direct employment, 2025 = **210,196** jobs (2025-01-01..2025-12-31) [keep: Kept as Illinois limited-service employment context; not pizza-specific.] quote: "LIMITED-SERVICE RESTAURANTS Direct Total $24.70B $45.29B 210,196 300,472"
  - p9 Illinois full-service restaurants direct employment, 2025 = **212,941** jobs (2025-01-01..2025-12-31) [keep: Kept as Illinois full-service employment context; not pizza-specific.] quote: "FULL SERVICE RESTAURANTS Direct Total $22.67B $40.29B 212,941 291,637"
- `https://www.prlog.org/11820232-the-us-commercial-foodservice-market-how-the-pizza-industry-is-making-an-impact.html` -> **live_dated** (page date 2026-10-18); points raw/verified 7/0
- `https://reportify.cn/reports/1290603838776152064` -> **live_dated** (page date 2026-06-09); points raw/verified 15/9
  - p10 US restaurant industry total sales, 2025, year-over-year growth = **2** percent (2025-01-01..2025-12-31) [keep: Kept as US restaurant sales-growth context; not pizza-specific.] quote: "2025年餐饮行业总销售额同比增长2.0%至7590亿美元"
  - p11 US limited-service restaurant sales, 2025, year-over-year growth = **2.9** percent (2025-01-01..2025-12-31) [keep: Kept as US limited-service growth context; not pizza-specific.] quote: "有限服务餐厅增长2.9%至4670亿美元"
  - p12 US full-service restaurant sales, 2025, year-over-year growth = **0.7** percent (2025-01-01..2025-12-31) [keep: Kept as US full-service growth context; not pizza-specific.] quote: "全方位服务餐厅增长0.7%至2920亿美元"
  - p13 Top 500 chain restaurant sales growth, 2025 = **3** percent (2025-01-01..2025-12-31) [keep: Kept as chain-sales growth context; not pizza-specific.] quote: "前500强连锁店销售额增长3.0%,独立餐厅增长0.7%"
  - p14 Independent restaurant sales growth, 2025 = **0.7** percent (2025-01-01..2025-12-31) [keep: Kept as independent-restaurant growth context; not pizza-specific.] quote: "前500强连锁店销售额增长3.0%,独立餐厅增长0.7%"
  - p15 Chain share of US restaurant industry sales, 2025 = **59.5** percent (2025-01-01..2025-12-31) [keep: Kept as chain-share context; not pizza-specific.] quote: "连锁店销售额占行业的59.5%,同比增加60个基点"
  - p16 Chain share of US restaurant industry sales, 2025, year-over-year change = **60** basis points (2025-01-01..2025-12-31) [keep: Kept as chain-share change context; not pizza-specific.] quote: "连锁店销售额占行业的59.5%,同比增加60个基点"
  - p17 Top 500 chain restaurant unit count change, 2025 = **1.4** percent (2025-01-01..2025-12-31) [keep: Kept as chain unit-count change context; not pizza-specific.] quote: "2025年行业门店总数下降0.9%,前500强连锁店增长1.4%,独立餐厅下降2.1%"
  - p18 US limited-service restaurant unit count change, 2025 = **0.2** percent (2025-01-01..2025-12-31) [keep: Kept as limited-service unit-count change context; not pizza-specific.] quote: "有限服务餐厅门店数量基本持平,增长0.2%,全方位服务餐厅下降2.4%"
- `https://www.prlog.org/12437416-chd-expert-evaluates-the-pizza-industry-in-the-united-states-any-way-you-slice-it-pizza-is-popular.html` -> **live_dated** (page date 2026-10-18); points raw/verified 15/0
- dropped by code checks: 38 (scale word 'billion' not supported by quote or table header: 10; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 2; period_end missing or unparseable: 20; number: value_as_written is only part of a larger CJK number in the quote: 3; value_as_written not in quote as a whole number: 3)

### d3 [capacity_consumption] Pizza restaurant operators and delivery platforms in Chicago

Hypothesis: Number of pizza-serving establishments in Chicago times average pizzas sold per establishment per day times average pizza mass gives total pizza throughput. Target = establishments * pizzas_per_day * mass_per_pizza.

Queries issued by the searcher: number of pizzerias in Chicago; average pizzas sold per day per pizzeria; Domino's Pizza number of stores Chicago Illinois 2024; how many pizzas are eaten per day in Chicago

- `https://rentechdigital.com/smartscraper/it/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p19 Count of pizza restaurants in Chicago (business listing count) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as the current Chicago pizza-establishment count for the capacity route; listing count, not throughput.] quote: "Ci sono 1987 Pizza restaurants in Chicago al April 1, 2026"
  - p20 Count of pizza restaurants in Chicago (total, restated) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p19 (same 1,987 count, same source/date).] quote: "Ci sono un totale di 1987 Ristoranti di pizza in Chicago al April 01, 2026."
  - p21 Single-owner pizza restaurants in Chicago (count) = **914** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as a partition of the establishment count; same source as p19.] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p22 Share of Chicago pizza restaurants that are single-owner operations = **46** % (2026-04-01..2026-04-01) [DISCARD: Redundant with p21/p64/p66 (46% share already implied by 914/1,987).] quote: "che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p23 Pizza restaurants in Chicago belonging to larger brands (count) = **1,073** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as a partition of the establishment count; same source as p19.] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p24 Share of Chicago pizza restaurants that are part of larger brands = **54** % (2026-04-01..2026-04-01) [DISCARD: Redundant with p23/p65/p67 (54% share already implied by 1,073/1,987).] quote: "le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p25 Average age of pizza restaurants in Chicago = **10** years (plus 2 months) (2026-04-01..2026-04-01) [keep: Kept as establishment-age context; not a direct input.] quote: "Average age of Pizza restaurants in Chicago is10 anni e 2 mesi."
  - p26 Pizza restaurants in Chicago with own website (count) = **1,848** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-website context; not a direct input.] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web"
  - p27 Pizza restaurants in Chicago without own website (count) = **139** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-website context; not a direct input.] quote: "e i restanti 139 non hanno un proprio sito web"
  - p28 Pizza restaurants in Chicago with Facebook pages (count) = **1,048** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "1048 hanno pagine Facebook"
  - p29 Pizza restaurants in Chicago with Instagram accounts (count) = **848** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "848 sono attivi su Instagram"
  - p30 Pizza restaurants in Chicago with X accounts (count) = **635** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "635 hanno account su X (precedentemente Twitter)"
  - p31 Pizza restaurants in Chicago with LinkedIn profiles (count) = **88** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "88 hanno profili LinkedIn"
  - p32 Pizza restaurants in Chicago with TikTok profiles (count) = **189** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "189 sono su TikTok"
  - p33 Pizza restaurants in Chicago with YouTube channels (count) = **151** pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as establishment-social context; not a direct input.] quote: "151 have YouTube channels"
- `https://foodeist.com/index.php/pizza-statistics` -> **live_dated** (page date 2026-03-10); points raw/verified 15/0
- `https://www.asau.ru/files/pdf/2907022.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.horecabc.pl/kiedy-pizzeria-zaczyna-realnie-zarabiac/` -> **live_dated** (page date 2026-02-27); points raw/verified 15/0
- dropped by code checks: 30 (period_end missing or unparseable: 24; number: more than one number in value_as_written: 4; scale word 'thousand' not supported by quote or table header: 2)

### d4 [base_rates] Consumer survey / dietary intake data

Hypothesis: Share of people eating pizza on a given day times average servings per eater times serving mass gives daily pizza mass per capita; scaled to Chicago population. Target = population * daily_pizza_eater_share * servings_per_eater * serving_mass.

Queries issued by the searcher: NHANES percentage of Americans eating pizza on a given day; average pizza serving grams per eating occasion USDA; Dietary Data Brief 62 pizza consumption United States 2024 grams of pizza per eating occasion mean intake; pizza consumption frequency times per month survey United States adults percent eat pizza weekly

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/11
  - p34 Share of U.S. population (2+ years) consuming pizza on any given day, NHANES 201 = **11** percent of population (2017-01-01..2020-03-31) [keep: Kept as the national daily pizza-eater share for the base-rate route; requires Chicago transfer.] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p35 Share of U.S. population consuming pizza on any given day, all ages (Figure 1) = **12** percent of population (2017-01-01..2020-03-31) [keep: Kept as an alternate rendering of the same daily pizza-eater share; same source as p34.] quote: "12 17 17 18 13 11 6 10 11 14 15 11 8 5 All 2-5 6-11 12-19 20-39 40-59 60+"
  - p36 Share of U.S. adults 60+ consuming pizza on any given day = **6** percent of population (2017-01-01..2020-03-31) [keep: Kept as age-structure context for the base-rate route.] quote: "the percentage consuming decreased to about 6% among older adults (60+)"
  - p37 Share of pizza consumed at lunch among children 2-19 years = **41** percent of pizza intake (2017-01-01..2020-03-31) [keep: Kept as occasion-share context; not a direct input.] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p38 Share of pizza consumed at dinner among children 2-19 years = **48** percent of pizza intake (2017-01-01..2020-03-31) [keep: Kept as occasion-share context; not a direct input.] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p39 Share of pizza consumed at dinner among adults 20+ years = **58** percent of pizza intake (2017-01-01..2020-03-31) [keep: Kept as occasion-share context; not a direct input.] quote: "4 28 58 10"
  - p40 Share of pizza consumed at lunch among adults 20+ years = **28** percent of pizza intake (2017-01-01..2020-03-31) [keep: Kept as occasion-share context; not a direct input.] quote: "4 28 58 10"
  - p41 Share of pizza intake from snacks = **4** percent of pizza intake (2017-01-01..2020-03-31) [keep: Kept as occasion-share context; not a direct input.] quote: "Snacks accounted for 4% of pizza intake."
  - p42 Share of pizza obtained from restaurants = **56** percent of pizza consumed (2017-01-01..2020-03-31) [keep: Kept as source-share context; not a direct input.] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p43 Share of pizza obtained from school/daycare = **12** percent of pizza consumed (2017-01-01..2020-03-31) [keep: Kept as source-share context; not a direct input.] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p44 Share of pizza obtained from 'Other' sources = **6** percent of pizza consumed (2017-01-01..2020-03-31) [keep: Kept as source-share context; not a direct input.] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources such as a sport or entertainment facility or a convenience store"
- `https://www.ncbi.nlm.nih.gov/books/NBK610659/` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0
- `https://www.ncbi.nlm.nih.gov/books/NBK589563/` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0
- `https://www.govinfo.gov/content/pkg/CFR-2014-title9-vol2/pdf/CFR-2014-title9-vol2.pdf` -> **live_dated** (page date 2020-01-24); points raw/verified 0/0
- dropped by code checks: 4 (value_as_written not in quote as a whole number: 3; number: more than one number in value_as_written: 1)

### d5 [physical_flow] Food supply / agricultural disappearance statistics

Hypothesis: Upstream flour, cheese, and tomato sauce flows into the Chicago food system, allocated to pizza, can bound pizza mass; or national pizza cheese disappearance allocated by population share. Target = (cheese/flour used for pizza in Chicago) / ingredient mass fraction of pizza.

Queries issued by the searcher: US per capita cheese consumption 2024 pizza share mozzarella disappearance USDA; pizza ingredient composition dough cheese sauce percentages by weight; Chicago pizza sales per year number of pizzerias market size statistics; USDA ERS dairy data per capita cheese consumption mozzarella 2024 table pounds

- `https://cheesemarketnews.com/guestcolumn/2026/16jan26_01.html` -> **live_dated** (page date 2026-01-01); points raw/verified 15/5
  - p45 U.S. per capita cheese consumption, 2008 = **32.1** pounds per person per year (2008-01-01..2008-12-31) [keep: Kept as an older vintage of the cheese-consumption series; context only.] quote: "cheese consumption picked back up and increased from 32.1 pounds per person in 2008 to 38.1 pounds in 2019"
  - p46 U.S. per capita cheese consumption, 2019 = **38.1** pounds per person per year (2019-01-01..2019-12-31) [keep: Kept as a cheese-consumption vintage; context only.] quote: "increased from 32.1 pounds per person in 2008 to 38.1 pounds in 2019, an increase of 19% or an average of 1.4% per year."
  - p47 U.S. per capita cheese consumption, 2022 = **39.9** pounds per person per year (2022-01-01..2022-12-31) [keep: Kept as a cheese-consumption vintage; context only.] quote: "per capita cheese consumption fell slightly from 39.9 pounds in 2022 to 39.5 pounds in 2024."
  - p48 U.S. per capita cheese consumption, 2024 = **39.5** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as a cheese-consumption vintage; context only.] quote: "per capita cheese consumption fell slightly from 39.9 pounds in 2022 to 39.5 pounds in 2024."
  - p49 Average annual growth in U.S. per capita cheese consumption, 2008-2019 = **1.4** % per year (2008-01-01..2019-12-31) [keep: Kept as a cheese-consumption growth rate; context only.] quote: "an increase of 19% or an average of 1.4% per year."
- `https://local.newsbreak.com/cultivated-comfort-322399924/4889381757455-comfort-food-cravings-are-usually-blamed-on-culture-or-personal-taste-more-than` -> **live_dated** (page date 2026-09-16); points raw/verified 13/13
  - p50 US per-person total cheese consumption, 2024 (USDA ERS) = **48** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as total per-capita cheese consumption; context for the physical-flow route.] quote: "per-person cheese consumption in the United States reached 48.0 pounds in 2024"
  - p51 US per-person total cheese consumption, 2023 all-time high = **48.4** pounds per person per year (2023-01-01..2023-12-31) [keep: Kept as a cheese-consumption high; context only.] quote: "a hair under 2023's all-time high of 48.4 pounds"
  - p52 US per-person natural cheese consumption, 2024 = **39.9** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as natural-cheese consumption; context for the physical-flow route.] quote: "about 39.9 pounds is natural cheese - cheddar, mozzarella, Swiss, the whole deli case"
  - p53 US per-person processed cheese consumption, 2024 = **8.1** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as processed-cheese consumption; context only.] quote: "the remaining 8.1 pounds comes from processed products like American singles and cheese spreads"
  - p54 US per-person mozzarella consumption, 2024 = **12.5** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as the most pizza-relevant cheese figure (mozzarella per capita); requires Chicago transfer and ingredient-fraction] quote: "Americans ate 12.5 pounds of mozzarella per person in 2024, the cheese behind most pizza and lasagna"
  - p55 US per-person cheddar consumption, 2024 = **10.9** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as cheddar consumption; context only.] quote: "Cheddar alone accounted for 10.9 pounds of the American-type total"
  - p56 US per-person total cheese consumption, 2015 = **42.6** pounds per person per year (2015-01-01..2015-12-31) [keep: Kept as a cheese-consumption vintage; context only.] quote: "in 2015, the combined total sat at 42.6 pounds"
  - p57 US per-person daily cheese consumption implied by 48 pounds per year = **2** ounces per person per day (2024-01-01..2024-12-31) [keep: Kept as a daily cheese-consumption conversion; context only.] quote: "48 pounds works out to a little over 2 ounces of cheese per person, per day"
  - p58 US per-person fluid milk consumption, 1975 = **247** pounds per person per year (1975-01-01..1975-12-31) [keep: Kept as fluid-milk context; not pizza-relevant.] quote: "Back in 1975, the same ERS records show Americans drinking 247 pounds of fluid milk a year"
  - p59 US per-person American and other-than-American cheese consumption, 1975 = **14.3** pounds per person per year (1975-01-01..1975-12-31) [keep: Kept as historical cheese context; not pizza-relevant.] quote: "eating a comparatively modest 14.3 pounds combined of American and other-than-American cheese"
  - p60 US per-person fluid milk consumption, 2024 = **127** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as fluid-milk context; not pizza-relevant.] quote: "fluid milk consumption has fallen to about 127 pounds"
  - p61 US per-person American and other-than-American cheese consumption, 2024 = **39.5** pounds per person per year (2024-01-01..2024-12-31) [keep: Kept as historical cheese context; not pizza-relevant.] quote: "that same cheese combination has climbed to 39.5 pounds - nearly triple"
  - p62 Percent increase in US per-person total cheese consumption, 2015 to 2024 = **13** percent (2015-01-01..2024-12-31) [keep: Kept as cheese-growth context; not pizza-relevant.] quote: "That is nearly 13 percent more cheese per person in ten years"
- `https://www.plymouth.ac.uk/uploads/production/document/path/23/23543/Margherita_Pizza.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://rentechdigital.com/smartscraper/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p63 Number of Pizza restaurants in Chicago as of April 1, 2026 = **1,987** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p19.] quote: "There are 1987 Pizza restaurants in Chicago as of April 1, 2026"
  - p64 Pizza restaurants in Chicago that are single-owner operations (share of all Pizz = **46** % (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p21/p66.] quote: "914 Pizza restaurants which is 46.00% of all Pizza restaurants in Chicago are single-owner operations"
  - p65 Pizza restaurants in Chicago that are part of larger brands (share of all Pizza  = **54** % (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p23/p67.] quote: "the remaining 1073 which is 54.00% are part of larger brands"
  - p66 Pizza restaurants in Chicago that are single-owner operations (count) = **914** Pizza restaurants (2026-04-01..2026-04-01) [keep: Kept as a partition of the establishment count; same source as p19.] quote: "914 Pizza restaurants which is 46.00% of all Pizza restaurants in Chicago are single-owner operations"
  - p67 Pizza restaurants in Chicago that are part of larger brands (count) = **1,073** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p23/p82.] quote: "the remaining 1073 which is 54.00% are part of larger brands"
  - p68 Average age of Pizza restaurants in Chicago = **10** years (plus 2 months) (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p25/p84.] quote: "Average age of Pizza restaurants in Chicago is 10 years and 2 months."
  - p69 Pizza restaurants in Chicago with their own website (count) = **1,848** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p26/p85.] quote: "About 1848 Pizza restaurants have their own website and the remaining 139 don't have their own website."
  - p70 Pizza restaurants in Chicago without their own website (count) = **139** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p27/p86.] quote: "the remaining 139 don't have their own website"
  - p71 Pizza restaurants in Chicago with Facebook Pages = **1,048** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p28/p87.] quote: "1048 have Facebook Pages"
  - p72 Pizza restaurants in Chicago active on Instagram = **848** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p29/p88.] quote: "848 are active on Instagram"
  - p73 Pizza restaurants in Chicago with X (formerly Twitter) handles = **635** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p30/p89.] quote: "635 have X (formerly Twitter) handles"
  - p74 Pizza restaurants in Chicago on TikTok = **189** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p32/p90.] quote: "189 are on TikTok"
  - p75 Pizza restaurants in Chicago with YouTube channels = **151** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p33/p91.] quote: "151 have YouTube channels"
  - p76 Pizza restaurants in Chicago with LinkedIn profiles = **88** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p31/p92.] quote: "88 have LinkedIn profiles"
  - p77 Pizza restaurants in Chicago with phone numbers listed = **1,946** Pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Phone-number listing count; no bearing on pizza volume.] quote: "1946 Phone numbers"
- dropped by code checks: 10 (period_end missing or unparseable: 9; period_end 2030-12-31 after as_of: 1)

### d6 [related_series] Pizza chain sales and store-level data for Chicago market

Hypothesis: Major pizza chains' Chicago-market sales (or US system sales times Chicago population share adjusted for store density) divided by average price per pizza and pizza mass gives chain pizza volume; adding independents' share yields total. Target = chain_sales_Chicago / price * mass + independent_share_adjustment.

Queries issued by the searcher: Domino's US system sales 2024 store count 10-K; pizza chain market share Chicago independent pizzerias; Chicago pizza market size annual sales billion pizzerias number; average unit volume Domino's Pizza Hut Papa John's US franchise store sales 2024 Technomic

- `https://dominos.gcs-web.com/static-files/d4245f85-5169-45bf-a102-cf41b8fdf45e` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://s3.amazonaws.com/pmq-com-images/wp-content/uploads/2019/05/PizzaPowerDecember20161.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.chicagotribune.com/2006/12/28/second-city-digits/` -> **live_dated** (page date 2006-12-28); points raw/verified 15/0
- `https://rentechdigital.com/smartscraper/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p78 Number of Pizza restaurants in Chicago (all pizza restaurants, count of location = **1,987** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p19.] quote: "There are 1987 Pizza restaurants in Chicago as of April 1, 2026"
  - p79 Share of Chicago pizza restaurants that are single-owner operations (numerator 9 = **46** % (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p21/p22.] quote: "914 Pizza restaurants which is 46.00% of all Pizza restaurants in Chicago are single-owner operations"
  - p80 Count of Chicago pizza restaurants that are single-owner operations = **914** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p21/p66.] quote: "914 Pizza restaurants which is 46.00% of all Pizza restaurants in Chicago are single-owner operations"
  - p81 Share of Chicago pizza restaurants that are part of larger brands (numerator 107 = **54** % (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p23/p24.] quote: "the remaining 1073 which is 54.00% are part of larger brands"
  - p82 Count of Chicago pizza restaurants that are part of larger brands = **1,073** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p23/p67.] quote: "the remaining 1073 which is 54.00% are part of larger brands"
  - p83 Year-over-year change in number of Chicago pizza restaurants (2023 to 2026) = **0** % (2023-01-01..2026-04-01) [DISCARD: 0% change in restaurant count 2023-2026 is a directory artifact with no volume meaning.] quote: "which is an 0.00% increase from 2023"
  - p84 Average age of pizza restaurants in Chicago = **10** years (plus 2 months) (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p25/p68.] quote: "Average age of Pizza restaurants in Chicago is 10 years and 2 months"
  - p85 Count of Chicago pizza restaurants with their own website = **1,848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p26/p69.] quote: "About 1848 Pizza restaurants have their own website"
  - p86 Count of Chicago pizza restaurants without their own website = **139** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p27/p70.] quote: "the remaining 139 don't have their own website"
  - p87 Count of Chicago pizza restaurants with Facebook Pages = **1,048** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p28/p71.] quote: "1048 have Facebook Pages"
  - p88 Count of Chicago pizza restaurants active on Instagram = **848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p29/p72.] quote: "848 are active on Instagram"
  - p89 Count of Chicago pizza restaurants with X (Twitter) handles = **635** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p30/p73.] quote: "635 have X (formerly Twitter) handles"
  - p90 Count of Chicago pizza restaurants on TikTok = **189** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p32/p74.] quote: "189 are on TikTok"
  - p91 Count of Chicago pizza restaurants with YouTube channels = **151** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p33/p75.] quote: "151 have YouTube channels"
  - p92 Count of Chicago pizza restaurants with LinkedIn profiles = **88** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant restatement of p31/p76.] quote: "88 have LinkedIn profiles"
- dropped by code checks: 15 (period_end missing or unparseable: 15)

### d7 [shocks] Population, tourism, and price dynamics affecting 2026

Hypothesis: 2026 pizza mass depends on Chicago population trend, visitor volume, and pizza price inflation (which may suppress volume). Adjusting a 2024/2025 baseline by population growth, tourism recovery, and real price change projects 2026. Target_2026 = baseline_mass * (1 + pop_growth) * (1 + visitor_effect) * (1 + price_volume_elasticity * real_price_change).

Queries issued by the searcher: Chicago population estimate 2025 Census; Chicago tourism visitors 2025 forecast 2026; CPI food away from home 2025 2026 forecast; pizza consumption per capita United States annual pounds per person 2025; USDA ERS food price outlook 2026 food away from home forecast percent

- `https://www.census.gov/quickfacts/fact/table/US,cookcountyillinois,chicagocityillinois/VET605222` -> **dropped** (live http 403); points raw/verified -/-
- `https://cdn.choosechicago.com/uploads/2026/06/cc_2025_economic_impact_midyear_v.2.pdf` -> **live_dated** (page date 2026-06-01); points raw/verified 15/10
  - p93 Chicago total visitors (domestic & international), 2025, with growth rate = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: Kept as visitor-volume context for a small exposure adjustment.] quote: "VISITORS \| 56.8 MILLION 2.6% GROWTH"
  - p94 Chicago domestic leisure visitors, 2025 = **40,700,000** visitors (2025-01-01..2025-12-31) [keep: Kept as visitor-segment context; not a direct input.] quote: "40.7 MILLION DOMESTIC LEISURE VISITORS"
  - p95 Chicago domestic overnight visitors, 2025 = **29,200,000** visitors (2025-01-01..2025-12-31) [keep: Kept as visitor-segment context; not a direct input.] quote: "29.2 MILLION DOMESTIC OVERNIGHT VISITORS"
  - p96 Chicago domestic day-trip business visitors, 2025 = **5,700,000** visitors (2025-01-01..2025-12-31) [keep: Kept as visitor-segment context; not a direct input.] quote: "5.7 MILLION DOMESTIC DAY-TRIP BUSINESS VISITORS"
  - p97 Chicago international visitors, 2025 (8% decline) = **1,900,000** visitors (2025-01-01..2025-12-31) [keep: Kept as visitor-segment context; not a direct input.] quote: "1.9 MILLION INTERNATIONAL VISITORS"
  - p98 Chicago hotel occupancy rate, 2025 = **69.1** % (2025-01-01..2025-12-31) [keep: Kept as hotel-occupancy context; not a direct input.] quote: "OCCUPANCY \| 69.1% (1.5% GROWTH)"
  - p99 Chicago average daily hotel rooms, 2025 = **47,009** rooms (2025-01-01..2025-12-31) [keep: Kept as hotel-room context; not a direct input.] quote: "AVERAGE DAILY HOTEL ROOMS \| 47,009"
  - p100 Chicago hotel RevPAR, 2025 = **168** USD per available room (2025-01-01..2025-12-31) [keep: Kept as hotel-RevPAR context; not a direct input.] quote: "REVPAR \| $168.25 (2.1% GROWTH)"
  - p101 Chicago tourism-related jobs, 2025 = **135,360** jobs (2025-01-01..2025-12-31) [keep: Kept as tourism-employment context; not a direct input.] quote: "TOURISM RELATED JOBS \| 135,360"
  - p102 Future citywide bookings in 2025 = **65** bookings (2025-01-01..2025-12-31) [DISCARD: Count of future citywide bookings; no pizza relevance.] quote: "65 FUTURE CITYWIDE BOOKINGS IN 2025"
- `https://www.ers.usda.gov/data-products/food-price-outlook/summary-findings` -> **live_dated** (page date 2026-09-25); points raw/verified 15/8
  - p103 Year-over-year change in US food-away-from-home CPI, August 2026 vs August 2025 = **3.4** percent (2026-08-01..2026-08-31) [keep: Kept as food-away-from-home inflation context for a volume-suppression adjustment.] quote: "The food-away-from-home (restaurant and other foodservice purchases) CPI increased 0.3 percent from July 2026 to August 2026 and was 3.4 percent higher than in August 2025."
  - p104 Month-over-month change in US food-away-from-home CPI, July 2026 to August 2026 = **0.3** percent (2026-08-01..2026-08-31) [keep: Kept as monthly inflation context; not a direct input.] quote: "The food-away-from-home (restaurant and other foodservice purchases) CPI increased 0.3 percent from July 2026 to August 2026 and was 3.4 percent higher than in August 2025."
  - p105 Annual change in US food-away-from-home CPI, 2025 (historical) = **3.8** percent (2025-01-01..2025-12-31) [keep: Kept as historical inflation context; not a direct input.] quote: "Food-away-from-home prices rose by 4.1 percent in 2024 and 3.8 percent in 2025, still faster than their historical average (3.5 percent per year)."
  - p106 Annual change in US food-away-from-home CPI, 2024 (historical) = **4.1** percent (2024-01-01..2024-12-31) [keep: Kept as historical inflation context; not a direct input.] quote: "Food-away-from-home prices rose by 4.1 percent in 2024 and 3.8 percent in 2025, still faster than their historical average (3.5 percent per year)."
  - p107 Year-over-year change in US all-food CPI, August 2026 vs August 2025 = **2.7** percent (2026-08-01..2026-08-31) [keep: Kept as all-food inflation context; not a direct input.] quote: "Food prices in August 2026 were 2.7 percent higher than in August 2025."
  - p108 Year-over-year change in US all-items CPI, August 2026 vs August 2025 = **3.4** percent (2026-08-01..2026-08-31) [keep: Kept as all-items inflation context; not a direct input.] quote: "The all-items Consumer Price Index (CPI), a measure of economy-wide inflation, increased 0.3 percent from July 2026 to August 2026. It was up 3.4 percent from August 2025."
  - p109 Annual change in US all-food CPI, 2025 (historical) = **2.9** percent (2025-01-01..2025-12-31) [keep: Kept as historical inflation context; not a direct input.] quote: "Food prices rose by 2.3 percent in 2024 and 2.9 percent in 2025, slower than they had increased during 2020-23."
  - p110 Annual change in US all-food CPI, 2024 (historical) = **2.3** percent (2024-01-01..2024-12-31) [keep: Kept as historical inflation context; not a direct input.] quote: "Food prices rose by 2.3 percent in 2024 and 2.9 percent in 2025, slower than they had increased during 2020-23."
- `https://www.choosechicago.com/press-media/press-releases/choose-chicago-announces-year-end-growth-and-shares-2026-outlook-at-annual-meeting/` -> **live_dated** (page date 2026-02-10); points raw/verified 14/9
  - p111 Chicago hotel room demand (room nights filled), 2025 = **11,900,000** room nights (2025-01-01..2025-12-31) [keep: Kept as hotel-demand context; not a direct input.] quote: "Chicago filled 11.9 million room nights, 2.3% more than 2024."
  - p112 Year-over-year growth in Chicago hotel room demand, 2025 vs 2024 = **2.3** percent (2025-01-01..2025-12-31) [keep: Kept as hotel-demand growth context; not a direct input.] quote: "showing a solid 2.3% rise in hotel room demand"
  - p113 US national hotel room demand change, 2025 = **0.5** percent decline (2025-01-01..2025-12-31) [keep: Kept as national hotel-demand context; not a direct input.] quote: "While hotel room demand declined nationally by 0.5%, Chicago filled 11.9 million room nights"
  - p114 Chicago leisure hotel room demand record, 2025 = **8,200,000** room nights (2025-01-01..2025-12-31) [keep: Kept as leisure-demand context; not a direct input.] quote: "setting a new leisure hotel room demand record of 8.2 million room nights."
  - p115 Chicago hotel revenues, 2025 (record) = **2,900,000,000** USD (2025-01-01..2025-12-31) [keep: Kept as hotel-revenue context; not a direct input.] quote: "These hotel bookings generated a record $2.9 billion in hotel revenues"
  - p116 Chicago hotel RevPAR, 2025 = **168** USD per available room (2025-01-01..2025-12-31) [keep: Kept as hotel-RevPAR context; duplicate of p100.] quote: "and $168.15 in Revenue per Available Room, or "RevPAR,""
  - p117 Future citywide conventions secured by Choose Chicago sales team = **65** conventions (2025-01-01..2025-12-31) [DISCARD: Count of future conventions secured; no pizza relevance.] quote: "securing 65 future citywide conventions and 2.8 million future room nights"
  - p118 Future room nights secured by Choose Chicago sales team = **2,800,000** room nights (2025-01-01..2025-12-31) [DISCARD: Future room nights secured; forward-looking booking metric, not 2026 exposure.] quote: "securing 65 future citywide conventions and 2.8 million future room nights"
  - p119 Major conventions setting attendance records, 2025 = **12** conventions (2025-01-01..2025-12-31) [DISCARD: Count of record-attendance conventions; no pizza relevance.] quote: "Strong convention and meetings performance, with 12 major conventions setting attendance records"
- dropped by code checks: 17 (scale word 'billion' not supported by quote or table header: 1; scale word 'million' not supported by quote or table header: 1; period_end missing or unparseable: 9; period_end 2026-12-31 after as_of: 5; period_end 2027-12-31 after as_of: 1)

### d8 [own_history] Any prior estimates of Chicago or US city pizza consumption

Hypothesis: If any published estimate of pizza consumed in Chicago or a comparable city exists (e.g., 'Chicago eats X pizzas per day'), it anchors the estimate directly; otherwise comparable-city estimates (New York, Los Angeles) scaled by population and pizza-culture adjustment serve as a cross-check. Target = comparable_city_mass * (Chicago_pop / city_pop) * culture_adjustment.

Queries issued by the searcher: how many pizzas does Chicago eat per day; pizzas sold per day Chicago estimate; "pizzas per day" New York City number of pizzas eaten estimate; Americans eat pizzas per day industry statistics slices per capita per year

- `https://www.chicagotribune.com/1988/03/24/ingredients-of-a-great-food-town-3/` -> **live_dated** (page date 2021-08-08); points raw/verified 2/2
  - p120 Chicago per-capita pizza meals per year (1986 survey) = **34.8** pizza meals per person per year (1986-01-01..1986-12-31) [keep: Kept as the 1986 Chicago pizza-meal rate; usable only with a large transfer assumption.] quote: "Chicagoans were named the nation`s biggest pizza fans in a 1986 survey that has us sitting down to pizza 34.8 times a year."
  - p121 Los Angeles per-capita pizza meals per year (1986 survey) = **20** pizza meals per person per year (upper bound, stated as less (1986-01-01..1986-12-31) [keep: Kept as the 1986 LA comparison; context for the culture adjustment.] quote: "Los Angeles, the home of designer pizzas, averaged less than 20 per capita pizza meals annually."
- `https://southfloridareporter.com/over-500000-pizzas-are-eaten-in-one-day-in-nyc/` -> **live_dated** (page date 2023-10-11); points raw/verified 15/4
  - p122 US mozzarella production in 2021 = **4,490,000,000** pounds of mozzarella (2021-01-01..2021-12-31) [keep: Kept as a national mozzarella supply bound; not a consumption measure.] quote: "In 2021, around 4.49 billion pounds of mozzarella were produced in the United States."
  - p123 Number of pizzerias in the United States as of 2022 = **80,000** pizzerias (2022-01-01..2022-12-31) [keep: Kept as national pizzeria-count context; not a direct input.] quote: "There were approximately 80,000 pizzerias in the United States, as of 2022."
  - p124 Number of pizzerias in the United States in 2021 = **75,000** pizzerias (2021-01-01..2021-12-31) [keep: Kept as national pizzeria-count context; not a direct input.] quote: "In 2021 that number shrank to 75,000."
  - p125 US pepperoni consumption as of 2019 (commonly cited figure) = **650,000,000** pounds of pepperoni (2019-01-01..2019-12-31) [keep: Kept as national pepperoni context; not a direct input.] quote: "Do the math, and that's more than 650 million pounds of pepperoni as of 2019."
- `https://chicago.eater.com/2012/5/11/6587185/by-the-numbers-roots-giordanos-lou-malnatis` -> **live_dated** (page date 2012-05-11); points raw/verified 15/1
  - p126 Giordano's pizzas shipped nationwide in 2011 = **26,888** pizzas shipped nationwide in 2011 (2011-01-01..2011-12-31) [DISCARD: Giordano's nationwide shipped pizzas (2011) is a mail-order figure, not Chicago consumption.] quote: "Number of pizzas shipped nationwide in 2011: 26,888"
- `https://chicago.eater.com/2014/3/20/6260173/pizza-by-the-numbers-dimos-bar-toma-and-ranallis` -> **live_dated** (page date 2014-03-20); points raw/verified 15/15
  - p127 Dimo's Pizza slices sold in a month = **29,760** slices (2014-01-01..2014-12-31) [keep: Kept as a 2014 single-pizzeria slice-throughput observation; small-sample.] quote: "Number of slices sold: 29760"
  - p128 Dimo's Pizza pounds of dough used in a month = **24,000** pounds of dough (2014-01-01..2014-12-31) [keep: Kept as a 2014 dough-use observation; useful for pizza-mass conversion.] quote: "Pounds of dough: 24000"
  - p129 Dimo's Pizza pounds of mozzarella used in a month = **7,056** pounds of mozzarella (2014-01-01..2014-12-31) [keep: Kept as a 2014 mozzarella-use observation; useful for ingredient-fraction conversion.] quote: "Pounds of Mozzarella: 7056"
  - p130 Ranalli's pizzas per week (lower bound) = **1,200** pizzas per week (2014-01-01..2014-12-31) [keep: Kept as a 2014 per-pizzeria weekly throughput observation; small-sample.] quote: "Pizzas per week: 1200 - 1500"
  - p131 Ranalli's pizzas per week (upper bound) = **1,500** pizzas per week (2014-01-01..2014-12-31) [DISCARD: Upper bound of the same Ranalli's weekly range as p130; keep p130 as the central weekly figure.] quote: "Pizzas per week: 1200 - 1500"
  - p132 Ranalli's pizzas per month = **5,000** pizzas per month (2014-01-01..2014-12-31) [keep: Kept as a 2014 per-pizzeria monthly throughput observation; small-sample.] quote: "Pizzas per month: 5000"
  - p133 Ranalli's Thin Crust pizzas sold in a month = **3,000** pizzas (2014-01-01..2014-12-31) [DISCARD: Ranalli's thin-crust monthly count is a subcomponent of p132; redundant for throughput.] quote: "Thin Crust: 3000"
  - p134 Ranalli's Chicago Stuffed pizzas sold in a month = **525** pizzas (2014-01-01..2014-12-31) [DISCARD: Ranalli's stuffed-pizza monthly count is a subcomponent of p132; redundant.] quote: "Chicago Stuffed: 525"
  - p135 Ranalli's Pan Pizza sold in a month = **350** pizzas (2014-01-01..2014-12-31) [DISCARD: Ranalli's pan-pizza monthly count is a subcomponent of p132; redundant.] quote: "Pan Pizza: 350"
  - p136 Ranalli's Double Deckers sold in a month = **200** pizzas (2014-01-01..2014-12-31) [DISCARD: Ranalli's double-decker monthly count is a subcomponent of p132; redundant.] quote: "Double Deckers: 200"
  - p137 Ranalli's Gluten Free pizzas sold in a month = **175** pizzas (2014-01-01..2014-12-31) [DISCARD: Ranalli's gluten-free monthly count is a subcomponent of p132; redundant.] quote: "Gluten Free: 175"
  - p138 Ranalli's pounds of cheese used in a week = **600** pounds of cheese (2014-01-01..2014-12-31) [keep: Kept as a 2014 cheese-use observation; useful for ingredient-fraction conversion.] quote: "Pounds of cheese: 600"
  - p139 Bar Toma pounds of fior di latte from Wisconsin used in a month = **2,400** pounds of fior di latte (2014-01-01..2014-12-31) [keep: Kept as a 2014 cheese-use observation; useful for ingredient-fraction conversion.] quote: "Pounds of fior di latte from Wisconsin: 2,400"
  - p140 Bar Toma gallons of tomato sauce used in a month = **300** gallons of tomato sauce (2014-01-01..2014-12-31) [keep: Kept as a 2014 sauce-use observation; useful for ingredient-fraction conversion.] quote: "Gallons of tomato sauce: 300"
  - p141 Bar Toma pounds of Imported Italian flour used in a month = **5,000** pounds of flour (2014-01-01..2014-12-31) [keep: Kept as a 2014 flour-use observation; useful for pizza-mass conversion.] quote: "Pounds of Imported Italian flour: 5,000"
- dropped by code checks: 25 (period_end missing or unparseable: 22; number: no number in value_as_written: 3)

### b1 [related_series] Chicago pizza demand

Hypothesis: A city-specific per-capita pizza consumption or pizza-spend figure (e.g., from a Chicago restaurant association, Technomic/Datassential Chicago market report, or a Chicago Tribune/NBC 'Chicago eats X pizzas a day' feature) would anchor d1/d8 directly and replace the 1986 meal-rate transfer, which is the largest single uncertainty in the per-capita route.

Queries issued by the searcher: Chicago how many pizzas eaten per day Chicago Tribune; Technomic Chicago pizza market report sales; Chicago pizza industry annual sales billion "Chicago" pizzas sold per year statistic; "Chicago" "pizzas" "per day" estimate number eaten city

- `https://www.chicagotribune.com/2006/12/28/second-city-digits/` -> **live_dated** (page date 2006-12-28); points raw/verified 15/0
- `https://www.chicagotribune.com/1988/03/24/ingredients-of-a-great-food-town-3/` -> **live_dated** (page date 2021-08-08); points raw/verified 2/2
  - p142 Chicago per-capita pizza meals per year (1986 survey) = **34.8** pizza meals per person per year (1986-01-01..1986-12-31) [keep: Kept as the 1986 Chicago pizza-meal rate; duplicate of p120.] quote: "Chicagoans were named the nation`s biggest pizza fans in a 1986 survey that has us sitting down to pizza 34.8 times a year."
  - p143 Los Angeles per-capita pizza meals per year (comparison, 1986 survey) = **20** pizza meals per person per year (upper bound, stated as 'les (1986-01-01..1986-12-31) [keep: Kept as the 1986 LA comparison; duplicate of p121.] quote: "Los Angeles, the home of designer pizzas, averaged less than 20 per capita pizza meals annually."
- `https://www.technomic.com/press-technomic-assesses-the-pizza-category-across-away-home-home-channels/` -> **live_dated** (page date 2026-10-09); points raw/verified 3/3
  - p144 Share of all consumer pizza spending through foodservice operators (US, Technomi = **86** % of consumer pizza spending (2023-01-01..2023-12-31) [keep: Kept as the foodservice share of pizza spend; supports a spend-based decomposition.] quote: "86% of all consumer spending on pizza is through foodservice operators, while only 14% of spending is with retailers"
  - p145 Share of all consumer pizza spending with retailers (US, Technomic) = **14** % of consumer pizza spending (2023-01-01..2023-12-31) [keep: Kept as the retail share of pizza spend; supports a spend-based decomposition.] quote: "86% of all consumer spending on pizza is through foodservice operators, while only 14% of spending is with retailers"
  - p146 Share of pizza-menu operators saying pizza is important to business success (US, = **86** % of operators menuing pizza (2023-01-01..2023-12-31) [keep: Kept as operator context; not a direct input.] quote: "86% of operators menuing pizza contend that pizza is important to the success of their business"
- `http://www.restaurantnews.com/pizza-occasions-grow-with-key-sales-drivers-including-innovation-convenience-and-versatility-finds-technomic/` -> **live_dated** (page date 2012-04-11); points raw/verified 8/0
- dropped by code checks: 23 (period_end missing or unparseable: 23)

### b2 [base_rates] per-establishment throughput

Hypothesis: A recent average weekly pizza volume per Chicago pizzeria (or per chain store vs independent) would convert the 1,987-location count (p19) into daily pizzas, unlocking the d3 capacity route with current rather than 2014 data. The 2014 Eater figures (p130, p132) are the only throughput evidence and are a decade old and small-sample.

Queries issued by the searcher: Chicago pizzeria average pizzas sold per week 2024; pizza restaurant unit volume average weekly sales US per store; Grubhub Chicago pizza orders per day statistics; "pizzas per week" pizzeria average Chicago 2023

- `https://pos.toasttab.com/zh-us/blog/on-the-line/how-much-do-pizza-shops-make` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.researchandmarkets.com/reports/5292834/state-of-the-industry-pizza-in-the-u-s-12th` -> **live_dated** (page date 2026-01-01); points raw/verified 0/0
- `https://finance.yahoo.com/news/why-mountain-mike-doesn-t-085600608.html` -> **live_dated** (page date 2025-05-13); points raw/verified 15/12
  - p147 Mountain Mike's Pizza restaurant count when bought by St. Geme and Britt (2017) = **170** restaurants (2017-01-01..2017-12-31) [keep: Kept as chain-growth context; not a direct input.] quote: "When Ed St. Geme and Chris Britt bought Mountain Mike's Pizza in 2017, the chain had about 170 restaurants across California"
  - p148 Mountain Mike's Pizza restaurant count surpassed (prior year) = **300** restaurants (2024-01-01..2024-12-31) [keep: Kept as chain-growth context; not a direct input.] quote: "Last year, Mountain Mike's surpassed 300 restaurants and is now working toward 350."
  - p149 Mountain Mike's Pizza target restaurant count = **350** restaurants (..) [keep: Kept as chain-growth context; not a direct input.] quote: "Last year, Mountain Mike's surpassed 300 restaurants and is now working toward 350."
  - p150 Expected US pizza segment sales this year (forecast) = **50,000,000,000** USD sales (..) [keep: Kept as a national pizza-segment sales forecast; requires Chicago allocation and price/mass conversion.] quote: "he expects the pizza segment will generate $50 billion in sales this year"
  - p151 Mountain Mike's average unit volumes (2024) = **1,100,000** USD per unit (2024-01-01..2024-12-31) [keep: Kept as a chain AUV benchmark; context for per-store throughput.] quote: "Average unit volumes: $1.1 million (2024)"
  - p152 Mountain Mike's states in operation = **10** states (..) [keep: Kept as chain-footprint context; not a direct input.] quote: "Where in operation: 10 states with plans to reach 15 states"
  - p153 Mountain Mike's planned states of operation = **15** states (..) [keep: Kept as chain-footprint context; not a direct input.] quote: "Where in operation: 10 states with plans to reach 15 states"
  - p154 Mountain Mike's current unit count (over) = **300** restaurants (..) [keep: Kept as chain-footprint context; not a direct input.] quote: "Current unit count: Over 300"
  - p155 Mountain Mike's restaurants opened in 2024 = **21** restaurants (2024-01-01..2024-12-31) [keep: Kept as chain-growth context; not a direct input.] quote: "In 2024, the brand opened 21 restaurants - its highest annual total of new units nationwide"
  - p156 Mountain Mike's expected locations by end of current year (forecast) = **330** locations (..) [keep: Kept as chain-growth context; not a direct input.] quote: "Metevier said he expects the chain to reach roughly 330 locations by the end of this year."
  - p157 Mountain Mike's units added to development pipeline = **40** restaurants (..) [keep: Kept as chain-growth context; not a direct input.] quote: "The company added 40 additional units to its development pipeline, including a 10-restaurant deal in Florida."
  - p158 Mountain Mike's total locations in development pipeline = **140** locations (..) [keep: Kept as chain-growth context; not a direct input.] quote: "The chain now has 140 locations in the pipeline"
- `https://www.nbcchicago.com/news/local/grubhub-pizza-orders-chicago/2050128/` -> **dropped** (live fetch error IncompleteRead); points raw/verified -/-
- dropped by code checks: 3 (number: no number in value_as_written: 3)

### b3 [related_series] average pizza mass

Hypothesis: The per-capita and establishment routes both need an average pizza mass (grams per whole pizza or per slice) for Chicago-style thin, deep-dish, and stuffed pizzas. A sourced average pizza weight or dough-ball weight would convert pizza counts to tonnes and is currently the weakest conversion factor.

Queries issued by the searcher: Chicago deep dish pizza weight grams; Giordano's deep dish pizza weight pounds; Chicago thin crust pizza weight ounces 14 inch tavern style; pizza dough ball weight ounces 14 inch pizza dough weight per pizza

- `https://www.harryanddavid.com/h/gourmet-foods/entrees/37710` -> **live_dated** (page date 2026-07-22); points raw/verified 6/0
- `https://www.costco.com/p/-/giordanos-chicago-frozen-10-deep-dish-stuffed-pizza-3-pack/100974087` -> **live_dated** (page date 2024-05-02); points raw/verified 13/0
- `https://www.instacart.com/products/16771814-ginos-east-pizza-thin-crust-meaty-legend-27-oz` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://the-kitchencoalition.com/wprm_print/chicago-thin-crust-pizza-crispy-tavern-style` -> **live_dated** (page date 2026-10-01); points raw/verified 15/0
- dropped by code checks: 34 (number: more than one number in value_as_written: 4; period_end missing or unparseable: 26; value_as_written not in quote as a whole number: 4)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['pizza consumption', 'chicago food', 'pizza sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p19', 'p20', 'p63', 'p78'] Same rentechdigital listing count of 1,987 Chicago pizza restaurants as of 2026-04-01, repeated across directions; one underlying measurement, not four independent confirmations.
- corroborating: ['p21', 'p22', 'p64', 'p66', 'p79', 'p80'] Single-owner count 914 = 46% of 1,987; same source, internally consistent, one measurement.
- corroborating: ['p23', 'p24', 'p65', 'p67', 'p81', 'p82'] Brand-affiliated count 1,073 = 54% of 1,987; same source, complements the single-owner split.
- corroborating: ['p26', 'p27', 'p69', 'p70', 'p85', 'p86'] Website presence split 1,848/139; same listing database, adds no independent information about pizza volume.
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92'] Social-media and phone presence counts from the same listing scrape; descriptive of the directory, not of throughput.
- corroborating: ['p25', 'p68', 'p84'] Average restaurant age ~10 years 2 months, repeated; same source.
- corroborating: ['p34', 'p35'] USDA/WWEIA NHANES 2017-March 2020: 11-12% of the US population eats pizza on any given day; the two figures are the same survey with slightly different age framing.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41'] Meal-occasion and snack shares of pizza intake from the same NHANES analysis; consistent internal breakdown.
- corroborating: ['p42', 'p43', 'p44'] Source-of-pizza shares (restaurant 56%, grocery 26%, school 12%, other 6%) from the same NHANES analysis; sums to 100%.
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62'] US per-capita cheese series from USDA ERS-derived reporting; 2024 total 48 lb, natural 39.9 lb, mozzarella 12.5 lb. Different vintages (cheesemarketnews vs newsbreak) but same underlying ERS data; tre
- corroborating: ['p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119'] Choose Chicago 2025 tourism metrics; 56.8M visitors, 11.9M room nights, 69.1% occupancy. Same source family, mutually consistent; useful for visitor exposure but not for pizza mass directly.
- corroborating: ['p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110'] USDA ERS CPI series: food-away-from-home +3.4% y/y Aug 2026, +3.8% 2025, +4.1% 2024; all-food +2.7% Aug 2026. Consistent inflation context for a price/volume adjustment.
- corroborating: ['p120', 'p121'] 1986 survey: Chicago 34.8 pizza meals/person/year vs LA <20; supports a Chicago pizza-culture premium over national norms, but is 40 years old and measures meals not mass.
- corroborating: ['p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139', 'p140', 'p141'] Chicago pizzeria operating statistics (2011-2014): Ranalli's ~1,200-1,500 pizzas/week, Dimo's 29,760 slices/month, Bar Toma ingredient flows. Same Eater Chicago feature; useful for per-establishment t
- corroborating: ['p122', 'p123', 'p124', 'p125'] US mozzarella production 4.49B lb (2021), ~80,000 pizzerias (2022), 650M lb pepperoni (2019); same secondary article, national context only.
- corroborating: ['p1', 'p2', 'p3', 'p4'] US pizza-chain sales $31B (2024) and restaurant-count peak in 2019; same Hindustan Times/Technomic-Datassential article. p2/p3 are CPK sale prices, not pizza volume.
- corroborating: ['p5', 'p6', 'p7', 'p8', 'p9'] National Restaurant Association Illinois/MSA employment and sales figures; same source, different geographies (MSA vs state) and segments.
- corroborating: ['p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18'] US restaurant industry 2025 growth and chain-share figures from one Chinese-language summary of industry data; internally consistent.
- conflicting: ['p19', 'p120'] Not a true contradiction: 1,987 listed pizza restaurants in the city vs a 1986 per-capita meal rate. The listing count is a directory count (may include non-pizza-primary venues, chains, and closed/du
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p19', 'p21', 'p23', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p66'] All from the same rentechdigital business-listing snapshot (April 2026); they are internally consistent partitions of one 1,987-location count, not independent measurements. Useful as a current establ
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p43', 'p44'] All from the same USDA/ARS NHANES 2017-March 2020 pizza intake analysis. p34 and p35 are two renderings of the same 'share eating pizza on a given day' statistic (11% vs 12%); they are not independent
- corroborating: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62'] USDA ERS-derived cheese consumption figures from two secondary write-ups. p47/p48 (39.9/39.5 lb) and p50/p52/p61 (48.0/39.9/39.5 lb) are consistent once natural vs total cheese is distinguished; p45/p
- corroborating: ['p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116'] Choose Chicago 2025 tourism statistics from two snapshots; p100 and p116 are the same RevPAR figure. They describe visitor volume and hotel demand, relevant only as a small exposure adjustment for non
- corroborating: ['p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110'] USDA ERS CPI figures. Food-away-from-home inflation (3.4% YoY Aug 2026, 3.8% in 2025) is a price signal that could modestly suppress real pizza volume; it is contextual, not a pizza quantity.
- corroborating: ['p120', 'p121', 'p142', 'p143'] p120 and p142 are the same 1986 Chicago Tribune survey figure (34.8 pizza meals/person/yr); p121 and p143 are the same Los Angeles comparison. One underlying survey, four decades old, with 'pizza meal
- corroborating: ['p127', 'p128', 'p129', 'p130', 'p132', 'p138', 'p139', 'p140', 'p141'] 2014 Eater Chicago pizzeria operating statistics. p130 (1,200-1,500/week) and p132 (5,000/month) are roughly consistent (~1,150/week implied). These are small-sample, decade-old, single-establishment 
- corroborating: ['p1', 'p150', 'p151', 'p144', 'p145'] US pizza market size and structure: Technomic $31B chain sales (2024), a ~$50B pizza-segment forecast, Mountain Mike's $1.1M AUV, and 86/14 foodservice/retail spend split. These are national and partl
- corroborating: ['p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18'] Restaurant-industry employment and sales-growth statistics for the Chicago MSA and Illinois. They are MSA/state scope, not city of Chicago, and describe all restaurants, not pizza; only weakly usable 
- corroborating: ['p122', 'p123', 'p124', 'p125'] National mozzarella production, pizzeria counts, and pepperoni consumption from one secondary article. Mozzarella production (p122) is a supply-side bound, not consumption; pizzeria counts (p123/p124)
- corroborating: ['p147', 'p148', 'p149', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158'] Mountain Mike's chain growth details from one article; a single regional chain, not representative of Chicago pizza volume. Contextual only.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Chicago city population, 2026 | 2,700,000 | 2,600,000..2,800,000 | 1,907,878..3,815,757 (widened) | people | m1 (m1), m2 (m2) | City of Chicago population is roughly 2.7M in recent Census estimates; no kept point supplies it, so it is assumed with a modest range reflecting migration uncertainty. | Target is the city of Chicago, not the metro area. | A Census 2026 city population estimate outside the range. |
| a2 | Average pizza mass per pizza meal | 0.35 | 0.2..0.55 | 0.2..0.55 | kg per pizza meal | m1 (m1) | A pizza meal is typically 2-3 slices of a ~2.5-3 kg whole pizza or a personal pizza; 0.35 kg is central with a wide range covering thin-crust slices and deep-dish portions. No kept point gives a direct per-meal mass. | Used to convert pizza-meal counts to mass. | A sourced average slice or whole-pizza weight implying a materially different per-meal mass. |
| a3 | Chicago pizza-culture adjustment to the 1986 meal rate | 1 | 0.7..1.4 | 0.7..1.4 | dimensionless | m1 (m1) | The 1986 survey already ranked Chicago highest; the adjustment covers four decades of change in eating patterns and whether the 1986 rate still holds. Centered at 1 with a wide range. | Used to transfer the 1986 Chicago pizza-meal rate to 2026. | Modern Chicago-specific pizza-frequency survey data showing a materially different rate. |
| a4 | Chicago adjustment to national daily pizza-eater share | 1.15 | 0.9..1.5 | 0.8216..1.643 (widened) | dimensionless | m2 (m2) | Chicago's dense pizza culture and restaurant supply suggest a modestly above-national daily eater share; centered slightly above 1 with a wide range. | Used to transfer the national NHANES daily pizza-eater share to Chicago. | Chicago-specific consumption-frequency data near or below the national average. |
| a5 | Average servings per pizza eater per day | 1.3 | 1..1.8 | 0.9487..1.897 (widened) | servings per eater per day | m2 (m2) | Most pizza eaters have one pizza occasion per day, some have two; 1.3 is a central value with a range. | Used with the daily eater share to get daily servings per capita. | Dietary-recall data showing a materially different servings-per-eater rate. |
| a6 | Average pizza serving mass | 0.15 | 0.1..0.25 | 0.1..0.25 | kg per serving | m2 (m2) | A serving is roughly one to two slices; 0.15 kg is a central value with a wide range. | Used to convert daily servings to mass. | A sourced average slice weight implying a materially different serving mass. |
| a7 | Average pizzas sold per Chicago pizzeria per day | 60 | 30..120 | 30..120 | pizzas per establishment per day | m3 (m3) | The 2014 Eater figures (p130, p132) imply roughly 160-215 pizzas/week at two busy establishments (~25-30/day); a citywide average across 1,987 listings including low-volume venues is plausibly higher in count but lower per store; 60/day is central with a wide range. | Used with the establishment count to estimate daily pizza throughput. | A current Chicago per-pizzeria volume survey outside the range. |
| a8 | Average whole-pizza mass | 1 | 0.6..1.6 | 0.6..1.6 | kg per pizza | m3 (m3) | Chicago thin, deep-dish, and stuffed pizzas vary widely; 1.0 kg is a central whole-pizza mass with a wide range. | Used to convert pizza counts to mass. | A sourced average Chicago pizza weight outside the range. |
| a9 | Share of Chicago pizza mass from non-establishment (home/frozen/retail) sources | 0.2 | 0.1..0.35 | 0.1..0.35 | fraction | m3 (m3) | Technomic reports 14% of pizza spend is retail (p145); mass share is likely somewhat higher because retail pizza is cheaper per kg; 0.2 is central. | Used to gross up establishment throughput to all pizza consumption. | Chicago-specific data showing a materially different retail/home share. |
| a10 | Chicago share of US pizza-segment sales | 0.008 | 0.005..0.012 | 0.005..0.012 | fraction | m4 (m4) | Chicago city population is ~0.8% of the US; pizza culture may push its share slightly above population share; 0.008 is central. | Used to allocate national pizza-segment sales to Chicago. | Chicago-specific pizza-sales data implying a materially different share. |
| a11 | Average price per kg of pizza | 12 | 8..18 | 8..18 | USD per kg | m4 (m4) | Pizza prices per kg vary by type and channel; $12/kg is central and consistent with typical per-pizza prices and masses. | Used to convert pizza spend to mass. | Sourced average pizza price per kg outside the range. |
| a12 | Visitor/commuter exposure adjustment to resident pizza mass | 1.05 | 1..1.15 | 0.7583..1.517 (widened) | dimensionless | m1 (m1), m2 (m2) | Chicago has substantial visitors and commuters (p93, p95) who eat pizza in the city; a modest uplift over resident-only mass is plausible. | Used to adjust resident-based estimates for non-resident eating in Chicago. | Evidence that visitors/commuters contribute negligibly or substantially more. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 90.78 | ['p120'] / ['a1', 'a12', 'a2', 'a3'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 78.38 | ['p34'] / ['a1', 'a12', 'a4', 'a5', 'a6'] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 141 | ['p19'] / ['a7', 'a8', 'a9'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 88.53 | ['p150'] / ['a10', 'a11'] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **97.13** t/day, 80% interval [40.01, 236] t/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-12-31, after as_of: it cannot have been published yet


## Final answer

The best estimate is 97.13 t/day (80% model-based interval 40.01 to 236 t/day) for total pizza mass consumed by people in the city of Chicago on an average day in calendar year 2026, covering restaurant, takeout, delivery, and home-prepared pizza.

Four routes were averaged with equal weights: a per-capita pizza-meal route anchored on 34.8 pizza meals per person per year from a [n] Chicago survey; a base-rate route using 11 percent of population from NHANES; a capacity route built on 1,987 pizza restaurants; and a spend route using 50,000,000,000 USD sales. Only these points are observed; population, per-meal and serving mass, per-store volume, whole-pizza mass, retail share, price per kg, and visitor adjustments are all analyst assumptions, and the [n] and national figures require transfers to Chicago in 2026.

The interval reflects input uncertainty only, not demonstrated accuracy. The biggest risk is the undefined [n] 'pizza meal' and its four-decade transfer, plus per-meal mass. Better evidence would be a current Chicago-specific pizza consumption or sales survey.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Chicago city population, 2026: 2,700,000 people, range 1,907,878 to 3,815,757 (range widened by code); used by m1, m2. Overturned by: A Census 2026 city population estimate outside the range.
- a2 Average pizza mass per pizza meal: 0.35 kg per pizza meal, range 0.2 to 0.55; used by m1. Overturned by: A sourced average slice or whole-pizza weight implying a materially different per-meal mass.
- a3 Chicago pizza-culture adjustment to the [n] meal rate: 1 dimensionless, range 0.7 to 1.4; used by m1. Overturned by: Modern Chicago-specific pizza-frequency survey data showing a materially different rate.
- a4 Chicago adjustment to national daily pizza-eater share: 1.15 dimensionless, range 0.8216 to 1.643 (range widened by code); used by m2. Overturned by: Chicago-specific consumption-frequency data near or below the national average.
- a5 Average servings per pizza eater per day: 1.3 servings per eater per day, range 0.9487 to 1.897 (range widened by code); used by m2. Overturned by: Dietary-recall data showing a materially different servings-per-eater rate.
- a6 Average pizza serving mass: 0.15 kg per serving, range 0.1 to 0.25; used by m2. Overturned by: A sourced average slice weight implying a materially different serving mass.
- a7 Average pizzas sold per Chicago pizzeria per day: 60 pizzas per establishment per day, range 30 to 120; used by m3. Overturned by: A current Chicago per-pizzeria volume survey outside the range.
- a8 Average whole-pizza mass: 1 kg per pizza, range 0.6 to 1.6; used by m3. Overturned by: A sourced average Chicago pizza weight outside the range.
- a9 Share of Chicago pizza mass from non-establishment (home/frozen/retail) sources: 0.2 fraction, range 0.1 to 0.35; used by m3. Overturned by: Chicago-specific data showing a materially different retail/home share.
- a10 Chicago share of US pizza-segment sales: 0.008 fraction, range 0.005 to 0.012; used by m4. Overturned by: Chicago-specific pizza-sales data implying a materially different share.
- a11 Average price per kg of pizza: 12 USD per kg, range 8 to 18; used by m4. Overturned by: Sourced average pizza price per kg outside the range.
- a12 Visitor/commuter exposure adjustment to resident pizza mass: 1.05 dimensionless, range 0.7583 to 1.517 (range widened by code); used by m1, m2. Overturned by: Evidence that visitors/commuters contribute negligibly or substantially more.

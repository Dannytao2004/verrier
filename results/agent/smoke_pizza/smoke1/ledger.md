# Evidence ledger: smoke_pizza

- Question: How many tonnes of pizza do people in Chicago eat on an average day in 2026?
- as_of: 2026-10-17
- Pinned target: Total mass of pizza consumed by people in Chicago (city of Chicago, Illinois) on an average day in calendar year 2026, counting all pizza eaten by residents and visitors within the city, including restaurant/takeout/delivery pizza and any pizza prepared at home from purchased or homemade pizza, meas | unit metric tons per day | period 2026-01-01..2026-12-31 | publisher No official publisher; analyst-constructed estimate

## Directions and pages

### d1 [related_series] Industry analyst / restaurant sales data

Hypothesis: Chicago foodservice pizza sales (USD) divided by average price per pizza/unit and converted to mass via average pizza weight gives foodservice pizza mass; foodservice is expected to be the dominant share (~70-85%) of total pizza consumption. Transfer assumption: city-level pizza sales can be approximated by national per-capita pizza sales scaled to Chicago population, or by Chicago-specific restaurant sales data.

Queries issued by the searcher: US pizza industry annual sales 2025 billion pizza restaurants; number of pizzerias Chicago pizza restaurants count; average pizza weight grams whole 14-inch pie how many grams; pizza consumption per capita United States pounds per year pizza

- `https://img1.ibisworld.com/united-states/industry/pizza-restaurants/4320/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://in.investing.com/news/stock-market-news/whos-winning-the-pizza-race-5443558` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://platelens.app/blog/how-many-calories-in-a-slice-of-pizza` -> **live_dated** (page date 2026-09-06); points raw/verified 15/0
- `https://foodeist.com/index.php/pizza-statistics` -> **live_dated** (page date 2026-03-10); points raw/verified 12/0
- dropped by code checks: 27 (period_end missing or unparseable: 27)

### d2 [base_rates] Consumer survey / dietary intake

Hypothesis: Per-capita pizza consumption frequency (meals/servings per person per week) times average mass per serving times population present in Chicago gives total daily mass. Transfer assumption: national dietary intake frequencies (e.g., NHANES pizza consumption prevalence) apply to Chicago, adjusted for Chicago's pizza culture possibly raising frequency.

Queries issued by the searcher: NHANES pizza consumption frequency percent of adults eat pizza on a given day; average pizza serving size grams Americans per capita pizza consumption study; Chicago population 2026 estimate Census Bureau 2.7 million city of Chicago; "pizza" NHANES percentage consumed pizza on any given day average grams per eating occasion 2017-2020

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/8
  - p1 Share of US population (2+ years) consuming pizza on any given day, overall = **11** % of population (2017-01-01..2020-03-31) [keep: ] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p2 Share of US population consuming pizza on any given day, older adults 60+ = **6** % of population (2017-01-01..2020-03-31) [keep: ] quote: "the percentage consuming decreased to about 6% among older adults (60+)."
  - p3 Share of pizza consumed at lunch and dinner combined (children and adults) = **90** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Almost 90% of pizza was consumed at lunch and dinner."
  - p4 Share of pizza intake at lunch, children 2-19 years = **41** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p5 Share of pizza intake at dinner, children 2-19 years = **48** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p6 Share of pizza intake from snacks = **4** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Snacks accounted for 4% of pizza intake."
  - p7 Share of pizza obtained from 'Other' sources = **6** % of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources such as a sport or entertainment facility or a convenience store"
  - p8 Share of pizza contribution to total daily energy intake among pizza consumers,  = **27** % of total energy intake (2017-01-01..2020-03-31) [keep: ] quote: "Overall, pizza contributed about 27% to total energy intake of pizza consumers on the intake day."
- `https://faseb.onlinelibrary.wiley.com/doi/10.1096/fasebj.30.1_supplement.lb407` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.census.gov/quickfacts/fact/dashboard/chicagocityillinois/PST045218` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.wlsam.com/2026/05/18/chicagos-population-grew-to-2-73m-people-in-2025-per-latest-estimate/` -> **live_dated** (page date 2026-05-18); points raw/verified 15/15
  - p9 Chicago city population estimate, 2025 (Census Bureau) = **2,731,585** people (2025-01-01..2025-12-31) [keep: ] quote: "- 2025: 2,731,585"
  - p10 Chicago city population estimate, 2024 (Census Bureau) = **2,726,332** people (2024-01-01..2024-12-31) [keep: ] quote: "- 2024: 2,726,332"
  - p11 Chicago city population estimate, 2023 (Census Bureau) = **2,698,758** people (2023-01-01..2023-12-31) [keep: ] quote: "- 2023: 2,698,758"
  - p12 Chicago city population estimate, 2022 (Census Bureau) = **2,680,609** people (2022-01-01..2022-12-31) [keep: ] quote: "- 2022: 2,680,609"
  - p13 Chicago city population estimate, 2021 (Census Bureau) = **2,705,934** people (2021-01-01..2021-12-31) [keep: ] quote: "- 2021: 2,705,934"
  - p14 Chicago city population estimate, 2020 (Census Bureau) = **2,741,640** people (2020-01-01..2020-12-31) [keep: ] quote: "- 2020: 2,741,640"
  - p15 Chicago population growth 2025 vs previous year (increase) = **5,000** people (2024-01-01..2025-12-31) [keep: ] quote: "The City of Chicago's population grew to more than 2.73 million people in 2025, an increase of more than 5,000 since the previous year"
  - p16 Chicago population decline 2020 to 2022 (decrease) = **67,700** people (2020-04-01..2022-12-31) [keep: ] quote: "by 2022, the population had fallen to around 2.68 million, a decline of more than 67,700 residents"
  - p17 Chicago population added in three years after 2022 = **51,000** people (2022-01-01..2025-12-31) [keep: ] quote: "In the three years afterwards, the city appears to have added nearly 51,000 people."
  - p18 Chicago population estimate, April 1 2020 Census = **2,740,000** people (2020-04-01..2020-04-01) [keep: ] quote: "The city's population was estimated to be around 2.74 million on April 1, 2020"
  - p19 Chicago population estimate, 2025 (headline, more than) = **2,730,000** people (2025-01-01..2025-12-31) [DISCARD: Rounded headline duplicate of p9; p9 gives the precise 2025 figure.] quote: "The City of Chicago's population grew to more than 2.73 million people in 2025"
  - p20 New York City population estimate (comparison city) = **8,584,629** people (2025-01-01..2025-12-31) [keep: ] quote: "- New York City: 8,584,629"
  - p21 Los Angeles population estimate (comparison city) = **3,869,089** people (2025-01-01..2025-12-31) [keep: ] quote: "- Los Angeles: 3,869,089"
  - p22 Houston population estimate (comparison city) = **2,397,315** people (2025-01-01..2025-12-31) [keep: ] quote: "- Houston: 2,397,315"
  - p23 Minimum city population threshold included in Census estimates = **20,000** people (..) [keep: ] quote: "The Census Bureau's estimates included cities with populations of at least 20,000."
- dropped by code checks: 7 (value_as_written not in quote as a whole number: 6; number: more than one number in value_as_written: 1)

### d3 [capacity_consumption] Pizzeria operator / throughput

Hypothesis: Number of pizzerias in Chicago times average daily pizzas sold per pizzeria times average pizza mass gives foodservice pizza mass. Transfer assumption: average daily pizza output per pizzeria can be benchmarked from industry averages or comparable cities.

Queries issued by the searcher: how many pizza restaurants in Chicago; average pizzas sold per pizzeria per day industry benchmark; 3 billion pizzas sold annually United States 75,000 pizzerias per day average; PMQ Pizza Magazine average pizzeria sells pizzas per week survey

- `https://rentechdigital.com/smartscraper/it/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p24 Count of pizza restaurants in Chicago (business listing total) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Ci sono 1987 Pizza restaurants in Chicago al April 1, 2026"
  - p25 Count of pizza restaurants in Chicago (stated total as of April 01, 2026) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p24 (same 1,987 count, same snapshot).] quote: "Ci sono un totale di 1987 Ristoranti di pizza in Chicago al April 01, 2026."
  - p26 Share of Chicago pizza restaurants that are single-owner operations (numerator 9 = **46** percent (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago"
  - p27 Count of single-owner pizza restaurants in Chicago = **914** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p28 Count of pizza restaurants in Chicago belonging to larger brands = **1,073** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p29 Share of Chicago pizza restaurants belonging to larger brands (numerator 1073 of = **54** percent (2026-04-01..2026-04-01) [keep: ] quote: "le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p30 Average age of pizza restaurants in Chicago = **10** years (plus 2 months) (2026-04-01..2026-04-01) [keep: ] quote: "Average age of Pizza restaurants in Chicago is10 anni e 2 mesi."
  - p31 Count of Chicago pizza restaurants with own website = **1,848** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web e i restanti 139 non hanno un proprio sito web."
  - p32 Count of Chicago pizza restaurants without own website = **139** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "e i restanti 139 non hanno un proprio sito web"
  - p33 Count of Chicago pizza restaurants with Facebook pages = **1,048** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "1048 hanno pagine Facebook"
  - p34 Count of Chicago pizza restaurants with Instagram accounts = **848** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "848 sono attivi su Instagram"
  - p35 Count of Chicago pizza restaurants with LinkedIn profiles = **88** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "88 hanno profili LinkedIn"
  - p36 Count of Chicago pizza restaurants with X accounts = **635** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "635 hanno account su X (precedentemente Twitter)"
  - p37 Count of Chicago pizza restaurants with TikTok profiles = **189** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "189 sono su TikTok"
  - p38 Count of Chicago pizza restaurants with YouTube channels = **151** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "151 have YouTube channels"
- `https://businesstats.com/pizza-restaurant-industry-market-size-us/` -> **live_dated** (page date 2026-05-30); points raw/verified 15/10
  - p39 Number of U.S. pizzeria businesses (2024, IBISWorld) = **74,000** pizzeria businesses (2024-01-01..2024-12-31) [keep: ] quote: "generated by more than 74,000 pizzeria businesses"
  - p40 U.S. pizza restaurant industry revenue (2024) = **50,100,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "The industry reached a projected $50.1 billion in revenue in 2024"
  - p41 Domino's U.S. sales (2024) = **9,500,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| Domino's U.S. Sales (2024) \| $9.5 Billion \|"
  - p42 Domino's U.S. units (2024) = **7,014** locations (2024-01-01..2024-12-31) [keep: ] quote: "\| Domino's U.S. Units (2024) \| 7,014 \|"
  - p43 Pizza Hut U.S. sales (2024) = **5,290,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| Pizza Hut U.S. Sales (2024) \| $5.29 Billion \|"
  - p44 Pizza Hut U.S. units (2024) = **6,518** units (2024-01-01..2024-12-31) [keep: ] quote: "It is followed by Pizza Hut ($5.29 billion, 6,518 units)"
  - p45 Little Caesars U.S. sales (2024) = **4,930,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| Little Caesars U.S. Sales (2024) \| $4.93 Billion \|"
  - p46 Little Caesars U.S. units (2024) = **4,249** units (2024-01-01..2024-12-31) [keep: ] quote: "Little Caesars ($4.93 billion, 4,249 units)"
  - p47 Papa Johns U.S. sales (2024, estimated) = **3,860,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "\| Papa Johns U.S. Sales (2024) \| $3.86 Billion (est.) \|"
  - p48 Papa Johns U.S. units (2024) = **3,320** units (2024-01-01..2024-12-31) [keep: ] quote: "Papa Johns (approximately $3.86 billion, 3,320 units)"
- `https://economictimes.indiatimes.com/news/international/us/americans-eat-over-3-billion-pizzas-every-year-350-slices-per-second-10-mind-blowing-pizza-` -> **live_dated** (page date 2025-07-23); points raw/verified 15/2
  - p49 Diameter of the largest pizza ever made (Rome, 2012) = **131** feet in diameter (2012-01-01..2012-12-31) [DISCARD: World-record pizza diameter; irrelevant to Chicago daily consumption.] quote: "The largest pizza ever made, measuring 131 feet in diameter, was rolled out in Rome in 2012."
  - p50 Year the first US pizzeria (Gennaro Lombardi) opened = **1,905** year (1905-01-01..1905-12-31) [DISCARD: Historical trivia (first US pizzeria year); no bearing on 2026 mass.] quote: "the first US pizzeria, Gennaro Lombardi, opened in 1905 at 32 Spring Street in New York City."
- `https://dojobusiness.com/blogs/news/pizza-restaurant-profitability` -> **live_dated** (page date 2023-10-29); points raw/verified 15/5
  - p51 Typical daily pizza orders per pizza restaurant (industry benchmark, 2025) = **100** orders per day per restaurant (2025-01-01..2025-12-31) [keep: ] quote: "Pizza restaurants in 2025 typically sell around 100 orders daily, generating approximately $2,000 in daily revenue."
  - p52 Daily orders benchmark in table (pizzas per day per restaurant, 2025) = **100** pizzas per day per restaurant (2025-01-01..2025-12-31) [DISCARD: Duplicate of p51 (same 100 orders/day benchmark).] quote: "\| Daily Orders \| 100 pizzas/day \| Foundation for revenue planning \|"
  - p53 Typical daily revenue per pizza restaurant (2025) = **2,000** USD per day per restaurant (2025-01-01..2025-12-31) [keep: ] quote: "A typical pizza restaurant sells approximately 100 orders per day, generating around $2,000 in daily revenue."
  - p54 Average ticket size lower bound per order (2025) = **18** USD per order (2025-01-01..2025-12-31) [keep: ] quote: "\| Average Ticket Size \| $18-$25 per order \| Upsells drive higher end of range \|"
  - p55 Average ticket size upper bound per order (2025) = **25** USD per order (2025-01-01..2025-12-31) [keep: ] quote: "\| Average Ticket Size \| $18-$25 per order \| Upsells drive higher end of range \|"
- dropped by code checks: 28 (period_end 2026-12-31 after as_of: 2; period_end missing or unparseable: 24; number: no number in value_as_written: 2)

### d4 [own_history] Prior estimates of city pizza consumption

Hypothesis: Any published estimate of Chicago or comparable-city pizza consumption (tonnes, slices, or pies per day/year) provides a direct anchor or validation. Transfer assumption: comparable-city per-capita estimates transfer to Chicago with population and cultural adjustment.

Queries issued by the searcher: how many pizzas does Chicago eat per day; US pizza consumption tons per year statistics; "Chicago" pizza consumption estimate "pizzas per day" city pizzeria count annual; USDA per capita pizza consumption pounds per year ERS food availability

- `https://www.chicagotribune.com/2006/12/28/second-city-digits/` -> **live_dated** (page date 2006-12-28); points raw/verified 15/0
- `https://bayareapizzaweek.com/2026/01/14/fun-pizza-facts/` -> **live_dated** (page date 2026-01-14); points raw/verified 12/1
  - p56 Diameter of largest pizza ever made (Rome, 2012) = **131** feet in diameter (2012-01-01..2012-12-31) [DISCARD: Duplicate of p49; irrelevant.] quote: "The largest pizza ever made measured 131 feet in diameter and was rolled out in Rome in 2012."
- `https://chicago.eater.com/2012/5/11/6587185/by-the-numbers-roots-giordanos-lou-malnatis` -> **live_dated** (page date 2012-05-11); points raw/verified 14/1
  - p57 Giordano's pizzas shipped nationwide in 2011 = **26,888** pizzas shipped nationwide (2011-01-01..2011-12-31) [DISCARD: 2011 Giordano's shipped-pizza count; stale, single-chain, and not a Chicago consumption measure.] quote: "Number of pizzas shipped nationwide in 2011: 26,888"
- `https://www.pmq.com/pizza-huts-annual-trends-report-32-percent-of-consumers-will-eat-more-pizza-this-year/` -> **live_dated** (page date 2025-01-09); points raw/verified 14/0
- dropped by code checks: 53 (period_end missing or unparseable: 51; value_as_written not in quote as a whole number: 2)

### d5 [physical_flow] Supply chain / ingredient flow

Hypothesis: Flour or cheese flowing into Chicago pizza production, converted to pizza mass via recipe ratios, gives an upper-bound cross-check on pizza mass. Transfer assumption: pizza flour/cheese use per unit pizza mass is stable and separable from other uses.

Queries issued by the searcher: mozzarella consumption pizza US per year; pizza flour usage per pizza kg dough yield; Chicago food distribution pizza ingredients flour cheese; USDA ERS mozzarella per capita consumption 2023 2024 data; US pizza cheese consumption annual tons pizza industry mozzarella 2024; Chicago flour mills pizza flour foodservice distribution; Chicago pizza market size annual sales number of pizzerias

- `https://www.pmq.com/the-numbers-and-nuances-of-dough/` -> **live_dated** (page date 2023-03-16); points raw/verified 15/0
- `http://www.ers.usda.gov/AmberWaves/February05/pdf/FindingsDietandHealthFeb05.pdf` -> **dropped** (live http 404); points raw/verified -/-
- `https://www.cnbc.com/2016/10/04/best-cheeses-americans-have-an-insatiable-demand-for-pizza-cheese.html` -> **live_dated** (page date 2016-10-04); points raw/verified 8/0
- `http://www.RealDeepDish.com/RDDHolyGrail2013.pdf` -> **live_dated** (page date 2014-02-02); points raw/verified 15/0
- dropped by code checks: 38 (period_end missing or unparseable: 35; number: no number in value_as_written: 3)

### d6 [related_series] Retail / grocery and frozen pizza

Hypothesis: Supermarket/frozen pizza sales attributable to Chicago households, converted to mass, cover the at-home component; combined with foodservice gives total. Transfer assumption: national frozen/refrigerated pizza retail sales per capita apply to Chicago households.

Queries issued by the searcher: frozen pizza retail sales US 2025 billion dollars; average frozen pizza weight grams; frozen pizza units sold US 2025 Circana million units average price per unit; "frozen pizza" average retail price per unit 2025 dollars units

- `https://greenwichgp.com/wp-content/uploads/2026/09/GCG-US-Frozen-Pizza-Industry-2026-Update.pdf.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/7
  - p58 U.S. frozen pizza retail dollar sales, 52 weeks ending April 19, 2026 = **7,300,000,000** USD (2025-04-20..2026-04-19) [keep: ] quote: "U.S. frozen pizza generated about $7.3 billion in the 52 weeks ending April 19, 2026, down 1.9% year over year"
  - p59 U.S. frozen pizza retail sales, prior level held through 2025 (upper bound) = **7,500,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "after holding near $7.4 to $7.5 billion through 2025"
  - p60 U.S. frozen pizza market size, IMARC 2025 estimate = **7,200,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "IMARC puts the U.S. market at ~$7.2 billion in 2025 rising to ~$11.0 billion by 2034, a 4.64% CAGR"
  - p61 Global frozen pizza market size, 2024 (Grand View Research) = **22,700,000,000** USD (2024-01-01..2024-12-31) [DISCARD: Global frozen pizza market size; wrong scope (global, not US/Chicago).] quote: "Grand View Research now pegs the global frozen pizza market at about $22.7 billion in 2024"
  - p62 North America share of global frozen pizza market = **37** percent (2024-01-01..2024-12-31) [DISCARD: North America share of global market; not needed once US retail sales are used directly.] quote: "growing ~3.5% annually, with North America roughly 37% of the total."
  - p63 Private label frozen pizza U.S. retail sales, 52 weeks ending April 19, 2026 = **1,100,000,000** USD (2025-04-20..2026-04-19) [keep: ] quote: "Private label frozen pizza is a roughly $1.1 billion business, but it swung from +4% growth in early 2025 to a 4.4% decline by April 2026."
  - p64 Share of U.S. households reached by frozen food department = **99** percent (2024-09-22..2025-09-21) [DISCARD: Share of US households reached by frozen food department; too broad (all frozen food) to inform pizza mass.] quote: "The broader U.S. frozen food department is roughly $93.5 billion, and frozen reaches about 99% of U.S. households."
- `https://frb.mydigitalpublication.com/articles/turning-up-the-heat-on-frozen-pizza` -> **dropped** (live http 202); points raw/verified -/-
- `https://www.ift.org/food-technology-magazine/consumers-consumers-flock-to-frozen` -> **live_dated** (page date 2025-05-02); points raw/verified 6/2
  - p65 US frozen pizza retail sales, year ended Feb. 23, 2025 (Circana) = **7,500,000,000** USD (2024-02-24..2025-02-23) [keep: ] quote: "seafood, $8.2 billion; pizza, $7.5 billion; processed poultry, $7.4 billion"
  - p66 US frozen dinners/entrées retail sales, year ended Feb. 23, 2025 (Circana) = **13,800,000,000** USD (2024-02-24..2025-02-23) [DISCARD: Frozen dinners/entrées sales; different category from pizza.] quote: "With sales of $13.8 billion for the year ended Feb. 23, 2025, frozen dinners/entrées were the largest frozen food category"
- `https://www.nutritionvalue.org/comparefoods.php?foods=58106205%252A1%2Bpiece%252C%2BNFS%2B%253D%2B133.0%2Bg` -> **live_dated** (page date 2026-01-01); points raw/verified 1/0
- dropped by code checks: 13 (scale word 'billion' not supported by quote or table header: 4; period_end 2034-12-31 after as_of: 1; period_end missing or unparseable: 7; number: no number in value_as_written: 1)

### d7 [persona] Chicago visitor/tourism and commuter flows

Hypothesis: People present in Chicago on an average day exceed resident population due to visitors and commuters; adjusting the resident-based estimate by an exposure factor (average daily present population / resident population) corrects for non-resident eating. Transfer assumption: visitors and commuters eat pizza at similar or slightly higher rates than residents.

Queries issued by the searcher: Chicago daily visitors average 2025 Choose Chicago tourism statistics; Chicago population 2025 estimate Census; Chicago daytime population commuters into city daily Census estimate; Chicago workers commute into city from suburbs number each day 2024

- `https://www.choosechicago.com/press-media/press-releases/chicago-welcomes-56-8-million-tourists-in-2025-generating-a-record-breaking-21-5-billion-in-s` -> **live_dated** (page date 2026-06-25); points raw/verified 7/4
  - p67 Chicago total visitors in 2025 (annual) = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "Chicago welcomed 56.8 million visitors in 2025, generating a record-setting $21.5 billion in visitor spending"
  - p68 Increase in Chicago visitors 2025 vs 2024 = **1,500,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "The city welcomed nearly 1.5 million more visitors than in 2024, reflecting continued growth despite economic uncertainty"
  - p69 Chicago visitor spending in 2025 (annual) = **21,500,000,000** US dollars (2025-01-01..2025-12-31) [keep: ] quote: "generating a record-setting $21.5 billion in visitor spending and supporting 135,360 local jobs across the region"
  - p70 Local jobs supported by Chicago tourism in 2025 = **135,360** jobs (2025-01-01..2025-12-31) [keep: ] quote: "supporting 135,360 local jobs across the region, according to data released today by Choose Chicago"
- `https://www.census.gov/quickfacts/fact/table/IL,chicagocityillinois,jolietcityillinois/` -> **dropped** (live http 403); points raw/verified -/-
- `https://twt-assets.washtimes.com/news/2023/jul/5/census-biggest-cities-lost-more-1m-day-residents-c/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.city-data.com/forum/city-vs-city/3037899-citydaytime-population-2017-a.html` -> **live_dated** (page date 2019-04-17); points raw/verified 15/11
  - p71 Chicago, IL daytime population, 2017 (Census daytime population estimate) = **2,920,652** people (2017-01-01..2017-12-31) [keep: ] quote: "2,920,652 Chicago, IL"
  - p72 Chicago, IL total workers working in city, 2017 = **1,533,399** workers (2017-01-01..2017-12-31) [keep: ] quote: "1,533,399 Chicago, IL 1,329,197 +204,202"
  - p73 Chicago, IL total employed residents in city, 2017 = **1,329,197** workers (2017-01-01..2017-12-31) [keep: ] quote: "1,533,399 Chicago, IL 1,329,197 +204,202"
  - p74 Chicago, IL net commuting inflow (workers in city minus employed residents), 201 = **204,202** workers (2017-01-01..2017-12-31) [keep: ] quote: "1,533,399 Chicago, IL 1,329,197 +204,202"
  - p75 Manhattan commuters into Manhattan, 2013 = **1,600,000** people (2013-01-01..2013-12-31) [DISCARD: Manhattan commuter count; wrong city, not transferable.] quote: "In 2013, 1.6 million people commuted into Manhattan"
  - p76 New York, NY daytime population, 2017 = **9,357,951** people (2017-01-01..2017-12-31) [DISCARD: NYC daytime population; wrong city.] quote: "City Daytime Population, 2017: 9,357,951 New York, NY"
  - p77 Los Angeles, CA daytime population, 2017 = **4,169,529** people (2017-01-01..2017-12-31) [DISCARD: LA daytime population; wrong city.] quote: "4,169,529 Los Angeles, CA"
  - p78 Houston, TX daytime population, 2017 = **3,018,200** people (2017-01-01..2017-12-31) [DISCARD: Houston daytime population; wrong city.] quote: "3,018,200 Houston, TX"
  - p79 New York, NY total workers working in city, 2017 = **4,808,014** workers (2017-01-01..2017-12-31) [DISCARD: NYC workers in city; wrong city.] quote: "4,808,014 New York, NY 4,072,761 +735,263"
  - p80 New York, NY net commuting inflow, 2017 = **735,263** workers (2017-01-01..2017-12-31) [DISCARD: NYC net commuting inflow; wrong city.] quote: "4,808,014 New York, NY 4,072,761 +735,263(number of workers who commute into city limits)"
  - p81 Houston, TX net commuting inflow, 2017 = **768,483** workers (2017-01-01..2017-12-31) [DISCARD: Houston net commuting inflow; wrong city.] quote: "1,851,938 Houston, TX 1,083,455 +768,483"
- dropped by code checks: 7 (period_end missing or unparseable: 7)

### d8 [shocks] Price and demand environment

Hypothesis: Pizza prices and demand in 2026 may differ from historical baselines due to inflation, cheese prices, or post-pandemic dining shifts; these affect the USD-to-mass conversion and per-capita frequency. Transfer assumption: real consumption frequency is stable but price levels shift the sales-based route.

Queries issued by the searcher: pizza price inflation 2025 2026 average price per pizza; restaurant pizza traffic trends 2025 Domino's Papa John's same-store sales; cheese prices 2026 cheddar block barrel pizza mozzarella wholesale USDA; BLS CPI pizza food away from home 2026 index

- `https://www.restaurantbusinessonline.com/financing/quick-service-pizza-sales-turned-negative-last-year` -> **live_dated** (page date 2026-05-13); points raw/verified 15/15
  - p82 QSR pizza category year-over-year sales change, 2025 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, however, the category slipped below the surface, registering a 0.3% year-over-year sales slide"
  - p83 QSR pizza category nominal sales change, 2024 = **0.6** % (2024-01-01..2024-12-31) [keep: ] quote: "following a nominal gain of just 0.6% in 2024"
  - p84 QSR pizza category sales change, 2023 = **2.8** % (2023-01-01..2023-12-31) [keep: ] quote: "and an increase of 2.8% in 2023, according to the Technomic Top 500 Chain Restaurant Report."
  - p85 QSR pizza category unit count change, 2025 = **0.1** % (2025-01-01..2025-12-31) [keep: ] quote: "Unit count has followed a similar trajectory, with just a 0.1% gain last year"
  - p86 QSR pizza category unit count change, 2024 = **0.6** % (2024-01-01..2024-12-31) [keep: ] quote: "following 0.6% in 2024 and 1.1% in 2023."
  - p87 QSR pizza category unit count change, 2023 = **1.1** % (2023-01-01..2023-12-31) [keep: ] quote: "following 0.6% in 2024 and 1.1% in 2023."
  - p88 QSR pizza category total sales, 2025 = **31,000,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "with $31 billion in sales"
  - p89 Overall restaurant industry Top 500 sales change, 2025 = **3** % (2025-01-01..2025-12-31) [keep: ] quote: "Notably, the overall restaurant industry was up just 3% in 2025"
  - p90 Pizza Hut sales change, 2025 = **8.2** % (2025-01-01..2025-12-31) [keep: ] quote: "Pizza Hut, No. 2, lost 8.2% of its sales in 2025, for instance."
  - p91 Domino's sales change, 2025 = **4.8** % (2025-01-01..2025-12-31) [keep: ] quote: "while Domino's extended its market share dominance with a 4.8% gain"
  - p92 Jet's Pizza sales change, 2025 = **11.5** % (2025-01-01..2025-12-31) [keep: ] quote: "No. 7 Jet's Pizza provided a bright spot with an 11.5% increase."
  - p93 Jet's Pizza total sales, 2025 = **613,400,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "which increased sales by 11.5% to end with $613.4 million and 474 locations (a 5.8% increase)"
  - p94 Jet's Pizza location count, end of 2025 = **474** locations (2025-12-31..2025-12-31) [keep: ] quote: "to end with $613.4 million and 474 locations (a 5.8% increase)"
  - p95 Number of limited-service pizza chains in Top 500 that gained sales, 2025 = **16** chains (2025-01-01..2025-12-31) [keep: ] quote: "Out of the 35 limited-service pizza chains in the Top 500, 16 gained sales in 2025 versus 19 that registered declines."
  - p96 Number of limited-service pizza chains in Top 500 that declined in sales, 2025 = **19** chains (2025-01-01..2025-12-31) [keep: ] quote: "Out of the 35 limited-service pizza chains in the Top 500, 16 gained sales in 2025 versus 19 that registered declines."
- `https://getmarketpulse.com/reports/restaurant-price-index` -> **live_dated** (page date 2026-10-01); points raw/verified 15/0
- `https://thatpizzakitchen.com/cheese-block-prices-mozzarella-october-2026/` -> **live_dated** (page date 2026-10-02); points raw/verified 15/6
  - p97 CME 40-pound cheddar blocks closing price, Tuesday September 29 2026 = **1.275** USD per pound (2026-09-29..2026-09-29) [keep: ] quote: "Cheddar blocks on the Chicago Mercantile Exchange closed at $1.2750 a pound on Tuesday, September 29, down 3.25 cents on the day and the lowest print of 2026."
  - p98 CME cheddar blocks closing price Thursday after rally = **1.302** USD per pound (2026-10-01..2026-10-01) [keep: ] quote: "$1.3025/lb - where blocks closed Thursday after a 3.25-cent rally on three sales."
  - p99 CME cheddar blocks price late August 2026 (CLAL series) = **1.565** USD per pound (2026-08-01..2026-08-31) [keep: ] quote: "Down about 15% - blocks were $1.5650 in late August and $1.6075 in late July, per CLAL's weekly US cheddar series"
  - p100 CME cheddar blocks price late July 2026 (CLAL series) = **1.607** USD per pound (2026-07-01..2026-07-31) [keep: ] quote: "blocks were $1.5650 in late August and $1.6075 in late July, per CLAL's weekly US cheddar series, which also puts prices around 14 percent below the same week last year."
  - p101 CME cheddar blocks opening price for the week = **1.308** USD per pound (2026-09-28..2026-09-28) [keep: ] quote: "Blocks opened the week at $1.3075, slid Tuesday, slipped again midweek, then recovered 3.25 cents to $1.3025 on Thursday"
  - p102 CME butter closing price Thursday = **1.34** USD per pound (2026-10-01..2026-10-01) [keep: ] quote: "Butter had its own rough week, closing Thursday at $1.34."
- `https://finks.ai/discover/pizza-is-shrinking-fast-and-the-stocks-are-telling-that-story` -> **live_dated** (page date 2026-08-06); points raw/verified 15/1
  - p103 Pizza Hut US locations shuttered in first half of 2026 = **250** US locations (2026-01-01..2026-06-30) [keep: ] quote: "Under its "Hut Forward" program, Pizza Hut shuttered roughly 250 US locations in the first half of 2026 alone."
- dropped by code checks: 38 (period_end missing or unparseable: 30; scale word 'thousand' not supported by quote or table header: 1; period_end 2026-12-31 after as_of: 6; period_end 2027-12-31 after as_of: 1)

### b1 [related_series] Chicago foodservice pizza dollar sales

Hypothesis: A Chicago-specific pizza restaurant sales total (or Chicago share of US pizza foodservice revenue) would replace the national per-capita scaling in the sales-to-mass route (d1), which currently carries the largest transfer uncertainty.

Queries issued by the searcher: Chicago pizza restaurant sales Technomic market report; "pizza" restaurant sales Chicago MSA million dollars 2024; Illinois Restaurant Association Chicago restaurant sales billion 2025 projected; US pizza sales total 2024 billion Technomic pizza restaurants annual sales

- `https://restaurant.org/getmedia/3ea909b6-a3c2-4178-bf6e-5d4a567b4f0f/il_econ_impact_study_fs-3.pdf` -> **live_dated** (page date 2025-07-29); points raw/verified 15/2
  - p104 Chicago-Naperville-Elgin MSA eating and drinking places direct employment, 2025  = **424,662** jobs (2025-01-01..2025-12-31) [keep: ] quote: "$46.99B $86.32B 424,662 588,064"
  - p105 Chicago-Naperville-Elgin MSA eating and drinking places total employment, 2025 p = **588,064** jobs (2025-01-01..2025-12-31) [keep: ] quote: "$46.99B $86.32B 424,662 588,064"
- `https://marketintelo.com/report/chicago-deep-dish-pizza-restaurant-market` -> **live_dated** (page date 2026-06-11); points raw/verified 15/10
  - p106 Chicago Deep-Dish Pizza Restaurant market size, global, 2025 (base year) = **900,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "The Chicago Deep-Dish Pizza Restaurant market is valued at $0.9 billion in 2025"
  - p107 Illinois and Chicago area share of total Chicago deep-dish market revenue, 2025 = **65** percent of total market revenue (2025-01-01..2025-12-31) [keep: ] quote: "Illinois and the Chicago area alone accounting for approximately 65.0% of total market revenue"
  - p108 Dine-In segment share of Chicago deep-dish market revenue, 2025 = **38.5** percent of total market revenue (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 38.5% of total market revenue in 2025, generating approximately $0.35 billion in annual revenue"
  - p109 Dine-In segment annual revenue, 2025 = **350,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 38.5% of total market revenue in 2025, generating approximately $0.35 billion in annual revenue"
  - p110 Takeout segment share of Chicago deep-dish market revenue, 2025 = **28.3** percent of total market revenue (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 28.3% of total market revenue in 2025, generating approximately $0.25 billion in annual revenue"
  - p111 Takeout segment annual revenue, 2025 = **250,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 28.3% of total market revenue in 2025, generating approximately $0.25 billion in annual revenue"
  - p112 Delivery segment share of Chicago deep-dish market revenue, 2025 = **22** percent of total market revenue (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 22.0% of total market revenue in 2025, generating approximately $0.20 billion in annual revenue"
  - p113 Delivery segment annual revenue, 2025 = **200,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 22.0% of total market revenue in 2025, generating approximately $0.20 billion in annual revenue"
  - p114 Catering segment share of Chicago deep-dish market revenue, 2025 = **11.2** percent of total market revenue (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 11.2% of total market revenue in 2025, generating approximately $0.10 billion in annual revenue"
  - p115 Catering segment annual revenue, 2025 = **100,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 11.2% of total market revenue in 2025, generating approximately $0.10 billion in annual revenue"
- `https://chicagochinesetimes.com/2025/07/09/%e3%80%90%e9%a2%a8%e5%9f%8e%e5%bf%ab%e5%a0%b1%e3%80%91%e6%a3%92-%e8%8a%9d%e5%8a%a0%e5%93%a52%e5%ae%b6%e7%9f` -> **live_dated** (page date 2025-07-09); points raw/verified 15/13
  - p116 US pizza chain sales growth rate, 2024 (Technomic annual report) = **0.5** % (2024-01-01..2024-12-31) [keep: ] quote: "2024 年披薩連鎖店的銷售額僅成長了 0.5%"
  - p117 Overall chain restaurant sales growth rate, 2024 (comparison to pizza chains) = **3** % (2024-01-01..2024-12-31) [keep: ] quote: "遠低於整體連鎖餐廳 3% 的銷售成長率"
  - p118 Giordano's total US restaurants at end of 2024 = **60** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "截至 2024 年底,Giordano's 在全國範圍內經營著 60 家餐廳"
  - p119 Giordano's total US restaurants in 2022 = **65** restaurants (2022-01-01..2022-12-31) [keep: ] quote: "相比 2022 年的 65 家有所減少"
  - p120 Lou Malnati's total restaurants (end of 2024) = **80** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "Lou Malnati's 則擁有 80 家分店"
  - p121 Lou Malnati's total restaurants in 2022 = **74** restaurants (2022-01-01..2022-12-31) [keep: ] quote: "高於 2022 年的 74 家"
  - p122 Giordano's restaurants in Florida (end of 2024) = **3** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "包括佛羅里達州(3 家)"
  - p123 Giordano's restaurants in Indiana (end of 2024) = **4** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "印第安納州(4 家)"
  - p124 Giordano's restaurants in Nevada (end of 2024) = **2** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "內華達州(2 家)"
  - p125 Giordano's restaurants in Ohio (end of 2024) = **2** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "俄亥俄州(2 家)"
  - p126 Lou Malnati's restaurants in Arizona (end of 2024) = **9** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "其中亞利桑那州截至 2024 年底有 9 家分店"
  - p127 Victory Park Capital acquisition price for majority of Giordano's assets, 2011 = **52,000,000** USD (2011-01-01..2011-12-31) [keep: ] quote: "2011 年,Victory Park Capital 以 5200 萬美元收購了 Giordano's 的大部分資產"
  - p128 Lou Malnati's valuation from Meritage Group stake purchase, 2011 = **500,000,000** USD (2011-01-01..2011-12-31) [keep: ] quote: "該交易使 Lou Malnati's 的估值達到 5 億美元"
- `https://www.bizjournals.com/newyork/news/2018/04/02/technomic-unearths-crusty-news-about-pizza-wars.html` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 20 (scale word 'billion' not supported by quote or table header: 13; period_end 2034-12-31 after as_of: 2; number: more than one number in value_as_written: 1; period_end missing or unparseable: 3; number: no number in value_as_written: 1)

### b2 [base_rates] Average mass per pizza serving

Hypothesis: The USDA prevalence route (d2) needs a grams-per-pizza-occasion figure; without it the frequency-to-mass bridge is the dominant uncertainty. A slice-weight or pie-weight benchmark would unlock a full independent estimate.

Queries issued by the searcher: NHANES pizza grams per eating occasion; WWEIA pizza portion size grams food pattern equivalents; "Dietary Data Brief" 62 pizza 2024 grams average amount consumed per eating occasion slices; FNDDS "pizza, cheese" "regular crust" 1 slice grams portion weight 1/6 14-inch

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/10
  - p129 Reference slice definition (definitions section): gram weight basis is one slice = **14** inches (pizza diameter) (..) [keep: ] quote: "The reference for a slice of pizza was the gram weight of one slice of a 14-inch fast food/restaurant cheese pizza with a regular crust (7)."
  - p130 Share of US population consuming pizza on any given day = **11** % of population (2017-01-01..2020-03-31) [keep: ] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p131 Share of US population 60+ consuming pizza on any given day = **6** % of population (2017-01-01..2020-03-31) [keep: ] quote: "the percentage consuming decreased to about 6% among older adults (60+)."
  - p132 Share of pizza intake consumed at lunch by children 2-19 years = **41** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p133 Share of pizza intake consumed at dinner by children 2-19 years = **48** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p134 Share of pizza intake consumed at lunch by adults 20+ years = **28** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "4 28 58 10"
  - p135 Share of pizza intake from snacks = **4** % of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Snacks accounted for 4% of pizza intake."
  - p136 Share of pizza obtained from restaurants (take-out or sit-down) = **56** % of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p137 Share of pizza obtained from school/daycare = **12** % of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p138 Share of pizza obtained from 'Other' sources = **6** % of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources"
- `https://faseb.onlinelibrary.wiley.com/doi/10.1096/fasebj.30.1_supplement.lb407` -> **dropped** (live http 403); points raw/verified -/-
- `https://jn.nutrition.org/article/S0022-3166(25` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/11_consumption_of_pizza_0710.pdf` -> **live_dated** (page date 2014-02-05); points raw/verified 15/15
  - p139 Energy content of a slice of cheese pizza (1/8th of a medium, all crust types),  = **220** kilocalories per slice (..) [keep: ] quote: "The amount of energy contained in a slice of cheese pizza (1/8th of a medium, all crust types) ranged from approximately 220-370 kilocalories (5)."
  - p140 Energy content of a slice of cheese pizza (1/8th of a medium, all crust types),  = **370** kilocalories per slice (..) [keep: ] quote: "The amount of energy contained in a slice of cheese pizza (1/8th of a medium, all crust types) ranged from approximately 220-370 kilocalories (5)."
  - p141 Mean energy intake obtained from pizza among child pizza consumers (2-19 years) = **538** kilocalories per consumer per day (2007-01-01..2010-12-31) [keep: ] quote: "Among consumers of pizza, the mean energy intake obtained from pizza was 538 kilocalories for children and 744 kilocalories for adults (data not shown)."
  - p142 Mean energy intake obtained from pizza among adult pizza consumers (20 years and = **744** kilocalories per consumer per day (2007-01-01..2010-12-31) [keep: ] quote: "Among consumers of pizza, the mean energy intake obtained from pizza was 538 kilocalories for children and 744 kilocalories for adults (data not shown)."
  - p143 Mean sodium intake obtained from pizza among child pizza consumers (2-19 years) = **1,136** milligrams per consumer per day (2007-01-01..2010-12-31) [keep: ] quote: "For consumers of pizza, the mean sodium intake obtained from pizza was 1136 mg for children and 1599 mg for adults (data not shown)."
  - p144 Mean sodium intake obtained from pizza among adult pizza consumers (20 years and = **1,599** milligrams per consumer per day (2007-01-01..2010-12-31) [keep: ] quote: "For consumers of pizza, the mean sodium intake obtained from pizza was 1136 mg for children and 1599 mg for adults (data not shown)."
  - p145 Share of U.S. population aged 2 years and over consuming pizza on any given day = **13** percent of population (2007-01-01..2010-12-31) [keep: ] quote: "Overall, 13% of the U.S. population aged 2 years and over, consumed pizza on any given day"
  - p146 Share of pizza consumption occurring in the home (all consumers) = **59** percent of pizza consumption (2007-01-01..2010-12-31) [keep: ] quote: "More than half (59%) of pizza consumption occurred in the home."
  - p147 Share of pizza consumption occurring at a snack occasion (all consumers) = **10** percent of pizza consumption (2007-01-01..2010-12-31) [keep: ] quote: "Overall, almost 10% of pizza consumption occurred at a snack occasion (Figure 5)."
  - p148 Share of pizza consumption occurring at lunch among children (2-19 years) = **44** percent of pizza consumption (2007-01-01..2010-12-31) [keep: ] quote: "For children, 44% of pizza consumption occurred at lunch and 42% occurred at dinner."
  - p149 Share of pizza consumption occurring at dinner among children (2-19 years) = **42** percent of pizza consumption (2007-01-01..2010-12-31) [keep: ] quote: "For children, 44% of pizza consumption occurred at lunch and 42% occurred at dinner."
  - p150 Share of pizza provided as percent of total daily energy among all pizza consume = **27** percent of daily energy intake (2007-01-01..2010-12-31) [keep: ] quote: "On the day consumed, pizza provided approximately 27% of total energy among all consumers."
  - p151 Share of U.S. children (2-19 years) consuming pizza on any given day = **20** percent of population (2007-01-01..2010-12-31) [keep: ] quote: "Overall, a higher percentage of children (2-19 years) consumed pizza than adults (20 years and over): 20% vs. 11%, respectively."
  - p152 Share of U.S. adults (20 years and over) consuming pizza on any given day = **11** percent of population (2007-01-01..2010-12-31) [keep: ] quote: "Overall, a higher percentage of children (2-19 years) consumed pizza than adults (20 years and over): 20% vs. 11%, respectively."
  - p153 WWEIA NHANES combined study sample size, individuals aged 2 years and over = **17,571** individuals (2007-01-01..2010-12-31) [keep: ] quote: "The study sample included 17,571 individuals, aged 2 years and over (excluding breast-fed children), with complete"
- dropped by code checks: 5 (value_as_written not in quote as a whole number: 4; number: more than one number in value_as_written: 1)

### b3 [persona] Average visitor length of stay in Chicago

Hypothesis: Converting p67 (56.8M annual visitors) into average daily present population requires an average nights-per-visitor figure; this exposure factor (d7) materially shifts the 'people present in Chicago' denominator.

Queries issued by the searcher: Choose Chicago average length of stay visitors 2025 hotel nights; Chicago average hotel nights per visitor length of stay; "Chicago" visitor "average length of stay" nights 2024 Choose Chicago overnight visitors person-stays; Chicago tourism 2025 overnight visitors 11.9 million room nights average party size nights per trip

- `https://cdn.choosechicago.com/uploads/2026/06/cc_2025_economic_impact_midyear_v.2.pdf` -> **live_dated** (page date 2026-06-01); points raw/verified 15/0
- `https://cdn.choosechicago.com/uploads/2026/09/Chicago-Tourism-Overview-2025.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/3
  - p154 Chicago hotel occupancy rate, 2025 = **69.2** percent (2025-01-01..2025-12-31) [keep: ] quote: "Occupancy Rate (%) 43.0 60.4 65.3 68.1 69.2"
  - p155 Chicago hotel average daily rate, 2025 = **243** US dollars per room night (2025-01-01..2025-12-31) [keep: ] quote: "Average Daily Rate $181.22 $228.58 $228.37 $241.86 $243.31"
  - p156 Chicago hotel RevPAR, 2025 = **168** US dollars per available room night (2025-01-01..2025-12-31) [keep: ] quote: "RevPAR $77.91 $138.04 $149.03 $164.80 $168.25"
- `https://es-mx.enjoyillinois.com/assets/Files-PDFs/Illinois-Chicago-2022-Visitor-Profile.pdf` -> **live_dated** (page date 2023-07-24); points raw/verified 15/7
  - p157 Chicago leisure average travel party size (persons), 2022 = **1.92** persons (2022-01-01..2022-12-31) [keep: ] quote: "an average travel party size of 1.90 people and 1.92 people respectively in 2022"
  - p158 Illinois leisure average travel party size (persons), 2022 = **1.9** persons (2022-01-01..2022-12-31) [keep: ] quote: "an average travel party size of 1.90 people and 1.92 people respectively in 2022"
  - p159 U.S. leisure average travel party size (persons), 2022 = **2.3** persons (2022-01-01..2022-12-31) [keep: ] quote: "a lower travel party average than the US of 2.30 people due to fewer families and traveling groups."
  - p160 Chicago leisure average expenditure per person per day (USD), 2022 = **237** USD per person per day (2022-01-01..2022-12-31) [keep: ] quote: "Leisure travelers spent $237 on average in Chicago but slightly less, $181 on average, when visiting the State of Illinois."
  - p161 Chicago leisure daily spending per person (USD), 2020 = **106** USD per person per day (2020-01-01..2020-12-31) [keep: ] quote: "Chicago leisure travelers' daily spending was $106 per person in 2020 and increased during the pandemic by 74% to $184 in 2021."
  - p162 Chicago leisure daily spending per person (USD), 2021 = **184** USD per person per day (2021-01-01..2021-12-31) [keep: ] quote: "Chicago leisure travelers' daily spending was $106 per person in 2020 and increased during the pandemic by 74% to $184 in 2021."
  - p163 Share of Chicago leisure travelers booking within one week of departure, 2022 = **45** % of travelers (2022-01-01..2022-12-31) [keep: ] quote: "While 45% of travelers booked their trip within one week of departure in 2022, only 37% booked during the pandemic."
- `https://www.choosechicago.com/press-media/press-releases/chicago-welcomes-56-8-million-tourists-in-2025-generating-a-record-breaking-21-5-billion-in-s` -> **live_dated** (page date 2026-06-25); points raw/verified 7/5
  - p164 Chicago total visitors in 2025 (annual count) = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "Chicago welcomed 56.8 million visitors in 2025, generating a record-setting $21.5 billion in visitor spending"
  - p165 Increase in Chicago visitors in 2025 vs 2024 = **1,500,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "The city welcomed nearly 1.5 million more visitors than in 2024, reflecting continued growth despite economic uncertainty"
  - p166 Chicago visitor spending in 2025 (annual total) = **21,500,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "generating a record-setting $21.5 billion in visitor spending and supporting 135,360 local jobs across the region"
  - p167 Local jobs supported by Chicago tourism in 2025 = **135,360** jobs (2025-01-01..2025-12-31) [keep: ] quote: "supporting 135,360 local jobs across the region, according to data released today by Choose Chicago"
  - p168 Share of leisure travelers planning to return within three years (2025 report) = **92** percent of leisure travelers (2025-01-01..2025-12-31) [keep: ] quote: "with 92% of leisure travelers indicating they plan to return within three years"
- dropped by code checks: 37 (value_as_written not in quote as a whole number: 2; period_end missing or unparseable: 16; scale word 'Million' not supported by quote or table header: 12; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 7)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['pizza consumption', 'chicago food', 'pizza sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2'] Both from the same USDA ARS dietary-intake analysis (2017-2020); p2 is a subpopulation of p1, not an independent measurement. Together they give a national pizza-consumption-day prevalence and an age 
- corroborating: ['p3', 'p4', 'p5', 'p6'] Same USDA source; meal-occasion shares of pizza intake. p4+p5 (children lunch+dinner = 89%) is consistent with p3 (~90% lunch+dinner overall). These are occasion splits, not mass or frequency.
- corroborating: ['p7', 'p8'] Same USDA source; p7 is a source-of-pizza share, p8 an energy-contribution share. Neither is a mass conversion factor directly, but p8 could support an energy-based mass bridge if a kcal/g for pizza w
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19'] All Chicago population figures from the same Census-vintage reporting (wlsam). p19 is a rounded restatement of p9; p15/p16/p17 are change statements consistent with the levels. Use p9 as the 2025 leve
- corroborating: ['p20', 'p21', 'p22'] Comparison-city populations from the same source; useful only as scale context, not as pizza evidence.
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] All from one Rentech Digital business-listing scrape (April 2026). p24 and p25 are duplicate statements of the same 1,987 count; p26/p27 and p28/p29 are numerator/share pairs. This is a directory coun
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] US pizzeria counts, industry revenue, and chain sales/units from businesstats (IBISWorld-derived). Chain sales/units give per-unit revenue benchmarks; industry revenue gives a national pizza-foodservi
- corroborating: ['p51', 'p52', 'p53', 'p54', 'p55'] Same dojobusiness benchmark page; p51 and p52 are the same 100 orders/day figure. p53 ($2,000/day) is consistent with 100 orders x $20 ticket. These are generic industry benchmarks, not Chicago-specif
- corroborating: ['p49', 'p56'] Same 'largest pizza' factoid from two aggregator sites; irrelevant to Chicago daily consumption.
- corroborating: ['p58', 'p59', 'p60', 'p63', 'p65'] US frozen-pizza retail dollar sales cluster around $7.2-7.5B for 2025-2026 from Circana/IMARC/Greenwich; p58 is the most current 52-week figure. These support the at-home retail channel.
- corroborating: ['p61', 'p62'] Global frozen-pizza market and North America share; only a sanity check on the US retail figure, not directly usable.
- corroborating: ['p64', 'p66'] Frozen-department household reach and frozen-entrée sales; context only, not pizza mass.
- corroborating: ['p67', 'p68', 'p69', 'p70'] Choose Chicago 2025 tourism release; p67 is annual visitors (56.8M), p68 the year-over-year increase. Visitors are person-trips, not person-days; converting to average daily present population require
- corroborating: ['p71', 'p72', 'p73', 'p74'] Census daytime-population estimate for Chicago (2017): daytime pop 2.92M vs resident ~2.72M, net commute inflow ~204k. This is the key exposure factor for the 'people present in Chicago' scope.
- corroborating: ['p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Daytime-population and commute-inflow figures for other cities; only analogues, not Chicago inputs.
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96'] Technomic/Restaurant Business QSR pizza category data: ~$31B 2025 sales, roughly flat nominal growth, mixed chain performance. Supports treating 2026 pizza demand as near-flat in real terms and using 
- corroborating: ['p97', 'p98', 'p99', 'p100', 'p101', 'p102'] CME cheese/butter prices for 2026; cheese is a major pizza input cost. Relevant to price-level shifts (d8) but not directly to mass.
- corroborating: ['p103'] Pizza Hut 2026 closures; a demand/supply shock signal consistent with flat-to-declining chain pizza volume.
- corroborating: ['p57'] Giordano's 2011 nationwide shipping volume; a Chicago deep-dish brand data point, but shipping volume is not local consumption and is a decade stale.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p130', 'p145'] All are USDA/NHANES-derived shares of the US population consuming pizza on any given day; p1 and p130 are duplicate statements of the same 11% figure from the same 2017-2020 WWEIA analysis, and p145 (
- corroborating: ['p2', 'p131'] Duplicate statements of the same 6% daily pizza prevalence among adults 60+ from the same USDA analysis; useful for age-structuring the prevalence but not independent.
- corroborating: ['p151', 'p152'] Children 20% vs adults 11% daily prevalence from the same 2007-2010 USDA analysis; consistent with p1/p145 and supports an age-weighted prevalence near 11-13%.
- corroborating: ['p3', 'p4', 'p5', 'p6', 'p132', 'p133', 'p134', 'p135', 'p147', 'p148', 'p149'] Meal-occasion shares of pizza intake from the same USDA analyses; internally consistent (lunch+dinner ~90%, snacks small). These describe when pizza is eaten, not how much, so they are contextual rath
- corroborating: ['p7', 'p136', 'p137', 'p138'] Source-of-pizza shares (restaurant 56%, grocery 26%, school 12%, other 6%) from the same USDA analysis; p7 and p138 are duplicate 'other' statements. These give the channel split needed to combine foo
- corroborating: ['p8', 'p150'] Both state pizza supplied ~27% of daily energy among pizza consumers; same underlying USDA measurement across two vintages.
- corroborating: ['p139', 'p140', 'p141', 'p142'] Energy-per-slice range (220-370 kcal) and mean per-consumer pizza energy (538 kcal children, 744 kcal adults) are from the same USDA source and are mutually consistent: ~2-3 slices per occasion. Toget
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18'] Census-derived Chicago population series from one secondary aggregator; internally consistent year-over-year changes. p9 (2,731,585 for 2025) is the best resident base for 2026.
- corroborating: ['p20', 'p21', 'p22'] Comparison-city populations from the same aggregator; only contextual, not used numerically.
- corroborating: ['p24', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] All from one business-listing snapshot (rentechdigital, April 2026) describing the same 1,987 Chicago pizza restaurants; the sub-counts are internally consistent but share one source and one definitio
- corroborating: ['p39', 'p40', 'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48'] US pizza industry revenue and chain sales/units from one secondary compilation; internally consistent and useful for per-unit revenue benchmarks, but not Chicago-specific.
- corroborating: ['p51', 'p53', 'p54', 'p55'] Industry-benchmark pizzeria economics (100 orders/day, ~$2,000/day revenue, $18-25 ticket) from one source; mutually consistent (100 x $20 = $2,000). These are generic benchmarks, not Chicago-measured
- corroborating: ['p58', 'p59', 'p60', 'p63', 'p65'] US frozen pizza retail dollar sales cluster around $7.2-7.5B across Circana/IMARC/Greenwich sources; overlapping measurement of the same retail category, so not independent, but a stable anchor for th
- corroborating: ['p67', 'p68', 'p164', 'p165'] Duplicate statements of 56.8M Chicago visitors in 2025 and the ~1.5M increase; same Choose Chicago release.
- corroborating: ['p69', 'p70', 'p166', 'p167'] Duplicate statements of $21.5B visitor spending and 135,360 tourism jobs; same source, contextual only.
- corroborating: ['p71', 'p72', 'p73', 'p74'] Census daytime-population components for Chicago 2017 from one aggregator; internally consistent (workers in city minus employed residents = net inflow). Supports an exposure factor for people present
- corroborating: ['p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p116', 'p117'] QSR/chain pizza sales and unit trends from Technomic-derived reporting; consistent picture of flat-to-slightly-negative real pizza demand in 2024-2025, relevant to the 2026 shock adjustment.
- corroborating: ['p97', 'p98', 'p99', 'p100', 'p101', 'p102'] CME cheese/butter prices in 2026 from one trade source; consistent within the period and relevant to price-driven USD-to-mass conversion, not to physical mass directly.
- corroborating: ['p104', 'p105'] Chicago MSA restaurant employment projections from the National Restaurant Association; same source, contextual for foodservice scale.
- corroborating: ['p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115'] Chicago deep-dish market-size report; internally consistent segment shares summing to 100%. However the 'global' framing and market-research provenance make it a weak, non-authoritative anchor for tot
- corroborating: ['p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p128'] Chicago deep-dish chain restaurant counts and valuations from one article; contextual only, not a mass driver.
- corroborating: ['p129', 'p139', 'p140'] USDA slice reference (14-inch cheese pizza) and kcal-per-slice range; together they define the per-slice mass/energy basis needed for the prevalence route.
- corroborating: ['p154', 'p155', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p168'] Choose Chicago / Illinois tourism metrics; internally consistent and useful only for the visitor exposure factor (nights, party size, spend), not for pizza mass directly.
- conflicting: ['p24', 'p39'] Chicago listing count (1,987 pizzerias) vs US total (74,000 businesses) implies Chicago holds ~2.7% of US pizzerias while holding ~0.8% of US population — a plausible pizza-culture premium but also a 

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Mean pizza mass consumed per pizza-eating occasion (grams) | 250 | 150..400 | 150..400 | g per occasion | unused | USDA per-consumer pizza energy of 538 kcal (children) and 744 kcal (adults) (p141, p142) at 220-370 kcal per slice (p139, p140) implies roughly 2-3 slices; at ~100-130 kcal/100 g for cheese pizza that is ~200-350 g. 250 g central with a band covering thin vs deep-dish and child vs adult. | Applied to a daily pizza-consumer prevalence rate to convert occasions to mass; assumes one eating occasion per consumer-day, consistent with NHANES 'intake day' framing. | Evidence that Chicago consumers eat materially more slices per occasion (e.g., deep-dish pies at 400+ g/serving) or that multiple pizza occasions per consumer-day are common. |
| a2 | Chicago pizza-culture prevalence multiplier vs US average | 1.15 | 1..1.4 | 0.8367..1.673 (widened) | ratio | unused | Chicago's deep-dish and tavern-style pizza culture plausibly raises daily pizza prevalence modestly above the 11% US average (p1/p130), but no Chicago-specific dietary data exist; a 1.0-1.4 band brackets 'no premium' to a strong local premium. | Used to scale the national 11% daily prevalence to Chicago residents. | Chicago-specific food-intake survey showing prevalence at or below the national 11%. |
| a3 | Average daily present population / resident population ratio for Chicago | 1.1 | 1.03..1.2 | 0.7861..1.572 (widened) | ratio | unused | Census daytime population (p71) vs resident base implies a ~1.07 commuter uplift; adding tourists (56.8M visitors, p67/p164, at ~2-3 nights each) adds a few percent more. Net ~1.10 with a 1.03-1.20 band. | Applied to resident-based consumption to capture pizza eaten by commuters and visitors within city boundaries (target scope a). | Evidence that visitors/commuters eat pizza at much lower rates, or a much larger tourist-night total than assumed. |
| a4 | Average pizza mass per foodservice order (grams) | 900 | 600..1,400 | 600..1,400 | g per order | unused | A typical order is ~1 medium/large pie (8 slices at ~110 g = ~880 g) or equivalent; deep-dish pies are heavier. 900 g central with 600-1400 g band. | Used with pizzeria count and daily orders to estimate foodservice pizza mass. | Evidence that Chicago orders average multiple pies or that single slices dominate order mix. |
| a5 | Effective active-pizzeria fraction of listed Chicago pizza restaurants | 0.75 | 0.55..0.9 | 0.4975..0.995 (widened) | fraction | unused | Business-listing counts (p24, 1,987) include chains, ghost kitchens, and closed units; the true count of operating pizzerias selling meaningful daily volume is lower. 0.75 central with a wide band. | Applied to the listed pizzeria count to get active pizzerias contributing to daily output. | A verified registry of active Chicago pizzerias showing near-100% of listings operating. |
| a6 | Chicago share of US frozen pizza retail sales (per-capita parity) | 0.0082 | 0.006..0.011 | 0.005745..0.01149 (widened) | fraction | unused | Chicago's ~2.73M residents are ~0.82% of the US population; assuming per-capita frozen pizza purchases at national parity gives ~0.82% of the $7.3B US frozen pizza market (p58). Band reflects possible local premium/discount. | Used to allocate national frozen pizza retail dollars to Chicago households. | Chicago-specific retail scanner data showing materially different per-capita frozen pizza spend. |
| a7 | Retail price per kg of frozen pizza (USD/kg) | 9 | 6.5..13 | 6.5..13 | USD per kg | unused | Frozen pizza retails roughly $4-8 per 400-600 g pie, i.e. ~$7-13/kg; $9/kg central with a band covering private-label to premium. | Converts Chicago frozen pizza retail dollars to mass. | Scanner data showing average frozen pizza price per kg well outside $6.5-13. |
| a8 | Average pizza mass per foodservice dollar (kg per USD) | 0.045 | 0.03..0.065 | 0.03..0.065 | kg per USD | unused | At ~$20 per order (p54, p55) and ~900 g per order (a4), mass per dollar is ~0.045 kg/USD; band covers ticket and pie-size variation. Used to convert Chicago foodservice pizza dollars to mass. | Applied to Chicago-attributable foodservice pizza revenue to get foodservice pizza mass. | Evidence that Chicago pizza prices per kg differ materially from the ~$22/kg implied here. |

Rejected by code:

- a9 Chicago share of US population (for allocating national pizza totals): id must be a1..a8
- a10 Non-frozen at-home pizza mass as a fraction of frozen retail pizza mass: id must be a1..a8

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input k: id k_grams_per_kg unknown or discarded |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input k: id k_grams_per_kg unknown or discarded |
| m3 | formula_mc | n/a | ['p58'] / ['a6', 'a7'] | [] |  | 0.00 |  | covers only retail_at_home of channel, so code does not combine it with full estimates; sum it with its siblings (foodservice) in one method, with an allowance assumption for parts without evidence |
| m4 | formula_mc | n/a |  | [] |  | 0.00 |  | input a9: assumption a9 was rejected (id must be a1..a8) |
| m5 | formula_mc | n/a |  | [] |  | 0.00 |  | input a9: assumption a9 was rejected (id must be a1..a8) |

- m1 coverage: the whole target
- m2 coverage: only foodservice of channel (siblings retail_at_home)
- m3 coverage: only retail_at_home of channel (siblings foodservice); not combined (its own estimate 17.71)
- m4 coverage: only foodservice of channel (siblings retail_at_home)
- m5 coverage: sum over channel of foodservice, retail_at_home

Result: central **n/a** t/day, 80% interval [n/a, n/a] t/day, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-12-31, after as_of: it cannot have been published yet


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

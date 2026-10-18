# Evidence ledger: smoke_pizza

- Question: How many tonnes of pizza do people in Chicago eat on an average day in 2026?
- as_of: 2026-10-18
- Pinned target: Total mass of pizza consumed by people in Chicago (city of Chicago, Illinois) on an average day in calendar year 2026, counting all pizza eaten by residents and visitors within the city, expressed as metric tons per day | unit metric tons per day | period 2026-01-01..2026-12-31 | publisher No official publisher; analyst-constructed estimate

## Directions and pages

### d1 [related_series] National/industry pizza sales data

Hypothesis: US per-capita pizza consumption (kg/person/year) multiplied by Chicago population gives total pizza mass; Chicago consumption assumed near national average, adjusted for Chicago's strong pizza culture. Target = per-capita rate × population / 365.

Queries issued by the searcher: US per capita pizza consumption pounds per year; how much pizza does the average American eat per year statistics; USDA ERS pizza consumption per capita data food availability; Chicago pizza sales statistics number of pizzerias Chicago market

- `https://www.ars.usda.gov/research/publications/publication/?seqNo115=421153` -> **live_dated** (page date 2026-10-17); points raw/verified 12/10
  - p1 Share of US population consuming pizza on any given day (NHANES 2017-March 2020  = **11** % (2017-01-01..2020-03-31) [keep: ] quote: "Overall, 11% of the population consumed pizza on any given day."
  - p2 Pizza contribution to total energy intake, US population (NHANES 2017-March 2020 = **27** % (2017-01-01..2020-03-31) [DISCARD: Pizza share of energy intake; not a mass or frequency input and already discarded.] quote: "Pizza contributed about 27% to total energy intake."
  - p3 Share of pizza consumed at lunch by children and adolescents = **41** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, almost half of pizza was consumed at lunch (41%) and at dinner (48%)"
  - p4 Share of pizza consumed at dinner by children and adolescents = **48** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, almost half of pizza was consumed at lunch (41%) and at dinner (48%)"
  - p5 Share of pizza consumption by adults at dinner = **58** % (2017-01-01..2020-03-31) [keep: ] quote: "almost two thirds (58%) of pizza consumption by adults was at dinner"
  - p6 Average slices of pizza consumed by males at an eating occasion = **4** as written "four", value check ok slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males consumed four and females consumed three slices of pizza at an eating occasion."
  - p7 Average slices of pizza consumed by females at an eating occasion = **3** as written "three", value check pending slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males consumed four and females consumed three slices of pizza at an eating occasion."
  - p8 Share of pizza obtained from the grocery store = **0.25** as written "one quarter", value check pending percent of pizza obtained (2017-01-01..2020-03-31) [keep: ] quote: "Over half of pizza was obtained from restaurants and one quarter was obtained from the grocery store."
  - p9 Pizza contribution to total fat intake (about one-third) = **0.3333** as written "one-third", value check pending percent of total fat intake (2017-01-01..2020-03-31) [DISCARD: Fat-intake share; irrelevant to mass.] quote: "About one-third of total fat, saturated fat, and sodium intakes were from pizza."
  - p10 Pizza contribution to total energy intake (over one-quarter) = **0.25** as written "one-quarter", value check pending percent of total energy intake (one-sided bound) (2017-01-01..2020-03-31) [DISCARD: Energy-intake share; irrelevant to mass.] quote: "Pizza contributed over one-quarter of total energy intake."
- `https://www.tastingtable.com/1854781/where-pizza-most-popular/` -> **live_dated** (page date 2025-05-15); points raw/verified 9/0
- `https://www.pmq.com/pizza-huts-annual-trends-report-32-percent-of-consumers-will-eat-more-pizza-this-year/` -> **live_dated** (page date 2025-01-09); points raw/verified 15/12
  - p11 Average pizza slices eaten per person per year, US (Pizza Hut report) = **288** slices per person per year (2024-01-01..2024-12-31) [keep: ] quote: "Americans eat an average of 288 slices of pizza per person each year."
  - p12 Pizza volume equivalent per person per year, US (stated as gallons of pizza) = **480** gallons of pizza per person per year (2024-01-01..2024-12-31) [DISCARD: 'Gallons of pizza' is a nonsensical marketing unit; unusable.] quote: "this is the equivalent of 480 gallons of pizza per person"
  - p13 Total pizza slices eaten nationwide per year, US (Pizza Hut report) = **95,000,000,000** slices per year (2024-01-01..2024-12-31) [DISCARD: Nationwide slice total from a marketing report; not a Chicago input and duplicates p11's basis.] quote: "or 95 billion slices nationwide"
  - p14 Share of consumers planning to eat more pizza this year than in 2024, US = **32** % (2024-01-01..2024-12-31) [DISCARD: Intent-to-eat-more survey share; not a volume measure.] quote: "32% of consumers said they plan on eating more pizza this year than they did in 2024"
  - p15 Number of American adults polled in Pizza Hut trends study = **5,000** adults surveyed (2024-01-01..2024-12-31) [DISCARD: Poll sample size; irrelevant.] quote: "5,000 American adults, split evenly by state, were polled by market research company Talker Research"
  - p16 Chicago Deep Dish share of preferred pizza style vote, US respondents = **22** % (2024-01-01..2024-12-31) [DISCARD: Style-preference vote share; not a mass input.] quote: "Chicago Deep Dish (22%), Sicilian (8%) and Detroit-style pizza (4%) also received a portion of the vote share."
  - p17 New York-style share of preferred pizza style vote, US respondents = **29** % (2024-01-01..2024-12-31) [DISCARD: Style-preference vote share; not a mass input.] quote: "New York-style pizza led the way, winning 29% of the vote."
  - p18 North Dakota average slices per sitting per month (highest state) = **9.9** slices per sitting per month (2024-01-01..2024-12-31) [DISCARD: North Dakota slices per sitting; irrelevant to Chicago.] quote: "North Dakota consumes more pizza on average than any other state, eating 9.9 slices per sitting per month."
  - p19 Friday share as most popular day to eat pizza, US respondents = **43** % (2024-01-01..2024-12-31) [DISCARD: Day-of-week preference; not a mass input.] quote: "Friday (43%) was by far the most popular day to eat pizza."
  - p20 Share of Americans agreeing pizza and wings are the ultimate pairing = **59** % (2024-01-01..2024-12-31) [DISCARD: Pairing preference; irrelevant.] quote: "Over half of Americans (59%) agree that pizza and wings are "the ultimate pairing,""
  - p21 Share of Americans who enjoy dipping pizza into sauces = **58** % (2024-01-01..2024-12-31) [DISCARD: Dipping preference; irrelevant.] quote: "Pizza Hut found that more than half (58%) of Americans enjoy dipping their pizza into sauces"
  - p22 Number of Olympic-sized swimming pools pizza would fill, US annual (Pizza Hut re = **240,000** Olympic-sized swimming pools (2024-01-01..2024-12-31) [DISCARD: Swimming-pool marketing analogy; unusable.] quote: "That is enough pizza to fill 240,000 Olympic-sized swimming pools"
- `https://www.euronews.com/culture/2025/01/17/its-world-pizza-day-from-italy-to-the-conquest-of-the-world` -> **live_dated** (page date 2025-01-17); points raw/verified 14/4
  - p23 Global pizza turnover 2024 (projected) = **160,000,000,000** euros per year (2024-01-01..2024-12-31) [DISCARD: Global turnover; not Chicago.] quote: "global pizza turnover in 2024 is projected to reach a record €160 billion"
  - p24 Italy pizza turnover contribution 2024 = **15,000,000,000** euros per year (2024-01-01..2024-12-31) [DISCARD: Italy turnover; not Chicago.] quote: "with Italy contributing €15 billion to this figure"
  - p25 Share of Italian families expected to prepare pizza at home in 2025 = **0.4** as written "four out of ten", value check pending share of families (2025-01-01..2025-12-31) [DISCARD: Italian home-pizza share; irrelevant.] quote: "In Italy, four out of ten families are expected to prepare pizza at home in 2025"
  - p26 Year-on-year growth in pizza delivery turnover 2024 to 2025 = **20** percent growth (2024-01-01..2025-12-31) [DISCARD: Delivery turnover growth; not a Chicago mass input.] quote: "Others point to year-on-year growth in turnover of 20 per cent between 2024 and 2025."
- dropped by code checks: 24 (value_as_written not in quote as a whole number: 4; period_end missing or unparseable: 20)

### d2 [related_series] Chicago restaurant/foodservice sales

Hypothesis: Chicago pizza restaurant revenue × implied price per tonne of pizza gives mass sold through foodservice; add retail/frozen pizza. Target = (foodservice pizza revenue / price per kg) + retail pizza mass, divided by 365.

Queries issued by the searcher: Chicago pizza restaurants number revenue statistics; Chicago restaurant industry sales statistics 2025 total revenue; pizza sales Chicago market size Technomic independent pizzerias sales; average American consumes pounds of pizza per year per capita pizza consumption

- `https://rentechdigital.com/smartscraper/it/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p27 Number of pizza restaurants in Chicago as of April 1, 2026 = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Ci sono 1987 Pizza restaurants in Chicago al April 1, 2026"
  - p28 Pizza restaurants in Chicago that are single-owner operations (count) = **914** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant with p45 (same 914 count).] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p29 Share of Chicago pizza restaurants that are single-owner operations (numerator 9 = **46** % (2026-04-01..2026-04-01) [DISCARD: Redundant with p46.] quote: "che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago"
  - p30 Pizza restaurants in Chicago that are part of larger brands (count) = **1,073** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Redundant with p47.] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p31 Share of Chicago pizza restaurants that are part of larger brands (numerator 107 = **54** % (2026-04-01..2026-04-01) [DISCARD: Redundant with p48.] quote: "le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p32 Average age of pizza restaurants in Chicago = **10** years (2026-04-01..2026-04-01) [DISCARD: Average restaurant age; irrelevant to mass.] quote: "Average age of Pizza restaurants in Chicago is10 anni e 2 mesi."
  - p33 Pizza restaurants in Chicago with their own website (count) = **1,848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Website count; irrelevant.] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web"
  - p34 Pizza restaurants in Chicago without their own website (count) = **139** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Website count; irrelevant.] quote: "e i restanti 139 non hanno un proprio sito web"
  - p35 Pizza restaurants in Chicago with Facebook pages (count) = **1,048** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "1048 hanno pagine Facebook"
  - p36 Pizza restaurants in Chicago active on Instagram (count) = **848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "848 sono attivi su Instagram"
  - p37 Pizza restaurants in Chicago with X accounts (count) = **635** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "635 hanno account su X (precedentemente Twitter)"
  - p38 Pizza restaurants in Chicago with LinkedIn profiles (count) = **88** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "88 hanno profili LinkedIn"
  - p39 Pizza restaurants in Chicago on TikTok (count) = **189** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "189 sono su TikTok"
  - p40 Pizza restaurants in Chicago with YouTube channels (count) = **151** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Social-media count; irrelevant.] quote: "151 have YouTube channels"
  - p41 Pizza restaurants in Chicago with email addresses listed (count) = **217** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Email-listing count; irrelevant.] quote: "217 Indirizzi email"
- `https://growjo.com/company/Pequod` -> **live_dated** (page date 2026-01-01); points raw/verified 0/0
- `https://chicagocitywire.com/chicago-restaurant-industry-faces-closures-amid-economic-pressures-and-declining-demand` -> **live_dated** (page date 2025-09-29); points raw/verified 11/0
- `https://foodeist.com/index.php/pizza-statistics` -> **live_dated** (page date 2026-03-10); points raw/verified 12/0
- dropped by code checks: 23 (period_end missing or unparseable: 20; value_as_written not in quote as a whole number: 3)

### d3 [capacity_consumption] Pizza establishments (supply side)

Hypothesis: Number of Chicago pizza-serving establishments × average pizzas sold per day × average pizza mass = total pizza sold per day. Target = establishment count × daily volume × mass per pizza.

Queries issued by the searcher: how many pizzerias in Chicago number of pizza restaurants; how many pizzas does a pizzeria sell per day average; average pizza weight whole 14 inch pizza grams how much does a pizza weigh; PMQ Pizza Magazine average pizzas sold per day per pizzeria survey

- `https://rentechdigital.com/smartscraper/it/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p42 Count of pizza restaurants in Chicago (as of April 1, 2026) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Ci sono 1987 Pizza restaurants in Chicago al April 1, 2026"
  - p43 Count of pizza restaurants in Chicago (restated total) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Ci sono un totale di 1987 Ristoranti di pizza in Chicago al April 01, 2026."
  - p44 Percent change in Chicago pizza restaurants vs 2023 = **0** % (2023-01-01..2026-04-01) [DISCARD: Zero percent change; no information.] quote: "il che rappresenta un aumento del 0.00% rispetto a 2023"
  - p45 Single-owner pizza restaurants in Chicago (count) = **914** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p46 Share of Chicago pizza restaurants that are single-owner operations = **46** % (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p47 Pizza restaurants in Chicago that are part of larger brands (count) = **1,073** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p48 Share of Chicago pizza restaurants that are part of larger brands = **54** % (2026-04-01..2026-04-01) [keep: ] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p49 Average age of pizza restaurants in Chicago = **10** years (2026-04-01..2026-04-01) [DISCARD: Duplicate of p32.] quote: "Average age of Pizza restaurants in Chicago is10 anni e 2 mesi."
  - p50 Chicago pizza restaurants with own website (count) = **1,848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p33.] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web e i restanti 139 non hanno un proprio sito web."
  - p51 Chicago pizza restaurants without own website (count) = **139** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p34.] quote: "e i restanti 139 non hanno un proprio sito web"
  - p52 Chicago pizza restaurants with Facebook pages (count) = **1,048** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p35.] quote: "1048 hanno pagine Facebook"
  - p53 Chicago pizza restaurants with Instagram accounts (count) = **848** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p36.] quote: "848 sono attivi su Instagram"
  - p54 Chicago pizza restaurants with LinkedIn profiles (count) = **88** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p38.] quote: "88 hanno profili LinkedIn"
  - p55 Chicago pizza restaurants with X accounts (count) = **635** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p37.] quote: "635 hanno account su X (precedentemente Twitter)"
  - p56 Chicago pizza restaurants with TikTok profiles (count) = **189** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Duplicate of p39.] quote: "189 sono su TikTok"
- `https://pantagraph.com/1-chicago-illinois/article_e935387b-c05b-5f55-b2ed-f376830102b5.html` -> **live_dated** (page date 2016-09-19); points raw/verified 4/0
- `https://www.usatoday.com/picture-gallery/life/food/2025/09/16/photos-downtown-house-of-pizza-in-fort-myers-turns-20/86156664007/` -> **dropped** (live http 402); points raw/verified -/-
- `https://platelens.app/blog/how-many-calories-in-a-slice-of-pizza` -> **live_dated** (page date 2026-09-06); points raw/verified 15/8
  - p57 Whole 14-inch chain cheese pizza weight, USDA measured (FDC 173292) = **853** grams per whole pizza (2019-01-01..2019-12-31) [keep: ] quote: "USDA weighed the whole pie at 853 g and one slice at 107 g."
  - p58 One slice weight, one eighth of 14-inch chain cheese pizza, USDA measured = **107** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "One slice as USDA measured it: 107 g, one eighth of a 14-inch (35.6 cm) chain cheese pizza, regular crust."
  - p59 Slices per 14-inch pie implied by USDA whole-pie and slice weights = **7.97** slices per pie (2019-01-01..2019-12-31) [keep: ] quote: "Divide 853 by 107 and you get 7.97 - the arithmetic way of saying the pie was cut into eight."
  - p60 Areal density of 14-inch chain cheese pizza (derived from USDA measurement) = **5.54** grams per square inch (2019-01-01..2019-12-31) [DISCARD: Derived areal density; redundant with p92.] quote: "Its 853 g spread over that area gives an areal density of 5.54 grams per square inch"
  - p61 Grams per slice when measured 853 g 14-inch pie is cut into 6 slices = **142** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 6 slices \| 142 g \| 378 kcal \|"
  - p62 Grams per slice when measured 853 g 14-inch pie is cut into 10 slices = **85** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 10 slices \| 85 g \| 227 kcal \|"
  - p63 Grams per slice when measured 853 g 14-inch pie is cut into 12 pieces = **71** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 12 pieces \| 71 g \| 189 kcal \|"
  - p64 Energy density of chain cheese pizza, USDA measured = **266** as written "266 kcal per 100 g", value check pending kcal per 100 grams (2019-01-01..2019-12-31) [DISCARD: Duplicate of p83.] quote: "USDA FoodData Central measured one chain cheese pizza at 266 kcal per 100 g (FDC 173292)"
- dropped by code checks: 11 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; period_end missing or unparseable: 7)

### d4 [base_rates] Consumer survey / eating frequency

Hypothesis: Share of people eating pizza on a given day × average servings per eater × serving mass × exposed population = daily pizza mass. Target = frequency × servings × mass × population.

Queries issued by the searcher: percentage of Americans eat pizza on a given day survey; NHANES pizza consumption frequency percent of population day; average pizza slice weight grams 100 grams per slice survey; Chicago population 2025 estimate Census city of Chicago residents

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/15
  - p65 Share of U.S. population (2+ years) consuming pizza on any given day, NHANES 201 = **11** % (2017-01-01..2020-03-31) [keep: ] quote: "On any given day, about 11% of the population consumed pizza."
  - p66 Share of older adults (60+) consuming pizza on any given day, NHANES 2017-March  = **6** % (2017-01-01..2020-03-31) [DISCARD: Duplicate of p181.] quote: "the percentage consuming decreased to about 6% among older adults (60+)"
  - p67 Average slices of pizza consumed by males at an eating occasion, NHANES 2017-Mar = **4** as written "four", value check pending slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males had four and females had three slices of pizza at an eating occasion."
  - p68 Average slices of pizza consumed by females at an eating occasion, NHANES 2017-M = **3** as written "three", value check pending slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males had four and females had three slices of pizza at an eating occasion."
  - p69 Reference slice definition: fraction of a 14-inch fast food/restaurant cheese pi = **0.1667** as written "1/6", value check pending fraction of a 14-inch pizza (..) [DISCARD: Reference slice fraction; redundant with p82.] quote: "One slice of pizza is approximately 1/6 of 14-inch fast food/restaurant cheese pizza with a regular crust (7)."
  - p70 Share of pizza consumed at lunch by children 2-19 years = **41** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p71 Share of pizza consumed at dinner by children 2-19 years = **48** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p72 Share of pizza consumed at dinner by adults 20+ years = **58** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "4 28 58 10"
  - p73 Share of pizza consumed at lunch by adults 20+ years = **28** percent of pizza intake (2017-01-01..2020-03-31) [DISCARD: Adult lunch share; contextual only, redundant with p5/p72.] quote: "4 28 58 10"
  - p74 Share of pizza obtained from restaurants = **56** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p75 Share of pizza obtained from grocery stores = **26** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p76 Share of pizza obtained from school/daycare = **12** percent of pizza consumed (2017-01-01..2020-03-31) [DISCARD: School/daycare share; not needed for a mass route.] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p77 Share of pizza obtained from 'Other' sources = **6** % (2017-01-01..2020-03-31) [DISCARD: Duplicate of p187.] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources"
  - p78 Share of pizza consumed at snacks = **4** % (2017-01-01..2020-03-31) [DISCARD: Duplicate of p186.] quote: "Snacks accounted for 4% of pizza intake."
  - p79 Total NHANES individuals 2+ years providing dietary intake data (sample size) = **13,444** individuals (2017-01-01..2020-03-31) [DISCARD: Duplicate of p189.] quote: "A total of 13,444 individuals 2 years of age and older"
- `https://www.ncbi.nlm.nih.gov/books/NBK610659/figure/usdaddb62.fig2b/` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0
- `https://platelens.app/blog/how-many-calories-in-a-slice-of-pizza` -> **live_dated** (page date 2026-09-06); points raw/verified 15/15
  - p80 Weight of one slice of USDA-measured 14-inch chain cheese pizza (one eighth of p = **107** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "USDA weighed the whole pie at 853 g and one slice at 107 g."
  - p81 Weight of whole USDA-measured 14-inch chain cheese pizza = **853** grams per whole pie (2019-01-01..2019-12-31) [keep: ] quote: "USDA weighed the whole pie at 853 g and one slice at 107 g."
  - p82 Number of slices the USDA-measured 14-inch pie was cut into (853/107) = **7.97** slices per pie (2019-01-01..2019-12-31) [keep: ] quote: "Divide 853 by 107 and you get 7.97 - the arithmetic way of saying the pie was cut into eight."
  - p83 Energy density of USDA-measured chain cheese pizza = **266** kcal per 100 g (2019-01-01..2019-12-31) [keep: ] quote: "USDA FoodData Central measured one chain cheese pizza at 266 kcal per 100 g (FDC 173292)"
  - p84 Calories per slice of USDA-measured 14-inch pie (one eighth) = **285** kcal per slice (2019-01-01..2019-12-31) [DISCARD: Derived calories per slice; redundant with p83/p58.] quote: "an eighth of a 14-inch pie is 107 g and 285 kcal"
  - p85 Derived weight of one eighth slice of 12-inch cheese pizza (area-scaled, not mea = **78** grams per slice (2019-01-01..2019-12-31) [DISCARD: Area-scaled derived slice mass; not measured, redundant.] quote: "\| 12′′ (30.5 cm) \| 113.1 sq in \| 627 g · 1,667 kcal \| 78 g \| 208 kcal \|"
  - p86 Derived weight of one eighth slice of 18-inch cheese pizza (area-scaled, not mea = **176** grams per slice (2019-01-01..2019-12-31) [DISCARD: Area-scaled derived slice mass; not measured, redundant.] quote: "the same eighth of an 18-inch pie is 176 g and 469 kcal"
  - p87 Derived whole-pie weight of 12-inch cheese pizza (area-scaled, not measured) = **627** grams per whole pie (2019-01-01..2019-12-31) [DISCARD: Area-scaled derived pie mass; not measured, redundant.] quote: "\| 12′′ (30.5 cm) \| 113.1 sq in \| 627 g · 1,667 kcal \| 78 g \| 208 kcal \|"
  - p88 Derived whole-pie weight of 18-inch cheese pizza (area-scaled, not measured) = **1,410** grams per whole pie (2019-01-01..2019-12-31) [DISCARD: Area-scaled derived pie mass; not measured, redundant.] quote: "\| 18′′ (45.7 cm) \| 254.5 sq in \| 1,410 g · 3,751 kcal \| 176 g \| 469 kcal \|"
  - p89 Grams per slice when the measured 853 g 14-inch pie is cut into 6 slices = **142** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 6 slices \| 142 g \| 378 kcal \|"
  - p90 Grams per slice when the measured 853 g 14-inch pie is cut into 10 slices = **85** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 10 slices \| 85 g \| 227 kcal \|"
  - p91 Grams per slice when the measured 853 g 14-inch pie is cut into 12 pieces = **71** grams per slice (2019-01-01..2019-12-31) [keep: ] quote: "\| 12 pieces \| 71 g \| 189 kcal \|"
  - p92 Areal density of USDA-measured 14-inch cheese pizza (grams per square inch) = **5.54** grams per square inch (2019-01-01..2019-12-31) [keep: ] quote: "Its 853 g spread over that area gives an areal density of 5.54 grams per square inch"
  - p93 Calories per gram of regular-crust cheese pizza = **2.66** kcal per gram (2019-01-01..2019-12-31) [keep: ] quote: "At 2.66 kcal per gram for regular-crust cheese, weighing the slice skips every assumption above at once."
  - p94 Ratio of 18-inch to 12-inch pie area (and slice mass at equal cut count) = **2.25** ratio (times) (2019-01-01..2019-12-31) [DISCARD: Area ratio; not needed.] quote: "the same one-eighth slice becomes 2.25 times as much food"
- `https://www.ncbi.nlm.nih.gov/books/NBK589563/` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0

### d5 [physical_flow] Ingredient/flour throughput

Hypothesis: Flour (or cheese) delivered to Chicago pizza makers × conversion to pizza mass gives pizza produced; target = ingredient mass × (pizza mass / ingredient mass) / 365. Cross-check on supply-side routes.

Queries issued by the searcher: flour used per pizza dough ratio pounds flour per pizza; Chicago pizza cheese consumption annual tons; how many pizzas sold per day in Chicago number of pizzerias; Chicago pizza industry statistics pizzerias number slice sold

- `https://chicago.eater.com/2014/3/20/6260173/pizza-by-the-numbers-dimos-bar-toma-and-ranallis` -> **live_dated** (page date 2014-03-20); points raw/verified 15/15
  - p95 Dimo's Pizza pounds of dough used in a month = **24,000** pounds of dough per month (2014-01-01..2014-12-31) [keep: ] quote: "What Dimo's Pizza goes through in a month: Pounds of dough: 24000"
  - p96 Dimo's Pizza pounds of Mozzarella used in a month = **7,056** pounds of mozzarella per month (2014-01-01..2014-12-31) [keep: ] quote: "Pounds of Mozzarella: 7056"
  - p97 Dimo's Pizza number of slices sold in a month = **29,760** slices sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Number of slices sold: 29760"
  - p98 Bar Toma pounds of Imported Italian flour used in a month = **5,000** pounds of flour per month (2014-01-01..2014-12-31) [DISCARD: Single-restaurant flour use; too narrow and old for a city flow.] quote: "Pounds of Imported Italian flour: 5,000"
  - p99 Bar Toma pounds of fior di latte from Wisconsin used in a month = **2,400** pounds of fior di latte per month (2014-01-01..2014-12-31) [DISCARD: Single-restaurant cheese use; too narrow and old.] quote: "Pounds of fior di latte from Wisconsin: 2,400"
  - p100 Bar Toma pounds of rye flour used in a month = **100** pounds of rye flour per month (2014-01-01..2014-12-31) [DISCARD: Single-restaurant rye flour; irrelevant.] quote: "Pounds of rye flour: 100"
  - p101 Ranalli's pizzas per week (lower bound) = **1,200** pizzas per week (2014-01-01..2014-12-31) [keep: ] quote: "Pizzas per week: 1200 - 1500"
  - p102 Ranalli's pizzas per week (upper bound) = **1,500** pizzas per week (2014-01-01..2014-12-31) [keep: ] quote: "Pizzas per week: 1200 - 1500"
  - p103 Ranalli's pizzas per month = **5,000** pizzas per month (2014-01-01..2014-12-31) [keep: ] quote: "Pizzas per month: 5000"
  - p104 Ranalli's pounds of cheese used in a week = **600** pounds of cheese per week (2014-01-01..2014-12-31) [DISCARD: Single-restaurant weekly cheese; too narrow and old.] quote: "Pounds of cheese: 600"
  - p105 Ranalli's Thin Crust pizzas sold in a month = **3,000** pizzas sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Thin Crust: 3000"
  - p106 Ranalli's Chicago Stuffed pizzas sold in a month = **525** pizzas sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Chicago Stuffed: 525"
  - p107 Ranalli's Pan Pizza sold in a month = **350** pizzas sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Pan Pizza: 350"
  - p108 Ranalli's Double Deckers sold in a month = **200** pizzas sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Double Deckers: 200"
  - p109 Ranalli's Gluten Free pizzas sold in a month = **175** pizzas sold per month (2014-01-01..2014-12-31) [keep: ] quote: "Gluten Free: 175"
- `https://www.pmq.com/the-numbers-and-nuances-of-dough/` -> **live_dated** (page date 2023-03-16); points raw/verified 15/0
- `https://chicago.eater.com/2012/5/11/6587185/by-the-numbers-roots-giordanos-lou-malnatis` -> **live_dated** (page date 2012-05-11); points raw/verified 14/1
  - p110 Giordano's pizzas shipped nationwide in 2011 = **26,888** pizzas shipped nationwide (2011-01-01..2011-12-31) [keep: ] quote: "· Number of pizzas shipped nationwide in 2011: 26,888"
- `https://www.chicagotribune.com/2006/12/28/second-city-digits/` -> **live_dated** (page date 2006-12-28); points raw/verified 15/0
- dropped by code checks: 43 (period_end missing or unparseable: 43)

### d6 [related_series] Population and visitor exposure

Hypothesis: Chicago's exposed population (residents + commuters + tourists, weighted by days present) is the multiplier for per-capita routes; target scales linearly with this exposure. Provides the denominator/numerator bridge for d1 and d4.

Queries issued by the searcher: Chicago population 2025 Census estimate; Chicago daytime population commuters estimate; Chicago tourism visitors annual statistics 2024 2025; Choose Chicago average length of stay overnight visitors nights 2025; Census daytime population city 2020 commuter-adjusted Chicago 2,9 million

- `https://cdn.choosechicago.com/uploads/2026/09/Chicago-Tourism-Overview-2025.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/3
  - p111 Chicago hotel occupancy rate, 2025, percent = **69.2** percent (2025-01-01..2025-12-31) [DISCARD: Duplicate of p149/p161 (69.1%).] quote: "Occupancy Rate (%) 43.0 60.4 65.3 68.1 69.2"
  - p112 Chicago average daily hotel rate, 2025, dollars = **243** dollars per room night (2025-01-01..2025-12-31) [DISCARD: Hotel rate; not needed.] quote: "Average Daily Rate $181.22 $228.58 $228.37 $241.86 $243.31"
  - p113 Chicago total visitation year-over-year % change, 2025 = **2.6** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p118/p152 growth.] quote: "Total (Domestic + International) 30.71 48.62 51.97 55.35 56.77 % Change 85.9% 58.3% 6.9% 6.5% 2.6%"
- `https://www.census.gov/quickfacts/fact/table/cookcountyillinois,chicagocityillinois,IL/PST045224` -> **dropped** (live http 403); points raw/verified -/-
- `https://investor.clearchannel.com/news/detail/528/clear-channel-outdoor-now-offers-brands-the-opportunity-to-capture-high-demand-business-consumers-ac` -> **live_dated** (page date 2025-04-10); points raw/verified 5/3
  - p114 Residential population of downtown Chicago area (2023 Census Estimates) = **23,793** people (2023-01-01..2023-12-31) [DISCARD: Downtown residential population; sub-area, not the city exposure population.] quote: "According to the 2023 Census Estimates, the residential population of this area is 23,793"
  - p115 Daytime (working) population of downtown Chicago area (2023 Census Estimates) = **284,083** people (2023-01-01..2023-12-31) [DISCARD: Downtown daytime population; sub-area only, not city-wide.] quote: "and the daytime (working) population is 284,083, making this a compelling opportunity for advertisers to reach commuters every day."
  - p116 Number of Chicago companies on the 2024 Fortune 500 list = **15** companies (2024-01-01..2024-12-31) [DISCARD: Fortune 500 count; irrelevant.] quote: "home to 15 ranked companies on the 2024 Fortune 500 list"
- `https://www.choosechicago.com/press-media/press-releases/chicago-welcomes-56-8-million-tourists-in-2025-generating-a-record-breaking-21-5-billion-in-s` -> **live_dated** (page date 2026-06-25); points raw/verified 9/7
  - p117 Chicago visitors in 2025 (annual visitor count) = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "Chicago welcomed 56.8 million visitors in 2025, generating a record-setting $21.5 billion in visitor spending"
  - p118 Increase in Chicago visitors 2025 vs 2024 = **1,500,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "The city welcomed nearly 1.5 million more visitors than in 2024, reflecting continued growth despite economic uncertainty"
  - p119 Chicago visitor spending in 2025 = **21,500,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of p159.] quote: "generating a record-setting $21.5 billion in visitor spending and supporting 135,360 local jobs across the region"
  - p120 Local jobs supported by Chicago tourism in 2025 = **135,360** jobs (2025-01-01..2025-12-31) [DISCARD: Tourism jobs; irrelevant to mass.] quote: "supporting 135,360 local jobs across the region, according to data released today by Choose Chicago"
  - p121 Chicago visitors in 2025 (rounded, quoted by Governor) = **57,000,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, nearly 57 million visitors from around the globe learned what we already know"
  - p122 Share of leisure travelers planning to return within three years = **92** % (2025-01-01..2025-12-31) [DISCARD: Return-intent share; irrelevant.] quote: "with 92% of leisure travelers indicating they plan to return within three years"
  - p123 Number of Chicago neighborhoods covered by tourism jobs = **77** neighborhoods (2025-01-01..2025-12-31) [DISCARD: Neighborhood count; irrelevant.] quote: "supporting more than 135,000 local jobs across all 77 neighborhoods"
- dropped by code checks: 16 (scale word 'million' not supported by quote or table header: 12; period_end missing or unparseable: 4)

### d7 [own_history] Historical Chicago pizza consumption proxies

Hypothesis: If any prior estimate of Chicago pizza consumption or sales exists, extrapolate to 2026 using population and price/volume growth. Target_2026 = historical value × growth factor.

Queries issued by the searcher: Chicago pizza consumption estimate tons per year; Chicago pizza market size sales billions; "Chicago" pizza "pounds of dough" per year Loyola University Chicago pizza consumption study; pizza sales growth United States 2024 2025 percent

- `https://chicago.eater.com/2012/5/11/6587185/by-the-numbers-roots-giordanos-lou-malnatis` -> **live_dated** (page date 2012-05-11); points raw/verified 15/1
  - p124 Giordano's pizzas shipped nationwide in 2011 = **26,888** pizzas shipped nationwide (2011-01-01..2011-12-31) [keep: ] quote: "Number of pizzas shipped nationwide in 2011: 26,888"
- `https://marketintelo.com/report/chicago-deep-dish-pizza-restaurant-market` -> **live_dated** (page date 2026-06-11); points raw/verified 15/10
  - p125 Global Chicago deep-dish pizza restaurant market value, 2025 base year = **900,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "The Chicago Deep-Dish Pizza Restaurant market is valued at $0.9 billion in 2025 and is projected to reach $1.2 billion by 2034"
  - p126 Illinois and Chicago area share of North American Chicago deep-dish pizza market = **65** % (2025-01-01..2025-12-31) [keep: ] quote: "Illinois and the Chicago area alone accounting for approximately 65.0% of total market revenue"
  - p127 Dine-In segment share of Chicago deep-dish pizza market revenue, 2025 = **38.5** % (2025-01-01..2025-12-31) [DISCARD: Duplicate of p128 segment share.] quote: "Dine-In segment held largest share at 38.5%"
  - p128 Dine-In segment annual revenue, 2025 = **350,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 38.5% of total market revenue in 2025, generating approximately $0.35 billion in annual revenue"
  - p129 Takeout segment annual revenue, 2025 = **250,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 28.3% of total market revenue in 2025, generating approximately $0.25 billion in annual revenue"
  - p130 Delivery segment annual revenue, 2025 = **200,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 22.0% of total market revenue in 2025, generating approximately $0.20 billion in annual revenue"
  - p131 Catering segment annual revenue, 2025 = **100,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "accounting for 11.2% of total market revenue in 2025, generating approximately $0.10 billion in annual revenue"
  - p132 Chicago visitors in 2024 (overnight and same-day) = **58,300,000** visitors (2024-01-01..2024-12-31) [DISCARD: 2024 visitor count; superseded by 2025 p117.] quote: "the city attracted approximately 58.3 million overnight and same-day visitors in 2024"
  - p133 Share of Chicago visitors actively seeking deep-dish pizza experiences, 2024 = **40** (range 35..45) as written "35-45%", value check pending % (2024-01-01..2024-12-31) [DISCARD: Deep-dish-seeking share; not a mass input.] quote: "with an estimated 35-45% of visitors actively seeking deep-dish pizza experiences during their stay"
  - p134 Active Chicago deep-dish pizza restaurant locations and delivery operations, 202 = **450** (range 400..500) as written "400-500", value check pending locations (2025-01-01..2025-12-31) [DISCARD: Deep-dish location count; narrow segment, not total pizza.] quote: "spanning approximately 400-500 active restaurant locations and delivery operations across all geographic markets"
- dropped by code checks: 19 (period_end missing or unparseable: 17; period_end 2034-12-31 after as_of: 2)

### d8 [shocks] Price and demand conditions 2025-2026

Hypothesis: Pizza prices, inflation, and demand shifts in 2025-2026 change per-capita volume; adjust historical or national rates for real price changes and any demand shocks. Target = baseline volume × demand adjustment.

Queries issued by the searcher: pizza price inflation 2025 2026; restaurant pizza demand trends 2025 traffic decline; Chicago pizza consumption per day estimate slices pizzas; Chicago restaurant closures 2026 pizzeria closing costs

- `https://www.thestreet.com/restaurants/pizza-hut-rival-papa-johns-closing-hundreds-of-restaurants` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.rabobank.com/knowledge/q011479495-weakness-in-us-pizza-chains-drags-down-pizza-box-demand` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.semafor.com/article/01/06/2026/pizzas-popularity-wanes-in-us` -> **live_dated** (page date 2026-01-06); points raw/verified 1/0
- `https://www.chicagotribune.com/1988/03/24/ingredients-of-a-great-food-town-3/` -> **live_dated** (page date 2021-08-08); points raw/verified 2/2
  - p135 Chicago per-capita pizza meals per year (1986 survey) = **34.8** pizza meals per person per year (1986-01-01..1986-12-31) [keep: ] quote: "Chicagoans were named the nation`s biggest pizza fans in a 1986 survey that has us sitting down to pizza 34.8 times a year."
  - p136 Los Angeles per-capita pizza meals per year (1986 survey, upper bound stated as  = **20** pizza meals per person per year (upper bound) (1986-01-01..1986-12-31) [DISCARD: LA comparison; not needed once Chicago's own 1986 figure is kept.] quote: "Los Angeles, the home of designer pizzas, averaged less than 20 per capita pizza meals annually."
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b1 [base_rates] population exposure

Hypothesis: A current (2020s) estimate of Chicago's daytime/commuter population and average visitor-days would let the per-capita route (d1/d4) use an exposure population rather than residents only; this is the largest scope uncertainty in the target.

Queries issued by the searcher: Census Bureau daytime population Chicago commuters; Choose Chicago average length of stay visitors 2024 2025; Chicago daytime population 2023 Census estimate million workers commuting into city; Choose Chicago "average length of stay" visitors nights

- `https://cdn.choosechicago.com/uploads/2026/06/cc_2025_economic_impact_midyear_v.2.pdf` -> **live_dated** (page date 2026-06-01); points raw/verified 15/14
  - p137 Total visitors to Chicago (domestic & international), 2025 = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "VISITORS \| 56.8 MILLION 2.6% GROWTH"
  - p138 Domestic leisure visitors to Chicago, 2025 = **40,700,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "40.7 MILLION DOMESTIC LEISURE VISITORS"
  - p139 Domestic overnight visitors to Chicago, 2025 = **29,200,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "29.2 MILLION DOMESTIC OVERNIGHT VISITORS"
  - p140 Domestic day-trip business visitors to Chicago, 2025 = **5,700,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "5.7 MILLION DOMESTIC DAY-TRIP BUSINESS VISITORS"
  - p141 International visitors to Chicago, 2025 = **1,900,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "1.9 MILLION INTERNATIONAL VISITORS"
  - p142 Average spend per overnight leisure travel party to Chicago, per stay = **1,342** US dollars per stay (..) [keep: ] quote: "Overnight leisure travel parties to Chicago spend an average of $1,342 per stay."
  - p143 Share of all Chicago visits occurring in summer = **34** % (..) [keep: ] quote: "Summer trips are the most common, accounting for 34% of all visits"
  - p144 Share of all Chicago visits occurring in fall = **28** % (..) [keep: ] quote: "though fall (28%), winter (22%), and spring (16%) each receive significant tourism activity."
  - p145 Share of all Chicago visits occurring in winter = **22** % (..) [keep: ] quote: "though fall (28%), winter (22%), and spring (16%) each receive significant tourism activity."
  - p146 Share of all Chicago visits occurring in spring = **16** % (..) [keep: ] quote: "though fall (28%), winter (22%), and spring (16%) each receive significant tourism activity."
  - p147 Share of Chicago visitors whose top activity is dining = **25** % (..) [keep: ] quote: "Top tourism activities include dining (25% of visitors), shopping (21%), sightseeing (14%), and museums or art exhibits (12%)."
  - p148 Average daily hotel rooms in Chicago, 2025 = **47,009** hotel rooms (2025-01-01..2025-12-31) [keep: ] quote: "AVERAGE DAILY HOTEL ROOMS \| 47,009"
  - p149 Chicago hotel occupancy rate, 2025 = **69.1** % (2025-01-01..2025-12-31) [keep: ] quote: "OCCUPANCY \| 69.1% (1.5% GROWTH)"
  - p150 Future citywide bookings in Chicago in 2025 = **65** bookings (2025-01-01..2025-12-31) [keep: ] quote: "65 FUTURE CITYWIDE BOOKINGS IN 2025"
- `https://www.chicagotribune.com/2026/06/25/choose-chicago-tourism/` -> **live_dated** (page date 2026-06-25); points raw/verified 15/15
  - p151 Chicago total visitors (residents and visitors, all origins), 2025 = **56,800,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "Chicago saw an increase in tourism last year, with 56.8 million visitors spending a record $21.5 billion in the Windy City"
  - p152 Increase in Chicago visitors, 2025 vs 2024 = **1,500,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "The city welcomed nearly 1.5 million more visitors than in 2024 as it continues to climb back toward pre-pandemic levels"
  - p153 Chicago international visitors, 2025 = **1,900,000** international visitors (2025-01-01..2025-12-31) [keep: ] quote: "there were 1.9 million international visitors to Chicago last year, an 8% decline, according to Choose Chicago"
  - p154 Year-over-year decline in Chicago international visitors, 2025 = **8** % (2025-01-01..2025-12-31) [keep: ] quote: "there were 1.9 million international visitors to Chicago last year, an 8% decline, according to Choose Chicago"
  - p155 Chicago international visitors, 2024 = **2,000,000** international visitors (2024-01-01..2024-12-31) [keep: ] quote: "In 2024, Chicago topped 2 million international visitors for the first time in the post-pandemic travel landscape."
  - p156 Nationwide decline in inbound international visits, 2025 = **5.5** % (2025-01-01..2025-12-31) [keep: ] quote: "including a nationwide 5.5% decline in inbound international visits, according to the U.S. Travel Association"
  - p157 Chicago domestic leisure visitors, 2025 = **40,700,000** domestic leisure visitors (2025-01-01..2025-12-31) [keep: ] quote: "The biggest area of growth for Chicago tourism in 2025 was the 40.7 million domestic leisure visitors, up 4.8% year-over-year"
  - p158 Year-over-year growth in Chicago domestic leisure visitors, 2025 = **4.8** % (2025-01-01..2025-12-31) [keep: ] quote: "the 40.7 million domestic leisure visitors, up 4.8% year-over-year, according to Choose Chicago"
  - p159 Chicago tourism spending, 2025 (record) = **21,500,000,000** US dollars (2025-01-01..2025-12-31) [keep: ] quote: "with tourism spending at a record $21.5 billion last year, up 2.7%, according to Choose Chicago"
  - p160 Chicago hotel revenue, 2025 = **2,900,000,000** US dollars (2025-01-01..2025-12-31) [keep: ] quote: "Chicago hotel revenue hit $2.9 billion in 2025, up from $2.8 billion the previous year"
  - p161 Chicago hotel occupancy rate, 2025 = **69.1** % (2025-01-01..2025-12-31) [keep: ] quote: "Hotel occupancy was at 69.1% for the year, up 1.5% over 2024."
  - p162 Chicago record annual visitors, 2019 = **61,000,000** visitors (2019-01-01..2019-12-31) [keep: ] quote: "Chicago first crossed that threshold in 2017 and set a record at 61 million visitors in 2019."
  - p163 Chicago visitors, 2020 (pandemic trough) = **16,000,000** visitors (2020-01-01..2020-12-31) [keep: ] quote: "But visits fell to 16 million in 2020 at the onset of the COVID-19 pandemic"
  - p164 Choose Chicago original visitor goal for 2020 = **55,000,000** visitors per year (2020-01-01..2020-12-31) [keep: ] quote: "Choose Chicago initially set a goal of 55 million visitors a year by 2020"
  - p165 Chicago visitors, 2025 (rounded restatement) = **57,000,000** visitors (2025-01-01..2025-12-31) [keep: ] quote: "While the city attracted nearly 57 million visitors in 2025, it has yet to claw back to pre-pandemic levels."
- `https://cmap.illinois.gov/download/6184/?tmstv=1729877213` -> **live_dated** (page date 2026-06-04); points raw/verified 14/14
  - p166 City of Chicago total population (ACS 2020-2024, 2024 estimate) = **2,711,226** people (2024-01-01..2024-12-31) [keep: ] quote: "Total Population 14,394 2,711,226 8,495,320"
  - p167 City of Chicago total households (ACS 2020-2024, 2024 estimate) = **1,160,205** households (2024-01-01..2024-12-31) [keep: ] quote: "Total Households 6,652 1,160,205 3,301,388"
  - p168 City of Chicago average household size (ACS 2020-2024) = **2.3** people per household (2024-01-01..2024-12-31) [keep: ] quote: "Average Household Size 2.2 2.3 2.5"
  - p169 City of Chicago total commuters (workers 16+, ACS 2020-2024) = **1,078,013** commuters (2024-01-01..2024-12-31) [keep: ] quote: "TOTAL COMMUTERS 7,209 88.1 1,078,013 79.0 3,448,348 81.5"
  - p170 City of Chicago workers working at home (ACS 2020-2024) = **286,353** workers (2024-01-01..2024-12-31) [keep: ] quote: "Work at Home* 971 11.9 286,353 21.0 783,713 18.5"
  - p171 City of Chicago employed residents (ACS 2020-2024) = **1,395,899** people (2024-01-01..2024-12-31) [keep: ] quote: "Employed * 8,461 95.7 1,395,899 91.9 4,310,932 93.5"
  - p172 O'Hare community area total population (ACS 2020-2024, 2024 estimate) = **14,394** people (2024-01-01..2024-12-31) [keep: ] quote: "Total Population 14,394 2,711,226 8,495,320"
  - p173 Employment in O'Hare community area, total workers at O'Hare workplaces (LEHD 20 = **29,995** workers (2023-01-01..2023-12-31) [keep: ] quote: "1.Transportation 29,995 60.2"
  - p174 O'Hare community area workers in Transportation sector (LEHD 2023) = **60.2** percent of workers in O'Hare (2023-01-01..2023-12-31) [keep: ] quote: "1.Transportation 29,995 60.2"
  - p175 O'Hare community area workers in Accommodation and Food Service sector (LEHD 202 = **4,055** workers (2023-01-01..2023-12-31) [keep: ] quote: "2. Accommodation and Food Service 4,055 8.1"
  - p176 O'Hare community area residents commuting to The Loop for work (LEHD 2023) = **896** workers (2023-01-01..2023-12-31) [keep: ] quote: "1.The Loop 896 16.6"
  - p177 O'Hare community area residents working in O'Hare (LEHD 2023) = **411** workers (2023-01-01..2023-12-31) [keep: ] quote: "2. O'Hare 411 7.6"
  - p178 City of Chicago mean commute time (ACS 2020-2024) = **33.1** minutes (2024-01-01..2024-12-31) [keep: ] quote: "Mean Commute Time (Minutes) 27.8 33.1 30.5"
  - p179 City of Chicago percent population change 2010-24 (ACS/Census) = **0.6** percent (2010-01-01..2024-12-31) [keep: ] quote: "Percent Population Change, 2010-24 12.8 0.6 0.8"
- `https://skyscraperpage.com/forum/showpost.php?p=10056436&postcount=6&s=4c603590a83fc1a43224e2b5f9178654` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (scale word 'million' not supported by quote or table header: 1)

### b2 [related_series] per-capita volume

Hypothesis: A measured US per-capita pizza consumption in kg/year (e.g., USDA ERS or industry shipment data) would replace the marketing '288 slices' claim and anchor the d1 route with a defensible rate.

Queries issued by the searcher: USDA ERS pizza consumption per capita kg per year; US per capita pizza consumption pounds per year; "Consumption of Pizza in the United States" What We Eat in America dietary data brief 62 grams per day; frozen pizza retail sales volume per capita US Nielsen 2024 pounds

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/10
  - p180 Share of U.S. population (2+ years) consuming pizza on any given day, NHANES 201 = **11** % (2017-01-01..2020-03-31) [keep: ] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p181 Share of U.S. adults 60+ consuming pizza on any given day, NHANES 2017-March 202 = **6** % (2017-01-01..2020-03-31) [keep: ] quote: "the percentage consuming decreased to about 6% among older adults (60+)"
  - p182 Average slices of pizza consumed by males at an eating occasion, NHANES 2017-Mar = **4** as written "four", value check pending slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males had four and females had three slices of pizza at an eating occasion."
  - p183 Average slices of pizza consumed by females at an eating occasion, NHANES 2017-M = **3** as written "three", value check pending slices per eating occasion (2017-01-01..2020-03-31) [keep: ] quote: "On average, males had four and females had three slices of pizza at an eating occasion."
  - p184 Share of pizza intake consumed at lunch by children 2-19 years, NHANES 2017-Marc = **41** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p185 Share of pizza intake consumed at dinner by children 2-19 years, NHANES 2017-Mar = **48** % (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p186 Share of pizza intake from snacks, NHANES 2017-March 2020 = **4** % (2017-01-01..2020-03-31) [keep: ] quote: "Snacks accounted for 4% of pizza intake."
  - p187 Share of pizza obtained from 'Other' sources, NHANES 2017-March 2020 = **6** % (2017-01-01..2020-03-31) [keep: ] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources such as a sport or entertainment facility or a convenience store"
  - p188 Pizza contribution to total daily energy intake among pizza consumers, NHANES 20 = **27** % (2017-01-01..2020-03-31) [keep: ] quote: "Overall, pizza contributed about 27% to total energy intake of pizza consumers on the intake day."
  - p189 Total NHANES individuals 2+ years providing complete dietary intake data (sample = **13,444** individuals (2017-01-01..2020-03-31) [keep: ] quote: "A total of 13,444 individuals 2 years of age and older (6,689 males and 6,755 females) provided complete and reliable dietary intake data."
- `https://www.ncbi.nlm.nih.gov/books/NBK589563/` -> **live_dated** (page date 2026-10-11); points raw/verified 0/0
- `https://www.tastingtable.com/1854781/where-pizza-most-popular/` -> **live_dated** (page date 2025-05-15); points raw/verified 9/0
- `https://www.expertmarketresearch.com/reports/united-states-pizza-market` -> **live_dated** (page date 2026-07-24); points raw/verified 8/1
  - p190 US pizza market value, base year 2025 = **22,790,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "The United States pizza market was approximately USD 22.79 Billion in 2025."
- dropped by code checks: 21 (period_end missing or unparseable: 14; value_as_written not in quote as a whole number: 4; period_end 2035-12-31 after as_of: 2; number: more than one number in value_as_written: 1)

### b3 [capacity_consumption] foodservice throughput

Hypothesis: Average daily pizzas sold per Chicago pizza establishment (from POS or industry benchmarks) would convert the 1,987-restaurant count into realised volume, completing the d3 route.

Queries issued by the searcher: pizza restaurant average daily orders benchmark independent pizzeria; independent pizzeria average weekly pizza sales number of pizzas per week; PMQ Pizza Magazine annual pizza industry census average weekly sales per pizzeria average ticket; Slice pizza app average number of pizzas sold per day per pizzeria data

- `https://slice.com/blog/pizzeria-more-demand-not-more-seats/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.pmq.com/pizza-power-report-2026-pizzeria-failure-rate-is-not-what-you-think/` -> **live_dated** (page date 2026-04-03); points raw/verified 15/7
  - p191 Average annual sales of top-quartile Slice pizzeria clients (2025) = **658,548** US dollars per year (2025-01-01..2025-12-31) [keep: ] quote: "the top quartile of its pizzeria clients logs annual sales of $658,548, on average"
  - p192 Median annual sales of top-quartile Slice pizzeria clients (2025) = **561,278** US dollars per year (2025-01-01..2025-12-31) [keep: ] quote: "annual median sales for that same group comes in at $561,278"
  - p193 Year-over-year increase in orders for indie pizza (Slice, 2025) = **20** % (2025-01-01..2025-12-31) [keep: ] quote: "We're seeing around a 20% year-over-year increase in orders for indie pizza"
  - p194 Restaurateurs providing input to R365 mid-2025 report = **5,000** restaurateurs (2025-01-01..2025-12-31) [keep: ] quote: "The report reflected input from 5,000-plus restaurateurs across all segments."
  - p195 Share of R365 respondents reporting labor costs up this year = **89** % (2025-01-01..2025-12-31) [keep: ] quote: "89% of respondents said their labor costs shot up this year"
  - p196 Share of R365 respondents reporting food costs up = **91** % (2025-01-01..2025-12-31) [keep: ] quote: "91% said their food costs were up, too."
  - p197 Share of R365 respondents expecting food cost rise of 11% to 25% due to tariffs = **29** % (2025-01-01..2025-12-31) [keep: ] quote: "29% expect increases in the range of 11% to 25%"
- `https://mediagrouponlineinc.com/wp-content/uploads/2020/01/Pizza-Market-Profiler-2020.docx` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://pos.toasttab.com/zh-us/blog/on-the-line/how-much-do-pizza-shops-make` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 8 (number: no number in value_as_written: 1; period_end missing or unparseable: 5; value_as_written not in quote as a whole number: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['pizza consumption', 'chicago food', 'pizza sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p65'] Same NHANES 2017–March 2020 finding (11% consume pizza on any given day) reported twice; identical underlying measurement, not independent.
- corroborating: ['p6', 'p7', 'p67', 'p68'] Same NHANES slice-per-occasion figures (males 4, females 3) restated; one underlying source.
- corroborating: ['p3', 'p4', 'p70', 'p71'] Same child/adolescent lunch 41% / dinner 48% split restated.
- corroborating: ['p5', 'p72'] Adults' 58% dinner share restated from same NHANES brief.
- corroborating: ['p8', 'p74', 'p75'] Grocery-store share ~25–26% and restaurant ~56% from same NHANES source; consistent.
- corroborating: ['p57', 'p58', 'p59', 'p80', 'p81', 'p82'] USDA FDC 173292 whole-pie 853 g and 107 g slice restated across d3/d4; one measurement.
- corroborating: ['p61', 'p62', 'p63', 'p89', 'p90', 'p91'] Same 853 g pie re-cut into 6/10/12 pieces; arithmetic restatements, not independent.
- corroborating: ['p27', 'p42', 'p43'] Same 1,987 Chicago pizza restaurants as of 2026-04-01 restated; one directory snapshot.
- corroborating: ['p28', 'p29', 'p45', 'p46'] 914 single-owner / 46% restated.
- corroborating: ['p30', 'p31', 'p47', 'p48'] 1,073 brand-affiliated / 54% restated.
- corroborating: ['p95', 'p96', 'p97'] Dimo's 2014 monthly dough, mozzarella and slice counts from one Eater Chicago piece; internally consistent single-restaurant flow data.
- corroborating: ['p101', 'p102', 'p103'] Ranalli's weekly 1,200–1,500 and monthly 5,000 pizzas from same 2014 article; consistent.
- corroborating: ['p105', 'p106', 'p107', 'p108', 'p109'] Ranalli's style breakdown sums to ~4,250/month, consistent with 5,000 total.
- corroborating: ['p110', 'p124'] Giordano's 2011 nationwide shipment count restated; one figure, and it is shipments not Chicago consumption.
- corroborating: ['p117', 'p121'] 56.8M vs 'nearly 57M' visitors 2025; same Choose Chicago release.
- conflicting: ['p117', 'p132'] 2025 visitors 56.8M vs 2024 visitors 58.3M from a market-research page; the 2024 figure is higher than 2025 despite Choose Chicago reporting ~1.5M growth, so the marketintelo visitor count is unreliab
- corroborating: ['p11', 'p13'] 288 slices/person × ~330M ≈ 95B slices; internally consistent Pizza Hut PR arithmetic, but a marketing claim, not a measurement.
- corroborating: ['p11', 'p12', 'p22'] Same Pizza Hut trend release; 480 gallons and 240,000 pools are rhetorical restatements of the same volume claim.
- corroborating: ['p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131'] Deep-dish market segments sum to $0.9B; one market-research report, and it covers deep-dish only, not all pizza.
- corroborating: ['p133', 'p134'] Same marketintelo report; 35–45% visitor deep-dish interest and 400–500 locations are analyst estimates, not measurements.
- corroborating: ['p135', 'p136'] Same 1986 survey reported in Tribune; Chicago 34.8 vs LA <20 pizza meals/year — a relative ranking, 40 years old.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p65', 'p180'] All three are the same NHANES 2017-March 2020 finding (11% of the US population 2+ consumed pizza on a given day) reported in USDA pages; they are one underlying measurement, not independent confirmat
- corroborating: ['p6', 'p7', 'p67', 'p68', 'p182', 'p183'] Same NHANES result (males 4, females 3 slices per eating occasion) restated across USDA pages. One measurement; the male/female split implies a population-weighted occasion average near 3.5 slices, wh
- corroborating: ['p3', 'p4', 'p5', 'p70', 'p71', 'p72', 'p184', 'p185'] Meal-occasion shares (children lunch 41%/dinner 48%, adults dinner 58%) from the same NHANES analysis. Contextual only; they do not enter a mass formula directly.
- corroborating: ['p8', 'p74', 'p75'] Source-of-pizza shares: restaurant ~56%, grocery ~25-26%. Same NHANES source; useful as the restaurant/grocery split for a channel-sum route, but note the two vintages differ slightly (25% vs 26% groc
- corroborating: ['p57', 'p58', 'p59', 'p80', 'p81', 'p82'] USDA-measured 14-inch chain cheese pizza: 853 g whole, 107 g per eighth slice, 7.97 slices per pie. Internally consistent (853/107). This is the best measured slice/pie mass anchor; it is a chain chee
- corroborating: ['p61', 'p62', 'p63', 'p89', 'p90', 'p91'] Alternative cut counts of the same 853 g pie; they are arithmetic restatements, not new measurements. Useful only to show slice mass depends on cut count.
- corroborating: ['p27', 'p42', 'p43'] Same Rentech Digital count of 1,987 Chicago pizza restaurants as of 2026-04-01, restated three times. One source; a directory count, not verified active establishments, and it excludes non-pizza resta
- corroborating: ['p45', 'p46', 'p47', 'p48'] Owner/brand split of the same 1,987 count; internally consistent (914+1073=1987). Contextual only.
- corroborating: ['p95', 'p96', 'p97'] Dimo's 2014 monthly dough, mozzarella and slice volumes from one Chicago pizzeria. Single-establishment, 12 years old; usable only as a scale check on per-establishment volume, not as a city total.
- corroborating: ['p101', 'p102', 'p103', 'p105', 'p106', 'p107', 'p108', 'p109'] Ranalli's 2014 monthly pizza counts by style; the style breakdown sums to ~4,250 vs the stated 5,000 total, a minor internal inconsistency. Single high-volume Chicago pizzeria; a scale check, not a ci
- corroborating: ['p110', 'p124'] Giordano's 2011 nationwide shipment count, duplicated. Nationwide shipments, not Chicago consumption; not usable as a Chicago mass input.
- corroborating: ['p117', 'p121', 'p137', 'p151', 'p165'] Choose Chicago / Tribune 2025 visitor count of 56.8M (rounded to ~57M in some restatements). One underlying source; use once.
- corroborating: ['p118', 'p152'] Same +1.5M visitor growth figure, duplicated.
- corroborating: ['p139', 'p140', 'p141', 'p157', 'p153', 'p155'] Visitor composition: 29.2M domestic overnight, 5.7M day-trip business, 40.7M domestic leisure, 1.9M international (down 8% from 2.0M in 2024). Consistent with the 56.8M total; useful for weighting vis
- corroborating: ['p148', 'p149', 'p161'] 47,009 average daily hotel rooms at 69.1% occupancy. A cross-check on overnight visitor-days (~11.9M room-nights), which is far below the 29.2M overnight visitor count, indicating the visitor count in
- corroborating: ['p166', 'p167', 'p168', 'p169', 'p170', 'p171'] CMAP/ACS 2020-2024 Chicago population 2,711,226, 1,160,205 households, 1,078,013 commuters, 286,353 work-at-home. Internally consistent (households × 2.3 ≈ population). These anchor the exposure popul
- corroborating: ['p125', 'p126', 'p128', 'p129', 'p130', 'p131'] Marketintelo deep-dish market figures: $0.9B global 2025, 65% Illinois/Chicago, segment revenues summing to $0.9B. A vendor market-research estimate of a narrow segment (deep-dish restaurants), not to
- conflicting: ['p135', 'p136'] 1986 survey: Chicago 34.8 pizza meals/year vs Los Angeles <20. Supports a Chicago-above-national culture multiplier, but is 40 years old and a 'meals' not mass measure; needs a time-gap adjustment.
- corroborating: ['p190', 'p191', 'p192'] US pizza market $22.79B (2025) and Slice top-quartile pizzeria sales ~$560-660k/yr. Provide a revenue-per-establishment scale check for the capacity route; top-quartile is above average, so average Ch

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Chicago exposure population (residents plus average daily visitor presence) | 3,100,000 | 2,750,000..3,600,000 | 2,224,860..4,449,719 (widened) | people | m1 (m1), m3 (m3) | Residents ~2.71M (p166). Commuters (p169) are largely residents already counted. 56.8M visitors/year (p117) with short stays add roughly 0.1-0.2M average daily presence; net exposure modestly above residents. | Per-capita routes are applied to all pizza eaten within city limits by anyone present. | A measured Chicago daytime/visitor-inclusive population materially outside 2.75-3.6M. |
| a2 | Chicago pizza-culture multiplier on the national per-capita rate | 1.15 | 1..1.35 | 0.8216..1.643 (widened) | ratio | m1 (m1) | 1986 survey (p135) put Chicago at 34.8 pizza meals/year, above LA (<20); Chicago has strong deep-dish/thin-crust culture, but national consumption has converged, so the advantage is likely modest today. | National NHANES frequency is transferred to Chicago. | Evidence that Chicago per-capita pizza consumption is at or below the national average. |
| a3 | Occasion-size adjustment (Chicago slices per occasion relative to NHANES male 4-slice figure) | 0.9 | 0.7..1.15 | 0.6344..1.269 (widened) | ratio | m1 (m1) | NHANES male 4 / female 3 slices implies a population-weighted occasion average near 3.5, ~0.88 of the male figure; Chicago deep-dish slices are heavier but fewer per sitting. | The male 4-slice figure is used as the occasion average. | Measured Chicago slices-per-occasion near 4 or above. |
| a4 | Average pizzas sold per Chicago pizza establishment per day | 45 | 20..90 | 20..90 | pizzas per establishment per day | m2 (m2) | Ranalli's (p103) sold ~5,000/month (~165/day) and Dimo's (p97) ~29,760 slices/month; these are high-volume Chicago pizzerias. The 1,987 directory count includes many small/low-volume shops, so the city average should be well below the high-volume examples. Centered ~45. | The 1,987 restaurant count is treated as active pizza-selling establishments. | POS data showing average Chicago pizzeria daily pizza volume far outside 20-90. |
| a5 | Average whole-pizza mass in Chicago | 1,050 | 800..1,500 | 775..1,549 (widened) | grams per pizza | m2 (m2) | USDA 14-inch chain cheese pizza is 853 g (p81); Chicago deep-dish and stuffed pies are heavier, thin-crust similar. A mix centered slightly above the chain cheese anchor. | Restaurant pizza mass is estimated from pizza counts. | Measured average Chicago pizza weight outside 800-1500 g. |
| a6 | Share of Chicago pizza mass sold through pizzerias/restaurants | 0.6 | 0.45..0.75 | 0.4108..0.8216 (widened) | share | m2 (m2) | NHANES source shares: restaurant ~56% (p74), grocery ~26% (p75), school/other remainder. Restaurant share is the complement of grocery plus other channels; centered near 0.6. | Restaurant-channel mass is scaled up to total pizza mass. | Evidence that restaurant share of Chicago pizza is far from 45-75%. |
| a7 | Time-gap adjustment for 1986 Chicago pizza-meal frequency to 2026 | 0.85 | 0.6..1.1 | 0.5745..1.149 (widened) | ratio | m3 (m3) | The 1986 survey (p135) predates four decades of menu diversification; national pizza frequency has been roughly flat-to-declining per capita. Centered slightly below 1 to reflect likely modest decline. | The 1986 Chicago frequency is used as a 2026 per-capita benchmark. | Evidence that Chicago pizza-meal frequency has risen since 1986. |
| a8 | Slices per pizza meal occasion (Chicago, 2026) | 3.5 | 2.5..4.5 | 2.372..4.743 (widened) | slices per occasion | m3 (m3) | NHANES male 4 / female 3 slices per occasion (p6, p7) implies a population-weighted average near 3.5; Chicago deep-dish slices are heavier but fewer per sitting, so the slice count is similar. Used to convert the 1986 meal frequency (p135) into slice mass. | The 1986 Chicago pizza-meal frequency is converted to slice mass. | Measured Chicago slices-per-occasion outside 2.5-4.5. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 154 | ['p1', 'p6', 'p81', 'p82'] / ['a1', 'a2', 'a3'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 158 | ['p27'] / ['a4', 'a5', 'a6'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 88.01 | ['p135', 'p81', 'p82'] / ['a1', 'a7', 'a8'] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **129** t/day, 80% interval [51.72, 321] t/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-12-31, after as_of: it cannot have been published yet


## Final answer

The best estimate for the total mass of pizza consumed within Chicago city limits by all persons present (residents plus average daily visitor presence), averaged over calendar year 2026, is 129 t/day (80% model-based interval 51.72 to 321 t/day). This combines 3 routes at equal weight: a per-capita frequency route (154 t/day), a restaurant-capacity route (158 t/day), and a Chicago-specific [n]-frequency route (88.01 t/day). Observed anchors include the US daily pizza-eating share 11%, male slices per occasion 4 slices per eating occasion, USDA pie mass 853 grams per whole pie cut into 7.97 slices per pie, 1,987 pizza restaurants, and the [n] Chicago meal frequency 34.8 pizza meals per person per year. Everything else rests on analyst assumptions: exposure population 3,100,000, culture multiplier 1.15, occasion adjustment 0.9, per-establishment volume 45, pizza mass 1,050, restaurant share 0.6, time-gap adjustment 0.85, and slices per occasion 3.5. The interval reflects input uncertainty only, not demonstrated accuracy. The biggest risk is the per-establishment volume and restaurant-share assumptions in the capacity route. Better evidence would be actual Chicago pizzeria sales volumes and a current local consumption survey.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Chicago exposure population (residents plus average daily visitor presence): 3,100,000 people, range 2,224,860 to 4,449,719 (range widened by code); used by m1, m3. Overturned by: A measured Chicago daytime/visitor-inclusive population materially outside [n]-[n]M.
- a2 Chicago pizza-culture multiplier on the national per-capita rate: 1.15 ratio, range 0.8216 to 1.643 (range widened by code); used by m1. Overturned by: Evidence that Chicago per-capita pizza consumption is at or below the national average.
- a3 Occasion-size adjustment (Chicago slices per occasion relative to NHANES male [n]-slice figure): 0.9 ratio, range 0.6344 to 1.269 (range widened by code); used by m1. Overturned by: Measured Chicago slices-per-occasion near [n] or above.
- a4 Average pizzas sold per Chicago pizza establishment per day: 45 pizzas per establishment per day, range 20 to 90; used by m2. Overturned by: POS data showing average Chicago pizzeria daily pizza volume far outside [n]-[n].
- a5 Average whole-pizza mass in Chicago: 1,050 grams per pizza, range 775 to 1,549 (range widened by code); used by m2. Overturned by: Measured average Chicago pizza weight outside [n]-[n] g.
- a6 Share of Chicago pizza mass sold through pizzerias/restaurants: 0.6 share, range 0.4108 to 0.8216 (range widened by code); used by m2. Overturned by: Evidence that restaurant share of Chicago pizza is far from [n]-[n].
- a7 Time-gap adjustment for [n] Chicago pizza-meal frequency to 2026: 0.85 ratio, range 0.5745 to 1.149 (range widened by code); used by m3. Overturned by: Evidence that Chicago pizza-meal frequency has risen since [n].
- a8 Slices per pizza meal occasion (Chicago, 2026): 3.5 slices per occasion, range 2.372 to 4.743 (range widened by code); used by m3. Overturned by: Measured Chicago slices-per-occasion outside [n]-[n].

# Evidence ledger: smoke_pizza

- Question: How many tonnes of pizza do people in Chicago eat on an average day in 2026?
- as_of: 2026-10-17
- Pinned target: Total mass of pizza consumed by people in Chicago (city of Chicago, all pizza types: thin, deep-dish, frozen/prepared, restaurant and at-home) on a single average day in calendar year 2026, measured as pizza mass as sold/served | unit metric tons per day | period 2026-01-01..2026-12-31 | publisher No official publisher; analyst-constructed estimate from population, consumption-survey, and food-service data

## Directions and pages

### d1 [related_series] National food-consumption survey analyst

Hypothesis: US per-capita pizza consumption (kg/person/year) from USDA/ERS or NHANES-style dietary intake data, multiplied by Chicago population, gives a first-order total; Chicago's pizza culture may push its per-capita above or below the national average, so a Chicago adjustment factor is needed.

Queries issued by the searcher: US per capita pizza consumption kg per year USDA ERS; NHANES pizza intake grams per day adults; pizza consumption by region United States per capita regional differences survey; Chicago pizza consumption per capita pizzeria density pizzerias per capita

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/8
  - p1 Share of U.S. population consuming pizza on any given day (all, 2+ years) = **11** percent of population (2017-01-01..2020-03-31) [keep: ] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p2 Share of U.S. population 60+ consuming pizza on any given day = **6** percent of population (2017-01-01..2020-03-31) [keep: ] quote: "the percentage consuming decreased to about 6% among older adults (60+)."
  - p3 Pizza contribution to total daily energy intake among pizza consumers, all = **27** percent of total energy intake (2017-01-01..2020-03-31) [keep: ] quote: "Overall, pizza contributed about 27% to total energy intake of pizza consumers on the intake day."
  - p4 Share of pizza intake at lunch, children 2-19 years = **41** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p5 Share of pizza intake at dinner, children 2-19 years = **48** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p6 Share of pizza intake from snacks = **4** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Snacks accounted for 4% of pizza intake."
  - p7 Share of pizza obtained from 'Other' sources = **6** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources such as a sport or entertainment facility or a convenience store"
  - p8 Total NHANES individuals 2+ years providing dietary intake data (sample size) = **13,444** individuals (2017-01-01..2020-03-31) [DISCARD: Sample size of the NHANES survey (13,444 individuals) — a study-design statistic, not a quantity relevant to pizza mass ] quote: "A total of 13,444 individuals 2 years of age and older (6,689 males and 6,755 females) provided complete and reliable dietary intake data."
- `https://faseb.onlinelibrary.wiley.com/doi/10.1096/fasebj.30.1_supplement.lb407` -> **dropped** (live http 403); points raw/verified -/-
- `https://brilliantmaps.com/pizza-consumption/` -> **live_dated** (page date 2026-10-12); points raw/verified 7/0
- `https://www.foodandwine.com/frozen-pizza-trends-instacart-report-11919729` -> **live_dated** (page date 2026-03-05); points raw/verified 15/15
  - p9 Pepperoni share of frozen pizza items sold on Instacart platform, 2025 = **43** % of frozen pizza items sold (2025-01-01..2025-12-31) [DISCARD: Pepperoni share of frozen pizza items — flavor mix, irrelevant to total mass.] quote: "pepperoni accounted for 43% of all frozen pizza items sold on the platform in 2025"
  - p10 Plain cheese share of frozen pizza items sold on Instacart platform, 2025 = **26.6** % of frozen pizza items sold (2025-01-01..2025-12-31) [DISCARD: Plain cheese share of frozen pizza items — flavor mix, irrelevant to total mass.] quote: "Plain cheese followed at 26.6%, with Supreme/Deluxe capturing nearly 11% share."
  - p11 Supreme/Deluxe share of frozen pizza items sold on Instacart platform, 2025 = **11** % of frozen pizza items sold (2025-01-01..2025-12-31) [DISCARD: Supreme/Deluxe share of frozen pizza items — flavor mix, irrelevant to total mass.] quote: "with Supreme/Deluxe capturing nearly 11% share"
  - p12 White pizza share of frozen pizza items sold on Instacart platform, 2025 = **0.4** % of frozen pizza items sold (2025-01-01..2025-12-31) [DISCARD: White pizza share of frozen pizza items — flavor mix, irrelevant to total mass.] quote: "White pizza accounts for just 0.4% of frozen pizza items sold."
  - p13 Wisconsin frozen pizza ounces purchased per customer vs national average, 2025 ( = **113** % more ounces per customer than national average (2025-01-01..2025-12-31) [DISCARD: Wisconsin frozen-pizza ounces vs national — regional analogue for a state not in scope; no Chicago/Illinois figure and n] quote: "Wisconsin customers purchased 113% more frozen pizza per customer than the national average, based on total ounces ordered per customer."
  - p14 North Dakota frozen pizza ounces purchased per customer vs national average, 202 = **82** % more ounces per customer than national average (2025-01-01..2025-12-31) [DISCARD: North Dakota frozen-pizza regional analogue — out of scope, no transferable Chicago factor.] quote: "North Dakota followed at +82%, with Minnesota (+63%), Iowa (+62%), and Missouri (+60%) rounding out the top five."
  - p15 Minnesota frozen pizza ounces purchased per customer vs national average, 2025 = **63** % more ounces per customer than national average (2025-01-01..2025-12-31) [DISCARD: Minnesota frozen-pizza regional analogue — out of scope.] quote: "North Dakota followed at +82%, with Minnesota (+63%), Iowa (+62%), and Missouri (+60%) rounding out the top five."
  - p16 Iowa frozen pizza ounces purchased per customer vs national average, 2025 = **62** % more ounces per customer than national average (2025-01-01..2025-12-31) [DISCARD: Iowa frozen-pizza regional analogue — out of scope.] quote: "North Dakota followed at +82%, with Minnesota (+63%), Iowa (+62%), and Missouri (+60%) rounding out the top five."
  - p17 Missouri frozen pizza ounces purchased per customer vs national average, 2025 = **60** % more ounces per customer than national average (2025-01-01..2025-12-31) [DISCARD: Missouri frozen-pizza regional analogue — out of scope.] quote: "North Dakota followed at +82%, with Minnesota (+63%), Iowa (+62%), and Missouri (+60%) rounding out the top five."
  - p18 Ranch dressing order frequency lift when frozen pizza in cart, 2025 = **156** % more often than average (2025-01-01..2025-12-31) [DISCARD: Ranch dressing order lift — basket-affinity trivia, irrelevant to pizza mass.] quote: "Ranch dressing appears in orders 156% more often than average when frozen pizza is in the cart"
  - p19 Neapolitan-style crust year-over-year order share change, 2025 vs 2024 = **303** % YoY increase in order share (2024-01-01..2025-12-31) [DISCARD: Neapolitan crust order-share growth — style trend, irrelevant to total mass.] quote: "Neapolitan-style crust saw a staggering +303% year-over-year increase in order share"
  - p20 Detroit-style crust year-over-year order share change, 2025 vs 2024 = **38** % YoY increase in order share (2024-01-01..2025-12-31) [DISCARD: Detroit-style crust growth — style trend, irrelevant to total mass.] quote: "Detroit-style - the thick, crispy-edged square pie - grew +38% YoY"
  - p21 Cauliflower crust sales change, 2025 vs 2024 = **14** % decline in sales (2024-01-01..2025-12-31) [DISCARD: Cauliflower crust sales decline — style trend, irrelevant to total mass.] quote: "cauliflower crust sales fell 14% compared to 2024"
  - p22 Oregon Hawaiian pizza order frequency vs national average, 2025 = **384** % more often than national average (2025-01-01..2025-12-31) [DISCARD: Oregon Hawaiian pizza order frequency — regional topping preference, irrelevant to mass.] quote: "Oregon leads the country in Hawaiian pizza purchases, ordering it 384% more often than the national average."
  - p23 Hawaii Hawaiian pizza order frequency vs national average, 2025 = **49** % less than national average (2025-01-01..2025-12-31) [DISCARD: Hawaii Hawaiian pizza order frequency — regional topping preference, irrelevant to mass.] quote: "Hawaii itself orders Hawaiian pizza 49% less than the national average"
- dropped by code checks: 14 (value_as_written not in quote as a whole number: 6; number: more than one number in value_as_written: 1; period_end missing or unparseable: 7)

### d2 [related_series] Food-service sales analyst

Hypothesis: Chicago pizza restaurant sales (USD/year) divided by average price per pizza/tonne yields pizza mass sold through restaurants; limited-service and full-service pizza outlets plus non-pizza restaurants that sell pizza must be summed.

Queries issued by the searcher: Chicago pizza market size revenue; pizza restaurant sales Chicago statistics annual revenue; Census County Business Patterns Chicago city NAICS 722513 limited-service restaurants sales receipts; average price large pizza Chicago 2025

- `https://www.restaurantbusinessonline.com/top-100-independents-2025/quartino-ristorante` -> **live_dated** (page date 2025-12-05); points raw/verified 4/0
- `https://learn.regaliscapital.com/buy-a-pizza-shop-in-chicago-illinois/` -> **live_dated** (page date 2026-03-19); points raw/verified 15/0
- `https://www.ifmaworld.com/images/PDF/Gated/2025/Datassential/Datassential_500_2025_IFMA.pdf` -> **live_dated** (page date 2025-08-05); points raw/verified 15/13
  - p24 LSR Pizza segment 2024 Q4 U.S. units = **30,346** units (2024-10-01..2024-12-31) [keep: ] quote: "30,346 units 30,154 units"
  - p25 LSR Pizza segment 2024 Q4 average AUV = **1,010,000** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$32.94 billion $1.01 million"
  - p26 FSR Italian/Pizza segment 2024 Q4 average AUV = **2,810,000** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$8.92 billion $2.81 million"
  - p27 Domino's Pizza 2024 U.S. systemwide sales = **9,500,100,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "Domino's Pizza 6,854 7,014 7,132 +2.3% +1.7% $9,026,100,000 $9,500,100,000 +5.3% $1,366,135"
  - p28 Pizza Hut 2024 U.S. systemwide sales = **5,291,540,808** USD (2024-01-01..2024-12-31) [keep: ] quote: "Pizza Hut 6,568 6,518 6,404 -0.8% -1.7% $5,375,104,200 $5,291,540,808 -1.6% $815,579"
  - p29 Little Caesars 2024 U.S. systemwide sales = **4,931,748,900** USD (2024-01-01..2024-12-31) [keep: ] quote: "Little Caesars 4,179 4,249 4,183 +1.7% -1.6% $4,425,507,288 $4,931,748,900 +11.4% $1,170,000"
  - p30 Papa Johns 2024 U.S. systemwide sales = **3,701,902,511** USD (2024-01-01..2024-12-31) [keep: ] quote: "Papa Johns 3,220 3,291 3,177 +2.2% -3.5% $3,864,198,863 $3,701,902,511 -4.2% $1,157,331"
  - p31 Domino's Pizza 2024 average AUV = **1,366,135** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$9,026,100,000 $9,500,100,000 +5.3% $1,366,135"
  - p32 Pizza Hut 2024 average AUV = **815,579** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$5,375,104,200 $5,291,540,808 -1.6% $815,579"
  - p33 Little Caesars 2024 average AUV = **1,170,000** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$4,425,507,288 $4,931,748,900 +11.4% $1,170,000"
  - p34 Papa Johns 2024 average AUV = **1,157,331** USD per unit per year (2024-01-01..2024-12-31) [keep: ] quote: "$3,864,198,863 $3,701,902,511 -4.2% $1,157,331"
  - p35 Food-away-from-home inflation rate 2024 (U.S.) = **4.1** % (2024-01-01..2024-12-31) [keep: ] quote: "Food-away-from-home inflation reached 4.1% 2024"
  - p36 Top 500 chains 2024 U.S. systemwide sales total = **435,380,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "$435.38 billion +4.7% since 2023"
- `https://chicagochinesetimes.com/2025/07/09/%e3%80%90%e9%a2%a8%e5%9f%8e%e5%bf%ab%e5%a0%b1%e3%80%91%e6%a3%92-%e8%8a%9d%e5%8a%a0%e5%93%a52%e5%ae%b6%e7%9f` -> **dropped** (live http 404); points raw/verified -/-
- dropped by code checks: 21 (period_end missing or unparseable: 11; scale word 'thousand' not supported by quote or table header: 8; scale word 'billion' not supported by quote or table header: 2)

### d3 [physical_flow] Pizza operator / supply-chain analyst

Hypothesis: Number of pizza transactions per day in Chicago times average pizza mass per transaction gives mass sold; transactions can be built from outlet count × orders per outlet per day.

Queries issued by the searcher: number of pizzerias in Chicago; Chicago pizza restaurants number 2024; average pizza orders per day per restaurant; average weight of Chicago deep dish pizza grams

- `https://rentechdigital.com/smartscraper/it/business-report-details/united-states/illinois/list-of-pizza-restaurants-in-chicago` -> **live_dated** (page date 2026-04-01); points raw/verified 15/15
  - p37 Count of pizza restaurants in Chicago (point-in-time, April 1 2026) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Ci sono 1987 Pizza restaurants in Chicago al April 1, 2026"
  - p38 Count of pizza restaurants in Chicago (total, restated) = **1,987** pizza restaurants (2026-04-01..2026-04-01) [DISCARD: Restatement of p37 (same 1,987 count).] quote: "Ci sono un totale di 1987 Ristoranti di pizza in Chicago al April 01, 2026."
  - p39 Pizza restaurants in Chicago that are single-owner operations = **914** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p40 Share of Chicago pizza restaurants that are single-owner operations = **46** % (2026-04-01..2026-04-01) [keep: ] quote: "914 Pizza restaurants, che rappresentano il 46.00% di tutte le Pizza restaurants in Chicago, sono operazioni a proprietario unico"
  - p41 Pizza restaurants in Chicago that are part of larger brands = **1,073** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p42 Share of Chicago pizza restaurants that are part of larger brands = **54** % (2026-04-01..2026-04-01) [keep: ] quote: "mentre le restanti 1073, ovvero 54.00%, fanno parte di marchi più grandi"
  - p43 Average age of pizza restaurants in Chicago = **10** years (plus 2 months) (2026-04-01..2026-04-01) [DISCARD: Average age of Chicago pizza restaurants — descriptive, not a mass driver.] quote: "Average age of Pizza restaurants in Chicago is10 anni e 2 mesi."
  - p44 Pizza restaurants in Chicago with own website = **1,848** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web e i restanti 139 non hanno un proprio sito web."
  - p45 Pizza restaurants in Chicago without own website = **139** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "Circa 1848 Ristoranti di pizza hanno il proprio sito web e i restanti 139 non hanno un proprio sito web."
  - p46 Pizza restaurants in Chicago with Facebook pages = **1,048** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "1048 hanno pagine Facebook"
  - p47 Pizza restaurants in Chicago with Instagram accounts = **848** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "848 sono attivi su Instagram"
  - p48 Pizza restaurants in Chicago with LinkedIn profiles = **88** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "88 hanno profili LinkedIn"
  - p49 Pizza restaurants in Chicago with X accounts = **635** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "635 hanno account su X (precedentemente Twitter)"
  - p50 Pizza restaurants in Chicago with TikTok profiles = **189** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "189 sono su TikTok"
  - p51 Pizza restaurants in Chicago with YouTube channels = **151** pizza restaurants (2026-04-01..2026-04-01) [keep: ] quote: "151 have YouTube channels"
- `https://foodeist.com/index.php/pizza-statistics` -> **live_dated** (page date 2026-03-10); points raw/verified 15/0
- `https://github.com/bernie236/Pizza-Sales/blob/main/README.md` -> **live_dated** (page date 2023-09-19); points raw/verified 10/0
- `https://www.timeout.com/chicago/restaurants/best-pizza-in-chicago` -> **live_dated** (page date 2026-04-20); points raw/verified 0/0
- dropped by code checks: 25 (period_end missing or unparseable: 25)

### d4 [capacity_consumption] Household consumption analyst

Hypothesis: At-home pizza consumption = Chicago households × share eating pizza on a given day × average mass per eating occasion; complements restaurant route to cover the full total.

Queries issued by the searcher: percentage of Americans eat pizza on a given day NHANES; Chicago households average size 2025 Census; NHANES pizza consumers mean grams of pizza per eating occasion; "pizza" "per eating occasion" grams average intake adults NHANES 2017-2020

- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/62_Pizza_Consumption_of_US_population_1720.pdf` -> **live_dated** (page date 2024-12-20); points raw/verified 15/11
  - p52 Share of US population (2+ years) consuming pizza on any given day, NHANES day 1 = **11** percent of population (2017-01-01..2020-03-31) [DISCARD: Exact duplicate of p1 (same 11% statistic, same source); adds no information.] quote: "On any given day, pizza was consumed by 11% of the population overall (data not shown)."
  - p53 Share of US older adults (60+) consuming pizza on any given day = **6** percent of population (2017-01-01..2020-03-31) [DISCARD: Duplicate of p2 (6% older-adult prevalence, same source).] quote: "the percentage consuming decreased to about 6% among older adults (60+)."
  - p54 Share of US children/adolescents consuming pizza on any given day (Figure 2a) = **14** percent of population (2017-01-01..2020-03-31) [keep: ] quote: "14 10 16 8 16 9 15 7 Percentage Non-Hispanic White"
  - p55 Share of US adults consuming pizza on any given day (Figure 2a) = **10** percent of population (2017-01-01..2020-03-31) [keep: ] quote: "14 10 16 8 16 9 15 7 Percentage Non-Hispanic White"
  - p56 Share of pizza consumed obtained from restaurants (US) = **56** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p57 Share of pizza consumed obtained from school/daycare (US) = **12** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "56 26 12 6 Restaurant Grocery store School/Daycare Other"
  - p58 Share of pizza consumed obtained from 'Other' sources (US) = **6** percent of pizza consumed (2017-01-01..2020-03-31) [keep: ] quote: "A small percentage (6%) of pizza consumed was obtained from "Other" sources"
  - p59 Share of pizza intake at dinner among adults 20+ (US) = **58** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "4 28 58 10"
  - p60 Share of pizza intake at lunch among adults 20+ (US) = **28** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "4 28 58 10"
  - p61 Share of pizza intake at lunch among children 2-19 (US) = **41** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
  - p62 Share of pizza intake at dinner among children 2-19 (US) = **48** percent of pizza intake (2017-01-01..2020-03-31) [keep: ] quote: "Among children and adolescents, 41% of pizza intake was at lunch and 48% was at dinner."
- `https://faseb.onlinelibrary.wiley.com/doi/10.1096/fasebj.30.1_supplement.lb407` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.census.gov/quickfacts/fact/table/US,chicagocityillinois,cookcountyillinois/PST045224` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/DBrief/11_consumption_of_pizza_0710.pdf` -> **live_dated** (page date 2014-02-05); points raw/verified 15/13
  - p63 Share of US population aged 2+ consuming pizza on any given day (NHANES 1-day re = **13** percent (2007-01-01..2010-12-31) [keep: ] quote: "Overall, 13% of the U.S. population aged 2 years and over, consumed pizza on any given day"
  - p64 Share of US children (2-19 years) consuming pizza on any given day = **20** percent (2007-01-01..2010-12-31) [keep: ] quote: "Overall, a higher percentage of children (2-19 years) consumed pizza than adults (20 years and over): 20% vs. 11%, respectively."
  - p65 Share of US adults (20 years and over) consuming pizza on any given day = **11** percent (2007-01-01..2010-12-31) [keep: ] quote: "Overall, a higher percentage of children (2-19 years) consumed pizza than adults (20 years and over): 20% vs. 11%, respectively."
  - p66 Share of US males consuming pizza on any given day = **15** percent (2007-01-01..2010-12-31) [keep: ] quote: "For all individuals, a higher percentage of males (15%) than females (11%) consumed pizza on any given day."
  - p67 Share of US females consuming pizza on any given day = **11** percent (2007-01-01..2010-12-31) [keep: ] quote: "For all individuals, a higher percentage of males (15%) than females (11%) consumed pizza on any given day."
  - p68 Share of US older adults (60 years and over) consuming pizza on any given day = **6** percent (2007-01-01..2010-12-31) [keep: ] quote: "22% among older children (6-11 years) and adolescents (12-19 years) to less than 6% among older adults, 60 years and over (Figure 1)."
  - p69 Share of US children (6-11 years) consuming pizza on any given day = **22** percent (2007-01-01..2010-12-31) [keep: ] quote: "22% among older children (6-11 years) and adolescents (12-19 years) to less than 6% among older adults, 60 years and over (Figure 1)."
  - p70 Share of pizza consumption occurring in the home (all individuals) = **59** percent (2007-01-01..2010-12-31) [keep: ] quote: "More than half (59%) of pizza consumption occurred in the home."
  - p71 Share of pizza consumption occurring at home among adults (20 years and over) = **65** percent (2007-01-01..2010-12-31) [keep: ] quote: "More adults (65%) than children (49%) consumed pizza at home (data not shown)."
  - p72 Share of pizza consumption occurring at home among children (2-19 years) = **49** percent (2007-01-01..2010-12-31) [keep: ] quote: "More adults (65%) than children (49%) consumed pizza at home (data not shown)."
  - p73 Mean energy obtained from pizza among US child consumers (2-19 years) on day con = **538** kilocalories (2007-01-01..2010-12-31) [keep: ] quote: "the mean energy intake obtained from pizza was 538 kilocalories for children and 744 kilocalories for adults (data not shown)."
  - p74 Mean energy obtained from pizza among US adult consumers (20 years and over) on  = **744** kilocalories (2007-01-01..2010-12-31) [keep: ] quote: "the mean energy intake obtained from pizza was 538 kilocalories for children and 744 kilocalories for adults (data not shown)."
  - p75 Share of pizza consumption occurring at snack occasion (all individuals) = **10** percent (2007-01-01..2010-12-31) [keep: ] quote: "Overall, almost 10% of pizza consumption occurred at a snack occasion (Figure 5)."
- dropped by code checks: 6 (value_as_written not in quote as a whole number: 3; number: more than one number in value_as_written: 1; period_end missing or unparseable: 2)

### d5 [related_series] National pizza-chain and frozen-pizza market analyst

Hypothesis: US total pizza sales (restaurant + frozen retail) divided by US population gives a national per-capita mass benchmark; scaling to Chicago and adjusting for local pizza culture constrains routes d1 and d2.

Queries issued by the searcher: US pizza industry annual sales pounds American Pizza Community statistics; frozen pizza retail volume US 2025 Circana pounds sales; US pizza restaurant sales billion 2025 Technomic pizza category foodservice; average pizza weight ounces 14-inch pizza pounds dough weight per pizza

- `https://frb.mydigitalpublication.com/articles/turning-up-the-heat-on-frozen-pizza` -> **dropped** (live http 202); points raw/verified -/-
- `https://greenwichgp.com/wp-content/uploads/2026/09/GCG-US-Frozen-Pizza-Industry-2026-Update.pdf.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/6
  - p76 U.S. frozen pizza retail dollar sales, 52 weeks ending April 19, 2026 (Circana) = **7,300,000,000** USD (2025-04-20..2026-04-19) [keep: ] quote: "U.S. frozen pizza generated about $7.3 billion in the 52 weeks ending April 19, 2026, down 1.9% year over year"
  - p77 U.S. frozen pizza market size 2025, IMARC estimate = **7,200,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "IMARC puts the U.S. market at ~$7.2 billion in 2025 rising to ~$11.0 billion by 2034, a 4.64% CAGR"
  - p78 Global frozen pizza market size 2024, Grand View Research = **22,700,000,000** USD (2024-01-01..2024-12-31) [keep: ] quote: "Grand View Research now pegs the global frozen pizza market at about $22.7 billion in 2024"
  - p79 Total U.S. frozen food department sales, 52 weeks ending Sept. 21, 2025 (Circana = **93,500,000,000** USD (2024-09-22..2025-09-21) [keep: ] quote: "The broader U.S. frozen food department is roughly $93.5 billion"
  - p80 Weekly pizza consumption rate in 2025 (Technomic) = **35** percent (2025-01-01..2025-12-31) [keep: ] quote: "35% Weekly pizza consumption in 2025, up from 24% in 2022"
  - p81 Private label frozen pizza sales, 52 weeks ending April 19, 2026 (Circana) = **1,100,000,000** USD (2025-04-20..2026-04-19) [keep: ] quote: "Private label frozen pizza is a roughly $1.1 billion business"
- `https://www.seattletimes.com/nation-world/people-are-ordering-smaller-pizzas-fewer-toppings-what-does-it-mean/` -> **live_dated** (page date 2025-12-01); points raw/verified 15/0
- `http://www.americanpizzacommunity.com/assets/files/America-Eats-Pizza.pdf` -> **dropped** (live http 404); points raw/verified -/-
- dropped by code checks: 24 (scale word 'billion' not supported by quote or table header: 2; value_as_written not in quote as a whole number: 2; period_end 2034-12-31 after as_of: 2; period_end 2030-12-31 after as_of: 1; period_end missing or unparseable: 14; period year 2024 does not appear in the page text or URL (likely mis-dated): 1; number: no number in value_as_written: 2)

### d6 [base_rates] Demographic denominator analyst

Hypothesis: Chicago population (residents, and separately daytime/visitor population) is the multiplier for per-capita routes; boundary choice (city vs metro) changes the answer by roughly a factor of 3, so pinning the denominator is essential.

Queries issued by the searcher: Chicago population estimate 2025 Census; Chicago metro area population 2025 Census estimate; Chicago daytime population commuters Census estimate city of Chicago; Chicago visitors 2025 annual overnight visitors Choose Chicago tourism

- `https://www.census.gov/quickfacts/fact/table/cookcountyillinois,chicagocityillinois,IL/PST045224` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.chicagotribune.com/2026/05/14/census-2025-population-estimates/` -> **live_dated** (page date 2026-05-14); points raw/verified 10/9
  - p82 Chicago city population estimate, 2025 (Census) = **2,750,000** people (2025-01-01..2025-12-31) [keep: ] quote: "Almost 2.75 million people called Chicago home in 2025, according to the latest census numbers."
  - p83 Chicago city population change since April 1, 2020 (decrease) = **16,748** residents (2020-04-01..2025-12-31) [keep: ] quote: "That's a decrease of 16,748 residents since April 1, 2020, but an increase of 5,253 people since 2024."
  - p84 Chicago city population change since 2024 (increase) = **5,253** people (2024-01-01..2025-12-31) [keep: ] quote: "That's a decrease of 16,748 residents since April 1, 2020, but an increase of 5,253 people since 2024."
  - p85 Houston population gain, 2025 = **97,000** residents (2025-01-01..2025-12-31) [DISCARD: Houston population gain — unrelated city, no role.] quote: "Houston, which gained more than 97,000 residents, was ranked fourth."
  - p86 Cook County population loss since 2020 = **84,385** people (2020-01-01..2025-12-31) [DISCARD: Cook County population loss since 2020 — county-level context; the city figure (p82) is the denominator. Redundant with ] quote: "Since 2020, Cook County as a whole has lost 84,385 people, or 1.6% of its population, which was almost 5.2 million in 2025."
  - p87 Cook County population loss since 2020 as share of population = **1.6** % (2020-01-01..2025-12-31) [DISCARD: Cook County loss as share — redundant context, not used.] quote: "Since 2020, Cook County as a whole has lost 84,385 people, or 1.6% of its population, which was almost 5.2 million in 2025."
  - p88 Cook County population estimate, 2025 = **5,200,000** people (2025-01-01..2025-12-31) [keep: ] quote: "Since 2020, Cook County as a whole has lost 84,385 people, or 1.6% of its population, which was almost 5.2 million in 2025."
  - p89 Kendall County population increase since 2020 = **13,500** people (2020-01-01..2025-12-31) [DISCARD: Kendall County population increase — out of scope.] quote: "Kendall County saw the largest increase in the state - more than 13,500 people have moved there since 2020, which is an 10.3% increase in population."
  - p90 Kendall County population increase since 2020 as share = **10.3** % (2020-01-01..2025-12-31) [DISCARD: Kendall County increase as share — out of scope.] quote: "Kendall County saw the largest increase in the state - more than 13,500 people have moved there since 2020, which is an 10.3% increase in population."
- `https://www.wikiwand.com/en/List_of_North_American_metropolitan_areas_by_population` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.washtimes.com/news/2023/jul/5/census-biggest-cities-lost-more-1m-day-residents-c/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 1 (number: no number in value_as_written: 1)

### d7 [own_history] Time-series analyst

Hypothesis: If any prior estimate of Chicago pizza consumption or Chicago pizza sales exists, its level and growth trend can anchor the 2026 figure; absent a direct series, Chicago restaurant-sales history can proxy the trend.

Queries issued by the searcher: Chicago pizza consumption per year estimate tons; how much pizza does Chicago eat per day estimate; Chicago pizza market size industry sales dollars; Chicago restaurant sales 2024 2025 Illinois Restaurant Association annual sales

- `https://chicagochinesetimes.com/2025/07/09/%e3%80%90%e9%a2%a8%e5%9f%8e%e5%bf%ab%e5%a0%b1%e3%80%91%e6%a3%92-%e8%8a%9d%e5%8a%a0%e5%93%a52%e5%ae%b6%e7%9f` -> **live_dated** (page date 2025-07-09); points raw/verified 15/13
  - p91 Pizza chain sales growth rate, 2024 (Technomic annual report) = **0.5** % (2024-01-01..2024-12-31) [keep: ] quote: "2024 年披薩連鎖店的銷售額僅成長了 0.5%"
  - p92 Overall chain restaurant sales growth rate, 2024 (comparison to pizza chains) = **3** % (2024-01-01..2024-12-31) [keep: ] quote: "遠低於整體連鎖餐廳 3% 的銷售成長率"
  - p93 Giordano's restaurants nationwide, end of 2024 = **60** restaurants (2024-12-31..2024-12-31) [keep: ] quote: "截至 2024 年底,Giordano's 在全國範圍內經營著 60 家餐廳"
  - p94 Giordano's restaurants nationwide, 2022 = **65** restaurants (2022-01-01..2022-12-31) [keep: ] quote: "相比 2022 年的 65 家有所減少"
  - p95 Lou Malnati's locations, end of 2024 = **80** locations (2024-12-31..2024-12-31) [keep: ] quote: "Lou Malnati's 則擁有 80 家分店"
  - p96 Lou Malnati's locations, 2022 = **74** locations (2022-01-01..2022-12-31) [keep: ] quote: "高於 2022 年的 74 家"
  - p97 Giordano's Florida locations, end of 2024 = **3** restaurants (2024-12-31..2024-12-31) [DISCARD: Giordano's Florida locations — chain footprint detail, not a mass driver.] quote: "包括佛羅里達州(3 家)"
  - p98 Giordano's Indiana locations, end of 2024 = **4** restaurants (2024-12-31..2024-12-31) [DISCARD: Giordano's Indiana locations — chain footprint detail.] quote: "印第安納州(4 家)"
  - p99 Giordano's Nevada locations, end of 2024 = **2** restaurants (2024-12-31..2024-12-31) [DISCARD: Giordano's Nevada locations — chain footprint detail.] quote: "內華達州(2 家)"
  - p100 Giordano's Ohio locations, end of 2024 = **2** restaurants (2024-12-31..2024-12-31) [DISCARD: Giordano's Ohio locations — chain footprint detail.] quote: "俄亥俄州(2 家)"
  - p101 Lou Malnati's Arizona locations, end of 2024 = **9** locations (2024-12-31..2024-12-31) [DISCARD: Lou Malnati's Arizona locations — chain footprint detail.] quote: "其中亞利桑那州截至 2024 年底有 9 家分店"
  - p102 Victory Park Capital acquisition price of Giordano's majority assets, 2011 = **52,000,000** USD (2011-01-01..2011-12-31) [DISCARD: 2011 Giordano's acquisition price — stale valuation, no mass relevance.] quote: "2011 年,Victory Park Capital 以 5200 萬美元收購了 Giordano's 的大部分資產"
  - p103 Lou Malnati's valuation from Meritage Group stake purchase, 2011 = **500,000,000** USD (2011-01-01..2011-12-31) [DISCARD: 2011 Lou Malnati's valuation — stale valuation, no mass relevance.] quote: "該交易使 Lou Malnati's 的估值達到 5 億美元"
- `https://gripsintelligence.com/insights/industries/food-beverages-tobacco/chicago-food-specialties` -> **live_dated** (page date 2022-01-01); points raw/verified 12/2
  - p104 Average order value (lower bound) for Chicago Food Specialties online industry,  = **100** USD (2026-08-01..2026-08-31) [DISCARD: Grips AOV $100-200 for 'Chicago Food Specialties' online — ambiguous scope, stale-dated page, cannot be tied to pizza ma] quote: "$100-200 AOVAug 26"
  - p105 Average order value (upper bound) for Chicago Food Specialties online industry,  = **200** USD (2026-08-01..2026-08-31) [DISCARD: Upper bound of the same Grips AOV — same problem as p104.] quote: "$100-200 AOVAug 26"
- `https://marketintelo.com/report/chicago-deep-dish-pizza-restaurant-market` -> **live_dated** (page date 2026-06-11); points raw/verified 15/9
  - p106 Global Chicago deep-dish pizza restaurant market size, 2025 (base year) = **900,000,000** USD (2025-01-01..2025-12-31) [keep: ] quote: "The Chicago Deep-Dish Pizza Restaurant market is valued at $0.9 billion in 2025 and is projected to reach $1.2 billion by 2034"
  - p107 Illinois and Chicago area share of North American Chicago deep-dish pizza market = **65** percent of North American market revenue (2025-01-01..2025-12-31) [keep: ] quote: "Illinois and the Chicago area alone accounting for approximately 65.0% of total market revenue"
  - p108 Dine-In share of Chicago deep-dish pizza market revenue, 2025 = **38.5** percent of market revenue (2025-01-01..2025-12-31) [keep: ] quote: "The Dine-In segment represents the largest consumption occasion within the Chicago Deep-Dish Pizza Restaurant market, accounting for 38.5% of total market revenue in 2025"
  - p109 Takeout share of Chicago deep-dish pizza market revenue, 2025 = **28.3** percent of market revenue (2025-01-01..2025-12-31) [keep: ] quote: "The Takeout segment represents the second-largest consumption occasion within the market, accounting for 28.3% of total market revenue in 2025"
  - p110 Delivery share of Chicago deep-dish pizza market revenue, 2025 = **22** percent of market revenue (2025-01-01..2025-12-31) [keep: ] quote: "The Delivery segment represents the fastest-growing consumption occasion within the Chicago Deep-Dish Pizza Restaurant market, accounting for 22.0% of total market revenue in 2025"
  - p111 Catering share of Chicago deep-dish pizza market revenue, 2025 = **11.2** percent of market revenue (2025-01-01..2025-12-31) [keep: ] quote: "The Catering segment represents an emerging growth opportunity within the Chicago Deep-Dish Pizza Restaurant market, accounting for 11.2% of total market revenue in 2025"
  - p112 Chicago visitors in 2024 (overnight and same-day) = **58,300,000** visitors (2024-01-01..2024-12-31) [keep: ] quote: "Chicago tourism statistics indicating that the city attracted approximately 58.3 million overnight and same-day visitors in 2024"
  - p113 Share of Chicago visitors actively seeking deep-dish pizza, lower bound = **35** percent of visitors (2024-01-01..2024-12-31) [keep: ] quote: "with an estimated 35-45% of visitors actively seeking deep-dish pizza experiences during their stay"
  - p114 Share of Chicago visitors actively seeking deep-dish pizza, upper bound = **45** percent of visitors (2024-01-01..2024-12-31) [keep: ] quote: "with an estimated 35-45% of visitors actively seeking deep-dish pizza experiences during their stay"
- `https://researchintelo.com/report/frozen-chicago-deep-dish-pizza-market` -> **live_dated** (page date 2025-10-01); points raw/verified 10/6
  - p115 Global Frozen Chicago Deep Dish Pizza market size, 2024 (base year) = **1,200,000,000** USD (2024-01-01..2024-12-31) [DISCARD: Global frozen Chicago deep-dish market — global scope, no Chicago-city mass bridge.] quote: "the Global Frozen Chicago Deep Dish Pizza market size was valued at $1.2 billion in 2024"
  - p116 North America share of global Frozen Chicago Deep Dish Pizza revenue, 2024 = **55** percent of total revenue (2024-01-01..2024-12-31) [DISCARD: North America share of frozen deep-dish — global-scope share, no usable bridge.] quote: "accounting for approximately 55% of total revenue in 2024"
  - p117 Report base year = **2,024** year (2024-01-01..2024-12-31) [DISCARD: Report base year metadata — not a quantity.] quote: "\| Base Year \| 2024 \|"
  - p118 Report historic data period start = **2,018** year (2018-01-01..2018-12-31) [DISCARD: Report historic period start — metadata.] quote: "\| Historic Data \| 2018-2023 \|"
  - p119 Report historic data period end = **2,023** year (2023-01-01..2023-12-31) [DISCARD: Report historic period end — metadata.] quote: "\| Historic Data \| 2018-2023 \|"
  - p120 Report forecast period start = **2,025** year (2025-01-01..2025-12-31) [DISCARD: Report forecast period start — metadata.] quote: "\| Forecast Period \| 2025-2033 \|"
- dropped by code checks: 22 (period_end missing or unparseable: 10; number: no number in value_as_written: 1; scale word 'million' not supported by quote or table header: 2; number: more than one number in value_as_written: 3; scale word 'thousand' not supported by quote or table header: 1; scale word 'billion' not supported by quote or table header: 1; period_end 2034-12-31 after as_of: 1; period_end 2033-12-31 after as_of: 3)

### d8 [shocks] Calendar and price-effect analyst

Hypothesis: Day-of-week, seasonality, holidays, and 2025-2026 price inflation shift daily pizza mass; an average-day figure should reflect the annual mean, but large events (e.g., major sports wins, festivals) and price-driven substitution could bias a single-day snapshot.

Queries issued by the searcher: pizza sales by day of week index Friday peak percentage; Super Bowl pizza sales increase percent day; BLS CPI pizza price inflation 2025 2026 frozen pizza restaurant price index; Americans eat pizza per day number of slices per capita pizza consumption statistics 2025

- `https://slice.com/blog/top-pizza-ordering-days/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.chicagotribune.com/2026/02/06/elgin-super-bowl-bars-restaurants-pizza/` -> **live_dated** (page date 2026-02-06); points raw/verified 10/0
- `https://slice.com/blog/februarys-big-ordering-days/` -> **dropped** (live http 403); points raw/verified -/-
- `https://thatpizzakitchen.com/august-cpi-food-prices-pizza/` -> **live_dated** (page date 2026-09-11); points raw/verified 15/9
  - p121 US CPI food at home, 12-month change (August 2026) = **2.2** percent (2025-08-01..2026-08-31) [keep: ] quote: "Food at home was unchanged for the month and up 2.2 percent over the year."
  - p122 US CPI food away from home, 12-month change (August 2026) = **3.4** percent (2025-08-01..2026-08-31) [keep: ] quote: "Food away from home rose 0.3 percent for the month and 3.4 percent over the year."
  - p123 US CPI limited-service meals (carryout/delivery pizza), 12-month change (August  = **3.2** percent (2025-08-01..2026-08-31) [keep: ] quote: "Limited-service meals, the category that holds carryout and delivery pizza, ran 3.2 percent higher."
  - p124 US CPI dairy and related products, 12-month change (August 2026) = **0.3** percent (2025-08-01..2026-08-31) [keep: ] quote: "Dairy and related products fell 0.3 percent over twelve months, the only one of the six grocery groups below zero."
  - p125 US CPI cereals and bakery products (flour side), 12-month change (August 2026) = **2.6** percent (2025-08-01..2026-08-31) [keep: ] quote: "Cereals and bakery products rose 2.6 percent over the year, though they were flat in August."
  - p126 US CPI fruits and vegetables (sauce side), 12-month change (August 2026) = **3.2** percent (2025-08-01..2026-08-31) [keep: ] quote: "Fruits and vegetables rose 3.2 percent for the year"
  - p127 National Restaurant Association menu prices, year-over-year through July = **3.4** percent (..2026-07-31) [keep: ] quote: "had menu prices up 3.4 percent year over year through July against 2.7 percent for groceries"
  - p128 National Restaurant Association grocery prices, year-over-year through July = **2.7** percent (..2026-07-31) [keep: ] quote: "had menu prices up 3.4 percent year over year through July against 2.7 percent for groceries"
  - p129 CME 40-pound cheddar blocks price, September 4 = **1.465** US dollars per pound (2026-09-04..2026-09-04) [DISCARD: CME cheddar block price — input-cost detail; not needed for mass and not a clean deflator for pizza price.] quote: "USDA's Dairy Market News put 40-pound blocks at $1.4650 and barrels at $1.5325 on September 4."
- dropped by code checks: 16 (period_end missing or unparseable: 10; number: more than one number in value_as_written: 1; number: no number in value_as_written: 1; period_end 2026-12-31 after as_of: 3; period_end 2027-12-31 after as_of: 1)

### b1 [related_series] Mass per pizza slice/pie

Hypothesis: The per-capita route (d1/d4) converts prevalence and energy intake into mass only via an assumed pizza energy density (kcal per gram of pizza as served). A sourced value for average pizza energy density (e.g., USDA FoodData Central values for thin-crust, deep-dish, and frozen pizza, weighted by style mix) would replace the largest single assumption in m1 and tighten the central estimate materially.

Queries issued by the searcher: USDA FoodData Central pizza 14-inch regular crust calories per 100g; deep dish pizza calories per 100 grams nutrition; "pizza, cheese, regular crust, frozen" USDA 100 g energy kcal FoodData Central 21256; frozen pizza average kcal per 100g label data survey nutrition

- `https://fdc.nal.usda.gov/food-details/173292/nutrients` -> **dropped** (live http 404); points raw/verified -/-
- `https://tools.myfooddata.com/print/2641987/100g/1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://tools.myfooddata.com/print/172055/100g/1` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.medindia.net/nutrition-data/pizza-cheese-topping-regular-crust-frozen-cooked.htm` -> **live_dated** (page date 1997-01-01); points raw/verified 8/0
- dropped by code checks: 8 (period_end missing or unparseable: 8)

### b2 [related_series] Chicago pizza sales dollars

Hypothesis: The sales-based route (d2) needs Chicago-specific pizza restaurant revenue to convert dollars to mass. A figure for Chicago pizza-restaurant annual sales (or Chicago share of US pizza sales) would let us use the national price-per-tonne implied by p25/p26 and the outlet count p37, replacing the assumption that Chicago per-capita pizza spend equals the national average.

Queries issued by the searcher: Chicago pizza restaurant industry annual sales revenue; Chicago pizza market size dollars per year; Cook County pizza restaurants annual sales Census County Business Patterns 722513; "Chicago" pizza sales per year billion "pizza" industry report

- `https://www.agmrc.org/media/cms/BizMiner_722513_D9673C22E5167.pdf` -> **live_dated** (page date 2018-09-24); points raw/verified 15/14
  - p130 US pizza restaurant industry market volume (all industry operations), 2017 = **67,584,047,264** USD (2017-01-01..2017-12-31) [keep: ] quote: "Industry 69,950,000,318 66,942,402,669 67,584,047,264 67,808,286,483"
  - p131 US pizza restaurant industry market volume (all industry operations), June-2018 = **67,808,286,483** USD (2018-01-01..2018-06-30) [DISCARD: Mid-2018 partial-year value in the AGMRC series; not a clean annual observation and redundant with p130.] quote: "Industry 69,950,000,318 66,942,402,669 67,584,047,264 67,808,286,483"
  - p132 US pizza restaurant industry market volume, 2015 = **69,950,000,318** USD (2015-01-01..2015-12-31) [keep: ] quote: "Industry 69,950,000,318 66,942,402,669 67,584,047,264 67,808,286,483"
  - p133 US pizza restaurant industry market volume, 2016 = **66,942,402,669** USD (2016-01-01..2016-12-31) [keep: ] quote: "Industry 69,950,000,318 66,942,402,669 67,584,047,264 67,808,286,483"
  - p134 US pizza restaurant industry sites (firms plus branches), 2017 = **75,156** industry sites (2017-01-01..2017-12-31) [keep: ] quote: "Industry Sites 83,935 76,514 75,156 74,231"
  - p135 US pizza restaurant industry sites, June-2018 = **74,231** industry sites (2018-01-01..2018-06-30) [DISCARD: Mid-2018 partial-year site count; redundant with p134.] quote: "Industry Sites 83,935 76,514 75,156 74,231"
  - p136 US pizza restaurant average annual sales per site, 2017 = **899,250** USD per site per year (2017-01-01..2017-12-31) [keep: ] quote: "Average Site 833,383 874,904 899,250 7.90 913,477"
  - p137 US pizza restaurant average annual sales per site, June-2018 = **913,477** USD per site per year (2018-01-01..2018-06-30) [DISCARD: Mid-2018 partial-year sales/site; redundant with p136.] quote: "Average Site 833,383 874,904 899,250 7.90 913,477"
  - p138 US pizza restaurant sales per person, 2017 = **212** USD per person per year (2017-01-01..2017-12-31) [keep: ] quote: "US Sales/ Person 223 211 212 213"
  - p139 US pizza restaurant sales per person, June-2018 = **213** USD per person per year (2018-01-01..2018-06-30) [DISCARD: Mid-2018 partial-year sales/person; redundant with p138.] quote: "US Sales/ Person 223 211 212 213"
  - p140 US pizza restaurant sales per household, 2017 = **504** USD per household per year (2017-01-01..2017-12-31) [keep: ] quote: "US Sales/ Household 527 502 504 506"
  - p141 US pizza restaurant sales per business site, 2017 = **4,499** USD per business site per year (2017-01-01..2017-12-31) [keep: ] quote: "US Sales/ Business Site 4,444 4,456 4,499 4,634"
  - p142 US pizza restaurant industry total employment, 2017 = **1,451,984** employees (2017-01-01..2017-12-31) [keep: ] quote: "Industry Total 1,564,387 1,473,561 1,451,984 1,436,099"
  - p143 US pizza restaurant sales per employee, 2017 = **46,546** USD per employee per year (2017-01-01..2017-12-31) [keep: ] quote: "US 44,714 45,429 46,546 47,217"
- `https://marketintelo.com/report/chicago-deep-dish-pizza-restaurant-market` -> **live_dated** (page date 2026-06-11); points raw/verified 15/7
  - p144 Global Chicago deep-dish pizza restaurant market size, 2025 (base year) = **900,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Duplicate of p106 (deep-dish market size).] quote: "The Chicago Deep-Dish Pizza Restaurant market is valued at $0.9 billion in 2025"
  - p145 Illinois and Chicago area share of total Chicago deep-dish market revenue, 2025 = **65** % of total market revenue (2025-01-01..2025-12-31) [DISCARD: Duplicate of p107 (65% Illinois/Chicago share).] quote: "Illinois and the Chicago area alone accounting for approximately 65.0% of total market revenue"
  - p146 North America share of global Chicago deep-dish market, 2025 = **100** % of global market (2025-01-01..2025-12-31) [DISCARD: Restates p106/p107 (100% North America share); redundant.] quote: "represents approximately $0.9 billion or 100% of the global Chicago Deep-Dish Pizza Restaurant market in 2025"
  - p147 Dine-In segment revenue, 2025 = **350,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Segment revenue restatement of p106 shares; redundant with p108.] quote: "accounting for 38.5% of total market revenue in 2025, generating approximately $0.35 billion in annual revenue"
  - p148 Takeout segment revenue, 2025 = **250,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Segment revenue restatement of p106 shares; redundant with p109.] quote: "accounting for 28.3% of total market revenue in 2025, generating approximately $0.25 billion in annual revenue"
  - p149 Delivery segment revenue, 2025 = **200,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Segment revenue restatement of p106 shares; redundant with p110.] quote: "accounting for 22.0% of total market revenue in 2025, generating approximately $0.20 billion in annual revenue"
  - p150 Catering segment revenue, 2025 = **100,000,000** USD (2025-01-01..2025-12-31) [DISCARD: Segment revenue restatement of p106 shares; redundant with p111.] quote: "accounting for 11.2% of total market revenue in 2025, generating approximately $0.10 billion in annual revenue"
- `https://www.ifmaworld.com/images/PDF/Gated/2025/Datassential/Datassential_500_2025_IFMA.pdf` -> **live_dated** (page date 2025-08-05); points raw/verified 15/12
  - p151 LSR Pizza segment 2024 Q4 U.S. units = **30,346** units (2024-10-01..2024-12-31) [DISCARD: Duplicate of p24 (LSR pizza units).] quote: "30,346 units 30,154 units"
  - p152 FSR Italian/Pizza segment 2024 Q4 U.S. units = **2,242** units (2024-10-01..2024-12-31) [keep: ] quote: "2,242 units 2,235 units"
  - p153 Domino's Pizza 2024 U.S. systemwide sales = **9,500,100,000** USD (2024-01-01..2024-12-31) [DISCARD: Duplicate of p27 (Domino's sales).] quote: "Domino's Pizza 6,854 7,014 7,132 +2.3% +1.7% $9,026,100,000 $9,500,100,000 +5.3% $1,366,135"
  - p154 Pizza Hut 2024 U.S. systemwide sales = **5,291,540,808** USD (2024-01-01..2024-12-31) [DISCARD: Duplicate of p28 (Pizza Hut sales).] quote: "Pizza Hut 6,568 6,518 6,404 -0.8% -1.7% $5,375,104,200 $5,291,540,808 -1.6% $815,579"
  - p155 Little Caesars 2024 U.S. systemwide sales = **4,931,748,900** USD (2024-01-01..2024-12-31) [DISCARD: Duplicate of p29 (Little Caesars sales).] quote: "Little Caesars 4,179 4,249 4,183 +1.7% -1.6% $4,425,507,288 $4,931,748,900 +11.4% $1,170,000"
  - p156 Papa Johns 2024 U.S. systemwide sales = **3,701,902,511** USD (2024-01-01..2024-12-31) [DISCARD: Duplicate of p30 (Papa Johns sales).] quote: "Papa Johns 3,220 3,291 3,177 +2.2% -3.5% $3,864,198,863 $3,701,902,511 -4.2% $1,157,331"
  - p157 LSR Pizza segment 2024 Q4 average AUV = **1,010,000** USD per unit (2024-01-01..2024-12-31) [DISCARD: Duplicate of p25 (LSR AUV).] quote: "$32.94 billion $1.01 million"
  - p158 FSR Italian/Pizza segment 2024 Q4 average AUV = **2,810,000** USD per unit (2024-01-01..2024-12-31) [DISCARD: Duplicate of p26 (FSR Italian/Pizza AUV).] quote: "$8.92 billion $2.81 million"
  - p159 Giordano's 2024 U.S. systemwide sales (Chicago-style deep dish chain) = **155,647,668** USD (2024-01-01..2024-12-31) [keep: ] quote: "Giordano's 62 60 59 -3.2% -1.7% $141,556,354 $155,647,668 +10.0% $2,594,128"
  - p160 Lou Malnati's Pizzeria 2024 U.S. systemwide sales (Chicago deep dish chain) = **106,930,479** USD (2024-01-01..2024-12-31) [keep: ] quote: "Lou Malnati's Pizzeria 81 79 78 -2.5% -1.3% $107,408,172 $106,930,479 -0.4% $1,353,550"
  - p161 Rosati's Chicago Pizza 2024 U.S. systemwide sales = **58,598,029** USD (2024-01-01..2024-12-31) [keep: ] quote: "Rosati's Chicago Pizza 63 63 71 +0.0% +12.7% $58,899,342 $58,598,029 -0.5% $945,130"
  - p162 Total 2024 U.S. sales of Datassential 500 chains = **435,380,000,000** USD (2024-01-01..2024-12-31) [DISCARD: Duplicate of p36 (top-500 chain sales total).] quote: "$435.38 billion +4.7% since 2023"
- `https://www.restaurantbusinessonline.com/top-100-independents-2025/quartino-ristorante` -> **live_dated** (page date 2025-12-05); points raw/verified 4/0
- dropped by code checks: 16 (period_end missing or unparseable: 10; period_end 2034-12-31 after as_of: 1; number: more than one number in value_as_written: 1; scale word 'billion' not supported by quote or table header: 2; value_as_written not in quote as a whole number: 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1)

### b3 [base_rates] Chicago pizza-culture adjustment

Hypothesis: The per-capita routes assume Chicago residents eat the national average mass of pizza. Chicago's strong pizza culture (deep-dish tourism, high outlet density ~1,987 outlets for 2.75M people) plausibly raises per-capita consumption above the national mean. Evidence on Chicago vs national pizza consumption frequency or per-capita spend would set the adjustment factor that currently dominates uncertainty in m1 and m3.

Queries issued by the searcher: Chicago pizza consumption per capita vs national; pizza restaurants per capita Chicago ranking outlets; pizzerias per 100,000 residents study cities Chicago rank 2025; Chicago pizza spending per household consumer expenditure survey pizza

- `https://www.globenewswire.com/news-release/2025/04/08/3057652/0/en/what-s-pizza-worth-to-you-americans-would-have-to-be-paid-14-million-to-give-up-piz` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://listwithclever.com/research/best-pizza-cities-2025/` -> **live_dated** (page date 2026-08-05); points raw/verified 15/15
  - p163 Chicago pizza restaurants per 100,000 residents (Clever 2025 ranking) = **6** pizza restaurants per 100,000 residents (..) [keep: ] quote: "\| 10 \| Chicago, IL \| 94.7 \| 2 \| 83.1 \| 6.0 \| 3.98 \| $22.73 \| $26.10 \| 2.92% \|"
  - p164 National average pizza restaurants per 100,000 residents (Clever 2025 ranking) = **12.4** pizza restaurants per 100,000 residents (..) [keep: ] quote: "\| - \| National Average \| - \| - \| 68.3 \| 12.4 \| 3.93 \| $18.02 \| $20.42 \| 2.51% \|"
  - p165 Chicago Pizza Passion Score out of 100 (Clever 2025 ranking) = **83.1** score out of 100 (..) [keep: ] quote: "earning the Windy City a significantly above-average Pizza Passion Score of 83.1 out of 100, compared to 68.3 nationally."
  - p166 National average Pizza Passion Score out of 100 = **68.3** score out of 100 (..) [keep: ] quote: "\| - \| National Average \| - \| - \| 68.3 \| 12.4 \| 3.93 \| $18.02 \| $20.42 \| 2.51% \|"
  - p167 Chicago average price of large cheese pizza = **22.73** US dollars (..) [keep: ] quote: "$22.73 for a typical large cheese pizza and $26.10 for a large pepperoni, compared to the national averages of $18.02 and $20.42, respectively."
  - p168 Chicago average price of large pepperoni pizza = **26.1** US dollars (..) [keep: ] quote: "$22.73 for a typical large cheese pizza and $26.10 for a large pepperoni, compared to the national averages of $18.02 and $20.42, respectively."
  - p169 National average price of large cheese pizza = **18.02** US dollars (..) [keep: ] quote: "\| - \| National Average \| - \| - \| 68.3 \| 12.4 \| 3.93 \| $18.02 \| $20.42 \| 2.51% \|"
  - p170 National average price of large pepperoni pizza = **20.42** US dollars (..) [keep: ] quote: "\| - \| National Average \| - \| - \| 68.3 \| 12.4 \| 3.93 \| $18.02 \| $20.42 \| 2.51% \|"
  - p171 Chicago share of median household income for weekly cheese+pepperoni pizza night = **2.92** % (..) [keep: ] quote: "it still adds up to an above-average 2.92% of the city's median household income to buy weekly cheese and pepperoni pizzas."
  - p172 National average share of median household income for weekly cheese+pepperoni pi = **2.51** % (..) [keep: ] quote: "\| - \| National Average \| - \| - \| 68.3 \| 12.4 \| 3.93 \| $18.02 \| $20.42 \| 2.51% \|"
  - p173 Share of Americans selecting Chicago as a top-five pizza city = **57** % (..) [keep: ] quote: "Americans most frequently selected New York (66%), Chicago (57%), Los Angeles (22%), Philadelphia (17%), and Detroit (16%)."
  - p174 Share of Americans selecting Illinois as a top-five pizza state = **56** % (..) [keep: ] quote: "\| 2 \| Illinois \| 56% \|"
  - p175 Share of Americans who love Chicago-style pizza = **40** % (..) [keep: ] quote: "Thick, saucy Chicago-style pizza came in second (40% love, 40% like)"
  - p176 Share of Americans who love New York-style pizza (comparison style) = **51** % (..) [keep: ] quote: "New York-style pizza, known for its thin, foldable crust and large slices, is America's favorite, loved by 51% of respondents and liked by 38% more."
  - p177 Share of Americans saying pizza is their favorite food = **59** % (..) [keep: ] quote: "Approximately 59% of Americans say pizza is their favorite food."
- `https://www.pmq.com/a-list-of-top-10-best-cities-for-pizza-lovers-surprisingly-omits-nyc-chicago/` -> **live_dated** (page date 2023-01-20); points raw/verified 10/9
  - p178 Number of cities analyzed by Apartment Guide that had at least one pizza busines = **11,000** cities (..) [keep: ] quote: "Apartment Guide analyzed roughly 11,000 cities that had at least one pizza business"
  - p179 Minimum share of dining franchises that are pizzerias among the top 10 cities (p = **15** percent of dining franchises (..) [keep: ] quote: "the 10 cities having at least 15% of its dining franchises as pizzerias"
  - p180 Maximum pizzerias per capita cited (Worcester, Massachusetts) = **71** pizzerias per capita (..) [DISCARD: Implausible '71 pizzerias per capita' figure; likely a units error and unusable.] quote: "as high as 71 pizzerias per capita (Worcester, Massachusetts)"
  - p181 Scranton, Pennsylvania rank in Apartment Guide Top 10 Cities for Pizza Lovers (p = **2** rank position (..) [keep: ] quote: "Scranton, Pennsylvania, from ranking No. 2 in Apartment Guide's Top 10 Cities for Pizza Lovers"
  - p182 Poughkeepsie rank among cities in New York making the Top 50 = **16** rank position (..) [keep: ] quote: "Poughkeepsie at 16th"
  - p183 Schenectady rank among cities in New York making the Top 50 = **19** rank position (..) [keep: ] quote: "Schenectady at 19th"
  - p184 Bronx rank among cities in New York making the Top 50 = **21** rank position (..) [keep: ] quote: "Bronx at 21st"
  - p185 Staten Island rank among cities in New York making the Top 50 = **47** rank position (..) [keep: ] quote: "Staten Island at 47th"
  - p186 Multiplier used to express pizza businesses per 100,000 people in Apartment Guid = **100,000** people (denominator for per-capita rate) (..) [DISCARD: Methodological multiplier (100,000 denominator), not a data observation.] quote: "multiplying by 100,000 to determine the number of pizza businesses per 100,000 people"
- `https://www.chicagotribune.com/1988/03/24/ingredients-of-a-great-food-town-3/` -> **live_dated** (page date 2021-08-08); points raw/verified 2/2
  - p187 Chicago per-capita pizza meals per year (1986 survey, Chicagoans named nation's  = **34.8** pizza meals per person per year (1986-01-01..1986-12-31) [keep: ] quote: "Chicagoans were named the nation`s biggest pizza fans in a 1986 survey that has us sitting down to pizza 34.8 times a year."
  - p188 Los Angeles per-capita pizza meals per year (comparison, less than) = **20** pizza meals per person per year (upper bound, stated as 'les (1986-01-01..1986-12-31) [keep: ] quote: "Los Angeles, the home of designer pizzas, averaged less than 20 per capita pizza meals annually."
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['pizza consumption', 'chicago food', 'pizza sales']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p52', 'p63'] Three NHANES-based estimates of the share of the US population 2+ consuming pizza on any given day: 11% (2017-2020), 11% (restated), 13% (2007-2010). Same underlying survey instrument; the 13%→11% dri
- corroborating: ['p2', 'p53', 'p68'] All three give ~6% for adults 60+, from the same NHANES family. Consistent age gradient; useful for age-structuring Chicago's population but not independent of p1.
- corroborating: ['p54', 'p55', 'p64', 'p65'] Age-split prevalence: children ~14-20%, adults ~10-11%. Consistent with the overall 11-13% and the 6% elderly figure. Same survey source.
- corroborating: ['p56', 'p57', 'p58', 'p7'] Source-of-pizza shares: restaurant 56%, grocery 26%, school 12%, other 6%. p7 restates the 6% 'other'. These partition the channel mix and are needed to split restaurant vs at-home mass.
- corroborating: ['p59', 'p60', 'p61', 'p62', 'p4', 'p5', 'p6', 'p75'] Occasion shares (dinner/lunch/snack) for adults and children, from the same USDA report. Internally consistent; used only for context, not a direct mass driver.
- corroborating: ['p73', 'p74'] Mean energy from pizza per consuming day: 538 kcal (children), 744 kcal (adults). These are the key bridge from prevalence to mass via an energy-density conversion.
- corroborating: ['p70', 'p71', 'p72'] Share of pizza consumed at home (59% overall, 65% adults, 49% children). Older vintage (2007-2010) but consistent with the 26% grocery + home-prepared framing; used as a cross-check on channel split.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50', 'p51'] All from one Rentech Digital listing scrape of Chicago pizza restaurants (1,987 outlets, April 2026). Internally consistent (914+1073=1987; 1848+139=1987). Single source, so not independent confirmati
- corroborating: ['p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36'] All from the same Technomic/IFMA Top 500 report: LSR pizza units, AUVs, chain sales, and food-away inflation. One underlying dataset; used together for the sales-based route, not as independent checks
- corroborating: ['p76', 'p77', 'p81'] US frozen pizza retail sales ~$7.2-7.3B (Circana/IMARC) and private label ~$1.1B. Consistent magnitudes; used to size the at-home/frozen channel.
- corroborating: ['p82', 'p83', 'p84', 'p88'] Census-based Chicago city population ~2.75M (2025) and Cook County ~5.2M. Same source (Census via Tribune). The city figure is the pinned denominator; county is context only.
- corroborating: ['p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114'] Market-intelo deep-dish market report: $0.9B global deep-dish market, 65% Illinois/Chicago, occasion splits, and 58.3M visitors with 35-45% seeking deep-dish. Single low-quality vendor report; interna
- corroborating: ['p91', 'p92', 'p93', 'p94', 'p95', 'p96'] Technomic pizza-chain growth (0.5% vs 3% overall) and Giordano's/Lou Malnati's store counts. Consistent slow-growth picture; used for trend context only.
- corroborating: ['p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129'] August 2026 CPI components (food at home 2.2%, away 3.4%, limited-service 3.2%, cheese, flour, produce). Same BLS-derived source; used to deflate/convert 2024-2025 dollar figures to 2026 and to note p
- conflicting: ['p1', 'p80'] NHANES 1-day recall gives 11% consuming on any given day, while Technomic reports 35% weekly consumption in 2025. Not a true contradiction: 'any given day' vs 'any given week' differ by ~7x, and the w
- conflicting: ['p63', 'p1'] 13% (2007-2010) vs 11% (2017-2020) same metric — a genuine decline over time, not a measurement conflict. Supports using the more recent 11% as the base with a possible upward adjustment for 2026 give
- conflicting: ['p104', 'p105', 'p106'] Grips 'Chicago Food Specialties' AOV ($100-200) and Marketintelo deep-dish market ($0.9B) are different scopes (online specialty orders vs global deep-dish restaurant revenue) and cannot be reconciled
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p52'] Same USDA/NHANES-derived statistic (11% of population 2+ consuming pizza on a given day, 2017-2020); p52 is a duplicate restatement of p1, not an independent measurement.
- corroborating: ['p2', 'p53', 'p68'] All report ~6% pizza consumption prevalence among adults 60+; p2/p53 from the 2017-2020 NHANES analysis, p68 from 2007-2010. Consistent across vintages, same survey family.
- corroborating: ['p54', 'p55', 'p64', 'p65'] Age gradient (children higher than adults) consistent across 2017-2020 and 2007-2010 NHANES analyses; magnitude drift reflects period/definition, not contradiction.
- conflicting: ['p1', 'p63'] Overall prevalence 11% (2017-2020) vs 13% (2007-2010). Different periods; treat as declining trend and prefer the recent vintage for 2026.
- corroborating: ['p56', 'p57', 'p58', 'p7'] Source-of-pizza shares (restaurant 56%, grocery 26%, school 12%, other 6%) sum to 100%; p7 restates the 6% other share. Same USDA analysis.
- corroborating: ['p73', 'p74', 'p3'] Energy-based intake measures (538 kcal children, 744 kcal adults; pizza = 27% of consumer daily energy) are mutually consistent and support an energy-to-mass conversion via pizza energy density.
- corroborating: ['p24', 'p151', 'p25', 'p157'] Duplicate restatements of the same IFMA/Datassential LSR pizza segment unit count and AUV; not independent.
- corroborating: ['p27', 'p153', 'p28', 'p154', 'p29', 'p155', 'p30', 'p156'] Chain-level systemwide sales duplicated across d2 and b2 tables; same source, corroborate only as a single measurement.
- corroborating: ['p37', 'p38', 'p39', 'p40', 'p41', 'p42'] Same rentechdigital Chicago pizza-restaurant census (1,987 outlets, 914 single-owner = 46%, 1,073 branded = 54%); internally consistent, single source.
- conflicting: ['p163', 'p164', 'p37'] Clever reports ~6 pizzerias per 100k for Chicago (implying ~165 outlets for 2.75M), far below the 1,987 count in p37. Different definitions (Clever likely counts a narrower 'pizzeria' category or uses
- corroborating: ['p106', 'p144', 'p107', 'p145', 'p146'] Duplicate restatements of the same marketintelo Chicago deep-dish market size ($0.9B, 65% Illinois/Chicago share, 100% North America). Single low-credibility source; use only as a weak cross-check.
- corroborating: ['p112', 'p113', 'p114'] Visitor count and deep-dish-seeking share from the same marketintelo report; internally consistent but single source.
- corroborating: ['p121', 'p122', 'p123', 'p127', 'p128'] 2026 CPI/menu-price inflation figures from one article; consistent picture of ~2-3% food inflation, relevant only for price-to-mass deflation, not mass itself.
- corroborating: ['p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p139'] AGMRC US pizza restaurant industry series (sales, sites, sales/site, sales/person) for 2015-2018; internally consistent single source, useful for per-capita spend benchmark.
- corroborating: ['p159', 'p160', 'p161'] Chicago deep-dish chain systemwide sales (Giordano's, Lou Malnati's, Rosati's) from IFMA; same source, useful as a Chicago-specific anchor.
- corroborating: ['p187', 'p188'] 1986 survey of per-capita pizza meals (Chicago 34.8 vs LA <20); old but directionally supports Chicago above-average consumption.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Average pizza energy density (as served) | 250 | 200..300 | 173..346 (widened) | kcal per 100 g | m1 (m1) | Typical pizza as served (thin, deep-dish, frozen weighted) is roughly 230-280 kcal/100g per USDA FoodData Central; used to convert NHANES energy intake (p73, p74) into pizza mass. | Converting pizza energy intake to served mass for US/Chicago consumers. | A sourced Chicago style-mix energy density outside 200-300 kcal/100g. |
| a2 | Chicago per-capita pizza consumption multiplier vs national | 1.15 | 1..1.4 | 0.8367..1.673 (widened) | ratio | m1 (m1) | Chicago's high pizza passion score (p165 vs p166) and high outlet count (p37) suggest above-national consumption; modest multiplier with wide range. Note p163's low density conflicts with p37, so the multiplier is kept near 1. | Scaling national per-capita pizza mass to Chicago residents. | Evidence that Chicago per-capita pizza spend or frequency equals or trails the national average. |
| a3 | Chicago adult share of population | 0.78 | 0.74..0.82 | 0.5508..1.102 (widened) | fraction | m1 (m1) | Chicago's age structure is somewhat younger than national; used to weight child vs adult energy intake (p73, p74). | Blending child and adult per-consumer energy into a population-average figure. | Census age distribution showing adult share outside 74-82%. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 1,027,630 | ['p82', 'p1', 'p74', 'p73'] / ['a1', 'a2', 'a3'] | [] |  | 1.00 | equal |  |

- m1 coverage: the whole target

Result: central **1,027,630** t/day, 80% interval [574,883, 1,836,936] t/day, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-12-31, after as_of: it cannot have been published yet


## Final answer

The best computed estimate is 1,027,630 t/day (80% model-based interval 574,883 to 1,836,936 t/day) for the city of Chicago proper, averaged over calendar year 2026, counting pizza mass as sold or served. The single method (weight 100%) multiplies Chicago population 2,750,000 people by daily pizza prevalence 11 percent of population, blends adult and child energy intake 744 kilocalories and 538 kilocalories using adult share 0.78, divides by energy density 250 to get mass, and applies a Chicago multiplier 1.15. Observed inputs are population, prevalence, and energy intake; the energy density, Chicago multiplier, and adult share are analyst assumptions with wide ranges (173 to 346, 0.8367 to 1.673, 0.5508 to 1.102). Only one method was used, so no weighting across methods applies. The biggest risk is the energy-density and multiplier assumptions, which drive the interval. Better local pizza-intake survey data for Chicago would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Average pizza energy density (as served): 250 kcal per [n] g, range 173 to 346 (range widened by code); used by m1. Overturned by: A sourced Chicago style-mix energy density outside [n]-[n] kcal/[n]g.
- a2 Chicago per-capita pizza consumption multiplier vs national: 1.15 ratio, range 0.8367 to 1.673 (range widened by code); used by m1. Overturned by: Evidence that Chicago per-capita pizza spend or frequency equals or trails the national average.
- a3 Chicago adult share of population: 0.78 fraction, range 0.5508 to 1.102 (range widened by code); used by m1. Overturned by: Census age distribution showing adult share outside [n]-[n].

# Evidence ledger: fc_us_milk_2026_09

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate total milk production in the 24 major States of the United States in September 2026, in pounds (the report states it in million pounds), as it will be first reported in the USDA National Agricultural Statistics Service's monthly Milk Production report.
- as_of: 2026-10-19
- Pinned target: Total milk production in the 24 major States as defined by USDA NASS, in pounds (reported by NASS in million pounds), during September 2026, as it will be first reported in the USDA NASS monthly Milk Production report. This is a completed-month production flow, not annual or YTD production and not a | unit pounds (reported in million pounds) | period 2026-09-01..2026-09-30 | publisher USDA National Agricultural Statistics Service (NASS)

## Directions and pages

### d1 [own_history] NASS monthly series analyst

Hypothesis: September 2026 24-state milk production should be anchored by the same series in prior Septembers and by 2026 year-to-date monthly values; recent year-over-year growth and the August-to-September seasonal pattern bracket the first-reported September value.

Queries issued by the searcher: USDA NASS Milk Production 24 major States September 2025 million pounds; NASS Milk Production report 2026 24 state milk production August 2026; nass.usda.gov Publications Todays_Reports reports mkpr0926.pdf milk production August 2026; "Milk Production" NASS report September 2024 24 major States "17.5 billion pounds" September 2023 24 states

- `https://www.nass.usda.gov/Publications/Todays_Reports/reports/mkpr1025.pdf` -> **live_dated** (page date 2025-11-07); points raw/verified 15/3
  - p1 24-State milk production, September 2025 (first-reported, million pounds) = **18,300,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Rounded duplicate of p34 for September 2025 24-state production.] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p2 24-State milk production, August 2025 revised (million pounds) = **18,800,000,000** pounds (2025-08-01..2025-08-31) [keep: ] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p3 24-State milk cows, September 2025 (thousand head) = **9,150,000** head (2025-09-01..2025-09-30) [DISCARD: Rounded duplicate of p38 for September 2025 24-state cow inventory; the 38,000-head change is kept as p150.] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p4 24-state milk production, August 2026 (preliminary), billion pounds = **19,172,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state milk production: 19.172 billion pounds, up 1.8%"
  - p5 24-state milk production year-over-year change, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state milk production: 19.172 billion pounds, up 1.8%"
  - p6 U.S. total milk production, August 2026 (preliminary), billion pounds = **19,900,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "- U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p7 U.S. total milk production year-over-year change, August 2026 vs August 2025 = **1.7** % (2026-08-01..2026-08-31) [keep: ] quote: "U.S. milk production rose about 1.7% compared to the same month last year"
  - p8 24-state cow numbers, August 2026, million head = **9,264,000** head (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state cow numbers: 9.264 million, up 151,000 head"
  - p9 24-state cow numbers year-over-year change, August 2026 vs August 2025, head = **151,000** head (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state cow numbers: 9.264 million, up 151,000 head"
  - p10 24-state average milk per cow, August 2026, pounds = **2,070** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p11 24-state average milk per cow year-over-year change, August 2026 vs August 2025, = **4** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "- 24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p12 U.S. cow numbers, August 2026, million head = **9,710,000** head (2026-08-01..2026-08-31) [keep: ] quote: "- U.S. cow numbers: 9.71 million, up 167,000 head"
  - p13 U.S. average milk per cow, August 2026, pounds = **2,049** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "- U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p14 Combined production increase, sixteen states, August 2026 vs August 2025, millio = **393,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p15 Combined production decrease, seven states, August 2026 vs August 2025, million  = **48,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p16 Texas milk production year-over-year increase, August 2026 vs August 2025, milli = **78,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p17 Kansas milk production year-over-year increase, August 2026 vs August 2025, mill = **61,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p18 California milk production year-over-year decline, August 2026 vs August 2025, m = **24,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
- `https://arec.tennessee.edu/extension/tennessee-market-highlights/monthly-dairy-comments/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/15
  - p19 24-state total milk production, August 2026 = **19,200,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p4 for August 2026 24-state production.] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p20 24-state milk production year-over-year change, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p21 24-state milk production per cow, August 2026 = **2,070** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "Production per cow for August averaged 2,070 pounds."
  - p22 24-state milk cow inventory, August 2026 = **9,260,000** head (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p8 for August 2026 24-state cow inventory.] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p23 24-state milk cow inventory change, August 2026 vs July 2026 = **15,000** head (2026-08-01..2026-08-31) [keep: ] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p24 24-state July 2026 milk production revision from preliminary estimates = **0.5** % (2026-07-01..2026-07-31) [keep: ] quote: "July production was revised down 0.5 percent from preliminary estimates."
  - p25 California milk production year-over-year change, August 2026 vs August 2025 = **0.7** % (2026-08-01..2026-08-31) [keep: ] quote: "California decreased 0.7% from August a year ago"
  - p26 Wisconsin milk production year-over-year change, August 2026 vs August 2025 = **1.5** % (2026-08-01..2026-08-31) [keep: ] quote: "Wisconsin up 1.5%"
  - p27 Texas milk production year-over-year change, August 2026 vs August 2025 = **5.1** % (2026-08-01..2026-08-31) [keep: ] quote: "Texas up 5.1%"
  - p28 Idaho milk production year-over-year change, August 2026 vs August 2025 = **1.6** % (2026-08-01..2026-08-31) [keep: ] quote: "Idaho up 1.6%"
  - p29 New York milk production year-over-year change, August 2026 vs August 2025 = **0.9** % (2026-08-01..2026-08-31) [keep: ] quote: "New York up 0.9%"
  - p30 Kansas milk production year-over-year change, August 2026 vs August 2025 = **13.9** % (2026-08-01..2026-08-31) [keep: ] quote: "Kansas (13.9%)"
  - p31 South Dakota milk production year-over-year change, August 2026 vs August 2025 = **8.4** % (2026-08-01..2026-08-31) [keep: ] quote: "South Dakota (8.4%)"
  - p32 Utah milk production year-over-year change, August 2026 vs August 2025 = **-3.6** % (2026-08-01..2026-08-31) [keep: ] quote: "Utah (-3.6%)"
  - p33 Arizona milk production year-over-year change, August 2026 vs August 2025 = **-3.1** % (2026-08-01..2026-08-31) [keep: ] quote: "Arizona (-3.1%)"
- `https://www.agproud.com/articles/62477-milk-production-continues-to-rise-in-usda-september-estimates` -> **live_dated** (page date 2025-11-10); points raw/verified 15/15
  - p34 24-state milk production, September 2025 preliminary (USDA NASS) = **18,279,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state milk production: 18.279 billion pounds, up 4.2%"
  - p35 24-state milk production year-over-year change, September 2025 vs September 2024 = **4.2** % (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state milk production: 18.279 billion pounds, up 4.2%"
  - p36 U.S. total milk production, September 2025 preliminary (USDA NASS) = **18,990,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "- U.S. milk production: 18.99 billion pounds, up 4%"
  - p37 U.S. total milk production year-over-year change, September 2025 vs September 20 = **4** % (2025-09-01..2025-09-30) [keep: ] quote: "- U.S. milk production: 18.99 billion pounds, up 4%"
  - p38 24-state cow numbers, September 2025 = **9,146,000** head (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state cow numbers: 9.146 million, up 235,000 head"
  - p39 24-state cow numbers year-over-year change, September 2025 vs September 2024 = **235,000** head (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state cow numbers: 9.146 million, up 235,000 head"
  - p40 24-state average milk per cow, September 2025 = **1,999** pounds per cow (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state average milk per cow: 1,999 pounds, up 30 pounds"
  - p41 24-state average milk per cow year-over-year change, September 2025 vs September = **30** pounds per cow (2025-09-01..2025-09-30) [keep: ] quote: "- 24-state average milk per cow: 1,999 pounds, up 30 pounds"
  - p42 U.S. cow numbers, September 2025 = **9,581,000** head (2025-09-01..2025-09-30) [keep: ] quote: "- U.S. cow numbers: 9.581 million, up 228,000 head"
  - p43 U.S. average milk per cow, September 2025 = **1,982** pounds per cow (2025-09-01..2025-09-30) [keep: ] quote: "- U.S. average milk per cow: 1,982 pounds, up 30 pounds"
  - p44 Combined production increase across twenty states, September 2025 vs September 2 = **789,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Twenty states boosted production a combined 789 million pounds; four states reduced production a combined 54 million pounds."
  - p45 Combined production reduction across four states, September 2025 vs September 20 = **54,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Twenty states boosted production a combined 789 million pounds; four states reduced production a combined 54 million pounds."
  - p46 Idaho milk production year-over-year increase, September 2025 vs September 2024 = **129,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Year-over-year growth leaders were Idaho (up 129 million pounds), Texas (up 103 million pounds) and New York (up 79 million pounds)."
  - p47 Texas milk production year-over-year increase, September 2025 vs September 2024 = **103,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Year-over-year growth leaders were Idaho (up 129 million pounds), Texas (up 103 million pounds) and New York (up 79 million pounds)."
  - p48 New York milk production year-over-year increase, September 2025 vs September 20 = **79,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Year-over-year growth leaders were Idaho (up 129 million pounds), Texas (up 103 million pounds) and New York (up 79 million pounds)."
- dropped by code checks: 12 (value_as_written not in quote as a whole number: 12)

### d2 [physical_flow] Dairy cow inventory and yield analyst

Hypothesis: Milk production equals average milk cows times milk produced per cow for the month, adjusted for September length; estimates of September 2026 24-state cow inventory and yield per cow can independently reconstruct the target.

Queries issued by the searcher: NASS Milk Production 24 major States milk cows milk per cow August 2026; USDA Cattle report July 2026 milk cow inventory; September 2025 milk production 24 major states milk per cow September 2025 NASS 18.3 billion pounds; "milk per cow" "24 major states" September 2024 September 2025 pounds table NASS Milk Production

- `https://www.nass.usda.gov/Publications/Todays_Reports/reports/mkpr1025.pdf` -> **live_dated** (page date 2025-11-07); points raw/verified 15/5
  - p49 24-State September 2025 milk production = **18,300,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p34 for September 2025 24-state production.] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p50 24-State September 2025 milk per cow = **1,999** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of p40 for September 2025 24-state milk per cow.] quote: "Production per cow in the 24 major States averaged 1,999 pounds for September, 30 pounds above September 2024."
  - p51 24-State September 2025 milk cows = **9,150,000** head (2025-09-01..2025-09-30) [DISCARD: Rounded duplicate of p38 for September 2025 24-state cow inventory.] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
  - p52 24-State August 2025 revised milk production = **18,800,000,000** pounds (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 for August 2025 revised 24-state production.] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p53 24-State September 2025 milk cows change vs September 2024 = **235,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of the September 2025 24-state cow year-over-year change already in p38/p3.] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p54 24-state milk production, August 2026 (preliminary), up 1.8% year over year = **19,172,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p4 for August 2026 24-state production.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p55 24-state average milk cows, August 2026 (preliminary), up 151,000 head year over = **9,264,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p8 for August 2026 24-state cow inventory.] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p56 24-state average milk per cow, August 2026 (preliminary), up 4 pounds year over  = **2,070** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p57 U.S. milk production, August 2026 (preliminary), up 1.7% year over year = **19,900,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p6 for U.S. August 2026 milk production.] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p58 U.S. cow numbers, August 2026 (preliminary), up 167,000 head year over year = **9,710,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p12 for U.S. August 2026 cow inventory.] quote: "U.S. cow numbers: 9.71 million, up 167,000 head"
  - p59 U.S. average milk per cow, August 2026 (preliminary), down 1 pound year over yea = **2,049** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p13 for U.S. August 2026 milk per cow.] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p60 Year-over-year change in 24-state average milk per cow, August 2026 vs August 20 = **4** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p11 for August 2026 24-state milk-per-cow year-over-year change.] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p61 Year-over-year change in 24-state cow numbers, August 2026 vs August 2025 = **151,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p9 for August 2026 24-state cow year-over-year change.] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p62 Year-over-year change in U.S. cow numbers, August 2026 vs August 2025 = **167,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of the U.S. cow year-over-year change already in p12.] quote: "U.S. cow numbers: 9.71 million, up 167,000 head"
  - p63 Year-over-year change in U.S. average milk per cow, August 2026 vs August 2025 = **1** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Sign is ambiguous: name/value suggest a positive change but quote says down 1 pound.] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p64 Year-over-year percent change in 24-state milk production, August 2026 vs August = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p65 Year-over-year percent change in U.S. milk production, August 2026 vs August 202 = **1.7** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p7 for U.S. August 2026 year-over-year growth.] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p66 Combined year-over-year increase in cow numbers for Kansas and Texas, August 202 = **58,000** head (2026-08-01..2026-08-31) [keep: ] quote: "Kansas and Texas led all states in year-over-year growth, up a combined 58,000 head in August."
  - p67 Combined year-over-year reduction in cow numbers for Arizona and Utah, August 20 = **9,000** head (2026-08-01..2026-08-31) [keep: ] quote: "That was partially offset by a combined 9,000-head reduction in Arizona and Utah."
  - p68 Combined year-over-year increase in milk production across 16 states, August 202 = **393,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p14 for sixteen-state August 2026 production gain.] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
- `https://arec.tennessee.edu/extension/tennessee-market-highlights/monthly-dairy-comments/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/14
  - p69 24-state total milk production, August 2026 = **19,200,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p4 for August 2026 24-state production.] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p70 24-state milk production per cow, August 2026 average = **2,070** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "Production per cow for August averaged 2,070 pounds."
  - p71 24-state milk cow inventory, August 2026 = **9,260,000** head (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p8 for August 2026 24-state cow inventory.] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p72 Change in 24-state milk cow inventory, August 2026 vs July 2026 = **15,000** head (2026-08-01..2026-08-31) [keep: ] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p73 24-state milk production, August 2026 vs August 2025 change = **1.8** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p74 July 2026 24-state milk production revision from preliminary estimates = **0.5** percent (2026-07-01..2026-07-31) [DISCARD: Duplicate of p24 for July 2026 revision.] quote: "July production was revised down 0.5 percent from preliminary estimates."
  - p75 Dairy cow slaughter, August 2026 = **221,100** head (2026-08-01..2026-08-31) [keep: ] quote: "Dairy cow slaughter in August was 221,100 head, down 6,500 head from July and 3,700 head more than August 2025."
  - p76 Dairy cow slaughter change, August 2026 vs July 2026 = **6,500** head (2026-08-01..2026-08-31) [keep: ] quote: "Dairy cow slaughter in August was 221,100 head, down 6,500 head from July and 3,700 head more than August 2025."
  - p77 Dairy cow slaughter change, August 2026 vs August 2025 = **3,700** head (2026-08-01..2026-08-31) [keep: ] quote: "Dairy cow slaughter in August was 221,100 head, down 6,500 head from July and 3,700 head more than August 2025."
  - p78 Wisconsin milk production change, August 2026 vs August 2025 = **1.5** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p26 for Wisconsin August 2026 growth.] quote: "Wisconsin up 1.5%"
  - p79 Texas milk production change, August 2026 vs August 2025 = **5.1** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p27 for Texas August 2026 growth.] quote: "Texas up 5.1%"
  - p80 Idaho milk production change, August 2026 vs August 2025 = **1.6** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p28 for Idaho August 2026 growth.] quote: "Idaho up 1.6%"
  - p81 New York milk production change, August 2026 vs August 2025 = **0.9** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p29 for New York August 2026 growth.] quote: "New York up 0.9%"
  - p82 Kansas milk production change, August 2026 vs August 2025 = **13.9** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p30 for Kansas August 2026 growth.] quote: "Other states with large production increases were Kansas (13.9%)"
- `https://www.nass.usda.gov/Newsroom/2026/07-24-2026.php` -> **live_dated** (page date 2026-07-24); points raw/verified 0/0
- dropped by code checks: 11 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 10; value_as_written not in quote as a whole number: 1)

### d3 [related_series] National dairy supply analyst

Hypothesis: The 24-state total is a high-share subset of U.S. milk production; multiplying a September 2026 U.S. total estimate by the recent 24-state share should approximate the target if the share is stable and if both series use comparable monthly definitions.

Queries issued by the searcher: USDA NASS Milk Production 24 major States United States total September 2025 million pounds; USDA NASS Milk Production report August 2026 24 states million pounds; USDA WASDE 2026 milk production forecast million pounds; 24 major milk producing states share U.S. milk production September 2024

- `https://www.nass.usda.gov/Publications/Todays_Reports/reports/mkpr1025.pdf` -> **live_dated** (page date 2025-11-07); points raw/verified 15/3
  - p83 24-state total milk production, September 2025 = **18,300,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p34 for September 2025 24-state production.] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p84 24-state total milk production, August 2025 (revised) = **18,800,000,000** pounds (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 for August 2025 revised 24-state production.] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p85 U.S. total milk production, July-September 2025 quarter = **58,200,000,000** pounds (2025-07-01..2025-09-30) [keep: ] quote: "Milk production in the United States during the July - September quarter totaled 58.2 billion pounds, up 3.8 percent from the July - September quarter last year."
- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p86 U.S. total milk production, August 2026 preliminary (USDA NASS) = **19,900,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p6 for U.S. August 2026 milk production.] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p87 24-state milk production, August 2026 preliminary (USDA NASS) = **19,172,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p4 for August 2026 24-state production.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p88 U.S. milk production year-over-year change, August 2026 vs August 2025 = **1.7** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p7 for U.S. August 2026 year-over-year growth.] quote: "U.S. milk production rose about 1.7% compared to the same month last year"
  - p89 24-state milk production year-over-year change, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p90 U.S. cow numbers, August 2026 = **9,710,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p12 for U.S. August 2026 cow inventory.] quote: "U.S. cow numbers: 9.71 million, up 167,000 head"
  - p91 24-state cow numbers, August 2026 = **9,264,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p8 for August 2026 24-state cow inventory.] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p92 U.S. average milk per cow, August 2026 = **2,049** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p13 for U.S. August 2026 milk per cow.] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p93 24-state average milk per cow, August 2026 = **2,070** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p94 Combined production increase across 16 states, August 2026 vs August 2025 = **393,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p14 for sixteen-state August 2026 production gain.] quote: "Sixteen states boosted production a combined 393 million pounds"
  - p95 Combined production reduction across 7 states, August 2026 vs August 2025 = **48,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p15 for seven-state August 2026 production loss.] quote: "seven states reduced production a combined 48 million pounds"
  - p96 Texas milk production year-over-year increase, August 2026 vs August 2025 = **78,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p16 for Texas August 2026 volume gain.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p97 Kansas milk production year-over-year increase, August 2026 vs August 2025 = **61,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p17 for Kansas August 2026 volume gain.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p98 Wisconsin milk production year-over-year increase, August 2026 vs August 2025 = **43,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Wisconsin volume gain is already contained in p16 and p134.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p99 California milk production year-over-year decline, August 2026 vs August 2025 = **24,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p18 for California August 2026 volume decline.] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
  - p100 Arizona milk production year-over-year decline, August 2026 vs August 2025 = **12,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
- `https://lmic.info/wp-content/lmic-files/lmic-data/memberspublic/Meetings/IOC2026/5_McConnell-Dairy%20Outlook%20Apr2026.pdf` -> **live_dated** (page date 2026-04-16); points raw/verified 15/4
  - p101 U.S. annual milk production percent change, Q3 2026 projection = **0.9** percent (2026-07-01..2026-09-30) [DISCARD: Stale Q3 2026 forecast from April 2026, superseded by observed August 2026 growth.] quote: "III 56.1 58.2 58.7 0.9"
  - p102 U.S. annual milk production percent change, Q1 2026 projection = **2.9** percent (2026-01-01..2026-03-31) [keep: ] quote: "I 57.0 56.9 58.5 2.9"
  - p103 U.S. annual milk production percent change, Q2 2026 projection = **1.7** percent (2026-04-01..2026-06-30) [keep: ] quote: "II 57.3 58.8 59.8 1.7"
  - p104 U.S. annual milk production percent change, Q3 2025 = **0.9** percent (2025-07-01..2025-09-30) [DISCARD: Label/period appears confused with the Q3 forecast table; not a clean historical observation.] quote: "III 56.1 58.2 58.7 0.9"
- `https://www.agproud.com/articles/64261-usda-milk-production-forecast-reverses-course-dips-lower` -> **live_dated** (page date 2026-10-09); points raw/verified 14/4
  - p105 Total U.S. milk production for calendar year 2025 (billion pounds) = **231,700,000,000** pounds (2025-01-01..2025-12-31) [keep: ] quote: "but still up 5.2 billion from 2025's total of 231.7 billion pounds."
  - p106 Dairy-quality alfalfa hay average price, August (USD per ton) = **243** USD per ton (2026-08-01..2026-08-31) [keep: ] quote: "dairy-quality alfalfa hay prices averaged $243 per ton in August"
  - p107 Alfalfa hay average price, August (USD per ton) = **206** USD per ton (2026-08-01..2026-08-31) [keep: ] quote: "alfalfa hay prices averaged $206 per ton"
  - p108 Other hay average price, August (USD per ton) = **152** USD per ton (2026-08-01..2026-08-31) [keep: ] quote: "prices for other hay averaged $152 per ton."
- dropped by code checks: 33 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 12; scale word 'billion' not supported by quote or table header: 9; period_end 2026-12-31 after as_of: 7; period_end 2027-12-31 after as_of: 5)

### d4 [related_series] State-level dairy production analyst

Hypothesis: The 24-state aggregate is the sum of production in the component major states; state-level trends in large producers can reveal whether the aggregate should run above or below a simple national trend, especially if some states diverge sharply.

Queries issued by the searcher: USDA NASS Milk Production report 24 major states August 2026 million pounds; NASS milk production September 2025 California Wisconsin Idaho Texas New York Pennsylvania Michigan Minnesota New Mexico Washington; mkpr0926.pdf milk production August 2026 states table nass.usda.gov; "Milk Cows and Production" "September 2026" states United States nass pdf

- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p109 U.S. total milk production, August 2026 preliminary estimate = **19,900,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p6 for U.S. August 2026 milk production.] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p110 24-state milk production, August 2026 preliminary estimate = **19,172,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p4 for August 2026 24-state production.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p111 24-state year-over-year change in milk production, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p112 U.S. year-over-year change in milk production, August 2026 vs August 2025 = **1.7** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p7 for U.S. August 2026 year-over-year growth.] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p113 24-state cow numbers, August 2026 = **9,264,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p8 for August 2026 24-state cow inventory.] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p114 24-state average milk per cow, August 2026 = **2,070** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p115 U.S. average milk per cow, August 2026 = **2,049** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p13 for U.S. August 2026 milk per cow.] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p116 Texas year-over-year change in milk production, August 2026 vs August 2025 = **78,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p16 for Texas August 2026 volume gain.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p117 Kansas year-over-year change in milk production, August 2026 vs August 2025 = **61,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p17 for Kansas August 2026 volume gain.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p118 Wisconsin year-over-year change in milk production, August 2026 vs August 2025 = **43,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Wisconsin volume gain is already contained in p16 and p134.] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p119 California year-over-year change in milk production, August 2026 vs August 2025 = **24,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p18 for California August 2026 volume decline.] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
  - p120 Arizona year-over-year change in milk production, August 2026 vs August 2025 = **12,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p100 for Arizona August 2026 volume decline.] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
  - p121 Kansas year-over-year percentage growth in milk production, August 2026 vs Augus = **13.93** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p30 for Kansas August 2026 percentage growth.] quote: "Kansas was the milk percentage growth leader for August 2026, up 13.93% from August 2025, with South Dakota following at 8.35% and Oregon at 7.69%."
  - p122 South Dakota year-over-year percentage growth in milk production, August 2026 vs = **8.35** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p31 for South Dakota August 2026 percentage growth.] quote: "Kansas was the milk percentage growth leader for August 2026, up 13.93% from August 2025, with South Dakota following at 8.35% and Oregon at 7.69%."
  - p123 Combined year-over-year production increase across sixteen states, August 2026 v = **393,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p14 for sixteen-state August 2026 production gain.] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
- `http://www.farmers-exchange.net/detailPage.aspx?articleID=25601` -> **live_dated** (page date 2026-10-16); points raw/verified 16/16
  - p124 24-state total milk production, August 2026 = **19,170,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Rounded duplicate of p4 for August 2026 24-state production.] quote: "The 24 state August total came in at 19.17 billion pounds, up 1.8% from a year ago."
  - p125 24-state total milk production year-over-year change, August 2026 = **1.8** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p5 for August 2026 24-state year-over-year growth.] quote: "The 24 state August total came in at 19.17 billion pounds, up 1.8% from a year ago."
  - p126 24-state total milk production, July 2026 (revised) = **19,300,000,000** pounds (2026-07-01..2026-07-31) [keep: ] quote: "The 24 state total was revised down 100 million pounds, to 19.3 billion, up 1.8%, instead of the 2.3% originally reported."
  - p127 24-state total milk production year-over-year change, July 2026 (revised) = **1.8** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p126 for July 2026 revised production growth.] quote: "The 24 state total was revised down 100 million pounds, to 19.3 billion, up 1.8%, instead of the 2.3% originally reported."
  - p128 50-state total milk production, August 2026 = **19,900,000,000** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p6 for U.S. August 2026 milk production.] quote: "The Agriculture Department's latest data shows output at 19.9 billion pounds, up 1.7% from August 2025"
  - p129 50-state total milk production year-over-year change, August 2026 = **1.7** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p7 for U.S. August 2026 year-over-year growth.] quote: "The Agriculture Department's latest data shows output at 19.9 billion pounds, up 1.7% from August 2025, which followed a 1.7% rise in July."
  - p130 24-state milk per cow, August 2026 = **2,070** pounds per cow (2026-08-01..2026-08-31) [DISCARD: Duplicate of p10 for August 2026 24-state milk per cow.] quote: "The 24 state average, at 2,070 pounds, was up 4 pounds or .2% from 2025."
  - p131 24-state milk cow numbers, August 2026 = **9,264,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p8 for August 2026 24-state cow inventory.] quote: "The 24 state count, at 9.264 million, was up 15,000 head from July's total which was revised down 18,000, but was up 151,000, or 1.7%, from a year ago."
  - p132 California milk production, August 2026 = **3,400,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "California produced just under 3.4 billion pounds of milk, down 24 million, or .7%, from a year ago"
  - p133 California milk production year-over-year change, August 2026 = **0.7** as written ".7%", value check pending % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p25 for California August 2026 percentage decline.] quote: "California produced just under 3.4 billion pounds of milk, down 24 million, or .7%, from a year ago"
  - p134 Wisconsin milk production, August 2026 = **2,800,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Wisconsin produced 2.8 billion pounds of milk, up 43 million, or 1.5%, from a year ago."
  - p135 Wisconsin milk production year-over-year change, August 2026 = **1.5** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p26 for Wisconsin August 2026 percentage growth.] quote: "Wisconsin produced 2.8 billion pounds of milk, up 43 million, or 1.5%, from a year ago."
  - p136 Idaho milk production, August 2026 = **1,600,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Idaho output hit 1.6 billion pounds, up 26 million, or 1.6%, from a year ago, thanks to 12,000 more cows."
  - p137 Idaho milk production year-over-year change, August 2026 = **1.6** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of p28 for Idaho August 2026 percentage growth.] quote: "Idaho output hit 1.6 billion pounds, up 26 million, or 1.6%, from a year ago, thanks to 12,000 more cows."
  - p138 Michigan milk production, August 2026 = **1,100,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Michigan put 1.1 billion pounds in the tank, up 28 million or 2.6%"
  - p139 Michigan milk production year-over-year change, August 2026 = **2.6** % (2026-08-01..2026-08-31) [DISCARD: Duplicate of the Michigan percentage change already in p138.] quote: "Michigan put 1.1 billion pounds in the tank, up 28 million or 2.6%"
- `https://keyagdairydiary.blogspot.com/2025/11/july-september-milk-production-up-38.html` -> **live_dated** (page date 2025-11-13); points raw/verified 15/15
  - p140 Milk production in the 24 major States, September total = **18,300,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p34 for September 2025 24-state production.] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p141 Year-over-year change in 24 major States milk production, September = **4.2** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of the September 2025 24-state year-over-year growth already in p34.] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p142 Revised milk production in the 24 major States, August = **18,800,000,000** pounds (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 for August 2025 revised 24-state production.] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p143 Year-over-year change in 24 major States milk production, August revised = **3.6** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of the August 2025 year-over-year growth already in p2.] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p144 August revision increase from prior preliminary estimate, 24 major States = **44,000,000** pounds (2025-08-01..2025-08-31) [keep: ] quote: "The August revision represented an increase of 44 million pounds or 0.2 percent from last month's preliminary production estimate."
  - p145 August revision increase as percent of prior preliminary estimate, 24 major Stat = **0.2** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p144 for August revision percentage.] quote: "The August revision represented an increase of 44 million pounds or 0.2 percent from last month's preliminary production estimate."
  - p146 Production per cow in the 24 major States, September average = **1,999** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of p40 for September 2025 24-state milk per cow.] quote: "Production per cow in the 24 major States averaged 1,999 pounds for September, 30 pounds above September 2024."
  - p147 Year-over-year change in production per cow, 24 major States, September = **30** pounds per cow (2025-09-01..2025-09-30) [keep: ] quote: "Production per cow in the 24 major States averaged 1,999 pounds for September, 30 pounds above September 2024."
  - p148 Milk cows on farms in the 24 major States, September = **9,150,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of p38 for September 2025 24-state cow inventory.] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
  - p149 Year-over-year change in 24 major States milk cow inventory, September = **235,000** head (2025-09-01..2025-09-30) [keep: ] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
  - p150 Month-over-month change in 24 major States milk cow inventory, September vs Augu = **38,000** head (2025-09-01..2025-09-30) [keep: ] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
  - p151 United States milk production, July-September quarter total = **58,200,000,000** pounds (2025-07-01..2025-09-30) [DISCARD: Duplicate of p85 for U.S. Q3 2025 production.] quote: "Milk production in the United States during the July - September quarter totaled 58.2 billion pounds, up 3.8 percent from the July - September quarter last year."
  - p152 Year-over-year change in United States milk production, July-September quarter = **3.8** % (2025-07-01..2025-09-30) [DISCARD: Duplicate of p85 for U.S. Q3 2025 year-over-year growth.] quote: "Milk production in the United States during the July - September quarter totaled 58.2 billion pounds, up 3.8 percent from the July - September quarter last year."
  - p153 Average milk cows in the United States, July-September quarter = **9,540,000** head (2025-07-01..2025-09-30) [keep: ] quote: "The average number of milk cows in the United States during the quarter was 9.54 million head, 82,000 head more than the April - June quarter, and 199,000 head more than the same period last year."
  - p154 Year-over-year change in average United States milk cow inventory, July-Septembe = **199,000** head (2025-07-01..2025-09-30) [keep: ] quote: "The average number of milk cows in the United States during the quarter was 9.54 million head, 82,000 head more than the April - June quarter, and 199,000 head more than the same period last year."
- `https://farmshine.news/2025/11/14/u-s-milk-production-surges-as-the-national-herd-grows/` -> **live_dated** (page date 2025-11-14); points raw/verified 15/15
  - p155 U.S. total milk output in September (all states) = **18,990,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p36 for U.S. September 2025 production.] quote: "U.S. milk output in September totaled 18.99 billion pounds, up 4.0% from a year earlier."
  - p156 U.S. milking herd size in September = **9,581,000** cows (2025-09-01..2025-09-30) [DISCARD: Conflicts with p42/p208 on U.S. September 2025 cow year-over-year change and is likely a typo/revision.] quote: "The milking herd reached 9.581 million cows, up 238,000 head from last year and the largest since 1993."
  - p157 U.S. July-through-September quarterly milk production = **58,200,000,000** pounds (2025-07-01..2025-09-30) [DISCARD: Duplicate of p85 for U.S. Q3 2025 production.] quote: "showing July through Sept. production totaled 58.2 billion pounds, up 3.8% from third quarter 2024."
  - p158 U.S. average milk cows in third-quarter 2025 = **9,540,000** cows (2025-07-01..2025-09-30) [DISCARD: Duplicate of p153 for U.S. Q3 2025 average cows.] quote: "The average number of milk cows in the U.S. during third-quarter 2025 was reported at 9.54 million head"
  - p159 California YoY milk production change, September = **2.4** % (2025-09-01..2025-09-30) [keep: ] quote: "California added 5000 cows (+2.4% milk)"
  - p160 Wisconsin YoY milk production change, September = **3.8** % (2025-09-01..2025-09-30) [keep: ] quote: "Wisconsin (+14,000 cows, +3.8% milk)"
  - p161 Idaho YoY milk production change, September = **9** % (2025-09-01..2025-09-30) [keep: ] quote: "Idaho added 53,000 (+9% milk)"
  - p162 Texas YoY milk production change, September = **7.4** % (2025-09-01..2025-09-30) [keep: ] quote: "Texas added 36,000 cows YoY (+7.4% milk)"
  - p163 New York YoY milk production change, September = **6** % (2025-09-01..2025-09-30) [keep: ] quote: "putting it 25,000 cows above year ago, producing 6% more milk"
  - p164 Pennsylvania YoY milk production change, September = **0.4** % (2025-09-01..2025-09-30) [keep: ] quote: "Pennsylvania remains 5000 cows below year-ago levels but produced 0.4% more milk"
  - p165 Minnesota YoY milk production change, September = **4.5** % (2025-09-01..2025-09-30) [keep: ] quote: "Minnesota (+14,000, +4.5%)"
  - p166 New Mexico YoY milk production change, September = **1.3** % (2025-09-01..2025-09-30) [keep: ] quote: "New Mexico (-3000 cows, -1.3% milk)"
  - p167 Washington YoY milk production change, September = **8.5** % (2025-09-01..2025-09-30) [keep: ] quote: "Washington's decline continued at 23,000 fewer cows making 8.5% less milk."
  - p168 Kansas YoY milk production change, September = **21.1** % (2025-09-01..2025-09-30) [keep: ] quote: "Kansas was up 38,000 for a whopping +21.1% milk increase"
  - p169 National per-cow milk gain YoY, September = **30** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of the September 2025 national per-cow gain already in p43/p147.] quote: "slightly under the national per-cow gain of 30 pounds"

### d5 [administrative] Livestock slaughter and culling analyst

Hypothesis: Milk cow slaughter and dairy heifer replacement rates are administrative traces of herd reduction; if September 2026 culling ran above or below normal, the 24-state cow inventory and therefore production likely moved in the opposite direction after a lag.

Queries issued by the searcher: USDA NASS Livestock Slaughter 2026 milk cows monthly federally inspected; weekly milk cow slaughter 2026 USDA AMS report; dairy cow slaughter September 2026 weekly USDA 2025 comparison; NASS Milk Production report August 2026 24 States million pounds

- `https://www.agproud.com/articles/64012-us-dairy-herd-growth-drives-july-cow-culling-higher` -> **live_dated** (page date 2026-08-24); points raw/verified 15/13
  - p170 US dairy cull cows marketed through slaughter plants, July 2026 = **227,600** head (2026-07-01..2026-07-31) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in July 2026 was estimated at 227,600"
  - p171 Month-over-month change in US dairy cull cow slaughter, June to July 2026 = **19,500** head (2026-07-01..2026-07-31) [keep: ] quote: "While up 19,500 from June, it was also 1,800 more than July 2025."
  - p172 Year-over-year change in US dairy cull cow slaughter, July 2026 vs July 2025 = **1,800** head (2026-07-01..2026-07-31) [keep: ] quote: "While up 19,500 from June, it was also 1,800 more than July 2025."
  - p173 Non-holiday weekdays and Saturdays in July 2025 = **26** days (2025-07-01..2025-07-31) [DISCARD: Calendar detail for July 2025; not needed for the September 2026 target.] quote: "July 2025 had 26 non-holiday weekdays and Saturdays while July 2026 also had 26 days."
  - p174 Non-holiday weekdays and Saturdays in July 2026 = **26** days (2026-07-01..2026-07-31) [DISCARD: Calendar detail for July 2026; not needed for the September 2026 target.] quote: "July 2025 had 26 non-holiday weekdays and Saturdays while July 2026 also had 26 days."
  - p175 Average dairy cow slaughter per business day, July 2026 = **8,800** head per business day (2026-07-01..2026-07-31) [keep: ] quote: "Slaughter averaged 8,800 head per business day this year, up 100 head from a year earlier."
  - p176 Year-over-year change in average daily dairy cow slaughter, July 2026 vs July 20 = **100** head per business day (2026-07-01..2026-07-31) [keep: ] quote: "Slaughter averaged 8,800 head per business day this year, up 100 head from a year earlier."
  - p177 USDA estimated July 2026 U.S. dairy herd = **9,710,000** dairy cows (2026-07-01..2026-07-31) [keep: ] quote: "The USDA estimated the July 2026 U.S. dairy herd at 9.71 million dairy cows, up 199,000 cows from July 2025."
  - p178 Year-over-year change in U.S. dairy herd, July 2026 vs July 2025 = **199,000** dairy cows (2026-07-01..2026-07-31) [DISCARD: Duplicate of the July 2026 U.S. cow year-over-year change already in p177.] quote: "The USDA estimated the July 2026 U.S. dairy herd at 9.71 million dairy cows, up 199,000 cows from July 2025."
  - p179 July 2026 culling rate as share of dairy herd = **2.3** % (2026-07-01..2026-07-31) [keep: ] quote: "It was also unchanged from the June estimate and put the July culling rate at about 2.3% of the herd."
  - p180 Year-to-date (January-July) 2026 dairy cull cow slaughter = **1,565,800** head (2026-01-01..2026-07-31) [keep: ] quote: "year-to-date (January-July) dairy cull cow slaughter now stands at about 1,565,800 head, up 64,600 from the same period a year ago."
  - p181 Year-over-year change in year-to-date (January-July) dairy cull cow slaughter, 2 = **64,600** head (2026-01-01..2026-07-31) [keep: ] quote: "year-to-date (January-July) dairy cull cow slaughter now stands at about 1,565,800 head, up 64,600 from the same period a year ago."
  - p182 July 2026 dairy cow slaughter, Upper Midwest region (IL, IN, MI, MN, OH, WI) = **58,700** head (2026-07-01..2026-07-31) [keep: ] quote: "Heaviest dairy cow culling during July occurred in the Upper Midwest (Illinois, Indiana, Michigan, Minnesota, Ohio and Wisconsin) at 58,700 head."
- `https://teseo.clal.it/en/?section=us_slaughter` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.ers.usda.gov/media/29466/ldp-m-386.pdf` -> **live_dated** (page date 2026-08-18); points raw/verified 15/11
  - p183 Dairy replacement heifers, United States, July 1, 2026 = **3,600,000** head (2026-07-01..2026-07-01) [keep: ] quote: "dairy replacement heifers rose 2.9 percent to 3.600 million head"
  - p184 Dairy replacement heifers, United States, July 1, 2026 (Cattle report, increase  = **100,000** head (2026-07-01..2026-07-01) [keep: ] quote: "milk replacement heifers totaled 3.600 million head as of July 1, 2026, an increase of 100,000 head from July 1, 2025"
  - p185 Ratio of milk replacement heifers to milk cows, United States, July 1, 2026 = **37** percent (2026-07-01..2026-07-01) [keep: ] quote: "The ratio of replacement heifers to milk cows remained at 37 percent as of July 1, 2026, compared to a year ago."
  - p186 Dairy cow inventories, United States, July 1, 2026 = **9,650,000** head (2026-07-01..2026-07-01) [keep: ] quote: "Dairy cow inventories reached an estimated 9.650 million head, up 2.1 percent from last year"
  - p187 Milk cows, United States, June 2026 = **9,677,000** head (2026-06-01..2026-06-30) [keep: ] quote: "The number of milk cows was 9.677 million head in June, 192,000 head above June 2025."
  - p188 Milk cows, United States, June 2026 (year-over-year increase) = **192,000** head (2026-06-01..2026-06-30) [keep: ] quote: "The number of milk cows was 9.677 million head in June, 192,000 head above June 2025."
  - p189 Milk production, United States, June 2026 = **19,705,000,000** pounds (2026-06-01..2026-06-30) [keep: ] quote: "estimated milk production in the United States totaled 19.705 billion pounds (656.8 million per day) in June 2026, 2.3 percent higher than June 2025"
  - p190 Average milk production per cow, United States, June 2026 = **2,036** pounds (2026-06-01..2026-06-30) [keep: ] quote: "The average milk production per cow was 2,036 pounds in June 2026, up 6 pounds from June 2025."
  - p191 Milk cow slaughter trend, first 30 weeks of 2026 vs same period 2025 (qualitativ = **30** weeks (2026-01-01..2026-07-26) [keep: ] quote: "While culling increased during the first 30 weeks of 2026 compared with the same period in 2025, the cow slaughter rate remained relatively low compared with the past 3‐year average"
  - p192 Milk cows forecast, third quarter 2026, United States = **9,680,000** head (2026-07-01..2026-09-30) [keep: ] quote: "Milk cows (thousands) 9,543 9,564 9,498 9,622 9,666 9,680 9,685 9,665 9,690 9,695 9,695"
  - p193 Milk per cow forecast, third quarter 2026, United States = **6,105** pounds (2026-07-01..2026-09-30) [keep: ] quote: "Milk per cow (pounds) 6,100 6,044 24,391 6,091 6,227 6,105 6,055 24,480 6,110 6,250 24,550"
- `https://sat-wp.afpc.tamu.edu/2026/09/29/cull-cow-prices-continue-slide/` -> **live_dated** (page date 2026-10-19); points raw/verified 8/6
  - p194 Southern Plains cull cow price peak this past Spring = **187** USD per cow (cull cow price) (2026-03-01..2026-05-31) [keep: ] quote: "Cull cow prices in the Southern Plains peaked at $187 this past Spring but have steadily declined to about $154 at the end of September."
  - p195 Southern Plains cull cow price at end of September = **154** USD per cow (cull cow price) (2026-09-01..2026-09-30) [keep: ] quote: "Cull cow prices in the Southern Plains peaked at $187 this past Spring but have steadily declined to about $154 at the end of September."
  - p196 Decline in cow prices from Spring peak to end of September = **18** % (2026-03-01..2026-09-30) [keep: ] quote: "This 18 percent decline in cow prices is not far off the normal seasonal decline from about June to October of about 24 percent."
  - p197 Wholesale price for 90 percent lean beef 4 weeks earlier = **4.49** USD per pound (2026-09-01..2026-09-07) [keep: ] quote: "The wholesale price for 90 percent lean beef has declined from $4.49 to $4.11 per pound over the last 4 weeks as increasing supplies hit the market."
  - p198 Wholesale price for 90 percent lean beef latest = **4.11** USD per pound (2026-09-22..2026-09-29) [keep: ] quote: "The wholesale price for 90 percent lean beef has declined from $4.49 to $4.11 per pound over the last 4 weeks as increasing supplies hit the market."
  - p199 Duration over which 90 percent lean beef wholesale price declined = **4** weeks (2026-09-01..2026-09-29) [keep: ] quote: "The wholesale price for 90 percent lean beef has declined from $4.49 to $4.11 per pound over the last 4 weeks as increasing supplies hit the market."
- dropped by code checks: 8 (period_end missing or unparseable: 2; period_end 2026-12-31 after as_of: 3; scale word 'billion' not supported by quote or table header: 1; period_end 2026-10-31 after as_of: 1; period_end 2026-11-30 after as_of: 1)

### d6 [forecasts_markets] USDA forecast and market-outlook analyst

Hypothesis: USDA WASDE and dairy outlook forecasts for 2026 U.S. milk production contain supply expectations that, with a seasonal September allocation and 24-state share, constrain the target; forecasts are not observations but can indicate direction versus prior-year history.

Queries issued by the searcher: USDA WASDE 2026 milk production forecast October 2026; ERS dairy outlook 2026 milk production forecast billion pounds; NASS Milk Production report September 2025 24 major states million pounds; "September 2026" milk production 24 states million pounds USDA NASS

- `https://www.ziskapp.com/post/usda-milk-production-forecast-reverses-course-dips-lower` -> **live_dated** (page date 2026-10-13); points raw/verified 3/1
  - p200 USDA WASDE forecast for total U.S. milk production in 2025 (prior-year total, co = **231,700,000,000** pounds (2025-01-01..2025-12-31) [keep: ] quote: "At 236.9 billion pounds, the 2026 milk production estimate was lowered from last month's report, but still up 5.2 billion from 2025's total of 231.7 billion pounds."
- `https://www.ers.usda.gov/topics/animal-products/dairy/market-outlook` -> **live_dated** (page date 2026-10-19); points raw/verified 7/0
- `https://lmic.info/wp-content/lmic-files/lmic-data/memberspublic/Meetings/IOC2026/5_McConnell-Dairy%20Outlook%20Apr2026.pdf` -> **live_dated** (page date 2026-04-16); points raw/verified 15/3
  - p201 USDA WASDE/WAOB forecast U.S. milk production Q3 2026 percent change = **0.9** percent (2026-07-01..2026-09-30) [DISCARD: Duplicate of stale Q3 2026 forecast p101.] quote: "III 56.1 58.2 58.7 0.9"
  - p202 All milk price 2025 = **21.17** USD per cwt (2025-01-01..2025-12-31) [keep: ] quote: "All Milk Price (2025)- $21.17/cwt Milk per Cow (2025)- 243.91 cwt"
  - p203 Milk per cow 2025 = **244** cwt per cow (2025-01-01..2025-12-31) [keep: ] quote: "All Milk Price (2025)- $21.17/cwt Milk per Cow (2025)- 243.91 cwt"
- `https://www.agproud.com/articles/62477-milk-production-continues-to-rise-in-usda-september-estimates` -> **live_dated** (page date 2025-11-10); points raw/verified 15/15
  - p204 U.S. total milk production, September 2025 preliminary estimate = **18,990,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p36 for U.S. September 2025 production.] quote: "U.S. milk production: 18.99 billion pounds, up 4%"
  - p205 U.S. total milk production year-over-year change, September 2025 vs September 20 = **4** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of p37 for U.S. September 2025 growth.] quote: "U.S. milk production: 18.99 billion pounds, up 4%"
  - p206 24-state milk production, September 2025 preliminary estimate = **18,279,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p34 for September 2025 24-state production.] quote: "24-state milk production: 18.279 billion pounds, up 4.2%"
  - p207 24-state milk production year-over-year change, September 2025 vs September 2024 = **4.2** % (2025-09-01..2025-09-30) [DISCARD: Duplicate of September 2025 24-state growth in p34.] quote: "24-state milk production: 18.279 billion pounds, up 4.2%"
  - p208 U.S. cow numbers, September 2025 = **9,581,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of p42 for U.S. September 2025 cow inventory.] quote: "U.S. cow numbers: 9.581 million, up 228,000 head"
  - p209 U.S. cow numbers year-over-year change, September 2025 vs September 2024 = **228,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of the U.S. September 2025 cow year-over-year change in p42.] quote: "U.S. cow numbers: 9.581 million, up 228,000 head"
  - p210 U.S. average milk per cow, September 2025 = **1,982** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of p43 for U.S. September 2025 milk per cow.] quote: "U.S. average milk per cow: 1,982 pounds, up 30 pounds"
  - p211 U.S. average milk per cow year-over-year change, September 2025 vs September 202 = **30** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of the U.S. September 2025 milk-per-cow change in p43.] quote: "U.S. average milk per cow: 1,982 pounds, up 30 pounds"
  - p212 24-state cow numbers, September 2025 = **9,146,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of p38 for September 2025 24-state cow inventory.] quote: "24-state cow numbers: 9.146 million, up 235,000 head"
  - p213 24-state cow numbers year-over-year change, September 2025 vs September 2024 = **235,000** head (2025-09-01..2025-09-30) [DISCARD: Duplicate of the September 2025 24-state cow year-over-year change in p38/p3.] quote: "24-state cow numbers: 9.146 million, up 235,000 head"
  - p214 24-state average milk per cow, September 2025 = **1,999** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of p40 for September 2025 24-state milk per cow.] quote: "24-state average milk per cow: 1,999 pounds, up 30 pounds"
  - p215 24-state average milk per cow year-over-year change, September 2025 vs September = **30** pounds per cow (2025-09-01..2025-09-30) [DISCARD: Duplicate of the September 2025 24-state milk-per-cow change in p40.] quote: "24-state average milk per cow: 1,999 pounds, up 30 pounds"
  - p216 Combined milk production increase across twenty states, September 2025 vs Septem = **789,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p44 for twenty-state September 2025 production gain.] quote: "Twenty states boosted production a combined 789 million pounds; four states reduced production a combined 54 million pounds."
  - p217 Combined milk production decrease across four states, September 2025 vs Septembe = **54,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p45 for four-state September 2025 production loss.] quote: "Twenty states boosted production a combined 789 million pounds; four states reduced production a combined 54 million pounds."
  - p218 Idaho milk production year-over-year increase, September 2025 vs September 2024 = **129,000,000** pounds (2025-09-01..2025-09-30) [DISCARD: Duplicate of p46 for Idaho September 2025 volume gain.] quote: "Year-over-year growth leaders were Idaho (up 129 million pounds), Texas (up 103 million pounds) and New York (up 79 million pounds)."
- dropped by code checks: 21 (period_end 2026-12-31 after as_of: 6; period_end 2027-12-31 after as_of: 4; scale word 'billion' not supported by quote or table header: 8; scale word 'thousand' not supported by quote or table header: 3)

### d7 [shocks] Dairy risk and disruption analyst

Hypothesis: Weather, HPAI in dairy cattle, feed costs, margins, and culling can shift September 2026 milk output away from historical seasonal patterns; measurable exposure indicators should adjust cow numbers, yield per cow, or both.

Queries issued by the searcher: HPAI dairy cattle 2026 USDA APHIS detections; USDA NASS Milk Production report September 2026; September 2026 heat wave dairy cows milk production California Wisconsin yields; dairy cow slaughter September 2026 weekly slaughter up year over year culling

- `https://www.centerfordairyexcellence.org/markets-management/dairy-week-in-review/september-30-2026-dairy-week-in-review/` -> **live_dated** (page date 2026-09-30); points raw/verified 8/8
  - p219 U.S. total milk production, August 2026 = **19,900,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "the U.S. milk output totaled 19.9 billion pounds for August 2026"
  - p220 U.S. total milk production year-over-year change, August 2026 = **1.7** percent (2026-08-01..2026-08-31) [DISCARD: Duplicate of p7 for U.S. August 2026 year-over-year growth.] quote: "a 1.7 percent increase from the same month the prior year"
  - p221 National monthly average milk production per cow, August 2026 = **2,049** pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of p13 for U.S. August 2026 milk per cow.] quote: "The national monthly average milk production per cow fell one pound year over year to 2,049 pounds."
  - p222 Year-over-year change in national monthly average milk production per cow, Augus = **1** as written "one", value check pending pounds (2026-08-01..2026-08-31) [DISCARD: Duplicate of the U.S. August 2026 milk-per-cow change in p13.] quote: "The national monthly average milk production per cow fell one pound year over year to 2,049 pounds."
  - p223 U.S. milk cow numbers, August 2026 average = **9,710,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of p12 for U.S. August 2026 cow inventory.] quote: "For August 2026, the U.S. milk cow numbers averaged 9.71 million head"
  - p224 Change in U.S. milk cow numbers from August 2025 to August 2026 = **167,000** head (2026-08-01..2026-08-31) [DISCARD: Duplicate of the U.S. August 2026 cow year-over-year change in p12.] quote: "up 167,000 head from August 2025"
  - p225 Change in U.S. milk cow numbers from July 2026 to August 2026 = **15,000** head (2026-08-01..2026-08-31) [keep: ] quote: "up 15,000 from July 2026"
  - p226 U.S. milk cow numbers, July 2026 = **9,695,000** head (2026-07-01..2026-07-31) [keep: ] quote: "After the small dip in cow numbers to 9.695 million head for July"
- `http://www.farmers-exchange.net/detailPage.aspx?articleID=25564` -> **live_dated** (page date 2026-10-16); points raw/verified 15/5
  - p227 Dairy cows sent to slaughter, week ending Aug. 29, 2026 = **52,400** head (2026-08-23..2026-08-29) [keep: ] quote: "USDA's latest weekly slaughter report showed 52,400 dairy cows sent to slaughter the week ending Aug. 29, up 200 or .4%, from a year ago."
  - p228 Dairy cows sent to slaughter, week ending Aug. 29, 2026: change from year ago = **200** head (2026-08-23..2026-08-29) [DISCARD: Duplicate of the weekly slaughter year-over-year change in p227.] quote: "USDA's latest weekly slaughter report showed 52,400 dairy cows sent to slaughter the week ending Aug. 29, up 200 or .4%, from a year ago."
  - p229 Dairy cows culled year to date (as of week ending Aug. 29, 2026) = **1,810,900** head (2026-01-01..2026-08-29) [keep: ] quote: "Year to date, 1,810,900 head had been culled, up 73,300 ,or 4.2%, from a year ago."
  - p230 Dairy cows culled year to date: change from year ago = **73,300** head (2026-01-01..2026-08-29) [keep: ] quote: "Year to date, 1,810,900 head had been culled, up 73,300 ,or 4.2%, from a year ago."
  - p231 Dairy cows culled year to date: percent change from year ago = **4.2** % (2026-01-01..2026-08-29) [keep: ] quote: "Year to date, 1,810,900 head had been culled, up 73,300 ,or 4.2%, from a year ago."
- `https://en.edairynews.com/us-milk-production-expands-as-national-dairy-herd-grows/` -> **live_dated** (page date 2026-10-05); points raw/verified 15/0
- `https://www.aphis.usda.gov/news/agency-announcements/usda-confirms-highly-pathogenic-avian-influenza-two-dairy-herds` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 25 (scale word 'billion' not supported by quote or table header: 2; period_end 2026-12-31 after as_of: 4; period_end 2027-12-31 after as_of: 3; period_end missing or unparseable: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 15)

### d8 [related_series] Milk marketing order and receipts analyst

Hypothesis: Federal Milk Marketing Order pool receipts and milk marketed in major orders for September 2026 provide a partial administrative measure of milk flowing into regulated markets; scaling by the orders' share of the 24-state total can cross-check the estimate.

Queries issued by the searcher: Federal Milk Marketing Order September 2026 pool receipts milk marketed; USDA AMS FMMO monthly statistical data 2026 milk receipts by order; "Market Summary and Utilization Report" September 2026; mymarketnews AMS 3352 Market Summary Utilization Report 2026-09-01; USDA NASS Milk Production report August 2026 24 states million pounds September 2025; "September 2025" federal milk marketing order producer receipts "million pounds" all markets combined

- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/3462/2026-02-01/1312023/ams_3462_00065.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/3351/2026-01-01/1305760/ams_3351_00067.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://docs.publicnow.com/viewDoc.aspx?filename=97843%5CEXT%5C6B4AD9DA0C29CA873B8A04410C48EB2533C1AF95_AEB0C367704AA3CD016963E0389B617FC78896E7.PDF` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/3352/2026-08-01/1354287/ams_3352_00075.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-

### b1 [related_series] administrative cross-check

Hypothesis: Federal Milk Marketing Order pool receipts for September 2026 would provide an independent partial measure of milk marketed; scaling by the orders' recent share of the 24-state total could validate or shift the September 2026 level, especially if the August-to-September seasonal ratio differs from 2025.

Queries issued by the searcher: Federal Milk Marketing Order pool receipts September 2025 pounds total pooled milk; USDA NASS Milk Production report September 2025 24 major states million pounds; milk production 24 major states August 2026 USDA NASS million pounds; "milk pooled" federal orders 2026 monthly volume billion pounds AMS

- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p232 U.S. total milk production, August 2026 preliminary (USDA) = **19,900,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p233 24-state milk production, August 2026 preliminary (USDA) = **19,172,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p234 U.S. milk production year-over-year change, August 2026 vs August 2025 = **1.7** % (2026-08-01..2026-08-31) [keep: ] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p235 24-state milk production year-over-year change, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p236 U.S. cow numbers, August 2026 = **9,710,000** head (2026-08-01..2026-08-31) [keep: ] quote: "U.S. cow numbers: 9.71 million, up 167,000 head"
  - p237 24-state cow numbers, August 2026 = **9,264,000** head (2026-08-01..2026-08-31) [keep: ] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p238 U.S. average milk per cow, August 2026 = **2,049** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p239 24-state average milk per cow, August 2026 = **2,070** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p240 Combined production increase across 16 states, August 2026 vs August 2025 = **393,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p241 Combined production decrease across 7 states, August 2026 vs August 2025 = **48,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p242 Texas year-over-year milk production increase, August 2026 = **78,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p243 Kansas year-over-year milk production increase, August 2026 = **61,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p244 Wisconsin year-over-year milk production increase, August 2026 = **43,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Year-over-year growth leaders were Texas (up 78 million pounds), Kansas (up 61 million pounds) and Wisconsin (up 43 million pounds)."
  - p245 California year-over-year milk production decline, August 2026 = **24,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
  - p246 Arizona year-over-year milk production decline, August 2026 = **12,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "The states posting largest volume declines were California (down 24 million pounds) and Arizona (down 12 million pounds)."
- `https://www.nass.usda.gov/Publications/Todays_Reports/reports/mkpr1025.pdf` -> **live_dated** (page date 2025-11-07); points raw/verified 15/4
  - p247 24 major States milk production, September 2025 (million pounds) = **18,300,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p248 24 major States milk production, August 2025 revised (million pounds) = **18,800,000,000** pounds (2025-08-01..2025-08-31) [keep: ] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p249 United States milk production, July-September 2025 quarter (billion pounds) = **58,200,000,000** pounds (2025-07-01..2025-09-30) [keep: ] quote: "Milk production in the United States during the July - September quarter totaled 58.2 billion pounds, up 3.8 percent from the July - September quarter last year."
  - p250 24 major States milk cows, September 2025 (million head) = **9,150,000** head (2025-09-01..2025-09-30) [keep: ] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/3352/2025-09-01/1281333/ams_3352_00064.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://arec.tennessee.edu/extension/tennessee-market-highlights/monthly-dairy-comments/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/14
  - p251 Milk production in the 24 major states, August 2026 total = **19,200,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p252 Milk production in the 24 major states, August 2026 vs August 2025 percent chang = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "Milk production in the 24 major states during August totaled 19.2 billion pounds, up 1.8 percent from August 2025."
  - p253 Production per cow, 24 major states, August 2026 average = **2,070** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "Production per cow for August averaged 2,070 pounds."
  - p254 Number of milk cows, August 2026 = **9,260,000** head (2026-08-01..2026-08-31) [keep: ] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p255 Milk cow herd change, August 2026 vs July 2026 = **15,000** head (2026-08-01..2026-08-31) [keep: ] quote: "The number of milk cows was 9.26 million head, 15,000 more than July 2026."
  - p256 July 2026 milk production revision from preliminary estimates = **0.5** % (2026-07-01..2026-07-31) [keep: ] quote: "July production was revised down 0.5 percent from preliminary estimates."
  - p257 Southeast Federal Order Class I utilization, August 2026 = **72.16** % (2026-08-01..2026-08-31) [keep: ] quote: "Southeast Class I utilization was 72.16%, down 1.18% from July and 4.38% lower than August a year ago."
  - p258 Appalachian Federal Order Class I utilization, August 2026 = **73.75** % (2026-08-01..2026-08-31) [keep: ] quote: "Appalachian Class I utilization was 73.75%, up 0.60% from July, and 0.68% higher than August a year ago."
  - p259 Southeast Uniform milk price, August 2026 = **22.93** USD per cwt (2026-08-01..2026-08-31) [keep: ] quote: "The Southeast Uniform milk price for August was $22.93, down $2.57 from July and $0.62 lower than August 2025."
  - p260 Appalachian Uniform milk price, August 2026 = **22.71** USD per cwt (2026-08-01..2026-08-31) [keep: ] quote: "The Appalachian Uniform milk price was $22.71 down $2.69 from July and $0.31 lower than August 2025."
  - p261 Class III milk price, August 2026 = **16.64** USD per cwt (2026-08-01..2026-08-31) [keep: ] quote: "August's Class III price was $16.64, up $1.12 from July, and $0.60 lower than August a year ago."
  - p262 Class IV milk price, August 2026 = **17.36** USD per cwt (2026-08-01..2026-08-31) [keep: ] quote: "The Class IV price was down $0.98 at $17.36, and $1.14 lower than August 2025."
  - p263 Dairy cow slaughter, August 2026 = **221,100** head (2026-08-01..2026-08-31) [keep: ] quote: "Dairy cow slaughter in August was 221,100 head, down 6,500 head from July and 3,700 head more than August 2025."
  - p264 Southeast Federal Order Class I utilization, July 2026 = **73.34** percent (2026-07-01..2026-07-31) [keep: ] quote: "\| Jul 26 \| 25.50 \| 27.13 \| 15.52 \| 18.34 \| 73.34 \| 1.7132 \|"
- dropped by code checks: 12 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 11; period_end 2026-10-31 after as_of: 1)

### b2 [administrative] herd-change indicator

Hypothesis: Weekly September 2026 dairy cow slaughter and culling rates would show whether the September 2026 herd change around August matched the 2025 September increase used in the physical formula, reducing uncertainty in the cow-inventory component.

Queries issued by the searcher: USDA AMS weekly dairy cow slaughter September 2026; dairy cow slaughter weekly report 2025 culling rate monthly; "August report on dairy cows culled for beef" 2026; USDA NASS Milk Production report September 2026 24 major states million pounds

- `https://mymarketnews.ams.usda.gov/filerepo/sites/default/files/3658/2026-09-06/1353626/ams_3658_00200.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.agproud.com/articles/keyword/1709-cull-cows` -> **live_dated** (page date 2026-09-24); points raw/verified 9/8
  - p265 US dairy cull cows marketed through slaughter plants, August 2026 (estimated) = **221,100** dairy cull cows (2026-08-01..2026-08-31) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in August 2026 was estimated at 221,100."
  - p266 US dairy cull cows marketed through slaughter plants, July 2026 (estimated) = **227,600** dairy cull cows (2026-07-01..2026-07-31) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in July 2026 was estimated at 227,600."
  - p267 US dairy cull cows marketed through slaughter plants, June 2026 (estimated) = **208,100** dairy cull cows (2026-06-01..2026-06-30) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in June 2026 was estimated at 208,100."
  - p268 US dairy cull cows marketed through slaughter plants, May 2026 (estimated) = **191,700** dairy cull cows (2026-05-01..2026-05-31) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in May 2026 was estimated at 191,700."
  - p269 US dairy cull cows marketed through slaughter plants, April 2026 (estimated) = **215,100** dairy cull cows (2026-04-01..2026-04-30) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in April 2026 was estimated at 215,100."
  - p270 US dairy cull cows marketed through slaughter plants, March 2026 (estimated) = **239,200** dairy cull cows (2026-03-01..2026-03-31) [keep: ] quote: "the number of dairy cull cows marketed through U.S. slaughter plants in March 2026 was estimated at 239,200."
  - p271 Quarterly average price for US replacement dairy cows, July (USDA estimate) = **3,260** USD per head (2026-07-01..2026-07-31) [keep: ] quote: "Quarterly average prices in July increased to $3,260 per head according to estimates from the USDA."
  - p272 Quarterly average price for US replacement dairy cows, April (USDA estimate) = **3,130** USD per head (2026-04-01..2026-04-30) [keep: ] quote: "Quarterly average prices in April increased to $3,130 per head according to estimates from the USDA."
- `https://southernagtoday.org/2026/09/29/cull-cow-prices-continue-slide/` -> **live_dated** (page date 2026-09-29); points raw/verified 8/6
  - p273 Southern Plains cull cow price peak this past Spring = **187** USD per hundredweight (cull cow price) (2026-03-01..2026-05-31) [keep: ] quote: "Cull cow prices in the Southern Plains peaked at $187 this past Spring"
  - p274 Southern Plains cull cow price at end of September = **154** USD per hundredweight (cull cow price) (2026-09-01..2026-09-30) [keep: ] quote: "have steadily declined to about $154 at the end of September"
  - p275 Decline in cow prices from Spring peak to end of September = **18** % (2026-03-01..2026-09-30) [keep: ] quote: "This 18 percent decline in cow prices is not far off the normal seasonal decline"
  - p276 Wholesale price for 90 percent lean beef 4 weeks ago = **4.49** USD per pound (2026-09-01..2026-09-07) [keep: ] quote: "The wholesale price for 90 percent lean beef has declined from $4.49 to $4.11 per pound over the last 4 weeks"
  - p277 Wholesale price for 90 percent lean beef latest = **4.11** USD per pound (2026-09-22..2026-09-29) [keep: ] quote: "declined from $4.49 to $4.11 per pound over the last 4 weeks"
  - p278 Duration of wholesale 90 percent lean beef price decline = **4** weeks (2026-09-01..2026-09-29) [keep: ] quote: "over the last 4 weeks as increasing supplies hit the market"
- `https://hoards.com/print-article-38465-permanent.html` -> **live_dated** (page date 2024-11-01); points raw/verified 10/2
  - p279 Additional dairy cull cows sent to packer year-to-date through July (year-over-y = **70,200** head (2026-01-01..2026-07-31) [keep: ] quote: "dairy farmers have sent 70,200 more cull cows to the packer year-to-date through July"
  - p280 Average additional dairy cull cows per week over last year (year-to-date through = **2,300** head per week (2026-01-01..2026-07-31) [keep: ] quote: "averaging 2,300 additional head per week over last year"
- dropped by code checks: 11 (period_end missing or unparseable: 9; period_end 2026-10-31 after as_of: 1; period_end 2026-11-30 after as_of: 1)

### b3 [shocks] yield-risk indicator

Hypothesis: September 2026 heat stress, HPAI dairy cases, or feed-cost shocks could make September yield deviate from the 2025 September/August seasonal ratio; measurable exposure would adjust the physical cow×yield route.

Queries issued by the searcher: USDA NASS Milk Production report September 2026 24 major states million pounds; HPAI dairy cattle cases 2026 USDA confirmed herds; "Milk production in the 24 major States during September" 2025 totaled billion pounds NASS; September 2026 heat wave dairy cows milk yield decline western states

- `https://www.nass.usda.gov/Publications/Todays_Reports/reports/mkpr1025.pdf` -> **live_dated** (page date 2025-11-07); points raw/verified 15/6
  - p281 Milk production, 24 major States, September 2025 (total) = **18,300,000,000** pounds (2025-09-01..2025-09-30) [keep: ] quote: "Milk production in the 24 major States during September totaled 18.3 billion pounds, up 4.2 percent from September 2024."
  - p282 Milk production, 24 major States, August 2025 (revised total) = **18,800,000,000** pounds (2025-08-01..2025-08-31) [keep: ] quote: "August revised production, at 18.8 billion pounds, was up 3.6 percent from August 2024."
  - p283 Milk production per cow, 24 major States, September 2025 (average) = **1,999** pounds per cow (2025-09-01..2025-09-30) [keep: ] quote: "Production per cow in the 24 major States averaged 1,999 pounds for September, 30 pounds above September 2024."
  - p284 Milk cows on farms, 24 major States, September 2025 (count) = **9,150,000** head (2025-09-01..2025-09-30) [keep: ] quote: "The number of milk cows on farms in the 24 major States was 9.15 million head, 235,000 head more than September 2024, and 38,000 head more than August 2025."
  - p285 Milk production, United States, July-September 2025 quarter (total) = **58,200,000,000** pounds (2025-07-01..2025-09-30) [keep: ] quote: "Milk production in the United States during the July - September quarter totaled 58.2 billion pounds, up 3.8 percent from the July - September quarter last year."
  - p286 Average milk cows, United States, July-September 2025 quarter = **9,540,000** head (2025-07-01..2025-09-30) [keep: ] quote: "The average number of milk cows in the United States during the quarter was 9.54 million head, 82,000 head more than the April - June quarter, and 199,000 head more than the same period last year."
- `https://www.agproud.com/articles/64184-dairy-cow-numbers-milk-production-edge-higher-in-august` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p287 U.S. total milk production, August 2026 preliminary estimate = **19,900,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "U.S. milk production: 19.9 billion pounds, up 1.7%"
  - p288 24-state milk production, August 2026 preliminary estimate = **19,172,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p289 24-state cow numbers, August 2026 = **9,264,000** head (2026-08-01..2026-08-31) [keep: ] quote: "24-state cow numbers: 9.264 million, up 151,000 head"
  - p290 24-state average milk per cow, August 2026 = **2,070** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p291 U.S. average milk per cow, August 2026 = **2,049** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p292 U.S. cow numbers, August 2026 = **9,710,000** head (2026-08-01..2026-08-31) [keep: ] quote: "U.S. cow numbers: 9.71 million, up 167,000 head"
  - p293 Year-over-year change in U.S. milk production, August 2026 vs August 2025 = **1.7** % (2026-08-01..2026-08-31) [keep: ] quote: "U.S. milk production rose about 1.7% compared to the same month last year"
  - p294 Year-over-year change in 24-state milk production, August 2026 vs August 2025 = **1.8** % (2026-08-01..2026-08-31) [keep: ] quote: "24-state milk production: 19.172 billion pounds, up 1.8%"
  - p295 Year-over-year change in 24-state average milk per cow, August 2026 vs August 20 = **4** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "24-state average milk per cow: 2,070 pounds, up 4 pounds"
  - p296 Year-over-year change in U.S. average milk per cow, August 2026 vs August 2025 = **1** pounds per cow (2026-08-01..2026-08-31) [keep: ] quote: "U.S. average milk per cow: 2,049 pounds, down 1 pound"
  - p297 Combined year-over-year milk production increase across 16 states, August 2026 = **393,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p298 Combined year-over-year milk production decrease across 7 states, August 2026 = **48,000,000** pounds (2026-08-01..2026-08-31) [keep: ] quote: "Sixteen states boosted production a combined 393 million pounds; seven states reduced production a combined 48 million pounds."
  - p299 Georgia year-over-year change in milk output per cow, August 2026 vs August 2025 = **65** pounds per cow per month (2026-08-01..2026-08-31) [keep: ] quote: "Georgia showed per-cow output increased 65 pounds per month compared to the same month a year ago"
  - p300 Kansas year-over-year milk production growth rate, August 2026 vs August 2025 = **13.93** % (2026-08-01..2026-08-31) [keep: ] quote: "Kansas was the milk percentage growth leader for August 2026, up 13.93% from August 2025"
  - p301 Arizona year-over-year milk production decline rate, August 2026 vs August 2025 = **3.14** % (2026-08-01..2026-08-31) [keep: ] quote: "August 2026 production was down 3.57% from a year earlier in Utah and 3.14% in Arizona."
- `https://www.efeedlink.com/articles/washington-us-confirms-first-h5n1-bird-flu-cases-in-dairy-cattle` -> **live_dated** (page date 2026-10-19); points raw/verified 3/1
  - p302 Start month of US HPAI-in-dairy-cattle state count = **2,024** year (2024-03-01..2024-03-31) [keep: ] quote: "since March 2024"
- `https://www.aphis.usda.gov/news/agency-announcements/usda-confirms-highly-pathogenic-avian-influenza-two-dairy-herds` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 11 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 9; period_end missing or unparseable: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['milk production', 'usda milk report', 'september milk']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p34', 'p1', 'p49', 'p83', 'p140', 'p206'] All report the same NASS first-reported September 2025 24-state production total around 18.3 billion pounds, up 4.2% from September 2024. p34 gives the more precise first-reported figure; the others a
- corroborating: ['p2', 'p52', 'p84', 'p142'] Same August 2025 revised 24-state production figure, about 18.8 billion pounds. p2/p52 are rounded to 0.1 billion pounds, so they are less precise than the September 2025 and August 2026 three-decimal
- corroborating: ['p4', 'p19', 'p54', 'p69', 'p87', 'p110', 'p124'] Same August 2026 preliminary 24-state production figure, about 19.17–19.2 billion pounds, up 1.8% year over year. p4 gives the precise first-reported 19.172 billion value.
- corroborating: ['p5', 'p20', 'p64', 'p73', 'p89', 'p111', 'p125'] All state the August 2026 24-state year-over-year production growth as 1.8%, from the same NASS August 2026 report.
- corroborating: ['p38', 'p3', 'p51', 'p148', 'p212'] Same September 2025 24-state milk cow inventory around 9.15 million head. p38 gives 9.146 million head; p3/p51 round to 9.15 million and note the 38,000-head increase over August.
- corroborating: ['p40', 'p50', 'p146', 'p214'] Same September 2025 24-state milk per cow, 1,999 pounds, up 30 pounds from September 2024.
- corroborating: ['p8', 'p22', 'p55', 'p71', 'p91', 'p113', 'p131'] Same August 2026 24-state cow inventory, about 9.26 million head, up 15,000 from July and 151,000 from August 2025. p8 gives 9.264 million.
- corroborating: ['p10', 'p21', 'p56', 'p70', 'p93', 'p114', 'p130'] Same August 2026 24-state milk per cow, 2,070 pounds, up 4 pounds year over year.
- corroborating: ['p11', 'p60'] Both state the August 2026 24-state milk-per-cow year-over-year gain as 4 pounds.
- corroborating: ['p14', 'p15', 'p68', 'p94', 'p95', 'p123'] August 2026 state detail: sixteen states added a combined 393 million pounds and seven states lost a combined 48 million pounds, consistent with the 24-state total being up about 1.8% year over year.
- corroborating: ['p16', 'p17', 'p18', 'p96', 'p97', 'p99', 'p116', 'p117', 'p119'] State-level August 2026 growth/decline leaders: Texas, Kansas, and Wisconsin up sharply; California and Arizona down. This is consistent with the 24-state aggregate growth pattern.
- corroborating: ['p25', 'p26', 'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p78', 'p79', 'p80', 'p81', 'p82'] State-level August 2026 year-over-year percentage changes are consistent with the reported state volume changes: Kansas and South Dakota strong, Texas/Wisconsin/Idaho/New York positive, Arizona/Utah n
- corroborating: ['p6', 'p57', 'p86', 'p109', 'p128', 'p219'] Same U.S. total August 2026 milk production figure, about 19.9 billion pounds. This is a broader population than the 24-state target.
- corroborating: ['p7', 'p65', 'p88', 'p112', 'p129', 'p220'] Same U.S. August 2026 year-over-year milk production growth, about 1.7%, slightly below the 24-state growth of 1.8%.
- corroborating: ['p12', 'p58', 'p90', 'p223'] Same U.S. August 2026 cow inventory, about 9.71 million head, up 167,000 from August 2025.
- corroborating: ['p13', 'p59', 'p92', 'p115', 'p221'] Same U.S. August 2026 milk per cow, 2,049 pounds, down 1 pound year over year.
- corroborating: ['p36', 'p204', 'p155'] Same U.S. September 2025 total milk production, about 18.99 billion pounds, up 4.0% year over year.
- corroborating: ['p37', 'p205'] Same U.S. September 2025 year-over-year milk production growth, 4.0%.
- corroborating: ['p42', 'p208'] Same U.S. September 2025 cow inventory, 9.581 million head, up 228,000 from September 2024.
- corroborating: ['p43', 'p210'] Same U.S. September 2025 milk per cow, 1,982 pounds, up 30 pounds year over year.
- corroborating: ['p44', 'p45', 'p216', 'p217'] September 2025 state detail: twenty states added 789 million pounds and four states lost 54 million, consistent with the 4.2% 24-state growth.
- corroborating: ['p46', 'p47', 'p48', 'p218'] September 2025 growth leaders: Idaho, Texas, and New York, consistent with the 24-state September 2025 growth pattern.
- corroborating: ['p75', 'p76', 'p77'] August 2026 dairy cow slaughter was 221,100 head, down from July but above August 2025. This is an administrative trace on herd change, not a direct production measure.
- corroborating: ['p170', 'p171', 'p172', 'p175', 'p176', 'p179', 'p180', 'p181'] July 2026 culling data show slaughter slightly above year-ago levels and a culling rate near 2.3% of the herd. This is consistent with continued herd expansion but slower culling pressure.
- corroborating: ['p227', 'p229', 'p230', 'p231'] Weekly and year-to-date culling through late August 2026 shows slaughter above 2025 but not at extreme levels. This supports a modestly expanding herd.
- corroborating: ['p183', 'p184', 'p185', 'p186'] July 1, 2026 replacement heifers and dairy cow inventories point to herd stability/expansion rather than rapid contraction.
- corroborating: ['p105', 'p200'] Both use a 2025 U.S. milk production total of 231.7 billion pounds; p200 is the October 2026 WASDE 2026 forecast of 236.9 billion pounds, implying annual growth. This is a forecast, not a September mo
- corroborating: ['p101', 'p201'] Both reflect an earlier USDA/LMIC Q3 2026 U.S. milk production projection of about 0.9% year-over-year growth. The later August 2026 actual growth of 1.7–1.8% suggests this forecast is stale.
- conflicting: ['p42', 'p156'] p42/p208 report U.S. September 2025 cows up 228,000 year over year; p156 reports the same 9.581 million level but up 238,000. The 10,000-head difference is likely a typo or revision, and p42/p208 are 
- conflicting: ['p13', 'p63'] p13 and related U.S. yield points say August 2026 U.S. milk per cow was down 1 pound year over year. p63 lists a positive value of 1 with a name that could imply an increase, despite a quote saying do
- needs-conversion: ['p2', 'p4', 'p5'] p4 and p5 together imply an August 2025 base, but p2 is rounded to 0.1 billion pounds. For growth-rate transfer, the reported 1.8% in p5 is more direct and less affected by rounding than p4/p2.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 18,635,218,721 | ['p34', 'p5'] / [] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 18,664,705,813 | ['p8', 'p10', 'p40', 'p11', 'p38', 'p150'] / [] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 18,297,574,049 | ['p34', 'p200', 'p105'] / [] | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target

Result: central **18,531,747,988** lb, 80% interval [13,451,592,188, 25,530,485,812] lb, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['ytd']; measure stems ['major', 'milk', 'milli', 'pound', 'produ']; 2 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

The best computed estimate for total milk production in USDA NASS's [n] major States during September 2026 is 18,531,747,988 lb (80% model-based interval 13,451,592,188 to 25,530,485,812 lb). This is a completed-month flow, not annual or year-to-date production, and the first-reported value before revisions.

Three routes were averaged with equal weights (3 methods): transferring August 2026 year-over-year growth (1.8%) to the September 2025 level (18,279,000,000 pounds); scaling August 2026 cow×yield (9,264,000 head, 2,070 pounds per cow) by 2025 September/August seasonal ratios (1,999 pounds per cow, 9,146,000 head, 38,000 head); and applying WASDE-implied annual growth (231,700,000,000 pounds, 231,700,000,000 pounds) to the prior September. The first two are transfers of observed relationships; the third is forecast-based. The weighting reflects code's fixed equal scheme, not demonstrated backtest accuracy.

The main risk is that September 2026 herd culling, heat stress, or yield seasonality diverged from the transferred patterns. Better evidence would be September 2026 state-level cow and yield data or an early NASS signal.

Key assumptions: none (every formula input is an observed data point).

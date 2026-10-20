# Evidence ledger: fc_nhs_ae_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the total number of A&E attendances in England in September 2026 (all A&E types, including minor injury units and walk-in centres), as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics.
- as_of: 2026-09-08
- Pinned target: Total A&E attendances (all reported A&E department types, including minor injury units and walk-in centres where reported) in England during calendar September 2026, as would be reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics. The count is attendances/visits, no | unit attendance (A&E visit) | period 2026-09-01..2026-09-30 | publisher NHS England

- Official value (scoring only, never shown to the agent): 2,440,000

## Directions and pages

### d1 [own_history] NHS England monthly national A&E return

Hypothesis: September 2026 total attendances should be close to the September 2025 total scaled by recent year-on-year growth, with a possible calendar adjustment; the historical September values and latest 2026 year-to-date values provide the baseline and trend.

Queries issued by the searcher: NHS England A&E attendances September 2025 all types monthly statistics; A&E Attendances and Emergency Admissions monthly statistics 2026 NHS England; NHS England A&E attendances July 2026 statistical commentary all types total attendance; "A&E" attendances England 2026 "2.4" million July busiest month record NHS England

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] NHS England provider returns by A&E department type

Hypothesis: Total attendances equal the sum of attendances across reported department types; type-level September shares and 2026 year-on-year changes can project the September 2026 total and reveal whether growth is concentrated in Type 1 or in MIU/WIC/other settings.

Queries issued by the searcher: NHS England A&E attendances by type 1 type 2 type 3 September 2025; A&E attendances department type England monthly 2026 NHS England statistics; A&E attendances and emergency admissions for July 2026 NHS England statistical commentary; "A&E" attendances "type 1" "type 2" "type 3" monthly time series England 2026 table

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [base_rates] Population-level attendance incidence

Hypothesis: Annual A&E attendances per person multiplied by England population and by the historical September share of annual attendances gives an independent check on the September 2026 level, assuming incidence and seasonality remain broadly stable.

Queries issued by the searcher: NHS England annual A&E attendances 2024 total all types; ONS England population mid-2025; NHS England A&E attendances September seasonal monthly 2024 2025; NHS England A&E attendances September 2025 million monthly; NHS England A&E attendances 2025 calendar year total 28 million; "September 2024" "A&E attendances" 2.21 million England 2024 annual 27.42; England population mid-2025 57.7 million ONS table

- `https://www.england.nhs.uk/2025/01/busiest-year-on-record-for-emergency-services-as-winter-flu-pressure-rages-on/` -> **snapshot** (snapshot 20260514064854) **LEAK SENTINEL HIT ['(?<![\\d.,])2\\.44\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2024` -> **snapshot** (snapshot 20260820115551); points raw/verified 15/15
  - p1 UK total population estimate, mid-2024 = **69,300,000** people (2024-07-01..2024-07-01) [DISCARD: UK rounded population total, not England; p2 is an exact duplicate with the same scope, and neither supplies an England ] quote: "reaching an estimated 69.3 million people (69,281,400)"
  - p2 UK total population estimate, mid-2024 (exact) = **69,281,400** people (2024-07-01..2024-07-01) [DISCARD: UK exact population total, not England; no England population level is available to combine with England growth rates.] quote: "reaching an estimated 69.3 million people (69,281,400)"
  - p3 England population growth rate, year to mid-2024 = **1.2** % (2023-07-01..2024-07-01) [keep: ] quote: "The population grew faster in England (1.2%) than in Scotland (0.7%), Wales (0.6%) or Northern Ireland (0.4%)."
  - p4 UK population increase, year to mid-2024 = **755,300** people (2023-07-01..2024-07-01) [DISCARD: UK population increase, not an England A&E count or England denominator.] quote: "The size of the population increased by 755,300 (1.1%) from mid-2023."
  - p5 UK population growth rate, year to mid-2024 = **1.1** % (2023-07-01..2024-07-01) [DISCARD: UK population growth rate, not England A&E attendance and no direct conversion.] quote: "The size of the population increased by 755,300 (1.1%) from mid-2023."
  - p6 England rate of population change from net international migration, year to mid- = **1.2** % (2023-07-01..2024-07-01) [DISCARD: England net international migration rate, not attendance and no direct conversion.] quote: "The rate of population change from net international migration was highest for England (1.2%) and lowest for Northern Ireland (0.3%)"
  - p7 UK immigration, year to mid-2024 = **1,235,300** people (2023-07-01..2024-07-01) [DISCARD: UK immigration, not England A&E attendance and no direct conversion.] quote: "1,235,300 people arrived in the UK to live for 12 months or more"
  - p8 UK emigration, year to mid-2024 = **496,500** people (2023-07-01..2024-07-01) [DISCARD: UK emigration, not England A&E attendance and no direct conversion.] quote: "496,500 people left the UK for at least 12 months"
  - p9 UK net international migration, year to mid-2024 = **738,700** people (2023-07-01..2024-07-01) [DISCARD: UK net migration, not England A&E attendance and no direct conversion.] quote: "net international migration to the UK was 738,700"
  - p10 UK births, year to mid-2024 = **662,100** births (2023-07-01..2024-07-01) [DISCARD: UK births, not attendance and no direct conversion.] quote: "there were 662,100 births, a decrease of 2,300 compared with mid-2023"
  - p11 UK deaths, year to mid-2024 = **645,900** deaths (2023-07-01..2024-07-01) [DISCARD: UK deaths, not attendance and no direct conversion.] quote: "there were 645,900 deaths, a decrease of 34,800 compared with mid-2023"
  - p12 UK natural change (births minus deaths), year to mid-2024 = **16,200** people (2023-07-01..2024-07-01) [DISCARD: UK natural change, not attendance and no direct conversion.] quote: "natural change, the difference between births and deaths, contributed an increase in the population of 16,200"
  - p13 England median age, mid-2024 = **40.2** years (2024-07-01..2024-07-01) [DISCARD: England median age, not an attendance count and no age-specific attendance rate is supplied.] quote: "40.2 years in England"
  - p14 England population aged 65 years and over increase, year to mid-2024 = **1.8** % (2023-07-01..2024-07-01) [keep: ] quote: "1.8% in England"
  - p15 England population aged 15 years and under increase, year to mid-2024 = **0.6** % (2023-07-01..2024-07-01) [keep: ] quote: "The number of people aged 15 years and under increased in England by 0.6%"
- `https://www.myhsn.co.uk/top-tip/nhs-winter-pressure-is-a-myth-what-the-data-really-shows/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/hospital-accident--emergency-activity/2024-25` -> **snapshot** (snapshot 20251006051044); points raw/verified 4/4
  - p16 England total A&E attendances, all A&E types including UTCs, MIUs and walk-in ce = **27,400,000** attendance (A&E visit) (2024-04-01..2025-03-31) [keep: ] quote: "In 2024-25 there were 27.4 million attendances in Accident and Emergency (Source: MSitAE)"
  - p17 Share of patient attendances spending 4 hours or less in A&E, England, 2024-25 ( = **73.9** % (2024-04-01..2025-03-31) [DISCARD: Annual within-4-hours share is a performance measure, not an attendance count; no September 2026 conversion.] quote: "For 2024-25, 73.9 per cent of patient attendances spent 4 hours or less in A&E (Source: MSitAE)."
  - p18 Ratio of A&E attendance rate per head in most deprived areas to least deprived a = **1.9** ratio of attendances per head (2024-04-01..2025-03-31) [DISCARD: Deprivation ratio of attendance rates is contextual, not a total attendance level.] quote: "the rates of A&E attendances per head of population for people living in the most deprived areas was 1.9 times that of those in the least deprived (Source: ECDS)."
  - p19 Share of all A&E attendances accounted for by patients aged under 35 years, Engl = **45.2** % (2024-04-01..2025-03-31) [DISCARD: Under-35 share of attendances is a composition measure, not a total count.] quote: "In 2024-25 patients aged under 35 years of age accounted for 45.2 per cent of all attendances (Source: ECDS)."

### d4 [related_series] Emergency admissions arising from A&E

Hypothesis: Total attendances can be estimated from emergency admissions divided by the admission conversion rate, where the conversion rate is emergency admissions per A&E attendance; this provides an independent constraint if the conversion rate is stable around September.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions September 2025 statistics; NHS England A&E attendances and emergency admissions July 2026; A&E attendance emergency admission conversion rate England; "July 2026" NHS England A&E attendances "emergency admissions" 2026 statistical commentary; NHS England A&E Attendances and Emergency Admissions August 2026 publication

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.rcp.ac.uk/news-and-media/news-and-opinion/new-government-faces-early-test-as-first-nhs-performance-figures-are-published/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [own_history] Daily or weekly urgent-care operational returns

Hypothesis: A monthly total is the sum of daily attendances; early September 2026 daily or weekly partial data, combined with the September 2025 day-of-week profile, can anchor the monthly projection and adjust for weekday composition.

Queries issued by the searcher: NHS England daily A&E attendances sitrep September 2026; weekly A&E attendances England September 2025 day of week; NHS England weekly A&E attendances September 2025 publication; "daily situation report" urgent and emergency care NHS England A&E attendances weekly 2026

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/publications/emergency-department-weekly-bulletins-for-2025` -> **snapshot** (snapshot 20260813044017); points raw/verified 0/0
- `https://shepwayvox.org/wp-content/uploads/2025/10/CBP-7281.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/statistical-work-areas/uec-sitrep/urgent-and-emergency-care-daily-situation-reports-2025-26/` -> **snapshot** (snapshot 20260617071808); points raw/verified 0/0

### d6 [capacity_consumption] A&E units and throughput capacity

Hypothesis: Total attendances equal reporting units multiplied by average daily attendances per unit and by 30 days; unit counts and average throughput provide a capacity-based constraint, though heterogeneity across major A&E departments and MIU/WIC settings limits precision.

Queries issued by the searcher: number of A&E departments England 2025 type 1 major A&E units count NHS England; NHS England A&E attendances and emergency admissions monthly statistics average daily attendances per type 1 department; "A&E Attendances and Emergency Admissions" 2026 statistical commentary "type 1" attendances reporting trusts; how many type 1 A&E departments England 2025 "122" OR "123" OR "125" reporting trusts

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **snapshot** (snapshot 20260515081905); points raw/verified 15/15
  - p20 Total A&E attendances in England, April 2026 (all types) = **2,345,329** attendance (A&E visit) (2026-04-01..2026-04-30) [keep: ] quote: "The total number of attendances in April 2026 was 2,345,329."
  - p21 Total A&E attendances year-on-year growth, April 2026 vs April 2025 = **2.1** % (2026-04-01..2026-04-30) [keep: ] quote: "This was 2.1% higher when compared with April 2025."
  - p22 Type 1 A&E attendances year-on-year growth, April 2026 vs April 2025 = **3** % (2026-04-01..2026-04-30) [keep: ] quote: "Attendances at Type 1 A&E departments were 3.0% higher compared with April 2025."
  - p23 Type 3 A&E attendances year-on-year growth, April 2026 vs April 2025 = **0.3** % (2026-04-01..2026-04-30) [keep: ] quote: "Attendances at Type 3 departments were 0.3% higher compared with April 2025."
  - p24 Type 1 A&E attendances 12-month growth, latest 12 months vs preceding 12 months = **2.3** % (2025-05-01..2026-04-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for Type 1 was 2.3% and for Type 3 was 1.9%."
  - p25 Type 3 A&E attendances 12-month growth, latest 12 months vs preceding 12 months = **1.9** % (2025-05-01..2026-04-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for Type 1 was 2.3% and for Type 3 was 1.9%."
  - p26 Booked A&E attendances, April 2026 = **73,777** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: Booked A&E count is duplicated in richer form by p65, which also gives the year-on-year change.] quote: "Last month there were 73,777 A&E attendances that had been booked."
  - p27 Emergency admissions in England, April 2026 = **525,660** emergency admission (2026-04-01..2026-04-30) [DISCARD: April 2026 emergency admissions count is duplicated in richer form by p66, which also gives the year-on-year change.] quote: "There were 525,660 emergency admissions in April 2026."
  - p28 All A&E attendances admitted/transferred/discharged within 4 hours, April 2026 = **1,803,787** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: April 2026 all-type within-4-hours count is duplicated in richer form by p67.] quote: "The number of attendances admitted, transferred or discharged within 4 hours was 1,803,787."
  - p29 Type 1 attendances within 4 hours, April 2026 = **913,227** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: April 2026 Type 1 within-4-hours count is duplicated in richer form by p68.] quote: "Of these, 913,227 were Type 1 attendances; 9.2% higher than in April 2025."
  - p30 Type 3 attendances within 4 hours, April 2026 = **840,154** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: April 2026 Type 3 within-4-hours count is duplicated in richer form by p69.] quote: "There were 840,154 Type 3 attendances. This was 0.7% higher than in April 2025."
  - p31 Share of all A&E attendances within 4 hours, April 2026 = **76.9** % (2026-04-01..2026-04-30) [DISCARD: April 2026 all-type within-4-hours share is duplicated in richer form by p70.] quote: "76.9% of patients were admitted, transferred or discharged within 4 hours in all A&E Departments in April 2026"
  - p32 Share of Type 1 attendances within 4 hours, April 2026 = **63.8** % (2026-04-01..2026-04-30) [keep: ] quote: "63.8% of patients were admitted, transferred or discharged within 4 hours in Type 1 A&E Departments in April 2026"
  - p33 Share of Type 3 attendances within 4 hours, April 2026 = **97.5** % (2026-04-01..2026-04-30) [keep: ] quote: "97.5% of patients were admitted, transferred or discharged within 4 hours in Type 3 A&E departments"
  - p34 Reporting trusts with Type 1 departments, April 2026 = **121** reporting trusts with Type 1 departments (2026-04-01..2026-04-30) [DISCARD: Trust count with Type 1 departments alone lacks average throughput and cannot give attendances.] quote: "0 out of 121 reporting trusts with Type 1 departments achieved the 95% standard on all types during the month."
- `https://commonslibrary.parliament.uk/research-briefings/cbp-7281/` -> **snapshot** (snapshot 20260823123218); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://arjus.co.uk/ae_dashboard.php` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [physical_flow] Ambulance conveyances and NHS 111 referrals

Hypothesis: A&E attendances equal ambulance conveyances divided by the share of attendances arriving by ambulance, with self-presentations making up the remainder; ambulance and 111 flow data can constrain the level if the arrival-mode share is stable.

Queries issued by the searcher: NHS England ambulance conveyances to A&E September 2025 monthly statistics; proportion of A&E attendances arrived by ambulance England percentage; "A&E attendances" September 2025 England monthly NHS England 2.2 million statistics; NHS England ambulance quality indicators "conveyances" September 2025 "category 2" number of patients conveyed

- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gettingitrightfirsttime.co.uk/wp-content/uploads/2022/07/Emergency-Medicine-Apr22q-FINAL.pdf` -> **snapshot** (snapshot 20251226021516); points raw/verified 14/8
  - p35 England average ambulance conveyance rate (proportion of ambulance calls resulti = **57** % (2020-01-01..2020-12-31) [keep: ] quote: "England average 57.0%"
  - p36 Mean proportion of ED patients who arrive by ambulance (ECDS, Type 1 EDs) = **31** % (2019-04-01..2020-03-31) [keep: ] quote: "31% 27% 36% 16% to 54% Mean Lower quartile Upper quartile Range"
  - p37 Lower quartile proportion of ED patients who arrive by ambulance (ECDS, Type 1 E = **27** % (2019-04-01..2020-03-31) [keep: ] quote: "31% 27% 36% 16% to 54% Mean Lower quartile Upper quartile Range"
  - p38 Upper quartile proportion of ED patients who arrive by ambulance (ECDS, Type 1 E = **36** % (2019-04-01..2020-03-31) [keep: ] quote: "31% 27% 36% 16% to 54% Mean Lower quartile Upper quartile Range"
  - p39 NHS 111 calls in England (February 2019) = **1,400,000** calls (2019-02-01..2019-02-28) [DISCARD: 2019 NHS 111 call volume, not 2026 and not an A&E attendance count.] quote: "There were 1.4 million calls to the NHS 111 service in England in February 2019."
  - p40 Share of NHS 111 callers recommended to attend local ED (February 2019) = **8.7** % (2019-02-01..2019-02-28) [DISCARD: 2019 NHS 111 referral share, not A&E attendance and no current 111 volume.] quote: "Of these patients, 8.7% were recommended to attend their local ED."
  - p41 Share of NHS 111 callers referred to the ambulance service (February 2019) = **13.4** % (2019-02-01..2019-02-28) [DISCARD: 2019 NHS 111 ambulance referral share, not A&E attendance and no current 111 volume.] quote: "A further 13.4% of patients were referred to the ambulance service, who then conveyed the majority to an ED."
  - p42 Share of NHS 111 callers effectively referred to an ED (February 2019) = **22.1** % (2019-02-01..2019-02-28) [DISCARD: 2019 NHS 111 effective ED referral share, not an attendance count and no current 111 volume.] quote: "This means that nearly 22.1% of patients who called NHS 111 were effectively referred to an ED."
- `https://www.clinicalservicesjournal.com/story/49617/frustrating-rise-in-waiting-lists-despite-nhs-managing-record-elective-cases-ove` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.cqc.org.uk/sites/default/files/20191023_uec18_statisticalrelease.pdf` -> **snapshot** (snapshot 20240227134207); points raw/verified 15/14
  - p43 Share of Type 1 A&E respondents taken to A&E by ambulance (2018 survey) = **32** % (2018-09-01..2018-09-30) [keep: ] quote: "Of those respondents who attended a Type 1 A&E department, almost a third (32%) were taken there by ambulance."
  - p44 Total A&E attendances in England, 2018/19 (all types) = **24,800,000** attendances (2018-04-01..2019-03-31) [keep: ] quote: "there were 24.8 million total attendances in A&E in 2018/19, an increase of 4% from 2017/18"
  - p45 Year-on-year increase in total A&E attendances, 2018/19 vs 2017/18 = **4** % (2018-04-01..2019-03-31) [keep: ] quote: "an increase of 4% from 2017/18, and an increase of 21% compared with 2009/10"
  - p46 Increase in total A&E attendances 2018/19 vs 2009/10 = **21** % (2018-04-01..2019-03-31) [keep: ] quote: "an increase of 4% from 2017/18, and an increase of 21% compared with 2009/10"
  - p47 Type 3 share of A&E attendances, 2009/10 = **30** % (2009-04-01..2010-03-31) [keep: ] quote: "Figures for Type 3 attendances are slowly increasing over time, increasing from 30% in 2009/10 to 35% in 2018/19."
  - p48 Type 3 share of A&E attendances, 2018/19 = **35** % (2018-04-01..2019-03-31) [keep: ] quote: "Figures for Type 3 attendances are slowly increasing over time, increasing from 30% in 2009/10 to 35% in 2018/19."
  - p49 Share of all urgent and emergency care attendances lasting more than four hours, = **10** % (2018-09-01..2018-09-30) [DISCARD: 2018 waiting-time survey share, not an attendance count.] quote: "In September 2018 (the sample month for the survey) NHS England reported that 10% of people spent more than four hours from arrival to admission, transfer or discharge."
  - p50 Median time to treatment for all patients receiving treatment, September 2018 (N = **61** minutes (2018-09-01..2018-09-30) [DISCARD: 2018 median time to treatment, not an attendance count.] quote: "the median average time to treatment for all patients receiving treatment was 61 minutes with 95% of patients receiving treatment within 3 hours 33 minutes."
  - p51 Estimated number of Type 3 and 4 urgent care services combined, England (Septemb = **200** services (2018-09-01..2018-09-30) [keep: ] quote: "we estimate there to be around 200 Type 3 and 4 urgent care services combined."
  - p52 Type 1 respondents whose visit lasted more than four hours, 2018 = **41** % (2018-09-01..2018-09-30) [DISCARD: 2018 survey duration share, not an attendance count.] quote: "just over two fifths of Type 1 respondents (40% in 2016 and 41% in 2018) said that overall, their visit to A&E lasted for more than four hours."
  - p53 Type 3 respondents whose visit lasted more than four hours, 2018 = **12** % (2018-09-01..2018-09-30) [DISCARD: 2018 Type 3 survey duration share, not an attendance count.] quote: "For Type 3 departments this is much lower at 12% (improved from 15% in 2016)."
  - p54 Type 1 respondents who first contacted 999 emergency service before attending (2 = **21** % (2018-09-01..2018-09-30) [DISCARD: 2018 survey contact route share, not an attendance count.] quote: "For Type 1 services the most common response was their GP practice (29%) followed by NHS 111 telephone or online service (28%) and the 999 emergency service (21%)."
  - p55 Type 1 respondents who first contacted NHS 111 telephone/online service before a = **28** % (2018-09-01..2018-09-30) [DISCARD: 2018 survey NHS 111 contact share, not an attendance count.] quote: "For Type 1 services the most common response was their GP practice (29%) followed by NHS 111 telephone or online service (28%) and the 999 emergency service (21%)."
  - p56 Type 3 respondents who first contacted NHS 111 telephone/online service before a = **20** % (2018-09-01..2018-09-30) [DISCARD: 2018 survey Type 3 contact route share, not an attendance count.] quote: "For Type 3 services, the most common response was their GP practice (40%) followed by an NHS 111 telephone or online service (20%)."
- dropped by code checks: 7 (scale word 'million' not supported by quote or table header: 3; period_end missing or unparseable: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d8 [shocks] Reporting-scope and service-configuration changes

Hypothesis: Changes in A&E reporting scope, unit openings/closures, reconfigurations, or respiratory/weather shocks between September 2025 and September 2026 could shift the total away from a simple trend; identifying measurable changes constrains the projection and caveats.

Queries issued by the searcher: NHS England A&E attendances statistics reporting changes 2026; A&E department closures England 2026; "A&E Attendances and Emergency Admissions" July 2026 statistical commentary mapped attendances; NHS England A&E attendances September 2025 total 2.3 million monthly statistics

- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **snapshot** (snapshot 20260515081905); points raw/verified 15/15
  - p57 Total A&E attendances, all department types, England, April 2026 = **2,345,329** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p20 for the April 2026 all-type total.] quote: "The total number of attendances in April 2026 was 2,345,329. This was 2.1% higher when compared with April 2025."
  - p58 Year-on-year growth in total A&E attendances, all types, April 2026 vs April 202 = **2.1** % (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p21 for April 2026 total year-on-year growth.] quote: "The total number of attendances in April 2026 was 2,345,329. This was 2.1% higher when compared with April 2025."
  - p59 Year-on-year growth in Type 1 A&E attendances, April 2026 vs April 2025 = **3** % (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p22 for April 2026 Type 1 growth.] quote: "Attendances at Type 1 A&E departments were 3.0% higher compared with April 2025."
  - p60 Year-on-year growth in Type 3 A&E attendances, April 2026 vs April 2025 = **0.3** % (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p23 for April 2026 Type 3 growth.] quote: "Attendances at Type 3 departments were 0.3% higher compared with April 2025."
  - p61 Type 1 A&E attendance growth, last 3 months vs same period last year (as of Apri = **2.3** % (2026-02-01..2026-04-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, was 2.3% higher and type 3 growth on the same basis was 0.6% higher."
  - p62 Type 3 A&E attendance growth, last 3 months vs same period last year (as of Apri = **0.6** % (2026-02-01..2026-04-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, was 2.3% higher and type 3 growth on the same basis was 0.6% higher."
  - p63 Type 1 A&E attendance growth, last 12 months vs preceding 12 months (as of April = **2.3** % (2025-05-01..2026-04-30) [DISCARD: Exact duplicate of p24 for 12-month Type 1 growth.] quote: "Growth over the last 12 months, compared to the preceding 12 months, for Type 1 was 2.3% and for Type 3 was 1.9%."
  - p64 Type 3 A&E attendance growth, last 12 months vs preceding 12 months (as of April = **1.9** % (2025-05-01..2026-04-30) [DISCARD: Exact duplicate of p25 for 12-month Type 3 growth.] quote: "Growth over the last 12 months, compared to the preceding 12 months, for Type 1 was 2.3% and for Type 3 was 1.9%."
  - p65 Booked A&E attendances, England, April 2026 = **73,777** attendance (A&E visit) (2026-04-01..2026-04-30) [DISCARD: Booked attendances are a subset of total attendances, with no supplied total-to-booked conversion.] quote: "Last month there were 73,777 A&E attendances that had been booked. This was 15.9% lower than in April 2025."
  - p66 Emergency admissions, England, April 2026 = **525,660** emergency admission (2026-04-01..2026-04-30) [keep: ] quote: "There were 525,660 emergency admissions in April 2026. This was 0.5% lower than in April 2025."
  - p67 A&E attendances admitted, transferred or discharged within 4 hours, all types, A = **1,803,787** attendance (A&E visit) (2026-04-01..2026-04-30) [keep: ] quote: "The number of attendances admitted, transferred or discharged within 4 hours was 1,803,787. This was 5.0% higher than in April 2025."
  - p68 Type 1 A&E attendances admitted, transferred or discharged within 4 hours, April = **913,227** attendance (A&E visit) (2026-04-01..2026-04-30) [keep: ] quote: "Of these, 913,227 were Type 1 attendances; 9.2% higher than in April 2025."
  - p69 Type 3 A&E attendances admitted, transferred or discharged within 4 hours, April = **840,154** attendance (A&E visit) (2026-04-01..2026-04-30) [keep: ] quote: "There were 840,154 Type 3 attendances. This was 0.7% higher than in April 2025."
  - p70 Share of all A&E attendances admitted, transferred or discharged within 4 hours, = **76.9** % (2026-04-01..2026-04-30) [keep: ] quote: "76.9% of patients were admitted, transferred or discharged within 4 hours in all A&E Departments in April 2026 compared to 77.1% in March 2026 and 74.8% in April 2025."
  - p71 Number of reporting trusts with Type 1 departments, April 2026 = **121** reporting trusts (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p34 for reporting trusts with Type 1 departments.] quote: "0 out of 121 reporting trusts with Type 1 departments achieved the 95% standard on all types during the month."
- `https://www.england.nhs.uk/2026/06/aes-bore-the-brunt-as-heatwave-piled-pressure-on-nhs/` -> **snapshot** (snapshot 20260618085903); points raw/verified 14/8
  - p72 Total A&E attendances in England, May 2026 (record month) = **2,457,398** attendance (A&E visit) (2026-05-01..2026-05-31) [keep: ] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year - according to newly published NHS data."
  - p73 Increase in A&E attendances in May 2026 over previous record (March 2026) = **25,000** attendance (A&E visit) (2026-05-01..2026-05-31) [keep: ] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year - according to newly published NHS data."
  - p74 A&E attendances managed within four hours of arrival, May 2026 = **1,860,000** attendance (A&E visit) (2026-05-01..2026-05-31) [keep: ] quote: "Despite the unprecedented demand, 1.86 million attendances were managed within four hours of arrival at hospital - the highest number for any May in a decade - as the NHS continued to cut waits for pa"
  - p75 Ambulance incidents handled in May 2026 (third busiest month ever) = **832,089** incident (2026-05-01..2026-05-31) [keep: ] quote: "ce services were also under intense pressure, with paramedics experiencing their third busiest month ever - and demand at levels never seen outside of winter - after handling 832,089 incidents in May."
  - p76 Average daily patients experiencing corridor care in emergency departments, May  = **2,241** patients per day (2026-05-01..2026-05-31) [DISCARD: Corridor-care patient count is a capacity-pressure measure, not an attendance count.] quote: "The figures show that on average, 2,241 patients each day experienced corridor care in emergency departments, while a further 669 patients received care in similar settings elsewhere in hospital."
  - p77 Average daily patients receiving care in similar settings elsewhere in hospital  = **669** patients per day (2026-05-01..2026-05-31) [DISCARD: Similar-setting care count is a capacity-pressure measure, not an attendance count.] quote: "The figures show that on average, 2,241 patients each day experienced corridor care in emergency departments, while a further 669 patients received care in similar settings elsewhere in hospital."
  - p78 Number of trusts accounting for majority of corridor care in emergency departmen = **20** trusts (2026-05-01..2026-05-31) [DISCARD: Trust count accounting for corridor care is not an attendance count and lacks throughput.] quote: "NHS analysis found that 20 trusts accounted for more than half of the cases of corridor care in emergency departments, while 20 trusts also accounted for more than two thirds of cases of corridor care"
  - p79 Diagnostic tests delivered in April 2026 (record for that month) = **2,500,000** diagnostic tests (2026-04-01..2026-04-30) [DISCARD: Diagnostic tests are unrelated to the A&E attendance count.] quote: "Meanwhile, the NHS delivered 2.5 million diagnostic tests in April - the highest number ever recorded for that month."
- `https://www.kentonline.co.uk/canterbury/news/review-into-opening-hours-at-urgent-treatment-centre-deeply-342520/` -> **snapshot** (snapshot 20260731133848); points raw/verified 4/2
  - p80 Year KCH was downgraded to urgent treatment centre (UTC) = **2,016** year (2016-01-01..2016-12-31) [DISCARD: Local KCH UTC downgrade history is not a national reporting-scope change relevant to September 2026.] quote: "and then further downgraded in 2016 to an urgent treatment centre (UTC)"
  - p81 Year KCH last had a fully-functional A&E department = **2,005** year (2005-01-01..2005-12-31) [DISCARD: Local KCH history of full A&E status is not a national reporting-scope change relevant to September 2026.] quote: "serves a massive population in east Kent, but has not had a fully-functional A&E department since 2005"
- dropped by code checks: 8 (number: no number in value_as_written: 2; period_end missing or unparseable: 4; period_end 2026-12-31 after as_of: 1; number: low/high given but value_as_written is not a range: 1)

### b1 [own_history] NHS England monthly A&E collection

Hypothesis: Finding the actual September 2025 all-type total plus the June-August 2026 monthly totals would replace the broad September/April and September/May assumptions with observed recent seasonality and trend, which is the largest uncertainty in the current projection.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions monthly statistics September 2025; A&E attendances England monthly statistics June 2026 total attendances; "A&E attendances" July 2026 NHS England 2.4 million statistical commentary; NHS England A&E attendances and emergency admissions time series September 2025 total attendances 2,3

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://policymogul.com/key-updates/58041/busiest-summer-ever-for-nhs-but-a-es-see-record-numbers-within-four-hours` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-july-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] daily and weekly operational returns

Hypothesis: Early September 2026 daily or weekly A&E attendance returns would anchor the first part of the month and allow the September 2025 day-of-week profile to be applied, reducing reliance on a single monthly ratio.

Queries issued by the searcher: NHS England weekly A&E attendances operational data September 2026; NHS England A&E attendances and emergency admissions monthly statistics August 2026; NHS England "urgent and emergency care" situation report weekly data 2026 A&E attendances provider level; UKHSA emergency department syndromic surveillance weekly bulletin week 36 2026 attendances daily

- `https://www.gov.uk/government/publications/emergency-department-weekly-bulletins-for-2026` -> **snapshot** (snapshot 20260827140906); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://thenhsalliance.org/resources/nhs-activity-tracker-september-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/10/ECDS_Supplementary_Analysis_Statistical_Commentary_September_2026_KUQEYN.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] emergency admissions and conversion

Hypothesis: September emergency admissions and the admissions-per-attendance conversion rate would make the admissions-based route independently usable and help resolve disagreement between the April, May and annual-baseline projections.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions September 2025 statistics; NHS England monthly A&E attendances emergency admissions type 1 type 3 September 2025; NHS England A&E attendances emergency admissions July 2026 statistics; "June 2026" A&E attendances emergency admissions England record

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.rcp.ac.uk/news-and-media/news-and-opinion/new-government-faces-early-test-as-first-nhs-performance-figures-are-published/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p20', 'p57'] Both report the same April 2026 all-type total of 2,345,329; p57 is a duplicate wording of p20, so it adds no independent measurement.
- corroborating: ['p21', 'p58'] Both state April 2026 total attendances were 2.1% above April 2025; duplicate from the same release.
- corroborating: ['p22', 'p59'] Both state Type 1 April 2026 attendances were 3.0% above April 2025; duplicate.
- corroborating: ['p23', 'p60'] Both state Type 3 April 2026 attendances were 0.3% above April 2025; duplicate.
- corroborating: ['p24', 'p63'] Both give 12-month Type 1 growth of 2.3%; duplicate.
- corroborating: ['p25', 'p64'] Both give 12-month Type 3 growth of 1.9%; duplicate.
- corroborating: ['p27', 'p66'] Both give April 2026 emergency admissions as 525,660; p66 adds the year-on-year comparison, so it is the richer copy.
- corroborating: ['p28', 'p67'] Both give April 2026 all-type within-4-hours attendances as 1,803,787; p67 adds growth context.
- corroborating: ['p29', 'p68'] Both give April 2026 Type 1 within-4-hours attendances as 913,227; p68 adds growth context.
- corroborating: ['p30', 'p69'] Both give April 2026 Type 3 within-4-hours attendances as 840,154; p69 adds growth context.
- corroborating: ['p31', 'p70'] Both give the April 2026 all-type within-4-hours share as 76.9%; p70 adds comparison context.
- corroborating: ['p34', 'p71'] Both give 121 reporting trusts with Type 1 departments in April 2026; p71 is a duplicate.
- corroborating: ['p20', 'p72', 'p73'] April 2026 and the May 2026 record month come from the same NHS England monthly collection; p73 places March 2026 just below May 2026. These support a recent level above the 2024-25 average but are no
- corroborating: ['p16', 'p20', 'p72'] The 2024-25 annual total in p16 and the 2026 monthly totals in p20 and p72 are from the same A&E collection. They are consistent in scale, but p16 is annual and older, so it requires a trend and seaso
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5'] ONS population estimates are mutually consistent, but p1 and p2 are UK totals, p4 and p5 are UK growth, and p3 is England growth rather than an England population level. These are contextual only for 
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p43'] Ambulance arrival-share evidence clusters around roughly 31-32% for Type 1 settings, but the periods are older and the scope is not all A&E types; it is contextual rather than directly substitutable.
- corroborating: ['p51', 'p80', 'p81'] Local urgent-care and KCH reconfiguration evidence is not a national reporting-scope change for September 2026; it does not materially move the England total.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p20', 'p67', 'p70'] April 2026 all-type total, all-type within-4-hours count, and 76.9% share are from the same NHS England release; p67/p70 reproduce p20, so this is internal consistency, not independent confirmation.
- corroborating: ['p20', 'p72', 'p73'] April and May 2026 totals, with May described as a record 25,000 above March, show a high 2026 level; same monthly collection and overlapping source.
- corroborating: ['p21', 'p22', 'p23', 'p24', 'p25', 'p61', 'p62'] Growth figures in the same release point to modest positive total growth, with Type 1 stronger than Type 3; they share the same underlying collection, so not independent.
- corroborating: ['p16', 'p20', 'p72'] The 2024-25 annual total gives an average monthly level below April/May 2026, consistent with positive trend; periods and coverage differ but all-type England scope is comparable.
- corroborating: ['p32', 'p33', 'p68', 'p69'] April Type 1 and Type 3 within-4-hour counts divided by their respective shares recover type-level attendance totals; same release, so a consistency route rather than independent evidence.
- corroborating: ['p66', 'p20'] Emergency admissions and total attendances are different measures from the same release; their ratio is a conversion check, not independent confirmation of the attendance level.
- corroborating: ['p72', 'p74', 'p75'] May 2026 record attendances, high within-4-hour count, and ambulance incidents all indicate high urgent-care demand; different metrics and not direct attendance counts.
- corroborating: ['p35', 'p36', 'p37', 'p38', 'p43'] Older conveyance and ambulance-arrival shares cluster around a substantial minority arriving by ambulance; pre-2020 and Type 1/survey scope, usable only with stability and all-type transfer assumption
- corroborating: ['p44', 'p45', 'p46', 'p47', 'p48'] Historical 2018/19 total and Type 3 share provide long-term context; too old and not directly bridgeable to September 2026 without strong trend assumptions.
- different_scope: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Population estimates are UK-level or England growth components; no England population level is supplied, and none is an attendance count. Useful only as broad demographic context, not a direct denomin
- different_scope: ['p17', 'p18', 'p19'] Performance and demographic-use shares describe A&E activity but do not determine the September 2026 attendance count.
- different_scope: ['p76', 'p77', 'p78'] Corridor-care and trust counts show pressure but are not attendance counts and lack a throughput conversion.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 seasonal factor relative to average monthly attendance in 2026-27 | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m1 (m1) | p16 gives the 2024-25 annual all-type total and p21 gives recent total year-on-year growth; applying that growth over the roughly two years to September 2026 and using a September seasonal factor near the annual average bridges the annual total to the target. p20 and p72 show 2026 months above the 2 | Recent total growth embedded in p21 persists through 2026-27 and September is near the annual monthly average. | September 2026 daily returns or a reporting change show attendance far from the annual average or growth materially away from p21. |
| a2 | September 2026 attendance relative to April 2026 | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m2 (m2) | p20 is the April 2026 all-type total. p72 and p73 show May 2026 was a record, and p21 shows positive April year-on-year growth. September is often close to April in level but can be lower, so the ratio is centered near parity with a wide range for weekday composition and seasonality. | September 2026 has a similar weekday and seasonal pattern to April 2026 and no major reporting-scope change. | September 2026 totals deviate materially from April after adjusting for weekday composition. |
| a3 | September 2026 attendance relative to May 2026 | 0.96 | 0.9..1.02 | 0.6775..1.355 (widened) | ratio | m3 (m3) | p72 is the record May 2026 total. May is typically a high month and September is usually lower, while p20 and p21 indicate a high underlying 2026 level. The ratio is therefore below one but not deeply so. | May 2026 is a valid high-season anchor and September follows the usual May-to-September decline. | September 2026 is at or above the May record, or May was distorted by a one-off reporting change. |
| a4 | September 2026 emergency admissions relative to April 2026 | 0.99 | 0.93..1.06 | 0.7021..1.404 (widened) | ratio | m4 (m4) | p66 gives April 2026 emergency admissions. Emergency admissions are seasonal and September is usually similar to or slightly below April, while p21 shows positive underlying A&E growth. The range covers respiratory and weather uncertainty. | Emergency admissions in September 2026 follow usual April-to-September seasonality. | September admissions surge or fall outside the range because of respiratory, weather, or reporting shocks. |
| a6 | September 2026 attendances per emergency admission relative to April 2026 | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m4 (m4) | p20 and p66 jointly determine the April 2026 attendances-per-emergency-admission conversion. September case mix is assumed to leave that conversion near April after allowing for Type 1 and Type 3 growth differences in p22, p23, p61, and p62. | The admissions-to-attendance conversion remains near the April 2026 level after case-mix adjustment. | Type 1/Type 3 case mix or admission thresholds shift materially. |
| a7 | Type 1 September 2026 attendance relative to April 2026 | 1 | 0.94..1.06 | 0.7058..1.412 (widened) | ratio | m5 (m5) | p68 and p32 recover the April 2026 Type 1 total, and p22 and p61 show recent Type 1 growth. September is assumed to be near April for Type 1, with uncertainty from seasonality and reporting scope. | Type 1 September attendance follows usual seasonality relative to April and recent growth persists. | Type 1 growth diverges from p22/p61 or reporting scope changes. |
| a8 | Type 3 September 2026 attendance relative to April 2026 | 1.01 | 0.95..1.07 | 0.7129..1.426 (widened) | ratio | m5 (m5) | p69 and p33 recover the April 2026 Type 3 total, and p23 and p62 show Type 3 growth was positive but weaker than Type 1. Type 3 services are assumed to move slightly above April, with a range covering MIU/WIC reporting changes. | Type 3 September attendance follows usual seasonality relative to April and recent growth persists. | Type 3 growth diverges from p23/p62 or MIU/WIC reporting changes. |
| a9 | Other A&E types September 2026 attendance relative to April 2026 | 1 | 0.9..1.1 | 0.7036..1.407 (widened) | ratio | m5 (m5) | The other-type component is the residual after subtracting type-recovered Type 1 and Type 3 from p20. It is small and has less direct evidence, so the change factor is centered at parity with a wide range for reclassification. | The small residual other-type group moves roughly with the April-to-September average. | A provider reclassification shifts material volume into or out of other types. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2,372,271 | ['p16', 'p21'] / ['a1'] | [] |  | 0.20 | equal |  |
| m2 | formula_mc | 2,345,691 | ['p20'] / ['a2'] | [] |  | 0.20 | equal |  |
| m3 | formula_mc | 2,343,586 | ['p72'] / ['a3'] | [] |  | 0.20 | equal |  |
| m4 | formula_mc | 2,330,752 | ['p66', 'p20'] / ['a4', 'a6'] | [] |  | 0.20 | equal |  |
| m5 | formula_mc | 2,428,420 | ['p68', 'p32', 'p69', 'p33', 'p20'] / ['a7', 'a8', 'a9'] | [] |  | 0.20 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target
- m5 coverage: sum over department type of Type 1, Type 3, other

Result: central **2,363,890** attendance, 80% interval [1,395,609, 4,003,966] attendance, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total A&E attendances across all reported A&E types in England during September 2026 is 2,363,890 attendance (80% model-based interval 1,395,609 to 4,003,966 attendance). This is a conditional range reflecting input uncertainty, not demonstrated accuracy.

Five routes were combined with equal weights of 20% each: 2,372,271, 2,345,691, 2,343,586, 2,330,752 and 2,428,420 attendance. They anchor on observed 2026 months — 2,345,329 attendance (A&E visit) and the record 2,457,398 attendance (A&E visit) — plus 27,400,000 attendance (A&E visit), 2.1%, 525,660 emergency admission, 913,227 attendance (A&E visit), 63.8%, 840,154 attendance (A&E visit) and 97.5%. Each route transfers these to September via assumptions a1–a9 (ratios near parity, e.g. 0.96, 1.01).

The main risk is that September seasonality, weekday composition or reporting scope departs from the assumed ratios, and the routes share the April/May 2026 anchors rather than being independent. Better evidence would be actual September seasonal ratios and any 2026 provider reporting changes.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 seasonal factor relative to average monthly attendance in 2026-[n]: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m1. Overturned by: September 2026 daily returns or a reporting change show attendance far from the annual average or growth materially away from p21.
- a2 September 2026 attendance relative to April 2026: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m2. Overturned by: September 2026 totals deviate materially from April after adjusting for weekday composition.
- a3 September 2026 attendance relative to May 2026: 0.96 ratio, range 0.6775 to 1.355 (range widened by code); used by m3. Overturned by: September 2026 is at or above the May record, or May was distorted by a one-off reporting change.
- a4 September 2026 emergency admissions relative to April 2026: 0.99 ratio, range 0.7021 to 1.404 (range widened by code); used by m4. Overturned by: September admissions surge or fall outside the range because of respiratory, weather, or reporting shocks.
- a6 September 2026 attendances per emergency admission relative to April 2026: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m4. Overturned by: Type [n]/Type [n] case mix or admission thresholds shift materially.
- a7 Type [n] September 2026 attendance relative to April 2026: 1 ratio, range 0.7058 to 1.412 (range widened by code); used by m5. Overturned by: Type [n] growth diverges from p[n]/p[n] or reporting scope changes.
- a8 Type [n] September 2026 attendance relative to April 2026: 1.01 ratio, range 0.7129 to 1.426 (range widened by code); used by m5. Overturned by: Type [n] growth diverges from p[n]/p[n] or MIU/WIC reporting changes.
- a9 Other A&E types September 2026 attendance relative to April 2026: 1 ratio, range 0.7036 to 1.407 (range widened by code); used by m5. Overturned by: A provider reclassification shifts material volume into or out of other types.

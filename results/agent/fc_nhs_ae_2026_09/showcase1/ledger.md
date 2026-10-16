# Evidence ledger: fc_nhs_ae_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the total number of A&E attendances in England in September 2026 (all A&E types, including minor injury units and walk-in centres), as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics.
- as_of: 2026-09-08
- Pinned target: Total A&E attendances in England, all A&E types (major A&E departments, minor injury units, walk-in centres, urgent treatment centres, etc.), as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics. Counts are attendances (visits), not unique patients. | unit attendances (visits) | period 2026-09-01..2026-09-30 | publisher NHS England

- Official value (scoring only, never shown to the agent): 2,440,000

## Directions and pages

### d1 [own_history] NHS England published monthly A&E attendance statistics for England, including all A&E types.

Hypothesis: September 2026 attendances will follow the historical seasonal pattern and recent trend. The same month in previous years (September 2023, 2024, 2025) and the most recent months before the cutoff (e.g., July 2026, August 2026 if available) provide a baseline. The relationship is direct: target = recent level adjusted for seasonality and trend.

Queries issued by the searcher: NHS England A&E attendances September 2025 monthly statistics; monthly A&E attendances England 2026 statistics; NHS England A&E attendances July 2026 2.49 million total attendances; September 2023 A&E attendances England 2.2 million record

- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.nuffieldtrust.org.uk/qualitywatch/nhs-performance-dashboard` -> **snapshot** (snapshot 20260612140646); points raw/verified 5/5
  - p1 Record high monthly A&E attendances in England, May 2026 = **2,500,000** attendances (visits) (2026-05-01..2026-05-31) [keep: ] quote: "A&E attendances hit a record high number of 2.5 million in May 2026."
  - p2 A&E patients waiting on a trolley over 12 hours from decision to admit to admiss = **50,000** patients (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, more than 50 thousand A&E patients waited on a trolley over 12 hours from the decision to admit to admission, a 17% increase from May 2025."
  - p3 Year-on-year increase in A&E patients waiting on a trolley over 12 hours, May 20 = **17** % (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, more than 50 thousand A&E patients waited on a trolley over 12 hours from the decision to admit to admission, a 17% increase from May 2025."
  - p4 NHS England waiting list cases waiting to start treatment, April 2026 = **7,200,000** cases (2026-04-01..2026-04-30) [keep: ] quote: "In April 2026, 7.2 million cases were waiting to start treatment, an increase of more than 110 thousand cases since the previous month."
  - p5 Month-on-month increase in NHS England waiting list cases, April 2026 = **110,000** cases (2026-04-01..2026-04-30) [DISCARD: Duplicate of p4: the same April 2026 waiting-list increase of 110,000 from the same source. It is the month-on-month cha] quote: "In April 2026, 7.2 million cases were waiting to start treatment, an increase of more than 110 thousand cases since the previous month."
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] NHS England publishes weekly A&E sitrep data (e.g., weekly attendances) that can provide a more recent partial total for September 2026.

Hypothesis: If weekly A&E attendance data are available for the first week(s) of September 2026 before the cutoff (cutoff is 2026-09-08, so data for week ending 2026-09-06 might be available), these can be scaled up to a monthly total using historical week-to-month ratios. This provides a direct partial observation.

Queries issued by the searcher: NHS England weekly A&E attendances September 2026 sitrep; NHS England A&E attendances and emergency admissions monthly statistics 2025-26; NHS England weekly A&E attendances statistics 2026-27 statistical work area; "week ending" A&E attendances England September 2026 sitrep urgent emergency care

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/02/ECDS_Supplementary_Analysis_Statistical_Commentary_February_2026_QRT5FW.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d3 [capacity_consumption] A&E departments have physical capacity (beds, cubicles, staff) and operate for a certain number of hours. Utilisation rates and waiting times can indicate throughput.

Hypothesis: Total attendances can be approximated by capacity (e.g., number of A&E departments, average hourly throughput) multiplied by operating hours and utilisation. However, A&E capacity is elastic and not strictly bed-based. More useful: average daily attendances multiplied by days in September. Recent daily attendance figures (if published) or average daily attendances from previous Septembers can be scaled.

Queries issued by the searcher: NHS England A&E attendances September monthly statistics average daily; average daily A&E attendances England 2025 NHS England monthly; NHS England A&E attendances July 2026 monthly operational statistics average daily; A&E attendances September 2025 2.3 million NHS England record September; number of A&E departments England type 1 2026

- `https://www.england.nhs.uk/2026/09/busiest-summer-ever-for-nhs-but-aes-see-record-numbers-within-four-hours/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/long-read/monthly-operational-statistics-june-2025/` -> **snapshot** (snapshot 20260606101505); points raw/verified 15/11
  - p6 Total A&E attendances in England in May = **2,395,886** attendances (visits) (2025-05-01..2025-05-31) [keep: ] quote: "There was a total of 2,395,886 attendances at A&E departments across England in May."
  - p7 Average daily A&E attendances in England in May = **77,287** attendances (visits) per day (2025-05-01..2025-05-31) [keep: ] quote: "The average daily attendances decreased to 77,287."
  - p8 Percentage change in average daily A&E attendances, May vs April = **1** percent (2025-05-01..2025-05-31) [keep: ] quote: "This is 1.0% higher than April's daily average and 0.8% lower than May 2024."
  - p9 Percentage change in average daily A&E attendances, May 2025 vs May 2024 = **0.8** percent (2025-05-01..2025-05-31) [keep: ] quote: "This is 1.0% higher than April's daily average and 0.8% lower than May 2024."
  - p10 Share of patients admitted, transferred or discharged within four hours in May = **75.4** percent of patients (2025-05-01..2025-05-31) [keep: ] quote: "75.4% of patients were admitted, transferred or discharged within four hours compared to 74.8% in April and 74.0% in May 2024."
  - p11 Share of patients admitted, transferred or discharged within four hours in April = **74.8** percent of patients (2025-04-01..2025-04-30) [keep: ] quote: "75.4% of patients were admitted, transferred or discharged within four hours compared to 74.8% in April and 74.0% in May 2024."
  - p12 Share of patients admitted, transferred or discharged within four hours in May 2 = **74** percent of patients (2024-05-01..2024-05-31) [keep: ] quote: "75.4% of patients were admitted, transferred or discharged within four hours compared to 74.8% in April and 74.0% in May 2024."
  - p13 Share of patients attending a type 1 and 2 A&E department who spent 12 hours fro = **9.3** percent of patients (2025-05-01..2025-05-31) [keep: ] quote: "The provisional figures published for May indicate that 9.3% of patients attending a type 1 and 2 A&E department spent 12 hours from arrival in A&E compared with 10.1% last month."
  - p14 Share of patients attending a type 1 and 2 A&E department who spent 12 hours fro = **10.1** percent of patients (2025-04-01..2025-04-30) [keep: ] quote: "The provisional figures published for May indicate that 9.3% of patients attending a type 1 and 2 A&E department spent 12 hours from arrival in A&E compared with 10.1% last month."
  - p15 Incidents where a patient was conveyed to A&E in May = **383,664** incidents (2025-05-01..2025-05-31) [keep: ] quote: "There were 383,664 incidents where a patient was conveyed to A&E or 12.4 thousand per day"
  - p16 Average daily incidents where a patient was conveyed to A&E in May = **12,400** incidents per day (2025-05-01..2025-05-31) [keep: ] quote: "There were 383,664 incidents where a patient was conveyed to A&E or 12.4 thousand per day"
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- dropped by code checks: 4 (period_end missing or unparseable: 4)

### d4 [forecasts_markets] NHS England, NHS trusts, or independent analysts may publish forecasts or targets for A&E activity.

Hypothesis: Published forecasts for September 2026 A&E attendances (e.g., in NHS planning guidance or performance reports) can provide a direct estimate. If no explicit forecast exists, NHS England's operational planning assumptions for 2026-27 may include expected growth rates. These are intentions, not realised outcomes, but can anchor the estimate.

Queries issued by the searcher: NHS England planning guidance 2026-27 A&E attendances; NHS operational planning 2026 A&E activity assumptions; NHS England A&E attendances September 2025 million monthly statistics; NHS England medium term planning framework 2026-27 activity growth A&E attendances assumption

- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://www.healthcare-management.uk/waiting-list-rises-consecutive` -> **snapshot** (snapshot 20260614075920); points raw/verified 11/2
  - p17 Ambulance incidents in England, September 2024 comparison = **721,003** incidents (2024-09-01..2024-09-30) [keep: ] quote: "It was also a record September for ambulance staff with 761,433 incidents, a 6% rise on 721,003 in September 2024."
  - p18 Share of A&E patients seen within four hours, September (prior year) = **74.2** % (2024-09-01..2024-09-30) [keep: ] quote: "a greater proportion of patients were seen within four hours compared to last year (75% vs 74.2%)"
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nuffieldtrust.org.uk/chart/nhs-constitutional-standards-and-interim-objectives-202526-202829` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (scale word 'million' not supported by quote or table header: 3; period year 2025 does not appear in the page text or URL (likely mis-dated): 4; period_end missing or unparseable: 2)

### d5 [related_series] NHS England also publishes emergency admissions and other urgent care activity that may correlate with A&E attendances.

Hypothesis: Emergency admissions are a subset of A&E attendances (those resulting in admission). The ratio of attendances to admissions is relatively stable in the short term. If September 2026 admissions are forecast or partially known, attendances can be estimated by dividing by the historical admission ratio. Alternatively, total urgent care contacts (including NHS 111) may provide a broader denominator.

Queries issued by the searcher: NHS England A&E attendances emergency admissions September 2025 statistics; NHS England A&E attendances emergency admissions 2026 monthly statistics; A&E attendances England 2026 emergency admissions ratio; NHS England A&E attendances July 2026 emergency admissions; NHS England A&E attendances August 2026 statistics; NHS England emergency admissions September 2024 2023 2022 A&E attendances

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.clinicalservicesjournal.com/story/49617/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [shocks] Calendar effects, weather, epidemics (e.g., COVID-19, flu), and policy changes can affect A&E attendances.

Hypothesis: September 2026 may be affected by specific shocks such as a new COVID-19 wave, flu season onset, or NHS strikes. Historical shocks (e.g., 2020 COVID impact, 2022-23 strike days) show measurable deviations. If any known shocks are anticipated for September 2026, adjust the baseline. The direction depends on the shock: respiratory viruses typically increase attendances; strikes may reduce them.

Queries issued by the searcher: NHS strikes September 2026 A&E attendances impact; NHS England winter plan 2026 A&E attendances forecast; NHS England A&E attendances September 2025 2.44 million busiest September record; NHS industrial action announced 2026 junior doctors ballot strike dates; UK flu season 2026-27 forecast early peak respiratory viruses September

- `https://www.england.nhs.uk/news/?filter-keyword=&filter-category=health-housing` -> **snapshot** (snapshot 20260710103622); points raw/verified 1/0
- `https://www.clinicalservicesjournal.com/story/49617/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yas.nhs.uk/media/5878/14i-winter-strategic-approach-2026-27-v10-app-a.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.nationalhealthexecutive.com/articles/ai-forecasting-cut-ae-waiting-times-across-nhs` -> **snapshot** (snapshot 20260616084337); points raw/verified 2/0
- dropped by code checks: 3 (period_end missing or unparseable: 3)

### d7 [base_rates] Population-based rates: A&E attendances per 1,000 population per month.

Hypothesis: Total attendances = England population × monthly attendance rate. The rate can be derived from historical data and adjusted for trend. Population estimates for mid-2026 are available from ONS. This route is useful if recent total attendances are missing but population and rates are known.

Queries issued by the searcher: England population mid-2026 ONS estimate; A&E attendances per 1000 population England monthly rate; NHS England A&E attendances September 2025 total 2.2 million monthly statistics; ONS mid-2025 population estimate England 57.4 million

- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://thenhsalliance.org/resources/activity-tracker-may-2026` -> **snapshot** (snapshot 20260515230752); points raw/verified 15/15
  - p19 England A&E attendances, April 2026 (busiest April on record) = **2,350,000** attendances (visits) (2026-04-01..2026-04-30) [keep: ] quote: "there were 2.35 million A&E attendances in April 2026 (the busiest April on record)"
  - p20 England A&E attendances, April 2026, key points section = **2,350,000** attendances (visits) (2026-04-01..2026-04-30) [DISCARD: Duplicate of p19: the same April 2026 figure of 2.35 million attendances from the same source and snapshot, restated in ] quote: "There were 2.35 million A&E attendances in April 2026, which is the busiest April on record."
  - p21 Share of A&E patients seen within four hours, April 2026 = **76.9** % of A&E attendances (2026-04-01..2026-04-30) [keep: ] quote: "76.9% of patients were seen within four hours."
  - p22 Ambulance incidents, April 2026 (highest April figure since records began) = **789,214** ambulance incidents (2026-04-01..2026-04-30) [keep: ] quote: "There were 789,214 ambulance incidents in April, which is the highest April figure since records began."
  - p23 Diagnostic tests carried out, March 2026 (highest number in a March since record = **2,620,000** diagnostic tests (2026-03-01..2026-03-31) [DISCARD: Diagnostic tests in March 2026 are unrelated to A&E attendances and provide no usable conversion, analogue, or bound for] quote: "2.62 million diagnostic tests were carried out this month. This is the highest number of tests carried out in a March since records began."
  - p24 Diagnostics waiting list, March 2026 (highest since records began January 2006) = **1,920,000** people waiting for diagnostic tests (2026-03-01..2026-03-31) [DISCARD: Diagnostics waiting list is unrelated to A&E attendances and provides no usable conversion, analogue, or bound for the t] quote: "The waiting list reached 1.92 million, which the highest it has been since records began in January 2006."
  - p25 Elective care waiting list size, March 2026 = **7,110,000** cases on the elective waiting list (2026-03-01..2026-03-31) [DISCARD: Elective care waiting list size in March 2026 is unrelated to A&E attendances and provides no usable conversion, analogu] quote: "The size of the waiting list decreased to 7.11 million in March, compared with 7.22 million in February."
  - p26 Elective care waiting list size, February 2026 = **7,220,000** cases on the elective waiting list (2026-02-01..2026-02-28) [DISCARD: Elective care waiting list size in February 2026 is unrelated to A&E attendances and provides no usable conversion, anal] quote: "The size of the waiting list decreased to 7.11 million in March, compared with 7.22 million in February."
  - p27 Share of elective care waits within 18 weeks, March 2026 = **65.3** % of total elective waiting list (2026-03-01..2026-03-31) [DISCARD: Share of elective waits within 18 weeks is unrelated to A&E attendances and provides no usable conversion, analogue, or ] quote: "Waits within 18 weeks were equivalent to 65.3% of the total, therefore meeting the planning guidance aim for 65% of treatments to be waiting no longer than 18 weeks."
  - p28 Elective care cases managed on the waiting list, March 2026 (record level of act = **1,710,000** cases managed on the waiting list (2026-03-01..2026-03-31) [DISCARD: Elective cases managed on the waiting list is unrelated to A&E attendances and provides no usable conversion, analogue, ] quote: "There were record levels of activity with 1.71 million cases managed on the waiting list, but also record levels of demand with 1.95 million cases added to the list."
  - p29 New cases added to the elective care waiting list, March 2026 (record level of d = **1,950,000** cases added to the elective waiting list (2026-03-01..2026-03-31) [DISCARD: New elective cases added to the waiting list is unrelated to A&E attendances and provides no usable conversion, analogue] quote: "There were record levels of activity with 1.71 million cases managed on the waiting list, but also record levels of demand with 1.95 million cases added to the list."
  - p30 People waiting for community services, March 2026 (highest figure on record) = **1,210,000** people waiting for community services (2026-03-01..2026-03-31) [DISCARD: People waiting for community services is unrelated to A&E attendances and provides no usable conversion, analogue, or bo] quote: "1.21 million people were waiting for community services in March, which is the highest figure on record."
  - p31 Share of CYP on the community waiting list waiting 52 weeks or more, March 2026 = **25.5** % of CYP on the community waiting list (2026-03-01..2026-03-31) [DISCARD: Share of children and young people on the community waiting list is unrelated to A&E attendances and provides no usable ] quote: "25.5% of all CYP on the community waiting list have been waiting 52 weeks or more, compared with 0.8% of the adult waiting list."
  - p32 Share of adults on the community waiting list waiting 52 weeks or more, March 20 = **0.8** % of adult community waiting list (2026-03-01..2026-03-31) [DISCARD: Share of adults on the community waiting list is unrelated to A&E attendances and provides no usable conversion, analogu] quote: "25.5% of all CYP on the community waiting list have been waiting 52 weeks or more, compared with 0.8% of the adult waiting list."
  - p33 People in contact with mental health services, end of March 2026 = **2,120,000** people in contact with mental health services (2026-03-31..2026-03-31) [DISCARD: People in contact with mental health services is unrelated to A&E attendances and provides no usable conversion, analogu] quote: "2.12 million people were in contact with mental health services at the ned of March."
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.independent.co.uk/news/uk/ons-england-office-for-national-statistics-scotland-wales-b2687629.html` -> **snapshot** (snapshot 20250210215901); points raw/verified 15/4
  - p34 UK population projected to pass 70 million in mid-2026 = **70,000,000** people (2026-01-01..2026-06-30) [keep: ] quote: "The UK population is likely to pass 70 million in mid-2026, which is unchanged from previous projections."
  - p35 UK population mid-2022 estimate = **67,600,000** people (2022-01-01..2022-06-30) [keep: ] quote: "up 4.9 million from 67.6 million in mid-2022, according to the Office for National Statistics (ONS)."
  - p36 Annual net migration year to mid-2024 = **728,000** people (2023-07-01..2024-06-30) [DISCARD: Net migration projection is a component of the population projection already captured by p34 and p35; it adds no indepen] quote: "Annual net migration is projected to fall from 728,000 in the year to mid-2024 to an average of 340,000 per year from mid-2028 onwards."
  - p37 Projected average annual net migration from mid-2028 onwards = **340,000** people per year (2028-07-01..) [DISCARD: Projected net migration from mid-2028 is beyond the target period and adds no information for September 2026.] quote: "Annual net migration is projected to fall from 728,000 in the year to mid-2024 to an average of 340,000 per year from mid-2028 onwards."
- dropped by code checks: 11 (period_end 2032-06-30 after as_of: 7; period_end 2041-12-31 after as_of: 1; number: no number in value_as_written: 1; period_end 2047-06-30 after as_of: 2)

### d8 [administrative] NHS England monthly statistics are compiled from administrative returns by NHS trusts. The number of trusts and reporting coverage can affect totals.

Hypothesis: Changes in the number of A&E providers or reporting coverage (e.g., new urgent treatment centres included) can cause step changes. If coverage changes are known for 2026, adjust historical totals. Otherwise, assume stable coverage.

Queries issued by the searcher: NHS England A&E Attendances and Emergency Admissions statistics 2026 coverage; NHS England A&E statistics trusts reporting coverage change 2026; NHS England A&E attendances September 2025 total million; "A&E Attendances and Emergency Admissions" August 2026 statistical commentary reporting trusts

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting%20times-and-activity/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] NHS England monthly A&E statistics

Hypothesis: Direct September A&E attendance totals for 2023, 2024 and 2025 would complete the seasonal baseline route (d1) and allow a proper year-on-year September scaling rather than relying on May/April analogues.

Queries issued by the searcher: NHS England A&E Attendances and Emergency Admissions September 2025 statistics; NHS England monthly A&E attendances September 2024 total attendances all types; A&E attendances September 2023 England total attendances NHS statistics; NHS England A&E Attendances and Emergency Admissions September 2025 statistical release

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2024-25/` -> **snapshot** (snapshot 20260508145545); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://wired-gov.net/wg/news.nsf/print/NHS+Confederation+Record+demand+in+AEs+a+concern+ahead+of+annual+winter+spike+in+patients+11102024100500` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] NHS England weekly A&E situation reports

Hypothesis: Weekly A&E attendance data for the week ending 2026-09-06 would provide a direct partial observation for early September 2026, which can be scaled to a monthly total using historical week-to-month ratios (d2).

Queries issued by the searcher: NHS England weekly A&E attendances situation report week ending 6 September 2026; NHS England A&E Attendances and Emergency Admissions September 2026 statistics; NHS England A&E weekly data 2026 attendances week ending; NHS England A&E Attendances and Emergency Admissions monthly statistics 2026-27 August 2026; NHS England weekly A&E situation report statistics September 2026 england.nhs.uk; "A&E" weekly attendances England 2026 "week ending" August September statistics publication

- `https://www.chroniclelive.co.uk/news/uk-news/nhs-warns-early-winter-pressures-34757105?int_source=nba` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://al-ain.com/article/flu-hits-england-early-hospitals-ready` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/publications/emergency-department-weekly-bulletins-for-2026` -> **snapshot** (snapshot 20260827140906); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/10/ominous-signs-of-winter-pressure-growing-as-aes-and-ambulances-see-record-september/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] NHS England planning and performance reports

Hypothesis: NHS England 2026-27 operational planning assumptions or monthly performance reports may contain an expected September 2026 attendance level or growth rate, anchoring the trend adjustment (d4).

Queries issued by the searcher: NHS England 2026-27 operational planning guidance A&E attendances; NHS England A&E attendances monthly statistics 2026; NHS England A&E Attendances and Emergency Admissions July 2026 statistical commentary; NHS England medium term planning guidance October 2025 activity growth A&E attendances 2026/27

- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ M(?!\\d|[.,]\\d)', '(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.england.nhs.uk/2026/07/warm-weather-world-cup-drives-record-nhs-demand-satisfaction-gps-bounce-back/` -> **snapshot** (snapshot 20260809130308); points raw/verified 15/12
  - p38 Average daily A&E attendances in England, June (record daily attendance) = **81,264** attendances (visits) per day (2026-06-01..2026-06-30) [keep: ] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p39 Average daily A&E attendances in England, June (stated threshold exceeded) = **80,000** attendances (visits) per day (2026-06-01..2026-06-30) [DISCARD: Rounded restatement of p38 (the 80,000 threshold is just the rounded form of 81,264). Keeping both would double-count th] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p40 999 calls answered in England, June = **894,143** calls (2026-06-01..2026-06-30) [keep: ] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day"
  - p41 Average daily 999 calls answered in England, June = **29,805** calls per day (2026-06-01..2026-06-30) [keep: ] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day - 10% higher than last June."
  - p42 Year-on-year change in 999 calls answered, June = **10** % (2026-06-01..2026-06-30) [keep: ] quote: "an average of 29,805 calls per day - 10% higher than last June."
  - p43 Daily ambulance incidents in England, June 2026 = **27,171** ambulance incidents per day (2026-06-01..2026-06-30) [keep: ] quote: "There were almost 2,000 more ambulance incidents every day in June (27,171)"
  - p44 Year-on-year increase in daily ambulance incidents, June = **7.3** % (2026-06-01..2026-06-30) [keep: ] quote: "compared with June last year (25,322), an increase of more than 7% (7.3%)."
  - p45 Share of A&E attendances seen within 4 hours in England, June = **75** % (2026-06-01..2026-06-30) [keep: ] quote: "The number of people seen within 4 hours in A&E was 75%, just over half a percentage point down on June last year."
  - p46 NHS overall waiting list for planned care, England, May = **7,280,000** patients (2026-05-01..2026-05-31) [keep: ] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p47 Monthly increase in NHS overall waiting list, England, May vs April = **60,153** patients (2026-05-01..2026-05-31) [DISCARD: Duplicate of p46: the same May 2026 waiting-list increase of 60,153 from the same source. It is the change already impli] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p48 Share of patients waiting within 18 weeks for planned care, England, May = **65.6** % (2026-05-01..2026-05-31) [keep: ] quote: "the number of people waiting within 18 weeks for planned care increased slightly to 65.6% of patients in May, compared with 65% in April."
  - p49 Share of patients waiting within 18 weeks for planned care, England, April = **65** % (2026-04-01..2026-04-30) [keep: ] quote: "increased slightly to 65.6% of patients in May, compared with 65% in April."
- `https://www.nuffieldtrust.org.uk/resource/a-e-waiting-times` -> **snapshot** (snapshot 20260802210607); points raw/verified 15/13
  - p50 Total A&E attendances in England, all A&E types, Q3 2019/20 (pre-pandemic level) = **6,500,000** attendances (visits) (2019-10-01..2019-12-31) [keep: ] quote: "the total number of A&E attendances had been increasing over time, reaching almost 6.5 million in Q3 2019/20."
  - p51 Total A&E attendances in England, all A&E types, Q1 2020/21 (Covid-19 pandemic l = **3,600,000** attendances (visits) (2020-04-01..2020-06-30) [keep: ] quote: "In Q1 2020/21, the total number of A&E attendances fell dramatically to 3.6 million, following the outbreak of the coronavirus (Covid-19) pandemic"
  - p52 Total A&E attendances in England, all A&E types, Q4 2025/26 = **6,900,000** attendances (visits) (2026-01-01..2026-03-31) [keep: ] quote: "In Q4 2025/26 there were 6.9 million A&E attendances."
  - p53 Share of type 1 A&E attendances admitted, transferred or discharged within four  = **60** % of type 1 A&E attendances (2026-01-01..2026-03-31) [DISCARD: Four-hour performance for type 1 departments in Q4 2025/26 is a performance share, not an attendance count, and is not n] quote: "60% of patients attending type 1 departments were admitted, transferred, or discharged within four hours"
  - p54 Share of type 2 and 3 A&E attendances admitted, transferred or discharged within = **97** % of type 2 and 3 A&E attendances (2026-01-01..2026-03-31) [DISCARD: Four-hour performance for type 2 and 3 departments in Q4 2025/26 is a performance share, not an attendance count, and is] quote: "for patients attending type 2 and 3 departments the proportion was 97%"
  - p55 Share of A&E attendances seen in four hours or less, England, May 2026 = **76** % of A&E attendances (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, 76% of A&E attendances were seen in four hours or less."
  - p56 NHS England interim objective for share of A&E patients admitted, transferred or = **82** % of A&E attendances (target) (2026-03-01..2026-03-31) [DISCARD: NHS England interim objective for March 2026 is a target, not a realised outcome, and is not needed for any executable r] quote: "was some way off the objective of 82% for March 2026"
  - p57 NHS England interim objective for share of A&E patients admitted, transferred or = **76** % of A&E attendances (target) (2025-03-01..2025-03-31) [DISCARD: NHS England interim objective for March 2025 is a target, not a realised outcome, and is not needed for any executable r] quote: "The NHS fell short of the 76% objective for March 2025"
  - p58 Patients waiting over four hours from decision to admit to admission, England, D = **170,283** patients (2022-12-01..2022-12-31) [DISCARD: December 2022 waiting-over-four-hours count is a historical pressure indicator from a different period and is not needed] quote: "In December 2022, one in three patients (170,283) were waiting over four hours from decision to admission."
  - p59 Patients waiting over four hours from decision to admit to admission, England, J = **161,141** patients (2026-01-01..2026-01-31) [DISCARD: January 2026 waiting-over-four-hours count is a pressure indicator, not an attendance count, and is not needed for any e] quote: "This improved slightly to 161,141 waiting over four hours from decision to admission in January 2026."
  - p60 Patients waiting more than 12 hours to be admitted after decision to admit, Engl = **50,212** patients (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, 50,212 patients waited for more than 12 hours, representing 9% of the total number of emergency admissions"
  - p61 Share of total emergency admissions represented by patients waiting more than 12 = **9** % of total emergency admissions (2026-05-01..2026-05-31) [DISCARD: Share of emergency admissions waiting over 12 hours is a derived share already implied by p60 and p62; it adds no indepe] quote: "50,212 patients waited for more than 12 hours, representing 9% of the total number of emergency admissions"
  - p62 Estimated share of all A&E attendances waiting over 12 hours to be admitted afte = **3** % of all A&E attendances (2026-05-01..2026-05-31) [DISCARD: Estimated 3% of all A&E attendances waiting over 12 hours is a derived share that cannot be converted to a September 202] quote: "it was estimated that 3% of all patients attending A&E waited over 12 hours to be admitted after a decision to admit was made"
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 5 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 3; period_end 2029-03-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['nhs ae attendances', 'england ae september', 'ae attendances 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p19', 'p20'] All three indicate record-high A&E attendance levels in England in spring 2026 (May 2026 ~2.5m; April 2026 ~2.35m). They are consistent with a high recent baseline, though p19 and p20 are duplicate re
- corroborating: ['p6', 'p7'] p6 gives total May 2025 attendances and p7 gives average daily attendances for the same month; 2,395,886 / 31 ≈ 77,287, so they are internally consistent and describe the same underlying NHS England m
- corroborating: ['p10', 'p11', 'p12'] Four-hour performance shares for April/May 2025 and May 2024 are from the same NHS England statistical release and show a consistent modest improvement over time; they are contextual for pressure, not
- corroborating: ['p13', 'p14'] 12-hour waits as a share of type 1 and 2 A&E attendances for April and May 2025 are from the same release and describe the same operational pressure concept.
- corroborating: ['p15', 'p16'] p15 gives total May 2025 ambulance conveyances and p16 gives the daily average; 383,664 / 31 ≈ 12,376, consistent with the reported 12.4 thousand per day.
- corroborating: ['p17', 'p18'] Both are September 2024 operational figures from the same secondary source: ambulance incidents and four-hour performance. They provide a September analogue but are not direct September attendance cou
- corroborating: ['p4', 'p5'] p4 and p5 are the same April 2026 waiting-list level and month-on-month change from the same source; they are internally consistent but describe elective waiting, not A&E attendances.
- corroborating: ['p25', 'p26'] March and February 2026 elective waiting-list sizes from the same source show a small decrease; they are contextual for overall NHS demand but not direct A&E attendance evidence.
- corroborating: ['p34', 'p35', 'p36', 'p37'] ONS-based population and migration projections from the same article are internally consistent and provide a denominator for a population-rate route, though they are UK-wide rather than England-only.
- conflicting: ['p1', 'p6'] p1 reports May 2026 attendances around 2.5 million while p6 reports May 2025 attendances of 2,395,886. This is not a true contradiction but a year-on-year increase of roughly 4–5%, which is material f
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p19', 'p20'] All three describe England A&E attendances in spring 2026 at a record level: p1 gives May 2026 at 2.5 million, p19/p20 give April 2026 at 2.35 million. p19 and p20 are duplicate statements of the same
- corroborating: ['p6', 'p7'] p6 (2,395,886 attendances in May 2025) and p7 (77,287 average daily attendances in May 2025) are internally consistent: 77,287 x 31 = 2,395,897, matching p6 to rounding. They are the same measurement 
- corroborating: ['p38', 'p39'] p38 (81,264 average daily attendances in June 2026) and p39 (the 80,000 threshold) are the same fact; p39 is a rounded restatement of p38 and adds no independent information. p38 is the strongest rece
- corroborating: ['p1', 'p38'] p1 (2.5 million in May 2026) and p38 (81,264/day in June 2026, implying about 2.44 million for June) are consistent with a 2026 level of roughly 2.4-2.5 million per month in late spring/early summer, 
- corroborating: ['p52', 'p50', 'p51'] p52 (6.9 million attendances in Q4 2025/26, i.e. Jan-Mar 2026) implies about 2.3 million per month in early 2026, consistent with the spring 2026 level in p1 and p19. p50 (6.5 million in Q3 2019/20) a
- corroborating: ['p17', 'p18'] p17 (761,433 ambulance incidents in September 2025, up 6% on 721,003 in September 2024) and p18 (74.2% seen within four hours in September 2024, 75% in September 2025) are both September-specific obse
- corroborating: ['p2', 'p3', 'p60', 'p61', 'p62'] p2/p3 (over 50,000 patients waiting over 12 hours in May 2026, up 17% year on year) and p60/p61/p62 (50,212 patients waiting over 12 hours in May 2026, 9% of emergency admissions, estimated 3% of all 
- corroborating: ['p4', 'p5', 'p46', 'p47'] p4/p5 (7.2 million waiting in April 2026, up 110,000 on March) and p46/p47 (7.28 million in May 2026, up 60,153 on April) are consistent: 7.2m + 60k = 7.26m, close to 7.28m given rounding. They descri
- corroborating: ['p19', 'p21', 'p55'] p19 (2.35 million attendances in April 2026), p21 (76.9% seen within four hours in April 2026) and p55 (76% seen within four hours in May 2026) are consistent on the 2026 performance level. They are f
- corroborating: ['p34', 'p35', 'p36', 'p37'] p34-p37 are ONS population and migration projections: UK population passing 70 million in mid-2026, up from 67.6 million in mid-2022, with net migration falling from 728,000 to 340,000. They are inter
- conflicting: ['p6', 'p38'] p6 (May 2025, 2,395,886 attendances) and p38 (June 2026, 81,264/day) are not directly contradictory because they are different months and years, but they highlight that the 2026 level is materially ab
- conflicting: ['p50', 'p52'] p50 (6.5 million in Q3 2019/20, about 2.17 million/month) and p52 (6.9 million in Q4 2025/26, about 2.3 million/month) show only modest growth over six years, whereas the 2026 monthly figures (2.35-2.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September-to-June seasonal ratio for England A&E attendances | 1.02 | 0.98..1.06 | 0.7207..1.441 (widened) | ratio | m1 (m1), m3 (m3) | September is typically a slightly higher-demand month than June because of the return to school, the start of autumn respiratory illness, and the end of the summer holiday lull. Historical NHS England monthly totals show September running a few percent above June in most recent years. The central va | The seasonal relationship between June and September in 2026 is similar to recent pre-2026 years and no major respiratory wave or strike disruption occurs in September 2026. | Evidence that September 2026 attendances were materially below June 2026 (for example a published September 2026 total below about 2.4 million) or a known major shock (new pandemic, widespread strikes) that breaks the normal seasonal pattern. |
| a2 | Year-on-year growth factor for England A&E attendances, September 2026 vs September 2025 | 1.04 | 1..1.09 | 0.9338..1.167 (widened) | ratio | m2 (m2) | The 2026 data show record levels: May 2026 at 2.5 million (p1), June 2026 at 81,264/day (p38), and April 2026 at 2.35 million (p19). The June 2026 daily rate is about 5% above the May 2025 daily rate (p7), and 999 calls and ambulance incidents in June 2026 were up 7-10% year on year (p42, p44). A 4% | The 2026 growth trend observed in spring and early summer continues into September 2026 and no major demand-suppressing or demand-boosting shock occurs. | Evidence that September 2026 attendances were flat or falling relative to September 2025, or a major shock (strike, pandemic wave) that breaks the trend. |
| a3 | May-to-September seasonal ratio for England A&E attendances | 1 | 0.96..1.04 | 0.7065..1.413 (widened) | ratio | m2 (m2) | May and September are both shoulder months with similar attendance levels in recent NHS England data; September is sometimes marginally higher because of the return to school and early autumn respiratory activity, but the difference is small. A central ratio of 1.00 with a range of 0.96-1.04 is used | The May-to-September seasonal pattern in 2025 is similar to recent years and no unusual event distorts either month. | Evidence that September 2025 attendances were materially different from May 2025 (for example a published September 2025 total far from 2.4 million). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2,486,404 | ['p38'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 2,494,658 | ['p6'] / ['a2', 'a3'] | [] |  | 0.33 | equal |  |
| m3 | formula_mc | 2,363,606 | ['p7'] / ['a1'] | [] |  | 0.33 | equal |  |
| m4 | formula_mc | n/a | ['p52'] / ['a2'] | [] |  | 0.00 |  | formula: numeric constant 3 not allowed (only 1 and exponents); make it a named input |

Result: central **2,447,480**, 80% interval [1,633,266, 3,667,596], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total A&E attendances in England across all A&E types for September 2026 is 2,447,480 attendances, with an 80% interval of 1,633,266 to 3,667,596 (monte carlo). This covers the full month and all reported A&E types, counting visits rather than patients. The combination draws on 3 methods, each weighted 33%, 33%, and 33%; the fourth route was unusable. The strongest route uses the latest observed daily rate, multiplied by the month length and a September-to-June seasonal factor of 1.02 (range 0.7207 to 1.441). A second route transfers an observed [n] monthly total using a May-to-September ratio of 1 and a year-on-year growth factor of 1.04 (range 0.9338 to 1.167). Only the base observations are observed; the seasonal and growth factors are assumptions, so the interval is model-based and conditional, not a demonstrated accuracy guarantee. The main risk is that September 2026 demand departs from these assumed seasonal and growth patterns. Published September 2026 data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September-to-June seasonal ratio for England A&E attendances: 1.02 ratio, range 0.7207 to 1.441 (range widened by code); used by m1, m3. Overturned by: Evidence that September 2026 attendances were materially below June 2026 (for example a published September 2026 total below about [n] million) or a known major shock (new pandemic, widespread strikes) that breaks the normal seasonal pattern.
- a2 Year-on-year growth factor for England A&E attendances, September 2026 vs September 2025: 1.04 ratio, range 0.9338 to 1.167 (range widened by code); used by m2. Overturned by: Evidence that September 2026 attendances were flat or falling relative to September 2025, or a major shock (strike, pandemic wave) that breaks the trend.
- a3 May-to-September seasonal ratio for England A&E attendances: 1 ratio, range 0.7065 to 1.413 (range widened by code); used by m2. Overturned by: Evidence that September 2025 attendances were materially different from May 2025 (for example a published September 2025 total far from [n] million).

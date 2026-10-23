# Evidence ledger: fc_nhs_ae_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the total number of A&E attendances in England in September 2026 (all A&E types, including minor injury units and walk-in centres), as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics.
- as_of: 2026-09-08
- Pinned target: Total number of A&E attendances (all A&E types, including major A&E departments, single-specialty A&E, minor injury units and walk-in centres) in England during September 2026, as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics (count of attendances, not unique  | unit attendances | period 2026-09-01..2026-09-30 | publisher NHS England (A&E Attendances and Emergency Admissions monthly statistics)

- Official value (scoring only, never shown to the agent): 2,440,000

## Directions and pages

### d1 [own_history] NHS England monthly statistics publisher

Hypothesis: September 2026 attendances will follow the level and seasonal pattern of recent Septembers and the most recent published months (through mid-2026); a trend-plus-seasonal-factor extrapolation from the latest actual monthly totals gives the central estimate.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions monthly statistics 2026; NHS England A&E attendances September 2025 total monthly; NHS England A&E attendances June 2026 July 2026 total million monthly figures; "A&E" attendances England monthly total 2,3 million 2024 2025 time series xls NHS England statistics

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.thesun.co.uk/health/40046708/nhs-record-high-emergency-visits-july-summer-surge-heatwave/` -> **snapshot** (snapshot 20260814104209); points raw/verified 0/0
- `https://www.healthcare-management.uk/waiting-list-rises-consecutive` -> **snapshot** (snapshot 20260614075920); points raw/verified 11/5
  - p1 England total A&E attendances, prior September (year-on-year comparison base) = **2,210,000** attendances (2024-09-01..2024-09-30) [keep: ] quote: "There were 2.31m A&E attendances last month, a 4% rise on last September (2.21m)."
  - p2 England ambulance incidents, prior September (comparison base) = **721,003** incidents (2024-09-01..2024-09-30) [keep: ] quote: "It was also a record September for ambulance staff with 761,433 incidents, a 6% rise on 721,003 in September 2024."
  - p3 Share of A&E patients seen within four hours, prior September = **74.2** % (2024-09-01..2024-09-30) [keep: ] quote: "a greater proportion of patients were seen within four hours compared to last year (75% vs 74.2%)"
  - p4 Cancer diagnoses within 28 days (record) = **654,640** cancer diagnoses within 28 days (not stated (page dated 2025-10-09)) [DISCARD: Cancer diagnosis count; irrelevant to A&E attendance volume.] quote: "and cancer diagnosis (654,640 within 28 days)"
  - p5 Appointments and procedures postponed due to five days of resident doctor strike = **54,095** appointments and procedures (not stated (page dated 2025-10-09)) [DISCARD: Postponed appointments from strikes; irrelevant to attendance count.] quote: "despite 54,095 appointments and procedures being postponed due to five days of strike action by resident doctors."
- `https://www.england.nhs.uk/2026/06/aes-bore-the-brunt-as-heatwave-piled-pressure-on-nhs/` -> **snapshot** (snapshot 20260618085903); points raw/verified 12/10
  - p6 England A&E attendances, all types, May 2026 (record month) = **2,457,398** attendances (2026-05-01..2026-05-31) [keep: ] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year"
  - p7 Increase in A&E attendances in May 2026 over previous record (March 2026) = **25,000** attendances (2026-05-01..2026-05-31) [keep: ] quote: "up 25,000 on the previous record set in March earlier this year"
  - p8 England A&E attendances managed within four hours, May 2026 = **1,860,000** attendances (2026-05-01..2026-05-31) [keep: ] quote: "1.86 million attendances were managed within four hours of arrival at hospital - the highest number for any May in a decade"
  - p9 Ambulance incidents handled in May 2026 (third busiest month ever) = **832,089** incidents (2026-05-01..2026-05-31) [keep: ] quote: "after handling 832,089 incidents in May"
  - p10 Average daily patients experiencing corridor care in emergency departments (expe = **2,241** patients per day (2026-05-01..2026-05-31) [DISCARD: Corridor-care patients per day; pressure indicator, not attendance volume.] quote: "on average, 2,241 patients each day experienced corridor care in emergency departments"
  - p11 Average daily patients receiving care in similar settings elsewhere in hospital  = **669** patients per day (2026-05-01..2026-05-31) [DISCARD: Corridor-care elsewhere; pressure indicator.] quote: "a further 669 patients received care in similar settings elsewhere in hospital"
  - p12 NHS overall elective waiting list = **7,220,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Elective waiting list; unrelated to A&E attendances.] quote: "The overall waiting list now stands at 7.22 million"
  - p13 Share of patients waiting within 18 weeks for elective treatment = **65** % (not stated (page dated 2026-06-01)) [DISCARD: 18-week elective share; unrelated.] quote: "with 65% of patients waiting less within 18 weeks for elective treatment"
  - p14 Diagnostic tests delivered in April 2026 (highest ever for that month) = **2,500,000** diagnostic tests (2026-04-01..2026-04-30) [DISCARD: Diagnostic tests; unrelated.] quote: "the NHS delivered 2.5 million diagnostic tests in April - the highest number ever recorded for that month"
  - p15 Reduction in waiting list compared to start of government = **400,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Waiting-list reduction; unrelated.] quote: "cut the waiting lists by more than 400,000 compared to when we came into government"
- dropped by code checks: 8 (period year 2025 does not appear in the page text or URL (likely mis-dated): 6; number: no number in value_as_written: 2)

### d2 [related_series] NHS England type-level breakdown

Hypothesis: Total attendances = type 1 + type 2 + type 3; type 3 (minor injury/walk-in) is a large and separately trending component, so estimating each type's September level and summing reduces error versus a single aggregate trend.

Queries issued by the searcher: NHS England A&E attendances by type 1 2 3 monthly statistics; A&E attendances type 3 minor injury units walk-in centres England monthly September; "August 2026" A&E attendances England type 1 type 2 type 3 total 2,342,959; A&E attendances England monthly time series type 1 type 3 September 2025 2.2 million

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/09/Monthly-AE-Time-Series-August-2026-YG43sd.xls` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://britishresilienceindex.com/deep-dive/ae-england` -> **snapshot** (snapshot 20260828220835); points raw/verified 15/15
  - p16 Total A&E attendances in England, July 2026 (all A&E types) = **2,487,580** attendances (2026-07-01..2026-07-31) [keep: ] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p17 Total A&E attendances in England, 12 months to July 2026 (cumulative) = **28,248,841** attendances (2025-08-01..2026-07-31) [keep: ] quote: "Across the 12 months to July 2026, there were 28,248,841 attendances."
  - p18 Total A&E attendances in England, full year 2011 (all A&E types) = **21,400,000** attendances (2011-01-01..2011-12-31) [keep: ] quote: "By comparison, in 2011 there were around 21.4 million across the full year."
  - p19 Year-on-year change in total A&E attendances, July 2026 vs July 2025 = **3.3** % (2026-07-01..2026-07-31) [keep: ] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p20 Share of all A&E attendances seen within four hours, all department types, July  = **75.4** % (2026-07-01..2026-07-31) [keep: ] quote: "In July 2026, 75.4% of all attendances were seen within four hours across all department types, against the 95% NHS Constitution standard."
  - p21 Share of Type 1 attendances seen within four hours, July 2026 = **61.7** % (2026-07-01..2026-07-31) [keep: ] quote: "July 2026 All types 75.4%; Type 1 61.7%. Zero trusts with a Type 1 department met the 95% standard."
  - p22 Share of all A&E attendances seen within four hours, all department types, Novem = **97.2** % (2010-11-01..2010-11-30) [keep: ] quote: "In November 2010, the first full month on record, England's emergency departments saw 97.2% of patients across all department types within four hours"
  - p23 Share of Type 1 attendances seen within four hours, November 2010 = **95.9** % (2010-11-01..2010-11-30) [keep: ] quote: "For Type 1 major departments the figure was 95.9%."
  - p24 Share of all A&E attendances seen within four hours, all department types, 2022 = **71.2** % (2022-01-01..2022-12-31) [keep: ] quote: "By 2022, after the pressure of the pandemic and its aftermath, it was 71.2%."
  - p25 Share of all A&E attendances seen within four hours, all department types, 2019 = **84.7** % (2019-01-01..2019-12-31) [keep: ] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p26 Share of Type 1 attendances seen within four hours, 2019 = **76.3** % (2019-01-01..2019-12-31) [keep: ] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p27 Share of all A&E attendances seen within four hours, all department types, 2014  = **94.4** % (2014-01-01..2014-12-31) [keep: ] quote: "2014 Last year England met the 95% standard nationally on all types performance (94.4% average; the standard was met in some individual months)."
  - p28 Number of trusts reporting Type 1 attendances, July 2026 = **120** trusts (2026-07-01..2026-07-31) [keep: ] quote: "Of the 120 trusts reporting Type 1 attendances, the league table below shows the 15 under most pressure."
  - p29 12 hour decision-to-admit waits, England, July 2026 (single month) = **47,438** waits (2026-07-01..2026-07-31) [keep: ] quote: "In a single month, July 2026, there were 47,438 such waits."
  - p30 12 hour decision-to-admit waits, England, full year 2025 = **554,044** waits (2025-01-01..2025-12-31) [keep: ] quote: "In 2025 it happened 554,044 times, over four thousand times a day on average."
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2023/10/Statistical-commentary-September-2023-abcdr.pdf` -> **snapshot** (snapshot 20260313184035); points raw/verified 15/15
  - p31 Total A&E attendances, England, September 2023 (all A&E types) = **2,166,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "The total number of attendances in September 2023 was 2,166,000, an increase of 7.8% on September 2022."
  - p32 Year-on-year growth in total A&E attendances, England, September 2023 vs Septemb = **7.8** % (2023-09-01..2023-09-30) [keep: ] quote: "The total number of attendances in September 2023 was 2,166,000, an increase of 7.8% on September 2022."
  - p33 Year-on-year growth in type 1 A&E attendances, England, September 2023 vs Septem = **5.2** % (2023-09-01..2023-09-30) [keep: ] quote: "Attendances at type 1 A&E departments were 5.2% higher when compared with September 2022."
  - p34 Year-on-year growth in type 3 A&E attendances, England, September 2023 vs Septem = **13.1** % (2023-09-01..2023-09-30) [keep: ] quote: "Attendances at type 3 departments were 13.1% higher when compared with September 2022."
  - p35 Type 1 A&E attendance growth, England, last 3 months vs same period last year (t = **1.9** % (2023-07-01..2023-09-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, is 1.9% and type 3 growth on the same basis is 9.4%."
  - p36 Type 3 A&E attendance growth, England, last 3 months vs same period last year (t = **9.4** % (2023-07-01..2023-09-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, is 1.9% and type 3 growth on the same basis is 9.4%."
  - p37 Type 1 A&E attendance growth, England, last 12 months vs preceding 12 months (to = **1** % (2022-10-01..2023-09-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for type 1 is 1.0%, and for type 3 is 10.7%."
  - p38 Type 3 A&E attendance growth, England, last 12 months vs preceding 12 months (to = **10.7** % (2022-10-01..2023-09-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for type 1 is 1.0%, and for type 3 is 10.7%."
  - p39 Booked A&E attendances, England, September 2023 = **66,200** attendances (2023-09-01..2023-09-30) [keep: ] quote: "This month there were 66,200 A&E attendances that had been booked, an increase of 14.0% on September 2022."
  - p40 Emergency admissions, England, September 2023 = **522,000** emergency admissions (2023-09-01..2023-09-30) [keep: ] quote: "There were 522,000 emergency admissions in the month, 7.1% higher than September 2022."
  - p41 Share of type 1 major A&E attendees requiring admission to hospital, England, Se = **28** % (2023-09-01..2023-09-30) [keep: ] quote: "28.0% of patients that attended a type 1 major A&E department required admission to hospital, which compares to 27.2% for September 2022."
  - p42 Share of type 1 major A&E attendees requiring admission to hospital, England, Se = **27.2** % (2022-09-01..2022-09-30) [keep: ] quote: "28.0% of patients that attended a type 1 major A&E department required admission to hospital, which compares to 27.2% for September 2022."
  - p43 Type 1 attendances admitted, transferred or discharged within 4 hours, England,  = **789,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "Of these, 789,000 were type 1 attendances, an increase of 21.5% on September 2022."
  - p44 Type 3 attendances admitted, transferred or discharged within 4 hours, England,  = **721,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "721,000 were type 3 attendances, an increase of 21.9% on September 2022."
  - p45 Share of type 3 A&E attendees seen within 4 hours, England, September 2023 = **95.7** % (2023-09-01..2023-09-30) [keep: ] quote: "95.7% of patients were seen within 4 hours in type 3 A&E departments, compared to 96.5% in August 2023 and 96.0% in September 2022."

### d3 [related_series] Emergency admissions and conversion

Hypothesis: Emergency admissions are reported alongside attendances; the admissions-to-attendance ratio is fairly stable, so a September 2026 admissions forecast divided by the recent conversion ratio provides an independent cross-check on total attendances.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions monthly statistics 2026; NHS England emergency admissions monthly 2026 A&E attendances ratio; A&E attendances and emergency admissions September England 2025 NHS England; "Monthly A&E July 2026" NHS England CSV emergency admissions attendances; NHS England A&E time series August 2026 attendances emergency admissions 2.49 million 547,828; September 2025 A&E attendances 2.31 million emergency admissions 535,609 ratio

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wired-gov.net/wg/news.nsf/articles/NHS+Confederation+Frustrating+rise+in+waiting+lists+despite+NHS+managing+record+elective+cases+over+the` -> **snapshot** (snapshot 20251118134117); points raw/verified 12/12
  - p46 Total A&E attendances across England in September = **2,310,000** attendances (2025-09-01..2025-09-30) [keep: ] quote: "There were 2.31 million attendances at A&Es across England in September, making it the busiest September on record"
  - p47 Emergency admissions in England in September = **535,609** emergency admissions (2025-09-01..2025-09-30) [keep: ] quote: "There were 535,609 emergency admissions in September, another record for the month;"
  - p48 Share of A&E patients admitted, transferred or discharged within four hours in E = **75** % (2025-09-01..2025-09-30) [keep: ] quote: "Some 75.0% of patients were admitted, transferred or discharged from A&E departments within four hours in September"
  - p49 Share of A&E patients admitted, transferred or discharged within four hours in E = **75.9** % (2025-08-01..2025-08-31) [keep: ] quote: "down on the 75.9% in August"
  - p50 Year-on-year change in A&E attendances in England for September = **7** % (2025-09-01..2025-09-30) [keep: ] quote: "It is worrying to see A&E attendances nearly 7% higher than the same month last year"
  - p51 Total waiting list for procedures and appointments in England in August = **7,410,000** patients waiting (2025-08-01..2025-08-31) [DISCARD: Elective waiting list; unrelated.] quote: "The total waiting list for procedures and appointments increased to 7.41 million in August"
  - p52 Record elective cases managed by NHS over the summer = **4,600,000** elective cases (2025-06-01..2025-08-31) [DISCARD: Elective cases; unrelated.] quote: "managing a record 4.6 million elective cases this summer"
  - p53 People waiting more than a year for treatment in England = **200,000** people (not stated (page dated 2025-10-10)) [DISCARD: Year-plus waiters; unrelated.] quote: "there are still nearly 200,000 people who have been waiting more than a year for treatment"
  - p54 Category 2 ambulance average response time in England in September = **30.46** as written "30 minutes and 46 seconds", value check pending minutes and seconds (2025-09-01..2025-09-30) [keep: ] quote: "Category 2 ambulance average response time for September was 30 minutes and 46 seconds"
  - p55 Category 2 ambulance average response time in England in August = **27.03** as written "27 minutes and 03 seconds", value check pending minutes and seconds (2025-08-01..2025-08-31) [keep: ] quote: "worse than the 27 minutes and 03 seconds recorded in August"
  - p56 Category 1 ambulance average response time in England in September = **8.01** as written "8 minutes and 1 second", value check pending minutes and seconds (2025-09-01..2025-09-30) [keep: ] quote: "For Category 1 ambulances, the average response time was 8 minutes and 1 second in September"
  - p57 Category 1 ambulance average response time in England in August = **7.47** as written "7 minutes and 47 seconds", value check pending minutes and seconds (2025-08-01..2025-08-31) [keep: ] quote: "compared to 7 minutes and 47 seconds in August"
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] Daily/weekly operational activity data

Hypothesis: NHS England publishes daily or weekly A&E activity (e.g. daily sitrep/operational data); summing daily attendances over available 2026 days and scaling to a 30-day September gives a bottom-up estimate and reveals within-month variation.

Queries issued by the searcher: NHS England daily A&E attendances sitrep 2026; NHS England operational pressures daily A&E attendances data 2026; "A&E Attendances and Emergency Admissions" July 2026 statistical commentary daily average attendances; Urgent and Emergency Care Daily Situation Reports 2026-27 weekly A&E attendances

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/07/warm-weather-world-cup-drives-record-nhs-demand-satisfaction-gps-bounce-back/` -> **snapshot** (snapshot 20260809130308); points raw/verified 15/14
  - p58 Average daily A&E attendances in England, June (record high) = **81,264** attendances per day (2026-06-01..2026-06-30) [keep: ] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p59 Average daily A&E attendances in England, June, stated threshold exceeded = **80,000** attendances per day (2026-06-01..2026-06-30) [keep: ] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p60 Extra day in May compared with June (day-count difference) = **1** days (2026-05-01..2026-05-31) [keep: ] quote: "despite May recording a slightly higher overall total due to having 1 extra day"
  - p61 999 calls answered in June, England = **894,143** calls (2026-06-01..2026-06-30) [keep: ] quote: "There were 894,143 calls to 999 answered in June"
  - p62 Average 999 calls answered per day in June, England = **29,805** calls per day (2026-06-01..2026-06-30) [keep: ] quote: "an average of 29,805 calls per day - 10% higher than last June"
  - p63 Year-on-year change in 999 calls answered per day, June = **10** % (2026-06-01..2026-06-30) [keep: ] quote: "an average of 29,805 calls per day - 10% higher than last June"
  - p64 Ambulance incidents per day in June, England = **27,171** incidents per day (2026-06-01..2026-06-30) [keep: ] quote: "There were almost 2,000 more ambulance incidents every day in June (27,171)"
  - p65 Year-on-year increase in daily ambulance incidents, June = **7.3** % (2026-06-01..2026-06-30) [keep: ] quote: "an increase of more than 7% (7.3%)"
  - p66 Share of A&E patients seen within 4 hours, June = **75** % (2026-06-01..2026-06-30) [keep: ] quote: "The number of people seen within 4 hours in A&E was 75%"
  - p67 Average daily instances of corridor care in emergency departments, England = **2,432** instances per day (not stated (page dated 2026-07-01)) [DISCARD: Corridor-care instances; pressure indicator.] quote: "Nationally per day, there were on average 2,432 instances of Corridor Care in emergency departments"
  - p68 Average daily patients receiving corridor care elsewhere in hospital, England = **749** patients per day (not stated (page dated 2026-07-01)) [DISCARD: Corridor-care elsewhere; pressure indicator.] quote: "749 patients receiving Corridor Care elsewhere in hospital"
  - p69 Overall NHS waiting list, May = **7,280,000** patients (2026-05-01..2026-05-31) [DISCARD: Waiting list; unrelated.] quote: "The overall waiting list increased to 7.28 million in May"
  - p70 Increase in overall waiting list, May vs April = **60,153** patients (2026-05-01..2026-05-31) [DISCARD: Waiting-list change; unrelated.] quote: "a rise of 60,153 compared to April"
  - p71 Share of patients waiting within 18 weeks for planned care, May = **65.6** % (2026-05-01..2026-05-31) [DISCARD: 18-week share; unrelated.] quote: "the number of people waiting within 18 weeks for planned care increased slightly to 65.6% of patients in May"
- `https://www.england.nhs.uk/2026/06/aes-bore-the-brunt-as-heatwave-piled-pressure-on-nhs/` -> **snapshot** (snapshot 20260618085903); points raw/verified 15/13
  - p72 England A&E attendances, May 2026 (record month) = **2,457,398** attendances (2026-05-01..2026-05-31) [DISCARD: Duplicate of p6.] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year - according to newly published NHS data."
  - p73 Increase in A&E attendances in May 2026 over previous record (March 2026) = **25,000** attendances (2026-05-01..2026-05-31) [DISCARD: Duplicate of p7.] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year - according to newly published NHS data."
  - p74 England A&E attendances, March 2026 (previous record month) = **2,457,398** attendances (2026-03-01..2026-03-31) [DISCARD: Duplicate of p6/p7 (March record value mislabeled).] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year - according to newly published NHS data."
  - p75 England A&E attendances managed within four hours, May 2026 = **1,860,000** attendances (2026-05-01..2026-05-31) [DISCARD: Duplicate of p8.] quote: "Despite the unprecedented demand, 1.86 million attendances were managed within four hours of arrival at hospital - the highest number for any May in a decade - as the NHS continued to cut waits for pa"
  - p76 Ambulance incidents handled in May 2026 (third busiest month ever) = **832,089** incidents (2026-05-01..2026-05-31) [DISCARD: Duplicate of p9.] quote: "ce services were also under intense pressure, with paramedics experiencing their third busiest month ever - and demand at levels never seen outside of winter - after handling 832,089 incidents in May."
  - p77 Average daily patients experiencing corridor care in emergency departments = **2,241** patients per day (not stated (page dated 2026-06-01)) [DISCARD: Duplicate corridor-care; pressure indicator.] quote: "The figures show that on average, 2,241 patients each day experienced corridor care in emergency departments, while a further 669 patients received care in similar settings elsewhere in hospital."
  - p78 Average daily patients receiving care in similar settings elsewhere in hospital  = **669** patients per day (not stated (page dated 2026-06-01)) [DISCARD: Duplicate corridor-care; pressure indicator.] quote: "The figures show that on average, 2,241 patients each day experienced corridor care in emergency departments, while a further 669 patients received care in similar settings elsewhere in hospital."
  - p79 NHS overall waiting list size = **7,220,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Duplicate waiting list; unrelated.] quote: "The overall waiting list now stands at 7.22 million, with 65% of patients waiting less within 18 weeks for elective treatment."
  - p80 Share of patients waiting within 18 weeks for elective treatment = **65** % (not stated (page dated 2026-06-01)) [DISCARD: 18-week share; unrelated.] quote: "The overall waiting list now stands at 7.22 million, with 65% of patients waiting less within 18 weeks for elective treatment."
  - p81 Diagnostic tests delivered in April 2026 (record for that month) = **2,500,000** diagnostic tests (2026-04-01..2026-04-30) [DISCARD: Diagnostic tests; unrelated.] quote: "Meanwhile, the NHS delivered 2.5 million diagnostic tests in April - the highest number ever recorded for that month."
  - p82 Reduction in waiting list compared to start of government = **400,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Waiting-list reduction; unrelated.] quote: " treated a record number of people within four hours in A&E in May, delivered record levels of diagnostic tests and cut the waiting lists by more than 400,000 compared to when we came into government."
  - p83 Number of trusts accounting for concentrated corridor care cases = **20** trusts (not stated (page dated 2026-06-01)) [DISCARD: Corridor-care trust count; not a volume driver usable here.] quote: "NHS analysis found that 20 trusts accounted for more than half of the cases of corridor care in emergency departments, while 20 trusts also accounted for more than two thirds of cases of corridor care"
  - p84 Number of points in NHS plan to eradicate corridor care = **7** points (not stated (page dated 2026-06-01)) [DISCARD: Plan point count; irrelevant.] quote: "lly unacceptable and should have no place in the NHS, and this is why we have set out a 7-point plan to eradicate it, alongside offering targeted support for the trusts facing the greatest challenges."
- `https://www.england.nhs.uk/statistics/statistical-work-areas/uec-sitrep/urgent-and-emergency-care-daily-situation-reports-2025-26/` -> **snapshot** (snapshot 20260617071808); points raw/verified 0/0
- dropped by code checks: 3 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; number: no number in value_as_written: 2)

### d5 [shocks] Calendar and seasonal effects analyst

Hypothesis: September has a specific weekday composition and post-summer/back-to-school pattern; adjusting a recent-month baseline by the September-vs-baseline weekday and seasonal multiplier (from prior years) corrects for calendar effects that shift attendance counts.

Queries issued by the searcher: NHS England A&E attendances September 2025 monthly statistics; A&E attendances seasonal variation England month of year; NHS England A&E attendances June 2026 monthly statistics total attendances; "A&E" attendances England monthly time series 2019 2020 2021 2022 2023 2024 2025 by month table

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/07/ECDS_Supplementary_Analysis_Statistical_Commentary_June_2026_82ESB8.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/hospital-accident--emergency-activity/2019-20/time-of-day` -> **snapshot** (snapshot 20201229103705); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] NHS planning and forecast bodies

Hypothesis: NHS England planning guidance, winter pressure forecasts or published projections may indicate expected A&E demand levels for autumn 2026, providing an external anchor for the September estimate.

Queries issued by the searcher: NHS England A&E attendances monthly statistics 2026; NHS planning guidance 2026/27 A&E activity growth assumption; September 2025 A&E attendances England total monthly 2.2 million NHS England statistics; "2026/27" national planning assumptions A&E attendances growth 1.8% non-elective 2.6%

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/07/warm-weather-world-cup-drives-record-nhs-demand-satisfaction-gps-bounce-back/` -> **snapshot** (snapshot 20260809130308); points raw/verified 15/14
  - p85 Average daily A&E attendances in England, June (record daily attendance) = **81,264** attendances per day (2026-06-01..2026-06-30) [DISCARD: Duplicate of p58.] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p86 Average daily A&E attendances threshold exceeded in June, England = **80,000** attendances per day (2026-06-01..2026-06-30) [DISCARD: Duplicate of p59.] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p87 Extra day in May versus June (explaining higher May overall A&E total) = **1** days (2026-05-01..2026-05-31) [DISCARD: Duplicate of p60.] quote: "despite May recording a slightly higher overall total due to having 1 extra day"
  - p88 Share of A&E patients seen within 4 hours, June, England = **75** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p66.] quote: "The number of people seen within 4 hours in A&E was 75%, just over half a percentage point down on June last year."
  - p89 999 calls answered in June, England = **894,143** calls (2026-06-01..2026-06-30) [DISCARD: Duplicate of p61.] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day - 10% higher than last June."
  - p90 Average daily 999 calls answered in June, England = **29,805** calls per day (2026-06-01..2026-06-30) [DISCARD: Duplicate of p62.] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day - 10% higher than last June."
  - p91 Year-on-year increase in 999 calls answered, June = **10** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p63.] quote: "an average of 29,805 calls per day - 10% higher than last June"
  - p92 Average daily ambulance incidents in June, England = **27,171** ambulance incidents per day (2026-06-01..2026-06-30) [DISCARD: Duplicate of p64.] quote: "There were almost 2,000 more ambulance incidents every day in June (27,171) - compared with June last year (25,322)"
  - p93 Year-on-year increase in daily ambulance incidents, June = **7.3** % (2026-06-01..2026-06-30) [DISCARD: Duplicate of p65.] quote: "an increase of more than 7% (7.3%)"
  - p94 Average daily corridor care instances in emergency departments, England = **2,432** instances per day (not stated (page dated 2026-07-01)) [DISCARD: Duplicate corridor-care; pressure indicator.] quote: "Nationally per day, there were on average 2,432 instances of Corridor Care in emergency departments"
  - p95 Average daily patients receiving corridor care elsewhere in hospital, England = **749** patients per day (not stated (page dated 2026-07-01)) [DISCARD: Duplicate corridor-care; pressure indicator.] quote: "749 patients receiving Corridor Care elsewhere in hospital"
  - p96 Overall NHS waiting list, May, England = **7,280,000** patients (2026-05-01..2026-05-31) [DISCARD: Duplicate waiting list; unrelated.] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p97 Increase in overall NHS waiting list, May versus April, England = **60,153** patients (2026-05-01..2026-05-31) [DISCARD: Waiting-list change; unrelated.] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p98 Share of patients waiting within 18 weeks for planned care, May, England = **65.6** % (2026-05-01..2026-05-31) [DISCARD: 18-week share; unrelated.] quote: "the number of people waiting within 18 weeks for planned care increased slightly to 65.6% of patients in May, compared with 65% in April"
- `https://www.hfma.org.uk/articles/blended-model-uec-heart-payment-system-proposals` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.healthcare-management.uk/waiting-list-rises-consecutive` -> **snapshot** (snapshot 20260614075920); points raw/verified 12/6
  - p99 A&E attendances in England, previous September (comparison year) = **2,210,000** attendances (2024-09-01..2024-09-30) [DISCARD: Duplicate of p1.] quote: "There were 2.31m A&E attendances last month, a 4% rise on last September (2.21m)."
  - p100 Share of A&E patients seen within four hours, previous September = **74.2** % (2024-09-01..2024-09-30) [DISCARD: Duplicate of p3.] quote: "a greater proportion of patients were seen within four hours compared to last year (75% vs 74.2%)"
  - p101 Ambulance incidents in England, September 2024 = **721,003** incidents (2024-09-01..2024-09-30) [DISCARD: Duplicate of p2.] quote: "a 6% rise on 721,003 in September 2024"
  - p102 Cancer diagnoses within 28 days = **654,640** cancer diagnoses within 28 days (not stated (page dated 2025-10-09)) [DISCARD: Duplicate of p4; irrelevant.] quote: "cancer diagnosis (654,640 within 28 days)"
  - p103 Appointments and procedures postponed due to five days of resident doctor strike = **54,095** appointments and procedures (not stated (page dated 2025-10-09)) [DISCARD: Duplicate of p5; irrelevant.] quote: "despite 54,095 appointments and procedures being postponed due to five days of strike action by resident doctors"
  - p104 Days of resident doctor strike action = **5** as written "five", value check pending days (not stated (page dated 2025-10-09)) [DISCARD: Strike days; irrelevant to attendance volume.] quote: "54,095 appointments and procedures being postponed due to five days of strike action by resident doctors"
- dropped by code checks: 7 (period year 2025 does not appear in the page text or URL (likely mis-dated): 7)

### b1 [own_history] NHS England monthly A&E statistics

Hypothesis: A complete monthly total-attendance series for England from 2024-01 through 2026-08 (all A&E types) would let us fit a trend-plus-September-seasonal-factor model directly, replacing the sparse two-point September history (p1, p46) and the single July 2026 anchor (p16). This is the missing input that would complete the d1 route.

Queries issued by the searcher: NHS England A&E Attendances and Emergency Admissions monthly statistics 2026-27 total attendances; statistics.england.nhs.uk A&E attendances emergency admissions monthly time series; "A&E Time Series" NHS England monthly attendances xlsx "Time Series" March 2026 total attendances England; NHS England A&E Attendances and Emergency Admissions 2025-26 monthly data England time series attendances by month

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://theobsidian.media/healthcare/intelligence/nhs` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-april-2026/acute-sector` -> **snapshot** (snapshot 20260417150357) **LEAK SENTINEL HIT ['(?<![\\d.,])2\\.34\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-

### b2 [related_series] NHS England type-level breakdown

Hypothesis: Separate type 1, type 2 and type 3 monthly attendance totals for 2025 and 2026 would let us estimate each component's September level and sum them (d2), reducing error versus a single aggregate trend and testing whether type 3 growth is still outpacing type 1 as in 2023 (p33, p34).

Queries issued by the searcher: NHS England A&E attendances by type monthly 2026 type 1 type 2 type 3; A&E Attendances and Emergency Admissions monthly statistics NHS England September 2025 type 1 type 2 type 3; "type 3" attendances September 2025 NHS England A&E "2.31 million" type 1 attendances; NHS England A&E time series monthly attendances by department type xlsx 2026

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/04/ECDS_Supplementary_Analysis_Statistical_Commentary_March_2026_V1THYY.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://britishresilienceindex.com/deep-dive/ae-england` -> **snapshot** (snapshot 20260828220835); points raw/verified 15/15
  - p105 Total A&E attendances in England, July 2026 (all department types) = **2,487,580** attendances (2026-07-01..2026-07-31) [DISCARD: Duplicate of p16.] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p106 Year-on-year change in total A&E attendances, July 2026 vs July 2025 = **3.3** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p19.] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p107 Total A&E attendances in England, 12 months to July 2026 (cumulative) = **28,248,841** attendances (2025-08-01..2026-07-31) [DISCARD: Duplicate of p17.] quote: "Across the 12 months to July 2026, there were 28,248,841 attendances."
  - p108 Total A&E attendances in England, full year 2011 (all department types) = **21,400,000** attendances (2011-01-01..2011-12-31) [DISCARD: Duplicate of p18.] quote: "By comparison, in 2011 there were around 21.4 million across the full year."
  - p109 Share of all A&E attendances seen within four hours, all department types, July  = **75.4** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p20.] quote: "In July 2026, 75.4% of all attendances were seen within four hours across all department types, against the 95% NHS Constitution standard."
  - p110 Share of Type 1 major A&E attendances seen within four hours, July 2026 = **61.7** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p21.] quote: "July 2026 All types 75.4%; Type 1 61.7%. Zero trusts with a Type 1 department met the 95% standard."
  - p111 Share of all A&E attendances seen within four hours, all department types, 2022 = **71.2** % (2022-01-01..2022-12-31) [DISCARD: Duplicate of p24.] quote: "By 2022, after the pressure of the pandemic and its aftermath, it was 71.2%."
  - p112 Share of all A&E attendances seen within four hours, all department types, Novem = **97.2** % (2010-11-01..2010-11-30) [DISCARD: Duplicate of p22.] quote: "In November 2010, the first full month on record, England's emergency departments saw 97.2% of patients across all department types within four hours"
  - p113 Share of Type 1 major A&E attendances seen within four hours, November 2010 = **95.9** % (2010-11-01..2010-11-30) [DISCARD: Duplicate of p23.] quote: "For Type 1 major departments the figure was 95.9%."
  - p114 Share of all A&E attendances seen within four hours, all department types, 2019 = **84.7** % (2019-01-01..2019-12-31) [DISCARD: Duplicate of p25.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p115 Share of Type 1 major A&E attendances seen within four hours, 2019 = **76.3** % (2019-01-01..2019-12-31) [DISCARD: Duplicate of p26.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p116 Number of trusts reporting Type 1 attendances, July 2026 = **120** trusts (2026-07-01..2026-07-31) [DISCARD: Duplicate of p28.] quote: "Of the 120 trusts reporting Type 1 attendances, the league table below shows the 15 under most pressure."
  - p117 12 hour decision-to-admit waits, England, July 2026 (single month) = **47,438** waits (2026-07-01..2026-07-31) [DISCARD: Duplicate of p29.] quote: "In a single month, July 2026, there were 47,438 such waits."
  - p118 12 hour decision-to-admit waits, England, full year 2025 = **554,044** waits (2025-01-01..2025-12-31) [DISCARD: Duplicate of p30.] quote: "In 2025 it happened 554,044 times, over four thousand times a day on average."
  - p119 12 hour decision-to-admit waits, England, full year 2011 = **130** waits (2011-01-01..2011-12-31) [DISCARD: Duplicate of p30 context; irrelevant.] quote: "In 2011, across all of England, it happened 130 times in the whole year."

### b3 [base_rates] Seasonal calendar adjustment

Hypothesis: A September-vs-August and September-vs-July seasonal multiplier for total attendances, estimated from several prior years, would convert the July 2026 anchor (p16) and June daily rate (p58) into a September 2026 level (d5). Without it we must assume a seasonal factor.

Queries issued by the searcher: NHS England A&E attendances monthly 2019 2020 2021 2022 2023 2024 2025 statistics; A&E attendances England September seasonal pattern monthly time series; "Monthly A&E Time Series" NHS England statistics xls attendances by month; King's Fund A&E attendances monthly England 2019 2020 2021 2022 2023 2024 chart data September August

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.myhsn.co.uk/top-tip/nhs-winter-pressure-is-a-myth-what-the-data-really-shows/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://shepwayvox.org/wp-content/uploads/2025/10/CBP-7281.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['nhs ae attendances', 'england ae september', 'ae attendances 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p99'] Both give England total A&E attendances for September 2024 as ~2.21m; p99 is a duplicate of p1 from the same healthcare-management.uk snapshot, so they are not independent.
- corroborating: ['p46', 'p50', 'p1'] p46 (2.31m September 2025) and p50 (~7% YoY rise) are consistent with p1's 2.21m September 2024 base; same underlying NHS England monthly statistics, so not independent measurements.
- corroborating: ['p6', 'p72'] Duplicate statements of May 2026 total 2,457,398 from the same NHS England release; identical value, no added independence.
- corroborating: ['p7', 'p73', 'p74'] p7/p73 give the +25,000 May-over-March increment; p74 mislabels the March record with the May value (2,457,398) rather than March's implied ~2,432,398, so p74 is internally inconsistent and should not
- corroborating: ['p16', 'p17', 'p19'] July 2026 total 2,487,580, 12-month cumulative 28,248,841 and +3.3% YoY are mutually consistent from the same britishresilienceindex.com summary; one underlying source.
- corroborating: ['p58', 'p85', 'p59', 'p86'] June 2026 average daily attendances 81,264 (first time >80,000) repeated across two NHS England snapshots; same measurement, not independent.
- corroborating: ['p60', 'p87'] Both state May had one extra day versus June, explaining May's slightly higher total despite lower daily rate; consistent with p6 and p58.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] September 2023 NHS England release: total 2,166,000 with type 1 +5.2% and type 3 +13.1% YoY, and 3-/12-month growth figures consistent with type 3 growing faster than type 1. Same release, one source.
- corroborating: ['p40', 'p47'] Emergency admissions September 2023 (522,000) and September 2025 (535,609) form a comparable September series; both from NHS England monthly statistics.
- corroborating: ['p41', 'p42'] Type 1 admission share 28.0% (Sep 2023) vs 27.2% (Sep 2022) — a stable conversion ratio usable for cross-checks.
- corroborating: ['p43', 'p44', 'p45'] Type 1 and type 3 4-hour performance counts and type 3 95.7% seen-within-4h are internally consistent with the September 2023 release.
- corroborating: ['p20', 'p21', 'p66', 'p88'] All-types 4-hour performance ~75% in mid-2026 (July 75.4%, June 75%) — consistent across sources; performance, not volume, so only contextual.
- corroborating: ['p48', 'p49', 'p100'] September 2025 75.0% vs August 75.9%, and September 2024 74.2% — a stable performance band; contextual only.
- corroborating: ['p2', 'p101'] September 2024 ambulance incidents 721,003 stated twice; same source.
- corroborating: ['p9', 'p76'] May 2026 ambulance incidents 832,089 stated twice; same release.
- corroborating: ['p61', 'p62', 'p89', 'p90'] June 2026 999 calls 894,143 and 29,805/day stated across two snapshots; same measurement.
- corroborating: ['p64', 'p92'] June 2026 ambulance incidents 27,171/day stated twice; same release.
- corroborating: ['p10', 'p77'] May 2026 corridor care 2,241/day stated twice; same release.
- corroborating: ['p11', 'p78'] May 2026 corridor care elsewhere 669/day stated twice; same release.
- corroborating: ['p12', 'p79'] Waiting list 7.22m stated twice; same release.
- corroborating: ['p13', 'p80'] 65% within 18 weeks stated twice; same release.
- corroborating: ['p14', 'p81'] April 2026 diagnostic tests 2.5m stated twice; same release.
- corroborating: ['p15', 'p82'] 400,000 waiting-list reduction stated twice; same release.
- corroborating: ['p67', 'p94'] Corridor care 2,432/day stated twice; same release.
- corroborating: ['p68', 'p95'] Corridor care elsewhere 749/day stated twice; same release.
- corroborating: ['p69', 'p96'] Waiting list 7.28m May 2026 stated twice; same release.
- corroborating: ['p70', 'p97'] Waiting-list rise 60,153 stated twice; same release.
- corroborating: ['p71', 'p98'] 65.6% within 18 weeks stated twice; same release.
- corroborating: ['p4', 'p102'] Cancer diagnoses 654,640 stated twice; same source, irrelevant to A&E volume.
- corroborating: ['p5', 'p103', 'p104'] 54,095 postponed appointments over 5 strike days stated twice; irrelevant to A&E volume.
- corroborating: ['p51', 'p52', 'p53'] Elective waiting list 7.41m, 4.6m elective cases, ~200,000 >1yr waiters — same wired-gov release, contextual only.
- corroborating: ['p54', 'p55', 'p56', 'p57'] September 2025 vs August 2025 ambulance response times — same release, contextual only.
- corroborating: ['p22', 'p23', 'p24', 'p25', 'p26', 'p27'] Historical 4-hour performance series (2010, 2014, 2019, 2022) from britishresilienceindex.com; consistent trend, contextual only.
- corroborating: ['p28', 'p29', 'p30'] July 2026 120 type-1 trusts, 47,438 12-hour waits, 554,044 in 2025 — same source, contextual only.
- corroborating: ['p39', 'p31'] Booked attendances 66,200 in September 2023 is a subset of the 2,166,000 total; consistent.
- corroborating: ['p18', 'p31', 'p46'] Long-run growth from 21.4m (2011) to 2.17m (Sep 2023) to 2.31m (Sep 2025) is consistent with a rising trend; different periods, not contradictions.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p46', 'p31'] Three successive September totals (2023: 2.166m; 2024: 2.21m; 2025: 2.31m) from NHS-derived reporting; consistent upward drift of roughly 2-4% per year. Different vintages but same definition (all A&E
- corroborating: ['p16', 'p105', 'p17', 'p107', 'p19', 'p106'] Duplicate copies of the same July 2026 release (2,487,580; +3.3% YoY; 28,248,841 rolling 12m). Same underlying NHS England publication, so not independent confirmation — one measurement.
- corroborating: ['p6', 'p72', 'p73', 'p74'] May 2026 record 2,457,398 and the +25,000 over March 2026 record; consistent with July 2026 at 2,487,580 (a further record). Establishes 2026 monthly level around 2.45-2.49m.
- corroborating: ['p58', 'p85', 'p59', 'p86', 'p60', 'p87'] June 2026 average daily 81,264 (first time >80,000); May had one extra day so slightly higher monthly total despite lower daily rate. Internally consistent; implies June total ≈ 2.44m.
- corroborating: ['p46', 'p47', 'p50'] September 2025: 2.31m attendances, 535,609 emergency admissions, ~7% YoY growth — same release, same month, mutually consistent.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38'] September 2023 release: total 2.166m (+7.8%), type 1 +5.2%, type 3 +13.1%; 3-month and 12-month growth figures consistent with type 3 outpacing type 1. Same publication.
- corroborating: ['p20', 'p21', 'p109', 'p110'] July 2026 four-hour performance (all types 75.4%, type 1 61.7%) duplicated across snapshots; describes pressure, not volume — contextual only.
- corroborating: ['p1', 'p99', 'p3', 'p100'] September 2024 total 2.21m and 74.2% four-hour performance duplicated across snapshots; same measurement.
- corroborating: ['p2', 'p101'] September 2024 ambulance incidents 721,003 duplicated; different metric from attendances, contextual only.
- corroborating: ['p47', 'p40'] Emergency admissions September 2023 (522,000) and September 2025 (535,609) show slow growth; supports a stable admissions/attendance ratio as a cross-check, though the ratio must be derived from paire
- corroborating: ['p12', 'p51', 'p69', 'p96', 'p79'] Elective waiting list figures across 2025-2026 (7.22-7.41m) — unrelated to A&E attendance volume; contextual only.
- corroborating: ['p4', 'p5', 'p102', 'p103', 'p104'] Cancer diagnoses and strike-postponed appointments — unrelated to A&E attendance counts; not usable.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 vs July 2026 total attendance change factor | 0.97 | 0.93..1.01 | 0.8669..1.084 (widened) | ratio | m1 (m1) | September typically runs slightly below the summer peak month; 2025 September (2.31m) was below the 2025 summer level, and 2026 July (p16) is a record. A modest decline of ~3% with wide uncertainty reflects month-to-month variation and trend. | September 2026 follows the usual post-summer dip relative to July. | Evidence that September 2026 exceeds July 2026 or falls far below. |
| a2 | September 2026 vs September 2025 YoY growth factor | 1.035 | 1.01..1.06 | 0.9255..1.157 (widened) | ratio | m2 (m2) | Recent YoY growth: July 2026 +3.3% (p19), September 2025 ~+7% (p50), September 2024 ~+4% (p1 vs p31). A ~3.5% growth is consistent with the moderating 2026 trend. | September 2026 YoY growth is near the recent 2026 monthly growth rate. | Evidence of a sharp acceleration or reversal in 2026 attendance growth. |
| a3 | September 2026 vs June 2026 daily-rate change factor | 0.98 | 0.94..1.02 | 0.8758..1.095 (widened) | ratio | m3 (m3) | June 2026 daily rate 81,264 (p58) is a record; September typically slightly lower than the June peak. A ~2% decline with wide range. | September 2026 daily rate is close to but slightly below the June 2026 record. | Evidence that September 2026 daily rate exceeds June 2026 or falls far below. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2,410,625 | ['p16'] / ['a1'] | [] |  | 0.25 | median_of_backtested |  |
| m2 | formula_mc | 2,394,142 | ['p46'] / ['a2'] | [] |  | 0.25 | median_of_backtested |  |
| m3 | formula_mc | 2,386,014 | ['p58'] / ['a3'] | [] |  | 0.25 | median_of_backtested |  |
| m4 | series_naive | 2,310,000 |  | [2025] | 0.044 | 0.25 | backtest |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **2,374,877** attendance, 80% interval [1,723,846, 3,271,778] attendance, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule inverse_backtest_error, weight on methods that use assumptions 0.75

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total A&E attendances across all A&E types in England during September 2026 is 2,374,877 attendance (80% model-based interval 1,723,846 to 3,271,778 attendance). This covers major A&E, single-specialty, minor injury units and walk-in centres for the full month.

Evidence: the most recent published month, July 2026, was 2,487,580 attendances; September 2025 was 2,310,000 attendances; the June 2026 daily rate was 81,264 attendances per day; and the prior September base was 2,210,000 attendances. Methods m1, m2 and m3 apply assumption factors 0.97, 1.035 and 0.98 respectively, while m4 carries forward the prior September. Only the observed points are data; the seasonal and growth factors are analyst assumptions, not observed.

Code combined the methods with equal weights (25%, 25%, 25%, 25%) because backtest years were too few to calibrate; the interval is a fixed default width, not demonstrated accuracy.

The main risk is a break in the 2026 trend or an unusual September surge/dip. Actual September 2026 daily counts would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 vs July 2026 total attendance change factor: 0.97 ratio, range 0.8669 to 1.084 (range widened by code); used by m1. Overturned by: Evidence that September 2026 exceeds July 2026 or falls far below.
- a2 September 2026 vs September 2025 YoY growth factor: 1.035 ratio, range 0.9255 to 1.157 (range widened by code); used by m2. Overturned by: Evidence of a sharp acceleration or reversal in 2026 attendance growth.
- a3 September 2026 vs June 2026 daily-rate change factor: 0.98 ratio, range 0.8758 to 1.095 (range widened by code); used by m3. Overturned by: Evidence that September 2026 daily rate exceeds June 2026 or falls far below.

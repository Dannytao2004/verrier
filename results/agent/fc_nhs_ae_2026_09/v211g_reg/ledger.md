# Evidence ledger: fc_nhs_ae_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the total number of A&E attendances in England in September 2026 (all A&E types, including minor injury units and walk-in centres), as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics.
- as_of: 2026-09-08
- Pinned target: Total number of A&E attendances (all A&E types, including major A&E departments, single-specialty A&E, minor injury units and walk-in centres) in England during September 2026, as reported in NHS England's monthly A&E Attendances and Emergency Admissions statistics (count of attendances, not unique  | unit attendances | period 2026-09-01..2026-09-30 | publisher NHS England (A&E Attendances and Emergency Admissions monthly statistics)

- Official value (scoring only, never shown to the agent): 2,440,000

## Directions and pages

### d1 [own_history] NHS England statistical publisher

Hypothesis: September 2026 total attendances will follow the level and seasonal pattern of recent Septembers and the most recent published months (through mid-2026), adjusted for trend. Own history gives the base level and month-of-year seasonal factor.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions monthly statistics 2026; A&E attendances England September 2025 total all types million; NHS England A&E monthly time series 2024-25 September attendances England time series xlsx; "September 2025" A&E attendances England "2.3 million" NHS England monthly statistics

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/06/aes-bore-the-brunt-as-heatwave-piled-pressure-on-nhs/` -> **snapshot** (snapshot 20260618085903); points raw/verified 12/12
  - p1 Total A&E attendances in England, May 2026 (record month) = **2,457,398** attendances (2026-05-01..2026-05-31) [keep: ] quote: "The NHS managed 2,457,398 attendances in A&E during May - up 25,000 on the previous record set in March earlier this year"
  - p2 Increase in A&E attendances, May 2026 over previous record (March 2026) = **25,000** attendances (2026-05-01..2026-05-31) [DISCARD: Redundant with p1: it is the increment over the previous record, not an independent attendance level, and adds no usable] quote: "up 25,000 on the previous record set in March earlier this year"
  - p3 A&E attendances managed within four hours of arrival, May 2026 = **1,860,000** attendances (2026-05-01..2026-05-31) [DISCARD: Within-four-hour attendance count for May 2026, a performance sub-count rather than total attendances; not usable as a l] quote: "1.86 million attendances were managed within four hours of arrival at hospital - the highest number for any May in a decade"
  - p4 Ambulance incidents handled, May 2026 (third busiest month ever) = **832,089** incidents (2026-05-01..2026-05-31) [DISCARD: Ambulance incidents, not A&E attendances; no reliable conversion to attendance total and not needed given direct attenda] quote: "after handling 832,089 incidents in May"
  - p5 Average daily patients experiencing corridor care in emergency departments = **2,241** patients per day (not stated (page dated 2026-06-01)) [DISCARD: Corridor-care patient count; not an attendance measure and no usable conversion.] quote: "on average, 2,241 patients each day experienced corridor care in emergency departments"
  - p6 Average daily patients receiving care in similar settings elsewhere in hospital = **669** patients per day (not stated (page dated 2026-06-01)) [DISCARD: Corridor-care elsewhere count; not an attendance measure.] quote: "while a further 669 patients received care in similar settings elsewhere in hospital"
  - p7 NHS overall elective waiting list = **7,220,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Elective waiting list; unrelated to A&E attendance volume.] quote: "The overall waiting list now stands at 7.22 million"
  - p8 Share of patients waiting within 18 weeks for elective treatment = **65** % (not stated (page dated 2026-06-01)) [DISCARD: 18-week elective share; unrelated to A&E attendance volume.] quote: "with 65% of patients waiting less within 18 weeks for elective treatment"
  - p9 Diagnostic tests delivered, April 2026 (highest ever for that month) = **2,500,000** diagnostic tests (2026-04-01..2026-04-30) [DISCARD: Diagnostic tests; unrelated to A&E attendance volume.] quote: "the NHS delivered 2.5 million diagnostic tests in April - the highest number ever recorded for that month"
  - p10 Reduction in waiting lists since government came into office = **400,000** patients (not stated (page dated 2026-06-01)) [DISCARD: Waiting-list reduction; unrelated to A&E attendance volume.] quote: "cut the waiting lists by more than 400,000 compared to when we came into government"
  - p11 Number of trusts accounting for more than half of corridor care cases in emergen = **20** trusts (not stated (page dated 2026-06-01)) [DISCARD: Count of trusts with corridor care; not an attendance measure.] quote: "20 trusts accounted for more than half of the cases of corridor care in emergency departments"
  - p12 Number of trusts accounting for more than two thirds of corridor care cases else = **20** trusts (not stated (page dated 2026-06-01)) [DISCARD: Count of trusts with corridor care elsewhere; not an attendance measure.] quote: "while 20 trusts also accounted for more than two thirds of cases of corridor care elsewhere in hospitals"
- `https://www.myhsn.co.uk/top-tip/nhs-winter-pressure-is-a-myth-what-the-data-really-shows/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Statistical-commentary-April-2026-G4dal2.pdf` -> **snapshot** (snapshot 20260515081905); points raw/verified 15/15
  - p13 Total A&E attendances (all types) in England, April 2026 = **2,345,329** attendances (2026-04-01..2026-04-30) [keep: ] quote: "The total number of attendances in April 2026 was 2,345,329."
  - p14 Year-on-year change in total A&E attendances (all types), April 2026 vs April 20 = **2.1** % (2026-04-01..2026-04-30) [keep: ] quote: "This was 2.1% higher when compared with April 2025."
  - p15 Year-on-year change in Type 1 A&E attendances, April 2026 vs April 2025 = **3** % (2026-04-01..2026-04-30) [keep: ] quote: "Attendances at Type 1 A&E departments were 3.0% higher compared with April 2025."
  - p16 Year-on-year change in Type 3 A&E attendances, April 2026 vs April 2025 = **0.3** % (2026-04-01..2026-04-30) [keep: ] quote: "Attendances at Type 3 departments were 0.3% higher compared with April 2025."
  - p17 Type 1 A&E attendance growth over last 3 months vs same period last year (to Apr = **2.3** % (2026-02-01..2026-04-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, was 2.3% higher"
  - p18 Type 3 A&E attendance growth over last 3 months vs same period last year (to Apr = **0.6** % (2026-02-01..2026-04-30) [keep: ] quote: "type 3 growth on the same basis was 0.6% higher."
  - p19 Type 1 A&E attendance growth over last 12 months vs preceding 12 months (to Apri = **2.3** % (2025-05-01..2026-04-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for Type 1 was 2.3%"
  - p20 Type 3 A&E attendance growth over last 12 months vs preceding 12 months (to Apri = **1.9** % (2025-05-01..2026-04-30) [keep: ] quote: "and for Type 3 was 1.9%."
  - p21 Booked A&E attendances in England, April 2026 = **73,777** attendances (2026-04-01..2026-04-30) [DISCARD: Booked attendances subset; too small and not needed as a separate input.] quote: "Last month there were 73,777 A&E attendances that had been booked."
  - p22 Emergency admissions in England, April 2026 = **525,660** emergency admissions (2026-04-01..2026-04-30) [keep: ] quote: "There were 525,660 emergency admissions in April 2026."
  - p23 A&E attendances admitted, transferred or discharged within 4 hours (all types),  = **1,803,787** attendances (2026-04-01..2026-04-30) [keep: ] quote: "The number of attendances admitted, transferred or discharged within 4 hours was 1,803,787."
  - p24 Type 1 attendances admitted, transferred or discharged within 4 hours, April 202 = **913,227** attendances (2026-04-01..2026-04-30) [keep: ] quote: "Of these, 913,227 were Type 1 attendances"
  - p25 Type 3 attendances admitted, transferred or discharged within 4 hours, April 202 = **840,154** attendances (2026-04-01..2026-04-30) [keep: ] quote: "There were 840,154 Type 3 attendances."
  - p26 Share of all A&E attendances admitted, transferred or discharged within 4 hours, = **76.9** % (2026-04-01..2026-04-30) [keep: ] quote: "76.9% of patients were admitted, transferred or discharged within 4 hours in all A&E Departments in April 2026"
  - p27 Share of all A&E attendances admitted, transferred or discharged within 4 hours, = **77.1** % (2026-03-01..2026-03-31) [keep: ] quote: "compared to 77.1% in March 2026 and 74.8% in April 2025."

### d2 [related_series] NHS England type-level breakdown

Hypothesis: Total attendances = type 1 + type 2 + type 3. If only type 1 (major A&E) is reliably reported, total can be reconstructed using the historical share of types 2 and 3 in the total.

Queries issued by the searcher: NHS England A&E attendances by type 1 2 3 monthly statistics; NHS England A&E attendances type 3 minor injury units walk-in centres monthly; NHS England A&E type breakdown September attendances; "July 2026" "type 1" "type 3" A&E attendances England; "August 2026" A&E attendances "type 1" "type 2" "type 3"; NHS England monthly A&E attendances 2025-26 type 1 type 2 type 3 time series; site:england.nhs.uk/statistics "A&E Attendances and Emergency Admissions" "August 2026"

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2023/10/Statistical-commentary-September-2023-abcdr.pdf` -> **snapshot** (snapshot 20260313184035); points raw/verified 15/15
  - p28 Total A&E attendances in England, September 2023 (all A&E types) = **2,166,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "The total number of attendances in September 2023 was 2,166,000, an increase of 7.8% on September 2022."
  - p29 Year-on-year growth in total A&E attendances, September 2023 vs September 2022 = **7.8** % (2023-09-01..2023-09-30) [keep: ] quote: "The total number of attendances in September 2023 was 2,166,000, an increase of 7.8% on September 2022."
  - p30 Year-on-year growth in type 1 A&E attendances, September 2023 vs September 2022 = **5.2** % (2023-09-01..2023-09-30) [keep: ] quote: "Attendances at type 1 A&E departments were 5.2% higher when compared with September 2022."
  - p31 Year-on-year growth in type 3 A&E attendances, September 2023 vs September 2022 = **13.1** % (2023-09-01..2023-09-30) [keep: ] quote: "Attendances at type 3 departments were 13.1% higher when compared with September 2022."
  - p32 Type 1 A&E attendance growth over last 3 months vs same period last year = **1.9** % (2023-07-01..2023-09-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, is 1.9% and type 3 growth on the same basis is 9.4%."
  - p33 Type 3 A&E attendance growth over last 3 months vs same period last year = **9.4** % (2023-07-01..2023-09-30) [keep: ] quote: "Type 1 growth over the last 3 months, compared to the same period last year, is 1.9% and type 3 growth on the same basis is 9.4%."
  - p34 Type 1 A&E attendance growth over last 12 months vs preceding 12 months = **1** % (2022-10-01..2023-09-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for type 1 is 1.0%, and for type 3 is 10.7%."
  - p35 Type 3 A&E attendance growth over last 12 months vs preceding 12 months = **10.7** % (2022-10-01..2023-09-30) [keep: ] quote: "Growth over the last 12 months, compared to the preceding 12 months, for type 1 is 1.0%, and for type 3 is 10.7%."
  - p36 Booked A&E attendances in September 2023 = **66,200** attendances (2023-09-01..2023-09-30) [DISCARD: Booked attendances subset for 2023; not needed.] quote: "This month there were 66,200 A&E attendances that had been booked, an increase of 14.0% on September 2022."
  - p37 Emergency admissions in September 2023 = **522,000** emergency admissions (2023-09-01..2023-09-30) [keep: ] quote: "There were 522,000 emergency admissions in the month, 7.1% higher than September 2022."
  - p38 Share of type 1 major A&E attendances requiring admission to hospital, September = **28** % (2023-09-01..2023-09-30) [DISCARD: Type 1 admission share; not needed for the total and not a clean conversion.] quote: "28.0% of patients that attended a type 1 major A&E department required admission to hospital, which compares to 27.2% for September 2022."
  - p39 Total attendances admitted, transferred or discharged within 4 hours, September  = **1,551,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "The number of attendances admitted, transferred or discharged within 4 hours was 1,551,000, a 21.8% increase on the equivalent figure for September 2022."
  - p40 Type 1 attendances admitted, transferred or discharged within 4 hours, September = **789,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "Of these, 789,000 were type 1 attendances, an increase of 21.5% on September 2022."
  - p41 Type 3 attendances admitted, transferred or discharged within 4 hours, September = **721,000** attendances (2023-09-01..2023-09-30) [keep: ] quote: "721,000 were type 3 attendances, an increase of 21.9% on September 2022."
  - p42 Share of patients seen within 4 hours in all A&E departments, September 2023 = **71.6** % (2023-09-01..2023-09-30) [keep: ] quote: "71.6% of patients were seen within 4 hours in all A&E departments this month compared to 73.0% in August 2023 and 71.1% in September 2022."
- `https://britishresilienceindex.com/deep-dive/ae-england` -> **snapshot** (snapshot 20260828220835); points raw/verified 15/15
  - p43 Total A&E attendances in England, July 2026 (all department types) = **2,487,580** attendances (2026-07-01..2026-07-31) [keep: ] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p44 Total A&E attendances in England, 12 months to July 2026 (cumulative) = **28,248,841** attendances (2025-08-01..2026-07-31) [keep: ] quote: "Across the 12 months to July 2026, there were 28,248,841 attendances."
  - p45 Total A&E attendances in England, full year 2011 (around) = **21,400,000** attendances (2011-01-01..2011-12-31) [DISCARD: 2011 annual total; too old and not needed given recent series.] quote: "By comparison, in 2011 there were around 21.4 million across the full year."
  - p46 Year-on-year change in total A&E attendances, July 2026 vs July 2025 = **3.3** % (2026-07-01..2026-07-31) [keep: ] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p47 Share of all A&E attendances seen within four hours, all department types, July  = **75.4** % (2026-07-01..2026-07-31) [keep: ] quote: "In July 2026, 75.4% of all attendances were seen within four hours across all department types, against the 95% NHS Constitution standard."
  - p48 Share of Type 1 (major A&E) attendances seen within four hours, July 2026 = **61.7** % (2026-07-01..2026-07-31) [keep: ] quote: "July 2026 All types 75.4%; Type 1 61.7%. Zero trusts with a Type 1 department met the 95% standard."
  - p49 Share of all A&E attendances seen within four hours, all department types, Novem = **97.2** % (2010-11-01..2010-11-30) [DISCARD: 2010 four-hour share; historical context only, not an attendance input.] quote: "In November 2010, the first full month on record, England's emergency departments saw 97.2% of patients across all department types within four hours"
  - p50 Share of Type 1 (major A&E) attendances seen within four hours, November 2010 = **95.9** % (2010-11-01..2010-11-30) [DISCARD: 2010 type 1 four-hour share; historical context only.] quote: "For Type 1 major departments the figure was 95.9%."
  - p51 Share of all A&E attendances seen within four hours, all department types, 2022 = **71.2** % (2022-01-01..2022-12-31) [DISCARD: 2022 four-hour share; not an attendance input.] quote: "By 2022, after the pressure of the pandemic and its aftermath, it was 71.2%."
  - p52 Share of all A&E attendances seen within four hours, all department types, 2019 = **84.7** % (2019-01-01..2019-12-31) [DISCARD: 2019 four-hour share; not an attendance input.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p53 Share of Type 1 (major A&E) attendances seen within four hours, 2019 = **76.3** % (2019-01-01..2019-12-31) [DISCARD: 2019 type 1 four-hour share; not an attendance input.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p54 Share of all A&E attendances seen within four hours, all department types, 2014  = **94.4** % (2014-01-01..2014-12-31) [DISCARD: 2014 four-hour share; not an attendance input.] quote: "2014 Last year England met the 95% standard nationally on all types performance (94.4% average; the standard was met in some individual months)."
  - p55 Number of trusts reporting Type 1 attendances, July 2026 = **120** trusts (2026-07-01..2026-07-31) [DISCARD: Count of trusts reporting type 1; not an attendance measure.] quote: "Of the 120 trusts reporting Type 1 attendances, the league table below shows the 15 under most pressure."
  - p56 12 hour decision-to-admit waits, England, July 2026 (single month) = **47,438** waits (2026-07-01..2026-07-31) [DISCARD: 12-hour waits; not an attendance measure.] quote: "In a single month, July 2026, there were 47,438 such waits."
  - p57 12 hour decision-to-admit waits, England, full year 2025 = **554,044** waits (2025-01-01..2025-12-31) [DISCARD: 12-hour waits annual; not an attendance measure.] quote: "In 2025 it happened 554,044 times, over four thousand times a day on average."

### d3 [related_series] NHS England emergency admissions and conversion

Hypothesis: Emergency admissions are a stable fraction of attendances; if admissions for September 2026 are forecastable, attendances can be derived by dividing by the historical admission-to-attendance ratio.

Queries issued by the searcher: NHS England A&E attendances and emergency admissions September 2025 monthly statistics; A&E attendance to emergency admission ratio England monthly statistics 2025; "ae-attendances-and-emergency-admissions-2025-26" NHS England statistics time series; NHS England A&E attendances and emergency admissions England level time series xlsx 2025-26

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2025-26/` -> **snapshot** (snapshot 20260508144434); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wired-gov.net/wg/news.nsf/articles/NHS+Confederation+Frustrating+rise+in+waiting+lists+despite+NHS+managing+record+elective+cases+over+the` -> **snapshot** (snapshot 20251118134117); points raw/verified 12/12
  - p58 Total A&E attendances across England in September = **2,310,000** attendances (2025-09-01..2025-09-30) [keep: ] quote: "There were 2.31 million attendances at A&Es across England in September, making it the busiest September on record"
  - p59 Emergency admissions in September (England) = **535,609** emergency admissions (2025-09-01..2025-09-30) [keep: ] quote: "There were 535,609 emergency admissions in September, another record for the month;"
  - p60 Share of A&E patients admitted, transferred or discharged within four hours in S = **75** % (2025-09-01..2025-09-30) [keep: ] quote: "Some 75.0% of patients were admitted, transferred or discharged from A&E departments within four hours in September"
  - p61 Share of A&E patients admitted, transferred or discharged within four hours in A = **75.9** % (2025-08-01..2025-08-31) [keep: ] quote: "down on the 75.9% in August;"
  - p62 Year-on-year increase in A&E attendances for September = **7** % (2025-09-01..2025-09-30) [keep: ] quote: "It is worrying to see A&E attendances nearly 7% higher than the same month last year"
  - p63 Total waiting list for procedures and appointments in August = **7,410,000** patients on waiting list (2025-08-01..2025-08-31) [DISCARD: Elective waiting list; unrelated.] quote: "The total waiting list for procedures and appointments increased to 7.41 million in August"
  - p64 Record elective cases managed this summer = **4,600,000** elective cases (2025-06-01..2025-08-31) [DISCARD: Elective cases; unrelated.] quote: "managing a record 4.6 million elective cases this summer"
  - p65 People waiting more than a year for treatment = **200,000** people (not stated (page dated 2025-10-10)) [DISCARD: Long-wait patients; unrelated.] quote: "there are still nearly 200,000 people who have been waiting more than a year for treatment"
  - p66 Category 2 ambulance average response time in September = **30.77** as written "30 minutes and 46 seconds", value check pending minutes (2025-09-01..2025-09-30) [DISCARD: Ambulance response time; not an attendance measure.] quote: "Category 2 ambulance average response time for September was 30 minutes and 46 seconds"
  - p67 Category 2 ambulance average response time in August = **27.05** as written "27 minutes and 03 seconds", value check pending minutes (2025-08-01..2025-08-31) [DISCARD: Ambulance response time; not an attendance measure.] quote: "worse than the 27 minutes and 03 seconds recorded in August"
  - p68 Category 1 ambulance average response time in September = **8.017** as written "8 minutes and 1 second", value check pending minutes (2025-09-01..2025-09-30) [DISCARD: Ambulance response time; not an attendance measure.] quote: "For Category 1 ambulances, the average response time was 8 minutes and 1 second in September"
  - p69 Category 1 ambulance average response time in August = **7.783** as written "7 minutes and 47 seconds", value check pending minutes (2025-08-01..2025-08-31) [DISCARD: Ambulance response time; not an attendance measure.] quote: "compared to 7 minutes and 47 seconds in August"
- `https://nhsproviders.org/resources/nhs-activity-tracker-august-2025/acute` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [physical_flow] NHS operational activity / daily sitrep

Hypothesis: Daily A&E attendance counts (e.g., from NHS England daily winter/operational situation reports or trust-level data) can be summed over September days to give a monthly total; daily averages times days in month.

Queries issued by the searcher: NHS England A&E attendances September 2024 monthly statistics total attendances; NHS England average daily A&E attendances England 2025 daily sitrep; "Monthly Operational Statistics" 2026 average daily attendances A&E NHS England; NHS England A&E Attendances and Emergency Admissions statistics 2026-27 monthly September 2025 2.31 million

- `https://www.england.nhs.uk/2026/07/warm-weather-world-cup-drives-record-nhs-demand-satisfaction-gps-bounce-back/` -> **snapshot** (snapshot 20260809130308); points raw/verified 13/12
  - p70 Average daily A&E attendances in England, June (record high) = **81,264** attendances per day (2026-06-01..2026-06-30) [keep: ] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p71 Threshold for average daily A&E attendances first exceeded in June (lower bound) = **80,000** attendances per day (2026-06-01..2026-06-30) [keep: ] quote: "Average daily A&E attendances exceeded 80,000 (81,264) for the first time ever in June"
  - p72 Extra day in May compared with June (days in month difference) = **1** days (2026-05-01..2026-05-31) [keep: ] quote: "despite May recording a slightly higher overall total due to having 1 extra day"
  - p73 Average daily 999 calls answered in June = **29,805** calls per day (2026-06-01..2026-06-30) [DISCARD: 999 calls; not an attendance measure.] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day - 10% higher than last June."
  - p74 Total 999 calls answered in June = **894,143** calls (2026-06-01..2026-06-30) [DISCARD: 999 calls; not an attendance measure.] quote: "There were 894,143 calls to 999 answered in June, an average of 29,805 calls per day - 10% higher than last June."
  - p75 Average daily ambulance incidents in June 2026 = **27,171** ambulance incidents per day (2026-06-01..2026-06-30) [DISCARD: Ambulance incidents; not an attendance measure.] quote: "There were almost 2,000 more ambulance incidents every day in June (27,171) - compared with June last year (25,322)"
  - p76 Share of A&E patients seen within 4 hours in June = **75** % (2026-06-01..2026-06-30) [keep: ] quote: "The number of people seen within 4 hours in A&E was 75%, just over half a percentage point down on June last year."
  - p77 Average daily instances of corridor care in emergency departments, nationally = **2,432** instances per day (not stated (page dated 2026-07-01)) [DISCARD: Corridor-care instances; not an attendance measure.] quote: "Nationally per day, there were on average 2,432 instances of Corridor Care in emergency departments"
  - p78 Average daily patients receiving corridor care elsewhere in hospital, nationally = **749** patients per day (not stated (page dated 2026-07-01)) [DISCARD: Corridor-care elsewhere; not an attendance measure.] quote: "and 749 patients receiving Corridor Care elsewhere in hospital."
  - p79 Overall NHS waiting list in May = **7,280,000** patients (2026-05-01..2026-05-31) [DISCARD: Elective waiting list; unrelated.] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p80 Increase in overall NHS waiting list from April to May = **60,153** patients (2026-05-01..2026-05-31) [DISCARD: Waiting-list change; unrelated.] quote: "The overall waiting list increased to 7.28 million in May, a rise of 60,153 compared to April."
  - p81 Share of patients waiting within 18 weeks for planned care in May = **65.6** % (2026-05-01..2026-05-31) [DISCARD: 18-week share; unrelated.] quote: "the number of people waiting within 18 weeks for planned care increased slightly to 65.6% of patients in May, compared with 65% in April."
- `https://thenhsalliance.org/resources/nhs-activity-tracker-july-2026/acute-sector` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/04/ECDS_Supplementary_Analysis_Statistical_Commentary_March_2026_V1THYY.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d5 [forecasts_markets] NHS planning / forecast publisher

Hypothesis: Published NHS or independent forecasts/planning assumptions for 2026-27 A&E activity can anchor the September 2026 level; annual planned attendances divided by 12 with seasonal adjustment.

Queries issued by the searcher: NHS England operational planning guidance 2026-27 A&E attendances activity; NHS England A&E attendances forecast 2026-27 annual activity; A&E attendances England monthly statistics 2025-26 total attendances September; "A&E" attendances July 2026 2.4 million NHS England monthly statistics; 2026/27 planning "activity" growth assumption "A&E attendances" percent NHS England medium term planning framework urgent care

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://www.nuffieldtrust.org.uk/resource/a-e-waiting-times` -> **snapshot** (snapshot 20260802210607); points raw/verified 15/13
  - p82 Total A&E attendances in England, Q4 2025/26 (quarterly total, all A&E types) = **6,900,000** attendances (2026-01-01..2026-03-31) [keep: ] quote: "In Q4 2025/26 there were 6.9 million A&E attendances."
  - p83 Total A&E attendances in England, Q3 2019/20 (quarterly total, pre-pandemic peak = **6,500,000** attendances (2019-10-01..2019-12-31) [keep: ] quote: "the total number of A&E attendances had been increasing over time, reaching almost 6.5 million in Q3 2019/20."
  - p84 Total A&E attendances in England, Q1 2020/21 (quarterly total, pandemic low) = **3,600,000** attendances (2020-04-01..2020-06-30) [keep: ] quote: "In Q1 2020/21, the total number of A&E attendances fell dramatically to 3.6 million"
  - p85 Share of type 1 A&E attendances admitted, transferred or discharged within four  = **60** % (2026-01-01..2026-03-31) [keep: ] quote: "60% of patients attending type 1 departments were admitted, transferred, or discharged within four hours"
  - p86 Share of type 2 and 3 A&E attendances admitted, transferred or discharged within = **97** % (2026-01-01..2026-03-31) [keep: ] quote: "for patients attending type 2 and 3 departments the proportion was 97%"
  - p87 Share of A&E attendances seen in four hours or less, England, May 2026 = **76** % (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, 76% of A&E attendances were seen in four hours or less."
  - p88 Interim four-hour target objective for March 2026 (share of A&E attendances) = **82** % (2026-03-01..2026-03-31) [DISCARD: Target objective share; not an attendance input.] quote: "was some way off the objective of 82% for March 2026"
  - p89 Interim four-hour target objective for March 2025 (share of A&E attendances) = **76** % (2025-03-01..2025-03-31) [DISCARD: Target objective share; not an attendance input.] quote: "The NHS fell short of the 76% objective for March 2025"
  - p90 Patients waiting over 12 hours from decision to admit to admission, England, May = **50,212** patients (2026-05-01..2026-05-31) [keep: ] quote: "In May 2026, 50,212 patients waited for more than 12 hours, representing 9% of the total number of emergency admissions"
  - p91 Share of total emergency admissions represented by patients waiting over 12 hour = **9** % (2026-05-01..2026-05-31) [keep: ] quote: "representing 9% of the total number of emergency admissions"
  - p92 Estimated share of all A&E attendances waiting over 12 hours to be admitted afte = **3** % (2026-05-01..2026-05-31) [DISCARD: 12-hour share; not an attendance input.] quote: "it was estimated that 3% of all patients attending A&E waited over 12 hours to be admitted after a decision to admit was made"
  - p93 Patients waiting over four hours from decision to admit to admission, England, J = **161,141** patients (2026-01-01..2026-01-31) [DISCARD: Decision-to-admit waits; not an attendance input.] quote: "This improved slightly to 161,141 waiting over four hours from decision to admission in January 2026."
  - p94 Patients waiting over four hours from decision to admit to admission, England, D = **170,283** patients (2022-12-01..2022-12-31) [DISCARD: Decision-to-admit waits; not an attendance input.] quote: "In December 2022, one in three patients (170,283) were waiting over four hours from decision to admission."
- `https://www.irejournals.com/paper-details/1722770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.nuh.nhs.uk/download/trust-board-open-meeting-combined-pack-thursday-12-march-2026pdf.pdf?ver=41257` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (period_end 2029-03-31 after as_of: 1; number: more than one number in value_as_written: 1)

### d6 [capacity_consumption] NHS trust / provider

Hypothesis: Total attendances can be built from trust-level monthly attendances summed across all trusts; a sample of large trusts scaled by their share of national activity gives the national total.

Queries issued by the searcher: NHS England A&E attendances monthly statistics provider level 2025; A&E attendances by trust monthly England 2026; "September 2025" A&E attendances England total 2.2 million NHS England monthly; NHS England "A&E Attendances and Emergency Admissions 2025-26" July 2026 published 13 August 2026

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://digital.nhs.uk/data-and-information/publications/statistical/provisional-accident-and-emergency-quality-indicators-for-england/september-2025-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://geraclinic.com/ae-performance` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [shocks] Policy/operational analyst

Hypothesis: Calendar effects (weekday composition of September 2026, bank holidays), weather, flu/COVID waves, and NHS pressures (strikes, closures) shift September attendances away from a naive trend; quantify exposure where measurable.

Queries issued by the searcher: September 2026 calendar bank holidays England; A&E attendances weekday effect England monthly statistics; NHS England A&E attendances September 2025 monthly statistics; NHS industrial action 2026 strikes impact A&E

- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.centralbedfordshire.gov.uk/contact-us/bank-holidays` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/hospital-accident--emergency-activity/2019-20/time-of-day` -> **snapshot** (snapshot 20201229103705); points raw/verified 0/0

### d8 [base_rates] Population/epidemiology analyst

Hypothesis: Attendances ≈ population × attendance rate per person per month; using England population and a stable per-capita monthly attendance rate (with seasonal factor) gives an independent cross-check.

Queries issued by the searcher: A&E attendances per 1000 population England annual attendance rate; England population mid-2025 estimate ONS; NHS England A&E attendances monthly statistics July 2026 total attendances million; "A&E attendances" England monthly time series 2025-26 total attendances September

- `https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://thenhsalliance.org/resources/nhs-activity-tracker-august-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] NHS England monthly A&E statistics

Hypothesis: A published August 2026 total (and any revised June/July 2026 totals) would pin the most recent level immediately before September and let a month-over-month seasonal factor carry it into September, materially tightening the forecast.

Queries issued by the searcher: NHS England A&E attendances July 2026 monthly statistics; england.nhs.uk statistics A&E attendances and emergency admissions 2026; "September 2025" A&E attendances England total all types monthly statistics 2.3 million; NHS England A&E attendances June 2026 total all types 2.46 million June 2026 statistics

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 12/9
  - p95 Latest publication month of NHS England A&E Attendances and Emergency Admissions = **2,026** month (2026-05-01..2026-05-31) [keep: ] quote: "Latest publication May 2026 published 11 June 2026"
  - p96 Statistical commentary May 2026 file size = **221** KB (2026-05-01..2026-05-31) [keep: ] quote: "Statistical commentary May 2026 (PDF, 221KB)"
  - p97 ECDS Supplementary Analysis Statistical Commentary May 2026 file size = **139** KB (2026-05-01..2026-05-31) [keep: ] quote: "ECDS Supplementary Analysis Statistical Commentary May 2026 (PDF, 139KB)"
  - p98 Monthly A&E April 2026 XLS file size = **417** KB (2026-04-01..2026-04-30) [keep: ] quote: "Monthly A&E April 2026 (XLS, 417KB)"
  - p99 Monthly A&E April 2026 CSV file size = **28** KB (2026-04-01..2026-04-30) [keep: ] quote: "Monthly A&E April 2026 (CSV, 28KB)"
  - p100 ECDS Activity Finalised May 2026 XLS file size = **732** KB (2026-05-01..2026-05-31) [keep: ] quote: "ECDS Activity Finalised May 2026 (XLS, 732KB)"
  - p101 ECDS Performance Finalised May 2026 XLS file size = **183** KB (2026-05-01..2026-05-31) [keep: ] quote: "ECDS Performance Finalised May 2026 (XLS, 183KB)"
  - p102 Statistical commentary April 2026 file size = **221** KB (2026-04-01..2026-04-30) [keep: ] quote: "Statistical commentary April 2026 (PDF, 221KB)"
  - p103 Number of acute provider footprint data changes in South East for April 2026 = **2** providers (2026-04-01..2026-04-30) [keep: ] quote: "a change has been made to the acute provider footprint data in the South East for 2 providers: RVV and RPA"
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/08/ECDS_Supplementary_Analysis_Statistical_Commentary_July_2026_3DNA6L.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.england.nhs.uk/2026/08/nhs-keeps-its-cool-as-temperatures-and-demand-soar/` -> **snapshot** (snapshot 20260819122744) **LEAK SENTINEL HIT ['(?<![\\d.,])7\\.27\\ million(?!\\d|[.,]\\d)'] (excluded)**; points raw/verified -/-
- `https://www.wired-gov.net/wg/news.nsf/print/NHS+Confederation+Frustrating+rise+in+waiting+lists+despite+NHS+managing+record+elective+cases+over+the+su` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (number: more than one number in value_as_written: 2; period year 2016 does not appear in the page text or URL (likely mis-dated): 1)

### b2 [own_history] seasonal pattern

Hypothesis: A clean September-vs-August and September-vs-July seasonal ratio from 2023-2025 would convert the known July 2026 level (p43) into a September 2026 estimate with a defensible month-of-year factor rather than a naive year-on-year scaling.

Queries issued by the searcher: NHS England A&E attendances September 2024 total monthly; A&E attendances August 2025 England total monthly statistics; "A&E Attendances and Emergency Admissions" September 2025 NHS England statistics; NHS England A&E attendances time series 2023 2024 2025 monthly total attendances September

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/` -> **snapshot** (snapshot 20260825194924); points raw/verified 0/0
- `https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2025/10/AE-statistical-commentary-September-2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions/for-september-2025-and-quarterly-rep` -> **snapshot** (snapshot 20251028011323); points raw/verified 0/0
- `https://www.myhsn.co.uk/top-tip/nhs-winter-pressure-is-a-myth-what-the-data-really-shows/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] type decomposition

Hypothesis: Type 1 and type 3 monthly totals for mid-2026 would let the total be reconstructed as type1+type2+type3 with the historical type-2/3 share, providing an independent check on the all-type series and resolving any definitional drift.

Queries issued by the searcher: NHS England A&E attendances type 1 type 3 July 2026 monthly statistics; A&E attendances by department type England monthly 2026 type 1 type 2 type 3; "July 2026" A&E attendances "type 3" England 2,487,580; NHS England A&E September 2025 type 1 type 2 type 3 attendances monthly table

- `https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2026-27/` -> **snapshot** (snapshot 20260611125437); points raw/verified 0/0
- `https://theobsidian.media/healthcare/intelligence/nhs` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://myemail.constantcontact.com/Capacityt.html?soid=1102665899193&aid=IzLKkVhhEdk` -> **snapshot** (snapshot 20260821155915); points raw/verified 8/6
  - p104 Type 1 major A&E attendances, England, latest year (2025/26) = **17,350,000** attendances (2025-04-01..2026-03-31) [keep: ] quote: "Type 1, major A&E attendances have risen about 18%, from 14.65m to 17.35m."
  - p105 Type 1 major A&E attendance growth since 2011/12, England = **18** % (2011-04-01..2026-03-31) [keep: ] quote: "Type 1, major A&E attendances have risen about 18%, from 14.65m to 17.35m."
  - p106 Type 3 urgent-care attendances, England, latest year (2025/26) = **10,020,000** attendances (2025-04-01..2026-03-31) [keep: ] quote: "Type 3 urgent-care attendances have risen 47%, from 6.83m to 10.02m."
  - p107 Type 3 urgent-care attendance growth since 2011/12, England = **47** % (2011-04-01..2026-03-31) [keep: ] quote: "Type 3 urgent-care attendances have risen 47%, from 6.83m to 10.02m."
  - p108 Type 1 A&E attendances year-on-year growth, England, July 2026 = **3.3** % (2026-07-01..2026-07-31) [keep: ] quote: "Type 1 attendances were up 3.3% year-on-year"
  - p109 Type 3 urgent-care attendances year-on-year growth, England, July 2026 = **3** % (2026-07-01..2026-07-31) [keep: ] quote: "Type 3 up 3.0%."
- `https://britishresilienceindex.com/deep-dive/ae-england` -> **snapshot** (snapshot 20260828220835); points raw/verified 15/15
  - p110 Total A&E attendances, all department types, England, July 2026 = **2,487,580** attendances (2026-07-01..2026-07-31) [DISCARD: Duplicate of p43 (same July 2026 total from the same release); keeping both would double-count one measurement.] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p111 Year-on-year change in total A&E attendances, July 2026 vs July 2025, England = **3.3** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p46 (same July 2026 y/y growth); redundant.] quote: "Total A&E attendances in July 2026 were 2,487,580, up 3.3% on July 2025."
  - p112 Total A&E attendances, all department types, England, 12 months to July 2026 = **28,248,841** attendances (2025-08-01..2026-07-31) [DISCARD: Duplicate of p44 (same 12-month cumulative total); redundant.] quote: "Across the 12 months to July 2026, there were 28,248,841 attendances."
  - p113 Total A&E attendances, all department types, England, full year 2011 = **21,400,000** attendances (2011-01-01..2011-12-31) [keep: ] quote: "By comparison, in 2011 there were around 21.4 million across the full year."
  - p114 Share of all A&E attendances seen within four hours, all department types, Engla = **75.4** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p47 (same July 2026 four-hour share); redundant.] quote: "In July 2026, 75.4% of all attendances were seen within four hours across all department types, against the 95% NHS Constitution standard."
  - p115 Share of Type 1 attendances seen within four hours, England, July 2026 = **61.7** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of p48 (same July 2026 Type 1 four-hour share); redundant.] quote: "July 2026 All types 75.4%; Type 1 61.7%. Zero trusts with a Type 1 department met the 95% standard."
  - p116 Share of all A&E attendances seen within four hours, all department types, Engla = **97.2** % (2010-11-01..2010-11-30) [DISCARD: Duplicate of p49 (same November 2010 four-hour share); redundant.] quote: "In November 2010, the first full month on record, England's emergency departments saw 97.2% of patients across all department types within four hours"
  - p117 Share of Type 1 attendances seen within four hours, England, November 2010 = **95.9** % (2010-11-01..2010-11-30) [DISCARD: Duplicate of p50 (same November 2010 Type 1 four-hour share); redundant.] quote: "For Type 1 major departments the figure was 95.9%."
  - p118 Share of all A&E attendances seen within four hours, all department types, Engla = **71.2** % (2022-01-01..2022-12-31) [DISCARD: Duplicate of p51 (same 2022 four-hour share); redundant.] quote: "By 2022, after the pressure of the pandemic and its aftermath, it was 71.2%."
  - p119 Share of all A&E attendances seen within four hours, all department types, Engla = **84.7** % (2019-01-01..2019-12-31) [DISCARD: Duplicate of p52 (same 2019 four-hour share); redundant.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p120 Share of Type 1 attendances seen within four hours, England, 2019 = **76.3** % (2019-01-01..2019-12-31) [DISCARD: Duplicate of p53 (same 2019 Type 1 four-hour share); redundant.] quote: "2019 All types performance had fallen to 84.7%. Type 1 at 76.3%."
  - p121 Share of all A&E attendances seen within four hours, all department types, Engla = **94.4** % (2014-01-01..2014-12-31) [DISCARD: Duplicate of p54 (same 2014 four-hour share); redundant.] quote: "2014 Last year England met the 95% standard nationally on all types performance (94.4% average; the standard was met in some individual months)."
  - p122 12 hour decision-to-admit waits, England, July 2026 = **47,438** waits (2026-07-01..2026-07-31) [DISCARD: Duplicate of p56 (same July 2026 12-hour waits); redundant.] quote: "In a single month, July 2026, there were 47,438 such waits."
  - p123 12 hour decision-to-admit waits, England, full year 2025 = **554,044** waits (2025-01-01..2025-12-31) [DISCARD: Duplicate of p57 (same 2025 12-hour waits); redundant.] quote: "In 2025 it happened 554,044 times, over four thousand times a day on average."
  - p124 Number of trusts reporting Type 1 attendances, England, July 2026 = **120** trusts (2026-07-01..2026-07-31) [DISCARD: Duplicate of p55 (same 120 trusts reporting Type 1); redundant.] quote: "Of the 120 trusts reporting Type 1 attendances, the league table below shows the 15 under most pressure."
- dropped by code checks: 2 (period year 2012 does not appear in the page text or URL (likely mis-dated): 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['nhs ae attendances', 'england ae september', 'ae attendances 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p13', 'p43', 'p44', 'p70'] All describe the same national all-type A&E attendance series in 2026 from NHS England-derived reporting; p1/p2 are the May record, p13 April, p43/p44 July and 12-month cumulative, p70 June daily aver
- corroborating: ['p28', 'p58', 'p62'] September all-type totals for 2023 (2.166m) and 2025 (2.31m) plus ~7% YoY growth in Sept 2025 are consistent with a rising September series; different years but same definition and publisher lineage.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p46'] Growth rates for type 1 and type 3 in 2026 (April and July) all point to modest low-single-digit growth, consistent with the level implied by p13, p43 and p70.
- corroborating: ['p22', 'p37', 'p59', 'p90', 'p91'] Emergency admissions figures for April 2026, Sept 2023, Sept 2025 and the 12-hour-wait share are mutually consistent with a stable admissions-to-attendance ratio of roughly 0.22-0.24; useful as a cros
- corroborating: ['p3', 'p23', 'p24', 'p25', 'p26', 'p27', 'p39', 'p40', 'p41', 'p42', 'p47', 'p48', 'p60', 'p61', 'p76', 'p85', 'p86', 'p87'] Four-hour performance shares and within-4-hour counts across 2023-2026 are internally consistent (all-type ~75-77%, type 1 ~60-62%); they do not directly give the attendance total but confirm the seri
- corroborating: ['p70', 'p71', 'p72'] June 2026 daily average 81,264 and the May-has-one-extra-day note jointly imply May total ≈ 2.457m (p1) and June ≈ 2.438m; consistent with p1 and p43.
- corroborating: ['p82', 'p83', 'p84'] Quarterly totals from Nuffield Trust (Q4 2025/26 6.9m; Q3 2019/20 6.5m; Q1 2020/21 3.6m) are consistent with the monthly series and give a long-run trend context; different aggregation but same defini
- corroborating: ['p1', 'p43'] May 2.457m and July 2.488m bracket the June daily-average-implied total; the three months form a coherent summer plateau.
- corroborating: ['p58', 'p28'] September 2023 2.166m and September 2025 2.31m imply ~3.3%/yr growth over two years, consistent with the 2026 growth rates in p14/p46.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p13', 'p43', 'p110'] All are total all-type A&E attendance levels for England in 2026 months (May, April, July). They are consistent with a level around 2.35–2.49m per month and rising through spring/summer; p43 and p110 
- corroborating: ['p28', 'p58'] September all-type totals for 2023 (2.166m) and 2025 (2.31m) form a consistent rising September series; p58 is described as the busiest September on record, consistent with growth from p28.
- corroborating: ['p43', 'p46', 'p108', 'p109', 'p111'] July 2026 total up 3.3% y/y, with Type 1 up 3.3% and Type 3 up 3.0%; these are internally consistent components of the same release and indicate broad-based growth, not independent confirmation.
- corroborating: ['p44', 'p112'] Duplicate statements of the 12-month cumulative total to July 2026 (28,248,841); same source, not independent.
- corroborating: ['p104', 'p106'] Type 1 (17.35m) and Type 3 (10.02m) 2025/26 annual totals sum to about 27.4m, close to the 12-month all-type total p44 (28.25m) once Type 2 and timing differences are allowed; broadly consistent scope
- corroborating: ['p70', 'p71', 'p72', 'p1'] June 2026 average daily attendances of 81,264 imply a June total near 2.44m, consistent with May's record 2.457m and the note that May's higher total reflects one extra day. These are consistent daily
- corroborating: ['p22', 'p59', 'p37'] Emergency admissions for April 2026 (525,660), September 2025 (535,609) and September 2023 (522,000) show a stable admissions level; useful as a cross-check on attendance scale via the admission ratio
- corroborating: ['p26', 'p27', 'p42', 'p47', 'p60', 'p61', 'p76', 'p87', 'p114'] Four-hour performance shares across months and years are mutually consistent in showing performance in the low-to-mid 70s percent; they are performance indicators, not attendance counts, and do not di
- corroborating: ['p82', 'p83', 'p84'] Quarterly attendance totals show the long-run level and pandemic dip; Q4 2025/26 at 6.9m implies roughly 2.3m per month, consistent with the 2026 monthly levels.
- corroborating: ['p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103'] Publication metadata confirming the latest official release was May 2026; they establish data availability and vintage but carry no attendance quantity.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p62'] Year-on-year growth rates for total, Type 1 and Type 3 across 2023 and 2026 are mutually consistent with modest positive growth (roughly 2–3% for Type 1, 0–3% for Type 3, higher in 2023). They support
- corroborating: ['p39', 'p40', 'p41', 'p23', 'p24', 'p25'] Within-four-hour attendance counts by type are internally consistent with the reported performance shares; they are not total attendance counts and are not used directly.
- corroborating: ['p113', 'p105', 'p107'] Long-run growth context (2011 total ~21.4m; Type 1 +18%, Type 3 +47% since 2011/12) supports the rising trend but is too distant to pin September 2026.
- corroborating: ['p85', 'p86', 'p90', 'p91', 'p122', 'p123', 'p124', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121'] Performance, waiting-time and trust-count context; consistent with the picture of high pressure but not direct attendance quantities.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 to July 2026 seasonal/trend ratio | 0.96 | 0.9..1.02 | 0.857..1.071 (widened) | ratio | m1 (m1) | September typically runs slightly below the July summer peak in all-type attendances; with a modest upward trend into autumn, a ratio near 0.96 is plausible. Range reflects uncertainty in both seasonality and trend. | The July 2026 level (p43) is a valid base and September 2026 follows the recent seasonal pattern. | Evidence that September 2026 attendances exceed July 2026 or fall more than 10% below it. |
| a2 | September 2026 vs September 2025 year-on-year growth factor | 1.03 | 0.99..1.07 | 0.9206..1.151 (widened) | ratio | m2 (m2) | Recent y/y growth has been around 3% (p46, p108, p109, p14), and September 2025 was itself up ~7% on 2024 (p62); a 3% growth factor is consistent with the recent trend, with a range spanning flat to 7%. | September 2025 (p58) is a valid base and the recent low-single-digit growth trend continues. | Evidence of a sharp acceleration or contraction in A&E demand in mid/late 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 2,389,985 | ['p43'] / ['a1'] | [] |  | 0.33 | median_of_backtested |  |
| m2 | formula_mc | 2,371,760 | ['p58'] / ['a2'] | [] |  | 0.33 | median_of_backtested |  |
| m3 | series_naive | 2,310,000 |  | [2025] | 0.064 | 0.33 | backtest |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **2,356,999** attendance, 80% interval [1,710,868, 3,247,147] attendance, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule inverse_backtest_error, weight on methods that use assumptions 0.67

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for total A&E attendances across all A&E types in England during September 2026 is 2,356,999 attendance (80% model-based interval 1,710,868 to 3,247,147 attendance). This covers major A&E, single-specialty, minor injury units and walk-in centres for the full month.

Evidence: the most recent all-type total, 2,487,580 attendances, was carried forward with a seasonal/trend ratio of 0.96 (range 0.857 to 1.071). A second route scaled the prior September figure, 2,310,000 attendances, by a year-on-year growth factor of 1.03 (range 0.9206 to 1.151). A naive anchor used 2,166,000 attendances and the recent September level. The three methods were weighted roughly equally (33%, 33%, 33%) because backtest evidence was too thin to discriminate between them.

Observed inputs are the published monthly totals; the seasonal ratio and growth factor are analyst assumptions, not observations. The main risk is an unusual September surge or a change in reporting scope. The most useful missing evidence would be a longer run of recent all-type monthly totals to calibrate seasonality and trend.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 to July 2026 seasonal/trend ratio: 0.96 ratio, range 0.857 to 1.071 (range widened by code); used by m1. Overturned by: Evidence that September 2026 attendances exceed July 2026 or fall more than [n] below it.
- a2 September 2026 vs September 2025 year-on-year growth factor: 1.03 ratio, range 0.9206 to 1.151 (range widened by code); used by m2. Overturned by: Evidence of a sharp acceleration or contraction in A&E demand in mid/late 2026.

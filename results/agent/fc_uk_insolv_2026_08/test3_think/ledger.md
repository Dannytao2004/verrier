# Evidence ledger: fc_uk_insolv_2026_08

- Question: Assume today is 2026-08-19. You know nothing published after this date. Estimate the number of registered company insolvencies in England and Wales in August 2026 (the headline monthly total of compulsory liquidations, creditors' voluntary liquidations, administrations, company voluntary arrangements and receivership appointments, in which the first three are seasonally adjusted), as it will be first reported in the Insolvency Service's monthly Company Insolvency Statistics release.
- as_of: 2026-08-19
- Pinned target: Number of registered company insolvencies in England and Wales in August 2026, as the headline monthly total first reported by the Insolvency Service: compulsory liquidations, creditors' voluntary liquidations, administrations, company voluntary arrangements and receivership appointments, with the s | unit registered company insolvencies | period 2026-08-01..2026-08-31 | publisher Insolvency Service

- Official value (scoring only, never shown to the agent): 1,946

## Directions and pages

### d1 [own_history] Insolvency Service statistical release archive

Hypothesis: The target is the next point in the same monthly series. The latest published July 2026 headline and component totals can be used as an anchor, multiplied by an August/July seasonal factor estimated from prior years, and adjusted for the recent year-on-year trend. Prior August observations and revisions constrain the plausible range.

Queries issued by the searcher: Insolvency Service monthly company insolvency statistics July 2026; company insolvency statistics August 2025 England Wales monthly Insolvency Service; gov.uk "company insolvencies" "July 2026" statistics commentary; Insolvency Service "August 2023" company insolvencies 1,9 England Wales monthly total July 2023

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-august-2025` -> **snapshot** (snapshot 20260804142926); points raw/verified 14/13
  - p1 Registered company insolvencies in England and Wales, August 2025 headline total = **2,048** registered company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 2,048 in August 2025"
  - p2 Registered company insolvencies in England and Wales, July 2025 headline total = **2,083** registered company insolvencies (2025-07-01..2025-07-31) [keep: ] quote: "2% lower than in July 2025 (2,083)"
  - p3 Registered company insolvencies in England and Wales, August 2024 headline total = **1,933** registered company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p4 Compulsory liquidations in England and Wales, August 2025 = **311** compulsory liquidations (2025-08-01..2025-08-31) [keep: ] quote: "Company insolvencies in August 2025 consisted of 311 compulsory liquidations"
  - p5 Creditors' voluntary liquidations (CVLs) in England and Wales, August 2025 = **1,600** creditors' voluntary liquidations (2025-08-01..2025-08-31) [keep: ] quote: "1,600 creditors' voluntary liquidations (CVLs)"
  - p6 Administrations in England and Wales, August 2025 = **121** administrations (2025-08-01..2025-08-31) [keep: ] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p7 Company voluntary arrangements (CVAs) in England and Wales, August 2025 = **16** company voluntary arrangements (2025-08-01..2025-08-31) [keep: ] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p8 Receivership appointments in England and Wales, August 2025 = **0** as written "no", value check pending receivership appointments (2025-08-01..2025-08-31) [keep: ] quote: "There were no receivership appointments."
  - p9 Month-on-month change in headline company insolvencies, August 2025 vs July 2025 = **2** % (2025-08-01..2025-08-31) [DISCARD: The quoted text says '2% lower' but the stored value is positive; sign-ambiguous and redundant with p1 and p2.] quote: "2% lower than in July 2025 (2,083)"
  - p10 Year-on-year change in headline company insolvencies, August 2025 vs August 2024 = **6** % (2025-08-01..2025-08-31) [keep: ] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p11 Month-on-month change in compulsory liquidations, August 2025 vs July 2025 = **9** % (2025-08-01..2025-08-31) [DISCARD: The quoted text says '9% lower' but the stored value is positive; sign-ambiguous and lacks the paired July compulsory-li] quote: "The number of compulsory liquidations was 9% lower than in July 2025"
  - p12 Company insolvency rate per 10,000 companies on effective register, 12 months en = **52.6** insolvencies per 10,000 companies (2024-09-01..2025-08-31) [keep: ] quote: "at a rate of 52.6 per 10,000 companies) entered insolvency between 1 September 2024 and 31 August 2025"
  - p13 Company insolvency rate per 10,000 companies on effective register, 12 months en = **55.5** insolvencies per 10,000 companies (2023-09-01..2024-08-31) [keep: ] quote: "a decrease from the 55.5 per 10,000 companies that entered insolvency in the 12 months ending 31 August 2024"
- `https://businesshelpline.uk/company-insolvency-statistics-august-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2009 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] Insolvency case-type decomposition / insolvency practitioner

Hypothesis: The headline total equals the sum of five case types. The dominant CVL series and the smaller compulsory liquidation and administration series can be forecast separately using recent levels, August seasonality and component-specific seasonal factors; summing the component forecasts gives the target and reveals composition risk.

Queries issued by the searcher: Insolvency Service company insolvency statistics monthly data tables 2026 creditors voluntary liquidation; company insolvency statistics England Wales June 2026 monthly Insolvency Service; "company insolvencies, July 2026" Insolvency Service gov.uk; company insolvency statistics August 2025 2,019 CVLs compulsory liquidations administrations CVA England Wales

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-june-2026/commentary-company-insolvency-statistics-june-2026` -> **snapshot** (snapshot 20260804142630); points raw/verified 15/14
  - p14 England and Wales total registered company insolvencies, June 2026 (seasonally a = **1,845** registered company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 1,845 in June 2026"
  - p15 England and Wales total registered company insolvencies, May 2026 (seasonally ad = **1,849** registered company insolvencies (2026-05-01..2026-05-31) [keep: ] quote: "similar to in May 2026 (1,849) but 10% lower than the same month in the previous year"
  - p16 England and Wales total registered company insolvencies, June 2025 (seasonally a = **2,048** registered company insolvencies (2025-06-01..2025-06-30) [keep: ] quote: "10% lower than the same month in the previous year (2,048 in June 2025)"
  - p17 England and Wales compulsory liquidations, June 2026 (seasonally adjusted) = **276** compulsory liquidations (2026-06-01..2026-06-30) [keep: ] quote: "Company insolvencies in June 2026 consisted of 276 compulsory liquidations"
  - p18 England and Wales creditors' voluntary liquidations (CVLs), June 2026 (seasonall = **1,364** creditors' voluntary liquidations (2026-06-01..2026-06-30) [keep: ] quote: "1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)"
  - p19 England and Wales administrations, June 2026 (seasonally adjusted) = **191** administrations (2026-06-01..2026-06-30) [keep: ] quote: "1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)"
  - p20 England and Wales company voluntary arrangements (CVAs), June 2026 (not seasonal = **14** company voluntary arrangements (2026-06-01..2026-06-30) [keep: ] quote: "191 administrations and 14 company voluntary arrangements (CVAs). There were no receivership appointments."
  - p21 CVL share of all England and Wales company insolvencies, June 2026 = **74** % (2026-06-01..2026-06-30) [keep: ] quote: "In June 2026, CVLs accounted for 74% of all company insolvencies."
  - p22 England and Wales compulsory liquidations, May 2026 (seasonally adjusted) = **281** compulsory liquidations (2026-05-01..2026-05-31) [keep: ] quote: "\| May 2026 \| 1,849 \| 281 \| 1,411 \| 132 \| 25 \| 0 \|"
  - p23 England and Wales creditors' voluntary liquidations (CVLs), May 2026 (seasonally = **1,411** creditors' voluntary liquidations (2026-05-01..2026-05-31) [keep: ] quote: "\| May 2026 \| 1,849 \| 281 \| 1,411 \| 132 \| 25 \| 0 \|"
  - p24 England and Wales administrations, May 2026 (seasonally adjusted) = **132** administrations (2026-05-01..2026-05-31) [keep: ] quote: "\| May 2026 \| 1,849 \| 281 \| 1,411 \| 132 \| 25 \| 0 \|"
  - p25 England and Wales company voluntary arrangements (CVAs), May 2026 = **25** company voluntary arrangements (2026-05-01..2026-05-31) [keep: ] quote: "\| May 2026 \| 1,849 \| 281 \| 1,411 \| 132 \| 25 \| 0 \|"
  - p26 England and Wales compulsory liquidations, April 2026 (seasonally adjusted) = **384** compulsory liquidations (2026-04-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 2,079 \| 384 \| 1,492 \| 182 \| 20 \| 1 \|"
  - p27 England and Wales administrations, April 2026 (seasonally adjusted) = **182** administrations (2026-04-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 2,079 \| 384 \| 1,492 \| 182 \| 20 \| 1 \|"
- `https://businesshelpline.uk/insolvency-statistics/procedures/administration/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d3 [related_series] Companies House registrar / stock-flow accounting

Hypothesis: Monthly insolvencies can be estimated as active registered company stock multiplied by a monthly insolvency rate. The stock is slow-moving and observable; the monthly rate has seasonal and cyclical patterns. Applying a defensible August rate to mid-2026 active company stock gives an independent estimate.

Queries issued by the searcher: Companies House register size 2025-26 active companies statistical release; Insolvency Service company insolvency rate per 10,000 companies England Wales 2025; "company insolvency statistics" July 2026 commentary Insolvency Service rate per 10,000; "incorporated companies in the UK" April to June 2026 effective register size

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/incorporated-companies-in-the-uk-january-to-march-2026/incorporated-companies-in-the-uk-january-to-march-2026` -> **snapshot** (snapshot 20260501210938); points raw/verified 15/15
  - p28 Total register size, UK companies register, end of March 2026 = **5,479,045** companies (2026-03-31..2026-03-31) [keep: ] quote: "the total register size at the end of March 2026 was 5,479,045, an increase of 28,681 companies (0.53%) compared with the end of December 2025"
  - p29 Effective register size (excludes companies in dissolution or liquidation), UK,  = **4,930,634** companies (2026-03-31..2026-03-31) [keep: ] quote: "there were 4,930,634 companies on the effective register at the end of March 2026, an increase of 53,653 companies (1.10%) compared with the end of December 2025"
  - p30 Companies in the process of dissolution or liquidation included in total registe = **548,411** companies (2026-03-31..2026-03-31) [keep: ] quote: "The total register includes companies in the process of dissolution and liquidation (548,411)."
  - p31 Quarterly change in total register size, England and Wales, end December 2025 to = **27,233** companies (2025-12-31..2026-03-31) [keep: ] quote: "an increase of 27,233 (0.54%) companies in England and Wales"
  - p32 Quarterly percentage change in total register size, England and Wales, end Decem = **0.54** % (2025-12-31..2026-03-31) [DISCARD: Percentage version redundant with p31 absolute quarterly change.] quote: "an increase of 27,233 (0.54%) companies in England and Wales"
  - p33 Quarterly change in total register size, Scotland, end December 2025 to end Marc = **1,804** companies (2025-12-31..2026-03-31) [keep: ] quote: "an increase of 1,804 (0.66%) companies in Scotland"
  - p34 Quarterly change in total register size, Northern Ireland, end December 2025 to  = **356** companies (2025-12-31..2026-03-31) [keep: ] quote: "a decrease of 356 (0.40%) companies in Northern Ireland"
  - p35 Incorporations, UK, January to March 2026 = **204,612** companies (2026-01-01..2026-03-31) [keep: ] quote: "between January and March 2026, there were 204,612 incorporations in the UK, an increase of 19,724 (10.67%) compared with October to December 2025"
  - p36 Dissolutions, UK, January to March 2026 = **190,836** companies (2026-01-01..2026-03-31) [keep: ] quote: "there were 190,836 dissolutions in the UK between January and March 2026, an increase of 14,120 (7.99%) compared with October to December 2025"
  - p37 Companies in the course of dissolution, UK, end of March 2026 = **438,990** companies (2026-03-31..2026-03-31) [keep: ] quote: "there were 438,990 companies in the course of dissolution at the end of March 2026, a decrease of 24,538 (5.29%) compared with the end of December 2025"
  - p38 Quarterly change in incorporations, England and Wales, January to March 2026 vs  = **17,695** companies (2026-01-01..2026-03-31) [keep: ] quote: "an increase of 17,695 (10.20%) in England and Wales"
  - p39 Quarterly change in dissolutions, England and Wales, January to March 2026 vs Oc = **13,319** companies (2026-01-01..2026-03-31) [keep: ] quote: "an increase of 13,319 (8.06%) in England and Wales"
  - p40 Quarterly change in companies in the course of dissolution, England and Wales, e = **22,269** companies (2025-12-31..2026-03-31) [keep: ] quote: "a decrease of 22,269 (5.14%) in England and Wales"
  - p41 Year-on-year change in effective register size, UK, end March 2025 to end March  = **58,341** companies (2025-03-31..2026-03-31) [keep: ] quote: "There was an increase of 58,341 companies (1.20%) on the effective register size for the UK since the end of March 2025."
  - p42 Year-on-year change in total register size, UK, end March 2025 to end March 2026 = **51,258** companies (2025-03-31..2026-03-31) [keep: ] quote: "There has been an increase of 51,258 companies (0.94%) on the total register for the UK since the end of the same quarter in 2025."
- `https://www.gov.uk/government/statistics/companies-register-activities-statistical-release-april-2025-to-march-2026/companies-register-activities-stat` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-august-2025/commentary-company-insolvency-statistics-august-2025` -> **snapshot** (snapshot 20260420040622); points raw/verified 15/15
  - p43 Registered company insolvencies in England and Wales, August 2025 (headline mont = **2,048** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1 for August 2025 headline total.] quote: "The number of registered company insolvencies in England and Wales was 2,048 in August 2025"
  - p44 Registered company insolvencies in England and Wales, August 2024 (same month pr = **1,933** registered company insolvencies (2024-08-01..2024-08-31) [DISCARD: Duplicate of p3 for August 2024 headline total.] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p45 Registered company insolvencies in England and Wales, July 2025 = **2,083** registered company insolvencies (2025-07-01..2025-07-31) [DISCARD: Duplicate of p2 for July 2025 headline total.] quote: "2% lower than in July 2025 (2,083)"
  - p46 Company insolvency rate, England and Wales, 12 months ending 31 August 2025 (per = **52.6** insolvencies per 10,000 companies on the effective register (2024-09-01..2025-08-31) [DISCARD: Duplicate of p12 for the 12-month insolvency rate ending August 2025.] quote: "One in 190 companies on the Companies House effective register (at a rate of 52.6 per 10,000 companies) entered insolvency between 1 September 2024 and 31 August 2025."
  - p47 Company insolvency rate, England and Wales, 12 months ending 31 August 2024 (per = **55.5** insolvencies per 10,000 companies on the effective register (2023-09-01..2024-08-31) [DISCARD: Duplicate of p13 for the 12-month insolvency rate ending August 2024.] quote: "a decrease from the 55.5 per 10,000 companies that entered insolvency in the 12 months ending 31 August 2024"
  - p48 Peak company insolvency rate, England and Wales, 2008-09 recession (per 10,000 c = **113** insolvencies per 10,000 companies on the effective register (not stated (page dated 2025-09-19)) [DISCARD: Duplicate peak-rate context already supplied by newer p115.] quote: "it remains much lower than the peak of 113.1 per 10,000 companies seen during the 2008-09 recession"
  - p49 Compulsory liquidations, England and Wales, August 2025 = **311** compulsory liquidations (2025-08-01..2025-08-31) [DISCARD: Duplicate of p4 for August 2025 compulsory liquidations.] quote: "Company insolvencies in August 2025 consisted of 311 compulsory liquidations"
  - p50 Creditors' voluntary liquidations (CVLs), England and Wales, August 2025 = **1,600** creditors' voluntary liquidations (2025-08-01..2025-08-31) [DISCARD: Duplicate of p5 for August 2025 CVLs.] quote: "1,600 creditors' voluntary liquidations (CVLs)"
  - p51 Administrations, England and Wales, August 2025 = **121** administrations (2025-08-01..2025-08-31) [DISCARD: Duplicate of p6 for August 2025 administrations.] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p52 Company voluntary arrangements (CVAs), England and Wales, August 2025 = **16** company voluntary arrangements (2025-08-01..2025-08-31) [DISCARD: Duplicate of p7 for August 2025 CVAs.] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p53 Receivership appointments, England and Wales, August 2025 = **0** as written "no", value check pending receivership appointments (2025-08-01..2025-08-31) [DISCARD: Duplicate of p8 for August 2025 receiverships.] quote: "There were no receivership appointments."
  - p54 Receivership appointments registered in the 12 months ending August 2025, Englan = **4** as written "four", value check ok receivership appointments (2024-09-01..2025-08-31) [keep: ] quote: "with only four being registered in the past 12 months ending August 2025"
  - p55 Company insolvency rate, Scotland, 12 months ending August 2025 (per 10,000 comp = **51** insolvencies per 10,000 companies on the effective register (2024-09-01..2025-08-31) [keep: ] quote: "The total insolvency rate in Scotland in the 12 months to August 2025 was 51.0 per 10,000 companies on the effective register"
  - p56 Company insolvency rate, Northern Ireland, 12 months ending August 2025 (per 10, = **37.2** insolvencies per 10,000 companies on the effective register (2024-09-01..2025-08-31) [keep: ] quote: "The total insolvency rate in the 12 months to August 2025 in Northern Ireland was 37.2 per 10,000 companies on the effective register"
  - p57 Average absolute month-to-month change in England and Wales company insolvencies = **11** % (not stated (page dated 2025-09-19)) [DISCARD: Older volatility statement; p84 provides a more recent comparable average absolute change.] quote: "less than the average absolute change of 11% between consecutive months over the past three years"

### d4 [administrative] London Gazette insolvency notices

Hypothesis: Insolvency notices published in the Gazette are an administrative trace of liquidations, administrations, CVAs and receiverships. Counts in August 2026, observed through 2026-08-19 plus an expected remainder, should move with the official total, though notice duplication, timing lag and type coverage require a bridge factor estimated from prior months.

Queries issued by the searcher: London Gazette insolvency notices August 2026 company insolvency; Insolvency Service monthly company insolvency statistics July 2026; Credit Connect "INSOLVENCY NOTICES" "Appointment of Administrators" August 2025 London Gazette; thegazette.co.uk insolvency notices search corporate insolvency notice counts by month

- `https://www.thegazette.co.uk/index.php/all-notices/content/company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cpa.co.uk/uk-business-news-today-19-august-2026-economy-markets-insolvencies/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.credit-connect.co.uk/news/insolvency-notices-appointment-of-administrators-august-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.credit-connect.co.uk/tag/appointment-of-administrators/` -> **snapshot** (snapshot 20260615203345); points raw/verified 0/0

### d5 [administrative] Court and Companies House filings

Hypothesis: Compulsory liquidations are driven by winding-up petitions and orders; CVLs follow creditor meetings and resolutions. Court petitions or orders and Companies House liquidation filings in August 2026 are leading or coincident administrative indicators. Historical conversion ratios translate them into case counts, with lags and coverage adjustments.

Queries issued by the searcher: winding up petitions August 2026 England Wales compulsory liquidation orders; Insolvency Service monthly insolvency statistics 2026 compulsory liquidations CVL; number of winding up petitions presented High Court 2026 statistics monthly HMRC; "winding up petitions" 2025 statistics ratio petitions to orders compulsory liquidations Insolvency Service

- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.4dcontact.com/uk-insolvency-intelligence-digest/` -> **snapshot** (snapshot 20260606171255); points raw/verified 2/2
  - p58 HMRC share of UK High Court winding-up petitions, early 2026 = **80** % (2026-01-01..2026-03-31) [keep: ] quote: "from over 80% in early 2026 to 62% in this period"
  - p59 HMRC share of UK High Court winding-up petitions, five-week period = **62** % (not stated (page dated 2026-06-02)) [keep: ] quote: "from over 80% in early 2026 to 62% in this period"
- `https://windinguppetitionsolicitors.co.uk/companies-winding-up-cause-list-5-august-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.k2-partners.com/publications/court/high-court-of-justice-chancery-division` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Trade body / economic forecaster

Hypothesis: A published 2026 annual or quarterly company insolvency forecast can be converted to August by multiplying by the historical August share of the annual total, or by the monthly pattern within the quarter. Forecasts provide an outside constraint if they are independent of the Insolvency Service headline.

Queries issued by the searcher: UK company insolvencies forecast 2026; R3 insolvency forecast 2026 company insolvencies; Insolvency Service company insolvencies August 2025 monthly statistics England and Wales; R3 responds to June 2026 insolvency statistics company insolvencies monthly

- `https://www.allianz-trade.com/en_GB/newsroom/2026-allianz-trade-insolvency-report.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-august-2025/commentary-company-insolvency-statistics-august-2025` -> **snapshot** (snapshot 20260420040622); points raw/verified 15/14
  - p60 Registered company insolvencies in England and Wales, August 2025 (headline mont = **2,048** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1.] quote: "The number of registered company insolvencies in England and Wales was 2,048 in August 2025"
  - p61 Registered company insolvencies in England and Wales, July 2025 (prior month tot = **2,083** registered company insolvencies (2025-07-01..2025-07-31) [DISCARD: Duplicate of p2.] quote: "2% lower than in July 2025 (2,083)"
  - p62 Registered company insolvencies in England and Wales, August 2024 (same month pr = **1,933** registered company insolvencies (2024-08-01..2024-08-31) [DISCARD: Duplicate of p3.] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p63 Compulsory liquidations, England and Wales, August 2025 = **311** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p4.] quote: "Company insolvencies in August 2025 consisted of 311 compulsory liquidations"
  - p64 Creditors' voluntary liquidations (CVLs), England and Wales, August 2025 = **1,600** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p5.] quote: "1,600 creditors' voluntary liquidations (CVLs)"
  - p65 Administrations, England and Wales, August 2025 = **121** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p6.] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p66 Company voluntary arrangements (CVAs), England and Wales, August 2025 = **16** registered company insolvencies (2025-08-01..2025-08-31) [DISCARD: Duplicate of p7.] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p67 CVL share of all company insolvencies, England and Wales, August 2025 = **78** % (2025-08-01..2025-08-31) [DISCARD: CVL share already derivable from p5/p1 and not needed separately.] quote: "In August 2025, CVLs accounted for 78% of all company insolvencies."
  - p68 Average absolute month-to-month change in company insolvencies, England and Wale = **11** % (not stated (page dated 2025-09-19)) [DISCARD: Duplicate of p57 and superseded by p84.] quote: "less than the average absolute change of 11% between consecutive months over the past three years"
  - p69 Company insolvency rate, England and Wales, 12 months ending 31 August 2025 = **52.6** insolvencies per 10,000 companies on the effective register (2024-09-01..2025-08-31) [DISCARD: Duplicate of p12.] quote: "at a rate of 52.6 per 10,000 companies) entered insolvency between 1 September 2024 and 31 August 2025"
  - p70 Company insolvency rate, England and Wales, 12 months ending 31 August 2024 = **55.5** insolvencies per 10,000 companies on the effective register (2023-09-01..2024-08-31) [DISCARD: Duplicate of p13.] quote: "a decrease from the 55.5 per 10,000 companies that entered insolvency in the 12 months ending 31 August 2024"
  - p71 Peak company insolvency rate, England and Wales, 2008-09 recession = **113** insolvencies per 10,000 companies on the effective register (not stated (page dated 2025-09-19)) [DISCARD: Duplicate of peak-rate context; newer p115 retained.] quote: "the peak of 113.1 per 10,000 companies seen during the 2008-09 recession"
  - p72 Typical magnitude of seasonal adjustment applied to monthly numbers, England and = **10** % (not stated (page dated 2025-09-19)) [keep: ] quote: "Seasonal adjustment in this publication typically results in numbers being adjusted by up to 10%."
  - p73 Seasonal adjustment uplift to April compulsory liquidation numbers when Easter f = **25** (range 20..30) as written "20-30%", value check pending % (not stated (page dated 2025-09-19)) [DISCARD: April-specific Easter seasonal-adjustment statement not applicable to August target.] quote: "the process of seasonal adjustment increases the April compulsory liquidation numbers by approximately 20-30%"
- `https://www.r3.org.uk/press-policy-and-research/news/more/32764/page/1/insolvency-rates-increase-as-middle-east-tensions-threaten-to-undermine-economi` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.r3.org.uk/wp-content/uploads/2026/07/Business-Health-Report-Q2-2026-FINAL.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### d7 [shocks] Macroeconomic and business-distress indicators

Hypothesis: Monthly insolvency counts respond to interest rates, inflation, GDP, unemployment and corporate distress indices. As of August 2026, current macro readings can shift the baseline from a pure seasonal extrapolation; historical elasticities or distressed-company shares provide the bridge. The direction depends on whether conditions are tighter or looser than the recent baseline.

Queries issued by the searcher: UK company insolvencies monthly 2026 Insolvency Service England and Wales; UK economy August 2026 interest rate inflation GDP unemployment; "Company insolvencies" July 2026 gov.uk commentary published 18 August 2026; Insolvency Service company insolvency statistics economic context interest rates inflation 2026 commentary

- `https://www.gov.uk/government/statistics/company-insolvencies-april-2026/commentary-company-insolvency-statistics-april-2026` -> **snapshot** (snapshot 20260617143546); points raw/verified 15/15
  - p74 Total registered company insolvencies, England and Wales, April 2026 (seasonally = **2,085** registered company insolvencies (2026-04-01..2026-04-30) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 2,085 in April 2026"
  - p75 Total registered company insolvencies, England and Wales, March 2026 (seasonally = **2,037** registered company insolvencies (2026-03-01..2026-03-31) [keep: ] quote: "2% higher than in March 2026 (2,037)"
  - p76 Total registered company insolvencies, England and Wales, April 2025 (seasonally = **2,028** registered company insolvencies (2025-04-01..2025-04-30) [keep: ] quote: "3% higher than the same month in the previous year (2,028 in April 2025)"
  - p77 Total registered company insolvencies, England and Wales, January 2026 (seasonal = **1,764** registered company insolvencies (2026-01-01..2026-01-31) [keep: ] quote: "\| Jan 2026 \| 1,764 \| 259 \| 1,333 \| 158 \| 13 \| 1 \|"
  - p78 Total registered company insolvencies, England and Wales, February 2026 (seasona = **1,907** registered company insolvencies (2026-02-01..2026-02-28) [keep: ] quote: "\| Feb 2026 \| 1,907 \| 261 \| 1,480 \| 156 \| 10 \| 0 \|"
  - p79 Compulsory liquidations, England and Wales, April 2026 (seasonally adjusted) = **371** compulsory liquidations (2026-04-01..2026-04-30) [DISCARD: Superseded by p26 for April 2026 compulsory liquidations.] quote: "Company insolvencies in April 2026 consisted of 371 compulsory liquidations"
  - p80 Creditors' voluntary liquidations (CVLs), England and Wales, April 2026 (seasona = **1,510** creditors' voluntary liquidations (2026-04-01..2026-04-30) [DISCARD: Older May-release April CVL figure; p26's July-release row indicates a revised CVL value.] quote: "1,510 creditors' voluntary liquidations (CVLs)"
  - p81 Administrations, England and Wales, April 2026 (seasonally adjusted) = **183** administrations (2026-04-01..2026-04-30) [DISCARD: Superseded by p27 for April 2026 administrations.] quote: "183 administrations, 20 company voluntary arrangements (CVAs) and one receivership appointment"
  - p82 Company voluntary arrangements (CVAs), England and Wales, April 2026 (not season = **20** company voluntary arrangements (2026-04-01..2026-04-30) [DISCARD: Duplicate April 2026 CVA count already present in the p26 quoted row.] quote: "There were 20 CVAs in April 2026, this was the same as in March 2026"
  - p83 Receivership appointments, England and Wales, April 2026 = **1** as written "one", value check pending receivership appointments (2026-04-01..2026-04-30) [DISCARD: Duplicate April 2026 receivership count already present in the p26 quoted row.] quote: "There was one receivership appointment in April 2026."
  - p84 Average absolute month-to-month change in England and Wales company insolvencies = **9** % (2023-04-01..2026-04-30) [keep: ] quote: "The increase of 2% compared to March 2026 is less than the average absolute change of 9% between consecutive months over the past three years."
  - p85 Connected Real Estate companies entering administration, March and April 2026 co = **200** connected companies (2026-03-01..2026-04-30) [keep: ] quote: "Numbers in March and April 2026 were affected by approximately 200 connected companies in the Real Estate sector entering administration in these months."
  - p86 Real Estate companies entering administration, April 2026 = **73** companies (2026-04-01..2026-04-30) [keep: ] quote: "73 companies in the Real Estate sector entering administration in April 2026"
  - p87 12-month rolling company insolvency rate, England and Wales, 12 months to April  = **51.8** insolvencies per 10,000 companies on the effective register (2025-05-01..2026-04-30) [keep: ] quote: "The company insolvency rate in the last 12 months was 51.8 per 10,000 companies on the effective register in England and Wales"
  - p88 12-month rolling company insolvency rate, England and Wales, 12 months to April  = **52.5** insolvencies per 10,000 companies on the effective register (2024-05-01..2025-04-30) [keep: ] quote: "This was a decrease from the 52.5 per 10,000 companies that entered insolvency in the 12 months ending 30 April 2025."
- `https://www.gov.uk/government/statistics/company-insolvencies-february-2026/commentary-company-insolvency-statistics-february-2026` -> **snapshot** (snapshot 20260516120441); points raw/verified 15/14
  - p89 Registered company insolvencies, England and Wales, February 2026 (headline mont = **1,878** registered company insolvencies (2026-02-01..2026-02-28) [DISCARD: Older vintage February 2026 headline; p78 is the later revised value.] quote: "The number of registered company insolvencies in England and Wales was 1,878 in February 2026"
  - p90 Registered company insolvencies, England and Wales, January 2026 (headline month = **1,749** registered company insolvencies (2026-01-01..2026-01-31) [DISCARD: Older vintage January 2026 headline; p77 is the later revised value.] quote: "7% higher than in January 2026 (1,749)"
  - p91 Registered company insolvencies, England and Wales, February 2025 (headline mont = **2,015** registered company insolvencies (2025-02-01..2025-02-28) [keep: ] quote: "7% lower than the same month in the previous year (2,015 in February 2025)"
  - p92 Registered company insolvencies, England and Wales, December 2025 (headline mont = **1,685** registered company insolvencies (2025-12-01..2025-12-31) [keep: ] quote: "\| Dec 2025 \| 1,685 \| 246 \| 1,318 \| 106 \| 15 \| 0 \|"
  - p93 Registered company insolvencies, England and Wales, November 2025 (headline mont = **1,842** registered company insolvencies (2025-11-01..2025-11-30) [keep: ] quote: "\| Nov 2025 \| 1,842 \| 251 \| 1,435 \| 137 \| 18 \| 1 \|"
  - p94 Average monthly number of company insolvencies, England and Wales, last four mon = **1,789** company insolvencies per month (2025-11-01..2026-02-28) [keep: ] quote: "The average monthly number over the last four months (1,789) was 10% lower than the average monthly number between the start of 2022 and the end of 2025 (1,982)."
  - p95 Average monthly number of company insolvencies, England and Wales, January 2022  = **1,982** company insolvencies per month (2022-01-01..2025-12-31) [keep: ] quote: "the average monthly number between the start of 2022 and the end of 2025 (1,982)"
  - p96 Compulsory liquidations, England and Wales, February 2026 (seasonally adjusted) = **249** compulsory liquidations (2026-02-01..2026-02-28) [DISCARD: Older February 2026 compulsory liquidation value; p108 is the later snapshot.] quote: "Company insolvencies in February 2026 consisted of 249 compulsory liquidations"
  - p97 Creditors' voluntary liquidations (CVLs), England and Wales, February 2026 (seas = **1,473** creditors' voluntary liquidations (2026-02-01..2026-02-28) [DISCARD: Older February 2026 CVL value; p109 is the later snapshot.] quote: "1,473 creditors' voluntary liquidations (CVLs)"
  - p98 Administrations, England and Wales, February 2026 (seasonally adjusted) = **146** administrations (2026-02-01..2026-02-28) [DISCARD: Older February 2026 administration value; p110 is the later snapshot.] quote: "146 administrations and 10 company voluntary arrangements (CVAs)"
  - p99 Company voluntary arrangements (CVAs), England and Wales, February 2026 (not sea = **10** company voluntary arrangements (2026-02-01..2026-02-28) [DISCARD: Older February 2026 CVA value; p111 is the later snapshot.] quote: "146 administrations and 10 company voluntary arrangements (CVAs)"
  - p100 Share of all company insolvencies accounted for by CVLs, England and Wales, Febr = **78** % (2026-02-01..2026-02-28) [DISCARD: Redundant CVL share for February 2026.] quote: "In February 2026, CVLs accounted for 78% of all company insolvencies."
  - p101 Average absolute month-to-month change in company insolvencies, England and Wale = **10** % (2023-03-01..2026-02-28) [DISCARD: Older volatility statement; p84 is more recent and comparable.] quote: "The increase of 7% compared to January 2026 is less than the average absolute change of 10% between consecutive months over the past three years."
  - p102 Company insolvency rate, England and Wales, 12 months ending February 2026 (per  = **51.5** insolvencies per 10,000 companies on the effective register (2025-03-01..2026-02-28) [DISCARD: Duplicate of p113 for the February 2026 12-month rate.] quote: "The company insolvency rate in the last 12 months was 51.5 per 10,000 companies on the effective register in England and Wales"
- `https://www.gov.uk/government/statistics/company-insolvencies-february-2026` -> **snapshot** (snapshot 20260804142925); points raw/verified 14/14
  - p103 Registered company insolvencies in England and Wales, February 2026 = **1,878** registered company insolvencies (2026-02-01..2026-02-28) [DISCARD: Duplicate of older February 2026 headline; p78 retained.] quote: "The number of registered company insolvencies in England and Wales was 1,878 in February 2026"
  - p104 Registered company insolvencies in England and Wales, January 2026 = **1,749** registered company insolvencies (2026-01-01..2026-01-31) [DISCARD: Duplicate of older January 2026 headline; p77 retained.] quote: "7% higher than in January 2026 (1,749)"
  - p105 Registered company insolvencies in England and Wales, February 2025 = **2,015** registered company insolvencies (2025-02-01..2025-02-28) [DISCARD: Duplicate of p91 for February 2025 headline.] quote: "7% lower than the same month in the previous year (2,015 in February 2025)"
  - p106 Year-on-year change in England and Wales company insolvencies, February 2026 vs  = **7** % (2026-02-01..2026-02-28) [DISCARD: Derived year-on-year percentage already represented by p78 and p105.] quote: "but 7% lower than the same month in the previous year (2,015 in February 2025)"
  - p107 Month-on-month change in England and Wales company insolvencies, February 2026 v = **7** % (2026-02-01..2026-02-28) [DISCARD: Derived month-on-month percentage already represented by p77 and p78.] quote: "The number of registered company insolvencies in England and Wales was 1,878 in February 2026, 7% higher than in January 2026"
  - p108 Compulsory liquidations in England and Wales, February 2026 = **249** compulsory liquidations (2026-02-01..2026-02-28) [keep: ] quote: "Company insolvencies in February 2026 consisted of 249 compulsory liquidations"
  - p109 Creditors' voluntary liquidations (CVLs) in England and Wales, February 2026 = **1,473** creditors' voluntary liquidations (2026-02-01..2026-02-28) [keep: ] quote: "1,473 creditors' voluntary liquidations (CVLs)"
  - p110 Administrations in England and Wales, February 2026 = **146** administrations (2026-02-01..2026-02-28) [keep: ] quote: "146 administrations and 10 company voluntary arrangements (CVAs)"
  - p111 Company voluntary arrangements (CVAs) in England and Wales, February 2026 = **10** company voluntary arrangements (2026-02-01..2026-02-28) [keep: ] quote: "146 administrations and 10 company voluntary arrangements (CVAs)"
  - p112 Receivership appointments in England and Wales, February 2026 = **0** as written "no", value check pending receivership appointments (2026-02-01..2026-02-28) [keep: ] quote: "There were no receivership appointments."
  - p113 Company insolvency rate, England and Wales, 12 months ending 28 February 2026 (p = **51.5** insolvencies per 10,000 companies (2025-03-01..2026-02-28) [keep: ] quote: "One in 194 companies on the Companies House effective register (at a rate of 51.5 per 10,000 companies) entered insolvency between 1 March 2025 and 28 February 2026."
  - p114 Company insolvency rate, England and Wales, 12 months ending 28 February 2025 (p = **52.3** insolvencies per 10,000 companies (2024-03-01..2025-02-28) [keep: ] quote: "a decrease from the 52.3 per 10,000 companies that entered insolvency in the 12 months ending 28 February 2025"
  - p115 Peak company insolvency rate, England and Wales, 2008-09 recession (per 10,000 c = **113** insolvencies per 10,000 companies (not stated (page dated 2026-03-17)) [keep: ] quote: "it remains much lower than the peak of 113.1 per 10,000 companies seen during the 2008-09 recession"
  - p116 Companies entering insolvency as a share of effective register, 12 months ending = **194** companies on effective register per insolvency (2025-03-01..2026-02-28) [keep: ] quote: "One in 194 companies on the Companies House effective register"
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b1 [own_history] Insolvency Service monthly Company Insolvency Statistics

Hypothesis: The July 2026 monthly release, if published before the 2026-08-19 cutoff, would provide the latest headline and component anchor and replace the June-based year-on-year extrapolation. It would show whether the May-June plateau near 1.85k continued into July, materially reducing the August forecast error.

Queries issued by the searcher: site:gov.uk company insolvency statistics July 2026; Insolvency Service monthly company insolvency statistics July 2026 England and Wales

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thegazette.co.uk/index.php/all-notices/content/company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.forvismazars.com/uk/en/services/financial-advisory/restructuring-and-insolvency-services/restructuring-insolvency-insights/monthly-insolve` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [administrative] The Gazette insolvency notices

Hypothesis: August 1-19 2026 Gazette notice counts, scaled by the historical share of full-August notices already observed by the 19th, would give a direct partial-period nowcast of August 2026 and test the June-based extrapolation. The key missing input is the historical coverage ratio by notice type.

Queries issued by the searcher: The Gazette insolvency notices August 2026; Gazette corporate insolvency notices search England Wales monthly counts; "The Gazette" insolvency notices monthly counts August 2025 corporate insolvency notices 2024 2023; thecompliancealliance appointment statistics weekly Gazette notices August 2026

- `https://www.k2-partners.com/publications/trends/2025-08` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://thecompliancealliance.co.uk/blog/appointment-statistics/` -> **snapshot** (snapshot 20260613151505); points raw/verified 11/11
  - p117 CVL change in Q1 2026 compared with Q1 2025 = **1** % (2026-01-01..2026-03-31) [keep: ] quote: "CVLs: 1% drop in Q1 2026"
  - p118 MVL change in Q1 2026 compared with Q1 2025 = **10** % (2026-01-01..2026-03-31) [DISCARD: MVLs are solvent-member liquidations and are not part of the headline registered company insolvency total.] quote: "MVLs: 10% up in Q1 2026"
  - p119 Gazette notices for connected ADM appointments skewing Q1 2026 increase = **156** Gazette notices (2026-01-01..2026-03-31) [keep: ] quote: "the 156 Gazette notices for the connected appointments skews the increase to 65% in Q1 2026"
  - p120 ADM increase in Q1 2026 compared with Q1 2025 including connected appointments = **65** % (2026-01-01..2026-03-31) [keep: ] quote: "skews the increase to 65% in Q1 2026"
  - p121 ADM increase in Q1 2026 compared with Q1 2025 excluding connected appointment bl = **27** % (2026-01-01..2026-03-31) [keep: ] quote: "even removing this blip, Q1 2026 is 27% higher than Q1 2025"
  - p122 BKY change in Q1 2026 compared with Q1 2025 = **23** % (2026-01-01..2026-03-31) [DISCARD: BKY bankruptcy change is a different insolvency measure and is not part of the company-insolvency headline.] quote: "BKYs: 23% higher in Q1 2026"
  - p123 WUC change in Q1 2026 compared with Q1 2025 = **7** % (2026-01-01..2026-03-31) [keep: ] quote: "WUCs: 7% higher."
  - p124 Highest weekly WUC count since Feb-2020, week ending 02/05/26 = **135** WUCs in a week (2026-04-27..2026-05-03) [keep: ] quote: "the week ending 02/05/26 saw the highest number of WUCs in any week since Feb-2020 at 135"
  - p125 Dissolutions over last four reported quarters = **750,000** dissolutions (not stated (page dated 2020-04-20)) [DISCARD: Aggregate dissolutions over four reported quarters are not insolvencies and are not needed for the target.] quote: "over the last four reported quarters, there were 750,000 dissolutions"
  - p126 Liquidations (all types) over last four reported quarters = **0** liquidations (not stated (page dated 2020-04-20)) [DISCARD: Stored value is zero while the quote says approximately 31,000 liquidations; extraction is unusable.] quote: "but only c.31,000 liquidations (all types)"
  - p127 Connected ADM appointments behind recent spikes = **230** as written "c.230", value check pending connected appointments (not stated (page dated 2020-04-20)) [DISCARD: The connected-appointment count is ambiguous and overlaps/conflicts with the clearer p85 and p119 evidence; page date co] quote: "the recent spikes in ADMs relate to c.230 connected appointments"
- `https://www.companydebt.com/data/winding-up-petition-tracker/` -> **snapshot** (snapshot 20260710210442); points raw/verified 11/11
  - p128 Winding-up petitions advertised, May 2026 (The Gazette) = **482** winding-up petitions (2026-05-01..2026-05-31) [keep: ] quote: "482 Winding-up petitions advertised May 2026The Gazette"
  - p129 Winding-up orders made, May 2026 (The Gazette) = **373** winding-up orders (2026-05-01..2026-05-31) [keep: ] quote: "373 Winding-up orders made May 2026The Gazette"
  - p130 Petitions dismissed, May 2026 (The Gazette) = **25** petitions dismissed (2026-05-01..2026-05-31) [keep: ] quote: "25 Petitions dismissed May 2026The Gazette"
  - p131 Total corporate insolvency notices, May 2026 (The Gazette) = **6,023** corporate insolvency notices (2026-05-01..2026-05-31) [keep: ] quote: "6,023 Total corporate insolvency notices May 2026The Gazette"
  - p132 Winding-up petitions advertised, May 2026 (notice breakdown table) = **482** winding-up petitions (2026-05-01..2026-05-31) [DISCARD: Duplicate of p128 winding-up petitions.] quote: "Winding-up petitionsCreditor applications to close a company 482"
  - p133 Winding-up orders, May 2026 (notice breakdown table) = **373** winding-up orders (2026-05-01..2026-05-31) [DISCARD: Duplicate of p129 winding-up orders.] quote: "Winding-up ordersCourt orders for compulsory liquidation 373"
  - p134 Liquidator appointments, May 2026 (across voluntary and compulsory cases) = **2,031** liquidator appointments (2026-05-01..2026-05-31) [keep: ] quote: "Liquidator appointmentsAcross voluntary and compulsory cases 2,031"
  - p135 CVL resolutions, May 2026 (creditors' voluntary liquidations) = **1,868** CVL resolutions (2026-05-01..2026-05-31) [keep: ] quote: "CVL resolutionsCreditors' voluntary liquidations 1,868"
  - p136 Administrator appointments, May 2026 (companies entering administration) = **138** administrator appointments (2026-05-01..2026-05-31) [keep: ] quote: "Administrator appointmentsCompanies entering administration 138"
  - p137 Petition dismissals, May 2026 (notice breakdown table) = **25** petition dismissals (2026-05-01..2026-05-31) [DISCARD: Duplicate of p130 petition dismissals.] quote: "Petition dismissalsPetitions struck out before any order 25"
  - p138 Share of advertised petitions followed by a winding-up order (stated as roughly  = **0.75** as written "three in four", value check pending winding-up orders per petition advertised (not stated (page dated 2026-06-19)) [keep: ] quote: "Roughly three in four advertised petitions are followed by a winding-up order."
- `https://financeclearly.com/uk-insolvency-notices-data/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [base_rates] Companies House register statistics

Hypothesis: The rate-based route currently uses the UK effective register because the E&W effective register level is missing. A mid-2026 E&W effective register level, or an updated E&W share of the UK effective register, would remove a large scope assumption. A more recent 12-month E&W insolvency rate through June/July 2026 would also reduce the August adjustment uncertainty.

Queries issued by the searcher: Companies House companies register statistics 2026 England and Wales effective register; Insolvency Service company insolvency rate 12 months ending June 2026 England and Wales; "company insolvencies" July 2026 Insolvency Service 12-month rate July 2026 published August 2026; "effective register" England and Wales "end June 2026" companies

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/incorporated-companies-in-the-uk-april-to-june-2026/incorporated-companies-in-the-uk-april-to-june-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.thegazette.co.uk/index.php/all-notices/content/company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['company', 'insolvency', 'august']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p14', 'p15', 'p77', 'p78', 'p75', 'p74', 'p92', 'p93'] Latest Insolvency Service headline levels (Nov 2025-Jun 2026) show a 2026 run-rate around 1.7k-2.1k, with May and June near 1.85k. p77/p78 are revised upward from older p90/p89; p74 is an older April 
- corroborating: ['p1', 'p2', 'p3', 'p16', 'p76', 'p91'] Historical anchors: Aug 2025 2048, Jul 2025 2083, Aug 2024 1933, Jun 2025 2048, Apr 2025 2028, Feb 2025 2015. Support a prior-year August level near 2.0k and a modest year-on-year decline into 2026.
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8'] August 2025 components sum exactly to p1 2048: compulsory 311, CVL 1600, administration 121, CVA 16, receivership 0. Confirms CVL dominance and negligible receiverships.
- corroborating: ['p17', 'p18', 'p19', 'p20', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'] 2026 component rows: June components sum to p14 1845; May components sum to p15 1849; April p26 row plus p27 components sum to about 2079, while older p74 total is 2085. Administrations are elevated v
- corroborating: ['p12', 'p13', 'p87', 'p88', 'p113', 'p114', 'p116'] England and Wales 12-month insolvency rates around 51-55 per 10,000, declining slightly; p116 gives the reciprocal one in 194. Supports a monthly flow near 2k, though the rate is an annual-average mea
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p33', 'p34', 'p35', 'p36', 'p37', 'p41', 'p42'] UK company register is growing; effective register was 4.93m at end March 2026. E&W quarterly change 27,233 versus Scotland 1,804 and NI -356 shows E&W dominates the UK register. Needed to convert UK 
- corroborating: ['p9', 'p10', 'p11', 'p21', 'p67', 'p100'] August 2025 was about 2% below July and 6% above August 2024; CVL shares were 74-78% across months. p9 is rounded: p1/p2 is about -1.7%, not exactly -2%.
- contextual: ['p58', 'p59'] HMRC share of High Court winding-up petitions fell from over 80% in early 2026 to 62% in a five-week period. Periods differ, so this is not a direct aggregate contradiction but indicates a shift in en
- corroborating: ['p84', 'p57', 'p68', 'p101', 'p94', 'p95'] Month-to-month volatility is 9-11%; the recent four-month average 1,789 is below the 2022-25 average 1,982, consistent with lower 2026 levels and wide monthly uncertainty.
- corroborating: ['p85', 'p86', 'p19'] Real-estate connected administrations (~200 in March-April, 73 in April) explain elevated 2026 administration counts and are relevant to component forecast risk.
- contextual: ['p72', 'p73'] Seasonal adjustment can move monthly numbers by up to 10%; April compulsory liquidations get a 20-30% Easter adjustment. The April-specific factor is not applicable to August, but it supports using th
- conflicting: ['p74', 'p26'] April 2026 total: p74 says 2,085 in the May release, while p26's quoted July-release row lists 2,079 (p26's value field is compulsory liquidations 384). Indicates a revision; latest vintage should be 
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p9', 'p10'] Historical August/July anchor: p1 is August 2025 headline, p2 July 2025, p3 August 2024; p10 confirms year-on-year increase. p9 has wording '2% lower' despite a positive value, so it is redundant and 
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p1'] August 2025 components p4-p8 decompose the p1 headline total; receiverships p8 are zero. These are the component anchors for a component-sum route.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21'] June 2026 headline p14 and components p17-p20 are internally consistent; p15 May 2026 and p16 June 2025 provide the recent plateau and year-on-year comparison. p21 gives the June 2026 CVL share.
- corroborating: ['p22', 'p23', 'p24', 'p25', 'p15'] May 2026 components p22-p25 decompose p15. This supports component-level forecasting and confirms that CVLs dominate the total.
- conflicting: ['p26', 'p27', 'p82', 'p83', 'p74', 'p76'] p26's quoted April 2026 row totals 2,079 and components p26/p27/p82/p83 sum to that later-vintage row, while p74's first-reported April 2026 headline is 2,085. This is a revision/vintage difference, n
- corroborating: ['p77', 'p78', 'p91', 'p92', 'p93', 'p94', 'p95'] Recent monthly target levels p77, p78, p92 and p93, together with Feb 2025 p91 and averages p94/p95, show 2026 below the 2022-25 average but fluctuating around a lower plateau. They are target-history
- conflicting: ['p78', 'p108', 'p109', 'p110', 'p111', 'p112'] p78 is the first-reported February 2026 headline with components summing to it, while later-snapshot components p108-p112 imply a revised February total. Keep vintages separate; do not mix p78 and p10
- corroborating: ['p28', 'p29', 'p30', 'p31', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p41', 'p42'] Companies House register evidence: p29 gives the UK effective register denominator, p28/p30 give total register and liquidation/dissolution components, and p31-p42 give recent E&W/UK register movement
- corroborating: ['p12', 'p13', 'p87', 'p88', 'p113', 'p114', 'p115', 'p116'] E&W insolvency rates decline from p13/p12 through p113 and p87; p116 gives the 'one in 194' 12-month rate to February 2026. p115 is a distant historical peak and only a loose bound. These support a de
- corroborating: ['p55', 'p56', 'p54'] p55 and p56 are Scotland/Northern Ireland rates, useful only as scope comparisons, not E&W observations. p54 shows receiverships are negligible in E&W and can be proxied by a small annual average.
- corroborating: ['p58', 'p59', 'p72', 'p84'] p58/p59 indicate HMRC's share of High Court winding-up petitions fell in 2026; p72 quantifies typical seasonal adjustment magnitude; p84 gives average absolute month-to-month volatility. These are con
- corroborating: ['p117', 'p119', 'p120', 'p121', 'p123', 'p124'] Q1/May 2026 administrative indicators: p117 shows CVLs roughly flat year-on-year in Q1; p119-p121 show administrations elevated partly by connected appointments, with p121 giving the cleaner ex-blip i
- corroborating: ['p85', 'p86', 'p119'] Connected real-estate administrations explain the administration spike: p85 gives the combined March-April connected-company effect, p86 the April real-estate subset, and p119 the Q1 Gazette notice co
- corroborating: ['p128', 'p129', 'p130', 'p131', 'p134', 'p135', 'p136', 'p138'] May 2026 Gazette administrative indicators: p128/p129/p130 are petition/order/dismissal counts, p131 is the broad notice total, p134 liquidator appointments, p135 CVL resolutions, p136 administrator a
- corroborating: ['p132', 'p133', 'p137'] Redundant duplicates of p128, p129 and p130 respectively; they add no new measurement.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | England and Wales share of UK effective register | 0.935 | 0.9..0.96 | 0.6573..1.315 (widened) | share | m3 (m3) | p29 is a UK effective-register denominator while the target is E&W only. E&W dominates the UK register; p31/p33/p34 give recent E&W, Scotland and Northern Ireland register movements but no E&W effective-register level. The share is placed near the high end because E&W is much larger than the other U | Used to convert the UK effective-register denominator in p29 to an E&W-equivalent denominator for the rate route. | An E&W effective-register share outside the stated range, or a published E&W effective-register level materially different from this share of p29. |
| a2 | August 2026 monthly rate adjustment versus 12-month average ending February 2026 | 0.93 | 0.85..1.02 | 0.6584..1.317 (widened) | factor | m3 (m3) | p116 gives the E&W 12-month rate to February 2026. p113, p87 and p12 show a generally declining 12-month rate into 2026, and recent monthly levels p14/p15 are below the year-earlier p16 comparison. August 2026 is therefore expected slightly below the 12-month average rate, with a wide range because  | Used to convert the 12-month average rate embedded in p116 into an August 2026 monthly-rate factor. | Evidence that August 2026 insolvency activity rebounded to or above the 12-month average ending February 2026. |
| a3 | Year-on-year factor for compulsory liquidations, August 2026 versus August 2025 | 0.95 | 0.75..1.25 | 0.75..1.25 | factor | m4 (m4) | p4 is the August 2025 compulsory-liquidation anchor. Recent 2026 compulsory levels p17 and p22 are below p4, while p26 includes an April spike. Winding-up activity indicators p128, p129, p138 and p124 point to elevated petitions/orders, but p58/p59 show the HMRC petition share falling. The factor is | Applied to p4 to project August 2026 compulsory liquidations. | A clear August 2026 petition/order collapse or a sustained compulsory-liquidation level far outside the recent p17/p22/p26 range. |
| a4 | Year-on-year factor for CVLs, August 2026 versus August 2025 | 0.9 | 0.8..1.02 | 0.8..1.02 | factor | m4 (m4) | p5 is the August 2025 CVL anchor. Recent 2026 CVL levels p18 and p23 are lower, and p117 indicates Q1 2026 CVLs were only slightly below Q1 2025. p135 is a gross May Gazette CVL-resolutions count and needs caution. The factor allows for a modest decline, not a repeat of the full headline year-on-yea | Applied to p5 to project August 2026 CVLs. | Sustained CVL resolutions at or above the 2025 level through summer 2026, or a sharper collapse than the stated range. |
| a5 | Year-on-year factor for administrations, August 2026 versus August 2025 | 1.15 | 0.85..1.5 | 0.85..1.5 | factor | m4 (m4) | p6 is the August 2025 administration anchor. Recent administration counts p19, p24, p27 and p110 are generally higher than p6. p121 indicates a Q1 2026 increase even excluding connected appointments, while p85/p86/p119 show a temporary connected real-estate administration blip. The factor is above o | Applied to p6 to project August 2026 administrations. | Evidence that the connected-administration effect fully unwinds and August 2026 administrations return to near the p6 level or below. |
| a6 | Year-on-year factor for CVAs, August 2026 versus August 2025 | 1 | 0.6..1.5 | 0.6..1.5 | factor | m4 (m4) | p7 is the August 2025 CVA anchor. Recent CVA counts p20, p25, p82 and p111 are volatile and show no clear trend. A flat central factor with a wide range reflects that volatility and the small count size. | Applied to p7 to project August 2026 CVAs. | A sustained run of CVA counts well above or below the 2025 and early-2026 range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_auto | 1,963 | ['p91', 'p76', 'p16', 'p1', 'p78', 'p74', 'p14'] / [] | [] |  | 0.00 | B1 of 4 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 1,844 | ['p14', 'p1', 'p16'] / [] | [] |  | 0.50 | B2 of 4 blocks; median of blocks: this block is the median |  |
| m3 | formula_mc | 1,825 | ['p29', 'p116'] / ['a1', 'a2'] | [] |  | 0.00 | B3 of 4 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m4 | formula_mc | 1,915 | ['p4', 'p5', 'p6', 'p7', 'p54'] / ['a3', 'a4', 'a5', 'a6'] | [] |  | 0.50 | B4 of 4 blocks; median of blocks: this block is the median |  |

- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Method details (computed by code):

- m1 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 1,963 (base month 2025-08 = 2,048 x growth 0.9583 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-02: 1,907 / 2,015; 2026-04: 2,085 / 2,028; 2026-06: 1,845 / 2,048). Data window 2025-02 (p91), 2025-04 (p76), 2025-06 (p16), 2025-08 (p1), 2026-02 (p78), 2026-04 (p74), 2026-06 (p14) (7 months used, not consecutive; last month 2026-06, 2 month(s) before the target; the run of consecutive months ending there is 8 long). Calibrated 80% interval 1,613 to 2,435; own 80% width x/÷1.23 (benchmark calibration, row yoy\|pairs3\|h2 of table bench-d12f86e0-1013c974)
- m2 formula_mc: p14 * (p1 / p16); Monte Carlo P10 to P90 1,344 to 2,524; result unit insolvency converted to insolvency; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p29 * a1 / p116 / k_months_per_year * a2; Monte Carlo P10 to P90 1,051 to 3,205; result unit (insolvency/month) * 1 month converted to insolvency; own 80% width x/÷1.75 (Monte Carlo of the formula inputs)
- m4 formula_mc: p4 * a3 + p5 * a4 + p6 * a5 + p7 * a6 + p54 / k_months_per_year; Monte Carlo P10 to P90 1,608 to 2,286; result unit (insolvency/month) * 1 month converted to insolvency; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 4 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 1,963 (width x/÷1.23, benchmark calibration); B2 = m2: 1,844 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 1,825 (width x/÷1.75, Monte Carlo of the formula inputs); B4 = m4: 1,915 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.45; Birge ratio 0.14 (not above one, so no widening); final width x/÷1.45.
- Seasonal naive baseline (not combined): 2,048 (2025-08, point p1, from m1); the estimate is -8.3% against it.

Result: central **1,879** insolvency, 80% interval [1,293, 2,730] insolvency, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for registered company insolvencies in England and Wales in August 2026 (headline monthly total, seasonally adjusted) is 1,879 insolvency (80% model-based interval 1,293 to 2,730 insolvency).

Evidence: an own-history year-on-year route (1,963) and a June-to-August seasonal bridge (1,844) use observed months including 1,845 registered company insolvencies, 2,048 registered company insolvencies and 2,048 registered company insolvencies. A component-sum route (1,915) scales August 2025 components 311 compulsory liquidations, 1,600 creditors' voluntary liquidations, 121 administrations and 16 company voluntary arrangements by assumed factors 0.95 to 1. A rate route (1,825) divides the effective register 4,930,634 companies by 194 companies on effective register per insolvency, adjusted by assumptions 0.935 and 0.93.

Code combined four overlapping-evidence blocks with equal weight per block, taking the median; the interval reflects the blocks' own widths.

Main risk: the August 2026 month is incomplete at cutoff, and the component year-on-year factors are assumptions. Better evidence would be July 2026 headline figures and component-level 2026 data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 England and Wales share of UK effective register: 0.935 share, range 0.6573 to 1.315 (range widened by code); used by m3. Overturned by: An E&W effective-register share outside the stated range, or a published E&W effective-register level materially different from this share of p29.
- a2 August 2026 monthly rate adjustment versus [n]-month average ending February 2026: 0.93 factor, range 0.6584 to 1.317 (range widened by code); used by m3. Overturned by: Evidence that August 2026 insolvency activity rebounded to or above the [n]-month average ending February 2026.
- a3 Year-on-year factor for compulsory liquidations, August 2026 versus August 2025: 0.95 factor, range 0.75 to 1.25; used by m4. Overturned by: A clear August 2026 petition/order collapse or a sustained compulsory-liquidation level far outside the recent p[n]/p[n]/p[n] range.
- a4 Year-on-year factor for CVLs, August 2026 versus August 2025: 0.9 factor, range 0.8 to 1.02; used by m4. Overturned by: Sustained CVL resolutions at or above the 2025 level through summer 2026, or a sharper collapse than the stated range.
- a5 Year-on-year factor for administrations, August 2026 versus August 2025: 1.15 factor, range 0.85 to 1.5; used by m4. Overturned by: Evidence that the connected-administration effect fully unwinds and August 2026 administrations return to near the p6 level or below.
- a6 Year-on-year factor for CVAs, August 2026 versus August 2025: 1 factor, range 0.6 to 1.5; used by m4. Overturned by: A sustained run of CVA counts well above or below the 2025 and early-2026 range.

Method details (computed by code):
- m1 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 1,963 (base month 2025-08 = 2,048 x growth 0.9583 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-02: 1,907 / 2,015; 2026-04: 2,085 / 2,028; 2026-06: 1,845 / 2,048). Data window 2025-02 (p91), 2025-04 (p76), 2025-06 (p16), 2025-08 (p1), 2026-02 (p78), 2026-04 (p74), 2026-06 (p14) (7 months used, not consecutive; last month 2026-06, 2 month(s) before the target; the run of consecutive months ending there is 8 long). Calibrated 80% interval 1,613 to 2,435; own 80% width x/÷1.23 (benchmark calibration, row yoy|pairs3|h2 of table bench-d12f86e0-1013c974)
- m2 formula_mc: p14 * (p1 / p16); Monte Carlo P10 to P90 1,344 to 2,524; result unit insolvency converted to insolvency; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p29 * a1 / p116 / k_months_per_year * a2; Monte Carlo P10 to P90 1,051 to 3,205; result unit (insolvency/month) * 1 month converted to insolvency; own 80% width x/÷1.75 (Monte Carlo of the formula inputs)
- m4 formula_mc: p4 * a3 + p5 * a4 + p6 * a5 + p7 * a6 + p54 / k_months_per_year; Monte Carlo P10 to P90 1,608 to 2,286; result unit (insolvency/month) * 1 month converted to insolvency; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 4 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 1,963 (width x/÷1.23, benchmark calibration); B2 = m2: 1,844 (width x/÷1.38, no error evidence, code's default width); B3 = m3: 1,825 (width x/÷1.75, Monte Carlo of the formula inputs); B4 = m4: 1,915 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.45; Birge ratio 0.14 (not above one, so no widening); final width x/÷1.45.
- Seasonal naive baseline (not combined): 2,048 (2025-08, point p1, from m1); the estimate is -8.3% against it.

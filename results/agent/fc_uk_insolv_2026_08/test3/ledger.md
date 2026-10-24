# Evidence ledger: fc_uk_insolv_2026_08

- Question: Assume today is 2026-08-19. You know nothing published after this date. Estimate the number of registered company insolvencies in England and Wales in August 2026 (the headline monthly total of compulsory liquidations, creditors' voluntary liquidations, administrations, company voluntary arrangements and receivership appointments, in which the first three are seasonally adjusted), as it will be first reported in the Insolvency Service's monthly Company Insolvency Statistics release.
- as_of: 2026-08-19
- Pinned target: Headline monthly total of registered company insolvencies in England and Wales reported in the Insolvency Service's monthly Company Insolvency Statistics release for August 2026: sum of compulsory liquidations, creditors' voluntary liquidations (CVLs), administrations, company voluntary arrangements | unit company insolvencies | period 2026-08-01..2026-08-31 | publisher Insolvency Service (UK)

- Official value (scoring only, never shown to the agent): 1,946

## Directions and pages

### d1 [own_history] Insolvency Service published monthly series

Hypothesis: The August 2026 headline total will be close to the recent seasonally adjusted monthly run-rate (roughly the 2025-2026 level) adjusted for any trend and for August-specific seasonal factors already embedded in the SA series; own history is the primary anchor.

Queries issued by the searcher: Insolvency Service monthly company insolvency statistics July 2026; company insolvencies England Wales August 2025 monthly Insolvency Service; gov.uk "company insolvencies" July 2026 commentary monthly company insolvencies by type table; "August 2023" company insolvencies England and Wales 2,308 monthly Insolvency Service August 2024 1,933

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-august-2025` -> **snapshot** (snapshot 20260804142926); points raw/verified 15/15
  - p1 Registered company insolvencies in England and Wales, August 2025 = **2,048** company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 2,048 in August 2025"
  - p2 Registered company insolvencies in England and Wales, July 2025 = **2,083** company insolvencies (2025-07-01..2025-07-31) [keep: ] quote: "2% lower than in July 2025 (2,083)"
  - p3 Registered company insolvencies in England and Wales, August 2024 = **1,933** company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p4 Compulsory liquidations, England and Wales, August 2025 = **311** company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "Company insolvencies in August 2025 consisted of 311 compulsory liquidations"
  - p5 Creditors' voluntary liquidations (CVLs), England and Wales, August 2025 = **1,600** company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "1,600 creditors' voluntary liquidations (CVLs)"
  - p6 Administrations, England and Wales, August 2025 = **121** company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p7 Company voluntary arrangements (CVAs), England and Wales, August 2025 = **16** company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "16 company voluntary arrangements (CVAs)"
  - p8 Receivership appointments, England and Wales, August 2025 = **0** as written "no", value check pending company insolvencies (2025-08-01..2025-08-31) [keep: ] quote: "There were no receivership appointments."
  - p9 Insolvency rate per 10,000 companies on effective register, 12 months ending 31  = **52.6** company insolvencies per 10,000 companies (2024-09-01..2025-08-31) [keep: ] quote: "at a rate of 52.6 per 10,000 companies) entered insolvency between 1 September 2024 and 31 August 2025"
  - p10 Insolvency rate per 10,000 companies on effective register, 12 months ending 31  = **55.5** company insolvencies per 10,000 companies (2023-09-01..2024-08-31) [keep: ] quote: "decrease from the 55.5 per 10,000 companies that entered insolvency in the 12 months ending 31 August 2024"
  - p11 Peak insolvency rate per 10,000 companies during 2008-09 recession = **113** company insolvencies per 10,000 companies (not stated (page dated 2025-09-19)) [keep: ] quote: "remains much lower than the peak of 113.1 per 10,000 companies seen during the 2008-09 recession"
  - p12 Share of companies on effective register entering insolvency, 12 months ending 3 = **190** companies entering insolvency per company on effective regis (2024-09-01..2025-08-31) [DISCARD: Already discarded in round 1; a share (1 in 190) that duplicates the rate information in p9/p84 and is not needed.] quote: "One in 190 companies on the Companies House effective register"
  - p13 Year-on-year change in registered company insolvencies, August 2025 vs August 20 = **6** % (2025-08-01..2025-08-31) [DISCARD: Already discarded; a percentage change that duplicates the level information in p1/p3.] quote: "6% higher than the same month in the previous year"
  - p14 Month-on-month change in registered company insolvencies, August 2025 vs July 20 = **2** % (2025-08-01..2025-08-31) [DISCARD: Already discarded; a percentage change duplicating p1/p2.] quote: "2% lower than in July 2025 (2,083)"
  - p15 Month-on-month change in compulsory liquidations, August 2025 vs July 2025 = **9** % (2025-08-01..2025-08-31) [DISCARD: Already discarded; a percentage change duplicating p4/p29.] quote: "The number of compulsory liquidations was 9% lower than in July 2025"
- `https://www.gov.uk/government/statistics/company-insolvencies-august-2025/commentary-company-insolvency-statistics-august-2025` -> **snapshot** (snapshot 20260420040622); points raw/verified 15/15
  - p16 Total registered company insolvencies, England and Wales, August 2025 (seasonall = **2,048** company insolvencies (2025-08-01..2025-08-31) [DISCARD: Already discarded; duplicate of p1 (same August 2025 SA headline).] quote: "The number of registered company insolvencies in England and Wales was 2,048 in August 2025"
  - p17 Total registered company insolvencies, England and Wales, July 2025 (seasonally  = **2,083** company insolvencies (2025-07-01..2025-07-31) [DISCARD: Already discarded; duplicate of p2 (same July 2025 SA headline).] quote: "2% lower than in July 2025 (2,083)"
  - p18 Total registered company insolvencies, England and Wales, August 2024 (seasonall = **1,933** company insolvencies (2024-08-01..2024-08-31) [DISCARD: Already discarded; duplicate of p3 (same August 2024 SA headline).] quote: "6% higher than the same month in the previous year (1,933 in August 2024)"
  - p19 Total registered company insolvencies, England and Wales, May 2025 (seasonally a = **2,228** company insolvencies (2025-05-01..2025-05-31) [keep: ] quote: "\| May 2025 \| 2,228 \| 353 \| 1,724 \| 137 \| 14 \| 0 \|"
  - p20 Total registered company insolvencies, England and Wales, June 2025 (seasonally  = **2,051** company insolvencies (2025-06-01..2025-06-30) [keep: ] quote: "\| Jun 2025 \| 2,051 \| 336 \| 1,583 \| 117 \| 15 \| 0 \|"
  - p21 Compulsory liquidations, England and Wales, August 2025 (seasonally adjusted) = **311** company insolvencies (2025-08-01..2025-08-31) [DISCARD: Already discarded; duplicate of p4 (August 2025 compulsory liquidations).] quote: "Company insolvencies in August 2025 consisted of 311 compulsory liquidations"
  - p22 Creditors' voluntary liquidations (CVLs), England and Wales, August 2025 (season = **1,600** company insolvencies (2025-08-01..2025-08-31) [DISCARD: Already discarded; duplicate of p5 (August 2025 CVLs).] quote: "1,600 creditors' voluntary liquidations (CVLs)"
  - p23 Administrations, England and Wales, August 2025 (seasonally adjusted) = **121** company insolvencies (2025-08-01..2025-08-31) [DISCARD: Already discarded; duplicate of p6 (August 2025 administrations).] quote: "121 administrations and 16 company voluntary arrangements (CVAs)"
  - p24 Company voluntary arrangements (CVAs), England and Wales, August 2025 (not seaso = **16** company insolvencies (2025-08-01..2025-08-31) [DISCARD: Already discarded; duplicate of p7 (August 2025 CVAs).] quote: "16 company voluntary arrangements (CVAs). There were no receivership appointments."
  - p25 Compulsory liquidations, England and Wales, August 2024 (seasonally adjusted) = **279** company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "\| Aug 2024 \| 1,933 \| 279 \| 1,520 \| 114 \| 20 \| 0 \|"
  - p26 Creditors' voluntary liquidations (CVLs), England and Wales, August 2024 (season = **1,520** company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "\| Aug 2024 \| 1,933 \| 279 \| 1,520 \| 114 \| 20 \| 0 \|"
  - p27 Administrations, England and Wales, August 2024 (seasonally adjusted) = **114** company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "\| Aug 2024 \| 1,933 \| 279 \| 1,520 \| 114 \| 20 \| 0 \|"
  - p28 Company voluntary arrangements (CVAs), England and Wales, August 2024 (not seaso = **20** company insolvencies (2024-08-01..2024-08-31) [keep: ] quote: "\| Aug 2024 \| 1,933 \| 279 \| 1,520 \| 114 \| 20 \| 0 \|"
  - p29 Compulsory liquidations, England and Wales, July 2025 (seasonally adjusted) = **342** company insolvencies (2025-07-01..2025-07-31) [keep: ] quote: "\| Jul 2025 \| 2,083 \| 342 \| 1,584 \| 145 \| 12 \| 0 \|"
  - p30 Administrations, England and Wales, July 2025 (seasonally adjusted) = **145** company insolvencies (2025-07-01..2025-07-31) [keep: ] quote: "\| Jul 2025 \| 2,083 \| 342 \| 1,584 \| 145 \| 12 \| 0 \|"

### d2 [related_series] Insolvency Service quarterly and annual series

Hypothesis: Quarterly company insolvency totals and the SA methodology give a smoothed level and seasonal pattern that can be interpolated to August 2026; quarterly Q3 2026 will contain August but is not yet published, so Q2 2026 and prior quarters constrain the level.

Queries issued by the searcher: Insolvency Service company insolvency statistics quarterly Q2 2026 England and Wales; Insolvency Service monthly company insolvency statistics seasonal adjustment methodology; "company insolvencies" July 2026 Insolvency Service 1,931 seasonally adjusted England and Wales; gov.uk company insolvency statistics tables 1a seasonally adjusted monthly England and Wales 2026

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/publications/insolvency-statistics-policy-and-procedures/insolvency-statistics-seasonal-adjustment-review-april-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.swgroup.com/insights-events/insights/insolvency-update-q2-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Companies House and business population data

Hypothesis: The stock of active companies and the rate of company dissolution/insolvency per thousand companies provide a base-rate route: expected insolvencies = active company stock x monthly insolvency rate, with the rate anchored on recent history.

Queries issued by the searcher: Companies House register statistics 2026 active companies on register; company insolvency rate per 1000 companies UK Insolvency Service monthly statistics; Insolvency Service company insolvency statistics July 2026 England and Wales 1,931 commentary; "company insolvencies" June 2026 England and Wales Insolvency Service monthly release effective register

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/incorporated-companies-in-the-uk-april-to-june-2026` -> **snapshot** (snapshot 20260812085714); points raw/verified 0/0
- `https://www.gov.uk/government/statistics/companies-register-activities-statistical-release-april-2025-to-march-2026` -> **snapshot** (snapshot 20260729042158); points raw/verified 0/0
- `https://www.gov.uk/government/statistics/company-insolvencies-april-2026/commentary-company-insolvency-statistics-april-2026` -> **snapshot** (snapshot 20260617143546); points raw/verified 15/15
  - p31 England and Wales 12-month rolling company insolvency rate per 10,000 companies  = **51.8** company insolvencies per 10,000 companies on the effective r (2025-05-01..2026-04-30) [keep: ] quote: "The company insolvency rate in the last 12 months was 51.8 per 10,000 companies on the effective register in England and Wales"
  - p32 England and Wales 12-month rolling company insolvency rate per 10,000 companies  = **52.5** company insolvencies per 10,000 companies on the effective r (2024-05-01..2025-04-30) [keep: ] quote: "This was a decrease from the 52.5 per 10,000 companies that entered insolvency in the 12 months ending 30 April 2025."
  - p33 England and Wales 12-month rolling company insolvency rate per 10,000 companies  = **51.7** company insolvencies per 10,000 companies on the effective r (2025-02-01..2026-01-31) [keep: ] quote: "\| Jan 2026 \| 51.7 \| 8.1 \| 39.9 \| 3.3 \| 0.4 \| 0.0 \|"
  - p34 England and Wales 12-month rolling company insolvency rate per 10,000 companies  = **51.5** company insolvencies per 10,000 companies on the effective r (2025-03-01..2026-02-28) [keep: ] quote: "\| Feb 2026 \| 51.5 \| 7.8 \| 39.9 \| 3.4 \| 0.4 \| 0.0 \|"
  - p35 England and Wales 12-month rolling company insolvency rate per 10,000 companies  = **51.6** company insolvencies per 10,000 companies on the effective r (2025-04-01..2026-03-31) [keep: ] quote: "\| Mar 2026 \| 51.6 \| 7.9 \| 39.6 \| 3.7 \| 0.4 \| 0.0 \|"
  - p36 England and Wales 12-month rolling CVL insolvency rate per 10,000 companies on t = **39.6** CVL insolvencies per 10,000 companies on the effective regis (2025-05-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 51.8 \| 7.9 \| 39.6 \| 3.9 \| 0.4 \| 0.0 \|"
  - p37 England and Wales 12-month rolling compulsory liquidation rate per 10,000 compan = **7.9** compulsory liquidations per 10,000 companies on the effectiv (2025-05-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 51.8 \| 7.9 \| 39.6 \| 3.9 \| 0.4 \| 0.0 \|"
  - p38 England and Wales 12-month rolling administration rate per 10,000 companies on t = **3.9** administrations per 10,000 companies on the effective regist (2025-05-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 51.8 \| 7.9 \| 39.6 \| 3.9 \| 0.4 \| 0.0 \|"
  - p39 England and Wales 12-month rolling CVA rate per 10,000 companies on the effectiv = **0.4** CVAs per 10,000 companies on the effective register (2025-05-01..2026-04-30) [keep: ] quote: "\| Apr 2026 \| 51.8 \| 7.9 \| 39.6 \| 3.9 \| 0.4 \| 0.0 \|"
  - p40 England and Wales peak 12-month rolling company insolvency rate per 10,000 compa = **113** company insolvencies per 10,000 companies on the effective r (not stated (page dated 2026-05-19)) [keep: ] quote: "it remains much lower than the peak of 113.1 per 10,000 companies seen during the 2008-09 recession"
  - p41 England and Wales total registered company insolvencies, April 2026 (seasonally  = **2,085** company insolvencies (2026-04-01..2026-04-30) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 2,085 in April 2026"
  - p42 England and Wales total registered company insolvencies, March 2026 (seasonally  = **2,037** company insolvencies (2026-03-01..2026-03-31) [keep: ] quote: "2% higher than in March 2026 (2,037)"
  - p43 England and Wales total registered company insolvencies, April 2025 (seasonally  = **2,028** company insolvencies (2025-04-01..2025-04-30) [keep: ] quote: "3% higher than the same month in the previous year (2,028 in April 2025)"
  - p44 England and Wales total registered company insolvencies, January 2026 (seasonall = **1,764** company insolvencies (2026-01-01..2026-01-31) [keep: ] quote: "\| Jan 2026 \| 1,764 \| 259 \| 1,333 \| 158 \| 13 \| 1 \|"
  - p45 England and Wales total registered company insolvencies, February 2026 (seasonal = **1,907** company insolvencies (2026-02-01..2026-02-28) [keep: ] quote: "\| Feb 2026 \| 1,907 \| 261 \| 1,480 \| 156 \| 10 \| 0 \|"

### d4 [shocks] Macro and policy environment

Hypothesis: Insolvency volumes respond to interest rates, energy costs, wage/National Insurance changes, and creditor enforcement behaviour; adverse macro conditions in 2026 would push August above the recent run-rate, while easing would push below.

Queries issued by the searcher: UK company insolvencies monthly 2026 Insolvency Service statistics; Bank of England base rate path market expectations mid-2026; Commentary Company Insolvency Statistics July 2026 gov.uk England and Wales; HMRC winding up petitions 2026 increase creditor enforcement

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mpamag.com/uk/mortgage-industry/market-trends/heres-what-to-expect-from-the-bank-of-england-for-the-rest-of-2026/583656` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ajbell.co.uk/group/news/bank-england-rate-setters-expected-hold-base-rate-375` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] Creditor and sector signals

Hypothesis: Sector-specific distress (construction, retail, hospitality) and creditor behaviour drive CVL and compulsory liquidation volumes; sector insolvency counts and creditor enforcement data can validate the level and direction.

Queries issued by the searcher: company insolvencies by sector 2026 construction retail hospitality Insolvency Service; Insolvency Service monthly company insolvency statistics 2026 compulsory liquidations CVL; company insolvency statistics July 2026 published 18 August 2026 compulsory liquidations CVL industry; winding up petitions presented England Wales 2026 creditor enforcement HMRC statistics

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026/commentary-company-insolvency-statistics-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hollowaydavies.co.uk/research/uk-sector-insolvency-league` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [forecasts_markets] Forecasters and prediction markets

Hypothesis: Published forecasts or market-implied expectations for UK insolvency volumes in 2026 provide an independent check on the level; if a prediction market exists for the August 2026 figure, its implied value is a direct signal.

Queries issued by the searcher: UK company insolvency forecast 2026 insolvency practitioners company failures; prediction market UK company insolvencies August 2026; company insolvencies July 2026 Insolvency Service monthly statistics; Polymarket UK company insolvencies 2026 market; "2026" forecast corporate insolvencies to rise number predicted annual total UK restructuring outlook

- `https://www.pwc.com/gx/en/deals/pdf/global-insolvency-report-2025-26-united-kingdom.pdf` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://www.antonybatty.com/zombie-firms-2026-speak-to-insolvency-practitioners-early/` -> **snapshot** (snapshot 20260515083032); points raw/verified 5/5
  - p46 Share of UK mid-market businesses at risk of being or becoming Zombie firms (res = **0.1667** as written "1 in 6", value check pending share of UK mid-market businesses (2025-02-01..2025-02-28) [keep: ] quote: "Research (Feb 2025) found that 1 in 6 UK mid‐market businesses (15.9%) are at risk of being or becoming Zombie firms"
  - p47 Percentage of UK mid-market businesses at risk of being or becoming Zombie firms = **15.9** % (2025-02-01..2025-02-28) [DISCARD: Already discarded; percentage version of p46, redundant.] quote: "1 in 6 UK mid‐market businesses (15.9%) are at risk of being or becoming Zombie firms"
  - p48 Increase in number of UK mid-market businesses at risk of being or becoming Zomb = **600** companies (2024-02-01..2025-02-28) [keep: ] quote: "an increase of more than 600 companies in just 12 months"
  - p49 Year-on-year rise in UK company insolvencies, October 2025 = **17** % (2025-10-01..2025-10-31) [keep: ] quote: "company insolvencies rose 17% year on year in October 2025, reaching their highest level since 2011."
  - p50 Year in which UK company insolvencies were last at the level reached in October  = **2,011** year (2011-01-01..2011-12-31) [DISCARD: Already discarded; a year label, not a usable quantity.] quote: "company insolvencies rose 17% year on year in October 2025, reaching their highest level since 2011."
- `https://www.ii.co.uk/news/uk-company-failures-rise-amid-fears-iran-war-will-push-collapses-up-al1773752840259923200` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bmmagazine.co.uk/in-business/zombie-companies-critical-distress-begbies-traynor-2026/` -> **snapshot** (snapshot 20260705002018); points raw/verified 7/6
  - p51 Increase in UK companies in critical financial distress, Q4 2025 vs Q4 2024 (Beg = **44** % (2025-10-01..2025-12-31) [keep: ] quote: "with a 44 per cent increase in companies classed as being in "critical financial distress" in the final three months of last year compared with the same period in 2024."
  - p52 Total UK companies in critical financial distress, Q4 2025 (Begbies Traynor Red  = **67,369** companies (2025-10-01..2025-12-31) [keep: ] quote: "In total, 67,369 companies were identified as facing critical distress, according to Begbies' latest Red Flag Alert report."
  - p53 Increase in hotels showing signs of critical distress over the past year = **54** % (2025-01-01..2025-12-31) [keep: ] quote: "Hotels saw a 54 per cent increase in businesses showing signs of critical distress over the past year"
  - p54 Increase in bars and restaurants showing signs of critical distress over the pas = **39** % (2025-01-01..2025-12-31) [keep: ] quote: "while bars and restaurants recorded a 39 per cent rise."
  - p55 Registered company insolvencies in 2025 (UK) = **23,938** company insolvencies (2025-01-01..2025-12-31) [keep: ] quote: "In 2025, there were 23,938 registered company insolvencies, broadly in line with 2024 levels."
  - p56 Change in company administrations in 2025 vs 2024 = **6** % (2025-01-01..2025-12-31) [keep: ] quote: "company administrations, where an insolvency practitioner takes control in an attempt to rescue the business or achieve a better outcome for creditors, fell by 6 per cent last year compared with 2024."
- dropped by code checks: 1 (period_end 2026-12-31 after as_of: 1)

### d7 [administrative] Insolvency Service operational data

Hypothesis: The Insolvency Service's operational statistics (e.g., redundancy payments, case volumes, DRO/breathing space) and Companies House filing data are administrative traces that correlate with insolvency processing volumes and can constrain the August 2026 level.

Queries issued by the searcher: Insolvency Service monthly company insolvency statistics 2026; Insolvency Service operational statistics 2026 redundancy payments cases; gov.uk "company insolvencies" July 2026 commentary insolvency service published August 2026; Companies House monthly statistics 2026 incorporations dissolutions

- `https://www.gov.uk./government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/news/insolvency-service-returns-427-million-to-the-economy-and-strengthens-action-against-financial-wrongdoing` -> **snapshot** (snapshot 20260714152812); points raw/verified 11/0
- `https://questions-statements.parliament.uk/written-questions/detail/2026-04-24/129688` -> **snapshot** (snapshot 20260430000629); points raw/verified 13/13
  - p57 HR1 (Advance Notice of Redundancy) forms recorded by the Insolvency Service, tot = **4,566** HR1 forms (2025-04-01..2026-03-31) [keep: ] quote: "In the financial year 2025/2026, the Insolvency Service recorded a total of 4,566 HR1 (Advance Notice of Redundancy) forms as follows:"
  - p58 HR1 forms recorded, April 2025 = **365** HR1 forms (2025-04-01..2025-04-30) [keep: ] quote: "\| April 2025 \| 365 \|"
  - p59 HR1 forms recorded, May 2025 = **382** HR1 forms (2025-05-01..2025-05-31) [keep: ] quote: "\| May 2025 \| 382 \|"
  - p60 HR1 forms recorded, June 2025 = **414** HR1 forms (2025-06-01..2025-06-30) [keep: ] quote: "\| June 2025 \| 414 \|"
  - p61 HR1 forms recorded, July 2025 = **407** HR1 forms (2025-07-01..2025-07-31) [keep: ] quote: "\| July 2025 \| 407 \|"
  - p62 HR1 forms recorded, August 2025 = **285** HR1 forms (2025-08-01..2025-08-31) [keep: ] quote: "\| August 2025 \| 285 \|"
  - p63 HR1 forms recorded, September 2025 = **345** HR1 forms (2025-09-01..2025-09-30) [keep: ] quote: "\| September 2025 \| 345 \|"
  - p64 HR1 forms recorded, October 2025 = **412** HR1 forms (2025-10-01..2025-10-31) [keep: ] quote: "\| October 2025 \| 412 \|"
  - p65 HR1 forms recorded, November 2025 = **412** HR1 forms (2025-11-01..2025-11-30) [keep: ] quote: "\| November 2025 \| 412 \|"
  - p66 HR1 forms recorded, December 2025 = **248** HR1 forms (2025-12-01..2025-12-31) [keep: ] quote: "\| December 2025 \| 248 \|"
  - p67 HR1 forms recorded, January 2026 = **396** HR1 forms (2026-01-01..2026-01-31) [keep: ] quote: "\| January 2026 \| 396 \|"
  - p68 HR1 forms recorded, February 2026 = **430** HR1 forms (2026-02-01..2026-02-28) [keep: ] quote: "\| February 2026 \| 430 \|"
  - p69 HR1 forms recorded, March 2026 = **470** HR1 forms (2026-03-01..2026-03-31) [keep: ] quote: "\| March 2026 \| 470 \|"
- `https://www.companywatch.net/the-insolvency-rate-has-a-denominator-problem-and-eccta-is-about-to-make-it-bigger/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (period year 2026 does not appear in the page text or URL (likely mis-dated): 11)

### b1 [own_history] Insolvency Service monthly release

Hypothesis: The May, June and July 2026 SA headline totals would extend the 2026 series (Jan-Apr known) to the month immediately before the target, letting series_auto run on a 13+ month consecutive series and pinning the trend/level for August 2026. This is the single most valuable missing input.

Queries issued by the searcher: Insolvency Service Company Insolvency Statistics July 2026 monthly company insolvencies England and Wales; "company insolvencies" June 2026 Insolvency Service monthly statistics; gov.uk "company insolvencies" July 2026 statistical tables data tables csv seasonally adjusted monthly series England and Wales; "company insolvencies" May 2026 1,849 Insolvency Service release 15 June 2026 compulsory liquidations CVLs

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/company-insolvencies-june-2026` -> **snapshot** (snapshot 20260804142636); points raw/verified 15/15
  - p70 Registered company insolvencies in England and Wales, June 2026 = **1,845** company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 1,845 in June 2026, similar to in May 2026 (1,849) but 10% lower than the same month in the previous year (2,048 in June 2025)."
  - p71 Registered company insolvencies in England and Wales, May 2026 = **1,849** company insolvencies (2026-05-01..2026-05-31) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 1,845 in June 2026, similar to in May 2026 (1,849) but 10% lower than the same month in the previous year (2,048 in June 2025)."
  - p72 Registered company insolvencies in England and Wales, June 2025 = **2,048** company insolvencies (2025-06-01..2025-06-30) [keep: ] quote: "The number of registered company insolvencies in England and Wales was 1,845 in June 2026, similar to in May 2026 (1,849) but 10% lower than the same month in the previous year (2,048 in June 2025)."
  - p73 Compulsory liquidations, England and Wales, June 2026 = **276** company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "Company insolvencies in June 2026 consisted of 276 compulsory liquidations, 1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)."
  - p74 Creditors' voluntary liquidations (CVLs), England and Wales, June 2026 = **1,364** company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "Company insolvencies in June 2026 consisted of 276 compulsory liquidations, 1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)."
  - p75 Administrations, England and Wales, June 2026 = **191** company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "Company insolvencies in June 2026 consisted of 276 compulsory liquidations, 1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)."
  - p76 Company voluntary arrangements (CVAs), England and Wales, June 2026 = **14** company insolvencies (2026-06-01..2026-06-30) [keep: ] quote: "Company insolvencies in June 2026 consisted of 276 compulsory liquidations, 1,364 creditors' voluntary liquidations (CVLs), 191 administrations and 14 company voluntary arrangements (CVAs)."
  - p77 Change in CVLs, June 2026 vs May 2026 = **3** % (2026-06-01..2026-06-30) [keep: ] quote: "The number of CVLs was 3% lower than in May 2026, and 15% lower than in June 2025."
  - p78 Change in CVLs, June 2026 vs June 2025 = **15** % (2026-06-01..2026-06-30) [keep: ] quote: "The number of CVLs was 3% lower than in May 2026, and 15% lower than in June 2025."
  - p79 Change in compulsory liquidations, June 2026 vs May 2026 = **2** % (2026-06-01..2026-06-30) [keep: ] quote: "Compulsory liquidations in June 2026 were 2% lower than in May 2026 and 15% lower than in June 2025."
  - p80 Change in compulsory liquidations, June 2026 vs June 2025 = **15** % (2026-06-01..2026-06-30) [keep: ] quote: "Compulsory liquidations in June 2026 were 2% lower than in May 2026 and 15% lower than in June 2025."
  - p81 Change in CVAs, June 2026 vs May 2026 = **44** % (2026-06-01..2026-06-30) [keep: ] quote: "CVAs were 44% lower than in May 2026."
  - p82 Change in administrations, June 2026 vs May 2026 = **45** % (2026-06-01..2026-06-30) [keep: ] quote: "Administrations in June 2026 were 45% higher than in May 2026."
  - p83 Connected real estate companies entering administration, June 2026 (approximate) = **60** companies (2026-06-01..2026-06-30) [keep: ] quote: "Numbers of administrations in June 2026 were affected by approximately 60 connected companies in the real estate sector entering administration."
  - p84 Company insolvency rate, 12 months ending 30 June 2026 = **50.5** company insolvencies per 10,000 companies (2025-07-01..2026-06-30) [keep: ] quote: "One in 198 companies (at a rate of 50.5 per 10,000 companies) entered insolvency between 1 July 2025 and 30 June 2026."
- `https://www.iqinsolvency.com/uk-insolvency-statistics/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.forvismazars.com/uk/en/services/financial-advisory/restructuring-and-insolvency-services/restructuring-insolvency-insights/monthly-insolve` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [base_rates] Companies House register

Hypothesis: The number of companies on the effective register in mid-2026 combined with the ~51.5 per 10,000 annual rate (p31-p35) gives an independent level check via expected monthly insolvencies = register x rate/12; it would resolve whether the 2026 level is drifting up or flat.

Queries issued by the searcher: Companies House statistical release "Companies register activities 2025-26"; Companies House monthly incorporation and dissolution data 2026; Insolvency Service company insolvency statistics July 2026 monthly release rate per 10,000 companies; "effective register" England and Wales companies June 2026 Companies House insolvency rate per 10,000

- `https://www.gov.uk/government/statistics/companies-register-activities-statistical-release-april-2025-to-march-2026/companies-register-activities-stat` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk./government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.uk/government/statistics/incorporated-companies-in-the-uk-april-to-june-2026/incorporated-companies-in-the-uk-april-to-june-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.companywatch.net/the-insolvency-rate-has-a-denominator-problem-and-eccta-is-about-to-make-it-bigger/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [shocks] Macro/creditor behaviour

Hypothesis: HMRC/creditor winding-up petition volumes and Bank of England Bank Rate path through mid-2026 would indicate whether compulsory liquidations (currently ~260-340/month) are trending up, the component most sensitive to enforcement and the main source of upside risk to the August total.

Queries issued by the searcher: Bank of England Bank Rate decision August 2026 Monetary Policy Committee; Insolvency Service monthly company insolvency statistics July 2026 compulsory liquidations; HMRC winding-up petitions statistics 2026 number presented quarterly; "winding-up petitions" 2026 rise HMRC creditor enforcement insolvency courts

- `https://www.gov.uk/government/statistics/company-insolvencies-july-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businessmanchester.co.uk/2026/07/24/winding-up-petitions-hit-three-year-high-as-creditors-lose-patience-court-data-reveals/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://londonlovesbusiness.com/hmrc-turns-up-the-heat-on-uk-businesses-as-tax-debt-crackdown-intensifies/` -> **snapshot** (snapshot 20260730025507); points raw/verified 5/5
  - p85 HMRC winding-up petitions applied for against companies over unpaid tax debts, p = **4,761** companies (not stated (page dated 2026-07-29)) [keep: ] quote: "HMRC applied to wind up 4,761 companies over unpaid tax debts during the past year"
  - p86 Year-on-year increase in HMRC winding-up petitions applied for, past year = **31** % (not stated (page dated 2026-07-29)) [keep: ] quote: "a 31 per cent increase on the previous 12 months"
  - p87 HMRC winding-up petitions resulting in court-ordered liquidations, past year = **2,400** companies (not stated (page dated 2026-07-29)) [keep: ] quote: "nearly 2,400 of those petitions ultimately resulted in court-ordered liquidations"
  - p88 HMRC tax debt in arrears (stock) = **42,800,000,000** GBP (not stated (page dated 2026-07-29)) [keep: ] quote: "HMRC grapples with £42.8 billion of tax debt in arrears"
  - p89 Planned additional HMRC debt management officers recruited by end of decade = **2,400** debt management officers (not stated (page dated 2026-07-29)) [keep: ] quote: "HMRC planning to recruit another 2,400 debt management officers by the end of the decade"
- `https://www.investing.com/news/economy-news/bank-of-england-to-hold-rates-for-remainder-of-year-despite-inflation-risks-reuters-poll-4865665` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['company insolvencies', 'insolvency service', 'uk insolvency']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p16', 'p17', 'p18'] Same headline series (registered company insolvencies, E&W, SA) for Aug 2025, Jul 2025, Aug 2024; p16-p18 are the SA-vintage duplicates of p1-p3 and agree exactly, so they are one measurement, not ind
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p21', 'p22', 'p23', 'p24'] Component breakdown of the Aug 2025 headline (311+1600+121+16+0=2048); SA and non-SA vintages coincide for this month, confirming internal consistency of the headline definition.
- corroborating: ['p19', 'p20', 'p29', 'p30', 'p25', 'p26', 'p27', 'p28'] Monthly SA component table for May/Jun/Jul/Aug 2025 and Aug 2024; establishes the recent run-rate band (~1,900-2,230) and the component mix (CVL ~76-78%, compulsory ~15-17%, admin ~6-7%).
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45'] 2026 SA monthly totals: Jan 1,764, Feb 1,907, Mar 2,037, Apr 2,085; Apr 2026 is 3% above Apr 2025 (2,028). Shows a rising 2026 trajectory from a weak January, with April near the 2025 average.
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39'] 12-month rolling insolvency rate ~51.5-51.8 per 10,000 through Apr 2026, slightly below the 52.5 a year earlier; component rates (CVL 39.6, compulsory 7.9, admin 3.9, CVA 0.4) are consistent with the 
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p40'] Historical rate context (52.6, 55.5, peak 113.1, 1-in-190); confirms current level is well below crisis peaks and gently declining, supporting a no-break trend assumption.
- corroborating: ['p49', 'p50', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56'] Distress indicators (Oct 2025 +17% y/y, highest since 2011; Q4 2025 critical distress +44%; 2025 total 23,938 broadly flat) point to elevated but not accelerating distress into 2026 — consistent with 
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] HR1 forms: Aug 2025 was a seasonal trough (285 vs ~400 typical), and Jan-Mar 2026 rose to 396-470, the strongest quarter in the series — a leading signal of somewhat higher insolvency activity in mid/
- corroborating: ['p46', 'p47', 'p48'] Zombie-firm share (1 in 6 mid-market, +600 in 12 months) is qualitative distress context only; no direct conversion to monthly counts.
- corroborating: ['p13', 'p14', 'p15'] Percentage changes that restate p1-p3 and p4/p29; redundant with the levels but confirm the arithmetic.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p19', 'p20', 'p41', 'p42', 'p43', 'p44', 'p45', 'p70', 'p71', 'p72'] All are SA headline monthly totals for England and Wales from the same Insolvency Service series. They form the primary level anchor: 2025 ran ~2,000-2,230, early 2026 dipped (Jan 1,764, Feb 1,907, Ma
- corroborating: ['p4', 'p5', 'p6', 'p7', 'p8', 'p73', 'p74', 'p75', 'p76'] Component breakdowns of the headline for Aug 2025 and Jun 2026. They sum to the headline (Aug 2025: 311+1,600+121+16+0 = 2,048; Jun 2026: 276+1,364+191+14 = 1,845). Confirms the headline is a sum of t
- corroborating: ['p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83'] Month-on-month and year-on-year changes for June 2026 components. p82 (administrations +45% m/m) is explained by p83 (~60 connected real-estate companies), so the June administration spike is a one-of
- corroborating: ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p84', 'p9', 'p10'] 12-month rolling insolvency rates per 10,000 companies. They drift gently (52.5 -> 51.8 -> 50.5 by June 2026), confirming a mild downward trend in the rate, not a collapse. p84 (50.5, year to June 202
- corroborating: ['p57', 'p58', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69'] HR1 redundancy-notice forms by month. August 2025 (p62 = 285) is a clear seasonal trough vs spring/autumn (~400+), corroborating an August seasonal dip in insolvency activity. HR1 is a leading/adminis
- conflicting: ['p85', 'p86', 'p87', 'p88', 'p89'] HMRC winding-up petitions up 31% y/y and ~2,400 court-ordered liquidations in the past year suggest upward pressure on compulsory liquidations, which conflicts with the observed ~15% y/y fall in compu
- corroborating: ['p46', 'p48', 'p49', 'p51', 'p52', 'p53', 'p54', 'p55', 'p56'] Distress indicators (zombie firms, critical financial distress, sector distress in hotels/bars) and 2025 totals. They point to elevated but not accelerating distress; p55 (23,938 in 2025, broadly in l
- corroborating: ['p11', 'p40'] Both cite the 2008-09 peak rate of 113.1 per 10,000; identical figure from the same source, so they are one fact, not two. Useful only as a distant upper bound; current rate (~50) is far below it.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 level relative to August 2025 | 0.95 | 0.85..1.06 | 0.6712..1.342 (widened) | ratio | m3 (m3) | 2026 monthly totals (May 1,849, Jun 1,845) are ~10% below the same months of 2025 (p70 vs p72), and the rolling rate fell from 52.5 to 50.5 (p32 vs p84). August 2025 was 2,048 (p1). A modest further decline or stabilisation is the central case; HMRC petition growth (p86) is an upside risk, hence the | The 2026 y/y decline observed in May-June persists into August without a sharp enforcement-driven rebound. | Evidence that compulsory liquidations surge in mid-2026 (e.g. HMRC petition orders converting at a high rate) or that CVLs re-accelerate to 2025 levels. |
| a2 | August 2026 level relative to April 2026 | 0.97 | 0.87..1.08 | 0.6854..1.371 (widened) | ratio | m2 (m2) | April 2026 was 2,085 (p41); May and June fell to ~1,847 (p70, p71), a ~11% drop. August typically sits below spring (HR1 August trough, p62). Central case assumes the post-April step-down is largely retained with a small seasonal August dip. | The May-June 2026 step-down is a level shift rather than a one-off, and August shows its usual seasonal softness. | A July 2026 rebound back toward 2,000+ or evidence that the May-June dip was a reporting artefact. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | yoy_scaling | 2,106 | ['p1', 'p3', 'p41', 'p43'] / [] | [] |  | 0.00 | B1 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m2 | formula_mc | 2,030 | ['p41'] / ['a2'] | [] |  | 1.00 | B2 of 3 blocks; median of blocks: this block is the median |  |
| m3 | formula_mc | 1,950 | ['p1'] / ['a1'] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m2 coverage: the whole target
- m3 coverage: the whole target

Method details (computed by code):

- m1 yoy_scaling: target 2025 2,048 x signal 2,085 / 2,028 (growth 1.0281); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p41 * a2; Monte Carlo P10 to P90 1,367 to 2,983; result unit company converted to company; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 formula_mc: p1 * a1; Monte Carlo P10 to P90 1,320 to 2,881; result unit company converted to company; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 2,106 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 2,030 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 1,950 (width x/÷1.48, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.45; Birge ratio 0.14 (not above one, so no widening); final width x/÷1.45.
- Seasonal naive baseline (not combined): 2,048 (2025, from m1); the estimate is -0.9% against it.

Result: central **2,030** company, 80% interval [1,404, 2,934] company, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for the headline monthly total of registered company insolvencies in England and Wales for August 2026 (compulsory liquidations, CVLs, administrations, CVAs and receiverships, with the first three seasonally adjusted) is 2,030 company (80% model-based interval 1,404 to 2,934 company).

Evidence: the seasonal analogue anchors on August 2025 at 2,048 company insolvencies, adjusted by assumption a1 (0.95, range 0.6712 to 1.342) reflecting the ~[n] year-on-year fall in May-June 2026. A second route scales April 2026 (2,085 company insolvencies) by assumption a2 (0.97, range 0.6854 to 1.371) for the post-April step-down and August softness. The combination is the median of three equally weighted blocks, not narrowed for their number.

Observed inputs are the historical monthly totals; the August 2026 change factors are analyst assumptions, not data. The main risk is that the May-June dip was a one-off reporting effect, making this under-predict; HMRC petition growth is an upside risk. Actual August 2026 data would most improve it.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 August 2026 level relative to August 2025: 0.95 ratio, range 0.6712 to 1.342 (range widened by code); used by m3. Overturned by: Evidence that compulsory liquidations surge in mid-2026 (e.g. HMRC petition orders converting at a high rate) or that CVLs re-accelerate to 2025 levels.
- a2 August 2026 level relative to April 2026: 0.97 ratio, range 0.6854 to 1.371 (range widened by code); used by m2. Overturned by: A July 2026 rebound back toward [n]+ or evidence that the May-June dip was a reporting artefact.

Method details (computed by code):
- m1 yoy_scaling: target 2025 2,048 x signal 2,085 / 2,028 (growth 1.0281); no backtest year; own 80% width x/÷1.38 (no error evidence, code's default width)
- m2 formula_mc: p41 * a2; Monte Carlo P10 to P90 1,367 to 2,983; result unit company converted to company; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- m3 formula_mc: p1 * a1; Monte Carlo P10 to P90 1,320 to 2,881; result unit company converted to company; own 80% width x/÷1.48 (Monte Carlo of the formula inputs)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1: 2,106 (width x/÷1.38, no error evidence, code's default width); B2 = m2: 2,030 (width x/÷1.48, Monte Carlo of the formula inputs); B3 = m3: 1,950 (width x/÷1.48, Monte Carlo of the formula inputs). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.45; Birge ratio 0.14 (not above one, so no widening); final width x/÷1.45.
- Seasonal naive baseline (not combined): 2,048 (2025, from m1); the estimate is -0.9% against it.

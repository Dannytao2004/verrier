# Evidence ledger: fc_de_cars_2026_09

- Question: Assume today is 2026-09-05. You know nothing published after this date. Estimate the number of new passenger cars (Pkw) registered in Germany in September 2026, as it will be first reported in the Kraftfahrt-Bundesamt's (KBA) monthly press release on vehicle registrations.
- as_of: 2026-09-05
- Pinned target: Number of new passenger cars (Pkw) with first-time registration in Germany during September 2026, as reported by the Kraftfahrt-Bundesamt (KBA) in its monthly press release on vehicle registrations (Fahrzeugzulassungen). Counts new Pkw only (Neuzulassungen von Personenkraftwagen), excluding used-car | unit new passenger car registrations | period 2026-09-01..2026-09-30 | publisher Kraftfahrt-Bundesamt (KBA)

- Official value (scoring only, never shown to the agent): 256,774

## Directions and pages

### d1 [own_history] KBA monthly series analyst

Hypothesis: September new Pkw registrations follow a recurring seasonal pattern (September is typically a strong month due to model-year/plate effects and Q3 push). Prior Septembers (2019, 2023, 2024, 2025) and the 2026 monthly run-rate anchor the level; September/adjacent-month ratio transfers the current level to September.

Queries issued by the searcher: KBA Pkw Neuzulassungen September 2025 Kraftfahrt-Bundesamt; Kraftfahrt-Bundesamt Fahrzeugzulassungen Neuzulassungen Pkw August 2026; KBA Pressemitteilung Fahrzeugzulassungen September 2023 Pkw Neuzulassungen 260; "September 2019" Pkw Neuzulassungen KBA 244.622

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2025/pm39_2025_n_09_25_pm_komplett.html` -> **snapshot** (snapshot 20251008160911); points raw/verified 14/12
  - p1 New passenger car (Pkw) registrations in Germany, September 2025 = **236** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "235.528 Personenkraftwagen (Pkw) wurden im September 2025 neu zugelassen."
  - p2 New Pkw registrations in Germany, September 2025, change vs previous month (Augu = **13.7** as written "+13,7", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p3 New Pkw registrations in Germany, September 2025, change vs September 2024 = **12.8** as written "+12,8", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Um +12,8 Prozent Prozent übertraf das Zulassungsvolumen das Niveau des Vorjahresmonats."
  - p4 New Pkw registrations in Germany, January to September 2025, change vs same peri = **-0.3** as written "-0,3", value check pending percent (2025-01-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p5 Commercial new Pkw registrations share of total, September 2025 = **65.8** as written "65,8", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Commercial share; structural, not a level driver.] quote: "Die gewerblichen Neuzulassungen stiegen um +10,7 Prozent, ihr Anteil betrug 65,8 Prozent."
  - p6 BEV new Pkw registrations in Germany, September 2025 = **45.49** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: BEV count 2025; sub-component.] quote: "45.495 Elektro (BEV) Neuwagen kamen zur Zulassung und damit +31,9 Prozent mehr als im Vorjahresmonat, ihr Anteil betrug 19,3 Prozent."
  - p7 BEV share of new Pkw registrations, September 2025 = **19.3** as written "19,3", value check pending percent (2025-09-01..2025-09-30) [DISCARD: BEV share 2025; sub-component share.] quote: "45.495 Elektro (BEV) Neuwagen kamen zur Zulassung und damit +31,9 Prozent mehr als im Vorjahresmonat, ihr Anteil betrug 19,3 Prozent."
  - p8 Total new motor vehicles (Kfz) registrations in Germany, September 2025 = **283** new motor vehicle registrations (2025-09-01..2025-09-30) [DISCARD: Total Kfz 2025; different scope from Pkw.] quote: "Insgesamt wurden 283.299 Kfz (+11,7 %) und 22.523 (+3,7 %) Kfz-Anhänger neu zugelassen."
  - p9 Used-car transfers (Besitzumschreibungen) of Pkw in Germany, September 2025 = **560** used passenger car ownership transfers (2025-09-01..2025-09-30) [DISCARD: Used-car transfers; different population (Besitzumschreibungen), not new registrations.] quote: "\| Personenkraftwagen \| 560.399 \| +9,0 \| +5,6 \| 4.952.038 \| +0,5 \|"
  - p10 SUV segment share of new Pkw registrations, September 2025 = **33.6** as written "33,6", value check pending percent (2025-09-01..2025-09-30) [DISCARD: SUV segment share; no route to total level.] quote: "Das Segment der SUVs erreichte im Vergleich zum Vorjahresmonat ein Plus von 21,4 Prozent und war im September mit einem Anteil von 33,6 Prozent erneut das stärkste Segment."
  - p11 VW brand new Pkw registrations in Germany, September 2025 = **45.23** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Single-brand share; not a total-level driver.] quote: "\| VW \| 45.225 \| 19,2 \| +16,2 \| 420.628 \| 19,9 \| +3,9 \|"
  - p12 Average CO2 emissions of new Pkw in Germany, September 2025 = **103** as written "102,8", value check pending g/km (2025-09-01..2025-09-30) [DISCARD: CO2 emissions; irrelevant to registration count.] quote: "Der durchschnittliche CO2-Ausstoß sank gegenüber dem Vorjahresmonat um -8,8 Prozent und betrug 102,8 g/km."
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2023/pm37_2023_n_09_23_pm_komplett.html` -> **snapshot** (snapshot 20250326122956); points raw/verified 15/14
  - p13 New passenger car (Pkw) registrations in Germany, September 2023 = **225** new passenger car registrations (2023-09-01..2023-09-30) [keep: ] quote: "224.502 Personenkraftwagen (Pkw) wurden im September 2023 neu zugelassenen."
  - p14 New Pkw registrations in Germany, September 2023, change vs previous month (Augu = **-17.9** as written "-17,9", value check pending % change vs previous month (2023-09-01..2023-09-30) [keep: ] quote: "\| Personenkraftwagen \| 224.502 \| -17,9 \| -0,1 \| 2.138.066 \| +14,5 \|"
  - p15 New Pkw registrations in Germany, September 2023, change vs September 2022 = **-0.1** as written "-0,1", value check pending % change vs same month previous year (2023-09-01..2023-09-30) [keep: ] quote: "Mit -0,1 Prozent lag das Zulassungsvolumen in etwa auf dem Niveau des Vorjahresmonats."
  - p16 Cumulative new Pkw registrations in Germany, January to September 2023, change v = **14.5** as written "+14,5", value check pending % change vs prior-year period (2023-01-01..2023-09-30) [keep: ] quote: "\| Personenkraftwagen \| 224.502 \| -17,9 \| -0,1 \| 2.138.066 \| +14,5 \|"
  - p17 Commercial (gewerblich) share of new Pkw registrations, September 2023 = **66.9** as written "66,9", value check pending % of new Pkw registrations (2023-09-01..2023-09-30) [DISCARD: Commercial share 2023; structural, not a level driver.] quote: "Die gewerblichen Neuzulassungen stiegen um +5,7 Prozent, ihr Anteil betrug 66,9 Prozent."
  - p18 Battery-electric (BEV) new Pkw registrations in Germany, September 2023 = **31.71** new BEV passenger car registrations (2023-09-01..2023-09-30) [DISCARD: BEV count 2023; sub-component.] quote: "31.714 Elektro (BEV) Neuwagen kamen zur Zulassung, -28,6 Prozent weniger als im Vorjahresmonat, ihr Anteil betrug 14,1 Prozent."
  - p19 BEV share of new Pkw registrations, September 2023 = **14.1** as written "14,1", value check pending % of new Pkw registrations (2023-09-01..2023-09-30) [DISCARD: BEV share 2023; sub-component share.] quote: "31.714 Elektro (BEV) Neuwagen kamen zur Zulassung, -28,6 Prozent weniger als im Vorjahresmonat, ihr Anteil betrug 14,1 Prozent."
  - p20 Hybrid new Pkw registrations in Germany, September 2023 = **73.18** new hybrid passenger car registrations (2023-09-01..2023-09-30) [DISCARD: Hybrid count 2023; sub-segment, not needed for total.] quote: "73.178 Pkw und damit +6,9 Prozent mehr als im Vergleichsmonat waren mit einem hybriden Antrieb ausgestattet"
  - p21 Plug-in hybrid new Pkw registrations in Germany, September 2023 = **15.38** new plug-in hybrid passenger car registrations (2023-09-01..2023-09-30) [DISCARD: PHEV count 2023; sub-segment.] quote: "darunter 15.383 Plug-in-Hybride, deren Anzahl um -45,7 Prozent zurückging und einen Anteil von 6,9 Prozent ausmachte."
  - p22 Petrol new Pkw registrations in Germany, September 2023 = **78.98** new petrol passenger car registrations (2023-09-01..2023-09-30) [DISCARD: Petrol count 2023; sub-segment.] quote: "78.979 Pkw waren mit einem Benzinantrieb ausgestattet, +9,1 Prozent mehr als im September des Vorjahres."
  - p23 Diesel new Pkw registrations in Germany, September 2023 = **39.9** new diesel passenger car registrations (2023-09-01..2023-09-30) [DISCARD: Diesel count 2023; sub-segment.] quote: "39.900 neu zugelassene Diesel-Neuwagen bewirkten ein Plus von 4,6 Prozent und einen Anteil von 17,8 Prozent."
  - p24 Total new motor vehicle (Kfz) registrations in Germany, September 2023 = **272** new motor vehicle registrations (2023-09-01..2023-09-30) [DISCARD: Total Kfz (all motor vehicles) 2023; different scope from Pkw.] quote: "Insgesamt wurden 272.322 Kraftfahrzeuge (Kfz) (-0,5 %) und 22.015 (-11,7 %) Kfz-Anhänger neu zugelassen."
  - p25 Used passenger car (Pkw) ownership transfers in Germany, September 2023 = **501** used passenger car ownership transfers (2023-09-01..2023-09-30) [DISCARD: Used-car transfers 2023; different population.] quote: "\| Personenkraftwagen \| 500.570 \| -6,0 \| +4,8 \| 4.550.244 \| +6,2 \|"
  - p26 Average CO2 emissions of new Pkw in Germany, September 2023 = **120** as written "119,8", value check pending g/km (2023-09-01..2023-09-30) [DISCARD: CO2 emissions 2023; irrelevant.] quote: "Der durchschnittliche CO2-Ausstoß stieg um +12,4 Prozent und betrug 119,8 g/km."
- `https://www.auto-medienportal.net/artikel/detail/66193` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 3 (number: ambiguous separators: '.' used as a thousands separator: 3)

### d2 [related_series] European auto market analyst

Hypothesis: Germany is a stable share (~20–25%) of EU new car registrations; EU-wide September 2026 registrations (ACEA) times Germany's historical share gives an independent cross-check. Direction: if EU momentum is up, Germany likely up.

Queries issued by the searcher: ACEA new car registrations September 2025 EU Germany passenger car market; ACEA press release new passenger car registrations 2026 EU Germany monthly; Kraftfahrt-Bundesamt Fahrzeugzulassungen August 2026 Pkw Neuzulassungen Pressemitteilung; reifenpresse ACEA Pkw-Neuzulassungen Juli 2026 Deutschland EU

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/european-union/car-registrations` -> **snapshot** (snapshot 20260824062202); points raw/verified 15/14
  - p27 EU new passenger car registrations, June 2026 (level) = **1,150,000** new passenger car registrations (2026-06-01..2026-06-30) [DISCARD: Redundant rounded copy of p28 (same June 2026 EU level); p28 is the precise value.] quote: "EU passenger car registrations surged 13.6% yoy to a three-month high of 1.15 million units in June 2026"
  - p28 EU new passenger car registrations, June 2026 (precise level) = **1,147,962** new passenger car registrations (2026-06-01..2026-06-30) [keep: Precise EU June 2026 level; usable only as a share-based cross-check, not a German level.] quote: "\| New Car Registrations YoY \| 1147962.00 \| 955013.00 \| Units \| Jun 2026 \|"
  - p29 EU new passenger car registrations, May 2026 = **955,013** new passenger car registrations (2026-05-01..2026-05-31) [keep: ] quote: "Car Registrations in European Union decreased to 955013 Units in May from 972314 Units in April of 2026."
  - p30 EU new passenger car registrations, April 2026 = **972,314** new passenger car registrations (2026-04-01..2026-04-30) [keep: ] quote: "Car Registrations in European Union decreased to 955013 Units in May from 972314 Units in April of 2026."
  - p31 EU new passenger car registrations, year-on-year growth, June 2026 = **13.6** % (2026-06-01..2026-06-30) [keep: ] quote: "EU passenger car registrations surged 13.6% yoy to a three-month high of 1.15 million units in June 2026"
  - p32 EU new passenger car registrations, year-on-year growth, May 2026 = **3.2** % (2026-05-01..2026-05-31) [keep: ] quote: "accelerating sharply from a 3.2% rise in May"
  - p33 EU new passenger car registrations, year-on-year growth, H1 2026 = **5.7** % (2026-01-01..2026-06-30) [keep: ] quote: "In H1 of 2026, new EU car registrations grew 5.7%"
  - p34 Germany new passenger car registrations, year-on-year growth, June 2026 = **15.7** % (2026-06-01..2026-06-30) [keep: ] quote: "The bloc's four largest markets all posted notable growth: Germany (15.7%), France (11.4%), Italy (10.6%), and Spain (7.8%)."
  - p35 Germany car registrations, July 2026 (level) = **268,068** car registrations (2026-07-01..2026-07-31) [keep: Kept but flagged: TE 'car registrations' July 2026 level conflicts with VDA cumulative; usable only as a directional/def] quote: "\| Car Registrations - Germany \| 268068.00 \| 296378.00 \| Units \| Jul 2026 \|"
  - p36 Germany car registrations, previous period (June 2026) = **296,378** car registrations (2026-06-01..2026-06-30) [keep: Same caveat as p35; June 2026 TE level, definitional cross-check only.] quote: "\| Car Registrations - Germany \| 268068.00 \| 296378.00 \| Units \| Jul 2026 \|"
  - p37 EU battery-electric vehicle share of EU market, June 2026 = **20.7** % (2026-06-01..2026-06-30) [DISCARD: EU BEV share; not a German total-level driver.] quote: "Battery-electric vehicles (BEVs) accounted for 20.7% of the EU market, up from 15.6% a year earlier"
  - p38 EU new passenger car registrations, all-time high (March 2017) = **1,890,664** new passenger car registrations (2017-03-01..2017-03-31) [DISCARD: All-time-high EU level from 2017; irrelevant to a 2026 German September level.] quote: "reaching an all time high of 1890664.00 Units in March of 2017"
  - p39 EU new passenger car registrations, record low (April 2020) = **270,682** new passenger car registrations (2020-04-01..2020-04-30) [DISCARD: Record-low EU level from April 2020 (COVID); irrelevant outlier.] quote: "and a record low of 270682.00 Units in April of 2020"
  - p40 EU new passenger car registrations, long-run monthly average 2003-2026 = **1,089,663** new passenger car registrations per month (2003-01-01..2026-08-31) [DISCARD: Long-run EU monthly average; too coarse and different scope to inform a single German month.] quote: "Car Registrations in European Union averaged 1089662.62 Units from 2003 until 2026"
- `https://investir.lesechos.fr/actu-des-valeurs/la-vie-des-actions/les-ventes-de-voitures-neuves-dans-lue-ont-cru-de-93-en-septembre-acea-2258308` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d3 [forecasts_markets] industry forecaster / order-book watcher

Hypothesis: Published 2026 forecasts (VDA, ifo, CAR-Center, Bloomberg/Reuters consensus) for German new car registrations and order intake imply a September level; order backlog and BEV incentive changes shift timing. Direction: higher order intake → higher September registrations with a lag.

Queries issued by the searcher: VDA Pkw Inlandsmarkt Prognose 2026; Germany new car registrations forecast 2026 KBA; KBA Pkw-Neuzulassungen August 2026 Fahrzeugzulassungen; ifo Geschäftsklima Automobilindustrie Auftragsbestand 2026

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/en/press/press-releases/2025/251208_PM_Forecasts_2026` -> **snapshot** (snapshot 20260630155227); points raw/verified 15/0
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.boersen-zeitung.de/unternehmen-branchen/vda-erwartet-etwas-mehr-neuzulassungen` -> **snapshot** (snapshot 20260105000408); points raw/verified 13/0
- dropped by code checks: 28 (period_end 2026-12-31 after as_of: 22; value_as_written not in quote as a whole number: 1; number: unknown scale word 'Millionen': 4; number: low/high given but value_as_written is not a range: 1)

### d4 [shocks] policy and demand analyst

Hypothesis: Policy changes (BEV purchase incentives, company-car tax rules, CO2/fleet rules) and macro conditions (interest rates, consumer confidence) can shift September registrations, especially pull-forward/pull-back around effective dates. Direction depends on timing of any incentive change.

Queries issued by the searcher: Deutschland E-Auto Förderung 2026 Änderung Kaufprämie; KBA Fahrzeugzulassungen August 2026 Pkw Neuzulassungen; "September 2026" Neuzulassungen Pkw Prognose KBA Sondereffekt; GfK Konsumklima August 2026 Verbraucherstimmung Deutschland

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.verbraucherzentrale.de/wissen/energie/emobilitaet/eautopraemie-2026-so-sichern-sie-sich-bis-zu-6000-euro-116489` -> **snapshot** (snapshot 20260618162749); points raw/verified 15/0
- `https://www.kba.de/SharedDocs/Downloads/DE/Pressemitteilungen/2026/pm_35_2026_fahrzeugzulassungen_08_2026.pdf?__blob=publicationFile&v=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period_end 2029-12-31 after as_of: 14; scale word 'billion' not supported by quote or table header: 1)

### d5 [base_rates] calendar/seasonality analyst

Hypothesis: September has a specific working-day count and seasonal multiplier relative to the annual run-rate; applying the 2026 YTD run-rate times a September seasonal factor yields the estimate. Direction: more working days / typical September strength → above-average month.

Queries issued by the searcher: Pkw Neuzulassungen September Saisonfaktor Kraftfahrt-Bundesamt Monatsdurchschnitt; Arbeitstage September 2026 Deutschland Anzahl; KBA Fahrzeugzulassungen August 2026 Pkw Neuzulassungen kumuliert Januar bis August 2026; Pkw Neuzulassungen Deutschland September 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 Monatszahlen KBA Jahresübersicht

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://genesis.destatis.de/datenbank/online/table/81000-0050/table-toolbar` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/en/news/facts-and-figures/monthly-figures` -> **snapshot** (snapshot 20260521201106); points raw/verified 13/13
  - p41 New passenger car registrations in Germany, April 2026 = **249,163** new passenger car registrations (2026-04-01..2026-04-30) [keep: ] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p42 New passenger car registrations in Germany, January-April 2026 cumulative = **948,567** new passenger car registrations (2026-01-01..2026-04-30) [keep: ] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p43 Year-on-year change in new passenger car registrations, April 2026 vs April 2025 = **3** % (2026-04-01..2026-04-30) [keep: ] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p44 Year-on-year change in new passenger car registrations, January-April 2026 vs 20 = **5** % (2026-01-01..2026-04-30) [keep: ] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p45 New registrations of German makes incl. group makes, April 2026 = **170,953** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: German-makes split; sub-component, not needed for total.] quote: "\| German makes incl. group makes \| 170,953 \| 0 \| 650,025 \| 3 \|"
  - p46 New registrations of foreign makes, April 2026 = **78,210** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: Foreign-makes split; sub-component.] quote: "\| Foreign makes \| 78,210 \| 8 \| 298,542 \| 9 \|"
  - p47 New registrations of electric passenger cars (Electro), April 2026 = **91,898** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: Electro (incl. PHEV) count; sub-component.] quote: "\| Electro \| 91,898 \| 32 \| 327,648 \| 33 \|"
  - p48 New registrations of BEV passenger cars, April 2026 = **64,350** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: BEV count April 2026; sub-component.] quote: "\| of which BEV \| 64,350 \| 41 \| 223,980 \| 41 \|"
  - p49 New registrations of PHEV passenger cars, April 2026 = **27,546** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: PHEV count April 2026; sub-component.] quote: "\| PHEV \| 27,546 \| 13 \| 103,660 \| 18 \|"
  - p50 Domestic passenger car production, April 2026 = **352,400** passenger cars produced (2026-04-01..2026-04-30) [DISCARD: April 2026 production; not needed for September.] quote: "\| Domestic Production \| 352,400 \| -4 \| 1,421,400 \| -2 \|"
  - p51 Passenger car exports from domestic production, April 2026 = **270,400** passenger cars exported (2026-04-01..2026-04-30) [DISCARD: April 2026 exports; not needed for September.] quote: "\| Of which Exports \| 270,400 \| -3 \| 1,075,100 \| -2 \|"
  - p52 Commercial vehicle new registrations total, April 2026 = **27,710** commercial vehicle registrations (2026-04-01..2026-04-30) [DISCARD: Commercial vehicle registrations; different scope.] quote: "\| CV new registrations total \| 27,710 \| 1 \| 106,233 \| -3 \|"
  - p53 Commercial vehicle new registrations total, January-April 2026 cumulative = **106,233** commercial vehicle registrations (2026-01-01..2026-04-30) [DISCARD: Commercial vehicle cumulative; different scope.] quote: "\| CV new registrations total \| 27,710 \| 1 \| 106,233 \| -3 \|"

### d6 [physical_flow] production/logistics analyst

Hypothesis: Domestic registrations are supplied by domestic production plus imports minus exports; German Pkw production and export volumes (VDA/Statistisches Bundesamt) constrain the pool available for domestic registration. Direction: higher production/imports → higher potential registrations, with inventory buffer.

Queries issued by the searcher: VDA Pkw Produktion Deutschland 2026 Monat; Germany car production exports monthly 2026 VDA Inland Produktion; VDA Pressemeldung August 2026 Pkw-Inlandsproduktion Neuzulassungen; KBA Fahrzeugzulassungen August 2026 Pressemitteilung Neuzulassungen Pkw

- `https://www.vda.de/de/presse/Pressemeldungen/2026/260903_PM_Nationale_PM_Pkw-Produktion_in_Deutschland_im_August_2026` -> **snapshot** (snapshot 20260905172623); points raw/verified 15/9
  - p54 Pkw production in Germany, August 2026 = **230** Pkw (2026-08-01..2026-08-31) [keep: ] quote: "Im August wurden 229.900 Pkw in Deutschland produziert."
  - p55 Pkw exports from Germany, August 2026 = **168** Pkw (2026-08-01..2026-08-31) [keep: ] quote: "Der Export lag im August bei 168.300 Einheiten um 12 Prozent unter dem Wert des Vorjahresmonats."
  - p56 New Pkw registrations in Germany, August 2026 (table) = **213** new Pkw registrations (2026-08-01..2026-08-31) [keep: ] quote: "\| Neuzulassungen in Deutschland \| \| \| 212.563 \| 3 \| 1.965.024 \| 5 \|"
  - p57 New Pkw registrations by German brands (incl. group brands), August 2026 = **136** new Pkw registrations (2026-08-01..2026-08-31) [DISCARD: German-makes split August 2026; sub-component.] quote: "\| dt. Marken inkl. Konzernmarken \| \| \| 136.093 \| -6 \| 1.326.191 \| 1 \|"
  - p58 New Pkw registrations by foreign brands, August 2026 = **76.47** new Pkw registrations (2026-08-01..2026-08-31) [DISCARD: Foreign-makes split August 2026; sub-component.] quote: "\| ausl. Marken \| \| \| 76.470 \| 21 \| 638.833 \| 13 \|"
  - p59 New Pkw registrations by foreign brands, January-August 2026 cumulative = **639** new Pkw registrations (2026-01-01..2026-08-31) [DISCARD: Foreign-makes cumulative; sub-component.] quote: "\| ausl. Marken \| \| \| 76.470 \| 21 \| 638.833 \| 13 \|"
  - p60 BEV new registrations in Germany, August 2026 = **68.93** new Pkw registrations (2026-08-01..2026-08-31) [DISCARD: BEV count August 2026; sub-component.] quote: "\| BEV \| \| \| 68.930 \| 75 \| 515.545 \| 53 \|"
  - p61 BEV new registrations in Germany, January-August 2026 cumulative = **516** new Pkw registrations (2026-01-01..2026-08-31) [DISCARD: BEV cumulative; sub-component.] quote: "\| BEV \| \| \| 68.930 \| 75 \| 515.545 \| 53 \|"
  - p62 Electric share of total new Pkw registrations, August 2026 = **44** % of total new Pkw registrations (2026-08-01..2026-08-31) [DISCARD: Electric share; sub-component share, not a total-level driver.] quote: "Der Elektroanteil an den Gesamtzulassungen erreichte mit 44 Prozent den höchsten Wert seit der Reduktion des Umweltbonus Ende 2022 und den zweithöchsten Wert überhaupt."
- `https://www.vda.de/de/presse/Pressemeldungen/2026/260806_PM_Nationale_PM_Pkw-Produktion_in_Deutschland_im_Juli_2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.marklines.com/ja/statistics/flash_prod/automotive-production-in-germany-by-month` -> **snapshot** (snapshot 20251116120404); points raw/verified 15/15
  - p63 Germany passenger car production, September 2025 (VDA preliminary, incl. CKD par = **385,300** vehicles (2025-09-01..2025-09-30) [keep: September 2025 production; useful as a supply-side analogue for September seasonality, with scope caveat (incl. CKD).] quote: "\| 生産台数 \| 385,300 \| 2% \| 3,139,000 \| 2% \|"
  - p64 Germany passenger car exports, September 2025 (VDA preliminary, incl. CKD parts  = **292,900** vehicles (2025-09-01..2025-09-30) [keep: September 2025 exports; supply-side analogue with scope caveat.] quote: "\| 輸出台数 \| 292,900 \| -2% \| 2,406,700 \| 0% \|"
  - p65 Germany passenger car production, January-September 2025 cumulative (VDA prelimi = **3,139,000** vehicles (2025-01-01..2025-09-30) [DISCARD: Cumulative Jan-Sep 2025 production; redundant with p63 for a monthly September estimate.] quote: "\| 生産台数 \| 385,300 \| 2% \| 3,139,000 \| 2% \|"
  - p66 Germany passenger car exports, January-September 2025 cumulative (VDA preliminar = **2,406,700** vehicles (2025-01-01..2025-09-30) [DISCARD: Cumulative Jan-Sep 2025 exports; redundant with p64.] quote: "\| 輸出台数 \| 292,900 \| -2% \| 2,406,700 \| 0% \|"
  - p67 Germany passenger car production, October 2025 (VDA preliminary) = **353,600** vehicles (2025-10-01..2025-10-31) [DISCARD: October 2025 production; outside the September seasonal window and not needed.] quote: "\| 生産台数 \| 353,600 \| -4% \| 3,499,000 \| 1% \|"
  - p68 Germany passenger car exports, October 2025 (VDA preliminary) = **277,500** vehicles (2025-10-01..2025-10-31) [DISCARD: October 2025 exports; outside the September seasonal window.] quote: "\| 輸出台数 \| 277,500 \| -1% \| 2,677,700 \| 0% \|"
  - p69 Germany passenger car production, January-October 2025 cumulative (VDA prelimina = **3,499,000** vehicles (2025-01-01..2025-10-31) [DISCARD: Cumulative Jan-Oct 2025 production; redundant.] quote: "\| 生産台数 \| 353,600 \| -4% \| 3,499,000 \| 1% \|"
  - p70 Germany passenger car exports, January-October 2025 cumulative (VDA preliminary) = **2,677,700** vehicles (2025-01-01..2025-10-31) [DISCARD: Cumulative Jan-Oct 2025 exports; redundant.] quote: "\| 輸出台数 \| 277,500 \| -1% \| 2,677,700 \| 0% \|"
  - p71 Germany passenger car production, August 2025 (VDA preliminary) = **237,600** vehicles (2025-08-01..2025-08-31) [keep: August 2025 production; pairs with p54 (August 2026) to form a production YoY signal.] quote: "\| 生産台数 \| 237,600 \| -21% \| 2,752,100 \| 2% \|"
  - p72 Germany passenger car exports, August 2025 (VDA preliminary) = **177,700** vehicles (2025-08-01..2025-08-31) [keep: August 2025 exports; pairs with p55 (August 2026) for an export YoY signal.] quote: "\| 輸出台数 \| 177,700 \| -24% \| 2,100,200 \| 0% \|"
  - p73 Germany passenger car production, July 2025 (VDA preliminary) = **347,100** vehicles (2025-07-01..2025-07-31) [DISCARD: July 2025 production; not needed for a September estimate.] quote: "\| 生産台数 \| 347,100 \| 9% \| 2,518,400 \| 5% \|"
  - p74 Germany passenger car exports, July 2025 (VDA preliminary) = **283,500** vehicles (2025-07-01..2025-07-31) [DISCARD: July 2025 exports; not needed.] quote: "\| 輸出台数 \| 283,500 \| 7% \| 1,936,400 \| 3% \|"
  - p75 Germany passenger car production, June 2025 (VDA preliminary) = **359,700** vehicles (2025-06-01..2025-06-30) [DISCARD: June 2025 production; not needed.] quote: "\| 生産台数 \| 359,700 \| 3% \| 2,173,700 \| 4% \|"
  - p76 Germany passenger car exports, June 2025 (VDA preliminary) = **274,700** vehicles (2025-06-01..2025-06-30) [DISCARD: June 2025 exports; not needed.] quote: "\| 輸出台数 \| 274,700 \| 5% \| 1,659,100 \| 3% \|"
  - p77 Germany passenger car production, May 2025 (VDA preliminary) = **363,600** vehicles (2025-05-01..2025-05-31) [DISCARD: May 2025 production; not needed.] quote: "\| 生産台数 \| 363,600 \| 19% \| 1,810,700 \| 4% \|"
- `https://www.autohaus.de/nachrichten/autohandel/pkw-markt-in-deutschland-gemischtes-bild-3888055` -> **snapshot** (snapshot 20260807205559); points raw/verified 11/0
- dropped by code checks: 17 (number: unknown scale word 'Mio.': 3; number: ambiguous separators: '.' used as a thousands separator: 3; period year 2026 does not appear in the page text or URL (likely mis-dated): 8; number: scale word 'Millionen' is not English or CJK (not supported): 3)

### b1 [own_history] KBA monthly seasonality

Hypothesis: A September/adjacent-month seasonal ratio (e.g., September vs August and vs July) computed from KBA Pkw Neuzulassungen 2019-2025 would let us transfer the observed August 2026 level (p56) to September 2026, the single most direct route. Currently we lack a clean multi-year September-vs-August ratio series.

Queries issued by the searcher: KBA Pkw Neuzulassungen September 2019 August 2019 Monat; Kraftfahrt-Bundesamt Fahrzeugzulassungen Monatsbericht Neuzulassungen Personenkraftwagen September 2020 2021 Tabelle; Pkw-Neuzulassungen Deutschland Monatstabelle 2019 2020 2021 2022 2023 2024 August September Anzahl Übersicht; KBA Pkw Neuzulassungen August 2019 313 Pkw August September 2021 2022 197

- `https://www.kba.de/DE/Statistik/Fahrzeuge/Neuzulassungen/MonatlicheNeuzulassungen/monatl_neuzulassungen_node.html` -> **snapshot** (snapshot 20260903231833); points raw/verified 0/0
- `https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ8/fz8_202009_pdf.pdf?__blob=publicationFile&v=1` -> **snapshot** (snapshot 20230307051839); points raw/verified 14/14
  - p78 New Pkw registrations in Germany, September 2020 (total) = **265,227** as written "265 227", value check pending new passenger car registrations (2020-09-01..2020-09-30) [keep: ] quote: "Insgesamt 265 227 134,3 - 13,4 243 352 79 854 162 355 21 188 54 036 20 127"
  - p79 New Pkw registrations in Germany, September 2020, change vs September 2019 (%) = **8.4** as written "+ 8,4", value check pending % (2020-09-01..2020-09-30) [keep: ] quote: "265 227 100,0 + 8,4 2 041 831 100,0"
  - p80 New Pkw registrations in Germany, January-September 2020 (cumulative total) = **2,041,831** as written "2 041 831", value check pending new passenger car registrations (2020-01-01..2020-09-30) [keep: ] quote: "265 227 100,0 + 8,4 2 041 831 100,0"
  - p81 New Pkw registrations in Germany, January-September 2020, change vs January-Sept = **-25.5** as written "- 25,5", value check pending % (2020-01-01..2020-09-30) [keep: ] quote: "265 227 244 622 + 8,4 2 041 831 2 740 158 - 25,5"
  - p82 New Pkw registrations in Germany, September 2019 (total, from CO2 table) = **244,622** as written "244 622", value check pending new passenger car registrations (2019-09-01..2019-09-30) [keep: ] quote: "265 227 244 622 + 8,4 2 041 831 2 740 158 - 25,5"
  - p83 New Pkw registrations in Germany, January-September 2019 (cumulative total, from = **2,740,158** as written "2 740 158", value check pending new passenger car registrations (2019-01-01..2019-09-30) [keep: ] quote: "265 227 244 622 + 8,4 2 041 831 2 740 158 - 25,5"
  - p84 New Pkw registrations in Germany, September 2020, petrol (Benzin) count = **120,645** as written "120 645", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Petrol subset of September 2020; mix detail, not a level input.] quote: "NEUZULASSUNGEN INSGESAMT 265 227 134,3 120 645 150,1 6,5 67 901 169,7 6,4 606 809 54 036 20 127 21 188"
  - p85 New Pkw registrations in Germany, September 2020, diesel count = **67,901** as written "67 901", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Diesel subset of September 2020; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 265 227 134,3 120 645 150,1 6,5 67 901 169,7 6,4 606 809 54 036 20 127 21 188"
  - p86 New Pkw registrations in Germany, September 2020, electric (Elektro) count = **21,188** as written "21 188", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Electric subset of September 2020; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 265 227 134,3 120 645 150,1 6,5 67 901 169,7 6,4 606 809 54 036 20 127 21 188"
  - p87 New Pkw registrations in Germany, September 2020, hybrid count = **54,036** as written "54 036", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Hybrid subset of September 2020; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 265 227 134,3 120 645 150,1 6,5 67 901 169,7 6,4 606 809 54 036 20 127 21 188"
  - p88 New Pkw registrations in Germany, September 2020, private holders (private Halte = **95,514** as written "95 514", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Private-holder subset of September 2020; mix detail.] quote: "265 227 95 514 36,0 169 610 63,9 50 578 19,1 19 818 7,5"
  - p89 New Pkw registrations in Germany, September 2020, commercial holders (gewerblich = **169,610** as written "169 610", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Commercial-holder subset of September 2020; mix detail.] quote: "265 227 95 514 36,0 169 610 63,9 50 578 19,1 19 818 7,5"
  - p90 New Pkw registrations in Germany, September 2020, VW brand count = **40,398** as written "40 398", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: VW brand subset of September 2020; mix detail.] quote: "40 398 15,2 + 1,6 367 181 18,0"
  - p91 New Pkw registrations in Germany, September 2020, Wohnmobile (motorhomes) subset = **5,414** as written "5 414", value check pending new passenger car registrations (2020-09-01..2020-09-30) [DISCARD: Motorhome subset of September 2020; mix detail.] quote: "10 756 3 380 9 686 4 969 7 181 5 183 85 265 227 2 041 831 269 59 151 81 346 80 1 5 414 62 175"
- `https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ8/fz8_201909_pdf.pdf?__blob=publicationFile&v=1` -> **snapshot** (snapshot 20230307050231); points raw/verified 15/14
  - p92 New passenger car (Pkw) registrations in Germany, January-September 2019 (cumula = **2,740,158** as written "2 740 158", value check pending new passenger car registrations (2019-01-01..2019-09-30) [keep: ] quote: "244 622 100,0 + 22,2 2 740 158 100,0"
  - p93 New passenger car (Pkw) registrations in Germany, September 2019, change vs Sept = **22.2** as written "+ 22,2", value check pending % (2019-09-01..2019-09-30) [keep: ] quote: "244 622 100,0 + 22,2 2 740 158 100,0"
  - p94 New passenger car (Pkw) registrations in Germany, September 2018 (prior-year com = **200,134** as written "200 134", value check pending new passenger car registrations (2018-09-01..2018-09-30) [keep: ] quote: "244 622 200 134 + 22,2 2 740 158 2 673 418 + 2,5"
  - p95 New passenger car (Pkw) registrations in Germany, January-September 2018 (prior- = **2,673,418** as written "2 673 418", value check pending new passenger car registrations (2018-01-01..2018-09-30) [keep: ] quote: "244 622 200 134 + 22,2 2 740 158 2 673 418 + 2,5"
  - p96 New passenger car (Pkw) registrations in Germany, January-September 2019, change = **2.5** as written "+ 2,5", value check pending % (2019-01-01..2019-09-30) [keep: ] quote: "244 622 200 134 + 22,2 2 740 158 2 673 418 + 2,5"
  - p97 New passenger car (Pkw) registrations in Germany, September 2019, petrol (Benzin = **146,463** as written "146 463", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Petrol subset of September 2019; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 244 622 155,1 146 463 156,9 6,8 72 519 167,6 6,3 514 293 18 945 3 572 5 880"
  - p98 New passenger car (Pkw) registrations in Germany, September 2019, diesel fuel ty = **72,519** as written "72 519", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Diesel subset of September 2019; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 244 622 155,1 146 463 156,9 6,8 72 519 167,6 6,3 514 293 18 945 3 572 5 880"
  - p99 New passenger car (Pkw) registrations in Germany, September 2019, electric (Elek = **5,880** as written "5 880", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Electric subset of September 2019; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 244 622 155,1 146 463 156,9 6,8 72 519 167,6 6,3 514 293 18 945 3 572 5 880"
  - p100 New passenger car (Pkw) registrations in Germany, September 2019, hybrid (incl.  = **18,945** as written "18 945", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Hybrid subset of September 2019; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 244 622 155,1 146 463 156,9 6,8 72 519 167,6 6,3 514 293 18 945 3 572 5 880"
  - p101 New passenger car (Pkw) registrations in Germany, September 2019, plug-in hybrid = **3,572** as written "3 572", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: PHEV subset of September 2019; mix detail.] quote: "NEUZULASSUNGEN INSGESAMT 244 622 155,1 146 463 156,9 6,8 72 519 167,6 6,3 514 293 18 945 3 572 5 880"
  - p102 New passenger car (Pkw) registrations in Germany, September 2019, private holder = **80,714** as written "80 714", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Private-holder subset of September 2019; mix detail.] quote: "244 622 80 714 33,0 163 820 67,0 52 927 21,6 19 933 8,1"
  - p103 New passenger car (Pkw) registrations in Germany, September 2019, commercial hol = **163,820** as written "163 820", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: Commercial-holder subset of September 2019; mix detail.] quote: "244 622 80 714 33,0 163 820 67,0 52 927 21,6 19 933 8,1"
  - p104 New passenger car (Pkw) registrations in Germany, September 2019, VW brand = **39,750** as written "39 750", value check pending new passenger car registrations (2019-09-01..2019-09-30) [DISCARD: VW brand subset of September 2019; mix detail.] quote: "39 750 16,2 + 96,0 498 481 18,2"
  - p105 New passenger car (Pkw) registrations in Germany, September 2019, average CO2 em = **155** as written "155,1", value check pending g/km (2019-09-01..2019-09-30) [DISCARD: CO2 average for September 2019; not a registration level.] quote: "Insgesamt 244 622 155,1 - 0,6 237 924 11 716 217 626 5 880 18 945 3 572"
- `https://aeemobility.de/tag/kba/page/6/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 1 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b2 [related_series] 2026 momentum

Hypothesis: A clean KBA/VDA September 2026 order-intake or early-month registration signal (or a September 2026 ifo/VDA forecast) would resolve whether the strong August 2026 BEV-driven momentum (p56, p60) carries into September. This is the largest uncertainty in the level.

Queries issued by the searcher: KBA Fahrzeugzulassungen August 2026 Neuzulassungen Personenkraftwagen; VDA Inlandsaufträge Pkw August 2026; Neuzulassungen September 2026 Prognose Pkw Deutschland; ifo Institut Autoindustrie Geschäftsklima August 2026 Auftragsmangel Pkw

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/de/presse/Pressemeldungen/2026/260903_PM_Nationale_PM_Pkw-Produktion_in_Deutschland_im_August_2026` -> **snapshot** (snapshot 20260905172623); points raw/verified 15/13
  - p106 Pkw new registrations in Germany, August 2026 (VDA/KBA table) = **213** new passenger car registrations (2026-08-01..2026-08-31) [DISCARD: Exact duplicate of p56 (same VDA/KBA August 2026 table value 212,563); keeping both would double-count one observation.] quote: "\| Neuzulassungen in Deutschland \| \| \| 212.563 \| 3 \| 1.965.024 \| 5 \|"
  - p107 Pkw new registrations in Germany, August 2026 (rounded, press text) = **213** new passenger car registrations (2026-08-01..2026-08-31) [DISCARD: Rounded restatement of p56 (212,600); redundant copy of the same measurement.] quote: "Die Zahl der Pkw-Neuzulassungen stieg im August im Vergleich zum Vorjahresmonat um 3 Prozent auf ein Volumen von 212.600 Einheiten."
  - p108 BEV new registrations in Germany, August 2026 = **68.93** BEV new passenger car registrations (2026-08-01..2026-08-31) [keep: ] quote: "\| BEV \| \| \| 68.930 \| 75 \| 515.545 \| 53 \|"
  - p109 BEV new registrations in Germany, August 2026 (rounded, press text) = **68.9** BEV new passenger car registrations (2026-08-01..2026-08-31) [DISCARD: Rounded restatement of p108 (68,900 vs 68,930); redundant.] quote: "Die Registrierungen von BEV stiegen überdurchschnittlich um 75 Prozent auf 68.900 Einheiten."
  - p110 BEV new registrations in Germany, January-August 2026 cumulative = **516** BEV new passenger car registrations (2026-01-01..2026-08-31) [keep: ] quote: "\| BEV \| \| \| 68.930 \| 75 \| 515.545 \| 53 \|"
  - p111 PHEV new registrations in Germany, August 2026 = **25.41** PHEV new passenger car registrations (2026-08-01..2026-08-31) [keep: ] quote: "\| PHEV \| \| \| 25.406 \| 6 \| 219.808 \| 16 \|"
  - p112 Electric (BEV+PHEV+FCEV) new registrations in Germany, August 2026 = **94.34** electric new passenger car registrations (2026-08-01..2026-08-31) [keep: ] quote: "\| Elektro \| \| \| 94.336 \| 49 \| 735.364 \| 40 \|"
  - p113 Electric (BEV+PHEV+FCEV) new registrations in Germany, January-August 2026 cumul = **735** electric new passenger car registrations (2026-01-01..2026-08-31) [keep: ] quote: "\| Elektro \| \| \| 94.336 \| 49 \| 735.364 \| 40 \|"
  - p114 Electric share of total Pkw new registrations in Germany, August 2026 = **44** % of total new passenger car registrations (2026-08-01..2026-08-31) [keep: ] quote: "Der Elektroanteil an den Gesamtzulassungen erreichte mit 44 Prozent den höchsten Wert seit der Reduktion des Umweltbonus Ende 2022"
  - p115 Private new registrations share of total Pkw market in Germany, August 2026 = **40.5** as written "40,5 Prozent", value check pending % of total new passenger car registrations (2026-08-01..2026-08-31) [keep: ] quote: "ließ den Anteil privater Neuzulassungen am Pkw-Gesamtmarkt auf 40,5 Prozent steigen"
  - p116 Domestic order intake for BEV at German manufacturers, August 2026 year-on-year  = **62** % change vs prior-year month (2026-08-01..2026-08-31) [keep: ] quote: "Bei den deutschen Herstellern legten die inländische Auftragseingänge für rein batterieelektrische Fahrzeuge (BEV) im August um 62 Prozent gegenüber dem Vorjahresmonat zu."
  - p117 Domestic order intake for BEV at German manufacturers, January-August 2026 year- = **64** % change vs prior-year period (2026-01-01..2026-08-31) [keep: ] quote: "Seit Jahresbeginn gingen aus dem Inland 64 Prozent mehr BEV-Bestellungen ein als im entsprechenden Vorjahreszeitraum."
  - p118 Pkw production in Germany, August 2026 = **230** passenger cars produced (2026-08-01..2026-08-31) [DISCARD: Exact duplicate of p54 (229,900 Pkw production August 2026).] quote: "Im August wurden 229.900 Pkw in Deutschland produziert."
- `https://www.vda.de/en/news/facts-and-figures/monthly-figures` -> **snapshot** (snapshot 20260521201106); points raw/verified 11/11
  - p119 New passenger car registrations, Germany, April 2026 = **249,163** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: Exact duplicate of p41 (April 2026 registrations 249,163).] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p120 New passenger car registrations, Germany, January-April 2026 cumulative = **948,567** new passenger car registrations (2026-01-01..2026-04-30) [DISCARD: Exact duplicate of p42 (Jan-Apr 2026 cumulative 948,567).] quote: "\| New registrations \| 249,163 \| 3 \| 948,567 \| 5 \|"
  - p121 New passenger car registrations, German makes incl. group makes, April 2026 = **170,953** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: German-makes subset of April 2026 registrations; not needed for a September level estimate and duplicates p45.] quote: "\| German makes incl. group makes \| 170,953 \| 0 \| 650,025 \| 3 \|"
  - p122 New passenger car registrations, foreign makes, April 2026 = **78,210** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: Foreign-makes subset of April 2026 registrations; duplicates p46 and not needed.] quote: "\| Foreign makes \| 78,210 \| 8 \| 298,542 \| 9 \|"
  - p123 New passenger car registrations, electric (Electro), April 2026 = **91,898** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: April 2026 electric subset; duplicates p47, not needed for total level.] quote: "\| Electro \| 91,898 \| 32 \| 327,648 \| 33 \|"
  - p124 New passenger car registrations, BEV, April 2026 = **64,350** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: April 2026 BEV subset; duplicates p48.] quote: "\| of which BEV \| 64,350 \| 41 \| 223,980 \| 41 \|"
  - p125 New passenger car registrations, BEV, January-April 2026 cumulative = **223,980** new passenger car registrations (2026-01-01..2026-04-30) [DISCARD: April 2026 BEV cumulative; duplicates p48/p125 context, not needed.] quote: "\| of which BEV \| 64,350 \| 41 \| 223,980 \| 41 \|"
  - p126 New passenger car registrations, PHEV, April 2026 = **27,546** new passenger car registrations (2026-04-01..2026-04-30) [DISCARD: April 2026 PHEV subset; duplicates p49.] quote: "\| PHEV \| 27,546 \| 13 \| 103,660 \| 18 \|"
  - p127 Domestic passenger car production, April 2026 = **352,400** passenger cars produced (2026-04-01..2026-04-30) [DISCARD: April 2026 production; duplicates p50, not needed for September level.] quote: "\| Domestic Production \| 352,400 \| -4 \| 1,421,400 \| -2 \|"
  - p128 Domestic passenger car exports, April 2026 = **270,400** passenger cars exported (2026-04-01..2026-04-30) [DISCARD: April 2026 exports; duplicates p51.] quote: "\| Of which Exports \| 270,400 \| -3 \| 1,075,100 \| -2 \|"
  - p129 Commercial vehicle new registrations total, April 2026 = **27,710** commercial vehicle new registrations (2026-04-01..2026-04-30) [DISCARD: Commercial vehicle registrations; different vehicle class, irrelevant to Pkw target.] quote: "\| CV new registrations total \| 27,710 \| 1 \| 106,233 \| -3 \|"
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: ambiguous separators: '.' used as a thousands separator: 1; number: unknown scale word 'Mio.': 1)

### b3 [shocks] policy timing

Hypothesis: Any BEV purchase-incentive or company-car tax change effective in late 2026 could pull registrations forward into September or push them back; identifying the effective date would materially shift the estimate. Currently no such policy point is in the evidence.

Queries issued by the searcher: E-Auto-Kaufprämie 2026 Starttermin Deutschland Förderung neue Elektroautos; Dienstwagenbesteuerung 2026 Änderung Elektroautos 0,25 Prozent Grenze; KBA Neuzulassungen August 2026 Pressemitteilung Personenkraftwagen Elektroautos Anteil; Dienstwagenbesteuerung Änderung ab 1. Januar 2027 Elektroautos 0,25 Prozent auslaufen

- `https://www.autohaus.de/nachrichten/autohersteller/automarkt-im-august-elektroautos-legen-weiter-zu-3898583` -> **snapshot** (snapshot 20260903220642); points raw/verified 15/0
- `https://www.bundesregierung.de/breg-de/aktuelles/e-auto-foerderportal-2403088` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.tk-lex.tk.de/web/guest/externalcontent/-/haufeindex_renderedresource/_leongexternalcontentportlet_WAR_leongcontentportlet_INSTANCE_J1Irw0L` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.electrive.net/2026/09/03/kba-zahlen-324-prozent-aller-neuwagen-fahren-vollelektrisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 15 (period year 2026 does not appear in the page text or URL (likely mis-dated): 14; number: ambiguous separators: '.' used as a thousands separator: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['germany car registrations', 'kba september 2026', 'pkw neuzulassungen']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p2', 'p3', 'p4'] All from the same KBA September 2025 press release; p1 is the level, p2/p3/p4 are derived changes from the same table. They are one measurement, not independent confirmations.
- corroborating: ['p13', 'p14', 'p15', 'p16'] Same KBA September 2023 release; level and changes are internally consistent. Provides a second September vintage for seasonality.
- corroborating: ['p1', 'p13'] Two September levels (2023: 224.5k; 2025: 235.5k) show September is a relatively strong month, consistent with a seasonal uplift vs adjacent months.
- conflicting: ['p35', 'p36', 'p56'] p35/p36 (TradingEconomics 'car registrations') give July 2026 = 268,068 and June 2026 = 296,378, while VDA p56 gives August 2026 = 212,563 and Jan-Aug cumulative 1,965,024. The TE June/July levels are
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49'] Single VDA April 2026 release; internal sums (German makes + foreign makes = total; BEV+PHEV = Electro) are consistent. One measurement vintage.
- corroborating: ['p54', 'p55', 'p56', 'p57', 'p58', 'p59', 'p60', 'p61', 'p62'] Single VDA August 2026 release; p57+p58 ≈ p56, p60/p56 ≈ p62. One measurement, but the most recent and most relevant anchor for the 2026 run-rate.
- corroborating: ['p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77'] Marklines/VDA production and export series; internally consistent cumulative differences. Different scope (production incl. CKD) from registrations, so usable only as a supply-side context, not a dire
- corroborating: ['p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p37', 'p38', 'p39', 'p40'] TradingEconomics/ACEA EU series; p27 and p28 are the same June 2026 figure at different precision (redundant). EU momentum (H1 +5.7%, June +13.6%) is a directional cross-check for German momentum.
- corroborating: ['p5', 'p17'] Commercial share ~66-67% in both Septembers; stable structural feature, not a level driver.
- corroborating: ['p6', 'p7', 'p18', 'p19', 'p60', 'p61', 'p62'] BEV share rose from 14.1% (Sep 2023) to 19.3% (Sep 2025) to 44% electric share (Aug 2026, VDA definition incl. PHEV). Consistent upward BEV trend; supports a higher 2026 level but does not by itself s
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p2', 'p3', 'p4'] Same KBA September 2025 release: level 235,528, +13.7% vs August 2025, +12.8% vs September 2024, and Jan-Sep 2025 -0.3%. Internally consistent; the +13.7% month-on-month confirms September is seasonal
- corroborating: ['p13', 'p14', 'p15', 'p16'] Same KBA September 2023 release: 224,502 Pkw, -17.9% vs August 2023, -0.1% vs September 2022, Jan-Sep 2023 +14.5%. Shows September/August ratio is not stable across years (2023 September fell vs Augus
- corroborating: ['p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p92', 'p93', 'p94', 'p95', 'p96'] KBA September 2019/2020 releases: September 2020 = 265,227 (+8.4% vs Sept 2019), September 2019 = 244,622 (+22.2% vs Sept 2018), September 2018 = 200,134. Consistent chain; 2019 and 2020 Septembers we
- corroborating: ['p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p97', 'p98', 'p99', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105'] Fuel-type, holder, brand and CO2 breakdowns of the same September 2019/2020 totals; they sum consistently to the totals and add no independent level information. Useful only as context on mix (e.g. BE
- corroborating: ['p56', 'p106', 'p107'] Duplicate reporting of August 2026 new Pkw registrations: 212,563 (table) and 212,600 (rounded press text), +3% yoy. Same VDA/KBA source; treat as one observation.
- corroborating: ['p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117'] August 2026 VDA release: BEV 68,930 (+75% yoy), PHEV 25,406, electric total 94,336 (44% share), private share 40.5%, domestic BEV order intake +62% in August and +64% YTD. Strong BEV momentum and orde
- corroborating: ['p54', 'p55', 'p118'] August 2026 production 229,900 and exports 168,300 (p54/p118 duplicate; p55 export). Production roughly equals registrations plus exports, so domestic supply is not a binding constraint on September r
- corroborating: ['p63', 'p64', 'p71', 'p72'] September 2025 production 385,300 and exports 292,900 vs August 2025 237,600/177,700: September production is far above August (post-summer-break ramp), consistent with September registrations exceedi
- corroborating: ['p35', 'p36', 'p34', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33'] TradingEconomics/ACEA-derived: Germany June 2026 296,378 (+15.7% yoy), July 2026 268,068; EU June 2026 1,147,962 (+13.6%), H1 +5.7%. Confirms a strong 2026 German market running well above 2025 levels
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p119', 'p120'] VDA April 2026: 249,163 registrations (+3% yoy), Jan-Apr 948,567 (+5% yoy). Duplicated across p41/p119 and p42/p120; consistent with the +5% YTD growth seen in the ACEA-derived series.
- conflicting: ['p1', 'p56', 'p35'] Level comparison across years: September 2025 (235,528) vs August 2026 (212,563) vs July 2026 (268,068). The 2026 monthly path is volatile (July high, August low), so a simple September/August ratio f

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September/August seasonal multiplier for German new Pkw registrations | 1.11 | 0.95..1.3 | 0.7858..1.572 (widened) | ratio | m1 (m1) | September 2025 was +13.7% vs August 2025 (p2), but September 2023 was -17.9% vs August 2023 (p14), and September production is far above August (p63 vs p71). The median of these signals is a modest uplift; the wide range reflects the observed instability of the September/August ratio. | August 2026 is a representative base month and no policy pull-forward distorts September 2026. | Evidence of a September 2026 policy change or a very weak/strong early-September registration signal. |
| a2 | Year-on-year change factor for September 2026 vs September 2025 | 1.05 | 0.85..1.3 | 0.85..1.3 | ratio | m2 (m2) | 2026 German registrations are running +5% YTD (p44, p33) with strong BEV momentum (+75% in August, p108) and order intake +64% YTD (p117); a modest continuation of the 2026 growth trend is assumed, with a wide range to cover policy and macro risk. | The 2026 growth trend persists into September without a major incentive change. | A sharp reversal in BEV orders or a new purchase-tax/incentive change effective in September 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 236 | ['p56'] / ['a1'] | [] |  | 0.33 | equal |  |
| m2 | formula_mc | 248 | ['p1'] / ['a2'] | [] |  | 0.33 | equal |  |
| m3 | series_naive | 230 |  | [] |  | 0.33 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **238** vehicle, 80% interval [161, 352] vehicle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.67

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for new passenger car (Pkw) first-time registrations in Germany during September 2026 is 238 vehicle (80% model-based interval 161 to 352 vehicle). This covers new Pkw only, calendar month September 2026, as first published by the KBA.

Evidence: August 2026 stood at 213 new Pkw registrations; September 2025 at 236 new passenger car registrations; September 2023 at 225 new passenger car registrations. Method m1 transfers the August level via a September/August multiplier of 1.11 (range 0.7858 to 1.572), giving 236 vehicle. Method m2 applies a year-on-year factor of 1.05 (range 0.85 to 1.3) to last September, giving 248 vehicle. Method m3 averages recent Septembers, giving 230 vehicle. The three methods were weighted equally (33%, 33%, 33%); no backtest errors were available.

Only the observed points are data; the multipliers are analyst assumptions. The main risk is an unstable September/August ratio or a policy-driven trend break. Better evidence would be actual September order books and daily registration data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September/August seasonal multiplier for German new Pkw registrations: 1.11 ratio, range 0.7858 to 1.572 (range widened by code); used by m1. Overturned by: Evidence of a September 2026 policy change or a very weak/strong early-September registration signal.
- a2 Year-on-year change factor for September 2026 vs September 2025: 1.05 ratio, range 0.85 to 1.3; used by m2. Overturned by: A sharp reversal in BEV orders or a new purchase-tax/incentive change effective in September 2026.

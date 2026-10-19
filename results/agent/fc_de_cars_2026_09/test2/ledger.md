# Evidence ledger: fc_de_cars_2026_09

- Question: Assume today is 2026-09-05. You know nothing published after this date. Estimate the number of new passenger cars (Pkw) registered in Germany in September 2026, as it will be first reported in the Kraftfahrt-Bundesamt's (KBA) monthly press release on vehicle registrations.
- as_of: 2026-09-05
- Pinned target: Number of new passenger cars (Pkw) with first registration in Germany during September 2026, as reported by the Kraftfahrt-Bundesamt (KBA) in its monthly press release on vehicle registrations (Fahrzeugzulassungen). Counts new Pkw first registrations (Neuzulassungen), including passenger cars of dom | unit new passenger car registrations | period 2026-09-01..2026-09-30 | publisher Kraftfahrt-Bundesamt (KBA)

- Official value (scoring only, never shown to the agent): 256,774

## Directions and pages

### d1 [own_history] KBA monthly time series

Hypothesis: September new Pkw registrations in prior years (2019, 2023, 2024, 2025) plus the 2026 monthly YTD series establish a base level and seasonal September factor; September is typically a strong month (post-summer, pre-Q4), so September 2026 ≈ recent monthly run-rate × September seasonal index.

Queries issued by the searcher: KBA Neuzulassungen Pkw September 2025 Kraftfahrt-Bundesamt Fahrzeugzulassungen; Germany new car registrations monthly 2026 Kraftfahrt-Bundesamt; "Neuzulassungen von Personenkraftwagen im Jahresverlauf" KBA 2023 2024 2025 2026 September; KBA September 2023 Pkw Neuzulassungen 224.816

- `https://www.kba.de/DE/Statistik/Fahrzeuge/Fahrzeugarten/fahrzeugarten_node.html` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://trendonify.com/germany/new-car-registrations` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.auto-medienportal.net/artikel/detail/70873` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2025/pm39_2025_n_09_25_pm_komplett.html` -> **snapshot** (snapshot 20251008160911); points raw/verified 15/13
  - p1 New Pkw registrations in Germany, September 2025 = **236** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "235.528 Personenkraftwagen (Pkw) wurden im September 2025 neu zugelassen."
  - p2 Year-on-year change in new Pkw registrations, September 2025 vs September 2024 = **12.8** as written "+12,8", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Um +12,8 Prozent Prozent übertraf das Zulassungsvolumen das Niveau des Vorjahresmonats."
  - p3 Month-on-month change in new Pkw registrations, September 2025 vs August 2025 = **13.7** as written "+13,7", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p4 Year-on-year change in new Pkw registrations, January to September 2025 vs same  = **-0.3** as written "-0,3", value check pending percent (2025-01-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p5 Commercial new Pkw registrations share of total, September 2025 = **65.8** as written "65,8", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Die gewerblichen Neuzulassungen stiegen um +10,7 Prozent, ihr Anteil betrug 65,8 Prozent."
  - p6 Year-on-year change in commercial new Pkw registrations, September 2025 = **10.7** as written "+10,7", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Die gewerblichen Neuzulassungen stiegen um +10,7 Prozent, ihr Anteil betrug 65,8 Prozent."
  - p7 Year-on-year change in private new Pkw registrations, September 2025 = **17.1** as written "+17,1", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Die privaten Neuzulassungen legten im Berichtsmonat um +17,1 Prozent zu."
  - p8 BEV new Pkw registrations in Germany, September 2025 = **45.49** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "45.495 Elektro (BEV) Neuwagen kamen zur Zulassung und damit +31,9 Prozent mehr als im Vorjahresmonat, ihr Anteil betrug 19,3 Prozent."
  - p9 BEV share of new Pkw registrations, September 2025 = **19.3** as written "19,3", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "45.495 Elektro (BEV) Neuwagen kamen zur Zulassung und damit +31,9 Prozent mehr als im Vorjahresmonat, ihr Anteil betrug 19,3 Prozent."
  - p10 Hybrid new Pkw registrations in Germany, September 2025 = **97.21** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "97.212 Pkw und damit +28,9 Prozent mehr als im Vergleichsmonat waren mit Hybridem Antrieb ausgestattet (Anteil 41,3 %), darunter 27.685 Plug-in-Hybride"
  - p11 Petrol new Pkw registrations in Germany, September 2025 = **63.05** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "63.047 Pkw waren mit Benzinantrieb ausgestattet, -5,9 Prozent weniger als im September des Vorjahres."
  - p12 Total new motor vehicles (Kfz) registrations in Germany, September 2025 = **283** new motor vehicle registrations (2025-09-01..2025-09-30) [keep: ] quote: "Insgesamt wurden 283.299 Kfz (+11,7 %) und 22.523 (+3,7 %) Kfz-Anhänger neu zugelassen."
  - p13 SUV segment share of new Pkw registrations, September 2025 = **33.6** as written "33,6", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Das Segment der SUVs erreichte im Vergleich zum Vorjahresmonat ein Plus von 21,4 Prozent und war im September mit einem Anteil von 33,6 Prozent erneut das stärkste Segment."
- dropped by code checks: 2 (number: ambiguous separators: '.' used as a thousands separator: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### d2 [forecasts_markets] Industry forecasters and associations

Hypothesis: VDA, ifo, and analyst forecasts for 2026 German passenger car registrations (full-year) can be divided into months using seasonal weights to bound September 2026; a full-year forecast of ~2.8–2.9 million implies ~230–260k in September.

Queries issued by the searcher: VDA Pkw Inlandsmarkt Prognose 2026 Neuzulassungen; Germany car sales forecast 2026 new passenger car registrations; Neuzulassungen Pkw 2026 Prognose August 2026 KBA Inlandsmarkt; KBA Pkw Neuzulassungen September 2025 236.000 Jahresverlauf Monatsanteil

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/en/press/press-releases/2025/251208_PM_Forecasts_2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.auto-medienportal.net/artikel/detail/69022` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.dataforce.de/news/august-2026-ein-positives-signal-fuer-den-markt/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] European auto market (ACEA) and German passenger car market

Hypothesis: Germany's share of EU new car registrations is stable (~20–22%); ACEA monthly EU totals and Germany's share can cross-check the KBA-derived level and flag whether 2026 German demand is running above/below the EU trend.

Queries issued by the searcher: ACEA passenger car registrations September 2025 Germany; ACEA new car registrations 2026 monthly EU Germany; KBA Fahrzeugzulassungen August 2026 Pkw Neuzulassungen Pressemitteilung; Prognose Pkw-Neuzulassungen Deutschland 2026 gesamt Jahr Marktentwicklung

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.largus.fr/pros/actualite-automobile/les-groupes-renault-stellantis-et-volkswagen-surperforment-dans-un-marche-europeen-en-croissance-30044` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tradingeconomics.com/european-union/car-registrations` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/en/2026/international-brands-set-records-market-share-of-electric-mobility-is-growing-rapidly/?print=print` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [shocks] Policy and incentive environment

Hypothesis: Changes to EV purchase incentives (Umweltbonus ended 2023; possible 2025–2026 reintroduction or company-car tax changes) and CO2/fleet rules shift September 2026 registrations via pull-forward or payback effects; a known incentive change effective Q4 2026 could pull registrations into September.

Queries issued by the searcher: Umweltbonus 2026 Elektroauto Förderung Wiedereinführung; Dienstwagensteuer 2026 Änderung Elektroauto Firmenwagen; KBA Neuzulassungen August 2026 Pkw Pressemitteilung Fahrzeugzulassungen; E-Auto-Förderung 2026 Mittel ausgeschöpft Antragszahlen August 2026 BAFA

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.n-tv.de/der_tag/Neue-E-Auto-Foerderung-stoesst-auf-grosses-Interesse-id31161295.html` -> **snapshot** (snapshot 20260810022651); points raw/verified 7/1
  - p14 Maximum Umweltbonus subsidy per vehicle before it was ended end-2023 = **4,500** euros per vehicle (..2023-12-31) [DISCARD: Umweltbonus maximum subsidy from before end-2023; no evidence of a 2026 incentive change tied to September, so it cannot] quote: "Die Höhe lag damals bei bis zu 4500 Euro, wovon die Hälfe die Hersteller tragen mussten."
- `https://www.vorwaerts.de/faq/neue-praemie-so-wird-die-anschaffung-von-elektroautos-jetzt-gefoerdert` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (period year 2026 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 3; scale word 'billion' not supported by quote or table header: 1; period_end 2029-12-31 after as_of: 1)

### d5 [base_rates] Calendar and day-count adjustment

Hypothesis: Monthly registrations scale with selling days; September 2026 has 22 working days vs August's ~21, and September historically runs ~10–15% above the annual monthly average; a day-adjusted run-rate from July–August 2026 gives a September anchor.

Queries issued by the searcher: Arbeitstage September 2026 Deutschland Anzahl; KBA Neuzulassungen August 2026 Pkw; KBA Neuzulassungen September 2025 Pkw 236.000; Pkw Neuzulassungen Monate 2025 Juli August September KBA Tabelle

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://genesis.destatis.de/datenbank/online/table/81000-0050/table-toolbar` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2025/pm39_2025_n_09_25_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.autobild.de/artikel/pkw-neuzulassungszahlen-september-2025-top-ten-22262259.html` -> **snapshot** (snapshot 20251112135739); points raw/verified 15/15
  - p15 KBA new passenger car (Pkw) registrations in Germany, September 2025 = **236** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p1 (same KBA September 2025 total).] quote: "235.528 Einheiten zählte das Kraftfahrt-Bundesamt (KBA)"
  - p16 Year-on-year change in German Pkw new registrations, September 2025 vs September = **12.8** as written "12,8 Prozent", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p2.] quote: "das sind 12,8 Prozent mehr Neuwagen als im September 2024"
  - p17 Increase in German Pkw new registrations, September 2025 vs August 2025 (count) = **28.3** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Derived count change, redundant with p3/p1.] quote: "im Vergleich mit dem Vormonat August 2025 insgesamt 28.299 Neuwagen mehr verkauft"
  - p18 Month-on-month change in German Pkw new registrations, September 2025 vs August  = **13.7** as written "13,7 Prozent", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p3.] quote: "(plus 13,7 Prozent)"
  - p19 Petrol-only Pkw new registrations in Germany, September 2025 = **63.05** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p11.] quote: "Rein benzinbetriebene Pkw machten mit 63.047 verkauften Einheiten im September 2025"
  - p20 Petrol Pkw share of all German Pkw new registrations, September 2025 = **26.8** as written "26,8 Prozent", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Derived share, redundant with p11/p1.] quote: "einen Anteil von 26,8 Prozent unter allen Pkw-Neuzulassungen aus"
  - p21 Diesel Pkw new registrations in Germany, September 2025 = **28.87** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "mit insgesamt 28.871 neuen Dieselfahrzeugen einem Marktanteil von 12,3 Prozent"
  - p22 Hybrid Pkw new registrations in Germany, September 2025 = **97.21** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p10.] quote: "insgesamt wurden 97.212 neue Hybride zugelassen"
  - p23 Plug-in hybrid Pkw new registrations in Germany, September 2025 = **27.68** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p39.] quote: "Darin enthalten sind 27.685 Plug-in-Hybride"
  - p24 Battery-electric (BEV) new registrations in Germany, September 2025 = **45.49** new passenger car registrations (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p8.] quote: "45.495 neue E-Autos wurden zugelassen"
  - p25 BEV share of German Pkw new registrations, September 2025 = **19.3** as written "19,3 Prozent", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p9.] quote: "Ihr Anteil an den Neuzulassungen betrug 19,3 Prozent"
  - p26 BEV share of German Pkw new registrations, January to September 2025 = **18.6** as written "18,6 Prozent", value check pending percent (2025-01-01..2025-09-30) [keep: ] quote: "im Zeitraum Januar bis September lag die E-Auto-Quote bei 18,6 Prozent"
  - p27 LPG (Flüssiggas) Pkw new registrations in Germany, September 2025 = **891** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "Mit 891 neuen Zulassungen erreichten die sie gerade mal 0,4 Prozent Marktanteil"
  - p28 SUV share of German Pkw new registrations, September 2025 = **33.6** as written "33,6 Prozent", value check pending percent (2025-09-01..2025-09-30) [DISCARD: Redundant duplicate of p13.] quote: "kamen sie auf einen Marktanteil von 33,6 Prozent"
  - p29 Compact class share of German Pkw new registrations, September 2025 = **17.5** as written "17,5 Prozent", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "und einem Marktanteil von 17,5 Prozent bilden die Kompakten die zweitstärkste Pkw-Sparte"

### d6 [physical_flow] OEM production and inventory

Hypothesis: German OEM domestic production plus imports minus exports approximates available supply; if production is constrained (chip/energy) or inventories are high, registrations deviate from demand. September registrations ≈ dealer deliveries, which track production ~4–8 weeks earlier.

Queries issued by the searcher: VDA Pkw Produktion August 2026 Inlandsproduktion; Kraftfahrt-Bundesamt Neuzulassungen August 2026 Pkw; KBA Fahrzeugzulassungen September 2025 Pkw Neuzulassungen Pressemitteilung; VDA "Monthly figures" July 2026 domestic production exports passenger cars

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/en/news/facts-and-figures/monthly-figures` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2025/pm39_2025_n_09_25_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.autohaus.de/nachrichten/autohandel/privatkunden-stuetzen-den-automarkt-e-autos-treiben-neuzulassungen-im-august-3901066` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [related_series] Powertrain mix and segment

Hypothesis: BEV/PHEV share shifts affect total volume because incentive-driven BEV demand can add or subtract registrations; splitting September 2026 into ICE + BEV + PHEV using recent shares and known policy gives a cross-check on the aggregate.

Queries issued by the searcher: KBA Neuzulassungen Elektroauto Anteil 2026; Germany BEV registrations monthly 2026 KBA; KBA Pressemitteilung Fahrzeugzulassungen August 2026 Neuzulassungen Pkw 212.563; KBA Neuzulassungen September 2025 Pkw 235.587

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/SharedDocs/Downloads/DE/Pressemitteilungen/2026/pm_35_2026_fahrzeugzulassungen_08_2026.pdf?__blob=publicationFile&v=4` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/SharedDocs/Downloads/DE/Pressemitteilungen/2026/pm_13_2026_alternative_Antriebe_02_2026.pdf?__blob=publicationFile&v=5` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] d1/d5

Hypothesis: A 2026 monthly YTD series (Jan-Aug 2026 KBA new Pkw registrations) would anchor the September 2026 level via a day-adjusted run-rate and a September seasonal factor; without it the estimate rests only on September 2025 and cannot capture 2026 momentum.

Queries issued by the searcher: KBA Fahrzeugzulassungen August 2026 Neuzulassungen Pkw Monatsbericht; KBA Neuzulassungen Pkw Januar bis August 2026; KBA Neuzulassungen Pkw September 2025 236.364; KBA Fahrzeugzulassungen "Januar 2026" Pkw Neuzulassungen Monat Februar März April Mai Juni

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/SharedDocs/Downloads/DE/Pressemitteilungen/2026/pm_32_2026_fahrzeugzulassungen_07_2026.pdf?__blob=publicationFile&v=7` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2025/pm39_2025_n_09_25_pm_komplett.html` -> **snapshot** (snapshot 20251008160911); points raw/verified 15/13
  - p30 New Pkw registrations Germany September 2025 = **236** new passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "235.528 Personenkraftwagen (Pkw) wurden im September 2025 neu zugelassen."
  - p31 New Pkw registrations Germany September 2025 change vs previous month = **13.7** as written "+13,7", value check pending percent change vs previous month (2025-09-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p32 New Pkw registrations Germany September 2025 change vs same month previous year = **12.8** as written "+12,8", value check pending percent change vs previous year month (2025-09-01..2025-09-30) [keep: ] quote: "Um +12,8 Prozent Prozent übertraf das Zulassungsvolumen das Niveau des Vorjahresmonats."
  - p33 New Pkw registrations Germany January-September 2025 change vs previous year per = **-0.3** as written "-0,3", value check pending percent change vs previous year period (2025-01-01..2025-09-30) [keep: ] quote: "\| Personenkraftwagen \| 235.528 \| +13,7 \| +12,8 \| 2.110.348 \| -0,3 \|"
  - p34 Commercial new Pkw registrations share September 2025 = **65.8** as written "65,8", value check pending percent share of new Pkw registrations (2025-09-01..2025-09-30) [keep: ] quote: "Die gewerblichen Neuzulassungen stiegen um +10,7 Prozent, ihr Anteil betrug 65,8 Prozent."
  - p35 Commercial new Pkw registrations change September 2025 = **10.7** as written "+10,7", value check pending percent change vs previous year month (2025-09-01..2025-09-30) [keep: ] quote: "Die gewerblichen Neuzulassungen stiegen um +10,7 Prozent, ihr Anteil betrug 65,8 Prozent."
  - p36 Private new Pkw registrations change September 2025 = **17.1** as written "+17,1", value check pending percent change vs previous year month (2025-09-01..2025-09-30) [keep: ] quote: "Die privaten Neuzulassungen legten im Berichtsmonat um +17,1 Prozent zu."
  - p37 BEV new Pkw registrations September 2025 = **45.49** new BEV passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "45.495 Elektro (BEV) Neuwagen kamen zur Zulassung und damit +31,9 Prozent mehr als im Vorjahresmonat, ihr Anteil betrug 19,3 Prozent."
  - p38 Hybrid new Pkw registrations September 2025 = **97.21** new hybrid passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "97.212 Pkw und damit +28,9 Prozent mehr als im Vergleichsmonat waren mit Hybridem Antrieb ausgestattet (Anteil 41,3 %)"
  - p39 Plug-in hybrid new Pkw registrations September 2025 = **27.68** new plug-in hybrid passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "darunter 27.685 Plug-in-Hybride, deren Anzahl um +85,4 Prozent über dem Ergebnis des Vorjahresmonats lag und einen Anteil von 11,8 Prozent ausmachte."
  - p40 Petrol new Pkw registrations September 2025 = **63.05** new petrol passenger car registrations (2025-09-01..2025-09-30) [keep: ] quote: "63.047 Pkw waren mit Benzinantrieb ausgestattet, -5,9 Prozent weniger als im September des Vorjahres."
  - p41 SUV segment share of new Pkw registrations September 2025 = **33.6** as written "33,6", value check pending percent share of new Pkw registrations (2025-09-01..2025-09-30) [keep: ] quote: "Das Segment der SUVs erreichte im Vergleich zum Vorjahresmonat ein Plus von 21,4 Prozent und war im September mit einem Anteil von 33,6 Prozent erneut das stärkste Segment."
  - p42 Total Kfz new registrations Germany September 2025 = **283** new motor vehicle registrations (2025-09-01..2025-09-30) [keep: ] quote: "Insgesamt wurden 283.299 Kfz (+11,7 %) und 22.523 (+3,7 %) Kfz-Anhänger neu zugelassen."
- `https://www.vdik.de/2026/internationale-marken-mit-rekord-marktanteil-elektromobilitaet-waechst-dynamisch/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: ambiguous separators: '.' used as a thousands separator: 1; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1)

### b2 [forecasts_markets] d2

Hypothesis: A full-year 2026 German passenger-car registration forecast (VDA/ifo/analyst) divided by a September seasonal weight would bound September 2026 and resolve whether the market is running above or below the 2025 level.

Queries issued by the searcher: VDA Pkw Inlandsmarkt Prognose 2026; German new car market forecast 2026 passenger car registrations; KBA Pkw Neuzulassungen August 2026; KBA Pkw Neuzulassungen September 2025 Fahrzeugzulassungen Monatsbericht

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.vda.de/en/press/press-releases/2025/251208_PM_Forecasts_2026` -> **snapshot** (snapshot 20260630155227); points raw/verified 15/0
- `https://www.auto-medienportal.net/artikel/detail/69022` -> **snapshot** (snapshot 20260119091743); points raw/verified 9/0
- `https://www.boersen-zeitung.de/unternehmen-branchen/vda-erwartet-etwas-mehr-neuzulassungen` -> **snapshot** (snapshot 20260105000408); points raw/verified 13/0
- dropped by code checks: 37 (scale word 'million' not supported by quote or table header: 6; period_end 2026-12-31 after as_of: 18; value_as_written not in quote as a whole number: 1; number: unknown scale word 'Millionen': 8; period_end missing or unparseable: 3; number: low/high given but value_as_written is not a range: 1)

### b3 [shocks] d4

Hypothesis: A known 2026 EV incentive or company-car tax change effective around Q4 2026 would create a pull-forward into September 2026; identifying it would let us adjust the base level rather than assume no policy effect.

Queries issued by the searcher: Deutschland E-Auto Förderung 2026 Wiedereinführung Kaufprämie; Dienstwagensteuer Änderung 2026 Elektroauto geldwerter Vorteil; KBA Neuzulassungen Pkw August 2026 Pressemitteilung Fahrzeugzulassungen; Dienstwagensteuer 1. Januar 2027 Änderung Elektro Bruttolistenpreis Grenze geplant

- `https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugzulassungen/2026/pm35_2026_n_08_26_pm_komplett.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.auto-motor-und-sport.de/verkehr/foerderportal-fuer-e-autos-startet-ab-dienstag-kann-die-e-auto-foerderung-beantragt-werden/` -> **snapshot** (snapshot 20260706215919); points raw/verified 8/6
  - p43 Maximum taxable household income for subsidy eligibility, households without chi = **80** EUR household taxable income (2026-05-19..2026-05-19) [keep: ] quote: "Die Einkommensgrenze liegt bei maximal 80.000 Euro für Haushalte ohne Kinder."
  - p44 Maximum taxable household income for subsidy eligibility, families with children = **90** EUR household taxable income (2026-05-19..2026-05-19) [keep: ] quote: "Familien mit Kindern können die Förderung bis zu einer Grenze von 90.000 Euro erhalten."
  - p45 Minimum holding period for subsidised vehicles = **36** months (2026-05-19..2026-05-19) [keep: ] quote: "Zu den weiteren Voraussetzungen gehört eine Mindesthaltedauer von 36 Monaten."
  - p46 Retroactive subsidy eligibility start date for first registrations = **1** as written "1. Januar 2026", value check pending day of month (January 2026) (2026-01-01..2026-01-01) [keep: ] quote: "Die Förderung gilt rückwirkend für alle förderfähigen Fahrzeuge, die seit dem 1. Januar 2026 erstmals zugelassen wurden."
  - p47 Date the subsidy application portal opens (start of application phase) = **19** as written "19. Mai 2026", value check pending day of month (May 2026) (2026-05-19..2026-05-19) [keep: ] quote: "Mit der Freischaltung des Förderportals am 19. Mai 2026 startet die Antragsphase für die neue staatliche Förderung von Elektroautos und Plug-in-Hybriden."
  - p48 Number of prior tax years used to determine household income for subsidy tier = **2** as written "zwei", value check pending tax years (2026-05-19..2026-05-19) [keep: ] quote: "Maßgeblich für die Einstufung ist das zu versteuernde Haushaltseinkommen der vergangenen zwei Steuerjahre."
- `https://www.vwfs.de/geschaeftskunden/magazin-flotte/dienstwagen/0-5-prozent-regelung.html` -> **snapshot** (snapshot 20260411073715); points raw/verified 15/3
  - p49 Plug-in hybrid company-car 0.5% rule: minimum electric-only range for cars acqui = **60** kilometres electric range (2022-01-01..2024-12-31) [keep: ] quote: "war eine Mindestreichweite von 60 Kilometern mit rein elektrischem Antrieb vorgeschrieben.3"
  - p50 Electric company car 0.25% rule: gross list price cap for cars acquired 2024 to  = **70** EUR gross list price (2024-01-01..2025-06-30) [keep: ] quote: "Bei der Anschaffung eines reinen Elektrofahrzeugs nach dem 31.12.2023 bis Ende Juni 2025 galt noch eine Obergrenze des Bruttolistenpreises von 70.000 Euro.5"
  - p51 Window for first private provision of company e-bike for tax valuation (start) = **1.01** date (2019-01-01..2019-01-01) [keep: ] quote: "Das muss zwischen dem 01.01.2019 und dem 31.12.2030 erfolgen."
- `https://www.haufe.de/id/beitrag/anhebung-der-bruttolistenpreisgrenze-bei-der-dienstwagenbesteuerung-fuer-elektrofahrzeuge-HI17067274.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 14 (number: low/high given but value_as_written is not a range: 2; period_end 2030-12-31 after as_of: 4; period_end 2026-12-31 after as_of: 1; period_end missing or unparseable: 7)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['germany car registrations', 'kba neuzulassungen', 'september pkw']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p15'] Both report 235,528 new Pkw registrations in September 2025; autobild (p15) is a secondary retelling of the KBA figure, so this is one underlying measurement, not independent confirmation.
- corroborating: ['p1', 'p2', 'p16'] p2 and p16 both give +12.8% YoY for September 2025; p16 is secondary reporting of the same KBA release. Consistent with p1 as the September 2025 level.
- corroborating: ['p3', 'p17', 'p18'] p3 (KBA) and p17/p18 (autobild) all describe the same +13.7% MoM / +28,299 unit September-vs-August 2025 increase; same underlying source.
- corroborating: ['p8', 'p9', 'p24', 'p25'] BEV September 2025 = 45,495 and 19.3% share appear identically in KBA (p8, p9) and autobild (p24, p25); one measurement.
- corroborating: ['p10', 'p22', 'p23'] Hybrid total 97,212 and PHEV 27,685 match across KBA (p10) and autobild (p22, p23); same source.
- corroborating: ['p11', 'p19', 'p20'] Petrol 63,047 and 26.8% share consistent across KBA (p11) and autobild (p19, p20).
- corroborating: ['p13', 'p28'] SUV share 33.6% identical in KBA (p13) and autobild (p28); same measurement.
- corroborating: ['p1', 'p12'] Total Kfz 283,299 (p12) exceeds Pkw 235,528 (p1), consistent with Pkw being a subset of all motor vehicles; no conflict.
- corroborating: ['p5', 'p6', 'p7'] Commercial share 65.8% with +10.7% and private +17.1% are internally consistent with an overall +12.8% (weighted blend), same KBA release.
- contextual: ['p4', 'p1'] YTD Jan-Sep 2025 was -0.3% YoY while September alone was +12.8%, indicating September 2025 was an unusually strong month relative to the year; relevant for seasonal/base-level reasoning, not a contrad
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p30', 'p15'] All three are the same KBA September 2025 Pkw total (235,528); p30 and p15 are redundant copies of p1, not independent confirmation.
- corroborating: ['p2', 'p32', 'p16'] Same +12.8% YoY figure for September 2025 from the same KBA release; duplicates.
- corroborating: ['p3', 'p31', 'p18'] Same +13.7% month-on-month September 2025 figure; duplicates.
- corroborating: ['p4', 'p33'] Same Jan-Sep 2025 cumulative -0.3% YoY; duplicates.
- corroborating: ['p5', 'p6', 'p34', 'p35'] Commercial share 65.8% and +10.7% growth are the same KBA statement; duplicates.
- corroborating: ['p7', 'p36'] Private +17.1% YoY, same KBA statement; duplicates.
- corroborating: ['p8', 'p9', 'p37', 'p24', 'p25'] BEV 45,495 and 19.3% share from the same KBA release; duplicates.
- corroborating: ['p10', 'p38', 'p22'] Hybrid 97,212 (41.3%) from same KBA release; duplicates.
- corroborating: ['p11', 'p40', 'p19'] Petrol 63,047 from same KBA release; duplicates.
- corroborating: ['p12', 'p42'] Total Kfz 283,299 from same KBA release; duplicates.
- corroborating: ['p13', 'p41', 'p28'] SUV share 33.6% from same KBA release; duplicates.
- corroborating: ['p21', 'p27', 'p29'] Autobild secondary reporting of KBA September 2025 detail (diesel 28,871, LPG 891, compact 17.5%); consistent with KBA primary but derived from same underlying data.
- corroborating: ['p1', 'p8', 'p10', 'p11', 'p21'] Powertrain split (BEV 45.5k + hybrid 97.2k + petrol 63.0k + diesel 28.9k ≈ 234.6k) roughly reconciles to the 235.5k total, confirming internal consistency of the September 2025 baseline.
- corroborating: ['p43', 'p44', 'p45', 'p46', 'p47', 'p48'] All describe the same 2026 EV/PHEV subsidy scheme (income caps, holding period, retroactive start, portal opening); they are one policy package, not independent demand signals.
- corroborating: ['p49', 'p50', 'p51'] Company-car tax rules for BEV/PHEV; contextual for powertrain mix, not directly a September 2026 volume driver.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September 2026 YoY change factor vs September 2025 | 1 | 0.85..1.15 | 0.85..1.15 | dimensionless | m1 (m1) | No 2026 YTD KBA series is available at cutoff, so momentum is unknown. September 2025 was already a strong month (+12.8% YoY, +13.7% MoM), so a flat-to-slightly-negative carry is plausible; the 2026 EV subsidy (p43-p48) may support BEV but the overall market is mature. Range spans a modest decline t | September 2026 demand is broadly similar to September 2025 with no large policy pull-forward. | A 2026 YTD series showing a sharp market contraction or boom, or a known Q4 2026 incentive change pulling registrations into September. |
| a2 | September seasonal index vs annual monthly average | 1.12 | 1.05..1.2 | 0.7937..1.587 (widened) | dimensionless | m2 (m2) | September is historically a strong registration month (post-summer, pre-Q4); p3 shows +13.7% MoM in September 2025. Index of ~1.12 relative to the annual monthly average is consistent with typical German seasonality. | September 2026 follows normal seasonal patterns with 22 working days and no holiday distortion. | Evidence of an unusual September calendar or a policy deadline shifting registrations out of the month. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 233 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 265 | ['p1'] / ['a2'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **249** vehicle, 80% interval [168, 367] vehicle, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate for new passenger car (Pkw) first registrations in Germany during September 2026, as to be reported by the KBA, is 249 vehicle (80% model-based interval 168 to 367 vehicle). This combines 2 methods at equal weight (50% and 50%).

The only observed anchor is September 2025 at 236 new passenger car registrations. Method m1 (233 vehicle) applies a YoY change factor of 1 (range 0.85 to 1.15) to that base. Method m2 (265 vehicle) scales the same base by a September seasonal index of 1.12 (range 0.7937 to 1.587). Both routes therefore rest entirely on the single observed point; the YoY factor and seasonal index are analyst assumptions, not observations. Equal weighting reflects the absence of backtest evidence to favor either.

The main risk is a large 2026 market shift (policy or EV-incentive effects) not captured by the flat carry. The most useful missing evidence is the 2026 year-to-date KBA monthly series, which would replace the assumed momentum with observed data.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 September 2026 YoY change factor vs September 2025: 1 dimensionless, range 0.85 to 1.15; used by m1. Overturned by: A 2026 YTD series showing a sharp market contraction or boom, or a known Q4 2026 incentive change pulling registrations into September.
- a2 September seasonal index vs annual monthly average: 1.12 dimensionless, range 0.7937 to 1.587 (range widened by code); used by m2. Overturned by: Evidence of an unusual September calendar or a policy deadline shifting registrations out of the month.

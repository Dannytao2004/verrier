# Evidence ledger: fc_de_unemployed_2026_10

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate the number of registered unemployed persons in Germany in October 2026 (not seasonally adjusted, all of Germany), as it will be first reported in the Federal Employment Agency's (Bundesagentur für Arbeit) monthly labour market press release.
- as_of: 2026-10-19
- Pinned target: Registered unemployed persons in Germany (Arbeitslose) as reported in the Bundesagentur für Arbeit monthly labour market press release, national total, not seasonally adjusted, stock at the reference date of the October 2026 reporting month | unit person | period 2026-10-01..2026-10-31 | publisher Bundesagentur für Arbeit (Federal Employment Agency), Statistik der BA

## Directions and pages

### d1 [own_history] BA monthly labour market statistics time series

Hypothesis: October unadjusted unemployment stock follows a stable seasonal pattern relative to September and to the prior October; the target equals the most recent observed level plus the typical September-to-October seasonal change plus a trend/cycle adjustment.

Queries issued by the searcher: Bundesagentur für Arbeit Arbeitslose Oktober 2025 Pressemitteilung Arbeitslosenquote; Statistik der Bundesagentur für Arbeit Arbeitslose Zeitreihe Monatszahlen nicht saisonbereinigt; "Arbeitsmarkt im September 2026" Bundesagentur für Arbeit Arbeitslose; statistik.arbeitsagentur.de Arbeitslose und Arbeitslosenquoten Deutschland Monate 2023 2024 2025 Tabelle xlsx

- `https://www.arbeitsagentur.de/presse/2026-37-arbeitsmarkt-im-september-2026` -> **live_dated** (page date 2026-09-30); points raw/verified 15/10
  - p1 Germany national registered unemployed year-on-year change, September 2026 vs Se = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +40.000"
  - p2 Germany national registered unemployment rate, September 2026, not seasonally ad = **6.4** as written "6,4 Prozent", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,4 Prozent."
  - p3 Germany national registered unemployment rate month-on-month change, September 2 = **-0.1** as written "-0,1 Prozentpunkte", value check pending percentage points (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,4 Prozent"
  - p4 Germany national registered unemployed month-on-month change, September 2026 vs  = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p5 Germany national registered unemployment rate year-on-year change, September 202 = **0.1** as written "0,1 Prozentpunkte", value check ok percentage points (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote hat sich im Vorjahresvergleich um 0,1 Prozentpunkte erhöht."
  - p6 Germany underemployment year-on-year change, September 2026 vs September 2025 = **25** persons (2026-09-01..2026-09-30) [keep: ] quote: "Mit 3.615.000 war sie um 25.000 höher als vor einem Jahr."
  - p7 Germany underemployment month-on-month change, September 2026 vs August 2026, se = **7** persons (2026-09-01..2026-09-30) [keep: ] quote: "Sie ist saisonbereinigt im September gegenüber dem Vormonat um 7.000 gesunken."
  - p8 Germany ILO unemployment rate, August 2026 = **4.3** as written "4,3 Prozent", value check pending percent (2026-08-01..2026-08-31) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im August auf 4,3 Prozent."
  - p9 Germany registered job vacancies (Arbeitsstellen) stock, September 2026 = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
  - p10 Germany registered job vacancies year-on-year change, September 2026 vs Septembe = **30** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202609/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-202609-pdf.pdf?__b` -> **live_dated** (page date 2026-09-01); points raw/verified 15/9
  - p11 Germany registered unemployed, month-on-month change August to September 2026 (u = **-66.98** persons (2026-09-01..2026-09-30) [keep: ] quote: "Bestand Arbeitslose 2.994.415 3.061.396 2.954.747 -66.981 -2,2 39.668 1,3"
  - p12 Germany registered unemployed, year-on-year change September 2026 vs September 2 = **39.67** persons (2026-09-01..2026-09-30) [keep: ] quote: "Bestand Arbeitslose 2.994.415 3.061.396 2.954.747 -66.981 -2,2 39.668 1,3"
  - p13 Germany registered unemployed, seasonally adjusted month-on-month change Septemb = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Entsprechend errechnet das Saisonbereinigungsverfahren einen Anstieg von 12.000."
  - p14 Germany registered unemployed, seasonally adjusted month-on-month change August  = **5** persons (2026-08-01..2026-08-31) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
  - p15 Germany registered unemployed, seasonally adjusted month-on-month change July 20 = **7** persons (2026-07-01..2026-07-31) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
  - p16 Germany registered unemployed, seasonally adjusted month-on-month change June 20 = **1** persons (2026-06-01..2026-06-30) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
  - p17 Germany registered unemployed, seasonally adjusted month-on-month change May 202 = **-11** persons (2026-05-01..2026-05-31) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
  - p18 Germany registered unemployed, seasonally adjusted month-on-month change April 2 = **19** persons (2026-04-01..2026-04-30) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
  - p19 Germany registered unemployed, seasonally adjusted month-on-month change March 2 = **1** persons (2026-03-01..2026-03-31) [keep: ] quote: "Arbeitslose 12.000 5.000 7.000 1.000 -11.000 19.000 1.000"
- `https://www.arbeitsagentur.de/presse/2025-44-arbeitsmarkt-im-oktober-2025` -> **live_dated** (page date 2025-10-30); points raw/verified 15/12
  - p20 Germany registered unemployed month-on-month change, September to October 2025,  = **-44** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Oktober: -44.000 auf 2.911.000"
  - p21 Germany registered unemployed year-on-year change, October 2025 vs October 2024 = **120** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +120.000"
  - p22 Germany registered unemployment rate, October 2025 = **6.2** as written "6,2 Prozent", value check pending percent (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,2 Prozent."
  - p23 Germany registered unemployment rate month-on-month change, October 2025 = **-0.1** as written "-0,1 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,2 Prozent"
  - p24 Germany registered unemployment rate year-on-year change, October 2025 vs Octobe = **0.2** as written "0,2 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote hat sich gegenüber dem Vorjahresmonat um 0,2 Prozentpunkte erhöht."
  - p25 Germany registered unemployed, seasonally adjusted month-on-month change, Octobe = **1** persons (2025-10-01..2025-10-31) [keep: ] quote: "Saisonbereinigt hat sie sich gegenüber dem Vormonat mit - 1.000 so gut wie nicht verändert."
  - p26 Germany underemployment seasonally adjusted month-on-month change, October 2025 = **14** persons (2025-10-01..2025-10-31) [keep: ] quote: "Sie ist saisonbereinigt gegenüber dem Vormonat um 14.000 gesunken."
  - p27 Germany ILO unemployment rate, September 2025 = **4.1** as written "4,1 Prozent", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im September auf 4,1 Prozent."
  - p28 Germany registered job vacancies at BA, October 2025 = **623** jobs (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober waren 623.000 Arbeitsstellen bei der BA gemeldet, 66.000 weniger als vor einem Jahr."
  - p29 Germany registered job vacancies year-on-year change, October 2025 = **66** jobs (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober waren 623.000 Arbeitsstellen bei der BA gemeldet, 66.000 weniger als vor einem Jahr."
  - p30 Germany BA-X labour demand index, October 2025 = **97** index points (2025-10-01..2025-10-31) [keep: ] quote: "sank im Oktober 2025 um 1 Punkt auf 97 Punkte."
  - p31 Germany recipients of unemployment benefit (Arbeitslosengeld), October 2025 = **984** persons (2025-10-01..2025-10-31) [keep: ] quote: "984.000 Personen erhielten nach Hochrechnung der BA im Oktober 2025 Arbeitslosengeld, 104.000 mehr als vor einem Jahr."
- `https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Interaktive-Statistiken/Zeitreihen/Lange-Zeitreihen-Nav.html` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- dropped by code checks: 14 (number: ambiguous separators: '.' used as a thousands separator: 11; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 2)

### d2 [related_series] BA press releases and monthly reports for the most recent months before cutoff

Hypothesis: The latest published monthly level and its reported month-on-month change give the base level; applying the historical average September-to-October seasonal increment yields the October 2026 estimate.

Queries issued by the searcher: Bundesagentur für Arbeit Pressemitteilung September 2026 Arbeitslose; Arbeitsmarkt August 2026 Arbeitslosenzahl Bundesagentur für Arbeit; "Arbeitsmarkt im Juli 2026" Bundesagentur für Arbeit Presseinfo Arbeitslose drei Millionen; Bundesagentur für Arbeit Oktober Arbeitslosigkeit saisonüblich Anstieg durchschnittlich letzten Jahre Oktober September

- `https://www.arbeitsagentur.de/presse/2026-37-arbeitsmarkt-im-september-2026` -> **live_dated** (page date 2026-09-30); points raw/verified 15/8
  - p32 Registered unemployment rate in Germany, September 2026 (not seasonally adjusted = **6.4** as written "6,4", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,4 Prozent."
  - p33 Month-on-month change in registered unemployment rate in Germany, September 2026 = **-0.1** as written "-0,1", value check pending percentage points (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,4 Prozent"
  - p34 Year-on-year change in registered unemployed persons in Germany, September 2026 = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +40.000"
  - p35 Seasonally adjusted month-on-month change in registered unemployed persons in Ge = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p36 Seasonally adjusted month-on-month change in underemployment in Germany, Septemb = **7** persons (2026-09-01..2026-09-30) [keep: ] quote: "Sie ist saisonbereinigt im September gegenüber dem Vormonat um 7.000 gesunken."
  - p37 Registered job vacancies at BA in Germany, September 2026 = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
  - p38 BA-X job vacancy index in Germany, September 2026 = **104** index points (2026-09-01..2026-09-30) [keep: ] quote: "stieg im September 2026 um 1 Punkt auf 104 Punkte"
  - p39 ILO unemployment rate in Germany, August 2026 = **4.3** as written "4,3", value check pending percent (2026-08-01..2026-08-31) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im August auf 4,3 Prozent."
- `https://www.arbeitsagentur.de/presse/2026-31-arbeitsmarkt-im-august-2026` -> **live_dated** (page date 2026-08-28); points raw/verified 15/10
  - p40 Germany registered unemployed stock, August 2026, seasonally adjusted month-on-m = **4** persons (2026-08-01..2026-08-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 4.000 höher."
  - p41 Germany registered unemployed year-on-year change, August 2026 = **36** persons (2026-08-01..2026-08-31) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +36.000"
  - p42 Germany unemployment rate, August 2026, not seasonally adjusted = **6.5** as written "6,5 Prozent", value check pending percent (2026-08-01..2026-08-31) [keep: ] quote: "Die Arbeitslosenquote stieg um 0,1 Prozentpunkte auf 6,5 Prozent."
  - p43 Germany unemployment rate month-on-month change, August 2026 = **0.1** as written "+0,1 Prozentpunkte", value check pending percentage points (2026-08-01..2026-08-31) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: +0,1 Prozentpunkte auf 6,5 Prozent"
  - p44 Germany underemployment seasonally adjusted month-on-month change, August 2026 = **3** persons (2026-08-01..2026-08-31) [keep: ] quote: "Sie ist saisonbereinigt im August gegenüber dem Vormonat um 3.000 gesunken."
  - p45 Germany underemployment year-on-year change, August 2026 = **33** persons (2026-08-01..2026-08-31) [keep: ] quote: "Mit 3.674.000 war sie um 33.000 höher als vor einem Jahr."
  - p46 Germany ILO unemployment rate, July 2026 = **4.2** as written "4,2 Prozent", value check pending percent (2026-07-01..2026-07-31) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im Juli auf 4,2 Prozent."
  - p47 Germany registered job vacancies stock, August 2026 = **656** jobs (2026-08-01..2026-08-31) [keep: ] quote: "Im August waren 656.000 Arbeitsstellen bei der BA gemeldet, 25.000 mehr als vor einem Jahr."
  - p48 Germany BA-X job vacancy index, August 2026 = **103** index points (2026-08-01..2026-08-31) [keep: ] quote: "blieb im August 2026 unverändert bei 103 Punkten"
  - p49 Germany employed persons (Inlandskonzept), July 2026, seasonally adjusted month- = **14** persons (2026-07-01..2026-07-31) [keep: ] quote: "hat sich die Zahl der Erwerbstätigen (nach dem Inlandskonzept) im Juli 2026 saisonbereinigt gegenüber dem Vormonat um 14.000 verringert."
- `https://www.arbeitsagentur.de/presse/2026-30-arbeitsmarkt-im-juli-2026` -> **live_dated** (page date 2026-07-31); points raw/verified 15/10
  - p50 Germany registered unemployed month-on-month change, July 2026, not seasonally a = **71** persons (2026-07-01..2026-07-31) [keep: ] quote: "Arbeitslosenzahl im Juli: +71.000 auf 3.007.000"
  - p51 Germany registered unemployed stock, July 2026, seasonally adjusted month-on-mon = **6** persons (2026-07-01..2026-07-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 6.000 höher."
  - p52 Germany registered unemployed year-on-year change, July 2026 = **28** persons (2026-07-01..2026-07-31) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +28.000"
  - p53 Germany unemployment rate, July 2026, not seasonally adjusted = **6.4** as written "6,4 Prozent", value check pending percent (2026-07-01..2026-07-31) [keep: ] quote: "Die Arbeitslosenquote stieg um 0,2 Prozentpunkte auf 6,4 Prozent."
  - p54 Germany unemployment rate month-on-month change, July 2026 = **0.2** as written "+0,2 Prozentpunkte", value check pending percentage points (2026-07-01..2026-07-31) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: +0,2 Prozentpunkte auf 6,4 Prozent"
  - p55 Germany underemployment year-on-year change, July 2026 = **28** persons (2026-07-01..2026-07-31) [keep: ] quote: "Mit 3.645.000 war sie um 28.000 höher als vor einem Jahr."
  - p56 Germany registered job vacancies stock, July 2026 = **653** jobs (2026-07-01..2026-07-31) [keep: ] quote: "Im Juli waren 653.000 Arbeitsstellen bei der BA gemeldet, 25.000 mehr als vor einem Jahr."
  - p57 Germany BA-X labour demand index, July 2026 = **103** index points (2026-07-01..2026-07-31) [keep: ] quote: "blieb im Juli 2026 unverändert bei 103 Punkten"
  - p58 Germany employed persons seasonally adjusted month-on-month change, June 2026 = **23** persons (2026-06-01..2026-06-30) [keep: ] quote: "hat sich die Zahl der Erwerbstätigen (nach dem Inlandskonzept) im Juni 2026 saisonbereinigt gegenüber dem Vormonat um 23.000 verringert"
  - p59 Germany ILO unemployment rate, June 2026 = **4** as written "4,0 Prozent", value check pending percent (2026-06-01..2026-06-30) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im Juni auf 4,0 Prozent."
- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202608/arbeitsmarktberichte/lage-arbeitsmarkt/lage-arbeitsmarkt-d-0-202608-pdf.pdf?__blob=pu` -> **live_dated** (page date 2026-08-01); points raw/verified 15/8
  - p60 Month-on-month change in registered unemployed persons, Germany, July to August  = **54** persons (2026-08-01..2026-08-31) [keep: ] quote: "Die Arbeitslosigkeit hat im Vergleich zum Juli um 54.000 zugenommen."
  - p61 Seasonally adjusted month-on-month change in registered unemployed persons, Germ = **4** persons (2026-08-01..2026-08-31) [keep: ] quote: "Saisonbereinigt ergibt sich ein Anstieg um 4.000."
  - p62 Year-on-year change in registered unemployed persons, Germany, August 2026 vs Au = **36** persons (2026-08-01..2026-08-31) [keep: ] quote: "Gegenüber August 2025 hat sich die Arbeitslosigkeit um 36.000 oder 1 Prozent erhöht."
  - p63 Unemployment rate, Germany, August 2026 = **6.5** as written "6,5%", value check pending % (2026-08-01..2026-08-31) [keep: ] quote: "6,4% 6,4% 6,5%"
  - p64 Unemployment rate, Germany, July 2026 = **6.4** as written "6,4%", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "6,4% 6,4% 6,5%"
  - p65 Month-on-month change in registered unemployed persons in Rechtskreis SGB III, G = **27** persons (2026-08-01..2026-08-31) [keep: ] quote: "In der Arbeitslosenversicherung (SGB III) ist die Arbeitslosigkeit im August gegenüber dem Vormonat um 27.000 gestiegen."
  - p66 Month-on-month change in registered unemployed persons in Rechtskreis SGB II, Ge = **28** persons (2026-08-01..2026-08-31) [keep: ] quote: "In der Grundsicherung für Arbeitsuchende (SGB II) waren im aktuellen Berichtsmonat 28.000 Menschen mehr arbeitslos gemeldet als im Juli."
  - p67 Registered unemployed persons under 25 years, Germany, August 2026 = **326** persons (2026-08-01..2026-08-31) [keep: ] quote: "Die Arbeitslosigkeit von jungen Menschen unter 25 Jahren ist von Juli auf August um 26.000 auf 326.000 gestiegen."
- dropped by code checks: 24 (number: ambiguous separators: '.' used as a thousands separator: 15; value_as_written not in quote as a whole number: 2; scale word 'million' not supported by quote or table header: 4; number: unknown scale word 'Mio': 2; period_end missing or unparseable: 1)

### d3 [related_series] Eurostat / OECD harmonised unemployment series for Germany

Hypothesis: Harmonised unemployment (ILO definition) levels and month-on-month changes for Germany track the registered series with a roughly stable ratio; the ratio can bridge from a harmonised estimate to the registered stock.

Queries issued by the searcher: Eurostat une_rt_m Germany harmonised unemployment level thousands monthly unadjusted; Germany registered unemployed vs ILO harmonised unemployed ratio Bundesagentur für Arbeit; Bundesagentur für Arbeit Pressemitteilung Arbeitsmarkt Oktober 2025 Arbeitslose 2,9 Millionen; statistik.arbeitsagentur.de Monatsbericht Oktober 2025 Erwerbslose ILO Arbeitslose Tabelle

- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202601/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-202601-pdf.pdf` -> **live_dated** (page date 2026-01-01); points raw/verified 14/3
  - p68 Germany ILO unemployment rate, December, percent = **3.6** as written "3,6 Prozent", value check pending percent (2025-12-01..2025-12-31) [keep: ] quote: "für den Dezember auf 1,60 Mio und die Erwerbslosenquote auf 3,6 Prozent."
  - p69 Germany registered unemployment rate (SGB III), December, percent = **6.2** as written "6,2 Prozent", value check pending percent (2025-12-01..2025-12-31) [keep: ] quote: "Die registrierte Arbeitslosigkeit nach dem Sozialgesetzbuch III betrug im gleichen Monat 2,91 Mio und die Arbeitslosenquote 6,2 Prozent."
  - p70 Germany seasonally adjusted registered unemployment rate, January 2026, percent = **6.3** as written "6,3 Prozent", value check pending percent (2026-01-01..2026-01-31) [keep: ] quote: "Saisonbereinigt blieb sie unverändert bei 6,3 Prozent."
- `https://www.arbeitsagentur.de/presse/2025-44-arbeitsmarkt-im-oktober-2025` -> **live_dated** (page date 2025-10-30); points raw/verified 15/12
  - p71 Month-on-month change in registered unemployed persons in Germany, October 2025 = **-44** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Oktober: -44.000 auf 2.911.000"
  - p72 Year-on-year change in registered unemployed persons in Germany, October 2025 = **120** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +120.000"
  - p73 Registered unemployment rate in Germany, October 2025 = **6.2** as written "6,2 Prozent", value check pending percent (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,2 Prozent."
  - p74 Month-on-month change in registered unemployment rate in Germany, October 2025 = **-0.1** as written "-0,1 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,2 Prozent"
  - p75 Year-on-year change in registered unemployment rate in Germany, October 2025 = **0.2** as written "0,2 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote hat sich gegenüber dem Vorjahresmonat um 0,2 Prozentpunkte erhöht."
  - p76 Seasonally adjusted month-on-month change in registered unemployed persons in Ge = **1** persons (2025-10-01..2025-10-31) [keep: ] quote: "Saisonbereinigt hat sie sich gegenüber dem Vormonat mit - 1.000 so gut wie nicht verändert."
  - p77 ILO harmonised unemployment rate for Germany (Statistisches Bundesamt), Septembe = **4.1** as written "4,1 Prozent", value check pending percent (2025-09-01..2025-09-30) [keep: ] quote: "Die vom Statistischen Bundesamt nach dem ILO-Erwerbskonzept ermittelte Erwerbslosenquote belief sich im September auf 4,1 Prozent."
  - p78 Seasonally adjusted month-on-month change in underemployment in Germany, October = **14** persons (2025-10-01..2025-10-31) [keep: ] quote: "Sie ist saisonbereinigt gegenüber dem Vormonat um 14.000 gesunken."
  - p79 Persons with notified cyclical short-time work in Germany, 1-26 October 2025 = **37** persons (2025-10-01..2025-10-26) [keep: ] quote: "Nach aktuellen Daten wurde vom 1. bis einschließlich 26. Oktober für 37.000 Personen konjunkturelle Kurzarbeit angezeigt."
  - p80 Employees receiving cyclical short-time work allowance in Germany, August 2025 ( = **171** persons (2025-08-01..2025-08-31) [keep: ] quote: "In diesem Monat wurde nach vorläufigen hochgerechneten Daten für 171.000 Beschäftigte konjunkturelles Kurzarbeitergeld gezahlt."
  - p81 Registered job vacancies at BA in Germany, October 2025 = **623** jobs (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober waren 623.000 Arbeitsstellen bei der BA gemeldet, 66.000 weniger als vor einem Jahr."
  - p82 Persons receiving unemployment benefit (Arbeitslosengeld) in Germany, October 20 = **984** persons (2025-10-01..2025-10-31) [keep: ] quote: "984.000 Personen erhielten nach Hochrechnung der BA im Oktober 2025 Arbeitslosengeld, 104.000 mehr als vor einem Jahr."
- `https://www.hiddenmetrix.com/data/labour/eurostat-germany-harmonised-unemployment-eurostat-data` -> **live_dated** (page date 2026-08-31); points raw/verified 15/1
  - p83 Harmonised unemployment in Germany (Eurostat), month-on-month change, August 202 = **0.51** % (2026-08-01..2026-08-31) [DISCARD: Already discarded; harmonised m/m change with unclear units and no usable bridge to the registered stock.] quote: "Veränderung+0.51 %"
- `https://ec.europa.eu/eurostat/databrowser/view/une_rt_m/default/table` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 28 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3; scale word 'million' not supported by quote or table header: 2; number: ambiguous separators: '.' used as a thousands separator: 7; scale word 'thousand' not supported by quote or table header: 2; number: unknown scale word 'Tsd.': 14)

### d4 [forecasts_markets] Economic research institutes, Bundesbank, and consensus forecasters

Hypothesis: Published forecasts of German unemployment for late 2026 (levels or rates) constrain the October 2026 stock; converting a forecast unemployment rate via labour force gives an independent estimate.

Queries issued by the searcher: Gemeinschaftsdiagnose Herbst 2026 Arbeitslosigkeit Prognose; IAB Arbeitsmarktprognose 2026 Arbeitslose; Gemeinschaftsdiagnose Herbst 2026 Arbeitslosenzahl Millionen 2027 Arbeitslosenquote Prognose Tabelle; Bundesbank Monatsbericht Oktober 2026 Arbeitsmarkt Arbeitslosigkeit

- `https://gemeinschaftsdiagnose.de/wp-content/uploads/2026/09/GD26H_PM_de.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/1
  - p84 Actual unemployment rate BA (unemployed as % of civilian labour force), 2025 = **6.3** as written "6,3", value check pending percent of civilian labour force (2025-01-01..2025-12-31) [DISCARD: Annual average rate, not a monthly stock; adds nothing beyond p2/p32.] quote: "Arbeitslosenquote BA3 (in %) 5,7 6,0 6,3 6,4 6,2 5,8"
- `https://doku.iab.de/kurzber/2026/kb2026-17.pdf` -> **live_dated** (page date 2026-09-22); points raw/verified 15/1
  - p85 IAB forecast: carry-over (Überhang) of SGB III unemployed at start of 2026 = **40** persons (2026-01-01..2026-01-01) [DISCARD: IAB carry-over forecast for start of 2026, not applicable to October 2026 stock.] quote: "Im Jahresdurchschnitt 2026 steigt sie um rund 80.000 Personen auf 1,18 Millionen, auch wegen eines Überhangs von rund 40.000 zu Jahresbeginn."
- `https://iab.de/presseinfo/iab-prognose-fuer-2026-fiskalpolitischer-rueckenwind-trifft-auf-geopolitischen-gegenwind/` -> **live_dated** (page date 2026-03-27); points raw/verified 11/0
- `https://gemeinschaftsdiagnose.de/2026/09/24/gemeinschaftsdiagnose-herbst-2026-aufschwung-mit-strukturproblemen-finanzpolitik-auf-abwegen/` -> **live_dated** (page date 2026-09-24); points raw/verified 0/0
- dropped by code checks: 39 (scale word 'thousand' not supported by quote or table header: 15; period_end 2026-12-31 after as_of: 11; period_end 2027-12-31 after as_of: 3; period_end 2028-12-31 after as_of: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; scale word 'million' not supported by quote or table header: 3; number: low/high given but value_as_written is not a range: 1)

### d5 [physical_flow] Labour market flow accounting (BA Arbeitsmarkt in Zahlen)

Hypothesis: The stock equals the previous stock plus inflows (Zugänge in Arbeitslosigkeit) minus outflows (Abgänge aus Arbeitslosigkeit); October inflows rise seasonally as summer jobs and training contracts end, so the net flow is typically positive.

Queries issued by the searcher: BA Zugänge Abgänge Arbeitslosigkeit Monatszahlen Oktober; Arbeitsmarkt in Zahlen Zu- und Abgänge Arbeitslosigkeit Oktober Bundesagentur für Arbeit; "Eckwerte des Arbeitsmarktes" Oktober 2025 Zugang an Arbeitslosen Abgang Deutschland pdf; statistik.arbeitsagentur.de "Arbeitslosigkeit im Zeitverlauf" Zugang Abgang Bestand Monate 2025

- `https://www.arbeitsagentur.de/presse/2025-44-arbeitsmarkt-im-oktober-2025` -> **live_dated** (page date 2025-10-30); points raw/verified 15/13
  - p86 Change in registered unemployed persons in Germany, month-on-month, October 2025 = **-44** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Oktober: -44.000 auf 2.911.000"
  - p87 Change in registered unemployed persons in Germany, year-on-year, October 2025 = **120** persons (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +120.000"
  - p88 Unemployment rate in Germany, not seasonally adjusted, October 2025 = **6.2** as written "6,2 Prozent", value check pending percent (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,2 Prozent."
  - p89 Change in unemployment rate in Germany, month-on-month, October 2025 = **-0.1** as written "-0,1 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,2 Prozent"
  - p90 Change in unemployment rate in Germany, year-on-year, October 2025 = **0.2** as written "0,2 Prozentpunkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote hat sich gegenüber dem Vorjahresmonat um 0,2 Prozentpunkte erhöht."
  - p91 Change in registered unemployed persons in Germany, seasonally adjusted, month-o = **1** persons (2025-10-01..2025-10-31) [keep: ] quote: "Saisonbereinigt hat sie sich gegenüber dem Vormonat mit - 1.000 so gut wie nicht verändert."
  - p92 Change in underemployment in Germany, seasonally adjusted, month-on-month, Octob = **14** persons (2025-10-01..2025-10-31) [keep: ] quote: "Sie ist saisonbereinigt gegenüber dem Vormonat um 14.000 gesunken."
  - p93 Persons with notified cyclical short-time work (Kurzarbeit), 1-26 October 2025 = **37** persons (2025-10-01..2025-10-26) [keep: ] quote: "Nach aktuellen Daten wurde vom 1. bis einschließlich 26. Oktober für 37.000 Personen konjunkturelle Kurzarbeit angezeigt."
  - p94 Employees receiving cyclical short-time work allowance, August 2025 (provisional = **171** employees (2025-08-01..2025-08-31) [keep: ] quote: "In diesem Monat wurde nach vorläufigen hochgerechneten Daten für 171.000 Beschäftigte konjunkturelles Kurzarbeitergeld gezahlt."
  - p95 Change in employees receiving cyclical short-time work allowance, month-on-month = **32** employees (2025-08-01..2025-08-31) [keep: ] quote: "Das waren 32.000 weniger als im Vormonat, aber 6.000 mehr als im August des Vorjahres."
  - p96 Registered job vacancies at BA, October 2025 = **623** jobs (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober waren 623.000 Arbeitsstellen bei der BA gemeldet, 66.000 weniger als vor einem Jahr."
  - p97 BA job index (BA-X), October 2025 = **97** points (2025-10-01..2025-10-31) [keep: ] quote: "sank im Oktober 2025 um 1 Punkt auf 97 Punkte."
  - p98 Persons receiving unemployment benefit (Arbeitslosengeld) in Germany, October 20 = **984** persons (2025-10-01..2025-10-31) [keep: ] quote: "984.000 Personen erhielten nach Hochrechnung der BA im Oktober 2025 Arbeitslosengeld, 104.000 mehr als vor einem Jahr."
- `https://web.arbeitsagentur.de/cms-dezentrale-dst-redaktion-prod-media/prodddst/s3fs-public/2025-10/317-AMR-2025-10-Agenturbezirk.pdf` -> **live_dated** (page date 2025-10-01); points raw/verified 15/15
  - p99 Stock of registered unemployed, Agentur für Arbeit Bielefeld, October 2025 = **27.7** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld agency-level stock; no reliable scaling to national total and not needed.] quote: "Bestand an Arbeitslosen Insgesamt 27.704 28.154 28.870 -450 -1,6 482 1,8 2,2 1,9"
  - p100 Stock of registered unemployed, Agentur für Arbeit Bielefeld, September 2025 = **28.15** persons (2025-09-01..2025-09-30) [DISCARD: Bielefeld agency-level stock; local scope, unusable for national target.] quote: "Bestand an Arbeitslosen Insgesamt 27.704 28.154 28.870 -450 -1,6 482 1,8 2,2 1,9"
  - p101 Stock of registered unemployed, Agentur für Arbeit Bielefeld, August 2025 = **28.87** persons (2025-08-01..2025-08-31) [DISCARD: Bielefeld agency-level stock; local scope, unusable for national target.] quote: "Bestand an Arbeitslosen Insgesamt 27.704 28.154 28.870 -450 -1,6 482 1,8 2,2 1,9"
  - p102 Inflows (Zugang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, October 20 = **5.085** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld inflows; local flow, no national scaling evidence.] quote: "Zugang an Arbeitslosen Insgesamt 5.085 4.281 4.692 804 18,8 470 10,2 3,7 1,4"
  - p103 Inflows (Zugang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, September  = **4.281** persons (2025-09-01..2025-09-30) [DISCARD: Bielefeld inflows; local flow, no national scaling evidence.] quote: "Zugang an Arbeitslosen Insgesamt 5.085 4.281 4.692 804 18,8 470 10,2 3,7 1,4"
  - p104 Inflows (Zugang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, August 202 = **4.692** persons (2025-08-01..2025-08-31) [DISCARD: Bielefeld inflows; local flow, no national scaling evidence.] quote: "Zugang an Arbeitslosen Insgesamt 5.085 4.281 4.692 804 18,8 470 10,2 3,7 1,4"
  - p105 Outflows (Abgang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, October 2 = **5.56** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld outflows; local flow, no national scaling evidence.] quote: "Abgang an Arbeitslosen Insgesamt 5.560 4.996 4.502 564 11,3 608 12,3 1,7 -1,1"
  - p106 Outflows (Abgang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, September = **4.996** persons (2025-09-01..2025-09-30) [DISCARD: Bielefeld outflows; local flow, no national scaling evidence.] quote: "Abgang an Arbeitslosen Insgesamt 5.560 4.996 4.502 564 11,3 608 12,3 1,7 -1,1"
  - p107 Outflows (Abgang an Arbeitslosen) total, Agentur für Arbeit Bielefeld, August 20 = **4.502** persons (2025-08-01..2025-08-31) [DISCARD: Bielefeld outflows; local flow, no national scaling evidence.] quote: "Abgang an Arbeitslosen Insgesamt 5.560 4.996 4.502 564 11,3 608 12,3 1,7 -1,1"
  - p108 Inflows from employment (Zugang aus Erwerbstätigkeit), Agentur für Arbeit Bielef = **1.828** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld inflow component; local scope.] quote: "dar. aus Erwerbstätigkeit 1.828 1.718 1.900 110 6,4 14 0,8 1,4 1,5"
  - p109 Inflows from training/other measures (Zugang aus Ausbildung/sonst. Maßnahme), Ag = **1.5** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld inflow component; local scope.] quote: "aus Ausbildung/sonst. Maßnahme 1.500 1.094 1.272 406 37,1 359 31,5 11,7 10,0"
  - p110 Outflows into employment (Abgang in Erwerbstätigkeit), Agentur für Arbeit Bielef = **1.835** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld outflow component; local scope.] quote: "dar. in Erwerbstätigkeit 1.835 1.782 1.359 53 3,0 139 8,2 4,7 -3,4"
  - p111 Outflows into training/other measures (Abgang in Ausbildung/sonst. Maßnahme), Ag = **1.633** persons (2025-10-01..2025-10-31) [DISCARD: Bielefeld outflow component; local scope.] quote: "in Ausbildung/sonst. Maßnahme 1.633 1.429 1.127 204 14,3 324 24,8 -1,7 0,6"
  - p112 Cumulative inflows since start of year (Zugang seit Jahresbeginn), Agentur für A = **45.17** persons (2025-01-01..2025-10-31) [DISCARD: Bielefeld cumulative inflows; local scope.] quote: "seit Jahresbeginn 45.173 40.088 35.807 x x -330 -0,7 -2,0 -2,6"
  - p113 Cumulative outflows since start of year (Abgang seit Jahresbeginn), Agentur für  = **44.76** persons (2025-01-01..2025-10-31) [DISCARD: Bielefeld cumulative outflows; local scope.] quote: "seit Jahresbeginn 44.764 39.204 34.208 x x 1.039 2,4 1,1 1,0"
- `https://www.arbeitsagentur.de/vor-ort/datei/arbeitsmarktbericht_oktober_2025_chemnitz_ba255573.pdf` -> **live_dated** (page date 2025-11-06); points raw/verified 15/15
  - p114 Stock of registered unemployed, Agentur für Arbeit Chemnitz, October 2025 = **12.26** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz agency-level stock; local scope.] quote: "Bestand an Arbeitslosen Insgesamt 12.260 12.313 12.480 -53 -0,4 915 8,1 9,6 9,6"
  - p115 Stock of registered unemployed, Agentur für Arbeit Chemnitz, September 2025 = **12.31** persons (2025-09-01..2025-09-30) [DISCARD: Chemnitz agency-level stock; local scope.] quote: "Bestand an Arbeitslosen Insgesamt 12.260 12.313 12.480 -53 -0,4 915 8,1 9,6 9,6"
  - p116 Stock of registered unemployed, Agentur für Arbeit Chemnitz, August 2025 = **12.48** persons (2025-08-01..2025-08-31) [DISCARD: Chemnitz agency-level stock; local scope.] quote: "Bestand an Arbeitslosen Insgesamt 12.260 12.313 12.480 -53 -0,4 915 8,1 9,6 9,6"
  - p117 Zugang an Arbeitslosen (inflows), Agentur für Arbeit Chemnitz, October 2025 = **2.233** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz inflows; local scope.] quote: "Zugang an Arbeitslosen Insgesamt 2.233 2.001 2.032 232 11,6 175 8,5 -2,1 8,5"
  - p118 Zugang an Arbeitslosen (inflows), Agentur für Arbeit Chemnitz, September 2025 = **2.001** persons (2025-09-01..2025-09-30) [DISCARD: Chemnitz inflows; local scope.] quote: "Zugang an Arbeitslosen Insgesamt 2.233 2.001 2.032 232 11,6 175 8,5 -2,1 8,5"
  - p119 Zugang an Arbeitslosen (inflows), Agentur für Arbeit Chemnitz, August 2025 = **2.032** persons (2025-08-01..2025-08-31) [DISCARD: Chemnitz inflows; local scope.] quote: "Zugang an Arbeitslosen Insgesamt 2.233 2.001 2.032 232 11,6 175 8,5 -2,1 8,5"
  - p120 Abgang an Arbeitslosen (outflows), Agentur für Arbeit Chemnitz, October 2025 = **2.329** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz outflows; local scope.] quote: "Abgang an Arbeitslosen Insgesamt 2.329 2.208 2.064 121 5,5 343 17,3 -0,4 7,1"
  - p121 Abgang an Arbeitslosen (outflows), Agentur für Arbeit Chemnitz, September 2025 = **2.208** persons (2025-09-01..2025-09-30) [DISCARD: Chemnitz outflows; local scope.] quote: "Abgang an Arbeitslosen Insgesamt 2.329 2.208 2.064 121 5,5 343 17,3 -0,4 7,1"
  - p122 Abgang an Arbeitslosen (outflows), Agentur für Arbeit Chemnitz, August 2025 = **2.064** persons (2025-08-01..2025-08-31) [DISCARD: Chemnitz outflows; local scope.] quote: "Abgang an Arbeitslosen Insgesamt 2.329 2.208 2.064 121 5,5 343 17,3 -0,4 7,1"
  - p123 Zugang an Arbeitslosen seit Jahresbeginn (cumulative inflows Jan–Oct), Agentur f = **20.53** persons (2025-01-01..2025-10-31) [DISCARD: Chemnitz cumulative inflows; local scope.] quote: "seit Jahresbeginn 20.526 18.293 16.292 x x 1.144 5,9 5,6 6,6"
  - p124 Abgang an Arbeitslosen seit Jahresbeginn (cumulative outflows Jan–Oct), Agentur  = **20.09** persons (2025-01-01..2025-10-31) [DISCARD: Chemnitz cumulative outflows; local scope.] quote: "seit Jahresbeginn 20.095 17.766 15.558 x x 1.142 6,0 4,7 5,5"
  - p125 Zugang an Arbeitslosen aus Erwerbstätigkeit, Agentur für Arbeit Chemnitz, Octobe = **725** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz inflow component; local scope.] quote: "dar. aus Erwerbstätigkeit 725 687 665 38 5,5 82 12,8 17,2 16,5"
  - p126 Zugang an Arbeitslosen aus Ausbildung/sonst. Maßnahme, Agentur für Arbeit Chemni = **676** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz inflow component; local scope.] quote: "aus Ausbildung/sonst. Maßnahme 676 677 688 -1 -0,1 47 7,5 -12,3 10,4"
  - p127 Abgang an Arbeitslosen in Erwerbstätigkeit, Agentur für Arbeit Chemnitz, October = **663** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz outflow component; local scope.] quote: "dar. in Erwerbstätigkeit 663 670 606 -7 -1,0 87 15,1 15,5 16,8"
  - p128 Abgang an Arbeitslosen in Ausbildung/sonst. Maßnahme, Agentur für Arbeit Chemnit = **740** persons (2025-10-01..2025-10-31) [DISCARD: Chemnitz outflow component; local scope.] quote: "in Ausbildung/sonst. Maßnahme 740 728 660 12 1,6 101 15,8 -14,4 -3,4"
- `https://www.braunschweig.de/politik_verwaltung/fb_institutionen/fachbereiche_referate/fb01/ref0120/stadtforschung/infoline_stafo_2016_01_ARMAR_Arbeits` -> **live_dated** (page date 2016-01-01); points raw/verified 15/9
  - p129 Germany (Bund) change in registered unemployed vs previous month, December 2015  = **48.26** persons (2015-12-01..2015-12-31) [DISCARD: December 2015 national change; too old and wrong month for October 2026.] quote: "122 182 52 102 77 44 17 86 682 5.341 48.258"
  - p130 Germany (Bund) change in registered unemployed vs previous month, December 2015  = **1.8** as written "1,8", value check pending percent (2015-12-01..2015-12-31) [DISCARD: December 2015 percent change; too old and wrong month.] quote: "1,5 3,9 1,8 2,5 1,5 1,4 0,5 2,7 2,0 2,2 1,8"
  - p131 Germany (Bund) change in registered unemployed vs previous year, December 2015 ( = **-82.11** persons (2015-12-01..2015-12-31) [DISCARD: December 2015 y/y change; too old and wrong month.] quote: "-558 105 24 -119 -519 -262 -144 -146 -1.619 -8.401 -82.106"
  - p132 Braunschweig city Zugänge in Arbeitslosigkeit (inflows), October 2015 = **1.922** persons (2015-10-01..2015-10-31) [DISCARD: Braunschweig city inflows; local scope.] quote: "Okt 15 1.922 2.190 -268 -168 -329 161 -334 -249 -85"
  - p133 Braunschweig city Abgänge aus Arbeitslosigkeit (outflows), October 2015 = **2.19** persons (2015-10-01..2015-10-31) [DISCARD: Braunschweig city outflows; local scope.] quote: "Okt 15 1.922 2.190 -268 -168 -329 161 -334 -249 -85"
  - p134 Braunschweig city net flow (Saldo Zugänge minus Abgänge), October 2015 = **-268** persons (2015-10-01..2015-10-31) [DISCARD: Braunschweig net flow; local scope.] quote: "Okt 15 1.922 2.190 -268 -168 -329 161 -334 -249 -85"
  - p135 Braunschweig city Zugänge in Arbeitslosigkeit (inflows), October 2014 = **2.256** persons (2014-10-01..2014-10-31) [DISCARD: Braunschweig 2014 inflows; local scope and old.] quote: "Okt 14 2.256 2.439 -183 269 -87 356 -145 90 -235"
  - p136 Braunschweig city Abgänge aus Arbeitslosigkeit (outflows), October 2014 = **2.439** persons (2014-10-01..2014-10-31) [DISCARD: Braunschweig 2014 outflows; local scope and old.] quote: "Okt 14 2.256 2.439 -183 269 -87 356 -145 90 -235"
  - p137 Braunschweig city net flow (Saldo Zugänge minus Abgänge), October 2014 = **-183** persons (2014-10-01..2014-10-31) [DISCARD: Braunschweig 2014 net flow; local scope and old.] quote: "Okt 14 2.256 2.439 -183 269 -87 356 -145 90 -235"
- dropped by code checks: 8 (number: ambiguous separators: '.' used as a thousands separator: 7; number: unknown scale word 'Mio.': 1)

### d6 [base_rates] Seasonal adjustment factors and calendar effects

Hypothesis: The unadjusted October figure equals the seasonally adjusted level times a seasonal factor; BA/ Eurostat seasonal factors for October are stable and can convert an adjusted-level estimate into the unadjusted target.

Queries issued by the searcher: Bundesagentur für Arbeit Arbeitslose saisonbereinigt Oktober 2026 Saisonfaktor; Eurostat seasonal adjustment unemployment Germany October factor; "Oktober 2025" Arbeitslose 2.9 Millionen saisonbereinigt Bundesagentur Pressemitteilung; statistik.arbeitsagentur.de Arbeitslosigkeit im Zeitverlauf Monatszahlen saisonbereinigt Ursprungswerte Tabelle; "September 2025" Arbeitslose saisonbereinigt "3,0" Millionen BA September 2025 saisonbereinigt gestiegen

- `https://www.faz.net/aktuell/wirtschaft/arbeitsmarktdaten-da-ist-eine-kleinigkeit-dazwischengekommen-nennt-sich-irankrieg-201275794.html` -> **live_dated** (page date 2026-09-30); points raw/verified 12/8
  - p138 Month-on-month change in registered unemployed persons, September vs August, not = **67** persons (2026-09-01..2026-09-30) [keep: ] quote: "Das sind 67.000 Menschen weniger als noch im Monat zuvor."
  - p139 Month-on-month change in registered unemployed persons, September, seasonally ad = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Rechnet man das heraus, ist die Zahl der Arbeitslosen nicht gesunken, sondern sogar leicht gestiegen - um 12.000 Personen."
  - p140 Unemployment rate in Germany, September = **6.4** as written "6,4 Prozent", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Damit beträgt die Arbeitslosenquote derzeit 6,4 Prozent."
  - p141 Month-on-month change in underemployment, September, seasonally adjusted = **7,000** persons (2026-09-01..2026-09-30) [keep: ] quote: "ging diese Zahl im Gegensatz zur Arbeitslosigkeit um 7000 Personen zurück."
  - p142 Registered vacancies reported to BA, stock, September = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September verzeichnete die BA 660.000 gemeldete Stellen."
  - p143 Year-on-year change in unemployment benefit recipients, September = **85** persons (2026-09-01..2026-09-30) [keep: ] quote: "Das seien 85.000 mehr als noch im Jahr zuvor."
  - p144 Year-on-year change in employable beneficiaries of basic security (Grundsicherun = **145** persons (2026-09-01..2026-09-30) [keep: ] quote: "Bei der Grundsicherung zählte die BA im Vergleich zum September 2025 145.000 erwerbsfähige Leistungsberechtigte weniger."
  - p145 Share of people of working age in Germany receiving basic security, September = **6.8** as written "6,8 Prozent", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "In Deutschland seien damit 6,8 Prozent der Menschen im erwerbsfähigen Alter hilfebedürftig."
- `https://www.arbeitsagentur.de/news/arbeitsmarkt?utm_source=carsten-paehlke.beehiiv.com&utm_medium=newsletter&utm_campaign=carsten-pahlke-karrierebrief` -> **live_dated** (page date 2026-09-30); points raw/verified 15/10
  - p146 Month-on-month change in unadjusted registered unemployed, Germany, September 20 = **67** persons (2026-09-01..2026-09-30) [keep: ] quote: "ist die Arbeitslosigkeit im September 2026 um 67.000 auf 2.994.000 zurückgegangen."
  - p147 Month-on-month change in seasonally adjusted registered unemployed, Germany, Sep = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p148 Month-on-month change in unadjusted registered unemployed, Germany, August 2026 = **54** persons (2026-08-01..2026-08-31) [keep: ] quote: "ist die Arbeitslosigkeit im August 2026 um 54.000 auf 3.061.000 gestiegen."
  - p149 Month-on-month change in seasonally adjusted registered unemployed, Germany, Aug = **4** persons (2026-08-01..2026-08-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 4.000 höher."
  - p150 Month-on-month change in unadjusted registered unemployed, Germany, July 2026 = **71** persons (2026-07-01..2026-07-31) [keep: ] quote: "ist die Arbeitslosigkeit im Juli 2026 um 71.000 auf 3.007.000 gestiegen."
  - p151 Month-on-month change in seasonally adjusted registered unemployed, Germany, Jul = **6** persons (2026-07-01..2026-07-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 6.000 höher."
  - p152 Month-on-month change in unadjusted registered unemployed, Germany, June 2026 = **15** persons (2026-06-01..2026-06-30) [keep: ] quote: "Die Arbeitslosigkeit ist im Juni 2026 um 15.000 auf 2.936.000 gesunken."
  - p153 Month-on-month change in seasonally adjusted registered unemployed, Germany, Jun = **1** persons (2026-06-01..2026-06-30) [keep: ] quote: "Saisonbereinigt hat sie gegenüber dem Vormonat um 1.000 abgenommen."
  - p154 Month-on-month change in unadjusted registered unemployed, Germany, May 2026 = **58** persons (2026-05-01..2026-05-31) [keep: ] quote: "Die Arbeitslosigkeit ist im Mai 2026 um 58.000 auf 2.950.000 gesunken."
  - p155 Month-on-month change in seasonally adjusted registered unemployed, Germany, May = **12** persons (2026-05-01..2026-05-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 12.000 niedriger."
- `https://statistik.arbeitsagentur.de/DE/Statischer-Content/Grundlagen/Methodik-Qualitaet/Qualitaetsberichte/Generische-Publikationen/Qualitaetsbericht-` -> **live_dated** (page date 2026-09-22); points raw/verified 0/0
- `https://lajme.mk/sa-eshte-numri-i-te-papuneve-ne-gjermani` -> **live_dated** (page date 2026-10-01); points raw/verified 5/0
- dropped by code checks: 14 (number: unknown scale word 'Millionen': 4; number: ambiguous separators: '.' used as a thousands separator: 5; scale word 'million' not supported by quote or table header: 2; period year 2026 does not appear in the page text or URL (likely mis-dated): 3)

### d7 [administrative] BA short-time work, job vacancies, and registration statistics

Hypothesis: Rising short-time work (Kurzarbeit) and falling vacancies signal weakening demand and upward pressure on unemployment; the direction and magnitude of recent changes inform the trend adjustment to the seasonal baseline.

Queries issued by the searcher: Bundesagentur für Arbeit Kurzarbeit Anzeigen 2026; gemeldete Arbeitsstellen 2026 Bundesagentur für Arbeit Arbeitsmarkt; "Arbeitsmarkt im September 2026" Bundesagentur für Arbeit Arbeitslose 2,9 Millionen Presseinfo 37; Arbeitslosigkeit Oktober 2026 Prognose Herbstbelebung Bundesagentur

- `https://www.arbeitsagentur.de/presse/2026-37-arbeitsmarkt-im-september-2026` -> **live_dated** (page date 2026-09-30); points raw/verified 15/13
  - p156 Registered unemployed in Germany, national total, September 2026 (monthly change = **-67** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im September: -67.000 auf 2.994.000"
  - p157 Registered unemployed in Germany, year-on-year change, September 2026 = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +40.000"
  - p158 Unemployment rate Germany, September 2026 = **6.4** as written "6,4 Prozent", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,4 Prozent."
  - p159 Seasonally adjusted change in registered unemployed, September 2026 vs previous  = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p160 Seasonally adjusted change in underemployment, September 2026 vs previous month = **7** persons (2026-09-01..2026-09-30) [keep: ] quote: "Sie ist saisonbereinigt im September gegenüber dem Vormonat um 7.000 gesunken."
  - p161 Kurzarbeit notifications (konjunkturelle Kurzarbeit), persons, 1-24 September 20 = **18** persons (2026-09-01..2026-09-24) [keep: ] quote: "wurde vom 1. bis einschließlich 24. September für 18.000 Personen konjunkturelle Kurzarbeit angezeigt"
  - p162 Realised konjunkturelles Kurzarbeitergeld recipients, July 2026 (preliminary) = **118** employees (2026-07-01..2026-07-31) [keep: ] quote: "wurde in diesem Monat für 118.000 Beschäftigte konjunkturelles Kurzarbeitergeld gezahlt"
  - p163 Change in realised Kurzarbeit recipients, July 2026 vs previous month = **13** employees (2026-07-01..2026-07-31) [keep: ] quote: "Das waren 13.000 weniger als im Vormonat und rund 69.000 weniger als vor einem Jahr."
  - p164 Change in realised Kurzarbeit recipients, July 2026 vs year earlier = **69** employees (2026-07-01..2026-07-31) [keep: ] quote: "Das waren 13.000 weniger als im Vormonat und rund 69.000 weniger als vor einem Jahr."
  - p165 Registered vacancies (gemeldete Arbeitsstellen) at BA, September 2026 = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
  - p166 Change in registered vacancies, September 2026 vs year earlier = **30** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
  - p167 BA-X job index Germany, September 2026 = **104** index points (2026-09-01..2026-09-30) [keep: ] quote: "stieg im September 2026 um 1 Punkt auf 104 Punkte"
  - p168 Seasonally adjusted change in employed persons (Inlandskonzept), August 2026 vs  = **29** persons (2026-08-01..2026-08-31) [keep: ] quote: "hat sich die Zahl der Erwerbstätigen (nach dem Inlandskonzept) im August 2026 saisonbereinigt gegenüber dem Vormonat um 29.000 verringert"
- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202609/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-202609-pdf.pdf?__b` -> **live_dated** (page date 2026-09-01); points raw/verified 15/5
  - p169 Short-time work share of sv-pflichtig Beschäftigte in manufacturing, percent, Ge = **1.5** as written "1,5 Prozent", value check pending percent (2026-06-01..2026-06-30) [keep: ] quote: "Danach bezogen in diesem Monat 1,5 Prozent der sozialversicherungspflichtig Beschäftigten im Verarbeitenden Gewerbe konjunkturelles Kurzarbeitergeld."
  - p170 Short-time work notifications (Anzeigen), persons, Germany, 1-24 September 2026 = **18** persons (2026-09-01..2026-09-24) [keep: ] quote: "Demnach wurde für 18.000 Personen konjunkturelle Kurzarbeit angezeigt."
  - p171 Registered vacancies, stock change vs previous year, Germany, September 2026 = **30** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im Vergleich zum Vorjahr lag der Stellenbestand im September 2026 um 30.000 höher."
  - p172 Registered vacancies, outflow (Abgang), Germany, September 2026 = **128** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September wurden 128.000 Arbeitsstellen abgemeldet, 11.000 mehr als im Vorjahr."
  - p173 BA job index (BA-X), points, Germany, September 2026 = **104** index points (2026-09-01..2026-09-30) [keep: ] quote: "Im September lag der Stellenindex bei 104 Punkten."
- `https://www.eu-stellenangebot.de/arbeitsmarkt-2026-zahlen-statistik-zu-stellen-arbeitslosigkeit-und-engpaessen-in-deutschland-europa/` -> **live_dated** (page date 2026-10-06); points raw/verified 15/12
  - p174 Change in registered unemployed Germany, not seasonally adjusted, September 2026 = **67** persons (2026-09-01..2026-09-30) [keep: ] quote: "Gegenüber August sank die nicht saisonbereinigte Zahl um 67.000 Personen."
  - p175 Change in registered unemployed Germany, seasonally adjusted, September 2026 vs  = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt nahm sie dagegen um 12.000 zu."
  - p176 Change in registered unemployed Germany, September 2026 vs September 2025 = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Gegenüber September 2025 wurden 40.000 Arbeitslose mehr registriert."
  - p177 BA unemployment rate Germany, September 2026 = **6.4** as written "6,4 Prozent", value check pending percent of civilian labour force (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote der Bundesagentur für Arbeit lag bei 6,4 Prozent."
  - p178 BA reported vacancies (gemeldete Arbeitsstellen) Germany, September 2026 = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Gleichzeitig waren im September 2026 bei der Arbeitsvermittlung 660.000 Arbeitsstellen gemeldet."
  - p179 Change in BA reported vacancies Germany, September 2026 vs September 2025 = **30** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Das waren 30.000 mehr als ein Jahr zuvor."
  - p180 Decline in IAB open jobs Germany, Q2 2026 vs Q1 2026 = **130** jobs (2026-04-01..2026-06-30) [DISCARD: IAB open-jobs decline Q2 2026; no calibrated link to registered unemployment stock.] quote: "Der Rückgang betrug damit 129.800 Stellen beziehungsweise laut Veröffentlichung rund 11 Prozent."
  - p181 Decline in IAB open jobs Germany, Q2 2026 vs Q1 2026, percent = **11** percent (2026-04-01..2026-06-30) [DISCARD: IAB open-jobs percent decline; no calibrated link to stock.] quote: "Der Rückgang betrug damit 129.800 Stellen beziehungsweise laut Veröffentlichung rund 11 Prozent."
  - p182 Share of IAB open jobs immediately fillable Germany, Q2 2026 = **81** percent of open jobs (2026-04-01..2026-06-30) [DISCARD: Share of immediately fillable jobs; not a stock driver.] quote: "Rund 81 Prozent der im zweiten Quartal erfassten offenen Stellen waren sofort zu besetzen."
  - p183 Employers responding to IAB survey Germany, Q2 2026 = **8.529** employers (2026-04-01..2026-06-30) [DISCARD: Survey respondent count; not a quantity for the target.] quote: "Im zweiten Quartal 2026 antworteten 8.529 Arbeitgeber."
  - p184 Job vacancy rate Germany, Q2 2026 = **2.4** as written "2,4 Prozent", value check pending percent of all posts (occupied and open) (2026-04-01..2026-06-30) [DISCARD: Job vacancy rate Q2 2026; no calibrated bridge to registered unemployment.] quote: "Für Deutschland wurden 2,4 Prozent ausgewiesen."
  - p185 Job vacancy rate EU-27, Q2 2026 = **2** as written "2,0 Prozent", value check pending percent of all posts (occupied and open) (2026-04-01..2026-06-30) [DISCARD: EU-27 vacancy rate; not Germany-specific.] quote: "Im zweiten Quartal 2026 lag die Quote offener Stellen in der EU bei 2,0 Prozent."
- `https://www.finanznachrichten.de/nachrichten-2026-09/69714587-arbeitsmarkt-im-september-2026-herbstbelebung-beginnt-ohne-schwung-ba-presseinfo-nr-37-0` -> **live_dated** (page date 2026-10-01); points raw/verified 15/13
  - p186 Registered unemployed in Germany, September 2026, month-on-month change (BA pres = **-67** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im September: -67.000 auf 2.994.000"
  - p187 Registered unemployed in Germany, September 2026, year-on-year change = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +40.000"
  - p188 Unemployment rate Germany, September 2026, month-on-month change in percentage p = **-0.1** as written "-0,1", value check pending percentage points (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenquote gegenüber Vormonat: -0,1 Prozentpunkte auf 6,4 Prozent"
  - p189 Unemployment rate Germany, September 2026 (not seasonally adjusted) = **6.4** as written "6,4", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,4 Prozent."
  - p190 Registered unemployed in Germany, September 2026, seasonally adjusted month-on-m = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p191 Underemployment Germany, September 2026, seasonally adjusted month-on-month chan = **7** persons (2026-09-01..2026-09-30) [keep: ] quote: "Sie ist saisonbereinigt im September gegenüber dem Vormonat um 7.000 gesunken."
  - p192 Kurzarbeit notifications (Anzeigen) for cyclical short-time work, 1-24 September = **18** persons (2026-09-01..2026-09-24) [keep: ] quote: "wurde vom 1. bis einschließlich 24. September für 18.000 Personen konjunkturelle Kurzarbeit angezeigt"
  - p193 Realised cyclical Kurzarbeit (Kurzarbeitergeld recipients), July 2026, prelimina = **118** employees (2026-07-01..2026-07-31) [keep: ] quote: "wurde in diesem Monat für 118.000 Beschäftigte konjunkturelles Kurzarbeitergeld gezahlt"
  - p194 Realised cyclical Kurzarbeit, July 2026, month-on-month change = **13** employees (2026-07-01..2026-07-31) [keep: ] quote: "Das waren 13.000 weniger als im Vormonat"
  - p195 Realised cyclical Kurzarbeit, July 2026, year-on-year change = **69** employees (2026-07-01..2026-07-31) [keep: ] quote: "rund 69.000 weniger als vor einem Jahr"
  - p196 Reported vacancies (gemeldete Arbeitsstellen) at BA, Germany, September 2026, st = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
  - p197 Reported vacancies at BA, September 2026, year-on-year change = **30** jobs (2026-09-01..2026-09-30) [keep: ] quote: "660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr"
  - p198 BA job index (BA-X), Germany, September 2026, level = **104** index points (2026-09-01..2026-09-30) [keep: ] quote: "stieg im September 2026 um 1 Punkt auf 104 Punkte"
- dropped by code checks: 17 (number: ambiguous separators: '.' used as a thousands separator: 8; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 9)

### d8 [shocks] Macro and policy shocks affecting German labour demand in 2026

Hypothesis: Specific shocks (industrial restructuring, automotive sector layoffs, energy prices, migration/refugee labour supply, policy changes) shift October 2026 away from the pure seasonal extrapolation; measurable exposure indicates the sign and rough size of the deviation.

Queries issued by the searcher: Stellenabbau Deutschland 2026 Automobilindustrie; Bürgergeld Reform 2026 Arbeitslose Statistik Bundesagentur für Arbeit; Arbeitslosenzahl September 2026 Bundesagentur für Arbeit Pressemitteilung; Arbeitsmarkt Oktober 2026 Herbstbelebung Arbeitslose Prognose

- `https://www.arbeitsagentur.de/presse/2026-37-arbeitsmarkt-im-september-2026` -> **live_dated** (page date 2026-09-30); points raw/verified 15/9
  - p199 Year-on-year change in registered unemployed persons in Germany, September 2026 = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Arbeitslosenzahl im Vorjahresvergleich: +40.000"
  - p200 Seasonally adjusted monthly change in registered unemployed persons in Germany,  = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p201 Unemployment rate in Germany, September 2026 = **6.4** as written "6,4 Prozent", value check pending percent (2026-09-01..2026-09-30) [keep: ] quote: "Die Arbeitslosenquote sank um 0,1 Prozentpunkte auf 6,4 Prozent."
  - p202 Persons for whom cyclical short-time work was notified, 1-24 September 2026 = **18** persons (2026-09-01..2026-09-24) [keep: ] quote: "wurde vom 1. bis einschließlich 24. September für 18.000 Personen konjunkturelle Kurzarbeit angezeigt."
  - p203 Employees receiving cyclical short-time work allowance in Germany, July 2026 (pr = **118** employees (2026-07-01..2026-07-31) [keep: ] quote: "wurde in diesem Monat für 118.000 Beschäftigte konjunkturelles Kurzarbeitergeld gezahlt"
  - p204 Year-on-year change in employees receiving cyclical short-time work allowance, J = **69** employees (2026-07-01..2026-07-31) [keep: ] quote: "Das waren 13.000 weniger als im Vormonat und rund 69.000 weniger als vor einem Jahr."
  - p205 Year-on-year change in employed persons in Germany (domestic concept), August 20 = **236** persons (2026-08-01..2026-08-31) [keep: ] quote: "Mit 45,58 Millionen Personen ist sie im Vergleich zum Vorjahr um 236.000 geringer."
  - p206 Year-on-year change in socially insured employment in Germany, July 2026 = **84** employees (2026-07-01..2026-07-31) [keep: ] quote: "Im Vergleich zum Vorjahr lag sie mit 34,68 Millionen Beschäftigten um 84.000 niedriger."
  - p207 Registered job vacancies at the BA in Germany, September 2026 = **660** jobs (2026-09-01..2026-09-30) [keep: ] quote: "Im September waren 660.000 Arbeitsstellen bei der BA gemeldet, 30.000 mehr als vor einem Jahr."
- `https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/08/PD26_N057_42.html` -> **live_dated** (page date 2026-08-14); points raw/verified 15/13
  - p208 Automotive industry employees in Germany, end of H1 2026 (level) = **691,500** as written "691 500", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Automotive employment level; no calibrated conversion to unemployment stock.] quote: "Mit 691 500 hat die Zahl der Beschäftigten in der Automobilindustrie einen weiteren Tiefstand erreicht"
  - p209 Automotive industry employees in Germany, year-on-year change, end of H1 2026 = **42,300** as written "42 300", value check pending persons (2025-07-01..2026-06-30) [DISCARD: Automotive employment change; no calibrated conversion to unemployment stock.] quote: "Zum Ende des 1. Halbjahres 2026 arbeiteten 42 300 weniger Beschäftigte in der Branche als noch ein Jahr zuvor"
  - p210 Manufacturing sector employees, year-on-year change, end of H1 2026 = **144,100** as written "144 100", value check pending persons (2025-07-01..2026-06-30) [DISCARD: Manufacturing employment change; no calibrated conversion.] quote: "Dies entsprach einem Rückgang von 144 100 oder 2,7 % binnen eines Jahres."
  - p211 Manufacturing sector employees, year-on-year percentage change, end of H1 2026 = **2.7** as written "2,7 %", value check pending % (2025-07-01..2026-06-30) [DISCARD: Manufacturing percent change; no calibrated conversion.] quote: "Dies entsprach einem Rückgang von 144 100 oder 2,7 % binnen eines Jahres."
  - p212 Motor vehicle and motor vehicle engine manufacturing employees, end of H1 2026 ( = **429,200** as written "429 200", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Motor vehicle employment level; no calibrated conversion.] quote: "Im Bereich der Herstellung von Kraftwagen und Kraftwagenmotoren waren mit insgesamt 429 200 Beschäftigten zum Ende des 1. Halbjahres 6,1 % weniger Personen beschäftigt als ein Jahr zuvor."
  - p213 Motor vehicle and engine manufacturing employees, year-on-year percentage change = **6.1** as written "6,1 %", value check pending % (2025-07-01..2026-06-30) [DISCARD: Motor vehicle percent change; no calibrated conversion.] quote: "Im Bereich der Herstellung von Kraftwagen und Kraftwagenmotoren waren mit insgesamt 429 200 Beschäftigten zum Ende des 1. Halbjahres 6,1 % weniger Personen beschäftigt als ein Jahr zuvor."
  - p214 Motor vehicle parts and accessories suppliers employees, end of H1 2026 (level) = **219,500** as written "219 500", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Parts supplier employment level; no calibrated conversion.] quote: "Im Zulieferbereich der Herstellung von Teilen und Zubehör für Kraftwagen betrug der Beschäftigtenrückgang 7,6 % auf zuletzt 219 500."
  - p215 Motor vehicle parts and accessories suppliers, year-on-year percentage change, e = **7.6** as written "7,6 %", value check pending % (2025-07-01..2026-06-30) [DISCARD: Parts supplier percent change; no calibrated conversion.] quote: "Im Zulieferbereich der Herstellung von Teilen und Zubehör für Kraftwagen betrug der Beschäftigtenrückgang 7,6 % auf zuletzt 219 500."
  - p216 Body, superstructure and trailer suppliers employees, end of H1 2026 (level) = **42,800** as written "42 800", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Body/trailer employment level; no calibrated conversion.] quote: "In der kleineren Zulieferbranche der Herstellung von Karosserien, Aufbauten und Anhängern stieg die Zahl der Beschäftigten um 10,0 % auf 42 800."
  - p217 Body, superstructure and trailer suppliers, year-on-year percentage change, end  = **10** as written "10,0 %", value check pending % (2025-07-01..2026-06-30) [DISCARD: Body/trailer percent change; no calibrated conversion.] quote: "In der kleineren Zulieferbranche der Herstellung von Karosserien, Aufbauten und Anhängern stieg die Zahl der Beschäftigten um 10,0 % auf 42 800."
  - p218 Mechanical engineering employees, end of H1 2026 (level) = **905,900** as written "905 900", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Mechanical engineering employment level; no calibrated conversion.] quote: "die zweitgrößte Industriebranche nach dem Maschinenbau mit 905 900 Beschäftigten zum Ende des 1. Halbjahres 2026"
  - p219 Metal products manufacturing employees, end of H1 2026 (level) = **471,700** as written "471 700", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Metal products employment level; no calibrated conversion.] quote: "In der Herstellung von Metallerzeugnissen sank sie binnen eines Jahres um 3,8 % auf 471 700 zum Ende des 1. Halbjahres 2026."
  - p220 Chemical industry employees, end of H1 2026 (level) = **312,000** as written "312 000", value check pending persons (2026-06-30..2026-06-30) [DISCARD: Chemical industry employment level; no calibrated conversion.] quote: "Höher als im Durchschnitt fiel der Beschäftigtenrückgang auch in der chemischen Industrie (-3,6 % auf 312 000)"
- `http://www.biaj.de/component/tortags/tag/arbeitsmarkt_arbeitslosigkeit.html?Itemid=166` -> **live_dated** (page date 2026-10-10); points raw/verified 15/0
- `https://www.zeit.de/thema/buergergeld` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 23 (number: ambiguous separators: '.' used as a thousands separator: 3; value_as_written not in quote as a whole number: 1; scale word 'million' not supported by quote or table header: 3; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; number: unknown scale word 'Millionen': 13; number: unknown scale word 'Milliarden': 2)

### b1 [own_history] seasonal pattern

Hypothesis: A multi-year national series of September-to-October unadjusted changes (2015-2025) would let us estimate the typical October seasonal increment directly rather than relying on the single 2025 observation (p20/p71/p86). This is the largest uncertainty in the seasonal route.

Queries issued by the searcher: statistik.arbeitsagentur.de Arbeitslose Bestand Monat September Oktober Zeitreihe; BA Arbeitsmarkt im Oktober 2025 Arbeitslosenzahl Vormonat September; "Arbeitslose" Deutschland Monatszahlen Tabelle 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 Oktober Bestand Zeitreihe; "Arbeitsmarkt im Oktober" 2019 Bundesagentur für Arbeit Pressemitteilung Arbeitslosenzahl September Vormonat

- `https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Fachstatistiken/Arbeitsuche-Arbeitslosigkeit-Unbeschaeftigung/Produkte/Zeitreihen-Arbeit` -> **dropped** (live http 404); points raw/verified -/-
- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/201912/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-201912-pdf.pdf` -> **live_dated** (page date 2019-12-01); points raw/verified 15/0
- `https://www.arbeitsagentur.de/datei/Arbeitsmarktbericht-09-18_ba019778.pdf` -> **live_dated** (page date 2018-09-28); points raw/verified 15/0
- `https://www.tagesspiegel.de/wirtschaft/arbeitsmarkt-talsohle-mit-klebstoff-arbeitsmarkt-verharrt-im-tief-14701007.html` -> **live_dated** (page date 2025-10-30); points raw/verified 15/11
  - p221 September-to-October 2025 change in German registered unemployed (unadjusted), p = **44,000** as written "44. 000", value check pending persons (2025-09-01..2025-10-31) [keep: ] quote: "2,911 Millionen Menschen arbeitslos gemeldet, 44. 000 weniger als im September"
  - p222 Year-over-year change in German registered unemployed, October 2025 vs October 2 = **120** persons (2025-10-01..2025-10-31) [keep: ] quote: "aber 120.000 mehr als noch im Oktober 2024"
  - p223 German unemployment rate (Arbeitslosenquote), October 2025, percent = **6.2** as written "6,2 Prozent", value check pending percent (2025-10-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote sank im Vergleich zum September um 0,1 Punkte auf 6,2 Prozent"
  - p224 Month-over-month change in German unemployment rate, September to October 2025,  = **0.1** as written "0,1 Punkte", value check pending percentage points (2025-09-01..2025-10-31) [keep: ] quote: "Die Arbeitslosenquote sank im Vergleich zum September um 0,1 Punkte auf 6,2 Prozent"
  - p225 Year-over-year change in German unemployment rate, October 2025 vs October 2024, = **0.2** as written "0,2 Punkte", value check pending percentage points (2025-10-01..2025-10-31) [keep: ] quote: "erhöhte sich aber im Vergleich zum Vorjahr um 0,2 Punkte"
  - p226 Registered open vacancies (offene Arbeitsplätze) in Germany, October 2025 = **623** vacancies (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober waren den Angaben der Bundesagentur zufolge 623.000 offene Arbeitsplätze gemeldet."
  - p227 Year-over-year change in registered open vacancies, October 2025 vs October 2024 = **66** vacancies (2025-10-01..2025-10-31) [keep: ] quote: "Das sind 66.000 weniger als vor einem Jahr."
  - p228 Recipients of Arbeitslosengeld in Germany, October 2025 = **984** persons (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober erhielten 984.000 Menschen in Deutschland Arbeitslosengeld, 104.000 mehr als ein Jahr zuvor."
  - p229 Year-over-year change in Arbeitslosengeld recipients, October 2025 vs October 20 = **104** persons (2025-10-01..2025-10-31) [keep: ] quote: "Im Oktober erhielten 984.000 Menschen in Deutschland Arbeitslosengeld, 104.000 mehr als ein Jahr zuvor."
  - p230 Year-over-year change in Bürgergeld recipients, October 2025 vs October 2024 = **134** persons (2025-10-01..2025-10-31) [keep: ] quote: "Das sind 134.000 weniger als im Oktober 2024."
  - p231 Share of employable-age population in Germany receiving basic security (Bürgerge = **7** as written "7,0 Prozent", value check pending percent (2025-10-01..2025-10-31) [keep: ] quote: "Insgesamt waren den Angaben zufolge 7,0 Prozent der in Deutschland lebenden Menschen im erwerbsfähigen Alter hilfebedürftig."
- dropped by code checks: 34 (number: ambiguous separators: '.' used as a thousands separator: 30; number: unknown scale word 'Millionen': 3; period year 2026 does not appear in the page text or URL (likely mis-dated): 1)

### b2 [related_series] trend/cycle

Hypothesis: A national seasonally adjusted unemployed level series (not just month-on-month changes) would let us anchor the October 2026 adjusted level and apply the October seasonal factor, providing an independent route to the target.

Queries issued by the searcher: statistik.arbeitsagentur.de Arbeitslose saisonbereinigt Bestand Tabelle; BA Arbeitslosenzahl saisonbereinigt Niveau 2026; "saisonbereinigt" "Arbeitslose" "2.9" 2026 Bestand Tabelle Monatsbericht; site:statistik.arbeitsagentur.de "Arbeitslose" "saisonbereinigt" "2026" "Bestand"; Bundesagentur für Arbeit Arbeitsmarkt September 2026 saisonbereinigt Arbeitslosenzahl

- `https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Interaktive-Statistiken/Zeitreihen/Lange-Zeitreihen-Nav.html?Fachstatistik%3Dalo%26DR_Ge` -> **live_dated** (page date 2025-01-01); points raw/verified 0/0
- `https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202605/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-202605-pdf.pdf` -> **live_dated** (page date 2026-05-01); points raw/verified 15/11
  - p232 Seasonally adjusted month-on-month change in registered unemployed, Germany, May = **-12** persons (2026-05-01..2026-05-31) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p233 Seasonally adjusted month-on-month change in registered unemployed, Germany, Apr = **19** persons (2026-04-01..2026-04-30) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p234 Seasonally adjusted month-on-month change in registered unemployed, Germany, Mar = **1** persons (2026-03-01..2026-03-31) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p235 Seasonally adjusted month-on-month change in registered unemployed, Germany, Feb = **1** persons (2026-02-01..2026-02-28) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p236 Seasonally adjusted month-on-month change in registered unemployed, Germany, Jan = **3** persons (2026-01-01..2026-01-31) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p237 Seasonally adjusted month-on-month change in registered unemployed, Germany, Dec = **1** persons (2025-12-01..2025-12-31) [keep: ] quote: "Arbeitslose -12.000 19.000 - 1.000 1.000 3.000 1.000"
  - p238 Seasonally adjusted unemployment rate (all civilian labour force), Germany, May  = **6.3** as written "6,3", value check pending percent (2026-05-01..2026-05-31) [keep: ] quote: "Arbeitslosenquote bezogen auf alle zivilen EP 6,3 6,4 6,3 6,3 6,3 6,3 6,3"
  - p239 Seasonally adjusted unemployment rate (all civilian labour force), Germany, Apri = **6.4** as written "6,4", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "Arbeitslosenquote bezogen auf alle zivilen EP 6,3 6,4 6,3 6,3 6,3 6,3 6,3"
  - p240 Seasonally adjusted unemployment rate (all civilian labour force), Germany, Marc = **6.3** as written "6,3", value check pending percent (2026-03-01..2026-03-31) [keep: ] quote: "Arbeitslosenquote bezogen auf alle zivilen EP 6,3 6,4 6,3 6,3 6,3 6,3 6,3"
  - p241 Seasonally adjusted unemployment rate (all civilian labour force), Germany, Febr = **6.3** as written "6,3", value check pending percent (2026-02-01..2026-02-28) [keep: ] quote: "Arbeitslosenquote bezogen auf alle zivilen EP 6,3 6,4 6,3 6,3 6,3 6,3 6,3"
  - p242 Seasonally adjusted unemployment rate (all civilian labour force), Germany, Janu = **6.3** as written "6,3", value check pending percent (2026-01-01..2026-01-31) [keep: ] quote: "Arbeitslosenquote bezogen auf alle zivilen EP 6,3 6,4 6,3 6,3 6,3 6,3 6,3"
- `https://www.arbeitsagentur.de/news/arbeitsmarkt` -> **live_dated** (page date 2026-09-30); points raw/verified 15/8
  - p243 National unemployed stock, Germany, September 2026, month-on-month change, not s = **67** persons (2026-09-01..2026-09-30) [keep: ] quote: "ist die Arbeitslosigkeit im September 2026 um 67.000 auf 2.994.000 zurückgegangen."
  - p244 National unemployed stock, Germany, September 2026, month-on-month change, seaso = **12** persons (2026-09-01..2026-09-30) [keep: ] quote: "Saisonbereinigt ist die Arbeitslosenzahl gegenüber dem Vormonat jedoch um 12.000 gestiegen."
  - p245 National unemployed stock, Germany, September 2026, year-on-year change, seasona = **40** persons (2026-09-01..2026-09-30) [keep: ] quote: "Verglichen mit dem September des letzten Jahres liegt sie um 40.000 höher."
  - p246 National unemployed stock, Germany, August 2026, month-on-month change, seasonal = **4** persons (2026-08-01..2026-08-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 4.000 höher."
  - p247 National unemployed stock, Germany, July 2026, month-on-month change, seasonally = **6** persons (2026-07-01..2026-07-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 6.000 höher."
  - p248 National unemployed stock, Germany, June 2026, month-on-month change, seasonally = **1** persons (2026-06-01..2026-06-30) [keep: ] quote: "Saisonbereinigt hat sie gegenüber dem Vormonat um 1.000 abgenommen."
  - p249 National unemployed stock, Germany, May 2026, month-on-month change, seasonally  = **12** persons (2026-05-01..2026-05-31) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat um 12.000 niedriger."
  - p250 National unemployed stock, Germany, April 2026, month-on-month change, seasonall = **20** persons (2026-04-01..2026-04-30) [keep: ] quote: "Saisonbereinigt ist sie gegenüber dem Vormonat jedoch um 20.000 gestiegen."
- `https://www.reuters.com/5f374b32b07b/de/hauslich/ba-deutsche-arbeitslosenzahl-steigt-auf-3007-millionen-2026-07-31/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 11 (number: ambiguous separators: '.' used as a thousands separator: 11)

### b3 [forecasts_markets] forecast

Hypothesis: Published autumn 2026 forecasts (IAB, Bundesbank, Sachverständigenrat) of Q4 2026 unemployment level or rate would constrain the trend adjustment and resolve whether the recent +12,000 adjusted monthly rise continues.

Queries issued by the searcher: IAB Prognose Arbeitslosigkeit 2026 Q4; Bundesbank Herbstprojektion 2026 Arbeitsmarkt Arbeitslosigkeit; IAB Prognose Herbstgutachten 2026 Arbeitslosigkeit 2027 Arbeitslose Millionen; Sachverständigenrat Jahresgutachten 2026 Arbeitslosenquote Prognose

- `https://doku.iab.de/kurzber/2026/kb2026-17.pdf` -> **live_dated** (page date 2026-09-22); points raw/verified 15/0
- `https://o-ton-arbeitsmarkt.de/2026/09/24/herbstgutachten-2026-und-iab-prognose/` -> **live_dated** (page date 2026-09-24); points raw/verified 15/3
  - p251 Unemployment rate in Germany, August = **6.4** as written "6,4 %", value check pending % (2026-08-01..2026-08-31) [DISCARD: Secondary aggregator gives August 2026 rate 6.4%, conflicting with BA/Destatis 6.5% (p42/p63); unreliable and redundant.] quote: "die Arbeitslosenquote betrug 6,4 %"
  - p252 Cyclical short-time work (Kurzarbeit) persons, Germany, June = **140** persons (2026-06-01..2026-06-30) [keep: ] quote: "Die konjunkturelle Kurzarbeit nahm in den vergangenen Monaten ab und lag mit 140.000 Personen im Juni etwa 55.000 Personen unter dem Vorjahreswert."
  - p253 Cyclical short-time work, year-on-year change, Germany, June = **55** persons (2026-06-01..2026-06-30) [keep: ] quote: "lag mit 140.000 Personen im Juni etwa 55.000 Personen unter dem Vorjahreswert"
- `https://www.br.de/nachrichten/wirtschaft/die-erwerbstaetigkeit-schumpft-obwohl-die-wirtschaft-waechst,VW7hY4A` -> **live_dated** (page date 2026-09-24); points raw/verified 7/0
- `https://web.gate.it/vi/news/calendar/151192` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 34 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4; scale word 'thousand' not supported by quote or table header: 6; period_end 2026-12-31 after as_of: 9; period_end 2027-12-31 after as_of: 9; value_as_written not in quote as a whole number: 1; number: unknown scale word 'Millionen': 2; period_end 2028-12-31 after as_of: 2; period_end missing or unparseable: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['germany unemployment', 'arbeitslosenzahl oktober', 'german jobless']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p11', 'p12', 'p146', 'p156', 'p174', 'p186'] All report the September 2026 unadjusted month-on-month change of -67,000 and the level 2,994,000; they trace to the same BA press release, so they are one measurement, not independent confirmation.
- corroborating: ['p1', 'p34', 'p157', 'p176', 'p187', 'p199'] Same BA September 2026 year-on-year change of +40,000; single underlying source.
- corroborating: ['p2', 'p32', 'p140', 'p158', 'p177', 'p189', 'p201'] September 2026 unadjusted rate 6.4%, same BA release.
- corroborating: ['p4', 'p13', 'p35', 'p139', 'p147', 'p159', 'p175', 'p190', 'p200'] Seasonally adjusted September 2026 change +12,000; same source.
- corroborating: ['p20', 'p71', 'p86'] October 2025 unadjusted change -44,000 to 2,911,000; same release.
- corroborating: ['p21', 'p72', 'p87'] October 2025 year-on-year +120,000; same release.
- corroborating: ['p25', 'p76', 'p91'] October 2025 seasonally adjusted change -1,000; same release.
- corroborating: ['p9', 'p37', 'p142', 'p165', 'p178', 'p196', 'p207'] September 2026 vacancies 660,000, +30,000 y/y; same BA release.
- corroborating: ['p38', 'p167', 'p173', 'p198'] BA-X 104 in September 2026; same source.
- corroborating: ['p161', 'p170', 'p192', 'p202'] Kurzarbeit notifications 18,000 for 1-24 September 2026; same source.
- corroborating: ['p162', 'p193', 'p203'] Realised Kurzarbeit 118,000 in July 2026; same source.
- corroborating: ['p163', 'p194'] July 2026 Kurzarbeit -13,000 m/m; same source.
- corroborating: ['p164', 'p195', 'p204'] July 2026 Kurzarbeit -69,000 y/y; same source.
- corroborating: ['p60', 'p148'] August 2026 unadjusted change +54,000 to 3,061,000; same release.
- corroborating: ['p61', 'p149'] August 2026 seasonally adjusted +4,000; same release.
- corroborating: ['p62', 'p41'] August 2026 year-on-year +36,000; same release.
- corroborating: ['p63', 'p42'] August 2026 unadjusted rate 6.5%; same release.
- corroborating: ['p50', 'p150'] July 2026 unadjusted +71,000 to 3,007,000; same release.
- corroborating: ['p51', 'p151'] July 2026 seasonally adjusted +6,000; same release.
- corroborating: ['p52', 'p150'] July 2026 year-on-year +28,000; same release.
- corroborating: ['p53', 'p64'] July 2026 unadjusted rate 6.4%; same release.
- corroborating: ['p8', 'p39'] ILO rate August 2026 4.3%; same source.
- corroborating: ['p27', 'p77'] ILO rate September 2025 4.1%; same source.
- corroborating: ['p68', 'p69'] December 2025 ILO 3.6% and registered 6.2% (2.91m); same source, different definitions.
- corroborating: ['p11', 'p138', 'p146'] September 2026 unadjusted change -67,000; same release.
- corroborating: ['p20', 'p25'] October 2025: unadjusted -44,000 while seasonally adjusted -1,000, implying a seasonal factor of roughly -43,000 for Sep-Oct; consistent with a seasonal decline in October.
- corroborating: ['p99', 'p100', 'p101'] Bielefeld local stock series Aug-Oct 2025; local analogue only, not national.
- corroborating: ['p114', 'p115', 'p116'] Chemnitz local stock series Aug-Oct 2025; local analogue only.
- corroborating: ['p102', 'p103', 'p104', 'p105', 'p106', 'p107'] Bielefeld inflow/outflow series; local analogue for flow decomposition.
- corroborating: ['p117', 'p118', 'p119', 'p120', 'p121', 'p122'] Chemnitz inflow/outflow series; local analogue.
- corroborating: ['p132', 'p133', 'p134', 'p135', 'p136', 'p137'] Braunschweig October net flows 2014/2015; local analogue.
- corroborating: ['p129', 'p130', 'p131'] Bund December 2015 changes; old national analogue, not October.
- corroborating: ['p84', 'p85'] Forecast/contextual material on 2025-2026 unemployment; not a direct October 2026 level.
- corroborating: ['p208', 'p209', 'p210', 'p211', 'p212', 'p213', 'p214', 'p215', 'p216', 'p217', 'p218', 'p219', 'p220'] Industrial/automotive employment decline evidence; supports upward pressure on unemployment but no direct October level.
- corroborating: ['p79', 'p80', 'p93', 'p94', 'p95'] October 2025 Kurzarbeit context; older period analogue.
- corroborating: ['p28', 'p29', 'p30', 'p81', 'p96', 'p97'] October 2025 vacancy/BA-X context; older period analogue.
- corroborating: ['p31', 'p82', 'p98'] October 2025 Arbeitslosengeld recipients; same release.
- corroborating: ['p83'] Harmonised unemployment m/m change August 2026; third-party aggregator, weak.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p11', 'p146', 'p156', 'p174', 'p186', 'p243'] All report the same BA September 2026 unadjusted month-on-month change of -67,000 to a stock of 2,994,000; they share the BA press release as underlying source, so this is one measurement, not indepen
- corroborating: ['p4', 'p13', 'p35', 'p139', 'p147', 'p159', 'p175', 'p190', 'p200', 'p244'] Same BA seasonally adjusted September 2026 change of +12,000, repeated across outlets; single underlying measurement.
- corroborating: ['p1', 'p12', 'p34', 'p157', 'p176', 'p187', 'p199', 'p245'] September 2026 year-on-year change of +40,000 (p12 gives the precise 39,668); one BA measurement.
- corroborating: ['p2', 'p32', 'p140', 'p158', 'p177', 'p189', 'p201'] September 2026 unadjusted rate 6.4%, down 0.1pp; single BA figure.
- corroborating: ['p20', 'p71', 'p86', 'p221'] October 2025 unadjusted change of -44,000 to 2,911,000; same BA release. p221 confirms the -44,000 September-to-October 2025 change, which is the only observed seasonal step available.
- corroborating: ['p21', 'p72', 'p87', 'p222'] October 2025 year-on-year change +120,000; same BA release.
- corroborating: ['p25', 'p76', 'p91'] October 2025 seasonally adjusted change -1,000; same BA release.
- corroborating: ['p9', 'p10', 'p37', 'p142', 'p165', 'p166', 'p178', 'p179', 'p196', 'p197', 'p207'] September 2026 vacancies 660,000, +30,000 y/y; one BA measurement repeated. Note the sign convention: vacancies are rising, which is a mildly labour-demand-positive signal, not a weakening one.
- corroborating: ['p38', 'p167', 'p173', 'p198'] BA-X 104 in September 2026, +1 point; one index reading.
- corroborating: ['p161', 'p170', 'p192', 'p202'] 18,000 Kurzarbeit notifications 1-24 September 2026; one BA figure.
- corroborating: ['p162', 'p163', 'p164', 'p193', 'p194', 'p195', 'p203', 'p204'] July 2026 realised Kurzarbeit 118,000, -13,000 m/m and -69,000 y/y; one BA figure. Falling Kurzarbeit is a mildly favourable signal, contrary to the d7 'rising Kurzarbeit' premise.
- corroborating: ['p8', 'p39'] ILO rate August 2026 4.3%; same Destatis/BA figure. Different definition from registered unemployment, so usable only as a cross-check, not a substitute.
- corroborating: ['p60', 'p148'] August 2026 unadjusted change +54,000 to 3,061,000; consistent with p11's August level.
- corroborating: ['p50', 'p150'] July 2026 unadjusted change +71,000 to 3,007,000.
- corroborating: ['p11', 'p60', 'p50', 'p152', 'p154'] Monthly unadjusted levels chain consistently: May 2,950,000; June 2,936,000; July 3,007,000; August 3,061,000; September 2,994,000. This gives a coherent 2026 path and confirms p11's level.
- corroborating: ['p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p232', 'p233', 'p234', 'p235', 'p236', 'p237', 'p246', 'p247', 'p248', 'p249', 'p250'] Seasonally adjusted monthly changes Dec 2025-Aug 2026 cluster around +1,000 to +20,000 with a positive drift; supports a modest upward trend adjustment. Overlapping vintages (p14-p19 vs p232-p237) are
- corroborating: ['p68', 'p69'] December 2025: ILO 1.60m/3.6% vs registered 2.91m/6.2%. Confirms the registered series runs roughly 1.8x the ILO level; useful only as a ratio sanity check, not a direct input.
- conflicting: ['p251', 'p42', 'p63'] p251 gives August 2026 rate 6.4% while p42/p63 give 6.5%. p251 is a secondary aggregator page; the BA/Destatis figures (6.5%) are authoritative. p251 is not used numerically.
- corroborating: ['p79', 'p93', 'p161', 'p170', 'p192', 'p202'] Kurzarbeit notification counts for October 2025 (37,000) and September 2026 (18,000) are the same administrative flow series; the decline indicates easing rather than rising short-time work.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September-to-October 2026 unadjusted change in national registered unemployed, as a factor on the observed 2025 step | 0.9 | 0.4..1.6 | 0.4..1.6 | dimensionless | unused | Only one observed September-to-October step exists (p20/p221: -44,000 in 2025). October usually brings a small decline as summer-job and training-contract inflows fade. The 2026 labour market is slightly weaker (y/y +40,000 in September, p1; adjusted drift +12,000, p4), so the decline is assumed mar | The 2026 September-to-October seasonal pattern resembles 2025 and no large shock hits in October. | Evidence that October 2026 inflows from training-contract endings are unusually large, or a BA statement of a rising October stock. |
| a2 | Year-on-year change in national unadjusted registered unemployed, October 2026 vs October 2025, as a factor on the observed September 2026 y/y change | 1 | 0.5..1.8 | 0.5..1.8 | dimensionless | unused | September 2026 y/y change was +40,000 (p1/p12) and the seasonally adjusted series has drifted up by roughly +1,000 to +20,000 per month through 2026 (p14-p19, p232-p237), so October y/y is assumed near the September value with a modest upward tilt. Factor 1.0 on the +40,000 September y/y; range allo | The y/y trend of late summer 2026 persists into October. | A sharp autumn 2026 deterioration or improvement in the adjusted series (e.g. adjusted change far outside +1,000 to +20,000). |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input p11 must be positive for lognormal sampling |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input p20 must be positive for lognormal sampling |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **n/a** person, 80% interval [n/a, n/a] person, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **no_candidates**. target period ends 2026-10-31, after as_of: it cannot have been published yet


## Final answer

No estimate: no estimation method could be computed from the verified evidence.
